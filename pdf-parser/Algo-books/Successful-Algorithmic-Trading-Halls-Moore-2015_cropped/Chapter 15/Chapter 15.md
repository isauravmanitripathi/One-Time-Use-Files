## Chapter 15

# Trading Strategy Implementation

In this chapter we are going to consider the full implementation of trading strategies using the aforementioned event-driven backtesting system. In particular we will generate equity curves for all trading strategies using notional portfolio amounts, thus simulating the concepts of margin/leverage, which is a far more realistic approach compared to vectorised/returns based approaches.

The rst set of strategies are able to be carried out with freely available data, either from Yahoo Finance, Google Finance or Quandl. These strategies are suitable for long-term algorithmic traders who may wish to only study the trade signal generation aspect of the strategy or even the full end-to-end system. Such strategies often possess smaller Sharpe ratios, but are far easier to implement and execute.

The latter strategy is carried out using intraday equities data. This data is often not freely available and a commercial data vendor is usually necessary to provide sucient quality and quantity of data. I myself use DTN IQFeed for intraday bars. Such strategies often possess much larger Sharpe ratios, but require more sophisticated implementation as the high frequency requires extensive automation.

We will see that our rst two attempts at creating a trading strategy on interday data are not altogether successful. It can be challenging to come up with a protable trading strategy on interday data once transaction costs have been taken into account. The latter is something that many texts on algorithmic trading tend to leave out. However, it is my belief that as many factors as possible must be added to the backtest in order to minimises surprises going forward.

In addition, this book is primarily about how to eectively create a realistic interday or intraday backtesting system (as well as a live execution platform) and less about particular individual strategies. It is far harder to create a realistic robust backtester than it is to nd trading strategies on the internet! While the rst two strategies presented are not particularly attractive, the latter strategy (on intraday data) performs well and gives us condence in using higher frequency data.

## 15.1 Moving Average Crossover Strategy

I'm quite fond of the Moving Average Crossover technical system because it is the rst nontrivial strategy that is extremely handy for testing a new backtesting implementation. On a daily timeframe, over a number of years, with long lookback periods, few signals are generated on a single stock and thus it is easy to manually verify that the system is behaving as would be expected.

In order to actually generate such a simulation based on the prior backtesting code we need to subclass the Strategy object as described in the previous chapter to create the MovingAverageCrossStrategy object, which will contain the logic of the simple moving averages and the generation of trading signals.

In addition we need to create the \_\_main\_\_ function that will load the Backtest object and actually encapsulate the execution of the program. The following le, mac.py, contains both of these objects.

The rst task, as always, is to correctly import the necessary components. We are importing nearly all of the objects that have been described in the previous chapter:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# mac.py
from __future__ import print_function
import datetime
import numpy as np
import pandas as pd
import statsmodels.api as sm
from strategy import Strategy
from event import SignalEvent
from backtest import Backtest
from data import HistoricCSVDataHandler
from execution import SimulatedExecutionHandler
```

**from** portfolio **import** Portfolio

Now we turn to the creation of the MovingAverageCrossStrategy. The strategy requires both the bars DataHandler, the events Event Queue and the lookback periods for the simple moving averages that are going to be employed within the strategy. I've chosen 100 and 400 as the "short" and "long" lookback periods for this strategy.

The nal attribute, bought, is used to tell the Strategy when the backtest is actually "in the market". Entry signals are only generated if this is "OUT" and exit signals are only ever generated if this is "LONG" or "SHORT":

```
# mac.py
```

```
class MovingAverageCrossStrategy(Strategy):
    """
    Carries out a basic Moving Average Crossover strategy with a
    short/long simple weighted moving average. Default short/long
    windows are 100/400 periods respectively.
    """
    def __init__(
        self, bars, events, short_window=100, long_window=400
    ):
        """
        Initialises the Moving Average Cross Strategy.
        Parameters:
        bars - The DataHandler object that provides bar information
        events - The Event Queue object.
        short_window - The short moving average lookback.
        long_window - The long moving average lookback.
        """
        self.bars = bars
        self.symbol_list = self.bars.symbol_list
        self.events = events
        self.short_window = short_window
        self.long_window = long_window
```

# Set to True if a symbol is in the market self.bought = self.\_calculate\_initial\_bought()

Since the strategy begins out of the market we set the initial "bought" value to be "OUT", for each symbol:

```
# mac.py
    def _calculate_initial_bought(self):
        """
        Adds keys to the bought dictionary for all symbols
        and sets them to 'OUT'.
        """
        bought = {}
        for s in self.symbol_list:
            bought[s] = 'OUT'
        return bought
```

The core of the strategy is the calculate\_signals method. It reacts to a MarketEvent object and for each symbol traded obtains the latest N bar closing prices, where N is equal to the largest lookback period.

It then calculates both the short and long period simple moving averages. The rule of the strategy is to enter the market (go long a stock) when the short moving average value exceeds the long moving average value. Conversely, if the long moving average value exceeds the short moving average value the strategy is told to exit the market.

This logic is handled by placing a SignalEvent object on the events Event Queue in each of the respective situations and then updating the "bought" attribute (per symbol) to be "LONG" or "OUT", respectively. Since this is a long-only strategy, we won't be considering "SHORT" positions:

```
# mac.py
```

```
def calculate_signals(self, event):
    """
    Generates a new set of signals based on the MAC
    SMA with the short window crossing the long window
    meaning a long entry and vice versa for a short entry.
    Parameters
    event - A MarketEvent object.
    """
    if event.type == 'MARKET':
        for s in self.symbol_list:
            bars = self.bars.get_latest_bars_values(
                s, "adj_close", N=self.long_window
            )
            bar_date = self.bars.get_latest_bar_datetime(s)
            if bars is not None and bars != []:
                short_sma = np.mean(bars[-self.short_window:])
                long_sma = np.mean(bars[-self.long_window:])
                symbol = s
                dt = datetime.datetime.utcnow()
                sig_dir = ""
                if short_sma > long_sma and self.bought[s] == "OUT":
                    print("LONG: %s" % bar_date)
                    sig_dir = 'LONG'
```

```
signal = SignalEvent(1, symbol, dt, sig_dir, 1.0)
    self.events.put(signal)
    self.bought[s] = 'LONG'
elif short_sma < long_sma and self.bought[s] == "LONG":
    print("SHORT: %s" % bar_date)
    sig_dir = 'EXIT'
    signal = SignalEvent(1, symbol, dt, sig_dir, 1.0)
    self.events.put(signal)
    self.bought[s] = 'OUT'
```

That concludes the MovingAverageCrossStrategy object implementation. The nal task of the entire backtesting system is populate a \_\_main\_\_ method in mac.py to actually execute the backtest.

Firstly, make sure to change the value of csv\_dir to the absolute path of your CSV le directory for the nancial data. You will also need to download the CSV le of the AAPL stock (from Yahoo Finance), which is given by the following link (for Jan 1st 1990 to Jan 1st 2002), since this is the stock we will be testing the strategy on:

http://ichart.nance.yahoo.com/table.csv?s=AAPL&a=00&b=1&c=1990&d=00&e=1 &f=2002&g=d&ignore=.csv

Make sure to place this le in the path pointed to from the main function in csv\_dir.

The \_\_main\_\_ function simply instantiates a new backtest object and then calls the simulate\_trading method on it to execute it:

```
# mac.py
```

```
if __name__ == "__main__":
    csv_dir = '/path/to/your/csv/file' # CHANGE THIS!
    symbol_list = ['AAPL']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(1990, 1, 1, 0, 0, 0)
    backtest = Backtest(
        csv_dir, symbol_list, initial_capital, heartbeat,
        start_date, HistoricCSVDataHandler, SimulatedExecutionHandler,
        Portfolio, MovingAverageCrossStrategy
    )
    backtest.simulate_trading()
```

To run the code, make sure you have already set up a Python environment (as described in the previous chapters) and then navigate the directory where your code is stored. You should simply be able to run:

#### python mac.py

You will see the following listing (truncated due to the bar count printout!):

.. .. 3029 3030 Creating summary stats... Creating equity curve... AAPL cash commission total returns equity\_curve drawdown datetime 2001-12-18 0 99211 13 99211 0 0.99211 0.025383 2001-12-19 0 99211 13 99211 0 0.99211 0.025383 2001-12-20 0 99211 13 99211 0 0.99211 0.025383 2001-12-21 0 99211 13 99211 0 0.99211 0.025383

| 2001-12-24                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
|--------------------------------|----------------------------|-------|----|-------|---|---------|----------|
| 2001-12-26                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
| 2001-12-27                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
| 2001-12-28                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
| 2001-12-31                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
| 2001-12-31                     | 0                          | 99211 | 13 | 99211 | 0 | 0.99211 | 0.025383 |
| [('Total Return', '-0.79%'),   |                            |       |    |       |   |         |          |
| ('Sharpe Ratio', '-0.09'),     |                            |       |    |       |   |         |          |
|                                | ('Max Drawdown', '2.56%'), |       |    |       |   |         |          |
| ('Drawdown Duration', '2312')] |                            |       |    |       |   |         |          |
| Signals: 10                    |                            |       |    |       |   |         |          |
| Orders: 10                     |                            |       |    |       |   |         |          |
| Fills: 10                      |                            |       |    |       |   |         |          |
|                                |                            |       |    |       |   |         |          |

The performance of this strategy can be seen in Fig 15.1:

![](_page_4_Figure_2.jpeg)

Figure 15.1: Equity Curve, Daily Returns and Drawdowns for the Moving Average Crossover strategy

Evidently the returns and Sharpe Ratio are not stellar for AAPL stock on this particular set of technical indicators! Clearly we have some work to do in the next set of strategies to nd a system that can generate positive performance.

## 15.2 S&P500 Forecasting Trade

In this sectiuon we will consider a trading strategy built around the forecasting engine discussed in prior chapters. We will attempt to trade o the predictions made by a stock market forecaster.

We are going to attempt to forecast SPY, which is the ETF that tracks the value of the S&P500. Ultimately we want to answer the question as to whether a basic forecasting algorithm using lagged price data, with slight predictive performance, provides us with any benet over a buy-and-hold strategy.

The rules for this strategy are as follows:

- 1. Fit a forecasting model to a subset of S&P500 data. This could be Logistic Regression, a Discriminant Analyser (Linear or Quadratic), a Support Vector Machine or a Random Forest. The procedure to do this was outlined in the Forecasting chapter.
- 2. Use two prior lags of adjusted closing returns data as a predictor for tomorrow's returns. If the returns are predicted as positive then go long. If the returns are predicted as negative then exit. We're not going to consider short selling for this particular strategy.

#### Implementation

For this strategy we are going to create the snp\_forecast.py le and import the following necessary libraries:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# snp_forecast.py
from __future__ import print_function
import datetime
import pandas as pd
from sklearn.qda import QDA
from strategy import Strategy
from event import SignalEvent
from backtest import Backtest
from data import HistoricCSVDataHandler
from execution import SimulatedExecutionHandler
from portfolio import Portfolio
from create_lagged_series import create_lagged_series
```

We have imported Pandas and Scikit-Learn in order to carry out the tting procedure for the supervised classier model. We have also imported the necessary classes from the event-driven backtester. Finally, we have imported the create\_lagged\_series function, which we used in the Forecasting chapter.

The next step is to create the SPYDailyForecastStrategy as a subclass of the Strategy abstract base class. Since we will "hardcode" the parameters of the strategy directly into the class, for simplicity, the only parameters necessary for the \_\_init\_\_ constructor are the bars data handler and the events queue.

We set the self.model\_\*\*\* start/end/test dates as datetime objects and then tell the class that we are out of the market (self.long\_market = False). Finally, we set self.model to be the trained model from the create\_symbol\_forecast\_model below:

```
# snp_forecast.py
```

```
class SPYDailyForecastStrategy(Strategy):
    """
```

```
S&P500 forecast strategy. It uses a Quadratic Discriminant
Analyser to predict the returns for a subsequent time
period and then generated long/exit signals based on the
prediction.
"""
def __init__(self, bars, events):
    self.bars = bars
    self.symbol_list = self.bars.symbol_list
    self.events = events
    self.datetime_now = datetime.datetime.utcnow()
    self.model_start_date = datetime.datetime(2001,1,10)
    self.model_end_date = datetime.datetime(2005,12,31)
    self.model_start_test_date = datetime.datetime(2005,1,1)
    self.long_market = False
    self.short_market = False
    self.bar_index = 0
    self.model = self.create_symbol_forecast_model()
```

Here we dene the create\_symbol\_forecast\_model. It essentially calls the create\_lagged\_series function, which produces a Pandas DataFrame with ve daily returns lags for each current predictor. We then consider only the two most recent of these lags. This is because we are making the modelling decision that the predictive power of earlier lags is likely to be minimal.

At this stage we create the training and test data, the latter of which can be used to test our model if we wish. I have opted to not output testing data, since we have already trained the model before in the Forecasting chapter. Finally we t the training data to the Quadratic Discriminant Analyser and then return the model.

Note that we could easily replace the model with a Random Forest, Support Vector Machine or Logistic Regression, for instance. All we need to do is import the correct library from Scikit-Learn and simply replace the model = QDA() line:

```
# snp_forecast.py
```

```
def create_symbol_forecast_model(self):
    # Create a lagged series of the S&P500 US stock market index
    snpret = create_lagged_series(
        self.symbol_list[0], self.model_start_date,
        self.model_end_date, lags=5
    )
    # Use the prior two days of returns as predictor
    # values, with direction as the response
    X = snpret[["Lag1","Lag2"]]
    y = snpret["Direction"]
    # Create training and test sets
    start_test = self.model_start_test_date
    X_train = X[X.index < start_test]
    X_test = X[X.index >= start_test]
    y_train = y[y.index < start_test]
    y_test = y[y.index >= start_test]
    model = QDA()
    model.fit(X_train, y_train)
    return model
```

At this stage we are ready to override the calculate\_signals method of the Strategy base class. We rstly calculate some convenience parameters that enter our SignalEvent object and then only generate a set of signals if we have received a MarketEvent object (a basic sanity check).

We wait for ve bars to have elapsed (i.e. ve days in this strategy!) and then obtain the lagged returns values. We then wrap these values in a Pandas Series so that the predict method of the model will function correctly. We then calculate a prediction, which manifests itself as a +1 or -1.

If the prediction is a +1 and we are not already long the market, we create a SignalEvent to go long and let the class know we are now in the market. If the prediction is -1 and we are long the market, then we simply exit the market:

```
# snp_forecast.py
```

```
def calculate_signals(self, event):
    """
    Calculate the SignalEvents based on market data.
    """
    sym = self.symbol_list[0]
    dt = self.datetime_now
    if event.type == 'MARKET':
        self.bar_index += 1
        if self.bar_index > 5:
            lags = self.bars.get_latest_bars_values(
                self.symbol_list[0], "returns", N=3
            )
            pred_series = pd.Series(
                {
                    'Lag1': lags[1]*100.0,
                    'Lag2': lags[2]*100.0
                }
            )
            pred = self.model.predict(pred_series)
            if pred > 0 and not self.long_market:
                self.long_market = True
                signal = SignalEvent(1, sym, dt, 'LONG', 1.0)
                self.events.put(signal)
            if pred < 0 and self.long_market:
                self.long_market = False
                signal = SignalEvent(1, sym, dt, 'EXIT', 1.0)
                self.events.put(signal)
```

In order to run the strategy you will need to download a CSV le from Yahoo Finance for SPY and place it in a suitable directory (note that you will need to change your path below!). We then wrap the backtest up via the Backtest class and carry out the test by calling simulate\_trading:

```
# snp_forecast.py
```

```
if __name__ == "__main__":
    csv_dir = '/path/to/your/csv/file' # CHANGE THIS!
    symbol_list = ['SPY']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2006,1,3)
    backtest = Backtest(
```

```
csv_dir, symbol_list, initial_capital, heartbeat,
    start_date, HistoricCSVDataHandler, SimulatedExecutionHandler,
    Portfolio, SPYDailyForecastStrategy
)
```

```
backtest.simulate_trading()
```

The output of the strategy is as follows and is net of transaction costs:

```
..
..
2209
2210
Creating summary stats...
Creating equity curve...
            SPY cash commission total returns equity_curve \
datetime
2014-09-29 19754 90563.3 349.7 110317.3 -0.000326 1.103173
2014-09-30 19702 90563.3 349.7 110265.3 -0.000471 1.102653
2014-10-01 19435 90563.3 349.7 109998.3 -0.002421 1.099983
2014-10-02 19438 90563.3 349.7 110001.3 0.000027 1.100013
2014-10-03 19652 90563.3 349.7 110215.3 0.001945 1.102153
2014-10-06 19629 90563.3 349.7 110192.3 -0.000209 1.101923
2014-10-07 19326 90563.3 349.7 109889.3 -0.002750 1.098893
2014-10-08 19664 90563.3 349.7 110227.3 0.003076 1.102273
2014-10-09 19274 90563.3 349.7 109837.3 -0.003538 1.098373
2014-10-09 0 109836.0 351.0 109836.0 -0.000012 1.098360
          drawdown
datetime
2014-09-29 0.003340
2014-09-30 0.003860
2014-10-01 0.006530
2014-10-02 0.006500
2014-10-03 0.004360
2014-10-06 0.004590
2014-10-07 0.007620
2014-10-08 0.004240
2014-10-09 0.008140
2014-10-09 0.008153
[('Total Return', '9.84%'),
('Sharpe Ratio', '0.54'),
('Max Drawdown', '5.99%'),
('Drawdown Duration', '811')]
Signals: 270
Orders: 270
Fills: 270
```

The following visualisation in Fig 15.2 shows the Equity Curve, the Daily Returns and the Drawdown of the strategy as a function of time:

Note immediately that the performance is not great! We have a Sharpe Ratio < 1 but a reasonable drawdown of just under 6%. It turns out that if we had simply bought and held SPY in this time period we would have performed similarly, if slightly worse.

Hence we have not actually gained very much from our predictive strategy once transaction costs are included. I specically wanted to include this example because it uses an "end to end" realistic implementation of such a strategy that takes into account conservative, realistic transaction costs. As can be seen it is not easy to make a predictive forecaster on daily data that produces good performance!

![](_page_9_Figure_0.jpeg)

Figure 15.2: Equity Curve, Daily Returns and Drawdowns for the SPY forecast strategy

Our nal strategy will make use of other time series and a higher frequency. We will see that performance can be improved dramatically after modifying certain aspects of the system.

## 15.3 Mean-Reverting Equity Pairs Trade

In order to seek higher Sharpe ratios for our trading, we need to consider higher-frequency intraday strategies.

The rst major issue is that obtaining data is signicantly less straightforward because high quality intraday data is usually not free. As stated above I use DTN IQFeed for intraday minutely bars and thus you will need your own DTN account to obtain the data required for this strategy.

The second issue is that backtesting simulations take substantially longer, especially with the event-driven model that we have constructed here. Once we begin considering a backtest of a diversied portfolio of minutely data spanning years, and then performing any parameter optimisation, we rapidly realise that simulations can take hours or even days to calculate on a modern desktop PC. This will need to be factored in to your research process.

The third issue is that live execution will now need to be fully automated since we are edging into higher-frequency trading. This means that such execution environments and code must be highly reliable and bug-free, otherwise the potential for signicant losses can occur.

This strategy expands on the previous interday strategy above to make use of intraday data. In particular we are going to use minutely OHLCV bars, as opposed to daily OHLCV.

The rules for the strategy are straightforward:

1. Identify a pair of equities that possess a residuals time series which has been statistically identied as mean-reverting. In this case, I have found two energy sector US equities with tickers AREX and WLL.

- 2. Create the residuals time series of the pair by performing a rolling linear regression, for a particular lookback window, via the ordinary least squares (OLS) algorithm. This lookback period is a parameter to be optimised.
- 3. Create a rolling z-score of the residuals time series of the same lookback period and use this to determine entry/exit thresholds for trading signals.
- 4. If the upper threshold is exceeded when not in the market then enter the market (long or short depending on direction of threshold excess). If the lower threshold is exceeded when in the market, exit the market. Once again, the upper and lower thresholds are parameters to be optimised.

Indeed we could have used the Cointegrated Augmented Dickey-Fuller (CADF) test to identify an even more accurate hedging parameter. This would make an interesting extension of the strategy.

#### Implementation

The rst step, as always, is to import the necessary libraries. We require pandas for the rolling\_apply method, which is used to apply the z-score calculation with a lookback window on a rolling basis. We import statsmodels because it provides a means of calculating the ordinary least squares (OLS) algorithm for the linear regression, necessary to obtain the hedging ratio for the construction of the residuals.

We also require a slightly modied DataHandler and Portfolio in order to carry out minutely bars trading on DTN IQFeed data. In order to create these les you can simply copy all of the code in portfolio.py and data.py into the new les hft\_portfolio.py and hft\_data.py respectively and then modify the necessary sections, which I will outline below.

Here is the import listing for intraday\_mr.py:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# intraday_mr.py
from __future__ import print_function
import datetime
import numpy as np
import pandas as pd
import statsmodels.api as sm
from strategy import Strategy
from event import SignalEvent
from backtest import Backtest
from hft_data import HistoricCSVDataHandlerHFT
from hft_portfolio import PortfolioHFT
from execution import SimulatedExecutionHandler
```

In the following snippet we create the IntradayOLSMRStrategy class derived from the Strategy abstract base class. The constructor \_\_init\_\_ method requires access to the bars historical data provider, the events queue, a zscore\_low threshold and a zscore\_high threshold, used to determine when the residual series between the two pairs is mean-reverting.

In addition, we specify the OLS lookback window (set to 100 here), which is a parameter that is subject to potential optimisation. At the start of the simulation we are neither long or short the market, so we set both self.long\_market and self.short\_market equal to False:

```
class IntradayOLSMRStrategy(Strategy):
    """
    Uses ordinary least squares (OLS) to perform a rolling linear
    regression to determine the hedge ratio between a pair of equities.
    The z-score of the residuals time series is then calculated in a
    rolling fashion and if it exceeds an interval of thresholds
    (defaulting to [0.5, 3.0]) then a long/short signal pair are generated
    (for the high threshold) or an exit signal pair are generated (for the
    low threshold).
    """
    def __init__(
        self, bars, events, ols_window=100,
        zscore_low=0.5, zscore_high=3.0
    ):
        """
        Initialises the stat arb strategy.
        Parameters:
        bars - The DataHandler object that provides bar information
        events - The Event Queue object.
        """
        self.bars = bars
        self.symbol_list = self.bars.symbol_list
        self.events = events
        self.ols_window = ols_window
        self.zscore_low = zscore_low
        self.zscore_high = zscore_high
        self.pair = ('AREX', 'WLL')
        self.datetime = datetime.datetime.utcnow()
        self.long_market = False
        self.short_market = False
```

The following method, calculate\_xy\_signals, takes the current zscore (from the rolling calculation performed below) and determines whether new trading signals need to be generated. These signals are then returned.

There are four potential states that we may be interested in. They are:

- 1. Long the market and below the negative zscore higher threshold
- 2. Long the market and between the absolute value of the zscore lower threshold
- 3. Short the market and above the positive zscore higher threshold
- 4. Short the market and between the absolute value of the zscore lower threshold

In either case it is necessary to generate two signals, one for the rst component of the pair (AREX) and one for the second component of the pair (WLL). If none of these conditions are reached, then a pair of None values are returned:

```
# intraday_mr.py
```

```
def calculate_xy_signals(self, zscore_last):
    """
    Calculates the actual x, y signal pairings
    to be sent to the signal generator.
```

```
175
```

```
Parameters
zscore_last - The current zscore to test against
"""
y_signal = None
x_signal = None
p0 = self.pair[0]
p1 = self.pair[1]
dt = self.datetime
hr = abs(self.hedge_ratio)
# If we're long the market and below the
# negative of the high zscore threshold
if zscore_last <= -self.zscore_high and not self.long_market:
    self.long_market = True
    y_signal = SignalEvent(1, p0, dt, 'LONG', 1.0)
    x_signal = SignalEvent(1, p1, dt, 'SHORT', hr)
# If we're long the market and between the
# absolute value of the low zscore threshold
if abs(zscore_last) <= self.zscore_low and self.long_market:
    self.long_market = False
    y_signal = SignalEvent(1, p0, dt, 'EXIT', 1.0)
    x_signal = SignalEvent(1, p1, dt, 'EXIT', 1.0)
# If we're short the market and above
# the high zscore threshold
if zscore_last >= self.zscore_high and not self.short_market:
    self.short_market = True
    y_signal = SignalEvent(1, p0, dt, 'SHORT', 1.0)
    x_signal = SignalEvent(1, p1, dt, 'LONG', hr)
# If we're short the market and between the
# absolute value of the low zscore threshold
if abs(zscore_last) <= self.zscore_low and self.short_market:
    self.short_market = False
    y_signal = SignalEvent(1, p0, dt, 'EXIT', 1.0)
    x_signal = SignalEvent(1, p1, dt, 'EXIT', 1.0)
```

**return** y\_signal, x\_signal

The following method, calculate\_signals\_for\_pairs obtains the latest set of bars for each component of the pair (in this case 100 bars) and uses them to construct an ordinary least squares based linear regression. This allows identication of the hedge ratio, necessary for the construction of the residuals time series.

Once the hedge ratio is constructed, a spread series of residuals is constructed. The next step is to calculate the latest zscore from the residual series by subtracting its mean and dividing by its standard deviation over the lookback period.

Finally, the y\_signal and x\_signal are calculated on the basis of this zscore. If the signals are not both None then the SignalEvent instances are sent back to the events queue:

```
# intraday_mr.py
    def calculate_signals_for_pairs(self):
        """
        Generates a new set of signals based on the mean reversion
        strategy.
```

```
Calculates the hedge ratio between the pair of tickers.
We use OLS for this, althought we should ideall use CADF.
"""
# Obtain the latest window of values for each
# component of the pair of tickers
y = self.bars.get_latest_bars_values(
    self.pair[0], "close", N=self.ols_window
)
x = self.bars.get_latest_bars_values(
    self.pair[1], "close", N=self.ols_window
)
if y is not None and x is not None:
    # Check that all window periods are available
    if len(y) >= self.ols_window and len(x) >= self.ols_window:
        # Calculate the current hedge ratio using OLS
        self.hedge_ratio = sm.OLS(y, x).fit().params[0]
        # Calculate the current z-score of the residuals
        spread = y - self.hedge_ratio * x
        zscore_last = ((spread - spread.mean())/spread.std())[-1]
        # Calculate signals and add to events queue
        y_signal, x_signal = self.calculate_xy_signals(zscore_last)
        if y_signal is not None and x_signal is not None:
            self.events.put(y_signal)
            self.events.put(x_signal)
```

The nal method, calculate\_signals is overidden from the base class and is used to check whether a received event from the queue is actually a MarketEvent, in which case the calculation of the new signals is carried out:

```
# intraday_mr.py
```

```
def calculate_signals(self, event):
    """
    Calculate the SignalEvents based on market data.
    """
    if event.type == 'MARKET':
        self.calculate_signals_for_pairs()
```

The \_\_main\_\_ section ties together the components to produce a backtest for the strategy. We tell the simulation where the ticker minutely data is stored. I'm using DTN IQFeed format. I truncated both les so that they began and ended on the same respective minute. For this particular pair of AREX and WLL, the common start date is 8th November 2007 at 10:41:00AM. Finally, we build the backtest object and begin simulating the trading:

```
# intraday_mr.py
```

```
if __name__ == "__main__":
    csv_dir = '/path/to/your/csv/file' # CHANGE THIS!
    symbol_list = ['AREX', 'WLL']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2007, 11, 8, 10, 41, 0)
    backtest = Backtest(
        csv_dir, symbol_list, initial_capital, heartbeat,
```

```
start_date, HistoricCSVDataHandlerHFT, SimulatedExecutionHandler,
PortfolioHFT, IntradayOLSMRStrategy
```

```
backtest.simulate_trading()
```

However, before we can execute this le we need to make some modications to the data handler and portfolio objects.

In particular, it is necessary to create new les hft\_data.py and hft\_portfolio.py which are copies of data.py and portfolio.py respectively.

In hft\_data.py we need to rename HistoricCSVDataHandler to HistoricCSVDataHandlerHFT and replace the names list in the \_open\_convert\_csv\_files method.

The old line is:

```
names=[
    'datetime', 'open', 'high',
    'low', 'close', 'volume', 'adj_close'
]
```

This must be replaced with:

```
names=[
    'datetime', 'open', 'low',
    'high', 'close', 'volume', 'oi'
]
```

This is to ensure that the new format for DTN IQFeed works with the backtester.

The other change is to rename Portfolio to PortfolioHFT in hft\_portfolio.py. We must then modify a few lines in order to account for the minutely frequency of the DTN data. In particular, within the update\_timeindex method, we must change the following code:

```
for s in self.symbol_list:
    # Approximation to the real value
    market_value = self.current_positions[s] * \
        self.bars.get_latest_bar_value(s, "adj_close")
    dh[s] = market_value
    dh['total'] += market_value
```

To:

```
for s in self.symbol_list:
    # Approximation to the real value
    market_value = self.current_positions[s] * \
        self.bars.get_latest_bar_value(s, "close")
    dh[s] = market_value
    dh['total'] += market_value
```

This ensures we obtain the close price, rather than the adj\_close price. The latter is for Yahoo Finance, whereas the former is for DTN IQFeed.

We must also make a similar adjustment in update\_holdings\_from\_fill. We need to change the following code:

```
# Update holdings list with new quantities
fill_cost = self.bars.get_latest_bar_value(
    fill.symbol, "adj_close"
)
```

To:

```
# Update holdings list with new quantities
fill_cost = self.bars.get_latest_bar_value(
    fill.symbol, "close"
)
```

)

The nal change is occurs in the output\_summary\_stats method at the bottom of the le. We need to modify how the Sharpe Ratio is calculated to take into account minutely trading. The following line:

```
sharpe_ratio = create_sharpe_ratio(returns)
```

Must be changed to:

sharpe\_ratio = create\_sharpe\_ratio(returns, periods=252\*6.5\*60)

This completes the necessary changes. Upon execution of intraday\_mr.py we get the following (truncated) output from the backtest simulation:

```
..
..
375072
375073
Creating summary stats...
Creating equity curve...
                   AREX WLL cash commission total returns \
datetime
2014-03-11 15:53:00 2098 -6802 120604.3 9721.4 115900.3 -0.000052
2014-03-11 15:54:00 2101 -6799 120604.3 9721.4 115906.3 0.000052
2014-03-11 15:55:00 2100 -6802 120604.3 9721.4 115902.3 -0.000035
2014-03-11 15:56:00 2097 -6810 120604.3 9721.4 115891.3 -0.000095
2014-03-11 15:57:00 2098 -6801 120604.3 9721.4 115901.3 0.000086
2014-03-11 15:58:00 2098 -6800 120604.3 9721.4 115902.3 0.000009
2014-03-11 15:59:00 2099 -6800 120604.3 9721.4 115903.3 0.000009
2014-03-11 16:00:00 2100 -6801 120604.3 9721.4 115903.3 0.000000
2014-03-11 16:01:00 2100 -6801 120604.3 9721.4 115903.3 0.000000
2014-03-11 16:01:00 2100 -6801 120604.3 9721.4 115903.3 0.000000
                   equity_curve drawdown
datetime
2014-03-11 15:53:00 1.159003 0.003933
2014-03-11 15:54:00 1.159063 0.003873
2014-03-11 15:55:00 1.159023 0.003913
2014-03-11 15:56:00 1.158913 0.004023
2014-03-11 15:57:00 1.159013 0.003923
2014-03-11 15:58:00 1.159023 0.003913
2014-03-11 15:59:00 1.159033 0.003903
2014-03-11 16:00:00 1.159033 0.003903
2014-03-11 16:01:00 1.159033 0.003903
2014-03-11 16:01:00 1.159033 0.003903
[('Total Return', '15.90%'),
('Sharpe Ratio', '1.89'),
('Max Drawdown', '3.03%'),
('Drawdown Duration', '120718')]
Signals: 7594
Orders: 7478
Fills: 7478
```

You can see that the strategy performs adequately well during this period. It has a total return of just under 16%. The Sharpe ratio is reasonable (when compared to a typical daily strategy), but given the high-frequency nature of the strategy we should be expecting more. The major attraction of this strategy is that the maximum drawdown is low (approximately 3%). This suggests we could apply more leverage to gain more return.

The performance of this strategy can be seen in Fig 15.3:

Note that these gures are based on trading a total of 100 shares. You can adjust the leverage by simply adjusting the generate\_naive\_order method of the Portfolio class. Look for the

![](_page_16_Figure_0.jpeg)

Figure 15.3: Equity Curve, Daily Returns and Drawdowns for intraday mean-reversion strategy

attribute known as mkt\_quantity. It will be set to 100. Changing this to 2000, for instance, provides these results:

```
..
..
[('Total Return', '392.85%'),
 ('Sharpe Ratio', '2.29'),
 ('Max Drawdown', '45.69%'),
 ('Drawdown Duration', '102150')]
..
..
```

Clearly the Sharpe Ratio and Total Return are much more attractive, but we have to endure a 45% maximum drawdown over this period as well!

## 15.4 Plotting Performance

The three Figures displayed above are all created using the plot\_performance.py script. For completeness I've included the code so that you can use it as a base to create your own performance charts.

It is necessary to run this in the same directory as the output le from the backtest, namely where equity.csv resides. The listing is as follows:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# plot_performance.py
import os.path
```

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
if __name__ == "__main__":
    data = pd.io.parsers.read_csv(
        "equity.csv", header=0,
        parse_dates=True, index_col=0
    ).sort()
    # Plot three charts: Equity curve,
    # period returns, drawdowns
    fig = plt.figure()
    # Set the outer colour to white
    fig.patch.set_facecolor('white')
    # Plot the equity curve
    ax1 = fig.add_subplot(311, ylabel='Portfolio value, %')
    data['equity_curve'].plot(ax=ax1, color="blue", lw=2.)
    plt.grid(True)
    # Plot the returns
    ax2 = fig.add_subplot(312, ylabel='Period returns, %')
    data['returns'].plot(ax=ax2, color="black", lw=2.)
    plt.grid(True)
    # Plot the returns
    ax3 = fig.add_subplot(313, ylabel='Drawdowns, %')
    data['drawdown'].plot(ax=ax3, color="red", lw=2.)
    plt.grid(True)
    # Plot the figure
    plt.show()
```
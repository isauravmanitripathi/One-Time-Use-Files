## Chapter 28

# Kalman Filter-Based Pairs Trading using QSTrader

In previous chapters of the book we considered the mathematical underpinnings of State Space Models and Kalman Filters, as well as the application of the [PyKalman](https://pykalman.github.io/) library to a pair of ETFs to dynamically adjust a hedge ratio as a basis for a mean reverting trading strategy.

In this chapter we will discuss a trading strategy originally due to Ernest Chan[32] and tested by Aidan O'Mahony over at Quantopian[73]. We will make use of the QSTrader backtesting framework in order to provide a new implementation of the strategy. QSTrader will carry out the "heavy lifting" of the position tracking, portfolio handling and data ingestion, while we concentrate here solely on the code that generates the trading signals.

### 28.1 The Trading Strategy

The pairs-trading strategy is applied to a couple of Exchange Traded Funds (ETF) that both track the performance of varying duration US Treasury bonds. They are:

- [TLT iShares 20+ Year Treasury Bond ETF](https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf)
- [IEI iShares 3-7 Year Treasury Bond ETF](https://www.ishares.com/us/products/239455/ishares-37-year-treasury-bond-etf)

The goal is to build a mean-reverting strategy from this pair of ETFs.

The synthetic "spread" between TLT and IEI is the time series that we are actually interested in longing or shorting. The Kalman Filter is used to dynamically track the hedging ratio between the two in order to keep the spread stationary.

To create the trading rules it is necessary to determine when the spread has moved too far from its expected value. How do we determine what "too far" is? We could utilise a set of fixed absolute values, but these would have to be empirically determined. This would introduce another free parameter into the system that would require optimisation (and additional danger of overfitting).

One approach to creating these values is to consider a multiple of the standard deviation of the spread (as in the previous chapter) and use these as the bounds. For simplicity we can set the coefficient of the multiple to be equal to one.

Hence we can "long the spread" if the forecast error drops below the negative standard deviation of the spread. Respectively we can "short the spread" if the forecast error exceeds the positive standard deviation of the spread. The exit rules are simply the opposite of the entry rules.

The dynamic hedge ratio is represented by one component of the hidden state vector at time t, θt, which we will denote as θ 0 t . This is the "beta" slope value that is well known from linear regression.

"Longing the spread" here means purchasing (longing) N units of TLT and selling (shorting) bθ 0 <sup>t</sup> Nc, where bxc is the "floor" representing the highest integer less than x. The latter is necessary as we must transact a whole number of units of the ETFs. "Shorting the spread" is the opposite of this. N controls the overall size of the position.

e<sup>t</sup> represents the forecast error or residual error of the prediction at time t, while Q<sup>t</sup> represents the variance of this prediction at time t.

For completeness, the rules are specified here:

- 1. e<sup>t</sup> < − √ Q<sup>t</sup> - Long the spread: Go long N shares of TLT and go short bθ 0 <sup>t</sup> Nc units of IEI
- 2. <sup>e</sup><sup>t</sup> ≥ −<sup>√</sup> Q<sup>t</sup> - Exit long: Close all long positions of TLT and IEI
- 3. e<sup>t</sup> > √ Q<sup>t</sup> - Short the spread: Go short N shares of TLT and go long bθ 0 <sup>t</sup> Nc units of IEI
- 4. e<sup>t</sup> ≤ √ Q<sup>t</sup> - Exit short: Close all short positions of TLT and IEI

The role of the Kalman filter is to help us calculate θt, as well as e<sup>t</sup> and Qt. θ<sup>t</sup> represents the vector of the intercept and slope values in the linear regression between TLT and IEI at time t. It is estimated by the Kalman filter. The forecast error/residual e<sup>t</sup> = y<sup>t</sup> − yˆ<sup>t</sup> is the difference between the value of TLT today and the Kalman filter's estimate of TLT today. Q<sup>t</sup> is the variance of the predictions and hence <sup>√</sup> Q<sup>t</sup> is the standard deviation of the prediction.

For more detail on where these quantities arise please see the previous chapter on State Space Models and the Kalman Filter.

The implementation of the strategy involves the following steps:

- 1. Receive daily market OHLCV bars for both TLT and IEI
- 2. Use the recursive "online" Kalman filter to estimate the price of TLT today based on yesterdays observations of IEI
- 3. Take the difference between the Kalman estimate of TLT and the actual value, often called the forecast error or residual error, which is a measure of how much the spread of TLT and IEI moves away from its expected value
- 4. Long the spread when the movement is negatively far from the expected value and correspondingly short the spread when the movement is positively far from the expected value
- 5. Exit the long and short positions when the series reverts to its expected value

#### 28.1.1 Data

In order to carry out this strategy it is necessary to have OHLCV pricing data for the period covered by this backtest. In particular it is necessary to download the following:

- TLT For the period 3rd August 2009 to 1st August 2016 [\(link here\)](http://real-chart.finance.yahoo.com/table.csv?s=TLT&a=07&b=1&c=2009&d=07&e=1&f=2016&g=d&ignore=.csv)
- IEI For the period 3rd August 2009 to 1st August 2016 [\(link here\)](http://real-chart.finance.yahoo.com/table.csv?s=IEI&a=07&b=1&c=2009&d=07&e=1&f=2016&g=d&ignore=.csv).

This data will need to placed in the directory specified by the QSTrader settings file if you wish to replicate the results.

### 28.2 Python QSTrader Implementation

Since QSTrader handles the position tracking, portfolio management, data ingestion and order management the only code we need to write involves the Strategy object itself.

The Strategy communicates with the PortfolioHandler via the event queue, making use of SignalEvent objects to do so. In addition we must import the base abstract strategy class, AbstractStrategy.

Note that in the current alpha version of QSTrader we must also import the PriceParser class. This is used to multiply all prices on input by a large multiple (10<sup>8</sup> ) and perform integer arithmetic when tracking positions. This avoids floating point rounding issues that can accumulate over the long period of a backtest. We must divide all the prices by PriceParser.PRICE\_MULTIPLIER to obtain the correct values:

**from** \_\_future\_\_ **import** print\_function

```
from math import floor
```

**import** numpy as np

```
from qstrader.price_parser import PriceParser
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
```

The next step is to create the KalmanPairsTradingStrategy class. The job of this class is to determine when to create SignalEvent objects based on received BarEvents from the daily OHLCV bars of TLT and IEI from Yahoo Finance.

There are many different ways to organise this class. I have opted to hardcode all of the parameters in the class for clarity of the explanation. Notably I have fixed the value of δ = 10<sup>−</sup><sup>4</sup> and v<sup>t</sup> = 10<sup>−</sup><sup>3</sup> . They represent the system noise and measurement noise variance in the Kalman Filter model. This could also be implemented as a keyword argument in the \_\_init\_\_ constructor of the class. Such an approach would allow straightforward parameter optimisation.

The first task is to set the time and invested members to be equal to None, as they will be updated as market data is accepted and trade signals generated. latest\_prices is an array of length two containing the current prices of TLT and IEI, used for convenience throughout the class.

The next set of parameters all relate to the Kalman Filter and are explained in depth in the previous chapters.

The final set of parameters include days, used to track how many days have passed as well as qty and cur\_hedge\_qty, used to track the absolute quantities of ETFs to purchase for both the long and short side. I have set this to be 2,000 units on an account equity of 100,000 USD.

```
class KalmanPairsTradingStrategy(AbstractStrategy):
    """
    Requires:
    tickers - The list of ticker symbols
    events_queue - A handle to the system events queue
    """
    def __init__(
        self, tickers, events_queue
    ):
        self.tickers = tickers
        self.events_queue = events_queue
        self.time = None
        self.latest_prices = np.array([-1.0, -1.0])
        self.invested = None
        self.delta = 1e-4
        self.wt = self.delta / (1 - self.delta) * np.eye(2)
        self.vt = 1e-3
        self.theta = np.zeros(2)
        self.P = np.zeros((2, 2))
        self.R = None
        self.days = 0
        self.qty = 2000
        self.cur_hedge_qty = self.qty
```

The next method \_set\_correct\_time\_and\_price is a "helper" method utilised to ensure that the Kalman Filter has all of the correct pricing information available at the right point. This is necessary because in an event-driven backtest system such as QSTrader market information arrives sequentially, and possibly "out of order".

We might be in a situation on day K where we have received a price for IEI, but not TFT. Hence we must wait until both TFT and IEI market events have arrived from the backtest loop, through the events queue. In live trading this is not an issue since they will arrive almost instantaneously compared to the trading period of a few days. However, in an event-driven backtest we must wait for both prices to arrive before calculating the new Kalman filter update.

The code essentially checks if the subsequent event is for the current day. If it is then the correct price is added to the latest\_price list of TLT and IEI. If it is a new day then the latest prices are reset and the correct prices are once again added.

```
def _set_correct_time_and_price(self, event):
    """
    Sets the correct price and event time for prices
    that arrive out of order in the events queue.
    """
    # Set the first instance of time
    if self.time is None:
```

```
self.time = event.time
# Set the correct latest prices depending upon
# order of arrival of market bar event
price = event.adj_close_price/float
    PriceParser.PRICE_MULTIPLIER
)
if event.time == self.time:
    if event.ticker == self.tickers[0]:
        self.latest_prices[0] = price
    else:
        self.latest_prices[1] = price
else:
    self.time = event.time
    self.days += 1
    self.latest_prices = np.array([-1.0, -1.0])
    if event.ticker == self.tickers[0]:
        self.latest_prices[0] = price
    else:
        self.latest_prices[1] = price
```

The core of the strategy is carried out in the calculate\_signals method. Firstly we set the correct times and prices (as described above). Then we check that we have both prices for TLT and IEI, at which point we can consider new trading signals.

y is set equal to the latest price for IEI, while F is the observation matrix containing the latest price for TLT, as well as a unity placeholder to represent the intercept in the linear regression. The Kalman Filter is subsequently updated with these latest prices. Finally we calculate the forecast error <sup>e</sup><sup>t</sup> and the standard deviation of the predictions, <sup>√</sup> Qt. We will run through this code step-by-step as it looks a little complicated.

The first task is to form the scalar value y and the observation matrix F, containing the prices of IEI and and TLT respectively. We calculate the variance-covariance matrix R or set it to the zero-matrix if it has not yet been initialised. Subsequently we calculate the new prediction of the observation yhat as well as the forecast error et.

We then calculate the variance of the observation predictions Qt as well as the standard deviation sqrt\_Qt. We use the update rules derived in the chapter on State Space Models to obtain the posterior distribution of the states theta, which contains the hedge ratio/slope between the two prices:

```
def calculate_signals(self, event):
    """
    Calculate the Kalman Filter strategy.
    """
    if event.type == EventType.BAR:
        self._set_correct_time_and_price(event)
```

# Only trade if we have both observations

```
if all(self.latest_prices > -1.0):
    # Create the observation matrix of the latest prices
    # of TLT and the intercept value (1.0) as well as the
    # scalar value of the latest price from IEI
    F = np.asarray([self.latest_prices[0], 1.0]).reshape((1, 2))
    y = self.latest_prices[1]
    # The prior value of the states \theta_t is
    # distributed as a multivariate Gaussian with
    # mean a_t and variance-covariance R_t
    if self.R is not None:
        self.R = self.C + self.wt
    else:
        self.R = np.zeros((2, 2))
    # Calculate the Kalman Filter update
    # ----------------------------------
    # Calculate prediction of new observation
    # as well as forecast error of that prediction
    yhat = F.dot(self.theta)
    et = y - yhat
    # Q_t is the variance of the prediction of
    # observations and hence \sqrt{Q_t} is the
    # standard deviation of the predictions
    Qt = F.dot(self.R).dot(F.T) + self.vt
    sqrt_Qt = np.sqrt(Qt)
    # The posterior value of the states \theta_t is
    # distributed as a multivariate Gaussian with mean
    # m_t and variance-covariance C_t
    At = self.R.dot(F.T) / Qt
    self.theta = self.theta + At.flatten() * et
    self.C = self.R - At * F.dot(self.R)
```

Finally we generate the trading signals based on the values of <sup>e</sup><sup>t</sup> and <sup>√</sup> Qt. To do this we need to check what the "invested" status is - either "long", "short" or "None". Notice how we need to adjust the cur\_hedge\_qty current hedge quantity when we go long or short as the slope θ 0 t is constantly adjusting in time:

```
# Only trade if days is greater than a "burn in" period
if self.days > 1:
    # If we're not in the market...
    if self.invested is None:
        if e < -sqrt_Q:
            # Long Entry
```

```
print("LONG: %s" % event.time)
        self.cur_hedge_qty = int(floor(self.qty*self.theta[0]))
        self.events_queue.put(
            SignalEvent(self.tickers[1], "BOT", self.qty)
        )
        self.events_queue.put(
            SignalEvent(self.tickers[0], "SLD", self.cur_hedge_qty)
        )
        self.invested = "long"
    elif e > sqrt_Q:
        # Short Entry
        print("SHORT: %s" % event.time)
        self.cur_hedge_qty = int(floor(self.qty*self.theta[0]))
        self.events_queue.put(
            SignalEvent(self.tickers[1], "SLD", self.qty)
        )
        self.events_queue.put(
            SignalEvent(self.tickers[0], "BOT", self.cur_hedge_qty)
        )
        self.invested = "short"
# If we are in the market...
if self.invested is not None:
    if self.invested == "long" and e > -sqrt_Q:
        print("CLOSING LONG: %s" % event.time)
        self.events_queue.put(
            SignalEvent(self.tickers[1], "SLD", self.qty)
        )
        self.events_queue.put(
            SignalEvent(self.tickers[0], "BOT", self.cur_hedge_qty)
        )
        self.invested = None
    elif self.invested == "short" and e < sqrt_Q:
        print("CLOSING SHORT: %s" % event.time)
        self.events_queue.put(
            SignalEvent(self.tickers[1], "BOT", self.qty)
        )
        self.events_queue.put(
            SignalEvent(self.tickers[0], "SLD", self.cur_hedge_qty)
        )
        self.invested = None
```

This is all of the code necessary for the Strategy object. We also need to create a backtest file to encapsulate all of our trading logic and class choices. The particular version is very similar to those used in the examples directory and replaces the equity of 500,000 USD with 100,000 USD.

It also changes the FixedPositionSizer to the NaivePositionSizer. The latter is used to "naively" accept the suggestions of absolute quantities of ETF units to trade as determined in the KalmanPairsTradingStrategy class. In a production environment it would be necessary to adjust this depending upon the risk management goals of the portfolio.

Here is the full code for the kalman\_qstrader\_backtest.py:

**import** datetime

```
import click
```

```
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.yahoo_daily_csv_bar import \
    YahooDailyCsvBarPriceHandler
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.naive import NaivePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
```

```
from qstrader.trading_session.backtest import Backtest
```

**from** kalman\_qstrader\_strategy **import** KalmanPairsTradingStrategy

**def** run(config, testing, tickers, filename):

```
# Set up variables needed for backtest
events_queue = queue.Queue()
csv_dir = config.CSV_DATA_DIR
initial_equity = PriceParser.parse(100000.00)
```

```
# Use Yahoo Daily Price Handler
start_date = datetime.datetime(2009, 8, 3)
end_date = datetime.datetime(2016, 8, 1)
price_handler = YahooDailyCsvBarPriceHandler(
    csv_dir, events_queue, tickers,
    start_date=start_date, end_date=end_date
)
```

```
# Use the KalmanPairsTrading Strategy
strategy = KalmanPairsTradingStrategy(tickers, events_queue)
strategy = Strategies(strategy, DisplayStrategy())
```

```
# Use the Naive Position Sizer (suggested quantities are followed)
    position_sizer = NaivePositionSizer()
    # Use an example Risk Manager
    risk_manager = ExampleRiskManager()
    # Use the default Portfolio Handler
    portfolio_handler = PortfolioHandler(
        initial_equity, events_queue, price_handler,
        position_sizer, risk_manager
    )
    # Use the ExampleCompliance component
    compliance = ExampleCompliance(config)
    # Use a simulated IB Execution Handler
    execution_handler = IBSimulatedExecutionHandler(
        events_queue, price_handler, compliance
    )
    # Use the Tearsheet Statistics
    title = ["Kalman Filter Pairs Trade on TLT/IEI"]
    statistics = TearsheetStatistics(
        config, portfolio_handler, title
    )
    # Set up the backtest
    backtest = Backtest(
        price_handler, strategy,
        portfolio_handler, execution_handler,
        position_sizer, risk_manager,
        statistics, initial_equity
    )
    results = backtest.simulate_trading(testing=testing)
    statistics.save(filename)
    return results
@click.command()
@click.option(
    '--config', default=settings.DEFAULT_CONFIG_FILENAME,
    help='Config filename'
@click.option(
```

)

```
'--testing/--no-testing', default=False,
    help='Enable testing mode'
)
@click.option('--tickers', default='SP500TR', help='Tickers (use comma)')
@click.option(
    '--filename', default='',
    help='Pickle (.pkl) statistics filename'
)
def main(config, testing, tickers, filename):
    tickers = tickers.split(",")
    config = settings.from_file(config, testing)
    run(config, testing, tickers, filename)
if __name__ == "__main__":
```

main()

As long as QSTrader is correctly installed and the data has been downloaded from Yahoo Finance the code can be executed via the following command in the terminal:

```
$ python kalman_qstrader_backtest.py --tickers=TLT,IEI
```

Thanks to the efforts of many volunteer developers, particularly [@ryankennedyio,](https://github.com/ryankennedyio) [@femto](https://github.com/femtotrader)[trader](https://github.com/femtotrader) and [@nwillemse,](https://github.com/nwillemse) the code is well-optimised for OHLCV bar data and carries out the backtesting rapidly.

### 28.3 Strategy Results

The equity curve is presented in Figure 28.1. It begins relatively flat for the first year of the strategy but rapidly escalates during the latter half of 2010 and 2011. During 2012 the strategy becomes significantly more volatile remaining "underwater" until 2015 and reaching a maximum daily drawdown percentage of 17.46%. The performance gradually increases from the maximum drawdown in late 2013 through to 2016.

The strategy has a CAGR of 7.66% with a Sharpe Ratio of 0.65. It also has a long maximum drawdown duration of 817 days–well over two years! Note that this strategy is carried out net of transaction costs so is reasonably reflective of real-world performance, under the assumption of achieving closing prices of assets.

### 28.4 Next Steps

There is a lot of research work necessary to turn this into a profitable strategy that we would deploy in a live setting. Potential avenues of research include:

• Parameter Optimisation - Varying the parameters of the Kalman Filter via crossvalidation grid search or some form of machine learning optimisation. However, this introduces the distinct possibility of overfitting to historical data.

![](_page_10_Figure_0.jpeg)

#### Kalman Filter Pairs Trade on TLT/IEI

Figure 28.1: Kalman Filter-Based Pairs Trade Tearsheet from QSTrader

• Asset Selection - Choosing additional, or alternative, pairs of ETFs would help to add diversification to the portfolio, but increases the complexity of the strategy as well as the number of trades (and thus transaction costs).

### 28.5 Full Code

```
# kalman_qstrader_strategy.py
from math import floor
import numpy as np
from qstrader.price_parser import PriceParser
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
class KalmanPairsTradingStrategy(AbstractStrategy):
    """
    Requires:
    tickers - The list of ticker symbols
    events_queue - A handle to the system events queue
    """
    def __init__(
        self, tickers, events_queue
    ):
        self.tickers = tickers
        self.events_queue = events_queue
        self.time = None
        self.latest_prices = np.array([-1.0, -1.0])
        self.invested = None
        self.delta = 1e-4
        self.wt = self.delta / (1 - self.delta) * np.eye(2)
        self.vt = 1e-3
        self.theta = np.zeros(2)
        self.P = np.zeros((2, 2))
        self.R = None
        self.days = 0
        self.qty = 2000
        self.cur_hedge_qty = self.qty
    def _set_correct_time_and_price(self, event):
```

```
"""
    Sets the correct price and event time for prices
    that arrive out of order in the events queue.
    """
    # Set the first instance of time
    if self.time is None:
        self.time = event.time
    # Set the correct latest prices depending upon
    # order of arrival of market bar event
    price = event.adj_close_price/float(
        PriceParser.PRICE_MULTIPLIER
    )
    if event.time == self.time:
        if event.ticker == self.tickers[0]:
            self.latest_prices[0] = price
        else:
            self.latest_prices[1] = price
    else:
        self.time = event.time
        self.days += 1
        self.latest_prices = np.array([-1.0, -1.0])
        if event.ticker == self.tickers[0]:
            self.latest_prices[0] = price
        else:
            self.latest_prices[1] = price
def calculate_signals(self, event):
    """
    Calculate the Kalman Filter strategy.
    """
    if event.type == EventType.BAR:
        self._set_correct_time_and_price(event)
        # Only trade if we have both observations
        if all(self.latest_prices > -1.0):
            # Create the observation matrix of the latest prices
            # of TLT and the intercept value (1.0) as well as the
            # scalar value of the latest price from IEI
            F = np.asarray([self.latest_prices[0], 1.0]).reshape((1, 2))
            y = self.latest_prices[1]
            # The prior value of the states \theta_t is
            # distributed as a multivariate Gaussian with
            # mean a_t and variance-covariance R_t
```

```
if self.R is not None:
    self.R = self.C + self.wt
else:
    self.R = np.zeros((2, 2))
# Calculate the Kalman Filter update
# ----------------------------------
# Calculate prediction of new observation
# as well as forecast error of that prediction
yhat = F.dot(self.theta)
et = y - yhat
# Q_t is the variance of the prediction of
# observations and hence \sqrt{Q_t} is the
# standard deviation of the predictions
Qt = F.dot(self.R).dot(F.T) + self.vt
sqrt_Qt = np.sqrt(Qt)
# The posterior value of the states \theta_t is
# distributed as a multivariate Gaussian with mean
# m_t and variance-covariance C_t
At = self.R.dot(F.T) / Qt
self.theta = self.theta + At.flatten() * et
self.C = self.R - At * F.dot(self.R)
# Only trade if days is greater than a "burn in" period
if self.days > 1:
    # If we're not in the market...
    if self.invested is None:
        if et < -sqrt_Qt:
            # Long Entry
            print("LONG: %s" % event.time)
            self.cur_hedge_qty = int(
                floor(self.qty*self.theta[0])
            )
            self.events_queue.put(
                SignalEvent(
                    self.tickers[1],
                    "BOT", self.qty
                )
            )
            self.events_queue.put(
                SignalEvent(
                    self.tickers[0],
                    "SLD", self.cur_hedge_qty
```

```
)
        )
        self.invested = "long"
    elif et > sqrt_Qt:
        # Short Entry
        print("SHORT: %s" % event.time)
        self.cur_hedge_qty = int(
            floor(self.qty*self.theta[0])
        )
        self.events_queue.put(
            SignalEvent(
                self.tickers[1], "SLD", self.qty
            )
        )
        self.events_queue.put(
            SignalEvent(
                self.tickers[0], "BOT",
                self.cur_hedge_qty
            )
        )
        self.invested = "short"
# If we are in the market...
if self.invested is not None:
    if self.invested == "long" and et > -sqrt_Qt:
        print("CLOSING LONG: %s" % event.time)
        self.events_queue.put(
            SignalEvent(
                self.tickers[1],
                "SLD", self.qty
            )
        )
        self.events_queue.put(
            SignalEvent(
                self.tickers[0],
                "BOT", self.cur_hedge_qty
            )
        )
        self.invested = None
    elif self.invested == "short" and et < sqrt_Qt:
        print("CLOSING SHORT: %s" % event.time)
        self.events_queue.put(
            SignalEvent(
                self.tickers[1],
                "BOT", self.qty
            )
```

```
)
                            self.events_queue.put(
                                SignalEvent(
                                     self.tickers[0],
                                     "SLD", self.cur_hedge_qty
                                )
                            )
                            self.invested = None
# kalman_qstrader_backtest.py
import click
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.yahoo_daily_csv_bar import \
    YahooDailyCsvBarPriceHandler
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.naive import NaivePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading_session.backtest import Backtest
from kalman_qstrader_strategy import KalmanPairsTradingStrategy
def run(config, testing, tickers, filename):
    # Set up variables needed for backtest
    events_queue = queue.Queue()
    csv_dir = config.CSV_DATA_DIR
    initial_equity = PriceParser.parse(100000.00)
    # Use Yahoo Daily Price Handler
    price_handler = YahooDailyCsvBarPriceHandler(
        csv_dir, events_queue, tickers
    )
    # Use the KalmanPairsTrading Strategy
```

strategy = KalmanPairsTradingStrategy(tickers, events\_queue)

```
strategy = Strategies(strategy, DisplayStrategy())
    # Use the Naive Position Sizer (suggested quantities are followed)
    position_sizer = NaivePositionSizer()
    # Use an example Risk Manager
    risk_manager = ExampleRiskManager()
    # Use the default Portfolio Handler
    portfolio_handler = PortfolioHandler(
        initial_equity, events_queue, price_handler,
        position_sizer, risk_manager
    )
    # Use the ExampleCompliance component
    compliance = ExampleCompliance(config)
    # Use a simulated IB Execution Handler
    execution_handler = IBSimulatedExecutionHandler(
        events_queue, price_handler, compliance
    )
    # Use the default Statistics
    statistics = TearsheetStatistics(
        config, portfolio_handler, title=""
    )
    # Set up the backtest
    backtest = Backtest(
        price_handler, strategy,
        portfolio_handler, execution_handler,
        position_sizer, risk_manager,
        statistics, initial_equity
    )
    results = backtest.simulate_trading(testing=testing)
    statistics.save(filename)
    return results
@click.command()
@click.option(
    '--config',
    default=settings.DEFAULT_CONFIG_FILENAME,
    help='Config filename'
```

)

```
@click.option(
    '--testing/--no-testing',
    default=False, help='Enable testing mode'
)
@click.option(
    '--tickers',
    default='SP500TR', help='Tickers (use comma)'
)
@click.option(
    '--filename',
    default='', help='Pickle (.pkl) statistics filename'
)
def main(config, testing, tickers, filename):
    tickers = tickers.split(",")
    config = settings.from_file(config, testing)
    run(config, testing, tickers, filename)
if __name__ == "__main__":
```

main()
## Chapter 25

# Introductory Portfolio Strategies

In this chapter we are going to gently introduce the usage of QSTrader via the backtesting of long-only portfolios comprised solely of Exchange Traded Funds (ETF). Such strategies are easy to interpret. They serve to provide insight into the mechanics of the software in a more elementary setting.

## 25.1 Motivation

Many institutional global asset managers are constrained by the need to invest in long-only strategies with zero or minimal leverage. This means that their strategies are often highly correlated to "the market" (usually the S&P500 index). While it is difficult to minimise this correlation without applying a short market hedge, it can be reduced by investing in non-equities based ETFs.

These portfolios usually possess an infrequent rebalance rate–often weekly or monthly. They differ substantially from a classic intraday stat-arb quant strategy but are nevertheless fully systematic in their approach.

In this chapter a simple fixed proportion portfolio framework is presented to demonstrate the basics of QSTrader. The strategies themselves are not novel–they are straightforward examples of classic diversified ETF mixes–but it does serve to demonstrate the rebalancing mechanic within the software.

Some of the portfolio mixes presented here are extremely well known but the latter "strategic mix" was inspired by a recent article[80] over at the [The Capital Spectator](http://www.capitalspectator.com/) blog.

## 25.2 The Trading Strategies

The trading strategies are extremely similar, only varying in portfolio weights and starting dates.

At the end of every month the strategy fully liquidates the portfolio. It then rebalances each asset to be dollar-weighted according to the initially specified fixed proportion of the current account equity.

The first strategy simply carries a 60%/40% weighting of equities and bonds using the ETFs with tickers SPY and AGG. They represent large-cap US equities and investment-grade US bonds respectively.

The second strategy provides a 30% allocation to US equities via SPY and IJS, 25% to emerging markets equities via EFA and EEM, 25% to US bonds (investment grade and highyield) via AGG and JNK, 10% allocation to commodities via DJP and finally a 10% allocation to real estate investment trusts (REITs) via RWR.

The third strategy uses the same set of ETFs as the second strategy but provides an equal weighting at 12.5% for all eight.

The starting dates are varied solely on the availability of data. Strategy #1 begins on the 29th September 2003, while strategies #2 and #3 begin on the 4th December 2007. All strategies end on the 12th October 2016.

| Ticker | #1 - 60/40 US Equities/Bonds | #2 - "Strategic" Weight | #3 - Equal Weight |
|--------|------------------------------|-------------------------|-------------------|
| SPY    | 60.0%                        | 25.0%                   | 12.5%             |
| IJS    | 0.0%                         | 5.0%                    | 12.5%             |
| EFA    | 0.0%                         | 20.0%                   | 12.5%             |
| EEM    | 0.0%                         | 5.0%                    | 12.5%             |
| AGG    | 40.0%                        | 20.0%                   | 12.5%             |
| JNK    | 0.0%                         | 5.0%                    | 12.5%             |
| DJP    | 0.0%                         | 10.0%                   | 12.5%             |
| RWR    | 0.0%                         | 10.0%                   | 12.5%             |

## 25.3 Data

In order to carry out this strategy it is necessary to have daily bar open-high-low-close (OHLC) pricing data for the period covered by the backtests. All ETF pricing data can be downloaded from Yahoo Finance in the links given in the following table:

| Ticker | Name                                                         | Period                                     | Link          |
|--------|--------------------------------------------------------------|--------------------------------------------|---------------|
| SPY    | SPDR S&P 500 ETF                                             | 29th September 2003<br>- 12th October 2016 | Yahoo Finance |
| IJS    | iShares<br>S&P<br>Small<br>Cap 600 Value ETF                 | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |
| EFA    | iShares MSCI EAFE<br>ETF                                     | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |
| EEM    | iShares<br>MSCI<br>Emerging<br>Markets<br>ETF                | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |
| AGG    | iShares Core US Ag<br>gregate Bond ETF                       | 29th September 2003<br>- 12th October 2016 | Yahoo Finance |
| JNK    | SPDR Barclays Cap<br>ital High Yield Bond<br>ETF             | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |
| DJP    | iPath<br>Bloomberg<br>Commodity<br>Index<br>Total Return ETN | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |
| RWR    | SPDR<br>Dow<br>Jones<br>REIT ETF                             | 4th December 2007 -<br>12th October 2016   | Yahoo Finance |

This data will need to placed in the directory specified by the QSTrader settings file if you wish to replicate the results.

## 25.4 Python QSTrader Implementation

In this section the required components within the QSTrader codebase will be explained in order to allow further exploration and/or development of your own rebalancing logic. Secondly, the "client" code will be outlined in order to demonstrate how to quickly setup a backtest using the built-in monthly rebalance logic.

There are two components within the QSTrader codebase required to make this monthly rebalance logic work. The first is a subclass of the Strategy base class, namely MonthlyLiquidateRebalanceStrategy. The second is a subclass of the PositionSizer base class, namely LiquidateRebalancePositionSizer.

#### 25.4.1 MonthlyLiquidateRebalanceStrategy

MonthlyLiquidateRebalanceStrategy contains new methods not present on the Strategy base class. The first is \_end\_of\_month. It simply uses the Python [calendar](https://docs.python.org/3/library/calendar.html) module along with the monthrange method to determine if the date passed is the final day of that particular month:

```
def _end_of_month(self, cur_time):
    """
    Determine if the current day is at the end of the month.
    """
    cur_day = cur_time.day
    end_day = calendar.monthrange(cur_time.year, cur_time.month)[1]
    return cur_day == end_day
```

The second method is \_create\_invested\_list, which simply creates a dictionary from a dictionary comprehension of all tickers as keys and boolean False as values. This tickers\_invested dict is used for "housekeeping" to check whether an asset has been purchased at the point of carrying out subsequent trading logic.

This is necessary because on the first run through of the code the liquidation of the entire portfolio is not required:

```
def _create_invested_list(self):
    """
    Create a dictionary with each ticker as a key, with
    a boolean value depending upon whether the ticker has
    been "invested" yet. This is necessary to avoid sending
    a liquidation signal on the first allocation.
    """
    tickers_invested = {ticker: False for ticker in self.tickers}
    return tickers_invested
```

The core logic for all Strategy-derived classes is encapsulated in the calculate\_signals method. This code initially checks whether the date of the current bar is the final day of the month. If this is the case it then determines whether the portfolio has previously been purchased, and if so, whether it should liquidate it fully prior to rebalancing.

Irrespective of the liquidation it simply sends a long signal ("BOT" in Interactive Brokers terminology) to the events queue. It then updates the tickers\_invested dict to show that this ticker has now been purchased at least once:

```
def calculate_signals(self, event):
    """
    For a particular received BarEvent, determine whether
    it is the end of the month (for that bar) and generate
    a liquidation signal, as well as a purchase signal,
    for each ticker.
    """
    if (
        event.type in [EventType.BAR, EventType.TICK] and
        self._end_of_month(event.time)
```

```
):
    ticker = event.ticker
    if self.tickers_invested[ticker]:
        liquidate_signal = SignalEvent(ticker, "EXIT")
        self.events_queue.put(liquidate_signal)
    long_signal = SignalEvent(ticker, "BOT")
    self.events_queue.put(long_signal)
    self.tickers_invested[ticker] = True
```

This wraps up the code for the MonthlyLiquidateRebalanceStrategy. The next object is the LiquidateRebalancePositionSizer.

#### 25.4.2 LiquidateRebalancePositionSizer

This component is responsible for the actual position sizing, which for the strategies outlined above is fixed-proportion equity dollar-weighting of all positions at the end of each month.

In the initialisation of the object it is necessary to pass a dictionary containing the initial weights of the tickers. Each key is a ticker name and each value lies between 0.0 and 1.0, representing a percentage weight of that ticker to the portfolio:

**def** \_\_init\_\_(self, ticker\_weights): self.ticker\_weights = ticker\_weights

The ticker\_weights dict has the following example structure for these strategies:

```
ticker_weights = {
    "SPY": 0.6,
    "AGG": 0.4
```

}

It is easy to see how this can be expanded to possess any initial set of ETFs or equities with various weights. At this stage, while not a hard requirement, the code is set up to handle allocations only when the weights add up to 1.0. A weighting in excess of 1.0 would indicate the use of leverage/margin, which is not currently handled in QSTrader.

The main code for LiquidateRebalancePositionSizer is given in the size\_order method. It initially asks whether the order received has an "EXIT" (liquidate) action or whether it is a "BOT" long action. This determines how the order is modified.

If it is a liquidate signal then the current quantity already purchased is determined and an opposing signal is created to net out the quantity of the position to zero. If instead it is a long signal to purchase shares then the current price of the asset must first be determined. This is achieved by querying portfolio.price\_handler.tickers[ticker]["adj\_close"].

Once the current price of the asset is determined the full portfolio equity must be obtained. With these two values it is possible to calcualte the new dollar-weighting for that particular asset by multiplying the full equity by the proportion weight of the asset. This is finally converted into an integer value of shares to purchase.

Note that the market price and equity value must be divided by PriceParser.PRICE\_MULTIPLIER to avoid round-off errors.

**def** size\_order(self, portfolio, initial\_order):

```
"""
Size the order to reflect the dollar-weighting of the
current equity account size based on pre-specified
ticker weights.
"""
ticker = initial_order.ticker
if initial_order.action == "EXIT":
    # Obtain current quantity and liquidate
    cur_quantity = portfolio.positions[ticker].quantity
    if cur_quantity > 0:
        initial_order.action = "SLD"
        initial_order.quantity = cur_quantity
    elif cur_quantity < 0:
        initial_order.action = "BOT"
        initial_order.quantity = cur_quantity
    else:
        initial_order.quantity = 0
else:
    weight = self.ticker_weights[ticker]
    # Determine total portfolio value, work out dollar weight
    # and finally determine integer quantity of shares to purchase
    price = portfolio.price_handler.tickers[ticker]["adj_close"]
    price /= PriceParser.PRICE_MULTIPLIER
    equity = portfolio.equity / PriceParser.PRICE_MULTIPLIER
    dollar_weight = weight * equity
    weighted_quantity = int(floor(dollar_weight / price))
    # Update quantity
    initial_order.quantity = weighted_quantity
return initial_order
```

#### 25.4.3 Backtest Interface

In order to streamline the generation of multiple separate portfolios without excessive code duplication a new file called monthly\_rebalance\_run.py has been created. This contains the backtesting "boilerplate" code necessary to carry out a monthly full liquidation and rebalanced backtest. The full file listing can be found at the end of the chapter.

To generate the separate portfolio backtests for this chapter the function run\_monthly\_rebalance is imported from monthly\_rebalance\_run.py. It is then called with the benchmark ticker (SPY), the ticker\_weights dictionary containing the ETF proportions, the tearsheet title text, start/end dates and account equity.

This makes it extremely straightforward to modify portfolio composition assuming availability of the pricing data. As an example the code for the 60/40 US equities/bond mix is given by:

# equities\_bonds\_60\_40\_etf\_portfolio\_backtest.py

```
from qstrader import settings
from monthly_rebalance_run import run_monthly_rebalance
if __name__ == "__main__":
    ticker_weights = {
        "SPY": 0.6,
        "AGG": 0.4,
    }
    run_monthly_rebalance(
        settings.DEFAULT_CONFIG_FILENAME, False, "",
        "SPY", ticker_weights, "US Equities/Bonds 60/40 Mix ETF Strategy",
        datetime.datetime(2003, 9, 29), datetime.datetime(2016, 10, 12),
        500000.00
    )
```

The code for other portfolio compositions can be found in the "Full Code" section at the end of the chapter, although they are very similar to the above snippet.

To run any of the backtests it is necessary to change directory to the location of the monthly\_rebalance\_run.py file and then type the following into the console:

```
$ python equities_bonds_60_40_etf_portfolio_backtest.py
```

Remember to change the filename depending upon which backtest you wish to run.

## 25.5 Strategy Results

#### 25.5.1 Transaction Costs

The strategy results presented here are given net of transaction costs. The costs are simulated using [Interactive Brokers US equities fixed pricing for shares in North America.](https://www.interactivebrokers.co.uk/en/index.php?f=1590&p=stocks1) They do not take into account commission differences for ETFs, but they are reasonably representative of what could be achieved in a real trading strategy.

#### 25.5.2 US Equities/Bonds 60/40 ETF Portfolio

The strategy itself is carried out for SPY and AGG with historic data stretching back to 2003. The tearsheet for the strategy is presented in Figure 25.1.

The benchmark is provided by a buy-and-hold portfolio (i.e. no monthly rebalancing) solely of the SPY ETF.

The Sharpe Ratio of the benchmark and this portfolio are identical at 0.4. Hence a corresponding cost is paid in maximum drawdown by only investing in SPY. The CAGR of the strategy is 4.43%, lower than the 5.92% of SPY, due to transaction costs of carrying out the rebalancing as well as the underperformance of AGG with respect to SPY.

AGG did somewhat cushion the vast drawdown of 2008 for the portfolio but the recent underperformance of AGG over the last five years drags the results of the portfolio down significantly.

![](_page_7_Figure_1.jpeg)

Figure 25.1: US Equities/Bonds 60/40 ETF Portfolio

Because of the 2008 crash the portfolio is underwater for 1242 days–almost 3 1/2 years– compared to the benchmark's 1365 days. Be aware however that this period has had a dramatic effect on nearly any ETF portfolio, given the heavy US bias of most ETFs in existence.

#### 25.5.3 "Strategic" Weight ETF Portfolio

The tearsheet for the strategy is given in Figure 25.2.

As above the benchmark is provided by a buy-and-hold portfolio (i.e. no monthly rebalancing) solely of the SPY ETF.

In the strategic weight portfolio an attempt was made to replicate the portfolio found within this article[80]. However, suitable instruments could not be obtained to replicate the specific indices of VWEXH, RPIBX, PREMX and VGSIX. These represent US junk bonds, foreign developed markets bonds, emerging markets bonds and US REITs respectively.

In addition it was difficult to locate sufficient data for ETFs intended to represent RPIBX

![](_page_8_Figure_1.jpeg)

Figure 25.2: "Strategic" Weight ETF Portfolio

and PREMX, namely VWOB (Vanguard Emerging Markets Government Bond ETF) and BNDX (Vanguard Total International Bond ETF). The latter two only began trading in late 2013, which only admits the possibility of a 36-month period backtest. Such a duration is not sufficiently long to produce representative performance for a monthly rebalance strategy.

Hence the universe was reduced to eight ETFs compared to ten in the aforementioned post. They are outlined above in the "Data" section. Instead the portfolio is weighted 30% to US equities, 25% to emerging markets equities, 25% to US bonds, 10% to commodities and 10% to real estate.

The performance of this strategy is far worse than the 60/40 portfolio. It has a negative CAGR. Some of the pressure on the returns comes from the transaction costs of trading in eight separate securities every month. However nearly all other ETFs in the portfolio underperformed SPY by a wide margin, dragging the returns down significantly.

Commodities and fixed income in particular have not had good performance over the last

five years relative to US equities. This suggests that an equal weighting will likely degrade performance further. In the next section the strategy for equal weighting is carried out.

#### 25.5.4 Equal Weight ETF Portfolio

The tearsheet for the strategy is given in Figure [25.3.](#page-9-0)

![](_page_9_Figure_3.jpeg)

<span id="page-9-0"></span>Figure 25.3: Equal Weight ETF Portfolio

Once again the benchmark is provided by a buy-and-hold portfolio (i.e. no monthly rebalancing) solely of the SPY ETF.

As expected the performance of this portfolio is indeed significantly worse than either the strategic weighting or the 60/40 mix. The portfolio remains underwater from 2008 onwards and posts a CAGR of almost -5%. The maximum daily drawdown of this strategy is just under 73%.

However it is also clear that nearly all of the drawdown is a consequence of the 2008 financial crisis. Had the backtest been carried out a year later the results would likely have been quite different, albeit still underperforming with regards to SPY.

## 25.6 Full Code

)

```
# monthly_rebalance_run.py
import datetime
import click
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.yahoo_daily_csv_bar import \
    YahooDailyCsvBarPriceHandler
from qstrader.strategy.monthly_liquidate_rebalance_strategy import \
    MonthlyLiquidateRebalanceStrategy
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.rebalance import \
    LiquidateRebalancePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading_session.backtest import Backtest
def run_monthly_rebalance(
    config, testing, filename,
    benchmark, ticker_weights, title_str,
    start_date, end_date, equity
):
    config = settings.from_file(config, testing)
    tickers = [t for t in ticker_weights.keys()]
    # Set up variables needed for backtest
    events_queue = queue.Queue()
    csv_dir = config.CSV_DATA_DIR
    initial_equity = PriceParser.parse(equity)
    # Use Yahoo Daily Price Handler
    price_handler = YahooDailyCsvBarPriceHandler(
        csv_dir, events_queue, tickers,
        start_date=start_date, end_date=end_date
```

```
# Use the monthly liquidate and rebalance strategy
strategy = MonthlyLiquidateRebalanceStrategy(tickers, events_queue)
strategy = Strategies(strategy, DisplayStrategy())
# Use the liquidate and rebalance position sizer
# with prespecified ticker weights
position_sizer = LiquidateRebalancePositionSizer(ticker_weights)
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
title = [title_str]
statistics = TearsheetStatistics(
    config, portfolio_handler, title, benchmark
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
```

```
import datetime
from qstrader import settings
from monthly_rebalance_run import run_monthly_rebalance
if __name__ == "__main__":
    ticker_weights = {
        "SPY": 0.6,
        "AGG": 0.4,
    }
    run_monthly_rebalance(
        settings.DEFAULT_CONFIG_FILENAME, False, "",
        "SPY", ticker_weights, "US Equities/Bonds 60/40 Mix ETF Strategy",
        datetime.datetime(2003, 9, 29), datetime.datetime(2016, 10, 12),
        500000.00
    )
# strategic_weight_etf_portfolio_backtest.py
import datetime
from qstrader import settings
from monthly_rebalance_run import run_monthly_rebalance
if __name__ == "__main__":
    ticker_weights = {
        "SPY": 0.25,
        "IJS": 0.05,
        "EFA": 0.20,
        "EEM": 0.05,
        "AGG": 0.20,
        "JNK": 0.05,
        "DJP": 0.10,
        "RWR": 0.10
    }
    run_monthly_rebalance(
        settings.DEFAULT_CONFIG_FILENAME, False, "",
        "SPY", ticker_weights, "Strategic Weight ETF Strategy",
        datetime.datetime(2007, 12, 4), datetime.datetime(2016, 10, 12),
        500000.00
    )
```

```
from qstrader import settings
from monthly_rebalance_run import run_monthly_rebalance
if __name__ == "__main__":
    ticker_weights = {
        "SPY": 0.125,
        "IJS": 0.125,
        "EFA": 0.125,
        "EEM": 0.125,
        "AGG": 0.125,
        "JNK": 0.125,
        "DJP": 0.125,
        "RWR": 0.125
    }
    run_monthly_rebalance(
        settings.DEFAULT_CONFIG_FILENAME, False, "",
        "SPY", ticker_weights, "Equal Weight ETF Strategy",
        datetime.datetime(2007, 12, 4), datetime.datetime(2016, 10, 12),
        500000.00
    )
```
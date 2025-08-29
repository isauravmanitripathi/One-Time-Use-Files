## Chapter 30

# Sentiment Analysis via Sentdex Vendor Sentiment Data with QSTrader

In addition to the "usual" tricks of statistical arbitrage, trend-following and fundamental analysis, many quant shops and retail quants engage in natural language processing (NLP) techniques to build systematic strategies. Such techniques fall under the banner of Sentiment Analysis.

In this chapter a group of quantitative trading strategies will be developed that utilise a set of sentiment signals generated from a vendor API. These signals provide an integer scale ranging from -3 ("Strongest negative sentiment") to +6 ("Strongest positive sentiment"), associated with a date and a ticker symbol, that can be used as entry and exit thresholds in an event-driven backtesting simulation.

A key challenge in developing such a system is integrating the events representing sentiment, as stored in a CSV file of "datetime-ticker-sentiment" rows, into an event-driven trading system that is usually designed to trade directly off pricing data.

The chapter will begin with a brief discussion of how sentiment analysis is carried out, along with an outline of the nature of vendor APIs and sample files. It will continue by discussing the sentiment functionality present in QSTrader, including snippets of the associated Python code. It will conclude by presenting the results of three separate backtests of the sentiment strategy applied to S&P500 stocks in the tech, defence and energy sectors. The full code for these strategies is presented at the end of the chapter.

## 30.1 Sentiment Analysis

The goal of sentiment analysis is, generally, to take large quantities of "unstructured" data (such as blog posts, newspaper articles, research reports, tweets, video, images etc) and use NLP techniques to quantify positive or negative "sentiment" about certain assets.

For equities in particular this often amounts to a statistical machine learning analysis of the language utilised and whether it contains bullish or bearish phrasing. This phrasing can be quantified in terms of strength of sentiment, which translates into numerical values. Often this means positive values reflecting bullish sentiment and negative values representing bearish sentiment.

In recent years there has been a steady growth of sentiment analysis vendors, including Sentdex, PsychSignal and Accern. All use proprietary techniques to identify "entities" within alternative data and then associate a timestamped sentiment score with any extracted information. This information can then be aggregated over a time period (such as a day), in order to produce date-entity-sentiment tuples. Such tuples form the basis of a trading signal.

The actual task of taking large quantities of "big data" and quantifying the sentiment is beyond the scope of the book. An end-to-end production-ready sentiment analysis tool is a large software engineering undertaking. Hence for retail traders it is often practical to obtain vendor signals and use those as part of a broader portfolio of quantitative signals to form a strategy.

This chapter will describe a trading strategy based on a particular vendor's sentiment data, namely Sentdex, and how a basic long-only strategy can be generated around it.

#### 30.1.1 Sentdex API and Sample File

Sentdex provides an API that allows download of their sentiment data for a wide variety of financial instruments. The data is available at one minute or one day granularity. More details of their (paid) offering can be found at their [API page.](http://api.sentdex.com/)

The API will not be discussed in this chapter since it is a paid product and is mostly useful as a paper trading or live trading streaming event generator. Since this book concerns backtesting strategies across historical data it is more appropriate to use a static, locally-stored file to represent the sentiment data.

Fortuitously, Sentdex provides a sample data file (which can be found at [http://sentdex.](http://sentdex.com/api/finance/sentiment-signals/sample/) [com/api/finance/sentiment-signals/sample/](http://sentdex.com/api/finance/sentiment-signals/sample/)) that contains almost five years worth of sentiment signals, at daily resolution, for many of the constituents of the S&P500.

A snippet of the file is presented below:

```
date,symbol,sentiment_signal
2012-10-15,AAPL,6
2012-10-16,AAPL,2
2012-10-17,AAPL,6
2012-10-18,AAPL,6
2012-10-19,AAPL,6
2012-10-20,AAPL,6
2012-10-21,AAPL,1
2012-10-22,MSFT,6
2012-10-22,GOOG,6
2012-10-22,AAPL,-1
2012-10-23,AAPL,-3
2012-10-23,GOOG,-3
2012-10-23,MSFT,6
2012-10-24,GOOG,-1
2012-10-24,MSFT,-3
2012-10-24,AAPL,-1
```

It can be seen that each row contains a date, a ticker symbol and then an integer representing strength of sentiment, between +6 ("strong positive sentiment") and -3 ("strong negative sentiment").

This sample file forms the basis of the sentiment data utilised within the three separate simulations carried out in this chapter.

## 30.2 The Trading Strategy

The complexity of this implementation comes mainly from adjustments to QSTrader, rather than the strategy itself, which is quite straightforward once the sentiment signal has been generated. The strategy has been deliberately kept simple and there is plenty of scope for modification and optimisation.

The strategy is long-only in this implementation but is easily modified to include short positions. Entry and exit thresholds are determined, which are then used to generate long positions and close them out, respectively.

There are three strategies presented that are all identical with the exception of the selection of stocks they operate on. The list of stocks are as follows:

- Tech MSFT, AMZN, GOOG, IBM, AAPL
- Energy XOM, CVX, SLB, OXY, COP
- Defence BA, GD, NOC, LMT, RTN

The rules of the strategy are as follows:

- Long a ticker if its sentiment value reaches +6
- Close the ticker position if its sentiment value reaches -1

There is no percentage allocation to each stock, instead a fixed quantity of shares is used for each throughout the strategy. This fixed quantity is modified for each of the above three sectors, however.

One obvious modification would be to create a dollar-weighted investment that dynamically adjusts allocation based on account size. However, in this chapter the position-sizing is kept simple for ease of understanding the core sentiment event generation.

## 30.3 Data

In order to carry out this strategy it is necessary to have daily OHLCV pricing data for the equities in the period covered by these backtests. There are three separate simulations carried out in this chapter, each containing a group of five stocks from the S&P500. The first group consists of technology/consumer staple stocks and can be found in the first table below:

| Ticker | Name                                   | Period                                      | Link          |
|--------|----------------------------------------|---------------------------------------------|---------------|
| MSFT   | Microsoft                              | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| AMZN   | Amazon.com                             | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| GOOG   | Alphabet                               | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| AAPL   | Apple                                  | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| IBM    | International<br>Busi<br>ness Machines | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |

The second group consists of a set of defence stocks, also from the S&P500. They can be found in the table below:

| Ticker | Name                         | Period                                      | Link          |
|--------|------------------------------|---------------------------------------------|---------------|
| BA     | The<br>Boeing<br>Com<br>pany | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| LMT    | Lockheed Martin              | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| NOC    | Northrop Grumman             | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| GD     | General Dynamics             | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| RTN    | Raytheon                     | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |

The final set of tickers consist of energy stocks, once again from the S&P500. They can be found in the table below:

| Ticker | Name                    | Period                                      | Link          |
|--------|-------------------------|---------------------------------------------|---------------|
| XOM    | Exxon Mobil             | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| CVX    | Chevron                 | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| SLB    | Schlumberger            | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| OXY    | Occidental<br>Petroleum | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |
| COP    | ConocoPhilips           | 15th October 2012<br>-<br>2nd February 2016 | Yahoo Finance |

This data will need to placed in the directory specified by the QSTrader settings file if you wish to replicate the results.

In addition the Sentdex API sample file will be need to be placed in the same QSTrader data directory.

## 30.4 Python Implementation

#### 30.4.1 Sentiment Handling with QSTrader

In order to backtest the sentiment-based strategies it is necessary to consider how sentiment "signals" will be incorporated into the backtest.

The current QSTrader backtesting model is to place the event response-handling branching code into a large **while** loop that iterates over all TickEvent or BarEvent objects. Any set of historical data stored in a database or separate ticker CSV files is concatenated and iterated over line-by-line, with each row in the subsequent Pandas DataFrame forming a TickEvent or BarEvent per ticker.

The previous code to carry this out was as follows:

```
while self.price_handler.continue_backtest:
    try:
        event = self.events_queue.get(False)
    except queue.Empty:
        self.price_handler.stream_next()
    else:
        if event is not None:
            if event.type == EventType.TICK or event.type == EventType.BAR:
                self.cur_time = event.time
                self.strategy.calculate_signals(event)
                self.portfolio_handler.update_portfolio_value()
```

```
self.statistics.update(event.time, self.portfolio_handler)
elif event.type == EventType.SIGNAL:
    self.portfolio_handler.on_signal(event)
elif event.type == EventType.ORDER:
    self.execution_handler.execute_order(event)
elif event.type == EventType.FILL:
    self.portfolio_handler.on_fill(event)
else:
    raise NotImplemented(
        "Unsupported event.type '%s'" % event.type
    )
```

This code continues looping until the backtest finishes (this being determined by the PriceHandler object). It attempts to pull the latest Event from the queue and dispatches it to the correct event handler object.

However the challenge here is that the previously mentioned sentiment signals CSV file also contains timestamped sentiment signals. Hence it is necessary to "inject" the appropriate sentiment signal for a particular ticker at the correct time point in the backtest.

This has been achieved by creating a new event called SentimentEvent. It stores a timestamp, a ticker and a sentiment value (which can be a floating-point value, integer or a string) that is sent to the Strategy object in order to generate SignalEvents. The QSTrader code for SentimentEvent is as follows:

```
class SentimentEvent(Event):
    """
    Handles the event of streaming a "Sentiment" value associated
    with a ticker. Can be used for a generic "date-ticker-sentiment"
    service, often provided by many data vendors.
    """
    def __init__(self, timestamp, ticker, sentiment):
        """
        Initialises the SentimentEvent.
        Parameters:
        timestamp - The timestamp when the sentiment was generated.
        ticker - The ticker symbol, e.g. 'GOOG'.
        sentiment - A string, float or integer value of "sentiment",
            e.g. "bullish", -1, 5.4, etc.
        """
        self.type = EventType.SENTIMENT
        self.timestamp = timestamp
        self.ticker = ticker
```

self.sentiment = sentiment

An additional object hierarchy called AbstractSentimentHandler has also been created. It allows subclassing of sentiment handler objects for various vendor APIs, all shared through a common interface. Since sentiment indicators are nearly always "timestamp-ticker-sentiment" tuples, it is useful to create a unified interface.

To handle the Sentdex sample CSV file a SentdexSentimentHandler object has been written into QSTrader. As with most handlers it requires a handle to the events queue, a subset of tickers to act upon as well as a starting and ending date:

```
class SentdexSentimentHandler(AbstractSentimentHandler):
```

```
"""
SentdexSentimentHandler is designed to provide a backtesting
sentiment analysis handler for the Sentdex sentiment analysis
provider (http://sentdex.com/financial-analysis/).
It uses a CSV file with date-ticker-sentiment tuples/rows.
Hence in order to avoid implicit lookahead bias a specific
method is provided "stream_sentiment_events_on_date" that only
allows sentiment signals to be retrieved for a particular date.
"""
def __init__(
    self, csv_dir, filename,
    events_queue, tickers=None,
    start_date=None, end_date=None
):
    self.csv_dir = csv_dir
    self.filename = filename
    self.events_queue = events_queue
    self.tickers = tickers
    self.start_date = start_date
    self.end_date = end_date
    self.sent_df = self._open_sentiment_csv()
```

There are two methods associated with this class. The first is \_open\_sentiment\_csv. It wraps the opening of a CSV into a Pandas DataFrame along with associated ticker and date filtering:

```
def _open_sentiment_csv(self):
    """
    Opens the CSV file containing the sentiment analysis
    information for all represented stocks and places
    it into a pandas DataFrame.
    """
    sentiment_path = os.path.join(self.csv_dir, self.filename)
    sent_df = pd.read_csv(
        sentiment_path, parse_dates=True,
        header=0, index_col=0,
        names=("Date", "Ticker", "Sentiment")
    )
    if self.start_date is not None:
        sent_df = sent_df[self.start_date.strftime("%Y-%m-%d"):]
```

```
if self.end_date is not None:
    sent_df = sent_df[:self.end_date.strftime("%Y-%m-%d")]
if self.tickers is not None:
    sent_df = sent_df[sent_df["Ticker"].isin(self.tickers)]
return sent_df
```

The second is stream\_next, which is used to "stream" the next sentiment signal into the events queue. Since the Sentdex CSV file contains multiple tickers on the same date, it is necessary to specify a stream\_date so that lookahead bias is not introduced. That is, the eventhandler should never see a sentiment signal that is generated "in the future" by peeking too far ahead into the CSV file.

Crucially, this method actually outputs multiple SentimentEvent objects, which are all those that were generated on a particular day:

```
def stream_next(self, stream_date=None):
    """
    Stream the next set of ticker sentiment values into
    SentimentEvent objects.
    """
    if stream_date is not None:
        stream_date_str = stream_date.strftime("%Y-%m-%d")
        date_df = self.sent_df.ix[stream_date_str:stream_date_str]
        for row in date_df.iterrows():
            sev = SentimentEvent(
                stream_date, row[1]["Ticker"],
                row[1]["Sentiment"]
            )
            self.events_queue.put(sev)
    else:
```

```
print("No stream_date provided for stream_next sentiment event!")
```

The final modification to the QSTrader codebase is within the Backtest object. It involves modifying the event dispatcher to handle the addition of SentimentEvent objects that must be dispatched to an appropriate Strategy object.

In particular, within the event handling for TICK or BAR events, an extra few lines have been added. The first of these checks whether this is a strategy that contains a SentimentHandler or not. If it does, then all SentimentEvent objects for a particular day, referenced in the Sentdex sentiment file, are created.

Further down the event handler such events are sent to the Strategy object, which will then act upon them to generate signals:

```
while self.price_handler.continue_backtest:
```

```
try:
    event = self.events_queue.get(False)
except queue.Empty:
    self.price_handler.stream_next()
else:
    if event is not None:
```

```
if event.type == EventType.TICK or event.type == EventType.BAR:
    self.cur_time = event.time
    # Generate any sentiment events here
    if self.sentiment_handler is not None:
        self.sentiment_handler.stream_next(
            stream_date=self.cur_time
        )
    self.strategy.calculate_signals(event)
    self.portfolio_handler.update_portfolio_value()
    self.statistics.update(event.time, self.portfolio_handler)
elif event.type == EventType.SENTIMENT:
    self.strategy.calculate_signals(event)
elif event.type == EventType.SIGNAL:
    self.portfolio_handler.on_signal(event)
elif event.type == EventType.ORDER:
    self.execution_handler.execute_order(event)
elif event.type == EventType.FILL:
    self.portfolio_handler.on_fill(event)
else:
    raise NotImplemented(
        "Unsupported event.type '%s'" % event.type
    )
```

That concludes the modifications to QSTrader. These changes are now in the latest version found on Github, so if you wish to replicate these strategies, make sure to update your local QSTrader version.

#### 30.4.2 Sentiment Analysis Strategy Code

The full code listings for this strategy and backtest are presented at the end of the chapter.

The above modifications to QSTrader provide the necessary structure to run a sentiment analysis strategy. However it remains to be shown how the above entry and exit rules are actually implemented. As it turns out the majority of the "hard work" has been done in the above modules. The strategy implementation itself is relatively straightforward.

As always the first task is to import the necessary libraries. There are no surprises here, simply Python2/3 compatibility and the basic QSTrader objects that interact with a Strategy subclass:

# sentdex\_sentiment\_strategy.py

```
from __future__ import print_function
```

```
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
```

The new subclass is called SentdexSentimentStrategy. It only requires a list of tickers to act upon, a handle to the events queue, a sent\_buy integer sentiment threshold entry value and a sent\_sell corresponding exit threshold. Both of these are specified later in the backtest code.

In addition a base quantity of shares is required for trading. In order to keep the strategy relatively straightforward the position sizing solely buys and sells such a base quantity for each ticker at any time point in the strategy. That is, there is no dynamic adjustment of position sizes or percentage allocation to any ticker. In a production strategy this would be one of the first parts to optimise. Since this position sizing code is likely to distract from the main "sentiment" aspect of the strategy, it was decided that it be kept simple for this chapter.

Finally a self.invested dictionary member is created to store whether each ticker is currently being traded. This is done by adjusting a boolean True/False value for each ticker depending upon whether a long position is open or not:

#### **class** SentdexSentimentStrategy(AbstractStrategy):

```
"""
Requires:
tickers - The list of ticker symbols
events_queue - A handle to the system events queue
sent_buy - Integer entry threshold
sent_sell - Integer exit threshold
base_quantity - Number of shares to be traded
"""
def __init__(
    self, tickers, events_queue,
    sent_buy, sent_sell, base_quantity
):
    self.tickers = tickers
    self.events_queue = events_queue
    self.sent_buy = sent_buy
    self.sent_sell = sent_sell
    self.qty = base_quantity
    self.time = None
    self.tickers.remove("SPY")
    self.invested = dict(
        (ticker, False) for ticker in self.tickers
    )
```

As with all subclasses of AbstractStrategy the calculate\_signals method is where the actual event-driven trading rules are placed. In all other QSTrader strategies to date this method has responded to BarEvent or TickEvent objects.

In every strategy presented thus far the first line in this method always checks what the event type is (**if** event.type == EventType...). This provides greater flexibility in AbstractStrategy subclasses, since they can respond to arbitrary events, not just those based around asset pricing data.

Once the event has been confirmed as a SentimentEvent the code checks whether that particular ticker is already being traded. If not, it checks whether the sentiment exceeds the sentiment integer entry threshold and then creates a long of the base quantity of shares. If it is already trading this ticker, and the current sentiment threshold is below the provided exit threshold, then it closes the position.

Hence the strategy presented below only goes long. It is a straightforward matter to extend this to short trading. Example code for shorting has been presented in other trading strategies to date. In particular the code for the Kalman Filter Pairs Trade provides this capability.

```
def calculate_signals(self, event):
    """
    Calculate the signals for the strategy.
    """
    if event.type == EventType.SENTIMENT:
        ticker = event.ticker
        # Long signal
        if (
            self.invested[ticker] is False and
            event.sentiment >= self.sent_buy
        ):
            print("LONG %s at %s" % (ticker, event.timestamp))
            self.events_queue.put(SignalEvent(ticker, "BOT", self.qty))
            self.invested[ticker] = True
        # Close signal
        if (
            self.invested[ticker] is True and
            event.sentiment <= self.sent_sell
        ):
            print("CLOSING LONG %s at %s" % (ticker, event.timestamp))
            self.events_queue.put(SignalEvent(ticker, "SLD", self.qty))
            self.invested[ticker] = False
```

As with all QSTrader implemented strategies, there is a corresponding backtest file that specifies the parameters of the strategy. It is very similar to the other backtest files found within the book. Hence the full listing is only presented at the end of this chapter.

The main differences are the instantiation of the SentimentHandler object and setting of the parameters for the entry and exit thresholds. These are set to 6 for entry and -1 for exit, as reflected in the underlying strategy rules above. It is instructive (and potentially more profitable!) to optimise these values for various sets of tickers.

The sentdex\_sample.csv is placed in the QSTrader CSV\_DATA\_DIR, which is where the pricing data also usually resides. The start and end dates reflect the duration over which the Sentdex sample file contains sentiment predictions.

```
..
..
start_date = datetime.datetime(2012, 10, 15)
end_date = datetime.datetime(2016, 2, 2)
..
..
```

# Use the Sentdex Sentiment trading strategy

```
sentiment_handler = SentdexSentimentHandler(
    config.CSV_DATA_DIR, "sentdex_sample.csv",
    events_queue, tickers=tickers,
    start_date=start_date, end_date=end_date
)
base_quantity = 2000
sent_buy = 6
sent_sell = -1
strategy = SentdexSentimentStrategy(
    tickers, events_queue,
    sent_buy, sent_sell, base_quantity
)
strategy = Strategies(strategy, DisplayStrategy())
```

In order to execute this strategy it is necessary to utilise your QSTrader virtual environment, as always, and type the following into the terminal, where the list of tickers must be adapted to suit the particular strategy at hand. Make sure to include SPY if a benchmark comparison is desired.

The following example simulation consists of a selection of S&P500 defence stocks, including Boeing, General Dynamics, Lockheed Martin, Northrop-Grumman and Raytheon:

#### \$ python sentdex\_sentiment\_backtest.py --tickers=BA,GD,LMT,NOC,RTN,SPY

The truncated output of the defence stocks example will be as follows:

.. .. --------------------------------- Backtest complete. Sharpe Ratio: 1.62808089233 Max Drawdown: 0.0977963517677 Max Drawdown Pct: 0.0977963517677

## 30.5 Strategy Results

#### 30.5.1 Transaction Costs

The strategy results presented here are given net of transaction costs. The costs are simulated using Interactive Brokers US equities fixed pricing for shares in North America. They are reasonably representative of what could be achieved in a real trading strategy.

#### 30.5.2 Sentiment on S&P500 Tech Stocks

The base quantity of shares used for each ticker is 2,000.

The tech stocks sentiment analysis strategy posts a CAGR of 21.0% compared to the benchmark of 9.4%, using 2,000 shares of each of the five tickers. It generates large gains in only three months, namely May 2013, October 2013 and July 2015. The remainder of the time it

![](_page_12_Figure_1.jpeg)

![](_page_12_Figure_2.jpeg)

is mostly down or flat. In addition it has a large drawdown duration of 318 days during mid-2014 to mid-2015 and a large maximum daily drawdown of 17.23%, compared to 13.04% for the benchmark.

Despite this it does admit a Sharpe ratio of 1.12 compared to 0.75 for the benchmark, but the performance is not significant enough to justify a full production implementation of the strategy.

#### 30.5.3 Sentiment on S&P500 Energy Stocks

The base quantity of shares used for each ticker is 5,000.

The energy stocks mix performs quite differently to the collection of tech stocks. It is very

![](_page_13_Figure_1.jpeg)

![](_page_13_Figure_2.jpeg)

volatile, posting months with large gains and other months with large losses. Its maximum daily drawdown is extensive at 27.49%, which single-handedly eliminates it from any further consideration as a reasonable quantitative strategy. In addition the strategy seems to lose all effectiveness after mid-2014, when it drops underwater and remains flat through 2015.

It has a poor Sharpe ratio at 0.63 compared to the benchmark of 0.75. Hence this is not a viable strategy that would be taken forward in its current form.

#### 30.5.4 Sentiment on S&P500 Defence Stocks

The base quantity of shares used for each ticker is 2,000.

![](_page_14_Figure_1.jpeg)

![](_page_14_Figure_2.jpeg)

Defence stocks provide a different story compared to tech and energy. The strategy possesses many months of solid gains and has a healthy long-only, daily-period Sharpe of 1.69. Its maximum drawdown is less than the benchmark at 9.69%. It also has a strong CAGR at 25.45%. Despite these advantages it made most of its gains in 2013, with 2014 and 2015 posting far smaller returns.

While this strategy is certainly interesting there is a lot more to be done in order to put it into production. For one, it should be tested over a far larger period. In addition adding shorts would allow the strategy to be somewhat market-neutral, hopefully reducing market beta.

Optimisation of position sizing and risk management are the next logical steps and would likely have a significant effect on performance. A final modification would be to increase diversification by adding many more stocks to the mix, perhaps across sectors. Clearly there are some interesting research avenues to pursue in order to improve the strategy.

## 30.6 Full Code

# sentdex\_sentiment\_strategy.py

```
from __future__ import print_function
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
class SentdexSentimentStrategy(AbstractStrategy):
    """
    Requires:
    tickers - The list of ticker symbols
    events_queue - A handle to the system events queue
    sent_buy - Integer entry threshold
    sent_sell - Integer exit threshold
    base_quantity - Number of shares to be traded
    """
    def __init__(
        self, tickers, events_queue,
        sent_buy, sent_sell, base_quantity
    ):
        self.tickers = tickers
        self.events_queue = events_queue
        self.sent_buy = sent_buy
        self.sent_sell = sent_sell
        self.qty = base_quantity
        self.time = None
        self.tickers.remove("SPY")
        self.invested = dict(
            (ticker, False) for ticker in self.tickers
        )
    def calculate_signals(self, event):
        """
        Calculate the signals for the strategy.
        """
        if event.type == EventType.SENTIMENT:
            ticker = event.ticker
            # Long signal
```

```
if (
                self.invested[ticker] is False and
                event.sentiment >= self.sent_buy
            ):
                print("LONG %s at %s" % (ticker, event.timestamp))
                self.events_queue.put(SignalEvent(ticker, "BOT", self.qty))
                self.invested[ticker] = True
            # Close signal
            if (
                self.invested[ticker] is True and
                event.sentiment <= self.sent_sell
            ):
                print("CLOSING LONG %s at %s" % (ticker, event.timestamp))
                self.events_queue.put(SignalEvent(ticker, "SLD", self.qty))
                self.invested[ticker] = False
# sentiment_sentdex_backtest.py
import datetime
import click
import numpy as np
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.yahoo_daily_csv_bar import \
    YahooDailyCsvBarPriceHandler
from qstrader.sentiment_handler.sentdex_sentiment_handler import \
    SentdexSentimentHandler
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.naive import NaivePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading_session.backtest import Backtest
```

**from** sentdex\_sentiment\_strategy **import** SentdexSentimentStrategy

**def** run(config, testing, tickers, filename): # Set up variables needed for backtest

```
events_queue = queue.Queue()
csv_dir = config.CSV_DATA_DIR
initial_equity = PriceParser.parse(500000.00)
# Use Yahoo Daily Price Handler
start_date = datetime.datetime(2012, 10, 15)
end_date = datetime.datetime(2016, 2, 2)
price_handler = YahooDailyCsvBarPriceHandler(
    csv_dir, events_queue, tickers,
    start_date=start_date, end_date=end_date
)
# Use the Sentdex Sentiment trading strategy
sentiment_handler = SentdexSentimentHandler(
    config.CSV_DATA_DIR, "sentdex_sample.csv",
    events_queue, tickers=tickers,
    start_date=start_date, end_date=end_date
)
base_quantity = 2000
sent_buy = 6
sent_sell = -1
strategy = SentdexSentimentStrategy(
    tickers, events_queue,
    sent_buy, sent_sell, base_quantity
)
strategy = Strategies(strategy, DisplayStrategy())
# Use the Naive Position Sizer
# where suggested quantities are followed
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
```

```
execution_handler = IBSimulatedExecutionHandler(
        events_queue, price_handler, compliance
    )
    # Use the Tearsheet Statistics
    title = ["Sentiment Sentdex Strategy"]
    statistics = TearsheetStatistics(
        config, portfolio_handler, title,
        benchmark="SPY"
    )
    # Set up the backtest
    backtest = Backtest(
        price_handler, strategy,
        portfolio_handler, execution_handler,
        position_sizer, risk_manager,
        statistics, initial_equity,
        sentiment_handler=sentiment_handler
    )
    results = backtest.simulate_trading(testing=testing)
    statistics.save(filename)
    return results
@click.command()
@click.option(
    '--config',
    default=settings.DEFAULT_CONFIG_FILENAME,
    help='Config filename'
)
@click.option(
    '--testing/--no-testing',
    default=False,
    help='Enable testing mode'
)
@click.option(
    '--tickers',
    default='SPY',
    help='Tickers (use comma)'
)
@click.option(
    '--filename',
    default='',
    help='Pickle (.pkl) statistics filename'
)
```

```
def main(config, testing, tickers, filename):
    tickers = tickers.split(",")
    config = settings.from_file(config, testing)
    run(config, testing, tickers, filename)
```

```
if __name__ == "__main__":
    main()
```
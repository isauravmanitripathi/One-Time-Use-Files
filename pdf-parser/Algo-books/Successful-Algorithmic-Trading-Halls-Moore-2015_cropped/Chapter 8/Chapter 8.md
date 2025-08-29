# Chapter 8

# Processing Financial Data

In the previous chapter we outlined how to construct an equities-based securities master database. This chapter will discuss a topic that is not often considered to any great extent in the majority of trading books, that of processing nancial market data prior to usage in a strategy test.

The discussion will begin with an overview of the dierent types of data that will be of interest to algorithmic traders. The frequency of the data will then be considered, from quarterly data (such as SEC reports) through to tick and order book data on the millisecond scale. Sources of such data (both free and commercial) will then be outlined along with code for obtaining the data. Finally, cleansing and preparation of the data for usage in strategies will be discussed.

# 8.1 Market and Instrument Classication

As algorithmic traders we are often interested in a broad range of nancial markets data. This can range from underlying and derivative instrument time series prices, unstructured text-based data (such as news articles) through to corporate earnings information. This book will predominantly discuss nancial time series data.

## 8.1.1 Markets

US and international equities, foreign exchange, commodities and xed income are the primary sources of market data that will be of interest to an algorithmic trader. In the equities market it is still extremely common to purchase the underlying asset directly, while in the latter three markets highly liquid derivative instruments (futures, options or more exotic instruments) are more commonly used for trading purposes.

This broad categorisation essentially makes it relatively straightforward to deal in the equity markets, albeit with issues surrounding data handling of corporate actions (see below). Thus a large part of the retail algorithmic trading landscape will be based around equities, such as direct corporate shares or Exchange Traded Funds (ETFs). Foreign exchange (forex) markets are also highly popular since brokers will allow margin trading on percentage in point (PIP) movements. A pip is one unit of the fourth decimal point in a currency rate. For currencies denominated in US dollars this is equivalent to 1/100th of a cent.

Commodities and xed income markets are harder to trade in the underlying directly. A retail algorithmic trader is often not interested in delivering barrels of oil to an oil depot! Instead, futures contracts on the underlying asset are used for speculative purposes. Once again, margin trading is employed allowing extensive leverage on such contracts.

## 8.1.2 Instruments

A wide range of underlying and derivative instruments are available to the algorithmic trader. The following table describes the common use cases of interest.

| Market           | Instruments                         |
|------------------|-------------------------------------|
| Equities/Indices | Stock, ETFs, Futures, Options       |
| Foreign Exchange | Margin/Spot, ETFs, Futures, Options |
| Commodities      | Futures, Options                    |
| Fixed Income     | Futures, Options                    |

For the purposes of this book we will concentrate almost exclusively upon equities and ETFs to simplify the implementation.

## 8.1.3 Fundamental Data

Although algorithmic traders primarily carry out analysis of nancial price time series, fundamental data (of varying frequencies) is also often added to the analysis. So-called Quantitative Value (QV) strategies rely heavily on the accumulation and analysis of fundamental data, such as macroeconomic information, corporate earnings histories, ination indexes, payroll reports, interest rates and SEC lings. Such data is often also in temporal format, albeit on much larger timescales over months, quarters or years. QV strategies also operate on these timeframes.

This book will not discuss QV strategies or large time-scale fundamental driven strategies to any great extent, rather will concentrate on the daily or more frequent strategies derived mostly from price action.

## 8.1.4 Unstructured Data

Unstructured data consists of documents such as news articles, blog posts, papers or reports. Analysis of such data can be complicated as it relies on Natural Language Processing (NLP) techniques. One such use of analysing unstructured data is in trying to determine the sentiment context. This can be useful in driving a trading strategy. For instance, by classifying texts as "bullish", "bearish" or "neutral" a set of trading signals could be generated. The term for this process is sentiment analysis.

Python provides an extremely comprehensive library for the analysis of text data known as the [Natural Language Toolkit](http://www.nltk.org/) (NLTK). Indeed an O'Reilly book on NLTK can be downloaded for free via the authors' website - [Natural Language Processing with Python\[](http://www.nltk.org/book/)3].

#### Full-Text Data

There are numerous sources of full-text data that may be useful for generating a trading strategy. Popular nancial sources such as [Bloomberg](http://www.bloomberg.com/) and the [Financial Times,](http://www.ft.com/home/uk) as well as nancial commentary blogs such as [Seeking Alpha](http://seekingalpha.com/) and [ZeroHedge,](http://www.zerohedge.com/) provide signicant sources of text to analyse. In addition, proprietary news feeds as provided by data vendors are also good sources of such data.

In order to obtain data on a larger scale, one must make use of web scraping tools, which are designed to automate the downloading of websites en-masse. Be careful here as automated web-scraping tools sometimes breach the Terms Of Service for these sites. Make sure to check before you begin downloading this sort of data. A particularly useful tool for web scraping, which makes the process ecient and structured, is the [ScraPy library.](http://scrapy.org/)

#### Social Media Data

In the last few years there has been signicant interest in obtaining sentiment information from social media data, particularly via the [Twitter](https://twitter.com) micro-blogging service. Back in 2011, a hedge fund was launched around Twitter sentiment, known as Derwent Capital. Indeed, academic studies[4] have shown evidence that it is possible to generate a degree of predictive capability based on such sentiment analysis.

While sentiment analysis is out of the scope of this book if you wish to carry out research into sentiment, then there are two books[15, 14] by Matt Russell on obtaining social media data via the public APIs provided by these web services.

# 8.2 Frequency of Data

Frequency of data is one of the most important considerations when designing an algorithmic trading system. It will impact every design decision regarding the storage of data, backtesting a strategy and executing an algorithm.

Higher frequency strategies are likely to lead to more statistically robust analysis, simply due to the greater number of data points (and thus trades) that will be used. HFT strategies often require a signicant investment of time and capital for development of the necessary software to carry them out.

Lower frequency strategies are easier to develop and deploy, since they require less automation. However, they will often generate far less trades than a higher-frequency strategy leading to a less statistically robust analysis.

## 8.2.1 Weekly and Monthly Data

Fundamental data is often reported on a weekly, monthly, quarterly or even yearly basis. Such data include payroll data, hedge fund performance reports, SEC lings, ination-based indices (such as the Consumer Price Index, CPI), economic growth and corporate accounts.

Storage of such data is often suited to unstructured databases, such as MongoDB, which can handle hierarchically-nested data and thus allowing a reasonable degree of querying capability. The alternative is to store at-le text in a RDBMS, which is less appropriate, since full-text querying is trickier.

## 8.2.2 Daily Data

The majority of retail algorithmic traders make use of daily ("end of day"/EOD) nancial time series data, particularly in equities and foreign exchange. Such data is freely available (see below), but often of questionable quality and subject to certain biases. End-of-day data is often stored in RDBMS, since the nature of ticker/symbol mapping naturally applies to the relational model.

EOD data does not entail particularly large storage requirements. There are 252 trading days in a year for US exchanges and thus for a decade there will be 2,520 bars per security. Even with a universe of 10,000 symbols this is 25,200,000 bars, which can easily be handled within a relational database environment.

## 8.2.3 Intraday Bars

Intraday strategies often make use of hourly, fteen-, ve-, one-minutely or secondly OHLCV bars. Intraday feed providers such as QuantQuote and DTN IQFeed will often provide minutely or secondly bars based on their tick data.

Data at such frequencies will possess many "missing" bars simply because no trades were carried out in that time period. Pandas can be used to pad these values forward, albeit with a decrease in data accuracy. In addition pandas can also be used to create data on less granular timescales if necessary.

For a ten year period, minutely data will generate almost one million bars per security. Similarly for secondly data the number of data points over the same period will total almost sixty million per security. Thus to store one thousand of such securities will lead to sixty billion bars of data. This is a large amount of data to be kept in an RDBMS and consequently more sophisticated approaches are required.

Storage and retrieval of secondly data on this magnitude is somewhat outside the scope of this book so I won't discuss it further.

## 8.2.4 Tick and Order Book Data

When a trade is lled at an exchange, or other venue, a tick is generated. Tick feeds consist of all such transactions per exchange. Retail tick feeds are stored with each datum having a timestamp accurate to the millisecond level. Tick data often also includes the updated best bid/ask price. The storage of tick data is well beyond the scope of this book but needless to say the volumes of such data are substantial. Common storage mechanisms include [HDF5,](http://www.hdfgroup.org/HDF5/) [kdb](http://www.kx.com/) and simply at-le/CSV.

Multiple limit orders at an exchange lead to the concept of an order book. This is essentially the list of all bid and ask limit orders at certain volumes for each market participant. It leads to the denition of the bid-ask spread (or simply the spread), which is the smallest dierence in the bid and ask prices for the top of book orders. Creating a historical representation, or a market simulator, of a limit order book is usually necessary for carrying out ultra high frequency trading (UHFT) strategies. The storage of such data is complex and as such will be outside the scope of this book.

# 8.3 Sources of Data

There are numerous sources and vendors of nancial data. They vary substantially in breadth, timeliness, quality and price.

Broadly speaking, nancial market data provided on a delayed daily frequency or longer is available freely, albeit with dubious overall quality and the potential for survivorship bias. To obtain intraday data it is usually necessary to purchase a commercial data feed. The vendors of such feeds vary tremendously in their customer service capability, overall feed quality and breadth of instruments.

## 8.3.1 Free Sources

Free end-of-day bar data, which consists of Open-High-Low-Close-Volume (OHLCV) prices for instruments, is available for a wide range of US and international equities and futures from [Yahoo](http://finance.yahoo.com/) [Finance,](http://finance.yahoo.com/) [Google Finance](https://www.google.com/finance) and [Quandl.](http://www.quandl.com/)

#### Yahoo Finance

[Yahoo Finance](http://finance.yahoo.com/) is the "go to" resource when forming an end-of-day US equities database. The breadth of data is extremely comprehensive, listing thousands of traded equities. In addition stock-splits and dividends are handled using a back-adjustment method, arising as the "Adj Close" column in the CSV output from the API (which we discuss below). Thus the data allows algorithmic traders to get started rapidly and for zero cost.

I have personally had a lot of experience in cleaning Yahoo data. I have to remark that the data can be quite erroneous. Firstly, it is subject to a problem known as backlling. This problem occurs when past historical data is corrected at a future date, leading to poor quality backtests that change as your own database is re-updated. To handle this problem, a logging record is usually added to the securities master (in an appropriate logging table) whenever a historical data point is modied.

Secondly, the Yahoo feed only aggregates prices from a few sources to form the OHLCV points. This means that values around the open, high, low and close can be deceptive, as other exchanges/liquidity sources may have executed diering prices in excess of the values.

Thirdly, I have noticed that when obtaining nancial data en-masse from Yahoo, that errors do creep into the API. For instance, multiple calls to the API with identical date/ticker parameters occasionally lead to diering result sets. This is clearly a substantial problem and must be carefully checked for.

In summary be prepared to carry out some extensive data cleansing on Yahoo Finance data, if you choose to use it to populate a large securities master, and need highly accurate data.

#### Quandl

[Quandl](http://www.quandl.com/) is a relatively new service which purports to be The easiest way to nd and use numerical data on the web. I believe they are well on the way to achieving that goal! The service provides a substantial daily data set of US and international equities, interest rates, commodities/futures, foreign exchange and other economic data. In addition, the database is continually expanded and the project is very actively maintained.

All of the data can be accessed by a very modern HTTP API (CSV, JSON, XML or HTML), with plugins for a wide variety of programming languages including R, Python, Matlab, Excel, Stata, Maple, C#, EViews, Java, C/C++, .NET, Clojure and Julia. Without an account 50 calls to the API are allowed per day, but this can be increased to 500 if registering an account. In fact, calls can be updated to 5,000 per hour if so desired by contacting the team.

I have not had a great deal of experience with Quandl "at scale" and so I can't comment on the level of errors within the dataset, but my feeling is that any errors are likely to be constantly reported and corrected. Thus they are worth considering as a primary data source for an end-of-day securities master.

Later in the chapter we will discuss how to obtain US Commodities Futures data from Quandl with Python and pandas.

## 8.3.2 Commercial Sources

In order to carry out intraday algorithmic trading it is usually necessary to purchase a commercial feed. Pricing can range anywhere from \$30 per month to around \$500 per month for retail level feeds. Institutional quality feeds will often be in the low-to-mid four gure range per month and as such I won't discuss them here.

#### EODData

I have utilised [EODData](http://eoddata.com/) in a fund context, albeit only with daily data and predominantly for foreign exchange. Despite their name they do provide a degree of intraday sources. The cost is \$25 per month for their platinum package.

The resource is very useful for nding a full list of traded symbols on global exchanges, but remember that this will be subject to survivorship bias as I believe the list represents current listed entities.

Unfortunately (at least back in 2010) I found that the stock split feed was somewhat inaccurate (at least when compared to [Morningstar](http://morningstar.com/) information). This lead to some substantial spike issues (see below) in the data, which increased friction in the data cleansing process.

#### DTN IQFeed

[DTN IQFeed](http://www.iqfeed.net/) are one of the most popular data feeds for the high-end retail algorithmic trader. They claim to have over 80,000 customers. They provide real-time tick-by-tick data unltered from the exchange as well as a large quantity of historic data.

The pricing starts at \$50 per month, but in reality will be in the \$150-\$200 per month range once particular services are selected and exchange fees are factored in. I utilise DTN IQFeed for all of my intraday equities and futures strategies. In terms of historical data, IQFeed provide for equities, futures and options:

- 180 calendar days of tick (every trade)
- 7+ years of 1 minute historical bars
- 15+ years of daily historical bars

The major disadvantage is that the DTN IQFeed software (the mini-server, not the charting tools) will only run on Windows. This may not be a problem if all of your algorithmic trading is carried out in this operating system, but I personally develop all my strategies in Ubuntu Linux. However, although I have not actively tested it, I have heard it is possible to run DTN IQFeed under the [WINE](http://www.winehq.org/) emulator.

Below we will discuss how to obtain data from IQFeed using Python in Windows.

#### QuantQuote

[QuantQuote](https://quantquote.com/) provide reasonably priced historical minute-, second- and tick-level data for US equities going back to 1998. In addition they provide institutional level real-time tick feeds, although this is of less interest to retail algorithmic traders. One of the main benets of QuantQuote is that their data is provided free of survivorship bias, due to their TickMap symbol-matching software and inclusion of all stocks within a certain index through time.

As an example, to purchase the entire history of the S&P500 going back to 1998 in minutelybars, inclusive of de-listed stocks, the cost at the time of writing was \$895. The pricing scales with increasing frequency of data.

QuantQuote is currently the primary provider of market data to the QuantConnect webbased backtesting service. QuantQuote go to great lengths to ensure minimisation of error, so if you are looking for a US equities only feed at high resolution, then you should consider using their service.

# 8.4 Obtaining Data

In this section we are going to discuss how to use Quandl, pandas and DTN IQFeed to download nancial market data across a range of markets and timeframes.

## 8.4.1 Yahoo Finance and Pandas

The pandas library makes it exceedingly simple to download EOD data from Yahoo Finance. Pandas ships with a DataReader component that ties into Yahoo Finance (among other sources). Specifying a symbol with a start and end date is sucient to download an EOD series into a pandas DataFrame, which allows rapid vectorised operations to be carried out:

```
from __future__ import print_function
```

```
import datetime
import pandas.io.data as web
if __name__ == "__main__":
    spy = web.DataReader(
        "SPY", "yahoo",
        datetime.datetime(2007,1,1),
```

```
datetime.datetime(2015,6,15)
)
print(spy.tail())
```

The output is given below:

|            | Open       | High       | Low        | Close      | Volume    | \ |
|------------|------------|------------|------------|------------|-----------|---|
| Date       |            |            |            |            |           |   |
| 2015-06-09 | 208.449997 | 209.100006 | 207.690002 | 208.449997 | 98148200  |   |
| 2015-06-10 | 209.369995 | 211.410004 | 209.300003 | 210.960007 | 129936200 |   |
| 2015-06-11 | 211.479996 | 212.089996 | 211.199997 | 211.649994 | 72672100  |   |
| 2015-06-12 | 210.639999 | 211.479996 | 209.679993 | 209.929993 | 127811900 |   |
| 2015-06-15 | 208.639999 | 209.449997 | 207.789993 | 209.100006 | 121425800 |   |
|            | Adj Close  |            |            |            |           |   |
| Date       |            |            |            |            |           |   |
| 2015-06-09 | 208.449997 |            |            |            |           |   |
| 2015-06-10 | 210.960007 |            |            |            |           |   |
| 2015-06-11 | 211.649994 |            |            |            |           |   |
| 2015-06-12 | 209.929993 |            |            |            |           |   |
| 2015-06-15 | 209.100006 |            |            |            |           |   |
|            |            |            |            |            |           |   |

Note that in pandas 0.17.0, pandas.io.data will be replaced by a separate pandas-datareader package. However, for the time being (i.e. pandas versions 0.16.x) the syntax to import the data reader is **import** pandas.io.data as web.

In the next section we will use Quandl to create a more comprehensive, permanent download solution.

## 8.4.2 Quandl and Pandas

Up until recently it was rather dicult and expensive to obtain consistent futures data across exchanges in frequently updated manner. However, the release of the Quandl service has changed the situation dramatically, with nancial data in some cases going back to the 1950s. In this section we will use Quandl to download a set of end-of-day futures contracts across multiple delivery dates.

### Signing Up For Quandl

The rst thing to do is sign up to Quandl. This will increase the daily allowance of calls to their API. Sign-up grants 500 calls per day, rather than the default 50. Visit the site at [www.quandl.com:](http://www.quandl.com)

![](_page_6_Picture_6.jpeg)

Figure 8.1: The Quandl homepage

Click on the sign-up button on the top right:

| wirch Quandi |                                                                                                                                                                              | Learn More • | Sign In Sign Up |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
|              | Sign up                                                                                                                                                                      |              |                 |
|              | A Quand account increases your downloads/API calls per day to 500, and<br>provides supersets, favories, data upload and the Python, Excel, R, Matlab and<br>State libraries. |              |                 |
|              | Sign up using:                                                                                                                                                               |              |                 |
|              | g<br>О<br>Linkedin<br>Google<br>Github<br>Twitter                                                                                                                            |              |                 |
|              | Or sign up directly                                                                                                                                                          |              |                 |
|              | First name<br>Last name                                                                                                                                                      |              |                 |
|              | * Usemame                                                                                                                                                                    |              |                 |
|              | Formal L                                                                                                                                                                     |              |                 |

Figure 8.2: The Quandl sign-up page

Once you're signed in you'll be returned to the home page:

![](_page_7_Picture_0.jpeg)

Figure 8.3: The Quandl authorised home page

#### Quandl Futures Data

Now click on the ["New: Futures page..."](http://www.quandl.com/futures) link to get to the futures homepage:

| Asrch Guardi                                                       |               |                                                                                                                                                                                                                                                                        |        |          | Learn More . | My Uploade . |         | Formarites .  | ⊥ mhallsmoore v |
|--------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------|--------------|--------------|---------|---------------|-----------------|
| Quandi > Futures<br>Futures<br>Last undated at 2013-12-04 10:13:05 |               |                                                                                                                                                                                                                                                                        |        |          |              |              |         |               |                 |
| About                                                              | $\gg$         | About                                                                                                                                                                                                                                                                  |        |          |              |              |         |               |                 |
| Energy                                                             | >             |                                                                                                                                                                                                                                                                        |        |          |              |              |         |               |                 |
| Grains - North America                                             | 3             | This page is a portal to QuandTs index of historical futures data. QuandI covers 200+ futures contracts from 10+ exchanges, with data<br>going back as far as the 1950s. Data indexed includes current market prices, commitment of traders, continuous contracts, and |        |          |              |              |         |               |                 |
| Grains - World                                                     | 3.            | historical contracts.                                                                                                                                                                                                                                                  |        |          |              |              |         |               |                 |
| Softs                                                              | >             | All futures data indexed on Quandi is available free to Quandi users. There are no restrictions on the use of this data. I welcome and<br>appreciate your comments and suggestions.                                                                                    |        |          |              |              |         |               |                 |
| Equities - North America                                           | $\gg$         | More information about the organization of futures data on Quandi can be found at the bottom of this page.                                                                                                                                                             |        |          |              |              |         |               |                 |
| Equities - World                                                   | $\mathcal{F}$ |                                                                                                                                                                                                                                                                        |        |          |              |              |         |               |                 |
| Currencies                                                         | $\gg$         | Energy                                                                                                                                                                                                                                                                 |        |          |              |              |         |               |                 |
| Rates.                                                             | $\gg$         |                                                                                                                                                                                                                                                                        |        |          |              |              |         |               |                 |
| Bonds                                                              | 3.            | Name                                                                                                                                                                                                                                                                   | Symbol | Exchange | Price        | 1-Day Chg    | MTD Cho | Open Interest | Full Info       |
| Metals                                                             | $\mathcal{D}$ | WTI Crude Cill                                                                                                                                                                                                                                                         | CL.    | NYMEX    | 96.04        | $2.37\%$     | 3.58%   | 326,186       | Full Info.      |
| Other Agriculturais                                                | >             | Natural Gas                                                                                                                                                                                                                                                            | NG     | NYMEX    | 3.98         | $-0.30\%$    | 0.56%   | 322,670       | Full Info       |
| Global Indices                                                     | $\gg$         | Heating Oil                                                                                                                                                                                                                                                            | HO     | NYMEX    | 3.07         | 0.49%        | 0.57%   | 95.704        | Full Info       |
| MSCI Indices                                                       | 3.            | Gasoline                                                                                                                                                                                                                                                               | RB.    | NYMEX    | 2.72         | 1,69%        | 1.48%   | 93.620        | Full Info       |

Figure 8.4: The Quandl futures contracts home page

For this tutorial we will be considering the highly liquid E-Mini S&P500 futures contract, which has the futures symbol ES. To download other contracts the remainder of this tutorial can be carried out with additional symbols replacing the reference to ES.

Click on the E-Mini S&P500 link (or your chosen futures symbol) and you'll be taken to the following screen:

Scrolling further down the screen displays the list of historical contracts going back to 1997: Click on one of the individual contracts. As an example, I have chosen ESZ2014, which refers to the contract for December 2014 'delivery'. This will display a chart of the data:

By clicking on the "Download" button the data can be obtained in multiple formats: HTML, CSV, JSON or XML. In addition we can download the data directly into a pandas DataFrame using the Python bindings. While the latter is useful for quick "prototyping" and exploration of the data, in this section we are considering the development of a longer term data store. Click the download button, select "CSV" and then copy and paste the API call:

The API call will have the following form:

## http://www.quandl.com/api/v1/datasets/OFDP/FUTURE\_ESZ2014.csv? &auth\_token=MY\_AUTH\_TOKEN&trim\_start=2013-09-18 &trim\_end=2013-12-04&sort\_order=desc

The authorisation token has been redacted and replaced with MY\_AUTH\_TOKEN. It will be necessary to copy the alphanumeric string between "auth\_token=" and "&trim\_start" for

| E-mini S-and-P 500 Index Futures<br>Last undated at 2013-12-64 06:58:99 |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
|-------------------------------------------------------------------------|----|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------|-----------|---------------|-----------------|
|                                                                         |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
| Overview                                                                | 3  | Overview             |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
| Latest Quotes                                                           |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
| Commitment of Traders - Legacy                                          |    | Name                 |                                                                                                                                                                                                                                                                 | Symbol      |                                                                                                                                     | Exchange  | Months           | Category  | Price         | Change          |
| Format                                                                  |    | E-mini S&P 500 Index |                                                                                                                                                                                                                                                                 | ES          | CME                                                                                                                                 |           | HMUZ<br>Equities |           | 1.799.75      | n.a.            |
| Continuous Contracts                                                    | ٠. |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
| Historical Contracts                                                    |    |                      | E-mini S&P 500 Index Futures are traded on the Chicago Mercantile Exchange (CME), which is part of the CME Group. Each contract<br>is for \$50 multiplied by the E-mini S&P 500 Index. Prices are quoted in Index points.                                       |             |                                                                                                                                     |           |                  |           |               |                 |
| See Also                                                                | >  |                      | E-mini S&P 500 Index Futures contracts exist for the months of March (H), June (M), September (U) and December (Z). The<br>deliverable product for the E-mini S&P 500 Index Futures contract is None; this contract is cash-settled based on the S&P 500 Index. |             |                                                                                                                                     |           |                  |           |               |                 |
|                                                                         |    |                      |                                                                                                                                                                                                                                                                 |             | Click on any price shown on this page to see a time series of the underlying data, along with gotions for graphing, downloading and |           |                  |           |               |                 |
|                                                                         |    | validating the data. |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
|                                                                         |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
|                                                                         |    | Latest Quotes        |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |
|                                                                         |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     | MTD Cho   |                  | Volume    | Open Interest | Historical Data |
|                                                                         |    | Contract             | Price                                                                                                                                                                                                                                                           | As Of       | 1-Day Chg                                                                                                                           |           | YTD Chg          |           |               |                 |
|                                                                         |    | Front: ES1           | 1,799.75                                                                                                                                                                                                                                                        | 02-Dec-2013 | n.a.                                                                                                                                | $-0.08\%$ | 29.7M%           | 1,324,016 | 2.798.542     | Historical Data |
|                                                                         |    |                      |                                                                                                                                                                                                                                                                 |             |                                                                                                                                     |           |                  |           |               |                 |

![](_page_8_Figure_1.jpeg)

| rch Quandi                               |               |      |                      |              | Learn More . | My Uploade .<br>Formuritae w |  |
|------------------------------------------|---------------|------|----------------------|--------------|--------------|------------------------------|--|
| Overview                                 | >             |      | Historical Contracts |              |              |                              |  |
| Latest Quotes                            | $\gg$         |      |                      |              |              |                              |  |
| Commitment of Traders - Legacy<br>Format | $\rightarrow$ | 1997 | н<br>ESH1967         | M<br>ESM1997 | u<br>ESU1997 | Z<br>ESZ1997                 |  |
| Continuous Contracts                     | >             | 1998 | ESH1998              | ESM1998      | ESU1998      | ESZ1998                      |  |
| Historical Contracts                     | $\gg$         | 1993 | ESH1000              | ESM1909      | ESU1999      | ESZ1909                      |  |
| See Also                                 | >             | 2000 | ESH2000              | ESM2000      | ESU2000      | ESZ2000                      |  |
|                                          |               | 2001 | E\$H2001             | ESM2001      | E\$U2001     | ES22001                      |  |
|                                          |               | 2002 | ESH2002              | ESM2002      | E5U2002      | ESZ2002                      |  |
|                                          |               | 2003 | ESH2003              | ESM2003      | ESU2003      | ESZ2003                      |  |
|                                          |               | 2004 | ESH2004              | ESM2004      | E5U2004      | ESZ2004                      |  |
|                                          |               | 2005 | ESH2005              | ESM2005      | ESU2005      | ESZ2005                      |  |
|                                          |               | 2006 | E8H2006              | ESM2006      | E8U2006      | E8Z2006                      |  |
|                                          |               | 2007 | ESH2007              | ESM2007      | ESU2007      | ESZ2007                      |  |
|                                          |               | 2008 | E8H2008              | ESM2008      | ESU2006      | E822008                      |  |
|                                          |               | 2009 | ESH2009              | ESM2009      | ESU2009      | ESZ2009                      |  |
|                                          |               | 2010 | ESH2010              | ESA(2010     | ESU2010      | ESZ2010                      |  |
|                                          |               | 2011 | ESH2011              | ESM2011      | ESU2011      | ESZ2011                      |  |

Figure 8.6: E-Mini S&P500 historical contracts

![](_page_8_Figure_4.jpeg)

Figure 8.7: Chart of ESZ2014 (December 2014 delivery)

later usage in the Python script below. Do not share it with anyone as it is your unique authorisation token for Quandl downloads and is used to determine your download rate for the day.

This API call will form the basis of an automated script which we will write below to download a subset of the entire historical futures contract.

|                                                                         |                                                                  |                                     |        |                                  |                                                         |                                                                                                       |   |          | Learn More w My Uploads w Favourites w A mhallencore w |
|-------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------|--------|----------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---|----------|--------------------------------------------------------|
|                                                                         | OPEN FINANCIAL DATA PROJECT<br>FE-mini S&P 500 Futures, December |                                     |        |                                  | Data Download Wizard                                    |                                                                                                       | × |          |                                                        |
|                                                                         | 2013-09-18 G 2013-12-03 G Default Frequency H No 1               |                                     |        | Format                           |                                                         |                                                                                                       |   |          |                                                        |
| 1775-<br>1000<br>Tree -<br>1000<br>1755.4<br>1750 -<br>1741.4<br>1141 - |                                                                  |                                     |        | 4 Download Data<br>Show API call | Eroei CSV JSON XML @                                    | Directly access this dataset<br>through R, Python, MATLAB,<br>Maple, Stata, and more<br>View Packages |   | 9 Walume | Open in High.<br>+ Low + Settle<br>Open Interest       |
|                                                                         |                                                                  |                                     |        |                                  | ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ ਸਮੇਖ                 |                                                                                                       |   |          |                                                        |
|                                                                         |                                                                  |                                     |        |                                  |                                                         |                                                                                                       |   |          |                                                        |
|                                                                         | TIME TIME TIME                                                   |                                     | THE R. |                                  | עלות חלים חלים שלים שלים                                |                                                                                                       |   |          |                                                        |
| Date .                                                                  |                                                                  |                                     |        |                                  | Open 🚍 High 📳 Low 🚍 Settle 🗄 Volume 🖷 – Open Interest 🖷 |                                                                                                       |   |          |                                                        |
| 2012-12-01                                                              |                                                                  | 1,767.50 1,767.50 1,760.00 1,765.00 |        | $\sim 2$                         | $-125$                                                  |                                                                                                       |   |          |                                                        |
| 2012-12-02                                                              |                                                                  | 1,780,00 1,780,00 1,779,50 1,771,21 |        | $-2$                             | 1, 222                                                  |                                                                                                       |   |          |                                                        |
| 2013-11-29                                                              |                                                                  | 0.00 0.00 0.00 1,777.50             |        | 0                                | $-120$                                                  |                                                                                                       |   |          |                                                        |

Figure 8.8: Download modal for ESZ2014 CSV le

### Downloading Quandl Futures into Python

Because we are interested in using the futures data long-term as part of a wider securities master database strategy we want to store the futures data to disk. Thus we need to create a directory to hold our E-Mini contract CSV les. In Mac/Linux (within the terminal/console) this is achieved by the following command:

## cd /PATH/TO/YOUR/quandl\_data.py mkdir -p quandl/futures/ES

Note: Replace /PATH/TO/YOUR above with the directory where your quandl\_data.py le is located.

This creates a subdirectory of called quandl, which contains two further subdirectories for futures and for the ES contracts in particular. This will help us to organise our downloads in an ongoing fashion.

In order to carry out the download using Python we will need to import some libraries. In particular we will need requests for the download and pandas and matplotlib for plotting and data manipulation:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# quandl_data.py
from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd
import requests
```

The rst function within the code will generate the list of futures symbols we wish to download. I've added keyword parameters for the start and end years, setting them to reasonable values of 2010 and 2014. You can, of course, choose to use other timeframes:

```
def construct_futures_symbols(
        symbol, start_year=2010, end_year=2014
    ):
    """
    Constructs a list of futures contract codes
    for a particular symbol and timeframe.
    """
    futures = []
```

```
# March, June, September and
# December delivery codes
months = 'HMUZ'
for y in range(start_year, end_year+1):
    for m in months:
        futures.append("%s%s%s" % (symbol, m, y))
return futures
```

Now we need to loop through each symbol, obtain the CSV le from Quandl for that particular contract and subsequently write it to disk so we can access it later:

```
def download_contract_from_quandl(contract, dl_dir):
    """
    Download an individual futures contract from Quandl and then
    store it to disk in the 'dl_dir' directory. An auth_token is
    required, which is obtained from the Quandl upon sign-up.
    """
    # Construct the API call from the contract and auth_token
    api_call = "http://www.quandl.com/api/v1/datasets/"
    api_call += "OFDP/FUTURE_%s.csv" % contract
    # If you wish to add an auth token for more downloads, simply
    # comment the following line and replace MY_AUTH_TOKEN with
    # your auth token in the line below
    params = "?sort_order=asc"
    #params = "?auth_token=MY_AUTH_TOKEN&sort_order=asc"
    full_url = "%s%s" % (api_call, params)
    # Download the data from Quandl
    data = requests.get(full_url).text
    # Store the data to disk
    fc = open('%s/%s.csv' % (dl_dir, contract), 'w')
    fc.write(data)
    fc.close()
```

Now we tie the above two functions together to download all of the desired contracts:

```
def download_historical_contracts(
        symbol, dl_dir, start_year=2010, end_year=2014
    ):
    """
    Downloads all futures contracts for a specified symbol
    between a start_year and an end_year.
    """
    contracts = construct_futures_symbols(
        symbol, start_year, end_year
    )
    for c in contracts:
        print("Downloading contract: %s" % c)
        download_contract_from_quandl(c, dl_dir)
```

Finally, we can add one of the futures prices to a pandas dataframe using the main function. We can then use matplotlib to plot the settle price:

```
if __name__ == "__main__":
    symbol = 'ES'
    # Make sure you've created this
    # relative directory beforehand
```

```
dl_dir = 'quandl/futures/ES'
# Create the start and end years
start_year = 2010
end_year = 2014
# Download the contracts into the directory
download_historical_contracts(
    symbol, dl_dir, start_year, end_year
)
# Open up a single contract via read_csv
# and plot the settle price
es = pd.io.parsers.read_csv(
    "%s/ESH2010.csv" % dl_dir, index_col="Date"
)
es["Settle"].plot()
plt.show()
```

The output of the plot is given in Figure 8.4.2.

![](_page_11_Figure_2.jpeg)

Figure 8.9: ESH2010 Settle Price

The above code can be modied to collect any combination of futures contracts from Quandl as necessary. Remember that unless a higher API request is made, the code will be limited to making 50 API requests per day.

## 8.4.3 DTN IQFeed

For those of you who possess a DTN IQFeed subscription, the service provides a client-server mechanism for obtaining intraday data. For this to work it is necessary to download the IQLink server and run it on Windows. Unfortunately, it is tricky to execute this server on Mac or Linux unless making use of the WINE emulator. However once the server is running it can be connected to via a socket at which point it can be queried for data.

In this section we will obtain minutely bar data for a pair of US ETFs from January 1st 2007 onwards using a Python socket interface. Since there are approximately 252 trading days within each year for US markets, and each trading day has 6.5 hours of trading, this will equate to at least 650,000 bars of data, each with seven data points: Timestamp, Open, Low, High, Close, Volume and Open Interest.

I have chosen the SPY and IWM ETFs to download to CSV. Make such to start the IQLink program in Windows before executing this script:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# iqfeed.py
import sys
import socket
def read_historical_data_socket(sock, recv_buffer=4096):
    """
    Read the information from the socket, in a buffered
    fashion, receiving only 4096 bytes at a time.
    Parameters:
    sock - The socket object
    recv_buffer - Amount in bytes to receive per read
    """
    buffer = ""
    data = ""
    while True:
        data = sock.recv(recv_buffer)
        buffer += data
        # Check if the end message string arrives
        if "!ENDMSG!" in buffer:
            break
    # Remove the end message string
    buffer = buffer[:-12]
    return buffer
if __name__ == "__main__":
    # Define server host, port and symbols to download
    host = "127.0.0.1" # Localhost
    port = 9100 # Historical data socket port
    syms = ["SPY", "IWM"]
    # Download each symbol to disk
    for sym in syms:
        print "Downloading symbol: %s..." % sym
        # Construct the message needed by IQFeed to retrieve data
        message = "HIT,%s,60,20070101 075000,,,093000,160000,1\n" % sym
        # Open a streaming socket to the IQFeed server locally
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        # Send the historical data request
        # message and buffer the data
        sock.sendall(message)
```

```
data = read_historical_data_socket(sock)
sock.close
# Remove all the endlines and line-ending
# comma delimiter from each record
data = "".join(data.split("\r"))
data = data.replace(",\n","\n")[:-1]
# Write the data stream to disk
f = open("%s.csv" % sym, "w")
f.write(data)
f.close()
```

With additional subscription options in the DTN IQFeed account, it is possible to download individual futures contracts (and back-adjusted continuous contracts), options and indices. DTN IQFeed also provides real-time tick streaming, but this form of data falls outside the scope of the book.

# 8.5 Cleaning Financial Data

Subsequent to the delivery of nancial data from vendors it is necessary to perform data cleansing. Unfortunately this can be a painstaking process, but a hugely necessary one. There are multiple issues that require resolution: Incorrect data, consideration of data aggregation and backlling. Equities and futures contracts possess their own unique challenges that must be dealt with prior to strategy research, including back/forward adjustment, continuous contract stitching and corporate action handling.

## 8.5.1 Data Quality

The reputation of a data vendor will often rest on its (perceived) data quality. In simple terms, bad or missing data leads to erroneous trading signals and thus potential loss. Despite this fact, many vendors are still plagued with poor or inconsistent data quality. Thus there is always a cleansing process necessary to be carried.

The main culprits in poor data quality are conicting/incorrect data, opaque aggregation of multiple data sources and error correction ("backlling").

## Conicting and Incorrect Data

Bad data can happen anywhere in the stream. Bugs in the software at an exchange can lead to erroneous prices when matching trades. This lters through to the vendor and subsequently the trader. Reputable vendors will attempt to ag upstream "bad ticks" and will often leave the "correction" of these points to the trader.

## 8.5.2 Continuous Futures Contracts

In this section we are going to discuss the characteristics of futures contracts that present a data challenge from a backtesting point of view. In particular, the notion of the "continuous contract". We will outline the main diculties of futures and provide an implementation in Python with pandas that can partially alleviate the problems.

#### Brief Overview of Futures Contracts

Futures are a form of contract drawn up between two parties for the purchase or sale of a quantity of an underlying asset at a specied date in the future. This date is known as the delivery or expiration. When this date is reached the buyer must deliver the physical underlying (or cash equivalent) to the seller for the price agreed at the contract formation date.

In practice futures are traded on exchanges (as opposed to Over The Counter - OTC trading) for standardised quantities and qualities of the underlying. The prices are [marked to market](http://en.wikipedia.org/wiki/Mark-to-market_accounting#Marking-to-market_a_derivatives_position) every day. Futures are incredibly liquid and are used heavily for speculative purposes. While futures were often utilised to hedge the prices of agricultural or industrial goods, a futures contract can be formed on any tangible or intangible underlying such as stock indices, interest rates of foreign exchange values.

A detailed list of all the symbol codes used for futures contracts across various exchanges can be found on the CSI Data site: [Futures Factsheet.](http://www.csidata.com/factsheets/factsheet-futures.html)

The main dierence between a futures contract and equity ownership is the fact that a futures contract has a limited window of availability by virtue of the expiration date. At any one instant there will be a variety of futures contracts on the same underlying all with varying dates of expiry. The contract with the nearest date of expiry is known as the near contract. The problem we face as quantitative traders is that at any point in time we have a choice of multiple contracts with which to trade. Thus we are dealing with an overlapping set of time series rather than a continuous stream as in the case of equities or foreign exchange.

The goal of this section is to outline various approaches to constructing a continuous stream of contracts from this set of multiple series and to highlight the tradeos associated with each technique.

#### Forming a Continuous Futures Contract

The main diculty with trying to generate a continuous contract from the underlying contracts with varying deliveries is that the contracts do not often trade at the same prices. Thus situations arise where they do not provide a smooth splice from one to the next. This is due to [contango](http://en.wikipedia.org/wiki/Contango) and [backwardation](http://en.wikipedia.org/wiki/Backwardation) eects. There are various approaches to tackling this problem, which we now discuss.

Unfortunately there is no single "standard" method for joining futures contracts together in the nancial industry. Ultimately the method chosen will depend heavily upon the strategy employing the contracts and the method of execution. Despite the fact that no single method exists there are some common approaches:

The Back/Forward ("Panama") Adjustment method alleviates the "gap" across multiple contracts by shifting each contract such that the individual deliveries join in a smooth manner to the adjacent contracts. Thus the open/close across the prior contracts at expiry matches up.

The key problem with the Panama method includes the introduction of a trend bias, which will introduce a large drift to the prices. This can lead to negative data for suciently historical contracts. In addition there is a loss of the relative price dierences due to an absolute shift in values. This means that returns are complicated to calculate (or just plain incorrect).

The Proportionality Adjustment approach is similar to the adjustment methodology of handling stock splits in equities. Rather than taking an absolute shift in the successive contracts, the ratio of the older settle (close) price to the newer open price is used to proportionally adjust the prices of historical contracts. This allows a continous stream without an interruption of the calculation of percentage returns.

The main issue with proportional adjustment is that any trading strategies reliant on an absolute price level will also have to be similarly adjusted in order to execute the correct signal. This is a problematic and error-prone process. Thus this type of continuous stream is often only useful for summary statistical analysis, as opposed to direct backtesting research.

The Rollover/Perpetual Series method creates a continuous contract of successive contracts by taking a linearly weighted proportion of each contract over a number of days to ensure a smoother transition between each.

For example consider ve smoothing days. The price on day 1, P1, is equal to 80% of the far contract price (F1) and 20% of the near contract price (N1). Similarly, on day 2 the price is P<sup>2</sup> = 0.6 × F<sup>2</sup> + 0.4 × N2. By day 5 we have P<sup>5</sup> = 0.0 × F<sup>5</sup> + 1.0 × N<sup>5</sup> = N<sup>5</sup> and the contract then just becomes a continuation of the near price. Thus after ve days the contract is smoothly transitioned from the far to the near.

The problem with the rollover method is that it requires trading on all ve days, which can increase transaction costs. There are other less common approaches to the problem but we will avoid them here.

The remainder of the section will concentrate on implementing the perpetual series method as this is most appropriate for backtesting. It is a useful way to carry out strategy pipeline research.

We are going to stitch together the WTI Crude Oil "near" and "far" futures contract (symbol CL) in order to generate a continuous price series. At the time of writing (January 2014), the near contract is [CLF2014](http://www.quandl.com/OFDP/FUTURE_CLF2014) (January) and the far contract is [CLG2014](http://www.quandl.com/OFDP/FUTURE_CLG2014) (February).

In order to carry out the download of futures data I've made use of the [Quandl](http://www.quandl.com/) plugin. Make sure to set the correct Python virtual environment on your system and install the Quandl package by typing the following into the terminal:

#### pip install Quandl

Now that the Quandl package is intalled, we need to make use of NumPy and pandas in order to carry out the rollover construction. Create a new le and enter the following import statements:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# cont_futures.py
from __future__ import print_function
import datetime
import numpy as np
import pandas as pd
```

**import** Quandl

The main work is carried out in the futures\_rollover\_weights function. It requires a starting date (the rst date of the near contract), a dictionary of contract settlement dates (expiry\_dates), the symbols of the contracts and the number of days to roll the contract over (defaulting to ve). The comments below explain the code:

```
def futures_rollover_weights(start_date, expiry_dates,
    contracts, rollover_days=5):
    """This constructs a pandas DataFrame that contains weights
    (between 0.0 and 1.0) of contract positions to hold in order to
    carry out a rollover of rollover_days prior to the expiration of
    the earliest contract. The matrix can then be 'multiplied' with
    another DataFrame containing the settle prices of each
    contract in order to produce a continuous time series
    futures contract."""
    # Construct a sequence of dates beginning
    # from the earliest contract start date to the end
    # date of the final contract
    dates = pd.date_range(start_date, expiry_dates[-1], freq='B')
    # Create the 'roll weights' DataFrame that will store the multipliers for
    # each contract (between 0.0 and 1.0)
    roll_weights = pd.DataFrame(np.zeros((len(dates), len(contracts))),
                                index=dates, columns=contracts)
    prev_date = roll_weights.index[0]
    # Loop through each contract and create the specific weightings for
    # each contract depending upon the settlement date and rollover_days
    for i, (item, ex_date) in enumerate(expiry_dates.iteritems()):
        if i < len(expiry_dates) - 1:
```

```
roll_weights.ix[prev_date:ex_date - pd.offsets.BDay(), item] = 1
        roll_rng = pd.date_range(end=ex_date - pd.offsets.BDay(),
                                 periods=rollover_days + 1, freq='B')
        # Create a sequence of roll weights (i.e. [0.0,0.2,...,0.8,1.0]
        # and use these to adjust the weightings of each future
        decay_weights = np.linspace(0, 1, rollover_days + 1)
        roll_weights.ix[roll_rng, item] = 1 - decay_weights
        roll_weights.ix[roll_rng,
            expiry_dates.index[i+1]] = decay_weights
    else:
        roll_weights.ix[prev_date:, item] = 1
    prev_date = ex_date
return roll_weights
```

Now that the weighting matrix has been produced, it is possible to apply this to the individual time series. The main function downloads the near and far contracts, creates a single DataFrame for both, constructs the rollover weighting matrix and then nally produces a continuous series of both prices, appropriately weighted:

```
if __name__ == "__main__":
    # Download the current Front and Back (near and far) futures contracts
    # for WTI Crude, traded on NYMEX, from Quandl.com. You will need to
    # adjust the contracts to reflect your current near/far contracts
    # depending upon the point at which you read this!
    wti_near = Quandl.get("OFDP/FUTURE_CLF2014")
    wti_far = Quandl.get("OFDP/FUTURE_CLG2014")
    wti = pd.DataFrame({'CLF2014': wti_near['Settle'],
                        'CLG2014': wti_far['Settle']}, index=wti_far.index)
    # Create the dictionary of expiry dates for each contract
    expiry_dates = pd.Series(
        {'CLF2014': datetime.datetime(2013, 12, 19),
         'CLG2014': datetime.datetime(2014, 2, 21)}).order()
    # Obtain the rollover weighting matrix/DataFrame
    weights = futures_rollover_weights(wti_near.index[0],
                                       expiry_dates, wti.columns)
    # Construct the continuous future of the WTI CL contracts
    wti_cts = (wti * weights).sum(1).dropna()
    # Output the merged series of contract settle prices
    print(wti_cts.tail(60))
```

The output is as follows:

2013-10-14 102.230 2013-10-15 101.240 2013-10-16 102.330 2013-10-17 100.620 2013-10-18 100.990 2013-10-21 99.760 2013-10-22 98.470 2013-10-23 97.000 2013-10-24 97.240 2013-10-25 97.950 ..

| 2013-12-24 | 99.220                     |
|------------|----------------------------|
| 2013-12-26 | 99.550                     |
| 2013-12-27 | 100.320                    |
| 2013-12-30 | 99.290                     |
| 2013-12-31 | 98.420                     |
| 2014-01-02 | 95.440                     |
| 2014-01-03 | 93.960                     |
| 2014-01-06 | 93.430                     |
| 2014-01-07 | 93.670                     |
| 2014-01-08 | 92.330                     |
|            | Length: 60, dtype: float64 |
|            |                            |

It can be seen that the series is now continuous across the two contracts. This can be extended to handle multiple deliveries across a variety of years, depending upon your backtesting needs.
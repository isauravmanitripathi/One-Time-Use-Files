# **Chapter 14. The FXCM Trading Platform**

Financial institutions like to call what they do trading. Let's be honest. It's not trading; it's betting. Graydon Carter

This chapter introduces the trading platform from FXCM Group, LLC ("FXCM" hereafter), with its RESTful and streaming application programming interface (API), as well as the Python wrapper package fxcmpy. FXCM offers to retail and institutional traders a number of financial products that can be traded both via traditional trading applications and programmatically via the API. The focus of the products lies on currency pairs as well as contracts for difference (CFDs) on major stock indices and commodities, *etc.*

### **RISK DISCLAIMER**

Trading forex/CFDs on margin carries a high level of risk and may not be suitable for all investors as you could sustain losses in excess of deposits. Leverage can work against you. The products are intended for retail and professional clients. Due to the certain restrictions imposed by the local law and regulation, German resident retail client(s) could sustain a total loss of deposited funds but are not subject to subsequent payment obligations beyond the deposited funds. Be aware and fully understand all risks associated with the market and trading. Prior to trading any products, carefully consider your financial situation and experience level. Any opinions, news, research, analyses, prices, or other information is provided as general market commentary, and does not constitute investment advice. The market commentary has not been prepared in accordance with legal requirements designed to promote the independence of investment research, and it is therefore not subject to any prohibition on dealing ahead of dissemination. FXCM and the author will not accept liability for any loss or damage, including without limitation to, any loss of profit, which may arise directly or indirectly from use of or reliance on such information.

The trading platform of FXCM allows even individual traders with smaller capital positions to implement and deploy algorithmic trading strategies.

This chapter covers the basic functionalities of the FXCM trading API and the fxcmpy Python package required to implement an automated algorithmic trading strategy programmatically. It is structured as follows:

### *"Getting Started"*

This section shows how to set up everything to work with the FXCM REST API for algorithmic trading.

### *"Retrieving Data"*

This section shows how to retrieve and work with financial data (down to the tick level).

### *"Working with the API"*

This section illustrates typical tasks implemented using the REST API, such as retrieving historical and streaming data, placing orders, and looking up account information.

## **Getting Started**

Detailed documentation of the FXCM API is found at *[https://fxcm.github.io/rest](https://fxcm.github.io/rest-api-docs)api-docs*. To install the Python wrapper package fxcmpy, execute this command in the shell:

pip install fxcmpy

The documentation for the fxcmpy package is found at *<http://fxcmpy.tpq.io>*.

To get started with the FXCM trading API and the fxcmpy package, a free demo account with FXCM is [sufficient.](https://www.fxcm.com/uk/forex-trading-demo/) <sup>1</sup> The next step is to create a unique API token — say, YOUR\_FXCM\_API\_TOKEN — from within the demo account. A connection to the API is then opened, for example, via:

```
import fxcmpy
api = fxcmpy.fxcmpy(access_token=YOUR_FXCM_API_TOKEN, log_level='error')
```

Alternatively, a configuration file (say, *fxcm.cfg*) can be used to connect to the API. This file's contents should look as follows:

```
[FXCM]
log_level = error
log_file = PATH_TO_AND_NAME_OF_LOG_FILE
access_token = YOUR_FXCM_API_TOKEN
```

One can then connect to the API via:

```
import fxcmpy
api = fxcmpy.fxcmpy(config_file='fxcm.cfg')
```

Connects to the demo server.

By default, the fxcmpy class connects to the demo server. However, by the use of the server parameter, the connection can be made to the live trading server (if such an account exists):

```
api = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')
api = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='real')
```

Connects to the demo server.

Connects to the live trading server.

# **Retrieving Data**

FXCM provides access to historical market price data sets, such as tick data, in a prepackaged variant. This means that one can retrieve, for instance, compressed files from FXCM servers that contain tick data for the EUR/USD exchange rate for week 26 of 2018, as described in the following subsection. The retrieval of historical candles data from the API is explained in the subsequent subsection.

### **Retrieving Tick Data**

For a number of currency pairs, FXCM provides historical tick data. The fxcmpy package makes retrieval of such tick data and working with it convenient. First, some imports:

```
In [1]: import time
        import numpy as np
        import pandas as pd
        import datetime as dt
        from pylab import mpl, plt
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
```

Second, a look at the available symbols (currency pairs) for which tick data is available:

```
In [3]: from fxcmpy import fxcmpy_tick_data_reader as tdr
In [4]: print(tdr.get_available_symbols())
        ('AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'EURAUD', 'EURCHF',
         'EURGBP', 'EURJPY', 'EURUSD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'GBPUSD',
         'GBPCHF', 'GBPJPY', 'GBPNZD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD',
         'USDCAD', 'USDCHF', 'USDJPY')
```

The following code retrieves one week's worth of tick data for a single symbol. The resulting pandas DataFrame object has more than 1.5 million data rows:

```
In [5]: start = dt.datetime(2018, 6, 25)
        stop = dt.datetime(2018, 6, 30)
In [6]: td = tdr('EURUSD', start, stop)
In [7]: td.get_raw_data().info()
        <class 'pandas.core.frame.DataFrame'>
        Index: 1963779 entries, 06/24/2018 21:00:12.290 to 06/29/2018
         20:59:00.607
        Data columns (total 2 columns):
        Bid float64
        Ask float64
        dtypes: float64(2)
        memory usage: 44.9+ MB
In [8]: td.get_data().info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 1963779 entries, 2018-06-24 21:00:12.290000 to 2018-06-29
         20:59:00.607000
        Data columns (total 2 columns):
        Bid float64
```

```
Ask float64
       dtypes: float64(2)
       memory usage: 44.9 MB
In [9]: td.get_data().head()
Out[9]: Bid Ask
       2018-06-24 21:00:12.290 1.1662 1.16660
       2018-06-24 21:00:16.046 1.1662 1.16650
       2018-06-24 21:00:22.846 1.1662 1.16658
       2018-06-24 21:00:22.907 1.1662 1.16660
       2018-06-24 21:00:23.441 1.1662 1.16663
```

This retrieves the data file, unpacks it, and stores the raw data in a DataFrame object (as an attribute to the resulting object).

The td.get\_raw\_data() method returns the DataFrame object with the raw data; i.e., with the index values still being str objects.

The td.get\_data() method returns a DataFrame object for which the index has been transformed to a DatetimeIndex.

Since the tick data is stored in a DataFrame object, it is straightforward to pick a subset of the data and to implement typical financial analytics tasks on it. Figure 14-1 shows a plot of the mid prices derived for the subset and a simple moving average (SMA):

```
In [10]: sub = td.get_data(start='2018-06-29 12:00:00',
                         end='2018-06-29 12:15:00')
In [11]: sub.head()
Out[11]: Bid Ask
        2018-06-29 12:00:00.011 1.16497 1.16498
        2018-06-29 12:00:00.071 1.16497 1.16497
        2018-06-29 12:00:00.079 1.16497 1.16498
        2018-06-29 12:00:00.091 1.16495 1.16498
        2018-06-29 12:00:00.205 1.16496 1.16498
In [12]: sub['Mid'] = sub.mean(axis=1)
In [13]: sub['SMA'] = sub['Mid'].rolling(1000).mean()
In [14]: sub[['Mid', 'SMA']].plot(figsize=(10, 6), lw=0.75);
```

Picks a subset of the complete data set.

Calculates the mid prices from the bid and ask prices.

![](_page_7_Figure_1.jpeg)

![](_page_7_Figure_2.jpeg)

Derives SMA values over intervals of 1,000 ticks.

*Figure 14-1. Historical mid tick prices for EUR/USD and SMA*

### **Retrieving Candles Data**

FXCM also provides access to historical candles data (beyond the API) — i.e., to data for certain homogeneous time intervals ("bars") with open, high, low, and close values for both bid and ask prices.

First, a look at the available symbols for which candles data is provided:

```
In [15]: from fxcmpy import fxcmpy_candles_data_reader as cdr
In [16]: print(cdr.get_available_symbols())
         ('AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'EURAUD', 'EURCHF',
          'EURGBP', 'EURJPY', 'EURUSD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'GBPUSD',
          'GBPCHF', 'GBPJPY', 'GBPNZD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD',
          'USDCAD', 'USDCHF', 'USDJPY')
```

Second, the data retrieval itself. It is similar to the tick data retrieval. The only difference is that a period value — i.e., the bar length — needs to be specified (e.g., m1 for one minute, H1 for one hour, or D1 for one day):

```
In [17]: start = dt.datetime(2018, 5, 1)
        stop = dt.datetime(2018, 6, 30)
In [18]: period = 'H1'
In [19]: candles = cdr('EURUSD', start, stop, period)
In [20]: data = candles.get_data()
In [21]: data.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 1080 entries, 2018-04-29 21:00:00 to 2018-06-29 20:00:00
        Data columns (total 8 columns):
        BidOpen 1080 non-null float64
        BidHigh 1080 non-null float64
        BidLow 1080 non-null float64
        BidClose 1080 non-null float64
        AskOpen 1080 non-null float64
        AskHigh 1080 non-null float64
        AskLow 1080 non-null float64
        AskClose 1080 non-null float64
        dtypes: float64(8)
        memory usage: 75.9 KB
In [22]: data[data.columns[:4]].tail()
Out[22]: BidOpen BidHigh BidLow BidClose
        2018-06-29 16:00:00 1.16768 1.16820 1.16731 1.16769
        2018-06-29 17:00:00 1.16769 1.16826 1.16709 1.16781
        2018-06-29 18:00:00 1.16781 1.16816 1.16668 1.16684
        2018-06-29 19:00:00 1.16684 1.16792 1.16638 1.16774
        2018-06-29 20:00:00 1.16774 1.16904 1.16758 1.16816
In [23]: data[data.columns[4:]].tail()
```

```
Out[23]: AskOpen AskHigh AskLow AskClose
       2018-06-29 16:00:00 1.16769 1.16820 1.16732 1.16771
       2018-06-29 17:00:00 1.16771 1.16827 1.16711 1.16782
       2018-06-29 18:00:00 1.16782 1.16817 1.16669 1.16686
       2018-06-29 19:00:00 1.16686 1.16794 1.16640 1.16775
       2018-06-29 20:00:00 1.16775 1.16907 1.16760 1.16861
```

Specifies the period value.

Open, high, low, close values for the *bid* prices.

Open, high, low, close values for the *ask* prices.

To conclude this section, the following code calculates mid close prices and two SMAs, and plots the results (see Figure 14-2):

```
In [24]: data['MidClose'] = data[['BidClose', 'AskClose']].mean(axis=1)
In [25]: data['SMA1'] = data['MidClose'].rolling(30).mean()
         data['SMA2'] = data['MidClose'].rolling(100).mean()
In [26]: data[['MidClose', 'SMA1', 'SMA2']].plot(figsize=(10, 6));
```

Calculates the mid close prices from the bid and ask close prices.

Calculates two SMAs, one for a shorter time interval, one for a longer one.

![](_page_10_Figure_0.jpeg)

*Figure 14-2. Historical hourly mid close prices for EUR/USD and two SMAs*

# **Working with the API**

```
While the previous sections demonstrate retrieving prepackaged historical tick
data and candles data from FXCM servers, this section shows how to retrieve
historical data via the API. For this, a connection object to the FXCM API is
needed. Therefore, first the import of the fxcmpy package, the connection to the
API (based on the unique API token), and a look at the available instruments: In
[27]: import fxcmpy In [28]: fxcmpy.__version__ Out[28]: '1.1.33'
In [29]: api = fxcmpy.fxcmpy(config_file='../fxcm.cfg') In [30]:
instruments = api.get_instruments() In [31]: print(instruments)
['EUR/USD', 'XAU/USD', 'GBP/USD', 'UK100', 'USDOLLAR', 'XAG/USD',
'GER30', 'FRA40', 'USD/CNH', 'EUR/JPY', 'USD/JPY', 'CHN50',
'GBP/JPY', 'AUD/JPY', 'CHF/JPY', 'USD/CHF', 'GBP/CHF', 'AUD/USD',
'EUR/AUD', 'EUR/CHF', 'EUR/CAD', 'EUR/GBP', 'AUD/CAD', 'NZD/USD',
'USD/CAD', 'CAD/JPY', 'GBP/AUD', 'NZD/JPY', 'US30', 'GBP/CAD',
'SOYF', 'GBP/NZD', 'AUD/NZD', 'USD/SEK', 'EUR/SEK', 'EUR/NOK',
'USD/NOK', 'USD/MXN', 'AUD/CHF', 'EUR/NZD', 'USD/ZAR', 'USD/HKD',
'ZAR/JPY', 'BTC/USD', 'USD/TRY', 'EUR/TRY', 'NZD/CHF', 'CAD/CHF',
'NZD/CAD', 'TRY/JPY', 'AUS200', 'ESP35', 'HKG33', 'JPN225',
'NAS100', 'SPX500', 'Copper', 'EUSTX50', 'USOil', 'UKOil', 'NGAS',
'Bund']
```

This connects to the API; adjust the path/filename.

### **Retrieving Historical Data**

Once connected, data retrieval for specific time intervals is accomplished via a single method call. When using the get\_candles() method, the parameter period can be one of m1, m5, m15, m30, H1, H2, H3, H4, H6, H8, D1, W1, or M1. The following code gives a few examples. Figure 14-3 shows one-minute bar ask close prices for the EUR/USD instrument (currency pair): In [32]: candles = api.get\_candles('USD/JPY', period='D1', number=10) In [33]: candles[candles.columns[:4]] Out[33]: bidopen bidclose bidhigh bidlow date 2018-10-08 21:00:00 113.760 113.219 113.937 112.816 2018-10-09 21:00:00 113.219 112.946 113.386 112.863 2018-10-10 21:00:00 112.946 112.267 113.281 112.239 2018-10-11 21:00:00 112.267 112.155 112.528 111.825 2018-10-12 21:00:00 112.155 112.200 112.491 111.873 2018-10-14 21:00:00 112.163 112.130 112.270 112.109 2018-10-15 21:00:00 112.130 111.758 112.230 111.619 2018-10-16 21:00:00 112.151 112.238 112.333 111.727 2018-10-17 21:00:00 112.238 112.636 112.670 112.009 2018-10-18 21:00:00 112.636 112.168 112.725 111.942 In [34]: candles[candles.columns[4:]] Out[34]: askopen askclose askhigh asklow tickqty date 2018-10-08 21:00:00 113.840 113.244 113.950 112.827 184835 2018-10-09 21:00:00 113.244 112.970 113.399 112.875 321755 2018-10-10 21:00:00 112.970 112.287 113.294 112.265 329174 2018-10-11 21:00:00 112.287 112.175 112.541 111.835 568231 2018-10-12 21:00:00 112.175 112.243 112.504 111.885 363233 2018-10-14 21:00:00 112.219 112.181 112.294 112.145 581 2018-10-15 21:00:00 112.181 111.781 112.243 111.631 322304 2018-10- 16 21:00:00 112.163 112.271 112.345 111.740 253420 2018-10-17 21:00:00 112.271 112.664 112.682 112.022 542166 2018-10-18 21:00:00 112.664 112.237 112.738 111.955 369012 In [35]: start = dt.datetime(2017, 1, 1) end = dt.datetime(2018, 1, 1) In [36]: candles = api.get\_candles('EUR/GBP', period='D1', start=start, stop=end) In [37]: candles.info() <**class** '**pandas**.core.frame.DataFrame'> DatetimeIndex: 309 entries, 2017-01- 03 22:00:00 to 2018-01-01 22:00:00 Data columns (total 9 columns): bidopen 309 non-null float64 bidclose 309 non-null float64 bidhigh 309 non-null float64 bidlow 309 non-null float64 askopen 309 non-

```
null float64 askclose 309 non-null float64 askhigh 309 non-null
float64 asklow 309 non-null float64 tickqty 309 non-null int64
dtypes: float64(8), int64(1) memory usage: 24.1 KB In [38]: candles
= api.get_candles('EUR/USD', period='m1', number=250) In [39]:
candles['askclose'].plot(figsize=(10, 6))
```

Retrieves the 10 most recent end-of-day prices.

Retrieves end-of-day prices for a whole year.

Retrieves the most recent one-minute bar prices available.

![](_page_13_Figure_7.jpeg)

*Figure 14-3. Historical ask close prices for EUR/USD (minute bars)*

### **Retrieving Streaming Data**

While *historical* data is important to, for example, backtest algorithmic trading strategies, continuous access to *real-time or streaming* data (during trading hours) is required to deploy and automate algorithmic trading strategies. The FXCM API allows for the subscription to real-time data streams for all instruments. The fxcmpy wrapper package supports this functionality, among others, in that it allows users to provide user-defined functions (so-called *callback functions*) to process the real-time data stream.

The following code presents a simple callback function — it only prints out selected elements of the data set retrieved — and uses it to process data retrieved in real time after subscribing to the desired instrument (here, EUR/USD):

```
In [40]: def output(data, dataframe):
            print('%3d | %s | %s | %6.5f, %6.5f'
                  % (len(dataframe), data['Symbol'],
                     pd.to_datetime(int(data['Updated']), unit='ms'),
                     data['Rates'][0], data['Rates'][1]))
In [41]: api.subscribe_market_data('EUR/USD', (output,))
          1 | EUR/USD | 2018-10-19 11:36:39.735000 | 1.14694, 1.14705
          2 | EUR/USD | 2018-10-19 11:36:39.776000 | 1.14694, 1.14706
          3 | EUR/USD | 2018-10-19 11:36:40.714000 | 1.14695, 1.14707
          4 | EUR/USD | 2018-10-19 11:36:41.646000 | 1.14696, 1.14708
          5 | EUR/USD | 2018-10-19 11:36:41.992000 | 1.14696, 1.14709
          6 | EUR/USD | 2018-10-19 11:36:45.131000 | 1.14696, 1.14708
          7 | EUR/USD | 2018-10-19 11:36:45.247000 | 1.14696, 1.14709
In [42]: api.get_last_price('EUR/USD')
Out[42]: Bid 1.14696
        Ask 1.14709
        High 1.14775
        Low 1.14323
        Name: 2018-10-19 11:36:45.247000, dtype: float64
In [43]: api.unsubscribe_market_data('EUR/USD')
          8 | EUR/USD | 2018-10-19 11:36:48.239000 | 1.14696, 1.14708
```

The callback function that prints out certain elements of the retrieved data set.

The subscription to a specific real-time data stream; data is processed asynchronously as long as there is no "unsubscribe" event.

During the subscription, the .get\_last\_price() method returns the last available data set.

This unsubscribes from the real-time data stream.

### **CALLBACK FUNCTIONS**

Callback functions are a flexible means to process real-time streaming data based on a Python function or even multiple such functions. They can be used for simple tasks, such as the printing of incoming data, or complex tasks, such as generating trading signals based on online trading algorithms (see Chapter 16).

### **Placing Orders**

The FXCM API allows the placement and management of all types of orders that are also available via the trading application of FXCM (such as entry orders or trailing stop loss orders). <sup>2</sup> However, the following code illustrates basic market buy and sell orders only since they are in general sufficient to at least get started with algorithmic trading. It first verifies that there are no open positions, then opens different positions (via the create\_market\_buy\_order() method):

```
In [44]: api.get_open_positions()
Out[44]: Empty DataFrame
        Columns: []
        Index: []
In [45]: order = api.create_market_buy_order('EUR/USD', 10)
In [46]: sel = ['tradeId', 'amountK', 'currency',
               'grossPL', 'isBuy']
In [47]: api.get_open_positions()[sel]
Out[47]: tradeId amountK currency grossPL isBuy
        0 132607899 10 EUR/USD 0.17436 True
In [48]: order = api.create_market_buy_order('EUR/GBP', 5)
In [49]: api.get_open_positions()[sel]
Out[49]: tradeId amountK currency grossPL isBuy
        0 132607899 10 EUR/USD 0.17436 True
        1 132607928 5 EUR/GBP -1.53367 True
```

Shows the open positions for the connected (default) account.

Opens a position of 100,000 in the EUR/USD currency pair. 3

Shows the open positions for selected elements only.

Opens another position of 50,000 in the EUR/GBP currency pair.

While the create\_market\_buy\_order() function opens or increases positions, the create\_market\_sell\_order() function allows one to close or decrease positions. There are also more general methods that allow the closing out of positions, as the following code illustrates:

```
In [50]: order = api.create_market_sell_order('EUR/USD', 3)
In [51]: order = api.create_market_buy_order('EUR/GBP', 5)
In [52]: api.get_open_positions()[sel]
Out[52]: tradeId amountK currency grossPL isBuy
        0 132607899 10 EUR/USD 0.17436 True
        1 132607928 5 EUR/GBP -1.53367 True
        2 132607930 3 EUR/USD -1.33369 False
        3 132607932 5 EUR/GBP -1.64728 True
In [53]: api.close_all_for_symbol('EUR/GBP')
In [54]: api.get_open_positions()[sel]
Out[54]: tradeId amountK currency grossPL isBuy
        0 132607899 10 EUR/USD 0.17436 True
        1 132607930 3 EUR/USD -1.33369 False
In [55]: api.close_all()
In [56]: api.get_open_positions()
Out[56]: Empty DataFrame
        Columns: []
        Index: []
```

This reduces the position in the EUR/USD currency pair.

This increases the position in the EUR/GBP currency pair.

For EUR/GBP there are now two open long positions; contrary to the EUR/USD position, they are not netted.

The close\_all\_for\_symbol() method closes all positions for the specified symbol.

The close\_all() method closes all open positions.

### **Account Information**

Beyond, for example, open positions, the FXCM API allows retrieval of more general account information as well. For example, one can look up the default account (if there are multiple accounts) or get an overview of the equity and margin situation: In [57]: api.get\_default\_account() Out[57]: 1090495 In [58]: api.get\_accounts().T Out[58]: 0 accountId 1090495 accountName 01090495 balance 4915.2 dayPL -41.97 equity 4915.2 grossPL 0 hedging Y mc N mcDate ratePrecision 0 t 6 usableMargin 4915.2 usableMargin3 4915.2 usableMargin3Perc 100 usableMarginPerc 100 usdMr 0 usdMr3 0

Shows the default accountId value.

Shows for all accounts the financial situation and some parameters.

# **Conclusion**

This chapter is about the REST API of FXCM for algorithmic trading and covers the following topics:

- Setting everything up for API usage
- Retrieving historical tick data
- Retrieving historical candles data
- Retrieving streaming data in real time
- Placing market buy and sell orders
- Looking up account information

The FXCM API and the fxcmpy wrapper package provide, of course, more functionality, but these are the basic building blocks needed to get started with algorithmic trading.
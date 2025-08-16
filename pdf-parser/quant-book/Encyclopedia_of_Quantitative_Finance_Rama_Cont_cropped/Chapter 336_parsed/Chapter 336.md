# **High-frequency Data**

High-frequency financial data usually refer to data sampled at a time horizon smaller than a trading day [5, 6, 8]. In this sense, high-frequency data are essentially intended as intraday data. However, the meaning of high frequency has changed over the years following the availability of more and more detailed information on the trading process. A stricter viewpoint considers those financial records where no kind of temporal aggregation is done as highfrequency data. The use of such data in finance is recent and dates to the late 1980s [16]. Among the first high-frequency databases worth mentioning are the Berkeley Option Data, containing bid–ask quotes and trade prices of option traded at the Chicago Board Option Exchange (CBOE), the TORQ database containing trades and quotes relative to 144 New York Stock Exchange (NYSE) stocks (1990–1991), the HFDF93 database of foreign exchange data released by Olsen & Associates (1992–1993), and the computerized trade reconstruction records maintained by the Commodities Futures Trading Commission (CFTC). In the following, we describe the most common types of datasets.

# **• Tick-by-tick data**

The simplest form of financial data without any temporal aggregation is the so-called tick-by-tick data. In this type of data, all transactions are recorded. Typically, the dataset contains information on the time, price, and volume of each trade. Clearly, the time frequency at which data are recorded is not fixed, but can be different in different phases of a trading day (see below).

# **• Trade and quote data**

A more refined type of dataset contains information on transactions and best quotes (Level 1 data). Transaction data usually contain the transaction prices, the time when the transaction occurred, and the exchanged volume. Quote data usually contain information about the best bid and the best ask price and the available volume at these prices. Quote data are usually updated every time there is a quote change either in the price or in the volume. The availability of trade and quote data allows one to infer whether the transaction was buyer or seller initiated. The idea is to compare the trade price with the bid and ask prices of the prevailing quote, which is the most recent past quote. One of the most famous methods to assign signs to trades is by using the Lee and Ready algorithm [10]. However in some markets (e.g. NYSE), the signing process is not always straightforward because of some data and market subtleties; for a more recent discussion, see, for example, [14].

One of the most famous trade and quote database is the TAQ (Trade and Quote) database, maintained by NYSE since 1993. The trades and quotes data are available for a wide range of stock exchanges and markets worldwide.

# **• Order book data**

The next level of high-frequency data resolution (Level 2 data) includes complete information about the order book in a given market. While the quote data contain information only on the best bid and best ask prices, in the order book data, all limit orders to buy or sell are recorded both when they are placed and when they expire or are canceled. This type of dataset allows one to reconstruct the limit order book at any instant of time and to follow the market dynamics more closely. A variant of this type of database contains the transaction data and the price and volume of a fixed number (usually 5 or 10) of best price levels on both sides of the order book. The use of such data dates back to the early 1990s [1]. One of the most popular databases of order book data is the Rebuild Order Book maintained by the London Stock Exchange (LSE). A different type of order book dataset provides a snapshot of the book with a fixed time frequency, rather than providing each individual event affecting the order-book dynamics. For example, the OpenBook database of the NYSE provides a snapshot of the order book refreshed every second.

# **• Market member data**

Recently, a few markets have released financial datasets with another level of resolution. These datasets contain also the identity of the market members (and/or brokers, traders) involved

![](_page_1_Figure_1.jpeg)

**Figure 1** Size in gigabytes of the trade and quote (TAQ) database of the New York Stock Exchange during the period 1995–2003. The dashed line is a fit with an exponential function and the estimated doubling time is 1.5 years

in each transaction and sometimes of the market member who placed each limit order. For reasons of privacy, the identity of the market member is often coded, and, in some cases, the coding is different for different stocks or different time periods. This type of database allows one to identify the different strategies followed by different traders [12]. For example, the Spanish Stock Exchange releases such a database where the market member identity is completely transparent. In other markets, this information is recorded although it is not transparent to the agents during the market activity.

Two important aspects of high-frequency data are data size and time resolution. The size of highfrequency data has significantly increased in the last years because of the explosion of trading activity in financial markets. As an example, Figure 1 shows the approximate size (in gigabytes) of the TAQ database of the NYSE for the years from 1995 to 2003. The size has increased more than 50 times in magnitude, and the growth seems to be well fitted by an exponential law with a doubling time of about 1.5 years. More recently, the total volume of data related to United States large caps on a typical day of 2007 was 57 million lines, approximately a gigabyte of stored data.

The size of high-frequency data increases also when the level of data resolution is increased, for example, data on a high cap LSE stock in 2002 occupy roughly 12 kB for daily data, 15 MB for trade data, and more than 100 MB for order book data.

Concerning the issue of time resolution, very often, high-frequency data are recorded with a 1-s resolution. While this resolution was sufficient several years ago, nowadays, this resolution is insufficient to allow a correct time ordering of the market events. To give an example, at the end of 2007, Apple had on average 6 transactions per second, and on the order of 100 events per second affecting the order book. With this event frequency, it is very hard to infer the correct time ordering of events within a second. Of late, high-frequency databases are either released with a 1-ms resolution, or still have the 1-s resolution but the events are correctly sorted out within the second, according to the actual order of events.

### **Issues with High-frequency Data**

Working with high- and ultrahigh-frequency financial data presents many additional issues when compared to the more traditional analysis of daily or weekly data. Besides the fact that high-frequency data analysis is computationally more demanding, the issues involved can be categorized into at least seven classes, which we have chosen as follows: data cleaning, irregular temporal spacing, discreteness, variable definition, daily periodicities, temporal correlations, and market structure; we briefly review these in the following.

# **• Data cleaning**

High-frequency data are often plagued by errors. Therefore it is very often necessary to perform a few preliminary steps to clean the data. A typical problem is the identification and removal of outliers. Such a cleaning procedure is quite problematic, given the arbitrariness in the definition of outliers. Typically, one considers a window of neighboring records, called the *filtering window*, and judges the plausibility of a record according to the statistical properties of the other records in the filtering window [2, 6].

# **• Irregular temporal spacing**

Events such as trades, quotes, and limit order placement do not occur at regular intervals of time either in tick-by-tick data or in limit order-book data; rather they occur at irregularly spaced time intervals. In this framework, the time between events is itself a random variable with often nontrivial temporal correlations. Moreover, there are statistical dependencies between the time interval between two trades and the variables characterizing them. Figure 2 shows an example of the occurrence of irregular time spacing in a financial time series.

There are two possible approaches to the problem of irregular temporal spacing. In the first approach, one extracts a regularly spaced time series by using some kind of interpolation scheme. For example, the *previous tick interpolation* scheme uses the past most recent record as the value of the variable at a given instant of time. Alternatively, one can use a linear interpolation between the past most recent and the future most recent events to assign a value to a variable [6]. Interpolation schemes may introduce spurious correlations. The second approach makes use of models that explicitly take into account the irregular temporal spacing. Point processes [3] give a natural description of irregularly spaced events. There are several classes of models dealing with this issue, including the autoregressive conditional duration model [4] and the continuous time random walk model [13].

# **• Discreteness**

When one starts dealing with events at the highest resolution level, the issue of variable discreteness cannot be neglected. For example, asset prices can only assume integer multiples of the tick size, which is the smallest allowable price change. Similarly, the volume of an order must be integer multiples of the minimum allowable number of shares in a single order. The discretization unit can also be variable in time. For example, in the last years US equities passed from a large tick

![](_page_2_Figure_9.jpeg)

**Figure 2** Graphical representation of the dynamics of the order book of the stock AstraZeneca traded at the London Stock Exchange during a 10-min interval on September 4, 2002. The filled (empty) circles are buyer- (seller-) initiated transactions. The thick lines are the bid and the ask price. The dashed lines are limit orders

#### 4 **High-frequency Data**

size  $(1/8$  of a dollar) to a small tick size (one cent, since  $2001$ ). The reduction of tick size has been related to several empirical facts, such as the decrease of the spreads and depths of the limit order book [7]. Many statistical models treat the variables as continuous variables, whereas from the above discussion, it is clear that at very high frequency, the variables should be treated as discrete.

### Variable definition

The availability of data with the resolution of quotes or of the order book raises the problem of the proper definition of variables. As an example, consider the price of an asset. At a given instant of time, there are many prices that can be considered as the relevant representative price. The most common one is the midprice, which is the mean of the best bid and the best ask prices. However, significantly different volumes may be available at the bid and at the ask, and one may wonder whether a volume-weighted average between the bid and the ask prices is a more proper definition of price. If one wants to include not only the information on the volume at the best price but also the information of volume in part or in the entire order book, then the number of possible definitions of average price increases significantly.

### **Daily periodicity**

Financial time series at high frequency display strong daily periodicity. Among the variables having a daily periodicity, we mention volatility, trading volume, number of transactions, time between trades, and spread. The daily periodicity is due to the fact that the trading activity is not constant throughout the day. Typically, the trading activity is high around the opening. it decreases until midday, and finally increases toward the end of the trading day. This is sometimes referred to as a *U*-shape pattern. An example is shown in Figure 3. Figure  $3(a)$ –(c) shows the mean intraday pattern for volume, volatility. and number of trades for General Electric at the NYSE. The volatility proxy is the absolute price

![](_page_3_Figure_7.jpeg)

**Figure 3** Examples of the intraday pattern. One bin corresponds to 15 min and the x-axis shows the hour of the day. The figure shows the traded volume (a), the absolute price change (b), and the number of trades (c) of General Electric at the NYSE during the period 2002–2003. (d) The number of trades of AstraZeneca exchanged in the electronic market (SET1) of the LSE during the period May 2000–December 2002

change here. The three quantities display a Ushape, even if the detailed shape of the U is quite different. Figure 3(d) shows the mean intraday pattern of the number of trades for AstraZeneca at the LSE. By comparing panel Figure 3(c) and (d), it is evident how the intraday pattern for a variable can be strongly dependent on the considered market. Note that in Figure 3(d) there is almost a doubling of the frequency of trades around 14 : 30. This is the London time corresponding to the opening of US markets. More generally, in many markets, one often observes peaks of activity or regime changes that correspond to the opening or closing of markets in other time zones.

One important consequence of daily periodicity is that financial time series are not stationary because the statistical properties of a variable depend on the time of the day. Moreover, the presence of the U-shape produces periodicities in financial time series. For these reasons, one is often interested in removing these "trivial" temporal dependencies from the series. This can be done, for example, by dividing the variable by its mean value observed in the sample at that time of the day. It is worth noting that other types of periodicity (e.g., weekly, yearly) are also present. For example, in US markets, the trading volume is larger at the middle of the week than at beginning and at the end. Usually, these periodicities are less intense than the daily periodicity.

Foreign exchange (FX) markets display different types of periodicity [6]. In fact, FX markets have no trading-hour limitations, which means that new bid–ask prices can arrive from all over the world at any time. The intraday patterns of FX variables are therefore not U-shaped. Typically, FX intraday patterns show three broad peaks that correspond to the working periods in America, Europe, and East Asia. Other seasonalities are observable in the FX data, such as the intraweek patterns that arise in connection with the fact that during the weekends the market activity is much smaller.

# **• Temporal correlations**

Typically, financial variables sampled at high frequency display strong temporal correlations. Some temporal correlations are specific to the microstructure of financial markets at high frequency [9]. Other correlations are also present at a lower frequency but are more intense with intraday data. For example, Figure 4 shows the autocorrelation function of transaction price returns for the AstraZeneca (AZN) stock traded at LSE. The lags on the horizontal line are measured in event time. The autocorrelation function of transaction price returns is strongly negative at the first lag and then it rapidly decreases to zero. This is the well-known bid–ask bounce [15] and is mainly due to the presence of two trading

![](_page_4_Figure_6.jpeg)

**Figure 4** Autocorrelation function of transaction price returns (solid circles), absolute value of transaction price returns (open circles), returns of midprice sampled before each transaction (filled triangles), and returns of midprice sampled before each market event (filled squares) for the AstraZeneca (AZN) stock traded at LSE in 2002. The lags on the horizontal line are measured in event time

prices, one for buyer- and one for seller-initiated transactions. This negative autocorrelation disappears when one considers aggregate returns, and it is therefore a typical microstructural effect. Figure 4 shows also the autocorrelation function of the absolute value of trade price returns, considered here as a proxy of volatility. This autocorrelation function decays very slowly showing that persistency and volatility clustering can also been observed at the tick-by-tick timescale. It is important to stress that at this scale the sampling procedure plays an important role. As an example, Figure 4 shows the autocorrelation function of returns of the midprice sampled before each transaction and sampled before each market event (including limit order placements and cancellations). In the first case, a negative correlation at one lag is still present (though smaller than the one for trade price returns), whereas in the second case the negative correlation disappears.

Finally, many financial variables at high frequency display strong temporal persistence that can often be modeled in terms of long memory processes. Examples include transaction rate, spread, sign of the order flow, and volume (*see* **Order Flow**).

# **• Market structure**

When one works with high-frequency data, it is important to take into account the structure of the market under investigation. Many financial markets have a multiple structure composed of electronic markets, block markets, dark pools, and so on. The statistical properties of a financial variable can be quite different in different segments of the market. For example, trading volume distribution is fat tailed in the block market while it is usually thin tailed in the electronic segment [11]. Therefore, in the analysis of high-frequency data, it is important to take into account this market heterogeneity either by specializing the investigation to a given segment or by weighting the different statistical properties in a suitable way.

### **References**

[1] Biais, B., Hillion, P. & Spatt, C. (1995). An empirical analysis of the limit order book and the order flow in the Paris Bourse, *Journal of Finance* **50**, 1665–1690.

- [2] Brownlees, C.T. & Gallo, G.M. (2006). Financial econometric analysis at ultra-high frequency: data handling concerns, *Computational Statistics and Data Analysis* **51**, 2232–2245.
- [3] Cox, D.R. & Isham, V. (1980). *Point Processes*, Chapman & Hall.
- [4] Engle, R. & Russell, J. (1998). Autoregressive conditional duration: a new model for irregularly spaced data, *Econometrica* **66**, 1127–1162.
- [5] Engle, R.F. & Russell, J.R. (2006). Analysis of high frequency data, in *Handbook of Financial Econometrics*, Y. AitSahalia & L.P. Hansen, eds, North-Holland.
- [6] Gen¸cay, R., Dacorogna, M., Muller, U.A., Pictet, O. & Olsen, R. (2001). *An Introduction to High-Frequency Finance*, Academic Press.
- [7] Goldstein, M.A. & Kavajecz, K.A. (2000). Eighths, sixteenths, and market depth: changes in tick size and liquidity provision on the NYSE, *Journal of Financial Economics* **56**, 125–149.
- [8] Goodhart, C.A.E. & O'Hara, M. (1997). High frequency data in financial markets: issues and applications, *Journal of Empirical Finance* **4**, 73–114.
- [9] Hasbrouck, J. (2007). *Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading*, Oxford University Press.
- [10] Lee, C.M. & Ready, M.J. (1991). Inferring trade direction from intraday data, *Journal of Finance* **46**, 733–746.
- [11] Lillo, F., Mike, S. & Farmer, J.D. (2005). Theory for long memory in supply and demand, *Physical Review E* **71**, 066122.
- [12] Lillo, F., Moro, E., Vaglica, G. & Mantegna, R.N. (2008). Specialization and herding behavior of trading firms in a financial market, *New Journal of Physics* **10**, 043019.
- [13] Montroll, E.W. & Weiss, G.H. (1965). Random walks on lattices. II, *Journal of Mathematical Physics* **6**, 167–181.
- [14] Odders-White, E. (2000). On the occurrence and consequence of inaccurate trade classification, *Journal of Financial Markets* **3**, 259–286.
- [15] Roll, R. (1984). A simple implicit measure of the effective bid-ask spread in an efficient market, *Journal of Finance* **39**, 1127–1139.
- [16] Wood, R.A., McInish, T.H. & Ord, J.K. (1985). An investigation of transaction data for the NYSE stocks, *Journal of Finance* **40**, 723–741.

### **Related Articles**

### **Automated Trading**; **Limit Order Markets**; **Market Microstructure Effects**; **Order Flow**; **Order Types**; **Price Impact**.

FABRIZIO LILLO & SALVATORE MICCICHE`
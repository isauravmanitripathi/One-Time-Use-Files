## CHAPTER 9

# **Working with Tick Data**

 $\bullet$  rading opportunities are largely a function of the data that identifies them. As discussed in Chapter 7, the higher the data frequency, the more arbitrage opportunities appear. When researching profitable opportunities, therefore, it is important to use data that is as granular as possible. Recent microstructure research and advances in econometric modeling have facilitated a common understanding of the unique characteristics of tick data. In contrast to traditional low-frequency regularly spaced data, tick data is irregularly spaced with quotes arriving randomly at very short time intervals. The observed irregularities present researchers and traders with a wealth of information not available in low-frequency data sets. Intertrade durations may signal changes in market volatility, liquidity, and other variables, as discussed further along in this chapter.

In addition, the sheer volume of data allows researchers to produce statistically precise inferences. As noted by Dacorogna et al. (2001), large sets of data can support considerably wider ranges of input variables (parameters) because of the expanded number of allowable degrees of freedom.

Finally, the copious quantities of tick data allow researchers to use short-term data samples to make statistically significant inferences pertaining to the latest changes in the markets. Whereas a monthly set of daily data is normally deemed too short a sample to make statistically viable predictions, volumes of tick data in the same monthly sample can make such short-term estimation practical. Other frequency-specific considerations, such as intra-day seasonality, must be taken into account in assessing the sufficient number of observations.

This chapter discusses the following topics:

- Various properties of tick data
- Econometric techniques specific to tick data estimation
- How trading systems can make better trading decisions using tick data
- How trading systems can apply traditional econometric principles

### PROPERTIES OF TICK DATA

The highest-frequency data is a collection of sequential "ticks," arrivals of the latest quote, trade, price, and volume information. Tick data usually has the following properties:

- A timestamp
- A financial security identification code
- An indicator of what information it carries:
  - Bid price
  - Ask price
  - Available bid volume
  - Available ask volume
  - Last trade price
  - Last trade size
  - Option-specific data, such as implied volatility
- The market value information, such as the actual numerical value of the price, available volume, or size

A timestamp records the date and time at which the quote originated. It may be the time at which the exchange or the broker-dealer released the quote, or the time when the trading system has received the quote. The quote travel time from the exchange or the broker-dealer to the trading system can be as small as 20 milliseconds. All sophisticated systems, therefore, include milliseconds as part of their timestamps.

Part of the quote is an identifier of the financial security. In equities, the identification code can be a ticker, or, for tickers simultaneously traded on multiple exchanges, a ticker followed by the exchange symbol. For futures, the identification code can consist of the underlying security, futures expiration date, and exchange code.

The last trade price shows the price at which the last trade in the security cleared. Last trade price can differ from the bid and ask. The differences can arise when a customer posts a favorable limit order that is immediately matched by the broker without broadcasting the customer's quote. Last trade size shows the actual size of the last executed trade.

The bid quote is the highest price available for sale of the security in the market. The ask quote is the lowest price entered for buying the security at any particular time. Both bid and ask quotes are provided by other market participants through limit orders. A yet-to-be-executed limit order to buy with the highest price becomes the market bid, and a limit order to sell with the lowest price among other limit orders in the same book becomes the market ask. Available bid and ask volumes indicate the total demand and supply, respectively, at the bid and ask prices.

#### **QUANTITY AND QUALITY OF TICK DATA**

High-frequency data is voluminous. According to Dacorogna et al. (2001), the number of observations in a single day of tick-by-tick data is equivalent to 30 years of daily observations. The quality of data does not always match its quantity. Centralized exchanges generally provide accurate data on bids, asks, and volume of any trade with a reasonably timely timestamp. The information on the limit order book is less commonly available. In decentralized markets, such as foreign exchange and the interbank money market, no market-wide quotes are available at any given time. In such markets, participants are aware of the current price levels, but each institution quotes its own prices adjusted for its order book. In decentralized markets, each dealer provides his own tick data to his clients. As a result, a specific quote on a given financial instrument at any given time may vary from dealer to dealer. Reuters, Telerate, and Knight Ridder, among others, collect quotes from different dealers and disseminate them back, improving the efficiency of the decentralized markets. There are generally thought to be three anomalies in inter-dealer quote discrepancies.

Each dealer's quotes reflect that dealer's own inventory. For example, a dealer that has just sold a customer \$100 million of USD/CAD would be eager to diversify the risk of his position and avoid selling any more of USD/CAD. Most dealers are, however, obligated to transact with their clients on tradeable quotes. To incite his clients to place sell orders on USD/CAD, the dealer temporarily raises the bid quote on USD/CAD. At the same time, to encourage his clients to withhold placing buy orders, the dealer raises the ask quote on USD/CAD. Thus, dealers tend to raise both bid and ask prices whenever they are short in a particular financial instrument and lower both bid and ask prices whenever they are disproportionally long in a financial instrument.

In an anonymous marketplace, such as a dark pool, dealers as well as other market makers may "fish" for market information by sending indicative quotes that are much off the previously quoted price to assess the available demand or supply.

Dacorogna et al. (2001) note that some dealers' quotes may lag real market prices. The lag is thought to vary from milliseconds to a minute. Some dealers quote moving averages of quotes of other dealers. The dealers who provide delayed quotes usually do so to advertise their market presence in the data feed. This was particularly true when most order prices were negotiated over the telephone, allowing a considerable delay between quotes and orders. Fast-paced electronic markets discourage lagged quotes, improving the quality of markets.

#### **BID-ASK SPREADS**

The difference between the bid quote and the ask quote at any given time is known as the bid-ask spread. The bid-ask spread is the cost of instantaneously buying and selling the security. The higher the bid-ask spread, the higher a gain the security must produce in order to cover the spread along with other transaction costs. Most low-frequency price changes are large enough to make the bid-ask spread negligible in comparison. In tick data, on the other hand, incremental price changes can be comparable or smaller than the bid-ask spread.

Bid-ask spreads usually vary throughout the day. Figure 9.1 illustrates the average bid-ask spread cycles observed in the institutional EUR/USD market for the last two weeks of October 2008. As Figure 9.1 shows, the average spread increases significantly during Tokyo trading hours when the market is quiet. The spread then reaches its lowest levels during the overlap of the London and New York trading sessions when the market has many active buyers and sellers. The spike in the spread over the weekend of October 18–19, 2008, reflects the market concern over the subpoenas

![](_page_3_Figure_5.jpeg)

**FIGURE 9.1** Average hourly bid-ask spread on EUR/USD spot for the last two weeks of October 2008 on a median transaction size of USD 5 million.

![](_page_4_Figure_1.jpeg)

**FIGURE 9.2** Comparison of average bid-ask spreads for different hours of the day during normal market conditions and crisis conditions.

issued on October 17, 2009, to senior Lehman executives in a case relating to potential securities fraud at Lehman Brothers.

Bid-ask spreads typically increase during periods of market uncertainty or instability. Figure 9.2, for example, compares average bid-ask spreads on EUR/USD in the stable market conditions of July–August 2008 and the crisis conditions of September–October 2008. As Figure 9.2 shows, the intra-day spread pattern is persistent in both crisis and normal market conditions, but the spreads are significantly higher during crisis months than during normal conditions at all hours of the day. As Figure 9.2 also shows, the spread increase is not uniform at all hours of the day. The average hourly EUR/USD spreads increased by 0.0048% (0.48 basis points or pips) between the hours of 12 GMT and 16 GMT, when the London and New York trading sessions overlap. From 0 to 2 GMT, during the Tokyo trading hours, the spread increased by 0.0156 percent, over three times the average increase during the New York/London hours.

As a result of increasing bid-ask spreads during periods of uncertainty and crises, the profitability of high-frequency strategies decreases during those times. For example, high-frequency EUR/USD strategies running over Asian hours incurred significantly higher costs during September and October 2008 as compared with normal market conditions. A strategy that executed 100 trades during Asian hours alone resulted in 1.56 percent evaporating from daily profits due to the increased spreads, while the same strategy running during London and New York hours resulted in a smaller but still significant daily profit decrease of 0.48 percent. The situation can be even more severe for high-frequency strategies built for less liquid instruments. For example, bid-ask spreads for NZD/USD (not shown) on average increased thrice during September–October in comparison with market conditions of July–August 2008.

Future realizations of the bid-ask spread can be estimated using the model of Roll (1984), where the price of an asset at time *t*, *pt*, is assumed to equal an unobservable fundamental value, *mt*, offset by a value equal to half of the bid-ask spread, *s.* The price offset is positive when the next market order is a buy, and negative when the trade is a sell, as shown in equation (9.1):

$$p_t = m_t + \frac{s}{2}I_t \tag{9.1}$$

where

*It* = 1, market buy at ask −1, market sell at bid

If either a buy or a sell order can arrive next with equal probability, then *E*[*It*] = 0, and *E*[*pt*] = 0, absent changes in the fundamental asset value, *mt*. The covariance of subsequent price changes, however, is different from 0:

$$\operatorname{cov}\left[\Delta p_{t}, \, \Delta p_{t+1}\right] = E\left[\Delta p_{t} \Delta p_{t+1}\right] = -\frac{s^{2}}{4} \tag{9.2}$$

As a result, the future expected spread can be estimated as follows:

$$E[s] = 2\sqrt{-\text{cov}\left[\Delta p_t, \Delta p_{t+1}\right]} \text{ whenever } \text{cov}\left[\Delta p_t, \Delta p_{t+1}\right] < 0.$$

Numerous extensions of Roll's model have been developed to account for contemporary market conditions along with numerous other variables. Hasbrouck (2007) provides a good summary of the models.

#### **BID-ASK BOUNCE**

While tick data carries information about market dynamics, it is also distorted by the same processes that make the data so valuable in the first place. Dacorogna et al. (2001) report that sequential trade price bounces between the bid and ask quotes during market execution of orders introduce significant distortions into estimation of high-frequency parameters. Corsi, Zumbach, Muller, and Dacorogna (2001), for example, show that the ¨ bid-ask bounce introduces a considerable bias into volatility estimates. The authors calculate that the bid-ask bounce on average results in –40 percent negative first-order autocorrelation of tick data. Corsi et al. (2001) as well as Voev and Lunde (2007) propose to remedy the bias by filtering the data prior from the bid-ask noise prior to estimation.

#### **MODELING ARRIVALS OF TICK DATA**

Unlike low-frequency data, which is recorded at regular time periods, tick data arrives at irregularly spaced intervals. Several researchers have studied whether the time distance between subsequent quote arrivals itself carries information. Most researchers agree that inter-trade intervals indeed carry information on securities for which short sales are disallowed; the lower the inter-trade duration, the more likely the yet-to-be-observed good news and the higher the impending price change.

The process of information arrivals is modeled using so-called duration models. Duration models are used to estimate the factors affecting the duration between any two sequential ticks. Such models are known as quote processes and trade processes, respectively. Duration models are also used to measure the time elapsed between price changes of a prespecified size, as well as the time interval between predetermined trade volume increments. The models working with fixed price are known as price processes; the models estimating variation in duration of fixed volume increments are known as volume processes.

Durations are often modeled using Poisson processes. Poisson processes assume that sequential events, like quote arrivals, occur independently of one another. The number of arrivals between any two time points *t* and (*t* + τ ) is assumed to have a Poisson distribution.

In a Poisson process, λ arrivals occur per unit time. In other words, the arrivals occur at an average rate of (1/λ). The average arrival rate may be assumed to hold constant, or it may vary with time. If the average arrival rate is constant, the probability of observing exactly *k* arrivals between times *t* and (*t* + τ ) is

$$P[(N(t+\tau)-N(t))=k] = \frac{1}{k!}e^{-\lambda\tau}(\lambda\tau)^k, k=0,1,2,\dots$$
 (9.3)

Diamond and Verrecchia (1987) and Easley and O'Hara (1992) were the first to suggest that the duration between subsequent data arrivals carries information. The models posit that in the presence of short-sale constraints, inter-trade duration can indicate the presence of good news; in markets of securities where short selling is disallowed, the shorter the inter-trade duration, the higher is the likelihood of unobserved good news. The reverse also holds: in markets with limited short selling and normal liquidity levels, the longer the duration between subsequent trade arrivals, the higher the probability of yet-unobserved bad news. A complete absence of trades, however, indicates a lack of news.

Easley and O'Hara (1992) further point out that trades that are separated by a time interval have a much different information content than trades occurring in close proximity. One of the implications of Easley and O'Hara (1992) is that the entire price sequence conveys information and should be used in its entirety whenever possible, strengthening the argument for high-frequency trading.

Table 9.1 shows summary statistics for a duration measure computed on all trades recorded for S&P 500 Depository Receipts ETF (SPY) on May 13, 2009. As Table 9.1 shows, the average inter-trade duration was the longest outside of regular market hours, and the shortest during the hour preceding the market close (3–4 P.M. ET).

Variation in duration between subsequent trades may be due to several other causes. While the lack of trading may be due to a lack of new information, trading inactivity may also be due to low levels of liquidity, trading halts on exchanges, and strategic motivations of traders. Foucault, Kadan, and Kandel (2005) consider that patiently providing liquidity using limit orders may itself be a profitable trading strategy, as liquidity providers

|           | Number<br>of Trades | Inter-Trade Duration (milliseconds) |        |                 |                   |          |
|-----------|---------------------|-------------------------------------|--------|-----------------|-------------------|----------|
| Hour (ET) |                     | Average                             | Median | Std Dev         | Skewness Kurtosis |          |
| 4–5 AM    | 170                 | 19074.58                            | 5998   | 47985.39        | 8.430986          | 91.11571 |
| 5–6 AM    | 306                 | 11556.95                            | 4781.5 | 18567.83        | 3.687372          | 21.92054 |
| 6–7 AM    | 288                 | 12606.81                            | 4251   | 20524.15        | 3.208992          | 16.64422 |
| 7–8 AM    | 514                 | 7096.512                            | 2995   | 11706.72        | 4.288352          | 29.86546 |
| 8–9 AM    | 767                 | 4690.699                            | 1997   |                 | 7110.478 3.775796 | 23.56566 |
| 9–10 AM   | 1089                | 2113.328                            | 1934   | 24702.9         | 3.5185            | 24.6587  |
| 10–11 AM  | 1421                | 2531.204                            | 1373   |                 | 3409.889 3.959082 | 28.53834 |
| 11–12 PM  | 1145                | 3148.547                            | 1526   |                 | 4323.262 3.240606 | 17.24866 |
| 12–1 PM   | 749                 | 4798.666                            | 1882   |                 | 7272.774 2.961139 | 13.63373 |
| 1–2 PM    | 982                 | 3668.247                            | 1739.5 |                 | 5032.795 2.879833 | 13.82796 |
| 2–3 PM    | 1056                | 3408.969                            | 1556   |                 | 4867.061 3.691909 | 23.90667 |
| 3–4 PM    | 1721                | 2094.206                            | 1004   | 2684.231 2.9568 |                   | 15.03321 |
| 4–5 PM    | 423                 | 8473.593                            | 1500   | 24718.41        | 7.264483          | 69.82157 |
| 5–6 PM    | 47                  | 73579.23                            | 30763  | 113747.8        | 2.281743          | 7.870699 |
| 6–7 PM    | 3                   | 1077663                             | 19241  | 1849464         | 0.707025          | 1.5      |

**TABLE 9.1** Hourly Distributions of Inter-Trade Duration Observed on May 13, 2009 for S&P 500 Depository Receipts ETF (SPY)

should be compensated for their waiting. The compensation usually comes in the form of a bid-ask spread and is a function of the waiting time until the order limit is "hit" by liquidity takers; lower inter-trade durations induce lower spreads. However, Dufour and Engle (2000) and Saar and Hasbrouck (2002) find that spreads are actually higher when traders observe short durations, contrasting the time-based limit order compensation hypothesis.

In addition to durations between subsequent trades and quotes, researchers have also been modeling durations between fixed changes in security prices and volumes. The time interval between subsequent price changes of a specified magnitude is known as price duration. Price duration has been shown to decrease with increases in volatility. Similarly, the time interval between subsequent volume changes of a prespecified size is known as the volume duration. Volume duration has been shown to decrease with increases in liquidity.

The information content of quote, trade, price, and volume durations introduces biases into the estimation process, however. If the available information determines the time between subsequent trades, time itself ceases to be an independent variable, introducing substantial endogeneity bias into estimation. As a result, traditional estimates of variance of transaction prices are too high in comparison with the true variance of the price series. The variance of the high-frequency data, however, can be consistently estimated using the generalized autoregressive conditional heteroscedasticity (GARCH) process framework that can incorporate inter-trade and inter-quote duration.

## APPLYING TRADITIONAL ECONOMETRIC TECHNIQUES TO TICK DATA

Most modern computational techniques have been developed to work with regularly spaced data, presented in monthly, weekly, daily, hourly, or other consistent intervals. The traditional reliance of researchers on fixed time intervals is due to

- Relative availability of daily data (newspapers have published daily quotes since the  $1920s$ )
- Relative ease of processing regularly spaced data
- An outdated view that "whatever drove security prices and returns, it probably did not vary significantly over short time intervals." (Goodhart and O'Hara 1997, pp. 80–81)

The major difference between tick data and traditional, regularly spaced data is that tick-by-tick observations are separated by varying time

![](_page_9_Figure_1.jpeg)

**FIGURE 9.3** Data-sampling methodologies.

intervals. One way to overcome the irregularities in the data is to sample it at certain predetermined periods of time—for example, every hour or minute.

Traditional financial literature samples closing prices. For example, if the data is to be converted from tick data to minute "bars," then under the traditional approach, the bid or ask price for any given minute would be determined as the last quote that arrived during that particular minute. If no quotes arrived during a certain minute, then the previous minute's closing prices would be taken as the current minute's closing prices, and so on. Figure 9.3, panel (a) illustrates this idea. This approach implicitly assumes that in the absence of new quotes, the prices stay constant, which does not have to be the case.

Dacorogna et al. (2001) propose a potentially more precise way to sample quotes—linear time-weighted interpolation between adjacent quotes. At the core of the interpolation technique is an assumption that at any given time, unobserved quotes lie on a straight line that connects two neighboring observed quotes. Figure 9.3, panel (b) illustrates linear interpolation sampling.

As shown in Figure 9.3 panels (a) and (b), the two quote-sampling methods produce quite different results. Dacorogna et al. (2001) do not provide or reference any studies that compare the performances of the two sampling methods.

Mathematically, the two sampling methods can be expressed as follows:

Quote sampling using closing prices: 
$$\hat{q}_t = q_{t, last}$$
 (9.4)

Quote sampling using linear interpolation:

$$\hat{q}_t = q_{t,last} + (q_{t,next} - q_{t,last}) \frac{t - t_{last}}{t_{next} - t_{last}} \tag{9.5}$$

where ˆ*qt* is the resulting sampled quote, *t* is the desired sampling time (start of a new minute, for example), *tlast* is the timestamp of the last observed quote prior to the sampling time *t*, *qt*,*last* is the value of the last quote prior to the sampling time *t*, *tnext* is the timestamp of the first observed quote after the sampling time *t*, and *qt*,*next* is the value of the first quote after the sampling time *t*.

Another way to assess the variability of the tick data is through modeling the high-frequency distributions using the mixtures of distributions model (MODM). Tauchen and Pitts (1983), for example, show that if changes in the market prices are normally distributed, then aggregates of price changes and volume of trades approximately form a jointly normal distribution.

## **CONCLUSION**

Tick data differs dramatically from low-frequency data. Utilization of tick data creates a host of opportunities not available at lower frequencies.
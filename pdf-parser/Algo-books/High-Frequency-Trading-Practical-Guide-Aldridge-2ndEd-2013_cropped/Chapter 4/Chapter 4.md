# **CHAPTER 4** High-Frequency Data

Trade and quote information is often distributed in Level I or Level II formats. Level I quotes include the best bid price, best ask price, best bid size, best ask size, and last trade price and size, where available. Level II quotes include all changes to the order book, including new limit order arrivals and cancellations at prices away from the market price. This chapter describes the details of data quotations and sampling methodologies and contrasts the data with their low-frequency counterparts.

#### What Is High-Frequency Data?

High-frequency data, also known as *tick data*, are records of live market activity. Every time a customer, a dealer, or another entity posts a so-called limit order to buy  $s$  units of a specific security with ticker  $X$  at price  $q$ , a bid quogte  $\stackrel{\mathbf{b}}{\Leftarrow}$  is logged at time  $t_{\scriptscriptstyle b}$  to buy  $\stackrel{\mathbf{b}}{\Leftarrow}$  units of X. Market orders are incorporated into tick data in a different way, as discussed in this chapter.

When the newly arrived bid quote  $\stackrel{\bullet}{\ll}$  has the highest price relative to all other previously arrived bid quotes in force, de becomes known as "the best bid" available at time  $t_{\rm b}$ . Similarly, when a trading entity posts a limit order to sell *s* units of X at price *q*, an ask quote  $\stackrel{d}{\ll}$  is logged at time *t* to sell  $\stackrel{e}{\ll}$ units of X. If the latest  $\stackrel{\scriptscriptstyle\bullet}{\phantom{}_{\bullet}}$  is lower than all other available ask quotes for security X,  $\stackrel{d}{\leq}$  becomes known as "the best ask" at time  $t$ .

What happens to quotes from the moment they arrive largely depends on the venue where the orders are posted. Best bids and asks posted directly on an exchange will be broadcast to all exchange participants and other parties tracking quote data. In situations when the new best bid exceeds the best ask already in force on the exchange,  $\stackrel{a}{\ll} \geq \stackrel{a}{\ll}$ , most exchanges will immediately "match" such quotes, executing a trade at the preexisting best ask,  $\stackrel{a}{\ll}$  at time  $t_{\rm b}$ . Conversely, should the newly arrived best ask fall below

the current best bid,  $\stackrel{a}{\ll} \leq \stackrel{b}{\ll}$ , the trade is executed at the preexisting best bid,  $\frac{1}{\mathbf{c}}$  at time  $t_{\mathbf{a}}$ .

Most dark pools match bids and asks by "crossing the spread," but may not broadcast the newly arrived quotes (hence the mysterious moniker, the "dark pools"). Similarly, quotes destined for the interdealer networks may or may not be disseminated to other market participants, depending on the venue.

Market orders contribute to high-frequency data in the form of "last trade" information. Unlike a limit order that is an order to buy a specified quantity of a security at a certain price, a market order is an order to buy a specified quantity of a security at the best price available at the moment the order is "posted" on the trading venue. As such, market orders are executed immediately at the best available bid or best ask prices, with each market buy order executed at the best ask and each market sell matched with the best bid, and the transaction is recorded in the quote data as the "last trade" price" and the "last trade size."

A large market order may need to be matched with one or several best quotes, generating several "last trade" data points. For example, if the newly arrived market buy order is smaller in size than that of the best ask, the best ask quote may still remain in force on most trading venues, but the best ask size will be reduced to reflect that the portion of the best ask quote has been matched with the market order. When the size of the incoming market buy order is bigger than the size of the corresponding best ask, the market order consumes the best ask in its entirety, and then proceeds to be matched sequentially with the next available best ask until the size of the market order is fulfilled. The remaining lowest-priced ask quote becomes the best ask available on the trading venue.

Most limit and market orders are placed in so-called "lot sizes": increments of certain number of units, known as a lot. In foreign exchange, a standard trading lot today is US\$5 million, a considerable reduction from a minimum of \$25 million entertained by high-profile brokers just a few years ago. On equity exchanges, a lot can be as low as one share, but dark pools may still enforce a 100 share minimum requirement for orders. An order for the amount other than an integer increment of a lot size, is called "an odd lot."

Small limit and market "odd lot" orders posted through a broker-dealer may be aggregated, or "packaged," by the broker-dealer into larger-size orders in order to obtain volume discounts at the orders' execution venue. In the process, the brokers may "sit" on quotes without transmitting them to an executing venue, delaying execution of customers' orders.

# How Is High-Frequency Data Recorded?

The highest-frequency data are a collection of sequential "ticks," arrivals of the latest quote, trade, price, order size, and volume information. Tick data usually has the following properties:

- A timestamp
- A financial security identification code
- An indicator of what information it carries:
  - Bid price
  - Ask price
  - Available bid size
  - Available ask size
  - Last trade price
  - Last trade size
- Security-specific data, such as implied volatility for options
- The market value information, such as the actual numerical value of the price, available volume, or size

A timestamp records the date and time at which the quote originated. It may be the time at which the exchange or the broker-dealer released the quote, or the time when the trading system has received the quote. At the time this article is written, the standard "round-trip" travel time of an order quote from the ordering customer to the exchange and back to the customer with the acknowledgment of order receipt is 15 milliseconds or less in New York. Brokers have been known to be fired by their customers if they are unable to process orders at this now standard speed. Sophisticated quotation systems, therefore, include milliseconds and even microseconds as part of their timestamps.

Another part of the quote is an identifier of the financial security. In equities, the identification code can be a ticker, or, for tickers simultaneously traded on multiple exchanges, a ticker followed by the exchange symbol. For futures, the identification code can consist of the underlying security, futures expiration date, and exchange code.

The last trade price shows the price at which the last trade in the security cleared. Last trade price can differ from the bid and ask. The differences can arise when a customer posts a favorable limit order that is immediately matched by the broker without broadcasting the customer's quote. Last trade size shows the actual size of the last executed trade.

The best bid is the highest price available for sale of the security in the market. The best ask is the lowest price entered to buy the security at any particular time. In addition to the best bid and best ask, quotation systems may disseminate "market depth" information: the bid and ask quotes entered posted on the trading venue at prices worse than the best bid and ask, as well as aggregate order sizes corresponding to each bid and ask recorded on the trading venue's "books." Market depth information is sometimes referred to as the Level II data and may be disseminated as the premium subscription service only. In contrast, the best bid, best ask, last trade price, and size information ("Level I data") is often available for a small nominal fee.

Panels A and B of Figure 4.1 illustrate a 30-second log of Level I highfrequency data recorded by New York Stock Exchange (NYSE) Arca for Standard & Poor's Depositary Receipts (SPDR) S&P 500 exchange-traded fund (ETF; ticker SPY) from 14:00:16:400 to 14:02:00:000 GMT on November 9, 2009. Panel A shows quote data: best bid, best ask and last trade information, while panel B displays corresponding position sizes (best bid size, best ask size, and last trade size).

#### **Figure 4.1** Level I High-Frequency Data Recorded by NYSE Arca for SPY from 14:00:16:400 to 14:02:00:000 GMT on November 9, 2009. Data source: Bloomberg

![](_page_4_Figure_2.jpeg)

![](_page_4_Figure_4.jpeg)

#### Properties of High-Frequency Data

High-frequency securities data have been studied for many years. Yet they are still something of a novelty to many academics and practitioners. Unlike daily or monthly data sets commonly used in much of financial research and related applications, high-frequency data have distinct properties, which simultaneously can be advantageous and intimidating to researchers. Table 4.1 summarizes the properties of high-frequency data. Each property

and its advantages and disadvantages are discussed in detail later in the article.

| Property of HF Data                                             | Description                                                                                                                                                                             | Pros                                                                                                                                                 | Cons                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Voluminous                                                      | Each day of high-<br>frequency data<br>contains the number of<br>observations equivalent to<br>30 years of daily data.                                                                  | Large numbers of<br>observations carry lots of<br>information.                                                                                       | High-frequency data are<br>difficult to handle manually.                                                                                                                                                                                                                                               |
| Subject to bid-ask<br>bounce                                    | Unlike traditional data<br>based on just closing<br>prices, tick data carry<br>additional supply-and-<br>demand information in the<br>form of bid and ask prices<br>and offering sizes. | Bid and ask quotes can<br>carry valuable information<br>about impending<br>market moves, which<br>can be harnessed to the<br>researcher's advantage, | Bid and ask quotes are<br>separated by a spread.<br>Continuous movement<br>from bid to ask and back<br>introduces a jump process,<br>difficult to deal with through<br>many conventional models.                                                                                                       |
| Not normally<br>or lognormally<br>distributed                   | Returns computed from<br>tick are not normal or<br>lognormal.                                                                                                                           | Many tradable models are<br>still to be discovered.                                                                                                  | Traditional asset pricing<br>models assuming<br>lognormality of prices do<br>not apply.                                                                                                                                                                                                                |
| in time                                                         | Irregularly spaced Arrivals of tick data are<br>asynchronous,                                                                                                                           | Durations between data<br>arrival carry information.                                                                                                 | Most traditional models<br>require regularly spaced<br>data; need to convert high-<br>frequency data to some<br>regular intervals, or "bars"<br>of data. Converted data are<br>often sparse (populated<br>with zero returns), once<br>again making traditional<br>econometric inferences<br>difficult. |
| Do not include<br>buy or sell<br>trade direction<br>information | Level I and Level II data do<br>not include information<br>on whether the trade was<br>a result of a market buy or<br>a market sell order                                               | Data are leaner without<br>trade direction information;<br>trade information is more<br>difficult for bystanders to<br>extract.                      | The information on whether<br>a trade is buyer initiated or<br>seller initiated is a desired<br>input in many models.                                                                                                                                                                                  |

**Table 4.1** Summary of Properties of High-Frequency Data

#### High-Frequency Data Are Voluminous

The nearly two-minute sample of tick data for SPY shown in Figure 4.1 contained over 2,000 observations of Level I data: best bid quotes and sizes, best ask quotes and sizes, and last trade prices and sizes. Table 4.2 summarizes the breakdown of the data points provided by NYSE Arca for SPY from 14:00:16:400 to 14:02:00:000 GMT on November 9, 2009, and

SPY, Japanese yen futures, and a euro call option throughout the day on November 9, 2009. Other Level I data omitted from [Table 4.2](#page-6-0) include cumulative daily trade volume for SPY and Japanese yen futures, and "greeks" for the euro call option. The number of quotes observed on November 9, 2009, for SPY alone would comprise over 160 years of daily open, high, low, close, and volume data points, assuming an average of 252 trading days per year.

|                  | SPY, 14:00:16:400 to |              | USD/ JPY Dec. 2009 | EUR/USD Call Expiring Dec. 2009      |  |
|------------------|----------------------|--------------|--------------------|--------------------------------------|--|
| Quote Type       | 14:02:00:000 GMT     | SPY, All Day | Futures, All Day   | with Strike Price of 1.5100, All Day |  |
| Best bid quote   | $4(3\%)$             | 5,467 (3%)   | 6,320 (5%)         | 1,521 (3%)                           |  |
| Best bid size    | 36 (29%)             | 38,948 (19%) | 39,070 (32%)       | 5,722 (11%)                          |  |
| Best ask quote   | $4(3\%)$             | 4,998 (2%)   | 6,344 (5%)         | 1,515 (3%)                           |  |
| Best ask size    | 35 (28%)             | 38,721 (19%) | 38,855 (32%)       | 5,615 (11%)                          |  |
| Last trade price | 6 (5%)               | 9,803 (5%)   | 3,353 (3%)         | 14 (0%)                              |  |
| Last trade size  | 20 (16%)             | 27,750 (14%) | 10,178 (8%)        | 25 (0%)                              |  |
| Total            | 125                  | 203,792      | 123,216            | 49,982                               |  |

<span id="page-6-0"></span>**Table 4.2** Summary Statistics for Level I Quotes for Selected Securities on November 9, 2009

The quality of data does not always match its quantity. Centralized exchanges generally provide accurate data on bids, asks, and size. U.S. equity exchanges are required by law to archive and maintain reliable records of every tick of data, as well as to submit best quotes within one minute of their occurrence to the U.S. centralized ticker tape known as the *Securities Information Processor* (SIP). The information on the limit order book beyond the best bid and best offer is known as Level II data and can be obtained via special subscription.

In decentralized markets, such as foreign exchange and the interbank money market, no market-wide quotes are available at any given time. In such markets, participants are aware of the current price levels, but each institution quotes its own prices adjusted for its order book. In decentralized markets, each dealer provides his own tick data to his clients. As a result, a specific quote on a given financial instrument at any given time may vary from dealer to dealer. Reuters, Telerate, and Knight Ridder, among others, collect quotes from different dealers and disseminate them back, improving the efficiency of the decentralized markets.

There are generally thought to be three anomalies in interdealer quote discrepancies. First, each dealer's quotes reflect that dealer's own inventory.

For example, a dealer that has just sold a customer \$100 million of USD/CAD would be eager to diversify the risk of his position and avoid selling any more of USD/CAD. Most dealers, however, are obligated to transact with their clients on tradable quotes. To incite his clients to place sell orders on USD/CAD, the dealer temporarily raises the bid quote on USD/CAD. At the same time, to encourage his clients to withhold placing buy orders, the dealer raises the ask quote on USD/CAD. Thus, dealers tend to raise both bid and ask prices whenever they are short in a particular financial instrument and lower both bid and ask prices whenever they are disproportionately long in a financial instrument.

Second, in an anonymous marketplace, such as a dark pool, dealers as well as other market makers may "fish" for market information by sending indicative quotes that are much off the previously quoted price to assess the available demand or supply.

Third, Dacorogna et al. (2001) note that some dealers' quotes may lag real market prices. The lag is thought to vary from milliseconds to a minute. Some dealers quote moving averages of quotes of other dealers. The dealers who provide delayed quotes usually do so to advertise their market presence in the data feed. This was particularly true when most order prices were negotiated over the telephone, allowing a considerable delay between quotes and orders. Fast-paced electronic markets discourage lagged quotes, improving the quality of markets.

## High-Frequency Data Are Subject to the Bid-Ask Bounce

In addition to trade price and volume data long available in low-frequency formats, high-frequency data comprise bid and ask quotes and their associated order sizes. Bid and ask data arrive asynchronously and introduce noise in the quote process.

The difference between the bid quote and the ask quote at any given time is known as the bid-ask spread. The bid-ask spread is the cost of instantaneously buying and selling the security. The higher the bid-ask spread, the higher the gain the security must produce in order to cover the

spread along with other transaction costs. Most low-frequency price changes are large enough to make the bid-ask spread negligible in comparison. In tick data, however, incremental price changes can be comparable or smaller than the bid-ask spread.

<span id="page-8-1"></span>Bid-ask spreads usually vary throughout the day. [Figure 4.2](#page-8-0) illustrates the average bid-ask spread cycles observed in the institutional EUR/USD market for the last two weeks of October 2008. As [Figure 4.2](#page-8-0) shows, the average spread increases significantly during Tokyo trading hours, when the market is quiet. The spread then reaches its lowest levels during the overlap of the London and New York trading sessions, when the market has many active buyers and sellers. The spike in the spread over the weekend of October 18–19, 2008, reflects the market concern over the subpoenas issued on October 17, 2009, to senior Lehman executives in a case relating to potential securities fraud at Lehman Brothers.

<span id="page-8-0"></span>**[Figure 4.2](#page-8-1)** Average Hourly Bid-Ask Spread on EUR/USD Spot for the Last Two Weeks of October 2008 on a Median Transaction Size of US\$5 Million

![](_page_8_Figure_3.jpeg)

Bid-ask spreads typically increase during periods of market uncertainty or instability. Figure 4.3, for example, compares average bid-ask spreads on EUR/USD in the stable market conditions of July–August 2008 and the crisis conditions of September–October 2008. As the figure shows, the

intraday spread pattern is persistent in both crisis and normal market conditions, but the spreads are significantly higher during crisis months than during normal conditions at all hours of the day. As [Figure 4.3](#page-9-0) also shows, the spread increase is not uniform at all hours of the day. The average hourly EUR/USD spreads increased by 0.0048 percent (0.48 basis points or pips) between the hours of 12 GMT and 16 GMT, when the London and New York trading sessions overlap. From 0 to 2 GMT, during the Tokyo trading hours, the spread increased by 0.0156 percent, over three times the average increase during the New York/London hours.

<span id="page-9-0"></span>**Figure 4.3** Comparison of Average Bid-Ask Spreads for Different Hours of the Day during Normal Market Conditions and Crisis Conditions

![](_page_9_Figure_2.jpeg)

As a result of increasing bid-ask spreads during periods of uncertainty and crises, the profitability of high-frequency strategies decreases during those times. For example, high-frequency EUR/USD strategies running over Asian hours incurred significantly higher costs during September and October 2008 as compared with normal market conditions. A strategy that executed 100 trades during Asian hours alone resulted in 1.56 percent evaporating from daily profits due to the increased spreads, while the same

strategy running during London and New York hours resulted in a smaller but still significant daily profit decrease of 0.48 percent. The situation can be even more severe for high-frequency strategies built for less liquid instruments. For example, bid-ask spreads for NZD/USD (not shown) on average increased three times during September–October in comparison with market conditions of July–August 2008.

While tick data carry information about market dynamics, it is also distorted by the same processes that make the data so valuable in the first place. Dacorogna et al. (2001) report that sequential trade price bounces between the bid and ask quotes during market execution of orders introduce significant distortions into estimation of high-frequency parameters. Corsi, Zumbach, Muller, and Dacorogna (2001), for example, show that the bidask bounce introduces a considerable bias into volatility estimates. The authors calculate that the bid-ask bounce on average results in  $-40$  percent first-order autocorrelation of tick data. Corsi et al. (2001) as well as Voev and Lunde (2007) propose to remedy the bias by filtering the data from the bid-ask noise prior to estimation.

In addition to real-time adjustments to bid-ask data, researchers deploy forecasting techniques to estimate the impending bid-ask spread and adjust for it in models ahead of time. Future realizations of the bid-ask spread can be estimated using the model suggested by Roll (1984), where the price of an asset at time  $t$ ,  $p$ , is assumed to equal an unobservable fundamental value,  $m$ , offset by a value equal to half of the bid-ask spread, s. The price offset is positive when the next market order is a buy, and negative when the trade is a sell, as shown in equation (3):

$$p_t = m_t + \frac{s}{2}I_t$$
(3) where  $I_t = \begin{cases} 1, & \text{market buy at ask} \\ -1, & \text{market sell at bid} \end{cases}$ 

If either a buy or a sell order can arrive next with equal probability, then  $E[I] = 0$ , and  $E[\Delta p] = 0$ , absent changes in the fundamental asset value, *m*. The covariance of subsequent price changes, however, is different from 0:

$$(4) \stackrel{\text{cov}}{=} \left[\Delta p_t, \Delta p_{t+1}\right] = E\left[\Delta p_t \Delta p_{t+1}\right] = -\frac{s^2}{4}$$

As a result, the future expected spread can be estimated as follows:

 $E[s] = 2\sqrt{-\cos[\Delta p_t, \Delta p_{t+1}]}$  whenever  $\cos[\Delta p_t, \Delta p_{t+1}] < 0$ 

Numerous extensions of Roll's model have been developed to account for contemporary market conditions along with numerous other variables. Hasbrouck (2007) provides a good summary of the models.

To use standard econometric techniques in the presence of the bid-ask bounce, many practitioners convert the tick data to "midquote" format: the simple average of the latest bid and ask quotes. The midquote is used to approximate the price level at which the market is theoretically willing to trade if buyers and sellers agreed to meet each other halfway on the price spectrum. Mathematically, the midquote can be expressed as follows:

(5) 
$$\hat{q}_{t_m}^m = \frac{1}{2} \Big( q_{t_a}^a + q_{t_b}^b \Big) \text{ where } t_m = \begin{cases} t_a, \text{if } t_a \ge t_b \\ t_b, \text{ otherwise} \end{cases}$$

The latter condition for  $t_m$  reflects the continuous updating of the midquote estimate:  $\mathbb{Q}$  is updated whenever the latest best bid,  $\mathbb{Q}$ , or best ask quote,  $\overrightarrow{\mathbf{q}}$ , arrives, at  $t_{\rm b}$  or  $t_{\rm a}$  respectively.

Another way to sample tick quotes into a cohesive data series is by weighing the latest best bid and best ask quotes by their accompanying order sizes:

$$\tilde{q}_{t}^{s} = \frac{q_{t_{b}}^{b}s_{t_{a}}^{a} + q_{t_{a}}^{a}s_{t_{b}}^{b}}{s_{t_{a}}^{a} + s_{t_{b}}^{b}}$$

where  $\stackrel{\mathbf{b}}{\Leftarrow}$  and  $\stackrel{\mathbf{b}}{\Leftarrow}$  is the best bid quote and the best bid available size recorded at time  $t_{\rm b}$  (when  $\frac{b}{\rm b}$  became the best bid), and  $\frac{a}{\rm b}$  and  $\frac{a}{\rm b}$  is the best bid quote and the best bid available size recorded at time  $t$ .

#### High-Frequency Data Are Not Normal or Lognormal

Many classical models assume lognormality of prices, allowing price diffusion models to work seamlessly, and resulting in several pricing models, such as Black-Scholes, to be considered fair approximations of market evolutions of related financial instruments. A necessary condition for lognormality of prices is the normal distribution of sequential price

changes. As this section shows, however, sequential changes in most of the tick data, like midquotes and size-weighted quotes and trades, do not follow normal distribution, yet distribution of sequential trade ticks is close to that of normal. Trade tick data are, therefore, the best choice for modelers assuming lognormal prices.

<span id="page-12-1"></span>[Figure 4.4](#page-12-0) compares the histograms of simple returns computed from midquote (panel A), size-weighted midquote (panel B) and trade-price (panel C) processes for SPDR S&P 500 ETF data recorded as they arrive throughout November 9, 2009. The data neglect the time difference between the adjacent quotes, treating each sequential quote as an independent observation. Figure 4.5 contrasts the quantile distribution plots of the same data sets with the quantiles of a standard normal distribution.

<span id="page-12-0"></span>**[Figure 4.4](#page-12-1)** Histograms of Simple Returns Computed from Midquote (Panel A), Size-Weighted Midquote (Panel B) and Trade Price (Panel C) Processes for SPY Data Recorded as They Arrive throughout November 9, 2009

Panel A: Midquote simple returns

Panel B: Size-weighted midquote simple returns

Panel C: Last trade price simple returns

![](_page_13_Figure_0.jpeg)

As Figures 4.4 and [4.5](#page-13-0) show, the basic midquote distribution is constrained by the minimum "step size": the minimum changes in the midquote can occur at half-tick increments (at present, the minimum tick size is \$0.01 in equities). The size-weighted midquote forms the most continuous distribution among the three distributions discussed. [Figure 4.5](#page-13-0) confirms this notion further and also illustrates the fat tails present in all three types of data distributions.

<span id="page-13-0"></span>**Figure 4.5** Quantile Plots of Simple Returns of Midquote (Panel A), Size-Weighted Midquote (Panel B) and Trade-Price (Panel C) Processes for SPY Data Recorded as They Arrive throughout November 9, 2009

Panel A: Midquote returns

Panel B: Size-weighted midquote returns

Panel C: Trade price returns

![](_page_15_Figure_0.jpeg)

![](_page_16_Figure_0.jpeg)

![](_page_17_Figure_0.jpeg)

![](_page_18_Figure_0.jpeg)

As clearly shown in Figure 4.5, of the three methodologies, tick-by-tick trade returns most closely fit the normal distribution, when heavy tails past four standard deviations are ignored. Midquote values and size-weighted midquotes alike begin to deviate from normality at just two standard deviations, while trade returns follow the normal up to four standard deviations.

## High-Frequency Data Are Irregularly Spaced in Time

Most modern computational techniques have been developed to work with regularly spaced data, presented in monthly, weekly, daily, hourly, or other consistent intervals. The traditional reliance of researchers on fixed time intervals is due to:

- Relative availability of daily data (newspapers have published daily quotes since the 1920s).
- Relative ease of processing regularly spaced data.
- An outdated view that "whatever drove security prices and returns, it probably did not vary significantly over short time intervals." (Goodhart and O'Hara 1997, pp. 80–81)

By contrast, high-frequency observations are separated by varying time intervals. One way to overcome the irregularities in the data are to sample it

at certain predetermined periods of time—for example, every hour or minute. For example, if the data are to be converted from tick data to minute "bars," then under the traditional approach, the bid or ask price for any given minute would be determined as the last quote that arrived during that particular minute. If no quotes arrived during a certain minute, then the previous minute's closing prices would be taken as the current minute's closing prices, and so on. [Figure 4.7](#page-19-0), panel A illustrates this idea. This approach implicitly assumes that in the absence of new quotes, the prices stay constant, which does not have to be the case.

<span id="page-19-0"></span>**[Figure 4.7](#page-19-1)** Midquote "Closing Quotes" Sampled at 200-ms (top) and 15-s Intervals

<span id="page-19-1"></span>![](_page_19_Figure_2.jpeg)

Dacorogna et al. (2001) propose a potentially more precise way to sample quotes: linear time-weighted interpolation between adjacent quotes. At the core of the interpolation technique is an assumption that at any given time, unobserved quotes lie on a straight line that connects two neighboring observed quotes. Figure 4.6, panel B illustrates linear interpolation sampling.

As shown in Figure 4.6, panels A and B, the two quote-sampling methods produce quite different results.

Mathematically, the two sampling methods can be expressed as follows: Quote sampling using closing prices:

$$(7) \; \hat{q}_t = q_{t,\text{last}}$$

Quote sampling using linear interpolation:

$$(8) \stackrel{\hat{q}_t = q_{t,last} + (q_{t,next} - q_{t,last})}{=} \frac{t - t_{last}}{t_{next} - t_{last}}$$

where is the resulting sampled quote, *t* is the desired sampling time (start of a new minute, for example), *t* last is the timestamp of the last observed quote prior to the sampling time *t*, *q*t,last is the value of the last quote prior to the sampling time *t*, *t* next is the timestamp of the first observed quote after the sampling time *t*, and *q*t,next is the value of the first quote after the sampling time *t*.

Figures 4.7 and 4.8 compare histograms of the midquote data sampled as closing prices and interpolated, at frequencies of 200 ms and 15 s. Figure 4.9 compares quantile plots of closing prices and interpolated distributions. As Figures 4.7 and 4.8 show, oft-sampled distributions are sparse, that is, contain more zero returns than distributions sampled at lower frequencies. At the same time, returns computed from interpolated quotes are more continuous than closing prices, as Figure 4.9 illustrates.

**Figure 4.8** Midquote "Time-Interpolated Quotes" Sampled at 200-ms (top) and 15-s Intervals

![](_page_21_Figure_1.jpeg)

![](_page_22_Figure_0.jpeg)

**Figure 4.9** Quantile Plots: Closing Prices versus Interpolated Midquotes Sampled at 200 ms

Instead of manipulating the interquote intervals into the convenient regularly spaced formats, several researchers have studied whether the time distance between subsequent quote arrivals itself carries information. For example, most researchers agree that intertrade intervals indeed carry information on securities for which short sales are disallowed; the lower the intertrade duration, the more likely the yet-to-be-observed good news and the higher the impending price change.

Duration models are used to estimate the factors affecting the time between any two sequential ticks. Such models are known as quote processes and trade processes, respectively. Duration models are also used

to measure the time elapsed between price changes of a prespecified size, as well as the time interval between predetermined trade volume increments. The models working with fixed price are known as *price processes;* the models estimating variation in duration of fixed volume increments are known as *volume processes.*

Durations are often modeled using Poisson processes that assume that sequential events, like quote arrivals, occur independently of one another. The number of arrivals between any two time points *t* and (*t* + ) is assumed to have a Poisson distribution. In a Poisson process, arrivals occur per unit time. In other words, the arrivals occur at an average rate of (1/ ). The average arrival rate may be assumed to hold constant, or it may vary with time. If the average arrival rate is constant, the probability of observing exactly K arrivals between times *t* and (*t* + ) is

(9) 
$$P[(N(t+\tau)-N(t))=k] = \frac{1}{k!}e^{-\lambda\tau}(\lambda\tau)^k, \quad k=0,1,2,...$$

Diamond and Verrecchia (1987) and Easley and O'Hara (1992) were the first to suggest that the duration between subsequent ticks carries information. Their models posit that in the presence of short-sale constraints, intertrade duration can indicate the presence of good news; in markets of securities where short selling is disallowed, the shorter the intertrade duration, the higher the likelihood of unobserved good news. The reverse also holds: in markets with limited short selling and normal liquidity levels, the longer the duration between subsequent trade arrivals, the higher the probability of yet-unobserved bad news. A complete absence of trades, however, indicates a lack of news.

Easley and O'Hara (1992) further point out that trades that are separated by a time interval have a much different information content than trades occurring in close proximity. One of the implications of Easley and O'Hara (1992) is that the entire price sequence conveys information and should be used in its entirety whenever possible, strengthening the argument for highfrequency trading.

Table 4.3 shows summary statistics for a duration measure computed on all trades recorded for SPY on May 13, 2009. As Table 4.3 illustrates, the average intertrade duration was the longest outside of regular market hours,

and the shortest during the hour preceding the market close (3:00 to 4:00 p.m. ET).

|                            |               | --------------------------------------- |         |           |          |          |
|----------------------------|---------------|-----------------------------------------|---------|-----------|----------|----------|
| Hour (ET)                  | No. of Irades | Average                                 | Median  | Std. Dev. | Skewness | Kurtosis |
| $4:00-5:00 \text{ a.m.}$   | 170           | 19,074.58                               | 5,998   | 47,985.39 | 8.430986 | 91.11571 |
| $5:00-6:00 \text{ a.m.}$   | 306           | 11,556.95                               | 4,781.5 | 18,567.83 | 3.687372 | 21.92054 |
| $6:00-7:00 \text{ a.m.}$   | 288           | 12,606.81                               | 4,251   | 20,524.15 | 3,208992 | 16,64422 |
| $7:00-8:00 \text{ a.m.}$   | 514           | 7,096.512                               | 2,995   | 11,706.72 | 4.288352 | 29.86546 |
| $8:00-9:00 \text{ a.m.}$   | 767           | 4,690,699                               | 1,997   | 7,110,478 | 3.775796 | 23.56566 |
| $9:00-10:00 \text{ a.m.}$  | 1,089         | 2,113,328                               | 1,934   | 24,702.9  | 3.5185   | 24,6587  |
| $10:00-11:00 \text{ a.m.}$ | 1,421         | 2,531,204                               | 1,373   | 3,409.889 | 3,959082 | 28.53834 |
| 11:00-12:00 p.m.           | 1,145         | 3,148.547                               | 1,526   | 4,323,262 | 3.240606 | 17.24866 |
| $12:00-1:00 \text{ p.m.}$  | 749           | 4,798,666                               | 1,882   | 7,272,774 | 2.961139 | 13.63373 |
| $1:00-2:00 \text{ p.m.}$   | 982           | 3,668,247                               | 1,739.5 | 5,032,795 | 2.879833 | 13.82796 |
| $2:00-3:00 \text{ p.m.}$   | 1,056         | 3,408.969                               | 1,556   | 4,867.061 | 3.691909 | 23.90667 |
| 3:00-4:00 p.m.             | 1,721         | 2,094,206                               | 1,004   | 2,684,231 | 2.9568   | 15,03321 |
| 4:00-5:00 p.m.             | 423           | 8,473,593                               | 1,500   | 24,718.41 | 7,264483 | 69,82157 |
| $5:00-6:00 \text{ p.m.}$   | 47            | 73,579.23                               | 30,763  | 113,747.8 | 2,281743 | 7.870699 |
| 6:00-7:00 p.m.             | 3             | 1,077,663                               | 19,241  | 1,849,464 | 0.707025 | 1.5      |

**Table 4.3** Hourly Distributions of Intertrade Duration Observed on May 13, 2009, for SPY

The variation in duration between subsequent trades may be due to several other causes. While the lack of trading may be due to a lack of new information, trading inactivity may also be due to low levels of liquidity, trading halts on exchanges, and strategic motivations of traders. Foucault, Kadan, and Kandel (2005) consider that patiently providing liquidity using limit orders may itself be a profitable trading strategy, as liquidity providers should be compensated for their waiting. The compensation usually comes in the form of a bid-ask spread and is a function of the waiting time until the order limit is "hit" by liquidity takers; lower intertrade durations induce lower spreads. However, Dufour and Engle (2000) and Hasbrouck and Saar (2002) find that spreads are actually higher when traders observe short durations, contrasting the time-based limit order compensation hypothesis.

In addition to durations between subsequent trades and quotes, researchers have been modeling durations between fixed changes in security prices and volumes. The time interval between subsequent price changes of a specified magnitude is known as *price duration.* Price duration has been shown to decrease with increases in volatility. Similarly, the time

interval between subsequent volume changes of a prespecified size is known as the *volume duration.* Volume duration has been shown to decrease with increases in liquidity.

Using a variant of the volume-duration methodology, Easley, Lopez de Prado, and O'Hara (2011) propose volume-based sampling of highfrequency data. In the volume-based approach, the researchers define a clock unit as a "bucket" of certain trade volume, say 50 futures contracts. The volume clock then "ticks" whenever the bucket is filled. Thus, the 50 contract volume clock advances whenever 50 single-contract trades arrive in sequence. The 50-contract volume clock advances twice when a 100 contract trade is executed.

The information content of quote, trade, price, and volume durations introduces biases into the estimation process, however. If the available information determines the time between subsequent trades, time itself ceases to be an independent variable, introducing substantial endogeneity bias into estimation. As a result, traditional estimates of variance of transaction prices are too high in comparison with the true variance of the price series.

## Most High-Frequency Data Do Not Contain Buy-and-Sell Identifiers

Neither Level I nor Level II tick data contain identifiers specifying whether a given recorded trade was a result of a market buy order or a market sell order, yet some applications call for buy-and-sell trade identifiers as inputs into the models. To overcome this challenge, four methodologies have been proposed to estimate whether a trade was a buy or a sell from Level I data:

- Tick rule
- Quote rule
- Lee-Ready rule
- Bulk volume classification

The tick rule is one of the three most popular methodologies used to determine whether a given trade was initiated by a buyer or a seller, in the absence of such information in the data set. The other two popular methods

are the quote rule and the Lee-Ready rule, after Lee and Ready (1991). The newest method is the bulk volume classification (BVC), due to Easley, Lopez de Prado, and O'Hara (2012).

According to the tick rule, the classification of a trade is performed by comparing the price of the trade to the price of the preceding trade; no bid or offer quote information is taken into account. Each trade is then classified into one of the four categories:

- *Uptick,* if the trade price is higher than the price of the previous trade.
- *Downtick,* if the trade price is lower than the price of the previous trade.
- *Zero-uptick,* if the price has not moved, but the last recorded move was an uptick.
- *Zero-downtick,* if the price has not moved, but the last recorded move was a downtick.

If the trade's price differs from that of the previous trade, the last trade is classified as an uptick or a downtick, depending on whether the price has moved up or moved down. If the price has not moved, the trade is classified as a zero-uptick or a zero-downtick, depending on the direction of the last nonzero price change. According to Ellis, Michaely, and O'Hara (2000), in 1997–1998, the tick rule correctly classified 77.66 percent of all Nasdaq trades. [Figure 4.10](#page-26-0) illustrates the tick rule.

<span id="page-26-1"></span><span id="page-26-0"></span>**[Figure 4.10](#page-26-1)** An Illustration of the Tick Rule, Used to Classify Trades into Buys and Sells

A. Uptick: The trade is classified as a buy (initiated by a market buy order)

![](_page_26_Figure_9.jpeg)

B. Zero-uptick: The trade is classified as a buy

![](_page_27_Figure_0.jpeg)

The low proportion of correctly classified trades may be due to specifically to regulatory issues in equities. For example, Asquith, Oman, and Safaya (2008) report that the observed misclassifications are due at least in part to regulations requiring that short sales of stocks be executed on the uptick or zero-uptick (known as the *uptick rule*), the rule the Securities and Exchange Commission (SEC) repealed in 2007. Because nearly 30 percent of equity trades are short sales, Asquith et al. (2008) suggest that regulation-constrained short sales alone may be responsible for the observed errors in trade classification. In the absence of short-sale constraints, all of the preceding trade classifications are likely to be much more precise. On futures data, free from the uptick rule, Easley et al. (2012) indeed find that the tick rule delivers much higher accuracy in classifying

trades into buyer initiated and seller initiated. According to Easley et al. (2012) calculations, the tick rule correctly classifies 86.43 percent of all trades of E-mini futures on the S&P 500.

The quote rule is another way to classify quotes also documented by Lee and Ready (1991) and Ellis et al. (2000). Under this rule, a trade is a buy (sell) if the trade price is above (below) the average of the bid and the ask quotes prevailing at the time. If the trade price happens to be exactly at the midpoint of the prevailing bid and ask, the trade is not classified. While the quote rule is used often and has been shown to correctly classify 76.4 percent of all trades on Nasdaq (see Ellis et al., 2000), the definition of *prevailing quote* may be subject to interpretation and can potentially deliver a worse result than the tick rule. For example, Lee and Ready (1991) point out that quotes and trades are often reported out of sequence, making determination of the prevailing quote difficult. Specifically, they show that with the introduction of electronic books, quotes are often recorded ahead of the trades that triggered them. They propose to mitigate this situation by using the quotes at least five seconds ahead to classify trades. In 1991, five seconds was Nasdaq's median delay in reporting trades. However, the validity of the rule may have deteriorated over the past two decades as markets gained considerable speed since Lee and Ready's study was published. Figure 4.11 shows an example of the quote rule classification.

![](_page_29_Figure_0.jpeg)

**Figure 4.11** Example of the Quote Rule Classification

The so-called Lee-Ready rule classifies trades first using the quote rule. The trades occurring at the midpoint between the prevailing bid and ask quotes are not classified under the quote rule, and are subsequently classified using the tick rule. Once again, Lee and Ready (1991) emphasize matching trades with quotes that occurred at least five seconds prior in order to avoid erroneous sequencing of quotes. Dufour and Engle (2000) follow the five-second rule, while Ellis et al. (2000) object to it, showing that the trade reporting delay may differ depending on the end user's system. Ignoring the five-second delay, Ellis et al. (2000) show that the Lee-Ready rule correctly classifies just 81.05 percent of all trades as either buy or sell-initiated, a small improvement over the tick classification.

To further increase the accuracy of trade classification, Easley et al. (2012) propose a methodology that produces a probabilistic estimate of a particular volume generated by a market buy or a market sell order. The rule, named *bulk volume classification*, works as follows: for every unit of time or volume (a "volume bar," say every 100 shares traded), BVC assigns the probability of the observed volume being a buy as follows:

(10) 
$$\Pr(V_{\tau} = B) = Z \left( \frac{p_{\tau} - p_{\tau-1}}{\sigma \Delta P} \right)$$

where:

is the total volume observed during time or volume interval .

is the price difference observed between the two subsequent time or volume bars, and .

is the standard deviation of sequential time or volume-clock based price changes.

*Z* is the pdf of a standard normal distribution.

The buyer-initiated trade volume can then be estimated as

$$v_{\tau}^{B} = v_{\tau} z \left( \frac{p_{\tau} - p_{\tau - 1}}{\sigma \, \Delta P} \right)$$

According to the BVC, the probability of a specific volume's being generated by a market sell order then becomes:

$$\Pr(V_{\tau} = S) = 1 - \Pr(V_{\tau} = B) = 1 - Z \left( \frac{p_{\tau} - p_{\tau - 1}}{\sigma_{\triangle} P} \right)$$

And the respective size of the seller-initiated volume is then

$$V_{\tau}^{S} = V_{\tau} \left( 1 - Z \left( \frac{p_{\tau} - p_{\tau - 1}}{\sigma \Delta P} \right) \right)$$

Easley et al. (2012) apply the BVC methodology to E-mini futures and show that the BVC rule correctly classifies 86.6 percent of all trades when time bars are used, and 90.7 percent of all trades when the volume clock is used instead of the time-based clock.

#### Summary

Tick data differ dramatically from low-frequency data. Utilization of tick data creates a host of opportunities not available at lower frequencies. A multitude of possible sampling and interpolation techniques creates diverse angles for data exploration. Various methods of organizing and interpreting the discreet ticks of data deliver different statistical properties of the resulting time series.

## End-of-Chapter Questions

1. What are the key properties of high-frequency data?

2. What types of data messages are most frequent?

3. What data sampling technique produces high-frequency time series most closely fitting the normal distribution?

4. What are the key differences between the tick trade classification rule and quote rule, Lee-Ready rule, and bulk volume classification rule?

5. Consider a trade executed at time *t* at 17.01, the best bid quote prevailing at time *t*. The previous trade, executed at time *t* – 1, was executed at 17.00. Should the trade at time *t* be classified as buyer initiated or seller initiated under the quote rule? How should the trade completed at time *t* be classified under the tick rule?

<sup>1</sup> A version of this chapter appears in F. Fabozzi, ed., *Encyclopedia of Financial Models* (3 volume set) (Hoboken, NJ: John Wiley & Sons, 2012).
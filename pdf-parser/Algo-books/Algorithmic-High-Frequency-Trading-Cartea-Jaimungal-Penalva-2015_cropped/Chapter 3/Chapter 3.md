# Em pi rica I and Statistica I Evidence: Prices and Returns

### 3.1 **Introduction**

3

The next two chapters contain empirical analysis of different aspects of trading: prices, returns, spreads, volume, etc., using primarily millisecond stamped data, though we start with daily data that will give us a general overview of the main issues. Chapter 3 focuses on prices and returns, while Chapter 4 is dedicated to volume and market quality measures such as spreads, volatility, or depth.

This chapter, first looks at millisecond data. We then turn to look at the properties of returns both at the daily and at much shorter ( one second) time intervals, as well as looking at the interarrival times of price changes. Section 3.4 looks at how market conditions may change when facing latency, as well as the issue of tick size. This is followed by a discussion on price dynamics. Section 3.6 provides a glimpse of the issue of market fragmentation in the US, while the last section provides .a first look at the empirics of pairs trading.

In addition to the empirical analysis, we also include plausible interpretations and speculation as to what could be behind some of the results of that analysis. These speculations are included to make the chapter more engaging and to encourage the reader to think about the results. However, they should not be interpreted as anything other than speculative theorising, and should be kept separate from the descriptive analysis of the empirical facts that is limited in scope to the data sample we are using.

## 3.1.1 The Data

We use data from several sources. For daily and monthly data we use publicly available aggregated data from Yahoo! Finance, and data from the Center for Research in Security Prices ( CRSP). We also use millisecond timestamped ITCH data (publicly available industry standard data, similar to the direct data feed, recently timestamps go to nanosecond resolution). Our data have been converted into table format for easier processing and is in binary for speed and storage reasons. For illustration purposes we convert these to more human-readable form. The data are made up of the following fields ( we drop two fields that are irrelevant here):

o Timestamp: number of milliseconds after midnight

- Order ID: Unique order ID
- $\bullet$  Message Type:
  - $-$  "B"  $-$  Add buy order
  - $-$  "S"  $-$  Add sell order
  - $-$  "E" Execute outstanding order in part
  - $-$  "C" Cancel outstanding order in part
  - $-$  "F" Execute outstanding order in full
  - $-$  "D" Delete outstanding order in full
  - $-$  "X" Bulk volume for the cross event
  - $-$  "T" Execute non-displayed order
- Shares: order quantity (Zero for "F" and "D" messages)
- Price: zero for cancellations and executions
- Ticker : the ticker associated with the asset in question
- MPID: Market Participant ID associated with the transaction<sup>1</sup>
- Exchange: ID of the current market (NASDAQ  $= 1$ )

These messages record events that affect the limit order book  $(\text{LOB})$ , so essentially, they capture what happens to limit orders (LOs). LOs are posted  $(B,S)$  and later on they are cancelled  $(C,D)$  or executed  $(E,F)$ . So, market orders  $(MOs)$ are not recorded but must be deduced from observing how they are executed against standing LOs (or against non-displayed/hidden orders,  $T$ ).

Consider the following example (the row numbers have been added to facilitate the discussion and we have dropped the MPID column):

| 1: 33219784 4889087 B |   | 1900 | 345800 | TZA  | 1 |
|-----------------------|---|------|--------|------|---|
| 2: 33219784 4887036   | С | 200  | 0      | FMS  | 1 |
| 3: 33219784 4879129   |   | 0    | 0      | QQQQ | 1 |
| 4: 33219784 4889088   | S | 2000 | 454800 | QQQQ | 1 |
| 5: 33219784 4879130   | ת | 0    | 0      | QQQQ | 1 |
| 6: 33219784 4889089   | S | 500  | 454800 | QQQQ | 1 |
| 7: 33219785 4882599   | D | 0    | 0      | QQQQ | 1 |
| 8: 33219785 4888889 F |   | 0    | $\cap$ | STD  | 1 |
|                       |   |      |        |      |   |

These messages are sent to the market between  $33219784$  and  $33219785$  ms from midnight (July 13th, 2010), that is between 09:13:39.784 and 09:13:39.785. We see several messages for the  $\text{ETF }QQQQ$ , and one each for the  $\text{ETF }TZA$ , and the stocks FMS and STD (STD has since changed its ticker to SAN).

The first line is for the TZA ETF and should be read as follows: message recorded at 33219784 ms from midnight (09:13:39.784), with order ID number  $4889087$ , the LO is a posted LO to buy (B) for 1,900 shares at a price of \$34.58 (all prices are in dollars  $\times$  10,000). The number 1 in the final column represents the market code for NASDAQ.

For  $QQQQ$  we observe an LO being cancelled (row 3), followed by the posting of a sell LO  $(4)$ , another LO cancellation  $(5)$ , a second sell LO posted  $(6)$ 

 $1$  This information is usually missing from the public feed.

and a third LO being cancelled (7). The posted sell orders include the quantity and price for the orders (2,000 at \$45.48 and 500 also at \$45.48), while cancelled orders must be matched with their original posted orders (ID 4879130 and 4882599) in order to identify the corresponding prices and quantities. vVe see the same pattern for the full execution of order ID 4888889 for STD (8) - i.e. no price or quantity - while for FMS (2) we see a partial cancellation of 200 units from order ID 4887036 (the price needs to be read off the original posted order).

From this data, one can reconstruct the complete order book at any point in time, and study how the market changes over time using different variables and methods. We now proceed to give a brief overview of some of the features we observe.

#### 3.1.2 Daily Asset Prices and Returns

When trading, the first variable of interest is the price level. If we have to acquire/liquidate a position we want to know what price we can get if we aggressively execute it, and if we are providing liquidity we want to know at what prices shares are being bought and sold.

As we discussed in Section 1.2, each investor is in the market to meet some objective, and will participate for as long as she feels that she is not losing too much money in pursuit of her objective (e.g., if the transaction costs do not consume the expected price gains, or if the market will adjust prices in reaction to her order, eliminating the original mispricing she wanted to profit from - we discuss these below). The observed price process is the outcome of the interaction between these investors. In electronic markets, we see these prices continuously as traders change their positions to meet their objectives in response to changes in market conditions and information flows. Market efficiency theories tell us that the resulting price process is not predictable and any positive expected return you can predict, is there as compensation for bearing risk. Thus, long-term investors receive a compensation for risk, be this market risk, risk from monetary policy changes, or just compensation for future price fluctuations and dividend uncertainty. Liquidity providers also require compensation: they require compensation for leaving offers at the bid and ask, and will continue to post orders while their trades are sufficiently profitable. Other traders pursue strategies aimed at exploiting deviations from market efficiency, such as keeping prices of similar assets close to each other.

Whether one believes in market efficiency or not, the properties of the price process are amenable to analysis and in this chapter we look at some of the methods and results obtained from detailed message data for specific assets.

We analyse the properties of the price process for a selection of assets from equity markets. Our primary focus is on 2013 prices for AAPL (Apple Inc.), as representative of a highly liquid, very highly traded asset. To illustrate differences across assets, we look at three other assets with tickers ISNS, FARO and MENT: ISNS is the company Image Sensing Systems, Inc. Industry (Application Software); FARO is FARO Technologies Inc. (Scientific & Technical Instruments); and MENT is Mentor Graphics Corp. Industry (Technical & System Software). These assets are all in the technology sector and represent different levels of trading activity (although depending on your definition, you can argue about whether AAPL is a technology or a consumer goods firm).

#### $3.1.3$ Daily Trading Activity

In Table 3.1 we can see different measures of trading activity for these assets: average number of transactions per day on NASDAQ  $(N)$ , average total daily dollar value of shares traded on NASDAQ  $(V(\$))$ , in 000s), average number of shares traded daily on NASDAQ  $(V(Q))$ , in 000s), total average number of shares traded in all markets (Total  $V(Q)$ , in 000s), and **share turnover** (Turnover). Share turnover represents the total number of shares traded during 2013 divided by the number of **outstanding shares** -also included in Table 3.1 (ShrOut, in millions, as of Dec 30th, 2012). From the column with the number of transactions  $(N)$  and using the fact that the regular market is open for 6.5 hours (from 9:30 to 16:00) we can conclude that ISNS is a very rarely traded asset (traded about once every half hour in 2013), while FARO and MENT are regular small assets (with on average 1 to 3 trades per minute in 2013), and AAPL is one of the most highly traded equity stocks (around 1 trade per second  $-$  note that we are using 2013 data, and these numbers are not rescaled to account for the AAPL June 2,  $2014$  7-for-1 split).

| $\text{Asset}$ | N      | (\$<br>$(\times 10^3)$ | V(Q)<br>$(\times 10^3)$ | Total $V(Q)$<br>$(\times 10^3)$ | $\text{ShrOut}$<br>$(\times 10^{6})$ | Turnover |
|----------------|--------|------------------------|-------------------------|---------------------------------|--------------------------------------|----------|
| ISNS           | 14     | 18                     | 3                       | 12                              | 5                                    | 0.62     |
| FARO           | 315    | 1,396                  | 34                      | 137                             | 17                                   | 2.04     |
| MENT           | 908    | 3.964                  | 204                     | 694                             | 112                                  | 1.56     |
| $\text{AAPL}$  | 24.582 | 1,505,175              | 3,208                   | 14,516                          | 941                                  | 3.89     |

**Table 3.1** Daily Average Volume in 2013 for selected assets.

This pattern is repeated regardless of which measures of volume in Table 3.1 you look at, and whether measured only for the NASDAQ market or for all markets together.

#### 3.1.4 Daily Price Predictability

We first look at the properties of the price process by considering returns constructed from changes in prices from market open to market close for each day in 2013. According to the efficient market hypothesis, daily asset returns should be close to unpredictable and reflect information in the market. To investigate

this we run ordinary least squares (OLS) regressions for intra-day (market open to market close) returns for our four assets. We include a number of variables related to market efficiency and market forces as follows.

The first of these variables is the return on the SPY: the SPY is an exchangetraded fund (ETF) that tracks the S&P500 index. In subsection 1.1 we discussed ETFs in the context of the different types of asset classes in the market, and saw that the SPY is an asset traded on the exchanges, just like ISNS, FARO, MENT and AAPL. When we buy the SPY we buy a fund (similar to a mutual fund or a pension fund) whose objective is to track the S&P500 at the lowest possible cost. Thus, many investors who just want the value of their investments to move with "the market" (as represented by the S&P500) prefer to buy the SPY rather than invest in an equity-based mutual fund. Moreover, traders would rather purchase the SPY than acquiring all the 500 assets in the index, since it is (much) cheaper to do so, and removes the costs associated with constantly rebalancing one's portfolio to match changes in the weights the different assets represent in the S&P500. The cost of doing so, but doing so efficiently, is already incorporated into the SPY.

Another variable is the volatility index VIX: the VIX is an index continuously published by the Chicago Board of Options Exchange which is designed to measure the market's expectation on future short-term volatility in the S&P500 index - it is computed by taking a certain weighted average of short-term options on the S&P500 index. It is used as a proxy for market uncertainty, investor sentiment, the market taste for risk (market risk aversion) and other related concepts. There are ETFs that try to track VIX, there are futures backed by it, and there are options based on the index.

A third variable of importance is order flow. By order flow we mean the difference between the number of shares aggressively bought and shares aggressively sold. Naturally, in a market, for every transaction there is a buyer and a seller. But, in electronic markets we can differentiate between posted limit orders (LOs) and executed market orders (MOs). Thus, if a transaction is the result of a passive limit sell (buy) order being lifted (hit) by an aggressive market buy (sell) order, we refer to it as an aggressive buy (sell) order. An aggressive buy (sell) order is driven by some trader's desire for a rapid buy (sell) and indicates her demand for (supply of) shares of this asset to the overall demand/supply in the market. Thus, the order flow is a proxy for the net demand for the asset which, as we saw in Chapter 2, can incorporate information relevant to market making strategies and future price movements.

In Table 3.2 we show the regression coefficients from the OLS regressions for the following two models.

$$r_{t,j} = \alpha + \beta_{1,j} r_{t-1,j} + \beta_{2,j} \text{SPY}_t + \beta_{3,j} \text{VIX}_t + \beta_{4,j} \log(1 + Q_t) + \beta_{5,j} \text{OF}_t + \epsilon_{t,j}$$
(3.1)

$$\begin{split} r_{t,j} &= \alpha + \beta_{1,j} \, r_{t-1,j} + \beta_{2,j} \, \text{SPY}_t + \beta_{3,j} \, \text{VIX}_t + \beta_{4,j} \, \log(1+Q_t) + \beta_{5,j} \, \text{OF}_t \\ &+ \beta_{6,j} \, \text{SPY}_t \, \mathbf{1}_{\text{SPY}_t < 0} + \beta_{7,j} \, \text{VIX}_t \, \mathbf{1}_{\text{VIX}_t < 0} + \epsilon_{t,j}. \end{split}$$

 $(3.2)$ 

The first model  $(3.1)$  (M1 in Table 3.2) is an OLS regression for the intraday return for each of our four stocks, where  $r_{t,i}, j \in \{ \text{ISNS}, \text{FARO}, \text{MENT}, \text{AAPL} \}.$ The return is computed as the price of the stock at the close of the market minus the price of the stock at the opening of the market, divided by the price of the stock at the opening of the market:  $r = \frac{P_{\text{close}} - P_{\text{open}}}{P_{\text{open}}}$ . The model includes as right-hand side variables:

- (i)  $\alpha$ : a constant which captures the mean-daily return and should be close to  $zero,$
- (ii)  $r_{t-1,j}$ : the previous day's intra-day return (should be insignificant as returns should not be predictable),
- (iii)  $SPY_t$ : the contemporaneous intraday return on the  $SPY$  computed like the stock's intra-day return,
- (iv)  $\text{VIX}_t$ : the contemporaneous intraday 'return' on the VIX computed like the stock's intra-day return,
- (v)  $\log(1+Q_t)$ : the log of one plus the number of shares of the stock traded in all markets that day (we add one so that when no shares are traded we do not have to deal with  $\log(0)$ ,
- (vi)  $OF_t$ : order flow for the stock on NASDAQ that day.

In addition, the second model  $(3.2)$  (M2 in Table 3.2) includes the variables in the first model  $(M1)$ , plus the returns on the SPY and the VIX multiplied by indicators which equal 1 on days in which the VIX or the NASDAQ moved down, and  $0$  otherwise. These two variables allow us to verify if there is an asymmetric reaction of the asset's return to any 'good' or 'bad' news on the market (or its volatility).

The fitted models in Table 3.2 represent **robust OLS** estimates. Robust OLS estimation is very similar to the standard OLS minimisation of the sum squared residuals, that is, the minimisation of the sum of the squared distance between the observations and the fitted values. The main difference between standard and robust OLS is that with robust OLS the errors in the estimation are weighted so as to reduce the impact of outliers on the estimated parameters. To obtain the estimates in Table 3.2, the weighting is done iteratively and using the Huber's loss function which penalises large errors linearly rather than quadratically – more details on OLS and robust OLS can be found in any standard econometrics textbook, e.g., see Greene (2011) or Cameron & Trivedi (2005).

|            | ISNS  |       |       | FARO  | MENT  |       | AAPL  |       |
|------------|-------|-------|-------|-------|-------|-------|-------|-------|
| Variables  | Ml    | M2    | Ml    | M2    | Ml    | M2    | Ml    | M2    |
| constant   | 0.25  | 0.27  | -2.83 | -2.92 | -2.97 | -3.07 | 1.09  | 1.18  |
| Tt-1,j     | -0.10 | -0.09 | 0.06  | 0.06  | 0.05  | 0.05  | -0.12 | -0.12 |
| SPY(%)     | -0.60 | -1.36 | 1.04  | 1.03  | 1.04  | 1.07  | 0.28  | 0.06  |
| VIX (%)    | -0.08 | -0.01 | -0.03 | -0.05 | 0.00  | 0.01  | -0.03 | -0.02 |
| Log Q      | 0.01  | 0.00  | 0.25  | 0.27  | 0.23  | 0.24  | -0.08 | -0.08 |
| Order Flow | 0.03  | 0.02  | 0.05  | 0.05  | 0.03  | 0.03  | 0.06  | 0.05  |
| Negv SPY   |       | 1.43  |       | 0.11  |       | -0.08 |       | 0.52  |
| Negv VIX   |       | -0.19 |       | 0.06  |       | -0.01 |       | -0.01 |
| Adj R      | 0.01  | 0.01  | 0.17  | 0.17  | 0.27  | 0.27  | 0.31  | 0.31  |

**Table 3.2** Robust OLS regression of intraday (open-to-close) return. (Bold: 5% significance)

As Table 3.2 shows, the OLS results for the thinly traded ISNS reflect a lot of noise (in the sense that the R-squared ( "adj R") is very close to zero) and the significance of the coefficients is not very reliable. For the other assets we find that the OLS regression does pick up some information, and there is one variable that is consistently significant for the other three assets, namely order flow. The coefficient is significant and positive for all three assets indicating that NASDAQ order flow and the asset's return move together, which is consistent with the interpretation of order flow as the market's net demand for the asset, and the models of liquidity of Glosten and Milgrom, and Kyle. We expected the constant and the previous day's return to be insignificant, and we find the first to be the case, and the latter to be true for FARO and MENT. AAPL displays a negative autocorrelation in daily returns, which suggests a significant mean-reverting component in the return process which is not consistent with the efficient market hypothesis, and provides evidence of (negative) short-run momentum, although in the microstructure literature (Roll (1984)) the presence of negative autocorrelation can also be explained in terms of the 'bid-ask bounce' - that is, that trades do not take place at the 'market price' but rather an aggressive buy has to cross a non-zero spread to match with the bid and executes against the LO standing there, at the bid. Finally, we find that during 2013 our assets' returns were not significantly affected by changes in market sentiment (as measured through the VIX). FARO and MENT have significant exposure to market movements, though AAPL (somewhat surprisingly) seems not to. We also find no significant evidence that there is an asymmetry between 'good' and 'bad' news from movements either in the market or in market sentiment.

![](_page_7_Figure_1.jpeg)

Figure 3.1 Sample distribution and QQ-plot of the 1-second returns of AAPL on July 30, 2013.

#### 3.2 Asset Prices and Returns Intraday

Daily market information is of primary interest only for investors with mediumto long-term investment horizons, but high-frequency trading strategies are executed over very short horizons so we must look at what goes on in much finer detail. To do so, we use millisecond-stamped message-level ITCH data for the NASDAQ market to study prices over several sampling periods.

Focusing on AAPL and on a single day, July 30th 2013, we construct asset returns over one-second intervals. The choice of dates is arbitrary. It was a day with a small positive price gain and positive net order flow: there were  $1.45$ million shares bought vs 1.24 million shares sold on NASDAQ, and the price increased from market open ( $$449.96$ ) to market close ( $$453.32$ ) by  $$3.36$  ( $+74$ bps).

The asset's return is computed using the microprice. The **microprice**  $(S_t^*)$ , also called the weighted-midprice, is the weighted average of the best bid  $(P_t^b)$ and the best ask  $(P_t^a)$ , weighted by the relative quantities posted at the bid  $(V_t^b)$ and ask  $(V_t^a)$ :

$$S_t^* = \frac{V_t^b}{V_t^b + V_t^a} P_t^a + \frac{V_t^a}{V_t^b + V_t^a} P_t^b.$$
 (3.3)

The microprice is similar to the midprice, but it incorporates information on order imbalance: e.g., a relatively larger quantity of offers on the bid than on the ask indicates greater buying pressure, and the 'true' price is closer to the ask than to the bid (the microprice was discussed at the end of Chapter  $1$  – also Chapter 12 is devoted to trading strategies that employ volume imbalance in the LOB as a key variable in trading decisions, the same volume imbalance that moves the microprice towards the ask or the bid).

The choice of sampling frequency is important as it has a very significant effect on the properties of the empirical distribution of the asset's return. If the sampling frequency is very short then many of the observations will be equal to

![](_page_8_Figure_1.jpeg)

Figure 3.2 Plot of the tails (log scales) for AAPL on July 30, 2013.

zero. In our example, we sample at the one second frequency, and find that for AAPL on July 30, 2013,  $33\%$  of the returns are equal to zero.

We carry out our analysis using returns, and we use basis points (bps) as our unit of analysis (that is, a value of  $1$  in Figure 3.1 represents a change in the microprice of  $1/100$ th of a percentage point). In our sample, the average microprice is  $$454.30$ , so that a positive return of 1 bps represents an increase in the microprice of  $4.5$  cents, and  $0.22$  bps is equivalent to 1 tick, i.e. one cent. Looking at the histogram of the 1-second returns in the left panel of Figure  $3.1$ , we find that the distribution is single-peaked and seems to have fat tails. This is confirmed by the  $QQ$ -plot in the right panel of Figure 3.1.

The fat tails exhibited by the asset returns occur often when sampling at short intervals, but may persist at longer frequencies. Figure 3.2 zooms into the right and left tails. Specifically, we use returns above the  $95$ th percentile  $(1.94)$ bps) and below the 5th percentile  $(-1.94 \text{ bps})$  to define these tails. Taking these cutoff values as given, we assume the tails follow a power-law with a probability distribution function given by  $f(r)$ , where

$$f(r) = \frac{\alpha - 1}{r_{\min}} \left(\frac{r}{r_{\min}}\right)^{-\alpha} \,,$$

and estimate the parameter  $\alpha$  using maximum likelihood estimation (MLE). The MLE for  $\alpha$  can be shown to be (see, e.g., Clauset, Shalizi & Newman (2009))

$$\hat{\alpha} = 1 + T \left[ \sum_{t=1}^{T} \log \left( \frac{r_t}{r_{\min}} \right) \right]^{-1}$$

Using the given cutoffs, these estimators give us  $\hat{\alpha}_{\text{right}} = 3.35$  and  $\hat{\alpha}_{\text{left}} = 3.38$ . The model fit of the tails corresponds to the black dashed lines in Figure 3.2, and indicate that the 1-second returns have very heavy tails.

To gain a sense of whether the market behaves in accordance with the efficient market hypothesis, we estimate the autocorrelation function (ACF) from the return data. Recall that the ACF  $f(n)$  is given by the correlation of  $r_{t-n}$  with  $r_t$ 

![](_page_9_Figure_1.jpeg)

Figure 3.3 Sample ACF of 1-second returns for AAPL on July 30, 2013.

and can be estimated from the sample correlation. The sample ACF for APPL on July  $30, 2013$  is shown in the right panel of Figure  $3.3$ . This gives a negative and significant autocorrelation for the first lag, which indicates a significant meanreversion component in the microprice. We also find that the 12th lag is (weakly) significant and positive, while the 14th is negative and significant. There are no strong theoretical reasons to observe such patterns, so without further research we cannot be sure if this is a spurious pattern that appears on this particular day, or something truly significant.

#### 3.3 Interarrival Times

We have seen that even at one second intervals,  $33\%$  of the time there are no price changes. As the sampling frequency becomes smaller, it becomes increasingly tenuous to try to model the observed prices as a continuous process, and we need to consider discrete processes. We start by looking at the interarrival times between movements at either the bid or the ask.

Let  $\tau_i$  denote the times at which there is change either in the bid or in the ask, and we look at the frequency of interarrival times,  $X_i = \tau_{i+1} - \tau_i$ . The mean is  $10.4 \text{ ms}$  and the median  $3 \text{ ms}$ . Figure  $3.4 \text{ provides additional insight: the top}$ panels describe the histogram of  $X_i$  in absolute and log scales, while the bottom panel contains the  $QQ$ -plot relative to the exponential (with the same mean). These graphs indicate that the interarrival times have a power-law distribution with very heavy tails. We estimate the parameter for the right tail (as we did for the 1-second returns above), and we obtain an MLE of  $\hat{\alpha} = 3.13$  for the power using the  $95\text{th percentile (41 ms)}$  as the cutoff.

We also briefly look at the dynamics of the interarrival process. Figure  $3.5$ describes the ACF. As shown, changes to the bid and ask are not independent, but have a strong autocorrelated component. This suggests a commonly observed empirical fact about such changes, namely, that they cluster. Rapid changes in the bid/ask are followed by further rapid changes, while a relatively long calm period is also similarly followed by another calm period.

![](_page_10_Figure_1.jpeg)

**Figure 3.4** Plot of the frequency of interarrival times  $(X)$  in absolute and log scales for AAPL on July 30, 2013. The bottom panel describes the QQ-plot relative to the exponential distribution and the power law distribution:  $\mathbb{P}(X_i \leq x) = 1 - (k/x)^{\alpha}$ .

![](_page_10_Figure_3.jpeg)

![](_page_10_Figure_4.jpeg)

#### 3.4 Latency and Tick Size

Suppose we wish to execute a trade, e.g., buy 1,000 shares of AAPL. The first trade-off we face is immediacy versus cost of execution. If you are concerned about immediacy, the fastest way to execute a trade is to cross the spread and aggressively execute as much as possible using a market order  $(MO)$ . But, any agent for whom immediacy is very important needs to account for a new issue: message latency. Latency refers to the delay between sending a message to the

market and it being received and processed by the exchange. Sometimes the time it takes for the exchange to acknowledge receipt of the message is also added in. Latency is random and depends on many factors such as distance between sender and exchange, the structure and type of network, the amount of orders in the network (which can generate congestion), etc. In addition, the word latency is more generally used to express the time it takes for a message to travel from one point to another, such as the latency of a news feed. A classic example of latency is the time it takes for a message to go from the Chicago options exchange ( or rather, the CME colocation centre) to New York ( or rather, NASDAQ's processing centre in New Jersey). The latency between these two centres is estimated to be between 7.5 and 6.7 ms when travelling by fibre optic cable, or between 4.2 and 5.2 ms when travelling by microwave ( on a clear day).

If an agent is trading from home, through a broker, she must be aware of the substantial delay between the moment she asks her broker to execute her order and the time it reaches the market. During that time, market conditions may have changed a great deal. If, however, the agent is trading directly through a broker's feed or she has her own feed into the market, the latency will be much shorter, though still significant relative to centres which are colocated. Being colocated, also known as colocation, means that an agent's trading system is physically housed at the electronic exchange's data centre and has a direct connection to the exchange's matching engine. In principle, those who are colocated face similar latency amongst themselves - though there will still be some latency dependent on their software and hardware configurations ( colocation was also discussed in Chapter 1).

Latency is an issue for agents for several reasons. An agent who is trading frequently and on narrow margins needs to be aware of the state of the market and be able to adapt her orders, whether to post a new or cancel an existing LO, or submit an MO. Furthermore, when executing an MO, an agent needs to be aware of the relationship between her choice of routing strategy and how other traders may react to the information that may be extracted from observing the strategy's outcomes. A large, poorly routed MO will telegraph its progress through the several exchanges leading to poor execution quality and high execution costs, as other traders reposition themselves to absorb the order at more favourable prices (to them).

For certain assets, circumstances change very fast while for others the market is quite stable. We see this in the movements of prices and spreads in Tables 3.3 and 3.4. The former captures the slow changes in seldom traded assets, such as ISNS, FARO or MENT. The latter looks at more frequently traded stocks, AAPL and ORCL.

Table 3.3 looks at what happens to the bid/ask/midprice/quoted spread from the end of one minute to the next for three assets: ISNS, FARO and MENT. A one minute delay is a very long time for a trader, and one would not expect such a delay unless one is trading through a very slow connection to the exchange ( or the order does not go directly to the exchange). We see this in the first column of

|       |               | L'l.X#O |       |      | Stats (for L'l.X # 0) |     |      |
|-------|---------------|---------|-------|------|-----------------------|-----|------|
| Asset | Var           | (%)     | POl   | Ql   | Q2                    | Q3  | P99  |
| ISNS  | Bid           | 4.2     | -43.0 | -4.0 | 1.0                   | 5.0 | 40.0 |
|       | Ask           | 3.4     | -51.0 | -4.0 | -1.0                  | 3.0 | 51.0 |
|       | Mid price     | 6.7     | -25.8 | -2.0 | 0.5                   | 2.0 | 26.8 |
|       | Quoted Spread | 6.7     | -45.0 | -5.0 | -1.0                  | 4.0 | 46.0 |
| FARO  | Bid           | 48.6    | -21.0 | -2.0 | 1.0                   | 3.0 | 19.0 |
|       | Ask           | 49.0    | -19.0 | -3.0 | -1.0                  | 3.0 | 22.0 |
|       | Midprice      | 63.4    | -16.0 | -1.5 | 0.5                   | 2.0 | 16.0 |
|       | Quoted Spread | 60.8    | -18.0 | -2.0 | -1.0                  | 2.0 | 18.0 |
| MENT  | Bid           | 44.2    | -5.0  | -1.0 | 1.0                   | 1.0 | 6.0  |
|       | Ask           | 44.1    | -5.0  | -1.0 | -1.0                  | 1.0 | 5.0  |
|       | Mid price     | 52.8    | -4.5  | -1.0 | 0.5                   | 1.0 | 5.0  |
|       | Quoted Spread | 31.1    | -5.0  | -1.0 | -1.0                  | 1.0 | 4.0  |

Table 3,3 One minute changes in bid, ask, midprice, and quoted spread.

Table 3.3 (labelled 6.X *cf.* 0) where we find the percentage of minutes for which the bid/ask/midprice/quoted spread is different (not equal to zero). For ISNS we observe that for only 4.2 percent of the time are there changes in the bid from one minute to the next. In the adjacent columns we can see the statistics for those minutes in which the variable of interest changed. From these, we can conclude that for half of the time ISNS's bid price changed, it moved between an increase of 5 cents (Q3) and a drop of 4 cents (Ql). If we look at the midprice for ISNS, we see that it changed only 6.7 percent of the time, and when it did, half of those changes were between an increase of 2 cents and a drop of 2 cents. On the other hand, if one considers assets such as FARO or MENT, a oneminute delay will face changes in the bid (similarly in the ask) around half of the time, as well as (naturally) in the midprice and quoted spread. Note that this is an unconditional analysis for all minutes of 2013, and does not take into account that market participants react to order flow. For example, if one sends a market buy order, then other agents may quickly adjust their quotes upwards in response to this new information. Hence, it is natural that an asset with very little public information (in the form of trades/MOs) like ISNS will see fewer price movements than more frequently traded ones, like FARO or MENT.

This is not the same picture that we find when looking at the most popular stocks (in terms of activity). Assets such as AAPL and ORCL will almost certainly experience changes in prices within one minute, but for these assets a one minute delay is unreasonably long by any standard. Table 3.4 reflects the same information as Table 3.3 but after a 100 ms delay rather than one minute (and for the last three months in 2013 rather than the whole year). Also, rather than report the statistics for the whole sample, we report the median values for the statistics computed at the daily level. That is, after computing the daily percent-

|       |               | b.X/0 |       |      | Stats (for b.X # 0) |     |      |
|-------|---------------|-------|-------|------|---------------------|-----|------|
| Asset | Var           | (%)   | POl   | Ql   | Q2                  | Q3  | pgg  |
| AAPL  | Bid           | 3.84  | -17.0 | -3.0 | -1.0                | 3.0 | 18.0 |
|       | Ask           | 4.00  | -18.3 | -3.0 | 1.0                 | 3.0 | 17.0 |
|       | Midprice      | 6.75  | -11.5 | -1.5 | 0.5                 | 1.5 | 11.0 |
|       | Quoted Spread | 6.69  | -16.0 | -3.0 | -1.0                | 3.0 | 18.0 |
| ORCL  | Bid           | 0.41  | -2.0  | -1.0 | -0.5                | 1.0 | 2.0  |
|       | Ask           | 0.40  | -2.0  | -1.0 | 1.0                 | 1.0 | 2.0  |
|       | Midprice      | 0.47  | -2.0  | -1.0 | 0.5                 | 1.0 | 2.0  |
|       | Quoted Spread | 0.16  | -3.0  | -1.0 | -1.0                | 1.0 | 2.0  |

Table 3.4 One hundred ms changes in bid, ask, midprice, and quoted spread.

age of 100 ms intervals with non-zero bid price changes for AAPL for each day from October to December 2013, we report that the median of these is 3.84%. Similarly, after computing the first quartile of the non-zero bid price changes for each day, we report the median of these, which is -3 cents, while the median of the third quartiles is an increase of 3 cents.

Note that there is a noticeable difference in the frequency and magnitude of price changes for AAPL and ORCL. AAPL sees more frequent changes and of greater magnitude than ORCL. There are two factors that are important here: (i) the volume traded (in dollars) for AAPL is one order of magnitude greater than for ORCL, but also, (ii) the price of AAPL in the last quarter of 2013 was between \$490 and \$560, while that of ORCL was between \$32 and \$38. As both assets have the same minimum tick size ( of one cent), this means that AAPL can experience much smaller percentage changes in its price (1 cent **=** 0.2 bps of \$500) than ORCL (1 cent **=** 2.5 bps of \$40). Thus, one would expect more frequent price movements for AAPL than for ORCL ( even after AAPL's share split of one old share into seven new ones, as after the split and AAPL prices around \$100, a one cent change is equivalent to a 1 bps change, much greater than the 2.5 bps of ORCL).

## **3.5 Non-Markovian Nature of Price Changes**

In this section, we investigate how successive price changes are interrelated. For this, we first look at whether the sign of the current price change can predict the sign of the next (non-zero) price change. *We* continue using AAPL on July 30, 2013 for the analysis, and record price changes every time they occur. In Table 3.5 we see how an increase in the price (bid or ask) is more often than not followed by a reversal, and similarly for a fall in the price.

In Table 3.5 we see that an increase in the ask price (an uptick) is followed by a down tick 57% of the time, while a drop in the ask is followed by an increase

|               | Ask    |          |               | Bid    |          |
|---------------|--------|----------|---------------|--------|----------|
|               | Uptick | Downtick |               | Uptick | Downtick |
| t / t + 1     | (11')  | (�)      |               | ( 11') | (�)      |
| Uptick ( 11') | 43.0   | 57.0     | Uptick (11')  | 36.5   | 63.5     |
| Downtick ( �) | 61.8   | 38.2     | Downtick ( �) | 55.3   | 44.7     |

**Table 3.5** Empirical Transition Rates: Single Price Change.

61.8% of the time. For the bid price the numbers are 63.5% and 55.3% of the time. Earlier, in Table 3.4, we saw that a 100 ms latency resulted in no changes in the bid more than 96 percent of the time (in at least half the observation period). But, in Section 3.3 we saw that the median interarrival time of a change in either the bid or the ask is 3 ms ( that for the bid is 8 ms). The numbers in Table 3.5 help us reconcile these two seemingly contradictory statements: even though after a 100 ms delay one may not observe a *net* change in the bid, this zero net change is a result of both no changes during the 100 ms period and also of several changes that cancel each other out. So, for latencies greater than 8 ms, if you submit an MO, by the time it hits the market, the price may have moved away but it may also have returned to the price that was there when the MO was submitted. Latency, therefore, introduces execution risk specially for traders who are not colocated.

Table 3.5 also illustrates an asymmetry that appears on this day in the relative frequencies of ptice reversals. This asymmetry suggests that a shrinking of the quoted spread ( a fall in the ask or an increase in the bid) was more likely to be reversed than an increase in the quoted spread ( an increase in the ask or a fall in the bid).

So we present Table 3.6 to investigate whether the sign of the current price change can predict the sign of the price changes in the next two periods. This table describes the relative frequency of price reversals ('Reversal', 1r � or � 1r) relative to consecutive movements in the same direction ('Up'(il'il') and 'Down'(��)) conditional on the current price change being up 1r or down �- Around 60% of consecutive changes in the bid and in the ask are in opposite directions. Table 3.6 shows not only the conditional probability of the future two price moves, but also the unconditional one. Comparing those transitions we are led to the conclusion that there seems to be little if any difference between the conditional and the unconditional transitions. Thus, even though price changes tend to be reversed, the direction of the current price change (whether it is an uptick or a downtick) does not carry additional information about future price changes.

Finally, we consider a longer sequence of price changes, i.e. we consider whether the signs of the two past price changes can predict the next one. To accomplish this we define four states, one for each possible pair of signs of price changes as follows: *A* is an uptick followed by another uptick *(A* = i)'il'), *B* is an uptick followed by a downtick ( *B* = i)' �), *C* is a down tick followed by an uptick ( *C* = � 1r),

|                     |                  | Ask                    |                    |
|---------------------|------------------|------------------------|--------------------|
|                     | Up(t+l,t+2)      | Reversal(t + 1, t + 2) | Down(t + 1, t + 2) |
|                     | (1r1r)           | (11'-!J,, -(!,11')     | (-(!,-(!,)         |
| Uptick(t) (11')     | 17.1             | 59.5                   | 23.4               |
| Downtick( t) (-(!,) | 19.6             | 59.1                   | 21.3               |
| Unconditional       | 18.3             | 59.3                   | 22.4               |
|                     |                  | Bid                    |                    |
|                     | Up(t + 1, t + 2) | Reversal(t + 1, t + 2) | Down(t + 1, t + 2) |
|                     | ( 1r1r)          | (11'-!J,, -(!,11')     | (-(!,-(!,)         |
| Uptick(t) (11')     | 24.0             | 60.3                   | 15.7               |
| Downtick( t) (-(!,) | 23.7             | 58.1                   | 18.2               |
| Unconditional       | 23.9             | 59.1                   | 17.0               |

Table 3.6 Empirical Transition Rates: Pairs of Tick Changes.

and D is a down tick followed by another downtick ( D **=** JJ,JJ,). The price change signs are then used to generate a sequence of *A, B, C, D* with overlapping observations, so that, e.g., the sequence 11 JJ,JJ,11 would be represented as *BDC.*  Note that there are several transitions that cannot occur. For example, *B* cannot be followed by *A,* since if the price change was B(11JJ,), then either (i) the next change is 11, in which case we transition to the state C(JJ,11), or (ii) the next change is JJ,, in which case we transition to the state D( JJ,JJ,).

The estimated transition frequencies for this Markov chain are provided in Table 3.7. The transition *AA* should be interpreted as the sequence of ticks 111111, *BC* as 11JJ,11, and so on. In the table we can see confirmation of price reversals: the transitions *BC* and *CB* have markedly higher probability, suggesting that successive price movements (both for the bid and the ask) tend to go in opposite directions.

## **3.6 Market Fragmentation**

Another issue to consider when executing aggressively is that of market fragmentation. vVe only address this issue superficially here but it is a serious concern for high-frequency traders.

So far we have focused on detailed data from one exchange, NASDAQ. As of October 2014 in the US there were 11 exchanges and around 45 alternative trading venues, most of which were dark pools - dark pools are trading venues that do not publicly display price quotes and in 2014 NASDAQ represented around 20 percent of the trading (later, in section 7.4, we provide execution algorithms were the agent has access to a standard lit market and also to a dark

|                                             |      | Ask    |              |                                          |
|---------------------------------------------|------|--------|--------------|------------------------------------------|
| $(t + 1)$                                   | А (🏠 | B (∱↓) | С (↓ ↑)      | $D \ (\Downarrow \Downarrow)$            |
| $A(t)$ ( $\Uparrow\Uparrow$ )               | 54.4 | 45.6   |              |                                          |
| $\mathbf{B}(t) \; (\Uparrow \Downarrow)$    |      |        | 70.0         | 30.0                                     |
| $C(t)$ ( $\downarrow \Uparrow$ )            | 34.4 | 65.6   | 0.0          | 0.0                                      |
| $D(t) \ (\downarrow \downarrow \downarrow)$ |      |        | 48.6         | 51.4                                     |
|                                             |      |        |              |                                          |
|                                             |      |        |              |                                          |
|                                             |      |        | $\text{Bid}$ |                                          |
| $(t + 1)$                                   | А (🏠 | B (∱↓) | С (↓↑        | $D \left( \Downarrow \Downarrow \right)$ |
| $A(t)$ ( $\Uparrow\Uparrow$ )               | 43.0 | 57.0   |              |                                          |
| $\mathrm{B}(t) \; (\Uparrow \Downarrow)$    |      |        | 62.2         | 37.8                                     |
| $C(t)$ ( $\downarrow \Uparrow$ )            | 32.8 | 67.2   |              |                                          |

**Table 3.7** Empirical Transition Rates: Pairs of Ticks.

pool). So, we cannot truly talk about 'the market' as a single exchange, but as the aggregation of activity across a large number of venues. To get an idea of the degree of market fragmentation, that is, the extent to which the market for one asset is distributed across different venues, we look at trading during market hours (9:30-16:00) for one asset, AAPL, on July 30, 2013 across all venues using Consolidated Tape data. These data provide information on all transactions and best quotes from all venues.

Here we have reconstructed the bid and ask for the venues for which we have AAPL activity reported during that day. With the reconstructed bid and ask, we compute the percentage of time each exchange's best price (the bid or the ask) coincides with the best price across all venues. Table 3.8 captures this information. We can see that NASDAQ-OMX's bid coincides with the best bid across all venues during 67 percent of regular trading hours, while the same figure is 19 percent for BATS, 43 percent for the NYSE-ARCA, 35 percent for  $\text{EDGE-X}$ and never for EDGE-A markets.

Thus, optimally executing a trade is not just about timing and prices displayed in one exchange, but also about: how to organise the way an order (or orders) reaches a particular trading venue, what the different laws governing how exchanges should handle orders are and the rules exchanges use to implement them, how to programme the routing of the order, and which order types are best suited to one's particular routing and trading strategy, etc.

In the US the specific regulation, Reg NMS (National Market System), has been set up to facilitate competition between exchanges and to protect investors. In particular, it has specific provisions to protect investors' orders by preventing trade-throughs (i.e. the execution of an order at an inferior price when a better price is available, especially when that price comes from a 'proper' (protected)

|                     |              | $Percentage$ $Time$ at $NBBO$ |
|---------------------|--------------|-------------------------------|
| Exchange            | $\text{Bid}$ | Ask                           |
| NASDAQ              | 67.8         | 61.3                          |
| $\text{BATS}$       | 18.8         | 15.7                          |
| ARCA-NYSE           | 43.4         | 38.3                          |
| $\text{NSE}$        | 0.0          | 0.0                           |
| $\text{FINRA}$      | 0.0          | 0.0                           |
| $\text{CSE}$        | 0.0          | 0.0                           |
| $\text{CBOE}$       | 1.2          | 0.7                           |
| $\text{EDGA}$       | 0.0          | 0.0                           |
| $\text{EDGX}$       | 34.5         | 41.0                          |
| $NASDAQ-BX$         | 0.0          | 0.0                           |
| $\text{NASDAQ-PSX}$ | 0.0          | 0.0                           |
| BATS-Y              | 4.5          | 0.0                           |

**Table 3.8** Percentage of Time that Exchange's Best prices are at the NBBO.

quote in another trading venue). Tables 3.9 and 3.10 look at trade executions in the different venues and compare the price at which the trade was executed relative to the best bid/ask price in the exchange in which the trade is reported (Local) and relative to the best available price across all venues we have reconstructed from the data (NBBO).

|                 |              | $\text{Local}$ |        |              | NBBO     |          |
|-----------------|--------------|----------------|--------|--------------|----------|----------|
| Exchange        | $\text{Bid}$ | Ask            | Total  | $\text{Bid}$ | Ask      | Total    |
| $\text{NASDAQ}$ | 22, 214      | 8, 122         | 30,336 | 458,994      | 367, 181 | 824, 675 |
| BATS            | 1,854        | 2,200          | 4,054  | 118, 205     | 108,407  | 225,512  |
| $ARCA-NYSE$     | 9,840        | 5,630          | 15,470 | 292, 933     | 273, 729 | 566, 361 |
| NSE             | 901          | 200            | 1, 101 | 13, 244      | 11,057   | 24, 301  |
| $\text{FINRA}$  | 0            | 0              | 0      | 534, 178     | 406,346  | 940, 424 |
| $\text{CSE}$    | 0            | 0              | 0      | 0            | 0        | 0        |
| $\text{CBOE}$   | 0            | $\cap$         | 0      | 5,005        | 1,550    | 6,555    |
| $\text{EDGA}$   | 0            | 100            | 100    | 31,357       | 22,125   | 53, 482  |
| $\text{EDGX}$   | 9,324        | 2,300          | 11,624 | 230, 187     | 207,005  | 436, 392 |
| $NASDAQ-BX$     | 1,016        | 1,100          | 2, 116 | 60,971       | 48, 365  | 109,336  |
| $NASDAQ-PSX$    | 0            | 100            | 100    | 600          | 1,525    | 2,125    |
| $\text{BATS-Y}$ | 100          | 1,000          | 1,100  | 16,519       | 16, 178  | 32, 497  |

Table 3.9 Number of Shares Executed at Best Prices (Local refers to best price at local exchange if local best price is not NBBO).

Table  $3.9$  compares for each venue, the executions that occurred at the best price across all venues (NBBO) versus the ones at the best price in that venue (Local), when that venue's best price was not the best across all venues. We can

| Exchange   | NBBO | Local Best | Inside Best | Outside Best | Shares (total) |
|------------|------|------------|-------------|--------------|----------------|
| NASDAQ     | 39.8 | 1.5        | 57.5        | 1.3          | 2,073,946      |
| BATS       | 34.8 | 0.6        | 64.2        | 0.4          | 648,137        |
| ARCA-NYSE  | 43.3 | 1.2        | 54.4        | 1.2          | 1,308,771      |
| NSE        | 33.1 | 1.5        | 64.3        | 1.1          | 73,486         |
| FINRA      | 22.2 | 0.0        | 71.5        | 6.4          | 4,238,247      |
| CSE        | 0.0  | 0.0        | 0.0         | 100.0        | 122,250        |
| CBOE       | 63.3 | 0.0        | 36.7        | 0.0          | 10,350         |
| EDGA       | 27.8 | 0.1        | 71.6        | 0.5          | 192,202        |
| EDGX       | 30.6 | 0.8        | 67.4        | 1.1          | 1,425,145      |
| NASDAQ-BX  | 41.1 | 0.8        | 55.5        | 3.4          | 266,166        |
| NASDAQ-PSX | 52.1 | 2.5        | 40.5        | 4.9          | 4,075          |
| BATS-Y     | 26.0 | 0.9        | 73.2        | 0.0          | 125,220        |

Table 3.10 Percentage of Shares Executed, by Execution Quality.

see that when trading against a best price, it occurs against the NEBO most of the time. In Table 3.10, we allow for further types of executions, not just against a best price, but also inside the (Local) spread (between the local best bid and ask, while not at the NEBO) and outside the spread (for FINRA and CSE we use the NEBO as reference because no Local bid/ask quotes are reported). The numbers clearly show that almost all trades occur at the computed NEBO or inside the (local) spread: 40 and 58 percent for NASDAQ respectively, 43 and 54 for NYSE-ARCA, 35 and 64 for BATS, and 30 and 67 percent for EDGE-X. The same percentages for trades reported to FINRA are 22 and 72 percent respectively using the NEBO as reference. These numbers suggest quite high execution quality, although the proportion of trades inside the spread seems unusually large if one takes into account that a regular market order should be executing at best prices. A possible explanation is that many of these trades are being executed against hidden orders posted inside the spread and/or via alternative order types which allow aggressive postings inside spread.

## 3. 7 Empirics of Pairs Trading

Most traders do not look at one asset at a time, but consider the interactions between different assets. This makes sense when you can extract information from the interaction between different assets. This works best with groups of assets that share common shocks and occurs naturally for assets in the same industry.

In this section we focus on the interaction between two technology stocks (Intel, INTC) and a technology ETF (Merrill Lynch Semiconductor ETF, SMH) on November 1, 2013. These two assets move together for two main reasons. The first is mechanical: around 20% of the ETF holdings are shares of INTC. The

second is economic: the ETF is designed to represent the semiconductor industry, and hence its price will move in response to news that affects that industry, and the same news will have a similar effect on the price of INTC. In Chapter 11, devoted to pairs trading and statistical arbitrage, we build on some of the ideas presented here to show how to take advantage of the information provided by a collection of assets. In particular, we present different trading algorithms based on the co-integration in the stock price level or in the drift component of a collection of assets that builds on the following empirical analysis.

Our analysis is based on the following theoretical model: we assume that both INTC and SMH are stocks whose dynamics have a transitory (mean-reverting) component and a permanent (Brownian) component. We express the dynamics of this process in vector form as follows:

$$d\mathbf{S}_{t} = \kappa \left(\boldsymbol{\theta} - \mathbf{S}_{t}\right)dt + \boldsymbol{\sigma}d\boldsymbol{W}_{t}, \qquad (3.4)$$

where�= aa', and Wt is a Brownian motion.

The presence of a mean-reverting component (the term proportional to dt) introduces the opportunity for generating positive expected returns from trading by exploiting that component's predictability. In this case, we use the joint information from the two processes to create a stronger trading signal by constructing a linear combination of the two assets, which is most strongly driven by the mean-reverting component (and which is the basis for the some of the algorithms of Chapter 11).

This is done by transforming the system in Equation (3.4), which has a generic matrix *K,,* into an equivalent system,

$$d\tilde{S}_{t} = \tilde{\kappa} \left( \tilde{\theta} - \tilde{S}_{t} \right) dt + \tilde{\sigma} dW_{t}, \qquad (3.5)$$

where *;:;,* is a diagonal matrix; that is, we look for the constants {an, 0'.12, a21, a22} such that

$$\tilde{S}_{t,1} = \alpha_{11} S_{t,1} + \alpha_{1,2} S_{t,2} \n\tilde{S}_{t,2} = \alpha_{21} S_{t,1} + \alpha_{2,2} S_{t,2} ,$$

and

$$\tilde{\boldsymbol{\kappa}} = \left[ \begin{array}{cc} \tilde{\kappa}_1 & 0 \ 0 & \tilde{\kappa}_2 \end{array} \right] \, .$$

The resulting r;, matrix has { K-1, K:2} equal to the eigenvalues of *K,,* and the process St,j corresponding to the largest of these (in absolute terms), max{IK-1 I, IK-2 I}, will have the strongest exposure to the mean-reverting process, and hence should contain the most trading-relevant information - i.e. it will generate the best trading signal (see the algorithms developed in Chapter 11).

We illustrate this by a simple estimation of the relationship between INTC and SMH during November 1, 2013. We sample using the midprice and estimate the process at regular intervals (every 5 seconds). We fit the discrete version of

|                                           |                | R                      |                       |
|-------------------------------------------|----------------|------------------------|-----------------------|
|                                           | A              | $\Delta S_{t-1, INTC}$ | $\Delta S_{t-1,SMH}$  |
| $\Delta S_{t,INTC}$<br>$\Delta S_{t,SMH}$ | 0.011<br>0.035 | ***<br>0.997<br>0.003  | 0.002<br>***<br>0.998 |

**Table 3.11** Estimated parameters of VAR (\*\*\* significant at 1% level).

the model in  $(3.4)$  and use it to compute the values of the transformed model in  $(3.5)$  in order to build the trading signal.

To estimate the discrete version of model  $(3.4)$  we estimate the vector autore- $\text{gressive process (VAR)}$ 

$$\Delta S_t = A + B \, \Delta S_{t-1} + \varepsilon_t \,$$

where  $S_t = [S_{t,INTC} \quad S_{t,SMH}]'$  are the asset prices, and  $\Delta S_{t,j}$  denotes the change in asset  $j - A$  is a vector of constants,  $B$  a matrix of constants and  $\varepsilon_t$  a vector of white noise. The resulting estimates are described in Table 3.11. From these we can recover the parameters of model  $(3.4)$ :

$$\boldsymbol{\kappa} = \frac{\mathbb{I} - \boldsymbol{B}}{\Delta t} = \begin{bmatrix} 0.003 & -0.002 \\ -0.003 & 0.002 \end{bmatrix}, \qquad \boldsymbol{\theta} = \boldsymbol{\kappa}^{-1} \boldsymbol{A} \,\Delta t = \begin{bmatrix} 24.30691 \\ 40.91387 \end{bmatrix},$$

and diagonalise  $\kappa$  to obtain  $\tilde{\kappa}$  and S:

$$\kappa = \boldsymbol{U} \cdot \boldsymbol{\Lambda} \cdot \boldsymbol{U}^{-1}, \qquad \tilde{\kappa} = \boldsymbol{\Lambda} = \begin{bmatrix} 0.0047 & 0 \\ 0 & 0.0007 \end{bmatrix},$$

$$\tilde{\bm{S}}_t = \bm{U}^{-1} \bm{S}_t = \begin{bmatrix} 0.682 & 0.547 \ -0.731 & 0.837 \end{bmatrix} \bm{S}_t.$$

![](_page_20_Figure_11.jpeg)

Figure 3.6 INTC and SMH on November 1, 2013: (left) midprice relative to mean midprice; (right) co-integration factor. The x-axis is time in terms of fractions of the trading day. The dashed line indicates the mean-reverting level; the dash-dotted lines indicate the 2 standard deviation bands.

|                                                                               | Constant                                  | $r_{t-1}$                                 |            | $r_{t-2}$                           |            |
|-------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|------------|-------------------------------------|------------|
| $r_{t,INTC}$<br>$r_{t,SMH}$<br>$r_{\tilde{S}_{t,1}}$<br>$r_{\tilde{S}_{t,2}}$ | $-0.000$<br>$-0.000$<br>0.000<br>$-0.000$ | $-0.011$<br>$-0.057$<br>$-0.195$<br>0.013 | ***<br>*** | 0.025<br>0.014<br>$-0.079$<br>0.044 | ***<br>*** |

**Table 3.12** Estimated parameters of individual AR(n),  $***$  significant at 1% level.

In Figure 3.6 we display the price process for the two assets in the left panel, and in the right panel the price process for  $\tilde{S}_1$ , which is called the co-integration factor. Visual inspection (not included here) suggests a much stronger meanreverting (auto-regressive component) for  $\tilde{S}_1$  than for  $\tilde{S}_2$ . We verify this by running autoregressions on the returns for all four price processes:  $r_{\text{INTC}}, r_{\text{SMH}}, r_{\tilde{S}}$ , and  $r_{\tilde{S}_2}$ . We can see the results in Table 3.12. For the assets, INTC and SMH, the coefficient on lagged returns is only significant for the ETF, SMH. After estimating the model and applying the diagonalisation on  $\kappa$ , the return on one of the resulting portfolios,  $S_1$  (the co-integration factor), has a coefficient on lagged returns that is almost four times larger than the one on SMH (and includes an additional significant coefficient on the returns two periods prior).

#### 3.8 Bibliography and Selected Readings

Hasbrouck (1991), Ait-Sahalia, Mykland & Zhang (2005), Bandi & Russell (2008), Barndorff-Nielsen & Shephard (2004), Engle (2000), Hansen & Lunde (2006), Mykland & Zhang (2012), Cartea & Karyampas (2012), Corsi & Renò (2012), Bandi & Renò (2012), Barndorff-Nielsen & Shephard (2006a), Barndorff-Nielsen & Shephard (2006b), Barndorff-Nielsen & Shephard (2004), Corsi (2009), Corsi, Pirino & Renò (2010), Aït-Sahalia et al. (2005), Cartea & Karyampas (2014), Hasbrouck (1995), Hasbrouck (1993), Bauwens & Hautsch (2006), Bauwens & Hautsch (2009), Cameron & Trivedi (2005), Ding, Hanna & Hendershott (2014).
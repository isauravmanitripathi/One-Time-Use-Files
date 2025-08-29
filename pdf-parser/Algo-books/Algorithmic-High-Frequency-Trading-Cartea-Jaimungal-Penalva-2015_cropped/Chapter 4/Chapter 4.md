# 4 Em pi rica I and Statistica I Evidence: Acti ity and Market Quality

This chapter continues our overview of empirical matters by looking at volume and market quality. As in the previous chapter we start by looking at daily volume though focusing on its relationship with volatility. We then move on to 'seasonal' patterns observed in the data, both in volume as well as in prices. Section 4.3 turns to market quality. These are variables that affect trade execution, such as spreads, volatility, depth, and price impact. Section 4.4 looks at message activity and the relationship between cancellations, executions and distance from the midprice. The chapter concludes with a look at hidden orders.

## **4.1 Daily Volume and Volatility**

So far we have seen that the price level (and the asset's returns) over the course of a whole day are difficult to predict and move with market forces. Over short horizons, these prices have fat tails, are subject to rapid changes (where the speed of change in price levels depends on the frequency with which the asset is traded), these changes tend to cluster in time, and are more likely than not to return to their previous level.

But trading activity, usually measured using volume ( either in number of shares or the value of shares traded) has a different dynamic structure that has important ramifications for the way we look at market data. Andersen & Bondarenko (2014) capture this idea very well:

Since volume and volatility are highly correlated and display strong time series persistence, any variable correlated with volatility will, inevitably, possess non-trivial forecast power for future volatility. This is true for bid-ask spreads, the quote intensity, the transaction count, the (normalized) trading volume ...

This and subsequent sections will consider the empirical aspects of some of these variables associated with volatility.

As a first step, we look at the relationship between volume and volatility using a robust regression for our four main assets (ISNS, FARO, MENT and AAPL) with daily volume as the dependent variable. As in subsection 3.1.4, we estimate two models using robust OLS. The left-hand side variable is the log of the number of shares traded on each trading day of 2013, log(l + Qt) (remember that we must add 1 to  $Q_t$  as for some assets, ISNS in particular, there are trading days with no trading and zero volume).

The variables on the right-hand side are the variables we used in the model for intraday returns. In particular, the first model (M1) includes a constant, the lagged values of the left-hand side variable (lagged volume), intraday returns on the VIX and the SPY, the contemporaneous intraday return of the asset, and OF which is the day's net order flow, on NASDAQ, defined as the volume of buy minus the volume of sell orders.

Hence, Model 1  $(M1)$  is

$$\log(1 + Q_{t,j}) = \alpha + \beta_{1,j} \log(1 + Q_{t-1,j}) + \beta_{2,j} \text{SPY}_t + \beta_{3,j} \text{VIX}_t + \beta_{4,j} r_{t,j} + \beta_{5,j} \text{OF}_t + \epsilon_j,$$

while Model 2  $(M2)$  is

$$\begin{split} \log(1 + Q_{t,j}) \\ &= \alpha + \beta_{1,j} \, \log(1 + Q_{t-1,j}) + \beta_{2,j} \, \text{SPY}_t + \beta_{3,j} \, \text{VIX}_t + \beta_{4,j} \, r_{t,j} + \beta_{5,j} \, \text{OF}_t \\ &+ \beta_{6,j} \, (\text{SPY}_t)^2 + \beta_{7,j} \, (\text{VIX}_t)^2 + \beta_{8,j} \, \text{HL}_t + \beta_{9,j} \, (r_t)^2 + \epsilon_j \,. \end{split}$$

In addition to the variables appearing in  $M1$ ,  $M2$  also includes

- $(SPY_t)^2$ : the squared value of the intraday return on the SPY ETF, as a proxy for market wide volatility,
- $(VIX_t)^2$ : the squared value of the intraday 'return' on the VIX, as a proxy for the volatility of volatility, or the variation in intraday changes in market sentiment,
- $\text{HL}_t$  (HL-volat): the asset's price range (max  $P_t \min P_t$ ) during the day, as a measure of the day's price volatility, and
- $r_t^2$ : the square of the asset's intraday return (another, distinct, measure of intraday volatility)

|                    |         | ISNS        |                          | FARO    | MENT                     |             |         | AAPL    |
|--------------------|---------|-------------|--------------------------|---------|--------------------------|-------------|---------|---------|
| Variables          | M1      | $\text{M2}$ | M1                       | M2      | M1                       | $\text{M2}$ | M1      | M2      |
| $\text{constant}$  | 6.47    | 5.40        | 4.88                     | 5.22    | 7.77                     | 7.70        | 5.46    | 9.66    |
| $\log 1 + Q_{t-1}$ | 0.22    | 0.22        | 0.58                     | 0.52    | 0.41                     | 0.39        | 0.67    | 0.38    |
| $SPY$ (%)          | 0.04    | 0.19        | $-0.17$                  | $-0.21$ | 0.03                     | 0.07        | 0.00    | 0.03    |
| $VIX$ (%)          | 0.02    | 0.02        | 0.00                     | $-0.01$ | 0.01                     | 0.02        | 0.00    | $-0.00$ |
| $r_t$              | $-0.01$ | $-0.03$     | 0.05                     | 0.04    | 0.06                     | 0.01        | 0.01    | $-0.01$ |
| Order Flow         | 0.02    | 0.04        | 0.00                     | $-0.00$ | $-0.01$                  | $-0.00$     | $-0.00$ | 0.00    |
| $\text{SPY}^2$     | $\sim$  | $-0.01$     | $\overline{\phantom{a}}$ | 0.09    | $\sim$                   | $-0.11$     | $\sim$  | $-0.03$ |
| $VIX^2$            | $\sim$  | 0.00        | $\sim$                   | $-0.00$ | $\overline{\phantom{a}}$ | 0.00        | $\sim$  | 0.00    |
| $\text{HL-volat}$  | $\sim$  | 0.32        | $\overline{\phantom{a}}$ | 0.10    | $\sim$                   | 0.20        | $\sim$  | 0.28    |
| $r_t^2$            |         | $-0.01$     | $\overline{ }$           | 0.01    | $\sim$                   | $-0.02$     |         | $-0.02$ |
| $\text{Adj R}$     | 0.03    | 0.18        | 0.30                     | 0.50    | 0.17                     | 0.24        | 0.38    | 0.65    |

|  | <b>Table 4.1</b> Robust OLS regression of intraday volume (Bold: $5\%$ significance) |  |
|--|--------------------------------------------------------------------------------------|--|
|--|--------------------------------------------------------------------------------------|--|

![](_page_2_Figure_1.jpeg)

The results in Table 4.1 display no evidence of significant effects from market variables (VIX or SPY) nor from order flow on volume. We also find no effect of the day's intraday return - FARO has a positive and significant effect in M1, but it disappears as we include better proxies for intraday volatility. What we find is substantial support for Andersen and Bondarenko's statement: volume seems to have significant time series persistence as evidenced by the common, positive and significant coefficient on last period's volume (M1 and M2 for all assets), and positive and significant 'correlation' with volatility, as measured by HL-volatility (in M2, all assets). Volatility, as measured by the square of the intraday return, seems statistically insignificant in the presence of HL-volatility.

#### 4.2 Intraday Activity

There are other well-known empirical patterns of intraday volume. Figure 4.1 shows the volume (number of shares traded in NASDAQ) at three different time scales over the course of a single trading day for AAPL. The top panel shows the results over the whole day when volume is aggregated in one-minute buckets (although the volumes for the first and last couple of minutes are off the scale). A striking characteristic for this day are the peaks at the beginning of the day and at the end of the day. There is a third peak around noon but (as we see

later) it represents a pattern that is specific to this trading day and is not a generic feature observed when trading in this asset.

A second striking feature is the large variability in volume. Computing the descriptive statistics on volume we find a mean of 6,898 shares, a standard deviation of 7,014, and quantiles Ql: 3,299, median: 5,349 and Q3: 8,039. The third and fourth moments give us a measure of skewness of 6.14 and kurtosis 60.83. All these confirm the impression that intraday volume has very large peaks of trading.

The peaks in volume observable at certain minutes, form a pattern that is repeated as one zooms into smaller time intervals. The bottom two pictures in Figure 4.1 look at the pattern of volume during a 30-minute and a one-minute window in the middle of the day. The left panel compares volume aggregated in ten-second buckets with their one-minute average (the thick line). We see substantial variation with large peaks of trading mixed in with periods of relative calm. Zooming in further, the pattern in the right panel is even more striking. For a single minute of the day, the grey columns identify volume aggregated to one second, while the large dots represent volume aggregated at 20 ms (which is almost equivalent to plotting individual transactions). Transactions seem randomly distributed over the minute, and it is not obvious whether the clustering of changes in prices we saw earlier (in subsection 3.3) is also taking place at this time scale. Transactions also appear to happen in multiples of 100 shares.

The fact that transactions occur at round quantities is an institutional feature. The market designers and regulators differentiate between 'odd', 'even', 'mixed' and 'round' lots. A round lot is a message or transaction involving units of even lots (an even lot is 100 shares). Odd lots are trades smaller than an even lot, and can be more expensive to trade (in terms of fees/commissions), while mixed lots are transactions which include both round and odd lots. Odd lots are sometimes aggregated and even not displayed on the consolidated tape (the public ticker that includes 'all' transactions from all exchanges). Also, trading in odd lots is subject to special rules which are in the process of being changed and reviewed (see for example SEC Release No. 34-71057 SEC (2013b), on the reporting of odd lots and changes in the definitions of "market" orders).

There are many algorithms which are based on or linked to volume. For example, some execution algorithms (see Chapters 6, 7 and 8) may require that MOs sent to the exchange do not exceed a percentage of what other market participants are trading at that point in time. In the same vein, some algorithms are designed to trade in a given direction, buy or sell the asset, whilst targeting a given percentage of the market - these are known as POV or percentage of volume algorithms. Moreover, volume plays a very important role in determining execution cost benchmarks. One of the most important of these is VWAP, which stands for volume weighted average price. We devote Chapter 9 to algorithms that target POV and VWAP where we also expand on the discussion of intraday volume to which we now turn.

![](_page_4_Figure_1.jpeg)

Figure 4.2 Volume as a function of the time of day.

#### 4.2.1 Intraday Volume Patterns

To gain insight into the intraday volume patterns, in Figure 4.2 we show heatmaps (left panels) of daily volume for the year 2013 for AAPL and MENT. The heat-maps are generated by first bucketing traded volume into five-minute windows throughout the day, for every day of the year. Then, for each five-minute bucket, we compute the distribution of volume. The heat-map is a visualisation of the collection of these distributions for each five-minute bucket all at once. In the figures we use coloured lines to represent the first and third quartiles, as well as the median.

We see that volume for AAPL is very large at the beginning of the day, and it gradually slows down until around 14:00, at which time there is a small surge in activity. The 14:00 surge slowly builds up and accelerates during the last half hour of the trading day, peaking at the close.

A reasonable hypothesis for the 14:00 surge is that at that time there are more announcements than is the norm, and these announcements tend to generate greater volume. For example, the monthly Treasury Budget is announced at that time of the day. Earlier we saw this figure for the day of July 30th. There we saw the usual peaks at the beginning and end of the day as well as a peak of trading volume around noon, which we can now show that is atypical for this asset.

To explain the peaks at the beginning and the end of the day, we need to hypothesise about the factors that drive volume. A common hypothesis in the literature, which is also made here, is that new information generates greater volume. In addition to the 14:00 surge, this would also explain why there is such a large volume at and just after the opening, as overnight news is gradually incorporated into prices during that time. But, this hypothesis does not explain the magnitude of the increase in volume at the end of the day, as there is not an unusually large number of announcements at that time. However, in Chapter 7 we will see another possible explanation for this peak in trading at the end of the day: traders who have not been able to meet their liquidation targets will accelerate trade execution as the market approaches its time to close. A second, not unrelated, possible explanation is that traders may prefer to postpone non urgent executions towards the end of the day when execution costs are lower (See for instance Section 4.3.5 where we discuss price impact, in particular Figure 4.11 where we show that the impact of orders (walking the LOB) is lower at the end of the trading day for INTC, and in Chapter 6 we show similar behaviour for SMH, see Figure 6.1). Finally, strategies that target volume (such as the ones developed in Chapter 9) will naturally exacerbate the increase in volume anticipated during this period.

The right panels of Figure 4.2 expand our analysis a bit further. They show a functional data analysis (FDA) approach to viewing the data. In these graphs for every trading day we regress the realised five-minute volume against Legendre polynomials and plot the resulting curve as a thin line in the figure. This generates a smooth volume curve for each day of the year. We then plot the mean of these curves ( the solid blue line) which represents the expected ( or average) trading volume throughout the day for the corresponding ticker. The conclusions that we drew about the behaviour of volume but we obtain additional insights.

In the right panels we observe four large outliers for AAPL - four curves that disappear off the bottom of the scale. These represent four special days for 2013. Three of these four were predictable while the other was not. The predictable three correspond to July 3 (Independence day), November 29 (Thanksgiving), and December 24 (Christmas) when NASDAQ closed early (13:00) for the holidays. These days are excluded from the calculations for MENT. The fourth outlier corresponds to August 22, 2013. On this day NASDAQ suffered major problems that led to a market shutdown for about three hours. So, in addition to identifying regularities in intraday trading patterns, the FDA curves have helped us identify outliers in the data. Outliers are very important when using historical data for analysis, backtesting, and designing algorithms. Quite often, an outlier will have a disproportionate effect on an algorithm's profitability, whether when backtesting it against historical events or running it live in the market. Thus, it is crucial to keep track of these outliers and account for them in the design and evaluation of algorithms. In our historical analysis of the intraday pattern of volume, AAPL's mean daily volume function drawn in the right panels is lower

![](_page_6_Figure_1.jpeg)

Figure 4.3 Trading pattern within a second.

than it would have been if we had not included those four particular dates in the estimation.

In order to contrast the intraday behaviour of AAPL with that of a less frequently traded asset, Figure 4.2 displays the same analysis for MENT. We observe that the daily peaks at the beginning and the end of the day are also there, though slightly modified, and distorted by the discreteness of trading lots. For MENT, the initial burst of trading is not as frequent as with AAPL. As we can discern from the pictures on the right, there are a substantial number of days for which trading starts unusually slowly. These slow days balance out the bursts of trading from other days, so that on average volume in early trading does not seem to differ substantially from that during the rest of the day. It is at the end of the day that we see a substantial amount of trading activity in MENT.

We have omitted ISNS and FARO from this analysis, as the frequency of trading for those assets is even lower than for MENT, and thus there are many more zero-volume observations. The resulting figures are qualitatively similar, although there is a lot more noise in the estimation, and a much larger number of zero trading intervals.

#### 4.2.2 Intrasecond Volume Patterns

When working at time intervals much finer than a second, a natural question to ask is whether we observe time patterns at such small intervals, like the ones we found over the duration of the day. Focusing only on AAPL we look at the millisecond trading pattern, that is, for each transaction we look at the millisecond in which it occurred. In Figure 4.3 we display the average number of transactions at each millisecond for each day in 2013 (AAPL), as well as the quartiles  $(Q1, median and Q3)$  for the daily means for each millisecond (the quartiles have been smoothed using moving averages).<sup>1</sup>

We see that there is hardly a persistent pattern at the millisecond level, although an initial spike is observable at the 000-020 ms range, followed by a subtle

 $1$  To improve the visual presentation the 10 highest realisations in the year have been removed from the figure.

![](_page_7_Figure_1.jpeg)

**Figure 4.4** Cumulative distribution function of transaction count for specific milliseconds.

valley that ends around the 100 ms point. To explore this in more detail, in Figure 4.4 we identify the empirical cumulative distribution function of the number of transactions ending at six different milliseconds: three early ones (at 4, 5, and 6 milliseconds), and three later ones (at 104, 105, and 106 ms). From the figure we can see that the early milliseconds stochastically dominate the other three. (The choice of 104-106 is arbitrary and the same pattern is observed if we choose other milliseconds to compare with what happens at 4, 5, and 6 - sometimes even more starkly.)

This pattern suggests that there is an unusual number of transactions that are recorded just after the exact beginning of a second. A plausible explanation is that there may be an unusual number of transactions that are entered ( automatically) at the exact end/beginning of a second and what we observe is the latency or clock-asynchronicity of these orders (machines).

#### 4.2.3 Price Patterns

It is quite standard to look at volume patterns, but not price patterns. In this section we ask whether executions at prices that end in multiples of 5 cents (round values) are different from those that do not. There is no strong fundamental reason why the price of an asset, which in theory represents a fraction of the income for shareholders generated by a firm, should have a round value, such as \$450.25 or \$21.00. However, if we look at the frequency with which we observe transactions taking place at different prices grouped by the number of cents in the price, we find the pattern displayed in Figure 4.5.<sup>2</sup>The figure also shows the quartiles Ql, median and Q3 as solid lines.

The patterns are quite evident. There is a very large accumulation of transactions whose prices end in exact dollar-valued prices, a large number of transactions with prices that end in 50 cents, and spikes of larger than usual numbers of transactions at prices that end in units of 10 cents, and even 5 cents ( these differences are for the most part statistically significant).

2 To improve the visual presentation the 10 highest realisations in the year have been removed from the picture and the quartile estimation (10 out of 98,280).

![](_page_8_Figure_1.jpeg)

![](_page_8_Figure_2.jpeg)

There is a quite straightforward interpretation for this phenomenon, which is that for some reason (rational or not) there is a preference for providing liquidity at prices that end in round cent values. We use the term 'preference for providing liquidity', as transaction prices are (mostly) determined by an aggressive MO filling a standing posted LO, so it is liquidity providers who decide to accept a larger number of executions at a particular price level.

Why would agents provide liquidity in this way? We can hypothesise that there are a number of stop-loss orders and momentum orders programmed to execute as MOs at round prices. These could be latent, having been programmed by agents who decide to enter/exit when the price moves beyond a certain barrier, which is psychologically or conveniently set at a whole number. This type of reasoning is consistent with chartist ideas such as 'price supports' and 'price ceilings'. If the above reasoning is correct, then the accumulation of executions at those prices may be triggered by psychologically-based demand for liquidity which is then happily provided by agents who do not have such psychological inclinations and expect the unusual demand for liquidity at these prices to be unjustified by economic/market microstructure fundamentals (and hence, a source of profit).

## **4.3 Trading and Market Quality**

Financial markets play a key role in helping a market economy to allocate resources over time and uncertainty. Financial markets provide a forum for firms to raise capital, and facilitate investor participation in the general economic progress of the economy. In this context, the stock market provides a forum where equity holders can convert their equity into cash (and vice versa) quickly and at a reasonable price. In this section we look at different ways of measuring the market's effectiveness in this role under the generic heading of 'market quality'.

In subsection 4.2.1 we used two basic arguments to explain intraday patterns: that new information increases trading volume, and that an increased desire to trade ( e.g. due to increased trader urgency) interacts with the quality of the mar-

ket which feeds back to motivate further trading. Market quality enters directly into the second argument: an expected increase in volume generates expectations of better market quality, that is of improved effectiveness of the market in facilitating trade via lower execution costs (spreads), greater price efficiency (less mean-reversion in price levels or lower transitory volatility), etc., which induces greater volume. In the first argument, market quality enters indirectly, as it modulates the relationship between the exogenous forces of new information and traders' desire to execute trades. Either way, if the quality of the market varies, trading activity will vary with it.

So what determines market quality? What determines the effectiveness of the market in facilitating trade? Naturally, the direct cost of trading matters: how much does one pay for shares one wishes to buy; what is the price one pays relative to one's opinion of its market value; how much does one value the information obtained from the market, and how easy is it to complete a transaction? Think of a medieval cattle market. Suppose one lives on a farm which is equidistant from two towns that hold their weekly cattle market on the same day of the month. How does one choose between them? One will probably go to the market that is most likely to offer the best price, and which can be obtained after an easy sale process, and with the best guarantees that the transaction is finalised and one can walk away with the money. In a financial market, where agents are buying and selling, these dimensions along which to evaluate the quality of a market are: having sufficient information to identify the true market value of the asset, being able to buy ( or sell) any quantity at prices sufficiently close to the asset's value, and having the confidence that the deals are honoured. Of course, one may have qualms about the existence of such a thing as 'the true market price' of an asset, but regardless, it is a useful concept to work with and is the basis of much of the literature. If one does not believe there is or can ever be such a thing as the true market price, the concept is still useful as a theorectical construct in the study of market microstructure, in the same way as the concept of an ideal gas is useful in physics.

From our short list of dimensions of market quality, the last one (honouring of deals) is usually taken for granted, although when prices suffer large fluctuations we do see some transactions being cancelled by the exchange ( usually because they occur at 'ridiculous' prices). The other two issues are captured by measures of market quality such as spreads, price impact, volatility, resilience, depth, probability of informed trading (referred to as PIN), etc. Spreads measure the immediate cost of executing a trade aggressively; price impact measures the cost of executing larger trades via their impact of trading on prices; volatility measures the effectiveness of the price in transmitting information about the market value of an asset; resilience is related to market impact and measures the market's ability to return to equilibrium after a trade; depth measures the amount of visible liquidity in the market, and PIN measures the degree of information asymmetry in the market and hence, like volatility, the ability of the market

to transmit information about the market value of an asset. We now look at spreads, volatility, depth and price impact.

#### 4.3.1 Spreads

Spreads measure the execution costs of small transactions by measuring how close the price of a trade is to the market price. The first problem, naturally, is to determine what is the 'true market price'. The simplest, and most common approach, is to use the midprice,

$$S_t = \frac{1}{2}(a_t + b_t), \qquad (4.1)$$

the simple average of the bid (b<sup>t</sup> ) and the ask (a<sup>t</sup> ) price. This reference is based on the economic concept that the market price is the equilibrium price, the price at which demand equals supply, and in a market with frictions that generate a gap between the best buy price (the ask) and the best sell price (the bid), the equilibrium should lie somewhere in between. The midprice is the simplest way to estimate this market price, although, as we saw in Chapter 2, the spread may arise for different reasons ( compensation for inventory risk, or adverse selection from trading against more informed traders) and in some cases the 'true price' may be closer to the bid or the ask.

We saw an alternative estimate of the market price earlier as well, the microprice defined in (3.3). This seems more meaningful economically (and to develop algorithmic trading strategies) as it incorporates the quantities offered to sell and buy at the bid and ask (respectively) to weigh the bid and ask prices, and which may better reflect some of the microstructure issues described above. There are other, more sophisticated models that try to estimate the equilibrium price, e.g. by separating movements in the midprice into a temporary and a permanent component (the permanent being the equilibrium price), but we do not treat them here.

The two most common spread measures are the quoted and the effective spread, both of which use the midprice as the market price. The quoted spread, QS, is the difference between the ask and the bid prices,

$$\mathrm{QS}_t = a_t - b_t,$$

and represents the potential cost of immediacy: the difference in price between posting an LO at the best price and aggressively executing an MO (and hence 'crossing the spread') at any point in time. It also reflects distance from the market price, if one takes the midprice as reference. The direct trading cost of a market sell order would be St - bt = QStf 2, while that of a market buy order would be at - S<sup>t</sup> = QSt/2 (the quoted half-spread).

In contrast, the effective (half-)spread, ES, measures the realised difference between the price paid and the midprice, which for a market buy order is

$$\mathrm{ES}_t = a_t - S_t \,,$$

while for a market sell order it is

$$\mathrm{ES}_t = S_t - b_t \, .$$

For an MO executed in full on an exchange against a visible LO, the effective spread is equal to the quoted halfspread (if it does not walk the LOB). Sometimes it will be greater, if it does walk the LOB, or smaller, if it is matched with a hidden order inside the spread - it could even be negative, if the hidden order was aggressively posted. ewe saw hidden orders in the context of different order types in subsection 1.3.4 and we will discuss this further in subsection 4.5 - a hidden order is an LO that is posted in the LOB but is not visible to market participants.) A negative effective spread reflects that one is buying at a price below or selling at a price above the 'market price' (represented by the midprice). In empirical analysis, these spreads are usually normalised and expressed in bps relative to the midprice.

In Table 4.2 we look at the quoted spread for our four assets during 2013 ( ordered from least to most traded). For each asset we compute the time-weighted average quoted spread, tQS, for each minute of the day. This is calculated as follows: for each minute of the day, t = 1 : 390, while the market is open (from 9:30-16:00),

$$\text{tQS}_{t} = \sum_{i=1}^{n-1} (\tau_{i+1} - \tau_i) \text{QS}_{t_i},$$

where *i* E {l, ... ,n} indexes the time (in minutes) at which the quoted spread changes during minute *t,* Ti· Table 4.2 describes the statistics for the minutes of every day in 2013 (252 trading days), for each asset.

| Asset | Mean | StdDev | POI | Ql   | Median | Q3   | P99   |
|-------|------|--------|-----|------|--------|------|-------|
| ISNS  | 33.2 | 270.8  | 2.0 | 11.0 | 22.0   | 40.0 | 129.2 |
| FARO  | 23.9 | 192.0  | 2.4 | 8.9  | 12.0   | 16.6 | 71.0  |
| MENT  | 3.5  | 27.4   | 1.0 | 1.0  | 1.1    | 2.0  | 13.9  |
| AAPL  | 13.6 | 54.7   | 5.4 | 11.0 | 13.8   | 16.9 | 29.3  |

**Table 4.2** Time-average Quoted Spread (in cents).

The descriptive statistics of the resulting sample are provided in Table 4.2. The first thing to note is that the data on the table suggest that more frequently traded assets trade at lower spreads. This positive relationship between volume and market quality can work both ways: volume attracts liquidity and improves market quality, or higher market quality facilitates trade and generates greater volume.

Nevertheless, AAPL seems to have an enormous spread. But, recalling the discussion on tick size earlier, the large spread for AAPL is an illusion as we have not adjusted for the relative tick size. The average mid prices ( at the end of each minute) for our assets are: ISNS \$5.25, FARO \$40.62, MENT \$19.93, and AAPL \$473.00. This implies that the median quoted spreads are: for ISNS 419bps, FARO 29.5bps, MENT 5.5bps and AAPL 2.9bps. By evaluating spreads relative to the midprice we recover the expected relationship between quoted spreads and volume.

Also from Table 4.2 we can compute the interquartile range (as a percentage of the median). From these calculations we find that more frequently traded assets tend to have less volatile quoted spreads (the numbers arc: 1.32bps for ISNS, 0.64bps for FARO, 0.91bps for MENT, and 0.42bps for AAPL).

The MENT example illustrates another aspect of the importance of tick sizes which is of great interest, especially to regulators. In the US (for assets with prices greater than one dollar), the minimum tick size is legally fixed at one cent there are ways to trade in fractions of a cent but the one cent minimum is binding in most cases. Imposing a minimum tick size of one cent may affect trading for some assets, such as MENT. From Table 4.2 we can see that for almost 50 percent of all minutes, the one cent minimum is constraining MENT's quoted spread at that level ( one cent). This translates to a possibly significantly large relative minimum quoted spread ( around 5bps for MENT) and may be limiting the market quality for this asset.

A final comment on Table 4.2: the numbers in this table are contaminated by an event we mentioned earlier, in subsection 4.2.1, namely that the data is not corrected for trading stops, and in particular for the trading halt during August 22nd. We do not include the corrected table as they are not significantly different and so it is not necessary, but only because our data set includes all the minutes in 2013, almost 100,000 observations per asset, so the overall effect on the statistical aggregates is very small. Nevertheless, we wanted to take this opportunity to point out the importance of knowing the details of your dataset. In the ITCH dataset, all messages are recorded and timestamped, *even when the market is halted and there is no trading.* We mentioned earlier how on August 22nd the NASDAQ halted trading for three hours. During that time, messages kept coming into the exchange and were time-stamped. In particular, many orders were cancelled and the 'ask' and 'bid' moved dramatically. As trading was suspended, these fluctuations led to huge and also negative *art�ficial* spreads, and they contaminate the data in Table 4.2 (primarily the mean and standard deviation, although the effect is small). If we wanted to use our analysis for trading or designing an algorithm, especially if it involves unsupervised/ deep learning, the unfiltered data could generate significant distortions.

We have also computed the effective (half-)spreads. In order to obtain numbers that are comparable to those in Table 4.2 we doubled the effective spreads and included them in Table 4.3. Again we have constructed one-minute buckets, and for each, we have computed the quantity-weighted effective spreads, qES, for our four assets:

| Asset | Mean  | StdDev | POI    | Ql   | Median | Q3    | P99   |
|-------|-------|--------|--------|------|--------|-------|-------|
| ISNS  | 12.56 | 45.00  | -42.00 | 3.50 | 9.23   | 19.00 | 65.00 |
| FARO  | 7.63  | 8.61   | -10.00 | 3.33 | 6.50   | 10.76 | 32.84 |
| MENT  | 1.23  | 1.57   | 0.00   | 1.00 | 1.00   | 1.03  | 5.38  |
| AAPL  | 9.32  | 3.85   | 2.67   | 6.61 | 8.83   | 11.47 | 20.20 |

**Table 4.3** Quantity-weighted Effective spread (in cents).

$$\text{qES}_t = \sum_{j=1}^m \frac{q_j}{\sum_{s=1}^m q_s} \text{ES}_j$$

where *j* **E** {1, ... , m} indexes the trades that took place during minute *t,* qj denotes the number of shares in trade *j,* and ESj is the effective spread for trade *j.* 

Effective spreads differ from quoted spreads in several ways. Earlier we saw that the effective spread is equal to the quoted halfspread when a trade executes against a visible LO and does not walk the LOB. In our dataset, trades are recorded via the execution of the posted LO, so we do not have information on the MO that was sent to the market. This implies that none of our executions walk the LOB. This biases our measure of the ES downwards, but the bias is small, as we see very few executions of LOs away from the bid/ ask during previous milliseconds (a necessary condition for an MO to walk the LOB at NASDAQ, as the remaining quantity may need rerouting in search of best execution in all markets). Another reason why this bias is small, is that in the fragmented US market, when an MO comes into a market and it is greater than the depth at the bid/ask, the part that is not executed is usually routed to other markets, and only under very special circumstances will it literally walk the LOB. Note, that in general this rerouting makes it virtually impossible to reconstruct the quantity of a large incoming MO without specific information from the agent who sent it.

Thus, our measured ES has to be equal to or lower than the (current) quoted spread. A visible trade will generate ES = QS/2. As not all posted LOs are visible, some trades will be executed at prices better than the bid/ask. This will generate an ES that is strictly smaller than the QS, and may even produce a *negative* ES. One obtains a negative effective spread if an incoming market buy (sell) order meets a hidden sell (buy) order that is below (above) the midprice. That this occurs is evident by looking at the first percertile of the empirical distribution for ES (the POl (first percentile) statistic in Table 4.3).

There is another difference between ES and QS, namely that ES can only be measured when there is a trade, while quoted spreads are always observable. Therefore, it may be possible that quoted spreads differ from effective spreads if market conditions around trades are systematically different from those without

![](_page_14_Figure_1.jpeg)

![](_page_14_Figure_2.jpeg)

trades. Looking at the interquartile range and the standard deviations of ES and  $QS$  in Tables 4.2 and 4.3 we find that  $ES$  is less volatile than  $QS$ . This would happen if executions tend to be concentrated around times of narrow quoted spreads, something we explore in more detail in subsection 4.4.

We have seen that assets with greater trading frequency have better market quality in the sense that execution costs for small trades (the quoted spread) is smaller. If we look at the intraday pattern of trades we find further evidence that lower execution costs occur when trading is high (as anticipated by the theoretical discussions in Chapter 2, where we saw that if the number of informed traders stays constant and the number of uninformed traders increases, the spread shrinks). In Figure 4.6 we plot the one-minute time-averaged quoted spreads for AAPL in 2013, as well as the first quartile, median and third quartile. As the figure shows, quoted spreads are initially high, decline rapidly during the first half-hour of trading, and are mostly constant throughout the remainder of the day until the last (half) hour of trading, when the spread rapidly declines. This pattern in quoted spreads is also seen in the effective spread. Recall that in Figure 4.2 we saw that the afternoon is associated with increased trading, and hence we find, as hypothesised, that during a period with a constant flow of information more trading and lower spreads occur together.

This connection between trading volume and spreads fails during the morning where the situation is completely reversed: declining volumes go hand-in-hand with declining spreads. This can be explained by appealing to the other factor affecting volume which we discussed earlier, namely information. When the market opens, and during the subsequent hour of trading, the market absorbs all the information that has accumulated since the last market close. This would explain the heavier trading. But a lot of new information is also associated with a great deal of uncertainty. Theoretically, as we saw in Chapter 2, in the presence of greater uncertainty it is optimal to post wider bid-ask spreads, and in the market making algorithms developed in Chapter 10, see for example Section  $10.3$ , we show that greater price uncertainty increases the depths of the quotes that a risk-averse market makers sends to the LOB. Thus, more information at

the beginning of the day explains the coincidence of wider spreads with greater volume.

#### 4.3.2 Volatility

vVe now consider another dimension of market quality, namely volatility. Volatility measures price fluctuations and represents a cost (i.e. low market quality) in the sense that a rapidly changing price makes it difficult to determine the actual market price of the asset. Of course, one may observe price changes because the true market value of the asset is changing, and hence the literature differentiates between fundamental volatility and microstructure noise. The first captures the fluctuations in the true market price, while microstructure noise represents extraneous fluctuations due to the way the market operates. There is a large (and growing) number of measures of raw volatility (unconditional volatility which does not distinguish fundamental volatility from microstructure noise) and of microstructure volatility.

For simplicity we use the term volatility to refer to raw volatility, and we measure the volatility of asset returns, rather than of asset prices. We have seen several measures of volatility when studying the relationship between volume and volatility in Section 4.1. The simplest such measure is the realised volatility: the standard deviation of a sample of returns. We have seen volatility measured using the square ( or the absolute value) of the return � this is useful if you have very few observations and you are working in a sufficiently small time scale so that the mean return can be safely assumed to be (essentially) equal to zero. Another common alternative is to use the range of the return ( or price): e.g. by taking the difference between the maximum (max) and minimum (min) values of the price over a certain interval and normalising it by either the minimum value, the mean/median, the initial value, or the average of the min and the max. Here we look at realised volatility, the range of returns, and the number of times the bid or the ask changes.

| Asset        | Mean       | StdDev      | POl        | Ql         | Median     | Q3          | pgg          |
|--------------|------------|-------------|------------|------------|------------|-------------|--------------|
| ISNS         | 16.6       | 54.8        | 0.0        | 0.0        | 0.0        | 14.4        | 160.3        |
| FARO<br>MENT | 8.3<br>5.6 | 12.7<br>6.6 | 0.0<br>0.0 | 3.8<br>3.2 | 6.6<br>4.6 | 10.3<br>6.5 | 31.3<br>20.1 |
| AAPL         | 5.5        | 4.2         | 1.0        | 3.3        | 4.7        | 6.7         | 18.1         |

**Table 4.4** Realised one-min volatility (15 min samples).

Table 4.4 displays the statistical properties of realised volatility measured as *O"t,* the standard deviation of one-minute returns over fifteen minute periods (for every day in 2013), that is, for every 15-minute period (each 15-minute period indexed by *t)* ,

$$\sigma_t^2 = \sum_{j=1}^{15} \left( r_j - \frac{1}{15} \sum_{s=1}^{15} r_s \right)^2,$$

where *j* E {1, ... , 15} is the index for each of the individual minutes within the 15 minute period (t), and *rj* is the realised return for minute *j* int. What we observe as we go from AAPL to ISNS in Table 4.4 is that the more frequently traded asset also has a higher mean volatility.

| Asset                        | Mean                         | StdDev                       | POl                              | Ql                           | Median                       | Q3                           | P99                             |
|------------------------------|------------------------------|------------------------------|----------------------------------|------------------------------|------------------------------|------------------------------|---------------------------------|
| ISNS<br>FARO<br>MENT<br>AAPL | 0.10<br>3.77<br>3.00<br>6.23 | 1.37<br>2.33<br>3.47<br>2.85 | 0.00<br>1.<br>10<br>0.00<br>3.72 | 0.00<br>2.50<br>0.00<br>4.72 | 0.00<br>2.84<br>2.18<br>5.28 | 0.00<br>4.26<br>5.04<br>6.45 | 0.00<br>12.05<br>12.84<br>19.47 |

|  | Table 4.5 Interquartile Range of one-minute returns. |  |  |  |
|--|------------------------------------------------------|--|--|--|
|--|------------------------------------------------------|--|--|--|

Table 4.5 displays an alternative way to look at the same idea, only now we are looking at the statistical properties of a different variable, sampled over smaller time intervals. In Table 4.5 we include the statistics for the interquartile range of one-minute returns. That is, for AAPL, 5.28bps is the median of 25 2 observations, one for each trading day, of the interquartile range observed for the one-minute returns during that day.

Because the sampling method is distinct we observe some interesting differences. ISNS displays a zero interquartile range for most days. This is natural, as it is an asset that displays very few price movements - the median realised 15-minute volatility is zero as we saw in Table 4.4. By focusing on the median interquartile range for each day, this sampling method misses the very large but relatively rare price movements that are responsible for the high volatility numbers for ISNS in Table 4.4.

A different effect is responsible for the differences between MENT and FARO. Despite MENT having similar trading activity than FARO, it has lower volatility. MENT has more than 25% of days with an interquartile range equal to zero, but it also has lower realised one-minute volatility. The difference between MENT and FARO has probably much more to do with MENT's relative tick size. As we saw above when looking at the quoted spread, the one cent tick size is a binding constraint for MENT most of the time. This leads to an unusual degree of price stickiness, as many small price movements are not sufficient to push the bid or ask a whole cent (5 bps) away from their current levels. Thus, despite having similar activity levels as FARO, its price displays lower volatility.

In subsection 3.5 we looked at the non-Markovian nature of price changes. We found that there is a significant tendency (at least for AAPL on July 3 0th, 2013) for price movements to reverse themselves. Thus, looking at the volatility of

| Asset | Mean | StdDev | POl | Ql | Median | Q3  | P99 |
|-------|------|--------|-----|----|--------|-----|-----|
| ISNS  | 2    | 29     | 0   | 0  | 0      | 0   | 16  |
| FARO  | 11   | 25     | 0   | 0  | 3      | 13  | 100 |
| MENT  | 6    | 18     | 0   | 0  | 2      | 7   | 75  |
| AAPL  | 150  | 149    | 7   | 64 | 109    | 185 | 709 |

**Table 4.6** Number of Changes in the ask or bid.

one-minute returns misses many such price movements. To account for all price changes, we construct yet another measure of volatility: we count the number of changes in the bid and ask within a one-minute period, and report the statistics in Table 4.6.

We find that the less frequently traded assets (ISNS, FARO and MENT) also have more stable prices (bid and ask) - at least 25 percent of the time we see no price changes at all. For ISNS this is even more marked, as it happens at least 75 percent of the time. Nevertheless, the average is 2 per minute, suggesting that price changes occur infrequently but when they do, there are a lot of them. For MENT and FARO we see more price movements than for ISNS which is consistent with what we found earlier. MENT sees fewer price changes than FARO even though there is more trading in the former stock, but this is linked · to the issue of minimum tick size discussed above.

The statistics in Table 4.6 indicate that AAPL displays almost two orders of magnitude more price changes than MENT or FARO. However, the realised volatility of its return is lower than that of FARO and similar to that of MENT (in Table 4.4). We interpret this as reflecting the interaction of small relative tick size and large frequency of trading. A one cent price change for AAPL (with an average price of around \$500 in 2013) is 0.2 bps. An asset with such a small relative tick size and with such a large trading activity is bound to have a price level that is very sensitive ( and hence generates many changes in the bid/ ask within a minute), but most of the resulting changes will be rapidly reversed ( as we saw in Tables 3.5 and 3.6), generating relatively low realised volatility (Table 4.4).

To conclude our discussion of volatility, in Figure 4. 7 we look at how volatility (in terms of the interquartile range of one-minute returns) changes over the course of one trading day. The figure uses dots to displays the interquartile range for each minute of the day, estimated using all trading days in 2013 (390 observations - one per minute). The lines represent fitted quartic curves. The blue line is fitted with standard OLS while the red line is fitted using robust OLS, which controls for outliers by reducing the weight of the more extreme observations at the beginning and the end of the day.

Comparing the intraday volatility pattern in Figure 4. 7 to the intraday volume pattern in Figure 4.2, we see a common pattern: high at the beginning of the

![](_page_18_Figure_1.jpeg)

**Figure 4.7** Intraday volatility: interquartile range for one-minute returns.

day, lower as the day progresses until it reaches a plateau between noon and 15:00, followed by an increase until market close. While Figure 4.7 shows a large left-slanted smile for the volatility pattern, Figure 4.2 shows a more symmetric volume smile and, if anything, slanted to the right. This is consistent with trading at the beginning of the day being subject to more uncertainty and also being more informationally driven, while trading at the end of the day is driven less by information, and possibly more by traders rushing to close their positions.

#### 433 Market Depth and Trade Size

| $\text{Asset}$ | $\text{Mean}$ | $\text{StdDev} \quad \text{P01}$ |     | Ο1  | $\text{Median}$ | $\Omega 3$ | P99   |
|----------------|---------------|----------------------------------|-----|-----|-----------------|------------|-------|
| ISNS           | 619           | 787                              | 51  | 150 | 300             | 750        | 3.250 |
| FARO           | 142           | 125                              | 14  | 86  | 122             | 171        | 484   |
| MENT           | 661           | 694                              | 117 | 351 | 527             | 784        | 2.852 |
| AAPL           | 189           | 169                              | 64  | 127 | 161             | 210        | 662   |

**Table 4.7** Average Depth at the Bid and Ask (number of shares).

Market quality is not just about the informational content of prices or the cost of executing a small order, it is also about depth. By depth, we mean the volume posted in the LOB and available for immediate execution. In this section we focus mostly on the volume at-the-touch, that is at the bid and ask price levels. Mutual and pension funds manage a large fraction of people's wealth and they need markets to adjust their positions, pay their investors, and evaluate their performance. These funds move large quantities of shares. In any one day a fund may want to buy or sell thousands, tens of thousands, or even more shares of any one company. Table 4.7 illustrates how unreasonable it is to think that the market will match those trades at the published bid/ask prices. The table shows the distribution of the one-minute time-weighted average of the quantity of shares available at the ask and bid on NASDAQ for every day in 2013. This number does not exceed  $1,000$  shares in  $75\%$  of cases for any one of the four

![](_page_19_Figure_1.jpeg)

Figure 4.8 Average monthly trade size, AAPL 2000-2013.

assets (not even  $\text{AAPL}$ ). Recall (see Table 3.1) that in 2013,  $\text{NASDAQ}$  intraday trading represents around 22 percent of total volume.

Depth and trade size are not independent of one another; the decision of how much to trade depends on the expected availability of shares resting as LOs for immediate execution, and similarly, the decision of how much to offer will depend on the expected flow of incoming MOs. If the depth is thin (few orders resting in the LOB), MOs will be small – which implies that in thin markets, relatively urgent large orders that would walk the LOB need to be broken up into smaller MOs which are then sequentially executed over a period of time.

The institutional, legal, technological and economic changes of the last 15 years have produced a steady decline of the average trade size (the number of shares in a single trade). We can see this for AAPL in Figure 4.8 which displays the monthly average trade size, computed from  $CRSP$  data – the dots are the monthly averages and the dark line is a smoothed representation (a moving average). It shows a sharp increase in the early  $2000s$  to a peak of around  $1,300$ shares per trade, and a steady decline to around  $200$  shares by the end of  $2013$ . (Nowadays, with the 7:1 split, the numbers should be different, though a similar pattern is observable in most stocks.) Table 4.8 gives the statistics on NASDAQ trade sizes (total number of shares traded,  $Q$ , divided by the number of trades,  $n$ ) for 2013. As can be seen there, trade sizes in AAPL are smaller than for the other three assets, though not substantially so.

| $\text{Asset}$ |       | $Mean \t StdDev \t P01$ |      | $\text{O1}$ | $\text{Median}$ | $\text{O3}$ | P99    |
|----------------|-------|-------------------------|------|-------------|-----------------|-------------|--------|
| ISNS           | 206.2 | 348.7                   | 1.0  | 100.0       | 100.0           | 200.0       | 1600.0 |
| FARO           | 99.8  | 76.4                    | 1.0  | 64.0        | 100.0           | 100.3       | 374.8  |
| MENT           | 199.9 | 172.9                   | 60   | 100.0       | 150.0           | 240.3       | 867.1  |
| AAPL           | 121.1 | 40.5                    | 52.2 | 95.7        | 115.4           | 139.0       | 252.8  |

**Table 4.8** Average Size of a Trade  $(Q/n)$ .

When developing algorithms that provide liquidity to the market, the depth, captured by the shape of the LOB, is critical because this dictates where a trader

![](_page_20_Figure_1.jpeg)

**Figure 4.9** lntraday depth: (log) average quantity of shares posted at the bid and at the ask.

should post her LOs. We already discussed a simple model of market making in Section 2.1.4, and in subsequent chapters we develop these ideas further in the context of optimising market making and optimal execution algorithms. For instance, Chapter 8 looks at optimal execution (buying or selling large positions) when the agent employs LOs and possibly also MOs. In Chapter 10 the shape of the LOB plays a critical role in the optimal posting of liquidity for a market maker, and we consider how different assumptions about the shape of the book affect the optimal posting strategy.

To close this discussion we look at the intraday patterns of depth in Figure 4.9. This figure shows the intraday pattern of the average quantity of shares posted at the bid and ask every minute of 2013. As expected, there is the usual sharp increase at the end of the trading day. This is consistent with greater market quality in the form of narrower spreads (as seen earlier, in Figure 4.6) and the increased desire of traders to close positions at the end of the day. Somewhat, though only marginally, surprising is that depth is also higher at the beginning of the day, where we hypothesised that high price uncertainty leads to wider spreads. The figure suggests that the theoretical trade-off between the benefits of market making from increased order arrival and the cost from higher uncertainty discussed in subsection 2.1.1 is resolved in practice in favour of providing greater liquidity.

#### 4.3.4 Price Impact

A main concern for participants that wish to execute a large order is that the order will have an adverse price impact: increasing the price when buying aggressively and lowering it when selling. There are several variables that can be used to measure the price impact of an order. Measuring depth, as we have just done, gives us a measure of price impact, in the sense that the depth at the bid/ ask tells us how large a market order can be with a zero price impact, i.e. without walking the LOB.

But, in a single market, a large order would consume all the volume at the best quote and work its way through to the next tick and so on until the order is filled. Thus, whenever an MO walks the LOB, the average price per share is worse than the best quote at the moment the MO was sent to the LOB. In Chapter 6 we have a thorough discussion of how to devise optimal strategies to minimise the market impact of large orders.

So far we have only considered what happens to the MO as it reaches the LOB, but executing a (relatively large) trade can be quite complex. In the US, with 11 public exchanges, regulators have felt a need to regulate what should happen to orders that consume all existing liquidity in one venue at the best bid/ ask, in order to protect investors. This regulation and the multiplicity of exchanges raise related issues of time delays between different venues. So, when sending an MO one has to design the routing strategy very carefully: to which exchanges and when to submit the order, and what will happen if that order consumes all available liquidity at some point. So, an agent needs to know what happens as the order is executed, but also what happens in the aftermath of a trade.

With the information we have from NASDAQ we now look at what happens after orders are executed there. Table 4.9 looks at the executions for AAPL on NASDAQ on July 30th, 2013. As mentioned earlier (in Chapter 3), we do not observe MOs, but rather, what happens to existing posted orders. To illustrate the kind of analysis that can be done, we make the simplistic assumption that all orders executed at the same time (same millisecond) and at the same price level, are all part of the same MO, and are aggregated accordingly.

Table 4.9 looks at what happens when different types of buy and sell orders are executed, i.e. we look at the arrival of MOs under different circumstances. The row labelled "Benchmark" captures what happens on average by including every 10 ms interval during the trading day (2.34 million observations). This serves as benchmark with which to compare what happens in the 10 ms time interval AFTER an MO comes in. We compare this benchmark with what happens after the following six events:

- e Buy[Sell] Order: an order is executed against orders posted on the ask (sellside) [bid (buy-side)] of the book;
- Buy[Sell] Order (n-o): same as Buy [Sell] Order but ignoring buy [sell] orders within 10 ms of a previous buy [sell] order;
- ® Buy[Sell] Order-Large: buy [sell] orders for strictly more than 300 shares.

In Table 4.9 we include statistics on order arrival on the bid and ask side in the benchmark case, as well as after these six events. The columns labelled 'n = O' describe the percentage of cases in which we do not observe an MO arriving on the bid/ask side after an execution. In the benchmark case we see that despite the high level of trading activity in AAPL, our interval size is sufficiently small so that in roughly 99.4 percent of cases we do not observe an order arriving. After any type of execution, this proportion falls on both sides of the book. We observe that after a Buy MO there is at least a second MO arriving in 30 percent of cases, and at least one sell MO in 5 percent of cases. A similar pattern is observed after a Sell MO: in at least 25 percent of cases a sell MO is followed by at least one other MO, while in at least 5 percent of cases a sell MK is followed by a buy MO. We also see very similar patterns if we exclude MO arrivals that occur just after other MOs. The number of arrivals, however, increases substantially after a large order: a large buy (sell) is followed by other buys in 43 (38) percent of cases, and by sells in 8 (8) percent of cases. If we look at the quartiles conditional on there being at least one MO (the columns labeled 'Ql', 'Q2' and 'Q3'), the arrival of a market buy (sell) order seems to have no clear effect on the distribution of arriving sell (buy) orders, but we do see evidence suggesting that incoming orders on the same side may be more frequent. So, our very preliminary and limited analysis suggests that order arrival seems to be followed by further order arrival on both sides of the book, and more on its own side than on the other side of the book.

|                  |           |      | Buy Market Orders |    |    | Sell Market Orders |    |    |    |
|------------------|-----------|------|-------------------|----|----|--------------------|----|----|----|
| Event            | n         | n=O  | Ql                | Q2 | Q3 | n=O                | Ql | Q2 | Q3 |
| Benchmark        | 2,340,000 | 99.6 | 1                 | 1  | 2  | 99.7               | 1  | 1  | 2  |
| Buy Order        | 6,852     | 70.7 | 1                 | 2  | 3  | 94.3               | 1  | 1  | 2  |
| Buy Order (n-o)  | 5,707     | 71.5 | 1                 | 2  | 3  | 94.4               | 1  | 1  | 2  |
| Buy Order-Large  | 532       | 57.5 | 1                 | 2  | 5  | 92.1               | 1  | 1  | 2  |
| Sell Order       | 7,358     | 94.5 | 1                 | 1  | 2  | 74.9               | 1  | 2  | 3  |
| Sell Order (n-o) | 6,269     | 94.7 | 1                 | 1  | 2  | 75.7               | 1  | 2  | 3  |
| Sell Order-Large | 347       | 92.2 | 1                 | 1  | 2  | 62.2               | 1  | 2  | 4  |

**Table 4.9** Market Impact of an execution on MOs (AAPL 20130730).

In Table 4.10 we do a similar analysis where we look at how different events affect the bid and ask prices. For this table we follow the convention that + 1 is a one cent move away from the best price, that is: if the ask price is \$453.02, a + 1 in the ask is a change from \$453.02 to \$453.03, while on the bid side, with the bid price at \$452.96, + 1 in the bid is a price drop of one cent, that is a change from \$452.96 to \$452.95. With this convention, positive price changes represent moves away from the midprice and negative price changes represent moves towards the midprice, which allows us to provide a more streamlined presentation of the different effects of MOs on bid and ask sides.

Returning to Table 4.10, we consider how different orders affect the best price on their own side of the LOB, that is, the left side of the table describes how the ask price reacts to an aggressive buy MO, and the right decribes how the bid side reacts to an aggressive sell MO.

We consider two benchmark cases: the column 'Ask' ('Bid') is the benchmark case that looks at average changes in the ask (bid), that is after every 10 ms interval. The first row tells us the percentage of time for which there was no change in the bid (99.5 percent) and no change in the ask (also 99.5 percent). We also look at what happens to the ask (bid) after a 'Buy' ('Sell') order comes in, and the percentage of times when the ask (bid) stays the same drops to

|        |      |       | Changes in ASK |        |      |       | Changes in BID |        |
|--------|------|-------|----------------|--------|------|-------|----------------|--------|
| Ticks  | Ask  | Buys  | L # 0          | L > 3c | Bid  | Sells | L#O            | L > 3c |
| Obs    |      | 6,852 | 3,259          | 1,165  |      | 7,358 | 4,052          | 1,910  |
| 0      | 99.5 | 28.2  | 10.7           | 9.7    | 99.5 | 22.7  | 7.2            | 6.1    |
| ::0--5 | 12.8 | 0.1   | 0.0            | 0.0    | 17.2 | 0.3   | 0.4            | 0.2    |
| -4     | 4.5  | 0.1   | 0.1            | 0.3    | 4.5  | 0.0   | 0.0            | 0.0    |
| -3     | 5.6  | 0.1   | 0.1            | 0.0    | 5.6  | 0.1   | 0.1            | 0.0    |
| -2     | 8.6  | 0.1   | 0.1            | 0.1    | 7.0  | 0.1   | 0.1            | 0.1    |
| -1     | 22.6 | 1.1   | 0.4            | 0.7    | 17.9 | 0.8   | 0.4            | 0.5    |
| 1      | 14.2 | 19.5  | 20.5           | 0.9    | 13.3 | 15.7  | 14.3           | 0.9    |
| 2      | 7.4  | 13.6  | 13.6           | 0.9    | 7.1  | 11.8  | 11.3           | 0.9    |
| 3      | 5.6  | 12.3  | 11.9           | 1.9    | 5.5  | 10.4  | 10.2           | 0.9    |
| 4      | 4.4  | 9.8   | 9.2            | 15.3   | 4.3  | 9.5   | 9.4            | 12.2   |
| :S5    | 14.3 | 43.4  | 44.2           | 80.0   | 17.5 | 51.3  | 53.9           | 84.4   |

Table 4.10 Market Impact of an execution on the best price - own side (AAPL 20130730).

28 (23) percent. This percentage falls even further if we only look at executions that sweep the order book (6. # 0), that is after a buy (sell) order that generates . an immediate change in the ask (bid). Such 'large' executions are more long-lived in the sense that 10 ms after such a change the probability that the ask (bid) has returned to its pre-order arrival level drops to 11 (7) percent. The columns labelled '6. > 3c' look at the subset of the executions that sweep the order book, and we also observe a large (greater than three cent) change in the ask (bid) price respectively. The likelihood of returning is smaller than that for all sweep orders but not by much.

The rows of Table 4.10 (except the 'Obs' and 'O' rows) reflect the distribution of price movements conditional on different non-zero price changes. The benchmark distributions for bid and ask price movements are symmetric and very similar, something that is not true for the distributions after MOs arrivals. After a buy (sell) order, the distribution of the ask (bid) clearly shifts away from its previous level and is almost never better ( closer to the mid price) than before the arrival of the MO 10 ms later. The difference we observe for a sweep order seems to be centred on the probability of returning to the pre-arrival level, but does not seem to have much effect on the distribution of price changes for non-zero changes. However, large price swings do seem to be followed by changes in the distribution of bid/ ask price changes, and we see little evidence that these large price movements are reversed within 10 ms.

In Table 4.11 we repeat the analysis but looking at the effect of an order arrival on the other side of the book, that is how the arrival of a buy (sell) MO affects the bid (ask). We keep the signs so that a positive move in Table 4.10 is also a positive move on the other side of the book in Table 4.11. That is, suppose the

|       |      |      | Changes in BID |        |      |       | Changes in ASK |        |
|-------|------|------|----------------|--------|------|-------|----------------|--------|
| Ticks | Bid  | Buys | 6 #0           | 6 > 3c | Ask  | Sells | 6#0            | 6 > 3c |
| Obs   |      | 6852 | 3259           | 1165   |      | 7358  | 4052           | 1910   |
| 0     | 99.5 | 81.6 | 78.7           | 75.4   | 99.5 | 82.2  | 80.3           | 79.1   |
| 2:-5  | 17.5 | 6.9  | 6.5            | 7.7    | 14.3 | 6.0   | 6.0            | 8.3    |
| -4    | 4.3  | 1.8  | 1.7            | 2.8    | 4.4  | 1.7   | 1.8            | 2.0    |
| -3    | 5.5  | 1.8  | 1.9            | 3.1    | 5.6  | 2.1   | 2.1            | 2.8    |
| -2    | 7.1  | 3.2  | 3.9            | 3.1    | 7.4  | 3.4   | 3.3            | 4.3    |
| -1    | 13.3 | 8.7  | 8.2            | 9.1    | 14.2 | 8.0   | 8.1            | 8.5    |
| 1     | 17.9 | 29.5 | 28.7           | 34.8   | 22.6 | 29.2  | 27.7           | 28.8   |
| 2     | 7.0  | 10.8 | 11.8           | 11.8   | 8.6  | 11.6  | 12.9           | 13.5   |
| 3     | 5.6  | 7.0  | 6.3            | 7.3    | 5.6  | 6.5   | 6.4            | 6.0    |
| 4     | 4.5  | 6.1  | 5.0            | 2.4    | 4.5  | 6.8   | 5.6            | 4.5    |
| :::;5 | 17.2 | 24.2 | 25.9           | 17.8   | 12.8 | 24.7  | 26.1           | 21.3   |

Table 4.11 Market Impact of an execution on the best price - other side (AAPL 20130730).

ask price is \$453.02 and the bid is \$452.96. After a buy order, a+ 1 cent change in the ask is an increase from \$453.02 to \$453.03 (Table 4.10), and a +l cent move in the bid is an increase from \$452.96 to \$452.97 (Table 4.11). Whereas after a sell order, a +l cent change in the bid results in a decrease from \$452.96 to \$452.95 (Table 4.10), and a +l cent move in the ask results is a change from \$453.02 to \$453.01 (Table 4.11).

With this convention, we see that the effect of an arrival on one side of the LOB is followed by a similar but weaker effect on the other. The probability of the price remaining/returning to the pre-arrival level drops from 99.5 to 82 for both the bid and the ask after a buy and a sell order arrive, respectively. This probability is slightly smaller for (intermarket) sweep orders. We also see a shift in the distribution of non-zero price changes that (weakly) follows that of the changes on the other side of the book. So we see how the arrival of a buy order is followed by a shift in the (non-zero) bid price changes away from the midprice, so the conditional probability of a 1 cent move away from the prearrival bid price goes from 17.9 to 29.5 percent after a buy order, and that of a 1 cent move away from the pre-arrival ask price goes from 22.6 to 29.2 percent after a sell order. The pattern is very similar after a buy (sell) order, a sweep buy (sell) order, or a sweep buy (sell) order with a large price move. Combining this observation with the price moves in Table 4.10, we find evidence that the quoted spread increases after a buy or sell order, and substantially so after a large sweep order.

To conclude our look at the impact of MOs, in Table 4.12 we look at the effect on the changes we observed at the 10 ms horizon, we consider longer (30 ms, 100 ms and 1,000 ms) horizons. Table 4.12 is split horizontally into three sections:

|       | Ticks    | 10   | 30   | Changes in ASK<br>100 | 1,000 | 10   | 30   | Changes in BID<br>100 | 1,000 |
|-------|----------|------|------|-----------------------|-------|------|------|-----------------------|-------|
|       |          |      |      |                       |       |      |      |                       |       |
|       | <= -3    | 0.1  | 0.3  | 1.0                   | 7.7   | 0.1  | 0.4  | 1.2                   | 8.9   |
|       | {-1,-2}  | 0.2  | 0.4  | 1.2                   | 7.7   | 0.1  | 0.3  | 0.7                   | 4.0   |
| Bench | 0        | 99.5 | 98.7 | 96.0                  | 72.9  | 99.5 | 98.6 | 95.7                  | 70.3  |
|       | {1,2}    | 0.1  | 0.3  | 0.7                   | 3.9   | 0.1  | 0.4  | 1.1                   | 6.9   |
|       | >= 3     | 0.1  | 0.3  | 1.0                   | 7.7   | 0.1  | 0.4  | 1.3                   | 9.9   |
|       | <= -3    | 0.2  | 0.3  | 0.4                   | 1.3   | 6.9  | 9.8  | 13.2                  | 26.2  |
|       | {-1, -2} | 0.8  | 1.0  | 1.4                   | 3.1   | 7.4  | 7.8  | 8.3                   | 11.3  |
| Buys  | 0        | 28.2 | 26.7 | 24.3                  | 16.0  | 81.6 | 77.8 | 72.4                  | 49.2  |
|       | {1,2}    | 23.8 | 22.4 | 21.8                  | 18.4  | 2.2  | 2.4  | 2.6                   | 4.1   |
|       | >=3      | 47.0 | 49.6 | 52.1                  | 61.3  | 1.9  | 2.2  | 3.5                   | 9.2   |
|       | <= -3    | 6.8  | 8.3  | 12.0                  | 24.0  | 4.1  | 4.2  | 4.6                   | 6.8   |
|       | {-1,-2}  | 7.3  | 8.3  | 9.3                   | 13.3  | 4.1  | 4.0  | 4.3                   | 6.2   |
| Sells | 0        | 82.2 | 78.8 | 73.4                  | 52.3  | 47.3 | 44.6 | 41.1                  | 28.1  |
|       | {1,2}    | 2.0  | 2.1  | 2.6                   | 4.0   | 15.9 | 15.7 | 15.0                  | 14.5  |
|       | >=3      | 1.8  | 2.4  | 2.7                   | 6.4   | 28.5 | 31.4 | 35.0                  | 44.4  |

Table 4.12 Market Impact of an execution on the midprice over time (AAPL 20130730).

the first ('Bench') is the benchmark table that looks at changes in the bid and ask over the corresponding horizons for all such time intervals; the bottom two sections consider the effects of the arrival of a buy and a sell order respectively on bid and ask prices. For this table we continue to keep the signs matched on the bid and ask sides, but to avoid confusion we keep the sign of changes on the bid (ask) side the same as in the benchmark case, as well as after a buy or a sell order, that is, the interpretation of the sign does not depend on whether it follows a buy or a sell MO, but only on which side of the book we are looking at. So, suppose the ask price is \$453.02 and the bid is \$452.96. After a buy order, a + 1 cent in the ask is a move from \$453.02 to \$453.03, and a + 1 cent move in the bid is a move from \$452.96 to \$452.95 (a 1 cent move away from the midprice). The same happens after a sell order (and in the benchmark case): a +1 cent in the ask results in an increase from \$453.02 to \$453.03, and a + 1 cent move in the bid is move from \$452.96 to \$452.95 (one cent away from the midprice). Note also, that all percentiles reflect probabilities ( we are not conditioning on non-zero price movements in this table).

The first thing to notice in Table 4.12 is the natural effect of time on all prices: as we expand the horizon, prices tend to move more, and the distributions become more dispersed. We also see that the initial price movements are not followed by quick reversals and that even one second (1,000 ms) after a buy order there is a marked shift of the bid and ask away from its pre-execution level, with worse prices and a hint of a delayed price impact on future executions and wider spreads.

All these results must be interpreted in context, and not causally. As we will now see, MOs do not arrive at random times. They tend to arrive when spreads are narrow, and opportunistically hit orders that are posted closer to the midprice, so it is only natural that we should observe a wider spread after an execution.

### 4.3.5 Walking the LOB and Permanent Price Impact

We have seen that one of the key ingredients in trading algorithms is how the investor's own actions together with the order flow of the other market participants affect the price of the assets she is trading in. In the trading algorithms developed in Part III we show how strategics depend on the market impact of trades. For example in Chapter 6 we show how to trade large positions when the investor's own trades walk the LOB, in addition to adversely affecting the midprice by exerting upward ( downward) pressure in the drift of the midprice if the investor is buying (selling). In Chapter 7 we study the problem of an agent wishing to liquidate a large position when the order flow from other traders in the market also impacts the midprice. In this case, if the agent's execution programme is going with or against net order flow, the strategy adapts to maximise the revenues from liquidating the position.

Here we want to empirically assess the parameter values for the different effects a trade can have on prices: the permanent and the temporary price impact. We look at these impacts for five stocks using data from NASDAQ and for the year 2013. A first approach is to estimate these separately. We first estimate the permanent price impact by looking at the impact of order flow on the change in price over five-minute intervals. Let b..Sn = Sm- - S(n-l)T be the change in the midprice during the time interval [(n - l)T, nT] where T = 5 min. Let µn be the net order flow defined as the difference between the volumes of buy and sell MOs during the same time interval. We then estimate the permanent price impact as the parameter b in the following robust linear regression:

$$\Delta S_n = b \,\mu_n + \varepsilon_n,\tag{4.2}$$

where *En* is the error term (assumed normal). The model (4.2) is estimated every day, using Winsorised data, excluding the upper and lower 0.5% tails. The first row of Table 4.13 shows the average value of the estimated parameters for permanent price impact and the second row shows its standard deviation.

In the third and fourth rows of the table we show the parameter estimate for temporary impact and its standard deviation respectively. To estimate this parameter, which we denote by *k,* we assume that temporary price impact is linear in the volume traded. Specifically, the difference between the execution price that the investor receives and the best quote is k *Q,* where *Q* is the total volume traded. To perform the estimation, we take a snapshot of the LOB each second, determine the price per share s;xec(Qi) for various volumes {Q1, Q*2,* ... , QN} (by walking the LOB), compute the difference between the execution price per share and the best quote at that time, and perform a linear regression. That is we regress,

$$S_{i,t}^{exec, bid} = S_t^{bid} - k^{bid} Q_i + \varepsilon_{i,t}^{bid} , \qquad S_{i,t}^{exec, ask} = S_t^{ask} + k^{ask} Q_i + \varepsilon_{i,t}^{ask}$$

where  $\varepsilon_{i,t}$  represent the estimation error of the *i*<sup>th</sup> volume for the *t*<sup>th</sup> timestamp.

The slope argument of the linear regression  $\hat{k}$  is an estimate of the temporary price impact per share at that time. We do this for every second of every trading day and in the table we report the mean and standard deviation of these daily estimates (for the buy side) when we exclude the first and last half-hour of the trading day and Winsorise the data. Moreover, the fifth row shows the mean of the daily ratio  $b/k$ , and the sixth row shows its standard deviation. We observe that FARO shows the smallest ratio of  $1.02$  and SMH shows the largest at  $7.43$  $-$  at the end of this section we discuss this ratio in more detail.

| INTC           | ORCL           | NTAP                                                                                                                                                                                                                                                               | $\text{SMH}$   | FARO           |     |
|----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------------|-----|
|                |                | $\hat{b} = 1.41 \times 10^{-4} = 5.45 \times 10^{-6} = 5.93 \times 10^{-6} = 1.82 \times 10^{-6} = 6.15 \times 10^{-7}$<br>$(9.61 \times 10^{-5}) \quad (4.20 \times 10^{-6}) \quad (2.31 \times 10^{-6}) \quad (7.19 \times 10^{-7}) \quad (2.16 \times 10^{-7})$ |                |                |     |
|                |                | $1.86 \times 10^{-4}$ $8.49 \times 10^{-7}$ $3.09 \times 10^{-6}$ $8.23 \times 10^{-7}$ $2.50 \times 10^{-7}$<br>$(2.56 \times 10^{-4})$ $(8.22 \times 10^{-7})$ $(1.75 \times 10^{-6})$ $(3.78 \times 10^{-7})$ $(1.25 \times 10^{-7})$                           |                |                | k   |
| 2.55<br>(0.70) | 2.28<br>(0.74) | 2.04<br>(0.77)                                                                                                                                                                                                                                                     | 7.43<br>(6.24) | 1.02<br>(0.83) | b/k |

**Table 4.13** Permanent and temporary price impact parameters for NASDAQ stocks for 2013. Below each parameter estimate we show its standard deviation.

Moreover, to showcase the variability of the permanent price impact parameter, the first panel of Figure 4.10 depicts the estimate of  $b$  for each day of 2013 - the dashed line shows the average  $\hat{b}$ . The second panel in the figure shows a histogram of the five-minute net order flow using all the data in 2013. Finally, the last panel shows the expected net order flow (with error bars) conditional on a given price change being observed.<sup>3</sup> As already shown by the regression results there is a positive relationship between net order flow and price changes. The figure shows further details of this relationship to support the finding that when net order flow is positive (negative), that is more (less) buy than sell MOs, the midprice tends to increase (decrease). Moreover, we see that assuming a linear relationship between price changes and net order flow is plausible for a wide range of midprice changes. Only in the two extremes, very high or very low price changes, does the relationship fails to be linear, but we note that there are fewer

 $^{3}$  For the year 2013, 99% of the 5 minute price changes for INTC were within the range  $[-0.1, 0.1]$ .

![](_page_28_Figure_1.jpeg)

observations in the tails as shown by the histogram and this is also shown by the confidence intervals around the estimates.

Figure 4.11 explores the temporary price impact for INTC. The top panel shows a snapshot of the LOB for INTC on Nov 1, 2013 at 11am. The bottom left panel captures the empirical temporary price impact curve generated by hypothetical MOs of various quantities as they walk through the buy side of the LOB. Each curve represents the curve at every second from 11:00 to 11:01. We also include a linear regression with intercept set to the half-spread (the dash line) which would correspond to the model used to estimate the parameter k above. Notice that the impact function fluctuates within the minute, and with it the impact that trades of different size could have. The linear regression provides an approximation of the temporary impact during that one minute.

The third picture in the Figure shows how the slope of this linear impact model fluctuates throughout the entire day. We see that the largest impact tends to occur in the morning, then this impact flattens and stays flat throughout the day, and towards the end of the day it lessens. Such a pattern is seen in a number of assets and is consistent with the reduction in spreads and increases in depth we have documented earlier.

The analysis above looks at temporary and permanent effects separately but their joint dynamics is a relevant quantity in execution algorithms. Liquidation and acquisition strategies take into account the trade-off between costs that stem from walking the book and the permanent impact. In particular, when both types

![](_page_29_Figure_1.jpeg)

of impact are linear in the rates of trading, this trade-off is in part captured by the ratio  $b/k$  (see for example Section 7.3 in the context of a liquidation algorithm and Chapter 9 for strategies that track volume such as POV and VWAP). In the left panel of Figure 4.12 we show a scatter plot of the daily pair  $(b, k)$  for INTC which shows a clear positive relationship between temporary and permanent impact. This is consistent with the theoretical relationship between price impact and depth, so that days with little depth will be associated with high price impact, both permanent and temporary, while a deep market will be associated with lower price impacts. Finally, in the right panel of the figure we see the histogram for the ratio  $b/k$  which ranges between 1 and 4 and is symmetric around approximately  $2.5$ .

#### 4.4 Messages and Cancellation Activity

An important feature in the way exchanges operate is the ability to cancel LOs which have not been filled. Traders who provide liquidity must be able to change their views on the market and therefore cancel their LOs or reposition them in the light of new information. Later, when we look at algorithms that provide liquidity to the market (see for instance Chapters 7, 8 and  $10$ ) we will see that these rely on the ability to reposition LOs in the LOB. For example, when we develop market making algorithms that require low latency, the agent is

![](_page_30_Figure_1.jpeg)

**Figure 4.12** Price Impact INTC using daily observations for 2013.

constantly cancelling LOs to reposition them as new information arrives and the agent's view on short-lived deviations in the midprice are taken into account.

Here we employ our detailed ITCH data to measure trading activity by the number of messages recorded by the exchange, where a 'message' is a line of data in the ITCH dataset, as we saw at the beginning of the chapter. The total number of messages is slightly greater than twice the number of posted orders, as most posted orders are either cancelled or executed in full.

| $\text{Asset}$ | Mean    | $\text{StdDev}$ | P01     | $\text{O1}$ | Median  | $\text{O3}$ | P99       |
|----------------|---------|-----------------|---------|-------------|---------|-------------|-----------|
| ISNS           | 1.711   | 6.078           | 173     | 450         | 760     | 1.745       | 8,943     |
| FARO           | 24.038  | 10.871          | 8.524   | 16.277      | 22.347  | 29,232      | 71,445    |
| MENT           | 59,661  | 21.755          | 23.157  | 43.477      | 53,972  | 72,639      | 131,715   |
| AAPL           | 531.728 | 166.652         | 280,242 | 417.576     | 500,680 | 614.437     | 1.067.248 |

**Table 4.14** Daily Number of Messages (in 000s).

Table 4.14 contains the descriptive statistics for daily messages for our four assets (in thousands; P01 and P99 refer to the 1st and 99th percentile, respectively). We can see how, as with trading activity, the number of messages for each asset is different by orders of magnitude (except that for of MENT which is about  $2.5$  times that for FARO). In order to adjust for trading activity, a usual procedure is to normalise by the number of trades (as we do in Table  $(4.15)$  or by trading volume. The results in Table  $4.15$  suggest an interesting phenomenon: more frequently traded assets 'require' fewer messages per trade than less frequently traded ones.

The reverse of this phenomenon is captured in Table 4.16, where we look at the percentage of cancellations (out of all messages: posts, cancels and executions). Only for AAPL do we see less than  $45\%$  of orders being cancelled most of the time.

| Asset        | Mean         | StdDev       | POl          | Ql           | Median       | Q3            | P99            |
|--------------|--------------|--------------|--------------|--------------|--------------|---------------|----------------|
| ISNS         | 226.7        | 749.1        | 10.8         | 44.4         | 80.7         | 159.1         | 2885.1         |
| FARO<br>MENT | 88.2<br>70.0 | 55.8<br>21.8 | 20.7<br>29.8 | 57.8<br>54.2 | 79.4<br>66.5 | 106.1<br>83.2 | 223.5<br>134.2 |
| AAPL         | 22.6         | 4.9          | 12.6         | 19.3         | 22.3         | 25.3          | 39.4           |

**Table 4.15** Messages per Number of Trades.

| Asset | Mean | StdDev | POI  | Ql   | Median | Q3   | P99  |
|-------|------|--------|------|------|--------|------|------|
| ISNS  | 45.8 | 3.2    | 36.3 | 44.2 | 46.4   | 48.3 | 49.9 |
| FARO  | 48.1 | 1.0    | 44.4 | 47.6 | 48.3   | 48.7 | 49.5 |
| MENT  | 47.2 | 1.0    | 44.1 | 46.7 | 47.4   | 48.0 | 48.9 |
| AAPL  | 43.1 | 1.9    | 37.8 | 41.8 | 43.3   | 44.3 | 47.1 |

**Table 4.16** Cancellations as percentage of Messages.

For intraday trading, it is very important to understand the posting and cancellation dynamics, especially around the bid and ask. Table 4.17 looks at the orders posted by their distance to the midprice ('Distance to Mid', k) for AAPL on July 30th, 2013 and to illustrate the contents of the table we use Figure 4.13. The second column ('Posts') counts the number of messages posted k ticks (cents) from the mid price. In Figure 4.13 we display this visually using a hypothetical midprice of \$101.05, and split the quantities evenly between the bid and the ask. Thus, for example, the total quantity posted two ticks from the midprice (3,053 units) is displayed as 1,527 units posted at \$101.07 and 1,527 units posted at \$101.03 (the total length of the bars). The third column ('% Exe') looks at the percentage of those posted messages that were executed, that is, the posted order was crossed with an incoming MO. In Figure 4.13 this is illustrated by using a lighter colour for the orders that were executed (and a darker one for those cancelled). Thus, for example, of the 1,527 units posted at \$101.07, 64.7 percent (988 units) were executed. Finally, the fourth column ('Exe') describes the percentage of the total number of executed orders that were executed at that level. So, these 988 orders executed at \$101.07 plus the 988 executed at \$101.03, represent 9.2% of the total number of orders executed that day.

If we consider that the ( one-minute time-average) quoted spread for that day is 10.3 cents on average (Ql: 8.5, median: 10.2, Q3: 11.7), most of the time the distance to the midprice (half of the quoted spread) is between 4 and 6 cents. Using the information in Table 4.17 we compute that 26% of orders executed were initially posted at between 1 and 3 cents from the midprice, but only 32% are posted between 4 and 6 and the remaining 42% of orders executed had been originally posted relatively far from the midprice (7+ cents away).

If, on the other hand, we look at the distance from the midprice at the time

| Distance    |         | At Post |      |         | At Exit     |      |
|-------------|---------|---------|------|---------|-------------|------|
| to Midprice | Posts   | % Exec  | Exec | Posts   | % Exec      | Exec |
| <2          | 905     | 78.6    | 3.3  |         | 988<br>88.4 | 4.1  |
| 2           | 3,053   | 64.7    | 9.2  | 3,508   | 76.4        | 12.5 |
| 3           | 5,193   | 55.4    | 13.5 | 6,236   | 67.5        | 19.7 |
| 4           | 5,617   | 44.4    | 11.7 | 6,448   | 51.5        | 15.6 |
| 5           | 6,374   | 34.9    | 10.4 | 7,557   | 45.5        | 16.1 |
| 6           | 7,626   | 27.6    | 9.8  | 7,586   | 29.9        | 10.6 |
| 7           | 7,996   | 20.2    | 7.6  | 7,624   | 20.4        | 7.3  |
| 8           | 7,826   | 15.9    | 5.8  | 8,062   | 14.2        | 5.4  |
| 9           | 7,675   | 12.3    | 4.4  | 7,946   | 7.5         | 2.8  |
| 10          | 7,967   | 8.6     | 3.2  | 7,487   | 6.1         | 2.1  |
| ><br>10     | 195,415 | 2.3     | 21   | 192,205 | 0.4         | 3.8  |

**Table 4.17** Messages by distance to midprice at post and at exit (AAPL 2013-07-30).

![](_page_32_Figure_3.jpeg)

**Figure 4.13** Illustration of orders posted and executed as described in Table 4.17.

the trade was *executed,* not posted, in Table 4.17, we find that the distance to the midprice is (naturally) shorter, and we can compute that 36% of orders were executed at prices between 1 and 3 cents from the midprice, and 42% at prices between 4 and 6, so that only 22 % of executions were relatively far from the midprice (7+ cents away). This illustrates the point made earlier (when comparing the volatility of the effective and the quoted spreads) that executions tend to occur more often when the spread is narrower, and hence the effective spread will naturally be less volatile than the quoted spread.

In Figure 4.14 we display the survivor function, *S(x),* (one minus the CDF: *S(x)* = *Pr(X* > *x)* = *l-F(x))* of total executions, as the distance from the price at which the original LO was posted increases. This represents an approximation to the 'fill probability' - the probability that a posted order is executed. The thick blue line describes the distribution in Table 4.17. We have also included the same distribution separating executions on the bid and ask side, and it is interesting that the distribution for bid-( ask-)side executions lies systematically below (above) the one for all executions. This indicates that market buy orders

![](_page_33_Figure_1.jpeg)

**Figure 4.14** Survivor function for executions as a function of distance from mid price.

tended to occur much closer to the midprice than market sell orders on this particular day, which had an overall positive order flow for AAPL shares and a slight price increase from market open to market close.

In Figure 4.14, we have also included total executions separated by the time of day: the first half hour after the market opens (Mkt Start), the last half hour before the market closes (Mkt Close), and the time in between (Intraday). We observe that Mkt Close tends to be below that of Intraday, implying that during the last half hour of trading, executions tend to be close to the midprice, which is consistent with the pattern of the quoted spread in Figure 4.6. But the difference · does not seem to be very large and may be statistically insignificant.

What happens at the market open does look very different, as the distribution is above and quite far away from that for Intraday. It appears that the wider spreads we observed in Figure 4.6 and the uncertainty from Figure 4.7 combine to generate executions for orders posted quite far from the midprice.

Figure 4.15 looks at the same data from a different angle. In it we consider (in logs) the proportion of orders posted a certain distance from the mid price, that were eventually executed. Interpreting this proportion as a probability, the figure displays the natural decreasing relationship between the distance from the midprice and the probability of the order being executed. We have drawn these curves for: all executions, aggressive buys and sells, and executions by time of day: around the market open, the market close, and the rest of the day. All of them are very similar with only one exception: that for the first half hour of the trading day (Mkt Start). What we observe (looking at the underlying data) is that, at Mkt Start, an unusually high proportion of trades which were posted six cents from the midprice were later executed, and this generates the shift in the CDF we observe in Figure 4.15. Looking at the quoted spreads during that time, we find that the mean was 15.2 cents on average (Ql: 12.5, median: 14.2, Q3: 19.0), which suggests that as early morning uncertainty over the 'true market price' was reduced, the quoted spread was slow to react and a relatively large number of executions occurred - and this happened when the quoted spread had fallen to around 12 cents.

![](_page_34_Figure_1.jpeg)

Figure 4.15 Log of the proportion of posted orders that are executed as a function of distance from midprice.

#### $4.5$ Hidden Orders

When discussing market quality earlier (Section  $4.3$ ), and spreads in particular, we saw that one of the reasons why the quoted spread is generally greater than the effective spread is the presence of posted orders that are not visible to market participants, but that will match with incoming MOs ahead of existing visible ones (at a price at or better than the current bid/ask). These are **hidden orders**.

| $\text{Asset}$ | Mean  | $\text{StdDev}$ | P01 | Q1    | Median | Q3    | P99    |
|----------------|-------|-----------------|-----|-------|--------|-------|--------|
| ISNS           | 4     | 59              | 0   | 0     | 0      | 0     | 100    |
| FARO           | 31    | 154             | 0   | 0     | 0      | 0     | 600    |
| MENT           | 117   | 568             | 0   | 0     | 0      | 0     | 2,150  |
| $\text{AAPL}$  | 3.849 | 5,905           | 0   | 1,052 | 2,220  | 4,504 | 26,547 |
| ISNS           | 1.2   | 10.7            | 0.0 | 0.0   | 0.0    | 0.0   | 99.6   |
| FARO           | 9.9   | 27.1            | 0.0 | 0.0   | 0.0    | 0.0   | 100.0  |
| MENT           | 9.4   | 24.1            | 0.0 | 0.0   | 0.0    | 0.0   | 100.0  |
| AAPL           | 44.6  | 16.9            | 0.0 | 33.5  | 44.9   | 56.0  | 83.7   |

**Table 4.18** Execution against hidden orders (volume  $(Q)$  and percentage).

Table 4.18 is split into two panels. The top panel of the table describes the quantity executed against hidden orders in NASDAQ per minute, for each minute of 2013. As we can see, for the less traded assets, ISNS, FARO and MENT, there is little trading taking place against hidden orders (less than 25 percent of the time), though when it happens it can be quite significant. But for AAPL, the case is quite different. We find trading against hidden orders more than 75 percent of the time, and for a substantial amount of shares (more than  $1,000$  units per minute). Note that these large quantities are not indicative of large trades, but rather of quite frequent ones: the distribution of the average size of an MO executed against a hidden order (per minute) has a mean of  $127$ , with Q1 equal to 94 and  $Q3$  to 148 shares per trade.

The bottom panel of Table 4.18 considers the same variable, the quantity of

shares executed against hidden orders, but rather than in absolute numbers, as a proportion of the total number of shares executed (in that minute). For ISNS, FARO and MENT, executions are relatively infrequent, and when they occur against hidden orders they tend to be isolated trades. In those cases, the hidden order is a large proportion, if not one hundred percent, of all shares traded during that minute. For AAPL, execution against hidden orders is a common phenomenon and half the time they represent between 33 and 56 percent of all trades. An agent posting visible offers for AAPL at the bid and ask ( during 2013) found her offers trumped by more aggressive hidden ones relatively often.

## 4.6 Bibliography and Selected Readings

Boehmer, Fong & Wu (2012), Chabaud, Hjalmarsson, Vega & Chiquoine (2009), Moallemi & Saglam (2013), SEC (2010), CFTC & SEC (2010), Hendershott, Jones & Menkveld (2011), Biais, Bisiere & Spatt (2010), Biais et al. (2005), Hagstromer & Norden (2013), Andersen & Bondarenko (2014), Pascual & Veredas (2009), Hirschey (2013), Martinez, Nieto, Rubio & Tapia (2005), Hasbrouck (2013), Hasbrouck & Saar (2013), Cartea & Meyer-Brandis (2010), Cartea (2013), Brogaard, Hendershott & Riordan (2014), Menkveld (2013), Riordan & Starkenmaier (2012), Hendershott & Riordan (2013), Foucault, Kadan & Kandel (2013), Moro, Vicente, Moyano, Gerig, Farmer, Vaglica, Lillo & Mantegna (2009), Gerig (2012), Hall & Hautsch (2007), Gould, Porter, Williams, McDonald, Fenn & Howison (2013).
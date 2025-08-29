![](_page_0_Picture_1.jpeg)

Transaction costs can have a significant effect on investment returns. Therefore, it is important to both measure and analyse them if "best execution" is to be achieved.

### 6.1 Introduction

Each time an asset is bought or sold transaction costs are incurred. In economic terms, Robert Kissell (2006) describes them as costs paid by buyers, but not received by the sellers. They can have a considerable effect on investment returns, for instance, Ed Nicoll (2004) estimated total annual transaction costs of approximately \$120 billion for the \$12 trillion U.S. equity market. This is based on costs per order ranging from 20 basis points (bps) up to  $200$  (or 2%) of the value. The wide range is partly due to the different characteristics of each asset and order, but is also due to the different ways transaction costs may be assigned.

One of the most common ways to examine transaction costs has been to compare the actual performance of a portfolio with its "paper" equivalent. A paper portfolio is simply a virtual portfolio traded at benchmark prices, but without accounting for any costs.

![](_page_0_Figure_6.jpeg)

Figure 6-1 Comparing the performance of a portfolio

The difference in performance between a portfolio and its theoretical "paper" equivalent

was termed the "implementation shortfall" by André Perold (1988), as shown in Figure 6-1. Alternatively, this is sometimes referred to as "slippage".

A specific example of the impact of transaction costs is given by David Leinweber (2002) for the returns of a fund based on the Value Line portfolio. The Value Line Investment Survey is a weekly stock analysis newsletter focussed on the U.S. Between 1979 and 1991 the paper portfolio achieved an annualized return of 26.2%, whereas the actual fund actually managed  $16.1\%$ . Much of this difference is directly attributable to transaction costs, since the fund made the same trades as recommended in the newsletter.

Whilst transaction costs are inevitable, they can be minimised. Therefore, in order to maximise investment returns it is important to accurately measure transaction costs and to analyse them to understand how and why they occur.

### 6.2 The investment process

Transaction costs span the entire investment process. They may be tracked from the initial decision to buy/sell an asset through to the actual orders and executions that achieve it.

![](_page_1_Figure_6.jpeg)

Figure 6-2 The investment process

 $\frac{1}{2}$  Leinweber notes that some of the shortfall was due to enforced delays before trading, ensuring that the fund did not front-run the newsletter subscribers.

Figure 6-2 shows a simplified view of the process, covering both traditional broker trading as well as algorithmic / DMA execution: The initial source of each order lies on the buy-side, with an investment buy or sell idea. The potential impact on the investment portfolio is then modelled by the portfolio manager, who will use optimisation techniques and risk analysis to determine the set of target positions. An internal trader must then identify the best way to trade these orders,  $^{2}$  This is achieved by estimating the potential transaction costs, as well as considering historical broker performance. Having decided on the most appropriate means of trading, the orders are then routed for execution. Most commonly, this will mean sending them to a sell-side institution, from where they will be sent out to the market. This may be achieved via a salesperson/trader or by an algorithmic trading/DMA process.<sup>3</sup> Finally. executions from the market will complete the order and trade reports will be sent back to the buy-side.

An alternative way of viewing this process is to consider the whole investment cycle, as highlighted by Ananth Madhavan (2002). Rather than focussing on the individuals involved, it emphasises the cyclical nature of the investment process, shown in Figure 6-3. Trade execution is driven by the investment strategy, but it also gives important feedback, which may affect future investment decisions.

![](_page_2_Figure_3.jpeg)

Source: Madhavan (2002b)

Reproduced with permission from ITG Inc. and Institutional Investor

Figure 6-3 The investment cycle

Clearly, transaction cost analysis is an important part of the investment process:

- $\bullet$ Pre-trade analysis concentrates on estimating potential transaction costs. Hence it is a key input into the choice of trading strategy and can have a substantial effect on the overall execution (and so investment) performance. Liquidity analysis may also be used to identify the best strategies and venues for trading.
- Post-trade analysis focuses on execution performance and measurement of . transaction costs. It is essential for understanding the effectiveness of both the investment ideas and their implementation. In turn, this performance is an

 $^{2}$  Note that some of these different roles may be adopted the same person depending on the size of the organisation.

<sup>&</sup>lt;sup>3</sup> Salespeople are increasingly becoming sales/traders, able to route orders directly to trading algorithms.

important consideration when new investment strategies are formulated. For example, an investment opportunity worth 30 basis points may not be worth following up if previous transaction costs for similar orders have been around this level.

Historically, most of the early research on transaction costs focussed on post-trade analysis. Though, over the last few years pre-trade analysis has become ever more important. In particular, algorithmic trading is often reliant on pre-trade models in order to achieve more cost efficient execution.

In order to compare the various components of transaction costs, throughout this chapter we will use the following example trade.

**Example 6-1:** A decision to buy 50,000 of asset XYZ, its mid-price and our executions are all shown in Figure 6-4.

![](_page_3_Figure_5.jpeg)

Figure 6-4 A plot of trading price and executions for the order in Example  $6-1$ 

As we can see in Figure 6-4, the investment decision to buy XYZ is made when the price is at  $p_d$ , which happens to coincide with the previous day's closing price of 90. After analysis, an order to buy 50,000 is dispatched to a broker at time  $t_0$ , which (for simplicity) is filled by three separate child orders. The child orders execute at times  $t_1$ ,  $t_2$  and  $t_3$ . The first two executions are for 10,000 at an average price of 91.15 followed by 20,000 at 92.5, and are reasonably close to the best market price at those times. The third order, of 15,000, caused more impact and so achieved a poorer price of 93.8. Note that these example executions are just intended to help highlight the various types of transaction costs; they are not linked to any specific type of trading strategy or algorithm.

Immediately from Figure 6-4 we can see two distinct phases, the pre-trade period and the actual execution. The pre-trade period lasts from  $t_d$  to  $t_0$  when the order is dispatched to a broker, whilst the execution phase lasts from  $t_0$  to the order's completion, or in this case, the

day's close since the order is not fully executed. The strong price trend is also obvious, rising steadily, from opening at 90.5 to finally closing at 93.0.

The following sections provide a more comprehensive description of both pre and posttrade analysis, together with a detailed breakdown of how transaction costs are formed, using this example trade. For even more detailed coverage of transaction cost analysis it is well worth referring to 'Optimal Trading Strategies' by Robert Kissell and Morton Glantz (2003).

### 6.3 **Pre-trade analysis**

Pre-trade analysis is important to ensure that best execution is achieved. These analytics help investors or traders make informed decisions about how best to execute a given order.

Most brokers/vendors provide a considerable amount of general reference information. This may be as simple as the associated country and currency, or it may be more asset specific. For instance, for equities they may provide fundamental information such as the market capitalisation and the various investment ratios (e.g. price to carnings  $(P/E)$ , price to book (P/B)), together with any relevant sector and index data. Similarly, for bonds, they may provide the bond's yield and duration, as well as details of its credit rating, issue size and any relevant terms and conditions.

Table 6-1 outlines the data that is key to trading strategy selection. Essentially, this consists of prices, liquidity measures and data for risk analysis and cost estimates.

| Type           | Data                                                 |
|----------------|------------------------------------------------------|
| Prices         | Market prices, Price ranges, Trends/momentum         |
| Liquidity      | Percentage of ADV, Volume profile, Trading stability |
| Risk           | Volatility, Beta, Risk exposure                      |
| Cost estimates | Market impact, Timing risk                           |

## Table 6-1 A summary of key pre-trade analytics data

The liquidity and risk estimates highlight the expected difficulty of trading. The cost estimates give a reasonable indication of what might be achieved. This is particularly important for algorithmic trading, since it gives us an idea of how suitable the order is for a given strategy. Prohibitive risk or cost estimates mean that it is worth discussing the order directly with a broker or trader since manual execution may be the best option. In Chapter 7, we shall see how we can use these cost and risk estimates to try to select the optimal trading strategy for a specific order.

# Price data

A wide range of price data is useful for pre-trade analytics. The current market bid and offer prices, or a recent snapshot, act as a baseline for what we might achieve. The last traded price is also useful, particularly for illiquid assets, since this may be significantly different from the current quotes. The bid offer spread provides an estimate for the cost of immediacy. Historical average spreads allow us to gauge whether the current spread is unusual.

Price ranges, such as the difference between today's high and low prices, give an indication of the current price volatility. Likewise, benchmarks such as today's opening price or last night's close arc also useful. Trends may be reflected by daily, weekly or even monthly percentage changes.

# Liquidity data

Liquidity is closely related to transaction costs. Trading volume offers a simple way to rate the liquidity of a given asset. The average daily volume (ADV) is often calculated for the last 30 or 90 days. The percentage of ADV represents our order size as a fraction of this volume. Hence, we can gauge how difficult it may be to work any given order. For instance, anything less than 20-25% should be achievable within a day; however, anything over this could have a more significant effect on the market.

An estimate of the required trading horizon may be based on the ADV, together with a factor ( $\alpha$ ) which represents our desired trading rate:

$$Horizon = Size / (ADV * a)$$

For example, given an order size of  $50,000$  with an ADV of  $1,000,000$ , if we do not want to participate in more than 10% of the market volume then the required time is:

Horizon = 
$$50,000 / (1,000,000 * 0.1) = 0.5$$
 days.

At 10% participation, it could take us half a day to complete the order, whilst if we are only prepared to be 5% it could take the entire day.

Clearly, for such estimates to be reliable it is important that the actual trading volume closely matches the historical volume profile. Kissell and Glantz (2003) quantify this by adopting a coefficient of variation (CV), which is based on the standard deviation  $\sigma$  (ADV):

## $CV = \sigma(ADV) / ADV$

The trading stability is inversely related to this coefficient, so a high value of CV implies that sizeable variation from the historical average is possible.

Provided the trading activity is reasonably stable we can estimate what today's trading volume might be just by comparing the volume so far with the historical profile. If the market has only been open an hour and the days volume is 50% higher than the historical average then this may well continue for the rest of the day, in which case we need to resize the volume profile. Obviously, in such cases it is also important to check whether there is any news that may be driving this additional volume.

As we will see in Chapter 10, a range of factors can have an impact on the expected volumes. For instance, Kissell and Glantz (2003) note the importance of the day of the week for U.S. equities: Mondays generally see below average volumes whilst Wednesday and Thursdays see slightly above average ones.

The average trade size can also sometimes be useful, particularly if the order is to be worked manually. This acts as a simple guide to prevent signalling risk; if the order is significantly larger than the average trade size then it is worth splitting it or using hidden orders.

# Risk data

Volatility is a key variable for estimating how much risk we may be exposed to. It is based on the standard deviation of price returns, often for the last 3 or 6 months. As we have already seen, a high volatility implies a considerable amount of timing risk. Therefore, more aggressive trading strategies will generally be used to counteract this.

Market risk may be measured using an asset's beta, which is a measure of its sensitivity to market returns. A positive value means that the asset price moves in the same direction as the market whilst a negative one means it behaves in a contrarian fashion.<sup>4</sup> A beta of 1 means that the asset price moves in line with the market, so if the market as a whole drops 10% then the asset price will do the same. A beta of greater than 1 means the price response is magnified, so a beta of 2 would drop 20%, whilst a beta of 0.5 would only drop 5%. Note we shall cover other portfolio risk metrics in more detail in Chapter 12.

# Transaction cost estimates

Transaction cost models generally provide an estimate for the overall cost as well as detailing the major cost components such as market impact and timing risk. These are detailed in section  $6.5$ .

The basis for many transaction cost models is a framework suggested by Robert Almgren and Neil Chriss (2000). This uses a random walk model to estimate the current market price in terms of permanent market impact, price trending and volatility. Chapter 10 provides a more in-depth review of these cost-estimation models.

In terms of asset selection, given two assets with similar expected returns it is logical to trade the one that has the lower expected transaction costs. Exactly the same may be said for comparing various types of trading strategy, whether it is using a crossing system, a trading algorithm or DMA. Detailed pre-trade analysis is still required (to ensure the latest market information is incorporated in any decisions); however, historical cost data may certainly also be used to guide the selection decision.

Cost estimates are an important guide to the difficulty of an order. For instance, if the timing risk estimate is significantly larger than the market impact forecast then it is worth considering a more aggressive trading strategy. Conversely, a larger market impact may suggest adopting a more passive style. In Chapter 7, we will see how these decisions affect algorithm choice.

### Post-trade analysis 6.4

The historical results of post trade analysis act as a measure of broker/trader performance; they may also inform both investment and execution decisions.

Clearly, there is a lot more to transaction costs than fees and commissions. Past performance is therefore an important tool for comparing the quality of execution of both brokers and individual traders. Unbundling research fees has also made it easier for investors to link costs to the execution, and so use post-trade analysis to accurately compare broker performancc.

Breaking the costs down into their components allows us to see where and how the costs (or slippage) actually occurred. Detailed measurement helps to ensure that future efforts for cost reduction are focussed on the correct stage of the investment process. It may also be used to guide the execution method selection. For example, high timing risk and/or opportunity cost suggests that the trading may have been too passive.

# **Performance analysis**

How can we tell if a broker/trader is skilful or lucky? Similarly, how can we know whether a certain broker's VWAP algorithm performs better than another's? Performance analysis is an important tool for post-trade comparison of broker/trader/algorithm results.

Benchmark comparison is probably the most widespread tool used for performance

<sup>&</sup>lt;sup>4</sup> Note it can sometimes be hard to find assets with a negative beta (except over a short time period).

analysis. This simply means selecting an appropriate benchmark and then comparing the average execution price with it. In theory a good performer should, on average, match (or beat) the benchmark.

Still, benchmarks are not perfect; in particular, difficulties can arise when using them to compare performance across assets and over time. So after a brief review of the major benchmarks we shall also consider an alternative metric proposed by Robert Kissell (1998). This is the Relative Performance Measure (RPM), which assigns each trade a percentile ranking compared to the rest of the market. This makes it much easier to compare performance across a range of assets as well as over time. It can also allow for price trends and other market conditions.

# **Benchmarks**

A good benchmark should be easy to track and readily verifiable, it should also provide an accurate performance measurement. Table 6-2 shows the various benchmarks grouped in terms of when they may be determined.

| Benchmark               |                             | Results for Example 6-1 |                   |  |  |
|-------------------------|-----------------------------|-------------------------|-------------------|--|--|
|                         | Name                        | Benchmark               | Relative          |  |  |
| Type                    |                             | Price                   | performance (bps) |  |  |
| Post-Trade              | Close                       | 93.00                   | 37                |  |  |
|                         | Future Close ( $next day$ ) | 94.00                   | 137               |  |  |
|                         | OHLC                        | 92.00                   | -63               |  |  |
| Intraday                | TWAP                        | 92.20                   | -43               |  |  |
|                         | $\text{VWAP}$               | 92.40                   | -23               |  |  |
|                         | Previous Close              | 90.00                   | $-263$            |  |  |
| Pre-Trade               | Opening Price               | 90.50                   | $-213$            |  |  |
|                         | Decision Price              | 90.00                   | $-263$            |  |  |
|                         | Arrival Price               | 90.65                   | $-198$            |  |  |
| Average execution price |                             | 92.63                   | n/a               |  |  |

# **Table 6-2 Types of benehmark**

Post-trade benchmarks, such as the day's close, will not be known until after the trading has been completed. In comparison, pre-trade benchmarks, such as the previous close or the opening price, are known before the day's trading even commences. Intraday benchmarks, such as VWAP, need to be recalculated as the day progresses. For those that span the whole trading day, the definitive value will not in fact be known until trading has completed. Hence, trading with an intraday or post-trade benchmark usually requires some extra work. An interim value for the benchmark (intraday) or prediction (post-trade) will need to be maintained so that intraday performance may be monitored.

To allow comparison, the benchmark prices and performances from Example 6-1 are quoted separately in Table 6-2. For example, if we compare the average execution price to the closing price for our execution:

Close price  $= (92.63 - 93) * 45,000 = $16,500$  $= (16,500/4,500,000) = 0.37\% \text{ or } 37 \text{ bps (basis points)}$ 

To convert into basis points we can divide by the value of our overall order. Note that this was for  $50,000 \text{ XYZ}$  based on a decision price of 90 (rather than the 45,000 we executed).

These values may be viewed in turn to evaluate the performance of the example trade. Positive relative performances are good, therefore the example appears to have done well compared to the post-trade benchmarks. Conversely, it seems to have fared less well in terms of the intraday and pre-trade benchmarks. The following sub-sections outline each of the benchmarks in more detail.

Note that Example 6-1 has been specifically designed to highlight the different potential costs; hence, it has missed some of the benchmarks by over 200 basis points (bps). In section 6.6 we shall look at actual reported transaction costs from some of the world's markets.

## Post-trade benchmarks

Generally, these are based on closing prices, whether they are for the current trading day or for some time in the near future. Their popularity as a benchmark is due to the fact that the closing price is often used as a milestone for marking to market and for profit and loss (P&L) calculations. Future close prices may be used to retrospectively analyse performance. They provide a benchmark that is easy to determine and widely used. Though, in terms of a performance measure, they merely act as a milestone.

Markets tend to be more active at the close so prices are less reflective of actual market conditions throughout the day. In particular, if the asset's price is trending then orders completed earlier in the day will be compared with a benchmark price that is substantially different to that at the time of execution. Thus, an unfavourable price trend may make buy or sell orders look to have performed well; conversely, a favourable trend may make them appear to have performed poorly.

Post-trade benchmarks also tend to encourage trading closer to the end of the trading day. Unfortunately, the closing period is exactly when asset prices may be most sensitive to order flow, as demonstrated by Cushing and Madhavan (2001). This can expose an order to unnecessary timing risk and also to more volatile conditions. Whilst call auctions can reduce end of day volatility there can still be a considerable premium for traders requiring liquidity at the close.

For a trader or algorithm trying to track a post-trade benchmark, generally the goal will be to achieve (or beat) the closing price. Therefore, unless the trading strategy is simply to participate in the closing auction they will need to use a predicted price as a guideline. This price will need to be regularly updated, for instance, notice how the price trails off towards the close in Figure 6-4.

In terms of our example order, the price trend makes it appear to have performed well. The average price achieved for Example 6-1 is 92.63, beating the close by 37 basis points. Assuming the trend continues for the next day, to close at 94, means it performs even better versus this future close price. However, even better performance could have been achieved by tilting the execution towards the beginning of the day, when prices were lower. In terms of benchmarks, this only becomes evident by looking at the previous close price of 90. So although closing prices might be a popular benchmark, in isolation they are not the best means of performance analysis.

### Intraday benchmarks

These use average prices to try and more accurately reflect the intraday market conditions.

The OHLC (Open High Low Close) average has often been used as a proxy for the mean market price. Though, its popularity has waned as improved access to time and sales data has allowed more accurate calculations. Clearly, as an average of only four data points it may be easily distorted by extreme values.

The TWAP (Time Weighted Average Price) benchmark is an average of all the observed

trade prices over a set period. Equal weighting is given to all trades, so small trades at extreme prices can have a large effect on it. Generally, TWAP is used where trade volume data is not available.

The VWAP (Volume Weighted Average Price) benchmark arguably gives the fairest indication of how the market price has moved over the time span. This average weights each trade price by its corresponding size. The VWAP for a given period is the total traded value divided by the total traded quantity. Consequently, small trades at extreme prices will have much less effect; instead, the average will be dominated by the largest trades.

A trader or algorithm trying to track the TWAP or VWAP will need to frequently recalculate the benchmark price to incorporate new market information. Since post trade information has become more widely available VWAP has become one of the most popular benchmarks, due to the accuracy of its intraday performance.

The VWAP benchmark is not perfect, though, particularly for large orders. Institutional investors frequently need to trade large quantities, for example, consider trading an order equal to the average daily volume (ADV) of asset XYZ. The order would represent so much of the day's trading that the VWAP has practically no meaning in terms of performance. In fact, the same may be argued for anything over 30% of the ADV. Tracking the VWAP also tends to encourage trading to be spread out over time, reducing the overall market impact, but exposing the order to considerable price risk. For instance, let's assume half an order is worked throughout the first day, achieving an average price close to the current VWAP. Based on the benchmark, the performance so far is good, so the temptation is to leave the rest of the order for the next day. However, in terms of overall costs it may have been more advantageous to fully execute the order on the first day, despite any additional market impact. For assets which are volatile or for which there is a strong adverse price trend tracking the VWAP may even lead to poorer overall performance. Likewise, for small orders, it may not be appropriate to spread the execution out over a long time.

In terms of the performance for Example 6-1, the following table shows an aggregated view of the trading volumes throughout the day grouped by execution price.

| Price     | 90.50   | 91.00  | 91.50   | 92,00  | 92.50   | 93.00   | 93.50   | 94.00  |          |
|-----------|---------|--------|---------|--------|---------|---------|---------|--------|----------|
| Size      | 25,000  | 20,000 | 5,000   | 10,000 | 30,000  | 50,000  | 40,000  | 10.000 | 200,000  |
| # Trades  |         |        | 4       |        |         |         |         |        |          |
| Value \$k | 2,262.5 | .820.0 | 1,372.5 | 920.0  | 2,775.0 | 4,650.0 | 3,740.0 | 940.0  | 18,480.0 |

## Table 6-3 Aggregated price and volume data for Example 6-1

Using this data the intraday benchmarks may be calculated as:

| $OHLC = (90.5+94+90.5+93)/4$                     | $= 92.00$ |
|--------------------------------------------------|-----------|
| $\text{TWAP} = (5*90.50 + 3*91.00 + 2*91.50)/27$ | $= 92.20$ |
| $VWAP = (18,480,000/200,000)$                    | $= 92.40$ |

In comparison with the others, the VWAP benchmark best represents the average market conditions throughout the day. Its higher price corresponds to the greater impact from the increased trading volumes at 93 and 93.5. It is also lower than the closing price of 93, and so reflects the volume that was traded earlier in the day at lower prices.

In comparison to the post-trade benchmarks, the example order seems to have performed less well versus the intraday ones. The example order has missed the VWAP by 23 basis points. This is not that surprising given that the order was filled in three executions; especially since more was filled later in the day when the price had riscn. Given the trending price, it seems that more of the order should have been executed earlier in the day. Hence, the VWAP does indeed act as a reasonable performance benchmark.

## Pre-trade benchmarks

These are an immediately available milestone, which may be used to directly measure performance. The previous close and the opening price may both be used to determine trading costs. Although, just as for the post-trade benchmarks, the trading at these times may be more volatile and so they are not necessarily reflective of the actual market conditions throughout the day. A substantial price shift can also make the benchmark less meaningful for any subsequently entered orders, since they will be comparing to a price they could never have achieved.

The decision price represents the price at which the choice to invest was actually made, which ties in with Perold's concept of implementation shortfall. Arrival price is used in a similar fashion to the decision price, it represents the time at which the order could actually be traded. In the case of a broker, it is the time when the order arrives from the investor. This may then be used to measure what has sometimes been termed the execution shortfall, since unlike implementation shortfall it only tracks the trading-related costs.

Prc-trade benchmarks are appealing since they are both easily determined and immediately available for comparison. Whilst they do not reflect actual market conditions throughout the day, this may also be used as an advantage since it means there is no way to influence or "game" the benchmark. Another advantage is that they are just as appropriate for all order sizes.

Note that the decision and arrival prices are not always recorded by investors, so previous close and opening prices may be used as corresponding proxies for them. This will clearly affect the accuracy of the transaction cost measurement. In particular, it will affect the investment-related costs, often meaning these are underestimated.

The trade from Example 6-1 appears to have performed extremely poorly compared to the pre-trade benchmarks. This is caused by the noticeable price trend throughout the day. Lower transaction costs could have been achieved by completing more of the order earlier in the day.

## **Relative Performance Measure**

Kissell's (1998) Relative Performance Measure (RPM) is an alternative to price-based benchmarks. It is based on a comparison of what the trade achieved in relation to the rest of the market. In terms of volume, the RPM represents the ratio of the volume traded at a less favourable price to the total market volume:

$$RPM(\text{volume}) = \frac{\text{Total volume at price less favourable than execution}}{\text{Total market volume}}$$

 $RPM(\text{trades}) = \text{Number of trades at price less favourable than execution}$ Total number of trades

Transaction cost is dependent on many factors: the asset's characteristics (liquidity, volatility), market conditions (price trends, momentum), trading strategy etc. Therefore, when comparing the performance of two separate orders we need to take these various factors into account. Simply comparing how many basis points cach order beat the VWAP by does not give a fair comparison.

One of the main advantages of the RPM metric is the fact that its results are already

normalised, since the percentage rates the trade's performance compared to the rest of the market. Thus, a trade that achieves a 90% RPM has performed significantly better than one achieving 60%. This makes the RPM a useful tool for comparing the relative performance across a variety of hoth orders and assets, as well as over time.

Kissell proposes a range of adjustments for RPM to make it suitable for a wide range of trading strategies. Such as using time filtering to deal better with short trades, or adding weightings to incorporate the aggressiveness of the trading strategy. More details about the RPM may be found in Kissell and Glantz (2003).

Using the aggregated volume data from Table 6-3, the RPM's for Example 6-1 may be determined:

 $\text{RPM}(\text{volume}) = (50,000 + 40,000 + 10,000) / 200,000 = 50\%$  $\text{RPM}(\text{trades}) = (5 + 4 + 2) / 27 = 41\%$ Average RPM =  $45\%$ 

In other words, 50% of traded volume performed as well or better than the example order, whilst the remainder achieved a worse average price. This confirms that the example trade's performance is average at best.

## Post-trade transaction costs

The total transaction costs of a trade may be determined using Perold's implementation shortfall measure. This is the difference in value between the idealised paper portfolio and the actually traded one:

# IS=Returns<sub>Paper</sub> - Returns<sub>Real</sub>

The theoretical (or paper) returns depend on the price when the decision to invest was made  $(p_d)$ , the final market price  $(p_N)$  and the size of the intended investment (X). The real returns depend on the actual transaction costs. So if  $x_i$  represent the sizes of the individual executions and  $p_i$  are the achieved prices:

$$IS = \underbrace{X(p_N - p_d)}_{\text{Re}\text{turns}_{\text{Paper}}} - \underbrace{(Xp_N - \sum x_j p_j - fixed)}_{\text{Re}\text{turns}_{\text{Real}}} = \sum x_j p_j - Xp_d + fixed$$

Note that this assumes that the order is fully executed. To take account of this Robert Kissell and Morton Glantz (2003) introduced an opportunity cost factor, since not every order will be fully executed:

$$IS = \underbrace{\sum x_j p_j - (\sum x_j) p_d}_{\text{Execution Cost}} + \underbrace{(X - \sum x_j)(p_N - p_d)}_{\text{Opportunity Cost}} + fixed$$

where  $(X - \Sigma x_i)$  corresponds to the size of the unexecuted position.

So for Example 6-1:

Execution cost = 
$$(10,000*91.15 + 20,000*92.5 + 93.8*15,000) - (45,000*90.0)$$
  
= \$118,500  
Opportunity cost =  $(50,000 - 45,000) * (93.0 - 90.0)$   
= \$15,000  
Order value =  $50,000 * 90.0 = $4,500,000$ 

Implementation shortfall (IS) =  $$133,500 +$  lixed costs  $= (133,500/4,500,000) = 297 \text{bps} + \text{fixed costs}$ 

Wayne Wagner and Steven Glass (2001) also showed that transaction costs incorporate a delay factor. This corresponds to the effect of a price move from when the initial investment decision is made to when the order is actually sent for execution. So it may be shown that the overall costs consist of:

$$\text{Transaction costs} = \underbrace{X(p_0 - p_d)}_{\text{Investment related}} + \underbrace{\sum x_j p_j - (\sum x_j) p_0}_{\text{Trading related}} + \underbrace{(X - \sum x_j)(p_N - p_0)}_{\text{Opportunity Cost}} + \text{fixed} \tag{6-1}$$

where the price  $p_0$  is the market price when the order was dispatched, commonly known as the arrival price. Notice that the trading-related and opportunity costs now account for the change from this arrival price rather than the decision price.

Kissell and Glantz (2003) incorporated this into a measure they called the expanded implementation shortfall. This manages to not only account for transaction costs, but also helps to identify where the costs actually occurred. The following section shows how these costs may be broken down into factors such as spreads, market impact and timing risk.

#### Breaking down transaction costs 6.5

There has been a considerable amount of research focussed on trading costs. Most notable amongst these is a study by Wayne Wagner and Mark Edwards (1993) which split out the trading costs into specific components, namely timing, delay, impact and opportunity costs.

There are several different ways of classifying the constituents of transaction costs, as shown in Table 6-4.

|            | Classification   |              | Focus for:   |       |              |            |                      |
|------------|------------------|--------------|--------------|-------|--------------|------------|----------------------|
| Cost type  |                  | Explicit     | Implicit     | Fixed | Variable     | Algorithms | Execution<br>Tactics |
|            | Taxes            | $\checkmark$ |              |       | $\checkmark$ |            |                      |
| Investment | Delay Cost       | $\sqrt{5}$   |              |       |              |            |                      |
|            | Commission       | $\checkmark$ |              |       |              |            |                      |
|            | Fees             | $\checkmark$ |              |       |              | 0          | 0                    |
|            | Spreads          |              | 16           |       | /            |            |                      |
| Trading    | Market Impact    |              | $\checkmark$ |       | /            |            | 0                    |
|            | Price Trend      |              | $\checkmark$ |       | /            |            |                      |
|            | Timing Risk      |              | $\checkmark$ |       |              |            | 0                    |
|            | Opportunity Cost |              | $\checkmark$ |       |              | 0<br>r.    | $\sim$               |

• often  $\circ$  sometimes

## Table 6-4 Transaction cost constituents

<sup>&</sup>lt;sup>5</sup> Note that if the investment decision price  $(p_d)$  and the arrival price  $(p_0)$  are known then delay cost is explicit, but since one or both of these prices are often not recorded then it becomes a more implicit cost.

Although bid offer spreads are easily viewable, they must be recorded each time an order is split in order to determine the spread cost. So measuring it is similar to monitoring a price trends or market impact.

Differentiating between investment and trading related costs is useful since it helps identify who best can control them. Looking back at the trading example in Figure 6-4, the investment-related costs may be classed as everything which occurs before  $t_0$  (when the order is placed with the broker/trader) whilst the trading-related costs account for the rest.

Transaction costs are also commonly termed as either explicit or implicit. Explicit costs are clearly identifiable and easily measured, whereas implicit costs are less directly observable and so harder to quantify. Fixed costs are set regardless of the trading strategy whilst variable ones depend on the asset, the order, market conditions and the trading strategy. Another way of viewing these different cost types is shown in Figure 6-5. Note that although this is not drawn to scale, it does try to emphasise the relative importance of each type.

![](_page_13_Picture_3.jpeg)

Figure 6-5 Categorising transaction cost types

Pre-trade analysis tools allow both investors and traders to estimate these various transaction costs. This also helps make trading-related costs more transparent, and allows investors much more control over them. Investors should set clear targets for acceptable levels of cost and risk. Then by modelling a range of diverse trading strategies/algorithms, they may select the most appropriate approach. This is also a good way of reducing opportunity cost, since the analysis will highlight orders that may be too large. If an order does not appear to be viable, the investor may choose to consider other assets that are more liquid. Alternatively, if the order is not price sensitive then spreading it over several days may work. Note that most pre-trade analysis is based on historical data, so discussing with a trader can confirm current market conditions.

Clearly, the main aim is to achieve a reduction in the total transaction costs. The fixed commissions and fees may be reduced by negotiation. However, in terms of reducing overall cost, the most potential lies with the implicit and variable costs. The most important of which are trading-related, in particular market impact and timing risk. Generally, these are dependent on the asset, market conditions, the order and the trading strategy. By taking advantage of pre-trade analysis and algorithmic trading, investors can select trading strategies that are much more suitable for their overall investment goals. By choosing an appropriate trading strategy, the overall cost and risk should be considerably reduced.

A nice illustration of an in-depth transaction cost breakdown is provided by Instinct (2005). In order to compare the relative effects of the components Figure 6-6 shows a more detailed breakdown of the costs associated with Example 6-1. The following sub-sections provide more detailed descriptions for each of the individual cost components.

![](_page_14_Figure_1.jpeg)

Figure 6-6 Detailed transaction cost breakdown for Example 6-1

# Investment-related costs

Investment-related costs can be a significant proportion of the overall transaction costs. They primarily consist of a delay cost with taxes making up the rest. The delay reflects the time from the investment decision being made  $(t_{d})$  to when an order is actually dispatched  $(t_{0})$ . This is shown as the shaded region in Figure  $6-6$ .

# Taxes

Taxes must be incorporated into the investment strategy. Generally, they are applied based on capital gains; however, some markets such as the U.K. stock market have an additional stamp duty on share purchases.

# **Delay Cost**

The delay cost is caused by any price change from the initial decision to invest to when an order has actually been received by a broker. This may be specified as:

$$\text{Delay Cost} = X * (p_0 - p_d)$$

where X is the order size,  $p_d$  is the mid price when the investment decision was made (time

 $t_{\rm d}$ ) and  $p_0$  is the mid price at  $t_0$  when the order was received by the broker.

 $= 50,000 * (90.65 - 90.00)$ For Example 6-1: Delay Cost  $=$  \$32,500  $= 72 \text{ bps}$ 

Using the decision price benchmark, the example trade's performance was -293 bps. Therefore, for this example a quarter of the transaction costs are due to delay cost.

Such costs are clearly more important for assets whose price is trending away (i.c. up for buys and down for sells). Similarly, more volatile assets may also suffer.

Delay cost may be caused by a simple lag between the investment decision and issuing the order. Sometimes it may be inevitable, for instance, when the decision is made out of market hours. Time may also be spent on pre-trade analysis and choosing the most suitable broker, particularly for more illiquid assets and markets. Alternatively, if the buy-side trader has a strong view on the market this may cause them to wait for an optimal time. Nevertheless, if this judgement proves incorrect it will incur a delay cost.

The increasing availability of tools and systems for pre-trade analysis could help reduce this cost. Especially as they become more tightly integrated with order and execution management systems (OMSs and EMSs). Note there is no reason why the delay cost could not be broken down further. For example, market prices could be recorded at each stage of the process from the initial strategy and research through to portfolio formation.

# Trading-related costs

The explicit trading-related costs comprise of commissions and fees. Often these will be quoted in advance of trading as percentages of the traded value. Obviously, these may be reduced to a certain extent, based on negotiation between the investor and the brokers. The rates offered will usually depend on the client's volume of trading and the level of service they require.

The most significant costs are the implicit trading-related costs, primarily market impact and timing risk, but also spread, price trend and opportunity cost. Figure 6-6 shows the breakdown of these costs for our example buy order.

Market impact represents a payment for liquidity (or immediacy) and a cost due to the information content of the order. The price trend cost represents the added burden caused by a trending market. Timing risk is primarily associated with the volatility of an asset's price, as well as its liquidity. Spread cost is also included here since although being visible it is not always as easily measurable as fees or commissions. Finally, opportunity cost represents the risk from not fully executing the order, possibly because the trading strategy was too passive.

Note that for convenience the time related costs are grouped together as an overall timing cost in Figure 6-6, where:

$$\text{Timing Cost} = \text{Price Trend} + \text{Timing Risk} \tag{6-2}$$

Whilst these trading costs may not be eliminated, they may be controlled by selecting suitable trading strategies. Market impact costs are higher for aggressive trading whereas timing risk is higher for passive trading. Consequently, the trader needs to find the appropriate balance between impact cost and risk, and adjust the trading strategy accordingly. This selection also needs to take into account the specifics of each order together with the current market conditions and the investor's goal's and level of risk aversion. In Chapter 7, we will cover these decisions in more detail.

In terms of trading algorithms, Table 6-4 showed which cost components are generally focussed on. Clearly, market impact is a prime focus, but some algorithms will also closely monitor timing risk (e.g. implementation shortfall) and price trends. Execution tactics generally concentrate on spread costs, although some may also monitor price trends. Smart order routing systems and liquidity algorithms will also incorporate fees into their calculations when deciding the best venue to route orders to.

## Commission

Brokers charge commission for agency trading to compensate them for the costs (particularly labour and capital) incurred in handling orders, executing trades and performing clearing and settlement. Commission is generally quoted in basis points (bps). Though, in the U.S. equity markets quoting in cents per share (cps) is common.

Commissions have been steadily decreasing over time. Certainly, over a longer period commissions have fallen significantly. For instance, Hans Stoll (2001) noted that back in 1970 commissions for 500 shares of a \$40 stock were \$270, or 135 bps (54 cps). Whilst this was for a retail investor, even institutional investors paid around 65 bps (26 cps) on a 5000 share trade. Nowadays, in the U.S., commissions are often below ten basis points, particularly for DMA. Similarly, in the European equities marketplace a full service brokerage will probably charge around 20 bps, with algorithmic trading services costing around 10 bps and basic DMA even less than this.

Clearly, one way of reducing this cost is to compare the commissions for a wide range of brokers. Bear in mind, though, that commission is only one part of the transaction costs. A detailed comparison of all the associated costs is required to properly compare brokers.

## Fees

Fees represent the actual charges from trading. These may be from floor brokers, exchange fees, or clearing and settlement costs. Often brokers incorporate these into their commission charge. Note that some exchanges and ECNs assign costs only to aggressively priced orders in order to encourage liquidity provision. For instance, Table 6-5 highlights charges from BATS for September 2008.

| Fees (\$/share)    | Tape A<br>(NYSE) | Tape B<br>(Regional) | Tape C<br>(NASDAO) |
|--------------------|------------------|----------------------|--------------------|
| Adding liquidity   | $-0.0024$        | $-0.0030$            | 0.0024             |
| Removing liquidity | 0.0025           | 0.0025               | 0.0025             |
| Routing out        | 0.0029           | 0.0029               | 0.0029             |

Source: BATS (2008)

# Table 6-5 Sample Fees for using BATS (Sept 2008)

Notice how the charges for taking liquidity (i.e. aggressive orders) may be almost nullified by rebates offered for providing liquidity (i.e. passive orders). Some markets even provide multiple venues with different pricing schemes. For example, the Direct-Edge ECN provides EDGA where all orders pay a set fee, whilst EDGX offers the rebate style pricing where liquidity providers are compensated at the expense of liquidity takers.

Algorithms and execution tactics which deal with multiple execution venues are the most likely to track broker and exchange fees. They need this information when deciding between routing destinations to ensure they make a fair comparison of the real price.

## **Spreads**

Spread cost represents the difference between the best bid and offer prices at any given time. The spread compensates those who provide liquidity. Clearly, aggressive trading styles will result in a higher spread cost than passive ones.

The overall spread cost may be determined by summing the bid offer spreads for each execution. (A factor of  $0.5$  is used since we only pay half the spread for each trade):

$$Spread Cost = \sum (x_i * (0.5 * s_i))$$

where  $x_i$  is the size of each execution and  $s_i$  is the bid offer spread at that time. Note that this is the quoted spread at the time of each execution, rather than the effective spread, which also incorporates the immediate market impact.

In Example 6-1: Spread Cost  $=(10,000 * (91.1-91)) + (20,000 * (92.4-92.2))$  $+(15,000*(93.45-93.4))$  $=$  \$ 5,750  $= 13 \text{ bps}$ 

Spread costs vary considerably across both markets and assets. For some assets/markets, the spread can be a major cost factor. In the U.S. equity market, decimalisation sharply reduced spread cost to around 5 bps, although during the 2007-09 financial crisis spreads nearly doubled. In Europe and Japan spreads may be much higher, ranging from 10-50 bps or even more. Unsurprisingly, large-cap and liquid stocks have lower spreads. More volatile stocks tend to have higher spreads.

The simplest way to lower spread costs is to trade more passively, using limit orders which are priced at the market or just behind it. Algorithms may not always directly consider spread cost, although it may affect their choice of execution tactics (passive or aggressive). Most price-based execution tactics will closely monitor the spread in order to use an appropriate level of aggression when placing and updating orders.

### Market impact

Market impact represents the price change caused by a specific trade or order. Generally, it has an adverse affect, for instance, helping drive prices up when we are trying to buy.

The exact market impact cost is the difference between the actual price chart and the hypothetical one that would have occurred if our order had not been created. Though, this makes market impact difficult to measure and estimate accurately, as Kissell and Glantz (2003) observe. Figure 6-7 tries to show this effect for the order from Example 6-1; the hypothetical price chart is labelled as the "paper" one (borrowing from Perold's implementation shortfall nomenclature).

Market impact is usually broken down into temporary and permanent impacts:

$$Market Impact = Temporary Impact + Permanent Impact \qquad (6-3)$$

The temporary impact reflects the cost of demanding liquidity. For instance, an order that "walks the book" will usually achieve a poorer price than if it had just taken the quantity available at the best bid or offer.

Permanent impact corresponds to the long-term effect of our order, representing the information content that it has exposed to the market. Clearly, if the market detects a large buyer or seller this acts as a strong signal and will affect the price accordingly. A single, large order might have a larger temporary impact than a series of smaller orders. However,

![](_page_18_Figure_1.jpeg)

Figure 6-7 Potential impact cost for Example 6-1

netting the permanent impacts of the smaller orders will give a similar result to the signal given by the large order.

An approximate measure for market impact is to sum the total impacts for each order. The impact may be determined as the difference in price between our execution and the best bid or offer at that time (bid for sells and offer for buys):

$$\text{Market Impact} = \sum (x_i * (p_i - p_b)) \tag{6-4}$$

where  $x_i$  is the size of each execution and  $p_i$  is the price achieved for each execution and  $p_b$ is the best bid or offer at that time.

For example, let's consider one of the individual trades from Example 6-1 in more detail. Figure 6-8 shows a before and after view of the order book for the second execution at  $t_2$ .

| Buvs        |         |        | Sells |       |        |         | Sells |       |        |         |     |
|-------------|---------|--------|-------|-------|--------|---------|-------|-------|--------|---------|-----|
| ld          | Time    | Size   | Price | Price | Size   | Time    | ld    | Price | Size   | Time    | 1d  |
| $\text{B}1$ | 1:05:00 | 000, 1 | 92.0  | 92.4  | 10,000 | 1:05:00 | S1    | 92.4  | 10,000 | 1:05:00 | S1  |
| B2          | 1:00:25 | 3,000  | 91.9  | 92.5  | 7,000  | 1:00:25 | S2    | 92.5  | 7,000  | 1:00:25 | \$2 |
| B3          | 1:04:09 | 4,000  | 91.8  | 92.8  | 2,000  | 1:04:09 | S3    | 92.8  | 2.000  | 1:04:09 | S3  |
|             |         |        |       | 92.9  | 3,000  | 1:05:00 | S4    | 92.9  | 1,000  | 1:05:00 | \$4 |
|             |         |        |       |       |        |         |       | 92.9  | 2.000  | 1:05:00 | S4  |

(a) before

|               |         | Buys  |       |       | Sells |         |    |
|---------------|---------|-------|-------|-------|-------|---------|----|
| ld            | Time    | Size  | Pricc | Price | Size  | Time    | 1d |
| B6            | 1:07:00 | 1,000 | 92.1  | 92.5  | 5,000 | 1:08:00 | S5 |
| $\mathbf{B5}$ | 1:08:00 | 2,000 | 92.1  | 92.6  | 4,000 | 1:09:00 | S6 |
| $\text{B1}$   | 1:05:00 | 1,000 | 92.0  | 92.9  | 2,000 | 1:09:10 | S7 |
| B2            | 1:00:25 | 3,000 | 91.9  | 92.9  | 5,000 | 1:08:00 | S8 |

(b) immediately after

 $(c)$  5 minutes later

## Figure 6-8 A view of the order book for trade $t_2$ from Example 6-1

By issuing a market order to buy 20,000 XYZ, we can see that this will "walk the book", crossing with sell orders S1, S2, S3 and S4. So we receive fills of 10,000 at 92.4, 7,000 at 92.5, 2,000 at 92.8 and 2,000 at 92.9, achieving an average price of 92.5. The temporary effect of the trade has been to shift the offer price up to 92.9. Though, within a few minutes new orders arrive which stabilise the offer price back to 92.5. The permanent impact, caused by our trade, helped shift the offer price from 92.4 to 92.5. Our order acted as an indication that the asset was undervalued and so helped raise the price permanently, as we can see in Figure 6-9.

![](_page_19_Figure_2.jpeg)

Figure 6-9 The components of market impact

The overall impact for Example  $6-1$ , using equation  $6-4$ :

 $=(10,000 * (91.15-91.1)) + (20,000 * (92.5-92.4))$ Market impact  $+(15,000*(93.8-93.45))$  $=$  \$7,750  $= 17 \text{ bps}$ 

Breaking this down into its temporary and permanent components is a bit more difficult. Some cost estimation models actually set the permanent impact as zero, assuming that the trade will not have a significant overall effect. Still, we can make an approximation by using the estimation model from Kissell and Glantz (2003). <sup>7</sup> First, the instantaneous impact cost  $I_{s}$ is determined by rearranging their estimation equation as follows:

$$MI_{\$} = 0.95I_{\$} \cdot \eta^{-1} + 0.05I_{\$} \Rightarrow I_{\$} = \frac{MI_{\$}}{(0.95\eta^{-1} + 0.05)}$$
(6-5)

where  $\eta = (X + 0.5 * Q) / X$ , and X is the order size, Q is the ADV.

Hence 
$$\eta$$
 = (45,000 + (0.5 \* 200,000)) / 45,000 = 3.22  
 $I_{\$}$  = \$ 7,750 / ((0.95 / 3.22) + 0.05)  
= \$ 22,475  
= 50 bps

<sup>&</sup>lt;sup>7</sup> Note the Kissell and Glantz (2003) market impact estimation model is discussed in more detail in Chapter 10.

This instantaneous impact cost may then be fed back into the first part of equation 6-5 to determine both the temporary and permanent impact costs:

| Temporary Impact | $=(0.95 * $22,475) / 3.22$<br>$=$ \$6,626<br>$= 15 \text{ bps}$ |
|------------------|-----------------------------------------------------------------|
| Permanent Impact | $= 0.05 * $ 22,475$<br>$=$ \$ 1,124<br>$= 2 \text{ bps}$        |

Overall market impact is dependent on the order/trade size, but most importantly on the market liquidity. Generally, larger orders incur a higher market impact compared to smaller ones. Though, this effect is considerably reduced for more liquid assets.

As we saw in Chapter 5, reducing market impact cost has been one of the primary aims of algorithms since the earliest order slicing approaches. By taking a large order and splitting it into smaller ones, which are traded over a period of time, we should achieve a much lower overall impact cost. Many of the currently available algorithms directly incorporate this factor into their decisions of how and when to place orders. The aggressiveness of execution tactics also has an effect on the market impact costs. Issuing market orders or aggressive limit orders will incur higher costs. Some tactics may actually use limit order models to decide on the appropriate level of aggression.

# **Price trending**

Asset prices sometimes exhibit broadly consistent trends. This price drift, or momentum, is also known as short-term alpha. An upward trend implies that costs will increase when buying an asset, whilst savings will be made if selling. Conversely, the opposite is true for a downward price trend.

The price trend cost may be determined based on the difference between this trend price and the arrival price:

Price Trend Cost = 
$$\sum (x_j * (p_j^* - p_0))$$

where  $x_j$  is the size of each execution,  $p_j^*$  is the expected price based on the price trend and  $p_0$  is again the mid price at  $t_0$  when the order was received by the broker.

For simplicity, in Example 6-1 the trend line has been set to cross between the previous close and the days OHLC average. This is shown on as the dashed line on Figure 6-6. Interpolation gives the following trend prices:

| Trade       |       |           |       |
|-------------|-------|-----------|-------|
| Mid price   | 91.00 | 92.20     | 93.40 |
| Trend price | 90.50 | .00<br>01 | 91.60 |

## Table 6-6 Trend prices for Example 6-1

So: Price Trend Cost = 
$$(10,000 * (90.5-90.65)) + (20,000 * (91-90.65))$$
  
+  $(15,000 * (91.6-90.65))$   
= \$ 19,750  
= 44 bps

Note this simplistic trend may have given a higher trend cost measurement; however, this will not affect the overall transaction cost measurement. Since timing cost is the sum of trend cost and timing risk, if the trend cost is overestimated then the timing risk will be underestimated by an equivalent amount.

For our example, the timing cost may be determined from the difference between the mid price  $(m_i)$  and the arrival price  $(p_0)$ .

$$\text{Timing Cost} = \sum (x_i * (m_i - p_0))$$

Reducing trend cost may really only be achieved by shortening the trading horizon and so increasing market impact costs. For large orders, which may span multiple days, investors must use pre-trade analysis to find the optimal trading approach to balance both these costs.

Price trending is a focus for the price-sensitive algorithms, such as implementation shortfall and market on close. In particular, the adaptive shortfall and price inline algorithms actively respond to trends either aggressively or passively. That said, schedule based algorithms may also be modified to cope with price trends. Some variants of TWAP and VWAP allow parameters to specify how to tilt their schedules based on which way the trader thinks the price may trend. Some execution tactics may also become more or less aggressive if they detect short-term market trends.

## Timing risk

Kissell and Glantz (2003) use timing risk to represent the uncertainty of the transaction cost estimate. The two main sources of uncertainty are volatility of both the asset's price and of the traded volume, although other factors such as spread risk could also be considered. For the purposes of this book, timing risk will simply be reduced to the sum of these two main risks together with a generic error factor ( $\varepsilon$ ):

$$\text{Timing Risk} = \text{Volatility Risk} + \text{Liquidity Risk} + \varepsilon$$

Price volatility is arguably the most important risk. The more volatile an asset then the more likely its price will move away and so increase the transaction costs. The liquidity risk represents the uncertainty with respect to the market impact cost. Generally, market impact costs are estimated based on historical volumes, so if the actual trading volumes differ significantly this may result in a shift in the market impact. For instance, if the market volume is higher then the market impact costs will tend to be less.

Based on the calculation for timing cost shown in the previous sub-section, timing risk is effectively the residual cost once the price trend has been accounted for. Hence, timing risk may be measured using:

Timing Risk = 
$$\sum (x_j * (m_j - p_j^*))$$

where  $x_j$  is the size of each execution,  $m_j$  is the mid price at this time and  $p_j^*$  is the expected price based on the price trend.

For Example 6-1, using the mid and trend prices from Table 6-6:

 $=(10,000 * (91-90.5)) + (20,000 * (92.2-91))$ Timing Risk  $+(15,000*(93.4-91.6))$  $=$  \$ 56,000  $= 124 \text{ bps}$ 

Clearly, this order has been considerably affected by timing risk. Shortening the trading horizon should reduce the effect. So investors must find an appropriate balance between market impact costs and timing risk.

Timing risk is a focus for the risk based algorithms, namely implementation and adaptive shortfall as well as market on close. Most execution tactics do not directly incorporate timing risk, although some may become more aggressive as time goes on, to try to complete any extant orders. Similarly, when an aggressive execution style is set by an algorithm this will somewhat reduce timing risk by preventing the algorithm from lagging behind their trading targets. Though, this only ensures completion of the dispatched child orders. An aggressive VWAP algorithm will still schedule its orders based on a historic volume profile, so orders will still he spaced out over time.

## Opportunity cost

Opportunity cost reflects the cost of not fully executing an order. This may be because the asset's price went beyond a client's price limit or could just be due to insufficient liquidity. Either way, it represents a missed opportunity, since the next day prices may move even further away.

The overall cost may be determined as the product of the remaining order size and the price difference between the final price  $(p_N)$  and the arrival price:

$$OC = (X - \sum x_j)(p_N - p_0)$$

Unlike the other cost components, opportunity cost represents a virtual loss rather than a physical one. The loss is only realised when a new order makes up the remainder at a less favourable price.

So for Example 6-1: Opportunity Cost  $=(50,000 - 45,000) * (93.0 - 90.65)$  $=$  \$11,750  $= 26 \text{ bps}$ 

If the price trend reverts tomorrow then it should be easy to purchase the remaining  $5,000$  $XYZ$  at less than 93.0. If the trend continues then an opportunity cost of at least 26 bps will be realised.

Reducing opportunity cost may really only be achieved by using pre-trade analysis to confirm orders are sized correctly for current market conditions. For large orders, the investor must decide whether to risk market impact, or spread the trade over several days, risking exposure to a price move. Setting price limits effectively signifies that opportunity cost is acceptable (so long as it is due to the market moving to an unfavourable price). For such orders sudden price shifts can stop the order from being executable. Good communication between the investor and traders is vital to allow modification of the trading strategy if necessary.

Some algorithms may directly consider opportunity cost; typically, this is the cost-based ones such as implementation shortfall. Still, it is important to use pre-trade analytics to ensure the asset's liquidity is sufficient for the proposed order. Opportunity cost is also addressed indirectly by the optional finish-up logic provided by brokers/vendors for some algorithms. This is primarily intended to complete orders that may have an odd lot remainder.

## Summary

The previous sections have outlined each of these individual transaction cost components in some detail. Figure 6-6 gave a visual breakdown of the constituent costs for Example 6-1. These are summarised in the following table.

| Type               | Cost \$ | Cost bps | % of costs |
|--------------------|---------|----------|------------|
| Taxes <sup>8</sup> |         |          |            |
| Delay cost         | 32,500  | 72       | 24         |
| Commission/Fees    | 4,500   | 10       | 3          |
| Spread cost        | 5,750   | 13       |            |
| Market impact      | 7,750   | 17       | 6          |
| Price trend        | 19,750  | 44       | 14         |
| Timing risk        | 56,000  | 124      | 41         |
| Opportunity cost   | 11,750  | 26       | Q          |
| Total              | 138,000 | 307      | 100        |

| Table 6-7 Cost Estimate for Example 6-1 |
|-----------------------------------------|
|-----------------------------------------|

Thus, the overall cost is 10 bps more than the 297 bps implementation shortfall we calculated earlier. This is because the initial implementation shortfall calculation did not take into account commissions/fees (or taxes).

Note it is also different from the 263 bps underperformance we saw back in Table 6-2 using the decision price benchmark. This is because the benchmark only shows the performance for the executed trades, and not the 5,000 which did not execute. So it does not include the opportunity cost. This is why implementation shortfall is an important (and accurate) tool for post-trade analysis, and can be more useful than benchmarks.

In terms of individual cost components, clearly delay cost and timing risk are important cost factors in this example. Market impact cost is also significant. Our estimate for the instantaneous impact cost was 50bps. For this order, market impact has been reduced by splitting into several smaller orders. Though, with hindsight, much better performance could have been achieved by trading more aggressively at the start of day. Admittedly, the market impact costs would have been higher, but the timing risk and price trend cost would have been much less.

It is important to remember that Example 6-1 was specifically designed to highlight the various potential costs. Obviously, the trading strategy was sub-optimal. In Chapter 7, we shall address the selection of optimal trading strategies in more detail. For more realistic costs, the following section shows figures reported for some of the world's major markets.

#### 6.6 Transaction costs across world markets

Having gone through a worked example to illustrate each of the main components of transaction costs it is worth seeing how these actually differ across the world's markets. A few vendors provide transaction cost analysis (TCA) which is truly global in scope. In general, these have been focussed on the equities markets, although they are also starting to cover other asset classes. Table 6-8 shows average transaction costs for global equity trading taken from quarterly cost reviews carried out by ITG Inc. for both 2007 and 2008.

 $8$  For simplicity taxes are assumed to be zero (we will assume it is a charitable account).

| Region                                                                                                                                                                                                                                                                                    | Average Cost<br>in <i>O4</i> 2008 /bps |      |       | Average Cost<br>in <i>O2</i> 2007 /bps |        |      |       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|------|-------|----------------------------------------|--------|------|-------|
|                                                                                                                                                                                                                                                                                           | Shortfall                              | Comm | Total | Delay                                  | Impact | Comm | Total |
| U.S. (Combined)                                                                                                                                                                                                                                                                           | 76                                     | 9    | 85    | 20                                     | 11     | 7    | 38    |
| U.S. (Large Cap)                                                                                                                                                                                                                                                                          | 54                                     | 8    | 62    | 19                                     | 10     | 6    | 35    |
| U.S. (Small Cap)                                                                                                                                                                                                                                                                          | 124                                    | 12   | 136   | 27                                     | 13     | 10   | 51    |
| U.K.                                                                                                                                                                                                                                                                                      | 73                                     | 12   | 84    | 31                                     | 4      | 11   | 46    |
| Europe ex U.K.<br>(Austria, Belgium, Denmark, Finland,<br>France, Germany, Greece, Ireland,<br>Italy, Luxembourg, Netherlands,<br>Norway, Portugal, Spain, Sweden,<br>Switzerland)                                                                                                        | 66                                     | 11   | 77    | 37                                     | 6      | 11   | 54    |
| Japan                                                                                                                                                                                                                                                                                     | 111                                    | 9    | 120   | 39                                     | 16     | 8    | 63    |
| Developed Asia<br>(Australia, Hong Kong, Malaysia, New<br>Zealand, Singapore)                                                                                                                                                                                                             | 113                                    | 15   | 128   | 95                                     | 16     | 14   | 125   |
| All Emerging<br>(Argentina, Brazil, Chile, Chile, China,<br>Colombia, Cyprus, Czech Republic,<br>Egypt, Hungary, India, Indonesia,<br>Israel, Jordan, Mexico, Morocco,<br>Pakistan, Peru, Philippines, Poland,<br>Russia, S. Korea, South Africa, Sri<br>Lanka, Taiwan, Thailand, Turkey) | 128                                    | 21   | 148   | 80                                     | 12     | 20   | 112   |

Source: ITG (2009, 2008)

## Table 6-8 Average transaction costs for global equities

Unsurprisingly, the costs are closely related to market liquidity, so the lowest costs are for U.S. large cap firms, followed by Europe and Japan. Comparing the differences between 2007 and 2008, it is clear that during the market turmoil costs rose sharply, particularly in the more developed markets. In fact, Tahle 6-8 shows that transaction costs doubled from Q2 2007 to Q4 2008 for the ITG U.S. combined figures, mainly due to a massive increase in costs for small cap equities. Similarly, the U.K. and Japan saw cost increases of over 50%, whilst European markets saw around a 22% increase.

Table 6-8 also shows a breakdown of these costs. For 2007 the delay cost, market impact and commissions (labelled Comm) are shown, whilst for 2008 the shortfall cost represents the sum of the delay and market impact. Again, market impact costs are generally lower in the largest and most developed markets. The delay cost seems to be most important for the Asian markets, Commissions tend to be lowest in the US and Japan, followed by Europe then the rest of Asia.

Transaction cost analysis has seen a slower uptake for other asset classes. A lack of transparency has been one of the key difficulties with dealer driven markets like fixed income. Clearly, for transaction cost analysis to be useful we need access to price data in order to accurately determine market impact, spread and delay costs. Still, the situation is gradually improving with the increasing adoption of electronic trading for these asset classes.

In the fixed income marketplace, several TCA vendors now offer global cost reports. For example, Table 6-9 shows some average costs from reviews by Elkins/McSherry for 2007/8. Fixed income markets also saw significant cost increases during the 2007-09 financial crisis. Note the sample costs shown in Table 6-9 do not give a breakdown into their individual

| Country     | Average cost / bps<br>Q4-Q1 2007-8 |
|-------------|------------------------------------|
| Greece      | $\sim 9.1$                         |
| UK          | $-5.3$                             |
| Netherlands | $\sim 9.5$                         |
| Japan       | $\sim 5.5$                         |
| Hong Kong   | $\sim 11.1$                        |
| Singapore   | $\sim 12.0$                        |
| Malaysia    | $\sim 14.0$                        |
| Mexico      | ~7.2                               |
| Turkey      | $\sim 16.0$                        |

| U.S. bonds | Average cost / bps<br>2007 |
|------------|----------------------------|
| Treasury   | 5.87                       |
| Agency     | 6.73                       |
| Municipal  | 11.32                      |
| Mortgage   | 5.23                       |
| Corporate  | 6.97                       |

Source: Elkins McSherry (2008, a)

## Table 6-9 Average transaction costs for global bond trading

components, although they are noticeably lower than the figures reported for equities. However, there can also be a substantial cost associated with volatility, as shown in a proof of concept study of over 25,000 State Street bond portfolios reported in Pensions & Investments (2003). A volatility cost of 22 bps was found for trading in Japanese bonds, 47 bps for German ones, 53 bps in the U.S. and up to 62 bps in the U.K. This additional cost brings the figures more in line with equities, and may be seen as delay costs or timing risk.

For foreign exchange, the sums involved mean a few basis points can mean millions, so transaction cost analysis could bring considerable benefits to investors and traders. A review of FX specific transaction cost analysis by Michael DuCharme (2007) notes an average cost of around 9 bps, based on a study of FX trading by the Russell Investment Group. The dataset consisted of more than 36,000 trades for both developed and emerging currencies, worth around \$15 billion. One interesting problem they faced was a lack of time stamps for their data. Simple omissions like this can pose real problems for TCA. Outside of the major systems from Reuters and EBS, some vendors are starting to provide multi-broker aggregated price feeds, helping tackle the issue of sourcing sufficient price data. Although daily price fixings still provide a key benchmark for many users.

There are also signs of TCA spreading into listed derivatives. Hopefully, the adoption of TCA will continue to grow, allowing us to monitor the efficiency of these markets.

#### 6.7 Summary

- Transaction costs can have a significant effect on investment returns; therefore, it is important to both measure and analyse them if "best execution" is to be achieved.
- Implementation shortfall, or "slippage", is the difference in performance between an actual portfolio and its theoretical "paper" equivalent.
- Pre-trade analysis concentrates on estimating the:
  - Expected difficulty of trading, using forecasts from liquidity and risk models.

- Potential transaction cost. This helps show how suitable a given trading strategy is.
- in. Post-trade analysis focuses on execution performance and cost measurement.
  - \_ Benchmark comparison is still one of the most common tools:
    - Closing price benchmarks are popular since they are used for P&L calculations.  $-$
    - Intraday benchmarks, such as VWAP, reflect the market conditions.
    - The decision price gives the closest estimate for implementation shortfall.
  - Alternative metrics, such as Kissell's RPM, may be used to compare performance across a range of assets as well as over time.
- Transaction costs may be decomposed into a wide range of different components:
  - Commissions, fees and taxes represent charges levied by floor brokers and exchanges as well as any costs associated with clearing and settlement.
  - Spread cost represents the compensation traders require for providing liquidity.
  - Delay cost reflects any price changes between the initial decision to invest and when an order is actually sent for execution.
  - Market impact represents the effect the order has on the asset's price (both temporary and permanent).
  - Timing risk reflects volatility in both the asset's price and its liquidity.
  - Opportunity cost represents the missed opportunity if an order is not completed.
- Transaction cost analysis is spreading across asset classes. Costs are closely related to market liquidity and volatility, so it is often cheaper to trade in the U.S. followed by Europe and Asia.
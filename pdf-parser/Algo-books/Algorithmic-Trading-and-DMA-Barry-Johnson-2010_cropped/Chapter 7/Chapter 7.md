![](_page_0_Picture_1.jpeg)

Selecting the best trading strategy for any given order is a case of carefully balancing the investment objectives with market conditions.

#### Introduction 7.1

Best execution has become an increasingly commonplace term of late. Market regulators are trying to put in force rules and guidelines to ensure that client orders are executed with the most favourable terms, based on their objectives and on market conditions. Clearly, the overall transaction cost is a key component to best execution. Therefore, it is important to note that the speed of execution (reflecting timing risk) and its completeness (reflecting opportunity cost) can have as much significance as price.

Unfortunately, there are no hard and fast rules for how to achieve best execution. The judgement depends on factors such as the choice of benchmark and the investor's level of risk aversion, as well as their overall goals.

So how do we go about determining the optimal trading strategy for a given order? We will start by examining an example trading decision framework, as described by Wayne Wagner (2006) and shown in Figure 7-1. This framework illustrates the process from the point of view of a buy-side trader:

## Step

- A portfolio manager initially notifies them of the order. 1.
- 2. If there are any specific restrictions then the trader must use the designated broker.
- 3. Otherwise, the trader must assess how difficult the order will be to trade.
- 3.1 For orders that will provide much needed liquidity to the markets, the trader should strive for the optimal price.
- 3.2 Similarly, for orders that are judged easy, the trader has a lot of leeway in how best to deal with them.
- 3.3 Tough orders may be sub-categorised based on whether:
  - They are a large percentage of the average daily volume (ADV). 0
  - The asset is exhibiting significant trading momentum.  $\circ$
  - The investor has flagged the order as urgent. ο

Depending on the perceived difficulty, the trader then must select the most appropriate method of trading. This may mean using trading algorithms, DMA, trying to cross the order, or negotiating a principal transaction with a dealer.

![](_page_1_Figure_1.jpeg)

Source: Wagner (2006)

Reproduced with permission from Institutional Investor

![](_page_1_Figure_4.jpeg)

#### 7.2 Assessing the difficulty of orders

Determining how difficult an order will be depends on a range of properties. Wagner (2006) points out three such factors, namely large orders (relative to the ADV), unfavourable price momentum and urgency. Conversely, the key feature that makes trading easy is liquidity. Other asset specific properties such as volatility can also have a substantial effect.

One way of quantifying the potential order difficulty is based on historical results from transaction cost analysis (TCA). For example, Figure 7-2 shows the results of a proprietary liquidity and impact cost analysis performed by Jacqueline King and Yan Yaroshevsky  $(2005)$  at Abel/Noser. They studied the realized costs for a sample of 1,500 equities across a range of different order sizes (shown as a percentage of the ADV). Let's examine each of these key factors in turn:

## Order size:

A large order executed immediately will generally cause significant market impact. Anything over 20-25% of the ADV is a large trade and so is more difficult, whilst anything less than 1% is a small trade. Still, as we can see in Figure 7-2 the effect of order size is closely linked to the asset's liquidity. A large order for a highly liquid asset will tend to cause much less market impact than for an illiquid one.

![](_page_2_Figure_1.jpeg)

Figure 7-2 Realized costs for different asset groups

## Liquidity:

An asset's liquidity can also have a considerable effect on transaction costs, as Figure 7-2 shows. A lower bid offer spread is commonly associated with liquid assets, so the expected spread cost should be lower for these. For equities, the company's market capitalisation and turnover may be used as a proxy for liquidity. In the Abel/Noser study, the market capitalisation ranged from \$100 million to \$100 billion. A large-cap stock has a value of greater than \$10 billion, a small-cap is below \$1 billion and a micro-cap has a value under \$100 million. Likewisc, a higher relative turnover means the stock is more liquid, so again we would expect lower impact costs.

## Volatility:

An asset's volatility affects both its expected cost and timing risk. When combined with liquidity it can have a massive effect on the overall costs. For instance, in Figure 7-2 there is a huge jump in costs for equities which were illiquid with a high volatility (from around 400-1200 bps) when compared to those which were highly liquid with a low volatility (from around 10-40 bps).

#### Price momentum:

A persistent and favourable price trend also makes trades easier. Still, the key to reducing costs is trading more passively so as to take advantage of the trend. Conversely, a persistently adverse trend favours aggressive trading, so any delay will simply result in even worse executions.

#### Urgency:

Trading aggressively over a small time horizon will often cause significant market impact. The key is to determine whether this is outweighed by factors such as price momentum or volatility. Either way, aggressive trading will probably be required to meet the trading goals.

#### Trading horizon:

The trade horizon is closely linked with the urgency. Comparing the order size to the ADV assumes that the trade horizon is for the entire trading day. So a shorter trading horizon can make executing the order more difficult. For instance, an order for 10% of the ADV received two hours before the close is much more difficult to trade than its order size alone might suggest.

Other factors can also have an effect. For example, Scott Lyden (2007) reported on the importance of the time of day, noting that market impact for U.S. stocks was higher for trading in the first half hour after the open.

#### Selecting the optimal trading strategy 7.3

Having gauged the difficulty of the order, we now need to determine the best way to execute it. Since the concept of best execution revolves around achieving the investor's objectives, it is vital that these are considered. Therefore, we also need to know the:

- intended benchmark
- level of risk aversion
- $\bullet$ desired trading goals

These will have a significant impact on our choice of strategy. Though, before we cover each of these factors in more detail, we must first explain a concept known as the efficient trading frontier. This provides the basis for comparing the expected costs and risks associated with different trading strategies, and so is a key part of the decision process.

## The efficient trading frontier

In Chapter 1, we saw the efficient frontier for portfolios proposed by Harry Markowitz (1952). This plots the optimal portfolio in terms of returns for different levels of risk (or volatility). However, trading strategies are generally more focussed on cost, so Robert Almgren and Neil Chriss (2000) proposed the efficient trading frontier. They reasoned that rational traders would always seek to minimize expected costs for a certain level of risk. Hence, an optimal trading strategy was defined as one for which there were no alternatives with lower expected costs for the same degree of risk. The set of optimal solutions were termed the efficient trading frontier, consisting of a single solution for every possible level of risk. In order to determine this frontier they sought to solve the following unconstrained optimization for the expected cost  $E(x)$ :

$$\min_{x} (E(x) + \lambda V(x)) \tag{7-1}$$

where  $V(x)$  corresponds to the expected risk and  $\lambda$  is a Lagrange multiplier introduced to relate to the various levels of risk. By plotting the optimal solutions on a chart of expected cost (or loss) against its corresponding variance (as a proxy for risk), as shown in Figure 7-3, the convex nature of the efficient trading frontier may clearly be seen.

The shaded region in Figure 7-3 represents the set of all possible strategies, whilst the

solid curve shows the actual efficient trading frontier. Each point on this curve represents an optimal solution for a specific value of  $\lambda$ . In terms of cost, strategy B has the lowest expected value, although focussing on minimising this has resulted in the highest risk of any of the optimal strategies. Note that the dashed curve highlights strategies for which there is an optimal alternative with both lower expected cost and risk, namely strategy B.

![](_page_4_Figure_2.jpeg)

Source: Almgren and Chriss (2000) Reprinted with kind permission from The Journal of Risk, Incisive Media

#### Figure 7-3 An efficient trading frontier

Based on equation 7-1 the gradient of the curve in Figure 7-3 corresponds to  $-\lambda$ , so the tangent shows the optimal strategy for  $\lambda$  with a value of around  $10^{-6}$  (marked with a circle). In financial terms, the risk multiplier  $\lambda$  corresponds to the level of risk aversion. A higher value signifies less willingness to accept possible variance and so infers a higher expected cost. In other words, a higher risk aversion implies more aggressive trading. Conversely, a lower value of  $\lambda$  means less risk aversion; more passive trading results in lower expected costs, but with a higher variance. Thus in Figure 7-3 strategy A corresponds to a more aggressive strategy, whilst strategy  $B$  is the most passive optimal strategy.

Note that although variance is used in Figure 7-3 other risk measures may also be adopted. For instance, Almgren and Chriss (2000) also created a version for Value at Risk (VaR) whilst Robert Kissell and Roberto Malamut (2005b) normalised the frontier by plotting both cost and risk in terms of basis points.

Although the efficient trading frontier is an extremely useful theoretical concept, creating them can be time consuming since it requires the solution of the optimisation shown in equation 7-1 for every reasonable value of  $\lambda$ . To make things easier, Robert Kissell and Morton Glantz proposed an approximation by fitting an exponential decay curve to just a few specific strategies. More details may be found in Kissell and Glantz (2003).

# Choosing the benchmark

As we saw in Chapter 6, the benchmark can have a substantial effect on the accuracy of performance measures. A similar result may be observed for the efficient trading frontiers, as highlighted in a study by Kissell and Malamut (2005b), shown in Figure 7-4. The expected costs and risks for each of these benchmarks are given in Table 7-1. We will cover the actual cost estimation models in more detail in Chapter 10.

![](_page_5_Figure_3.jpeg)

# **Timing Risk**

Source: Kissell and Malamut (2005b)

Reproduced with permission from Institutional Investor

Figure 7-4 The efficient trading frontier for a range of different benchmarks

| Bench-<br>mark                           | Cost                                                             | Risk                                                                       |
|------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------|
| Previous<br>Closing/<br>Opening<br>Price | $Cost(\alpha) = h(X, \alpha) + g(X) + (p_0 - p_d) + \varepsilon$ | $\Re(\alpha) = \sqrt{\sigma^2(\varepsilon(\alpha)) + \sigma^2(p_0 - p_d)}$ |
| Arrival<br>Price                         | $Cost(\alpha) = h(X, \alpha) + g(X) + \varepsilon$               | $\Re(\alpha) = \sigma(\varepsilon(\alpha))$                                |
| Future<br>Closing<br>Price               | $Cost(\alpha) = h(X, \alpha) + \varepsilon$                      | $\Re(\alpha) = \sigma(\varepsilon(\alpha))$                                |

Source: Kissell and Malamut (2005 and 2005b)

# Table 7-1 Benchmark expected costs and risks

An arrival price benchmark  $(p_0)$  gives the same expected cost and risk as we saw in Chapter 6. The cost consists of both temporary and permanent impact. The permanent impact  $g()$  is based on the order size (X) whilst the temporary impact cost function  $h()$  also depends on the trade rate ( $\alpha$ ). The timing risk principally consists of the price volatility  $\sigma$ (), which in turn is based on an error factor  $(\varepsilon)$ , this just represents random noise.<sup>1</sup>

Using a pre-trade benchmark  $(p_d)$  earlier than the arrival price means an additional price change  $(p_0 - p_d)$  must be considered. This corresponds to the delay cost. Therefore, benchmarks based on previous closing or opening prices must incorporate this into their expected costs and risks. In terms of expected cost, the efficient trading frontier will be shifted by this amount. The direction depends on whether the order is a buy or a sell. For instance, assuming a buy order then a price rise will shift the frontier upwards, with the opposite effect for a sell order. Similarly, the additional timing risk factor is reflected as  $\sigma^2 (p_0 - p_d)$ . This increased risk helps shift the frontier to the right in Figure 7-4.

In comparison, using a post-trade benchmark based on a future closing price will reduce the expected cost. This is because the permanent market impact is already accounted for in the future benchmark price. Hence, the estimated cost is just the temporary market impact (assuming no real price trend). Thus, the efficient trading frontier is shifted downwards by an amount equal to the permanent market impact. Though, in terms of timing risk, it will be just like the arrival price benchmark (since the time periods are the same).

Note that intraday benchmarks behave somewhat differently, since they are based on prices throughout the day so they incorporate both temporary and permanent impact cost. Therefore, for a VWAP benchmark it is possible to minimise both cost and timing risk by participating evenly with the day's volume.

The benchmark choice can clearly affect the efficient trading frontier, and so it can alter the optimal choice of trading strategy. For instance, Figure 7-5(a) shows the two frontiers depending on whether the arrival price or the previous close is used as the benchmark. Given the same target cost  $C_1$ , the shifted efficient trading frontier for the previous close benchmark results in an optimal strategy  $(X_2)$ , which has a higher risk  $(R_2)$  than the corresponding optimal strategy  $(X_1)$  for an arrival price benchmark.

![](_page_6_Figure_6.jpeg)

Reproduced with permission from Institutional Investor

Figure 7-5 The effect of benchmarks on implementation goals

 $\mathbf{I}$  For simplicity these examples assume there is no real price trend and liquidity volatility is excluded from the timing risk.

Conversely, given the same timing risk  $(R_1)$ , Figure 7-5(b) shows how using the day's close price as a benchmark will have a lower expected cost  $(C_2)$  when compared to using the arrival price  $(C_1)$ , due to the closing price incorporating permanent market impact.

# Determining the level of risk aversion

Risk aversion directly affects the aggressiveness of a trading strategy. A high level indicates that timing risk is not acceptable and so the strategy should be more aggressive to try to complete faster. This increases the expected cost due to market impact. Alternatively, a low level suggests that minimising market impact is more important.

![](_page_7_Figure_4.jpeg)

Figure 7-6 Risk aversion

Kissell and Malamut (2005b) highlighted this relationship between the risk aversion parameter  $(\lambda)$  and trading style by plotting a normalised efficient trading frontier. As Figure 7-6 shows, both the cost and timing risk axes are expressed in terms of basis points. Hence, the values of  $\lambda$  are much clearer, ranging from 0 to 3, rather than  $10^{-6}$  to  $10^{-7}$ . They observed an approximately linear relationship between the risk aversion parameter  $(\lambda)$  and an investor's level of concern about risk relative to cost. For example, a value of  $\lambda = 1$  in Figure 7-6 represents an investor who is equally concerned about both risk and expected cost, whereas for  $\lambda = 0.5$  the investor is only half as concerned about risk. The gradient  $\lambda$  also corresponds to the total trading time. A higher value of  $\lambda$  suggests more urgency and so a shorter horizon, whilst lower values suggest a more patient approach.

# Choosing a trading goal

Having specified both a benchmark and the level of risk aversion, we can now start to focus on finding the optimal trading strategy. Robert Kissell, Morton Glantz, and Roberto Malamut  $(2004)$  outline three distinct trading objectives, namely to:

- Minimize the expected cost for a given level of risk
- $\bullet$ Achieve price improvement over a given level of cost
- Balance the trade-off between expected cost and risk

Different types of investors may prefer specific goals; those driven by exposure will often

choose to fix their expected risk, whilst information-driven investors may select price improvement to maximize the short-term returns.

# Minimize cost

The efficient trading frontier represents the set of optimal trading strategies; they offer the lowest expected cost for each specific level of risk. Therefore, for a given level of risk we can find the optimal strategy simply by finding the corresponding point on the frontier. The optimal strategy A lies on the frontier with an estimated cost C and risk R, as Figure 7-6 shows. In comparison, suh-optimal strategies lie above the frontier, and so achieve the same level of risk, but with a much higher expected cost.

# **Price improvement**

Roberto Malamut proved that the optimal price improvement strategy to beat a specific cost (C) could be found from the tangent of a line drawn from  $(0, C)$  to the efficient trading frontier.

![](_page_8_Figure_6.jpeg)

Source: Kissell, Glantz, and Malamut (2004) Copyright © Elsevier 2004 Reproduced with permission from Elsevier

# Figure 7-7 Maximising the likelihood of price improvement

This is shown as strategy  $X_3$  in Figure 7-7, with a timing risk of 150 bps it offers the most chance of beating the expected cost of 50 bps.

# Balancing the trade-off between cost and risk

Minimising the overall cost of trading is made more difficult by the fact that its two main components move in opposite directions. Impact cost may be reduced by more passive trading, whilst timing risk may be lowered by trading more aggressively. Kissell and Glantz (2003) term this optimisation problem the trader's dilemma. As we saw in Figure 7-6, each level of risk aversion  $\lambda$  has a corresponding optimal strategy. At this point, the slope of a line tangent to the efficient trading frontier equals  $-\lambda$ . We can use this fact to determine the optimal cost profile for a given  $\lambda$ , simply by sliding a line with a slope of  $-\lambda$  until it becomes a tangent with the frontier curve. Thus, in Figure 7-8 the optimal strategy where  $\lambda=1$  is  $X_2$ , which has an expected cost of 62 bps and a risk of 65 bps.

![](_page_9_Figure_1.jpeg)

Source: Kissell, Glantz, and Malamut (2004) Copyright © Elsevier 2004 Reproduced with permission from Elsevier

Figure 7-8 Balancing the trade-off between cost and risk

# Determining the optimal trading horizon

Understanding the optimal trading horizon can be very useful, even for orders which are intended to be traded VWAP over the day (if only to confirm they are viable to trade over a single day). Figure 7-9 shows the various costs/risks for an example strategy as they vary over time. We can construct the total cost curve by summing the market impact and timing risk for different levels of risk aversion ( $\lambda$ ) based on equation 7-1.

![](_page_9_Figure_6.jpeg)

Figure 7-9 Trading strategy optimisation

From this, we can then determine the trading horizon that achieves the minimum overall cost. This time span could be used to guide an implementation shortfall algorithm, or converted into a target volume participation rate, based on the historical volume profile or ADV. Kissell and Malamut (2005b) go on to derive a solution for the minimum cost in terms of the optimal trading rate.

#### Choosing between trading algorithms $7.4$

So far, we have seen how various factors can affect strategy choice, but how does this actually translate to selecting different trading algorithms?

Firstly, we shall map the trading algorithms onto an example efficient trading frontier. This will allow us to compare the suitability of specific algorithms for set objectives. To choose the optimal algorithm for a given order, we would need to create an efficient trading frontier tailored for its specific details. This will incorporate the factors we saw in section 7.2 when assessing the difficulty of orders. Hence, we will examine how these conditions affect both the efficient trading frontier and our ultimate choice of the optimal strategy. We will also consider some of the essential requirements for trading algorithms, and see how factors such as data availability and market structure limit our choice.

# Mapping algorithms to the efficient trading frontier

As we have seen, the efficient trading frontier allows traders and investors to see the potential costs and risks of a wide range of trading strategies, from which they may then select their preferred approach.

![](_page_10_Figure_6.jpeg)

Figure 7-10 Differentiating algorithms using an efficient trading frontier

In order to map trading algorithms onto this, we would need to determine estimates for each of their expected costs and timing risks and then overlay these on an efficient trading frontier for the prospective order. Figure 7-10 tries to illustrate this for an example order. Note that this is merely an illustration, to highlight the relative differences between algorithm types. Clearly, specific instances may perform differently. Also not all algorithms may even be on the efficient frontier, since there may be better alternatives.

Notice that for some algorithms Figure 7-10 also includes aggressive (A), passive (P) and neutral versions. As we have seen, more aggressive trading generally implies higher expected costs, although interestingly the price adaptive mechanisms (e.g. aggressive-in-themoney (AIM)) actually have the opposite effect.

Impact-driven algorithms tend to appear towards the right hand side of the efficient trading frontier, exhibiting lower expected cost but higher risk, as we might expect.

#### VWAP:

The VWAP algorithm concentrates on minimizing market impact, by splitting the order into quantities based on the historical volume profile. Although for smaller orders this may unnecessarily prolong trading, causing additional risk exposure. So, a VWAP order left to trade through the whole day has one of the highest associated risks. This may be used as a reference point on the efficient trading frontier, labelled as VWAP/day in Figure 7-10. Simply by reducing the trading time to one appropriate for the order size, the risk may be considerably reduced (labelled VWAP). Notice that the cost does not significantly increase to achieve this.

## TWAP:

In Figure 7-10, TWAP is shown as the only algorithm not to be actually on the efficient trading frontier. This is because when a TWAP algorithm splits an order it does not take into account market conditions. So it may incur additional market impact compared to other algorithms (except for small orders or very liquid assets). Still, in terms of risk it is similar to VWAP, either spread over the whole trading day or for a shorter period. Thus, TWAP is shown directly above VWAP on the efficient trading frontier. (Note that for venues where volume information is not available TWAP is a viable alternative to VWAP.)

#### Percent of volume (POV):

POV algorithms have a similar goal to VWAP, namely minimization of market impact. The only real difference between the two approaches is that the trading trajectory for a POV algorithm is generated dynamically, based on a fixed proportion of the actual market volume. Since its participation is based on the current market volume, each order is more likely to complete in a timescale appropriate for its size. Consequently, the timing risk should be reduced compared to VWAP, although the market impact cost may be slightly higher to achieve this. So, on the efficient trading frontier, POV algorithms are positioned to the just left of VWAP, whilst still exhibiting more risk than implementation shortfall algorithms. Note that the aggressiveness of a POV algorithm may be inferred from its participation rate,  $<5\%$  is relatively passive, so this appears to the right of VWAP on the frontier.

#### Minimal impact:

By focusing solely on minimising the overall market impact cost, these algorithms take on a higher level of timing risk. Consequently, they appear on the right hand side of the efficient trading frontier.

Cost-driven algorithms attempt to balance both cost and risk. Therefore, they will tend to be more in the centre of the efficient trading frontier. Although aggressive versions will be closer to the left hand side, achieving lower risk, but at a higher expected cost.

#### *Implementation Shortfall (IS):*

These algorithms seek to minimize both market impact and risk, often by determining the optimal rate of trading. They tend to trade more quickly than VWAP or POV algorithms, resulting in a lower timing risk. Though, this reduced risk is achieved at a slightly higher expected cost. Thus IS trading algorithms using aggressive (A) or neutral trading styles appear to the left of POV on the efficient trading frontier shown in Figure 7-10. Only the passive (P) style exhibits lower cost, although this still has lower timing risk than VWAP.

## Market close (MC):

These algorithms aim to match or better the future closing price. Whereas an

implementation shortfall algorithm calculates an optimal trade duration, MC algorithms reverse this process to determine an optimal start time. Since their target price is subject to the same timing risk, this offsets some of their risk. However, the closing period is often more volatile and so MC algorithms will often incur higher costs. As a result, they are positioned just to the left of implementation shortfall on the efficient frontier, with lower risk, but higher expected costs.

#### Adaptive Shortfall:

An aggressive in-the-money (AIM) adaptive shortfall algorithm becomes more aggressive with favourable prices. As Kissell and Malamut (2005b) highlighted this results in a skewed distribution of returns between rising and falling markets. In comparison, algorithms with a low sensitivity to price movements (such as POV) have a more symmetrical distribution of returns. We can clearly see this in Figure 7-11 (a) taken from their study, where the AIM adaptive shortfall algorithm is compared with a constant trade rate (POV) algorithm. Since the AIM price adaptation takes advantage of better market conditions, it achieves a lower expected cost  $(C3)$ . The downside is that this approach will be increasingly exposed to risk in adverse conditions, since it will be more passive as the price becomes unfavourable. This also helps explain the skewed cost distribution. Therefore, in terms of the efficient trading frontier the AIM adaptive shortfall (AS) algorithm will be to the right of the POV algorithm.

![](_page_12_Figure_4.jpeg)

![](_page_12_Figure_5.jpeg)

Reproduced with permission from Institutional Investor

Figure 7-11 Cost distribution of adaptation tactics

Conversely, the passive in-the-money (PIM) version becomes more passive with favourable prices, again shown in Figure 7-11 (b). Therefore, it has a higher expected cost (C4) but a lower overall risk; so it is sited to the left of POV on the frontier.

Note that since adaptive shortfall algorithms are sensitive to timing risk their rate of trading does not change pace quite as rapidly as a purely price inline algorithm. The net result is that whilst the effective cost of an AIM adaptive shortfall algorithm is still lower than a POV algorithm it is slightly more than that of an aggressive price inline algorithm. So it sits between these two algorithms on the efficient trading frontier.

The opportunistic algorithms are slightly more difficult to place on the efficient trading frontier. They can aggressively take advantage of favourable conditions, although this can lead to substantial impact costs. They are also prepared to wait passively until the market conditions become favourable, exposing them to timing risk.

#### Price Inline:

As we have already seen for the adaptive shortfall algorithm, an AIM price inline algorithm has a skewed cost distribution. We can see this most clearly when compared with a POV algorithm as shown in Figure 7-12, again taken from the study by Kissell and Malamut (2005b). Note the price inline algorithm is labelled as "Target". Thus, the AIM price adaptation takes advantage of better market conditions, achieving a lower expected cost (C2), but exposing it to higher overall risk. Therefore, on the efficient trading frontier the aggressive PI(AIM) algorithm will be to the right of the POV algorithm. On the other hand, the reversed behaviour of the passive in-the-money (PIM) version is effectively a mirror image resulting in a lower overall risk (but higher cost) and so is sited to the left of POV on the efficient frontier.

![](_page_13_Figure_3.jpeg)

Source: Kissell and Malamut (2005b)

Reproduced with permission from Institutional Investor

Figure 7-12 Cost distribution of an AIM price inline algorithm

#### Liquidity-driven:

A liquidity-driven algorithm will trade fairly aggressively when there is liquidity, but at other times it simply will not trade. Some controls on the permitted level of participation will prevent the market impact being too high. However, the algorithms do not generally account for timing risk. So in Figure 7-10 the optimal liquidity-seeking algorithm is positioned just to the right of the price adaptive AIM based strategies. Though, it is arguable that different versions of the algorithm might be placed anywhere on the frontier between VWAP/day and implementation shortfall.

#### Pairs:

A pair trading algorithm has a degree of inbuilt hedging, provided the relationship between the two asset prices behaves as we expect. So gains (or losses) on asset B should hopefully offset any losses (or gains) on asset A. Still, if the relationship breaks down the strategy may expose us to more risk. There is also an issue if there is a sizable difference in liquidity between the two assets; significant legging will mean a higher exposure to risk. Therefore, it is hard to place pair trading algorithms on Figure 7-10. Given a suitable pair, the optimal pair trading algorithm could achieve a similar expected cost to VWAP, but with less risk. Whilst a sub-optimal pair may require much more aggressive trading in order to try to minimise the risk.

Again note that these summaries merely give an indication of how the various trading

algorithms might be positioned on an efficient trading frontier, actual versions may perform slightly differently.

# Factors affecting algorithm choice

When seeking the optimal trading strategy it is vital to balance the investor's objectives with the factors that dictate the overall difficulty of trading. Consequently, the choice of algorithm/strategy is dictated by factors such as:

- Investor requirements (e.g. benchmark, risk aversion and trading goals)
- Order specific properties (e.g. size)  $\bullet$
- Asset specific properties (e.g. liquidity, volatility and price trends) .

Each of these can have a considerable effect on the overall cost. For instance, Figure 7-13 shows how both order size and asset volatility increase the overall cost for a percent of volume (POV) algorithm.

![](_page_14_Figure_8.jpeg)

Reproduced with permission from ITG Inc. and The Trade Source: Brandes et al. (2007)

Figure 7-13 Relating cost to order size and volatility

This cost estimate is based on performance data from ITG Inc., reported in a study by Yossi Brandes *et al.* (2007). We can therefore use such historical performance data to guide our choice. If the projected cost is too high then we can repeat the process for other types of algorithm until we find the one that is closest to matching our requirements. In the following sub-sections, we shall examine the effect of each of these factors.

# **Investor requirements**

The investor's requirements are clearly also a key determinant in the choice of trading algorithm, in much the same way as we saw for the optimal strategy selection.

# Benchmark

The choice of benchmark affects the efficient trading frontier, as we saw in Figure 7-4. If the benchmark is the arrival or decision price then implementation shortfall is probably the most appropriate algorithm. If it is VWAP then a VWAP algorithm makes most sense.

## **Risk aversion**

A high risk aversion suggests an aggressive trading style, whereas a low aversion means more passive algorithms may be used. For example, Figure 7-14 shows the relationship between cost and risk aversion for an opportunistic algorithm (ITG Active) and a more aggressive implementation shortfall based approach (ITG ACE), based on a review by Jian Yang and Brett Jiu (2006). At low levels of risk aversion, the more opportunistic algorithm proves cost effective, whilst at higher levels the implementation shortfall algorithm performs best. A similar effect might be seen if we replaced the opportunistic algorithm with an impact driven one, such as VWAP. In terms of the efficient trading frontier, a high risk aversion suggests a shift towards more aggressive algorithms on the left hand side of the frontier, whilst a low aversion implies a shift to the right.

![](_page_15_Figure_4.jpeg)

Source: Yang and Jiu (2006)

Reproduced with permission from ITG Inc.

Figure 7-14 Relating cost to risk aversion

#### **Trading goals**

If the goal is to minimise the expected cost, then we can achieve that by finding the algorithm whose projected risk is the closest match for the required level. Whereas if the goal is to achieve a balance between expected cost and risk then cost-driven algorithms such as implementation shortfall may be the most appropriate choice. Alternatively, if price improvement is the main focus then perhaps an opportunistic liquidity-driven algorithm or a passively priced impact-driven algorithm is more suitable.

## Order specific factors

From section 7.2, we have already seen the effect order-specific properties, such as size and trading horizon, can have on the difficulty of an order. Hence, this can also affect our choice of algorithm, based on the expected cost and risk.

## Order size

Larger order sizes generally mean increased transaction costs. Trying to execute a large order immediately will cause significant market impact. Conversely, splitting it into smaller child

orders and working these over time will expose it to timing risk. Therefore, most algorithms exhibit increased costs as order size increases. However, the magnitude of these increases can vary markedly across different algorithms. Figure 7-15 highlights this for a range of algorithms trading low volatility stocks, taken from a study by ITG Inc.

![](_page_16_Figure_2.jpeg)

Figure 7-15 Relating impact cost to order size for a range of algorithms

Clearly, the opportunistic stealth-driven algorithm (labelled "Dark") performs the best. In part, this is due to its successful minimisation of signalling risk by using IOC orders and hidden trading at "dark pool" ATSs. The impact-driven algorithms perform reasonably well, with VWAP outperforming POV at the highest order sizes. Though, the implementation shortfall (IS) algorithm fares the worst for large orders. The size of difference between this and VWAP is interesting, suggesting that they may have been executed more aggressively, resulting in higher market impact.

If the order size is sufficiently large, then it may be worth considering trading over multiple days, depending on price trends and volatility. In comparison, the choice of algorithm has much less effect for small orders. An order for <1% ADV will probably attain similar results with either VWAP or implementation shortfall.

In terms of the efficient trading frontier, the potential cost of large orders tends to shift the selection to the more passive (but riskier) algorithms on the right hand side of Figure 7-10. In other words, a participation or VWAP algorithm may be preferable to implementation shortfall for large orders.

#### Trade horizon

The trade horizon is usually specified by the order's start and end-time parameters. This is also related to the order size, since we can determine an estimate for the optimal horizon based on the ADV and the desired trading rate.

Clearly, a trade horizon that is shorter than the optimal one is more aggressive, although meeting this requirement can lead to excessive market impact costs. Whereas, if the horizon is much longer than optimal then there can be substantial timing risk. For instance, a small order worked throughout the entire trading day is exposed to unnecessary risk since it could have easily been completed much earlier. As we saw for order size, there will tend to be less difference in performance for short horizons compared to longer ones.

So in terms of algorithm selection, shorter horizons will therefore favour a more aggressive trading, such as a percent of volume or even an implementation shortfall algorithm. Longer horizons favour more passive, impact-driven algorithms, such as an allday VWAP.

## Asset specific factors

Asset-specific factors, such as liquidity and volatility, also affect algorithm choice since they reflect the difficulty of an order, as we saw in the trading costs back in Figure 7-2.

## Liquidity

Liquidity can have a considerable effect on market impact. In fact, it can counteract some of the effects of order size, since a large order for a highly liquid asset will tend to cause less impact than for an illiquid one. Signalling risk can also be an issue for less liquid assets, even for quite small orders.

Since a liquid asset will be easier (and so cost less) to trade than an illiquid one this tends to widen the potential choice of optimal algorithms. Conversely, an illiquid asset limits the choice to more specialised algorithms, such as liquidity-driven ones.

#### Volatility

An asset's volatility affects both its expected cost and timing risk. So for volatile assets it is generally better to select an algorithm that is risk sensitive. In other words, algorithms that achieve lower timing risk such as implementation or adaptive shortfall algorithms.

![](_page_17_Figure_10.jpeg)

![](_page_17_Figure_11.jpeg)

Figure 7-16 Relating impact cost to volatility for a range of algorithms

We can clearly see this in Figure 7-16, which shows the results of the study by Brandes  $et$  $al.$  (2007). As the intraday volatility increases, the cost barely changes for the

implementation shortfall (IS) algorithms. The impact driven VWAP and percent of volume (labelled VP) algorithms fare less well, both suffering increased costs as volatility increases. This is hardly surprising since they have no inbuilt price sensitivity. Certainly, the percent of volume algorithm is the most affected; Brandes *et al.* reason that this is due to the fluctuation of market volume in reaction to price movements. The opportunistic algorithms are also affected, but somewhat less than the impact-driven ones. For example, ITG Active, a liquidity seeking algorithm which uses dynamic pegging, seems to cope with short term price moves nearly as well as an implementation shortfall algorithm.

For lower volatility assets, timing risk is less of an issue and so the potential reduced costs of volume participation make impact-driven or even opportunistic algorithms more suitable.

#### **Price trends**

A persistent and favourable price trend allows us to reduce costs by trading more passively. Whilst an unfavourable trend requires more aggressive trading, since any delay will simply result in even worse executions. Therefore, if we are confident of a price trend persisting then we should consider using algorithms from the appropriate side of the efficient trading frontier in order to benefit most. For instance, a more passively traded VWAP algorithm may perform better for favourable price trends. Alternatively, an implementation shortfall algorithm is more appropriate to prevent losses from an unfavourable price trend. Note that the level of aggressiveness needs to be appropriate for the size of the expected price trend; otherwise, the increased market impact costs will counteract any gains/savings.

Price adaptive algorithms, such as price inline or adaptive shortfall may also be used to take advantage of trends. As we have seen these give a more skewed distribution of expected costs, with aggressive in-the-money (AIM) strategies achieving a lower cost but higher risk, whilst passive in-the-money (PIM) versions do the opposite. If the price trend is short-lived or mean reverts then an aggressive (AIM) approach may be more appropriate. Though, if the trend persists then the passive in-the-money approach may offer the best results.

So in terms of the efficient trading frontier favourable and persistent trends shift the selection to the more passive (but riskier) algorithms on the right hand side of Figure 7-10, whereas unfavourable trends shift it to the left.

#### Summary

The efficient trading frontier can also be used to summarise the effect these factors have, as

![](_page_18_Figure_9.jpeg)

Figure 7-17 Factors which influence trading choice

Figure 7-17 shows. Unsurprisingly, urgency, risk aversion, and volatility all tend to bias the strategy selection towards more aggressive trading with lower risk, but potentially higher impact costs. Conversely, larger orders and favourable price trends tend to encourage a more passive approach with lower impact costs, but potentially higher risk.

# Other requirements for trading algorithms

So far, we have focussed on the theory of algorithm selection. In the real world, basic requirements such as market structure and data availability also limit our choices. Obviously, algorithms need electronic access to make requests or place orders. Market data is another key requirement for trading algorithms, without it they are blind. Hence, the availability of pre- and post-trade market data is vital for most strategies.

Market structure also plays its part. In a single dealer environment there is little point in splitting up an order (unless it is huge and even then it is debatable). Instead, it makes more sense to discuss with the dealer how best to work the whole order. Therefore, to even consider using trading algorithms the market should have multiple dealers/market makers. Conversely, markets that are very fragmented are more difficult to trade in than centralised ones, so this will also affect algorithm choice.

Asset specific factors such as liquidity and trade frequency may also be broadly generalised by asset class. For instance, equities tend to be more liquid than most bonds. Thus, characteristics of the asset class can also affect algorithm choice.

#### **Data requirements**

Trading algorithms rely on market data in order to function. Although market transparency is increasing, there are still marked differences between the world's markets, both for pre- and post-trade information.

Pre-trade prices can be delivered in streams, either from a market data vendor, direct from the execution venue or via a request for stream (RFS) type mechanism. They may also be gathered via a request for quote (RFQ) mechanism. Although the considerable latency associated with an RFQ-based approach means that it is only really viable for strategies that will not be generating a lot of small child orders.

Post-trade data needs to provide accurate information on trade prices, sizes and times (and if possible any counterparty information). For some markets, such information simply has not been available. For example, in the early days of adoption in the FX markets some venues only provided traded prices but not sizes.

Many algorithms track the traded volume, so if this is not available the choice will be severely restricted. Likewise, if the data is available but only after a considerable delay then it is of little use to algorithms such as percent of volume. Post-trade data is also needed to create historical volume profiles, as well as for many of the models that algorithms use to estimate execution probability or costs.

Order book data is necessary for any strategies that are based on the available liquidity. Clearly, this must be available in real-time for any algorithm which actively tracks liquidity. Historical order book data may also be required for limit order and cost models.

Even the most basic trading algorithms need access to real-time best bid and offer prices, otherwise they risk placing orders significantly away from the market. The alternative is to only ever issue market orders. More complex trading algorithms obviously have more stringent requirements, as outlined in Table 7-2.

| Algorithm                |        | Historical |            |        |
|--------------------------|--------|------------|------------|--------|
|                          | Prices | Trades     | Order book | Trades |
| TWAP                     |        |            |            |        |
| VWAP                     |        |            |            |        |
| Percent of Volume        |        |            |            |        |
| Implementation shortfall |        |            |            |        |
| Liquidity-based          |        |            |            |        |

Required ○ Often needed

#### Table 7-2 Basic data requirements for common trading algorithms

As we saw in Chapter 5, some of the earlier statically-driven algorithms can survive based on historical data. So for markets with the bare minimum of electronic access and multiple dealers the only really viable trading algorithm is simple order slicing or TWAP. Consequently, they are available for most types of market or asset class.

VWAP algorithms require detailed trade information in order to construct their volume profiles, Likewise, percent of volume (POV) algorithms need trade reports in real-time in order to track the market volume. In fragmented markets, some brokers/vendors have also started to create their own proprietary measures, hased on aggregated data.

Implementation shortfall (IS) algorithms need to carefully track the current price and the potential risk in order to minimise the overall cost. Therefore, these algorithms need as much help as they can get, otherwise their performance will suffer. Although we might possibly be able to get a shortfall-based algorithm to work for an RFQ based market, it is debatable whether this approach is worthwhile.

Similarly, liquidity-driven algorithms need readily available order book information. If this is limited then algorithms will have to rely more on estimates, which may substantially reduce their efficiency. Signalling risk is obviously a key concern, so again the market needs to support anonymous trading. Given the opportunistic nature of such algorithms, latency can also be a key consideration for them.

Other information such as fees for routing and/or clearing/settlement may also need to taken into account; otherwise, unexpected costs may be incurred.

#### Market structure

Each of the world's major markets has their own specific characteristics, as we saw in Chapter 3. Equities and listed derivatives are traded at centralised venues, although admittedly there is considerable fragmentation in some of these markets. In comparison, OTC trading is still the norm for a lot of fixed income trading. Although clearly there are exceptions, such as the U.S. Treasury market which is so large that its inter-dealer market is not that different from the major U.S. exchanges.

Given their well-established central markets with a range of highly liquid assets, the equities markets were the perfect starting place for algorithmic trading. As we have already seen, the algorithms have progressed from simple order slicing to VWAP, implementation shortfall and liquidity-based algorithms. However, not all algorithms are equal; some are more applicable across a range of asset classes than others, as Table 7-3 tries to show.

Simple order slicing or TWAP algorithms are a basic starting point for every asset class, since they have the least requirements.

Volume-driven algorithms, such as VWAP, make most sense for centralised markets. This is because there only needs to be one set of trade reports, so it is easy to track the market

| Algorithm                | <i>Equities</i> | Bonds | FX | Futures | Options | ETF <sub>S</sub> |
|--------------------------|-----------------|-------|----|---------|---------|------------------|
| $\text{TWAP}$            |                 |       |    |         |         |                  |
| VWAP                     |                 |       |    |         |         |                  |
| Percent of Volume        |                 |       |    |         |         |                  |
| Implementation shortfall |                 |       |    |         |         |                  |
| Liquidity-based          |                 |       |    |         |         |                  |

• High  $\circ$  Medium

#### Table 7-3 Applicability of current trading algorithms across different asset classes

volume. As markets become more fragmented, the volumes for each venue need to be tracked. In order to give meaningful results these algorithms really need to track the total market volume. For instance, if the main market only has around 50% of the total trading volume then VWAP or POV algorithms, which only consider the volume traded here are missing half the picture. Thus, aggregated market data feeds have become increasingly important. If there is a unified source of pre- and post-trade information, this is straightforward; otherwise, we will have to create our own. This also makes transaction cost analysis and performance monitoring more difficult.

Hence, going forward the two most applicable types of algorithm are the implementation shortfall and liquidity-based approaches.

## Asset-class specific factors

There are considerable differences between asset classes in terms of the:

- Number of assets available
- Liquidity
- Frequency of trading / average trade size  $\bullet$

The FX market has easily the lowest number of tradable assets; hence, these are highly liquid. Conversely, there are hundreds of thousands of distinct honds and options, so any one generally has much less liquidity than a corresponding equity.

Trading activity is linked to liquidity and the number of available assets. It is also affected by investors' objectives. For instance, bonds are often bought and held, so after an initial flurry on their first issuance the trading activity quickly subsides. It is not uncommon for corporate bonds to trade less than once a day, on average. In comparison, equities are often held for shorter periods, hence their much higher levels of trading. Volume-driven algorithms need a substantial amount of trading activity for them to be useful; they are just not as meaningful for illiquid assets. So, whilst a VWAP algorithm may be viable for some U.S. Treasuries, it will not be for certain corporate bonds or options.

Trade size and costs also differ amongst the asset classes. For example, bonds generally trade in larger sizes than equities. Bonds also realise lower costs for larger trades, so impact costs will be very different to those for equities.

Other properties associated with asset classes can also affect algorithm choice. For instance, price is not always a key driver for assets. As we saw in Chapter 5, implied volatility can be more important than the actual price for some options algorithms.

Likewise, trading volume is not as vital for some assets. Open-ended ETFs are not subject to a fixed fund size, an in-kind creation and redemption process allows specialised dealers to react to the demands of the secondary market. Therefore, supply and demand have less impact on the price of such ETFs than for equities. Thus, trading volume is a less important indicator for these. So, volume driven approaches, such as VWAP or POV, may be less appropriate.

As algorithmic trading continues to spread, algorithms will probably evolve to be even more tailored for specific asset-classes. In the future, we may well see a new breed of algorithms evolve which treat assets in a more fungible way. Algorithms tailored for bond trading might select between a set of assets, if the investor is happy to consider an alternative with similar characteristics. Similarly, for options, trading based on the risk characteristics (or the "Greeks") may become more important than finding a match for a specific contract.

#### 7.5 To cross or not to cross?

The additional liquidity offered by "dark pool" ATSs means that crossing is another important consideration when seeking the optimal trading strategy. They offer the potential for substantial cost reduction by trading in size without incurring significant market impact. Therefore, it is important to also consider the possibility of using crossing as part of the optimal trading strategy.

Although crossing has obvious advantages, execution is not always guaranteed. Also, whenever trading in size signalling risk is always a concern, even for venues that are intended to be completely opaque. So the optimal approach may well involve a combination of crossing and trading algorithms.

# The benefits of crossing networks and "dark pools"

Using crossing networks or trading via "dark pools" can realise considerable cost savings. Table 7-4 shows a breakdown of these from a study by the Quantitative Services Group LLC (OSG). They compared the performance of trades on the Millennium ATS (between December 2007 and March 2008) with those from a wide range of other execution venues. Overall, they found that "dark pool" execution reduced the market impact of trades by 62%, giving a saving of 6.6 bps. The market impact savings appear to be fairly consistent, regardless of market capitalisation, although the higher costs associated with trading less liquid stocks mean significantly larger savings for the small and micro-cap stocks in terms of basis points/share.

| Category         | Decrease in<br>market impact | Savings<br>(in bps/share) |  |
|------------------|------------------------------|---------------------------|--|
| Micro-cap        | 66%                          | 21.53                     |  |
| Small-cap        | 63%                          | 13.43                     |  |
| Mid-cap          | 59%                          | 8.08                      |  |
| Large-cap        | 62%                          | 5.18                      |  |
| Weighted Average | 62%                          | 6.61                      |  |

Source: QSG (2008)

## <table> Table 7-4 Comparative cost savings achieved on the Millennium ATS

An interesting comparison of the performance between traditional crossing networks and "dark pool" algorithms was carried out in a detailed study for ITG Inc. by Ian Domowitz, Ilya Finkelshteyn and Henry Yegerman (2008). They found that using crossing networks achieved significant cost savings regardless of the market conditions, as shown in Table 7-5.

|                 | Cost saving versus benchmark (bps) |                           |            |               |  |  |
|-----------------|------------------------------------|---------------------------|------------|---------------|--|--|
| Conditions      | Periodic                           | "Dark pool"<br>Continuous |            | Peer universe |  |  |
|                 | crossing                           | crossing                  | algorithms |               |  |  |
|                 | (POSIT)                            | (POSIT Now)               | (ITG Dark) |               |  |  |
| Low volatility  | $+3$                               |                           |            |               |  |  |
| High volatility | +4                                 | -                         |            | -18           |  |  |
| Overall         |                                    |                           |            | -12           |  |  |

Source: Domowitz, Finkelshteyn and Yegerman (2008)

## Table 7-5 A comparison of the costs of different crossing mechanisms by ITG Inc.

From their data, crossing via POSIT realised savings of 3-4 bps in both low and high volatility regimes. Continuous crossing via POSIT Now and "dark pool" algorithms (ITG Dark) were also found to achieve lower costs than a universe of peer trades, whose average cost was 12 bps, reaching 18 bps during periods of high volatility.

Their study considered over 20 million orders, of which around 12.6 million were entered during 2007 using a range of mechanisms, including both periodic and continuous crossing and liquidity aggregation. A further 8 million orders were taken from a complementary transaction cost database. So as well as covering the ITG crossing networks the study also encompassed "dark pools" from a variety of vendors/brokers.

Domowitz, Finkelshteyn and Yegerman also analysed the distribution of transaction costs between these different mechanisms. For orders completed within thirty minutes of submission, they found that the probability of achieving a cost between  $-20$  and  $+20$  bps was highest for periodic crossing (POSIT) at 88%. Continuous crossing via POSIT Now had a 77% probability of meeting this cost band whilst trading via a liquidity aggregator was found to only have a 61% chance. They found that the risk of incurring higher transaction costs was significantly lower for the dedicated crossing mechanisms. For periodic crossing, the probability of incurring a cost of more than 20 bps was only 4% whilst for continuous crossing it was 10%, reaching 20% for the "dark pool" algorithms based on liquidity aggregation.

The effect of execution duration was analysed as well. They found a consistent degradation in performance with increasing time. For example, the periodic crossing for POSIT realised healthy savings for up to the first hour of execution, but after 2.5 hours this became a cost of 6 bps. In comparison, they found this effect to be even greater for other "dark pools", realising losses of up to 25 bps after 2.5 hours.

Overall, Domowitz, Finkelshteyn and Yegerman (2008) concluded that execution using "dark pools" is beneficial; though, they found no improvement using "dark pool" algorithms compared to periodic crossing. They reason that this is probably due to information leakage: whilst each venue may be dark, the more orders are routed between them the more chance there is of leakage. Hence, algorithms that route orders between different "dark pools" may not necessarily perform as well as simply routing the order to a single venue.

Clearly, substantial cost savings can be realised by crossing, but it is also worth comparing the various mechanisms. Using a periodic crossing may well prove to be a more cost efficient approach than using some of the dedicated "dark pool" liquidity algorithms.

#### 7.6 Market conditions during the 2007-09 financial crisis

Up until this point, the focus has been on general principles. Still, it is impossible to ignore the conditions during the 2007-09 financial crisis, particularly in the stock markets. Major stock indices saw ten year lows, with daily falls (and rises) of  $3-5\%$ , or even more.

![](_page_24_Figure_3.jpeg)

#### Figure 7-18 Changing market conditions

Market volatility and trading volumes surged, as shown in Figure 7-18, the volatility spikes are easy to see. Indeed, the CBOE's VIX volatility index reached an unprecedented high of 89 in October 2008. Market volumes also surged, as investors sought to convert their positions to cash, as well as the unwinding of positions in funds that had failed.

In contrast to this, many of the key indicators of market liquidity actually declined: Spreads increased whilst the displayed depth on many order books was significantly reduced. In such an unpredictable trading environment, there is clearly a benefit to getting additional market "colour" and discussing orders with a trader. In fact, a TABB Group (2008) review of U.S. institutional trading found that sales traders' captured 44% of huy-side flow in 2008, up from 37% the year before. Interestingly, though, this seems mainly to have been at the expense of DMA and crossing networks or "dark pools". They found that algorithmic trading usage actually increased to 24%, from 22% in 2007. Despite the harshest of trading conditions, algorithms appear to have proved themselves.

The partial decline in usage of DMA and crossing networks is understandable given the extreme market conditions: When markets move so rapidly it is difficult to handle a large number of orders directly. Similarly, leaving an order for a long time in a "dark pool" is a much riskier proposition since the market prices could rapidly change. In both cases, it is casier to leave orders to be handled by a sales trader or an algorithm.

The market crisis also led banks to reduce the amount of principal and proprietary trading.

Trading large block orders became more difficult, since the "upstairs" market was a shadow of its former self. Hence the value of crossing networks and "dark pools". In fact, a survey of U.S. "dark pools" carried out by Rosenblatt Securities (2008a) found that their market share actually increased in November 2008, to 8.57%, after falls in September and October. They also note that the volatility seemed to have most impact on the venues focussed on large block orders.

Transaction costs also saw considerable increases due to the market volatility. The most visible change was in spread costs. Dealers and market makers need to incorporate the higher level of risk in their quoted prices. Thus, bid offer spreads nearly doubled, even for some blue-chip stocks. Less liquid firms saw even higher increases. Spreads saw similar increases across Europe and even larger ones in Asia. Although spread cost is not the only concern, since the reduced liquidity also led to higher market impact costs. In fact, in their study of 2008 ITG client execution data Hitesh Mittal and James Wong (2008) found that there was 37% less displayed liquidity during the high volatility regime. Overall, they estimated that selecting the optimal trading algorithm led to savings of 60 bps for their clients, compared to 20 bps during lower volatility periods.

As we have already seen, volatility tends to lead to more aggressive trading strategies seeking to minimise the risk at the cost of higher potential impact. Consequently, the market crisis resulted in a shift in the type of algorithms being used. Implementation or adaptive shortfall algorithms became much more important. Lower levels of visible liquidity and the desire to minimise signalling risk also meant that liquidity-based algorithms became more widely used. Overall, Mittal and Wong (2008) found the best performance was from dynamic/opportunistic algorithms, which took advantage of market conditions but also tracked implementation shortfall costs. So it is important for trading algorithms to:

- $\sim$ Track cost and risk
- . Take advantage of all available liquidity
- Minimise signalling risk / information leakage  $\sim$

Clearly, a first generation static schedule-driven VWAP algorithm is going to struggle compared to more sophisticated algorithms that dynamically adapt to conditions. Note, this is not to say VWAP trading does not still have a place. As we saw in the previous section, in high volatility it can actually realise lower costs than POV algorithms since it is less prone to chasing the market. Again, it is all down to doing the pre-trade analysis and selecting the most appropriate algorithm for a given order based on the investor's requirements and the market conditions.

Volatile markets also pose a significant problem for the models which trading algorithms use to determine potential costs or to determine a trading horizon. In turbulent markets, historical data often does not act as a good indicator for future conditions. Short-term forecasting models may be used, adjusting the historical estimates based on current market conditions. In Chapter 10, we will cover these forecast models for conditions, such as price, volatility and volume, in more detail. Also in Chapter 15, we will see how techniques such as data mining and artificial intelligence may be used to improve their accuracy.

#### A decision tree for strategy selection 7.7

We started this chapter with Wayne Wagner's (2006) example trading decision framework, shown back in Figure 7-1. The first key decision was to determine the difficulty of the order. As we saw in section 7.2, three of the main factors for this are liquidity, volatility and order size. These also tie in with the trends shown back in Figure 7-17.

A potential decision tree for algorithm selection for difficult orders is shown in Figure 7-19. The main choice is whether the order is urgent or large. An order may be urgent because the investor's risk aversion is high or the asset is volatile, whilst a large order might be anything over 20% of the ADV.

![](_page_26_Figure_3.jpeg)

Figure 7-19 An algorithm selection decision tree for difficult orders

Volatile assets can have considerable timing risk, so they need to be traded more urgently. Larger orders can cause substantial market impact, so they require more careful handling. Bear in mind that order size is relative. For instance, a million shares might be very little for a blue-chip stock whilst ten thousand might be a massive amount for an illiquid firm. So liquidity can be incorporated, to an extent, in the relative order size. Hence, liquidity is treated as a secondary factor, which makes our trading easier. Thus, urgent or large orders for liquid assets pose much less of a problem than for illiquid ones.

The choice of trading algorithm follows the trends we saw in Figure 7-17, which also ties in with the algorithm mapping from the efficient frontier in Figure 7-10. Urgent trades for liquid assets will tend to use the cost-driven implementation (or adaptive) shortfall based algorithms, whilst large trades for liquid assets will use the more impact-driven VWAP or POV algorithms. With illiquid assets there is much less choice, in order to achieve best execution we shall have to rely on liquidity based algorithm. For urgent orders, the timing risk means the trading will need to be reasonably aggressive, whilst for large orders a more passive approach is worthwhile.

Crossing is another key consideration. Trading algorithms are increasingly interacting with crossing networks. Though, this may simply mean passing orders through crossing venues. The risk of overfilling means it is often not viable to leave an entire order at a crossing venue whilst trading it in parallel via an algorithm or DMA. Therefore, some liquidity-based algorithms may well leave a sizeable proportion of the order at a crossing venue, whilst splitting off slices to trade on the markets. This approach will generally be adopted for illiquid assets or larger orders, since the lower probability of execution makes it less appealing for urgent orders.

Figure 7-19 does not show any choices for easy orders. This is because these have no real constraints. Similar results could be achieved with any of the trading algorithms. So, it comes down to the investor/trader's preferences. Clearly, the decision tree shown in Figure 7-19 is only one example of how we might perform algorithm selection.

Going one step further, Neovest has actually created an algorithmic management system called AlgoGenetics; a screenshot is shown in Figure 7-20. This provides a drag-and-drop interface allowing traders to establish the exact conditions for algorithm or DMA order selection. It also caters for algorithms from a wide range of brokers/vendors. Thus, rules may be set to select the "best of breed". Traders can also specify their own customised behaviours effectively creating their own "meta-algorithms". For instance, an order might initially be configured to participate in the opening auction. The remainder could then be split between a range of different algorithms: baseline participation might be achieved with a POV algorithm whilst in parallel it might seek further price improvement from a more price adaptive or liquidity-seeking algorithm.

![](_page_27_Figure_4.jpeg)

Source: Traders Magazine (2007b) Reproduced with permission of Neovest, Inc. and Traders Magazine

Figure 7-20 Creating rules for algorithm choice with AlgoGenetics

Such flexibility clearly gives traders a powerful tool for algorithm selection. Note that selecting the optimal trading algorithm from the many hundreds versions which are available will always be a difficult choice. Still, it is important to stay focused on the overall investment objectives. As usual, the choice will often mean striking the right balance between cost and risk.

#### 7.8 Summary

- There are no hard and fast rules for how to achieve best execution. The judgement  $\mathbf{m}$ depends on the investor's objectives, so key factors are the:
  - Target benchmark
  - Level of risk aversion
  - Specific trading goals, such as to:
    - Minimize the expected cost.
    - Achieve price improvement.  $-$
    - Balance the trade-off between expected cost and risk.  $\overline{\phantom{a}}$
- Trading decision frameworks often start by gauging the difficulty of the order, which is determined by the following properties:
  - Order size (relative to the  $ADV$ )  $-$
  - Price momentum
  - Volatility \_
    - Urgency and/or the trading horizon
  - Liquidity
- Based on this difficulty, the trader then must select the most appropriate methods, whether this means manual, DMA, crossing, using trading algorithms or a mixture of these.
- The efficient trading frontier represents the set of optimal trading strategies. Each one of these has the lowest expected cost for a given level of risk. Algorithms and other strategies may be mapped to this frontier, allowing comparison between them.
- A wide range of factors affects the choice of trading algorithm.
  - Urgency, risk aversion and volatility tend to bias towards more aggressive trading.
  - Larger orders and favourable price trends tend to encourage a more passive style. \_
  - Fundamental issues, such as the availability of market data and market structure also restrict the choice of strategy.
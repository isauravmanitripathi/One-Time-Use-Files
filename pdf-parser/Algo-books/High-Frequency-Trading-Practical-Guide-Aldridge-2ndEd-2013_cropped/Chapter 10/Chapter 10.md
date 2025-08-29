# **CHAPTER 10** Automated Market Making—Naïve Inventory Models

Most high-frequency trading (HFT) systems are deployed to provide automated market-making services. Some 30 years ago, this activity was entirely human, but is now moving to a nearly fully computerized mode. This chapter considers the basic principles behind the successful marketmaking models.

#### **Introduction**

Every veteran trader can recount a story of a dominant human market maker who "owned" transactions in a particular financial instrument. These kingpins of financial markets generated heavy transaction-based profits for their employers, commanded extensive bonuses and lived luxurious lifestyles.

With rare exceptions, nearly all stories about these once-potent human traders end on the same sour note: "and then one day, the market turned against him, he suffered a major loss, and was fired the next day." An example of such a "burnout" was a trader in USD/CAD foreign exchange futures at a certain bank, who made markets for a long time and periodically enhanced his profitability and bonus by taking directional bets at his personal discretion. Once, the trader's bet fell radically off its mark, resulting in nearly instantaneous multimillion-dollar losses to his employer. The trader was immediately dismissed following the incident and was prohibited from ever again setting a foot on any trading floor.

Automated market making provides several advantages to the marketmaking institution as well as other market participants. First, automated market makers stay on script. Unlike human traders, properly programmed and tested computer systems do not deviate into discretionary actions. As a

result, automated market makers reduce the incidence of market crashes and negative surprises for market makers' bottom line. Second, execution of automated market making is cost efficient: once the human-intensive programming and testing stages are completed (see Chapter 16 for details of HFT development processes), automated market makers require little compensation. The savings from head-count reductions are significant and are passed directly to the automated market makers' shareholders and clients in the form of enhanced profitability and reduced transaction costs.

Perhaps the best feature of market-making strategies is their scalability across various markets. Almost any market-making strategy running on an exchange equipped with a centralized limit order book can be run on another exchange, another financial instrument and even another asset class, provided that the new trading venue also deploys centralized limit order book methodology (see Chapter 3 for limit order book definitions and description). Most of today's exchanges in the world deploy the centralized limit order book model, making market-making technology extremely portable.

A market-making process works as follows: a market maker, whether human or computerized, posts limit buy and limit sell orders. Depending on market conditions and positions in the market maker's current portfolio, the market maker may choose to post only limit buy or only limit sell orders. Some market participants, however, consider market making to refer strictly to a continuous activity with open limit orders placed simultaneously on both sides of the market. *Liquidity provision* is a more general term describing market making as well as most limit order trading.

When the market price reaches the market maker's limit buy order with the highest price, this price becomes the best bid on that market, and is distributed to other market participants as a Level I "quote." Similarly, when the market maker's limit sell order is the lowest-priced limit sell order in the market, his order becomes a best offer or best ask, and is quoted to other market participants.

Market makers' orders are executed by virtue of being matched with incoming market orders of the opposite direction. The market maker's bids are said to be "hit" by market sell orders, and the market maker's ask or offer limit orders are said to be "lifted" by incoming market buy orders.

With every executed limit order, the market maker accumulates or divests quantities of the traded financial instrument in his account. These quantities are known as *inventory.* Immediately upon acquiring the inventory, the market maker begins to manage it, to reduce risk and enhance profitability.

The two broad functions of a market maker are therefore:

- Manage inventory to ensure sufficient profitability.
- Keep track and respond to information in order to avoid being "run over" or "picked over" by the markets.

Too little inventory may be insufficient to generate a profit; too much inventory makes the trader risk inability to quickly liquidate his position and face a certain loss.

# Market Making: Key Principles

In a nutshell, "market-making" describes placement of limit orders on both sides of the market price. A market maker placing a limit buy order just below the market price and a limit sell order just above the market price creates or "makes" the "market." When a market buy order arrives from another market participant, it is matched with the market maker's limit sell order, and the limit sell order is executed (i.e., a short position is recorded in the market maker's account). Similarly, if a market sell order arrives from yet another market participant, it is matched with the market maker's limit buy order, and a long position is added to the market maker's account. If the size of the long position neutralizes the size of the short position in the market maker's portfolio, the market maker collects the spread as a compensation for providing limit orders, or liquidity, to traders placing market orders. The market order traders are known as *liquidity takers.*

Of course, market making is subject to risk. As soon as the market maker places his limit orders, he immediately faces two types of risk:

- Inventory risk
- Risk of adverse selection

Inventory risk describes the potential loss the market maker might incur when the value of his inventory declines in price due to natural market movements. Thus, a market maker accumulating a long position (buying) in

a downward-trending market is likely to experience a loss on his position, at least in the short term. In addition, inventory risk is incurred when the market maker wishes to close his positions, as the market maker may face competition from other parties looking to sell their positions at the same time, resulting in difficulties liquidating his inventory. Inventory risk also includes the opportunity costs reflecting the gains the market maker misses while waiting for execution of his limit orders.

The risk of adverse selection measures potential loss due to informational differences between the market maker and a market taker. When the market taker possesses better information set than the market maker, the market maker is likely to be entering the losing end of the trade. For example, when a market maker's limit buy order is matched with a market sell order, it is possible that the seller has better information than the market maker about the imminent direction of the market – in this case, down, and that the market maker is about to commit to a losing trade. Per Copeland and Galai (1983), all limit orders suffer from an informational disadvantage, whereby they are picked off by better-informed investors. While the risks of inventory and adverse selection can produce significant losses for the market makers, the risks can be profitably controlled.

## Simulating a Market-Making Strategy

Trading with limit orders generates nonlinear payoffs; sometimes limit orders execute and sometimes they do not. As a result, limit orders are difficult to model. This section delves into the logistics of limit-order modeling.

Strategies that deploy market orders can be simulated with an assumption that each order is executed near the latest trade price observed in data at the time the simulated order is placed. By contrast, simulating execution of limit orders requires additional work. Most solid simulations consider a given limit order executed only when the best opposing quote reaches or crosses the limit order, in a process shown in Figure 10.1. A limit buy order is considered executed when the last trade price or the best ask quote falls below the price of the simulated limit order. A limit sell order can be

marked processed whenever the last trade price or the best bid quote exceeds the price of the simulated limit order.

![](_page_4_Figure_1.jpeg)

Naïve Market-Making Strategies

This section explains the details of practical market-making strategies that concern themselves only with effective management of inventory. Enhancements based on short-term directional market forecasts are discussed in Chapter 11.

#### Fixed Offset

The most naïve market-making strategy is continuously placing limit orders at a predetermined number of ticks away from the market price, on both sides of the market. Naturally, the probability of limit orders being executed depends on the limit order price proximity to the current market price. Limit orders placed at current market quotes are likely to be executed, whereas

the probability of execution for passive limit orders, those far away from the market price, is close to zero. In most financial instruments, market makers are allowed to place limit orders only within 10 percent of the current market price, to prevent so-called "stub quotes" far away from the market from executing at times of extreme volatility.

The smaller the offset of a limit order from the market price in a naïve strategy, the higher the probability of order execution, and the more frequent the resulting reallocation of the market maker's capital. Frequency of trading has been shown to be key to market makers' profitability. The higher the number of times the market maker can "flip" his capital, the higher the cumulative spread the market-maker can capture, and the lower the risk the market maker bears waiting for execution of his orders. A study of market making on actively traded stocks on the Stockholm Stock Exchange, for example, found that the expected profit on limit orders increases when they are matched more frequently. The study, written by Sandas (2001), shows that market makers' profitability is not proportional to the time they spend providing liquidity; instead, market makers' profit is directly tied to the frequency with which their orders are executed.

By contrast, early market-making theories presumed that market makers were content to be compensated for time spent providing liquidity. The longer the waiting time until order execution, the thought went, the higher was the expected compensation to liquidity providers who did not change their limit order specifications once they submitted the orders. Such ideas were known as *static equilibrium models* and included Rock (1996), Glosten (1994), and Seppi (1997).

The assumptions of static equilibrium models reflected early exchange conditions. Changing the details of a limit order and canceling orders was prohibitively costly, and market makers indeed expected a tidy compensation for bearing the risk of ending up in an adverse position once their limit orders were hit. Limit order cancellations and revisions could be performed free of charge on most markets at the time this book was written. As a result, today's high-frequency market makers enjoy better profitability than their human market-making counterparts.

The ability to place orders at the best bid and best ask prices, however, may be limited by the speed of the HFT market maker's technology. Superfast technology allows market makers to continually cancel and resubmit their limit orders to ensure their spot on the top of the book, high execution rates, and high profitability. Slower technology can still deliver profitable market-making strategies via larger offsets away from the going market price.

#### Volatility-Dependent Offset

To improve the fixed-offset strategy, one may vary the offset of limit orders with market conditions. One intuitive way to change the offset is to make it a function of volatility: in high-volatility conditions, limit orders farther away from the market are likely to be hit, generating higher premium for market makers. In low-volatility conditions, however, limit orders may need to be placed closer to the market to be executed. A sample determination of volatility-dependent offset is shown in equation (1):

(1) 
$$\text{offset}_{t} = \text{round}\left(\frac{1}{T}\sum_{\tau=t-1}^{t-T} (P_{\tau} - P_{\tau-1})^{2}\right)$$

#### Offset Is a Function of Order-Arrival Rate

Still another way to improve the naïve market making is to make the offset dependent on the arrival frequency of market orders. As Parlour and Seppi (2008) point out, limit orders compete with other limit orders, both existing and those submitted in the future. Furthermore, all limit orders execute against future market orders. The market order arrival rate, therefore, is an important determinant of market-making profitability.

The market orders can be assumed to arrive independently of one another, and with a great degree of randomness. Much like the arrival of subway trains or street cars, though, the randomness of order arrivals can be modeled using well-specified statistical distributions. Under the assumptions of exponentially-distributed inter-arrival times, for example, the market orders arrive to "hit the bid" and to "lift the ask" with a certain average rate, *μ*. The limit orders can be assumed to repopulate the top of the limit order book at an average rate λ. Probability of a top-of-the-book limit order being matched can then be expressed as a function of λ = 1/λ, µ = 1/µ and a given interval of time, Δ*t*:

$$P(\textit{hit}, \Delta t) = 1 - P(\textit{not hit}, \Delta t) = 1 - \exp\left(-\frac{\lambda}{\mu}\Delta t\right)$$

Parameters λ and µ can be calibrated on recent tick data. Level I data can be used to calibrate parameters for minimal time intervals, Δ*t* = 1. When the best bid moves up or the size at the best bid increases, a new limit buy order is assumed to have arrived. When the best ask moves up or the size at the best ask decreases, a market buy order is recorded. Avellaneda and Stoikov (2008) present an example of strategy deploying arrival rates.

Another analytical model for determining the optimal offset of limit orders is due to Foucault, Kadan, and Kandel (2005). This model explicitly suggests whether a trader should place a passive or an aggressive limit order, and how many ticks away from the market price should the trader place his limit order. The model makes the following key assumptions:

- All other execution parameters have been selected.
- All traders in the market are free to switch from passive to aggressive execution, and vice versa.

The determining factor in whether or not a trader decides to place a passive or an aggressive order, is the so-called "reservation spread," defined as follows:

$$j^{\mathsf{R}} = ceiling\left[\frac{\delta}{\mu\Delta}\right]$$

where

- δ is the market-maker's expected dollar-cost of execution that may incorporate expectations about market impact.
- Δ is the minimal tick size, say \$0.01 for equities.
- *μ* is the arrival rate of matching market orders per unit of time; with 1/ *μ* representing the average time between two sequential order arrivals. If the model is used to determine levels of aggressiveness of limit buy orders, *μ* is the rate of arrival of market sell orders, computed as a number of market sell orders recorded per unit of time. In Foucault et al. (2005), all orders, both market and limit, are assumed to be of the same size.

Foucault et al. (2005) use the reservation spread *j*g *R* to establish a shortrun equilibrium, where all traders achieve their optimality. To do so, Foucault et al. (2005) consider three different types of markets:

1. A market with identical (homogenous) traders.

2. A market with two different types of traders, facing diverging transaction costs.

3. A market with  $q$  different types of traders, with heterogeneous transaction costs.

The main intuition behind the model works as follows: The trader's reservation spread is the cost of executing the given order slice. If the current market spread is smaller than the trader's reservation spread, the trader can avoid additional costs associated with the risk of nonexecution, placing a market order. When the trader's execution costs per rate of arrival of opposing orders are smaller than the market spread, the trader places an aggressive limit order, shrinking the spread and further improving his cost structure by avoiding crossing the spread.

In a market with identical traders, all traders  $[1 \ldots q]$  have the same transaction costs, and face common arrival rates for opposing orders, resulting in equal reservation spreads:  $j_1^R = j_2^R = ... = j_q^R = j^R$ . In such a market, each trader would submit a limit order  $j^R$  ticks away from the market whenever the inside market spread *s* is greater than  $j^R$ , and submit a market order otherwise. Such a market is characterized by a highly competitive outcome, with traders shrinking market spreads to the minimum tick size.

In a market with two traders facing different transaction costs, similar dynamics take place. Trader 1 places a limit order  $j_1^R$  ticks away from the market whenever the market spread *s* is larger than  $j_1^R$ . Similarly, trader 2 places a limit order  $j_{2}^{R}$  ticks away from the market whenever the market spread *s* is larger than  $j_{2}^{R}$ . Yet, when the market inside spread *s* exceeds  $j_{1}^{R}$ and  $S < j_{2}^{R}$ , trader 2 places a market order, while trader 1 places a limit order  $j_1^R$  ticks away from the market price, potentially shrinking the spread. In this market with identically sized orders, no trader ever places a limit order "behind" the market or farther away from the market than the spread.

In a market with  $[1 \dots q]$  heterogeneous traders,  $j_1^R < j_2^R < \dots < j_q^R$ , similar dynamics hold: whenever the market spread  $s$  is smaller than the *i*th trader reservation spread  $j_i^R$ , all traders  $[i, ..., q]$  place market orders. All traders with reservation spread smaller than the market spread *s,* on the other hand, place limit orders at their reservation spread.

The differences in transaction costs of traders may be due to the following factors:

- Fees: Large institutional traders are likely to face lower fees than smaller traders.
- Market impact: Large child orders are expected to bear higher market impact than smaller order slices.
- Taxes: Individual investors may be subject to high marginal tax rates on their trading gains.
- Other quantifiable transaction costs.

The Foucault et al. (2005) model takes into account only the aggregate transaction cost facing a trader, and does not distinguish among various types of costs.

Key implications from Foucault et al. (2005) model, , include the following observations:

- Higher market order arrival rates lead to lower reservation spreads, and as a result, lower market spreads. As a result, competing market orders are good for the markets, lowering the costs of overall trading.
- Lower trading costs also lead to lower spreads, suggesting that rebates help facilitate cheaper execution, not to make trading more expensive.
- High execution costs and low market order arrival rates, however, result in wide reservation spreads, and may destroy markets by creating no-trade voids. Such conditions can be observed in long-dated futures markets following the ban of stub quotes: due to the low demand and the resulting low number of orders, traders in long-dated futures have traditionally "quoted wide," at large deviations from the market. The so-called quote stuffing ban adopted in Europe and the United States in 2010–2011 prohibits traders from placing limit orders farther than 10 percent away from the prevailing market price, eliminating the ability to trade in naturally wide-quoted markets, and hurting farmers, agricultural processors, and other consumption traders in the process.

While the Foucault et al. (2005) model presents groundbreaking foundation for predicting micro-trader behavior, several assumptions of the model deviate from market reality and thus limit its applicability. For one, the model assumes that all limit and market orders are always of the same size, and that the arrival of the opposing market orders *μ* and the execution costs δ are invariant with time. As a result, all limit orders in the model shrink the spread, and no limit orders behind the market price are ever placed, an impractical consequence in many today's markets where the spread has already contracted to the size of the minimum tick allowed.

## Trend-Dependent Offset

An improvement to basic market-making models may involve differentiation between trending and mean-reverting markets. In a meanreverting market, the price bounces up and down within a range, reducing the risk of adverse selection and making such market conditions perfect for market making. In trending markets, however, a market maker needs to reduce the size of limit orders on the "wrong" side of the markets, hedge the exposure, or exit the markets altogether. To determine whether the market is trending, the systems may deploy directional analysis, like the event-based frameworks presented in Chapter 9 and intelligent forecasting discussed in Chapter 11.

# Market Making as a Service

The key objective of market making was formally defined over 50 years ago as provision of "predictable immediacy" in supply and demand on security exchanges (see Demsetz, 1968). This predictable immediacy comprises *liquidity.*"

Intuitively, a service adding liquidity is particularly useful, and the associated premium and the strategy profitability particularly high, whenever the liquidity levels are low. By reverse logic, whenever the liquidity levels are particularly high, aggressive liquidity-consuming orders may deliver better profitability.

Many measures of liquidity have been developed over the years. Among the most popular metrics are:

- The tightness of the bid-ask spread.
- Market depth at best bid and best ask.
- Shape of the order book.
- Price sensitivity to block transactions.
- Price sensitivity to order-flow imbalance.
- Price change per unit volume.
- Technical support and resistance levels.
- Market resilience.

## The Tightness of the Bid-Ask Spread

The tightness of the bid-ask spread reflects the degree of competition among limit order–placing traders. The more traders are competing to post and execute limit orders, the closer will the traders post their limit orders to the market price, the tighter will be the resulting bid-ask spread. This metric is an easy liquidity test suitable for most markets, and particularly in markets with wide spreads, such as most U.S. equity options.

## Market Depth at Best Bid and Best Ask

In many securities, the bid-ask spread often reaches its minimum value and stays at the minimum value through the most market hours. For example, in commonly traded U.S. equities, the spread was often \$0.01 at the time this book was written. In such conditions, the tightness of the bid-ask spread loses its potency, and the relative liquidity levels can be approximated using market depth at the best bid and the best ask. The sizes at the best bid and ask can be thought of as the sizes of limit orders of traders that desire to be at the top of the book, if the minimum tick size were smaller.

## Shape of the Order Book

When available, Level II data can be used to calculate the exact amount of aggregate supply and demand available on a given trading venue. Using Level II data, supply and demand can be determined as the cumulative sizes

of limit orders posted on the sell and buy sides of the limit order book, respectively

Shape of the order book also helps separate immediately available top-ofthe-book liquidity from deeper-in-the-book "behind-the-market" liquidity. Such separation may be particularly interesting to market makers seeking to fine-tune their algorithms to post orders at selected price points. High liquidity observed deeper in the book may indicate presence of large investors. Academic research suggests that, when a large investor is present, all human and automated market makers choose to cater to that specific investor by placing aggressive limit orders on the opposite side of the limit order book. Handa, Schwartz, and Tiwari (2003), for example, find that when the order book is imbalanced due to the presence of a large investor, market makers on the opposing side of the book exert greater market power and obtain better prices from investors on the populous trading side.

Limit order books may also contain "holes," ranges of prices that are skipped by investors when submitting limit orders. Holes were empirically documented by Biais, Hillion, and Spatt (1995), among others. The impact of holes on trading has not been thoroughly studied.

#### Price Sensitivity to Block Transactions

When the Level II data are not available, the shape of the order book can still be estimated using techniques that hail from technical analysis, like support and resistance levels and moving averages. Due to the popularity of the support and resistance methodology, for example, many human traders as well as trading algos choose to place limit orders at the market support and resistance levels. Computing support and resistance helps pinpoint liquidity peaks without parsing cumbersome Level II information. This fact was first pointed out by Kavajecz and Odders-White (2004).

Mathematically, support and resistance levels are determined as linear projections of recent price minima in case of support, and maxima in case of resistance. To determine the support level one minute ahead, the algorithm would compute minimum prices within the past minute and the prior minute, and then project the minima trend one minute ahead:

(4)

Similarly, resistance level can be computed as:

(5)

In addition to support and resistance levels, indicators based on moving averages help identify the skewness of the order book. When a short-run moving average rises above a long-run moving average, the buy-side liquidity pool in the limit order book moves closer to the market price.

Kavajecz and Odders-White (2004) speculate that technical analysis remains popular in dark markets and markets without centralized order books, like foreign exchange, because the technical techniques help traders reverse-engineer unobservable limit order books and deploy profitable liquidity provision strategies.

#### Price Sensitivity to Order-Flow Imbalance

Price sensitivity to block transactions measures how the market price moves following an order. The main idea is that low liquidity makes a large market order "eat" through the limit order book, moving the market price substantially. Price sensitivity measures the relationship between the net directional trading volume and the price change induced by the trade size. The sensitivity parameter is known as *Kyle's lambda* after Kyle (1985):

(6)

where Δ*P<sup>t</sup>* is the change in market price from time *t* – 1 to time *t* due to the market impact of orders and *NVOL<sup>t</sup>* is the difference between sizes recorded at the best bid and best ask quotes at time *t*. Parameters α, λ, and ε*<sup>t</sup>* are then components of the linear regression specification of equation (6): ε*<sup>t</sup>* is the error term associated with each individual observation Δ*P<sup>t</sup>* , α is the intercept of the regression, and λ is the Kyle's lambda, the parameter of interest, measuring the sensitivity of price changes to net volume imbalance. The lower the lambda, the less sensitive the price to large directional trades, and the higher the liquidity available on the trading venue.

## Price Change per Unit Volume

A modified Kyle's lambda proposed by Aldridge (2012d) works as follows:

 $(7) \Delta P_t = \alpha + \lambda (S_t^b - S_t^a) + \varepsilon_t$ 

where  $\Delta P_{t}$  is a change in prices on executed trades observed during predefined time period *t*,  $S_t^b$  is the aggregate volume of trades executed at the best bid that was in force at the time each trade was processed during period *t*, and  $S^a$  is the volume of trades matched at the best ask prevailing at trade time. The difference between  $S_t^b - S_t^a$  can be interpreted as the net order flow imbalance observed during time period *t*: the volume executed at bid is likely to be generated by market sell orders, while the trades processed at ask are often a result of market buy orders.

#### Technical Support and Resistance Levels

Absolute price change per unit volume traded is yet another measure of liquidity:

$$\gamma_t = \frac{1}{D_t} \sum_{d=1}^{D_t} \frac{\left| r_{d,t} \right|}{v_{d,t}}$$

This metric is due to Amihud (2002) and is known as the illiquidity ratio. Similarly to Kyle's lambda, illiquidity ratio estimates size-induced change in price of the traded financial instrument. The smaller the average price change per unit of trading volume, the deeper is the available liquidity. While modified Kyle's lambda requires attribution of trades to prevailing bid and ask quotes, the metric of equation  $(8)$  assumes that the liquidity is balanced at all times, and accounts only for the absolute change in price per unit volume traded.

#### Market Resilience

Market resilience is yet another metric of liquidity and measures just how quickly the order book recovers its "shape" following a market order. Estimation of market resilience is discussed in Chapter 15 of this book.

# Profitable Market Making

To ensure that the market-making operation is profitable, several key conditions must hold. The conditions, dating back to Garman (1976), relate the arrival rates of limit orders, probability of gain and loss, and prices of traded instruments.

Temporary imbalances between buy and sell orders are due to differences between the individual trader and the way a dealer optimizes his order flow, which may reflect underlying differences in budgets, risk appetite, access to markets, and a host of other idiosyncrasies. The individual trader optimization problems themselves are less important than the aggregated order imbalances that these optimization differences help create. The market maker's objective is to maximize profits while avoiding bankruptcy or failure. The latter arise whenever the market maker has no inventory or cash. Both buy and sell orders arrive as independent stochastic processes.

The model solution for optimal bid and ask prices lies in the estimation of the rates at which a unit of cash (e.g., a dollar or a "clip" of 10 million in foreign exchange) "arrives" to the market maker when a customer comes in to buy securities (pays money to the dealer) and "departs" the market maker when a customer comes in to sell (the dealer pays the customer). Suppose the probability of an arrival, a customer order to buy a security at the market ask price *P<sup>a</sup>* is denoted λ*<sup>a</sup>* . Correspondingly, the probability of departure of a clip from the market maker to the customer, or a customer order to sell securities to the market maker at the bid price *P<sup>b</sup>* , can be denoted λ*<sup>b</sup>* .

The solution is based on the solution to a classical problem known as the Gambler's Ruin Problem. In the dealer's version of the Gambler's Ruin Problem, a gambler, or a dealer, starts out with a certain initial wealth position and wagers (stays in business) until he loses all his money. This version of the Gambler's Ruin Problem is known as an unbounded problem. The bounded problem assumes that the gambler bets until he either loses all his money or reaches a certain level of wealth, at which point he exits.

Under the Gambler's Ruin Problem, the probability that the gambler will lose all his money is

$$\text{Pr}_{\text{Failure}} = \left(\frac{\Pr(\text{Loss}) \times \text{Loss}}{\Pr(\text{Gain}) \times \text{Gain}}\right)^{\text{Initial Weight}}$$

where *Initial Wealth* is the gambler's start-up cash, Pr(*Loss*) is the probability of losing an amount (*Loss*) of the initial wealth, and Pr(*Gain*) is

the probability of gaining an amount (*Gain*).

From the Gambler's Ruin Problem, we can see that the probability of failure is always positive. It can be further shown that failure is certain whenever the probability of losing exceeds the probability of gaining. In other words, the minimum condition for a positive probability of avoiding failure in the long term is  $Pr(Gain) > Pr(Loss)$ .

Garman (1976) applies the Gambler's Ruin Problem to the market-making business in the following two ways:

1. The market maker fails if he runs out of cash.

2. The market maker fails if he runs out of inventory and is unable to satisfy client demand.

In modeling the Gambler's Ruin Problem for the market maker's ruin through running out of inventory, we assume that both the *Gain* and *Loss* variables are single units of the underlying financial asset. In other words,

 $Gain = 1$ 

 $Loss = 1$ 

In the case of equity, this unit may be a share of stock. In the case of foreign exchange, the unit may be a clip. Then, from the market maker's perspective, the probability of "losing" one unit of inventory is the probability of selling a unit of inventory, and it equals the probability  $\lambda$  of a buyer arriving. By the same logic, the probability of gaining one unit of inventory is  $\lambda_{\nu}$ , the probability of a seller arriving. The Gambler's Ruin Problem equation (9) now becomes

 $\lim_{t \to \infty} \text{Pr}_{\text{Failure}}(t) \approx \left(\frac{\lambda_a}{\lambda_b}\right)^{\text{InitialWealth/E}_o(P_e, P_b)}, \text{ if } \lambda_b > \lambda_a$ 

 $= 1$ , otherwise.  $(10)$ 

where  $E_{o}(P_{a}, P_{b})$  is the initial average price of an underlying unit of inventory and

#### Initial Wealth

 $E_0(p_a, p_b)$  is the initial number of units of the financial instrument in possession

of the market maker.

The Gambler's Ruin Problem is further applied to the market maker's probability of failure due to running out of cash. From the market maker's perspective, gaining a unit of cash—say a dollar—happens when a buyer of the security arrives. As before, the arrival of a buyer willing to buy at price  $P_{a}$  happens with probability  $\lambda_{a}$ . As a result, the market maker's probability of gaining a dollar is  $P_{a}$ . Similarly, the market maker's probability of "losing" or giving away a dollar to a seller of the security for selling the security at price  $P_{b}$  is  $\lambda_{b}$ . The Gambler's Ruin Problem now takes the following shape:

$$\lim_{t \to \infty} \text{Pr}_{\text{Failure}}(t) \approx \left(\frac{\lambda_b p_b}{\lambda_a p_a}\right)^{\text{InitialWeath}}, \text{ if } \lambda_a P_a > \lambda_a P_b$$

$$(11) = 1$$
, otherwise.

For a market maker to remain in business, the first conditions of equations  $(10)$  and  $(11)$  need to be satisfied simultaneously. In other words, the following two inequalities have to hold contemporaneously:

 $\lambda_{b} > \lambda_{a}$  and

 $\lambda_{a} p_{a} > \lambda_{a} p_{b}$ 

For both inequalities to hold at the same time, the following must be true at all times:  $p_{a} > p_{b}$ , defining the bid-ask spread. The bid-ask spread allows the market maker to earn cash while maintaining sufficient inventory positions. The reverse, however, does not hold true: the existence of the bidask spread does not guarantee that the market maker satisfies profitability conditions of equation  $(11)$ .

## Summary

Market making and any liquidity provision is a service to the markets and deserves compensation. Profitable automated market making is feasible with very simple models that only take into account inventory on the market maker's books. While Level II data is informative, and, therefore, desirable, the information delivered by Level II data can be extracted out of Level I data using simple techniques like technical analysis.

# End-of-Chapter Questions

1. What is market making? How does it differ from liquidity provision?

2. Why is market making inherently profitable?

3. What is the core market-making strategy? What are the common extensions?

4. What are the common measures of liquidity?

5. What are the minimum profitability conditions of market-making strategies?
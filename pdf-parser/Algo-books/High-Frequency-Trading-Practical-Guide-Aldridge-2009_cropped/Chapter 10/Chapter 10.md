# CHAPTER 10 **Trading on** Market Microstructure

Inventory Models

ational expectations and the efficient markets hypotheses imply that, following a relevant news release, market prices adjust instantaneously. From the perspective of a long-term investor, holding positions for days or months, the adjustment may indeed seem instantaneous. Anyone who has watched the markets surrounding a major news release, however, has observed a different picture—a volatile price that eventually settles within a specific price band. Note that the price eventually settles within a price range and not at a constant price level, because a degree of volatility, however small, accompanies all market conditions. The process of the market finding its optimal post-announcement price band is often referred to as tâtonnement, from French for "trial and error."

Figure 10.1 illustrates price adjustments as viewed at different frequencies. At very high frequencies, the price adjustment process is hardly instantaneous. The tâtonnement toward a new optimal price happens through the implicit negotiation among buyers and sellers that is occurring in the order flow; the market participants develop individual security valuations given the news, which are reflected in their bids and asks. These quotes provide market participants with information about other market participants' valuations. The process repeats until most market participants agree on a range of acceptable prices; the equilibrium price band can then be considered achieved. The process of tâtonnement, therefore, not only incorporates information into prices but also shapes beliefs of market participants through a form of collective bargaining process.

The discipline that studies the price formation process is known as market microstructure. Trading on market microstructure is the holy grail

![](_page_1_Figure_1.jpeg)

**FIGURE 10.1** USD/CHF price adjustments to Swiss unemployment news, recorded on July 8, 2009 at hourly (top panel) and tick-by-tick (bottom panel) frequencies.

of high-frequency trading. The idea of market microstructure trading is to extract information from the observable quote data and trade upon that extracted information in order to obtain gains. Holding periods for positions in market microstructure trading can vary in duration from seconds to hours.

The optimal holding period is influenced by the transaction costs faced by the trader. A gross average gain for a position held just several seconds will likely be in the range of several basis points (1 basis point = 1 bp = 1 pip = 0.01%), at most. To make such trading viable, the expected gain has to surpass the transaction costs. In an institutional setting (e.g., on a proprietary trading desk of a broker-dealer), a trader will often face transaction costs of 1 bp or less on selected securities, making a seconds-based trading strategy with an expected gain of at least 2 bps per trade quite profitable. Other institutional players, such as hedge funds, can expect their transaction costs to range anywhere from 3 bps to 30 bps per trade, mandating strategies that call for longer holding periods.

According to Lyons (2001), the field of market microstructure encompasses two general types of models—inventory models and information models. Information models are concerned with the process of impounding information into prices in response to news. With information models, order flow carries information that induces price changes. Inventory models, on the other hand, explain transitory variations in prices in the absence of news. As with information models, it is order flow that causes these temporary variations. Unlike information models where order flow is a result of end customers receiving and acting on information, inventory models concern themselves with the order flow resulting from dealer book imbalances.

This chapter reviews inventory models and their applications to highfrequency trading. The following chapter, Chapter 11, discusses information models.

## **OVERVIEW OF INVENTORY TRADING STRATEGIES**

Inventory trading, also known as liquidity provision or market making, concerns itself with profitable management of inventory. Liquidity provision was once performed only by dedicated broker-dealers, known as market makers. Market makers kept enough liquidity on hand to satisfy supply and demand of any arriving traders. During the past decade, this system changed. The proliferation of electronic transacting capability coupled with the 1997 SEC order display rule enabled most traders to place the short-term limit orders required to make markets. Several competitive liquidity provision strategies have emerged to profitably capture liquidity premiums available in the markets.

Inventory trading strategies possess the following key characteristics:

 The strategies are executed predominantly using limit orders, although an occasional market order is warranted to close a position.

- The strategies rely on a multitude of very small realized gains; it is not uncommon for these strategies to move in and out of positions 2,000 times per day.
- As a result, these strategies operate at very high frequencies; short position holding time is what makes it possible to move capital in and out of multiple trades, generating a large surplus at the end of each day.
- High-speed transmission of orders and low-latency execution are required for successful implementation of liquidity provision strategies.

# **ORDERS, TRADERS, AND LIQUIDITY**

### **Orders Used in Microstructure Trading**

Limit orders, first introduced in Chapter 6, are commitments to buy or sell a particular security at a prespecified price. Limit orders can be seen as ex-ante commitments to provide market liquidity. As noted by Demsetz (1968), while limit orders are in queue, the trader who placed limit orders incurs inventory and waiting costs. The inventory costs arise from the uncertainty as to the market price of the securities that the trader may hold in his portfolio while his limit orders are pending. The waiting costs are the opportunity costs associated with the time between placing an order and its execution. In addition, per Copeland and Galai (1983), limit orders suffer from an informational disadvantage, whereby they are picked off by better-informed investors.

Naturally, the probability of limit orders being executed depends on the limit order price proximity to the current market price. Cohen, Maier, Schwartz, and Whitcomb (1981), call this phenomenon a "gravitational pull" of existing quotes. Limit orders placed at current market quotes are likely to be executed, whereas the probability of execution for aggressive limit orders is close to zero.

Trading with limit orders generates nonlinear payoffs; sometimes limit orders execute and sometimes they do not. As a result, limit orders are difficult to model. As Parlour and Seppi (2008) point out, limit orders compete with other limit orders, both existing and those submitted in the future. Further, all limit orders execute against future market orders. Thus, when selecting the price and quantity for a limit order, the trader must take into account the future trading process, including the current limit order book, as well as past histories of orders and trading outcomes.

Early limit order models, known as static equilibrium models, presumed that limit order traders were to be compensated for providing liquidity. Examples of such models include Rock (1996), Glosten (1994), and Seppi (1997). The longer the waiting time until order execution, the higher was the expected compensation to liquidity providers who did not change their limit order specifications once they submitted the orders. The assumptions behind the static equilibrium models reflected early exchange conditions. Changing the details of a limit order was prohibitively costly, and market makers indeed expected a tidy compensation for bearing the risk of ending up in an adverse position once their limit orders were hit.

Static equilibrium models, however, have found little empirical support in the recent literature. In fact, Sandas (2001) in his study of limit orders on actively traded stocks on the Stockholm Stock Exchange finds that the expected profit on limit orders appears to decrease as the time duration between market orders increases, contradicting previously formulated theory. The implicit outcome of empirical evidence is that the limit orders are submitted by traders with active profit motives, rather than by market makers interested strictly in providing liquidity.

Demand for trading immediacy can be fueled by the traders' need for capital and their risk aversion, among other factors. Traders strapped for cash may choose to set the limit price close to the market to turn their positions into cash as soon as possible. Risk-averse traders may choose to set the limit price close to the market to ensure swift execution and to minimize uncertainty.

An extension to static equilibrium models penalizes aggressive limit orders with a non-execution cost. The cost can be considered a penalty for deviating too far from the trading targets of active limit order traders. Examples of such an approach include Kumar and Seppi (1994), who modeled two types of limit order traders—value traders and liquidity traders. Value traders submit limit orders to exploit undervalued limit orders but have no other reason to trade. Liquidity traders submit limit orders to respond to random liquidity shocks; randomness in their orders leads to price risk for other traders' market orders and execution risk in all limit orders. Cao, Hansch, and Wang (2004) find cointegration of different orders in the limit order book, supporting the existence of value traders.

#### **Trader Types in Market Microstructure Trading**

Harris (1998) identifies three types of traders:

- **1.** Informed traders, who possess material information about an impending market move
- **2.** Liquidity traders (also known as uninformed traders), who have no material market insights and aim to profit from providing liquidity and following short-term price momentum

**3.** Value-motivated traders, who wait for security prices to become cheap relative to their proprietary valuations of security based on fundamental indicators

Informed traders possess private information that allows them to predict future price changes in a particular security. Private information can include analyses from paid-for news sources, like Bloomberg, not yet available to the general public, and superior forecasts based on market microstructure. Informed traders are often high-frequency money managers and other proprietary traders with superior access to information and skill in assessing immediate market situations. The informed traders' private information can make a significant impact on the market. As a result, informed traders are impatient and typically execute their orders at market prices or at prices close to market (see Vega [2007]). Alam and Tkatch (2007) find that institutional orders are more likely to be market orders as opposed to limit orders, potentially reflecting advanced information and skill of institutional money managers.

Liquidity (or uninformed) traders specialize in crafting order submission strategies in an effort to capture best prices for their customers. These traders have little proprietary information about the true value of the security they trade. Executing broker-dealers are examples of liquidity traders.

Value traders run models to determine the fair value of each security, based on the publicly available information. Value traders might be traditional, low-frequency, institutional money managers; individual daytraders; or high-frequency managers running high-frequency fundamental models.

These three types of traders decide when to submit a market order as opposed to a limit order and at what price to submit a limit order. Such decisions are optimized to minimize trading costs and maximize portfolio returns.

According to Harris (1998), market orders and aggressively priced limit orders are placed by impatient traders, those with material market information about to become public. Limit orders that are far away from the current market price are typically placed by value traders, those seeking to obtain bargain prices. The remaining limit orders are placed by uninformed liquidity traders who are attempting to profit from making markets and from detecting and following short-term price momentum. Figure 10.2 illustrates the distributions of order aggressiveness and trader types relative to the market price in the limit order book. Harris (1998) considers a market for a single security, so that no substitute securities can be traded in place of an overpriced or illiquid security.

![](_page_6_Figure_1.jpeg)

**FIGURE 10.2** A graphical representation of order aggressiveness and trader type distributions in the limit order book.

Kaniel and Liu (2006) extend Angel (1992) and Harris (1998) to show that informed investors may use limit orders whenever their private information has a sufficient degree of persistence. Bloomfield, O'Hara, and Saar (2005) discuss how informed investors are natural liquidity providers. Because the informed investors know the true value of an asset, they are the first to know when the prices have adjusted to the levels at which the limit orders cannot be picked off by other traders. Measures of aggressiveness of the order flow may capture informed traders' information and facilitate generation of short-term profits.

### **Liquidity Provision**

Limit orders provide market liquidity. As such, limit orders may fare better in lower-liquidity markets. The extent of market liquidity available can be assessed using one or more of the following measures:

- **1. The tightness of the bid-ask spread.** The bid-ask spread indicates the cost of instantaneous reversal of a given position for a standard trading amount, or "clip."
- **2. Market depth.** The depth of the market is the size of all limit orders posted at the current market price (the best limit price). Market depth therefore indicates the size of the order that can be processed immediately at the current market price.
- **3. Market resilience.** Market resilience is a measure of how quickly the market price mean-reverts to its equilibrium level following a random order flow.
- **4. Price sensitivity to block transactions.** The sensitivity is most often measured by what came to be known as "Kyle's λ," which is a

coefficient from OLS estimation of the following regression (Kyle, 1985):

$$\Delta P_t = \alpha + \lambda NVOL_t + \varepsilon_t \tag{10.1}$$

where -*Pt* is the change in market price due to the market impact of orders and *NVOLt* is the difference between the buy and sell market depths in period *t*. The smaller the market sensitivity to transaction size, λ, the larger the market's capacity to absorb orders at the current market price.

**5. Illiquidity ratio of Amihud (2002).** Amihud (2002) notes that illiquid markets are characterized by more drastic relative price changes per trade. Although changes in trade prices in the most liquid securities can be as low as one tick (e.g., 0.005 of 1 percent in most currency markets), in illiquid markets the changes in trade prices can be as large as 20 percent per trade. Amihud (2002), therefore, proposes to measure the degree of market illiquidity as the average ratio of relative price change to quantity traded:

$$\gamma_t = \frac{1}{D_t} \sum_{d=1}^{D_t} \frac{|r_{d,t}|}{\nu_{d,t}} \tag{10.2}$$

where *Dt* is the number of trades executed during time period *t*, *rd,t* is the relative price change following trade *d* during trade period *t*, and ν*d,t* is the trade quantity executed within trade *d*.

Limit order books are also often characterized by the presence of "holes"—that is, ranges of prices that are skipped by investors when submitting limit orders. Holes were empirically documented by Biais, Hillion and Spatt (1995), among others.

### **PROFITABLE MARKET MAKING**

Harrison and Kreps (1978) showed that the current value of an asset is determined by its resale potential; as a result, high-frequency investors trading in multiple markets arbitrage away price discrepancies among markets. The simplest profitable liquidity provision strategy involves identification of mispricings on the same security across different markets and arbitraging away the difference. This is done by posting a limit order to buy just below the market price in the low-priced market and a limit order to sell just above market in the high-priced market, and then reversing the positions once transaction costs were overcome.

Garman  $(1976)$  was the first to investigate the optimal market-making conditions through modeling temporary imbalances between buy and sell orders. These imbalances are due to differences between the individual trader and the way a dealer optimizes his order flow, which may reflect underlying differences in budgets, risk appetite, access to markets, and a host of other idiosyncrasies. The individual trader optimization problems themselves are less important than the aggregated order imbalances that these optimization differences help create. In the Garman (1976) model, the market has one monopolistic market maker (dealer). The market maker is responsible for deciding on and then setting bid and ask prices, receiving all orders, and clearing trades. The market maker's objective is to maximize profits while avoiding bankruptcy or failure. The latter arise whenever the market maker has no inventory or cash. Both buy and sell orders arrive as independent stochastic processes.

The model solution for optimal bid and ask prices lies in the estimation of the rates at which a unit of cash (e.g., a dollar or a "clip" of 10 million in FX) "arrives" to the market maker when a customer comes in to buy securities (pays money to the dealer) and "departs" the market maker when a customer comes in to sell (the dealer pays the customer). Suppose the probability of an arrival, a customer order to buy a security at the market ask price  $p_a$  is denoted  $\lambda_a$ . Correspondingly, the probability of departure of a clip from the market maker to the customer, or a customer order to sell securities to the market maker at the bid price  $p_b$ , can be denoted  $\lambda_b$ . Garman (1976) proposes a simple but effective model for the minimum bidask spreads necessary in order for the market maker to remain viable.

The model's solution is based on the solution to a classical problem known as the Gambler's Ruin Problem. In the dealer's version of the Gambler's Ruin Problem, a gambler, or a dealer, starts out with a certain initial wealth position and wagers (stays in business) until he loses all his money. This version of the Gambler's Ruin Problem is known as an unbounded problem. The bounded problem assumes that the gambler bets until he either loses all his money or reaches a certain level of wealth, at which point he exits.

Under the Gambler's Ruin Problem, the probability that the gambler will lose all his money is

$$\Pr_{Failure} = \left(\frac{\Pr(\text{Loss}) \times \text{Loss}}{\Pr(\text{Gain}) \times \text{Gain}}\right)^{\text{Initial Wealth}} \tag{10.3}$$

where *Initial Wealth* is the gambler's start-up cash,  $Pr(Loss)$  is the probability of losing an amount ( $Loss$ ) of the initial wealth, and  $Pr(Gain)$  is the probability of gaining an amount  $(Gain)$ .

From the Gambler's Ruin Problem, we can see that the probability of failure is always positive. It can be further shown that failure is certain whenever the probability of losing exceeds the probability of gaining. In other words, the minimum condition for a positive probability of avoiding failure in the long term is Pr(*Gain*) > Pr(*Loss*).

Garman (1976) applies the Gambler's Ruin Problem to the marketmaking business in the following two ways:

- **1.** The market maker fails if he runs out of cash.
- **2.** The market maker fails if he runs out of inventory and is unable to satisfy client demand.

In modeling the Gambler's Ruin Problem for the market maker's ruin through running out of inventory, we assume that both the *Gain* and *Loss* variables are single units of the underlying financial asset. In other words,

$$Gain = 1$$
  
 $Loss = 1$ 

In the case of equity, this unit may be a share of stock. In the case of foreign exchange, the unit may be a clip. Then, from the market maker's perspective, the probability of "losing" one unit of inventory is the probability of selling a unit of inventory, and it equals the probability λ*<sup>a</sup>* of a buyer arriving. By the same logic, the probability of gaining one unit of inventory is λ*b*, the probability of a seller arriving. The Gambler's Ruin Problem equation (1) now becomes

$$\lim_{t \to \infty} \Pr_{Failure}(t) \approx \left(\frac{\lambda_a}{\lambda_b}\right)^{Initial\; Wealth/E_0(p_a, p_b)}, \quad \text{if } \lambda_b > \lambda_a \\ = 1, \text{ otherwise.} \tag{10.4}$$

where *E*0(*pa*, *pb*) is the initial average price of an underlying unit of inventory and

$$\frac{\textit{Initial Wealth}}{E_0(p_a,\,p_b)}$$

is the initial number of units of the financial instrument in possession of the market maker.

The Gambler's Ruin Problem is further applied to the market maker's probability of failure due to running out of cash. From the market maker's perspective, gaining a unit of cash—say a dollar—happens when a buyer of the security arrives. As before, the arrival of a buyer willing to buy at price *pa* happens with probability λ*a*. As a result, the market maker's probability of gaining a dollar is *pa*. Similarly, the market maker's probability of "losing" or giving away a dollar to a seller of the security for selling the security at price *pb* is λ*b*. The Gambler's Ruin Problem now takes the following shape:

$$\lim_{t \to \infty} \Pr_{Failure}(t) \approx \left(\frac{\lambda_b \, p_b}{\lambda_a \, p_a}\right)^{Initial \; Wealth}, \quad \text{if } \lambda_a \, p_a > \lambda_b \, p_b \\ = 1, \text{ otherwise} \tag{10.5}$$

For a market maker to remain in business, the first conditions of equations (10.4) and (10.5) need to be satisfied simultaneously. In other words, the following two inequalities have to hold contemporaneously:

λ*<sup>b</sup>* > λ*<sup>a</sup>* and λ*<sup>a</sup> pa* > λ*<sup>b</sup> pb*

For both inequalities to hold at the same time, the following must be true at all times: *pa* > *pb*, defining the bid-ask spread. The bid-ask spread allows the market maker to earn cash while maintaining sufficient inventory positions.

Other inventory models assume more detailed specifications for the market maker's objectives and constraints. For example, Stoll (1978) assumes that the main objective of the dealer is not only to stay in business but to effectively manage his portfolio in the face of market pressures. The bid-ask spread is the market maker's reward for bearing the costs of market making. These costs arise from the following three sources:

- **1.** Inventory costs—the market maker often is left holding a suboptimal position in order to satisfy market demand for liquidity.
- **2.** Order processing costs specific to the market maker's own trading mechanism—these costs may involve exchange fees, settlement and trade clearing costs, and transfer taxes, among other charges.
- **3.** The information asymmetry cost—a market maker trading with wellinformed traders may often be forced into a disadvantaged trading position.

As a result, Stoll's (1978) model predicts that the differences in bidask spreads between different market makers are a function of the market makers' respective risk tolerances and execution set-ups.

In Ho and Stoll (1981), the market maker determines bid and ask prices so as to maximize wealth while minimizing risk. The market maker controls his starting wealth positions, as well as the amounts of cash and inventory held on the book at any given time. As in Garman (1976), the arrival rates of bid and ask orders are functions of bid and ask prices, respectively. In the outcome of the Ho and Stoll (1981) model, the market maker's spreads depend on the his time horizon. For example, as the market maker nears the end of the day, the possible changes in positions become smaller, and consequently the market maker's risk of carrying a position decreases. Therefore, the market maker may lower the spread towards the end of the day. On the other hand, when the market maker's time horizon increases, he increases the spread to be compensated for a higher probability of an adverse movement to the market maker's book positions.

Avellaneda and Stoikov (2008) transform Garman's model into a quantitative market-making limit order book strategy that generates persistent positive returns. Furthermore, the strategy outperforms the "best-bid-bestask" market-making strategy where the trader posts limit orders at the best bid and ask available on the market. For fully rational, "risk-neutral" traders, the strategy of Avellaneda and Stoikov (2008) also outperforms the "symmetric" bid and ask strategy whereby the trader places bid and ask limit orders that are equidistant from the current mid-market price.

Avellaneda and Stoikov (2008) focus on the effects of inventory risk and derive the optimal bid and ask limit prices for the market maker, given the following six parameters:

- **The frequency of new bid quotes,** λ*<sup>b</sup>*. For example, λ*<sup>b</sup>* can be five per minute. The frequency of bid quotes can be thought of as demand for a given security as it reflects the arrival of new sellers.
- **The frequency of new ask quotes,** λ*<sup>a</sup>*. The frequency of ask quotes can be thought of as an indicator of supply of a given security and the probability that new buyers will emerge.
- **The latest change in frequency of new bid quotes,** λ*<sup>b</sup>*. For example, if 5 bid quotes arrived during the last minute, but 10 bid quotes arrived during the previous minute, then the change in the bid arrival frequency is λ*<sup>b</sup>* = (5 − 10)/10 = –0.5.
- **The latest change in frequency of new ask quotes,** λ*<sup>a</sup>*. For example, if 5 ask quotes arrived during the last minute, and 5 ask quotes arrived during the previous minute, then the change in the ask arrival frequency is λ*<sup>a</sup>* = (5 − 5)/5 = 0.
- **The relative risk aversion of the trader,** γ . A small value of risk aversion, γ ∼ 0, represents a risk-neutral investor. A risk aversion of 0.5, on the other hand, represents a very risk-averse investor.
- **The trader's reservation prices.** These are the highest price at which the trader is willing to buy a given security, *r<sup>b</sup>*, and the lowest price at which the trader is willing to sell a given security, *r<sup>a</sup>*. Both *r<sup>a</sup>* and *r<sup>b</sup>* are determined from a partial differential equation with the security price, *s*, trader's inventory, *q*, and time, *t*, as inputs.

The optimal limit bid price, *b*, and limit ask price, *a*, are then determined as follows:

$$b = r^b - \frac{1}{\gamma} \ln \left( 1 - \gamma \frac{\lambda^b}{\Delta \lambda^b} \right) \quad \text{and} \quad a = r^a - \frac{1}{\gamma} \ln \left( 1 - \gamma \frac{\lambda^a}{\Delta \lambda^a} \right)$$

Avellaneda and Stoikov (2008) offer the following comparisons of their inventory strategy with best bid/best ask and symmetric strategies for a reasonable trader risk aversion of 0.1. As Figure 10.3 shows, the inventory strategy proposed by Avellaneda and Stoikov (2008) has a narrow profit distribution, resulting in a high Sharpe ratio trading performance.

### **DIRECTIONAL LIQUIDITY PROVISION**

#### **When the Limit Order Book Is Observable**

One of the key observations of inventory models is that the shape of the order book is predictive of impending changes in the market price. Figure 10.4 illustrates the phenomenon identified by Cao, Hansch, and Wang (2004). In panel (a), market price is "pushed" by a large concentration of conservative limit orders.

Cao, Hansch, and Wang (2004) find that the shape of the limit order book is actively exploited by market-making traders. Cao, Hansch, and Wang (2004) also find that the breadth and depth (also known as the length and height) of the limit order book predicts 30 percent of the impending price moves. Furthermore, the asymmetry in the order book generates additional information. Handa, Schwartz, and Tiwari (2003) find that the bidask spread is greater in "balanced" markets when the number of buyers and sellers is comparable; conversely, the bid-ask spread is lower whenever the number of traders on one side of the trading equation exceeds the number of traders on the other side. According to Handa, Schwartz, and Tiwari (2003), this imbalance effect stems from the fact that the few traders on the sparse trading side exert greater market power and obtain better prices from the investors on the populous trading side who are desperate to trade.

Rosu (2005) determines that the shape of the limit order book depends on the probability distribution for arriving market orders. High probabilities of large market orders lead to hump-shaped limit order books. Foucault, Kadan, and Kandel (2005) model continuous-time markets as an order-determination process on a multiprice grid with infinitely lived limit orders. Rosu (2005) extends the research with cancelable limit orders.

![](_page_13_Figure_1.jpeg)

**FIGURE 10.3** Comparison of performance of inventory, best bid/best ask, and symmetric strategies per Avellaneda and Stoikov (2008).

![](_page_14_Figure_1.jpeg)

**FIGURE 10.3** (*Continued*)

Panel a): market price gets "pushed" by a large concentration of conservative limit orders.

![](_page_14_Figure_4.jpeg)

Current market price

Panel b): market price gets "pulled" by a large concentration of aggressive limit orders.

![](_page_14_Figure_7.jpeg)

Current market price

**FIGURE 10.4** Limit book distribution and subsequent price moves.

Foucault, Moinas, and Theissen (2005) find that the depth of the limit order book can forecast future volatility of asset prices. In Holden and Subrahmanyam (1992), the more volatile the common valuation of the traded asset, the lower the depth of the information that can be gleaned from the limit order book. As a result, the limit order market multiplies the changes in volatility of the traded asset; small changes in the volatility of the value of the traded asset lead to large changes in volatility of transaction prices, and informed traders are less likely to provide liquidity.

Berber and Caglio (2004) find that limit orders carry private information around events such as earnings announcements.

The ability to observe the limit order book in full, however, can deliver unfair advantage to market makers. Harris and Panchapagesan (2005) show that market makers able to fully observe the information in the limit order book can extract abnormal returns, or "pick off" other limit traders.

#### **When the Limit Order Book Is Not Observable**

The directional strategy based on Cao, Hansch, and Wang (2004) requires full transparency of the limit order book for the instrument of interest. In many trading venues (e.g., dark pools), the limit order book is not available. This section discusses approaches for estimating the shape of the order book.

Kavajecz and Odders-White (2004) show limit orders to be indicative of future pockets of liquidity. Technical analysis has long been a friend of traders and a bane of academics. The amount of resources dedicated to technical analysis in the investment management industry, however, continues to puzzle academics, who find little plausible explanation for technical inferences in the science of economics. Most seem to agree that technical analysis is a self-fulfilling prophecy; when enough people believe that a particular pricing move is about to occur, they drive the price to its target location. Yet, technical analysis is more popular in some markets than in others; for example, many foreign exchange traders actively use technical analysis, while proportionally fewer equity traders do.

An interesting new application of technical analysis has been uncovered by Kavajecz and Odders-White (2004). The authors find that technical analysis may provide information about the shape of the limit book. Specifically, Kavajecz and Odders-White (2004) find that traders are more likely to place limit orders at the technical support and resistance levels. Thus, the support and resistance indicators pinpoint the liquidity peaks in the limit order book. This finding may be particularly helpful to ultra–high-frequency traders working in opaque or dark markets.

In addition, Kavajecz and Odders-White (2004) find that indicators based on moving averages help identify the skewness of the order book. When a short-run moving average rises above a long-run moving average, the buy-side liquidity pool in the limit order book moves closer to the market price. In this sense, moving average indicators help determine the skewness of the limit order book. Kavajecz and Odders-White (2004) speculate that the popularity of technical analysis in foreign exchange is driven by the absence of a centralized limit order book in the foreign exchange market. The authors believe that technical analysis helps traders reverse-engineer limit order books and deploy profitable liquidity provision strategies.

### **CONCLUSION**

How does one take advantage of the opportunities present at ultra-high frequencies? First, a thorough econometric analysis of past short-term price and order book variability can be used to reveal a set of relationships that can be traded upon. Next, traders can simultaneously submit vectors of market and limit orders to promptly react to random fluctuations in buying and selling interest. The uncertainty in the timing of execution of limit orders, however, must be competently managed because it leads to random slippage in traders' portfolios, introducing a potentially undesirable stochastic dimension to their portfolio holdings.

Liquidity provision is not only profitable but is also an important function. As Parlour and Seppi (2008) note, valuation of publicly traded assets is a "social activity," strengthening the connection between liquidity and asset prices. Thus, trading activity creates value to investors who wish to reallocate their portfolios in response to changes in their personal valuations of assets.
# CHAPTER 11 **Trading on** Market Microstructure

Information Models

nventory models, discussed in Chapter 10, propose ways in which a market maker can set limit order prices based on characteristics of the market maker such as inventory (limit order book) and risk preferences. As such, inventory models do not account for motivations of other market participants. The dynamics relating to the trading rationale and actions of other market participants, however, can significantly influence the market maker's behavior.

Information models specifically address the intent and future actions of various market participants. Information models include game-theoretic approaches to reverse-engineer quote and trade flows to discover the information a market maker possesses. Information models also use observed or inferred order flow to make informed trading decisions.

At their core, information models describe trading on information flow and possible informational asymmetries arising during the dissemination of information. Differences in information flow persist in different markets. Information flow is comparably faster in transparent centralized markets, such as most equity markets and electronic markets, and slower in the opaque markets, such as foreign exchange and OTC markets in bonds and derivatives.

The main outcome of information models is that the bid-ask spreads persist even when the market maker has unlimited inventory and is able to absorb any trading request instantaneously. In fact, the spread is the way that the market maker stays solvent in the presence of well-informed traders. As the order flow from informed traders to the market maker conveys information from traders to the market maker, the subsequent changes in the bid-ask spread may also convey information from the market maker to other market participants.

This chapter describes information-based microstructure trading strategies.

# MEASURES OF ASYMMETRIC INFORMATION

Asymmetric information present in the markets leads to adverse selection, or the ability of informed traders to "pick off" uninformed market participants. According to Dennis and Weston (2001) and Odders-White and Ready (2006), the following measures of asymmetric information have been proposed over the years:

- Quoted bid-ask spread
- Effective bid-ask spread
- Information-based impact
- Adverse-selection components of the bid-ask spread
- Probability of informed trading

# **Quoted Bid-Ask Spread**

The quoted bid-ask spread is the crudest, yet most readily observable measure of asymmetric information. First suggested by Bagehot (1971) and later developed by numerous researchers, the bid-ask spread reflects the expectations of market movements by the market maker using asymmetric information. When the quoting dealer receives order flow that he suspects may come from an informed trader and may leave the dealer at a disadvantage relative to the market movements, the dealer increases the spread he quotes in order to compensate himself against potentially adverse uncertainty in price movements. As a result, the wider the quoted bid-ask spread, the higher the dealer's estimate of information asymmetry between his clients and the dealer himself. Given that the dealer has the same access to public information as do most of the dealer's clients, the quoted bid-ask spread may serve as a measure of asymmetric information available in the market at large at any given point in time.

## **Effective Bid-Ask Spread**

The effective bid-ask spread is computed as twice the difference between the latest trade price and the midpoint between the quoted bid and ask prices, divided by the midpoint between the quoted bid and ask prices. The effective spread, therefore, produces a measure that is virtually identical to the quoted bid-ask spread but reflects the actual order book and allows comparison among financial instruments with various price levels.

#### **Information-Based Impact**

The information-based impact measure of asymmetric information is attributable to Hasbrouck (1991). Brennan and Subrahmanyam (1996) specify the following vector autoregressive (VAR) model for estimation of the information-based impact measure,  $\lambda$ :

$$V_{i,t} = \theta_{i,0} + \sum_{k=1}^{K} \beta_{i,k} \Delta P_{i,t-k} + \sum_{m=1}^{M} \gamma_{i,m} V_{i,t-m} + \tau_{i,t}$$
(11.1)

$$\Delta P_{i,t} = \phi_{i,0} + \phi_{i,1} \text{sign}(\Delta P_{i,t}) + \lambda_i \tau_{i,t} + \varepsilon_{i,t}$$
(11.2)

where  $\Delta P_{i,t}$  is the change in price of security *i* from time  $t-1$  to time *t*,  $V_{i,t} = \text{sign}(\Delta P_{i,t}) \cdot v_{i,t}$ , and  $v_{i,t}$  is the volume recorded in trading the security *i* from time  $t-1$  to time *t*. Brennan and Subrahmanyam (1996) propose five lags in estimation of equation (1):  $K = M = 5$ .

#### Adverse Selection Components of the **Bid-Ask Spread**

The adverse selection components of the bid-ask spread is attributable to Glosten and Harris (1988). The model separates the bid-ask spread into the following three components:

- Adverse selection risk
- Order-processing costs
- Inventory risk

Models in a similar spirit were proposed by Roll (1984); Stoll (1989); and George, Kaul, and Nimalendran (1991). The version of the Glosten and Harris (1988) model popularized by Huang and Stoll (1997) aggregates inventory risk and order-processing costs and is specified as follows:

$$\Delta P_{i,t} = (1 - \lambda_i) \frac{S_{i,t}}{2} \text{sign}(\Delta P_{i,t}) + \lambda_i \frac{S_{i,t}}{2} \text{sign}(\Delta P_{i,t}) \cdot v_{i,t} + \varepsilon_{i,t} \qquad (11.3)$$

where  $\Delta P_{i,t}$  is the change in price of security i from time  $t-1$  to time t,  $V_{i,t} = \text{sign}(\Delta P_{i,t}) \cdot v_{i,t}, v_{i,t}$  is the volume recorded in trading the security i

from time *t-*1 to time *t*, *Si,t* is the effective bid-ask spread as defined previously, and λ*<sup>i</sup>* is the fraction of the traded spread due to adverse selection.

#### **Probability of Informed Trading**

Easley, Kiefer, O'Hara, and Paperman (1996) propose a model to distill the likelihood of informed trading from sequential quote data. The model reverse-engineers the quote sequence provided by a dealer to obtain a probabilistic idea of the order flow seen by the dealer.

The model is built on the following concept: Suppose an event occurs that is bound to impact price levels but is observable only to a select group of investors. Such an event may be a controlled release of selected information or a research finding by a brilliant analyst. The probability of such an event is α. Furthermore, suppose that if the event occurs, the probability of its having a negative effect on prices is δ and the probability of the event having a positive effect on prices is (1-δ). When the event occurs, informed investors know of the impact the event is likely to have on prices; they then place trades according to their knowledge at a rate µ. Thus, all the investors informed of the event will place orders on the same side of the market—either buys or sells. At the same time, investors uninformed of the event will keep placing orders on both sides of the market at a rate ω. The probability of informed trading taking place is then determined as follows:

$$PI = \frac{\alpha\mu}{\alpha\mu + 2\omega} \tag{11.4}$$

The parameters α, µ, and ω are then estimated from the following likelihood function over *T* periods of time:

$$L(B, S|\alpha, \mu, \omega, \delta) = \prod_{t=1}^{T} \ell(B, S, t|\alpha, \mu, \omega, \delta)$$
(11.5)

where (*B*, *S*,*t*|α,µ,ω,δ) is the daily likelihood of observing *B* buys and *S* sells:

$$\ell(B, S, t | \alpha, \mu, \omega, \delta) = (1 - \alpha) \left[ \exp(-\omega T) \frac{(\omega T)^B}{B!} \right] \left[ \exp(-\omega T) \frac{(\omega T)^S}{S!} \right]$$
$$+ \alpha (1 - \delta) \left[ \exp(-(\omega + \mu)T) \frac{((\omega + \mu)T)^B}{B!} \right] \left[ \exp(-\omega T) \frac{(\omega T)^S}{S!} \right] \quad (11.6)$$
$$+ \alpha \delta \left[ \exp(-\omega T) \frac{(\omega T)^B}{B!} \right] \left[ \exp(-(\omega + \mu)T) \frac{((\omega + \mu)T)^S}{S!} \right]$$

#### **INFORMATION-BASED TRADING MODELS**

#### **Trading on Information Contained in Bid-Ask Spreads**

Liquidity-providing market participants (or market makers) use bid-ask spreads as compensation for bearing the costs of market making. These costs arise from the following four sources:

- **1. Order-processing costs.** Order-processing costs are specific to the market maker's own trading platform. These costs may involve exchange fees, settlement and trade clearing costs, transfer taxes, and the like. To transfer the order-processing costs to their counterparties, market makers simply increase the bid-ask spread by the amount it costs market makers to process the orders.
- **2. Inventory costs.** Market makers often find themselves holding suboptimal positions in order to satisfy market demand for liquidity. They therefore increase the bid-ask spreads they quote to their counterparties to slow down further accumulation of adverse positions, at least until they are able to distribute their inventory among other market participants.
- **3. Information asymmetry costs.** A market maker trading with wellinformed traders may often be forced into a disadvantageous trading position. For example, if a well-informed trader is able to correctly forecast that EUR/JPY is about to increase by 1 percent, then the wellinformed trader buys a certain amount of EUR/JPY from the market maker, leaving the market maker holding a short position in EUR/JPY in the face of rising EUR/JPY. To hedge his risk of ending up in such situations, the market maker widens the bid-ask spreads for all of his counterparties, informed and uninformed alike. The bid-ask spread on average compensates for the market maker's risk of being at a disadvantage.
- **4. Time-horizon risk.** Most market makers are evaluated on the basis of their daily performance, with a typical trading day lasting eight hours. At the end of each trading day, the market maker closes his position book or transfers the book to another market maker who takes the responsibility and makes decisions on all open positions. At the beginning of each trading shift, a market maker faces the risk that each of his open market positions may move considerably in the adverse direction by the end of the day if left unattended. As the day progresses, the market maker's time horizon shrinks, and with it shrinks the risk

of a severely adverse move by the traded security. The market maker uses the bid-ask spreads he quotes to his counterparties to hedge the time-horizon risk of his own positions. The bid-ask spreads are greatest at the beginning of the trading day and smallest at the end of each trading day.

Figures 11.1–11.3 illustrate the first three dimensions per Lyons (2001). If bid-ask spreads were to compensate the dealer for order processing costs only, then the mid-price does not change in response to the

![](_page_5_Figure_3.jpeg)

**FIGURE 11.1** Order-processing costs.

![](_page_5_Figure_5.jpeg)

**FIGURE 11.2** Inventory costs.

![](_page_5_Figure_7.jpeg)

**FIGURE 11.3** Asymmetric information (adverse selection).

order. If bid-ask spreads were to compensate the dealer for the risks associated with holding excess inventory, then any changes in prices would be temporary. If all orders were to carry information that led to permanent price changes, the bid-ask spreads would compensate the dealer for the potential risk of encountering adverse asymmetric information.

Analyzing the bid-ask spreads of the market maker gives clues to the position sizes of the market maker's inventory and allows the market maker to estimate the order flow faced by the market maker. Unexpectedly widening spreads may signal that the market maker has received and is processing large positions. These positions may be placed by well-informed institutional traders and may indicate the direction of the security price movement in the near future. Information about future price movements extracted from the bid-ask spreads may then serve as reliable forecasts of direction of upcoming price changes.

Gains achieved in the markets are due either to market activity or to trading activity. Market gains, also referred to as capital gains, are common to most long-term investors. When markets go up, so do the gains of most investors long in the markets; the opposite occurs when the markets go down. Over time, as markets rise and fall, market investors expect to receive the market rate of return on average. As first noted by Bagehot (1971), however, the presence of short-term speculative traders may skew the realized return values.

If a market maker knew for sure that a specific trader had superior information, that market maker could raise the spread for that trader alone. However, most traders trade on probabilities of specific events occurring and cannot be distinguished ahead of closing their positions from uninformed market participants. To compensate for the informed trader–related losses, the market maker will extract higher margins from all of his clients by raising the bid-ask spread. As a result, in the presence of well-informed traders, both well-informed and less-informed market participants bear higher bid-ask spreads.

Important research on the topic is documented in Glosten and Milgrom (1985). The authors model how informed traders' orders incorporate and distribute information within a competitive market. At the fundamental level, traders who have bad news about a particular financial security ahead of the market will sell that security, and traders with good news will buy the security. However, well-informed traders may also buy and sell to generate liquidity. Depending on the type of the order the market maker receives (either a buy or a sell), the market maker will adjust his beliefs about the impending direction of the market for a particular financial security. As a result, the market maker's expected value of the security changes, and the market maker subsequently adjusts the bid and the ask prices he is willing to trade upon with his clients.

Glosten and Milgrom (1985) model the trading process as a sequence of actions. First, some traders obtain superior information about the true value of the financial security, *V*, while other market participants do not. Informed traders probabilistically profit more often than do uninformed traders and consequently are interested in trading as often as possible. Because informed traders know the true value *V*, they will always gain at the expense of the uninformed traders. The uninformed traders may choose to trade for reasons other than short-term profits. For example, market participants such as long-term investors uninformed of the true value of the security one minute from now may have a pretty good idea of the true value of the security one day from now. These uninformed investors are therefore willing to trade with an informed trader now even though in just one minute the investors could get a better price, unbeknownst to them at present. In the foreign exchange market, uninformed market participants such as multinational corporations may choose to trade to hedge their foreign exchange exposure.

The informed traders' information gets impounded into prices by the market maker. When a market maker receives an order, the market maker reevaluates his beliefs about the true value of the financial security based on the parameters of the order. The order parameters may be the action (buy or sell), limit price if any, order quantity, leverage or margin, and the trader's prior success rate, among other order characteristics. The process of incorporating new information into prior beliefs that the market maker undergoes with every order is often modeled according to the Bayes rule. Updating beliefs according to the Bayes rule is known as Bayesian learning. Computer algorithms employing Bayesian learning are often referred to as genetic algorithms.

"In Praise of Bayes," an article in the *The Economist* from September 40, 2000, describes Bayesian learning as follows:

*The essence of the Bayesian approach is to provide a mathematical rule explaining how you should change your existing beliefs in the light of new evidence. In other words, it allows scientists to combine new data with their existing knowledge or expertise. The canonical example is to imagine that a precocious newborn observes his first sunset, and wonders whether the sun will rise again or not. He assigns equal prior probabilities to both possible outcomes, and represents this by placing one white and one black marble into a bag. The following day, when the sun rises, the child places another white marble in the bag. The probability that a marble plucked randomly from the bag will be white (i.e., the child's degree of belief in future sunrises) has thus gone from a half to two-thirds. After sunrise the next day, the child adds another white marble, and the probability* *(and thus the degree of belief) goes from two-thirds to three-quarters. And so on. Gradually, the initial belief that the sun is just as likely as not to rise each morning is modified to become a near-certainty that the sun will always rise.*

Mathematically, the Bayes rule can be specified as follows:

Pr(seeing data) = Pr(seeing data | event occurred) Pr(event occurred)

+ Pr(seeing data | no event) Pr(no event) (11.7)

where Pr(event) may refer to the probability of the sun rising again or the probability of security prices rising, while seeing may refer to registering a buy order or actually observing the sunrise. No event may refer to a lack of buy orders or inability to observe a sunrise on a particular day—for example, due to a cloudy sky. The probability of seeing data and registering an event at the same time has the following symmetric property:

$$Pr(seeing data, event) = Pr(event| seeing data) Pr(seeing data)$$
$$= Pr(seeing data|event) Pr(event)$$
(11.8)

Rearranging equation (11.8) to obtain expression for Pr(event|seeing data) and then substituting Pr(seeing data) from equation (1) produces the following result:

Pr(event|seeing data) =

Pr(seeing data|event) Pr(event)

Pr(seeing data|event) Pr(event) + Pr(seeing data|no event) Pr(no event) (11.9)

Equation (11.9) is known as the Bayes rule, and it can be rewritten as follows:

$$\begin{aligned} & \text{Posterior belief} = \text{Pr}( \text{event} | \text{seeing data}) \\ & = \frac{\text{Prior belief} \times \text{Pr}( \text{seeing data} | \text{event})}{\text{Marginal likelihood of the data}} \end{aligned} \tag{11.10}$$

Market makers apply the Bayes rule after each order event, whether they consciously calculate probabilities or unconsciously use their trading experience. For example, suppose that the market maker is in charge of providing liquidity for the Australian dollar, AUD/USD. The current mid-price, *Vmid*, for AUD/USD is 0.6731. Consequently, the market maker's initial belief about the true price for AUD/USD is 0.6731. At what level should the market maker set bid and ask prices?

According to the Bayes rule, the market maker should set the new ask price to the expected *V*ask, given the buy order: *E*[*V*ask|buy order]. Suppose that the market maker cannot distinguish between informed and uninformed traders and assigns a 50 percent probability to the event that a market buy order will arrive from an informed trader and a 50 percent probability to the event that a market buy order will arrive from an uninformed trader. In addition, suppose that any informed trader would place a buy order only if the trader was certain he could make at least 5 pips on each trade in excess of the bid-ask spread and that there are no other transaction costs. If the average bid-ask spread on AUD/USD quoted by the market maker is 2 pips, then an informed trader would place a buy order only if he believes that the true value of AUD/USD is at least 0.6738. From the market maker's perspective, the Bayesian probability of the true value of AUD/USD, *V*ask, being worth 0.6738 after observing a buy order is calculated as follows:

$$\begin{split} \Pr(V_{\text{ask}} = 0.6738 | \text{buy order}) &= \\ \frac{\Pr(V_{\text{ask}} = 0.6738) \Pr(\text{buy order}|V_{\text{ask}} = 0.6738)}{\Pr(V_{\text{ask}} = 0.6731) \Pr(\text{buy order}|V_{\text{ask}} = 0.6731)} \\ + \Pr(V_{\text{ask}} = 0.6738) \Pr(\text{buy order}|V_{\text{ask}} = 0.6738) \end{split} \tag{11.11}$$

If the true value *V*ask is indeed 0.6738, then an informed trader places the buy order with certainty (a probability of 100 percent), while the uninformed trader may place a buy order with a probability of 50 percent (also with a probability of 50 percent, the uninformed trader may place a sell order instead). Thus, if the true price *V*ask = 0.6738,

$$\text{Pr}(\text{buy order}|V_{\text{ask}} = 0.6738) = \text{Pr}(\text{informed trader}) \text{ }^* \text{ } 100 \text{ percent}$$

+ Pr(uninformed trader)<sup>∗</sup>50 percent

(11.12)

Since we previously assumed that the market maker cannot distinguish between informed and uninformed traders and assigns equal probability to either,

$$Pr(\text{informed trader}) = Pr(\text{uninformed trader}) = 50 \text{ percent}$$
 (11.13)

Combining equations (11.12) and (11.13), we obtain the following probability of the buy order being an indication of the buy order resulting from higher true value *V*ask:

$$\text{Pr(buy order}|V_{ask} = 0.6738) = 50 \text{ percent}^* 100 \text{ percent}$$
  
+50 percent\* 50 percent (11.14)  
= 75 percent.

The probability of the buy order resulting from the lower, unchanged, true value *V*ask is then

$$\begin{aligned} &\text{Pr(buy order}|V_{ask}=0.6731)=1-~\text{Pr(buy order}|V_{ask}=0.6738) \\ &= 25\text{ percent.} \end{aligned} \tag{11.15}$$

Assuming that the market maker has no indication where the market is going—in other words, from the market maker's perspective at the given moment,

$$\Pr(V_{\text{ask}} = 0.6738) = \Pr(V_{\text{ask}} = 0.6731) = 50 \text{ percent} \tag{11.16}$$

and substituting equations (11.13), (11.14), (11.15), and (11.16) into equation (11.11), we obtain the following probability of the true value of AUD/USD being at least 0.6738 given that the buy order arrived:

$$\Pr(V_{\text{ask}} = 0.6738 | \text{buy order}) = \frac{50\% \times 75\%}{50\% \times 25\% + 50\% \times 75\%} = 75\%$$

By the same logic, Pr(*V*ask = 0.6731|buy order) = 25%.

Having calculated these probabilities, the market maker is now ready to set market prices. He sets the price equal to the conditional expected value as follows:

New ask price = 
$$E[V|\text{buy order}] = 0.6731 \times \Pr(V_{\text{ask}} = 0.6731)$$
  
+0.6738  $\times \Pr(V_{\text{ask}} = 0.6738)$  (11.17)  
= 0.6731  $\times$  25% + 0.6738  $\times$  75% = 0.6736

Similarly, a new bid price can be calculated as *E*[*V*bid|sellorder] after observing a sell order. The resulting bid and ask values are tradable "regretfree" quotes. When the market maker sells a unit of his inventory known as a clip to the buyer at 0.6736, the market maker is protected against the loss because of the buyer's potentially superior information.

If a buy order at ask of 0.6738 actually arrives, the market maker then recalculates his bid and ask prices as new conditional expected values. The market maker's new posterior probability of a buy coming from an informed trader is 75 percent by the foregoing calculation. Furthermore, an informed buyer would buy at 0.6738 only if the true value of AUD/USD less the ask price exceeded the average spread and the trader's minimum desired gain. Suppose that, as before, the trader expects the minimum desired gain to be 5 pips and the average spread to be 2 pips, making him willing to buy at 0.6738 only if the true value of AUD/USD is at least 0.6745. The market maker will now once again adjust his bid and ask prices conditional on such expectation.

One outcome of Glosten and Milgrom (1985) is that in the presence of a large number of informed traders, a market maker will set unreasonably high spreads in order to break even. As a result, no trades will occur and the market will shut down.

In Glosten and Milgrom (1985) all trades are done on one unit of the financial security. Glosten and Milgrom (1985) do not consider the impact that the trade size has on price. Easley and O'Hara (1987) extend the Glosten and Milgrom model to incorporate varying trade sizes. Easley and O'Hara (1987) further add one more level of complexity—information arrives with probability α. Still, both Glosten and Milgrom (1985) and Easley and O'Hara are models in which informed traders simply submit orders at every trading opportunity until prices adjust to their new full-information value. The traders do not strategically consider the optimal actions of market makers and how market makers may act to reduce traders' profitability.

By contrast, the class of models known as strategic models develop conjectures about pricing policies of the market maker and incorporate those conjectures into their trading actions. One such strategic model by Kyle (1985) analyzes how a single informed trader could best take advantage of his information in order to maximize his profits.

Kyle (1985) describes how information is incorporated into security prices over time. A trader with exclusive information (e.g., a good proprietary quantitative model) hides his orders among those of uninformed traders to avoid provoking the market maker into increasing the spread or otherwise adjusting the price in any adverse manner.

Mende, Menkhoff, and Osler (2006) note that the process of embedding information into foreign exchange prices differs from the process of other asset classes, say equities. Traditional microstructure theory observes four components contributing to the bid-ask spread: adverse selection, inventory risk, operating costs, and occasional monopoly power. Foreign exchange literature often excludes the possibility of monopolistic pricing in the foreign exchange markets due to decentralization of competitive foreign exchange dealers. Some literature suggests that most bid-ask spreads arise as a function of adverse selection; dealers charge the bid-ask spread to neutralize the effects of losing trades in which the counterparties are better informed than the dealer himself. As a result, dealers that can differentiate between informed and uninformed customers charge higher spreads on trades with informed customers and lower spreads on trades with uninformed customers.

Mende, Menkhoff, and Osler (2006) note that in foreign exchange markets the reverse is true: uninformed customers, such as corporate and commercial entities that transact foreign exchange as part of their operations, receive higher bid-ask spreads from dealers than do institutional customers that transact foreign exchange for investment and speculative purposes. Mende, Menkhoff, and Osler (2006) further suggest that the dealers may be simply enjoying higher margins on corporate and commercial entities than on institutional customers due to competitive pressures from the electronic marketplace in the latter markets. Mende, Menkhoff, and Osler (2006) attribute this phenomenon to the relative market power of foreign exchange dealers among corporate and commercial enterprises.

In addition, Mende, Menkhoff, and Osler (2006) suggest that the dealers may strategically subsidize the trades that carry information, as first noted by Leach and Madhavan (1992, 1993) and Naik, Neuberkert, and Viswanathan (1999). For example, the dealers may provide lower spreads on large block orders in an effort to gather information and use it in their own proprietary trades.

Mende, Menkhoff, and Osler (2006), however, emphasize that the majority of price variations in response to customer orders occurs through dealer inventory management. When the dealer transacts with an informed customer, the dealer immediately needs to diversify the risk of ending up on the adverse side of the transaction. For example, if a dealer receives a buy order from an informed customer, there is a high probability that the market price is about to rise; still, the dealer has just sold his inventory to the customer. To diversify his exposure, the dealer places a buy in the interdealer markets. When the dealer receives a buy order from an uninformed customer, on the other hand, the probability that the market price will rise is low, and the dealer has no immediate need to diversify the exposure that results from his trading with the uninformed customer.

#### **Trading on Order Aggressiveness**

Much of the success of microstructure trading is based on the trader's ability to retrieve information from observed market data. The market data can be publicly observed, as is real-time price and volume information. The data can also be private, such as the information about client order flow that can be seen only by the client's broker.

To extract the market information from the publicly available data, Vega (2007) proposes monitoring the aggressiveness of trades. Aggressiveness refers to the percentage of orders that are submitted at market prices, as opposed to limit prices. The higher the percentage of market orders, the more aggressive the trader in his bid to capture the best available price and the more likely the trader is to believe that the price of the security is about to move away from the market price.

The results of Vega (2007) are based on those of Foster and Viswanathan (1996), who evaluate the average response of prices in a situation where different market participants are informed to a different degree. For example, before an expected economic announcement is made, it is common to see "a consensus forecast" that is developed by averaging forecasts of several market analysts. The consensus number is typically accompanied by a range of forecasts that measures the dispersion of forecasts by all analysts under consideration. For example, prior to the announcement of the January 2009 month-to-month change in retail sales in the United States, Bloomberg LP reported the analysts' consensus to be –0.8 percent, while all the analysts' estimates for the number ranged from –2.2 percent to 0.3 percent (the actual number revealed at 8:30 A.M. on February 12, 2009, happened to be +1.0 percent).

Foster and Viswanathan (1996) show that the correlation in the degree of informativeness of various market participants affects the speed with which information is impounded into prices, impacts profits of traders possessing information, and also determines the ability of the market participants to learn from each other. In other words, the narrower the analysts' forecast range, the faster the market arrives at fair market prices of securities following a scheduled news release. The actual announcement information enters prices through active trading. Limit orders result in more favorable execution prices than market orders; the price advantage, however, comes at a cost—the wait and the associated risk of non-execution. Market orders, on the other hand, are executed immediately but can be subject to adverse pricing. Market orders are used in aggressive trading, when prices are moving rapidly and quick execution must be achieved to capture and preserve trading gains. The better the trader's information and the more aggressive his trading, the faster the information enters prices.

As a result, aggressive orders may themselves convey information about the impending direction of the security price move. If a trader executes immediately instead of waiting for a more favorable price, the trader may convey information about his beliefs about where the market is going. Vega (2007) shows that better-informed market participants trade more aggressively. Mimicking aggressive trades, therefore, may result in a consistently profitable trading strategy. Measures of aggressiveness of the order flow may further capture informed traders' information and facilitate generation of short-term profits.

Anand, Chakravarty, and Martell (2005) find that on the NYSE, institutional limit orders perform better than limit orders placed by individuals, orders at or better than market price perform better than limit orders placed inside the bid-ask spread, and larger orders outperform smaller orders. To evaluate the orders, Anand, Chakravarty, and Martell (2005) sampled all orders and the execution details of a 3-month trading audit trail on the NYSE, spanning November 1990 through January 1991.

Anand, Chakravarty, and Martell (2005) use the following regression equation to estimate the impact of various order characteristics on the price changes measured as *Difft*, the difference between the bid-ask midpoints at times *t* and *t* + *n*:

$$\begin{split} \begin{split} \mathit{Diff}_t = \beta_0 + \beta_1 \mathit{Size}_t + \beta_2 \mathit{Aggressiveness}_t + \beta_3 \mathit{Institutional}_t \ + \gamma_1 D_{1t} + \cdots + \gamma_k D_{k-1,t} + \varepsilon_t \end{split} \end{split}$$

where *t* is the time of the order submission, *n* equals 5 and then 60 minutes after order submission. *Size* is the number of shares in the particular order divided by the mean daily volume of shares traded in the particular stock over the sample period. For buy orders, *Aggressiveness* is a dummy that takes the value 1 if the order is placed at or better than the standing quote and zero otherwise. *Institutional* is a dummy variable that takes the value 1 for institutional orders and 0 for individual orders. *D*<sup>1</sup> to *Dk*-1 are stockspecific dummies associated with the particular stock that was traded.

|                              | Intercept | Size   | Aggressiveness | Institutional |
|------------------------------|-----------|--------|----------------|---------------|
| Panel A: 97 stocks           |           |        |                |               |
| 5 min after order placement  | 0.005     | 0.010* | 0.016*         | 0.004*        |
| 60 min after order placement | 0.020**   | 0.020* | 0.012*         | 0.006*        |
| Panel B: 144 stocks          |           |        |                |               |
| 5 min after order placement  | 0.006     | 0.012* | 0.014*         | 0.004*        |
| 60 min after order placement | 0.021**   | 0.023* | 0.012*         | 0.004*        |

**TABLE 11.1** Difference in the Performance of Institutional and Individual Orders

This table, from Anand, Chakravarty, and Martell (2005), summarizes the results of robustness regressions testing for a difference in the performance of institutional and individual orders. The regression equation controls for stock selection by institutional and individual traders. The dependent variable in the regression is the change in the bid-ask midpoint 5 and then 60 minutes after order submission. \*t-test significant at 1 percent.

\*\*t-test significant at 5 percent.

Reprinted from *Journal of Financial Markets*, 8/3 2005, Amber Anand, Sugato Chakravarty, and Terrence Martell, "Empirical Evidence on the Evolution of Liquidity: Choice of Market versus Limit Orders by Informed and Uninformed Traders," page 21, with permission from Elsevier.

According to several researchers, market aggressiveness exhibits autocorrelation that can be used to forecast future realizations of market aggressiveness. The autocorrelation of market aggressiveness is thought to originate from either of the following sources:

- Large institutional orders that are transmitted in smaller slices over an extended period of time at comparable levels of market aggressiveness
- Simple price momentum

Research into detecting autocorrelation of market aggressiveness was performed by Biais, Hillion, and Spatt (1995), who separated orders observed on the Paris Bourse by the degree of aggressiveness—from the least aggressive market orders that move prices to the most aggressive limit orders outside the current book. The authors found that the distribution of orders in terms of aggressiveness depends on the state of the market and that order submissions are autocorrelated. The authors detected a "diagonal effect" whereby initial orders of a certain level of aggressiveness are followed by other orders of the same level of aggressiveness. Subsequent empirical research confirmed the findings for different stock exchanges. See, for example, Griffiths, Smith, Turnbull, and White (2000) for the Toronto Stock Exchange; Ranaldo (2004) for the Swiss Stock Exchange; Cao, Hansch, and Wang (2004) for the Australian Stock Exchange; Ahn, Bae, and Chan (2001) for the Stock Exchange of Hong Kong; and Handa, Schwartz, and Tiwari (2003) for the CAC40 stocks traded on the Paris Bourse.

## **Trading on Order Flow**

**Order Flow Overview** Order flow is the difference between buyerinitiated and seller-initiated trading volume. Order flow has lately been of particular interest to both academics and practitioners studying the flow's informational content. According to Lyons (2001), order flow is informative for three reasons:

- **1.** Order flow can be thought of as market participants exposing their equity to their own forecasts. A decision to send an order can be costly to market participants. Order flow therefore reflects market participants' honest beliefs about the upcoming direction of the market.
- **2.** Order flow data is decentralized with limited distribution; brokers see the order flow of their clients and inter-dealer networks only. Clients seldom see any direct order flow at all, but can partially infer the order flow information from market data provided by their brokers using a

complex and costly mechanism. Because the order flow is not available to everyone, those who possess full order flow information are in a unique position to exploit it before the information is impounded into market prices.

3. Order flow shows large and nontrivial positions that will temporarily move the market regardless of whether the originator of the trades possesses any superior information. Once again, an entity observing the order flow is best positioned to capitalize on the market movements surrounding the transaction.

Lyons (2001) further distinguishes between transparent and opaque order flows, with transparent order flows providing immediate information, and opaque order flows failing to produce useful data or subjective analysis to extract market beliefs. According to Lyons (2001), order flow transparency encompasses the following three dimensions:

- Pre-trade versus post-trade information
- Price versus quantity information
- Public versus dealer information

Brokers observing the customer and inter-dealer flow firsthand have access to the information pre-trade, can observe both the price and the quantity of the trade, and can see both public and dealer information. On the other hand, end customers can generally see only the post-trade price information by the time it becomes public or available to all customers. Undoubtedly, dealers are much better positioned to use the wealth of information embedded in the order flow to obtain superior returns, given the appropriate resources to use the information efficiently.

Order flow information is easy to trade profitably. A disproportionately large number of buy orders will inevitably push the price of the traded security higher; placing a buy order at the time a large buy volume is observed will result in positive gains. Similarly, a large number of sell orders will depress prices, and a timely sell order placed when the sell order flow is observed will generate positive results.

Order Flow Is Directly Observable As noted by Lyons (1995), Perraudin and Vitale (1996), and Evans and Lyons (2002), among others, order flow is a centralized measure of information that was previously dispersed among market participants. Order flow for a particular financial security at any given time is formally measured as the difference between buyer-initiated and seller-initiated trading interest. Order flow is sometimes referred to as buying or selling pressures. When the trade sizes are observable, the order flow can be computed as the difference between the cumulative size of buyer-initiated trades and the cumulative size of sellerinitiated trades. When trade quantities are not directly observable, order flow can be measured as the difference between the number of buyerinitiated trades and seller-initiated trades in each specific time interval.

Both trade-size–based and number-of-trades–based measures of order flow have been used in the empirical literature. The measures are comparable since most orders are transmitted in "clips," or parcels of a standard size, primarily to avoid undue attention and price run-ups that would accompany larger trades. Jones, Kaul, and Lipson (1994) actually found that order flow measured in number of trades predicts prices and volatility better than order flow measured in aggregate size of trades.

The importance of order flow in arriving at a new price level following a news announcement has been verified empirically. Love and Payne (2008), for example, examine the order flow in foreign exchange surrounding macroeconomic news announcements and find that order flow directly accounts for at least half of all the information impounded into market prices.

Love and Payne (2008) studied the impact of order flow on three currency pairs: USD/EUR, GBP/EUR, and USD/GBP. The impact of the order flow on the respective rates found by Love and Payne (2008) is shown in Table 11.2. The authors measure order flow as the difference between the number of buyer-initiated and the number of seller-initiated trades in each 1-minute interval. Love and Payne (2008) document that at the time of news release from Eurozone, each additional buyer-initiated trade in excess of seller-initiated trades causes USD/EUR to increase by 0.00626 or 0.626 percent.

|                                                                    | USD/EUR<br>Return | GBP/EUR<br>Return | USD/GBP<br>Return |
|--------------------------------------------------------------------|-------------------|-------------------|-------------------|
| Flowt<br>at a time coinciding with a news<br>release from Eurozone | 0.00626*          | 0.000544          | 0.00206           |
| Flowt<br>at a time coinciding with a news<br>release from the UK   | 0.000531          | 0.00339***        | 0.00322***        |
| Flowt<br>at a time coinciding with a news<br>release from the U.S. | 0.00701***        | 0.00204           | 0.00342**         |

**TABLE 11.2** Average Changes in 1-Minute Currency Returns Following a Single Trade Increase in the Number of Buyer-Initiated Trades in Excess of Seller-Initiated Trades

\*\*\*, \*\* and \* denote 99.9 percent, 95 percent, and 90 percent statistical significance, respectively.

**Order Flow Is Not Directly Observable** Order flow is not necessarily transparent to all market participants. For example, executing brokers can directly observe buy-and-sell orders coming from their customers, but generally the customers can see only the bid and offer prices, and, possibly, the depth of the market.

As a result, various models have sprung up to extract order flow information from the observable data. Most of these models are based on the following principle: the aggregate number of buy orders dominates the aggregate number of sell orders for a particular security whenever the price of that security rises, and vice versa. Hasbrouck (1991) proposes the following identification of order flow, adjusted for orders placed in previous time periods and conditioned on the time of day:

$$x_{i,t} = \alpha_x + \sum_{k=1}^{K} \beta_k r_{i,t-k} + \sum_{m=1}^{M} \gamma_m x_{t-m} + \sum_{t=1}^{T} \delta D_t + \varepsilon_{i,t}$$
(11.18)

where *xi*,*<sup>t</sup>* is the aggregate order flow for a security *i* at time *t*, equal to +1 for buys and –1 for sells; *ri*,*<sup>t</sup>* is a one-period return on the security *i* from time *t-*1 to time *t*; and *Dt* is the dummy indicator controlling for the time of day into which time *t* falls. Hasbrouck (1991) considers nineteen *Dt* operators corresponding to half-hour periods between 7:30 A.M. and 5:00 P.M. EST.

**Autocorrelation of Order Flows** Like market aggressiveness, order flows exhibit autocorrelation, according to a number of articles including those by Biais, Hillion, and Spatt (1995); Foucault (1999); Parlour (1998); Foucault, Kadan, and Kandel (2005); Goettler, Parlour, and Rajan (2005, 2007); and Rosu (2005).

Ellul, Holden, Jain, and Jennings (2007) interpret short-term autocorrelation in high-frequency order flows as waves of competing order flows responding to current market events within liquidity depletion and replenishment. Ellul, Holden, Jain, and Jennings (2007) confirm strong positive serial correlation in order flow at high frequencies, but find negative order firm correlation at lower frequencies on the New York Stock Exchange. Hollifield, Miller, and Sandas (2004) test the relationship of the limit order fill rate at different profitability conditions on a single Swedish stock. Like Hedvall, Niemeyer, and Rosenqvist (1997) and Ranaldo (2004), Hollifield, Miller, and Sandas (2004) find asymmetries in investor behavior on the two sides of the market of the Finnish Stock Exchange. Foucault, Kadan, and Kandel (2005) and Rosu (2005) make predictions about order flow autocorrelations that support the diagonal autocorrelation effect first documented in Biais, Hillion, and Spatt (1995).

# **CONCLUSION**

Understanding the type and motivation of each market participant can unlock profitable trading strategies. For example, understanding whether a particular market participant possesses information about impending market movement may result in immediate profitability from either engaging the trader if he is uninformed or following his moves if he has superior information.
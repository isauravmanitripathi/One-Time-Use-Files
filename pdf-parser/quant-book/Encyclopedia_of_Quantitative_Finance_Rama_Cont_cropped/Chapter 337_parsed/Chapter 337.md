# **Order Flow**

According to a common definition, "order flow is transaction volume with a sign" [1]. The sign of the volume conveys information on the initiator of the transaction. Conventionally, positive volumes are associated with buyer-initiated transactions, whereas negative volumes are associated with sellerinitiated transactions. Under this definition, order flow is characterized only by orders that result in an immediate transaction. A more general definition of order flow should also include orders that do not result in an immediate transaction. More precisely, most modern financial markets work through a double auction mechanism. In these markets, impatient traders submit *market orders*, which are orders to buy or sell a given quantity of shares at the best available price,a and are therefore immediately executed (*see* **Order Types**). More patient traders submit *limit orders*, which are orders to buy or sell a given amount of shares at a given price or better. If there are no counterparties willing to trade at this price, the order is added to a queue called the *limit order book*. A trader can decide to remove his/her limit order from the book whenever he/she wants and this event is called a *cancellation*. The order flow is the joint process of market and limit order placements and cancellations. The price formation process results from the interaction between these events and is the focus of market microstructure theory [1–3]. Order flow is related to supply and demand and to liquidity. More precisely, when one considers the sign of the orders, "Order flow, as used in microstructure finance, is a variant of a key term in economics excess demand" [1]. Whatever the order sign, the flow of limit orders increases the liquidity of the asset, while market orders and cancellations deplete liquidity.

## **Statistical Properties**

The order flow is a complex stochastic process that takes place in continuous time. It has three components (limit orders, market orders, and cancellations), each component being characterized by a sign, a volume, and a price. The order flow is, furthermore, strongly dependent on the state of the limit order book. There is no available stochastic model able to fully describe the dependence structure of this process. One usually restricts to a subpart of the order flow and attempts to describe it within a suitable reduced model.

In order to simplify the presentation, this article focuses on the statistical modeling of each component separately and refers mainly to stock markets.

### *Market Order Flow*

The unconditional probability of the sign of a market order is very close to 1/2. The probability density function of the volume of market orders is often described by a decreasing function with a power-law tail (see Figure 1). The market order flow has very interesting temporal correlation properties. Consider, for simplicity, the symbolic time series obtained in event time by replacing buy market orders with +1 and sell market orders with −1, irrespective of the volume of the order. The autocorrelation function *C(τ )* of these strings of bits decays very slowly to zero and its asymptotic behavior is well fitted by a power-law function

$$C(\tau) \approx \frac{1}{\tau^{\alpha}} \tag{1}$$

where *α <* 1 (typically *α* ∼= 0*.*5) [4, 5]. A process with such a nonsummable autocorrelation is called a *long-memory process* [6]. Panel (a) of Figure 2 shows the autocorrelation function of market order signs for AstraZeneca (AZN) traded at the London Stock Exchange (LSE). It is worth noting that the persistence in the market order flow is still statistically significant after many trading hours. The volume-weighted market order flow also shows strong temporal persistency, although weakened by the volume fluctuations (see Figure 2b). The longmemory properties of market order signs have been observed in different markets and can also be observed after temporal aggregation of the order flow. It has been proposed that the long memory is due to order splitting [7].

The persistence of market order flow raises the problem of how market efficiency is maintained. A positively correlated order flow and a fixed and permanent market impact imply positively correlated return time series, in contradiction with market efficiency. To reconcile a correlated order flow with efficiency, one has either to assume a fixed but temporary

![](_page_1_Figure_1.jpeg)

Figure 1 Probability density function of the log-volume of individual orders, for the three different components of the order flow. For comparison, the figure also shows the probability density function of decimal logarithm of the volume at the best (ask) price, sampled before each transaction. The inset shows in a double logarithmic scale the cumulative probability distribution of the volume for different types of orders. The dashed line is a power-law function with slope 2.8, which is the maximum likelihood estimator of the tail exponent for market orders. Data refer to the stock AZN traded at the LSE in the period  $1999-2002$ 

impact or a permanent but history-dependent impact [8] (see **Price Impact**).

The conditional properties of market order flow are also important. First, the size of the bid-ask spread is a key determinant of the market order flow. The rate of market orders submission, independently on their sign, decreases as the spread increases (see Figure 3). This behavior is intuitively expected since a large bid-ask spread is a strong disincentive to trade, given that the spread-related cost is large. A second conditional property concerns the volume of a market order, which is strongly dependent on the volume at the opposite best price. Specifically, it is rare that the volume of a market order exceeds the volume at the opposite best and thus that the trade penetrates more than one price level [9]. For example, in a set of 16 highly capitalized stocks traded at the LSE, approximately 86% of the market orders leading to an immediate price change have a volume exactly equal to the volume at the opposite best. Moreover, approximately 97% of the market orders leading to an immediate price change have a volume that is less than the total volume at the best and at the second-best opposite price. This indicates strong selective liquidity taking, meaning that agents condition the size of their market orders on

prevailing liquidity, making large transactions only when liquidity is high and small transactions when it is low.

## Limit Order Flow

A limit order is characterized by its sign, volume, and limit price. Several statistical regularities of limit orders placement have also been observed. First, the unconditional distribution of limit order volume is similar to the one for market orders (see Figure 1). Second, the time series of limit order signs is also characterized by the long-memory property [5, 10]. Figure  $2(c)$  shows the autocorrelation function of limit order signs for AZN. Third, several statistical regularities of limit order flow are observed when one also considers the limit price. The limit price characterizes the aggressiveness of the limit order and the patience of the trader since the probability that the order is executed in a given time interval depends on where it is placed. Limit orders in the spread are very aggressive and more likely to be executed, while limit orders placed in the book very far from the best price are less aggressive and their execution probability is low. For high cap stocks at LSE between 1999 and 2002, roughly one-third of

![](_page_2_Figure_1.jpeg)

Figure 2 Autocorrelation of the order flow in event time plotted on a double logarithmic scale. Specifically, the panels show the autocorrelation function of market order sign (a), market order signed volume (b), limit order sign (c), and cancellation sign (d). The span of the x-axis corresponds on average to two trading days. The data refer to the stock AZN traded at the LSE in the period  $1999-2002$ 

limit orders were placed inside the spread, another third at the best prices, and the last third inside the book. One of the statistical regularities recently observed is the power-law distribution of limit order price in continuous double-auction financial markets. Let  $b(t) - \Delta$  denote the price of a new buy limit order and  $a(t) + \Delta$  the price of a new sell limit order. Here  $a(t)$  is the best ask price and  $b(t)$  is the best bid price when the limit order is placed. The probability density function  $\rho(\Delta)$  of the relative price  $\Delta$  is very similar for buy and sell orders. Moreover, for large values of  $\Delta$ , the probability density function is well fitted by a power-law function

$$\rho(\Delta) \approx \frac{1}{\Delta^{1+\mu}} \tag{2}$$

where  $\mu \approx 1.5$  for LSE stocks [11], and  $\mu \approx 0.6$ for stocks traded at the Paris Stock Exchange [12]. This power law extends from 1 tick to over 100 ticks (sometimes even 1000 ticks), corresponding to a relative change of price of 5 to 50%. Such a broad distribution of limit order prices tells us that the

opinion of market participants about the price of the stock in a near future could be anything from its present value to 50% above or below this value. Mike and Farmer [13] fit the distribution of relative limit prices  $\Delta$  for LSE stocks with a Student distribution with 1.3 degrees of freedom corresponding to a value  $\mu = 1.3$ . Interestingly, the Student distribution fits relative limit order price both outside ( $\Delta > 0$ ) and inside ( $\Delta < 0$ ) the spread.

The rate of limit order placement strongly depends on spread. When the spread is large, the rate of limit order placement is also large (see Figure 3). This is true also if one considers only limit orders placed inside the spread (see Figure 3). The reason is that a large spread is an incentive to provide liquidity and to acquire price priority by placing a limit order in the spread. The limit order flow is also dependent on book thickness. Patient traders become more aggressive in their limit order submission when the own side book is thicker and when the opposite side book is thinner  $[14]$ .

![](_page_3_Figure_1.jpeg)

**Figure 3** Rates of different types of events in the limit order book conditional to the size of the spread. The data refer to the stock AZN traded at the LSE in 2002 [Adapted from [20].]

#### *Cancellation Flow*

A limit order can be canceled or can expire and both events lead to a depletion of liquidity. Not surprisingly, the volume of canceled limit orders is distributed in a similar way to the volume of limit orders (see Figure 1). The time series of cancellation signs also displays the longmemory property (see Figure 2d). Moreover, the rate of cancellations increases with spread size (see Figure 3). This is probably due to the high limit order placement/cancellation activity observed when a temporary liquidity crisis triggers a competition between liquidity providers in order to find a new equilibrium value for the bid and ask prices. Finally, the lifetime of a given limit order (which is inversely related to the cancellation probability) increases as one moves away from the bid–ask spread [15]. This phenomenon can be explained by considering that far away orders are typically put in the market by patient investors that want to benefit from significant price swings in the medium term, while orders close to the bid and ask prices correspond to very active market participants that readjust their orders at a very high frequency. The cancellation probability at time *t* depends also on the ratio between the distance of the limit price from the best at time *t* and at the time *t*<sup>0</sup> *< t* when the order was placed. Mike and Farmer fit the cancellation probability with the functional form

$$p(t) \propto 1 - \exp[-\Delta(t)/\Delta(t_0)] \tag{3}$$

meaning that if the price moves in a direction opposite to the limit order, its cancellation probability increases [13].

#### *Diagonal Effect*

As discussed above, a common phenomenon observed in the statistics of order flow is a strong serial correlation of each component of the order flow. This phenomenon has been termed *diagonal effect* [16]. More precisely, the probability that a given type of event occurs is larger after that event has just occurred than it would be for the unconditional occurrence of the event [16]. This type of serial persistence is observed also for longer lags and it has been observed in different markets including foreign exchange markets [17]. The possible origins of these serial correlations are (i) strategic order splitting in order to reduce market impact; (ii) imitation behavior across traders that observe other participants and imitate their behavior; and (iii) traders reacting similarly to the same event. It is, in general, difficult to separate these alternative explanations. However, by using brokerage data, it has been shown that correlation in market order flow is mainly explained by order splitting [8]. Positive serial correlation of limit order flow is also due largely to order splitting and the undercutting behavior among limit order traders. Controlling for these two effects explains up to 72% of the positive serial correlation [10].

*Commonality in Order Flow and Liquidity Provision*

The above discussion has focused on the statistical properties of the order flow for an individual stock. However, the order flow of different stocks simultaneously traded in the same market can display mutual dependencies. Since the order flow determines the supply and demand of liquidity of a stock, this type of dependency is also called *commonality in liquidity*. When order flow is signed according to the buy/sell side, direct and indirect measures indicate that commonality in the order flows explains a consistent part (two-thirds as described in [18]) of the commonality in returns [18, 19]. By considering order flow with orders signed according to the liquidity supply or demand, empirical analysis shows that there are significant commonalities in liquidity and that a liquidity market factor exists [18, 19].

## **End Notes**

a*.* In some markets only limit orders are allowed and a limit order crossing the spread results in an immediate transaction. Thus a crossing limit order behaves as an effective market order.

## **References**

- [1] Lyons, R.K. (2001). *The Microstructure Approach to Exchange Rates*, The MIT Press.
- [2] O'Hara, M. (1995). *Market Microstructure Theory*, Blackwell Publishing.
- [3] Hasbrouck, J. (2007). *Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading*, Oxford University Press.
- [4] Bouchaud, J.P., Gefen, Y., Potters, M. & Wyart, M. (2004). Fluctuations and response in financial markets: the subtle nature of "random" price changes, *Quantitative Finance* **4**, 176–190.
- [5] Lillo, F. & Farmer, J.D. (2004). The long memory of the efficient market, *Studies in Nonlinear Dynamics and Econometrics* **8**, 1.
- [6] Beran, J. (1994). *Statistics for Long-Memory Processes*, Chapman & Hall.
- [7] Lillo, F., Mike, S. & Farmer, J.D. (2005). Theory for long memory in supply and demand, *Physical Review E* **71**, 066122.

- [8] Bouchaud, J.P., Farmer, J.D. & Lillo, F. (2009). How markets slowly digest changes in supply and demand, in *Handbook of Finance: Dynamics and Evolution of Financial Markets*, K. Schenke-Hoppe & T. Hens, eds, North-Holland. Available at SSRN: http://ssrn.com/abstract=1266681.
- [9] Farmer, J.D., Gillemot, L., Lillo, F., Mike, S. & Sen, A. (2004). What really causes large price changes? *Quantitative Finance* **4**, 383–397.
- [10] Yeo, Y. (2006). *Persistence in Limit Order Flow.* Available at SSRN: http://ssrn.com/abstract=923022.
- [11] Zovko, I. & Farmer, J.D. (2002). The power of patience; a behavioral regularity in limit order placement, *Quantitative Finance* **2**, 387–392.
- [12] Bouchaud, J.P., Mezard, M. & Potters, M. (2002). ´ Statistical properties of the stock order books: empirical results and models, *Quantitative Finance* **2**, 251–256.
- [13] Mike, S. & Farmer, J.D. (2008). An empirical behavioral model of liquidity and volatility, *Journal of Economic Dynamics and Control* **32**, 200–234.
- [14] Ranaldo, A. (2004). Order aggressiveness in limit order book markets, *Journal of Financial Markets* **7**, 53–74.
- [15] Potters, M. & Bouchaud, J.P. (2003). More statistical properties of order books and price impact, *Physica A* **324**, 133–140.
- [16] Biais, B., Hillion, P. & Spatt, C. (1995). An empirical analysis of the limit order book and the order flow in the Paris Bourse, *Journal of Finance* **50**, 1665–1690.
- [17] Danielsson, J. & Payne, R.G. (2001). Measuring and explaining liquidity on an electronic limit order book: evidence from Reuters D2000-2), *EFA 2001 Barcelona Meetings*. Barcelona. Available at SSRN: http://ssrn.com/abstract=276541.
- [18] Hasbrouck, J. & Seppi, D.J. (2001). Common factors in prices, order flows, and liquidity, *Journal of Financial Economics* **59**, 383–411.
- [19] Domowitz, I., Hansch, O. & Wang, X. (2005). Liquidity commonality and return co-movement, *Journal of Financial Markets* **8**, 351–376.
- [20] Ponzi, A., Lillo, F. & Mantegna, R.N. (2009). Market reaction to a bid-ask spread change: a power-law relaxation dynamics, *Physical Review E* **80**, 016112.

## **Related Articles**

**Algorithmic Trading**; **Bid–Ask Spreads**; **Highfrequency Data**; **Inventory Effects**; **Limit Order Markets**; **Liquidity**; **Market Microstructure Effects**; **Order Types**; **Price Impact**.

FABRIZIO LILLO
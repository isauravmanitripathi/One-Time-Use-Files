# **Glosten–Milgrom Models**

Glosten–Milgrom models analyze transaction prices arising from quotes of competing risk-neutral dealers making a market in a single security and facing both privately informed and uninformed traders. The dealers must quote bid and offer prices at which they are willing to, respectively, buy and sell. A trader arrives and decides to buy, sell, or leave. Upon seeing the outcome of the trader's decision, the dealers modify their quotes in preparation for the next arrival. Implementation of the model thus requires a specification of the arrival processes of informed and uninformed traders and the nature of public and private information. This specification, in turn, leads to the calculation of quotes and the time series of quotes and transaction prices.

## **Mathematical Structure and Results**

The discussion follows the analysis in [7], and proofs can be found there. The model is designed to describe trade over a relatively small interval of time in which there is private information about the future cash flows of the security, but this private information will depreciate, either through information revealed in trade or *via* public announcements of the information. By the time all asymmetric information has been resolved, at *T* , the value of a share of the security will be *V* . Prior to *T* , this value is not known, but at time *t*, there has been a history of trade and public announcements. This information is summarized by the filtration *Ht* . Justified by the fact that a relatively short period of time is being analyzed, the time value of money and risk aversion can be reasonably ignored, and the value of a share of stock at time *t* is just its expected value conditional on time *t* information, *E*[*V* |*Ht*].

During the trading period, potential traders arrive at the market one by one. An arriving trader at time *t* observes the bid and ask quotes *Bt* and *At* , respectively. If the trader is informed, with information represented by *Ft* , a refinement of the history *Ht* , then the trader is presumed to buy if *E*[*V* |*Ft*] exceeds the ask and sell, if this expectation is below the bid. Otherwise, the trader does not trade. A trader who is uninformed is presumed to have a value *Mt* , which could be a function of the history *Ht*

as well as other features of the trader's preferences. This private valuation should be thought of as a random variable independent of private information. The uninformed trader will buy if *Mt* exceeds the ask price, and sell if this idiosyncratic valuation is below the bid. Describing the arrival process by an indicator variable *It* , which is one if an arrival at time *t* is informed and zero if uninformed, we can describe the personal valuation of an arrival at time *t* by *Zt* = *ItE*[*V* |*Ft*] + *(*1 − *It)Mt* .

Consider the quoting problem of a market maker at time *t* facing a possible arrival. Should the arrival buy, the market maker will receive the ask price and give up a share of stock ultimately worth *V* . This will happen if *Zt* exceeds the ask price. Similarly, if the arrival sells at the bid, the market maker will receive a share ultimately worth *V* and pay the bid price. Otherwise, there will be no transaction and no profit. Thus, the expected profit to a market maker quoting bid *B* and ask *A*, is

$$E[(A-V)\mathbf{1}\{Z_t > A\} + (V-B)\mathbf{1}\{Z_t < B\}|H_t]$$
(1)

Assuming that dealer competition drives the expected profit for both a buy and a sell to zero, the ask and bid quotes are the solutions, if they exist, to the two fixed-point problems:

$$A_t = E[V|H_t, Z_t > A_t] \quad \text{and}$$
  
$$B_t = E[V|H_t, Z_t < B_t] \tag{2}$$

If solutions do not exist, the market is said to close down.

The zero-profit bid and ask prices are "no regret" prices in the sense that the market maker, after having sold to an order at the ask price will revise expectations and the revised expectation is precisely the ask price. That is, to quote the ask price the dealer must determine what the revised expectations will be in the event of a purchase.

The first result is immediate and intuitive: the ask price exceeds the expectation at the time of the quote that exceeds the bid. If a buy occurs, one possibility is that the arriving trader is informed and has a valuation higher than the ask price. It could never be the case that the arriving trader is informed and has a valuation less than the ask price and buys. This alone requires that the market increase the conditional expected value in response to a buy. This argument justifies the term *adverse selection spread* as a description of the difference between the ask price and bid in the model (*see* **Adverse Selection**).

The second observation follows from the fact that transaction prices occur at the "no regret" quotes. The transaction price is a conditional expectation of the terminal value, *V* . A transaction at time *t* can be written, where *Ht*<sup>+</sup> indicates the information available following a transaction at time *t*:

$$P_{t} = A_{t} \mathbf{1}_{\{Z_{t} > A_{t}\}} + B_{t} \mathbf{1}_{\{Z_{t} < B_{t}\}}$$
$$= E[V|H_{t}, Z_{t} > A_{t}] \mathbf{1}_{\{Z_{t} > A_{t}\}}$$
$$+ E[V|H_{t}, Z_{t} < B_{t}] \mathbf{1}_{\{Z_{t} < B_{t}\}}$$
$$= E[V|H_{t+}] \qquad (3)$$

Thus, transaction prices form a martingale. From this observation, flow a number of immediate conclusions. Since reasonably behaved martingales such as this one converge, the absolute differences between transaction prices must get small. As long as trade continues, it must be the case that the spread gets small and that the informational difference between the informed traders and the market gets small.

A number of comparative statics results are readily obtained. At a point in time, an increase in the probability of informed arrival or an increase in the precision of private information increases the spread. As the elasticity of uninformed demand and supply increases, the spread increases as well. It is important to note, however, that these results hold only at a point in time—when the probability of informed trade increases, the rate at which trade reveals private information increases reducing spreads in the future.

The uninformed valuation plays a crucial role in the model. If the uninformed valuation varies little from the mean, then it is quite possible that the only bid and ask prices satisfying the condition are, respectively, the lowest and highest possible realizations of *V* . In this case, there is no trade and the market shuts down. On the other hand, if there is significant variation, so that the uninformed demand and supply are inelastic, then interior solutions for the quotes are guaranteed.

## **Canonical Example**

The most common implementation of a Glosten– Milgrom model assumes that uninformed demand and supply are perfectly inelastic and equally likely, the terminal value *V* has a two-point distribution and informed traders know what value of *V* will be realized. Without losing much generality, the two possible values of *V* can be taken to be zero and one. Define *α* to be the probability that an informed trader arrives in any time period. If *p* is the probability, conditional on past history, that the realization of *V* is one, then the conditional probability of a buy is *αp* + 0*.*5*(*1 − *α)* and the conditional probability of a sell is *α(*1 − *p)* + 0*.*5*(*1 − *α)*. The ask and bid prices are thus

$$A = P\{V = 1 | \text{buy}\} = P\{\text{buy}|V = 1\}p/P\{\text{buy}\}\$$
$$= \frac{(\alpha + 0.5(1 - \alpha))p}{\alpha p + 0.5(1 - \alpha)}$$
$$B = P\{V = 1 | \text{sell}\} = \frac{0.5(1 - \alpha)p}{\alpha(1 - p) + 0.5(1 - \alpha)} \tag{4}$$

The spread is thus *αp(*1 − *p)/(P*{buy}*P*{sell}*)*. Ignoring the denominator, which is approximately 0.25, the spread is increasing in the unresolved variance of *V , p(*1 − *p)*, and the probability of informed trade, *α*.

This model has particularly tractable transaction price dynamics. Recalling that transaction prices are updated expectations, it is readily seen that, denoting by *p*<sup>+</sup> the updated probability, and letting *Q* be a trade direction indicator (+1 for buy at ask and −1 for sell at bid), the following holds:

$$\frac{p^{+}}{1-p^{+}} = \left(\frac{p}{1-p}\right) \left(\frac{1+\alpha}{1-\alpha}\right)^{Q} \tag{5}$$

Assuming that, initially, it is equally likely that *V* be high or low, and denoting by *pt* the revised probability that *V* is one, after t transactions, it is immediate that

$$\ln\left(\frac{p_t}{1-p_t}\right) = \ln\left(\frac{1+\alpha}{1-\alpha}\right)\{Q_1 + \dots + Q_t\} \quad (6)$$

Conditional on *V* , the log odds ratio is proportional to a random walk with expected increment *α(*2*V* − 1*)*. The larger the probability of informed trade is, the faster the log odds ratio increases in the case *V* = 1 and decreases in the case *V* = 0. The larger *α* is, the larger is the initial spread, but the faster the information gets impounded in prices and the faster the spread will fall.

In this model, expectations will not converge to one or zero in finite time. However, the convergence to almost one or zero can be quite fast. Let *TN* be the first time that the log odds ratio hits *N* in the case *V* = 1 and −*N* in the case *V* = 0, starting from *p*<sup>0</sup> = 0*.*5. Straightforward calculations show that the expectation of this stopping time is *N/*[*α* ln*((*1 + *α)/(*1 − *α))*]. For example, if the threshold odds ratio is 0.99/0.01, then *N* is less than 5. Setting *N* = 5, and letting *α* be 0.2, the expected first passage time is roughly 62 trades. The spread at these threshold odds and with *α* equal to 0.2 is 0.008. Setting *α* to 0.1 increases the expected number of trades to 250. The spread at these threshold odds and *α* = 0*.*1 is 0.004. Thus, a stock with even moderate trading will reveal private information relatively rapidly, and the spread will decline quickly.

Relating the expected first passage time and the spread at the first passage time indicates an interesting trade-off. As the percentage of informed trading goes up, the initial spread increases, yet the speed with which the spread declines goes up as well. For *α* = 0*.*2, the spread starts out at 0.2, but declines rapidly, becoming near zero with fewer than 100 expected transactions. In contrast, when *α* = 0*.*05, the initial spread is 0.05, yet it takes an expected 300 trades to become minimal.

This raises intriguing questions about the welfare effects of informed trading; but these are not issues that this example of a Glosten–Milgrom model can handle. Since the uninformed trade, no matter what the spread, informed profit is merely uninformed loss and the total welfare is unaffected by how much informed trade there is. The spread is often related to a welfare measure, but this requires a questionable value judgment—informed are not entitled to their profits. To measure the welfare loss associated with informed trade, a model must incorporate elastic trade on the part of the uninformed.

## **Example with Elastic Uninformed Trade**

The literature does not offer an analysis of transaction price dynamics with elastic uninformed trade. The following is a tractable model. As in the model above, the informed arrive with probability *α*, and know the terminal value. An uninformed trader arrives with private valuation, *M*, and buys if *M* exceeds the ask, sells if *M* is below the bid, and leaves otherwise. Market makers do not know the private valuation, but know that if the current estimate of the security's value is *p*, then an uninformed trader's valuation has the following distribution:

$$P\{M < t\} = \frac{t(1-p)}{t(1-p) + p(1-t)};$$
  
0 < 1 (7)

In this case, the probability of a buy, when the current valuation is *p* and the offer is *A* is *αp* + *(*1 − *α) P*{*M>A*}. The probability of a buy given that *V* is one is *α* + *(*1 − *α)P*{*M>A*} where *P*{*M>A*} = *p(*1 − *A)/*[*A(*1 − *p)* + *p(*1 − *A)*] from equation (7). The ask, *A*, is the solution to

$$A = \frac{p(\alpha + (1 - \alpha)P\{M > A\})}{\alpha p + (1 - \alpha)P\{M > A\}}\tag{8}$$

*A* = 1 is one solution, but this will lead to no trade. Another solution is *A* = *p/(*1 − 2*α(*1 − *p))*, as long as this is less than one and greater than zero, which is true if and only if *α <* 0*.*5. Similarly, on the bid side, *B* = *p(*1 − 2*α)/(*1 − 2*αp)* is the solution as long as *α <* 0*.*5. If *α* exceeds 0.5, the market does not open since *A* = 1 and *B* = 0 are the only feasible solutions.

Because of assuming elastic uninformed trade, the initial spread is larger by the factor 1*/(*1 − *α)*. As the dealer increases the spread, he or she loses less to the informed, per trade, but as uninformed with less-extreme valuations drop out, the probability of transacting with an informed trader increases. This requires a greater widening of the spread.

In this model, not every arrival leads to a trade. The probability that an uninformed trader arrives and decides not to trade is *α*, precisely the probability of an informed trade. This model also has convenient dynamics. Conditional on *V* , the log odds ratio is −ln*(*1 − 2*α)* times a random walk with drift *(*2*V* − 1*)α*.

## **Assumptions and Extensions**

One feature of the model leads to its immediate refutation—trades are for a single quantity. Several papers have extended the basic analysis to multiple trade sizes. Two possible trade sizes is considered by Easley and O'Hara [3], while Glosten [5] considers a continuum of trade sizes. Glosten [6] analyzes continuous trade sizes in an electronic limit order book (*see* **Limit Order Markets**). Interestingly, there is evidence in [8] that the number of trades, as opposed to quantity is what contributes to volatility. Furthermore, [1] shows that a Kyle model ([9]; also *see* **Kyle Model**) with a continuum of allowable trades can, under some conditions, be thought of as a temporal aggregation of a dynamic Glosten–Milgrom model with a strategic informed trader.

One unreasonable assumption of the model is that the bid and offer are determined by a zero-profit assumption. The assumption implies that there is no compensation for the time and effort market making requires. The reason for the assumption is that the analysis can then focus on only the informational source of the spread. It is easy to extend the model to include compensation for market-maker opportunity (and other) cost by specifying that the bid, for example, satisfy *B* = *E*[*V* |*Z<B*] − *c*, where *c* is the economic cost that needs to be covered. With this more realistic specification, it is now apparent that the spread consists of two components—the cost component and the adverse selection component.

When there is no cost component, the martingale property of transaction prices implies that there will be no serial correlation in price changes. When there is only a cost component, however, it is easy to see that transaction prices will bounce back and forth between bid and ask, inducing negative serial correlation in price changes. That the different spread components lead to different transaction price dynamics informs empirical investigations of the spread (*see* **Adverse Selection**).

A strong assumption of the model is that the existence of informed traders is common knowledge. This is relaxed, first in [4] and then in a series of papers by Easley, O'Hara, and coauthors, in which the *probability of informed trade* (PIN) is theoretically derived and empirically investigated (*see* **Probability of Informed Trading**).

While the model is described in terms of competing market makers, it is somewhat more general than that. In particular, the model is not necessarily inconsistent with modeling trade on the New York Stock Exchange, or even an electronic limit order book. In the first case, the competing providers of liquidity are the specialist, floor brokers, and limit order submitters. In the second, limit order submitters compete to provide the quote. Significantly, however, the model does not consider the trader choice between using a market or limit order, an important feature of trading on the NYSE and electronic limit order book markets (*see* **Adverse Selection**; **Limit Order Markets**).

Two survey papers on market microstructure, [10] and [2], are recommended. The first is stronger on a survey of empirical analyses, while the second is stronger on modeling issues.

## **References**

- [1] Back, K. & Baruch, S. (2004). Information in securities markets: Kyle meets Glosten and Milgrom, *Econometrica* **72**, 433–465.
- [2] Biais, B., Glosten, L.R. & Spatt, C. (2005). Market microstructure: a survey of microfoundations, empirical results, and policy implications, *Journal of Financial Markets* **8**, 217–264.
- [3] Easley, D. & O'Hara, M. (1987). Price, trade size, and information in securities markets, *Journal of Financial Economics* **19**, 69–90.
- [4] Easley, D. & O'Hara, M. (1992). Time and the process of security price adjustment, *Journal of Finance* **47**, 576–605.
- [5] Glosten, L.R. (1989). Insider Trading, liquidity, and the role of the monopolist specialist, *Journal of Business* **62**, 211–236.
- [6] Glosten, L.R. (1994). Is the electronic open limit order book inevitable? *Journal of Finance* **49**, 1127–1161.
- [7] Glosten, L.R. & Milgrom, P.R. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders, *Journal of Financial Economics* **14**, 71–100.
- [8] Jones, C., Kaul, G. & Lipson, M.L. (1994). Transactions, volume, and volatility, *Review of Financial Studies* **7**, 631–651.
- [9] Kyle, A.S. (1985). Continuous auctions and insider trading, *Econometrica* **53**, 1315–1335.
- [10] Madhavan, A. (2000). Market microstructure, *Journal of Financial Markets* **3**, 205–258.

## **Related Articles**

**Adverse Selection**; **Kyle Model**; **Limit Order Markets**; **Probability of Informed Trading**.

LAWRENCE R. GLOSTEN
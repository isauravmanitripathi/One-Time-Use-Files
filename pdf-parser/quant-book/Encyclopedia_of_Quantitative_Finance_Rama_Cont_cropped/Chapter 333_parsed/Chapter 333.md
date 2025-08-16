# **Price Impact**

*Price impact* refers to the correlation between an incoming order (to buy or to sell) and the subsequent price change. That a buy trade should push the price up seems at first sight obvious and is easily demonstrated empirically, as we will review below. It is also a dour reality for traders for whom price impact is tantamount to a cost: their second buy trade is on average more expensive than the first because of their own impact (and *vice versa* for sells). Monitoring and controlling impact is therefore one of the most active and rapidly expanding domains of research within trading firms. The most important questions are related to the volume dependence of impact (do larger trades impact prices more?), and the temporal behavior of impact (is the impact of a trade immediate and permanent, or is there some lag dependence of the impact?).

A moment of reflection suggests that the interpretation of price impact is far from trivial, and may even lead to contradictions–isn't a transaction a fair deal between a buyer and a seller? So why is there price impact? Three distinct possibilities come to mind:

- 1. *Agents successfully forecast short term price movements and trade accordingly.* This can result in measurable correlation between trades and price changes, even if the trades by themselves have absolutely no effect on prices at all. If an agent correctly forecasts price movements and if the price is about to rise, the agent is likely to buy in anticipation of it. But in this framework "noise induced" trades, based on no information at all, should have no price impact.
- 2. *The impact of trades reveal some private information.* The arrival of new private information causes trades, which cause other agents to update their valuations, leading to a price change. But if trades are anonymous and there is no easy way to distinguish informed traders from noninformed traders, then all trades will impact the price since other agents will believe that a fraction of these trades might contain some private information.
- 3. *Impact is a statistical effect due to order flow fluctuations.* Imagine, for example, a completely random order flow process that leads to a certain order book dynamics (see, e.g., [7] for a description of such models). Conditional to an extra buy

order, the price will on average move up if everything else is kept constant. Fluctuations in supply and demand can thus be completely random, unrelated to information, and still a well-defined notion of price impact will emerge. In this case, impact is a completely mechanical–or better, statistical–phenomenon.

All three of these mechanisms result in some "price impact", that is, a positive correlation of trading volume and price movement, but they are conceptually very different. In the first two pictures, as emphasized in [13], "orders do not *impact* prices. It is more accurate to say that orders *forecast* prices." In the second picture, price impact is of paramount importance to understand how information gets incorporated into prices. If some traders really have an information on the "true" price at some time in the future, then the observation of an excess of buy trades allows the market to guess that the price will move up and to change the quotes accordingly (*see* **Glosten–Milgrom Models**; **Kyle Model**; for explicit implementations). Thus, while on one hand market impact is a friction, it should also be viewed as the mechanism that allows prices to adjust to new information.

But if the third, mechanical, interpretation is correct, correlation between price changes and order flow is a tautology. If prices move only because of trades, "information revelation" may merely be a self-fulfilling prophecy that would occur even if the fraction of informed traders is zero. Possible differences between these pictures may come about in the volume dependence and temporal behavior of impact, which we discuss below.

# **Linear and Permanent Impact: The Kyle Model**

The simplest assumption is that impact is both linear in the traded volume and permanent in time. These assumptions can be partly justified within the Kyle model [17], where an insider trader and noise traders submit orders that are cleared by a market maker (MM) every time step *t*. In this model, the price adjustment rule *p* of the MM must be linear in the total signed volume *v*, that is,a

$$\Delta p = \lambda \epsilon v \tag{1}$$

where *λ* is a measure of impact, and is inversely proportional to the liquidity of the market. This price adjustment is furthermore *permanent*, that is, the price change between time  $t = 0$  and  $t = T = N\Delta t$  is

$$p_T = p_0 + \sum_{n=0}^{N-1} \Delta p_n = p_0 + \lambda \sum_{n=0}^{N-1} \epsilon_n v_n \qquad (2)$$

This formula assumes that the impact  $\lambda \epsilon_n v_n$  of trades in the  $n$ th time interval persists unabated up to time  $T.$  Huberman and Stanzl [15] and Farmer [6] show that the linear price adjustment of the Kyle model is the only specification that does not allow price manipulations, *provided impact is permanent* (see below). From the above equation, it is clear that the sign of the trades must be serially uncorrelated if the price is to follow an unpredictable random walk. Within the setting of the Kyle model, the trading schedule of the insider is precisely such that the  $\epsilon_n$  are uncorrelated [17]. But data from real markets reveal correlations of the sign of the traded volume over long timescales; we will come back to this important point below.

#### **Measures of Price Impact**

An interesting measure of price impact is the correlation between the price change between 0 and  $T$  and the sign of the trade at time 0, defined, in general, as

$$R(T) = E\left[ (p_T - p_0) \cdot \epsilon_0 \right] - E\left[ (p_T - p_0) \right] E\left[ \epsilon_0 \right]$$
(3)

In the following, we will assume that drifts can be neglected so that only the first term in the right-hand side (RHS) is not zero. This is often the case, in practice, if  $T$  is chosen to be sufficiently small and/or if there is no strong buy/sell asymmetry  $(E[\epsilon_0] = 0)$ .

Within the Kyle framework where the  $\epsilon$ 's are uncorrelated,  $R(T)$  is easily computed and is found to be

$$R(T) = \lambda \ E[v] \tag{4}$$

The impact function  $R(T)$  is therefore lag independent in this model. One can, of course, also define a volume-dependent impact function by conditioning the above average on the incoming volume, that is,

$$R(T, v) = E\left[ (p_T - p_0) \cdot \epsilon_0 | v_0 = v \right] \tag{5}$$

which, in the Kyle model, is equal to  $\lambda v$ , for all T. Note that both  $R(T)$  and  $R(T, v)$  a priori depend on the choice of the elementary timescale  $\Delta t$ , but we want to avoid heavy notations and skip this extra variable dependence.

Another commonly used measure of impact is the correlation  $\rho(T)$  between the price change from 0 to  $T$  and the total signed volume in the same interval, or, more precisely,

$$\rho(T) = \frac{E\left[\left(p_T - p_0\right) \cdot \sum_{n=0}^{N-1} \epsilon_n v_n\right]}{\sqrt{E\left[\left(p_T - p_0\right)\right]^2 E\left[\left(\sum_{n=0}^{N-1} \epsilon_n v_n\right)^2\right]}} \quad (6)$$

In the Kyle model, this correlation is trivially equal to unity, but this correlation can decrease if liquidity fluctuates ( $\lambda$  becomes time dependent), or if other sources of volatility are taken into account. For example, the MM can revise his quotes in the absence of any trades, say, because of some incoming news. This can be modeled by adding an extra term in  $\text{equation (2) above.}$ 

$$p_T = p_0 + \lambda \sum_{n=0}^{N-1} \epsilon_n v_n + \sum_{n=0}^{N-1} \eta_n \tag{7}$$

where the  $\eta_n$ 's are uncorrelated increments, representing causes of price variations not directly related to trading.

It is often useful to generalize the above definition of  $\rho(T)$  by replacing the volumes  $v_n$  by  $v_n^{\psi}$ , where  $\psi$  is a certain exponent. As discussed below, the measured correlations are found to be stronger when  $\psi < 1.$ 

### **Empirical Facts**

Here we summarize briefly the salient empirical facts that emerged in the last 20 years, concerning the volume dependence and the temporal behavior of impact (see [3] for a recent review). Note that to characterize impact empirically, one has to specify two timescales: (i) the "elementary" timescale  $\Delta t$ over which trades are aggregated; (ii) the timescale  $T$ over which the impact of the initial trade is measured.

#### Concave Volume Dependence

The Kyle model assumes linear dependence of impact on the traded volume. One can measure

the volume-dependent instantaneous impact function  $R(T = \Delta t, v)$  for different elementary timescales  $\Delta t$ , ranging from the average transaction time to several hours or days. One typically finds that the volume dependence of this impact is *sublinear* and well described by a power-law:

$$R(T = \Delta t, v) \propto v^{\psi(\Delta t)}; \qquad \psi(\Delta t) \le 1 \quad (8)$$

The exponent  $\psi$  increases with the elementary timescale, taking rather small values  $\psi \simeq 0.1 \rightarrow 0.3$ for individual trades, and increasing toward  $\psi = 1$ when  $\Delta t$  corresponds to several thousands of trades, with some concavity remaining for large volumes [14, 20]. The correlation coefficient  $\rho(T = \Delta t)$  similarly increases as  $\Delta t$  increases, and reaches rather large values  $> 0.5$  for daily returns of individual stocks, futures, or currencies [5].

Note that the small value of  $\psi$  at the individual trade level means that impact is only weakly dependent on volume, in line with many studies that show a stronger correlation of price changes with the *number of trades* rather than with the traded volume [16]. The small value of  $\psi$  is often interpreted in terms of discretionary trading: large market orders are only submitted when there is a large prevailing volume at the best quote, a conditioning that mitigates the impact of these large orders.

The above results are established using the total aggregated signed volumes, independent of the origin of the trades. Large brokerage or trading firms can also measure the price impact of their own trades; a concave impact function is usually observed with a value of  $\psi$  close to 1/2 [1] (see **Execution Costs**). For example, the BARRA price impact model posits that, on a time interval  $\Delta t$  needed to complete a typical trade,

$$R(\Delta t, v) = A\sigma \sqrt{\frac{v}{V}} \tag{9}$$

where  $\sigma$  is the volatility per unit time and V the traded volume per unit time, and  $A$  a numerical coefficient of order unity [2]. Different theoretical justifications for this square-root impact law are given in [2, 11] and [8].

In the case of stocks, one can also study empirically the influence of the market capitalization  $M$ . One finds that when  $\Delta t$  corresponds to a single trade, the data can be approximately rescaled as [18]

$$R(\Delta t, v) \approx M^{-0.3} F\left(M^{0.3} \frac{v}{\overline{v}}\right) \tag{10}$$

where  $\overline{v}$  is the average volume per trade for a given stock, and  $F(.)$  a master function that behaves as a power law with exponent  $\psi$ .

#### Impact Cannot be Permanent

As we observed above, a permanent impact model leads to unpredictable price changes only if the signed volume is uncorrelated. However, empirical data show that on a large variety of markets the autocorrelation of the signs  $\epsilon_n$  decays extremely slowly with time, over at least several days, representing thousands of trades or more [3]. The order flow is therefore found to be strongly persistent and predictable. This comes from the fact that even "highly liquid" markets only offer very small volumes for immediate execution. The fact that the outstanding liquidity is so small has an immediate consequence: trades must be fragmented, and need several hours, days, or even weeks to be completed. This clearly creates long memory in the sign of the order flow and shows that private information can only be slowly incorporated into prices. This observation, however, is incompatible with a permanent impact model such as equation (2), which would lead to trends, that is, strongly autocorrelated price changes.

#### *Nonlinear Transient Impact*

To reconcile persistent order flow with nearly unpredictable price changes, one can postulate a nonlinear, transient impact model that generalizes equation (2) above.

$$p_T = p_{-\infty} + \lambda \sum_{n=-\infty}^{N-1} G(N-n)\epsilon_n v_n^{\psi} \qquad (11)$$

where  $G(\ell)$  describes the temporal behavior of impact. One can show that it is possible to choose a certain *decaying shape* for the impact function  $G(\ell)$ such as to offset exactly the autocorrelation of the order flow and ensure that the price changes are white noise.

Assume for simplicity that volumes are all equal:  $v_n \equiv v, \forall n$ . One can then show that if  $C(\ell) = E[\epsilon_n \cdot$  $\epsilon_{n+\ell}]$  decays for large  $\ell$  as  $\ell^{-\gamma}$  with  $\gamma < 1$  (typically  $\gamma \approx 0.5$  for stocks), then  $G(\ell)$  should itself decay to zero as  $\ell^{-\beta}$  with  $\beta = (1 - \gamma)/2$  [4]. A permanent impact component  $G(\ell \to \infty) > 0$  is only compatible with the random nature of prices if  $C(\ell)$  decays fast enough (*γ >* 1). Within this transient impact model with fixed volume of trades, the relation between the price impact function *R(T )*, *G()*, and *C()* reads [4] as follows:

$$R(T = \ell \Delta t)$$
  
=  $\lambda v^{\psi} \bigg[ G(\ell) + \sum_{0 < j < \ell} G(\ell - j) C(j)$   
+  $\sum_{j > 0} \big[ G_0(\ell + j) - G_0(j) \big] C(j) \bigg]$  (12)

In other words, the impact *G()* of a single trade in isolation is different from the directly measurable impact *R(T )*, which picks up contributions from the fact that trades tend to repeat themselves in the same direction.

Note that even if the impact *G()* of an individual trade decays with time, one can show that both the total impact *R(T )* and the correlation *ρ(T )* defined by equation (6) tend to a nonzero limit when *T* is large, whenever the relation *β* = *(*1 − *γ )/*2 holds.

Finally, we mentioned above that the linear impact model, corresponding to *ψ* = 1, is the only choice consistent with the absence of price manipulation strategies if impact is permanent (*β* = 0). But if impact is transient, other values of *ψ* ≤ 1 become acceptable. Gatheral has recently shown that if *β* + *ψ* ≥ 1, price manipulation is not possible [9].

### *Surprise in the Order Flow*

If one insists *a priori* that prices must follow a strict random walk, then only the *surprise* in the order flow can impact the price. In other words, the impact of the trades in the *n*th interval of time *t* should read (neglecting volume fluctuations) as follows:

$$\Delta p_n = \lambda v^{\psi} \left( \epsilon_n - E[\epsilon_n | I_{n-1}] \right) \tag{13}$$

where *In*<sup>−</sup><sup>1</sup> is the information set available just before the *n*th interval of time. If the *<sup>n</sup>*'s are independent, then *E*[*<sup>n</sup>*|*In*−1] = 0 and one recovers the specification of the Kyle model. If, on the other hand, the *<sup>n</sup>*'s are correlated, then one can form a prediction for the next value of *<sup>n</sup>* based on the past realizations *m<n*, such that the surprise component *<sup>n</sup>* − *E*[*<sup>n</sup>*|*In*−1] is, by construction, uncorrelated for different times. Within this simplified framework, there are only two possible outcomes: either the sign of the *n*th transaction matches the sign of the predictor *E*[*<sup>n</sup>*|*In*−1], or the signs are opposite. It is easy to show that the more likely outcome, that is, *<sup>n</sup>* = sign*(E*[*<sup>n</sup>*|*In*−1]*)*, has the smaller impact [10]. Because of the positive correlation in order flow, the impact of a buy following a buy should be less than the impact of a sell following a buy–otherwise trends would appear. The detailed microstructural mechanism for such an history-dependent asymmetric impact is a topic of research (see [3] and references therein).

Using a linear autoregression model for *E*[*<sup>n</sup>*|*In*−1] allows one to identify the above surprise model, equation (13), with the transient impact model of the previous section. Following Hasbrouck's VAR model [12], one may assume that

$$E[\epsilon_n|I_{n-1}] = \sum_{j=1}^{\infty} a_j \epsilon_{n-j} \tag{14}$$

where the coefficients *aj* can be computed from the sign autocorrelation *C()* using standard methods in filtering theory. Then the above transient impact model is precisely recovered provided the following identification holds:

$$G(\ell) = 1 - \sum_{j=1}^{\ell-1} a_j \tag{15}$$

# **Spread and Impact are Two Sides of the Same Coin**

Since MMs (or liquidity providers) cannot guess the surprise of the next trade, they post a bid price *bn* and an ask price *an* given by

$$a_n = p_{n-1} + \lambda v^{\psi} \left( 1 - E[\epsilon_n | I_{n-1}] \right);$$
  

$$b_n = p_{n-1} + \lambda v^{\psi} \left( -1 - E[\epsilon_n | I_{n-1}] \right) \tag{16}$$

The above rule ensures no *ex post* regrets for the market maker: whatever the sign of the trade, the traded price is always the "right" one [19]. The bid– ask spread *S* is then given by:

$$S = a_n - b_n = 2\lambda v^{\psi} \tag{17}$$

showing that spread and impact are two sides of the same coin: liquidity providers must be compensated for the adverse impact of market order trades (see Adverse Selection: Limit Order Markets). Conversely, one sees that the impact of trades is expected to be proportional to the bid-ask spread, suggesting that the volatility per trade  $\sigma_1$  is also proportional to the bid-ask spread. Such a correlation is well supported by empirical data [21]. The relation with the volatility *per unit time*  $\sigma$  involves the trading frequency f, through  $\sigma = \sigma_1 \sqrt{f}$ .

## Conclusion

Although "price impact" seems to convey the idea of a forceful and intuitive mechanism, the story behind it might not be that simple. Empirical studies show that the correlation between signed order flow and price changes is indeed strong, but the impact of trades is neither linear in volume nor permanent, as assumed in several models, such as the Kyle model. Impact is rather found to be strongly concave in volume and transient, the latter property being a necessary consequence of the long-memory nature of the order flow. Only after averaging on a long timescale (on the order of days) may an effective linear and permanent model make sense. This is an important observation not only for monitoring and control of execution costs but also for building agent-based models of market activity that often posit linear and permanent impact. Coming back to Hasbrouck's [13] comment -do trades impact prices or do they *forecast* future price changes? Since trading on modern electronic markets is anonymous, there cannot be any obvious difference between "informed" trades and "uninformed" trades if the strategies used for their execution are similar. Hence, the impact of any trade must statistically be the same, whether informed or not informed. Impact indeed allows private information to be reflected in prices, but by the same token, random fluctuations in order flow (induced by noise traders) must also contribute to the volatility of markets.

## **End Notes**

<sup>a.</sup> $\epsilon = +1$  if the volume of buys  $v_b$  is larger than the volume of sells  $v_s$  in the time interval  $\Delta t$ , and  $\epsilon = -1$  in the opposite case; and  $v = |v_b - v_s|$ .

## References

- Almgren, R., Thum, C., Hauptmann, H.L. & Li, H.  $[1]$ (2005). Equity market impact, Risk 18(7, July), 57-62.
- BARRA (1997). Market Impact Model Handbook, Barra, [2] Berkeley.
- Bouchaud, J.-P., Farmer, J.D. & Lillo, F. (2009). How [3] markets slowly digest changes in supply and demand, in Handbook of Financial Markets: Dynamics and Evolution, T. Hens & K. Schenk-Hoppe, eds, Elsevier, North-Holland.
- Bouchaud, J.-P., Gefen, Y., Potters, M. & Wyart, M. [4] (2004). Fluctuations and response in financial markets: the subtle nature of "random" price changes, Quantitative Finance  $4(2)$ , 176–190.
- Evans, M. & Lyons, R. (2002). Order flow and [5] exchange rate dynamics. Journal of Political Economy 110, 170–180.
- Farmer, J.D. (2002). Market force, ecology and evolu-[6] tion, Industrial and Corporate Changes 11, 895–953.
- [7] Farmer, J.D., Patelli, P. & Zovko, I. (2005). The predictive power of zero intelligence in financial markets, Proceedings of National Academy of Sciences of USA 102, 2254-2259.
- [8] Gabaix, X., Gopikrishnan, P., Plerou, V. & Stanley, H. (2006). Institutional investors and stock market volatility, Quarterly Journal of Economics 121, 461-504.
- [9] Gatheral, J. (2008). No dynamic arbitrage and market impact, Working Paper.
- [10] Gerig, A. (2007). A Theory for Market Impact: How Order Flow Affects Stock Price. PhD thesis, University of Illinois (available at: arXiv:0804.3818).
- [11] Grinold, R.C. & Kahn, R.N. (1999). Active Portfolio Management, McGraw-Hill.
- [12] Hasbrouck, J. (1991). Measuring the information-content of stock trades, Journal of Finance 46, 179-207.
- [13] Hasbrouck, J. (2007). *Empirical Market Microstructure*, Oxford University Press.
- [14] Hasbrouck, J. & Seppi, D. (2001). Common factors in prices, order flows and liquidity, Journal of Financial Economics 59, 388-411.
- [15] Huberman, G. & Stanzl, W. (2004). Price manipulation and quasi-arbitrage, *Econometrica* 74, 1247-1276.
- Jones, C., Kaul, G. & Lipson, M.L. (1994). Transactions, [16] volume, and volatility, Review of Financial Studies 7, 631-651.
- [17] Kyle, A. (1985). Continuous auctions and insider trading, Econometrica 53, 1315-1335.
- [18] Lillo, F., Farmer, J.D. & Mantegna, R.N. (2003). Master curve for price impact function, Nature 421, 129-130.
- [19] Madhavan, A., Richardson, M. & Roomans, M. (1997). Why do security prices fluctuate? A transaction-level analysis of NYSE stocks, Review of Financial Studies 10, 1035-1064.

- [20] Plerou, V., Gopikrishnan, P., Gabaix, X. & Stanley, H.E. (2002). Quantifying stock price response to demand fluctuations, *Physical Review E* **66**, 027104.
- [21] Wyart, M., Bouchaud, J.-P., Kockelkoren, J., Potters, M. & Vettorazzo, M. (2008). Relation between bid-ask spread, impact and volatility in double auction markets, *Quantitative Finance* **8**, 41–57.

**Related Articles**

**Algorithmic Trading**; **Inventory Effects**; **Kyle Model**; **Liquidity**; **Market Microstructure Effects**.

JEAN-PHILIPPE BOUCHAUD
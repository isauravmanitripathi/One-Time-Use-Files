# **Good-deal Bounds**

Most contingent claims valuation is based, at least notionally, on the concept of exact replication. The difficulties of exactly replicating derivative positions suggest that in many cases we should, instead, put bounds around the value of an instrument. These bounds ought to depend on model assumptions and on the prices of securities that would be used to exploit mispricing. No-arbitrage bounds are often very weak, so good-deal bounds provide an attractive alternative.

Good-deal bounds provide a range of prices within which an instrument must trade if it is not to offer a surprisingly good reward-for-risk opportunity. This is illustrated in Figure 1, where the horizontal axis represents the distribution of future payoffs (or values) after zero cost hedging. In an incomplete market setting, rather strong assumptions are needed to arrive at a unique forward value, such as  $p^*$  in the figure. Conversely, risk-free arbitrage typically allows a rather wide band of prices, as between the upper and lower bounds  $b_{+}, b_{-}$ . We can hope to obtain a much narrower band without the need for strong assumptions if we simply preclude profitable opportunities. This gives the good-deal bounds  $p_{+}$  and  $p_{-}$ . These bounds have two alternative interpretations: we can think of them as establishing normative bid and ask forward prices for a particular trader or as predicting a range in which we expect the market price to lie.

This line of valuation analysis now has an interesting history and it has inspired a quite significant literature, much of it very mathematical. There are a great many different variations by which the philosophy just described can be implemented.

This article aims to cover the main issues without going too deeply into mathematical technicalities. We begin by considering a simple illustrative example to provide intuitive insights into the nature of the analysis, including the use of duality in the solutions. We then sketch the history of this topic, including the generalized Sharpe ratio. Finally, there is a discussion of the role of the utility function (see **Utility Function**) in the analysis, of applications, and of the more recent literature.

## Illustration

Consider the problem faced by a financial intermediary in determining reservation bid and ask prices for some derivative which can, at best, only be partly hedged. There is no chance of replicating this claim exactly, and super-replication bounds may be too loose to be practically helpful. The company expects to trade using some kind of statistical arbitrage, for which each transaction passes a minimum rewardfor-risk threshold and overall to obtain a portfolio that performs much better than that minimun.

More specifically, reservation forward bid and ask prices  $p_{-} < p_{+}$  are to be determined at time zero for a derivative that will pay a random amount  $\tilde{C}_T$  at later date  $T$ . We suppose a von Neumann-Morgenstern utility function  $U(.)$  for date  $T$  wealth and a forward wealth endowment of  $W_0$ . The reservation prices are constructed so that trade will provide a level of expected utility at a predetermined level  $U_R$  that exceeds the expected utility that could be reached without it by  $A > 0$ .

Figure 2 illustrates the construction. The horizontal axis represents the price of the contingent claim. The vertical axis represent the expected utility obtained from buying (or selling) the optimal quantity of the claim. Outside the super-replication bounds,  $b_{-}, b_{+}$ , unbounded wealth can be obtained.

In the case where no hedging will be undertaken and the forward price of the claim is  $p$ , we simply have the optimization of the quantity  $\theta$  bought or sold as

$$\frac{Max}{\theta}E\left[U\left(W_0+\theta\left(\tilde{C}_T-p\right)\right)\right] \tag{1}$$

If  $p$  is low enough we will expect to buy the claim, and if  $p$  is high enough we will want to sell it. Intuitively the good-deal lower bound,  $p_{-}$ , is the highest price at which we can buy the claim and obtain expected utility of  $U_R$ , and the gooddeal upper bound,  $p_{+}$ , is the lowest price at which we can sell the claim and obtain expected utility of  $U_R$ .

Now consider the first-order conditions from the optimization:

$$E\left[\left(\tilde{C}_{T}-p\right)U'\left(W_{0}+\theta\left(\tilde{C}_{T}-p\right)\right)\right]=0, \text{ so } (2)$$
$$p=\frac{E\left[\tilde{C}_{T}\left[U'\left(\tilde{W}_{T}\right)\right]\right]}{E\left[U'\left(\tilde{W}_{T}\right)\right]},$$
$$\text{where } \tilde{W}_{T}=W_{0}+\theta\left(\tilde{C}_{T}-p\right) \tag{3}$$

![](_page_1_Figure_1.jpeg)

Figure 1 Good-deal bounds. Alternative forward prices and the distribution of future values after zero cost hedging:  $b_{-}, b_{+}$ : super-replication bounds;  $p_{-}, p_{+}$ : good-deal bounds;  $p^*$ : unique (indifference) price

![](_page_1_Figure_3.jpeg)

Figure 2 Expected utility against price. The good-deal bounds,  $p_{-}, p_{+}$ , are defined as the prices at or beyond which expected utility of  $U_R$  can be obtained

Thus, the reservation price corresponds to pricing with stochastic discount factors induced by the marginal utility at the optimal wealth levels corresponding to this price.

In principle, the extension to hedging is straightforward. The gains or losses from a self-financing strategy with zero initial cost are simply added into the date  $T$  wealth. If at date  $t$  the strategy involves holdings  $x_t$  at prices  $P_t$ , the expression for wealth at date  $T$  becomes

$$\tilde{W}_T = W_0 + \theta \left( \tilde{C}_T - p \right) + \int_0^T x_t \mathrm{d}P_t \tag{4}$$

Ideally, we would like to find and use the optimum hedging strategies, but any strategies that enhance expected utility will provide tighter reservation prices. Note that if the claim can be replicated exactly, then both the good-deal bounds will tend to the replication cost. Similarly, the good-deal bounds will always be at least as tight as any superreplication bounds that can be based on the same assumptions.

So far, we have only described the primal view of this problem. Well-known duality results provide an alternative viewpoint that provides both insights and alternative computational schemes. The good-deal lower bound is characterized as the infimum of values over nonnegative changes of measure,  $m$ , that price all reference assets and have insufficient dispersion to provide higher levels of expected utility. For example,

$$p_{-} = \inf_{m \ge 0} \left\{ E \left\lfloor m \tilde{C}_{T} \right\rfloor \right\} \text{ subject to}$$
  
$$E[V(m)] \le A, \ E[mS_{T}] = S_{0}$$
(5)

where  $V(m)$  is the conjugate function of U, defined by

$$V(m) = \sup_{S_T} \{ U(S_T) - mS_T \} \text{ for } m > 0 \tag{6}$$

and the final constraint in equation  $(5)$  represents the correct pricing of reference assets.

Note that this only differs from the formulation for super-replication (no-arbitrage) bounds by the addition of the inequality constraint in equation (5), which precludes extreme changes of measure that would generate expected utility greater than  $U_R$ . In both cases, the more assets we hedge with, the more the change of measure is constrained and the tighter the valuation bounds.

#### Early Literature

Finding bounds on the values of derivatives has a long history. Merton [15] summarizes the conventional upper and lower bounds on vanilla options and how they are enforced by arbitrage. The subsequent contributions of Harrison and Kreps [10], Dybvig and Ross [8], and others have shown the pricing implications of no arbitrage more generally. Later papers by Perrakis and Ryan [16] and Levy [14] obtained slightly more general bounds on the prices of options, for example, based on stochastic dominance by adding some additional stronger assumptions. More recently a number of papers, such as [11], have considered super-replication bounds on exotic options when vanilla options can be used to engineer the hedge (see Arbitrage Bounds). Interest in this topic has further intensified with the growth of the literature on Levy processes (see **Exponential Lévy Models**), exotic options, and incomplete markets.

Much of the work in the incomplete markets literature focuses on ways to obtain a particular pricing measure and hence unique prices (for example, *see* **Minimal Entropy Martingale Measure**; **Minimal Martingale Measure** and Schweitzer [17]), but it is not clear why a particular agent would be prepared to trade at these prices.

The good-deal literature represents an important alternative between these two paths. Hansen and Jagannathan [9] provide a crucial stepping stone. They showed that the Sharpe ratio on any security is bounded by the coefficient of variation of the stochastic discount factor (*see* **Stochastic Discount Factors**). The Sharpe ratio provides a very natural benchmark (see [18]) and Cochrane and Saa-Requejo ´ [6] subsequently used this to limit the volatility of the stochastic discount factor and infer the first no-gooddeal prices, conditional on the absence of high Sharpe ratios. At about the same time, a related paper by Bernardo and Ledoit [2] showed how similar bounds could be obtained relative to a maximum gain–loss ratio for the economy as a whole. These papers have their disadvantages. Cochrane and Saa-Requejo ´ work with quadratic utility (and sometimes truncated quadratic utility), whereas Bernardo and Ledoit use Domar–Musgrave utility (i.e., two linear segments). This led Hodges [12] to investigate bounds based on the more conventional choice of exponential utility and to thereby introduce the idea of a generalized Sharpe ratio.

This concept was extended by Cern ˇ y and Hodges ´ [5] into the more general framework of good-deal pricing mostly used today. By then, it was already clear that these prices satisfied the criteria for coherent risk measures of Artzner *et al.*, [1], namely, the linearity, subadditivity, and monotonicity properties. This includes the representation of the lower gooddeal price as an infimum over values from alternative pricing measures. Nevertheless, Jaschke and Kuchler ¨ [13] provided an important clarification and unification of these ideas.

## **General Framework**

The general framework of "no-good-deal" pricing (first described by Cern ˇ y and Hodges [5]) places no- ´ arbitrage and representative agent equilibrium at the two ends of a spectrum of possibilities. They define a *desirable claim* as one which provides a specific level of von Neumann–Morgenstern expected utility and a *good-deal* as a desirable claim with zero or negative price. Within the analysis, it is assumed that any quantity of any claim may be bought or sold.

The economy contains a collection of claims with predetermined prices, so called basis assets. These claims generate the marketed subspace *M* and their prices define a price correspondence on this subspace. In an incomplete market, it is often convenient to suppose that the market is augmented in such a way that the resulting complete market contains no arbitrages. Instead, we can more powerfully augment the market so that the complete market contains no good-deals. We obtain a set of pricing functionals that form a subset of those that simply preclude arbitrage.

The link between no arbitrage and strictly positive pricing rules carries over to good-deals and enables price restrictions to be placed on nonmarketed claims. Under suitable technical assumptions, the no-gooddeal price region for a set of claims is a convex set, and redundant assets have unique good-deal prices.

With an *acceptance set* of deals, *K*, typically defined in terms of expected utility, the upper and lower good-deal bounds can be defined simply as

$$p_{+} = \inf_{p, x_t} \left\{ p \left| -\tilde{C}_T + p + \int_0^T x_t \mathrm{d}S_t \in K \right\} \text{ and } (7)$$

$$p_{+} = \inf_{p, x_t} \left\{ p | \tilde{C}_T - p + \int_0^T x_t \mathrm{d}S_t \in K \right\} \tag{8}$$

For a given utility function, the positions of the good-deal bounds naturally depend on the required expected utility premium, *A*. The higher this level, the further apart the bounds will be. Coherent risk measures, well into the tails of the final distribution, can be obtained if high levels are employed for *A*. Except for the case of exponential utility, the bounds also depend on the initial wealth level.

## **Generalized Sharpe Ratios**

One method for setting the required premium comes from the Sharpe ratio available on a market opportunity. This give rise to what are called generalized Sharpe ratio bounds (see [12] or [4]). The idea is to first compute the level of expected utility *UR* attainable from a market opportunity offering a specific annualized Sharpe ratio, such as 0.25, and without any investment in the derivative. The good-deal bounds that are supported by this level of expected utility (but without this market opportunity) are then said to correspond to a generalized Sharpe ratio of  $0.25$ . In the case of negative exponential utility, the wealth level and the risk aversion parameter play the same role and become irrelevant since the opportunity can be accepted at any scale. This provides a particularly simple implementation with minimal parameter requirements.

Subsequent analysis by  $\check{\text{Cern}}\check{\text{y}}$  [4] further expands both the notions and the analysis of generalized Sharpe ratios. The analysis provides details of the dual formulations for alternative standard utility functions. For example, the dual constraints on the change of measure  $m$  for different utility functions are as given in Table 1.

The various properties of the utility affect the details of the mathematical analysis considerably. For some features to work cleanly we need unbounded utility, whereas for others the behavior for low wealth levels is critical. Exponential utility precludes any delta hedge that gives a short lognormal position over finite time-even though it would have a smaller standard deviation than the fully covered position. Capping such a liability at a finite level can therefore have a big effect on the good-deal price resulting from such an analysis. Depending on the context, this may or may not be desirable. While exponential utility precludes fat negative tails, such as the short lognormal, power and log utility preclude the possibility of any negative future wealth, and even stronger effects can, in principle, derive from this.

With constant absolute risk aversion (CARA) utility, changing the scale of investment is equivalent to changing the level of risk aversion. With constant relative risk aversion (CRRA), it is equivalent to scaling the initial wealth,  $W_0$ . The CRRA-based good-deal bound thus searches across measures with the same exponent, but different wealth levels. There may be some advantages to finding alternative utility functions that have properties intermediate between

<table>

 **Table 1** Stochastic discount factor constraints for various
utility functions

| Utility function                                                                        | Constraint                                                                                                                          |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Ouadratic: Cochrane <i>et al.</i><br>Exponential<br>Power, RRA $=\gamma$<br>Logarithmic | $E[m^2] \leq 1 + A^2$<br>$E[m \ln m] < A$<br>$E[m^{1-1/\gamma}] \leq (1+\frac{A}{\gamma})^{1/\gamma-1}$<br>$-E[\ln m] \le \ln(1+A)$ |

the Domar-Musgrave function used by Bernardo and Ledoit and the negative exponential one.

#### **Coherent Risk Measures**

Jaschke and Küchler [13] expand the link between good-deal bounds and coherent risk measures. They show that there is a one-to-one correspondence between

- "coherent risk measures" (see Convex Risk 1. Measures)
- 2. cones of "desirable claims"
- partial orderings 3.
- 4. good-deal valuation bounds
- 5. sets of "admissible" price systems.

It should be noted from this analysis that it is sufficient but not necessary to use expected utility to define all the abstract measures considered in their paper. In other words, acceptance sets must be consistent with coherence, but not necessarily with expected utility.

It is clear from the foregoing that good-deal analysis can easily be applied as the basis of risk measurement and will satisfy the axioms of coherent risk measures (see Convex Risk Measures). They can also be applied as a method of risk adjustment for performance measurement. For example, a utilitybased generalized Sharpe ratio, when applied to an empirical distribution, provides a method of adjusting for skewness in the distribution. In doing so, it makes sense to apply a negative sign to situations where a short position would have been optimal.

#### **Recent and Prospective Literature**

Important new papers continue to appear quite regularly; a few recent ones are mentioned here. Staum [19] provides much of the background, treating good-deals from the perspective of convex optimization. Bjork and Slinko [3] provide extensions to Cochrane and Saá-Requejo in a multidimensional jump-diffusion setting. There are further papers that expand on the dynamic aspects of this analysis, apply it to settings with stochastic volatility, or implement similar optimizations using mathematical programming. There are also a number of papers, which although not directly within the framework developed here, deal with related ideas in different ways.

The apparently simple concept of good-deal bounds has turned out to provide a great deal of richness for mathematicians to analyze, and there are now many variations on this theme in the published literature. Although the theory stems from a practical desire, very few of the papers have an applied flavor. Rather little algorithmic or numerical work has been reported, and most of that uses only somewhat simplified models, seldom calibrated to the market. The good-deal bounds approach could easily be adapted to deal with model risk, something which is hinted at in Cont [7]. The literature needs more real applications, and, perhaps, the balance will have changed when the next survey of this area comes to be written.

## **References**

- [1] Artzner, P., Delbaen, F., Eber, J. & Heath, D. (1999). Coherent measures of risk, *Mathematical Finance* **9**(3), 203–228.
- [2] Bernardo, A. & Ledoit, O. (1996). Gain, loss and asset pricing, *Journal of Political Economy* **108**(1), 144–172.
- [3] Bjork, T. & Slinko, I. (2006). Towards a general theory of good-deal bounds, *Review of Finance* **10**, 221–260.
- [4] Cern ˇ y, A. (2003). Generalised sharpe ratios and asset ´ pricing in incomplete markets, *European Finance Review* **7**, 191–233.
- [5] Cern ˇ y, A. and Hodges, S.D. (2001). The theory of good- ´ deal pricing in financial markets, in *Selected Proceedings of the First Bachalier Congress Held in Paris, 2000*, H. Geman, D. Madan, S.R. Pliska & T. Vorst, eds, Springer Verlag.
- [6] Cochrane, J.H. & Saa-Requejo, J. (2000). Beyond arbi- ´ trage: 'Good-Deal' asset price bounds in incomplete markets, *Journal of Political Economy* **108**(1), 79–119.
- [7] Cont, R. (2006). Model uncertainty and its impact on the pricing of derivative instruments, *Mathematical Finance* **16**(3), 519–547.
- [8] Dybvig, P.H. & Ross, S.A. (1987). Arbitrage, in *The New Palgrave: A Dictionary of Economics*, J. Eatwell, M. Milgate & P. Newman., eds, Macmillan, London, Vol. 1, pp. 100–106.

- [9] Hansen, L.P. & Jagannathan, R. (1991). Implications of security market data for models of dynamic economies, *Journal of Political Economy* **99**, 225–262.
- [10] Harrison, J. & Kreps, J. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **11**, 215–260.
- [11] Hobson, D.G. (1998). Robust hedging of the lookback option, *Finance and Stochastics* **2**, 329–347.
- [12] Hodges, S.D. (1998). *A Generalization of the Sharpe ratio and its Applications to Valuation Bounds and Risk Measures*. FORC Preprint 1998/88, University of Warwick.
- [13] Jaschke, S. & Kuchler, U. (2001). Coherent risk mea- ¨ sures and good-deal bounds, *Finance and Stochastics* **5**, 181–200.
- [14] Levy, H. (1985). Upper and lower bounds of put and call option values: stochastic dominance approach, *Journal of Finance* **40**, 1197–1218.
- [15] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics* **4**, 141–183.
- [16] Perrakis, S. & Ryan, P.J. (1984). Option pricing bounds in discrete time, *Journal of Finance* **39**, 519–525.
- [17] Schweizer, M. (1995). On the minimal martingale measure and the Follmer-Schweizer decomposition, ¨ *Stochastic Analysis and its Applications* **13**, 573–599.
- [18] Sharpe, W.F. (1994). The sharpe ratio, *Journal of Portfolio Management* **21**, 49–59.
- [19] Staum, J. (2004). Pricing and hedging in incomplete markets: fundamental theorems and robust utility maximization, *Mathematical Finance* **14**(2), 141–161.

## **Related Articles**

**Arbitrage Strategy**; **Convex Risk Measures**; **Stochastic Discount Factors**; **Sharpe Ratio**; **Superhedging**; **Utility Function**.

STEWART D. HODGES
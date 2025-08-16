# **Spectral Measures of Risk**

The term spectral measures of risk (SMRs) [1] denotes a subclass of coherent measures of risk (CMRs) [4] (see Convex Risk Measures) characterized by the additional properties of law invariance and comonotonic additivity, which make them particularly appropriate for financial risk management applications. In financial mathematics, this class was first defined in [1] and [7], which studied it from different perspectives. It was however soon realized that this class is in close correspondence with socalled distortion measures already introduced in 1996 in actuarial mathematics [9] in a different axiomatic framework from that of CMRs.

The most popular example of SMR is given by conditional Value at Risk/expected shortfall  $(ES)$  (see **Expected Shortfall**), which is, in fact, the building block of all the class of SMRs as will be seen.

An SMR of a random variable  $(r.v.)$  X denoted by  $\rho_{\phi}(X)$  can be defined as *minus the*  $\phi$ -weighted average of all possible outcomes of  $X$  sorted from the lowest to the highest, where  $\phi$  is a weight function, called the risk spectrum of the SMR, which needs to be positive, normalized, and decreasing.

In financial risk management, the SMR of a portfolio  $\pi$  usually means the SMR  $\rho_{\phi}(r_T^{(\pi)})$  of the return  $r_T^{(\pi)} = \pi_T - (1 + R) \pi_0$  between the current date  $t = 0$  and a chosen future date  $t = T$ , R being the risk-free interest. Clearly,  $\rho_{\phi}(r_T^{(\pi)})$  expresses the  $\phi$ -weighted average of all possible losses of  $\pi$  sorted in decreasing order.

Strictly speaking, it is only the SMR  $\rho_{\phi}(\pi_T)$  of the "value" (and not of the "return") of a portfolio that is a true CMR for the same reasons as explained for  $ES$  in **Expected Shortfall**. In this article, we discuss the mathematical properties of an SMR as a statistic of a generic r.v.  $X$  and loosely use the term *coherent* to mean monotonic, translational invariant, positive homogeneous, and subadditive.

## Formal Definition of SMR

For the sake of simplicity, we overlook some technical details such as integrability of r.v.'s and continuity of risk measures. For a more detailed exposition, we refer to [6].

SMRs can be defined as the most general convex combinations of all possible  $ESs$ . Let us consider a probability space with probability measure  $P$  and let X be an r.v. A generic SMR  $\rho^{\mu}(X)$  can therefore be uniquely written as

$$\rho^{\mu}(X) = \int_0^1 ES_{\alpha}(X) \, \mathrm{d}\mu(\alpha) \tag{1}$$

where  $d\mu$  is a measure on the interval [0, 1] and, *vice versa*, any such  $d\mu$  defines an SMR.

For the sake of financial intuition, this expression can be recast into a mixture of quantiles of the variable X. Let  $F_X^{-1}:(0,1) \to \mathbb{R}$  denote an inverse function of the probability distribution function  $F_X(x)$  of X. Choose, for instance, the lower p-quantile function  $F_X^{-1}(p) := q_p(X) =$  $\inf\{x \in \mathbb{R} | F_X(x) \ge p\}$ . One can show that  $\rho^{\mu} = \rho_{\phi}$ with

$$\rho_{\phi}(X) = -\int_{0}^{1} \phi(p) F_{X}^{-1}(p) \, \mathrm{d}p \tag{2}$$

with  $\phi$  defined by

$$\begin{aligned} \phi(p) &= \mu(\{0\}) \,\delta_0(p) & p &= 0\\ \phi(p) &= \int_{[p,1]} \mathrm{d}\mu(\alpha) \,\alpha^{-1} & p \in (0,1] \end{aligned} \tag{3}$$

Alternatively, one can adopt equation  $(2)$  as a definition of SMR. The *risk spectrum*  $\phi$  must be of the form  $\phi = c\delta_0(p) + \phi$  with  $c \in [0, 1]$  and  $\phi : [0, 1] \to \mathbb{R}$ and satisfy the conditions

$$\begin{aligned} \phi(p) &\ge 0 & 0 < p \le 1 \\ \int_{[0,1]} \phi(p) \, \mathrm{d}p &= 1 \\ \phi(p_1) &\ge \phi(p_2) & 0 < p_1 < p_2 \le 1 \end{aligned} \tag{4}$$

which can be shown to be necessary and sufficient for  $\rho_{\phi}$  in equation (2) to be a coherent measure of risk [1]. We see therefore that equation  $(2)$  can indeed be read as minus the  $\phi$ -weighted average of all the outcomes of X sorted in decreasing order, where  $\phi$ is a positive, normalized, and decreasing function. In general,  $\phi$  also admits a Dirac delta term  $c\delta_0$  in the origin, but the singular case  $c \neq 0$  is of no practical interest.

Expression  $(2)$  together with conditions  $(4)$  tells us that a mixture of quantiles is coherent only when they are weighted in such a way that worse events are given higher weights. This is an important lesson we learn when dealing with quantile-based measures of risk. We immediately also learn that for such a measure to be coherent it needs to weight all the left tail without neglecting any portion of its extreme values.

If we consider  $\alpha$ -Value at Risk  $(V@R_{\alpha})$  (see Value-at-Risk), which is not a CMR (and hence not an SMR), we see that it can also be expressed through formula (2), but its risk spectrum turns out to be a Dirac delta  $\phi^{V@R_{\alpha}}(p) = \delta_{\alpha}(p)$ , which is clearly not decreasing on  $[0, 1]$ . Here, we see that the reason why  $V@R$  is not a CMR lies exactly in the fact that it completely neglects the worst cases at quantiles smaller than  $\alpha$ .

Taking  $ES_{\alpha}$  (see **Expected Shortfall**) as an example of SMR, it is easy to show that its risk spectrum is given by  $\phi^{ES_{\alpha}}(p) = \alpha^{-1} \mathbf{1}_{p < \alpha}$ , namely, it is flat on  $[0, \alpha]$  and vanishing elsewhere. This is a perfectly coherent choice corresponding to an equally weighted average of all the cases beyond the  $\alpha$  quantile only.

The function  $\phi$  is also termed a *risk-aversion function* of the SMR [1] because it expresses different aversions encoded in  $\rho_{\phi}$  to different quantiles of the profit-loss distribution.

The relationship with the class of "distortion measures" defined in [9] is established by writing

$$\rho_{\phi}(X) = D_{\varrho}(-X) \tag{5}$$

where the distortion measure  $D_g$  is defined as the *Choquet integral (see, for instance, [6])* 

$$D_{g}(Y) := \int Y \, \mathrm{d}(g_{\circ}P) = \int_{0}^{\infty} g \, (1 - F_{Y}(y)) \, \mathrm{d}y$$
$$+ \int_{-\infty}^{0} \left[ g \, (1 - F_{Y}(y)) - 1 \right] \, \mathrm{d}y \qquad (6)$$

and the function  $g: [0, 1] \to \mathbb{R}$  is a "concave distortion" of the probability measure  $P$ . The function  $g$  is related to  $\phi$  by

$$g(p) = 0 \t p = 0$$
  
$$g(p) = c + \int_{(0,p]} \phi(q) \, \mathrm{d}q \quad p \in (0,1] \t (7)$$

The expression  $D_g(-X)$  is another possible definition of SMR, provided that  $g:[0,1] \to \mathbb{R}$  is increasing and concave and satisfies  $g(0) = 0$  and  $g(1) = 1$ .

In [9], the definition of "distortion measures" is slightly less general, as it is given on positive-valued loss variables  $Y$  only, which reflects the actuarial context. Notice also the different convention between the actuarial literature (where losses are modeled as positive variables) and the financial literature (where profits are modeled as positive variables). Apart from these technical details, Wang's work [9] can be considered a precursor of the development of SMRs in all respects.

As an example of SMR, consider the oneparameter family class of exponential risk spectra given by

$$\phi_{\gamma}(p) = \frac{\mathrm{e}^{-p/\gamma}}{\gamma \left(1 - \mathrm{e}^{-1/\gamma}\right)}\tag{8}$$

It is easy to show that this expression satisfies equation (4) and therefore defines an SMR for any  $\gamma > 0$ . This risk spectrum is nonvanishing on all the quantiles range  $p \in [0, 1]$ . Smaller values of  $\gamma$ provide SMRs that are more focused on the extreme left tail of the distribution.

The corresponding concave distortion is easily obtained from equation  $(7)$ :

$$g(p) = \frac{1 - e^{-p/\gamma}}{1 - e^{-1/\gamma}}$$
 (9)

# **Properties of SMRs and Their** Characterization

Any SMR  $\rho_{\phi}$  can be shown to be coherent [1, 7] (see Convex Risk Measures). In other words, it satisfies the following properties  $[4]$ :

(i) *monotonicity* 

$$\rho_{\phi}(X) \ge \rho_{\phi}(Y) \quad \text{if} \quad X \le Y \text{ almost surely.}$$
(10)

(ii) translational invariance

$$\rho_{\phi}(X+c) = \rho_{\phi}(X) - c \quad \text{if} \quad c \in \mathbb{R} \quad (11)$$

(iii) positive homogeneity

$$\rho_{\phi}(\lambda X) = \lambda \,\rho_{\phi}(X) \quad \text{if} \quad \lambda \ge 0 \tag{12}$$

(iv) *subadditivity* 

$$\rho_{\phi}(X+Y) \le \rho_{\phi}(X) + \rho_{\phi}(Y) \tag{13}$$

These conditions represent the cornerstone of axiomatic financial risk theory and strong arguments have been given to show that any measure of risk violating them turns out to be inappropriate for capital allocation purposes. In particular, subadditivity embodies the risk diversification principle and prevents the occurrence of paradoxical regulatory arbitrages. Adopting a nonsubadditive measure of risk to compute the regulatory capital of a portfolio, in fact, one can, in principle, obtain a lower value by just splitting the portfolio into two parts and computing the regulatory capital on each part [3].

Conditions (iii) and (iv) imply, in particular, convexity

$$\rho_{\phi}(\mu X + (1 - \mu) Y) \n\leq \mu \rho_{\phi}(X) + (1 - \mu) \rho_{\phi}(Y) \quad \text{if} \quad \mu \in [0, 1] \n$$
(14)

which plays a fundamental role in asset allocation as it entails the convexity of portfolio optimization problems (see, for instance, [2, 8]).

It is particularly important to identify the additional properties that characterize SMRs as a subclass of CMRs. It can be shown that SMRs are, in fact, all CMRs that are also law invariant and comonotonic additive [6, 7].

A measure of risk is said to be *law invariant* if it only depends on the probability distribution function of its argument, or, in other words, if it takes the same value on any two r.v.'s that are identically distributed.

(vi) law invariance

$$\rho_{\phi}(X) = \rho_{\phi}(Y) \quad \text{if} \quad X \sim Y \qquad (15)$$

This property may appear puzzling at first sight because every statistic obviously satisfies it. It has, however, to be kept in mind that not all CMRs are "statistics" because they are defined without necessarily specifying a probability space, but by specifying only a set of events [4] (see Convex Risk Measures). Hence, law invariance is a stringent condition on CMRs, and, in fact, it is the condition characterizing all CMRs that are also statistics and can therefore be estimated from data [2]. This condition is therefore often considered as inevitable for practical risk management applications, where portfolios are confronted with a model of the "real-world" probability distribution.

The further characterizing property of SMRs within CMRs is comonotonic additivity

#### (vii) *comonotonic additivity*

$$\rho_{\phi}(X+Y) = \rho_{\phi}(X) + \rho_{\phi}(Y) \quad \text{if}$$
  
X, Y comonotonic (16)

This means that for SMRs the subadditivity diversification benefit of adding two portfolios  $X$  and  $Y$ vanishes in the limiting case when they happen to be comonotonic, which means they are perfectly dependent on each other (for a definition of comonotonicity, see, for instance, [5]). This property is also crucial, particularly in the context of capital adequacy in association with subadditivity, because, if it does not hold, another kind of regulatory arbitrage opportunity appears. By exploiting subadditivity, one could lower the capital requirement of two distinct portfolios by just putting them together, even in the comonotonic case when they provide no mutual hedge at all. It seems, in other words, that the diversification principle is correctly represented by conditions (iv) and (vii) together and not by subadditivity alone.

Law invariance and comonotonic additivity, therefore, enrich the set of coherency axioms  $(i)$ - $(iv)$ . Owing to these additional properties, SMRs are considered to be a particularly interesting subset of CMRs for concrete risk management applications (see, for instance, [3] for a discussion).

Further properties of SMRs are monotonicity with respect to both first- and second-order stochastic dominance [6], which are important preference criteria among portfolios in utility theory. We recall that an r.v.  $X$  is said to dominate  $Y$  according to first-order stochastic dominance (notation:  $X \stackrel{1^{st}}{\succ} Y$ ) if  $F_X(z) \leq$  $F_Y(z)$  for all  $z \in \mathbb{R}$ , while X is said to dominate  $Y$  according to second-order stochastic dominance (notation:  $X \stackrel{2^{nd}}{\succ} Y$ ) if  $\int_{-\infty}^{z} [F_Y(t) - F_X(t)] dt \ge 0$  for all *z* ∈  $\mathbb{R}$ . First-order implies second-order stochastic dominance. SMRs turn out to be compatible with the notions of preference among portfolios induced by stochastic dominance

(viii) *monotonicity with respect to first- and second*order stochastic dominance

$$\rho_{\phi}(X) \le \rho_{\phi}(Y) \quad \text{if} \quad X \stackrel{1^{st}, 2^{nd}}{\succ} Y \qquad (17)$$

This means that an SMR always detects higher risk on dominated portfolios.

It is important to stress that conditions  $(vi)$ – $(viii)$ do not hold, in general, for CMRs.

#### **Estimation of SMRs**

Thanks to law invariance, SMRs can be estimated from data. This is fundamental both when an empirical distribution for the variable  $X$  is given and when a closed-form solution for  $\rho_{\phi}(X)$  is not known, but one can sample from the distribution of  $X$  to perform a Monte Carlo simulation.

Consider an SMR  $\rho_{\phi}$  with a given risk spectrum  $\phi$ . Given a sample of N i.i.d. outcomes  $x_i$ , of an r.v. X, a consistent estimator of  $\rho_{\phi}(X)$  can be obtained by [1, 2]

$$\widehat{\rho}_{\phi}(X) = -\sum_{i=0}^{N} \phi_i x_{i:N} \tag{18}$$

where  $x_{i:N}$  denotes the ordered statistics, that is, the vector  $\{x_{i:N}\}_{i=1,\ldots,N}$  of values  $x_{1:N} \leq \ldots \leq x_{N:N}$ obtained sorting the vector  $\{x_i\}_{i=1,\dots,N}$  and the weights  $\phi_i$  are given by

$$\phi_i = \int_{(i-1)/N}^{i/N} \tilde{\phi}(p) \, \mathrm{d}p + \delta_{i,1} \, c \tag{19}$$

It can be shown that  $\widehat{\rho}_{\phi}(X)$  converges to  $\rho_{\phi}(X)$  for  $N \to \infty$ .  $\widehat{\rho}_{\phi}(X)$  is, in fact, nothing but the SMR  $\rho_{\phi}$ of the empirical distribution of the sample and as such it is coherent by construction for any finite  $N$ .

As an example, consider the family of SMRs defined by equation (8). It can be seen immediately that the spectrum is nonsingular  $(c = 0)$  and that the weights of the estimator  $(18)$  are given by

$$\phi_i = \frac{e^{1/N\gamma} - 1}{1 - e^{-1/\gamma}} e^{-i/N\gamma} \tag{20}$$

#### References

- [1] Acerbi, C. (2002). Spectral measures of risk: a coherent representation of subjective risk aversion, Journal of Banking and Finance 26, 1505-11518.
- [2] Acerbi, C. (2004). Coherent representations of subjective risk aversion, in Risk Measures for the 21st Century, G. Szego, ed, John Wiley & Sons, pp. 147-207.
- [3] Acerbi, C. (2007). Coherent measures of risk in everyday market practice, *Quantitative Finance* 7(4), 359–3364.
- [4] Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D. (1999). Coherent measures of risk, Mathematical Finance 9(3),  $203 - 228.$
- [5] Embrechts, P., Frey, R. & McNeil, A.J. (2005). Quantitative Risk Management, Princeton University Press.
- Föllmer, H. & Schied, A. (2004). Stochastic Finance, 2<sup>nd</sup> [6] Edition, de Gruyter.
- [7] Kusuoka, S. (2001). On law invariant coherent risk measures, Advances in Mathematical Economics 3, 83-95.
- Rockafellar, R.T. & Uryasev, S. (2001). Conditional [8] value-at-risk for general loss distributions, Journal of Banking and Finance 26, 1443-11471.
- [9] Wang, S. (1996). Premium calculation by transforming the layer premium density, Astin Bulletin  $26$ , 71–92.

### **Related Articles**

Convex Risk Measures; Expected Shortfall; Valueat-Risk.

CARLO ACERBI
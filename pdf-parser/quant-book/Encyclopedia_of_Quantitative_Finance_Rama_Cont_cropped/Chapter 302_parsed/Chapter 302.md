# **Expected Shortfall**

The synonymous terms conditional Value at Risk  $(CV@R)$  and expected shortfall (ES) refer to a particular statistics of a random variable, which is widely adopted as a measure of portfolio risk. It is also known as tail Value at Risk (TV@R) or average Value at Risk (AV@R) among other names. Here we adopt the name ES.

The "ES of a random variable  $X$ ", denoted by  $ES_{\alpha}(X)$ , is most easily defined in plain English as minus the average of the  $\alpha$  lowest outcomes of X, where  $\alpha \in [0, 1]$  is a chosen confidence level (e.g.,  $\alpha = 5\%$ ). There are several equivalent mathematical expressions of this definition. We discuss the most useful ones in the section "Mathematical Expressions for ES".

In financial risk management, the "ES of a portfolio  $\pi$ " is usually meant as the expected shortfall  $ES_{\alpha}(r_T^{(\pi)})$  of the return  $r_T^{(\pi)} = \pi_T - (1 +$  $R\pi_0$  between the current date  $t=0$  and a chosen future date  $t = T$ , in perfect analogy with the practice introduced by V@R (see Value-at-Risk). Here,  $R$  is the risk-free interest on  $[0, T]$ . It is then clear that  $ES_{\alpha}(r_T^{(\pi)})$  represents the *average portfolio loss* at time T in the  $\alpha$  worst cases.

Measures of risk similar to ES (in particular TCE, equation (2), and "average shortfall" [10]) appeared in the practice of risk management already in the early 1990s, along with the diffusion of V@R methods. The main motivation for their introduction was to remedy the fact that  $V@R$  is totally blind to the severity of the losses contained in the tail beyond the specified confidence level. The idea of averaging the outcomes contained in the tail instead of detecting only its threshold quantile is so natural that it came simultaneously from several academicians and practitioners, and this is probably the reason why no consensus was ever achieved on the name of this risk measure.

The interest around ES increased considerably after the appearance of [5] with the advent of coherent measures of risk (CMRs) (see Convex Risk Measures) and the consequent criticism that was addressed to V@R when it was recognized to be not subadditive, that is, not compatible with the risk diversification principle. ES, in fact, in the modern version introduced in  $[1, 12]$ , turned out to be a subadditive measure of risk and, in fact, it provides

the best-known example of a coherent measure of risk.

A lively debate has arisen in the past years on whether ES should replace  $V@R$  in the regulatory framework of the Basel Committee on Banking Supervision. A number of arguments [3, 5, 6] have been given to display the superiority of a coherent measure of risk for capital adequacy purposes, like absence of regulatory arbitrage opportunities, huge computational advantages related to subadditivity and convexity, and absence of risk paradoxes. No sound arguments have ever been given to display why  $V@R$ should be more appropriate than ES, instead. Yet, to date, ES still plays no role in the Basel II Accord (see Regulatory Capital).

#### **Mathematical Expressions for ES**

We denote with  $F_X(x) = \mathbb{P}\{X \le x\}$  the probability distribution function of  $X$  in a chosen probability space and we define for any  $p \in (0, 1)$  the lower *p*-quantile  $q_p(X) = \inf \{x \in \mathbb{R} | F_X(x) \ge p \}$  and the upper *p*-quantile  $q^p(X) = \inf \{x \in \mathbb{R} | F_X(x) > p \}.$ A (generic)  $p$ -quantile  $X_p$  is defined as any value in the interval  $[q_p(X), q^p(X)].$ 

For any  $\alpha \in (0, 1]$ ,  $ES_{\alpha}$  can then be expressed as

$$ES_{\alpha}(X) = -\frac{1}{\alpha} \int_{0}^{\alpha} X_{p} \, \mathrm{d}p \tag{1}$$

where  $X_p$  is a *p*-quantile whose choice is irrelevant, showing that there exists a unique definition for ES. For V@R, on the contrary, which is defined as  $V@R_{\alpha}(X) = -X_{\alpha}$ , this choice does indeed affect the result, leading to possible alternative different notions (upper and lower  $V@R$ , for instance) when the quantiles  $p \mapsto X_p$  turn out not to be single valued.

For the extreme case  $\alpha = 0$ , the definition is naturally extended by placing  $ES_0(X) = -\text{ess inf } X =$  $-\inf\{x\in[-\infty,+\infty]|F_X(x)>0\}$ , while for  $\alpha=1$ one easily recognizes that  $ES_1(X) = -\mathbb{E}[X]$ .

Note how equation  $(1)$  clearly expresses the fact that ES is indeed *minus the average of the*  $\alpha$  *lowest* outcomes of  $X$ .

It is important to distinguish ES from the so-called tail conditional expectation (TCE) defined as  $[5]$ 

$$TCE_{\alpha}(X) = -\mathbb{E}[X|X \le q_{\alpha}(X)]$$
 (2)

This expression can be shown to coincide with  $ES_{\alpha}(X)$  only under special conditions on the distribution function, for instance, when  $F_X(x)$  is a continuous function. However, for general distribution functions, ES and TCE differ and it is only the former, which can be shown to be subadditive  $[1, 12]$ . Equation  $(2)$  is, in any case, a useful expression for ES when one works with parametric distributions whose continuity is assumed to hold  $a$ priori.

The correction to expression  $(2)$  needed to express ES on general (noncontinuous) probability distributions is contained in the following formula  $[1]$ :

$$ES_{\alpha}(X) = -\frac{1}{\alpha} \left\{ \mathbb{E} \left[ X \mathbf{1}_{\{X \le X_{\alpha}\}} \right] - X_{\alpha}(F_X(X_{\alpha}) - \alpha) \right\}$$
(3)

where the choice of the  $\alpha$ -quantile  $X_{\alpha}$  is again irrelevant. This formula shows that  $ES_{\alpha}(X) = TCE_{\alpha}(X)$ if and only if  $F_X(X_\alpha) = \alpha$ .

ES can also be defined as the solution of a convex minimization problem [9, 11, 12]:

$$ES_{\alpha}(X) = \min_{s} \left\{-s + \frac{1}{\alpha} \mathbb{E}\left[s - X\right]^{+}\right\} \qquad (4)$$

attaining the minimum in any  $s \in [q_{\alpha}(X), q^{\alpha}(X)].$ This formulation of ES is very important because it allows to obtain fast algorithms for portfolio ESoptimization  $[11, 12]$ .

## **Properties of ES**

ES satisfies the following important properties for any  $\alpha \in [0, 1]$  and random variables X, Y [1, 7, 9]:

(i) *monotonicity* 

$$ES_{\alpha}(X) \ge ES_{\alpha}(Y)$$
 if  $X \le Y$  a.s. (5)

(ii) translational invariance

$$ES_{\alpha}(X+c) = ES_{\alpha}(X) - c \quad \text{if} \quad c \in \mathbb{R} \quad (6)$$

(iii) positive homogeneity

$$ES_{\alpha}(\lambda X) = \lambda ES_{\alpha}(X) \quad \text{if} \quad \lambda \ge 0 \quad (7)$$

(iv) *subadditivity* 

$$ES_{\alpha}(X+Y) \le ES_{\alpha}(X) + ES_{\alpha}(Y) \qquad (8)$$

Formally, these properties coincide with the axioms of coherence [5]. However, it has to be kept in mind that the concept of coherence is not just a property of a statistics of a generic random variable but a property of a portfolio statistics with a precise economic interpretation. To speak of coherence of a portfolio measure of risk, it is also necessary that the random variables  $X$  and  $Y$  in these conditions represent future "portfolio values" (as opposed to "portfolio returns"). This fact is crucial for the correct economic interpretation of condition  $(6)$  in the spirit of capital adequacy. A CMR is, in fact, supposed to decrease by the amount  $c$  when a risk-free capital of future deterministic value  $c$  (and not a portfolio yielding a deterministic return  $c$ ) is added to any portfolio  $X$ .

Hence, strictly speaking, the expected shortfall of a portfolio  $ES_{\alpha}(r_{T}^{(\pi)})$ , widely adopted by practitioners as on alternative to V@R, although monotonic, translational invariant, positive homogeneous, and subadditive with respect to its return argument, is, nevertheless, not a CMR in the sense of [5]. It is the *expected shortfall of a portfolio value*  $ES_{\alpha}(\pi_T)$ , which represents a truly CMR. The connection between the two notions is however just a constant offset, thanks to property (2).

$$ES_{\alpha}(\pi_T) = ES_{\alpha} \left( r_T^{(\pi)} \right) - (1 + R)\pi_0 \qquad (9)$$

Properties  $(5)$ – $(8)$  are, in any case, extremely important also for return-based measures, in particular for the convexity properties they induce on portfolio optimization problems. That is why some authors (e.g.,  $[3, 6]$ ) (somehow improperly) call them *axioms* of *coherence* also when referred to statistics acting on portfolio returns.

Particularly important is the subadditivity property, which V@R fails to satisfy. Inequality (8) formalizes the fact that the risk (expressed by ES) of the sum of two portfolios  $X$  and  $Y$  never exceeds the sum of their individual risks. The difference between right- and left-hand side of the inequality expresses the hedging benefit of merging the two portfolios. In a CMR this benefit is positive, and just in exceptional cases vanishing, but never negative, a situation that would give rise to paradoxes and regulatory arbitrages (see, for instance,  $[3-5]$  for a discussion).

An important immediate consequence of properties  $(7)$  and  $(8)$  is convexity.

(v) *convexity* 

$$\begin{aligned} ES_{\alpha}(\mu X + (1 - \mu)Y) \\ \le \mu ES_{\alpha}(X) + (1 - \mu)ES_{\alpha}(Y) \quad \text{if} \quad \mu \in [0, 1] \end{aligned} \tag{10}$$

which states that the risk of a blend of two portfolios is less than the blend of the individual risks. This expresses the clearest formalization of the risk diversification principle and is of utmost importance for portfolio optimization problems [3, 11, 12], because they generally turn out to be convex.

Other important properties of ES are related to the concepts of portfolio preference under first or second stochastic dominance. We recall that a random variable  $X$  is said to dominate  $Y$  according to first-order stochastic dominance (notation:  $X \stackrel{1''}{\succ} Y$  if  $F_X(z) \leq F_Y(z)$  for all  $z \in \mathbb{R}$ , while  $X$  is said to dominate  $Y$  according to secondorder stochastic dominance (notation:  $X \stackrel{2^{nd}}{\succ} Y$ ) if  $\int_{-\infty}^{z} [F_Y(t) - F_X(t)] dt \ge 0 \text{ for all } z \in \mathbb{R}. \text{ First order}$ implies second-order stochastic dominance. It can be shown  $[7-9]$  that ES is compatible with both these preferences.

### (vi) *monotonicity with respect to first- and second*order stochastic dominance

$$ES_{\alpha}(X) \le ES_{\alpha}(Y) \quad \text{if} \quad X \stackrel{1^{s_{1}},2^{na}}{\succ} Y \quad (11)$$

which tells us that if a portfolio  $X$  is preferable to  $Y$  under either first- or second-order stochastic dominance, its ES will be smaller.

Furthermore, one can show comonotonic additivity [7, 8].

(vii) *comonotonic additivity* 

$$ES_{\alpha}(X + Y) = ES_{\alpha}(X) + ES_{\alpha}(Y) \quad \text{if}$$
  
X, Y comonotonic (12)

Comonotonic additivity represents the limiting case of subadditivity, achieved when two random variables happen to be comonotonic and therefore ineffective to hedge each other. It is in this case that the hedging benefit of subadditivity is expected to vanish. Comonotonic additivity is not implied by the axioms of coherence and this is sometimes argued to be a weakness of the axioms, because noncomonotonic additive CMRs can give rise to capital regulatory arbitrages [4].

Furthermore, ES belongs to the class of lawinvariant, comonotonic additive CMRs [8], also known as spectral measures of risk (SMRs) [2] (see Spectral Measures of Risk). Actually, the set  $\{ES_{\alpha} | \alpha \in [0, 1]\}$  of all possible ES is the smallest set whose convex hull corresponds to the class of SMRs. In other words, any SMR can be uniquely expressed as a convex combination of ESs [8].

Law-invariance plays a special role as the distinguishing property of the CMRs, which may be estimated from data sets.

## **Estimation of ES**

A number of cases are known where exact expressions of ES can be computed directly from equation (1) by direct calculation (analytical or numerical) knowing the distribution of  $X$ . However, in general cases, and in particular when parametric distributions are not assumed *a priori* like in many risk management platforms, ES is obtained by estimation.

Given a sample of  $N$  independent and identically distributed outcomes  $x_i$ , of a random variable X, a consistent estimator of  $ES_{\alpha}(X)$  can be obtained by  $[1, 3]$ 

$$\widehat{ES}_{\alpha}(X) = -\frac{1}{N\alpha} \left( \sum_{i=1}^{\lfloor N\alpha \rfloor} x_{i:N} + (N\alpha - \lfloor N\alpha \rfloor) x_{\lfloor N\alpha \rfloor + 1:N} \right)$$
$$= \frac{1}{\lfloor N\alpha \rfloor} \sum_{i=1}^{\lfloor N\alpha \rfloor} x_{i:N} + o(1/N) \qquad (13)$$

where  $[n]$  denotes the integer part of *n* and  $x_{i:N}$ denotes the ordered statistics, that is, the vector  $\{x_{i:N}\}_{i=1,...,N}$  of values  $x_{1:N} \leq \cdots \leq x_{N:N}$  obtained sorting the vector  $\{x_i\}_{i=1,\dots,N}$ . This expression converges to  $ES_{\alpha}(X)$  for  $N \to \infty$ . It can be shown to

be nothing but the ES of the empirical distribution of the sample, and as such, it is clearly coherent for any finite *N*.

In equation (13) the *o(*1*/N )* term can be neglected for simplicity in those applications where *N* is large like some Monte Carlo simulations, but it is not at all negligible, for instance, in a historical simulation of *N* = 252 data, with a confidence level of say, 5%. In general, it is always safer, and not computationally penalizing, to adopt the complete estimator.

An equivalent expression [11, 12] can be obtained by exploiting equation (4):

$$\widehat{ES}_{\alpha}(X) = \min_{s} \left\{ -s + \frac{1}{N\alpha} \sum_{i=1}^{N} \left[ s - x_i \right]^+ \right\} \quad (14)$$

which has the solution *s* ∈ [*xNα , xNα*<sup>+</sup>1]. From a computational point of view, there may be cases where the cost of minimization of equation (14) is smaller than the cost of the sorting procedure needed for equation (13). These formulas are essential tools for any risk management application based on exact Monte Carlo or historical simulation.

## **References**

- [1] Acerbi, C., Tasche, D. (2002). On the coherence of expected shortfall, *Journal of Banking and Finance* **26**, 1487–1503.
- [2] Acerbi, C. (2002). Spectral measures of risk: a coherent representation of subjective risk aversion, *Journal of Banking and Finance* **26**, 1505–1518.

- [3] Acerbi, C. (2004). Coherent representations of subjective risk aversion, in *Risk Measures for the 21st Century*, G. Szego, ed., Wiley & Sons, pp. 147–207.
- [4] Acerbi, C. (2007). Coherent measures of risk in everyday market practice, *Quantitative Finance* **7**(4), 359–364.
- [5] Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D. (1999). Coherent measures of risk, *Mathematical Finance* **9**(3), 203–228.
- [6] Embrechts, P., Frey, R. & McNeil, A.J. (2005). *Quantitative Risk Management*, Princeton University Press.
- [7] Follmer, H. & Schied, A. (2004). ¨ *Stochastic Finance*, 2nd Edition, de Gruyter.
- [8] Kusuoka, S. (2001). On law invariant coherent risk measures, *Advances in Mathematical Economics* **3**, 83–95.
- [9] Pflug, G. (2000). Some remarks on the value-atrisk and the conditional value-at-risk, in *Probabilistic Constrained Optimization: Methodology and Applications*, S. Uryasev, ed., Kluwer Academic Publishers, pp. 278–287.
- [10] Rappoport, P. (1993). *A New Approach: Average Shortfall* J.P. Morgan, Fixed Income Research. (44–71) pp. 325–399.
- [11] Rockafellar, R.T. & Uryasev, S. (2000). Optimization of conditional value-at-risk, *Journal of Risk* **2**(3), 21–42.
- [12] Rockafellar, R.T. & Uryasev, S. (2001). Conditional value-at-risk for general loss distributions, *Journal of Banking and Finance* **26**, 1443–1471.

## **Related Articles**

**Convex Risk Measures**; **Spectral Measures of Risk**; **Value-at-Risk**.

CARLO ACERBI
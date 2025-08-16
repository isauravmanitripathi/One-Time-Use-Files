# **Actuarial Premium** Principles

An actuarial premium principle is a method for assigning an appropriate price for an insurance policy. This price is the amount that has to be paid by the insured for exchanging "risk" with "certainty." The agreed premium represents an equilibrium between the parties involved. In fact, individual agents look at the price they are willing to pay for hedging (partially or totally) their risks, whereas insurers take into account how much premium they should charge in order to avoid technical ruin and to guarantee the rentability of the underlying insurance portfolio. Premium principles deal with the analysis and the characterization of such equilibrium.

In the first section, we introduce basic notions, an axiomatic characterization, and a review of premium principles. Next, an economic method to interpret the relation between premium principles and market systems is described. Then, we present a unified approach based on a generalized Markov inequality for tail probabilities and show how several types of premium principles can be derived from it.

In the last section, we consider the analysis of insurance portfolios (i.e., collections of insurance contracts) traded in financial markets. In this case, portfolios are transferred either from an insurer to another insurer or from an insurer to the market (see **Securitization**). We devote the last paragraph to the analysis of pricing such portfolios.

In this article, we focus on the main aspects of the theory of premium principles. Topics that are not covered include insurer profitability and solvency requirements (*see* **Solvency**).

Notice that in the recent literature, premium principles are often considered as akin to risk measures (see Convex Risk Measures; Value-at-Risk; Expected Shortfall; Spectral Measures of Risk).

# The Axiomatic Characterization of Premium Principles

Classes of premium principles may be derived from sets of axioms. The introduction of such axioms is not an arbitrary or dogmatic approach but rather an essential step for defining the properties a premium principle has to satisfy. Indeed, in case a set of axioms proposed does not suit a certain intuition of insurance risk, we could modify it properly. In this way, it is possible to justify an axiomatic characterization by showing its strengths or to criticize it by demonstrating its lack of practical importance.

The analysis of premium principles using an axiomatic characterization was introduced in the actuarial context in [20].

Let us consider a probability space  $(\Omega, F)$ , where  $\Omega$  is the set of the scenarios equipped with a  $\sigma$ -algebra F. A risk is a random variable defined on  $(\Omega, F)$ , that is,  $X : \Omega \to \mathbb{R}$  is a risk if  $X^{-1}((-\infty,x]) \in F$  for all  $x \in \mathbb{R}$ . When X takes only positive values, that is,  $X > 0$ , we call it a *risk*. The class of all random variables on  $(\Omega, F)$  is denoted by **W**. We equip the measurable space with a probability measure  $P$ , which we call the *base prob*ability measure.

A premium principle  $\pi$  is a functional that assigns a real number to any random variable  $X$  in  $W$ .

The above definition may be extended to the case where risks are noninsurable, that is, when  $\pi[X] =$  $+\infty$ .

In the following, we introduce some axioms and properties a premium principles may (or may not) satisfy. All random variables are assumed to be elements of the set  $\mathbf{W}$  introduced above.

*Monotonicity*:  $\pi$  is monotonic if  $\pi[Y] \leq \pi[X]$ when  $Y(\omega) < X(\omega)$  for all  $\omega \in \Omega$ .  $\pi$  is *P*-monotonic if  $\pi[Y] \leq \pi[X]$  when  $Y \leq X$ , *P*-almost sure.

Positive homogeneity (scale invariance, scale *equivariance*):  $\pi$  is positively homogeneous if  $\pi[aX] = a\pi[X]$  for all  $a > 0$ .

Translation invariance (translation equivariance, *translativity, consistency*):  $\pi$  is translation invariant if  $\pi[X + c] = \pi[X] + c$  for all real c.

Subadditivity:  $\pi$  is subadditive if  $\pi[X+Y] <$  $\pi[X] + \pi[Y]$ . If the inequality is reversed, then the property is called *superadditivity*.

Additivity for independent risks:  $\pi$  is additive if  $\pi[X+Y] = \pi[X] + \pi[Y]$  for independent X,  $Y \in \mathbf{W}$ .

Comonotonic additivity:  $\pi$  is comonotonic additive (see Copulas in Insurance) if  $\pi[X+Y] =$  $\pi[X] + \pi[Y]$  whenever X and Y are comonotonic.

See [17, 23] for a review of independent and comonotonic additive premium principles and [10, 11] for an introduction to comonotonicity.

For taking in account violations of the axioms of subadditivity and positive homogeneity due to liquidity risk (see Liquidity Premium), it is possible to replace these two with the requirement by convexity. The interested reader is referred to  $[1, 16, 22]$ and Convex Risk Measures and also to [12].

Convexity:  $\pi$  is convex if  $\pi[aX + (1-a)Y] \leq$  $a\pi[X] + (1-a)\pi[Y]$  for all  $a \in (0, 1)$ .

Law-invariance:  $\pi$  is law invariant if  $\pi[X] =$  $\pi[Y]$  in case  $X \stackrel{d}{=} Y$ .

Preserving stop-loss order:  $\pi$  preserves stop-loss order if  $\pi[X] \leq \pi[Y]$  when  $E[(X-d)_+] \leq E[(Y$  $d_{+}$  for all  $d \in \mathbb{R}$ .

Preserving first-order stochastic dominance (*FOSD*):  $\pi$  preserves first-order stochastic dominance if  $\pi[X] \leq \pi[Y]$  when  $P[X \leq x] \geq P[Y \leq x]$  for all  $x \in \mathbb{R}$ .

These two properties are closely linked to each other. Indeed, the latter is a direct consequence of the former. For a review on the applications of stop-loss and stochastic ordering in actuarial science, see [9].

Positive risk loading:  $\pi$  induces a risk loading if  $\pi[X] > E[X]$ .

Having a positive risk loading is a suitable property because without it an insurer will make a loss in the long run. We will see the relevance of this property comparing the net and the expected value principle.

*No rip-off* (*maximal loss*):  $\pi[X] \leq ess \sup[X]$ . *Not unjustified:*  $\pi$  is not unjustified if  $\pi[X] = c$ , when  $X \in \mathbf{W}$  is equal to  $c \ge 0$  almost everywhere.

#### **Premium Principles: A Review**

In this section, we introduce several premium principles as well as their relevant properties. We also give the definition of the Dutch premium calculation principle.

Note that all the following premium principles implicitly assume the existence of a given utility function (see Utility Theory: Historical Perspectives; Utility Function). For an analysis of expected utility theory and subjective expected utility theory, the interested reader is referred to [29, 35]. For more applications of the theory of choice under uncertainty and the utility framework within actuarial science, we refer to [7].

*Expected value principle*: The expected value principle is given as

$$\pi[X] = (1 + \alpha)E[X] \tag{1}$$

where  $\alpha \in \mathbb{R}$ . In case  $\alpha = 0$  we find the net premium that does not load for risk. This principle is justified by the strong law of large numbers (SLLN). Given that the risk  $X = \sum_{i=1}^{n} X_i$  is linked to a large homogeneous portfolio, let us suppose that  $X_i$  are independent and identically distributed (i.i.d.) and their first moment exists and is finite,  $E[X_i] = \mu <$  $\infty$ , for  $i = 1, 2, \ldots$  Thus, from the SLLN, we find that

$$\lim_{n \to \infty} P[|n^{-1}X - \mu| < \varepsilon] = 1 \tag{2}$$

for all  $\varepsilon > 0$ .

The net premium principle is appropriate only in case insurers are risk-neutral. Indeed from the ruin theory (see **Ruin Theory**), it is known that ruin will inevitably occur whenever there is no loading.

Equivalent utility principle: The equivalent utility premium is obtained for the premium that makes the expected utility of the income  $\pi[X] - X$  of the insurer equal to the utility of not accepting the risk. We could assume that the utility function is subjective and the probability measure objective, if we choose the framework introduced in [35]. Otherwise, following the results in  $[29]$ , the probability measure is also considered to be subjective and not known.

The minimal premium,  $\pi^{-}[X]$ , and the maximal premium,  $\pi^+[X]$ , are derived by solving

$$E[u(w + \pi[X] - X)] = u(w) \tag{3}$$

and

$$E[\overline{u}(\overline{w} - X)] = \overline{u}(\overline{w} - \pi[X]) \tag{4}$$

respectively, where  $X$  is a positive random variable, w a real number, and  $\overline{u}$  denotes the utility function of the insured and  $u$  the one of the insurer.

Thus, the insurer will sell the insurance contract if and only if  $\pi[X] > \pi^{-}[X]$ , whereas the insured will buy it when  $\pi[X] \leq \pi^+[X]$ . Hence, the equilibrium price lies in the interval

$$[\pi^{-}[X], \pi^{+}[X]]$$

In case both the insurer and the insured are riskaverse (see Risk Aversion), it follows that

$$E[X] \le \pi^{-}[X] \le \pi^{+}[X] \tag{5}$$

Different specifications of the utility function yield different expressions  $\pi^{-}[X]$  and  $\pi^{+}[X]$ . It is not guaranteed that an explicit expression for  $\pi^{-}[X]$  or  $\pi^+[X]$  is obtained.

As a final remark, the difference  $\pi^+[X] - \pi^-[X]$ denotes the mark-up price. It is maximum in the case of insurer's monopoly, whereas in a competitive insurance market it tends to zero.

*Distortion principle*: The distortion principle as a premium principle was introduced in [36, 37] and it can be seen as an attempt to overcome some of the shortcomings of the expected utility theory. Indeed as a consequence of the Allais paradox [3], some nonexpected utility theories were proposed. The distortion principle refers to Yaari's dual theory [38]. Yaari showed that the amount of money  $\pi(v)$ (certainty equivalent) that makes it indifferent to hold the lottery V or to receive the amount  $\pi(v)$  with certainty is given as

$$\pi(v) = -\int_{-\infty}^{0} (1 - g(\overline{F}_V(v))) \mathrm{d}v + \int_{0}^{+\infty} g(\overline{F}_V(v)) \mathrm{d}v \tag{6}$$

where  $\overline{F}_V(v) = 1 - P[V \le v]$ . The function g:  $[0, 1] \rightarrow [0, 1]$  is known as distortion function and it is nondecreasing and it fulfills  $g(0) = 0$  and  $g(1) = 1.$ 

Using the distorted distribution function  $F_g^*(x) =$  $1 - g(\overline{F}_V(x))$  together with equation (6), we get that  $\pi(v) = \int_{-\infty}^{+\infty} x dF_g^*(x)$ .

For an overview on distortion risk measures, the reader is referred to  $[9, 13]$ .

Proportional hazard (PH) principle: The PH principle arises as a special case of the distortion principle<br>when  $\overline{g}(x) = x^{1/\alpha}$ ,  $\alpha \ge 1$ , and it is given as

$$\pi[X] = -\int_{-\infty}^{0} \left(1 - (\overline{F}_X(x))^{1/\alpha}\right) \mathrm{d}x$$
$$+ \int_{0}^{+\infty} \left( (\overline{F}_X(x))^{1/\alpha} \right) \mathrm{d}x \tag{7}$$

See  $[36]$  for a review of the properties of this premium principle.

*Mean value principle*: The mean value principle arises as the root  $\pi$  of the following equation:

$$f(\pi) = E[f(x)] \tag{8}$$

where  $f$  is a nondecreasing and nonnegative function defined on  $\Re$ .

*Variance principle*: For some  $\alpha > 0$ , the variance principle is given as

$$f(\pi) = E[X] + \alpha \text{Var}[X] \tag{9}$$

*Standard deviation principle*: For some  $\alpha > 0$ , the standard deviation principle is given as

$$f(\pi) = E[X] + \alpha \sqrt{\text{Var}[X]} \tag{10}$$

The last two principles are built on the expected value by including a risk loading that is proportional to the variance or the standard deviation of the risk. Denneberg [8] suggested to replace the standard deviation with the absolute deviation. See [27, 30] for a generalization of the variance and standard deviation principles to the dynamic case.

*Exponential principle*: The exponential principle is given as

$$\pi[X] = \frac{1}{\alpha} \log E[\exp(aX)] \tag{11}$$

where  $\alpha > 0$ . The exponential principle represents a special case of the equivalent utility principle in the case of an exponential utility function; see  $[17,$ 23, 26].

*Esscher principle*: The Esscher premium is given as

$$\pi[X] = \frac{E[Xe^{aX}]}{E[e^{aX}]} \tag{12}$$

where  $\alpha > 0$ . This premium is based on the notion of Esscher transform (see Esscher Transform), introduced by Esscher [15]. Let us consider a random variable X and a positive real number  $\alpha$  such that  $E[e^{aX}] < \infty$ ; one considers a transformed distribution function:

$$F_{\tilde{X}}(x) = \int_0^x \frac{e^{\alpha X}}{E[e^{\alpha X}]} dF_X(x) \tag{13}$$

In this way, we obtain the Esscher measure that is mutually absolute continuous, that is, equivalent (see Equivalence of Probability Measures), with respect to the original probability measure. For a review of the characterizations of Esscher principle, we refer to  $[32]$ . In the last paragraph, we demonstrate the importance of Esscher transform in an insurance pricing framework.

*Swiss principle*: The Swiss premium  $\pi$  is the root of the following equation in  $\pi$ :

$$E[w(W - p\pi)] = w((1 - p)\pi) \tag{14}$$

| Principle           | M            | $\text{PH}$ | TI | SAd | $\text{Ad}$ | IAd | CAd | С | SL           | NR           | RL |
|---------------------|--------------|-------------|----|-----|-------------|-----|-----|---|--------------|--------------|----|
| Expected Value      | $\mathbf{v}$ | Y           | N  | Y   | Y           | Y   | Y   | Y | v            | N            | Y  |
| Equivalent utility  | $\mathbf{v}$ | N           | Y  | N   | N           | N   | N   | N | v            | Y            | Y  |
| Distortion          | $\mathbf{v}$ | Y           | Y  | Y   | N           | N   | Y   | Y | v            | Y            |    |
| Proportional Hazard | Y            | Y           | Y  | Y   | N           | N   | Y   | Y | v            | Y            |    |
| Mean value          | Y            | N           | Y  | N   | N           | N   | N   | N | Y            | Y            |    |
| Variance            | N            | N           | Y  | N   | N           | Y   | N   | N | N            | N            | Y  |
| Standard Deviation  | N            | Y           | Y  | Y   | N           | N   | N   | Y | N            | N            | Y  |
| Exponential         | $\mathbf{v}$ | N           | Y  | N   | N           | Y   | N   | N | Y            | Y            | Y  |
| Esscher             | N            | N           | Y  | N   | N           | Y   | N   | N | N            | $\mathbf{v}$ |    |
| Swiss               |              | N           | N  | N   | N           | N   | N   | N | $\mathbf{v}$ | $\mathbf{v}$ |    |
| Dutch               |              | Y           | N  | Y   | N           | N   | N   | Y | v            | $\mathbf{v}$ |    |
| Orlicz              |              | Y           | N  | Y   | N           | N   | N   | v | v            | Y            | Y  |

Table 1 All premiums mentioned above are law invariant. All principles are not unjustified except the expected value principle for  $\alpha > 0$ 

M, monotonicity; PH, positive homogeneity; TI, translation invariance; SAd, subadditivity; Ad, additivity; IAd, independent additivity; Cad, comonotonic additivity; C, convexity; SL, stop-loss order; NR, no rip-off; RL, risk loading

for a nonnegative and nondecreasing function  $w$ defined on  $\Re$  and a given parameter  $0 < p < 1$ .

Both the equivalent utility principle and the mean value principle can be obtained as particular cases of the Swiss premium principle; see [20].

*Dutch principle*: The Dutch principle is given as

$$\pi[X] = E[X] + \theta E[(X - \alpha E[X])_+],$$
  
$$\alpha \ge 1, \quad 0 < \theta \le 1 \tag{15}$$

The Dutch premium principle was introduced in [31].

*Orlicz principle*: The Orlicz principle is given by the root of

$$E[\psi(X/\pi)] = 1\tag{16}$$

where  $X > 0$  and  $\psi$  is a normalized Young function on  $\Re_+ \cup \{0\}$ . This premium reflects a change in risk in a proportional change in premium (Table 1).

#### The Economic Method

In 1980, Bühlmann derived the economic premium principle in contrast to classical premium principles that depend only on the risk to be covered; see [4]. He took into account general market conditions and proposed a premium principle based on economic arguments. In this way, the economic premium principle is a function that associates with a random variable  $X$  representing insurance risk and a random variable Z denoting market risk  $\pi$ , that is,  $\n\pi: (X, Z) \to \mathbb{R}.\n$ 

Let consider a market with  $n$  insurer agents. We suppose that the insurer *i* bears risk  $X_i$ ,  $i =$  $1, 2, \ldots, n$ , and that his/her risk aversion is characterized by the exponential utility function  $u_i(x) =$  $\frac{1}{\alpha_i}(1 - e^{(-\alpha_i x)})$ . Bühlmann obtained the following  $\mathbf{r}$  expression for the equilibrium pricing density for the risk  $X$ :

$$\pi[X,Z] = \frac{E[Xe^{\alpha Z}]}{E[e^{\alpha Z}]} \tag{17}$$

that is, the Esscher premium; see [4]. Moreover, it can be considered as a Pareto optimal risk exchange. In the case where  $X$  and  $Z - X$  are independent to each other, we derive the standard premium principle:

$$\pi[X, Z] = \frac{E[Xe^{\alpha X}]E[Xe^{\alpha(Z-X)}]}{E[e^{\alpha X}]E[e^{\alpha(Z-X)}]}$$
$$= \frac{E[Xe^{\alpha Z}]}{E[e^{\alpha Z}]} = \pi[X] \tag{18}$$

Bühlmann derived the above result using the concept of a pricing density (pricing kernel and state price deflator). The interested reader is referred to [28].

Bühlmann generalized this result in [5], allowing for insurers with general utility functions. For an extension of the above model to the dynamic multiperiod case, see [25].

| Premium principle  | υ(x) | φ(x, π )                  |
|--------------------|------|---------------------------|
| Mean value         | 1    | f (x)<br>f (π )           |
| Equivalent utility | 1    | u(π − x)<br>u(0)          |
| Swiss              | 1    | ω(x − pπ)<br>ω((1 − p)π ) |
| Orlicz             | 1    | ψ(x/π )                   |

**Table 2** Premium principles derived from the generalized Markov inequality

# **A Unified Approach by Markov Inequality for Tail Probabilities and VaR**

A unified approach for generating premium principles based on the Markov inequality of tail probabilities has been introduced in [21]. Indeed, using two exogenous functions *υ(*·*)* and *φ(*·*,* ·*)* (Table 2), an exogenous parameter *α* ≤ 1, and assuming that *υ(*·*)* is both nonnegative and nondecreasing and fulfills *φ(x, π )* ≥ 1{*x>π*}, where 1{*x>π*} = 1 if *x>π* 0 if *x<π* , then by the generalized Markov inequality we find that

$$P[X > \pi] \le \frac{E[\phi(X,\pi)\upsilon(X)]}{E[\upsilon(X)]} \tag{19}$$

Focusing on the upper bound of the above equation, if it is set to the confidence level *α* ≤ 1, we have that

$$P[X > \pi] \le \frac{E[\phi(X,\pi)\upsilon(X)]}{E[\upsilon(X)]} = \alpha \le 1 \qquad (20)$$

When *α* = 1, equation (21) can be used for generating several well-known premium principles:

$$\frac{E[\phi(X,\pi)\upsilon(X)]}{E[\upsilon(X)]} = 1\tag{21}$$

It should be remarked that this unified approach is also directly linked to the quantile-based approach. Indeed, for all *φ*, *υ*, using the results shown above, we find that *π* ≥ inf{*x* ∈ - : *P*[*X* ≤ *x*] ≥ 1 − *α*}; see [20].

# **Insurance Pricing**

This section is devoted to the analysis of insurance portfolios (i.e., collections of insurance contracts) traded in financial markets.

Although traditional actuarial pricing of insurance relies on economic theory of decision under uncertainty, financial pricing of contingent claims mainly relies on risk-neutral valuation, which can be justified within a no-arbitrage setting (*see* **Arbitrage: Historical Perspectives**; **Arbitrage Pricing Theory**). Even if this assumption may seem unrealistic in the case of traditional insurance markets, it is suitable for insurance products traded on financial markets; see [2, 7, 33, 34]. Moreover, owing to the incompleteness of insurance markets, we will observe an infinite number of equivalent martingale measures (*see* **Equivalence of Probability Measures**; **Martingales**) and hence an uncountable set of possible prices.

Insurance prices can be derived by means of the Esscher transform, as suggested by Gerber and Shiu [18, 19]. These authors defined the Esscher transform for exponential Levy processes ( ´ *see* **Levy Processes ´** ), that is, processes with independent and stationary increments. Under the Esscher transform probability measure, it is possible to establish a change of measure for a random variable. Choosing suitable Esscher parameters, discounted prices become martingales and thus no-arbitrage prices can be calculated. In the case where equivalent martingale measure is unique, it is derived by the Esscher transform. Otherwise, if it is not unique, as is usual in the case of insurance markets, the equivalent martingale measure can be derived by the Esscher transform assuming the existence of a representative agent that maximizes its expected utility to a power utility function.

The interested reader is referred to [6, 14, 24] for a review of recent developments in this topic.

# **Acknowledgments**

The authors acknowledge the financial support of the Onderzoeksfond K.U. Leuven (GOA 2007–2011: Risk modeling and valuation of insurance and financial cash flows, with applications to pricing, provisioning, and solvency). Jan Dhaene and Marc Goovaerts also thank the financial support of Fortis (K.U. Leuven Fortis Chair in Financial and Actuarial Risk Management).

# **References**

- [1] Acerbi, C. & Scandolo, G. (2008). Liquidity and coherent risk measures, *Quantitative Finance* forthcoming.
- [2] Albrecht, P. (1992). Premium calculation without arbitrage? A note on a contribution by G. Venter, *Astin Bulletin* **22**, 247–254.

# **6 Actuarial Premium Principles**

- [3] Allais, M. (1953). Le comportement de l'homme rationnel devant le risque: critique des postulates t axiomes de l' ecole Am ´ ericaine, ´ *Econometrica* **21**, 503–546.
- [4] Buhlmann, H. (1980). An economic premium principle, ¨ *Astin Bulletin* **14**, 13–22.
- [5] Buhlmann, H. (1984). The general economic premium ¨ principle, *Astin Bulletin* **14**, 89–101.
- [6] Buhlmann, H., Delbaen, F., Embrechts, P. & Shirayev, ¨ A.N. (1996). No arbitrage, change of measure and conditional Esscher transforms, *CWI Quarterly* **9**, 291–317.
- [7] Delbaen, F. & Haezendonck, J. (1989). A martingale approach to premium calculation principles in an arbitrage free market, *Insurance: Mathematics and Economics* **8**, 269–277.
- [8] Dennenberg, D. (1990). Premium calculation: why standard deviation should be replaced by absolute deviation, *Astin Bulletin* **20**, 181–190.
- [9] Denuit, M., Dhaene, J., Goovaerts, M.J. & Kaas, R. (2005). *Actuarial Theory for Dependent Risks*, Wiley, New York.
- [10] Dhaene, J., Denuit, M., Goovaerts, M.J., Kaas, R. & Vyncke, D. (2002). The concept of comonotonicity in actuarial science and finance: theory, *Insurance: Mathematics and Economics* **31**, 3–33.
- [11] Dhaene, J., Denuit, M., Goovaerts, M.J., Kaas, R. & Vyncke, D. (2002). The concept of comonotonicity in actuarial science and finance: applications, *Insurance: Mathematics and Economics* **31**, 133–161.
- [12] Dhaene, J., Laeven, R.J.A, Vanduffel, S., Darkiewicz, G. & Goovaerts, M.J. (2008). Can a coherent risk measure be too subadditive? *Journal of Risk and Insurance* **75**, 365–386.
- [13] Dhaene, J., Vanduffel, S., Tang, Q., Goovaerts, M.J., Kaas, R. & Vyncke, D. (2006). Risk measures and comonotonicity: a review, *Stochastic Models* **22**, 573–606.
- [14] Embrechts, P. (2000). Actuarial versus financial pricing of insurance, *Risk Finance* **1**, 17–26.
- [15] Esscher, F. (1932). On the probability function in the collective theory of risk, *Scandinavian Actuarial Journal* **15**, 175–195.
- [16] Follmer, H. & Schied, A. (2002). Convex measures of risk and trading constraints, *Finance and Stochastics* **6**, 429–447.
- [17] Gerber, H.U. (1974). On additive premium calculations principles, *Astin Bulletin* **7**, 215–222.
- [18] Gerber, H.U. & Shiu, S.W.E. (1994). Option pricing by Esscher transform, *Transactions of the Societies of Actuaries* **46**, 99–191.
- [19] Gerber, H.U. & Shiu, S.W.E. (1996). Actuarial bridges to dynamic hedging and option pricing, *Insurance: Mathematics and Economics* **18**, 183–218.
- [20] Goovaerts, M.J., De Vylder, F.E.C. & Haezendonck, J. (1984). *Insurance Premiums*, North Holland Publishing, Amsterdam.

- [21] Goovaerts, M.J., Kaas, R., Dhaene, J. & Tang, Q. (2003). A unified approach to generate risk measures, *Astin Bulletin* **33**, 173–191.
- [22] Goovaerts, M.J., Kaas, R., Dhaene, J. & Tang, Q. (2004). Some new classes of consistent risk measures, *Insurance: Mathematics and Economics* **34**, 505–516.
- [23] Goovaerts, M.J., Kaas, R., Dhaene, J., Laeven, R.J.A. & Tang, Q. (2004). A comonotonic image of independence for additive risk measures, *Insurance: Mathematics and Economics* **35**, 581–594.
- [24] Goovaerts, M.J. & Laeven, R.J.A. (2008). Actuarial risk measures for financial derivative pricing, *Insurance: Mathematics and Economics* **42**, 540–547.
- [25] Iwaki, H., Kijima, M. & Morimoto, Y. (2001). An economic premium principle in a multiperiod economy, *Insurance: Mathematics and Economics* **28**, 325–339.
- [26] Kaas, R., Goovaerts, M.J., Dhaene, J. & Denuit, M. (2001). *Modern Actuarial Risk Theory*, Kluwer Academic Publishers, Amsterdam.
- [27] Møller, T. (2001). On transformations of actuarial valuation principles, *Insurance: Mathematics and Economics* **28**, 281–303.
- [28] Rubinstein, M. (1976). The valuation of uncertain income and the pricing of options, *The RAND Corporation* **7**, 407–425.
- [29] Savage, L.J. (1954). *The Foundations of Statistics*, Wiley, New York.
- [30] Schweizer, M. (2001). From actuarial to financial valuation principles, *Insurance: Mathematics and Economics* **28**, 31–47.
- [31] Van Heerwaarden, A.E. & Kaas, R. (1992). The Dutch premium principle, *Insurance: Mathematics and Economics* **11**, 129–133.
- [32] Van Heerwaarden, A.E., Kaas, R. & Goovaerts, M.J. (1989). Properties of the Esscher premium calculation principle, *Insurance: Mathematics and Economics* **8**, 261–267.
- [33] Venter, G.G. (1991). Premium calculation implications without arbitrage, *Astin Bulletin* **21**, 223–230.
- [34] Venter, G.G. (1992). Premium calculation implications without arbitrage Authors reply on the note by P. Albrecht, *Astin Bulletin* **22**, 255–256.
- [35] Von Neumann, J. & Morgenstern, O. (1947). *Theory of Games and Economic Behavior*. Princeton university Press, Princeton.
- [36] Wang, S.S. (1996). Premium calculation by transforming the layer premium density, *Astin Bulletin* **26**, 71–92.
- [37] Wang, S.S., Young, V.R. & Panjer, H.H. (1997). Axiomatic characterization of insurance prices, *Insurance: Mathematics and Economics* **21**, 173–183.
- [38] Yaari, M.E. (1987). The dual theory of choice under risk, *Econometrica* **55**, 95–115.

MARC J. GOOVAERTS, JAN DHAENE & OMAR RACHEDI
# **Entropy-based Estimation**

Let P,  $\mu$  be two probability measures on a probability space, with  $P$  absolutely continuous with respect to  $\mu$  (see Equivalence of Probability Measures), and denote the density of P with respect to  $\mu$  by  $dP/d\mu > 0$ . The relative entropy  $D(P||\mu)$ , sometimes called the *Kullback-Leibler information* [9] or divergence in statistics, is defined as

$$D(P \|\mu) = \int_{\Omega} \log \left(\frac{\mathrm{d}P}{\mathrm{d}\mu}\right) \mathrm{d}P$$
$$= \int_{\Omega} \frac{\mathrm{d}P}{\mathrm{d}\mu} \log \left(\frac{\mathrm{d}P}{\mathrm{d}\mu}\right) \mathrm{d}\mu \tag{1}$$

Jensen's inequality can be used to show  $D(P||\mu) > 0$ and  $D(P\|\mu) = 0$  if and only if  $P \equiv \mu$ .  $D(P\|\mu)$ is thus an (asymmetric) index of the discrepancy between P and  $\mu$ , and its definition is grounded in information theory and statistical mechanics. When  $P = (P_1, ..., P_H)$  and  $\mu = (\mu_1, ..., \mu_H)$ are probability measures on a discrete set with  $H$  elements,  $D(P\|\mu) = \sum_{h=1}^{H} P_h \log\left(\frac{P_h}{\mu_h}\right)$ . In the special case where  $\mu_h \equiv 1/H$  is the uniform distribution,  $D(P\|\mu)$  is the Shannon entropy  $-\sum_h P_h \log P_h.$ 

# **Estimation by Entropy Minimization** under Constraints

Let x denote a (vector) of random variable(s),  $\beta$ a (vector) of parameter(s), and  $f(x, \beta)$  a (column vector) of real-valued function(s). Let  $E_P[f(x, \beta)]$ denote its expectation computed with probability measure P. For a specific value of  $\beta$ , define the set of probability measures:

$$\mathcal{P}(\beta) \equiv \{P : E_P[f(x,\beta)] = 0\} \tag{2}$$

which additionally are absolutely continuous with respect to a distinguished measure  $\mu$  that is determined by the application. Selection of a particular probability measure in  $\mathcal{P}(\beta)$  is an example of *lin*ear inverse problem. One way to select a solution in stable manner is by picking the probability measure,

which minimizes the relative entropy with respect to  $\mu$  under constraints

$$\begin{aligned} & \min_{P \in \mathcal{P}(\beta)} D(P \| \mu) \\ & \equiv \min_{P} \int \log(\mathrm{d}P/d\mu) \, \mathrm{d}P \ \ s.t. \ E_{P}[f(x, \beta)] \\ & = 0 \end{aligned} \tag{3}$$

When  $\mu$  is the uniform distribution on a finite set with H elements,  $\mu_h \equiv 1/H$  and the constrained minimization of  $D(P||\mu)$  is equivalent to maximization of the Shannon entropy  $-\sum_h P_h \log P_h$ .

The solution to equation  $(3)$  is well known ([10],  $sec.3(A)$ ) to have the following *Gibbs Canonical* or Esscher Transformed density (see Esscher Transform)

$$\frac{\mathrm{d}P(\beta)}{\mathrm{d}\mu} = \frac{\mathrm{e}^{\gamma(\beta)'f(x,\beta)}}{E_{\mu}[\mathrm{e}^{\gamma(\beta)'f(x,\beta)}]} \tag{4}$$

To compute the coefficient vector  $\gamma(\beta)$  in equation  $(4)$ , solve the following problem

$$\gamma(\beta) = \arg\max_{\gamma} I \equiv -\log E_{\mu}[\mathrm{e}^{\gamma' f(x,\beta)}] \quad (5)$$

where the maximized value of  $I$  in equation (5) turns out to be the minimal relative entropy  $D(P(\beta) \| \mu)$ in equation (3). This constrained minimum of relative entropy also has a frequentist interpretation from the large deviations (see **Large Deviations**) theory of IID processes, which will prove useful in motivating the parameter estimation procedure described later.

# **Application to Derivative Security** Valuation

Consider the simplest problem of option pricing: value a European call option, written on a single underlying stock that pays no dividends, whose price at expiration T-periods ahead is denoted  $x(T)$ . The riskless, continuously compounded gross interest rate  $r$  is constant between now and expiration. Under the familiar assumptions of complete and frictionless markets that do not admit arbitrage opportunities, there is a *risk-neutral* probability measure  $P$  under which the call option's price  $C$  is the expected value of its risklessly discounted payoff at expiration, that is,

$$C = E_P[\max[x(T) - K, 0]/r^T] \tag{6}$$

where the risk-neutral probabilities  $P$  satisfy the *"martingale"* constraint  $x(0) = E_P \left[ \frac{x(T)}{T} \right]$ , rewritten as

$$E_P\left[\frac{x(T)}{x(0)r^T} - 1\right] = 0\tag{7}$$

Risk-neutral pricing of options proceeds by specifying a parametric model for the risk-neutral stochastic price process of the underlying stock. Parameter values are found that make the model's computed stock prices and/or option prices close (e.g., in the least-squares sense) to observed stock and/or option prices [4]. In the simplest case (the Black-Scholes model), this procedure requires an estimate of the volatility parameter, found either from past stock returns (i.e., historical volatility) or from market option prices (i.e., a best-fitting implied volatility).

However, suppose one has doubts about the correct parametric model. The formalism of the previous section provides an alternative. Let the scalar function  $f(x, \beta) = \frac{x(T)}{x(0)r^T} - 1$ , where  $\beta = r$ . The distribution  $\mu$  is the forecast distribution of  $x(T)$ . To estimate this, one could just use a histogram of past  $T$ -period stock returns as in [27, 29], a conditional histogram [28], or a more complex forecasting model [13]. The distribution is then substituted into equation (5) and solved to find the  $\nu(\beta)$  needed to estimate the density  $P(\beta)$ in equation (4), which is required to compute the option valuation (6). It is possible to extend the approach to handle stochastic dividends and interest rates.

Another approach presumes a particular form for  $\mu$ , and defines a vector  $f(x, \beta)$  with *i*th component  $\max[x(T) - K_i, 0]/r^T - C_i$ , where  $C_i$  is the observed market price for a call with exercise price  $K_i$ , as in [5, 19]. Then, equations (4)–(5) are used to study the nature of the measure  $P(\beta)$  implied by those options' market prices, while equation  $(6)$ could be used to value options other than those present in  $f$ . See [3, 7, 8] for some theoretical and applied extensions of this approach. (see also Weighted Monte Carlo).

Further refinements were developed by Gray et al. [16], showing that the associated dynamic hedge (i.e., entropic hedge ratio) outperformed hedging benchmarks, and by Alcock and Carmichael [1], extending the concept to enable valuation of American options.

The entropic approaches are not necessarily inconsistent with the conventional approach. In fact, extant closed-form option pricing models can be analytically derived by specification of the process generating the stock price distributions, and systematically applying the **Esscher transform**  $(4)$  as in  $[12, 14]$ .

#### **Application to Parameter Estimation**

A research program initiated by Hansen [17] first developed the generalized methods of moments (GMM) parameter estimator. Two entropy-based alternatives are defined, motivated by alternative frequentist estimation criteria suggested by large deviations theory (see Cramér's Theorem; Large Deviations). We begin with this alternative frequentist criterion, and finish by describing its connection to entropy. Interpret  $\beta$  in equation (2) to be an unknown vector of parameters from a set  $\Theta$  of possible parameter vectors, and  $f(x; \beta) = (f_1, \ldots, f_r)$ to be an  $r$ -component column vector of observable, real-valued functions. A time series of the random variable x is denoted  $x_1, \ldots, x_T$ . The corresponding (random) sample average of the vector  $f$  is denoted  $f_T(\beta) \equiv \sum_{t=1}^T f(x_t; \beta) / T.$ 

The empirical asset pricing literature considers processes for which a typical realization produces  $\lim_{T\to\infty} f_T(\beta) = E[f(x;\beta)],$  where the expectations operator is, unless otherwise subscripted, taken with respect to the invariant measure  $\mu$  of the process. So the probability of observing  $f_T(\beta)$  in a compact neighborhood that does not contain the population mean  $E[f(x;\beta)]$  must approach zero as  $T \to \infty$ . The asymptotic rate at which this probability goes to zero can be calculated by use of part of a powerful result of Ellis [11], exposited in [6], (pp.  $20-22$ ), and perhaps first used in asset pricing by Stutzer [26], (Appendix). Define the following extended, real-valued function of an  $r$ -component vector  $\nu$ :

$$\begin{split} \phi_T(\gamma;\beta) &\equiv \frac{1}{T} \log E \left[ e^{\gamma' \sum_{t=1}^T f(x_t,\beta)} \right] \\ &= \frac{1}{T} \log E \left[ \prod_{t=1}^T e^{\gamma' f(x_t,\beta)} \right] \end{split} \tag{8}$$

Define the asymptotic limit of equation  $(8)$  to be

$$\phi(\gamma;\beta) \equiv \lim_{T \to \infty} \phi_T(\gamma;\beta) \tag{9}$$

and the nonnegative, probability decay *rate* function

$$I(c) \equiv \sup_{\gamma} [\gamma' c - \phi(\gamma; \beta)] \tag{10}$$

identical to the optimally weighted GMM criterion:

$$\arg\min_{\beta} I(0) = \frac{1}{2} E[f(x;\beta)]'$$
$$\times \left(\sum_{\tau=-\infty}^{\tau=+\infty} \Gamma_{\tau}(\beta)\right)^{-1} E[f(x;\beta)] \tag{12}$$

forming the foundation for different feasible estimators, corresponding to different ways of estimating the population moments and infinite sum present in equation  $(12)$ , though the large deviation interpretation (see Large Deviations) of equation (12) no longer holds outside of Gaussianity.<sup>a</sup>

What can be done in more realistic cases where the researcher does not want to commit to specific distributional assumptions? The general criterion is

$$\arg\min_{\beta} \left[ I(0) = \sup_{\gamma} - \lim_{T \to \infty} \left( \phi_T(\gamma; \beta) \equiv \frac{1}{T} \log E \left[ e^{\gamma' \sum_{t=1}^T f(x_t, \beta)} \right] \right) \right] \tag{13}$$

Then the probability of observing a value of the sample average lying within a closed (open) set  $C$  (O) that does *not* contain the population mean  $E[f(x; \beta)],$  decays toward zero at a positive asymptotic rate that must be weakly larger (smaller) than  $\inf_{c \in C} I(c; \beta) \ (\inf_{c \in O} I(c; \beta)).$ 

Hansen [17] GMM framework estimates parameters and tests theoretical implications represented by the constraints:

$$\exists \; !\beta^* : E[f(x;\beta^*)] = 0 \tag{11}$$

where  $\beta^*$  is the unique parameter vector (to be estimated) that satisfies the moment constraints.

Define  $\mathcal{O}_{\epsilon}$  to be the open  $\epsilon$ -ball about  $E[f(x; \beta^*)]$  $= 0$ . Because the identification condition (11) implies that  $E[f(x;\beta)] \neq 0$  when  $\beta \neq \beta^*$ , the probability of finding  $f_T(\beta) \in \mathcal{O}_{\epsilon}$  decays to zero at an asymptotic rate weakly lower than  $\inf_{c \in \mathcal{O}_c} I(c)$ . Because the limit of this as  $\epsilon \downarrow 0$  is  $I(0)$ , which is 0 if and only if  $\beta = \beta^*$ , a sensible estimation criterion is to search for a value of  $\beta$  making it as small as possible, that is, find arg  $\min_{\beta} I(0)$  [15]. Kitamura and Stutzer [23] show that when the vector  $f$  is Gaussian with stationary covariance sequence  $E[(f(x_t; \beta) E[f(x_t;\beta)]\ (f(x_t;\ \beta) - E[f(x_{t-\tau};\ \beta)])'] \equiv \Gamma_{\tau}(\beta),$  $j = -\infty, \ldots, +\infty$ , this estimation criterion is

so a feasible estimator of equation  $(13)$  is needed. Fortunately, Kitamura [20] developed a smoothing approach to estimation, which was used in ([22], (equation (9)) to produce an analog estimator [24] of the minimizing  $\beta$  in equation (13) (for proof, see [23]). Under regularity conditions listed there, they showed that this estimator is asymptotically equivalent to feasible, optimally weighted GMM in non-IID cases.

#### Entropic Interpretation

When the process is IID (but not necessarily Gaussian),  $\phi_T(\gamma;\beta) = \log E[e^{\gamma' f(x;\beta)}]$ , so  $I(0) \equiv$  $\max_{\gamma} - \log E[e^{\gamma' f(x;\beta)}]$  and the large deviations estimation (see Large Deviations) criterion (13) simplifies to the exponential tilting criterion, that is,  $\arg \min_{\beta} [I(0) = \max_{\gamma} - \log E[e^{\gamma' f(x;\beta)}]]$ . From  $\text{equation (5)}$  and the comment immediately following it, we see that the optimized value of the criterion may also be interpreted as the moment-constrained minimum of relative entropy in equation  $(3)$ , in the IID special case.

In the general case  $(13)$ , the aforementioned analog estimator developed in  $(22]$ , equation  $(9)$ ) also has an entropic interpretation. It is the estimator that minimizes the relative entropy between the empirical distribution of smoothed observations and the distribution of smoothed observations under the moment restriction.

Alternatively, when one substitutes *D(µ P )* for *D(P µ)* in equation (3) with no change in the rest of the formalism, the result is the *empirical likelihood* criterion [25]. From the view point of statistical inference and estimation, the empirical likelihood criterion *D(µ P )* achieves various optimality properties, especially in terms of large deviations [21]. First-order Taylor approximation of *D(µ P )* results in the *χ*<sup>2</sup> distance (see [9], p. 333), so substituting it for *D(µ P )* yields the *Euclidean Empirical Likelihood* criterion [2, 18]. Of course, the large deviations interpretation is different, due to the interchange of *P* and *µ* in the formalism.

## **End Notes**

a*.* Also, the choice of criterion function impacts the finite sample behavior of feasible estimators even under Gaussianity.

## **References**

- [1] Alcock, J. & Carmichael, T. (2008). Nonparametric American option pricing, *Journal of Futures Markets* **28**, 717–748.
- [2] Antoine, B., Bonnal, H. & Renault, E. (2007). On the efficient use of informational content of estimating equations: implied probabilities and Euclidean empirical likelihood, *Journal of Econometrics* **138**, 461–486.
- [3] Avellaneda, M. (1998). Minimum relative-entropy calibration of asset-pricing models, *Journal of Theoretical and Applied Finance* **1**, 447–472.
- [4] Bates, D.S. (1996). Testing option pricing models, in *Handbook of Statistics 15* , G.S. Maddala & C.R. Rao, eds, North-Holland.
- [5] Buchen, P.W. & Kelly, M. (1996). The maximum entropy distribution of an asset inferred from option prices, *Journal of Financial and Quantitative Analysis* **31**, 143–159.
- [6] Bucklew, J. (1990). *Large Deviation Techniques in Decision, Simulation, and Estimation*, Wiley.
- [7] Cont, R. & Tankov, P. (2004). Nonparametric calibration of jump-diffusion processes, *Journal of Computational Finance* **7**(3), 1–49.
- [8] Cont, R. & Tankov, P. (2006). Retrieving Levy processes from option prices: regularization of a nonlinear inverse problem, *SIAM Journal of Control and Optimization* **45**, 1–25.

- [9] Cover, T.M. & Thomas, J.A. (1991). *Elements of Information Theory*, Wiley.
- [10] Csiszar, I. (1975). I-divergence geometry of probability distributions and minimization problems, *Annals of Probability* **3**, 146–158.
- [11] Ellis, R. (1984). Large deviations for a general class of random vectors, *Annals of Probability* **12**, 1–12.
- [12] Eberlein, E., Keller, U. & Prause, K. (1998). New insights into smile, mispricing, and value at risk: The Hyperbolic model, *Journal of Business* **71**, 371–405.
- [13] Foster, F.D. & Whiteman, C.H. (1999). An application of Bayesian option pricing to the soybean market, *American Journal of Agricultural Economics* **81**, 222–272.
- [14] Gerber, H. & Shiu, E. (1994). Option pricing by Esscher Transforms, *Transactions of the Society of Actuaries* **46**, 99–140.
- [15] Glasserman, P. & Jin, Y. (2000). *Comparing Stochastic Discount Factors Through their Implied Measures*, mimeo, Graduate School of Business, Columbia University.
- [16] Gray, P., Edwards, S. & Kalotay, E. (2007). Canonical pricing and hedging of index options, *Journal of Futures Markets* **27**, 771–790.
- [17] Hansen, L. (1982). Large sample properties of generalized methods of moments estimators, *Econometrica* **50**, 1029–1054.
- [18] Hansen, L., Heaton, J. & Yaron, A. (1996). Finite-sample properties of some alternative GMM estimators, *Journal of Business and Economic Statistics* **14**, 262–280.
- [19] Hawkins, R.J., Rubinstein, M. & Daniell, G.J. (1996). Reconstruction of the probability density function implicit in option prices from incomplete and noisy data, in *Maximum Entropy and Bayesian Methods*, K. Hanson & R. Silver, eds, Kluwer.
- [20] Kitamura, Y. (1997). Empirical likelihood methods with weakly dependent processes, *Annuals of Statistics* **25**, 2084–2102.
- [21] Kitamura, Y. (2007). Empirical likelihood methods in econometrics, in *Advances in Economics and Econometrics*, R. Blundell, W. Newey & T. Persson, eds, Cambridge University Press.
- [22] Kitamura, Y. & Stutzer, M. (1997). An informationtheoretic alternative to generalized method of moments estimation, *Econometrica* **65**, 861–874.
- [23] Kitamura, Y. & Stutzer, M. (2002). Connections between entropic and linear projections in asset pricing estimation, *Journal of Econometrics* **107**, 159–174.
- [24] Manski, C. (1988). *Analog Estimation Methods in Economics*, Chapman and Hall, London.
- [25] Owen, A. (2001). Chapman and Hall, *Empirical Likelihood*.
- [26] Stutzer, M. (1995). A Bayesian approach to diagnosis of asset pricing models, *Journal of Econometrics* **68**, 367–397.

- [27] Stutzer, M. (1996). A simple nonparametric approach to derivative security valuation, *Journal of Finance* **51**, 1633–1652.
- [28] Stutzer, M. & Chowdhury, M. (1999). A simple nonparametric approach to bond futures option pricing, *Journal of Fixed Income* **8**, 67–76.
- [29] Zou, J. & Derman, E. (1999). *Strike Adjusted Spread: A New Metric for Estimating the Value of Equity Options, Quantitative Strategies Research Note*, Goldman, Sachs and Co.

# **Further Reading**

Osborne, M.F.M. (1970). Brownian motion in the stock market, in *The Random Character of the Stock Market*, P. Cootner, ed., MIT Press.

Stutzer, M. (2003). Portfolio choice with endogenous utility: a large deviations approach, *Journal of Econometrics* **116**, 365–386.

## **Related Articles**

**Cramer's Theorem ´** ; **Esscher Transform**; **Generalized Method of Moments (GMM)**; **Large Deviations**; **Minimal Entropy Martingale Measure**; **Model Calibration**; **Weighted Monte Carlo**.

YUICHI KITAMURA & MICHAEL STUTZER
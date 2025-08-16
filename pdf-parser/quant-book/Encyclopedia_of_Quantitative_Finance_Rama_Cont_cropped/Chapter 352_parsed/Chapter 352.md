# **Stochastic Volatility** Models

The Black-Scholes model (see Black-Scholes For**mula**) rests upon a number of assumptions that are, to some extent, "counterfactual". Among these are continuity in time of the asset price process (they do not jump), the ability to hedge continuously without transaction costs, independent Gaussian returns, and constant volatility. Stochastic volatility models relax the last assumption by allowing volatility to be randomly varying; this is motivated by the following reason: the dependence of Black-Scholes implied volatilities computed from market prices of call and put options, known as the smile curve (see Implied Volatility Surface), is accounted for by stochastic volatility models. In other words, this modification of the Black-Scholes theory succeeds in one area where the classical model fails. In fact, it has been shown  $[18, 23]$  that any randomness in volatility produces a smile of implied volatilities. Empirical evidence for the smile curve of implied volatility appears in many studies, including [20], using data from before the 1987 crash, and in [16], where the postcrash skew is documented (see Implied Volatility Surface). Early work on fitting an implied volatility surface, includes [1], and [4, 6, 21]. An extensive empirical study of the stability of the fitted surfaces can be found in [5].

In fact, modeling volatility as a stochastic process is motivated *a priori* by empirical studies of stock price returns in which estimated volatility is observed to exhibit "random" characteristics. Additionally, the effects of transaction costs show up, under many models, as uncertainty in the volatility; fat-tailed returns distributions can be simulated by stochastic volatility; market "jump" phenomena are often best modeled as volatility jump processes. Stochastic volatility modeling is therefore more than a simple fix to one particular Black-Scholes assumption, but rather a powerful modification that describes a much more complex market.

Pricing derivatives in a market with stochastic volatility is an incomplete markets problem, a distinction explained below, and one which has far-reaching consequences, particularly for the hedging problem and the problem of parameter estimation. It is the

latter inverse problem that is the biggest mathematical and practical challenge introduced by such models.

Early surveys can be found in [9, 11], or [14], and books on stochastic volatility are also available [7, 17], and [10].

In most stochastic volatility models, the asset price  $(X_t)_{t\geq 0}$  satisfies the stochastic differential equation

$$dX_t = \mu X_t dt + \sigma_t X_t dW_t \tag{1}$$

where  $(\sigma_t)_{t>0}$  is called the volatility process. It must satisfy some regularity conditions for the model to be well defined, but it does not have to be an Itô process: it can be a jump process, a Markov chain, and so on. In order for it to be a volatility, it should be positive. Unlike the implied deterministic volatility models (see Local Volatility Model), the volatility process is *not* perfectly correlated with the Brownian motion  $(W_t)$ . Therefore, volatility is modeled to have an independent random component of its own. This leads to an incomplete market, that is, derivatives cannot, in general, be perfectly hedged by trading the underlying asset and money market only. In fact, there is no *unique* equivalent martingale measure.

#### Mean-reverting Stochastic Volatility Models

Typically, volatility is taken to be an Itô process satisfying a stochastic differential equation driven by a second Brownian motion. This is the easiest way to incorporate correlation with stock price changes. One desirable feature is *mean reversion*. The term itmean reverting refers to the characteristic (typical) time it takes for a process to get back to the mean level of its invariant distribution (the long-run distribution of the process) and "forget" about its past. From a financial modeling perspective, mean reverting refers to a linear pull-back term in the drift of the volatility process itself, or in the drift of some (underlying) process of which volatility is a function. Let us denote  $\sigma_t = f(Y_t)$  where f is some positive function. Then mean-reverting stochastic volatility means that the stochastic differential equation for  $(Y_t)$  has the following form:

$$dY_t = \alpha (m - Y_t) dt + \cdots d\hat{Z}_t \tag{2}$$

where  $(\hat{Z}_t)_{t\geq 0}$  is a Brownian motion correlated with  $(W_t)$ :  $d\langle W, \hat{Z}\rangle_t = \rho dt$ , with  $|\rho| \leq 1$ . It is often found

from financial data that  $\rho < 0$ , and there are economic arguments for a negative correlation or *leverage effect* between stock price and volatility shocks. From common experience and empirical studies, when volatility goes up, asset prices tend to go down. Some common driving processes  $(Y_t)$  are

LN Lognormal (non-mean-reverting):

$$dY_t = c_1 Y_t dt + c_2 Y_t d\hat{Z}_t \tag{3}$$

OU Ornstein-Uhlenbeck:

$$dY_t = \alpha (m - Y_t)dt + \beta d\hat{Z}_t \tag{4}$$

CIR Feller or Cox-Ingersoll-Ross:

$$dY_t = \kappa (m' - Y_t) dt + v \sqrt{Y_t} d\hat{Z}_t \qquad (5)$$

Some models studied in the literature are listed in Table 1.

Classical references investigating specific stochastic volatility models are [2, 13, 15, 22, 24], and [25]. These particular models are chosen for their nice properties (e.g., positivity and mean reversion) and analytical tractability, rather than from deeper financial reasons. The Heston model is very popular for its computational tractability.

Probability density functions of the stock price obtained from simulations exhibit fatter tails because of the random volatility. In particular, the negative correlation causes the tails to be asymmetric: the left tail is fatter.

## **Option Pricing**

Suppose first that there is an equivalent martingale measure  $\mathbb{I}P^{\star}$  under which the discounted stock price

**Table 1** Stochastic volatility models

| Authors                 | Correlation                 | f(y)                                   | $Y$ Process                       |
|-------------------------|-----------------------------|----------------------------------------|-----------------------------------|
| $Hull - White$<br>Scott | $\rho = 0$<br>$\rho = 0$    | $f(y) = \sqrt{y}$<br>$f(y) = e^y$      | Lognormal<br>Mean-<br>reverting   |
| Stein-Stein             | $\rho = 0$                  | $f(y) =  y $                           | $\text{OU}$<br>Mean-<br>reverting |
| Ball–Roma<br>Heston     | $\rho = 0$<br>$\rho \neq 0$ | $f(y) = \sqrt{y}$<br>$f(y) = \sqrt{y}$ | $\text{OU}$<br>CIR<br>CIR         |

 $e^{-rt}X_t$  is a martingale. Then, if we price any (and all) derivatives with maturity time  $T$  and payoff  $H$ using the formula  $V_t = I\!\!E^{\star} \{ e^{-r(T-t)} H | \mathcal{F}_t \}$ , for all  $t \leq T$  where  $(\mathcal{F}_t)$  is the filtration generated by the two Brownian motions, then there is no arbitrage opportunity. Thus  $V_t$  is a possible price for the claim. Equivalent martingale measures are constructed by rewriting  $\hat{Z}_t = \rho W_t + \sqrt{1 - \rho^2} Z_t$  where W and Z are independent standard Brownian motions under the physical measure  $\mathbb{I}P$ , and by setting

$$W_t^* = W_t + \int_0^t \frac{(\mu - r)}{f(Y_s)} \mathrm{d}s, \ \ Z_t^* = Z_t + \int_0^t \gamma_s \mathrm{d}s \tag{6}$$

The shift of the second independent Brownian motion does not affect the drift of  $X_t$ . By Girsanov's theorem,  $(W^{\star})$  and  $(Z^{\star})$  are independent standard Brownian motions under a measure  $\mathbb{P}^{(\gamma)}$  defined by

$$\frac{\mathrm{d}I\!P^{\star(\gamma)}}{\mathrm{d}I\!P} = \exp\left(-\frac{1}{2}\int_{0}^{T} ((\theta_{s}^{(1)})^{2} + (\theta_{s}^{(2)})^{2})\mathrm{d}s - \int_{0}^{T} \theta_{s}^{(1)}\mathrm{d}W_{s} - \int_{0}^{T} \theta_{s}^{(2)}\mathrm{d}Z_{s}\right),$$
$$\theta_{t}^{(1)} = \frac{\mu - r}{f(Y_{t})}, \qquad \theta_{t}^{(2)} = \gamma_{t} \tag{7}$$

Here  $(\gamma_t)$  is any adapted (and suitably regular) process. Technically, one needs to make an assumption on the pair  $(\frac{\mu-r}{f(Y_t)}, \gamma_t)$  so that  $\mathbb{P}^{*(\gamma)}$  is well defined as a probability measure. In particular, this is the case if  $\mu$  may depend on  $Y_t$  in such a way that the Sharpe ratio  $\frac{\mu(Y_t) - r}{f(Y_t)}$  and  $\gamma_t$  are bounded. Then, under  $\mathbb{P}^{(\gamma)}$ , the stochastic differential equations (1, 2) become

$$dX_t = rX_t dt + f(Y_t)X_t dW_t^{\star}$$
(8)

$$dY_t = [\alpha(m - Y_t) - \beta \Lambda] dt + \beta d\hat{Z}_t^{\star} \qquad (9)$$

where  $\hat{Z}_t^{\star} = \rho W_t^{\star} + \sqrt{1 - \rho^2} Z_t^{\star}$ , and  $\Lambda = \rho \frac{(\mu - r)}{f(Y_t)}$  $+\gamma_t\sqrt{1-\rho^2}$ . Any allowable choice of  $\gamma$  leads to an equivalent martingale measure  $\mathbb{I}P^{\star(\gamma)}$  and to the no*arbitrage* derivative prices

$$V_t = I\!E^{\star(\gamma)} \{ e^{-r(T-t)} H | \mathcal{F}_t \}$$
 (10)

where the conditional expectation is taken with respect to the filtration generated by the two Brownian motions. In the Markovian case, *Vt* = *P (t, Xt, Yt)* where *P (t, x, y)* is the solution of the pricing partial differential equation (PDE) obtained by the *Feynman–Kac formula*.

### *Special Case: Uncorrelated Volatility*

It turns out that the *ρ* = 0 case is much easier to handle mathematically. In equity markets, it is widely believed *ρ <* 0, but some studies suggest *ρ* is close to zero in foreign-exchange data. We now assume *ρ* = 0 and *(γt)* is independent of the Brownian motion *(Wt)* driving the stock price so that under the risk-neutral probability *IP(γ )* the volatility remains uncorrelated with *(Wt)*. The pricing formula (10) can be simplified under these assumptions. We can condition on the path of the volatility process and by iterated expectations, the price of a call option, for example, is then given by

$$C(t, X_t, Y_t) = I\!\!E^{\star(\gamma)} \Big\{ I\!\!E^{\star(\gamma)} \{ e^{-r(T-t)} (X_T - K)^+ \times |\mathcal{F}_t, \sigma_s, t \le s \le T \} |\mathcal{F}_t \} \tag{11}$$

The inner expectation is just the Black–Scholes computation with a time-dependent volatility. The answer is the Black–Scholes formula with appropriately averaged volatility, leading to the *Hull–White formula*:

$$C(t, x, y) = I\!E^{\star(\gamma)} \left\{ C_{\text{BS}}(t, x; K, T; \sqrt{\overline{\sigma^2}}) | Y_t = y \right\}$$
(12)

where

$$\overline{\sigma^2} = \frac{1}{T - t} \int_t^T f(Y_s)^2 \mathrm{d}s \tag{13}$$

and, for simplicity, we have assumed *(Yt)* is a Markov process. Thus *σ*<sup>2</sup> is the root-mean-square time average of *σ (*·*)* over the remaining trajectory of each realization, and the call option price is the average over all possible volatility paths. This formula admits a generalization in the correlated case obtained simultaneously in [19] and [26].

### *Summary*

The positive aspects of the stochastic volatility approach are as follows:

- It directly models the observed random behavior of market volatility.
- It allows to reproduce more realistic returns distributions, in particular fatter-than-lognormal tails.
- The asymmetry of the distribution is easily incorporated by correlating the noise sources.
- The smile/skew effect in option prices is exhibited in stochastic volatility models, where the correlation controls the skew.
- Stochastic volatility has also been successfully used in fixed income, foreign exchange, and credit markets.

However, new difficulties are associated with this approach:

- Volatility is not directly observed. As a consequence, estimation of the parameters of a specific model and the current level of volatility is not straightforward.
- There is no canonical stochastic volatility model that is generally accepted and the relevance of explicit formulas for particular models is not obvious.
- We have to deal with an incomplete market, which means that derivatives cannot be perfectly hedged with just the underlying. In addition, a volatility risk premium has to be estimated from option prices.
- Besides the choice of a particular model and its calibration, pricing with stochastic volatility models is a real challenge requiring sophisticated numerical methods. Various approximation techniques have also been proposed such as regular and singular perturbation methods in [7] and [8], WKB expansion for SABR models in [12], or small-time asymptotics in [3].

## **References**

[1] Avellaneda, M., Friedman, C., Holmes, R. & Samperi, D. (1997). Calibrating volatility surfaces via relativeentropy minimization, *Applied Mathematical Finance* **4**(1), 37–64.

- [2] Ball, C. & Roma, A. (1994). Stochastic volatility option pricing, *Journal of Financial and Quantitative Analysis* **29**(4), 589–607.
- [3] Berestycki, H., Busca, J. & Florent, I. (2004). Computing the implied volatility in stochastic volatility models, *Communications on Pure and Applied Mathematics* **57**(10), 1352–1373.
- [4] Derman, E. & Kani, I. (1994). Riding on a smile, *Risk* **7**, 32–39.
- [5] Dumas, B., Fleming, J. & Whaley, R. (1998). Implied volatility functions: empirical tests, *Journal of Finance* **53**(6), 2059–2106.
- [6] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- [7] Fouque, J.-P., Papanicolaou, G. & Sircar, K. (2000). *Derivatives in Financial Markets with Stochastic Volatility*, Cambridge University Press.
- [8] Fouque, J.-P., Papanicolaou, G., Sircar, K. & Solna, K. (2003). Multiscale stochastic volatility asymptotics, *SIAM Journal Multiscale Modeling and Simulation* **2**(1), 22–42.
- [9] Frey, R. (1996). Derivative asset analysis in models with level-dependent and stochastic volatility, *CWI Quarterly* **10**(1), 1–34.
- [10] Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*, Wiley Finance.
- [11] Ghysels, E., Harvey, A. & Renault, E. (1996). Stochastic volatility, in *Statistical Methods in Finance*, G. Maddala & C. Rao, eds, Handbook of Statistics, North Holland, Amsterdam, Vol. 14, chapter 5, pp. 119–191.
- [12] Hagan, P., Kumar, D., Lesniewski, A. & Woodward, D. (2002). *Managing Smile Risk*, Willmott Magazine, pp. 84–108.
- [13] Heston, S. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**(2), 327–343.
- [14] Hobson, D. (1996). *Stochastic Volatility*. Technical report, School of Mathematical Sciences, University of Bath.
- [15] Hull, J. & White, A. (1987). The pricing of options on assets with stochastic volatilities, *Journal of Finance* **XLII**(2), 281–300.

- [16] Jackwerth, J. & Rubinstein, M. (1996). Recovering probability distributions from contemporaneous security prices, *Journal of Finance* **51**(5), 1611–1631.
- [17] Lewis, A. (2000). *Option Valuation under Stochastic Volatility*, Finance Press.
- [18] Renault, E. & Touzi, N. (1996). Option hedging and implied volatilities in a stochastic volatility model, *Mathematical Finance* **6**(3), 279–302.
- [19] Romano, M. & Touzi, N. (1997). Contingent claims and market completeness in a stochastic volatility model, *Mathematical Finance* **7**, 399–410.
- [20] Rubinstein, M. (1985). Nonparametric tests of alternative option pricing models, *Journal of Finance* **XL**(2), 455–480.
- [21] Rubinstein, M. (1994). Implied binomial trees, *Journal of Finance* **LXIX**(3), 771–818.
- [22] Scott, L. (1987). Option pricing when the variance changes randomly: theory estimation, and an application, *Journal of Financial and Quantitative Analysis* **22**(4), 419–438.
- [23] Sircar, K.R. & Papanicolaou, G.C. (1999). Stochastic volatility, smile and asymptotics, *Applied Mathematical Finance* **6**(2), 107–145.
- [24] Stein, E. & Stein, J. (1991). Stock price distributions with stochastic volatility: an analytic approach, *Review of Financial Studies* **4**(4), 727–752.
- [25] Wiggins, J. (1987). Option values under stochastic volatility, *Journal of Financial Economics* **19**(2), 351–372.
- [26] Willard, G. (1997). Calculating prices and sensitivities for path-independent derivative securities in multifactor models, *Journal of Derivatives* **5**, 45–61.

## **Related Articles**

**Barndorff-Nielsen and Shephard (BNS) Models**; **Bates Model**; **Heston Model**; **Implied Volatility in Stochastic Volatility Models**; **Implied Volatility: Market Models**; **Regime-switching Models**; **Time Change**; **Uncertain Volatility Model**.

JEAN-PIERRE FOUQUE
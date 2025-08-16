# **Mixture of Distribution** Hypothesis

The mixed distribution hypothesis (MDH) in finance maintains heavy tails in price fluctuations  $\Delta X(t)$ that can be explained by embedding randomized time  $\xi(t)$ . Intuitively, the net price change  $\Delta X(t)$ over period t is hypothesized to be the sum of  $\xi(t)$ incremental interperiod steps, say  $\Delta X_{t,i}$ , giving

$$\Delta X(\xi(t)) = \sum_{i=1}^{\xi(t)} \Delta X_{t,i} \tag{1}$$

Randomized time  $\xi(t)$  can be thought of as the amount of economic time or the number of information events that traders actually experience during  $t$ , typically associated with volume-traded  $V(t)$ . The resulting convolution  $\Delta X(\xi(t))$  has a mixed distribution that can capture leptokurtosis, explain heterogeneity, including conditional heteroscedasticity, and improve model fitting similar to nonparametrics. Applications abound in finance (equity returns, bond prices) and macroeconomics (income, unemployment, exchange rates).

The statistical foundations of mixtures are well known [7]. If  $y(t) := \Delta X(t)$  has density  $f_y(y;\xi)$ and economic time  $\xi(t) \geq 0$  has density  $f_{\xi}(\xi)$ , then the observed convolution  $y(\xi(t))$  has a density mixture

$$f_{y(\xi)}(y) = \int_0^\infty f_y(y;\xi) f_{\xi}(\xi) \, \mathrm{d}\xi \tag{2}$$

See [22] for a survey of mixture models, including generalized gamma and beta, log-Cauchy and lognormal.

The use of compound or mixed distributions to explain leptokurtosis in price fluctuations  $\Delta X(t)$ , while retaining a finite variance, first appears in the finance literature in the 1960s<sup>a</sup>. A sequence of papers, including [25, 26], and prominently Clark [4], exploited in various ways a subordinated finite variance process model  $\Delta X(\xi(t))$  as a direct response to Mandelbrot's [20] controversial  $\alpha$ -stable hypothesis of aggregate prices. The latter "extreme value theory" framework permits infinite variance, but at a cost of estimation and inference challenges (see [5, 17]). Nevertheless, only the  $\alpha$ -stable laws form a

closed distribution class under affine transformations: finite variance  $\alpha$ -stable laws are the Gaussian laws that are necessarily symmetric, and infinite variance  $\alpha$ -stable laws permit asymmetry, making this class attractive for applied statistical analysis in finance (see [28] for an encyclopedic treatment of the  $\alpha$ stable laws).

Tests of MDH against nonmixtures, including normality or  $\alpha$ -stability, have mixed results [12, 21, 30], and there exists a sharp identification problem that is typically ignored (consider [19]). The subordinated process premise has successfully evolved into randomized volatility  $[1, 3, 11]$ , which now receives vigorous attention in the finance literature  $[8, 9, 11,$ 27] and extreme value theory literature [14, 15, 18]; some applications of distribution mixtures in finance are motivated by specification flexibility rather than explaining heavy tails  $[10]$ .

In the remainder of this article, we discuss at length Clark's [4] seminal model, noting the early attempts to improve on it, and conclude with remarks on recent extensions in the stochastic volatility literature.

#### **Randomized Time and Subordination**

Clark's [4] influential model of asset returns exploits Bochner's [2] and Feller's [7] work on subordinated Gaussian processes. Denote by  $\mu_{\nu}$ ,  $\sigma_{\nu}^2$ , and  $\kappa_{\nu}$  respectively the mean, variance, and kurtosis of  $y$ , and  $\sigma_{\text{v}|\text{z}}^2(t)$  is the conditional variance, given random z.

If  $\{X(t)\} \equiv \{X(t) : -\infty < t < \infty\}$  is a stochastic process and  $\{\xi(t)\}, \xi : \mathbb{N} \to \mathbb{R}_+$ , is a "driving process" then the stochastically indexed  $X(\xi(t))$  is "subordinated" to  $X(t)$ . If  $\{\Delta\xi(t)\}\$  is stationary and independent with mean  $\mu_{\Delta \xi} > 0$ , and<sup>b</sup>  $\Delta X(t) \stackrel{\text{iid}}{\sim} (0, \sigma_{\Lambda X}^2)$ , then the subordinated fluctuations  $\Delta X(\xi(t))$  are stationary and independent, and distributed:

$$\Delta X \left( \xi(t) \right) \stackrel{\text{iid}}{\sim} \left( 0, \mu_{\Delta \xi} \times \sigma_{\Delta X}^2 \right) \tag{3}$$

Since  $\mu_{\Delta\xi}$  reflects the arrival of new information, in Clark's model only the average amount of new information effects the dispersion of embedded returns  $\sigma^2_{\Lambda X(\xi)}$ . If, in addition, price fluctuations are normally distributed  $\Delta X(t) \stackrel{\text{iid}}{\sim} N(0, \sigma_{\Delta X}^2)$  and  $\sigma_{\Delta E}^2$  $< \infty$  and  $\Delta \xi(t)$  are independent of  $X(t)$ , then price

fluctuations  $\Delta X \left( \xi(t) \right)$  have kurtosis

$$\kappa_{\Delta X(\xi)} = 3 \left( 1 + \frac{\sigma_{\Delta\xi}^2}{\mu_{\Delta\xi}^2} \right) > 3 \tag{4}$$

a simple positive function of  $\sigma_{\Lambda\xi}^2$ , and larger than 3, the benchmark value for normals and therefore for what is considered canonically to be heavy tailed. The tails of price fluctuations  $\Delta X(\xi(t))$  grow heavier as the variance  $\sigma_{\Lambda k}^2$  of information flow increases, and are heavy tailed in the strict sense of being thicker than normals for any directing process  $\{\xi(t)\}\$  with  $\sigma_{\Lambda\xi}^2 > 0$ . Further, as in [4], if iid  $\Delta\xi(t)$  are lognormal with parameters  $\{c, v^2\}$  then

$$\mu_{\Delta\xi} = \exp\{c + v^2/2\} \text{ and } \sigma_{\Delta\xi}^2\n$$
  
 $\n= \exp\{2c + v^2\} \times [\exp\{v^2\} + 1] \qquad (5)$ 

and from equation (1) the convolution  $y(\xi(t))$  $\equiv \Delta X(\xi(t))$  is lognormal-normally distributed as follows:

$$f_{y}(y) = \frac{1}{2\pi\sigma_{\Delta X}^{2}\sigma_{\Delta\xi}^{2}} \int_{0}^{\infty} u^{-3/2}$$
$$\times \exp\left\{\frac{-(\ln u - c)^{2}}{2v^{2}} - \frac{y^{2}}{2u\sigma_{\Delta X}^{2}}\right\} du$$
(6)

Volume-traded  $V(t)$  may be positively associated with economic time  $\xi(t)$ , in which case equity returns should be heavier tailed during periods of substantial trader activity. Heimstra and Jones [13], for example, use this prediction to test for variance causality from volume to returns under a finite variance assumption.

Many models for relating randomized time to volume have been suggested. See [16] for a survey. Clark [4] used the parametric specification

$$\sigma_{\Delta X|\xi}^2(t) = \beta V(t)^{\gamma}, \text{ where } \beta, \gamma > 0 \qquad (7)$$

for the log-price  $X(t)$  of cotton future prices. Epps and Epps [6] use a parsimonious parametric asset price model to support Clark's mixtures of distribution model. Tauchen and Pitts [29] propose an asset price model that relates price fluctuations to volume via a variance-components framework with trader-specific and traderwide shocks. Unlike Clark their model predicts  $\Delta X(t)$  and  $V(t)$  are independent for each transaction, but have moments with common parameters. For example,  $\sigma_{\Delta X}^2$  and  $\mu_V$  are both increasing functions of the variance of the trader-specific shock and therefore exhibit spurious positive association (as opposed to Clark's ad hoc association).

Stochastic volatility models for asset returns inherently exploit the premise that a mixture of distributions captures the arrival of news, making this literature the latest offshoots of Clark's model [1, 11, 27]. The Brownian semimartingale framework for stochastic volatility has become dominant in the option pricing literature by permitting volatility clustering and accounting for market incompleteness (which abnegates option redundancy), providing flexible extensions of the Black-Scholes option pricing model. See, especially, **Stochastic Volatility Models** and **Econometrics of Option Pricing** in this volume, and consult [9, 23].

## **End Notes**

<sup>a.</sup>Evidently Newcomb [24] first used a mixture of normal distributions to account for numerous "discordant" observations (i.e., heavy tails), with an application to planetary orbits.

<sup>b.</sup>  $y \sim (\mu, \sigma^2)$  implies y is distributed with mean  $\mu$  and variance  $\sigma^2$ , iid stands for "independent and identically distributed".

#### References

- [1] Anderson, T. (1996). Return volatility and trading volume: an information flow interpretation of stochastic volatility, Journal of Finance 51, 169-204.
- [2] Bochner, S. (1960). Harmonic Analysis and the Theory of Probability, University of California Press, Berkeley.
- Carr, P., Geman, H., Madan, D.B. & Yor, M. (2003). [3] Stochastic volatility for Lévy processes, Mathematical Finance 13, 345-382.
- Clark, P.K. (1973). Subordinated stochastic process [4] model with finite variance for speculative processes, Econometrica 41, 133-153.
- Davis, R.A. (2009). Heavy tailed processes, in *Encyclo-*[5] pedia of Quantitative Finance, R. Cont, ed., Wiley, New York.
- [6] Epps, T.W. & Epps, M.L. (1976). The stochastic dependence of security price changes and transaction volumes: implications for the mixture-of-distributions hypothesis, Econometrica 44, 305-321.
- [7] Feller, W. (1971). An Introduction to Probability Theory and its Applications, Wiley, New York, Vol. II.

- [8] Fouque, J.-P. (2009). Option pricing with stochastic volatility, in *Encyclopedia of Quantitative Finance*, R. Cont, ed., Wiley, New York.
- [9] Garcia, R., Ghysels, E. & Renault, E. (2009). Econometrics of option pricing models, in *Handbook of Financial Econometrics*, Y. Ait-Sahalia & L.P. Hansen, eds, Elsevier, North Holland, forthcoming.
- [10] Geweke, J. & Keane, M. (2007). Smoothly mixing regressions, *Journal of Econometrics* **138**, 252–290.
- [11] Ghysels, E., Harvey, A. & Renault, E. (1995). Stochastic Volatility, in *Handbook of Statistics 15, Statistical Methods in Finance*, G.S. Maddala & C.R. Rao, eds, North Holland, Amsterdam.
- [12] Hall, J.A., Brorsen, W. & Irwin, S.H. (1989). The distribution of futures prices: a test of the stable paretian and mixture of normals hypotheses, *Journal of Financial and Quantitative Analysis* **24**, 105–116.
- [13] Heimstra, C. & Jones, J.D. (1994). Testing for linear and nonlinear granger causality in the stock price-volume relation, *Journal of Finance* **49**, 1639–1664.
- [14] Hill, J.B. (2008). *Robust Estimation and Inference for Extremal Dependence in Time Series*, Department of Economics, University of North Carolina, Chapel Hill, submitted.
- [15] Hill, J.B. (2009). On functional central limit theorems for dependent, heterogeneous arrays with applications to tail index and tail dependence estimation, *Journal of Statistical Planning and Inference* **139**, 2091–2110.
- [16] Karpoff, J.M. (1987). The relation between price changes and trading volume: a survey, *Journal of Financial and Quantitative Analysis* **22**, 109–126.
- [17] Kluppleberg, C. (2009). Extreme value theory, in ¨ *Encyclopedia of Quantitative Finance*, R. Cont, ed., Wiley, New York.
- [18] Kluppleberg, C. & Lindner, A. (2008). ¨ *Extremes of Random Volatility Models*, Department of Mathematics, Universitat M¨ unchen, submitted. ¨
- [19] Li, L.A. & Sedransk, N. (1988). Mixtures of distributions: a topological approach, *Annals of Statistics* **16**, 1623–1634.

- [20] Mandelbrot, B. (1963). The variation of certain speculative prices, *Journal of Business* **36**, 394–419.
- [21] Mandelbrot, B. (1973). Comments on: "A subordinated stochastic process model with finite variance for speculative processes" by P.K. Clark, *Econometrica* **41**, 157–159.
- [22] McDonald, J.B. & Butler, R.J. (1987). Generalized mixture distributions with an application to unemployment duration, *Review of Economics and Statistics* **69**, 232–240.
- [23] Mykland, P. & Zhang, L. (2008). *Inference for Continuous Semimartingales Observed at High Frequency: A General Approach*, mimeo, University of Chicago.
- [24] Newcomb, S. (1886). A generalized theory of the combination of observations so as to obtain the best result, *American Journal of Mathematics* **8**, 343–366.
- [25] Praetz, P.D. (1972). The distribution of share price changes, *Journal of Business* **45**, 49–55.
- [26] Press, J.S. (1967). A compound events model for security prices, *Journal of Business* **40**, 317–335.
- [27] Renault, E. (2009). Econometrics of option pricing, in *Encyclopedia of Quantitative Finance*, R. Cont, ed., Wiley, New York.
- [28] Samorodnisky, G. & Taqqu, M. (1994). *Stable Non-Gaussian Random Processes*, Chapman and Hall, New York.
- [29] Tauchen, G.E. & Pitts, M. (1983). The price variabilityvolume relationship on speculative markets, *Econometrica* **51**, 485–505.
- [30] Upton, D.E. & Shannon, D.S. (1979). The stable paretian distribution, subordinated stochastic processes, and asymptotic lognormality: an empirical investigation, *Journal of Finance* **34**, 1031–1039.

## **Related Articles**

**Stylized Properties of Asset Returns**; **Time Change**; **Time-changed Levy Process ´** .

JONATHAN B. HILL
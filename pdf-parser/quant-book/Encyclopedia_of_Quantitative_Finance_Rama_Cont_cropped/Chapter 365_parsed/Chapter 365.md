# **Realized Volatility and Multipower Variation**

Many financial markets effectively operate in continuous time with multiple transaction prices and quotes recorded each second. Although, such "ultra high-frequency" data are not useful for assessing the expected mean return of the underlying asset, it is highly informative regarding the strength of another key financial characteristic, namely, return volatility. In particular, it is feasible to estimate the realized return volatility over a fixed time period directly from high-frequency data with good precision without imposing a specific parametric structure on the return dynamics. Hence, as access to tick-bytick data became more commonplace and the first empirical links between cumulative absolute return measures and the underlying volatility were established in the mid-1990s, the literature on extracting time-varying return variation measures from highfrequency data has grown dramatically. The initial developments focused on measures reflecting the actual squared return variation, loosely denoted realized volatility (RV), over daily and weekly frequencies. However, extended measures capturing different return moments and/or providing more robust inference regarding the continuous *versus* jump components of the return variation process are now an integral part of this literature. The potential applications to areas such as risk management, derivatives pricing, portfolio choice, market microstructure, and general asset pricing are basically unlimited. This article briefly reviews the main developments in this literature.

A general no-arbitrage setting for a continuously evolving logarithmic asset price is given by a jumpdiffusive process. Formally, on an appropriate probability space, the stochastic logarithmic price process  $X_t$  is defined *via* 

$$X_t = X_0 + \int_0^t b_s \, \mathrm{d}s + \int_0^t \sigma_s \, \mathrm{d}W_s + \sum_{0 \le s \le t} \Delta X_s \quad (1)$$

where the predictable drift component,  $b_s$ , signifies the instantaneous (continuously compounded) mean return, the diffusive coefficient,  $\sigma_s$ , reflects the strength of the diffusive volatility,  $W_s$  denotes a standard Brownian motion, and  $\Delta X_s := X_s - X_{s-}$ 

indicates the jump size and is nonzero only if the price jumps exactly at time  $s$ . In the definition of  $X_t$ , we implicitly assume certain (weak) regularity conditions and that jumps are of finite variation: some results below extend to the case of infinite variation jumps, [29]. Equation (1) is a generic representation of the jump-diffusive stochastic volatility model that serves as a workhorse for continuous-time finance.

We are interested in inference regarding the actual volatility displayed by  $X$  over a given interval of time  $[0, T]$ . In the (infeasible) scenario, where we have access to a continuous record of  $X_t$ , we can directly determine the actual realization of the so-called quadratic variation (QV) of  $X.$ 

$$QV_{[0,T]} = \int_0^T \sigma_s^2 \, \mathrm{d}s + \sum_{0 \le s \le T} |\Delta X_s|^2 \qquad (2)$$

Importantly, in the continuous-record case, we may also perfectly identify the jumps in the sample path and we thus "observe" the continuous and discontinuous parts of the QV and obtain the decomposition.

$$QV_{[0,T]}^{c} = \int_{0}^{T} \sigma_{s}^{2} \, \mathrm{d}s \quad \text{and} \quad QV_{[0,T]}^{d} = \sum_{0 \le s \le T} |\Delta X_{s}|^{2}$$
(3)

The QV is of a particular interest as it is closely related to the (variance) risk of the asset. This is most transparent in a simplified setting. For a pure diffusion, if the (stochastic) volatility process is independent of the return innovations, and ignoring the (negligible) return variation induced by innovations to the mean drift, the returns are conditionally Gaussian with variance governed by  $QV_{[0,T]}^c$ . If the return interval is small, such as a day, we may safely ignore the mean drift altogether and for simplicity equate it to zero. We then have the distributional result.

$$(X_T - X_0) \bigg| \{ \sigma_s \}_{0 \le s \le T} \sim N \left( 0, \int_0^T \sigma_s^2 \, \mathrm{d}s \right) \quad (4)$$

Notice that the Gaussian distributional result is conditional on the realization of the so-called integrated variance which a priori is stochastic. In other words, the returns follow a Gaussian mixture distribution with the realization of the (diffusive) QV governing the actual return variation. If this integrated variance process is persistent, that is, displays pronounced positive serial correlation, then the return distribution is symmetric, but displays both unconditional and conditional leptokurtosis along with volatility clustering. The main features, which may modify this characterization and induce both asymmetries and more extreme outliers in the conditional return distribution are correlation between the return innovations and the volatility, the so-called leverage effect, and the presence of jumps. Nonetheless, the interpretation of  $QV_{[0,T]}$  as the relevant return variation measure remains intact. Moreover, the multivariate version of equation (4) applies as stated in [7].

In practice, we do not observe financial series continuously but rather obtain transaction price and quote data referring to specific points in time. Hence, the challenge is to design estimators from the discrete observations of  $X$  that can estimate continuous-time quantities like the QV and its decomposition into continuous and jump components. A closely related issue is the development of tests for the presence of jumps in the (partially) observed path of  $X$ . Suppose, we observe *X* at 0, ...,  $i\Delta_n$ , ...[ $T/\Delta_n$ ] $\Delta_n$ , where  $\Delta_n$  is a small positive sampling interval and  $[y]$  denotes the integer part of  $y$ . Since the time interval,  $T$ , is fixed, we cannot exploit standard "large (sample length)  $T$ " asymptotics for developing estimation and testing procedures but instead appeal to continuous-record asymptotics, that is,  $\Delta_n \to 0$ . For example, we may think of  $[0, T]$  as one trading day and assume that we observe the price process every 10 min, 5 min, 1 min, and so on. The exposition is split in three parts. We first define RV as a feasible estimator of QV and discuss its relation to the underlying return distribution. Next, the notion of multipower variation is introduced and we outline its use for robust inference regarding critical aspects of the quadratic return variation. In the following section, we discuss the application of realized multipower variation in formal testing for the presence of jumps. Finally, we briefly touch on procedures designed to mitigate the impact of market microstructure noise, which potentially allow for more efficient inference, as well as some multivariate generalizations of the results discussed in this article.

### **Realized Volatility**

Realized volatility, also interchangeably referred to as realized quadratic variation, is defined as

$$RV_T = \sum_{i=1}^{\left[T/\Delta_n\right]} |\Delta_i^n X|^2 \tag{5}$$

where  $\Delta_i^n X := X_{i\Delta_n} - X_{(i-1)\Delta_n}$ . Some authors label  $RV_T$  the realized variance, and refer to its square root as the Realized volatility. However, in this article, we follow the early literature and term  $RV_T$  Realized volatility.  $RV_T$  is simply a cumulative sum of squared high-frequency observations. Its usefulness stems from the fact that it consistently estimates the (unobservable) QV as  $\Delta_n \to 0$ , that is,

$$RV_T \stackrel{\mathbb{P}}{\longrightarrow} QV_T \tag{6}$$

A few comments are in order. First, the estimator is model-free and applies very broadly independent of parametric model assumptions. Moreover, it remains valid in the multivariate case as well. Second, the measure estimates the return variation over an interval and not the underlying spot volatility at any given point. In fact, inference regarding spot volatility is problematic without restrictive assumptions owing to the lack of a continuous record of price observations and the impact of microstructure frictions at ultra high frequencies. Third,  $RV_T$  resembles a rolling sample variance estimator. This statistic, labeled "historical volatility" has precedents in the literature. Fourth, Merton [36] notes that, in theory, high-frequency data can provide perfect inference whenever volatility is locally constant. Direct linkage of an empirical RV measure based on intraday returns to an underlying (stochastic) quadratic return variation appears first in [3]. Fifth, one trading day is the natural measurement period owing to the pronounced intraday volatility patterns and significant news announcement effects. These features render interpretation of realized return variation over intraday periods much more complex, [4]. Finally, it is important to recognize that  $RV_T$ provides an *ex post* estimate of the return variation, which is conceptually distinct from the *ex ante* conditional return variance.

In order to assess the accuracy with which  $RV_T$ measures  $QV_T$ , a central limit theorem (CLT)—characterizing its behavior as the sampling frequency increases—is useful. In the simplest case without jumps it follows from  $[14, 16, 17]$  that

$$\frac{1}{\sqrt{\Delta_n}} \left( RV_T - QV_T \right) \xrightarrow{\mathcal{L}-s} \epsilon \times \sqrt{2 \int_0^T \sigma_s^4 \, \mathrm{d}s} \tag{7}$$

where  $\stackrel{\mathcal{L}-s}{\longrightarrow}$  means stable convergence in law and  $\epsilon$ is a standard normal variable, defined on an extension of the original probability space. Stable convergence in law strengthens the usual convergence in law by  $\text{guaranteeing}$  that the convergence in equation (7) is joint with any random variable defined on the original probability space. This property is critical for feasible asymptotic inference as well as in the application of the delta method. We further note that for two nonoverlapping intervals, the measurement errors for the QV are serially uncorrelated. Evidently, the precision of  $RV_T$  can be gauged formally only if we can obtain a measure of the so-called integrated quarticity,  $IQ_T = \int_0^I \sigma_s^4 ds$ , from a given set of discrete price observations. This is, in fact, feasible through the general realized multipower variation statistics introduced below. Finally, we note that bootstrapping may improve finite sample inference, [26].

The result in equation (7) can be extended to the case when  $X$  contains jumps, [29]. The realized variation then provides a consistent estimate of the overall QV. If we want to further decompose it into the continuous and jump parts, we need to exploit results pertaining to the theory for general multipower variation statistics.

### **Multipower Variation**

The initial example of a multipower variation process is the so-called bipower variation  $(BV)$  proposed by Barndorff-Nielsen and Shephard [18, 19] and defined as . . . . .

$$BV_T = \frac{\pi}{2} \sum_{i=2}^{\lfloor 1/\Delta_n \rfloor} |\Delta_{i-1}^n X| |\Delta_i^n X| \tag{8}$$

The above papers prove that, even in the presence of a jump process,

$$BV_T \xrightarrow{\mathbb{P}} QV_T^c \tag{9}$$

Hence, it provides a consistent estimator for the integrated variance and we may thus further consistently estimate the jump contribution to QV via the difference between  $RV_T$  and  $BV_T$ . However, we note that the associated CLT for  $BV_T$  in the continuous case will not hold when jumps are present.

More generally, we may define realized multipower variation by raising  $m$  successive absolute price increments to arbitrary powers, indexed by the vector  $\mathbf{p} = (p_1, \dots, p_m)$ , where  $p_j \ge 0, j =$  $1, \ldots, m$ 

$$V(X; \mathbf{p}; \Delta_n)_T = (\mu_{p_1} \dots \mu_{p_m})^{-1} \times \sum_{i=m}^{[T/\Delta_n]} |\Delta_{i-m+1}^n X|^{p_m} \dots |\Delta_i^n X|^{p_1}$$
(10)

for  $\mu_a$  denoting the *a*th absolute moment of a standard normal. By appropriate scaling of the realized multipower variation, in the absence of jumps, we obtain the corresponding convergence result

$$\Delta_n^{1-p/2} V(X; \mathbf{p}; \Delta_n)_T \xrightarrow{\mathbb{P}} \int_0^T \sigma_s^p \, \mathrm{d}s \qquad (11)$$

where  $p = p_1 + \cdots + p_m$ . In analogy to the bipower variation case, this result is robust to the presence of jumps provided max $\{p_i\}_{i=1,\dots,m}$  < 2. Further generalizations and asymptotic properties are explored in [14] for  $X$  continuous. Some of these properties are extended to the case when  $X$  contains jumps in [21].

A prominent special case of multipower variation arises when **p** is a scalar. Then  $V(X; p; \Delta_n)_T$ is labeled realized power variation of order  $p$ . Obviously,  $V(X; 2; \Delta_n)_T$  coincides with the RV estimator. In addition, a natural estimator of integrated quarticity under the null hypothesis of no jumps may be based on the realized fourth power variation,  $V(X; 4; \Delta_n)_T$ . While this statistic is inconsistent under the jump alternative, many realized multipower variation statistics are consistent in the presence of jumps, including the so-called realized tripower variation with  $\mathbf{p} =$  $(4/3, 4/3, 4/3)$  and the realized quadpower variation with  $\mathbf{p} = (1, 1, 1, 1)$ .

An alternative way of estimating the continuous part of the QV is to use the truncated squared power variation proposed by Mancini [33, 34] and also analyzed by Jacod [29]. It is formally defined as

$$\widetilde{V}(X, 2, \Delta_n)_T = \sum_{i=1}^{[T/\Delta_n]} |\Delta_i^n X|^2 \mathbf{1}_{\{|\Delta_i^n X| \le \alpha(\Delta_n)^\gamma\}} \quad (12)$$

for arbitrary  $\alpha > 0$  and  $\gamma \in (0, 1/2)$ . The intuition is simple-we discard increments higher than a given threshold in the summation of the squared returns—thus effectively discarding the impact of jumps.

Given their consistency for  $QV_T$  and  $QV_T^c$  and the absence of serial correlation in the associated measurement errors,  $RV_T$  and  $BV_T$  serve as a natural basis for measuring and forecasting return volatility. The literature is too extensive for a thorough review and so we only provide an account of a few established findings. First, Andersen et al. [7], demonstrate that reduced-form time-series models for a realized volatility within the ARFIMA class generate forecasts which dominate traditional stochastic volatility and GARCH models estimated from daily return data. The long memory dependence incorporated in the ARFIMA setting is invariably highly significant and an important factor in forecast performance. Another key feature in the superior forecast performance is the ability of  $RV_T$  to adapt quickly to shifts in the underlying level of volatility. This allows forecasts to be conditioned on a more accurate assessment of the current volatility state compared to models based on daily returns. Second, Andersen et al. [5] find that forecast performance may be boosted further through a decomposition of  $RV_T$  into the continuous and jump parts. The diffusive volatility is the main source of long-range dependence, so separating out the jumps allows for a more refined measure of the relevant volatility state and improves forecast precision correspondingly. An alternative approach exploiting a mix of different realized power variation statistics for forecasting is the so-called MIDAS regressions proposed by Ghysels et al. [25]. Third, Andersen et al.  $[10]$  provide an analytic framework for gauging the performance of reduced form a realized volatility forecasts across a broad class of popular diffusive stochastic volatility specifications, finding that the loss of predictive ability is minor relative to using (infeasible) forecasts based on the true underlying model. The usefulness of reduced form a realized volatility and (in the multivariate extension) covariation forecast models from practical perspectives is documented, for example, in [24] and [13] for portfolio allocation, in [8] for dynamic estimation of systematic (beta) market risk, in [2] for specification testing of term structure models, and in [12] for option pricing and associated trading strategies.

Realized multipower variation also facilitates estimating general parametric continuous-time models, which are challenging because of the latency of the stochastic volatility and the presence of price jumps. Barndorff-Nielsen and Shephard [16, 20] consider estimation by computing second-order moments of realized volatility. Meddahi [35] provides moments of realized volatility across a broad class of models. Closed-form expressions for moments of general realized multipower variation statistics (e.g., bipower variation), however, are typically not known, even when the moments of their continuous-time counterparts can be computed. Bollerslev and Zhou [22] estimate affine jump-diffusion models by treating the realized volatility as the unobservable quadratic variation in a method-of-moments procedure. They show via simulations that the impact of the measurement error on the parameter estimates is small. Corradi and Distaso [23] provide formal justification for the estimator of [22]. They consider joint asymptotics, both long time span and continuous record, and show that (in the general case) when the intraperiod sampling frequency increases faster than sample length, the measurement error of realized volatility (and in some cases bipower variation) is asymptotically negligible. Todorov [38] further generalizes these results. He proves the uniform integrability of realized multipower variation statistics under general specifications for the price jump process and demonstrates that the realized multipower variation can be used effectively in making semiparametric inference about general classes of continuous-time models containing jumps.

# Jump Testing

Another important application of realized multipower variation is to determine whether, *on a given path*, the process  $X$  contains jumps or not. This may again be accomplished in entirely model-independent fashion, that is, without imposing additional structure on  $X$  besides specification (1). Barndorff-Nielsen and Shephard [18, 19] propose testing for jumps by determining whether  $QV_{[0,T]}^d$  is statistically different from zero. For this purpose, they derive the joint

asymptotic distribution of RV and BV conditional on the path of  $X$  not containing jumps.

Huang and Tauchen [28] discuss various transformations of these tests which often lead to significant improvements in finite sample test performance. They also document that these procedures generally provide reliable tests. Alternative tests for the null hypothesis of no jumps can be derived by replacing the bipower variation with other realized multipower variation estimates of  $QV_T^c$  or with the truncated squared power variation (see also [31] for an alternative but related jump test).

Recently, Ait-Sahalia and Jacod [1] proposed an attractive alternative to these tests. They constructed a test statistic as a ratio of power variation of order four computed over two different frequencies

$$\Phi_n^{(j)} = \frac{V(X;4;k\Delta_n)_T}{V(X;4;\Delta_n)_T} \tag{13}$$

where  $k > 2$  is an integer (typically 2 or 3). This test statistic behaves very differently depending on whether  $X$  contains jumps on the (partially) observed path or not, since,

$$\Phi_n^{(j)} \xrightarrow{\mathbb{P}} \begin{cases} 1 & \text{if } X \text{ contains jumps} \\ k & \text{if } X \text{ does not contain jumps} \end{cases} \tag{14}$$

Ait-Sahalia and Jacod [1] derive the CLT for  $\Phi_n^{(j)}$ both when the given path of  $X$  contains jumps and when it does not. This allows for tests of both the null of no jumps (like above) and the null of jumps.

Finally, Lee and Mykland [32] pursue a different strategy as they test for jumps at each single high-frequency observation. The motivation is that, under the null hypothesis of no jumps, the high-frequency increments, standardized by the estimated local volatility, are asymptotically normally distributed. It has the convenient feature that the exact timing of significant jumps within the trading period is identified. Andersen et al. [9] explore a similar strategy determining the exact location of, potentially multiple, jumps from uniform test statistics across all high-frequency returns over each trading day.

## Some Important Extensions

An important feature ignored in our exposition is the impact of so-called market microstructure noise.

This refers to the patterns induced in high-frequency returns owing to features such as a discrete price grid, the absence of continuous trading, and the presence of a bid-ask spread. Hence, the observed price may be seen as a noisy indicator of an underlying ideal price contaminated by a (small) noise process. This noise component induces a bias in the empirical RV measures which tends to grow with increasing sampling frequency. As such, when a realized volatility is computed from ultra high-frequency returns, it is critical to adjust for the impact of microstructure noise. Andersen *et al.* [6] suggest gauging the highest sampling frequency at which the systematic bias induced by the noise is negligible, via a so-called volatility signature plot, and use that frequency for the realized volatility computation. However, it is potentially more efficient to sample more frequently and adjust for the noise component. This approach is pursued in a number of papers in the recent years; see, for example, [11, 15, 27, 39, 40]. While the asymptotic theory has developed for the case of a pure diffusive price process, the properties of the various procedures in the presence of jumps remain largely unknown. Recently, Podolskij and Vetter [37] propose to modify the bipower variation in a way which is robust both to the microstructure noise and price jumps (of finite activity).

In addition, our exposition has focused on the univariate case. If  $X$  is continuous, the multivariate extension is conceptually straightforward and has been done in [14, 17] (although the practical application can be challenging). If  $X$  contains jumps, matters are much more complicated, as realized multipower variation can behave very differently depending on whether the jumps in individual series arrive jointly or not. This is exploited by Jacod and Todorov [30], who propose tests for both whether the jumps in the individual components arrive together or not without any restriction on the possible jump dependence.

In summary, the realized volatility and related realized multipower variation literature is vibrant. Given the large efficiency gains obtained from volatility measurements exploiting high-frequency data relative to daily data and the increasing availability of tick-by-tick data, both the theoretical and the empirical research within this area will surely continue to grow in the future.

## **Acknowledgments**

Andersen's work was supported by a grant from the NSF to the NBER and CREATES funded by the Danish National Research Foundation.

## **References**

- [1] Ait-Sahalia, Y. & Jacod, J. (2009). Testing for jumps in a discretely observed process, *Annals of Statistics* **37**, 184–222.
- [2] Andersen, T.G. & Benzoni, L. (2009). Do Bonds span volatility risk in the U.S. Treasury Market? A specification test for affine term structure models, *Journal of Finance* forthcoming.
- [3] Andersen, T.G. & Bollerslev, T. (1998). Answering the critics: yes, standard volatility models do provide accurate forecasts, *International Economic Review* **39**, 885–905.
- [4] Andersen, T.G. & Bollerslev, T. (1998). Deutsche markdollar volatility: intraday activity patterns, macroeconomic announcements, and longer run dependencies, *Journal of Finance* **53**, 219–265.
- [5] Andersen, T., Bollerslev, T. & Diebold, F.X. (2007). Roughing it up: including jump components in the measurement, modeling, and forecasting of return volatility, *Review of Economics and Statistics* **89**, 701–720.
- [6] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Labys, P. (2000). Great realizations, *Risk* **13**, 105–108.
- [7] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Labys, P. (2003). Modeling and forecasting realized volatility, *Econometrica* **71**, 579–625.
- [8] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Wu, G. (2006). Realized beta: persistence and predictability, in *Advances in Econometrics: Econometric Analysis of Economic and Financial Time Series*, T. Fomby & D. Terrell, eds, Elsevier Science, Vol. 20.
- [9] Andersen, T.G., Bollerslev, T. & Dobrev, D. (2007). Noarbitrage semimartingale restrictions for continuous-time volatility models subject to leverage effects, jumps and i.i.d. noise: theory and testable distributional assumptions, *Journal of Econometrics* **138**, 125–180.
- [10] Andersen, T.G., Bollerslev, T. & Meddahi, N. (2004). Analytic evaluation of volatility forecasts, *International Economic Review* **45**, 1079–1110.
- [11] Bandi, F. & Russell, J. (2006). Separating microstructure noise from volatility, *Journal of Financial Economics* **79**, 655–692.
- [12] Bandi, F.M., Russell, J.R. & Yang, C. (2008). Realized volatility forecasting and option pricing, *Journal of Econometrics* **71**, 34–46.
- [13] Bandi, F., Russell, J. & Zhu, J. (2008). Using highfrequency data in dynamic portfolio choice, *Econometric Reviews* **27**, 163–198.
- [14] Barndorff-Nielsen, O.E., Graversen, S., Jacod, J., Podolskij, M. & Shephard, N. (2005). A central limit

theorem for realised power and bipower variations of continuous semimartingales, in *From Stochastic Analysis to Mathematical Finance, Festschrift for Albert Shiryaev*, Y. Kabanov & R. Lipster, eds, Springer.

- [15] Barndorff-Nielsen, O.E., Hansen, P., Lunde, A. & Shephard, N. (2008). Designing realised kernels to measure the ex-post variation of equity prices in the presence of noise, *Econometrica* **76**, 1481–1536.
- [16] Barndorff-Nielsen, O.E. & Shephard, N. (2002). Econometric analysis of realised volatility and its use in estimating stochastic volatility models, *Journal of the Royal Statistical Society: Series B* **64**, 253–280.
- [17] Barndorff-Nielsen, O.E. & Shephard, N. (2004). Econometric analysis of realised covariation: high-frequency covariance, regression and correlation in financial economics, *Econometrica* **72**, 885–925.
- [18] Barndorff-Nielsen, O.E. & Shephard, N. (2004). Power and bipower variation with stochastic volatility and jumps, *Journal of Financial Econometrics* **2**, 1–37.
- [19] Barndorff-Nielsen, O.E. & Shephard, N. (2006). Econometrics of testing for jumps in financial economics using bipower variation, *Journal of Financial Econometrics* **4**, 1–30.
- [20] Barndorff-Nielsen, O.E. & Shephard, N. (2006). Impact of jumps on returns and realised variances: econometric analysis of time-deformed Levy processes, ´ *Journal of Econometrics* **131**, 217–252.
- [21] Barndorff-Nielsen, O.E., Shephard, N. & Winkel, M. (2006). Limit theorems for multipower variation in the presence of jumps in financial econometrics, *Stochastic Processes and their Applications* **116**, 796–806.
- [22] Bollerslev, T. & Zhou, H. (2002). Estimating stochastic volatility diffusionusing conditional moments of integrated volatility, *Journal of Econometrics* **109**, 33–65.
- [23] Corradi, V. & Distaso, W. (2006). Semiparametric comparison of stochastic volatility models using realized measures, *Review of Economic Studies* **73**, 635–667.
- [24] Fleming, J.R., Kirby, C.W. & Ostdiek, B.F. (2003). The economic value of volatility timing using realized volatility, *Journal of Financial Economics* **67**, 473–509.
- [25] Ghysels, E., Santa-Clara, P. & Valkanav, R. (2006). Predicting volatility: how to get most out of returns data sampled at different frequencies, *Journal of Econometrics* **131**, 59–95.
- [26] Goncalves, S. & Meddahi, N. (2009). Bootstrapping realized volatility, *Econometrica* **77**, 283–306.
- [27] Hansen, P. & Lunde, A. (2006). Realized variance and market microstructure noise, *Journal of Business and Economic Statistics* **24**, 127–161.
- [28] Huang, X. & Tauchen, G. (2005). The relative contributions of jumps to total variance, *Journal of Financial Econometrics* **3**, 456–499.
- [29] Jacod, J. (2008). Asymptotic properties of power variations and associated functionals of semimartingales, *Stochastic Processes and their Applications* **118**, 517–559.

- [30] Jacod, J. & Todorov, V. (2009). Testing for common arrivals of jumps for discretely observed multidimensional processes, *Annals of Statistics* **37**, 1792–1838.
- [31] Jiang, G. & Oomen, R. (2008). A new test for jumps in asset prices, *Journal of Econometrics* **144**, 352–370.
- [32] Lee, S. & Mykland, P. (2008). Jumps in financial markets: a new nonparametric test and jump dynamics, *Review of Financial Studies* **21**, 2535–2563.
- [33] Mancini, C. (2001). Disentangling the jumps of the diffusion in a geometric jumping Brownian motion, *Giornale dell'Instituto Italiano degli Attuari* **LXIV**, 19–47.
- [34] Mancini, C. (2009). Nonparametric threshold estimation for models with stochastic diffusion coefficient and jumps, *Scandinavian Journal of Statistics* **36**, 270–296.
- [35] Meddahi, N. (2002). Theoretical comparison between integrated and realized volatility, *Journal of Applied Econometrics* **17**, 479–508.

- [36] Merton, R.C. (1980). On estimating the expected return on the market, *Journal of Financial Economics* **8**, 323–361.
- [37] Podolskij, M. & Vetter, M. (2009). Estimation of volatility functionals in the simultaneous presence of microstructure noise and jumps, *Bernoulli* **15**, 634–658.
- [38] Todorov, V. (2009). Estimation of continuous-time stochastic volatility models with jumps using highfrequency data, *Journal of Econometrics* **148**, 131–148.
- [39] Zhang, L. (2006). Efficient estimation of stochastic volatility using noisy observations: a multi-scale approach, *Bernoulli* **19**, 1019–1043.
- [40] Zhang, L., Mykland, P. & Ait-Sahalia, Y. (2005). A tale of two time scales: determining integrated volatility with noisy high frequency data, *Journal of the American Statistical Association* **100**, 1394–1411.

TORBEN G. ANDERSEN & VIKTOR TODOROV
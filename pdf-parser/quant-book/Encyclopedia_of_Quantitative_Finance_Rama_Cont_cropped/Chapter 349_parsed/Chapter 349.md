# **Long Range Dependence**

## From Long to Short-range Dependency in **Discrete-time Models**

The widely known class of ARMA (autoregressive moving average) processes used for modeling discrete-time processes (see  $[5, 6]$ ) gives a first approach to short- and long-range dependence. For instance, the model that explains the value of a variable today, say  $X_t$ , mainly via its value yesterday,  $X_{t-1}$ , up to a centered error  $\varepsilon_t$ , leads under mild conditions to a zero mean stationary dependent process  $(X_t)_{t\in\mathbb{Z}},$ 

$$X_t = bX_{t-1} + \varepsilon_t \tag{1}$$

for an independent, identically distributed (i.i.d) noise sequence  $\varepsilon$  and  $|b| < |$ . Such a process is, short-range dependent; this means that the process quickly forgets all about its past. A more rigorous criterion is that, under stationary assumption, the correlation function  $\rho_X(h) = \text{corr}(X_t, X_{t+h})$  is exponentially decreasing, with

$$|\rho_X(h)| \sim_{h \to +\infty} e^{-\vartheta h} \tag{2}$$

for positive constant  $\vartheta$ , a property satisfied by equation (1) with  $\vartheta = -\log(|b|)$ .

Now consider the lag operator L,  $LX_t = X_{t-1}$  and rewrite model  $(1)$  as follows:

$$(1 - bL)X_t = \varepsilon_t \tag{3}$$

For the above behavior to occur, it is required that  $|b| < 1$ . If  $|b| = 1$ , the process is no longer stationary, and , for example, for  $b = 1$  the so-called unit root problem appears. An intermediate case of high interest is that of a fractional unit root. More precisely, set

$$(1 - L)^{\alpha} X_t = \varepsilon_t \tag{4}$$

where  $|\alpha| < 1/2$  is not an integer. The operator  $(1 - L)^{\alpha}$  is then defined (see [14, 15, 22]) by its series expansion

$$(1-L)^{\alpha} = 1 - \sum_{k=1}^{\infty} \frac{\alpha \Gamma(k-\alpha)}{\Gamma(k+1)\Gamma(1-\alpha)} L^{k}$$

where, for positive x,  $\Gamma(x) = \int_0^{+\infty} u^{x-1} e^{-u} du$  and  $L^k X_t = X_{t-k}$ . In that case, we recover a stationary

process  $(X_t)$ , but for large values of h,

$$|\rho_X(h)| \sim_{h \to +\infty} Ch^{2\alpha - 1} \tag{5}$$

This means that the covariance function (which is a measure of dependence between the observations) decays slowly. This can also be characterized in the frequency domain by the behavior near zero of the discrete spectral density defined by

$$f_X(\lambda) = \sigma_0^2 \sum_{h \in \mathbb{Z}} \rho_X(h) \mathrm{e}^{i\lambda h} \tag{6}$$

The spectral density is such that  $f_X(0)$  is finite positive and well defined in case (1) under  $|b| < 1$ , whereas

$$f(\lambda) \sim_{\lambda \to 0} C\lambda^{-2\alpha} \tag{7}$$

in case (4). Here, we can see that in the range  $-1/2 < \alpha < 1/2$ , two different cases arise:

- the case  $-1/2 < \alpha < 0$ , where  $f_X(0) = 0$ , and the sum of the correlations is finite—also called intermediate-memory case;
- the case  $0 < \alpha < 1/2$ , where  $f_X(0) = +\infty$ , and the sum of the correlations is infinite—also called long-memory case.

It is worth mentioning that many strategies for statistical inference (see [3]) on  $\alpha$  are related to the expansion  $\log f_X(\lambda) = C - 2\alpha \log \lambda + \text{Remain-}$ *der*, for  $\lambda$  small enough (see [12, 20]). Note also that standard log-likelihood methods were studied in this framework, which was new in the 1980s in the sense that many crucial standard assumptions required to obtain "good" properties of the estimators were violated (see [10, 11]).

Such models have been applied to the term structure of interest rates [1] and to foreign exchange rates [8]. However, it is well known that linear models fail to adequately represent asset returns, which have been frequently modeled using GARCH (generalized autoregressive conditionally heteroskedastic) (see **GARCH Models**) models [13]. Fractional extensions of GARCH models have been proposed to capture long-range dependence properties in the volatility process [2, 4]. More precisely, a GARCH model represents  $X_t = \ln(S_t/S_{t-1})$  where  $S_t$  is an asset price as  $X_t = \sigma_t \varepsilon_t$  and  $\varepsilon_t$  is a centered white-noise process

with variance 1. Then the recurrence equations

$$\sigma_t^2 = a_0 + \sum_{j=1}^p a_j X_{t-j}^2 + \sum_{k=1}^q b_k \sigma_{t-k}^2 \qquad (8)$$

can be written as ARMA representations with respect to the white noise  $v_t = X_t^2 - \sigma_t^2$ . It is then natural to study the effect of fractional unit root in such equations, and the long-range dependence properties. The point in GARCH models is that the existence of a unit root in this framework leading to processes called IGARCH (Integrated GARCH) models can be compatible with stationarity and is a mean of modeling persistence in variance of shocks. Thus, fractional models in this context turn out to be less essential. The theoretical study of the resulting processes can be also difficult: it is already the case without long-range dependence.

It is therefore natural to formulate such models in continuous time.

# Long-range-dependent Continuous-time **Models in Finance**

Indeed, model (4) for  $X_t$  has properties that are very similar to fractional Brownian motion (see Fractional Brownian Motion) increments, introduced by Mandelbrot and Van Ness [18]. More precisely, a natural analog of  $(1 - L)^{-\alpha} \varepsilon_t$  is  $\int_0^t (t - s)^{\alpha} dB(s)$  where  $B$  is a standard Brownian motion. The integral should start at  $-\infty$  for stationarity purpose, but it would not have finite variance. This is why the truncated version above is often used for modeling purposes. Fractional Brownian motion, whether truncated or not, does not have the semimartingale property. As this property is crucially required for log asset prices in continuous-time arbitrage-free models, fractional models led to problems in this regard. This was confirmed by Rogers [21] who showed the existence of arbitrage in presence of fractional Brownian motion for the log-prices. Moreover, there is no compelling empirical evidence of long memory in asset returns. But Hull and White-type [17] or stochastic volatility models lead to the idea that there was some kind of persistence in the volatility process. This persistence can be modeled by the insertion of fractional Brownian motion in the volatility equation.

Consider first a stochastic volatility model (see Stochastic Volatility Models) defined as a bivariate diffusion process:

$$\begin{cases} \mathrm{d}S_t/S_t = \mu(t, S_t)\mathrm{d}t + \sigma_t \mathrm{d}B_t^{(1)},\\ \sigma_t^2 = f(\eta_t),\\ \mathrm{d}\eta_t = m(\eta_t)\mathrm{d}t + g(\eta_t)\mathrm{d}B_t^{(2)} \end{cases} \tag{9}$$

where  $(B_t^{(1)}, B_t^{(2)})$  is a bidimensional standard Brownian motion. Let us consider the case where  $B^{(1)}$  and  $B_t^{(2)}$  are independent. To introduce some long-range dependence in the volatility behavior, the Brownian motion driving the volatility equation can be replaced by a fractional Brownian motion. Stochastic differential equations driven by fractional Brownian motions require advanced tools for proving existence and uniqueness of solutions [7, 16, 19]. A few simple examples can be studied with more "elementary" tools (see [9]). For instance, take

$$\begin{cases}\ndS_t/S_t = \mu(t, S_t)dt + \sigma_t dB_t^{(1)}, \\
\sigma_t^2 = \exp(2\eta_t), \\
d\eta_t = k(\theta - \eta_t)dt + g dB_t^{(\alpha)}, \quad k, \theta, g \quad \text{constants} \n\end{cases} \n$$
(10)

where  $B_t^{(\alpha)} = \int_0^t (t-s)^{\alpha} dB_s^{(2)} / \Gamma(1+\alpha)$ . For simplicity, we shall set  $\mu \equiv 0$  in the following. Initial conditions for  $\sigma_t$  can be chosen so that the process is stationary. Then, it can be checked that the process  $\sigma_t$  is long-range dependent when considered as continuously observed, in the sense given in equations (5) and (7), where the spectral density is now the continuous-time one (i.e.,  $f_Y^c(\lambda) =$  $s_0^2 \int e^{i\lambda u} \rho_X(u) du$ .

Of course, the process is, in fact, discretely observed. It is worth noting that the correlation property is stable from continuous to discrete-time observations. The folding formula that links the continuous-time formula of spectral density to the discrete-time one (namely, if  $\Delta$  is the sample step,  $f_X(\lambda) = (1/\Delta) \sum_{n \in \mathbb{Z}} f_X^c((\lambda + 2\pi n)/\Delta)$  shows, on the other hand, that the spectral long-memory behavior is preserved when going from continuous-time observation to discrete-time sample for  $0 < \alpha <$  $1/2.$ 

The additional difficulty here is that the volatility  $\sigma_t^2$  process is not observed. Therefore, for statistical purpose and estimation of the parameters of the model, approximations must be used. As the first equation is standard, the quadratic variation of the observed log price process is the integrated volatility, and therefore, if  $\{t_i\}_i$  is a partition of the interval  $[t, T]$ , then

$$\int_{t}^{T} \sigma_{u}^{2} \mathrm{d}u = \lim_{\max_{i} |t_{i+1}-t_{i}| \to 0} \sum_{i} [\ln(S_{t_{i+1}}) - \ln(S_{t_{i}})]^{2}$$
(11)

where the limit holds in probability. Thus, it is possible, if high-frequency data are available, to build pseudo-observations of the process  $(1/h) \int_{t}^{t+h} \sigma_{u}^{2}$  $du \sim \sigma_t^2$ , for small values of h. Note that  $Z_t =$  $\int_{t}^{t+1} \sigma^{2}(u) du$  can also be consistently estimated with high-frequency data; it is stationary and long memory, with the same memory parameter  $\alpha$  as  $\sigma^2$ . Statistical inference for the parameters can then be implemented, by using Whittle contrast or more classical log-likelihood maximization.

From the point of view of option pricing, the general formula of option prices for a deterministic interest rate  $r(t)$  under the no-free-lunch assumption is still valid. The call option price  $C_t$  is given by  $C_t =$  $B(t, T) \mathbb{E}^{\mathbb{Q}}[\max(0, S_T - K)|\mathcal{F}_t]$  where  $B(t, T) =$  $\exp(-\int_t^T r(u) du)$  is the price at t of a zero coupon bond of maturity T and  $\mathbb{Q}$  is the probability equivalent to  $\mathbb{P}$  under which the discounted price process is martingale. Then we get

$$C_{t} = S_{t} \left\{ \mathbb{E}^{\mathbb{Q}} \left[ \Phi \left( \frac{m_{t}}{U_{t,T}} + \frac{U_{t,T}}{2} \right) \right] - e^{-m_{t}} \mathbb{E}^{\mathbb{Q}} \left[ \Phi \left( \frac{m_{t}}{U_{t,T}} - \frac{U_{t,T}}{2} \right) \right] \right\} \quad (12)$$

where  $m_t = \ln(S_t/(KB(t,T))), U_{t,T} = \sqrt{\int_t^T \sigma_u^2 du}$ and  $\Phi(u) = \int_{-\infty}^{u} e^{-t^2/2} dt / \sqrt{2\pi}$ . The point is that the bivariate process  $(\ln(S_t), \sigma_t^2)$  is no longer Markovian so that a conditional expectation given  $\mathcal{F}_t$ , the information set generated by the past of the process until  $t$ , does not only depend on the value of the process at time t but on the whole past of  $\sigma^2$ . This is the price to pay for incorporating long-range dependence of  $\sigma^2$  in the model. Practitioners are used to computing the so-called Black–Scholes implied volatility by inversion of the Black-Scholes option pricing formula on the observed option prices. It can be checked that long-memory properties are transmitted to many approximations of implied volatilities that can be deduced from the above formula, under the assumption that there is no premium for volatility risk (so

that conditional expectations under  $\mathbb{Q}$  are the same as under the current probability measure  $\mathbb{P}$ ). Then statistical strategies can be devised by using option prices, at least to estimate  $\alpha$ , or to recover integrated volatilities.

#### References

- Backus, D.K. & Zin, S.E. (1993). Long-memory infla- $[1]$ tion uncertainty: evidence from the term structure of interest rates, Journal of Money, Credit, and Banking 3, 681-700.
- [2] Baillie, R.T., Bollerslev, T. & Mikkelsen, H.O. (1996). Fractionally integrated generalized autoregressive conditional heteroskedasticity, Journal of Econometrics 74,  $3 - 30$
- Beran, J. (1994). Statistics for long memory processes, [3] in Monographs on Statistics and applied Probability, Chapman and Hall, New York, Vol. 61.
- Bollerslev, T. & Mikkelsen, H.O. (1996). Modelling and [4] pricing long memory in stock market volatility, Journal of Econometrics 73, 151-184.
- Box, G. & Jenkins, G. (1970). Time Series Analysis: [5] Forecasting and Control, Holden Day.
- Brockwell, P.J. & Davis, R.A. (1991). Time Series: [6] Theory and Methods, 2nd Edition, Springer.
- Carmona, P., Coutin, L. & Montseny, G. (2003). [7] Stochastic integration with respect to fractional Brownian motion, Annales de l'Institut Henri Poincaré, Probability and Statistics 39, 27-68.
- [8] Cheung, Y.-W. (1993). Long memory in foreign exchange rates, Journal of Business and Economic Statistics 11, 93-101.
- Comte, F. & Renault, E. (1998). Long memory in con-[9] tinuous time stochastic volatility models, Mathematical Finance 8,  $291-323$ .
- Dahlhaus, R. (1989). Efficient parameter estimation  $[10]$ for self-similar processes, Annals of Statistics 17, 1749-1766.
- [11] Fox, R. & Taqqu, M.S. (1986). Large sample properties of parameter estimates for strongly dependent time series, Annals of Statistics 14, 517-532.
- [12] Geweke, J. & Porter-Hudak, S. (1983). The estimation and application of long memory time series models, Journal of Time Series Analysis 4, 221-238.
- [13] Giraitis, L., Leipus, R. & Surgailis, D. (2007). Recent advances in ARCH modelling, in Long Memory in Economics, edsG. Teyssière & A.P. Kirman, eds, Springer, Berlin, pp. 3-38.
- [14] Granger, C.W.J. & Joyeux, R. (1980). An introduction to long memory time series models and fractional differencing, Journal of Time Series Analysis 1, 15-29.
- [15] Hosking, J.M.R. (1981). Fractional differencing, Biometrika  $68$ , 165–176.
- [16] Hu, Y., Oksendal, B. & Sulem, A. (2003). Optimal consumption and portfolio in a Black-Scholes market

driven by fractional Brownian motion, *Infinite Dimensional Analysis Quantum Probability and Related Topics* **6**(4), 519–536.

- [17] Hull, J. & White, A. (1987). The pricing of options on assets with stochastic volatilities, *The Journal of Finance* **3**, 281–300.
- [18] Mandelbrot, B.B. & Van Ness, J.W. (1968). Fractional Brownian motions, fractional noises and applications, *SIAM Review* **10**, 422–437.
- [19] Nualart, D. (2006). Fractional Brownian motion: stochastic calculus and applications, in *Proceedings of the International Congress of Mathematicians (ICM), Madrid, Spain*, M. Sanz-Sole, J. Soria, J.L. Varona & ` J. Verdera , eds, European Mathematical Society, Zurich, ¨ Vol. III, Invited lectures, pp. 1541–1562.
- [20] Robinson, P.M. (1995). Log periodogram regression of time series with long range dependence, *Annals of Statistics* **23**, 1630–1660.

- [21] Rogers, L.C.G. (1997). Arbitrage with fractional Brownian motion, *Mathematical Finance* **7**, 95–105.
- [22] Sowell, F. (1990). The fractional unit root distribution, *Econometrica* **58**, 495–505.

# **Further Reading**

Black, F & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **3**, 637–654.

## **Related Articles**

#### **Fractional Brownian Motion**; **Multifractals**.

FABIENNE COMTE
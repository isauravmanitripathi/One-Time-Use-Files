# Multifractals

Since the early work of Mandelbrot on the fluctuations of the cotton price in the early sixties, it is well known that market price variations are poorly described by the standard geometric Brownian motion [14]. Extreme events are more probable than in a Gaussian world and volatility fluctuations are well known to be of an intermittent and correlated nature. As we discuss in this article, multifractal analysis has provided new concepts and tools to analyze market fluctuations and has inspired a particularly elegant family of models that accounts for the main observed empirical properties in a parsimonious way. These models while capturing the "heteroskedastic" nature of return fluctuations, still preserve, in some sense, the nice stability property across timescales of Brownian motion. This sharply contrasts with classical econometric models that can hardly be controlled as the timescale is changed.

#### **Multifractal Scaling**

Let  $p(t)$  be the price of some asset at time t,  $X(t) =$  $\ln[p(t)]$  and  $\delta_{\ell}X(t)$  the log return between times t and  $t + \ell$ :  $\delta_{\ell} X(t) = X(t + \ell) - X(t)$ .<sup>a</sup>  $X(t)$  will be called a *multifractal process* if, for a range of  $q$ , the order q absolute moment of  $\delta_{\ell}X(t)$  behaves as a power law when  $\ell$  varies

$$M(q,\ell) = \mathbb{E}\left[|\delta_{\ell}X|^{q}\right] \sim C_{q}\ell^{\zeta(q)}, \quad l \leq T \qquad (1)$$

where  $\mathbb{E}$ [.] stands for the mathematical expectation, the exponent  $\zeta(q)$  is a nonlinear concave function of  $q$  and  $T$  is a large characteristic timescale referred to as the *integral scale*.

The multifractal nature of market data is illustrated on the S&P 500 index in Figure 1 using traded prices sampled every 10 min. In perfect agreement with equation (1), log-log plots of  $M(q, l)$  versus  $\ell$ show linear behavior up to a scale of the order of  $T \simeq 1$  year and the so-obtained  $\zeta(q)$  spectrum (using linear regression) turns out to be well fitted by a parabolic shape. The S&P 500 future index can thus be considered, at least at this description level, as a multifractal signal. During the last decade, a lot of works have studied various market data within the framework of multifractal scaling analysis: on FX rates, commodity markets, stock markets, future markets, and emerging markets (see [2] for a review). These studies point to multifractality as a stylized feature of financial time series.

The scaling of return moments as a function of the timescale  $\ell$  is, in fact, intimately related to some selfsimilarity property of the process  $X(t)$ . A process  $X(t)$  is called *self-similar* of exponent H if it has stationary increments and if  $\forall s > 0$ .

$$\delta_{s\ell}X(st) \underset{\text{Law}}{=} s^H \delta_{\ell}X(t) \tag{2}$$

This means that the original process and a dilated version of it are statistically undistinguishable. In that case,  $M(q, \ell) \sim \ell^{qH}$  and  $\zeta(q)$  is a linear function of  $q$ . To account for multifractality (i.e., nonlinear  $\zeta(q)$ ), one can replace the deterministic factor  $s^H$  by a random one and get the stochastic self-similarity property:

$$\delta X_{s\ell}(st) \underset{\text{Law}}{=} W_s \delta X_{\ell}(t) \tag{3}$$

where  $W_s = e^{\omega_s}$  is a positive random variable independent of the process  $X$  and which law is log infinitely divisible and only depends on  $s$ . From this equation, it is easy to show that  $\zeta(q) =$  $\ln \mathbb{E}\left[e^{-q\omega_s}\right] / \ln s$ . The multifractality *strength* of the process is generally characterized by the curvature of  $\zeta(q)$ , that is, by the so-called intermittency coefficient  $\lambda^2 = -\zeta''(0)$ . The simplest nonlinear case is the lognormal model that corresponds to a parabolic  $\zeta(q)$ (i.e.,  $\omega_s$  is Gaussian).

Let us point out that the stochastic self-similarity implies (i) that the smaller the  $\ell$  is, the *fatter* the tails of the probability distribution function (PDF) of  $\delta_{\ell} X$ are and (ii) that the covariance function of  $\ln |\delta X_{\ell}|$  is slowly decreasing (up to scale  $T$ ) as the logarithm of the lag. These two features are indeed observed on most financial data as illustrated on S&P 500 future data in Figures 2 and 3.

### **Random Cascades Models**

Let us first note that, following an idea of Mandelbrot [14], if  $\theta(t)$  (referred to as the *trading time*) is a nondecreasing multifractal process satisfying equation (3) and  $B(t)$  a Brownian motion that is independent of  $\theta(t)$ , then the process

$$X(t) = B\left[\theta(t)\right] \tag{4}$$

![](_page_1_Figure_1.jpeg)

Figure 1 Multifractal Analysis of S&P 500 future index. Traded prices have been sampled every 10 min during the period 1988–1999. (a) Log-log plots of  $M(q, l)$  versus  $\ell$ for  $q = 1, 2, 3, 4, 5$ . The timescales  $\ell$  range from 10 min to 6 years. They display linear behavior up to a scale  $T \simeq 1$ year. (b)  $\zeta(q)$  spectrum obtained by linear regression of plots on the left. The plot in the inset is the parabolic nonlinear part of  $\zeta(q)$ 

is also multifractal with  $\zeta_X(q) = \zeta_\theta(q/2)$ . If we write  $\theta(t) = \int_0^t d\theta(t)$ , the multifractal random measure  $d\theta(t)$  can be seen as the instantaneous stochastic *volatility*. Consequently, multifractal models of asset returns reduce to multifractal models of volatility measures.

Discrete multiplicative cascades were first introduced in the field of empirical finance by the pioneering work of Calvet *et al.* on exchange rates volatility [15]. Their construction is a direct translation of the self-similarity property  $(3)$ . In the simplest case, the construction of  $\theta(t)$  involves a dyadic tree in a timescale  $(t, s)$  half plane. The level *n* lies at scale  $s_n = T2^{-n}$  and has  $2^n$  nodes  $\{p_{n,k}\}_{0 \le k \le 2^n}$ , which are uniformly distributed on  $[0, T]$  leading to a partition made of  $2^n$  intervals  $I_{n,k}$  of size  $s_n$ . Moreover, i.i.d. (positive) log infinitely divisible random factors  $W_{n,k}$ are associated with the nodes  $p_{n,k}$ . The cascading process starts at the integral scale  $s_0 = T$  where a measure is uniformly spread on [0, T]:  $d\theta_0(t) = dt$ . At step  $n = 1$ , the measure  $d\theta_1(t)$  is obtained from

 $d\theta_0(t)$  by multiplying its density on the interval  $I_{1,0}$ (respectively,  $I_{1,1}$ ) by the corresponding factors  $W_{1,0}$ (respectively,  $W_{1,1}$ ). At step n,  $d\theta_n(t)$  is obtained by multiplying  $d\theta_{n-1}(t)$  on each  $I_{n-1,k}$  by  $W_{n-1,k}$  leading to the representation

$$\mathrm{d}\theta_n(u) = 2^{-n} \mathrm{e}^{\sum_{i=1}^n \delta \omega_{i,u_k}} \, \mathrm{d}t \tag{5}$$

where  $W_{i,u_k} = e^{\delta \omega_{i,u_k}}$  and  $u_k$  corresponds to the integer part of  $u2^n$ . Finally, one gets  $d\theta(t) =$  $\lim_{n\to+\infty} d\theta_n(t)$ .

Grid-bounded cascades, though simple, do not provide a satisfying solution to model volatility fluctuations: (i) they involve an arbitrary fixed scale ratio, (ii) they are not built in a causal way, and (iii) they are not stationary. In their "Poisson multifractal model", Calvet and Fisher [7] get rid of (ii) and (iii), by basically replacing, for a fixed *n*, the points  $\{p_{n,k}\}_k$ by random Poisson points with intensity  $r(s_n) = s_n^{-1}$ . Barral and Mandelbrot [5] go one step further (getting rid of (i)), by replacing the points  $\{p_{n,k}\}_{n,k}$  and their associated weights  $\{W_{n,k}\}_{n,k}$  by a nonhomogeneous spatial compound Poisson process, with the compound law W and the intensity  $r(s, t) = s^{-1}$ . This construction can be generalized by replacing the compound Poisson process by an arbitrary infinitely divisible random noise  $d\omega(t, s)$  in the half plane  $(t, s)$ (with density dt ds/ $s^2$ ). Equation (4) is replaced by

$$d\theta_{s}(t) = e^{\int_{(s',t') \in C_{s}(t)} d\omega(t',s')} dt \qquad (6)$$

where  $C_s(t)$  is a cone-like domain (pointing at  $(0, t)$  and truncated below scale s). This construction [3] corresponds to the fully continuous generalization of equation (4). The limiting measure  $d\theta(t) =$  $\lim_{s\to 0} d\theta_s(t)$  is shown to be stochastic self-similar, with *exact* scaling  $(M(q, l) = C_q l^{\zeta(q)}, \forall l \leq T)$  and having none of the drawbacks  $(i)$ – $(iii)$ . Of course, the corresponding  $X(t) = B(\theta(t))$  process shares exactly the same properties, it is referred to as a *multifractal* random walk (MRW).

The "simplest" MRW model corresponds to the case W is log-normal. In that case  $d\omega(t', s')$  is a Gaussian white noise, and it can be shown that  $\theta(t)$ can be obtained directly by

$$\theta(t) = \lim_{\Delta \to 0} \int_0^t e^{2\omega_{\Delta}(u)} du \tag{7}$$

![](_page_2_Figure_1.jpeg)

**Figure 2** Continuous deformation of increment PDF's  $\delta_{\ell}X$  across scales. Standardized PDF's (in logarithm scale) at large (b) to small (a) scales. Plots have been arbitrarily shifted along the vertical axis to illustrate the tails getting fatter as the scale is going smaller. (b) same S&P 500 data as in Figure 1. The scales range from 10 min to 1 month. (a) MRW Model with  $\lambda^2 = 0.03$ ,  $\Delta = 1/16$  and  $T = 8192$ . The scales range from 16 sampling size to two integral scales. Estimation ( $\circ$ ) made from 500 MRW realizations of  $2^{17}$  sampled points. The solid line corresponds to the prediction from the largest scale using equation  $(10)$ 

where the *magnitude process*  $\omega_{\Delta}(u)$  is a stationary Gaussian process fully defined by

$$\mathbb{E}\left[\omega_{\Delta}(t)\right] = -\lambda^2 \ln\left(\frac{T}{\Lambda}\right) \tag{8}$$

$$R_{\Delta}(\tau) = \begin{cases} \lambda^{2} \left( \ln \left( \frac{T}{\Delta} \right) + 1 - \frac{\tau}{\Delta} \right), & \tau \leq \Delta \\ \lambda^{2} \ln \left( \frac{T}{\tau} \right), & \tau \in [\Delta, T] \\ 0, & \tau > T \end{cases}$$
(9)

where  $R_{\Delta}(\tau) = \mathbb{C}ov(\omega_{\Delta}(t), \omega_{\Delta}(t+\tau)).$ 

Statistical issues such as parameter estimation remain to be studied (see [18]). Calvet and Fisher [7] introduced a Markov-switching version of their

cascade model that is amenable to maximum likelihood estimation. They were the first to propose a generalized method of moments (GMMs) to estimate the parameters of their model (see also [12, 13] for discrete cascades). The log-normal MRW model is fully defined by three parameters:  $\sigma^2$  the variance of the Brownian motion,  $T$  the integral scale (decorrelation timescale of the volatility), and  $\lambda^2$  the intermittency factor, which is involved in the nonlinear part of  $\zeta_q$  (equation (8)). Since, as briefly discussed below, many of statistical moments associated with the MRW model can be analytically computed, GMM can be simply devised and all these parameters can be easily estimated [11]. We observed that for both

![](_page_3_Figure_1.jpeg)

**Figure 3** Log-volatility covariance  $C_{\omega}(\ell,\tau)$  of the S&P 500 future. (a)  $C_{\omega}(\ell,\tau)$  versus  $\tau$  for  $\tau = 10$  min. The solid line represents a fit according to the MRW model logarithmic expression. (b)  $C_{\omega}(\ell,\tau)$  versus  $\ln(\tau)$ . The MRW model predicts a linear behavior that crosses the y-axis at  $\ln(\tau) = \ln(T)$ 

the daily and intraday financial data, the correlation time  $T$  is very large (greater than one year) and the parameter  $\lambda^2$  lies in [0.02, 0.05].

### **Properties and Risk Forecasting**

As far as multifractal properties are concerned,  $X(t)$ verifies the exact stochastic self-similarity property as defined by equation  $(3)$  and therefore its moments behave exactly as a power law of the timescale  $(\ell < T)$  with a parabolic multifractal spectrum

$$\zeta(q) = q(1/2 + \lambda^2) - \frac{\lambda^2}{2}q^2 \tag{10}$$

Many other scaling laws can be computed and notably those of "*p*-volatility" correlations  $C_p(\ell, \ell)$  $\tau \equiv \mathbb{E} \left[ |\delta_{\ell} X(\tau)|^p |\delta_{\ell} X(0)|^p \right]$ . In [17], it is shown that

$$C_p(\ell,\tau) \sim K_p^2 \left(\frac{l}{T}\right)^{2\zeta_p} \left(\frac{\tau}{T}\right)^{-\lambda^2 p^2} \tag{11}$$

where the constant  $K_p$  can be computed analytically. For proofs and details, see [2, 3]. Although they did not explicitly refer to the framework of multifractal analysis, Ding and Granger [9] were the first to observe a nontrivial dependence of  $C_p(\ell,\tau)$  as a function of p. Note that when  $p \rightarrow 0$ , one recovers the logarithmic slowly decreasing of the log-volatility covariance  $C_{\omega}(\ell, \tau)$  as illustrated in Figure 3.

Equation (9) can be directly used to predict volatility. In [7], Calvet and Fisher have already shown that their cascade model provides better volatility forecasts as compared to  $GARCH(1,1)$  or Markov-switching GARCH (see also [13]). Bacry and Muzy  $[2, 4]$  have shown that linear volatility forecast provided by the MRW model outperforms  $GARCH(1,1)$  models.

Actually, the MRW model allows to estimate the full (conditional) return probability density function at all time horizons and scales. Very much like standard Brownian motion that is stable with respect to time aggregation, the self-similarity properties of the MRW process *X(t)* allows to control how the return probability law changes when varying the timescale. Indeed, it can be shown that, in a good approximation, when *λ*<sup>2</sup> 1, the returns of the MRW process, can be written, in law, as

$$\delta_{\ell}X(t) \underset{\text{Law}}{\simeq} \epsilon_{\ell}(t) \mathrm{e}^{\Omega_{\ell}(t)} \tag{12}$$

(see [4] for details and for the precise meaning of the symbol ) for all *-* ≤ *T* , where  is a Gaussian white noise of variance *σ*<sup>2</sup> and the process *-(t)* is the *renormalized magnitude*. It is a stationary Gaussian process whose mean and covariance are very similar to equation (7). In Figure 2, we see that, as observed for S&P 500 data, the MRW returns PDF strongly depends on the timescale and evolves from a "quasi-Gaussian" shape at large scales (*- T* ) to PDF's with high kurtosis at small scales. Even if the precise shape of the PDF tails returns is a matter of debate, the most commonly admitted form is a power law with a tail exponent *µ* within the interval [3*,* 5] (see, e.g., [6, 10]). The MRW model allowed to point out [1, 16] that this behavior is strongly related to the choice of the asymptotics in the estimation process. The "high-frequency asymptotics" (sampling frequency going to infinity) has to be distinguished from the "long duration asymptotics" (duration of the considered time period going to infinity).

All previous considerations can be extended to conditional laws and can be of practical interest for VaR forecasting. As shown in [2, 4], MRW predictions of VaR at various time horizons can be more reliable than predictions based on a GARCH(1,1) model.

## **End Notes**

a*.* We do not address here the modeling of intraday modulation of the data. This modulation can be removed following [8]. We consider that *δ-X(t)* is stationary and has zero mean.

## **References**

- [1] Bacry, E., Gloter, A., Hoffmann, M. & Muzy, J.F. (2009). Multifractal analysis in a mixed asymptotic framework, *Annals of Applied Probability* Preprint, arXiv.org/math/0805.0194. To appear.
- [2] Bacry, E., Kozhemyak, A. & Muzy, J.F. (2008). Continuous cascade models for asset returns, *Journal of Economic Dynamics and Control* **32**, 156–199.

- [3] Bacry, E. & Muzy, J.F. (2003). Log-infinitely divisible multifractal process, *Communications in Mathematical Physics* **236**, 449–475.
- [4] Bacry, E., Kozhemyak, A. & Muzy, J.F. (2009). Log-normal continuous cascades: aggregation properties and estimation, *Quantitative Finance* Preprint, arXiv.org/physics/0804.0185. To appear.
- [5] Barral, J. & Mandelbrot, B.B. (2002). Multifractal products of cylindrical pulses, *Probability Theory and Related Fields* **124**, 409–430.
- [6] Bouchaud, J.P. & Potters, M. (2003). *Theory of Financial Risk and Derivative Pricing*, Cambridge University Press, Cambridge.
- [7] Calvet, L. & Fisher, A. (2004). How to forecast long-run volatility, *Journal of Financial Econometrics* **2**, 49–83.
- [8] Dacorogna, M.M., Gen¸cay, R., Muller, U.A., Olsen, R.B. ¨ & Pictet, O.V. (2001). *An introduction to High Frequency Finance*, Academic Press, San Diego.
- [9] Ding, Z. & Granger, C.W.J. (1996). Modeling volatility persistence of speculative returns: a new approach, *Journal of Econometrics* **73**, 185–215.
- [10] Gopikrishnam, P., Meyer, M., Amaral, L.A.N. & Stanley, H.E. (1998). Inverse cubic law for the distribution of stock price variations, *The European Physical Journal B* **3**, 139–140.
- [11] Lastwave gnu software, (2008). www.cmap. polytechnique.fr/∼bacry/LastWave
- [12] Lux, T. (2001). Turbulence in financial markets, *Quantitative Finance* **1**, 632.
- [13] Lux, T. (2004). *The Markov-Switching Multi-Fractal Model of Asset Returns*, Economic, University of Kiel, working paper.
- [14] Mandelbrot, B.B. (1997). *Fractals and Scaling in Finance. Discontinuity, Concentration, Risk*, Springer, New York.
- [15] Mandelbrot, B.B., Calvet, L. & Fisher, A. (1997). *The Multifractal Model of Asset Returns*, Preprint, Cowles Foundation Discussion paper 1164.
- [16] Muzy, J.F., Bacry, E. & Kozhemyak, A. (2006). Extreme values and fat tails of multifractal fluctuations, *Physical Review E* **73**, 066114.
- [17] Muzy, J.F., Delour, J. & Bacry, E. (2000). Modelling fluctuations of financial time series, *European Journal of Physics B* **17**, 537–548.
- [18] Ossiander, M. & Waymire, E.C. (2000). Statistical estimation for multiplicative cascades, *The Annals of Statistics* **28**, 1533–1560.

## **Further Reading**

- Kahane, J.P. & Peyriere, J. (1976). Sur certaines martingales de ` Benoˆit Mandelbrot, *Advances in Mathematics* **22**, 131–145.
- Molchan, G.M. (1996). Scaling Exponents and Multifractal Dimensions for independent random cascades, *Communications in Mathematical Physics* **179**, 681–702.

EMMANUEL BACRY & JEAN-FRAN MUZY
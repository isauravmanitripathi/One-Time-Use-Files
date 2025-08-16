# **Stochastic Volatility Models: Foreign Exchange**

In finance, the term *volatility* has a dilative meaning. There exists a definition in the statistical sense, which states that volatility is the standard deviation per unit time (usually per year) of the (logarithmic) asset returns. However, empirical evidence about derivatives markets shows that refinements of this definition are necessary.

First, one can observe a dependency of Black–Scholes-implied volatility on at least the strike price and time to maturity implicit in option prices. This dependency defines the **implied volatility surface**. One possibility to incorporate this dependency into a model is by using a deterministic function for the instantaneous volatility, that is, the volatility governing the changes in spot returns in infinitesimal time steps. This function of spot price and time is called *local volatility* (*see* **Local Volatility Model**).

In addition, empirical evidence indicates that the local volatility surface is not constant over time, but is subject to changes. This is not surprising since the expectations of the market participants with respect to the future instantaneous volatility might change over time. Furthermore, for some derivative products, the dynamics of the volatility surface is crucial for a reliable valuation. A prominent example is the product class of cliquet options, which are basically a collection of forward start options with increasing forward start time. The payoff depends on the absolute or the relative performance of the underlying during the lifetime of the options. It is intuitive that an option with a forward start time of one year, for instance, depends substantially on the one-year forward volatility surface. Since this volatility is uncertain, it seems advisable to model this risk by an additional stochastic factor.

## **Stochastic Volatility FX Models**

Now, we review some common procedures for incorporating a stochastic behavior of volatility into foreign exchange (FX) rate models. The first approach is to model the FX rate *Xt* with a volatility process *vt* by a system of stochastic differential equations, like

$$dX_t = \mu_t X_t dt + \sigma_t X_t dW_t^X$$
  

$$dv_t = \eta(v_t) dt + \zeta(v_t) dW_t^v$$
 (1)

where *vt* = *f (σt)* for a function *f* and the increments of the Brownian motions *W<sup>X</sup>* and *W<sup>v</sup>* are possibly correlated. Table 1 gives an overview of some common stochastic volatility models.

A general class of stochastic volatility models is formed by the affine jump diffusion models. They have been studied by Duffie *et al.* [5]. The Heston model is a special case of this kind of model.

The second approach is inspired by the observation that higher volatility comes along with an increased trading activity and *vice versa*. This is realized by a time change in the FX rate process. For instance, consider a standard Brownian motion {*Wt*}*t*≥<sup>0</sup> with variance *t* for *Wt* , that is, the value of the process after *t* units of physical time. Now, if the economic time elapses twice as fast as the physical time due to market activity, the process could be expressed by the deterministically time-changed process {*W*2*<sup>t</sup>*}*t*<sup>≥</sup>0. Hence, the variance for the values of the process after *t* units of physical time would then be 2*t*. This idea can be generalized by representing the economic time as a stochastic process *Yt* , which is named *stochastic clock*. For every realization of the process {*Yt*}*t*<sup>≥</sup>0, economic time must be a monotone function of physical time, that is, the process is a subordinator. Recently proposed models use a normal inverse gamma or variance gamma Levy process for representing the exchange ´ rate process and an integrated Cox– Ingersoll–Ross or Gamma–Ornstein–Uhlenbeck process for stochastic time. All these models have the common feature that the characteristic function of the logarithm of the time-changed exchange rate, ln *XYt* , can be expressed in closed form.

Besides the models mentioned here, there exist other modeling approaches. For a general overview of stochastic volatility models, see [6, 11] and for especially in the FX context see [12].

## **Heston's Stochastic Volatility Model**

In the following, we discuss the stochastic volatility model of Heston and its option valuation applied to

| $f(\sigma_t)$ | $\n\eta(v_t) \qquad \zeta(v_t)\n$ | Reference                                                                                                                                                                                                                                                          |
|---------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               |                                   | $\sigma_t^2$ $\kappa(\theta - v_t)$ $\xi v_t$ GARCH similar diffusion<br>model $[11]$                                                                                                                                                                              |
|               |                                   | $\begin{array}{lll} \sigma_t^2 & \kappa(\theta - v_t) & \xi \sqrt{v_t} & \text{Heston model } [ \\ \sigma_t^2 & \kappa(\theta v_t - v_t^2) & \xi v_t^{3/2} & 3/2 \text{ model } [11] \end{array}$<br>$\kappa(\theta - v_t) \qquad \xi \sqrt{v_t}$ Heston model [9] |
|               |                                   |                                                                                                                                                                                                                                                                    |
|               |                                   | $\ln \sigma_t^2$ $\kappa(\theta - v_t)$ $\xi$ Log-volatility<br>Ornstein–Uhlenbeck [11]                                                                                                                                                                            |

**Table 1** Some common stochastic volatility models

an FX setting. The model is characterized by the stochastic differential equations:

$$\begin{aligned} \mathrm{d}X_t &= (r_d - r_f) X_t \mathrm{d}t + \sqrt{v_t} X_t \mathrm{d}W_t^X \\ \mathrm{d}v_t &= \kappa (\theta - v_t) \mathrm{d}t + \sigma \sqrt{v_t} \mathrm{d}W_t^v \end{aligned} \tag{2}$$

with  $\text{Cov}\left[\text{d}W_t^X, \text{d}W_t^v\right] = \rho \text{d}t$ . Here, the FX rate process  $\{X_t\}_{t\geq 0}$  is modeled by a process, similar to the geometric Brownian motion, but with a nonconstant instantaneous variance  $v_t$ . The variance process  $\{v_t\}_{t>0}$  is driven by a mean-reverting stochastic square-root process. The increments of the two Wiener processes  $\{W_t^X\}_{t>0}$  and  $\{W_t^v\}_{t>0}$  are assumed to be correlated with rate  $\rho$ . In an FX setting, the risk-neutral drift term of the underlying process is the difference between the domestic and the foreign interest rates  $r_d - r_f$ . The quantities  $\kappa \ge 0$  and  $\theta \ge 0$  denote the rate of mean reversion and the longterm variance. The parameter  $\sigma$  is often called *vol of* vol, but it should be called volatility of instantaneous variance.

The term  $\sqrt{v_t}$  in equation (2) ensures a nonnegative volatility in the FX rate process. It is known that the distribution of values of  $\{v_t\}_{t\geq 0}$  is given by a noncentral chi-squared distribution. Hence, the probability that the variance takes a negative value is equal to zero. Thus, if the process touches the zero bound, the stochastic part of the volatility process turns zero and the deterministic part will ensure a nonnegative volatility because of the positivity of  $\kappa$  and  $\theta$ .

The Heston model is often not capable of fitting complicated structures of implied volatility surfaces. In particular, this is true if the term structure exhibits a nonmonotone form or the sign of the skew changes with increasing maturity. For a discussion of the implied volatility surface generated by this model, see [7]. One approach to tackle this limitation is to extend the original Heston model by time-dependent parameters [3, 14].

#### Valuation of Options in the Heston Model

For the valuation of options in the Heston model, we consider the value function of a general contingent claim  $V(t, v, X)$ . As shown in [8], applying Itô's lemma, the self-financing condition, and the possibility to trade in the underlying exchange rate, money market, and another option, which is dependent on time, volatility, and  $X$ , we arrive at Garman's partial differential equation:

$$\frac{\partial V}{\partial t} + \kappa (\theta - v) \frac{\partial V}{\partial v} + (r_d - r_f) X \frac{\partial V}{\partial X} + \frac{1}{2} \sigma^2 v \frac{\partial^2 V}{\partial v^2}$$
$$+ \frac{1}{2} v X^2 \frac{\partial^2 V}{\partial X^2} + \rho \sigma v X \frac{\partial^2 V}{\partial v \partial X} - r_d V = 0$$
(3)

A solution to the above equation can be obtained by specifying appropriate boundary and exercise conditions, which depend on the contract specifications. In the case of European vanilla options, Heston [9] provided a closed-form solution, namely,

$$\text{Vanilla} = \phi \left[ e^{-r_f \tau} X_t P_1 - K e^{-r_d \tau} P_2 \right] \tag{4}$$

where  $\tau = T - t$  is the time to maturity,  $\phi = \pm 1$  is the call-put indicator and  $K$  is the strike price. The quantities  $P_1$  and  $P_2$  define the probability that the exchange rate  $X$  at maturity is greater than  $K$  under the spot and the risk-neutral measure, respectively. The spot delta of the European vanilla option is equal to  $\phi e^{-r_f \tau} P_1$ .

Assuming that the distribution of  $\ln X_T$  at time  $t$  under the two different measures is determined uniquely by its characteristic function  $\varphi_j$ , for  $j =$ 1, 2, it is shown, in [15], that  $P_1$  and  $P_2$  can be expressed in terms of the inverse Fourier transformation

$$P_{j} = \frac{1}{2} + \frac{1}{\pi} \phi \int_{0}^{\infty} \Re \left[ \frac{\exp(-\mathrm{i}u \ln K) \varphi_{j}(u)}{\mathrm{i}u} \right] du \tag{5}$$

The integration in equation  $(5)$  can be done using numerical integration methods such as Gauss–Laguerre integration or fast Fourier transform approximation. In [10], it is shown that the computational time of the fast Fourier transform approach to compute vanilla option prices is higher compared to a numerical integration method with certain caching techniques.

The characteristic function is exponentially affine and available in closed form as

$$\varphi_2(u) = \exp\left(B(u) + A(u)v_t + \mathrm{i}u\ln X_t\right) \quad (6)$$

The functions  $A$  and  $B$  arise as the solution of the so-called Riccati differential equations as shown in [8]. They are defined as follows:

$$A(u) = -iu(1 - iu)\frac{(1 - e^{-d(u)\tau})}{\gamma(u)}$$
(7)

$$B(u) = iu(r_d - r_f)\tau$$
  
+  $\frac{\kappa\theta}{\sigma^2}(\kappa - iu\rho\sigma - d(u))\tau + \frac{2\kappa\theta}{\sigma^2}\ln\frac{2d(u)}{\gamma(u)}$   
(8)

 $d(u) = \sqrt{(\rho \sigma i u - \kappa)^2 + i u \sigma^2 (1 - i u)}$  and with  $\gamma(u) = d(u) \left( 1 + e^{-d(u)\tau} \right) + (\kappa - iu\rho\sigma) \left( 1 - e^{-d(u)\tau} \right).$ The characteristic function  $\varphi_1$  has the same form as the function  $\varphi_2$ , but with u replaced by  $u - i$  and multiplied by a factor  $\exp(-(r_d - r_f)\tau - X_0)$ . This is due to the change from the spot to the risk-neutral measure in the derivation of  $\varphi_1$ .

There exist several different representations of the characteristic function  $\varphi$ . In some formulations of  $\varphi$ , the characteristic function can become discontinuous if the multivalued complex logarithm contained in the integrand is restricted to the calculation of its principal branch, as is the case in many implementations. Wrong results of the value  $P_i$  may occur unless a rotation count algorithm is employed. For other representations of  $\varphi$ , stability for all choices of model parameters can be proved. Details can be found in  $[1]$ .

Besides vanilla options, closed-form solutions for exotic options have been found for the volatility option, the correlation option, the exchange option, the forward start option, the American option, the discrete barrier option, and others. Numerical pricing of exotic options in the Heston model can be carried out by using conventional numerical methods such as Monte Carlo simulation [2, 13], finite differences [8], or an exact simulation method [4].

#### Calibration of Heston's Model

We realize the estimation by fitting the Heston model parameters to the smile of the current vanilla option market. Thereby, the choice of the loss function to minimize the differences between the model and market Black-Scholes-implied volatilities is crucial. Here, we decide to do a least-squared error fit over absolute values of volatilities, rather than minimizing over relative volatilities or option values.

For a fixed time to maturity  $\tau$ , given marketimplied volatilities  $\sigma_1^{\text{market}}, \ldots, \sigma_n^{\text{market}}$  and corresponding spot delta (premium unadjusted) values  $\Delta_1, \ldots, \Delta_n$ , the calibration is set up as follows:

1. Before starting the optimization, we determine the strikes  $K_i$  corresponding to  $\sigma_i^{\text{market}}$  with

$$K_{i} = X_{0} \exp\left\{-\phi N^{-1} (\phi e^{r_{f}\tau} \Delta_{i}) \sigma_{i}^{\text{market}} \sqrt{\tau} + \left(r_{d} - r_{f} + \frac{1}{2} (\sigma_{i}^{\text{market}})^{2}\right) \tau\right\} \quad 1 \leq i \leq n$$
(9)

which requires the inversion of the cumulative normal distribution function  $N$ .

- The aim is to minimize the objective function  $M$ 2. defined below. We repeat the steps  $(a)-(c)$  until a certain accuracy in the optimization routine is achieved.
  - We use the analytic formula in equation a (4) to calculate the vanilla option values in the Heston model for the strikes  $K_1, \ldots, K_n$ :

$$H_i(\kappa, \sigma, \theta, \rho, v_0)$$
  
= Vanilla( $\kappa, \sigma, \theta, \rho, v_0$ , market data,  
 $K_i, \phi$ ) (10)

For  $i = 1, \ldots, n$ , we compute all option h. values  $H_i$  in terms of  $Black-$ Scholes-implied volatilities  $\sigma_i^{\text{model}}(\kappa, \sigma, \theta,$  $\rho$ ,  $v_0$ ) by applying a root search.

The objective function is given as c.

$$M(\kappa, \sigma, \theta, \rho, v_0)$$
  
=  $\sum_{i=1}^{n} w_i \big[ \sigma_i^{\text{market}} - \sigma_i^{\text{model}}(\kappa, \sigma, \theta, \rho, v_0) \big]^2$   
+ *penalty* (11)

The implementation of a penalty function  $penalty$ and some weights  $w_i$  may give the calibration routine some additional stability. There exist various choices for the penalty function. For example, in [14], it is suggested to penalize the retraction from the initial set of model parameters, but we may also use the penalty to introduce further constraints such as the condition  $2\kappa\theta - \sigma^2 > 0$  to ensure that in subsequent simulations the volatility process cannot sojourn in zero. In addition, we could use the weights  $w_i$  to favor at-the-money (ATM) or out-of-the-money fits.

For the minimization, a great variety of either local or global optimizers in multidimensions could be used. Algorithms of Levenberg-Marquardt type are frequently used, because they utilize the leastsquares form of the objective function. Since the objective function is usually not convex, there may exist many local extrema and the use of a computationally more expensive global (stochastic) algorithm, such as simulated annealing or differential evolution, in the calibration routine may be considered. From a practical point of view, taking the value of a short-dated implied volatility as an initial value for  $v_0$  is a good start for the calibration. In light of parameter stability, the result of the previous (the day before) calibration could be used as an initial guess for the remaining parameters. Furthermore, to enhance the speed of calibration, it is suggested in [8] to fix the model parameter  $\kappa$  and run the calibration in only four dimensions, since the influence of the mean reversion is often compensated by a stronger volatility of variance  $\sigma$ . To ensure that the correlation parameter  $\rho$  attains values in  $[-1, 1]$ , we reparametrize with the function  $2 \arctan(\rho)/\pi$ .

### Hedging

If volatility is introduced as a stochastic factor but cannot be traded, the market is incomplete. By

the introduction of a tradable market instrument  $U(t, v, X)$ , which depends on the volatility, the market can be completed and volatility risk can be hedged dynamically. In the Heston model, to make a portfolio containing the contingent claim  $V(t, v, X)$ instantaneously risk free, the hedge portfolio has to consist of  $\Delta_X$  units of the foreign currency and  $\Delta_U$  units of the contingent claim  $U(t, v, X)$ , with

$$\Delta_X = \frac{\partial V}{\partial X} - \Delta_U \frac{\partial U}{\partial X} \quad \text{and} \quad \Delta_U = \frac{\partial V/\partial v}{\partial U/\partial v} \quad (12)$$

Common FX market instruments applicable for market completion and hedging are, on the one hand, ATM forward plain vanilla options for different maturities. On the other hand, for most of the FX markets risk reversals (RR) and butterflies (BF) are traded for certain maturities and strikes. These instruments are defined as<sup>a</sup>

$$RR(T, \Delta) = Call(T, K_{\Delta}) - Put(T, K_{-\Delta}) \qquad (13)$$
$$BF(T, \Delta) = \frac{1}{2} \Big( Call(T, K_{\Delta}) + Put(T, K_{-\Delta}) \Big)$$
$$- Call(T, K_{ATM}) \qquad (14)$$

where  $K_{\Delta}$  is the strike as given in equation (9), such that the corresponding plain vanilla option has a Black–Scholes delta of  $\Delta$ .  $K_{\text{ATM}}$  denotes the ATM strike, which is often taken to be the strike generating a zero delta for a straddle in FX markets. Risk reversals and butterflies are quoted in Black-Scholesimplied volatilities instead of prices, that is, if  $\nu_{\Lambda}$ denotes the implied volatility of a call with strike  $K_{\Delta}$  (analogously,  $\nu_{-\Delta}$  for puts and  $\nu_{\text{ATM}}$ ), the FX smile quotes are

$$\nu_{\rm RR} = \nu_{\Delta} - \nu_{-\Delta} \quad \text{and} \quad \nu_{\rm BF} = \frac{1}{2} (\nu_{\Delta} + \nu_{-\Delta}) - \nu_{\rm ATM}$$
(15)

Since individual ATM options are liquidly traded, and therefore  $\nu_{ATM}$  is known, the volatilities  $\nu_{\Delta}$  and  $v_{-\Delta}$  can be calculated from  $v_{\rm RR}$  and  $v_{\rm BF}$ .

The quantities  $v_{RR}$  and  $v_{BF}$  relate to the skew and smile, respectively, of the implied volatility surface. This is schematically illustrated for  $\Delta = 0.25$  in Figure 1.

![](_page_4_Figure_0.jpeg)

Figure 1 The meaning of  $v_{RR}$  and  $v_{BF}$  in the context of the implied volatility curve for a fixed maturity

#### Example

In this section, we give an example of the difference between Heston and Black-Scholes option prices. Thereby, we consider discrete down-and-out put options written on the USD/JPY exchange rate. The option holder receives a vanilla put option payoff at maturity in 18 months as long as the FX rate does not fall below a given barrier  $B$  at the barrier fixing times in 6, 12, and 18 months. Otherwise, the option expires worthless. We compare ATM option prices for barriers of 10%, 50%, 60%, 70%, 80%, and 90% of the spot price.

For the valuation in the Heston model, we calibrate to European plain vanilla options with maturities of 1, 2, 3, 6, 9, 12, and 24 months and strikes with respect to  $10\%\Delta$  put,  $25\%\Delta$  put, ATM,  $10\%\Delta$  call, and  $25\% \Delta$  call for May 21, 2009 (Figure 2). The weights are set to 1 for ATM strikes, to 0.75 for  $25\%\Delta$ strikes, and to 0.25 for  $10\% \Delta$  strikes, since usually options with strikes far from the ATM forward are less liquidly traded. Figure  $2(a)$  demonstrates that the market-implied volatilities (dots) are adequately matched by the calibrated model volatilities (circles connected by lines). Figure  $2(b)$  shows the term structure of market-implied volatilities (dots) and calibrated implied volatilities (circles) for strikes with respect to 25% $\Delta$  call, ATM, and 25% $\Delta$  put (from

![](_page_4_Figure_7.jpeg)

Figure 2 Implied volatilities of the Heston model fitted to market volatilities for USD/JPY with maturities of 1, 2, 3, 6, 9, 12, and 24 months and strikes for  $10\% \Delta$  and  $25\% \Delta$  put, ATM,  $10\% \Delta$ , and  $25\% \Delta$  call. The dots show the market volatilities and the circles the calibrated volatilities. (a) The whole volatility surface. (b) The implied volatility term structure for strikes  $25\%\Delta$  call, ATM, and  $25\%\Delta$  put (from bottom to top)

| Barrier (% of spot)     | 90               | 80               | 70               | 60               | 50               | 10               |  |  |  |
|-------------------------|------------------|------------------|------------------|------------------|------------------|------------------|--|--|--|
| Black–Scholes<br>Heston | 0.8752<br>0.6309 | 3.7068<br>1.8723 | 5.7670<br>3.1830 | 6.2663<br>4.3376 | 6.3000<br>5.2202 | 6.3012<br>6.3023 |  |  |  |

**Table 2** Down-and-out put values with at-the-money strike and discrete monitoring at 6, 12, and 18 months

The value of the corresponding plain vanilla put in the Heston model is given by 6.3060

bottom to top). The resulting model parameters are given by *κ* = 0*.*2170, *θ* = 0*.*0444, *σ* = 0*.*3410, *ρ* = −0*.*5927, and *v*<sup>0</sup> = 0*.*0228.

As mentioned in the section Valuation of Options in the Heston Model, there exists a value function in (semi-) closed form for discrete barrier options in the Heston model. The distribution of the random variables ln *Xti* at the barrier fixing times *ti* can be determined uniquely by the derivation of their joint characteristic function and with the application of Shephard's theorem given in [15] the required knock-out probabilities can be computed.

For the valuation in the Black–Scholes model, we use the interpolated ATM forward-implied volatility for plain vanilla options with a maturity of 18 months, which is *σ*BS = 0*.*1270 in our example.

Finally, the FX spot trades at *X*<sup>0</sup> = 94*.*43, and the domestic and foreign interest rates for 18 months are given by *rd* = 0*.*0065 and *rf* = 0*.*0139. The resulting prices for the described options are shown in Table 2.

Comparing the prices, we can observe two effects. First, the Heston prices are lower than the corresponding Black–Scholes prices. This behavior might be in major part due to the fact that the Black–Scholes valuation uses a flat volatility, whereas the Heston model incorporates the whole volatility smile. Since the volatilities below the ATM strikes increase substantially (Figure 2), the knock-out probabilities also increase and the option prices drop. Second, the prices of Heston and Black–Scholes converge with decreasing barrier level. This appears reasonable, since the likelihood of a knock-out decreases more and more and the valuation finally results in put prices, which should be equal for both models in the case of a good calibration fit.

## **End Notes**

a*.* There exist different definitions for risk reversals and butterflies in the literature with respect to sign and coefficients.

## **References**

- [1] Albrecher, H., Mayer, P., Schoutens, W. & Tistaert, J. (2007). *The Little Heston Trap*, Wilmott No. 1, pp. 83–92.
- [2] Andersen, L. (2007). *Efficient Simulation of the Heston Stochastic Volatility Model*. Working paper. Available at SSRN: http://ssrn.com/abstract=946405
- [3] Benhamou, E., Gobet, E. & Miri, M. (2009). *Time Dependent Heston Model*. Working paper. Available at SSRN: http://ssrn.com/abstract=1367955.
- [4] Broadie, M. & Kaya, O. (2006). Exact simulation of stochastic volatility and other affine jump diffusion models, *Operations Research* **54**(2), 217–231.
- [5] Duffie, D., Singleton, K. & Pan, J. (2000). Transform analysis and asset pricing for affine jump-diffusions, *Econometrica* **68**, 1343–1376.
- [6] Fouque, J.P., Papanicolaou, G. & Sircar, K.R. (2000). *Derivatives in Financial Markets with Stochastic Volatility*, Cambridge University Press.
- [7] Gatheral, J. (2006). *The Volatility Surface*, Wiley.
- [8] Hakala, J. & Wystup, U. (2002). *Foreign Exchange Risk*, Risk Publications.
- [9] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–343.
- [10] Kilin, F. (2007). *Accelerating the Calibration of Stochastic Volatility Models*. Working Paper. Available at SSRN: http://ssrn.com/abstract=965248
- [11] Lewis, A.L. (2000). *Option Valuation under Stochastic Volatility*, Finance Press.
- [12] Lipton, A. (2001). *Mathematical Methods for Foreign Exchange*, World Scientific.
- [13] Lord, R., Koekkoek, R. & van Dijk, D. (2006). *A Comparison of Biased Simulation Schemes for Stochastic Volatility Models*. & Working Paper. Available at SSRN: http://ssrn.com/abstract=903116
- [14] Nogel, U. & Mikhailov, S. (2003). Heston's Stochastic ¨ Volatility Model. Implementation, Calibration and some Extensions, *Wilmott* Juli, 74–49.
- [15] Shephard, N.G. (1991). From characteristic function to distribution function, *Econometric Theory* **7**(4), 519–529. Cambridge University Press.
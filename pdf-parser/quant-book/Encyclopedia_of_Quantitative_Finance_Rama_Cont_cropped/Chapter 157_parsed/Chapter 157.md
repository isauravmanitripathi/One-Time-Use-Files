# **Regime-switching Models**

Many financial time series exhibit sudden changes in the structure of the data-generating process. Examples include financial crises, exchange rate swings, and jumps in the volatility. Sometimes, this sudden switch is due to a change in policy, for example, when moving from a fixed to a floating exchange rate regime. In other cases, the behavior of the series is influenced by an exogenous fundamental variable, such as the current position on the business or the credit cycle.

Regime-switching models attempt to capture this behavior by allowing the data-generating process to change in time, depending on an underlying, discrete but unobserved state variable. Typically, the functional form of the data-generating process remains the same across the different regimes with only the parameter values being state-dependent, as, for example, in a random walk equity return model where the drift and volatility change with the regime. However, it is feasible to set up models where the data-generating process itself changes, for example, moving from a deterministic fixed exchange to a stochastic floating one.

From a statistical point of view, regime-switching models will produce mixtures of distributions (*see* **Mixture of Distribution Hypothesis**), offering a very stylized and intuitive way of accommodating features such as fat tails, skewness, and volatility clustering (*see* **Stylized Properties of Asset Returns**). It is very easy to calibrate regimeswitching models on historical data using maximum likelihood techniques, implementing what can be thought of as a discrete version of the Kalman filter (*see* **Filtering**). Virtually all economic and financial time series have been analyzed under the regime-switching framework, including interest and exchange rates, equity returns, commodity prices, energy prices, and credit spreads.

Derivative prices can be computed for regimeswitching models by using transform methods (*see* **Hazard Rate**). The characteristic function of a regime-switching process can be computed in closed form if the characteristic functions conditional on each regime are available. This makes such processes a viable alternative to the stochastic volatility models, where one has to also resort to transform methods for pricing.

# **The Regime-switching Framework**

A regime-switching model can be cast in either a discrete or continuous time setting. The model is built conditional to a Markov chain *s(t)*, the realization of which is not directly observed by economic agents. The chain can take a discrete set of values, and here we label them as *s(t)* ∈ {1*,* 2*,...,N*} = *S* . The Markov chain is determined by its transition probability matrix in discrete time or its rate matrix in continuous time. In particular, in a discrete time setting, we write the transition probabilities *pi,j*

$$P[S(t+1) = j | S(t) = i] = p_{i,j} \tag{1}$$

and we collect the elements {*pi,j* } in the transition probability matrix **P**. The columns of **P** must sum up to 1, and all transition probabilities must be nonnegative. For a continuous time process, we define the transition rates *qi,j* :

$$P[S(t + dt) = j | S(t) = i] = \mathbf{1}(i = j) + q_{i,j}dt \quad (2)$$

where **1** is the indicator function. The elements {*qi,j* } are collected in the rate matrix **Q**. Note that by this definition, the columns of the rate matrix must sum up to 0, and the diagonal elements will be negative. The infinitesimal transition probability matrix is given as

$$\mathbf{P}(\mathrm{d}t) = \mathbf{I} + \mathbf{Q}\mathrm{d}t \tag{3}$$

where **I** is the unit *(N* × *N )* matrix.

At each point in time, the data-generating process will vary, according to the regime *s(t)* that prevails at that time. Thus, for a discrete time process, we can write

$$x(t) = g[t, s(t), \mathbf{y}(t), \epsilon(t); \boldsymbol{\beta}] \tag{4}$$

In the above expression, **y***(t)* includes variables known at time *t*, including exogenous variables and lagged values of *x(t)*, and *(t)* represents the error term. In continuous time, we can write the stochastic differential equation:

$$dx(t) = \mu[t, s(t), \mathbf{y}(t); \boldsymbol{\beta}]dt$$
  
+  $\sigma[t, s(t), \mathbf{y}(t); \boldsymbol{\beta}]dB(t)$  (5)

Again, **y***(t)* can include exogenous variables and the history of *x(t)*, while now *B(t)* is a standard Brownian motion. The above equation can be extended to a multidimensional setting and can be generalized to include jumps or Levy ´ processes.

A standard simple example is a regime-dependent random walk process, where

$$\Delta x(t) = \mu \left[ s(t) \right] + \sigma \left[ s(t) \right] \epsilon(t) \text{ in discrete time}$$
  
$$dx(t) = \mu \left[ s(t) \right] dt + \sigma \left[ s(t) \right] dB(t)$$
  
in continuous time (6)

The parameter set in this example is  $\beta = {\mu(1)}$ .  $\sigma(1), \mu(2), \sigma(2), \ldots, \mu(N), \sigma(N)$ .

#### **Estimation from Historical Data**

Given a set of historical values, the parameter vector  $\beta$  can be calibrated using maximum likelihood. As data are available over a discrete time grid, we focus on the calibration of the discrete time model. We give the switching random walk model with Gaussian noise as an example, but it should be straightforward to generalize this to more complex structures.

We denote the conditional density of  $x(t)$ by  $f_t(x|j) = P[x(t) \in dx | s(t) = j]$ , given that the underlying Markov chain is in state  $j$ . In our example, this is a Gaussian density, with mean  $\mu(j)$  and variance  $\sigma^2(j)$ . In addition, for future reference, we define the vector of conditional probabilities  $\xi(t|t')$ , with elements

$$\boldsymbol{\xi}(t|t') = \{ \mathbf{P}[S(t) = j|\mathscr{F}(t')] \}_{j \in \mathscr{S}} \tag{7}$$

An important component of the calibration procedure is the vector of filtered probabilities  $\boldsymbol{\xi}_{t|t}$ .

Given the parameter set  $\beta$ , the filtered probabilities can be computed based on the following recursion:

- Assume that the filtered probabilities are available up to time  $t$ .
- Compute the forecast probabilities  $\xi(t+1|t) =$  $\mathbf{P}\boldsymbol{\xi}(t|t)$ .
- The Bayes theorem yields the filtered probability:

- The numerator of the above expression is the . product of the conditional density with the forecast probability for each state.
- The denominator, which is the sum of all numerators computed in the previous step, is also the conditional density of  $P[x(t+1) \in dx | \mathcal{F}(t)]$ . This is the likelihood function of the observation  $x(t + 1)$ .

In the Kalman filtering terminology, the above computation can be compactly written in two steps:

Prediction: 
$$\boldsymbol{\xi}(t+1|t) = \mathbf{P}\boldsymbol{\xi}(t|t)$$
 (9)

Correction: 
$$\boldsymbol{\xi}(t+1|t+1)$$
  
=  $\frac{\mathbf{f}(t+1) \odot \boldsymbol{\xi}(t+1|t)}{t' \cdot (\mathbf{f}(t+1) \odot \boldsymbol{\xi}(t+1|t))}$  (10)

The vector  $\mathbf{f}(t)$  above collects the conditional distributions, across all possible regimes. In the Gaussian regime-switching model, the elements of  $\mathbf{f}(t)$  would have the following elements:

$$\mathbf{f}(t) = \left\{ \frac{1}{\sqrt{2\pi}\sigma(j)} \exp\left(-\frac{(x(t) - \mu(j))^2}{2\sigma^2(j)}\right) \right\}_{j \in \mathscr{S}} \tag{11}$$

The symbol " $\odot$ " denotes element-by-element multiplication, and  $\iota$  is an  $(N \times 1)$  vector of ones.

More details on estimation methods can be found in [18]. A small sample of the vast number of empirical applications that utilize the regime-switching framework is provided in [3, 15, 17, 19, 23, 27]. Generalizations include time-varying transition probabilities that depend on explanatory variables [14], switching generalized autoregressive conditionally heteroskedastic (GARCH)-type processes [16, 20], and models that resemble a multifractal setting [6]. A Bayesian alternative to maximum likelihood is sought in [1].

$$\begin{split} \mathbf{P}[s(t+1) &= j|\mathscr{F}(t+1)] = \mathbf{P}[s(t+1) = j|x(t+1), \mathscr{F}(t)] \\ &= \mathbf{P}[x(t+1) \in \mathrm{d}x | s(t+1) = j, \mathscr{F}(t)] \cdot \frac{\mathbf{P}[s(t+1) = j|\mathscr{F}(t)]}{\mathbf{P}[x(t+1) \in \mathrm{d}x | \mathscr{F}(t)]} \\ &= \frac{\mathbf{P}[x(t+1) \in \mathrm{d}x | s(t+1) = j, \mathscr{F}(t)] \cdot \mathbf{P}[s(t+1) = j|\mathscr{F}(t)]}{\sum_{\ell \in \mathscr{S}} \mathbf{P}[x(t+1) \in \mathrm{d}x | s(t+1) = \ell, \mathscr{F}(t)] \cdot \mathbf{P}[s(t+1) = \ell|\mathscr{F}(t)]} \end{split} \tag{8}$$

Derivative pricing is typically carried out in a continuous time setting.<sup>a</sup> For a vanilla payoff with maturity T, say  $z(T) = h(x(T))$ , the time-zero price is given by the risk neutral expectation:

$$z(0) = \mathbf{E}^{\mathcal{Q}}[D(T)z(T)] \tag{12}$$

where  $D(t)$  is the discount factor.

In the regime-switching framework, pricing is routinely carried out using the Fourier inversion techniques (see Fourier Transform) outlined in [7]. In particular, if the log asset price  $x(T)$  follows a regime-switching Brownian motion

$$dx(t) = \mu(s(t))dt + \sigma(s(t))dB(t) \qquad (13)$$

then the characteristic function  $\phi(u;T) = \text{E} \exp$  $(iux(T))$  is given by the matrix exponential

$$\phi(u;T) = \iota' \exp(T\mathbf{A}(u))\xi(0|0) \tag{14}$$

where the  $(N \times N)$  matrix  $\mathbf{A}(u)$  has the following form:

$$a_{i,j}(u) = \begin{cases} q_{i,i} + g(u;i) & \text{if } i = j \\ q_{i,j} & \text{if } i \neq j \end{cases}$$
(15)

for  $g(u; i) = iu\mu(i) - \frac{1}{2}u^2\sigma^2(i)$ .

The first implementation that prices options where a two-regime process is present is that in [26]. In a more general setting with  $N$  regimes, vanilla call option prices can be easily retrieved using the Fast Fourier Transform (FFT) approach of Carr and Madan [7] or the fractional variant that allows explicit control of the discretization grids [10].

The above prototypical process can be extended in two directions. Rather than having switching Brownian motions that generate the conditional paths, one can consider switching Lévy processes (see Lévy **Processes; Exponential Lévy Models**) between the regimes (see [24], for the special two-regime case, and [11], for a more general setting). In that case, the function  $g(u; i)$  in  $A(u)$  is replaced by the characteristic exponent of the Lévy process that is active in the  $i$ th regime. In addition, to introduce a correlation structure between the regime changes and the log-price changes, a jump in the log-price is introduced when the Markov chain switches. In that

case, the off-diagonal elements of  $A(u)$  are multiplied by the characteristic function of the jump size.

Pricing of American options can be done by setting up the continuation region  $[5]$  or by employing a variant of Carr's randomization procedure [4]. More exotic products can be handled by setting up a system of partial (integro-)differential equations (see Partial Integro-differential Equations (PIDEs)) or by explicitly using Fourier methods as in [22]. As the conditional distribution can be recovered from the characteristic function numerically, the density-based approach of [2] (see **Quadrature Methods**) can be a viable alternative.

## **Regime Switching as an Approximation**

Rather than serving as the fundamental latent process, the Markov chain can serve as an approximation to more complex jump-diffusive dynamics. Then, one can use the regime-switching framework to tackle problem in a nonaffine (see Affine Models) setting, both in terms of calibration and derivative pricing. To achieve that, the number of regimes must be large, but the transition rates and conditional dynamics will be functions of a small number of parameters. The book by Kushner and Dupuis [25] outlines the convergence conditions for the approximation of generic diffusions and shows how one can implement the Markov chain approximation in practice.

Following this approach, many stochastic volatility problems can be cast as regime-switching ones. Chourdakis [8] shows how a generic stochastic volatility process can be approximated in that way, whereas Chourdakis [9] extends this method to produce the counterpart of the [21] stochastic volatility model (see Heston Model) in a regime-switching framework where the equity is driven by a Lévy noise.

## **End Notes**

<sup>a.</sup>The treatment in References [12, 13] are exceptions to this.

## References

[1] Albert, J. & Chib, S. (1993). Bayes inference via Gibbs sampling of autoregressive time series subject to Markov mean and variance shifts, Journal of Business and Economic Statistics  $11, 1-15$ .

# **4 Regime-switching Models**

- [2] Andricopoulos, A.D., Widdicks, M., Duck, P.W. & Newton, D.P. (2003). Universal option valuation using quadrature methods, *Journal of Financial Economics* **67**, 447–471.
- [3] Ang, A. & Bekaert, G. (2002). Regime switches in interest rates, *Journal of Business and Economic Statistics* **20**(2), 163–182.
- [4] Boyarchenko, S.I. & Levendorski, S.Z. (2006). *American Options in Regime-switching Models*. Manuscript available online at SSRN: 929215.
- [5] Buffington, J. & Elliott, R.J. (2002). American options with regime switching, *International Journal of Theoretical and Applied Finance* **5**, 497–514.
- [6] Calvet, L. & Fisher, A. (2004). How to forecast long-run volatility: regime-switching and the estimation of multifractal processes, *Journal of Financial Econometrics* **2**, 49–83.
- [7] Carr, P. & Madan, D. (1999). Option valuation using the Fast Fourier Transform, *Journal of Computational Finance* **3**, 463–520.
- [8] Chourdakis, K. (2004). Non-affine option pricing, *Journal of Derivatives* **11**(3), 10–25.
- [9] Chourdakis, K. (2005). Levy processes driven by ´ stochastic volatility, *Asia-Pacific Financial Markets* **12**, 333–352.
- [10] Chourdakis, K. (2005b). Option pricing using the Fractional FFT, *Journal of Computational Finance* **8**(2), 1–18.
- [11] Chourdakis, K. (2005c). *Switching Levy Models in Continuous Time: Finite Distributions and Option Pricing*. Manuscript available online at SSRN: 838924.
- [12] Chourdakis, K. & Tzavalis, E. (2000). *Option Pricing Under Discrete Shifts in Stock Returns*. Manuscript available online at SSRN: 252307.
- [13] Duan, J.-C., Popova, I. & Ritchken, P. (1999). *Option Pricing under Regime Switching*. Technical report, Hong Kong University of Science and Technology.
- [14] Filardo, A.J. (1994). Business-cycle phases and their transitional dynamics, *Journal of Business and Economic Statistics* **12**, 299–308.
- [15] Garcia, R., Luger, R. & Renault, E. (2003). Empirical assessment of an intertemporal option pricing model with latent variables, *Journal of Econometrics* **116**, 49–83.
- [16] Gray, S. (1996). Modeling the conditional distribution of interest rates as a regime-switching process, *Journal of Financial Economics* **42**, 27–62.

- [17] Hamilton, J.D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle, *Econometrica* **57**, 357–384.
- [18] Hamilton, J.D. (1994). *Time Series Analysis*, Princeton University Press, Princeton, NJ.
- [19] Hamilton, J.D. (2005). What's real about the business cycle? *Federal Reserve Bank of St. Louis Review* **87**(4), 435–452.
- [20] Hamilton, J.D. & Susmel, R. (1994). Autoregressive conditional heteroscedasticity and changes in regime, *Journal of Econometrics* **64**, 307–333.
- [21] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–344.
- [22] Jackson, K.R., Jaimungal, S. & Surkov, V. (2007). *Fourier Space Time-stepping for Option Pricing with L´evy Models*. Manuscript available online at SSRN: 1020209.
- [23] Jeanne, O. & Masson, P. (2000). Currency crises, sunspots, and Markov-switching regimes, *Journal of International Economics* **50**, 327–350.
- [24] Konikov, M. & Madan, D. (2002). Option pricing using Variance Gamma Markov chains, *Review of Derivatives Research* **5**(1), 81–115.
- [25] Kushner, H.J. & Dupuis, P.G. (2001). *Numerical Methods for Stochastic Control Problems in Continuous Time*, 2nd Edition, Applications of Mathematics, Springer Verlag, New York, NY, Vol. 24.
- [26] Naik, V. (1993). Option valuation and hedging strategies with jumps in the volatility of asset returns, *The Journal of Finance* **48**, 1969–1984.
- [27] Weron, R., Bierbauer, M. & Truck, S. (2004). Modeling ¨ electricity prices: jump diffusion and regime switching, *Physica A* **336**, 39–48.

# **Related Articles**

**Exponential Levy Models ´** ; **Filtering**; **Fourier Methods in Options Pricing**; **Fourier Transform**; **Monte Carlo Simulation**; **Stochastic Volatility Models**; **Stylized Properties of Asset Returns**; **Variance-gamma Model**.

KYRIAKOS CHOURDAKIS
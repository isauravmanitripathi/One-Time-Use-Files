# **Foreign Exchange Smile** Interpolation

This article provides a short introduction into the handling of FX-implied volatility market data-especially their inter- and extrapolation across delta space and time. We discuss a low-dimensional Gaussian kernel approach as the method of choice showing several advantages over usual smile interpolation methods such as cubical splines.

## **FX-implied Volatility**

Implied volatilities for FX vanilla options are normally quoted against Black-Scholes deltas

$$\Delta_{\text{BS}} = e^{-r_f T} N$$

$$\times \left( \frac{\ln(S/K) + \left( r_d - r_f + \left( \sigma^2(\Delta)/2 \right) \right) T}{\sigma(\Delta)\sqrt{T}} \right) \tag{1}$$

Note that these deltas are dependent on  $\sigma(\Delta)$ , that is, the market-given volatility should be quoted. Thus, when retrieving a volatility for a given strike, an iterative processes is needed. However, under normal circumstances, the mapping from a delta-volatility to a strike-volatility coordinate system works via a quickly converging fixed point iteration.

## Proposition 1 (Delta–Strike fixed point iteration). $Let$

 $\Delta_n: A \mapsto A, A \subset (0, 1)$  be a mapping, defined by

$$\sigma_0 = \sigma_{\text{ATM}}$$
$$\Delta_0 = \Delta(K_{\text{Call}}, \sigma_{\text{ATM}})$$

 $\Delta_{n+1}$ 

$$= e^{-r_f(T-t)} N(d_1(\Delta_n))$$
(2)  
$$= e^{-r_f(T-t)} N \times \left( \frac{\ln(S/K) + (r_d - r_f + \sigma^2(\Delta_n)/2) (T-t)}{\sigma(\Delta_n)\sqrt{T-t}} \right)$$
(3)

For sufficiently large  $\sigma(\Delta_n)$  and a smooth, differentiable volatility smile, the sequence converges for  $n \to \infty$  against the unique fixed point  $\Delta^* \in A$  with  $\sigma^* = \sigma(\Delta^*)$ , corresponding to strike K.

The usual FX smiles normally satisfy the above mentioned regularity conditions. More details concerning this proposition can be found in [5]. However, note that already smoothness is demanded here, which directly leads to the issue of an appropriate smile interpolation.

#### Interpolation

Before the discussion of specific interpolation methods, let us take a step backward and remember Rebonato's well-known statement of implied volatility as the wrong number in the wrong formula to obtain the right price [3]. Therefore, the explanatory power of implied volatilities for the dynamics of a stochastic process remains limited. Implied volatilities give a lattice on which marginal distributions can be constructed. However, even using many data points to generate marginal distributions, forward distributions and extremal distributions, which determine the prices of some products such as compound and barrier products, cannot be uniquely defined by implied volatilities (see [4] for a discussion of this).

The attempt to capture FX smile features can lead to two different general approaches.

#### Parametrization

One possibility to express smile or skew patterns is just to capture it as the calibration parameter set of an arbitrary stochastic volatility or jump diffusion model that generates the observed market implied volatilities. However, as spreads are rather narrow in liquid FX options markets, it is preferred to exactly fit the given input volatilities. This automatically leads to an interpolation approach.

#### Pure Interpolation

As an introduction, we would like to pose four requirements for an acceptable volatility surface interpolation:

1. Smoothness in the sense of continuous differentiability. Especially with respect to the possible application of Dupire-style local volatility models, it is crucial to construct an interpolation that is at least  $C^2$  in strike and at least  $C^1$  in time direction. This becomes obvious when considering the expression for the local volatility in this context:

**Definition 1** (**Slice Kernel**). *Let*  $(x_1, y_1), (x_2, y_2), \ldots$  $(x_n, y_n)$  be n given points and  $g: \mathbb{R} \mapsto \mathbb{R}$  a smooth function which fulfills

$$g(x_n) = y_n, \quad n = 1, \dots, n$$
 (6)

$$\sigma_{loc}^{2}(S,K) = \frac{\partial C(K,T)/\partial T + r_{f}C(K,T) + K(r_{d}-r_{f})\partial C(K,T)/\partial K}{(1/2)K^{2}(\partial^{2}C(K,T)/K^{2})}$$

$$= \frac{\frac{\sigma_{i}}{T} + 2(r_{d}-r_{f})K(\partial\sigma_{i}/\partial K) + 2(\partial\sigma_{i}/\partial T)}{K^{2}\left(\frac{1}{\sigma_{i}}\left(1/(K\sqrt{T}+d_{+}\partial\sigma_{i}/\partial K)\right)^{2} + \partial^{2}\sigma_{i}/\partial K^{2} - d_{+}\sqrt{T}\left(\partial\sigma_{i}/\partial K\right)^{2}\right)}$$

$$(4)$$

where  $C(K, T)$  denotes the Black-Scholes prices of a call option with strike  $K$ ,  $\sigma_i$  its corresponding implied volatility, and

$$d_{+} = \frac{\ln\left(S/K\right) + \left(r_d - r_f + \sigma^2(\Delta)/2\right)T}{\sigma(\Delta)\sqrt{T}} \quad (5)$$

Note in addition that local volatilities can directly be extracted from delta-based FX volatility surfaces, that is, the Dupire formula can alternatively be expressed in terms of delta. See [2] for details.

- 2. Absence of oscillations, which is guaranteed if the sign of the curvature of the surface does not change over different strike or delta levels.
- 3. Absence of arbitrage possibilities on single smiles of the surface as well as absence of calendar arbitrage
- 4. A reasonable extrapolation available for the interpolation method.

A widely used classical interpolation method is cubical splines. They attempt to fit surfaces by fitting piecewise cubical polynomials to given data points. They are specified by matching their second derivatives at each intersection. Although this ensures the required smoothness by construction, it does not prevent oscillations, which directly leads to the danger of arbitrage possibilities or it does not define how to extrapolate the smile. We, therefore, introduce the concept of a slice kernel volatility surface as an alternative:

A smooth interpolation is then given by

$$g(x) := \frac{1}{\Phi_{\lambda}(x)} \sum_{i=1}^{N} \alpha_{i} K_{\lambda}(\|x - x_{i}\|) \tag{7}$$

where

$$\Phi_{\lambda}(x) := \sum_{i=1}^{N} K_{\lambda}(\|x - x_{i}\|) \tag{8}$$

 $and$ 

$$K_{\lambda}(u) := \exp\left\{-\frac{u^2}{2\lambda^2}\right\} \tag{9}$$

The described kernel is also called Gaussian Kernel. The interpolation reduces to determining the  $\alpha_i$ , which is straightforward via solving a linear equation system. Note that  $\lambda$  remains as a free smoothing parameter, which also affects the condition of the equation system. At the same time, it can be used to fine-tune the extrapolation behavior of the kernel.

Generally, the slice kernel produces reasonable output smiles based on a maximum of seven deltavolatility points. Then it fulfills all the abovementioned requirements. It is  $\mathcal{C}^{\infty}$ , does not create oscillations, passes typical no-arbitrage conditions as they are, for example, posed by Gatheral [1], and finally has an inherent extrapolation method.

In time direction, one might connect different slice kernels by linear interpolation of the variances for same deltas. This also normally ensures the absence of calendar arbitrage, for which a necessary condition

![](_page_2_Figure_1.jpeg)

![](_page_2_Figure_2.jpeg)

**Figure 1** Kernel interpolation of an FX volatility surface

is a nondecreasing variance for constant moneyness *F/K* (see also [1] for a discussion of this).

Figure 1 displays the shape of a slice kernel applied to a typical FX volatility surface constructed from 10 and 25 delta volatilities, and the ATM volatility (in this example *λ* = 0*.*25 was chosen).

# **References**

- [1] Gatheral, J. (2004). *A Parsimonious Arbitrage-free Implied Volatility Parameterization with Application to the Valuation of Volatility Derivatives*, Workshop Presentation, Madrid.
- [2] Hakala, J. & Wystup, U. (2002). Local volatility surfaces—tackling the smile, *Foreign Exchange Risk*, Risk Books.

- [3] Rebonato, R. (1999). *Volatility and Correlation*, John Wiley & Sons.
- [4] Tistaert, J., Schoutens, W. & Simons, E. (2004). A perfect calibration now what? *Wilmott Magazine* (March), 66–78.
- [5] Wystup, U. (2006). *FX Options and Structured Products*, John Wiley & Sons.

# **Related Articles**

**Foreign Exchange Markets**; **Foreign Exchange Options: Delta- and At-the-money Conventions**.

UWE WYSTUP
# **Ouadratic Gaussian** $\mathbf{Models}^{\mathbf{a}}$

Ouadratic Gaussian (OG) models are factor models for the pricing of interest-rate derivatives, where interest rates are quadratic functions of underlying Gaussian factors. The OG model of interest rates was first introduced by Beaglehole and Tenney [3] and by El Karoui *et al.* [11]. Similar models had been introduced in epidemiology [16]. Jamshidian [14], under restrictive hypothesis on the dynamic of the factors, obtained closed formulas for the prices of vanilla options in the QG model. Durand and El Karoui [10] have detailed some properties and statistical analysis of the QG model. One may refer, for example, to  $[1, 6]$  for general studies of quadratic term-structure models.

## **Ouadratic Gaussian Model**

Uncertainty is represented by an  $n$ -dimensional Brownian motion  $\widehat{\widehat{W}}_t = (\widehat{W}_t^1, \widehat{W}_t^2, \dots, \widehat{W}_t^n)^{*b}$  on the filtered probability space  $(\Omega, F_t, P)$ , where  $F_t$  is the natural augmented filtration of Brownian motion  $\widehat{W}$ and  $P$  the historical probability. We then add two assumptions:

**Hypothesis 1** The asset price processes in all the different markets are regular deterministic functions of  $n$  state variables.

**Hypothesis 2** The state variables have a Gaussian– Markovian distribution with respect to all the risk-neutral probabilities (which includes the forwardneutral probabilities).

The first hypothesis is common and is used in numerical methods such as finite difference methods to price and hedge options; the second is also natural if we want to have results as explicit as possible. We specify, more precisely, the diffusion of the state variable Z under the risk-neutral probability (see Ornstein-Uhlenbeck Processes):

$$dZ_t = (A_t Z_t + \mu_t) dt + \Sigma_t dW_t \tag{1}$$

where  $(W_t)$  is a Brownian motion under the domestic risk-neutral probability  $\mathcal{Q}$ .

**Theorem 1** [11]. Under these assumptions, there exist a family of symmetrical matrices  $\widehat{\Gamma}(t,T)$ , a family of vectors  $\widehat{b}(t,T)$ , and a family of scalars  $\widehat{a}(t,T)$  such that the zero-coupon price at t of the bond  $P(t, T)$  is given by

$$P(t,T) = \exp\left[Z_t^* \widehat{\Gamma}(t,T) Z_t + \widehat{b}^*(t,T) Z_t + \widehat{a}(t,T)\right]$$
(2)

In particular, the functional dependence of the short rate  $r_t$  on the factors is quadratic affine:

$$r_t = -\partial_T \ln P(t, T)_{t=T}$$
  
=  $\left[ Z_t^* \Gamma(t, t) Z_t + b^*(t, t) Z_t + a(t, t) \right]$  (3)

where

$$\begin{cases}\n\Gamma(t,T) = -\partial_T \widehat{\Gamma}(t,T) \\
b(t,T) = -\partial_T \widehat{b}(t,T) \\
a(t,T) = -\partial_T \widehat{a}(t,T)\n\end{cases} \tag{4}$$

To describe completely the dynamics of the interest rates, we need to make explicit the computation of the matrices  $\widehat{\Gamma}(t,T)$ ,  $\widehat{b}(t,T)$ , and  $\widehat{a}(t,T)$ . Once again, the no-arbitrage assumption will give us the solution.

Theorem 2 [11]. Given the short rate parameters,  $\Gamma(t, t)$ ,  $b(t, t)$ , and  $a(t, t)$ , the matrices  $\widehat{\Gamma}(t, T)$ ,  $\widehat{b}(t,T)$ , and  $\widehat{a}(t,T)$  are the solutions of the backward  $\text{differential system with respect to the current date } t$ 

$$\begin{cases} \partial_t U_t = -(A_t^* U_t + U_t A_t) + 2U_t^* \Sigma_t \Sigma_t^* U_t - \Gamma(t, t) \\ \partial_t u_t = -A_t^* u_t + 2U_t \Sigma_t^* \Sigma_t u_t - 2U_t \mu_t - b(t, t) \\ \partial_t \alpha_t = -tr[\Sigma_t \Sigma_t^* U_t] - u_t^* \mu_t + \frac{1}{2} u_t^* \Sigma_t \Sigma_t^* u_t - a(t, t) \end{cases}$$

$$(5)$$

with the initial conditions

$$\begin{cases} U_T = 0\\ u_T = 0\\ \alpha_T = 0 \end{cases} \tag{6}$$

These two results, which are direct consequences of the hypothesis, completely describe the diffusion of the interest rates under the risk-neutral probability. In the stationary case, let us denote  $\hat{\Gamma}_{\infty}$  the solution of the algebraic Riccati equation on  $U$ :

$$A^*U + UA - 2U^*\Sigma\Sigma^*U + \Gamma = 0 \tag{7}$$

If  $A - 2\hat{\Gamma}_{\infty} \Sigma \Sigma^*$  has only negative eigenvalues, then the equations of Theorem 2 will only have nonexploding solutions. In those cases, one can even obtain a simple expression for the limit of the zero-coupon interest rate when the maturity increases to infinity; this limit does not depend on the time (see  $[10]$ ). The QG model admits, for example, the following models as particular cases:

- the Gaussian model of Vasicek [15], its generalization by Hull and White [13], and its multidimensional version by Heath, Jarrow, and Morton (HJM) [12] (see Gaussian Interest-Rate Models):
- Cox, Ingersoll, and Ross (CIR) [8], Chen and Scott [7], and Duffie and Kan [9]; also see Cox-Ingersoll-Ross (CIR) Model.

#### **Statistical Justification**

In addition to the practical and computational justification of the hypothesis that lead to the QG model, this model can also be justified by statistical studies of the interest rates. The most intuitive justification comes from principal component analysis (PCA). For most currencies, using a PCA will lead to keeping two factors to explain the diffusion of the interest yield curves. Then, the residual noise may be explained by a quadratic form of the first two factors of the PCA. For a detailed description of this analysis, we refer to [10].

## **Option Pricing**

In the QG model, the instantaneous volatility of the zero-coupon interest rates  $R(t, T)$  is an affine form of the factors  $Z_t$ , and when we consider two factors or more, the instantaneous volatility of  $R(t, T)$  cannot be written as a deterministic form of  $R(t, T)$ : in some way, we can therefore consider the QG model as a stochastic volatility model.<sup>c</sup> Its main interest will be in interest-rate exotic option pricing and hedging.

#### Closed Form for Vanilla Option

Quasi-closed form for vanillas options are the consequence of the following result.

**Theorem 3** [11]. Let us denote by  $m^{T}(t, u)$  and  $V^{T}(t, u)$  the conditional mean and the conditional variance of  $Z_u$  under the forward-neutral probability of maturity  $T \mathbf{Q}_{t}^{T}$ . The conditional mean  $m^{T}(t, T)$  and

variance  $V^{T}(t,T)$  of the factors are solutions of the differential system given by equation (8):

$$\begin{cases} \frac{\partial V^T(t,T)}{\partial T} = V^T(t,T)(A_T)^* + A_T V^T(t,T) \\ -2V^T(t,T)\Gamma(T,T)V^T(t,T) + \Sigma_T \Sigma_T^* \\\frac{\partial m^T(t,T)}{\partial T} = A_T m^T(t,T) \\ -2V^T(t,T)\Gamma(T,T)m^T(t,T) \\ +2V^T(t,T)b(T,T) + \mu_T \end{cases} \tag{8}$$

and under the risk-neutral probability  $\mathbf{Q}_t$ , the conditional mean  $m(t, T)$  and variance  $V(t, T)$  of the factors are solutions of the differential system:

$$\begin{cases}\n\frac{\partial V(t,T)}{\partial T} = V(t,T)(A_T)^* + A_T V(t,T) + \Sigma_T \Sigma_T^* \\
\frac{\partial m(t,T)}{\partial T} = A_T m(t,T) + \mu_T \\
V(t,t) = 0 \qquad m(t,t) = Z_t\n\end{cases} \tag{9}$$

Assefa [2] has detailed swaption prices in the QG model and has described how approximations may be obtained using Fourier transform. Some analytical approximations of caps, floors, and swaptions are also proposed in  $[4]$ .

## Pricing of Exotic Options

To use the QG model to price and hedge exotic options, one needs to add some constraints to simplify the different equations and to accelerate the different numerical schemes used in the different steps of calibrating the model on plain vanilla option prices and used to price exotic options. Some calibration results of a two-factor OG model on USD Libor caps and swaptions are shown in [2]. Depending on the shape of the smile and on the payoff of the exotic option studied, one uses a one- or two-factor model: empirically, by using a one-factor QG model one will generate increasing or decreasing volatility smiles; with a two-factor QG model, "U-shape" volatility smiles may be generated. The QG model can then be successfully calibrated on vanilla option prices and on interest-rate correlation to price and hedge exotic interest-rate options. We recommend to choose a calibration set for each exotic option and not to try to calibrate simultaneously to the entire volatility cube. We also recommend to specify a correlation structure

on the forward interest rate and not to deduce it implicitly from the market implied volatilities.

# **Summary**

Owing to its capacity to calibrate interest-rate volatility smiles and correlation term structure, the QG is an interesting model to price and hedge exotic interest-rate derivatives, as multicancelable options on interest-rate spreads. Several banks have developed proprietary models based on the QG model, each choosing its own parameterization, mainly as a consequences of choices made on the numerical schemes used.

# **End Notes**

a*.* This article reflects the author's point of view and do not necessarily represents the point of view of Banque de France.

b*.* Here *x*<sup>∗</sup> denotes transpose *(x)*.

c*.* In fact, as we can deduce the factors *Zt* from the interestrate curve, we can write the instantaneous volatility of *R(t, θ )* as a deterministic function of interest rate of different maturities; in a theoretical point of view, the QG model may be not a stochastic volatility model as defined in [5].

# **References**

- [1] Ahn, D.-H., Dittmar, R.F. & Gallant, A.R. (1999). *Quadratic Term Structure Models: Theory and Evidence*, working paper, University of North Carolina.
- [2] Assefa, S. (2007). *Calibrating and Pricing in a Multi-Factor Quadratic Gaussian Model*, research paper, Quantitative Finance Research Centre, University of Technology Sydney.
- [3] Beaglehole, D. & Tenney, M. (1991). General solutions of some interest rate contingent claim pricing equations, *Journal of Fixed Income* **1**, 69–83.

- [4] Boyarchenko, N. & Levendorski, S. (2007). The eigenfunction expansion method in multi-factor quadratic term structure models, *Mathematical Finance* **17**, 503–539.
- [5] Casassus, J., Collin-Dufresne, P. & Goldstein, B. (2005). Unspanned stochastic volatility and fixed income derivatives pricing, *Journal of Banking and Finance* **29**, 2723–2749.
- [6] Chen, L., Filipovic, D. & Poor, H.V. (2004). Quadratic term structure models for risk-free and defaultable rates, *Mathematical Finance* **14**, 515–536.
- [7] Chen, R.-R. & Scott, L. (1992). Pricing interest rate options in a two-factor cox-ingersoll-ross model of the term structure, *Review of Financial Studies* **5**, 613–636.
- [8] Cox, J., Ingersoll, J. & Ross, S. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–407.
- [9] Duffie, D. & Kan, R. (1992). *A Yield-Factor Model of Interest Rates*, working paper, Stanford University.
- [10] Durand, Ph. & El Karoui, N. (1998). *Interest Rates Dynamics and Option Pricing with the Quadratic Gaussian Model in Several Economies*, working paper.
- [11] El Karoui, N., Myneni, R. & Viswanathan, R. (1991). *Arbitrage Pricing and Hedging of Interest Rate Claims with State Variables, Theory and Applications*, working paper, Universite Paris VI.
- [12] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**, 77–105.
- [13] Hull, J. & White, A. (1990). Pricing interest rate derivative securities, *Review of Financial Studies* **3**, 573–592.
- [14] Jamshidian, F. (1996). Bond, futures and option evaluation in the quadratic interest rate model, *Applied Mathematical Finance* **3**, 93–115.
- [15] Vasicek, O. (1977). An equilibrium characterisation or the term structure, *Journal of Financial Economics* **5**, 177–188.
- [16] Woodbury, M.A., Manton, K.G. & Stallard, E. (1979). Longitudinal analysis of the dynamics and risk of coronary heart disease in the framingham study, *Biometrics* **35**, 575–585.

PHILIPPE DURAND
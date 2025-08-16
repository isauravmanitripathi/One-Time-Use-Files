# **LIBOR Market Models:** Simulation

The Libor market (LM) model (see LIBOR Market Model) involves a large number of Markov state variables—namely, the full number of Libor forward rates on the yield curve plus any additional variables such as stochastic volatility—so finite difference methods are rarely applicable, and securities pricing will nearly always require Monte Carlo methods. The specific form of the stochastic differential equations (SDEs) governing the dynamics of forward Libor rates gives rise to some specialized approaches, as well as to particular challenges, that are covered in this article. The notation used throughout is that of LIBOR Market Model.

## **Euler-type Schemes**

## Basic Stepping Method

Assume that we stand at time  $t$ , and Libor forwards  $(L)$  maturing at all dates in the tenor structure are known. We wish to devise a scheme to advance time to  $t + \Delta$  and construct a sample<sup>a</sup> of  $L_{q(t+\Delta)}(t + \Delta)$  $\Delta$ ),...,  $L_{N-1}(t+\Delta)$ . Notice that  $q(t+\Delta)$  may or may not exceed  $q(t)$ ; if it does, some of the front-end forward rates expire and "drop off" the curve in the move to  $t + \Delta$ .

Under the spot measure  $\mathbf{P}^B$ , general LM model dynamics are of the form (see LIBOR Market Model)

$$dL_n(t) = \sigma_n(t)^{\top} \left(\mu_n(t) dt + dW_B(t)\right),$$
  
$$\mu_n(t) = \sum_{j=q(t)}^n \frac{\tau_j \sigma_j(t)}{1 + \tau_j L_j(t)} \tag{1}$$

where  $\sigma_n(t)$  are adapted vector-valued volatility functions and  $W_B$  is an *m*-dimensional Brownian motion in measure  $\mathbf{P}^B$ . The simplest way of drawing an approximate sample  $\hat{L}_n(t + \Delta)$  for  $L_n(t + \Delta)$  would be to apply a first-order Euler-type scheme,<sup>b</sup>

Euler : 
$$\hat{L}_n(t + \Delta)$$
  
=  $\hat{L}_n(t) + \sigma_n(t)^{\top} \left(\mu_n(t)\Delta + \sqrt{\Delta}z\right)$  (2)

log-Euler :  $\hat{L}_n(t+\Delta)$ 

$$= \hat{L}_n(t) \exp\left\{\frac{\sigma_n(t)^{\top}}{\hat{L}_n(t)} \left(\mu_n(t)\Delta - \frac{1}{2}\frac{\sigma_n(t)}{\hat{L}_n(t)}\Delta + \sqrt{\Delta}z\right)\right\}$$
(3)

where z is a vector of m independent  $\mathcal{N}(0, 1)$ Gaussian draws. For specifications of  $\sigma_n(t)^\top$  that are close to proportional in  $L_n(t)$  (e.g., the lognormal LM model), the log-Euler scheme  $(3)$  can be expected to produce lower biases than the Euler scheme (2). The log-Euler scheme will keep forward rates positive, whereas the Euler scheme will not.

As shown, both schemes  $(2)$  and  $(3)$  advance time only by a single time step, but creation of a full path of forward curve evolution through time is merely a matter of repeated application of the single-period stepping schemes on a (possibly nonequidistant) time line  $t_0, t_1, \ldots$ 

While Euler-type schemes such as  $(2)$  and  $(3)$ are not very sophisticated and result in rather slow convergence of the discretization bias  $(O(\Delta))$ , these schemes are appealing in their straightforwardness and universal applicability.

## Iterative Drift Calculations

In the straight Euler scheme (2), the computational effort involved in advancing  $L_n$  is dominated by the computation of  $\mu_n(t)$  which, in a direct implementation of equation (1), involves  $m \cdot (n - q(t) + 1) =$  $O(mn)$  operations for a given value of n. To advance all  $N - q(t + \Delta)$  forwards, it follows that the computational effort is  $O(mN^2)$  for a single time step. Generation of a full path of forward curve scenarios from time 0 to time  $T_{N-1}$  will thus require a total computational effort of  $O(mN^3)$ .

A simple observation allows one to substantially reduce the computational effort. Invoking the recursive relationship

$$\mu_n(t) = \mu_{n-1}(t) + \frac{\tau_n \sigma_n(t)}{1 + \tau_n \hat{L}_n(t)} \tag{4}$$

allows one to compute all  $\mu_n$ ,  $n = q(t+\Delta)$ , ...,  $N-1$ , by an  $O(N)$ -step iteration starting from  $\mu_{q(t+\Delta)}(t)$  $= \sum_{j=q(t)}^{q(t+\Delta)} \tau_j \sigma_j(t) / (1+\tau_j \hat{L}_j(t)).$  In total, the computational effort of advancing the full curve onetime step will be *O(mN )*, and the cost of taking *N* such time steps will be *O(mN*<sup>2</sup>*)*—and not *O(mN*<sup>3</sup>*)*.

This reduction in effort is discussed, in considerable level of detail, in [6]. It can be verified to hold for any of the probability measures used in LM modeling; the starting point of recursions would depend on which measure is used.

## *Long Time Steps*

Most exotic interest rate derivatives involve revolving cash flows paid on a tightly spaced schedule (e.g., quarterly). Hence, the average time spacing used in path generation will thus normally, by necessity, be quite small. In certain cases, however, there may be large gaps between cash flow dates, for example, when a security is forward-starting or has an initial lockout period. One may want, then, to be able to take a "large" time step in the simulation; here "large" is defined as spanning more than one period in the tenor structure.

When taking large time steps in simulation, not all probability measures are equally useful. In particular, the usage of the spot measure **P***<sup>B</sup>* is inconvenient, as skipping over points in the tenor structure will preclude one from "rolling" *B(t)* correctly. Circumventing this issue, however, is merely a matter of changing the numeraire from *B* to an asset that involves no rollover in the time step in question. For instance, we could use the discount bond *P (t, TN )*, the choice of which corresponds to running simulated paths in the terminal measure. Model dynamics under this measure are given in **LIBOR Market Model**.

# **Other Simulation Schemes**

When simulating on a reasonably tight time schedule, the performance of the Euler scheme is often sufficiently accurate to serve as the default scheme for many types of LM models. However, as discussed above, in some cases, it could be beneficial to use coarse time steps in some parts of the path-generation algorithm, requiring one to pay more attention to the discretization scheme.

*Special-purpose Schemes with Drift Predictor–Corrector*

In integrated form, the general LM dynamics in equation (1) become

$$L_n(t + \Delta) = L_n(t) + \int_t^{t+\Delta} \sigma_n(u)^\top \mu_n(u) \, du$$
$$+ \int_t^{t+\Delta} \sigma_n(u)^\top \, dW_B(u)$$
$$\equiv L_n(t) + D_n(t + \Delta) + M_n(t + \Delta) \tag{5}$$

where *Mn* and *Dn* is a martingale and a predictable process, respectively, on the interval [*t,t* + ]. In many cases of practical interest, high-performance special-purpose schemes exist for simulation of the martingale process *Mn*. A simple approach is to use Euler stepping for the predictable part,

$$\hat{L}_n(t+\Delta) = \hat{L}_n(t) + \sigma_n(t)^\top \mu_n(t) \Delta + \hat{M}_n(t+\Delta)$$
(6)

where *M*ˆ *n(t* + *)* is generated by a special-purpose scheme.

The drift adjustments in equation (6) are explicit in nature, as they are based only on the forward curve at time *t*. To incorporate information from time *t* + , one can use the *predictor–corrector* scheme, see [8] and **Monte Carlo Simulation for Stochastic Differential Equations**, which for equation (6) takes the two-step form

$$\begin{split} \bar{L}_n(t+\Delta) \\ &= \hat{L}_n(t) + \sigma_n\big(t; \big\{\hat{L}_i(t)\big\}\big)^\top \mu_n\big(t; \big\{\hat{L}_i(t)\big\}\big) \,\Delta \\ &+ \hat{M}_n(t+\Delta) \end{split} \tag{7}$$
$$\begin{split} \hat{L}_n(t+\Delta) \\ &= \hat{L}_n(t) + \theta \sigma_n\big(t; \big\{\hat{L}_i(t)\big\}\big)^\top \mu_n\big(t; \big\{\hat{L}_i(t)\big\}\big) \,\Delta \\ &+ (1-\theta)\sigma_n\left(t+\Delta; \big\{\bar{L}_i(t+\Delta)\big\}\right)^\top \\ &\times \mu_n\left(t+\Delta; \big\{\bar{L}_i(t+\Delta)\big\}\right) \,\Delta + \hat{M}_n(t+\Delta) \end{split} \tag{8}$$

where *θ* is a parameter in [0*,* 1] that determines the degree of implicitness in the scheme (*θ* = 1: fully explicit; *θ* = 0: fully implicit). In practice, one would nearly always make the balanced choice of  $\theta = 1/2$ . In equations  $(7)$  and  $(8)$  the short-hand notation

$$\mu_n\left(t;\left\{\hat{L}_i(t)\right\}\right)$$

is used to indicate that  $\mu_n$  (and  $\sigma_n$ ) may depend on the state of the entire forward curve at time  $t$ .

Clearly, the same idea could be developed with the log-Euler scheme  $(3)$  as a starting point.

While the weak convergence order of simulation schemes may not be affected by predictor-corrector schemes, experiments show that equations  $(7)$  and  $(8)$ often will reduce the bias significantly relative to a fully explicit Euler scheme. Some results (and further refinements) can be found in  $[4, 9]$  and  $[10]$ . As the computational effort of computing the predictorstep is not insignificant, the speed-accuracy trade-off must be evaluated on a case-by-case basis.

## Further Refinements of Drift Estimation

For large time steps, it may be useful to explicitly integrate the time-dependent parts of the drift, rather than rely on pure Euler-type approximations. Focusing on, say, equation (6), assume that one can write

$$\sigma_n(u)^{\top} \mu_n(u) \approx f\left(u, \{L_i(t)\}\right), \quad u \ge t \qquad (9)$$

for a function  $f$  that depends on time as well as the state of the forward curve frozen at time  $t$ . Then,

$$D_n(t + \Delta) = \int_t^{t+\Delta} \sigma_n(u)^\top \mu_n(u) \, \mathrm{d}u$$
$$\approx \int_t^{t+\Delta} f\left(u, \{L_i(t)\}\right) \, \mathrm{d}u \qquad (10)$$

As f evolves deterministically for  $u > t$ , the integral on the right-hand side can be evaluated either analytically (if  $f$  is simple enough) or by numerical quadrature.

The approach in equation  $(10)$  easily combines with predictor-corrector logic, that is,

$$D_n(t+\Delta) \approx \theta \int_t^{t+\Delta} f\left(u, \{L_i(t)\}\right) \, \mathrm{d}u$$
  
 
$$+(1-\theta) \int_t^{t+\Delta} f\left(u, \{\bar{L}_i(t+\Delta)\}\right) \, \mathrm{d}u$$
  
(11)

where  $\bar{L}_i(t + \Delta)$  has been found in a predictor step using equation  $(10)$  in equation  $(6)$ .

#### Brownian Bridge Schemes and Other Ideas

As a variation on the predictor-corrector scheme, a further refinement to take into account variance of the Libor curve between the sampling dates  $t$  and  $t + \Delta$  could be made. Schemes attempting to do so by application of Brownian bridge techniques were proposed in [9], among others. While performance of these schemes vary—tests in  $[7]$  show rather mixed results in comparison to simpler predictor-corrector schemes—the basic idea is sufficiently simple and instructive to merit a brief mention. In a nutshell, the Brownian bridge approach aims to replace in equation (10) all forward rates  $\{L_i(t)\}\$  with their expected values at time  $u$ , *conditional* upon the forward rates ending up at  $\{\bar{L}_i(t+\Delta)\}\$ , with  $\{\bar{L}_i(t+\Delta)\}\$  generated in a predictor step. Under simplifying assumptions on the dynamics of  $L_n(t)$ , a closed-form expression is possible for this expectation. For example, if we assume that

$$\mathrm{d}L_n(t) \approx \sigma_n(t)^\top \,\mathrm{d}W(t) \tag{12}$$

where  $\sigma_n$  is *deterministic* and  $W(t)$  is an *m*dimensional Brownian motion in some probability measure **P**, then, for  $u \in [t, t + \Delta]$ ,

$$E(L_n(u)|L_n(t), L_n(t+\Delta))$$
  
=  $L_n(t) + \frac{\Sigma_1}{\Sigma_2} (L_n(t+\Delta) - L_n(t))$  (13)

where

$$\Sigma_1 = \int_t^u |\sigma_n(s)|^2 \, \mathrm{d}s, \quad \Sigma_2 = \int_t^{t+\Delta} |\sigma_n(s)|^2 \, \mathrm{d}s \tag{14}$$

If it is more appropriate to assume that  $L_n$  is roughly lognormal, that is,

$$\mathrm{d}L_n(t)/L_n(t) \approx \sigma_n(t)^\top \,\mathrm{d}W(t) \tag{15}$$

for a deterministic volatility  $\sigma_n$ , then, for  $u \in$  $[t, t + \Delta],$ 

$$E(L_n(u)|L_n(t), L_n(t+\Delta))$$
  
=  $L_n(t) \left(\frac{L_n(t+\Delta)}{L_n(t)}\right)^{\Sigma_1 \Sigma_2^{-1}}$   
 $\times \exp\left(\frac{1}{2}\Sigma_2^{-1}\Sigma_1(\Sigma_2-\Sigma_1)\right)$  (16)

The article [7] investigates a number of other possible discretization schemes for the drift term in the LM model, including those that attempt to incorporate information about the correlation between various forward rates. In general, many of these schemes will result in some improvement of the discretization error, but at the cost of more computational complexity and effort—effort that in some instances might be better spent on just using a finer time discretization in a simpler discretization scheme.

#### High-order Schemes

Higher order schemes (such as the Milstein scheme and similar Taylor-based approaches, see Monte Carlo Simulation for Stochastic Differential Equations and Stochastic Taylor Expansions) are cumbersome to use for LM modeling due to the high dimensionality of the model. Consequently, there are very few empirical results on their relative performance. Andersen and Andreasen [1] list some results for Richardson extrapolation (see [8]), the effect of which seems to be rather modest.

## **Martingale Discretization**

It is possible to select a measure such that a particular zero-coupon bond and a particular forward rate agreement (FRA) will be priced bias-free<sup>c</sup> by Monte Carlo simulation, even when using a simple Euler scheme. While one is rarely interested in pricing zero-coupon bonds by Monte Carlo methods, this observation can, nevertheless, occasionally help guide the choice of simulation measure, particularly if, say, a security can be argued to depend primarily on a single forward rate (e.g., caplet-like securities). In practice, matters are rarely this clear-cut, and one wonders whether perhaps simulation schemes exist that will simultaneously price all zero-coupon bonds  $P(\cdot, T_1)$ ,  $P(\cdot, T_2), \ldots, P(\cdot, T_N)$  bias-free. It should be obvious that this cannot be accomplished by a simple measure shift, but will require a more fundamental change in simulation strategy.

### Deflated Bond Price Discretization

To develop a simulation scheme, which, by construction, will ensure that all numeraire-deflated bond prices are martingales, one can follow the suggestion offered in [3]: instead of discretizing the dynamics for Libor rates directly, simply discretize the deflated bond prices themselves. Consider the spot measure, and define

$$U(t, T_{n+1}) = \frac{P(t, T_{n+1})}{B(t)}$$
(17)

The dynamics for deflated zero-coupon bond prices  $(17)$  are given by

$$\frac{\mathrm{d}U(t,T_{n+1})}{U(t,T_{n+1})} = -\sum_{j=q(t)}^{n} \tau_j \frac{U(t,T_{j+1})}{U(t,T_j)} \sigma_j(t)^{\top} \mathrm{d}W_B(t),$$
  
$$n = q(t), \dots, N-1 \tag{18}$$

Discretization schemes for equation (18), which preserve the martingale property, are easy to construct. For instance, the log-Euler scheme

$$\hat{U}(t + \Delta, T_{n+1}) = \hat{U}(t, T_{n+1})$$
$$\times \exp\left(-\frac{1}{2} |\eta_{n+1}(t)|^2 \Delta + \eta_{n+1}(t)^\top z \sqrt{\Delta}\right) \tag{19}$$

has this property where, as before,  $z$  is an  $m$ dimensional standard Gaussian variable, and

$$\eta_{n+1}(t) \stackrel{\Delta}{=} -\sum_{j=q(t)}^{n} \tau_j \frac{\hat{U}(t, T_{j+1})}{\hat{U}(t, T_j)} \sigma_j(t) \tag{20}$$

One can replace equation (19) with another discretization of equation (18), or one can try to discretize a quantity other than the deflated bonds  $U(t, T_n)$ . The latter idea is pursued in [3], where several suggestions for discretization variables are considered. For instance, one can consider the differences

$$U(t, T_n) - U(t, T_{n+1})$$
 (21)

which are martingales, since the  $Us$  are. Discretizing  $U(t, T_n) - U(t, T_{n+1})$  is, in a sense, close to discretizing  $L_n$  itself, which may be advantageous. [7] contains some tests of discretization schemes based on equation  $(21)$ , in a lognormal model setting.

## **End Notes**

<sup>a.</sup>We recall from **LIBOR Market Model** that  $q(t)$  is an index function, indicating which bucket of a tenor structure  $\{T_n\}_{n=0}^N$  time *t* belongs to.

 $\mathbf{b}$ . In the interest of brevity and conciseness, the simulation schemes discussed in this article omit a number of real-life details, such as proper rate fixing conventions, interpolation techniques and introduction of stochasticity in the front stub, that is, in the bucket  $[t, T_{a(t)}]$ . Interpolation and propagation of "nonstandard" rates, that is, rates with dates not aligned with the tenor structure  $\{T_n\}$ , are covered in, for example, [2], and a simple representative technique for stochastic front stubs can be found in [5].

<sup>c.</sup>But not error-free, obviously—there will still be a statistical mean-zero error on the simulation results.

## References

- Andersen, L.B.G. & Andreasen, J. (2000). Volatil- $[1]$ ity skews and extensions of the Libor market model, Applied Mathematical Finance 7, 1-32.
- [2] Brigo, D. & Mercurio, F. (2001). Interest-Rate Models—Theory and Practice, Springer Verlag.
- Glasserman, P. & Zhao, X. (2000). Arbitrage-free dis-[3] cretization of lognormal forward Libor and swap rate models, Finance and Stochastics 4, 35-68.

- Hunter, C.J., Jäckel, P. & Joshi, M.S. (2001). Getting [4] the drift, Risk 14(7), 81-84.
- Jäckel, P. (2005). The Practicalities of Libor Market [5] *Models*. Training course notes, http://www.jaeckel.org/  $The Practicalities Of Libor Market Models.pdf.$
- Joshi, M.S. (2003). Rapid Drift Computations in the [6] Libor Market Model, Wilmott.
- [7] Joshi, M.S. & Stacey, A.M. (2008). New and robust drift approximations for the Libor market model, Quantitative Finance 8, 427-434.
- [8] Kloeden, P.E. & Platen E. (2000). Numerical Solution of Stochastic Differential Equations, Stochastic Modelling and Applied Probability, Springer.
- [9] Pietersz, R., Pelsser, A. & van Regenmortel, M. (2004). Fast drift approximated pricing in the BGM model, Journal of Computational Finance 8, 93-124.
- [10] Rebonato, R. (2002). Modern Pricing of Interest Rate Derivatives: The Libor Market Model and Beyond, Princeton University Press.

# **Related Articles**

LIBOR Market Model; Monte Carlo Simulation for Stochastic Differential Equations; Stochastic Taylor Expansions.

> LEIF B.G. ANDERSEN & VLADIMIR V. PITERBARG
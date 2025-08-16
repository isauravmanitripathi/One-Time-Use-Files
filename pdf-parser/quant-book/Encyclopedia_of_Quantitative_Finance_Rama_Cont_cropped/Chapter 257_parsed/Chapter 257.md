# **Partial Integro-differential Equations (PIDEs)**

Partial integro-differential equationss (PIDEs) appear in finance in the context of option pricing in discontinuous models. They generalize the Black-Scholes partial differential equation (PDE) when the continuous Black-Scholes dynamics for the underlying price is replaced by a Markov process with jumps.

The jump models proposed for option pricing are mostly based on Lévy processes (see Exponential Lévy Models). The jumps of a Lévy process are characterized by a positive measure  $\nu(dx)$  on  $\mathbb{R} \setminus \{0\}$ , called Lévy measure, which satisfies the following integrability condition:

$$\int_{\mathbb{R}\setminus\{0\}} \min(1, x^2) \nu(\mathrm{d}x) < \infty \tag{1}$$

In particular, it may be singular at the origin.

Consider an asset whose risk-neutral dynamics are described by an exponential Lévy model  $S_t =$  $S_0 \exp X_t$ , where  $X_t$  is a Lévy process with coefficient  $\sigma$  and Lévy measure  $\nu$  (the drift is determined by the martingale condition on  $e^{-rt}S_t$ ). The value  $V_t =$  $V(t, S_t)$  at time  $t \leq T$  of a European option on this underlying with maturity T and payoff  $H(S_T)$  is then given by the solution of the following PIDE:

$$V_{t} + \frac{1}{2}\sigma^{2}S^{2}V_{SS} + rSV_{S} - rV$$
  
+ 
$$\int \left[ V(t, S e^{y}) - V(t, S) - S(e^{y} - 1)V_{S}(t, S) \right] \nu(dy) = 0 \qquad (2)$$

The subscripts indicate partial derivatives and  $r$ is the continuously compounded risk-free interest rate. We can see that this equation contains the same terms as the Black-Scholes PDE and an integral term with respect to the Lévy measure v. In particular, if v is equal to 0, the integral term disappears and equation (2) reduces to the Black-Scholes equation. This is compatible with the fact that an exponential Lévy model without jumps is simply the Black-Scholes model.

Similar to the diffusion case, the PIDE formulation can be used for other types of options, such as barrier or American options, leading to boundary-value problems or variational inequalities with the same integro-differential operator. The PIDE approach can also be generalized to more complicated cases: for example, stochastic volatility with jumps, nonhomogeneous jump measure  $v_{t,x}(dx)$ , multiasset derivatives (see Jump Processes; Exponential Lévy **Models**). Finally, one can obtain a *forward PIDE*—in maturity and strike variables—for call options, analogous to the Dupire equation (see  $[6, 14]$ ) in one-factor Markovian models with jumps.

We first present the specific features of the integrodifferential equations compared with the PDEs. In particular, we highlight the difficulties that arise for the numerical solution of these equations. We see that the use of standard techniques, such as finite differences or finite elements, is not straightforward. We then survey the existing approaches to adapt numerical methods developed for PDEs to the solution of partial integro-differential equations.

# **General Remarks**

To solve the PIDE (2), it is convenient to make the change of variables  $x = \log(S/S_0)$  and  $\tau = T - t$ . Denote  $v(\tau, x) = e^{r(T-t)}V(t, S) = e^{r\tau}V(T - t)$  $\tau$ ,  $S_0e^x$ ). This leads to the following equation:

$$v_{\tau} = \frac{1}{2}\sigma^{2}v_{xx} + \left(r - \frac{1}{2}\sigma^{2}\right)v_{x}$$
$$+ \int [v(\tau, x + y) - v(\tau, x)$$
$$- (e^{y} - 1)v_{x}(\tau, x)]v(dy) \tag{3}$$

The payoff function provides a terminal condition for (2):  $V(T, S) = H(S)$  and an initial condition for  $equation (3):$ 

$$v(0, x) = H(S_0 e^x) \equiv h(x), \quad x \in \mathbb{R} \tag{4}$$

The main sources of difficulties with the PIDEs of type  $(2)$  or  $(3)$  are the following:

- . nonlocal character of the operator;
- possible lack of regularity of the solution, espe- $\bullet$ cially in the pure jump case ( $\sigma = 0$ ); and
- possible singularity of the Lévy measure at 0. .

Let us get a closer look at these issues. Observe that the operator in equation  $(3)$  is nonlocal in space: that is, to evaluate it at a given point  $(\tau, x_*)$ , we need the values  $v(\tau, x)$  for all  $x \in \mathbb{R}$ . This has multiple implications. First of all, if we consider equation  $(3)$ on a bounded domain in  $x$ , which is always the case if we solve it numerically, the boundary conditions must be specified not only *at* the boundary but also *beyond* the boundary:

$$v(\tau, x) = g(\tau, x) \quad \forall x \notin (x_{\min}, x_{\max}) \tag{5}$$

where  $g$  is a given function. Second, a finite difference or finite element discretization of equation (3) gives rise to a dense matrix, in contrast with the PDE case where the discretized operator is a sparse (usually tridiagonal) matrix easy to invert. The direct solution of a nonsparse linear system of N equations requires, in general,  $O(N^3)$  operations, which makes the direct application of these methods inefficient. Finally, the integral operator propagates possible irregularities of the solution. For instance, the price of a barrier option is usually discontinuous at the barrier. While in the PDE case this discontinuity influences only the neighborhood of the boundary, a PIDE will propagate it inside the domain. It is worth mentioning that the regularity of the solution is not only a theoretical issue but also has a direct impact on the efficiency (stability and order of convergence) of numerical methods.

If the volatility  $\sigma$  is strictly positive (jump diffusion case), the integro-differential operator has the same regularizing property as the differential Black-Scholes operator: the solution is smooth for all  $t < T$  even for discontinuous payoffs. The same is true in the pure jump case (without diffusion component) if there are "sufficiently many" jumps. More precisely, we have the following result  $[15, 16]$ :

**Proposition 1** Let  $H$  be a measurable function with a finite set of discontinuities. Suppose that  $h(x) \equiv H(S_0e^x)$  has at most polynomial growth:  $\exists p \geq 0, |h(x)| \leq C(1+|x|^p)$ . Let X be a Lévy process with characteristic triplet  $(\sigma, \nu, \gamma)$  satisfying  $\int_{|y|>1} |y|^{2p} \nu(dy) < \infty \text{ and}$ 

$$\sigma > 0 \quad or \quad \exists \beta \in (0, 2),$$
  
$$\liminf_{\varepsilon \downarrow 0} \frac{1}{\varepsilon^{2-\beta}} \int_{-\varepsilon}^{\varepsilon} |y|^2 \nu(dy) > 0 \tag{6}$$

Then the forward European option price  $v(\tau, x) =$  $E[h(x+X_{\tau})]$  belongs to the class  $C^{\infty}((0,T]\times$  $\mathbb{R}$ ) with  $\left|\partial^{n+m}v/\partial x^n\partial t^m(x)\right| \leq C(1+|x|^p)$ , for all  $n, m \ge 0$ . Moreover,  $v(\tau, x)$  is a solution of the PIDE  $(3)$  with the initial condition  $(4)$ .

The main idea of the proof is to apply the Itô formula to the discounted option price, which is a martingale, identify the drift term, and put it to 0: this gives the corresponding PIDE (see also **Partial Differential Equations**). The condition (6) ensures the regularity of the option price, so that we can apply the Itô formula. While the condition (6) is satisfied by most of the exponential Lévy models in the literature, there are some exceptions such as the popular Variance Gamma model (see Variance-gamma Model). When equation  $(6)$  is not satisfied, the irregularities in the payoff are not smoothened immediately and the option price may not be sufficiently regular to apply the Itô formula (see the examples in [16]). In the case of barrier options, the option price may be irregular even if  $\sigma > 0$ . This is due to the fact that the irregularity at the barrier is propagated inside the domain by the integral operator.

The possible lack of regularity of option prices led to consider them as different kinds of weak solutions of the PIDEs. Existence and uniqueness of solutions of integro-differential equations in Sobolev spaces has been studied in  $[10]$  and more recently in  $[25, 26,$ 33]. This approach provides the necessary framework for the solution of PIDEs by finite element methods. Another type of weak solution is the viscosity solution (see Monotone Schemes). Viscosity solutions of PIDEs are studied in  $[4, 5, 7, 9, 23, 27-29]$ . This approach is naturally linked to the probabilistic interpretation of the solution [16]. Moreover, it can be shown that any monotone scheme converges to the viscosity solution of the equation (see **Monotone Schemes**). This property is exploited in  $[11, 17]$ .

We stress that Proposition 1 gives the PIDE satisfied by a *European* option price in the relatively simple *exponential Lévy models*. Although a rigorous proof of similar results for more complicated jump models or option types is often not available, the formal derivation of the pricing PIDEs is very easy and is regularly used for numerical valuation of option prices in models with jumps. However, we should be aware that, in many cases, the PIDE approach remains to be justified.

Finally, let us comment on the singularity of the Lévy measure. In pure jump models, such as Variance Gamma or CGMY (see Tempered Stable Process), the jumps are of infinite activity in order to compensate the absence of diffusion component. This implies that the jump measure  $\nu$  is not integrable at 0, which brings an additional difficulty for the discretization of equation (3). For finite element discretization, this is not really a problem because we do not need to discretize  $\nu$  separately but only to evaluate the integral on some basis functions. To solve the PIDE using finite differences, we can approximate small jumps of the Lévy process by a Brownian motion with appropriately chosen volatility. This approximation is based on the results obtained in [8], and its impact on the option price is estimated in  $[17]$ . In the case of jumps of finite variation, as in the Variance Gamma model, it is also possible to replace small jumps by a drift rather than a diffusion term, as done in [24].

## Numerical Solution

To illustrate the issues discussed above, we describe a simple finite difference scheme for equation (3) proposed in [17]. We consider here the case of nonzero diffusion and finite jump measure. As noted above, the general case may be reduced to this one by approximating small jumps.

#### *European Vanilla and Barrier Options*

To solve numerically the integro-differential problem  $(3)-(4)$ , we first need to localize it to a bounded computational domain in  $x$  and truncate the integration domain in the integral part.

Truncation of the integration domain. Since we cannot calculate numerically an integral on the infinite range  $(-\infty, \infty)$ , the domain is truncated to a bounded interval  $(B_l, B_r)$ . In terms of the Lévy process, this corresponds to removing large jumps. Usually, the tails of  $\nu$  decrease exponentially, so the probability of large jumps is small and the impact on the solution of the truncation is exponentially small in the domain size (see  $[17]$  for pointwise estimates).

Localization. Similarly, for the computational purposes, the domain of definition of the equation has to be bounded. For barrier options, the barriers are the natural limits for this domain and the rebate is the natural boundary condition. In the absence of barriers, we have to choose artificial bounds  $(x_{\min}, x_{\max})$ and impose artificial boundary conditions. Recall that "boundary" conditions in this case must extend the

solution beyond the bounds as well (cf. equation  $(5)$ ). It can be shown that any bounded function  $g(\tau, x)$ leads to an exponentially decreasing localization error when the size of the domain increases. However, from the numerical point of view, it is better to take into account the asymptotic behavior of the solution. For instance, a good choice for a put option is  $g(\tau, x) = (K - S_0 e^{x + r\tau})^+$ . Of course, in the case of one barrier option, we need this condition only on one side of the domain: the other is zero or given by the rebate.

**Remark** In [25, 26], the authors subtract the payoff from the option price and solve a PIDE with zero boundary conditions on the excess to payoff. This leads to a source term in the equation which is, in the case of a put option, a Dirac delta-function. This is easily handled in the finite element framework but makes problem for finite difference discretization.

Discretization. We consider now the localized problem on  $(x_{\min}, x_{\max})$ :

on  $(0, T] \times (x_{\min}, x_{\max})$  (7)  $v_{\tau} = Lv$ 

$$v(0, x) = h(x), \qquad x \in (x_{\min}, x_{\max})$$
 (8)

$$v(\tau, x) = g(\tau, x), \quad x \notin (x_{\min}, x_{\max}) \tag{9}$$

where  $L$  is the following integro-differential operator:

$$Lv = \frac{1}{2}\sigma^2 v_{xx} - \left(\frac{1}{2}\sigma^2 - r\right)v_x$$
  
+ 
$$\int_{B_l}^{B_r} v(\mathrm{d}y)v(\tau, x+y) - \lambda v - \alpha v_x \quad (10)$$

with  $\lambda = \int_{B_l}^{B_r} \nu(dy)$ ,  $\alpha = \int_{B_l}^{B_r} (e^y - 1)\nu(dy)$ . We introduce a uniform grid on  $[0, T] \times \mathbb{R}$ :

$$\tau_n = n\Delta t, \quad n = 0, \dots, M,$$
  
$$x_i = x_{\min} + i\Delta x, \quad i \in \mathbb{Z}$$
(11)

with  $\Delta t = T/M$ ,  $\Delta x = (x_{\text{max}} - x_{\text{min}})/N$ . The values of  $v$  on this grid are denoted by  $\{v_i^n\}$ . The space derivatives of  $v$  are approximated by finite differences:

$$(v_{xx})_i \approx \frac{v_{i+1} - 2v_i + v_{i-1}}{(\Delta x)^2} \tag{12}$$

$$(v_x)_i \approx \frac{v_{i+1} - v_i}{\Delta x}$$
 or  $(v_x)_i \approx \frac{v_i - v_{i-1}}{\Delta x}$  (13)

The choice of the approximation of the firstorder derivative—forward or backward difference depends on the parameters  $\sigma$ , r, and  $\alpha$ .

To approximate the integral term, we use the trapezoidal rule with the same discretization step  $\Delta x$ . Choose integers  $K_l$ ,  $K_r$  such that  $[B_l, B_r]$  is contained in  $[(K_l - 1/2)\Delta x, (K_r + 1/2)\Delta x]$ . Then,

$$\int_{B_l}^{B_r} \nu(\mathrm{d}y) \nu(\tau, x_i + y) \approx \sum_{j=K_l}^{K_r} \nu_j v_{i+j} \quad \text{where}$$
$$\nu_j = \int_{(j-1/2)\Delta x}^{(j+1/2)\Delta x} \nu(\mathrm{d}y) \tag{14}$$

Using equations  $(12)$ – $(14)$ , we obtain an approximation for  $Lv \approx D_{\Delta}v + J_{\Delta}v$ , where  $D_{\Delta}v$  and  $J_{\Delta}v$ are chosen as follows:

*Explicit–implicit Scheme.* Without loss of generality, suppose that  $\sigma^2/2 - r < 0$ . Then

$$(D_{\Delta}v)_{i} = \frac{\sigma^{2}}{2} \frac{v_{i+1} - 2v_{i} + v_{i-1}}{(\Delta x)^{2}} - \left(\frac{\sigma^{2}}{2} - r\right) \frac{v_{i+1} - v_{i}}{\Delta x}$$

If  $\sigma^2/2 - r > 0$ , to ensure the stability of the algorithm, we must change the discretization of  $v_x$  by choosing the backward difference instead of the forward one. Similarly, if  $\alpha < 0$  we discretize J as follows:

$$(J_{\Delta}v)_{i} = \sum_{j=K_{l}}^{K_{r}} v_{j}v_{i+j} - \lambda v_{i} - \alpha \frac{v_{i+1} - v_{i}}{\Delta x} \qquad (15)$$

Otherwise, we change the approximation of the first derivative. Finally, we replace the problem  $(7)$ – $(9)$ with the following semiimplicit scheme:

#### Initialization:

$$v_i^0 = h(x_i)$$
 if  $i \in \{0, \dots, N-1\}$  (16)

$$v_i^0 = g(0, x_i) \qquad \text{otherwise} \tag{17}$$

For 
$$\mathbf{n} = 0, \dots, \mathbf{M} - 1$$
:  

$$\frac{v_i^{n+1} - v_i^n}{\Delta t} = (D_\Delta v^{n+1})_i + (J_\Delta v^n)_i$$
if  $i \in \{0, \dots, N-1\}$  (18)

 $v_i^{n+1} = g((n+1)\Delta t, x_i)$ otherwise  $(19)$  Here, the nonlocal operator  $J$  is treated explicitly to avoid the inversion of the fully populated matrix  $J_{\wedge}$ , while the differential part *D* is treated implicitly. At each time step, we first evaluate vector  $J_{\wedge}v^n$ where  $v^n$  is known from the previous iteration, and then solve the tridiagonal system (18) for  $v^{n+1} =$  $(v_0^{n+1}, \ldots, v_{N-1}^{n+1}).$ 

**Remark** A direct computation of the term  $J_{\Delta}v^n$ would require  $O(N^2)$  operations and would be the most expensive step of the method. Fortunately, the particular form of the sum-discrete convolution of two vectors—allows to compute it efficiently and simultaneously for all  $i$  using fast Fourier transform (FFT) (see [21]). Note, however, that this is only possible in the case of a translation invariant jump measure. Another way to solve the problem of the dense matrix, valid also for nonhomogeneous jump models, is proposed in [26]. The authors use a finite element method with a special basis of wavelet functions (see also Wavelet Galerkin Method). In this basis, most of the entries in the matrix operator are very small, so that they can be replaced by zeros without affecting the solution much. The efficiency of the wavelet compression depends on the degree of singularity of the jump measure. Although it does not appear explicitly, this is also the case for the finite difference scheme, because of the trade-off that has to be done between the parameter  $\varepsilon$  of truncation of small jumps and discretization step  $\Delta x$ (see  $[17]$ ). Finally, let us mention  $[31]$  where the integral is evaluated in linear complexity using a recursive formula in the particular case of the Kou model (see **Kou Model**).

*Stability.* The scheme  $(16)$ – $(19)$  is stable if

$$\Delta t < \frac{\Delta x}{|\alpha| + \lambda \Delta x} \tag{20}$$

It is possible to make it unconditionally stable by moving the local terms in equation  $(15)$  in the implicit part. However, numerical experiments show that this leads to large errors for infinite activity Lévy measures.

#### Remark

• In [21, 26, 30–32], fully implicit or Crank-Nicolson finite difference schemes are used, which are unconditionally stable. To solve the resulting dense linear systems, the authors use

iterative methods that require only matrix-vector multiplication performed using FFT.

- Equation  $(2)$  can be solved directly in the original variables. We can also choose a nonuniform grid with, for example, more nodes near the strike and maturity [2, 31]. In this case, an interpolation at each time step is needed in order to apply FFT [21].
- Similar semiimplicit scheme in the finite activity case is used in  $[11]$ . In  $[6]$ , the operator is also split into differential and integral parts, and then an alternating direction implicit (ADI) time stepping is used.
- The situation is more challenging for PIDEs in  $\bullet$ more than one dimension. The main idea here is to devise an operator-splitting scheme as above where each component only acts on one of the variables, thus reducing the dimension in each step of the computation [12, 13, 18].

#### American Options

Pricing American options in jump models leads to integro-differential variational inequalities [10, 27]. Equivalently, option price may be represented as solution of a linear complementarity problem (LCP) of the following form (see also Finite Difference **Methods for Early Exercise Options):** 

$$V_{\tau} - \mathcal{L}V \ge 0 \tag{21}$$

$$V - V^* \ge 0 \tag{22}$$

$$(V_{\tau} - \mathcal{L}V)(V - V^*) = 0 \tag{23}$$

For example, in exponential Lévy models,  $\mathcal{L}$  is the same integro-differential operator as in the PIDE (2) and  $V^*$  is the payoff received upon exercise. Pricing American options in Lévy driven models based on equations (21)–(23) is considered in  $[1-3,$ 19-22, 24, 25, 32, 33]. Numerical solution of the integro-differential problem  $(21)$ – $(23)$  faces globally the same difficulties as that of PIDEs. The dense and nonsymmetric matrix of the operator makes unfeasible or inefficient standard methods for solving LCPs. The solutions proposed rely on similar ideas as in the European case: splitting the operator  $[1, 33]$ , wavelet compression [25], using iterative methods with suitable preconditioning. In [19, 21, 32], the LCP is replaced by an equation with a nonlinear penalty term. We refer to the references cited above for the details on these methods.

### References

- $[1]$ Almendral, A. (2005). Numerical valuation of American options under the CGMY process, in *Exotic* Options Pricing and Advanced Levy Models, A. Kyprianou, W. Schoutens & P. Wilmott, eds, Wiley.
- [2] Almendral, A. & Oosterlee, C.W. (2006). Highly accurate evaluation of European and American options under the variance gamma process, Journal of Computational Finance 10(1), 21-42.
- [3] Almendral, A. & Oosterlee, C.W. (2007). Accurate evaluation of European and American options under the CGMY Process, SIAM Journal on Scientific Computing 29. 93-117.
- Alvarez, O. & Tourin, A. (1996). Viscosity solutions [4] of non-linear integro-differential equations, Annales de l'Institut Henri Poincaré 13(3), 293-317.
- [5] Amadori, A.L. (2003). Nonlinear integro-differential evolution problems arising in option pricing: a viscosity solutions approach, Journal of Differential Integral *Equations*  $16(7)$ , 787–811.
- Andersen, L. & Andreasen, J. (2000). Jump-diffusion [6] models: volatility smile fitting and numerical methods for pricing, Review of Derivatives Research 4(3), 231-262.
- [7] Arisawa, M. (2006). A new definition of viscosity solutions for a class of second-order degenerate elliptic integro-differential equations, Annales de l'Institut Henri Poincaré (C) Non Linear Analysis, 23(5), 695-711.
- [8] Asmussen, S. & Rosiński, J. (2001). Approximations of small jumps of Lévy processes with a view towards simulation. *Journal of Applied Probability* **38**(2), 482–493.
- [9] Barles, G., Buckdahn, R. & Pardoux, E. (1997). Backward stochastic differential equations and integral-partial differential equations, Stochastics and Stochastic Reports 60. 57-83.
- [10] Bensoussan, A. & Lions, J.-L. (1982). Contrôle Impulsionnel et Inéquations Quasi-Variationnelles, Dunod, Paris.
- [11] Briani, M., Natalini, R. & Russo, G. (2007). Implicitexplicit numerical schemes for jump-diffusion processes, Calcolo 44, 33-57.
- [12] Carr, P. & Itkin, A. (2007). A Finite-Difference Approach to the Pricing of Barrier Options in Stochastic Skew *Model*, Working Paper.
- [13] Clift, S. & Forsyth, P. (2008). Numerical solution of two asset jump diffusion models for option valuation, Applied Numerical Mathematics, 58(6), 743-782.
- [14] Cont, R. & Tankov, P. (2008). Financial Modelling with Jump Processes, 2nd Edition, CRC Press.
- [15] Cont, R., Tankov, P. & Voltchkova, E. (2005). Hedging with options in models with jumps, in Stochastic Analysis and Applications: The Abel Symposium 2005 in honor of Kiyosi Ito, F.E. Benth, G. Di Nunno, T. Lindstrom, B. Oksendal & T. Zhang, eds, Springer, pp. 197-218.

- [16] Cont, R. & Voltchkova, E. (2005). Integro-differential equations for option prices in exponential Levy models, ´ *Finance and Stochastics* **9**, 299–325.
- [17] Cont, R. & Voltchkova, E. (2005). Finite difference methods for option pricing in jump-diffusion and exponential Levy models, ´ *SIAM Journal on Numerical Analysis* **43**(4), 1596–1626.
- [18] Farkas, W., Reich, N. & Schwab, C. (2006). *Anisotropic Stable L´evy Copula Processes—Analytical and Numerical Aspects*. Research Report No. 2006-08, Seminar for Applied Mathematics, ETH Zurich. ¨
- [19] d'Halluin, Y., Forsyth, P. & Labahn, G. (2004). A penalty method for American options with jump diffusion processes, *Numerische Mathematik* **97**, 321–352.
- [20] d'Halluin, Y., Forsyth, P. & Labahn, G. (2005). A semi-Lagrangian approach for American Asian options under jump diffusion, *SIAM Journal on Scientific Computing* **27**, 315–345.
- [21] d'Halluin, Y., Forsyth, P. & Vetzal, K. (2005). Robust numerical methods for contingent claims under jump diffusion processes, *IMA Journal on Numerical Analysis* **25**, 87–112.
- [22] Hirsa, A. & Madan, D.B. (2003). Pricing American options under variance gamma, *Journal of Computational Finance* **7**(2), 63–80.
- [23] Jakobsen, E.R. & Karlsen, K.H. (2006). A "maximum principle for semicontinuous functions" applicable to integro-partial differential equations, *Nonlinear Differential Equations Applications* **13**, 137–165.
- [24] Levendorskii, S., Kudryavtsev, O. & Zherder, V. (2005). The relative efficiency of numerical methods for pricing American options under Levy processes, ´ *Journal of Computational Finance* **9**(2), 69–97.
- [25] Matache, A.-M., Nitsche, P.-A. & Schwab, C. (2005). Wavelet Galerkin pricing of American options on Levy- ´ driven assets, *Quantitative Finance* **5**(4), 403–424.
- [26] Matache, A.-M., von Petersdorff, T. & Schwab, C. (2004). Fast deterministic pricing of options on Levy ´ driven assets, *Mathematical Modelling and Numerical Analysis* **38**(1), 37–71.

- [27] Pham, H. (1998). Optimal stopping of controlled jumpdiffusion processes: a viscosity solution approach, *Journal of Mathematical Systems* **8**(1), 1–27.
- [28] Sayah, A. (1991). Equations d'Hamilton Jacobi du premier ordre avec termes integro-differentiels, *Communications in Partial Differential Equations* **16**, 1057–1093.
- [29] Soner, H.M. (1986). Optimal control of jump-Markov processes and viscosity solutions, *IMA Volumes in Mathematics and Applications*, Springer-Verlag, New York, Vol. 10, 501–511.
- [30] Tavella, D. & Randall, C. (2000). *Pricing Financial Instruments: The Finite Difference Method*, Wiley, New York.
- [31] Toivanen, J. (2008). Numerical valuation of European and American options under Kou's jump-diffusion model, *SIAM Journal on Scientific Computing* **30**(4), 1949–1970.
- [32] Wang, I.R., Wan, J.W.L. & Forsyth, P. (2007). Robust numerical valuation of European and American options under the CGMY process, *Journal of Computational Finance* **10**, 31–69.
- [33] Zhang, X.L. (1997). Numerical analysis of American option pricing in a jump-diffusion model, *Mathematics of Operations Research* **22**(3), 668–690.

# **Related Articles**

**Backward Stochastic Differential Equations: Numerical Methods**; **Econometrics of Option Pricing**; **Exponential Levy Models ´** ; **Finite Difference Methods for Barrier Options**; **Finite Difference Methods for Early Exercise Options**; **Jump Processes**; **Lattice Methods for Path-dependent Options**; **Monotone Schemes**; **Option Pricing Theory: Historical Perspectives**; **Partial Differential Equations**; **Stochastic Volatility Models**; **Timechanged Levy Process ´** .

EKATERINA VOLTCHKOVA
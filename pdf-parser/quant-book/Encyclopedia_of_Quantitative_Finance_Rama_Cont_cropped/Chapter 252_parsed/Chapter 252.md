# **Wavelet Galerkin Method**

Wavelet methods in finance are a particular realization of the finite element method (*see* **Finite Element Methods**) that provides a very general PDE-based numerical pricing technique. The methods owe their name to the choice of a wavelet basis in the finite element method. This particular choice of basis allows the method to solve partial integro-differential equations (PIDEs) arising from a very large class of market models. Therefore, wavelet-based finite element methods are well suited for the analysis of model risk and pricing in multidimensional and exotic market models. Since wavelet methods are mesh-based methods they allow for the efficient calculation of Greeks and other model sensitivities.

As for any finite element method, the general setup for wavelet methods can be described as follows. Consider a basket of *d* ≥ 1 assets whose log returns *Xt* are modeled by a Levy or, more generally, a Feller ´ process with state space *<sup>d</sup>* and *X*<sup>0</sup> = *x*. By the fundamental theorem of asset pricing, the arbitragefree price *u* of a European contingent claim with payoff *g(*·*)* on these assets is given by the conditional expectation

$$u(x,t) = \mathbb{E}\left[g(X_t) \mid X_0 = x\right] \tag{1}$$

under an *a priori* chosen equivalent martingale measure (*see* **Exponential Levy Models ´** ). Provided sufficient smoothness of *u*, the price can be obtained as the solution of a PIDE (*see* **Partial Differential Equations**; **Partial Integro-differential Equations (PIDEs)**):

$$\frac{\partial u}{\partial t} + \mathcal{A}u = 0$$
  
$$u(\cdot, 0) = g \tag{2}$$

where A denotes the infinitesimal generator of the process *X*. For the Galerkin-based finite element implementation, equation (2) is converted into variational form on a suitable test space *V* (cf., e.g., [11, 20] and the references therein). The variational pricing equation then reads: find *u* ∈ *V* such that

$$\left\langle \frac{d}{dt}u, v \right\rangle + \mathcal{E}(u, v) = 0 \quad \text{ for all } v \in V \quad (3)$$

where E*(u, v)* := A*u, vL*2×*L*<sup>2</sup> denotes the bilinear form associated to the process *X*. Note that this bilinear form is the central object of discretization in wavelet methods. Owing to the variational formulation (3), wavelet methods are also referred to as *variational methods*.

In one dimension, wavelet methods have been introduced by Matache *et al.* [20, 21]. They were successively applied to American-type contracts (cf. [19, 27]) as well as stochastic volatility models (cf. [14]). In [11], this approach was extended to multidimensional market models based on the sparse tensor product approach and wavelet compression techniques as described in [23, 26] and the references therein.

## **Admissible Pricing Models**

Wavelet-based finite element methods are applicable whenever the variational equation (3) admits a unique solution. Some admissible market models are the multidimensional Black–Scholes model, local volatility models, Kou's model (*see* **Kou Model**), stochastic volatility models (*see* **Barndorff-Nielsen and Shephard (BNS) Models**; **Heston Model**; **Hull–White Stochastic Volatility Model**), one-dimensional Levy models ( ´ *see* **Variancegamma Model**; **Jump-diffusion Models**; **Timechanged Levy Process ´** ; **Exponential Levy Models ´** ), multidimensional Levy copula models (see [11]), ´ as well as models based on time inhomogeneous or nonstationary processes (see [6]). The particular choice of market model determines the particular form of the bilinear form E*(*·*,* ·*)* in equation (3). In all the above market models, the bilinear form is governed by the characteristic triplet *(γ ,* Q*,ν)* of the underlying Levy process. It consists of a drift ´ vector *<sup>γ</sup>* <sup>∈</sup> *<sup>d</sup>* , a covariance matrix <sup>Q</sup> <sup>∈</sup> *<sup>d</sup>*×*<sup>d</sup>* , and a Levy-type measure ´ *ν* that is assumed to be absolutely continuous with density *k(z)*d*z* = *ν(*d*z)*. Then, E*(*·*,* ·*)* is of the abstract form

$$\mathcal{E}(u,v) = \langle \gamma \nabla u, v \rangle + \frac{1}{2} \langle \mathcal{Q} \nabla u, \nabla v \rangle$$
$$- \int_{\mathbb{R}^d} \int_{\mathbb{R}^d} (u(x+f(z)) - u(x)$$
$$- f(z) \cdot \nabla u(x)) v(x) v(\mathrm{d}z) \, \mathrm{d}x \quad (4)$$

Note that in case the underlying process  $X$  is not stationary or time inhomogeneous, the parameters  $(\gamma, \mathcal{Q}, \nu) = (\gamma(x, t), \mathcal{Q}(x, t), \nu(x, t))$  as well as the function  $f(\cdot)$  may depend on space and time (e.g., in models based on Sato processes [6]). Furthermore, the parameters are allowed to degenerate (e.g., in stochastic volatility models). Under rather weak conditions, wavelet-based finite elements methods are still applicable in these cases.

# **Wavelet-based Finite Element** Discretization

The wavelet-based finite element implementation of equation (3) is obtained in three steps: first, the original space domain  $\mathbb{R}^d$  has to be *localized* to a bounded domain  $\Box := [-R, R]^d$ ,  $R > 0$ . Second, the test space  $V$  needs to be *discretized* by an increasing sequence of finite dimensional subspaces  $V^L \subset V$ ,  $L \in \mathbb{N}$ . Third, a *time-stepping* scheme has to be applied to discretize in time.

### Localization

For the localization, we find that in finance truncation of the original x-domain  $\mathbb{R}^d$  to  $\Box$  corresponds to approximating the solution  $u$  of equation (2) by the price  $u_R$  of a corresponding barrier option on  $[e^{-R}, e^{R}]^{d}$ . In case the underlying stochastic process  $X$  admits semiheavy tails, the solution of the localized problem  $u_R$  converges pointwise exponentially to the solution  $u$  of equation (3). There exist constants  $\alpha, \beta > 0$  such that

$$|u(t,x) - u_R(t,x)| \lesssim e^{-\alpha R + \beta \|x\|_{\infty}} \tag{5}$$

It therefore indeed suffices to replace the original price space domain  $\mathbb{R}^d$  by  $\Box = [-R, R]^d$  with sufficiently large  $R > 0$ . For details we refer to [24].

#### Space Discretization

In wavelet methods, the space discretization is based on the concepts of classical finite element methods (see Finite Element Methods). To this end, for any level index  $L \in \mathbb{N}$ , let  $V^L \subset V$  be a subspace of dimension  $N := \dim V^L = \mathcal{O}(h^{-d})$  generated by a tensor product finite element basis  $\Phi_L := \{ \phi_{j,L} : j \in \mathbb{R} \}$  $\Delta_L$ } with some suitable index set  $\Delta_L$  corresponding to a mesh of width  $h = 2^{-L}$ . There holds  $V^L \subset V^{L+1}$  for all  $L \in \mathbb{N}$ . For further details on classical finite element approximations see, for example [10].

Denote by  $\underline{U}_L$  the coefficient vector of  $u$  with respect to  $\Phi_L$ . Then equation (3) is equivalent to: find  $\underline{U}_L(t) \in \mathbb{R}^N$  such that  $\underline{U}_L(0) = \underline{U}_0$  and

$$\mathbf{M}\underline{U}'_{L}(t) + \mathbf{A}\underline{U}_{L}(t) = 0, \quad t \in (0, T) \tag{6}$$

where  $\mathbf{M}$  and  $\mathbf{A}$  are the so-called mass and stiffness matrices.

Straightforward application of standard finite element schemes to calculate the stiffness matrix  $\mathbf{A} = (\mathcal{E}(\phi_{i,L}, \phi_{j,L}))_{i,j \in \Delta_L}$  arising from general market models fails due to two reasons. For high-dimensional models, we have the "curse of dimension": the number of degrees of freedom on a tensor product finite element mesh of width  $h$  in dimension  $d$  grows like  $\mathcal{O}(h^{-d})$  as  $h \to 0$ . For jump models, the nonlocality of the underlying operator implies that the standard finite element stiffness matrix **A** consists of  $\mathcal{O}(h^{-2d})$ nonzero entries, which is not practicable even in one dimension with small mesh widths.

Wavelets can overcome these issues while still being easy to compute. There are three main advantages.

- Break the curse of dimension using sparse tensor products (*see* **Sparse Grids**)  $\Rightarrow$  dimensionindependent complexity (up to log-factors).
- Multiscale compression of jump measure of  $X$  $\Rightarrow$  complexity of jump models can asymptotically be reduced to Black-Scholes complexity.
- Efficient preconditioning.

In one dimension, biorthogonal *complement* or *wave*let bases  $\Psi_L = \{\psi_{j,L} : j \in \nabla_L\}, \nabla_L := \Delta_{L+1} \backslash \Delta_L$ are constructed from the single-scale bases  $\Phi_L$ ; for details see [7, 9, 22]. Denoting by  $W^L$  the span of  $\Psi_L$ , the spaces  $V^{L+1}$  admit a splitting

$$V^{L+1} = W^L \oplus V^L, \quad L > 0 \tag{7}$$

Each wavelet space  $W^L$  can be thought of as describing the increment of information when refining the finite element approximation from  $V^L$  to  $V^{L+1}$ . Furthermore, equation (7) implies that for any  $L > 0$  the finite element space  $V^L$  can be written as a direct *multilevel* sum of the wavelet spaces  $W^{\ell}$ ,  $\ell < L$ . Thus, any  $u_L \in V^L$  has the representation

$$u_L = \sum_{\ell=0}^{L-1} \sum_{j \in \nabla_{\ell}} d_{j,\ell} \psi_{j,\ell} \tag{8}$$

![](_page_2_Figure_0.jpeg)

Figure 1 Schematic of single-scale space  $V^L$  and its decomposition into multiscale wavelet spaces  $W^{\ell}$ 

with suitable coefficients  $d_{i,\ell} \in \mathbb{R}$ . Figure 1 illustrates the decomposition of the finite element space  $V^L$ ,  $L = 4$ , spanned by continuous, piecewise linear (nodal) basis functions  $\phi_{i,L}$  into its increment spaces  $W^{\ell}, \ell = 0, \ldots, 3$ , spanned by wavelets  $\psi_{i,\ell}$ .

In the multidimensional setting, we obtain multivariate wavelet basis functions by using tensor products. The finite element spaces  $V^L$  can then be characterized by

$$V^{L} = \text{span}\left\{\psi_{j_{1},\ell_{1}}(x_{1})\cdots\psi_{j_{d},\ell_{d}}(x_{d})\;:\; \atop \ell_{1},\ldots,\ell_{d} \leq L, \; j_{i} \in \nabla_{\ell_{i}}\right\}$$
(9)

Since these multivariate wavelet bases comprise of products of one-dimensional wavelets, they form *hierarchical bases* as in [12]. Thus, the spaces  $V^L$ can be replaced by *sparse tensor product* spaces

$$\widehat{V}^{L} = \text{span}\left\{ \psi_{j_{1},\ell_{1}}(x_{1}) \cdots \psi_{j_{d},\ell_{d}}(x_{d}) \; : \right.$$
$$\left. \ell_{1} + \ldots + \ell_{d} \leq L, \; j_{i} \in \nabla_{\ell_{i}} \right\} \tag{10}$$

In  $[3, 26]$  it is shown that, under certain smoothness assumptions on the solution  $u$  of equation (3), the sparse tensor product spaces preserve the approximation properties of the full tensor product spaces, while there holds  $\widehat{N} := \text{dim}\widehat{V}^L = \mathcal{O}\left(h^{-1}|\log h|^{d-1}\right) \ll N.$ Herewith, the complexity of the finite element

stiffness matrix can be reduced to  $\mathcal{O}(h^{-2}|\log h|^{2(d-1)})$ instead of the original  $\mathcal{O}(h^{-2d})$  nonzero entries.

Furthermore, wavelet basis functions give rise to certain cancellation properties and norm equivalences as illustrated in, for example [2, 7]. One therefore obtains sharp estimates for the entries of the corresponding stiffness matrix, cf. [20, 23]. Herewith  $a$ *priori* compression schemes can be defined that further reduce the complexity of the stiffness matrix. The compression exploits the fact that the position of large entries in the stiffness matrix arising from a model with jumps resembles the structure of a Black-Scholes stiffness matrix. The remaining entries can *a priori* be proved to be negligible. Therefore, the compression scheme (asymptotically) reduces the complexity of a model with jumps to that of the Black-Scholes model. To give a brief illustration of this idea, in Figure 2, the density pattern of the stiffness matrix of the Black-Scholes model (a) and a Lévy model of tempered-stable-type (b) in one dimension is given.

Combining the compression scheme with the sparse tensor product spaces results in a computational complexity of  $\mathcal{O}(h^{-1}|\log h|^{2(d-1)})$  instead of the original  $\mathcal{O}(h^{-2d})$ . It is proved that these wavelet schemes preserve stability and convergence of the classical finite element schemes, cf. [23].

## Time Stepping

To finally obtain a fully discrete solution of equation (3), there are various methods to approximate the solution of the ordinary differential equation  $(6)$ . These time-stepping methods are not specific to wavelet-based finite element methods. We therefore mention only a few examples here: one obtains algebraic convergence  $\mathcal{O}((\Delta t)^{\alpha})$  in the time step size  $\Delta t$ for all the above market models using the implicit Euler scheme, then  $\alpha = 1$  or the Crank–Nicholson scheme, then  $\alpha = 2$ ; see, for example [1]. Furthermore, exponential convergence rates can be obtained by discretizing equation (6) by a  $hp$ -discontinuous Galerkin (dG) method as in [14, 25].

### **American Contracts**

The price  $u$  of an American-type contract is given by an optimal stopping, free boundary problem:

$$u(t,x) = \sup_{t \le \tau \le T} \mathbb{E}[g(X_\tau) \mid X_t = x] \qquad (11)$$

![](_page_3_Figure_1.jpeg)

**Figure 2** Density pattern for the stiffness matrix **A** for *L* = 8 refinement steps. Matrix for Black–Scholes model (a) and for tempered stable process (b)

with *τ* running over stopping times. The solution of equation (11) then solves a partial integro-differential *inequality* (see [19]). Similar to the variational formulation for European contracts, the wavelet-based finite element implementation solves the corresponding variational inequality: Find *u(t,* ·*)* ∈ *Kg* := {*v* ∈ *V* | *v* ≥ *g* a*.*e*.*} such that

$$\left\langle \frac{\partial u}{\partial t}, v - u \right\rangle + \mathcal{E}(u, v - u) \le 0 \quad \text{for all } v \in K_g$$
(12)

Choosing finite dimensional subspaces *V <sup>L</sup>* ⊂ *V* , as above, to discretize in space and applying a timestepping scheme leads to a sequence of matrix linear complementary problems. For large size *N* = dim*V <sup>L</sup>*, standard solution methods such as projected successive overrelaxation [8] are not suitable, since their rate of convergence depends on *N*. The waveletbased solution algorithm suggested in [19] relies on a fixed point iteration where in each iteration step a *V* –projection *PKg* onto the convex cone *Kg* has to be realized. Owing to norm equivalences of the wavelet basis, the outer fixed point iteration convergences at a rate independent of the dimension *N* of the space *V <sup>L</sup>*. The projection *PKg* is based on a wavelet generalization of the classical Cryer algorithm [8].

## **Sensitivities and Greeks**

As a PDE-based pricing method, wavelet methods are well suited for the fast and accurate calculation of sensitivities of market models with respect to model parameters. Classical examples are variations of option prices with respect to the spot price or with respect to time to maturity, the so-called "Greeks" of the model.

There are two classes of sensitivities: the sensitivity of the solution *u* to variation of a model parameter, like the Greek Vega (*∂σ u*), and the sensitivity of the solution *u* to a variation of the state space such as the Greek Delta (*∂xu*).

Suppose that the infinitesimal generator A of *X* depends on a parameter *η*. We write *u(η*0*)* for a fixed parameter *η*<sup>0</sup> to emphasize the dependence of *u* on *η*0. Then, the derivative of *u* with respect to *η*

$$\widetilde{u}(\delta\eta) := \lim_{s \to 0^+} \frac{1}{s} \Big( u(\eta_0 + s\delta\eta) - u(\eta_0) \Big) \tag{13}$$

is the solution of the PIDE (see [15])

$$\partial_t \widetilde{u}(\delta \eta) + \mathcal{A}(\eta_0) \widetilde{u}(\delta \eta) = -D_\eta \mathcal{A}u(\eta_0)$$
$$\widetilde{u}(\delta \eta)(0, \cdot) = 0 \quad \text{in } \mathbb{R}^d \tag{14}$$

where *Dη*A is the derivative of A with respect to *η*. Therefore, the derivative of *u* with respect to *η* can be obtained as a solution of the same pricing PIDE with a right-hand side depending on *u*, cf. [15].

For sensitivities with respect to a variation of the state space, a finite difference like differentiation procedure is presented in [15], which allows to obtain the sensitivities from the finite element forward price without additional forward solver.

## **Numerical Examples**

In this section, we illustrate the use of wavelet-based finite element methods by a number of numerical examples.

#### Multidimensional Lévy Models

We consider a two-dimensional basket with payoff  $g = \left(\frac{1}{2}(S_1 + S_2) - K\right)^{+}$ , strike  $K = 1$ , and maturity  $\tilde{T} = 1$ . The price process is a pure jump process, which is given by the Clayton copula [16] and tempered stable margins [5]. The parameters are  $C = (1, 1), G = (10, 10), M = (10, 10),$  and  $Y = (0.5, 1.5)$ . The copula depends on a parameter  $\theta > 0$  parameterizing the dependence among jumps. Different values for  $\theta$  are used to analyze the different dependence structures. In Figure 3, we compare the model with a Black-Scholes model having the same marginal variances and the same correlation.

## American-type Options in Lévy Models

We consider the finite horizon multiple stopping time problem as in  $[4]$  arising from swing options with maturity  $T = 1$  and interest rate  $r = 0.05$ . The holder has  $p = 5$  exercise rights and there is a refracting time  $\delta = 0.1$  after each exercise. For computational details, see [27]. The computed prices and the exercise boundary are shown in Figure 4 where we use a tempered stable/CGMY model [5] and computed a swing put option with up

![](_page_4_Figure_8.jpeg)

Figure 3 Time value for basket options using a Lévy model (a) and Black–Scholes model (b)

![](_page_4_Figure_10.jpeg)

Figure 4 Swing option price (a) and exercise boundary (b) of a put option with up to six exercise rights

![](_page_5_Figure_1.jpeg)

**Figure 5** Convergence rates of sensitivities for a European call in the variance Gamma (a) and Heston (b) model

to five exercise rights and strike  $K = 100$ . The model parameters are  $C = 1$ ,  $G = 10$ ,  $M = 10$ , and  $Y =$ 0.5. In contrast to the result in the Black-Scholes model, the exercise boundary values in a Lévy model never reach the option's strike price, which is well known for American options [17, 19].

#### Sensitivities

We compute various sensitivities for the variance Gamma [18] and the Heston model [13] where the price is known in closed form such that we are able to compute the errors between the exact price/sensitivities and their finite element approximations.

We consider a European call with strike  $K = 1$ and maturity  $T = 0.5$ . For the variance Gamma model, we calculate the Greeks Delta,  $\Delta = \partial u / \partial S$ , and Gamma,  $\Gamma = \partial^2 u / \partial S^2$ , and use the parameters  $\sigma = 0.4$ ,  $\nu = 0.04$ , and  $\vartheta = -0.2$ . For the Heston model, we calculate the sensitivities  $\widetilde{u}(\delta\rho)$  and  $\widetilde{u}(\delta\alpha)$ with respect to correlation  $\rho$  of the Brownian motions that drive the underlying and the volatility and the rate of mean reversion  $\alpha$ . The model parameters are  $\lambda = 0, \sigma = 0.5, m = 0.06, \rho = -0.5, \text{ and } \alpha = 2.5.$ 

The convergence rates are shown in Figure 5. All sensitivities convergence with the same rate as the price  $u$  itself [15].

## References

Achdou, Y. & Pironneau, O. (2005). Computational [1] methods for option pricing, Frontiers in Applied Mathematics, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, Vol. 30.

- [2] Bramble, J.H., Cohen, A. & Dahmen, W. (2003). Multiscale problems and methods in numerical simulations, Lecture Notes in Mathematics, Springer-Verlag, Berlin, Vol. 1825.
- [3] Bungartz, H.-J. & Griebel, M. (1999). A note on the complexity of solving Poisson's equation for spaces of bounded mixed derivative, Journal of Complexity 15,  $167 - 199$
- [4] Carmona, R. & Touzi, N. (2006). Optimal multiple stopping and valuation of swing options, Mathematical Finance, 18(2), 239-268.
- Carr, P., Geman, H., Madan, D.B. & Yor, M. (2002). [5] The fine structure of assets returns: an empirical investigation, Journal of Business 75(2), 305-332.
- [6] Carr, P., Geman, H., Madan, D.B. & Yor, M. (2007). Self-decomposability and option pricing, Mathematical Finance  $17(1), 31-57.$
- Cohen, A. (2003). Numerical Analysis of Wavelet Meth-[7] ods, Elsevier, Amsterdam.
- [8] Cryer, C.W. (1971). The solution of a quadratic programming problem using systematic overrelaxation, SIAM Journal of Control 9(3), 385-392.
- [9] Dahmen, W., Kunoth, A. & Urban, K. (1999). Biorthogonal spline wavelets on the interval-stability and moment conditions, Applied and Computational Harmonic Analysis 6, 259-302.
- $[10]$ Ern, A. & Guermond, J.-L. (2004). Theory and Practice of Finite Elements, Springer Verlag, New York.
- $[11]$ Farkas, W., Reich, N. & Schwab, C. (2007). Anisotropic stable Lévy copula processes—analytical and numerical aspects, Mathematical Models and Methods in Applied Sciences 17, 1405-1443.
- [12] Griebel, M. & Oswald, P. (1995). Tensor product type subspace splittings and multilevel iterative methods for anisotropic problems, Advances in Computational Mathematics 4, 171-206.
- [13] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility, with applications to bond and

currency options, *The Review of Financial Studies* **6**, 327–343.

- [14] Hilber, N., Matache, A.-M. & Schwab, C. (2005). Sparse wavelet methods for option pricing under stochastic volatility, *The Journal of Computational Finance* **8**(4), 1–42.
- [15] Hilber, N., Schwab, C. & Winter, C. (2008). Variational Sensitivity Analysis of Parametric Markovian Market Models, in *Advances in Mathematics in Finance*, L. Stettner, ed, Banach Center Publications Vol. **83**, 85–106.
- [16] Kallsen, J. & Tankov, P. (2006). Characterization of dependence of multidimensional Levy processes using ´ Levy copulas, ´ *Journal of Multivariate Analysis* **97**, 1551–1572.
- [17] Levendorski˘i, S.Z. (2004). Early exercise boundary and option prices in Levy driven models, ´ *Quantitative Finance* **4**(5), 525–547.
- [18] Madan, D.B., Carr, P. & Chang, E. (1998). The variance gamma process and option pricing, *European Finance Review* **2**, 79–105.
- [19] Matache, A.-M., Nitsche, P.-A. & Schwab, C. (2005). Wavelet Galerkin pricing of American options on Levy ´ driven assets, *Quantitative Finance* **5**(4), 403–424.
- [20] Matache, A.-M., Petersdorff, T. & Schwab, C. (2004). Fast deterministic pricing of options on Levy driven ´ assets, *M2AN Mathematical Modelling and Numerical Analysis* **38**(1), 37–71.

- [21] Matache, A.-M., Schwab, C. & Wihler, T.P. (2006). Linear complexity solution of parabolic integro-differential equations, *Numerical Mathematics* **104**(1), 69–102.
- [22] Nguyen, H. & Stevenson, R. (2003). Finite elements on manifolds, *IMA Journal of Numerical Analysis* **23**, 149–173.
- [23] Reich, N. (2008). *Wavelet Compression of Anisotropic Integrodifferential Operators on Sparse Tensor Product Spaces*, PhD Thesis, ETH, Zurich.
- [24] Reich, N. Schwab, C. & Winter, C. (2008). *Anisotropic multivariate L´evy processes and their Kolmogorov equation*, research report no. 2008-03, *Seminar for Applied Mathematics*, ETH, Zurich.
- [25] Schotzau, D. & Schwab, C. (2001). ¨ *hp*-discontinuous Galerkin time-stepping for parabolic problems, *Comptes Rendus de l'Academie des Sciences Series I Mathematics*, **333**(12).
- [26] von Petersdorff, T. & Schwab, C. (2004). Numerical solution of parabolic equations in high dimensions, *M2AN Mathematical Modelling and Numerical Analysis* **38**(1), 93–127.
- [27] Wilhelm, M. & Winter, C. (2008). Finite element valuation of swing options, *Journal of Computational Finance* **11**(3), 107–132.

NORBERT HILBER, NILS REICH & CHRISTOPH WINTER
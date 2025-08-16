# **Affine Models**

# Definition

**Notation 1** *Throughout the article,*  $\langle \cdot, \cdot \rangle$  *denotes the* standard scalar product on  $\mathbb{R}^N$ .

**Definition 1** Let  $r_t$  be a short-rate model specified as an affine function of an N-dimensional Markov process  $X_t$  with state space  $D \subseteq \mathbb{R}^N$ :

$$r_t = l + \langle \lambda, X_t \rangle \tag{1}$$

for some (nontime-dependent) constants  $l \in \mathbb{R}$  and  $\lambda \in \mathbb{R}^N$ . This is called an affine term structure model (ATSM) if the zero-coupon bond price has exponential-affine form, that is,

$$P(t,T) = \mathbb{E}\left[e^{-\int_t^T r_s \mathrm{d}s} \Big| X_t\right]$$
$$= e^{G(t,T) + \langle H(t,T), X_t \rangle} \tag{2}$$

where  $\mathbb{E}$  denotes the expectation under a risk neutral probability measure.

# **Early Examples**

Early well-known examples are the Vasiček [14] and the Cox et al. [5] (see Term Structure Models; Cox-Ingersoll-Ross (CIR) Model) time-homogeneous one-factor short-rate models. In equation (1), both models are characterized by  $N = 1$ ,  $l = 0$ , and  $\lambda = 1$ .

## Vasiček Model

 $X_t$  follows an Ornstein-Uhlenbeck process on  $D=\mathbb{R},$ 

$$dX_t = (b + \beta X_t) dt + \sigma dW_t, \quad b, \beta \in \mathbb{R}, \quad \sigma \in \mathbb{R}_+$$
(3)

where  $W_t$  is a standard Brownian motion. Under these model specifications, bond prices can be explicitly calculated and the corresponding coefficients  $G$  and  $H$  in equation (2) are given by

$$H(t,T) = \frac{1 - e^{\beta(T-t)}}{\beta}$$

$$G(t,T) = \frac{\sigma^2}{2} \int_t^T H^2(s,T) \, \mathrm{d}s$$
$$+ b \int_t^T H(s,T) \, \mathrm{d}s \tag{4}$$

provided that  $\beta \neq 0$  (see also **Term Structure** Models).

## Cox-Ingersoll-Ross Model

 $X_t$  is defined as the solution of the following affine diffusion process on  $D = \mathbb{R}_+$ , known as *Feller* square root process,

$$\begin{aligned} \mathrm{d}X_t &= (b + \beta X_t) \,\mathrm{d}t + \sigma \sqrt{X_t} \,\mathrm{d}W_t \\ b, \sigma \in \mathbb{R}_+, \quad \beta \in \mathbb{R} \end{aligned} \tag{5}$$

Like in the Vasiček model, there is a closed-form solution for the bond price. If  $\sigma \neq 0$ , G and H in equation  $(2)$  are then of the form:

$$G(t,T) = \frac{2b}{\sigma^2} \ln \left( \frac{2\gamma e^{(\gamma-\beta)(T-t)/2}}{(\gamma-\beta)(e^{\gamma(T-t)}-1)+2\gamma} \right)$$
$$H(t,T) = \frac{-2(e^{\gamma(T-t)}-1)}{(\gamma-\beta)(e^{\gamma(T-t)}-1)+2\gamma} \tag{6}$$

where  $\gamma := \sqrt{\beta^2 + 2\sigma^2}$  (see also **Cox–Ingersoll–** Ross (CIR) Model).

Since the development of these first onedimensional term structure models, many multifactor extensions have been considered with the aim to provide more realistic models.

## **Regular Affine Processes**

The generic method to construct ATSMs is to use regular affine processes. A concise mathematical foundation was provided by Duffie et al. [8]. Henceforth, we fix the state space  $D = \mathbb{R}^m_+ \times \mathbb{R}^{N-m}$ , for some  $0 \le m \le N$ .

**Definition 2** A Markov process  $X$  is called regular affine if its characteristic function has exponentialaffine dependence on the initial state, that is, for  $t \in \mathbb{R}_+$  and  $u \in i \mathbb{R}^N$ , there exist  $\phi(t, u) \in \mathbb{C}$  and  $\psi(t, u) \in \mathbb{C}^N$ , such that for all  $x \in D$ 

$$\mathbb{E}\left[e^{\langle u,X_t\rangle}\middle|X_0=x\right] = e^{\phi(t,u) + \langle\psi(t,u),x\rangle} \tag{7}$$

Moreover, the functions  $\phi$  and  $\psi$  are continuous in t and  $\partial_t^+ \phi(t,u)|_{t=0}$  and  $\partial_t^+ \psi(t,u)|_{t=0}$  exist and are *continuous at*  $u = 0$ .

Regular affine processes have been defined and completely characterized in [8]. The main result is stated below.

**Theorem 1** A regular affine process is a Feller semimartingale with infinitesimal generator

$$\begin{split} \mathcal{A}f(x) &= \sum_{k,l=1}^{N} A_{kl}(x) \frac{\partial^2 f(x)}{\partial x_k \partial x_l} \\ &+ \langle B(x), \nabla f(x) \rangle - C(x) f(x) \\ &+ \int_{D \setminus \{0\}} (f(x+\xi) - f(x) \\ &- \langle \nabla f(x), \chi(\xi) \rangle) M(x, \, \mathrm{d}\xi) \end{split} \tag{8}$$

for  $f$  in the set of smooth test functions, with

$$A(x) = a + \sum_{i=1}^{m} x_i \alpha_i, \quad a, \alpha_i \in \mathbb{R}^{N \times N} \quad (9)$$

$$B(x) = b + \sum_{i=1}^{N} x_i \beta_i, \quad b, \beta_i \in \mathbb{R}^N \qquad (10)$$

$$C(x) = c + \sum_{i=1}^{m} x_i \gamma_i, \quad c, \gamma_i \in \mathbb{R}_+ \tag{11}$$

$$M(x, d\xi) = m(d\xi) + \sum_{i=1}^{m} x_i \mu_i(d\xi)$$
 (12)

where  $m, \mu_i$  are Borel measures on  $D\{0\}$  and  $\chi: \mathbb{R}^N \to \mathbb{R}^N$  some bounded continuous truncation function with  $\chi(\xi) = \xi$  in a neighborhood of 0. Furthermore,  $\phi$  and  $\psi$  in equation (7) solve the generalized Riccati equations,

$$\partial_t \phi(t, u) = F(\psi(t, u)), \quad \phi(0, u) = 0 \quad (13)$$

$$\partial_t \psi(t, u) = R(\psi(t, u)), \quad \psi(0, u) = u \quad (14)$$

with

$$F(u) = \langle au, u \rangle + \langle b, u \rangle - c$$

$$+\int_{D\setminus\{0\}} \Big(\mathrm{e}^{\langle u,\xi\rangle}-1-\langle u,\chi(\xi)\rangle\Big) m(\mathrm{d}\xi) \tag{15}$$

$$R_{i}(u) = \langle \alpha_{i}u, u \rangle + \langle \beta_{i}, u \rangle - \gamma_{i}$$
  
+ 
$$\int_{D \setminus \{0\}} \left( e^{\langle u, \xi \rangle} - 1 - \langle u, \chi(\xi) \rangle \right) \mu_{i}(\mathrm{d}\xi)$$
  
for  $i \in \{1, \dots, m\}$  (16)

$$R_i(u) = \langle \beta_i, u \rangle, \quad \text{for } i \in \{m+1, \dots, N\}$$

Conversely, for any choice of admissible parameters  $a, \alpha_i, b, \beta_i, c, \gamma_i, m, \mu_i$ , there exists a unique regular affine process with generator (8).

 $(17)$ 

**Remark 1** It is worth noting that the infinitesimal generator of every Feller process on  $\mathbb{R}^N$  has the form of the above integro-differential operator (8) with some functions  $A$ ,  $B$ ,  $C$  and a kernel  $M$ . The specific characteristic of regular affine processes is that these functions are all affine, as described in equations  $(9-12)$ .

Observe furthermore that by the definition of the infinitesimal generator and the form of  $F$  and  $R$ , we have

$$\frac{\mathrm{d}}{\mathrm{d}t} \mathbb{E} \left[ \mathrm{e}^{\langle u, X_t \rangle} \Big| X_0 = x \right] \Big|_{t=0_+}$$
$$= \left( \partial_t^+ \phi(t, u) \Big|_{t=0} + \partial_t^+ \psi(t, u) \Big|_{t=0} \right) \mathrm{e}^{\langle u, x \rangle}$$
$$= \left( F(u) + \langle R(u), x \rangle \right) \mathrm{e}^{\langle u, x \rangle} = \mathcal{A} \mathrm{e}^{\langle u, x \rangle} \tag{18}$$

This gives the link between the form of the operator  $\mathcal{A}$  and the functions  $F$  and  $R$  in the Riccati equations (13) and (14).

Remark 2 The above parameters satisfy certain admissibility conditions guaranteeing the existence of the process in  $D$ . These parameter restrictions can be found in Definition 2.6 and equations  $(2.23)$ – $(2.24)$ in  $[8]$ . We note that admissibility, in particular, means  $\alpha_{i,kl} = 0$  for  $i, k, l \leq m$  unless  $k = l = i$ .

## **Systematic Analysis**

## Regular Affine Processes and ATSMs

Regular affine processes generically induce ATSMs. This relation is explicitly stated in the subsequent argument. Under some technical conditions that are specified in [8, Chapter 11], we have for  $r_t$  as defined in equation  $(1)$ ,

$$\mathbb{E}\left[e^{-\int_0^t r_s \mathrm{d}s} \mathrm{e}^{\langle u, X_t \rangle} \middle| X_0 = x\right] = \mathrm{e}^{\widetilde{\phi}(t,u) + \langle \widetilde{\psi}(t,u), x \rangle} \quad (19)$$

where

$$\begin{aligned} \partial_t \widetilde{\psi}(t, u) &= \widetilde{F}(\widetilde{\psi}(t, u)) \\ \partial_t \widetilde{\psi}(t, u) &= \widetilde{R}(\widetilde{\psi}(t, u)) \end{aligned} \tag{20}$$

with  $\widetilde{F}(u) = F(u) - l$  and  $\widetilde{R}(u) = R(u) - \lambda$ . Setting  $u = 0$  in equation (19), one immediately gets equation (2) with  $G(t,T) = \phi(T-t,0)$  and  $H(t,T) =$  $\psi(T-t,0).$ 

#### Diffusion Case

Conversely, for a class of diffusions

$$dX_t = B(X_t) dt + \sigma(X_t) dW_t \tag{21}$$

on  $D$ , Duffie and Kan [7] analyzed when equation (2) implies an affine diffusion matrix  $A = \frac{\sigma \sigma^T}{2}$  and an affine drift  $B$  of form equations (9) and (10), respectively.

#### One-dimensional Nonnegative Markov Process

For  $D = \mathbb{R}_+$ , Filipović [9] showed that equation (1) defines an ATSM if and only if  $X_t$  is a regular affine process.

#### Relation to Heath-Jarrow-Morton Framework

Filipović and Teichmann [10] established a relation between the Heath-Jarrow-Morton (HJM) framework (see **Heath–Jarrow–Morton Approach**) and ATSMs: essentially, all generic finite dimensional realizations<sup>a</sup> of a HJM term structure model are timeinhomogeneous ATSMs.

## **Canonical Representation**

An ATSM stemming from a regular affine diffusion process X on  $\mathbb{R}^m_+ \times \mathbb{R}^{N-m}$  can be represented in different ways by applying nonsingular affine transformations to  $X$ . Indeed, for every nonsingular  $N \times N$ -matrix  $K$  and  $\kappa \in \mathbb{R}^N$ , the transformation

 $KX + \kappa$  modifies the particular form of equation (21) and the short-rate process (1), while observable quantities (e.g., the term structure or bond prices) remain unchanged. To group those  $N$ -dimensional ATSMs generating identical term structures, Dai and Singleton [6] found  $N + 1$  subfamilies  $A_m(N)$ , where  $0 < m < N$  is the number of state variables actually appearing in the diffusion matrix (i.e., the dimension of the positive half space). For each class, they specified a canonical representation whose diffusion matrix  $\sigma \sigma^T$  is of diagonal form with

$$(\sigma \sigma^T(x))_{kk} = \begin{cases} x_k, & k \le m \\ 1 + \sum_{i=1}^m \lambda_{k,i} x_i, & k > m \end{cases} (22)$$

where  $\lambda_{k,i} \in \mathbb{R}$ . For  $N \leq 3$  the Dai–Singleton specification comprises all ATSMs generated by regular affine diffusions on  $\mathbb{R}^m_+ \times \mathbb{R}^{N-m}$ . The general situation  $N > 3$  was analyzed by Cheridito *et al.* [4].

## **Empirical Aspects**

Pricing

The price of a claim with payoff function  $f(X_t)$  is given by the risk neutral expectation formula:

$$\pi(t,x) = \mathbb{E}\left[e^{-\int_0^t r_s \, \mathrm{d}s} f(X_t) \middle| X_0 = x\right] \tag{23}$$

Suppose that  $f$  can be expressed by

$$f(x) = \int_{\mathbb{R}^N} e^{(C+i\lambda, x)} \widetilde{f}(\lambda) d\lambda, \quad \lambda \in \mathbb{R}^N \qquad (24)$$

for some integrable function  $\tilde{f}$  and some constant  $C \in \mathbb{R}^N$ . If, moreover,

$$\mathbb{E}\left[e^{-\int_0^t r_s \, \mathrm{d}s} e^{\langle C, X_t\rangle} \middle| X_0 = x\right] < \infty \tag{25}$$

then equation  $(19)$  implies

$$\begin{split} \pi(t,x) &= \mathbb{E}\bigg[e^{-\int_0^t r_s \, \mathrm{d}s} \bigg(\int_{\mathbb{R}^N} \mathrm{e}^{\langle C+i\lambda, X_t\rangle} \widetilde{f}(\lambda) \, \mathrm{d}\lambda\bigg) \bigg| X_0 = x\bigg] \\ &= \int_{\mathbb{R}^N} \mathbb{E}\bigg[e^{-\int_0^t r_s \, \mathrm{d}s} \mathrm{e}^{\langle C+i\lambda, X_t\rangle} \bigg| X_0 = x\bigg] \widetilde{f}(\lambda) \, \mathrm{d}\lambda \\ &= \int_{\mathbb{R}^N} \mathrm{e}^{\widetilde{\phi}(t, C+i\lambda) + \langle \widetilde{\psi}(t, C+i\lambda), x \rangle} \widetilde{f}(\lambda) \, \mathrm{d}\lambda \end{split} \tag{26}$$

Hence, the price  $\pi(t, x)$  can be computed *via* numerical integration, since the integrands are, in principle, known. For instance, in the case  $N = 1$ , the payoff function of a European call  $(e^x - e^k)^+$ , where x corresponds to the log price of the underlying and  $k$  to the log strike price, satisfies equation (24). In particular, we have the following integral representation (see  $[11]$ ):

$$(\mathbf{e}^{x} - \mathbf{e}^{k})^{+} = \frac{1}{2\pi} \int_{\mathbb{R}} \mathbf{e}^{(C+i\lambda)x} \frac{\mathbf{e}^{k(1-C-i\lambda)}}{(C+i\lambda)(C+i\lambda-1)} \mathrm{d}\lambda \tag{27}$$

Therefore, the previous formula to compute the price of the call  $\pi(t, x)$  is applicable. An alternative approach leading to the same result can be found in [3].

#### Estimation

Statistical methods to estimate the parameters of ATSMs have been based on maximum likelihood and generalized method of moments.

Concerning maximum likelihood techniques, the conditional log densities entering into the log likelihood function can, in general, be obtained by inverse Fourier transformation. Since this procedure is computationally costly, several approximations and limited-information estimation strategies have been considered (e.g., [13]). Another possibility is to use closed-form expansions of the log likelihood function, which are available for general diffusions [1] and which have been applied to ATSMs. In the case of Gaussian and Cox-Ingersoll-Ross models, one can forgo such techniques, since the log densities are known in closed form (e.g., [12]).

As conditional moments of the form  $\mathbb{E}[X_{t}^{m}X_{t}^{n}]$ for  $m, n \ge 0$  can be computed from the derivatives of the conditional characteristic function and are, in general, explicitly known up to the solution of the Riccati ordinary differential equations (ODEs) (13) and  $(14)$ , the generalized method of moments is an alternative to maximum likelihood estimation (e.g., [2]).

## Acknowledgments

Authors Christa Cuchiero and Josef Teichmann gratefully acknowledge the support from the FWF-grant Y 328 (START prize from the Austrian Science Fund). Damir Filipovic gratefully acknowledges the support from WWTF (Vienna Science and Technology Fund).

## **End Notes**

<sup>a.</sup>For a precise definition, see  $[10]$ .

# References

- [1] Ait-Sahalia, Y. (2008). Closed-form likelihood expansions for multivariate diffusions, Annals of Statistics 36, 906-937.
- [2] Andersen, T.G. & Sørensen, B.E. (1996). GMM estimation of a stochastic volatility model: A Monte Carlo study, Journal of Business & Economic Statistics 14, 328-352.
- [3] Carr, P. & Madan, D. (1998). Option valuation using the fast Fourier transform, Journal of Computational Finance 2, 61-73.
- [4] Cheridito, P., Filipović, D. & Kimmel, R.L. A note on the Dai-Singleton canonical representation of affine term structure models. Forthcoming in Mathematical Finance.
- Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory [5] of the term structure of interest rates, *Econometrica* 53,  $385 - 407$
- [6] Dai, Q. & Singleton, K.J. (2000). Specification analysis of affine term structure models, Journal of Finance 55, 1943-1978
- Duffie, D. & Kan, R. (1996). A yield-factor model of [7] interest rates, Mathematical Finance 6, 379-406.
- Duffie, D., Filipović, D. & Schachermayer, W. (2003). [8] Affine processes and applications in finance, *The Annals* of Applied Probability 13, 984-1053.
- Filipović, D. (2001). A general characterization of [9] one factor affine term structure models, Finance and Stochastics 5, 389-412.
- [10] Filipović, D. & Teichmann, J. (2004). On the geometry of the term structure of interest rates, Proceedings of The Royal Society of London. Series A. Mathematical, Physical and Engineering Sciences 460, 129-167.
- Hubalek, F., Kallsen, J. & Krawczyk, L. (2006).  $[111]$ Variance-optimal hedging for processes with stationary independent increments, Annals of Applied Probability 16, 853-885.
- [12] Pearson, N.D. & Sun, T.-S. (1994). Exploiting the conditional density in estimating the term structure: An application to the Cox, Ingersoll, and Ross model, Journal of Finance 49, 1279-1304.
- [13] Singleton, K.J. (2001). Estimation of affine asset pricing models using the empirical characteristic function, Journal of Econometrics 102, 111-141.
- [14] Vasiček, O. (1977). An equilibrium characterization of the term structure, Journal of Financial Economics 5, 177-188.

# **Related Articles**

**Cox–Ingersoll–Ross (CIR) Model**; **Gaussian Interest-Rate Models**; **Heath–Jarrow–Morton** **Approach**; **Heston Model**; **Simulation of Squareroot Processes**; **Term Structure Models**.

> CHRISTA CUCHIERO, JOSEF TEICHMANN & DAMIR FILIPOVIC
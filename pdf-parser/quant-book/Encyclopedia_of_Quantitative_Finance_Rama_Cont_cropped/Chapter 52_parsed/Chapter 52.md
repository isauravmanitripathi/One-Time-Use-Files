# **Sauared Bessel Processes**

Squares of Bessel processes enjoy both an additivity property and a scaling property, which are, arguably, the main reasons why these processes occur naturally in a number of Brownian, or linear diffusion, studies. This survey is written in a minimalist manner; the aim is to refer the reader to a few references where many facts and formulae are discussed in detail.

#### Squared Bessel (BESO) Processes

A squared Bessel (BESQ) process  $(X_t^{(x,\delta)}, t \ge 0)$  may be defined (in law) as the solution of the stochastic differential equation:

$$X_t = x + 2 \int_0^t \sqrt{X_s} \mathrm{d}\beta_s + \delta t \ , \quad X_t \ge 0 \quad (1)$$

where x is the starting value:  $X_0 = x$ ,  $\delta$  is the so-called dimension of X, and  $(\beta_s)_{s>0}$  is standard Brownian motion. For any integer dimension  $\delta$ ,  $(X_t, t > 0)$  may be obtained as the square of the Euclidean norm of  $\delta$ -dimensional Brownian motion.

The general theory of stochastic differential equations (SDEs) ensures that equation  $(1)$  enjoys pathwise uniqueness, hence uniqueness in law, and consequently the strong Markov property. Denoting by  $Q_r^{\delta}$ the law of  $(X_t)_{t>0}$ , solution of equation (1), on the canonical space  $C_{+} \equiv C(\mathbb{R}_{+}, \mathbb{R}_{+}),$  where  $(Z_{u}, u \geq$ 0) is taken as the coordinate process, there is the convolution property:

$$Q_x^{\delta} * Q_{x'}^{\delta'} = Q_{x+x'}^{\delta+\delta'} \tag{2}$$

which holds for all  $x, \delta \ge 0$  ([7]); in other terms, adding two independent BESQ processes yields another BESQ process, whose starting point, respectively dimension, is the sum of the starting points, respectively dimensions.

It follows from equation (2) that for any positive measure  $\mu(\mathrm{d}u)$  on  $\mathbb{R}_+$  such that  $\int \mu(\mathrm{d}u)(1+u) <$  $\infty$ , then, if  $I_{\mu} = \int \mu(\mathrm{d}u) Z_{u}$ ,  $Q_x^{\delta} \left( \exp{-\frac{1}{2}I_{\mu}} \right) = (A_{\mu})^{\delta} (B_{\mu})^x$ (3) with  $A_{\mu} = (\phi_{\mu}(\infty))^{1/2}$ ;  $B_{\mu} = \exp(\phi_{\mu}'(0+))$  for  $\phi_{\mu}$ ,<br>the unique decreasing solution of the Sturm-Liouville equation:  $\phi'' = \phi \mu$ ;  $\phi(0) = 1$ .

Equation (3) may be considered as the (generalized) Laplace transform (with argument  $\mu$ ) of the probability  $Q_x^{\delta}$ , while as  $Q_x^{\delta}$ , for any fixed  $\delta$  and x, is infinitely divisible, the next formula is the Lévy Khintchine representation of  $Q_r^{\delta}$ :

$$Q_x^{\delta} \left( \exp{-\frac{1}{2}I_{\mu}} \right)$$
  
=  $\exp\left(-\int_{C_+} M_{x,\delta}(\mathrm{d}z) \left(1 - \mathrm{e}^{-\frac{1}{2}I_{\mu}(z)}\right) \right)$  (4)

where  $M_{x,\delta} = xM + \delta N$ , for M and N two  $\sigma$ -finite measures on  $C_{+}$ , which are described in detail in, for example, [5] and [6].

## **Brownian Local Times and BESQ** Processes

The Ray-Knight theorems for Brownian local times  $(L^y_t; y \in \mathbb{R}, t \ge 0)$  express the laws of  $(L^y_T; y \in \mathbb{R})$ for some very particular stopping times in terms of certain  $Q_r^{\delta}$ 's, namely,

1. if  $T = T_a$  is the first hitting time of *a* by Brownian motion then  $\widetilde{Z}_y^{(a)} \equiv L_{T_a}^{a-y}, y \ge 0$ , satisfies the following:

$$\widetilde{Z}_{y} = 2 \int_{0}^{y} \sqrt{\widetilde{Z}_{z}} d\beta_{z} + 2(y \wedge a) \qquad (5)$$

2. if  $T = \tau_{\ell}$  is the first time  $(L_t^0, t \ge 0)$  the Brownian local time at level 0 reaches  $\ell$ , then  $(L_{\tau_{\ell}}^{y}, y \geq$ 0) and  $(L_{\tau_{\ell}}^{-y}, y \ge 0)$  are two independent BESQ processes, distributed as  $Q_{\ell}^{0}$ .

## An Implicit Representation in Terms of **Geometric Brownian Motions**

Lamperti [3] showed a one-to-one correspondence between Lévy processes  $(\xi_t, t \ge 0)$  and semistable Markov processes ( $\Sigma_u, u \ge 0$ ) via the (implicit) formula:

$$\exp(\xi_t) = \sum \int_0^t \mathrm{d}s \exp(\xi_s) \quad , \quad t \ge 0 \qquad (6)$$

In the particular case where  $\xi_t = 2(B_t + vt), t \ge$  $0$ , formula  $(6)$  becomes

$$\exp(2(B_t + \nu t)) = X^{(1,\delta)}_{\begin{subarray}{c}0\\ \end{subarray}} \text{ds} \exp(2(B_s + \nu s)) \tag{7}$$

where, in agreement with our notation,  $(X_u^{(1,\delta)}, u \geq$ 0) denotes a BESQ process starting from 1 with dimension  $\delta = 2(1 + \nu)$ . We note that in equation (7),  $\delta$  may be negative, that is,  $\nu < -1$ ; however, formula (7) reveals  $(X_u^{(1,\delta)})$  for  $u < T_0(X^{(1,\delta)})$  the first hitting time of 0 by  $(X^{(1,\delta)})$ . Nonetheless, the study of BESQ<sup> $\delta$ </sup>, for any  $\delta \in \mathbb{R}$ , has been developed in [1].

Absolute continuity relationships between the laws of different BESQ processes may be derived from equation (7), combined with the Cameron-Martin relationship between the laws of  $(B_t + vt, t \ge 0)$  and  $(B_t, t > 0).$ 

Precisely, one obtains thus, for  $\delta \geq 2$ :

$$Q_{x|\mathcal{Z}_{u}}^{\delta} = \left(\frac{Z_{u}}{x}\right)^{\frac{\nu}{2}} \exp\left(-\frac{\nu^{2}}{2} \int_{0}^{u} \frac{\mathrm{d}s}{Z_{s}}\right) \cdot Q_{x|\mathcal{Z}_{u}}^{2} \quad (8)$$

where  $\mathcal{Z}_u \equiv \sigma \{Z_s, s \leq u\}$ , and  $\nu = \frac{\delta}{2} - 1$ . The combination of equations (7) and (8) may be used to derive results about  $(B_t + vt, t \ge 0)$  from results about  $X^{x,\delta}$  (and *vice versa*). In particular, the law of

$$A_{T_{\lambda}}^{(\nu)} := \int_0^{T_{\lambda}} \mathrm{d}s \exp(2(B_s + \nu s)) \tag{9}$$

where  $T_{\lambda}$  denotes an independent exponential time, was derived in ([8], Paper  $\sharp$ 2) from this combination.

### Some Explicit Formulae for BESQ Functionals

Formula (3), when  $\mu$  is replaced by  $\lambda \mu$ , for any scalar  $\lambda \geq 0$ , yields the explicit Laplace transform

of  $I_{\mu}$ , provided the function  $\phi_{\lambda\mu}$  is known explicitly, which is the case for  $\mu(\mathrm{d}t) = at^{\alpha}1_{(t < A)}\mathrm{d}t + b\varepsilon_A(\mathrm{d}t)$ and many other examples.

Consequently, the semigroup of BESQ may be expressed explicitly in terms of Bessel functions, as well as the Laplace transforms of first hitting times (see, for example, [2]) and distributions of last passage times (see, for example, [4]). Chapter XI of [6] is entirely devoted to Bessel processes.

#### References

- [1] Goïng-Jaeschke, A. & Yor, M. (2003). A survey and some generalizations of Bessel processes, Bernoulli 9(2),  $313 - 350$
- [2] Kent, J. (1978). Some probabilistic properties of Bessel functions, *The Annals of Probability* **6**, 760–770.
- [3] Lamperti, J. (1972). Semi-stable Markov processes, Zeitschrift fur Wahrscheinlichkeitstheorie und verwandte Gebiete 22, 205-225.
- [4] Pitman, J. & Yor, M. (1981). Bessel processes and infinitely divisible laws, in Stochastic Integrals, D. Williams, ed., LNM 851, Springer, pp. 285-370.
- [5] Pitman, J. & Yor, M. (1982). A decomposition of Bessel Bridges, Zeitschrift fur Wahrscheinlichkeitstheorie und verwandte Gebiete 59, 425-457.
- [6] Revuz, D. & Yor, M. (1999). *Continuous Martingales and* Brownian Motion, 3rd Edition, Springer.
- Shiga, T. & Watanabe, S. (1973). Bessel diffusions as [7] a one-parameter family of diffusion processes, Zeitschrift fur Wahrscheinlichkeitstheorie und verwandte Gebiete 27,  $37 - 46$
- [8] Yor, M. (2001). Exponential Functionals of Brownian Motion and Related Processes, Springer-Finance.

#### **Related Articles**

Affine Models; Cox-Ingersoll-Ross (CIR) Model; Heston Model; Simulation of Square-root Processes.

MARC J. YOR
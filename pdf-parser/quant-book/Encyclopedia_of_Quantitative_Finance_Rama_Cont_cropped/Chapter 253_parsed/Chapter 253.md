# **Integral Equation Methods for Free** Boundaries

Free boundary problems (FBPs) are ubiquitous in modern mathematical finance. They arise as early exercise boundaries for American style options (arguably the first example in finance, introduced by McKean [15] in 1965), as default barriers in structural (value-of-firm) models of credit default [7], as the optimal strategies for refinancing mortgages [13, 21], exercising employee stock options [14] (see **Employee Stock Options**) and callable convertible bonds [20], and so on. There are many methods for treating the FBPs that arise as mathematical models of these finance problems, including variational inequalities [11], viscosity solutions [8], and the classical partial differential equations (PDE) approach [10, 16]. In this article, we focus on an integral equation (IE) approach that is particularly suited for the types of FBPs that arise in finance.

In the section Free Boundary Problems as Integral Equations, we sketch the method in the context of the American put option, perhaps the most widely known and best understood FBP in finance. After deriving an IE problem mathematically equivalent to the original Black, Scholes, and Merton (BSM) PDE FBP for the American put, we outline how the IE problem can be used to prove existence and uniqueness for the original problem and to derive analytical and numerical estimates for the location of the early exercise boundary [4, 5]. In the section Application of the IE Method to Other FBPs, we sketch how this IE approach can be carried over to other FBPs in finance [7, 21] with the goal of indicating that this is a unified approach to a diverse collection of problems.

## **Free Boundary Problems as Integral** Equations

In this section, we outline the IE approach in the context of an American put option on a geometric Brownian motion underlier (*see* **American Options**). The BSM risk-neutral pricing theory says that the

option value,  $p(S, t)$ , satisfies the FBP

$$p_{t} + \frac{\sigma^{2} S^{2}}{2} p_{SS} + r S p_{S} - r p = 0,$$
  
$$S_{f}(t) < S < \infty, 0 < t < T \qquad (1)$$

$$p(S, t) = K - S \text{ on } S = S_f(t), \quad 0 < t < T \quad (2)$$

$$p_S(S, t) = -1$$
 on  $S = S_f(t), \quad 0 < t < T$  (3)

$$p(S, t) \to 0 \text{ as } S \to \infty$$
 (4)

$$p(S, T) = \max(K - S, 0), \quad K = S_f(T) < S < \infty$$
(5)

where  $r, \sigma, K, T$  have the conventional meanings and  $S_f(t)$  is the location of the early exercise, free boundary to be determined along with  $p(S, t)$ . Letting  $\tau = \frac{\sigma^2}{2}(T - t)$  (the scaled time to expiry) and  $x = ln(S/K)$ , then the scaled option price

$$P_{\text{new}} = \begin{cases} 1 - S/K & S < S_f(t) \\ p/K & S > S_f(t) \end{cases} \tag{6}$$

satisfies the transformed problem (dropping the subscript) in  $-\infty < x < \infty$ ,  $0 < \tau < \sigma^2 T/2$ 

$$p_{\tau} - \{p_{xx} + (k-1)p_x - kp\} = kH(x_f(\tau) - x)$$
(7)
$$p(x, 0) = \max(1 - e^x, 0)$$
(8)

where  $k = 2r/\sigma^2$ , *H* is the Heaviside function.  $x_f(\tau) = \ln(S_f/S)$ , and the coefficient k appears on the right-hand side (rhs) of equation (7) because the intrinsic payoff,  $p_0(x) = 1 - e^x$  satisfies

$$p_{0\tau} - \{p_{0xx} + (k-1)p_{0x} - kp_0\} = k \qquad (9)$$

The solution to problems  $(7)$  and  $(8)$  can be written in terms of the free boundary,  $x_f(\tau)$ , using the fundamental solution of the pdo on the left-hand side (lhs) of equation  $(7)$ ,

$$\Gamma(x,\,\tau) = \frac{e^{-k\tau}}{2\sqrt{\pi\tau}} e^{-(x+(k-1)\tau)^2/4\tau} \tag{10}$$

in the form

$$p(x,\tau) = \int_{-\infty}^{0} (1 - e^{y}) \Gamma(x - y, \tau) \, \mathrm{d}y$$
$$+ k \int_{0}^{\tau} \int_{-\infty}^{x_{f}(u)} \Gamma(x - y, \tau - u) \, \mathrm{d}y \, \mathrm{d}u \tag{11}$$

The first term is the price of the European style put while the second is the premium for the American optionality. Integral representations of this sort have been discussed in the finance literature for some time (see, e.g., [3]).

For the representation  $(11)$  to be useful, one must first determine the unknown location of the boundary,  $x_f(\tau)$ , which appears in the second integral on the  $\text{rhs of equation (11)}$ . The usual approach in the free boundary literature proceeds by starting with equation (11) and evaluating the lhs at  $x = x_f(\tau)$  using one or other of the conditions

$$p(x_f(\tau), \tau) = 1 - e^{x_f(\tau)}$$
 (12)

$$p_x(x_f(\tau), \tau) = -e^{x_f(\tau)} \tag{13}$$

which are the transformed versions of the smooth pasting conditions  $(2)$  and  $(3)$ . Instead, we use a trick here, based on financial considerations, to notice that  $p_{\tau}(x_f(\tau), \tau) = 0$ . Thus, from equation (11),

$$p_{\tau}(x,\tau) = \Gamma(x,\tau) + k \int_0^{\tau} \Gamma(x - x_f(u), \tau - u)$$
$$\times \dot{x}_f(u) \, \mathrm{d}u \tag{14}$$

which, upon evaluation on the early exercise boundary, provides the following nonlinear IE for  $x_f(\tau)$ :

$$\Gamma(x_f(\tau), \tau) = -k \int_0^{\tau} \Gamma(x_f(\tau) - x_f(u), \tau - u)$$
$$\times \dot{x}_f(u) \, du \tag{15}$$

This equation has proved, in our experience, to be much more effective in the mathematical analysis of this problem than the versions obtainable from equations  $(12)$  and  $(13)$ . In addition, we have obtained still other versions, also derivable from the representation  $(11)$ , whose particular forms have proven useful in various situations  $[5]$ :

$$\int_0^{\tau} \{\Gamma_x(x_f(\tau), u) + k\Gamma(x_f(\tau), u)\} du$$
  
=  $k \int_0^{\tau} \Gamma(x_f(\tau) - x_f(u), \tau - u) du$  (16)

$$\Gamma(x_f(\tau), \tau) = \frac{k}{2} + k \int_0^\tau \{ \Gamma(x_f(\tau) - x_f(u), \tau - u) - \Gamma_x(x_f(\tau) - x_f(u), \tau - u) \} du$$
(17)

$$\dot{x}_f(\tau) = \frac{-2\Gamma_x(x_f(\tau), \tau)}{k}$$
$$+ 2\int_0^t \Gamma_x(x_f(\tau) - x_f(u), \tau - u)$$
$$\times \dot{x}_f(u) \, \mathrm{d}u \tag{18}$$

Using the representation (11) to compute  $p_x$ ,  $p_{xx}$ and  $p_{x\tau}$ , the above IEs for  $x_f(\tau)$  follow (after some rearrangement of terms) by evaluation on the boundary.

The underlying theoretical rationale for using this IE approach to treat the original FBPs  $(1)$ – $(5)$  or  $(7)$ , (8), is summarized in the following result.

**Theorem 1** (Theorem 3.2 and Sections 4, 5, 6 of [5]). Suppose that  $x_f \in C^1((0,\infty)) \cap C^0([0,\infty))$  and  $\alpha(\tau) = x_f(\tau)^2/4\tau$ . Assume that as  $\tau \searrow 0$ ,  $\alpha(\tau) =$  $[-1+0(1)]\ln\sqrt{\tau}$ , and  $\tau\dot{\alpha}(\tau)=0(1)$ . Then  $x_f$ , together with  $p$  defined by equation (11), solves the (equivalent) FBPs  $(1-5)$  or  $(7, 8)$ , if and only if  $x_f$  satisfies any of the equivalent integro-differential equations (IODEs)  $(15-18)$ . Finally, equation (18) has a unique solution with the properties listed above.

The equivalence of the IODEs  $(15-18)$  is established in Lemma 3.1 of [6] and the required estimates on  $\alpha$  are rigorously derived from equation  $(15)$ . The proof that equation  $(18)$  has a solution with the required properties is a highly technical analysis [6] based on Schauder's fixed point theorem. Peskir [18] used the IE obtained from equation  $(11)$  with equation (12), along with local time-space arguments, to prove uniqueness in the class of continuous boundaries.

Analytical and numerical estimates for the location of the early exercise boundary, that might be useful to practitioners, can also be obtained from the IODEs  $(15-18)$ . For example, if we make the change of variables  $\eta = (x_f(\tau) - x_f(u))/2\sqrt{\tau - u}$  in equation (15), the rhs for small  $\tau$  (near expiry) behaves like

$$-k\int_0^{\alpha(\tau)} \left[1 - \frac{x_f(\tau) - x_f(u)}{2\dot{x}_f(u)(\tau - u)}\right]^{-1} \frac{e^{-\eta^2}}{\sqrt{\pi}} d\eta \quad (19)$$

which tends to k because  $\alpha(\tau) \rightarrow -\infty$  (from the above theorem) and  $[\cdots]^{-1} \rightarrow 1/2$  uniformly in u because of the convexity of  $x_f$  (proved separately in [6] using the method of Friedman and Jensen [12]); an independent proof of convexity was obtained by Ekstrom [9]. Thus, from equation (15) with small  $\tau$ ,

$$\Gamma(x_f(\tau), \tau) = \frac{e^{-k\tau}}{2\sqrt{\pi\tau}} e^{-(x_f(\tau) + (k-1)\tau)^2/4\tau} \cong$$
$$= \frac{e^{-x_f(\tau)^2/4\tau}}{2\sqrt{\pi}} \cong k \tag{20}$$

which leads to

$$x_f(\tau) \approx 2\sqrt{\tau} \sqrt{-\ln(4\pi k^2 \tau)^{1/2}} \text{ as } \tau \to 0 \quad (21)$$

This implies the first rigorous estimate for the near-expiry behavior of the early exercise boundary obtained by Barles et al. [2]

$$S_f(t) \simeq k \bigg[ 1 - \sigma \sqrt{-(T-t)\ln(T-t)} \bigg], t \sim T \tag{22}$$

In addition, it provides the first estimate for  $\alpha(\tau)$ in the above existence theorem. Specifically,

$$\alpha(\tau) = x_f(\tau)^2 4\tau \approx -\ln(4\pi k^2 \tau)^{1/2} = -\frac{\xi}{2} \quad (23)$$

where  $\xi = \ln(4\pi k^2 \tau)$ .

More precise analytical and numerical estimates can be obtained for  $\alpha(\tau)$  (equivalently  $x_f(\tau)$  and  $S_{f}(t)$ , valid for intermediate and large times as well  $[5]$ , by using Mathematica to iterate equation (23) through equation (15). Perhaps even more importantly, a very fast, accurate numerical scheme can be obtained from the IODE (18), which can be written in the equivalent form

$$\dot{x}_f(\tau) = \frac{x_f(\tau)}{2k\tau} \Gamma(x_f(\tau), \tau) [1 + m(\tau)] \qquad (24)$$

where

$$m(\tau) = k \int_0^{\tau} \left[ \frac{2\tau}{x_f(\tau)} \left( \frac{x_f(\tau) - x_f(u)}{\tau - u} \right) - 1 \right] \times \frac{\Gamma(x_f(\tau) - x_f(u), \tau - u)}{\Gamma(x_f(\tau), \tau)} \dot{x}_f(u) \, \mathrm{d}u \tag{25}$$

that is to be solved with initial data  $x_f(0) = 0$ . Solving this iteratively with  $m(\tau) = m_0(\tau) \equiv 0$  initially provides the fastest and most accurate approximation among all our estimates [5].

The above IE formalism can be carried over to the American put with a continuous dividend rate,  $d$ . The analog of equations  $(24)$  and  $(25)$  was used to show numerically that for a small interval of dividend rates,  $r < d < (1 + \epsilon)r$ , the early exercise boundary loses convexity near maturity (see Figure 1). This agrees qualitatively with the folklore on this problem generally attributed to M. Broadie.

#### Application of the IE Method to Other $FBPs$

In the previous section, we described how to formulate the American put FBP in terms of IODEs for the early exercise boundary and how to use this

![](_page_2_Figure_20.jpeg)

Figure 1 Graph of the early exercise boundary,  $S_f(t)$ , near expiry for a dividend paying stock with  $r = 0.05, d = 0.51, K = 100, T = 0.1$ . A numerical scheme based on the analog of equation (26) was used with  $x_f(0) = ln(r/d)$  and the first time step computed from the well- known  $\sqrt{T-t}$  behavior near expiry

formulation to establish theoretical results (existence, uniqueness) as well as analytical and numerical estimates for the original problem. In this section, we indicate the wider applicability of the method by briefly discussing several other problems arising from finance.

#### Jump-diffusion Processes

These IE methods can be extended to jump-diffusion models (see Lévy Processes; Poisson Process). Specifically, letting  $x = ln(S/K)$ , we now assume that the transformed asset price follows the process

$$X(t) = (\mu - \sigma^2/2)t + \sigma W(t) + N(t) \qquad (26)$$

where  $N(t)$  is a Poisson process with rate  $\lambda t$  and has jumps of size  $\pm \epsilon$  with equal probability. In this case, the transformed PDEs analogous to equations (7) and  $(8)$  are

$$\mathcal{L}p = \mathcal{L}(1 - e^x)H(x_f(\tau) - x) \tag{27}$$

$$p(x, 0) = \max(1 - e^x, 0) \tag{28}$$

where  $\mathcal{L}$  is the nonlocal pdo

$$\mathcal{L}p = p_{\tau} - \{p_{xx} + (k-1)p_x - kp\}$$
$$+ \lambda \{p(x+\epsilon,\tau) - 2p + p(x-\epsilon,\tau)\}$$
(29)

This problem is amenable by the methods outlined above because the fundamental solution can be explicitly calculated. Specifically,

$$\Gamma(x,\tau) = \sum_{u=0}^{\infty} \frac{(\lambda\tau)^n}{2^n n!} e^{-\lambda\tau}$$
$$\times \left(\sum_{j=0}^n \binom{n}{j} \Gamma_{\text{BS}}((2j-u)\epsilon + x,\tau)\right)$$
(30)

where  $\Gamma_{\text{BS}}$  is the BSM fundamental solution in equation (10). Proceeding as in the section Free Boundary Problems as Integral Equations, one obtains the ana- $\log$  to equation (15) in the form

$$\Gamma(x_f(\tau), \tau) = -\int_0^\tau [k + \lambda \{2 - e^{\epsilon} - e^{-\epsilon}\} e^{x_f(u)} \times \Gamma(x_f(\tau) - x_f(u), \tau - u) \cdot \times \dot{x}_f(u)] du + \lambda \int_0^\epsilon (1 - e^{y - \epsilon}) \times \Gamma(x_f(\tau) - y, \tau) dy \tag{31}$$

from which we obtain the near-expiry estimate for  $\alpha(\tau) = x_f(\tau)^2/4\tau$  (see analog (23) with no jumps)

$$\sqrt{\tau}e^{\alpha} \approx 1/\sqrt{4\pi\tilde{k}^2} \text{ as } \tau \to 0$$
 (32)

where  $\tilde{k} = k + \lambda (1 - e^{-\epsilon})$ , agreeing with the result of Pham [19] using other methods.

#### Interest Rate Processes

These IE methods can also be used to study American style contracts on other underliers. For example, a mortgage prepayment option provides the holder with the right to prepay the outstanding balance of a fixedrate mortgage

$$M(t) = \frac{m}{c}(1 - e^{-c(T-t)})$$
 (33)

where  $T$  is the maturity,  $c$  is the (continuous) fixed mortgage rate, and  $m$  is the (continuous) rate of payment of the mortgage (i.e.,  $m$  d $t$  is the premium paid in any time interval  $dt$ ). Clearly, the value of the prepayment option depends on  $M(t)$  and also on the rate of return,  $r(t)$ , that the mortgage holder (borrower) can obtain by investing  $M(t)$ . If this shortterm rate is assumed to follow the Vasicek model (see **Term Structure Models)** 

$$dr = (\eta - \theta r) dt + \sigma dW \tag{34}$$

in a risk-neutral world, then the value of the prepayment option,  $V(r, t)$ , satisfies [13, 21]

$$V_t + \frac{\sigma^2}{2} V_{rr} + (\eta - \theta r) V_r + m - rV$$
  
= 0,  $R(t) < r < \infty, 0 < t < T$  (35)

$$V(r, t) = M(t), r = R(t), 0 < t < T \t(36)$$

$$V_r(r,t) = 0, \ r = R(t), \ 0 < t < T \tag{37}$$

$$V(r, t) \to 0$$
, as  $r \to \infty$ ,  $0 < t < T$  (38)

$$V(r,T) = 0, \ c = R(0) < r < \infty \tag{39}$$

The optimal strategy for the mortgage holder is to exercise the option to pay off the mortgage the first time that the rate r falls below  $R(t)$  at time t. Existence and uniqueness for this FBP was proved using variational methods [13].

Because the fundamental solution for the Vasicek "bond pricing equation"—equation (35)—can be explicitly calculated, its form suggests a sequence of changes of dependent and independent variables (not relevant for this summary) that reduces the FBPs  $(35-39)$  to the following analog of equations (7) and (8) in  $-\infty < x < \infty, s > 1$ 

$$u_s - \frac{1}{4}u_{xx} = f(x,s)H(x - x_f(s)) \qquad (40)$$

$$u(x,1) = 0 \tag{41}$$

where  $f(x, s)$  is a specific function resulting from the transformations and  $x_f(s)$  is the transformed free boundary with  $u(x_f(s), s) = 0 = u_x(x_f(s), s)$ .

In this form, the procedure outlined in the previous section can be followed to obtain

$$u(x,s) = \int_1^s \left[ \int_{x_f(u)}^\infty \Gamma(x-y,s-u) f(y,u) \, \mathrm{d}y \right] \mathrm{d}u \tag{42}$$

where  $\Gamma$  is the fundamental solution of the heat operator  $\partial_s - \frac{1}{4} \partial_{xx}$ , and the free boundary can be obtained by solving the IE

$$\int_{1}^{s} \left[ \int_{x_{f}(u)}^{\infty} \Gamma(x_{f}(s) - y, s - u) f(y, u) \, \mathrm{d}y \right] \mathrm{d}u = 0 \tag{43}$$

In [21], Dejun Xie used the integral representations  $(42)$  and  $(43)$  to obtain near-expiry estimates for the critical rate as well as to obtain a numerical scheme to determine  $x_f(s)$  globally. Specifically, if  $Q(x, s)$  denotes the integral on the rhs of equation (42), he showed that the Newton-Raphson iterative scheme to solve equation (43),  $Q(x_f(s), s) = 0$ , can be written as

$$x_f(s)^{\text{new}} = x_f(s)^{\text{old}} + \frac{Q(x_f(s)^{\text{old}}, s)}{2f(x_f(s)^{\text{old}}, s)}$$
(44)

where, in the denominator,  $Q_x(x_f(s), s)$  is approximated by

$$\frac{1}{2} \left\{ Q_x(x_f(s) + s) + Q_x(x_f(s) - s) \right\}$$
$$= \frac{1}{2} u_{xx}(x_f(s), s) = -2f(x_f(s), s) \quad (45)$$

#### Default Barrier Models

As a final example, we outline how these methods can be used to obtain an IE formulation for the inverse first-crossing problem in a value-of-firm (structural) model for credit default (see Structural Default Risk **Models**). Suppose the default index of a company,  $X(t)$ , is a Brownian motion with drift following

$$dX(t) = a dt + \sigma dW(t), \quad X(0) = x_0 \quad (46)$$

(equivalently, the log of such an index that originally satisfied a geometric Brownian motion). Default of the firm is said to occur the first time  $\tau$  that  $X(t)$ falls below a preassigned value,  $b(t)$ . The survival pdf,  $u(x, t)$  defined by

$$u(x, t) dx = Pr[x < x(t) < x + dx|t < \tau]$$

is known to satisfy the following problem for the forward Kolmogorov equation:

$$u_t = \frac{\sigma^2}{2} u_{xx} - au_x, b(t) < x < \infty, 0 < t < T$$
(47)

$$u(x,t) = 0, \ x = b(t), 0 < t < T \tag{48}$$

$$u(x, t) \to 0 \ x \to \infty, 0 < t < T \tag{49}$$

$$u(x,0) = \delta(x - x_0), b(0) < x < \infty \tag{50}$$

and the resulting survival probability is given, in terms of the solution *u(x, t)*, by

$$Pr(\tau > t) = P(t) = \int_{b(t)}^{\infty} u(x, t) \, \mathrm{d}x \tag{51}$$

Motivated by the work of Avellaneda and Zhu [1], Lan Cheng, studied the inverse first-crossing problem [7]: given the survival probability *P (t)* for 0 *<t< T* , find the time-dependent absorbing boundary *b(t)* in equation (48), including *b(*0*)*, such that equations (47)– (51) are satisfied. The more usual extra Neumann boundary condition appearing in FBPs can be obtained by differentiating equation (51):

$$P'(t) = -u(b(t), t)b'(t) + \int_{b(t)}^{\infty} u_t(x, t) dx$$
  
=  $\frac{-\sigma^2}{2} u_x(b(t), t)$  (52)

using the PDE (47) and the boundary conditions. With −*P (t)* = *(*1 − *P (t))* = *Q (t)* = *q(t)* denoting the default pdf, the extra boundary condition becomes

$$u_x(x,t) = \frac{2}{\sigma^2}q(t), x = b(t), 0 < t < T \qquad (53)$$

Following the outline in the section Free Boundary Problems as Integral Equations, one can derive IEs for *b(t)* in the form

$$\Gamma(b(t),t) = \int_0^t \Gamma(b(t) - b(s), t - s)q(s) \, \mathrm{d}s$$

$$\frac{1}{2}q(t) = \Gamma_x(b(t), t)$$

$$-\int_0^t \Gamma_x(b(t) - b(s), t - s)q(s) \, \mathrm{d}s$$
(55)

where is the fundamental solution of the pdo in equation (47). A fast and accurate numerical scheme for solving

$$F(x, t) = \Gamma(x, t) - \int_0^t \Gamma(x - b(s), t - s)q(s) \, ds = 0$$
(56)

for *x* = *b(t)* (i.e., solving equation (54)) is the Newton—Raphson iteration

$$b(t)^{\text{new}} = b(t)^{\text{old}} - \frac{F(b(t)^{\text{old}}, t)}{q(t)/2} \qquad (57)$$

where, in computing *Fx* in the denominator, we have used

$$\frac{1}{2}q(t) = F_x(b(t), t) \simeq F_x(b(t)^{\text{old}}, t)$$
$$= \simeq \Gamma_x(b(t)^{\text{old}}, t) - \int_0^t \Gamma_x(b(t)^{\text{old}} - b(s)^{\text{old}}, t - s)q(s) \, \text{d}s \tag{58}$$

Finally, we mention that an IEs formulation of the first passage problem for Brownian motion was given by Peskir [17] but the inverse problem described here was not treated. In [7], the proof of existence and uniqueness used viscosity solution methods. A proof using integral equations is still an open question for this problem as well as the two others listed in this section.

### **Acknowledgments**

The author acknowledges support by NSF award DMS 0707953.

### **References**

- [1] Avellaneda, M. & Zhu, J. (2001). Modeling the distanceto-default of a firm, *Risk* **14**, 125–129.
- [2] Barles, G., Burdeau, J., Romano, M. & Samsoen, N. (1995). Critical stock price near expiration, *Mathematical Finance* **5**, 77–95.
- [3] Carr, P., Jarrow, J. & Myneni, R. (1992). Alternative characterizations of American put option, *Mathematical Finance* **2**, 87–105.
- [4] Chen, X. & Chadam, J. (2003). Analytical and numerical approximations for the early exercise boundary for American put options, *Continuous, Discrete and Impulsive Systems, Series A: Mathematical Analysis* **10**, 649–660.
- [5] Chen, X. & Chadam, J. (2006). A mathematical analysis for the optimal exercise boundary of American put options, *SIAM Journal of Mathematical Analysis* **38**, 1613–1641.
- [6] Chen, X., Chadam, J., Jiang, L. & Zheng, W. (2008). Convexity of the exercise boundary of the American put

option on a zero dividend asset, *Mathematical Finance* **18**, 185–197.

- [7] Cheng, L., Chen, X., Chadam, J. & Saunders, D. (2006). Analysis of an inverse first passage problem from risk management, *SIAM Journal of Mathematical Analysis* **38**, 845–873.
- [8] Crandall, M., Iskii, H. & Lions, P.L. (1992). User's guide to viscosity solutions of second order partial differential equations, *Bulletin of AMS* **27**, 1–67.
- [9] Ekstrom, E. (2004). Convexity of the optimal stopping time for the American put option, *Journal of Mathematical Analysis and Applications* **299**, 147–156.
- [10] Friedman, A. (1964). *Partial Differential Equations of Parabolic Type*, Prentice Hall.
- [11] Friedman, A. (1983). *Variational Principles and Free Boundary Problems Lems*, John Wiley & Sons.
- [12] Friedman, A. & Jensen, R. (1978). Convexity of the free boundary in the Stefan problem and in the dam problem, *Archive for Rational Mechanics and Analysis* **67**, 1–24.
- [13] Jiang, L., Bian, B. & Yi, F. (2005). A parabolic variational inequality arising from the valuation of fixed rate mortgages, *European Journal of Applied Mathematics* **16**, 361–383.
- [14] Leung, T. & Sircar, R. (2009). Accounting for risk aversion, vesting, job termination risk and multiple exercises in valuation of employee stock options, *Mathematical Finance* **19**, 99–128.
- [15] McKean, H.P. Jr. (1965). A free boundary problem for the heat equation arising from a problem of mathematical economics, *Industrial Management Review* **6**, 32–39.

- [16] Ockendon, J., Howison, S., Lacey, A. & Movchan, A. (2003). *Applied Partial Differential Equations*, Oxford University Press.
- [17] Peskir, G. (2002). On integral equations arising in the first-passage problem for Brownian motion, *The Journal of Integral Equations and Applications* **14**, 397–423.
- [18] Peskir, G. (2005). On the American option problem, *Mathematical Finance* **15**, 169–181.
- [19] Pham, H. (1997). Optimal stopping, free boundary and American option in a jump-diffusion model, *Applied Mathematics Optimization* **35**, 145–164.
- [20] Sirbu, M. & Shreve, S. (2006). A two-person game for pricing convertible bonds, *SIAM Journal of Control and Optimization* **45**, 1508–1639.
- [21] Xie, D., Chen, X. & Chadam, J. (2007). Optimal prepayment of mortgages, *European Journal of Applied Mathematics* **18**, 363–388.

### **Related Articles**

**American Options**; **Finite Difference Methods for Early Exercise Options**; **Structural Default Risk Models**; **Term Structure Models**.

JOHN CHADAM
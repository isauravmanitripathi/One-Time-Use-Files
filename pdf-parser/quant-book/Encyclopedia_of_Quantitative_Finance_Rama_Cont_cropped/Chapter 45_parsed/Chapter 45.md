## **Backward Stochastic Differential Equations**

Backward stochastic differential equations (BSDEs) occur in situations where the terminal (as opposed to the initial) condition of stochastic differential equations is a given random variable. Linear BSDEs were first introduced by Bismut (1976) as the adjoint equation associated with the stochastic version of the Pontryagin maximum principle in control theory. The general case of a nonlinear BSDE was first introduced by Peng and Pardoux [23] to give a Feynman-Kac representation of nonlinear parabolic partial differential equations (PDEs). The solution of a BSDE consists of a pair of adapted processes  $(Y, Z)$ satisfying

$$-dY_t = f(t, Y_t, Z_t)dt - Z'_t dW_t, \quad Y_T = \xi \quad (1)$$

where f is called the *driver* and  $\xi$  the *terminal condition.* This type of equation appears naturally in hedging problems. For example, in a complete market (*see* **Complete Markets**), the price process  $(Y_t)_{0 \le t \le T}$ of a European contingent claim  $\xi$  with maturity T corresponds to the solution of a BSDE with a linear driver f and a terminal condition equal to  $\xi$ .

Reflected BSDEs were introduced by El Karoui *et al.* [6]. In the case of a reflected BSDE, the solution  $Y$  is constrained to be greater than a given process called the *obstacle*. A nondecreasing process  $K$  is introduced in the equation in order to push (upward) the solution so that the constraint is satisfied, and this push is minimal, that is,  $Y$  satisfies the following equation:

$$-dY_t = f(t, Y_t, Z_t)dt + dK_t - Z'_t dW_t, \quad Y_T = \xi$$
(2)

with  $(Y_t - S_t) dK_t = 0$ . One can show that the price of an American option (with eventually some nonlinear constraints) is the solution of a reflected BSDE, where the obstacle is given by the payoff process.

## **Definition and Properties**

We adopt the following notation:  $\mathbb{F} = \{\mathcal{F}_t, 0 \le t\}$  $\leq T$  is the natural filtration of an *n*-dimensional

Brownian motion W:  $L^2$  is the set of random variables  $\xi$  that are  $\mathcal{F}_T$ -measurable and squareintegrable;  $\textit{IH}^2$  is the set of predictable processes  $\phi$  such that  $E \int_0^T |\phi_t|^2 dt < \infty$ . In the following, the sign ' denotes transposition.

Let us consider the following BSDE (with dimension 1 to simplify the presentation):

$$-dY_t = f(t, Y_t, Z_t)dt - Z'_t dW_t, \quad Y_T = \xi \quad (3)$$

where  $\xi \in L^2$  and f is a *driver*, that is, it satisfies the following assumptions:  $f: \Omega \times [0, T] \times \mathbb{R} \times$  $\mathbb{R}^n \to \mathbb{R}$  est  $\mathcal{P} \otimes \mathcal{B} \otimes \mathcal{B}^n$ -measurable,  $f(., 0, 0) \in$  $\mathbb{H}^2$  and f is uniformly Lipschitz with respect to v, z with constant  $C > 0$ . Such a pair  $(\xi, f)$  is called a pair of *standard parameters*. If the driver  $f$  does not depend on y and z, the solution Y of equation (3) is then given as

$$Y_{t} = E\left[\xi + \int_{t}^{T} f(s) \mathrm{d}s / \mathcal{F}_{t}\right] \tag{4}$$

and the martingale representation theorem for Brownian motion ([16] Theorem  $4.15$ ) gives the existence of a unique process  $Z \in \mathbb{H}^2$  such that

$$E\left[\xi + \int_0^T f(s) \mathrm{d}s / \mathcal{F}_t\right] = Y_0 + \int_0^t Z'_s \mathrm{d}W_s \quad (5)$$

In 1990, Peng and Pardoux [23] stated the following theorem.

**Theorem 1** If  $\xi \in L^2$  and if f is a driver, then there exists a unique pair of solutions  $(Y, Z) \in \mathbb{H}^2 \times \mathbb{H}^2$ of equation (3).

In [7], El Karoui *et al.* have given a short proof of this theorem based on *a priori estimations* of the solutions. More precisely, the proposition is given as follows:

**Proposition 1** (A Priori Estimations). Let  $f^1$ ,  $\xi^1$ ,  $f^2$ ,  $\xi^2$  be standard parameters. Let  $(Y^1, Z^1)$  be the solution associated with  $f^1$ ,  $\xi^1$  and  $(Y^2, Z^2)$  be the solution associated with  $f^2$ ,  $\xi^2$ . Let C be the Lipschitz constant of  $f^1$ . Substitute  $\delta Y_t = Y_t^1 - Y_t^2$ ,  $\delta Z_t =$  $Z_t^1 - Z_t^2$ , and  $\delta_2 f_t = f^1(t, Y_t^2, Z_t^2) - f^2(t, Y_t^2, Z_t^2)$ .<br>For  $(\lambda, \mu, \beta)$  such that  $\lambda^2 > C$  and  $\beta$  sufficiently large, that is,  $\beta > C(2 + \lambda^2) + \mu^2$ , the following estimations hold:

$$\left|\left|\delta Y\right|\right|_{\beta}^{2} \leq T\left[e^{\beta T}E(\left|\delta Y_{T}\right|^{2}) + \frac{1}{\mu^{2}}\left|\left|\delta_{2}f\right|\right|_{\beta}^{2}\right] \tag{6}$$

$$||\delta Z||_{\beta}^{2} \leq \frac{\lambda^{2}}{\lambda^{2} - C} \left[ e^{\beta T} E(|\delta Y_{T}|^{2}) + \frac{1}{\mu^{2}} ||\delta_{2} f||_{\beta}^{2} \right]$$
(7)

where  $||\delta Y||_{\beta}^2 = E \int_0^T e^{\beta t} |\delta Y_t|^2 dt$ .

From these estimations, uniqueness and existence of a solution follow by using the fixed point theorem applied to the function  $\Psi : I\!H^2_{\beta} \otimes I\!H^2_{\beta} \to I\!H^2_{\beta} \otimes$  $\mathbb{H}^2_{\beta}$ ;  $(y, z) \mapsto (Y, Z)$ , where  $(Y, Z)$  is the solution associated with the driver  $f(t, y_t, z_t)$  and  $I\!H^2_{\beta}$  denotes the space  $\mathbb{H}^2$  endowed with norm  $||\cdot||_{\beta}$ . Indeed, by using the previous estimations, one can show that for sufficiently large  $\beta$ , the mapping  $\Psi$  is strictly contracting, which gives the existence of a unique fixed point, which is the solution of the BSDE.

In addition, from "*a priori* estimations" (Proposition 1), some *continuity* and *differentiability* of solutions of BSDEs (with respect to some parameter) can be derived  $(7]$  section 2).

Furthermore, estimations (1) are also very useful to derive some results concerning approximation or discretization of BSDEs [14].

Recall the dependence of the solutions of BSDEs with respect to terminal time  $T$  and terminal condition  $\xi$  by the notation  $(Y_t(T,\xi), Z_t(T,\xi))$ . We have the following flow property.

**Proposition 2** (Flow Property). Let  $(Y(T, \xi), Z)$  $(T,\xi)$ ) be the solution of a BSDE associated with the terminal time  $T > 0$  and standard parameters  $(\xi, f)$ . *For any stopping time*  $S \leq T$ *,* 

$$Y_t(T,\xi) = Y_t(S,Y_S(T,\xi)),$$
  

$$Z_t(T,\xi) = Z_t(S,Y_S(T,\xi)),$$
  

$$t \in [0, S], \quad dP \otimes dt\text{-almost surely} \quad (8)$$

**Proof** By conventional notation, we define the solution of the BSDE with terminal condition  $(T, \xi)$  for  $t \geq T$  by  $(Y_t = \xi, Z_t = 0)$ . Thus, if  $T' \geq T$ , then  $((Y_t, Z_t); t \leq T')$  is the unique solution of the BSDE with terminal time  $T'$ , coefficient  $f(t, y, z)\mathbf{1}_{\{t \le T\}}$ , and terminal condition  $\xi$ .

Let  $S \leq T$  be a stopping time, and denote by  $Y_t(S,\xi')$  the solution of the BSDE with terminal time T, coefficient  $f(t, y, z) \mathbf{1}_{\{t < S\}}$ , and terminal condition  $\xi^{'}$  ( $\mathcal{F}_{S}$ -measurable). Both the processes  $(Y_t(S, Y_S), Z_t(S, Y_S); t \in [0, T])$  and  $(Y_{t \wedge S}(T, \xi),$  $Z(T, \xi) \mathbf{1}_{\{t \le S\}}; t \in [0, T]$ ) are solutions of the BSDE with terminal time T, coefficient  $f(t, y, z) \mathbf{1}_{\{t \le S\}}$ , and terminal condition  $Y_{S}$ . By uniqueness, these processes are the same  $dP \otimes dt$ -a.s.

The simplest case is that of a *linear* BSDE. Let  $(\beta, \gamma)$  be a bounded  $(\mathbb{R}, \mathbb{R}^n)$ -valued predictable process and let  $\varphi \in \mathbb{H}^2(\mathbb{R}), \xi \in \mathbb{L}^2(\mathbb{R})$ . We consider the following BSDE:

$$- dY_t = (\varphi_t + Y_t \beta_t + Z'_t \gamma_t) dt - Z'_t dW_t,$$
  
$$Y_T = \xi \qquad (9)$$

By applying Itô's formula to  $\Gamma_t Y_t$ , it can easily be shown that the process  $\Gamma_t Y_t + \int_0^t \Gamma_s \varphi_s ds$  is a local martingale and even a uniformly integrable martingale, which gives the following proposition.

**Proposition 3** The solution  $(Y, Z)$  of the linear  $BSDE(9)$  satisfies

$$\Gamma_t Y_t = E\left[\xi \Gamma_T + \int_t^T \Gamma_s \varphi_s \mathrm{d}s \, |\mathcal{F}_t\right] \qquad (10)$$

where  $\Gamma$  is the adjoint process (corresponding to a change of numéraire or a deflator in finance) defined by  $d\Gamma_t = \Gamma_t[\beta_t dt + \gamma_t^* dW_t], \ \Gamma_0 = 1.$ 

**Remark 1** First, it can be noted that if  $\xi$  and  $\varphi$  are positive, then the process  $Y$  is positive. Second, if in addition  $Y_0 = 0 \, a.s.,$  then for any  $t, Y_t = 0 \, a.s.$  and  $\varphi_t = 0 \, \mathrm{d}t \otimes \mathrm{d}P \text{-}a.s.$ 

From the first point in this remark, one can derive the classical *comparison* theorem, which is a key property of BSDEs.

**Theorem 2** (Comparison Theorem). If  $f^1, \xi^1$  and  $f^2, \xi^2$  are standard parameters and if  $(Y^1, Z^1)$ (respectively  $(Y^2, Z^2)$ ) is the solution associated with  $(f^1, \xi^1)$  (respectively  $(f^2, \xi^2)$ ) satisfying

- 1.  $\xi^1 \ge \xi^2$  *P*-a.s.
- 2.  $\delta_2 f_t = f^1(t, Y_t^2, Z_t^2) f^2(t, Y_t^2, Z_t^2) \ge 0 \text{ dt } \times$  $dP$ -a.s.
- 3.  $f^1(t, Y_t^2, Z_t^2) \in \mathbb{H}^2$ .

Then, we have  $Y^1 > Y^2P$ -a.s.

In addition, the comparison theorem is strict, that is, on the event  $\{Y_t^1 = Y_t^2\}$ , we have  $\xi_1 = \xi_2$ a.s.,  $f^1(t, Y_t^2, Z_t^2) = f^2(t, Y_t^2, Z_t^2) ds \times dP$ -a.s. and  $Y_s^1 = Y_s^2 \ a.s., \ t \le s \le T.$ 

**Idea of the proof.** We denote by  $\delta Y$  the spread between those two solutions:  $\delta Y_t = Y_t^2 - Y_t^1$  and  $\delta Z_t = Z_t^2 - Z_t^1$ . The problem is to show that under the above assumptions,  $\delta Y_t \geq 0$ .

Now, the pair  $(\delta Y, \delta Z)$  is the solution of the following LBSDE:

$$-d\delta Y_t = \delta_y f^2(t)\delta Y_t + \delta_z f^2(t)\delta Z_t + \varphi_t dt$$
$$-\delta Z'_t dW_t,$$
$$\delta Y_T = \xi^2 - \xi^1 \tag{11}$$

where  $\delta_y f^2(t) = \frac{f^2(t, Y_t^2, Z_t^2) - f^2(t, Y_t^1, Z_t^2)}{Y_t^2 - Y_t^1}$  if

 $Y_t^2 - Y_t^1$  is not equal to 0, and 0 otherwise (and the same for  $\delta_{z} f^{2}(t)$ ). Now, since the driver  $f^{2}$  is supposed to be uniformly Lipschitz with respect to  $(y, z)$ , it follows that  $\delta f_y^2(t)$  and  $\delta f_y^2(t)$  are bounded. In addition,  $\varphi_t$  and  $\delta Y_T$  are nonnegative. It follows from the first point of Remark (1) that the solution  $\delta Y_t$  of the LBSDE (11) is nonnegative. In addition, the second point of Remark (1) gives the *strict* comparison theorem.

From this theorem, we then state a general principle for *minima* of BSDEs [7]: if a driver  $f$  can be written as an infimum of a family of drivers  $f^{\alpha}$  and if a random variable  $\xi$  can be written as an infimum of random variables  $\xi^{\alpha}$ , then the solution of the BSDE associated with  $f$  and  $\xi$  can be written as the infimum of the solutions of the BSDEs associated with  $f^{\alpha}, \xi^{\alpha}$ .

More precisely, we have the following proposition.

**Proposition 4** (Minima of BSDEs). Let  $(f, f^{\alpha}; \alpha \in$ A) be a family of drivers and let  $(\xi, \xi^{\alpha}; \alpha \in A)$  be a family of terminal conditions. Let  $(Y, Z)$  be the solution of the BSDE associated with  $(f, \xi)$  and let  $(Y^{\alpha}, Z^{\alpha})$  be the solution of the BSDE associated with  $(f^{\alpha}, \xi^{\alpha})$ . Suppose that there exists a parameter  $\overline{\alpha}$  such that

$$f(t, Y_t, Z_t) = \operatorname{ess} \inf_{\alpha} f^{\alpha}(t, Y_t, Z_t)$$
  
=  $f^{\overline{\alpha}}(t, Y_t, Z_t), \text{d}t \otimes \text{d}P\text{-a.s.}$  (12)

$$\xi = \operatorname{ess} \inf_{\alpha} \xi^{\alpha} = \xi^{\overline{\alpha}}, \quad \text{$P$-a.s.} \tag{13}$$

Then,

$$Y_t = \operatorname{ess} \inf_{\alpha} Y_t^{\alpha} = Y_t^{\overline{\alpha}}, \quad 0 \le t \le T, \, P\text{-a.s.} \quad (14)$$

**Proof** For each  $\alpha$ , since  $f(t, Y_t, Z_t) < f^{\alpha}(t, Y_t, Z_t)$  $dt \otimes dP$ -a.s. and  $\xi \leq \xi^{\alpha}$ , the comparison theorem gives that  $Y_t \leq Y_t^{\alpha} \ 0 \leq t \leq T$ , *P*-a.s. It follows that

$$Y_t \le \operatorname{ess} \inf_{\alpha} Y_t^{\alpha}, \quad 0 \le t \le T, \ \ P\text{-a.s.} \tag{15}$$

Now, by assumption, it is clear that  $Y_t = Y_t^{\overline{\alpha}}, 0 \le$  $t \leq T$ , *P*-a.s., which gives that the inequality in (15) is an equality, which ends the proof.

Note also that from the strict comparison theorem, one can derive an *optimality criterium* [7]:

**Proposition 5** A parameter  $\overline{\alpha}$  is 0-optimal (i.e.,  $\min_{\alpha} Y_0^{\alpha} = Y_0^{\overline{\alpha}}$ ) if and only if

$$f(s, Y_s, Z_s) = f^{\overline{\alpha}}(s, Y_s, Z_s) dP \otimes ds \text{-a.s.}$$
  
$$\xi = \xi^{\overline{\alpha}} \quad P \text{-a.s.}$$
 (16)

The flow property (Proposition 2) of the value function corresponds to the *dynamic programming principle* in stochastic control.

Indeed, using the same notation as in Proposition 2, for any stopping time  $S < T$ ,

$$Y_t(T,\xi) = \operatorname{ess} \inf_{\alpha} Y_t^{\alpha}(S,Y_S(T,\xi)),$$
  
 
$$0 \le t \le S, \ \ P\text{-a.s.}$$
(17)

From the principle on minima of BSDEs (Proposition 4), one can easily obtain some links between BSDEs and stochastic control (see, e.g. [10] Section 3 for a financial presentation or  $[26]$  for a more classical presentation in stochastic control).

Note, in particular, that if this principle on minima of BSDEs is formulated a bit differently, it can be seen as a verification theorem for some stochastic control problem written in terms of BSDEs . More precisely, let  $(f^{\alpha}; \alpha \in \mathcal{A})$  be a family of drivers and let  $(\xi^{\alpha}; \alpha \in \mathcal{A})$  be a family of terminal conditions. Let  $(Y^{\alpha}, Z^{\alpha})$  be the solution of the BSDE associated with  $(f^{\alpha}, \xi^{\alpha})$ . The value function is defined at time  $t$  as

$$\overline{Y}_t = \operatorname{ess} \inf_{\alpha} Y_t^{\alpha}, \ \ P \text{-a.s.} \tag{18}$$

If there exist standard parameters  $f$  and  $\xi$  and a parameter  $\overline{\alpha}$  such that equation (12) holds, then the value function coincides with the solution of the BSDE associated with  $(f, \xi)$ . In other words,  $\overline{Y}_t = Y_t, \ 0 \le t \le T, \ P \text{-a.s., where } (Y, Z) \text{ denotes}$ the solution of the BSDE associated with  $(f, \xi)$ . It can be noted that this *verification theorem* generalizes the well-known Hamilton–Jacobi–Bellman–verification theorem, which holds in a Markovian framework.

Indeed, recall that in the *Markovian case*, that is, the case where the driver and the terminal condition are functions of a state process, Peng and Pardoux  $(1992)$  have given an interpretation of the solution of a BSDE in terms of a PDE [24]. More precisely, the state process  $X^{t,x}$  is a diffusion of the following type:

$$dX_s = b(s, X_s)ds + \sigma(s, X_s)dW_s, \quad X_t = x \quad (19)$$

Then, let us consider  $(Y^{t,x}, Z^{t,x})$  solution of the following BSDE:

$$-dY_s = f(s, X_s^{t,x}, Y_s, Z_s)ds - Z'_s dW_s,$$
  
$$Y_T = g(X_T^{t,x})$$
 (20)

where  $b$ ,  $\sigma$ ,  $f$ , and  $g$  are deterministic functions. In this case, one can show that under quite weak conditions, the solution  $(Y^{t,x}_s, Z^{t,x}_s)$  depends only on time s and on the state process  $X^{t,x}_s$  (see [7] Section 4). In addition, if  $f$  and  $g$  are uniformly continuous with respect to  $x$  and if  $u$  denotes the function such that  $Y_t^{t,x} = u(t,x)$ , one can show (see [24] or [10] p. 226 for a shorter proof) that  $u$  is a viscosity solution of the following PDE:

$$\partial_t u + \mathcal{L}u(t, x) + f(t, x, u(t, x), \partial_x u \sigma(t, x)) = 0,$$
  
$$u(T, x) = g(x)$$
  
(21)

where  $\mathcal{L}$  denotes the infinitesimal generator of X (see Forward-Backward Stochastic Differential **Equations (SDEs); Markov Processes).** There are some complementary results concerning the case of a non-Brownian filtration (see [1] or [7] Section 5). In addition, some properties of *differentiability* in Malliavin's sense of the solution of a BSDE can be given [7, 24]. In particular, under some smoothness assumptions on  $f$ , the process  $Z_t$  corresponds to the *Malliavin* derivative of  $Y_t$ , that is,

$$D_t Y_t = Z_t, \quad \text{d}P \otimes \text{d}t \text{-a.s.} \tag{22}$$

Many tentatives have been made to relax the Lipschitz assumption on the driver  $f$ ; for instance, Lepeltier and San Martín [19] and have proved the existence of a solution for BSDEs with a driver  $f$ , which is only *continuous with linear growth* by an approximation method. Kobylanski [17] studied the case of *quadratic* BSDEs [20]. To give some intuition on quadratic BSDEs, let us consider the following simple example:

$$-dY_t = \frac{Z_t^2}{2} dt - Z_t dW_t,$$
  
$$Y_T = \xi$$
 (23)

Let us make the exponential change of variable  $y_t = e^{Y_t}$ . By applying Itô's formula, we easily derive

$$\begin{aligned} \mathrm{d} y_t &= \mathrm{e}^{Y_t} Z_t \mathrm{d} W_t, \\ y_T &= \mathrm{e}^{\xi} \end{aligned} \tag{24}$$

and hence, if  $\xi$  is supposed to be bounded and Z  $\in H^2$ , we have  $y_t = E[e^{\xi}/\mathcal{F}_t]$ . Thus, for quadratic BSDEs, it seems quite natural to suppose that the terminal condition is bounded. More precisely, the following existence result holds [17].

**Proposition 6** (Quadratic BSDEs). If the terminal condition  $\xi$  is bounded and if the driver f is linear growth in  $y$  and quadratic in  $z$ , that is,

$$|f(t, y, z)| \le C(1 + |y| + |z|^2) \tag{25}$$

then there exists an adapted pair of processes  $(Y, Z)$ , which is the solution of the quadratic BSDE associated with f and  $\xi$  such that the process Y is bounded and  $Z \in H^2$ .

The idea is to make an exponential change of variable  $y_t = e^{2CY_t}$  and to show the existence of a solution by an approximation method. More precisely, it is possible to show that there exists a nonincreasing sequence of Lipschitz drivers  $F^p$ , which converges to  $F$  (where  $F$  is the driver of the BSDE satisfied by  $y_t$ ). Then, one can show that the (nonincreasing) sequence  $y^p$  of solutions of classical BSDEs associated with  $F^p$  converges to a solution y of the BSDE associated with the driver  $F$  and terminal condition  $e^{2C\xi}$ , which gives the desired result.

## **BSDE** for a European Option

Consider a market model with a nonrisky asset, where price per unit  $P_0(t)$  at time t satisfies

$$dP_0(t) = P_0(t)r(t)dt$$
 (26)

and *n* risky assets, the price of the *i*th stock  $P_i(t)$  is modeled by the linear stochastic differential equation

$$dP_i(t) = P_i(t) \left[ b_i(t)dt + \sum_{j=1}^n \sigma_{i,j}(t) dW_t^j \right] \quad (27)$$

driven by a standard  $n$ -dimensional Wiener process  $W = (W^1, \ldots, W^n)'$ , defined on a filtered probability space  $(\Omega, I\!F, P)$ . We assume the filtration  $I\!F$ generated by the Brownian  $W$  is complete. The probability  $P$  corresponds to the objective probability measure. The coefficients r,  $b_i$ ,  $\sigma_{i,j}$  are *IF*-predictable processes. We denote the vector  $\vec{b} := (b^1, \dots, b^n)'$  by b and the volatility matrix  $\sigma := (\sigma_{i,j}, 1 \leq i \leq n, 1 \leq$  $j \leq n$ ) by  $\sigma$ . We will assume that the matrix  $\sigma_t$  has full rank for any  $t \in [0, T]$ . Let  $\theta_t = (\theta_t^1, \dots, \theta_t^d)'$  be the classical risk-premium vector defined as

$$\theta_t = \sigma^{-1}(b_t - r_t \mathbf{1}) \ P \text{-a.s.} \tag{28}$$

The coefficients  $\sigma$ , b,  $\theta$ , and r are supposed to be bounded.

Let us consider a small investor, who can invest in the  $n+1$  basic securities. We denote by  $(X_t)$  the wealth process. At each time  $t$ , he/she chooses the amount  $\pi_i(t)$  invested in the *i*th stock.

More precisely, a portfolio process is an adapted process  $\pi = (\pi_1, \ldots, \pi_n)'$  with  $\int_0^T |\sigma'_t \pi_t|^2 dt < \infty$ ,  $P$ -a.s.

The strategy is supposed to be self-financing, that is, the wealth process satisfies the following dynamics:

$$dX_t^{x,\pi} = r_t X_t dt + \pi'_t \sigma_t (dW_t + \theta_t dt)$$
(29)

Generally, the initial wealth  $x = X_0$  is taken as a primitive, and for an initial endowment and portfolio process  $(x, \pi)$ , there exists a unique wealth process  $X$ , which is the solution of the linear equation (29) with initial condition  $X_0 = x$ . Therefore, there exists a one-to-one correspondence between pairs  $(x, \pi)$ and trading strategies  $(X, \pi)$ .

Let  $T$  be a strictly positive real, which will be the terminal time of our problem. Let  $\xi$  be a European contingent claim settled at time T, that is, an  $\mathcal{F}_T$ measurable square-integrable random variable (it can be thought of as a contract that pays the amount  $\xi$  at time  $T$ ). By a direct application of BSDE results, we derive that there exists a unique  $P$ -square-integrable strategy  $(X, \pi)$  such that

$$dX_t = r_t X_t dt + \pi'_t \sigma_t \theta_t dt + \pi'_t \sigma_t dW_t,$$
  
$$X_T = \xi \tag{30}$$

 $X_t$  is the price of claim  $\xi$  at time t and  $(X, \pi)$  is a hedging strategy for  $\xi$ .

In the case of constraints such as the case of a borrowing interest rate  $R_t$  greater than the bond rate r (see [10] p. 201 and 216 or [7]), the case of taxes [8], or the case of a large investor (whose strategy has an influence on prices, see [10] p. 216), the dynamics of the wealth-portfolio strategy is no longer linear. Generally, it can be written as follows:

$$-dX_t = b(t, X_t, \sigma'_t \pi_t) dt - \pi'_t \sigma_t dW_t \tag{31}$$

where  $b$  is a driver (the classical case corresponds to the case where  $b(t, x, z) = -r_t x - z'\theta_t$ .

Let  $\xi$  be a square-integrable European contingent claim. BSDE results give the existence and the uniqueness of a *P*-square-integrable strategy  $(X, \pi)$ such that

$$-dX_t = b(t, X_t, \sigma'_t \pi_t) dt - \pi'_t \sigma_t dW_t,$$
  
$$X_T = \xi \tag{32}$$

As in the classical case,  $X_t$  is the price of the claim  $\xi$  at time t and  $(X, \pi)$  is a hedging strategy of  $\xi$ . Also note that, under some smoothness assumptions on the driver b, by equality (22), the hedging portfolio process (multiplied by the volatility)  $\pi'_t \sigma_t$ corresponds to the Malliavin derivative  $D_t X_t$  of the price process, that is,

$$D_t X_t = \sigma'_t \pi_t, \ dP \otimes dt \text{-a.s.} \tag{33}$$

which generalizes (to the nonlinear case) the useful result stated by Karatzas and Ocone [21] in the linear case. Thus, we obtain a nonlinear *price system* (see  $[10]$  p. 209), that is, an application that, for each  $\xi \in L^2(\mathcal{F}_T)$  and  $T \geq 0$ , associates an adapted process  $(X_t^b(\xi,T))_{\{0\leq t\leq T\}}$ , where  $X_t^b(\xi,T)$  denotes the solution of the BSDE associated with the driver b, terminal condition  $\xi$ , and terminal time T.

By the comparison theorem, this price system is *nondecreasing* with respect to  $\xi$  and satisfies the *noarbitrage* property:

- **A1.** If  $\xi^1 \ge \xi^2$  and if  $X_t^b(\xi^1, T) = X_t^b(\xi^2, T)$  on an event  $A \in \mathcal{F}_t$ , then  $\xi^1 = \xi^2$  on A. By the flow property of BSDEs (Proposition 2), it is also *consistent*: more precisely, if S is a stopping time (smaller than  $T$ ), then for each time  $t$  smaller than  $S$ , the price associated with payoff  $\xi$  and maturity T coincides with the price associated with maturity  $S$  and payoff  $X_{\mathcal{S}}^b(\xi, T)$ , that is,
- **A2.**  $\forall t \leq S, X_t^b(\xi, T) = X_t^b(X_S^b(\xi, T), S).$ 
  - In addition, if  $b(t, 0, 0) \ge 0$ , then, by the comparison theorem, the price  $X^b$  is positive. At least, if b is sublinear with respect to  $(x, \pi)$ (which is generally the case), then, by the comparison theorem, the price system is *sublinear*. Also note that if  $b(t, 0, 0) = 0$ , then the price of a contingent claim  $\xi = 0$  is equal to 0, that is,  $X_t^b(0,T) = 0$  and moreover (see, e.g., [25]), the price system satisfies the  $zero-one$ *law* property, that is,
- **A3.**  $X_t(\mathbf{1}_A \xi, T) = \mathbf{1}_A X_t(\xi, T)$  a.s. for  $t \leq T, A \in$  $\mathcal{F}_t$ , and  $\xi \in L^2(\mathcal{F}_T)$ . Furthermore, if  $b$  does not depend on  $x$ , then the price system satisfies the *translation invariance property:*
- **A4.**  $X_t(\xi + \xi', T) = X_t(\xi, T) + \xi'$ , for any  $\xi \in$  $L^2(\mathcal{F}_T)$  and  $\xi' \in L^2(\mathcal{F}_t)$ . Intuitively, it can be interpreted as a market with interest rate  $r$  equal to zero.

In the case where the driver  $b$  is convex with respect to  $(x, \pi)$  (which is generally the case), we have a variational formulation of the price of a European contingent claim (see [7] or [10] Prop.  $3.8$ p. 215). Indeed, by classical properties of convex analysis,  $b$  can be written as the maximum of a family of affine functions. More precisely, we have

$$b(t,x,\pi) = \sup_{(\beta,\gamma)\in\mathcal{A}} \{b^{\beta,\gamma}(t,x,\pi)\}\tag{34}$$

where  $b^{\beta,\gamma}(t, x, \pi) = B(t, \beta_t, \gamma_t) - \beta_t x - \gamma_t' \pi$ , where  $B(t,.,.)$  is the polar function of b with respect to  $x, \pi$ , that is,

$$B(\omega, t, \beta, \gamma) = \inf_{(x,\pi) \in \mathbb{R} \times \mathbb{R}^{n}} [b(\omega, t, x, \pi) + \beta_{t}(\omega) x + \gamma_{t}^{'}(\omega) \pi]$$
(35)

 $\mathcal{A}$  is a bounded set of pairs of adapted processes  $(\beta, \gamma)$  such that  $E \int_0^T B(t, \beta_t, \gamma_t)^2 dt < +\infty$ . BSDEs' properties give the following variational formulation:

$$X_t^b = \text{ess} \sup_{(\beta,\gamma)\in\mathcal{A}} X_t^{\beta,\gamma} \tag{36}$$

where  $X^{\beta,\gamma}$  is the solution of the linear BSDE associated with the driver  $b^{\beta,\gamma}$  and terminal condition  $\xi$ . In other words,  $X^{\beta,\gamma}$  is the classical linear price of  $\xi$  in a fictitious market with interest rate  $\beta$  and riskpremium  $\gamma$ . The function B can be interpreted as a *cost* function or a *penalty* function (which is equal to  $0$  in quite a few examples).

An interesting question that follows is "Under what conditions does a nonlinear price system have a BSDE representation?" In 2002, Coquet *et al.* [3] gave the first answer to this question.

**Theorem 3** Let  $X(.)$  be a price system, that is, an application that, for each  $\xi \in L^2(\mathcal{F}_T)$  and  $T >$ 0, associates an adapted process  $(X_t(\xi,T))_{\{0\le t\le T\}}$ that is nondecreasing, which satisfies the no-arbitrage  $property (A1), time consistency (A2), zero-one law$  $(A3)$ , and translation invariance property  $(A4)$ .

Suppose that it satisfies the following assumption: *There exists some*  $\mu > 0$  *such that* 

 $X_0(\xi + \xi', T) - X_0(\xi, T) \le Y_0^{\mu}(\xi', T)$ , for any  $\xi$  $\in L^2(\mathcal{F}_T)$  and  $\xi'$  a positive random variable  $\in$  $L^{2}(\mathcal{F}_{T})$ , where  $Y_{t}^{\mu}(\xi',T)$  is solution of the following  $BSDE:$ 

$$-dY_t = \mu |Z_t| dt - Z_t dW_t, \quad Y_T = \xi' \quad (37)$$

Then the price system has a BSDE representation, that is, there exists a standard driver  $b(t, z)$  that does not depend on x such that  $b(t, 0) = 0$  and that is Lipschitz with respect to z with coefficient  $\mu$ , such that  $X(\xi, T)$  corresponds to the solution of the BSDE associated with the terminal time  $T$ , driver  $b$ , and terminal condition  $\xi$ , for any  $\xi \in L^2(\mathcal{F}_T)$ ,  $T \geq 0$ , that  $iS, X(\xi, T) = X^{b}(\xi, T).$ 

In this theorem, the existence of the coefficient  $\mu$ might be interpreted in terms of risk aversion.

Many nonlinear BSDEs also appear in the case of an *incomplete* market (see Complete Markets). For example, the superreplication price of a European contingent claim can be obtained as the limit of a nondecreasing sequence of penalized prices, which are solutions of nonlinear BSDEs [9, 10]. Another example is given by the pricing a European contingent claim via exponential utility maximization in an incomplete market. In this case, El Karoui and Rouge [11] have stated that the price of such an option is the solution of a *quadratic* BSDE. More precisely, let us consider a complete market (see Com**plete Markets**) [11] that contains  $n$  securities, whose (invertible) volatility matrix is denoted by  $\sigma_t$ . Suppose that only the first  $i$  securities are available for hedging and their volatility matrix is denoted by  $\sigma_t^1$ . The utility function is given by  $u(x) = -e^{-\gamma x}$ , where  $\nu$  (> 0) corresponds to the risk-aversion coefficient. Let  $\xi$  be a given contingent claim corresponding to an exercise time T; in other words,  $\xi$  is a bounded  $\mathcal{F}_T$ -measurable variable. Let  $(X_t(\xi, T))$  (also denoted by  $(X_t)$  be the forward price process defined *via* the exponential utility function as in [11]. By Theorem 5.1 in [11], there exists  $Z \in H^2(\mathbb{R}^n)$  such that the pair  $(X, Z)$  is solution of the quadratic BSDE:

$$-\mathrm{d}X_{t} = \left\{ -(\eta_{t} + \sigma_{t}^{-1}\nu_{t}^{0}) \cdot Z_{t} + \frac{\gamma}{2}|\Pi(Z_{t})|^{2} \right\}$$
$$\times \mathrm{d}t - Z_{t}\mathrm{d}W_{t}, \quad X_{T} = \xi \tag{38}$$

where  $\eta$  is the classical relative risk process,  $v^0$  is a given process [11], and  $\Pi(z)$  denotes the orthogonal projection of z onto the kernel of  $\sigma^1$ .

# **Dynamic Risk Measures**

In the same way as in the previous section, some dynamic measures of risk can be induced quite simply by BSDEs (note that time-consistent dynamic riskmeasures are otherwise very difficult to deal with).

More precisely, let  $b$  be a standard driver. We define a *dynamic risk-measure*  $\rho^b$  as follows: for each  $T \geq 0$  and  $\xi \in L^2(\mathcal{F}_T)$ , we set

$$\rho^{b}(\xi, T) = X^{b}(-\xi, T) \tag{39}$$

where  $(X_t^b(-\xi, T))$  denotes the solution of the BSDE associated with the terminal condition  $-\xi$ , terminal time T, and driver  $b(t, \omega, x, z)$  [25]. Also note that  $\rho^b(\xi,T) = -X^{\overline{b}}(\xi,T)$ , where  $\overline{b}(t,x,z) =$  $-b(t, -x, -z).$ 

Then, by the results of the previous section, the dynamic risk measure  $\rho^b$  is *nonincreasing* and satisfies the no-arbitrage property (A1). In addition, the risk measure  $\rho^b$  is also *consistent*.

If b is superadditive with respect to  $(x, z)$ , then the dynamic risk-measure  $\rho^b$  is *subadditive*, that is,

For any  $T > 0, \xi, \xi' \in L^2(\mathcal{F}_T), \rho_t^b(\xi + \xi', T) <$  $\rho^b_t(\xi,T) + \rho^b_t(\xi',T).$ 

If  $b(t, 0, 0) = 0$ , then  $\rho^b$  satisfies zero-one law (A3).

In addition, if  $b$  does not depend on  $x$ , then the measure of risk satisfies the translation invariance property (A4).

In addition, if  $b$  is positively homogeneous with respect to  $(x, z)$ , then the risk measure  $\rho^b$  is *positively homogeneous* with respect to  $\xi$ , that is,  $\rho^b(\lambda \xi, T) =$  $\lambda \rho^b(\xi, T)$ , for each real  $\lambda \ge 0$ ,  $T \ge 0$ , and  $\xi \in$  $L^2(\mathcal{F}_T)$ .

If  $b$  is convex (respectively, concave) with respect to  $(x, z)$ , then  $\rho^b$  is concave (respectively, convex) with respect to  $\xi$ . Furthermore, if b is concave (respectively, convex), we have a variational formulation of the risk measure  $\rho^b$  (similar to the one obtained for nonlinear price systems). Note that in the case where  $b$  does not depend on  $x$ , this dual formulation corresponds to a famous theorem for convex and translation-invariant risk measures [12] and the polar function  $B$  corresponds to the penalty function.

Clearly, Theorem 3 can be written in terms of risk measures. Thus, it gives the following interesting result.

**Proposition 7** Let  $\rho$  be a dynamic risk measure, that is, an application that, for each  $\xi \in L^2(\mathcal{F}_T)$ and  $T \ge 0$ , associates an adapted process  $(\rho_t(\xi, T))_{\{0 \le t \le T\}}$ . Suppose that  $\rho$  is nonincreasing and satisfies assumptions  $(A1)$ – $(A4)$  and that there exists some  $\mu > 0$  such that  $\rho_0(\xi + \xi', T)$  –  $\rho_0(\xi,T) \ge -Y_0^{\mu}(\xi',T)$ , for any  $\xi \in L^2(\mathcal{F}_T)$  and  $\xi'$  a positive random variable  $\in L^2(\mathcal{F}_T)$ , where  $Y_t^{\mu}(\xi',T)$ is solution of BSDE (37). Then,  $\rho$  can be represented by a backward equation, that is, there exists a standard driver  $b(t, z)$ , which is Lipschitz with respect to z with coefficient  $\mu$ , such that  $\rho = \rho^b$  a.s.

### **Relation with Recursive Utility**

Another example of BSDEs in finance is given by recursive utilities introduced by Duffie and Epstein [5]. Such a utility function associated with a consumption rate  $(c_t, 0 \le t \le T)$  corresponds to the solution of BSDE (3) with terminal condition  $\xi$ , which can be interpreted as a terminal reward (which can be a function of terminal wealth) and a driver  $f(t, c_t, y)$  depending on the consumption rate  $c_t$ . The case of a standard utility function corresponds to a linear driver f of the form  $f(t, c, y) = u(c) - \beta_t y$ , where  $u$  is a nondecreasing and concave deterministic function and  $\beta$  corresponds to the discounted rate.

Note that by BSDE results, we may consider a driver  $f$  that depends on the variability process  $Z_t$  [7]. The generalized recursive utility is then the solution of the BSDE associated with  $\xi$  and  $f(t, c_t, y, z)$ . The standard utility function can be generalized to the following model first introduced by Chen and Epstein [2]:

$$f(t, c, y, z) = u(c) - \beta_t y - K.|z| \tag{40}$$

where  $K = (K_1, \ldots, K_n)$  and  $|z| = (|z^1|, \ldots, |z^n|)$ . The constants  $K_i$  can be interpreted as risk-aversion coefficients (or ambiguity-aversion coefficients).

By the flow property of BSDEs, recursive utility is *consistent*. In addition, by the comparison theorem, if f is concave with respect to  $(c, y, z)$  (respectively, nondecreasing with respect to  $c$ ), then recursive utility is *concave* (respectively, nondecreasing) with respect to  $c$ .

In the case where the driver  $f$  is concave, we have a variational formulation of recursive utility (first stated in  $[7]$ ) similar to the one obtained for nonlinear convex price systems (see the previous section). Let  $F(t, c_t, \dots)$  be the polar function of f with respect to y, z and let  $\mathcal{A}(c)$  be the (bounded) set of pairs of adapted processes  $(\beta, \gamma)$  such that  $E\int_0^1 F(t,c_t,\beta_t,\gamma_t)^2 dt < +\infty.$  Properties on optimization of BSDEs lead us to derive the following variational formulation:

$$Y_t = \text{ess} \inf_{(\beta,\gamma)\in\mathcal{A}} Y_t^{\beta,\gamma} \tag{41}$$

where  $Y^{\beta,\gamma}$  is the solution of the linear BSDE associated with the driver  $f^{\beta,\gamma}(t,c,x,\pi) := F(t,c,\beta_t,\gamma_t)$  $+\beta_t y + \gamma'_t z$  and the terminal condition  $\xi$ . Note that  $Y^{\beta,\gamma}$  corresponds to a standard utility function evaluated under a discounted rate  $-\beta$  and under a probability  $Q^{\gamma}$  with density with respect to P given by  $Z^{\gamma}(T) = \exp\left(-\int_0^T \gamma'_s \mathrm{d}W_s - \frac{1}{2} \int_0^T |\gamma_s|^2 \mathrm{d}s\right).$  Indeed,

we have

$$Y_t^{\beta,\gamma} = E_{\mathcal{Q}^{\gamma}} \left[ \int_t^T e^{\int_t^s \beta_u du} F(s, c_s, \beta_s, \gamma_s) ds \right. \\ \left. + e^{\int_t^T \beta_u du} Y \middle| \mathcal{F}_t \right] \tag{42}$$

El Karoui et al. [8] considered the optimization problem of a recursive utility with nonlinear constraints on the wealth. By using BSDE techniques, the authors state a maximum principle that gives a necessary and sufficient condition of optimality. The variational formulation can also lead to transform the initial problem into a max-min problem, which can be written as a min-max problem under some assumptions.

## **Reflected BSDEs**

Reflected BSDEs have been introduced by El Karoui et al. [6]. For a reflected BSDE, the solution is constrained to be greater than a given process called the *obstacle*.

Let  $S^2$  be the set of predictable processes  $\phi$ such that  $E(\sup_{t} |\phi_{t}|^{2}) < +\infty$ . We are given a couple of standard parameters, that is, a standard *driver*  $f(t, y, z)$  and a process  $\{\xi_t, 0 \le t \le T\}$  called the *obstacle*, which is supposed to be continuous on [0, T[, adapted, belonging to  $S^2$  and satisfying  $\lim_{t\to T}\xi_t < \xi_T$ .

A solution of the reflected BSDE associated with f and  $\xi$  corresponds to a triplet  $(Y, Z, K) \in S^2 \times$  $I\!H^2 \times S^2$  such that

$$-dY_t = f(t, Y_t, Z_t)dt + dK_t - Z'_t dW_t,$$
  

$$Y_T = \xi_T$$
(43)

with  $Y_t \geq \xi_t$ ,  $0 \leq t \leq T$  and where K is nondecreasing, continuous, adapted process equal to 0 at time 0 such that  $\int_0^T (Y_s - \xi_s) d\hat{K}_s = 0$ . The process K can be interpreted as the minimal push, which allows the solution to stay above the obstacle.

We first give a characterization of the solution (first stated by El Karoui and Quenez [10]). For each  $t \in [0, T]$ , let us denote the set of stopping times by  $T_t \tau$  such that  $\tau \in [t, T]$  a.s.

For each  $\tau \in T_t$ , we denote by  $(X_s(\tau, \xi_\tau),$  $\pi_s(\tau, \xi_\tau), t \leq s \leq \tau$ ) the (unique) solution of the BSDE associated with the terminal time  $\tau$ , terminal condition  $\xi_{\tau}$ , and coefficient f. We easily derive the following property.

**Proposition 8** (Characterization). Suppose that  $(Y, Z, K)$  is solution of the reflected BSDE (43). Then, for each  $t \in [0, T]$ ,

$$Y_t = X_t(D_t, \xi_{D_t}) = \operatorname*{ess\,sup}_{\tau \in T_t} X_t(\tau, \xi_{\tau}) \tag{44}$$

where  $D_t = \inf\{u \ge t; Y_u = \xi_u\}$ .

**Proof** By using the fact that  $Y_{D_t} = \xi_{D_t}$  and since the process K is constant on  $[t, D_t]$ , we easily derive that  $(Y_s, t \le s \le D_t)$  is the solution of the BSDE associated with the terminal time  $D_t$ , terminal condition  $\xi_{D}$ , and coefficient f, that is,

$$Y_t = X_t(D_t, \xi_{D_t}) \tag{45}$$

It remains now to show that  $Y_t \geq X_t(\tau, \xi_{\tau})$ , for each  $\tau \in T_t$ .

Fix  $\tau \in T_t$ . On the interval  $[t, \tau]$ , the pair  $(Y_s, Z_s)$ satisfies

$$-dY_s = f(s, Y_s, Z_s)ds + dK_s - Z_sdW_s,$$
  
$$Y_\tau = Y_\tau$$
 (46)

In other words, the pair  $(Y_s, Z_s, t \le s \le D_t)$  is the solution of BSDE associated with the terminal time  $\tau$ , terminal condition  $Y_{\tau}$ , and coefficient

$$f(s, y, z) + dK_s$$

Since  $f(s, y, z) + dK_s \ge f(s, y, z)$  and since  $Y_{\tau} \geq \xi_{\tau}$ , the comparison theorem for BSDEs gives

$$Y_t \ge X_t(\tau, \xi_\tau) \tag{47}$$

and the proof is complete.

Proposition 8 gives the uniqueness of the solution:

**Corollary 1** (Uniqueness). *There exists a unique* solution of reflected BSDE(43).

In addition, from Proposition 8 and the comparison theorem for classical BSDEs, we quite naturally derive the following comparison theorem for RBS-DEs (see [6] or [18] for a shorter proof).

**Proposition 9** (Comparison). Let  $\xi^1$ ,  $\xi^2$  be two obstacle processes and let  $f^1$ ,  $f^2$  be two coefficients.

Let  $(Y^1, Z^1, K^1)$  (respectively,  $(Y^2, Z^2, K^2)$ ) be a solution of the reflected BSDE (43) for  $(\xi^1, f^1)$ (respectively, for  $(\xi^2, f^2)$  and assume that

 $\xi^1 \le \xi^2 \text{ a.s.}$ <br> $f^1(t, y, z) \le f^2(t, y, z), \qquad t \in [0, T], (y, z) \in$  $\mathbb{R} \times \mathbb{R}^d$ . Then,  $Y^1 \leq Y^2 \quad \forall t \in [0, T]$  a.s.

As in the case of classical BSDEs, some *a priori estimations* similar to equations  $(6)$  and  $(7)$  can be given [6]. From these estimations, we can derive the existence of a solution, that is, the following theorem.

**Theorem 4** There exists a unique solution  $(Y, Z, K)$ of RBSDE (43).

**Sketch of the proof.** The arguments are the same as in the classical case. The only problem is to show the existence of a solution in the case where the driver  $f$  does not depend on  $y, z$ . However, this problem is already solved by optimal stopping time theory. Indeed, recall that by Theorem  $(4)$ , we have *Y* that is a solution of the RBSDE associated with the driver  $f(t)$  and obstacle  $\xi$ ; then,

$$Y_{t} = \operatorname*{ess\,sup}_{\tau \in T_{t}} X(\tau, \xi_{\tau})$$
  
$$= \operatorname*{ess\,sup}_{\tau \in T_{t}} E\left[\int_{t}^{\tau} f(s) \, \mathrm{d}s + \xi_{\tau} \middle| \mathcal{F}_{t}\right] \quad (48)$$

Thus, to show the existence of a solution, a natural candidate is the process

$$\overline{Y}_t = \operatorname{ess} \sup_{\tau \in T_t} E\left[\int_t^{\tau} f(s) \, \mathrm{d}s + \xi_{\tau} \middle| \mathcal{F}_t\right] \tag{49}$$

Then, by using classical results of the Snell envelope theory, we derive that there exist a nondecreasing continuous process  $K$  and an adapted process  $Z$ such that  $(\overline{Y}, Z, K)$  is the solution of the RBSDE associated with  $f$  and  $\xi$ .

**Remark 2** The existence of a solution of the reflected BSDE can also be derived by an approximation method via penalization [6]. Indeed, one can show that the sequence of penalized processes  $(Y^n, n \in \mathbb{N})$ , defined as the solutions of classical BSDEs

$$-dY_t^n = f(t, Y_t^n, Z_t^n)dt$$
  
+
$$n(Y_t^n - S_t)^{-} dt - Z_t^n dW_t, \quad Y_T^n = \xi$$
  
(50)

is nondecreasing (by the comparison theorem) and that it converges a.s. to the solution  $Y$  of the reflected BSDE.

In the Markovian case [6], that is, in the case where the driver and the obstacle are functions of a state process, we can give an interpretation of the solution of the reflected BSDE in terms of an obstacle problem. More precisely, the framework is the same as in the case of a Markovian BSDE. The state process  $X^{t,x}$  follows the dynamics (19). Let  $(Y^{t,x}, Z^{t,x}, K^{t,x})$  be the solution of the reflected BSDE:

$$-dY_s = f(s, X_s^{t,x}, Y_s, Z_s)ds + dK_s - Z'_s dW_s,$$
  
$$Y_T = g(X_T^{t,x})$$
 (51)

with  $Y_s \ge \xi_s := h(s, X_s^{t,x}), t \le s \le T$ . Moreover, we assume that  $h(T, x) \leq g(x)$  for  $x \in \mathbb{R}^d$ . The functions  $f, h$  are deterministic and satisfy

$$h(t, x) \le K(1 + |x|^p), \quad t \in [0, T], \ x \in \mathbb{R}^d$$
(52)

In this case, if  $u$  denotes the function such that  $Y_t^{t,x} = u(t,x)$ , we have the following theorem.

**Theorem 5** Suppose that the coefficients  $f$ ,  $b$ ,  $\sigma$ , and h are jointly continuous with respect to t and  $x$ . Then, the function  $u(t, x)$  is a viscosity solution of the following obstacle problem:

$$\min\left((u-h)(t,x), -\partial_t u - \mathcal{L}u - f(t,x,u(t,x),\right)$$
  
$$\partial_x u \sigma(t,x) = 0, \quad u(T,x) = g(x) \tag{53}$$

**Idea of the proof.** A first proof [6] can be given by using the approximation of the solution  $Y$  of the RBSDE by the increasing sequence  $Y^n$  of penalized solutions of BSDEs (50). By the previous results on classical BSDEs in the Markovian case, we know that  $Y_t^{n,t,x} = u_n(t,x)$  where  $u_n$  is the unique viscosity

solution of a parabolic PDE. Thus, we have that  $u_n(t,x) \uparrow u(t,x)$  as  $n \to \infty$  and by using classical techniques of the theory of viscosity solutions, it is possible to show that  $u(t, x)$  is a viscosity solution of the obstacle problem  $(53)$ .

Another proof can be given by directly showing that  $u$  is a viscosity solution of the obstacle problem [18].

Under quite standard assumptions on the coefficients, there exists a unique viscosity solution (see **Monotone Schemes**) of the obstacle problem (53) [6]. Generalizations of the previous results have been done on reflected BSDEs. Cvitanic and Karatzas [4] have studied reflected BSDEs with two obstacles and their links with stochastic games. Hamadène et al. [15] have studied reflected BSDEs with two obstacles with continuous coefficients. Gegout-Petit and Pardoux [13] have studied reflected BSDEs in a convex domain, Ouknine [22] has studied reflected BSDEs with jumps, and finally Kobylanski et al. [18] have studied reflected quadratic RBSDEs.

# **Reflected BSDEs and Pricing of an** American Option under Constraints

In this section, we see how these results can be applied to the problem of evaluation of an American option (see, e.g., [10] Section 5.4). The framework is the one that is described in the previous section (a complete market with nonlinear constraints such as a large investor).

Recall that an American option consists, at time t, in the selection of a stopping time  $v \ge t$  and (once this exercise time is chosen) of a payoff  $\xi_{\nu}$ , where  $(\xi_t, 0 \le t \le T)$  is a continuous adapted process on [0,  $T$ [ with  $\lim_{t\to T} \xi_t \leq \xi_T$ .

Let  $\nu$  be a fixed stopping time. Then, from the results on classical BSDEs, there exists a unique pair of square-integrable adapted processes  $(X(v, \xi_v))$ ,  $\pi(\nu,\xi_{\nu})$ ) denoted also by  $(X^{\nu},\pi^{\nu})$ , satisfying

$$- dX_t^{\nu} = b(t, X_t^{\nu}, \pi_t^{\nu}) dt - (\pi_t^{\nu})' dW_t, \quad X_T^{\nu} = \xi$$
(54)

(To simplify the presentation,  $\sigma_t$  is assumed to be equal to the identity).  $X(\nu, \xi_{\nu})$  corresponds to the price of a European option of exercise time  $\nu$  and payoff  $\xi_{\nu}$ .

The price of the American option is then given by a right continuous left limited (RCLL) process  $Y$ , satisfying for each  $t$ ,

$$Y_t = \operatorname{ess} \sup_{\nu \in T_t} X_t(\nu, \xi_{\nu}), \quad \text{$P$-p.s.}$$
 (55)

By the previous results, the price  $(Y_t, 0 \le t \le T)$ corresponds to the solution of a reflected BSDE associated with the coefficient b and obstacle  $\xi$ . In other words, there exists a process  $\pi \in \mathbb{H}^2$  and K an increasing continuous process such that

$$-dY_t = b(t, Y_t, \pi_t)dt + dK_t - \pi'_t dW_t,$$
  
$$Y_T = \xi_T$$
 (56)

with  $Y_{\cdot} \geq \xi_{\cdot}$  and  $\int_{0}^{T} (Y_{t} - \xi_{t}) dK_{t} = 0$ . In addition, the stopping time  $D_{t} = \inf \{ s \geq t / Y_{s} = \xi_{s} \}$  is optimal, that is,

$$Y_{t} = \operatorname{ess} \sup_{\nu \in T_{t}} X(\nu, \xi_{\nu}) = X_{t}(D_{t}, \xi_{D_{t}})$$
(57)

Moreover, by the minimality property of the increasing process  $K$ , the process  $Y$  corresponds to the surreplication price of the option, that is, the smallest price that allows the surreplication of the payoff.

One can also easily state that the price system  $\xi \mapsto Y(\xi)$  is nondecreasing and sublinear if b is sublinear with respect to x,  $\pi$ . Note (see [10] p. 239) that the nonarbitrage property holds only in a weak sense: more precisely, let  $\xi$  and  $\xi'$  be two payoffs and let *Y* and *Y'* their associated prices. If  $\xi \ge \xi'$  and also  $Y_0 = Y'_0$ , then  $D_0 \leq D'_0$ , the payoffs are equal at time  $D'_0$ , and the prices are equal until  $D'_0$ .

In the previous section, we have seen how, in the case where the driver  $b$  is convex, one can obtain a variational formulation of the price of a European option. Similarly, one can show that the price of an American option is equal to the value function of a mixed control problem [10].

#### References

- Buckdahn, R. (1993). Backward Stochastic Differential [1] Equations Driven by a Martingale. Preprint.
- Chen, Z. & Epstein, L. (1998). Ambiguity, Risk and [2] Asset Returns in Continuous Time, working paper 1998, University of Rochester.
- [3] Coquet, F., Hu, Y., Mémin, J. & Peng, S. (2002). Filtration-consistent nonlinear expectations and related

g-expectations, Probability Theory and Related Fields 123, 1-27.

- [4] Cvitanić, J. & Karatzas, I. (1996). Backward stochastic differential equations with reflection and Dynkin games, Annals of Probability 4, 2024-2056.
- [5] Duffie, D. & Epstein, L. (1992). Stochastic differential utility, Econometrica 60, 353-394.
- [6] El Karoui, N., Kapoudjian, C., Pardoux, E., Peng, S. & Quenez, M.C. (1997). Reflected solutions of Backward SDE's and related obstacle problems for PDE's, The Annals of Probability 25(2), 702-737.
- El Karoui, N., Peng, S. & Quenez, M.C. (1997). [7] Backward stochastic differential equations in finance, Mathematical Finance  $7(1)$ , 1–71.
- El Karoui, N., Peng, S. & Quenez, M.C. (2001). A [8] dynamic maximum principle for the optimization of recursive utilities under constraints, Annals of Applied Probability 11(3), 664-693.
- [9] El Karoui, N. & Quenez, M.C. (1995). Dynamic programming and pricing of a contingent claim in an incomplete market, SIAM Journal on Control and optimization 33(1), 29-66.
- El Karoui, N. & Quenez, M.C. (1996). Non-linear  $[10]$ pricing theory and backward stochastic differential equations, in *Financial Mathematics*, Lectures Notes in Mathematics, Bressanone 1656, W.J. Runggaldieredssnm, ed., collection, Springer.
- [11] El Karoui, N. & Rouge, R. (2000). Contingent claim pricing via utility maximization, Mathematical Finance 10(2), 259-276.
- [12] Föllmer, H. & Shied, A. (2004). Stochastic Finance: An introduction in Discrete Time, Walter de Gruyter, Berlin.
- [13] Gegout-Petit, A. & Pardoux, E. (1996). Equations différentielles stochastiques rétrogrades réfléchies dans un convexe, Stochastics and Stochastic Reports 57,  $111 - 128.$
- [14] Gobet, E. & Labart, C. (2007). Error expansion for the discretization of Backward Stochastic Differential Equations, Stochastic Processes and their Applications 10(2), 259-276.
- [15] Hamadane, S., Lepeltier, J.P. & Matoussi, A. (1997). Double barrier reflected backward SDE's with continuous coefficient, in Backward Stochastic Differential Equations, Collection Pitman Research Notes in Mathematics Series 364, N. El Karoui & L. Mazliak, eds, Longman.
- [16] Karatzas, I. & Shreve, S. (1991). Brownian Motion and Stochastic Calculus, Springer Verlag.
- [17] Kobylanski, M. (2000). Backward stochastic differential equations and partial differential equations with quadratic growth, The Annals of Probability 28, 558-602.
- [18] Kobylanski, M., Lepeltier, J.P., Quenez, M.C. & Torres, S. (2002). Reflected BSDE with super-linear quadratic coefficient, Probability and Mathematical Statistics 22, Fasc.1, 51-83.
# **Finite Difference Methods for Early Exercise Options**

Analytical formulas for the price are not available for options with early exercise possibility. Numerical methods are needed for pricing them. A common way is to derive a partial differential equation (PDE) for the price of the corresponding European-type option (without early exercise possibility) and then modify the equation to allow early exercise. With this approach, most often the underlying partial differential operator is discretized using a finite difference method that we consider in the following. Finite difference methods can be seen as a special (but simpler) case of the finite element method (*see* **Finite Element Methods**).

An American-type option can be exercised any time during its life (*see* **American Options**) while a Bermudan-type option can be exercised at specified discrete times during its life. Most typical examples are American put and call options, but American and Bermudan exercise features can be added virtually to any option. In the following, we use an American put option under the Black–Scholes model as an example. Many of the considered methods can be used in a straightforward manner for other types of models and options, as discussed below.

# **PDE Formulation**

We denote the price of an option by *V* , which is a function of the value of the underlying asset *S* and time *t*. As it is more common to consider problems forward in time instead of backward, we use the inverted time variable *τ* = *T* − *t* instead of *t* in the following. The payoff function *g* gives the value of the option at the expiry date *T* , and also if it is exercised early. For example, for a put option, it is *g(S, τ )* = max{*K* − *S,* 0}, where *K* is the strike price.

The price *V* of a European option is given by a parabolic PDE

$$V_{\tau} + LV = 0 \tag{1}$$

with the initial condition *V* = *g* at *τ* = 0 together with boundary conditions, where *L* is linear partial differential operator. Under the Black–Scholes model [6], the operator *L* is defined by

$$LV = -\frac{1}{2}\sigma^2 S^2 V_{SS} - rSV_S + rV \qquad (2)$$

for *S >* 0, where *σ* is the volatility and *r* is the interest rate (*see* **Black–Scholes Formula**).

At the moment when the owner of an American or Bermudan-type option exercises it, she/he will receive a payment defined by the payoff function *g*. Hence the value *V* of such an option cannot be less than *g*, otherwise there would be an arbitrage opportunity. This leads to an early exercise constraint

$$V \ge g \tag{3}$$

which holds whenever the option can be exercised. As this inequality constrains the price *V* , it does not satisfy the PDE (1) everywhere; instead, it satisfies an inequality

$$V_{\tau} + LV \ge 0 \tag{4}$$

whenever equation (3) holds. Furthermore, either equation (3) or equation (4) has to hold with the equality at each point. Combining these conditions for an American-type option leads to a linear complementarity problem (LCP)

$$V_{\tau} + LV \ge 0, \quad V \ge g,$$
  
$$(V_{\tau} + LV)(V - g) = 0 \tag{5}$$

For a Bermudan option, the LCP (5) holds when the option can be exercised, and at other times, the PDE (1) holds. Another possibility is to formulate a variational inequality for the price *V* ; see [1, 18, 27], for example.

At time *τ* , the space can be divided into two parts: an early exercise (stopping) region *E(τ )* and a hold (continuation) region *H (τ )*. In the early exercise region, it is optimal to exercise the option, whereas in the hold region, it is optimal not to exercise it. For example, under the Black–Scholes model, these regions can be defined as

$$E(\tau) = \{S > 0 : V(S, \tau) = g(S)\},\$$
  
$$H(\tau) = \{S > 0 : V(S, \tau) > g(S)\}\$$
(6)

The boundary between these regions is called the *early exercise boundary Sf (τ )*. This is a time-dependent free boundary whose location is not known before solving the LCP (5) or some equivalent problem.

Alternatively, the price *V* can be computed as the solution of a free boundary problem in which the function *Sf (τ )* is also unknown. When the smooth pasting principle holds, the first derivative of *V* is continuous across the boundary *Sf (τ )*, and this gives an additional boundary condition on *Sf (τ )* that can be used to locate the free boundary. We remark that the smooth pasting principle does not hold, for example, when the model has *σ* = 0 like the variance gamma model (*see* **Variance-gamma Model**). Under the Black–Scholes model, we can formulate the problem for a put option:

$$V_{\tau} + LV = 0 \quad \text{for } S > S_f(\tau),$$
  
$$V(S_f(\tau), \tau) = g(S_f(\tau)) = S_f(\tau) - K,$$
  
$$V_S(S_f(\tau), \tau) = g_x(S_f(\tau)) = -1 \tag{7}$$

with the initial condition *V (S,* 0*)* = *g(S)*. One advantage of this formulation is that it can give a good approximation for the free boundary *Sf (τ )*. The domain *(Sf (τ ),*∞*)* in which the PDE needs to be satisfied is time varying. This makes the use of a finite difference method more complicated. An approach used in [32, 43] is to use a time-dependent change of variable in such a way that the computational domain is independent of time. The free boundary problem (7) is nonlinear, and devising a simpler and efficient solution procedure can be also a challenging task. We do not consider this formulation in the following.

A semilinear formulation for American put and call options under the Black–Scholes model was described in [4, 28]. For a put option, it leads to a semilinear PDE

$$V_{\tau} - LV = q \tag{8}$$

for *S >* 0, where

$$q(S,\tau) = \begin{cases} 0 & \text{if } V(S,\tau) > g(S) \\ rK & \text{if } V(S,\tau) \le g(S) \end{cases} \tag{9}$$

This PDE has a simple form, and it is posed in the fixed domain *(*0*,*∞*)*. The discontinuous *q* can make the numerical solution of this problem difficult. The PDE (8) with a regularized *q* was solved using an explicit finite difference method in [5].

# **Finite Difference Scheme**

Here, we consider the finite difference discretization of the LCP formulation (5) for an American option. Furthermore, we use the Black–Scholes operator *L* in equation (2) as an example. For discussion on finite difference discretizations, see [1, 15, 36, 37].

First, the domain *(*0*,*∞*)* is truncated into a sufficiently large interval *(*0*, S*max*)* and an artificial boundary condition is introduced at *S*max. For a put option, one possibility is *V (S*max*,τ)* = 0. Next, we define a grid *Si*, *i* = 0*,...,p*, such that 0 = *S*<sup>0</sup> *< S*<sup>1</sup> *<* ··· *< Sp* = *S*max. We allow the grid to be nonuniform, that is, the grid steps *Si*<sup>+</sup><sup>1</sup> = *Si*<sup>+</sup><sup>1</sup> − *Si* can vary. An alternative approach would be to use a coordinate transformation together with a uniform grid (*see* **Finite Difference Methods for Barrier Options**). In the finite difference discretization, we seek the value of *V* at the grid points *Si*. For better accuracy, it is desirable to have finer grid where *V* changes more rapidly such as near the strike price *K* for a put and call option, and near where the option price is desired. For example, we can construct a finer grid near the strike price *K* using a formula

$$S_i = \left(1 + \frac{\sinh(\mu(i/p - \xi))}{\sinh(\mu\xi)}\right)K\qquad(10)$$

where the constant *µ* is solved numerically from the equation *Sp* = *S*max. By choosing *ξ* , we control the amount of grid refinement.

The adopted space finite difference discretization leads to an approximation

$$(LV)(S_i) \approx -\alpha_i V_{i-1}$$
  
+ 
$$(\alpha_i + \beta_i + r)V_i - \beta_i V_{i+1} \quad (11)$$

at the internal grid points *Si*, *i* = 1*,...,p* − 1, where the grid point values of *V* are denoted by *Vi* = *V (Si)*. The coefficients *αi* and *βi* are defined by

$$\alpha_i = \frac{\sigma^2 S_i^2}{\Delta S_i (\Delta S_{i+1} + \Delta S_i)} - \frac{r S_i}{\Delta S_{i+1} + \Delta S_i},$$

$$\beta_i = \frac{\sigma^2 S_i^2}{\Delta S_{i+1} (\Delta S_{i+1} + \Delta S_i)} + \frac{r S_i}{\Delta S_{i+1} + \Delta S_i}$$
(12)

if  $\Delta S_i < \sigma^2 S_i/r$ , and otherwise by

$$\alpha_i = \frac{\sigma^2 S_i^2}{\Delta S_i (\Delta S_{i+1} + \Delta S_i)},$$
  
$$\beta_i = \frac{\sigma^2 S_i^2}{\Delta S_{i+1} (\Delta S_{i+1} + \Delta S_i)} + \frac{r S_i}{\Delta S_{i+1}} \qquad (13)$$

The reason to switch over to the latter formulas based on a one-sided difference for  $V_S$  when the above condition does not hold is to always have positive coefficients  $\alpha_i$  (and  $\beta_i$ ). The latter formulas are less accurate. Usually, it is necessary to use them only for a few grid points near  $S = 0$ , and this has minor (or no) influence on accuracy. We form a vector

$$\mathbf{V} = \begin{pmatrix} V_0 \\ V_1 \\ \vdots \\ V_p \end{pmatrix} \in \mathbb{R}^{p+1} \tag{14}$$

and a  $p+1 \times p+1$  tridiagonal matrix A with  $A_{i+1,i} = -\alpha_i, A_{i+1,i+1} = \alpha_{i-1} + \beta_{i-1} + r$ , and  $A_{i+1,i+2} = -\beta_{i-1}$  for  $i = 1, \ldots, p-1$ . The first and last row of  $A$  depends on the boundary conditions. For example, for a put option, we choose them to be zero rows. The matrix vector multiplication AV results in a vector that contains the approximations of LV at the grid points.

The space finite difference discretization leads to a semidiscrete LCP for the vector function  $V(\tau)$ given by

$$\mathbf{V}_{\tau} - \mathbf{A}\mathbf{V} \ge \mathbf{0}, \quad \mathbf{V} \ge \mathbf{g},$$
  
$$(\mathbf{V}_{\tau} - \mathbf{A}\mathbf{V})^T (\mathbf{V} - \mathbf{g}) = 0 \tag{15}$$

for  $\tau \in (0, T]$ . The initial value  $\mathbf{V}(0)$  and the vector  $\mathbf{g}$  contain the grid point values of the payoff function  $g$ . In the above and following, the inequalities hold componentwise.

The finite difference discretization of the LCP gives the value of  $V$  only at the grid points. Thus, any simple approximation of the early exercise region  $E(\tau)$  and the free boundary  $S_f(\tau)$  can have only the same accuracy as the grid step size.

The time discretization approximates the vector function **V** at times  $\tau^n$  such that  $0 = \tau^0 < \tau^1 < \cdots <$  $\tau^m = T$ . In the following, **V** at the approximation time  $\tau^n$  is denoted by  $\mathbf{V}^n = \mathbf{V}(\tau^n)$  and the time step between  $\tau^n$  and  $\tau^{n+1}$  is denoted by  $\Delta \tau^{n+1} =$  $\tau^{n+1} - \tau^n$ . The popular  $\theta$  time stepping scheme leads to a sequence of discrete LCPs

$$\mathbf{B}\mathbf{V}^{n+1} \ge \mathbf{b}^{n+1} \quad \mathbf{V}^{n+1} \ge \mathbf{g},$$
  
$$(\mathbf{B}\mathbf{V}^{n+1} - \mathbf{b}^{n+1})^T (\mathbf{V}^{n+1} - \mathbf{g}) = 0 \qquad (16)$$

for  $n = 0, 1, \ldots, m-1$  with the initial vector  $\mathbf{V}^0 =$  $g$ , where we have used the notations

$$\mathbf{B} = \mathbf{I} + \theta^{n+1} \Delta \tau^{n+1} \mathbf{A},$$
  
$$\mathbf{b}^{n+1} = \left[ \mathbf{I} + (1 - \theta^{n+1}) \Delta \tau^{n+1} \mathbf{A} \right] \mathbf{V}^n \qquad (17)$$

Different choices of  $\theta^{n+1}$  lead to the following commonly used method: the explicit Euler method  $\theta^{n+1}$  = 0, the Crank-Nicolson method  $\theta^{n+1} = 1/2$ , and the implicit Euler method  $\theta^{n+1} = 1$ . The Rannacher scheme is obtained by taking a few (say, four) first time steps with the implicit Euler method  $(\theta_n = 1, n = 1, 2, 3, 4)$  and then using the Crank-Nicolson method  $(\theta_n = 1/2, n = 5, \ldots, m)$  (see Crank-Nicolson Scheme).

Usually, the exercise boundary  $S_f(\tau)$  moves rapidly near the expiry and more slowly away from it. For example, for a put option under the Black-Scholes model the boundary behaves like

$$S_f(\tau) \approx K \left( 1 - \sigma \sqrt{-\tau \log \tau} \right)$$
 (18)

near the expiry  $\tau = 0$  [29]. Because of this, with uniform time steps, time discretization errors are likely to be much larger during the first time steps than during the later steps. This suggests that it is beneficial to use variable time steps. By gradually increasing the length of time steps, the errors can be made more equidistributed. This way, better accuracy can be obtained with a given number of time steps. Thus, we can reduce the computational effort to reach a desired accuracy.

One possible way to choose the time steps is so that the exercise boundary moves approximately the same amount at each time step. For the Rannacher scheme, by neglecting the logarithm term in the exercise boundary estimate given by equation (18), this approach leads to the approximation times

$$\tau^n = \left(\frac{n}{2m-4}\right)^2 T, \quad n = 1, 2, 3, 4,$$
$$\tau^n = \left(\frac{n-2}{m-2}\right)^2 T, \quad n = 5, \dots, m \qquad (19)$$

where the lengths of the four implicit Euler steps are further reduced by the factor  $\frac{1}{2}$ .

Another approach is to use adaptive time step selector that uses already computed time steps to predict a good length for the next time step. In [17], the time step  $\Delta \tau^{n+1}$  was suggested to be selected according to

$$\Delta \tau^{n+1} = C \left( \min_{i} \left[ \frac{\max\left\{ |V_i^{n-1}|, |V_i^n|, D \right\}}{|V_i^n - V_i^{n-1}|} \right] \right) \Delta \tau^n \tag{20}$$

where  $C$  is a target relative change over the time step and  $D$  is a scale of value of the option (for example, we could have  $D = 1$  if the value of the option is of the order of one monetary unit).

In the following sections, we describe common ways to solve the discrete LCPs  $(16)$ , or approximate them and then solve resulting problems.

## Solution Methods for LCPs

In the following, we consider the solution of the model LCP

$$\mathbf{BV} \ge \mathbf{b}, \quad \mathbf{V} \ge \mathbf{g},$$
$$(\mathbf{BV} - \mathbf{b})^T (\mathbf{V} - \mathbf{g}) = 0 \tag{21}$$

arising at each time step.

A commonly used iterative method for LCPs is the projected successive over relaxation (PSOR) method [11, 12, 22]. It reduces to the projected Gauss–Seidel method when the relaxation parameter denoted by  $\omega$ is 1. The basic idea of the projected Gauss-Seidel method is to solve components  $V_i$  successively, using the *i*th row of the system  $\mathbf{BV} = \mathbf{b}$  and then project  $V_i$  to be  $g_i$  if it is below it. The PSOR method over corrects each component by the factor  $\omega$  before the projection. The following pseudocode performs one iteration with the PSOR method for the LCP  $(21)$ . The vector  $\mathbf{V}$  contains the initial guess for the solution, which is usually the value from the previous time step or the vector  $\mathbf{V}$  returned by the previous iteration.

Algorithm PSOR(**B**, **V**, **b**, **g**)  
For 
$$i = 1, p + 1$$
  
 $r_i = b_i - \sum_j B_{i,j} V_j$   
 $V_i = \max \{V_i + \omega r_i / B_{i,i}, g_i\}$   
End For

The PSOR method is guaranteed to converge when the matrix  $\mathbf{B}$  is strictly diagonal dominant with positive diagonal entries  $(\sum_{j \neq i} |B_{i,j}| < B_{i,i}$  for all *i*) and the relaxation parameter  $\omega$  has value in (0, 1]. For more precise and general convergence results, we refer to  $[11, 22]$ . The convergence rate reduces as the number of grid points grows. On the other hand, smaller time steps make the matrix  $\mathbf{B}$  more diagonally dominant and convergence improves. Overall, the convergence slows down somewhat when both space and time steps are reduced at the same rate. The relaxation parameter  $\omega$  has a big influence on the convergence. Usually, on coarse grids, the optimal value of  $\omega$  is closer to 1 and on finer grids, it approaches 2. There is no formula for the optimal value; however, it is possible to form a reasonable estimate for it. Even then, quite often,  $\omega$  is chosen by hand tuning it for a given grid.

A grid-independent convergence rate can obtained using multigrid methods (see Multigrid Methods). For LCPs, suitable projected multigrid methods have been considered in  $[7, 33, 34]$ , for example. The basic idea is to use a sequence of coarser grids to get better corrections with a small computational effort. These methods are more involved and thus it takes more effort to implement them. Nevertheless, for higher dimensional models, it may be necessary to use these methods to keep computation times feasible.

The LCP  $(21)$  can be equivalently formulated as a linear programming (LP) problem [14] when  $\mathbf{B}$  is a Z-matrix (offdiagonal entries are nonpositive, that is,  $B_{i,j} \leq 0$  for all  $i \neq j$ ) and it is strictly diagonal dominant with positive diagonal entries. The solution  $\mathbf{V}$  of equation (21) is given by the LP

$$\min_{\mathbf{V}\in F} \mathbf{c}^T \mathbf{V}, \quad F = \{ \mathbf{V} \in \mathbb{R}^{p+1} \, : \, \mathbf{V} \ge \mathbf{g}, \, \mathbf{B} \mathbf{V} \ge \mathbf{b} \}$$
(22)

for any fixed  $\mathbf{c} > 0$  in  $\mathbb{R}^{p+1}$ . The LP problems can be solved using the (direct) simplex method or an

(iterative) interior point method. For discussion on this approach see [14].

When the matrix **B** is symmetric (**B***<sup>T</sup>* = **B**) and strictly diagonal dominant with positive diagonal entries, the LCP (21) can be equivalently formulated as a quadratic programming (QP) problem, which reads

$$\min_{\mathbf{V} \ge g} \frac{1}{2} \mathbf{V}^T \mathbf{B} \mathbf{V} - \mathbf{b}^T \mathbf{V} \tag{23}$$

There exists a host of methods to solve such QP problems. Our example of discretization above does not lead to a symmetric matrix **B**. However, it is often possible to symmetrize the problem by performing a coordinate transformation for the underlying operator or by applying a diagonal similarity transform to LCP. Particularly, these two approaches are applicable for the Black–Scholes operator. For example, we could employ a common transformation to the heat equation to symmetrize **B**.

The Brennan–Schwartz algorithm [8] is a direct method to solve the LCP (21) with a tridiagonal matrix **B**. In [27], it has been shown that the algorithm gives the solution of the LCP when **B** is a strictly diagonal dominant matrix with positive diagonal entries and there exists *k* such that *Vi* = *gi* for all *i* ≤ *k* and *Vi > gi* for all *i>k*. The latter condition means that the early exercise region is *(*0*, Sk)*. This is the case with a put option. A similar direct method has been considered in [16].

Effectively, the algorithm forms an **UL** decomposition for **B** such that **L** is a bidiagonal lowertriangular matrix and **U** is a bidiagonal uppertriangular matrix with ones on the diagonal. Then it performs the steps of solving the system **ULV** = **b** with the modification that in the backsubstitution step employing **L**, the components of **V** are projected to be feasible (*Vi* = max{*Vi, gi*}) as soon as they are computed. The following pseudocode solves the LCP (21) using the Brennan–Schwartz algorithm.

Algorithm BS(**B**, **V**, **b**, **g**)  

$$w_{p+1} = B_{p+1,p+1}$$
  
For  $i = p, 1, -1$   
 $w_i = B_{i,i} - B_{i,i+1}B_{i+1,i}/w_{i+1}$   
 $V_i = V_i - B_{i,i+1}V_{i+1}/w_{i+1}$   
End For  
 $V_1 = \max \{V_1/w_1, g_1\}$   
For  $i = 2, p + 1$   
 $V_i = \max \{(V_i - B_{i,i-1}V_{i-1})/w_i, g_i\}$   
End For

When the continuous early exercise region is *(Sk, S*max*)* for some *k*, there are two possible ways to use a Brennan–Schwartz-type algorithm. This is the case with a call option. The first one is to use the above code with the reverse index numbering for the vectors and matrices. Alternatively, the algorithm can be changed to use an **LU** decomposition instead of the **UL** decomposition.

The Brennan–Schwartz algorithm is usually the fastest way to solve LCPs when it is applicable. Direct methods for LCP with tridiagonal matrices can also be developed for more general exercise regions [13]. These methods are more complicated to implement and they are computationally more expensive.

The LCP (21) can be equivalently formulated using a Lagrange multiplier *λ* as

$$\begin{array}{ll} \mathbf{BV}-\boldsymbol{\lambda}=\mathbf{b},\\ \boldsymbol{\lambda}\geq\mathbf{0},\quad\mathbf{V}\geq\mathbf{g}\\ \boldsymbol{\lambda}^{T}(\mathbf{V}-\mathbf{g})=0 \end{array} \tag{24}$$

or, alternatively, [21] as

$$\begin{aligned} \mathbf{BV} - \boldsymbol{\lambda} &= \mathbf{b}, \\ \boldsymbol{\lambda} - \max\{\boldsymbol{\lambda} + \eta(\mathbf{g} - \mathbf{V}), \ \mathbf{0}\} &= \mathbf{0} \end{aligned} \tag{25}$$

for any *η >* 0. For these formulations, several active set solution strategies have been developed; see [1, 21, 42] and references therein.

# **Penalty Methods**

The penalty methods enforce the early exercise constraint by penalizing its violations. For the model LCP (21) a typical power penalty approximation is given by

$$\mathbf{BV} = \mathbf{b} + \frac{1}{\epsilon} [\max \left\{ \mathbf{g} - \mathbf{V}, \ \mathbf{0} \right\}]^k \tag{26}$$

where the maximum and the power function are applied componentwise, and  *>* 0 is a small penalty parameter. The linear penalty *k* = 1 and the quadratic penalty *k* = 2 are the most common ones. For example, the linear penalty was considered for the Black–Scholes model in [17], and both linear and quadratic penalties were considered for the Heston stochastic volatility model in [45]. The penalty parameter  $\epsilon$  controls the quality of the approximation. A small value for  $\epsilon$  enforces the constraint more strictly. The following pseudocode performs one (semismooth) Newton iteration for the system of nonlinear equations (26). The vector  $\mathbf{V}$  contains the initial guess for the solution or the vector  $\mathbf{V}$  returned by the previous iteration.

Algorithm Penalty(**B**, **V**, **b**, **g**)  

$$\mathbf{J} = \mathbf{B}$$
For  $i = 1, p + 1$   
 $r_i = b_i - \sum_j B_{i,j} V_j$   
If  $V_i < g_i$  Then  
 $r_i = r_i + \frac{1}{\epsilon} (g_i - V_i)^k$   
 $J_{i,i} = J_{i,i} + \frac{1}{\epsilon} k (g_i - V_i)^{k-1}$   
End If  
End For  
Solve  $\mathbf{Jd} = \mathbf{r}$   
 $\mathbf{V} = \mathbf{V} + \mathbf{d}$ 

For our example of discretization, the Jacobian matrix **J** is tridiagonal and the system  $\mathbf{Jd} = \mathbf{r}$  can be solved efficiently using an LU decomposition (or the UL decomposition used by Algorithm BS), for example. With higher dimensional models, it is probably necessary to solve these problems iteratively to obtain reasonable computational times. Under the Heston model, the BiCGSTAB method with an incomplete  $LU$  preconditioner was used in [45] and a multigrid method was used in [25].

The penalty approximation (26) leads to  $V$  that violates the early exercise constraint  $V \geq g$  by a small amount in the early exercise region. The size of the violation depends on the penalty parameter  $\epsilon$  and the violation vanishes when  $\epsilon$  approaches zero. The use of very small values for  $\epsilon$  can lead to numerical difficulties. A modified penalty approximation in [26],

$$\mathbf{BV} = \mathbf{b} + \max\{\bar{\lambda} + (\mathbf{g} - \mathbf{V})/\epsilon, \ \mathbf{0}\}\tag{27}$$

with  $\bar{\lambda} = \max\{\mathbf{Bg} - \mathbf{b}, \mathbf{0}\}\$  can be shown to lead always to V satisfying the constraint  $V \geq g$ . For example, the above (semismooth) Newton method can be modified to solve the system (27). Another penalty function enforcing the constraint strictly was considered in  $[32]$ .

## Other Approximations for LCP

The simplest way to enforce the early exercise constraint  $V > g$  is to treat it explicitly. In this socalled explicit payoff method, one first solves the system of linear equations

$$\mathbf{B}\hat{\mathbf{V}} = \mathbf{b} \tag{28}$$

and then the intermediate solution  $\tilde{\mathbf{V}}$  is projected to be feasible by setting

$$\mathbf{V} = \max{\{\tilde{\mathbf{V}}, \ \mathbf{g}\}}\tag{29}$$

Typically, this approach leads the order of accuracy to be only  $\Delta \tau$ . With the explicit Euler method, the LCP  $(21)$  reduces to the steps in equations  $(28)$  and (29) with **B** being the  $p + 1 \times p + 1$  identity matrix. Owing to the stability restriction of the explicit Euler method, the time step  $\Delta \tau$  has to be of order  $(\Delta S)^2$ . Thus with the explicit Euler method, the order of accuracy usually is  $\Delta \tau \sim (\Delta S)^2$ .

Another approach to approximate the LCP with a system of linear equations and a correction enforcing the constraint is to employ an operator splitting method [23, 25]. This method is based on the Lagrange multiplier formulation (24). The basic idea is to use the Lagrange multiplier  $\lambda$  from the previous time step to form a linear system, and then update the solution and Lagrange multiplier to satisfy the constraints pointwise. In the first step, the system of linear equations reads

$$\mathbf{B}\mathbf{V}^{n+1} = \mathbf{b}^n + \boldsymbol{\lambda}^n \tag{30}$$

and the correction in the second step is

$$\mathbf{V}^{n+1} - \tilde{\mathbf{V}}^{n+1} = \boldsymbol{\lambda}^{n+1} - \boldsymbol{\lambda}^{n},$$
  
$$\boldsymbol{\lambda}^{n+1} \ge \mathbf{0}, \qquad \mathbf{V}^{n+1} \ge \mathbf{g},$$
  
$$(\boldsymbol{\lambda}^{n+1})^{T} (\mathbf{V}^{n+1} - \mathbf{g}) = 0 \tag{31}$$

For higher dimensional models like the Heston model or options on several assets, the LCPs are much more challenging to solve than those with one-dimensional models. One approach is to approximate the resulting problems with a sequence of problems corresponding to a one-dimensional model as in alternating direction implicit (ADI) schemes (see Alternating Direction Implicit (ADI) Method). With early exercise possibility, this approach usually leads to solving LCPs with Black-Scholes-type one-dimensional models. When the solutions have suitable form, these LCPs can be solved efficiently using the Brennan-Schwartz algorithm. Such methods have been considered for American options in [24, 25, 39].

#### Example

As an example, we consider pricing an American put option with the parameters:  $S = K = 100, r = 0.1,$  $T = 0.25$  years, and  $\sigma = 0.2$ . The same option was also priced in [17]. For discretization, we truncate the semi-infinite interval at  $S_{\text{max}} = 400$ , and we construct nonuniform time-space grids that are refined near the expiry date  $\tau = 0$  and the strike price K. The space grid is constructed using the formula  $(10)$  with  $\xi = 0.4$ . We choose the time steps explicitly for the Rannacher time stepping according to the formulas  $(19).$ 

We compute the option price using the Brennan-Schwartz algorithm, the linear penalty method with  $\epsilon = (\Delta \tau^m)^2$ , and the PSOR method. For a comparison, we also use the explicit payoff method. Table 1 reports the results. The errors with the explicit and implicit treatments of the constraint are given for a sequence of grids. All implicit methods give essentially the same accuracy. The total iteration counts are reported for the penalty method and the PSOR method. We have optimized the relaxation parameter  $\omega$  for each grid. CPU times show that it is possible to price hundreds of options with a good precision in one second under the Black-Scholes model.

We have plotted a very coarse grid and an approximation of the early exercise boundary  $S_f(\tau)$ in Figure 1. It shows a typical jagged boundary obtained using the LCP formulation. Though the approximation of  $S_f(\tau)$  can be only  $\Delta S$  Accurate, the order of accuracy for the price appears to be  $(\Delta S)^2$ and  $(\Delta \tau)^2$  with the implicit treatment of the early exercise constraint. This behavior is studied in [17], which concludes that with suitably chosen time steps a quadratic convergence rate is attainable.

**Table 1** Numerical results with different methods for an American put option. The parameters are  $S = K = 100, r = 0.1$ ,  $T = 0.25$  years, and  $\sigma = 0.2$ . The reference price is 3.0701067. The number of time steps is m and the number of space grid points is  $p+1$ . Ratio is the ratio of successive errors. Iter is the total number of iterations. Time is the CPU time in seconds on a 3.2-GHz Pentium 4 PC

| Grid |               | Explicit              |       | Direct | Implicit              |       | BS     | Penalty |        | $\mathsf{PSOR}$ |        |
|------|---------------|-----------------------|-------|--------|-----------------------|-------|--------|---------|--------|-----------------|--------|
| m    | $\mathcal{D}$ | error at $K$          | ratio | time   | error at $K$          | ratio | time   | iter    | time   | iter            | time   |
| 18   | 80            | $-3.1 \times 10^{-2}$ |       | 0.0002 | $-1.5 \times 10^{-2}$ |       | 0.0003 | 24      | 0.0004 | 204             | 0.0010 |
| 34   | 160           | $-1.2 \times 10^{-2}$ | 2.5   | 0.0008 | $-3.7 \times 10^{-3}$ | 4.0   | 0.0009 | 47      | 0.0013 | 511             | 0.0045 |
| 66   | 320           | $-5.3 \times 10^{-3}$ | 2.3   | 0.0032 | $-9.5 \times 10^{-4}$ | 3.9   | 0.0034 | 91      | 0.0053 | 1236            | 0.0212 |
| 130  | 640           | $-2.5 \times 10^{-3}$ | 2.1   | 0.0124 | $-2.4 \times 10^{-4}$ | 3.9   | 0.0139 | 179     | 0.0208 | 3205            | 0.1071 |
| 258  | 1280          | $-1.2 \times 10^{-3}$ | 2.1   | 0.0506 | $-6.0 \times 10^{-5}$ | 4.0   | 0.0561 | 356     | 0.0858 | 8315            | 0.5645 |

![](_page_6_Figure_9.jpeg)

**Figure 1** A part of 41  $\times$  10 space-time grid and an approximation of the early exercise boundary  $S_f(\tau)$  given by the Brennan-Schwartz algorithm

# **Other Models and Options**

Often it is desirable to add jumps to the model of the underlying asset (*see* **Exponential Levy Models ´** ; **Variance-gamma Model**; **Jump-diffusion Models**). Models with jumps lead to a partial integro differential equation (PIDE) for the price of European options (*see* **Partial Integro-differential Equations (PIDEs)**) and an LCP with same operator can be derived for the price of American options. The discretization of these problems can lead to nonsparse matrices and the efficient solution of the resulting equations is more challenging. Finite-differencebased methods for pricing American options under jump models have been considered in [3, 10, 19, 31, 37, 38, 40, 41].

Stochastic volatility models like the Heston model (*see* **Heston Model**) lead to LCPs with partial differential operators with two space dimensions. These can be discretized with finite differences in a fairly straightforward manner. Owing to the correlation between the asset value and its volatility the resulting partial differential operator has a second-order cross derivative that can lead to numerical issues. No direct method like the Brennan–Schwartz algorithm is available for these problems. Furthermore, because of two space dimensions, the systems resulting from the discretization are much larger. Finite difference methods for options under stochastic volatility models have been considered in [9, 24, 25, 33, 45]. Similar discretizations and solution methods can be used when interest rates or dividends are modeled as stochastic.

Asian options lead to partial differential operator with an additional dimension for the average of the underlying asset. Similar finite difference methods can be used for American-style Asian options as for the above-mentioned options. The partial differential operator has only the first derivative present in the direction of the new dimension, and this makes discretizing the operator more involved. Americanstyle Asian options have been priced numerically in [20, 44], for example.

The payoff of a multiasset option depends on several underlying assets. Each underlying asset adds one dimension to the model, leading to high dimensional problems. With a few underlying assets, the standard finite difference methods can still be used. For example, American basket options on two stocks were priced in [39]. With the standard finite differences, the computational cost grows to be high with several underlying assets; see [34]. A special sparse grid technique can be used to reduce the size of the discrete problem (*see* **Sparse Grids**). This technique relies on the regularity properties of the price function *V* . The early exercise possibility reduces the regularity of *V* and thus the straightforward application of the sparse grid technique for American options might lead to reduced accuracy for the price. Nevertheless, in [35] it was observed that the accuracy for American options was still good.

# **Related Topics**

The grids and time steps are chosen usually on the basis of the behavior of discretization error in numerical experiments. Error estimation gives a more systematic way to choose (nearly) optimal discretizations where the number of grid points and time steps are minimized to reach a desired accuracy. In [30] finite difference discretizations were constructed on the basis of an error estimate for European multiasset options. For finite elements, error estimation has been consider in [1] for European options and in [2] for American options.

# **References**

- [1] Achdou, Y. & Pironneau, O. (2005). *Computational Methods for Option Pricing*, *Frontiers in Applied Mathematics*, SIAM, Philadelphia, Vol. 30.
- [2] Allegretto, W., Lin, Y. & Yan, N. (2006). A posteriori error analysis for FEM of American options, *Discrete Continuous Dynamical Systems Series B* **6**, 957–978.
- [3] Almendral, A. & Oosterlee, C.W. (2007). Accurate evaluation of European and American options under the CGMY process, *SIAM Journal of Scientific Computing* **29**, 93–117.
- [4] Benth, F.E., Karlsen, K.H. & Reikvam, K. (2003). A semilinear Black and Scholes partial differential equation for valuing American options, *Finance and Stochastics* **7**, 277–298.
- [5] Benth, F.E., Karlsen, K.H. & Reikvam, K. (2004). A semilinear Black and Scholes partial differential equation for valuing American options: approximate solutions and convergence, *Interfaces and Free Boundaries* **6**, 379–404.
- [6] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.

- [7] Brandt, A. & Cryer, C.W. (1983). Multigrid algorithms for the solution of linear complementarity problems arising from free boundary problems, *SIAM Journal on Scientific and Statistical Computing* **4**, 655–684.
- [8] Brennan, M.J. & Schwartz, E.S. (1977). The valuation of American put options, *Journal of Finance* **32**, 449–462.
- [9] Clarke, N. & Parrott, K. (1999). Multigrid for American option pricing with stochastic volatility, *Applied Mathematical Finance* **6**, 177–195.
- [10] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman & Hall/CRC, Boca Raton.
- [11] Cottle, R.W., Pang, J.-S. & Stone, R.E. (1992). *The Linear Complementarity Problem*, Academic Press, Boston.
- [12] Cryer, C.W. (1971). The solution of a quadratic programming problem using systematic overrelaxation, *SIAM Journal on Control* **9**, 385–392.
- [13] Cryer, C.W. (1983). The efficient solution of linear complementarity problems for tridiagonal Minkowski matrices, *ACM Transaction on Mathematical Software* **9**, 199–214.
- [14] Dempster, M.A.H. & Hutton, J.P. (1999). Pricing American stock options by linear programming, *Mathematical Finance* **9**, 229–254.
- [15] Duffy, D.J. (2006). *Finite Difference Methods in Financial Engineering*, *Wiley Finance Series*, John Wiley & Sons, Chichester.
- [16] Elliott, C.M. & Ockendon, J.R. (1982). *Weak and Variational Methods for Moving Boundary Problems*, *Research Notes in Mathematics*, Pitman, Boston, Vol. 59.
- [17] Forsyth, P.A. & Vetzal, K.R. (2002). Quadratic convergence for valuing American options using a penalty method, *SIAM Journal of Scientific Computing* **23**, 2095–2122.
- [18] Glowinski, R. (1984). *Numerical Methods for Nonlinear Variational Problems*, *Springer Series in Computational Physics*, Springer-Verlag, New York.
- [19] d'Halluin, Y., Forsyth, P.A. & Labahn, G. (2004). A penalty method for American options with jump diffusion processes, *Numerische Mathematik* **97**, 321–352.
- [20] d'Halluin, Y., Forsyth, P.A. & Labahn, G. (2005). A semi-Lagrangian approach for American Asian options under jump diffusion, *SIAM Journal of Scientific Computing* **27**, 315–345.
- [21] Hintermuller, M., Ito, K. & Kunisch, K. (2003). The ¨ primal-dual active set strategy as a semismooth Newton method, *SIAM Journal on Optimization* **13**, 865–888.
- [22] Huang, J. & Pang, J.-S. (1998). Option pricing and linear complementarity, *The Journal of Computational Finance* **2**, 31–60.
- [23] Ikonen, S. & Toivanen, J. (2004). Operator splitting methods for American option pricing, *Applied Mathematics Letters* **17**, 809–814.
- [24] Ikonen, S. & Toivanen, J. (2007). Componentwise splitting methods for pricing American options under stochastic volatility, *International Journal of Theoretical and Applied Finance* **10**, 331–361.
- [25] Ikonen, S. & Toivanen, J. (2007). Efficient numerical methods for pricing American options under stochastic

volatility, *Numerical Methods Partial Differential Equations* **24**, 104–126.

- [26] Ito, K. & Kunisch, K. (2006). Parabolic variational inequalities: The Lagrange multiplier approach, *Journal de Mathmatiques Pures et Appliquees* **85**, 415–449.
- [27] Jaillet, P., Lamberton, D. & Lapeyre, B. (1990). Variational inequalities and the pricing of American options, *Acta Applicandae Mathematicae* **21**, 263–289.
- [28] Kholodnyi, V.A. (1997). A nonlinear partial differential equation for American options in the entire domain of the state variable, *Nonlinear Analysis* **30**, 5059–5070.
- [29] Kuske, R.A. & Keller, J.B. (1998). Optimal exercise boundary for an American put option, *Applied Mathematical Finance* **5**, 107–116.
- [30] Lotstedt, P., Persson, J., von Sydow, L. & Tysk, J. ¨ (2007). Space-time adaptive finite difference method for European multi-asset options, *Computers & Mathematics with Applications* **53**, 1159–1180.
- [31] Matache, A.-M., Nitsche, P.-A. & Schwab, C. (2005). Wavelet Galerkin pricing of American options on Levy ´ driven assets, *Quantitative Finance* **5**, 403–424.
- [32] Nielsen, B.F., Skavhaug, O. & Tveito, A. (2002). Penalty and front-fixing methods for the numerical solution of American option problems, *The Journal of Computational Finance* **5**, 69–97.
- [33] Oosterlee, C.W. (2003). On multigrid for linear complementarity problems with application to American-style options, *Electronic Transactions on Numerical Analysis* **15**, 165–185.
- [34] Reisinger, C. & Wittum, G. (2004). On multigrid for anisotropic equations and variational inequalities: pricing multi-dimensional European and American options, *Computing and Visualization in Science* **7**, 189–197.
- [35] Reisinger, C. & Wittum, G. (2007). Efficient hierarchical approximation of high-dimensional option pricing problems, *SIAM Journal of Scientific Computing* **29**, 440–458.
- [36] Seydel, R.U. (2006). *Tools for Computational Finance*, 3rd Edition, Universitext, Springer-Verlag, Berlin.
- [37] Tavella, D. & Randall, C. (2000). *Pricing Financial Instruments: The Finite Difference Method*, John Wiley & Sons, Chichester.
- [38] Toivanen, J. (2008). Numerical valuation of European and American options under Kou's jump-diffusion model, *SIAM Journal of Scientific Computing* **30**, 1949–1970.
- [39] Villeneuve, S. & Zanette, A. (2002). Parabolic ADI methods for pricing American options on two stocks, *Mathematics of Operations Research* **27**, 121–149.
- [40] Wang, I.R., Wan, J.W.L. & Forsyth, P.A. (2007). Robust numerical valuation of European and American options under the CGMY process, *The Journal of Computational Finance* **10**, 31–69.
- [41] Zhang, X.L. (1997). Numerical analysis of American option pricing in a jump-diffusion model, *Mathematics of Operations Research* **22**, 668–690.

- [42] Zhang, K., Yang, X.Q. & Teo, K.L. (2006). Augmented Lagrangian method applied to American option pricing, *Automatica Journal of IFAC* **42**, 1407–1416.
- [43] Zhu, Y.-L., Chen, B.-M., Ren, H. & Xu, H. (2003). Application of the singularity-separating method to American exotic option pricing, *Advances in Computational Mathematics* **19**, 147–158.
- [44] Zvan, R., Forsyth, P.A. & Vetzal, K.R. (1998). Robust numerical methods for PDE models of Asian options, *The Journal of Computational Finance* **1**, 39–78.
- [45] Zvan, R., Forsyth, P.A. & Vetzal, K.R. (1998). Penalty methods for American options with stochastic volatility, *Journal of Computational and Applied Mathematics* **91**, 199–218.

# **Related Articles**

**Alternating Direction Implicit (ADI) Method**; **American Options**; **Asian Options**; **Crank–Nicolson Scheme**; **Jump-diffusion Models**; **Method of Lines**; **Monotone Schemes**; **Multigrid Methods**; **Partial Differential Equations**; **Partial Integrodifferential Equations (PIDEs)**; **Sparse Grids**.

JARI TOIVANEN
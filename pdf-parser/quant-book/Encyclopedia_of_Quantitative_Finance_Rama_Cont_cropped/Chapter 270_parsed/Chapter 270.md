# **Stochastic Mesh Method**

The stochastic mesh method has been proposed by Broadie and Glasserman [2] to price multivariate Bermudan options. These contracts include an early exercise feature, which makes their pricing a challenging computational problem. There are several methods available for options with payoff functions depending only on one asset. They include finite difference methods and approaches based on lattices (*see* **Finite Difference Methods for Early Exercise Options**). These methods, however, become typically ineffective for high-dimensional problems, like basket options.

The stochastic mesh approach belongs to simula tion-based methods, whose attractiveness for complex computational problems stems from the fact that the convergence rate is typically independent of the dimension of the problem.

The method is based on the dynamic programming representation and in each period uses a finite collection of points from the state space. In these aspects, the method is similar to the binomial tree approach. Its distinctive feature is that at each time interval the nodes are selected randomly and their number is always the same.

To illustrate the method, we consider a Bermudan option whose payoff depends only on the current price of an underlying asset. We assume that changes of the asset's price can be described by a Markov chain: {*Sti*}{*i*=0*,...,M*}, with values in <sup>R</sup>*<sup>b</sup>*. Since Bermudan options are often used to approximate prices of American options, {*Sti*}{*i*=0*,...,M*} may be obtained as a result of sampling a continuous process {*St*}{0≤*t*≤*<sup>T</sup>* }. The option can be exercised at *M* + 1 time points (including the initial time), which we shall denote as *t*0*, t*1*,...,tM* = *T* . At the time of exercise *τ* , the options are equal to *G(τ, Sτ )*, where *G* is a given function.

An arbitrage-free price of the option can be obtained by using the risk-neutral representation:

$$P(t_0, S_0) := \max_{\tau} E[B(t_0, \tau)G(\tau, S_\tau)] \qquad (1)$$

where *τ* is a stopping time that takes values in the set {*t*0*, t*1*,...,T* }. Here, the expectation is taken with respect to a given risk-neutral measure, *Q*, and *B(s, t)* denotes the discount factor for the period *(s, t)*. The main difficulty in using equation (1) is due to the fact that the optimal exercise strategy is unknown. The price of the option and the optimal strategy can be obtained, however, from the dynamic programming characterization of the problem. For this, we use the following backward recursion to calculate, for *i* = *M,... ,* 0, functions *P (ti,* ·*)*:

$$P(T, x) = G(T, x)$$
(2)  
$$P(t_i, x) = \max\{G(t_i, x), C(t_i, x)\},$$
  
$$i = M - 1, \dots, 0$$
(3)

where the continuation value, *C(ti, x)*, is defined as

$$C(t_i, x) := B_{t_i} E[P(t_{i+1}, S_{t_{i+1}})|S_{t_i} = x]$$
(4)

Then the price of the instrument at *t*<sup>0</sup> is given by *P (t*0*, S*0*)*. For simplicity of exposition, we assume that the discount factor *Bti* ≡ *B(ti, ti*<sup>+</sup>1*)* is deterministic, but in a more general formulation of the method it can be stochastic.

To use this method in practice, we must be able to efficiently calculate the conditional expectation

$$E[P(t_{i+1}, S_{t_{i+1}})|S_{t_i} = x]$$
 (5)

for *i* = 0*,...,M* − 1 and the selected set of points *x* from the state space. To accomplish this, several techniques have been proposed, including binomial trees and Monte Carlo simulations.

In the stochastic mesh method, the expectation (5) are approximated by arithmetic sums. For this, in the first phase, we generate at each exercise time *ti, i* = 0*,...,M*, the same number of random points, {*xij , j* = 1*,...,d*}. Then, at each node of the mesh the option price is calculated using the backward recursion. At the terminal nodes, we take *P (T , x* ˆ *Mj )* = *G(T , xMj ), j* = 1*,...,d*. At all other exercise times, we estimate the price of the option using the following mesh estimator

$$\hat{P}(t_i, x_{ij}) = \max\{G(t_i, x_{ij}), \ \hat{C}(t_i, x_{ij})\} \qquad (6)$$

with the estimate *C*ˆ of the continuation value defined by

$$\hat{C}(t_i, x_{ij}) := B_{t_i} \frac{1}{d} \sum_{k=1}^d \hat{P}(t_{i+1}, x_{(i+1)k}) w_i(j, k) \quad (7)$$

where *wi(j, k)* ≡ *wi(xij , x(i*<sup>+</sup>1*)k )* is a weight attached to the pair *(xij , x(i*<sup>+</sup>1*)k)*. Thus, for each fixed node at

![](_page_1_Figure_1.jpeg)

**Figure 1** An example of a stochastic mesh with *d* = 4. Weight that is attached to each arc is used in a weightedsum approximation to the corresponding continuation value

time *ti*, all nodes at the next time are used to calculate the corresponding continuation value. This has been depicted in Figure 1 for *d* = 4. Selection of these weights depends on the mechanism we have used to generate the mesh points {*xij* }. The weighted sum (7) can be interpreted as an estimate of the conditional expectation (5) when the process is in state *xij* at time *ti*. Since in calculations we always use all mesh points at the next time, regardless of the current state of the process, the main purpose of these weights is to estimate the continuation values without bias. We provide more details about different mechanisms of selecting mesh points and weights in the following section.

# **Selection of the Mesh Points and Weights**

Proper choices of the mesh points and weights *wi(j, k)* in equation (7) are essential for the method to be successful. The approaches suggested in the literature are based on the assumption that the Markov process {*Sti*}*i*=0*,...,M* admits transition densities and they are known or can be evaluated numerically. We therefore assume that conditional on *Sti* = *x* the value of the process at the next time instance, *Sti*<sup>+</sup><sup>1</sup> , has density *f (ti, x,* ·*)*. Denote by *h(ti,* ·*)* the density of *Sti* conditional on the initial value *S*0. We refer to *h(ti,* ·*)* as the marginal density of *Sti* .

Broadie and Glasserman [2] have considered two constructions of mesh points, which we present in Figure 2. In both, the points {*xij , j* = 1*,...,b*} at time *ti* are generated as independent and identically distributed observations from some density *g(ti,* ·*)*, called the *mesh density function*. In the first method, the mesh density is allowed to depend on time but not on the mesh points generated at previous time intervals. In the second method, the mesh is constructed in a forward procedure where at time *ti* the points {*xij , j* = 1*,...,b*} are generated as samples from a mesh density that depends on observations at the previous time *ti*−1. Although other methods of generating mesh points have been proposed later (e.g., [4]), we focus only on these two.

A natural choice for the mesh density *g(ti,* ·*)* is to take it equal to the marginal density function *h(ti,* ·*)*. In this case, the mesh points at time *ti* are generated independently of points at previous times *t*1*,...,ti*−1. Using a simple change of measure, we can transform conditional expectation (5) to an expectation with respect to the density *h(ti*<sup>+</sup>1*,* ·*)*:

$$E[P(t_{i+1}, S_{t_{i+1}})|S_{t_i} = x_{ij}]$$
  
=  $\int P(t_{i+1}, z) f(t_i, x_{ij}, z) dz$   
=  $\int P(t_{i+1}, z) \frac{f(t_i, x_{ij}, z)}{h(t_{i+1}, z)} h(t_{i+1}, z) dz$  (8)

![](_page_1_Figure_10.jpeg)

**Figure 2** Two methods of generating mesh points. (a) The points are generated independently at each time interval. (b) The points are generated by independent paths

Since this result is valid for any integrable function *P*, it implies that weighted sums with weights equal to the likelihood ratio

$$w_i(j,k) := \frac{f(t_i, x_{ij}, x_{(i+1)k})}{g(t_{i+1}, x_{(i+1)k})}$$
(9)

provide unbiased estimates of conditional expectations with respect to the transition density *f (ti, xij ,* ·*)*, meaning that

$$E\left[\frac{B_{t_i}}{d}\sum_{k=1}^{d}P(t_{i+1},X_k)w_i(x_{ij},X_k)\right] = C(t_i,x_{ij})$$
(10)

where *X*1*,...,Xd* are independent and identically distributed random variables with the common density equal to *g(ti*<sup>+</sup>1*,* ·*)*.

A drawback of selecting the mesh density equal to the marginal density function is that it can lead to estimators whose variance grows exponentially with the number of exercise times. In the context of an European option, this fact has been demonstrated by Broadie and Glasserman [2]. The authors have also observed that this build up of variance can be avoided if we choose the mesh density equal to the average of transition density functions

$$g^{A}(t_{i+1}, x_{i-}, x) = \frac{1}{d} \sum_{j=1}^{d} f(t_{i}, x_{ij}, x),$$
  
$$i = 1, \dots, M - 1 \qquad (11)$$

and *gA(t*1*, x)* = *f (t*0*, S*0*, x)*, where *xi*· denotes the vector of mesh points at time *ti*. For this choice of the density, points at time *ti*<sup>+</sup><sup>1</sup> are generated from a distribution that depends on the position of the mesh points at the previous time *ti*. The particular form of the mesh density (11) as a mixture of transition densities allows for two equivalent interpretations of the generation mechanism. In the first, we use a forward procedure where at each time we independently generate all points from the same distribution. To generate a point at time *ti* from the density *g(ti, x(i*<sup>−</sup>1*)*·*,* ·*)*, we first randomly choose a point from the set {*x(i*<sup>−</sup>1*)*1*,...,x(i*<sup>−</sup>1*)d* }, say *x(i*<sup>−</sup>1*)j* <sup>∗</sup> , and then sample from the transition density *f (ti*<sup>−</sup>1*, x(i*<sup>−</sup>1*)j* <sup>∗</sup> *,* ·*)*. This procedure is repeated until all *d* points have been obtained, after which we proceed to the next time interval. Alternatively, generating a mesh using equation (11) is equivalent to generating *d* independent paths of the process {*S*0*, St*<sup>1</sup> *,...,StM* }, as presented in Figure 2(b), and then disconnecting the nodes on each path.

For this construction of a mesh, we can use the likelihood ratio weights (9) with the mesh density *g(ti,* ·*)* replaced by *gA(ti, xi*·*,* ·*)*. These weights preserve the property of the weighted sum being an unbiased estimator of conditional expectation. In this case, however, expectation (10) is conditional on the position of the mesh points at the previous time *ti*−1.

# **Properties of the Method and Its Extensions**

The stochastic mesh method has an important property of being asymptotically consistent, meaning that by increasing the number of mesh points it can be assured that the mesh estimates will converge to the true price of the option. When the distributions used to sample mesh points are set to marginal distributions of the process, this result has been established by Broadie and Glasserman [2]. Avramidis and Matzinger [1] have proved the asymptotic consistency under weaker assumptions on the generating mechanism, which, in particular, cover the construction based on independent paths of the process {*Sti*}*i*=0*,...,M*.

Broadie and Glasserman [2] and Glasserman [4] have also shown that under some conditions on the mechanism of selecting the mesh points and weights in equation (7), the mesh estimator defined by equations (6) and (7) is biased high. This means that for a fixed number of mesh points and a fixed number of exercise opportunities, if we randomly generate sufficiently many meshes and calculate the corresponding mesh estimates, then the arithmetic average of all these estimates will be strictly greater than the true price of the option. The proof of this result uses Jensen's inequality and relies on a particular choice of weights that guarantees the unbiasedness property of the weighted sums (10). In particular, the likelihood ratios and the two constructions of the mesh points described in the previous section lead to mesh estimators that are bias high.

The bias high property of the method can be used to construct conservative confidence intervals for the option price. For this, we can combine the mesh estimator with any bias low estimator. The latter can be constructed quite easily, since an application of any exercise strategy in equation (1) that is different from the optimal one will lead to a bias low estimate of the price. Such a suboptimal stopping rule can also be constructed within the stochastic mesh method [2]. In the process of finding the mesh estimate through the dynamic programming procedure (6) and (7), each node of the mesh can be classified as either belonging to the exercise region or not, depending whether the maximum in equation (6) is equal to the current value of the option or the continuation value. This classification can be extended to an arbitrary state of the process. Because the immediate exercise value *G(ti, x)* in equation (6) is defined for all *x*, we need to estimate a continuation value *C(t* ˆ *i, x)* at an arbitrary state *x*. To do this, it suffices to extend the weights *wi(j, k)* to all points in the state space, which for the likelihood ratio weights (9) can be easily accomplished by simply replacing *xij* with *x*.

A bias low estimator, called *path estimator*, is based on the exercise region corresponding to these continuation values. Its value is obtained by randomly generating a certain number of trajectories of the underlying process and then stopping each trajectory if it reaches this exercise region. Thus, for the *j* th simulated path, *S<sup>j</sup>* , the exercise time *τ*ˆ is defined as

$$\hat{\tau}(S^{j}) = \min\{t_{i}: G(t_{i}, S^{j}_{t_{i}}) \ge \hat{C}(t_{i}, S^{j}_{t_{i}})\} \qquad (12)$$

in the case when the trajectory reaches the exercise region, and *τ*ˆ = *T* , otherwise. Then, conditional on this mesh, the path estimate based on *N*-simulated trajectories is simply the average of the discounted payoffs at the exercise time

$$\frac{1}{N} \sum_{j=1}^{N} B(t_0, \hat{\tau}(S^j)) G(\hat{\tau}(S^j), S^j_{\hat{\tau}(S^j)}) \qquad (13)$$

If we repeat this procedure for a number of independently generated meshes, then the sample mean of the estimates (13) obtained for each copy of the mesh will give a bias low estimate of the price of the option. Under some conditions, this estimator is asymptotically unbiased as the number of mesh points *d* increases to infinity. Therefore, the confidence interval that combines the bias high and the bias low estimators will shrink to the true price of the option as *d* → ∞ and the number of generated trajectories *N* increases to infinity.

Several numerical examples illustrating applications of the stochastic mesh method have been presented by Broadie and Glasserman [2]. Numerical tests conducted by the authors suggest that the efficiency of the method can be significantly improved when it is combined with some standard variance reduction techniques, in particular, those based on control variates (*see* **Variance Reduction**). Another way of enhancing the method is proposed in Boyle *et al.*, where mesh points are generated using lowdiscrepancy points (*see* **Quasi-Monte Carlo Methods**). A serious limitation of the method is the need for a transition density. To address this issue, in [3] the authors extend the stochastic mesh method by proposing to choose mesh weights through a constrained optimization problem.

# **References**

- [1] Avramidis, A.N. & Matzinger, H. (2004). Convergence of the stochastic mesh estimator for pricing Bermudan options, *The Journal of Computational Finance* **7**, 73–91.
- [2] Broadie, M. & Glasserman, P. (2004). A stochastic mesh method for pricing high-dimensional American options, *The Journal of Computational Finance* **7**, 35–72.
- [3] Broadie, M., Glasserman, P. & Ha, Z. (2000). Pricing American options by simulation using a stochastic mesh with optimized weights, in *Probabilistic Constrained Optimization: Methodology and Applications*, S. Uryasev, ed, Kluwer, Norwell, pp. 32–50.
- [4] Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*, Springer, New York.

# **Further Reading**

Boyle, P.P., Kolkiewicz, A. & Tan, K.S. (2001). Valuation of the reset options embedded in some equity-linked insurance products, *North American Actuarial Journal* **5**, 1–18.

# **Related Articles**

**American Options**; **Bermudan Options**; **Bermudan Swaptions and Callable Libor Exotics**; **Exercise Boundary Optimization Methods**; **Early Exercise Options: Upper Bounds**; **Finite Difference Methods for Early Exercise Options**; **Integral Equation Methods for Free Boundaries**; **Monte Carlo Simulation for Stochastic Differential Equations**; **Sparse Grids**; **Tree Methods**; **Weighted Monte Carlo**.

ADAM KOLKIEWICZ
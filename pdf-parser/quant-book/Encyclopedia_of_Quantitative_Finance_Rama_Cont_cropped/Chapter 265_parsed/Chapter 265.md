## **Bermudan Options**

A Bermudan option allows its holder to exercise the contract before maturity, and this feature makes its pricing significantly more difficult in comparison with the corresponding European option. Even for simple put options, currently there are no explicit formulae for their prices and therefore numerical methods must be employed. Although there are several such methods available for pricing Bermudan and American (see American Options) options depending on a single asset (see Finite Difference Methods for Early **Exercise Options**), these methods become typically ineffective for options on multiple assets. In such cases, we have to usually resort to methods based on Monte Carlo simulations. In this context, approaches that combine simulations with regression techniques have proven to be particularly effective. An attractive feature of these methods is that, in principle, they can be applied to any situation where trajectories of the underlying process can be simulated, since no other information about the process is required (unlike, e.g., the stochastic mesh method) (see Stochastic Mesh Method). In particular, they can be applied to pathdependent options. Since their introduction by several authors, especially Carrière [2], Thitsiklis and Van Roy [7], and Longstaff and Schwartz [4], the area of their applications has been extended beyond the pricing of Bermudan options, and currently it also includes the optimal dynamic asset allocation problem [1] and hedging [6].

Regression methods use the dynamic programming representation to determine the price of the option and also the optimal exercise strategy. To simplify the presentation of these methods, suppose that our objective is to price a Bermudan style option whose payoff depends only on the current value of the underlying security. The option can be exercised at  $M + 1$  time points (including the initial time), which we shall denote by  $t_0, t_1, \ldots, t_M = T$ . At the time of exercise,  $\tau$ , the value of the option is equal to  $G(\tau, S_{\tau})$ , where G is a payoff function. The dynamic of the price of the underlying security is described by a process  $\{S_{t_i}\}_{i=0,1,\dots,M}$ , which we assume to be a Markov chain with values in  $\mathcal{R}^b$ . This process may be obtained, for example, as a result of sampling a continuous process  $\{S_t\}_{\{0 \le t \le T\}}$  that solves a stochastic differential equation.

From the general theory of arbitrage-free pricing (see Risk-neutral Pricing), it follows that an arbitrage-free price of the option can be represented as the optimal expected discounted payoff:

$$P(t_0, S_0) := \max E[B(t_0, \tau)G(\tau, S_\tau)] \qquad (1)$$

where the expectation is taken with respect to a given risk-neutral measure O, and  $B(s, t)$  denotes the discount factor for the period  $(s, t)$ . The maximum in equation (1) is taken over all stopping times taking values in the set  $\{t_0, t_1, \ldots, t_M\}$ .

Since we do not know the optimal exercise strategy, a direct calculation of the price from equation (1) is not feasible. However, the price of the option can also be obtained by using the dynamic programming representation. For this, we use the following backward recursion to find functions  $P(t_i, \cdot)$ ,  $i =$  $1, \ldots, M$ ,

$$P(T, x) = G(T, x)$$
(2)  
$$P(t_i, x) = \max\{G(t_i, x), C(t_i, x)\},$$
  
$$i = M - 1, \dots, 0$$
(3)

where the continuation value,  $C(t_i, x)$ , is defined as

$$C(t_i, x) := B_i E[P(t_{i+1}, S_{t_{i+1}})|S_{t_i} = x] \qquad (4)$$

Then the price of the option at  $t_0$  is given by  $P(t_0, S_0)$ . In the last equation, we assume that the discount factor  $B_i \equiv B(t_i, t_{i+1})$  is deterministic. Equation (3) lends itself to a very intuitive explanation. At the  $i$ th exercise opportunity, the owner of the option makes the decision about early exercise by comparing the immediate exercise value with the present value of continuing. The larger of these two determines the present value of the option and the optimal action.

To use this method, in practice, we must be able to calculate efficiently the conditional expectations

$$E[P(t_{i+1}, S_{t_{i+1}})|S_{t_i} = x]$$
 (5)

for  $i = 0, \ldots, M - 1$  and some selected set of points  $x \in \mathbb{R}^b$  from the state space. Regression-based methods accomplish this through the regression of option values at the next time step on a set of regressors that depend on the current state. The main assumption behind these methods is that the conditional expectation (5) as a function of the state variable  $x$  can be represented in the form of an infinite series expansion, meaning that we have

$$C(t_i, x) = \sum_{j=1}^{\infty} a_{ij} \beta_j(x) \tag{6}$$

for some basis functions  $\beta_i : \mathcal{R}^b \to \mathcal{R}$  and constants  $\{a_{ij}\}\$ . Then an approximation to the continuation value can be obtained by using only a finite number of basis functions, say  $L$ . This can be accomplished, for example, by projecting  $C(t_i, \cdot)$  onto the span of the basis functions  $\beta_j$ ,  $j = 1, \ldots, L$ . If the projection space is equipped with a measure that corresponds to the distribution of  $S_{t_i}$ , then the coefficients in this approximation,  $a_{i1}^*, \ldots, a_{iL}^*$ , solve the following optimization problem

$$E\left[ (C(t_i, S_{t_i}) - \sum_{j=1}^{L} a_{ij}^* \beta_j (S_{t_i}))^2 \right]$$
  
= 
$$\min_{\{a_{i1}, \dots, a_{iL}\}} E\left[ (C(t_i, S_{t_i}) - \sum_{j=1}^{L} a_{ij} \beta_j (S_{t_i}))^2 \right]$$
  
(7)

Thus, here the continuation value is approximated by a member of a parametric family of functions. This method, however, cannot be implemented directly since the continuation value  $C(t_i, \cdot)$  is unknown. From the definition of  $C(t_i, \cdot)$ , it follows that for a single realization  $(s_{i1}, s_{(i+1)1})$  of the vector  $(S_{t_i}, S_{t_{i+1}})$ the continuation value  $C(t_i, s_{i1})$  can be approximated by  $B_{t_i} P(t_{i+1}, s_{(i+1)1})$ . This observation leads to the selection of the coefficients  $a_{i1}^*, \ldots, a_{iL}^*$  that minimize the following criterion (see  $[8]$ ):

$$E\left[ (B_i P(t_{i+1}, S_{t_{i+1}}) - \sum_{j=1}^{L} a_{ij} \beta_j (S_{t_i}))^2 \right] \quad (8)$$

where the expectation is taken with respect to the joint distribution of  $(S_{t_i}, S_{t_{i+1}})$ .

The argument that motivates the use of equation  $(8)$  as a method of approximation may suggest that the method will not be accurate, since we are approximating the continuation value at a given state by using only one successor. We should observe, however, that in this method we are not approximating continuation values individually at each state but rather we approximate the continuation value  $C(t_i, \cdot)$ treated as a function. Because of this and the assumed smoothness of this function, the resulting estimate of the continuation value at any state "borrows" also information about continuation values from points in a neighborhood of this state.

A factor that indeed determines the effectiveness of this approach is the selection of the basis functions. The assumption that guarantees the existence of the infinite series expansion (6) is rather a weak one, as any sufficiently smooth function can be approximated, for example, by polynomials. In practice, however, we have to truncate this expansion to a finite sum and hence we have to decide which terms we need to keep. The choice of a finite number of basis functions determines the success of the method and often must be crafted to the problem at hand. It becomes especially difficult for options on multiple assets, since then the number of required basis functions grows quickly with the dimension of the underlying price process.

On the basis of this method of approximation of continuation values, we can define an implementable procedure for pricing Bermudan options. For this, in equation  $(8)$  we have to substitute for  $P(t_{i+1}, \cdot)$  its approximation,  $\hat{P}(t_{i+1}, \cdot)$ , determined from the backward induction  $(2)-(4)$ . In addition, to find the coefficients  $a_{i1}^*, \ldots, a_{iM}^*$  that minimize equation  $(8)$ , typically we have to approximate the expectation by using a sample mean. The resulting algorithm can be summarized in the following way. In the first phase, we simulate  $N$  independent trajectories  $\{s_{1j}, \ldots, s_{Mj}\}, j = 1, \ldots, N$ , of the Markov chain  $\{S_{t_i}\}_{\{0 \le i \le M\}}$ . At maturity of the contract, we set  $\hat{P}_{Mj} = G(T, s_{Mj})$  and then start the backward induction. Given the estimated values  $\hat{P}_{(i+1)j}$ ,  $j =$ 1,..., *N*, we approximate the continuation value<br>at  $s_{ij}$  by  $\hat{C}_{ij} = \sum_{k=1}^{M} a_{ik}^* \beta_k(s_{ij})$ , where  $a_{i1}^*, \ldots, a_{iM}^*$ minimize

$$\sum_{j=1}^{N} \left[ B_i \hat{P}_{(i+1)j} - \sum_{k=1}^{M} a_{ik} \beta_k(s_{ij}) \right]^2 \tag{9}$$

Then, we set  $\hat{P}_{ij} = \max\{G(t_i, s_{ij}), \hat{C}_{ij}\}$ . Finally, the price of the option is calculated as  $\max\{B_o(\hat{P}_{11} +$  $\cdots + \hat{P}_{1N})/N, G(t_0, s_0)$ .

Carrière [2] has proposed a similar approach, but instead of approximating the continuation value by a member of a parametric family he suggests using nonparametric regression techniques based on splines and a local polynomial smoother. The approach proposed by Longstaff and Schwartz [4] is similar to the one presented here except that the authors use a different formula for calculating  $\hat{P}_{ij}$ . They also recommend using the least-squares method (9) only for options in the money.

Convergence properties of regression-based methods have been studied in [3, 5, 7, 8]. In particular, Clément et al. [3] prove convergence of the method proposed by Longstaff and Schwartz as the number of simulated trajectories,  $N$ , tends to infinity. Stentoft [5] presents a detailed numerical analysis of the Longstaff and Schwartz approach. By considering alternative families of polynomials and different numbers of basis functions, the author provides a guidance into the problem of proper selection of basis functions. He also finds that in problems with high number of assets the least-squares approach is superior to the binomial model method in terms of the trade-off between computational time and precision.

## References

[1] Brandt, M.W., Goyal, A., Santa-Clara, P. & Stroud, J.R.  $(2005)$ . A simulation approach to dynamic portfolio choice with an application to learning about return predictability, *Review of Financial Studies* **18**, 831–873.

- [2] Carrière, J. (1996). Valuation of early-exercise price of options using simulations and non-parametric regression, Insurance: Mathematics and Economics 19, 19-30.
- [3] Clément, E., Lamberton, D. & Protter, P. (2002). An analysis of a least squares regression algorithm for American option pricing, Finance and Stochastics 6, 449-471.
- [4] Longstaff, F.A. & Schwartz, E.S. (2001). Valuing American options by simulation: a simple least-squares approach, Review of Financial Studies 14, 113–147.
- [5] Stentoft, L. (2004). Assessing the least-squares Monte-Carlo approach to American option valuation, *Review of* Derivatives Research 7, 129–168.
- [6] Tebaldi, C. (2005). Hedging using simulation: a least squares approach, Journal of Economic Dynamics and Control 29, 1287-1312.
- [7] Thitsiklis, J. & Van Roy, B. (1999). Optimal stopping of Markov processes: Hilbert space theory, approximation algorithms, and an application to pricing highdimensional financial derivatives, IEEE Transactions on Automatic Control 44, 1840-1851.
- [8] Thitsiklis, J. & Van Roy, B. (2001). Regression methods for pricing complex American-style options, IEEE Transactions on Neural Networks 12, 694-703.

## **Related Articles**

American Options; Finite Difference Methods for Early Exercise Options; Integral Equation Methods for Free Boundaries; Monte Carlo Simulation for Stochastic Differential Equations.

ADAM KOLKIEWICZ
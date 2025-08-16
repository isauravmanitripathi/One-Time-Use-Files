# **Tree Methods**

Tree methods are among the most popular numerical methods to price financial derivatives. Mathematically speaking, they are easy to understand and do not require severe implementation skills to obtain algorithms to price financial derivatives. Tree methods basically consist in approximating the diffusion process modeling the underlying asset price by a discrete random walk.

In fact, the price of a European option of maturity  $T$  can always be written as an expectation either of the form

$$\mathbb{E}(\mathrm{e}^{-rT}\psi(S_T))$$

in the case of vanilla options or of the form

$$\mathbb{E}(\mathrm{e}^{-rT}\psi(S_t, 0 \le t \le T))$$

in the case of exotic options, where  $(S_t, t \ge 0)$  is a stochastic process describing the evolution of the stock price,  $\psi$  is the payoff function, and r is the instantaneous interest rate. The basic idea of tree methods is to approximate the stochastic process  $(S_t, t \ge 0)$  by a discrete Markov chain  $(\bar{S}_n^N, n \ge 0)$ , such that

$$\mathbb{E}(\mathrm{e}^{-rT}\psi(S_t, 0 \le t \le T))$$
  
 
$$\approx \mathbb{E}(\mathrm{e}^{-rT}\psi(\bar{S}_n^N, 0 \le n \le N)) \tag{1}$$

for N large enough ( $\approx$  is used to remind the reader that the equality is only guarantied for  $N = \infty$ ). To ensure the quality of the approximation, we are interested in a particular notion of convergence called convergence in distribution (weak convergence) of discrete Markov chains to continuous stochastic processes. It is interesting to note that tree methods can also be regarded as a particular case of explicit finite difference algorithms.

Tree methods provide natural algorithms to price both European and American options when the risky asset is modeled by a geometric Brownian motion (see  $[27]$ , for an introduction on how to use tree methods in financial problems). When considering more complex models—such as models with jumps or stochastic volatility models—the use of tree methods is much more difficult; analytic approaches like finite difference (see **Partial Differential Equations**; Partial Integro-differential Equations (PIDEs)) or finite element (see Finite Element Methods) methods are usually preferred, and Monte Carlo methods are also widely used for complex models. Binomial (see **Binomial Tree**) and trinomial trees may also be constructed to approximate the stochastic differential equation governing the short rate  $[21, 26]$  or the intensity of default [32], permitting hereby to obtain the price of, respectively, interest rate derivatives or credit derivatives. Implied binomial trees, which enable us to construct trees consistent with the market prices of plain vanilla options, are a generalization of the standard tree methods used to price more exotic options (see  $[11, 14]$ ).

For the sake of simplicity, consider a market model where the evolution of the risky asset is driven by the Black-Scholes stochastic differential equation

$$dS_t = S_t(r \, dt + \sigma \, dW_t), \quad S_0 = s_0 \tag{2}$$

in which  $(W_t)_{0 \le t \le T}$  is a standard Brownian motion (under the so-called risk neutral probability measure) and the positive constant  $\sigma$  is the volatility of the risky asset.

The seminal work of Cox-Ross-Rubinstein (CRR) [10] initiated the use of tree methods and many variants have been introduced to improve the quality of the approximation when pricing plain vanilla or exotic options.

#### **Plain Vanilla Options**

The multiplicative binomial CRR model [10] is interesting on its own as a basic discrete-time model for the underlying asset of a financial derivative, since it converges to a log-normal diffusion process under appropriate conditions. One of its most attractive features is the ease of implementation to price plain vanilla options by backward induction.

Let  $N$  denote the number of steps of the tree and  $\Delta T = T/N$  the corresponding time step. The log-normal diffusion process  $(S_{n\Delta T})_{0 \le n \le N}$ is approximated by the CRR binomial process  $\left(\bar{S}_{n}^{N} = s_{0} \prod_{j=1}^{n} Y_{j}\right)_{\substack{0 \leq n \leq N \ \text{algebra } Y_{1}, \ldots, Y_{N} \text{ are independent and identically dis$ tributed with values in  $\{d, u\}$  (*u* is called the *up factor* and *d* the *down factor*) with  $p_u = \mathbb{P}(Y_n = u)$ 

![](_page_1_Figure_1.jpeg)

Figure 1 CRR tree

and  $p_d = \mathbb{P}(Y_n = d)$ . The dynamics of the binomial tree (see Figure 1) is given by the following Markov chain:

$$\bar{S}_{n+1}^{N} = \begin{cases} \bar{S}_{n}^{N} u & \text{with probability} \quad p_{u} \\ \bar{S}_{n}^{N} d & \text{with probability} \quad p_{d} \end{cases} \tag{3}$$

Kushner and Dupuis [23] proved that the local consistency conditions given by equation  $(4)$ —that is, the matching at the first order in  $\Delta T$  of the first and second moments of the logarithmic increments of the approximating chain with those of the continuoustime limit—grant the convergence in distribution:

$$\mathbb{E}\log\frac{\bar{S}_{n+1}^{N}}{\bar{S}_{n}^{N}} = \mathbb{E}\log\frac{S_{(n+1)\Delta T}}{S_{n\Delta T}} + o\left(\Delta T\right)$$
$$\mathbb{E}\log^{2}\frac{\bar{S}_{n+1}^{N}}{\bar{S}_{n}^{N}} = \mathbb{E}\log^{2}\frac{S_{(n+1)\Delta T}}{S_{n\Delta T}} + o\left(\Delta T\right)$$
(4)

This first-order matching condition rewrites

$$\begin{cases} p_u \log u + (1 - p_u) \log \ d = (r - \frac{\sigma^2}{2}) \Delta T \\ p_u \log^2 u + (1 - p_u) \log^2 \ d = \sigma^2 \Delta T \end{cases} \tag{5}$$

The usual CRR tree corresponds to the choice  $u =$  $1/d = e^{\sigma\sqrt{\Delta T}}$ , which leads to  $p_u = e^{r\Delta T} - e^{-\sigma\sqrt{\Delta T}}/e^{\sigma\sqrt{\Delta T}} - e^{-\sigma\sqrt{\Delta T}} = 1/2 + r - \sigma^2/2/2\sigma\sqrt{\Delta T} + r$  $\mathcal{O}(\Delta T^{3/2})$ . When  $\Delta T$  is small enough (i.e., for N large), the above value of  $p_u$  belongs to [0,1]. For this choice of  $u$ ,  $d$ , and  $p_u$ , the difference between both sides of each equality in equation  $(5)$  is of order  $(\Delta T)^2$ . This is sufficient to ensure the convergence to the Black-Scholes model when  $N$  tends to infinity.

As  $(\bar{S}_n)_n$  defined by the CRR model is Markovian, the price at time  $n \in \{0, \ldots, N\}$  of an American put option (see American Options) in the CRR model with maturity  $T$  and strike  $K$  can be written as  $v(n, \bar{S}_n)$  where the function  $v(n, x)$  can be computed by the following backward dynamic programming eauations:

$$\begin{cases} v_N(N,x) = (K-x)^+\\ v_N(n,x) = \max\left(\psi(x),\\ e^{-r\Delta T} \big[ p_u v_N(n+1,xu)\\ v_N(n+1,xd) \big] \right) \end{cases} \tag{6}$$

where  $\psi(x) = (K - x)^{+}$ . Note that the algorithm requires the comparison between the intrinsic value and the continuation value. When considering European options,  $\psi \equiv 0$ .

The initial price of a put option in the Black-Scholes model can be approximated by  $v_N(0, s_0)$ . The initial delta, which is the quantity of risky asset in the replicating portfolio on the first time step in the CRR model, is approximated by  $v_N(1, s_0u)$   $v_N(1, s_0 d)/s_0(u - d)$ . Note that to obtain the approximated price and delta, one only needs to compute  $(v_N(n, s_0 u^k d^{n-k}), 0 \le k \le n)$  by backward induction on  $n$  from  $N$  to 0. Figure 2 gives an example of backward computation of the price of an American put option using  $N = 4$  time steps. The complexity of the algorithm is of order  $N^2$ , more precisely the function  $v_N$  has to be evaluated at  $(N + 1)(N + 2)/2$ nodes.

For the computation of the delta, Pelsser and Vorst [28] suggested to enlarge the original tree by adding two new initial nodes generated by an extended two-period back tree (dashed lines in Figure 2). To achieve the convergence in distribution, many other choices for  $u$ ,  $d$ ,  $p_u$ , and  $p_d$  can be made, leading to as many other Markov chains. We may choose other two-point schemes, such as a random walk approximation of the Brownian motion, threepoint schemes (trinomial trees), or more general  $p$ -point schemes. The random walk approximation of the Brownian motion  $(Z_{n+1} = Z_n + U_{n+1}$  with  $(U_i)_i$ independent and identically distributed with  $\mathbb{P}(U_i =$ 1) =  $\mathbb{P}(U_i = -1) = 1/2$ ) can be used as long as  $S_T$ is given by

$$S_T = s_0 e^{(r - \sigma^2/2)T + \sigma W_T} \tag{7}$$

![](_page_2_Figure_1.jpeg)

**Figure 2** Backward induction for a CRR tree with  $N = 4$ for an American put option with parameters  $s_0 = K = 100$ ,  $r = 0.1, \sigma = 0.2, T = 1$ 

This leads to  $p_u = 1/2$  and

$$u = e^{(r - \sigma^2/2)\Delta T + \sigma\sqrt{\Delta T}}$$
  

$$d = e^{(r - \sigma^2/2)\Delta T - \sigma\sqrt{\Delta T}}$$
(8)

The most popular trinomial tree has been introduced by Kamrad and Ritchken [22] who have chosen to approximate  $(S_{n\Delta T})_{0 \le n \le N}$  by a symmetric three-point Markov chain  $(\bar{S}_n)_{0 \le n \le N}$ 

$$\bar{S}_{n+1} = \begin{cases}\n\bar{S}_n u & \text{with probability} \quad p_u \\
\bar{S}_n & \text{with probability} \quad p_m \\
\bar{S}_n d & \text{with probability} \quad p_d\n\end{cases} \tag{9}$$

The convergence is ensured as soon as the first two moment matching condition on  $\log (S_{\Delta T}/s_0)$ is satisfied. With  $u = e^{\lambda \sigma \sqrt{\Delta T}}$  and  $d = 1/u$ , this condition leads to

$$p_u = \frac{1}{2\lambda^2} + \frac{\left(r - \sigma^2/2\right)\sqrt{\Delta T}}{2\lambda\sigma}, \quad p_m = 1 - \frac{1}{\lambda^2}$$
$$p_d = \frac{1}{2\lambda^2} - \frac{\left(r - \sigma^2/2\right)\sqrt{\Delta T}}{2\lambda\sigma} \tag{10}$$

The parameter  $\lambda$ —the stretch parameter—appears as a free parameter of the geometry of the tree, which can be tuned to improve the convergence. The value  $\lambda \approx 1.22474$  corresponding to  $p_m = 1/3$ 

is reported to be a good choice for at-the-money plain vanilla options. Note that choosing  $u = 1/d$ is essential to avoid a complexity explosion. In this case, the complexity is still of order  $N^2$ , but this time  $(N+1)(N+3)$  evaluations of the function  $v_N$  are required. The value  $\lambda = 1$  corresponds to the CRR tree.

Note that complexity is intimately related to the quality of the approximation. Therefore, one should always try to balance the additional computational cost with the improvement of the convergence it brings out.

#### **Convergence Issues**

Over the last years, significant advances have been made in understanding the convergence behavior of tree methods for option pricing and hedging (see [13, 24, 25, 33]). As noted in [12, 15], there are two sources of error in tree methods for call (see Call **Options**) or put option: the first one (*the distribution error*) ensues from the approximation of a continuous distribution by a discrete one, whereas the second one (*the nonlinearity error*) stems from the interplay between the strike and the grid nodes at the final time step. Because of the nonlinearity error, the convergence is slow except for at-the-money options. Let  $P_N^{\text{CRR}}$  and  $P^{\text{BS}}$  denote the initial price of the European put option with maturity  $T$  and strike  $K$ , respectively, in the CRR tree (with  $N$  steps) and in the Black-Scholes model. Using the call-put parity relationship in both the models and the results given for the call option in  $[13]$ , one finds

$$P_N^{\text{CRR}} = P^{\text{BS}} - \frac{K e^{-rT}}{N} e^{-d_2^2/2} \sqrt{\frac{2}{\pi}}$$
$$\times \left[ \kappa_N (\kappa_N - 1) \sigma \sqrt{T} + D_1 \right] + \mathcal{O}\left(\frac{1}{N^{3/2}}\right) \tag{11}$$

where  $d_2 = (\log(s_0/K) + (r - (\sigma^2/2))T)/\sigma\sqrt{T}, \kappa_N$ denotes the fractional part of  $\log(K/s_0)/2\sigma\sqrt{N/T}$  –  $N/2$  and  $D_1$  is a constant. For at-the-money options (i.e.,  $K = s_0$ ),  $\kappa_N = 0$  for N even and  $\kappa = 1/2$  for N odd; hence, the difference  $(P_N^{\text{CRR}} - P^{\text{BS}})_N$  is an alternating sequence. Figure<sup>a</sup> 3 shows that for  $N$  even  $P_N^{\text{CRR}}$  gives an upper estimate of  $P^{\text{BS}}$ , whereas for  $N$  odd  $P_N^{\rm{CRR}}$  gives a lower estimate. The monotonicity of  $(P_{2N+1})_N$  and  $(P_{2N})_N$  for at-the-money

![](_page_3_Figure_1.jpeg)

Figure 3 Convergence for an at-the-money put option with parameters  $s_0 = K = 100, r = 0.1, \sigma = 0.2, T = 1$ 

options enables us to use a Richardson extrapolation (i.e., consider  $2P_{4N}^{\text{CRR}} - P_{2N}^{\text{CRR}}$  or  $2P_{4N+1}^{\text{CRR}} - P_{2N+1}^{\text{CRR}}$ ) to make the terms of order  $1/N$  disappear. For not at-the-money options, Figure 4 shows that the sequences  $(P_{2N+1}^{\text{CRR}})_N$  and  $(P_{2N}^{\text{CRR}})_N$  are not monotonic and present an oscillating behavior. In this context, a naive Richardson extrapolation performs badly.

Several tree methods [6, 15, 18] try to deal with the nonlinearity error at maturity reproducing in some sense an at-the-money situation. The binomial Black-Scholes (BBS) method introduced by Broadie and Detemple [6] replaces at each node of the last but one time step before maturity, the continuation value with the Black-Scholes European one [3]. A two-point Richardson extrapolation aiming

![](_page_3_Figure_5.jpeg)

**Figure 4** Convergence for a not at-the-money put option with parameters  $s_0 = 100$ ,  $K = 90$ ,  $r = 0.1$ ,  $\sigma = 0.2$ ,  $T = 1$ 

at improving the convergence leads to the binomial Black-Scholes-Richardson (BBSR) method.

Adaptive mesh model (AMM) is a trinomial-based method introduced by Figlewski and Gao [15]. By taking into account that the nonlinearity error at maturity only affects the node nearest to the strike, AMM resorts to thickening the trinomial grid only around the strike and only at maturity time.

The binomial interpolated (with Richardson extrapolation) method (BI(R)) introduced by Gaudenzi and Pressacco [18] tries to recover the regularity of the sequences giving the CRR price of the European at-the-money options. The logic of the BI approach is to create a set of computational options, each one with a computational strike lying exactly on a final node of the tree. The value of the option with the contractual strike is then obtained by interpolating the values of the computational options.

Let us finally remark that similar techniques have been developed in numerical analysis for PDEs associated to option pricing problems (see [19]). In the case of nonsmooth initial conditions, to get good convergence of finite element and finite difference methods, there should always be a node at the strike and the payoff may have to be smoothed (see [30] for a classical reference).

In the American option case, a new source of error arises compared to the European case: the loss of opportunity to early exercise in any interval between two discrete times of the tree.

## **Exotic Options**

The classical CRR approach may be troublesome when applied to barrier options (see **Barrier Options**) because the convergence is very slow in comparison with plain vanilla options. The reason is quite obvious: let  $L$  be the barrier and  $n_L$  denote the index such that

$$s_0 d^{n_L} \ge L > s_0 d^{n_L+1}$$

Then, the binomial algorithm yields the same result for any value of the barrier between  $s_0 d^{n_L}$  and  $s_0 d^{n_L+1}$ , while the limiting value changes for every barrier  $L$ .

Several different approaches have been proposed to overcome this problem.

Boyle and Lau [5] choose the number of time steps in order to have a layer of nodes of the tree as close as possible to the barrier. Ritchken [31] noted that the trinomial method is more suitable than the binomial one. The main idea is to choose the stretch parameter *λ* such that the barrier is exactly hit. Later, Cheuk and Vorst [9] presented a modification of the trinomial tree (based on a change of the geometry of the tree), which enables to set a layer of the nodes exactly on the barrier for any choice of the number of time steps. Numerical interpolation techniques have also been provided by Derman *et al.* [12].

In the case of Asian options (*see* **Asian Options**; **Lattice Methods for Path-dependent Options**) with arithmetic average, the CRR method is not efficient since the number of possible averages increases exponentially with the number of the steps of the tree. For this reason, Hull and White [20] and in a similar way Barraquand and Pudet [2] proposed more feasible approaches. The main idea of their procedure is to restrict the possible arithmetic averages to a set of representative values. These values are selected in order to cover all the possible values of the averages reachable at each node of the tree. The price is then computed by a backward induction procedure, whereas the prices associated to the averages outside of representative value set are obtained by some suitable interpolation methods.

These techniques drastically reduce the computation time compared to the pure binomial tree; however, they present some drawbacks (convergence and numerical accuracy) as observed by Forsyth *et al.* [16]. Chalasani *et al.* [7, 8] proposed a completely different approach to obtain precise upper and lower bounds on the pure binomial price of Asian options. This algorithm significantly increases the precision of the estimates but induces a different problem: the implementation requires a lot of memory compared to the previous methods.

In the case of lookback options (*see* **Lookback Options**), the complexity of the pure binomial algorithm is of order *O(N*<sup>3</sup>*)* and the methods proposed in [2, 20] do not improve the efficiency. Babbs [1] gave a very efficient and accurate solution to the problem for American floating strike lookback options by using a procedure of complexity of order *O(N*<sup>2</sup>*)*. He proposed a change of "numeraire" approach, which cannot be applied in the fixed strike case.

Gaudenzi *et al.* [17] introduced the singular point method to price American path-dependent options. The main idea is to give a continuous representation of the option price function as a piecewise linear convex function of the path-dependent variable. These functions are characterized only by a set of points named *singular points*. Such functions can be evaluated by backward induction in a straightforward manner. Hence, this method provides an alternative and more efficient approach to evaluate the pure binomial prices associated with the path-dependent options. Moreover, because the piecewise linear function representing the price is convex, it is easy to obtain upper and lower bounds of the price.

For the rainbow options, extensions of the binomial approach for pricing American options on two or more stocks have been made by Boyle *et al.* [4] and Kamrad and Ritchken [22]. In higher dimensional problems (say, dimension greater than three), the straightforward application of tree methods fails because of the so-called curse of dimension: the computational cost and the memory requirement increase exponentially with the dimension of the problem.

## **End Notes**

a*.* The graphics have been generated using PREMIA software [29].

## **References**

- [1] Babbs, S. (2000). Binomial valuation of lookback options, *Journal of Economic Dynamics and Control* **24**, 1499–1525.
- [2] Barraquand, J. & Pudet, T. (1996). Pricing of American path-dependent contingent claims, *Mathematical Finance* **6**, 17–51.
- [3] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [4] Boyle, P.P., Evnine, J. & Gibbs, S. (1989). Numerical evaluation of multivariate contingent claims, *Review of Financial Studies* **2**, 241–250.
- [5] Boyle, P.P. & Lau, S.H. (1994). Bumping up against the barrier with the binomial method, *Journal of Derivatives* **1**, 6–14.
- [6] Broadie, M. & Detemple, J. (1996). American option valuation: new bounds, approximations and a comparison of existing methods, *The Review of Financial Studies* **9–4**, 1221–1250.
- [7] Chalasani, P., Jha, S., Egriboyun, F. & Varikooty, A. (1999). A refined binomial lattice for pricing American Asian options, *Review of Derivatives Research* **3**, 85–105.

- [8] Chalasani, P., Jha, S. & Varikooty, A. (1999). Accurate approximations for European Asian Options, *Journal of Computational Finance* **1**, 11–29.
- [9] Cheuk, T.H.F. & Vorst, T.C.F. (1996). Complex barrier options, *Journal of Derivatives* **4**, 8–22.
- [10] Cox, J., Ross, S.A. & Rubinstein, M. (1979). Option pricing: a simplified approach, *Journal of Financial Economics* **7**, 229–264.
- [11] Derman, E. & Kani, I. (1994). Riding on a smile, *Risk Magazine* **7**, 32–39.
- [12] Derman, E., Kani, I., Bardhan, D. & Ergener, E.B. (1995). Enhanced numerical methods for options with barriers, *Finance Analyst Journal* **51–6**, 65–74.
- [13] Diener, F. & Diener, M. (2004). Asymptotics of the price oscillations of a European call option in a tree model, *Mathematical Finance* **14**(2), 271–293.
- [14] Dupire, B. (1994). Pricing on a smile, *Risk Magazine* **7**, 18–20.
- [15] Figlewski, S. & Gao, B. (1999). The adaptive mesh model: a new approach to efficient option pricing, *Journal of Financial Economics* **53**, 313–351.
- [16] Forsyth, P.A., Vetzal, K.R. & Zvan, R. (2002). Convergence of numerical methods for valuing pathdependent options using interpolation, *Review of Derivatives Research* **5**, 273–314.
- [17] Gaudenzi, M., Lepellere, M.A. & Zanette, A. (2007). *The Singular Points Binomial Method For Pricing American Path-Dependent Options*, Working Paper, Finance Department, University of Udine, Vol. 1, pp. 1–17.
- [18] Gaudenzi, M. & Pressacco, F. (2003). An efficient binomial method for pricing American put options, *Decisions in Economics and Finance* **4–1**, 1–17.
- [19] Giles, M.B. & Carter, R. (2006). Convergence analysis of Crank-Nicolson and Rannacher time-marching, *Journal of Computational Finance* **4–9**, 89–112.
- [20] Hull, J. & White, A. (1993). Efficient procedures for valuing European and American path-dependent options, *Journal of Derivatives* **1**, 21–31.

- [21] Hull, J. & White, A. (1993). Numerical procedures for implementing term structure models I: single factor models, *Journal of derivatives* **2**, 7–16.
- [22] Kamrad, B. & Ritchken, P. (1991). Multinomial approximating models for options with k state variables, *Management Science* **37**, 1640–1652.
- [23] Kushner, H. & Dupuis, P.G. (1992). *Numerical Methods for Stochastic Control Problems in Continuous Time*, Springer Verlag.
- [24] Lamberton, D. (1998). Error estimates for the binomial approximation of American put options, *Annals of Applied Probability* **8**(1), 206–233.
- [25] Lamberton, D. (2002). Brownian optimal stopping and random walks, *Applied Mathematics and Optimization* **45**, 283–324.
- [26] Li, A., Ritchken, P. & Sankarasubramanian, L. (1995). Lattice methods for pricing American interest rate claims, *The Journal of Finance* **2**, 719–737.
- [27] Martini, C. (1999). *Introduction to Tree Methods for Financial Derivatives*. *PREMIA software documentation*. http://www.premia.fr.
- [28] Pelsser, A. & Vorst, T. (1994). The binomial model and the Greeks, *Journal of Derivatives* **1–3**(3), 45–49.
- [29] PREMIA. *An Option Pricer Project*. *MathFi, INRIA-ENPC*. http://www.premia.fr (accessed 2008).
- [30] Rannacher, A. (1984). Finite element solution of diffusion problems with irregular data, *Numerische Mathematik* **43–2**, 309–327.
- [31] Ritchken, P. (1995). On pricing barrier options, *Journal of Derivatives*, **3**, 19–28.
- [32] Schonbucher, P.J. (2002). A tree implementation of a credit spread model for credit derivatives, *Journal of Computational Finance* **6–2**, 1–38.
- [33] Walsh, J.B. (2003). The rate of convergence of the binomial tree scheme, *Finance and Stochastics* **7**, 337–361.

JER´ OME ˆ LELONG & ANTONINO ZANETTE
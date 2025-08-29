# 7 Optimal Execution with Continuous Trading 11

### 7.1 **Introduction**

In the previous chapter we studied the problem of optimal execution for an agent who aims to liquidate/acquire a considerable proportion of the average daily volume (ADV) of shares. There we saw how the agent trades off the impact on prices that her trades would have if she traded quickly, with the uncertainty in prices she would receive/pay if she traded slowly. We find that the agent's optimal strategy is to trade quickly initially ( ensuring that she receives a price close to the arrival price, but with a non-trivial impact) and then slow down as time goes by (to reduce her overall impact, but increase price uncertainty). Surprisingly, the optimal strategies we obtain are deterministic and in particular are independent of the midprice process - regardless of the level of urgency required to complete her trade. In this chapter, we incorporate a number of other important aspects of the problem that the agent may wish to include in her optimisation decision, and explore how her trading behaviour adjusts to account for them.

Specifically, we look at three distinct aspects of the optimal execution problem.

- **1.** An upper price limit: In Section 7.2 we study the problem of an agent wishing to acquire a large position, who has an upper price limit on what she is willing to pay. We find that the optimal strategy in this case is no longer independent of the midprice, beyond the obvious change that the agent stops trading when the upper limit price is breached.
- **11.** Informative order flow: In Section 7.3 we study the problem of an agent wishing to liquidate a large position, taking into account that the order flow from other traders in the market also impacts the midprice. We show that the agent alters her strategy so that when the net effect of other market participants is to trade in her direction, she increases her trading speed; conversely, if the net effect of other agents is to trade in the opposite direction, she decreases her trading speed.
- m. Dark pools: In Section 7.4, the agent has access to a (standard) lit market and also to a dark pool. Trading in the dark pool exposes her to execution risk, but removes some of the price impact. We find that the optimal strategy is still deterministic: initially the agent trades in the lit market at speeds below that dictated by Almgren & Chriss (2000) (AC), and posts the whole of the remaining order in the dark pool, in the hope of it being filled there.

After a while, if the order has not been filled in the dark pool, the agent's speed of trading in the lit pool increases above that of AC.

Throughout this chapter we use the same notation as in Chapter 6.

#### **Optimal Acquisition with a Price Limiter** 7.2

In this section we solve the problem for an agent whose target is to acquire  $\mathfrak{N}$  shares over a trading horizon of T, with a cap on the price at which she acquires shares equal to  $\overline{S}$ . If the midprice reaches this limit price before T, all remaining shares are immediately purchased and the acquisition programme stops. We assume that the midprice dynamics follow (6.1b) with  $g(\nu_t) = b \nu_t$ ,  $b \ge 0$ , and the execution price is as in (6.1c) with linear price impact  $f(\nu_t) = k \nu_t$ ,  $k > 0$ . The agent will stop trading if any one of the following events occur:

a. the agent's inventory reaches the target level  $\mathfrak{N}$ ,

- b. the terminal time  $T$  is reached,
- c. the midprice  $S_t$  reaches the upper *limit price*  $\overline{S}$ .

These define the following stopping time,  $\tau$ :

$$\tau = T \wedge \inf\{t \,:\, S_t = \overline{S}\} \wedge \{t \,:\, Q_t = \mathfrak{N}\}\,.$$

When either of events (b) or (c) occur, the agent acquires the remaining  $\mathfrak{N}-Q^{\nu}_{\tau}$ units of the security and pays  $S_{\tau} + \alpha (\mathfrak{N} - Q_{\tau}^{\nu})$  per unit, where  $\alpha > 0$ . To simplify notation we let  $Y_t^{\nu} = \mathfrak{N} - Q_t^{\nu}$  denote the remaining shares to be acquired, satisfying

$$dY_t^{\nu} = -\nu_t \, dt \,,$$

where  $\nu_t$  is the (positive) rate of trading.

To complete the setup of the problem, we write the agent's performance criteria as

$$H^{\nu}(t,S,y) = \mathbb{E}_{t,S,y} \left[ \int_{t}^{\tau} (S_{u} + k\nu_{u}) \,\nu_{u} \,du + \,y_{\tau} \,\left(S_{\tau} + \alpha \,y_{\tau}\right) + \phi \int_{t}^{\tau} \,y_{u}^{2} \,du \right],\tag{7.1}$$

where  $\phi \int_{t}^{\tau} y_{u}^{2} du$  with  $\phi \geq 0$  is a running inventory penalty of the remaining shares to be acquired (as discussed in the previous chapter this penalty is not a financial penalty), and her value function is

$$H(t, S, y) = \inf_{\nu \in \mathcal{A}} H^{\nu}(t, S, y) ,$$

for all  $0 \le t \le T$ ,  $S \le \overline{S}$ ,  $0 \le y \le Q$ , and  $\mathcal{A}$  is the admissible set of trading strategies in which  $\nu$  is non-negative and uniformly bounded from above.

Applying the dynamic programming principle (DPP), the value function should satisfy the dynamic programming equation (DPE)

$$\partial_t H + \frac{1}{2}\sigma^2 \partial_{SS} H + \phi y^2 + \min_{\nu} \left\{ -\nu \,\partial_y H + b\,\nu \,\partial_S H + \left( S + k\,\nu \right) \nu \right\} = 0\,,\tag{7.2a}$$

subject to the terminal and boundary conditions

$$H(T, S, y) = (S + \alpha y) y, \qquad (7.2b)$$

$$H(t,\overline{S},y) = (\overline{S} + \alpha y) y, \qquad (7.2c)$$

$$H(t, S, 0) = 0. \t(7.2d)$$

The terminal and boundary conditions reflect the fact that the agent acquires the remaining shares at the stopping time. Note that when her inventory equals the target 1)1: at *t* < T, she stops acquiring and there is no penalty, hence the value function equals zero along y = 0.

From the first order conditions, we obtain the optimal acquisition strategy in feedback form as

$$\nu^*(t,S,y) = -\frac{1}{2k} \left( b \,\partial_S H - \partial_y H + S \right) \,,$$

and upon substituting back into the DPE above, the value function *H* then solves the non-linear PDE

$$\partial_t H + \frac{1}{2}\sigma^2 \partial_{SS} H - \frac{1}{4k} \left( b \,\partial_S H - \partial_y H + S \right)^2 + \phi \, y^2 = 0\,,\tag{7.3}$$

subject to the terminal and boundary conditions in (7.2).

# **Dimensionality Reduction without Permanent Price Impact**

In general, the DPE (7.3) will have to be solved numerically; however, in practice it is normally the case that the effect of permanent impact is much smaller than the temporary impact from walking the LOB, so to reduce the dimension of the problem we set b = 0.

In this case, due to the form of the DPE (7.3) and its terminal and boundary conditions in (7.2), it is possible to solve for the dependence in q exactly by using the ansatz

$$H(t, S, y) = y S + y2 h(t, S),$$

in which case, the function h satisfies the Fisher-type PDE

$$\partial_t h + \frac{1}{2}\sigma^2 \partial_{SS} h - \frac{1}{k} h^2 + \phi = 0, \quad (t, S) \in [0, T) \times \left( -\infty, \overline{S} \right) \,, \tag{7.4a}$$

subject to the terminal and boundary conditions

$$h(T,S) = \alpha, \quad S \le \overline{S},\tag{7.4b}$$

$$h(t,\overline{S}) = \alpha, \quad t \le T,$$
(7.4c)

and, furthermore, the optimal acquisition strategy  $\nu^*$  reduces to

$$\nu^*(t,S,y) = \frac{1}{k} y h(t,S) \,. \tag{7.5}$$

In particular, it follows from  $(7.5)$  that as inventory Q increases (so that Y decreases), all else being equal, the optimal rate of acquisition slows down.

## Numerical Solution I: Crank-Nicolson

The  $(1+1)$ -dimensional terminal boundary value problem  $(7.4)$  can be efficiently solved numerically using a Crank-Nicolson scheme, by placing the problem on a grid in the domain  $[0,T] \times [S,\overline{S}]$  and treating the quadratic term  $h^2$  explicitly.

By introducing this grid, we now have a new boundary at  $S$ , and, in order to have a well-posed problem, we need to specify a boundary condition along  $S =$  $S \ll \overline{S}$ . A usual approach is to specify the boundary condition as  $\partial_{SS} h|_{S=S} = 0$ . In order to evaluate whether this is a reasonable boundary or not we determine what this condition implies about the behaviour of the optimal strategy at the lower boundary.

Denote  $\chi(t) = h(t,\underline{S})$ . Combining (7.4) with  $\partial_{SS}h(t,\underline{S}) = 0$ , we see that  $\chi(t)$ satisfies the ordinary differential equation  $(ODE)$ 

$$\begin{cases} \partial_t \chi - \frac{1}{k} \chi^2 + \phi &= 0, \quad t \in [0, T), \\ \chi(T) &= \alpha. \end{cases}$$

As this is a Riccati equation, its solution follows from standard methods (as outlined in Section  $6.5$ ) and is given explicitly by

$$\chi(t) = \begin{cases}\n\sqrt{k\phi} \frac{\zeta e^{2\gamma(T-t)} + 1}{\zeta e^{2\gamma(T-t)} - 1}, & \phi > 0, \\
\left(\frac{1}{\alpha} + \frac{T-t}{k}\right)^{-1}, & \phi = 0,\n\end{cases} \tag{7.6}$$

where the constants are

$$\gamma = \sqrt{\frac{\phi}{k}}\n$$
 and  $\n\zeta = \frac{\alpha + \sqrt{k\phi}}{\alpha - \sqrt{k\phi}}$ 

Note that  $0 \leq \chi(t) \leq \alpha$  and that  $\chi$  is increasing in t and takes on its maximum at  $t = T$ .

Moreover,  $qS + q^2\chi(t)$  is precisely the value function in which there is no limit price, as studied in Section 6.5 with permanent impact  $b$  set to zero. Therefore, the boundary condition  $\partial_{SS}h(t,\underline{S})=0$  leads to a solution which has an optimal trading speed equal to the no limit price trading speed.

Thus, imposing the boundary condition  $\partial_{SS}h(t,S) = 0$  generates a reasonable optimal behaviour on the boundary. But, if we accept this boundary condition because we think the boundary behaviour reasonable, we can equivalently, and more straightforwardly, restrict admissible strategies to those that generate the desired boundary behaviour:  $\nu$  must equal the no limit price strategy when  $S =$ 

fi. We therefore impose that the agent ignores the limit price when the midprice is sufficiently far away from it.

Although we cannot obtain an explicit solution to (7.4), we can obtain upper and lower bounds on the function *h(t, S)* by appealing to the maximum principle. First, from standard results in PDEs, a unique solution to (7.4) exists. Hence, by treating the non-linear term *h <sup>2</sup>*= *h* · Ti, where the term Ti is the solution to the PDE, we can invoke a standard maximum principle.

THEOREM 7.1 (Maximum Principle) *Suppose that* D C JR *is a bounded connected set and that* u : D x [O, oo) --+ JR *satisfies*

$$\begin{aligned} \partial_t u + \partial_{xx} u &= 0 \,, & x \in \Omega, \ t > 0 \,, \\ u(t, x) &= p(t) \,, & x \in \partial\Omega, \ t > 0 \,, \\ u(0, x) &= q(x) \,, & x \in \partial\Omega, \ t > 0 \,. \end{aligned}$$

*Then*

$$\max_{\overline{\Omega}\times[0,T]} u \le \max\left(p(t) \; ; \; \max_{\overline{\Omega}} q\right) \quad \text{and} \quad \min_{\overline{\Omega}\times[0,T]} u \ge \min\left(p(t) \; ; \; \min_{\overline{\Omega}} q\right) \, .$$

As noted earlier, *x(t)* is increasing in *t* and O � *x �* a. Hence a direct application of this maximum principle to (7.4), supplemented with the boundary condition *h(t,;i)* = *x(t)* (or as discussed, equivalently by restricting the trading strategy to equal the no limit price strategy along *S* = fi) provides us with upper and lower bounds on *h* as follows:

$$\chi(t) \le h(t, S) \le \alpha. \tag{7.7}$$

Since the optimal trading rate v\* ( *t, S, y)* = ½ *y h( t, S),* the above inequality implies that at each inventory level, the agent with the limit price constraint trades at least as fast as the agent without the limit price, and attains a maximal speed of trading of'/; *y.* This implies that the agent with the limit price constraint will have acquired more shares than the agent without the constraint at any given fixed point in time.

Finally, it is important to point out that the inventory held by the agent at any given time can be obtained in terms of the path of the midprice process by solving for Yt, where Yt satisfies the SDE

$$dY_t^* = -\nu_t^* \, dt = -\frac{1}{k} \, Y_t \, h(t, S_t) \, dt \,,$$

hence

$$Q_t^* = \left(1 - \exp\left\{-\frac{1}{k}\int_0^t h(u, S_u) \, du\right\}\right) \, \mathfrak{N}, \quad t \le \tau \, .$$

This has the same form as in the case without the limit price, but here the path that the midprice takes plays an important role in determining how much inventory the agent has at any given time. Below, after discussing an alternative numerical solution and the case T --+ oo, we show some examples of the optimal strategy for different midprice paths.

### Numerical Solution II: Iterative Scheme

An alternative approach to solving the non-linear terminal boundary value (TBV) problem  $(7.4)$  is to use an exact iterative scheme, rather than resorting to finitedifference methods. The essential idea is to take an approximate solution to the problem at the  $m^{th}$ -iteration, denote it by  $h^{(m-1)}(t, S)$ , and use it to linearise the TBV to obtain an updated approximation  $h^{(m)}(t, S)$  which solves the *linear*  $\text{TBV}$ 

$$\left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS} - \frac{1}{k} \,h^{(m-1)}(t,S)\right)h^{(m)}(t,S) + \phi = 0\tag{7.8a}$$

subject to

 $h^{(m)}(t,\overline{S}) = \alpha, \quad h^{(m)}(t,\underline{S}) = \chi(t), \quad \forall t \in [0,T),$  $(7.8b)$ 

and

$$h^{(m)}(T,S) = \alpha, \quad \forall S \in (\underline{S}, \overline{S}). \tag{7.8c}$$

At each iteration, the boundary and terminal conditions are respected, so all that changes is the behaviour of the solution in the interior. The solution to the PDE  $(7.8c)$  can be obtained in closed-form up to a Laplace transform by first introducing an integrating factor and writing

$$h^{(m)}(t,S) = e^{\frac{1}{k} \int_0^t h^{(m-1)}(u,S) \, du} \, g^{(m)}(t,S) \,,$$

so that  $q^{(m)}(t, S)$  satisfies the linear PDE

$$\left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)g^{(m)}(t,S) + \phi \,\ell^{(m-1)}(t,S) = 0\,,\tag{7.9a}$$

subject to

$$g^{(m)}(t,\overline{S}) = \alpha \,\ell^{(m-1)}(t,\overline{S}), \quad \text{and}$$
 (7.9b)

$$g^{(m)}(t,\underline{S}) = \chi(t) \,\ell^{(m-1)}(t,\underline{S}), \quad \forall t \in [0,T) \,, \tag{7.9c}$$

and

$$h^{(m)}(T,S) = \alpha \,\ell^{(m-1)}(T,S), \quad \forall S \in (\underline{S}, \overline{S})\,,\t$$
(7.9d)

where

$$\ell^{(m)}(t,S) = e^{-\frac{1}{k} \int_0^t h^{(m)}(u,S) \, du} \, .$$

The system of linear PDEs requires an initial guess to begin the iteration. One simple approach is to use a linear interpolation (in S) between  $h(t,\underline{S}) = \chi(t)$ and  $h(t,\overline{S}) = \alpha$  at each point in time. This initial guess can be written as

$$h^{(0)}(t,S) = \frac{S-\underline{S}}{\overline{S}-\underline{S}}\,\chi(t) + \frac{\overline{S}-S}{\overline{S}-\underline{S}}\,\alpha\,.$$

Armed with the initial guess, the above system of linear PDEs can in principle be solved using Laplace transform techniques. The final steps are to show that the mapping  $h^{(k-1)} \mapsto h^{(k)}$  is indeed a contraction mapping on a suitable space of functions, and then show that the sequence of solutions converges to the solution of the original non-linear PDE.

# **The Perpetual Case**

As mentioned earlier, the acquisition problem with the price limit may always be solved numerically, e.g. via a Crank-Nicolson scheme. However, if we assume that the agent's terminal date *T* -t oo, i.e. the agent trades until she acquires all inventory or the limit price is reached, then the problem reduces to a simpler one that we can solve analytically. In this case, h is independent of time and equation (7.4) reduces to a boundary value problem for the ODE

$$\frac{1}{2}\sigma^2 \partial_{SS}^2 h - \frac{1}{k}h^2 + \phi = 0, \quad S \in (\underline{S}, \overline{S}), \tag{7.10a}$$

with boundary conditions

$$h(\overline{S}) = \alpha$$
, and  $h(\underline{S}) = \sqrt{k\phi}$ . (7.10b)

The boundary condition h(S\_) = -!k¢ arises by recalling that we impose the condition *h(t,* S..) = x(t) and from (7.6) we have limr-+oo x(t) = *-!k<f>.* 

The general solution of equations of the above kind are elliptic functions see e.g., Chapter 18 in Abramowitz & Stegun (1972). In our specific case (with ¢ > 0), the solution can be written in terms of the Weierstrass g::i-function as follows:

$$h(S) = 3 k \sigma^2 \wp \left( S + C_1; \frac{4}{3} \frac{\phi}{k \sigma^4}, C_2 \right) , \qquad (7.11)$$

where the last two arguments denote the invariants of the elliptic function and the constants C1 and C2 must be determined numerically to match the boundary conditions in (7.10b).

If ¢ = 0 and S.. -t -oo the solution can be obtained in terms of elementary functions by solving the ODE (7.10a) using the ansatz *h(S)* = /31 *(S* + /32) /3*3,*  where /3<sup>1</sup> , /32, /33 are constants to be determined. Two of the constants can be obtained from the boundary conditions, and the third is obtained by ensuring the ansatz closes the ODE. We leave it as an exercise to show that the solution indeed reduces to the simple equation

$$h(S) = \frac{\sigma^2 k}{2} \left( \frac{\overline{S} - S}{\sqrt{6}} + \sqrt{\frac{\sigma^2 k}{2\alpha}} \right)^{-2} . \tag{7.12}$$

Recall that the optimal trading speed v\* = ¼ *y h(t,* S). Hence, the perpetual solution shows that the agent's speed of trading increases (for the same fixed amount of inventory) as the limit price S is approached from below. This is natural, since the agent observes the price getting closer to the limit and therefore wishes to acquire as many shares as possible prior to breaching the price cap without paying too much in immediate impact costs. Note, however, as inventory is acquired, the speed of trading slows down. The net result of these two opposing effects will depend on which of the two is stronger.

![](_page_7_Figure_1.jpeg)

**Figure 7.1** Left panel: The rate of acquisition relative to remaining inventory as a function of time and fundamental price. Right panel: the rate of acquisition relative to inventory as a function of S at  $t = 0$  for various volatility levels.

# Simulations of the Strategy with Price Limiter

We now illustrate several aspects of the agent's optimal behaviour when she imposes a price limiter in her strategy.

Throughout, we use the following parameters

$$T = 1 \text{ day}, \quad k = 10^{-4}, \quad b = 0,$$
  
 $\alpha = 100k, \quad \phi = 10^{-3}, \quad \sigma = 0.1.$ 

We also normalise the acquisition target to  $\mathfrak{N}=1$  (this can be viewed as a percentage of the ADV, and we assume the agent trades once per second). Recall that the ratio  $\alpha/k$  sets the maximum trading speed, hence our choice for  $\alpha$ . We set the limiting price to  $\overline{S} = S_0 + \sigma$  with initial price  $S_0 = 20$ , and our choice of volatility  $\sigma = 0.1 \, (\text{day})^{-\frac{1}{2}}$  corresponds to annualised relative volatility of  $0.1/20 \times \sqrt{255} \sim 8\%$ .

First, in the left panel of Figure  $7.1$  we depict the optimal execution strategy  $\nu^*$  relative to the current remaining inventory, i.e.  $\nu^*/y$ . As maturity approaches, the trading rate increases, because for a fixed number of shares remaining the agent must acquire faster to avoid the terminal penalty cost. Moreover, as the fundamental price approaches the limit price, the speed of trading also increases to avoid the terminal penalty. The bounds on the rate of trading implied by the maximum principle  $(7.7)$  can also be seen in the figure. In the case with no limit price, the agent's optimal strategy is independent of the asset's volatility. However, with the limit price, as shown in the right panel of Figure 7.1, the agent's behaviour does indeed depend on volatility. The more volatile the market, the faster the agent trades, but as the price moves far away from the limit price, the effect of volatility diminishes.

The agent's strategy is constantly being updated to reflect changes in her inventory (due to her own trading) and the innovations in the midprice, hence the static views in Figure 7.1 do not tell the full story. To gain additional insight

![](_page_8_Figure_1.jpeg)

Figure 7.2 Sample paths of the evolution of the midprice, acquisition rate and inventory. Dashed line in the bottom left panel represents the evolution of inventory in the corresponding AC strategy.

into the dynamic behaviour, in Figure 7.2 we plot three sample paths of the fundamental price together with the rate of acquisition, inventory, and cost per share. In the bottom left panel, using a dashed line, we include the inventories' lower bound, the Almgren-Chriss  $(AC)$  strategy, as described by the inequality in  $(7.7)$ .

As the figures show, the red path is mostly away from the limit price and after some initial noise, the agent's strategy is very close to the deterministic AC strategy. The blue path stays mostly near the arrival price so that the trading speed displays stochastic dynamics. The agent has an increased trading rate between  $t = 0.2$  and  $t = 0.3$  when the midprice approaches the limit price. Also, around  $t = 0.6$  the midprice almost touches the limit price and the agent's trading speed spikes there; however, due to aggressive trading earlier on, by that time she has already acquired a significant proportion of her shares, and the spike is not very large. The green path hits the limit price early on, and as the figure illustrates, the agent trades quickly (relative to the AC strategy) up until the price hits the boundary.

The bottom right panel of Figure 7.2 shows the cost per share along the three paths. Note that the green path, which hits the limit price early on, is more

![](_page_9_Figure_1.jpeg)

**Figure 7.3** Inventory and trading speed heat-maps from  $1,000$  simulations of the optimal strategy.

expensive than the other paths for two somewhat interrelated reasons: (i) the midprice was generally higher (and it hit the limit price) during trading; and (ii) since the price generally trended upwards, the agent trades more quickly and hence has a large temporary impact compared with the other paths.

Finally, in Figure 7.3, we show heat-maps of the agent's inventory (left panel) and trading speed (right panel) resulting from 1,000 simulations. We see a thin contribution to the heat-map along an inventory level of 1 as well as along a trading speed of  $0$ . These represent those paths that breached the price limit early. We also show the mean inventory path and the mean trading speed trajectory. As expected, the mean inventory path lies above the AC strategy, since the trading speed for the same level of inventory must lie above the AC strategy as dictated by the maximum principle and encoded in the inequality  $(7.7)$ .

Inequality  $(7.7)$ , does not, however, imply that the trading speed will always lie below the AC trading speed. This is because the inventory level varies with the sample path and will not generally equal that of the AC inventory. Indeed, as the right panel of Figure 7.3 shows, the mean trading speed starts above that of the AC, but as time passes, it eventually falls below it. The intuition for this is that since the optimal strategy requires the agent to trade more quickly than the AC, her inventory is generally higher (and closer to the target inventory) than if she were trading according to the AC strategy. Since she eventually has less inventory, her trading speed generally slows down which results in the behaviour observed in the figure.

#### 7.3 Incorporating Order Flow

In the previous chapter and in the last section, we assume that in the absence of the agent's trades, the midprice process is a martingale. We also assume that when the agent begins to liquidate (acquire) shares, her actions induce

a downward (upward) drift in the midprice process. In other words, the act of her selling (buying) shares induces the market as a whole to adjust prices downwards (upwards). Yet at the same time we are ignoring the trades of other market participants, implicitly assuming that on average their actions even out to yield a net of zero drift. This may be acceptable at an aggregate level, but over short time horizons, there may be order flow imbalance, which very often results in prices trending upwards or downwards over short intervals in time. In this section, we show how to incorporate the order flow from the remainder of the market into the midprice dynamics and how the agent modifies her strategy to adapt to it locally.

### The Model Setup

In addition to the usual state variables and stochastic processes introduced in the previous chapter, we now also model the dynamics of the buy and sell rate of order flow *µt* and assume that they satisfy the SDE

$$d\mu_t^{\pm} = -\kappa \,\mu_t^{\pm} \,dt + \eta \,dL_t^{\pm} \,,\tag{7.13}$$

where *Lt* are independent Poisson processes (assumed independent of all other processes as well) with equal intensity A. This assumption implies that the buy and sell order flows arrive independently at Poisson times with rate A, and induce an increase in the order flow rate by T/ and jumps in order flow rate decay at the speed "'·

Next, we incorporate the order flow in the midprice process S<sup>t</sup> , which now satisfies the SDE

$$dS_t^{\nu} = \sigma \, dW_t + (g(\mu_t^+) - g(\mu_t^- + \nu_t)) \, dt \, ,$$

where Wt is a Brownian motion independent of the Poisson processes and g is an impact function which dictates how the mid price drift is affected by buy/ sell order flow. In this manner, the action of the agent's trades and other traders' actions are treated symmetrically. vVe can define the net order flow µt = µi -µ;, and a short computation shows that

$$d\mu_t = -\kappa \left(\mu_t^+ - \mu_t^-\right) dt + \eta \left(dL_t^+ - dL_t^-\right)$$
  
=  $-\kappa \mu_t dt + \eta \left(dL_t^+ - dL_t^-\right)$ .

Hence, if the permanent impact functions g(x) = bx are linear (with b � 0), we can use the net order flow as a state process rather than having to keep track of order flow in both directions separately. Overall, we have

$$dS_t^{\nu} = \sigma \, dW_t + b \left(\mu_t - \nu_t\right) dt \, .$$

The remainder of the agent's optimisation problem is as in Section 6.5. Briefly, the agent's inventory Q <sup>v</sup>is

$$dQ_t^{\nu} = -\nu_t \, dt \,,$$

and her cash process *x<sup>v</sup>*satisfies the SDE

$$dX_t^{\nu} = (S_t^{\nu} - k \nu_t) \nu_t dt,$$

where k > 0 is the temporary linear impact parameter. Also, the agent's performance is the usual one so

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,x,S,\mu,q} \left[ X_T^{\nu} + Q_T^{\nu} \left( S_T^{\nu} - \alpha Q_T^{\nu} \right) - \phi \int_t^T (Q_u^{\nu})^2 \ du \right], \quad (7.14)$$

and her value function is

$$H(t, x, S, \mu, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, \mu, q) \, .$$

### The Resulting DPE

The DPP for the value function suggests that the value function *H(t, x, S,* µ, *q)*  satisfies the DPE (the value function now has an additional state variable,µ)

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)H + \mathcal{L}^{\mu}H - \phi \,q^2$$
  
+ 
$$\sup_{\nu} \left\{ \left(\nu \left(S - k\,\nu\right)\partial_x + b\left(\mu - \nu\right)\partial_S - \nu\,\partial_q\right)H\right\},\right\}$$

subject to the terminal condition

$$H(T, x, S, \mu, q) = x + q S - \alpha q^{2},$$

where the infinitesimal generator for the net order flow acts on the value function as follows:

$$\mathcal{L}^{\mu}H(t,x,S,\mu,q) = -\kappa \,\mu \,\partial_{\mu}H + \lambda \left[ H(t,x,S,\mu+\eta,q) - H(t,x,S,\mu,q) \right]$$
  
+  $\lambda \left[ H(t,x,S,\mu-\eta,q) - H(t,x,S,\mu,q) \right]$ .  
(7.15)

Inserting the ansatz

$$H(t,x,S,\mu,q) = x + q\,S + h(t,\mu,q)\,, \label{eq:hamiltonian}$$

we see that the excess book value function *h(t, µ, q)* satisfies the equation

$$\partial_t h + \mathcal{L}^{\mu} h + b \mu q - \phi q^2 + \sup_{\nu} \left\{ -k \nu^2 - (b q + \partial_q h) \nu \right\} = 0,$$

subject to the terminal condition *h(T, µ, q)* = *-a q 2 .* Recall that *x* + *q S* represents the cash from the sale of shares so far plus the book value ( at mid price) of the shares the agent still holds and aims to liquidate.

The optimal control in feedback form is the same as in **(6.22),** but the function *h* satisfies a new equation, More specifically, the first order conditions imply that

$$\nu^* = -\frac{1}{2k} \left( b \, q + \partial_q h \right) \,,$$

and upon substitution back into the previous equation we find that h satisfies the non-linear partial-integral differential equation (PIDE)

$$(\partial_t + \mathcal{L}^{\mu}) h + b \mu q - \phi q^2 + \frac{1}{4k} (b q + \partial_q h)^2 = 0. \tag{7.16}$$

### Solving the DPE

Due to the existence of linear and quadratic terms in  $q$  in  $(7.16)$ , and its terminal conditions, we expect  $h(t,\mu,q)$  to be a quadratic form in q, and we assume the  $ansatz$ 

$$h(t,\mu,q) = h_0(t,\mu) + q h_1(t,\mu) + q^2 h_2(t,\mu).$$

Inserting this into  $(7.16)$  and collecting like terms in q leads to the following coupled system of PIDEs:

$$(\partial_t + \mathcal{L}^{\mu}) h_0 + \frac{1}{4k} h_1^2 = 0, \qquad (7.17a)$$

$$(\partial_t + \mathcal{L}^{\mu}) h_1 + b \mu + \frac{1}{2k} h_1 (b + 2h_2) = 0, \qquad (7.17b)$$

$$(\partial_t + \mathcal{L}^{\mu}) h_2 - \phi + \frac{1}{4k} (b + 2h_2)^2 = 0, \qquad (7.17c)$$

subject to the terminal conditions

$$h_0(T,\mu) = 0, \quad h_1(T,\mu) = 0, \quad h_2(T,\mu) = -\alpha.$$

Note that since (7.17c) for  $h_2$  contains no source terms in  $\mu$  and its terminal condition is independent of  $\mu$ , the solution must be independent of  $\mu$ , i.e.  $h_2$  is a function only of time. In this case,  $(7.17c)$  reduces to  $(6.25)$  – the equation for  $h_2(t)$  in the AC problem. Thus

$$h_2(t,\mu) = \chi(t) - \frac{1}{2}b$$
, where  $\chi(t) = \sqrt{k\phi} \frac{1+\zeta e^{2\gamma(T-t)}}{1-\zeta e^{2\gamma(T-t)}}$ ,

with the constants  $\gamma$  and  $\zeta$  as defined in (6.26), but repeated here for convenience:

$$\gamma = \sqrt{\frac{\phi}{k}}, \quad \text{and} \quad \zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{k\,\phi}}{\alpha - \frac{1}{2}b - \sqrt{k\,\phi}}.$$

Next, to solve for  $h_1$  in (7.17b), we exploit the affine structure of the model for the net order flow and write

$$h_1(t,\mu) = \ell_0(t) + \mu \,\ell_1(t) \,,$$

in which case,

$$\mathcal{L}^{\mu} h_1 = -\kappa \,\mu \,\ell_1 + \lambda (\eta \,\ell_1) + \lambda (-\eta \,\ell_1) = -\kappa \,\mu \,\ell_1 \,,$$

with terminal conditions  $\ell_0(T) = \ell_1(T) = 0$ . Therefore, (7.17b) reduces to

$$\left\{\partial_t \ell_0 + \frac{1}{k}\,\chi(t)\,\ell_0\right\} + \left\{\partial_t \ell_1 + \left(\frac{1}{k}\,\chi(t) - \kappa\right)\,\ell_1 + b\right\}\,\mu = 0\,.$$

Since this must hold for every value of  $\mu$ , each term in the braces must vanish individually and we obtain two simple ODEs for  $\ell_0$  and  $\ell_1$ . Since  $\ell_0(T) = 0$  and

its ODE is linear in  $\ell_0$ , the solution is  $\ell_0(t) = 0$ . For  $\ell_1$ , due to the source term  $b$ , the solution is non-trivial and can be written as

$$\ell_1(t) = b \int_t^T e^{-\kappa(s-t)} e^{\frac{1}{k} \int_t^s \chi(u) \, du} \, ds \,. \tag{7.18}$$

As in  $(6.29)$ , we use the integral

$$\int_0^t \frac{\chi(s)}{k} ds = \log \frac{\zeta e^{\gamma(T-t)} - e^{-\gamma(T-t)}}{\zeta e^{\gamma T} - e^{-\gamma T}}$$

to simplify the expression for  $\ell_1$  to

$$\ell_1(t) = b \,\bar{\ell}_1(T - t) \ge 0\,,\tag{7.19}$$

where

$$\bar{\ell}_1(\tau) = \frac{1}{\zeta \, e^{\gamma \tau} - e^{-\gamma \tau}} \left\{ e^{\gamma \tau} \frac{1 - e^{-(\kappa + \gamma)\tau}}{\kappa + \gamma} \, \zeta - e^{-\gamma \tau} \frac{1 - e^{-(\kappa - \gamma)\tau}}{\kappa - \gamma} \right\} \, ,$$

and  $\tau = T - t$  represents the time remaining to the end of the trading horizon.

The solution of  $h_0$ , which satisfies (7.17a), can be obtained in a similar manner, but the optimal speed of trading does not depend on  $h_0$  since as we showed earlier,  $\nu^* = -(bq + \partial_q h)/2k$ , and  $\partial_q h(t,\mu) = h_1(t,\mu) + 2q h_2(t,\mu)$ . Putting these results together we find that the optimal speed of trading is

$$\nu_t^* = -\frac{1}{k} \chi(t) Q_t^{\nu^*} - \frac{b}{2k} \bar{\ell}_1(t) \mu_t. \n$$
(7.20)

The optimal trading speed above differs from the AC solution by the second term on the right-hand side of  $(7.20)$  which represents the perturbations to the trading speed due to excess order flow. Recall that in the limit  $\alpha \to \infty$ ,  $\chi \leq 0$ , and from the explicit equation above  $\bar{\ell}_1 \geq 0$ , hence, when the excess order flow is tilted to the buy side  $(\mu_t > 0)$ , the agent slows down trading since she anticipates that excess buy order flow will push the prices upwards - and therefore will receive better prices when she eventually speeds up trading to sell assets later on. Contrastingly, she increases her trading speed when order flow is tilted to the sell side ( $\mu_t < 0$ ), since other traders are pushing the price downwards and she aims to get better prices now, rather than waiting for other traders to push it further down. Another interpretation is that she attempts to hide her orders by trading when order flow moves in her direction. Finally, recall that  $\ell_1(t) \xrightarrow{t \to T} 0$ , hence, the order flow influences the agent's trading speed less and less as maturity approaches because there is little time left to take advantage of directional trends in the midprice.

Somewhat surprisingly, the volatility of the order flow process  $\eta$  does not appear explicitly in the optimal strategy. It does, however, affect the way the agent trades through its influence on the path which order flow takes. When the order flow path is volatile, the optimal trading speed will be volatile as well. It is also interesting to observe that if the jumps  $\eta$  in the order flow at the Poisson times were random and not constant, the resulting strategy would be identical, see Exercise  $E.7.1$ . Similarly, if we add a Brownian component to the order flow process  $\mu_t$ , the resulting optimal strategy in terms of  $\mu_t$  would be identical, i.e.  $(7.20)$  remains true. Naturally, the actual path taken by the order flow, and therefore also that of trading, would be altered by these modifications to the  $model.$ 

A final point we make about this optimal trading strategy is that  $\nu_t$  is not necessarily strictly positive. If the order flow  $\mu_t$  is sufficiently positive, then the agent may be willing to purchase the asset to make gains from the increase in asset price (i.e. her liquidation rate becomes negative). This is because the way we have introduced order flow into the model generates predictability in the price process which can be exploited, even if the agent is not executing a trade. In fact, if the agent has liquidated the target  $\mathfrak{N}$  at  $t < T$  the optimal strategy is not to stop, but to continue trading and exploit the effect of the order flow, and we see this as her inventory can become negative at intermediate times. If there is sufficient selling pressure (i.e.  $\mu_t$  is sufficiently negative), then by shorting the asset, she may benefit from the downward price movement.

One approach to avoid such scenarios is to simply restrict the trading strategy in a naive manner, by setting

$$\nu^{\dagger} = \max\left(-\frac{1}{k}\,\chi(t)\,Q_t^{\nu^{\dagger}} - \frac{b}{2\,k}\,\bar{\ell}_t(t)\,\mu_t\;;\;0\right)\,\mathbbm{1}_{\left\{Q_t^{\nu^{\dagger}}>0\right\}}\,. \tag{7.21}$$

In other words, we can follow the unrestricted optimal solution whenever the trading rate is positive and the agent has positive inventory, otherwise we impose a trading stop. This trading strategy,  $\nu^{\dagger}$ , is not the true optimal strategy. To obtain the true optimal strategy we would need to go back to the DPE and impose the constraint  $\nu \geq 0$  in the supremum and add an additional boundary condition along  $q = 0$ . In this case, the DPE will not have an analytical solution, although numerical schemes can be used to solve the problem. Nonetheless, the  $\nu^{\dagger}$  strategy provides a reasonable approximation that is easy to implement.

### Simulations of the Strategy with Order Flow

In this section we perform simulations to show the behaviour of the optimal strategy in this model. Throughout, we use the following parameters:

$$T = 1 \text{ day}, \quad k = 10^{-3}, \quad b = 10^{-4}, \quad \phi = 0.01,$$
  
 $\lambda = 1000, \quad \kappa = 10, \quad \eta \sim Exp(5), \quad \sigma = 0.1,$ 

where  $\eta \sim Exp(\eta_0)$  denotes the exponential distribution with mean size  $\mathbb{E}[\eta]$  $\eta_0$ .

Figure 7.4 shows three scenarios of the midprice, the order flow, the optimal inventory, and the optimal speed of trading when the agent uses the augmented strategy  $\nu^{\dagger}$  in (7.21). As the figure shows, when the order flow is positive/negative the agent trades more slowly/quickly than the AC trading speed. For example,

![](_page_15_Figure_1.jpeg)

Figure 7.4 Optimal trading in the presence of order flow. The dashed lines show the  $\text{classical} \text{AC solution.}$ 

the large order flow in the buy direction ( $\mu_t > 0$ ), shown by the green path, causes the agent to trade more slowly in the initial stages of the trade. As the end of the trading horizon approaches, the order flow influences her strategy less, but she must speed up her trading since there is little time remaining in which to liquidate the remaining shares. The red path has order flow that fluctuates mostly around zero, and as shown in the diagrams, she follows closely the AC strategy, but locally adjusts her trades relative to the path. Finally, the blue path has a bias towards sell order flow, and the agent adds to this flow by trading more quickly throughout most of the trading horizon and eventually liquidates her shares early.

To gain further insight into the strategy, Figure 7.5 shows heat-maps from  $5,000$  scenarios of the optimal inventory to hold and the optimal speed of trading. Panel (a) shows the results when  $\eta \sim Exp(5)$  as in Figure 7.4, while panel (b) shows the results when  $\eta \sim Exp(10)$ . As expected, the optimal trading strategy in scenario (b) is more volatile than in scenario (a), despite the optimal strategy (as seen in  $(7.21)$ ) having no explicit dependence on this volatility.

![](_page_16_Figure_1.jpeg)

Figure 7.5 Heat-maps of the optimal trading in the presence of order flow for two volatility levels. The dashed lines show the classical AC solution.

#### 7.3.1 Probabilistic Interpretation

Above we studied a particular choice of the dynamics of other market participants' rate of trading  $\mu_t$ . Here we provide a general solution where we do not assume a particular model for  $\mu$ , all we specify is the generator  $\mathcal{L}^{\mu}$ , which nests  $(7.15)$  as a particular case. In this general setup the solution to the problem is very similar to that derived above. We need to solve the system of coupled PIDEs in (7.17) and in particular we must solve for  $h_1$  which satisfies equation  $(7.17b)$ , which we repeat here for convenience:

$$(\partial_t + \mathcal{L}^{\mu}) h_1 + b \mu + \frac{1}{2k} h_1 (b + 2h_2) = 0, \qquad h_1(T) = 0,$$

where

$$h_2(t,\mu) = \sqrt{k\,\phi} \, \frac{1+\zeta\,e^{2\gamma(T-t)}}{1-\zeta\,e^{2\gamma(T-t)}} - \frac{1}{2}\,b\,.$$

This is a linear PIDE for  $h_1$  in which  $h_2 + \frac{1}{2}b$  acts as an effective discount rate and  $b\mu$  is a source term. The general solution of such an equation can be represented using the Feynman-Kac Theorem. Thus we write

$$h_1(t,\mu) = b \mathbb{E}_{t,\mu} \left[ \int_t^T \exp\left\{ \frac{1}{k} \int_t^u \left( h_2(s) + \frac{1}{2}b \right) ds \right\} \mu_u du \right]$$

and using  $(6.28)$  to simplify the exponential term, we obtain

$$h_1(t,\mu) = b \mathbb{E}_{t,\mu} \left[ \int_t^T \left( \frac{e^{-\gamma(T-u)} - \zeta e^{\gamma(T-u)}}{e^{-\gamma(T-t)} - \zeta e^{\gamma(T-t)}} \right) \mu_u \, du \right] \,. \tag{7.22}$$

Recall that the optimal speed of trading is given by

$$\nu^* = -\frac{1}{2k} \left( b q + \partial_q h \right) \,,$$

with

$$h(t,\mu,q) = h_0(t,\mu) + q h_1(t,\mu) + q^2 h_2(t,\mu).$$

Hence, we have

$$\nu_t^* = \gamma \frac{\zeta e^{2\gamma(T-t)} + 1}{\zeta e^{2\gamma(T-t)} - 1} Q_t^{\nu^*} - \frac{b}{2k} \int_t^T \frac{\zeta e^{\gamma(T-u)} - e^{-\gamma(T-u)}}{\zeta e^{\gamma(T-t)} - e^{-\gamma(T-t)}} \mathbb{E} \left[ \mu_u \mid \mathcal{F}_t^{\mu} \right] du. \n$$
(7.23)

In the limit in which the terminal penalty becomes infinite  $(\alpha \rightarrow \infty)$ , so that the agent must completely liquidate her position by the end of the trading horizon, we have  $\zeta \to 1$ , and the optimal trading speed simplifies to

$$\lim_{\alpha \to \infty} \nu_t^* = \gamma \frac{\cosh(\gamma (T - t))}{\sinh(\gamma (T - t))} Q_t^{\nu^*} - \frac{b}{2k} \int_t^T \frac{\sinh(\gamma (T - u))}{\sinh(\gamma (T - t))} \mathbb{E} \left[ \mu_u \, | \, \mathcal{F}_t^{\mu} \right] \, du \, .$$

The first term corresponds to the classical AC solution, while the second corrects the liquidation speed based on the weighted average of the future expected net order flow. If this weighted average future order flow is positive (which would occur, e.g., if the current order flow is positive and hence biased towards buying), then the agent slows down to take advantage of the upward trend in prices that the excess positive order flow will have. The opposite holds if order flow is negative. This dependence on order flow becomes less important as maturity approaches, and the agent instead focuses on completing her execution.

### 7.4 Optimal Liquidation in Lit and Dark Markets

Up until now, the agent has been trading on transparent (lit) markets, where all agents can observe quantities being offered for sale or purchase at different prices, that is, the LOB is visible to all interested parties. We now consider the possibility that the agent can also trade in what are known as **dark pools**. Dark

pools are trading venues which, in contrast to traditional ( or lit) exchanges, do not display bid and ask quotes to their clients. Trading may occur continuously, as soon as orders are matched, or consolidated and cleared periodically (sometimes referred to as throttling). We focus on a particular kind of dark pool known as a *crossing network* defined by the Securities Exchange Commission (SEC) as (see also Section 3.6)

> *" ... systems that allow participants to enter unpriced orders to buy and sell securities, these orders are crossed at a specified time at a price derived from another market ...* "

Typically, the price at which transactions are crossed is the midprice in a corresponding lit trading venue. When a trader places an order in a dark pool, she may have to wait for some time until a matching order arrives so that her order is executed. Thus, on the one hand the trader who sends orders to the dark pool is exposed to execution risk, but on the other hand does not receive the additional temporary price impact of walking the LOB.

Here we analyse the case when the agent trades continuously in the lit market and simultaneously posts orders in the dark pool with the aim to liquidate SJ1 shares.

### Model Setup

On the lit market, we assume, as before, that the agent is exposed to a temporary market impact from her market orders so when trading Vtdt in the lit market, she receives St = St - k Vt per share, with k > 0, where the midprice St is a Brownian motion. In addition to trading in the lit market, the agent posts Yt :::; qt units of inventory in the dark pool, where qt \_.:; SJ1 are the remaining shares to be liquidated, and she may continuously adjust this posted order. Matching orders in the dark have no price impact because they are pegged to the lit market's midprice, so the agent receives St per share for each unit executed in the dark pool which is not necessarily the whole amount Yt·

Furthermore, other market participants send matching orders to the dark pool which are assumed to arrive at Poisson times and the volumes associated with the orders are independent. More specifically, let *Nt* denote a Poisson process with intensity .X and let { *�j* : *j* = 1, 2, ... } be a collection of independent and identically distributed random variables corresponding to the volume of the various matching orders which are sent by other market participants into the dark pool. The total volume of buy orders (which may match the agent's posted sell order) placed in the dark pool up to time *t* is the compound Poisson process

$$V_t = \sum_{n=1}^{N_t} \xi_n.$$

When a matching order arrives, it may be larger or smaller than the agent's

posted sell order, hence the agent's inventory (accounting for both the continuous trading in the lit market and her post in the dark pool) satisfies the SDE

$$dQ_t^{\nu,y} = -\nu_t \, dt - \min\left(y_t, \, \xi_{1+N_{t-}}\right) \, dN_t \,,$$

and recall that the agent's aim is to liquidate  $\mathfrak{N}$  shares on or before the terminal date  $T$ . In the equation above the first term on the right-hand side represents the shares that the agent liquidates using MOs in the lit market and the second represents the orders she sends to the dark pool.

We assume that the agent is at the front of the sell queue in the dark pool, so that she is first to execute against any new orders coming into that market. The model can be modified to account for the agent not being at the front. This can be done by introducing another random variable representing the volume of orders in front of the agent. This, however, complicates but does not alter the approach in a fundamental way, so we leave the interested reader to try this, see Exercise  $E.7.2$ .

Hence, the agent's cash process  $X_t^{\nu,y}$  satisfies the SDE

$$dX_t^{\nu,y} = (S_t - k \,\nu_t) \,\nu_t \,dt + S_t \,\min\left(y_t, \,\xi_{1+N_{t^-}}\right) \,dN_t \,.$$

Her performance criteria is, as usual, given by

$$H^{\nu,y}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X_{\tau} + Q_{\tau}^{\nu,y} \left( S_{\tau} - \alpha \, Q_{\tau}^{\nu,y} \right) - \phi \int_{t}^{\tau} \left( Q_{u}^{\nu,y} \right)^{2} \, du \right] \, ,$$

where  $\mathbb{E}_{t,x,S,q}[\cdot]$  denotes expectation conditional on  $X_{t^-} = x, S_t = S, Q_{t^-} = q,$ and the stopping time

$$\tau = T \wedge \inf\{t : Q_t = 0\},\$$

represents the time until the agent's inventory is completely liquidated, or the terminal time has arrived. The value function is

$$H(t,x,S,q) = \sup_{\nu,y\in\mathcal{A}} H^{\nu,y}(t,x,S,q) \,,$$

where the set of admissible strategies consists of  $\mathcal{F}$ -predictable processes bounded from above, and her posted volume in the dark pool is at most her remaining inventory, i.e.  $y_t \leq Q_t^{\nu,y}$ .

# The Resulting DPE

Applying the DPP shows that the value function should satisfy the DPE

$$\begin{split} \partial_t H &+ \tfrac{1}{2} \sigma^2 \partial_{SS} H - \phi \, q^2 \\ &+ \sup_{\nu} \left\{ (S - k \, \nu) \, \nu \, \partial_x H - \nu \, \partial_q H \right\} \\ &+ \sup_{y \le q} \left\{ \lambda \, \mathbb{E} \left[ H \left( t, x + S \, \min(y, \xi), \, S, \, q - \min(y, \xi) \right) - H \right] \right\} = 0 \,, \end{split}$$

subject to the terminal condition

$$H(T, x, S, q) = x + q(S - \alpha q).$$

In the above, the expectation represents an expectation over the random variable  $\xi$  and the various terms in the DPE carry the following interpretations:

- the term  $\partial_{SS}$  represents the diffusion of the midprice,
- the  $-\phi q^2$  term represents the running penalty which penalises inventories different from zero,
- the  $\sup_{\nu} \{\cdot\}$  term represents optimising over continuous trading in the lit market.
- the  $\sup_{y \leq q}$  term represents optimising over the volume posted in the dark pool, and the expectation is there to account for the fact that buy volume coming into the dark pool from other traders is random.

The terminal condition once again suggests the ansatz  $H(t, x, S, q) = x + qS +$  $h(t,q)$ . Recall that  $x + qS$  represents the cash from sales so far, in both lit and dark markets, plus the book value (at midprice) of the shares the agent still holds and aims to liquidate. Hence,  $h$  represents the value of optimally trading beyond the book value of cash and assets. The DPE then reduces to a simpler equation for  $h$ :

$$\partial_t h - \phi q^2 + \sup_{\nu} \left\{-k\,\nu^2 - \nu\,\partial_q h\right\}$$
  
+  $\lambda \sup_{y \le q} \mathbb{E}\left[h\left(t, q - \min(y, \xi)\right) - h(t, q)\right] = 0\,,\tag{7.24}$ 

subject to the terminal condition  $h(T,q) = -\alpha q^2$ . Next, the first order condition for  $\nu$  implies that the optimal speed to trade in feedback control form is

$$\nu^* = -\frac{1}{2k} \partial_q h \,, \tag{7.25}$$

 $SO$ 

$$\sup_{\nu} \left\{-k\,\nu^2 - \nu\,\partial_q h\right\} = \frac{1}{4k} \left(\partial_q h\right)^2 \,.$$

To determine the optimal over  $y$  (i.e. the optimal volume to post in the dark pool), we need to either resort to numerics or place more structure on the random variable  $\xi$ .

#### $7.4.1$ Explicit Solution when Dark Pool Executes in Full

To obtain an explicit solution to the problem we assume that the agent's desired execution (the liquidation order) is small relative to the volume coming into the dark pool,  $\xi_i \geq \mathfrak{N}$  (for all  $i = 1, 2, \ldots$ ). This assumption ensures that when a matching buy order arrives in the dark pool, the agent's order is executed in full, as the incoming buy order is larger than the amount posted in the agent's sell order – the agent's inventory at any point in time is at most  $\mathfrak{N}$  (the initial amount she must liquidate). As the agent's posts are always filled entirely, in  $(7.24) \min(\xi_1, y) = y.$ 

We hypothesise that the ansatz is a polynomial in  $q$ . Before proposing the

ansatz, note that the DPE contains an explicit  $q^2$  penalty, the optimum over  $\nu$ is quadratic in  $\partial_q h$ , and the terminal condition is  $-\alpha q^2$ . Thus this suggests the following ansatz for  $h(t,q)$ :

$$h(t,q) = h_0(t) + h_1(t) q + h_2(t) q^2,$$

with terminal conditions  $h_0(T) = h_1(T) = 0$  and  $h_2(T) = -\alpha$ . The supremum over  $y$  becomes

$$\begin{split} \sup_{y \le q} \mathbb{E} \left[ h \left( t, q - \min(y, \xi) \right) - h(t, q) \right] \\ &= \sup_{y \le q} \left[ h \left( t, q - y \right) - h(t, q) \right] \\ &= \sup_{y \le q} \left[ -y \, h_1 + \left( y^2 - 2 \, q \, y \right) h_2 \right] \\ &= -\frac{1}{4 \, h_2} \left( h_1 - 2 \, q \, h_2 \right)^2 \,, \end{split}$$

and the optimal dark pool volume in feedback form is

$$y^* = q + \frac{1}{2} \frac{h_1}{h_2} \, .$$

From the terminal condition,  $h_2(t) < 0$ . It remains to be seen that  $h_1(t) \ge 0$  so that indeed  $y^* \leq q$  and the admissibility criteria are satisfied.

Furthermore, the optimal speed of trading, in feedback form, simplifies to

$$\nu^* = -\frac{1}{2k} \left( h_1 + 2q \, h_2 \right) \, .$$

Notice that both  $y^*$  and  $\nu^*$  are independent of  $h_0$ , so while  $h_0$  is important in determining the value function, it is irrelevant for obtaining the optimal strategy.

Inserting the above feedback controls into the DPE  $(7.24)$ , collecting terms in powers of  $q$ , and setting each to zero, leads to the coupled system of ODEs

$$\partial_t h_2 - \phi - \lambda h_2 + \frac{1}{k} h_2^2 = 0, \qquad (7.26a)$$

$$\partial_t h_1 + \left(\lambda + \frac{1}{k} h_2\right) h_1 = 0,$$
 (7.26b)

$$\partial_t h_0 + \frac{1}{k} h_1^2 - \frac{\lambda}{4} \frac{h_1^2}{h_2} = 0. \qquad (7.26c)$$

Since  $h_1$  vanishes at T and its ODE in (7.26b) is linear in  $h_1$ , the solution is  $h_1(t) = 0$  and it is also trivial to see that  $h_0(t) = 0$ . If there was a drift in the midprice, these terms would not vanish, see Exercise E.7.3. Then, overall, we are left with only the  $h_2$  equation, which is modified somewhat from the no dark pool case ((6.25) with  $b = 0$ ) by the term  $-\lambda h_2$ . This term represents a "leakage" of inventory resulting from the possibility that the order posted in the dark pool is fully executed. Clearly, we see that if there is no dark pool, that is  $\lambda = 0$ , the problem reduces to that of optimal liquidation already discussed above in Chapter 6. For instance, see that for  $\lambda = 0$ , ODE (7.26a) is the same as  $(6.25)$  and both have the same boundary condition.

The equation for  $h_2$  is of Riccati type and can be solved explicitly. Let  $\zeta^{\pm}$ denote the roots of the polynomial  $\phi + \lambda p - \frac{1}{k} p^2 = 0$ , then write (7.26a) as

$$\partial_t h_2 = -\frac{1}{k} \left( h_2 - \zeta^+ \right) \left( h_2 - \zeta^- \right),$$

where

$$\zeta^{\pm} = \frac{1}{2}k\,\lambda \pm \sqrt{\frac{1}{4}k^2\,\lambda^2 + k\phi} \,.$$

Cross multiplying and writing as partial fractions, we have

$$\partial_t h_2 \left( \frac{1}{h_2 - \zeta^+} - \frac{1}{h_2 - \zeta^-} \right) = -\frac{1}{k} \left( \zeta^+ - \zeta^- \right),$$

and integrating from  $t$  to  $T$  leads to

$$\log\left(\frac{h_2-\zeta^-}{h_2-\zeta^+}\right) - \log\left(\frac{\alpha+\zeta^-}{\alpha+\zeta^+}\right) = -\frac{1}{k}\left(\zeta^+ - \zeta^-\right)(T-t)\,,$$

where we have used the terminal condition  $h_2(T) = -\alpha$ . Re-arranging the equation, we finally obtain

$$h_2(t) = \frac{\zeta^- - \zeta^+ \,\beta \, e^{-\gamma(T-t)}}{1 - \beta \, e^{-\gamma(T-t)}} \,,$$

where the constants are

$$\beta = \frac{\alpha + \zeta^-}{\alpha + \zeta^+} \quad \text{and} \quad \gamma = \frac{1}{k} (\zeta^+ - \zeta^-) \,.$$

Therefore, the optimal trading strategy is

$$\nu_t^* = -\frac{1}{k} h_2(t) Q_t^{\nu^*, y^*} \quad \text{and} \quad y_t^* = Q_t^{\nu^*, y^*}.\n$$
(7.27)

As before, we can obtain the optimal inventory to hold, up to the arrival of matching order in the dark pool, by solving

$$dQ_t^{\nu^*,y^*} = -\nu_t^* dt = \frac{1}{k} h_2(t) Q_t^{\nu^*,y^*} dt,$$

so that

$$Q_t^{\nu^*,y^*} = Q_0 \exp\left\{\frac{1}{k} \int_t^T h_2(u) \, du\right\} \, .$$

and therefore by direct integration

$$Q_t^{\nu^*,y^*} = e^{(\zeta^-/k)t} \left(\frac{1-\beta \, e^{-\gamma(T-t)}}{1-\beta \, e^{-\gamma T}}\right) \mathfrak{N}. \tag{7.28}$$

In the limit in which the terminal penalty  $\alpha$  is very large, i.e.  $\alpha \to \infty$  (so that the agent guarantees full execution by the end of the trading horizon),  $\beta \rightarrow 1$ and hence,

$$Q_t^{\nu^*,y^*} \xrightarrow{\alpha \to \infty} e^{\left(\frac{\zeta^-}{k} + \frac{\gamma}{2}\right)t} \frac{\sinh\left(\frac{\gamma}{2}(T-t)\right)}{\sinh\left(\frac{\gamma}{2}T\right)} \mathfrak{N}.$$

Furthermore, in the limit ,\--+ 0, (---+ *-vfc{>* and 1--+ 2J¢lk and thus

$$Q_t^{\nu^*,y^*} \xrightarrow{(\alpha,\lambda) \to (\infty,0)} \frac{\sinh\left(\sqrt{\frac{\phi}{k}}\left(T-t\right)\right)}{\sinh\left(\sqrt{\frac{\phi}{k}}\,T\right)} \mathfrak{N},$$

which recovers the results from the *AC* case without the dark pool.

# Liquidation Strategy with Dark Pool

It is clear that the optimal amount to send to the dark pool is always what remains to be liquidated. This makes sense because in our model there is no market impact in the dark pool so the agent obtains the midprice for orders that are crossed in the dark pool. The more interesting part of the liquidation strategy is how much the agent should send to the lit markets now that she has access to a dark pool. To answer this question it is useful to compare the lit market liquidation rate v\* in (7.27) with the optimal liquidation strategy when there is no dark pool, i.e. ,\ = 0. Recall that when ,\ = 0 the optimal speed of trading in the lit market is that given by the AC solution, see for instance (6.27) with *b* = 0 or simply use (7.27) with ,\ = 0. It is not immediately clear whether the modified rate at which the agent is trading in the lit market is larger or smaller than the liquidation rate when the agent does not have access to a dark pool. Also, it is not clear whether the trading rate is decreasing as in the *AC* case.

In Figure 7.6 we plot the optimal liquidation rate in the lit market given in (7.27) for different levels of the rate of arrival of matching orders in the dark pool. The figure shows that the trading rate may be larger or smaller than the *AC* case, and it may be increasing or decreasing. Also, the optimal inventory to hold ( up to the time at which a matching order arrives) may be either convex or concave or neither.

In particular, the top two panels of Figure 7.6 show the optimal inventory path and optimal speed of trading where we also assume that the liquidation penalty at time *T* is a --+ oo and the paths shown are prior to the order posted in the dark pool being executed. Other model parameters are k = 0.001 and</>= 0.01.

The bottom two panels of the figure show the case where the order in the dark pool was executed at time t = 0.6 and the agent's inventory drops to zero. Since the execution of the orders in the dark pool occur according to a Poisson process with intensity ..\, the time at which this occurs is exponentially distributed with mean 1/ ,\. Thus, when ,\ = 0 there are no executions in the dark pool and the liquidation strategy corresponds to the AC solution. When ,\ > 0 the agent starts trading slower than the *AC* speed in the lit market, to allow for the potential of dark pool execution, but then as time runs out and no execution occurs, her rate of trading increases to compensate for the initially slow trading. Interestingly, the optimal trading curve ceases to be convex, and its convexity changes signs. In the limiting case when ,\ --+ oo, the agent does not trade at all in the lit

market, since execution in the dark pool is guaranteed. In this case, the optimal inventory path flows along  $Q_t^* = \mathfrak{N} \mathbb{1}_{t < T}$ , but is then infinitely fast at T to rid herself of the assets.

![](_page_24_Figure_2.jpeg)

Figure 7.6 The top panels show optimal inventory path and speed of trading prior to a matching order in the dark pool. The bottom panels show the optimal inventory and trading speed where we assume that the dark pool matching order arrives at  $t = 0.6$ , right after which inventory drops to zero.

### 7.5 Bibliography and Selected Readings

Laruelle, Lehalle & Pagès (2011), Buti, Rindi & Werner (2011b), Buti, Rindi & Werner (2011a), Crisafi & Macrina (2014), Iyer, Johari & Moallemi (2014), Moallemi, Saglam & Sotiropoulos (2014), Bechler & Ludkovski (2014), Cartea & Jaimungal  $(2014b)$ .

#### 7.6 Exercises

E.7.1 Use the same setup as in Section 7.3 but allow for  $\eta$  to be random so that

$$d\mu_t^{\pm} = -\kappa \,\mu_t^{\pm} \,dt + \eta \,dL_t^{\pm} \,,\tag{7.29}$$

where 7/ are i.i.d. with finite first moment. Find the optimal speed of liquidation and compare this result to (7.20).

- E.7.2 Assume the setup in Section 7.4. Instead of the agent's orders always being at the front of the queue in the dark pool, assume that ahead of her order there are other market participants' orders which have priority. Model this volume as a random variable and derive the optimal speed of trading in the lit market and the number of shares that the agent sends to the dark pool.
- E.7.3 The setup is as in section 7.4.1 and let the midprice satisfy

$$dS_t = \mu dt + \sigma dW_t \,,$$

where µ is constant. Derive the DPE and propose an ansatz to specify the optimal speed of trading. Compare your results to the case where µ = 0.
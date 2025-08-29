# 5 Stochastic Optimal Control and Stopping

#### 5.1 **Introduction**

Stochastic control problems arise in many facets of financial modelling. The classical example is the optimal investment problem introduced and solved in continuous-time by Merton (1971). Of course there is a multitude of other applications, such as optimal dividend setting, optimal entry and exit problems, utility indifference valuation and so on. In general, the all-encompassing goal of stochastic control problems is to maximise ( or minimise) some expected profit (cost) function by tuning a strategy which itself affects the dynamics of the underlying stochastic system, and to find the strategy which attains the maximum (minimum). For example, in the simplest form of the Merton problem, the agent is trying to maximise expected utility of future wealth by trading a risky asset and a risk-free bank account. The agent's actions affect her wealth, but at the same time the uncertain dynamics in the traded asset modulate the agent's wealth in a stochastic manner. The resulting optimal strategies are tied to the dynamics of the asset and perhaps also to the agent's wealth. It is a surprising fact that, in many cases, the optimal strategies turn out to be Markov in the underlying state variables, even if the agent is considering non-Markovian controls (which may depend on the entire history of the system).

One tool keeps coming to the forefront when solving stochastic control problems: the dynamic programming principle (DPP) and the related non-linear partial differential equation (PDE) known as the Hamilton-Jacobi-Bellman (HJB) equation� also called the dynamic programming equation (DPE). The DPP allows a stochastic control problem to be solved from the terminal date backwards and the HJB equation / DPE can be viewed as its infinitesimal version.

Here, the subtle mathematical issues are not addressed and focus is instead placed on the mechanics which allow for immediate application to algorithmic trading problems employed at low and high frequencies. The interested reader is referred to the many excellent texts which focus on the theoretical aspects of stochastic control for a thorough treatment of the subject: Yong & Zhou (1999), Fleming & Saner (2006), 0ksendal & Sulem (2007), Pham (2010), and Touzi (2013).

# 5.2 Examples of Control Problems in Finance

This section provides a few examples of financially motivated stochastic control problems. The first example is a classical one in finance and pertains to optimal investment over long time horizons. The second is one of the first algorithmic trading control problems and pertains to the optimal liquidation of assets. The third refers to optimal placement of orders in a limit order book (LOB). All of these are essentially toy models and the last two will encompass the focus of many of the future chapters.

### 5.2.1 The Merton Problem

As a first example let us consider the classical portfolio optimisation problem of Merton ( 1971), in which the agent seeks to maximise expected (discounted) wealth by trading in a risky asset and the risk-free bank account (see Merton (1992) for many more examples and generalisations). Specifically, at time *t,* she places Kt dollars of her total wealth Xt in the risky asset St and seeks to obtain the so-called value function

$$H(S,x) = \sup_{\pi \in \mathcal{A}_{0,T}} \mathbb{E}_{S,x} \left[ U \left( X_T^{\pi} \right) \right], \tag{5.1}$$

which depends on the current wealth *x* and asset price *S,* and the resulting optimal trading strategy 1r, where,

$$dS_t = (\mu - r) S_t dt + \sigma S_t dW_t, \qquad S_0 = S, \qquad \text{risky asset}, \quad (5.2a)$$
  
$$dX_t^{\pi} = (\pi_t (\mu - r) + r X_t^{\pi}) dt + \pi_t \sigma dW_t, \quad X_0^{\pi} = x, \quad \text{agent's wealth}. \quad (5.2b)$$

In the above, µ represents the (expected) continuously compounded rate of growth of the traded asset, r is the continuously compounded rate of return of the risk-free bank account,

- *W* = (Wt){o:"'.t:"'.T} is a Brownian motion,
- ® *S* = (St){O:"'.t:"'.T} is the discounted price process of a traded asset,
- *<sup>e</sup>*1r = (1rt){O:"'.t:"'.T} is a self-financing trading strategy corresponding to having 1ft invested in the risky asset at time t (with the remaining funds in the risk-free bank account),
- ® x1r = (X!:){O:"'.t:"'.T} is the agent's discounted wealth process given that she follows the self-financing strategy 1r,
- e U(x) is the agent's utility function (e.g., power exponential -e-,x, and HARA �(x - xo)'),
- *e* A<sup>t</sup> ,T is a set of strategies, called the admissible set, corresponding to all F-predictable self-financing strategies that have *Jt* 1r; *ds* < +oo. This constraint excludes doubling strategies and allows strong solutions of (5.2b) to exist.

In this classical example, the agent's trading decisions affect only her wealth process, but not the dynamics of the asset which she is trading. On long time scales, and if the agent's strategy does not change "too quickly", this is a reasonable assumption. However, if an agent is attempting to acquire (or sell) a large number of shares in a short period of time, her actions most certainly affect the dynamics of the price itself – in addition to her wealth process. This issue is ignored in the Merton problem, but is at the heart of research into algorithmic trading and specifically optimal execution problems which we introduce next.

#### 5.2.2 The Optimal Liquidation Problem

As mentioned above, imagine that an agent has a large number of shares  $\mathfrak{N}$  of an asset whose price is  $S_t$ . Furthermore, suppose her fundamental analysis on the asset shows that it is no longer a valuable investment to hold. She therefore wishes to liquidate these shares by the end of the day, say at time  $T$ . The fact that the market does not have infinite liquidity (to absorb a large sell order) at the best available price implies that the agent will obtain poor prices if she attempts to liquidate all units immediately. Instead, she should spread this out over time, and solve a stochastic control problem to address the issue. She may also have a certain sense of urgency to get rid of these shares, represented by penalising holding inventories different from zero throughout the strategy. If  $\nu_t$ denotes the rate at which the agent sells her shares at time  $t$ , then the agent seeks the value function

$$H(x, S, q) = \sup_{\nu \in \mathcal{A}_{0, T}} \mathbb{E}\left[X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}) - \phi \int_0^T (Q_s^{\nu})^2 ds\right]$$
(5.3)

and the resulting optimal liquidation trading strategy  $\nu^*$ , where,

| $dQ_t^{\nu} = -\nu_t \, dt,$                      | $Q_0^{\nu} = q,$          | $\text{agent's inventory}, \quad (5.4a)$ |        |
|---------------------------------------------------|---------------------------|------------------------------------------|--------|
| $dS_t^{\nu} = -g(\nu_t) dt + \sigma dW_t,$        | $S_0^{\nu} = S$ ,         | fundamental asset price,                 | (5.4b) |
| $\hat{S}_t^{\nu} = S_t^{\nu} - h(\nu_t) \,,$      | $\hat{S}_0^{\nu} = S \,,$ | execution price, $(5.4c)$                |        |
| $dX_t^{\nu} = \nu_t \, \hat{S}_t^{\nu} \, dt \,,$ | $X_0^{\nu} = x$ ,         | $\text{agent's cash.} \qquad (5.4d)$     |        |

In the above,

- $\nu = (\nu_t)_{\{0 \le t \le T\}}$  is the (positive) rate at which the agent trades (liquidation rate) and is what the agent can control,
- $Q^{\nu} = (Q^{\nu}_{t})_{\{0 \le t \le T\}}$  is the agent's inventory,
- $W = (W_t)_{\{0 \le t \le T\}}$  is a Brownian motion,
- $S^{\nu} = (S^{\nu}_{t})_{\{0 < t < T\}}$  is the fundamental price process,
- $g: \mathbb{R}_+ \to \mathbb{R}_+$  denotes the permanent (negative) impact that the agent's trading action has on the fundamental price,
- $\hat{S}^{\nu} = (S^{\nu}_{t})_{\{0 \le t \le T\}}$  corresponds to the execution price process at which the agent can sell the asset,

- $h: \mathbb{R}_+ \to \mathbb{R}_+$  denotes the temporary (negative) impact that the agent's trading action has on the price they can execute the trade at,
- $X^{\nu} = (X^{\nu}_{t})_{\{0 \le t \le T\}}$  is the agent's cash process,
- $\mathcal{A}_{t,T}$  is the admissible set of strategies:  $\mathcal{F}$ -predictable non-negative bounded strategies. This constraint excludes repurchasing of shares and keeps the liquidation rate finite.

#### 5.2.3 Optimal Limit Order Placement

In the optimal liquidation problem above, the agent is assumed to post market orders spread through time to liquidate her shares. Such a strategy is intuitively sub-optimal since she will consistently be crossing the spread and potentially walking the book in order to sell her shares. Since she may also place limit orders, she can at least save the cost of crossing the spread, and perhaps even achieve better performance by posting deeper in the limit order book  $\text{LOB}$  – at a depth of  $\delta_t$  relative to the midprice  $S_t$ . The risk in doing so is that she may not execute her shares. Conditional on a market sell order arriving, the probability that it lifts the agent's posted offer at a price of  $S_t + \delta_t$  can be modelled as a function of  $\delta_t$  which we call the fill probability and denote by  $P(\delta_t)$ . The agent therefore can pose a control problem to decide how deep she must post in the LOB to optimise the value of liquidating her shares, subject to crossing the spread at the end of the trading horizon.

In this case, the agent's value function is given by

$$H(x, S, q) = \sup_{\delta \in \mathcal{A}_{[0,T]}} \mathbb{E}\left[X_T^{\delta} + Q_T^{\delta} \left(S_T^{\delta} - \alpha Q_T^{\delta}\right) - \phi \int_0^T \left(Q_s^{\delta}\right)^2 ds\right],$$

where

$$M_t$$
 market sell orders, (5.5a)

$$S_t = S_0 + \sigma W_t, \qquad \text{asset midprice}, \qquad (5.5b)$$

$$dX_t^{\delta} = (S_t + \delta_t) \left( -dQ_t^{\delta} \right), \qquad \qquad X_0^{\delta} = x, \qquad \qquad \text{agent's cash}, \qquad (5.5c)$$
  
$$dQ_t^{\delta} = -\mathbb{1}_{\left\{ U_{M_t^{-1} + 1} > P(\delta_t) \right\}} dM_t, \qquad Q_0^{\delta} = q, \qquad \text{agent's inventory}. \qquad (5.5d)$$

and where  $U_1, U_2, \ldots$  are i.i.d. uniform random variables.

#### 5.3 **Control for Diffusion Processes**

In this section, the control problems are of the general form

$$H(\boldsymbol{x}) = \sup_{\boldsymbol{u}\in\mathcal{A}_{0,T}} \mathbb{E}\left[G(\boldsymbol{X}_{T}^{\boldsymbol{u}}) + \int_{0}^{T} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) ds\right],\tag{5.6}$$

where u = (ut) <sup>o</sup><t<T is the vector (dim p) valued control process, *x<sup>u</sup>*= (Xt) <sup>o</sup><t<T is the vector (dim n) valued controlled process assumed (in this section) to be an Ito diffusion satisfying

$$d\boldsymbol{X}_{t}^{u} = \boldsymbol{\mu}(t, \boldsymbol{X}_{t}^{u}, \boldsymbol{u}_{t}) dt + \boldsymbol{\sigma}(t, \boldsymbol{X}_{t}^{u}, \boldsymbol{u}_{t}) d\boldsymbol{W}_{t}, \qquad \boldsymbol{X}_{0}^{u} = \boldsymbol{x}, \qquad (5.7)$$

where *(W* t) <sup>o</sup><t<T is a vector of independent Brownian motions, *A* is a set ( called the admissible set) of F-predictable processes such that (5.7) admits a strong solution (and may contain other constraints such as the process being bounded), *G* : ]R<sup>n</sup>*f--t* JR is a terminal reward and *F* : lR+ x ]Rn+p *f--t* JR is a running penalty /reward. The running penalty /reward may, in general, be dependent on time *t,* the current position of the controlled process **Xf,** and the control itself U<sup>t</sup> , while the terminal reward depends solely on the terminal value of the controlled process. For simplicity, the functions *G* and *F* are assumed uniformly bounded and the vector of drifts µt and volatilities at are, as usual, Lipschitz continuous. The integrability assumption on the controls, drift and volatility are necessary to ensure that the steps outlined below can be made rigorous. The predictability assumption on the controls is necessary since otherwise the agent may be able to peek into the future to optimise her strategy, and strategies which do peek into the future cannot be implemented in the real world.

The value function (5.6) has the interpretation that the agent wishes to maximise the total of terminal reward function *G* and running reward/penalty by acting in an optimal manner. Her actions *u* affect the dynamics of the underlying system in some generic way given by (5.7). Thus, her past actions affect the future dynamics and she must therefore adapt and tune her actions to account for this feedback effect.

For an arbitrary admissible control *u,* define the so-called performance criteria H<sup>u</sup> (x) by

$$H^{\boldsymbol{u}}(\boldsymbol{x}) = \mathbb{E}\left[G\left(\boldsymbol{X}_{T}^{\boldsymbol{u}}\right) + \int_{0}^{T} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds\right] \,.$$
(5.8)

The agent therefore seeks to maximise this performance criteria, and naturally

$$H(\boldsymbol{x}) = \sup_{\boldsymbol{u} \in \mathcal{A}_{0,T}} H^{\boldsymbol{u}}(\boldsymbol{x}) \,.$$
 (5.9)

As mentioned in the introduction, rather than optimising H<sup>u</sup> (x) directly, it is more convenient (and powerful) to introduce a time-indexed collection of optimisation problems on which a dynamic programming principle (DPP) can be derived. The DPP in infinitesimal form leads to a DPE - the Hamilton-Jacobi-Bellman (HJB) equation - which is a non-linear PDE whose solution is a tentative solution to the original problem. If a classical solution <sup>1</sup>to the DPE exists, it is possible to prove, through a verification argument, that it is in fact the solution to the original control. The next three subsections take on this programme.

<sup>1</sup> Here, a classical solution means that the solution is once differentiable in time and twice in all (diffusive) state variables, so that the infinitesimal generator can be applied to it.

![](_page_5_Figure_1.jpeg)

**Figure 5.1** The OPP allows the value function to be written as an expectation of the future value function. The key idea is to flow the dynamics of the controlled process from *t* to T and then rewrite the remaining expectation as the future performance criteria.

#### 5.3.1 The Dynamic Programming Principle

The usual trick<sup>2</sup>to solving stochastic (and deterministic!) control problems is to embed the original problem into a larger class of problems indexed by time *t* E [O, T] but equal to the original problem at *t* = 0. To this end, first define (with a slight abuse of notation)

$$H(t, \boldsymbol{x}) := \sup_{\boldsymbol{u} \in \mathcal{A}_{t, T}} H^{\boldsymbol{u}}(t, \boldsymbol{x}) \,, \quad \text{and} \tag{5.10a}$$

$$H^{u}(t,\boldsymbol{x}) := \mathbb{E}_{t,\boldsymbol{x}} \left[ G(\boldsymbol{X}_{T}^{u}) + \int_{t}^{T} F(s,\boldsymbol{X}_{s}^{u},\boldsymbol{u}_{s}) \, ds \right], \tag{5.10b}$$

where the notation lEt,x [·] represents expectation conditional on *Xf* = *x.* These two objects are the time indexed analog of the original control problem and the performance criteria. In particular, *H(O, x)* coincides with the original control problem (5.6) and H<sup>u</sup>(o, x) with the performance criteria (5.8).

Next take an arbitrary admissible strategy u and imagine flowing the *X* process forward in time from *t* to an arbitrary stopping time *T � T.* Then, conditional on *X":,* the contribution of the running reward/penalty from *T* to *T* and the terminal reward can be viewed as the performance criteria starting from the new value of *X":* (see Figure 5.1). This allows the value function to be written in terms of the expectation of its future value at *T* plus the reward between now and *T.* 

More precisely, by iterated expectations the time-indexed performance criteria

<sup>2</sup> There is another approach to controlling both deterministic and stochastic systems which makes use of Pontryagin's maximum principle. See Yong & Zhou (1999) for a wonderful exposition of its use for stochastic systems and the connection between it and the DPP formulation.

becomes

$$H^{\boldsymbol{u}}(t,\boldsymbol{x}) = \mathbb{E}_{t,\boldsymbol{x}} \left[ G(\boldsymbol{X}^{\boldsymbol{u}}_{T}) + \int_{\tau}^{T} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds + \int_{t}^{\tau} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right]$$
$$= \mathbb{E}_{t,\boldsymbol{x}} \left[ \mathbb{E}_{\tau,\boldsymbol{X}^{\boldsymbol{u}}_{\tau}} \left[ G(\boldsymbol{X}^{\boldsymbol{u}}_{T}) + \int_{\tau}^{T} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right] + \int_{t}^{\tau} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right]$$
$$= \mathbb{E}_{t,\boldsymbol{x}} \left[ H^{\boldsymbol{u}}(\tau,\boldsymbol{X}^{\boldsymbol{u}}_{\tau}) + \int_{t}^{\tau} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right]. \tag{5.11}$$

Now,  $H(t,x) \geq H^u(t,x)$  for an arbitrary admissible control  $u$  (with equality holding if  $u$  is the optimal control  $u^*$  - assuming that  $u^* \in \mathcal{A}_{t,T}$ , i.e. the supremum is attained by an admissible strategy<sup>3</sup>) and an arbitrary  $x$ . Hence, on the right-hand side of (5.11), the performance criteria  $H^u(\tau, X^u_\tau)$  at the stopping time  $\tau$  is bounded above by the value function  $H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}})$ . The equality can then be replaced by an inequality with the value function (and not the performance criteria) showing up under the expectation:

$$H^{\boldsymbol{u}}(t,\boldsymbol{x}) \leq \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds \right]$$
  
$$\leq \sup_{\boldsymbol{u} \in \mathcal{A}} \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds \right]$$

Note that on the right-hand side of the above, the arbitrary control  $\boldsymbol{u}$  only acts over the interval  $[t, \tau]$  and the optimal one is implicitly incorporated in the value function  $H(\tau, X^{\boldsymbol{u}}_{\tau})$  but starting at the point to which the arbitrary control  $\boldsymbol{u}$ caused the process  $X$  to flow, namely  $X^{\boldsymbol{u}}_{\tau}$ .

Taking supremum over admissible strategies on the left-hand side, so that the left-hand side also reduces to the value function, we have that

$$H(t,\boldsymbol{x}) \leq \sup_{\boldsymbol{u}\in\mathcal{A}} \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau,\boldsymbol{X}^{\boldsymbol{u}}_{\tau}) + \int_{t}^{\tau} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right] . \tag{5.12}$$

This provides us with a first inequality.

Next, we aim to show that the inequality above can be reversed. Take an arbitrary admissible control  $u \in \mathcal{A}$  and consider what is known as an  $\varepsilon$ -optimal con**trol** denoted by  $\boldsymbol{v}^{\varepsilon} \in \mathcal{A}$  and defined as a control which is better than  $H(t, \boldsymbol{x}) - \varepsilon$ , but of course not as good as  $H(t,x)$ , i.e. a control such that

$$H(t, x) \ge H^{\boldsymbol{v}^{\varepsilon}}(t, x) \ge H(t, x) - \varepsilon.$$

$$(5.13)$$

Such a control exists, assuming that the value function is continuous in the space of controls. Consider next the modification of the  $\varepsilon$ -optimal control

$$\tilde{\boldsymbol{\upsilon}}^{\varepsilon} = \boldsymbol{u}_{t} \,\mathbbm{1}_{t < \tau} + \boldsymbol{\upsilon}^{\varepsilon} \,\mathbbm{1}_{t > \tau} \,, \tag{5.14}$$

 $^3$  It may be the case that the supremum is obtained by a limiting sequence of admissible strategies for which the limiting strategy is in fact not admissible.

i.e. the modification is  $\varepsilon$ -optimal after the stopping time  $\tau$ , but potentially suboptimal on the interval  $[t, \tau]$ . Then we have that

$$\begin{split} H(t,\boldsymbol{x}) &\geq H^{\tilde{\boldsymbol{v}}^{\varepsilon}}(t,\boldsymbol{x}) \\ &= \mathbb{E}_{t,\boldsymbol{x}} \left[ H^{\tilde{\boldsymbol{v}}^{\varepsilon}}(\tau,\boldsymbol{X}_{\tau}^{\tilde{\boldsymbol{v}}^{\varepsilon}}) + \int_{t}^{\tau} F(s,\boldsymbol{X}_{s}^{\tilde{\boldsymbol{v}}^{\varepsilon}},\tilde{\boldsymbol{v}}^{\varepsilon}_{s}) \, ds \right] \,, \qquad \qquad \text{(from (5.11))}\,, \end{split}$$

$$= \mathbb{E}_{t,\boldsymbol{x}} \left[ H^{\tilde{\boldsymbol{v}}}(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds \right], \qquad \qquad \text{(using (5.14))},$$

$$\geq \mathbb{E}_{t,\boldsymbol{x}}\left[H(\tau,\boldsymbol{X}_{\tau}^{\boldsymbol{u}})+\int_{t}^{\tau}F(s,\boldsymbol{X}_{s}^{\boldsymbol{u}},\boldsymbol{u}_{s})\,ds\right]-\varepsilon\,,\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\$$

Taking the limit as  $\varepsilon \searrow 0$ , we have

$$H(t,\boldsymbol{x}) \geq \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{u}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{u}, \boldsymbol{u}_{s}) \, ds \right] .$$

Moreover, since the above holds true for every  $u \in \mathcal{A}$  we have that

$$H(t,\boldsymbol{x}) \geq \sup_{\boldsymbol{u}\in\mathcal{A}} \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau,\boldsymbol{X}^{\boldsymbol{u}}_{\tau}) + \int_{t}^{\tau} F(s,\boldsymbol{X}^{\boldsymbol{u}}_{s},\boldsymbol{u}_{s}) \, ds \right] \,.$$
(5.15)

The upper bound  $(5.12)$  and lower bound  $(5.15)$  form the dynamic programming inequalities. Putting them together, we obtain the theorem below.

Dynamic Programming Principle for Diffusions. The THEOREM  $5.1$ value function  $(5.10)$  satisfies the DPP

$$H(t,\boldsymbol{x}) = \sup_{\boldsymbol{u}\in\mathcal{A}} \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds \right] \,, \tag{5.16}$$

for all  $(t, x) \in [0, T] \times \mathbb{R}^n$  and all stopping times  $\tau \leq T$ .

This equation is really a sequence of equations that tie the value function to its future expected value, plus the running reward/penalty. Since it is a sequence of equations, an even more powerful equation can be found by looking at its  $\text{infinitesimal version}$  – the so-called DPE.

#### 5.3.2 Dynamic Programming Equation / Hamilton–Jacobi–Bellman Equation

The DPE is an infinitesimal version of the dynamic programming principle  $\text{(DPP)}$  (5.16). There are two key ideas involved:

(i) Setting the stopping time  $\tau$  in the DPP to be the minimum between (a) the time it takes the process  $X_t^u$  to exit a ball of size  $\epsilon$  around its starting point, and (b) a fixed (small) time  $h$  – all while keeping it bounded by  $T$ . This can be viewed as in Figure  $5.2$  and can be stated precisely as

$$\tau = T \wedge \inf \left\{ s > t : (s - t, \ |\boldsymbol{X}_{s}^{\boldsymbol{u}} - \boldsymbol{x}|) \notin [0, h) \times [0, \epsilon) \right\}.$$

Notice that as  $h \searrow 0$ ,  $\tau \searrow t$ , a.s. and that  $\tau = t + h$  whenever h is

![](_page_8_Figure_1.jpeg)

Figure 5.2 The DPE is an infinitesimal version of the DPP where the stopping time  $\tau$  is the first exit time from a ball of size  $\epsilon$  or a small time  $h$ , whichever occurs first. This sample plot of three paths, and the corresponding value  $X^u_\tau$  and stopping time  $\tau$  indicated by the black circles for  $\epsilon = 0.05$  and  $h = 0.01$ .

sufficiently small – since as the time span  $h$  shrinks, it is less and less likely that  $X$  will exit the ball first.

(ii) Writing the value function (for an arbitrary admissible control  $\boldsymbol{u}$ ) at the stopping time  $\tau$  in terms of the value function at t using Itô's lemma. Specifically, assuming enough regularity of the value function, we can write

$$H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}})$$
  
=  $H(t, \boldsymbol{x}) + \int_{t}^{\tau} (\partial_{t} + \mathcal{L}_{s}^{\boldsymbol{u}}) H(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}) ds + \int_{t}^{\tau} \mathcal{D}_{x} H(s, \boldsymbol{X}_{s}^{\boldsymbol{u}})' \boldsymbol{\sigma}_{s}^{\boldsymbol{u}} d\boldsymbol{W}_{s},$  (5.17)

where  $\boldsymbol{\sigma}^{\boldsymbol{u}}_t := \sigma(t, \boldsymbol{X}^{\boldsymbol{u}}_t, \boldsymbol{u}_t)$  for compactness,  $\mathcal{L}^{\boldsymbol{u}}_t$  represents the infinitesimal generator of  $\boldsymbol{X}_{t}^{\boldsymbol{u}}$ , and  $\boldsymbol{\mathcal{D}}_{x}H(\cdot)$  denotes the vector of partial derivatives with components  $[\mathcal{D}_x H(\cdot)]_i = \partial_{x^i} H(\cdot)$ . For example, in the one-dimensional case,

$$\begin{split} \mathcal{L}_t^u &= \mu_t^u \, \partial_x + \tfrac{1}{2} (\sigma_t^u)^2 \, \partial_{xx} \\ &= \mu(t, x, u) \, \partial_x + \tfrac{1}{2} \sigma^2(t, x, u) \, \partial_{xx} \end{split}$$

As before, we derive the DPE in two stages by obtaining two inequalities.

First, taking  $\mathbf{v} \in \mathcal{A}$  to be constant over the interval  $[t, \tau]$ , applying the lower bound  $(5.15)$ , and substituting  $(5.17)$  into the right-hand side implies that

$$H(t, \boldsymbol{x}) \geq \sup_{\boldsymbol{u} \in \mathcal{A}} \mathbb{E}_{t, \boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}}, \boldsymbol{u}_{s}) \, ds \right]$$
  

$$\geq \mathbb{E}_{t, \boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{v}}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{v}}, \boldsymbol{v}) \, ds \right]$$
  

$$= \mathbb{E}_{t, \boldsymbol{x}} \left[ H(t, \boldsymbol{x}) + \int_{t}^{\tau} (\partial_{t} + \mathcal{L}_{s}^{\boldsymbol{v}}) \, H(s, \boldsymbol{X}_{s}^{\boldsymbol{v}}) \, ds \right]$$
  

$$+ \int_{t}^{\tau} \mathcal{D}_{\boldsymbol{x}} H(s, \boldsymbol{X}_{s}^{\boldsymbol{v}})' \boldsymbol{\sigma}_{s}^{\boldsymbol{v}} \, dW_{s} + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{v}}, \boldsymbol{v}) \, ds \right]$$

The integrand in the stochastic integral above, i.e.  $\mathcal{D}_x H(s, \boldsymbol{X}_s^{\boldsymbol{v}})' \boldsymbol{\sigma}_s^{\boldsymbol{v}}$ , is bounded on the interval  $[t,\tau]$  since we have ensured that  $|X_t^{\upsilon}-x|\leq \epsilon$  on the interval. Hence, this stochastic integral is the increment of a martingale and we can be

assured that its expectation is zero. Therefore,

$$H(t,\boldsymbol{x}) \geq \mathbb{E}_{t,\boldsymbol{x}} \left[ H(t,\boldsymbol{x}) + \int_t^\tau \left\{ \left( \partial_t + \mathcal{L}_s^{\boldsymbol{v}} \right) H(s,\boldsymbol{X}_s^{\boldsymbol{v}}) + F(s,\boldsymbol{X}_s^{\boldsymbol{v}},\boldsymbol{v}) \right\} ds \right],$$

and recall that *T* = *t* + *h.*

Moving the *H(t, x)* on the left-hand side over to the right-hand side, dividing by h and taking the limit as h '\, 0 yields

$$0 \geq \lim_{h \downarrow 0} \mathbb{E}_{t, \boldsymbol{x}} \left[ \frac{1}{h} \int_{t}^{\tau} \left\{ \left( \partial_{t} + \mathcal{L}_{s}^{\boldsymbol{v}} \right) H(s, \boldsymbol{X}_{s}^{\boldsymbol{v}}) + F(s, \boldsymbol{X}_{s}^{\boldsymbol{v}}, \boldsymbol{v}) \right\} ds \right]$$
  
=  $\left( \partial_{t} + \mathcal{L}_{t}^{\boldsymbol{v}} \right) H(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{v}) \, .$ 

The second line follows from:

- (i) as h '\, 0, *T* = *t* + h a.s. since the process will not hit the barrier of E in extremely short periods of time,
- (ii) the condition that IX� xi ::; E, which implies that if the process does hit the barrier it is bounded,
- (iii) the Mean-Value Theorem allows us to write limh-1-0 ¼ J/+h w*8 ds* = Wt, and

(iv) the process starts at 
$$\boldsymbol{X}_{t}^{\boldsymbol{v}} = \boldsymbol{x}$$
.

Since the above inequality holds for arbitrary *v* E A, it follows that

$$\partial_t H(t, \boldsymbol{x}) + \sup_{\boldsymbol{u} \in \mathcal{A}} \left( \mathcal{L}_t^{\boldsymbol{u}} H(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}) \right) \le 0.$$
 (5.18)

Next, we show that the inequality is indeed an equality. To show this, suppose that *u\** is an optimal control, then from (5.16), we have

$$H(t,\boldsymbol{x}) = \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau, \boldsymbol{X}_{\tau}^{\boldsymbol{u}^*}) + \int_{t}^{\tau} F(s, \boldsymbol{X}_{s}^{\boldsymbol{u}^*}, \boldsymbol{u}^*) ds \right].$$

As above, by applying Ito's lemma to write *H(T,x�·)* in terms of *H(t,x)* plus the integral of its increments, taking expectations, and then the limit as h '\, 0, we find that

$$\partial_t H(t, \boldsymbol{x}) + \mathcal{L}_t^{\boldsymbol{u}^*} H(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}^*) = 0.$$

Combined with (5.18), we finally arrive at the DPE (also known in this context as the **Hamilton-Jacobi-Bellman equation)**

$$\partial_t H(t, \boldsymbol{x}) + \sup_{\boldsymbol{u} \in \mathcal{A}} \left( \mathcal{L}_t^{\boldsymbol{u}} H(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}) \right) = 0,$$
  
$$H(T, \boldsymbol{x}) = G(\boldsymbol{x}) \,.$$
 (5.19)

The terminal condition above follows from the definition of the value function in (5.10) from which we see that the running reward/penalty drops out and *G(X'!f,)* is Fr measurable.

Notice that the optimisation of the control in (5.19) is only over its value at time *t,* rather than over the whole path of the control. Hence, it appears that the optimal control can be obtained pointwise. Treating the value function as known, the optimal control can often be found in feedback control form in terms of the value function itself. Substituting the feedback control back into (5.19) results in non-linear PDEs. In fact the function

$$\mathfrak{H}(t, x, \mathcal{D}_x H, \mathcal{D}_x^2 H) = \sup_{u \in \mathcal{A}} \left( \mathcal{L}_t^u H(t, x) + F(t, x, u) \right)$$

is called the **Hamiltonian** of the associated stochastic control problem. Here DxH and D;H represent the collection of first and second order derivatives of the value function H respectively (recall that in general *X* is vector-valued) and in particular

$$[\mathcal{D}H]_k = \partial_{x^k} H \,, \qquad \text{and} \qquad [\mathcal{D}_x^2 H]_{jk} = \partial_{x^j x^k} H \,.$$

These objects appear in the infinitesirnal generator.

### **Example: The Merton Problem**

Consider now the Merton optimisation problem described in Section 5.2.1. The optimisation problem is given in (5.1) and has the associated time dependent performance criteria

$$H^{\pi}(t,x,S) = \mathbb{E}_{t,x,S} \left[ U \left( X_T^{\pi} \right) \right] \,, \tag{5.20}$$

where x1r (investor wealth) and 8 (risky asset price) satisfy the SDEs (5.2) with 1r representing the dollar value of wealth invested in the risky asset 8. From (5.2b ), the infinitesimal generator of the pair of processes *(X;,* 8t)o�t�T is then

$$\mathcal{L}_t^{\pi} = \left(r\,x + \left(\mu - r\right)\pi\right)\,\partial_x + \tfrac{1}{2}\sigma^2\,\pi\,\partial_{xx} + \left(\mu - r\right)S\,\partial_S + \tfrac{1}{2}\sigma^2\,S^2\,\partial_{SS} + \sigma\,\pi\,\partial_{xS} \ .$$

According to (5.19), the value function H(t, *x, 8)* = sup1rE A[ ,.TJ H1r(t, *x, 8)* should satisfy the equation

$$0 = \left(\partial_t + r \, x \, \partial_x + \frac{1}{2} \, \sigma^2 \, S^2 \, \partial_{SS}\right) H$$
  
+ 
$$\sup_{\pi} \left\{ \pi \, \left( \left(\mu - r\right) \partial_x + \sigma \, \partial_{xS} \right) H + \frac{1}{2} \sigma^2 \, \pi^2 \, \partial_{xx} H \right\} \, ,$$

subject to the terminal condition H(T, x, 8) = U(x). Note that the argument of the sup is quadratic in 7r and as long as BxxH(t, *x, 8)* < 0, the sup attains a maximum. By completing the squares we have

$$\pi \left( \left( \mu - r \right) \partial_x + \sigma \partial_{xS} \right) H + \frac{1}{2} \sigma^2 \pi^2 \partial_{xx} H$$
  
=  $\frac{1}{2} \sigma^2 \partial_{xx} H \left( \left( \pi - \pi^* \right)^2 - \left( \pi^* \right)^2 \right) ,$ 

where

$$\pi^* = -\frac{(\mu - r)\,\partial_x H + \sigma\,\partial_{xS} H}{\sigma^2\,\partial_{xx} H}$$

is the optimal control in feedback form - i.e. it is the optimal control given the known value function H(t, *x,* 8). Substituting this optimum back into the DPE

yields the non-linear PDE for the value function

$$0 = \left(\partial_t + r \, x \, \partial_x + \frac{1}{2} \, \sigma^2 \, S^2 \, \partial_{SS}\right) H - \frac{\left((\mu - r) \, \partial_x H + \sigma \, \partial_{xS} H\right)^2}{2 \, \sigma^2 \, \partial_{xx} H}$$

This simplifies somewhat by observing that the terminal condition  $H(t, x, S) =$  $U(x)$  is independent of S. Hence, it suggests the ansatz  $H(t,x,S) = h(t,x)$  in which case we obtain a simpler, but still non-linear, equation for  $h(t, x)$ 

$$0 = (\partial_t + r x \,\partial_x) h(t, x) - \frac{\lambda}{2 \,\sigma} \frac{\left(\partial_x h(t, x)\right)^2}{\partial_{xx} h(t, x)}$$

with terminal condition  $h(T,x) = U(x)$  and where  $\lambda = \frac{\mu-r}{\sigma}$  is the market price of risk, also referred to as the Sharpe ratio. Moreover, the optimal control simplifies  $to$ 

$$\pi^* = -\frac{\lambda}{\sigma} \left( \frac{\partial_x h}{\partial_{xx} h} \right) \, .$$

The explicit solution of the non-linear PDE depends on the precise form of the utility function  $U(x)$ . Two classic examples are

 $(i)$  exponential utility

$$U(x) = -e^{-\gamma x}, \qquad \gamma > 0,$$

which is defined for all  $x \in \mathbb{R}$ , and

 $(ii)$  hyperbolic absolute risk aversion  $(HARA)$  utility

$$U(x) = \frac{1-\gamma}{\gamma} \left( a + \frac{b}{1-\gamma} x \right)^{\gamma}, \qquad \gamma > 1, \ b > 0, \ x \in \left( -(1-\gamma)\frac{a}{b}, +\infty \right) \ .$$

Admissible wealth has a lower bound in this case and the investor is infinitely averse to dropping below this level.

For exponential utility, the value function admits an affine solution and we can write an ansatz

$$h(t,x) = -\alpha(t) e^{-\gamma x \beta(t)},$$

where  $\alpha(t)$  and  $\beta(t)$  are yet to be determined functions of time alone. From the terminal condition  $h(T,X) = -e^{-\gamma x}$  we have that  $\alpha(T) = \beta(T) = 1$  and upon substituting this back into the non-linear PDE above, we find that

$$\left(\partial_t \alpha - \frac{\lambda}{2\sigma} \,\alpha\right) - \gamma \,\left(\partial_t \beta + r \,\beta\right) \,\alpha \, x = 0 \,.$$

Since this must hold for every  $x$  and  $t$ , the terms in braces must individually vanish. These two equations  $\partial_t \alpha - \frac{\lambda}{2\sigma} \alpha = 0$  and  $\partial_t \beta + r \beta = 0$ , together with the terminal conditions, are easily solved to find

$$\alpha(t) = e^{-\frac{\lambda}{2\sigma}(T-t)}, \quad \beta(t) = e^{r(T-t)}$$

Upon back substitution, we find that the optimal amount to invest in the risky asset is a deterministic function of time

$$\pi^*(t) = \frac{\lambda}{\gamma \sigma} e^{-r(T-t)}.$$

As risk-aversion increases, the investor puts less into the risky asset. The fact that the amount invested is independent of wealth results from the agent's absolute risk aversion, defined as *-U"(x)/U'(x)* = *1,* being a constant since she uses exponential utility. For HARA utilities, e.g., neither the absolute risk aversion nor the relative risk aversion, defined as *R(x)* = *-x U"(x)/U'(x),* are constants. In the HARA case, the agent's risky investment is a non-trivial function of both wealth and time.

#### 5.3.3 Verification

The derivation of the DPE (5.19) in the previous section provides a necessary condition for the value function. A pertinent question, however, is whether or not a solution of the DPE does indeed provide the solution to the original control problem. The main workhorse for showing this is indeed the case, when classical solutions to the associated DPE exist, is the so-called verification theorem. We state the result below and refer the reader to many of the excellent texts on optimal control for its proof, see e.g., Yong & Zhou (1999), Fleming & Saner **(2006),** 0ksendal & Sulem **(2007),** and Pham **(2010).** 

THEOREM 5.2 Verification Theorem. *Let* 'ljJ E C 1 • 2 ([0, T] x 1R<sup>n</sup> ) *and satisfies, for all u* EA,

$$\partial_t \psi(t, \boldsymbol{x}) + (\mathcal{L}_t^{\boldsymbol{u}} \psi(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u})) \le 0 \,, \quad \forall \ (t, \boldsymbol{x}) \in [0, T] \times \mathbb{R}^n \,,$$
$$G(\boldsymbol{x}) - \psi(T, \boldsymbol{x}) \le 0 \,.$$

*Then*

$$\psi(t,\boldsymbol{x}) \ge H^{\boldsymbol{u}}(t,\boldsymbol{x}) \,, \quad \forall \ (t,\boldsymbol{x}) \in [0,T] \times \mathbb{R}^n \,,$$

*for all Markov controls u* E A.

*Moreover, if for every (t,x)* E [O,T] x 1R<sup>n</sup> , *there exists measurable u\*(t,x) such that*

$$0 = \partial_t \psi(t, \boldsymbol{x}) + \left( \mathcal{L}_t^{\boldsymbol{u}^*(t, \boldsymbol{x})} \psi(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}^*(t, \boldsymbol{x})) \right)$$
  
=  $\partial_t \psi(t, \boldsymbol{x}) + \sup_{\boldsymbol{u} \in \mathcal{A}} \left( \mathcal{L}_t^{\boldsymbol{u}} \psi(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}) \right), \qquad \forall (t, \boldsymbol{x}) \in [0, T] \times \mathbb{R}^n,$ 

*with '1/J(T, x)* = *G(x), and the SDE*

$$d\boldsymbol{X}_{s}^{*} = \mu(t, \boldsymbol{X}_{s}^{*}, \boldsymbol{u}^{*}(t, \boldsymbol{X}_{s}^{*})) dt + \boldsymbol{\sigma}(t, \boldsymbol{X}_{s}^{*}, \boldsymbol{u}^{*}(t, \boldsymbol{X}_{s}^{*})) d\boldsymbol{W}_{s}, \qquad \boldsymbol{X}_{t}^{*} = \boldsymbol{x},$$

*admits a unique solution and {u\*(s,x:)h:<'.s:<'.T* EA, *then*

$$H(t,\boldsymbol{x}) = \psi(t,\boldsymbol{x})\,, \qquad \forall \; (t,\boldsymbol{x}) \in [0,T] \times \mathbb{R}^n\,,$$

*and u\* is an optimal Markov control.*

The theorem states that if we can find a solution to the DPE and demonstrate that it is a classical solution, i.e. once differentiable in time and twice differentiable in the state variables, and the resulting control is admissible, then

the solution is indeed the value function we seek and the resulting control is the  $optimal one - at least an optimal Markov control. Another key result is that, un$ der some more technical assumptions, the optimal control is Markov, even if we search over general  $\mathcal{F}$ -predictable controls. See, e.g., Theorem 11.2.3 in Øksendal  $(2010).$ 

#### 5.4 **Control for Counting Processes**

In the previous section, diffusion processes were the driving sources of uncertainty in the control problem. In many circumstances, and in particular problems related to algorithmic and high-frequency trading, counting processes will be used to drive uncertainty. There are many features that can be incorporated into the analysis, but the general approach remains the same, and as such only the case of a single counting process with controlled intensity will be investigated. This amounts to treating doubly stochastic Poisson processes, or Cox processes, which are counting processes with intensity that itself is a stochastic process and in this case at least partially controlled.

Consider the situation in which the agent can control the frequency of the jumps in a counting process  $N$  and does so to maximise some target. In this case, the control problem is of the general form

$$H(n) = \sup_{u \in \mathcal{A}_{0,T}} \mathbb{E}\left[G(N_T^u) + \int_0^T F(s, N_s^u, u_s) ds\right],\tag{5.21}$$

where  $u = (u_t)_{0 \le t \le T}$  is the control process,  $(N_t^u)_{0 \le t \le T}$  is a controlled doubly stochastic Poisson process (starting at  $N_{0^-} = n$ ) with intensity  $\lambda_t^u = \lambda(t, N_{t-}^u, u_t)$  so that  $(\widehat{N}_t^u)_{0 \le t \le T}$ , where

$$\widehat{N}_t^u = N_t - \int_0^t \lambda_s^u \, ds$$

is a martingale,  $\mathcal A$  is a set of  $\mathcal F\text{-predictable processes such that } \widehat N$  is a true martingale,  $G: \mathbb{R} \mapsto \mathbb{R}$  is a terminal reward and  $F: \mathbb{R}_+ \times \mathbb{R}^2 \mapsto \mathbb{R}$  is a running reward/penalty. As before, the functions  $G$  and  $F$  are assumed uniformly bounded.

For an arbitrary admissible control u, the **performance criteria**  $H^u(n)$  is given by

$$H^{u}(n) = \mathbb{E}\left[G\left(N_{T}^{u}\right) + \int_{0}^{T} F(s, N_{s}^{u}) ds\right],\tag{5.22}$$

and the agent seeks to maximise this performance criteria, i.e.

$$H(n) = \sup_{u \in \mathcal{A}_{0,T}} H^u(n) \,. \tag{5.23}$$

In the next two subsections we provide a concise derivation of the DPP and the  $\text{associated DPE.}$ 

#### $5.4.1$ The Dynamic Programming Principle

As before, the original problem is embedded into a larger class of  $\text{problems}$ indexed by time  $t \in [0, T]$  by first defining

$$H(t,n) := \sup_{u \in \mathcal{A}_{t,T}} H^u(t,n), \text{ and } (5.24a)$$

$$H^{u}(t,n) := \mathbb{E}_{t,n} \left[ G(N_{T}^{u}) + \int_{t}^{T} F(s, N_{s}^{u}, u_{s}) ds \right], \qquad (5.24b)$$

where the notation  $\mathbb{E}_{t,n}[\cdot]$  represents expectation conditional on  $N_{t^-} = n$ . Next, take an arbitrary admissible strategy  $u$  and flow the  $N$  process forward in time from t to an arbitrary stopping time  $\tau \leq T$ . Then, conditional on  $N^{\tau}_{\tau}$ , the contribution of the running reward/penalty from  $\tau$  to T and the terminal reward can be viewed as the performance criteria starting from the new value of  $N^u_{\tau}$ . This allows the value function to be written in terms of the expectation of its future value at  $\tau$  plus the reward between now and  $\tau$ .

More precisely, by iterated expectations the time-indexed performance criteria becomes

$$H^{u}(t,n) = \mathbb{E}_{t,n} \left[ G(N_{T}^{u}) + \int_{\tau}^{T} F(s, N_{s}^{u}, u_{s}) ds + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right]$$
  
$$= \mathbb{E}_{t,n} \left[ \mathbb{E}_{\tau, N_{\tau}^{u}} \left[ G(N_{T}^{u}) + \int_{\tau}^{T} F(s, N_{s}^{u}, u_{s}) ds \right] + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right]$$
  
$$= \mathbb{E}_{t,n} \left[ H^{u}(\tau, N_{\tau}^{u}) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right]. \tag{5.25}$$

Now,  $H(t,n) \geq H^u(t,n)$  for an arbitrary admissible control u (with equality holding if u is the optimal control  $u^*$ ) and an arbitrary n. Hence, on the righthand side of (5.25) the performance criteria  $H^u(\tau, N^u_\tau)$  is bounded above by the value function  $H(\tau, N^u_\tau)$  and the equality can be replaced by an inequality with the value function (and not the performance criteria) showing up under the  $\text{expectation:}$ 

$$H^{u}(t,n) \leq \mathbb{E}_{t,n} \left[ H(\tau, N_{\tau}^{u}) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right]$$
  
$$\leq \sup_{u \in \mathcal{A}} \mathbb{E}_{t,n} \left[ H(\tau, N_{\tau}^{u}) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right] . \tag{5.26}$$

Note that on the right-hand side of the first line of  $(5.26)$ , the arbitrary control u only acts over the interval  $[t, \tau]$  and the optimal control is implicitly incorporated in the value function  $H(\tau, N^u_\tau)$ , but with the state variable N beginning at the point where the arbitrary control u caused N to flow, namely  $N_{\tau}^{u}$ . Next, taking the best control on the right-hand side must also dominate the left-hand side, since the arbitrary one does. Then, the right-hand side is no longer dependent on the arbitrary control. Finally, taking a supremum over all admissible controls on the left-hand side allows us to replace the left-hand side with the value function

and provides us with the first inequality

$$H(t,n) \leq \sup_{u \in \mathcal{A}} \mathbb{E}_{t,n} \left[ H(\tau, N^u_\tau) + \int_t^t F(s, N^u_s, u_s) \, ds \right] \,. \tag{5.27}$$

To obtain the reverse inequality, take an  $\epsilon$ -optimal control denoted by  $v^{\epsilon} \in \mathcal{A}$ such that

$$H(t,x) \ge H^{v^{\epsilon}}(t,x) \ge H(t,x) - \epsilon. \tag{5.28}$$

Such a control exists if the value function is continuous in the space of controls. Consider its modification up to time  $\tau$ :

$$\tilde{\upsilon}^{\epsilon} = u_t \, \mathbbm{1}_{t \le \tau} + \upsilon^{\epsilon} \, \mathbbm{1}_{t > \tau} \,, \tag{5.29}$$

where  $u \in \mathcal{A}$  is an arbitrary admissible control. Then we have that

$$H(t,n) \geq H^{\tilde{v}^{\varepsilon}}(t,n)$$
  
$$= \mathbb{E}_{t,n} \left[ H^{\tilde{v}^{\varepsilon}}(\tau, N_{\tau}^{\tilde{v}^{\varepsilon}}) + \int_{t}^{\tau} F(s, N_{s}^{\tilde{v}^{\varepsilon}}, \tilde{v}_{s}^{\varepsilon}) ds \right], \qquad \text{(from (5.25))},$$
  
$$= \mathbb{E}_{t,n} \left[ H^{\tilde{v}^{\varepsilon}}(\tau, N^{u}) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) ds \right], \qquad \text{(using (5.29))}.$$

$$\begin{aligned} & -\mathbb{E}_{t,n} \left[ H \left( \tau, N_{\tau}^{u} \right) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) \, ds \right], \qquad \text{(using (5.28))}, \\ & \geq \mathbb{E}_{t,n} \left[ H(\tau, N_{\tau}^{u}) + \int_{t}^{\tau} F(s, N_{s}^{u}, u_{s}) \, ds \right] - \varepsilon, \qquad \text{(by (5.28))}. \end{aligned}$$

Since the above holds for every u and every  $\epsilon$ , it holds for the sup, and we take the limit as  $\varepsilon \searrow 0$  to find the inequality

$$H(t,n) \ge \sup_{u \in \mathcal{A}} \mathbb{E}_{t,n} \left[ H(\tau, N^u_\tau) + \int_t^\tau F(s, N^u_s, u_s) \, ds \right] \,. \tag{5.30}$$

Putting  $(5.30)$  together with  $(5.27)$ , we obtain the theorem below.

THEOREM 5.3 Dynamic Programming Principle for Counting Pro**cesses.** The value function  $(5.23)$  satisfies the DPP

$$H(t,n) = \sup_{u \in \mathcal{A}} \mathbb{E}_{t,n} \left[ H(\tau, N^u_\tau) + \int_t^\tau F(s, N^u_s, u_s) \, ds \right], \tag{5.31}$$

for all  $(t, n) \in [0, T] \times Z_+$  and all stopping times  $\tau \leq T$ .

#### 5.4.2 Dynamic Programming Equation / Hamilton–Jacobi–Bellman Equation

This section develops the DPE satisfied by the value function, which we obtain by looking at the DPP over infinitesimal amounts of time. Analogous to the diffusion case, set the stopping time  $\tau$  in the DPP to be the minimum of (i) the time it takes the process  $N_t^u$  to exit a ball of size  $\epsilon$  around its starting point, and (ii) a fixed (small) time  $h$ , all while keeping it bounded by  $T$ .

$$\tau = T \wedge \inf\{s > t : (s - t, |N_s^u - n|) \notin [0, h) \times [0, \epsilon)\}.$$

Next, write the value function (for an arbitrary admissible control  $u$ ) at the stopping time  $\tau$  in terms of the value function at t using Itô's lemma. Specifically,

$$H(\tau, N_{\tau}^{u}) = H(t, n) + \int_{t}^{\tau} (\partial_{t} + \mathcal{L}_{s}^{u}) H(s, N_{s}^{u}) ds$$
  
+ 
$$\int_{t}^{\tau} [H(s, N_{s^{-}}^{u} + 1) - H(s, N_{s^{-}}^{u})] d\widehat{N}_{s}^{u}, \qquad (5.32)$$

where  $\mathcal{L}_t^u$  represents the infinitesimal generator of  $N_t^u$  and acts on functions  $h: \mathbb{R}_+ \times \mathbb{Z}_+ \mapsto \mathbb{R}$  as follows:

$$\mathcal{L}_t^u h(t,n) = \lambda(t,n,u) \left[ h(t,n+1) - h(t,n) \right]$$

Taking  $v \in \mathcal{A}$  to be constant over the interval  $|t,\tau|$ , applying the lower bound  $(5.30)$ , and substituting  $(5.32)$  into the right-hand side implies that

$$\begin{split} H(t,n) &\geq \sup_{u \in \mathcal{A}} \mathbb{E}_{t,n} \left[ H(\tau, N^{\upsilon}_{\tau}) + \int_{t}^{\tau} F(s, N^{\upsilon}_{s}, u_{s}) \, ds \right] \\ &\geq \mathbb{E}_{t,n} \left[ H(\tau, N^{\upsilon}_{\tau}) + \int_{t}^{\tau} F(s, N^{\upsilon}_{s}, v) \, ds \right] \\ &= \mathbb{E}_{t,n} \left[ H(t,n) + \int_{t}^{\tau} \left( \partial_{t} + \mathcal{L}^{\upsilon}_{s} \right) H(s, N^{\upsilon}_{s}) \, ds \right. \\ &\quad \left. + \int_{t}^{\tau} \left( H(s, N^{\upsilon}_{s^{-}} + 1) - H(s, N^{\upsilon}_{s^{-}}) \right) d\widehat{N}^{\upsilon}_{s} + \int_{t}^{\tau} F(s, N^{\upsilon}_{s}, v) \, ds \right] \\ &= \mathbb{E}_{t,n} \left[ H(t,n) + \int_{t}^{\tau} \left( (\partial_{t} + \mathcal{L}^{\upsilon}_{s}) \, H(s, N^{\upsilon}_{s}) + F(s, N^{\upsilon}_{s}, v) \right) \, ds \right] \, . \end{split}$$

The third equality follows because the stochastic integral with respect to  $\widehat{N}_t$ has zero mean since  $\widehat{N}_t$  is a martingale. The martingale property is guaranteed because we have  $|N_t^{\upsilon}-n|\leq \epsilon$ , and so  $\mathcal{L}_t^{\upsilon}H(t,N_t^{\upsilon})$  is bounded. Subtracting  $H(t,n)$ , dividing by h, and taking the limit as  $h \searrow 0$  implies that

$$0 \geq \lim_{h \downarrow 0} \mathbb{E}_{t,n} \left[ \frac{1}{h} \int_t^\tau \left( (\partial_t + \mathcal{L}_s^v) H(s, N_s^v) + F(s, N_s^v, v) \right) ds \right]$$
  
=  $(\partial_t + \mathcal{L}_t^v) H(t,n) + F(t,n,v)$ . (5.33)

In the above, the control is constant, and equals  $v$ , on the interval  $[t, \tau]$ . The second line follows, as before, from:

- (i) as  $h \searrow 0$ ,  $\tau = t + h$  a.s. since the process will not hit the barrier of  $\epsilon$  in extremely short periods of time,
- (ii) the condition that  $|N_{\tau}^{\upsilon}-n|\leq\epsilon$ , so that if the process does hit the barrier, it is bounded,
- (iii) the Fundamental Theorem of Calculus:  $\lim_{h\downarrow 0} \frac{1}{h} \int_{t}^{t+h} \omega_s \, ds = \omega_t$ , and
- (iv)  $N_{t-}^{u} = n$ .

Since the above inequality holds for arbitrary  $v \in \mathcal{A}$ , it follows that

$$\partial_t H(t,n) + \sup_{u \in \mathcal{A}} \left( \mathcal{L}_t^u H(t,n) + F(t,n,u) \right) \le 0. \tag{5.34}$$

Next, we show the inequality is indeed an equality. For this purpose, suppose

that  $u^* \in \mathcal{A}$  is an optimal control, then from the DPP (5.31) we have

$$H(t,n) = \mathbb{E}_{t,n} \left[ H(\tau, N^{u^*}_{\tau}) + \int_{t}^{\tau} F(s, N^{u^*}_{s}, u^*_{s}) \, ds \right] \, .$$

Repeating the steps from above (i.e. applying Itô's lemma, taking expectations, and the limit as  $h \searrow 0$  we find that

$$\partial_t H(t,n) + \mathcal{L}_t^{u^*} H(t,n) + F(t,n,u^*) = 0.$$

Combining this result with  $(5.34)$ , we arrive at the DPE (also known in this context as the Hamilton–Jacobi–Bellman equation)

$$\begin{cases} \partial_t H(t,n) + \sup_{u \in \mathcal{A}_t} \left( \mathcal{L}_t^u H(t,n) + F(t,n,u) \right) = 0 \,, \\ H(T,n) = G(n) \,. \end{cases} \tag{5.35}$$

The terminal condition follows from the observation that the integral in the optimisation problem (5.24) vanishes as  $t \nearrow T$ . Recall that the generator  $\mathcal{L}_t^u$  for the controlled process acts as follows:

$$\mathcal{L}_t^u H(t,n) = \lambda(t,n,u) \left[ H(t,n+1) - H(t,n) \right] \, .$$

As in the diffusion case, the optimisation of the control in  $(5.35)$  is only over its value at time  $t$ , rather than over the whole path of the control. Hence, it appears that the optimal control can be obtained pointwise. Treating the value function as known, the optimal control can often be found in **feedback control** form in terms of the value function itself. Substituting the feedback control back into  $(5.35)$  typically results in non-linear PDEs. In this Poisson case, the supremum in  $(5.35)$  has a very simple form since

$$\sup_{u \in \mathcal{A}_t} \left( \mathcal{L}_t^u H(t,n) + F(t,n,u) \right)$$
  
= 
$$\sup_{u \in \mathcal{A}_t} \left\{ \lambda(s,n,u) \left[ H(t,n+1) - H(t,n) \right] + F(t,n,u) \right\},$$

and hence, if  $F = 0$ , the optimal choice of the control is to make  $\lambda(s, n, u)$ as large as possible if  $H(t, n + 1) - H(t, n) > 0$  and as small as possible if  $H(t,n+1)-H(t,n) < 0.$  Such controls are called **bang-bang controls** because the quantity being controlled (in this case the intensity) reaches its extremal points. To make the problem more interesting we either need to (i) include a running reward/penalty (i.e.  $F \neq 0$ ) or, more interestingly (and relevant), (ii) introduce another stochastic process which is driven by the counting process, and therefore controlled indirectly, and have this stochastic process affect the agent's terminal and running rewards.

## Using the Poisson Process to Drive a Secondary Controlled $\text{Process}$

One such way to do this, which will also appear in later chapters as a result of optimisation problems in algorithmic trading, is to let  $(X_t^u)_{0 \le t \le T}$  denote a controlled process satisfying the SDE

$$dX_t^u = \mu(t, X_t^u, N_t^u, u_t) dt + \sigma(t, X_{t^-}^u, N_{t^-}^u, u_t) dN_t^u.$$
 (5.36)

In this manner, the counting process  $N^u$  acts as the source of jumps in  $X^u$ , and the control  $u$  may modulate the size of those jumps as well as the drift of the  $X$  $process - in addition to the arrival rate of the jumps themselves.$ 

In this more general context, the performance criteria can depend on both  $N$ and  $X$ . Specifically, let

$$H(t,x,n) := \sup_{u \in \mathcal{A}} H^u(t,x,n), \quad \text{and} \tag{5.37a}$$

$$H^{u}(t,x,n) := \mathbb{E}_{t,x,n} \left[ G(X^{u}_{T},N^{u}_{T}) + \int_{t}^{T} F(s,X^{u}_{s},N^{u}_{s},u_{s}) ds \right], \qquad (5.37b)$$

where  $\mathbb{E}_{t,x,n}[\cdot]$  denotes expectation conditional on  $N_{t^-} = n$  and  $X_{t^-} = x$ . Following the same arguments as in the previous sections, the DPP for this problem can be written as

$$H(t,x,n) = \sup_{u \in \mathcal{A}} \mathbb{E}_{t,x,n} \left[ H(\tau, X^u_\tau, N^u_\tau) + \int_t^\tau F(s, X^u_s, N^u_s, u_s) \, ds \right], \quad (5.38)$$

and a  $DPE$  can be derived to find

$$\begin{cases} \partial_t H(t,x,n) + \sup_{u \in \mathcal{A}} \left( \mathcal{L}_t^u H(t,x,n) + F(t,x,n) \right) = 0 \,, \\ H(T,x,n) = G(x,n) \,. \end{cases} \tag{5.39}$$

Here, the infinitesimal generator  $\mathcal{L}_t^u$  acts as follows:

$$\mathcal{L}_t^u H(t, x, n) = \mu(t, x, n, u) \, \partial_x H(t, x, n) + \lambda(t, x, n, u) \left[ H(t, x + \sigma(t, x, n, u), n+1) - H(t, x, n) \right] .$$

Notice that the control appears in both the intensity factor and in the difference operator, and there is a partial derivative with respect to the state variable  $x$ . This represents the trade-off between increasing/decreasing intensity through the control and what that change does to the process  $X_t^u$ , as well as what the control does to the drift.

# Example: Maximising Expected Wealth using Round-Trip Trades

Here, we provide an example of an agent who uses a market order  $(MO)$  to purchase one share at the best offer and then seeks to unwind her position by posting a limit order (LO) at the midprice plus the depth  $u$  which she controls. She repeats this operation over and over again until a future date  $T$ . Her cost from acquiring the share is  $S_t + \Delta/2$ , where  $\Delta$  is the spread between the best bid and best ask and is assumed constant, and since  $S_t$  is the midprice, the best ask is resting in the LOB at  $S_t + \Delta/2$ . The revenue from selling (if her LO is lifted by an MO) is  $S_t + u_t$ . Therefore, the wealth that is accrued to the agent from this round-trip trade is  $u_t - \Delta/2$ .

There is, however, no guarantee that the sell LO will be filled, and in this case the agent's wealth X satisfies (5.36) with *µ.* = 0 and *CTf* = (ut -% ) so that

$$dX_t^u = \left(u_t - \frac{\Delta}{2}\right) dN_t^u.$$

Here Nt counts the number of round-trip trades that the agent has completed up until time *t.* The agent controls the intensity of this counting process because the larger she chooses u, the lower is the probability of her LO being filled.

There are many ways in which we can model the probability of the LO being filled given how deep in the LOB the agent posts the order. We need two ingredients. First, we need to assume an arrival rate for the buy MOs that are sent by other market participants. Here we assume, for simplicity, that this rate is a constant A > 0. The other ingredient is the probability of the LO being filled conditional on the MO arriving. A popular choice in the literature is to assume that when posted u 2> 0 away from the midprice, the probability of being filled, given that an MO arrives, is P(u) = e-,rn,, and another is *P(v.)* = (1 + K.?Lt)-*1,*  where *r;.* and I are positive constants. Putting these ingredients together gives us two choices to model the fill probability: Af = e-" u, A and At = (1 + *r;.* ?Lt)-, A.

To solve the agent's optimisation problem we use the performance criteria and value function as in (5.37) with *F* = 0 and *G(x, n)* = *x.* If we assume that the fill rate is At = e-"u, A, the DPE becomes

$$\partial_t H + \sup_{u \ge 0} \Lambda \, e^{-\kappa \, u} \left( H(t, x + \left( u - \frac{1}{2} \Delta \right), n+1) - H(t, x, n) \right) = 0 \,,$$

subject to *H(T, x,* n) = *x.* Since there is no explicit dependence on *n* itself, we can assume *H(t, x,* n) = *h(t, x)* so the value function depends solely on wealth and time. Furthermore, due to the linear nature of the problem, we can further write *h(t, x)* = *x* + g(t) for some deterministic function g(t) with terminal condition g(T) = 0. Hence, the above reduces to

$$\partial_t g + \sup_{u \ge 0} \Lambda \, e^{-\kappa u} \left( u - \frac{1}{2} \Delta \right) = 0 \,. \tag{5.40}$$

This shows that the optimal control is independent of t, *x* and *n.* In particular,

$$u^* = \operatorname*{argmax}_{u \ge 0} \left\{ e^{-\kappa u} \left( u - \frac{1}{2} \Delta \right) \right\},\,$$

and it is straightforward to show that

$$u^* = \frac{1}{2}\Delta + \frac{1}{\kappa} \, .$$

It is not difficult to check that this is indeed a maximum and not a minimum, and upon substituting the feedback control (which in this case is just a constant) back into (5.40), we find that g satisfies

$$\partial_t g + \frac{\Lambda}{\kappa} \, e^{-\kappa \left(\frac{1}{2}\Delta + \frac{1}{\kappa}\right)} = 0 \, .$$

The value function is therefore given by the very compact expression

$$H(t,x,n) = x + \frac{\Lambda}{\kappa} e^{-\kappa \left(\frac{1}{2}\Delta + \frac{1}{\kappa}\right)} (T-t).$$

The optimal posting strategy  $(5.4.2)$  has a simple interpretation. The agent must recover the half-spread cost she incurred when using an MO to acquire the asset, and this is given by  $\frac{1}{2}\Delta$  in the optimal posting (5.4.2). In addition she posts further away from the midprice by an amount which maximises how much deeper her posting can rest in the book, given the probability of being filled, and this is the term  $\frac{1}{\kappa}$ .

The strategy derived here is optimal, but naive because it is a result of our simplifying assumptions in the way we model the state variables, and the simple performance criteria employed by the agent. For instance, this strategy does not make any adjustments to the optimal posting based on important quantities and costs such as: accumulated inventory, wealth, remaining time to trade, and adverse selection costs. The economic principles that underpin the link between these quantities and costs to the optimal postings were discussed in Chapter 2. In the latter parts of this book we incorporate these issues in the trading strategies when developing algorithms where the agent maximises profits executing roundtrip trades in a more realistic and general setting than the one developed here.

#### 5.4.3 Combined Diffusion and Jumps

As already hinted above, there are many situations in which the agent is exposed to more than one source of uncertainty. Typically, an agent is faced with control problems where both diffusive and jump uncertainty appear, and she may be able to control all or only parts of the system. Such scenarios will appear in several of the algorithmic trading problems that arise in the sections ahead and here we simply state the main results for a fairly general class of models.

First, let  $N^u = (N^u_t)_{0 \le t \le T}$  denote a collection of counting processes (of dim p) with controlled intensities  $\lambda^u = (\lambda^u_t)_{0 \le t \le T}$ , and let  $u = (u_t)_{0 \le t \le T}$ denote the control processes (of dim m). Furthermore, let  $W = (W_t)_{0 \le t \le T}$ denote a collection of independent Brownian motions (of dim m). Next, let  $X^u =$  $(X_t^{\boldsymbol{u}})_{0 \le t \le T}$  denote the controlled processes (of dim m) which will appear directly in the agent's performance criteria. If one (or more) of the counting processes  $N_t^i$  should appear in the performance criteria or in the dependence in  $\mu_t^u$ ,  $\sigma_t^u$ and/or  $\gamma_t^u$ , shown below, then take  $X_t^j = N_t^i$  for some j, i.e. include it through one of the components in X. We next assume that the controlled  $X^u$  processes  $\text{satisfy the SDEs}$ 

$$dX_t^{\boldsymbol{u}} = \boldsymbol{\mu}_t^{\boldsymbol{u}} dt + \boldsymbol{\sigma}_t^{\boldsymbol{u}} dW_t + \boldsymbol{\gamma}_t^{\boldsymbol{u}} dN_t^{\boldsymbol{u}}.$$
 (5.41a)

With a slight abuse of notation we write the controlled drift, volatility and jump

size as

$$\boldsymbol{\mu}_t^{\boldsymbol{u}} := \boldsymbol{\mu}(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t), \qquad (m \times 1 \text{ vector}), \qquad (5.41b)$$

$$\boldsymbol{\sigma}^{\boldsymbol{u}}_t := \boldsymbol{\sigma}(t, \boldsymbol{X}^{\boldsymbol{u}}_t, \boldsymbol{u}_t), \qquad (m \times m \text{ matrix}), \qquad (5.41c)$$

$$\boldsymbol{\gamma}_t^{\boldsymbol{u}} := \boldsymbol{\gamma}(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t), \qquad (m \times p \text{ matrix}). \qquad (5.41\text{d})$$

Furthermore, we assume that the controlled intensity takes the form

$$\lambda_t^{\boldsymbol{u}} := \boldsymbol{\lambda}\left(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t\right) \,. \tag{5.41e}$$

The modelling approach above implies that the agent can control, in general, the drift, volatility, jump size and jump arrivals. Precisely how much control she has depends on the specific form of the various functions appearing in  $(5.41b)$ ,  $(5.41c)$ ,  $(5.41d)$  and  $(5.41e)$ .

The agent's performance criteria is given by

$$H^{\boldsymbol{u}}(t,\boldsymbol{x}) = \mathbb{E}_{t,\boldsymbol{x}} \left[ G\left(\boldsymbol{X}^{\boldsymbol{u}}_{T}\right) + \int_{t}^{T} F\left(s, \boldsymbol{X}^{\boldsymbol{u}}_{s}, \boldsymbol{u}_{s}\right) \, ds \right] \,, \tag{5.42a}$$

and the value function is then given by the usual expression

$$H(t, \boldsymbol{x}) = \sup_{\boldsymbol{u} \in \mathcal{A}_{[t,T]}} H^{\boldsymbol{u}}(t, \boldsymbol{x}). \tag{5.42b}$$

Repeating the analysis along similar lines to the previous sections, we arrive at the DPP for the combined problem.

THEOREM 5.4 Dynamic Programming Principle for Jump-Diffusions. The value function  $(5.42)$  satisfies the DPP

$$H(t,\boldsymbol{x}) = \sup_{\boldsymbol{u}\in\mathcal{A}_{[t,T]}} \mathbb{E}_{t,\boldsymbol{x}} \left[ H(\tau,\boldsymbol{X}_{\tau}^{\boldsymbol{u}}) + \int_{t}^{\tau} F(s,\boldsymbol{X}_{s}^{\boldsymbol{u}},\boldsymbol{u}_{s}) \, ds \right] \,, \tag{5.43}$$

for all  $(t, x) \in [0, T] \times \mathbb{R}^m$  and all stopping times  $\tau \leq T$ .

Moreover, following similar arguments as before, one can develop a DPE

$$\begin{cases} \partial_t H(t, \boldsymbol{x}) + \sup_{\boldsymbol{u} \in \mathcal{A}_t} \left( \mathcal{L}_t^{\boldsymbol{u}} H(t, \boldsymbol{x}) + F(t, \boldsymbol{x}, \boldsymbol{u}) \right) = 0 \,, \\ H(T, \boldsymbol{x}) = G(\boldsymbol{x}) \,, \end{cases} \tag{5.44}$$

where the infinitesimal generator  $\mathcal{L}^{\boldsymbol{u}}_t$  acts as follows:

$$\begin{split} \mathcal{L}_t^{\boldsymbol{u}} H(t,\boldsymbol{x}) &= \boldsymbol{\mu}(t,\boldsymbol{x},\boldsymbol{u}) \cdot \boldsymbol{D}_{\boldsymbol{x}} H(t,\boldsymbol{x}) + \frac{1}{2} \boldsymbol{\sigma}(t,\boldsymbol{x},\boldsymbol{u}) \boldsymbol{\sigma}(t,\boldsymbol{x},\boldsymbol{u})' \boldsymbol{D}_{\boldsymbol{x}}^2 H(t,\boldsymbol{x}) \\ &+ \sum_{j=1}^p \lambda_j(t,\boldsymbol{x},\boldsymbol{u}) \left[ H(t,\boldsymbol{x} + \boldsymbol{\gamma}_{\cdot j}(t,\boldsymbol{x},\boldsymbol{u})) - H(t,\boldsymbol{x}) \right] \,, \end{split}$$

where  $\gamma_{,i}$  denotes the vector corresponding to the  $j^{th}$  column of  $\gamma$ ,  $D_x H$  represents the vector of partial derivatives with respect to x, and  $D_x^2H$  represents the matrix of (mixed) second order partial derivatives with respect to  $x$ .

The various terms in the generator can be easily interpreted: in the first line, the first term represents the ( controlled) drift of *X,* and the second term represents the (controlled) volatility of *X;* in the second line, the intensity for each counting process is shown separately, and each term in the sum has the ( controlled) rate of arrival of that jump component through A<sup>j</sup> , the difference terms that appear are due to the jump arriving and causing that component of *N* to increment, and simultaneously cause (potentially all components of) *X* to jump by r-;·

### 5.5 Optimal Stopping

In many circumstances the agent wishes to find the best time at which to enter or exit a given strategy. The classical finance example of this is the 'American put option' in which an agent who owns the option has the right, at any point in time up to, and including, the maturity date *T,* to exercise the option by receiving the amount of cash K in exchange for the underlying asset. The net cash value of this transaction at the exercise date Tis *(K* -S<sup>T</sup> ). Naturally, the agent will not exercise when ST > *K,* hence the effective payoff is *(K* -S<sup>T</sup> )<sup>+</sup> where (·)+ = max(·, 0). This simple observation provides only a trivial part of the strategy: to determine the full strategy, the agent seeks the stopping time *<sup>T</sup>*which maximises the discounted value of the payoff, i.e. she searches for the stopping time which attains the supremum (if possible)

$$\sup_{\tau \in \mathcal{T}} \mathbb{E} \left[ e^{-r\tau} \left( K - S_{\tau} \right)_+ \right] \,,$$

where Tare the F-stopping times bounded by *T.* This is just one of many such problems, and in general, problems which seek optimal stopping times are called optimal stopping problems. Similar to optimal control problems, optimal stopping problems admit a DPP and have an infinitesimal version, i.e. a DPE. In this section we provide a concise outline of the DPP and DPE for optimal stopping problems.

Rather than first developing the diffusion case, then the jump, and then the jump-diffusion, here we begin immediately with a fairly general jump-diffusion model. For this purpose, let X = (X t)o<t<T denote a vector-valued process of dim m satisfying the SDE

$$d\boldsymbol{X}_{t} = \boldsymbol{\mu}(t, \boldsymbol{X}_{t}) dt + \boldsymbol{\sigma}(t, \boldsymbol{X}_{t}) d\boldsymbol{W}_{t} + \boldsymbol{\gamma}(t, \boldsymbol{X}_{t}) d\boldsymbol{N}_{t},$$

whereµ: [O,T] X IR<sup>m</sup>H IR<sup>m</sup>, a: [O,T] X IR<sup>m</sup>H IR<sup>m</sup>X IR<sup>m</sup>, 1: [O,T] X IR<sup>m</sup><sup>H</sup> IR<sup>m</sup>x IR<sup>m</sup>, Wis an m-dimensional Brownian motion with independent components, and N is an m-dimensional counting process with intensities *>..(t,* Xt) The filtration *F* is the natural one generated by *X,* and the generator of the process  $\mathcal{L}_t$  acts on twice differentiable functions as follows:

$$\begin{split} \mathcal{L}_t h(t,x) &= \mu(t,x) \cdot D_x h(t,x) + \frac{1}{2} \boldsymbol{T} \boldsymbol{r} \boldsymbol{\sigma}(t,x) \boldsymbol{\sigma}(t,x') D_x^2 h(t,x) \\ &+ \sum_{j=1}^p \lambda_j(t,x) \left[ h(t,x+\gamma_{\cdot j}(t,x)) - h(t,x) \right] \,. \end{split}$$

Recall that  $D_x h$  represents the vector of partial derivatives with respect to x, and  $D_x^2 h$  represents the matrix of (mixed) second order partial derivatives with respect to  $x$ .

The agent then has a performance criterion, for each  $\mathcal{F}$ -stopping time  $\tau \in$  $\mathcal{T}_{[t,T]}$ , given by

$$H^{\tau}(t, \boldsymbol{x}) = \mathbb{E}_{t, \boldsymbol{x}} \left[ G(\boldsymbol{X}_{\tau}) \right] , \qquad (5.45a)$$

where  $G(\mathbf{X}_{\tau})$  is the reward upon exercise, and she seeks to find the value function

$$H(t, \boldsymbol{x}) = \sup_{\tau \in \mathcal{T}_{[t, \mathcal{T}]} } H^{\tau}(t, \boldsymbol{x}) \,, \tag{5.45b}$$

and the stopping time  $\tau$  which attains the supremum if it exists. At first glance, it appears that we have omitted the running reward/penalty  $\int_t^{\tau} F(s, \boldsymbol{X}_s) ds$  that we included when studying optimal control. Such terms can, however, be cast into the above form by choosing one of the components of  $X$ , say  $X^1$ , to satisfy

$$dX_t^1 = F(t, X_t^2, \dots, X_t^m) dt,$$

and writing  $G(x) = x^1 + \tilde{G}(x^2,\ldots,x^m)$ . It is therefore no loss of generality to consider only terminal rewards. In the stochastic control case, we kept the explicit running reward/penalty since it traditionally appears there. Now it will prove more convenient to absorb the running reward/penalty in  $G$ . Similarly, we can incorporate discounting by introducing a second state process which equals the discount factor up to that point in time, and modify  $G$  accordingly.

From the posing of the stopping problem in  $(5.45)$ , intuitively, we see that the agent is attempting to decide between stopping 'now' and receiving the reward  $G$ , or continuing to hold off in hopes of receiving a larger reward in the future. However, on closer examination it seems clear that she should continue to wait at the point  $(t,x) \in [0,T] \times \mathbb{R}^m$  as long as the value function has not attained a value of  $G(x)$  there. This motivates the definition of the stopping region,  $\mathcal{S}$ , which we define as

$$\mathcal{S} = \left\{ (t, \boldsymbol{x}) \in [0, T] \times \mathbb{R}^m : H(t, \boldsymbol{x}) = G(\boldsymbol{x}) \right\}.$$

It should be evident that whenever  $(t,x) \in \mathcal{S}$ , i.e. if the state of the system lies in  $\mathcal{S}$ , it is optimal to stop immediately – since the agent cannot improve beyond G by the definition of the value function in  $(5.45)$ . The complement of this region,  $\mathcal{S}^c$ , is known as the **continuation region**. In this region, the agent can still improve her value and therefore continues to wait. Both regions can be generically visualised as in Figure  $5.3$ .

The difficulties in optimal stopping problems arise because the region  $\mathcal{S}$  (or

![](_page_24_Figure_1.jpeg)

Figure 5.3 A generic depiction of the continuation and stopping regions for the optimal stopping problem (5.45). A sample path is also shown and the red dot corresponds to the optimal time to stop.

equivalently its boundary 8S) must be solved simultaneously with the value function itself. Hence, the DPEs which arise in this context are free-boundary problems, also called obstacle problems, or variational inequalities. Such PDEs are more difficult to solve, and even very simple examples typically do not admit explicit solutions take for example the American put option when the underlying asset is a geometric Brownian motion. Nonetheless, a non-linear PDE is often enough to characterise the solution and many numerical schemes exist for solving them.

#### 5.5.1 The Dynamic Programming Principle

Reasoning along similar lines as before, we can show that the following DPP applies.

THEOREM 5.5 *Dynamic Programming Principle for Stopping Problems. The value function* (5.45) *satisfies the DPP* 

$$H(t, \boldsymbol{x}) = \sup_{\tau \in \mathcal{T}_{[t, T]}} \mathbb{E}_{t, \boldsymbol{x}} \left[ G(\boldsymbol{X}_{\tau}) \mathbbm{1}_{\tau < \theta} + H(\theta, \boldsymbol{X}_{\theta}) \mathbbm{1}_{\tau \ge \theta} \right], \qquad (5.46)$$

*for all* (t,x) E [O,T] x ]R<sup>m</sup>*and all stopping times 8::::; T.*

The intuition of this DPP is that if the optimal stopping time *T\** occurs prior to 8, then the agent's value function equals the reward at *T\*.* If, however, the agent has not stopped by 8, then at 8 she receives the value function evaluated at the current state of the system.

#### 5.5.2 Dynamic Programming Equation

As in the optimal control problems studied earlier, the DPP for optimal stopping can be recast in its infinitesimal version - a much more useful form for computation - i.e. it can be used to derive a DPE. This time, we state the result first and then provide the proof. We follow closely the proof in Touzi (2013) as it provides a nice alternative to the usual construction. It also opens the door for

the interested reader to move on to studying the viscosity solution approach to stochastic optimal control and optimal stopping, which relies heavily on the proof by contradiction approach taken here.

THEOREM  $5.6$ Dynamic Programming Equation for Stopping Prob**lems.** Assume that the value function  $H(t,x)$  is once differentiable in t and all second order derivatives in  $\boldsymbol{x}$  exist, i.e.  $H \in C^{1,2}([0,T],\mathbb{R}^m)$ , and that  $G:\mathbb{R}^m \mapsto$  $\mathbb{R}$  is continuous. Then H solves the **variational inequality**, also known as an obstacle problem, or free-boundary, problem:

$$\max\left\{\partial_t H + \mathcal{L}_t H, G - H\right\} = 0, \quad \text{on} \quad \mathcal{D}, \tag{5.47}$$

where  $\mathcal{D} = [0, T] \times \mathbb{R}^m$ .

*Proof* The proof is broken up into two steps by showing (on  $\mathcal{D}$ ) that (i) the left-hand side is first smaller than or equal to zero, and that (ii) by contradiction the left-hand side is also greater than or equal to zero. Therefore, equality must hold.

(i) First we establish that

$$\max\left\{\partial_t H + \mathcal{L}_t H, G - H\right\} \le 0, \quad \text{on} \quad \mathcal{D}.$$

To show this, first note that the constant stopping rule  $\tau = t$  is admissible. Therefore, the performance criteria on this constant rule equals  $G$  and we must have  $H > G$  so that  $G - H < 0$ .

Next, take any point  $(t_0, x_0) \in \mathcal{D}$ . We show that the desired inequality holds at this point. Consider the sequence of stopping times indexed by  $h > 0$ ,

$$\theta_h = \inf \left\{ t > t_0 \, : \, (t, ||\boldsymbol{X}_t - \boldsymbol{x}_0||) \notin [t_0, t_0 + h] \times 1 \right\},\,$$

where  $||\cdot||$  denotes the Euclidean norm. That is, we take a stopping time equal to the minimum of  $t_0 + h$  and the time it takes X to exit a ball of size 1 from its current position. As long as  $h < T - t_0$ , this is an admissible stopping time. Therefore, by taking  $\tau = t_0$ , the DPP (5.46) implies that

$$H(t_0, \boldsymbol{x}_0) \geq \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ H\left(\theta_h, \boldsymbol{X}_{\theta_h}\right) \right] \, .$$

We then expand the term under the expectation using Itô's lemma for jump- $\text{diffusions to write}$ 

$$\begin{split} &H\left(\theta_{h}, \boldsymbol{X}_{\theta_{h}}\right) \\ &= H(t_{0}, \boldsymbol{x}_{0}) \\ &+ \int_{t_{0}}^{\theta_{h}} \left\{\partial_{t}H(t, \boldsymbol{X}_{t}) + \mathcal{L}_{t}H(t, \boldsymbol{X}_{t})\right\} dt + \int_{t_{0}}^{\theta_{h}} \left(\boldsymbol{\sigma}(t, \boldsymbol{X}_{t}) \boldsymbol{D}_{x}H(t, \boldsymbol{X}_{t})\right)' d\boldsymbol{W}_{t} \\ &+ \sum_{j=1}^{p} \int_{t_{0}}^{\theta_{h}} \left[H\left(t, \boldsymbol{X}_{t} + \boldsymbol{\gamma}_{\cdot j}(t, \boldsymbol{X}_{t})\right) - H\left(t, \boldsymbol{X}_{t}\right)\right] d\widehat{\boldsymbol{N}}_{t}^{j}, \end{split}$$

where N t = *N* t - *J�* >..( *s, X* s) *ds* are the compensated versions of the counting process, and /.j denotes the l<sup>h</sup>column of T

Since the stopping time 0h is chosen so that the process *X* remains bounded by the ball of size 1 around x*0* plus the potential of a jump (which we assume bounded), it follows that the stochastic integrals with respect to both the Brownian motions and the compensated counting processes vanish under the expectation. Hence, we have

$$0 \geq \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ \int_{t_0}^{\theta_h} \left\{ \partial_t H(t, \boldsymbol{X}_t) + \mathcal{L}_t H(t, \boldsymbol{X}_t) \right\} dt \right] \, .$$

Dividing by hand taking h \i 0, in which case 01i \i h a.s. (since Xt will a.s. not hit the edge of the bounding ball), the Mean-Value Theorem implies that

$$\partial_t H(t,\boldsymbol{x}_0) + \mathcal{L}_t H(t_0,\boldsymbol{x}_0) \leq 0.$$

This completes the first part of the proof.

(ii) We next show by contradiction that

$$\max\left\{\partial_t H + \mathcal{L}_t H, G - H\right\} \ge 0, \quad \text{on} \quad \mathcal{D}.$$

If the above inequality does not hold on D, then there exists a point (to, x*0)* E D such that

$$G(t_0, x_0) - H(t_0, x_0) < 0$$
 and  $(\partial_t + \mathcal{L}_t)H(t_0, x_0) < 0$ . (5.48)

We show that (5.48) contradicts the DPP in (5.46). To this end, introduce a new function i.ps which approximates the value function near (to, xo) but locally dominates it:

$$\varphi_{\varepsilon}(t,\boldsymbol{x}) := H(t,\boldsymbol{x}) + \varepsilon \left( ||\boldsymbol{x} - \boldsymbol{x}_0||^4 + |t - t_0|^2 \right) \,, \quad \forall (t,\boldsymbol{x}) \in \mathcal{D} \,, \qquad \varepsilon > 0.$$

Under the assumption (5.48), for *E* > 0 but sufficiently small, there is a small neighbourhood around (to, xo) on which the value function is at least o larger than the reward G and for which the operator (8t + L<sup>t</sup> ) renders the approximation i.ps negative. More precisely, there exists h > 0 and c5 > 0 such that

$$H \geq G + \delta \quad \text{and} \quad (\partial_t + \mathcal{L}_t) \,\varphi_\varepsilon \leq 0 \quad \text{on} \quad \mathcal{D}_h := [t_0, t_0 + h] \times \mathcal{B}_h \,, \quad (5.49)$$

where Bh is a ball of size h around xo, i.e. Bh = *{x* E ]R<sup>m</sup>: llx - xoll � h} . Also, near (to, xo), i.ps is locally larger than *H,* hence,

$$-\zeta := \max_{\partial \mathcal{D}_h} (H - \varphi_{\varepsilon}) < 0, \qquad (5.50)$$

where 8Dh represents the boundary of the set Dh.

vVe now take a stopping time equal to the first time the process exits this ball:

$$\theta := \inf \left\{ t > t_0 : (t, \boldsymbol{X}_t) \notin \mathcal{D}_h \right\}.$$

Take a second stopping rule, this time arbitrary, *T* E Tft,TJ, and let '1/; = *TI\* 0. Then we have

$$H(\psi, \mathbf{X}_{\psi}) - H(t_0, \mathbf{x}_0)$$
  
=  $(H - \varphi_{\epsilon})(\psi, \mathbf{X}_{\psi}) + (\varphi_{\epsilon}(\psi, \mathbf{X}_{\psi}) - \varphi_{\epsilon}(t_0, \mathbf{x}_0))$ , (5.51)

since 4Jc and H coincide at (to, xo). From Ito's lemma, and the fact that *X* 1/i is bounded due to stopping the first time *X* exits the ball Bh, we have

$$\mathbb{E}_{t_0,x_0} \left[ \varphi_{\epsilon}(\psi\,,\,X_{\psi}) - \varphi_{\epsilon}(t_0,x_0) \right] = \mathbb{E}_{t_0,x_0} \left[ \int_{t_0}^{\psi} \left( \partial_t + \mathcal{L}_t \right) \varphi_{\varepsilon}(t,X_t) \, dt \right] \le 0 \,.$$

The diffusive and jump terms vanish because they are martingales, and the inequality follows from the second inequality in (5.49).

Hence, putting this together with (5.51), we have

$$\mathbb{E}_{t_0,\boldsymbol{x}_0}\left[H(\boldsymbol{\psi}\,,\,\boldsymbol{X}_{\boldsymbol{\psi}})-H(t_0,\boldsymbol{x}_0)\right] \leq \mathbb{E}_{t_0,\boldsymbol{x}_0}\left[(H-\varphi_{\varepsilon})(\boldsymbol{\psi}\,,\,\boldsymbol{X}_{\boldsymbol{\psi}})\right] \leq -\zeta\,\mathbb{P}(\tau\geq\theta)\,,$$

where the second inequality follows from (5.50). By rearranging to isolate H(to, xo), we have

$$H(t_0, \boldsymbol{x}_0) \ge \zeta \, \mathbb{P}(\tau \ge \theta) + \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ H(\psi, \, \boldsymbol{X}_\psi) \right]$$
  
=  $\zeta \, \mathbb{P}(\tau \ge \theta) + \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ H(\tau, \, \boldsymbol{X}_\tau) \mathbb{1}_{\tau < \theta} + H(\theta, \, \boldsymbol{X}_\theta) \mathbb{1}_{\tau \ge \theta} \right] \, .$ 

By the first inequality in (5.49), H 2'. G + 15 on D1i, so therefore

$$H(t_0, \boldsymbol{x}_0) \geq \zeta \, \mathbb{P}(\tau \geq \theta) + \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ \left( G(\boldsymbol{X}_{\tau}) + \delta \right) \mathbb{1}_{\tau < \theta} + H(\theta \,, \, \boldsymbol{X}_{\theta}) \mathbb{1}_{\tau \geq \theta} \right] \,,$$

where we have replaced H(T, X7) by its lower bound (G(XT) + 15) on { *T* < 0}, since in that event we are still in D1i. Finally, since lEt<sup>o</sup> ,xo []\_ <sup>T</sup> <0] = lP'(T < 0), we have

$$H(t_0, \boldsymbol{x}_0) \ge \zeta \, \mathbb{P}(\tau \ge \theta) + \delta \, \mathbb{P}(\tau < \theta) + \mathbb{E}_{t_0, \boldsymbol{x}_0} \left[ G(\boldsymbol{X}_{\tau}) \mathbb{1}_{\tau < \theta} + H(\theta, \boldsymbol{X}_{\theta}) \mathbb{1}_{\tau \ge \theta} \right] \, .$$

By the arbitrariness of *T* E 'Tft,TJ, and the fact that the constants added to the expectation above are positive, we arrive at a contradiction to the DPP (5.46) and the proof is complete.

D

The approximating function cp*6* in the second part of the above proof can be seen as an upper-semicontinuous approximation to the value function, and the viscosity solution approach makes heavy use of both upper and lower semicontinuous envelopes of the value function when it is not smooth enough to differentiate. We do not divert into these discussions here, and instead refer the interested reader to the excellent monographs Touzi (2013) as well as Pham (2010) and Fleming & Saner (2006).

It is worth briefly exploring the interpretation of the variational inequality appearing above, repeated here for convenience:

$$\max\left\{\partial_t H + \mathcal{L}_t H, G - H\right\} = 0, \text{ on } \mathcal{D}.$$

This really represents two possibilities: either we have

(i) 
$$\partial_t H + \mathcal{L}_t H = 0$$
 and  $H < G$ ,

or we have

(ii) 
$$H = G$$
 and  $\partial_t H + \mathcal{L}_t H < 0$ .

The first of these possibilities corresponds to the value function  $H$  being lower than the reward  $G$ , and in this region the value function satisfies a linear PDE. If we introduce the stochastic process  $h_t = H(t, \boldsymbol{X}_t)$ , then due to the linear PDE having zero right-hand side,  $h_t$  is a martingale. The region in which (i) holds is what we identified earlier as the continuation region  $\mathcal{S}^c$ , since it is suboptimal to stop there. The second of these possibilities corresponds to the value function H equalling the reward G, and hence occurs in the stopping region S. Moreover, the linear operator  $\partial_t + \mathcal{L}_t$  renders the value function negative. In this region, if we did not pin the value function to the reward, we see that the process  $h_t$ would be a supermartingale; however, pinning it to the reward constrains the process to become a martingale. Hence, we see that the stochastic process  $h_t$ corresponding to the flow of the value function is in fact a martingale on the entire  $\mathcal{D}$ .

#### 5.6 **Combined Stopping and Control**

There are many instances in which an agent wishes to solve a **combined opti**mal stopping and control problem  $-$  i.e. she wishes to solve simultaneously for the optimal timing and optimal strategy in order to maximise a reward. Such problems inherit features from both problem types and we will see that the resulting DPEs are in effect a combination of the HJB equation and variational inequality.

In this case, we adopt the modelling assumptions and notation from subsection 5.4.3 but repeat it here. First, let  $N^u = (N^u_t)_{0 \le t \le T}$  denote a collection of counting processes (of dim  $p$ ) with controlled intensities  $\lambda^u = (\lambda^u_t)_{0 \le t \le T}$ , and let  $\boldsymbol{u} = (\boldsymbol{u}_t)_{0 \le t \le T}$  denote the control processes (of dimension m). Furthermore, let  $W = (W_t)_{0 \le t \le T}$  denote a collection of independent Brownian motions (of dim m). Next, let  $X^u = (X_t^u)_{0 \le t \le T}$  denote the controlled processes (of dim m) which will appear directly in the agent's performance criteria. If one (or more) of the counting processes  $N_t^i$  should appear in the performance criteria or in the dependence in  $\boldsymbol{\mu}_{t}^{\boldsymbol{u}}, \boldsymbol{\sigma}_{t}^{\boldsymbol{u}}$  and/or  $\boldsymbol{\gamma}_{t}^{\boldsymbol{u}},$  shown below, then take  $X_{t}^{\boldsymbol{j}} = N_{t}^{\boldsymbol{i}}$  for some j. i.e. include it through one of the components in  $X$ . We next assume that the controlled  $X^u$  processes satisfy the SDEs

$$d\boldsymbol{X}_{t}^{\boldsymbol{u}} = \boldsymbol{\mu}_{t}^{\boldsymbol{u}} dt + \boldsymbol{\sigma}_{t}^{\boldsymbol{u}} d\boldsymbol{W}_{t} + \boldsymbol{\gamma}_{t}^{\boldsymbol{u}} d\boldsymbol{N}_{t}^{\boldsymbol{u}}.$$
 (5.52a)

With a slight abuse of notation we write the controlled drift, volatility and jump

size as

$$\boldsymbol{\mu}_t^{\boldsymbol{u}} := \boldsymbol{\mu}(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t), \qquad (m \times 1 \text{ vector}), \qquad (5.52b)$$

$$\boldsymbol{\sigma}^{\boldsymbol{u}}_t := \boldsymbol{\sigma}(t, \boldsymbol{X}^{\boldsymbol{u}}_t, \boldsymbol{u}_t), \qquad (m \times m \text{ matrix}), \qquad (5.52c)$$

$$\boldsymbol{\gamma}_t^{\boldsymbol{u}} := \boldsymbol{\gamma}(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t), \qquad (m \times p \text{ matrix}).$$
 (5.52d)

Furthermore, we assume that the controlled intensity takes the form

$$\lambda_t^{\boldsymbol{u}} := \boldsymbol{\lambda}\left(t, \boldsymbol{X}_t^{\boldsymbol{u}}, \boldsymbol{u}_t\right) \,. \tag{5.52e}$$

The modelling approach above implies that the agent can control, in general, the drift, volatility, jump size and jump arrivals. Precisely how much control she has depends on the specific form of the various functions appearing in  $(5.52b)$ ,  $(5.52c)$ ,  $(5.52d)$  and  $(5.52e)$ .

Next, the agent's performance criteria for a given admissible control  $\boldsymbol{u}$  and admissible stopping time  $\tau$  is given by

$$H^{\boldsymbol{u},\tau}(t,\boldsymbol{x}) = \mathbb{E}_{t,\boldsymbol{x}}\left[G\left(\boldsymbol{X}_{\tau}^{\boldsymbol{u}}\right)\right],\tag{5.53a}$$

and her value function is

$$H(t, \boldsymbol{x}) = \sup_{\tau \in \mathcal{T}_{[t,T]}} \sup_{\boldsymbol{u} \in \mathcal{A}_{[t,T]}} H^{\boldsymbol{u},\tau}(t, \boldsymbol{x}). \tag{5.53b}$$

In this manner, the agent selects a stopping rule, seeks the best strategy, and then selects the stopping rule which provides the best overall performance. As such, she is aiming to decide whether to stop 'now' and receive the reward at the point in state space to which her strategy took her, or wait and continue to control the process in hopes of receiving a better reward later on.

A DPP still applies in the current setting; however, now we must take care of both optimal stopping and control. Following similar arguments as in the previous sections we arrive at the following DPP.

Dynamic Programming Principle for Optimal Stopping THEOREM  $5.7$ and Control. The value function  $(5.53)$  satisfies the DPP

$$H(t,\boldsymbol{x}) = \sup_{\tau \in \mathcal{T}_{[t,T]}} \sup_{\boldsymbol{u} \in \mathcal{A}_{[t,T]}} \mathbb{E}_{t,\boldsymbol{x}} \left[ G(X_{\tau}^{\boldsymbol{u}}) \, \mathbb{1}_{\tau < \theta} + H(\theta, \boldsymbol{X}_{\theta}^{\boldsymbol{u}}) \, \mathbb{1}_{\tau \ge \theta} \right] \,, \tag{5.54}$$

for all  $(t, x) \in [0, T] \times \mathbb{R}^m$  and all stopping times  $\theta \leq T$ .

The intuition here is similar to the previous DPPs. If stopping has not yet occurred  $(\tau \geq \theta)$ , then the agent receives the value function at that point in time, at that point in state space, where the optimal control has driven her to. If stopping has already occurred  $(\tau < \theta)$ , then the agent has already received the reward, and her value equals the reward at the time it was paid, at the point in state space where the optimal control drove her to.

Next, we state the DPE arising in this class of problems.

THEOREM 5.8 *Dynamic Programming Equation for Stopping and Control Problems. Assume that the value function H(t, x) is once differentiable ·in t and all second order derivatives ·in x exist, i.e. H E* C 1 • <sup>2</sup>([O, *Tl,* ]R<sup>m</sup>), *and that G :* ]R<sup>m</sup>*H* IR *is continuo11,s. Then H solves the quasi-variational inequality (QVI),* 

$$\max\left\{\partial_t H + \sup_{\boldsymbol{u}\in\mathcal{A}_t} \mathcal{L}_t^{\boldsymbol{u}} H, \ G - H\right\} = 0, \quad \text{on} \quad \mathcal{D},\tag{5.55}$$

*where D* = [O, T] x lR<sup>m</sup> .

This is similar in spirit to the variational inequality (5.47) for the optimal stopping problem, but now contains an optimisation over the control process as well. The optimisation results in the equation becoming non-linear, as in the HJB equation (5.44), and hence the above equation is referred to as a quasi-variational inequality rather than a variational inequality.

We once again have the notion of a stopping region S and continuation region *s c ,* where

$$\mathcal{S} = \left\{ (t, \boldsymbol{x}) \in [0, T] \times \mathbb{R}^m : H(t, \boldsymbol{x}) = G(\boldsymbol{x}) \right\}.$$

The only difference is that in the continuation region *s c ,* the value function should satisfy an HJB equation

$$\partial_t H + \sup_{\boldsymbol{u}\in\mathcal{A}_t} \mathcal{L}_t^{\boldsymbol{u}} H = 0, \quad \text{on} \quad \mathcal{S}^c,$$

rather than a linear PDE as in the stopping problem.

# 5. 7 Bibliography and Selected Readings

Merton (1971), Bertsekas & Shreve (1978), Merton (1992), Yong & Zhou (1999), Chang (2004), Fleming & Soner (2006), 0ksendal & Sulem (2007), 0ksendal (2010), Pham (2010), Tonzi (2013).
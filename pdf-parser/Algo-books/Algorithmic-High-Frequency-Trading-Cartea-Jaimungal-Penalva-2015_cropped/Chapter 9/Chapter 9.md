# **9.1 Introduction**

Execution algorithms are designed to minimise the market impact of large orders. As discussed in the previous chapters, slicing and dicing parent orders into child orders is the main principle upon which most algorithms are devised. One source of uncertainty which determines the market impact of each child order is the volume of the child order relative to the volume that the market can bear at that point in time. To see why, consider executing one child order. If it is small, then the order will not walk beyond the best quotes in the limit order book (LOB) and it will have little or no temporary market impact. If the order size is considerable, then it may walk through several layers of the LOB and, therefore, receive poor execution prices relative to the midprice. Furthermore, to complete this description of order size and volume we must also ask whether any other orders are reaching the market at the same time or just prior to the arrival of the child order.

Over short-time scales (seconds), the impact of a market order (MO) depends on many factors where size, relative to what is displayed in the LOB, is key. But what traders see on the LOB might change by the time their orders reach the market. Even traders with access to ultra-fast technology are exposed to the risk of changes in the quantity and prices displayed by limit orders (LOs) because there is a delay between sending an MO and its execution. These changes are due to modifications in the provision of liquidity and the activity of liquidity takers. LOs may be cancelled or more may be added, thus the best quotes and/ or depth of the LOB change. Similarly, other MOs may arrive just before the agent's and deplete liquidity that was sitting in the LOB. Thus, the size of the agent's child order is relative to what the LOB can bear when all MOs amalgamate with that of the agent's on the liquidity taking side of the market.

Over long-time scales (minutes/hours), the accumulated orders sent by the agent can exert unusual one-sided pressure which may result in further adverse market impact. Ideally, an agent's strategy may avoid adverse over-tilting of the market order flow by devising algorithms that camouflage her orders. One way to do this is to choose a rate of trading which targets a predetermined fraction of the total volume traded over the time horizon of the strategy.

Here arc two strategies that aim at executing a number of shares equivalent to a fraction of:

- i. the rate at which other participants are sending MOs; and
- ii. the total volume that has been traded over the entire time horizon.

The rate and the total volume quantities are connected because total volume is the sum over the rate of trading, but the optimal execution strategy could be quite different in both cases. One simple approach to targeting (i) is to observe the volume traded over the last several seconds or minutes, and then trade a percentage of this volume over the next several seconds or minutes. Obviously this approach is not optimal because it does not address the problem of market impact when the agent's orders amalgamate with other orders.

Targeting (ii) is difficult because total volume traded, over the planned execution horizon, is not known ahead of time. Naturally, trading a percentage of the volume that has been traded over the last several seconds will also target (ii), although it may not be optimal.

Moreover, neither (i) nor (ii) is entirely compatible with the objective of completing the acquisition or liquidation of an order in full by the end of the trading horizon, because there is no guarantee that the sum of the fractions of volume traded will add up to the number of shares that the agent set out to acquire or liquidate.

Trading algorithms that target benchmarks based on volume are extensively used. One of the most popular benchmarks is the Volume Weighted Average Price, known as VWAP. This benchmark consists, as it name clearly suggests, in calculating

$$\text{VWAP}(T_1, T_2) = \frac{\int_{T_1}^{T_2} S_t \, dV_t}{\int_{T_1}^{T_2} dV_t} \,, \tag{9.1}$$

where ½ is the total volume executed up to time *t,* St is the mid price, and [T1, T2] is the interval over which VWAP is measured.

Targeting VWAP is challenging for it is difficult to know ahead of time how many shares will be traded over a period of time. Investors target VWAP because of their desire to ensure that when acquiring or liquidating a large position they obtain an average price close to what the market has traded over the same period of time. One way to target VWAP is to follow strategy (i) because targeting a fraction of the rate of trading at every instant in time ensures that the investor is tracking the average price. Ideally, if the investor's strategy smoothes the execution of the number of shares she wishes to execute over the planned time horizon and at the same time adamantly targets a fixed proportion of the rate at which other market participants are trading, then the average cost of the shares she executes will be close to VWAP.

In this chapter we show how to formulate and solve the agent's liquidation problem for (i) and (ii) in a way that is consistent with the overall goal of full

![](_page_2_Figure_1.jpeg)

**Figure 9.1** Trading volume, for both buy and sell orders, for INTC for Oct-Nov, ·2013 using 5 minute windows.

(or partial) liquidation - the acquisition problem is very similar. Strategies that target (i) are often called percentage of volume (POV) and we label strategies that target (ii) as percentage of cumulative volume (POCV).

An important source of risk when targeting POV and POCV is that one cannot anticipate the timing and volume of the arrival of other trader's MOs. This uncertainty introduces another dimension of risk into the execution problem. In Figure 9.1 we show the volume of trades (for both buy and sell orders) of INTC (Intel Corporation) using 5 minute windows for every trading day (which consists of 6.5 hours) of the fourth quarter of 2013. The panel on the left shows a heat-map of the data together with the median (second quartile), and first and third quartile estimates - note that we plot log(l + volume) because there are 5 minute windows with no trades so volume is zero. The panel on the right shows a functional data analysis (FDA) approach to viewing the data whereby the volumes are regressed against Legendre polynomials (the thin lines). The mean of the regression is then plotted as the solid blue line, which represents the expected ( or average) trading volume throughout the day for this ticker. The data are also shown using the dots. From the two pictures one observes that although volume exhibits a 'U'-shape pattern, high volumes at the start and end of the trading day and lower volume in the hours in between, there are days where realised traded volumes deviate from this intraday pattern.

Figure 9.2 uses the same data as Figure 9.1 but instead of the volume it shows the intensity of trades for both buy and sell orders. For each 5 minute window we calculate the intensity ,,\ as the number of trades that were made over that time window. The figure shows log(l + ..\) because there are 5 minute intervals where no MOs were sent. The panel on the left shows a heat-map of the data together with the median, and first and third quartile estimates. The panel on the right shows an FDA approach to viewing the data whereby the intensities are regressed against Legendre polynomials ( the thin lines). The mean of the regression is then plotted as the solid blue line, which represents the expected ( or average) trade intensity through the day. The data are also shown using the

![](_page_3_Figure_1.jpeg)

Figure 9.2 Trading intensity, for both buy and sell orders, for INTC for Oct-Nov, 2013 using  $5$  minute windows.

dots. As expected, the trading intensity follows a similar pattern to that of the volume shown in Figure  $9.1$ .

We structure this chapter as follows. In Section 9.2 we show how an agent optimally liquidates shares when her strategy targets a fraction of the speed of the rest of the market. We use simulations to show that targeting a fraction of POV can deliver an average execution price which is very close to VWAP. Section  $9.3$  shows how the agent liquidates shares and her strategy targets POCV. In Section 9.4 the agent modifies her strategy because her own and other market participants' rates of trading have a permanent effect on the midprice. Finally, Section 9.5 shows how to manage price risk through exponential utility when the  $\text{agent targets } \text{POV}.$ 

# 9.2 Targeting Percentage of Market's Speed of Trading

In this section we assume that the agent's execution strategy **targets** a percentage of the speed at which other market participants are trading, and we focus on the liquidation strategy with MOs only. The setup for optimal acquisition, as opposed to liquidation, is very similar. In the liquidation problem, the agent searches for an optimal liquidation speed, which we denote by  $\nu_t$ , to target a fraction  $\rho$  of the speed at which the overall market (excluding the agent) is trading. This is different from a strategy which caps the optimal liquidation speed to be at most a fraction of other market participant's speed of trading  $-$  this will become clear when we write down the agent's performance criteria. The agent's inventory  $Q^{\nu}$  satisfies the SDE

$$dQ_t^{\nu} = -\nu_t \, dt \,, \qquad Q_0^{\nu} = \mathfrak{N} \,.$$

Let  $\mu_t$  denote the speed at which all other market participants are selling shares using MOs. This rate of selling can be estimated by summing all shares that are executed over a small time window, and dividing by the time window.

We assume that the agent's speed of liquidation is not taken into account when calculating  $\mu_t$ . The case when the agent targets a percentage of the total order flow (including her own trades) is left as Exercise  $E.9.3$ . Therefore, since the agent's objective is to seek an optimal liquidation speed  $\nu_t$  which targets the POV  $\rho \mu_t$  at every instant in time, with  $0 < \rho < 1$ , her performance criteria and value function are

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,x,S,\mu,q} \left[ X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}) - \varphi \int_t^T (\nu_u - \rho \,\mu_u)^2 du \right] \tag{9.2}$$

and

$$H(t, x, S, \mu, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, \mu, q), \qquad (9.3)$$

respectively.

Here  $X^{\nu}_{T}$  is terminal cash,  $\alpha \geq 0$  is a liquidation penalty, and  $\varphi \geq 0$  is the target penalty parameter. In this setup, deviations from the target are penalised by  $\varphi \int_t^T (\nu_u - \rho \mu_u)^2 \ du$ , but this penalisation does not affect the cash process. High values of  $\varphi$  constrain the strategy to closely track the target  $\rho \mu_t$  at every instant in time, and low values of  $\varphi$  result in liquidation strategies which are more lax about tracking the POV target.

The agent's speed of trading  $\nu_t$  has both temporary and permanent impact on the price of the asset. We assume that the impacts are linear in  $\nu_t$ , so

$$dS_t^{\nu} = -b\,\nu_t\,dt + \sigma\,dW_t\,,\qquad \qquad S_0^{\nu} = S\,,\tag{9.4a}$$

$$\hat{S}_t^{\nu} = S_t^{\nu} - k\,\nu_t\,, \qquad \hat{S}_0^{\nu} = \hat{S}\,, \tag{9.4b}$$

$$dX_t^{\nu} = \hat{S}_t^{\nu} \nu_t dt, \qquad \qquad X_0^{\nu} = x, \qquad (9.4c)$$

with  $b \geq 0$  and  $k \geq 0$ . In this setup we assume that the order flow  $\mu_t$  from other agents does not affect the midprice process. In Section 9.4 we modify this assumption and have the order flow of all agents impacting the midprice.

## 9.2.1 Solving the DPE when Targeting Rate of Trading

We solve the agent's control problem  $(9.3)$  assuming that order flow of other agents  $\mu_t$  is Markov and independent of all other processes (specifically it is independent of the Brownian motion  $W_t$  which drives the midprice), and denote its infinitesimal generator by  $\mathcal{L}^{\mu}$ . The dynamic programming principle suggests that the value function should satisfy the DPE

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \partial_{SS} + \mathcal{L}^{\mu}\right) H + \sup_{\nu} \left\{ (S - k\nu) \,\nu \,\partial_x H - \nu \,\partial_q H - b\,\nu \,\partial_S H - \varphi \left(\nu - \rho \,\mu\right)^2 \right\} \,, \tag{9.5}$$

subject to the terminal condition  $H(T, x, S, \mu, q) = x + q(S - \alpha q)$ , and attains a supremum at

$$\nu^* = \frac{S\partial_x H - \partial_q H - b\,\partial_S H + 2\,\varphi\,\rho\,\mu}{2(k+\varphi)}\,. \tag{9.6}$$

To solve  $(9.5)$  we make the ansatz

$$H(t, x, S, \mu, q) = x + q S + h(t, \mu, q), \qquad (9.7)$$

which can be interpreted as the accumulated cash of the liquidation strategy, the marked-to-market book value of the inventory at the midprice, and the added value obtained from optimally liquidating the remaining shares  $(h(t,\mu,q)).$ 

Upon substituting the ansatz in  $(9.5)$  we obtain the following equation satisfied by  $h(t, \mu, q)$ :

$$0 = (\partial_t + \mathcal{L}^{\mu}) h + \frac{1}{4(k+\varphi)} (\partial_q h + b q - 2\varphi \,\rho \,\mu)^2 - \varphi \,\rho^2 \,\mu^2 \,, \tag{9.8}$$

subject to the terminal condition  $h(T,\mu,q) = -\alpha q^2$ . By observing that the terminal condition and the DPE  $(9.8)$  are at most quadratic in q, we use the ansatz

$$h(t, \mu, q) = h_0(t, \mu) + q h_1(t, \mu) + q^2 h_2(t, \mu). \tag{9.9}$$

With this ansatz, the optimal trading speed in feedback form reduces consider- $\text{ably to}$ 

$$\nu^* = \frac{1}{k+\varphi} \left\{ \left[ \varphi \,\rho \,\mu - \frac{1}{2} \,h_1(t,\mu) \right] - \left[ \frac{1}{2}b + h_2(t,\mu) \right] q \right\}.$$

Moreover, substituting back into the DPE, after straightforward (but tedious) manipulations, collecting terms in  $q$ , then setting each to zero, we find the problem reduces to solving the coupled system of equations

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_2 + \frac{\left(h_2 + \frac{1}{2}b\right)^2}{k + \varphi},\tag{9.10a}$$

$$0 = (\partial_t + \mathcal{L}^{\mu}) h_1 + \frac{h_1 - 2\varphi \rho \mu}{k + \varphi} \left( h_2 + \frac{1}{2} b \right) , \qquad (9.10b)$$

$$0 = (\partial_t + \mathcal{L}^{\mu}) h_0 + \frac{1}{4(k+\varphi)} (h_1 - 2\varphi \,\rho \,\mu)^2 - \varphi \,\rho^2 \,\mu^2 , \qquad (9.10c)$$

with terminal conditions  $h_2(T,\mu) = -\alpha$  and  $h_1(T,\mu) = h_0(T,\mu) = 0$ . Each equation is in fact a linear PDE with non-linear sources terms given by the solution to the other PDEs. These equations are also dependent in a constructive manner, i.e.  $h_2$  is independent of all others,  $h_1$  only depends explicitly on  $h_2$ , while  $h_0$  only depends on  $h_1$ . Therefore, they can be solved sequentially.

Now observe that equation (9.10a) for  $h_2$  contains no source terms dependent on  $\mu$  and its terminal condition is independent of  $\mu$ , hence the solution must also be independent of  $\mu$ , and it is given by

$$h_2(t,\mu) = -\left(\frac{T-t}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right)^{-1} - \frac{1}{2}b\,,\tag{9.11}$$

and since the optimal speed of trading does not depend on  $h_0$ , we do not need to solve (9.10c). What remains is to solve the PDE for  $h_1(t,\mu)$ . At this point, we instead simply assume we have solved for it and derive expressions for the optimal trading speed and the resulting optimal inventory trajectory. Once we

have these expressions, in the subsections ahead, we make some specific modelling assumptions and compute  $h_1$  explicitly as well as provide a probabilistic representation for the general case.

We can then express the optimal speed of trading as

$$\nu_t^* = \frac{1}{k+\varphi} \left[ \varphi \, \rho \, \mu_t - \frac{1}{2} \, h_1(t,\mu_t) \right] + \frac{Q_t^{\nu^*}}{(T-t)+\zeta} \,, \tag{9.12}$$

where the constant

$$\zeta = \frac{k + \varphi}{\alpha - \frac{1}{2}b}$$

The optimal speed of trading consists of two terms. The second term on the right-hand side of  $(9.12)$  is very similar to the strategy discussed in the optimal liquidation problems in Chapter 6. For instance, one can see that if in  $(6.27)$ we let the running inventory penalty parameter  $\phi = 0$ , we obtain the second term on the right-hand side of (9.12) with  $\varphi = 0$ . Therefore, one can view this term as the TWAP-like liquidation strategy (we refer to it as TWAP-like because only when  $\zeta = 0$  do we obtain TWAP). The first term on the right-hand side of  $(9.12)$  provides the volume corrections to the TWAP-like strategy. This correction depends on the POV target,  $\rho \mu_t$ , and on the function  $h_1(t,\mu)$  which encodes how the optimal strategy behaves given the dynamics of the volume process.

Before specifying the stochastic process for the rate of trading  $\mu_t$ , we comment on some general features of the POV strategy. The boundary condition  $h_1(T,\mu)=0$  implies that near the end of the trading horizon,  $(T-t)\ll 1$ , the optimal strategy behaves like

$$\nu_t^* = \frac{\varphi \,\rho}{k + \varphi} \,\mu_t + \frac{Q_t^{\nu^*}}{(T - t) + \zeta} \,,$$

and we can further examine two interesting limiting cases.

First, when  $\alpha \to \infty$ , so that the agent must execute all shares by the trading end,  $\zeta \to 0$ . For a fixed inventory level, the second term on the right-hand side in the equation becomes dominant as  $t$  approaches  $T$ . Hence, the agent ignores the POV constraint and instead focuses on using TWAP when approaching the end of the trading horizon. Note, however, that the inventory also flows as time evolves, so it is not clear if that term truly dominates near maturity. Below, once we solve for  $Q_t^{\nu^*}$ , we will see that indeed the POV constraint is ignored near maturity.

Second, if  $\alpha$  remains finite, but  $\varphi \to \infty$ , so that the agent heavily penalises trades that deviate from POV, then  $\zeta \to \infty$  and the strategy ignores the TWAPlike term, and trades at a rate of  $\rho \mu_t$  as expected. Naturally, these limits do not commute as they are contradictory objectives – unless the volume to be traded is exactly equal to  $\rho$  percentage of the total volume traded over the execution duration.

Armed with the optimal trading speed in  $(9.12)$ , we can obtain an expression for the optimal inventory to hold by solving for  $Q_t^{\nu^*}$ . Recall that  $dQ_t^{\nu^*} = -\nu_t^* dt$ , and hence,

$$dQ_t^{\nu^*} = -\tilde{h}_1(t,\mu_t) dt - \frac{Q_t^{\nu^*}}{(T-t) + \zeta} dt,$$

where

$$\tilde{h}_1(t,\mu) := \frac{1}{k+\varphi} \left[ \varphi \,\rho \,\mu - \frac{1}{2} \, h_1(t,\mu) \right]$$

The ODE above can be solved by introducing an integrating factor, by writing

$$\begin{split} Q_t^{\nu^*} &= e^{-\int_0^t ((T-s)+\zeta)^{-1} \, ds} \, q_t^{\nu^*} \\ &= e^{\log \frac{(T-t)+\zeta}{T+\zeta}} \, q_t^{\nu^*} = \frac{(T-t)+\zeta}{T+\zeta} \, q_t^{\nu^*} \, , \end{split}$$

and solving for the unknown process  $q_t^{\nu^*}$ . By direct computation we have that

$$\begin{split} dq_t^{\nu^*} &= e^{\int_0^t ((T-s)+\zeta)^{-1} \, ds} \left\{ ((T-t)+\zeta)^{-1} \, Q_t^{\nu^*} \, dt + dQ_t^{\nu^*} \right\} \\ &= -e^{\int_0^t ((T-s)+\zeta)^{-1} \, ds} \, \tilde{h}_1(t,\mu_t) \, dt \\ &= -\frac{T+\zeta}{(T-t)+\zeta} \, \tilde{h}_1(t,\mu_t) \, dt \,, \end{split}$$

and so

$$q_t^{\nu^*} - q_0 = -\int_0^t \frac{T+\zeta}{(T-s)+\zeta} \,\tilde{h}_1(s,\mu_s) \,ds \,.$$

Therefore, we can write

$$Q_t^{\nu^*} \frac{T+\zeta}{(T-t)+\zeta} - \mathfrak{N} = -\int_0^t \frac{T+\zeta}{(T-s)+\zeta} \,\tilde{h}_1(s,\mu_s) \,ds\,,$$

so that finally

$$Q_t^{\nu^*} = \left(1 - \frac{t}{T+\zeta}\right) \mathfrak{N} - \frac{1}{k+\varphi} \int_0^t \frac{(T-t)+\zeta}{(T-s)+\zeta} \left\{\varphi \,\rho \,\mu_s - \frac{1}{2} \,h_1(s,\mu_s)\right\} ds. \tag{9.13}$$

The optimal inventory to hold at any point in time has two components. The first term is a TWAP-like strategy. The second term controls for fluctuations in the market's trading rate. Now that we are equipped with this general framework for the optimal trading speed  $(9.12)$  and the optimal inventory to hold  $(9.13)$ , we proceed by specifying the volume dynamics and then solving for explicit formulae for the optimal speed of trading and the optimal inventory path.

![](_page_8_Figure_1.jpeg)

Figure 9.3 AAPL volume rates per minute from 10.00 to 10.30 on Jan 5, 2011. Estimation using  $30 \text{ sec}$  and  $10 \text{ sec}$ time windows.

### 9.2.2 Stochastic Mean-Reverting Trading Rate

Figure 9.3 shows the estimate of the volume rate of trading (per minute) for  $\text{AAPL}$  on Jan 5, 2011 from 10:00 to 10:30. The estimate is computed by counting the volume traded over 30 sec and 10 sec windows and scaling the counts to one minute. As the figure shows, a reasonable first order model is that traded volume comes in bursts of activity which persists for a while (seconds for instance) and then decays to zero. Thus, for an agent whose objective is to target the rate of trading over short-time horizons, we assume that the sell volume rate  $\mu_t$  is a mean reverting process which satisfies the SDE

$$d\mu_t = -\kappa \,\mu_t \,dt + \,\eta_{1+N_{t-}} \,dN_t \,, \tag{9.14}$$

where  $\kappa \geq 0$  is the mean reversion rate,  $N_t$  is a homogeneous Poisson process with intensity  $\lambda$ , and  $\{\eta_1, \eta_2, \dots\}$  are non-negative i.i.d. random variables with distribution function F, with finite first moment, independent of  $N_t$ . The solution to  $(9.14)$  is

$$\mu_t = e^{-\kappa t} \mu_0 + \int_0^t e^{-\kappa(t-u)} \eta_{1+N_u-} dN_u$$
$$= e^{-\kappa t} \mu_0 + \sum_{m=1}^{N_t} e^{-\kappa(t-\tau_m)} \eta_m , \qquad (9.15)$$

where  $\tau_m$  denotes the time of the  $m^{th}$  arrival of the Poisson process. As shown earlier in Figure 9.2, the arrival of trades follows a U-shaped pattern that can be incorporated in  $(9.14)$  by introducing a deterministic component in the drift of the process, but here, for simplicity, we assume that the trading rate always mean-reverts to zero. Although the order flow process mean-reverts to zero, its long-run expected value is not zero; indeed from  $(9.15)$  we have

$$\mathbb{E}[\mu_t] = e^{-\kappa t} \mu_0 + \int_0^t e^{-\kappa(t-u)} \mathbb{E}[\eta_1] \lambda \, dt$$
$$= e^{-\kappa t} \mu_0 + \frac{\lambda \mathbb{E}[\eta_1]}{\kappa} \left(1 - e^{-\kappa t}\right) \xrightarrow{t \to \infty} \frac{\lambda \mathbb{E}[\eta_1]}{\kappa} \, .$$

With order flow satisfying  $(9.14)$ , its infinitesimal generator acts on the value

function as follows:

$$\mathcal{L}^{\mu}H(t,S,\mu,q) = -\kappa\,\mu\,\partial_{\mu}H + \lambda\,\mathbb{E}\left[H(t,S,\mu+\eta,q) - H(t,S,\mu,q)\right]\,,\tag{9.16}$$

where the expectation is with respect to the random variable  $\eta$  with distribution function  $F$ .

We now find the solution  $h_1$  to (9.10b) with this model assumption. Since this model is of the affine type, and (9.10b) is linear in  $\mu$ , we expect the function  $h_1(t,\mu)$  to be linear in  $\mu$ . Specifically, we write

$$h_1(t,\mu) = \ell_0(t) + \ell_1(t)\,\mu\,,$$

for some deterministic functions of time  $\ell_0(t)$  and  $\ell_1(t)$ . The terminal condition  $h(T,\mu) = 0$  implies that we must also impose  $\ell_0(T) = \ell_1(T) = 0$ . When the generator (9.16) acts on  $h_1(t,\mu)$  we obtain

$$\mathcal{L}^{\mu}h_1(t,\mu) = -\kappa \,\mu \,\ell_1 + \psi \,\ell_1 \,,$$

where  $\psi = \lambda \mathbb{E}[\eta]$  so that equation (9.10b) becomes

$$0 = \left\{ \partial_t \ell_0 + \frac{h_2 + \frac{1}{2}b}{k+\varphi} \ell_0 + \psi \,\ell_1 \right\} + \left\{ \partial_t \ell_1 - \kappa \ell_1 + \frac{\ell_1 - 2\varphi\rho}{k+\varphi} \left( h_2 + \frac{1}{2}b \right) \right\} \,\mu \,.$$

To solve for  $\ell_0(t)$  and  $\ell_1(t)$  in the above equation, we observe that since the equation must hold for all  $\mu$ , the terms in braces must vanish individually. We first solve the ODE in the second set of braces and then use the expression for  $\ell_1$  to solve the ODE contained in the first set of braces.

For  $\ell_1$ , we solve

$$\partial_t \ell_1 - \kappa \ell_1 + \frac{\ell_1 - 2\varphi \rho}{k + \varphi} \left( h_2 + \frac{1}{2} b \right) = 0 \,,$$

using the integrating factor technique by multiplying it by the integrating factor

$$\exp\int \left(\frac{h_2(t) + \frac{1}{2}b}{k+\varphi} - k\right) dt = \left(\frac{T-t}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right) e^{-kt}$$

and after simple algebra and integrating between  $t$  and  $T$ , the ODE above reduces  $to$  solving

$$\int_t^T d\left(\left(\frac{T-u}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right) e^{-ku} \ell_1(u)\right) + \frac{2\varphi\rho}{k+\varphi} \int_t^T e^{-ku} du = 0.$$

Finally, using the boundary condition  $\ell_1(T) = 0$  we obtain

$$\ell_1(t) = 2 \varphi \rho \left( (T - t) + \zeta \right)^{-1} \frac{1 - e^{-\kappa (T - t)}}{\kappa} \,,$$

where recall that the constant  $\zeta = (k + \varphi)/(\alpha - \frac{1}{2}b)$ .

We proceed in a similar way to solve the ODE for  $\ell_0$  resulting from setting the

first set of braces to zero. First substitute the solution for  $\ell_1$  into the equation for  $\ell_0$ , then multiply the ODE through by the integrating factor

$$\exp\int \left(\frac{h_2 + \frac{1}{2}b}{k+\varphi}\right) dt = \left(\frac{T-t}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right) ,$$

and integrate between  $t$  and  $T$ , to obtain

$$\frac{1}{k+\varphi} \int_t^T d\left( (T-u+\zeta) \ \ell_0(u) \right) + \frac{2\psi\varphi\rho}{k+\varphi} \int_t^T \frac{1-e^{-k(T-u)}}{k} \ du = 0 \,,$$

with terminal condition  $\ell_0(T) = 0$ . Evaluating the explicit integral, we can then write

$$\ell_0(t) = 2 \varphi \rho \psi \left( (T - t) + \zeta \right)^{-1} \frac{e^{-\kappa (T - t)} - 1 + \kappa (T - t)}{\kappa^2}$$

Finally, substituting these results back into the optimal speed of trading in  $(9.12)$ , we have

$$\nu_t^* = \frac{1}{k+\varphi} \left[ \varphi \, \rho \, \mu_t - \frac{1}{2} \left( \ell_0(t) + \ell_1(t) \, \mu_t \right) \right] + \frac{Q_t^{\nu^*}}{(T-t) + \zeta} \,. \tag{9.17}$$

#### 9.2.3 Probabilistic Representation

In this section we show how to solve for the optimal liquidation strategy for the most general case, where we do not specify the particular process followed by the trading rate  $\mu_t$  and the only assumption is that it is Markov and independent of the Brownian motion driving the midprice. We establish this result by applying the Feynman-Kac Theorem to  $(9.10b)$ , which is the evolution equation for  $h_1(t,\mu)$ , and represent  $h_1$  as

$$\begin{split} h_1(t,\mu) \\ &= -\frac{2\,\varphi\,\rho}{k+\varphi}\,\mathbb{E}_{t,\mu} \left[ \int_t^T \exp\left\{ \frac{1}{k+\varphi} \int_t^u \left( h_2(s,\mu_s) + \frac{1}{2}b \right) \, ds \right\} \left( h_2(t,\mu_u) + \frac{1}{2}b \right) \mu_u \, du \right] \\ &= \frac{2\,\varphi\,\rho}{k+\varphi}\,\mathbb{E}_{t,\mu} \left[ \int_t^T \exp\left\{ -\frac{1}{k+\varphi} \int_t^u \left( \frac{T-s}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b} \right)^{-1} \, ds \right\} \left[ \frac{T-u}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b} \right]^{-1} \mu_u \, du \right] \\ &= \frac{2\,\varphi\,\rho}{k+\varphi}\,\mathbb{E}_{t,\mu} \left[ \int_t^T \exp\left\{ \log\left( \frac{T-s}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b} \right) \Big|_{s=t}^u \right\} \left[ \frac{T-u}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b} \right]^{-1} \mu_u \, du \right], \end{split}$$

where  $\mathbb{E}_{t,\mu}[\cdot]$  is shorthand notation for the conditional expectation  $\mathbb{E}[\cdot \mid \mu_t = \mu]$ . After a series of cancellations in the integrand above, we have the following

compact representation for the solution to  $h_1(t,\mu)$ :

$$h_1(t,\mu) = 2\varphi \rho \frac{\int_t^T \mathbb{E}\left[\mu_u \mid \mu_t = \mu\right] du}{(T-t) + \zeta} \,. \tag{9.18}$$

Recall that the constant  $\zeta = (k + \varphi)/(\alpha - \frac{1}{2}b)$ . The integral appearing above

is precisely the **expected total volume** over the remainder of the trading horizon. This is because it is the integral of the expected trading rate  $\mu_t$  between the current time and the end of the strategy's trading horizon. Moreover, the integral term combined with the factor  $((T-t)+\zeta)^{-1}$  is approximately the average expected trading rate for the remaining time horizon. This combination would be exactly the average expected trading rate if  $k = \varphi = 0$  and/or  $\alpha \to \infty$ .

Using this general form for  $h_1$ , the agent's optimal trading speed can be represented as

$$\nu_t^* = \frac{\varphi \,\rho}{k + \varphi} \left[ \mu_t - \frac{\int_t^T \mathbb{E} \left[ \,\mu_u \mid \mathcal{F}_t^{\mu} \,\right] \, du}{(T - t) + \zeta} + \frac{Q_t^{\nu^*}}{(T - t) + \zeta} \right], \tag{9.19}$$

where the conditional expectation is now with respect to the filtration  $\mathcal{F}_t^{\mu}$  generated by  $\mu$ . By inserting the general result for  $h_1$  into the optimal inventory to hold, we also have the compact representation

$$Q_t^{\nu^*} = \left(1 - \frac{t}{T+\zeta}\right) \mathfrak{N}$$
$$- \frac{\varphi \,\rho}{k+\varphi} \int_0^t \frac{(T-t)+\zeta}{(T-s)+\zeta} \left[\mu_s - \frac{\int_s^T \mathbb{E}\left[\mu_u \mid \mathcal{F}_s^{\mu}\right] du}{(T-s)+\zeta}\right] ds. \tag{9.20}$$

To understand the intuition of the strategy  $(9.19)$  we start by pointing out that the agent's performance criteria  $(9.2)$  includes competing objectives. On the one hand the strategy aims at liquidating  $\mathfrak{N}$  shares by T, and on the other hand the strategy must track a fraction of other market participants' trading rate. Only when  $\mathfrak{N}$  is exactly equal to the desired fraction  $\rho$  of the total volume over the execution duration  $T$  are these two objectives compatible.

Next, rewrite the optimal trading speed as

$$\nu_t^* = \frac{\varphi}{k + \varphi} \,\rho \,\mu_t \tag{9.21a}$$

$$+\frac{1}{(T-t)+\zeta}\left(Q_t^{\nu^*}-\frac{\varphi\,\rho}{k+\varphi}\,\int_t^T\mathbb{E}[\,\mu_u\,|\,\mathcal{F}_t^{\mu}\,]\,du\right)\,. \tag{9.21b}$$

The first component of the strategy  $(9.21a)$  accounts for the trading rate that must be achieved to meet the POV target, taking into account the trade-off between the POV target penalty  $\varphi$  and the costs stemming from temporary price impact k. Although the POV target is  $\rho \mu_t$ , the strategy targets a lower amount since  $\frac{\varphi \rho}{k+\varphi} \leq \rho$ , where equality is achieved if the costs of missing the target are  $\varphi \to \infty$  and k remains finite, or there is no temporary impact  $k \downarrow 0$ .

The second component is a TWAP-like strategy (the first term in the braces in  $(9.21a)$  with a downward adjustment (the second term in the braces) because throughout the trading horizon there is the component targeting the POV. This is why we see that the TWAP-like strategy is applied to the remaining inventory  $Q_t^{\nu^*}$  minus the number of shares that are expected to be liquidated as part of the POV target, which will be done by the first term of the strategy  $(9.21a)$  over the remaining time of the strategy.

We continue our discussion of the optimal strategy by looking at some limiting cases.

The limiting case in which the agent wishes to always track a fraction  $\rho$  of the rate  $\mu_t$  is obtained by letting the target penalty parameter  $\varphi \to \infty$ . In this case, the liquidation speed and inventory path become

$$\nu_t^* \xrightarrow{\varphi \to \infty} \rho \mu_t \qquad \text{and} \qquad Q_t^{\nu^*} \xrightarrow{\varphi \to \infty} \mathfrak{N} - \rho \int_0^t \mu_s \, ds \,,$$

because  $\zeta \xrightarrow{\varphi \to \infty} \infty$ .

Regardless of what the inventory target is, the strategy liquidates at a rate of  $\rho\mu_t$ . Clearly, as shown by the inventory path, the strategy could liquidate an amount of shares which exceeds or falls short of the initial target  $\mathfrak{N}$ . When the strategy reaches  $T$  any outstanding shares, short or long, are liquidated with an MO at the midprice and receive a finite penalty of  $\alpha q_T^2$  which, in this limit, the agent prefers to picking up the more onerous running penalty which would be infinite if she did not liquidate at the rate  $\rho\mu_t$ .

The limiting case in which the agent wishes to fully liquidate her inventory leads to a finite trading strategy, with finite inventory paths. In particular,  $\zeta \xrightarrow{\alpha \to \infty} 0$ , and so we have

$$\begin{split}\n\nu_t^* &\xrightarrow{\alpha \to \infty} \frac{\varphi \,\rho}{k + \varphi} \left[ \mu_t - \frac{\int_t^T \mathbb{E} \left[ \mu_u \, | \, \mathcal{F}_t^{\mu} \right] \, du}{T - t} \right] + \frac{Q_t^{\nu^*}}{T - t}, \\
Q_t^{\nu^*} &\xrightarrow{\alpha \to \infty} \left( 1 - \frac{t}{T} \right) \, \mathfrak{N} - \frac{\varphi \,\rho}{k + \varphi} \int_0^t \frac{T - t}{T - s} \left[ \mu_s - \frac{\int_s^T \mathbb{E} \left[ \mu_u \, | \mathcal{F}_s^{\mu} \right] \, du}{T - s} \right] \, ds \, .\n\end{split}$$

Suppose that, in addition to requiring full liquidation, the agent is also very averse to trading at a rate different from  $\rho \mu_t$ . As  $\varphi$  increases, she will target more and more closely the required trading rate; however, due to the constraint that she must fully liquidate, she will not be able to match the required trading rate at all times. Therefore, in the limit in which  $\varphi \to \infty$ , after we have already taken  $\alpha \to \infty$ , the value function will become arbitrarily large and negative, and will not be finite. The limiting optimal strategy, however, does remain finite, as does her optimal inventory path, and the net value of liquidating her shares remains finite and well behaved. The optimal speed of trading and inventory position in this second double limiting case are

$$\lim_{\varphi \to \infty} \lim_{\alpha \to \infty} \nu_t^* = \rho \left[ \mu_t - \frac{\int_t^T \mathbb{E} \left[ \mu_u \, | \, \mathcal{F}_t^{\mu} \right] \, du}{T - t} \right] + \frac{Q_t^{\nu^*}}{T - t},$$
$$\lim_{\varphi \to \infty} \lim_{\alpha \to \infty} Q_t^{\nu^*} = \left( 1 - \frac{t}{T} \right) \mathfrak{N} - \rho \int_0^t \frac{T - t}{T - s} \left[ \mu_s - \frac{\int_s^T \mathbb{E} \left[ \mu_u \, | \, \mathcal{F}_s^{\mu} \right] \, du}{T - s} \right] \, ds.$$

Interestingly, when the other agents trade at a constant rate, i.e.  $\mu_t$  is a constant,

![](_page_13_Figure_1.jpeg)

Figure 9.4 Three sample paths of the market's trading rate, the optimal trading rate, the difference between the optimal trading rate and the targeted rate, and the agent's inventory.

the POV correction terms in the above cancel and the agent's strategy becomes TWAP.

### 9.2.4 Simulations

In this section we provide some simulations of the optimal strategy for the meanreverting volume model in subsection  $9.2.2$ . We focus on the double limiting case of first ensuring that all inventory is liquidated ( $\alpha \rightarrow \infty$ ), and second that the agent wishes to trade very close to POV ( $\varphi \to \infty$ ). In this case, we have

$$\lim_{\varphi \to \infty} \lim_{\alpha \to \infty} \nu_t^* = \rho \left[ \mu_t - \frac{\frac{1 - e^{-\kappa (T-t)}}{\kappa} \left( \mu_t - \frac{\psi}{\kappa} \right) + (T-t) \frac{\psi}{\kappa}}{(T-t)} \right] + \frac{Q_t^{\nu^*}}{T-t} \,,$$

where  $\psi = \lambda \mathbb{E}[\eta]$  and therefore the long-run expected trading rate is  $\mathbb{E}[\mu_t] = \psi/\kappa$ . For the simulations, we use the following modelling parameters:

 $S_0 = 20$ ,  $\sigma = 0.5$ ,  $T = 1$ ,

$$\mu_0 = \psi/\kappa, \quad \eta \sim \text{Exp}(10), \quad \lambda = 50, \quad \kappa = 20,$$

![](_page_14_Figure_1.jpeg)

**Figure 9.5** Left: histogram of the correlation between the agent's trading rate  $\nu_t^*$  and  $\mu_t$ . Right: histogram of the difference between the execution price per share and the VWAP.

 $k = 0.1$ ,  $b = 0.1$ , and  $\rho = 0.05$ .

We assume that the agent is attempting to liquidate  $\rho$  percentage of the volume she expects to arrive in the market over her trading horizon, thus  $\mathfrak{N} = \rho T \psi/\kappa$ 1.25. Our parameterisation of the exponential distribution is such that  $\mathbb{E}[\eta] = 10$ .

In Figure 9.4 we show three sample paths of the trading rate of other market participants  $\mu_t$ , the optimal trading rate  $\nu_t^*$ , the difference between the optimal rate and the target rate  $\nu_t^* - \rho \mu_t$ , and the agent's inventory  $Q_t^{\nu^*}$ . In the bottom left panel, the dotted line is the expected trading rate equal to  $\psi/\kappa$  and in the bottom right panel, the dotted line is TWAP. Note that  $\nu_t^*$  and  $\mu_t$  are strongly correlated. Indeed, in the left panel of Figure 9.5 we show the histogram of the correlation between  $\nu_t^*$  and  $\mu_t$  viewed as a time series, along 10,000 sample paths. The mean correlation is quite high at  $0.88$ , illustrating the fact that the trading rate tracks the rate of order flow. There are, however, deviations from the targeted rate of  $\rho \mu_t$ . These differences appear most notably towards the end of the trading horizon (as seen in the top right panel in Figure 9.4) where the agent's main concern is to drive her inventory to zero and she is less concerned about targeting other participants' trading rate.

Moreover, in the right panel of Figure 9.5 we show the difference between the executed price per share and the VWAP. As discussed in the introduction, if the agent is closely targeting a fraction  $\rho$  of the trading volume then this results in strategies which do indeed target VWAP on average. The deviation around VWAP is symmetric (skewness = 0.06) with mean  $-1.4 \times 10^{-4}$  and standard error  $\pm 3 \times 10^{-4}$ .

In Figure 9.6 we illustrate a heat-map of the agent's trading rate and her inventory. The dotted lines here indicate the  $5\%$ ,  $50\%$  and  $95\%$  quantiles. Interestingly, the median inventory path is TWAP, while the agent's inventory may deviate both above and below this trajectory in her attempt to match the POV target. The median path of her optimal trading rate is essentially constant through time, although the mode of this trajectory tends to increase towards

![](_page_15_Figure_1.jpeg)

Figure 9.6 Heat-maps of the optimal trading rate and inventory. The dotted lines show the  $5\%$ ,  $50\%$  and  $95\%$  quantiles.

maturity. This suggests there is a slight bias towards first trading a little more slowly compared with TWAP and then trading faster to catch up.

# 9.3 Percentage of Cumulative Volume

In this section we assume that the agent's execution strategy targets a percentage of **cumulative** volume (POCV) and the liquidation strategy relies on MOs only. Here the accumulated volume  $V$  of sell orders, excluding the agent's own trades, is given by

$$V_t = \int_0^t \mu_u \, du \,,$$

where as above  $\mu_t$  denotes other market participants' rate of trading.

The agent's performance criteria is now modified to

$$H^{\nu}(t,x,S,\mu,V,q) = \mathbb{E}_{t,x,S,\mu,V,q} \left[ X_T^{\nu} + Q_T^{\nu} \left( S_T^{\nu} - \alpha Q_T^{\nu} \right) - \varphi \int_t^T \left( (\mathfrak{N} - Q_u^{\nu}) - \rho \, V_u \right)^2 du \right], \tag{9.22}$$

where  $\mathfrak{N}$  is the number of shares that the agent wishes to liquidate by the terminal date  $T$ .

The running target penalty  $\varphi \int_t^T \left( (\mathfrak{N} - Q_u^{\nu}) - \rho V_u \right)^2 du$  is not a financial cost that the agent incurs. Rather, its purpose is to allow the agent to seek for optimal liquidation rates where the total amount that has been liquidated up to time  $t$ is not too far away from a percentage of what the entire market has sold. For example, when the penalty parameter  $\varphi \to \infty$ , the optimal strategy is forced to liquidate shares so that at any point in time the number of shares that have already been liquidated,  $\mathfrak{N}-q_t$ , equals  $\rho V_t$ . In this manner, the agent devises a strategy where the cumulative sum of her own sell MOs is a fraction  $0 < \rho < 1$ 

of the market. As in the last section, in this setup the agent's own trades are not taken into account in the accumulated volume.

As usual, the agent's value function is

$$H(t, x, S, \mu, V, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, \mu, V, q), \qquad (9.23)$$

and her cash process  $X^{\nu}$ , the controlled midprice  $S^{\nu}$ , and execution price  $\hat{S}^{\nu}$ satisfy the equations in  $(9.4)$ . Applying the dynamic programming principle suggests that the value function should satisfy the DPE

$$0 = \left(\partial_t + \mathcal{L}^{S,\mu,V}\right)H - \varphi((\mathfrak{N}-q) - \rho V)^2 + \sup_{\nu} \left\{-b\,\nu\,\partial_S H + (S-k\,\nu)\,\nu\,\partial_x H - \nu\,\partial_q H\right\} \,, \tag{9.24}$$

subject to the terminal condition  $H(T, x, S, y, q) = x + q(S - \alpha q)$ . Here,  $\mathcal{L}^{S, \mu, V}$ denotes the infinitesimal generator of the joint process  $(S_t, \mu_t, V_t)_{0 \le t \le T}$ . Moreover, we assume that the volume trading rate  $\mu_t$ , and therefore the total volume  $V_t$ , is independent of the asset's midprice.

The first order conditions provide us with the optimal trading rate in feedback  $\text{form as}$ 

$$\nu^* = \frac{1}{2k} \left( S \,\partial_x H - \partial_q H - b \,\partial_S H \right)$$

The terminal condition suggests that to solve  $(9.24)$  we use the ansatz

 $H(t, x, S, \mu, V, q) = x + qS + h(t, \mu, V, q)$  $(9.25)$ 

to obtain the following equation satisfied by  $h(t, \mu, V, q)$ :

$$0 = \left(\partial_t + \mathcal{L}^{\mu,V}\right)h + \frac{1}{4k}\left(\partial_q h + bq\right)^2 - \varphi\left(\mathfrak{N} - q - \rho V\right)^2\,,\tag{9.26}$$

subject to the terminal condition  $h(T) = -\alpha q^2$ , where  $\mathcal{L}^{\mu,V}$  denotes the generator of the process  $(\mu_t, V_t)_{0 \le t \le T}$  which excludes the midprice because the trading rate is independent of the midprice.

The above non-linear equation can be reduced even further by noticing that the equation and its terminal condition are at most quadratic in  $q$ , hence we use  $\text{the ansatz}$ 

$$h(t,\mu,V,q) = h_0(t,\mu,V) + h_1(t,\mu,V) q + h_2(t,\mu,V) q^2,$$

subject to the boundary conditions

$$h_0(T,\mu,V) = h_1(T,\mu,V) = 0$$
, and  $h_2(T,\mu,V) = -\alpha$ 

By substituting this ansatz into equation  $(9.26)$ , collecting terms with equal powers in q, and setting each to zero, we find that  $h_0$ ,  $h_1$ , and  $h_2$  must satisfy the coupled system of PIDEs

$$0 = \left(\partial_t + \mathcal{L}^{\mu,V}\right)h_2 + \frac{1}{k}\left(h_2 + \frac{1}{2}b\right)^2 - \varphi\,,\tag{9.27a}$$

 $0 = \left(\partial_t + \mathcal{L}^{\mu,V}\right)h_1 + \frac{1}{k}\left(h_2 + \frac{1}{2}b\right)h_1 + 2\varphi\left(\mathfrak{N} - \rho V\right),$  $(9.27b)$ 

$$0 = \left(\partial_t + \mathcal{L}^{\mu,V}\right)h_0 + \frac{1}{4k}\left(h_1\right)^2 - \varphi\left(\mathfrak{N} - \rho\,V\right)^2. \tag{9.27c}$$

As in the POV section, each equation above is a linear PIDE with non-linear source terms given by the solution to the other PIDEs. These equations are also dependent in a sequential manner, i.e. *h2* is independent of all others, h1 only depends explicitly on h*2,* while ho only depends on h<sup>1</sup> . Therefore, they can be solved sequentially.

Now observe that equation (9.27a) for h2 contains no source terms dependent on *V* and its terminal condition is independent of *V,* hence the solution must also be independent of V. Therefore, we must solve the Riccati equation

$$0 = \partial_t h_2 + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right)^2 - \varphi \,,$$

which can be solved explicitly, see (6.25) where we provide detailed steps to solve a similar ODE, resulting in

$$h_2(t) = \sqrt{k\varphi} \frac{1 + \zeta e^{2\xi(T-t)}}{1 - \zeta e^{2\xi(T-t)}} - \frac{1}{2}b,$$
(9.28)

where

$$\xi = \sqrt{\frac{\varphi}{k}}$$
 and  $\zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{k\varphi}}{\alpha - \frac{1}{2}b - \sqrt{k\varphi}}$ . (9.29)

vVhat remains is to solve for h1, which we defer for now, and instead focus on the form of the optimal trading speed, given its solution. Once we have these expressions, in the subsections ahead, we make some specific modelling assumptions and compute h1 explicitly as well as provide a probabilistic representation for the general case. As before, ho does not appear in the optimal control and, hence, we do not attempt to solve for it, although a closed-form expression can be obtained.

Substituting this result into the expression for the optimal liquidation rate above, we can now express the optimal speed of trading in feedback form as

$$\nu_t^* = -\frac{1}{2k} \left\{ h_1(t, \mu_t, V_t) + 2 \left( h_2(t) + \frac{1}{2} b \right) Q_t^{\nu^*} \right\}, \n$$
(9.30)

where h<sup>1</sup> (t,µ, *V)* is the solution to (9.27b) and h<sup>2</sup> (t) is given in (9.28).

Thus, the optimal speed of trading can be decomposed into two terms. The second term is similar to the AC-like solution already seen in (6.27) where the penalty on deviations from POCV plays the same role as the urgency parameter in the AC-like setting. The first term adjusts the strategy to account for the rate and volume of trades up to that point in time. Its specific form depends on the precise modelling assumptions onµ and V. In all cases, however, the importance of this term vanishes as *t* -+ *T* due to the terminal condition h1 (T, µ, *V)* = 0, and the agent trades more and more like the AC solution.

Recall that the inventory *Q(* at time *t* solves the equation *dQ(* = *-v; dt;* hence,

$$dQ_t^{\nu^*} = \frac{1}{2k} \left\{ h_1(t, \mu_t, V_t) + 2 \left( h_2(t) + \frac{1}{2} b \right) Q_t^{\nu^*} \right\} dt. \tag{9.31}$$

To explicitly solve this ODE, we first multiply  $(9.31)$  through by the integrating factor

$$\exp\left\{-\frac{1}{\kappa}\int\left(h_2(t)+\frac{1}{2}b\right) dt\right\} ,$$

and write the ODE as

$$d\left(e^{-\frac{1}{\kappa}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}Q_{t}^{\nu^{*}}\right) = e^{-\frac{1}{\kappa}\int\left((h_{2}(t)+\frac{1}{2}b)\right)dt}\frac{1}{2k}h_{1}(t,\mu_{t},V_{t})dt. \tag{9.32}$$

We use (9.28) and recall that  $\xi = \sqrt{\varphi/k}$  to calculate explicitly the integral appearing in the integrating factor:

$$\frac{1}{\kappa} \int \left( h_2(t) + \frac{1}{2} b \right) dt = \xi \int \frac{1 + \zeta e^{2\xi(T-t)}}{1 - \zeta e^{2\xi(T-t)}} dt$$

$$= \xi \int \frac{e^{-2\xi(T-t)}}{e^{-2\xi(T-t)} - \zeta} dt + \xi \int \frac{\zeta e^{2\xi(T-t)}}{1 - \zeta e^{2\xi(T-t)}} dt$$

$$= \frac{1}{2} \log \left[ \left( e^{-2\xi(T-t)} - \zeta \right) \left( 1 - \zeta e^{2\xi(T-t)} \right) \right]$$

$$= \frac{1}{2} \log \left[ e^{2\xi(T-t)} \left( e^{-2\xi(T-t)} - \zeta \right)^2 \right]$$

$$= \log \left[ e^{-\xi(T-t)} - \zeta e^{\xi(T-t)} \right], \tag{9.34}$$

and integrate  $(9.32)$  between 0 and t to obtain

$$Q_{t}^{\nu^{*}} = \frac{\zeta e^{\xi (T-t)} - e^{-\xi (T-t)}}{\zeta e^{\xi T} - e^{-\xi T}} \mathfrak{N} + \frac{1}{2k} \int_{0}^{t} \frac{\zeta e^{\xi (T-t)} - e^{-\xi (T-t)}}{\zeta e^{\xi (T-u)} - e^{-\xi (T-u)}} h_{1}(u, \mu_{u}, V_{u}) du.$$
(9.35)

In this representation, we can immediately see how the first term represents AC-like optimal holdings, while the second term accounts for fluctuations in trading volume. If we take the limit in which the agent penalises all strategies which do not completely liquidate her inventory, i.e.  $\alpha \to +\infty$ , then  $\zeta \to 1$ , and  $\text{SO}$ 

$$Q_t^{\nu^*} \xrightarrow{\alpha \to \infty} \frac{\sinh(\xi (T-t))}{\sinh(\xi T))} \mathfrak{N} + \int_0^t \frac{\sinh(\xi (T-t))}{\sinh(\xi (T-u))} \lim_{\alpha \to \infty} \frac{1}{2k} h_1(u, \mu_u, V_u) \ du.$$

Next we show the optimal speed of liquidation and inventory path for the particular case where volume follows a compound Poisson process. Later, in subsection  $9.3.2$ , we assume that volume increments are due to a trading rate that follows an OU-type process as in  $(9.14)$ . Finally in subsection  $9.3.3$  we provide a general solution where we do not require a specific functional form for the volume or trading rate. Thus, the next two subsections are particular cases of the more general solution derived in subsection  $9.3.3$ .

# 9.3.1 Compound Poisson Model of Volume

In subsection 9.2.2, we motivated the volume trading rate by Figure 9.3 which shows the estimate of the volurne rate of trading (per minute) for AAPL on Jan 5, 2011 from 10:00 to 10:30. The estimate is computed by counting the volume traded over 30 and 10 second windows and scaling the counts to one minute. As the figure shows, a reasonable first order model is one where traded volume comes in bursts of activity which persists for a while (seconds for instance) and then decays to zero. In this section we model volume of trades as a marked point process:

$$V_t = \sum_{n=1}^{N_t} \eta_n \,, \tag{9.36}$$

where Nt is a homogenous Poisson process with intensity .\, and { 171, 172, ... } are non-negative i.i.d. random variables, with distribution function F and finite first moment, independent of Nt and of the Brownian motion driving the midprice. In this case, there is no volume rate process µ,t so the value function is a function *oft,x,S, V* and *q.*

With this model for volume, the infinitesimal generator of *V* acts on the value function as follows:

$$\mathcal{L}^{V}H(t, x, S, V, q) = \lambda \mathbb{E} \left[ H(t, x, S, V + \eta, q) - H(t, x, S, V, q) \right], \qquad (9.37)$$

where lE is the expectation operator with respect to the random variable *17* with distribution function F.

In the previous section we derived the general form (9.30) of the optimal strategy, with the only model dependent component stemming from the function h1 ( *t,* µ, *V)* which is, under the current model assumptions, now a function only of *V.* Thus, under the compound volume Poisson model, we need to solve

$$0 = \partial_t h_1 + \lambda \mathbb{E} \left[ h_1(t, V + \eta) - h_1(t, V) \right] + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right) h_1 - 2 \varphi \left( \rho \mu - \mathfrak{N} \right), \tag{9.38}$$

and since the source term is linear in *V,* we make the ansatz

$$h_1(t, V) = \ell_0(t) + \ell_1(t) V.$$

The terminal condition h1 (T, *V)* = 0 implies that 1!*0* (T) substituting this ansatz for h1 reduces (9.38) to f!1(T) 0, and

$$0 = \left\{ \partial_t \ell_0 + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right) \ell_0 + \psi \ell_1 + 2 \varphi \mathfrak{N} \right\} + \left\{ \partial_t \ell_1 + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right) \ell_1 - 2 \varphi \rho \right\} V.$$

Since the above must hold for every *V,* each term in the braces must vanish individually, resulting in two simple ODEs for 1!*0* and 1! <sup>1</sup> .

We first solve the ODE for f!1(t). As before, we use the integrating factor technique and find that

$$d\left(\exp\left\{\frac{1}{k}\int\left(h_{2}+\frac{1}{2}b\right)dt\right\}\,\ell_{1}\right)=2\,\varphi\,\rho\,\exp\left\{\frac{1}{k}\int\left(h_{2}+\frac{1}{2}b\right)dt\right\}\,dt\,.$$

Next, we use the explicit expression for the integrating factor in  $(9.34)$ , integrate between t and T, and use the boundary condition  $\ell_1(T) = 0$  to find

$$\ell_1(t) = \frac{-2\varphi\rho}{\xi\left(\zeta e^{\xi(T-t)} - e^{-\xi(T-t)}\right)} \left(\zeta e^{\xi(T-t)} + e^{-\xi(T-t)} - \zeta - \xi(t-t)\right)$$

where the constants  $\zeta$  and  $\xi$  are provided in (9.29).

To solve for  $\ell_0(t)$  we proceed as above and write

$$d\left(e^{\frac{1}{\kappa}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\,\ell_{0}(t)\right) = -\left(2\varphi\mathfrak{N}+\psi\ell_{1}(t)\right)e^{\frac{1}{\kappa}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\,dt\,.\tag{9.39}$$

Above we solved a similar ODE, so here the only new term we need to integrate is

$$\begin{split} &\int_{t}^{T} e^{\frac{1}{\kappa} \int \left(h_{2}(u) + \frac{1}{2} b\right) du} \ell_{1}(u) du \\ &= \frac{2\varphi \rho}{\xi} \int_{t}^{T} \left(\zeta e^{\xi(T-u)} + e^{-\xi(T-u)} - \zeta - du \right) \\ &= \frac{2\varphi \rho}{\xi^{2}} \left(\zeta e^{\xi(T-t)} - e^{-\xi(T-t)} - \xi(\zeta+1)(T-t) + 1 - z\right). \end{split}$$

Now, putting these results together we obtain

$$\begin{split} \ell_0(t) &= \frac{2\varphi\mathfrak{N}}{\xi\left(\zeta e^{\xi(T-t)} - e^{-\xi(T-t)}\right)} \left(\zeta e^{\xi(T-t)} + e^{-\xi(T-t)} - \zeta - 1\right) \\ &- \frac{2\psi\varphi\rho}{\xi^2} \frac{\left(\zeta e^{\xi(T-t)} - e^{-\xi(T-t)} - \xi(\zeta+1)(T-t) + 1 - \zeta\right)}{\zeta e^{\xi(T-t)} - e^{-\xi(T-t)}} \\ &= -\frac{\mathfrak{N}}{\rho} \ell_1(t) + \frac{2\psi\varphi\rho}{\xi^2} \frac{\left(\zeta e^{\xi(T-t)} - e^{-\xi(T-t)} - \xi(\zeta+1)(T-t) + 1 - \zeta\right)}{e^{-\xi(T-t)} - \zeta e^{\xi(T-t)}} \end{split}$$

To obtain the optimal liquidation rate and inventory path we substitute  $h_1$ and  $h_2$  into (9.31) and (9.35).

#### 9.3.2 Stochastic Mean-Reverting Volume Rate

In this section we adopt the model for trading volume rate developed in subsection 9.2.2. Recall that the cumulative volume of other market participant's trades on the sell side of the market is given by

$$V_t = \int_0^t \mu_u \, du \,, \tag{9.40}$$

and we assume that rate of trading  $\mu_t$  is as in (9.14), which we repeat for convenience:

$$d\mu_t = -\kappa \,\mu_t \,dt + \eta_{1+N_t^-} \,dN_t \,.$$

Earlier we derived the general form of the optimal strategy, with the only model dependent component stemming from the function  $h_1(t,\mu,V)$  which must satisfy

 $(9.27b)$ . With our current modelling assumptions, the infinitesimal generator of the joint rate and trading volume acts on  $h_1(t, \mu, V)$  as follows:

$$\mathcal{L}^{\mu,V}h_1(t,\mu,V) = (\mu \,\partial_V - \kappa \,\mu \,\partial_\mu) \, h_1(t,\mu,V) + \lambda \, \mathbb{E}[h_1(t,\mu+\eta,V) - h_1(t,\mu,V)] \,,$$

where the expectation is over the random variable  $\eta$  with distribution function  $F.$  Due to the affine nature of this generator and the fact that the terminal condition  $h_1(t,\mu,V) = 0$  is a constant, we use the affine ansatz

$$h_1(t) = \ell_0(t) + \ell_1(t) V + \ell_2(t) \mu, \qquad (9.41)$$

with terminal conditions  $\ell_i(T) = 0$  for  $i = 1, 2, 3$ . Therefore, (9.27b) reduces to solving a system of coupled ODEs for  $\ell_i(t)$ 

$$0 = \partial_t \ell_1 + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right) \ell_1 - 2 \varphi \rho, \qquad (9.42a)$$

$$0 = \partial_t \ell_2 + \left(\frac{1}{k} \left(h_2 + \frac{1}{2}b\right) - \kappa\right) \ell_2 + \ell_1, \tag{9.42b}$$

$$0 = \partial_t \ell_0 + \psi \,\ell_2 + \frac{1}{k} \left( h_2 + \frac{1}{2}b \right) \,\ell_0 + 2\,\varphi \,\mathfrak{N},\tag{9.42c}$$

and recall that  $h_2$  is given by (9.28).

To solve for  $\ell_1$  we once again make use of the integrating factor technique by writing  $(9.42a)$  as

$$d\left(e^{\frac{1}{k}\int\left(h_{2}+\frac{1}{2}b\right)dt}\ell_{1}\right) = 2\,\varphi\,\rho\,e^{\frac{1}{k}\int\left(h_{2}+\frac{1}{2}b\right)dt}\,,\t$$
(9.43)

using  $(9.33)$ , integrating between t and T, and using the terminal condition  $\ell_1(T) = 0$  to obtain

$$\ell_1(t) = \frac{2\varphi\rho}{e^{-\xi(T-t)} - \zeta e^{\xi(T-t)}} \left( e^{-\xi(T-t)} - \zeta e^{\xi(T-t)} + \zeta - \zeta e^{\xi(T-t)} \right) \tag{9.44}$$

where  $\zeta$  and  $\xi$  are given in (9.29).

Similarly, and after straightforward but tedious calculations, we solve  $(9.42b)$  $to obtain$ 

$$\ell_2(t) = \frac{2\varphi\rho}{\zeta e^{(\kappa+\xi)(T-t)} - e^{(\kappa-\xi)(T-t)}} \times \left(\frac{e^{(\kappa-\xi)(T-t)} - \zeta}{\kappa-\xi} + \frac{\zeta}{\kappa+\xi} \qquad e^{(\kappa+\xi)(T-t)}\right) + \frac{\zeta}{\kappa} \qquad e^{\kappa(T-t)}\right).$$

Finally, since we have  $\ell_2(t)$  we leave it to the reader to solve (9.42c) to obtain  $\ell_0(t)$ .

# 9.3.3 Probabilistic Representation

In the previous two subsections, we analysed two modelling specifications for the rate of volume arrivals and derived explicit closed-form expressions. It is in fact possible to derive a general form for the function  $h_1$  in a quite general setting. First, let us restate the equation satisfied by  $h_1$ :

$$0 = \left(\partial_t + \mathcal{L}^{\mu,V}\right)h_1 + \frac{1}{k}\left(h_2 + \frac{1}{2}b\right)h_1 + 2\,\varphi\left(\mathfrak{N} - \rho\,V\right),\,$$

subject to the terminal condition  $h_1(T,\mu,V)=0$ , and recall that  $h_2$  is a deterministic function of time given by (9.28). This is a linear PIDE for  $h_1$  in which  $h_2 + \frac{1}{2}b$  acts as an effective discount rate and  $2\varphi\left(\mathfrak{N}-\rho V\right)$  is a potential (or source) term. The general solution of such an equation can be represented using the Feynman-Kac Theorem. Thus we write

$$h_1(t,\mu,V) = 2\,\varphi\,\mathbb{E}_{t,\mu,V} \left[ \int_t^T \exp\left\{ \frac{1}{k} \int_t^u \left( h_2(s,\mu_s,V_s) + \frac{1}{2}b \right) \, ds \right\} \left( \mathfrak{N} - \rho \, V_u \right) \, du \right]$$
$$= 2\,\varphi\,\mathbb{E}_{t,\mu,V} \left[ \int_t^T \exp\left\{ \sqrt{\frac{\varphi}{k}} \int_t^u \frac{1+\zeta \, e^{2\xi \, (T-s)}}{1-\zeta \, e^{2\xi (T-s)}} \, du \right\} \left( \mathfrak{N} - \rho \, V_u \right) \, du \right].$$

Using  $(9.34)$  to compute the integral in the exponent, we can write

$$h_1(t,\mu,V) = 2\varphi \,\mathbb{E}_{t,\mu,V} \left[ \int_t^T \left( \frac{\zeta \, e^{\xi \, (T-u)} - e^{-\xi \, (T-u)}}{\zeta \, e^{\xi \, (T-t)} - e^{-\xi \, (T-t)}} \right) \, (\mathfrak{N} - \rho \, V_u) \, du \right]$$
$$= 2\varphi \, \int_t^T g(t,u) \, (\mathfrak{N} - \rho \, \mathbb{E}_{t,\mu,V}[V_u]) \, du \,,$$

where

$$g(t,u) = \left(\frac{\zeta e^{\xi (T-u)} - e^{-\xi (T-u)}}{\zeta e^{\xi (T-t)} - e^{-\xi (T-t)}}\right)$$

Upon inserting this representation into the optimal strategy we arrive at the general representation for an agent who targets POCV:

$$\nu_t^* = \xi \left( \begin{array}{c} \zeta e^{\xi (T-t)} + e^{-\xi (T-t)} \\ \zeta e^{\xi \left( \overline{T-t} \right)} - e^{-\xi (T-t)} \end{array} \right) Q_t^{\nu^*} \\
- \xi^2 \int_t^T g(t, u) \left( \mathfrak{N} - \rho \operatorname{\mathbb{E}} \left[ V_u \mid \mathcal{F}_t^{\mu, V} \right] \right) du \,. \tag{9.45}$$

Moreover, inserting the expression for  $h_1$  into the optimal inventory to hold  $(9.35)$  we obtain

$$Q_t^{\nu^*} = \left(\frac{-\zeta e^{\xi (T-t)} - e^{-\xi (T-t)}}{\zeta e^{\xi T} - e^{-\xi T}}\right) \mathfrak{N}$$
  
+ 
$$\xi^2 \int_0^t \int_s^T g(s, u) \left(\mathfrak{N} - \rho \mathbb{E}\left[V_u \,|\, \mathcal{F}_s^{\mu, V}\right]\right) du \, ds.$$
 (9.46)

To understand the intuition behind this general result we look at the limiting case in which the agent wishes full execution of all orders, i.e. in the limit  $\alpha \to \infty$ ,  $\zeta \xrightarrow{\alpha \to \infty} 1$ . In this scenario, the optimal inventory to hold through time simplifies to

$$\begin{split} Q_t^{\nu^*} &\xrightarrow{\alpha \to \infty} \frac{\sinh(\xi (T-t))}{\sinh(\xi T)} \, \mathfrak{N} \\ &+ \xi^2 \int_0^t \! \int_s^T \frac{\sinh(\xi (T-u))}{\sinh(\xi (T-s))} \, \left( \mathfrak{N} - \rho \, \mathbb{E} \left[ V_u \, \middle| \, \mathcal{F}_s^{\mu,V} \right] \right) \, du \, ds \, . \end{split}$$

As the expression shows, the first term is the classical AC strategy, and the second term corrects for deviations of the strategy from the POCV.

# 9.4 lnduding Impact of Other Traders

So far we have assumed that other traders' volume does not move the midprice, but that the liquidating agent's trades do. This is somewhat inconsistent. In this section, we assume that MOs from all market participants, including the agent's, have a permanent effect on the midprice as shown by the SDE

$$dS_t^{\nu} = b\left(\mu_t^+ - \left(\nu_t + \mu_t^-\right)\right) dt + \sigma dW_t,$$

where µ; denote the rate of trading for buy and sell MOs sent by other traders and Vt > 0 is the agent's liquidation rate. If the agent was acquiring shares then her trading rate would be added, instead of subtracted, to the drift of the SDE. Moreover, *b* > 0 represents the permanent impact that trading has on the midprice. As before, the agent's execution price Sf is assumed to be linear in her trading rate so that

$$\hat{S}_t^{\nu} = S_t^{\nu} - k \,\nu_t \,.$$

Here, we assume that the agent aims to target the rate of sell trading volume, and we leave the case of targeting cumulative volume to the reader, see Exercise E.9.3. In this case, her performance criteria is given by

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,x,S,\mu q} \left[ X^{\nu}_{T} + Q^{\nu}_{T}(S^{\nu}_{T} - \alpha Q^{\nu}_{T}) - \varphi \int_{t}^{T} (\nu_{u} - \rho \mu_{u}^{-})^{2} \ du \right] ,$$

where µ={µ <sup>+</sup> ,µ-}, and her value function is

$$H(t,x,S,\pmb{\mu},q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t,x,S,\pmb{\mu},q) \, .$$

Applying the dynamic programming principle suggests that the value function should satisfy the DPE

$$0 = \left(\partial_{t} + \frac{1}{2}\sigma^{2}\partial_{SS} + \mathcal{L}^{\mu}\right)H$$
  
+ 
$$\sup_{\nu} \left\{ \left(S - k\nu\right)\nu\,\partial_{x}H - \nu\,\partial_{q}H + b((\mu^{+} - \mu^{-}) - \nu)\,\partial_{S}H - \varphi\,(\nu - \rho\,\mu^{-})^{2} \right\},\tag{9.47}$$

where ,[J.L denotes the infinitesimal generator *ofµ.* The only difference between this DPE and the one for the case without impact (see (9.5)), is the term b (µ <sup>+</sup> µ-) *85H* which does not directly affect the optimisation over the agent's trading v in feedback form - it will however alter the value function, and hence the explicit form of *v\*.*

We once again use the ansatz

$$H(t,x,S,\pmb{\mu},q) = x + q\,S + h(t,\pmb{\mu},q)\,,$$

where h now depends on both trading rates  $\mu^+$  and  $\mu^-$ , and the terminal condition is  $h(T, \mu, q) = -\alpha q^2$ . Inserting into the DPE above, we find that h must satisfy

$$0 = (\partial_t + \mathcal{L}^{\mu}) h + b(\mu^+ - \mu^-) q$$
  
+ 
$$\sup_{\nu} \left\{ -k \nu^2 - (\partial_q h + bq) \nu - \varphi (\nu - \rho \mu^-)^2 \right\}.$$
 (9.48)

Solving for the first order condition provides the optimal speed of trading in  $\text{feedback form as}$ 

$$\nu^* = \frac{-(\partial_q h + b\,q) + 2\,\varphi\,\rho\,\mu^-}{2(k+\varphi)},\n$$
(9.49)

and upon inserting into the DPE we find the non-linear equation which  $h$  should satisfy:

$$0 = (\partial_t + \mathcal{L}^{\mu}) h + b(\mu^+ - \mu^-) q + \frac{1}{4(k+\varphi)} (\partial_q h + bq - 2\varphi \rho \mu^-)^2 - \varphi \rho^2 (\mu^-)^2.$$

Comparing this to the case where there is no impact from other traders shown in  $(9.8)$ , repeated here for convenience,

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right)h + \frac{1}{4(k+\varphi)}\left(\partial_q h + b\,q - 2\,\varphi\,\rho\,\mu\right)^2 - \varphi\,\rho^2\left(\mu\right)^2,$$

we see that the main difference is that the agent must now account for both buy and sell side trading rates, and the additional term  $b(\mu^+ - \mu^-)q$  makes the agent aware of the asset's drift due to net trading in either direction.

To solve the non-linear equation for  $h$ , we observe once again that the affine nature of the PDE and the terminal condition suggest the ansatz

$$h(t, \boldsymbol{\mu}, q) = h_0(t, \boldsymbol{\mu}) + h_1(t, \boldsymbol{\mu}) q + h_2(t, \boldsymbol{\mu}) q^2$$

subject to the terminal conditions  $h_0(T,\mu) = h_1(T,\mu) = 0$  and  $h_0(T,\mu) = -\alpha$ . On inserting this ansatz, expanding the expression and collecting terms with like powers in q, we find that the  $h_i$  satisfy the coupled system of equations

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_2 + \frac{\left(h_2 + \frac{1}{2}b\right)^2}{k + \varphi},\tag{9.50a}$$

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_1 + \frac{h_1 - 2\,\varphi\,\rho\,\mu^-}{k + \varphi} \left(h_2 + \frac{1}{2}\,b\right) + b\left(\mu^+ - \mu^-\right),\tag{9.50b}$$

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_0 + \frac{1}{4(k+\varphi)} \left(h_1 - 2\varphi \,\rho \,\mu^-\right)^2 - \varphi \,\rho^2 \,(\mu^-)^2 \,. \tag{9.50c}$$

We see that  $h_2$  which satisfies (9.50a), is the same equation as in the case where we ignore the impact of other agents, and its solution is given by  $(9.11)$ , repeated here for convenience:

$$h_2(t,\boldsymbol{\mu}) = -\left(\frac{T-t}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right)^{-1} - \frac{1}{2}b.$$

As before, this is independent of the rate of trading of other agents and corresponds to a TWAP-like trading strategy. In the next section, we focus on computing  $h_1$  under general assumptions.

#### 9.4.1 Probabilistic Representation

In the general case, we can once again make use of a Feynman-Kac formula and write the solution to  $(9.50b)$  as

$$h_t(t,\boldsymbol{\mu}) = \mathbb{E}_{t,\boldsymbol{\mu}} \left[ \int_t^T e^{\int_t^s \tilde{h}_2(u,\boldsymbol{\mu}_u) \, du} \left\{ -2\,\varphi\,\rho\,\tilde{h}_2(s,\boldsymbol{\mu}_s)\,\mu_s^- + b\left(\mu_s^+ - \mu_s^-\right) \right\} ds \right] \,,$$

where  $h_2(t,\boldsymbol{\mu}_t) := \frac{1}{k+\varphi} \left( h_2(t,\boldsymbol{\mu}_t) + \frac{1}{2}b \right)$ . The above expression can be simplified somewhat by noticing that

$$e^{\int_t^s \tilde{h}_2(u,\boldsymbol{\mu}_u) \, du} = \exp\left\{-\frac{1}{k+\varphi} \int_t^s \left(\frac{T-s}{k+\varphi} + \frac{1}{\alpha - \frac{1}{2}b}\right)^{-1} \, ds\right\} = \frac{(T-s) + \zeta}{(T-t) + \zeta}$$

where

$$\zeta = \frac{k + \varphi}{\alpha - \frac{1}{2} \, b} \, .$$

Inserting this integral into the expression for  $h_1$  above, and interchanging the expectation and outer integral, we arrive at

$$h_t(t,\boldsymbol{\mu}) = \varphi \,\rho \!\int_t^T \frac{\mathbb{E}_{t,\boldsymbol{\mu}}\left[\mu_s^-\right]}{(T-t)+\zeta} \,ds + b \!\int_t^T \frac{\left(\frac{(T-s)+\zeta}{(T-t)+\zeta}\right)}{\left(\frac{(T-s)+\zeta}{(T-t)+\zeta}\right)} \,\mathbb{E}_{t,\boldsymbol{\mu}}\left[\,\mu_s^+ - \mu_s^-\,\right] \,ds \,.$$

As the above formula shows, the first term accounts for the one-sided trades that move in the same direction as that of the agent (i.e. sell trades), while the second term accounts for the imbalance in buys and sells. Both terms are integrated over the remaining life of the trading horizon and weight the expected selling / imbalance trading rate through time. The first term computes the mean expected future selling rate, while the second weighs the earlier trades more  $\text{heavy} - \text{since those trades have more time in which to impact the midprice.}$ 

Recall that the agent's optimal trading speed is given by  $(9.49)$  which, in terms of  $h_i$ , reduces to

$$\nu_t^* = -\frac{1}{k+\varphi} \left( h_2(t,\boldsymbol{\mu}_t) + \frac{1}{2}b \right) Q_t^{\nu^*} + \frac{1}{2(k+\varphi)} \left( 2\,\varphi\,\rho\,\mu_t^- - h_1(t,\boldsymbol{\mu}_t) \right) .$$

Substituting the above results, we finally obtain

$$\nu_{t}^{*} = \frac{Q_{t}^{\nu^{*}}}{(T-t)+\zeta} + \frac{\varphi}{k+\varphi} \rho \left\{ \mu_{t}^{-} - \frac{\int_{t}^{T} \mathbb{E}\left[\mu_{s}^{-} \mid \mathcal{F}_{t}^{\boldsymbol{\mu}}\right] ds}{(T-t)+\zeta} \right\} - \frac{b}{k+\varphi} \frac{\int_{t}^{T} \left((T-s)+\zeta\right) \mathbb{E}\left[\left(\mu_{s}^{+}-\mu_{s}^{-}\right) \mid \mathcal{F}_{t}^{\boldsymbol{\mu}}\right] ds}{(T-t)+\zeta}.\n$$
(9.51)

To understand the functioning of the liquidation strategy we see that the first two terms are identical to the case which does not account for the impact of other traders, see  $(9.19)$  and discussion that follows. The new term in the second line of  $(9.51)$  acts to correct her trading based on her expectations of the net order flow from that point in time until the end of the trading horizon. When there is currently no imbalance  $(\mu_t^+ = \mu_t^-)$  her liquidation rate is as in (9.19). When

there is a surplus of buy trades, however, she slows down her trading rate to allow the midprice to appreciate before liquidating the rest of her order. When there is a surplus of sell orders, she speeds up her trades for two reasons: (i) because she must match the POV on the sell side; and (ii) the action of other sellers in the market will push prices downwards, and therefore degrade her profits if she waits. She therefore attempts to liquidate a larger portion of her orders now rather than later.

#### 9 Example: Stochastic Mean-Reverting Volume

It is helpful to provide a specific modelling example in which we can derive a simple closed-form formula for the optimal liquidation speed. We assume that buy and sell trading volumes arrive independently, where each satisfies the SDE

$$d\mu_t^{\pm} = -\kappa \,\mu_t^{\pm} \,dt + \eta_{1+N^{\pm}} \, \,dN_t^{\pm} \,,$$

where  $N_t^{\pm}$  are independent Poisson processes with intensity  $\lambda$ , and  $\{\eta_1^{\pm}, \eta_2^{\pm}, \dots\}$ are i.i.d. random variables, with distribution function  $F$ , representing jumps in trading volume, and independent of  $N_t^{\pm}$  and of the Brownian motion  $W_t$  driving the midprice. In this manner, the model assumes that buy/sell trading rates are two independent jump Ornstein-Uhlenbeck (OU) process.

We can solve the above SDE explicitly, by introducing an integrating factor and writing  $\mu_t^{\pm} = e^{-\kappa t} \tilde{\mu}_t^{\pm}$ , so that

$$d\tilde{\mu}_t^{\pm} = e^{\kappa t} \,\eta_{1+N_{\cdot-}^{\pm}} \,dN_t^{\pm} \,.$$

Therefore, we can write the trading rates as

$$\tilde{\mu}_s^{\pm} - \tilde{\mu}_t^{\pm} = \int_t^s e^{\kappa \, u} \, \eta_{1+N_{u^-}^{\pm}} \, dN_u^{\pm} \,,$$

and so, for  $s > t$ , we have

$$\mu_s^{\pm} = e^{-\kappa (s-t)} \mu_t^{\pm} + \int_t^s e^{-\kappa (s-u)} \eta_{1+N_u^{\pm}} dN_u^{\pm} .$$

The expression for the optimal trading speed requires only the expected value of the trading rate given its current value. For this purpose, we can compute, for  $s > t$ ,

$$\begin{split} \mathbb{E}_{t,\boldsymbol{\mu}}\left[\mu_{s}^{\pm}\right] &= e^{-\kappa\,(s-t)}\,\mu_{t}^{\pm} + \int_{t}^{s} e^{-\kappa\,(s-u)}\,\mathbb{E}[\eta]\,\lambda\,du \\ &= e^{-\kappa\,(s-t)}\,\mu_{t}^{\pm} + \frac{\lambda\,\mathbb{E}[\eta]}{\kappa}\,\left(1 - e^{-\kappa\,(s-t)}\right) \\ &= e^{-\kappa\,(s-t)}\,\left(\mu_{t}^{\pm} - \frac{\lambda\,\mathbb{E}[\eta]}{\kappa}\right) + \frac{\lambda\,\mathbb{E}[\eta]}{\kappa} \,. \end{split}$$

Next, substituting this result into the expression for the optimal trading rate

238

 $(9.51)$  and computing the integrals there leads to (with  $\tau := T - t$ )

$$\nu_t^* = \frac{Q_t^{\nu^*}}{\tau + \zeta} + \frac{\varphi}{k + \varphi} \rho \left\{ \mu_t^- - \frac{\int_t^T \left( e^{-\kappa \left( s - t \right)} \left( \mu_t^- - \frac{\lambda \operatorname{\mathbb{E}}[\eta]}{\kappa} \right) + \frac{\lambda \operatorname{\mathbb{E}}[\eta]}{\kappa} \right) ds}{\tau + \zeta} \right\} \\
+ \frac{b}{k + \varphi} \frac{\int_t^T \left( (T - s) + \zeta \right) e^{-\kappa \left( s - t \right)} ds}{\tau + \zeta} \left( \mu_t^+ - \mu_t^- \right) \\
= \frac{Q_t^{\nu^*}}{\tau + \zeta} + \frac{\varphi}{k + \varphi} \rho \left\{ \mu_t^- - \frac{\frac{1 - e^{-\kappa \tau}}{\kappa} \left( \mu_t^- - \frac{\lambda \operatorname{\mathbb{E}}[\eta]}{\kappa} \right) + \frac{\lambda \operatorname{\mathbb{E}}[\eta]}{\kappa}}{\tau + \zeta} \right\} \\
+ \frac{b}{k + \varphi} \frac{(1 - \kappa \zeta) e^{-\kappa \tau} + \kappa (\tau + \zeta) - 1}{\kappa^2 (\tau + \zeta)} \left( \mu_t^+ - \mu_t^- \right) .$$

# 9.5 Utility Maximiser

In this section the agent's objective is to maximise expected utility of terminal wealth but to also target POV. The setup is the same as the one described in Section 9.2 and the agent's preferences are described by exponential utility  $U(x) = -e^{-\gamma x}$ . If the agent ignores the POV objective, her performance criteria is

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,x,S,\mu,q} \left[ -e^{-\gamma(X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}))} \right] .$$

The question is how to incorporate a POV penalty while maintaining tractability of the problem. One naive answer is to simply add in a penalisation as we did before, e.g. by considering the performance criteria

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,x,S,\mu,q} \left[ -e^{-\gamma(X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}))} - \varphi \int_t^T \left( \nu_u - \rho \, \mu_u \right)^2 \, du \right] \,,$$

where  $\mu_t$  is the other agents' (selling) trading rate,  $0 < \rho < 1$  is the fraction of the trading rate that the agent targets, and  $\varphi \geq 0$  the target penalty parameter.

This approach, however, does not lead to analytically tractable results. The main reason is that the exponential utility and the linear penalty are in a sense incompatible, and, here, even the cash process does not factor out of the problem. Instead, we consider what is sometimes called a recursive intertemporally additive penalty. Stylistically we aim to have a value function defined as the continuous limit of the recursion

$$H_t = \sup_{\nu} \mathbb{E} \left[ H_{t+\Delta t} + \varphi \gamma \, H_{t+\Delta t} \left( \nu_t - \rho \, \mu_t \right)^2 \Delta t \right] \, ,$$

with  $H_T = \mathbb{E}\left[-e^{-\gamma(X_T^{\nu}+Q_T^{\nu}(S_T^{\nu}-\alpha Q_T^{\nu}))}\right]$ . Alternatively, one can view this as a stochastic differential utility, as in Duffie & Epstein  $(1992)$ .

By adopting this approach, when the agent wishes to optimally liquidate shares

whilst targeting POV, her performance criteria is

$$H^{\nu}(t,x,S,\mu,q) = \mathbb{E}_{t,S,\mu,q} \left[ -e^{-\gamma(X^{\nu}_{T} + Q^{\nu}_{T}(S^{\nu}_{T} - \alpha Q^{\nu}_{T}))} \right.$$
$$\left. + \varphi\gamma \int_{t}^{T} \left( \nu_{u} - \rho \,\mu_{u} \right)^{2} \, H^{\nu}(u,X^{\nu}_{u},S^{\nu}_{u},\mu_{u},Q^{\nu}_{u}) \, du \right]$$

and her value function is

$$H(t, x, S, \mu, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, \mu, q) \, .$$

Note that the penalty term has a positive sign in front of the integral. The reason is that  $H$  itself is negative, so that this term is indeed a penalty contribution. Deviations from the target POV are scaled by the value function at that time, so if there is a lot of value at that point in state space, the agent is averse to moving away from POV, while if there is little value at that point in state space, the agent is willing to deviate from POV if it gains her value.

Applying the dynamic programming principle suggests that the value function  $\text{should satisfy the DPE}$ 

$$\left(\partial_t + \frac{1}{2}\sigma^2 \partial_{SS} + \mathcal{L}^{\mu}\right) H + \sup_{\nu} \left\{ (S - k\,\nu)\,\nu\,\partial_x H - \nu \partial_q H - b\,\nu\,\partial_S H + \varphi\,\gamma\,(\nu - \rho\,\mu)^2 \,H \right\} = 0,$$

subject to the terminal condition  $H(T, x, S, \mu, q) = -e^{-\gamma (x+q(S-\alpha q))}$ , and attains a supremum at

$$\nu^* = \frac{1}{2} \frac{-S \,\partial_x H + \partial_q H + b \,\partial_S H + 2 \,\gamma \varphi \,\rho \mu \,H}{-k \,\partial_x H + \gamma \varphi \,H} \,. \tag{9.52}$$

The form of the terminal condition suggests that we use the ansatz

$$H = -e^{-\gamma(x+qS+h(t,\mu,q))} \,,$$

which leads to the following equation for  $h(t, \mu, q)$ :

$$0 = -\mathcal{L}^{\mu} \left( e^{-\gamma h} \right)$$
  
+ 
$$\left( \gamma \partial_t h - \frac{1}{2} \sigma^2 \gamma^2 q^2 + \gamma \frac{\left( b q + \partial_q h - 2 \varphi \rho \mu \right)^2}{4(k + \varphi)} - \gamma \varphi \rho^2 \mu^2 \right) e^{-\gamma h}, \quad (9.53)$$

with terminal condition  $h(T, \mu, q) = -\alpha q^2$ .

## 9.5.1 Solving the DPE with Deterministic Volume

We assume that the rate at which other market participants are selling shares is a deterministic function of time with derivative  $d\mu(t) = g(t) dt$  so that  $\mathcal{L}^{\mu}H =$  $\partial_{\mu}Hg(t)$ . In this case, we can view the agent as targeting a predictable trading pattern, which for example, may be taken as the solid blue line in the right panel of Figure  $9.2$ .

Thus we write  $(9.53)$  in the form

$$0 = (\partial_t + \mathcal{L}^{\mu}) h + \frac{(\partial_q h + bq - 2\varphi \rho \mu)^2}{4(k + \varphi)} - \varphi \rho^2 \mu^2 - \frac{1}{2} \sigma^2 \gamma q^2. \tag{9.54}$$

Note that (9.54) is the same as (9.8) with the extra term  $-\frac{1}{2}\sigma^2\gamma q^2$ , so we proceed as above and make the ansatz

$$h(t,\mu,q) = h_0(t,\mu) + q h_1(t,\mu) + q^2 h_2(t,\mu), \qquad (9.55)$$

and after straightforward manipulations and collecting terms in  $q$  we obtain the coupled system of PIDEs

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_2 + \frac{\left(h_2 + \frac{1}{2}b\right)^2}{k + \varphi} - \frac{1}{2}\sigma^2\gamma, \tag{9.56a}$$

$$0 = \left(\partial_t + \mathcal{L}^{\mu}\right) h_1 + \frac{h_1 - 2\varphi\rho\mu}{k + \varphi} \left(h_2 + \frac{1}{2}b\right) ,\qquad (9.56b)$$

$$0 = (\partial_t + \mathcal{L}^{\mu}) h_0 + \frac{1}{4(k+\varphi)} (h_1 - 2\varphi\rho\mu)^2 - \varphi\rho^2\mu^2, \qquad (9.56c)$$

with terminal conditions  $h_2(T) = -\alpha$ ,  $h_1(T) = h_0(T) = 0$ .

Now observe that equation (9.56a) for  $h_2$  contains no source terms dependent on  $\mu$  and its terminal condition is independent of  $\mu$ , hence the solution must also be independent of  $\mu$ . The equation satisfied by  $h_2$  is of Riccati type and can be solved explicitly. We solve for  $h_2$ , see the solution of the Riccati ODE (6.25), to obtain

$$h_2(t) = \sqrt{(k+\varphi)\xi} \, \frac{1+\zeta \, e^{2\omega \, (T-t)}}{1-\zeta \, e^{2\omega (T-t)}} - \frac{1}{2}b \,,$$

where

$$\xi = \frac{1}{2}\sigma^2\gamma \,, \quad \omega = \sqrt{\frac{\xi}{k+\varphi}}, \quad \text{and} \quad \zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{(k+\varphi)\,\xi}}{\alpha - \frac{1}{2}b - \sqrt{(k+\varphi)\,\xi}} \,. \tag{9.57}$$

Now we turn to solving the PIDE

$$0 = \partial_t h_1 - g \,\partial_\mu h_1 + \frac{h_1 - 2\varphi\rho\mu}{k + \varphi} \left(h_2 + \frac{1}{2}b\right) \,, \tag{9.58}$$

with terminal condition  $h_1(T) = 0$ . To solve this equation we look at the different components in (9.58) and observe that if we assume an ansatz linear in  $\mu$ :

$$h_1(t,\mu) = \ell_0(t) + \ell_1(t)\,\mu\,,\t\t(9.59)$$

then  $(9.58)$  becomes

$$0 = \left\{ \partial_t \ell_0 - g\ell_1 + \frac{h_2 + \frac{1}{2}b}{k+\varphi} \ell_0 \right\} + \left\{ \partial_t \ell_1 + \frac{\ell_1 - 2\varphi\rho}{k+\varphi} \left( h_2 + \frac{1}{2}b \right) \right\} \mu. \tag{9.60}$$

Now, since this equation must hold for all  $\mu$ , the terms in braces must vanish

individually. Therefore we must solve two uncoupled ODEs:

$$0 = \partial_t \ell_0 - g\ell_1 + \frac{h_2 + \frac{1}{2}b}{k + \varphi} \ell_0, \qquad (9.61)$$

$$0 = \partial_t \ell_1 + \frac{\ell_1 - 2\varphi\rho}{k + \varphi} \left(h_2 + \frac{1}{2}b\right) \,. \tag{9.62}$$

We first solve  $(9.62)$  using the integrating factor technique. First we calculate, in a similar way to  $(9.33)$ ,

$$\frac{1}{k+\varphi} \int \left( h_2(t) + \frac{1}{2} b \right) dt = \sqrt{\frac{\xi}{k+\varphi}} \int \frac{1+\zeta \, e^{2\omega \, (T-t)}}{1-\zeta \, e^{2\omega (T-t)}} dt$$
$$= \log \left[ e^{-\omega (T-t)} - \zeta e^{\omega (T-t)} \right] .$$

Now we write

$$d\left(e^{\frac{1}{k+\varphi}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\ell_{1}\right) = \frac{2\varphi\rho}{k+\varphi}e^{\frac{1}{k+\varphi}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\left(h_{2}(t)+\frac{1}{2}b\right)\,,$$

and integrate both sides between  $t$  and  $T$ :

$$-\left(e^{-\omega(T-t)} - \zeta e^{\omega(T-t)}\right)\ell_1(t)$$
  
$$= 2\varphi\rho\omega \int_t^T \left(e^{-\omega(T-u)} - \zeta e^{\omega(T-u)}\right) \frac{1+\zeta e^{2\omega(T-u)}}{1-\zeta e^{2\omega(T-u)}} du$$
  
$$= 2\varphi\rho \left(\zeta e^{\omega(T-t)} - e^{-\omega(T-t)} + 1 - \zeta\right)$$
  
$$\ell_1(t) = 2\varphi\rho \frac{\zeta e^{\omega(T-t)} - e^{-\omega(T-t)} + 1 - \zeta}{\zeta e^{\omega(T-t)} - e^{-\omega(T-t)}}.$$

Similarly, to solve for  $\ell_0$  we start as usual by writing

$$d\left(e^{\frac{1}{k+\varphi}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\,\ell_{0}(t)\right) = e^{\frac{1}{k+\varphi}\int\left(h_{2}(t)+\frac{1}{2}b\right)dt}\,g(t)\,\ell_{1}(t)$$

and integrate both sides between  $t$  and  $T$  to obtain

$$\ell_0(t) = \frac{2\varphi\rho}{e^{-\omega(T-t)} - \zeta e^{\omega(T-t)}} \int_t^T g(u) \left(\zeta e^{\omega(T-u)} - e^{-\omega(T-u)} + 1 - \zeta\right) du. \tag{9.63}$$

Finally, after straightforward manipulations, the optimal speed of trading is

$$\nu_t^* = -\omega \, \frac{1+\zeta \, e^{2\omega \, (T-t)}}{1-\zeta \, e^{2\omega (T-t)}} Q_t^{\nu^*} + \frac{\varphi\rho - \frac{1}{2}\ell_1(t)}{k+\varphi} \, \mu_t - \frac{\frac{1}{2}\ell_0(t)}{k+\varphi} \,, \tag{9.64}$$

where  $\omega$ ,  $\zeta$  are constant parameters given in (9.57).

In the optimal speed of liquidation we see that the first term is an AC-type term similar to the one derived in  $(6.27)$ . The other three terms adjust the speed so that the liquidation rate targets the fraction  $\rho$  of POV.

Note that when the risk aversion parameter  $\gamma \to 0$ , the agent's preferences are as those of a risk-neutral agent and the optimal liquidation strategy would be

the same as the one derived in subsection 9.2.1 for this particular choice of £.P. It is easy to see that if we set 1 = 0, the system of PIDEs (9.56) is the same as the system (9.10) and h1(t) and h2(t) have the same boundary conditions.

# 9.6 Bibliography and Selected Readings

Konishi (2002), Bialkowski, Darolles & Fol (2008), Humphery-Jenner (2011), McCulloch & Kazakov (2012), Frei & Westray (2013), Gueant & Royer (2014), Gueant (2014), Mitchell, Bialkowski & Tompaidis (2013), Cartea & Jaimungal (2014a).

# 9. 7 Exercises

E.9.1 Assume that the agent's objective is to liquidate 1)1 shares as in Section 9.2, but the strategy also penalises running inventory so that her performance criteria is

$$H^{\nu}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}) - \varphi \int_t^T (\nu_u - \rho V_u)^2 \ du - \phi \int_t^T (Q_u)^2 \ du \right].$$

(a) Show that the agent's value function H satisfies

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \partial_{SS} + \mathcal{L}^V\right)H - \phi q^2 + \sup_{\nu} \left\{ (S - k\nu)\,\nu - \nu \partial_q H - b\,\nu\,\partial_S H - \varphi\,(\nu - \rho V)^2 \right\} \,,$$

subject to the terminal condition H(T, S, v, q) = q(S -aq).

(b) J\ifake the ansatz

$$H(t, S, V, q) = q S + h_0(t, V) + q h_1(t, V) + q^2 h_2(t, V)$$

and show that the problem reduces to solving the coupled system of PIDEs

$$0 = \left(\partial_t + \mathcal{L}^V\right) h_2 + \frac{\left(h_2 + \frac{1}{2}b\right)^2}{k + \varphi} - \phi, \tag{9.65a}$$

$$0 = \left(\partial_t + \mathcal{L}^V\right) h_1 + \frac{h_1 - 2\varphi\rho V}{k + \varphi} \left(h_2 + \frac{1}{2}b\right) ,\qquad (9.65b)$$

$$0 = \left(\partial_t + \mathcal{L}^V\right) h_0 + \frac{1}{4(k+\varphi)} \left(h_1 - 2\varphi\rho V\right)^2 - \varphi \rho^2 V^2 \,. \tag{9.65c}$$

(c) Assuming that ½ satisfies (9.14), find the optimal speed of trading and compare it to (9.17).

E.9.2 An agent wishes to acquire  $\mathfrak{N}$  shares by time T. Her performance criteria is

$$H^{\nu}(t,x,S,y,q) = \mathbb{E}_{t,x,S,y,q} \left[ X_T^{\nu} + (\mathfrak{N} - Q_T^{\nu})(S_T^{\nu} + \alpha(\mathfrak{N} - Q_T^{\nu})) + \varphi \int_t^T \left( Q_u^{\nu} - \rho Y_u \right)^2 du \right]$$

and her value function is

$$H(t, x, S, y, q) = \inf_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, y, q) , \qquad (9.66)$$

where  $Y_t$  is the total volume purchased by other market participants, and the acquired inventory  $Q_t^{\nu}, S_t^{\nu}$ , and acquisition cost  $X_t^{\nu}$ , satisfy

$$dQ_t^{\nu} = \nu_t dt, \qquad \qquad Q_0^{\nu} = q,$$
  

$$dS_t^{\nu} = b \nu_t dt + \sigma dW_t, \qquad \qquad S_0^{\nu} = S,$$
  

$$dX_t^{\nu} = (S_t^{\nu} + k \nu_t) \nu_t dt, \qquad \qquad X_0^{\nu} = x.$$

(a) Show that the value function satisfies the DPE

$$\left(\partial_{t} + \frac{1}{2}\sigma^{2}\partial_{SS} + \mathcal{L}^{y,V}\right)H + \varphi(q - \rho y)^{2}$$
  
+ 
$$\inf_{\nu} \left\{(S^{\nu} + \nu k)\nu\,\partial_{x}H + b\nu\partial_{S}H + \nu\partial_{q}H\right\} \tag{9.68}$$

subject to terminal and boundary conditions and where  $\mathcal{L}^{y,V}$  is the generator of  $y$  and  $V$ .

(b) Show that the optimal acquisition speed is

$$\nu_t^* = \frac{\mathfrak{N} - Q_t^{\nu^*}}{k} \left( h_2(t) - \frac{1}{2}b \right) + \frac{h_1(t)}{2k} \,,$$

where

$$h_2(t) = \sqrt{k\,\varphi} \, \frac{1+\zeta\,e^{2\xi\,(T-t)}}{1-\zeta\,e^{2\xi(T-t)}} - \frac{1}{2}b\,,$$

with

$$\xi = \sqrt{\frac{\varphi}{k}} \quad \text{and} \quad \zeta = \frac{\alpha + \frac{1}{2}b + \sqrt{k\,\varphi}}{\alpha + \frac{1}{2}b - \sqrt{k\,\varphi}} \,,$$

and  $h_1(t)$  solves the PIDE

$$\left(\partial_t + \mathcal{L}^{y,V}\right)h_1 - \frac{1}{k}(h_2(t) - \frac{1}{2}b) - 2\varphi(\mathfrak{N} - \rho y) = 0.$$

Note that if  $\varphi = b = 0$  then the optimal acquisition speed is as in (6.17).

 $E.9.3$  Modify the problem of optimal liquidation described in Section 9.2 so that the liquidation rate  $\mu_t$  takes into account the agent's trade. Derive the optimal liquidation rate and the inventory path.

E.9.4 Assume the setup of Section 9.4 where the trading rates of the agent and other traders affect the midprice. Solve the optimal liquidation problem where the agent targets POCV, that is her performance criteria is

$$H^{\nu}(t,x,S,\mu,q)$$
  
=  $\mathbb{E}_{t,x,S,\mu,q} \left[ X_T^{\nu} + Q_T^{\nu}(S_T^{\nu} - \alpha Q_T^{\nu}) - \varphi \int_t^T ((\mathfrak{N} - Q_u^{\nu}) - \rho V_u)^2 \ du \right],$ 

where

$$V_t = \int_0^t \mu_u^- \, du$$

is the total volume traded on the sell side of the market.
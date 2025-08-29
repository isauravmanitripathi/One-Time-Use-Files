# 6 Optimal Execution with Continuous Trading I

### 6,1 **Introduction**

A classical problem in finance is how an agent can sell or buy a large amount of shares and yet minimise adverse price movements which are a consequence of her own trades. Here, the term 'large' means that the amount the agent is interested in buying or selling is too big to execute in one trade. One way to think about a trade being too large is to compare it to the size of an average trade or to the volume posted on the limit order book (LOB) at the best bid or best offer. Clearly, if the number of shares that the agent seeks to execute is significantly larger than the average size of a trade, then it is probably not a good idea to try to execute all the shares in one trade.

Investors who regularly come to the market with large orders ( orders that are a significant fraction of average daily volume) are institutional traders such as pension funds, hedge funds, mutual funds, and sovereign funds. These investors often delegate their trades to an agency broker (the agent) who acts on their behalf. The agent will slice the parent order into smaller parts ( sometimes called child orders) and try to execute each one of these child orders over a period of time, taking into account the balance between price impact (trade quicker) and price risk (take longer to complete all trades). What we mean by this trade-off is the following: imagine the situation in which the agent is selling shares. If she trades quickly, then her orders will walk through the buy side of the LOB and she will obtain worse prices for her orders. Even if she breaks up each order into small bits (so that each one does not walk the book), and sends them quickly to the market, then other traders will notice an excess of sell orders and reshuffle their quotes inducing again a negative price impact. If on the other hand, she trades slowly, so as to avoid this price impact, then she will be exposed to the uncertainty of what precisely the future prices will be. Hence, she must attempt to balance these two factors.

The time the agent takes to space out and execute the smaller orders is crucial. Short time horizons will lead to faster trading ( and hence more price impact) and less price uncertainty, but there are also many reasons why a long trading horizon might not be desirable. For instance, it might be that it is decided to sell a large chunk of shares because the price is convenient but by the time the agent executes all child orders, the share price could have dropped to a less desirable level. Another reason which constrains the time needed to sell all the shares, is that this particular operation is part of a bigger one which is the result of a portfolio rebalance which also requires the purchase of a large number of shares in another firm, and both operations need to be completed over approximately the same time period.

Hence the agent must formulate a model to help her decide how to optimally liquidate or acquire shares, where the aim is to minimise the cost of executing her trade(s) and balance it against price risk. Execution costs are measured as the difference between a benchmark price and the actual price (measured as the average price per share) at which the trade was completed. Our convention is that when the sign of the execution cost is positive, it means that there is loss of value in the operation because the actual price of the trade was worse than the benchmark price.

The benchmark price represents a perfectly executed price in a market with no frictions. It is customary to use the midprice of the asset at the time the order is given to execute the trade. This benchmark is known as the arrival price which is generally taken to be the average of the best bid and best ask, i.e. the midprice. Moreover, when the arrival price is the benchmark, the execution cost is known as the implementation shortfall or slippage, see Almgren (2010).

## 6.2 The Model

To pose the optimal execution problem we require notation to describe the number of shares the agent is holding (inventory), the dynamics of the midprice, and how the agent's market orders (MOs) affect the midprice.

The key stochastic processes are:

- @ v = (vt){o<::t<::T} is the trading rate, the speed at which the agent is liquidating or acquiring shares (it is also the variable the agent controls in the optimisation problem),
- e Q<sup>v</sup>= ( Qr) {O<::t<::T} is the agent's inventory, which is clearly affected by how fast she trades,
- & 3 <sup>v</sup>= (Sn{o<::t<::T} is the midprice process, and is also affected in principle by the speed of her trading,
- @ 5 <sup>v</sup>= (Sn{o<::t<::T} corresponds to the price process at which the agent can sell or purchase the asset, i.e. the execution price, by walking the LOB, and
- @ X<sup>v</sup>= (Xn{o<::t<::T} is the agent's cash process resulting from the agent's execution strategy.

Whether liquidating or acquiring, the agent's controlled inventory process is given in terms of her trading rate as follows:

$$dQ_t^{\nu} = \pm \nu_t \, dt \,, \qquad \qquad Q_0^{\nu} = q \,, \tag{6.1a}$$

while the midprice is assumed to satisfy the SDE

$$dS_t^{\nu} = \pm g(\nu_t) \, dt + \sigma \, dW_t \,, \qquad \qquad S_0^{\nu} = S \,, \tag{6.1b}$$

where

- *W* = (Wt){o::;t:s;T} is a standard Brownian motion, and
- *g:* lR+ -+ lR+ denotes the permanent price impact that the agent's trading action has on the midprice.

The execution price satisfies the SDE

$$\hat{S}_t^{\nu} = S_t^{\nu} \pm \left(\frac{1}{2}\Delta + f(\nu_t)\right) \,, \qquad \qquad \hat{S}_0^{\nu} = \hat{S} \,, \tag{6.1c}$$

where

- f : lR+ -+ lR+ denotes the temporary price impact that the agent's trading action has on the price they can execute the trade at, and
- fl 2: 0 is the bid-ask spread, assumed here to be a constant.

Equations (6.la, 6.lb, and 6.lc) apply to both liquidation and acquisition problems, where the sign ± changes depending on whether the problem is that of liquidating ( -) or acquiring ( +) shares.

In equity markets the fundamental price of the asset (also known in the literature as the efficient price or true price of the asset) refers to the share price that reflects fundamental information about the value of the firm and this is impounded in the price of the share. In this chapter we assume that during the optimal execution trading period the fundamental price is the same as the midprice of the asset. Thus, as new information about the actual and expected performance of the firm is revealed to the market, the mid price changes. This is partly captured in the model by the increments of the Brownian motion *W* in (6.lb).

A key element of the model is how the agent's trades affect the midprice. Here the agent's market orders affect the midprice in two ways: through f (vt) in (6.lc), and through g(vt) in (6.lb). These functions capture two different ways in which the agent's trades affect the midprice.

At any one time, the number of shares displayed and available in the market at the quoted bid/ask prices *S{* ± ½fl is limited. A large MO will walk the book, so that the average price per share obtained will be worse than the current bid/ ask price. This is captured in our model, as an order of size v dt will obtain an execution price per share of S{ ±(½ fl+ f(v)) with f(v) 2'. 0. Note, however, that the impact of the order as captured by f (vt) is limited to the execution price and does not affect the midprice of the asset.

In Figure 6.1 we show a snapshot of the LOB (top left panel) for SMH on Oct 1, 2013 at 11am, together with the price impact per share (top right panel) that an MO of various volumes would face as it walks through the buy side of the LOB. The bottom left panel shows the impact every second from 11:00 to 11:01 as well as the average of those curves over the minute (the dash-dotted line).

137

![](_page_3_Figure_1.jpeg)

**Figure 6.1** An illustration of how the temporary impact may be estimated from snapshots of the LOB using SMH on Oct 1, 2013. The top two panels are at  $11:00\text{am}$ . The bottom left from 11:00am to 11:01am and the bottom right the entire day.

We also include a linear regression (the dashed line) with intercept set to the half-spread; this would correspond to a linear impact function  $f(\nu_t)$ , which is the simple model we adopt in this chapter, and which is also widely used. Figure 6.1 illustrates that the  $f(\nu_t)$  function seems better described by a power law, and the model can be extended to incorporated this. We discuss this extension in Section  $6.7$ .

Notice that the impact function fluctuates within the minute, and with it the impact that trades of different size have. The linear regression provides an approximation of the temporary impact during that one minute. The bottom right panel shows how the slope of this linear impact model fluctuates throughout the entire day. We see that the largest impact tends to occur in the morning, then this impact flattens and stays flat throughout the day, and towards the end of the day it lessens. Such a pattern is seen in a number of assets.

The second way in which the agent's execution can affect the midprice is through  $g(\nu_t)$ . We refer to this as the permanent impact of the trading rate. If  $q(\nu_t) > 0$  in (6.1b) then a trade of size  $\nu \, dt > 0$  moves the midprice of the asset upwards. An interpretation of this modelling assumption is that the agent is trading on information that reflects permanent changes in the value of the firm, and market participants adjust their quotes in response to the agent's trades. Earlier on, in Chapter 4 we discussed linear market impact models and estimated the parameters for various stocks, see in particular subsection 4.3.5.

The model can also be modified to incorporate the situation where the agent's trades exert pressure on the midprice and then the pressure subsides after the agent has completed her execution target. But, as we are focusing on an agent's execution of a single block of shares, this is not relevant as she will never receive any of the benefits of the 'price correction' once she stops trading, and we exclude it from the analysis.

To conclude the description of the model, we turn to the agent's cash process, *x;:.* This process satisfies the SDE

$$dX_t^v = \hat{S}_t^{\nu} \nu_t \, dt \,, \qquad X_0^v = x \,, \tag{6.2}$$

and the expected revenue from the sale is

$$R^{\nu} = \mathbb{E}\left[X_T^{\nu}\right] = \mathbb{E}\left[\int_0^T \hat{S}_t \,\nu_t \,dt\right] \,,\tag{6.3}$$

which is easy to see if we look at the sales proceeds over discrete time-steps. Suppose that the agent must liquidate Q*0* = 5Jt amount of shares over the time period [O, T]. Now, split this trading horizon into equally spaced time intervals to = 0 < t1 < t2 < · · · < tN = *<sup>T</sup>* where tn - tn-1 = 6.t for n = l, 2, · · · , *N.* Next, assuming that over the time interval [O, t<sup>1</sup> ) the agent sells Qo - Qt, shares at the price So, and over the interval [ti, t2) she sells Qt, - **Qt**2 at the price St,, and so on, then the total expected revenue from selling shares is

$$R_{\Delta t}^{\nu} = \mathbb{E}\left[ (Q_0 - Q_{t_1}) \hat{S}_0 + (Q_{t_1} - Q_{t_2}) \hat{S}_{t_1} + \dots + (Q_{t_{N-1}} - Q_T) \hat{S}_{t_{N-1}} \right],$$

and recalling that the speed of trading is given by (6.la) we observe that as 6.t-+ 0 we obtain (6.3).

The rest of this chapter looks at different optimal strategies to trade a block of shares using only MOs, where in each section the setup of the control problem makes different assumptions about how the agent penalises and/ or controls inventory, and how her rate of trading affects her execution price as well as the midprice of the asset. We also alternate between share liquidation and share acquisition problems. In Section 6.3 the agent must liquidate a block of shares, and the agent's trades affect her execution price but do not affect the midprice of the asset *(g(v)* = 0). The setup of the problem assumes that the execution strategy is designed so that all shares are liquidated by the terminal date. In Section 6.4 the agent solves for the optimal acquisition rate where any remaining unacquired inventory may be purchased at the terminal date but subject to a penalty (and *g* ( *v)* = 0). In Section 6. 5 the agent has to liquidate a block of shares, and the agent's actions have both a permanent effect *(g( v)* :2': 0) on the execution price and a temporary effect *(.f(v)* :2': 0) on the midprice of the asset. In addition, we incorporate a parameter for the agent's urgency to execute the trade, through a penalisation exposure to inventory throughout the entire life of the strategy.

#### 6.3 Liquidation without Penalties only Temporary Impact

We start by discussing how an agent uses only MOs to optimally liquidate  $\mathfrak{N}$ shares between  $t = 0$  and T. We assume that the agent's own trades do not affect the midprice of the asset, thus the stock's midprice is as in  $(6.1b)$  with  $g(\nu_t) = 0$ . On the other hand, the agent's trades have temporary impact on her own execution price because these MOs walk the LOB. We assume that the temporary impact is linear in the speed of trading so  $f(\nu_t) = k \nu_t$  with  $k > 0$ in (6.1c) and recall that the speed of trading  $\nu_t$  is what the agent controls. For simplicity, we assume that the bid-ask spread  $\Delta = 0$ , or equivalently, that  $S_t$ represents the best bid price. It is a simple matter to include a non-zero spread and we leave it as an exercise for the interested reader. Finally, we also assume that the agent is adamant that all  $\mathfrak{N}$  shares are liquidated by time T.

The agent's objective is to choose the rate at which she liquidates  $\mathfrak{N}$  shares so that she obtains the maximum amount of revenue from the sale, and her strategy must be such that all shares are liquidated by time  $T$ , i.e. cannot reach expiry with any inventory left. In other words the agent wishes to find, among all admissible liquidation strategies  $\nu$ , the one that minimises the execution cost

$$EC^{\nu} = \Re\,S_0 - \mathbb{E}\left[\int_0^T \hat{S}_t^{\nu} \,\nu_t \,dt\right].$$

which is equivalent to maximising the expected revenues from the target sale of the  $\mathfrak{N}$  shares. Thus the agent's value function is

$$H(t, S, q) = \sup_{\nu \in \mathcal{A}} \mathbb{E}_{t, S, q} \left[ \int_{t}^{T} \left( S_{u} - k \nu_{u} \right) \nu_{u} \ du \right]$$

where  $\mathbb{E}_{t,S,q}[\cdot]$  denotes expectation conditional on  $S_t = S$  and  $Q_t = q$ , and  $\mathcal{A}$  is the set of admissible strategies:  $\mathcal{F}$ -predictable non-negative bounded strategies. This constraint excludes repurchasing of shares and keeps the liquidation rate finite.

To solve this optimal control problem we use the dynamic programming principle (DPP) which suggests that the value function satisfies the dynamic pro- $\text{gramming equation (DPE)}$ 

$$\partial_t H + \frac{1}{2} \sigma^2 \,\partial_{SS} H + \sup_{\nu} \left\{ (S - k\,\nu) \,\nu - \nu \,\partial_q H \right\} = 0 \,. \tag{6.4}$$

The agent requires that the optimal strategy liquidates all the inventory by time  $T$ , thus the value function reflects this by 'penalising' any terminal inventory which is not zero, so we require

 $H(T, S, q) \xrightarrow{t \to T} -\infty$ , for  $q > 0$ ,

and

$$H(T, S, 0) \xrightarrow{t \to T} 0.$$

The first order condition applied to DPE  $(6.4)$  shows that it attains a supre- $\text{mum at}$ 

$$\nu^* = \frac{1}{2k} \left( S - \partial_q H \right) \,, \tag{6.5}$$

which is the optimal trading speed in feedback control form. Upon substitution into the DPE we obtain the non-linear partial differential equation

$$\partial_t H + \frac{1}{2} \sigma^2 \partial_{SS} H + \frac{1}{4k} \left( S - \partial_q H \right)^2 = 0 \tag{6.6}$$

for the value function.

To propose an ansatz for the above equation it is helpful to look at the boundary conditions to get an idea of which variables are relevant in the value function. We know that if the strategy reaches the terminal date with a non-zero inventory, the value function must become arbitrarily large and negative  $-$  because the optimal strategy must ensure that all shares are liquidated. We propose that the value function be written in terms of the book value of the current inventory (marked-to-market using the midprice as reference) plus the excess value due to optimally liquidating the remaining shares, i.e.

$$H(t, S, q) = q S + h(t, q), \qquad (6.7)$$

where  $h(t,q)$  is still to be determined, though we know that it must blow up as t approaches  $T$ .

The way the problem is set up, the best the agent can do is achieve the midprice. Hence, the correction  $h(t,q)$  to the book value must be negative, and the agent's objective is to minimise this downward adjustment. Substituting this ansatz into the DPE (6.6), we arrive at the following equation for  $h(t, q)$ :

$$\partial_t h + \frac{1}{4k} \left( \partial_q h \right)^2 = 0.$$

Interestingly, the volatility of the asset's midprice drops out of the problem. The reason for this is that the Brownian component is a martingale, and hence on average it contributes zero to the value of liquidating shares.

Focusing on the above non-linear PDE for  $h$ , we see that writing a separation of variables in the form  $h(t,q) = q^2 h_2(t)$  (note the subscript 2 represents that this function is the coefficient of  $q^2$ ) allows us to factor out q and obtain a simple non-linear ODE for  $h_2(t)$ :

$$\partial_t h_2 + \frac{1}{k} h_2^2 = 0, \qquad (6.8)$$

which we solve by integrating between  $t$  and  $T$  to obtain

$$h_2(t) = \left(\frac{1}{h_2(T)} - \frac{1}{k}(T - t)\right)^{-1}$$

As discussed above, the optimal strategy must ensure that the terminal inventory is zero and this is equivalent to requiring  $h_2(t) \to -\infty$  as  $t \to T$ . In this way the value function heavily penalises non-zero final inventory. An alternative way to obtain this condition is to calculate the inventory path along the optimal strategy and impose that the terminal inventory be zero. To see this, use the ansatz  $(6.7)$  to reduce  $(6.5)$  to

$$\nu_t^* = -\frac{1}{k} h_2(t) Q_t^{\nu^*}, \n$$
(6.9)

then integrate  $dQ_t^{\nu^*} = -\nu_t^* dt$  over  $[0, t]$  to obtain the inventory profile along the optimal strategy:

$$\int_{0}^{t} \frac{dQ_{t}^{\nu^{*}}}{Q_{t}^{\nu^{*}}} = \int_{0}^{t} \frac{h_{2}(s)}{k} ds \quad \Rightarrow \quad Q_{t}^{\nu^{*}} = \frac{(T-t) - k/h_{2}(T)}{T - k/h_{2}(T)} \,\mathfrak{N}$$

To satisfy the terminal inventory condition  $Q_T^{\nu^*} = 0$ , and also ensure that the correction  $h(t,q)$  to the book value of the outstanding shares that need to be liquidated is negative, we must have

$$h_2(t) \to -\infty \quad \text{as} \quad t \to T \,.$$
 (6.10)

Returning to solving the optimal problem, we have that

$$h_2(t) = -k (T - t)^{-1},$$

so the optimal inventory to hold is

$$Q_t^{\nu^*} = \left(1 - \frac{t}{T}\right) \mathfrak{N},\tag{6.11}$$

and the optimal speed of trading is

$$\nu_t^* = \frac{\mathfrak{N}}{T}.\n$$
(6.12)

This final result for the optimal trading speed is quite simple: the shares must be liquidated at a constant rate and this strategy is the same as that of the **time** weighted average price  $(TWAP)$ .

### 6.4 **Optimal Acquisition with Terminal Penalty and Temporary** Impact

The problem now is to acquire (not liquidate)  $\mathfrak{N}$  shares by time T, starting with  $Q_0^{\nu} = 0$ . As in the previous section the agent's MOs walk the LOB so her execution price is described by (6.1c) with  $f(\nu) = k \nu, k > 0$ .

Although the agent's objective is to complete the acquisition programme by time T, she allows for strategies that fall short of this target,  $Q_T^{\nu} < \mathfrak{N}$ , and in this case she must execute a buy MO for the remaining amount and pick up an additional penalty. This terminal inventory penalty is parameterised by  $\alpha > 0$ , which includes the cost of walking the book at T and any other additional penalties that the agent must incur for the execution of the trade at the terminal date.

Thus, the agent's expected costs from strategy  $\nu_t$  is

$$EC^{\nu} = \mathbb{E}\Big[\underbrace{\int_{t}^{T} \hat{S}_{u}^{\nu} \nu_{u} \, du}_{\text{Terminal Cash}} + \underbrace{(\mathfrak{N} - Q_{T}^{\nu}) \, S_{T}}_{\text{Terminal execution at mid}} + \underbrace{\alpha \, (\mathfrak{N} - Q_{T}^{\nu})^{2}}_{\text{Terminal Penalty}}\Big] \,. \tag{6.13}$$

Compared to the expected costs in the previous section we have two additional terms. In the liquidation problem of the previous section, the agent seeks a strategy that ensures all shares are liquidated by  $T$  and the expected costs arise exclusively from continuous trading. Now, the agent can reach  $T$  short of her target, but this generates the additional terms that incorporate that sale plus the penalty to purchase the remaining shares at the terminal date.

To simplify notation, we introduce a new stochastic process  $Y = (Y_t)_{0 \le t \le T}$ to denote the shares remaining to be purchased between  $t$  and the end of the trading horizon  $T$ :

$$Y_t^{\nu} = \mathfrak{N} - Q_t^{\nu} \,, \qquad \text{so that} \qquad dY_t^{\nu} = -\nu_t \, dt \,,$$

and write the value function as

$$H(t, S, y) = \inf_{\nu \in \mathcal{A}} \mathbb{E}_{t, S, y} \left[ \int_t^T \hat{S}_u^{\nu} \nu_u \, du + Y_T^{\nu} S_T + \alpha \left( Y_T^{\nu} \right)^2 \right] \,,$$

where it is clear that the strategy seeks to minimise the cash paid to acquire the  $\text{shares.}$ 

Applying the DPP, we expect that the value function should satisfy the DPE

$$0 = \partial_t H + \frac{1}{2}\sigma^2 \partial_{SS} H + \inf_{\nu} \left\{ (S + k\nu) \nu - \nu \partial_y H \right\} ,\qquad (6.14)$$

with terminal condition  $H(T, S, y) = yS + \alpha y^2$ . Solving for the first order conditions, the optimal speed of trading in feedback form is given by

$$\nu^* = \frac{1}{2k} \left( \partial_y H - S \right) \,, \tag{6.15}$$

and upon substitution into the DPE above, we obtain

$$\partial_t H + \frac{1}{2}\sigma^2 \partial_{SS} H - \frac{1}{4k} \left( \partial_y H - S \right)^2 = 0.$$

To solve this DPE, we can write the value function in terms of the book value of the assets remaining to be acquired and the excess value function from optimally acquiring these shares. From looking at the terminal condition, and the way y enters into the DPE, we hypothesise that the excess value function can be written in terms of a quadratic function in  $y$ . The corresponding ansatz is

$$H(t, S, y) = y S + h_0(t) + h_1(t) y + h_2(t) y^2,$$
(6.16)

where  $h_2(t)$ ,  $h_1(t)$ ,  $h_0(t)$  are, yet to be determined, deterministic functions of time (note that the subscripts on the functions indicate the power of  $y$  which multiplies them in the full ansatz). Recalling that the value function at the terminal date T is  $H(T, S, y) = y S + \alpha y^2$ , then

$$h_2(T) = \alpha$$
 and  $h_1(T) = h_0(T) = 0$ .

Moreover, upon substituting the ansatz into the above non-linear PDE we find that

$$0 = \left\{ \partial_t h_2 - \frac{1}{k} h_2^2 \right\} y^2 + \left\{ \partial_t h_1 - \frac{1}{2k} h_2 h_1 \right\} y + \left\{ \partial_t h_0 - \frac{1}{4k} h_1^2 \right\} .$$

Since this equation must be valid for each  $y$ , each term in braces must individually vanish. This provides us with three equations for the three functions  $h_0$ ,  $h_1$  and  $h_2$ . Due to the terminal condition  $h_1(T) = 0$ , we see that the solution we get for  $h_1$  (by setting the second term in braces to zero) is  $h_1(t) = 0$ . Similarly, due to the terminal condition  $h_0(T) = 0$ , we see that the solution we get for  $h_0$  (by setting the third term in braces to zero, and knowing that  $h_1(t) = 0$  is  $h_0(t) = 0$ . Indeed we could have begun with the ansatz  $H(t, S, y) = y S + h_2(t) y^2$  and have ended up with the same equation for  $h_2$ . The final equation (obtained by setting the first term in braces to zero) allows us to obtain  $h_2(t)$  and in this case, since  $h_2(T) = \alpha$ , we obtain the non-trivial solution

$$h_2(t) = \left(\frac{1}{k}\left(T - t\right) + \frac{1}{\alpha}\right)^{-1}$$

Putting this together with the ansatz for the value function we find that the optimal trading speed is

$$\nu_t^* = \left( (T - t) + \frac{k}{\alpha} \right)^{-1} Y_t^{\nu^*} \,. \tag{6.17}$$

Here we see that as the terminal penalty parameter  $\alpha \to \infty$  the acquisition rate converges to that of TWAP. Similarly, the smaller the value of  $\alpha$ , all else being equal, the slower the acquisition rate will be. Furthermore, in the limiting case  $\alpha \to 0$ , the optimal strategy is not to purchase any shares until the terminal date is reached, at which point all  $\mathfrak{N}$  shares are purchased. In this limiting case, there are no costs of walking the book at date  $T$ , so it is optimal to purchase all the inventory at the end. In general, however, we expect that  $\alpha \gg k$ .

As before, we can solve for the optimal inventory path explicitly by integrating  $dY_t^{\nu^*} = -\nu_t^* dt$  over  $[0, t]$ , i.e. by solving

$$dY_t^{\nu^*} = -\left( (T - t) + \frac{k}{\alpha} \right)^{-1} Y_t^{\nu^*} dt$$

for  $Y_t^{\nu^*}$ . Recalling that  $Y_t^{\nu} = \mathfrak{N} - Q_t^{\nu}$ , it is straightforward to obtain the optimal inventory path as

$$Q_t^{\nu^*} = \frac{t}{T + \frac{k}{\alpha}} \mathfrak{N}.$$
 (6.18)

From this equation we can see that for any finite  $\alpha > 0$  and finite  $k > 0$ , it is always optimal to leave some shares to be executed at the terminal date, and the fraction of shares left to execute at the end decreases with the relative price impact at the terminal date,  $k/\alpha$ .

To obtain the optimal speed of acquisition, we substitute for  $Q_t^{\nu^*}$  into the

expression for  $\nu_t^*$ , so that

$$\nu_t^* = \frac{\mathfrak{N}}{T + \frac{k}{\alpha}}\n$$
(6.19)

Comparing this with the result from the previous section (see  $(6.11)$  and  $(6.12)$ , we see that the agent acquires at a constant, but slower rate than that of an agent who heavily penalises (i.e.  $\alpha \to \infty$ ) paths which do not complete the execution fully. Moreover, the agent trades at a constant speed and this speed is the same as that of an agent who must execute everything by the end of the period, but who has a terminal date  $T'$  that is further into the future,  $T' = T + \frac{k}{\alpha}$ .

#### 6.5 Liquidation with Permanent Price Impact

In this section we switch from acquisition back to liquidation. The agent continues to use only MOs to liquidate a total of  $\mathfrak{N}$  shares, but now her trades have both a temporary and a permanent price impact. The midprice dynamics are given by (6.1b) with drift  $g(\nu_t) > 0$ , which enters the equation with negative sign because the agent's sell trades exert a permanent downward pressure, and the execution price by (6.1c) with  $f(\nu_t) > 0$ , which enters the equation with a negative sign because the sell trades have an adverse temporary impact. Here we assume that if the agent's strategy reaches the terminal date  $T$  with inventory left, then she must execute an MO to reach  $\mathfrak{N}$  for a total revenue of  $Q_T^{\nu}(S_T^{\nu}-\alpha Q_T^{\nu}),$  where  $\alpha \geq 0$  is the terminal liquidation penalty parameter. The agent's objective is to minimise the execution cost

$$EC^{\nu} = \Re\,S_0 - \mathbb{E}\Big[\underbrace{X_T^{\nu}}_{\text{Terminal Cash}} + Q_T^{\nu}\,(\underbrace{S_T^{\nu}}_{\text{Midprice}} - \underbrace{\alpha\,Q_T^{\nu}}_{\text{Penalty per Share}})\Big],$$

where the process corresponding to the investor's wealth  $X^{\nu}_{\nu}$  is as in (6.2). Here we have switched from writing out the cash process explicitly in terms of the integrated execution costs, to including the cash process directly. This way the cash process becomes a state variable. Naturally, we could in principle keep using the integrated costs representation; however, it is sometimes easier to motivate the choice of ansatz for the forthcoming problems when value functions are written in terms of  $X$  as a state variable.

In this section, we also introduce another element into the model: a running inventory penalty of the form  $\phi \int_t^T (Q_u^{\nu})^2$  with  $\phi \geq 0$ . This running inventory penalty is not (and should not be considered) a financial cost to the agent's strategy. The parameter  $\phi$  allows us to incorporate the agent's urgency for executing the trade. The higher the value of  $\phi$ , the quicker the optimal strategy liquidates the shares, as it increases the penalty for the late liquidation of shares and incentivises strategies that front load the liquidation of inventory. Cartea, Donnelly  $\&$  Jaimungal (2013) show that the running inventory penalty is equivalent to

introducing ambiguity aversion on the part of the agent, where the ambiguity is over the midprice which, in their model, may have a non-zero stochastic drift.

Then, the agent's performance criterion is

$$H^{\nu}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ \underbrace{X_{T}^{\nu}}_{\text{Terminal Cash}} + \underbrace{Q_{T}^{\nu}(S_{T}^{\nu} - \alpha Q_{T}^{\nu})}_{\text{Terminal Execution}} - \underbrace{\phi \int_{t}^{T} (Q_{u}^{\nu})^{2} du}_{\text{Inventory Penalty}} \right], \tag{6.20}$$

and the value function

$$H(t, x, S, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, q)$$

The DPP implies that the value function should satisfy the HJB equation

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)H - \phi q^2 + \sup_{\nu} \left\{ \left(\nu \left(S - f(\nu)\right)\partial_x - g(\nu)\,\partial_S - \nu\,\partial_q\right)H \right\} \,, \tag{6.21}$$

subject to the terminal condition  $H(T, x, S, q) = x + S q - \alpha q^2$ .

We use the simplifying assumption that permanent and temporary price impact functions are linear in the speed of trading, i.e.  $f(\nu) = k \nu$  and  $g(\nu) = b \nu$ for finite constants  $k > 0$  and  $b > 0$ . The first order condition allows us to obtain the optimal speed of trading in feedback control form as

$$\nu^* = \frac{1}{2k} \frac{(S \,\partial_{\mathcal{C}} \,\overline{\phantom{a}} \, b \,\partial_S - \partial_q)H}{\partial_x H} \,.\n$$
(6.22)

Upon substituting the optimal feedback control into the DPE, it reduces to

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)H - \phi \,q^2 + \frac{1}{4\,k} \frac{\left[ (S \,\partial_x - b \,\partial_S - \partial_q)H \right]^2}{\partial_x H}$$

By inspecting the terminal condition  $H(T, x, S, q) = x + Sq - \alpha q^2$ , it suggests  $\text{the ansatz}$ 

$$H(t, x, S, q) = x + S q + h(t, S, q), \qquad (6.23)$$

where h, with terminal condition  $h(T, S, q) = -\alpha q^2$ , is yet to be determined. The first term of the ansatz is the accumulated cash of the strategy, the second is the marked-to-market book value (at midprice) of the remaining inventory, and  $h$  is the extra value stemming from optimally liquidating the rest of the shares.

Using this ansatz in the equation above and simplifying, we find the following non-linear PDE for  $h$ :

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)h - \phi \,q^2 + \frac{1}{4k} \left[b\left(q + \partial_S h\right) + \partial_q h\right]^2 \,.$$

Since the above PDE contains no explicit dependence on  $S$  and the terminal condition is independent of S, it follows that  $\partial_S h(t, S, q) = 0$ , and we can write  $h(t, S, q) = h(t, q)$  (with a slight abuse of notation). The equation then simplifies even further to

$$0 = \partial_t h(t, q) - \phi q^2 + \frac{1}{4k} \left[ b q + \partial_q h(t, q) \right]^2 \ .$$

Furthermore, the optimal control in feedback form from  $(6.22)$  takes on the much  $\text{more compact form}$ 

$$\nu^* = -\frac{1}{2k} \left( \partial_q h(t, q) + b \, q \right) \,. \tag{6.24}$$

In this form, it appears that the solution admits a separation of variables  $h(t,q) = h_2(t) q^2$  where  $h_2(t)$  satisfies the non-linear ODE (recall that the subscript 2 represents that this function is the coefficient of  $q^2$ )

$$0 = \partial_t h_2 - \phi + \frac{1}{k} \left[ h_2 + \frac{1}{2} b \right]^2 , \qquad (6.25)$$

subject to the terminal condition  $h_2(T) = -\alpha$ . This ODE is of Riccati type and can be integrated exactly. First, let  $h_2(t) = -\frac{1}{2}b + \chi(t)$ , then re-arranging the  $\text{ODE}$  we obtain

$$\frac{\partial_t \chi}{k\phi - \chi^2} = \frac{1}{k} \; ,$$

subject to  $\chi(T) = \frac{1}{2}b - \alpha$ . Next, integrating both sides of the above over  $[t, T]$ yields

$$\log \frac{\sqrt{k\phi} + \chi(T)}{\sqrt{k\phi} - \chi(T)} - \log \frac{\sqrt{k\phi} + \chi(t)}{\sqrt{k\phi} - \chi(t)} = 2\gamma (T - t),$$

so that

$$\chi(t) = \sqrt{k\,\phi} \, \frac{1+\zeta \, e^{2\gamma\,(T-t)}}{1-\zeta \, e^{2\gamma(T-t)}} \,,$$

where

$$\gamma = \sqrt{\frac{\phi}{k}} \quad \text{and} \quad \zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{k\phi}}{\alpha - \frac{1}{2}b - \sqrt{k\phi}} \ . \n$$
(6.26)

At this point the solution of the DPE is fully determined and the optimal speed of trading can now be explicitly shown in terms of the state variables rather than in feedback form. Specifically, from  $(6.24)$ , the optimal speed to trade at is

$$\nu_t^* = \gamma \frac{\zeta e^{\gamma (T-t)} + e^{-\gamma (T-t)}}{\zeta e^{\gamma (T-t)} - e^{-\gamma (T-t)}} Q_t^{\nu^*} \,. \n$$
(6.27)

Interestingly, the optimal speed to trade is still proportional to the investor's current inventory level, as we found in the previous simpler models, but now the proportionality factor depends non-linearly on time.

From this expression, it is also possible to obtain the agent's inventory  $Q_t^{\nu^-}$ that results from following this strategy. Recall that the agent's inventory satisfies  $dQ_t^{\nu} = -\nu_t dt$ , hence

$$dQ_t^{\nu^*} = \frac{\chi(t)}{k} Q_t^{\nu^*} dt \quad \text{so that} \quad Q_t^{\nu^*} = \Re \exp\left\{ \int_0^t \frac{\chi(s)}{k} ds \right\} \ .$$

To obtain the inventory along the optimal strategy we first solve the integral

$$\int_{0}^{t} \frac{\chi(s)}{k} ds = \frac{1}{k} \int_{0}^{t} \sqrt{k\phi} \frac{1 + \zeta e^{2\gamma(T-s)}}{1 - \zeta e^{2\gamma(T-s)}} ds$$
$$= \gamma \int_{0}^{t} \frac{e^{-2\gamma(T-s)}}{e^{-2\gamma(T-s)} - \zeta} ds + \gamma \int_{0}^{t} \frac{\zeta e^{2\gamma(T-s)}}{1 - \zeta e^{2\gamma(T-s)}} ds$$
$$= \log \left( e^{-\gamma(T-s)} - \zeta e^{\gamma(T-s)} \right) \Big|_{0}^{t} \tag{6.28}$$

$$= \log \frac{\zeta e^{\gamma(T-t)} - e^{-\gamma(T-t)}}{\zeta e^{\gamma T} - e^{-\gamma T}} , \qquad (6.29)$$

hence

$$Q_t^{\nu^*} = \frac{\zeta e^{\gamma(T-t)} - e^{-\gamma(T-t)}}{\zeta e^{\gamma T} - e^{-\gamma T}} \mathfrak{N} \,.$$

$$(6.30)$$

Substituting this expression into  $(6.27)$  allows us to write the optimal speed to trade as a simple deterministic function of time

$$\nu_t^* = \gamma \, \frac{\zeta \, e^{\gamma \, (T-t)} + e^{-\gamma \, (T-t)}}{\zeta \, e^{\gamma \, T} - e^{-\gamma \, T}} \, \mathfrak{N}$$

In the limit in which the quadratic liquidation penalty goes to infinity, i.e. as  $\alpha \to +\infty$ , we get  $\zeta \to 1$ . Then, the optimal inventory to hold and the optimal speed to trade simplify to

$$Q_t^{\nu^*} \xrightarrow[\alpha \to +\infty]{} \frac{\sinh\left(\gamma(T-t)\right)}{\sinh\left(\gamma T\right)} \mathfrak{N} \,,$$

and

$$\nu_t^* \xrightarrow[\alpha \to +\infty]{} \gamma \frac{\cosh\left(\gamma(T-t)\right)}{\sinh\left(\gamma\,T\right)} \mathfrak{N}$$

Both of these expressions are independent of b. For other values of  $\alpha$  the relationship between  $\alpha$  and the permanent price impact parameter b is more complex and we look at it after considering some numerical examples.

Figure  $6.2$  contains plots of the inventory level under the optimal strategy for two levels of the liquidation penalty  $\alpha$  and several levels of the running penalty  $\phi$ . Note that with no running penalty,  $\phi = 0$ , the strategies are straight lines and in particular, with  $\alpha \to \infty$  the strategy is equivalent to a TWAP strategy. As the running penalty  $\phi$  increases, the trading curves become more convex and the optimal strategy aims to sell more assets sooner. This is an intuitive result since  $\phi$  represents the agent's urgency to liquidate the position, and therefore as it increases she initially liquidates more quickly. Naturally, as the liquidation penalty increases, the terminal inventory is pushed to zero.

As an exercise, one can check that in the limit in which the running penalty vanishes,  $\phi \to 0$ , the analog of the result from the previous section is recovered,

![](_page_14_Figure_1.jpeg)

(b)  $\alpha = +\infty$ 

Figure 6.2 The investor's inventory along the optimal path for various levels of the running penalty  $\phi$ . The remaining model parameters are  $k = 10^{-3}$ ,  $b = 10^{-3}$ .

i.e.

$$Q_t^{\nu^*} \xrightarrow[\phi \to 0]{} \frac{t}{T + \frac{k}{\alpha}}$$

### Equivalence Between Permanent Price Impact and Terminal Liquidation Penalty

In the previous section we solved the general case when the agent's trades have temporary impact on the execution price and permanent impact on the midprice. We assumed that these two impacts were linear in the speed of trading,  $f(\nu)$  =  $k\nu$  and  $g(\nu) = b\nu$  for constants  $k \geq 0$  and  $b \geq 0$ . One typically observes that  $b \ll k$  and we also assume that the liquidation penalty parameter  $\alpha \gg k$ . In this section we discuss the relationship between the liquidation penalty parameter  $\alpha$  and the permanent price impact parameter  $b$  – the discussion for acquisition problems is very similar.

The basis for the analysis comes from observing that in the optimal speed of trading, as described in  $(6.27)$ , the permanent impact and the liquidation penalty always appear in the form  $\alpha - \frac{1}{2}b$ , see (6.26). This implies that in the current model, where the permanent impact is linear in the speed of trading and the liquidation of terminal inventory is quadratic,  $\alpha Q_T^2$ , one could define a single parameter  $c = \alpha - \frac{1}{2}b$  (so that  $c = \chi(T)$ ) to describe how both the permanent

impact and the liquidation penalty affect the optimal speed of trading. Obviously, we cannot do this for other variables in the model, such as for the cash obtained from liquidating shares. The impact of the permanent price impact parameter on this variable is quite distinct from that of the liquidation penalty.

To see this, we consider how the proceeds from selling the  $\mathfrak{N}$  shares are affected by the permanent impact that the agent's trades have on the midprice. First, we calculate the agent's terminal cash when she follows an arbitrary strategy  $\nu_t$ . Recall that the agent's cash position satisfies the SDE

$$dX_t^{\nu} = (S_t^{\nu} - k\,\nu_t)\,\nu_t\,dt\,,$$

where

$$dS_t^{\nu} = -b\,\nu\,dt + \sigma\,dW_t\,,$$

and, for simplicity, assume that  $X_0 = 0$ ,  $k = 0$ , and  $S_0 = 0$ . Then, the revenue from liquidating her shares, including the liquidation of the terminal inventory, is

$$\begin{split} R^{\nu} &= \int_{0}^{T} S_{t}^{\nu} \,\nu_{t} \, dt + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha Q_{T}^{\nu} \right) \\ &= \int_{0}^{T} \left\{ -b \int_{0}^{t} \nu_{u} \, du + \sigma \, W_{t} \right\} \,\nu_{t} \, dt + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha \, Q_{T}^{\nu} \right) \\ &= \int_{0}^{T} \left\{ -b \left( \mathfrak{N} - Q_{t}^{\nu} \right) + \sigma \, W_{t} \right\} \,\nu_{t} \, dt + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha \, Q_{T}^{\nu} \right) \\ &= \int_{0}^{T} \left\{ -b \left( \mathfrak{N} - Q_{t}^{\nu} \right) + \sigma W_{t} \right\} \left( -dQ_{t}^{\nu} \right) + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha \, Q_{T}^{\nu} \right) \\ &= -b \int_{0}^{T} \left( \mathfrak{N} - Q_{t}^{\nu} \right) d(\mathfrak{N} - Q_{t}^{\nu}) - \sigma \int_{0}^{T} W_{t} \, dQ_{t}^{\nu} + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha \, Q_{T}^{\nu} \right) \\ &= -\frac{1}{2} \, b \left( \mathfrak{N} - Q_{T}^{\nu} \right)^{2} + Q_{T}^{\nu} \left( S_{T}^{\nu} - \alpha \, Q_{T}^{\nu} \right) - \sigma \int_{0}^{T} W_{t} \, dQ_{t}^{\nu} \,. \end{split}$$

Having expressed  $R^{\nu}$  in this way, we see that both  $\alpha$  and b appear together with  $(Q_T^{\nu})^2$  and both act to penalise inventories different from zero. Nevertheless, if we isolate the terms in  $R^{\nu}$  that are affected by  $\alpha$  and b we obtain

$$R^{\nu} = -\frac{1}{2} b \left( \mathfrak{N}^2 - 2 \mathfrak{N} Q_T^{\nu} \right) - \left( \frac{1}{2} b + \alpha \right) \left( Q_T^{\nu} \right)^2 + Q_T^{\nu} S_T^{\nu} - \sigma \int_0^T W_t \, dQ_t^{\nu} \, .$$

It is now clear that not only do  $\alpha$  and b affect the revenue process in a very different way than they do the speed of trading, but also that the effect of the parameter of the permanent price impact cannot be absorbed into the liquidation penalty.

Indeed, b shows up explicitly in the value function separately from  $\alpha$ . First note that  $\alpha$  and b do appear in  $\chi(t)$  together in the form  $c = \alpha - \frac{1}{2}b$  (through ζ). But, b appears separately through the relationship of  $h_2(t) = \chi(t) - \frac{1}{2}b$ . Since  $\chi(t)$  is what determines the optimal trading strategy, we see that b can be absorbed into  $\alpha$  for the purpose of the trading strategy. But this effect does not extend to the revenue process. We can see this most clearly when the agent follows the optimal strategy in the limiting case where  $\alpha \to \infty$ . In this limiting case, the agent will complete the trade by the terminal date, hence  $Q_T^{\nu^*} = 0$ , and any terminal penalty would be applied to a terminal quantity equal to zero.

Nevertheless, the impact of the agent's trades on the midprice will be strictly positive: a loss of  $\frac{1}{2} b \mathfrak{N}^2$ .

### 6.6 **Execution with Exponential Utility Maximiser**

In the previous sections, the agent was viewed as a risk-neutral one in the sense that she is maximising her expected terminal wealth (from optimally trading and liquidating any remaining shares at maturity). With the exception of Section  $6.3$ , the agent is not strictly risk-neutral because she is also penalising holding inventory – which is a form of risk aversion. In this section, we demonstrate that if the agent is risk-averse with exponential utility then she acts in the same manner as the risk-neutral, but inventory averse, agent studied in the previous sections.

Let us consider the agent who sets preferences based on expected utility of terminal wealth with exponential utility:  $u(x) = -e^{-\gamma x}$ . Her performance criteria is

$$H^{\nu}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \Big[ -\exp\Big\{-\gamma \Big(X_T^{\nu} + Q_T^{\nu} \left(S_T^{\nu} - \alpha Q_T^{\nu}\right) \Big) \Big\} \Big],$$

and her value function is

$$H(t, x, S, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, q),$$

where  $S^{\nu}$ ,  $Q^{\nu}$  and  $X^{\nu}$  satisfy, as usual, the equations in (6.1) and (6.2). The agent's terminal wealth has two components: the cash that she has accumulated from trading through  $X_T^{\nu}$ , and the value she receives from liquidating any remaining assets at the end of the trading horizon through  $Q_T^{\nu} \left( S_T^{\nu} - \alpha Q_T^{\nu} \right)$  – which accounts, as before, for the impact of making a lump trade.

Applying the DPP we expect that  $H$  satisfies the DPE

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)H + \sup_{\nu} \left\{ \left(\nu\left(S - k\,\nu\right)\partial_x - b\,\nu\,\partial_S - \nu\,\partial_q\right)H \right\} \,, \tag{6.31a}$$

with terminal condition

$$H(T, x, S, q) = -\exp\{-\gamma \left(x + q \left(S - \alpha q\right)\right)\}.$$
 (6.31b)

The exponential terminal condition suggests that we use the ansatz

$$H(t, x, S, q) = -\exp\{-\gamma (x + q S + h(t, q))\}, \qquad (6.32)$$

and upon substitution into  $(6.31)$ , we find that h satisfies the non-linear PDE

$$0 = -\gamma \, h \, \partial_t h + \tfrac{1}{2} \, \sigma^2 \, \gamma^2 \, q^2 \, h + \sup_{\nu} \left\{ -\gamma \, \nu \, (S - k \, \nu) + \gamma \, q \, b \, \nu + \gamma \, \nu \, (S + \partial_q h) \right\} h \, ,$$

subject to the terminal condition  $h(T,q) = -\alpha q^2$ . Since we expect that h is negative, due to the terminal condition, we can factor out the common  $-\gamma h$ terms and obtain the simpler non-linear PDE

$$0 = \partial_t h - \frac{1}{2} \sigma^2 \gamma q^2 + \sup_{\nu} \left\{ -k \nu^2 - (q \, b + \partial_q h) \, \nu \right\} \,. \tag{6.33}$$

It is straightforward to obtain the optimal control  $\nu^*$  in feedback form as

$$\nu^* = -\frac{1}{2k}(qb + \partial_q h), \qquad (6.34)$$

and upon substitution into  $(6.33)$ , we further find that h solves

$$0 = \partial_t h - \frac{1}{2} \sigma^2 \gamma q^2 + \frac{1}{2k} (q b + \partial_q h)^2.$$

A further observation is that if we consider h to be quadratic in  $q$ , then all the terms in this non-linear equation are quadratic in  $q$ , and so is the terminal condition. Hence, we expect that  $h(t,q) = h_2(t) q^2$  for some deterministic function  $h_2(t)$  with terminal condition  $h_2(T) = -\alpha$  since  $h(T,q) = -\alpha q^2$ . Inserting this second ansatz, and factoring out  $q^2$ , we find that  $h_2(t)$  satisfies the non-linear  $\text{ODE}$ 

$$0 = \partial_t h_2 - \frac{1}{2} \sigma^2 \gamma + \frac{1}{k} \left( h_2 + \frac{1}{2} b \right)^2. \tag{6.35}$$

Comparing (6.35) to (6.25), we see that the two ODEs coincide whenever  $\phi =$  $\frac{1}{2}\gamma\sigma^2$ , and since the terminal conditions are identical, the solutions to the two PDEs are identical. Hence, using the same steps that show how to solve  $(6.25)$ , we find that in the case of an agent with exponential utility preferences, we have

$$h_2(t) = \sqrt{k \gamma \sigma^2} \, \frac{1 + \zeta \, e^{2 \, \xi \, (T - t)}}{1 - \zeta \, e^{2 \, \xi \, (T - t)}} - \frac{1}{2} \, b \,,$$

where the constants

$$\xi = \sqrt{\frac{\gamma \sigma^2}{2 k}} \,, \quad \text{and} \quad \zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{\frac{1}{2}k \gamma \sigma^2}}{\alpha - \frac{1}{2}b - \sqrt{\frac{1}{2}k \gamma \sigma^2}}$$

Recalling that  $h(t,q) = q^2 h_2(t)$  and substituting in the above solution into  $(6.34)$ , we find that the optimal speed to trade is

$$\nu_t^* = \xi \frac{\zeta \, e^{\xi \, (T-t)} + e^{-\xi \, (T-t)}}{\zeta \, e^{\xi \, (T-t)} - e^{-\xi \, (T-t)}} \, Q_t^{\nu^*} \,. \n$$
(6.36)

This strategy is identical in form to the one for the risk-neutral agent who is inventory averse appearing in  $(6.27)$ . Furthermore, the value functions for the two problems (the exponential utility maximiser and the risk-neutral with inventory aversion) can be mapped to one another. From  $(6.32)$ , we have

$$H^{exp-util}(t, x, q, S) = -\exp\left\{-\gamma(x + qS + q^2 h_2(t))\right\},\,$$

where the superscript  $exp-util$  emphasises that this is for the exponential utility maximiser. Similarly, from  $(6.23)$ , we have that

$$H^{inv-aver}(t,x,q,S) = x + qS + q^2 h_2(t),$$

where the superscript  $inv - aver$  emphasises that this is for the inventory averse

agent. Since the h*2* functions coincide when ¢ = ½, <sup>a</sup> *2 ,* we can write the value functions in terms of one another as follows:

$$\begin{split} &\sup_{\nu\in\mathcal{A}}\mathbb{E}\Big[-\exp\Big\{-\gamma\Big(X_T^{\nu}+Q_T^{\nu}\left(S_T^{\nu}-\alpha\,Q_T^{\nu}\right)\Big)\Big\}\Big] \\ &= -\exp\left\{-\gamma\sup_{\nu\in\mathcal{A}}\mathbb{E}\left[X_T^{\nu}+Q_T^{\nu}\left(S_T^{\nu}-\alpha\,Q_T^{\nu}\right)-\frac{\gamma\,\sigma^2}{2}\int_0^T(Q_u^{\nu})^2\,du\right]\right\}. \end{split}$$

In later sections, we see how the agent with exponential utility can be mapped back to a risk-neutral, but inventory averse agent in several different settings. For example, in Section 8.3 we study the mapping when the agent uses LOs to liquidate, in Section 9.5 we see how an agent who aims to target percentage of volume incorporates utility, and in Section 10.3 we investigate how risk-aversion modifies the behaviour of a market marker.

## **6.7 Non-Linear Temporary Price Impact**

In the previous sections we assumed the price impact function *f (v),* see (6.lc), to be linear in the speed of trading. From Figure 6.1, which shows a snapshot of the LOB and how an order of various volumes walks the book, we see that a linear model is a good approximation, but some research has shown that a power law with power less than one fits the data better. Others also argue that, given the extremely low predictive accuracy of market impact models ( typically < 5% *R 2 ),* the cost of increased complexity arising from moving away from a linear model would outweigh any gains from better describing market impact. Nonetheless, it is worthwhile investigating how the problem is modified in the case of non-linear price impact.

To focus on the effects of non-linear impact, we revert back to a risk-neutral agent with inventory aversion through a running penalty as in all sections, other than Section 6.6, and so the agent's performance criteria is as in (6.20) repeated here for convenience:

$$H^{\nu}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \Big[ X^{\nu}_T + Q^{\nu}_T \left( S^{\nu}_T - \alpha \, Q^{\nu}_T \right) - \phi \int_t^T (Q^{\nu}_u)^2 \, du \Big],$$

and the dynamics of s v , x<sup>v</sup>and Q <sup>v</sup>are also repeated here with the explicit non-linear impact model written in place:

$$dS_t^{\nu} = -b \nu_t dt + \sigma dW_t,$$
  

$$dX_t^{\nu} = (S_t^{\nu} - f(\nu_t)) \nu_t dt,$$
  

$$dQ_t^{\nu} = -\nu_t dt.$$

As usual, the DPP suggests that the value function

$$H(t, x, S, q) = \sup_{\nu \in \mathcal{A}} H^{\nu}(t, x, S, q),$$

![](_page_19_Figure_1.jpeg)

Figure 6.3 Graphical representation of the Legendre Transform  $F^*(y)$  of function  $F(x)$ . The point at which the tangent hits the vertical axis is the value of the transform evaluated at the slope at the tangent point.

 $\text{should satisfy the DPE}$ 

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \,\partial_{SS}\right)H - \phi q^2 + \sup_{\nu} \left\{ \left(\nu \left(S - f(\nu)\right)\partial_x - b\,\nu \,\partial_S - \nu \,\partial_q\right)H \right\} \,,$$

with terminal condition  $H(T, x, S, q) = x + q(S - \alpha q)$ . Applying the usual ansatz,  $H(t,x,S,q) = x + qS + h(t,q)$ , which separates out the book value of cash in hand and inventory from the value of optimally trading the remaining shares, we have the following non-linear PDE for  $h$ :

$$0 = \partial_t h - \phi q^2 + \sup_{\nu} \left\{ -\nu f(\nu) - (b q + \partial_q h) \nu \right\},\,$$

with terminal condition  $h(T,q) = -\alpha q^2$ .

To proceed, let us denote  $F(\nu) = \nu f(\nu)$ , and assume that  $\nu f(\nu)$  is convex. The implication is that the net cost (and not the price impact alone) of trading at a rate of  $\nu$  is convex. This certainly holds true for the linear price impact model, for which  $f(\nu) = k \nu$  and so  $F(\nu) = \nu^2$ . It also holds for the popular power law price impact models  $f(\nu) = k \nu^a$  where  $a > 0$ . Under this convexity assumption, the supremum term becomes

$$\sup \left\{-\nu f(\nu) - \left(b q + \partial_q h\right)\nu\right\} = F^* \left(-\left(b q + \partial_q h\right)\right) \,,$$

where  $F^*$  is the **Legendre transform** of the function F defined as

$$F^*(y) = \sup_x \left( x \, y - F(x) \right) \, .$$

The Legendre transform is a mapping from the graph of a function to the set of its tangents, and can be best understood from Figure 6.3. The figure shows that the Legendre transform  $F^*(y)$  of the function F equals the value at which the tangent at a point intersects the vertical axis, and the argument  $y$  is the slope of the function at that tangent point. Since the function is convex, the slope is increasing and therefore for each slope  $y$ , there exists only one point with that slope. Hence, the mapping is one-to-one.

For example, in a power law impact model we write  $f(x) = kx^a$ , and so  $F(x) = k x^{1+a}$ . Then

$$F^*(y) = \sup_x \left( x \, y - k \, x^{1+a} \right) \, .$$

![](_page_20_Figure_1.jpeg)

Figure 6.4 The effect of non-linear impact on the optimal strategy in the case of a power law temporary impact function with power parameter  $a$ . The model parameters are  $b = k = 10^{-4}$ ,  $\phi = 10 k$ ,  $\alpha = 100 k$ , and  $T = 1$ .

We can find the optimal point  $x^*$  from the first order condition

$$y - k(1+a)(x^*)^a = 0 \quad \Rightarrow \quad x^* = \left(\frac{y}{(1+a)k}\right)^{\frac{1}{a}}$$

 $\text{and so}$ 

$$F^*(y) = \xi \, y^{1 + \frac{1}{a}} \,, \qquad \xi = \frac{a \, k}{((1+a) \, k)^{1 + \frac{1}{a}}} \,,$$

and the optimal trading speed in feedback form is

$$\nu^* = \left(\begin{array}{c} b\,q + \partial_q h \\ \hline (1+a)\,k \end{array}\right)^{\frac{1}{a}}.\n$$
(6.37)

We can then write the non-linear PDE for  $h$  as

$$\partial_t h - \phi q^2 + F^* \left( -(b q + \partial_q h) \right) = 0, \quad \text{and} \quad h(t, q) = -\alpha q^2.$$
 (6.38)

In general, this equation cannot be solved analytically, and one must resort to numerical  $PDE$  techniques.

In Figure  $6.4$ , we show the effect of the strength of the power in the power law parameter a on the inventory path from following the optimal strategy  $Q_t^{\nu}$ . These curves are obtained by numerically solving  $(6.38)$  with a finite difference scheme, substituting the solution into  $(6.37)$ , and then numerically integrating  $dQ_t^{\nu^*} = -\nu_t^* dt$ , with  $Q_0^{\nu^*} = 1$ , to obtain  $Q_t^{\nu^*}$ . The striking result is that as the power law parameter decreases, so that orders of the same size have less and less of an impact, the agent liquidates faster. The intuition here is that since trading does not impact prices as much, the agent prefers to liquidate shares early and reduce her inventory risk, and doing so does not cause her to lose too much from temporary market impact. In some sense, the agent behaves as if she has a larger urgency parameter, but still uses a linear impact model.

### 6.8 Bibliography and Selected Readings

Bertsimas & Lo (1998), Large (2007), Obizhaeva & Wang (2013), Bayraktar

& Ludkovski (2011), Schied (2013), Almgren (2003), Almgren, Thum, Hauptmann & Li (2005), Almgren & Chriss (2000), Cont, Kukanov & Stoikov (2013), Lorenz & Almgren (2011), Kharroubi & Pham (2010), Alfonsi, Fruth & Schied (2010), Gatheral (2010), Gatheral, Schied & Slynko (2012), Alfonsi, Schied & Slynko (2012), Schied & Schöneborn (2009), Guéant & Lehalle (2013), Bayraktar & Ludkovski (2012), Guo, De Larrard & Ruan (2013), Gatheral & Schied (2013), Graewe, Horst & Qiu (2013), Graewe, Horst & Séré (2013), Li & Almgren (2014), Almgren (2013), Frei & Westray (2013), Curato, Gatheral & Lillo  $(2014)$ , Jaimungal & Nourian  $(2015)$ .

### 6.9 Exercises

E.6.1 The agent wishes to liquidate  $\mathfrak{N}$  shares between t and T using MOs. The value function is

$$H(t, S, q) = \sup_{\nu \in \mathcal{A}_{t, T}} \mathbb{E}_{t, S, q} \left[ \int_t^T \left( S_u - k v_u \right) \nu_u \, du - Q_T^{\nu} \left( S_T - \alpha Q_T^{\nu} \right)^2 \right],$$

where  $k > 0$  is the temporary market impact,  $\nu_t$  is the speed of trading,  $\alpha \geq 0$ is the liquidation penalty, and  $dS_t = \sigma dW_t$ .

(a) Show that the value function  $H$  satisfies

$$0 = -\left(\partial_q H - S\right)^2 - 4k\partial_t H - 2k\sigma^2 \partial_{SS} H.$$

(b) Make the ansatz

$$H(t, S, q) = h_2(t)q^2 + h_1(t)q + h_0(t) + qS \t\t(6.39)$$

and show that the optimal liquidation rate is

$$\nu_t^* = \frac{Q_t^{\nu^*}}{T - t + \frac{k}{\alpha}}.\n$$

$$(6.40)$$

- (c) Let  $\alpha \to \infty$  and show that (6.40) converges to (6.12). Moreover, discuss the intuition of the strategy when  $\alpha \to 0$ .
- E.6.2 This exercise is similar to that above but with a slightly different setup. The agent wishes to liquidate  $\mathfrak{N}$  shares and her objective is to maximise expected terminal wealth which is denoted by  $X_T^{\nu}$  (in the exercise above we wrote terminal wealth as  $\int_t^T (S_u - kv_u) \nu_u \ du$ ). The value function is

$$H(t, x, S, q) = \sup_{\nu} \mathbb{E}_{t, x, S, q} \left[ X_T^{\nu} - Q_T^{\nu} \left( S_T - \alpha Q_T^{\nu} \right)^2 \right], \tag{6.41}$$

where

$$dX_t^{\nu} = (S_t - k\,\nu_t)\,\nu_t dt. \tag{6.42}$$

(a) Show that the HJB satisfied by the value function *H(t,S,q,x)* is

$$0 = \left(\partial_t + \frac{1}{2}\sigma^2 \partial_{SS}\right)H + \sup_{\nu} \left\{ \left(-\nu \partial_q + \left(S - k\nu\right)\nu \partial_x\right)H \right\} \,, \tag{6.43}$$

and the optimal liquidation rate in feedback form is

$$\nu_t^* = \frac{\partial_q H - S \partial_x H}{-2k \,\partial_x H} \,. \tag{6.44}$$

(b) To solve (6.43), use the terminal condition H(T, x, S, q) = x + q S -aq*<sup>2</sup>*to propose the ansatz

$$H(t, S, x, q) = x + h(t) q^{2} + q S,$$
(6.45)

where h(t) is a deterministic function of time. Show that

$$h(t) = -\frac{k}{T - t + \frac{k}{\alpha}},\tag{6.46}$$

and

$$\nu_t^* = \frac{Q_t^{\nu^*}}{T - t + \frac{k}{\alpha}} \, .$$

$$E.6.3$$
 Let the stock price dynamics satisfy

$$dS_t = \mu \, dt + \sigma \, dW_t \,,$$

where u > 0, µ is a constant and Wt is a standard Brownian motion. The agent wishes to liquidate 5)1 shares and her trades create a temporary adverse move in prices so the price at which she transacts is

$$\hat{S}_t^{\nu} = S_t - k \,\nu_t \,,$$

with k > 0 and the inventory satisfies

$$dQ_t^{\nu} = -\nu_t \, dt \,,$$

where *Vt* is the liquidation rate. Any outstanding inventory at time *T* is liquidated at the midprice and picks up a penalty of a *Q}* where a :::,, 0 is a constant.

The agent's value function is

$$H(t, S, q) = \sup_{\nu} \mathbb{E}_{t, S, q} \left[ \int_{t}^{T} \left( S_{u} - k v_{u} \right) \nu_{u} \, du - Q_{T}^{\nu} \left( S_{T} - \alpha Q_{T}^{\nu} \right)^{2} \right]. \tag{6.47}$$

(a) Show that the optimal liquidation rate in feedback form is

$$\nu^* = \frac{\partial_q H - S}{-2k} \,. \tag{6.48}$$

(b) Use the ansatz  $H(t, S, q) = qS + h(t, S, q)$  to show that the optimal liquidation rate is given by

$$\nu_t^* = \frac{Q_t^{\nu^*}}{(T-t) + \frac{k}{\alpha}} - \frac{1}{4k} \mu \left(T-t\right) \frac{(T-t) + 2\frac{k}{\alpha}}{(T-t) + \frac{k}{\alpha}}$$

Comment on the magnitude of  $\mu$  and the sign of the liquidation rate.

(c) Let  $\alpha \to \infty$  and show that the inventory along the optimal strategy is given by

$$Q_t^{\nu^*} = (T - t) \left(\frac{\mathfrak{N}}{T} + \frac{\mu}{4k}t\right) \, .$$
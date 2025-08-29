# 11 Pairs Trading and Statistical Arbitrage Strategies

# $11.1$ Introduction

The success of many trading algorithms depends on the quality of the predictions of stock price movements. Predictions of the price of a single stock are generally less accurate than predictions of a portfolio of stocks. A classical strategy which makes the most of the predictability of the joint, rather than the individual, behaviour of two assets is **pairs trading** where a portfolio consisting of a linear combination of two assets is traded. At the heart of the strategy is how the two assets co-move – some of these statistical issues were discussed early in Section 3.7. As an example, take two assets whose spread, that is the difference between their prices, exhibits a marked pattern and deviations from it are temporary. Then, pairs trading algorithms profit from betting on the empirical fact that spread deviations tend to return to their historical or predictable level. Thus, pairs trading fall under the class of strategies sometimes labeled as **statisti**cal arbitrage (or StatArb for short). They are not true arbitrages (which are strategies that produce returns in excess of the risk-free rate with zero risk), but rather are strategies which bet off of the typical behaviour of asset prices, and hence are not risk-free.

![](_page_0_Figure_3.jpeg)

Figure 11.1 INTC and SMH on November 1, 2013 for the whole day of trading: (left panel) midprice relative to mean midprice; (right panel) co-integration factor. The dashed line indicates the mean-reverting level, the dash-dotted lines indicate the 2 standard deviation bands.

In Figure 11.1 we show an example with Intel Inc. (INTC) and the Market Vectors Semiconductor ETF (SMH) for November 1, 2013. The left panel shows the midprice paths of INTC and SMH (scaled by the mean midprices), and it is clear that the two assets tend to move together and in the same direction. Thus, a portfolio consisting of long one asset and short the other will exhibit a less volatile and more predictable behaviour than that of the individual assets. In this case, since the assets tend to co-move in the same direction, a simple pairs trading strategy is to buy the portfolio if its value is less than a threshold and sell it if its value is greater than the threshold. This strategy will deliver profits as long as the value of the portfolio fluctuates about and reverts to the threshold.

A more sophisticated approach is to look at the co-integration factor· of the prices of the two stocks. The right panel of Figure 11.1 shows the path of a co-integration factor Ct = *A* s?NTC) + *B* sf MH) ' where *A* and Bare estimated from the data that day to be *A"'* 0.95 and *B"'* -0.63, see Section 3.7. Thus, if the mean-reverting behaviour we have observed is persistent, then we expect the value of a portfolio long 0.95 shares in INTC and short 0.63 shares in SMH to hover around the mean of the co-integration factor which is zero. And how can we profit from the mean-reverting to zero value of this portfolio? The answer is a pairs trading strategy which consists in going long the portfolio when it is 'cheap' and then closing the position when the portfolio's value increases, or going short the portfolio when it is 'dear' and closing the position when the portfolio's value decreases.

In this chapter we present different trading algorithms based on co-integration in the stock price level or in the drift component of a collection of assets. In Section 11.2 we show naive approaches which place ad hoc bands around the mean-reverting level of the co-integration factor so that the strategy enters a position, long or short the portfolio when either band is hit, and then another pair of ad hoc bands to unwind the position. In Section 11.3 we develop more sophisticated approaches which determine the optimal bands to enter and close a position, and in Section 11.4 the drifts of a collection of assets are co-integrated.

## **11.2 Ad Hoc Bands**

A simple strategy to profit from the co-integration factor's mean-reversion, as seen in Figure 11.1, is to place bands which are one standard deviation above and below the mean-reverting level, which is zero, and buy one unit of the portfolio if the lower band is hit or sell one unit of the portfolio if the upper band is hit. Once the strategy has entered into a position, either long or short, the next step is to close it. To close the position the strategy waits for the value of the portfolio to be within a small interval, say 1/10 standard deviation of the meanreverting level of the co-integration factor, and at that point the agent liquidates the position.

![](_page_2_Figure_1.jpeg)

Figure 11.2 shows three pictures: a simulated sample path of the co-integration factor, the path of the inventory of the strategy which opens and closes positions a few times during the trading horizon, and finally, the accumulated cash and marked-to-market value of the strategy. The strategy starts by waiting for the path of the co-integration factor to breach one of the outer bands. At around  $t \sim 0.3$  the path hits the lower outer band so the agent longs the portfolio in anticipation of its value appreciating. Then for a short period of time the agent holds on to the portfolio whose value fluctuates one-to-one with changes in the co-integration factor. The book value of the strategy is given by

$$BV_t = X_t + \beta_t \left( A S_t^{(INTC)} + B S_t^{(SMH)} \right) \,,$$

where  $X_t$  is the strategy's accumulated cash position, and  $\beta_t$  denotes the units of the portfolio held by the strategy, in this case assuming that  $\beta_t \in \{-1, 0, 1\}$ .

The next step is to wait until the co-integration factor hits the inner band to close the position. Here this occurs at around  $t \sim 0.4$  and the strategy goes back to holding zero units of the portfolio and locks in a profit equal to the difference between the outer and inner bands. Next, the strategy waits for a little while and enters into a short position at around  $t \sim 0.51$  and liquidates at around  $t \sim 0.55$ . Finally, the strategy enters into a long position around  $t \sim 0.73$  and liquidates at around  $t \sim 0.83$ . In all, for this simulated path, the strategy makes a profit of three times the outer-inner band spread.

In the scenario in Figure 11.2, the agent ends the trading horizon with zero

![](_page_3_Figure_1.jpeg)

Figure 11.3 P&L histograms from  $10,000$  scenarios using the naive strategy with various trigger bands.

inventory. This is not guaranteed by the strategy, and in fact the strategy may have entered a long/short position which never reverted back to the inner band by the end of the trading horizon. This would induce potential losses into the strategy. The wider the trigger bands, the more likely it is to end with inventory. Also, while wider bands have larger profits when the position closes out, the con-integration factor makes fewer outer-inner band transitions when the band size increases.

Figure 11.3 shows the profit and loss  $(P\&L)$  histogram from generating 10,000 scenarios from the estimated model, computing the co-integration factor and placing trades as described above. The figure shows the effect that the band size has on the  $P\&L$  as well as the Sharpe ratio (i.e. the mean  $P\&L$  divided by the standard deviation of the  $P\&L$ ). Notice that the Sharpe ratio first increases as the band widens, but then starts decreasing. Also notice that when the band size is largest at  $2 \times std.dev$ , the distribution is multimodal. In fact, on close examination, all of the distributions are multimodal. The reason is because the profit from closing out a long/short position equals approximately the band size

(since you enter into a long/short position once the factor hits the band and close it out near the mean). Hence, the P&L is concentrated near integer multiples of the band size and the weight on a given multiple equals the probability of making that many round trip trades during the trading horizon. The reason the P &L is not concentrated solely on the band is because towards the end of the trading horizon, the co-integration factor may not return to the equilibrium value prior to trading end. Hence, the trader must close out a position that might make less profit than the band size, or in fact may take a loss if the co-integration factor moves away from the equilibrium prior to ending the trading horizon.

## 11.3 Optimal Band Selection

In the previous section, we introduced a very simple but naive strategy for entering and exiting a long/short position in the co-integration portfolio. Here, we determine the optimal strategy to enter and exit by posing the problem as an optimal stopping problem. In this context, the trader will make a single round trip trade and there is no terminal time horizon.

First, assume that there is a portfolio with A shares in one asset and B shares in another asset so that the portfolio dynamics are given by *Et,* which is the co-integration factor, and we assume that

$$d\varepsilon_t = \kappa \left(\theta - \varepsilon_t\right) dt + \sigma \, dW_t \,,$$

with Wt a standard Brownian motion. The coefficient "' is the rate of meanreversion, 0 is the level that the process mean-reverts to, and *lT* is the volatility of the process. To formulate the problem, we first solve for the optimal time at which to exit a long position in the portfolio and then use this as the input to determine when the agent should optimally enter a long position in the portfolio. The agent's performance criteria for exiting the long position is given by

$$H_{+}^{(\tau)}(t,\varepsilon) = \mathbb{E}_{t,\varepsilon} \left[ e^{-\rho \, (\tau - t)} (\varepsilon_{\tau} - c) \right] \, ,$$

where c is a transaction cost for closing out the portfolio, p > 0 is the agent's discount factor ( akin to an urgency parameter since increasing p will push the exit boundary in towards the long-run level), lEt,s[·] denotes expectation conditional on *Et* = c, and her corresponding value function is

$$H_{+}(t,\varepsilon) = \sup_{\tau} H_{+}^{(\tau)}(t,\varepsilon) \, .$$

The value function seeks for the optimal stopping time which maximises the performance criteria, because once the agent is long the portfolio the objective is to unwind the position when its value has increased.

Next, the agent's performance criteria for entering the long position is given by

$$G_{+}^{(\tau)}(t,\varepsilon) = \mathbb{E}_{t,\varepsilon} \left[ e^{-\rho(\tau-t)} \left( H_{+}(\tau,\varepsilon_{\tau}) - \varepsilon_{\tau} - c \right) \right] ,$$

and her corresponding value function is

$$G_{+}(t,\varepsilon) = \sup_{\tau} G_{+}^{(\tau)}(t,\varepsilon).$$

The intuition here is that the agent pays  $\varepsilon + c$  for the portfolio, but receives the exit option which has value  $H_{+}(\varepsilon,\tau)$ .

Now, due to the stationary properties of the OU process, the performance criteria and, therefore, the value functions do not depend on time. In what follows we suppress the time dependence. The dynamic programming principle (DPP) implies that the value functions  $H$  and  $G$  should satisfy the coupled system of  $\text{variational inequalities (VIs)}$ 

$$\max \left\{ (\mathcal{L} - \rho) \, H_+(\varepsilon) \; ; \; (\varepsilon - c) - H_+(\varepsilon) \right\} = 0 \, ,$$
$$\max \left\{ (\mathcal{L} - \rho) \, G_+(\varepsilon) \; ; \; (H_+(\varepsilon) - \varepsilon - c) - G_+(t, \varepsilon) \right\} = 0 \, ,$$

where  $\mathcal{L}$  is the infinitesimal generator of the co-integration process, i.e.

$$\mathcal{L} = \kappa \left( \theta - \varepsilon \right) \partial_{\varepsilon} + \frac{1}{2} \, \sigma^2 \, \partial_{\varepsilon \varepsilon} \, .$$

#### 11.3.1 The Optimal Exit Problem

The VI for  $H$  is very similar to the value of a perpetual call option, and can be obtained by finding the fundamental solutions of the ODE

$$(\mathcal{L} - \rho) F(\varepsilon) = 0, \qquad (11.1)$$

which we denote  $F_{\pm}(\varepsilon)$ , and write  $H_{+}(\varepsilon) = A F_{+}(\varepsilon) + B F_{-}(\varepsilon)$  in the continuation region  $(\varepsilon < \varepsilon^*)$  and  $H_+(\varepsilon) = (\varepsilon - c)$  in the exercise region  $\varepsilon > \varepsilon^*$ . We then need to impose the value matching and smooth pasting conditions

$$H_{+}(\varepsilon^{*}) = (\varepsilon^{*} - c), \quad \text{and} \quad \partial_{\varepsilon} H_{+}(\varepsilon^{*}) = 1,$$

to solve for the optimal point  $\varepsilon^*$  where the agent closes out the position.

To this end, one can check that

$$F_{+}(\varepsilon) = \int_{0}^{\infty} u^{\frac{\rho}{\kappa} - 1} e^{-\sqrt{\frac{2\kappa}{\sigma^{2}}} \left(\theta - \varepsilon\right) u - \frac{1}{2} u^{2}} du,$$
  
$$F_{-}(\varepsilon) = \int_{0}^{\infty} u^{\frac{\rho}{\kappa} - 1} e^{+\sqrt{\frac{2\kappa}{\sigma^{2}}} \left(\theta - \varepsilon\right) u - \frac{1}{2} u^{2}} du.$$

are solutions of  $(11.1)$ .

Moreover, it is easy to see (by differentiating under the integral) that  $F'_{+}(\varepsilon) >$  $0, F''_{+}(\varepsilon) > 0, F'_{-}(\varepsilon) < 0$ , and  $F''_{-}(\varepsilon) > 0$ , so that  $F_{+}$  is strictly positive, increasing and convex, while  $F_{-}$  is strictly positive, decreasing and convex. (As a side note, these integrals can be written in terms of Whittaker or confluent hypergeometric functions.)

The value function H must vanish as  $\varepsilon \to -\infty$  (since the time to exiting the position will tend to infinity and the discount factor will render such strategies worthless), hence we must have

$$H_{+}(\varepsilon) = A F_{+}(\varepsilon) \, \mathbb{1}_{\varepsilon < \varepsilon^{*}} + (\varepsilon - c) \, \mathbb{1}_{\varepsilon > \varepsilon^{*}} \,,$$

![](_page_6_Figure_1.jpeg)

Figure 11.4 The optimal exit trigger levels (given by the black circles) and corresponding value function  $H_{+}$ .

for some constant A, i.e,  $B = 0$  otherwise  $H_{+}$  would blow up. Applying the value matching and smooth pasting conditions, we have

$$A F_{+}(\varepsilon^{*}) = (\varepsilon^{*} - c), \quad \text{and} \quad A F'_{+}(\varepsilon^{*}) = 1.$$

Taking the ratio of these equations and re-arranging, the optimal level at which to close out the position is the unique solution to the non-linear equation

$$(\varepsilon^* - c) F'_+(\varepsilon^*) = F_+(\varepsilon^*), \qquad (11.2)$$

and further we have  $A = \frac{\varepsilon^* - c}{F_+(\varepsilon^*)}$ . The value function  $H_+$  can then be written as

$$H_{+}(\varepsilon) = \frac{F_{+}(\varepsilon)}{F_{+}(\varepsilon^{*})} \left( \varepsilon^{*} - c \right) \mathbb{1}_{\varepsilon < \varepsilon^{*}} + \left( \varepsilon - c \right) \mathbb{1}_{\varepsilon \ge \varepsilon^{*}}.$$

Figure 11.4 shows the value function  $H$  in the continuation regions (the solid lines) and exercise regions (the dashed lines) as the mean-reversion rate  $\kappa$  and discount rate  $\rho$  vary. We also set  $\theta = 0$ ,  $\sigma = 0.5$  and  $c = 0.01$ . As the mean-reversion rate increases, the optimal trigger levels decrease since the co-integration factor is drawn more strongly to the mean-reversion level. Similarly, as the discount rate  $\rho$  increases, the trigger levels decrease, to draw the stopping time nearer since future gains are discounted more.

#### 11.3.2 The Optimal Entry Problem

Armed with the optimal exit strategy, we can solve for the optimal entry problem. This also amounts to solving for the price of a perpetual American-style option, albeit now with the exercise value of  $H_{+}(\varepsilon) - \varepsilon - c$  rather than a simple call payoff. Now, we anticipate that the value function  $G_{+}$  should be decreasing, rather than increasing in  $\varepsilon$ . The reason is simple: suppose that  $\varepsilon < \theta$ , i.e. the co-integration portfolio value is currently less than its long-run level; then as  $\varepsilon$ increases, if the agent enters into a long position, she will extract less value from

![](_page_7_Figure_1.jpeg)

Figure 11.5 The optimal entry trigger level (given by the black circles) and corresponding value function  $G_{+}$ .

it once she exercises at the optimal exit point  $\varepsilon^*$ . This value should reduce to zero as  $\varepsilon$  tends to infinity, hence, we can write

$$G_{+}(\varepsilon) = D F_{-}(\varepsilon) \, \mathbb{1}_{\varepsilon > \varepsilon_{*}} + (H_{+}(\varepsilon) - \varepsilon - c) \, \mathbb{1}_{\varepsilon \leq \varepsilon_{*}}$$

for some constant  $D$ . The value matching and smooth pasting conditions are now

$$D F_{-}(\varepsilon_{*}) = H_{+}(\varepsilon_{*}) - \varepsilon_{*} - c, \quad \text{and} \quad D F'_{-}(\varepsilon_{*}) = H'_{+}(\varepsilon_{*}) - 1,$$

or solving for  $C$  and re-arranging, we have

$$\left(H_{+}(\varepsilon_{*})-\varepsilon_{*}-c\right)F'_{-}(\varepsilon_{*})=\left(H'_{+}(\varepsilon_{*})-1\right)F_{-}(\varepsilon_{*}).\tag{11.3}$$

Naturally, we anticipate that  $\varepsilon_* < \varepsilon^*$ . Putting these results together, the value function  $G$  can be written as

$$G_{+}(\varepsilon) = \frac{F_{-}(\varepsilon)}{F_{-}(\varepsilon_{*})} \left( H_{+}(\varepsilon_{*}) - \varepsilon_{*} - c \right) \mathbb{1}_{\varepsilon > \varepsilon_{*}} + \left( H_{+}(\varepsilon) - \varepsilon - c \right) \mathbb{1}_{\varepsilon \leq \varepsilon_{*}}.$$

Figure 11.5 shows the value function  $G_{+}$  in the continuation regions (the solid lines) and exercise regions (the dashed lines) as the mean-reversion rate  $\kappa$  and discount rate  $\rho$  vary. We also set  $\theta = 0$ ,  $\sigma = 0.5$  and  $c = 0.01$ . As the meanreversion rate increases, the optimal trigger levels increase (and move towards the mean-reversion level) since the co-integration factor is drawn more strongly to the mean-reversion level. Similarly, as the discount rate  $\rho$  increases, the trigger levels increase, to draw the stopping time nearer since future gains are discounted more.

Comparing Figure  $11.5$  to  $11.4$ , we observe that even with the same parameters, the optimal entry and exit prices are not symmetric around the meanreversion level. This is at first a somewhat surprising result. However, since the entry and exit times are ordered, the discount factor plays a role in biasing the entry point to occur closer to the mean-reversion level, relative to the exit point. For example, with  $\kappa = 4$ , we see the entry price is about  $-0.47$ , while the exit price is about 0.51. With "' = 0.5, the asymmetry is even larger as the entry price is about -0.97 while the exit price is about 1.1.

#### 11.3.3 **Double-Sided Optimal Entry-Exit**

In the previous sections we studied how an agent would behave if she wishes to enter into and then exit from a long position in a co-integration portfolio. This ignores the possibility that the agent may instead wish to enter into a short position. Here we incorporate a double-sided strategy which considers the optimal time in which to enter either a long or short position and then optimally exit the position.

Let the performance criteria for exiting from a long or short position be given by

$$\begin{split} H_{+}^{(\tau)}(t,\varepsilon) &= \mathbb{E}_{t,\varepsilon} \left[ e^{-\rho(\tau-t)} \left( \varepsilon_{\tau} - c \right) \right] \,, \\ H_{-}^{(\tau)}(t,\varepsilon) &= \mathbb{E}_{t,\varepsilon} \left[ e^{-\rho(\tau-t)} \left( -\varepsilon_{\tau} - c \right) \right] \,, \end{split}$$

with the corresponding value functions

$$H_{+}(t,\varepsilon) = \sup_{\tau} H_{+}^{(\tau)}(t,\varepsilon) ,$$
  
$$H_{-}(t,\varepsilon) = \sup_{\tau} H_{-}^{(\tau)}(t,\varepsilon) .$$

Naturally, fl<sup>+</sup>coincides with H+ from the previous section. We therefore only need to focus on computing H \_.

As before, we see that H \_ is independent of time and should satisfy the VI

$$\max\left\{(\mathcal{L}-\rho)H_{-}(\varepsilon) \; ; \; (-\varepsilon-c)-H_{-}(\varepsilon)\right\}=0 \, .$$

Clearly, since this is the value of exiting from a short position, the agent's value function must be decreasing in c and must vanish as c ---+ oo. Hence, we must have

$$H_{-}(\varepsilon) = A F_{-}(\varepsilon) \mathbbm{1}_{\varepsilon > \varepsilon_{-}^{*}} - (\varepsilon + c) \mathbbm{1}_{\varepsilon \le \varepsilon_{-}^{*}},$$

where c".\_ is the trigger level at which the agent will close out the position. Applying the value matching and smooth pasting conditions we have

$$A F_{-}(\varepsilon_{-}^{*}) = -(\varepsilon_{-}^{*} + c), \quad \text{and} \quad A F'_{-}(\varepsilon_{-}^{*}) = -1,$$

and taking the ratio of these equations and re-arranging, the optimal level at which to close out the position is the unique solution to the non-linear equation

$$(\varepsilon_{-}^{*} + c) F_{-}^{\prime}(\varepsilon_{-}^{*}) = F_{-}(\varepsilon_{-}^{*}). \tag{11.4}$$

In all, the value functions  $H_{\pm}$  can be written as

$$H_{+}(\varepsilon) = \frac{F_{+}(\varepsilon)}{F_{+}(\varepsilon_{-}^{*})} \left(\varepsilon_{+}^{*} - c\right) \mathbb{1}_{\varepsilon < \varepsilon_{+}^{*}} + (\varepsilon - c) \mathbb{1}_{\varepsilon \ge \varepsilon_{-}^{*}},$$
  
$$H_{-}(\varepsilon) = -\frac{F_{-}(\varepsilon)}{F_{-}(\varepsilon_{-}^{*})} \left(\varepsilon_{-}^{*} + c\right) \mathbb{1}_{\varepsilon > \varepsilon_{-}^{*}} - (\varepsilon + c) \mathbb{1}_{\varepsilon \le \varepsilon_{+}^{*}}.$$

Next, the agent's performance criteria  $G^{(\tau)}(t,\varepsilon)$  for the entry problem can be written as

$$G^{(\tau)}(t,\varepsilon) = \mathbb{E}_{t,\varepsilon} \left[ e^{-\rho(\tau_{+}-t)} \left( H_{+}(\tau_{+},\varepsilon_{\tau_{+}}) - \varepsilon_{\tau_{+}} - c \right) \mathbb{1}_{\min(\tau_{+},\tau_{-})=\tau_{+}} \right. \\ \left. + \left. e^{-\rho(\tau_{-}-t)} \left( H_{-}(\tau_{-},\varepsilon_{\tau_{-}}) + \varepsilon_{\tau_{-}} - c \right) \mathbb{1}_{\min(\tau_{+},\tau_{-})=\tau_{-}} \right] \right] .$$

The corresponding VI is

$$\max \left\{ \left( \mathcal{L} - \rho \right) G(\varepsilon) \; ; \right.$$
$$\left. \left( H_{+}(\varepsilon) - \varepsilon - c \right) - G(t, \varepsilon) \; ; \; \left( H_{-}(\varepsilon) + \varepsilon - c \right) - G(t, \varepsilon) \right\} = 0 \, .$$

Now there will be two trigger points  $\varepsilon_{\pm *}$  corresponding to entering the long or short position. In this case, in the continuation region, the function  $G$  will be a linear combination of both  $F_{\pm}$ , so that

$$\begin{split} G(\varepsilon) &= \left( A \, F_+(\varepsilon) + B \, F_-(\varepsilon) \right) \mathbbm{1}_{\varepsilon \in (\varepsilon_{*+}, \varepsilon_{*-})} \\ &+ \left( H_+(\varepsilon) - \varepsilon - c \right) \, \mathbbm{1}_{\varepsilon \le \varepsilon_{*+}} + \left( H_-(\varepsilon) + \varepsilon - c \right) \, \mathbbm{1}_{\varepsilon \ge \varepsilon_{*-}} \, . \end{split}$$

The constant coefficients  $A$  and  $B$  will be determined via value matching and smooth pasting at both trigger points. As such we have,

$$\begin{split} A\,F_{+}(\varepsilon_{*+}) + B\,F_{-}(\varepsilon_{*+}) &= H_{+}(\varepsilon_{*+}) - \varepsilon_{*+} - c \,, \\ A\,F'_{+}(\varepsilon_{*+}) + B\,F'_{-}(\varepsilon_{*+}) &= H'_{+}(\varepsilon_{*+}) - 1 \,, \\ A\,F_{+}(\varepsilon_{*-}) + B\,F_{-}(\varepsilon_{*-}) &= H_{-}(\varepsilon_{*-}) + \varepsilon_{*-} - c \,, \\ A\,F'_{+}(\varepsilon_{*-}) + B\,F'_{-}(\varepsilon_{*-}) &= H'_{-}(\varepsilon_{*-}) + 1 \,. \end{split}$$

We can solve for A and B in terms of  $\varepsilon_{*\pm}$  from the value matching conditions (first and third equations):

$$A = \frac{\left(H_{+}(\varepsilon_{*+}) - \varepsilon_{*+} - c\right)F_{-}(\varepsilon_{*-}) - \left(H_{-}(\varepsilon_{*-}) + \varepsilon_{*-} - c\right)F_{-}(\varepsilon_{*+})}{F_{+}(\varepsilon_{*+})\,F_{-}(\varepsilon_{*-}) - F_{+}(\varepsilon_{*-})\,F_{-}(\varepsilon_{*+})}\,,$$
$$B = \frac{\left(H_{+}(\varepsilon_{*+}) - \varepsilon_{*+} - c\right)F_{+}(\varepsilon_{*-}) - \left(H_{-}(\varepsilon_{*-}) + \varepsilon_{*-} - c\right)F_{+}(\varepsilon_{*+})}{F_{-}(\varepsilon_{*+})\,F_{+}(\varepsilon_{*-}) - F_{-}(\varepsilon_{*-})\,F_{+}(\varepsilon_{*+})}\,,$$

and substitute these expressions back in to determine  $\varepsilon_{*\pm}$  as roots of the smooth pasting conditions (second and fourth equations). To solve for the trigger points, it is reasonable to use initial starting points  $\varepsilon_{*+}^0$  for  $\varepsilon_{*\pm}$  implied from the onesided trade results of the last section, i.e  $\varepsilon_{*+}^0 \sim \varepsilon_*$  and  $\varepsilon_{*-}^0 \sim -\varepsilon_*$ .

In Figure 11.6 we show the resulting value functions for the case when

$$\rho = 0.01$$
,  $\sigma = 0.5$ ,  $\theta = 1$ , and  $c = 0.01$ ,

![](_page_10_Figure_1.jpeg)

and we allow the mean-reversion rate  $\kappa$  to vary. There are a few interesting points to notice. First,  $H_{+}$  and  $H_{-}$  behave quite differently. Second, the optimal exit points are not symmetric around  $\theta$ . Third, the optimal entry points are in fact equal to the corresponding optimal exit point from the opposite portfolio: e.g., the optimal entry point for the long portfolio equals the optimal exit point from the short position. The table below illustrates this point more clearly.

|          | $\text{exit triggers}$     |                               | $entry$ triggers          |                            |
|----------|----------------------------|-------------------------------|---------------------------|----------------------------|
| $\kappa$ | $\varepsilon^*_{+}$ (long) | $\varepsilon_{-}^{*}$ (short) | $\varepsilon_{*+}$ (long) | $\varepsilon_{*-}$ (short) |
| 0.5      | 1.9537                     | $-0.4060$                     | $-0.4060$                 | 1.9537                     |
| 1.0      | 1.7460                     | $-0.1815$                     | $-0.1815$                 | 1.7460                     |
| 2.0      | 1.5744                     | $-0.0740$                     | $-0.0740$                 | 1.5744                     |
| 4.0      | 1.4367                     | $-0.0410$                     | $-0.0410$                 | 1.4367                     |

#### $11.4$ Co-integrated Log Prices with Short-Term-Alpha

Another approach to devise trading algorithms that take advantage of structural dependencies between assets, is one where the drifts of a collection of assets are co-integrated, rather than the prices themselves.

#### 11.4.1 Model Setup

Suppose that we have a collection of risky assets whose vector of prices  $Y =$  $(Y_t^1, \ldots, Y_t^n)_{0 \le t \le T}$  satisfy the coupled system of SDEs

$$\frac{dY_t^k}{Y_t^k} = \delta_k \,\alpha_t \,dt + \sum_{i=1}^n \sigma_{ki} \,dW_t^i\,,\tag{11.5}$$

where

$$\alpha_t = a_0 + \sum_{i=1}^n a_i \log Y_t^i,$$

and  $W = (W_t^1, \ldots, W_t^n)_{0 \le t \le T}$  is a vector of independent Brownian motions. Focusing on the diffusion term above, it is not difficult to see that the instantaneous covariance, loosely interpreted as  $\mathbb{C}\left[\frac{dY_t^i}{Y_t^i}, \frac{dY_t^j}{Y_t^j}\Big|\mathcal{F}_t\right]$ , between assets *i* and  $j$  is given by

$$\Omega_{ij} = \sum_{k=1}^{n} \sigma_{ik} \sigma_{kj} \ .$$

Thus, the matrix  $\boldsymbol{\sigma}$  whose elements are  $\sigma_{ij}$  is the Cholesky decomposition of the instantaneous variance-covariance matrix  $\Omega$  so that in matrix notation  $\Omega = \sigma \sigma'$ . We assume that there are no redundant degrees of freedom here, so that  $\sigma$  is invertible. Furthermore, we show below that  $\alpha_t$  acts as a co-integration factor. First, note that when  $\alpha_t = 0$  all assets are simply correlated geometric Brownian motions with zero drift, and are hence martingales. In general, however,  $\alpha_t$  will be non-zero representing short-term deviations from martingale behaviour, and may also be considered as a 'short-term-alpha' component – see subsection  $10.4.2$ .

We justify calling  $\alpha_t$  a co-integration factor by demonstrating that it is indeed a mean-reverting process. First, note that the log-prices satisfy the SDEs

$$d\log Y_t^k = \left(\delta_k \,\alpha_t - \frac{1}{2}\Omega_{kk}\right) \, dt + \sum_{i=1}^n \sigma_{ki} \, dW_t^i \, .$$

Next we compute the differential of  $\alpha_t$  as follows:

$$d\alpha_t = d\left(a_0 + \sum_{k=1}^n a_k \log Y_t^k\right)$$
  
= 
$$\sum_{k=1}^n a_k \left(\delta_k \alpha_t - \frac{1}{2}\Omega_{kk}\right) dt + \sum_{k=1}^n a_k \sum_{i=1}^n \sigma_{ki} dW_t^i,$$

and therefore,

$$d\alpha_t = \kappa \left( \theta - \alpha_t \right) \, dt + \boldsymbol{a'} \boldsymbol{\sigma} \, d\boldsymbol{W}_t \,. \tag{11.6}$$

Here,  $a'$  represents the transpose of the column vector  $a$  where

$$\begin{aligned} a &= (a_1, \dots, a_n)', \\ \kappa &= -\sum_{k=1}^n a_k \,\delta_k = -\boldsymbol{\delta}' \, \boldsymbol{a} \,, \\ \theta &= \frac{\sum_{k=1}^n a_k \Omega_{kk}}{2\sum_{k=1}^n a_k \,\delta_k} = \frac{1}{2} \frac{\text{Tr}(\boldsymbol{A}\boldsymbol{\Omega})}{\boldsymbol{\delta}' \, \boldsymbol{a}} \end{aligned}$$

Here,  $\text{Tr}(\cdot)$  denotes the trace of the matrix in braces (i.e. the sum of its diagonal elements) and  $A = \text{diag}(a)$  is a diagonal matrix whose diagonal entries are a. To ensure that the model does indeed describe a mean-reverting process, as opposed to a mean-repelling one, we assume that  $\delta' a < 0$ .

From the SDE above, we can see that  $\alpha$  mean-reverts at a rate which depends on the various strengths of the impact that  $\alpha$  has on each asset (through  $\delta$ ) as well as the strength of the log-asset price's contribution to  $\alpha$  itself (through a). The mean-reversion level  $\theta$  depends on the ratio of the volatility relative to the impact each component has on the drift of the assets.

Another alternative representation of the model stems from inserting the expression for  $\alpha_t$  directly into the SDE for  $\log Y_t$ . In this case, we have

$$d\log Y_t^k = \delta_k \left( a_0 - \frac{1}{2}\Omega_{kk} + \sum_{i=1}^n a_i \log Y_t^i \right) dt + \sum_{i=1}^n \sigma_{ki} dW_t^i,$$

so that if we let  $Z_t = \log Y_k$ , where the log is interpreted componentwise, then

$$d\boldsymbol{Z}_t = (\boldsymbol{c} - \boldsymbol{B}\,\boldsymbol{Z}_t) \, dt + \boldsymbol{\sigma} \, d\boldsymbol{W}_t.$$

with

$$B = -\begin{pmatrix} \delta_1 a_1 & \delta_1 a_2 & \dots & \delta_1 a_n \\ \vdots & \vdots & & \vdots \\ \delta_n a_1 & \delta_n a_2 & \dots & \delta_n a_n \end{pmatrix}, \quad c = \begin{pmatrix} a_0 - \Omega_{11} \\ \vdots \\ a_0 - \Omega_{nn} \end{pmatrix}$$

In this representation, we directly see that the log-prices are a vector-autoregressive model (VAR). Although this representation is in some sense more compact, we will find in the next section that the short-term-alpha version of the model is a preferable representation for solving the agent's control problem. Note that here,  $B$  is singular and contains exactly one positive eigenvalue due to the singular co-integration factor that we incorporate into the model. If we have  $m \leq n$ co-integration factors then there will be in general  $m$  positive eigenvalues.

In contrast to our earlier work on price impact models of trading (see Chapters  $6$  and  $7$ ), here we assume there is no impact from trading, and instead optimise the agent's utility of expected wealth. Thus, let  $\pi = (\pi^0_t, \pi^1_t, \ldots, \pi^n_t)_{0 \le t \le T}$  denote the **dollar value invested** in the riskless  $(\pi_t^0)$  and risky assets  $(\pi_t^1, \ldots, \pi_t^n)$ , and let  $X^{\boldsymbol{\pi}} = (X^{\boldsymbol{\pi}}_t)_{0 \le t \le T}$  denote the agent's (controlled) wealth process. With this convention, the number of units  $m_t^k$  the agent holds in asset k is  $m_t^k = \pi_t^k / Y_t^k$ . Hence, the wealth process can be written as

$$X_t^{\pi} = \sum_{k=0}^n \pi_t^k = \sum_{k=0}^n m_t^k Y_t^k,$$

so that

$$dX_t^{\pi} = \sum_{k=0}^n d(m_t^k Y_t^k) = \sum_{k=0}^n m_t^k dY_t^k = \sum_{k=1}^n \pi_t^k \frac{dY_t^k}{Y_t^k}$$
  
=  $\sum_{k=1}^n \pi_t^k \left\{ \delta_k \, \alpha_t \, dt + \sum_{i=1}^n \sigma_{ki} \, dW_t^i \right\} = (\pi_t' \delta) \, \alpha_t \, dt + \pi_t' \sigma dW_t \, ,$ 

where the second equality follows from the usual self-financing constraint – which can be interpreted as the change in the wealth process due to the change in each asset's value, assuming the positions are held fixed over a small interval of time. The third equality is obtained by assuming that the time horizon is short enough that interest rates are zero (so that  $dY_t^0 = 0$ ), but long enough that the geometric model we employ is required. (It is not too difficult to include a deterministic discount factor and the interested reader is urged to try this out.) The last equality is a rewrite of the equations using vector/matrix notation.

To set up the dynamic programming equations below we require the quadratic variation and cross-variations of the processes X and  $y$ . First, it is easy to see that

$$d[Y^{i}, Y^{j}]_{t} = \sum_{k,l=1}^{n} Y_{t}^{i} Y_{t}^{j} \sigma_{ki} \sigma_{lj} d[W^{i}, W^{j}]_{t} = \sum_{k=1}^{n} Y_{t}^{i} Y_{t}^{j} \sigma_{ki} \sigma_{lk} dt = (\boldsymbol{y}_{t}^{\prime} \boldsymbol{\Omega} \boldsymbol{y}_{t})_{ij} dt,$$

where  $(y_t' \Omega y_t)_{ij}$  represents the *ij*th element of the matrix in the braces. Next,

$$d[X^{\pi}, X^{\pi}]_{t} = \sum_{i,j,k,l=1}^{n} \pi_{t}^{k} \pi_{t}^{l} \sigma_{ki} \sigma_{lj} d[W^{i}, W^{j}]_{t} = \sum_{i,k,l=1}^{n} \pi_{t}^{k} \pi_{t}^{l} \sigma_{ki} \sigma_{li} dt = \pi_{t}^{\prime} \Omega \pi_{t} dt.$$

Finally,

$$d[X^{\pi}, Y^{k}]_{t} = \sum_{i,j,l=1}^{n} \pi_{t}^{l} \sigma_{li} \, \sigma_{kj} \, Y_{t}^{k} \, d[W^{i}, W^{j}]_{t} = \sum_{j,l=1}^{n} \pi_{t}^{l} \sigma_{lj} \, \sigma_{kj} \, Y_{t}^{k} \, dt = (\pi_{t}^{\prime} \mathbf{\Omega} \, \boldsymbol{y}_{t})_{k} \;,$$

where  $(\boldsymbol{\pi}'_t \boldsymbol{\Omega} \boldsymbol{y}_t)_k$  represents the *k*th element of the vector in the braces.

#### 11.4.2 The Agent's Optimisation Problem

Next, the agent will optimise her dollar value in assets directly, rather than the rate of trading, and has exponential utility  $u(x) = -e^{-\gamma x}$ . Her performance criteria is given by

$$H^{\boldsymbol{\pi}}(t, x, \boldsymbol{y}) = \mathbb{E}_{t, x, \boldsymbol{y}} \left[ -\exp\left(-\gamma X_T^{\boldsymbol{\pi}}\right) \right] \,,$$

where  $\mathbb{E}_{t,x,y}[\cdot]$  represents expectation conditional on  $X_t^{\pi} = x$  and  $y_t = y$ . The agent's value function is as usual

$$H(t, x, \boldsymbol{y}) = \sup_{\boldsymbol{\pi} \in \mathcal{A}} H^{\boldsymbol{\pi}}(t, x, \boldsymbol{y}),$$

where the set of admissible strategies  $\mathcal{A}$  are those for which

$$\mathbb{E}\left[\sum_{k=0}^n \int_0^T (\pi_u^k)^2 \, du\right] < \infty \, .$$

Alternatively, we can enforce the condition that each component of  $\pi$  is bounded.

Applying the dynamic programming principle leads to the DPE which the value function should satisfy:

$$\begin{split} \partial_t H + \alpha \, \boldsymbol{\delta}' \mathcal{D}_y H + \tfrac{1}{2} \mathcal{D}^{\boldsymbol{\Omega}}_{yy} H \\ + \sup_{\boldsymbol{\pi}} \left\{ (\boldsymbol{\pi}' \boldsymbol{\delta}) \, \alpha \, \partial_x H + \tfrac{1}{2} (\boldsymbol{\pi}'_t \boldsymbol{\Omega} \boldsymbol{\pi}) \, \partial_{xx} H + \boldsymbol{\pi}' \boldsymbol{\Omega} \, \mathcal{D}_{xy} H \right\} &= 0 \,, \end{split}$$

subject to  $H(T, x, y) = -e^{-\gamma x}$ , and where  $\alpha = a_0 + a' \log y$  (the log being interpreted componentwise) represents the state of the co-integration process, and the following linear differential operators were introduced to reduce clutter:

$$\begin{aligned} \mathcal{D}_{y}H &= \left(y^{1}\partial_{y^{1}}H,\ldots,y^{n}\partial_{y^{n}}H\right)',\\ \mathcal{D}^{\Omega}_{yy} &= \sum_{i,j=1}^{n} y^{i}\Omega_{ij}y^{j}\partial_{y^{i}y^{j}}H,\\ \mathcal{D}_{xy} &= \left(y^{1}\partial_{xy^{1}}H,\ldots,y^{n}\partial_{xy^{n}}H\right)'. \end{aligned}$$

Next, let us obtain the optimal investment in feedback form. For this we focus on the supremum term and perform a matrix completion of the square. Specifically, assuming that  $\partial_{xx}H \neq 0$ , we write

$$\begin{split} \mathcal{M} &= \left. (\boldsymbol{\pi}'\boldsymbol{\delta}) \, \alpha \, \partial_x H + (\boldsymbol{\pi}'_t \boldsymbol{\Omega} \boldsymbol{\pi}) \, \partial_{xx} H + \boldsymbol{\pi}' \boldsymbol{\Omega} \, \mathcal{D}_{xy} H \\ &= \, \frac{1}{2} \partial_{xx} H \left\{ (\boldsymbol{\pi}'_t \boldsymbol{\Omega} \boldsymbol{\pi}) + 2 \, \boldsymbol{\pi}' \frac{(\boldsymbol{\delta} \, \alpha \, \partial_x H + \boldsymbol{\Omega} \, \mathcal{D}_{xy} H)}{\partial_{xx} H} \right\} \\ &= \, \frac{1}{2} \partial_{xx} H \left\{ (\boldsymbol{\pi}_t + \boldsymbol{\Omega}^{-1} \, \mathcal{L} H)' \, \boldsymbol{\Omega} \left( \boldsymbol{\pi}_t + \boldsymbol{\Omega}^{-1} \, \mathcal{L} H \right) - \frac{\mathcal{L}' H \, \boldsymbol{\Omega}^{-1} \mathcal{L} H}{(\partial_{xx} H)^2} \right\} \, , \end{split}$$

where the vector-valued linear operator  $\mathcal{L}$  acts on H as follows:

$$\mathcal{L}H = \boldsymbol{\delta}\,\alpha\,\partial_x H + \boldsymbol{\Omega}\,\mathcal{D}_{xy}H\,,$$

and we have used the fact that  $\Omega$  is symmetric (since it is a variance-covariance matrix) so that  $(\Omega^{-1})' = (\Omega')^{-1} = \Omega^{-1}$ . From the above expression we can immediately identify the optimal investment in feedback control form as

$$\boldsymbol{\pi}^* = -\frac{\boldsymbol{\Omega}^{-1} \boldsymbol{\delta} \,\alpha \,\partial_x H + \boldsymbol{\mathcal{D}}_{xy} H}{\partial_{xx} H} \,. \tag{11.7}$$

From the above matrix completion of the square, we also have the maximum

term

$$\mathcal{M} = -\frac{1}{2}\,\frac{\mathcal{L}'H\,\mathbf{\Omega}^{-1}\mathcal{L}H}{\partial_{xx}H}\,,$$

so that upon reinsertion into the DPE, we obtain the following non-linear PDE for the value function:

$$\partial_t H + \alpha \, \boldsymbol{\delta}' \mathcal{D}_y H + \tfrac{1}{2} \mathcal{D}^{\Omega}_{yy} H - \frac{\mathcal{L}' H \, \Omega^{-1} \mathcal{L} H}{2 \, \partial_{xx} H} = 0 \,. \tag{11.8}$$

#### 11.4.3 Solving the DPE

In the classical Merton problem, where the asset prices are geometric Brownian motions, the value function for exponential utility has the form  $-e^{-\gamma(x+h(t))}$ , where  $h$  is a deterministic function of time. Here, due to the presence of the co-integration factor we expect instead that the value function depends also on a combination of the price state variables which equals the co-integration factor. That is we expect to be to able to write

$$H(t, x, y) = -\exp\left\{-\gamma \left(x + h(t, a_0) + \sum_{i=1}^n a_i \log y^i\right)\right\}$$

for some function  $h(t,\alpha)$ , with  $\alpha = a_0 + \sum_{i=1}^n a_i \log y^i$ , and subject to the terminal condition  $h(T,\alpha) = 0$ . Note that differentiation with respect to  $y^k$  acts simply on  $h$ , specifically

$$\partial_{y^k} h(t,\alpha) = \frac{a_k}{y^k} \,\partial_\alpha h(t,\alpha) \,,$$

so that

$$\begin{split} \partial_{y^k} e^{-\gamma \, h(t,\alpha)} &= -\gamma \, \frac{a_k}{y^k} \, \partial_\alpha h(t,\alpha) \, e^{-\gamma \, h(t,\alpha)} \,, \\ \partial_{y^j y^k} h(t,\alpha) &= -\gamma \, \partial_{y^j} \left( \frac{a_k}{y^k} \, \partial_\alpha h(t,\alpha) \, e^{-\gamma \, h(t,\alpha)} \right) \,. \end{split}$$

Hence, for  $j \neq k$ ,

$$\begin{split} \partial_{y^j y^k} e^{-\gamma \, h(t,\alpha)} &= -\gamma \, \frac{a_k \, a_j}{y^k \, y^j} \, \partial_\alpha \left( \, \partial_\alpha h(t,\alpha) \, e^{-\gamma \, h(t,\alpha)} \right) \\ &= -\gamma \, \frac{a_k \, a_j}{y^k \, y^j} \, \left( \partial_{\alpha\alpha} h(t,\alpha) - \gamma \, (\partial_\alpha h(t,\alpha))^2 \right) \, e^{-\gamma \, h(t,\alpha)} \, . \end{split}$$

while for  $j = k$ ,

$$\begin{split} \partial_{y^j y^j} e^{-\gamma \, h(t,\alpha)} \\ &= -\gamma \, \left( -\frac{a_k}{(y^k)^2} \, \partial_\alpha h(t,\alpha) \, e^{-\gamma \, h(t,\alpha)} + \frac{a_k^2}{(y^k)^2} \partial_\alpha \left( \, \partial_\alpha h(t,\alpha) \, e^{-\gamma \, h(t,\alpha)} \right) \right) \\ &= -\gamma \, \frac{a_k}{(y^k)^2} \left( -\partial_\alpha h(t,\alpha) + a_k \left( \partial_{\alpha\alpha} h(t,\alpha) - \gamma \left( \partial_\alpha h(t,\alpha) \right)^2 \right) \right) \, e^{-\gamma \, h(t,\alpha)} \, . \end{split}$$

Putting these two results together we can write

$$\partial_{y^{j}y^{k}}e^{-\gamma h(t,\alpha)} = -\gamma \frac{a_{k} a_{j}}{y^{k} y^{j}} \left(\partial_{\alpha\alpha} h(t,\alpha) - \gamma \left(\partial_{\alpha} h(t,\alpha)\right)^{2}\right) e^{-\gamma h(t,\alpha)} + \delta_{jk} \gamma \frac{a_{k}}{(y^{k})^{2}} \partial_{\alpha} h(t,\alpha) e^{-\gamma h(t,\alpha)},$$

where  $\delta_{jk}$  is the Kronecker delta which equals 1 if  $j = k$  and 0 otherwise.

Armed with these results, the various linear differential operators that appear in the non-linear PDE  $(11.8)$  can be written as follows:

$$\begin{split} \mathcal{D}_{y}H &= \left(-\gamma\,H\right)\boldsymbol{a}\,\partial_{\alpha}h\,,\\ \mathcal{D}^{\Omega}_{yy} &= \left(-\gamma\,H\right)\,\sum_{i,j=1}^{n}\Omega_{ij}\,a_{i}\,a_{j}\,\left(\partial_{\alpha\alpha}h - \gamma(\partial_{\alpha}h)^{2}\right) + \left(\gamma\,H\right)\,\sum_{j=1}^{n}a_{j}\,\Omega_{jj}\,\partial_{\alpha}h\\ &= -\left(\gamma\,H\right)\left(\boldsymbol{a}'\boldsymbol{\Omega}\boldsymbol{a}\right)\,\left(\partial_{\alpha\alpha}h - \gamma(\partial_{\alpha}h)^{2}\right) + \left(\gamma\,H\right)\,\text{Tr}(\boldsymbol{A}\,\boldsymbol{\Omega})\,\partial_{\alpha}h\,, \end{split}$$

and recall that  $Tr(\cdot)$  denotes the trace of the matrix (i.e. the sum along its diagonal elements), and  $A = \text{diag}(a)$  is a diagonal matrix with the elements of the vector  $\boldsymbol{a}$  along the diagonal. Furthermore,

$$\begin{split} \mathcal{D}_{xy}H &= (\gamma^2 H) \, \boldsymbol{a} \, \partial_{\alpha} h \,, \\ \mathcal{L}H &= (-\gamma H) \, \boldsymbol{\delta} \, \alpha + (\gamma^2 H) \, \boldsymbol{\Omega} \boldsymbol{a} \, \partial_{\alpha} h \,. \end{split}$$

Inserting these expression into the PDE  $(11.8)$ , allows us to write

$$\begin{split} 0 &= \left(-\gamma H\right) \partial_{t} h + \left(-\gamma H\right) \left(\boldsymbol{\delta}' \boldsymbol{a}\right) \alpha \,\partial_{\alpha} h \\ &+ \frac{1}{2} \left(\left(-\gamma H\right) \left(\boldsymbol{a}' \boldsymbol{\Omega} \boldsymbol{a}\right) \left(\partial_{\alpha \alpha} h - \gamma (\partial_{\alpha} h)^{2}\right) + \left(\gamma H\right) \operatorname{Tr}(\boldsymbol{A} \,\boldsymbol{\Omega}) \,\partial_{\alpha} h\right) \\ &- \frac{1}{2} \frac{\left(\left(-\gamma H\right) \boldsymbol{\delta} \alpha + \left(\gamma^{2} H\right) \boldsymbol{\Omega} \boldsymbol{a} \,\partial_{\alpha} h\right)' \boldsymbol{\Omega}^{-1} \left(\left(-\gamma H\right) \boldsymbol{\delta} \alpha + \left(\gamma^{2} H\right) \boldsymbol{\Omega} \boldsymbol{a} \,\partial_{\alpha} h\right)}{\gamma^{2} H} . \end{split}$$

At this point, there are three important simplifications. First, cancelling  $-\gamma H$ in all terms, we find that

$$0 = \partial_t h + (\boldsymbol{\delta}' \boldsymbol{a}) \alpha \partial_{\alpha} h$$
  
+  $\frac{1}{2} \left( (\boldsymbol{a}' \boldsymbol{\Omega} \boldsymbol{a}) \left( \partial_{\alpha \alpha} h - \gamma (\partial_{\alpha} h)^2 \right) - \text{Tr}(\boldsymbol{A} \boldsymbol{\Omega}) \partial_{\alpha} h \right)$   
+  $\frac{1}{2\gamma} \left( \boldsymbol{\delta} \alpha - \gamma \boldsymbol{\Omega} \boldsymbol{a} \partial_{\alpha} h \right)' \boldsymbol{\Omega}^{-1} \left( \boldsymbol{\delta} \alpha - \gamma \boldsymbol{\Omega} \boldsymbol{a} \partial_{\alpha} h \right) .$  (11.9)

Next, expanding the third line, we have

$$\begin{split} \left(\boldsymbol{\delta}\alpha - \gamma\,\boldsymbol{\Omega}\boldsymbol{a}\,\partial_{\alpha}h\right)'\boldsymbol{\Omega}^{-1}\left(\boldsymbol{\delta}\alpha - \gamma\,\boldsymbol{\Omega}\,\boldsymbol{a}\,\partial_{\alpha}h\right) \\ = \boldsymbol{\delta}'\,\boldsymbol{\Omega}^{-1}\,\boldsymbol{\delta}\,\alpha^2 - 2\gamma\,\boldsymbol{\delta}'\,\boldsymbol{a}\,\alpha\,\partial_{\alpha}h + \gamma^2\,\boldsymbol{a}'\,\boldsymbol{\Omega}\boldsymbol{a}\,(\partial_{\alpha}h)^2 \, . \end{split}$$

so that upon substituting into the previous expression there are two important  $\text{cancellations:}$ 

- (i) the non-linear terms containing  $(\partial_{\alpha}h)^2$  from the expansion above and the second line in  $(11.9)$  cancel one another;
- (ii) the terms  $\delta' a \alpha \partial_{\alpha} h$  from the first line in (11.9) and the above expansion also  $\text{cancel.}$

Putting these observations together we then find that  $h$  satisfies a very simple  $\text{linear PDE:}$ 

$$\partial_t h - \frac{1}{2} \operatorname{Tr}(\boldsymbol{A} \,\boldsymbol{\Omega}) \,\partial_\alpha h + \frac{1}{2} (\boldsymbol{a}' \boldsymbol{\Omega} \boldsymbol{a}) \,\partial_{\alpha\alpha} h + \frac{\boldsymbol{\delta}' \boldsymbol{\Omega} \boldsymbol{\delta}}{2\gamma} \,\alpha^2 = 0\,,\tag{11.10}$$

subject to  $h(T,\alpha)=0.$ 

Returning to the optimal investment  $(11.7)$  in the assets, the ansatz for the value function  $H = -\exp\{-\gamma(x + h(t, \alpha))\}$  allows us to write

$$\begin{split} \boldsymbol{\pi}^* &= \ -\, \frac{-\gamma \, H \, (\boldsymbol{\Omega}^{-1} \boldsymbol{\delta}) \, \alpha + (\gamma^2 \, H) \, \boldsymbol{a} \, \partial_{\alpha} h}{\gamma^2 \, H} \\ &= \ -\, \frac{-(\boldsymbol{\Omega}^{-1} \boldsymbol{\delta}) \, \alpha + \gamma \, \boldsymbol{a} \, \partial_{\alpha} h}{\gamma} \\ &= \frac{1}{\gamma} \, (\boldsymbol{\Omega}^{-1} \boldsymbol{\delta}) \, \alpha - \boldsymbol{a} \, \partial_{\alpha} h \,. \end{split} \tag{11.11}$$

Let us recall that the optimal investment in the classical Merton problem is  $\frac{1}{\kappa}\Omega^{-1}(\nu-r)$  where r is the risk-free rate and  $\nu$  is (in the classical Merton problem) the drift of the GBMs that drives the asset prices. The first term of the above expression is quite similar, since here  $r = 0$ , and the drift of the assets are  $\delta \alpha_t$  - here, however, the drift is stochastic and hence the Merton solution cannot be applied directly. The optimal investment scales with the co-integration factor. Moreover, the optimal investment is perturbed from the Merton solution by the second term. In the coming sections we will see precisely what this contribution is to the investment policy.

First, from (11.10), we can see that the solution to h must be quadratic in  $\alpha$ . Indeed in the next section we construct an explicit probabilistic representation for  $h(t,\alpha)$  and also characterise the value function in terms of a risk-neutral probability measure which makes the quadratic dependence explicit. Given that h is quadratic in  $\alpha$ , we also see that the optimal dollar invested in each asset  $\pi^*$ will be linear in  $\alpha$ . Thus, the agent reacts to the co-integration factor in at most a linear fashion, but the size of the investment will vary with time.

# A Probabilistic Interpretation

This surprisingly simple PDE  $(11.10)$  has an interesting probabilistic interpretation. First, consider the probability measure change induced by a vector of market price of risk  $\lambda_t$ , which induces a new measure  $\mathbb{P}^*$  through the Radon-Nikodym derivative

$$\frac{d\mathbb{P}^*}{d\mathbb{P}} = \exp\left\{-\frac{1}{2}\int_0^T ||\boldsymbol{\lambda}_s||^2 ds - \int_0^T \boldsymbol{\lambda}_s' d\boldsymbol{W}_s\right\} \, .$$

Girsanov's Theorem implies that the stochastic processes

$$\boldsymbol{W}_{t}^{*} = -\int_{0}^{t} \boldsymbol{\lambda}_{s} \, ds + \boldsymbol{W}_{t}$$

are independent  $\mathbb{P}^*$ -Brownian motions. Let us choose  $\lambda_t$  such that the drift of the traded assets  $Y_t$  are martingales, i.e. let us find the measure transformation which produces the risk-neutral measure. To this end, rewrite the SDE as

$$\begin{split} dY_t^k &= \delta_k \, Y_t^k \, \alpha_t \, dt + \sum_{i=1}^n \sigma_{ki} \, Y_t^k \, dW_t^i \\ &= \left( \delta_k \, \alpha_t + \sum_{i=1}^n \sigma_{ki} \lambda_t^i \right) \, Y_t^k \, dt + \sum_{i=1}^n \sigma_{ki} \, Y_t^k \, dW_t^{*i} \, . \end{split}$$

The martingale condition requires that

$$\sum_{i=1}^{n} \sigma_{ki} \lambda_t^i = -\delta_k \alpha_t, \quad k = 1, \dots, n, \quad \Longleftrightarrow \quad \boldsymbol{\sigma} \boldsymbol{\lambda}_t = -\boldsymbol{\delta} \alpha_t.$$

Therefore, since  $\sigma$  is invertible by assumption, we have

$$\lambda_t = -\sigma^{-1} \, \delta \, \alpha_t \,. \tag{11.12}$$

At this point, we have found the probability measure  $\mathbb{P}^*$  which renders the traded assets martingales. That is, we have found the risk-neutral measure. Next, we can ask what the dynamics of the co-integration factor are in terms of the risk-neutral Brownian motions. Hence, from  $(11.6)$  we have

$$\begin{split} d\alpha_t &= \left(-\tfrac{1}{2}\operatorname{Tr}(A\,\Omega) + (a'\,\delta)\alpha_t\right)\,dt + a'\sigma dW_t \\ &= \left(-\tfrac{1}{2}\operatorname{Tr}(A\,\Omega) + (a'\,\delta)\alpha_t\right)\,dt + a'\sigma\left(\lambda_t\,dt + dW_t^*\right) \\ &= \left(-\tfrac{1}{2}\operatorname{Tr}(A\,\Omega) + (a'\,\delta)\alpha_t + a'\,\sigma\,\lambda_t\right)\,dt + a'\sigma\,dW_t^*\,, \end{split}$$

so that

$$d\alpha_t = -\frac{1}{2} \operatorname{Tr}(\boldsymbol{A} \,\boldsymbol{\Omega}) \, dt + \boldsymbol{a}' \boldsymbol{\sigma} \, d\boldsymbol{W}_t^* \,.$$
 (11.13)

The last equality follows from (11.12). Surprisingly, although  $\alpha_t$  is mean-reverting in the real-world  $\mathbb{P}$ -measure, it is a Brownian motion under the risk-neutral  $\mathbb{P}^*$ measure.

Let us now return to the PDE  $(11.10)$ . It can be re-written in the form

$$(\partial_t + \mathcal{L}^{*,\alpha}) h + \frac{\delta' \Omega \delta}{2\gamma} \alpha^2 = 0,$$

subject to  $h(T,\alpha) = 0$ , where  $\mathcal{L}^{*,\alpha}$  is the  $\mathbb{P}^*$ -infinitesimal generator of  $\alpha_t$  and therefore, applying a Feynman-Kac formula we see that  $h(t, \alpha)$  can be expressed as the following expectation:

$$h(t,\alpha) = \mathbb{E}_{t,\alpha}^* \left[ \frac{\delta' \Omega \delta}{2\gamma} \int_t^T \alpha_s^2 ds \right], \qquad (11.14)$$

where  $\mathbb{E}_{t,\alpha}^*$  denotes  $\mathbb{P}^*$ -expectation given that  $\alpha_t = \alpha$ . Putting this expression for  $h$  back into the value function we then have the following relationship:

$$\begin{array}{l} \sup_{\boldsymbol{\pi}\in\mathcal{A}}\mathbb{E}_{t,x,\boldsymbol{y}}\left[-\exp\left(-\gamma\,X_{T}^{\boldsymbol{\pi}}\right)\right] \\ \qquad = -\exp\left(-\gamma\,x-\frac{1}{2}\,\boldsymbol{\delta}'\,\boldsymbol{\Omega}\,\boldsymbol{\delta}\,\mathbb{E}_{t,x,\boldsymbol{y}}^{*}\left[\int_{t}^{T}\alpha_{s}^{2}\,ds\right]\right) \,. \end{array} \tag{11.15}$$

The future expectation of integrated  $\alpha_t^2$  determines the incremental value of trading on this co-integrated collection of assets. The strength of the contribution

increases with volatility (through 0) as well as through the strength that o: has on each asset (through t:5).

# Explicit Construction of the Optimal Investment Strategy

Based on the representation from the previous section, we can construct an explicit formula for *h(t,* o:). In particular, we have that

$$\begin{split} h(t,\alpha) &= \mathbb{E}_{t,\alpha}^* \left[ \frac{\delta' \Omega \delta}{2\gamma} \int_t^T \alpha_s^2 \, ds \right] \\ &= \frac{\delta' \Omega \delta}{2\gamma} \, \mathbb{E}^* \left[ \int_t^T \left( \alpha - \frac{1}{2} \operatorname{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega})(s-t) + \sqrt{\boldsymbol{a}' \boldsymbol{\Omega} \boldsymbol{a}} \left( B_s^* - B_t^* \right) \right)^2 \, ds \right] \,, \end{split}$$

where we have introduced the process *B;* = v �..-.. *a' a Wt* which is a standard *aua*  IP'\* -Brownian motion. Hence,

$$h(t,\alpha) = \frac{\delta' \mathbf{\Omega} \delta}{2\gamma} \mathbb{E}^* \left[ \int_t^T \left\{ \left( \alpha - \frac{1}{2} \operatorname{Tr}(\mathbf{A}\,\mathbf{\Omega})(s-t) \right)^2 \right. \\ \left. + 2 \left( \alpha - \frac{1}{2} \operatorname{Tr}(\mathbf{A}\,\mathbf{\Omega})(s-t) \right) \sqrt{\mathbf{a}'\mathbf{\Omega}\mathbf{a}} \left( B_s^* - B_t^* \right) \right. \\ \left. + \left( \mathbf{a}'\mathbf{\Omega}\mathbf{a} \right) \left( B_s^* - B_t^* \right)^2 \right\} ds \right] \\ = \frac{\delta' \mathbf{\Omega} \delta}{2\gamma} \left\{ -\frac{2}{3 \operatorname{Tr}(\mathbf{A}\,\mathbf{\Omega})} \left[ \left( \alpha - \frac{1}{2} \operatorname{Tr}(\mathbf{A}\,\mathbf{\Omega}) \tau \right)^3 - \alpha^3 \right] + \frac{1}{2} \left( \mathbf{a}'\mathbf{\Omega}\mathbf{a} \right) \tau^2 \right\} \,,$$

where *T* = T -*t.* The fourth equality follows by using Fubini to interchange the integral and expectation, in which case the second term in the third equation vanishes identically, and in the third term of the third equation we use JE\* ( [ B; - B;) <sup>2</sup> ] = (s -t).

In all, we see that *h(t,* o:) is quadratic in o:. Consequently, the optimal investment from (11.11) takes on the explicit form

$$\begin{split} \pi^* &= \tfrac{1}{\gamma} \left\{ \left( \mathbf{\Omega}^{-1} \boldsymbol{\delta} \right) \boldsymbol{\alpha} + \tfrac{\boldsymbol{\delta}' \mathbf{\Omega} \boldsymbol{\delta}}{\text{Tr}(\boldsymbol{A} \boldsymbol{\Omega})} \left[ \left( \boldsymbol{\alpha} - \tfrac{1}{2} \, \text{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega}) \, \boldsymbol{\tau} \right)^2 - \boldsymbol{\alpha}^2 \right] \boldsymbol{a} \right\} \\ &= \tfrac{1}{\gamma} \left\{ \left( \mathbf{\Omega}^{-1} \boldsymbol{\delta} \right) \boldsymbol{\alpha} + \tfrac{\boldsymbol{\delta}' \mathbf{\Omega} \boldsymbol{\delta}}{\text{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega})} \left[ \tfrac{1}{2} \, \text{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega}) \, \boldsymbol{\tau} \, \boldsymbol{\alpha} + \tfrac{1}{4} \left( \text{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega}) \right)^2 \, \boldsymbol{\tau}^2 \right] \boldsymbol{a} \right\} \,, \end{split}$$

so that

$$\pi^* = \frac{1}{\gamma} \left\{ (\mathbf{\Omega}^{-1} \boldsymbol{\delta}) \alpha + (\boldsymbol{\delta}' \mathbf{\Omega} \boldsymbol{\delta}) \left[ \frac{1}{2} \tau \alpha + \frac{1}{4} \text{Tr}(\boldsymbol{A} \, \boldsymbol{\Omega}) \tau^2 \right] \boldsymbol{a} \right\}.$$
 (11.16)

As a reminder, the first term is what you would expect from the classical Merton problem since t5 a are the drifts of the assets. The second term proportional to *a* represents the correction due to co-integration. As the above expression shows, the perturbation around the 'Merton' portfolio decays as the terminal date approaches. That is, the agent ignores the short-term-alpha effect when trading is coming to a close.

#### **11.4.4** Numerical Experiments

In this section we showcase how the strategy behaves in a three-asset case. For this purpose the following modelling parameters are chosen:

$$\boldsymbol{\delta} = (1 \ 1 \ 0)' \,, \qquad \boldsymbol{a} = (-1 \ 0 \ 1)' \,, \qquad a_0 = 0 \,,$$

![](_page_20_Figure_1.jpeg)

Figure 11.7 A single sample path of the co-integrated asset prices and the resulting optimal strategy.

and

$$\boldsymbol{\sigma} = \begin{pmatrix} 0.2000 & 0 & 0 \ 0.0375 & 0.1452 & 0 \ 0.0250 & 0.0039 & 0.0967 \end{pmatrix} \quad \Rightarrow \quad \boldsymbol{\Omega} = \begin{pmatrix} 0.04 & 0.0075 & 0.005 \ 0.0075 & 0.0225 & 0.0015 \ 0.005 & 0.0015 & 0.01 \end{pmatrix} \,.$$

The volatilities of the three assets can be read off of the diagonal of  $\Omega$  to be  $\{2\%, 1.5\%, 1\%\}$ , and the corresponding correlation matrix  $\boldsymbol{\rho}$  is

$$\boldsymbol{\rho} = \begin{pmatrix} 1.00 & 0.25 & 0.25 \ 0.25 & 1.00 & 0.10 \ 0.25 & 0.10 & 1.00 \end{pmatrix} \, ,$$

Finally, we start the asset prices at the following levels:

$$Y_t^1 = 11.10$$
,  $Y_t^2 = 12.00$ ,  $Y_t^3 = 11.00$ .

The particular choice of the co-integration vector  $\boldsymbol{a}$  implies that only the first and third assets feed into the co-integration factor. Yet, the strength term  $\delta$ implies that only the first and second asset's drift are affected by that factor.

In Figure 11.7 we show a sample path of the asset prices, co-integration factor, optimal strategy, and agent's wealth process. In Figure 11.8 we show the histogram of the  $P\&L$ .

![](_page_21_Figure_1.jpeg)

Figure 11.8 Histogram of the P&L of the optimal pairs trading strategy.

# 11.5 **Bibliography and Selected Readings**

 Elliott, Van Der Hoek & Malcolm (2005), Tourin & Yan (2013), Leung & Li (2014), Leung & Ludkovski (2011).
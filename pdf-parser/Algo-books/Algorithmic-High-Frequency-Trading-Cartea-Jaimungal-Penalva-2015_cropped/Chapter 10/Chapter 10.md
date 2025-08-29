#### $10.1$ Introduction

In this chapter we model how a **market maker** (MM) maximises terminal wealth by trading in and out of positions using limit orders (LOs). The MM provides liquidity to the limit order book (LOB) by posting buy and sell LOs and the control variable is the depth, which is measured from the midprice, at which these LOs are posted. To formalise the problem, we list the relevant variables that we use throughout this section:

- $S = (S_t)_{0 \le t \le T}$ , denotes the midprice, with  $S_t = S_0 + \sigma W_t$ ,  $\sigma > 0$  and  $W = (W_t)_{0 \le t \le T}$  is a standard Brownian motion,
- $\delta^{\pm} = (\delta^{\pm}_t)_{0 \le t \le T}$  denote the depth at which the agent posts LOs; sell LOs are posted at a price of  $S_t + \delta_t^+$  and buy LOs at a price of  $S_t - \delta_t^-$ ,
- $M^{\pm} = (M^{\pm}_t)_{0 \le t \le T}$  denote the counting processes corresponding to the arrival of other participants' buy  $(+)$  and sell  $(-)$  market orders (MOs) which arrive at Poisson times with intensities  $\lambda^{\pm}$ ,
- $N^{\delta,\pm} = \left(N^{\delta,\pm}_t\right)_{0 \le t \le T}$  denote the controlled counting processes for the agent's filled sell  $(+)$  and buy  $(-)$  LOs,
- conditional on a market order (MO) arrival, the posted LO is filled with probability  $e^{-\kappa^{\pm}} \delta_t^{\pm}$ , with  $\kappa^{\pm} \geq 0$ ,
- $X^{\delta} = (X^{\delta}_t)_{0 \le t \le T}$  denotes the MM's cash process and satisfies the SDE

$$dX_t^{\delta} = (S_{t-} + \delta_t^+) \, dN_t^{\delta, +} - (S_{t-} - \delta_t^-) \, dN_t^{\delta, -} \,, \tag{10.1}$$

which accounts for the cash increase when a sell LO is lifted by a buy MO and the cash outflow when a buy LO is hit by an incoming sell MO,

•  $Q^{\delta} = (Q^{\delta}_t)_{0 \le t \le T}$  denotes the agent's inventory process and

$$Q_t^{\delta} = N_t^{\delta, -} - N_t^{\delta, +} \,. \tag{10.2}$$

As discussed in Section 8.2, whenever the process  $N^{\delta,\pm}$  jumps, the process  $M^{\delta,\pm}$  must also jump; but when  $M^{\delta,\pm}$  jumps,  $N^{\delta,\pm}$  will jump only if the MO is large enough to fill the agent's LO, and  $N^{\delta,\pm}$  is not a Poisson process. Moreover, note that the fill rate of LOs can be written as  $\Lambda_t^{\delta,\pm} = \lambda^{\pm} e^{-\kappa_{\pm} \delta_t^{\pm}}$ , which is the rate of execution of an LO.

To simplify notation, in the rest of this chapter we suppress the superscript  $\delta$  in the counting process for filled LOs, cash, and inventory. In Section 10.2 we discuss market making strategies when the MM does not face adverse selection costs, and her strategy takes into account restrictions on the amount of inventory she is willing to hold during the life of the strategy, as well as how costly it is to liquidate outstanding inventory at the terminal date of the strategy. In Section  $10.3$  the agent maximises terminal utility of cash holdings. Finally, in Section 10.4 we introduce various ways in which the MM faces adverse selection costs and how this affects the market making strategies.

#### 10.2 Market Making

In this section we assume that the MM seeks the strategy  $(\delta_s^{\pm})_{0 \le s \le T}$  that maximises cash at the terminal date  $T$ . We also assume that at time  $T$  the MM liquidates her terminal inventory  $Q_T$  using an MO at a price which is worse than the midprice to account for liquidity taking fees as well as the MO walking the LOB. Finally, the MM caps her inventory so that it is bounded above by  $\overline{q} > 0$  and below by  $q < 0$ , both finite, and also includes a running inventory penalty so that the performance criterion is

$$H^{\delta}(t,x,S,q) = \mathbb{E}_{t,x,q,S} \left[ X_T + Q_T^{\delta}(S_T^{\delta} - \alpha Q_T^{\delta}) - \phi \int_t^T (Q_u)^2 du \right],$$

where  $\alpha \geq 0$  represents the fees for taking liquidity (i.e. using an MO) as well as the impact of the MO walking the LOB, and  $\phi \geq 0$  is the running inventory penalty parameter. The MM's value function is

$$H(t, x, S, q) = \sup_{\delta^{\pm} \in \mathcal{A}} H^{\delta}(t, x, S, q), \qquad (10.3)$$

where  $\mathcal{A}$  denotes the set of admissible strategies, i.e.  $\mathcal{F}$ -predictable, bounded from below.

To solve the optimal control problem, a dynamic programming principle holds and the value function satisfies the DPE

$$\begin{split} \mathfrak{D} &= \partial_{t}H + \frac{1}{2}\sigma^{2}\partial_{SS}H - \phi\,q^{2} \\ &+ \lambda^{+}\sup_{\delta^{+}} \left\{ e^{-\kappa^{+}\delta^{+}} \left( H(t,x+(S+\delta^{+}),q-1,S)-H \right) \right\} \mathbbm{1}_{q>\underline{q}} \\ &+ \lambda^{-}\sup_{\delta^{-}} \left\{ e^{-\kappa^{-}\delta^{-}} \left( H\left(t,x-(S-\delta^{-}),q+1,S\right)-H \right) \right\} \mathbbm{1}_{q<\overline{q}} \,, \end{split} \tag{10.4}$$

where  $\mathbb{1}$  is the indicator function, with terminal condition

$$H(T, x, S, q) = x + q(S - \alpha q). \tag{10.5}$$

Recall that the set of admissible strategies imposes bounds on  $q_t$ , so that when  $q_t = \overline{q}$  (q) the optimal strategy is to post one-sided LOs which are obtained by solving (10.4) with the term proportional to  $\lambda^{-}$  ( $\lambda^{+}$ ) absent as enforced by the indicator function  $\mathbb{1}$  in the DPE. Alternatively, one can view these boundary cases as imposing  $\delta^- = +\infty$  and  $\delta^+ = +\infty$  when  $q = \overline{q}$  and q respectively.

Intuitively, the various terms in the DPE equation represent the arrival of MOs that may be filled by LOs together with the diffusion of the asset price through the term  $\frac{1}{2}\sigma^2\partial_{SS}H$ , and the effect of penalising deviations of inventories from zero along the entire path of the strategy which is captured by the term  $\phi q^2$ . In the second line of the DPE the sup over  $\delta^+$  contain the terms due to the arrival of a market buy order (which is filled by a limit sell order), and here we see the change in the value function  $H$  due to the arrival of the MO which fills the LO, so that cash increases by  $(S + \delta^+)$  and inventory decreases by one unit. Similarly, in the last line in the DPE the sup over  $\delta^-$  contain the analogous terms for the market sell orders which are filled by limit buy orders.

To solve the DPE we use the terminal condition  $(10.5)$  to make an ansatz for  $H.$  In particular, we write

$$H(t, x, q, S) = x + q S + h(t, q), \qquad (10.6)$$

which has a simple interpretation. The first term is the accumulated cash, the second term is the book value of the inventory marked-to-market (i.e. the value of the shares at the current midprice), and the last term is the added value from following an optimal market making strategy up to the terminal date.

We proceed by substituting the ansatz into  $(10.4)$  to obtain

$$\begin{split}\n\phi \, q^2 &= \partial_t h(t,q) + \lambda^+ \sup_{\delta^+} \left\{ e^{-\kappa^+ \delta^+} \left( \delta^+ + h(t,q-1) - h(t,q) \right) \right\} \, \mathbbm{1}_{q > \underline{q}} \\
&+ \lambda^- \sup_{\delta^-} \left\{ e^{-\kappa^- \delta^-} \left( \delta^- + h(t,q+1) - h(t,q) \right) \right\} \, \mathbbm{1}_{q < \overline{q}} \,, \n\end{split} \tag{10.7}$$

with terminal condition  $h(T,q) = -\alpha q^2$ .

Then the optimal depths in feedback form are given by

$$\delta^{+,*}(t,q) = \frac{1}{\kappa^{+}} - h(t,q-1) + h(t,q), \quad q \neq \underline{q}, \qquad (10.8a)$$

$$\delta^{-,*}(t,q) = \frac{1}{\kappa^{-}} - h(t,q+1) + h(t,q), \quad q \neq \overline{q}, \tag{10.8b}$$

and the boundary cases are  $\delta^{+,*}(t,q) = +\infty$  and  $\delta^{-,*}(t,q) = +\infty$  when  $q = \overline{q}$ and  $q$  respectively.

To understand the intuition behind the feedback controls we first note that the optimal  $\delta^{\pm}$  can be decomposed into two components. The first component,  $1/\kappa^{\pm}$ , is the optimal strategy for a MM who does not impose any restrictions on inventory  $(\alpha = \phi = 0 \text{ and } |q| = \overline{q} = \infty)$  – see below in subsection 10.2.1.

The second component, the term  $-h(t, q-1) + h(t, q)$ , controls for inventories through time. As expected, if inventories are long, then the strategy consists in posting LOs that increase the probability of limit sell orders being hit. Moreover, the function  $h(t,q)$  also induces mean reversion to an optimal inventory level, as a result of penalising accumulated inventories throughout the entire trading horizon and the strategy approaching  $T$  as well as the other parameters of the model, including  $\phi$ .

Substituting the optimal controls into the DPE we obtain

$$\phi q^{2} = \partial_{t} h(t,q) + \frac{e^{-1}\lambda^{+}}{\kappa^{+}} e^{-\kappa^{+}(-h(t,q-1)+h(t,q))} \mathbb{1}_{q > q} + \frac{e^{-1}\lambda^{-}}{\kappa^{-}} e^{-\kappa^{-}(-h(t,q+1)+h(t,q))} \mathbb{1}_{q < \overline{q}}.$$
 (10.9)

### Solving the DPE

It is possible to find an analytical solution to the DPE if the fill probabilities of LOs are the same on both sides of the LOB. In this case, if  $\kappa = \kappa^+ = \kappa^-$  then write

$$h(t,q) = \frac{1}{\kappa} \log \omega(t,q) \,,$$

and stack  $\omega(t,q)$  into a vector

$$\boldsymbol{\omega}(t) = \left[\,\omega(t,\overline{q}),\,\omega(t,\overline{q}-1),\ldots,\,\omega(t,\underline{q})\,\right]' \,.$$

Now, let **A** denote the  $(\overline{q} - q + 1)$ -square matrix whose rows are labelled from  $\overline{q}$ to  $q$  and whose entries are given by

$$\mathbf{A}_{i,q} = \begin{cases} -\phi \,\kappa \, q^2 \,, & i = q \,, \\ \lambda^+ \, e^{-1} \,, & i = q - 1 \,, \\ \lambda^- \, e^{-1} \,, & i = q + 1 \,, \\ 0 \,, & \text{otherwise} \,, \end{cases} \tag{10.10}$$

with terminal and boundary conditions  $\omega(T,q) = e^{-\alpha \kappa q^2}$ .

Then  $(10.9)$  becomes

 $\partial_t \boldsymbol{\omega}(t) + A \boldsymbol{\omega}(t) = \mathbf{0}$ .

The solution of this matrix ODE is straightforward and we finally have,

$$\boldsymbol{\omega}(t) = e^{\mathbf{A}(T-t)} \mathbf{z} \,, \tag{10.11}$$

where **z** is a  $(\overline{q} - \underline{q} + 1)$ -dim vector where each component is  $z_i = e^{-\alpha \kappa j^2}$ ,  $j = \overline{q}, \ldots, q.$ 

# Behaviour of the Strategy

Figure 10.1 shows the behaviour of the optimal depths as a function of time for different inventory levels. In the examples the arrival rate of MOs is  $\lambda^{\pm} = 1$ (there are on average 1 buy and 1 sell MO per second),  $\overline{q} = -q = 3$ , and  $\phi = 10^{-5}$ in panel (a), and  $\phi = 2 \times 10^{-4}$  in panel (b). In the left of panel (a) we show the optimal sell postings  $\delta^+$ , i.e. upon the arrival of a market buy order the MM is willing to sell one unit of the asset at the price  $S_t + \delta^+$ , and in the right of panel (a) we show the optimal buy postings  $\delta^+$ . For example, when the strategy is far away from expiry and inventories are close to the allowed minimum, the optimal

![](_page_4_Figure_1.jpeg)

Figure 10.1 The optimal depths as a function of time for various inventory levels and  $T = 30$ . The remaining model parameters are:  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 3$ ,  $\alpha = 0.0001, \ \sigma = 0.01, \ S_0 = 100.$ 

sell posting is furthest away from the midprice because only at a very 'high' price is the MM willing to decrease her inventories further, and at the same time the optimal buy posting is very close to the midprice because the strategy would like to complete round-trip trades (i.e. a buy followed by a sell or a sell followed by a buy) and push inventories to zero.

We also observe that as the strategy approaches  $T$  and  $q_t < 0$  ( $q_t > 0$ ), the optimal sell (buy) depth  $\delta^+$  ( $\delta^-$ ) decreases (increases). To understand the intuition behind the optimal strategy note that if the terminal inventory  $q_T < 0$ is liquidated at the price  $S_T - \alpha q_T$ , then when  $\alpha$  is sufficiently low, as well as being fractions of a second away from expiry, it is optimal to post nearer the midprice to increase the chances of being filled (i.e. selling one more unit of the asset) because the price is not expected to move too much before expiry and the entire position will be unwound at the midprice - making a profit on the last unit of the asset that was sold.

It is also interesting to see that the optimal strategy induces mean reversion in inventories. For example, if  $q_t = 2$  then the sell depth is lower than the buy

![](_page_5_Figure_1.jpeg)

**Figure 10.2** Long-term inventory level. Model parameters are:  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -\underline{q} = 10, \ \alpha = 0.0001, \ \sigma = 0.01, \ S_0 = 100, \text{ and } \phi = \left\{2 \times 10^{-3}, \ 10^{-3}, \ 5 \times 10^{-4}\right\}.$ 

depth,  $\delta^+ < \delta^-$ , so that it is more likely for the strategy to sell, than to buy, one unit of the asset. This asymmetry in the optimal depths is what induces mean reversion to zero in the inventory. Moreover, in panel (b) the strategy's running inventory penalty is much higher and it is clear that the higher  $\phi$  is, the quicker inventories will revert to zero.

We also see that the strategy  $\delta^{*\pm}(t,q)$  induces mean reversion in inventories, by observing that the expected drift in inventories is given by the difference in the arrival rates of filled orders. Thus, given the pair of optimal strategies  $\delta^{+,*}(t,q), \delta^{-,*}(t,q)$ , the expected drift in inventories is given by

$$\mu(t,q) \triangleq \lim_{s \downarrow t} \frac{1}{s-t} \mathbb{E} \left[ Q_s - Q_t \, | \, Q_{t^-} = q \right]$$
  
$$= \lambda^- e^{-\kappa^- \delta^{-,*}(t,q)} - \lambda^+ e^{-\kappa^+ \delta^{+,*}(t,q)} \,.$$
(10.12)

Note that the drift  $\mu(t,q)$  depends on time. For instance, it is clear that for the same level of inventory the speed will be different depending on how near or far the strategy is from the terminal date, because at time  $T$  the strategy tries to unwind all outstanding inventory.

Figure 10.2 shows the optimal level of inventory to which the strategy reverts, where we assume that we are far away from  $T - t \to \infty$  in (10.12). The model parameters are  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 10$ ,  $\alpha = 0.0001$ ,  $\sigma = 0.01$ ,  $S_0 = 100$ and we vary the running penalty  $\phi = \{2 \times 10^{-3}, 10^{-3}, 5 \times 10^{-4}\}$ . Note that for the set of parameters we are using here it suffices to be a few seconds away from the terminal date so that the optimal postings are not affected by the proximity to  $T$ . In the left panel of the figure we plot the fill rate probabilities of both sides of the LOB which are given by  $\lambda^{\pm}e^{-\kappa^{\pm}\delta^{\pm(t,q),*}}$ . Blue circles and blue crosses are the fill rate probabilities for the sell side and buy side of the LOB respectively when  $\phi = 2 \times 10^{-4}$ .

Figure  $10.3$  shows the inventory and price path for one simulation of the strategy. The model parameters are  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 10$ ,  $\phi = 2 \times 10^{-4}$ ,

![](_page_6_Figure_1.jpeg)

**Figure 10.3** Inventory and midprice path. Model parameters are:  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 10, \ \phi = 2 \times 10^{-4}, \ \alpha = 0.0001, \ \sigma = 0.01, \ S_0 = 100.$ 

 $\alpha = 0.0001, \sigma = 0.01, S_0 = 100$ . In the left panel we see how the inventory is mean reverting to zero and for this particular path we see that although the maximum and minimum amount of inventory that the strategy is allowed to hold is 10, it never goes beyond five units of the asset short or long.

The right panel of Figure  $10.3$  shows a window of the midprice path along with MM's buy and sell LOs. Solid circles in the figure show the incoming MO's which are filled by the MM's resting LOs (a red circle is a sell MO filled by the MM's buy LO and a blue circle is a buy MO filled by the MM's sell LO) and grey circles represent MOs that were filled by other market participants. The distance between the midprice and the MOs that arrive shows how far the MOs are walking into the LOB. At the beginning of the window, the agent's inventory is zero and we observe that the strategy acquires two units (one at  $185.3s$  and another at  $187.5s$ ) before the first sell order (at  $187.8s$ ) is filled and then closed out an instant later (at  $187.9s$ ). After the first filled buy order the strategy remains asymmetric and the agent posts closer to the midprice on the sell side of the book, compared to the buy side of the book, to rid herself of her inventory. At  $189s$ ,  $190.2s$ ,  $190.8s$ ,  $191.1s$  and  $191.9s$ , a sequence of sell orders is filled and the agent holds a short position of 2 assets after the last sale at  $191.9s.$  Her strategy is therefore to post closer to the midprice on the buy side of the book to increase her chance of unwinding her position. These shifts in her posts, which induce the unwinding of any inventory she acquires (long or short), continues until the end of the trading horizon.

Now we turn to discussing the financial performance of the strategy. The left panel of Figure 10.4 shows the profit and loss  $(P\&L)$  of the optimal strategy and the right panel shows the lifetime inventory for different running penalty parameters  $\phi = \{10^{-5}, 5 \times 10^{-5}, 10^{-3}, 10^{-2}\}$ . We observe that when  $\phi$  increases the histogram of  $P\&L$  shifts to the left because the strategy does not allow inventory positions to stray away from zero, and hence expected profits decrease. The lifetime inventory histogram shows how much time the strategy holds an inventory of n. For example, when  $\phi = 10^{-2}$  we know that the strategy heavily penalises

![](_page_7_Figure_1.jpeg)

**Figure 10.4** P&L and Life Inventory of the optimal strategy for  $10,000$  simulations. The remaining model parameters are:  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\bar{q} = -q = 10$ ,  $\alpha = 0.0001$ ,  $\sigma = 0.01$ , and  $S_0 = 100$ .

deviations of running inventory from zero, so the strategy spends most of the time at inventory levels of  $-1$ , 0, 1. As the running inventory penalty becomes smaller, the strategy spends more time at levels away from zero.

#### 10 2 1 Market Making with no Inventory Restrictions

If we assume that the MM does not penalise running inventories, does not pick up a terminal inventory penalty, that is  $\phi = \alpha = 0$ , and there are no constraints on the amount of inventory the strategy may accumulate, i.e  $|q|, \overline{q} \to \infty$ , then the MM's strategy simplifies to

$$\delta^{+,*}(t,q) = \frac{1}{\kappa^{+}}, \quad \text{and} \quad \delta^{-,*}(t,q) = \frac{1}{\kappa^{-}}.$$
 (10.13)

This optimal strategy tells the MM to post in the LOB so that the probability of the LOs being filled is maximised. To see this we observe that if there are no penalties for liquidating terminal inventory, by assuming  $\alpha = 0$  the terminal inventory is unwound at the midprice, and there is no running penalty for inventories straying away from zero, then we make the ansatz

$$H(t, x, q, S) = x + qS + h(t). \qquad (10.14)$$

This is similar to the one proposed above, see (10.6), but here  $h(t)$  does not depend on  $q$  because the MM does not pose any restrictions on inventory throughout the life of the strategy and can liquidate terminal inventory at the midprice. Thus, substituting the ansatz into the DPE

$$0 = \partial_t h + \lambda^+ \sup_{\delta^+} \left\{ e^{-\kappa^+ \delta^+} \delta^+ \right\} + \lambda^- \sup_{\delta^-} \left\{ e^{-\kappa^- \delta^-} \delta^- \right\} \tag{10.15}$$

with terminal condition  $h(T) = 0$ , delivers the result (10.13).

Furthermore, we can show that

$$h(t) = e^{-1} \left(\frac{\lambda^{+}}{\kappa^{+}} + \frac{\lambda^{-}}{\kappa^{-}}\right) (T - t).$$

This result is simple to interpret. An MM who does not penalise inventories and who unwinds terminal inventory at the midprice, will make markets by maximising the probability of her LOs being filled at every instant in time regardless of the inventory position or how close the terminal date is. Therefore, the MM's problem reduces to choosing  $\delta^{\pm}$  to maximise the expected depth conditional on an MO hitting or lifting the appropriate side of the LOB, i.e. to maximise  $\delta^{\pm}e^{-\kappa^{\pm}\delta^{\pm}}$ . The first order condition of this optimisation problem is

$$e^{-\kappa^{\pm}\delta^{\pm}} - \kappa^{\pm}\delta^{\pm}e^{-\kappa^{\pm}\delta^{\pm}} = 0, \qquad (10.16)$$

so the optimal depths are as in  $(10.13)$ .

#### 10.2.2 Market Making At-The-Touch

In very liquid markets, most orders do not walk the book and instead tend to only lift or hit LOs posted at-the-touch. To capture this market feature, in this section we investigate the agent's optimal postings at-the-touch, i.e. at the best bid and best offer. Throughout we assume that the spread is constant and equal to  $\Delta$ . Next, let  $\ell_t^{\pm} \in \{0,1\}$  denote whether the agent is posted on the sell side  $(+)$  or buy side  $(-)$  of the LOB. In this way, the agent may be posted on both sides of the book, only the sell side, only the buy side, or not posted at all. Her performance criteria is

$$H^{\ell}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X_T^{\ell} + Q_T^{\ell} \left( S_T - \left( \frac{\Delta}{2} + \varphi \, Q_T^{\ell} \right) \right) - \phi \int_t^T \left( Q_u^{\ell} \right)^2 du \right],$$

where her cash process  $X_t^{\ell}$  now satisfies the SDE

$$dX_t^{\ell} = \left(S_t + \frac{\Delta}{2}\right) dN_t^{+,\ell} - \left(S_t - \frac{\Delta}{2}\right) dN_t^{-,\ell},$$

where  $N_t^{\pm,\ell}$  denote the counting process for filled LOs. We also further assume that, if she is posted in the LOB, when a matching MO arrives her LO is filled with probability one. In this case,  $N_t^{\pm,\ell}$  are controlled doubly stochastic Poisson processes with intensity  $\ell_t^{\pm} \lambda^{\pm}$ . Finally, at the terminal date any open inventory position is liquidated using an MO and the price obtained per share is the best bid  $(Q_T > 0)$  or offer  $(Q_T < 0)$  and picks up a penalty  $\varphi Q_T^2$ , with  $\varphi \geq 0$ , which includes market impact (walking the LOB) and liquidity taking fees.

As before, the set  $\mathcal{A}$  of admissible strategies are  $\mathcal{F}$ -predictable such that the agent is not posted on the buy (sell) side if her inventory is equal to the upper (lower) inventory constraints  $\overline{q}$  (q) and her value function is denoted by

$$H(t, x, S, q) = \sup_{\ell \in \mathcal{A}} H^{\ell}(t, x, S, q) .$$

### The Resulting DPE

Applying the DPP, we find the agent's value function  $H$  should satisfy the DPE

$$0 = \left(\partial_{t} + \frac{1}{2}\sigma^{2}\partial_{SS}\right)H - \phi q^{2}$$
  
+  $\lambda^{+} \max_{\ell^{+} \in \{0,1\}} \left\{ \left(H\left(t, x + \left(S + \frac{\Delta}{2}\right) \ell^{+}, S, q - \ell^{+}\right) - H\right) \right\} \mathbb{1}_{q > \underline{q}}$   
+  $\lambda^{-} \max_{\ell^{-} \in \{0,1\}} \left\{ \left(H\left(t, x - \left(S - \frac{\Delta}{2}\right) \ell^{-}, S, q + \ell^{-}\right) - H\right) \right\} \mathbb{1}_{q < \overline{q}},$ 

subject to the terminal condition

$$H(T, x, S, q) = x + q \left(S - \left(\frac{\Delta}{2} + \varphi q\right)\right)$$

The various terms in the DPE carry the following interpretations:

- the first line in the DPE represents the diffusive component of the midprice and the running inventory penalisation,
- the maximisation terms represent the agent's control to post or not on the sell or buy side of the LOB,
- the maximisation term in the second line represents the change in value function, if the agent is posted, due to the arrival of an MO which lifts the agent's offer,
- the third line is for the other side of the book.

The terminal condition once again suggests the ansatz which splits out the accumulated cash, the book value of the shares marked-to-market at the midprice, and the added value from optimally making markets throughout the remaining life of the strategy:

$$H(t, x, S, q) = x + q S + h(t, q),$$

and on substituting this ansatz into the above DPE we find that  $h$  satisfies

$$\begin{split} 0 &= \partial_t h - \phi \, q^2 \\ &+ \lambda^+ \max_{\ell^+ \in \{0, 1\}} \left\{ \left( \ell^+ \, \frac{\Delta}{2} + \left[ h(t, q - \ell^+) - h(t, q) \right] \right) \right\} \, \mathbb{1}_{q > \underline{q}} \\ &+ \lambda^- \max_{\ell^- \in \{0, 1\}} \left\{ \left( \ell^- \, \frac{\Delta}{2} + \left[ h(t, q + \ell^-) - h(t, q) \right] \right) \right\} \, \mathbb{1}_{q < \overline{q}} \,, \end{split}$$

subject to the terminal condition

$$h(T,q) = -q \left(\frac{\Delta}{2} + \varphi q\right) .$$

The form of the optimising terms allows us to characterise the optimal postings in a compact form. When  $\ell = 0$  both terms that are being maximised are zero, hence, the optimal postings of the agent can be characterised succinctly as

$$\ell^{+,*}(t,q) = \mathbb{1}_{\left\{ \frac{\Delta}{2} + [h(t,q-1) - h(t,q)] > 0 \right\} \cap \{q > \underline{q}\}} ,$$
  
$$\ell^{-,*}(t,q) = \mathbb{1}_{\left\{ \frac{\Delta}{2} + [h(t,q+1) - h(t,q)] > 0 \right\} \cap \{q < \overline{q}\}} .$$
  
(10.17)

255

![](_page_10_Figure_1.jpeg)

Figure 10.5 The optimal strategy for the agent who posts only at-the-touch.

The interpretation of this result is that the agent posts an LO on the appropriate side of the LOB by ensuring that she only posts if the arrival of an MO, which hit/lifts her LO, produces a change in her value function larger than  $-\frac{\Delta}{2}$ .

### Strategy Features

Next, we illustrate some typical features of the optimal solution to gain some insight into the optimal strategy. For this purpose we use the following set of  $model$  parameters:

$$T = 300 \text{ sec}, \quad \overline{q} = -\underline{q} = 20, \quad \lambda^{\pm} = \frac{50}{300},$$
  
 $\Delta = 0.01, \quad \phi = 0.01, \quad \sigma = 0.001.$ 

Note that the rate of arrival of market orders is chosen so that on average the agent's upper/lower inventory bounds are no more than  $20\%$  of the market.

Figure 10.5 shows how the agent's optimal posting varies with time and the running penalty. The left panel explicitly shows that the agent posts only sell LOs whenever her inventory is very high, and only buy LOs whenever her inventory is very low. In the central region, she posts both buy and sell LOs. In this manner, the agent's inventory is constrained to remain within one unit of the green region - once her inventory escapes she posts only on one side of the book thus pushing inventory back into the green region. We therefore see that despite the agent allowing herself to hold up to 20 units of the asset, long or short, the running penalty constrains her strategy. Furthermore, note that as the running penalty increases, the region over which the agent constrains her inventory shrinks, and eventually reaches the point at which she only takes on one single unit of the asset (long or short) and then immediately liquidates it.

Later, in subsection  $10.4.2$  we see how the agent modifies her strategy to account for adverse selection effects.

#### Market Making Optimising Volume 10.2.3

In the previous sections, when the agent posts an LO, she is assumed to be placing a single order. This single order can be thought of as the typical order size of, say, 100 shares. The agent may, however, wish to optimise the posted volume. In this case, the agent's performance criteria is taken to be

$$H^{\ell}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X_T^{\ell} + Q_T^{\ell} \left( S_T - \left( \frac{\Delta}{2} + \varphi \, Q_T^{\ell} \right) \right) - \phi \! \! \int_t^T \! \! \left( Q_u^{\ell} \right)^2 du \right],$$

and her cash process  $X_t^{\ell}$  now satisfies the SDE

$$dX_t^{\ell} = \left(S_t + \frac{\Delta}{2}\right) \ell_t^+ dN_t^{+,\ell} - \left(S_t - \frac{\Delta}{2}\right) \ell_t^- dN_t^{-,\ell},$$

where  $\ell_t^{\pm}$  are  $\mathcal{F}$ -predictable such that

$$\ell_t^+ \in \left\{0, 1, 2, \ldots, q_{t^-} - \underline{q}\right\} \quad \text{and} \quad \ell_t^- \in \left\{0, 1, 2, \ldots, \overline{q} - q_{t^-}\right\},\$$

and  $N_t^{\pm,\ell}$  denote the counting processes for her filled LOs – not accounting for the volume traded (i.e. it only counts whether an MO arrived and filled her posted LO). The restrictions on the volume ensure that the agent never posts a volume which, if filled, would send her inventory outside of her allowed trading bounds. We further assume that if she is posted in the LOB when a matching MO arrives, her LO is filled with probability  $\rho(\ell)$  where  $\ell$  is posted volume. For example,  $\rho(\ell) = e^{-\kappa \ell}$  would represent an exponential fill probability. In this case,  $N_t^{\pm,\ell}$  are controlled doubly stochastic Poisson processes with intensity  $\rho(\ell_t^{\pm}) \lambda^{\pm} \mathbb{1}_{\ell_t^{\pm} > 0}$ . In this formulation, we have further assumed that if the agent makes a post of a given volume, the entire volume is matched or none at all is matched. The approach here can be generalised to account for partial fills of postings, but this is left as an exercise for the reader.

As before, the set  $\mathcal{A}$  of admissible strategies also restricts her so that the strategy does not post on the buy (sell) side of the LOB if her inventory is equal to the upper (lower) inventory constraints  $\overline{q}$  (q). Her value function is denoted by

$$H(t, x, S, q) = \sup_{\ell \in \mathcal{A}} H^{\ell}(t, x, S, q) .$$

### The Resulting DPE

This analysis is similar to that of the previous section, except now the set of strategies allows the agent to post multiple volumes. In this case, applying the DPP we find the agent's value function  $H$  should satisfy the DPE

$$0 = \left(\partial_{t} + \frac{1}{2}\sigma^{2}\partial_{SS}\right)H - \phi q^{2}$$
  
+  $\lambda^{+} \max_{\ell^{+} \in \{0,1,\ldots,q-\underline{q}\}} \left\{\rho(\ell^{+})\left(H\left(t,x+\left(S+\frac{\Delta}{2}\right)\ell^{+},S,q-\ell^{+}\right)-H\right)\right\} \mathbbm{1}_{q>\underline{q}}$   
+  $\lambda^{-} \max_{\ell^{-} \in \{0,1,\ldots,\overline{q}-q\}} \left\{\rho(\ell^{-})\left(H\left(t,x-\left(S-\frac{\Delta}{2}\right)\ell^{-},S,q+\ell^{-}\right)-H\right)\right\} \mathbbm{1}_{q<\overline{q}}$ ,

![](_page_12_Figure_1.jpeg)

Figure 10.6 The optimal volume postings for the agent who posts only at-the-touch.

subject to the terminal condition

$$H(T, x, S, q) = x + q \left(S - \left(\frac{\Delta}{2} + \varphi q\right)\right)$$

With the exception that the maxima are computed over the set of allowed volumes and cash jumps accordingly, this non-linear PDE is identical to the one derived in the previous section when the agent did not optimise over the volume of the LOs. The terminal condition suggests the usual ansatz  $H(t, x, S, q) =$  $x+qS+h(t,q)$  which splits out the accumulated cash, book value of the inventory marked-to-market using the midprice, and the added value from optimally making markets throughout the remaining life of the strategy. On substituting into the DPE we find that  $h$  satisfies

$$0 = \partial_t h - \phi q^2$$
  
+  $\lambda^+ \max_{\ell^+ \in \{0, 1, \dots, q - \underline{q}\}} \left\{ \rho(\ell^+) \left( \ell^+ \frac{\Delta}{2} + \left[ h(t, q - \ell^+) - h(t, q) \right] \right) \right\} \mathbbm{1}_{q > \underline{q}}$   
+  $\lambda^- \max_{\ell^- \in \{0, 1, \dots, q - \overline{q}\}} \left\{ \rho(\ell^-) \left( \ell^- \frac{\Delta}{2} + \left[ h(t, q + \ell^-) - h(t, q) \right] \right) \right\} \mathbbm{1}_{q < \overline{q}},$ 

subject to the terminal condition

$$h(T,q) = -q \left(\frac{\Delta}{2} + \varphi \, q\right)$$

### Strategy Features

Figure  $10.6$  shows the agent's optimal volume postings at-the-touch using the following model parameters:

$$T = 10 \text{ sec}, \quad \overline{q} = -\underline{q} = 20, \quad \lambda^{\pm} = 5,$$
$$\Delta = 0.01, \quad \varphi = 0.01, \quad \sigma = 0.001,$$
$$\rho(\ell) = e^{-0.01 \ell}, \quad \text{and} \quad \phi = 10^{-3}.$$

Notice that the posted sell volume increases as inventory increases, while the posted buy volume increases as inventory decreases. Furthermore, there are large

![](_page_13_Figure_1.jpeg)

**Figure 10.7** The optimal volume postings (at  $t = 0$ ) for the agent who posts only at-the-touch. The left panel has  $\phi = 10^{-3}$  and the right panel shows only  $\ell^+$ .

regions where the agent is posted only on one side of the LOB. Figure 10.7 shows the asymptotic optimal volume postings at the start of trading. The left panel shows both the buy and sell postings when  $\phi = 10^{-3}$ , while the right panel shows how the postings vary when  $\phi$  varies for the sell side of the book. For  $\phi = 10^{-3}$ , the agent stops posting limit sell orders when her inventory is at or below  $-7$ and stops posting limit buy orders when her inventory is at or above  $+7$ . As the right panel in Figure  $10.7$  shows, the critical level below which the agent stops posting moves towards zero inventory as the inventory penalisation parameter  $\phi$  increases. With  $\phi = 0.1$ , the agent will withdraw from the market and simply not post any limit orders.

Interestingly, the agent's posted volume is typically not sufficient to draw her inventory back to zero. For example, when  $\phi = 10^{-3}$  and her inventory is 10, she will post only a sell LO for 7 units, which once filled, will draw her inventory down to 3. At this point, she will post a sell LO for 5 units and a buy LO for 3 units, neither of which if filled pulls her inventory to zero.

#### $10.3$ Utility Maximising Market Maker

In the previous section, the agent was indifferent to uncertainty in the cash value of her sales and instead maximised expected profit from making markets subject to inventory controls. Some agents, however, may instead wish to penalise uncertainty in their sales directly. Here, we show that if the agent uses exponential utility as a performance measure, her strategy will be identical (up to a constant and a re-scaling of parameters) to the one implied by the running penalty studied in Section  $10.2$ .

To this end, suppose the agent sets preferences based on expected utility of terminal cash with exponential utility  $u(x) = -e^{-\gamma x}$ . In this case, her performance criteria is

$$G^{\delta}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ -\exp\left\{-\gamma \left(X_T^{\delta} + Q_T^{\delta} \left(S_T - \alpha Q_T^{\delta}\right)\right)\right\} \right] .$$

Using the standard approach, her value function,

$$G(t, x, S, q) = \sup_{\delta \in \mathcal{A}} G^{\delta}(t, x, S, q),$$

will satisfy the  $DPE$ 

$$\begin{cases}\n\left(\partial_{t} + \frac{1}{2}\sigma^{2}\partial_{SS}\right)G \\
+ \lambda^{+} \sup_{\delta^{+}} \left\{e^{-\kappa^{+}\delta^{+}} \left[G(t,x+(S+\delta^{+}),S,q-1)-G\right] \mathbb{1}_{q>\underline{q}}\right\} \\
+ \lambda^{-} \sup_{\delta^{-}} \left\{e^{-\kappa^{-}\delta^{-}} \left[G(t,x-(S-\delta^{-}),S,q+1)-G\right] \mathbb{1}_{q<\overline{q}}\right\} \\
= 0, \\
G(t,x,S,0) = -e^{-\gamma x}, \\
G(T,x,S,q) = -e^{-\gamma(x+q(S-\alpha q))}.\n\end{cases}$$

We leave it as an exercise for the reader to show that ansatz

$$G(t, x, S, q) = -e^{-\gamma(x+qS+g(t,q))}$$

leads to the following equation for  $g(t, q)$ :

$$\partial_t g - \frac{1}{2} \sigma^2 \gamma q^2 + \sup_{\delta^+} \lambda^+ e^{-\kappa^+ \delta^+} \frac{1 - e^{-\gamma \left(\delta^+ + g(t, q-1) - g(t, q)\right)}}{\gamma} + \sup_{\delta^-} \lambda^- e^{-\kappa^- \delta^-} \frac{1 - e^{-\gamma \left(\delta^- + g(t, q+1) - g(t, q)\right)}}{\gamma} = 0, \tag{10.18}$$

with terminal and boundary conditions

$$g(t, 0) = 0$$
, and  $g(T, q) = -\alpha q^2$ .

From the first order condition, we find that the optimal depths, in feedback control form, at which the agent posts are

$$\delta^{*,+} = \frac{1}{\gamma} \log\left(1 + \frac{\gamma}{\kappa^{+}}\right) + g(t,q) - g(t,q-1), \qquad q > \underline{q},$$
  
$$\delta^{*,-} = \frac{1}{\gamma} \log\left(1 + \frac{\gamma}{\kappa^{-}}\right) + g(t,q) - g(t,q+1), \qquad q < \overline{q}.$$
 (10.19)

This form is very similar to, but slightly differs from, the optimal depth in the previous section provided in (10.8). The  $g$  function may differ from  $h$  and the base line level  $(\kappa^{\pm})^{-1}$  is modified to  $(\hat{\kappa}^{\pm})^{-1} = \frac{1}{\gamma} \log \left(1 + \frac{\gamma}{\kappa^{\pm}}\right)$ . This modification can be seen as a risk aversion bias. Indeed, in the limit of zero risk-aversion

$$\hat{\kappa}^{\pm} \xrightarrow{\gamma \downarrow 0} \kappa^{\pm} \,,$$

and the result from the previous section is recovered.

Substituting this feedback form into  $(10.18)$ , we now find the non-linear ODE

$$\partial_t g - \frac{1}{2}\sigma^2 \gamma q^2 + \frac{\hat{\lambda}^+}{\kappa^+} e^{-\kappa^+(g(t,q)-g(t,q-1))} + \frac{\hat{\lambda}^-}{\kappa^-} e^{-\kappa^-(g(t,q)-g(t,q+1))} = 0,$$

where

$$\hat{\lambda}^{\pm} = \left(\kappa^{\pm}/(\kappa^{\pm} + \gamma)\right)^{1 + \kappa^{\pm}/\gamma} \lambda^{\pm}.$$

In the limit of zero risk-aversion  $\hat{\lambda}^{\pm} \xrightarrow{\gamma \downarrow 0} e^{-1} \lambda^{\pm} = \tilde{\lambda}^{\pm}$  and once again we recover the parameter that appears in  $(10.9)$ . The above ODE is in fact identical in structure to  $(10.9)$ . Hence, matching parameters by setting

$$\phi = \frac{1}{2}\sigma^2\gamma, \quad \lambda_0 = e^{+1}\hat{\lambda}, \quad \text{and} \quad \kappa_0 = \kappa,$$

where the subscript  $0$  denotes the parameters to use in the base model from the previous section, we see that  $h(t,q)$  and  $g(t,q)$  will coincide and the optimal strategies satisfy the relation

$$\delta^{\pm,*} = \delta_0^{\pm,*} + \left( (\hat{\kappa}^{\pm})^{-1} - (\kappa_0^{\pm})^{-1} \right) \,. \tag{10.20}$$

In other words, with a re-scaling of model parameters, the optimal strategy for the utility maximising agent is the same, up to a constant shift, as that of the agent who only penalises running inventory.

In addition to the relationship between the optimal strategies, the value functions can be written in terms of one another. Since  $h(t,q) = g(t,q)$ , we have

$$H(t,x,S,q) = -\frac{1}{\gamma} \log \left( -G(t,x,S,q) \right) \,,$$

or writing the value function in the original control form, we obtain

$$\begin{split} & \sup_{\boldsymbol{\delta} \in \mathcal{A}} \mathbb{E}_{t,x,S,q} \left[ X_{\tau}^{\boldsymbol{\delta}} + Q_{\tau}^{\boldsymbol{\delta}} (S_{\tau} - \alpha Q_{\tau}) - \phi \int_{0}^{\tau} (Q_{s}^{\boldsymbol{\delta}})^{2} \, ds \right] \\ & = -\frac{1}{\gamma} \log \left( -\sup_{\boldsymbol{\delta} \in \mathcal{A}} \mathbb{E}_{t,x,S,q} \left[ -\exp \left\{ -\gamma \left( X_{\tau}^{\boldsymbol{\delta}} + Q_{\tau}^{\boldsymbol{\delta}} (S_{\tau} - \alpha Q_{\tau}) \right) \right\} \right] \right). \end{split} \tag{10.21}$$

This relationship between the value functions is in fact part of a more general result that relates optimisation problems to exponential utility, and optimisation problems to penalties (see the further readings section).

#### $10.4$ Market Making with Adverse Selection

The market place is populated by traders that come to the market for different reasons and with varying degrees of information. One of the most important risks faced by MMs is adverse selection risk. As discussed in Chapter 2 (see for example Sections  $2.2$  and  $2.3$ ), when trading with informed market participants the MM is exposed to having a sell limit order  $(LO)$  filled right before prices

go up, or a buy LO filled before prices go down. In this section we extend the market making problem developed in Section 10.2, and present two ways in which midprice dynamics incorporate adverse selection effects. In the first model we assume that the midprice undergoes jumps in the direction of incoming market orders (MOs). In the second specification the midprice's drift has a short-termalpha component which is affected by the arrival of MOs.

#### 10.4.1 Impact of Market Orders on Midprice

Here we assume that the midprice dynamics follows

$$dS_t = \sigma dW_t + \epsilon^+ dM_t^+ - \epsilon^- dM_t^-, \qquad (10.22)$$

where *M;t-* and *Mt-* are Poisson processes, with intensities .A <sup>+</sup>and .>-- respectively, which count the number of buy ( +) and sell ( -) MOs. Every time an MO arrives, the midprice will undergo a jump of size E <sup>±</sup>which are i.i.d. and whose distribution functions are p<sup>±</sup>with finite first moment denoted by c: <sup>±</sup>= JE[E<sup>±</sup> ].

Intuitively, here we can view the dynamics of the midprice as the sum of two components. The first component, the Brownian motion on the right-hand side of (10.22), captures the changes in the midprice that are due to information flows that reach all or some market participants who subsequently update their quotes. The other component, the jump process with increments <sup>E</sup> <sup>+</sup>*dM;t-* - E- *dMt-,*  represents the changes in the midprice caused by the arrival of MOs that have a permanent price impact. MOs may come at times when there is enough liquidity in the market - hence prices remain unchanged or change by a negligible amount; or they may arrive at times when liquidity is thin or the orders are sent by traders with superior information, and these trades have a permanent impact on prices. The impact of trading on the midprice may also be viewed as the action of informed traders. If an informed trader purchases (sells) shares, he will only do so if the asset price is known to be going up (down). The resulting increase (decrease) of the mid price following informed trading can be approximated by an immediate, and permanent, price impact as we model here.

The rest of the MM's setup is as in Section 10.2, with the only difference that here the midprice follows (10.22). For convenience we repeat the MM's performance criteria:

$$H^{\delta}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X_T^{\delta} + Q_T^{\delta}(S_T - \alpha Q_T^{\delta}) - \phi \int_t^T (Q_u^{\delta})^2 du \right],$$

so her value function is

$$H(t, x, S, q) = \sup_{\delta^{\pm} \in \mathcal{A}} H^{\delta}(t, x, S, q) .$$

Thus the MM's value function satisfies the DPE

$$0 = \partial_{t}H + \frac{1}{2}\sigma^{2}\partial_{SS}H - \phi q^{2}$$
  
 
$$+ \lambda^{+} \sup_{\delta^{+}} \left\{ e^{-\kappa^{+}\delta^{+}} \mathbb{1}_{q>q} \mathbb{E} \left[ H(t,x+(S+\delta^{+}),S+\epsilon^{+},q-1) - H \right] \right.$$
  
 
$$+ \left( 1 - e^{-\kappa^{+}\delta^{+}} \mathbb{1}_{q>q} \right) \mathbb{E} \left[ H(t,x,S+\epsilon^{+},q) - H \right] \right\} \qquad (10.23)$$
  
 
$$+ \lambda^{-} \sup_{\delta^{-}} \left\{ e^{-\kappa^{-}\delta^{-}} \mathbb{1}_{q<\overline{q}} \mathbb{E} \left[ H(t,x-(S-\delta^{-}),S-\epsilon^{-},q+1) - H \right] \right\}$$
  
 
$$+ \qquad e^{-\kappa^{-}\delta^{-}} \mathbb{1}_{q<\overline{q}} \right\} \mathbb{E} \left[ H(t,x,S-\epsilon^{-},q) - H \right] \right\},$$

subject to the terminal condition

$$H(T, x, S, q) = x + q(S - \alpha q), \qquad (10.24)$$

and where the expectation is over the random variables  $\epsilon^{\pm}$  (not over x, S, or q) and  $\mathbb{1}$  is the indicator function.

Intuitively, the various terms in the HJB equation have the same interpretation as the case above in Section  $10.2$ , with a difference in how the value function changes when the midprice jumps upon the arrival of an MO. To see this, note that the sup over  $\delta^+$  contains the terms due to the arrival of a market buy order (which is filled by a limit sell order). The first term represents the expected change in the value function  $H$  due to the arrival of an MO which fills the LO and the midprice  $S_t$  jumps up by the random amount  $\epsilon^+$ ; and the second term represents the arrival of an MO which does not reach the LO's price level (but still causes a random jump in the midprice). Similarly, the sup over  $\delta^-$  contains the analogous terms for the market sell orders which are filled by limit buy orders.

To solve the DPE we make the ansatz

$$H(t, x, S, q) = x + q S + h(t, q), \qquad (10.25)$$

and substituting it into the DPE we obtain

$$\begin{split}\n\phi \, q^2 &= \partial_t h + \lambda^+ \sup_{\delta^+} \left\{ e^{-\kappa^+ \delta^+} \left( \delta^+ - \varepsilon^+ + h_{q-1} - h_q \right) \right\} \, \mathbbm{1}_{q > \underline{q}} \\
&+ \lambda^- \sup_{\delta^-} \left\{ e^{-\kappa^- \delta^-} \left( \delta^- - \varepsilon^- + h_{q+1} - h_q \right) \right\} \, \mathbbm{1}_{q < \overline{q}} \\
&+ \left( \varepsilon^+ \lambda^+ - \varepsilon^- \lambda^- \right) q \,,\n\end{split} \tag{10.26}$$

subject to  $h(T,q) = -\alpha q^2$  which allows us to solve for the optimal controls in feedback form:

$$\delta^{+,*}(t,q) = \frac{1}{\kappa^{+}} + \varepsilon^{+} - h(t,q-1) + h(t,q), \quad q \neq \underline{q}, \qquad (10.27a)$$

$$\delta^{-,*}(t,q) = \frac{1}{\kappa^{-}} + \varepsilon^{-} - h(t,q+1) + h(t,q), \quad q \neq \overline{q}. \tag{10.27b}$$

The interpretation of the optimal controls in feedback form is very similar to what was discussed above. The main difference is that here MOs impact the

midprice and this affects the optimal controls in two ways: one is explicitly shown in (10.27) in the form of  $\varepsilon^{\pm}$ , and the other is encoded in the solution of  $h(t, q)$ .

It is clear that the MM incorporates the impact of MOs by including the expectation of the jump in prices, conditional on an MO arriving, by posting LOs which are  $\varepsilon^{\pm} = \mathbb{E}[\varepsilon^{\pm}]$  further away from the midprice. In this way the MM trader recovers, on average, the losses she incurs due to adverse selection.

Moreover, note that the effects of the jumps in the midprice also feed into the solution of  $h(t,q)$  because the optimal strategy must take into account the future arrival of MOs, as these move the prices. Thus, it is important to note that the optimal controls derived here are not the controls as given in  $(10.8)$  plus the recovery of the average losses  $\varepsilon^{\pm}$  adverse selection costs. This becomes clear when looking at the solution of the DPE which we discuss in the next subsection.

## Solving the DPE

If  $\kappa^+ = \kappa^- = \kappa$ , then write

$$h(t,q) = -\frac{1}{\kappa} \log \omega(t,q) \,,$$

and stack  $\omega(t,q)$  into a vector

$$\boldsymbol{\omega}(t) = \left[\omega(t,\overline{q}), \, \omega(t,\overline{q}-1), \dots, \, \omega(t,\underline{q})\right]' \, .$$

Furthermore, let **A** denote the  $(\overline{q} - q + 1)$ -square matrix whose rows are labelled from  $\overline{q}$  to q and whose entries are given by

$$\mathbf{A}_{i,q} = \begin{cases} q\,\kappa\left(\varepsilon^{+}\,\lambda^{+} - \varepsilon^{-}\,\lambda^{-}\right) - \phi\kappa\,q^{2}\,, & i = q\,,\\ \tilde{\lambda}^{+}\,, & i = q-1\,,\\ \tilde{\lambda}^{-}\,, & i = q+1\,,\\ 0, & \text{otherwise}\,, \end{cases} \tag{10.28}$$

where  $\tilde{\lambda}^{\pm} = \lambda^{\pm} e^{-1-\kappa \varepsilon^{\pm}}$ . Then, on substituting *h* in terms of  $\omega$  in (10.26), we find that

$$\partial_t \boldsymbol{\omega}(t) + \boldsymbol{A} \, \boldsymbol{\omega}(t) = \boldsymbol{0}$$
 .

This matrix ODE can be easily solved to find

$$\boldsymbol{\omega}(t) = e^{\mathbf{A}(T-t)}\mathbf{z}\,,\t(10.29)$$

where **z** is a  $(\overline{q} - \underline{q} + 1)$ -dim vector where each component is  $z_j = e^{-\alpha \kappa j^2}$ ,  $j = \overline{q}, \ldots, q$ . Note that this solution is similar to the one derived above in Section  $10.2$  but here we have the impact of the MOs on the midprice dynamics.

As a direct consequence of assuming that the shape of the LOB is symmetric, as well as assuming that the rate and impact on midprice of arrival of MOs is the same  $(\kappa^{\pm} = \kappa, \lambda^{\pm} = \lambda, \varepsilon^{\pm} = \varepsilon)$ , the MM's optimal depths on the buy side with q shares equals the optimal depth on the sell side with  $-q$  shares,  $\delta^{\pm *}(t,q) = \delta^{\mp *}(t,-q).$ 

![](_page_19_Figure_1.jpeg)

Figure 10.8 The optimal depths as a function of time for various inventory levels and  $T=30.$  The remaining model parameters are:  $\lambda^{\pm}=1, \ \kappa^{\pm}=100, \ \overline{q}=-q=3,$  $\phi = 0.02, \ \alpha = 0.0001, \ \sigma = 0.01, \ S_0 = 100, \ \varepsilon = 0.005.$ 

## The Behaviour of the Strategy

In this section we illustrate several aspects of the behaviour of the optimal strategy as a function of  $q$ ,  $\phi$ ,  $\alpha$ ,  $\lambda^{\pm}$ ,  $\overline{q}$ , and  $-q$ . In Figure 10.8 we show the optimal sell and buy depths when  $T = 30$ ,  $\lambda^{\pm} = 1$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 3$ ,  $\phi = 0.02$ ,  $\alpha = 0.0001, \sigma = 0.01, S_0 = 100, \text{ and } \varepsilon = 0.005.$  The figure shows that when  $q = 0$  the optimal buy and sell depths are the same, but when the inventory is  $q \neq 0$  the optimal depths are asymmetric (sell depth is different from buy depth) and the fill rates are tilted to induce mean reversion in inventories. For instance, if  $q = 2$  the optimal sell depth is lower than the optimal buy depth so that it is more likely for the strategy to sell one unit of the asset than to acquire a unit.

The top panel in Figure 10.9 illustrates further how the fill rates are tilted to induce mean reversion to the optimal level of inventory for different levels of the running inventory parameter  $\phi = \{0.2, 0.1, 0.05\}$ . The other model parameters are:  $\lambda^+ = 2$ ,  $\lambda^- = 1$ ,  $\varepsilon = 0.005$ ,  $\kappa^{\pm} = 100$ ,  $\overline{q} = -q = 10$ ,  $\alpha = 0.0001$ ,  $\sigma = 0.01$ ,  $S_0 = 100$ . The two bottom panels show that the optimal level of inventory for this choice of parameters is to hold a positive amount of shares - this optimal point is located where the inventory drift is zero because this is the level at which the strategy 'pulls' inventories.

We discuss in detail the trajectory of inventories when  $\phi = 0.05$  which is depicted by the red circles. For example, if  $\phi = 0.05$  and the current level of inventory is  $q = 4$ , the strategy posts asymmetrically so that the buy LO is closer to the midprice than the sell LO. In this way it is more likely for inventory to increase (positive inventory drift). Similarly, if the current level of inventory is  $q = 6$  the optimal strategy is to post sell LOs closer to the midprice than the buy LOs so that it is more likely that inventory will be reduced (negative inventory drift). The optimal level of inventory is when  $q = 5$  where LOs are symmetrically posted around the midprice (buy and sell fill rates are the same). If we follow the same line of reasoning, we see that for  $\phi = 0.1$ , depicted by green circles, the

![](_page_20_Figure_1.jpeg)

optimal level of inventory is between 2 and 3 units of the asset; and for  $\phi = 0.2$ , depicted by blue circles, the optimal level of inventory is approximately 1 unit of the asset.

To further understand these results, it is important to note that the optimal level of inventory is positive because the intensity of the arrival of buy MOs is  $\lambda^+=2$  whilst the intensity of the arrival of sell MOs is  $\lambda^-=1$ . Thus, on average, the midprice is drifting up because every time an MO arrives the midprice undergoes a jump (the distribution of the jumps up and down is the same), but since buy MOs arrive twice as often as sell MOs, the midprice is drifting upward – see the midprice dynamics  $(10.22)$ . Therefore, it is optimal for the strategy to post LOs so that the fill rates are tilted in favour of holding positive inventory because it appreciates on average due to the midprice's upward trend.

#### 10.4.2 Short-Term-Alpha and Adverse Selection

In this section we assume that the midprice of the asset follows

$$dS_t = (\upsilon + \alpha_t) dt + \sigma dW_t, \qquad (10.30)$$

where the drift is given by a long-term component  $\upsilon$  and by a short-term component  $\alpha_t$  which is a predictable zero-mean reverting process. Here the longand short-term components are important when devising market making strategies. For example, if the agent is an MM who trades at time scales where she

does not 'see' the short-term component  $\alpha_t$ , then her strategy will not only be sub-optimal, but will lose money to better informed traders – traders who are better informed will pick-off the LOs posted by the less informed MM. On the other hand, if the MM has the ability to observe  $\alpha_t$  then she will ensure that on average her strategy does not lose money to other traders, and will also use this knowledge to execute more speculative trades when  $\alpha_t$  is different from zero as we shall show below.

One can specify the dynamics of the predictable drift  $\alpha_t$  in many ways, depending on the factors that affect the short-term drift of the midprice. Here we assume that the MM is operating at high-frequency and short-term-alpha is driven by order flow. Thus, we model  $\alpha_t$  as a zero-mean-reverting process which jumps by a random amount at the arrival times of MOs. The short-term drift jumps up when buy MOs arrive and jumps down when sell MOs arrive. As such,  $\alpha_t$  satisfies

$$d\alpha_t = -\zeta \,\alpha_t \,dt + \eta \,dW_t^{\alpha} + \epsilon_{1+M_{t-}^+}^+ \,dM_t^+ - \epsilon_{1+M_{t-}^-}^- \,dM_t^-\,,\tag{10.31}$$

where  $\{\epsilon_1^{\pm}, \epsilon_2^{\pm}, \dots\}$  are i.i.d. random variables (independent of all processes) representing the size of the sell/buy MO impact on the drift of the midprice. Moreover,  $W_t^{\alpha}$  denotes a Brownian motion independent of all other processes,  $\zeta$ ,  $\eta$  are positive constants, and the MOs arrive at an independent constant rate of  $\lambda^{\pm}$ .

Now we pose the market making problem where the MM posts only at-thetouch, as we did in Section  $10.2.2$ . However, here the agent's strategy accounts for the influence of short-term-alpha. To this end, let  $\ell_t^{\pm} \in \{0, 1\}$  denote whether she is posted on the sell side  $(+)$  or buy side  $(-)$  of the LOB. Her performance criteria is as usual

$$H^{\ell}(t,x,S,\alpha,q) = \mathbb{E}_{t,x,S,\alpha,q} \left[ X_T^{\ell} + Q_T^{\ell} \left( S_T - \left( \frac{\Delta}{2} + \varphi \, Q_T^{\ell} \right) \right) - \phi \! \! \int_t^T \! \! \left( Q_u^{\ell} \right)^2 du \right],$$

and her cash process  $X_t^{\ell}$  satisfies the SDE

$$dX_t^{\ell} = \left(S_t + \frac{\Delta}{2}\right) dN_t^{+,\ell} - \left(S_t - \frac{\Delta}{2}\right) dN_t^{-,\ell},$$

where  $N_t^{\pm,\ell}$  denote the counting processes for her filled LOs. We further assume that, if she is posted in the LOB, when a matching MO arrives her LO is filled with probability one. In this case,  $N_t^{\pm,\ell}$  are controlled doubly stochastic Poisson processes with intensity  $\ell_t^{\pm} \lambda^{\pm}$ . (In Exercise E.10.2 we ask the reader to generalise the problem to account for a fill probability less than 1.)

As before, the set  $\mathcal{A}$  of admissible strategies are  $\mathcal{F}$ -predictable such that the agent is not posted on the buy (sell) side if her inventory is equal to the upper (lower) inventory constraints  $\overline{q}$  (q) and her value function is denoted by

$$H(t, x, S, \alpha, q) = \sup_{\ell \in \mathcal{A}} H^{\ell}(t, x, S, \alpha, q).$$

# **The Resulting DPE**

Applying the DPP we find that the agent's value function *H* should satisfy the DPE

$$0 = \left(\partial_{t} + \alpha \,\partial_{S} + \frac{1}{2}\sigma^{2}\partial_{SS} - \zeta \,\alpha\partial_{\alpha} + \frac{1}{2}\eta^{2}\partial_{\alpha\alpha}\right)H - \phi\,q^{2}$$
  
$$+ \lambda^{+} \max_{\ell^{+}\in\{0,1\}} \left\{ \mathbbm{1}_{q \geq \underline{q}} \mathbb{E}\left[H\left(t, x + \left(S + \frac{\Delta}{2}\,\ell^{+}\right)\,\ell^{+}, S, \alpha + \epsilon^{+}, q - \ell^{+}\right) - H\right] \right\}$$
  
$$+ \left(1 - \ell^{+}\,\mathbbm{1}_{q \geq \underline{q}}\right) \mathbb{E}\left[H\left(t, x, S, \alpha + \epsilon^{+}, q\right) - H\right] \right\}$$
  
$$+ \lambda^{-} \max_{\ell^{-}\in\{0,1\}} \left\{ \mathbbm{1}_{q < \overline{q}} \mathbb{E}\left[H\left(t, x - \left(S - \frac{\Delta}{2}\,\ell^{-}\right)\,\ell^{-}, S, \alpha - \epsilon^{-}, q + \ell^{-}\right) - H\right] \right\}$$
  
$$+ \left(1 - \ell^{-}\,\mathbbm{1}_{q < \overline{q}}\right) \mathbb{E}\left[H\left(t, x, S, \alpha - \epsilon^{-}, q + \ell^{-}\right) - H\right] \right\},$$

subject to the terminal condition

$$H(T, x, S, \alpha, q) = x + q \left( S - \left( \frac{\Delta}{2} + \varphi q \right) \right) .$$

Here, the expectations are over the random jump sizes E <sup>±</sup>. The various terms in the DPE carry the following interpretations:

- e the first line in the DPE represents the drift and diffusive components of the midprice and the short-term-alpha, as well as the alpha's mean-reverting feature,
- <sup>111</sup>the maximisation terms represent the agent's control whether to post an LO at-the-touch,
- @ the second line represents the change in value function, if the agent is posted, due to the arrival of an MO which lifts the agent's offer and simultaneously induces a jump in the short-term-alpha,
- @ the third line represents the change in the value function when an MO arrives, but the agent is not posted - in which case only the short-term-alpha jumps,
- e the fourth and fifth lines are for the other side of the book.

The terminal condition once again suggests the ansatz which splits out the accumulated cash, the book value of the shares which are marked-to-market at the midprice, and the added value from making markets optimally:

$$H(t, x, S, \alpha, q) = x + q S + h(t, \alpha, q).$$

In this context,  $h$  depends on time, inventory, and the short-term-alpha. Substituting the ansatz into the above DPE we find that  $h$  satisfies

$$0 = \left(\partial_{t} - \zeta \alpha \partial_{\alpha} + \frac{1}{2} \eta^{2} \partial_{\alpha \alpha}\right) h + \alpha q - \phi q^{2}$$
  
+  $\lambda^{+} \max_{\ell^{+} \in \{0,1\}} \left\{ \mathbbm{1}_{q > \underline{q}} \mathbb{E} \left[ \ell^{+} \frac{\Delta}{2} + h(t, \alpha + \epsilon^{+}, q - \ell^{+}) - h(t, \alpha + \epsilon^{+}, q) \right] \right\}$   
+  $\lambda^{-} \max_{\ell^{-} \in \{0,1\}} \left\{ \mathbbm{1}_{q < \overline{q}} \mathbb{E} \left[ \ell^{-} \frac{\Delta}{2} + h(t, \alpha - \epsilon^{-}, q + \ell^{-}) - h(t, \alpha - \epsilon^{-}, q) \right] \right\}$   
+  $\lambda^{+} \mathbb{E} \left[ h(t, \alpha + \epsilon^{+}, q) - h(t, \alpha, q) \right]$   
+  $\lambda^{-} \mathbb{E} \left[ h(t, \alpha - \epsilon^{-}, q) - h(t, \alpha, q) \right] ,$ 

subject to the terminal condition

$$h(T, \alpha, q) = -q \left(\frac{\Delta}{2} + \varphi q\right) .$$

The term  $\alpha q$  which appears in the first line of the above equation is responsible for making the solution to this problem explicitly dependent on  $\alpha$ . If it were absent, then the optimal postings and h function would be independent of  $\alpha$ , since the terminal conditions do not depend on  $\alpha$  and there would be no source terms in  $\alpha$ . However, it is precisely this dependence on  $\alpha$  which renders the strategy interesting and allows it to adapt to the adverse selection induced by the arrival of order flow. Finally, the expectation operator  $\mathbb{E}$  is with respect to the random jump size  $\epsilon$ .

The form of the optimising terms allows us to characterise the optimal postings in a compact form. When  $\ell = 0$  both terms that are being maximised are zero, hence, the optimal postings of the agent can be characterised succinctly as

$$\ell^{+,*}(t,q) = \mathbb{1}_{\left\{\frac{\Delta}{2} + \mathbb{E}\left[h(t,\alpha+\epsilon^{+},q-1) - h(t,\alpha+\epsilon^{+},q)\right] > 0\right\} \cap \left\{q > \underline{q}\right\}},$$

$$\ell^{-,*}(t,q) = \mathbb{1}_{\left\{\frac{\Delta}{2} + \mathbb{E}\left[h(t,\alpha-\epsilon^{-},q+1) - h(t,\alpha-\epsilon^{-},q)\right] > 0\right\} \cap \left\{q < \overline{q}\right\}}.$$

$$(10.32)$$

These postings are the analog of the optimal postings in  $(10.17)$  from subsection  $10.2.2$  where we investigated how the agent trades when posting only at-thetouch. The key difference here is that the agent knows that when an MO arrives,  $\alpha$  jumps up/down and therefore she compares the expected change in the value functions evaluated at  $\alpha \pm \epsilon^{\pm}$ , rather than at  $\alpha$ , with the half-spread.

# Features of the Strategy

For the purpose of focusing solely on the effect of short-term-alpha, we set the running penalty  $\phi = 0$ , and the remaining model parameters are

$$T = 60 \text{ sec}, \quad \overline{q} = -\underline{q} = 20, \quad \lambda^{\pm} = 0.8333, \quad \Delta = 0.01, \quad \varphi = 0.01,$$
  
 $\eta = 0.001, \quad \zeta = 0.5, \quad \mathbb{E}[\epsilon] = 0.005.$ 

![](_page_24_Figure_1.jpeg)

Figure 10.10 The optimal postings when accounting for short-term-alpha.

![](_page_24_Figure_3.jpeg)

The choice of  $\lambda^{\pm}$  ensures that the agent has a maximum inventory equal to  $20\%$  of the expected number of trades. With these parameters, Figure 10.10 shows how the optimal strategy behaves as a function of time and short-termalpha. The agent posts limit buys whenever her inventory is below the surface in the left panel, and she posts limit sells whenever her inventory is above the surface in the right panel. There are a number of notable features here.

- (i) Due to the symmetry of rates of arrival of MOs, the surfaces are mirror reflections of one another.
- (ii) As maturity approaches her strategy becomes essentially independent of shortterm-alpha, and instead induces her to sell when her inventory is positive and buy when inventory is negative. Therefore, the optimal strategy attempts to close the trading period with zero inventory.
- (iii) The optimal strategies become independent of time far from maturity.
- (iv) Far from maturity, the agent tends to post symmetrically when short-termalpha and inventory are close to zero. As  $\alpha$  increases, she is willing to take on inventory, but keeps posting on both sides, until  $\alpha$  becomes quite large, then she posts only buy LOs. The opposite holds when  $\alpha$  decreases.

Next, Figure 10.11 shows a sample path of the agent's posts together with the short-term-alpha. In the left panel, the green lines demonstrate when (and at

![](_page_25_Figure_1.jpeg)

Figure 10.11 Sample path of the optimal strategy. Green lines show when and at what price the agent is posted. Solid red circles indicate MOs that arrive and hit/lift the posted bid/offers. Open red circles indicate MOs that arrive but do not hit/lift the agent's posts. Shaded region is the bid-ask spread.

what price) she is posted, and the solid red circles indicate arrival of MOs that fill the agent's posts. In this sample path, her postings change a total of five times and her inventory begins at zero  $(Q = 0)$ . In regime A she is posted only on the buy side since  $\alpha$  is large enough to suggest that purchasing the asset is worthwhile. As time evolves and she enters regime  $B$ ,  $\alpha$  decays and she begins to post symmetrically. A buy MO arrives and lifts her offer (so that  $Q_t = -1$ ), short-term-alpha immediately jumps upwards and she removes her sell LO in regime C. A sell MO eventually arrives and hits her bid (so that  $Q_t = 0$ ) and immediately induces a downward jump in  $\alpha$ . Since  $\alpha$  in regime D is relatively small, and her inventory is zero, she posts symmetrically once again. Eventually a buy MO once again lifts her offer (so that  $Q_t = -1$ ) and induces an upward jump in  $\alpha$ . In regime E she now only posts on the buy side. A sequence of buy MOs arrive in this interval inducing more upward jumps in short-term-alpha; however, since she has no LO sell posted, her inventory remains one short and she remains posted only on the buy side.

#### $10.5$ Bibliography and Selected Readings

Ho & Stoll (1981), Avellaneda & Stoikov (2008), Stoikov & Sağlam (2009), Laruelle, Lehalle & Pagès (2013), Cartea & Jaimungal (2013), Cartea, Donnelly & Jaimungal (2013), Guéant, Lehalle & Fernandez-Tapia (2013), Jaimungal & Kinzebulatov (2013), Cartea, Jaimungal & Ricci (2014), Kharroubi & Pham (2010), Guilbaud & Pham (2013), Bouchard, Dang & Lehalle (2011), Carmona & Webster (2012), Carmona & Webster (2013).

#### **10.6 Exercises**

- E.10.l Consider the framework developed in subsection 10.2.2, where the MM posts only at-the-touch, but assume that when an MO arrives, and the agent is posted on the matching side of the LOB, her order is filled with probability *p* < l. Derive the DPE and compute the optimal strategy in feedback form. Also, implement the resulting non-linear coupled system of ODEs and show how the strategy is altered by the fill probability.
- E.10.2 Consider the framework developed in subsection 10.4.2, where the MM is subject to adverse selection from active traders, but assume that when an MO arrives, and the agent is posted on the matching side of the LOB, her order is filled with probability p < l. Derive the DPE and compute the optimal strategy in feedback form. Also, implement the resulting non-linear coupled system of ODEs and show how the strategy is altered by the fill probability.
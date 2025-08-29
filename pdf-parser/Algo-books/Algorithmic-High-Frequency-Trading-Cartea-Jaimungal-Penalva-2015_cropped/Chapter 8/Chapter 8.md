### **8.1 Introduction**

In the previous two chapters we focused on execution strategies which relied on market orders (MOs) only. One of the advantages of sending MOs is that execution is guaranteed. The execution price, however, is generally worse than the midprice due to both the existence of non-zero spread and the fact that orders may walk the book. In practice, the agent also employs limit orders (LOs) because instead of picking up liquidity-taking fees and incurring market impact costs, the prices at which LOs are filled are better than the midprice, but there is no guarantee that a matching order will arrive.

To address these issues, this chapter looks at optimal execution problems when the agent employs LOs and possibly also MOs. In Sections 8.2 and 8.3, the agent is only allowed to use LOs. In Section 8.4, the agent is allowed to trade with both LOs and MOs, and in Section 8.5, the agent aims to track a given schedule using LOs and MOs.

In all cases, when the agent posts LOs to liquidate a position, she posts a limit sell order for a fixed volume (e.g., some percentage of the average size of an MO, or a fixed amount of, say, 10 shares) at a price of S<sup>t</sup> + Ot, where St is the mid price. Hence, o is a premium the agent demands for providing liquidity to the market. The larger *o,* the larger the premium, but the probability that an order arrives and walks the limit order book (LOB), up to the posted depth, decreases with o. The strategy used by the agent relies on speed to post-and-cancel LOs. At every instant in time: the agent reassesses market conditions, cancels any LO resting in the book, posts a new LO at the optimal level, and so on. To do this, requires software, hardware, and connection to the exchange so that the strategy does not have stale quotes in the LOB and can quickly process information.

The probability of being filled when posting at a given depth *o,* conditional on the arrival of an MO, is called the **fill probability** which we denote by the function *P(o).* Naturally, *P* must be decreasing, it changes throughout the day, and it is sensitive to the current status of the LOB. To see this, consider the left panel of Figure 8.1 which shows a block-shaped LOB together with (i) a post at o = 10 (the dashed line); (ii) the depth to which an MO of volume 700 lifts sell orders (dark green region); and (iii) the depth to which an MO of volume 1,500 lifts sell LOs (dark plus light green region). The deeper the LO is posted (i.e.

![](_page_1_Figure_1.jpeg)

Figure 8.1 (Left) A flat (or block shaped) LOB. (Right) Empirical fill probabilities for NFLX on June 21, 2011 for the time interval 12:55pm to 1:00pm using 500 millisecond resting times. The straight line shows the fit to an exponential function.

further away from the midprice), the less likely it is that MOs large enough walk the LOB up to that price level. Hence, the probability of being filled decreases as  $\delta$  increases.

If we assume that the volume of individual MOs, denoted by  $V$ , is exponentially distributed with mean volume of  $\eta$ , and that the LOB is block shaped with height A, i.e. the posted volume at a price of  $S + \delta$  is equal to a constant A out to a maximum price level of  $S + \overline{\delta}$ , then the probability of fill is exponential. That is, conditional on the arrival of an MO of volume  $V$ , the probability that the sell LO is lifted is given by

$$\mathbb{P}(\text{order posted at depth } \delta \text{ is lifted}) = \mathbb{P}(V > A\delta) = \exp\left\{-\frac{A}{\eta}\,\delta\right\}. \tag{8.1}$$

One could in principle also use power law fill probabilities; however, to keep the analysis consistent and self-contained we use the exponential fill probability throughout.

#### 8.2 Liquidation with Only Limit Orders

Chapters  $6$  and  $7$  looked at the optimal execution problem for an agent who places only MOs. In this section, the agent posts only LOs and the setup of the problem is similar to that in Chapter 6. Now we must track not only the agent's inventory, but also the arrival of other traders' MOs, which is what will (possibly) lift the agent's posted sell LOs. We summarise the model ingredients and the notation here:

- $\mathfrak{N}$  is the amount of shares that the agent wishes to liquidate,
- $\bullet$  T is the terminal time at which the liquidation programme ends,
- $S = (S_t)_{0 \le t \le T}$  is the asset's midprice with  $S_t = S_0 + \sigma W_t$ ,  $\sigma > 0$ , and  $W = (\overline{W_t})_{0 \le t \le T}$  is a standard Brownian motion,

- e 5 = (5)o<t<T denotes the depth at which the agent posts limit sell orders, i.e. the agent posts LOs at a price of S<sup>t</sup> + 6t at time *t,*
- e M = (Mt)o<t<T denotes a Poisson process (with intensity >-) corresponding to the number of market buy orders (from other traders) that have arrived,
- @ N° = (Nf)o<t<T denotes the (controlled) counting process corresponding to the number of market buy orders which lift the agent's offer, i.e. MOs which walk the sell side of the book to a price greater than or equal to St + 6t,
- <sup>e</sup>*P(* 5) = e-"<sup>0</sup>with "' > 0 is the probability that the agent's LO will be lifted when a buy MO arrives,
- @ X<sup>0</sup>= (Xf)<sup>o</sup> �t�T is the agent's cash process and satisfies the SDE

$$dX_t^{\delta} = (S_t + \delta_t) dN_t^{\delta}, \qquad (8.2)$$

@ Qf = SJt - *Nf* is the agent's inventory which remains to be liquidated.

Note that whenever the process *N* jumps, the process *M* must also jump, but when *M* jumps, *N* will jump only if the MO is large enough to walk the book and lift the agent's posted LO. Moreover, conditional on an MO arriving (i.e. *}YI* jumps), N jumps with probability P(5t) = e-" *<sup>0</sup> ';* however N is not a Poisson process since its activity reacts to the depth at which the agent posts. Moreover, in contrast to the setup in Chapters 6 and 7, here, when the agent's orders are executed, she receives better than midprices.

Finally, the filtration *F* on which the problem is setup is the natural one generated by S, N and NI. Moreover, the agent's depth postings (or strategy) 5 will be F-predictable and in particular will be left-continuous with right limits.

## The Agent's Optimisation Problem

The agent wishes to maximise the profit from liquidating 5)1 shares, but also requires that most, if not all, of the shares are sold by the terminal time *T.* If the agent has inventory remaining at the end of the trading horizon, she liquidates it using an MO for which she obtains worse prices than the midprice. As argued in Chapter 6, a linear impact function on MOs is a reasonable first order approximation of market impact, hence the agent's optimisation problem is to find

$$H(x,S) = \sup_{\delta \in \mathcal{A}} \mathbb{E} \left[ X_{\tau}^{\delta} + Q_{\tau}^{\delta} \left( S_{\tau} - \alpha Q_{\tau}^{\delta} \right) \mid X_{0^{-}}^{\delta} = x, \, S_{0} = S, Q_{0^{-}}^{\delta} = \mathfrak{N} \right], \tag{8.3}$$

where a 2:: 0 is the liquidation penalty (linear impact function). Moreover, the admissible set A consists of strategies 5 which are bounded from below, and the stopping time

$$\tau = T \wedge \min\{ t \, : \, Q_t^{\delta} = 0 \}$$

is the minimum of *T* or the first time that the inventory hits zero, because then no more trading is necessary.

The corresponding value function is

$$H(t,x,S,q) = \sup_{\delta \in \mathcal{A}} \mathbb{E}_{t,x,S,q} \left[ X_{\tau}^{\delta} + Q_{\tau}^{\delta} \left( S_{\tau} - \alpha Q_{\tau}^{\delta} \right) \right] , \tag{8.4}$$

where the notation  $\mathbb{E}_{t,x,S,q}[\cdot]$  represents expectation conditional on  $X_{t-}^{\delta} = x$ ,  $S_t = S$ , and  $Q_{t-}^{\delta} = q$ . In this setup, the agent does not have any urgency, i.e. does not penalise inventories different from zero as discussed in Section  $6.5$ . Indeed, one can add in such a penalty and we leave this as an exercise for the reader, see Exercise  $E.8.1$ .

## The Resulting DPE

The dynamic programming principle (DPP) suggests that the value function solves the following dynamic programming equation  $(\text{DPE})$ :

$$\begin{cases} \partial_t H + \frac{1}{2}\sigma^2 \,\partial_{SS} H \\ + \sup_{\delta} \left\{ \lambda \, e^{-\kappa \delta} \left[ H(t, x + (S+\delta), S, q-1) - H(t, x, S, q) \right] \right\} = 0, \\ H(t, x, S, 0) = x, \\ H(T, x, S, q) = x + q \left( S - \alpha \, q \right). \end{cases}$$

We have an optimal trading problem where the state variables jump and the resulting  $\text{DPE}$  results in a non-linear partial integral differential equation (PIDE) rather than a non-linear PDE. Below we elaborate on the interpretation of the various terms of the PIDE.

- (i) The operator  $\partial_{SS}$  corresponds to the generator of the Brownian motion which drives the midprice.
- (ii) The supremum takes into account the agent's ability to control the depth of her sell  $\text{LOs}$ .
- (iii) The term  $\lambda e^{-\kappa\delta}$  represents the rate of arrival of other market participants' buy MOs which lift the agent's posted sell LO at price  $S + \delta$ .
- (iv) The difference (jump) term  $H(t, x + (S + \delta), S, q 1) H(t, x, S, q)$  represents the change in the agent's value function when an MO fills the agent's  $LO$  the agent's cash increases by  $S + \delta$  and her inventory decreases by 1.

The terminal condition at  $t = T$  represents the cash the agent has acquired up to that point in time, plus the value of liquidating the remaining shares at the worse than midprice of  $(S - \alpha q)$  per share - recall that at T she must execute an MO to complete her trade and as a result walks the book. The boundary condition along  $q = 0$  represents the cash the agent has at that stopping time and since  $q = 0$  there is no liquidation value, and the agent simply walks away with  $x$  in cash.

The terminal and boundary conditions suggest that the ansatz for the value function is

$$H(t, x, S, q) = x + q S + h(t, q), \qquad (8.5)$$

for a yet to be determined function  $h(t, q)$ . This ansatz has three terms. The first term is the accumulated cash, the second term denotes the book value of the remaining inventory which is marked-to-market using the midprice, and finally the function  $h(t,q)$  represents the added value to the agent's cash from optimally liquidating the remaining shares. With this ansatz, upon substitution into the DPE above, we find that  $h(t,q)$  satisfies the coupled system of non-linear ODEs

$$\begin{cases} \partial_t h + \sup_{\delta} \left\{ \lambda e^{-\kappa \delta} \left[ \delta + h(t, q - 1) - h(t, q) \right] \right\} = 0, \\ h(t, 0) = 0, \\ h(T, q) = -\alpha q^2. \end{cases}$$
(8.6)

The optimal depth can be found in feedback form by focusing on the first order conditions for the supremum. This provides us with the following:

$$0 = \partial_{\delta} \left\{ \lambda e^{-\kappa \delta} \left[ \delta + h(t, q - 1) - h(t, q) \right] \right\}$$
  
=  $\lambda \left( -\kappa e^{-\kappa \delta} \left[ \delta + h(t, q - 1) - h(t, q) \right] + e^{-\kappa \delta} \right)$   
=  $\lambda e^{-\kappa \delta} \left( -\kappa \left[ \delta + h(t, q - 1) - h(t, q) \right] + 1 \right)$ ,

and hence the optimal strategy  $\delta^*$  in feedback control form is given by

$$\delta^*(t,q) = \frac{1}{\kappa} + [h(t,q) - h(t,q-1)]. \qquad (8.7)$$

This form for the optimal depth has an interesting interpretation. Consider the first term  $\frac{1}{\kappa}$ . It stems from optimising the instantaneous expected profits from selling one share. The profit is given by the revenue of selling one share at  $(S+\delta)$ , minus the cost S, which results in  $\delta$ . Hence, the expected profit is  $\delta P(\delta)$ , and when the fill probability is  $P(\delta) = e^{-\kappa\delta}$ , the maximum is attained at  $\delta^{\dagger} = \frac{1}{\kappa}$ , see also the discussion in  $2.1.4$ .

The difference term  $h(t,q) - h(t,q-1)$  can be viewed as the agent's correction to this static optimisation taking into account her future optimal behaviour. In particular, it represents a reservation price, which is defined as the price  $p$  such that  $H(t, x+p, S, q-1) = H(t, x, S, q)$ , i.e. it is the additional wealth the agent demands for selling the asset such that her value function remains unchanged.

We expect that  $\delta^*(t,q)$  is decreasing in q, since the more inventory the agent has, the more urgent she should be in getting rid of her holdings and hence the closer to the midprice she should post. It may be that for large enough  $q$  the optimal depth becomes negative and the solution to the control problem is no longer financially meaningful. We should instead solve the constrained problem, where  $\delta^* \geq 0$  is enforced in the set of admissible strategies. One naive approach, which avoids solving the constrained problem, is to view negative depths as an indicator that the agent should execute a market order instead of positing a limit order. The sound approach to addressing the optimal posting of LOs versus MOs is investigated later in Section  $8.4$ .

Inserting the optimal depth in feedback control form into  $(8.6)$  provides a non-linear coupled system of ODEs for  $h(t, q)$ 

$$\partial_t h + \frac{\tilde{\lambda}}{\kappa} \exp\left\{-\kappa \left[h(t,q) - h(t,q-1)\right]\right\} = 0, \qquad (8.8)$$

where  $\lambda = \lambda e^{-1}$  and the same terminal and boundary conditions as in (8.6) apply. This system of ODEs can be solved exactly by making the substitution  $h(t,q) = \frac{1}{\kappa} \log \omega(t,q)$  and writing a new equation for  $\omega(t,q)$ , in which case,

$$0 = \partial_t h + \frac{\tilde{\lambda}}{\kappa} \exp\left\{-\kappa \left[h(t,q) - h(t,q-1)\right]\right\}$$
$$= \frac{1}{\kappa} \frac{\partial_t \omega(t,q)}{\omega(t,q)} + \frac{\tilde{\lambda}}{\kappa} \frac{\omega(t,q-1)}{\omega(t,q)},$$

which implies that

$$0 = \partial_t \omega(t, q) + \lambda \omega(t, q - 1), \qquad (8.9)$$

and the terminal and boundary conditions are now

$$\omega(T,q) = e^{-\kappa \alpha q^2}$$
 and  $\omega(t,0) = 1$ ,

respectively.

## Solving the DPE

The coupled system of ODEs  $(8.9)$ , which the DPE reduces to, can be solved explicitly (see Exercise  $E.8.2$ ) resulting in the expression

$$\omega(t,q) = \sum_{n=0}^{q} \frac{\tilde{\lambda}^n}{n!} e^{-\kappa \alpha (q-n)^2} (T-t)^n.$$
 (8.10)

This solution provides the function  $h(t,q)$  which can then be substituted into the equation for the optimal depth  $(8.7)$  to find

$$\delta^{*}(t,q) = \frac{1}{\kappa} \left[ 1 + \log \frac{\sum_{n=0}^{q} \frac{\tilde{\lambda}^{n}}{n!} e^{-\kappa \alpha (q-n)^{2}} (T-t)^{n}}{\sum_{n=0}^{q-1} \frac{\tilde{\lambda}^{n}}{n!} e^{-\kappa \alpha (q-1-n)^{2}} (T-t)^{n}} \right], \qquad (8.11)$$

for  $q > 0$ . The optimal depth at which to post is a decreasing function of time for any model parameter, a decreasing function of the agent's inventory  $q$ , and increases the rate of arrival of MOs. The increasing behaviour in activity rate is intuitive since as market order arrival rates increase, the agent is willing to post deeper in the book so that her effective rate of filled LOs remains essentially constant, while reaping more profits if a matching arrives.

In Figure  $8.2$ , the optimal depths are shown as a function of time for several inventory levels as well as penalty parameter  $\alpha$ . MOs arrive at the rate of 50/min

![](_page_6_Figure_1.jpeg)

**Figure 8.2** The optimal depths  $\delta^*$  at which the agent posts LOs as a function of time and current inventory. The parameters are  $\lambda = 50/\min$ ,  $\kappa = 100$ , and  $\mathfrak{N} = 5$  with the penalty  $\alpha$  shown in each panel. The lowest depth corresponds to  $q=5$  and the highest depth to  $q=0$ .

and the agent is attempting to liquidate  $\mathfrak{N}=5$  shares – and is hence 10% of the average market volume. These plots show several interesting features of the optimal depths, as described below.

- (i) The depths are decreasing in inventory. This is natural, as if the agent's inventory is large, she is willing to accept a lower premium  $\delta$ , for providing liquidity, to increase the probability that her order is filled. At the same time, this ensures that she may complete the liquidation of the  $\mathfrak{N}$  shares by end of the time horizon and avoid crossing the spread (i.e. using MOs) and paying a terminal penalty. However, if inventories are low, the agent is willing to hold on to it in exchange for large  $\delta$ , because with low inventory the terminal penalty she picks up when crossing the spread will be moderate.
- (ii) For fixed inventory level, the depths all decrease in time. Once again, this is due to the agent becoming more averse to holding inventories as the terminal time approaches, due to the penalty they will receive from crossing the spread.
- (iii) As the penalty parameter  $\alpha$  increases, all depths decrease because increasing the penalty induces the trader to liquidate her position faster, but at lower prices. We point out that if  $\alpha$  or  $q$  is large then the optimal depths can become negative. In practice one cannot post LOs which improve the best quote on the other side of the LOB, so one may want to interpret this as the agent being very keen to get her LO filled, but here we do not allow the agent to submit  $\text{MOs}$ , we do this below in Section 8.4.
- (iv) The depths keep increasing as one moves further from the end of the trading horizon. The reason is that the agent is only being penalised by her terminal inventory, so far from terminal time, there is no incentive to liquidate her position. If the agent instead penalises inventories through time, the strategies will become asymptotically constant far from maturity. For this case, see Exercise  $E.8.4.$

Far from the terminal time, i.e. when  $\tau = T - t \gg 1$ , the ratio appearing in the logarithm above (i.e.  $\omega(t,q)/\omega(t,q-1)$ ) is to  $o((T-t)^{-1})$  given by the ratio of the two terms  $n = q - 1$  and  $n = q$  in the numerator to the term  $n = q - 1$  in the denominator. Therefore we can write

$$\frac{\omega(t,q)}{\omega(t,q-1)} = \frac{\frac{\tilde{\lambda}^{q-1}}{(q-1)!}e^{-\kappa\,\alpha\,(q-(q-1))^2}\tau^{q-1} + \frac{\tilde{\lambda}^q}{q!}e^{-\kappa\,\alpha\,(q-q)^2}\tau^q}{\frac{\tilde{\lambda}^{q-1}}{(q-1)!}e^{-\kappa\,\alpha\,(q-1-(q-1))^2}\tau^{q-1}} + o\left(\tau^{-1}\right)$$
$$= e^{-\kappa\,\alpha} + \frac{\tilde{\lambda}}{q}\tau + o\left(\tau^{-1}\right) \,.$$

Therefore, far from the terminal time, the agent posts at depths that grow logarithmically as follows:

$$\delta^*(t,q) = \frac{1}{\kappa} \left[ 1 + \log \left( e^{-\kappa \alpha} + \frac{\lambda e^{-1}}{q} \tau \right) \right] + o\left(\tau^{-1}\right) \,.$$

In this expression, the dependence of the optimal depth on the parameters becomes clear: it is increasing in activity rate and decreasing in inventory, time, fill probability and terminal penalty.

### Numerical Experiments

In this section we carry out a simulation study to explore the optimal execution strategy. Throughout we use the following parameters:

$$T = 60 \,\text{sec}, \quad \lambda = 50/\,\text{min}, \quad \kappa = 100\,\text{$}^{-1}, \quad \alpha = 0.001\,\text{$}^{\text{s}}/\text{share}, \quad \mathfrak{N} = 5,$$
  
 $S_0 = \$30.00, \quad \text{and} \quad \sigma = \$\,\text{sec}^{-1/2}\,0.01,$ 

so that the agent is trading  $10\%$  of the market over this time interval.

Figure 8.3 shows three simulated sample paths for the midprice (panel a), the optimal depth (panel b), the resulting inventory (panel c) and the average price  $\mathbf{c}$ per share (panel d) computed as  $X_t/(\mathfrak{N}-q_t)$ . In the average price per share panel, TWAP, which is given by

$$A_{TWAP} = \frac{1}{T} \int_0^T S_u \, du \,,$$

is often used as a benchmark for comparison purposes so we include it as well.

Panel (c) shows that the algorithm may sometimes acquire all assets early, e.g. along the blue and green paths, or may need to execute MOs at the end of the interval, e.g., as in the red path. When we combine this panel with panel (b), which shows the inventory path, it illustrates how immediately after the agent's LO is filled, the agent increases the posted depth, but if the agent's LO is not filled, she posts closer to the midprice. Panel (d) illustrates how the algorithm (solid lines) outperforms TWAP (dashed lines). The key reason is that the agent mostly uses LOs to achieve her goal of liquidating  $\mathfrak{N}$  shares, which provides profits in excess of the midprice. However, some paths that do not completely

![](_page_8_Figure_1.jpeg)

Figure 8.3 Three sample paths for the agent following the optimal strategy. In panel (d), the dashed line indicates the TWAP curve.

liquidate prior to maturity, such as the red one, force the agent to execute MOs at the end of the trading horizon. Doing so causes her to lose some of the premia, as measured by the depth  $\delta$ , earned by executing LOs throughout the strategy.

The left panel of Figure 8.4, which shows the histogram of the number of executed MOs over  $10,000$  scenarios, demonstrates that only a small number of paths require executing MOs at the terminal time. The right panel shows a heat-map of the agent's inventory through time for the same 10,000 scenarios. The dashed line is the mean inventory at each point in time  $-$  notice that it is almost linear and reduces to almost, but not equal to, zero at the end of the trade horizon.

To illustrate the savings provided by the algorithm, Figure 8.5 shows the histogram of the difference between the price per share from the algorithm and the TWAP over the  $10,000$  scenarios.

![](_page_9_Figure_1.jpeg)

**Figure 8.4** Left panel shows the histograms (from  $10,000$  scenarios) of executed MOs at the end of trade execution. Right panel shows a heat-map of inventory through time.

![](_page_9_Figure_3.jpeg)

Figure 8.5 Histogram of the cost savings per share relative to TWAP.

#### 8.3 Liquidation with Exponential Utility Maximiser

In the previous section the agent is indifferent to uncertainty in the value of her sales and so her objective is to maximise expected proceeds from selling  $\mathfrak{N}$  shares. A more realistic setup is one in which the agent includes a running inventory penalty. Exercise E.8.4 shows that in this case the agent's performance criteria becomes

$$G^{\delta}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ X^{\delta}_{\tau} + Q^{\delta}_{\tau}(S_{\tau} - \alpha Q_{\tau}) - \phi \int_{0}^{\tau} \left( Q^{\delta}_{s} \right)^{2} ds \right], \qquad (8.12)$$

and, compared to the case with no running inventory penalty (i.e.  $\phi = 0$ ), the optimal strategy is modified to become more aggressive (sell faster) earlier on and then less aggressive towards the end of the trading horizon. This allows her to control the distribution of the value of the total sales, as well as how fast inventory is liquidated. This is akin to the approach taken in Chapter 6, where the agents have a running inventory penalty, or urgency, constraint. Some agents, however, may instead wish to penalise uncertainty in their sales directly. Here, we show that if the agent uses exponential utility as a performance measure, her strategy is identical (up to a constant and a re-scaling of parameters) to the  $one$ implied by  $(8.12)$ .

To demonstrate this equivalence, first let us consider the agent who sets preferences based on expected utility of terminal wealth with exponential utility  $u(x) = -e^{-\gamma x}$ . In this case, her performance criteria is

$$H^{\delta}(t,x,S,q) = \mathbb{E}_{t,x,S,q} \left[ -\exp\left\{-\gamma \left(X_{\tau}^{\delta} + Q_{\tau}^{\delta}(S_{\tau} - \alpha Q_{\tau}^{\delta})\right)\right\} \right] ,$$

and proceeding as usual, her value function

$$H(t, x, S, q) = \sup_{\delta \in \mathcal{A}} H^{\delta}(t, x, S, q)$$

 $\text{should satisfy the DPE}$ 

$$\partial_t H + \frac{1}{2}\sigma^2 \partial_{SS} H$$
  
+ 
$$\sup_{\delta} \left\{ \lambda e^{-\kappa \delta} \left[ H(t, x + (S + \delta), S, q - 1) - H(t, x, S, q) \right] \right\} = 0,$$

subject to the terminal and boundary conditions

$$H(T, x, S, q) = -e^{-\gamma (x + q(S - \alpha q))}$$
 and  $H(t, x, S, 0) = -e^{-\gamma x}$ 

We leave it as an exercise for the reader to show that ansatz

$$H(t, x, S, q) = -e^{-\gamma(x+qS+h(t,q))}$$
(8.13)

leads to the following equation for  $h(t, q)$ :

$$\partial_t h - \frac{1}{2}\sigma^2 \gamma q^2 + \sup_{\delta} \lambda e^{-\kappa\delta} \frac{1 - e^{-\gamma\left[\delta + h(t, q-1) - h(t, q)\right]}}{\gamma} = 0, \tag{8.14}$$

with terminal and boundary conditions

$$h(T, q) = -\alpha q^2$$
 and  $h(t, 0) = 0$ .

The interpretation of the ansatz  $(8.13)$  is similar to that of  $(8.5)$ , in particular, the right-hand side of equation  $(8.13)$  is the utility derived from the sum of: accumulated cash, the book value of the remaining inventory which is marked-to-market using the midprice, and, finally, the function  $h(t, q)$  representing the added value to the agent's utility from optimally liquidating the remaining shares.

If one takes the limit in which  $\gamma \to 0$ , we see that h satisfies the PDE

$$\partial_t h + \sup_{\delta} \left\{ \lambda \, e^{-\kappa \delta} [\delta + h(t, q-1) - h(t, q)] \right\} = 0 \,, \tag{8.15}$$

which is precisely the equation that the excess value function  $h$  satisfied in the previous section when the agent has linear utility (see  $(8.6)$ ).

Going back to the general case  $\gamma > 0$ , we obtain, from the first order condition, the optimal depth in feedback control form as

$$\delta^* = \frac{1}{\gamma} \log\left(1 + \frac{\gamma}{\kappa}\right) + \left[h(t, q) - h(t, q - 1)\right] \,. \tag{8.16}$$

This form is very similar to, but slightly differs from, the optimal depth in the

previous section provided in  $(8.7)$ . The h functions may differ and the base line level  $\kappa^{-1}$  is modified to  $\hat{\kappa}^{-1} = \frac{1}{\gamma} \log_{\kappa} + \frac{\gamma}{\kappa}$ . This modification can be seen as a risk aversion bias. Indeed, in the limit of zero risk-aversion

$$\hat{\kappa} \xrightarrow{\gamma \downarrow 0} \kappa$$
 ,

and the result from the previous section is recovered. Furthermore, we can view the contribution  $\frac{1}{\gamma} \log \left(1 + \frac{\gamma}{\kappa}\right)$  as stemming from the agent maximising her utility, from selling at a price of  $(S + \delta)$  and immediately repurchasing at S (i.e. measuring relative to midprice):

$$\max_{\delta} \left\{ u(x+\delta) P(\delta) + u(x) \left(1 - P(\delta)\right) \right\} = \frac{1}{\gamma} \log \left(1 + \frac{\gamma}{\kappa}\right)$$

Substituting the feedback form of the optimal depth  $(8.16)$  into the DPE  $(8.14)$ , we now find the non-linear system of coupled ODEs for h to be

$$\partial_t h - \frac{1}{2}\sigma^2 \gamma q^2 + \frac{\hat{\lambda}}{\kappa} \exp\left\{-\kappa \left[h(t,q) - h(t,q-1)\right]\right\} = 0, \qquad (8.17)$$

where,

$$\hat{\lambda} = \left(\kappa/(\kappa + \gamma)\right)^{1+\kappa/\gamma} \lambda.$$

In the limit of zero risk-aversion  $\hat{\lambda} \xrightarrow{\gamma \downarrow 0} e^{-1} \lambda = \tilde{\lambda}$  and once again we recover the parameter that appears in  $(8.8)$ . The above ODE is in fact identical in structure to (8.8), except that it contains the additional term  $-\frac{1}{2}\sigma^2\gamma q^2$ . As shown in Exercise E.8.4, when the value function  $G$  for the running penalty performance criteria (8.12) is written as  $G = x + qS + q(t,q)$ , then q satisfies the system of coupled ODEs (where we write the parameters in the running penalty model with a subscript  $0$ )

$$\partial_t g - \phi q^2 + \frac{e^{-1}\lambda_0}{\kappa_0} \exp\left\{-\kappa_0 \left[g(t,q) - g(t,q-1)\right]\right\} = 0,$$

and the optimal strategy is

$$\delta_0^* = \frac{1}{\kappa_0} + g(t, q) - g(t, q - 1) \, .$$

Hence, with

$$\phi = \frac{1}{2} \sigma^2 \gamma, \quad \lambda_0 = e^{+1} \hat{\lambda}, \quad \text{and} \quad \kappa_0 = \kappa,$$

we see that the  $h(t,q)$  and  $g(t,q)$  coincide and the optimal strategies satisfy the  $relation$ 

$$\delta^* = \delta_0^* + \left(\hat{\kappa}^{-1} - \kappa_0^{-1}\right) \,. \tag{8.18}$$

In other words, with a re-scaling of model parameters, the optimal strategy for the utility maximising agent is the same, up to a constant shift, as that of the agent who only penalises running inventory – with an appropriate choice of riskaversion level and a re-scaling of arrival rates.

In addition to the relationship between the optimal strategies, the value functions can be written in terms of one another. Since  $h(t,q) = g(t,q)$ , we have

$$G(t, x, S, q) = -\frac{1}{\gamma} \log \left(-H(t, x, S, q)\right) \,$$

or writing the value function in its original control form

$$\sup_{\delta \in \mathcal{A}} \mathbb{E}^{0}_{t,x,S,q} \left[ X^{\delta}_{\tau} + Q^{\delta}_{\tau}(S_{\tau} - \alpha Q_{\tau}) - \phi \int_{0}^{\tau} (Q^{\delta}_{s})^{2} ds \right]$$
  
$$= -\frac{1}{\gamma} \log \left( -\sup_{\delta \in \mathcal{A}} \mathbb{E}_{t,x,S,q} \left[ -\exp\left\{ -\gamma \left( X^{\delta}_{\tau} + Q^{\delta}_{\tau}(S_{\tau} - \alpha Q_{\tau}) \right) \right\} \right] \right), \tag{8.19}$$

where  $\mathbb{E}^0[\cdot]$  represents expectation under a probability measure where the arrival rate is  $\lambda_0$ . This relationship between the value functions is in fact part of a more general result that relates optimisation problems with exponential utility and optimisation problems with penalties (see the further readings section).

### 8.4 Liquidation with Limit and Market Orders

In the previous two sections, the agent considers posting only LOs and, as shown, posts more aggressively (i.e. depth  $\delta$  decreases so LOs are posted nearer the midprice) as maturity approaches when her inventory is held fixed. Here, we consider the situation in which the agent is allowed to post MOs in addition to LOs. In this case, when she is far behind schedule, i.e. when maturity is approaching but she still has many shares to liquidate, then she could be willing to execute an MO in order to place her strategy back on target. In this case, the agent searches for both an optimal control and a sequence of optimal stopping times at which to execute MOs.

## The Agent's Optimisation Problem

To formalise the problem, we now need to keep track of the agent's posted MOs, in addition to other traders' MOs, and her executed LOs. Below we list the additional stochastic processes and changes to the cash process to account for executing MOs. All other stochastic processes, including the midprice  $S$ , other trader's MOs  $M$ , and the agent's filled LOs  $N$ , posted at depth  $\delta$ , remain unaltered in their definition.

- $M^a = (M^a_t)_{0 \le t \le T}$  denotes the counting process for the agent's MOs.
- The corresponding increasing sequence of stopping times at which the agent executes MOs is denoted by  $\tau = \{\tau_k : k = 1, \ldots, K\}$ , with  $K \leq \mathfrak{N}$ , so that  $M_t^a = \sum_{k=1}^K \mathbb{1}_{\tau_k \leq t}$ . Note that the agent may place fewer, but never more, than  $\mathfrak{N}$  MOs.

- I!! l denotes the half-spread, i.e. half-way distance between the best ask and best bid.
- ® X = (Xt)o<t<r denotes the agent's cash process and satisfies the SDE

$$dX_t^{\boldsymbol{\tau},\delta} = (S_t + \delta_{t^-}) dN_t^{\delta} + (S_t - \xi) dM_t^{a,\boldsymbol{\tau}}.$$

The first term on the right-hand side of the cash process denotes the cash received from having an LO lifted, and the second term is the cash received from selling a share using an MO. Note that when the agent executes a sell MO she crosses the spread, which is why the proceeds from selling one unit of the asset is the midprice minus the half-spread, i.e. the best bid. Furthermore, we assume that the size of the MOs is small enough not to walk the LOB.

We assume that the agent is averse to holding inventory throughout the strategy - unlike in Section 8.2 where she wishes to rid herself of inventory due only to the terminal penalty. To achieve this, we apply an urgency penalty to her performance criteria, much like in Section 6.5, and more specifically equation (6.20). Hence, her performance criteria is

$$H^{(\boldsymbol{\tau},\delta)}(t,x,S,q)$$
  
=  $\mathbb{E}_{t,x,S,q} \left[ X_T^{\boldsymbol{\tau},\delta} + Q_T^{\boldsymbol{\tau},\delta} S_T - \ell \left( Q_T^{\boldsymbol{\tau},\delta} \right) - \phi \int_t^T \left( Q_u^{\boldsymbol{\tau},\delta} \right)^2 du \right],$  (8.20)

where as usual Et,x,S,q[·] denotes expectation conditional on *x;\_,\_* <sup>15</sup>= x, St- = S, Q;\_,\_*<sup>15</sup>*= q, and the terminal liquidation penalty

$$\ell(q) = q\left(\xi + \alpha\,q\right).$$

The terminal liquidating cost per share of the shares remaining at the end is written as (Sr - l - a Qr) because the agent must cross the spread and then walk the LOB to liquidate the remaining shares - recall that we assumed that the MOs sent during the liquidation strategy before the terminal date did not walk the LOB. And, since the agent may execute MOs, her inventory is reduced each time an LO is filled or an MO is executed, so that

$$Q_t^{\boldsymbol{\tau},\delta} = \mathfrak{N} - N_t - M_t^a \, .$$

The set of admissible strategies A now includes seeking over all F-stopping times in addition to the set of F-predictable, bounded from below, depths 6. In this case, the value function is

$$H(t,x,S,q) = \sup_{(\tau,\delta)\in\mathcal{A}} H^{(\tau,\delta)}(t,x,S,q) \, .$$

In the following we omit the dependence on (t, x, *S, q)* when there is no confusion.

## The Resulting DPE

Now, the DPP implies that the value function should satisfy the quasi-variationalinequality (QVI), rather than the usual non-linear PDE,

$$\begin{split} 0 &= \max\Biggl\{ \partial_t H + \tfrac{1}{2} \sigma^2 \partial_{SS} H - \phi \, q^2 \\ &+ \sup_{\delta} \lambda \, e^{-\kappa \delta} \Biggl[ H(t,x+(S+\delta),S,q-1) - H(t,x,S,q) \Biggr] \\ &\qquad \Biggl[ H(t,x+(S-\xi),S,q-1) - H(t,x,S,q) \Biggr] \Biggr\} \,, \end{split}$$

with boundary and terminal conditions

$$H(t, x, S, 0) = x$$
, and  
 $H(T, x, S, q) = x + q S - \ell(q)$ .

Note that the first part of the maximisation above is identical to the previous section where we have limit orders only. The various terms in the QVI may be interpreted as described below.

- (i) The overall max operator represents the agent's choice to either post an LO (the continuation region) resulting in the first term in the max operator, or to execute an MO (the stopping region) resulting in a value function change of [H(t, *x* + *(S* -(), *S, q* -1) -*H(t, x, S,* q)] - the agent's cash increases by *S* -( and inventory decreases by 1 upon executing an MO.
- (ii) Within the continuation region where the agent posts LOs (the first term in the max):
  - (a) the operator *ass* corresponds to the generator of the Brownian motion which drives midprice,
  - (b) the term -¢ q <sup>2</sup>corresponds to the contribution of the running inventory penalty,
  - (c) the supremum over 8 takes into account the agent's ability to control the posted depth,
  - ( d) the ,\ e-K,o coefficient represents the arrival rate of MOs which fill the agents posted LO at the price *S* + *8,*
  - (e) the difference term [H(t, *x* + *(S* + 8), *S, q* -1) -*H(t, x, S,* q)] represents the change in the value function when an MO fills the agent's LO - the agent's cash increases by S + 8 and her inventory decreases by 1.

As before, the terminal and boundary conditions suggest the ansatz for the value function *H(t, x, S, q)* = *x* + *q S* + *h(t, q).* Making this substitution, we find that  $h(t,q)$  satisfies the much simplified QVI

$$\max \left\{ \partial_t h - \phi \, q^2 + \sup_{\delta} \lambda \, e^{\kappa \, \delta} \left[ \delta + h(t, q-1) - h(t, q) \right] \; ; \right. \\ \left. - \xi + h(t, q-1) - h(t, q) \right\} = 0 \,, \tag{8.22a}$$

with terminal and boundary conditions

$$h(T,q) = -\ell(q)$$
,  $q = 1, ..., \mathfrak{N}$ , and (8.22b)

$$h(t,0) = 0. \t\t(8.22c)$$

Focusing on the supremum term, through the same computations as in the LO only case leading to  $(8.7)$ , the optimal posting in feedback control form is

$$\delta^* = \frac{1}{\kappa} + [h(t,q) - h(t,q-1)] \ . \tag{8.23}$$

In this feedback control form, the optimal posting is identical to the one without MOs (see (8.7)), but the precise function  $h(t,q)$  which enters into its computation is different. The first term  $\frac{1}{\kappa}$  has the same interpretation as before: it is the optimal depth to post to maximise the expected instantaneous profit from a round-trip liquidated at midprice, i.e. the  $\delta$  that maximises  $\delta P(\delta)$  (and recall that  $P(\delta)$  is the probability of the LO being filled conditional on an MO arriving). The difference term is the correction to this static optimisation to account for the agent's ability to optimally trade.

The timing of MO executions also have a simple feedback form. From  $(8.22a)$ , we see that an MO will be executed at time  $\tau_q$  whenever

$$h(\tau_q, q-1) - h(\tau_q, q) = \xi.$$
 (8.24)

This can be interpreted as executing an MO whenever doing so increases the value function by the half-spread. Combining this observation with the feedback form for the optimal depth above, we can place a simple lower bound on  $\delta^*$  of

$$\delta^* \ge \frac{1}{\kappa} - \xi \, .$$

Thus, it is clear that if we require  $\delta > 0$ , so that the strategy never posts sell LOs below the midprice, we must require that  $\xi < \frac{1}{a}$ .

Upon substituting the optimal control in feedback form into the simplified QVI (8.22), we find that  $h(t,q)$  satisfies

$$\max\left\{\partial_{t}h - \phi q^{2} + \frac{e^{-1}\lambda}{\kappa} e^{-\kappa\left[h(t,q) - h(t,q-1)\right]}; -\xi + h(t,q-1) - h(t,q)\right\} = 0.$$
(8.25)

At maturity, the agent is forced to execute an MO and pay a cost of  $\xi + \alpha q$ per share. However, the agent may execute MOs an instant prior to maturity at a cost of  $\xi$  per share. Hence, it is never optimal to wait until T to execute an MO

to liquidate remaining inventory. As a result, the left-limit of the value function is not equal to its value at maturity, and instead we have

$$h(T^-, q) = -\xi + h(T^-, q - 1)$$

for every q > 0, so that h(T-, q) = -qt This feature of having the left-limit of the solution different from the terminal condition is sometimes referred to as *face-lifting.* 

A further reduction of the DPE can be made by using the transformation

$$h(t,q) = \frac{1}{\kappa} \log \omega(t,q) \,,$$

which, after some algebra, leads to the following coupled system of QVIs for w(t, *q):*

$$\max\left\{\partial_t\omega(t,q) - \kappa\,\phi\,q^2\omega(t,q) + \tilde{\lambda}\,\omega(t,q-1)\right.;$$
$$e^{-\kappa\xi}\,\omega(t,q-1) - \omega(t,q)\right\} = 0\,,$$

where *5-* = e-<sup>1</sup>>.. and the terminal and boundary conditions are

$$\omega(T,q) = e^{-\kappa q(\xi + \alpha q)}, \quad \text{and} \quad \omega(t,0) = 1,$$

for q = 1, ... , 5Jl.

The intuition behind the system of equations is that one first solves for w(t, 1), knowing the q = 0 condition w(t, 0) = l. The q = 1 solution then feeds into the q = 2 solution, and so on.

# Solving the **DPE**

We now illustrate how one can in principle first solve the QVI analytically and then provide a simple numerical implementation using an explicit finite-difference scheme for its solution.

## **Constructing the Analytic Solution**

The q = 1 case: Let us begin by considering q = 1, in which case (since w(t, 0) = 1) w(t, 1) satisfies the equation

$$\max\left\{\partial_t\omega(t,1) - \kappa\,\phi\,\omega(t,1) + \tilde{\lambda} \; ; \; e^{-\kappa\xi} - \omega(t,1)\right\} = 0\,,\tag{8.26a}$$

$$\omega(T,1) = e^{-\kappa(\xi+\alpha)}\,. \tag{8.26b}$$

As pointed out above, it is optimal to execute MOs for all inventories greater than zero an instant prior to maturity, and we therefore have w(T-, q) = e-q" I;\_ Next, the solution to the ODE

$$\partial_t g_1(t) - \kappa \,\phi \, g_1(t) + \lambda = 0, \qquad g_1(T^-) = e^{-\kappa \xi}$$

is given by

$$g_1(t) = e^{-\kappa\xi} e^{-\kappa\phi(T-t)} + \tilde{\lambda} \frac{1 - e^{-\kappa\phi(T-t)}}{\kappa\phi}.$$
 (8.27)

The solution to the QVI therefore has two distinct behaviours depending on the relative sizes of the parameters. First, if

$$\phi \leq \frac{\tilde{\lambda} \, e^{\kappa \xi}}{\kappa} \,,$$

then  $q_1(t) > e^{-\kappa \xi}$  for all  $t \in (0,T)$  (i.e. the continuation value is always larger than the execution value), hence, the solution to the  $QVI$  (8.26) is

$$\omega(t,1) = g_1(t) \mathbbm{1}_{t < T} + e^{-\kappa(\xi + \alpha)} \mathbbm{1}_{t = T},$$

and it is never optimal to execute an MO except for an instant prior to maturity. Moreover, during the trade horizon, the optimal LO depth (see  $(8.23)$ ) is

$$\delta^*(t,1) = \frac{1}{\kappa} + \frac{1}{\kappa} \log \left( e^{-\kappa \xi} \, e^{-\kappa \phi(T-t)} + \frac{\tilde{\lambda}}{\kappa \, \phi} \, \left( 1 - e^{-\kappa \, \phi \, (T-t)} \right) \right)$$

for  $t < T$ . In this parameter regime, the depths narrow as maturity approaches.

If on the other hand

$$\phi > \frac{\tilde{\lambda} \, e^{\kappa \xi}}{\kappa} \,,$$

then  $g(t) < e^{-\kappa\xi}$  for all  $t \in (0,T)$  (i.e. the continuation value is always less than the execution value), hence, the solution to the  $QVI$  (8.26) is

$$\omega(t,1) = e^{-\kappa\xi} \mathbbm{1}_{t < T} + e^{-\kappa(\xi + \alpha)} \mathbbm{1}_{t = T},$$

and it is always optimal to execute an MO at all points in time, i.e.  $\tau_1 = 0$ .

The financial interpretation of this result is that if the running penalty is small enough, the agent is willing to post LOs and wait all the way until maturity before executing an MO. If on the other hand, the running penalty is large enough, it is always optimal to immediately execute an MO because the agent's urgency outweighs any potential gain in waiting for the possibility of filling her posted LO.

**The**  $q = 2$  case: This case has more structure in its solution and we must solve the equation

$$\max\left\{\partial_t\omega(t,2) - 4\,\kappa\,\phi\,\omega(t,2) + \tilde{\lambda}\,\omega(t,1) \; ; \; e^{-\kappa\xi}\,\omega(t,1) - \omega(t,2)\right\} = 0 \,,$$
$$\omega(T,2) = e^{-2\kappa(\xi+2\alpha)}$$

As mentioned in the previous section, although there is an explicit terminal condition on  $\omega(t,2)$ , the optimal strategy will force the agent to execute one single MO an instant prior to maturity, so that the terminal condition is facelifted to  $\omega(T^-, 2) = e^{-\kappa \xi} \omega(T^-, 1) = e^{-2\kappa \xi}.$ 

Here we only consider the case where  $\phi < (\lambda e^{\kappa \xi})/\kappa$  so that it is optimal to post LOs when  $q = 1$ . In this case, we must determine the time  $\tau_2$  at which the solution to the QVI "peels away" from its immediate execution value of  $\omega(t,2) = e^{-\kappa\xi} \omega(t,1)$ . This point is determined by ensuring that  $\omega(t,2)$  and its derivative are continuous at that time, i.e. such that

$$\omega(\tau_2^-, 2) = \omega(\tau_2, 2), \quad \text{and} \quad \partial_t \omega(\tau_2^-, 2) = \partial_t \omega(\tau_2, 2) = e^{-\kappa \xi} \partial_t \omega(\tau_2, 1).$$

From the equation that  $\omega(t,2)$  must satisfy in the continuation region, we have

$$\begin{split} 0 &= \partial_t \omega(\tau_2, 2) - 4 \,\kappa \,\phi \,\omega(\tau_2, 2) + \lambda \,\omega(\tau_2, 1) \\ &= e^{-\kappa \xi} \,\partial_t \omega(\tau_2, 1) - 4 \,\kappa \,\phi \,e^{-\kappa \xi} \omega(\tau_2, 1) + \tilde{\lambda} \,\omega(\tau_2, 1) \\ &= e^{-\kappa \xi} \,\left(\kappa \,\phi \,\omega(\tau_2, 1) - \tilde{\lambda}\right) - 4 \,\kappa \,\phi \,e^{-\kappa \xi} \,\omega(\tau_2, 1) + \tilde{\lambda} \,\omega(\tau_2, 1) \qquad \text{(from (8.26))} \\ &= \left[ -3 \,\kappa \,\phi \,e^{-\kappa \xi} + \tilde{\lambda} \right] \omega(\tau_2, 1) - e^{-\kappa \xi} \,\tilde{\lambda} \,, \end{split}$$

where the third equality follows from  $(8.26)$ , i.e. in the continuation region for  $q = 1$  (which is  $t \in (0,T)$ ) we have  $\partial_t \omega(t,1) = \phi \omega(t,1) - \lambda$ . Hence, the optimal time at which to execute an MO when the agent has two units of inventory, solves

$$\omega(\tau_2, 1) = e^{-\kappa \xi} \tilde{\lambda} \left[ \tilde{\lambda} - 3 \kappa \phi e^{-\kappa \xi} \right]^{-1} . \tag{8.28}$$

The above can be solved explicitly for  $\tau_2$  since  $\omega(t,1) = g_1(t)$  where  $g_1(t)$  is provided in  $(8.27)$ . Alternatively, a numerical zero finder can be used.

Once again, there are two parameter regimes which have differing behaviour. First, if

$$\phi < \frac{\tilde{\lambda} \, e^{\kappa \xi}}{3 \, \kappa} \, ,$$

then a solution to  $(8.28)$  exists. Therefore, when the agent holds two units of inventory, she posts LOs in the interval  $[0, \tau_2)$  and at  $\tau_2$  immediately executes an MO. At that point in time, she will post an LO up until her order is executed, or she arrives an instant prior to maturity. Second, if on the other hand,

$$\phi \ge \frac{\tilde{\lambda} \, e^{\kappa \xi}}{3 \, \kappa}$$

no solution exists, and the agent never posts LOs and instead immediately executes an MO if holding two units of inventory.

The financial intuition for these two cases is as before: if the running penalty is too high, there is no incentive to post LOs and hope for them to be matched, rather the agent aims to liquidate her position quickly. If, on the other hand, the penalty is low enough, she will be patient and post LOs up until the critical time  $\tau_2$  is reached when she executes an MO.

In the remainder of the section, we assume that  $\phi < \left(\tilde{\lambda}e^{\kappa\xi}\right)/3\kappa$ . Given the optimal time to execute an MO, we can write the full solution for  $\omega(t,2)$  by solving the continuation equation from  $\tau_2$  backwards. For this, the solution to  $\text{the ODE}$ 

$$\partial_t g_2(t) - \kappa \phi g_2(t) + \lambda g_1(t) = 0, \qquad g_2(\tau_2) = \Upsilon,$$

where 
$$\Upsilon = e^{-\kappa\xi}\omega(\tau_2, 1) = e^{-2\kappa\xi}\tilde{\lambda}\left[\tilde{\lambda} - 3\kappa\,\phi e^{-\kappa\xi}\right]^{-1}$$
, is  

$$g_2(t) = \Upsilon\,e^{-4\phi(\tau_2 - t)} + \tilde{\lambda}\int_t^{\tau_2} e^{-4\,\phi\,(u-t)}\,g_1(u)\,du$$

$$= \Upsilon\,e^{-4\kappa\,\phi(\tau_2 - t)} + \tilde{\lambda}\left\{e^{-\kappa\xi}\frac{1 - e^{-5\kappa\,\phi(\tau_2 - t)}}{5\kappa\,\phi} + \frac{\tilde{\lambda}}{\phi}\left(\frac{1 - e^{-4\kappa\,\phi(\tau_2 - t)}}{4\kappa\,\phi} - \frac{1 - e^{-5\kappa\,\phi(\tau_2 - \tau_2)}}{5\kappa\,\phi}\right)\right\}.$$

Hence, the solution to the QVI for  $\omega(t,2)$  is

$$\omega(t,2) = g_2(t) \mathbb{1}_{t < \tau_2} + g_1(t) \mathbb{1}_{t > \tau_2}.$$

Finally, the optimal depths at which the agent posts LOs is given by

$$\delta^*(t,2) = \frac{1}{\kappa} + \frac{1}{\kappa} \log \frac{\omega(t,2)}{\omega(t,1)}.$$

The procedure outlined here can be applied recursively to obtain the optimal times at which to execute MOs for all inventory levels, as well as the optimal depths at which to post. The formulae, as one can appreciate, become rather cumbersome fairly quickly. Hence, in the next section we take a numerical approach and solve the QVIs using finite-difference methods to show different aspects of the optimal strategy.

### Numerical Experiments

Here we carry out a simple numerical implementation to compute the optimal execution strategy, including the times at which to post an MO and the depth of posted LOs. Throughout we use the following parameters:

$$T = 1 \text{ min}, \quad \mathfrak{N} = 10, \quad \lambda = 50/\text{min}, \quad \kappa = 100,$$
  
 $S_0 = \$30.00, \quad \sigma = \$0.01, \quad \xi = 0.005, \quad \text{and} \quad \alpha = 0.001.$ 

so that the agent is trading  $20\%$  of the market over this time interval. The running penalty parameter  $\phi$  will be varied to illustrate its effect on the optimal execution strategy.

Figure  $8.6$  shows the optimal depths as well as the optimal time at which the agent should execute an MO. The TWAP schedule is also shown for comparison purposes. As before, the optimal depth at which to post an LO is decreasing in inventory and time, i.e. the agent becomes more aggressive, and posts closer to the midprice, when there is more inventory to unwind or maturity approaches.

The right panels show when it is optimal to execute an MO and can be understood as follows. If the agent holds inventory at a point in time that lies to the right of a dot, then she must immediately execute an MO. Prior to this execution time, she will post LOs at the corresponding depth shown in the left panels. For example, when  $\phi = 10^{-4}$ , at the start  $t = 0$ , the agent will immediately execute

![](_page_20_Figure_1.jpeg)

Figure 8.6 The optimal execution strategy showing: (left panels) the optimal depths  $\delta^*$  at which an agent posts LOs as a function of time and current inventory; (right panels) the times at which to execute an MO if LO has not been filled.

a sequence of four MOs reducing her inventory from 10 to 6. She will then post an LO at a depth of about  $0.007$  and slowly decrease it towards  $0.005$  until either an MO arrives and lifts her order, or if she is not matched by about  $t \sim 40 \text{ sec}$ she executes an MO, dropping her inventory to 5. Her posts then jump up to

![](_page_21_Figure_1.jpeg)

Figure 8.7 Some sample paths for the agent following the optimal strategy. In the inventory path (bottom left panel) the blue dots indicate that the agent executed an MO. The dashed lines indicate the TWAP for that path. Here,  $\phi = 10^{-4}$ .

about 0.007 and she will keep decreasing it until her order is lifted, or  $t \sim 50 \text{ sec}$ at which point she would execute another MO, and so on.

To provide additional insight into the dynamical behaviour of the optimal strategy, we next perform a simulation of the trading strategy using a running penalty of  $\phi = 10^{-4}$ . Figure 8.7 shows the midprice, depth, inventory and cost per share for three simulated paths. In the inventory path (bottom left panel) the blue dots indicate when the agent executed an MO. In all scenarios, the agent immediately executes four MOs, and every time an LO is lifted or an MO is executed, the optimal depth instantly jumps upwards and then decays with time until the next LO arrives, or the agent executes an MO.

Finally, in the left panel of Figure 8.8 we show a heat-map of the agent's inventory through time as well as the mean inventory at each point in time. The agent immediately executes four MOs in all scenarios (hence the drop to  $Q_0 = 6$ ), then on average she slowly liquidates the remaining inventory by varying the depth at which she posts her LOs. In most scenarios she ends with one or zero shares just prior to the end of the trading horizon. If she has any inventory an instant prior to maturity, she executes MOs in sequence to unwind all shares before reaching the terminal date and picking up the terminal penalty as a result of walking the LOB. It is also instructive to compare the performance of the

![](_page_22_Figure_1.jpeg)

Figure 8.8 The heat-map of the optimal inventory through time and the risk-reward profile as  $\phi$  varies over  $\{5 \times 10^{-6}, 5 \times 10^{-5}, 1 \times 10^{-4}, 2.5 \times 10^{-4}, 5 \times 10^{-4}, 10^{-3}, 10^{-2}\}$ from right to left.

algorithm as the value of the running penalty  $\phi$  varies. This is shown in the right panel of Figure 8.8 which contains a risk-reward plot of the profit and loss (P&L) relative to the arrival price:  $R = X_T - Q_T(S_T - \xi - \alpha Q_T)$ . Increasing  $\phi$ has two effects: (i) it decreases the standard deviation of the revenue; and (ii) it decreases the P&L. The limiting P&L is  $-0.005$  which equals the half-spread  $\xi$ used in these experiments, and results from large penalties inducing the agent to liquidate her shares immediately by executing MOs that pick up the half-spread  $cost.$ 

#### 8.5 Liquidation with Limit and Market Orders Targeting Schedules

In the previous sections we investigated the optimal strategies followed by an agent who wishes to liquidate  $\mathfrak{N}$  shares and who penalises inventory that differs from zero by including the running inventory penalty term  $\oint_t^T (Q_u)^2 du$  in her performance criteria. As pointed out before, this penalty term can be interpreted as representing the agent's urgency in ridding herself of inventory or her aversion to holding too much inventory at any one point in time. Or put another way, the agent's execution strategy is targeting a schedule where at any point in time the strategy should be tracking an inventory schedule of zero and deviations from this target are penalised. How heavy or light the penalty will be depends on the parameter  $\phi \geq 0$ .

An agent may, however, have a particular target schedule in mind that her strategy should track as part of the liquidation programme. For example, she may be interested in liquidating shares but also in tracking the inventory schedule followed by TWAP or a schedule such as those that were solved for in a continuous trading model in Chapter 6.

Here, we illustrate how the agent can achieve that goal. To this end, let  $\mathfrak{q}_t$ denote the (deterministic) schedule she wishes to target. To account for her desire to target this schedule, we can easily extend the methodology of the previous section by replacing the penalty term

$$\phi \int_t^T \left( Q_u^{\tau,\delta} \right)^2 \, du \; \rightsquigarrow \; \phi \int_t^T \left( Q_u^{\tau,\delta} - \mathfrak{q}_u \right)^2 \, du \, .$$

Making this replacement clearly penalises strategies that deviate from the target strategy qt. Her optimal behaviour will then be modified to track this schedule, and the parameter ¢ determines how closely she matches the target schedule. It is trivial to see that if we choose to target qt = 0 for all *t,* we obtain the running inventory penalty discussed above.

We leave it as an exercise for the reader to show that making this replacement in the agent's performance criteria, but keeping the ansatz as *H(t, x, S,* q) x + *q S* + h(t, *q),* leads to the usual optimal strategy

$$\delta^* = \frac{1}{\kappa} + [h(t,q) - h(t,q-1)] \;,$$

and the optimal timing Tq of MOs solves

$$h(\tau_q, q-1) - h(\tau_q, q) = \xi$$

where h satisfies the following modification of the QVI in (8.25):

$$\max\left\{\partial_t h - \phi \left(q - \mathfrak{q}_t\right)^2 + \frac{e^{-1}\lambda}{\kappa} e^{-\kappa \left[h(t,q) - h(t,q-1)\right]} \; ; \right.$$
$$\left. -\xi + h(t,q-1) - h(t,q) \; \right\} = 0 \, ,$$

subject to the terminal and boundary conditions

$$h(T,q) = -\ell(q)$$
, and  $h(t,0) = -\phi \int_t^T q_u^2 du$ .

The QVI can be linearised as before by making the transformation

$$h(t,q) = \frac{1}{\kappa} \log \omega(t,q) \,,$$

to reveal that *w* ( *t, q)* satisfies

$$\max\left\{ \left( \partial_t - \kappa \, \phi \, (q - \mathfrak{q}_t)^2 \right) \omega(t, q) + e^{-1} \, \lambda \, \omega(t, q - 1) \; ; \right.$$
$$\left. e^{-\kappa \xi} \, \omega(t, q - 1) - \omega(t, q) \right\} = 0 \; , \qquad (8.29)$$

subject to the terminal and boundary conditions

w(T,q)=e-KC(<sup>q</sup> ), and w(t,O)=e-"'¢Jtq�du\_

## Numerical Experiments

The QVI in (8.29) can be solved analytically as outlined in the previous section. Here, however, we solve it numerically and investigate the resulting strategy. For this we use the model parameters

$$T = 60 \text{ sec}, \quad \mathfrak{N} = 10, \quad \lambda = 50/\text{min}, \quad \kappa = 100,$$
  
 $S_0 = \$30.00, \quad \sigma = \$0.01, \quad \xi = 0.005, \quad \alpha = 0.001, \quad \phi = 10^{-3}.$ 

The target schedule qt is the continuous Almgren-Chriss (AC) trading schedule with temporary and permanent impact studied in Section 6.5, see (6.30), which we repeat here for convenience in the form of a target schedule:

$$\mathfrak{q}_t = \frac{\zeta e^{\gamma(T-t)} - e^{-\gamma(T-t)}}{\zeta e^{\gamma T} - e^{-\gamma T}} \mathfrak{N},$$

where

$$\gamma = \sqrt{\frac{\phi}{k}}\n$$
 and  $\n\zeta = \frac{\alpha - \frac{1}{2}b + \sqrt{k\phi}}{\alpha - \frac{1}{2}b - \sqrt{k\phi}},$ 

and use the following parameters:

$$T = 60 \,\text{sec}, \quad \mathfrak{N} = 10, \quad k = 0.001, \quad \phi = 10^{-5}, \quad b = 0, \quad \alpha = +\infty.$$

Figure 8.9 shows (top left) the optimal depth at which the agent posts at each point in time and inventory level, ( top right) the optimal time at which to execute an MO at each inventory level, (bottom left) the heat-map from 10,000 simulations of inventory she holds through time, and (bottom right) a histogram of the number of MOs she executes during the strategy. There are several typical features seen here. First, as time evolves the LOs are posted closer to the mid price - as the agent runs out of time, she becomes more aggressive in her posts to match the given target. As before, the less inventory she holds, the deeper she posts to reap additional revenue in exchange for being relatively ahead of schedule.

Second, the times at which she executes an MO occur when her LO posts are at the lower bound o\* = ¾ - �.

Third, the optimal time to post MOs (the blue dots) follows the target schedule fairly closely when the schedule changes rapidly, but allows for some slack when the schedule is not changing rapidly. This slack can be removed by increasing the penalty ¢.

In these simulations, the agent posts on average "" 4.36 MOs during the execution, which is considerably smaller than the 1)1 = 10 inventory she wishes to liquidate. Most of these posts occur within the first 10 sec of trading, during the time when the target is changing rapidly. In the heat-map there are jumps downward at every stopping time corresponding to an MO execution. Finally, most paths lead to holding one unit up to an instant prior to maturity.

![](_page_25_Figure_1.jpeg)

Figure 8.9 The optimal depth, time at which to execute MOs, heat-map of inventory, and histogram of executed MOs for the agent who targets an AC schedule. The solid blue lines represent the target inventory. The dashed line represents the mean inventory of the strategy.

#### 8.6 Bibliography and Selected Readings

Huitema (2013), Guilbaud & Pham (2013), Cartea, Jaimungal & Kinzebulatov (2013), Guéant, Pu & Royer (2013), Guéant, Lehalle & Fernandez Tapia (2012), (Buti & Rindi 2013), Cartea & Jaimungal (2013), Horst & Naujokat (2014).

#### 8.7 Exercises

E.8.1 Use the setup provided in Section 8.2. Assume that the agent penalises running inventory so that her value function  $(8.4)$  becomes

$$H(t,x,S,q) = \sup_{\delta \in \mathcal{A}} \mathbb{E}_{t,x,S,q} \left[ X_{\tau}^{\delta} + Q_{\tau}^{\delta} \left( S_{\tau} - \alpha Q_{\tau}^{\delta} \right) - \phi \int_{t}^{\tau} \left( Q_{u}^{\delta} \right)^{2} du \right] ,$$

where  $\phi \geq 0$ . Find the optimal depth at which the agent posts the limit sell  $orders.$ 

 $E.8.2$  Show that  $(8.10)$  is indeed the solution to  $(8.9)$  by completing the steps below.

- (a) Compute *w(t, q)* for *q* = 1, 2, 3 by explicit integration of (8.9).
- (b) Notice that the solutions are all polynomials in (T *t)* which increase in order as q increases. Hence, write the ansatz

$$\omega(t,q) = \sum_{n=0}^{q} a_n^{(q)} (T-t)^n$$

and show that the coefficients a�q) satisfy the recursion

$$a_n^{(q)} = \frac{\tilde{\lambda}}{n} a_{n-1}^{(q-1)}, \qquad (8.30)$$

for n = 1, ... , *q, q* = 1, 2, ... and a�q) = e-"'"' q *2*

- ( c) Prove via induction that the above form of the solution is indeed correct.
- ( d) Solve the recursion and show that

$$a_n^{(q)} = \frac{\tilde{\lambda}^n}{n!} e^{-\kappa \alpha (q-n)^2} , \qquad (8.31)$$

for n = 0, ... , q and q = 1, 2, ....

E.8.3 In the optimisation problem (8.3), the terminal penalty is assumed to be -aq*<sup>2</sup> .*  Suppose instead that terminal penalty is a generic bounded and increasing function of the terminal inventory £(q), so that the agent's optimisation problem is

$$H(x, S) = \sup_{\delta \in \mathcal{A}} \mathbb{E}_{0, x, S, \mathfrak{N}} \left[ X_{\tau} + Q_{\tau} S_{\tau} - \ell(Q_{\tau}) \right] . \tag{8.32}$$

- (a) Derive the corresponding DPE for the associated value function, and solve for the value function and the optimal trading strategy using the same methods as outlined in Section 8.2.
- (b) Many markets provide rebates to liquidity providers. This means that each time that an agent posts an LO and it is filled before being cancelled, the agent receives a rebate *(3.* Account for such rebates in the formulation of the agent's optimisation problem and determine the modified optimal posting strategy.
- E.8.4 Suppose that the agent wishes to penalise inventories different from zero not just at the terminal time, but also throughout the entire duration of trading. In this case, the agent adds a running penalty term to the optimisation problem and wishes to optimise

$$G(x, S) = \sup_{\delta \in \mathcal{A}} \mathbb{E}_{0, x, S, \mathfrak{N}} \left[ X_{\tau} + Q_{\tau} \left( S_{\tau} - \alpha Q_{\tau} \right) - \phi \sigma^2 \int_0^{\tau} Q_s^2 ds \right] \tag{8.33}$$

instead of (8.3), with¢ 2 0. When¢= 0, the agent solves the old optimisation problem, but when ¢ > 0, the agent modifies her behaviour to reflect her risk preference towards holding inventory.

(a) Show that the corresponding value function can be written as *G(t, x, S, q)* = *x+q S+g(t, q),* where *g(t, q)* satisfies the coupled non-linear system of ODEs

$$\begin{cases} \partial_t g + \tilde{\lambda} \exp\left\{-\kappa \left[g(t,q) - g(t,q-1)\right]\right\} &= \sigma \phi q^2, \\ g(t,0) &= 0, \\ g(T,q) &= -\alpha q^2, \end{cases}$$
(8.34)

and that the optimal depth *5\** is still provided in feedback form as

$$\delta^*(t,q) = \frac{1}{\kappa} + [g(t,q) - g(t,q-1)] \ . \tag{8.35}$$

- (b) By writing *g(t,q)* = *�w(t,q),* solve for *w(t,q)* and the optimal control *5.*
- (c) Demonstrate that if¢ > 0, then limr-++oo *5\*(t, q)* is finite for each *q* and independent of current time *t.*
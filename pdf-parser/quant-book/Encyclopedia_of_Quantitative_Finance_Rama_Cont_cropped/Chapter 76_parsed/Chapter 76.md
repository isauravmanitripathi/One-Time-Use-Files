# **Utility Indifference** Valuation

Under market frictions like illiquidity or transaction costs, contingent claims can incorporate some inevitable intrinsic risk that cannot be completely hedged away but remains with the holder. In general, they cannot be synthesized by dynamical trading in liquid assets and hence cannot be priced by noarbitrage arguments alone. Still, an agent (she) can determine a valuation with respect to her preferences towards risk. The utility indifference value for a variation in the quantity of illiquid assets held by the agent is defined as the compensating variation of wealth, under which her maximal expected utility remains unchanged.

Consider an agent acting in a financial market with  $d+1$  liquid assets, which can be traded at market prices in a frictionless way anytime up to horizon  $T < \infty$ . In addition, there are J illiquid assets providing risky payouts  $(B^j)_{h=1,\ldots,J}$  at T. A preference order of the agent is described by an (indirect) utility function  $u_t^b(x)$ , describing the maximal expected utility obtainable when holding at t a position consisting of wealth  $x \in \mathbb{R}$  invested in liquid assets (at market prices) and  $b \in \mathbb{R}^J$  shares of illiquid assets. At time  $t$ , the agent prefers a position  $(x, b)$  to  $(x', b')$  if  $u_t^b(x) \ge u_t^{b'}(x')$ . She is indifferent if  $u_t^b(x) = u_t^{b'}(x')$ . The agent's *utility indifference (buy) value* for adding  $\delta$  illiquid assets to her current position  $(x, b)$  is defined as the *compensating variation*  $\pi_t^{b,x}(\delta)$  of her present wealth that leaves her utility unchanged, that is, as the solution to

$$u_t^{b+\delta}(x-\pi_t^{b,x}(\delta)) = u_t^b(x) \tag{1}$$

The indifference sell value is  $-\pi_t^{b,x}(-\delta)$ . In comparison, the *certainty equivalent* for adding  $\delta$  to her position in illiquid assets is the equivalent variation  $\mathfrak{c}_{t}^{b,x}(\delta)$  of the wealth that yields the same utility, that is, it is the solution to

$$u_t^b(x + \mathfrak{c}_t^{b,x}(\delta)) = u_t^{b+\delta}(x) \tag{2}$$

Equations  $(1)$ ,  $(2)$  have unique solutions if the functions  $x \mapsto u_t^b(x)$  are strictly increasing and have the same range for any  $b$ . The notion *compensating variation* is classical from the economic theory of demand by John Richard Hicks [7]. Alternatively, the terms indifference value ("price") and reservation price have been used frequently in recent literature. We use the terms synonymously, but note that the classical terminology appears more accurate in reflecting the definition (1): in general, the compensating variation  $\pi^{b,x}_{t}(\delta)$  is not a "price" for which  $\delta$  illiquid assets can be traded in the market. Also,  $\pi_t^{b,x}(\delta)$  is determined only at t in dependence of the position  $(x, b)$ prevailing and the variation  $\delta$  occurring at the same time  $t$ ; it should not be interpreted prematurely as a "value at  $t$ " that could be attributed at times before  $t$ to the payoff  $\delta B$  at T.

Next, we introduce the setup for a market model in which a family of utility functions  $u_t$ ,  $t \leq T$ , is to be obtained. For simplicity, we consider a finite probability space  $(\Omega, \mathcal{F}, P)$ . For time  $t \in \{0, \ldots T\}$ being discrete, the information flow is described by a filtration  $(\mathcal{F}_t)_{0 \le t \le T}$  (see **Filtrations**), that is defined by refining partitions  $\mathcal{A}_t$  of  $\Omega$  and corresponds to a nonrecombining tree (see Arrow-Debreu Prices, Figure 1). The smallest nonempty events of  $\mathcal{F}_t$  are called atoms  $A \in \mathcal{A}_t$  of  $\mathcal{F}_t$ . Take  $\mathcal{F}_0$  as trivial,  $\mathcal{F}_T = \mathcal{F} = 2^{\Omega}$  as the set of all events, and all probabilities  $P(\omega) > 0$ ,  $\omega \in \Omega$  to be positive. Random variables  $X_t$  known at time t are denoted by  $X_t \in$  $L_{\mathcal{F}_t}$ . They are determined by their values on each atom  $A \in \mathcal{A}_t$ , and can be identified with elements of a suitable  $\mathbb{R}^N$ . A process  $(X_t)_{t \leq T}$  is adapted if  $X_t \in L_{\mathcal{F}_t}$  for any t. Inequalities and properties stated for random variables and functions are meant to hold for all outcomes (coordinates). Conditional expectations with respect to  $\mathcal{F}_t$  are denoted by  $E_t[\cdot]$ . For a family  $\{X_t^a\} \subset L_{\mathcal{F}_t}(\mathbb{R})$ , the random variable ess sup<sub>a</sub>  $X_t^a$  takes the value sup<sub>a</sub>  $X_t^a(A)$  on atom  $A \in \mathcal{A}_t$ .

The price evolution of  $d$  liquidly traded risky assets is described by an  $\mathbb{R}^d$ -valued adapted process  $(S_t)_{0 \le t \le T}$ . All prices are expressed in units of a further liquid riskless asset (unit of account) whose price is constant at 1. If, for example, the unit of account is the zero-coupon bond with maturity  $T$ , all prices are expressed in  $T$ -forward units. A trading strategy  $(\vartheta_t)_{t \leq T} \in \Theta$  is described by the numbers of liquid assets  $\vartheta_t \in L_{\mathcal{F}_{t-1}}$  to be held over any period  $[t-1, t)$ . Its gains from t until T are  $\int_t^T \vartheta \, dS :=$  $\sum_{k=t+1}^{T} \vartheta_k \Delta S_k$ , with  $\Delta S_k := S_k - S_{k-1}$ . Any  $X_T \in$  $L_{\mathcal{F}_T}$  of the form  $X_T = x + \int_t^T \vartheta \, dS$  represents a

wealth at time T that is attainable from  $x \in L_{\mathcal{F}}$  at t by trading. Let  $\mathcal{X}_T(x,t)$  denote the set of all such  $X_T$ , and set  $\mathcal{X}_t(x) := \mathcal{X}_t(x, t-1)$ . In addition to the liquid assets, there exist  $J$  illiquid assets delivering payoffs  $B = (B^j)_{1 \le j \le J} \in L_{\mathcal{F}_T}(\mathbb{R}^J)$  at T. A quantity  $b \in \mathbb{R}^J$  of illiquid assets provides at T the payoff  $bB := \sum_{i} b^{j} B^{j}$ . We assume that the market is free of arbitrage in the sense that the set  $\mathcal{M}^e$  of equivalent probability measures  $O$  under which  $S$  is a martingale (see **Martingales**) is nonempty. This is equivalent to assuming that all sets  $\mathcal{D}_{s,t}$ ,  $s < t \leq T$ , of conditional state-price densities are nonempty. Technically,  $\mathcal{D}_{s,t}$  is the set of strictly positive  $D_{s,t} \in L_{\mathcal{F}_t}$  satisfying  $E_s[D_{s,t}] = 1$  and  $E_s[D_{s,t} \int_s^t \vartheta \, dS] = 0$  for all  $\vartheta \in \Theta$ . For brevity, let  $\mathcal{D}_t := \mathcal{D}_{t-1,t}$ . State-price densities are related to the likelihood density process  $Z_t = E_t [dQ/dP]$  of a  $Q \in \mathcal{M}^e$  by  $D_{s,t} = Z_t/Z_s$ .

# **Conditional Utility Functions and Dual** Problems

Our agent's objective is to maximize her expected utility (3) of wealth at  $T$  for a direct utility function  $U$ , which is finite, differentiable, strictly increasing, and concave on all of  $\mathbb{R}$ , with  $\lim_{x\to -\infty} U'(x) = \infty$ and  $\lim_{x\to\infty} U'(x) = 0$ . Holding position  $(x, b) \in$  $\mathbb{R} \times \mathbb{R}^J$  in liquid and illiquid assets at  $t \leq T$ , she maximizes

$$u_t^b(x) := \operatorname*{ess\,sup}_{X_T \in \mathcal{X}_T(x,t)} E_t \left[ U(X_T + bB) \right]$$
  
=  $\operatorname*{ess\,sup}_{X_T \in \mathcal{X}_T(x,t)} E_t \left[ u_T^b(X_T) \right]$  (3)

We call  $u_t^b(x)$  *u*-regular if (for all  $b, \omega$ ) the function  $x \mapsto u_t^b(x)$  is strictly concave, increasing, and continuously differentiable on  $\mathbb{R}$  with  $\lim_{x \to -\infty} u^{\prime b}_{t}(x) =$  $+\infty$  and  $\lim_{x\to +\infty} u^{b}(x) = 0$ . For  $t = T$ ,  $u^{b}(x) =$  $U(x + bB)$  satisfies the condition

 $u_t^b(x)$  is *u*-regular, concave, and differentiable

in 
$$(x, b)$$
, with  $u_t^b(\mathbb{R}) = U(\mathbb{R})$  (4)

with  $U(\mathbb{R}) = \{U(x) : x \in \mathbb{R}\}$  denoting the range of U. The primal problems (3) are related, see A1-3, to the dual problems

$$v_t^b(y) := \underset{D_{t,T} \in \mathcal{D}_{t,T}}{\text{ess inf}} E_t \left[ V^b(yD_{t,T}) \right], \quad y > 0 \quad (5)$$

for the conjugate function

 $V^{b}(y) := \text{ess sup}_{x} (U(x + bB) - xy)$ 

 $(y > 0, b \in \mathbb{R}^J)$ , with  $V^b(y) = V^0(y) + ybB$  and  $v_T^b(y) = V^b(y)$ . For later arguments, we assume the following:

(A1)  $u_t^b(x)$  satisfies condition (4) for any t, b, and the value functions are conjugate:

$$v_t^b(y) = \operatorname{ess\,sup}_{x \in \mathbb{R}} (u_t^b(x) - xy), \quad y > 0 \quad (6)$$

$$u_t^b(x) = \operatorname{ess\,inf}_{y>0} (v_t^b(y) + xy), \quad x \in \mathbb{R} \quad (7)$$

(A2) For any  $t \leq T$  and  $b, x, y \in L_{\mathcal{F}_{t-1}}$ , there exist unique  $\widehat{X}_{t}^{b}(x)$  and  $\widehat{D}_{t}^{b}(y)$  that attain the single-period optima  $(8)$  and  $(9)$ 

$$u_{t-1}^{b}(x) = \underset{X_{t} \in \mathcal{X}_{t}(x, t-1)}{\text{ess sup}} E_{t-1} \left[ u_{t}^{b}(X_{t}) \right]$$
  
$$= E_{t-1} \left[ u_{t}^{b}(\widehat{X}_{t}^{b}(x)) \right] \qquad (8)$$
  
$$v_{t-1}^{b}(y) = \underset{D_{t} \in \mathcal{D}_{t}}{\text{ess inf}} E_{t-1} \left[ v_{t}^{b}(yD_{t}) \right]$$
  
$$= E_{t-1} \left[ v_{t}^{b}(y\widehat{D}_{t}^{b}(y)) \right] \qquad (9)$$

and satisfy  $u^b(\widehat{X}^b_t(x)) = y\widehat{D}^b_t(y)$  for x and y being related by  $u_{t-1}^{\prime b}(x) = y$ .

(A3) For  $t \leq T$ ,  $b, x, y \in L_{\mathcal{F}_t}$ , unique optima  $\widehat{X}^b_T$ and  $\widehat{D}_{t}^{b}$  for the multiperiod problems (3), (5) are attained, and can be constructed by dynamical programming  $\widehat{X}_{k}^{b} = \widehat{X}_{k}^{b}(\widehat{X}_{k-1}^{b})$  and  $\widehat{D}_{t,k}^{b} = \widehat{D}_{t,k-1}^{b}\widehat{D}_{k}^{b}(\widehat{y}\widehat{D}_{t,k-1}^{b})$ for  $t < k \leq T$ , with  $\widehat{D}_{k}^{b}(\cdot)$  and  $\widehat{X}_{k}^{b}(\cdot)$  from A2 and  $\widehat{X}_t^b := x$  and  $\widehat{D}_{t,t}^b := 1$ . The optima satisfy  ${u'}_k^b(\widehat{X}_k^b) =$  $y\widehat{D}_{t}^{b}$ ,  $t < k \leq T$ , for x and y being related by  $u^{\prime b}_{t}(x) = y.$ 

 $\Omega$  being finite, A1-3 can be shown by convex duality; by arguments as in [21] follows inductively that A1-3 hold for  $t-1$  on each atom, given they hold at t. Also see Convex Duality and Second Fundamental Theorem of Asset Pricing. Let us just mention here that, under regularity, the transforms  $(7)$  and  $(6)$  are inversions of each other, and  $-v_t^b(y)$  is the inverse function of the marginal utility  $u_{t}^{\prime b}(x) = \frac{\partial}{\partial x}u_{t}^{b}(x).$ 

#### **Properties of Utility Indifference Values**

#### Concavity (Convexity)

By concavity of  $U$ , indifference buy (sell) values  $\pi^{b,x}_t(\delta)$  (respectively  $-\pi^{b,x}_t(-\delta)$ ) are concave (convex) with respect to the quantity  $\delta$  of illiquid assets that they compensate for, that is,

$$\lambda \pi_t^{b,x}(\delta^1) + (1 - \lambda)\pi_t^{b,x}(\delta^2)$$
  
 
$$\leq \pi_t^{b,x}(\lambda \delta^1 + (1 - \lambda)\delta^2) \quad \text{for } \lambda \in [0, 1] \tag{10}$$

### Monotonicity

Monotonicity of U implies, on any atom  $A \in \mathcal{A}_t$ , that

$$1_{A}\pi_{t}^{b,x}(\delta) \le 1_{A}\pi_{t}^{b,x}(\delta') \quad \text{if } 1_{A}\delta B \le 1_{A}\delta' B$$
  
for  $\delta, \delta' \in \mathbb{R}^{J}$  (11)

and that  $1_A \pi_t^{b,x}(\delta) = 0$  holds if  $1_A \delta B = 0$ .

#### Dynamic consistency with no arbitrage

So far, we took the agent to trade optimally in liquid assets, while holding a fixed position  $b$  in illiquid assets. Now, suppose that she is ready to buy (or sell) at her compensating variations shares of illiquid assets in quantities as requested by another agent (he), dynamically over time. Let  $\beta_t - \beta_0 \in L_{\mathcal{F}_{t-1}}(\mathbb{R}^J)$ denote the cumulative position in illiquid assets she has accepted until date  $t-1$ , when she initially has held  $\beta_0 := b \in \mathbb{R}^J$ . At  $t - 1 < T$ , he chooses to sell  $\Delta \beta_t \in L_{\mathcal{F}_{t-1}}(\mathbb{R}^J)$  illiquid assets. Given  $\widehat{X}_{t-1}$  is the wealth in liquid assets she arrived with at  $t-1$ , paying compensating variation changes her liquid wealth to  $\widetilde{X}_{t-1} := \widehat{X}_{t-1} - \pi_{t-1}^{\beta_{t-1}, \widehat{X}_{t-1}}(\Delta \beta_t)$  such that the utility of her position stays equal  $u_{t-1}^{\beta_{t-1}}(\widehat{X}_{t-1}) =$  $u_{t-1}^{\beta_t}(\widetilde{X}_{t-1})$ . Investing optimally for the next period according to A2 from her new position  $(\widetilde{X}_{t-1}, \beta_t)$ (without knowing his future  $(\beta_{t+k})_{k>1}$ ), she arrives at  $t$  with liquid wealth

$$\widehat{X}_{t} = \widehat{X}_{t}^{\beta_{t}}(\widetilde{X}_{t-1})\n$$

$$\n=:\widehat{X}_{t-1} - \pi_{t-1}^{\beta_{t-1},\widehat{X}_{t-1}}(\Delta\beta_{t}) + \int_{t-1}^{t} \widehat{\vartheta} \, \mathrm{d}S \quad (12)$$

for an optimal strategy  $\widehat{\vartheta}$  over  $(t-1, t]$ . Given an initial wealth  $\widehat{X}_0 = x \in \mathbb{R}$ , the wealth process  $\widehat{X}_t$  is determined by compensating variations and A2 such that  $(u_t^{\beta_t}(\widehat{X}_t))$  is a martingale. Trading against indifference valuations but not following strategy  $\widehat{\vartheta}$  would result in a suboptimal wealth process  $X_t$  for which the utility process  $(u_t^{\beta_t}(X_t))$ is a supermartingale, therefore decreasing in the mean. By accepting to trade illiquid assets against her indifference values, she is not offering arbitrage

opportunities to her counterparty. Indeed, a strategy  $\theta \in \Theta$  would offer arbitrage profits to him, jointly with  $(\beta_t)$ , if his gains

$$G_{T} := \int_{0}^{T} \theta \, \mathrm{d}S$$
  
+ 
$$\sum_{t=1}^{T} \pi_{t-1}^{\beta_{t-1}, \widehat{X}_{t-1}} (\Delta \beta_{t}) - (\beta_{T} - b)B$$
  
(13)

satisfy  $G_T \ge 0$  and  $P[G_T > 0]$ . Unwinding her illiquid asset position at  $T$ , leaves her with final wealth

$$\widehat{X}_{T} = x + \int_{0}^{T} \widehat{\vartheta} \, \mathrm{d}S$$
$$- \sum_{t=1}^{T} \pi_{t-1}^{\beta_{t-1}, \widehat{X}_{t-1}} (\Delta \beta_{t}) + \beta_{T} B \qquad (14)$$

Adding equation  $(13)$  to equation  $(14)$ , would im- $\text{ply } E[u_T^b(x + \int_0^T \theta + \widehat{\vartheta} \, \text{d}S)] > E[u_T^{\hat{\beta}_T}(\widehat{X}_T)] = u_0^b(x),$ contradicting definition (3).

#### Static no-arbitrage bounds

In particular, there is no arbitrage from buy(sell)-andhold strategies in illiquid assets. For  $x \in \mathbb{R}, b, \delta \in \mathbb{R}^J$ it thus holds

$$\pi_t^{b,x}(\delta) \le \operatorname*{ess\,sup}_{Q \in \mathcal{M}^e} E_t^Q[\delta B]$$
  
and 
$$-\pi_t^{b,x}(-\delta) \ge \operatorname*{ess\,inf}_{Q \in \mathcal{M}^e} E_t^Q[\delta B]$$
  
(15

For replicable payoffs  $B^j = B^j_t + \int_t^T \vartheta^{B^j} dS$  with  $\vartheta^{B^j}$  in  $\Theta$  for all  $j, B_t \in L_{\mathcal{F}_t}(\mathbb{R}^d)$  the indifference value  $\pi_t^{b,x}(\delta)$  equals the replication cost (market price)  $\delta B_t$ .

#### **Marginal indifference values**

In general,  $\pi_t^{b,x}(\delta)$  is nonlinear in  $\delta$ . Since  $\varepsilon \mapsto u_t^{b+\varepsilon\delta}(x-\pi_t^{b,x}(\varepsilon\delta))$  is constant, it holds

$$\left. \frac{\partial}{\partial \varepsilon} \pi_t^{b,x}(\varepsilon \delta) \right|_{\varepsilon=0} = \frac{\text{grad}_b u_t^b(x)}{u_t^{'b}(x)} \delta \tag{16}$$

Hence, marginal indifference values, that is, compensating variations for infinitesimal changes of quantities, are linear in  $\delta$  and given by the ratio of the gradient of  $u_t^b(x)$  with respect to b and the marginal utility of wealth  $u_{t}^{\prime b}(x)$ . The principle of valuation at ratios of marginal utilities is classical in economics, see for example [4]. Marginal indifference values can be computed from optimizers of the dual problem. They coincide with prices of an arbitrage-free dynamical price process in an enlarged market, where previously illiquid assets are tradable at "shadow" price processes, which are such that the utility maximizing agent is not trading those assets. To see this for  $t = 0$ , fix x, b. For y and  $\widehat{D}_{0,T}^b$  from A3, let  $R_k := E_k^{\mathcal{Q}}[B], k \leq T$ , for  $d\mathcal{Q} := \widehat{D}_{0,T}^b dP$ . Let  $\bar{u}_{0}^{b}(x)$ ,  $\bar{v}_{0}^{b}(y)$  be the primal and dual value functions (cf. equations (3),(5)) of the market  $\bar{S} = (S, R)$  that is enlarged by the additional price process  $R$ . The set of state-price densities for the enlarged market is smaller, but includes the minimizer for equation (5). Hence  $\bar{v}_0^b(\cdot) \ge v_0^b(\cdot)$  and  $\bar{v}_0^b(y) = v_0^b(y)$ , implying  $\bar{v}_{0}^{\prime b}(y) = v_{0}^{\prime b}(y)$  and  $\bar{u}_{0}^{b}(x) = u_{0}^{b}(x)$  by A1. Thus, the optimal strategy in the enlarged market is not trading the additional asset at the shadow price process  $(R_t)$ . The agent is, in particular, indifferent to infinitesimal initial variations of his position at shadow prices. Hence,  $R_0$  must be given by the ratio in (16) of marginal utilities at  $t = 0$ . If the agent is taken to be representative for the whole market, holding a net supply of b illiquid assets, then  $(R_t)$  could be interpreted as a partial equilibrium price process.

#### **Numeraire dependence**

In general, utility indifference values depend on the utility functions and the numeraire (unit of account) with respect to which they are defined. But it is possible to choose state-dependent utility functions with respect to another numeraire such that indifference values (and optimal strategies) become numeraire invariant. Let  $(N_t)$  be the price process of a tradable numeraire, that is,  $N_t = N_0 + \int_0^t \vartheta^N \, dS$  for  $t \leq$  $T, \ \vartheta^N \in \Theta$ , with  $N > 0$ . Then indifference values coincide, that means  $\pi_{t,N}^{b,x}(\delta) = \pi_t^{b,xN_t}(\delta)/N_t$  holds, if utilities and payoffs with respect to  $N$  satisfy the relations  $u_{t}^{b}(x) = u_{t}^{b}(xN_{t})$  (for  $t = T$ , hence all t) and  $B_N := B/N_T$ . Likewise, for numeraires  $N, \widetilde{N}$ , the relations should be  $u_{t,\widetilde{N}}^b(x) = u_{t,N}^b(x\widetilde{N}_t/N_t)$  and  $B_{\widetilde{N}} = B_N N_T / \widetilde{N}_T.$ 

## **Partial hedging**

Compensating variations can be associated with a utility-based hedging strategy, which, for an aggregate position  $(x, b)$  at  $t = 0$ , is defined as the strategy whose wealth process is  $\widehat{X}_t^b(x) - \widehat{X}_t^0(x + \mathfrak{c}_0^{0,x}(b)),$ for optimal wealth processes  $\widehat{X}^b$ ,  $\widehat{X}^0$  from A3 and  $\mathfrak{c}_{0}^{0,x}(b)$  from equation (2). The risk that remains under partial hedging can be substantial, see the example below.

## **Case of Exponential Utility**

Much of the literature on indifference pricing deals with exponential utility  $U(x) = -\frac{1}{\alpha} \exp(-\alpha x)$  of constant absolute risk aversion  $\alpha > 0$ . Because U factorizes, the utility functions are of the form  $u_t^b(x) = -\frac{1}{\alpha}e^{-\alpha(x+C_t^b)}, t \leq T$ , for random variables  $C_t^b \in L_{\mathcal{F}_t}$  not depending on  $x$ , with  $C_T^b = bB$ .<br>Clearly,  $\pi_t^{b,x}(\delta) = C_t^{b+\delta} - C_t^b$  does not depend on  $x$ , and the compensating variation (1) and the equivalent variation (2) coincide for exponential utility. From the dual value functions  $v_t^b(y) = \frac{y}{\alpha} (\log y - 1 + \alpha C_t^b)$  from equation (5), one obtains a general formula

$$\pi_t^{0,x}(\delta) = \operatorname*{ess\;inf}_{D \in \mathcal{D}_{t,T}} \left\{ E_t[D(\delta B)] + \frac{1}{\alpha} \left( E_t[D\log D] - E_t[\widehat{D}_{t,T}^0 \log \widehat{D}_{t,T}^0] \right) \right\}$$
(17)

for the indifference value  $\pi_t^{b,x}(\delta) = \pi_t^{0,x}(\delta + b)$  –  $\pi^{0,x}_t(b)$ , where  $\widehat{D}^0_{t,T}$  is the minimizer of equation (5) for  $b = 0$  that satisfies  $E_t[\widehat{D}_{t}^0 \log \widehat{D}_{t}^0] =$ ess  $\inf_{D_{t,T}} E_t[D_{t,T} \log D_{t,T}]$ . By equation (17), utility indifference sell values  $\delta B \mapsto -\pi_t^{b,x}(-\delta)$  are monotonic in  $\alpha$ , and satisfy the properties of convexity, translation invariance, and monotonicity, that constitute a convex risk measure (see **Convex Risk** Measures).

Under particular model assumptions, indifference values  $\pi_t^{0,x}(\delta)$  can be computed by a backward induction scheme

-

$$= E_{t-1}^{\mathcal{Q}^0} \left[ \frac{1}{\alpha} \log E_{\mathcal{G}_t} \left[ \exp\left( -\alpha \pi_t^{0,x}(\delta) \right) \right] \right]$$
(18)

starting from  $\pi_T^{0,x}(\delta) = \delta B$ . Roughly speaking, the assumptions needed comprise certain independence conditions plus semicompleteness of the market at each period. The scheme (18) has intuitive appeal, in showing that the indifference valuation is computed here by intertwining two well-known valuation methods: First, one takes an exponential certainty equivalent with respect to nontradable risk at the inner expectation (with  $\mathcal{F}_{t-1} \subset \mathcal{G}_t \subset \mathcal{F}_t$ ); after that one takes a risk-neutral expectation of this certainty equivalent at the outer expectation (under the **minimal entropy martingale measure**), where,  $\mathcal{G}_t$ -risk is taken as replicable from  $t-1$ . See [1, 18] for precise technical assumptions and examples.

## **Example in Continuous Time**

For an instructive example, consider a (nonfinite) filtered probability space  $(\Omega, (\mathcal{F}_t)_{t \leq T}, P)$  with Brownian motions  $(W_t)$  and  $(W_t) = (\rho W_t + \sqrt{1 - \rho^2} W_t^{\perp})$ correlated by  $\rho \in [-1, 1]$ . The price process of a single risky asset is  $S_t = S_0 + \sigma(W_t + \lambda t)$  with  $\lambda$ ,  $S_0 \in \mathbb{R}, \ \sigma > 0$ , as in the model by **Louis Bachelier.** The illiquid asset's payout  $B := Y_T$  for  $Y_t =$  $Y_0 + \widetilde{\sigma}(W_t + \lambda t)$  can be interpreted as position in a nontraded but correlated asset. Trading strategies  $\vartheta \in \Theta$  are taken to be adapted and bounded. The maximal expected exponential utilities

$$u_t^b(x) = -\frac{1}{\alpha} \exp\left(-\alpha \left(x + \frac{1}{2} \frac{\lambda^2}{\alpha} (T - t) + \pi_t^{0, x}(b)\right)\right),\,$$
  
$$x, b \in \mathbb{R}$$
(19)

are then attained by the optimal strategies  $\widehat{\vartheta}^{\,b} =$  $\frac{\lambda}{\sigma\alpha} - b\frac{\sigma}{\sigma}\rho$ , with

$$\pi_t^{0,x}(b) = bY_t + b\widetilde{\sigma}(\widetilde{\lambda} - \lambda\rho)(T - t)$$
$$-\frac{1}{2}\alpha b^2 \widetilde{\sigma}^2 (1 - \rho^2)(T - t) \qquad (20)$$

Indifference values  $\pi_t^{b,x}(\delta) = \pi_t^{0,x}(b+\delta) - \pi_t^{0,x}(b)$ for exponential utility do not depend on wealth  $x$ . Optimality of equation (19) and  $\widehat{\vartheta}^{\widehat{b}}$  follows by noting that  $u_t^b(\int_0^t \vartheta \, dS)$  is a martingale for  $\vartheta = \widehat{\vartheta}^b$  and a supermartingale for any other  $\vartheta \in \Theta$ . Clearly, indifference buy (sell) values  $\pi_t^{b,x}(\delta)$  (respectively  $-\pi_t^{b,x}(-\delta)$  are decreasing (increasing) in the risk aversion  $\alpha$ . They are linear in the quantity  $\delta$  only if correlation is perfect ( $|\rho| = 1$ ). Then, they coincide with the replication cost of  $\delta B$ . Marginal utility indifference values are given by

$$\frac{\partial}{\partial \delta} \pi_t^{b,x}(\delta) = Y_t + \widetilde{\sigma}(\widetilde{\lambda} - \lambda \rho)(T - t)$$
$$- \alpha (b + \delta) \widetilde{\sigma}^2 (1 - \rho^2)(T - t) \quad (21)$$

Under the (minimal entropy) martingale measure  $dQ^0 = \exp(-\lambda W_T - \lambda^2 T/2) dP$  we have  $S_t =$  $S_0 + \sigma W_t^0$  for independent  $Q^0$ -Brownian motions  $(W_t^0)$  and  $(W_t^{\perp})$ . Indifference values can be expressed by

$$-\pi_t^{0,x}(b) = \frac{1}{\alpha(1-\rho^2)} \log E_t^{\mathcal{Q}^0} \left[ \exp\left(\alpha(1-\rho^2)(-bB)\right) \right] (22)$$

Formulas like equation  $(22)$  have also been obtained for different models, including the case where the price processes of the risky and the nontraded asset (underlying of  $B$ ) are given by correlated geometric Brownian motions, see  $[6, 16]$ .

To discuss the possible size of the partial hedging error, let  $S_0$ ,  $Y_0$ ,  $\lambda$ ,  $\tilde{\lambda}$  be zero,  $T=1$ , and  $\sigma = \widetilde{\sigma}$ . We assume that the agent has accepted initially an illiquid position  $b$  at her indifference valuation. Her utility-based partial hedging strategy when holding *b* illiquid assets is  $\hat{\vartheta}^b - \hat{\vartheta}^0 = -b\rho$ .<br>Her hedging error  $H = -\pi_0^{0,x}(b) + bB - b\sigma\rho W_1^0 = \frac{1}{2}\alpha b^2\sigma^2(1-\rho^2) + b\sigma\sqrt{1-\rho^2}W_1^{\perp}$  is normally distributed. Its standard deviation accounts for  $\sqrt{1-\rho^2}\times 100\%$  of that for the unhedged payoff  $bB = bY_T$ . For correlation  $\rho = 80\%$ , for example, the error size is still substantial at a ratio of 60%. Even for  $\rho = 99\%$ , it is still above 14%. To be compensated for the remaining risk in terms of her expected utility, the agent requires  $-\pi_0^{0,x}(b) =$  $\frac{1}{2}\alpha b^2\sigma^2(1-\rho^2)$  at  $t=0$ . Her compensating varia- $\overline{\text{tion}}$  of wealth is proportional to the variance of H and to her risk aversion  $\alpha$ .

## **Further Reading**

To value options under transaction costs, indifference valuation was applied in [8]. The method is not limited to European payoffs. For payoffs with optimal exercise features, see  $[10, 17]$ . Indifference values for payoff streams could be defined by equation  $(1)$ for utilities that reflect preferences on future payment streams, like in [22]. For results on nonexponential utilities, see [5, 12, 14]. For performance of utilitybased hedging strategies, see [15]. Besides dynamical programming and convex duality, solutions have been obtained by backward stochastic differential equations (*see* **Backward Stochastic Differential Equations**) [10, 13, 20], also for non-convex closed constraints [9] and jumps [2]. For asymptotic results on valuation and hedging for small volumes, see [2, 5, 12, 13]. A Paretian equilibrium formulation for indifference pricing has been presented in [11]. Being nonlinear, indifference values can reflect diversification or accumulation of risk for applications areas like real options or insurance, see [6, 14, 19, 22]; but modeling and computation are more demanding, since a portfolio of assets cannot be valued by parts in general. Instead, each component is to be judged by its contribution to the overall portfolio. More comprehensive references are given in [1, 3, 4, 6, 16].

# **References**

- [1] Becherer, D. (2003). Rational hedging and valuation of integrated risks under constant absolute risk aversion, *Insurance: Mathematics and Economics* **33**, 1–28.
- [2] Becherer, D. (2006). Bounded solutions to backward SDEs with jumps for utility optimization and indifference hedging, *Annals of Applied Probability* **16**, 2027–2054.
- [3] Davis, M.H.A. (2006). Optimal hedging with basis risk, in *From Stochastic Calculus to Mathematical Finance*, Y. Kabanov, R. Liptser & J. Stoyanov, eds, Springer, Berlin, pp. 169–188.
- [4] Foldes, L. (2000). Valuation and martingale properties of shadow prices: an exposition, *Journal of Economic Dynamics and Control* **24**, 1641–1701.
- [5] Henderson, V. (2002). Valuation of claims on non-traded assets using utility maximization, *Mathematical Finance* **12**, 351–373.
- [6] Henderson, V. & Hobson, D. (2008). Utility indifference pricing—an overview, in *Indifference Pricing*, R. Carmona, ed, Princeton University Press, pp. 44–74.
- [7] Hicks, J.R. (1956). *A Revision of Demand Theory*, Oxford University Press, Oxford.
- [8] Hodges, S.D. & Neuberger, A. (1989). Optimal replication of contingent claims under transaction costs, *Review of Futures Markets* **8**, 222–239.
- [9] Hu, Y., Imkeller, P. & Muller, M. (2005). Utility ¨ maximization in incomplete markets, *Annals of Applied Probability* **15**, 1691–1712.
- [10] Kobylanski, M., Lepeltier, J., Quenez, M. & Torres, S. (2002). Reflected backward SDE with super-linear

quadratic coefficient, *Probability and Mathematical Statistics* **22**, 51–83.

- [11] Kramkov, D. & Bank, P. (2007). *A model for large investor, where she trades at utility indifference prices of market makers*, ICMS, Edinburgh, Present ation, www.icms.org.uk/downloads/quantfin/Kramkov. pdf
- [12] Kramkov, D. & Sirbu, M. (2007). Asymptotic analysis of utility-based hedging strategies for small number of contingent claims, *Stochastic Processes and Applications* **117**, 1606–1620.
- [13] Mania, M. & Schweizer, M. (2005). Dynamic exponential utility indifference valuation, *Annals of Applied Probability* **15**, 2113–2143.
- [14] Møller, T. (2003). Indifference pricing of insurance contracts: applications, *Insurance: Mathematics and Economics* **32**, 295–315.
- [15] Monoyios, M. (2004). Performance of utility-based strategies for hedging basis risk, *Quantitative Finance* **4**, 245–255.
- [16] Musiela, M. & Zariphopoulou, T. (2004). An example of indifference pricing under exponential preferences, *Finance and Stochastics* **8**, 229–239.
- [17] Musiela, M. & Zariphopoulou, T. (2004). Indifference prices of early exercise claims, in *Mathematics of Finance*, G. Yin & Q. Zhang, eds, *Contemporary Mathematics*, AMS, Vol. 351, pp. 259–273.
- [18] Musiela, M. & Zariphopoulou, T. (2004). A valuation algorithm for indifference prices in incomplete markets, *Finance and Stochastics* **8**, 399–414.
- [19] Porchet, A., Touzi, N. & Warin, X. (2008). Valuation of power plants by utility indifference and numerical computation, *Mathematical Methods of Operations Research* [Online], DOI: 10.007/s00186-008- 0231-z.
- [20] Rouge, R. & El Karoui, N. (2000). Pricing via utility maximization and entropy, *Mathematical Finance* **10**, 259–276.
- [21] Schachermayer, W. (2002). Optimal investment in incomplete financial markets, in *Mathematical Finance: Bachelier Congress 2000*, H. Geman, D. Madan & S.R. Pliska, eds, Springer, Berlin, pp. 427–462.
- [22] Smith, J.E. & Nau, R.F. (1995). Valuing risky projects: option pricing theory and decision analysis, *Management Science* **41**, 795–816.

# **Related Articles**

**Complete Markets**; **Expected Utility Maximization: Duality Methods**; **Good-deal Bounds**; **Hedging**; **Minimal Entropy Martingale Measure**; **Utility Theory: Historical Perspectives**; **Utility Function**.

DIRK BECHERER
# **Expected Utility Maximization: Duality** Methods

Expected utility maximization has a long tradition in modern mathematical finance. It dates back to the 1950s [18] when it provided a theoretical foundation to the (Markowitz's) mean-variance asset allocation method (see Risk-Return Analysis). The objective of a rational and risk-averse agent acting is captured by a concave function, the utility  $U$  of the agent (see **Utility Function**). It is typically assumed that  $U$  is increasing since the agent prefers more wealth to less. Given his/her U, the agent chooses the portfolio  $P^*$ that maximizes the agent's *expected utility* over a horizon  $[0, T]$ .

Some famous case studies are considered in [12, 13], where the agent is planning for retirement in a Black-Scholes (and thus complete) financial market (see Merton Problem). The complete market framework (see **Complete Markets**) is a convenient mathematical idealization as any conceivable risk can be hedged by cleverly investing in the market. As a consequence, independently of the specific utility of the agent, the price of any claim is also uniquely assigned since by the no-arbitrage principle it must coincide with the initial value of the hedging portfolio.

In the more realistic situation of incomplete market, when there are, for example, intrinsic, nontraded sources of risk, both the valuation and the hedging problems become highly nontrivial issues. Expected utility maximization has also turned out to perform very well in the pricing problem in the general, incomplete market setup. The related pricing techniques are known as *pricing by marginal utility* and *indifference pricing* and are discussed briefly in this article (for more details see Utility Indifference Valuation).

The use of increasingly more complex probabilistic models of financial assets has continued to pose new mathematical challenges. If the setup is that of general non-Markovian diffusion or semimartingale models, direct methods from stochastic optimal control (as originally done by Merton and many others after him) become increasingly difficult to handle. As first suggested by Bismut [4], convex duality (see

**Convex Duality**) is a powerful alternative approach. In the mid-1980s, with the works of Pliska [14], He and Pearson [8], Karatzas et al. [10], and Cox and Huang [5] this new methodology started to fully develop. Relying on convex duality (see Convex Duality) and martingale (see Martingales) methods, it enables the treatment of the most general cases. The price to pay for the achieved generality is that the results obtained have a mathematical existence-uniqueness-characterization form. As is always the case, explicit calculations require the specification of a (very) tractable model.

The presentation given here is based on the convex duality approach, in a general semimartingale model. For a treatment of the same problem with martingale methods in a diffusion context, see **Expected Utility** Maximization or [9].

## Examples

Consider an agent who is a price taker, that is, his/her actions do not affect market prices, and whose goal is to trade dynamically in a financial market up to a horizon  $T$ , in order to achieve maximum expected utility. A host of features can be taken into account, such as the initial endowment, the possibility of intertemporal consumption, and the presence of a random endowment at time  $T$ . A list of various situations is given in the following. The mathematical details are discussed in the next section.

#### 1. Maximizing Utility of Terminal Wealth

The preferences of the investor are represented by a von Neumann–Morgenstern utility function

$$U: \mathbb{R} \to [-\infty, +\infty) \tag{1}$$

which must be not identical to  $-\infty$ , increasing, and concave.

Typical examples are  $U(x) = \ln x$ ,  $U(x) = \frac{1}{\alpha}x^{\alpha}$ with  $\alpha < 1, \alpha \neq 0$ , where it is intended that  $U(x) =$  $-\infty$  outside the domain, and  $U(x) = -\frac{1}{\nu}e^{-\gamma x}$  with  $\nu > 0.$ 

No consumption occurs before time  $T$ . The agent has the initial endowment  $x$  and can invest in the financial market. The resulting optimization problem is

$$\sup_{k \in K(x)} E[U(k)] \tag{2}$$

where *K(x)* is the set of random wealths that can be obtained at time *T* (terminal wealths) with initial wealth *x*.

The formulation of the problem with random endowment, namely, when the agent receives at T an additional cashflow *B* (say, an option), is the following:

$$\sup_{k \in K(x)} E[U(k+B)] \tag{3}$$

as his/her terminal possible wealths now are of the form *k* + *B*.

#### **2. Maximizing Utility of Consumption**

Suppose that the agent is not particularly interested in consumption at the terminal time *T* , but rather he/she is willing to consume over the entire planning horizon. A consumption plan *C* for the agent is determined by its random rate of consumption *c(t)* at time *t* for all *t* ∈ [0*, T* ]. It is evident from the financial perspective that the rate *c(t)* must be nonnegative, so the consumption in the interval [*t,t* + d*t*] increases by the quantity *c(t)*d*t*. The goal of the agent is thus the selection of the best consumption plan over [0*, T* ], starting with an initial endowment *x* ≥ 0. The utility function will now measure the degree of satisfaction with the intertemporal consumption or better with the rate of consumption. As this measure may change over the time, the utility also depends on the time parameter:

$$\overline{U} : [0, T] \times \mathbb{R} \to [-\infty, +\infty) \tag{4}$$

When *t* is fixed, then *U (t,* ·*)* is a utility function with the same properties as in case (1). As the rate of consumption cannot be negative, *U (t, x)* = −∞ when *x <* 0. The agent may clearly benefit from the opportunity of investing in the financial market, so in general his/her position can be expressed by a consumption plan *C* and a dynamically changing portfolio *P*. If *XC,P (t)* is the total wealth of the position *(C, P )* at time *t*, then as there is no inflow of cash the variation of the wealth in [*t,t* + d*t*] must satisfy

$$dX^{C,P}(t) = -c(t) dt + dV^{P}(t)$$
(5)

where d*V <sup>P</sup> (t)* is the variation of the value of the portfolio *P* at time *t* due to market fluctuations. Let A*(x)* indicate the set of all such consumption plans—portfolios *(C, P )* when starting from the wealth level *x*. The maximization is then that of the expected integrated utility from the rate of consumption:

$$\sup_{(C,P)\in\mathcal{A}(x)} E\left[\int_0^T \overline{U}(t,c(t))\,\mathrm{d}t\right] \tag{6}$$

## **3. Maximizing Utility of Terminal Wealth and Consumption**

Alternatively, the agent may wish to maximize expected utility from terminal wealth and intertemporal consumption given his/her initial wealth *x* ≥ 0. Therefore, there are two utilities, *U* and *U*, from terminal wealth and from the rate of consumption, respectively. Let A*(x)* be the set of the possible consumption plans—portfolios *(C, P )*, obtained with initial wealth *x*, and let *XC,P (T )* be the terminal wealth from the choice *(C, P )*. Then the optimal consumption–investment is the couple *(C*<sup>∗</sup>*, P*<sup>∗</sup>*)* that solves

$$\sup_{(C,P)\in\mathcal{A}(x)} \left\{ E\bigg[\int_0^T \overline{U}(t,c(t)) \,\mathrm{d}t \bigg] + E\left[U\left(X^{C,P}(T)\right)\right] \right\} \tag{7}$$

The case selected in the following section for the illustration of the duality technique and the main results is the first, that is, utility maximization of terminal wealth. When intertemporal consumption is taken into account, similar results can be proved. In addition, case 3 turns out to be a superposition of cases 1 and 2, as shown in Chapters 3, 6 of [9].

# **Maximizing the Utility of (Discounted) Terminal Wealth**

An analysis of any optimization problem relies on a precise definition of the domain of optimization and the objective function. Therefore, the study of maximization (2) requires a specification of

- 1. the financial market model and the admissible terminal wealths;
- 2. the technical assumptions on *U*; and
- 3. some joint condition on the market model and the utility function.

1. The financial market model considered is frictionless and consists of *N* risky assets and one risk-free asset (money market account). Although it is not necessary, for the sake of convenience, it is assumed that the risk-free asset,  $S^0$ , is constantly equal to 1, that is, the prices are *discounted*. The N risky assets are globally indicated by  $S =$  $(S^1, \ldots, S^N)$ . The trading can occur continuously in [0, T].  $S = (S_t)_{t \leq T}$  is, in fact, an  $\mathbb{R}^N$ -valued, continuous-time process, defined on a filtered probability space  $(\Omega, (\mathcal{F}_t)_{t \leq T}, \mathbb{P})$ . Since the wealth from an investment in this market is a (stochastic) inte- $\text{grad}$ , S is assumed to be a semimartingale so that the object "integral with respect to  $S$ " is mathematically well defined (see Stochastic Integrals). For expository reasons,  $S$  is a *locally bounded* semimartingale. This class of models is already very general, as all the diffusions are locally bounded semimartingales, as well as any jump-diffusion process with bounded jumps.

The agent has an initial endowment  $x$  and there are no restrictions on the quantities he/she can buy, sell, or sell short.  $H_t = (H_t^1, \dots H_t^N)$  is the random vector with the number of shares of each risky asset that the agent holds in the infinitesimal interval  $[t, t + dt]$ .  $B_t$  represents the number of shares of the risk-free asset held in the same interval.  $H = (H_t)_t$ and  $B = (B_t)_t$  are the corresponding processes and are referred to as the *strategy* of the agent. To be technically precise,  $H$  must be a predictable process and  $B$  a semimartingale. As there is no consumption and no infusion of money in the trading period  $[0, T]$ , the wealth from a strategy  $(H, B)$  is the process X that solves

$$\begin{cases} dX_t = (H_t \, dS_t + B_t \, dS_t^0) = H_t \, dS_t \\ X_0 = x \end{cases} \tag{8}$$

or, in integral form,  $X_t = x + \int_0^t H_s \, dS_s$ . This can be equivalently stated as the strategy  $(H, B)$  is selffinancing. Since  $dS^0 = 0$ , the self-financing condition enables a representation of the wealth  $X$  only in terms of H. This is the reason one typically refers to  $H$  only as the strategy.

As usual in continuous-time trading (see Fundamental Theorem of Asset Pricing) to avoid phenomena like doubling strategies, not every self-financing  $H$  is allowed. A self-financing strategy  $H$  is said to be *admissible* only if during the trading the losses do not exceed a finite credit line. That is,  $H$  is admissible

if there exists some constant  $c > 0$  such

for all 
$$t \in [0, T]$$
,  $\int_0^t H_s dS_s \ge -c \quad \mathbb{P} - a.s.$  (9)

so that for any x the wealth process  $X = x +$  $\int H_{\rm s} \, \mathrm{d}S_{\rm s}$  is also bounded from below. Maximizing expected utility from terminal wealth means, in fact, maximizing expected utility from the set  $K(x)$  of those random variables  $X_T$  that can be represented as  $X_T = x + \int_0^T H_t \, \mathrm{d}S_t$  with H admissible in the sense of equation (9).

Hereafter, the notation  $E[\cdot]$  indicates  $\mathbb{P}$ -expectation. When considering expectation under another probability  $\mathbb{Q}$ , the notation is explicitly  $E_{\mathbb{Q}}[\cdot]$ .

As shown by Delbaen and Schachermayer [7] a financially relevant set of probabilities is  $\mathcal{M}^e$ , namely, the set of the equivalent (local) martingale probabilities for  $S$ . When the market is complete, this set consists of only one probability, but in the general, incomplete market case, this set is infinite. Under each probability,  $\mathbb{Q} \in \mathcal{M}^e$  S is a (local) martingale and thus  $\mathbb{Q}$  is a risk-neutral probability. This is the theoretical justification for the use of each of these  $\mathbb{Q}$ s as a pricing measure for any derivative claim B, with (arbitrage-free) price given by the expectation  $E_{\bigcirc}[B]$ .

However, we need the less restrictive set  $\mathcal{M}$  of the absolutely continuous (local) martingale probabilities  $\mathbb{Q}$  for S, as this is the set that will show up in the dual problem. The set  $\mathcal{M}$  can be characterized in the following manner:

$$\mathcal{M} = \left\{ \mathbb{Q} \ll \mathbb{P} \mid E_{\mathbb{Q}} \left[ \int_{0}^{T} H_{t} \, \mathrm{d}S_{t} \right] \leq 0 \,\,\forall \,\,\mathrm{adm.} \,\, H \right\}$$
(10)

as the set of absolutely continuous probability measures that give nonpositive expectation to the terminal wealths from admissible self-financing strategies starting with zero wealth. Therefore, given any  $X_T \in K(x)$  and any  $\mathbb{Q} \in \mathcal{M}$ ,

$$E_{\mathbb{Q}}[X_T] = E_{\mathbb{Q}}\left[x + \int_0^T H_t \, \mathrm{d}S_t\right] \le x \qquad (11)$$

2. Hypothesis on  $U$ . As a case study, let us assume that U is finite valued on  $\mathbb{R}$ , that is, the wealth can become arbitrarily negative (the closest references are [2, 16]). A typical example is the exponential utility. The reason we prefer the exponential utility (and all the other utilities with the properties listed below) to, for example, the logarithmic or the power utilities is that the dual problem is easier to interpret. References for the case when there are constraints on the wealth (then  $U$  is finite only on a half-line), like  $U(x) = \ln x$  or  $U(x) =$  $\frac{1}{\alpha}x^{\alpha}$ , are [11], [17], and the bibliography contained therein.

A main difficulty the reader may encounter when comparing this literature is that the language and style in the papers differ. Very recently, Biagini and Frittelli [3] proposed a unifying approach that works both for the case of U finite on all  $\mathbb{R}$  and for the case of  $U$  finite only on a half-line. The result there is enabled by the choice of an innovative duality (an Orlicz space duality), naturally induced by the utility function  $U$ .

Regarding  $U$ , it is here required that

- $U$  is strictly concave, strictly increasing, and differentiable over  $(-\infty, +\infty)$  and
- $\lim_{x \downarrow -\infty} U'(x) = -\infty$  and  $\lim_{x \to +\infty} U'(x) = 0$ (these are known as the Inada condition on the marginal utility  $U'$ ).

In addition,  $U$  must satisfy the reasonable asymptotic elasticity condition  $RAE(U)$  introduced in [11, 16]:

$$\liminf_{x \to -\infty} \frac{xU'(x)}{U(x)} > 1, \quad \limsup_{x \to +\infty} \frac{xU'(x)}{U(x)} < 1 \quad (12)$$

In the cited references, it is also shown that this condition is necessary and sufficient for the duality to work properly if  $U$  is fixed and one considers all possible financial markets. However, within a specific *market model*, one may state more general necessary and sufficient conditions on  $U$  that enable the duality approach and ensure the existence of the optimal investment. We choose to impose  $RAE(U)$  for it has the advantage that it can be easily verified. Note also that  $RAE(U)$  is already satisfied by the commonly used utility functions, for example, by the classic exponential function  $U(x) = -\frac{1}{\nu}e^{-\gamma x}$ .

3. The convex conjugate  $V$  and a joint condition between preferences and the market. The conjugate  $V$  of  $U$  is the function

$$V(y) = \sup_{x} \{U(x) - yx\} \tag{13}$$

and, apart from some minus signs, it coincides with the Fenchel conjugate of  $U$  (see **Convex Duality**). Thus,  $V$  is a convex function, which is identically equal to  $+\infty$  when  $y < 0$ . It is also differentiable on  $(0, +\infty)$  and its derivative is  $V' = -(U')^{-1}$ . Traditionally, the inverse of the marginal utility  $(U')^{-1}$  is denoted by *I*. By mere definition of *V*, for all  $x$ ,  $y$ , the Fenchel inequality holds

$$U(x) \le xy + V(y) \tag{14}$$

and the above relation is, in fact, an equality iff  $y =$  $U'(x)$  or equivalently  $x = (U')^{-1}(y) = I(y)$ . Also note that

$$U(x) = \inf_{y} \{xy + V(y)\} = \inf_{y>0} \{xy + V(y)\} \quad (15)$$

The typical example (and most used) is the following couple  $(U, V)$ :

$$U(x) = -\frac{1}{\gamma} e^{-\gamma x}$$
  
$$V(y) = \begin{cases} \frac{1}{\gamma} (y \ln y - y) & y > 0\\ 0 & y = 0\\ +\infty & y < 0 \end{cases}$$
 (16)

Let us recall that a probability  $\mathbb{Q}$  absolutely continuous with respect to  $\mathbb{P}$  is said to have *finite generalized* entropy (or, also, finite V-divergence), if its density  $\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}$  is integrable when composed with V

$$E\left[V\left(\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] < +\infty\tag{17}$$

The joint condition required between preferences and the market is actually a condition between  $V$  and the set of probabilities  $\mathcal{M}$ , which is as follows:

**Condition 1** There exists a  $Q^0 \in \mathcal{M}$  with finite generalized entropy, that is,  $E\left[V\left(\frac{\mathrm{d}Q^0}{\mathrm{d}P}\right)\right] < +\infty$ .

## **Duality in Complete Market Models**

Suppose that the market is complete and arbitrage free. Thus, there exists a unique equivalent martingale measure  $\mathbb{Q} \in \mathcal{M}^e$ , which, by Condition 1, has also finite generalized entropy. Let us restate problem (2), the *primal* problem

$$u(x) := \sup_{X_T \in K(x)} E[U(X_T)] \tag{18}$$

where  $u(x)$  denotes the optimal level of the expected utility. It is not difficult to derive an upper bound for  $u(x)$ . From inequality (14), in fact, for all  $X_T \in K(x)$ and for all  $y > 0$ 

$$U(X_T) \le X_T y \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} + V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right) \tag{19}$$

and taking  $\mathbb{P}$ -expectations on both sides

$$E[U(X_T)] \le xy + E\left[V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] \qquad (20)$$

because  $E\left[X_T \frac{d\mathbb{Q}}{d\mathbb{P}}\right] = E_{\mathbb{Q}}[X_T] \leq x$ . Therefore, taking the supremum over  $X_T$  and the infimum over  $y$ ,

 $u(x)$ 

$$= \sup_{X_T \in K(x)} E[U(X_T)] \le \inf_{y>0} xy + E\left[V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right]$$
(21)

As noted by Merton, the above supremum is not necessarily reached over the restricted set of admissible terminal wealths  $K(x)$ . Following a wellknown procedure in the calculus of variations, a relaxation of the primal problem allows to obtain the optimal terminal wealth. Here, this means enlarging  $K(x)$  slightly and considering the larger set

$$K_{\mathbb{Q}}(x) := \{k \in L^{1}(\mathbb{Q}) \mid E_{\mathbb{Q}}[k] \le x\}$$
(22)

 $K_{\mathbb{O}}(x)$  is simply the set of claims that have initial price smaller or equal to the initial endowment  $x$ . An application of the separating hyperplane theorem gives that  $K_{\mathbb{Q}}(x)$  is the norm closure of  $K(x)$  –  $L^1_{+}(\mathbb{Q})$  in  $L^1(\mathbb{Q})$ . Then, an approximation argument shows that the optimal expected value  $u(x)$  and

$$u_{\mathbb{Q}}(x) := \sup_{k \in K_{\mathbb{Q}}(x)} E[U(k)] \tag{23}$$

are, in fact, equal. The *relaxed* maximization problem over  $K_{\mathbb{Q}}(x)$  is much simpler than the original one over  $K(x)$ . The replication-with-admissible-strategies issue has been removed and there is just an inequality constraint, given by the pricing measure  $\mathbb{Q}$ . To find

out the value  $u_{\mathbb{O}}(x) = u(x)$ , one can now apply the traditional Lagrange multiplier method to get

$$u_{\mathbb{Q}}(x) = \sup_{k \in K_{\mathbb{Q}}(x)} E[U(k)]$$
  
= 
$$\sup_{k \in L^{1}(\mathbb{Q})} \inf_{y>0} \{E[U(k)] + y(x - E_{\mathbb{Q}}[k])\}$$
  
(24)

The dual problem is defined by exchanging the inf and the sup in the above expression:

$$\inf_{y>0} \sup_{k \in L^1(\mathbb{Q})} \{ E[U(k)] + y(x - E_{\mathbb{Q}}[k]) \}$$
(25)

From [15 Theorem 21] or from a direct computation, the inner sup is actually equal to

$$xy + E\left[V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] \tag{26}$$

so that the dual problem takes the traditional form

$$\inf_{y>0} \left\{ xy + E\left[ V\left( y \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} \right) \right] \right\} \tag{27}$$

which is exactly the right-hand side of equation  $(21)$ .

Thanks to Condition 1, the dual problem is always finite valued and so is  $u.$  A priori, however, one has only the chain  $u(x) = u_{\mathbb{Q}}(x) \leq$  $\inf_{y>0} \left\{ xy + E \left[ V \left( y \frac{d\mathbb{Q}}{d\mathbb{P}} \right) \right] \right\}$ , but under the current assumptions there is no duality gap:

$$u(x) = u_{\mathbb{Q}}(x) = \inf_{y>0} \left\{ xy + E\left[ V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right) \right] \right\} \tag{28}$$

the infimum is a minimum and the supremum over  $K_{\mathbb{Q}}(x)$  is reached. In fact, the  $RAE(U)$  condition on the utility function U implies that  $E\left[V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] <$  $+\infty \ \forall y > 0$ , so the infimum in (27) can be obtained by differentiation under the expectation sign. The dual minimizer  $y^*$  (which depends on x) is then the unique solution of

$$x + E_{\mathbb{Q}} \left[ V' \left( y \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} \right) \right] = 0 \tag{29}$$

or, equivalently,  $y^*$  is the unique solution of

$$E_{\mathbb{Q}}\left[I\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] = x\tag{30}$$

Therefore, the (unique) optimal claim is  $k^* =$  $I\left(y^*\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)$  because it verifies the following:

- the balance equation  $E_{\mathbb{Q}}[k^*] = x$ , so  $k^* \in K_{\mathbb{Q}}(x)$ and
- the Fenchel equality

$$U(k^*) = k^* y^* \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} + V\left(y^* \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right) \tag{31}$$

from which, by taking the  $\mathbb{P}$ -expectations, we get

$$E[U(k^*)] = y^* E\left[k^* \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right] + E\left[V\left(y^* \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right]$$
$$= y^* x + E\left[V\left(y^* \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right] \tag{32}$$

which proves the main equality (28).

By market completeness, the martingale representation theorem applies, so that  $k^*$  can be obtained *via* a self-financing strategy  $H^*$ :

$$k^* = x + \int_0^T H_t^* \, \mathrm{d}S_t \tag{33}$$

though  $H^*$  is not admissible in general, that is, when optimally investing, the agent can incur arbitrarily large losses.

Moreover, as a function of  $x$ , the optimal value  $u(x)$  is also a utility function finite on  $\mathbb{R}$ , with the same properties of  $U$ . The duality equation (28) shows that  $u$  and

$$v(y) = \begin{cases} E\left[V\left(y\frac{\mathrm{d}Q}{\mathrm{d}P}\right)\right] & \text{if } y \ge 0\\ +\infty & \text{otherwise} \end{cases} \tag{34}$$

are conjugate functions.

The relationship between the primal and dual optima can also be expressed as

$$\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} = \frac{1}{y^*} U'(k^*) \tag{35}$$

which amounts to saying that  $\frac{d\mathbb{Q}}{d\mathbb{P}}$  is proportional to one's marginal utility from the optimal investment. Therefore, in the complete market case, pricing by taking  $\mathbb{Q}$ -expectations coincides with the *pricing by marginal utility principle*, introduced in the option pricing context by Davis [6].

## **Duality in Incomplete Market Models**

The same methodology applies to the incomplete market framework, but the technicalities require some more effort. The main results are (more or less intuitive) generalizations of what happens in the complete case, as summarized below (see [2, 16] for the proofs).

1. The duality relation is the natural generalization of equation  $(28)$ :

$$u(x) = \sup_{X_T \in K(x)} E[U(X_T)]$$
  
= 
$$\inf_{y>0, \mathbb{Q} \in \mathcal{M}} \left\{ xy + E\left[ V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right) \right] \right\}$$
(36)

and there exists a unique couple of dual minimizers  $y^*, \mathbb{Q}^*$ .

2. As in the complete case, the supremum of the expected utility on  $K(x)$  may be not reached.  $K_V(x)$  denotes the set of  $k \in L^1(\mathbb{Q})$  such that  $E_{\mathbb{Q}}[k] \leq x$  for all  $\mathbb{Q} \in \mathcal{M}$  with finite generalized entropy. Then, the supremum of the expected utility on  $K_V(x)$  coincides with the value  $u(x)$ and it is a maximum. The claim  $k^* \in K_V$  attaining the maximum is unique and the relationship between primal and dual optima still holds

$$\frac{\mathrm{d}\mathbb{Q}^*}{\mathrm{d}\mathbb{P}} = \frac{1}{y^*} U'(k^*) \tag{37}$$

- 3.  $\mathbb{Q}^*$  may be not equivalent to  $\mathbb{P}$ . However, in the case  $\mathbb{Q}^* \sim \mathbb{P}, k^*$  can be obtained through a selffinancing strategy  $H^*$ , albeit not admissible in general.
- The optimal value  $u$  as a function of the initial 4 endowment  $x$  is a utility function, with the same properties of U. In fact, it is finite on  $\mathbb{R}$ , strictly concave, strictly increasing, it verifies the Inada conditions, and  $RAE(u)$  holds. The duality relation (36), rewritten as  $u(x) = \inf_{y>0} \{xy + v(y)\}\$ with

$$v(y) = \begin{cases} \inf_{\mathbb{Q}\in\mathcal{M}} E\left[V\left(y\frac{\mathrm{d}Q}{\mathrm{d}P}\right)\right] & \text{if } y \ge 0\\ +\infty & \text{otherwise} \end{cases}$$
(38)

shows that  $u$  and  $v$  are conjugate functions (see **Convex Duality**)

As  $\mathbb{Q}^*$  results from a minimax theorem, it is also known as the *minimax measure*. For the applications, it is important to know that there are easy sufficient conditions that guarantee that  $\mathbb{Q}^*$  is equivalent to  $\mathbb{P}$ , such as the following: (i)  $U(+\infty) = +\infty$  as noted in [1] or (ii) in case  $U(x) = -\frac{1}{\nu}e^{-\gamma x}$ , the existence of a  $\mathbb{Q} \in \mathcal{M}^e$  with finite generalized entropy (see [17] for an extensive bibliography).

When  $\mathbb{Q}^*$  is indeed equivalent to  $\mathbb{P}$ , its selection in the class of all risk-neutral, equivalent probabilities  $\mathcal{M}^e$  as *the* pricing measure is economically motivated by its proportionality to the marginal utility from the optimal investment.

## **Utility Maximization with Random** Endowment

Under all the conditions stated above (on the market, on  $U$ , and on both), suppose that the agent has a random endowment  $B$  at  $T$ , in addition to the initial wealth x. For example,  $B$  can be the payoff of a European option expiring at  $T$ . The agent's goal is still maximizing of expected utility from terminal wealth, which now becomes

$$u(x, B) := \sup_{X_T \in K(x)} E[U(B + X_T)] \qquad (39)$$

The duality results, in this case, are similar to the ones just shown. In fact,

$$u(x, B) = \min_{y>0, \mathbb{Q} \in \mathcal{M}} \left\{ xy + yE_{\mathbb{Q}}[B] + E\left[V\left(y\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right)\right]\right\}$$
(40)

Note that the maximization without the claim can be seen as a particular case of the one above, with  $B = 0$ :  $u(x, 0) = u(x)$ . The solution of a utility maximization problem with random endowment is the key step to the indifference pricing technique. The (buyer's) indifference price of  $B$  is, in fact, the unique price  $p_B$  that solves

$$u(x - p, B) = u(x, 0) \tag{41}$$

This means that the agent is indifferent, that is, he/she has the same (optimal expected) utility, between (i) paying  $p_B$  at time  $t = 0$  and receiving B at  $T$  and (ii) not entering into a deal for the claim  $B$ .

## References

- Bellini, F. & Frittelli, M. (2002). On the existence of [1] minimax martingale measures, Mathematical Finance 12/1. 1-21.
- Biagini, S. & Frittelli, M. (2005). Utility maximization [2] in incomplete markets for unbounded processes, Finance and Stochastics 9, 493-517.
- Biagini, S. & Frittelli, M. (2008). A unified frame-[3] work for utility maximization problems: an Orlicz space approach, Annals of Applied Probability 18/3, 929-966.
- Bismut, J.M. (1973). Conjugate convex functions in [4] optimal stochastic control, Journal of Mathematical Analysis and Applications 44, 384–404.
- Cox, J.C. & Huang, C.F. (1989). Optimal consump-[5] tion and portfolio policies when asset prices follow a diffusion process, Journal of Economic Theory 49, 33-83.
- Davis, M.H.A. (1997). Option pricing in incomplete [6] markets, in Mathematics of Derivative Securities, M. Dempster & S.R. Pliska, eds, Cambridge University Press, pp. 216-227.
- [7] Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing, Mathematische Annalen 300, 463-520.
- [8] He, H. & Pearson, N.D. (1991). Consumption and portfolio policies with incomplete markets and shortsale constraints: the infinite-dimensional case, Journal of Economic Theory 54, 259-304.
- Karatzas, I. & Shreve, S. (1998). Methods of Mathemat-[9] ical Finance, Springer.
- [10] Karatzas, I., Shreve, S., Lehoczky, J. & Xu, G. (1991). Martingale and duality methods for utility maximization in an incomplete market, SIAM Journal on Control and Optimization 29, 702-730.
- [11] Kramkov, D. & Schachermayer, W. (1999). The asymptotic elasticity of utility function and optimal investment in incomplete markets, Annals of Applied Probability 9/3. 904-950.
- [12] Merton, R.C. (1969). Lifetime portfolio selection under uncertainty: the continuous-time case, The Review of Economics and Statistics  $51$ ,  $247-257$ .
- [13] Merton, R.C. (1971). Optimum consumption and portfolio rules in a continuous-time model, Journal of Economic Theory 3, 373-413.
- [14] Pliska, S.R. (1986). A stochastic calculus model of continuous trading: optimal portfolios, Mathematics of Operations Research 11, 371-382.
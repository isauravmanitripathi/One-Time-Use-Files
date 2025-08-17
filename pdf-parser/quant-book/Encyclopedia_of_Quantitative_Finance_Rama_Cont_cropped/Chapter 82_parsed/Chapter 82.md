# Arrow-Debreu Prices

Arrow-Debreu prices are the prices of "atomic" time and state-contingent claims, which deliver one unit of a specific consumption good if a specific uncertain state realizes at a specific future date. For instance, claims on the good "ice cream tomorrow" are split into different commodities depending on whether the weather will be good or bad, so that good-weather and bad-weather ice cream tomorrow can be traded separately. Such claims were introduced by Arrow and Debreu in their work on general equilibrium theory under uncertainty, to allow agents to exchange state and time contingent claims on goods. Thereby the general equilibrium problem with uncertainty can be reduced to a conventional one without uncertainty. In finite-state financial models, Arrow-Debreu securities delivering one unit of the numeraire good can be viewed as natural atomic building blocks for all other state-time contingent financial claims; their prices determine a unique arbitrage-free price system.

#### Arrow–Debreu Equilibrium Prices

This section explains Arrow-Debreu prices in an equilibrium context, where they originated, see [1, 3]. We first consider a single-period model with uncertain states that will be extended to multiple periods later. For this exposition, we restrict ourselves to a single consumption good only, and consider a pure exchange economy without production.

Let  $(\Omega, \mathcal{F})$  be a measurable space of finitely many outcomes  $\omega \in \Omega = \{1, 2, \ldots, m\}$ , where the  $\sigma$ -field  $\mathcal{F} = 2^{\Omega}$  is the power set of all events  $A \subset \Omega$ . There is a finite set of agents, each seeking to maximize the utility  $u^a(c^a)$  from his or her consumption  $c^a =$  $(c_0^a, c_1^a(\omega)_{\omega \in \Omega})$  at present and future dates 0 and 1, given some endowment that is denoted by a vector  $(e_0^a, e_1^a(\omega)) \in \mathbb{R}^{1+m}_{++}$ . For simplicity, let consumption preferences of agent  $a$  be of the expected utility form

$$u^{a}(c^{a}) = U_{0}^{a}(c_{0}) + \sum_{\omega=1}^{m} P^{a}(\omega)U_{\omega}^{a}(c_{1}(\omega)) \quad (1)$$

where  $P^a(\omega) > 0$  are subjective probability weights, and the direct utility functions  $U^a_\omega$  and  $U^a_0$  are, for present purposes, taken to be of the form  $U_i^a(c) =$   $d_i^a c^{\gamma}/\gamma$  with relative risk aversion coefficient  $\gamma =$  $\gamma^a \in (0, 1)$  and discount factors  $d_i^a > 0$ . This example for preferences satisfies the general requirements (insaturation, continuity and convexity) on preferences for state-contingent consumption in [3], which need not be of the separable subjective expected utility form above. The only way for agents to allocate their consumption is by exchanging state-contingent claims for the delivery of some units of the (perishable) consumption good at a specific future state. Let  $q_{\omega}$  denote the price at time 0 for the state-contingent claim that pays  $q_0 > 0$  units if and only if state  $\omega \in \Omega$ is realized. Given the endowments and utility preferences of the agents, an equilibrium is given by consumption allocations  $c^{a*}$  and a linear price system  $(q_{\omega})_{\omega \in \Omega} \in \mathbb{R}^m_{+}$  such that,

1. for any agent a, his or her consumption  $c^{a*}$ maximizes  $u^a(c^a)$  over all  $c^a$  subject to budget constraint  $(c_0^a - e_0^a)q_0 + \sum_{\omega} (c_1^a - e_1^a)(\omega)q_{\omega}$ 

$$\leq 0$$
, and

markets clear, that is  $\sum_{a} (c_t^a - e_t^a)(\omega) = 0$  for all 2. dates  $t = 0, 1$  and states  $\omega$ .

An equilibrium exists and yields a *Pareto optimal* allocation; see [3], Chapter 7, or the references below. Relative equilibrium prices  $q_{\omega}/q_0$  of the Arrow securities are determined by first-order conditions from the ratio of marginal utilities evaluated at optimal consumption: for any  $a$ ,

$$\frac{q_{\omega}}{q_0} = P^a(\omega) \frac{\partial}{\partial c_1^a} U^a_{\omega}(c_1^{a*}(\omega)) \bigg/ \frac{\partial}{\partial c_0^a} U^a_0(c_0^{a*}) \tag{2}$$

To demonstrate the existence of equilibrium, the classical approach is to show that excess demand vanishes, that is markets clear, by using a fixed point argument (see Chapter 17 in [8]). To this end, it is convenient to consider  $c^a$ ,  $e^a$  and  $q =$  $(q_0, q_1, \ldots, q_m)$  as vectors in  $\mathbb{R}^{1+m}$ . Since only relative prices matter, we may and shall suppose that prices are normalized so that  $\sum_{i=0}^{m} q_i = 1$ , that is, the vector  $q$  lies in the unit simplex  $\Delta =$  $\{q \in \mathbb{R}^{1+m}_+ | \sum_{0}^{m} q_i = 1\}$ . The budget condition 1 then reads compactly as  $(c^a - e^a)q \le 0$ , where the lefthand side is the inner product in  $\mathbb{R}^{1+m}$ . For given prices  $q$ , the optimal consumption of agent  $a$  is given by the inverse of the marginal utility, evaluated at a multiple of the state price density (see equation  $(12)$ for the general definition in the multiperiod case), as

$$c_0^{a*} = c_0^{a*}(q) = (U_0^{a'})^{-1} \left(\lambda^a q_0\right) \text{ and}$$
  
$$c_{1,\omega}^{a*} = c_{1,\omega}^{a*}(q) = (U_{\omega}^{a'})^{-1} \left(\lambda^a q_{\omega}/P^a(\omega)\right), \quad \omega \in \Omega$$
  
(3)

where  $\lambda^a = \lambda^a(q) > 0$  is determined by the budget constraint  $(c^{a*} - e^a)q = 0$  as the Lagrange multiplier associated to the constrained optimization problem 1. Equilibrium is attained at prices  $q^*$  where the aggregate excess demand

$$z(q) := \sum_{a} (c^{a*}(q) - e^{a}) \tag{4}$$

vanishes, that is  $z(q^*) = 0$ . One can check that  $z:\Delta\to\mathbb{R}^{1+m}$  is continuous in the (relative) interior  $\Delta^{\text{int}} := \Delta \cap \mathbb{R}^{1+m}_{++}$  of the simplex, and that  $|z(q^n)|$  goes to  $\infty$  when  $q^n$  tends to a point on the boundary of  $\Delta$ . Since each agent exhausts his or her budget constraint 1. with equality, Walras' law  $z(q)q = 0$  holds for any  $q \in \Delta^{\text{int}}$ . Let  $\Delta^n$  be an increasing sequence of compact sets exhausting the simplex interior:  $\Delta^{\text{int}} = \bigcup_n \Delta^n$ . Set  $\nu^n(z) :=$  $\{q \in \Delta^n \mid zq > zp \; \forall p \in \Delta^n\}$ , and consider the correspondence (a multivalued mapping)

$$\Pi^n : (q, z) \mapsto (\nu^n(z), z(q)) \tag{5}$$

that can be shown to be convex, nonempty valued, and maps the compact convex set  $\Delta^n \times z(\Delta^n)$  into itself. Hence, by Kakutani's fixed point theorem, it has a fixed point  $(q^{n*}, z^{n*}) \in \Pi^n(q^{n*}, z^{n*})$ . This implies that

$$z(q^{n*})q \le z(q^{n*})q^{n*} = 0 \quad \text{ for all } q \in \Delta^n \quad (6)$$

using Walras' law. A subsequence of  $q^{n*}$  converges to a limit  $q^* \in \Delta$ . Provided one can show that  $q^*$  is in the interior simplex  $\Delta^{\text{int}}$ , existence of equilibrium follows. Indeed, it follows that  $z(q^*)q \le 0$  for all  $q \in \Delta^{\text{int}}$ , implying that  $z(q^*) = 0$  since  $z(q^*)q^* = 0$ by Walras' law. To show that any limit point of  $q^{n*}$ is indeed in  $\Delta^{\text{int}}$ , it suffices to show that  $|z(q^{n*})|$  is bounded in  $n$ , recalling that  $z$  explodes at the simplex boundary. Indeed,  $z = \sum_{a} z^{a}$  is bounded from below since each agent's excess demand satisfies  $z^a = c^a - e^a \ge -e^a$ . This lower bound implies also an upper bound, by using equation (6) applied with some  $q \in \Delta^1 \subset \Delta^n$ , since  $0 < \epsilon \le q_i \le 1$  uniformly in  $i$ . This establishes existence of equilibrium. To ensure uniqueness of equilibrium, a sufficient condition is that all agents' risk aversions are less than or equal to 1, that is  $\gamma^a \in (0, 1]$  for all a, see [2].

For multiple consumption goods, the above ideas generalize if one considers consumption bundles and state-contingent claims of every good. Arrow [1] showed that in the case of multiple consumption goods, all possible consumption allocations are spanned if agents could trade as securities solely state-contingent claims on the unit of account (socalled Arrow securities), provided that spot markets with anticipated prices for all other goods exists in all future states. In the sequel, we only deal with Arrow securities in financial models with a single numeraire good that serves as unit of account, and could for simplicity be considered as money ("euro"). If the set of outcomes  $\Omega$  were (uncountably) infinite, the natural notion of atomic securities is lost, although a state price density (stochastic discount factor, deflator) may still exist, which could be interpreted intuitively as an Arrow-Debreu state price per unit probability.

## **Multiple Period Extension and No-arbitrage Implications**

The one-period setting with finitely many states is easily extended to finitely many periods with dates  $t \in \{0, \ldots, T\}$  by considering an enlarged state space of suitable date-event pairs (see Chapter 7 in  $[3]$ ). To this end, it is mathematically convenient to describe the information flow by a filtration  $(\mathcal{F}_t)$  that is generated by a stochastic process  $X = (X_t(\omega))_{0 \le t \le T}$ (abstract, at this stage) on the finite probability space  $(\Omega, \mathcal{F}, P_0)$ . Let  $\mathcal{F}_0$  be trivial,  $\mathcal{F}_T = \mathcal{F} = 2^{\Omega}$ , and assume  $P_0(\{\omega\}) > 0$ ,  $\omega \in \Omega$ . The  $\sigma$ -field  $\mathcal{F}_t$ contains all events that are based on information from observing paths of  $X$  up to time  $t$ , and is defined by a partition of  $\Omega$ . The smallest nonempty events in  $\mathcal{F}_t$  are "*t*-atomic" events  $A \in \mathcal{A}_t$  of the type  $A = [x_0 \cdots x_t] := \{X_0 = x_0, \ldots, X_t = x_t\}$ , and constitute a partition of  $\Omega$ . Figure 1 illustrates the partitions  $\mathcal{A}_t$  corresponding to the filtration  $(\mathcal{F}_t)_{t=0,1,2}$ in a five-element space  $\Omega$ , as generated by a process  $X_t$  taking values  $a, \ldots, f$ . It shows that a filtration can be represented by a nonrecombining tree. There are eight (atomic) date-event pairs  $(t, A)$ ,  $A \in \mathcal{A}_t$ . An adapted process  $(c_t)_{t>0}$ , describing, for instance, a consumption allocation, has the property that  $c_t$  is constant on each atom A of partition  $\mathcal{A}_t$ , and hence is determined by specifying its value  $c_t(A)$  at each node point  $A \in \mathcal{A}_t$  of the tree. Arrow–Debreu prices

![](_page_2_Figure_1.jpeg)

**Figure 1** Equivalent representations of the multiperiod case. (a) Tree of the filtration generating process  $X_t$ . (b) Partitions  $\mathcal{A}_t$  of filtration  $(\mathcal{F}_t)_{t=0,1,2}$ 

 $q(t, A)$  are specified for each node of the tree and represent the value at time 0 of one unit of account at date *t* in node  $A \in \mathcal{A}_t$ .

Technically, this is easily embedded in the previous single-period setting by passing to an extended space  $\Omega' := \{1, \dots T\} \times \Omega$  with  $\sigma$ -field  $\mathcal{F}'$  generated by all sets  $\{t\} \times A$  with A being an (atomic) event of  $\mathcal{F}_t$ , and  $P'_0(\{t\} \times A) := \mu(t) P_0(A)$  for a (strictly positive) probability measure  $\mu$  on  $\{1, \ldots T\}$ .

For the common no-arbitrage pricing approach in finance, the focus is to price contingent claims solely in relation to prices of other claims, that are taken as exogenously given. In doing so, the aim of the model shifts from the fundamental economic equilibrium task to explain all prices, toward a "financial engineering" task to determine prices from already given other prices solely by no-arbitrage conditions, which are a necessary prerequisite for equilibrium. From this point of view, the (atomic) Arrow–Debreu securities span a *complete market*, as every contingent payoff c, paying  $c_t(A)$  at time t in atomic event  $A \in \mathcal{A}_t$ , can be decomposed by  $c = \sum_{t, A \in \mathcal{A}_t} c_t(A) 1_{(t, A)}$  into a portfolio of atomic Arrow securities, paying one euro at date  $t$  in event  $A$ . Hence the no-arbitrage price of the claim must be  $\sum_{t,A\in\mathcal{A}_t} c_t(A)q(t,A)$ . Given that all atomic Arrow-Debreu securities are traded at initial time 0, the market is statically complete in that any statecontingent cash flow  $c$  can be *replicated* by a portfolio of Arrow–Debreu securities that is formed *statically* at initial time, without the need for any dynamic trading. The no-arbitrage price for  $c$  simply equals the cost of replication by Arrow-Debreu securities. It is easy to check that, if all prices are determined

like this and trading takes place only at time 0, the market is free of arbitrage, given all Arrow-Debreu prices are strictly positive. To give some examples, the price at time  $0$  of a zero coupon bond paying one euro at date t equals  $ZCB^t = \sum_{A \in \mathcal{A}_t} q(t, A)$ . For the absence of arbitrage, the *t*-forward prices  $q^{f}(t, A'), A' \in \mathcal{A}_{t}$ , must be related to spot prices of Arrow-Debreu securities by

$$q^{f}(t, A') = \frac{q(t, A')}{\sum_{A \in \mathcal{A}_{t}} q(t, A)}$$
$$= \frac{1}{ZCB^{t}} q(t, A'), \quad A' \in \mathcal{A}_{t} \qquad (7)$$

Hence, the forward prices  $q^{f}(t, A')$  are normalized Arrow-Debreu prices and constitute a probability measure  $Q^t$  on  $\mathcal{F}_t$ , which is the *t*-forward *measure* associated to the  $t - ZCB$  as numeraire, and yields  $q^f(t, A) = E^t[1_A]$  for  $A \in \mathcal{A}_t$ , with  $E^t$ denoting expectation under  $Q^t$ . Below, we also consider "non-atomic" state-contingent claims with payoffs  $c_k(\omega) = 1_{(t,B)}(k,\omega), k \leq T$ , for  $B \in \mathcal{F}_t$ , whose Arrow-Debreu prices are denoted by  $q(t, B) =$  $\sum_{A\in\mathcal{A}\cup A\subset B} q(t,A).$ 

### Arrow–Debreu Prices in Dynamic **Arbitrage-free Markets**

In the above setting, information is revealed dynamically over time, but trading decisions are static in that they are entirely made at initial time 0. To discuss relations between initial and intertemporal Arrow-Debreu prices in arbitrage-free models with dynamic trading, this section extends the above setting, assuming that all Arrow-Debreu securities are tradable dynamically over time.

Let  $q_s(t, A_t)$ ,  $s \le t$ , denote the price process of the Arrow-Debreu security paying one euro at  $t$  in state  $A_t \in \mathcal{A}_t$ . At maturity  $t$ ,  $q_t(t, A_t) = 1_{A_t}$  takes value 1 on  $A_t$  and is 0 otherwise. For the absence of arbitrage, it is clearly necessary that Arrow-Debreu prices are nonnegative, and that  $q_s(t, A_t)(A_s) > 0$ holds for  $s < t$  at  $A_s \in \mathcal{A}_s$  if and only if  $A_s \supset A_t$ . Further, for  $s < t$  it must hold that

$$q_s(t, A_t)(A_s) = q_s(s+1, A_{s+1})(A_s)$$
$$\times q_{s+1}(t, A_t)(A_{s+1}) \qquad (8)$$

for  $A_s \in \mathcal{A}_s$ ,  $A_{s+1} \in \mathcal{A}_{s+1}$  such that  $A_s \supset A_{s+1} \supset A_t$ . In fact, the above conditions are also sufficient to ensure that the market model is free of arbitrage: At any date  $t$ , the Arrow-Debreu prices for the next date define the interest rate  $R_{t+1}$  for the next period  $(t, t + 1)$  of length  $\Delta t > 0$  of a savings account  $B_t = \exp(\sum_{s=1}^t R_s \Delta t)$  by

$$\exp(-R_{t+1}(A_t)\Delta t) = \sum_{A_{t+1}\in\mathcal{A}_{t+1}(A_t), A_{t+1}\subset A_t} q_t(t+1, A_{t+1}),$$
  
for  $A_t \in \mathcal{A}_t$  (9)

which is locally riskless, in that  $R_{t+1}$  is known at time t, that means it is  $\mathcal{F}_t$ -measurable. They define an equivalent risk neutral probability  $Q^B$  by determining its transition probabilities from any  $A_t \in$  $\mathcal{A}_t$  to  $A_{t+1} \in \mathcal{A}_{t+1}$  with  $A_t \supset A_{t+1}$  as

$$Q^{B}(A_{t+1}|A_{t}) = \frac{q_{t}(t+1, A_{t+1})(A_{t})}{\sum_{A \in \mathcal{A}_{t+1}, A \subset A_{t}} q_{t}(t+1, A)(A_{t})} \quad (10)$$

The transition probability  $(10)$  can be interpreted as one-period forward price when being at  $A_t$  at time t, for one euro at date  $t + 1$  in event  $A_{t+1}$ , cf. (7). Since all B-discounted Arrow-Debreu price processes  $q_s(t, A_t)/B_s$ ,  $s \le t$ , are martingales under  $Q^B$  thanks to equations (8, 10), the model is free of arbitrage by the fundamental theorem of asset pricing, see [6]. For initial Arrow-Debreu prices, denoted

by  $q_0(t, A_t) \equiv q(t, A_t)$ , the martingale property and equations  $(8, 10)$  imply that

$$q(t+1, A_{t+1}) = e^{-R_{t+1}(A_t)\Delta t} Q^B(A_{t+1}|A_t)q(t, A_t)$$
(11)

Hence  $q(t, A_t) = Q^B(A_t)/B_t(A_t)$  for  $A_t \in \mathcal{A}_t$ .

The *deflator* or *state price density* for agent  $a$  is the adapted process  $\zeta^a$  defined by

$$\zeta_t^a(A_t) := \frac{q(t, A_t)}{P^a(A_t)} = \frac{Q^B(A_t)}{B_t(A_t)P^a(A_t)}, \quad A_t \in \mathcal{A}_t \tag{12}$$

so that  $\zeta_t^a S_t$  is a  $P^a$ -martingale for any security price process S, e.g.  $S_t = q_t(T, A_T), t \leq T$ , with  $A_T \in$  $\mathcal{A}_T$ . If one chooses, instead of  $B_t$ , another security  $N_t = \sum_{A_T \in \mathcal{A}_T} N_T(A_T) q_t(T, A_T)$  with  $N_T > 0$  as the numeraire asset for discounting, one can define an equivalent measure  $O^N$  by

$$\frac{Q^N(A)}{P^a(A)} = \frac{N_T(A)}{N_0(A)} \zeta_T^a(A) \,, \quad A \in \mathcal{A}_T \tag{13}$$

which has the property that  $S_t/N_t$  is a  $Q^N$ -martingale for any security price process S. Taking  $N =$  $(ZCB_t^T)_{t \leq T}$  as the T-zero-coupon bond yields the Tforward measure  $Q^T$ .

If X is a  $Q^B$ -Markov process, the conditional probability  $Q^B(A_{t+1}|A_t)$  in equation (11) is a transition probability  $p_t(x_{t+1}|x_t) := Q^B(X_{t+1} =$  $x_{t+1}|X_t = x_t$ , where  $A_k = [x_1 \dots x_k]$  for  $k = t$ ,  $t + 1$ . By summation of suitable atomic events

$$q(t+1, X_{t+1} = x_{t+1})$$
  
=  $\sum_{x_t} e^{-R(x_t)\Delta t} p_t(x_{t+1}|x_t)q(t, X_t = x_t)$   
(14)

where the sum is over all  $x_t$  from the range of  $X_t$ .

#### Application Examples: Calibration of **Pricing Models**

The role of Arrow-Debreu securities as "atomic building blocks" is theoretical, in that there exist no corresponding securities in real financial markets. Nonetheless, they are of practical use in the calibration of pricing models. For this section,  $X$  is taken to be a  $Q^B$ -Markov process, possibly timeinhomogeneous.

The first example concerns the calibration of a short rate model to some given term structure of zero coupon prices  $(ZCB_t)_{t \leq T}$ , implied by market quotes. For such models, a common calibration procedure relies on a suitable time-dependent shift of the state space for the short rate (see [7], Chapter 28.7). Let suitable functions  $R^*$  be given such that the variations of  $R_t^*(X_t)$  already reflect the desired volatility and mean-reversion behavior of the (discretized) short rate. Making an ansatz  $R_t(X_t) := R_t^*(X_t) + \alpha_t$  for the short rate, the calibration task is to determine the parameters  $\alpha_t$ ,  $1 \le t \le T$ , such that

$$ZCB_t = E^B \left[ \exp \left( -\sum_{k \le t} (R_k^*(X_k) + \alpha_k) \Delta t \right) \right]$$
(15)

with the expectation being taken under the risk neutral measure  $Q^B$ . It is obvious that this determines all the  $\alpha_t$  uniquely. When computing this expectation to obtain the  $\alpha_t$  by forward induction, it is efficient to use Arrow-Debreu prices  $q(t, X_t = x_t)$ , since X usually can be implemented by a recombining tree. Summing over the range of states  $x_t$  of  $X_t$  is more efficient than summing over all paths of  $X$ . Suppose that  $\alpha_k, k < t$ , and  $q(t, X_t = x_t)$  for all values  $x_t$  have been computed already. Using equation  $(14)$ , one can then compute  $\alpha_{t+1}$  from equation

$$ZCB_{t+1} = \sum_{x_{t+1}} \sum_{x_t} q(t, X_t = x_t)$$
$$\times e^{(R_{t+1}^*(x_t) + \alpha_{t+1})\Delta t} p_t(x_{t+1} | x_t) \quad (16)$$

where the number of summand in the double sum is typically bounded or grows at most linearly in  $t$ . Then Arrow-Debreu prices  $q(t + 1, X_{t+1} = x_{t+1})$  for the next date  $t+1$  are computed using equation (14), while those for  $t$  can be discarded.

The second example concerns the calibration to an implied volatility surface. Let  $X$  denote the discounted stock price  $X_t = S_t \exp(-rt)$  in a trinomial tree model with constant interest  $R_t := r$  and  $\Delta t = 1$ . Each  $X_{t+1}/X_t$  can attain three possible values  $\{m, u, d\} := \{1, e^{\pm \sigma \sqrt{2}}\}$  with positive probability, for  $\sigma > 0$ . The example is motivated by the task to calibrate the model to given prices of European calls and puts by a suitably choice of the (nonunique) risk neutral Markov transition probabilities for  $X_t$ . We focus here on the main step for this task, which is to show that the Arrow-Debreu

prices of all state-contingent claims, which pay one unit at some t if  $X_t = x_t$  for some  $x_t$ , already determine the risk neutral transition probabilities of  $X$ . It is easy to see that these prices are determined by those of calls and puts for sufficiently many strikes and maturities. Indeed, strikes at all tree levels of the stock for each maturity date  $t$  are sufficient, since Arrow–Debreu payoffs are equal to those of suitable butterfly options that are combinations of such calls and puts. From given Arrow-Debreu prices  $q(t, X_t = x_t)$  for all  $t, x_t$ , the transition probabilities  $p_t(x_{t+1}|x_t)$  are computed as follows: starting from the highest stock level  $x_t$  at some date t, one obtains  $p_t(x_t u|x_t)$  by equation (14) with  $R_t(x_t) = r$  and  $\Delta t = 1$ . The remaining transition probabilities  $p_t(x_t m|x_t)$ ,  $p_t(x_t d|x_t)$  from  $(t, x_t)$  are determined from

$$p_t(x_tu|x_t)u + p_t(x_tm|x_t)m + p_t(x_td|x_t)d = 1$$
(17)

and  $p_t(x_tu|x_t) + p_t(x_tm|x_t) + p_t(x_td|x_t) = 1$ . Using these results, the transition probabilities from the second highest (and subsequent) stock level(s) are implied by equation  $(14)$  in a similar way. This yields all transition probabilities for any  $t$ .

To apply this in practice, the call and put prices for the maturities and strikes required would be obtained from real market quotes, using suitable interpolation, and the trinomial state space (i.e.,  $\sigma$ , r,  $\Delta t$ ) has to be chosen appropriately to ensure positivity of all  $p_t$ , see [4, 5].

#### References

- [1] Arrow, K.J. (1964). The role of securities in the optimal allocation of risk-bearing, As translated and reprinted in 1964, Review of Financial Studies 31, 91-96.
- [2] Dana, R.A. (1993). Existence and uniqueness of equilibria when preferences are additively separable, *Econometrica* 61, 953-957.
- Debreu, G. (1959). Theory of Value: An Axiomatic Analysis of Economic Equilibrium, Yale University Press, New Haven.
- [4] Derman, E., Kani, I. & Chriss, N. (1996). Implied trinomial trees of the volatility smile, Journal of Derivatives 3, 7-22.
- [5] Dupire, B. (1997). Pricing and hedging with smiles, in Mathematics of Derivative Securities, M.A.H. Dempster & S.R. Pliska, eds, Cambridge University Press, Cambridge, pp. 227–254.

- [6] Harrison, J. & Kreps, D. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **20**, 381–408.
- [7] Hull, J. (2006). *Options, Futures and Other Derivative Securities*, Prentice Hall, Upper Saddle River, New Jersey.
- [8] Mas-Colell, A., Whinston, M.D. & Green, J.R. (1995). *Microeconomic Theory*, Oxford University Press, Oxford.

**Related Articles**

**Arrow, Kenneth**; **Complete Markets**; **Dupire Equation**; **Fundamental Theorem of Asset Pricing**; **Model Calibration**; **Pricing Kernels**; **Risk-neutral Pricing**; **Stochastic Discount Factors**.

DIRK BECHERER & MARK H.A. DAVIS
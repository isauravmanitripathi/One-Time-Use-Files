# **Transaction Costs**

Standard models for financial markets are based on the simplifying assumption that trading orders can be given and executed in continuous time with no friction. This assumption is clearly a strong idealization of the reality. In particular, securities should not be described by a single price but by a bid and ask curve. As a first approximation, one may assume that the bid and ask prices do not depend on the traded quantities, which leads to models with proportional transaction costs. These models have attracted a lot of attentions these last years, mostly because their linear structure allows to develop a nice duality theory as in frictionless models.

#### No Arbitrage with Proportional Costs

#### The Fictitious Markets Approach in the One-dimensional Case

The study of models with proportional transaction costs starts with the paper of Jouini and Kallal [22] who considered a financial market with one nonrisky asset  $S^1$ , taken as a numéraire and normalized to 1, and one risky asset called  $S^2$ .

To be consistent with the developments below, we use a different (but equivalent) presentation that the one used in [22]. In particular, we denote by  $\pi^{ij}$  the number of physical units of asset  $i$  for which an agent can buy 1 unit of asset  $j$ . With these notations, the bid and ask prices of  $S^2$  in terms of  $S^1$  are given by  $1/\pi^{21}$ and  $\pi^{12}$ . They are assumed to be right-continuous and adapted to the underlying (right-continuous) filtration  $(\mathcal{F}_t)_{t\leq T}.$ 

In this model, simple self-financing trading strategies are defined as finite sequences of trading times  $(t_n)_{n \leq N}$ , for some  $N \geq 1$ , and random vectors of traded quantities  $(\xi_{t_n})_{n\leq N}$  such that  $\xi_{t_n}$  is  $\mathcal{F}_{t_n}$ measurable. The *i*-th component  $\xi_{t_n}^i$  of  $\xi_{t_n}$  stands for the number of physical units of  $S^i$  bought at the times  $t_n$ . In this framework, the usual self-financing condition reads  $\xi_{t_n}^1 - (\xi_{t_n}^2)^+ \pi_{t_n}^{12} + (\xi_{t_n}^2)^- / \pi_{t_n}^{21} \le 0$  for each  $n \le N$ . The associated portfolio starting with a zero initial holding is described as a two-dimensional process  $V_t^{\xi} = \sum_{t_n \leq t} \xi_{t_n}$  whose *i*-th component is the numbers of units of  $S^i$  held.

The key observation of Jouini and Kallal [22] is the following: if  $\tilde{Z}^2$  is a process such that  $\tilde{Z}_t^2 \in$  $[1/\pi_t^{21}, \pi_t^{12}]$  a.s. (almost surely for all  $t \leq T$ , then the liquidation value at time T of the portfolio,  $\ell(V_T^{\xi})$  :=  $V_T^{\xi,1} - (V_T^{\xi,2})^- \pi_T^{12} + (V_T^{\xi,2})^+ / \pi_T^{21}, \text{ is a.s. lower than}$ <br>the terminal value  $\tilde{V}_T^{\xi} := \sum_{t_n \leq T} \xi_{t_n}^2 (\tilde{Z}_{t_{n+1} \wedge T}^2 - \tilde{Z}_{t_n}^2)$ associated to the same strategy in a *fictitious market* in which the risky asset has the dynamics  $\tilde{Z}^2$  and where there is no transaction costs. In particular, if there is an equivalent measure  $\mathbb Q$  such that  $\tilde Z^2$  is a martingale, then no arbitrage (NA) is possible:  $\ell(V_T^{\xi}) \in L^0(\mathbb{R}_+) \Rightarrow \tilde{V}_T^{\xi} \in L^0(\mathbb{R}_+) \Rightarrow \tilde{V}_T^{\xi} = 0 \Rightarrow \ell(V_T^{\xi}) = 0.$ Thus, the existence of such a process  $\tilde{Z}^2$ , called *fic*titious price process, admitting an equivalent martingale measure is a sufficient condition for the absence of arbitrage in this model.

The fundamental result in [22] is that this condition is actually also necessary, whenever we replace the notion of NA by that of no free lunch; see the above paper for a precise definition.

As an example, let us consider the case where  $1/\pi^{21} = (1 - \lambda)S^2$  and  $\pi^{12} = (1 + \lambda)S^2$  where  $S^2$  is now viewed as a right-continuous adapted process and  $\lambda \in (0, 1)$ . Then, a necessary and sufficient condition for the absence of *free lunch* for simple strategies is that there exists a process  $\tilde{Z}^2$  such that  $\tilde{Z}_t^2 \in [(1-\lambda)S_t^2, (1+\lambda)S_t^2]$  a.s. for all  $t \leq T$ and which is a martingale under some equivalent measure  $\mathbb{O}$ . An important consequence of this result is that  $S^2$  itself need not admit a martingale measure nor be a semimartingale under the original probability measure. One could, for instance, allow  $S^2$  to be a fractional Brownian motion as in [16].

#### The Multivariate Case: The Solvency Region and Its Polar

In the multivariate setting where direct exchanges between many assets is possible, which is typically the case on currency markets, a similar reasoning can be used, and the geometric structure of the problem is more apparent. In particular, the notion of *solvency* region, introduced by Kabanov [29], and its positive polar play an important role.

The solvency region at time t is the set  $K_t(\omega)$ formed by all vectors  $x$  such that we can find nonnegative numbers  $a^{ij}$  satisfying  $x^i + \sum_i (a^{ji}$  $a^{ij}\pi^{ij}_{t}(\omega) \geq 0$ . It corresponds to positions, which can be transformed into nonnegative holdings after suitable exchanges. A portfolio process, in units of physical quantities, is defined in [29] as a cadlad bounded variation process V satisfying  $dV_t \in -K_t$ . This means that there is a matrix-valued cadlag adapted process  $L$ , with nondecreasing components, such that  $dV_t = \sum_i (dL_t^{ji} - dL_t^{ij} \pi_t^{ij})$ , that is,  $dL^{ij}$ is the number of units of asset  $j$  obtained by selling  $dL_t^{ij}\pi_t^{ij}$  units of asset *i*.

In this model, a strategy is said to be admissible if the following *no-bankruptcy* condition holds:  $V_t$  –  $a1 \in K_t$  a.s. for some real number a with  $1 :=$  $(1, \ldots, 1)$ . This means that the *liquidation value* of the portfolio is bounded from below by  $a$ .

The counterpart of the key observation of Jouini and Kallal [22] is the following. Let  $Z$  be a continuous martingale with positive components such that  $Z_t$ takes values in the positive polar  $K_t^*$  of  $K_t$ :  $K_t^*(\omega) :=$  $\{z \in \mathbb{R}^d : 0 \leq z^i \leq z^j \pi_t^{ji}(\omega)\}$ . Then, by the integration by parts formula,  $Z_t \cdot V_t = \sum_i Z_t^i dV_t^i + V_t^i dZ_t^i$ . The first part is nonpositive because  $Z_t \in K^*_t$  and  $dV_t \in -K_t$ , the second part is a local martingale, and  $Z \cdot V$  is bounded from below by the martingale  $aZ$ . This implies that  $Z \cdot V$  is a supermartingale, which rules out any arbitrage opportunities:  $V_T \in L^0(K_T) \Rightarrow Z_T \cdot V_T \in L^0(\mathbb{R}_+) \Rightarrow Z_T \cdot V_T$  $V_T = 0 \Rightarrow V_T \in L^0(\partial K_T)$ . Otherwise stated, if the liquidation value of the portfolio is nonnegative a.s., then it must be equal to  $0$ .

As in [22], the process  $Z$  has a nice interpretation in terms of *fictitious price process*. Indeed, if we set  $Z^i = Z^i/(Z^1/\mathbb{E}[Z_T^1])$ , we see that the above conditions imply that the *fictitious market*, without transaction costs and where the dynamics of the *i*-th asset is given  $\tilde{Z}^i$ , is *cheaper* than the original one  $(\tilde{Z}^i/\tilde{Z}^j \in [1/\pi^{ij}, \pi^{ji}])$  and admits no arbitrage (there is at least one martingale measure  $\mathbb{Q} := Z_T^1 / \mathbb{E}[Z_T^1]$ .  $\mathbb{P}$  for  $\tilde{Z}$ ). See [7] for a precise statement.

Note that in this model no asset has been taken explicitly as a numéraire, except in the last interpretation in terms of *fictitious markets*. It turns out that, when working with quantities instead of amounts, as in usual frictionless models, the only important quantity is the bid-ask spread process  $\pi = (\pi^{ij})$ , which directly expresses the exchange rates between two assets.

#### No-arbitrage Conditions

Different notions of NA have been proposed for discrete time multivariate models. In the following,

we denote by  $A_T$  the set of terminal values of portfolios starting from 0.

1. The usual NA condition can be written as  $A_T \cap$  $L^0(K_T) = L^0(\partial K_T)$  (see above). It was studied in [32] and called weak no arbitrage condi*tion*therein. When the probability space is finite, it is equivalent to the existence of a martingale Z such that  $Z_t$  takes values in  $K_t^* - \{0\}$  for all  $t \leq T$  a.s. We therefore retrieve the process Z required for the NA condition in [29]. Moreover, this condition implies that  $A_T$  is closed in probability, a desirable feature to build on a nice duality for the set of superhedgeable claims (see below). Such a process  $Z$  was called a *consistent* price system in [36]. The notion of consistency reflects the fact that the exchange rates corresponding to the induced frictionless market (see above) lie within the original bid-ask spreads:  $\tilde{Z}^i/\tilde{Z}^j \in [1/\pi^{ij}, \pi^{ji}].$ 

However, this condition is not strong enough when  $\Omega$  is not finite (see [36]). This leads to the introduction of a second notion of NA.

The strict NA condition  $(NA<sup>s</sup>)$  introduced in 2. [31] reads as follows:  $A_t \cap L^0(K_t) = L^0(K_t^0)$ for all  $t \leq T$ . Here,  $K_t^0 := K_t \cap (-K_t) (= \partial K_t \cap$  $(-\partial K_t)$ ). The economic interpretation is that, if a wealth process  $V$  starting from a zero initial endowment has a nonnegative liquidation value at any time, then it is *equivalent* to 0, that is, its liquidation value is  $0(V_t \in \partial K_t)$  and it can be constructed from a 0 endowment at time  $t$  by a suitable immediate exchange on the market  $(V_t \in$  $-\partial K_t$ ). Under the *efficient friction* condition,  $1/\pi^{ij} < \pi^{ji}$  for all  $i \neq j$ , which means that no couple of assets can be exchanged freely and can be written as  $K_t^0 = \{0\}$ , this condition is equivalent to the existence of a martingale  $Z$ which lies in the relative interior  $\text{ri}K^*$  of  $K^*$ , that is,  $Z^{i}/Z^{j} \in \text{ri}[1/\pi^{ij}, \pi^{ji}]$ . Moreover, it implies that  $A_T$  is closed in probability. Such a process  $Z$  is called a *strictly consistent price system*.

This last notion of NA is sufficient to cover the cases where the transaction costs are strictly positive. However, up to the slight (also interesting) extension proposed  $[35]$ , it does not allow to show that  $A_T$  is closed or to construct a consistent price system in general without the extra efficient friction condition, see the counterexample in  $[36]$ .

- 3. The last notion was proposed in [36]. It is based on the idea that if a martingale  $Z$  satisfies the condition  $Z^i/Z^j \in \text{ri} \ [1/\pi^{ij}, \pi^{ji}],$  then one can construct a bid-ask spread matrix  $\bar{\pi}$  defined by  $\bar{\pi}^{ji} := Z^i/Z^j$ , which leads to a market without arbitrage, because  $Z$  is a martingale, and satisfies  $[1/\bar{\pi}^{ij}, \bar{\pi}^{ji}] \subset \text{ri}[1/\pi^{ij}, \pi^{ji}]$  by construction. Thus, the existence of a strictly consistent *price system* implies a strong notion of NA: there exists a market associated to a bid-ask spread matrix  $\bar{\pi}$  satisfying  $[1/\bar{\pi}^{ij}, \bar{\pi}^{ji}] \subset \text{ri}[1/\pi^{ij}, \pi^{ji}]$ in which there is no arbitrage. Otherwise stated, one can slightly reduce the transaction costs, when they are not already equal to 0, and still preserve the NA condition. This condition was called the *robust NA* condition  $(NA^r)$  in [36]. The main result of this article is that this condition is sufficient to ensure that  $A_T$  is closed in probability and is actually equivalent to the existence of a *strictly consistent price system*. This is the good condition to impose on a model:
  - It is equivalent to the existence of a *strictly* (a) consistent price system without any extra assumption.
  - When there is no friction, that is,  $1/\pi^{ij}$  = (b)  $\pi^{ji}$  for all *i*, *j*, it is equivalent to the usual no-abritrage condition in frictionless markets.
  - Similar notions can be used to study mod-(c) els with nonlinear frictions (see  $[5]$ ).
  - It can be extended to continuous-time mod-(d) els in the following form: the absence of arbitrage opportunities for arbitrary small transaction costs is equivalent to the existence of a strictly consistent price system for arbitrary small transaction costs. This result was proved in a model with only one risky asset with continuous paths in  $[17]$ . The existence of a *strictly consistent* price system for arbitrarily small transaction costs in a multivariate market with continuous price processes is a result of [18].

## Superhedging and No-arbitrage Price Intervals

When there are transaction costs, we generally have more than one fictitious price process and more than one martingale measure  $\mathbb{Q}$  satisfying the conditions above. Furthermore, as underlined in [1], even if a contingent claim  $G$  can be duplicated by dynamic trading, the duplication strategy does not necessarily correspond to the cheapest way to hedge this claim. They thus introduced the concept of *super-replication price*  $\pi(G)$  that corresponds to the minimum amount it costs to hedge the claim  $G$  (in terms of the first asset taken as a numéraire).

As first shown in [11] and [22], it can be obtained by taking the (normalized) expected value of  $\tilde{Z}_T \cdot G$ with respect to all the *fictitious markets*  $\tilde{Z}$  and all measures  $\mathbb{Q}$  that characterize the absence of arbitrage opportunities in the corresponding *fictitious market*. Here,  $G$  is viewed as the vector of units of the different assets to be delivered. This result can easily be understood in the light of the above discussion. If  $V_T - G \in K_T$ , then  $\tilde{Z}_T \cdot V_T \geq \tilde{Z}_T \cdot G$ . Since  $\tilde{Z} \cdot V$ is a  $\mathbb{Q}$ -supermartingale (see above) it follows that  $\tilde{Z}_0 \cdot V_0 \geq \mathbb{E}^{\mathbb{Q}}[\tilde{Z}_T \cdot G]$ . The converse implication is obtained by using a standard separation argument, once  $A_T$  is known to be closed in a suitable sense.

The no-arbitrage prices interval is then equal to  $[-\pi(-G), \pi(G)]$ . Using the viability concept for price systems introduced in [20], the paper [23] also proves that these bounds are the tightest bounds that can be inferred at the equilibrium on the price of a contingent claim without knowing the agent's preferences (see also  $[21]$ ). This is still the case even if we assume that agents have von Neumann-Morgenstern  $(VNM)$  preferences [24]. In particular, this means that even if the super-replication price seems too high (see below) it is always possible to construct VNM agents that are willing to pay amounts arbitrarily close to this super-replication price in order to hedge the considered asset (see also [4]).

Since endowments in different assets are not equivalent in the presence of transaction costs, it is also of interest to extend the notion of *superhedging price* to that of *initial endowments*  $x \in \mathbb{R}^d$  *that* allow to superhedge. In this case, the above dual formulation reads  $\tilde{Z}_0 \cdot x \geq \mathbb{E}^{\mathbb{Q}}[\tilde{Z}_T \cdot G]$  for all the fictitious markets  $\tilde{Z}$  and all associated martingale measures  $\mathbb{Q}$  (see [32] and [8]). It can be restated in terms of consistent price systems:  $Z_0 \cdot x \geq \mathbb{E}[Z_T \cdot G]$ for all *consistence price systems*  $Z$ .

The case of American options can be treated similarly. However, it is not sufficient to impose the above condition at any stopping time lower than  $T$  as in frictionless markets. This is due to the absence of total order on *d* . To overcome this problem, one has to relax the notion of stopping times and consider the more general notion of *randomized* stopping times. See [6] and [10] for discrete time models, and, [3] and [15] for a continuous-time extension.

The notion that *superhedging* typically leads to much too high prices to be useful in the market (it usually corresponds to a buy-and-hold strategy) was first conjectured in [13] for call options and then proved by different authors at different level of generality; see [7] and the reference therein.

## **Utility Maximization**

Thanks to the above-mentioned duality between superhedgeable claims and consistence price systems, existence of optimal strategies can be obtained for general models with transaction costs. The first general result was derived by Cvitani'c and Karatzas [11] in a Brownian diffusion model and then extended by Cvitani'c and Wang [12] to the semimartingale case. The general multivariate case was studied in [2] and [14] under *Asymptotic Elasticity* conditions similar to the one introduced in [33]; see [19] for the necessity of this condition in models with proportional transaction costs. All these papers show that the usual duality holds once we replace the notion of *equivalent local martingale measures* by that of *consistent price systems*.

In Markovian diffusion models, the partial differential equation (PDE) approach has also attracted a lot of attention. It leads to the Hamilton–Jacobi– Bellman (HJB) equations involving constraints on the gradients of the value function. It allows to show that the optimal strategy typically consists in maintaining the dotations in a given *no-trading region*. See, for example, [30, 37] and the references therein.

## **Extensions**

In order to take a large set of possible frictions including multivariate transaction costs into account, one can follow the approach of [9] (in discrete time) and [26] and [28] (in continuous time), where it is proposed to deal directly with the space of possible cash flows, instead of the space of terminal payoffs, and provide a characterization of the no free-lunch assumption in terms of the existence of a separating functional. In particular, Napp [34] develops an arbitrage pricing theory and a superreplication concept in this cash-flow space.

The case of fixed transaction costs is analyzed in [25] and [27]. The conclusion drawn is that the absence of free lunch is characterized by the existence of a (family of) martingale measure(s) for the frictionless price processes. The unique difference with the frictionless case consists in the fact that these martingale measures are not necessarily equivalent to the initial probability but only absolutely continuous with respect to it.

## **References**

- [1] Bensaid, B., Lesne, J.-P., Pages, H. & Scheinkman, J. ` (1992). Derivative asset pricing with transaction costs, *Mathematical Finance* **2**, 63–86.
- [2] Bouchard, B. (2002). Utility maximization on the real line under proportional transaction costs, *Finance and Stochastics* **6**(4), 495–516.
- [3] Bouchard, B. & Chassagneux, J.-F. (2009). Representation of continuous linear forms on the set of ladlag processes and the pricing of American claims under proportional costs, *Electronic Journal of Probability* **14**, 612–632.
- [4] Bouchard, B., Kabanov, Y. & Touzi, N. (2001). Option pricing by large risk aversion utility under transaction costs, *Decisions in Economics and Finance* **24**, 127–136.
- [5] Bouchard, B. & Pham, H. (2005). Optimal consumption in discrete time financial models with industrial investment opportunities and non-linear returns, *Annals of Applied Probability* **15**(4), 2393–2421.
- [6] Bouchard, B. & Temam, E. (2005). On the hedging of american options in discrete time markets with proportional transaction costs, *Electronic Journal of Probability* **10**, 746–760.
- [7] Bouchard, B. & Touzi, N. (2000). Explicit solution of the multivariate super-replication problem under transaction costs, *Annals of Applied Probability* **10**, 685–708.
- [8] Campi, L. & Schachermayer, W. (2006). A superreplication theorem in Kabanov's model of transaction costs, *Finance and Stochastics* **10**(4), 579–596.
- [9] Carassus, L. & Jouini, E. (2000). A discrete stochastic model for investment with an application to the transaction costs case, *Journal of Mathematical Economics* **33**, 57–80.
- [10] Chalasani, P. & Jha, S. (2001). Randomized stopping times and american option pricing with transaction costs, *Mathematical Finance* **11**(1), 33–77.
- [11] Cvitanic, J. & Karatzas, I. (1996). Hedging and port- ` folio optimization under transaction costs: a martingale approach, *Mathematical Finance* **6**(2), 133–165.

- [12] Cvitanic, J. & Wang, H. (2001). On optimal terminal ` wealth under transaction costs, *Journal of Mathematical Economics* **35**(2), 223–231.
- [13] Davis, M. & Clark, J.M.C. (1994). A note on superreplicating strategies, *Philosophical Transactions of the Royal Society of London A* **347**, 485–494.
- [14] Deelstra, G., Pham, H. & Touzi, N. (2002). Dual formulation of the utility maximization problem under transaction costs, *Annals of Applied Probability* **11**(4), 1353–1383.
- [15] Denis, E., De Valliere, D. & Kabanov, Y. (2009). ` Hedging of American options under transaction costs, *Finance and Stochastics* **13**(1), 105–119.
- [16] Guasoni, P. (2006). No arbitrage with transaction costs, fractional Brownian motion and Markov processes, *Mathematical Finance* **16**(3), 569–582.
- [17] Guasoni, P., Rasonyi, M. & Schachermayer, W. (2007). ´ The fundamental theorem of asset pricing for continuous processes under small transaction costs. *Annals of Finance* Forthcoming.
- [18] Guasoni, P., Rasonyi, M. & Schachermayer, W. (2008). ´ Consistent price systems and face-lifting pricing under transaction costs, *Annals of Applied Probability* **18**(2), 491–520.
- [19] Guasoni, P. & Schachermayer, W. (2004). Necessary conditions for the existence of utility maximizing strategies under transaction costs, *Statistics and Decisions* **22**(2), 153–170.
- [20] Harrison, J. & Kreps, D. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **20**, 381–408.
- [21] Jouini, E. (2000). Price functionals with bid-ask spreads: an axiomatic approach, *Journal of Mathematical Economics* **34**, 547–558.
- [22] Jouini, E. & Kallal, H. (1995). Martingales and arbitrage in securities markets with transaction costs, *Journal of Economic Theory* **66**, 178–197.
- [23] Jouini, E. & Kallal, H. (1999). Viability and equilibrium in securities markets with frictions, *Mathematical Finance* **9**(3), 275–292.
- [24] Jouini, E. & Kallal, H. (2001). Efficient trading strategies in the presence of market frictions, *Review of Financial Studies* **14**, 343–369.
- [25] Jouini, E., Kallal, H. & Napp, C. (2001). Arbitrage and viability in securities markets with fixed trading costs, *Journal of Mathematical Economics* **35**, 197–221.
- [26] Jouini, E. & Napp, C. (2001). Arbitrage and investment opportunities, *Finance and Stochastics* **5**, 305–325.
- [27] Jouini, E. & Napp, C. (2007). Arbitrage with fixed costs and interest rate models, *Journal of Financial and Quantitative Analysis* Forthcoming.

- [28] Jouini, E., Napp, C. & Schachermayer, W. (2005). Arbitrage and state price deflators in a general intertemporal framework, *Journal of Mathematical Economics* **41**, 722–734.
- [29] Kabanov, Y. (1999). Hedging and liquidation under transaction costs in currency market, *Finance and Stochastics* **3**(2), 237–248.
- [30] Kabanov, Y. & Kluppelberg, C. (2004). A geometric approach to portfolio optimization in models with transaction costs, *Finance and Stochastics* **8**, 207–227.
- [31] Kabanov, Y., Rasonyi, M. & Stricker, C. (2002). No ´ arbitrage criteria for financial markets with efficient friction, *Finance and Stochastics* **6**(3), 371–382.
- [32] Kabanov, Y. & Stricker, C. (2001). The Harisson-Pliska arbitrage pricing theorem under transaction costs, *Journal of Mathematical Economics* **35**(2), 185–196.
- [33] Kramkov, D. & Schachermayer, W. (1999). The asymptotic elasticity of utility functions and optimal investment in incomplete markets, *Annals of Applied Probability* **9**, 904–950.
- [34] Napp, C. (2001). Pricing issues with investment flows Applications to market models with frictions, *Journal of Mathematical Economics* **35**, 383–408.
- [35] Penner, I. (2001). *Arbitragefreiheit in Finanzm¨arkten mit Transaktionkosten*. Diplomarbeit, Humboldt-Universitat¨ zu Berlin, Berlin.
- [36] Schachermayer, W. (2004). The fundamental theorem of asset pricing under proportional transaction costs in finite discrete time, *Mathematical Finance*, **14**(1), 19–48.
- [37] Zariphopoulou, T. (1999). Transaction cost in portfolio management and derivative pricing, in *Introduction to Mathematical Finance. Proceedings of Symposia in Applied Mathematicss 57*, D. Heath & R. Swindle, eds, AMS, Providence, RI.

## **Further Reading**

Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing. *Mathematische Annalen*, **300**, 463–520.

# **Related Articles**

**Arbitrage Strategy**; **Bid–Ask Spreads**; **Execution Costs**; **Fundamental Theorem of Asset Pricing**; **Price Impact**; **Superhedging**.

BRUNO BOUCHARD & ELYES JOUINI
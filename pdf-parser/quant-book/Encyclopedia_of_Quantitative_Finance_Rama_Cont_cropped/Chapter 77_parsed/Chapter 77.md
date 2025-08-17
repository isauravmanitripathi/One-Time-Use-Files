# Superhedging

Pricing and hedging of contingent claims are the two main problems of mathematical finance. They both have a clear and transparent solution when the underlying market model is complete, that is, for each contingent claim with promised payoff  $H$  there exists a self-financing admissible trading strategy whose wealth at maturity equals  $H$  (see Complete **Markets**). Such a strategy is called the *hedging* strategy of the contingent claim  $H$ . The smallest initial wealth that allows to reach  $H$  at maturity *via* admissible trading is called the *hedging price* of  $H$ .

Under a suitable no-arbitrage assumption (see Fundamental Theorem of Asset Pricing), the second fundamental theorem of asset pricing (see Second Fundamental Theorem of Asset Pricing) states that replicability of every contingent claim is equivalent to the uniqueness of the equivalent martingale measure  $\mathbb{Q}$  (see Equivalent Martingale Measures).

It turns out that in a complete market (see Com**plete Markets**), the hedging price at time  $t = 0$ of a contingent claim H, denoted by  $p(H)$ , coincides with the expectation of discounted  $H$  under the unique equivalent martingale measure  $\mathbb{Q}$ , that is,  $p(H) = \mathbb{E}_{\mathbb{Q}}[D_T H]$  where  $D_T$  is a discounting factor over  $[0, T]$ .

If the market model is incomplete, there exist contingent claims that are not perfectly replicable *via* admissible trading strategies. In other words, in such financial models, contingent claims are not redundant assets. Therefore, since perfect replicability cannot be always achieved, this requirement has to be relaxed. One way of doing this consists in introducing the concept of *superhedging*.

Given a contingent claim H with maturity  $T > 0$ , a superhedging strategy for  $H$  is an admissible trading strategy such that its terminal wealth  $V_T$  superreplicates H, that is,  $V_T \geq H$ . The superhedging price of  $H$  is the smallest initial endowment that allows an investor to super-replicate  $H$  at maturity; in other words, it is the initial value  $V_0$  of the superhedging strategy of  $H$ .

Superhedging was introduced and investigated first by El Karoui and Quenez [13, 14] in a continuous-time setting where the risky assets follow a multidimensional diffusion process. Independently, Naik and Uppal [25] studied the same problem in a discrete-time model with finite set of scenarios and

noticed that, in the presence of leverage constraints, superhedging may be cheaper than perfect hedging. The same phenomenon has been observed by Benais et al. [1] in the presence of transaction costs.

The characterization of superhedging strategies and prices is the object of a family of results called superhedging theorems.

### **Superhedging Theorems**

A large literature has been devoted to characterizing the set of all initial endowments that allows to superhedge a contingent claim  $H$  as a first crucial step to compute the superhedging price, the infimum of that set. In this article, we focus essentially on continuous-time hedging of European options, that is, with a fixed exercise time  $T$ , and distinguish between two cases: frictionless incomplete markets and markets with frictions. For superhedging in discrete-time models and for American options, the interested reader could see respectively Föllmer and Schied's book [17] and American Options.

#### Frictionless Incomplete Markets

To facilitate the discussion, let us fix the notation first. We consider a market model composed of  $d \ge 1$  risky assets whose discounted price dynamics is described by a càdlàg and locally bounded semimartingale  $S = (S_t)_{t \in [0,T]}$ , where  $T > 0$  is a given finite time horizon. *S* is defined on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ and adapted to a filtration  $(\mathcal{F}_t)_{t \in [0,T]}$  with  $\mathcal{F}_t \subset \mathcal{F}$ for all  $t \leq T$  satisfying usual conditions. Notice that prices  $S$  are already discounted; this is equivalent to assuming that the spot interest rate  $r = 0$ . This model is, in general, incomplete, that is, it may admit infinitely many equivalent martingale measures (see **Equivalent Martingale Measures**).

Let H be a positive  $\mathcal{F}_T$ -measurable random variable, modeling the final payoff of a given contingent claim, for example,  $H = (S_T - K)^+$ , a European call option written on  $S$ , with maturity  $T$  and strike price  $K > 0.$ 

An admissible trading strategy is a couple  $(x, \theta)$ where  $x \in \mathbb{R}$  is an initial endowment and  $\theta =$  $(\theta_t)_{t \in [0,T]}$  a predictable *S*-integrable process, such that the corresponding wealth  $V_t^{x,\theta} = x + \int_0^t \theta_u \, dS_u \ge -a$ for every  $t \in [0, T]$  and for some threshold  $a >$ 0. We denote  $\mathcal{A}$  as the set of all admissible strategies.

**Definition 1** Let  $H \ge 0$  be a given contingent claim.  $(x,\theta) \in \mathcal{A}$  is a superhedging strategy for H if  $V_T^{x,\theta} \ge$  $H \mathbb{P}$ -a.s. (almost surely). Moreover, the superhedging price  $\bar{p}(H)$  of H is given by

$$\bar{p}(H) = \inf \left\{ x \in \mathbb{R} : \exists (x, \theta) \in \mathcal{A}, V_T^{x, \theta} \ge H \ a.s. \right\}$$
(1)

The fundamental result in the literature on superhedging is the dual characterization of the set  $\mathcal{D}^H$ of all initial endowments  $x \in \mathbb{R}$  leading to superhedge  $H$ . In an incomplete frictionless market, the relevant dual variables are the densities of all equivalent martingale measures  $d\mathbb{Q}/d\mathbb{P}$ . We denote  $\mathcal{M}^e$  as the set of all equivalent (local) martingale measures for  $S$ . In this setting, the superhedging theorem states that

$$\mathcal{D}^{H} = \left\{ x \in \mathbb{R} : \mathbb{E}_{\mathbb{Q}}[H] \le x, \forall \mathbb{Q} \in \mathcal{M}^{e} \right\} \qquad (2)$$

An important consequence of equation  $(2)$  is that the superhedging price  $\bar{p}(H)$  satisfies

$$\bar{p}(H) = \sup_{\mathbb{Q}\in\mathcal{M}^e} \mathbb{E}_{\mathbb{Q}}[H] \tag{3}$$

While an advantage of superhedging is that it is preference free, from the previous characterization of  $\bar{p}(H)$  as the biggest expectation  $\mathbb{E}_{\mathbb{O}}[H]$  over all equivalent martingale measures, it becomes apparent that pursuing a superhedging strategy can be too expensive, depending on the financial model and on the constraints on portfolios. This is the main disadvantage of such a criterion, which is, nonetheless, of great interest as a benchmark. Moreover, for an agent with a large risk aversion and under transaction costs (see the section Markets with Frictions), the reservation price approaches the superhedging price, as established in  $[2]$ .

El Karoui and Quenez [13, 14] first proved the superhedging theorem in an Itô's diffusion setting and Delbaen and Schachermayer [10, 11] generalized it to, respectively, a locally bounded and unbounded semimartingale model, using a Hahn-Banach separation argument.

The superhedging theorem can be extended in order to characterize the dynamics of the minimal superhedging portfolio of a contingent claim  $H$ , that is, the cheapest at any time t of all superhedging portfolios of  $H$  with the same initial

wealth. This extension is a consequence of the socalled *optional decomposition of supermartingales*. The optional decomposition was first proved in [13, 14] for diffusions and then extended to general semimartingales by Kramkov [24], Föllmer and Kabanov [15], and Delbaen and Schachermayer [12]. This is a very deep result of the general theory of stochastic processes and roughly states that any càdlàgpositive  $\mathbb{Q}$ -supermartingale X, for any  $\mathbb{Q} \in \mathcal{M}^e$ , can be decomposed as follows:

$$X_{t} = X_{0} + \int_{0}^{t} \theta_{u} \, \mathrm{d}S_{u} - C_{t}, \quad t \in [0, T] \quad (4)$$

where  $\theta$  is a predictable, S-integrable process and C an increasing optional process, to be interpreted as a cumulative consumption process. What is remarkable is that the local martingale part can be represented as a stochastic integral with respect to  $S$ so that it is a local martingale under any equivalent martingale measure  $\mathbb{Q}$ . In this sense, decomposition (4) is universal. The price to pay is that the increasing process  $C$  is, in general, not predictable as in the Doob-Meyer decomposition (see **Doob–Meyer Decomposition**) but only optional. The process  $C$  has the economic interpretation of cumulative consumption.

The decomposition (4) implies that the wealth dynamics of the minimal superhedging portfolio for a contingent claim  $H$  is given by

$$V_t = \text{ess sup}_{\mathbb{Q} \in \mathcal{M}^e} \mathbb{E}_{\mathbb{Q}}[H|\mathcal{F}_t], \quad t \in [0, T] \tag{5}$$

An analogous result holds for American contingent claims too (see  $[13-15, 24]$  for details at increasing levels of generality).

Finally, in the more specific setting of stochastic volatility models, Cvitanić et al. [8] compute the superhedging strategy and price for a contingent claim  $H = g(S_T)$ , yielding that the former is a buyand-hold strategy and so the latter is just  $S_0$ . The same study is carried over under portfolio constraints.

#### Markets with Frictions

In the previous section, we made the implicit assumption that investors can trade in continuous time and without frictions. This is clearly a strong idealization of the real world; that is why during the last 15 years much effort has been devoted to the superhedging approach under various types of trading constraints.

Transaction Costs. Financial models with proportional transaction costs were studied first by Jouini and Kallal [19] and then generalized in a series of papers by Kabanov and his coauthors  $[20-22]$ .

For the reader's convenience, we briefly introduce the model, following the bid-ask matrix formalism introduced by Schachermayer [27], which is only one of many equivalent convenient ways of describing it (see, e.g., [22] and Transaction Costs for more details).

We consider an economy with  $d \ge 1$  risky assets (e.g., foreign currencies);  $\pi_t^{ij}(\omega)$  denotes the number of physical units of asset  $i$  that can be exchanged with 1 unit of asset j at time  $t \in [0, T]$ . All of them are assumed to be adapted to some filtration and càdlàg. An important role is played by the so-called solvency region  $K_t(\omega)$ , the cone generated by the unit vectors  $e^i$  and  $\pi^{ij}e^i - e^j$  for  $1 \leq i, j \leq d$ . Elements of  $K_t(\omega)$  are all the positions that can be liquidated into a portfolio with a nonnegative quantity of each currency. We denote  $K^*_t(\omega)$  as the positive polar of  $K_t(\omega)$ .

A self-financing portfolio process is modeled by a d-dimensional finite variation process  $V = (V_t)_{t \in [0,T]}$ such that each infinitesimal change  $dV_t(\omega)$  lies in  $-K_t(\omega)$ , that is, a portfolio change at time t has to be done according to the trading terms described by the solvency cone  $K_t$ .

In this setting, so-called *strictly consistent price* systems play the same role as the equivalent martingale measures. A strictly consistent price system Z is a positive non-null  $d$ -dimensional martingale such that each  $Z_t(\omega)$  belongs to the relative interior of  $K_t^*(\omega)$  almost surely for all  $t \in [0, T]$ . We denote  $\mathcal{Z}^s$  as the set of all strictly consistent price systems. A standard assumption is that there exists at least one of such Z's, that is,  $\mathcal{Z}^{\prime s} \neq \emptyset$ , which is equivalent to some kind of no-arbitrage condition (see **Transaction Costs** for details).

Let  $H = (H^1, \ldots, H^d)$  be a d-dimensional contingent claim such that  $H + a\mathbf{1} \in K_T$  for some  $a \in$  $\mathbb{R}$ . We say that an admissible<sup>a</sup> portfolio V superhedges H if  $V_T - H \in K_T$ . Consider the set  $\mathcal{D}^{\bar{H}}$  of all initial endowment  $x \in \mathbb{R}^d$  such that there exists an admissible portfolio V,  $V_0 = x$ , that superhedges H.

In this model, the superhedging theorem states that

$$\mathcal{D}^{H} = \left\{ x \in \mathbb{R}^{d} : \mathbb{E}[Z_{T}H] \leq \langle x, Z_{0} \rangle, \forall Z \in \mathcal{Z}^{s} \right\}$$
(6)

where  $\langle \cdot, \cdot \rangle$  denotes the usual scalar product in  $\mathbb{R}^d$ . This theorem has been proven with increasing degree of generality by Cvitanić and Karatzas [7], Kabanov [20], and Kabanov and Last [21] for continuous bid-ask processes  $(\pi_t)_{t \in [0,T]}$  and constant proportional transaction costs, by Kabanov and Stricker [22] under slightly more general assumptions and finally, motivated by a counterexample constructed by Rásonyi [26], Campi and Schachermayer [5] extend it to discontinuous  $\pi$ .

Explicit computations of the superhedging price have been performed in [3, 9, 18] for a Europeantype contingent claim  $H = g(S_T)$ , where  $S_T$  is the price at time  $T$  of a given asset in terms of some fixed numéraire. Under different assumptions, the superhedging strategy is a buy-and-hold one, so that the corresponding superhedging price is the price at time  $t = 0$  of the underlying  $S_0$ .

Finally, duality methods for American options under proportional transaction costs are briefly treated in Transaction Costs.

Other Types of Market Frictions. Superhedging has also been studied under other types of constraints on, for example, shortselling and/or borrowing (see, e.g., Cvitanić and Karatzas' paper [6] and Karatzas and Shreve's book [23], Chapter 5, for more details). Very often, an agent willing to superhedge a contingent claim  $H$  has to choose a strategy fulfilling a given set of constraints. Let us denote  $\mathcal{A}_c$  as the class of constrained trading strategies. In this case, the constrained superhedging price  $\bar{p}_c(H)$  is given by

$$\bar{p}_c(H) = \inf \left\{ x \in \mathbb{R}^d : \exists (x, \theta) \in \mathcal{A}_c, V_T^{x, \theta} \ge H \right\}$$
(7)

Cvitanić and Karatzas [6] gave the first dual characterization of  $\bar{p}_c(H)$  in a diffusions setting, which was further generalized to general semimartingales by Föllmer and Kramkov [16] via a constrained version of the optional decomposition theorem, whose original version we already discussed at the end of the section Frictionless Incomplete Markets.

We conclude by mentioning a recent series of papers by Broadie et al. [4] and by Soner and Touzi [28, 29] on superhedging under *gamma constraints*, where an agent is allowed to hedge  $H$ , having at the same time a control on the gamma of his or her portfolios.

## **End Notes**

a*.* We remark *en passant* that the notion of admissibility in the presence of transaction costs, that we do not give here, is a subtle one. The interested reader could look at [5] for a short discussion.

## **References**

- [1] Benais, B., Lesne, J.P., Pages, H. & Scheinkman, J. ` (1992). Derivative asset pricing with transaction costs, *Mathematical Finance* **2**, 63–86.
- [2] Bouchard, B., Kabanov, Yu.M. & Touzi, N. (2001). Option pricing by large risk aversion utility under transaction costs, *Decisions in Economics and Finance* **24**, 127–136.
- [3] Bouchard, B. & Touzi, N. (2000). Explicit solution of the multivariate super-replication problem under transaction costs, *Annals of Applied Probability* **10**, 685–708.
- [4] Broadie, M., Cvitanic, J. & Soner, H.M. (1998). Optimal ´ replication of contingent claims under portfolio constraints, *The Review of Financial Studies* **11**, 59–79.
- [5] Campi, L. & Schachermayer, W. (2006). A superreplication theorem in Kabanov's model of transaction costs, *Finance and Stochastics* **10**(4), 579–596.
- [6] Cvitanic, J. & Karatzas, I. (1993). Hedging contingent ´ claims with constrained portfolios, *The Annals of Applied Probability* **3**(3), 652–681.
- [7] Cvitanic, J. & Karatzas, I. (1996). Hedging and port- ´ folio optimization under transaction costs: a martingale approach, *Mathematical Finance* **6**(2), 133–165.
- [8] Cvitanic, J., Pham, H. & Touzi, N. (1999). Super- ´ replication in stochastic volatility models under portfolio constraints, *Journal of Applied Probability* **36**(2), 523–545.
- [9] Cvitanic, J., Pham, H. & Touzi, N. (1999). A closed ´ form solution to the problem of super-replication under transaction costs, *Finance and Stochastics* **3**, 35–54.
- [10] Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing, *Mathematische Annalen* **300**, 463–520.
- [11] Delbaen, F. & Schachermayer, W. (1998). The fundamental theorem of asset pricing for unbounded stochastic processes, *Mathematische Annalen* **312**, 215–250.
- [12] Delbaen, F. & Schachermayer, W. (1999). A compactness principle for bounded sequences of martingales with applications, *Proceedings of the Seminar of Stochastic Analysis, Random Fields and Applications, Progress in Probability* **45**, 137–173.
- [13] El Karoui, N. & Quenez, M.-C. (1991). Programmation dynamique et evaluation des actifs contingents en ´ marche incomplet. (French) [Dynamic programming and ´ pricing of contingent claims in an incomplete market], *Comptes Rendus de l'Acad´emie des Sciences S´erie Math´ematiques* **313**(12), 851–854.

- [14] El Karoui, N. & Quenez, M.-C. (1995). Dynamic programming and pricing of contingent claims in an incomplete market, *SIAM Journal of Control and Optimization* **33**(1), 27–66.
- [15] Follmer, H. & Kabanov, Yu.M. (1998). Optional decom- ¨ position and Lagrange multipliers, *Finance and Stochastics* **2**(1), 69–81.
- [16] Follmer, H. & Kramkov, D. (1997). Optional decompo- ¨ sitions under constraints, *Probability Theory and Related Fields* **109**, 1–25.
- [17] Follmer, H. & Schied, A. (2004). ¨ *Stochastic Finance: An Introduction in Discrete Time*, 2nd Edition, de Gruyter Studies in Mathematics, Berlin, P. 27.
- [18] Guasoni, P., Rasonyi, M. & Schachermayer, W. (2007). ´ Consistent price systems and face-lifting under transaction costs, *Annals of Applied Probability* **18**(2), 491–520.
- [19] Jouini, E. & Kallal, H. (1995). Martingales and arbitrage in securities markets with transaction costs, *Journal of Economic Theory* **66**, 178–197.
- [20] Kabanov, Yu.M. (1999). Hedging and liquidation under transaction costs in currency markets, *Finance and Stochastics* **3**(2), 237–248.
- [21] Kabanov, Yu.M. & Last, G. (2002). Hedging under transaction costs in currency markets: a continuous-time model, *Mathematical Finance* **12**(1), 63–70.
- [22] Kabanov, Yu. & Stricker, Ch. (2002). Hedging of contingent claims under transaction costs, in *Advances in Finance and Stochastics. Essays in Honour of Dieter Sondermann*, K. Sandmann & Ph. Schonbucher, eds, Springer, Berlin, Heidelberg, New York.
- [23] Karatzas, I. & Shreve, S. (1998). *Methods of Mathematical Finance*, Springer.
- [24] Kramkov, D. (1996). Optional decomposition of supermartingales and hedging contingent claims in incomplete security markets, *Probability Theory and Related Fields* **105**, 459–479.
- [25] Naik, V. & Uppal, R. (1994). Leverage constraints and the optimal hedging of stock and bond options, *Journal of Financial and Quantitative Analysis* **29**(2), 199–222.
- [26] Rasonyi, M. (2003). ´ *A Remark on the Superhedging Theorem Under Transaction Costs. S´eminaires de Probabilit´es XXXVII*, Lecture Notes in Mathematics, 1832, Springer, pp. 394–398.
- [27] Schachermayer, W. (2004). The fundamental theorem of asset pricing under proportional transaction costs in finite discrete time, *Mathematical Finance* **14**(1), 19–48.
- [28] Soner, H.M. & Touzi, N. (2000). Super-replication under gamma constraints, *SIAM Journal of Control and Optimization* **39**(1), 73–96.
- [29] Soner, M. & Touzi, N. (2007). Hedging under gamma constraints by optimal stopping and face-lifting, *Mathematical Finance* **17**(1), 59–80.

LUCIANO CAMPI
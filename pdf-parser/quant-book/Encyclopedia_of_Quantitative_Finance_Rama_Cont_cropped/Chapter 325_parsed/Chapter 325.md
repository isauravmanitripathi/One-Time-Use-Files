# **Swing Options**

Unlike paper assets, trading in physical commodities often takes place over time and therefore involves volume as a second key state variable. Often, consumption rates of the commodity are unpredictable and make fixed delivery amounts uneconomic. To mitigate such volume risk, a swing contract gives the buyer the opportunity to manage fluctuating commodity demand levels in exchange for a fixed upfront fee. By exercising his or her swing up/down rights, the buyer can dynamically match supply and demand levels while hedging his or her costs. Swing options are widely offered by market makers and used extensively by major energy companies, especially in electricity and fossil fuel markets. Contracts with swing features are available as stand-alone financial tools; they can also be found embedded within structured physical transactions.

## **Definition and Use**

A typical definition of a swing option is as follows. At times  $n = 1, 2, \ldots, N$  the buyer is to receive a *baseload* amount  $\bar{K}$  of the commodity paying the strike price  $\bar{P}$ . In addition, over the life of the contract, the buyer has  $N_c \leq N$  swing rights to temporarily vary these deliveries, instead requesting to receive an amount  $k_n$ . This request is usually made on a one-period ahead basis, so that the supplier has time to adjust delivery. The swing amount  $k_n$ is subject to the constraint  $k_{\min} \leq k_n \leq k_{\max}$ , where  $k_{\min}$  (respectively,  $k_{\max}$ ) is the minimal (respectively, maximal) allowable one-period delivery volume. The timing of these exercises is at the discretion of the buyer. Thus, depending on the needs of the buyer, the amount received can be swung up or down up to  $N_c$  times.

Let  $Y_n$  denote the discounted present value of the net cash flow beyond the income expected from the baseload contract, due to the exercise of a swing right on date  $n$ . Assuming that the cashflow amount is linear in the swing volume and no other constraints are present, it is optimal to always apply full (bang-bang) volumetric exercise, that is,  $k_n \in$  $\{k_{\min}, k_{\max}\}\.$  It follows that

$$Y_n = e^{-rn}(k_n - \bar{K})(P_n - \bar{P}) \tag{1}$$

where  $P_n$  is the spot price of the commodity in period  $n$ , and  $r$  is the discount rate for one period. Note that if the exercise decision was made *before*  $n$ , then  $Y_n$ in equation  $(1)$  may be negative.

#### Take-or-Pay Provisions

To bound possible swings from the baseload contract, global volume constraints are often imposed. A take-or-pay provision adds the constraint  $S_{\min} \leq$  $\sum_{n=1}^{N} k_n \leq S_{\text{max}}$ , where  $S_{\text{min}}$  (respectively,  $S_{\text{max}}$ ) is the minimal (respectively, maximal) total volume over the  $N$  periods. Thus, the buyer must place his or her total cumulative consumption within a predefined volume band. This rule is enforced via penalties on the buyer (hence take or pay) if the provision is violated.

#### Nomination Contracts

A nomination contract is a variant of a swing option, where the swing amounts are permanent. Thus, changing the nomination amount from  $\bar{K}$  to  $k_n$ implies that the new baseload amount will be  $k_n$  for the remainder of the contract. Such ratcheting rules are common in pipeline contracts.

## Refraction Periods

Some contracts impose a minimal refraction period  $\delta$ between consecutive swings to prevent too rapid an exercise. Refraction periods also appear in research papers that consider swing options in continuous time; see the section Valuation and Theoretical Issues below.

Most existing contracts combine several of the above features and also include further custom rules, so that "vanilla" swing options are actually a rarity. Before proceeding with our discussion, we give a few examples of real-life swing contracts.

## Swing Option in the Natural Gas Market

Consider an industrial natural gas consumer that wishes to hedge its future input costs. The consumer does not know consumption volume precisely (which depends on demand for output, operational constraints, other suppliers, etc.), but has some volume range based on past usage. The consumer purchases a month-long swing option to offset this "volumetric risk" exposure. The swing option gives the consumer the right to buy up to 10 000 MMBtu at the price of *P*¯ = \$6 in each of the four weeks; the total volume must be between *S*min = 10 000 and *S*max = 30 000 MMBtu over the month. In this example, *Nc* = *N* = 4, *k*min = *K*¯ = 0*,* and *k*max = 10 000.

#### *Recall Option for an Oil Pipeline*

An oil pipeline company delivers oil from hub A to an industrial customer at point B. The pipeline plans on delivering 1000 bbl/day for the next month at the forward price of *P*¯ = \$100/bbl. However, owing to pipeline congestion, supply disruption, or engineering problems, the pipeline may be unable to fulfill its obligation. To mitigate this risk, the pipeline purchases a recall option from its customer. Upon giving notice the day before, the recall option gives the pipeline the right to withhold delivery (or deliver less than the baseload amount) on up to three days during the month. In this example, *Nc* = 3*, N* = 30, *k*min = 0, *K*¯ = *k*max = 1000. Similar interruptible delivery contracts are common in electricity markets; see [10, 16, 22].

#### *Load Serving Contract for an Electricity Utility*

Electricity swing options have become popular with the deregulation of electricity markets, which led to volume risk management by the power serving entities (PSE). A PSE is obliged by law to provide power to its customers and must adjust its production to maintain equilibrium with the fluctuating demand. Such dynamic load management can be synthetically reproduced by a swing contract that the PSE in effect sells to its customers. By buying an offsetting swing option on its input fossil fuel (such as natural gas), the PSE can transfer the corresponding volume risk exposure to other market participants.

# **Valuation and Theoretical Issues**

From a financial engineering perspective, a swing option is an exotic compound timing option on the underlying commodity asset. More precisely, it closely resembles a series of American options. Indeed, if the number of swing rights is *Nc* = 1, then the swing collapses to the usual American option (*see* **American Options**); if the number of swing rights is equal to the number of periods (*Nc* = *N*), then the value of the swing contract is equal to a strip of European options for each period. Let us denote by *V (t, m, p)* the value of owning a swing contract on date *t* with *m* remaining swing exercise rights and current price *p* of the commodity. Then the following *a priori* bound is always true irrespective of the underlying price process:

$$m \cdot EC(t, p) \le V(t, m, p) \le m \cdot AC(t, p) \quad (2)$$

where *EC* (respectively, *AC*) denotes the value of a European (respectively, American) option with expiration date *N*.

In the following discussion, we assume that *kn* ∈ {0*,* 1}; modulo constant scaling this is equivalent to full volumetric exercise. To set up a mathematical model, it is necessary to construct a framework for the multiple exercise opportunities. Recalling the concept of stopping times, define the set of *m*-tuples of stopping times used to model the multiple exercises as

$$S_{\alpha,\beta}^{(m)} = \{ \vec{\tau} = (\tau_1, \dots, \tau_m): \tau_i \text{ stopping time}$$
  
and  $\alpha \leq \tau_1 < \tau_2 < \dots < \tau_m \leq \beta \}$  (3)

Then the optimal multiple-stopping problem corresponding to a basic swing option with maturity *T* reduces to computing

$$V(t,m,p) = \sup_{\vec{\tau} \in \mathcal{S}_{t,T}^{(m)}} \mathbb{E}_t[Y_{\vec{\tau}}], \quad \text{where} \quad Y_{\vec{\tau}} := \sum_{i=1}^m Y_{\tau_i}$$
  
and  $P_t = p$  (4)

Beyond finding the value of the supremum in equation (4), it is of interest to know whether this supremum is actually attained (existence of optimal swing exercise strategy), and if yes, finding a computational algorithm giving a "minimal" set of optimal exercise times *τ*. For models of equation (4) in continuous time, the refraction time constraint *τi* ≥ *τi*<sup>−</sup><sup>1</sup> + *δ*, *δ >* 0 must be added to equation (3); otherwise *τi*<sup>−</sup><sup>1</sup> *< τi* is vacuous.

The problem (4) is best solved by an inductive procedure based on the solution of a sequence of single-exercise American options. For example, Carmona and Touzi [9] have proved that

$$V(t, m, p) = \sup_{t \le \tau \le T} \mathbb{E}_t \left[ Y_\tau + V(\tau, m - 1, P_\tau) \right] \tag{5}$$

where the maximization is over all stopping times  $\tau$ , and where  $\mathbb{E}_{\tau}$  denotes conditional expectation at time  $t$ . Equation (5) is of the same flavor as the American/Bermudan option problem, but with additional state variable  $m$ .

In a Markovian setting, an optimal swing exercise policy is characterized by an *exercise boundary*  $B$ , similar to American options, that is, the exercise boundary divides the commodity price space into a continuation region, where the holder of the swing does nothing, and an exercise region, where it is optimal to exercise a swing right. However, analysis of the swing exercise boundary is complicated by the fact that today's exercise reduces future delivery flexibility. Thus, the swing exercise boundary is a function both of time and number of remaining rights,  $B = B(t, m)$ . In certain settings [6, 9], it can be shown that  $B(t,m)$  is connected, and, moreover, is monotone in number of rights  $m$  and, similarly, is monotone in  $t$ . However, general properties of  $B(t, m)$  remain unresolved. An excellent summary of the structural features of swing options can be found in the book by Eydeland and Wolyniec [15, Chapter 8].

The major difficulties in valuing and analyzing swing options arise because of the high-dimensional setting and the contract's path-dependent features. Analysis of a basic swing option involves two state variables, namely, the current price  $P_n$  and the remaining number of exercise rights  $M_n$ . If a take-orpay provision is present, then one must also consider the current cumulative volume  $S_n := \sum_{j=1}^n k_j$ . Both the  $M$  and  $S$  state variables depend on the particular swing exercise policy and are therefore path and control dependent. This precludes simple application of dynamic programming to equation (5). Moreover, models of underlying commodity price processes (see **Commodity Price Models**) are often complex and include multiple factors to capture the observed seasonality, mean reversion, and nonlinearity in prices. Recall that if the exercise decision is made on a forward basis, modeling of the spot-forward relationship (see Commodity Forward Curve Modeling) is also needed.

To illustrate the difficulties involved, consider a simple binomial tree model that assumes a onedimensional random walk description of the underlying commodity price  $(P_n)$ . To price a swing option, we then need to set up a *forest* of  $N_c$  such trees, with a tree for each possible number of remaining exercise rights. One can then proceed using the backward dynamic programming algorithm like for standard American options (see American Options), where a swing exercise triggers a jump from a tree with  $M_n = m$  remaining rights to a tree with  $M_n = m - 1$ . Such an algorithm imposes memory and space constraints and raises efficiency issues. More sophisticated models might involve multiple factors or jumps (or take-or-pay provisions) and would require even more complex forests of trees.

# **Historical Perspective**

Initial discussion of swing options appeared in the early 1990s in energy practitioner magazines; see, for example, [3, 11, 12]. At the same time, a limited literature studied the embedded multiple exercise opportunities [14, 25, 30]. Theoretical treatment of swing options was first carried out rigorously by Jaillet et al. [21]. The connection to multiple-stopping problems was established by Carmona and Touzi [9], who showed in a certain mathematical framework that a swing option is equivalent to  $N_c$  compound American (optimal stopping) options on the underlying; see also (5). This fact suggests pricing of swing options based on existing methods for American options. In a simplified model, with single underlying risky asset, swing options could be, for example, priced by solving partial differential equations like in the classical Black-Scholes theory (see Finite Difference Methods for Early Exercise Options). However, nonlinearities rule out solutions in the classical sense, and complex free boundaries make the design and control of numerical schemes quite a challenge.

To overcome these challenges, a variety of approaches have been suggested, including other partial differential equation methods ( $[13, 31]$  and see Finite Element Methods), stochastic dynamic programming [2, 17], the aforementioned binomial and trinomial trees ([21] and see Tree Methods), Monte Carlo simulation methods ([4, 16, 20, 27] and see **Bermudan Options**), approximate techniques ([14, 23, 29] and *see* **Exercise Boundary Optimization Methods**), and optimal quantization (*see* **Quantization Methods** and [1]). Also see [16, 19, 24, 32] for analytic pricing of swing contracts under certain exotic models for the underlying commodity and [28] for game-theoretic aspects of swing options. Beyond the basic contracts, the modern practitioner/research trend is to value swing options using simulation tools that can achieve excellent computational complexity properties with respect to underlying models. However, as a trade-off, the error analysis of many simulation schemes is difficult, and usually only a lower bound on price can be obtained.

# **Hedging Issues**

Hedging of swing options can be carried out in the same framework as American options. However, several additional issues make hedging difficult in practice. First, recall that many buyers of swing options are industrial customers. Empirical evidence [15] suggests that such buyers often exercise suboptimally to meet their other obligations (e.g., as suppliers of electricity). Suboptimal exercise may be justified if the spot market is not sufficiently liquid, as is the case in many commodities, especially those with strong locational characteristics. This leads to nontrivial financial implications to sellers of swing options who hedge optimally.

Secondly, swing exercise decisions are typically made one-day-ahead on the basis of forward prices. Since the cashflow is based on spot prices, basis risk between forward and spot price becomes a cause of concern (both to buyer and seller of swing contracts). This is particularly so in electricity markets, where the commodity is nonstorable and there is no definite convergence between day-ahead and real-time prices.

The underlying commodity market may be financially incomplete (*see* **Complete Markets**) for other reasons. As such, the seller of the swing option cannot fully hedge his or her exposure and therefore the no-arbitrage risk-neutral valuation method might not make sense. Finally, in some less liquid markets, the buyer may be exercising market power by manipulating demand through his or her swing policy and therefore affecting future prices.

# **Extensions and other Contracts with Multiple Exercise**

With wide use of swing options, other modifications to the basic contract have become common.

## *Chooser Flexible Caps*

A cap contract with strike *P*¯ on a three-month interest rate is a portfolio of options on the quarterly interest payments that have to be made. Let us assume that the life of the contracts is *N* quarters, and the nominal is *X*. Each individual option is called a *caplet*. It covers one of the *N* quarters, and its payoff is *X* · *t* · *(L*<sup>3</sup> − *P )*¯ <sup>+</sup>*,* where *t* is the day-count fraction, and *L*<sup>3</sup> denotes the quarter-end three-month LIBOR rate. A *chooser flexible cap* is a contract such that, at each reset date, the holder of the contract has the right to decide whether to exercise that particular caplet and count it as part of the *Nc* allowable ones, or spare it for later use, each decision being final. The remaining caplet rights expire worthless if not used before the end of the *N* periods. A chooser cap reduces to a regular cap (*see* **Caps and Floors**) when *Nc* = *N*, while it can be viewed as a standard American/Bermudan option on the interest rate *L*<sup>3</sup> when *Nc* = 1. Valuation of such contracts has been studied in [27].

### *Two-sided Swing Options*

Some physical contracts combine the swing and recall features described above. Thus, the baseload contract is augmented with *Nr* recall rights for the party delivering the commodity, and *Nc* swing rights for the buyer. The interaction of these rights leads to a stochastic *game* between the two counterparties, with the buyer being the minimizing agent, and the seller the maximizing agent. Valuation of such twosided swing options is related to Dynkin games as explained in [5].

## *Gas Storage*

The owner of a gas storage facility attempts to maximize revenue by injecting gas into storage when prices are low and withdrawing gas when prices are high. Exercise of such flexibility can be viewed as a nomination swing option where *kn* is allowed to be both positive and negative (to model withdrawals). The volume constraints *S*min ≤ *Sn* ≤ *S*max then correspond to the physical size constraints of the facility. Gas storage valuation is complicated by additional storage costs, which add further path dependency to the problem; (*see* [4, 8]).

## *Tolling Agreements*

In a *tolling agreement*, the buyer is granted use of a commodity-generating facility for a fixed period of time. The buyer can then run the facility when commodity price is high and keep it shut down when prices are low. This is again a nomination swing option with additional engineering constraints, such as fixed switching costs. Modeling of such contracts fits within the more general framework of optimal switching problems [7, 18].

#### *Employee Stock Options*

Company employees are often granted multiple stock options in their employers (*see* **Employee Stock Options**). Partial exercise of such options by riskaverse employees is similar to a swing call option, as multiple exercises must be considered [26].

# **References**

- [1] Aj Bardou, O., Bouthemy, S. & Pages, G. (2007). ´ *Pricing Swing Options Using Optimal Quantization*, available at http://www.arxiv.org/0705.2110.
- [2] Baldick, R., Kolos, S. & Tompaidis, S. (2006). Interruptible electricity contracts from an electricity retailer's point of view: valuation and optimal interruption, *Operations Research* **54**, 627–642.
- [3] Barbieri, A. & Garman, M.B. (1996). Understanding the valuation of swing contracts, *Energy and Power Risk Management* **1**.
- [4] Barrera-Esteve, C., Bergeret, F., Dossal, C., Gobet, E., Meziou, A., Munos, R. & Reboul-Salze, D. (2006). Numerical methods for the pricing of swing options: A stochastic control approach, *Methodology and Computing in Applied Probability* **8**(4), 517–540.
- [5] Carmona, R. (2007). *Monte Carlo American Exercises, 2007* . Lecture Notes, Sixth Winter School in Financial Mathematics Jan. 22–24, 2007 Lunteren, Holland.
- [6] Carmona, R. & Dayanik, S. (2008). Optimal multiple stopping of linear diffusions, *Mathematics of Operations Research* **33**(2), 446–460.

- [7] Carmona, R. & Ludkovski, M. (2008). Pricing asset scheduling flexibility using optimal switching, *Applied Mathematical Finance* **15**(6), 405–447.
- [8] Carmona, R. & Ludkovski, M. (2009). Valuation of energy storage: an optimal switching approach, *Quantitative Finance* (To appear).
- [9] Carmona, R. & Touzi, N. (2008). Optimal multiple stopping and valuation of swing options, *Mathematical Finance* **18**(2), 239–268.
- [10] Cartea, A. & Williams, T. (2008). UK gas markets: the market price of risk and applications to multiple interruptible supply contracts, *Energy Economics* **30**(3), 829–846.
- [11] Clewlow, L., Strickland, C. & Kaminski, V. (2001). Valuation of swing contracts in trees, *Energy and Power Risk Management* **6**, 33–34.
- [12] Clewlow, L., Strickland, C. & Kaminski, V. (2001). Risk analysis of swing contracts, *Energy and Power Risk Management* **6**.
- [13] Dahlgren, M. (2005). A continuous time model to price commodity-based swing options, *Review of Derivatives Research* **8**(1), 27–47.
- [14] Davison, M. & Anderson, L. (2003). *A Recursive Framework for Approximating Early Exercise Boundaries of Electricity Swing Options*.
- [15] Eydeland, A. & Wolyniec, K. (2003). *Energy and Power Risk Management: New Developments in Modeling, Pricing and Hedging*. John Wiley & Sons, Hoboken, NJ.
- [16] Figueroa, M.G. (2006). *Pricing Multiple Interruptible-Swing Contracts*. Birkbeck Working Papers in Economics and Finance 0606. School of Economics, Mathematics & Statistics, Birkbeck, June 2006.
- [17] Haarbrucker, G. & Kuhn, D. (2009). Valuation of elec- ¨ tricity swing options by multistage stochastic programming, *Automatica* **45** (To appear).
- [18] Hamadene, S. & Jeanblanc, M. (2007). On the start- ` ing and stopping problem: application in reversible investments, *Mathematics of Operations Research* **32**(1), 182–192.
- [19] Hambly, B., Howison, S. & Kluge, T. (2007). *Modelling Spikes and Pricing Swing Options in the Electricity Markets, 2007* . Working paper, University of Oxford.
- [20] Iba´nez, A. (2004). Valuation by simulation of contingent ˜ claims with multiple exercise opportunities, *Mathematical Finance* **14**(2), 223–248.
- [21] Jaillet, P., Ronn, E.I. & Tompaidis, S. (2004). Valuation of commodity-based swing options, *Management Science* **50**(7), 909–921.
- [22] Kamat, R. & Oren, S.S. (2002). Exotic options for interruptible electricity supply contracts, *Operations Research* **50**(5), 835–850.
- [23] Keppo, J. (2004). Pricing of electricity swing options, *Journal of Derivatives* **11**, 26–43.
- [24] Kjaer, M. (2008). Pricing of swing options in a mean reverting model with jumps, *Applied Mathematical Finance* **15**(6), 479–502.

- [25] Lari-Lavassani, A., Simchi, M. & Ware, A. (2001). A discrete valuation of swing options, *The Canadian Applied Mathematics Quarterly* **9**(1), 35–73.
- [26] Leung, T. & Sircar, R. (2009). Accounting for risk aversion, vesting, job termination risk and multiple exercises in valuation of employee stock options, *Mathematical Finance* **19**(1), 99–128.
- [27] Meinshausen, N. & Hambly, B. (2004). Monte Carlo methods for the valuation of multiple exercise options, *Mathematical Finance* **14**, 557–583.
- [28] Pflug, G.C. & Broussev, N. (2009). Electricity swing options: Behavioral models and pricing, *European Journal of Operational Research*.
- [29] Ross, S.M. & Zhu, Z. (2008). On the structure of a swing contract's optimal value and optimal strategy, *Journal of Applied Probability* **45**(1), 1–15.
- [30] Thompson, A.C. (1995). Valuation of path-dependent contingent claims with multiple exercise decisions over time: the case of take or pay, *Journal of Financial and Quantitative Analysis* **30**, 271–293.

- [31] Winter, C. & Wilhelm, M. (2008). Finite element valuation of swing options, *Journal Of Computational Finance* **11**(3), 107–132.
- [32] Zeghal, A.B. & Mnif, M. (2006). Optimal multiple stopping and valuation of swing options in Levy mod- ´ els, *International Journal of Theoretical and Applied Finance* **9**(8), 1267–1297.

# **Related Articles**

**American Options**; **Bermudan Swaptions and Callable Libor Exotics**.

RENE´ CARMONA & MICHAEL LUDKOVSKI
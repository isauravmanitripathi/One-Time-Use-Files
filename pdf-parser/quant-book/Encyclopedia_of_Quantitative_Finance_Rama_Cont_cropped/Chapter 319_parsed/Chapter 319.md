# **Commodity Risk**

Before the emergence of B2B exchanges and the contracting innovations of interest here, the focus in procurement was on bilateral negotiation, and the literature provides analysis of many aspects of supply contracting in this setting (see [3] for a review). Bilateral contracting and traditional supplier management practices will remain essential elements of procurement management in the future. However, the growth of commodity exchanges, and derivative instruments defined on these, has introduced a fine-tuning mechanism that improves operational performance and simultaneously helps value longer term contractual, capacity, and technology decisions. The centerpiece of this new perspective is the integration of traditional forms of contracting with shorter term market-driven physical and financial transactions. This integration is the focus of this article.

An example will help clarify the scope and importance of this subject. Consider the beverage industry. Aluminum is an important element of the cost structure. For major buyers like Anheuser Busch, a restricted set of sellers is used to source aluminum, even though the aluminum spot market price is a key benchmark for sourcing and hedging, and is determined by the actions of scores of global players. Here, sourcing arrangements with main sellers are typically set according to the spot price plus processing costs, and contracts are marked to market on a daily basis. Second, there may be value-added services undertaken by these contractors to take aluminum ingots and prepare them in a more suitable fashion for can production, and again here this would be done only with specifications for these services worked out with a few sellers. However, the typical setup in metals is for a restricted set of contract sellers, with spot purchases and hedging used to benchmark prices and to "top up" contract purchases and hedge overall supply cash flows. The same general market and contracting structure operates in many other commodity markets, including energy and agricultural markets [5].

The first question to address is the consequence of competition among multiple sellers with heterogeneous costs/technologies. This question can be addressed in two ways: one is to assume a closed spot market in which all participants in the contract market also participate in the spot market, and *vice* *versa*. Alternatively, one can assume an open structure in which the spot market price is determined by a larger group of competitive sellers than the smaller, restricted group operating in the contract market for a particular buyer. In this article, we follow the latter assumption; for a discussion of closed spot markets and strategic behavior, see [10].

# **A Primer on Previous Literature**

The literature on contracting in economics has been driven by the transactions cost framework developed by Williamson [11], and subsequently formalized in the principal–agent literature [8].

A key question addressed in the economics literature has been the efficiency of various contracting structures. A well-known result in the economics contracting literature is due to Allaz and Vila [1], which examines the efficiency of pure forward contracts in an oligopolistic setting but with a deterministic spot market (which is fixed and common knowledge). Assuming homogeneous sellers and instantaneous scalability (with no capacity limitations), they show that forward markets can yield inefficient outcomes because of strategic use of these markets by sellers with market power. Wu and Kleindorfer [12] show that the Allaz–Vila-forward-market inefficiency disappears when options contracts are introduced into the mix of traded instruments, underscoring the importance of derivative instruments for supply management.

The financial economics literature provides basic pricing results for derivative instruments traded on standard contracts in liquid markets. In the context of supply contracting, an additional distinction is required in the types of options involved, between purely financial options and those connected to physical delivery of a particular good at a particular time and place. The early discussion and literature was focused on physical delivery options to fulfill a buyer's sourcing needs. These options would entail delivery at a particular time and place (e.g., FOB Pittsburgh). In these markets, options backed by physical delivery are central to the buyer's problem of arranging for sufficient supply to meet the buyer's demand. However, once a functioning spot market exists, this market can be used to define financial options on the basis of the spot price. Major buyers then find it in their interest not only to arrange optimal sourcing from the contract and spot markets for physical delivery of goods but also to use the financial options defined in the market for price discovery and as risk hedge instruments. As Birge [2] notes, if either revenue or costs associated with a given product line are correlated with some well-defined price (or cost) index arising from a competitive market, then this price index can be used to define an appropriate derivative or options instrument that provides not only risk hedging benefits but also valuation information for the underlying operations decisions whose outputs are correlated with the index.

# **Standard Commodity Hedging Framework**

The standard approach to supply management commodity risk [5, 12] is based on the following threeperiod timeline for trading in the B2B exchange, either using contracts or using the spot market (Figure 1).

- Period 0: At period 0, capacity and technology choices are made by buyers and sellers. As shown in [5], these choices will be different when rational managers know that they can fine-tune demand and supply through the spot market than when such a possibility does not exist.
- Period 1: At period 1, with updated information on the distribution of spot prices, sellers and buyers contract with one another, using options and forwards, for delivery of some good (either storable or nonstorable) at period 2.
- Period 2: Finally, at period 2, after possibly updating additional information, options are called, forwards are executed, deliveries are made, and additional sales and purchases are made in the short-term spot (or cash) market.

Between period 1 and period 2, there may be additional trading of options and additional, possibly continuous, updating of information on spot prices. The analysis here will assumes a discrete-time framework with no secondary trading. Thus, we are only concerned with the indicated decision instants at periods 0, 1, and 2.

The objective of the buyer is to maximize expected profit by choosing among the available forward and spot contracts. The objective of sellers is to maximize expected profit, jointly obtained from sales in both the contract market and the spot market and subject to the seller's capacity constraint. Either buyer or sellers may have additional risk-based constraints on their transactions, such as those derived from a Value-at-Risk (VaR) framework, as explained further subsequently.

A key factor influencing the incentives of sellers and the buyer to sign contracts is the existence of imperfect market access on the day, capturing possible access inefficiencies of the spot market, which includes cost and quality differences between contract markets and the spot market. In addition, in supply management for commodities, different grades and specifications for commodities often require prior contracting and procurement relations. These alternative situations give rise to various forms of commodity risk management, as shown in Table 1.

Access conditions are modeled in [12] *via* a function *m(Ps)*, which is defined as the probability that the seller can find a last-minute buyer on the spot market when the realized spot price is *Ps*. This market access probability can also be thought of as the proportion of the seller's capacity that can be expected to be sold at the last minute. This function may be thought of as a measure of the liquidity of the market and the degree to which the commodity in question is standardized. When quality and yield issues are present, then *m(Ps*) may also be

![](_page_1_Figure_11.jpeg)

**Figure 1** Market interactions in the standard commodity hedging framework

| Description of context                                                                                                  | Instruments used in optimal portfolio                                                                                                                                 | Examples                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Cost and access differences are<br>small and only standard<br>commodities are sourced                                   | Bilateral contracting and financial<br>hedge instruments are defined on<br>a common market and optimized<br>jointly                                                   | energy commodity metals                                                                              |
| Cost and access differences are<br>large and only standard<br>commodities are sourced                                   | Bilateral contracting is used for<br>most physical procurement, with<br>spot market used for topping up<br>supply, and for financial hedge<br>instruments             | Logistics services (standard air<br>and maritime cargo) Fed cattle<br>(beef), hogs, and lamb markets |
| Nonstandard commodities are<br>sourced, but their prices are<br>highly correlated with those of<br>standard commodities | Bilateral contracting is used for all<br>physical procurement, with<br>financial hedge instruments,<br>defined on correlated standard<br>products, used as an overlay | Plastic resins and commodity<br>chemicals                                                            |

**Table 1** Alternative contexts for commodity risk management of supply

thought of as the quality risk associated with spot purchases.

The standard problem of commodity sourcing and hedging for a buyer can be stated as follows (this is the problem facing the buyer at period 1 in Figure 1):

Maximize 
$$E\left\{\Pi(Q,\tilde{D},\tilde{P}_s)\right\}$$
 (1)

s.t.

 $G(Q, F_D, F_{P_s}) \ge 0$  physical delivery constraints

 $H(Q, F_D, F_{P_s}) \ge 0$  VaR constraints

 $Q \in X$ other constraints on instruments

where the maximization in equation  $(1)$  is over the vector of available financial and physical instruments  $Q$  at the time of contracting, where "demand" uncertainties are represented by  $\tilde{D}$ , and where spot price uncertainty is represented by the random variable  $\tilde{P}_s$ , with respective cumulative density functions of  $F_D$ and  $F_{Ps}$ . At period 2, of course, once *D* and  $P_s$  are observed, instruments are executed to fulfill the physical delivery constraints and to optimize profits on the day by executing all options that are "in the money", or needed for physical fulfillment. This problem "on the day" can sometimes be interesting, but it in theory is straightforward and we do not consider its solution here. Various forms of the problem in equation (1) have been developed for various types of markets, and the details for these differ considerably across these markets. To illustrate, let us consider the structure of this problem for the case of a distribution company or supplier in the case of electric power operating in the presence of a liquid spot market.

# **Electric Power: An Illustrative Example of Commodity Hedging**

We imagine an integrated utility, called the *Company*, which may own or lease generation, and which has a trading division that can sign contracts for power purchase agreements (PPAs), as well as puts, calls, and forwards, based on an underlying wholesale spot market. We abstract here from transmission constraints or markets.<sup>a</sup> For simplicity, we also imagine that the Company provides energy to retail customers at prices that are regulated. We will take the simplest possible approach to the regulated sector, assuming a fixed, exogenously determined regulated price per Kilowatt hour, independent of time. More complicated regulatory scenarios are easily incorporated into the framework developed. This feature of customer demand at regulated prices, together with the weather-driven level of spot prices and the nonstorability of electric power, makes electricity supply a risky business.

We are interested in formulating the Company's optimal portfolio problem for procuring and hedging its purchases of energy. The portfolio will be characterized by different levels of time-indexed instruments (puts, calls, forwards, etc.) that might be called upon either to fulfill retail demand or simply as part of profit-oriented trading/hedging activities by the Company's trading division. We refer to all potential assets for the portfolio, including owned/leased generation and PPAs, as instruments.

Following  $[6]$  and  $[7]$ , we think of each instrument as having a capacity (measured in megawatts) that can be called or sold in a specific period (consisting of specified hours during a given week or month, typically the  $5 \times 16 \text{ h}$  of "peak" or the  $7 \times 8 \text{ h}$  of "off-peak"). Each instrument entails a reservation price, possibly zero, per megawatt to reserve, and an execution price, per megawatt hour, if used. In this framework, instruments such as own generation and certain PPAs that have been precommitted have a fixed execution price (e.g., the marginal running cost of own generation), but may be thought of as available at a reservation price of zero. Purchased forwards, which are prepaid, fixed obligations to deliver power, may be viewed as call options having a zero execution price that therefore will be executed by the Company on the day. Forwards sold by the Company have the same characteristic, that is, they may be viewed as options contracts with a zero execution price (that therefore will be executed on the day).

To set up the model, we will assume that the planning period for the instruments in question is a month, with hours in the month being denoted by the set  $T = \{1, \ldots, 720\}$ . We will consider additional subsets of  $T$  below, such that certain instruments may be valid only for certain subsets of time (e.g., peak hours). We need the following additional notation:

- $Q_i$  = the amount (in megawatts) of instrument *i* that is purchased/sold
- $r_i$  = reservation price per megawatt hour for call asset  $i^{\text{b}}$
- $c_i$  = execution price per megawatt hour for call asset i
- $s_i$  = reservation price per megawatt hour for put asset  $i$

 $p_i$  = execution price per megawatt hour for put asset *i* 

- $T_i \subseteq T = \text{index of those hours of type "j", where}$  $j = 1, \ldots, J$  (types of time periods might be, for example, peak periods, off-peak periods, weekends, etc.)
- $I_{ci}$  = the set of indices for all call instruments (used in the following summation) that can be executed during hours of type  $j$
- $I_{pj}$  = the set of indices for all put instruments (used in the following summation) that can be executed during hours of type  $j$

- $n =$  the number of all instruments (so  $n = \sum_{j=1}^{J} |I_{cj}|$  $\cup I_{ni}|)$
- $m_i =$  lower bound or minimum amount allowed for instrument  $Q_i$
- $M_i$  = upper bound or maximum amount allowed for instrument  $Q_i$

The random variable of "monthly cash flows" depends on the level of each instrument  $Q_i$  in the portfolio, where some instruments, within each month, may apply to different periods of time (e.g., just the peak periods or just the off-peak periods, or to some other selection of periods). We can write cash flows (for some period, say month  $t$ ) in the following general form:

$$\Pi = \sum_{\tau \in T} (P_{c\tau} - P_{s\tau}) D_{c\tau} \n+ \sum_{j=1}^{J} \sum_{\tau \in T_{j}} \left[ \sum_{i \in I_{cj}} [(P_{s\tau} - c_{i\tau})^{+} - r_{i}] Q_{i} \n+ \sum_{i \in I_{pj}} [(p_{i\tau} - P_{s\tau})^{+} - s_{i}] Q_{i} \right] \n$$
(2)

where  $\tau \in T$  are the subperiods within the month in question, each assumed to be of length 1 h, and where we have indexed spot price  $P_s$  and the execution prices  $c_i$  and  $p_i$  for the options by time periods, in case these execution prices are time sensitive (e.g., different prices for peak or off-peak periods for the same instrument). Note that once an instrument is purchased, it is available for all hours covered by the instrument (e.g., a peak-period call option of  $Q_i$  MW is available for any peak hour in the month, subject to requirements—usually  $24 \text{ h}$  in advance—to execute the option).

Using equation  $(2)$ , it is easily seen how this problem fits the standard form of equation (1). The profit function is clear (though additional payments to capital providers would be accounted for as in equation (2) in the risk constraint). As for the physical fulfillment constraints, these are also straightforward as long as the spot market is completely reliable as a source of power on the day (and very high reliability is typical of such markets). The VaR constraint in equation  $(1)$  is represented as

$$\Pr\left\{\Pi(Q,\,\tilde{D},\,\tilde{P}_s) - F \ge -VaR\right\} \ge \gamma \qquad (3)$$

where  $\Pi(O, \tilde{D}, \tilde{P}_{s})$  are the cash flows in equation (2) resulting from the vector of contracts  $O$ , where  $F$ represents fixed capital payment obligations, and VaR is the maximal Value-at-Risk allowed for the period in question, with confidence level  $\gamma$  (see Valueat-Risk and also [4, 9] for a discussion of VaR). In the case where there are sufficient subperiods in  $T$  to make the normality assumption reasonable for  $\Pi(Q, \tilde{D}, \tilde{P}_s)$ , this standard VaR constraint translates into a simple function of the mean and standard deviation of  $\Pi(Q, \tilde{D}, \tilde{P}_s)$ . Since the profit function is linear in  $Q_i$  for every realization of the random variables involved, finding the efficient frontier (in  $E\{\Pi\}$ , VaR space) is then easily solved in the standard fashion via quadratic programming. Multiperiod VaR constraints are also discussed in [7]. For more complex problems that arise in practice, including sophisticated models of the evolution of the spot price and various exotic options, Monte Carlo simulation (see Monte Carlo Simulation) with an appropriate optimization engine can be used.

#### **Implementation and Research Challenges**

It is unfamiliar territory for most organizations to integrate finance and supply management, and this is precisely what is required in order to have the full benefit of the options approach described here. Companies wishing to do so must radically expand the traditional focus of procurement on cost, quality, and dependability to include tracking of spot market conditions, valuing options in operational and hedging terms, and linking these activities to an appropriate risk management structure. Companies that have done this well have recognized the need to develop capabilities in trading, data management, and financial reporting and management. These include new skills in pricing and valuation of contracts, new approaches to managing the portfolio of sourcing options for key manufacturing inputs, and a very different approach to customer and customer segment valuation and management.

The open questions associated with B2B exchanges and contracting can be described under two general headings. First are the model-based developments needed to capture the essence of the supply-demand coordination problem and the necessary options-based instruments to achieve efficiency in particular market contexts. Second is the continuing development of theory to understand the necessary guidelines for the structure and governance of sustainable business models for the exchanges supporting these instruments. Open research questions in these areas are noted in all of the references listed, especially in  $[5]$ .

### **End Notes**

<sup>a.</sup>To the extent that these are based on principles of locational marginal prices, transmission constraints and options could also be included as part of the portfolio optimization described below.

<sup>b.</sup>Thus, to reserve  $Q_i$  MW of callable capacity during a specific period of length L, the price paid is  $r_i Q_i L$ , where the maximum reserved/callable capacity during any hour of the period is  $O_i$  MW. The reader can think of the reservation price in dollars per megawatt hour as the allocated cost to each hour of the period in question, though instruments will be typically traded for groups of hours in a month, for example, 100 MW of capacity callable for any peak hour during the month.

#### References

- [1] Allaz, B. & Vila, J.-L. (1993). Cournot competition, forward markets and efficiency, Journal of Economic Theory 59, 1-16.
- [2] Birge, J.R. (2000). Option methods for incorporating risk into linear capacity planning models, Manufacturing and Service Operations Management 2(1), 19-31.
- [3] Cachon, G.P. (2003). Supply chain coordination with contracts, in Handbooks in Operations Research and Management Science: Supply Chain Management, S. Graves & T. deKok, eds, North-Holland, Amsterdam, рр. 229-340.
- [4] Crouhy, M., Mark, R. & Galai, D. (2000). Risk Management, McGraw-Hill Trade, New York.
- Geman, H. (2005). Commodities and Commodity Deriva-[5] tives, Wiley Finance, New York.
- [6] Kaminski, V. (2004). *Managing Energy Price Risk*, Risk Books, London.
- [7] Kleindorfer, P.R. & Lide, L. (2005). Multi-period, VaRconstrained portfolio optimization in electric power, *The Energy Journal* **26** $(1)$ , 1–26.
- [8] Laffont, J.-J. & Tirole, J. (1998). A Theory of Incentives in Procurement and Regulation, The MIT Press, Cambridge, MA.
- [9] Marshall, C. & Siegel, M. (1997). Value at risk: implementing a risk measurement standard, The Journal of *Derivatives* **4**(Spring), 91–110.

# **6 Commodity Risk**

- [10] Mendelson, H. & Tunca, T. (2007). Strategic spot trading in supply chains, *Management Science* **53**, 742–759.
- [11] Williamson, O.E. (1985). *The Economic Institutions of Capitalism*, The Free Press, New York.
- [12] Wu, D.J. & Kleindorfer, P.R. (2005). Competitive options, supply contracting and electronic markets, *Management Science* **51**(3), 452–466.

**Related Articles**

**Electricity Forward Contracts**; **Risk Exposures**; **Swing Options**; **Value-at-Risk**.

PAUL R. KLEINDORFER
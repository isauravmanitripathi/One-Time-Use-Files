# **Counterparty Credit Riska**

Counterparty credit risk (CCR) is the risk that a counterparty in a financial contract will default prior to the expiration of the contract and will fail to make all the payments required by the contract. Only the contracts privately negotiated between the counterparties—over-the-counter (OTC) derivatives and securities financing transactions (SFT)—bear CCR. Exchange-traded derivatives are not subject to CCR because all contractual payments promised by these derivatives are guaranteed by the exchange.

CCR is similar to other forms of credit risk (such as lending risk) in that the source of economic loss is an obligor's default. However, CCR has two unique features that set it apart from lending risk:

- **Uncertainty of credit exposure** Credit exposure of one counterparty to the other is determined by the market value of all the contracts between these counterparties. While one can obtain the current exposure from the current contract values, the future exposure is uncertain because the future contract values are not known at present.
- **Bilateral nature of credit exposure** Since both counterparties can default and the value of many financial contracts (such as swaps) can change sign, the direction of future credit exposure is uncertain. Counterparty A may be exposed to default of counterparty B under one set of future market scenarios, while counterparty B may be exposed to default of counterparty A under another set of scenarios.

The uncertainty of future credit exposure makes managing and modeling CCR of the trading book challenging. For a comprehensive introduction to CCR, see [1, 5, 17].

# **Managing and Mitigating Counterparty Credit Risk**

One of the most conventional techniques of managing credit risk is setting counterparty-level *credit limits*. If a new transaction with the counterparty would result in the counterparty-level exposure exceeding the limit, the transaction is not allowed. The limits usually depend on the counterparty's credit quality: higher rated counterparties have higher limits. To compare uncertain future exposure with a deterministic limit, *potential future exposure* (PFE) profiles are calculated from exposure probability distributions at future time points. PFE profiles are obtained by calculating a quantile of exposure at a high confidence level (typically, above 90%). Some institutions use different exposure measures, such as *expected exposure* (EE) profiles, for comparing with the credit limit. It is important to understand that a given credit limit amount is meaningful only in the context of a given exposure measure (e.g., 95%-level quantile).

Future credit exposure can be greatly reduced by means of risk-mitigating agreements between two counterparties, which include *netting agreements, margin agreements*, and *early termination agreements*. Netting agreement is a legally binding contract between two counterparties that, in the event of default of one of them, allows aggregation of transactions between these counterparties. Instead of each trade between the counterparties being settled separately, the entire portfolio covered by the netting agreement is settled as a single trade whose value equals the net value of the portfolio. Margin agreements limit the potential exposure of one counterparty to the other by means of requiring collateral should the unsecured exposure exceed a predefined threshold. The threshold value depends primarily on the credit quality of the counterparty: the higher the credit quality, the higher the threshold.

There are two types of early termination agreements: *termination clauses* and *downgrade provisions*. Termination clause is specified at the trade level. A unilateral (bilateral) termination clause gives one (both) of the counterparties the right to terminate the trade at the fair market value at a predefined set of dates. Downgrade provision is specified for the entire portfolio between two counterparties. Under a unilateral (bilateral) downgrade provision, the portfolio is settled at its fair market value the first time the credit rating of one (either) of the counterparties falls below a predefined level.

## **Contract-level Exposure**

Let us consider a financial institution (we will call it a *bank* for brevity) that has a single derivative contract with a counterparty. The bank's *exposure* to the counterparty at a given future time is given by the bank's economic loss in the event of the counterparty's default at that time. If the counterparty defaults, the bank must close out its position with the counterparty. To determine the loss arising from the counterparty's default, it is convenient to assume that the bank enters into a similar contract with another counterparty in order to maintain its market position. Since the bank's market position is unchanged after replacing the contract, the loss is determined by the contract's *replacement cost* at the time of default.

If the trade value at the time of default is negative for the bank, the bank receives this amount when it replaces the trade, but has to forward the money to the defaulting counterparty, so that the net loss is zero. If the trade value at the time of default is positive for the bank, the bank pays this amount when replacing the trade, but receives nothing (assuming no recovery) from the defaulting counterparty, so that the net loss is equal to the trade value.

Summarizing this, we can write the bank's credit exposure to the counterparty at future time *t* as

$$E_i(t) = \max\{V_i(t), 0\} \tag{1}$$

where *Vi(t)* is the value of trade *i* with the counterparty at time *t* from the bank's point of view and *Ei(t)* the bank's contract-level exposure to the counterparty created by trade *i* at time *t*.

Since the contract value changes unpredictably over time as the market moves, only the current exposure is known with certainty, while the future exposure is uncertain.

# **Counterparty-level Exposure and Netting Agreements**

If the bank has more than one trade with the counterparty and counterparty risk is not mitigated in any way, the bank's exposure to the counterparty is equal to the sum of the contract-level exposures:

$$E_{c}(t) = \sum_{i} E_{i}(t) = \sum_{i} \max\{V_{i}(t), 0\} \qquad (2)$$

where the subscript 'c' stands for 'counterparty'.

Netting agreements allow for a significant reduction of the credit exposure. There may be several netting agreements between the bank and the counterparty, as well as some trades that are not covered by any of the netting agreements. Counterparty-level exposure in this most general case is given by

$$E_{c}(t) = \sum_{k} \max \left[ \sum_{i \in \text{NA}_{k}} V_{i}(t), 0 \right]$$
$$+ \sum_{i \notin \text{[NA]}} \max [V_{i}(t), 0] \tag{3}$$

The inner summation in the first term of equation (3) aggregates the values of all trades covered by the *k*th netting agreement (hence the notation *i* ∈ NA*<sup>k</sup>* ), while the outer summation aggregates exposures across all netting agreements. The second term in equation (3) is simply the sum of the contract-level exposures of all trades that do not belong to any netting agreement (hence the notation *i /*∈ {NA}).

# **Margin Agreements and Collateral Modeling**

Margin agreements can further reduce credit exposure. Margin agreements can be either *unilateral* or *bilateral*. Under a unilateral agreement, only one of the counterparties has to post collateral. If the agreement is bilateral, both counterparties have to post collateral.

Usually a margin agreement covers one or more netting agreements. We can generalize equation (3) by specifying collateral amount *Ck(t)* available to the bank under netting agreements NA*<sup>k</sup>* at time *t* with the convention that this amount is positive when the bank holds collateral and negative when the bank has posted collateral:

$$E_{c}(t) = \sum_{k} \max \left[ \sum_{i \in NA_{k}} V_{i}(t) - C_{k}(t), 0 \right] + \sum_{i \notin \{NA\}} \max[V_{i}(t), 0]$$
(4)

For netting agreements that are not covered by a margin agreement, collateral is identically zero.

#### *Unilateral Margin Agreements*

Let us consider a single unilateral (in the bank's favor) margin agreement with the threshold *H*<sup>c</sup> ≥ 0 and minimum transfer amount (MTA). When the portfolio value exceeds the threshold, the counterparty must post collateral to keep the bank's exposure from rising above the threshold. As the exposure drops below the threshold, the bank returns collateral to the counterparty. MTA limits the frequency of collateral exchange. It is difficult to model collateral subject to MTA exactly because that would require daily simulation time points, which is not feasible given the long-term nature of exposure modeling. In practice, the actual threshold  $H_c$  is often replaced by the effective threshold defined as  $H_c^{(e)} = H_c +$ MTA. After this replacement, the margin agreement is treated as if it had zero MTA.

The simplest approach to modeling collateral is to limit the future exposure from above by the threshold (i.e., for all scenarios with portfolio value above the threshold, set the exposure equal to the threshold). However, this approach is too simplistic because it ignores the time lag between the last delivery of collateral and the time when the loss is realized. This time lag is known as the *margin period of risk* (*MPR*), which we will denote by  $\delta t$ . While the MPR is not known with certainty, it is typically assumed to be a deterministic number that is defined at the margin agreement level. Its value depends on the contractual margin call frequency and the liquidity of the portfolio. For example,  $\delta t = 2$  weeks is usually assumed for portfolios of liquid contracts and daily margin call frequency.

Applying the rules of posting collateral under the assumption of the effective threshold with zero MTA and taking into account the MPR, the collateral  $C(t)$ available to the bank at time  $t$  is given by

$$C(t) = \max\{V(t - \delta t) - H_c^{(e)}, 0\}$$
(5)

where  $V(t)$  is the portfolio value from the bank's point of view at time  $t$ .

#### **Bilateral Margin Agreements**

Under a bilateral margin agreement, both the counterparty and the bank have to post collateral: the counterparty posts collateral when the bank's exposure to the counterparty exceeds the counterparty's threshold, while the bank posts collateral when the counterparty's exposure to the bank exceeds the bank's threshold. Since we are doing our analysis from the point of view of the bank, we will keep the counterparty's threshold  $H_c$  nonnegative, but will specify the bank's threshold  $H_{\rm b}$  as *nonpositive*. Then, the bank posts collateral when the portfolio value (defined from the bank's point of view) is *below* the bank's threshold. The MTA is the same for the bank and the counterparty and MTA  $> 0$ .

Similar to the unilateral case, we will create effective thresholds for the bank and for the counterparty. Effective threshold for the counterparty,  $H^{(e)}_{c}$ , remains unchanged. From the counterparty's point of view, effective threshold for the bank must be defined in exactly the same way. After taking into account that we do not switch our point of view and  $H_{\rm b} < 0$ , the definition of the effective threshold for the bank will be  $H_{\rm b}^{(\rm e)} = H_{\rm b} - \text{MTA}$ . Now the bilateral agreement can be treated as if it had zero MTA.

Collateral available to the bank at time  $t$  under the bilateral agreement is modeled as

$$C(t) = \max\{V(t - \delta t) - H_{\rm c}^{(\rm e)}, 0\}$$
  
+  $\min\{V(t - \delta t) - H_{\rm b}^{(\rm e)}, 0\}$  (6)

The first term in the right-hand side of equation  $(6)$ describes the scenarios when the bank receives collateral (i.e.,  $C(t) > 0$ ), while the second term describes the scenarios when the bank posts collateral (i.e.,  $C(t) < 0$ ).

For more details on collateral modeling, see [9, 15. 161.

#### **Simulating Credit Exposure**

Because of the complex nature of banks' portfolios, exposure distribution at future time points is usually obtained via Monte Carlo Simulation process. This process typically consists of three major steps:

- Scenario generation Dynamics of market risk . factors (e.g., interest rates, foreign exchange (FX) rates, etc.) is specified *via* relatively simple stochastic processes (e.g., geometric Brownian motion). These processes are calibrated either to historical data or to market implied data. Future values of the market risk factors are simulated for a fixed set of future time points.
- **Instrument valuation** For each simulation time ٠ point and for each realization of the underlying market risk factors, valuation is performed for each trade in the counterparty portfolio.

• Aggregation For each simulation time point and for each realization of the underlying market risk factors, counterparty-level exposure is obtained by applying the necessary netting and collateral rules, conceptually described by equations  $(3)$  and  $(4)$ .

The outcome of this process is a set of realizations of the counterparty-level exposure (each realization corresponds to one market scenario) at each simulation time point.

Because of the computational intensity required to calculate counterparty exposures—especially for a bank with a large portfolio—certain compromises between the accuracy and the speed of the calculation are usually made: relatively small number of market scenarios (typically, a few thousand) and simulation time points (typically, in the  $50-200$  range), simplified valuation methods, and so on.

For more details on simulating credit exposure, see [7, 17].

## **Pricing Counterparty Risk—Unilateral** Approach

Let us assume that the bank is default-risk-free. Then, when pricing transactions with a counterparty, the bank should require a risk premium to be compensated for the risk of the counterparty defaulting. The market value of this risk premium, defined for the entire portfolio of trades with the counterparty, is known as unilateral credit valuation adjustment (CVA).

A Risk-neutral Pricing valuation framework is used for pricing CCR. The bank's economic loss arising from the counterparty's default and discounted to today is given by

$$L_{\rm u-l} = 1_{\{\tau_{\rm c} \le T\}} (1 - R_{\rm c}) E_{\rm c}(\tau_{\rm c}) \frac{B_0}{B_{\tau_{\rm c}}} \tag{7}$$

where  $\tau_c$  is the time of default of the counterparty;  $1_{\{A\}}$  is the indicator function that assumes the value 1 if Boolean variable  $A$  is TRUE and value 0, otherwise;  $E_c(t)$  is the bank's exposure to counterparty's default at time  $t$ ;  $R_c$  is the counterparty **Recovery Rate** (i.e., percentage of the bank's exposure to the counterparty that the bank will be able to recover in the event of the counterparty's default); and  $B_t$  is the value of the money-market account at time  $t$ .

One should keep in mind that counterparty-level exposure  $E_c(t)$  incorporates all netting and margin agreements between the bank and the counterparty, as discussed above.

Unilateral CVA is obtained by taking the riskneutral expectation of the loss in equation  $(7)$ . Under the assumption that recovery rate is independent of the market factors and the time of default, this results in

$$\text{CVA}_{\text{u}-\text{l}} = (1 - \overline{R}_{\text{c}}) \int_{0}^{T} \text{EE}_{\text{c}}^{*}(t) \, \text{d} \, \text{PD}_{\text{c}}(t) \qquad (8)$$

where  $EE_{c}^{*}(t)$  is the risk-neutral discounted EE at time  $t$ , conditional on the counterparty defaulting at time  $t$ , given by

$$\text{EE}_{\text{c}}^{*}(t) = \text{E}^{\mathcal{Q}} \left[ \left. \frac{B_{0}}{B_{t}} E_{\text{c}}(t) \right| \tau_{\text{c}} = t \right] \tag{9}$$

and  $\overline{R}_{c}$  is the expected recovery rate;  $PD_{c}(t)$  is the counterparty's cumulative from today to time  $t$ , estimated today; and  $T$  is the maturity of the longest trade in the portfolio.

The term structure of the risk-neutral PDs is obtained from the Credit Default Swaps spreads quoted in the market  $[19]$ .

We would like to emphasize that the expectation of the discounted exposure at time  $t$  in equation (9) is conditional on the counterparty's default occurring at time  $t$ . This conditioning is material when there is a significant dependence between the exposure and the counterparty credit quality. This dependence, known as right/wrong-way risk, was first considered in [8] and [12]. To account for it, the counterparty's credit quality must be modeled jointly with the market risk factors. For more details on modeling right/wrongway risk, see [4, 10, 18].

In practice, the dependence between exposure and the counterparty's credit quality is often ignored and conditioning on default in equation (9) is removed. Discounted EE is calculated for a set of simulation time points  $\{t_k\}$  under the exposure simulation framework outlined above. Then, CVA is calculated by approximating the integral in equation  $(8)$  by a sum:

$$\text{CVA}_{u-l} \approx (1 - \overline{R}_{c}) \sum_{k} \text{EE}_{c}^{*}(t_{k})$$
$$\times [\text{PD}_{c}(t_{k-1}) - \text{PD}_{c}(t_{k})] \qquad (10)$$

Since the exposure expectation in equation  $(10)$  is risk neutral, scenario models for all market risk factors should be arbitrage free. This is achieved by appropriate calibration of drifts. Moreover, risk factor volatilities should be calibrated to the available market prices of options on the risk factors.

For more details on unilateral CVA, see [3].

## **Pricing Counterparty Risk—Bilateral** Approach

In reality, banks are not default-risk-free. Because of the bilateral nature of credit exposure, the bank and the counterparty will never agree on the fair price of CCR if they apply unilateral pricing outlined above: each of them will demand a risk premium from the other. The bilateral approach specifies a single quantity-known as bilateral CVA-that accounts both for the bank's loss caused by the counterparty's default and the counterparty's loss caused by the bank's default.

Bilateral loss of the bank is given by

$$L_{\rm b-l} = 1_{\{\tau_{\rm c} \le T\}} 1_{\{\tau_{\rm c} < \tau_{\rm b}\}} (1 - R_{\rm c}) E_{\rm c}(\tau_{\rm c}) \frac{B_0}{B_{\tau_{\rm c}}}$$
$$- 1_{\{\tau_{\rm b} \le T\}} 1_{\{\tau_{\rm b} < \tau_{\rm c}\}} (1 - R_{\rm b}) E_{\rm b}(\tau_{\rm b}) \frac{B_0}{B_{\tau_{\rm b}}}$$
(11)

where  $\tau_{\rm b}$  is the time of default of the bank;  $E_{\rm b}(t)$  is the counterparty's exposure to bank's default at time t; and  $R_{\rm b}$  is the bank recovery rate (i.e., percentage of the counterparty's exposure to the bank that the counterparty will be able to recover in the event of the bank's default).

The first term in equation  $(11)$  describes the bank's loss when the counterparty defaults, but the bank does not default. The second term describes the loss of the counterparty in the event of the bank's default and the counterparty's survival. From the bank's point of view, the counterparty's loss is gain arising from the bank's option not to pay the counterparty when the bank defaults, so this term is subtracted from the bank's loss. Equation (11) is completely symmetric: if we change the sign of the right-hand side, we will obtain the bilateral loss of the counterparty.

Bilateral CVA is obtained by taking risk-neutral expectation of equation  $(11)$ :

$$\begin{split} \text{CVA}_{\text{b}-\text{l}} &= (1 - \overline{R}_{\text{c}}) \int_{0}^{T} \text{EE}_{\text{c}}^{*}(t) \\ &\times \text{Pr}[\tau_{\text{b}} > t | \tau_{\text{c}} = t] \, \text{dPD}_{\text{c}}(t) \\ &- (1 - \overline{R}_{\text{b}}) \int_{0}^{T} \text{EE}_{\text{b}}^{*}(t) \\ &\times \text{Pr}[\tau_{\text{c}} > t | \tau_{\text{b}} = t] \, \text{dPD}_{\text{b}}(t) \end{split} \tag{12}$$

where  $\text{EE}_{c}^{*}(t)$  is the discounted EE of the counterparty to the bank at time  $t$ , conditional on the counterparty defaulting at time  $t$ , defined in equation (9), and  $\text{EE}_{\text{h}}^{*}(t)$  is the discounted EE of the bank to the counterparty at time  $t$ , conditional on the bank defaulting at time  $t$ , defined as

$$\text{EE}_{\text{b}}^{*}(t) = \text{E}\left[\left.E_{\text{b}}(t)\frac{B_{0}}{B_{t}}\right|\tau_{\text{b}} = t\right] \tag{13}$$

If the dependence between credit exposure and the credit quality of the counterparty and of the bank can be ignored, the conditional expectations in equations  $(9)$  and  $(13)$  should be replaced with the unconditional ones. As expected, equation  $(12)$  is symmetric between the bank and the counterparty, so that the bank and the counterparty will always agree on the price of CCR for their portfolio.

One can use Default Time Copulas; Gaussian **Copula Model; Copulas: Estimation** to express the conditional probabilities in equation  $(12)$  as functions of the counterparty's and the bank's risk-neutral PDs. For example, if the normal copula model [13] is used to describe the dependence between  $\tau_{\rm c}$  and  $\tau_{\rm b}$ , the conditional probabilities in equation  $(12)$  take the form

$$\Pr[\tau_{\rm b} > t | \tau_{\rm c} = t]$$
  
= 1 - \Phi \left( \frac{\Phi^{-1}[PD\_{\mu}(t)] - \rho \Phi^{-1}[PD\_{\cdot}(t)]}{\sqrt{1 - \rho^2}} \right) (14)

and

$$\Pr[\tau_{c} > t | \tau_{b} = t]$$
  
= 1 -  $\Phi \left( \frac{\Phi^{-1}[\text{PD}_{c}(t)] - \rho \Phi^{-1}[\text{PD}_{b}(t)]}{\sqrt{1 - \rho^{2}}} \right)$  (15)

where  $\rho$  is the normal copula correlation and  $\Phi(\cdot)$  is the standard normal cumulative distribution function.

#### **Portfolio Loss and Economic Capital**

Until now we have discussed modeling credit exposure and losses at the counterparty level. However, the distribution of the credit loss of the bank's entire trading book provides more complete information about the risk a bank is taking. Portfolio loss distribution is needed for such risk management tasks as calculation and allocation of **Economic Capital**  $(EC)$ . For a comprehensive introduction to EC for CCR, see [14].

Portfolio credit loss  $L(T)$  for a time horizon T can be expressed as the sum of the counterparty-level losses over all counterparties:

$$L(T) = \sum_{j} 1_{\{\tau_j \le T\}} (1 - R^{(j)}) E^{(j)}(\tau_j) \frac{B_0}{B_{\tau_j}} \qquad (16)$$

where  $\tau_j$  is the time of default of counterparty  $j$ ;  $R^{(j)}$  is the recovery rate for counterparty j; and  $E^{(j)}(t)$  is the bank's counterparty-level exposure at time  $t$  created by all trades that the bank has with counterparty  $j$ .

The economic capital  $EC_q(T)$  for time horizon T and confidence level  $q$  is given by

$$\mathrm{EC}_{a}(T) = Q_{a}[L(T)] - \mathrm{E}[L(T)] \tag{17}$$

where  $Q_a[X]$  is the quantile of random variable X at confidence level  $q$  (in risk management, this quantity is often referred to as Value-at-Risk (VaR)). The distribution of portfolio loss  $L(T)$  can be obtained from equation (16) *via* joint Monte Carlo simulation of trade values for the entire bank portfolio and of default times of individual counterparties.

However, the joint simulation process is very expensive computationally and is often replaced by

a simplified approach, where simulation of counterparty defaults is completely separate from exposure simulation. The simplified approach is a two-stage process. During the first stage, exposure simulation is performed and a deterministic loan equivalent exposure (LEQ) is calculated from the exposure distribution for each counterparty. The second stage is a simulation of counterparty default events according to one of the credit risk portfolio models (see **Credit** Migration Models; Structural Default Risk Models;  $\text{CreditRisk+})$  that are used for loan portfolios. Portfolio credit loss is calculated as

$$L(T) = \sum_{j} 1_{\{\tau_j \le T\}} (1 - R^{(j)}) \text{LEQ}^{(j)}(T) \qquad (18)$$

where  $\text{LEO}^{(j)}(T)$  is the LEO of counterparty *j* for time horizon  $T$ .

Note that many loan portfolio models do not produce the time of default explicitly. Instead, they only distinguish between two events: "default has happened prior to the horizon (i.e.,  $\tau_i \leq T$ )" and "default has not happened prior to the horizon (i.e.,  $\tau_i > T$ ". Note also that, because the time of default is not known, discounting to present is not applied in equation  $(18)$ .

For an infinitely fine-grained portfolio with independent exposures, it has been shown  $[6, 20]$  that LEQ is given by the EE averaged from zero to  $T$ —this quantity is often referred to as *expected positive exposure*  $(EPE)$ :

$$\text{EPE}^{(j)}(T) \equiv \frac{1}{T} \int_{0}^{T} \text{EE}^{(j)}(t) dt \qquad (19)$$

If one uses LEQ given by equation  $(19)$  for a real portfolio, the EC will be understated because both exposure volatility and correlation between exposures are ignored. However, this understated EC can be used in defining a scaling parameter commonly known as *alpha*:

$$\alpha_q(T) = \frac{\text{EC}_q^{\text{(Real)}}(T)}{\text{EC}_q^{\text{(EPE)}}(T)}\tag{20}$$

where  $EC_q^{(Real)}(T)$  is the EC of the real portfolio with stochastic exposures, and  $EC_q^{(EPE)}(T)$  is the EC of the fictitious portfolio with stochastic exposures replaced by EPE.

If alpha of a real portfolio can be estimated, its LEQ can be defined according to

$$\text{LEQ}^{(j)}(T) = \alpha_q(T) \text{EPE}^{(j)}(T) \tag{21}$$

Because the EC of a portfolio with deterministic exposures is a homogeneous function of the exposures, using the LEQ defined in equation (21) will produce the correct EC*(*Real*) <sup>q</sup> (T )*. The caveat of this approach is that one has to run a joint simulation of trade values and counterparties' defaults to calculate *alpha*.

Several estimates of typical values of *alpha* for a large dealer portfolio and the time horizon *T* = 1 year are available. An International Swaps and Derivatives Association (ISDA) survey [11] has reported *alpha* calculated by four large banks for their actual portfolios to be in the 1.07–1.10 range. Theoretical estimates of *alpha* under a set of simplifying assumptions [6, 20] are 1.1 when market-credit correlations are ignored, and 1.2 when they are not.

The framework described above has found its place in the regulatory capital calculations under Basel II (*see* **Regulatory Capital**): a slightly modified version of equation (21) is used to calculate exposure at default (EAD) under the internal models method for CCR [2]. Basel fixes *alpha* at 1.4, but it allows banks to calculate their own *alpha*, subject to the supervisory approval and a floor of 1.2.

## **End Notes**

a*.* The opinions expressed here are those of the author and do not necessarily reflect the views or policies of the author's employer.

## **References**

- [1] Arvanitis, A. & Gregory, J. (2001). *Credit: The Complete Guide to Pricing, Hedging and Risk Management*, Risk Books.
- [2] Basel Committee on Banking Supervision (2006). *International Convergence of Capital Measurement and Capital Standards*, A Revised Framework.
- [3] Brigo, D. & Masetti, M. (2005). Risk neutral pricing of counterparty credit risk, in *Counterparty Credit Risk Modelling*, M. Pykhtin, ed., Risk Books.
- [4] Brigo, D. & Pallavicini, A. (2008). Counterparty risk and contingent CDS under correlation, *Risk* February, 84–88.

- [5] Canabarro, E. & Duffie, D. (2003). Measuring and marking counterparty risk, in *Asset/Liability Management for Financial Institutions*, L. Tilman, ed., Institutional Investor Books.
- [6] Canabarro, E., Picoult, E. & Wilde, T. (2003). Analysing counterparty risk, *Risk* September, 117–122.
- [7] De Prisco, B. & Rosen, D. (2005). Modeling stochastic counterparty credit exposures for derivatives portfolios, in *Counterparty Credit Risk Modelling*, M. Pykhtin, ed., Risk Books.
- [8] Finger, C. (2000). Toward a better estimation of wrongway credit exposure, *Journal of Risk Finance* **1**(3), 43–51.
- [9] Gibson, M. (2005). Measuring counterparty credit exposure to a margined counterparty, in *Counterparty Credit Risk Modelling*, M. Pykhtin, ed., Risk Books.
- [10] Hille, C., Ring, J. & Shimamoto, H. (2005). Modelling counterparty credit exposure for credit default swaps, *Risk* May, 65–69.
- [11] ISDA-TBMA-LIBA (2003). *Counterparty Risk Treatment of OTC Derivatives and Securities Financing Transactions*, June.
- [12] Levin, R. & Levy, A. (1999). Wrong way exposure—are firms underestimating their credit risk? *Risk* July, 52–55.
- [13] Li, D. (2000). On default correlation: a copula approach, *Journal of Fixed Income* **9**, 43–54.
- [14] Picoult, E. (2005). Calculating and hedging exposure, credit value adjustment and economic capital for counterparty credit risk, in *Counterparty Credit Risk Modelling*, M. Pykhtin, ed., Risk Books.
- [15] Pykhtin, M. (2009). Modeling credit exposure for collateralized counterparties, *Journal of Credit Risk*; to be published.
- [16] Pykhtin, M. & Zhu, S. (2006). Measuring counterparty credit risk for trading products under Basel II, in *Basel Handbook*, 2nd Edition, M. Ong, ed., Risk Books.
- [17] Pykhtin, M. & Zhu, S. (2007). A guide to modeling counterparty credit risk, *GARP Risk Review* July/August, 16–22.
- [18] Redon, C. (2006). Wrong way risk modelling, *Risk* April, 90–95.
- [19] Schonbucher, P. (2003). *Credit Derivatives Pricing Models*, Wiley.
- [20] Wilde, T. (2005). Analytic methods for portfolio counterparty risk, in *Counterparty Credit Risk Modelling*, M. Pykhtin, ed., Risk Books.

## **Related Articles**

**Default Time Copulas**; **Economic Capital**; **Exposure to Default and Loss Given Default**; **Monte Carlo Simulation**; **Risk-neutral Pricing**.

MICHAEL PYKHTIN
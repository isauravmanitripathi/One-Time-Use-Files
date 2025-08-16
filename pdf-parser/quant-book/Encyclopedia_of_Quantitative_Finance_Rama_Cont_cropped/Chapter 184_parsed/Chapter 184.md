# **Constant Maturity Credit Default Swap**

A constant maturity credit default swap (CM CDS) is a credit derivative with payments linked to periodic fixings of a standard CDS rate with a fixed tenor (e.g., 5 years) on a particular credit entity. In business practice, CM CDS is usually presented as an elaboration of a plain CDS suitable for use in trading strategies expressing certain views on the steepening or flattening of credit spreads. From the point of view of quantitative modeling, CM CDS is best understood as a simple representative of a family of structured credit exotics, more complicated members of which would depend on a nonlinear combination of CDS spreads of more than one maturity and/or refer to more than one credit entity. Both business practice and quantitative modeling of CM CDS are based on ideas and techniques originally developed for CMS-linked fixed income exotics and adapted to credit modeling.

## Instrument Structure

A CM CDS trade usually consists of two legs, one of which is a CM CDS leg, which is a sequence of payments  $P_1, P_2, \ldots, P_n$  made on a schedule of payment dates  $T_1', T_2', \ldots T_n'$  (which is typically set following conventions of a standard CDS schedule) and is computed by the following formula:

$$P_i = \Delta_i \min[C, a \cdot S(T_i, T_{i+M})] \tag{1}$$

Here  $S(T_i, T_{i+M})$  is the rate of a CDS spanning  $M$  payment periods and observed at the fixing date  $T_i$  associated with the payment date  $T'_i$ ,  $\Delta_i$  is the daycount fraction for the accrual period  $i$ ,  $a$  is the multiplier called *participation rate*, and  $C$  is the fixed rate reset cap.<sup>a</sup> Notional amount of the trade is set to 1. The fixing normally happens at the beginning of the accrual period, so that  $T'_{i} = T_{i+1}^{b}$ . In the case of a default of the reference credit, the fraction of the last payment accrued before the default is paid and further payments stop.

The second leg of a CM CDS is normally a standard CDS protection leg; however, structures where the second leg is either a standard CDS premium leg or another CM CDS leg corresponding to a different tenor are also possible. The quote for a CM CDS is usually given in terms of the participation rate,  $a$ , of the CM CDS leg. With the second leg being the standard CDS protection leg, a participation rate of less than 100% reflects the expectation of rising credit spreads, whereas a participation rate of more than  $100\%$  corresponds to the expectation of decreasing credit spreads.

## **Trading Aspects**

Descriptions of CM CDS structures started circulating in research communications of securities firms in early 2004, [3, 5, 6]. On November 21, 2005, ISDA provided a publication [4] setting a standard for the terms and condition of the CM CDS leg, including a mechanism for the determination of CDS rate resets. Establishing undisputable resets for CDS rates presents a problem because no standard source of information on CDS rates similar to Telerate pages of interest rates has emerged.

The primary mechanism stipulated by ISDA compels the seller of protection in a CM CDS to make a binding bid for the fixed rate premium that the seller is willing to pay in exchange for protection in a standard CDS on the same credit entity. This bid will be used as a CDS rate reset and is expected to be a good proxy for the true CDS rate because the seller has no incentive to quote a value that is too high (in which case the seller can be forced to buy overpriced CDS protection) or too low (in which case the seller will lose on the coming CM CDS payment). A fallback mechanism, which comes into effect if the receiver fails to provide a bid, puts on the buyer the burden of obtaining CDS quotes from a set of fallback dealers, subsequently using the highest quote as the rate reset.

At the time of this study, the volume of CM CDS transactions remains limited, taming optimistic predictions for the development of multilayered structures, such as tranches of CM CDS portfolios, but not destroying such prospects completely. We also note that more exotic structures with payoffs linked to nonlinear combinations of CDS rates of different maturities were observed in the market and have potential for further growth.

# **Ouantitative Modeling**

The present value of a CM CDS leg is given by the sum of expectations of the payments (1) discounted under risk-neutral measure:

$$V = \sum_{i} \Delta_{i} E[\min[C, a \cdot S_{T_{i}}(T_{i}, T_{i+M})] P_{T'_{i}} D(0, T'_{i})] + A$$
(2)

$$A = \sum_{i} \sum_{T'_{i-1} < \tau'_{k} \le T'_{i}} \Delta(T'_{i-1}, \tau'_{k})$$
$$\times E[\min[C, a \cdot S_{T_{i}}(T_{i}, T_{i+M})]$$
$$\times (P_{\tau'_{k-1}} - P_{\tau'_{k}})D(0, \tau'_{k})] \tag{3}$$

Here  $P_{T'}$  is the indicator of survival of the underlying name until time  $T'_i$ , and  $D(0, T'_i)$  is the stochastic discount factor from 0 to  $T'_i$ . We equipped the notation  $S_{T_i}(T_i, T_{i+M})$  for the CDS rate reset with a subscript  $T_i$  to indicate that this rate is modeled as a value at time  $T_i$  of a certain stochastic process. The contribution  $A$  of the interest accrued within the period of time  $\Delta(T'_{i-1}, \tau'_k)$  between the last coupon payment and the time of default is written in a discretized form using a sufficiently frequent subdivision  $\{\tau'_k\}$  of the segment  $[T'_{i-1}, T'_i]$ .

We consider major types of modeling approaches in the order of increasing sophistication, including the nonstochastic approximation, convexity adjustments, instantaneous hazard rate modeling, and forward credit spread modeling.

#### Nonstochastic Approximation

We can obtain a simple approximation assuming that the CDS rates are nonstochastic. In this approximation, each process  $S_t(T_i, T_{i+M})$  of the expectation of the time  $T_i$  CDS rate reset conditional on the information accumulated until time  $t$  is frozen at  $t = 0$ . As a result, the relevant CM CDS rate at date  $T_i$  is equal to the forward CDS rate  $F(T_i, T_{i+M})$ , which can be expressed in terms of the survival probability function,  $p_s(t) = E[P_t]$ , and the deterministic discount function,  $D_0(t) = E[D(0, t)],$ 

$$A_{j} = \sum_{T_{j-1} < \tau_{k} \leq T_{j}} \Delta(T_{j-1}, \tau_{k})$$
$$\times (p_{s}(\tau_{k-1}) - p_{s}(\tau_{k})) D_{0}(\tau_{k}) \tag{5}$$

Here R is the recovery rate and  $\{\tau_i\}$  is a subdivision of the segment  $[T_i, T_{i+M}]$ , sufficiently frequent to enable an accurate calculation of the default leg and the contributions  $A_i$  of the premium accrued in the time  $\Delta(T_{i-1}, \tau_k)$  between the last CDS coupon date and the event of default.<sup>c</sup>

The value of a CM CDS leg obtained by setting  $S_{T_i}(T_i, T_{i+M}) \to F(T_i, T_{i+M}), P_{T_i'} \to p_s(T_i'), \text{ and } D$  $(0, T'_i) \to D_0(T'_i)$  in equations (2-3) gives a quick estimate sufficient for a qualitative understanding of the relationship between the term structure of CDS spreads and the CM CDS participation rate but missing the essential effects of the dynamics of credit spreads. Indeed, even apart from the obvious problem of not handling the cap condition, the expectation  $E[S_{T_i}(T_i, T_{i+M})P_{T_i'}D(0, T_i')]$  can be very different from  $F(T_i, T_{i+M})p_s(T'_i)D_0(T'_i)$  when credit spread volatility is taken into account.

#### Convexity Adjustments

In this section a discussion on volatility-dependent corrections to the results obtained in the nonstochastic approximation is provided. Such correction can be either derived from a fully consistent model capable of computing  $E[S_{T_i}(T_i, T_{i+M})P_{T_i'}D(0, T_i')]$  or introduced in an *ad hoc* manner. We begin by looking at the convexity adjustments in the more limited sense of instrument-specific adjustments without building a full-fledged model. In the remainder of this article, we omit the discussion of the accrued interest term A and focus on the main term in equation  $(2)$ .<sup>d</sup>

The first step is to switch to a new measure in which the process  $S_t(T_i, T_{i+M})$  is a martingale. The numeraire  $N_t(T_i, T_{i+M})$  of the desired measure is known as the risky basis point value (RBPV) and is given as

$$F(T_{i}, T_{i+M}) = \frac{(1-R)\sum_{T_{i}<\tau_{j}\leq T_{i+M}}(p_{s}(\tau_{j-1}) - p_{s}(\tau_{j}))D_{0}(\tau_{j})}{\sum_{j=i+1}^{i+M}(\Delta_{j}p_{s}(T_{j})D_{0}(T_{j}) + A_{j})} \qquad N_{t}(T_{i}, T_{i+M}) = P_{t} \sum_{j=i+1}^{i+M} \left(\Delta_{j}B_{t}(T_{j}) + \sum_{T_{j-1}<\tau_{k}\leq T_{j}}\Delta(T_{j-1}, \tau_{k})H_{t}(\tau_{k-1}, \tau_{k})\right)$$

$$(4) \qquad (6)$$

where  $B_t(T_i)$  is the time t value of a risky unit payment at  $T_i$  and  $H_t(\tau_{k-1}, \tau_k)$  is the time t value of a unit payment at  $\tau_k$  conditional on a default event in the interval  $(\tau_{k-1}, \tau_k]$ . We used a discretized form of the accrued interest consistent with equa $tion (3)$ .

The existence of the required measure follows from a representation of the CDS rate as a ratio of two tradable assets:

$$S_t(T_i, T_{i+M}) = L_t(T_i, T_{i+M}) / N_t(T_i, T_{i+M}) \tag{7}$$

where  $L_t(T_i, T_{i+M})$  is the time t expectation of the CDS default leg.

$$L_t(T_i, T_{i+M}) = (1 - R)P_t \sum_{T_i < \tau_k \le T_{i+M}} H_t(\tau_{k-1}, \tau_k) \tag{8}$$

(For a rigorous discussion of the mathematics of measure change involving risky basis point value as a numeraire, see [8].) After the measure change, the contribution of each individual coupon payment to the CM CDS leg can be written as

$$\Delta_i N_0(T_i, T_{i+M}) E\left[\frac{B_{T_i}(T'_i)}{N_{T_i}(T_i, T_{i+M})} f(S_{T_i}(T_i, T_{i+M}))\right]$$
(9)

where  $f(X) = \min(C, aX)$ . The next step is to assume that  $S_t$  follows a lognormal martingale,  $F \exp(\sigma W_t - 0.5\sigma^2 t)$ , and to replace the true value of the ratio  $B_{T_i}(T_i')/N_{T_i}(T_i,T_{i+M})$  by the value of a suitable increasing function  $g(S)$  at  $S = S_{T_i}$ . Imposing the condition  $N_0(T_i, T_{i+M})g(F(T_i, T_{i+M}))$  $= p_s(T_i')D_0(T_i')$  ensures that the calculation of the average (9) for  $\sigma = 0$  brings us back to the nonstochastic valuation. A nonzero volatility  $\sigma > 0$ leads to a positive correction due to the convexity of the product  $g(S)f(S)$  in the region of values of S close to  $F(T_i, T_{i+M})$  and distant from the  $\text{cap } C$ .

This approach has an advantage of relative simplicity and potential ability of calibrating the model volatility  $\sigma$  to CDS options. The disadvantage is an uncontrollable assumption in the choice of the function  $g(S)$ .

#### Instantaneous Hazard Rate Modeling

A more systematic modeling of CM CDS is possible in the framework of stochastic instantaneous hazard rates. This approach starts with postulating a stochastic differential equation (SDE) for the stochastic default intensity  $\lambda(t)$ . A reasonable choice is a lognormal process (similar to the Black-Karasinski model of interest rates) or an affine process (similar to the Cox-Ingersoll-Ross model of interest rates). A normal process (similar to the Hull–White model of interest rates) was also used despite a conceptual problem posed by positive probabilities of negative hazard rates. Multifactor models for joint stochastic evolution of hazard rates and instantaneous interest rates are also possible.

An exact analytical solution for a CM CDS is not available in any of these models because of a two-layered structure involving inner expectations for CDS rates fixings conditional on the state achieved on the fixing dates. The machinery of trees, lattices, or partial differential equation (PDE) solvers, however, can be accommodated to handle CM CDS structures. The key element is a construction of a slice of values of CM CDS rate fixings on the set of model states achieved on the fixing date. This is done using a representation of the CDS rate in terms of conditional expectations of elementary instruments  $B_t(T)$  and  $H_t(T_1, T_2)$  provided by equations (7), (6), and (8). We refer to Chapter 7 of the book [7] for the details of a possible realization of a tree-based construction.

An advantage of hazard rate modeling is its consistency that allows to price a wide range of credit instruments of different maturities, including CDS options, asset swaps, bond options, and credit linked notes using the same model. A notable disadvantage is the difficulty of calibration.

#### Forward Credit Spread Modeling

As drawbacks of short-rate models of interest rates led to the invention and development of swap and LIBOR market models, similar progression is taking place in the space of structured credit models. We refer to the work [1] and Chapter 23 of [2] for details of a model in which the CDS rates  $S_t(T_i, T_{i+M})$  are chosen as primary variables.

An advantage of this approach is the ease of calibration and ability to derive efficient analytical approximations under minimal additional assumptions. At present, the disadvantage is the paucity of relevant market data, leaving a large freedom in specifying the structure of volatilities and correlations. A full payback from this level of model sophistication cannot be expected until the market for structured products develops enough to provide liquid quotes for CDS option volatilities for a dense set of maturities, similarly to caplet and swaption volatility matrices in the interest rate markets.

# **End Notes**

<sup>a.</sup>The structure can obviously be extended to admit a fixed rate reset floor, which, however, is not included in the standard ISDA template.

<sup>b</sup>. The actual payment dates  $T'_i$  usually have a delay of at least one business day and are rolled forward or backward to fall on a valid business day in accordance with currencydependent conventions. In the practice of quantitative modeling, proper care is taken to make sure that correct discount factors reflecting the actual payment dates are used.

<sup>c</sup>. These expressions are often written in terms of integrals obtained in the limit of an infinitely frequent discretization. The same remark applies to equation  $(3)$ .

<sup>d.</sup>A rigorous calculation of the convexity correction to accrued interest term is technically involved and can be avoided by using a proportionally adjusted correction to the main term.

# References

[1] Brigo, D. (2006). CMCDS valuation with market models, Risk June, 78-83.

- [2] Brigo, D. & Mercurio, F. (2007). Interest Rate Models-Theory and Practice, with Smile, Inflation, and Credit, 2nd Edition, Springer.
- [3] Calamaro, J.-P. & Nassar, T. (2004). CMCDS: The Path to Floating Credit Spread Products, Deutsche Bank, Global Markets Research.
- [4] ISDA (2005). Additional Provisions for Constant Maturity Credit Default Swaps, International Swaps and Derivatives Association, November 21, 2005. Available at www.isda.org.
- [5] Pedersen, C. & Sen, S. (2004). Valuation of Constant Maturity Default Swaps, Lehman Brothers, Quantitative Research Quarterly.
- [6] Renault, O. & Ratul, R. (2007). Constant maturity credit default swaps, in The Structured Credit Handbook, A. Rajan, G. McDermott & R. Ratul, eds, Wiley Finance, pp. 57-77.
- [7] Schönbucher, P. (2003). Credit Derivatives Pricing Models, Wiley Finance.
- [8] Schönbucher, P. (2004). Measure of survival, Risk August, 79–85.

# **Related Articles**

**Constant Maturity Swap; Convexity Adjustments;** Credit Default Swaps; Credit Default Swaption; Forward and Swap Measures; Hazard Rate; Intensity-based Credit Risk Models; Swap Market Models; Term Structure Models.

TIMUR S. MISIRPASHAEV
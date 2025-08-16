# **Credit Default Swap (CDS) Indices**

Credit markets have shown tremendous growth in the last 10 years. In particular, the telecom bubble and corporate scandals of the early 2000s increased the interest of market participants in products such as credit default swaps (CDS) (*see* **Credit Default Swaps**), which provide protection against credit events. In response to this demand for credit protection, credit indices were introduced in 2003, increasing the liquidity of CDS markets. These indices are, in essence, standardized baskets of CDS written on investment-grade and high-yield corporate issuers, or emerging-market governments. Table 1 shows the basic composition criteria of the main indices (more stringent criteria apply too, in particular, those concerning liquidity of the individual CDS). The specific constituents for each index are posted at www.markit.com.

In most indices, issuers are equally weighted. A new series of a given index is issued semiannually, excluding from the basket those issuers who no longer match selection criteria (e.g., downgraded issuers) and adding new ones. In case of a default event, the defaulting issuer is removed from the basket, but the weights remain and the index continues to trade. The reduced basket is referred to as a *new version* of the same series. The loss payment for a default event is determined through the same settlement auction as for single-name CDS (*see* **Credit Default Swaps**).

Credit indices are commonly issued with initial maturities of 3–10 years. Similar to CDS, a credit index is a contract which entails that the protection buyer pays a spread (or coupon) at a regular frequency (usually quarterly according to International Swaps and Derivatives Association (ISDA) dates) in return for default protection on some notional amount. In case of a default of one of the referenced issuers, the protection seller pays the nonrecovered part of the protected notional times the weight of the issuer in the index. The contract does not terminate, but the protected notional is reduced accordingly. Importantly, the index trades with a fixed spread for each series; changes in market pricing are reflected in the upfront payment required to enter the contract. In contrast, in a standard CDS (for all but distressed credits), the spread is set on any given day such that no upfront payment is required.a

A standard market practice is to roll index positions so as to maintain a position in the on-the-run (i.e., most recent) series and version, in order to guarantee maximum liquidity. From an investor's point of view, in addition to enabling credit diversification, credit indices introduce the possibility of leverage without significant liquidity concerns, as several derivatives on these indices exist today (*see* **Collateralized Debt Obligations (CDO)**; **Credit Default Swap Index Options**).

## **Pricing Framework**

Credit indices are routinely priced through the standard CDS model. Indeed, though the index contracts trade with a fixed spread, the convention is to quote a theoretical fair spread (i.e., the coupon that the index would need to pay in theory in order to require no upfront payment) and use the CDS model to convert this fair spread to an upfront payment for the index. The issuers in the basket are assumed to be homogeneous in credit quality and recovery rate. When deriving the common hazard credit curve for the issuers, the convention is to assume a flat curve (*see* **Hazard Rate**). The expected losses are computed from the credit curve, assuming that losses are paid at the end of a coupon period, and given a particular recovery rate. The present value for the index contract is then the difference between the discounted expected losses and the discounted spread payments weighted by the survival probability (since premium is only paid on the remaining protected notional).

The contract can alternatively be valued by using information on the individual constituents, thus relaxing the homogeneity assumption. We can theoretically replicate the index by considering a basket of individual CDS that pay the same spread. We compute the expected losses on the index by aggregating the individual-constituent expected losses, each of which is derived from the full-term structures of credit spreads for the constituent. Similarly, the payment side aggregates survival probabilities over all issuers. It is worth noting that the dependence structure between the issuers does not play a role here as the whole basket is considered.

| Index name          | Number of constituents | Region        | Credit quality                |
|---------------------|------------------------|---------------|-------------------------------|
| CDX.NA.IG           | 125                    | North America | Investment grades             |
| CDX.NA.IG.HVOL      | 30                     | North America | Low-quality investment grades |
| CDX.NA.HY           | 100                    | North America | Noninvestment grades          |
| CDX.NA.HY.B         |                        | North America | B rated                       |
| iTraxx Europe       | 125                    | Europe        | Investment grades             |
| iTraxx Europe HiVol | 30                     | Europe        | Low-quality investment grades |

**Table 1** Main credit indices

### **Imperfect Replication**

Pricing the index through the constituents is appealing, but it is not surprising to observe significant differences with the quoted index prices. The replicating strategy is not perfect, as the mechanics behind credit indices are slightly different from those for CDS. We mentioned earlier that an index trades with a floating upfront and a fixed spread, whereas most CDS trade with a floating spread and no upfront. This implies that we cannot, in general, enter into a basket of CDS contracts that pay the same spread as the index. And while the basket can be composed without initial capital, the index requires a nonzero upfront investment. After a default event, new differences between the credit index and the basket appear. On the index, the reduction in spread payments is independent of the defaulting issuer; the spread is fixed and only the protected notional changes. On the other hand, the spread reduction for the basket is proportional to the spread on the CDS for the specific defaulting issuer. The index and the basket consequently exhibit different behaviors through time, and offer different sensitivities to interest rates.

## **Fair Spread Decomposition**

As contracts in their own right, credit indices are subject to specific demand and supply effects, and have their own distinct risk profile. A simple, standard way of analyzing their risk is to observe the quoted index fair spread. This approach, though, cannot distinguish the risk due to specific issuers from the risk due to demand for the index as a whole.

A useful decomposition is to break the index fair spread into three components: the average fair CDS spread across the constituent issuers, the nonlinear component, and the basis. The first two components constitute the theoretical fair spread of the index, as replicated through a basket of (market-traded) issuer CDS. The nonlinear portion of this fair spread accounts for the heterogeneity in credit quality among the issuers, and increases both with the level of the average fair spread and the dispersion of the individual fair spreads. The nonlinear component is very sensitive to an increase in default likelihood of a single issuer. The basis—defined as the difference between the observed fair spread and the theoretical fair spread—contains a risk premium rewarding the index dealer for the small portion of risk that cannot be perfectly hedged through the replicating basket, and embeds a liquidity premium as well.

### **End Notes**

a*.* Note that changes to the conventional CDS protocol were instituted in early 2009. Among other things, the new protocol stipulates that single-name CDS trade with a fixed coupon of 100 or 500 bp, and settle *via* an upfront payment (*see* **Credit Default Swaps** for further discussion).

### **Further Reading**

Couderc, F. (2006). Measuring risk on credit indices: on the use of the basis, *Risk Metrics Journal* Winter 2007, 61–87. Zhang, H. (2005). Instant default, upfront concession and CDS index basis, *Journal of Credit Risk* **1**(2), 79–89.

### **Related Articles**

#### **Basket Default Swaps**; **Collateralized Debt Obligations (CDO)**; **Credit Default Swap Index Options**; **Credit Default Swaps**.

FABIEN COUDERC & CHRISTOPHER C. FINGER
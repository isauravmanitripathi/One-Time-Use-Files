# **Recovery Swap**

A recovery swap (RS), also called a *recovery lock* or a *recovery default swap* (RDS), is an agreement to exchange a fixed recovery rate *RS* for the realized recovery rate *φ*, the latter being determined under prespecified contractual terms. The fixed recovery rate may be specified in terms of a recovery of par amount (RP), or as the recovery percentage of an equivalent Treasury bond, known as *recovery of Treasury* (RT), or as a fraction of the market value of the bond prior to default, also known as *recovery of market value* (RMV).

A recovery swap is no different than a forward contract at rate *RS* on the underlying recovery rate *φ*. The maturity of the contract is denoted as *T* . If the reference credit underlying the recovery swap does not default before *T* , the swap expires worthless. There are no intermediate or periodic cash flows in a recovery swap. In a liquid market for recovery swaps, the quoted rate *RS* is the best forecast of the expected recovery rate for default at time *T* . This recovery rate may then be used to price credit default swaps (CDSs).

We assume that the buyer of the recovery swap will receive *RS* and pay *φ*. Hence, the buyer gains when the realized recovery rate is lower than that of the strike rate *RS* . The net payoff to the contract is *(RS* − *φ)*. Recovery swaps are quoted in terms of the "strike" rate *RS* . For example, a dealer might quote a recovery swap in GM at 37/40. This means the dealer is prepared to sell a recovery swap with *RS* = 37% and buy at *RS* = 40%.

### **Replication and No-arbitrage**

A recovery swap may be synthesized by selling a fixed recovery CDS (also known as a *digital default swap* or DDS) at a predetermined recovery rate *RD* and buying a standard CDS. When the reference name defaults, the seller of the DDS pays the loss amount on default *(*1 − *RD)* and receives *(*1 − *φ)* on the CDS, thereby generating cash flow *(RD* − *φ)*. There is a triangular arbitrage restriction between the three securities: RS, DDS, and CDS. If we hold 1 unit each of the RS, CDS, and DDS, then we would need that *RS* = *RD*.

In order to state the triangular arbitrage relation more generally, consider the case when *RS* = *RD*, that is, when the strike recovery rates of the recovery swap and DDS are not the same. Let the premium on the CDS be *c*<sup>1</sup> and the premium on the DDS be *c*2. In order to replicate the RS, we will hold *x* units of the CDS and *y* units of the DDS. The replication has two conditions:

1. The cashflows at default must be equal for the RS and the replicating portfolio of CDS and DDS. In other words,

$$x \cdot (1 - \phi) - y \cdot (1 - R_D) = R_S - \phi \qquad (1)$$

2. The premiums of the replicating portfolio must be net zero as the recovery swap does not have any intermediate cash flows. Hence the following equation must hold:

$$y \cdot c_2 - x \cdot c_1 = 0 \tag{2}$$

Set *x* = 1 in equation (1) so as to eliminate dependence on *φ* in the equation. Then we have that

$$x = 1 \quad \text{implies} \quad y = \frac{1 - R_S}{1 - R_D} \tag{3}$$

Substituting this result for *x, y* in equation (2) results in the following:

$$\frac{c_1}{c_2} = \frac{1 - R_S}{1 - R_D} = \frac{\mathcal{L}_S}{\mathcal{L}_D} \tag{4}$$

where L denotes the loss rate. We note the following:

- The no-arbitrage condition in equation (4) between the three securities implies that the ratio of the premium on the CDS to the premium on the DDS is equal to the ratio of loss rates on the recovery swap and the digital CDS. This is because the quote on the recovery swap *RS* is the expected recovery rate on the CDS contract.
- It follows immediately that if *RD* is specified, then equation (4) mandates a precise relation between the quotations on the three types of contracts, that is, rate *RS* for the recovery swap, premium *c*<sup>1</sup> on the CDS, and premium *c*<sup>2</sup> on the DDS. Given the quotes on any two of these securities, the quote on the third security is immediately obtained.

• These no-arbitrage based results do not depend in any way on the underlying process for default or that of recovery. This makes the relationships in equation (4) very general and easy to apply in practice, as well as easy to assess empirically for academic purposes.

### **Applications and Uses of Recovery Swaps**

Recovery swaps were first developed by BNP Paribas in early 2004 [10]. In response to market demand, banks started issuing fixed-rate recovery collateralized debt obligations (CDOs) and as a consequence were bearing recovery rate risk. In order to hedge against this recovery rate risk, market participants started selling recovery swaps.

Recovery swap markets are predominantly traded on reference entities with a high risk of default or of declining credit quality. For this reason, the largest activity in the recovery swaps market is in the auto parts and auto manufacturing sectors and geographically on North American entities [7]. Trading volumes in recovery swaps, although still small relative to the overall credit derivatives market, increased in 2005 with the defaults of Delphi Corporation and the Collins & Aikman Corporation [7]. Still, the market remains largely undeveloped and the International Swaps and Derivatives Association (ISDA), in May 2006, issued a template for the documentation on recovery swaps but the full documentation remains to be completed at this time [13].

There are two primary uses of recovery swaps. The first is to isolate the probability of default from the recovery rate. Traders may have in-house expertise in determining default probabilities but not in determining recovery and thus may wish to hedge their recovery risks through recovery swaps. The second use of recovery swaps is to eliminate recovery basis risk. Recovery basis risk occurs because of different settlement procedures between CDSs and CDOs. CDSs are often settled physically, meaning that when default occurs the seller of protection receives the defaulted bonds, whereas CDOs are almost always cash settled. The difference in settlement procedures is the source of recovery basis risk. For instance, an investor might hold a CDS Index that includes a given reference entity and have an offsetting position by selling the single-name CDS of the same entity. The investor is hedged

against the default risk of this entity, but because of differences in settlement at default between the CDS Index and the single-name CDS, the investor might get different recovery rates on the two instruments (recovery basis risk). Hence, recovery swaps can hedge against recovery basis risk by locking-in recovery rates.

Furthermore, in the case where the CDSs specify a physical settlement, it is possible that the underlying bonds might be scarce compared to the notional amount of CDS traded on the bond. This causes a "delivery squeeze" where the price, and therefore the recovery of the bond, is artificially increased because the buyers of CDS need to buy the bonds for delivery to their counterparty. For instance, in October 2005, Delphi Corporation had \$27.1 billion of outstanding CDSs against notional outstanding bonds of just \$2 billion causing the price of the defaulted bonds to surge by as much as 24% [9]. The consequence of this delivery squeeze is to reduce the profits accruing to buyers of CDSs, and recovery swaps provide a hedge against this by locking in the recovery rate ahead of time. More recently though, most CDSs are being settled in cash, thereby circumventing this problem.

### **Recovery Risk**

There is a growing literature on recovery risk. Berd [3] provides a nice introduction and analysis of recovery swaps. DDSs are analyzed in [4]. Altman *et al.* [2] present a detailed study showing how recovery rates depend on default rates, positing and finding an inverse relationship. Chan-Lau [6] presents a method to obtain the upper bound on recovery on emerging market debt. Das and Hanouna [8] develop a methodology for identifying implied recovery rates and default probabilities from CDS spreads and data on stock prices and volatilities. Acharya *et al.* [1] provide empirical evidence that recovery rates depend on the industry, state of the economy, and specificity of assets to the industry in which the firm operates. Carey and Gordy [5, 14] show that recovery has systematic risk. Guo *et al.* [11] look at recoveries in reduced form models by explicitly modeling the postbankruptcy process of recoveries. The well-known loss given default model of Gupton and Stein [12] is well liked and used. Absolute priority rule (APR) violations are modeled in [15]. For a nice overview, see [16].

## **References**

- [1] Acharya, V., Bharath, S. & Srinivasan, A. (2007). Does industry-wide distress affect defaulted firms? – Evidence from creditor recoveries, *Journal of Financial Economics* **85**(3), 787–821.
- [2] Altman, E., Brady, B., Resti, A. & Sironi, A. (2005). The link between default and recovery rates: theory, empirical evidence and implications, *Journal of Business* **78**, 2203–2228.
- [3] Berd, A. (2005). Recovery swaps, *Journal of Credit Risk* **1**(3), 1–10.
- [4] Berd, A. & Kapoor, V. (2002). Digital premium, *Journal of Derivatives* **10**(3), 66.
- [5] Carey, M. & Gordy, M. (2004). *Measuring Systematic Risk in Recovery on Defaulted Debt I: Firm-Level Ultimate LGDs*. Working paper, Federal Reserve Board.
- [6] Chan-Lau, J.A. (2003). *Anticipating Credit Events using Credit Default Swaps, with an Application to Sovereign Debt Crisis*. IMF working paper.
- [7] Creditflux Ltd (2006). *Jump-to-default Hedging Spurs Recovery-swap Surge*. January 1, 2006.
- [8] Das, S. & Hanouna, P. (2007). *Implied Recovery*. Working paper, Santa Clara University.
- [9] Euromoney Magazine (2006). *Why CDS Investors need to Lock in Recovery Rates Now*. May 1, 2006.

- [10] Financial Times (2004). *Capital Markets & Commodities: Investors Welcome Recovery Swap Tool*. June 18, 2004.
- [11] Guo, X., Jarrow, R. & Zeng, Y. (2005). *Modeling the Recovery Rate in a Reduced Form Model*. Working paper, Cornell University.
- [12] Gupton, G. & Stein, R. (2005). *LossCalcv2:Dynamic Prediction of LGD*. Working paper, Moodys.
- [13] Investment Dealers' Digest (2006). *New ISDA Documentation Boosts Recovery Swaps*. May 22, 2006.
- [14] Levy, A. & Hu, Z. (2006). *Incorporating Systematic Risk in Recovery: Theory and Evidence*. Working paper, Moodys KMV.
- [15] Madan, D., Guntay, L. & Unal, H. (2003). Pricing the risk of recovery in default with APR violation, *Journal of Banking and Finance* **27**(6), 1001–1218.
- [16] Schuermann, T. (2004). *What do we know about Loss Given Default?* 2nd Edition, Working paper, Federal Reserve Bank of New York, forthcoming in *Credit Risk Models and Management*.

### **Related Articles**

**Credit Default Swaps**; **Exposure to Default and Loss Given Default**; **Recovery Rate**.

SANJIV R. DAS & PAUL HANOUNA
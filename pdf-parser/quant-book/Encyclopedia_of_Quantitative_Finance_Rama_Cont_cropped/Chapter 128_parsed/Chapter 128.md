# **Equity Default Swaps**

Equity default swaps (EDS) are equity derivatives that are structured as far out-of-the-money Americanstyle binary puts with periodic swap payments rather than an up-front premium. The structure of EDS is similar to **credit default swaps** (CDS) except that the default event is defined in terms of a decline in the share price of the reference entity rather than a credit event experienced by the reference entity. Thus, similar to a CDS, an EDS can be seen in terms of the protection buyer and protection seller counterparties. In the case of an EDS, protection buyers are hedging themselves against a large decline in the share price.

More specifically, the protection buyer in an EDS makes periodic fixed payments to the protection seller. The size of the periodic payments is called the *EDS spread*. In return for the periodic payments, a default payment from the protection seller to the protection buyer is made if the share price of the reference entity declines a prespecified amount from the share price at initiation of the EDS contract. If this equity default event occurs and the default payment is made, then the contract terminates with the protection buyer ceasing to make further payments. If the equity default event never occurs before the maturity of the EDS contract, then no payment is ever made from the protection seller to the protection buyer.

Typically, the prespecified fall in the share price is a 70% decline, so that the equity default event is defined as the first time that the shares of the reference entity trade at 30% of the share price when the EDS contract is entered. The amount of the default payment is fixed when the EDS contract is initiated and computed as

$$N \times (1 - R) \tag{1}$$

where *N* is the notional value of the contract and *R* is the recovery rate, which is predetermined and typically set to be 50%. The formulation of the default payment in terms of a recovery rate is to further the analogy to CDS. EDS are usually medium-term contracts with maturities of five years being the most common.

The first EDS were issued in 2004 as a means to allow protection sellers to receive a higher return than from CDS. A credit event almost certainly implies that an equity default event will occur, but, conversely, an equity default event can occur without a credit event having occurred. This implies that for the same reference entity, the EDS spread must be greater than the CDS spread. Besides, since protection sellers receiving a higher return for EDS, the default event for EDS is easier to define than for CDS. Whether or not the share price has reached a predetermined level is unambiguous, but the various credit events can sometimes cause confusion for counterparties and have led to legal proceedings.

One difference between EDS and most equity derivatives is the swap feature. Not only is there no up-front premium but also upon an equity default event, no further swap payments are made. Gil-Bazo [4] finds the fraction of the EDS spread that is due to this swap feature under the Black–Scholes model, given plausible parameter values.

## **Applications of EDS**

Besides the obvious application of EDS as portfolio protection on long positions in shares, EDS are often used in ways that exploit their similarity to CDS. Two examples are given here: relative value trades in EDS–CDS carry trades and as yield-enhancing replacements for CDS in **collateralized debt obligations** (CDO).

In EDS–CDS carry trades, an investor sells protection with an EDS and buys protection with a CDS. The larger EDS spread is received while the smaller CDS is paid, so that the investor simply collects the positive carry if neither a credit nor an equity default event occurs. In the case that both default events occur, the investor is partially hedged with the effectiveness of the hedge depending on the relative timing of the default events as well as the recovery rate on the credit event. There is a risk of large losses if an equity default occurs without a credit event occurring.

Some CDO were constructed with the reference portfolio including some EDS in addition to CDS. While this increases the risk to the CDO investors, there can be significant yield enhancement. There have even been CDO where the reference portfolio was exclusively composed of EDS. These are termed *equity collateralized obligations (ECO)*.

### **EDS as Credit–Equity Hybrids**

Since a large fall in the equity price is needed to trigger the payout of an EDS, there are often accompanying credit implications to the firm leading many to refer to EDS as a *credit–equity hybrid instrument*, despite the default event being defined exclusively in terms of the share price.

There is empirical evidence that EDS should not be considered simply as an equity derivative. de Servigny and Jobst [8] assess the relative weighting of debt and equity factors for equity default probabilities. They find that for the typical definition of equity default as 30% of the initial share price, debt factors are more important than equity factors. In addition, Jobst and de Servigny [5] study EDS correlation and EDS–CDS correlation and find that multivariate analyses commonly used for credit are the most appropriate.

### **EDS Pricing**

Consider the problem of finding the fair spread for an EDS that is to be initiated now at time *t* = 0, with the current stock price as *S*0. The default payment in an EDS is made the first time that the share price trades at the prespecified level *L* where *L<S*0. In addition to this, the swap payments are made contingent on the share price not being traded at or below the prespecified level. Thus, to price an EDS, the probability distribution of the first passage time of the level *L* is required. Here, the first passage time of *L* is defined as

$$\tau_L = \inf\{t > 0; S_t \le L\} \tag{2}$$

Then, if an EDS with \$1 notional requires a periodic payment of *C* at times *T*1*,...,Tn* the price of the EDS for a protection buyer is

$$EDS(S_{0};C,R,L) = -C\sum_{i=1}^{n} D^{T_{i}}P(\tau_{L} > T_{i}|S_{0})$$
$$+ (1-R)E[D^{\tau_{L}}1_{\{\tau_{L} \leq T_{n}\}}|S_{0}]$$
(3)

where *R* is the recovery rate, *D<sup>t</sup>* is the discount factor to time *t* and *P* and *E* are probabilities and expectations under the risk-neutral measure. Then, the fair spread for an EDS is the value of *C* that makes *EDS (S*0;*C, R, L)* = 0.

The problem of deriving the first passage time distribution has been solved in several special cases. Albanese and Chen [1] compute the EDS spread under the assumption that the stock price follows a constant elasticity of variance (CEV) process (*see* **Constant Elasticity of Variance (CEV) Diffusion Model**) and Asmussen *et al.* [2] use the Wiener–Hopf factorization (*see* **Wiener–Hopf Decomposition**) to compute the EDS spread under the assumption that the stock price follows a Carr–Geman–Madan–Yorr (CGMY) Levy process ´ (*see* **Tempered Stable Process**). For models where credit considerations are more explicitly addressed, EDS spreads have been priced using different methods: Albanese and Chen [1] use a credit barrier model with a credit to equity mapping; Campi *et al.* [3] extend the CEV case to include jump to default; Medova and Smith [6] use a structural model of credit risk (*see* **Structural Default Risk Models**) where the firm's asset value follows a geometric Brownian motion; and Sepp [7] makes use of an extended structural model where the firm's asset value can have stochastic volatility (*see* **Heston Model**) or be a double exponential jump diffusion, with the default barrier being deterministic or stochastic.

## **References**

- [1] Albanese, C. & Chen, O. (2005). Pricing equity default swaps, *Risk* **18**, 83–87.
- [2] Asmussen, S., Madan, D. & Pistorius, M.R. (2008). Pricing equity default swaps under an approximation to the CGMY Levy Model, ´ *Journal of Computational Finance* **11**, 79–93.
- [3] Campi, L., Polbennikov, S. & Sbuelz, A. (2009). Systematic equity-based credit risk: a CEV model with jump to default, *Journal of Economic Dynamics and Control* **33**, 93–108.
- [4] Gil-Bazo, J. (2006). The value of the 'swap' feature in equity default swaps, *Quantitative Finance* **6**, 67–74.
- [5] Jobst, N. & de Servigny, A. (2006). An empirical analysis of equity default swaps (II): multivariate insights, *Risk* **19**, 97–103.

- [6] Medova, E. & Smith, R. (2006). A structural approach to EDS pricing, *Risk* **19**, 84–88.
- [7] Sepp, A. (2006). Extended CreditGrades Model with stochastic volatility and jumps, *Wilmott Magazine* September, 50–62.
- [8] de Servigny, A. & Jobst, N. (2005). An empirical analysis of equity default swaps (I): univariate insights, *Risk* **18**, 84–89.

**Related Articles**

**Constant Proportion Portfolio Insurance**; **Credit Default Swaps**; **Total Return Swap**; **Variance Swap**.

OLIVER CHEN
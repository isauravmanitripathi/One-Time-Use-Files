# **Swaps**

A *swap* is an over-the-counter (OTC) derivative where two parties exchange regular interest rate payments over the life of the contract based on a principal. The most liquid market for swaps is for maturities between 2 and 10 years. However, in some markets, 30- or 40-year swaps are traded as well, and there exist even longer term deals. Swap legs may be denominated in single currency, as in *interest rate swaps* (IRS), or in different currencies, as in *currency swaps*. We cover the most common contracts of both types that use LIBOR (*see* **LIBOR Rate**) to fix the interest payments. An extensive discussion of how swaps are priced and risk-managed can be found in [2].

# **Plain Vanilla Swaps**

The simplest IRS product is the *fixed/float swap* (sometimes also called *plain vanilla swap*). It is a contract where the payer pays a fixed rate and the receiver pays a floating rate fixed periodically against some rate index, for example, LIBOR; see Figure 1. The plain vanilla swap contract does not involve the principal exchange; only the interest is paid by the parties.

The purpose of such a transaction is to hedge against variations in the interest rates. In such capacity, vanilla swaps are used as basic hedges for all interest-rate-linked products (*see* **Hedging of Interest Rate Derivatives**). Another common use of vanilla swaps is to translate the fixed rate liabilities into floating rate ones on the back of bond issuance (*see* **Bond**). Since both forward rate agreement (FRA) and vanilla swap markets are fairly liquid, both of those instruments are used for yield curve construction (*see* **Yield Curve Construction**).

Most of the swap contracts are agreed on the terms of International Swaps and Derivatives Association

![](_page_0_Figure_6.jpeg)

**Figure 1** Fixed/float swap. The payer pays a fixed rate and receives a floating rate

(ISDA). For information about ISDA, conventions that specify swap agreements, see [1]. A swap can be viewed as a set of contiguous FRAs. Unlike in the FRAs, however, the frequencies of payments on the floating and the fixed legs of the swap may not be the same. Another difference is that each leg of a swap is normally making payments at the end of each accrual period. The latter fact allows to treat vanilla swaps as "linear" instruments. There exist other types of swaps for which the linear property does not hold (*see* **Constant Maturity Swap**).

Each payment amount in a plain vanilla swap equals the corresponding interest rate multiplied by the time fraction of the accrual period and by the notional amount. Such simple payout allows us to write down the present value (PV) formula of the plain vanilla swap for one unit of notional as

$$\begin{split} \text{PV}(0) &= \sum_{k=1}^{N} L(0, t_{k-1}, t_k) \cdot \tau_k \cdot P(0, t_k) \\ &- R_0 \sum_{j=1}^{M} \tau_j \cdot P(0, t_j) \end{split} \tag{1}$$

where the first sum runs over the floating leg payments, the second sum runs over the fixed leg payments, *τk* is the time fraction of accrual period *(tk*<sup>−</sup>1*, tk)*, *R*<sup>0</sup> is the swap's fixed rate, *P (T , S)* is the value of discount bond at *T* , and *L(t, T , S)* is the forward reference rate at *t*.

The valuation formula in equation (1) demonstrates that a plain vanilla swap, effectively being a linear combination of FRAs, can be valued off a forward curve and a discount function. At the inception of the swap transaction, the fixed rate is chosen such that *P V* is equal to zero. Such a rate is called *break-even swap rate*.

In addition to the plain vanilla swaps there exist other types of swaps based on LIBOR rates, for example, basis swaps and cross-currency basis swaps.

# **Basis Swaps**

In a *basis swap* the parties exchange floating payments fixed against different rate indices. Very often both legs are LIBOR-based. For example, one leg pays 3M LIBOR plus quoted spread, and the other leg pays 6M LIBOR. The economic rationale behind the existence of the basis spread between different LIBOR rates in single currency can be explained by the credit and the liquidity considerations. A bank would rather provide an unsecured credit for 3 months, then assess the market situation, and provide credit for another 3 months rather than lend money for 6 months from the very beginning.

# **Cross-currency Basis Swaps**

These contracts are designed to provide funding in one currency through borrowing of funds in another currency. In a *cross-currency basis swap*, the two legs of the swap are each denominated in a different currency. Usually, one floating leg is USD floating rate. In this type of a swap contract, the parties exchange both the principals and the interest payments in the two currencies, based on the foreign exchange rate at the time of the trade. The interest payments are normally fixed against the corresponding currencies' 3M LIBOR rates. The principal exchange, typically occurring at both the start and the end of the contract, is an important aspect of this transaction. Without the principal exchange, the associated swap would not achieve the goal of transforming liability from one currency into another.

# **References**

- [1] Available at: http://www.isda.org (2008).
- [2] Miron, P. & Swannell, P. (1992). *Pricing and Hedging Swaps*, Euromoney Institutional Investor PLC.

# **Further Reading**

Available at: http://www.bba.org.uk (2008).

- Henrard, M. (2007). The irony in the derivatives discounting, *Wilmott Magazine* July, 92–98.
- Traven, S. (2008). *Pricing Linear Derivatives with a Single Discount Curve*. working paper, unpublished.

# **Related Articles**

**Constant Maturity Swap**; **Forward and Swap Measures**; **LIBOR Rate**; **Swap Market Models**; **Trigger Swaps**; **Yield Curve Construction**.

SERGEI TRAVEN
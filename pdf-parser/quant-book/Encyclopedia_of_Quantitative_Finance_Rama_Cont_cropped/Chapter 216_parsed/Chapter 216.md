# **LIBOR Rate**

*LIBOR* stands for London Interbank Offered Rate. It provides a measure of banks' borrowing costs and represents one of the most widely referenced interest rates in the world. LIBOR is owned by the British Bankers' Association (BBA); see [1] for information about BBA and its publications. The *LIBOR rate* is a rate at which contributing banks believe they could raise unsecured funds for a short term. LIBOR panel banks are those with the best credit ratings, and this benchmark describes availability of funds to banks with similar creditworthiness. LIBOR is used as the basis for settlement of interest rate contracts, both those that are traded on the exchanges worldwide (interest rate futures, *see* **Eurodollar Futures and Options**, and futures options), and the over-thecounter (OTC) transactions. LIBOR supports a swap market estimated at over \$300 trillion and a loan market estimated at over \$10 trillion. All LIBOR rates are the benchmarks set in the London market.

LIBOR is set for 10 different currencies at 11 am London time. The LIBOR rates therefore reflect the relative availability of the corresponding currencies' funds in European markets.

The actual calculation of the LIBOR rates is done by Reuters for the BBA, and the process is overseen by several committees. Sixteen contributor banks are selected for each of the four major currencies: US dollar (USD), sterling (GBP), euro (EUR), and yen (JPY). Between 8 and 12 contributor banks are selected for the other six currencies which are Australian dollar (AUD), Canadian dollar (CAD), Swiss franc (CHF), Danish krone (DKK), New Zealand dollar (NZD), and Swedish krona (SEK).

The process starts with polling the contributor banks. The rate submitted must be formed from the bank's perception of its cost of funds in the interbank market. Hence the quotes are obtained from the money market trading desks (who manage the banks' cash positions), and not from interest rate derivative traders. After the quotes are collected, the 25 percentile of the highest and the 25 percentile of the lowest quotes are discarded. This makes it virtually impossible for a contributor to skew the result. The remaining two quartiles of the quotes are averaged producing the number, which is then published as *LIBOR fixing*.

LIBOR rates are fixed each London business day for a set of short-term maturities up to 12 months. A fixed LIBOR rate refers to a certain interest rate period, starting at the so-called value date and ending at the maturity date (Figure 1). There is an offset between the fixing date and the value date for all currencies except sterling. More details about the rules and conventions governing LIBOR fixing can be obtained from the BBA documentation [1].

## **Forward Rate Agreements (FRAs)**

A forward rate agreement (FRA) is a contract between two parties to fix a future interest rate based on a principal. It is an OTC product and represents an interest rate derivative in which one party (the buyer) pays a fixed interest rate and receives a floating interest rate, which is equal to some underlying rate called the *reference rate*. The most commonly used underlying rate is LIBOR.

FRAs are available for a variety of periods: starting from a few days to terms of several years. However, most of the liquidity in the FRA market is concentrated within 1 year, and those products are regarded as money-market instruments. FRAs are typically agreed on BBA-terms.

FRA's term period is normally specified by a pair of numbers separated by dash, forward slash, or very often by a cross: 0–3, 3/9, 3 × 6, and so on. The first number refers to the starting month and the second number denotes the ending month of the FRA term, counting from the current month. If no day of the month is given, the spot start is assumed; otherwise, the FRA term starts on a given day of the starting month. Figure 2 shows all dates that specify the FRA contract:

**Trade date** The date on which the contract is traded.

**Value date spot** Derived in the same way as the value date of the reference rate fixing.

![](_page_0_Figure_12.jpeg)

**Figure 1** LIBOR rate dates

![](_page_1_Figure_1.jpeg)

Figure 2 FRA dates

**Settlement date** The date on which the contract term commences. This is also the date when the amount due is paid by one party to the other.

**Fixing date** The date on which the reference rate is observed. For a LIBOR FRA, the relationship between the fixing date and the settlement date is the same as that between the fixing date and the value date shown in Figure 1.

**Maturity date** The end date of the FRA term.

The amount due is determined on the fixing date as a difference between interest rate payments for the buyer and the seller. The payment amount is

$$\frac{(L - R_0) \cdot \tau \cdot (\pm N)}{1 + L \cdot \tau} \tag{1}$$

where  $L$  is the reference rate fixing;  $R_0$  is the FRA rate; N is the principal amount ( $\pm = \text{buy}/\text{sell}$ ); and  $\tau$  is the time fraction of the FRA term.

The FRA settlement amount represents the difference in the values of deposits accrued to the maturity date; however, as the payment is exchanged on the settlement date, the appropriate discounting factor is applied, that is,  $1 + L \cdot \tau$  in the denominator of (1).

The pricing of an FRA is reduced to forecasting the fixing of the reference rate. The present value of the FRA contract can be written as the expected value-under the pricing measure-of the payoff given by equation (1), assuming that the fixing occurs at  $T$ and  $S$  is the maturity (per one unit of principal):

$$\text{PV}(0) = E\left\{\frac{P(T,S) \cdot [L(T,T,S) - R_0] \cdot \tau}{B(T)}\right\} \tag{2}$$

where  $P(T, S)$  is the value of discount bond at T;  $B(T)$  is the value of a money market account; and  $L(t, T, S)$  is the forward reference rate at t.

We observe that since  $P(T, S) \cdot L(T, T, S) \cdot \tau \equiv$  $1 - P(T, S)$ , the expression inside the expectation in equation (2) is a linear combination of traded assets of which discounted prices are martingales. Thus the FRA's values today can be expressed in terms of the forward rates:

$$PV(0) = P(0, T) - P(0, S) - R_0 \cdot P(0, S) \cdot \tau$$
  
=  $P(0, S) \cdot [L(0, T, S) - R_0] \cdot \tau$  (3)

In modeling literature, as in the derivation above, it is common to assume that discounting is done at rates consistent with forward LIBOR rates. In reality, however, discounting should reflect the true cost of financing of the corresponding derivative contract for a given bank. Such financing rate usually differs, and sometimes significantly, from the prevailing LIBOR forward rates. See [2, 3] for further details of derivative pricing using separate forward and discount curves.

### References

- $[1]$ Available at: http://www.bba.org.uk (2008).
- Henrard, M. (2007). The irony in the derivatives discount-[2] ing, Wilmott Magazine July, 92-98.
- [3] Traven, S. (2008). Pricing Linear Derivatives with a Single Discount Curve. working paper, unpublished.

#### **Further Reading**

Available at: http://www.isda.org (2008).

### **Related Articles**

**Bermudan Swaptions and Callable Libor Exotics;** Bond; Caps and Floors; LIBOR Market Model.

SERGEI TRAVEN
# **Caps and Floors**

#### **Definitions and Notation**

Let us consider a set of times  $0 =: T_0, T_1, \ldots, T_M$ and denote by  $P(t, T)$  the discount factor at time t for the generic maturity  $T$ .

A *cap* is a contract that pays at each time  $T_i$ ,  $i =$  $a, \ldots, b, a \ge 1$ , the difference, if positive, between the LIBOR rate set at the previous time  $T_{i-1}$  and a given rate  $K$  specified by the contract, which is shortly referred to as a strike. In formulas, assuming unit notional, the time- $T_i$  payoff is

$$\tau_i \max\{L(T_{i-1}, T_i) - K, 0\} = \tau_i [L(T_{i-1}, T_i) - K]^+$$
(1)

where  $\tau_i$  denotes the year fraction for the interval  $(T_{i-1}, T_i]$  and the LIBOR rate  $L(T_{i-1}, T_i)$  is the simply compounded rate at time  $T_{i-1}$  for maturity  $T_i$ , namely,

$$L(T_{i-1}, T_i) := \frac{1}{\tau_i} \left[ \frac{1}{P(T_{i-1}, T_i)} - 1 \right] \qquad (2)$$

(see also LIBOR Rate).

Each single option in a cap is called a *caplet*. A cap is then a strip of caplets.

Analogously, a *floor* is a contract that pays at each time  $T_i$ ,  $i = a, \ldots, b, a \ge 1$ , the difference, if positive, between a strike  $K$  and the LIBOR rate set at time  $T_{i-1}$ :

$$\tau_i \max\{K - L(T_{i-1}, T_i), 0\} = \tau_i [K - L(T_{i-1}, T_i)]^+$$
(3)

Each single option in a floor is called a *floorlet*. A floor is then a strip of floorlets.

A cap (floor) is said to be at-the-money (ATM) if its price is equal to that of the corresponding floor (cap). It is said to be in-the-money (ITM) or out-ofthe-money (OTM) if its price is, respectively, higher or lower than that of the corresponding floor (cap).

As a consequence of the put-call parity, which, on each  $T_i$ , reads as

$$\tau_i \max\{L(T_{i-1},T_i)-K,0\}$$

$$- \tau_i \max\{K - L(T_{i-1}, T_i), 0\}$$
  
=  $\tau_i [L(T_{i-1}, T_i) - K]$  (4)

(see also **Put-Call Parity**), the difference between a cap and a floor with the same payment times  $T_i$ ,  $i = a, \ldots, b$ ,  $a \ge 1$ , and strike K is an interest rate swap (IRS) where, at each time  $T_i$ , the floating rate  $L(T_{i-1}, T_i)$  is exchanged for the fixed rate K. Therefore, a cap (floor) is ATM if and only if the related IRS has zero value, that is, if and only if its strike equals the underlying (forward) swap rate:

$$K = K_{\text{ATM}} := \frac{P(0, T_{a-1}) - P(0, T_b)}{\sum_{i=a}^{b} \tau_i P(0, T_i)} \qquad (5)$$

Moreover, the cap is ITM if  $K < K_{\text{ATM}}$  and OTM if  $K > K_{\text{ATM}}$ . The converse holds for a floor.

#### **Pricing Formulas**

It is market practice to price caps and floors with sums of corresponding Black's formulas (see **Black–Scholes Formula**). Precisely, if the cap (floor) pays on dates  $T_i$ ,  $i = a, \ldots, b, a \ge 1$ , and has a strike  $K$ , its market formula is given by

$$\begin{aligned} \text{Cap}(K, T_a, T_b; \sigma_b) &= \sum_{i=a}^{b} P(0, T_i) \tau_i \\ &\times \text{Bl}(K, L(0, T_{i-1}, T_i), \ \sigma_b \sqrt{T_{i-1}}, 1) \\ \text{Floor}(K, T_a, T_b; \sigma_b) &= \sum_{i=a}^{b} P(0, T_i) \tau_i \\ &\times \text{Bl}(K, L(0, T_{i-1}, T_i), \ \sigma_b \sqrt{T_{i-1}}, -1) \quad (6) \end{aligned}$$

where

$$\begin{split} \text{Bl}(K,L,v,\omega) := &L\omega\Phi\bigg(\omega\frac{\ln(L/K) + \frac{1}{2}v^2}{v}\bigg) \\ &- K\omega\Phi\bigg(\omega\frac{\ln(L/K) - \frac{1}{2}v^2}{v}\bigg) \end{split}$$

 $\Phi$  denotes the standard Gaussian cumulative distribution function, and  $L(0, T_{i-1}, T_i)$  is the simply compounded forward LIBOR rate at time 0 for the interval [*Ti*<sup>−</sup>1*, Ti*]:

$$L(t;T_{i-1},T_i) := \frac{1}{\tau_i} \left[ \frac{P(t,T_{i-1})}{P(t,T_i)} - 1 \right], \quad t \le T_{i-1}$$
(7)

The parameter *σb* is called the *cap- (floor-) implied volatility*. It is a single volatility parameter that must be inputted in each Black's formula in equation (6) to reproduce the market price.

A cap and a floor with the same maturity and strike must be priced with the same implied volatility, as a consequence of the put–call parity (4).

# **Justification for the Market Formulas**

Practitioners used the market formulas (6) for years without a formal proof that they were indeed arbitrage free. Such a proof was first given by Jamshidian [3], followed by Miltersen *et al.* [4] and Brace *et al.* [1] with their celebrated lognormal LIBOR market models (*see also* **LIBOR Market Model**).

Let us consider a *Ti*-maturity caplet with strike *K*. The floorlet case is analogous. By classic riskneutral valuation (*see also* **Risk-neutral Pricing**), the no-arbitrage price of the caplet payoff (1) at time 0 is

$$E\left\{e^{-\int_{0}^{T_{i}}r(t)dt}\tau_{i}[L(T_{i-1},T_{i})-K]^{+}\right\}$$
$$=E\left\{e^{-\int_{0}^{T_{i}}r(t)dt}\tau_{i}[L(T_{i-1};T_{i-1},T_{i})-K]^{+}\right\}$$
(8)

where *E* denotes the risk-neutral expectation and *r(t)* the instantaneous short rate at time *t*. Switching to the *Ti*-forward measure *QTi* , whose associated numeraire is the zero-coupon bond *P (t, Ti)* (*see also* **Forward and Swap Measures**), the caplet price becomes

$$E\left\{e^{-\int_{0}^{T_{i}}r(t)dt}\tau_{i}[L(T_{i-1};T_{i-1},T_{i})-K]^{+}\right\}$$
  
=  $P(0,T_{i})\tau_{i}E^{T_{i}}\left\{[L(T_{i-1};T_{i-1},T_{i})-K]^{+}\right\}$  (9)

where *ETi* denotes expectation under *QTi* . The Black formula for the caplet in question can then be obtained by assuming that under such a measure:

$$dL(t;T_{i-1},T_i) = \varsigma_i L(t;T_{i-1},T_i) dW_i(t) \qquad (10)$$

where *ςi* is the (constant and deterministic) caplet volatility and *Wi* is a standard Brownian motion under *QTi* . Assuming a driftless dynamics for the forward rate *L(t*; *Ti*<sup>−</sup>1*, Ti)* under *QTi* is the only admissible choice since, by its own definition (7), the forward rate is a martingale under the *Ti*forward measure (tradable asset divided by the numeraire).

A more detailed descriptions of these arguments can be found in **LIBOR Market Model**.

# **Market Quotes and Smiles**

Given the pricing formulas (6), it is also a market practice to quote caps and floors through their implied volatility *σb*. Such a volatility is typically a function of the strike price, too: *σb* = *σb(K)*, meaning that caps (floors) with the same maturities but different strikes can be priced with different implied volatilities. This is called *smile effect*, due to the typical shape of the market implied volatility curves and surfaces.

The market quotes cap-/floor-implied volatilities for a number of maturities (up to 30 years for the main currencies). An example of cap implied volatility surface from the USD market is shown in Figure 1, where payment times are three-month spaced.

Let us denote by *Tjk* , *k* = 1*,...,N*, the *N* cap maturities in a given market, and assume that *jN* = *M*. From the corresponding cap quotes, one can strip the implied caplet volatilities *ςi*, for a given strike *K*, by recursively solving, for *k* = 1*,...,N*,

$$\begin{split} \text{Cap}(K, T_a, T_{jk}; \sigma_{jk}) \\ &= \sum_{i=a}^{jk} P(0, T_i) \tau_i \text{Cpl}(K, T_{i-1}, T_i; \varsigma_i) \\ &= \sum_{i=a}^{jk} P(0, T_i) \tau_i \text{Bl}(K, L(0, T_{i-1}, T_i), \varsigma_i \sqrt{T_{i-1}}, 1) \end{split} \tag{11}$$

![](_page_2_Figure_1.jpeg)

**Figure 1** USD cap volatilities as of February 13, 2009. Strikes are in percentage points

Unfortunately, the number *N* of traded (cap) maturities is typically (much) smaller than the number of underlying (caplet) payments times. Therefore, stripping the caplet volatilities is neither trivial nor uniquely defined. A common approach is based on assuming, for each given strike, specific interpolations along the maturity dimension. The simplest choice is to assume that the *ςi* are constant on the intervals defined by the cap maturities, namely, *ςi* = *ςh* when *Tjk*<sup>−</sup><sup>1</sup> *< Ti, Th* ≤ *Tjk* . This allows the recursive stripping of caplet volatilities from equation (11) by solving sequences of equations, each with a unique unknown.

The caplet-implied volatilities stripped from the caps of Figure 1 by assuming piece-wise constant interpolation along the maturity dimension are shown in Figure 2 for a limited range of maturities.

# **Beyond Black's Formula**

The lognormal dynamics (10) imply that caplets with the same maturity *Ti* but different strikes are priced with the same implied volatility *ςi*. However, as just seen, the implied volatilities quoted by the market change depending on the strike (smile effect). A popular alternative to equation (10), allowing for implied volatility smiles, is the stochastic alpha beta rho (SABR) model of Hagan *et al.* [2], where each forward LIBOR rate *L(t*; *Ti*<sup>−</sup>1*, Ti)* is assumed to

![](_page_2_Figure_7.jpeg)

**Figure 2** USD caplet volatilities as of February 13, 2009. Strikes are in percentage points

evolve under the corresponding forward measure *QTi* according to

$$dL(t; T_{i-1}, T_i) = V_i(t)L(t; T_{i-1}, T_i)^{\beta_i} dZ_i(t)$$
  
$$dV_i(t) = \epsilon_i V_i(t) dW_i(t)$$
  
$$V_i(0) = \alpha_i$$
 (12)

where *Zi* and *Wi* are *QTi*-standard Brownian motions with d*Zi(t)* d*Wi(t)* = *ρi* d*t* and where *βi* ∈ *(*0*,* 1], *i* and *αi* are positive constants, and *ρi* ∈ [−1*,* 1].

Cap prices in the SABR model are given by the following closed form approximation:

$$\text{Cap}^{\text{SABR}}(K, T_a, T_b)$$
  
=  $\sum_{i=a}^{b} P(0, T_i) \tau_i \text{Bl}(K, L(0, T_{i-1}, T_i),$   
 $\sigma_i^{\text{SABR}}(K, L(0; T_{i-1}, T_i)) \sqrt{T_{i-1}}, 1)$   
(13)

where

$$\sigma_{i}^{\text{SABR}}(K,L) = \frac{\alpha_{i}}{(LK)^{\frac{1-\beta_{i}}{2}} \left[1 + \frac{(1-\beta_{i})^{2}}{24} \ln^{2}\left(\frac{L}{K}\right) + \frac{(1-\beta_{i})^{4}}{1920} \ln^{4}\left(\frac{L}{K}\right) + \cdots\right]} \frac{z}{x(z)}\n$$

$$\n\times \left\{1 + \left[\frac{(1-\beta_{i})^{2}\alpha_{i}^{2}}{24(LK)^{1-\beta_{i}}} + \frac{\rho_{i}\beta_{i}\epsilon_{i}\alpha_{i}}{4(LK)^{\frac{1-\beta_{i}}{2}}} + \epsilon_{i}^{2}\frac{2-3\rho_{i}^{2}}{24}\right]T_{i-1} + \cdots\right\} \tag{14}$$

with  $z := \frac{\epsilon_i}{\alpha_i} (LK)^{\frac{1-\beta_i}{2}} \ln\left(\frac{L}{K}\right)$  and  $x(z) := \ln\left\{\frac{\sqrt{1-2\rho_i z+z^2}+z-\rho_i}{1-\rho_i}\right\}$ . An analogous formula holds for floors.

The success of the SABR model is mainly due to the existence of an analytical formula for the implied volatilities  $\sigma_i^{\text{SABR}}$ , which is flexible enough to recover typical market smiles. In fact, it is a widespread practice to construct cap smiles by using the SABR functional form  $\sigma_i^{\text{SABR}}$ , assuming specific patterns for the parameters  $\alpha_i$ ,  $\beta_i$ ,  $\epsilon_i$ , and  $\rho_i$  between a caplet maturity and the next (e.g., piece-wise linear interpolation).

## References

- [1] Brace, A., Gatarek, D. & Musiela, M. (1997). The market model of interest rate dynamics, *Mathematical Finance* 7, 127-154.
- [2] Hagan, P.S., Kumar, D., Lesniewski, A.S. & Woodward, D.E. (2002). Managing smile risk, Wilmott Magazine September, 84-108.

- [3] Jamshidian, F. (1996). Sorting out swaptions, Risk March, 59-60.
- [4] Miltersen, K.R., Sandmann, K. & Sondermann, D. (1997). Closed form solutions for term structure derivatives with log-normal interest rates, The Journal of Finance 52,  $409 - 430.$

#### **Further Reading**

Brigo, D. & Mercurio, F. (2006). Interest-Rate Models: Theory and Practice. With Smile, Inflation and Credit, Springer Finance.

### **Related Articles**

Black-Scholes Formula; Forward and Swap Measures; LIBOR Market Model; LIBOR Rate; Put-Call Parity; Risk-neutral Pricing.

FABIO MERCURIO
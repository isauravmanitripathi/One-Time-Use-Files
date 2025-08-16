# **Bermudan Swaptions and Callable Libor Exotics**

In this article we give an overview of callable interest rate products, a product class that includes Bermudan swaptions as well as callable Libor exotics (CLE). The main contractual features of these securities are discussed, and an outline of valuation algorithms is provided. CLEs are among the most complicated fixed income exotics derivatives traded, combining state-dependent coupons with other features such as a Bermudan-style callability option. As a consequence, these securities are particularly challenging to price and risk-manage.

# **Market Overview**

CLEs most often start their life as callable structured notes. In a callable structured note, a *note issuer* receives the principal from an *investor* and pays a coupon, which is typically a function of interest rates, in return. In addition, the issuer retains the right to *call*, or *cancel*, the note on particular days, often coupon fixing days, after some initial *lock-out* (or *noncall*) period. When a note is called by the issuer, the principal is returned to the investor and the issuer stops paying the coupons.

As the principal received by the issuer is invested and typically yields a Libor rate (plus or minus a spread), a cancelable note is equivalent to a *cancelable swap*, that is, a swap of structured coupons against Libor rate payments that can be canceled on specified dates. Alternatively, it can be viewed as a noncancelable swap plus an option to *enter*, on a given set of dates, into a reverse swap. A CLE is typically defined to be such a *Bermudan-style option* to enter an exotic swap.

An investor granting the issuer the right to cancel the structured note is essentially selling a Bermudanstyle right to enter an exotic swap. In return, the issuer compensates by making the coupon more attractive, which is often the motivation for adding the callability feature in the first place.

# **Types of Structured Coupons**

CLEs are defined by the structured coupon they are paying, plus other features such as callability. In this section we review some common types of coupons that one can encounter in a CLE. Coupons are usually structured to let the investors take speculative views on the interest rate market or to provide protection against adverse scenarios. For example, a floored payoff can be chosen if an investor desires protection against a fall in interest rates.

A structured coupon can be any function of observed interest rates (such as Libor or constant maturity swap (CMS); *see* **LIBOR Rate**; **Constant Maturity Swap**) on or before its fixing date. Many types are available. They can roughly be split into four categories: Libor-based, CMS-based, spreadbased, and range-accruals.

To provide some detail, we assume in the following sections that a tenor structure is defined:

$$0 = T_0 < T_1 < \cdots < T_N, \quad \tau_n = T_{n+1} - T_n \quad (1)$$

Typically, the rate observations, or fixings, for the *n*th coupon are made at *Tn*, and the coupon pays at *Tn*+1, *n* = 1*,...,N* − 1.

#### *Libor-based Exotic Swaps*

A Libor-based structured coupon is a function of a single Libor rate. Let us denote the *n*th coupon as a function of the *n*th Libor rate observed on its fixing date by

$$C_n = C_n(L_n(T_n)) \tag{2}$$

There is a large variety of structured coupons *Cn(*·*)* that can be used. For example<sup>a</sup>

• *Standard swap*: For fixed coupon *k*,

$$C_n(x) = k \tag{3}$$

• *Capped and floored floaters*: For strike *s*, gearing *g*, cap *c*, and floor *f* ,

$$C_n(x) = \max(\min(g \times x - s, c), f) \qquad (4)$$

• *Capped and floored inverse floaters*: For spread *s*, gearing *g*, cap *c*, and floor *f* ,

$$C_n(x) = \max(\min(s - g \times x, c), f) \qquad (5)$$

• *Digitals*: For strike *s* and coupon *k*,

$$C_n(x) = k \times 1_{\{x > s\}} \tag{6}$$

• "*Flip-flops*" *or* "*tip-tops*": For strike *s* and two coupons, *k*<sup>1</sup> and *k*2, "low" and "high" coupons, the coupon is

$$C_n(x) = \begin{cases} k_1, & x \le s \\ k_2, & x > s \end{cases} \tag{7}$$

Different coupon types can be added together to create new types of structured coupons.

#### *CMS-based Coupons*

The same payoffs can be applied to CMS rates. Structured coupons are then deterministic functions of CMS rates. If an *m*-period rate is used, and we denote by *Sn,m(*·*)* the forward swap rate that fixes at *Tn* and covers *m* periods, then a structured coupon for period *n* is defined by

$$C_n = C_n(S_{n,m}(T_n)) \tag{8}$$

with *Cn(x)* as defined in the previous section.

#### *Spread-based Coupons*

Spread-based structured coupons differ from Liboror CMS-based ones in that they involve more than one market rate, Libor or CMS, in the calculation of structured coupons. The most common example is a CMS spread coupon. Let *Sn,a(*·*)* and *Sn,b(*·*)* be two collections of CMS rates, fixing on *Tn*, *n* ≥ 0, and covering *a* and *b* periods, respectively. A CMS spread coupon with gearing *g*, spread *s*, cap *c*, and floor *f* is then defined by

$$C_n = \max(\min(g \times (S_{n,a}(T_n) - S_{n,b}(T_n)) + s, c), f)$$
(9)

A more general example can be obtained by using one of the payoff functions *Cn(x)* defined in section Libor-based Exotic Swaps when applied to the spread *x* = *Sn,a(Tn)* − *Sn,b(Tn)*. In particular, digital and flip-flop CMS spread swaps are popular.

Spread-based exotic swaps typically cannot be decomposed into "standard" instruments, such as standard swaps, caps, and so on. Therefore, they, as a rule, cannot be valued by replication arguments, and a model is required.

More than two rates can be used in the definition of a coupon. Relatively recently, the so-called "curve caps" became popular. In a curve cap, a coupon rate (Libor or CMS) is capped at a level that is given by a function (typically a spread) of two (other) rates. Often, the coupon rate is also floored at (another) function of two (yet other!) rates. Thus, the definition of a curve cap coupon can involve up to five rates. If the coupon rate is itself a spread, six rates define the coupon.

#### *Range-accruals*

A range-accrual structured coupon is defined as a fixed (or, sometimes, floating; see below) rate that only accrues when a reference rate is within a certain range. Let *X(t)* be such a reference rate, and let *l* be the low bound and *u* be the upper bound. Let *k* be a fixed rate. A range-accrual coupon pays

$$C_n = k \times \frac{\#\{t \in [T_n, T_{n+1}] : X(t) \in [l, u]\}}{\#\{t \in [T_n, T_{n+1}]\}} \quad (10)$$

where #{·} is used to denote the number of days that a given criterion is satisfied.

The fixed coupon *k* can be replaced with, for example, a Libor rate or, much less commonly, a CMS rate or any other structured coupon. Similarly, the reference rate *X(t)* can be any market-observable rate such as a Libor rate fixing at *t*, a CMS rate fixing at *t*, or even a CMS spread.

A fixed-rate range-accrual coupon can be decomposed into simpler coupons, because

$$\begin{aligned} \#\{t \in [T_n, T_{n+1}] : X(t) \in [l, u]\} \\ &= \sum_{t \in [T_n, T_{n+1}]} 1_{\{X(t) \in [l, u]\}} \end{aligned} \tag{11}$$

The sum on the right-hand side is over all business days in the period [*Tn, Tn*+1]. Thus, the range-accrual coupon can be seen as a collection of digitals on the reference rate. A similar decomposition can be applied to floating range-accruals.

# **Bermudan Swaptions and Callable Libor Exotics**

#### *Definition*

A *Bermudan swaption* is a Bermudan-style option to enter a fixed-for-floating swap, that is, a swap with the "structured" coupon paying fixed rate,  $C_n(x) = k$ . Bermudan swaptions on payer (pay-fixed, receivefloating) swaps are called *payer Bermuda swaptions*; similar conventions hold for receiver swaps. Bermudan swaptions are actively traded in both the US and European markets, with well-developed interdealer market in the United States for shorter-dated Bermudan swaptions.

If the underlying swap is an exotic swap, that is, a swap paying a structured coupon as in the previous section, then the Bermuda-style option to enter it is called a CLE.

For a CLE on an exotic swap with structured coupons  $\{C_n\}_{n=0}^{N-1}$ , we denote the value of the exotic swap that one can exercise on date  $T_n$ , the so-called exercise value, by

$$E_n(t) = \beta(t) \sum_{i=n}^{N-1} \tau_i \mathbf{E}_t(\beta^{-1}(T_{i+1}) \times (C_i - L_i(T_i))),$$
  
$$t \le T_n \qquad (12)$$

where  $\beta$  is a numeraire and  $E_t$  denotes time t expectation in the probability measure associated with  $\beta$  (see Forward and Swap Measures).

#### Types of Callable Libor Exotics

Any exotic swap can be used as an underlying for a CLE. The "taxonomy" of CLEs follows closely that of structured coupons; see the section Types of Structured Coupons. As we already mentioned, the simplest type of a CLE is a Bermudan swaption, with the underlying being a fixed-for-floating swap. We can generally distinguish four types of CLEs, Libor-based, CMS-based, spread-based, and callable range-accruals. If the underlying is an inverse floating swap, the CLE is called a *callable inverse* floater, and so on.

#### CLEs Accreting at Coupon Rate

Typically the notional of the underlying swap of a CLE is the same throughout the life of the deal, but occasionally this is not the case. A notional can vary deterministically by, for example, increasing or decreasing by the same amount or at a certain rate each period. Such deterministic accretion rarely adds extra complications from a modeling prospective. Sometimes, however, a contract specifies that the

notional of the swap increases, or accretes, at the structured coupon rate. As the structured coupon is not known in advance, the accretion rate is not deterministic. For such CLEs, definition (12) has to be amended. For this, let  $q_i$  be the notional to be applied to the coupon paid at the end of the period  $[T_i, T_{i+1}]$ .  $q_i$  is obtained from the notional over the previous period  $q_{i-1}$  by multiplying it by the structured coupon over the previous period. Formally,

$$E_n(t) = \beta(t) \sum_{i=n}^{N-1} \tau_i \mathbf{E}_t(\beta^{-1}(T_{i+1}) \times q_i)$$
$$\times (C_i - L_i(T_i))),$$
$$q_i = q_{i-1} \times (1 + \tau_{i-1}C_{i-1}) \tag{13}$$

The initial notional  $q_0$  is contractually specified.

#### Snowballs

In a *snowball*, the structure coupon is not just a function of the interest rate, but of the previous coupon as well. The most common snowball is of inverse floating type. In particular, the  $n$ th coupon  $C_n$  is defined by

$$C_n = (C_{n-1} + s_n - g_n \times L_n(T_n))^+ \qquad (14)$$

for  $n = 1, \ldots, N - 1$  (with  $C_0$  usually being a simple fixed-rate coupon). Here  $\{s_n\}$  and  $\{g_n\}$  are contractually specified deterministic sequences of spreads and gearings. With this particular type of coupon, a snowball is sometimes called a *callable inverse ratchet*.

Many variants on the snowball idea have appeared recently, all variations on the theme of using a previous coupon in the definition of the current one. For example, a *snowrange* is typically defined by

$$C_n = C_{n-1} \times \frac{\#\{t \in [T_n, T_{n+1}] : X(t) \in [l, u]\}}{\#\{t \in [T_n, T_{n+1}]\}}$$
(15)

#### Multitranches

As we discussed previously, the more optionality an investor can sell to the issuer, the better coupon he/she can receive. The option to call the note is already present in a callable structured note. Another

option that is sometimes embedded is the right for the issuer to increase the size of the note, or put more of the same note to the investor, whether he/she wants it or not. The name of this feature, a *multitranche* callable structured note, comes from the fact that these possible notional increases are formalized as tranches of the same note that the issuer has the right to put to the investor.

The times when the issuer has the right to increase the notional of the note typically come before the times when the issues can cancel the note altogether. Callability usually applies jointly to all "tranches" of the note.

# **Valuation of Callable Libor Exotics**

The valuation of multicallable securities, such as Bermudan or American options, requires a solution of the optimal exercise problem, a type of a dynamic programming problem (*see* **Binomial Tree**). If we denote by *Hn(t)* the value, at time *t*, of a CLE that has only the dates {*Tn*<sup>+</sup>1*,...,TN*<sup>−</sup>1} as exercise opportunities, then the value of a CLE, the value *H*0*(*0*)*, is defined recursively by

$$H_{n-1}(T_{n-1}) = \beta(T_{n-1})\mathbf{E}_{T_{n-1}}(\beta(T_n)^{-1} \times \max\{H_n(T_n), E_n(T_n)\}),$$
  

$$n = N - 1, \dots, 1,$$
  

$$H_{N-1} \equiv 0 \tag{16}$$

Bermudan swaptions are the most liquid interest rate exotics. As their values are mostly derived from up- and down-moves of the yield curve, they are often valued in low-dimensional short-rate models such as developed in **Term Structure Models**, using lattice or PDE numerical methods (*see* articles in **Partial Differential Equations**). The value of the "switch" option built into a Bermudan swaption, that is, the option to change which swap is entered into, can be captured by a model parameter responsible for rate autocorrelations, such as mean reversion in a one-factor Gaussian model, see [1]. To value other types of CLEs, a more involved setup is usually required. Complicated dependence of coupons on one or more underlying rates, combined with the need to account for callability, typically necessitates an application of a realistic, multifactor model of interest rates such as the Libor market model (*see* **LIBOR Market Model**). Owing to the high dimension of such a model, Monte Carlo methods become a necessity (*see* **LIBOR Market Models: Simulation**) and must be complemented by methods for estimating exercise boundaries of Bermudan-style options in Monte Carlo simulation (*see* **Bermudan Options**; **Exercise Boundary Optimization Methods**; **Early Exercise Options: Upper Bounds**). Additional details are available in [2].

# **End Notes**

a*.* Note that in all definitions we ignore day counting fractions.

# **References**

- [1] Andersen, L.B. & Andreasen, J. (2001). Factor dependence of Bermudan swaption prices: fact or fiction? *Journal of Financial Economics* **62**, 3–37.
- [2] Piterbarg V.V. (2005). Pricing and hedging callable Libor exotics in forward Libor models. *Journal of Computational Finance* **8**(2), 65–117.

# **Related Articles**

**Bermudan Options**; **Binomial Tree**; **Early Exercise Options: Upper Bounds**; **Exercise Boundary Optimization Methods**; **LIBOR Market Model**; **LIBOR Market Models: Simulation**.

```
LEIF B.G. ANDERSEN & VLADIMIR V.
                       PITERBARG
```
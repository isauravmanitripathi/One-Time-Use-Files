# **Equity–Credit Problem**

The equity–credit problem, perhaps the most significant problem of corporate finance, is the problem of linking the value of a firm's equity with that of its debt. Etymologically, the word "credit" is linked to credence, belief, faith, and confidence. As such it is passive and absolute; the only contingency that may affect it is default. One lends money to another on the faith that he/she will pay back the same. This introduces an asymmetry. The debtor may renege and the creditor will try to put his/her assets or company in bankruptcy. Equity, by contrast, is symmetric. Participating in somebody's equity is agreeing to share the profits, the losses, and the risks of the enterprise. Its only contingency is what action (not passion) the future has in stock for the shareholders. The word *equity* means "fairness" and the word for *share*, in French, is *action*.

The pricing and hedging of convertible bonds (*see* **Convertible Bonds**) is an example of equity-to-credit problem: the optimal conversion policy intimately fuses the two. Once the hazard rate (*see* **Hazard Rate**) is made explicit alongside the price process of the underlying stock, it is followed by the question what kind of correlation can prevail between the two. Trying to model this correlation is the quantitative side of the equity-to-credit problem.

Derivative pricing models are almost never used normatively, going from theoretical parameter to derivative theoretical value. They are used in reverse, going from derivative *market* price to implied parameters (*see* **Implied Volatility Surface**). From this, it becomes apparent that a single volatility parameter cannot explain the variety of prices of options of different strikes and different maturities (the volatility smile), not mentioning that credit default swaps (CDSs, *see* **Credit Default Swaps**) are also written on the company and traded. The equityto-credit problem, as it is understood today, is to find a unifying derivative pricing framework where the full volatility surface of equity options and the full term-structure of CDS spreads can be explained.

Corporate events, which may have been lost under the impassive writing of derivative payoffs, thus reemerge as the script, waiting for our examination, that the prices of equity derivatives and the prices of credit derivatives now *jointly* compose. The volatility skew of out-of-the-money puts, the term structures of volatility and credit spread, all of which are commonly observed on single names, cannot be handled by Black–Scholes–Merton (BSM) or by any of the models that tried to improve on it simply by tweaking its assumptions (local volatility (*see* **Local Volatility Model**), Heston stochastic volatility model (*see* **Heston Model**), etc.). These price structures are best (and most robustly) explained by a *regimeswitching model* (*see* **Regime-switching Models**). In this model, the volatility of the underlying share and the hazard rate can suddenly switch between different and very dissimilar regimes, accompanied by substantial jumps of the underlying equity price. Default itself is one such regime, except that it is a regime of a very extreme sort. Takeover and restructuring are other regimes. Poisson processes trigger the various switches, and the regime changes then lend themselves naturally to a reinterpretation in terms of *corporate events* [1]. The equity-to-credit problem, when it is reinterpreted in terms of derivative pricing, imprints back corporate events on market prices.

# **A Regime-switching Model**

There exist *K* volatility regimes, indexed from 1 to *K*, and one default regime, indexed by *d*. We assume that the regimes are observable and known at any time. By convention, regime 1 can be set as the present regime when we use the model, either to value contingent claims or to calibrate the model against their market prices. We let the discrete variable *ut* describe the current regime at time *t*. The dynamics of the regime is driven by a continuous time Markov process with a finite number of states or regimes. The important correlation between the stock price and its volatility, as well as between the stock price and the hazard rate, is captured by a possible jump on the stock price as a regime switch occurs. Here, we chose to model jumps by a very simple fixed percentage size jump; it would be possible to generalize to a density of jumps.

- *λ*ˆ *<sup>k</sup>*→*<sup>l</sup>* is the (risk neutral) intensity of going from regime *k* to regime *l*. This occurs with a percentage jump *yk*<sup>→</sup>*<sup>l</sup>* on the stock price.
- *λ*ˆ *<sup>k</sup>*→*<sup>d</sup>* is the (risk neutral) intensity of going from regime *k* to default. The corresponding jump on

the stock price is  $y_{k\rightarrow d}$ . When  $y_{k\rightarrow d} = -1$ , the stock goes to zero upon default.

- We let  $v_k$  and  $v_d$  be the volatility in regime k and in default, respectively. The jumps indexed from  $i = K$  to J correspond to stock price jumps inside a regime, which may be the default regime. Both the size and the intensity of the jumps depend on the regime.
- In every regime, we index the jumps in the following way. For *i* between 1 and  $(K-1)$ , the jump corresponds to a regime switch, which is also denoted as  $y_{k\rightarrow l}$  if the current regime is k and if the jump goes into regime  $l$ . For  $i$  between  $K$ and  $J$ , the jump is a pure stock price jump within a regime. For  $i = (J + 1)$ , the jump corresponds to default, also denoted as  $y_{k\rightarrow d}$  if the current regime is  $k$ .
- There is no recovery from the default regime so that  $\hat{\lambda}_{d \to k} = 0$ . However, there may be jumps in the stock price within the default regime.

For simplicity, we consider a nonstochastic riskfree term structure, and we denote the deterministic instantaneous forward rate at time t as  $r_t$ . We consider the most general setting with both continuous and discrete time dividends, although both are usually not present at the same time.  $r_t^f$  is the nonstochastic continuous dividend rate at time  $t$  (this notation stems from the foreign exchange market).

### **Pricing Equations**

We consider a general derivative instrument with value  $F(t, S_t, u_t)$  at time t when the stock price is  $S_t$ and the current regime is  $u_t$ . We have the following partial decoupling between the nondefault regimes and the default one.

- The value  $F(t, S_t, d)$  in the default regime can be computed on a stand-alone basis, without knowledge of  $F$  in the nondefault regimes.
- The value of  $F$  in the nondefault regimes gives rise to  $K$ -coupled equations, which, in general, involve the value of  $F$  in the default regime, unless the derivative is a call and the stock goes to zero upon default.

#### Stand-alone Default Regime

We start by evaluating the value of the general derivative  $F$  in the default regime. It is given by

the following stand-alone equation, which does not depend on the value of  $F$  in the nondefault regimes:

$$\frac{\partial F}{\partial t} + \frac{1}{2} v_d^2 S_t^2 \frac{\partial^2 F}{\partial S_t^2} + \left(r - r^f - \sum_{j=K}^J \hat{\lambda}_j y_j\right) S_t \frac{\partial F}{\partial S_t}$$
$$+ \sum_{j=K}^J \hat{\lambda}_j \left(F(t, S_t(1+y_j), d) - F(t, S_t, d)\right) = rF$$
(1)

with appropriate boundary conditions. The sums  $\sum_{j=K}^{J} \hat{\lambda}_{j}^{T} y_{j}$  and  $\sum_{j=K}^{J} \hat{\lambda}_{j} \Delta F$  correspond to stock price jumps inside the default regime.

#### Coupled Nondefault Regimes

For every nondefault regime  $u_t$ ,

$$\frac{\partial F}{\partial t} + \frac{1}{2} v_{u_t}^2 S_t^2 \frac{\partial^2 F}{\partial S_t^2} + \left( r - r^f - \sum_{j=1}^{J+1} \hat{\lambda}_j y_j \right) S_t \frac{\partial F}{\partial S_t} \\
+ \sum_{j=K}^{J} \hat{\lambda}_j (F(t, S_t(1+y_j), u_t) - F(t, S_t, u_t)) \\
+ \sum_{l \neq u_t} \hat{\lambda}_{u_t \to l} (F(t, S_t(1+y_{u_t \to l}), l) \\
- F(t, S_t, u_t)) \\
+ \hat{\lambda}_{u_t \to d} (F(t, S_t(1+y_{u_t \to d}), d) \\
- F(t, S_t, u_t)) = rF \tag{2}$$

again with appropriate boundary conditions. A few remarks concerning this equation are given below:

- We note that in the general case the value of  $F$ in the default regime is needed here.
- The sum  $\sum_{j=1}^{J+1} \hat{\lambda}_j y_j$  corresponds to a sum on all stock price jumps that may occur from the current regime  $u_t$ , both inside the regime and from the regime  $u_t$  to another one, including default. Although the notation is not explicit, the terms of this sum depend on the current regime  $u_t$ .
- The sum  $\sum_{i=K}^{J} \hat{\lambda}_j \Delta F$  corresponds to the stock price jumps inside the current regime  $u_t$ .
- The sum  $\sum_{l\neq u_{t}} \ddot{\lambda}_{u_{t}\rightarrow l} \Delta F$  corresponds to the changes in regime, from the current regime  $u_t$ to the other nondefault regimes indexed by  $l$ .

• The last term *λ*ˆ *ut*<sup>→</sup>*dF* corresponds to a jump from the current regime *ut* to the default.

### *Dividends*

In the absence of arbitrage, the derivative must be continuous across the payment of dividends. At a time *ti* when a fixed dividend *di(Sti*−*)* is paid by the company, we have

$$F(t_i-, S_{t_i-}, u_{t_i}) = F(t_i, S_{t_i}, u_{t_i})$$
  
=  $F(t_i, S_{t_i-} - d_i(S_{t_i-}), u_{t_i})$  (3)

where *uti* can be any regime, including default.

The same reasoning applies for proportional dividends. At a time *tj* when a proportional dividend *δjStj*<sup>−</sup> is paid by the company, we have

$$F(t_j-, S_{t_j-}, u_{t_j}) = F(t_j, S_{t_j}, u_{t_j})$$
  
=  $F(t_j, (1 - \delta_j)S_{t_j-}, u_{t_j})$  (4)

where again *utj* can be any regime, including default.

# **Credit Default Swaps**

### *Definitions*

We describe the contingent cash flows of the CDS, when the current time is *t* and the current nondefault regime is *ut* .

- The nominal of the CDS is 1.
- The payment frequency of the premium is *t*, a fraction of a year, which can be 1 for one year, 1*/*2 for a semester, 1*/*4 for a quarter, or 1*/*12 for one month.
- We let *N* ≥ 1 be the number of remaining premium payments, assuming no default up to maturity of the CDS.
- The first premium payment occurs at time *t*1, with the constraint that 0 *< (t*<sup>1</sup> − *t)* ≤ *t*.
- The remaining premium payments occur after *t*<sup>1</sup> with a constant interval *t*, which means that the dates of premium payments are denoted as *ti* = *t*<sup>1</sup> + *(i* − 1*)t* for *i* between 1 and *N*.
- The maturity *T* of the CDS is the last premium payment, that is, *T* = *tN* = *t*<sup>1</sup> + *(N* − 1*)t*.

- We define *t*<sup>0</sup> = *t*<sup>1</sup> − *t*, which is either the date of the last premium payment before *t* or the issue date of the CDS.
- *S* is the premium of the CDS paid until default with the payment frequency *t* after the first payment date *t*1. If default occurs at time *τ* and the last premium payment was at time *ti*, then the buyer of insurance still owes the accrued premium, defined as the linear fraction of the next premium payment, that is, *S(τ* − *ti)/t*.
- Let *R* be the recovery, between 0 and 1. Upon default, the party insured receives *(*1 − *R)* at the time *τ* of default, if default occurs before maturity *T* , and nothing otherwise.
- For a time *t* and a regime *ut* , we let *<sup>F</sup>*CDS*(t, ut* ; *<sup>t</sup>*1*, t, N , S, R)* be the value at time *t* when the regime is *ut* of the CDS with premium *S* and recovery *R*, whose sequence of premium payment dates is described by *t*1, the date of the first one, *t* the constant time between two premium payments after the first one, and *N* the total number of premium payments. Its maturity is *T* = *t*<sup>1</sup> + *(N* − 1*)t*. This value assumes the point of view of the holder of the CDS. He/she is the party who seeks insurance against default risk and who pays the streams of premia in exchange for a compensation in the case of default. When *ut* = *d*, we assume that default occurred at time *<sup>t</sup>* exactly, and *<sup>F</sup>*CDS*(t, d*; *<sup>t</sup>*1*, t, N , S, R)* values the benefit of the insurance upon default. At a time *ti* of premium payment, we assume that *<sup>F</sup>*CDS*(ti, ut* ; *<sup>t</sup>*1*, t, N , S, R)* corresponds to the value ex premium payment, that is, just after the payment of the premium *S*. When *(t*1*, t, N )*, the maturity *T* , the premium *S*, and the recovery *R* are understood, we simply write *<sup>F</sup>*CDS*(t, ut)*.

### *Value in Default*

Let *F*CDS*(t, d)* be the value of the CDS at time *t* assuming that default has occurred at time *t*. It is the difference between the compensation immediately received and the accrued premium still owed:

$$F^{\text{CDS}}(t, d) = 1 - R - S \frac{(t - [t])}{\Delta t}$$
 (5)

#### **Backward Equation**

We derive a backward equation for the value  $F^{\text{CDS}}(t, u_t)$  of the CDS. At maturity T and for every nondefault regime  $k$ , we have

$$F^{\text{CDS}}(T,k) = 0 \tag{6}$$

$$F^{\text{CDS}}(T-,k) = -S \tag{7}$$

since maturity  $T$  corresponds to the last premium payment. At a time  $t$  different from any premium payment date and for every nondefault regime  $k$ , we have

$$\begin{split} \frac{\partial F^{\text{CDS}}}{\partial t}(t,k) &+ \sum_{l \neq k} \hat{\lambda}_{k \rightarrow l} \\ &\times \left( F^{\text{CDS}}(t,l) - F^{\text{CDS}}(t,k) \right) \\ &+ \hat{\lambda}_{k \rightarrow d} \left( F^{\text{CDS}}(t,d) - F^{\text{CDS}}(t,k) \right) \\ &= r F^{\text{CDS}}(t,k) \end{split} \tag{8}$$

where the value in default  $F^{\text{CDS}}(t, d)$  has been derived in equation (5). At a time  $t_i = t_1 + (i - 1)\Delta t$ where the premium  $S$  is paid, we have

$$F^{\text{CDS}}(t_i-, k) = F^{\text{CDS}}(t_i, k) - S \tag{9}$$

which means that the value of the CDS increases by S after each premium payment. This yields a system of *K*-coupled backward equations.

The regime-switching model represents *corporate events* in terms of jumps. The volatility parameters  $v_k$  and  $v_d$ , the regime-switching intensities  $\lambda_{k\rightarrow l}$  and  $\lambda_{k\rightarrow d}$ , and the corresponding jump sizes  $y_{k\rightarrow l}$  and  $y_{k\rightarrow d}$  are all inferred by calibration of the model to the market prices of equity options and CDS spreads. This is achieved by solving an inverse problem characterized by the pricing equations above. For this reason, the regime-switching model is perfectly suited for pricing the convertible bond (see Convertible Bonds).

#### References

[1] Ayache, E. (2004). The Equity-to-Credit Problem. The Best of Wilmott 1, Incorporating the Quantitative Finance Review, 2004, John Wiley & Sons, Chichester, West Sussex, pp. 79-107.

## **Further Reading**

- Ayache, E., Forsyth, P.A. & Vetzal, K.R. (2002). Next generation models for convertible bonds with credit risk, Wilmott December  $68-77$
- Ayache, E., Forsyth, P.A. & Vetzal, K.R. (2003). The valuation of convertible bonds with credit risk, Journal of Derivatives  $11 \ 9 - 29$
- Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, Journal of Political Economy 81, 637-654.
- Ferguson, N. (2008). The Ascent of Money: A Financial History of the World, Allen Lane, Penguin Books, London, 119–175. Goldman, S. (1994). Valuing Convertible Bonds as Derivatives.
- Quantitative Strategies Research Notes, Goldman Sachs.
- Hull, J. (2008). Options, Futures, and Other Derivatives, 7th Edition, Prentice-Hall, Englewood Cliffs, New Jersey.
- MacKenzie, D. (2003). An equation and its worlds: bricolage, exemplars, disunity and performativity in financial economics, Social Studies of Science 33, 831-868.
- Smith, C.W. (2007). Markets as definitional practices, The Canadian Journal of Sociology  $32(1)$ , 1–39.
- Thorp, E.O. & Kassouf, S.T. (1967). Beat the Market, Random House, New York.
- Tsiveriotis, K. & Fernandes, C. (1998). Valuing convertible bonds with credit risk, Journal of Fixed Income 8, 95–102.
- Wilmott, P. (2006). Paul Wilmott on Quantitative Finance, 2nd Edition, John Wiley & Sons, London.

## **Related Articles**

Convertible Bonds; Credit Default Swaps; Hazard Rate; Regime-switching Models; Structural **Default Risk Models.** 

ÉLIE AYACHE
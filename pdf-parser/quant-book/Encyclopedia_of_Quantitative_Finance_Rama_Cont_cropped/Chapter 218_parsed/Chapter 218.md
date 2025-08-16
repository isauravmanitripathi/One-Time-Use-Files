# **Bond Options**

Bond options are contracts giving their buyer the right but not the obligation to buy (call option) or sell (put option) an underlying bond at a prespecified price (the strike price). The strike for options on bond prices is generally quoted in terms of clean price (i.e., not including the accrued interest). Upon exercise, the bond buyer pays the accrued interest to the bond seller. In some cases, the contract for options on bonds may specify a strike yield instead of a strike price. Since price and yields move in opposite directions, a call (put) option on price will correspond to a put (call) option on yield.

Option contracts have a termination date referred to as the *expiration date* and are classified based on the possible dates in which the option holder can exercise the option. European-style options can be exercised only at the contract's expiration date. Bermudan-style options may be exercised on a prespecified set of dates up to (or including) the expiration date, whereas American-style options can be exercised at any time up to (and including) the expiration date.

Most of the activity for options on cash bonds is over the counter (OTC) and has government bonds as the underlying, with the most common being options on long-term treasury bonds. The exchange-traded market for options on cash bonds is virtually nonexistent. Among the existing contracts, we mention the European options on treasury yields for 13-week treasury bills, 5- and 10 year treasury notes, and 30-year treasury bonds traded on the Chicago Board of Exchange (CBOE). These contracts are cash-settled, that is, there is no delivery of the physical underlying bond at exercise.

Closely related contracts are options on bond futures. These are exchange traded and significantly more liquid than options on cash bonds. In a bond futures contract, the side with the short position can deliver any bond in a predefined basket. For example, in the 30-year US treasury bond futures contract, \$100 000 of any US treasury bond that is not callable for at least 15 years and has a maturity of at least 15 years can be delivered. When a call (put) option on a bond futures is exercised, the buyer receives a cash payoff and is assigned a long (short) position in the underlying futures contract. The seller is assigned the corresponding opposite position. The most popular options on futures contracts are those on 5- and 10-year US treasury notes and 30-year US treasury bonds traded at the Chicago Board of Trade (CBOT). Exchangetraded options on bond futures are typically American style.

Besides being traded as separate contracts, bond options frequently appear as provisions in the bond contract itself. In this case, because they cannot be traded separately, they are referred to as *embedded options*. The most common types are call provisions, giving the issuer the right but not the obligation to buy back the bond at a predetermined price. Bonds containing a call provision are known as *callable bonds*. Analogously, putable bonds give the bond holder the right but not obligation to sell the bond back to the issuer at a predetermined strike price. A callable bond buyer is effectively buying the underlying noncallable bond and selling a call option on a bond to the issuer. In the case of a putable bond, the issuer is selling a put option to the bond holder along with the underlying nonputable bond. As with regular options, the embedded call and put options can be European, Bermudan, or American style.

Finally, as shown later, there is a close relationship between options on bonds and the most commonly traded OTC options on interest rates, namely, cap, floors, and swaptions. A cap (floor) is equivalent to a portfolio of European put (call) options on zero coupon bonds, whereas a swaption can be seen as an option on a fixed coupon bond.

We restrict our discussion in the following to the pricing of options on default-free bonds. The treatment of options on defaultable bonds is substantially more complex, since it requires consideration of both interest rate and credit components and their interaction. For more information, we refer to [6] and references therein.

# **European Options**

We denote the price of a default-free zero coupon bond at time *t* maturing at *T* by *P (t, T )*. Consider European call and put options with strike *K* and expiration *Te* written on a zero-coupon bond with maturity *Tm* ≥ *Te*. Their payoffs at time *Te* are given as

$$\max\{\omega(P(T_e, T_m) - K), 0\} = [\omega(P(T_e, T_m) - K)]^+$$
(1)

with  $\omega = 1$  for a call and  $\omega = -1$  for a put.

Default-free bullet bonds pay, with certainty, predetermined amounts  $c_i$  at times  $T_i$ ,  $i = 1, \ldots, M$ . We assume, for convenience, that the last payment also includes the repayment of principal. Their price can be trivially expressed in terms of prices of zero coupon bonds. More generally, defining for any given time  $T, l(T) := \max\{i \in 1, \ldots, M : T_i < T\}$ , we can express the time  $t \leq T$  value of the cash flows to be received after  $T$  as

$$B_{\rm cp}(t, T, \{c\}) = \sum_{i=l(T)+1}^{M} c_i P(t, T_i) \tag{2}$$

Call and put options on this bond expiring at time  $T$  and with strike price  $K$  are options on a portfolio of zero coupon bonds having payoff

$$\max\{\omega(B_{\rm cp}(T, T, \{c\}) - K), 0\} \tag{3}$$

with  $\omega = 1$  for a call and  $\omega = -1$  for a put.

Modeling typically proceeds in one of two ways. The first involves directly modeling the stochastic evolution of a finite number of bond prices (or yields) and is in essence an extension of the Black-Scholes-Merton approach [3, 10] to the pricing of option on bonds. The second involves modeling the stochastic evolution of the wholeterm structure of interest rates, or equivalently, the simultaneous evolution of zero coupon bonds of all maturities. A rather general framework for term structure modeling was proposed by Heath, Jarrow, and Morton (HJM) [7] (see also **Heath–Jarrow–Morton Approach**), who modeled the instantaneous forward rates as diffusion processes and established the appropriate conditions that need to be satisfied to ensure the absence of arbitrage opportunities. In the term structure modeling approach, the dynamics of bonds and other interest rate instruments follow as a consequence of the stochastic model imposed on the term structure of interest rates.

#### Black-Scholes Model

Historically, the first approach for valuing bond options made direct use of the Black-Scholes-Merton model (see also **Black–Scholes Formula**). It assumed a geometric Brownian motion process with constant instantaneous volatility for the price process of the underlying bond and a deterministic short-term interest rate. The time 0 price of call and put options on a European bond option with strike price  $K$  and expiring at time  $T_e$ , under this model, is

$$\begin{aligned} \text{Call}(0, K, T_e, \{c\}) \\ &= e^{-RT_e} \text{Bl}(K, e^{RT_e} B(0, T_e, \{c\}), \sigma_B \sqrt{T_e}, 1) \\\\ \text{Put}(0, K, T_e, \{c\}) \\ &= e^{-RT_e} \text{Bl}(K, e^{RT_e} B(0, T_e, \{c\}), \sigma_B \sqrt{T_e}, -1) \end{aligned} \tag{4}$$

where

$$\mathrm{Bl}(K,F,v,\omega) := F\omega\Phi\left(\omega\frac{\ln(F/K) + \frac{1}{2}v^2}{v}\right) - K\omega\Phi\left(\omega\frac{\ln(F/K) - \frac{1}{2}v^2}{v}\right)$$
(5)

 $\Phi$  denotes the standard Gaussian cumulative distribution function and  $R$  is the continuously compounded spot interest rate for time  $T_e$  and  $\sigma_B$  the bond price volatility.

Similar to the convention used in the equity market, option prices are also quoted in terms of their implied volatility, namely, the constant volatility to be imputed in Black's formula so as to reproduce the option price. In some situations, the market quotes implied yield volatilities rather than implied price volatilities. The conversion from a yield volatility to a price volatility is given as

$$\sigma_B = Dy\sigma_Y \tag{6}$$

where  $\sigma_B$  is the bond's price volatility, D is its modified duration, and  $\sigma_Y$  is its yield volatility.

There are some obvious drawbacks to the Black-Scholes-Merton approach applied to bond options. First, contrary to stocks, bond prices tend to their face value at maturity (the so-called "pull to par" effect), implying that their instantaneous volatility must go to zero as they approach maturity. Under a constant volatility assumption, the model is only appropriate in situations where the time to expiration is significantly shorter than the underlying bond's maturity. Another drawback is that given the lognormal distribution of prices, there is a nonzero probability that the price of the bond will be larger than the sum of the future cash flows, implying negative yields. Finally, the fact that bonds are modeled independently of each other does not guarantee the absence of arbitrage between them.

#### Black's 1976 Model

In 1976, Black [2] extended the Black-Scholes-Merton analysis to commodity contracts. An important point was the shift in focus toward forward rather than spot quantities. Under this perspective, one can try and model the underlying bond's forward price F for delivery at time  $T_e$  as a geometric Brownian motion with deterministic volatility  $\sigma_F(t)$ . Let R be the time 0 continuously compounded spot rate for time  $T_e$ . The pricing formulas for European bonds become

$$\begin{aligned} \text{Call}(0, K, T_e, \{c\}) \\ &= e^{-RT_e} \text{Bl}(K, F, \Sigma_F \sqrt{T_e}, 1) \\ \text{Put}(0, K, T_e, \{c\}) \\ &= e^{-RT_e} \text{Bl}(K, F, \Sigma_F \sqrt{T_e}, -1) \end{aligned} \tag{7}$$

with  $\Sigma^2_F := 1/T_e \int_0^T \sigma_F^2(s) ds$  the squared volatility of the bond's forward price. Note that in equation  $(4)$  we take the underlying as the bond's spot price with its corresponding volatility, whereas in equation  $(7)$  the underlying is the bond's forward price with its corresponding volatility. Since the forward price for time  $T_e$  is given by the ratio of the spot price and the zero coupon bond maturing at  $T_e$ , these two volatilities are not the same.

A further change in perspective led to the use of Black's model applied to forward rates rather than to forward prices. In the case of zero coupon bonds, define the simple compounded forward rate:

$$L(t;T_e,T_m) := \frac{1}{\tau} \left[ \frac{P(t,T_e)}{P(t,T_m)} - 1 \right], \quad t \le T_e \quad (8)$$

where  $\tau$  denotes the year fraction for  $(T_e, T_m]$ . By using a standard change of measure (see also Forward and Swap Measures) it is easy to show that

$$P(0, T_e)E^{T_e}\{[P(T_e, T_m) - K]^+\}$$
  
=  $P(0, T_m)\tau KE^{T_m}\left\{\left[\frac{1-K}{\tau K} - L(T_e; T_e, T_m)\right]^+\right\}$   
(9)

where  $E^T$  denotes expectation with respect to a measure having as numeraire the zero coupon bond maturing at  $T$ . Therefore, a call option on a zero coupon bond can be regarded as a put option on the forward rate  $L(T_e; T_e, T_m)$ . We can now use Black's model on the forward rate  $L$  assuming that it follows geometric Brownian motion with volatility  $\sigma_L(t)$ . The time 0 price of a call option with strike  $K$  and time to expiration  $T_e$  on a zero coupon bond maturing at  $T_m$  can then be written as

$$\begin{aligned} \text{Call}_{zc}(K, T_e, T_m) \\ &= \tau K P(0, T_m) \\ &\quad \times \text{Bl}(K', L(0, T_e, T_m), \Sigma_L \sqrt{T_e}, -1) \end{aligned} \tag{10}$$

with  $K' = \frac{1 - K}{\tau K}$  and  $\Sigma^2_L := 1/T_e \int_0^{T_e} \sigma_L^2(s) ds$ .<br>A similar argument can be used to obtain the

price of put options on zero coupon bonds in terms of the prices of call options on the forward rate  $L(T_e; T_e, T_m)$ . In the OTC market for London Interbank Offered Rate (LIBOR) rate based interest rate derivatives, it became market standard to express options in terms of forward rates and to use Black's formula for valuation (see also Risk-neutral Pricing). There is also an analogous relationship between options on coupon bonds and swaptions, which are options on forward swap rates.

Alternative models having the bond price as the only state variable have been proposed to account for some of the shortcomings of the Black-Scholes model. Ball and Torous [1] modeled the rate of return on a discount bond by a Brownian bridge process, which guarantees that the bond price converges to its face value at maturity. Schaefer and Schwartz [13] proposed a model where the price volatility of a coupon bearing bond is proportional to the duration and, therefore, decreases as the bond approaches maturity. Further attempts in this direction are reviewed by Rady and Sandmann [12].

### **Term Structure Models**

As we have mentioned, the HJM approach is a rather general framework for modeling the full-term structure, guaranteeing no arbitrage. To make progress and obtain explicit results for the price of options on bonds, one needs to choose concrete realizations. Among the most popular are the so-called *short-rate models*, which, as their names indicate, focus on the modeling of the instantaneous short rate *r(t)* (*see also* **Term Structure Models**) defined as

$$r(t) = \frac{-\mathrm{d}\log P(t,T)}{\mathrm{d}T}|_{T=t}$$
(11)

These models have a long history, dating back to Merton [10] and Vasicek [14]. In general, the short-rate process is assumed to follow a continuous Markov process, in which case prices of zero coupon bonds become a function of the short rate *r(t)*. The payoff for a European call option expiring at *T* on a coupon bond can then be written as

$$\left(\sum_{i=1}^{n} c_{i} P(r(T), T, T_{i}) - K\right)^{+} \tag{12}$$

If the zero coupon bond price is a continuous decreasing function of *r(t)*, the option will be exercised if and only if *r(T ) < r*<sup>∗</sup>, where *r*<sup>∗</sup> is the solution of

$$\sum_{i=1}^{n} c_i P(r^*, T, T_i) = K \tag{13}$$

In this case, one can decompose the value of the option into a sum of options on zero coupon bonds by rewriting the payoff as

$$\sum_{i=1}^{n} c_i (P(r(T), T, T_i) - P(r^*, T, T_i))^+ \qquad (14)$$

The aforementioned decomposition was discovered by Jamshidian [8] and is sometimes called the *Jamshidian formula*. Several popular term structure models allow for an exact solution for the price of zero coupon bonds in terms of the model parameters. Among them are the Vasicek/Hull–White [14] (*see also* **Cox–Ingersoll–Ross (CIR) Model**) and the Cox– Ingersoll–Ross (CIR) [5] (*see* **Gaussian Interest-Rate Models**) models. In their onefactor version, these two models satisfy the requirement that discount bonds are monotonically decreasing in the short rate, allowing us to obtain the prices of options on coupon bonds in terms of the prices of options on zero coupon bonds.

### **Bermudan and American Bond Options**

The pricing of Bermudan and American options is significantly more complex than their European counterpart. There are typically no closed-form solutions and one needs to resort to numerical methods for computing their value. A common approach is to calibrate a term structure model to European options and subsequently use the calibrated model to price American and Bermudan securities. The latter step would typically involve a numerical scheme such as Monte Carlo simulation or a finite difference method. Among the most popular models used are the one- and two-factor short-rate models (*see also* **Term Structure Models**) as well as the LIBOR market model (*see* **LIBOR Market Model**) family [4, 9, 11]).

### **References**

- [1] Ball, C.B. & Torous, W.N. (1983). Bond price dynamics and options, *Journal of Financial and Quantitative Analysis* **19**, 517–531.
- [2] Black, F. (1976). The market model of interest rate dynamics, *Mathematical Finance* **7**, 127–154.
- [3] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**(3), 637–654.
- [4] Brace, A., Gatarek, D. & Musiela, M. (1997). The market model of interest rate dynamics, *Mathematical Finance* **7**, 127–154.
- [5] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–407.
- [6] Duffie, D. & Singleton, K.J. (2003). *Credit Risk: Pricing, Measurement and Management*. Princeton Series in Finance.
- [7] Heath, D., Jarrow, R.A. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**(1), 77–105.

- [8] Jamshidian, F. (1989). An exact bond option formula, *The Journal of Finance* **44**(1), 205–209.
- [9] Jamshidian, F. (1997). Libor and swap market models and measures, *Finance and Stochastics* **1**(4), 293–330.
- [10] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**(1), 141–183.
- [11] Miltersen, K.R., Sandmann, K. & Sondermann, D. (1997). Closed form solutions for term structure derivatives with log-normal interest rates, *The Journal of Finance* **52**, 409–430.
- [12] Rady, S. & Sandmann, K. (1994). The direct approach to debt option pricing, *The Review of Futures Markets* **13**(2), 461–515.
- [13] Schaefer, S. & Schwartz, E. (1987). Time-dependent variance and the pricing of bond options, *The Journal of Finance* **42**(5), 1113–1128.
- [14] Vasicek, O. (1977). An equilibrium characterisation of the term structure, *Journal of Financial Economics* **5**, 177–188.

## **Further Reading**

- Black, F., Derman, E. & Toy, W. (1990). A one-factor model of interest rates and its application to treasury bond options, *Financial Analysts Journal* **46**, 24–32.
- Brigo, D. & Mercurio, F. (2006). *Interest-Rate Models: Theory and Practice. With Smile, Inflation and Credit*, Springer Finance.

### **Related Articles**

**Black–Scholes Formula**; **Caps and Floors**; **Cox– Ingersoll–Ross (CIR) Model**; **Forward and Swap Measures**; **Gaussian Interest-Rate Models**; **LIBOR Market Model**; **LIBOR Rate**; **Put–Call Parity**; **Term Structure Models**.

MARCELO PIZA
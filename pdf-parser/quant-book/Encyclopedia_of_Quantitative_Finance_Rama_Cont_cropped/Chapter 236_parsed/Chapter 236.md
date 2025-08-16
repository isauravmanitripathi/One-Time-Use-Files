# **Hedging of Interest Rate Derivatives**

# **Cash and the Zero Curve**

The simplest contract is a unit notional, zero-coupon bond to be paid at time *T* (the *maturity*). The value of such a bond is denoted by *P (T )*. a

The function *P* thus describes the evolution through time of interest rate expectations.

The instantaneous *forward rate f* is defined by *f (T )* ≡ −*P*-*(T )/P (T )*. Thus, the *forward curve f* provides a local view of the market forecast for future interest rates. While knowledge of *P* and *f* are in principle equivalent, the latter provides a superior framework for practical analysis.

# **FRAs, Swaps, and Bond Equivalence**

A forward rate agreement, *FRA*, is a contract to lend at a previously agreed rate over some time interval—thus it is equivalent to a calendar spread of zero-coupon bonds. A swap is very similar to a succession of FRAs, so its price can nearly be determined from the zero curve. The slight differences between Libor swaps and coupon-paying bonds stem from the differences between the Libor end date and the period payment date, and also (in most currencies) the difference between fixed and floating payment frequencies. For a more detailed description, *see* **LIBOR Rate**.

# **Libor Futures**

A Libor futures contract (*see* **Eurodollar Futures and Options**) pays, at its settlement, a proportion of the Libor rate fixed on the futures expiry date. However, since an FRA makes its payment only at its maturity date, its par rate in a risk-neutral world is equal to the expectation under the discount-adjusted measure to that maturity date. The daily updating of posted margins for Libor futures means that profit or loss from rate fluctuations is realized immediately; thus the par futures price reflects the risk-neutral expectation in an undiscounted measure.

Because the resulting "futures convexity adjustment" does not closely track other measures of volatility, it is traded actively only by a few specialists. For most purposes, we can think of a future as being equivalent to an FRA plus an exogenously specified spread.

# **Yield Curve Construction**

Since the function *P (T )*, or equivalently *f (T )*, practically determines the value of these Liborbased instruments, we price less-liquid instruments by fitting a *yield curve*—any object from which *P* and *f* can be computed—to the observed values of the most liquid *build instruments*. Since there will not be above a few dozen such instruments, this fitting problem is severely underconstrained.

One common method is *bootstrapping* of *zero yields*: we specify that the yield curve will be defined by linear interpolation on the zero-coupon bond yield *y(T )* ≡ − ln *P (T )/T* . This restricts the curve's degrees of freedom to one per interpolation point. If we place one interpolation point at the last maturity date (the latest payment or rate end date) of each build instrument, we can solve for each corresponding value of *y* with a succession of one-dimensional root searches.

Since *f (T )* = *y(T )* + *T y*-*(T )*, the forward curve thus constructed is gratuitously discontinuous and contains large-scale interpolation artifacts. We do not wish to recommend this construction method or to disparage others, but only wish to note its frequent use and to show a concrete example. For a more complete discussion, *see* **Yield Curve Construction**.

# **Hedging on the Yield Curve**

Once a yield curve is built, it can be used to price similar trades that are not among the build instruments, such as forward-starting or nonstandard swaps. Such pricing depends on two implicit assumptions: that the yield curve is the underlying of these trades as well as of its build instruments, and that its interpolation methods (or other nonmarket constraints) are sufficiently accurate. In practice, the former is widely accepted for Libor-based products, while the latter is a major arena of competition among market makers.

Any trade priced on the yield curve will have a *forward rate risk*, which we denote by *δf (T )*, so that its change in value for a small curve fluctuation *<sup>f</sup>* is equal to the change in  $\delta_f^{\wedge} \Delta f \equiv \int_0^{\infty} \delta_f(u) \Delta_f(u) \, du$ . Formally, we write

$$\delta_f(t) \equiv \lim_{h \to 0, \epsilon \to 0} \frac{U(f + h\eta_{t,\epsilon}) - U(f)}{h\epsilon} \qquad (1)$$

where

- $U(f)$  is the trade's value for a given yield curve described by the forward rates  $f$ ;
- $\n\eta(z)\n$  is a  $\mathcal{C}^{\infty}$  test function with support in [0, 1] and  $\int_0^1 \eta = 1$ ; and<br> $\eta_{t,\epsilon}(z) \equiv \eta((z-t)/\epsilon)$ .

For the *linear* trades, that we have so far discussed,  $\delta_f$  will change very little as f changes. A portfolio of trades with no net  $\delta_f$  has, at least for that moment, no interest rate risk.

Figure 1 shows the forward rate risk for a swap. The large-scale behavior is unsurprising; the forward rate risk steadily decreases as coupons are paid. The small-scale spikes are caused by overlapping, or in one case underlapping, of the start and end dates for the Libor rates on the floating side. The vertical scale is, of course, proportional to the swap notional amount, and is not shown here.

In practice, especially when trades cannot be exactly represented by equivalent cash flows, we will not know  $\delta_f$  exactly but we will have rather a numerically computed (e.g., piecewise constant) approximation thereto; but since we can control the *buckets*, that is, the intervals over which  $\delta_f$  is kept constant, this is not a major difficulty.

#### **Response Functions**

However, we cannot execute a hedge of the forward rate risk directly; instead, we must choose a set of hedge instruments that will allow us to offset it. Often, these hedge instruments are exactly the build instruments. Each hedge instrument will also, of course, have a forward rate sensitivity. In practice, we generally consider the sensitivity, not of the instrument value, but of the implied par rate (or just *implied rate*): The implied FRA rate for futures, par coupon for swaps, or yield for bonds implied by the vield curve.

In this case, we can compute a hedge by slightly bumping each instrument's implied rate  $r_i$ , rebuilding the curve, repricing the trade being hedged, and measuring its price change. This method has the advantage of enabling very precise p/l explanation, at the cost of requiring repeated yield curve builds.

The resulting instrument sensitivity is closely related to the forward rate risk. To be precise, let the *response function*  $\beta_i(T) \equiv dF(T)/dr_i$ . Then, the instrument sensitivity is exactly  $\beta_i^{\wedge} \delta_f$ . Thus, response functions provide an ideal tool for examining curve build methods.

![](_page_1_Figure_15.jpeg)

**Figure 1** Forward rate risk for a (Payer) swap

![](_page_2_Figure_1.jpeg)

**Figure 2** Response of  $F$  to fourth future and to 4-year swap

The response functions for two typical build instruments are displayed in Figure 2, for two different curve build methods. The response to a futures rate, shown against the left-hand scale, changes the forwards within the futures period and decreases them in the interval from the last future to the first swap (so that all other build instruments will have unchanged rates); naturally, within the futures period,  $dF(T)/dt_i \simeq 1$ . The response to a swap rate, which is substantially larger, is shown against the right-hand scale. In both cases, the bootstrapped curve shows the "sawteeth" characteristic of linear interpolation on  $y$ , while the smooth curve shows the inevitable loss of locality. This tension between smoothness and locality arises because a smooth curve, by its very nature, must alter values far from the source of a change in order to preserve smoothness; for details see **Yield Curve Construction.** 

#### **Bucket Delta Methods**

Another common hedge method is to set the bucket end dates to the maturities of the curve build instruments, and then compute the bucket deltas: sensitivities  $\delta_k$  to the forward rate in the kth bucket, computed by applying a parallel shift to those forward rates. We can also define a Jacobian matrix  $J$  such that  $J_{ik}$  is the sensitivity of the  $i$ th instrument's implied rate to the forward rate in the  $k$ th bucket; then the instrument sensitivities are given by  $J^{-1}\vec{\delta}$ . This is known as the *inverse* method.

A hedge can also be constructed from  $\vec{\delta}$  by minimizing the  $p/l$  variance of the hedge trade plus a portfolio of hedging instruments; for this we need an estimate of the covariance  $\Sigma(T_k, T_m)$  between the forward rates  $f(T_k)$  and  $f(T_m)$ . The variance is then a quadratic form in the hedge instrument notionals, which can easily be minimized. Any other quadratic form, such as a penalty function based on the hedge notionals, can be included without difficulty.

# **Nonlinear Products**

For any product, the sensitivity  $\delta_f$  is defined in each yield curve state; however, it need not be independent of that state. This nonlinearity is most pronounced for options, especially when they are short-dated and nearly at-the-money. In this case, to lock in an option value by hedging we must dynamically rebalance the hedging instruments, subject to the well-known limitations of payoff replication strategies.

One issue of particular importance is that the local hedge, based on  $\delta_t$  in the current state of the yield curve, can differ greatly from the varianceminimizing hedge if the rebalancing frequency is finite or if jumps are present. This occurs when the distribution of possible curve shifts is strongly asymmetric, or more frequently when the second derivative of the payoff is highly state-dependent.

These issues are not unique to interest rates, but they can become more pronounced for some payoffs owing to the tendency of short rates to move in discrete increments (e.g., in response to a central bank action). Nonlinearity is also important to the pricing and hedging of very long-dated swaps and bonds.

#### **Projected Gamma**

The second-order "gamma" risk is formally described by an extension of the first-order forward rate risk that we have just discussed; in fact, there is a power series

$$U(f) = U(f_0) + \delta_f^{\wedge} \Delta_f$$
  
+  $\frac{1}{2} \int \int \gamma_f(u, v) \Delta(u) \Delta(v) du dv + \dots$   
(2)

where  $\Delta_f(t) \equiv f(t) - f_0(t)$  and  $\delta_f$ ,  $\gamma_f$ , and so on, are computed at  $f = f_0$ . However, extracting this  $\gamma_f$  in all its detail is prohibitively time-consuming. Instead, we compute the f-dependence of  $\delta_f$ , which is the same to this order (and is, in fact, the more relevant measure), by computing the delta hedge in various interest rate scenarios.

These scenarios are generally constructed by parallel shifts to the market yield curve. There are several reasons for this:

- Only parallel-shift gamma can realistically be hedged (by trading short-dated options).
- Large unexpected moves in rates, necessitating delta rehedging, tend to be roughly parallel.
- The parallel shift is uniquely easy to define and to explain.

The industry standard is to create a progression of scenarios using parallel shifts, which are multiples of 10 basis points, for example, from  $-50$  to  $+50$  in steps of 10. This aids visualization of higher- order contributions to the hedge, which can sometimes be traced to their source; for example, a sudden change in delta indicates an upcoming option expiry or barrier test in that interval.

# **Vega Hedging**

The volatility sensitivity, or "vega", of an interest rate derivative is characterized by both the time during which its optionality is active, and the time covered by the underlying rate. In other words, nonlinear interest rate derivatives are sensitive to the Heath–Jarrow–Morton  $(HJM)^b$  forward volatility  $\sigma(t, T)$ , the volatility at time t of  $f(T)$ . This does not mean that we must use an HJM model: any interest rate model defines an expected forward volatility.

A given trade, then, has a "forward volatility footprint"  $v(t, T)$  so that its change in value, to first order in volatility, equals the change in  $\int v(t,T)\sigma(t,T) dt dT$ . In more sophisticated models, this change is computed with other parameters (e.g., correlations, elasticity of rates, or volatility of volatility) held fixed. Thus,  $v(t, T)$  is precisely analogous to the forward rate sensitivity  $\delta_f(T)$ .

In addition, any mechanistic calibration technique has a response function

$$B_j(t,T) \equiv \frac{\partial \sigma(t,T)}{\partial \sigma_j} \tag{3}$$

where  $\sigma_i$  is the quoted volatility of the *j*th calibration instrument and partial derivatives are taken with other calibration instruments fixed. The inner product  $\int \int v(t,T)B_i(t,T) dt dT$  is thus the *calibration* instrument vega, which will be computed by bumping, recalibrating, and repricing ("bump-and-grind"). It is worth noting that examination of response functions is by far the best test of the quality of a calibration technique.

Models with few state variables harshly restrict the form of  $\sigma(t, T)$ ; for example, in one-state-variable models we have  $\sigma(t,T) = g(t)H(T)$ .<sup>c</sup> This impacts vega hedging in two main ways. First, the forward vol footprint simply cannot be measured using such a model, since it is the sensitivity to a perturbation which the model cannot reproduce. Second, the response functions must reflect the constraints on  $\sigma(t, T)$ ; thus, they are inevitably nonlocal and often highly unnatural. Such models can be used for vega hedging in restricted environments, such as when the maturity of the hedging instruments is already known; but, in general, they are incapable of "finding" the vega hedge, owing to their intrinsic inability to localize perturbations.

# **Cost of Funding Complications**

So far, we have assumed that the market Libor rate reflects our own cost of funds; this assumption is necessary for a single zero curve to exist. In practice, many market participants consistently fund their operations above or below Libor; thus they must maintain a zero curve *Zc* for their own cashflows, and a different curve *Zr* for rate forecasts. To a very good approximation, this effect can be encapsulated by specifying the *funding adjustment Zc(T )/Zr(T )*.

This is most important in markets where the demand for currencies is highly asymmetric, particularly in Japanese Yen (*JPY*). The steady demand of JPY-based issuers for dollars means that foreign dealers can fund their JPY debts more cheaply, effectively increasing their own *Zc*—this effect drives the currency basis swaps market.

The presence of funding adjustments causes different dealers, observing the same market swap rates, to deduce different forward curves. The effect is always to create an incentive for the party with the higher cost of funds to take the side with initial positive cash flows, thus borrowing a fraction of the swap notional. To minimize this effect, most market quotes are for mutually collateralized swaps.

# **Cost of Tenor Complications**

The frequency of Libor fixings also influences the par rate for a swap; the curve *Zr*, which forecasts 3-month Libor will not forecast 1-month or 6-month Libor. In practice, the forward rates are higher for longer- tenor Libor rates; this is generally, attributed to credit issues, since a longer tenor entails a greater risk of a downgrade during the loan period.

This can be addressed by constructing separate curves for each tenor, or by adjusting Libor rate forecasts by some *ad hoc* tenor-dependent correction. The floating-for-floating swaps at mismatched tenors, in which these corrections can be traded, are also called *basis swaps*.

# **Collateral and Repo Complications**

For some markets, notably US Treasury bonds, the value of a bond is not fully captured by the value of its cashflows. The complex repo market for these bonds makes some *special* bonds valuable as collateral, giving them a positive convenience yield and raising their price above that predicted from the zero curve. Such markets are usually treated by building a *general collateral* curve based on bonds with no such added value, and then relating the premium in some bond's price to its expected repo rates. A derivative whose underlying is a special bond is thus exposed to both general collateral rates and the bond's forecast repo rates. For short-expiry trades, this combination of exposures is accurately expressed as an exposure to the special bond's price, but longdated trades require separate consideration of the two curves.

# **End Notes**

a*.* Even this simple contract is fraught with credit and collateral issues, which our notation conceals. Most of these are beyond the scope of this discussion.

b*.* For details of the HJM approach, *see* Bjork **Heath–Jarrow–Morton Approach**.

c*.* Here *σ (t, T )* need not be the normal HJM volatility; in Black–Karasinski models, for example, it is the volatility of the log forward rate in the risk-neutral measure which is separable.

# **Further Reading**

- Romanelli, P. (1997). The yield curve: from the ground up, Bankers Trust Topics in Derivatives Analytics 2.
- Hagan, P. & West, G. (2006). Interpolation methods for yield curve construction, *Applied Mathematical Finance* **3**(2), 89–129.
- Heath, D., Jarrow, R. & Morton, A. (1989). *Bond pricing and the term structure of interest rates: a new methodology*, Cornell University, working paper.
- Pennacchi, G., Ritchken, P. & Sankarasubramanian, L. (1996). On pricing kernels and finite state-variable Heath, Jarrow, Morton models, *Review of Derivatives Research* **1**, 87–99.

# **Related Articles**

**Delta Hedging**; **Gamma Hedging**; **Hedging**; **Mean–Variance Hedging**; **Yield Curve Construction**.

TOM HYER
# **Corridor Options**

Occupation time derivatives are debt securities that came into existence in 1993 and have attracted some attention from investors and researchers. A defining characteristic of these contracts is a payoff that depends on the time spent by the underlying asset in some predetermined region. Typical specifications consist in interest payments that are proportional to the time in which a reference index rate (most commonly the Libor rate) lies inside a given range. In return for the drawback that no interest will be paid for the time the corridor is left, they offer higher rates than comparable standard products, like floating rate notes. Various claims with features of this type have been studied and have been popularized with different names such as corridor bond or option, range note, range floater, range accrual note, LIBOR range note, fairway bond,<sup>a</sup> and hamster option.<sup>b</sup> The most common underlyings are stock indices, foreign currencies, and interest rates, such as LIBOR or swap rates. Also spread range notes are common. Range notes pay a coupon proportional to the number of days in which the difference between two interest rates (e.g., 10-year swap rate *versus* 30-year swap rate) is positive. Thus while the value of an interest range note depends on the volatility of the level of the term structure, the value of a range note depends on the volatility of the slope of the term structure. This makes it important to model the correlation of interest rates with different maturities accurately.

One of the most popular structures is the accrual note, typically of one- or two-year maturity, which offers a coupon calculated by the number of days in which three-month dollar Libor, for example, falls inside a predefined range. On these days, the note will typically offer a preassigned spread over the relevant treasury bond. When Libor is outside the range, the payout is zero. The note effectively provides a way for investors to sell volatility, but the binary structure protects them from the unlimited downside that would accompany similar strategies, such as writing a floor and cap on the range. Corridor products offer investors enhanced yield if they have a strong view that rates will stay within a range, and often they are structured to reflect an investor's view that is contrary to a particular forward-rate curve. In its simplest form, the payoff of the corridor bond can be seen as the sum of the payoffs of digital options expiring on successive days.

## Payoff

Let  $t$  be the current time (measured in years) and let  $0 = T_0 < t < T_1, \ldots, T_i, \ldots, T_n$  be the payment dates of the coupons  $\phi(T_i)$  ( $T_0$  is the last date at which a payment occurred). Let  $D(T_i, T_{i+1})$  be the number of days in the coupon period and let  $T_{j,i}$  be the date corresponding to *i* days after date  $T_j$ , that is,  $T_{i,i} = T_i + i/365, i = 1, \ldots, D(T_i, T_{i+1})$ . Let  $x_i$ and  $x_u$  be the lower and upper bound of the range (the prespecified range for each observed date can vary daily or across different compounding periods). Finally let  $X(t)$  be the value of the reference index at time  $t$ . Sometimes,  $X$  represents a stock index or a foreign currency rate, and sometimes is taken to be a LIBOR rate of a preassigned tenor (in this case  $X(t) = L(t, t + \theta)$ , where L is the LIBOR rate and  $\theta$  is its tenor) or the spread of two swap rates with different maturities.

The range note can have a fixed and a floating version. For a range note, the value of the coupon paid at time  $T_{i+1}$  is equal to

$$\phi(T_{j+1}) = C_{j+1} \times \frac{H(T_j, T_{j+1})}{D(T_j, T_{j+1})} \tag{1}$$

where  $C_{i+1}$  represents the annual coupon rate for the  $(j + 1)$ th compounding period and is given by

$$C_{j+1} = \begin{cases} C & \text{fixed range note,} \\ X(T_j) + \Delta & \text{delayed floating} \\ \text{range note,} \end{cases}$$
 (2)

where C is a constant and  $\Delta$  is the spread to be added to the reference rate, and

$$H(T_j, T_{j+1}) = \sum_{i=1}^{D(T_j, T_{j+1})} 1_{[x_l, x_u]} (X(T_{j,i})) \qquad (3)$$

where  $1_A(x)$  is the indicator function of the set A, that is,  $1_A(x) = 1$  if  $x \in A$ , otherwise  $1_A(x) = 0$ . Here the term *delayed* refers to the fact that the option maturity (or reset date)  $T_i$  anticipates the payment date  $T_{j+1}$ . Sometimes, instead of having the delayed floating range note we have the in-arrears floating range note where the coupon is set equal to

$$C_{j+1} = X\left(T_{j+1}\right) + \Delta \tag{4}$$

that is, the coupon payment depends on the level of the reference rate at the current coupon payment date (maturity and payment date coincide).

Sometimes, a minimum coupon clause is also included, so that the coupon amounts to

$$\phi(T_{j+1}) = \max\left(C_{j+1} \times \frac{H(T_j, T_{j+1})}{D(T_j, T_{j+1})}, K\right) \quad (5)$$

The standard contract is the fixed rate range note if the underlying is a stock index or a foreign currency and the delayed floating range note if the underlying is a LIBOR rate.

#### Pricing

In this section, we discuss the pricing problem of the corridor contracts described earlier.

#### Underlying is a Stock Index

In this case, we model the underlying according to the Geometric Brownian Motion (GBM) model, that is,

$$dX(t) = (r - q)X(t) dt + \sigma X(t) dW(t), X(t) = x$$
(6)

where

- $r$ : instantaneous risk-free rate,
- $q$ : instantaneous dividend yield,
- $\sigma$ : percentage volatility,
- $x$ : initial underlying price.

An analytical formula for pricing fixed range notes is promptly available, resorting to the fact that

$$\begin{split} &\mathbb{E}_{t} \left(1_{\left[x_{l}, x_{u}\right]} \left(X\left(T\right)\right)\right) \\ &= \mathbb{E}_{t} \left(1_{\left(-\infty, x_{u}\right]} \left(X\left(T\right)\right) - 1_{\left(-\infty, x_{l}\right]} \left(X\left(T\right)\right)\right) \\ &= \mathcal{N}\left(d_{T-t}^{x_{u}}\right) - \mathcal{N}\left(d_{T-t}^{x_{l}}\right) \end{split}$$

where

$$d_{T-t}^{w} = \frac{\ln \frac{x}{w} + (r-q)(T-t) - \frac{1}{2}\sigma^{2}(T-t)}{\sqrt{\sigma^{2}(T-t)}}$$
$$\mathcal{N}(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{\frac{-u^{2}}{2}} du \tag{7}$$

Therefore, for a fixed-rate range note, we have

$$\mathbb{E}_{t}\left(\phi\left(T_{j+1}\right)\right)$$

$$=\frac{C_{j}}{D\left(T_{j},T_{j+1}\right)}\sum_{i=1}^{D\left(T_{j},T_{j+1}\right)}\left(\mathcal{N}\left(d_{T_{j,i}-t}^{x_{0}}\right)-\mathcal{N}\left(d_{T_{j,i}-t}^{x_{l}}\right)\right)$$

$$(8)$$

and the price of the fixed range note is

$$\sum_{j=0}^{n} P\left(t, T_{j+1}\right) \mathbb{E}_{t}\left(\phi\left(T_{j+1}\right)\right) + P\left(t, T_{n}\right) \quad (9)$$

where  $P(t, T)$  refers to the price of a zero-coupon bond expiring in  $T$ .

From a pricing perspective, the case of the fixed range note with a minimum coupon provision appears more interesting. Indeed, in this case, the pricing formula requires the distribution of the occupation time of the range  $[x_l, x_u]$ . If the random variable  $H(T_i, T_{i+1})/D(T_i, T_{i+1})$  in equation (3) is replaced by its continuously monitored version

$$h(T_{j}, T_{j+1}; x_{l}, x_{u}) = \int_{T_{j}}^{T_{j+1}} 1_{[x_{l}, x_{u}]} (X(s)) ds \quad (10)$$

few analytical results are available. In particular, the distribution of  $h(T_i, T_{i+1}; x_l, x_u)$  when  $x_l =$  $-\infty$  (or  $x_u = \infty$ ) is obtained in [1], exploiting the Feynman-Kac formula. Related results are presented in [4, 5, 7, 10, 12, 16, 17]. Owing to the stationarity of the Brownian motion, we observe that the distribution of  $h(T_i, T_{i+1})$  is the same as the distribution of  $h(0, T_{i+1} - T_i; x_l, x_u)$ , and this law (when  $x_l =$  $-\infty$ ) is strictly related to the law of the occupation time in the time interval  $[0,\tau]$  as

$$Y_{0,x}(u,\tau) = \int_0^{\tau} \mathbf{1}_{(-\infty,u]} (\delta s + W(s)) \, \mathrm{d}s, \, W(0) = x \tag{11}$$

where  $\delta = (r - q - \sigma^2/2) / \sigma$ . Fusai [8] provides the pricing formula in the case of finite values of  $x_l$  and  $x_u$ , obtaining the Laplace transform in time of the characteristic function of  $Y_{0,x}(u,\tau)$ .

The real-life case of discrete monitoring is discussed in [9] using Monte Carlo simulation and finite difference methods. In particular, the authors stress that the price of the contract with continuous time monitoring is the highest (lowest) when the index is inside (outside) the band. This is due to the nature of the contract: if the index is inside the band, and we assume continuous time monitoring, then the passage of time will increase the value of the contract until the moment in which the index crosses the barriers. Instead, if we assume discrete time monitoring, we cannot exploit the passage of time completely: we register the position of the index only at discrete dates and if they are quite distant (e.g., a month), it is possible that the index at the reset date will move outside the band and so the occupation time does not increase. In this case, the time between two monitoring dates is entirely lost. Vice versa, in the discrete case, if we are outside the band, and between two monitoring dates the index moves inside the band, then the occupation time increases by the entire time distance between monitoring dates. Instead, with continuous time monitoring we miss every instant before the process crosses the barrier. So the continuous time formula will overvalue (undervalue) the discrete time formula when the index is inside (outside) the band.

We have not discussed here the pricing of the floating range notes with a stock index as underlying because they are not very common. However, using the stock as numéraire and the tower property (to take into account the delay between maturity date and payment date) analytical formula are promptly available. In the case of a minimum coupon, we need the joint law of Brownian motion and its occupation times. Useful formulas for this case are provided in [2, 10, 12].

#### Underlying is an Interest Rate

In this case, the underlying variable  $X(t)$  of the range note is a simple compounded interest rate with tenor  $\theta$  defined according to the formula

$$1 + X(t)\theta = \frac{1}{P(t, t + \theta)}$$
(12)

The pricing of range notes, with the underlying being an interest rate, has begun with Turnbull [18], who assumes that the interest rate dynamics is well represented by a one factor Gaussian Heath-Jarrow-Morton (HJM) model, that is, the dynamics of the price of a zero-coupon bond  $P(t, T)$  is given by

$$\frac{\mathrm{d}P\left(t,T\right)}{P\left(t,T\right)} = r\left(t\right)\,\mathrm{d}t + \sigma\left(t,T\right)\,\mathrm{d}W\left(t\right) \tag{13}$$

where  $\sigma(t, T)$  is deterministic.

In particular, Turnbull [18] considers the Ho and Lee model  $(\sigma(t, T) = \sigma$ , constant) and the Hull and White model  $(\sigma(t, T) = \sigma e^{-\lambda(T-t)}, \lambda > 0)$  and obtains a closed form formula for the range note (fixed rate and delayed floating case). A simpler and more intuitive derivation than [18] and for a more general volatility function (albeit still deterministic) is obtained, using the change of numéraire technique, in [14].

The multifactor Gaussian HIM

$$\frac{\mathrm{d}P\left(t,T\right)}{P\left(t,T\right)} = r\left(t\right)P\left(t,T\right)\,\mathrm{d}t + \sigma\left(t,T\right)' \cdot \mathrm{d}W\left(t\right) \tag{14}$$

where  $\cdot$  denotes the inner product in  $R^n$  and  $W(t) \in R^n$  is an *n*-dimensional standard Brownian motion as considered in [15]. Such extension is important because it enhances the term structure model calibration to the interest rates covariance matrix "observed" in the market, which, along with the term structure of interest rates, will ultimately determine the price of the range notes under analysis. In fact, in order to price and hedge range notes consistently with the market prices of related plainvanilla interest rate options (such as caps and/or European swaptions), it is essential to use an interest rate model that is analytically tractable and that provides a good fit to the term structures of interest rates, volatilities, and correlations observed in the market.

Reference [6] further extends these results to a multivariate Lévy term structure model, an extension of a Gaussian HJM model with jump processes.

The main limit of these models is that the rate  $X(t)$  can attain negative values with positive probability, which may cause some pricing error in many cases.

An extension to the class of affine term structure model, which encompasses both Gaussian and non-Gaussian models such as Cox-Ingersol-Ross (CIR) square-root models is introduced in [11]. The extension is useful in ensuring the positivity of the interest rate; moreover, Jangy and Yoon [11] have also consider the pricing spread range notes. The limit of their analysis is that they consider as underlying asset a continuously compounded interest rate of a given tenor rather than the corresponding simple compounded interest rate. On one hand, this allows to get (i) analytical formulas for a more general class of multifactor models and (ii) positive interest rates. On the other hand, the pricing formulas are not immediately adaptable to real-life contracts because the spread is usually between swap rates of different tenors.

A Libor Market Model is instead adopted in [19]. This has the advantage of enhancing the model calibration to the interest rate covariance matrix observed in the market, and, in addition, it guarantees the positivity of interest rates. However, in this model no analytical formulas are available for floating range notes, which need to be priced by Monte Carlo simulation. However, freezing the drift of forward rates in order to have a dynamics of the LIBOR rate with deterministic drift and volatility, Wu and Chen [19] are able to provide approximate pricing formulae.

Finally, we remark that, with an interest rate as underlying, no pricing formula has so far been made available in the literature concerning the pricing of a range note with a minimum coupon provision.

## **Related Payoff**

Exotic options related to corridor options are quantile options, introduced in [13], and studied in more detail in [1, 4]. Step options studied in [12] are contracts related to range notes, as an alternative to standard barrier options. Barrier options have the drawback of losing all value at the first touch of the barrier. Step options lose value more gradually. The option value decreases as the underlying asset spends more time at lower levels. Another example is the Parisian option (*see* **Constant Maturity Swap**). A Parisian out option with window *D*, barrier *L*, and maturity date *T* will lose all value if the underlying price has an excursion of duration *D* above or below the barrier *L* during the option's life. If the loss of value is prompted by an excursion above (below) the barrier, the option is said to be an up-and-out (downand-out) Parisian option. Parisian contractual forms were introduced and studied by Chesney *et al.* [3]. Contracts of this type are more robust to eventual price manipulations. The pricing formulas in [3, 12] involve inverse Laplace transforms.

## **End Notes**

a*.* The fairway in golf is like the index or interest rate range. The outlook is positive if the ball lands on the fairway. If, however, a ball lands in the rough, the outlook is negative. Source: http://www.investopedia.com/terms/f/fairwaybond. asp as of January 2009.

b*.* The German noun hamster has the same meaning as the English noun hamster: it is the name of a small rodent. But HAMSTER is also an acronym standing for Hoffnung Auf MarktSTabilitaet in Einer Range (literally: Hope on market stability in a given range). It really is a pun as in German the verb 'hamstern' has the meaning of 'to hoard'. HAMSTER options hoard the fixed amount one gets for each day; the underlying stays in the prespecified range. What is earned cannot be lost any more. Source http://www.margrabe.com/Dictionary/DictionaryGJ.html # sectH as January 2009.

## **References**

- [1] Akahori, J. (1995). Some formulae for a new type of path-dependent options, *Annals of Applied Probability* **5**, 383–388.
- [2] Borodin, A.N. & Salminen, P. (1996). *Handbook of Brownian Motion - Facts and Formulae*, Birkhauser.
- [3] Chesney, M., Jeanblanc-Picque, M. & Yor, M. (1997). ´ Brownian excursions and Parisian barrier options Brownian excursions and Parisian barrier options, *Advances in Applied Probability* **29**(1), 165–184.
- [4] Dassios, A. (1995). The distribution of the quantile of a Brownian motion with drift and the pricing of related path-dependent options, *Annals of Applied Probability* **4**(2), 719–740.
- [5] Douady, R. (1999). Closed form formulas for exotic options and their lifetime distribution, *International Journal of Theoretical and Applied Finance* **2**(1), 17–42.
- [6] Eberlein, E. & Kluge, W. (2006). Valuation of floating range notes in levy term-structure models, ´ *Mathematical Finance* **16**(2), 237–254.
- [7] Embrechts, P., Rogers, L.C.G. & Yor, M. (1995). A proof of Dassios' representation of the *α*-quantile of Brownian motion with drift, *Annals of Applied Probability* **5**(3), 757–767.
- [8] Fusai, G. (2000). Corridor options and Arc-Sine law, *Annals of Applied Probability* **10**(2), 634–663.
- [9] Fusai, G. & Tagliani, A. (2001). Pricing of occupation time derivatives: continuous and discrete monitoring, *Journal of Computational Finance* **5**(1), 1–37.
- [10] Hugonnier, J. (1999). The Feynman-Kac formula and pricing occupation time derivatives, *International Journal of Theoretical and Applied Finance* **2**(2), 153–178.
- [11] Jangy, B.G. & Hee Yoon, J. (2008). *Valuation of Range Notes Under Affine Term Structure Models*, http://ssrn.com/abstract=1291703.

- [12] Linetsky, V. (1999). Step options: The Feynman-Kac approach to occupation time derivatives, *Mathematical Finance* **9**, 55–96.
- [13] Miura, R. (1992). A note on lookback options based on order statistics, *Hitotsubashi Journal of Commerce and Management* **27**, 15–28.
- [14] Navatte, P. & Quittard-Pinon, F. (1999). The valuation of interest rate digital options and range notes revisited, *European Financial Management* **5**(3), 425–440.
- [15] Nunes, J.P.V. (2004). Multi-factor valuation of floating range notes, *Mathematical Finance* **14**(1), 79–97.
- [16] Pechtl, A. (1995). Classified information, in *Over the Rainbow*, J. Robert, ed, Risk Publications, pp. 71–74.
- [17] Takacs, L. (1996). On a generalization of the arc-sine ` law, *Annals of Applied Probability* **6**(3), 1035–1040.
- [18] Turnbull, S.M. (1995). Interest rate digital options and range notes, *Journal of Derivatives* **3**, 92–101.

[19] Wu, T.P. & Chen, S.N. (2008). Valuation of floating range notes in a LIBOR market model, *Journal of Futures Markets* **28**(7), 697–710.

## **Further Reading**

Tucker, A.L. & Wei, J.Z. (1997). The latest range, *Advances in Futures and Options Research* **9**, 287–296.

## **Related Articles**

**Barrier Options**; **Corridor Variance Swap**; **Discretely Monitored Options**; **Parisian Option**.

GIANLUCA FUSAI
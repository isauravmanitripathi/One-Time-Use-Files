# **Autocall**

An equity-linked autocallable note, or autocall, is a legal instrument in which the notional engaged by the customer is automatically reimbursed when the underlying stock reaches a strike at a specified recalling date or at maturity if such an event does not occur (when the recall appends a coupon is also paid to give the client a return on his/her capital higher than the one he/she would get from an investment in a bond). Equity-linked autocallable notes are examples of hybrid products in the sense that the equity and interest rate movements need to be jointly modeled.

## **Product Description**

A note is a legal wrapper issued by a financial institution. Usually, the capital engaged by the client is guaranteed at maturity and the note also delivers the payoff of a derivative instrument. If *T*<sup>0</sup> is the issue date, *T* the maturity, and *B(T*0*,T)*, the discount factor between *T*<sup>0</sup> and *T* , at *T*0, one unit of the capital guaranteed at maturity is worth *B(T*0*,T)* (if we do not consider the credit risk associated to the issuer). Hence, for an issue at par, the price of the derivative product should be 1 − *B(T*0*,T)* (called by practitioner *the available*). Thus, a fixed maturity note can be constructed with any type of payoff as long as the price of the derivative product matches the available.

When buying a note, the goal of the investor is to have a return on his/her capital that is higher than the riskless interest rate one, if the market ends at maturity in his/her expected configuration. However, the problem the client faces with fixed maturity notes is that his/her capital is blocked up until maturity. Autocallable notes solve that issue. The terms of a typical equity-linked autocallable note are listed below:

- At *T*0, the client invests 100.
- The product maturity is *T* and we consider *Ti*, 1 ≤ *i* ≤ *N* the autocallable dates with *T*<sup>0</sup> *< T*<sup>1</sup> *<* ··· *< Ti <* ··· *< TN* = *T* .
- If *S* is the underlying (a stock or an index), *Ki*, 1 ≤ *i* ≤ *N* a set of strikes, *Ci*, 1 ≤ *i* ≤ *N* a set of coupon, the payoff is as follows:

- Ž at *Ti*, 1 ≤ *i<N*, if the note has not been recalled at a previous autocallable date and if *STi* ≥ *Ki*, then the note is terminated ("automatically recalled" in the terminology) and the client receives 100 + *Ci* and,
- Ž at *T* , if the note has not been recalled at a previous autocallable date and if *STN* ≥ *KN* , the client receives 100 + *CN* ; otherwise, he receives 100.

Usually, the autocallable dates have a fixed frequency, the strikes are equal, and the coupons have a linear progression: *Ci* = *iC* with *C* that is higher than the riskless interest rate on the interval *T* = *Ti*<sup>+</sup><sup>1</sup> − *Ti*, 0 ≤ *i<N*. Thus, in a bullish market, the investor can have a higher return on his/her capital than the interest rate one and his/her capital is available as soon as his/her target is reached. This explains why autocallable notes are very popular in the equity markets and have been massively traded in the past years.

# **Adapted Equity Rate Modeling**

Compared to fixed maturity note, the modeling challenge with autocallable notes is the uncertain maturity of the product. With fixed maturity notes, the natural way of hedging the guaranteed capital is to trade a LIBOR-linked interest rate swap (*see* **LIBOR Rate**) from *T*<sup>0</sup> to *T* , where the seller of the note receives the fixed leg (the value of the LIBOR leg is 1 − *B(T*0*,T)* and offset the interest rate risk on the capital). With an autocallable note, we can trade the same swap but we need to be able to cancel the remaining part of it at any callable date *Ti* if *STi* ≥ *Ki*. In a deterministic interest rate framework, the hedge would be to wait for the callable date to trade the corresponding remaining swap. Obviously, because the evolution of the interest rates is also a risk factor, this is not acceptable. A joint model on the equity and on the interest rate is required.

Regarding the specific interest rate volatility risk, it is a first-order risk in a sense that an autocallable product is affected by the global level of the rate curve much more than it is by the shape of the distribution of forward start swaps or by the autocorrelation of the rate curve. In other words, a one-factor model on the rate curve is sufficient and a natural choice is an extended Vasicek model (*see* **Term** Structure Models) whose term structure of volatility has to be calibrated on the set of swaptions of maturity  $T_i$  written on the swap from  $T_i$  to T for all  $i, 1 \le i \le N$ , to be consistent with the autocallable note definition. This calibration set is a very classical one and is usually referred to as the *coterminal* calibration set (for the sum of the maturity of the swaptions and of the length of the corresponding swap is constantly equal to  $T - T_0$ ). Technically, this calibration can be done prior to the equity calibration as it is just associated to the dates of the contract (and possibly to its set of strikes if one wishes to chose swaption strikes not equal to the "at money" strike to integrate a part of the swaption smile risk).

Regarding the equity, we propose a simple representation using only a term structure of volatility to show the impact of the rate factor on the equity volatility. Specifically, we use a two-factor Brownian model, one factor for the interest rate and the other for the Equity. Moreover, we suppose that the Equity is not paying dividends (see **Dividend Modeling**) and that the repo rate (*see* **Swaps**) is null. Under the risk neutral measure  $O$ , this can be written as

$$\frac{\mathrm{d}B(t,T)}{B(t,T)} = r_t \,\mathrm{d}t + \Gamma(t,T) \,\mathrm{d}W_t^{\mathcal{Q},r} \qquad (1)$$

$$\frac{\mathrm{d}S_t}{S_t} = r_t \,\mathrm{d}t + \sigma_t^S \,\mathrm{d}W_t^{Q,S} \tag{2}$$

$$\mathrm{d}\left\langle W^{r},\,W^{S}\right\rangle_{t}=\rho\,\mathrm{d}t\tag{3}$$

The last equation does not depend on  $Q$  as change of measures affects neither the correlation between the Brownian motions nor their volatilities. Moreover, for the first equation, we suppose that the volatility  $\Gamma(t, T)$  has been calibrated according to the coterminal calibration set of the product. Since the equity is not paying fixed, discrete dividends, its forward  $F(t, T)$  is a martingale under the forward neutral measure  $Q_T$ , which is defined as

$$\frac{\mathrm{d}Q_T}{\mathrm{d}Q}(T) = \frac{\exp\left(-\int_{T_0}^T r_s \,\mathrm{d}s\right)}{B(T_0, T)}\tag{4}$$

The expression of the forward, in that case, is  $F(t, T) = S_t/B(t, T)$ ; hence, we have

$$\frac{\mathrm{d}F(t,T)}{F(t,T)} = \sigma^{S}(t,T) \,\mathrm{d}W_{t}^{Q_{T},S} \tag{5}$$

and also, by combining equations  $(1)$  and  $(2)$ 

$$\frac{\mathrm{d}F(t,T)}{F(t,T)} = \sigma_t^S \,\mathrm{d}W_t^{Q_T,S} - \Gamma(t,T) \,\mathrm{d}W_t^{Q_T,r} \tag{6}$$

Hence,

$$\int_{0}^{T} |\sigma^{S}(t, T)|^{2} dt = \int_{0}^{T} |\sigma_{t}^{S}|^{2} dt + \int_{0}^{T} |\Gamma(t, T)|^{2} dt$$
$$-2\rho \int_{0}^{T} |\sigma_{t}^{S}| |\Gamma(t, T)| dt \qquad (7)$$

Moreover, we have

$$E_{t}^{\mathcal{Q}}[B(t,T)(S_{T}-K)^{+}]$$
  
=  $E_{t}^{\mathcal{Q}}[B(t,T)(F(T,T)-K)^{+}]$   
=  $B(t,T)E_{t}^{\mathcal{Q}_{T}}[(F(T,T)-K)^{+}]$  (8)

which leads to the generalization of the Black and Scholes formula in the sense that, in a setting with stochastic interest rates, the implied volatility  $\Sigma_T$  of the Black and Scholes framework is given by

$$\Sigma_T = \sqrt{\frac{1}{T} \int_0^T |\sigma^S(t, T)|^2 dt}$$
 (9)

Thus, since the interest rate model has been calibrated independently to the equity model and supposing that the term structure of implied volatility is observed, it is possible to calibrate the term structure of the volatility of the stock,  $\sigma_t^S$ .

From the relation on the volatilities of this simple framework, it is important to note that, depending on the sign of the correlation of the rate factor with the equity factor and of the value of the volatility of the bond, the stock volatility can be either higher or lower than the implied volatility. This does not affect the probability of recalling the note at the first recalling date (which is not conditional) but the probability of recalling the note at a further recalling date conditionally of not having recalled the note at a prior recalling date. Furthermore, the addition of a rate factor, by extending the dimension of the model, leads to a Vega hedging of larger dimension since the swaptions used in the interest rate calibration set should now be considered as hedging instruments, and to a more complex Gamma hedging (see Gamma Hedging). In particular, for the latter, the "cross Gamma", the second derivative with respect to the spot of the equity and to the spot of the rate, cannot be hedged by any liquid instrument in the market. Therefore, it is necessary to adopt an approach by robustness, applying the same stochastic control arguments as for uncertain volatility models (*see* **Uncertain Volatility Model**), in order to control the evolution of the value of the hedged portfolio including the autocallable note. Practically, this can be done by replacing the instantaneous correlation between the two factors by an estimation of its upper bound as the cross Gamma, in the case of the autocallable note, is positive.

## **Advanced Modeling**

While the equity/rate issue is truly the specificity of autocallable notes, two other specificities of the equity market need to be taken into consideration for such products, namely, the smile modeling and the dividends.

Regarding the smile issue, the difference between the price of an up binary option in the Black and Scholes framework with a fixed volatility and the price of the same up binary option in the presence of a smile is equal to the Vega of the call of same strike time the opposite of the local skew, *∂/∂K*, of the implied volatility (this result is a direct application of the fact that an up binary option is bounded by two call spreads). Hence, in the equity market, the presence of a skew increases the price of the up binary option. Applying this result to the autocallable note means that the probability of recalling the note at the closest recalling date is higher if the volatility skew is considered than it is in a setting like the one we proposed earlier and, as a consequence, the term structure of the rate sensitivity is affected. However, while the risk associated to the skew of volatility is therefore important to model, the calibration of a twofactor model including this risk is more complex than what we proposed in the previous part and requires the use of numerical tools such as PDE resolutions (*see* **Forward–Backward Stochastic Differential Equations (SDEs)**; **Partial Differential Equations**; **Finite Element Methods**). In particular, it is not possible to use the local volatility formula (*see* **Local Volatility Model**) as it is specific to a monofactor model.

The dividend risk is not so much of an issue in the case of the autocallable note defined in the section Product Description. However, it could become more important in structures where the customer chose to risk a loss on his capital by selling a Down and In Put in exchange of higher coupons in case of an early termination. Nevertheless, under the forward neutral measure *QT* , all assets of the form *xt/B(t, T )*, with *xt* a spot process, are martingales (we have used this result in the previous part where *St* is a spot process). Yet, with the addition of fixed discrete dividends, the forward of the equity is including discount factor terms from each dividend dates to the considered maturity. Hence, it is no longer a martingale and, in the presence of stochastic interest rates, the calibration of its volatility is more complex than what we have proposed earlier and also requires the use of advanced numerical tools because of the **Convexity Adjustments** due to the fixed dividends.

## **Extensions**

The payoff we have presented is the most basic one. To increase the value of the coupons, a common practice is to consider a basket of stocks as underlying and to condition the recall on the spot of the worst performer at each recalling date. While this does not change the analysis we have made, this extends the dimension of the problem and can require the integration of other sources of risk such as the equity correlation skew (*see* **Basket Options**). Moreover, if the stocks are not in the same economy, the number of rate factors also increases and, as explained in **Quanto Options**, quanto drift terms lead to more complex equations.

Another classical extension of the autocallable note is to condition the coupon on a rate instrument. Typically, upon recall, the coupon paid would be equal to a swap rate or a LIBOR rate plus a fixed spread. In that case, it is usually necessary to adapt the rate factor to have correct convexity adjustments (*see* **CMS Spread Products** for the explanation of the convexity adjustment for constant maturity swaps and **Bermudan Swaptions and Callable Libor Exotics** for correlated issues). Moreover, in that case, the impact of the joint equity/rate modeling on the price of the autocallable note is far more important than it is in the fixed coupons case.

There are a few more extensions of the autocallable note that have been proposed in the recent years, but the payoffs we have mentioned represent the vast majority of traded contracts. Yet, in all cases, the modeling challenge lies in the integration of stochastic interest rates in the equity framework, which defines autocallable notes as hybrid products.

CHARLES-HENRI ROUBINET
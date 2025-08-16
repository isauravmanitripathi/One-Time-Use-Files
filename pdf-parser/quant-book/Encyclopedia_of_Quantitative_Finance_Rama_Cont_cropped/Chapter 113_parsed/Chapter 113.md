## **Call Spread**

A call spread is an option strategy with limited upside and limited downside that uses call options of two different strikes but the same maturity on the same underlying. More details and pricing models can be found in [1]. Market considerations can be found in [3–5]. The call spread produces a structure that at maturity pays off only in scenarios where the price of the underlying is above the lower strike. One can think of this strategy as buying a low-strike call option and financing part of the upfront cost by selling a higher strike call option. The effect of selling the higher strike option is to limit the upside potential, but reduce the cost of the structure. It should be used for expressing a bullish view that the underlying will rise in price above the lower strike. As with all options, choosing the strike and maturity will depend on one's view of how much the underlying will move and how quickly it will move there. An example is shown, in detail, in Figure 1.

In the example shown in Figure 1, we look at a 790/810 call spread on the S&P 500 index, SPX. With the underlying SPX index at 770 and with three months to expiration, a 790 strike call price is 49.44 and an 810 strike call price is 41.79. The spread cost is 49*.*44 − 41*.*79 = 7*.*65. Thus, the cost for a call spread is significantly reduced from the outright cost of a call option with the same strike. This upfront cost for the call spread is the most one can lose in a call spread. We subtract this initial investment from all other valuations, as shown in Figure 1, to get a total value. On the other hand, if both options expire in the money, one will earn 20 = 810 − 790 on the call spread. Then the maximum profit is the spread minus the initial cost, or 20 − 7*.*65 = 12*.*35.

Note that with three months to expiration, the call spread value is fairly insensitive to the underlying price. However, as the option gets closer to expiration, the sensitivity of the price of the call spread becomes greater, especially in the range of the spread itself. This sensitivity to underlying price or delta (*see* **Delta Hedging**) is illustrated in Figure 2.

The delta of the call spread stays relatively flat until relatively close to expiration of the option. When the call spread is close to expiration, the delta is very unstable around the two strikes.

Another important consideration is the volatility implied by the market (*see* **Implied Volatility: Market Models**). When the strikes are out of the money, the call spread price increases when volatility increases because the probability of finishing in the money increases. On the other hand, when the strikes are in the money, the call spread price decreases when volatility increases because the probability of finishing out of the money increases. This is illustrated in Figure 3.

## **The Relationship with Digital Options and Skew**

The value of a European call spread structure can be written in terms of the difference of two call options. If we let *p(S)* denote the probability distribution of the underlying at the time of option expiry, then we have

$$Call Spread = e^{-r\tau} \int_{K_1}^{\infty} (S - K_1) p(S) dS - e^{-r\tau}$$
$$\times \int_{K_2}^{\infty} (S - K_2) p(S) dS \tag{1}$$

$$Call Spread = e^{-r\tau} \int_{K_2}^{\infty} (K_2 - K_1) p(S) dS + e^{-r\tau}$$
$$\times \int_{K_1}^{K_2} (S - K_1) \cdot p(S) dS \qquad (2)$$

If we now take the strikes very close to each other, the second term becomes insignificant. Next, if we lever up by 1*/(K*<sup>2</sup> − *K*1*)*, the payoff approximates the payoff of a digital option, which pays one if the underlying at termination is greater than the strike and zero otherwise. In this case,

$$Digital Option = e^{-r\tau} \int_{K}^{\infty} p(S) dS$$
$$= e^{-r\tau} (1 - \Phi(K)) \qquad (3)$$

where *-(K)* is the cumulative probability distribution at termination of the underlying. For the original paper, see [6]. Also see [2, 7, 8] for more details. We can state equation (3) in words as follows. The

![](_page_1_Figure_1.jpeg)

Figure 1 The value of a call spread at various times before expiration

![](_page_1_Figure_3.jpeg)

Figure 2 The delta of a call spread at various times before expiration

probability distribution function of the underlying at termination can be inferred from market prices as the derivative of digital options prices with respect to the strike. As these digital option prices come from call spreads with close strikes, we can conclude that the probability distribution function can be inferred from vanilla option prices.

Equation  $(2)$  shows that for close strikes or long expiries, the value of a call spread is approximately the strike difference times the probability that the underlying finishes above the spread:

CallSpread 
$$\approx e^{-r\tau}(K_2 - K_1) \cdot (1 - \Phi(K_2))$$
 (4)

This can be used as a crude first-order estimate for the value of a call spread. The second term in equation (2) can be approximated as (similar to the

![](_page_1_Figure_9.jpeg)

**Figure 3** The vega of a call spread at various times before expiration

area of a triangle)

$$e^{-r\tau} \int_{K_1}^{K_2} (S - K_1) p(S) dS \approx e^{-r\tau} \frac{(K_2 - K_1)}{2} \times (\Phi(K_2) - \Phi(K_1))$$
(5)

This gives a better approximation

Call Spread 
$$\approx e^{-r\tau}(K_2 - K_1)$$
  
  $\times \left(1 - \frac{\Phi(K_1) + \Phi(K_2)}{2}\right)$  (6)

This is a very intuitive formula as it is just the payoff of the call spread times the "average" probability the call spread finishes in the money.

## References

- Hull, J. (2003). Options, Futures, and Other Derivatives,  $[1]$ 5th Edition, Prentice Hall.
- Lehman Brothers (2008). Listed Binary Options, availa-[2] ble at http://www.cboe.com/Institutional/pdf/ListedBinary Options.pdf
- [3] The Options Industry Council (2007). *Option Strategies* in a Bull Market, available at www.888options.com.
- The Options Industry Council (2007). Option Strategies [4] in a Bear Market, available at www.888options.com.
- The Options Industry Council (2007). The Equity Options [5] Strategy Guide, January 2007, available at www.888 options.com
- [6] Reiner, E. & Rubinstein, M. (1991). Breaking down the barriers, Risk Magazine 4, 28-35.
- Taleb, N.N. (1997). Dynamic Hedging: Managing Vanilla [7] and Exotic Options, Wiley Finance.

[8] Wikipedia (undated). *Binary Option*, available at http://en. wikipedia.org/wiki/Binary option

## **Further Reading**

Haug, E.G. (2007). *Option Pricing Formulas*, 2nd Edition, McGraw Hill.

**Related Articles**

**Call Options**.

ERIC LIVERANCE
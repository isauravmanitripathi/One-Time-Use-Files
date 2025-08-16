## **Butterfly**

A butterfly spread is an option strategy with limited upside and limited downside that uses call options of three different strikes but the same maturity on the same underlying. Specifically, a butterfly is a structure that is a long position in 1 low-strike call, a short position in 2 midstrike calls, and a long position in 1 high-strike call. More details and pricing models can be found in [2]. Market considerations can be found in [4–6]. The butterfly spread produces a structure that at maturity pays off only in scenarios where the price of the underlying is between the lowest and highest strikes. One can think of this strategy as buying an option on the underlying being in a range. The butterfly has limited upside potential, but a significantly reduced cost compared to that of an outright call option. It should be used for expressing a bullish view that the underlying will trade in a range. As with all options, choosing the strike and maturity will depend on one's view of how much the underlying will move and how quickly it will move there. An example is shown in detail in Figure 1.

In the example shown in Figure 1, we look at a 780/800/820 butterfly on the S&P 500 index, SPX. With the underlying SPX index at 770 and with three months to expiration, the butterfly cost is close to 1.00. The call option with the 800 strike is 70.14; thus, the cost for a butterfly is significantly reduced from the outright cost of a call option with the same strike. This upfront cost for the butterfly is the maximum that this butterfly position can lose. We subtract this initial investment from all other valuations, as shown in Figure 1, to get a total value. If the underlying is exactly 800 at expiration, the position will earn 20 on the butterfly from the lowstrike option. The maximum position profit then is the strike spread minus the initial cost, or 20 − 1*.*00 = 19*.*00.

Note that with three months to expiration, the butterfly value is fairly insensitive to the underlying price and is difficult to distinguish from the *x*-axis. However, as the option gets closer to expiration, the sensitivity of the price of the call spread becomes greater, especially in the range of the butterfly strikes. This sensitivity to underlying price or delta (*see* **Delta Hedging**) is illustrated in Figure 2.

The delta of the butterfly stays relatively flat until relatively close to expiration of the option. When the butterfly is close to expiration, the delta is very unstable around the three strikes.

Another important consideration is the volatility implied by the market (*see* **Implied Volatility: Market Models**). The vega profile of a butterfly is shown in Figure 3. When the underlying is close to the strikes, the vega is negative because when volatility increases the probability that the underlying expires out of the money increases. For this reason, it is common to use a butterfly with relatively long expiries and with strikes centered around at-themoney to take a view that implied volatility will decline while still holding a position with relatively small delta (insensitive to changes in the underlying). When the underlying is away from the money, the butterfly is long vega because when volatility increases, the probability that the underlying finishes in the money increases.

## **The Relationship with Distribution of the Underlying**

A butterfly can be thought of as a long call spread plus a short call spread, with overlapping strikes and the same strike spread. An approximation for the value of a call spread can be found in **Call Spread**:

Call Spread 
$$\approx e^{-r\tau} (K_2 - K_1)$$
  
  $\cdot \left(1 - \frac{\Phi(K_1) + \Phi(K_2)}{2}\right)$  (1)

where *-(x)* is the cumulative distribution function of the underlying. Applying equation (1) to a butterfly, we have

Butterfly 
$$\approx e^{-r\tau} (K_2 - K_1)^2 \left[ \frac{\Phi(K_3) - \Phi(K_1)}{K_3 - K_1} \right]$$
  
 $\approx e^{-r\tau} (K_2 - K_1)^2 p(K_2)$  (2)

where *p(x)* is the probability distribution function of the underlying at option expiration and is the derivative of *-(x)* (Figure 4).

We can apply this formula in the following way. We convert the triangle in the lower part of Figure 3 to a square. Then we let the value of the payoff of the

![](_page_1_Figure_1.jpeg)

**Figure 1** The value of a butterfly at various times before expiration

![](_page_1_Figure_3.jpeg)

**Figure 2** The delta of a butterfly at various times before expiration

butterfly to be represented as the probability times the area of the square, as in equation (2). Then turning around equation (2), we have

$$\text{prob}(K_a < S < K_b) \approx e^{r\tau} \frac{\text{Butterfly}}{(K_2 - K_1)}$$
 (3)

The relationship between option prices and the distribution of the underlying was first pointed out in [1], but see also [3, 7]. The use of call spreads and butterflies to impute the market-implied underlying probability distribution can be related to taking derivatives with respect to the strike of the call price. A call spread is like a first derivative and a butterfly is like a second derivative. Formally, we have

$$Call = e^{-r\tau} \int_{K}^{\infty} (S - K)p(S)dS \tag{4}$$

![](_page_1_Figure_9.jpeg)

**Figure 3** The vega of a butterfly at various times before expiration

![](_page_1_Figure_11.jpeg)

**Figure 4** Using a butterfly to infer the underlying probability distribution

$$\frac{\partial}{\partial K}Call = -e^{-r\tau} \int_{K}^{\infty} p(S)dS \tag{5}$$

$$\frac{\partial^2}{\partial K^2}Call = -e^{-r\tau}p(K) \tag{6}$$

## **References**

- [1] Breeden, D. & Litzenberger, R. (1978). Prices of statecontingent claims implicit in option prices, *Journal of Business* **51**, 621–651.
- [2] Hull, J. (2003). *Options, Futures, and Other Derivatives*, 5th Edition, Prentice Hall.
- [3] Jackwerth, J.C. (1999). Option-implied risk-neutral distributions and implied binomial trees: a literature review, *The Journal of Derivatives* **7**, 66–82.

- [4] The Options Industry Council (2007). *Option Strategies in a Bull Market*, available at www.888options.com.
- [5] The Options Industry Council (2007). *Option Strategies in a Bear Market*, available at www.888options. com
- [6] The Options Industry Council (2007). *The Equity Options Strategy Guide*, January 2007, available at www.888 options.com
- [7] Rubenstein, M. (1994). Implied binomial trees, *The Journal of Finance* **49**, 771–818.

**Related Articles**

**Corridor Options**; **Risk-neutral Pricing**; **Variance Swap**.

ERIC LIVERANCE
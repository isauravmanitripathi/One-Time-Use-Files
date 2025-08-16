## Volatility Swaps

Volatility swaps are very similar to variance swaps, both in concept and in application. Like variance swaps, volatility swaps can be used by hedge funds to speculate on volatility movements or by portfolio managers to hedge other products against volatility fluctuations. Since their introduction in 1998, they have seen rapid growth and there is currently a sizable market in both the equity and foreign exchange markets. Volatility swaps are also traded in interest rate and commodity markets.

Technically speaking, a volatility swap is not really a swap, but a forward contract on the realized volatility. At maturity, the buyer receives from the seller the difference between the realized volatility and the fixed strike amount, multiplied by the dollar notional (quoted in dollar per volatility point):

Volatility swap = Notional 
$$\times (\sigma_{\text{realized}} - K)$$
 (1)

while

Variance swap = Notional 
$$\times (\sigma_{\text{realized}}^2 - K^2)$$
 (2)

The fixed strike payment is usually referred to as the *fixed leg* of the swap and the realized volatility is referred to as the *floating leg*. The swap contract contains the detailed specifications on how the volatility is calculated. Typically, the floating leg is calculated as

Annualization 
$$\times \sum_{1}^{N} \left( \ln \frac{S_i}{S_{i-1}} \right)^2$$
 (3)

where  $S_i$  should be adjusted by discrete dividends across dividend payment days. In the most accepted convention, the floating leg is reset and computed daily.

Besides variance swaps, another product closely related to volatility swaps is the VIX contract, which is written as the square root of the sum of expected future variances.

Because variance is the square of volatility, the payoff of a variance swap is convex in volatility while the payoff of a volatility swap is linear in volatility. A volatility swap is thus cheaper than the corresponding variance swap. More specifically, the fair strike for the volatilty swap is slightly lower than that of a variance swap. The difference between the two is known as the *convexity adjustment* and gets larger as volatility of volatility gets larger. The convexity adjustment can be calculated, for example, in the Heston model.

The variance swap is preferred in the equity market due to the fact that it can be replicated with a linear combination of vanilla options and a dynamic position in futures (see Variance Swap; [2]). In other markets, the volatility swap is actually more liquid than the variance swap. Although a position in variance swap can be replicated, a position in volatility swap cannot. This means that different models that correctly calibrate to the vanilla option surface will give the same price for variance swaps but not for the volatility swaps. In other words, the price of a variance swap is model independent, but the price of volatility swap is not. In practice, the volatility swap and variance swap admit almost equal pricing for short-term maturities. Recent research also suggest that the model dependence is not as large as it is commonly believed and volatility swaps can also be approximately replicated by trading vanilla options (see Volatility Index Options; Realized Volatility **Options**; [1]). Newer models have been developed that can price volatility derivatives including volatility swaps, while remaining consistent with the entire volatility surface [3].

## References

- [1] Carr, P. & Lee, R. (2007). Realised volatility and variance: option via swaps, Risk  $20(5)$ , 76-83.
- [2] Demeterfi, K., Derman, E., Kamal, M. & Zou, J. (1999). More than You Ever Wanted to Know About Volatility Swaps, Goldman Sachs Quantitative Strategies Research Notes
- [3] Ren, Y., Madan, D. & Qian, M. (2007). Calibrating and pricing with embedded local volatility models,  $Risk\ 20(9)$ ,  $138 - 143$ .

## **Related Articles**

Corridor Variance Swap; Realized Volatility **Options; Variance Swap; Volatility Index Options;** Weighted Variance Swap.

YONG REN
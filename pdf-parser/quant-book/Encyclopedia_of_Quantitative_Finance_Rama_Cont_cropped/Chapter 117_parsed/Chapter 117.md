# **Correlation Swap**

A correlation swap is a type of exotic derivative security that pays off the observed statistical correlation between the returns of several underlying assets, against a preagreed price. At the time of writing, it is traded over-the-counter (OTC) on equity and foreign exchange derivatives markets. This article focuses on equity correlation swaps, which appeared in the early  $2000s$ , as a means to hedge the parametric risk exposure of exotic trading desks to changes in correlation.

### Pavoff

Similar to variance swaps, the correlation swap payoff involves a notional (the amount to be paid/ received per *correlation point*<sup>a</sup>), a realized correlation component (the formula used to calculate the level of observed statistical correlation between the underlying assets), and a strike price:

> $Correlation \nswap \npayoff = notional$  $\times$  (realized correlation – strike)

For example, a one-year correlation swap contract on the constituents of the Dow Jones Euro Stoxx 50 index would include the following terms:

- underlying assets—each of the 50 constituent stocks denoted by  $S_1, \ldots, S_N$  ( $N = 50$ );
- notional—€100 000 per correlation point;
- realized correlation— $\frac{2}{N(N-1)} \sum_{1 \le i < j \le N} \rho_{i,j}$ , where

 $\rho_{i,j} = \frac{Cov(X_i, X_j)}{\sqrt{Var(X_i) \times Var(X_j)}} \times 100 \text{ is the familiar}$ pairwise coefficient of correlation between the time series  $X_i$  and  $X_j$  of daily log returns observed in the year following the trade date;

strike—52.0 *correlation points*.

Thus, if after one year the arithmetic average of pairwise correlation coefficients between the 50 underlying assets is equal to 58.3 correlation points, the swap seller will pay a net cash flow of €630 000 to the swap buyer.

## **Realized Correlation**

There are mainly two types of realized correlation formulas currently found on over-the-counter (OTC) markets:

- equally weighted realized correlation—the formula used in the above example:
- weighted realized correlation— $\frac{\sum\limits_{1 \leq i < j \leq N} w_i w_j \rho_{i,j}}{\sum w_i w_j},$  $\bullet$ where  $w_1, \ldots, w_N$  are preagreed positive weights summing to 1. In the above example, one would typically take the "index weights" as of the trade date, that is, the stock quantities that a portfolio manager would invest in to track one unit of the Dow Jones Euro Stoxx 50 index.

Several technical reports have investigated how the above weighted realized correlation (WRC) formula relates to other proxy formulas that are popular in econometrics, when the underlying assets and weights correspond to an equity index. Tierens-Anadu  $[4]$  give empirical evidence that in the case of the S&P 500 index,

$$WRC \approx \frac{\sum_{i < j} w_i w_j Cov(X_i, X_j)}{\sum_{i < j} w_i w_j \sqrt{Var(X_i)Var(X_j)}} \tag{1}$$

In addition, Bossu [1, 2] derives the following limit-case proxy formula, subject to some conditions on the weights:

$$\frac{\sum_{i < j} w_i w_j Cov(X_i, X_j)}{\sum_{i < j} w_i w_j \sqrt{Var(X_i)Var(X_j)}}\n$$

$$\n\frac{Var\left(\sum_{i=1}^N w_i X_i\right)}{\sum_{N \to \infty}^{\sim} \frac{Var\left(\sum_{i=1}^N w_i X_i\right)}{\left(\sum_{i=1}^N w_i \sqrt{Var(X_i)}\right)^2}}\n$$
(2)

The proxy formula on the right-hand side is remarkable because we can interpret the numerator as "index variance" and the denominator as "average constituent variance", which is more straightforward than the average of  $N \times (N-1)/2$  pairwise correlation coefficients.

#### **Fair Value**

At the time of writing, little is known about the "fair value" of correlation swaps. Owing to the typically large number of underlyings, the popular Monte Carlo engine with or without local volatility surfaces requires an  $N \times N$  correlation matrix as additional input parameter. There are two problems with this approach: a practical one and a theoretical one. The practical problem is that individual correlation coefficients cannot be implied from listed option markets.<sup> $b$ </sup> The theoretical problem is that, even if one could come up with a sensible implied correlation matrix, a meaningful dynamic replication strategy for the correlation swap payoff would still be missing.<sup>c</sup>

Ongoing research (see, e.g., the working papers of Bossu [1] and Jacquier [3]) aims to identify the linkages between dispersion trading and the dynamic hedging of correlation swaps, especially when the underlying assets are the constituent stocks of an equity index. This approach exploits the proxy formulas above to rewrite the correlation swap payoff as a function of tradable variance swaps; in this framework the correlation swap becomes a multiasset volatility derivative (see Realized Volatility Options), rather than a classical multiasset derivative.

#### **End Notes**

<sup>a.</sup>In market jargon, a *correlation point* is equal to 0.01. With this convention, the value of a correlation coefficient is comprised between  $-100$  and  $+100$  correlation points. <sup>b.</sup>To imply the value for  $\rho_{i,j}$ , one needs three option prices:

a vanilla option on  $S_i$ , a vanilla option on  $S_i$  and, for

example, a vanilla option on a portfolio made of 50%  $S_i$ and 50%  $S_i$ . The former two options are listed, the latter is not

<sup>c</sup>. For example, in a two-asset extension of the Black-Scholes model with instantaneous correlation (dln  $S^1$ )(dln  $S_t^2 = \rho \, dt$ , the forward value of an equally weighted correlation swap is simply  $\rho$  – *strike*, which would be hedged purely with cash!

#### References

- [1] Bossu, S. (2007). A New Approach For Modelling and Pricing Correlation Swaps, Dresdner Kleinwort Equity Derivatives report (working paper). Available at http://math.uchicago.edu/ $\sim$ sbossu/CorrelationSwaps7.  $\text{pdf}$
- [2] Bossu, S. & Gu, Y. (2004). Fundamental Relationship Between an Index's Volatility and the Average Volatility and Correlation of its Components, JPMorgan Equity Derivatives report (working paper). Available at http://math.uchicago.edu/~sbossu/CorrelFundamentals.  $\text{pdf}$
- [3] Jacquier, A. (2007). *Variance Dispersion and Correlation* Swaps, Working paper. Available at SSRN: http://ssrn. com/abstract=998924
- [4] Tierens, I. & Anadu, M. (2004). Does it Matter Which Methodology you use to Measure Average Correlation Across Stocks? Goldman Sachs Equity Derivatives Strategy: Quantitative Insights, 13 April 2004.

### **Related Articles**

Basket Options; Correlation Risk; Dispersion Trading: Variance Swap.

Sébastien Bossu
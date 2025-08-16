# **Corridor Variance Swap**

A corridor variance swap, with corridor  $C$ , on an underlying Y is a weighted variance swap on  $X :=$  $log Y$  (unless otherwise specified), with weight given by the corridor's indicator function:

$$w(y) := \mathbb{1}_{y \in C} \tag{1}$$

For example, one may define an up-variance swap by taking  $C = (H, \infty)$  and a *down*-variance swap by taking  $C = (0, H)$ , for some agreed H.

In practice, the corridor variance swap monitors  $Y$  discretely, typically daily, for some number of periods N, annualizes by a factor such as  $252/N$ , and multiplies by notional, for a total payoff

Notional × Annualization × 
$$\sum_{n=1}^{N} \mathbb{1}_{Y_n \in C} \left( \log \frac{Y_n}{Y_{n-1}} \right)^2$$
 (2)

If the contract makes dividend adjustments (as typical for contracts on single stocks but not on indices), then the term inside the parentheses becomes  $\log((Y_n +$  $D_n/Y_{n-1}$ , where  $D_n$  denotes the dividend payment, if any, of the  $n$ th period.

Corridor variance swaps accumulate only the variance that occurs while price is in the corridor. The buyer therefore pays less than the cost of a full variance swap. Among the possible motivations for a volatility investor to accept this trade-off and to buy up (or down) variance are the following. First, the investor may be bullish (bearish) on  $Y$ . Second, the investor may have the view that the market's downward volatility skew is too steep (flat), making down-variance expensive (cheap) relative to upvariance. Third, the investor may be seeking to hedge a short volatility position that worsens as  $Y$  increases (decreases).

## **Model-free Replication and Valuation**

The continuously monitored corridor variance swap admits model-free replication by a static position in options and dynamic trading of shares, under conditions specified in Weighted Variance Swap, which include all positive continuous semimartingale share prices  $Y$  under deterministic interest rates and proportional dividends.

Explicitly, one replicates using equation  $(7)$  of that article, with  $\lambda$  derived in [3]:

$$\lambda(y) = \int_{K \in C} \frac{2}{K^2} \text{Van}(y, K) \, \text{d}K \tag{3}$$

where  $\text{Van}(y, K) := (K - y)^+ \mathbb{1}_{K < \kappa} + (y - K)^+ \mathbb{1}_{K > \kappa}$ for an arbitrary put/call separator  $\kappa$ .

Therefore, in the case that the interest rate equals the dividend yield (otherwise, see Weighted Vari**ance Swap**), a replicating portfolio statically holds  $2/K^2 dK$  vanilla calls or puts at each strike K in the corridor  $C$ . The corridor variance swap modelindependently has the same initial value as a claim on the time-T payoff  $\lambda(Y_r) - \lambda(Y_0)$ . Additionally, the replication strategy trades shares dynamically according to a "zero-vol" delta-hedge, meaning that its share holding equals the negative of what would be the European portfolio's delta under zero volatility.

For corridors of the type  $C = (0, H)$  or  $C =$  $(H, \infty)$  where  $H > 0$ , taking  $\kappa := H$  in equation (3) yields

$$\lambda(y) = (-2\log(y/H) + 2y/H - 2) \mathbb{1}_{y \in C} \tag{4}$$

This  $\lambda$ , with H chosen arbitrarily, is also valid for the variance swap  $C = (0, \infty)$ 

# **Further Properties**

1. For a small interval  $C = (a, b)$ , the corridor variance swap approximates a contract on local time, in the following sense. Corridor variance satisfies

$$V_T^{(a,b)} := \int_0^T \mathbb{1}_{X_t \in (\log a, \log b)} \, \mathrm{d} \langle X \rangle_t$$
$$= \int_{\log a}^{\log b} L_T^x \, \mathrm{d}x \tag{5}$$

by the occupation time formula, where  $L_T^x$ denotes (an  $x$ -cadlag modification of) the *local time* of  $X$ . Therefore, at any point  $a$ ,

$$\frac{1}{\log b - \log a} V_T^{(a,b)} \longrightarrow L_T^a \quad \text{as } b \downarrow a \tag{6}$$

2. Corridor variance can arise from imperfect replication of variance. The replicating portfolio for a standard variance swap holds options at all strikes  $K \in (0, \infty)$ . In practice, not all of those strikes actually trade. If we truncate the portfolio to hold only the strikes in some interval  $C$ , then the resulting value does not price a full variance swap but rather a C-corridor variance swap. (Moreover, in practice not even an interval of strikes actually trade, but rather a finite set, which can replicate instead a strike-to-strike notion of corridor variance, as shown in  $[1]$ .)

3. In the case  $C = (H, \infty)$ , where  $H > 0$ , we rewrite equation  $(4)$  as

$$\lambda(y) = \frac{2}{H}(y - H)^{+} - 2(\log y - \log H)^{+} \tag{7}$$

Thus, the replicating portfolio is long calls on  $Y_T$ and short calls on  $\log Y_T$ .

Let  $F_{X_T}$  be the characteristic function of  $X_T = \log Y_T$ . Then techniques in [4, 5] price the calls on  $Y_T$  and  $\log Y_T$ , respectively. Specifically, assuming zero interest rates and dividends, we have the following semiexplicit formula for the corridor variance swap's fair strike:

$$\mathbb{E}\lambda(Y_T) - \lambda(Y_0)$$
  
=  $\frac{2}{H\pi} \int_{0-\alpha i}^{\infty-\alpha i} \text{Re}\left(\frac{F_{X_T}(z-i)}{iz-z^2} e^{-iz\log H}\right) dz$   
+  $\frac{2}{\pi} \int_{0-\beta i}^{\infty-\beta i} \text{Re}\left(\frac{F_{X_T}(z)}{z^2} e^{-iz\log H}\right) dz - \lambda(Y_0)$   
(8)

for arbitrary positive  $\alpha$ ,  $\beta$  such that  $\alpha + 1$ ,  $\beta <$  $\sup\{p: \mathbb{E}Y_T^p < \infty\}$ , where  $\mathbb{E}$  denotes expectation with respect to martingale measure.

In the case  $C = (0, \infty)$ , equation (4) implies the fair strike formula

$$\mathbb{E}\lambda(Y_T) - \lambda(Y_0) = -2\mathbb{E}\log(Y_T/Y_0)$$
$$= 2iF'_{X_T}(0) + 2\log Y_0 \quad (9)$$

In the case  $C = (H_1, H_2)$ , where  $0 \le H_1 < H_2$ , subtract the formula for  $C = (H_2, \infty)$  from the formula for  $C = (H_1, \infty)$ .

In the case of nonzero interest rates or dividends, add to equation  $(8)$  a correction involving payoffs at all expiries in  $(0, T)$ , as specified in equation (7a) in **Weighted Variance Swap**, and in equation (9) replace  $Y_0$  by the forward price.

4 With discrete monitoring, the question arises, how to define up-variance and down-variance, and in particular how much variance to recognize, given a discrete move that takes  $Y$  across  $H.$  Definition (2) recognizes the full square of each move that ends in the corridor. Alternatively, the contract specifications in  $[2]$  treat the movements of  $Y$  across  $H$  by recognizing a fraction of the squared move. The fraction is defined in a way that admits approximate discrete hedging, in the sense that the time-discretized implementation of the continuous replication strategy has in each period a hedging error of only third order in that period's return.

#### References

- [1] Carr, P. & Lee, R. (2008). From Hyper Options to Variance Swaps, Bloomberg LP, University of Chicago.
- [2] Carr, P. & Lewis, K. (2004). Corridor variance swaps, Risk 17(2), 67-72.
- [3] Carr, P. & Madan, D. (1998). Towards a theory of volatility trading, in Volatility, R., Jarrow, ed, Risk Publications, pp. 417-427.
- [4] Carr, P. & Madan, D. (1999). Option valuation using the fast Fourier transform, Journal of Computational Finance  $3.463 - 520$
- [5] Lee, R. (2004). Option pricing by transform methods: extensions, unification, and error control, Journal of Computational Finance 7(3), 51-86.

## **Related Articles**

Delta Hedging; Gamma Swap; Realized Volatility Options; Variance Swap; Volatility Swaps; Weighted Variance Swap.

ROGER LEE
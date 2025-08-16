# Gamma Swap

A gamma swap on an underlying  $Y$  is a *weighted* variance swap (see Weighted Variance Swap) on  $\log Y$ , with weight function

$$w(y) := y/Y_0 \tag{1}$$

In practice, the gamma swap monitors  $Y$  discretely, typically daily, for some number of periods  $N$ , annualizes by a factor such as  $252/N$ , and multiplies by notional, for a total payoff

Notional × Annualization × 
$$\sum_{n=1}^{N} \frac{Y_n}{Y_0} \left( \log \frac{Y_n}{Y_{n-1}} \right)^2$$
 (2)

If the contract makes dividend adjustments (as typical for single-stock gamma swaps but not index gamma swaps), then the term inside the parentheses becomes  $\log((Y_n + D_n)/Y_{n-1})$ , where  $D_n$  denotes the dividend payment, if any, of the  $n$ th period.

Gamma swaps allow investors to acquire variance exposures proportional to the underlying level. One application is dispersion trading of a basket's volatility against its components' single-name volatilities; as a component's value increases, its proportion of the total basket value also increases and, hence, so does the desired volatility exposure of the singlename contract. This variable exposure to volatility is provided by gamma swaps, according to point 1 of the "Further Properties" below. A second application is to trade the volatility skew; for example, to express a view that the skew slopes too steeply downward, the investor can go long a gamma swap and short a variance swap, to create a weighting  $y/Y_0 - 1$ , which is short downside variance and long upside variance. A third application is to trade single-stock variance without the caps often embedded in variance swaps to protect the seller from crash risk; in a gamma swap, the weighting inherently dampens the downside variance, so caps are typically regarded as unnecessary.

### **Model-free Replication and Valuation**

The continuously monitored gamma swap admits model-free replication by a static position in options and dynamic trading of shares, under conditions specified in **Weighted Variance Swap**, which include all positive continuous semimartingale share prices  $Y$  under deterministic interest rates and proportional dividends.

Explicitly, one replicates by using equation  $(7)$  of the above article, with

$$\lambda(y) = \frac{2}{Y_0} \left[ y \log(y/\kappa) - y + \kappa \right]$$
$$= \int_0^\infty \frac{2}{Y_0 K} \text{Van}(y, K) \, \text{d}K \tag{3}$$

where  $\text{Van}(y, K) := (K - y)^+ \mathbb{1}_{K < \kappa} + (y - K)^+ \mathbb{1}_{K > \kappa}$ for an arbitrary put/call separator  $\kappa$ . Forms of this payoff were derived in, for instance, [2, 3].

Therefore, in the case that the interest rate equals the dividend yield (otherwise, see the weighted variance swap article), a replicating portfolio statically holds  $2/(Y_0K)$  dK vanilla calls or puts at each strike  $K$ . The gamma swap model independently has the same initial value as a claim on the time-T payoff  $\lambda(Y_T) - \lambda(Y_0)$ . Additionally, the replication strategy trades shares dynamically according to a "zero-vol" delta-hedge, meaning that its share holding equals the negative of what would be the European portfolio's delta under zero volatility.

### **Further Properties**

Points  $2-5$  follow from equation 3. Point 1 uses only the definition 1.

1. For an index  $Y_t := \sum_{j=1}^J \theta_j Y_{j,t}$ , let  $\alpha_{j,t} := \theta_j Y_{j,t} / Y_t$  be the fraction of total index value due to the quantity  $\theta_j$  of the jth component  $Y_{j,t}$ . Define the cumulative *dispersion*  $D_t$  by

$$dD_t = \sum_{j=1}^{J} \alpha_{j,t} d[\log Y_j]_t - d[\log Y]_t \qquad (4)$$

Going long  $\alpha_{i,0}$  gamma swaps (non-dividendadjusted) on each  $Y_i$  and short a gamma swap on  $Y$  creates the payoff

$$\sum_{j=1}^{J} \alpha_{j,0} \int_{0}^{T} \frac{Y_{j,t}}{Y_{j,0}} \, \mathrm{d}[\log Y_{j}]_{t} - \int_{0}^{T} \frac{Y_{t}}{Y_{0}} \, \mathrm{d}[\log Y]_{t}$$
$$= \int_{0}^{T} \frac{Y_{t}}{Y_{0}} \, \mathrm{d}D_{t} \tag{5}$$

as noted in [2]. Hence, a static combination of gamma swaps produces cumulative indexweighted dispersion.

- 2. By Corollary 2.7 in [1], if the implied volatility smile is symmetric in log-moneyness, and the dividend yield equals the interest rate  $(q_t = r_t)$ , and there are no discrete dividends, then a gamma swap has the same value as a variance swap.
- 3. Assuming that  $Y_T = Y_t R_{t,T}$  for all t, where the time-*t* conditional distribution of each  $R_{t,T}$ does not depend on  $Y_t$ , the gamma swap has time- $t$  gamma equal to a discounting/ dividend-dependent factor times

$$\frac{2}{Y_0} \mathbb{E}_t \left( \frac{\partial^2}{\partial y^2} \bigg|_{y=Y_t} y R_{t,T} \log(y R_{t,T}) \right) = \frac{2 \mathbb{E}_t R_{t,T}}{Y_0 Y_t}$$
(6)

where  $\mathbb{E}$  denotes expectation with respect to martingale measure. Therefore, the share gamma, defined to be  $Y_t$  times the gamma, does not depend on  $Y_t$ . This property motivates the term gamma swap.

4. Within the family of weight functions proportional to  $w(y) = y^n$ , the gamma swap takes  $n = 1$ . In that sense, the gamma swap is intermediate between the usual logarithmic variance swap (which takes  $n = 0$ ) and an arithmetic variance swap (which, in effect, takes  $n = 2$ ).

Expressed in terms of put and call holdings, the replicating portfolios in these three cases hold, at each strike  $K$ , a quantity proportional to  $K^{n-2}$ . The gamma swap  $O(1/K)$  is intermediate between logarithmic variance  $O(1/K^2)$  and arithmetic variance  $O(1)$ .

5. Let F be the characteristic function of  $\log Y_T$ . If  $\mathbb{E}Y_{T}^{p} < \infty$  for some  $p > 1$  then

$$\mathbb{E}Y_T \log Y_T = -iF'(-i) \tag{7}$$

Gamma swap valuations are therefore directly computable in continuous models for which  $F$ is known, such as the Heston model (see **Heston** Model).

### References

- [1] Carr, P. & Lee, R. Put-call symmetry: extensions and applications, *Mathematical Finance*, Forthcoming,
- [2] Mougeot, N. (2005). Variance Swaps and Beyond, BNP Paribas.
- [3] Overhaus, M., Bermúdez, A., Buehler, H., Ferraris, A., Jordinson, C. & Lamnouar, A. (2007). Equity Hybrid Derivatives, John Wiley & Sons.

## **Related Articles**

Corridor Variance Swap; Delta Hedging; Realized Volatility Options; Variance Swap; Volatility Swaps: Weighted Variance Swap.

ROGER LEE
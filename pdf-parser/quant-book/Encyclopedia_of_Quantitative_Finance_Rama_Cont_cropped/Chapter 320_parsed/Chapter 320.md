# **Commodity Trading**

Considerable concern has grown around speculative opportunities in commodity markets, which attracted hundreds of billions of dollars in recent years. In February 2008, a Reuter news item announced that "London coffee, cocoa and sugar futures rallied (*...*) to multi-year peaks as investment funds and speculators shifted money into soft commodities in search of stellar returns." In July 2008, Brent oil was quoted at its historical peak of 174.27 USD per barrel, before losing about 70% of that quote four months later (December 2008). Equally significant changes occurred in the prices of cotton, coffee, wheat, soybeans, corn as well as aluminum and copper.

Since unit production costs of agricultural and nonagricultural commodities did not vary so extensively in the same period—nor did consumption—we cannot just attribute the recent marked price changes to their fundamentals. Commodity index funds, hedge funds, and speculators are, therefore, the center of huge fluctuations, changing vastly the drivers of commodity markets.

Speculative opportunities are an obvious reason for this wide interest.

In oil futures markets, a significant role of speculation has been identified to explain the large daily upward and downward shifts observed in prices [3]. Thus, even these extremely liquid instruments suffer from liquidity shocks that induce periods of increased volatility and significant returns predictability [12]. These authors conclude that the oil futures market is not driven only by fundamentals.

Empirical papers have reported evidence of predictability in commodity markets (see among others [14, 17, 20]). Moreover, theoretical contributions [5, 6, 21] attribute a key role to inventories to limit extreme price fluctuations, recognizing at the same time that inventories introduce predictability on (storable) commodity prices.

Finally, the attraction to speculation on commodity markets can be self-induced.

"Herd behavior" on the side of speculators [7] or "excess consensus" [22] can exacerbate price movements in commodity futures markets and large storage owners can profit from large price deviations. Spurred by the growing attention of specialized press and by the academic evidence showing that commodity futures portfolios can be managed similarly to equities portfolios [16], the investment industry started offering products, allowing individuals and institutions to "invest" in commodities through several derivatives and structured notes. The performance of such products can be compared to that of popular commodity indices (e.g., Sachs commodity index) and have allowed some authors, as Domanski and Heath [9], to introduce the term *financialization* of commodity markets.

In commodity markets, predictability is essentially equivalent to mean reversion of prices as several theoretical and empirical contributions have shown (e.g., [1, 4, 10, 18] for securities [24], for commodities, and [8, 19] for electricity).

In their theoretical analysis on the role of inventories, Deaton and Laroque [5, 6] observe that the price boundaries introduced by inventory owners turn out to generate mean reversion in the price process.

From an empirical point of view, Elam [11] observes that the price of December cotton futures (at planting time) helps forecasting the cotton price at harvest. In particular, when futures price is higher than its long-term average, spot price tends to be lower and *vice versa*. This is exactly a mean-reverting behavior.

In their empirical analysis of several commodity markets [2], the authors adapt a simple trading strategy to exploit significant mean reversion observed in the corresponding price processes.

Till [25] takes into consideration two historically profitable trading strategies based on the meanreverting properties of commodity prices.

Predictability and the relevance of mean reversion on commodity markets have also been contrasted, as in [23]. Nevertheless, the authors cannot deny the significance of mean reversion over periods longer than six months.

This evidence justifies the interest of this work. We devise optimal boundaries for the entry and exit timing of a trading strategy in a mean-reverting market.

Since our strategy is based on the peculiar properties of a mean-reverting stationary price process, it is important to observe that as long as such a strategy remains profitable, the presence of a mean-reverting stationary behavior is confirmed.

## The Trading Strategy

Consider a mean-reverting process of an asset price  $x$  on which a long and a short position can be taken (such as a spot or a forward contract). The process can described by the following stochastic differential  $\text{equation} \quad \text{(SDE)}$ :

$$dx = -\lambda (x - \Phi) dt + \theta dW \qquad (1)$$

where  $\lambda$  is the continuous speed of reversion,  $\theta$  the diffusion coefficient, and  $\Phi$  is the long run average. If we consider discrete time intervals of length  $\Delta t$ , the corresponding discrete autoregressive process is

$$x_{t+1} = x_t + k(\Phi - x_t) + \sigma \varepsilon_{t+1} \tag{2}$$

where  $k = 1 - e^{-\lambda \Delta t}$ ,  $\sigma^2 = \frac{1 - e^{-2\lambda \Delta t}}{2\lambda} \theta^2$  and  $\{\varepsilon_n\}$  are independent and identically distributed  $N(0, 1)$ . As soon as the process  $x_t$  diverges from  $\Phi$ , the drift adjusts instantaneously to revert back to  $\Phi$ . The reversion speed depends on  $k$  ( $0 \le k \le 1$ ). The case  $k = 0$  corresponds to a random walk.

To keep things simple, we assume that the long run average is a constant. Still, we are aware that for long-term trading strategies, it could be worth considering the inflationary or other trend elements of this average. Our one-factor process limits the shape of the forward curve more severely than it actually happens. Further, the long run average could be stochastic itself. This can be a key factor that makes the process nonstationary  $[15]$ . On the other hand, in the empirical application that follows, we will see that a constant long run price average is statistically consistent at the usual levels for several markets. Besides, the assumption of a constant  $\Phi$ can be reasonable for finite (especially short) horizon strategies and has the advantage of improving the mathematical tractability.

We consider a strategy that is very close to a simple buy-and-hold. For ease of illustration, we account only for profits and losses, ignore the margin requirements, and do not consider transaction costs. We assume a zero-risk-free rate.

In a trading horizon  $[0, T]$  choose  $a > 0$  and construct two barriers around  $\Phi$ :  $\Phi + a$  and  $\Phi - a$ , respectively, the sell and buy barriers. Let  $t^* \in [0, T)$ be the first time when  $x_t \geq \Phi + a$  or  $x_t \leq \Phi - a$ , that is, when the price first crosses one of the two boundaries. A short or long position is then started depending on which one of the two conditions is verified first.

Suppose that  $x_t$  goes below  $\Phi - a$  in  $t^*$ , so one can take a long position (buy the asset on the spot market or a future/forward contract) for the nominal value of  $\Phi - a$ . The position can be closed in two ways. In the first case (*full closing*), the position is closed if  $x_t >$  $\Phi + a$  for some  $t < T$ ; the net profit is 2a. There is, however, the possibility that such a condition is not met before  $T$ . In this case, the position is closed at price  $x_T$ , with a random profit/loss  $x_T - (\Phi - a)$ . Analogously, the strategy is started with an opposite sign (short position) if  $x_t > \Phi + a$  in  $t^*$ . If  $t^* \notin [0, T)$ (i.e.,  $x_t$  remains within the two boundaries over all the trading period), the strategy is not started and the net profit is 0 (Table 1).

This trading strategy can be implemented on the spot (respectively, futures) market, assuming that  $x_t$ is the spot (respectively, futures) price. In the case of commodity spot markets, some additional technicalities are required, such as borrowing/lending the commodity in a self-financing position. Such aspects do not alter our results. Further, by assuming a zero interest rate and equally balancing the frequencies of long and short positions, we do not need to account for gains and losses generated by borrowing/lending positions.<sup>a</sup>

The expected profit can be optimized with respect to  $a$  under two different strategies:

1. no bounds on the full closing probabilities (maximum return strategy, MRS):

$$\max_{a} E[G(a;k,\sigma,T)] \tag{3}$$

a lower bound of 95% on the full closing probabilities (fixed risk strategy, FRS)

$$\max_{a} E[G(a;k,\sigma,T)]$$
  
s.t.  $p_{11} \ge 0.95$  (4)

where  $p_{11}$  is the full closing probability.

**Table 1** Plot of decision bounds over the price series. Outcomes of a trading strategy (time horizon  $T$ , boundaries  $\Phi + a$  and  $\Phi - a$ )

|                                               | $x_t$ goes above $\Phi + a$ before T |                    |  |  |
|-----------------------------------------------|--------------------------------------|--------------------|--|--|
| G                                             | Yes                                  | No                 |  |  |
| $x_t$ goes below $\Phi - a$ Yes<br>before $T$ | 2a<br>No $(\Phi + a) - x_T$          | $x_T - (\Phi - a)$ |  |  |

FRS is a VaR-like strategy as the "risk" involved in the strategy is constrained under the 5% probability of not having a full closing. We solved equations (3) and (4) numerically, searching for the optimal *a* on a large grid of *k* and *T* by a Monte Carlo simulation based on 2*.*727 × 10<sup>7</sup> trajectories. For more details, see [13].

#### *The Risk–Return Trade-off*

**MRS.** Simulations show that for every pair *(k, T )* there is a bound maximizing the expected profit. From Figure 1(a) we see that, in general, the maximum expected profit increases with *T* , but the effect is more pronounced for relatively low values of *k*, which for practical purposes is very interesting. From Figure 1(b) (MRS depending on *k* for several values of *T* ), we note that at short maturities MRS increases with *k*, while for longer maturities the expected profit is not monotonic: a positive reversion speed is required to generate positive expected profits; however, if it is too strong, it keeps the process close to the long run mean, reducing the profit opportunities generated by the diffusion.

**FRS.** Figure 2 shows the dependency of *a* on *T* and *k*. As a function of *k* (Figure 2b), short-term and long-term strategies differ: for short terms, faster reversion coefficients *k* imply higher closing probabilities (and so a larger *a* and a larger expected profit), but when the time horizon is high, an excessively strong reversion reduces the optimal bound and the

![](_page_2_Figure_6.jpeg)

**Figure 1** (a) MRS *vs* the maturity *T* for *k* = 0*.*01, 0*.*02, 0*.*1, 0*.*3, 1. (b) MRS *vs* the reversion *k* for *T* = 5, 10, 30, 90, 300, 1000

![](_page_2_Figure_8.jpeg)

**Figure 2** (a) The optimal bound *a*FRS *vs* the maturity *T* for *k* = 0*.*01, 0*.*02, 0*.*1, 0*.*3, 1. (b) The optimal bound *a*FRS *vs* the reversion *k* for *T* = 5, 10, 30, 90, 300, 1000

expected profit accordingly. For every large  $T$ , there is a  $k$  maximizing the full closing probability.

# **The Empirical Evidence**

We collected the series of 6931 daily prices of nearby futures contracts of live cattle, cotton, gas oil, copper, wheat and sugar for the period January 1, 1981 to July 27, 2007. We simulated a trader taking a short/long position during a time interval  $j$ . The position is taken only once on the basis of the trading signals suggested by the optimal values of  $a$  calculated on data available up to the interval  $j-1$ . The strategy starts only if a significant stationary mean reversion is observed up to  $i-1$ . We evaluated the profit/losses generated by the two trading strategies, MRS and FRS, over several subperiods obtained by splitting the original series in intervals of different length (30, 50, 70, 100, 200, 300, 500 trading days).

As a refinement of those strategies, when selling or buying conditions are met (i.e.,  $x_t \geq \Phi + a$ ,  $x_t < \Phi - a$ ), trades occur at price  $x_t$  instead of the boundary value. The strategies remain the same, but the order execution is similar to what is known as a *best price order* (the investor fixes a boundary price,

<table>

 **Table 2** Stationarity test and significance reversion speed
estimates and significance

| Series      | τ         | $\text{Prob}(\tau)$ | $k$ (%)  | $\text{Prob}(k)$ |
|-------------|-----------|---------------------|----------|------------------|
| Live cattle | $-3.1927$ | 0.0211              | 0.297    | 0.0026           |
| Cotton      | $-3.8290$ | 0.0028              | 0.360    | 0.0002           |
| Gas oil     | $-1.1244$ | 0.7086              | 0.084    | 0.3285           |
| Copper      | 1.3040    | 0.9987              | $-0.058$ | 0.3153           |
| Coffee      | $-2.1375$ | 0.2296              | 0.208    | 0.0390           |
| Wheat       | $-2.3858$ | 0.1459              | 0.218    | 0.0236           |

**Table 3** MRS strategy—percentage return

then the market trader executes the order at the best price available on the book satisfying the boundary).

Estimates and tests of stationarity and reversion speed are shown in Table 2. The stationarity test is based on a standard augmented Dickey-Fuller's  $\tau$  (Prob( $\tau$ ) is the rejection probability under the null hypothesis that the series is stationary). The significance of the reversion speed parameter is given by a  $t$ -test on the ordinary least squares (OLS) regression 1 ( $\text{Prob}(k)$  is the rejection probability under the null hypothesis  $k \neq 0$ ). Live cattle and cotton are significantly stationary and mean reverting. For gas oil and copper, stationarity is rejected, mainly due to the marked rise in prices that has occurred in the recent years; as a consequence, the reversion speed coefficients are not significantly different from zero. Coffee and wheat are not stationary, while their reversion coefficients are significant at 5% level.

Tables 3 and 4 report the results of MRS and FRS, respectively. To make results comparable among commodities, profits and losses are expressed as an average of all profit/losses under each maturity and are normalized as a percentage of the corresponding historical average price. Thus, figures may be taken as the average "rate of return" obtained by applying the strategy on one unit of the underlying commodity over a period of length  $T$ . A  $t$ -test assesses the statistical significance  $(1\%, 5\%)$ .

FRS and MRS show a similar pattern, with MRS offering higher average profits as expected. Trading in live cattle gives on average sizeable MRS profits for  $T = 100$ , 200, 300, and 500. Cotton offers MRS positive returns (of a lesser size) for  $T = 30, 100,$ 300, and 500. Gas oil and copper show negligible or even significant negative returns (with an isolated exception for gas oil at  $T = 500$ ): this is due to the nonstationarity of the series and the recent steady rise

| Series      | Maturity      |               |               |               |               |               |              |
|-------------|---------------|---------------|---------------|---------------|---------------|---------------|--------------|
|             | $T = 30$      | $T = 50$      | $T = 70$      | $T = 100$     | $T = 200$     | $T = 300$     | $T = 500$    |
| Live cattle | $-0.375^{**}$ | $-0.333**$    | 0.149         | $1.602**$     | 5.680**       | $4.450**$     | 8.793**      |
| Cotton      | $0.013^{**}$  | $0.005*$      | $-0.003$      | $-0.022^{**}$ | 0.082         | $0.056^{**}$  | $0.211^{**}$ |
| Gas oil     | 0.001         | $-0.004^*$    | $0.011**$     | $-0.004$      | 0.003         | $-0.037**$    | $0.140^{**}$ |
| Copper      | $-0.007^{**}$ | $-0.032^{**}$ | $-0.031^{**}$ | $-0.031^{**}$ | $-0.029^{**}$ | $-0.101^{**}$ | 0.019        |
| Coffee      | $-0.013^{**}$ | 0.005         | $-0.024^{**}$ | $-0.064^{**}$ | $-0.068**$    | $-0.100^{**}$ | $-0.157**$   |
| Wheat       | 0.903**       | 0.095         | 0.051         | $0.674*$      | $-0.466$      | $-5.864**$    | $-7.769**$   |

\* significant at 5%, \*\* significant at 1%

| Series      |               | Maturity      |               |               |               |               |            |  |
|-------------|---------------|---------------|---------------|---------------|---------------|---------------|------------|--|
|             | $T = 30$      | $T = 50$      | $T = 70$      | $T = 100$     | $T = 200$     | $T = 300$     | $T = 500$  |  |
| Live cattle | $-0.067$      | $-0.127$      | 0.029         | 0.797**       | 4.127         | 4.773**       | 7.584**    |  |
| Cotton      | $0.007**$     | $0.005*$      | 0.006         | $-0.028^{**}$ | 0.061         | $0.033^{**}$  | $0.117**$  |  |
| Gas oil     | 0.001         | $-0.004^{**}$ | 0.003         | $-0.001$      | 0.006         | $-0.032^{**}$ | 0.119**    |  |
| Copper      | $-0.005^{**}$ | $-0.023^{**}$ | $-0.031^{**}$ | $-0.032^{**}$ | $-0.030^{**}$ | $-0.112^{**}$ | $-0.002$   |  |
| Coffee      | $-0.007**$    | 0.002         | $-0.037**$    | $-0.063**$    | $-0.028*$     | $-0.108**$    | $-0.135**$ |  |
| Wheat       | $0.606**$     | $0.357**$     | $0.384*$      | $0.830^{**}$  | 1.241         | $-3.318**$    | 1.427      |  |

Table 4 FRS strategy—percentage return

\*\* significant at 1%, \* significant at 5%

in prices. Under such conditions, prices do not reverse within the chosen boundaries. Thus, according to our strategy, the position is opened often, but is seldom "fully" closed.

Coffee for  $T = 300$ , 500 and Wheat for  $T = 300$ (and also  $T = 500$  for MRS) show FRS statistically significant negative expected returns (of a relevant size for wheat). Our trading strategies would have offered significant positive returns if applied with opposite trading signs.

The empirical outcomes confirm the theoretical expectations only for live cattle and cotton, where both stationarity and mean reversion are statistically acceptable. The other commodities, for which stationarity is weak or not significant, offer significant positive returns only on a strict range of the trading intervals or even show significant losses. The lack of stationarity of gas oil, copper, and coffee generates average losses almost over all maturities. Puzzling results as returns turning from positive (for shorter maturities) to negative (for longer ones) may be explained by markets mixing "momentum" and "reverting" regimes, where prices revert to their historical average in the short run but tend to systematically diverge on longer observation periods. This is the case of wheat from 1986 to 1995 or from 1998 to 2007.

# Conclusions

We proposed a trading rule exploiting the peculiarities of a mean reversion process and investigated the related properties. The empirical results confirm the simulation analyses and show how our strategies perform nicely in markets that are stationary and mean reverting.

Such results lead to some relevant conclusions about the current hypothesis of mean reversion in commodity markets. Mean reversion can be a relevant component of the process governing many commodities. However, our results, in particular for wheat, are more consistent with markets showing regimes switching from reversion to momentum and back.

Moreover, commodity prices are not always stationary. Metals and energy prices were relatively stationary for a long time, but experienced a strong positive trend in the recent years. Many agricultural commodities mix trend with stationarity. The opportunity to fruitfully adopt our strategies is, therefore, linked to the ability of discriminating, for each commodity, stationarity from momentum market phases, which can be an easier task than forecasting size and sign of the future price changes. In such a case, switching from a momentum to a meanreverting strategy can be a useful practice for many investors and traders.

## **End Notes**

<sup>a.</sup>In a risk-neutral setting, a zero interest rate implies the absence of trend for any traded asset.

## References

- Bessembinder, H., Coughenor, J.F., Seguin, P.J. & [1] Smoller, M.M. (1995). Mean reversion in equilibrium asset prices: evidence from the futures term structure, *Journal of Finance* **50**(1), 361–375.
- [2] Carcano, G., Falbo, P. & Stefani, S. (2005). Speculative trading in mean reverting markets, European Journal of Operations Research 163(1), 132-144.
- [3] Cifarelli, G. & Paladino, G. (2008). Oil Price Dynamics and Speculation. A Multivariate Financial Approach. Dipartimento di Scienze Economiche, Università

degli Studi di Firenze, Working Paper N.15/2008, www.dse.unifi.it.

- [4] Cutler, D.M., Poterba, J.M. & Summers, L.H. (1991). Speculative dynamics, *Review of Economic Studies* **58**, 529–546.
- [5] Deaton, A.S. & Laroque, G. (1992). On the behavior of commodity prices, *Review of Economic Studies* **89**, 1–23.
- [6] Deaton, A.S. & Laroque, G. (1996). Competitive storage and commodity price dynamics, *Journal of Political Economy* **104**, 896–923.
- [7] De Long, J.B., Shleifer, A., Summers, L.H. & Waldmann, R.J. (1990). Positive feedback investment strategies and destabilizing rational speculation, *The Journal of Finance* **45**(2), 379–395.
- [8] Deng, S. (2000). *Stochastic Models of Energy Commodity Prices and Their Applications: Mean-reversion with Jumps and Spikes*. POWER, Working Paper PWP-073.
- [9] Domanski, D. & Heath, A. (2007). Financial investors and commodity markets, *Bank for International Settlements Quarterly Review* March, 53–67.
- [10] Dueker, M.J. (1997). Markov switching in GARCH processes and mean reverting stock market volatility, *Journal of Business and Economic Statistics* **15**(1), 26–34.
- [11] Elam, E. (2000). A marketing strategy for cotton producers based on mean reversion in cotton futures prices, *Beltwide Cotton Conferences Proceedings*, National Cotton Council, Memphis, TN, pp. 310–313.
- [12] Fagan, S. & Gencay, R. (2007). *Liquidity-induced Dynamics in Futures Markets*, Munich Personal RePEc Archive. MPRA Paper 6677, University Library of Munich.
- [13] Falbo, P., Felletti, D. & Stefani, S. (2007). *Optimal Trading in Mean Reverting Markets*. Dipartimento Metodi Quantitativi per le Scienze Economiche e Aziendali University Milano-Bicocca, Working Paper 125.
- [14] Finkenstadt, B. & Kuhbier, P. (1995). Forecasting nonlinear economic time series: a simple test to accompany the nearest neighbor approach, *Empirical Economics* **20**(2), 243–263.
- [15] Geman, H. (2005). Energy commodity prices: is mean reversion dead? *The Journal of Alternative Investments* Fall, 31–44.
- [16] Gorton, G.B., Hayashi, F. & Rouwenhorst, K.G. (2007). *The Fundamentals of Commodity Futures Returns*.

*National Bureau of Economic Research (NBER)*, Working Paper 13249.

- [17] Gregoriou, G.N. & Chen, Y. (2006). Evaluation of commodity trading advisors using fixed and variable and benchmark models, *Annals of Operations Research* **145**, 183–200.
- [18] Hsieh, D.A. (1995). Nonlinear dynamics in financial markets: evidence and implications, *Financial Analyst Journal* **51**(4), 55–62.
- [19] Lari-Lavassani, A., Sadeghi, A.A. & Ware, T. (2001). *Mean Reverting Models for Energy Option Pricing*, Electronic Publications of the International Energy Credit Association, www.ieca.net.
- [20] Moholwa, M. (2005). *Testing for Weak-form Efficiency in South African Futures Markets for White and Yellow Maize*, Michigan State University, Department of Agricultural Economics. Graduate Research Master's Degree Plan B Papers.
- [21] Ng, S. & Ruge-Murcia, F.J. (2000). Explaining the persistence of commodity prices, *Computational Economics* **16**, 149–71.
- [22] Roehner, B.M. & Sornette, D. (2000). Thermometers of speculative frenzy, *The European Physical Journal B - Condensed Matter and Complex Systems* **16**, 729–739.
- [23] Sam, Y.B. & Brorsen, B.W. (2000). Rollover hedging, *NCR-134 Conference on Applied Commodity Price Analysis, Forecasting, and Market Risk Management*, Chicago, http://ageconsearch.umn.edu/handle/18938.
- [24] Schwartz, E.S. (1997). The stochastic behavior of commodity prices: implications for valuation and hedging, *The Journal of Finance* **52**(3), 923–973.
- [25] Till, H. (2007). Trading strategies in the current commodity market environment, *Commodity Risk Magazine* May, www.energyrisk.com.

# **Related Articles**

## **Commodity Forward Curve Modeling**; **Commodity Price Models**; **Commodity Risk**.

PAOLO FALBO, DANIELE FELLETTI & SILVANA STEFANI
# **Foreign Exchange Smiles**

## **Smile Regularities for Foreign Exchange** Options

One trend in the empirical investigation of implied volatilities has been to concentrate on understanding the behavior of implied volatilities across strike prices and time to expiration [see 10]. This line of research assumes implicitly that these divergences provide information about the dynamics of the options markets. Another approach  $[3, 5, 6, 14]$  suggests that the divergences of implied volatilities across strike prices may provide information about the expected dispersion process for underlying asset prices. These papers assume that asset return volatility is a (locally) deterministic function of the asset price and time and that this information can be used to enhance the traditional Black-Scholes-Merton (BSM) option-pricing approach (see also Dupire Equation; Local Volatility Model). All these papers examine implied volatility patterns at a single point in time and assume that option prices provide an indication of the deterministic volatility function. However, Dumas et al.  $[4]$  (1998) tested for the existence of a deterministic implied volatility function and rejected the hypothesis that the inclusion of such a model in option pricing was an improvement in terms of predictive or hedging performance compared with BSM. Their research examined whether at a single point in time, implied volatility surfaces provide predictions of implied volatilities at some future date (one week hence).

Tompkins [15] looked at this problem in a slightly different way. The approach of Dumas et al. [4] assumes that the deterministic volatility function provides both a prediction of the future levels of implied volatility and the relative shapes of implied volatilities across strike prices and time. If the future levels of implied volatilities cannot be predicted, this does not mean that the relative shapes of implied volatilities cannot be predicted. Tompkins [15] examined the relative implied volatility bias rather than the absolute implied volatility bias. When the volatilities of each strike price were standardized by dividing the level of the at-the-money (ATM) volatility, regularities in the volatility function were found. He further found that these standardized smile patterns were dependent upon the term to expiration of the option. For a large sample of option expiration cycles, the smile patterns were almost identical for all options with the same time to expiration.

For currency options, Tompkins [15] examined options on futures for US dollar/Deutsche mark, US dollar/British pound, US dollar/Japanese ven, and US dollar/Swiss franc for a time period from 1985 to 2000. To determine relative shapes, the implied volatilities for each currency pair were standardized by

$$VSI = \left(\frac{\sigma_{x}}{\sigma_{\text{ATM}}}\right) \cdot 100 \tag{1}$$

where VSI is the volatility smile index,  $\sigma_x$  is the volatility of an option with strike price  $x$ , and  $\sigma_{\text{ATM}}$  is the volatility of the ATM option. The ATM volatility was determined using a simple linear interpolation for the two implied volatilities of the strike prices that bracketed the underlying asset price. This relative volatility measure will facilitate comparisons of biases (in percentage terms) within and between markets.

The strike prices were standardized to allow intra- and intermarket comparisons to be drawn. The standardized strike prices can be expressed as

$$\frac{\ln(X_{\tau}/F_{\tau})}{\sigma\sqrt{\tau/365}}\tag{2}$$

where  $X$  is the strike price of the option,  $F$  is the underlying futures price and the square root of time factor reflects the percentage in a year of the remaining time until the expiration of the option. The sigma ( $\sigma$ ) is the level of the ATM volatility.

As the analysis was restricted to the actively traded quarterly expiration schedule of March, June, September, and December maturities, implied volatility surfaces with a maximum term to expiration of approximately 90 days were obtained. Data were further pruned by restricting the analysis to 18 time points from (the date nearest to) 90 calendar days to expiration to (the date nearest) 5 calendar days to expiration in 5-day increments. Finally, the analysis of the implied volatilities was limited to those strike prices in the range  $\pm 3.5$  standard deviations away from the underlying futures price. Figure 1 displays the aggregated patterns for the 15-year period.

A logical starting point for an appropriate functional form to fit an implied volatility surface is the approach suggested by Dumas et al. [4] (1996), who

![](_page_1_Figure_1.jpeg)

Figure 1 Actual implied volatility surfaces of option prices for four foreign exchange futures standardized to the level of the ATM volatility (1985–2000)

tested a number of arbitrary models based upon a polynomial expansion across strike price  $(x)$  and time  $(t)$ . Tompkins [15] extended the polynomial expansion to degree three and included additional factors, which might also influence the behaviors of volatility surfaces.

For all four foreign exchange options markets, a parsimonious model explains the vast majority of the variance in the standardized implied volatility surfaces. The analysis allowed strike price effects to be separated into a first-order effect (the skew), a second-order effect (the smile), and higher order effects. For the skew effect, the results suggested that an asymmetrical smile pattern is a function of the level of the foreign exchange rate. The evidence suggests that when futures prices are low (high), the implied volatility pattern becomes more negatively (positively) skewed.

For the second-order "curved" pattern, all four markets display a convex pattern that becomes more extreme as the options expiration date is approached. Furthermore, a significant negative relationship is found between the degree of curvature and the level

of the ATM implied volatility. Curved patterns are independent of the level of the exchange rate. Finally, Tompkins [15] reports a significant third-order strike price effect for all four foreign exchange option markets. Tompkins [15] shows that the high degree of explanatory power is invariant to the time period of analysis and that the model provides accurate smile predictions outside of the estimation sample period. Under these assumptions, we conclude that regularities in implied volatility surfaces exist and are similar for the four currency markets. Furthermore, the regularities are time period invariant. These general results provide means to test alternative models, which could potentially explain why implied volatility surfaces exist. This is discussed in the following section.

## **Empirical Regularities for Currency Option Smiles**

From  $[15]$ , the following general conclusions can be drawn for the behaviors of implied volatility surfaces for options on foreign exchange:

- 1. Implied volatility patterns are symmetrical on average for options on currencies.
- 2. For three of the four markets, the skew effect is related to the level of the underlying futures price. The only exception is for the British pound/US dollar. The level of the futures price impacts the skewness in an inverse manner to the pure skewness effect. This suggests that for low futures prices a negative skew occurs and at higher futures prices the skew flattens and can become positive.
- 3. The skew effect for currency options is relatively invariant to the time to expiration of the options. It is solely due to extreme levels of the underlying exchange rate or to some market shock.
- 4. For two of the four markets, the level of the skew effect is inversely related to the level of the ATM implied volatility. For the Deutsche mark and Swiss franc, the higher (lower) the level of the ATM implied volatility, the more negative (positive) the level of the skew.
- 5. Shocks change the degree and sign of the skew effect. For the Deutsche mark and Swiss franc, the concerted intervention in the currency markets by the Group of Seven (G7) caused a negative skew to occur. The 1987 stock crash had minimal impact on the currency markets, with only a slightly negative skew impact for the Deutsche mark. For the second shock, the only currency option skew affected was the Japanese yen. This occurred in January 1988 and appears to have been associated with international capital flows out of the US dollar into yen.
- 6. All implied volatility patterns display some degree of curvature and the degree of curvature is inversely related to the option's term to expiration. The longer the term to expiration, the less extreme the degree of curvature in the smile.
- 7. Shocks change the degree of curvature of the implied volatility pattern. However, the effect is not systematic and often shocks reduce the degree of curvature. For the G7 intervention in 1985, there was a reduction in the degree of smile curvature for both the Deutsche mark and Swiss franc, while for the Japanese yen,

this event caused greater curvature for the smiles. For the second shock, both the British pound and Japanese yen displayed greater smile curvature thereafter.

- 8. For all four markets, the degree of curvature of the implied volatility pattern is inversely related to the level of the ATM implied volatility. Thus, the higher the level of ATM implied volatility, the less pronounced the degree of curvature in the smile.
- 9. For three of the four currency markets, the degree of curvature is independent of the level of the underlying futures price. The only exception is for the Japanese yen, where the higher the level of the exchange rate, the lesser the curvature (however, this impact is small).
- 10. For all four markets, the degree of curvature of the implied volatility pattern is asymmetrical. For the Deutsche mark, Japanese yen, and Swiss franc, the degree of asymmetry is negative. This suggests that the curvature is more extreme for options with strike prices below the current level of the underlying futures. For the British pound, the relationship is positive, indicating that the curvature is more extreme for options with strike prices above the current level of the underlying futures.

Using these 10 stylized facts as clues, we now examine alternative explanations for the existence of implied volatility smiles. It is crucial that any coherent explanation must conform to all of these facts simultaneously. If selected models are internally inconsistent with these facts, it is grounds for rejection.

A nontrivial problem is that the statistical testing of any option-pricing model has to be a joint hypothesis that the option-pricing model is correct and that the markets are efficient. Given that smiles do exist, we can reject the hypothesis that actual option values conform to the Black [2] model. However, we are uncertain as to why this occurs. Consider two possible reasons for the existence of smiles: the underlying asset may follow an alternative price process or the Black [2] model is correct but market imperfections exist. The next sections discuss both possibilities to better understand the regularities in implied volatility surfaces presented in [15].

# **Models with Alternative Price and Volatility Processes**

Consider first that some alternative price (and volatility) process is at work instead of geometric Brownian motion with constant variance. Following the general approach of Jarrow and Rudd [11], we consider alternative true terminal distributions for the underlying asset. Consider the following models that include stochastic volatility (*σ*ˆ ) and alternative price processes. For the sake of convenience, the volatility processes will be evaluated in terms of a stochastic variance process (√*<sup>V</sup>* ). Given that our previous results examined options on futures, the notation indicates that the underlying asset is a futures price (*F*). The first model, which will be considered, is a stochastic volatility model: the square root process model proposed by Heston [7] (*see also* **Stochastic Volatility Models: Foreign Exchange**; **Heston Model**). This choice is due to the ability of this model to allow correlated underlying and volatility processes. This will be defined as

*Model 1*

$$dF(t) = \mu F(t) dt + \hat{\sigma} F(t) dZ_1(t)$$
(3)

with the variance process defined by

$$dV(t) = \kappa(\theta - V(t)) dt + \xi \sqrt{V(t)} dZ_2(t) \qquad (4)$$

where *Z*<sup>1</sup> and *Z*<sup>2</sup> are standard Wiener processes with correlation *ρ*. The term *κ* indicates the rate of mean reversion of the variance, *θ* is the long-term variance, and *ξ* indicates the volatility of the variance. The terms *<sup>V</sup>* and. <sup>√</sup>*<sup>V</sup>* represent the variance and the volatility of the process, respectively.

The second model that we consider is the jumpdiffusion model proposed by Merton [13] (*see also* **Jump-diffusion Models**). Using his notation, this can be expressed as

*Model 2*

$$dF(t) = F(\alpha - \lambda \kappa) dt + F\sigma(t) dZ(t) + dq(t)$$
(5)

Using his notation, *α* is the instantaneous expected return on the futures contract, *σ(t)* is the instantaneous volatility of the futures contract, conditional on no arrivals of important new information (no jumps), d*Z* is a standard Wiener process, *q*(*t*) is the independent Poisson process, which captures the jumps. The term *λ* is the mean number of arrivals per unit time and *κ* represents the jumps size (which can also be a random variable).

Bates [1], Ho *et al.* [8], and Jiang [12] assumed that the volatility process is subordinated in a nonnormal price process; this provides the inspiration for the third model (see [1] for tests of these models). In this spirit, the third proposed model is a variant of the Heston [7] model, proposed by Tompkins [16, 17], which includes jumps (as captured by a normal inverse Gaussian (NIG) process) in the underlying price process.

*Model 3*

$$dF(t) = \mu F(t-) dt + \hat{\sigma}(t)F(t-) dN(t) \quad (6)$$

with the variance process defined by

$$dV(t) = k(\theta - V(t)) dt + \xi \sqrt{V(t)} dZ(t) \qquad (7)$$

where *N*(*t*) is a purely discontinuous martingale corresponding to log returns driven by an NIG Levy ´ process (*see* **Normal Inverse Gaussian Model**). This model will be referred to as *normal inverse Gaussian stochastic volatility* (*NIGSV*) for the sake of convenience.

# **Smile Patterns Associated with the Proposed Models**

Tompkins [17] discussed how parameters for each of these models could be estimated (under the physical measure) and the change of measure to allow risk neutral pricing. Of more interest to this article is the resulting smile behavior of each model. This can be seen in Figure 2 (restricted solely to the Deutsche mark/US dollar). Figure 2(a) shows the empirical smile patterns for Deutsche mark/US dollar from 1985 to 2000. Figure 2(b) shows the smile surface associated with the Heston [7] model. Figure 2(c) shows the smile surface associated with the jump-diffusion model of Merton [13]. Figure 2(d) represents the combination of stochastic volatility and jump processes (NIGSV model).

![](_page_4_Figure_1.jpeg)

Figure 2 Simulated implied volatility smiles for options on Deutsche mark/US dollar

## Smile Patterns Associated with Stochastic Volatility

As one can see in Figure  $2(b)$ , the Heston [7] model does generate a symmetrically curved smile function consistent with point #1, but the smiles are flat as the option expiration approaches and become more curved, the longer the term to expiration (which is inconsistent with point #6). This is exactly the opposite of what is observed for currency smiles empirically. The Heston [7] model can generate a skewed implied volatility pattern from a nonzero correlation between the volatility and underlying processes (see equations 3 and 4). However, the longer the term to expiration, the more extreme the skew pattern would be. This is inconsistent with point #3, that skewed patterns for currency options are time invariant and are only associated with the levels of the ATM implied volatility or the underlying currency exchange rate. However, this model is consistent with fact #5 that shocks could change the degree of skewness. The model could still be valid under a regime of stochastic correlations. However, it seems inconsistent from an economic standpoint; if shocks change the degree of asymmetry in the expected terminal distribution of the underlying asset, it is not clear why in half of the instances the degree of curvature (fact #8) is reduced. This model is also inconsistent with fact #8, that the higher the level of expected variance (ATM volatility), the flatter the degree of curvature. Given that this model would produce effects that are contradictory to both first and second strike price effects observed empirically, we must reject it. An alternative explanation is that the jump-diffusion model of Merton [13] may be more appropriate.

## Smile Patterns Associated with Stochastic Volatility

According to Hull [9], this model could produce a curved implied volatility surface and this curve would be consistent with fact  $\#6$ , that curves exist and become more extreme the shorter the time to expiration of the option. This can be seen in Figure 2, where the degree of curvature is most extreme closest to expiration. However, as the Poisson process in equation (5) is independent and identically distributed (i.i.d.), this will converge over time to a normal distribution and thus, the implied volatility surface would flatten, which is what occurs in Figure 2. It could also hold under a regime associated with fact #7, that shocks do change the degree of curvature. It could be that the inflow of new information changes the expectations of market agents regarding the degree and magnitude of future jumps. However, the model, as it stands, would not be able to explain the first-order strike price effects. One alternative would be to allow the shocks to be asymmetric. This would allow a skewed implied volatility pattern to exist. However, if the jumps follow some i.i.d. process, the central limit theorem would imply that the degree of skewness would be highest when the options are closest to expiration and would flatten as the term to expiration is lengthened. This is at variance with fact #3 that for currency options the skew effects are time invariant. Therefore, we can also reject a jumpdiffusion model as being inconsistent with the empirical record.

# **Smile Patterns Associated with the NIGSV Model**

This model assumes a symmetrical jump-diffusion process with a subordinated stochastic volatility process with nonzero correlations between the two processes. The simulated implied volatility smiles appear in Figure 2(d) and seem to resemble most the actual smiles for Deutsche mark/US dollars options in Figure 2(a). As can be seen, there is curvature in the smile patterns for both short term and longer term options. The shorter term curvature is associated with the jump process, while the longer term curvature is associated with stochastic volatility. This is consistent with both fact #1 and fact #6, that the average smile pattern is symmetrical and the degree of curvature is inversely related to time. Dynamics of the skew relationship can be explained with variations of the correlation between the two processes. Finally, the asymmetry of the smile shapes can be explained by the jump process. While this model appears to display many of the dynamics of empirical smiles, the degree of curvature is not as extreme as is observed for the actual smiles. The reason for this is that the parameters for the model were estimated using the underlying Deutsche mark/US dollar currency futures (see [17] for details). While a feasible measure change was used to price options (that omitted arbitrage), it is unlikely that this measure change is unique as nontraded sources of risk have been introduced into the state space. These include jumps and stochastic volatility. Given this, we should expect that option prices will also contain some risk premium above and beyond the values associated with the underlying asset.

### **Conclusions and Implications**

In this article, we have examined currency option smiles. Previous research by Tompkins [15] suggests that when implied volatility patterns are standardized, regularities are observed both across markets and across time. He concludes that this may suggest that market participants have developed some consistent algorithm to vary option prices in a consistent manner away from Black [2] values.

To better understand the nature of this algorithm, 10 stylized results are identified from his results for the four currency option markets. With these 10 results we test whether alternative models, which have been proposed to explain the existence of implied volatility surfaces, can generate the same dynamics as these empirical results. Initially, models were examined that suggest an alternative price process may better define the underlying price and volatility processes. We reject both the Heston [7] and the Merton [13] models as appropriate models, as they cannot produce all the empirical dynamics for actual smiles. The only model that could explain all the dynamics is a model that combines stochastic volatility and nonnormal innovations for currency returns. When appropriate parameters are input into this model and a feasible change of measure is made, option prices can be determined. The smiles associated with this model match the dynamics observed for actual currency option smiles. However, the model smiles do not display the same extreme degree of curvature as the empirical smiles. Following Tompkins [17], this suggests that a substantial risk premium exists for currency options and that the hypothesis that the existence of implied volatility surfaces are due solely to an alternative price process is rejected.

Alternatively, market imperfections may be the reason for the existence of implied volatility surfaces. Given that existing research has previously rejected this, we tend to concur that market imperfections alone are also probably not sufficient to explain the existence of implied volatility smiles. However, it is possible that both alternative price processes and market imperfections jointly contribute to the existence of implied volatility smiles.

### **References**

- [1] Bates, D.S. (1996). jumps and stochastic volatility: exchange rate process implicit in Deutsche Mark options, *Review of Financial Studies* **9**, 69–107.
- [2] Black, F. (1976). The pricing of commodity contracts, *Journal of Financial Economics* **3**, 167–179.
- [3] Derman, E. & Kani, I. (1994). Riding on the smile, *Risk* **7**, 32–39.
- [4] Dumas, B., Fleming, J. & Whaley, R.E. (1998). Implied volatility functions: empirical tests, *The Journal of Finance* **53**, 2059–2106.
- [5] Dupire, B. (1992). *Arbitrage Pricing with Stochastic Volatility*, Working Paper, Societ´ e G ´ en´ erale Options ´ Division.
- [6] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- [7] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–343.
- [8] Ho, M.S., Perraudin, W.R.M. & Sørensen, B.E. (1996). A continuous-time arbitrage-pricing model with stochastic volatility and jumps, *Journal of Business & Economic Statistics* **14**, 31–43.
- [9] Hull, J. (1997). *Options, Futures and other Derivative Securities*, 3rd Edition, Prentice Hall, Upper Saddle River.
- [10] Jackwerth, J.C. & Rubinstein, M. (1996). Recovering probability distributions from option prices, *The Journal of Finance* **51**, 1611–1631.
- [11] Jarrow, R. & Rudd, A. (1982). Approximate option valuation for arbitrary stochastic processes, *Journal of Financial Economics* **10**, 347–369.

- [12] Jiang, G. (1999). Stochastic volatility and jumpdiffusion—implications on option pricing, *International Journal of Theoretical and Applied Finance* **2**(4), 409–440.
- [13] Merton, R. (1976). Option pricing when underlying stock returns are discontinuous, *Journal of Financial Economics* **3**, 125–144.
- [14] Rubinstein, M. (1994). Implied binomial trees, *The Journal of Finance* **49**, 771–818.
- [15] Tompkins, R.G. (2001). Implied volatility surfaces: uncovering regularities for options of financial futures, *The European Journal of Finance* **7**, 198–230.
- [16] Tompkins, R.G. (2003). Options on bond futures: isolating the risk premium, *Journal of Futures Markets* **23**(2), 169–215.
- [17] Tompkins, R.G. (2006). Why smiles exist in foreign exchange options: isolating components of the risk neutral process, *The European Journal of Finance* **12**, 583–604.

### **Further Reading**

- Balyeat, R.B. (2002). The economic significance of risk premiums in the S&P 500 options market, *Journal of Futures Markets* **22**, 1145–1178.
- Garman, M. & Kohlhagen, S. (1983). Foreign currency option values, *Journal of International Money and Finance* **2**, 231–237.
- Henker, T. & Kazemi, H.B. (1998). The impact of deviations from random walk, in *Security Prices on Option Prices*, Working Paper, University of Massachusetts, Amherst.

### **Related Articles**

**Foreign Exchange Smile Interpolation**; **Implied Volatility Surface**; **Stochastic Volatility Models: Foreign Exchange**.

ROBERT G. TOMPKINS
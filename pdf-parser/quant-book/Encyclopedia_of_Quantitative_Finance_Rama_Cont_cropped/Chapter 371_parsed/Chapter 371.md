## **Stylized Properties of Asset Returns**

Since prices of different stocks are not necessarily influenced by the same events or information sets, price series obtained from different assets and  $-a$ fortiori-from different markets may exhibit different (statistical) properties. After all, why should properties of corn futures be similar to those of IBM shares or the dollar/yen exchange rate? Nevertheless, the result of more than half a century of empirical studies on financial time series indicates that this is the case if one examines their properties from a *statistical* point of view. The seemingly random variations of asset prices  $do$  share some nontrivial statistical properties. Such properties, common across a wide range of instruments, markets, and time periods, are called *stylized empirical facts* [10].

This assertion is backed by a vast research literature dealing with the statistical properties of financial time series which has developed during the last 50 years. Some early references include [25, 26, 29]. Surveys of stylized facts of financial time series are given in [17] for foreign exchange rates and in [5, 8, 10, 16, 30] for stocks and indices. Scaling and time-aggregation properties for high-frequency data are studied in [2] for stocks and in [17, 18, 27, 28] for foreign exchange rates. Numerous empirical studies on the scaling properties of returns can also be found in the physics literature [7].

Stylized facts are thus obtained by taking a common denominator among the properties observed in studies of different markets and instruments. Obviously, by doing so one gains in generality but tends to lose in the precision of the statements one can make about asset returns. Indeed, stylized facts are usually formulated in terms of *qualitative properties* of asset returns and may not be precise enough to distinguish among different parametric models. Nevertheless, albeit qualitative, these stylized facts are so constraining that it is not even easy to exhibit an  $(ad$ *hoc*) stochastic process which possesses the same set of properties, and stochastic modeling has gone to great lengths to reproduce these stylized facts.

Stylized facts are usually formulated in terms of asset (log-)returns defined as

$$r_t(\Delta) = \ln \frac{S_{t+\Delta}}{S_t} \tag{1}$$

where  $S_t$  is the price of an asset at date t and  $\Delta$  is a time horizon. The properties of returns series  $r_t(\Delta)$ greatly depend on the sampling frequency, that is, on  $\Delta$ .

We focus here on empirical properties for daily (log-)returns of stocks and stock market indices in liquid markets and refer to **High-frequency Data** and Market Microstructure Effects for properties of intraday data.

1. **Heavy tails:** The (unconditional) distributions of returns display—at time horizons ranging from an hour to several weeks—heavy tails and positive sample excess kurtosis, properties that both reject the Gaussian assumption (Figure 1). A more precise formulation requires measuring the heaviness of the tails. For heavy tails with "regular variation" (see Extreme Value **Theory**), that is, of the type

$$P(r_t \ge x) = \frac{l_-(x)}{|x|^{\alpha_+}}, \qquad P(r_t \le x) = \frac{l_-(x)}{|x|^{\alpha_-}}$$
(2)

where  $l_{+}$  (respectively  $l_{-}$ ) is slowly varying at  $+\infty$  (respectively  $-\infty$ ) and  $\alpha_{+}, \alpha_{-} > 0$  are the (right/left) tail exponents, the heaviness of the tails can be measured by the value of  $\alpha_+, \alpha_-, \xi_+ = 1/\alpha_+$  is sometimes called the (right) *tail index*. Light tailed distributions with exponential-type tail have a zero tail index, while a strictly positive tail index indicates heavy tails of regularly varying type. Tail exponents can be estimated using a Hill estimator or using methods based on the extreme value theory (see **Extreme Value Theory**). Figure 2 shows the estimation of right and left tail indices for SP100 daily returns: in this example we find  $\alpha_{+} \simeq 4$  and  $\alpha_{-} \simeq 3$ . For stock and index returns, tail exponents are often found to be finite, higher than two and less than five for most data sets studied [20, 23, 24]. In particular, this excludes stable laws with infinite variance and the normal distribution. Power-law or Pareto tails reproduce such behavior. But, as argued, for example, in Heyde and Kou [19], with small samples exponential tails ("semiheavy tails") may be difficult to distinguish from Pareto tails

![](_page_1_Figure_1.jpeg)

**Figure 1** Kernel estimator of empirical density of SP100 daily returns (solid line) vs Gaussian density (dotted line) with same mean and variance, on a logarithmic scale. Note the dominance of the tails with respect to the Gaussian and the asymmetry of the empirical density

2. **Absence of autocorrelations:** (Linear) autocorrelations of asset returns are often insignificant, except at short lags (10 min) for which microstructure effects come into play (*see* **Market Microstructure Effects**). Figure 3 illustrates this fact for the yen–US dollar exchange rate. This absence of significant autocorrelation can be attributed to the existence of arbitrageurs who "whiten the spectrum of price changes", making their second-order properties indistinguishable from a white noise sequence [26]. A consequence of this absence of autocorrela-

tion is the additivity of variance or "squareroot" scaling rule: the variance of returns at horizon *n* is *n* times the variance at horizon in the absence of autocorrelations; thus the standard deviation should be scaled by <sup>√</sup>*n*. This scaling is the basis of the variance ratio test

![](_page_1_Figure_5.jpeg)

**Figure 2** Hill estimators for the tail index of SP100 daily returns. We obtain *α*<sup>+</sup> 4 and *α*<sup>−</sup> 3. Note the large standard errors

![](_page_2_Figure_1.jpeg)

**Figure 3** Autocorrelation function of log-returns, USD/ yen exchange rate, = 5 min

for autocorrelation [8]. Note that this scaling rule breaks down for illiquid assets for which one typically observes high autocorrelation of returns.

3. **Gain/loss asymmetry:** Unconditional distributions of stock returns are often asymmetric. Although, this asymmetry may go undetected, when using moment-based measures such as skewness, one often observes a left tail which is heavier than the right tail, as attested by the tail index (*see* **Heavy Tails**) or extremal index (*see* **Extreme Value Theory**) estimates [20, 24]. For exchange rates between major currencies, there is a higher symmetry in up/down moves and the skewness can change sign from one period to another.

Daily changes in credit spreads (e.g., credit default swap spreads, *see* **Credit Default Swaps**) show an opposite asymmetry: they exhibit a heavier right (upper) tail and there are more frequent large upward jumps in credit spreads.

4. **Aggregational normality:** As one increases the timescale over which returns are calculated, their distribution looks more and more like a normal distribution. In particular, the shape of the distribution is not the same at different timescales: the heavy-tailed feature becomes less pronounced as the time horizon is increased.

5. **Volatility clustering:** "Large changes tend to be followed by large changes, of either sign, and small changes tend to be followed by small changes" [25]. A quantitative manifestation of this fact is that, while returns themselves are uncorrelated, absolute returns |*rt()*|, their squares, as well as other implied or historical volatility indicators display a positive, significant, and slowly decaying autocorrelation function. In particular, this observation rules out the assumption of independence of returns and points to nonlinear dependence in returns across time.

This property is sometimes called the "*ARCH effect*" in the econometrics literature, because of the fact that ARCH models (*see* **GARCH Models**) have this property. This is a misnomer: volatility clustering is a model-free property of data that has nothing to do with ARCH models.

6. **Conditional heavy tails:** Even after adjusting returns for volatility clustering (i.e. normalizing returns by a dynamic estimator of volatility, such as in GARCH-type models), the residuals (normalized returns) still exhibit heavy tails [5, 14]. However, the tails are less heavy than in the unconditional distribution of returns. This remark has motivated the development of

conditionally heteroskedastic models driven by non-Gaussian noise in discrete time and Levy- ´ driven stochastic volatility models in continuous time [4, 5, 13, 14] (*see* **GARCH Models**; **Jump Processes**; **Time-changed Levy Pro- ´ cess**; **Regime-switching Models**).

7. **Slow decay of autocorrelation in absolute returns:** The autocorrelation function of absolute (or squared) returns decays slowly as a function of the time lag, roughly as a power-law with an exponent *β* ≤ 1. An example is shown in Figure 4. This is sometimes interpreted as a sign of long-range dependence in volatility (*see* **Long Range Dependence**; **Multifractals**).

It has been argued [4, 22] that the decay of the autocorrelation of |*rt*| can also be reproduced by a superposition of several exponentials, indicating that the dependence is characterized by multiple timescales. In fact, an operational definition of long-range dependence is that the timescale of dependence in a sample of length

![](_page_3_Figure_1.jpeg)

**Figure 4** Autocorrelation function of squared log-returns: S&P500 futures, = 30 min

*T* is found to be of the order of *T* : dependence extends over the whole sample. Interestingly, the largest timescale in [22] is found to be of the order of the sample size, a prediction which would be compatible with long-range dependence [11].

8. **"Leverage" effect:** Volatility increases when the stock price falls. More precisely, changes in implied or historical indicators of volatility of an asset are negatively correlated with the returns of that asset. In fact, there is evidence of a lead–lag relationship: a negative correlation between *past* returns and (current) changes in volatility [6].

The name "leverage effect" comes from a supposed explanation based on a firm's capital structure: a decrease in the market valuation of a firm's equity increases the degree of leverage in its capital structure, leading to an increase in stock volatility. However, empirical studies do not seem to confirm this "explanation" [3] and the "leverage effect" should be seen more in terms of an asymmetric impact of news on returns and volatility [15].

9. **Volume-volatility correlation:** Trading volume in a given period (e.g., daily trading volume) is positively correlated with measures of volatility (e.g., realized volatility on the same day). The same holds for other measures of market activity such as the number of trades.

These observations have motivated the construction of models in which the dynamics of prices is modeled as a function of cumulative volume [9] or number of transaction, and has inspired models based on time-changed processes (*see* **Time-changed Levy Process ´** ; **Mixture of Distribution Hypothesis**; **Time Change**).

10. **Asymmetry in time scales:** Volatility indicators computed at lower frequency predict future volatility at higher frequency, whereas past values of high-frequency volatility indicators do not necessarily have predictive power for future low-frequency volatility [18]. This observation has led to the development of "random cascade" models, in which market shocks affect price behavior at low frequencies (fine scales) and their impact trickles down to lower scales (*see* **Multifractals**; [27]).

It may be noted that we have not included "selfsimilarity" or scale invariance among the above properties. In fact, there is ample empirical evidence showing that asset returns are *not* scale invariant or self-similar [12]. For example, the shape of the distribution of returns *rt()* at a horizon greatly varies with and "scales" in a nontrivial way, which is not captured by simple self-similar models such as *α*-stable Levy processes ( ´ *see* **Levy Processes ´** ) or (fractional) Brownian motion (*see* **Fractional Brownian Motion**).

## **Stylized Facts as Model Benchmarks**

Stylized empirical facts have motivated research in two different directions. One is the development of stochastic models—in discrete or continuous time—whose aim is to match some or all of the observed properties of financial time series. For instance, the (G)ARCH family of models (*see* **GARCH Models**) was mainly developed to model volatility clustering and heavy tails in asset returns, while stochastic volatility models were developed to model volatility clustering and the leverage effect. Similarly, models based on Levy processes ( ´ *see* **Exponential Levy Models ´** ) were initially introduced to capture the time-aggregation properties (heavy tails at high-frequency, scaling with respect to the horizon ) of the distribution of returns.

Another strand of research has aimed at proposing economic explanations for the origins of stylized facts. Representative agent models attempt to explain stylized facts in terms of the behavior of a hypothetical representative investor whose behavior generates market price changes. Ait Sahalia [1] shows that this approach can go a long way in terms of reproducing, if not explaining, stylized empirical facts. By contrast, agent-based market models [11, 21] tend to view stylized facts as properties *emerging* from the collective behavior of a large number of market participants. In all the cases, stylized empirical properties of asset returns serve as benchmarks for evaluating the plausibility of financial models before any estimation or testing is done.

## **References**

- [1] A¨ıt-Sahalia, Y. (1998). Dynamic equilibrium and volatility in financial asset markets, *Journal of Econometrics* **84**, 93–128.
- [2] Andersen, T. & Bollerslev, T. (1997). Intraday periodicity and volatility persistence in financial markets, *Journal of Empirical Finance* **4**, 115–158.
- [3] Aydemir, C., Gallmeyer, M. & Hollifield, B. (2007). *Financial Leverage and the Leverage Effect: A Market and Firm Analysis*. Working Paper 2007-031, Carnegie Mellon University.
- [4] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-Gaussian Ornstein-Uhlenbeck based models and some of their uses in financial econometrics, *Journal of the Royal Statistical Society Series B* **63**, 167–241.
- [5] Bollerslev, T., Chou, R. & Kroner, K. (1992). ARCH modeling in finance, *Journal of Econometrics* **52**, 5–59.
- [6] Bouchaud, J.-P., Matacz, A. & Potters, M. (2001). The leverage effect in financial markets: retarded volatility and market panic, *Physical Review Letters* **87**, 2287–2301.
- [7] Bouchaud, J. & Potters, M. (1997). *Th´eorie des Risques Financiers*, Alea, Saclay. ´
- [8] Campbell, J., Lo, A. & McKinlay, C. (1996). *The Econometrics of Financial Markets*, Princeton University Press, Princeton.
- [9] Clark, P.K. (1973). A subordinated stochastic process model with finite variance for speculative prices, *Econometrica* **41**, 135–155.
- [10] Cont, R. (2001). Empirical properties of asset returns: stylized facts and statistical issues, *Quantitative Finance* **1**, 1–14.
- [11] Cont, R. (2005). Volatility clustering in financial markets: empirical facts and agent-based models, in *Long*

*Memory in Economics*, A. Kirman & G. Teyssiere, eds, Springer, Berlin.

- [12] Cont, R., Bouchaud, J.-P. & Potters, M. (1997). Scaling in financial data: stable laws and beyond, in *Scale Invariance and Beyond*, B. Dubrulle, F. Graner & D. Sornette, eds, Springer, Berlin.
- [13] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman & Hall/CRC Press.
- [14] Engle, R. (ed.) (1995). ARCH: selected readings, in *Advanced Texts in Econometrics*, Oxford University Press.
- [15] Engle, R. & Ng, V. (1993). Measuring and testing the impact of news on volatility, *Journal of Finance* **48**, 1749–1778.
- [16] Fama, E. (1965). The behavior of stock market prices, *Journal of Business* **38**, 34–105.
- [17] Guillaume, D., Dacorogna, M., Dave, R., M ´ uller, U., ¨ Olsen, R. & Pictet, O. (1997). From the birds eye view to the microscope: a survey of new stylized facts of the intraday foreign exchange markets, *Finance and Stochastics* **1**, 95–131.
- [18] Guillaume, D., Dacorogna, M., Dave, R., M ´ uller, U., ¨ Olsen, R. & Pictet, O. (1997). Volatilities at different time resolutions: analyzing the dynamics of market components, *Journal of Empirical Finance* **4**, 213–239.
- [19] Heyde, C. & Kou, S. (2004). On the controversy over tailweight of distributions, *Operations Research Letters* **32**, 399–408.
- [20] Hols, M. & De Vries, C. (1991). The limiting distribution of extremal exchange rate returns, *Journal of Applied Econometrics* **6**, 287–302.
- [21] LeBaron, B. (2000). Agent-based computational finance: suggested readings and early research, *Journal of Economic Dynamics and Control* **24**, 679–702.
- [22] LeBaron, B. (2001). Stochastic volatility as a simple generator of apparent financial power laws and long memory, *Quantitative Finance* **1**, 621–631.
- [23] Longin, F. (1996). The asymptotic distribution of extreme stock market returns, *Journal of Business* **69**, 383–408.
- [24] Longin, F. (2005). The choice of the distribution of asset prices : how extreme value theory can help, *Journal of Banking and Finance* **29**, 1017–1035.
- [25] Mandelbrot, B.B. (1963). The variation of certain speculative prices, *Journal of Business* **XXXVI**, 392–417.
- [26] Mandelbrot, B.B. (1971). When can price be arbitraged efficiently? A limit to the validity of the random walk and martingale models, *The Review of Economics and Statistics* **53**, 225–236.
- [27] Mandelbrot, B.B., Calvet, L. & Fisher, A. (1997). *The Multifractality of the Deutschmark/US Dollar Exchange Rate*, Discussion paper 1166, Cowles Foundation for Economics, Yale University.
- [28] Muller, U., Dacorogna, M. & Pictet, O. (1998). ¨ Heavy tails in high-frequency financial data, in *A Practical Guide to Heavy Tails: Statistical Techniques for*

*Analysing Heavy Tailed Distributions*, R. Adler, R. Feldman & M. Taqqu, eds, Birkhauser, Boston, pp. 55–77. ¨

- [29] Officer, R. (1972). The distribution of stock returns, *Journal of the American Statistical Association* **67**, 807–812.
- [30] Pagan, A. (1996). The econometrics of financial markets, *Journal of Empirical Finance* **3**, 15–102.

## **Related Articles**

**Exponential Levy Models ´** ; **Extreme Value Theory**; **GARCH Models**; **Heavy Tails**; **Jump Processes**; **Long Range Dependence**; **Mixture of Distribution Hypothesis**; **Random Matrix Theory**; **Realized Volatility and Multipower Variation**; **Stochastic Volatility Models: Extremal Behavior**; **Stochastic Volatility Models**; **Time Change**; **Time-changed Levy Process ´** ; **Volatility**.

RAMA CONT
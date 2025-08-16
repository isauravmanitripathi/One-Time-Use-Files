# **Performance Measures**

The measurement of performance is the cornerstone of the evaluation of a fund. Since the advent of modern portfolio theory, it has been the focus of extensive practitioner and academic literature. We start by examining the hypothesis underlying the most commonly used measure, namely, the Sharpe ratio. We then present performance measures avoiding normality assumptions. The section on factor models analyzes the addition of multiple benchmarks for performance measurement. Finally, performance measures considering portfolio holdings are discussed.

#### **Sharpe Ratio**

The definition of the *ex post* Sharpe ratio (*see also* **Sharpe Ratio**) is as follows:

$$Sharpe = \frac{\bar{r}}{\sigma} \tag{1}$$

where *r*¯ is the average excess return over the riskfree rate and *σ* is the standard deviation of the excess return.

From a theoretical point of view, the Sharpe ratio finds its roots in the Capital Market Line, which weighs expected returns against the volatility. As a consequence, measuring performance with the *ex post* Sharpe ratio implicitly assumes that the return time series are normally distributed or that investor preferences can be described by a quadratic utility function. Moreover, the return time series need to be independently and identically distributed (i.i.d.) as shown in [11].

# **Performance Measures in the Absence of Normality**

Many asset classes, for example hedge funds, do not exhibit normally distributed returns. The use of derivatives has increased the potential of asymmetric behavior of investment strategies. The Sharpe ratio may be significantly increased in such circumstances ([18]). Moreover, this ratio does not reflect the preferences of risk-averse investors who tend to dislike negative skewness and high kurtosis (as shown in [14] and [16]).

As a remedy, new performance measures have emerged in order to cope with the absence of normality. The Sortino ratio, proposed by Sortino and Price [17], has been advocated to capture the asymmetry of the return distribution. It replaces the standard deviation in the Sharpe ratio by the downside deviation, which captures only the downside risk. The Sortino ratio is expressed as follows:

Sortino = 
$$\frac{\overline{R} - RMAR}{\text{Downside}(R, RMAR)}$$
 (2)

where *R* is the average return of the fund and *RMAR* is the minimum acceptable rate of return.

Downside(*R*, *RMAR*)  
= 
$$\sqrt{\frac{1}{T} \sum_{t} 1_{R_t < \textit{RMAR}} (R_t - \textit{RMAR})^2}$$
 (3)

The Stutzer index ([19]) does not rely explicitly on a utility function but on a behavioral hypothesis related to the "safety-first" principle of Roy [15]. It assumes that investors aim at minimizing the probability that the excess returns over a given threshold will be negative over a long time horizon. When the portfolio has a positive expected excess return, the aforementioned probability will exponentially decay to zero as the time horizon increases without limit irrespective of the threshold. The maximum possible decay is defined as the Stutzer index. More precisely, if the excess return process is i.i.d., the Stutzer index is expressed as follows:

$$I = -\lim_{T \to \infty} \frac{1}{T} \log (\text{Prob}[\bar{r}_T \le 0]) > 0 \tag{4}$$

where *r*¯*<sup>T</sup>* is the average excess return earned over the threshold periods.

It is interesting to note that for normal return distributions, the ranking of investments is exactly the same as with the Sharpe ratio. This is due to the fact that the Stutzer index is equal to half of the square of the Sharpe ratio in this case. In more general cases, higher moments of the distribution will have an impact on the value of the index. For example, a distribution with negative skewness and high kurtosis will result in a lower Stutzer index value than a normal distribution with the same mean and variance.

The Omega measure suggested by Keating and Shadwick [8] incorporates all the moments of the distribution by a direct transformation of the latter. More specifically, Omega provides a risk-reward measure for which returns are weighted by their probability of occurrence. In practice, the Omega function at a given threshold can be estimated as

$$\Omega(\text{Thres}) = \frac{\frac{1}{T} \sum_{t} \max(0, R_t - \text{Thres})}{\frac{1}{T} \sum_{t} \max(0, \text{Thres} - R_t)}\n$$
(5)

where *Rt* is the return of the fund at time *t* and Thres is the threshold defined by the investor.

The Omega function encodes the cumulative density function of the returns (see [8] for a proof). As a consequence, all moments are embodied in the function. In practice, investments may be difficult to rank with this performance measure. When the Omega function of a given investment dominates the Omega function of another, the investment second order stochastically dominates the other. All other possibilities lead to unclear results without defining risk preferences of the investors or without defining a specific metric on the Omega function.

# **Performance Measures** *versus* **Factor Models**

Factor models are widely used to decompose and analyze the performance of funds. A general model can be expressed as follows:

$$r_t = \alpha + \sum_i \beta_i F_{it} + \varepsilon_t \tag{6}$$

where *rt* is the excess return of the fund over the risk-free rate, *Fit* is the excess return of factor *i*, and *α* denotes the alpha of the fund.

Guided by the capital asset pricing model, Jensen [6, 7] uses a single market index as a benchmark. Merton's Intertemporal Capital Asset Pricing Model (ICAPM) [12] provides a theoretical framework for the presence of additional factors in equation (6). Fama and French [3] discovered purely empirical support for including a size (market capitalization) factor and a value (book-to-market ratio) factor, while Carhart [1] added a momentum factor. The emergence of hedge funds as an asset class has further refined the use of factor models. Fung and Hsieh [4] document that factor models are much poorer at decomposing hedge fund returns than at decomposing mutual fund returns. They show that hedge fund returns contain exposure to additional alternative factors.

The estimation of alpha is severely impacted by the length of the track record under consideration. Pastor and Stambaugh [13] propose a new methodology to increase the precision of the estimation and distinguish good managers from lucky ones. This methodology relies on information (returns) extracted from additional "seemingly unrelated" assets not used in the definition of the alpha. The additional nonbenchmark assets help estimate alpha if they are priced by the benchmarks or if their return histories are longer than that of the fund. Kosowski *et al.* [10] advocate a robust bootstrap approach for coping with the cross-sectional nonnormal distribution of individual fund alpha. Using both approaches, Kosowski *et al.* [9] show that persistence can be found in the alpha of top hedge fund managers.

# **Analysis Based on Portfolio Holdings Information**

When portfolio holdings are known, the analysis can be enhanced by looking at the relationship between the weights and the future returns of the portfolio components. More specifically, the performance measure is defined as

PerfHolding = 
$$\sum_{i} \text{cov}(w_{it-1}; R_{it})$$
 (7)

where *wit*<sup>−</sup><sup>1</sup> is the weight of underlying *i* at the end of period *t* − 1 and *Rit* is the return of underlying *i* between *t* − 1 and *t*.

Grinblatt and Titman [5] estimate equation (7) as

PerfHolding = 
$$\sum_{i} \frac{1}{T} \sum_{t} [w_{it-1} - E(w_{it-1})] R_{it}$$
(8)

where *E(wit*<sup>−</sup>1*)* refers to the benchmark weight of underlying *i*. In practice, the benchmark weight may be chosen as a long-run average.

Daniel *et al.* [2] introduce benchmarks to proxy characteristics of stocks in this context. They show that the gross return of an equity fund can be decomposed into three components:

$$CS_{t} = \sum_{i} w_{it-1} \left( R_{it} - R_{t}^{b_{it-1}} \right) \qquad (9)$$

Characteristic timing:

$$CT_{t} = \sum_{i} \left( w_{it-1} R_{it}^{b_{it-1}} - w_{it-k-1} R_{it}^{b_{it-k-1}} \right)$$
(10)

Average style measure:

$$AS_{t} = \sum_{i} w_{it-k-1} R_{it}^{b_{it-k-1}} \tag{11}$$

where  $R_t^{b_{it-1}}$  is the return of a value weighted portfolio that matches the characteristics of stock  $i$  at the end of period  $t-1$ . Wermers [20] documents the superiority of this approach *versus* the factor decomposition.

#### References

- [1] Carhart, M. (1997). On persistence in mutual fund performance, Journal of Finance 52, 57-82.
- Daniel, K., Grinblatt, M., Titman, S. & Wermers, R. [2] (1997). Measuring mutual fund performance with characteristic-based benchmarks, Journal of Finance 52, 1035-1058.
- Fama, E. & French, K. (1992). The cross-section [3] of expected stock returns, Journal of Finance 47(2), 427-465.
- [4] Fung, W. & Hsieh, D. (1997). Empirical characteristics of dynamic trading strategies: the case of hedge funds, Review of Financial Studies 10, 275-302.
- Grinblatt, M. & Titman, S. (1993). Performance mea-[5] surement without benchmarks: an examination of mutual fund returns, Journal of Business 66, 47-68.
- [6] Jensen, M. (1968). The performance of mutual funds in the period 1945-1964, Journal of Finance 23, 389-416.
- Jensen, M. (1969). Risk, the pricing of capital assets, [7] and the evaluation of investment portfolios, Journal of Business 42, 167-247.
- Keating, C. & Shadwick, F. (2002). A universal perfor-[8] mance measure, The Journal of Performance Measurement  $6(3)$ , 59-84.
- [9] Kosowski, R., Naik, N. & Teo, M. (2007). Do hedge funds deliver alpha? A Bayesian and bootstrap analysis, Journal of Financial Economics 84(1), 229–264.
- [10] Kosowski, R., Timmerman, A., Wermers, R. & White, H. (2006). Can mutual fund "stars" really pick stocks? New evidence from a bootstrap analysis, Journal of Finance 61(6), 2551-2595.

- [11] Lo, A. (2002). The statistics of Sharpe ratios, *Financial* Analysts Journal 58, 36-52.
- Merton, R. (1973). An intertemporal asset pricing model, [12] Econometrica 41. 867-887.
- [13] Pastor, L. & Stambaugh, R. (2002). Mutual fund performance and seemingly unrelated assets, Journal of Financial Economics 63(3), 315-349.
- [14] Pratt, J. & Zeckhauser, R. (1987). Proper risk aversion, Econometrica 55(1), 143-154.
- [15] Roy, A. (1952). Safety-first and the holding of assets, Econometrica 20, 431-449.
- [16] Scott, R. & Horvath, P. (1980). On the direction of preference for moments of higher order than the variance, Journal of Finance 35(4), 915-919.
- $[17]$ Sortino, F. & Price, L. (1994). Performance measurement in a downside risk framework, *Journal of Investing*  $3(3), 59-65.$
- [18] Spurgin, R. (2001). How to game your sharpe ratio, Journal of Alternative Investments  $4(3)$ ,  $38-46$ .
- [19] Stutzer, M. (2000). A portfolio performance index, Financial Analysts Journal 56(3), 52-61.
- Wermers, R. (2006). Performance evaluation with port-[20] folio holdings information, North American Journal of Economics and Finance 17, 207-230.

## **Further Reading**

- Ferson, W. & Schadt, R. (1996). Measuring fund strategy and performance in changing economic conditions, Journal of Finance 51, 425-461.
- Fung, W. & Hsieh, D. (2004). Hedge fund benchmarks: a risk based approach, Financial Analyst Journal 60, 65-80.
- Henriksson, R. & Merton, R. (1981). On market timing and investment performance II. Statistical procedures for evaluating forecasting skills, Journal of Business 54, 513-533.
- Lehmann, B. & Modest, D. (1987). Mutual fund performance evaluation: a comparison of benchmarks and benchmark comparisons. Journal of Finance 42, 233–265.
- Mamaysky, H., Spiegel, M. & Zhang, H. (2008). Estimating the dynamics of mutual fund alphas and betas, Review of Financial Studies 21, 233-264.
- Treynor, J. & Mazuy, K. (1966). Can mutual funds outguess the market? Harvard Business Review 44, 131-136.

## **Related Articles**

#### Sharpe Ratio; Style Analysis.

JEAN-FRANCOIS BACMANN & STEFAN SCHOLZ
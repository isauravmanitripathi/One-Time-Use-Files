### **CHAPTER 6**

# Performance and Capacity of High-Frequency Trading Strategies

Over the past few years, several studies attempted to measure highfrequency trading (HFT) performance and capacity. The results vary from author to author. Many different metrics have been developed over time to illuminate a strategy's performance. This chapter summarizes the most popular approaches for performance measurement and discusses strategy capacity and the length of time required to evaluate a strategy. The chapter also discusses estimation of capacity and illustrates capacity of HFT with specific examples.

## Principles of Performance Measurement

One can manage only something measurable. Performance measurement is therefore a critical function of investment management and of HFT. While many metrics developed for standard investment management apply well in a high-frequency setting, several other metrics have been developed specifically to evaluate HFT activity.

At the heart of a successful investment management of HFT lie three P's:

- Precision
- Productivity
- Performance

The first P, precision of mathematical metrics, refers to the exactitude required to quickly and reliably separate winning strategies from the losing ones. Statistical tools also help ascertain whether a strategy apparent profitability is a short-term fluke or a statistically solid predictor of performance.

Standardized metrics, when applied uniformly across all investment strategies, deliver the second P, productivity of the investment process. Statistical tools are highly scalable and can be rapidly deployed to optimize a diverse array of investing ideas.

The third P, performance, is particularly relevant to high-frequency systems. In an environment where data points from multiple sources arrive with nanosecond frequency, proper measuring systems are necessary. Monitoring systems equipped with the latest portfolio tracking and riskmanagement capabilities are critical for effective and sustainable investing.

The three P's share one key requirement: data. The simplest, least processed, data, such as tick data, is most informative and has consequently proven to be very valuable. Trade-by-trade data can reveal the short-term risks of the trading strategy, and to allow risk-mitigating approaches for strategy improvement. Additionally, most granular data allows to quickly and accurately identify strategy dependencies on specific market events or financial instruments, feeding back into strategy development and forming stronger, longer-lasting trading systems. Finally, tick data allow investment managers to monitor and evaluate performance of trading strategies in real time without losing the opportunity to limit losses and enhance profitability along the way.

### Basic Performance Measures

#### Return

Trading strategies may come in all shapes and sizes, but they share one characteristic that makes comparison across different strategies feasible return. Return can be expressed as a dollar difference in prices but is most often considered as a percentage change in value. The resulting dimensionless measure is independent of the price level of the financial instrument under consideration and allows easy cross-strategy and crossasset comparison of performance:

$$(1)^{R_{t1} = \frac{P_{t1}}{P_{t0}} - 1}$$

<span id="page-2-1"></span>Simple return of equation (1) is illustrated in [Figure 6.1](#page-2-0).

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

An equivalent log return metric is shown in equation (2):

(2)

It can be shown that at high frequencies, simple returns of equation (1) are nearly identical to log returns defined by equation (2). The choice of the return metric is often dependent on the application and mathematics of the estimation models.

### Volatility

Volatility of returns measures how much the return moves up and down around its average value. The movement of returns, often known as *dispersion,* is often taken as a measure of risk. Figures 6.2 and 6.3 illustrate low-volatility and high-volatility conditions, drawn comparatively to each other.

![](_page_3_Figure_0.jpeg)

At least a dozen measures of volatility exist, each metric assessed over a specific period of time: round-trip trade, minute, day, month, and so on. The most common measures of volatility include:

Simple standard deviation of returns is by far the most popular measure of volatility.

$$(3) \hat{\sigma}_{t}^{2} = \frac{1}{N} \sum_{i=1}^{N} \left( R_{t-i} - \overline{R_{t}} \right)^{2}$$

where is a simple average of *N* observations preceding time *t.*

Weighted average deviation, emphasizing later observations, is also used often:

$$\hat{\sigma}_{t}^{2} = \frac{\sum_{t=1}^{N} w_{t} \left(R_{t-t} - \overline{R}_{t}\right)^{2}}{\sum_{t=1}^{N} w_{t}}$$
(4)

where , and *w<sup>i</sup>* is the "data importance" weight corresponding

to each individual returns *R<sup>i</sup>* . All *w<sup>i</sup>* are often chosen to add up to 1 and to increase toward the most current observation:

$$(5) \sum_{i=1}^{N} w_i = 1$$

$$(6) w_i > w_{i+1} > w_{i+2} > \cdots > w_{i+N}$$

Average of open, high, low, and close prices is another metric of volatility

$$(7) \ \hat{\sigma_{t}} = \frac{P_{t-N} + \max(P_{\tau \in t-N, t-1}) + \min(P_{\tau \in t-N, t-1}) + P_{t-1}}{4}$$

High minus low recorded during a specific period of time is useful in analyses where many lagged variables are present. The high minus low metric avoids endogeneity problem inherent with standard deviation and lagged returns: since standard deviation is computed from lagged returns, the analysis comparing lagged returns and standard deviation is faulty by design.

$$(8) \hat{\sigma}_{t} = \max\left(P_{t \in t-N, t-1}\right) - \min\left(P_{t \in t-N, t-1}\right)$$

Average square returns recorded over a certain period of time is yet another metric of volatility. This one has been shown to work particularly well with applications like generalized autoregressive conditional heteroskedasticity (GARCH) (see Bollerslev, 2005):

(9) 
$$\hat{\sigma}_{t}^{2} = \frac{1}{N} \sum_{t=1}^{N} (R_{t-t})^{2}$$

### Drawdown

Drawdown is a measure of historical loss. It is recorded as a maximum loss relative to the highest previous value, the latter often referred to as the *water mark.* Investment managers typically receive performance fees only after they exceed the highest water mark on record.

Maximum drawdown identifies the biggest drop of price or value in history of the investment, and helps illustrate potential downside risk. [Figures 6.4](#page-5-0) and 6.5 illustrate computation of maximum drawdown.

<span id="page-5-1"></span><span id="page-5-0"></span>**[Figure 6.4](#page-5-1)** Maximum Drawdown Computation, Scenario 1

![](_page_5_Figure_4.jpeg)

![](_page_6_Figure_0.jpeg)

**Figure 6.5** Maximum Drawdown Computation, Scenario 2

Formally, maximum drawdown is a measure of tail risk popular among practitioners that documents the maximum severity of losses observed in historical data. As such, maximum drawdown records the lowest peak-totrough return from the last global maximum to the minimum that occurred prior to the next global maximum that supersedes the last global maximum. The global maximum measured on the past data at any point in time is known as *high water mark.* A drawdown is then the lowest return in between two successive high water marks. The lowest drawdown is known as the maximum drawdown:

(10)

In risk management, the concept of maximum drawdown is closely related to value-at-risk, a measure of worst quantity of losses, described in detail in Chapter 14.

#### Win Ratio

Win ratio explains what portion of the trades, trading days or trading months ended profitably:

(11)

Win ratios help compare accuracy of predictive signals of strategies: better forecasts result in higher win ratios. Win ratios also help in monitoring run-time performance. As a simplest metric, win ratio can be used to assess whether present performance record is consistent with prior performance. A decline in the win ratio may indicate that the strategy is reaching capacity, as [Figure 6.6](#page-7-0) illustrates.

<span id="page-7-0"></span>**[Figure 6.6](#page-7-1)** A Decline in Win Ratio Shown May Indicate that the Strategy Is Reaching Capacity

![](_page_7_Figure_3.jpeg)

<span id="page-7-1"></span>

Similar, but more advanced, tests for evaluating consistency of run-time performance are described in Chapter 14.

### Average Gain/Loss

Average gain and average loss are two metrics, statistically closely related to maximum drawdown. The average loss is also a close cousin of the concept of expected loss, discussed in Chapter 14. The average gain

measures the average profitability of the strategy when a positive result is recorded. Similarly, the average loss computes the average total for all trades, days or months when the strategy delivered negative performance.

Considered in conjunction with the win ratio, average gain and loss metrics may deliver additional insights. For example, a strategy with high win ratio may tolerate lower average gain relative to the observed average loss, while low win ratio requires a high average gain as compared with the average loss. The outcomes of various win ratio and average gain/loss combinations are shown in [Figure 6.7.](#page-8-0)

<span id="page-8-0"></span>

|  | Figure 6.7 Outcomes of Win Ratio and Average Gain/Loss Combinations |  |  |  |  |
|--|---------------------------------------------------------------------|--|--|--|--|
|  |                                                                     |  |  |  |  |

<span id="page-8-1"></span>

|                | High<br>WinRatio   | Low<br>WinRatio   |
|----------------|--------------------|-------------------|
| High Gain/Loss |                    | High<br>drawdowns |
| Low Gain/Loss  | High<br>volatility | X                 |

Formally, for the strategy to deliver positive performance, the following inequality must hold:

(12)

The inequality of equation (12) can be used as first step litmus test for evaluating performance of candidate investing strategies and manager credibility.

#### Correlation

Correlation measures co-movement of strategy returns with those of another strategy or financial instrument:

(13)

When two strategies with low correlation are combined in a portfolio, traditional portfolio management theory suggests that the resulting portfolio is diversified (i.e., allows one strategy to pull up returns when performance of another strategy temporarily declines).

Simple correlation, however, may no longer be sufficient in delivering robust measurements of co-movement of financial instruments. The main problem with simple correlation is the following observation: prices of financial instruments display increasingly divergent correlations in rising and in falling markets. Specifically, when broad market indices rise (a market entity such as Standard & Poor's [S&P] 500, for example) correlations vary from any two financial instruments to any other two financial instruments. When the broad market indices fall, however, returns of most financial instruments become highly correlated. Such divergent correlation in different states of the markets is known as the *asymmetric* or *tail correlation* that can be computed by dividing the data sample into points when price returns of one of the instruments measured are positive and negative:

$$(14)^{\rho_{1,2}}\Big|_{R_{1}>0} = \sum_{t} \Big(R_{1,t} - \mathbb{E}[R_{1}]\Big) \Big(R_{2,t} - \mathbb{E}[R_{2}]\Big)\Big|_{R_{1}>0}$$
$$(15)^{\rho_{1,2}}\Big|_{R_{1}<0} = \sum_{t} \Big(R_{1,t} - \mathbb{E}[R_{1}]\Big) \Big(R_{2,t} - \mathbb{E}[R_{2}]\Big)\Big|_{R_{1}<0}$$

In both equations (14) and (15) financial instrument 1 is taken as a reference. Equation (14) computes the correlation for the "up" states of returns of financial instrument 1, while equation (15) does the same for the "down" states. A strategy delivering returns negatively correlated to those of the existing portfolio helps buffer core portfolio's losses in the "down" states, and is much more valuable than the strategy delivering positively correlated returns and thereby amplifying losses of wider portfolio.

### Alpha and Beta

Alpha and beta are two now-mainstay measures of investment performance that are equally well suited for evaluation of high-frequency strategies. At its most basic level, alpha measures the return achieved by the strategy abstracted of any influences by the reference portfolio or the broader markets, measured by, say, the S&P 500 index. Thus, alpha reflects the performance of the strategy that is independent of the prevailing market conditions. A positive alpha is desirable. Strategies with a negative alpha are generally avoided, unless the negative-alpha strategy signals can be profitably used to trade "in reverse"—buy when the strategy advises to sell and vice versa.

Beta, however, is a multiplier that measures exactly how the strategy responds to the current market trends. A positive beta indicates that the strategy is likely to deliver positive performance when the reference portfolio rises in value. A negative beta shows that, on average, the strategy is likely to perform better when the reference portfolio declines. Depending on the investor's cumulative portfolio, either positive or negative beta may be preferable.

Alpha and beta are estimated using a linear regression (OLS):

(16)

where *Ri,t* is the return on a high-frequency strategy *i* observed over a unit of time *t*, *Rp,t* is the return on the reference portfolio observed over the same period of time, *α<sup>i</sup>* and *β<sup>i</sup>* are the parameters to be estimated, and ε*i,t* is the "statistical estimation error" specific to each observation when equation (16) is applied to data. By the assumptions of the model of equation (16), the errors ε*i,t* average to zero.

Figure 6.8 graphically illustrates alpha and beta, as computed from a scatterplot of returns: the returns of the reference portfolio are plotted along the horizontal axis, and the contemporaneous returns on the HF strategy are plotted along the vertical axis. When a straight line is fitted through the data, the slope of the line is beta. Alpha is the intercept, or the point where the line intersects the vertical axis.

![](_page_11_Figure_0.jpeg)

#### Skewness and Kurtosis

Skewness and kurtosis are additional parameters used to describe the distribution of returns of the strategy. *Skewness* describes the tendency of the strategy to deliver positive or negative returns. Positive skewness of a return distribution implies that the strategy is more likely to post positive returns than negative returns. Figure 6.9 illustrates possible skewness scenarios.

![](_page_12_Figure_0.jpeg)

**Figure 6.10** Kurtosis Values and Their Meaning in Distribution of Returns

![](_page_13_Figure_1.jpeg)

*Kurtosis* measures the likelihood of extreme occurrences, that is, of severely positive and severely negative returns relative to normal returns. When kurtosis is high, extreme returns are likely. When kurtosis is low, extreme returns are unlikely. Figure 6.10 illustrates the idea of kurtosis.

The average return, volatility, and maximum drawdown over a prespecified window of time measured at a predefined frequency are the mainstays of performance comparison and reporting for different trading strategies. In addition to the average return, volatility, and maximum drawdown, practitioners sometimes quote skewness and kurtosis of returns when describing the shape of their return distributions. As usual, skewness illustrates the position of the distribution relative to the return average;

positive skewness indicates prevalence of positive returns, while negative skewness indicates that a large proportion of returns is negative. Kurtosis indicates whether the tails of the distribution are normal; high kurtosis signifies "fat tails," a higher-than-normal probability of extreme positive or negative events.

## <span id="page-14-1"></span>Comparative Ratios

While average return, standard deviation, and maximum drawdown present a picture of the performance of a particular trading strategy, the measures do not lend to an easy point comparison among two or more strategies. Several comparative performance metrics have been developed in an attempt to summarize mean, variance, and tail risk in a single number that can be used to compare different trading strategies. [Table 6.1](#page-14-0) summarizes the most popular point measures.

<span id="page-14-0"></span>**[Table 6.1](#page-14-1)** Performance Measure Summary

| Sharpe ratio<br>(Sharpe, 1966)      | $SR = \frac{E[r] - r_f}{\sigma[r]}$ , where                                                                                                                                                                               | Adequate if returns are normally<br>distributed.                                                                                                                                                                                                                                                  |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                     | $E[r] = \frac{r_1 + \dots + r_T}{T}$<br>$\sigma[r] = \sqrt{\frac{(r_{\rm I} - E[r])^2 + \dots + (r_{\rm T} - E[r])^2}{T - 1}}$<br>The Sharpe ratio of high-frequency trading<br>strategies: $SR = \frac{E[r]}{\sigma[r]}$ |                                                                                                                                                                                                                                                                                                   |
| Treynor ratio<br>(Treynor, 1965)    | $T_{\text{reynor}_i} = \frac{E[r_i] - r_f}{\beta}$<br>$\beta$ is the regression coefficient of trading<br>returns on returns of the investor's reference<br>portfolio, such as the market portfolio.                      | Adequate if returns are normally<br>distributed and the investor wishes to split<br>his holdings between one trading strategy<br>and the market portfolio.                                                                                                                                        |
| Jensen's alpha<br>(Jensen, 1968)    | $\alpha_i = E[r_i] - r_f - \beta_i (r_M - r_f)$<br>$\beta$ is the regression coefficient of trading<br>returns on returns of the investor's<br>reference portfolio, such as the market<br>portfolio.                      | Measures trading return in excess of the<br>return predicted by CAPM, Adequate<br>if returns are normally distributed and<br>the investor wishes to split his holdings<br>between one trading strategy and the<br>market portfolio, but can be manipulated<br>by leveraging the trading strategy. |
| LPM of order $n$ for security $i$ : | Measures based on lower partial moments (LPMs);<br>$LPM_{ni}(\tau) = \frac{1}{T} \sum_{r}^{i} \max[\tau - r_{ir}, 0]^{n}$                                                                                                 |                                                                                                                                                                                                                                                                                                   |

where  $\tau$  is the minimal acceptable return;

n is the moment:  $n = 0$  is the shortfall probability,  $n = 1$  is the expected shortfall,  $n = 2$  for  $\tau = E[r]$  is the semivariance.

According to Eling and Schuhmacher (2007), more risk-averse investors should use higher-order n. LPMs consider only negative deviations of returns from a minimal acceptable return. As such, LPMs are deemed to be a better measure of risk than standard deviation, which considers both positive and negative deviations (Sortino and van der Meer, 1991). Minimal acceptable return can be zero, risk-free rate, or average return.

| Omega<br>(Shadwick and<br>Keating, 2002;<br>Kaplan and<br>Knowles, 2004) | $\Omega_{\rm i} = \frac{E[\tau] - \tau}{LPM_{\rm i}(\tau)} + 1$                                                                | $E[\tau] - \tau$ is the average return in excess of<br>the benchmark rate.                                                                                       |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sortino ratio<br>(Sortino and<br>van der Meer,<br>(1991)                 | $Sortino_i = \frac{E[t_i] - t}{\left(LPM_-(\tau)\right)^{1/2}}$                                                                |                                                                                                                                                                  |
| Карра 3<br>(Kaplan and<br>Knowles, 2004)                                 | $\text{K3}_{i} = \frac{E[r_{i}] - i}{\left(LPM_{2}(\tau)\right)^{1/3}}$                                                        |                                                                                                                                                                  |
| Upside<br>Potential ratio<br>(Sortino, van<br>der Meer, and              | $UPR_{i} = \frac{HPM_{1i}(\tau)}{(IPM_{i}(\tau))^{1/2}}$                                                                       | According to Eling and Schuhmacher<br>(2007), this ratio gains from the<br>consistent application of the minimal<br>acceptable return $\tau$ in the numerator as |
| Plantinga, 1999)                                                         | where $HPM$ = higher partial moment<br>$\text{HPM}_{\text{net}}(\tau) = \frac{1}{T} \sum_{i=1}^{T} \max[r_{it} - \tau, 0]^{n}$ | well as in the denominator.                                                                                                                                      |

Measures based on drawdown; frequently used by CTAs, according to Eling and Schuhmacher (2007, p.5), "because these measures illustrate what the advisors are supposed to do best-continually accumulating gains while consistently limiting losses (see Lhabitant, 2004)."  $\textit{MD}_{\text{cl}}$  denotes the lowest maximum drawdown,  $MD_{a}$  the second lowest maximum drawdown, and so on.

| Calmar ratio<br>(Young, 1991)       | $\text{Calmar}_i = \frac{E[r_i] - r_f}{-MD_{i1}}$                                         | $MD_{\cdot}$ , is the maximum drawdown.                                                                                                                                |
|-------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sterling ratio<br>(Kestner, 1996)   | $\text{Sterling}_{i} = \frac{E[r_{i}] - r_{f}}{-\frac{1}{N} \sum_{k=1}^{N} MD_{y}}$       | $-\frac{1}{N}\sum_{k=1}^{N}MD_{ij}$<br>is the average maximum<br>drawdown.                                                                                             |
| <b>Burke ratio</b><br>(Burke, 1994) | $Barke_i = \frac{E[r_i] - r_f}{\left[\sum_{i=1}^{N} \left(MD_{ij}\right)^2\right]^{1/2}}$ | $\left[\sum_{k=1}^{N} \left(MD_{y}\right)^{2}\right]^{1/2}$<br>is a type of variance<br>below the N <sup>th</sup> largest drawdown; accounts<br>for very large losses. |

Value-at-risk-based measures.

 $Value\text{-}at\text{-}risk$  ( $VaR_i$ ) describes the possible loss of an investment, which is not exceeded with a given probability of  $1-\alpha$  in a certain period. For normally distributed returns,  $VaR_i = -(E[r_i] + z_\alpha \sigma_i)$ , where  $z_{\alpha}$  is the  $\alpha$ -quantile of the standard normal distribution,

| Excess return<br>on value at risk<br>(Dowd, 2000)          | Excess R on $VaR = \frac{E[r] - r_f}{r_f}$<br>VaR                       | Not suitable for non-normal returns.                                                              |
|------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Conditional<br>Sharpe ratio<br>(Agarwal and<br>Naik, 2004) | $Conditional \; Shape = \frac{E[r] - r_f}{CVaR_i}$                      | The advantage of CVaR is that it satisfies<br>certain plausible axioms (Artzner et al.,<br>1999). |
|                                                            | $CVaR = E[-\varepsilon_{\bullet} \mid \varepsilon_{\bullet} \leq -VaR]$ |                                                                                                   |

| Gueyie (2003)<br>Cornish-Fisher expansion is calculated as<br>follows:<br>$MVaR_{i} = -(E[r_{i}] + \sigma_{i}(z_{\alpha} + (z_{\alpha}^{2} - 1)S_{i}/6)$<br>$+(z_{\alpha}^{3}-3z_{\alpha})EK_{\alpha}/24-(2z_{\alpha}^{3}-5z_{\alpha})S_{\alpha}^{2}/36)$<br>where $S_i$ denotes skewness and $EK$ the<br>excess kurtosis for security i (Favre and<br>Galeano, 2002). |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|

The first generation of point performance measures were developed in the 1960s and include the Sharpe ratio, Jensen's alpha, and the Treynor ratio. The Sharpe ratio is probably the most widely used measure in comparative performance evaluation; it incorporates three desirable metrics—average return, standard deviation, and the cost of capital borrowed for strategy leverage.

The Sharpe ratio was designed in 1966 by William Sharpe, later a winner of the Nobel Memorial Prize in Economics; it is a remarkably enduring concept used in the study and practice of finance. A textbook definition of the Sharpe ratio is

, where is the annualized average return from trading, σ*<sup>R</sup>* is the annualized standard deviation of trading returns, and *R<sup>F</sup>* is the risk-free rate (e.g., Fed Funds) that is included to capture the opportunity cost as well as the position carrying costs associated with the trading activity. It should be noted that in most instruments HFT with no positions carried overnight, the position carrying costs are zero. Therefore, the high-frequency Sharpe ratio is computed as follows:

$$SR = \frac{\overline{R}}{\sigma_R}$$

What makes the Sharpe ratio an appealing measure of performance, in comparison with, say, raw absolute return? Surprisingly, the Sharpe ratio is an effective metric for selecting mean-variance efficient securities.

Consider Figure 6.11, for example which illustrates the classic meanvariance frontier. In the figure, the Sharpe ratio is the slope of the line emanating from the risk-free rate and passing through a point corresponding to a given portfolio (*M* for market portfolio), trading strategy, or individual security. The bold line tangent to the mean-variance set of all portfolio

combinations is the efficient frontier itself. It has the highest slope and, correspondingly, the highest Sharpe ratio of all the portfolios in the set. For any other portfolio, trading strategy, or individual financial instrument *A*, the higher the Sharpe ratio, the closer the security is to the efficient frontier.

**Figure 6.11** Sharpe Ratio as a Mean-Variance Slope. The market portfolio has the highest slope and, correspondingly, the highest Sharpe ratio.

![](_page_18_Figure_2.jpeg)

Sharpe himself came up with the metric when developing a portfolio optimization mechanism for a mutual fund for which he was consulting. Sharpe's mandate was to develop a portfolio selection framework for the fund with the following constraint: no more than 5 percent of the fund's portfolio could be allocated to a particular financial security. Sharpe then created the following portfolio solution: he first ranked the security universe on what now is known as Sharpe ratio, then picked the 20 securities with the best performance according to the Sharpe ratio measure,

and invested 5 percent of the fund into each of the 20 securities. Equally weighted portfolio allocation in securities with the highest Sharpe ratios is just one example of a successful Sharpe ratio application.

Jensen's alpha is a measure of performance that abstracts from broad market influences, capital asset pricing model (CAPM)-style. Jensen's alpha implicitly takes into consideration the variability of returns in co-movement with chosen market indices.

The third ratio, the Treynor ratio, measures the average return in excess of the chosen benchmark per unit of risk proxied by beta from the CAPM estimation.

While these three metrics remain popular, they do not take into account the tail risk of extreme adverse returns. Brooks and Kat (2002), Mahdavi (2004), and Sharma (2004), for example, present cases against using Sharpe ratios on non–normally distributed returns. The researchers' primary concerns surrounding the use of the Sharpe ratio are linked to the use of derivative instruments that result in an asymmetric return distribution and fat tails. Ignoring deviations from normality may underestimate risk and overestimate performance. New performance measures have been subsequently developed to capture the tail risk inherent in the returns of most trading strategies.

A natural extension of the Sharpe ratio is to change the measure of risk from standard deviation to a drawdown-based methodology in an effort to capture the tail risk of the strategies. The Calmar ratio, Sterling ratio, and Burke ratio do precisely that. The Calmar ratio, developed by Young (1991), uses the maximum drawdown as the measure of volatility. The Sterling ratio, first described by Kestner (1996), uses the average drawdown as a proxy for volatility. Finally, the Burke ratio, developed by Burke (1994), uses the standard deviation of maximum drawdowns as a volatility metric.

In addition to ignoring the tail risk, the Sharpe ratio is also frequently criticized for including positive returns in the volatility measure. The argument goes that only the negative returns are meaningful when estimating and comparing performance of trading strategies. In response, a "Greek" class of ratios extended the Sharpe ratio by replacing volatility with the average metrics of adverse returns only. These adverse return

metrics are known as lower partial moments (LPMs) and are computed as regular moments of a distribution (i.e., mean, standard deviation, and skewness), except that the data used in computation comprises returns below a specified benchmark only. Thus, a metric known as Omega, developed by Shadwick and Keating (2002) and Kaplan and Knowles (2004), replaces the standard deviation of returns in the Sharpe ratio calculation with the first LPM, the average of the returns that fell below the selected benchmark. The Sortino ratio, developed by Sortino and van der Meer (1991), uses the standard deviation of the returns that fell short of the benchmark, the second LPM, as a measure of return volatility in the Sharpe ratio calculation. The Kappa 3 measure, developed by Kaplan and Knowles (2004), replaces the standard deviation in the Sharpe ratio with the third LPM of the returns, the skewness of the returns below the benchmark. Finally, the Upside Potential ratio, produced by Sortino, van der Meer, and Platinga (1999), measures the average return above the benchmark (the first higher partial moment) per unit of standard deviation of returns below the benchmark.

Value-at-risk (VaR) measures, discussed in detail in Chapter 14, also gained considerable popularity as metrics able to summarize the tail risk in a convenient point format within a statistical framework. The VaR measure essentially identifies the 90 percent, 95 percent, or 99 percent Z-score cutoff in distribution of returns (the metric is also often used on real dollar distributions of daily profit and loss). A VaR companion measure, the conditional VaR (CVaR), also known as expected loss (EL), measures the average value of return within the cutoff tail. Of course, the original VaR assumes normal distributions of returns, whereas the returns are known to be fat-tailed. To address this issue, a modified VaR (MVaR) measure was proposed by Gregoriou and Gueyie (2003) and takes into account deviations from normality. Gregoriou and Gueyie (2003) also suggest using MVaR in place of standard deviation in Sharpe ratio calculations.

How do these performance metrics stack up against each other? It turns out that all metrics deliver comparable rankings of trading strategies. Eling and Schuhmacher (2007) compare hedge fund ranking performance of the 13 measures listed and conclude that the Sharpe ratio is an adequate measure for hedge fund performance.

## Performance Attribution

Performance attribution analysis, often referred to as "benchmarking," goes back to the arbitrage pricing theory of Ross (1977) and has been applied to trading strategy performance by Sharpe (1992) and Fung and Hsieh (1997), among others. In a nutshell, performance attribution notes that *t-*period return on strategy *i* that invests into individual securities with returns *rjt* in period *t*, with *j* = 1, …, *J*, has an underlying factor structure:

$$R_{it} = \sum_{j} x_{jt} r_{jt}$$

where *xjt* is the relative weight of the *j*th financial security in the portfolio at time *t*,

. The *j*th financial security, in turn, has a period-*t* return that can be explained by *K* systematic factors:

$$(18) \, r_{jt} = \sum_{k} \lambda_{jk} F_{kt} + \varepsilon_{jt}$$

where *F*kt is one of *K* underlying systematic factors in period *t*, *k* = 1, …, *K*, l is the factor loading, and e*jt* is the security *j* idiosyncratic return in period *t*. Following Sharpe (1992), factors can be assumed to be broad asset classes, as well as individual stocks or other securities. Combining equations (17) and (18), we can express returns as follows:

$$R_{it} = \sum_{j,k} x_{jt} \lambda_{jk} F_{kt} + \sum_{j} x_{jt} \varepsilon_{jt}$$

reducing the large number of financial securities potentially underlying strategy *i*'s returns to a small group of global factors. Performance attribution to various factors then involves regressing the strategy's returns on a basket of factors:

$$R_{it} = \alpha_i + \sum_k b_{ik} F_{kt} + u_{it}$$

where *b*<sup>k</sup> measures the performance of the strategy that can be attributed to factor *k*, *α<sup>i</sup>* measures the strategy's persistent ability to generate abnormal returns, and *uit* measures the strategy's idiosyncratic return in period *t.*

In the performance attribution model, the idiosyncratic value added of the strategy is the strategy's return in excess of the performance of the basket of weighted strategy factors.

Fung and Hsieh (1997) find that the following eight global groups of asset classes serve well as performance attribution benchmarks:

- Three equity classes: MSCI U.S. equities, MSCI non–U.S. equities, and IFC emerging market equities
- Two bond classes: JPMorgan U.S. government bonds and JPMorgan non–U.S. government bonds
- One-month Eurodollar deposit representing cash
- The price of gold proxying commodities and the Federal Reserve's trade-weighted dollar index measuring currencies in aggregate.

Performance attribution is a useful measure of strategy returns for the following reasons:

- The technique may accurately capture investment styles of black-box strategies in addition to the details reported by the designer of the strategy.
- Performance attribution is a measure of true added value of the strategy and lends itself to easy comparison with other strategies.
- Near-term persistence of trending factors allows forecasting of strategy performance based on performance attribution (see, for example, Jegadeesh and Titman, 2001).

The bottom line in the performance attribution analysis is this: if the highfrequency strategy under consideration exhibits high dependency on a benchmark, it may be cheaper to invest into the benchmark instead of the HF strategy, particularly when development and transaction costs as well as the associated risks are taken into account. That is, when the performance attribution beta is high, and alpha is low, it might be more effective to invest into the benchmark, particularly when any one of the following conditions holds:

- Investing into benchmark can be passive or simply costs less in terms of aggregate transaction costs.
- The benchmark has lower drawdown risk.
- The benchmark is more liquid than the instrument traded in the HFT strategy, and the benchmark therefore faces a lower liquidation risk.

## Capacity Evaluation

Over the past few years, HFT strategies have been erroneously called lowcapacity strategies. One study, for example, based its low-capacity conclusions for HFT on a major gaffe—an assumption that all highfrequency traders solely use market orders to complete their trades. In such an analysis, market impact dominates and multiplies in fast trading, leaving high-frequency traders unable to profitably enter or liquidate their positions. The maximum capacity of a high-frequency market-order trading strategy then amounts to the liquidity available at the best bid or best offer at a specific time when each market sell or buy order, respectively, is placed.

In reality, as later chapters of this book describe, most HFT strategies place and execute limit orders, with very few market orders placed in the mix. Market orders in HFT are generally used at times when markets take an unexpected wrong turn and the trader's inventory has to be liquidated fast.

Limit orders generate much smaller market impact than do market orders, as Chapter 5 of this book explains. Still, even strategies relying solely on limit orders do not enjoy infinite capacity since two variables in addition to market impact also adversely affect performance of HFT strategies. These variables are probability of execution and transparent execution costs.<sup>1</sup>

Transparent execution costs, also described in Chapter 5 of this book, affect the profitability of round-trip trades, yet are predictable as they tend to be known ahead of each trade. Execution costs on selected venues may be positive or negative, depending on the venue's business model.

The probability of execution is simple for market orders: it is always close to 1. The probability of execution of limit orders, however, is not known with certainty at the time the order is placed. For a limit order to be executed, it needs to

1. Become the best available price—best bid or best ask—the process also known as "reaching the top of the book."

2. Be matched with or *crossed* by a market order or an aggressive limit order.

As a result, the probability of execution for limit orders is variable and depends on the following factors:

- The distance of the limit order price from the market price.
- Market volatility.
- The number of other limit orders available at the same price or closer to market.
- The size of the limit order.
- The rate of arrival of same-side limit orders.
- The rate of arrival of opposing market orders and aggressive limit orders.

A limit order placed far away from the market price faces a tangible risk of nonexecution: the market price may never reach limit orders placed far away from the market. The probability of the market price crossing the limit order, in turn, depends on the market volatility—the higher the volatility, the more likely is the market price to hit the level specified by the limit order. The congestion of limit orders also matters, as each limit placed at a given price will be stored in a queue and executed according to a scheme specific to the execution venue; as discussed in Chapter 3, the most common matching schemes are the first-in-first-out (FIFO) and pro-rata algorithms. Under the FIFO arrangements, the larger limit orders face a larger risk of nonexecution: large limit orders may be only partially executed before the market moves away, leaving some of the limit order in the queue. With a pro-rata algorithm, the opposite holds: all orders are executed on a fixed proportion of their sizes; small orders may take a long time to execute in full.

The higher the number of other limit orders arriving at the same price as the trader's close to market price, the steeper the competition for market orders, and the less likely the limit order to be matched. However, the higher the arrival rate of opposing market orders, the higher the probability of execution.

Algebraically, the maximum size of a limit order (capacity) *S* deployed by a high-frequency strategy can be expressed as follows:

$$(21)^{\max S_{s,t}} \sum_{t} \left[ SQ_{t} \left( 1 + MI_{t-1} \right) P_{t} Pr_{t} \left( \text{Execution} \right) - C_{t} \right] \ge 0 \text{ and } \sum_{t} Q_{t} = 0$$
where

*S* is the size of each order in the strategy, assuming the strategy can be executed using trades of equal size *S.*

is the direction of the order placed at time *t*: when the order is a buy, and when the order is a sell.

 is the market impact generated by the previous order placed by the HFT strategy, and impacting the market conditions at time *t*; only the market impact that has not fully decayed by time *t* needs to be considered.

*Pt* is the price of the order or, in case of a market order, the price obtained upon execution.

 is the probability that the order placed at time *t* will be executed; this probability can be assumed to be 1 for market orders.

Finally, *C<sup>t</sup>* is the cost of execution of the order placed at time *t*; this cost includes broker fees and other costs discussed in Chaper 5 of this book that affect the bottom-line profitability of high-frequency strategies.

As shown in Chapter 5, market impact (MI) can be probabilistically estimated. In addition to the magnitude of MI following an average order, the probability of execution can be estimated as well by noting the statistics of when a market price crosses limit orders placed at various points away from the market. Assuming that the trade signals of an HFT system deliver credibly positive results, the capacity of the system is then determined by a trade-off between market impact and probability of execution.

To further increase the capacity of an HFT strategy, market and limit orders may be potentially sequenced. Figure 6.12 shows a decision tree for evaluating the optimal capacity of an HF trading system.

![](_page_26_Figure_0.jpeg)

Ding et al. (2008) conjecture that when the amount of capital deployed is lower than the strategy capacity, the strategy performance may be positively related to its capitalization. However, once capitalization exceeds strategy capacity, performance becomes negatively related to the amount of capital involved. Chapter 15 discusses the latest research on optimizing order execution and potentially increasing strategy capacity further.

### Length of the Evaluation Period

Most portfolio managers face the following question in evaluating candidate trading strategies for inclusion in their portfolios: how long does one need to monitor a strategy in order to gain confidence that the strategy produces the Sharpe ratio advertised?

Some portfolio managers have adopted an arbitrarily long evaluation period: six months to two years. Some investors require a track record of at least six years. Yet others are content with just one month of daily performance data. It turns out that, statistically, any of the previously mentioned time frames is correct if it is properly matched with the Sharpe ratio it is intended to verify. The higher the Sharpe ratio, the shorter the

strategy evaluation period needed to ascertain the validity of the Sharpe ratio.

If returns of the trading strategy can be assumed to be normal, Jobson and Korkie (1981) showed that the error in Sharpe ratio estimation is normally distributed with mean zero and standard deviation

For a 90 percent confidence level, the claimed Sharpe ratio should be at least 1.645 times greater than the standard deviation of the Sharpe ratio errors, *s.* As a result, the minimum number of evaluation periods used for Sharpe ratio verification is

The Sharpe ratio *SR* used in the calculation of Tmin , however, should correspond to the frequency of estimation periods. If the annual Sharpe ratio claimed for a trading strategy is 2, and it is computed based on the basis of monthly data, then the corresponding monthly Sharpe ratio *SR* is 2/(12)0.5 = 0.5774. However, if the claimed Sharpe ratio is computed based on daily data, then the corresponding Sharpe ratio *SR* is 2/(250)0.5 = 0.1054. The minimum number of monthly observations required to verify the claimed Sharpe ratio with 90 percent statistical confidence is then just over nine months for monthly performance data and just over eight months for daily performance data. For a claimed Sharpe ratio of 6, less than one month of daily performance data is required to verify the claim. [Table 6.2](#page-27-0) summarizes the minimum performance evaluation times required for verification of performance data for key values of Sharpe ratios.

| Claimed Annualized<br>Sharpe Ratio | No. of Months Required (Monthly<br>Performance Data) | No. of Months Required (Daily<br>Performance Data) |
|------------------------------------|------------------------------------------------------|----------------------------------------------------|
| 0.5                                | 130.95                                               | 129.65                                             |
| 1.0                                | 33.75                                                | 32.45                                              |
| 1.5                                | 15.75                                                | 14.45                                              |
| 2.0                                | 9.45                                                 | 8.15                                               |
| 2.5                                | 6.53                                                 | 5.23                                               |
| 3.0                                | 4.95                                                 | 3.65                                               |

<span id="page-27-1"></span><span id="page-27-0"></span>**[Table 6.2](#page-27-1)** Minimum Trading Strategy Performance Evaluation Times Required for Verification of Reported Sharpe Ratios

| Claimed Annualized | No. of Months Required (Monthly | No. of Months Required (Daily |
|--------------------|---------------------------------|-------------------------------|
| Sharpe Ratio       | Performance Data)               | Performance Data)             |
| 4.0                | 3.38                            | 2.07                          |

## Alpha Decay

In addition to the performance metrics outlined earlier, HFT strategies can be evaluated on the basis of alpha decay, the erosion of alpha with time. The erosion of alpha may be due to the lack of execution in strategies relying on limit orders, or due to the poor latency infrastructure used for transmission of market orders. In either case, alpha decay can be measured and forecasted.

The alpha decay observed due to latency can be estimated as a distribution of market impact costs observed in a particular financial instrument a finite period of time after each trading decision was made.

Alpha decay of a strategy using limit orders measures the opportunity cost associated with failure to execute on trading signals of the strategy. Alpha decay is strategy specific and should be assessed based on the signals generated by the given strategy.

## Summary

Statistical tools for strategy evaluation allow managers to assess the feasibility and appropriateness of high-frequency strategies to their portfolios. As traders' and investment managers' understanding of HFT deepens, new metrics are deployed to capture the variability among HFT strategies. As a quick test of strategy feasibility, the Sharpe ratio remains the favorite.

## End-of-Chapter Questions

1. What is the Sharpe ratio? What are its drawbacks? How can it be enhanced?

2. What is the Sortino ratio?

3. Suppose a performance attribution analysis on a given high-frequency trading strategy finds strong dependence of trading gains on changes in the S&P 500. What are the implications for the trading strategy? Discuss.

4. Why does market impact enter calculation of strategy capacity? Why does probability of execution?

5. What is alpha decay and why does it exist?

1 Strategy capacity has been shown to be a function of trading costs and asset liquidity by Getmansky, Lo, and Makarov (2004).
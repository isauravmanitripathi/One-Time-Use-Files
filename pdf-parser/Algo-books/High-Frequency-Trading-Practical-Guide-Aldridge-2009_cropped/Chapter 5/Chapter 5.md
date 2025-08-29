![](_page_0_Picture_0.jpeg)

 $\bullet$  he field of strategy performance measurement is quite diverse. Many different metrics have been developed over time to illuminate a strategy's performance. This chapter summarizes the most popular approaches for performance measurement and discusses strategy capacity and the length of time required to evaluate a strategy.

# BASIC RETURN CHARACTERISTICS

Trading strategies may come in all shapes and sizes, but they share one characteristic that makes comparison across different strategies feasible return.

The return itself, however, can be measured across a wide array of frequencies: hourly, daily, monthly, quarterly, and annually, among others. Care should be exercised to ensure that all returns used for inter-strategy comparisons are generated at the same frequency.

Returns of individual strategies can be compared using a variety of performance measures. Average annual return is one such metric. An average return value is a simplistic summary of the location of the mean of the return distribution. Higher average returns may be potentially more desirable than lower returns; however, the average return itself says nothing about dispersion of the distribution of returns around its mean, a measure that can be critical for risk-averse investors.

Volatility of returns measures the dispersion of returns around the average return; it is most often computed as the standard deviation of returns. Volatility, or standard deviation, is often taken to proxy risk. Standard deviation, however, summarizes the average deviation from the mean and does not account for the risk of extreme negative effects that can wipe out years of performance.

A measure of tail risk popular among practitioners that documents the maximum severity of losses observed in historical data is maximum drawdown. Maximum drawdown records the lowest peak-to-trough return from the last global maximum to the minimum that occurred prior to the next global maximum that supersedes the last global maximum. The global maximum measured on the past data at any point in time is known as "high water mark." A drawdown is then the lowest return in between two successive high water marks. The lowest drawdown is known as the maximum drawdown.

Figure 5.1 illustrates the concepts of high water mark and maximum drawdown graphically. The graph presents an evolution of a sample cumulative return of a particular investment model over time. At time *tA*, the return *RA* is the highest cumulative return documented on the chart, so it is our high water mark at time *tA*. The cumulative return subsequently drops to level *RB* at time *tB*, but the value of our high water mark remains the same: *RA*. Since *RB* at time *tB* presents the lowest drop in cumulative return on record, the value (*RB* − *RA*) constitutes our maximum drawdown at time *tB*.

Subsequently, the model reaches a new high water mark at time *tA'* as soon as the cumulative return reached passes the previous high water mark *RA*. The value of the high water mark continues to increase until point C, where it reaches a peak value to date: *RC*. At this point, the maximum drawdown remains (*RB* − *RA*).

![](_page_1_Figure_5.jpeg)

**FIGURE 5.1** Calculation of maximum drawdowns.

Following point C, the cumulative return drops considerably, reaching progressively lower troughs. The new maximum drawdown is computed at a point X as soon as the following condition holds:  $R_X - R_C < R_B - R_C$  $R_A$ . Point C and the corresponding cumulative return  $R_C$  remain the high water mark until it is exceeded at point  $G$ . Point D sets the new maximum drawdown  $(R_D - R_C)$  that remains in effect for the duration of the time shown in the graph.

The average return, volatility, and maximum drawdown over a prespecified window of time measured at a predefined frequency are the mainstays of performance comparison and reporting for different trading strategies. In addition to the average return, volatility, and maximum drawdown, practitioners sometimes quote skewness and kurtosis of returns when describing the shape of their return distributions. As usual, skewness illustrates the position of the distribution relative to the return average; positive skewness indicates prevalence of positive returns, while negative skewness indicates that a large proportion of returns is negative. Kurtosis indicates whether the tails of the distribution are normal; high kurtosis signifies "fat tails," a higher than normal probability of extreme positive or negative events.

#### COMPARATIVE RATIOS

While average return, standard deviation, and maximum drawdown present a picture of the performance of a particular trading strategy, the measures do not lend to an easy point comparison among two or more strategies. Several comparative performance metrics have been developed in an attempt to summarize mean, variance, and tail risk in a single number that can be used to compare different trading strategies. Table 5.1 summarizes the most popular point measures.

The first generation of point performance measures were developed in the 1960s and include the Sharpe ratio, Jensen's alpha, and the Treynor ratio. The Sharpe ratio is probably the most widely used measure in comparative performance evaluation; it incorporates three desirable metrics—average return, standard deviation, and the cost of capital.

The Sharpe ratio was designed in 1966 by William Sharpe, later a winner of the Nobel Memorial Prize in Economics; it is a remarkably enduring concept used in the study and practice of finance. A textbook definition of the Sharpe ratio is  $SR = \frac{\bar{R} - R_F}{\sigma_R}$ , where  $\bar{R}$  is the annualized average return from trading,  $\sigma_R$  is the annualized standard deviation of trading returns, and  $R_F$  is the risk-free rate (e.g., Fed Funds) that is included to capture the opportunity cost as well as the position carrying costs associated with

| Sharpe Ratio<br>(Sharpe<br>[1966])      | SR = E [r]−rf<br>, where<br>σ[r]<br>E [r] = r1+···+rT<br>T<br><br>(r1−E [r])2+···+(rT−E [r])2<br>σ[r] =<br>T−1<br>The Sharpe ratio of<br>high-frequency trading<br>strategies: SR = E [r]<br>σ[r] | Adequate if returns are<br>normally distributed.                                                                                                                                                                                                                                                           |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Treynor Ratio<br>(Treynor<br>[1965])    | = E [ri]−rf<br>Treynori<br>βi<br>βi<br>is the regression<br>coefficient of trading<br>returns on returns of the<br>investor's reference<br>portfolio, such as the<br>market portfolio.            | Adequate if returns are<br>normally distributed and the<br>investor wishes to split his<br>holdings between one trading<br>strategy and the market<br>portfolio.                                                                                                                                           |
| Jensen's<br>Alpha<br>(Jensen<br>[1968]) | = E [ri] − rf<br>− βi(rM<br>− rf)<br>αi<br>βi<br>is the regression<br>coefficient of trading<br>returns on returns of the<br>investor's reference<br>portfolio, such as the<br>market portfolio.  | Measures trading return in<br>excess of the return predicted<br>by CAPM. Adequate if returns<br>are normally distributed and<br>the investor wishes to split his<br>holdings between one trading<br>strategy and the market<br>portfolio, but can be<br>manipulated by leveraging<br>the trading strategy. |

**TABLE 5.1** Performance Measure Summary

Measures based on lower partial moments (LPMs):

LPM of order *n* for security *i*:

$$LPM_{ni}(\tau) = \frac{1}{T} \sum_{t=1}^{T} \max[\tau - r_{it}, 0]^{n}$$

where τ is the minimal acceptable return;

*n* is the moment: *n* = 0 is the shortfall probability, *n* = 1 is the expected shortfall, *n* = 2 for τ = *E*[*r*] is the semi-variance.

According to Eling and Schuhmacher (2007), more risk-averse investors should use higher order *n*.

LPMs consider only negative deviations of returns from a minimal acceptable return. As such, LPMs are deemed to be a better measure of risk than standard deviation, which considers both positive and negative deviations (Sortino and van der Meer [1991]). Minimal acceptable return can be 0, risk-free rate, or average return.

#### TABLE 5.1 (Continued)

| Omega (Shadwick<br>and Keating<br>[2002]), (Kaplan<br>and Knowles<br>[2004])  | $\Omega_i = \frac{E[r_i] - \tau}{I \, PM_{\tau,i}(\tau)} + 1$                                                                                                              | $E[r_i] - \tau$ is the average<br>return in excess of the<br>benchmark rate.                                                                                                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sortino Ratio<br>(Sortino and van<br>der Meer [1991])                         | $\textit{Sortino}_i = \frac{E[r_i] - \tau}{(LPM_{2i}(\tau))^{1/2}}$                                                                                                        |                                                                                                                                                                                                          |
| Kappa 3 (Kaplan<br>and Knowles<br>[2004])                                     | $\mathsf{K3}_i = \frac{E[r_i] - \tau}{(IPM_{2i}(\tau))^{1/3}}$                                                                                                             |                                                                                                                                                                                                          |
| Upside Potential<br>Ratio (Sortino,<br>van der Meer, and<br>Plantinga [1999]) | $UPR_i = \frac{HPM_{1i}(\tau)}{(LPM_{2i}(\tau))^{1/2}}$ where<br>$HPM = higher partial moment$<br>$HPM_{ni}(\tau) = \frac{1}{T} \sum_{t=1}^{T} \max[r_{it} - \tau, 0]^{n}$ | According to Eling and<br>Schuhmacher (2007), this<br>ratio gains from the<br>consistent application of<br>the minimal acceptable<br>return $\tau$ in the numerator<br>as well as in the<br>denominator. |

Measures based on drawdown: frequently used by CTAs, according to Eling and Schuhmacher (2007, p. 5), "because these measures illustrate what the advisors are supposed to do best—continually accumulating gains while consistently limiting losses (see Lhabitant, 2004)." MD<sub>i1</sub> denotes the lowest maximum drawdown, MD<sub>i2</sub> the second lowest maximum drawdown, and so on.

| Calmar Ratio<br>(Young [1991])     | $Calmar_i = \frac{E[r_i] - r_f}{-MD_{ii}}$                                             | $MD_{i1}$ is the maximum<br>drawdown.                                                                                                                         |
|------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sterling Ratio<br>(Kestner [1996]) | $\textit{Sterling}_{i} = \frac{E[r_{i}] - r_{f}}{-\frac{1}{N} \sum_{i=1}^{N} MD_{ij}}$ | $-\frac{1}{N}\sum_{k=1}^{N}MD_{ij}$ is the<br>average maximum<br>drawdown.                                                                                    |
| Burke Ratio<br>(Burke [1994])      | $Burke_{i} = \frac{E[r_{i}] - r_{f}}{\left[\sum_{k=1}^{N} (MD_{ij})^{2}\right]^{1/2}}$ | $\left[\sum_{k=1}^{N} (MD_{ij})^2\right]^{1/2}$ is a type<br>of variance below the $N^{\text{th}}$<br>largest drawdown;<br>accounts for very large<br>losses. |

Value-at-risk-based measures.

Value at risk  $(VaR_i)$  describes the possible loss of an investment, which is not exceeded with a given probability of  $1 - \alpha$  in a certain period. For normally distributed returns,  $VaR_i = -(E[r_i] + z_\alpha \sigma_i)$ , where  $z_\alpha$  is the  $\alpha$ -quantile of the standard normal distribution.

| Excess return<br>on value at<br>risk (Dowd,<br>[2000])          | Excess R on VaR = $\frac{E[r]-r_f}{VaR}$                                                                                                                                                                                                                       | Not suitable for<br>non-normal returns.                                                                     |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Conditional<br>Sharpe ratio<br>(Agarwal and<br>Naik [2004])     | Conditional Sharpe = $\frac{E[r]-r_f}{CVaR_i}$<br>$CVaR_i = E[-r_{it} r_{it} < -VaR_i]$                                                                                                                                                                        | The advantage of<br>CVaR is that it<br>satisfies certain<br>plausible axioms<br>(Artzner et al.<br>[1999]). |
| Modified<br>Sharpe ratio<br>(Gregoriou<br>and Gueyie<br>[2003]) | Modified Sharpe = $\frac{E[r]-r_f}{MVaR_i}$<br>Cornish-Fisher expansion is calculated<br>as follows:<br>$MVaR_i = -(E[r_i] + \sigma_i(z_\alpha + (z_\alpha^2 - 1)S_i/6$<br>$+(z_{\alpha}^{3}-3z_{\alpha})EK_{i}/24-(2z_{\alpha}^{3}-5z_{\alpha})S_{i}^{2}/36)$ | Suitable for<br>non-normal returns.                                                                         |
|                                                                 | where Si denotes skewness and $EK_i$<br>the excess kurtosis for security i                                                                                                                                                                                     |                                                                                                             |

#### TABLE 5.1 (Continued)

the trading activity. It should be noted that in high-frequency trading with no positions carried overnight, the position carrying costs are 0. Therefore, the high-frequency Sharpe ratio is computed as follows:

$$SR = \frac{R}{\sigma_R}$$

What makes the Sharpe ratio an appealing measure of performance, in comparison with, say, raw absolute return? Surprisingly, the Sharpe ratio is an effective metric for selecting mean-variance efficient securities.

Consider Figure 5.2, for example, which illustrates the classic meanvariance frontier. In the figure, the Sharpe ratio is the slope of the line emanating from the risk-free rate and passing through a point corresponding to a given portfolio ( $M$  for market portfolio), or trading strategy, or individual security. The bold line tangent to the mean-variance set of all portfolio combinations is the efficient frontier itself. It has the highest slope and, correspondingly, the highest Sharpe ratio of all the portfolios in the set. For any other portfolio, trading strategy, or individual security A, the higher the Sharpe ratio, the closer the security is to the efficient frontier.

Sharpe himself came up with the metric when developing a portfolio optimization mechanism for a mutual fund for which he was consulting. Sharpe's mandate was to develop a portfolio selection framework for the

![](_page_6_Figure_1.jpeg)

**FIGURE 5.2** Sharpe ratio as a mean-variance slope. The market portfolio has the highest slope and, correspondingly, the highest Sharpe ratio.

fund with the following constraint: no more than 5 percent of the fund's portfolio could be allocated to a particular financial security. Sharpe then created the following portfolio solution: he first ranked the security universe on what now is known as Sharpe ratio, then picked the 20 securities with the best performance according to the Sharpe ratio measure, and invested 5 percent of the fund into each of the 20 securities. Equally weighted portfolio allocation in securities with the highest Sharpe ratios is just one example of a successful Sharpe ratio application.

Jensen's alpha is a measure of performance that abstracts from broad market influences, CAPM-style. Jensen's alpha implicitly takes into consideration the variability of returns in co-movement with chosen market indices.

The third ratio, the Treynor ratio, measures the average return in excess of the chosen benchmark per unit of risk proxied by beta from the CAPM estimation.

While these three metrics remain popular, they do not take into account the tail risk of extreme adverse returns. Brooks and Kat (2002), Mahdavi (2004), and Sharma (2004), for example, present cases against using Sharpe ratios on non-normally distributed returns. The researchers' primary concerns surrounding the use of the Sharpe ratio are linked to the use of derivative instruments that result in an asymmetric return distribution and fat tails. Ignoring deviations from normality may underestimate risk and overestimate performance. New performance measures have been subsequently developed to capture the tail risk inherent in the returns of most trading strategies.

A natural extension of the Sharpe ratio is to change the measure of risk from standard deviation to a drawdown-based methodology in an effort to capture the tail risk of the strategies. The Calmar ratio, Sterling ratio, and Burke ratio do precisely that. The Calmar ratio, developed by Young (1991), uses the maximum drawdown as the measure of volatility. The Sterling ratio, first described by Kestner (1996), uses the average drawdown as a proxy for volatility. Finally, the Burke ratio, developed by Burke (1994), uses the standard deviation of maximum drawdowns as a volatility metric.

In addition to ignoring the tail risk, the Sharpe ratio is also frequently criticized for including positive returns in the volatility measure. The argument goes that only the negative returns are meaningful when estimating and comparing performance of trading strategies. In response, a "Greek" class of ratios extended the Sharpe ratio by replacing volatility with the average metrics of adverse returns only. These adverse return metrics are known as lower partial moments (LPMs) and are computed as regular moments of a distribution (i.e., mean, standard deviation, and skewness), except that the data used in computation comprises returns below a specified benchmark only. Thus, a metric known as Omega, developed by Shadwick and Keating (2002) and Kaplan and Knowles (2004), replaces the standard deviation of returns in the Sharpe ratio calculation with the first lower partial moment, the average of the returns that fell below the selected benchmark. The Sortino ratio, developed by Sortino and van der Meer (1991), uses the standard deviation of the returns that fell short of the benchmark, the second LPM, as a measure of return volatility in the Sharpe ratio calculation. The Kappa 3 measure, developed by Kaplan and Knowles (2004), replaces the standard deviation in the Sharpe ratio with the third LPM of the returns, the skewness of the returns below the benchmark. Finally, the Upside Potential ratio, produced by Sortino, van der Meer, and Plantinga (1999), measures the average return above the benchmark (the first higher partial moment) per unit of standard deviation of returns below the benchmark.

Value-at-risk (VaR) measures also gained considerable popularity as metrics able to summarize the tail risk in a convenient point format within a statistical framework. The VaR measure essentially identifies the 90 percent, 95 percent, or 99 percent Z-score cutoff in distribution of returns (the metric is also often used on real dollar distributions of daily profit and loss). VaR companion measure, the conditional VaR (CVaR), also known as expected loss (EL), measures the average value of return within the cut-off tail. Of course, the original VaR assumes normal distributions of returns, whereas the returns are known to be fat-tailed. To address this issue, a modified VaR (MVaR) measure was proposed by Gregoriou and Gueyie (2003) and takes into account deviations from normality. Gregoriou and Gueyie (2003) also suggest using MVaR in place of standard deviation in Sharpe ratio calculations.

How do these performance metrics stack up against each other? It turns out that all metrics deliver comparable rankings of trading strategies. Eling and Schuhmacher (2007) compare hedge fund ranking performance of the 13 measures listed and conclude that the Sharpe ratio is an adequate measure for hedge fund performance.

### **PERFORMANCE ATTRIBUTION**

Performance attribution analysis, often referred to as "benchmarking," goes back to the arbitrage pricing theory of Ross (1977) and has been applied to trading strategy performance by Sharpe (1992) and Fung and Hsieh (1997), among others. In a nutshell, performance attribution notes that *t-*period return on strategy *i* that invests into individual securities with returns *rjt* in period *t*, with *j* = 1, ... , *J*, has an underlying factor structure:

$$R_{it} = \sum_{j} x_{jt} r_{jt} \tag{5.1}$$

where *xjt* is the relative weight of the *j*th financial security in the portfolio at time *t*, *j xjt* = 1. The *j*th financial security, in turn, has a period-*t* return that can be explained by *K* systematic factors:

$$r_{jt} = \sum_{k} \lambda_{jk} F_{kt} + \varepsilon_{jt} \tag{5.2}$$

where *Fkt* is one of *K* underlying systematic factors in period *t*, *k* = 1, ... , *K*, λ is the factor loading, and ε*jt* is the security *j* idiosyncratic return in period *t*. Following Sharpe (1992), factors can be assumed to be broad asset classes, as well as individual stocks or other securities. Combining equations (1) and (2) we can express returns as follows:

$$R_{it} = \sum_{j,k} x_{jt} \lambda_{jk} F_{kt} + \sum_{j} x_{jt} \varepsilon_{jt} \tag{5.3}$$

reducing the large number of financial securities potentially underlying strategy *i*'s returns to a small group of global factors. Performance attribution to various factors then involves regressing the strategy's returns on a basket of factors:

$$R_{it} = \alpha_i + \sum_k b_{ik} F_{kt} + u_{it} \tag{5.4}$$

where *bk* measures the performance of the strategy that can be attributed to factor *k*, α*<sup>i</sup>* measures the strategy's persistent ability to generate abnormal returns, and *uit* measures the strategy's idiosyncratic return in period *t.*

Performance attribution is a useful measure of strategy returns for the following reasons:

- The technique may accurately capture investment styles of black-box strategies in addition to the details reported by the designer of the strategy.
- Performance attribution is a measure of true added value of the strategy and lends itself to easy comparison with other strategies.
- Near-term persistence of trending factors allows forecasting of strategy performance based on performance attribution (see, for example, Jegadeesh and Titman [1993]).

In the performance attribution model, the idiosyncratic value-added of the strategy is the strategy's return in excess of the performance of the basket of weighted strategy factors.

Fung and Hsieh (1997) find that the following eight global groups of asset classes serve well as performance attribution benchmarks:

- Three equity classes: MSCI U.S. equities, MSCI non–U.S. equities, and IFC emerging market equities
- Two bond classes: JP Morgan U.S. government bonds and JP Morgan non-U.S. government bonds
- One-month Eurodollar deposit representing cash
- The price of gold proxying commodities and the Federal Reserve's trade-weighted dollar index measuring currencies in aggregate.

## OTHER CONSIDERATIONS IN STRATEGY EVALUATION

# **Strategy Capacity**

Strategy performance may vary with the amount of capital deployed. Sizeinduced changes in observed performance are normally due to limits in market liquidity for each trading instrument. Large position sizes consume available pools of liquidity, driving market prices into adverse directions and reducing the profitability of trading strategies. The capacity of individual strategies can be estimated through estimation of market impact, discussed in detail in Chapter 19. Extensive research on the impact of investment size on performance has been documented for hedge funds utilizing portfolios of strategies. This section notes the key findings in the studies of the impact of investment size on fund performance.

Fransolet (2004) shows that fast increase in capital in the entire industry may erode capacities of many profitable strategies. In addition, per Brown, Goetzmann, and Park (2004), strategy capacity may depend on a manager's skills. Furthermore, strategy capacity is a function of trading costs and asset liquidity, as shown by Getmansky, Lo, and Makarov (2004). As a result, Ding et al. (2008) conjecture that when the amount of capital deployed is lower than the strategy capacity, the strategy performance may be positively related to its capitalization. However, once capitalization exceeds strategy capacity, performance becomes negatively related to the amount of capital involved.

## **Length of the Evaluation Period for High-Frequency Strategies**

Most portfolio managers face the following question in evaluating candidate trading strategies for inclusion in their portfolios: how long does one need to monitor a strategy in order to gain confidence that the strategy produces the Sharpe ratio advertised?

Some portfolio managers have adopted an arbitrarily long evaluation period: six months to two years. Some investors require a track record of at least six years. Yet others are content with just one month of daily performance data. It turns out that, statistically, any of the previously mentioned time frames is correct if it is properly matched with the Sharpe ratio it is intended to verify. The higher the Sharpe ratio, the shorter the strategy evaluation period needed to ascertain the validity of the Sharpe ratio.

If returns of the trading strategy can be assumed to be normal, Jobson and Korkie (1981) showed that the error in Sharpe ratio estimation is normally distributed with mean 0 and standard deviation

$$s = [(1/T)(1 + 0.5SR^2)]^{1/2}$$

For a 90 percent confidence level, the claimed Sharpe ratio should be at least 1.645 times greater than the standard deviation of the Sharpe ratio errors, *s.* As a result, the minimum number of evaluation periods used for Sharpe ratio verification is

$$T_{\rm min} = (1.645^2 / SR^2)(1 + 0.5SR^2)$$

The Sharpe ratio *SR* used in the calculation of Tmin, however, should correspond to the frequency of estimation periods. If the annual Sharpe ratio claimed for a trading strategy is 2, and it is computed based on the basis of monthly data, then the corresponding monthly Sharpe ratio *SR* is 2/(12)0.5 = 0.5774. On the other hand, if the claimed Sharpe ratio is computed based on daily data, then the corresponding Sharpe ratio *SR*

| Claimed Annualized<br>Sharpe Ratio | No. of Months Required<br>(Monthly Performance Data) | No. of Months Required<br>(Daily Performance Data) |
|------------------------------------|------------------------------------------------------|----------------------------------------------------|
| 0.5                                | 130.95                                               | 129.65                                             |
| 1.0                                | 33.75                                                | 32.45                                              |
| 1.5                                | 15.75                                                | 14.45                                              |
| 2.0                                | 9.45                                                 | 8.15                                               |
| 2.5                                | 6.53                                                 | 5.23                                               |
| 3.0                                | 4.95                                                 | 3.65                                               |
| 4.0                                | 3.38                                                 | 2.07                                               |

**TABLE 5.2** Minimum Trading Strategy Performance Evaluation Times Required for Verification of Reported Sharpe Ratios

is 2/(250)0.5 = 0.1054. The minimum number of monthly observations required to verify the claimed Sharpe ratio with 90 percent statistical confidence is then just over nine months for monthly performance data and just over eight months for daily performance data. For a claimed Sharpe ratio of 6, less than one month of daily performance data is required to verify the claim. Table 5.2 summarizes the minimum performance evaluation times required for verification of performance data for key values of Sharpe ratios.

# **CONCLUSION**

Statistical tools for strategy evaluation allow managers to assess the feasibility and appropriateness of high-frequency strategies to their portfolios. Although several statistical strategy evaluation methods have been developed, the Sharpe ratio remains the most popular measure.
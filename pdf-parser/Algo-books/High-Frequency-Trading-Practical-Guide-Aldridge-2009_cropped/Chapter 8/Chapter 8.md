# CHAPTER 8

**Searching for High-Frequency** Trading Opportunities

 $\blacksquare$  his chapter reviews the most important econometric concepts used in the subsequent parts of the book. The treatment of topics is by no means exhaustive; it is instead intended as a high-level refresher on the core econometric concepts applied to trading at high frequencies. Yet, readers relying on software packages with preconfigured statistical procedures may find the level of detail presented here to be sufficient for quality analysis of trading opportunities. The depth of the statistical content should be also sufficient for readers to understand the models presented throughout the remainder of this book. Readers interested in a more thorough treatment of statistical models may refer to Tsay (2002); Campbell, Lo, and MacKinlay (1997); and Gouriéroux and Jasiak (2001).

This chapter begins with a review of the fundamental statistical estimators, moves on to linear dependency identification methods and volatility modeling techniques, and concludes with standard nonlinear approaches for identifying and modeling trading opportunities.

# STATISTICAL PROPERTIES OF RETURNS

According to Dacorogna et al. (2001, p. 121), "high-frequency data opened up a whole new field of exploration and brought to light some behaviors that could not be observed at lower frequencies." Summary statistics about aggregate behavior of data, known as "stylized facts," help distill particularities of high-frequency data. Dacorogna et al.  $(2001)$  review stylized facts for foreign exchange rates, interbank money market rates, and Eurofutures (futures on Eurodollar deposits).

Financial data is typically analyzed using returns. A return is a difference between two subsequent price quotes normalized by the earlier price level. Independent of the price level, returns are convenient for direct performance comparisons across various financial instruments. A simple return measure can be computed as shown in equation (8.1):

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1 \tag{8.1}$$

where *Rt* is the return for period *t*, *Pt* is the price of the financial instrument of interest in period *t*, and *Pt* <sup>−</sup> <sup>1</sup> is the price of the financial instrument in period *t* − 1. As discussed previously, determination of prices in highfrequency data may not always be straightforward; quotes arrive at random intervals, but the analysis demands that the data be equally spaced.

Despite the intuitiveness of simple returns, much of the financial literature relies on log returns. Log returns are defined as follows:

$$r_t = \ln{(R_t)} = \ln{(P_t)} - \ln{(P_{t-1})}$$
(8.2)

Log returns are often preferred to simple returns for the following reasons:

- **1.** If log returns are assumed to follow a normal distribution, then the underlying simple returns and the asset prices used to compute simple returns follow a lognormal distribution. Lognormal distributions better reflect the actual distributions of asset prices than do normal distributions. For example, asset prices are generally positive. Lognormal distribution models this property perfectly, whereas normal distributions allow values to be negative.
- **2.** Like distributions of asset prices, lognormal distributions have fatter tails than do normal distributions. Although lognormal distributions typically fail to model the fatness of the tails of asset prices exactly, lognormal distributions better approximate observed fat tails than do normal distributions.
- **3.** Once log prices have been computed, log returns are easy and fast to manipulate.

Returns can be computed on bid prices, ask prices, last trade prices, or mid prices. Mid prices can be taken to be just an arithmetic average, or a mid-point between a bid and an ask price at any point in time. In the absence of synchronous quotes, mid prices can be computed using the last bid and ask quotes.

Both simple and log returns can be averaged over time to obtain lowerfrequency return estimates. An average of simple and log returns can be computed as normal arithmetic averages:

$$E[R] = \frac{1}{T} \sum_{t=1}^{T} R_t \tag{8.3}$$

$$\mu = \frac{1}{T} \sum_{t=1}^{T} r_t \tag{8.4}$$

Variation in sequential returns is known as volatility. Volatility can be measured in a variety of ways. The simplest measure of volatility is variance of simple or log returns, computed according to equations (8.5) and (8.6).

$$\text{var}[R] = \frac{1}{T-1} \sum_{t=1}^{T} (R_t - E[R])^2 \tag{8.5}$$

$$\sigma^2 = \frac{1}{T-1} \sum_{t=1}^T (r_t - \mu)^2 \tag{8.6}$$

Note that the division factor in volatility computation is (*T* − 1), not *T*. The reduced number of normalizing observations accounts for reduced number of degrees of freedom—the variance equation includes the average return, which in most cases is itself estimated from the sample data. Standard deviation is a square root of the variance.

Other common statistics used to describe distributions of prices or simple or log returns are skewness and kurtosis. Skewness measures whether a distribution skews towards either the positive or the negative side of the mean, as compared with the standardized normal distribution. Skewness of the standardized normal distribution is 0. Skewness can be measured as follows:

$$S[R] = \frac{1}{T-1} \frac{\sum\limits_{t=1}^{T} (R_t - E[R])^3}{(\text{var}[R])^{3/2}}$$
(8.7)

Kurtosis is a measure of fatness of the tails of a distribution. The fatter the tails of a return distribution, the higher the chance of an extreme positive or negative return. Extreme negative returns can be particularly damaging to a trading strategy, potentially wiping out all previous profits and even equity capital. The standardized normal distribution has a kurtosis of 3. Kurtosis can be computed as follows:

$$K[R] = \frac{1}{T-1} \frac{\sum_{t=1}^{T} (R_t - E[R])^4}{(\text{var}[R])^2}$$
(8.8)

If returns indeed follow a lognormal distribution (i.e., log returns *rt* are normally distributed with mean µ and standard deviation σ2), then the mean and the standard deviation of simple returns has the following properties:

$$E[R_t] = \exp\left(\mu - \frac{\sigma^2}{2}\right) - 1$$
  
$$\operatorname{var}[R_t] = \exp\left(2\mu + \sigma^2\right) \left[\exp(\sigma^2) - 1\right]$$
  
(8.9)

Table 8.1 shows statistics for log returns of EUR/USD. The log returns are calculated from closing trade prices observed during each period at different frequencies. If no trades are observed during a particular time period, the closing trade price from the previous period is used in the estimation. As Table 8.1 illustrates, the higher the data frequency, the higher the kurtosis of the data—that is, the fatter the tails of the data distribution.

Another metric useful to describe distributions of returns is autocorrelation, which is a measure of serial dependence between subsequent

| TABLE 8.1 | Summary Statistics for Log Returns for Different Instruments of<br>EUR/USD at Various Frequencies and for Different Securities (The log<br>returns are computed from closing trade prices sampled at different<br>frequencies on data for August–November 2008.) |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Frequency                                  | Mean                          | Max                        | Median                     | Min                           | Standard<br>Deviation      | Skewness                      | Kurtosis                     |
|--------------------------------------------|-------------------------------|----------------------------|----------------------------|-------------------------------|----------------------------|-------------------------------|------------------------------|
| Daily Spot<br>5-min Spot<br>15-min<br>Spot | −0.0003<br>−0.0001<br>−0.0001 | 0.0119<br>0.0184<br>0.0186 | 0.0001<br>0.0000<br>0.0000 | −0.0179<br>−0.0225<br>−0.0226 | 0.0052<br>0.0009<br>0.0015 | −0.4389<br>−1.4723<br>−1.0278 | 3.3051<br>83.7906<br>32.6960 |
| 1-Hr Spot<br>1-Hr<br>Futures               | −0.0002<br>−0.0002            | 0.0213<br>0.0213           | −0.0001<br>−0.0001         | −0.0228<br>−0.0300            | 0.0029<br>0.0032           | −0.8184<br>−0.7207            | 14.5028<br>13.5256           |
| 1-Hr Call<br>Options                       | −0.0001                       | 0.6551                     | −0.0031                    | −0.6555                       | 0.1411                     | 0.3333                        | 8.3108                       |
| 1-Hr Put<br>Options                        | 0.0000                        | 2.1115                     | 0.0022                     | −1.7717                       | 0.1736                     | 0.9859                        | 51.8545                      |

returns sampled at a specific frequency. For example, autocorrelation of order 1 measures of 1-minute returns is a correlation of 1-minute returns with 1-minute returns that occurred 1 minute earlier. Autocorrelation of order 2 measures of 1-minute returns is a correlation of 1-minute returns with 1-minute returns that occurred 2 minutes earlier. The autocorrelation value of order  $p$  can be determined as follows:

$$\rho(p) = \frac{\sum\limits_{t=p+1}^{T} \left[ (R_t - E[R])(R_{t-p} - E[R]) \right]}{\left(\sum\limits_{t=p+1}^{T} (R_t - E[R])\right)^{1/2} \left(\sum\limits_{t=p+1}^{T} (R_{t-p} - E[R])\right)^{1/2}} \tag{8.10}$$

As any other correlation function,  $\rho(p)$  ranges from  $-1$  to 1. Equation  $(8.10)$  uses simple returns to compute autocorrelation, but returns of any type can be used instead.

Autocorrelation is of interest because its results indicate a persistent behavior in returns. For example, Dacorogna et al. (2001) report negative first-order autocorrelation in 10-minute spot foreign exchange data as evidence of persistent trends in price formation.

Autocorrelation allows us to check whether there are any persistent momentum/reversal relationships in the data that we could trade upon. For example, it is a well-known stylized fact that a large swing, or momentum, in the price of a financial security is typically followed by a reversal. Using autocorrelation at different frequencies we can actually establish whether the patterns persist and whether we can trade upon them.

Autocorrelation, like any correlation function, can range from  $-1$  to 1. High autocorrelation, say 0.5 and higher, implies a significant positive relationship between current and lagged observations. Low autocorrelation, say  $-0.5$  and lower, in turn implies a significant negative relationship between current and lagged observations. Thus, if a return today is positive and the lag-1 autocorrelation is greater than  $0.5$ , we can expect that the return tomorrow will be positive as well, at least 50 percent of the time. Thus, if a return today is positive and the lag-1 autocorrelation is less than  $-0.5$ , we can expect that the return tomorrow will be negative at least 50 percent of the time. Little, if anything, can be said about lagged relationships characterized by correlations closer to  $0$ .

Of course, we cannot make sweeping inferences without first formally testing the statistical significance of the observed autocorrelation. There are two popular tests: (1) a t-ratio test allows us to check whether autocorrelation is significant at a specific lag, and  $(2)$  the Portmanteau test and its variation, the Ljung-Box test, allow us to determine the last significant auto<br>correlation in the sequence, beginning with  $\rho(1)$ . The Portmanteau and Ljung-Box tests are useful in determining the number of lags necessary in the autoregressive process, which is discussed in the following section.

To determine whether an individual  $\rho(l)$  is significant, we can apply the following test:

$$t - \text{ratio} = \frac{\hat{\rho}_l}{\sqrt{(1 + 2\sum_{i=1}^{l-1} \hat{\rho}_i)/T}}$$
(8.11)

For a significance level of  $(100-\alpha)$  percent, we reject the observed autocorrelation  $\rho(l)$  if  $|t - \text{ratio}| > Z_{\alpha/2}$ , where  $Z_{\alpha/2}$  is the 100(1 –  $\alpha/2$ )th percentile of the standard normal distribution.

As the t-ratio test indicates, autocorrelation is only  $90$  percent+ statistically significant at lags 1 and 2, meaning that we can reliably use this analysis to make statistically accurate predictions for at most two days ahead.

To find the optimal number of autocorrelations or the number of lags to use in forecasting future values, many researchers use the Portmanteau test and its finite-sample enhancement, the Ljung-Box test. Unlike the t-ratio test, which tests the statistical significance of an individual autocorrelation at a particular lag, both the Portmanteau and Liung-Box tests help us determine whether correlations at lags  $1, 2, \ldots, l$  are jointly significant.

The end-goal of the test is to find the lag  $m$  where autocorrelations  $1, 2, \ldots, m$  are jointly significant, but autocorrelations  $1, 2, \ldots, m, m+1$ are no longer jointly significant. Such a lag  $m$ , once identified, signals the optimal number of lags to be used in further modeling for the security under consideration.

Both Portmanteau and Ljung-Box tests produce similar results when the number of observations is large. The Liung-Box test is optimized for samples with at least 200 observations or  $30$  at the very minimum.

Formally, the tests are specified as follows: the null hypothesis is that the  $m$  autocorrelations are not jointly statistically significant—that is,  $H_0: \rho_1 = \dots \rho_m = 0$ , and the alternative hypothesis is  $H_a: \rho_i \neq 0$  for some  $i \in \{1, \ldots, m\}$ . To establish that the *m*th autocorrelation is statistically significant, we need to be able to reject the null hypothesis.

Portmanteau test (Box and Pierce [1970]): 
$$Q^*(m) = T \sum_{l=1}^{m} \hat{\rho}_l^2$$
 (8.12)

Liung-Box test (Liung and Box  $[1978]$ ):

$$Q(m) = T(T+2) \sum_{l=1}^{m} \frac{\hat{\rho}_l^2}{T-l}$$
(8.13)

Assuming that the underlying data sequence is independently and identically distributed, both tests are asymptotically chi-squared random

|                       | <b>Statistical Significance</b> |            |            |               |  |  |  |
|-----------------------|---------------------------------|------------|------------|---------------|--|--|--|
| Degrees of<br>Freedom | 90 percent                      | 95 percent | 99 percent | 99.99 percent |  |  |  |
| 1                     | 2.705541                        | 3.841455   | 6.634891   | 15.13429      |  |  |  |
| 2                     | 4.605176                        | 5.991476   | 9.210351   | 18.42474      |  |  |  |
| 3                     | 6.251394                        | 7.814725   | 11.34488   | 21.10402      |  |  |  |
| 4                     | 7.779434                        | 9.487728   | 13.2767    | 23.5064       |  |  |  |
| 5                     | 9.236349                        | 11.07048   | 15.08632   | 25.75065      |  |  |  |
| 6                     | 10.64464                        | 12.59158   | 16.81187   | 27.85266      |  |  |  |
| 7                     | 12.01703                        | 14.06713   | 18.47532   | 29.88138      |  |  |  |
| 8                     | 13.36156                        | 15.50731   | 20.09016   | 31.82683      |  |  |  |
| 9                     | 14.68366                        | 16.91896   | 21.66605   | 33.72467      |  |  |  |
| 10                    | 15.98717                        | 18.30703   | 23.20929   | 35.55716      |  |  |  |
| 11                    | 17.27501                        | 19.67515   | 24.72502   | 37.36475      |  |  |  |
| 12                    | 18.54934                        | 21.02606   | 26.21696   | 39.13058      |  |  |  |
| 13                    | 19.81193                        | 22.36203   | 27.68818   | 40.87346      |  |  |  |
| 14                    | 21.06414                        | 23.68478   | 29.14116   | 42.57523      |  |  |  |
| 15                    | 22.30712                        | 24.9958    | 30.57795   | 44.25964      |  |  |  |
| 16                    | 23.54182                        | 26.29622   | 31.99986   | 45.92551      |  |  |  |
| 17                    | 24.76903                        | 27.5871    | 33.40872   | 47.55914      |  |  |  |
| 18                    | 25.98942                        | 28.86932   | 34.80524   | 49.18533      |  |  |  |
| 19                    | 27.20356                        | 30.14351   | 36.19077   | 50.78726      |  |  |  |
| 20                    | 28.41197                        | 31.41042   | 37.56627   | 52.38323      |  |  |  |

**TABLE 8.2** Critical Values for the Chi-Squared Distributions with Different **Degrees of Freedom** 

variables with  $m$  degrees of freedom. The decision rule is to reject the null hypothesis at  $100(1-\alpha)$  percent statistical significance if  $Q(m) > \chi^2_\alpha$ , where  $\chi^2_{\alpha}$  is the  $100(1-\alpha)$ th percentile of a chi-squared distribution with  $m$  degrees of freedom. Table 8.2 lists cut-off values for the chi-squared distributions with different levels of  $\alpha$ .

High-frequency trading relies on fast, almost instantaneous, execution of orders. In this respect, high-frequency trading works best when all orders are initiated, sent through, and executed via computer networks, bypassing any human interference. Depending on the design of a particular systematic trading mechanism, even a second's worth of delay induced by hesitation or distraction on the part of a human trader can substantially reduce the system's profitability.

# LINEAR ECONOMETRIC MODELS

Linear econometric models forecast random variables as linear combinations of other contemporaneous or lagged random variables with well-defined distributions. In equation terms, linear models can be expressed as follows:

$$y_t = \alpha + \sum_{i=0}^{\infty} \beta_i x_{t-i} + \sum_{j=0}^{\infty} \gamma_j z_{t-i} + \dots + \varepsilon_t \qquad (8.14)$$

where {*yt*} is the time series of random variables that are to be forecasted, {*xt*} and {*zt*} are factors significant in forecasting {*yt*}, and α, β, and γ are coefficients to be estimated.

Technical analysts like to refer to periods of momentums and reversals. While both can be readily observed on the charts, accurately predicting when the next momentum or reversal begins or ends is not simple. Autoregressive moving average (ARMA) is an estimation framework designed to detect consistent momentum and reversal patterns in data of selected frequencies.

Most linear models require that the distributional properties of data remain approximately constant through time, or stationary.

# **Stationarity**

Stationarity is measured on the residuals (error terms) of econometric models. Stationarity requires that the distribution of the residuals remains stable through time; it is a necessary condition of most linear models.

Stationarity describes the stability of a distribution of a random variable. Distribution of a stationary time series does not change if shifted in time or space. A number of stationarity tests have been developed, the few examples of which are Choi (1992), Cochrane (1991), Dickey and Fuller (1979), and Phillips and Perron (1988). The Augmented Dickey Fuller (ADF) test frequently appears in the literature and tests several lags of autocorrelation of the dependent variable for unit root (ρ = 1). The absence of unit root indicates stability in the inferences obtained in the estimation. On the other hand, presence of the unit root suggests that the obtained results may well be spurious and that the results are invalid.

# **Autoregressive (AR) Estimation**

Autoregressive (AR) estimation models are regressions on the lagged values of the dependent variable:

$$y_t = \alpha + \sum_{i=0}^{\infty} \beta_i y_{t-i} + \varepsilon_t \tag{8.15}$$

Coefficients obtained in autoregressions indicate momentum and reversal patterns in the data. Positive and statistically significant β coefficients, for example, indicate positive serial dependence or momentum. Similarly, negative statistically significant β coefficients indicate reversal.

# **Moving Average (MA) Estimation**

Moving average (MA) models constitute another set of tools for forecasting future movements of a financial instrument. While autoregressive AR models estimate what proportion of past period data is likely to persist in future periods, MA models focus on how future data reacts to innovation in the past data. In other words, AR models estimate future responses to the expected component realized in the past persistence, whereas MA models measure future responses to the unexpected component realized in the past data. Figure 8.1 illustrates the difference between AR and MA estimation.

Unlike the AR models that can be estimated using ordinary leastsquares or OLS regressions, estimation of moving average models is more complex. Many off-the-shelf packages provide built-in routines to assist users in the process.

![](_page_8_Figure_5.jpeg)

**FIGURE 8.1** Illustration of differences between AR and MA estimation.

 $MA(q)$  model, with q lags, can be specified as follows:

$$r_t = c_0 + a_t - \theta_1 a_{t-1} - \dots - \theta_q a_{t-q} \tag{8.16}$$

where  $c_0$  is the intercept,  $\theta_l$  is the coefficient pertaining to lag l, and  $a_l$ is the unexpected component of the return at lag  $l$ . The negative signs in front of the  $\theta$ 's are nothing more than a conventional notation of an MA representation.

For the intrepid, there are two main approaches to estimating MA:

- 1. Assume that the initial unexpected component is  $0$  and then recursively estimate other unexpected components using OLS.
- 2. Assume that the unexpected component is an additional parameter to be estimated, and then estimate the model using a technique known as maximum likelihood estimation (MLE).

Using the first approach, estimation proceeds as follows:

- 1. Run autocorrelation analysis to determine the last statistically significant lag,  $q$ .
- 2. Estimate  $c_0$  by running the following OLS regression of  $r_t$  on a vector of 1's:  $r_t = c_0 + a_t$ , assuming  $a_t \sim N(0, \sigma^2)$ . Determine  $a_1$ 's as  $a_t = r_t - c_0$ .
- 3. Estimate  $c_0$  and  $\theta_1$  using the following OLS regression:  $r_t = c_0 \theta_1 a_1 +$  $a_2$ , where  $a_1$  is as determined in Step 2. Find  $a_2$ 's as  $a_2 = r_t - c_0 + \theta_1 a_1$ .
- **4.** Repeat Step 3 to find  $a_3, \ldots, a_q$ , where  $q$  is as determined in Step 1.
- 5. Estimate MA(q) coefficients  $c_0, \theta_1, \theta_2, \ldots, \theta_q$  in the equation  $r_t =$  $c_0 - \theta_1 a_{t-1} - \theta_2 a_{t-2} - \cdots - \theta_q a_{t-q} + a_t$ , with  $a_{t-i} = a_i$  estimated previously, and  $a_t$  an error term distributed with mean 0 and variance  $\sigma_a^2$ .

Forecasting with MA models is a pretty straightforward exercise. For a one-period forecast, we are seeking to find  $E[r_{t+1}]$ , which for MA(q) model is

$$E[r_{t+1}|I_t] = E[c_0 - \theta_1 a_t - \theta_2 a_{t-1} - \dots - \theta_q a_{t-q} + a_{t+1}|I_t]$$
(8.17)

where  $I_t$  is the set of all information available at t. The key issue is to remember that forecasts for the unexpected components  $a_l$  have the following properties:  $E[a_{t+1}|I_t] = 0$ , and  $Var[a_{t+1}|I_t] = \sigma_a^2$ . Keeping these properties in mind,  $E[r_{t+1}|I_t]$  now becomes

$$E[r_{t+1}|I_t] = c_0 - \theta_1 a_t - \theta_2 a_{t-1} - \dots - \theta_q a_{t-q}$$
(8.18)

and the forecast error becomes  $e(1) = r_{t+1} - E[r_{t+1}|I_t] = a_{t+1}$  with variance  $Var[e(1)] = \sigma_a^2$ . A two-step-ahead forecast can be computed as follows:  $E[r_{t+2}|I_t] = E[c_0 - \theta_1 a_{t+1} - \theta_2 a_t - \cdots - \theta_q a_{t-q+1} + a_{t+2}|I_t] = c_0 - \theta_1 a_{t+1} - \theta_2 a_t - \cdots - \theta_q a_{t-q+1} + a_{t+2}|I_t] = c_0 - \theta_1 a_{t+1} - \theta_2 a_t - \cdots - \theta_q a_{t-q+1} + a_{t+2}|I_t] = c_0 - \theta_1 a_{t+1} - \theta_2 a_t - \cdots - \theta_q a_{t-q+1} + a_{t+2}|I_t] = c_0 - \theta_1 a_{t$  $\theta_2 a_t - \cdots - \theta_q a_{t-q+1}$ . Finally, an *l*-step ahead forecast for  $l > q$  is  $E[r_{t+l}|I_t] = c_0.$ 

#### Autoregressive Moving Average (ARMA)

Autoregressive moving average (ARMA) models combine the AR and MA models in a single framework.  $\text{ARMA}(p,q)$ , for example, is specified as follows:

$$r_{t} = \alpha + \sum_{i=0}^{p} \beta_{i} r_{t-i} - \sum_{i=0}^{q} \theta_{i} a_{t-i} + \varepsilon_{t}$$
(8.19)

Like MA models, ARMA models are estimated using maximum likelihood  $(\text{MLE}).$ 

# Cointegration

Cointegration is a popular technique used for optimal portfolio construction, hedging, and risk management. Cointegration measures the contemporaneous or lagged effect of one variable on another variable. For example, if both time series  $\{x\}$  and  $\{y\}$  represent price time series of two financial securities, cointegration identifies a lead-lag relationship between the two time series.

The simplest test for lead-lag relationships can be specified using the following equation, first suggested by Engle and Granger (1987):

$$x_t = \alpha + \beta y_t + \varepsilon_t \tag{8.20}$$

Equation  $(8.20)$  can be estimated using OLS, with the residuals tested for stationarity.

The cointegration specification of equation  $(8.20)$ , however, does not reveal whether one variable drives or causes another. To detect causality, a technique known as error correction model (ECM) is often used. In the simplest case with just two variables (e.g., log-price series), the ECM can be specified as the following pair of simultaneous equations:

$$\begin{aligned} \Delta x_t &= \alpha_1 + \beta_1 \Delta x_{t-1} + \beta_2 \Delta y_{t-1} + \gamma_1 z_{t-1} + \varepsilon_1 \\ \Delta y_t &= \alpha_2 + \beta_3 \Delta x_{t-1} + \beta_4 \Delta y_{t-1} + \gamma_2 z_{t-1} + \varepsilon_2 \end{aligned} \tag{8.21}$$

where denotes the first difference operator and *zt* is a stationary cointegrating vector, *zt* = *xt* − α − β*yt* from equation (8.20). Equations (8.21) are then simultaneously estimated using OLS. Coefficients γ <sup>1</sup> and γ <sup>2</sup> constrain deviations from long-run equilibrium specified by equation (8.20) and explain the "error correction" piece of the ECM.

If β2, the coefficient on the lagged *y* returns in the *x* equation is found to be significant, then changes in *y* lead changes in *x*. In Granger causality terminology, *y* "causes" *x*. Both the direction and strength of causalities may change over time.

Cointegration is widely used in testing for lead-lag relationships in generating cross-asset trading signals. Cointegration can also be an important component of portfolio management and hedging applications.

# **VOLATILITY MODELING**

Most of today's uses of volatility modeling involve forecasting components of future returns. The forecasts range from the point forecasts to quantiles of returns to the probabilistic density of future returns. These forecasts are used by portfolio managers to optimize the performance of their investment vehicles, by risk managers to limit their trading downside, and by quantitative traders to develop superior trading models. According to Engle and Patton (2001, p. 238):

*A risk manager must know today the likelihood that his portfolio will decline in the future. An option trader will want to know the volatility that can be expected over the future life of the contract. To hedge this contract he will also want to know the volatility of his forecast. A portfolio manager may want to sell a stock or a portfolio before it becomes too volatile. A market maker may want to set the bid ask spread wider when the future is believed to be more volatile.*

A good volatility model is the one that competently forecasts volatility:

- **1.** Volatility is persistent.
- **2.** Volatility is mean-reverting.
- **3.** Market returns may have asymmetric impact on volatility.
- **4.** External (exogenous) variables may affect volatility.

Persistence of volatility is sometimes referred to as "volatility clustering." The phenomenon describes the observed persistence in the levels of volatility; if volatility is high today, it is likely to be high tomorrow. The converse is also true; volatility that is low during the current observation period is likely to remain low in the next observation period. The observed volatility persistence implies that "shocks" (unusually large price moves) will impact expected volatility measures many observation periods ahead. According to Engle and Patton (2001), the impact of shocks on future volatility expectations declines geometrically but can be seen in options data as long as one year after the occurrence of the shock.

The mean-reversion properties of volatility describe the phenomenon whereby volatility regresses to its optimal intrinsic levels. Thus, if volatility is unusually high one period and, due to persistence, will remain high for several observation periods, it will nevertheless eventually fall to its normal level. A useful tool for comparing volatility models is to compare the models' forecasts many periods ahead. According to the mean-reversion property of volatility, long-term forecasts of all volatility models should converge on the same intrinsic volatility value, a finite number.

Positive and negative shocks to market returns have been found to impact subsequent volatility differently. Market crashes and other negative shocks have been shown to result in higher subsequent volatility levels than rallies and other news favorable to the market. This asymmetric property of volatility generates skews in volatility surfaces constructed of option-implied volatilities for different option strike prices. Engle and Patton  $(2001)$  cite the following example of volatility skews: the implied volatilities of in-the-money put options are lower than those of at-themoney put options. Furthermore, the implied volatilities of at-the-money put options are lower than the implied volatilities of out-of-the-money options.

Finally, volatility forecasts may be influenced by external events, such as news announcements. In foreign exchange, for example, price and return volatility of a particular currency pair increase markedly during macroeconomic announcements pertaining to one or both sides of the currency pair.

Volatility can be forecasted in a number of ways. The simplest volatility forecast assumes that the volatility remains constant through time and that, as a result, future volatility will be equal to the volatility estimate obtained from historical data. In this case, the forecast for future squared volatility,  $\sigma_{t+1}^2$ , is just the variance of the past returns of the security or portfolio under consideration:

$$E_t\left[\sigma_{t+1}^2\right] = \sigma_t^2 = \sigma^2 = \frac{1}{t-1} \sum_{\tau=1}^t \left(R_\tau - \overline{R}\right)^2 \tag{8.22}$$

Of course, volatility may change with time. Securities that exhibit timevarying volatility are said to possess "heteroscedastic" properties, with the **104** HIGH-FREQUENCY TRADING

term "heteroscedasticity" referring to the varying volatility; the term "homoscedasticity" describes constant volatility.

One way to model volatility that changes with time is to assume that it stays constant over short periods of time, known as volatility estimation windows. To do so, the volatility is forecasted as the volatility over the time window of returns on the security of interest:

$$E_{t} \left[ \sigma_{t+1}^{2} \right] = \frac{1}{T-1} \sum_{\tau=t-T+1}^{t} \left( R_{\tau} - \overline{R}_{t} \right)^{2} \tag{8.23}$$

where 
$$\overline{R}_t = \frac{1}{T} \sum_{\tau = t - T + 1}^t R_\tau$$
 (8.24)

Similar to moving average estimation, the window used in volatility estimation is then moved through time to obtain the latest estimates. According to the central limit theorem, the return window used for estimation of each individual volatility forecast should contain at least 30 observations. The time spaces between subsequent returns used within the window can be made as short as required—thirty 1-second returns can be used to estimate intraminute volatility.

The moving window approach to volatility estimation places equal weight on all the observations in the sample. The earliest changes in returns are given the same weights as the latest changes, but the latest changes may possess more relevance to the present time and forecasting of future returns. To address this issue, several weighting schemes for returns within a volatility estimation window have been proposed.

The simplest observation weighting scheme is linear or triangular weighting: each of the *T* observations within the window is multiplied by a coefficient that reflects the order of the observation within the window. The earliest observation is given the lowest weight, and the latest observations are given the highest significance. The resulting forecast of variance at time *t* + 1 is then computed as follows:

$$E_t\left[\sigma_{t+1}^2\right] = \sum_{\tau=t-T+1}^t \left(\frac{\tau-t+T}{T}R_\tau - \overline{R}_t\right)^2 \tag{8.25}$$

where 
$$\overline{R}_t = \sum_{\tau=t-T+1}^t \frac{\tau-t+T}{T} R_\tau$$
 (8.26)

An exponential weighting scheme also gives special significance to later observations. The scheme uses a geometric coefficient, λ, for weighting observations within the volatility estimation window. The geometric coefficient is known as the "smoothing parameter" and is used in estimation as follows:

$$E_t\left[\sigma_{t+1}^2\right] = \sum_{\tau=t-T+1}^t \left(\lambda^{t-\tau}(1-\lambda)R_\tau - \overline{R}_t\right)^2 \tag{8.27}$$

where 
$$\overline{R}_{t} = \sum_{\tau=t-T+1}^{t} \left[ \lambda^{t-\tau} (1-\lambda) R_{\tau} \right] \tag{8.28}$$

The smoothing parameter is normally estimated on historical data using maximum likelihood. RiskMetricsTM estimates λ to be 0.94, but λ may vary from security to security and with changes in the number of observations, *T*, used in the volatility estimation window.

Figure 8.2 graphically compares the shapes of the weights used in volatility estimation under the simple, equally weighted moving window, the triangular moving window, and the exponential moving window.

Panel A: Equally weighted estimation

![](_page_14_Figure_8.jpeg)

**FIGURE 8.2** Panel A: Equally weighted estimation.

The moving window estimators of volatility fail to model an important characteristic of volatility—"volatility clustering." Volatility clustering describes the phenomenon of volatility persistence. Current high volatility does not typically revert to lower volatility levels instantaneously; instead, high volatility persists for several time periods. The same observation holds for low volatility; low volatility at present is likely to lead to low volatility in the immediate future.

To model the observed volatility clustering, researchers use ARMA technique on volatilities:

$$\sigma_t^2 = \alpha_0 + \sum_{i=1}^m \alpha_i a_{t-i}^2 + \sum_{j=1}^s \beta_j \sigma_{t-j}^2 \tag{8.29}$$

where  $a_t = \sigma_t z_t$ , where  $\{z_t\}$  is a sequence of independent, identically distributed random variables with mean  $0$  and variance 1. Additional stationarity conditions include  $\alpha_0 > 0$ ,  $\alpha_i \ge 0$ ,  $\beta_j \ge 0$ , and  $\sum_{k=1}^{\max(m,s)} (\alpha_k + \beta_k) < 1$ . Such a volatility model is known as a generalized autoregressive conditional heteroscedasticity (GARCH) process, proposed by Bollerslev (1986), extending the ARCH specification of Engle (1982).

GARCH parameters are typically estimated recursively using maximum likelihood with the model's observation  $\sigma_0$  "seeded" with a windowestimated volatility value. Various extensions to the GARCH specification include additional explanatory right-hand side variables controlling for external events, an exponential "EGARCH" specification that addresses the asymmetric response of returns to positive and negative shocks (bad news is typically accompanied by a higher volatility than good news), and a "GARCH-M" model in which the return of a security depends on the security's volatility, among numerous other GARCH extensions.

In addition to the moving window and GARCH volatility estimators, popular volatility measurements include the intraperiod volatility estimator, known as the "realized volatility;" several measures based on the intraperiod range of prices; and a stochastic volatility model where volatility is thought to be a random variable drawn from a prespecified distribution. The realized volatility due to Andersen, Bollerslev, Diebold, and Labys  $(2001)$  is computed as the sum of squared intraperiod returns obtained by breaking a time period into  $n$  smaller time increments of equal duration:

$$RV_t = \sum_{i=1}^{n} r_{t,i}^2 \tag{8.30}$$

The range-based volatility measures are based on combinations of open, high, low, and close prices for every period under consideration. Garman and Klass (1980), for example, find that all of the following volatility estimators are less noisy than the conventional estimator based on the variance of returns  $(O_t, H_t, L_t)$ , and  $C_t$  denote the open, high, low, and close prices for period  $t$ , respectively):

$$\hat{\sigma}_{1,t}^2 = \frac{(O_t - C_{t-1})^2}{2f} + \frac{(C_t - O_t)^2}{2(1-f)}, \ 0 < f < 1 \tag{8.31}$$

$$\hat{\sigma}_{2,t}^2 = \frac{(H_t - L_t)^2}{4\ln(2)}\tag{8.32}$$

$$\hat{\sigma}_{3,t}^2 = 0.17 \frac{(O_t - C_{t-1})^2}{f} + 0.83 \frac{(H_t - L_t)^2}{(1 - f)4 \ln(2)}, \ 0 < f < 1 \quad (8.33)$$

$$\hat{\sigma}_{5,t}^{2} = 0.5(H_t - L_t)^{2} - [2\ln(2) - 1](C_t - O_t)^{2}$$
(8.34)

$$\hat{\sigma}_{6,t}^2 = 0.12 \frac{(O_t - C_{t-1})^2}{f} + 0.88 \frac{\hat{\sigma}_{5,t}^2}{1 - f}, \ 0 < f < 1 \tag{8.35}$$

GARCH estimators assume that volatility is a deterministic function of lagged observations and their variances. The deterministic condition can be restrictive and fail to reflect the dynamic nature of volatility. A different class of volatility estimators, known as stochastic volatility estimators, have been developed to allow modeling of heteroscedasticity and volatility clustering without the functional form restrictions on volatility specification.

The simplest stochastic volatility estimator can be specified as follows:

$$v_t = \sigma_t \xi_t = \varsigma \exp(\alpha_t/2) \xi_t \tag{8.36}$$

where  $\alpha_t = \phi \alpha_{t-1} + \eta_t$  is the parameter modeling volatility persistence,  $|\phi| < 1, \xi_t$  is an identically and independently distributed random variable with mean 0 and variance 1, and  $\zeta$  is a positive constant.

While stochastic volatility models reflect well the random nature underlying volatility processes, stochastic volatility is difficult to estimate. The parameters of equation  $(8.36)$  are often estimated using an econometric technique known as maximum likelihood or its close cousins. Given the randomness of the stochastic volatility estimator, the estimation process is quite complex. Estimation of GARCH can seem trivial in comparison with the estimation of stochastic volatility.

# **NONLINEAR MODELS**

# **Overview**

As their name implies, nonlinear models allow modeling of complex nontrivial relationships in the data.

Unlike linear models discussed in the first section of this chapter, nonlinear models forecast random variables that cannot be expressed as linear combinations of other, contemporaneous or lagged, random variables with well-defined distributions. Instead, nonlinear models can be expressed as some functions *f*(.) of other random variables. In mathematical terms, if a linear model can be expressed as shown in equation (8.37), reprinted here for convenience, then nonlinear models are best expressed as shown in equation (8.38) which follows:

$$y_t = \alpha + \sum_{i=0}^{\infty} \beta_i x_{t-i} + \varepsilon_t \tag{8.37}$$

$$y_t = f(x_t, x_{t-1}, x_{t-2}, \cdots) \tag{8.38}$$

where {*yt*} is the time series of random variables that are to be forecasted, {*xt*} is a factor significant in forecasting {*yt*}, and α and β are coefficients to be estimated.

The one-step-ahead nonlinear forecast conditional on the information available in the previous period is usually specified using a Brownian motion formulation, as shown in equation (8.39):

$$y_{t+1} = \mu_{t+1} + \sigma_{t+1}\xi_{t+1} \tag{8.39}$$

where µ*<sup>t</sup>*+<sup>1</sup> = *Et*[*yt*+1] is the one-period-ahead forecast of the mean of the variable being forecasted, σ*<sup>t</sup>*+<sup>1</sup> =  var*t*[*xt*+1] is the one-period-ahead forecast of the volatility of the variable being forecasted, and ξ*<sup>t</sup>*+<sup>1</sup> is an identically and independently distributed random variable with mean 0 and variance 1. The term ξ*<sup>t</sup>*+<sup>1</sup> is often referred to as a standardized shock or innovation.

The nonlinear estimation is often used in pricing derivatives and other complex financial instruments. In fact, many readers will recognize equation (8.39) as the cornerstone equation of derivatives pricing models.

Here, we will briefly review the following nonlinear estimation methods:

- Taylor series expansion (bilinear models)
- Threshold autoregressive model

109

- Markov switching model
- Nonparametric estimation
- Neural networks

For a detailed examination of nonlinear estimation, please see Priestley (1988) and Tong (1990).

# **Taylor Series Expansion (Bilinear Models)**

One of the simplest ways to deal with nonlinear functions is to linearize them using the Taylor series expansion. The Taylor series expansion of a univariate function  $f(x)$ , for any x in the vicinity of some specific value a, is a derivative-based approximation of the function  $f(x)$  and is defined as follows:

$$f(x) = f(a) + (x - a) \frac{df(x)}{dx} \bigg|_{x=a} + \frac{1}{2} (x - a)^2 \frac{d^2 f(x)}{dx^2} \bigg|_{x=a} + o(f(x)) \tag{8.40}$$

where  $f(a)$  is the value of the function  $f(x)$  at point  $a$ ,  $\frac{df(x)}{dx}|_{x=a}$  is the slope of the function  $f(x)$  at  $x = a$ ,  $\frac{d^2 f(x)}{dx^2}|_{x=a}$  is the curvature of the function  $f(x)$ at point a, and  $o(f(x))$  are higher-order derivative terms of the function  $f(x)$ . The higher-order derivative terms  $o(f(x))$  are generally small and are routinely ignored in estimation. $^{1}$ 

Granger and Andersen  $(1978)$  showed that equation  $(8.40)$  translates into the following linear econometric equation:

$$y_{t} = \alpha + \sum_{i=1}^{p} \phi_{i} y_{t-i} - \sum_{j=1}^{q} \theta_{j} x_{t-j} + \sum_{i=1}^{m} \sum_{j=1}^{s} \beta_{ij} y_{t-i} x_{t-j} + \varepsilon_{t}$$
(8.42)

where  $p, q, m$ , and s are nonnegative integers.

$$f(x,z) = f(a,b) + (x-a)\frac{df(x,z)}{dx}\bigg|_{x=a} + (z-b)\frac{df(x,z)}{dz}\bigg|_{z=b}$$
  
+  $\frac{1}{2}(x-a)^2\frac{d^2f(x,z)}{dx^2}\bigg|_{x=a} + \frac{1}{2}(z-b)^2\frac{d^2f(x,z)}{dz^2}\bigg|_{z=b}$  (8.41)  
+  $(x-a)(z-b)\frac{d^2f(x,z)}{dxdz}\bigg|_{x=a,z=b} + o(f(x,z))$ 

<sup>&</sup>lt;sup>1</sup>The Taylor series expansion of a bivariate function  $f(x, z)$ , for any x in the vicinity of some points  $x = a$  and  $z = b$ , includes a cross-derivative and is specified as follows:

Taylor series expansions can be used in estimation of cross-market derivative/underlying security arbitrage.

# **Threshold Autoregressive (TAR) Models**

Threshold autoregressive (TAR) models approximate nonlinear functions with piecewise linear estimation with thresholds defined on the dependent variable. For example, the model may have different specifications for positive and negative values of the dependent variable, in addition to separate linear models for large positive and large negative values. Such specification can be used in estimation of statistical arbitrage models. Figure 8.3 illustrates the idea.

An example of the TAR of Figure 8.3 may be the following AR(1) specification:

$$y_{t} = \begin{cases} -5y_{t-1} + \varepsilon_{t}, \text{ if } y_{t-1} < \text{Threshold 1} \\ 5y_{t-1} + \varepsilon_{t}, \text{ if } y_{t-1} \in (\text{Threshold 1}, \text{ Threshold 2}) \\ -5y_{t-1} + \varepsilon_{t}, \text{ if } y_{t-1} \in (\text{Threshold 2}, \text{ Threshold 3}) \\ 5y_{t-1} + \varepsilon_{t}, \text{ if } y_{t-1} > \text{Threshold 3} \end{cases}$$
(8.43)

The major problem of the TAR models is the models' discontinuity at thresholds. Smooth transition AR (STAR) models have been proposed to address the discontinuities of the TAR models. For detailed treatment of STAR models, please see Chan and Tong (1986) and Terasvirta (1994). ¨

# **Markov Switching Models**

Markov models are models with a finite number of mutually exclusive "states"; the states can be defined as value intervals between successive thresholds as in TAR models discussed previously, or as some discrete values potentially reflecting exogenous variables such as states of overall economy and the like. Contrary to TAR models, in Markov models each state has a discrete probability of transitioning into another state. The

![](_page_19_Figure_9.jpeg)

**FIGURE 8.3** Piecewise linear approximation of a nonlinear function.

transition probabilities are often estimated from historical data or determined analytically from theory.

An example of a two-state Markov model with a linear AR(1) specification in each state can be of the following nature:

$$y_{t} = \begin{cases} -5y_{t-1} + \varepsilon_{t}, \, if s_{t} = 1\\ 5y_{t-1} + \varepsilon_{t}, \, if s_{t} = 2 \end{cases} \tag{8.44}$$

where *st* denotes the "state" of *yt*, however the state is defined, and state transition probabilities are specified as follows:

$$P(s_t = 2|s_{t-1} = 1) = p_1$$
  

$$P(s_t = 1|s_{t-1} = 1) = 1 - p_1$$
  

$$P(s_t = 1|s_{t-1} = 2) = p_2$$
  

$$P(s_t = 2|s_{t-1} = 2) = 1 - p_2$$
  
(8.45)

Using the advanced statistical properties of the Markov processes, it can be shown that the expected proportion of time that the 2-state Markov process spends in state 1 is 1/*p*1, while the expected proportion of time that the 2-state Markov process spends in state 2 is 1/*p*2.

Markov switching models can be used in estimation of inter-trade durations and execution probabilities in limit order-based trading and other optimizations of execution. Markov switching models can also be applied in estimation of cross-market arbitrage opportunities.

# **Nonparametric Estimation of Nonlinear Models**

Nonparametric estimation denotes a broad class of econometric models that generally refers to econometric estimation without any assumptions as to the distribution of estimation errors or the shape of the function relating dependent and independent variables. One subclass of nonparametric models discussed here allows us to determine the functional relationship between dependent and independent variables directly from the historical data. Such nonparametric techniques boil down to smoothing the data into a functional form.

The nonparametric estimation of nonlinear models is designed to estimate the following function:

$$y_t = f(x_t) + \varepsilon_t \tag{8.46}$$

where {ε*t*} is the time series sequence of normally distributed errors and *f*(.) is an arbitrary, smooth function to be estimated. The simple average smoothing determines the value of *f*(*x*) at every point *x* = *X* by taking the across-time averages of both sides of equation  $(8.46)$  and utilizing the fact that  $E[\varepsilon] = 0$  by assumption:

$$E[y] = f(x) + E[\varepsilon] = f(x) \tag{8.47}$$

or, equivalently,

$$f(x) = \frac{1}{T} \sum_{t=1}^{T} y_t$$
 (8.48)

where  $T$  is the size of the sample.

To make sure that the estimation of  $f(x)$  considers only the values around x and not the values of the entire time series, the values of  $y_t$  can be weighted by a weight function,  $w_t(x)$ . The weight function is determined by another function, known as a "kernel function,"  $K_h(x)$ :

$$w_t(x) = \frac{K_h(x - x_t)}{\sum_{t=1}^T K_h(x - x_t)}$$
(8.49)

The weight function,  $w_t(x)$ , defines the location of the filter window that includes the  $y$  elements closest to the  $x$  being estimated at the moment and excludes all the  $y$ 's outside the filter window. The kernel function  $K_h(x)$  defines the shape of the filter window. As the window is moved through the continuum of  $x$ 's, the  $y$  elements fall in and out of the estimation window to reflect their relevance to the estimation. Since the weights w have to add up to 1 for all values of y considered,  $K(x)$  can be defined as the probability density function with  $K_h(x) \ge 0$  and  $\int K_h(z) dz = 1$ . Figure 8.4 shows the process of kernel estimation using the Gaussian kernel specified as the density of the normal distribution:

$$K_h(x) = \frac{1}{h\sqrt{2\pi}} \exp\left(-\frac{x^2}{2h^2}\right)$$

![](_page_21_Figure_10.jpeg)

**FIGURE 8.4** Kernel smoothing using a normal-density kernel.

The width of the estimation window can be controlled through a parameter known as bandwidth that enters the kernel function as shown in equation  $(8.50)$ :

$$K_h(x) = \frac{1}{h}K(x/h) \tag{8.50}$$

Fan and Yao (2003) determine the optimal bandwidth parameter  $h$  to be  $1.06sT^{-0.2}$ , where s is the sample standard error of x and T is the total size of the sample.

Kernel smoothing with different kernel functions is commonly used to filter the data—that is, to eliminate outliers and other noise.

#### Neural Networks

Neural networks are an example of semiparametric estimation. The term "neural network" is sometimes perceived to signal advanced complexity of a high-frequency system. In reality, neural networks are built instead to simplify algorithms dealing with econometric estimation.

A neural network is, in essence, a collection of interconnected rules that are selectively and sequentially triggered, depending on which conditions are satisfied in the real-time data. Caudill (1988, p. 53) defines a neural network as "a computing system made up of a number of simple, highly interconnected processing elements, which process information by their dynamic state response to external inputs." The simplest neural network can be built as shown in Figure  $8.5$ .

Advanced neural networks can comprise multiple decisions based on numerous simultaneous inputs. Neural networks can also incorporate feedback mechanisms whereby outputs of the previous periods are taken as inputs, for example.

![](_page_22_Figure_9.jpeg)

**FIGURE 8.5** A simple neural network that forecasts return values on the basis of the value of the previous return value. The forecast parameters  $\hat{\alpha}_1$ ,  $\hat{\alpha}_2$ ,  $\hat{\beta}_1$ ,  $\hat{\beta}_2$  are estimated from historical data.

The main advantage of neural networks is their simplified step-by-step structure that can significantly speed up execution of the forecasting algorithm. Neural networks are classified as semiparametric estimation tools, given that the networks may incorporate both distributional assumptions and rule-based systems in estimating and forecasting desired variables.

# **CONCLUSION**

The field of econometrics provides a wide range of tools to model statistical dependencies in the data. Linear models assume that data dependencies are direct, or linear, while nonlinear models comprise a set of functions for more involved relationships. Chapter 9 discusses additional high-frequency estimation models.
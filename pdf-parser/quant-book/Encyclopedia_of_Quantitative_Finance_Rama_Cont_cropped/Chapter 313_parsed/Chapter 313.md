# Backtesting

The term *backtesting* is used in several ways in finance. Most commonly, backtesting denotes either (i) an assessment of the hypothetical historical performance of a suggested trading strategy or (ii) the evaluation of financial risk models using historical data on risk forecasts and profit and loss realizations. The following discussion is about the evaluation of risk models.

The procedure is to consider the daily *ex ante* risk measure forecasts from a model and test it against the daily ex post realized portfolio loss. The risk measure forecast could take the form of a Value-at-Risk (VaR), an expected shortfall, or a distributional forecast. The goal is to be able to backtest any of these risk measures of interest. The backtesting procedures can be seen as a final diagnostic check on the risk model carried out by the risk management team that constructed the risk model, or they can be used by external model evaluators such as bank supervisors.

Evidence on actual bank VaRs and their backtesting performance can be found in  $[7, 22, 28,$ 29, 31]. The regulatory considerations involved in backtesting are detailed by the Basel Committee on Banking Supervision [2–4]. Lopez [24] analyzes the regulatory approach to backtesting and Campbell [9] provides a survey of backtesting that includes a discussion of regulatory considerations. Backtesting of credit risk models is investigated in [25].

First, we discuss procedures for backtesting the VaR metric (see Value-at-Risk; Market Risk). Second, we consider increasing backtesting power by using explanatory variables to backtest the VaR. Third, we consider the increasing power by backtesting risk measures other than VaR, and we discuss various other issues in backtesting.

## **Backtesting VaR**

By now, VaR is by far the most popular portfolio risk measure used by risk management practitioners. The VaR revolution in risk management was triggered by JP Morgans RiskMetrics approach launched in 1994. Supervisory authorities immediately recognized the need for methods to backtest VaR and the first research on backtesting was published soon after in

[21, 23]. Christoffersen [10] extended Kupiec's test of unconditional VaR coverage to tests of conditional VaR coverage. These concepts are defined later.

#### Defining the Hit Sequence

First, define  $VaR_{t+1}^p$  to be a number constructed on day t such that the portfolio losses on day  $t + 1$ will only be larger than the  $VaR_{t+1}^p$  forecast with probability  $p$ . If we observe a time series of past ex ante VaR forecasts and past ex post losses, PL, we can define the "hit sequence" of VaR violations as

$$I_{t+1} = 1$$
 if  $PL_{t+1} > VaR_{t+1}^p$  (1)

$$= 0 \qquad \text{if} \qquad PL_{t+1} < VaR_{t+1}^p \qquad (2)$$

The hit sequence returns a 1 on day  $t + 1$  if the loss on that day is larger than the VaR number predicted in advance for that day. If the VaR is not exceeded (or violated), then the hit sequence returns a 0. When backtesting the risk model, we construct a sequence  $\{I_{t+1}\}_{t=1}^T$  across T days, indicating when the past violations occurred.

#### The Null Hypothesis

If we use the perfect VaR model, then given all the information available to us at the time the VaR forecast is made, we should not be able to predict whether the VaR will be violated. We should be expecting a  $1$  in the hit sequence with probability  $p$  and we should be expecting a 0 with probability  $1 - p$  and the occurrences of the hits should be random over time.

We say that a risk model has correct *unconditional* VaR coverage if  $Pr(I_{t+1} = 1) = p$  and we say that a risk model has correct conditional VaR coverage if  $Pr_t(I_{t+1} = 1) = p$ . Roughly speaking, correct *unconditional* VaR coverage just means that the risk model delivers VaR hits with probability  $p$  on average across the days. Correct *conditional* VaR coverage means that the risk model gives a VaR hit with probability  $p$  on every day given all the information available on the day before. Note that correct conditional coverage implies correct unconditional coverage but not vice versa.

We can think of VaR backtesting as testing the hypothesis:

$$H_0: I_{t+1} \sim \text{i.i.d. Bernoulli}(p)$$
 (3)

If  $p$  is one half, then the i.i.d. Bernoulli distribution describes the distribution of getting a head when tossing a fair coin. When backtesting risk models,  $p$  will not be one half but instead on the order of  $0.01$  or  $0.05$  depending on the coverage rate of the VaR. The hit sequence from a correctly specified risk model should look like a sequence of random tosses of a coin that comes up heads  $1$  or  $5\%$  of the time depending on the VaR coverage rate.

Note that, in general, the expected value of a binary sequence is simply the probability of getting a 1:

$$E_t \left[ I_{t+1} \right] = \Pr_t \left( I_{t+1} = 1 \right) 1 + \Pr_t \left( I_{t+1} = 0 \right) 0$$
  
=  $\Pr_t \left( I_{t+1} = 1 \right) \equiv \pi_{t+1|t}$  (4)

We denote this conditional hit probability by  $\pi_{t+1|t}$ and its unconditional counterpart is defined  $E[I_{t+1}] \equiv \pi.$ 

We can therefore construct the following null hypothesis of correct conditional coverage for the hit sequence from a VaR model

$$H_0: E_t \left[ I_{t+1} \right] = \pi_{t+1|t} = p \tag{5}$$

namely that the conditionally expected value of the hit sequence at time  $t + 1$ , given all the information available at time  $t$  is the promised VaR coverage rate  $p$ .

#### Unconditional Coverage Testing

First, we want to test if the unconditional probability of a violation in the risk model,  $\pi$ , is significantly different from the promised probability,  $p$ . We call this the *unconditional coverage hypothesis*. We can write  $H_0: E[I_t] \equiv \pi = p$ .

The expected value of the hit sequence can be estimated by the sample average,  $\hat{\pi} = \frac{1}{T} \sum_{t=1}^{T} I_t = T_1/T$ , where  $T_1$  is the number of 1s in the sample. Note that if the null hypothesis is true, we have that  $E\left[\hat{\pi}\right] = E\left[\frac{1}{T}\sum_{t=1}^{T} I_t\right] = p$ . Assuming that the observations on the hit sequence are independent over time, the variance of the  $\hat{\pi}$  estimate is  $1/T \text{ Var}(I_t)$ where Var  $(I_t)$  can be estimated as the sample variance of the hit sequence. The hypothesis that  $E[I_t] =$  $p$  can therefore be tested in a simple means test

$$MT = \sqrt{T} \frac{\hat{\pi} - p}{\sqrt{Var(I_t)}} \sim N(0, 1) \tag{6}$$

We can also implement the unconditional coverage test as a likelihood ratio test. For this, we write the likelihood of an i.i.d. Bernoulli( $\pi$ ) hit sequence:

$$L(\pi) = \prod_{t=1}^{T} (1-\pi)^{1-I_{t+1}} \pi^{I_{t+1}} = (1-\pi)^{T_0} \pi^{T_1} \quad (7)$$

where  $T_0$  and  $T_1$  are the number of 0s and 1s in the sample. We can easily estimate  $\pi$  from  $\hat{\pi} = T_1/T$ , that is, the observed fraction of violations in the sequence. Plugging the ML estimates back into the likelihood function gives the optimized likelihood as

$$L\left(\hat{\pi}\right) = \left(1 - \frac{T_1}{T}\right)^{T_0} \left(\frac{T_1}{T}\right)^{T_1} \tag{8}$$

Under the unconditional coverage null hypothesis that  $\pi = p$ , where p is the known VaR coverage rate, we have the likelihood

$$L(p) = \prod_{t=1}^{T} (1-p)^{1-I_{t+1}} p^{I_{t+1}} = (1-p)^{T_0} p^{T_1} \quad (9)$$

And we can check the unconditional coverage hypothesis using a likelihood ratio test

$$LR_{uc} = -2\ln\left[\frac{L\left(p\right)}{L\left(\hat{\pi}\right)}\right] \sim \chi_{1}^{2} \qquad (10)$$

Asymptotically, that is, as the number of observations,  $T$ , goes to infinity, the test will be distributed as a  $\chi^2$  with one degree of freedom.

The choice of significance level comes down to an assessment of the costs of making two types of mistakes: we could reject a correct model (type I error) or we could fail to reject (that is accept) an incorrect model (type II error). Increasing the significance level implies larger type I errors but smaller type II errors and vice versa. In academic work, a significant level of 1, 5, or  $10\%$  is typically used. In risk management, type II errors may be very costly so that a significance level of 10% may be appropriate.

Often, we do not have a large number of observations available for backtesting, and we certainly will typically not have a large number of violations,  $T_1$ , which are the informative observations. It is, therefore, often better to rely on Monte-Carlo-simulated P values rather than those from the  $\chi^2$  distribution. Christoffersen and Pelletier [14] discuss how

to implement the  $[17]$  Monte Carlo *P*-values in a backtesting setting.

#### Independence Testing

There is strong evidence of time-varying volatility in daily asset returns as surveyed in [1]. If the risk model ignores such dynamics, then the VaR will react slowly to the changing market conditions and VaR violations will appear clustered in time. Pritsker [30] illustrates this problem using VaRs computed from historical simulation. If the VaR violations are clustered, then the risk manager can essentially predict that if today has a VaR hit, then there is a probability larger than  $p$  of getting a hit tomorrow, which violates that the VaR is based on an adequate model. This is clearly not satisfactory. In such a situation, the risk manager should increase the VaR in order to lower the conditional probability of a violation to the promised  $p$ .

The most common way to test for dynamics in time series analysis is to rely on the autocorrelation function and the associated portmanteau or Ljung-Box-type tests. We can implement this approach for backtesting as well. Let  $\gamma_k$  be the autocorrelation at lag k for the hit sequence. Plotting  $\gamma_k$ against k for  $k = 1, \ldots, m$  will give a visual impression of the correlation of between a hit in one of the last  $m$  trading days and a hit today. The Ljung-Box test provides a formal check of the null hypothesis that all of the first  $m$  autocorrelations are zero against the alternative that any of them is not. The test is easily constructed as

$$LB(m) = T (T + 2) \sum_{k=1}^{m} \frac{\gamma_k^2}{T - k} \sim \chi_m^2 \qquad (11)$$

where  $\chi^2_m$  denotes the chi-squared distribution with  $m$  degrees of freedom. Berkowitz *et al.* [6] find that setting  $m = 5$  gives good testing power in a realistic daily VaR backtesting setting.

Independence testing can also be done using the likelihood approach. Assume that the hit sequence is dependent over time and that it can be described as a first-order Markov sequence with transition probability matrix:

$$\Pi_1 = \begin{bmatrix} 1 - \pi_{01} & \pi_{01} \\ 1 - \pi_{11} & \pi_{11} \end{bmatrix} \n$$
(12)

These transition probabilities simply mean that conditional on today being a nonviolation (i.e.,  $I_t = 0$ ) then the probability of tomorrow being a violation (i.e.,  $I_{t+1} = 1$ ) is  $\pi_{01}$ . The probability of tomorrow being a violation given today is also a violation is  $\pi_{11} = \Pr(I_t = 1 \text{ and } I_{t+1} = 1)$ . The probability of a nonviolation following a nonviolation is  $1 - \pi_{01}$  and the probability of a nonviolation following a violation is  $1 - \pi_{11}$ .

If we observe a sample of  $T$  observations, then we can write the likelihood function of the first-order Markov process as

$$L\left(\Pi_{1}\right) = \left(1 - \pi_{01}\right)^{T_{00}} \pi_{01}^{T_{01}} \left(1 - \pi_{11}\right)^{T_{10}} \pi_{11}^{T_{11}} \quad (13)$$

where  $T_{ij}$ ,  $i, j = 0, 1$ , is the number of observations with a  $j$  following an  $i$ . Taking first derivatives with respect to  $\pi_{01}$  and  $\pi_{11}$  and setting these derivatives to zero, one can solve for the maximum likelihood estimates:

$$\hat{\pi}_{01} = \frac{T_{01}}{T_{00} + T_{01}}, \quad \hat{\pi}_{11} = \frac{T_{11}}{T_{10} + T_{11}} \tag{14}$$

Then using the fact that the probabilities have to sum to one, we have  $\hat{\pi}_{00} = 1 - \hat{\pi}_{01}$ ,  $\hat{\pi}_{10} = 1 - \hat{\pi}_{11}$ .

Allowing for dependence in the hit sequence corresponds to allowing  $\pi_{01}$  to be different from  $\pi_{11}$ . Positive dependence is a matter of concern, which amounts to the probability of a violation following a violation  $(\pi_{11})$  being larger than the probability of a violation following a nonviolation  $(\pi_{01})$ . If, on the other hand, the hits are independent over time, then the probability of a violation tomorrow does not depend on today being a violation or not and we write  $\pi_{01} = \pi_{11} = \pi$ . We can test the independence hypothesis that  $\pi_{01} = \pi_{11}$  using a likelihood ratio test

$$LR_{\text{ind}} = -2 \ln \left[ \frac{L\left(\hat{\pi}\right)}{L\left(\hat{\Pi}_1\right)} \right] \sim \chi_1^2 \qquad (15)$$

where  $L(\hat{\pi})$  is the likelihood under the alternative hypothesis from the  $LR_{\text{uc}}$  test.

Other methods for independence testing based on the duration of time between hits can be found in [14].

#### **Backtesting with Information Variables**

The preceding tests are quick and easy to implement. However, as they only use information on past VaR hits, they might not have much power to detect misspecified risk models. To increase the testing power, we consider using the information in past market variables, such as interest rate spreads or volatility measures. The basic idea is to test the model using information that may explain when violations occur. The advantage of increasing the information set is not only to increase power but also to help us understand the areas in which the risk model is misspecified. This understanding is key in improving the risk models further.

If we define the  $q$ -dimensional vector of information variables available to the backtester at time  $t$  as  $X_t$ , then the null hypothesis of a correct risk model can be written as

$$H_0: \Pr(I_{t+1} = 1 | X_t) = p \Leftrightarrow E[I_{t+1} - p | X_t] = 0$$
(16)

The hypothesis says that the conditional probability of getting a VaR violation on day  $t + 1$  should be independent of any variable observed at time  $t$  and it should simply be equal to the promised VaR coverage rate,  $p$ . This hypothesis is equivalent to the conditional expectation of the hit sequence less  $p$  being equal to  $0$ .

Engle and Manganelli [18] develop a conditional autoregressive VaR by regression quantiles approach. For backtesting, they suggest the following dynamic quantile test:

$$DQ = \frac{(I - p)' X (X'X)^{-1} X' (I - p)}{(Tp (1 - p))} \sim \chi_q^2 (17)$$

where X is the  $T \times q$  matrix of information variables, and  $(I - p)$  is the  $T \times 1$  vector of hits where each element has been subtracted by the desired covered rate  $p$ .

Berkowitz *et al.* [6] find that implementing the  $DQ$  test using simply the lagged VaR from a GARCH model as well as the lagged hit gives good power in a realistic daily VaR experiment. Smith [31] also finds good power when applying the  $DQ$  test. A regression-based approach to backtesting is also used in [11, 12]. Christoffersen et al. [13] develop tests for comparing different VaR models.

Smith [31] further suggests a probit approach where the potentially time-varying probability of a hit is modeled using the normal cumulative density function and where Lagrange multiplier tests are used.

When backtesting with information variables, the question of which variables to include in the vector  $X_t$  immediately arises. It is difficult to give a general answer as it depends on the particular portfolio at hand. It is likely that variables that are thought to be correlated with the future volatility in the portfolio are good candidates. In equity portfolios option, implied volatility measures such as the VIX would be an obvious candidate. In FX portfolios option, implied volatility measures could be constructed as well. In bond portfolios, variables such as term spreads and credit spreads are likely candidates as are variables capturing the level, slope, and curvature of the term structure.

#### **Other Issues in Backtesting**

When correctly specified, the one-day VaR measure tells the user that there is a probability  $p$  of losing more than the VaR over the next day. Importantly, it does not, for example, say how much one can expect to lose on the days where the VaR is violated. Thus, the VaR only contains partial information about the distribution of losses. This limitation of the VaR is reflected in the definition of the hit variable in equation (1), which in turn limits the possibilities for backtesting in the VaR setting. We can only backtest on the hit occurrences and not, for example, on the magnitude of the losses when the hits occur because the VaR does not promise hits of a certain magnitude.

#### Backtesting Expected Shortfall

The limitations of the VaR as a risk measure suggest alternative risk measures, most prominently expected shortfall  $(ES)$ , also referred to as *conditional VaR* (CVAR) (see Value-at-Risk; Market Risk), which denotes the expected loss on the days where the VaR is violated. We can define it formally as

$$ES_{t+1}^{p} = E_{t} \left[ PL_{t+1} | PL_{t+1} > VaR_{t+1}^{p} \right] \qquad (18)$$

Note that  $ES$  provides information on the expected magnitude of the loss whenever the VaR is violated. We now consider ways to backtest the  $ES$  risk measure

Consider again a vector of variables,  $X_t$ , which are known to the risk manager and which may help explain potential portfolio losses beyond what is explained by the risk model. The  $ES$  risk measure promises that whenever we violate the VaR, the expected value of the violation will be equal to  $ES_{t+1}^p$ . We can therefore test the  $ES$  measure by checking if the vector  $X_t$  has any ability to explain the deviation of the observed shortfall or loss,  $PL_{t+1}$ , from the expected shortfall on the days where the VaR was violated. Mathematically, we can write

$$PL_{t+1} - ES_{t+1}^p = b_0 + b_1' X_t + e_{t+1}$$
 for  
 $t+1 \text{ where } PL_{t+1} > VaR_{t+1}^p$  (19)

where  $t + 1$  now refers only to days where the VaR was violated. The observations where the VaR was not violated are simply removed from the sample. The error term  $e_{t+1}$  is assumed to be independent of the regressor,  $X_t$ .

To test the null hypothesis that the risk model from which the  $ES$  forecasts were made uses all information optimally  $(b_1 = 0)$  and that it is not biased  $(b_0 = 0)$ , we can jointly test that  $b_0 =$  $b_1 = 0.$ 

Note that now the magnitude of the violation shows up on the left-hand side of the regression. However, note that we can still only use information in the tail to backtest. The  $ES$  measure does not reveal any particular properties about the remainder of the distribution, and therefore we only use the observations where the losses were larger than the VaR.

Further, discussion of  $ES$  backtesting can be found in  $[26]$ .

#### Backtesting the Entire Distribution

Rather than focusing on particular risk measures from the loss distribution such as the VaR or the expected shortfall, we could instead decide to backtest the entire loss distribution from the risk model. This would have the benefit of potentially increasing further the power to reject bad risk models.

Assuming that the risk model produces a cumulative distribution of portfolio losses, call it  $F_t(*)$ . Then at the end of every day, after having observed the actual portfolio loss (or profit), we can calculate the risk model's probability of observing a loss below the actual. We denote this probability by  $p_{t+1} \equiv F_t \left( PL_{t+1} \right).$ 

If we use the correct risk model to forecast the loss distribution, then we should not be able to forecast the risk model's probability of falling below the actual return. In other words, the time series of observed probabilities  $p_{t+1}$  should be distributed independently over time as a  $Uniform(0,1)$  variable. We therefore want to consider tests of the null hypothesis:

$$H_0: p_{t+1} \sim \text{i.i.d. Uniform}(0, 1)$$
 (20)

The Uniform $(0,1)$  distribution function is flat on the interval 0-1 and 0 everywhere else. As the  $p_{t+1}$ variable is a probability, it is a must that it should lie in the  $0-1$  interval. Constructing a histogram and checking if it looks reasonably flat provide a useful visual diagnostic. If systematic deviations from a flat line appear in the histogram, then we would conclude that the distribution from the risk model is misspecified. A detailed discussion of this approach is found in  $[16]$ .

Unfortunately, testing the i.i.d. uniform distribution hypothesis is cumbersome due to the restricted support of the uniform distribution. However, we can transform the i.i.d. Uniform  $p_{t+1}$  to an i.i.d. standard normal variable,  $z_{t+1}$ , using the inverse cumulative distribution function,  $z_{t+1} = \Phi^{-1}(p_{t+1})$ . We are then left with a test of a variable conforming to the standard normal distribution, which can easily be implemented. The i.i.d. property of  $z_{t+1}$  can be assessed via the autocorrelation functions and by using the  $LB(m)$  test in equation (4) on  $z_{t+1}$  and  $|z_{t+1}|$ , for example. The normal distribution property can be tested using the method of moments approach in [8]. Regression-based tests using information variables can also be constructed. Further analysis of distribution backtesting can be found in  $[5, 15]$ .

## Dirty Profits and Losses

The backtesting procedures compare the ex ante forecast from a risk model to the *ex post* profit and losses  $(P/L)$ . It is therefore obviously essential, but unfortunately not always the case, that the *ex post* recorded  $P/L$  arise directly from the portfolio used to make the ex ante model predictions. The risk model will typically produce a risk forecast for the loss distributions of a particular portfolio of assets. The *ex post* profits and losses should only contain cash flows directly related to the portfolio of assets assumed in the risk models. However, the total *P/L* of a trading desk may contain trading commission revenues as well as costs that are not directly related to holding the portfolio of assets assumed in the risk model. This extraneous cash flows should be stripped from the *P/L* before backtesting.

The daily *P/L* may also include cash flows from intraday transactions, that is, the *P/L* from selling an asset that was bought the same day. Such cash flows are not directly related to the end-of-day portfolio entered into the risk model and should ideally be stripped away as well. A detailed discussion of these issues can be found in [27].

## *Multiple-day Horizons and Changing Portfolio Weights*

The backtesting procedures described earlier can be relatively easily adopted to the multiday risk-horizon setting. If, for example, a 10-day VaR forecast is observed daily along with the *ex post* 10-day *P/L*, then the hit sequence can be constructed daily as in equation (1). The 10-day VaR horizons implies that 9-day autocorrelation is to be expected in the hit sequence and that this should be allowed for when constructing its variance as in equation (6). Similarly, in the *DQ* test as in equation (17), one should use information variables available 10 days before the observed *P/L*. Smith [31] discusses backtesting with multiday VaRs.

# *Allowing for Risk Model Parameter Estimation Error*

In the discussion so far, we have abstracted from the fact that the risk models in use most likely contain parameters that are estimated with errors. This parameter estimation error will in turn render the hit sequence observed with error. As a consequence when backtesting the risk model, we may reject the "true" risk model just because its parameters were estimated with error. As discussed in [18], this is mainly an issue when the risk model is evaluated insample, that is, when the model is evaluated on the same data it was estimated on. In typical external

backtesting applications, the backtesting procedures are used in a more realistic out-of-sample manner where the model is estimated on data until day *t* and then used to forecast risk for day *t* + 1. In this setting, parameter estimation error is less likely to be critical. Parameter estimation issues in relation to VaR modeling has been analyzed in detail in [19, 20].

# **Acknowledgments**

The author is grateful for the financial support from FQRSC, IFM2, and SSHRC and from the Center for Research in Econometric Analysis of Time Series, CREATES, funded by the Danish National Research Foundation.

# **References**

- [1] Andersen, T., Bollerslev, T., Christoffersen, P. & Diebold, F. (2005). Practical volatility and correlation modeling for financial market risk management, in *Risks of Financial Institutions*, M. Carey & R. Stulz, eds, University of Chicago Press for NBER, pp. 513–548.
- [2] Basel Committee on Banking Supervision (1996). *Amendment to the Capital Accord to Incorporate Market Risks*, Bank for International Settlements.
- [3] Basel Committee on Banking Supervision (1996). *Supervisory Framework for the Use of 'Backtesting' in Conjunction With the Internal Models Approach to Market Risk Capital Requirements*, Bank for International Settlements.
- [4] Basel Committee on Banking Supervision (2004). *International Convergence of Capital Measurement and Capital Standards: a Revised Framework* .
- [5] Berkowitz, J. (2001). Testing density forecasts, applications to risk management, *Journal of Business and Economic Statistics* **19**, 465–474.
- [6] Berkowitz, J., Christoffersen, P. & Pelletier, D. (2007). *Evaluating Value-at-Risk Models with Desk-level Data*, Management Science, forthcoming.
- [7] Berkowitz, J. & O'Brien, J. (2002). How accurate are the Value-at-Risk models at commercial banks? *Journal of Finance* **57**, 1093–1112.
- [8] Bontemps, C. & Meddahi, N. (2005). Testing normality: a GMM approach, *Journal of Econometrics* **124**, 149–186.
- [9] Campbell, S. (2007). A review of backtesting and backtesting procedures, *Journal of Risk* **9**, 1–17.
- [10] Christoffersen, P. (1998). Evaluating interval forecasts, *International Economic Review* **39**, 841–862.
- [11] Christoffersen, P. (2003). *Elements of Financial Risk Management*, Academic Press.

- [12] Christoffersen, P. & Diebold, F. (2000). How relevant is volatility forecasting for financial risk management? *Review of Economics and Statistics* **82**, 1–11.
- [13] Christoffersen, P., Hahn, J. & Inoue, A. (2001). Testing and comparing Value-at-Risk measures, *Journal of Empirical Finance* **8**, 325–342.
- [14] Christoffersen, P.F. & Pelletier, D. (2004). Backtesting Value-at-Risk: a duration-based approach, *Journal of Financial Econometrics* **2**, 84–108.
- [15] Crnkovic, C. & Drachman, J. (1996). Quality control, *Risk* **9**, 138–143.
- [16] Diebold, F.X., Gunther, T. & Tay, A. (1998). Evaluating density forecasts, with applications to financial risk management, *International Economic Review* **39**, 863–883.
- [17] Dufour, J.-M. (2006). Monte Carlo tests with nuisance parameters: a general approach to finite-sample inference and nonstandard asymptotics in econometrics, *Journal of Econometrics* **133**, 443–477.
- [18] Engle, R.F. & Manganelli, S. (2004). CAViaR: conditional autoregressive Value-at-Risk by regression quantiles, *Journal of Business and Economic Statistics* **22**, 367–381.
- [19] Escanciano, J. & Olmo, J. (2007). *Estimation Risk Effects on Backtesting For Parametric Value-at-Risk Models*, City University London (Manuscript).
- [20] Giacomini, R. & Komunjer, I. (2005). Evaluation and combination of conditional quantile forecasts, *Journal of Business and Economic Statistics* **23**, 416–431.
- [21] Hendricks, D. (1996). Evaluation of Value-at-Risk models using historical data, *Economic Policy Review*, Federal Reserve Bank of New York, 39–69.
- [22] Jorion, P. (2002). How informative are Value-at-Risk disclosures? *Accounting Review* **77**, 911–931.

- [23] Kupiec, P. (1995). Techniques for verifying the accuracy of risk measurement models, *Journal of Derivatives* **3**, 73–84.
- [24] Lopez, J. (1999). Regulatory evaluation of Value-at-Risk models, *Journal of Risk* **1**, 37–64.
- [25] Lopez, J. & Saidenberg, M. (2000). Evaluating credit risk models, *Journal of Banking and Finance* **24**, 151–165.
- [26] McNeil, A. & Frey, R. (2000). Estimation of tailrelated risk measures for heteroskedastic financial time series: an extreme value approach, *Journal of Empirical Finance* **7**, 271–300.
- [27] O'Brien, J. & Berkowitz, J. (2005). Bank trading revenues, VaR and market risk, in *Risks of Financial Institutions*, M. Carey & R. Stulz, eds, University of Chicago Press for NBER.
- [28] Perignon, C., Deng, Z. & Wang, Z. (2006). *Do Banks Overstate their Value-at-Risk?*, HEC, Paris (Manuscript).
- [29] Perignon, C. & Smith, D. (2006). *The Level and Quality of Value-at-Risk Disclosure by Commercial Banks*, Simon Fraser University (Manuscript).
- [30] Pritsker, M. (2001). *The Hidden Dangers of Historical Simulation*, *Finance and Economics Discussion Series 2001–27* , Board of Governors of the Federal Reserve System.
- [31] Smith, D. (2007). *Conditional Backtesting of Value-at-Risk Models*, Simon Fraser University (Manuscript).

# **Related Articles**

## **Expected Shortfall**; **Market Risk**; **Model Validation**; **Value-at-Risk**.

PETER CHRISTOFFERSEN
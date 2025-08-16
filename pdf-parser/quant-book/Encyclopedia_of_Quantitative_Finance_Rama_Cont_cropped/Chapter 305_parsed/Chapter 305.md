# **Market Risk**

Market risk models were developed in the 1990s following the growth in proprietary trading in banking institutions. As an example, the chairman of Morgan asked his staff: "At the close of each business day, tell me what the market risks are across all businesses and locations." This led to quantitative risk measurements systems, such as Value at Risk (VAR), which aggregate risk at the top level of the institution, based on the most current positions.

The impetus for using VAR models came not only from the industry but also from financial regulators. Notably, the Basel Committee on Banking Supervision [2] allowed commercial banks to use their internal VAR models as the basis for their market risk charge, starting in 1998.

VAR summarizes the worst loss over a target horizon that will not be exceeded with a given level of confidence. For instance, in 1994, Morgan's daily VAR was approximately \$15 million at the 95% level of confidence over a horizon of one day. In other words, the bank should not expect to lose more than \$15 million in 95 days out of 100. Conversely, it should expect to lose \$15 million or more in the remaining 5 days out of 100. This single number describes the risk of the entire trading portfolio of the bank. Until then, risk was measured and managed at the level of a desk or business unit.

## **Portfolio Distributions**

VAR took hold as a universally accepted measure of risk because of its simplicity. It summarizes the downside risk in one measure, easy to understand, which is expressed in terms of a loss in the relevant currency. Because it is associated with a confidence level, it is sometimes called a *statistical measure of risk*.

The most useful aspect of VAR system, however, is the process that led to this number. To compute VAR, the institution has to set up systems to collect position and market data for the entire firm. From this information, its risk manager can build the entire probability density function of profits and losses over the risk horizon. As shown in Figure 1, VAR is just a quantile of the distribution. Specifying a confidence

![](_page_0_Figure_7.jpeg)

**Figure 1** Summarizing the distribution of losses

level *c*, this is the cutoff point such that the area to its left is precisely 1 − *c*.

If the distribution is normal, or more generally elliptical, the quantile can be derived from the standard deviation *σ* and a multiplier that is distributionspecific. For a normal distribution, for instance, the standard normal deviate that corresponds to the 99% confidence level is *α* = 2*.*33. Therefore, the 99% VAR can be obtained by multiplying *σ* by 2.33.

The entire distribution, however, is of interest. We should examine whether the distribution is symmetric or skewed. Skewness to the left implies a greater probability of large losses than gains. Another question is, what is the expected loss when VAR is exceeded? This is known as the *conditional VAR* (*CVAR*). This must be greater than VAR by construction. In most cases, CVAR is only slightly greater than VAR. In other cases, however, it can be much larger. In such situations, VAR limits may not be effective, as rare losses could bankrupt the institution.

As a risk measure, CVAR has other useful properties. Ideally, risk measures should obey several properties to be "coherent", as suggested by Artzner *et al.* [1]. If a portfolio has lower returns for all states of the world, its risk must be greater (monotonicity); adding cash to the portfolio should reduce its risk by this amount (translation invariance); scaling a portfolio should simply scale its risk (homogeneity); and merging portfolios cannot increase risk (subadditivity). VAR does not obey the last property, unlike CVAR. Hence, merging two portfolios could sometime produce a higher VAR than the sum of the two separate VAR measures. When distributions are elliptical, however, VAR measures are coherent (*see* **Convex Risk Measures**).

The VAR framework can also be used to uncover progressively larger but rarer losses, by increasing the confidence level. However, the empirical distribution becomes more irregular in the extreme tails due to the scarcity of data. To some extent, this problem can be alleviated by extreme value theory (EVT), which provides a theoretically sound analytical density function for the smoothing of the tails. Even so, historical data have severe limitations in some cases.

For instance, a trader may have a position on a foreign currency that is fixed against the dollar and for which there is no history of devaluations. Because the recent history shows no volatility, a VAR measure based on this would mistakenly indicate that the position is riskless, which may not be the case. In the case of corporate credits, there is usually no history of defaults by the creditors in the portfolio. A typical solution consists of assessing default probability from a history of similar creditors, perhaps within the same credit rating group. Even so, credit ratings may be flawed, as we have seen in the case of structured products that received very high credit ratings based on a recent history of home price appreciation, but led to massive defaults as soon as home prices turned lower in 2007.

This is why VAR systems must be supplemented by stress-tests scenarios. The risk manager needs to devise scenarios derived from history, perhaps from a very long time ago, and from prospective events. Stress tests can be used to estimate the effects of these scenarios on the portfolio. Such measures of risk are nonstatistical, yet are essential to evaluate the risk profile of the portfolio.

## **Structure of Risk Measurement Systems**

The potential for losses can be attributed to two sources. On the one hand are the exposures, derived from active positions taken by the trader or portfolio manager. On the other hand are the movements in the risk factors, which are outside their control. This dichotomy is reflected in the structure of risk management systems, which is described in Figure 2.

The left-hand side describes the portfolio positions, which takes as input trades from the front office. The right-hand side describes the risk factors, which has as input datafeeds with current market prices. Positions and risk factor distributions are brought together in the risk engine, which generates a distribution of portfolio values that can be summarized, for instance, by its VAR.

Different VAR methods make different assumptions for the modeling of positions and risk factors. Because modern risk measurement involves largescale aggregation, positions are routinely simplified or mapped to the risk factors. Positions can be replaced by their linear exposures to the risk factors,

![](_page_1_Figure_10.jpeg)

**Figure 2** Structure of risk measurement systems

by the quadratic exposures, or using full repricing. The distributions of risk factors can be modeled using a normal distribution, or the historical data, or using Monte Carlo simulations (MCSs). For more details on implementation, see  $[6, 7]$ .

## **Local Versus Full Valuation**

Conceptually, risk measurement methods can be separated into local valuation and full valuation methods, as shown in Figure 3. The left branch describes local valuation methods, also known as analytical *methods*, which provide closed-form solutions to risk measures. These include linear models and nonlinear models. Linear models are based on the covariance matrix approach. This matrix can be simplified using factor models, or even a diagonal model, which is a one-factor model. Nonlinear models take into account the first and second partial derivatives. The latter are called gamma or convexity (see Bond). Next, the right branch describes full valuation methods, which include historical or MCSs.

To illustrate different approaches, consider a simple instrument, a bond whose value depends on its yield to maturity, which can be taken as the single driving risk factor. The potential for loss depends on the exposure of the bond value to the yield and on potential movements in this yield dy. The linear exposure involves modified duration  $D^*$  and dollar duration  $D^*P$ . We can write

$$(\mathrm{d}P) = (-D^*P) \times (\mathrm{d}y) \tag{1}$$

![](_page_2_Figure_6.jpeg)

Figure 3 Comparison of risk measurement methods

Hence, the worst loss in the value of the bond at a specified confidence level can be derived from the worst movements in the yield at the same confidence level:

$$(\text{Worst d}P) = (-D^*P) \times (\text{Worst dy}) \tag{2}$$

More generally, the linear model implies a direct link between the bond's VAR and that of the risk factor. Because VAR is reported as a positive number, we take absolute values and have

$$VAR(dP) = |D^*P| \times VAR(dy)$$
(3)

As an example, take a position in a bond worth \$100 million. We wish to assess VAR over a horizon of one month at the 99% confidence level. Modified duration  $D^*$  is four years. From the distribution of yield changes, we observe that the worst increase in yields at the same confidence level and over the same horizon is 0.9%. Putting all of this together, the bond's VAR is  $(4 \times \$100) \times 0.9\% = \$3.6 \text{ million.}$ Note that we priced the bond only once, at the initial yield, which is why this is called a *local valuation* method.

This VAR measure is an approximation only because the bond price is not a simple linear function of the yield. For more precision, we could revalue the bond at the worst yield. Defining  $y_0$  as the initial yield, this gives

$$(\text{Worst d}P) = P[y_0 + (\text{Worst dy})] - P[y_0] \quad (4)$$

We call this approach full valuation because it requires repricing the asset at the new yield. This is more precise but, unfortunately, is more complex than a simple, linear valuation method, especially if the instrument requires valuation through lengthy simulations. More generally, this method requires full revaluation over the entire risk space, which involves a very large number of data points.

Ideally, we would like to keep the simplicity of the local valuation method while accounting for nonlinearities in the payoffs patterns. We can expand the price-yield function using a Taylor approximation:

$$dP \approx \frac{\partial P}{\partial y} dy + \left(\frac{1}{2}\right) \frac{\partial^2 P}{\partial y^2} (dy)^2$$
  
=  $(-D^*P) dy + \left(\frac{1}{2}\right) CP (dy)^2$  (5)

where the second-order term involves a coefficient called *convexity*  $C$ . Here, the valuation is still local because we only value the bond once, at the original point. The first and second derivatives are also evaluated at the local point.

Because the price is a monotonic function of the underlying yield, we can use the Taylor expansion to find the worst down move in the bond price from the worst move in the yield. This leads to a simple adjustment for VAR:

$$\text{VAR}(\text{d}P) = |D^*P| \times \text{VAR}(\text{d}y)$$
$$- \left(\frac{1}{2}\right) (CP) \text{VAR}(\text{d}y)^2 \qquad (6)$$

More generally, this method can be applied to derivatives, whose value depends on the underlying asset as a function  $f(S)$ . The Taylor approximation is

$$df \approx \frac{\partial f}{\partial S} dS + \left(\frac{1}{2}\right) \frac{\partial^2 f}{\partial S^2} dS^2 = \Delta \ dS + \left(\frac{1}{2}\right) \Gamma \ dS^2 \tag{7}$$

where delta,  $\Delta$ , is the first derivative and gamma,  $\Gamma$ , is now the second derivative, like convexity.

For a long call option position, for example, the worst value is achieved when the underlying price moves down by VAR(dS). With  $\Delta > 0$  and  $\Gamma > 0$ , the VAR for the derivative is now

$$\text{VAR}(\text{d}f) = |\Delta| \times \text{VAR}(\text{d}S) - \left(\frac{1}{2}\right)\Gamma \times \text{VAR}(\text{d}S)^2$$
(8)

This method is called *delta-gamma* because it provides an analytical, second-order correction to the delta-normal VAR. This explains why long positions in options, with positive gamma, have lower risk than with a linear model. This type of analysis can be used to understand how the option characteristics affect its VAR. Unfortunately, this analysis is most useful when there is one only risk factor. With multiple risk factors, the second-order corrections become unwieldy. As a result, this analysis is not applicable to large portfolios.

# Mapping

Whichever VAR method is used, the first step consists of mapping. Mapping is the process by which the current values of the portfolio positions are replaced by

global exposures on the risk factors. Mapping arises because of the fundamental nature of VAR, which is portfolio measurement at the highest level. As a result, this is usually a very large-scale aggregation problem. It would be too complex and time consuming to model all positions individually as risk factors. Furthermore, this is unnecessary because many positions are driven by the same set of risk factors. Once a portfolio has been mapped on the risk factors, any of the three VAR methods can be used to build the distribution of profits and losses.

Typical portfolios consist of a large number of instruments, say  $M$ . The risk manager must then decide on a small number of risk factors that effectively spans the risk space for the portfolio strategy. Define the number of risk factors as  $N$ . In the first step, each position is decomposed into a list of  $N$  exposures. In the second step, the exposures are aggregated across instruments. This yields global exposures  $x_i$  on each of the risk factors. The final step then consists of combining the exposures with the distribution of the risk factors using one of the three VAR methods.

Consider, for example, a portfolio consisting of many government bonds. The value of each bond represents the sum of the present values of cash flows at different point in times. So, in theory, we could have a number of risk factors that represent the number of days until the longest maturity, typically 30 years. This would involve too many factors. Instead, we could reduce the number of risk factors to three maturities only, for example. Figure 4 illustrates the mapping process with six bonds, which are replaced by three sets of exposures. These are summed across the portfolio, which is then prepared for the next step.

The choice of the number of risk factors must be done taking into account the trading strategies. For example, most fixed-income mutual funds follow a simple, long-only strategy, in which case one factor may be sufficient. The exposure to this factor is then the dollar duration. The portfolio can then be described by its total duration. This choice, however, still leaves out exposures to changes in the shape of the yield curve and would be totally inappropriate for a leveraged trading portfolio that can take long and short positions. If this portfolio is duration-neutral, the risk model would erroneously indicate that there is no risk. More factors are needed for this second type of portfolio. A third type of portfolio could also Instruments

![](_page_4_Figure_2.jpeg)

Figure 4 Mapping process

contain options, in that case additional factors such as implied volatilities are needed. In general, more complex strategies require more risk factors. Next, we turn to the different VAR methods.

### **Delta-normal Method**

The delta-normal method is the simplest VAR approach. This method, which is sometimes called *variance-covariance method*, assumes that the portfolio exposures are linear in the risk factors and that the risk factors are jointly normally distributed. As such, it is a local valuation method. The joint normal assumption is very useful, because a linear combination of normal variables is itself normally distributed. As a result, VAR can be expressed in analytical form, directly from the portfolio variance:

$$\sigma^2(\mathcal{R}_{p,t+1}) = x'_t \Sigma_{t+1} x_t \tag{9}$$

where  $\Sigma_{t+1}$  is the forecast of the covariance matrix over the horizon,  $x_t$  represents the dollar exposures on the risk factors, obtained via mapping and current as of t, and  $\sigma^2$  is the forecast variance of the portfolio dollar return  $R_{p,t+1}$ . If needed, the covariance matrix can be simplified to factor models. VAR is directly obtained from the dollar volatility and the standard normal deviate  $\alpha$  that corresponds to the confidence level  $c$ :

$$\text{VAR}^{\text{DN}} = \alpha \ \sigma(R_{p,t+1}) \tag{10}$$

More generally, this method can be adapted to portfolio distributions that differ from the normal, by changing  $\alpha$ . VAR can change over time as a result of changes in the positions  $x_t$  or in the forecast of the covariance matrix  $\Sigma_{t+1}$ . In the RiskMetrics approach developed by Morgan [8], variances and covariances are forecast using an exponentially weighted moving average (EWMA) model. This is a particular case of the class of generalized autoregressive conditional heteroskedasticity (GARCH) model developed by Engle [3]. Such models are widely employed for predicting time variation in risk because they are parsimonious and fit the data rather well.

Figure 5 shows an application to daily volatility forecasts of the S&P 500 stock index. The graph shows wide swings in the volatility over the short term. In addition, we observe longer term cycles, with elevated volatility from 1999 to 2002, followed by a much quieter period until 2007.

The EWMA model generates forecasts of the covariance between two risk factors  $i$  and  $j$  as follows. As of today, we observe the previous forecast  $\sigma_{i,i,t}$  and innovations in the two risk factors  $R_i$  and  $R_i$ , taken as deviation from their respective means. The forecast for tomorrow is then constructed as

$$\sigma_{ij, t+1} = \lambda \ \sigma_{ij, t} + (1 - \lambda)(R_{i, t} \times R_{j, t}) \tag{11}$$

This also applies to forecasts of the variance, in that case the two risk factors are the same. This model builds the covariance forecast in recursive form, which not only ensures some persistence in the forecast but also accounts for recent shocks. The relative weight is given by the decay factor  $\lambda$ , which is between 0 and 1. RiskMetrics selected  $\lambda = 0.94$  for daily data and  $\lambda = 0.97$  for monthly data. Although in theory, this choice could differ across the series, in practice using a common decay factor creates better properties for the covariance matrix.

The model can be also expressed in terms of all previous innovations. Taking the simple case of the variance, this gives

$$\sigma_{t+1}^2 = (1 - \lambda)(R_t^2 + \lambda R_{t-1}^2 + \lambda^2 R_{t-2}^2 + \cdots) \quad (12)$$

which shows that the variance forecast is a weighted average of previous squared innovations, with exponentially declining weights on older observations. With  $\lambda = 0.94$ , the weight on the latest observation is 6%. The weight on the previous observation is  $0.94 \times 6\%$ , and so on. More than half of the weights is placed on the last 12 observations.

![](_page_5_Figure_1.jpeg)

Figure 5 Forecast of daily volatility for S&P 500 Index using EWMA model

In summary, the main benefit of the delta-normal approach is its appealing simplicity. It provides a closed-form solution that is quick to compute. This analytical solution also lends itself well to a decomposition of VAR into its main risk drivers. This provides useful economic intuition.

This method, however, has drawbacks. It cannot account for nonlinear effects. Therefore, some of the risk will be missed for options or for instruments with imbedded options, such as mortgages. In addition, this method may also underestimate the occurrence of large losses because of its reliance on a normal distribution. In practice, most financial series have heavier tails than the normal distribution.

#### **Historical Simulation Method**

The historical simulation (HS) method applies current exposures to a time series of recent historical changes in the risk factors, for example, over the last 250 days. Define the current time as  $t$ ; we observe data from 1 to t. The current portfolio value is  $P_t$ , which is a function of the current N risk factors  $f_{i,t}$ :

$$P_t = P[f_{1,t}, f_{2,t}, \dots, f_{N,t}] \tag{13}$$

We sample the factor movements from the historical distribution, without replacement. The factor movements are drawn jointly for each day, which preserves the historical pattern of correlations. Call

 $\Delta f_i^k$  the hypothetical movement in risk factor *i* for the simulation numbered  $k$ . These are drawn from the historical distribution:

$$\Delta f_i^k \sim \{\Delta f_{i,1}, \Delta f_{i,2}, \dots, \Delta f_{i,t}\}\tag{14}$$

From this, we can construct hypothetical factor values, starting from the current one,  $f_i^k = f_{i,t} +$  $\Delta f_i^k$ . This new set of risk factor values can be used to construct a hypothetical value of the current portfolio under the new scenario,  $P^k = P[f_1^k, f_2^k, \ldots, f_N^k]$ using full valuation.

We can now compute changes in portfolio values from the current position  $R_p^k = (P^k - P_t)$ , sort these returns, and pick the one that corresponds to the  $c$ th quantile,  $R_n(c)$ . The HS VAR is obtained from the difference between the average and the quantile,

$$VARHS = AVE[Rp] - Rp(c)$$
(15)

Often, the mean is ignored. The advantage of this method is that it is easy to explain. The method is intuitive because each return is associated to an actual realization of risk factors, which gives insight into what could go wrong. The method also appears "distribution-free", because it makes no specific distributional assumption, other than assuming that the recent past is relevant. This is an improvement over the normal distribution because historical data typically contain fat tails. In addition, because the portfolio can be priced under full revaluation, this approach

can handle options and other nonlinear instruments. This explains why this is perhaps the most popular VAR method. It is also interesting to note that this apparatus can easily handle stress tests, where scenarios are prespecified by the risk manager instead of drawn from the recent history.

Historical simulation has drawbacks, however, as discussed by Finger [4]. It usually relies on a short historical moving window, such as one year, to infer movements in market prices. This may be too short to provide adequate representation of the risk space.

In addition, this method does not adequately track time variation in risk. Figure 5 indeed reveals long-term cycles in volatility. With a long window, the method is very slow to pick up changes in the risk environment. An alternative method, called *filtered simulation*, is proposed by Hull and White [5]. This consists of first fitting a time-series volatility model, such as the EWMA to each risk factor. This produces a series of returns scaled by their volatility forecast *σt*

$$\varepsilon_t = R_t / \sigma_t \tag{16}$$

Historical simulation is then applied to the sequence of scaled returns *εt* , which are then multiplied by the latest volatility forecast for the next day *σt*+1. The advantage of this approach is that is does not assume that the scaled returns follow a normal distribution. This method combines any fat tails in the data with the more recent volatility forecast, which should lead to more precise estimates of the risk forecasts. The disadvantage of these more reactive methods, however, is that they create a more volatile capital charge unless there is some smoothing of the daily VAR measures.

## **Monte Carlo Simulation Method**

The MCS method is similar to historical simulation, except that the movements in risk factors are generated by drawings from some prespecified distribution:

$$\Delta f^k \sim g(\theta) \tag{17}$$

where *g* is the joint distribution (e.g., normal, Student's *t*, or other) with parameters *θ*. The risk manager samples pseudorandom values for the risk factors from this distribution. As in the case of historical simulation, these are used to price the portfolio for different scenarios. The returns are then sorted to produce the desired VAR.

This method is the most flexible, because it allows full revaluation as well as complex distributions for the risk factors. One the other hand, it is computationally more onerous. Monte Carlo methods also create inherent sampling variability because of the randomization process. Different sequences of random numbers will lead to different results. It may take a large number of iterations to converge to a stable VAR measure. Finally, the Monte Carlo method requires users to make detailed assumptions about the form and parameters of the stochastic process. The process makes the output less amenable to economic interpretation than other methods. Therefore, it is subject to model risk. Risk managers need to understand how sensitive the results are to the model assumptions.

## **Backtesting**

Whichever method is used, it is essential to compare the risk forecasts with the actual distribution of revenues. This provides a reality check on the accuracy of models. Backtesting involves systematically comparing historical VAR measures with the subsequent daily returns. Each exceedance is called an *exception*. Assume, for example, that VAR is measured at the 99% level of confidence. If the model is well specified, we should observe on average 2.5 exceptions over the course of a year. This is because 100–99%, or 0*.*01 × 250 trading days gives 2.5. In practice, some deviation around this number is to be expected. If there are too many exceptions, however, the risk manager will have to conclude that the model is flawed. Such backtesting provides valuable feedback to users about the accuracy of the VAR system. The procedure can also be used to search for possible improvements in the models.

One final drawback of risk measurement models should be mentioned. All models assume that the current positions are frozen over the horizon. In practice, trading will occur, which can change the trading risk profile. More exceptions can occur if intraday risk is greater than at the close of the trading day. This is why exception tests should also be performed on a hypothetical return series. This represents a frozen portfolio, obtained from fixed positions applied to the actual returns on all securities, measured from close to close. This also abstracts from fee income or interest payments that are included in actual revenues. A bank experiencing too many exceptions using both actual and hypothetical returns should conclude that its risk model is fundamentally flawed.

## **Conclusions**

Quantitative approaches to measuring market risk have become widespread. Risk is now increasingly measured at the top level of the institution, which involves the large-scale aggregation of data across many instruments and types of financial risks.

In spite of its quantitative aspects, risk management is still largely an art form, however. The design of risk architecture involves many tradeoffs. The goal of risk systems should be to produce reasonably accurate estimates of risk at a reasonable cost and within a reasonable time frame. Most importantly, the risk manager needs to be keenly aware of limitations in quantitative risk measures.

## **References**

[1] Artzner, P., Delbaen, F., Eber, J.M. & Heath, D. (1999). Coherent measures of risk, *Mathematical Finance* **9**, 203–228.

- [2] Basel Committee on Banking Supervision. (1996). *Amendment to the Basel Capital Accord to Incorporate Market Risk*, BIS, Basel.
- [3] Engle, R. (1982). Autoregressive conditional heteroskedasticity with estimates of the variance of United Kingdom inflation, *Econometrica* **50**, 987–1007.
- [4] Finger, C. (2006). *How Historical Simulation Made Me Lazy*, Working Paper, RiskMetrics Group, New York.
- [5] Hull, J. & White, A. (1998). Incorporating volatility updating into the historical simulation method for valueat-risk, *Journal of Risk* **1**, 5–19.
- [6] Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk*, McGraw-Hill, New York.
- [7] Jorion, P. (2007). *Financial Risk Manager Handbook*, Wiley, New York.
- [8] Morgan, J.P. (1995). *RiskMetrics Technical Manual*, J.P. Morgan, New York.

## **Related Articles**

**Backtesting**; **Bond**; **Convex Risk Measures**; **Expected Shortfall**; **Rare-event Simulation**; **Risk Exposures**; **Risk Management: Historical Perspectives**; **Risk Measures: Statistical Estimation**; **Stress Testing**; **Value-at-Risk**.

PHILIPPE JORION
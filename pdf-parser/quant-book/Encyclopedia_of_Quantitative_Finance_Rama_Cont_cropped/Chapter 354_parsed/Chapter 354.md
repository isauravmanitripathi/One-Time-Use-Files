# **Mixed Data Sampling**

Regression models that involve data sampled at different frequencies, or the so-called MIxed DAta Sampling (MIDAS) regression models, were introduced in both filtering and regression context in a number of recent papers, including [15, 17, 19], among others. These regressions deal with a situation often encountered in practice. For example, macroeconomic data are typically sampled at monthly or quarterly frequencies, whereas financial time series are sampled at almost any arbitrarily high frequency. Although most economic time series are not sampled at the same frequency, the typical practice of estimating econometric models involves aggregating all variables to the same (low) frequency using an equal weighting scheme.

Temporal aggregation in regression models, in contrast, is a well-studied area. The problem of temporal aggregation concerning dynamic models has been considered in the work of many authors, for example, [5, 11, 14, 21, 24, 26, 30–33, 36, 39–41].

In the first section, we draw comparisons between temporal aggregation and MIDAS. In the second section, we focus on a specific topic of special interest in finance-volatility forecasting.

#### **Temporal Aggregation and MIDAS**

MIDAS regressions not only share some features with distributed lag models but also have unique novel features. A stylized distributed lag model is a regression model of the following type:  $y_t = \beta_0 + B(L)x_t + B(L)x_t$  $\varepsilon_t$ , where  $B(L)$  is some finite or infinite lag polynomial operator, usually parameterized by a small set of hyperparameters (see, e.g., [8] for a survey on distributed lag models). In a standard MIDAS regression model, the regressor is sampled  $m$  times more frequently than the regressand, where the latter has a sample of  $T$  observations. The asymptotics are based on  $T$  for a given  $m$ . Therefore, one studies the asymptotic properties of the estimators assuming that the span of the data set  $T$  grows and the high-frequency sample size of the regressors would be  $mT$  such that when  $T \rightarrow \infty$  then both the low- and high-frequency samples tend to become large.

Andreou et al. [2] decompose the MIDAS regression model into two terms: the equal or flat aggregated term and a MIDAS term, which involves weighted higher order differences of the highfrequency process. This decomposition allows one to link the MIDAS regression model with the traditional temporal aggregation literature, which omits the MIDAS term.

Consider the mixed data sampling data  $\{y_t, \mathbf{x}_{t/m}^{(m)}\}$ where  $\mathbf{x}_{t/m}^{(m)} = (1, x_{2,t/m}^{(m)}, \dots, x_{p,t/m}^{(m)})$  is a *p*-dimensional vector of higher frequency data observed at most m time between t and  $t-1$ . The data are assumed to be weakly dependent. The conventional approach in empirical macroeconomics and finance employs the linear regression based on aggregated data, which are typically obtained by a pre-estimation procedure that computes simple averages to bring the high-frequency data to a common (low) frequency. In other words, the conventional approach employs the linear regression subject to the temporal aggregation restriction of an equal weighting scheme. Define the variable  $\mathbf{x}_{t}^{A} = \frac{1}{m} \sum_{j=1}^{m} L^{j/m} \mathbf{x}_{t/m}^{(m)}$  that temporally aggregates the covariates  $\mathbf{x}_{t/m}^{(m)}$  using equal weights (simple average), where  $q$  is the number of highfrequency lags used in the temporal aggregation of  $\mathbf{x}_{t/m}^{(m)}$  with  $L^{j/m}$  being the high-frequency lag operator. Then the conventional approach estimates by Least squares (LS) the following linear regression model:

$$y_t = \mathbf{x}_t^{A'} \boldsymbol{\beta}^* + u_t^*, \quad q = 2, 3, \dots$$
 (1)

where  $E(u_t^*|\mathbf{x}_t^A) = 0$  and  $E(u_t^{*2}|\mathbf{x}_t^A) = \sigma^{*2}$ .

Consider now a projection of the high-frequency data onto  $y$  and let the linear polynomial of the projection be  $\mathbf{W}(L^{1/m};\boldsymbol{\theta})$ , which is parameterized by a low-dimensional  $r \times 1$  vector of parameters  $\theta$ . Then we can define a MIDAS regression model as

$$y_t = \boldsymbol{\beta}' \mathbf{x}_t(\boldsymbol{\theta}) + u_t, \quad t = 1, 2, \dots, T \qquad (2)$$

where  $E(u_t|\mathbf{x}_{t/m}^{(m)}) = 0$  and  $E(u_t^2|\mathbf{x}_{t/m}^{(m)}) = \sigma^2$  where<br>  $\mathbf{x}_t(\boldsymbol{\theta}) = \left(1, x_{2,t}^{(m_2)}(\theta_2), \dots, x_{p,t}^{(m_p)}(\theta_p)\right)'$  is a nonlinear function that maps the higher frequency data into a common low frequency and

$$x_{k,t}^{(m)}(\theta_k) = W(L^{1/m}; \theta_k) x_{k,t/h}^{(m)}$$
$$= \sum_{j=1}^q w_{j,k}(\theta_k) L^{j/m} x_{k,t/m}^{(m)},$$
$$k = 2, \dots, p \tag{3}$$

where  $w_{j,k}(\theta_k) \in (0, 1)$  and  $\sum_{j=1}^{m} w_{j,k}(\theta_k) = 1$ . The latter assumption allows the identification of the slope coefficient vector *β.* Equation (2) is a nonlinear regression that allows both the weighting scheme of the temporal aggregation as parameterized by the vector *θ* and the slope coefficient vector *β* to be estimated from the data. Following Ghysels *et al.* [17] the lag coefficients, *wj,k(θk ),* which determine the weighting scheme used, are parsimoniously parameterized *via* exponential Almon, Almon, Beta, or step function schemes.

Andreou *et al.* [2] study regression models that involve data sampled at different frequencies and compare them with a traditional model that involves temporal aggregation for the estimation of a model at the same sampling frequency that implies an equal weighting scheme. They derive the asymptotic properties of the MIDAS nonlinear least squares (MIDAS-NLS) estimators of regression models with mixed frequencies and general weighting schemes and show that the LS estimator is always relatively less efficient than the MIDAS-NLS estimator. Our analysis reveals the effects of the aggregation horizon on the properties of the MIDAS-NLS and temporally aggregated or FLAT-LS estimators. In particular, they show that the FLAT-LS estimator is asymptotically biased and inefficient when the high-frequency regressor exhibits linear temporal dependence as in the case of AR(1), while it is only inefficient in the case of *i.i.d*. and ARCH(1) high-frequency processes. Furthermore, they propose two types of aggregation bias tests: a simple LM test and a Wu–Hausmantype test that uses the high-frequency variables as instruments.

To conclude, it is worth discussing one particular application of regression models, namely, testing for Granger causality among variables–a topic of interest in many financial applications. Much has been written about the spurious effects temporal aggregation may have on testing for Granger causality; see, for example [4, 20, 22, 23, 27, 28, 34], among others. Ghysels and Valkanov [18] show that there are unexplored advantages in testing Granger causality in combining the data sampled at the different frequencies. They develop a set of Granger causality tests that explicitly take advantage of data sampled at different frequencies. Along similar lines, Andreou *et al.* (2009) document many predictable patterns between daily financial data and monthly and quarterly macroeconomic variables. Such patterns significantly improve macroeconomic forecasts. Recent work on this topic includes improving quarterly macroforecasts with monthly data using MIDAS regressions [3, 7, 13, 35, 38] or improving quarterly and monthly macroeconomic predictions with daily financial data [2]; Ghysels and Wright (2008); [25, 37].

## **Volatility Forecasting with MIDAS**

The original work on MIDAS focused on volatility predictions [1, 6, 10, 12, 15, 16], among others. The abundance of high-frequency data, combined with the desire to predict volatility over longer horizons, provides an ideal setting for applying such regressions. The original work on MIDAS was in fact a filtering and not a regression setting. Ghysels *et al.* [15] studied the risk-return trade-off—where returns were computed over longer horizons, whereas risk was measured by conditional variance over the same horizon but measured with a filter of weighted daily returns. In [16], the same approach was adopted in a regression format to predict multihorizon volatility. Chen and Ghysels [6] take this a step further and use a semiparametric MIDAS regression that related news impact curves applied to intradaily data to future realized volatility. They find that returns have significant asymmetric effects on future volatility–a topic somehow lost in the recent realized volatility literature—as originally emphasized in the context of ARCH-type models by Engle and Ng (1993). As mentioned in the previous section, this work distinguishes itself from the more standard temporal aggregation literature in the context of volatility [9, 29].

## **References**

- [1] Alper, C., Fendoglu, S. & Saltoglu, B. (2008). *Forecasting Stock Market Volatilities Using MIDAS Regressions: An Application to the Emerging Markets*. MPRA Paper No. 7460.
- [2] Andreou, E., Ghysels, E. & Kourtellos, A. (2008). *Should Macroeconomic Forecasters look at Daily Financial Data?* Tech. rep., Discussion Paper, UNC and University of Cyprus.
- [3] Andreou, E., Ghysels, E. & Kourtellos, A. (2009). Regression models with mixed sampling frequencies, *Journal of Econometrics* (forthcoming).
- [4] Armesto, M., Hernandez-Murillo, R., Owyang, M. & Piger, J. (2008). Measuring the information content of the beige book: a mixed data sampling approach, *Journal of Money, Credit and Banking* forthcoming.

- [5] Breitung, J. and Swanson, N. (2002). Temporal aggregation and spurious instantaneous causality in multiple time series models, *Journal of Time Series Analysis* **23**, 651–665.
- [6] Brewer, K. (1973). Some consequences of temporal aggregation and systematic sampling for ARMA and ARMAX models, *Journal of Econometrics* **1**, 133–154.
- [7] Chen, X. & Ghysels, E. (2008). *News-Good or Badand its Impact on Volatility Predictions Over Multiple Horizons*. Discussion Paper, UNC.
- [8] Clements, M. & Galvao, A. (2008). Macroeconomic ˜ forecasting with mixed frequency data: forecasting US output growth, *Journal of Business and Economic Statistics* **26**, 546–554.
- [9] Dhrymes, P. (1971). *Distributed Lags: Problems of Estimation and Formulation*, Holden-Day, San Francisco.
- [10] Drost, F. & Nijman, T. (1993). Temporal aggregation of GARCH processes, *Econometrica* **61**, 909–927.
- [11] Engle, R., Ghysels, E. & Sohn, B. (2008). *On the Economic Sources of Stock Market Volatility*. Discussion Paper, NYU and UNC.
- [12] Engle, R.F. & Ng, V.K. (1993). Measuring and testing the impact of news on volatility, *Journal of Finance* **48**(5), 1749–1778.
- [13] Engle, R. & Liu, T. (1972). Effects of aggregation over time on dynamic characteristics of an econometric model, in *Econometric Models of Cyclical Behaviors*, B. G. Hickman ed, National Bureau of Economic Research, Inc, Columbia, UP, Vol. 2.
- [14] Forsberg, L. & Ghysels, E. (2006). Why do absolute returns predict volatility so well? *Journal of Financial Econometrics* **6**, 31–67.
- [15] Galvao, A. (2006). ˜ *Changes in Predictive Ability with Mixed Frequency Data*. Discussion Paper, Queen Mary University.
- [16] Geweke, J. (1978). Temporal aggregation in the multiple regression model, *Econometrica* **46**, 643–661.
- [17] Ghysels, E., Santa-Clara, P. & Valkanov, R. (2005). There is a risk-return tradeoff after all, *Journal of Financial Economics* **76**, 509–548.
- [18] Ghysels, E., Santa-Clara, P. & Valkanov, R. (2006a). Predicting volatility: getting the most out of return data sampled at different frequencies, *Journal of Econometrics* **131**, 59–95.
- [19] Ghysels, E., Sinko, A. & Valkanov, R. (2006b). MIDAS regressions: further results and new directions, *Econometric Reviews* **26**, 53–90.
- [20] Ghysels, E. & Wright, J. (2007). Forecasting professional forecasters, *Journal of Business and Economic Statistics* forthcoming.
- [21] Ghysels, E. & Valkanov, R. (2008). *Granger Causality Tests with Mixed Data Frequencies*. Working paper, UNC and UCSD.
- [22] Ghysels, E. & Wright, J. (2009). Forecasting professional forecasters, *Journal of Business and Economic Statistics* (forthcoming).

- [23] Granger, C. (1980). Testing for causality: a personal viewpoint, *Journal of Economic Dynamics and Control* **2**, 329–352.
- [24] Granger, C. (1987). Implications of aggregation with common factors, *Econometric Theory* **3**, 208–222.
- [25] Granger, C. (1988). Some recent developments in a concept of causality, *Journal of Econometrics,* **39**, 199–211.
- [26] Granger, C. (1995). Causality in the long run, *Econometric Theory* **11**, 530–536.
- [27] Griliches, Z. (1967). Distributed lags: a survey, *Econometrica* **35**, 16–49.
- [28] Hamilton, J. (2006). *Daily Monetary Policy Shocks and the Delayed Response of New Home Sales*. Working paper, UCSD.
- [29] Hsiao, C. (1979). Linear regression using both temporally aggregated and temporally disaggregated data, *Journal of Econometrics* **10**(2), 243–252.
- [30] Lutkepohl, H. (1993). Testing for causation between ¨ two variables in higher dimensional VAR models, in *Studies in Applied Econometrics*, H. Schneeweiss & K. Zimmerman, eds, Springer-Verlag, Heidelberg, p. 75.
- [31] McCrorie, J. & Chambers, M. (2006). Granger causality and the sampling of economic processes, *Journal of Econometrics* **132**, 311–336.
- [32] Meddahi, N. & Renault, E. (2004). Temporal aggregation of volatility models, *Journal of Econometrics* **119**, 355–379.
- [33] Mundlak, Y. (1961). Aggregation over time in distributed lag models, *International Economic Review* **2**, 154–163.
- [34] Phillips, P. (1972). The structural estimation of a stochastic differential equation system, *Econometrica* **40**, 1021–1041.
- [35] Phillips, P. (1973). The problem of identification in finite parameter continuous time models, *Journal of Econometrics* **1**, 351–362.
- [36] Phillips, P. (1974). The estimation of some continuous time models, *Econometrica* **42**, 803–824.
- [37] Renault, E., Sekkat, K. & Szafarz, A. (1998). Testing for spurious causality in exchange rates, *Journal of Empirical Finance* **5**, 47–66.
- [38] Schumacher, C. & Breitung, J. (2008). Real-time forecasting of German GDP based on a large factor model with monthly and quarterly data, *International Journal of Forecasting,* **24**, 386–398.
- [39] Sims, C. A. (1971). Discrete approximations to continuous time distributed lags in econometrics, *Econometrica* **39**, 545–563.
- [40] Tay, A. (2006). *Financial Variables as Predictors of Real Output Growth*. Discussion Paper, SMU.
- [41] Tay, A. (2007). *Mixing Frequencies: Stock Returns as a Predictor of Real Output Growth*. Discussion Paper, SMU.
- [42] Theil, H. (1954). *Linear Aggregation of Economic Relationships*, North Holland.

- [43] Tiao, G.C. & Wei W.S., (1976). Effect of temporal aggregation on the dynamic relationship of two time series variables, *Biometrika* **63**, 513–523.
- [44] Zellner, A. & Montmarquette, C. (1971). A study of some aspects of temporal aggregation problems in econometric analysis, *Review of Economic Statistics* **53**, 335–342.

## **Further Reading**

- Anderson, E., Ghysels, E. & Juergens, J. (2009). The impact of risk and uncertainty on expected returns, *Journal of Financial Economics* (forthcoming).
- Chen, X., Ghysels, E. & Wang, F. (2009). *The HYBRID GARCH Model, Discussion Paper UNC*.

- Colacito, R., Engle, R. & Ghysels, E. (2008). *A Component Model of Dynamic Correlations, Discussion Paper UNC*.
- Ghysels, E., Santa-Clara, P. & Valkanov, R. (2003). *The MIDAS Touch: Mixed Data Sampling Regression Models*, Working paper, UNC and UCLA.
- Ghysels, E. Rubia, A & Valkanov, R. (2009). Multi-Period Forecasts of Volatility: Direct, Iterated, and Mixed-Data Approaches, *Discussion Paper UNC*.
- Ghysels, E. & Sinko, A. (2009). Volatility forecasting and microstructure noise, *Journal of Econometrics* (forthcoming).

ERIC GHYSELS
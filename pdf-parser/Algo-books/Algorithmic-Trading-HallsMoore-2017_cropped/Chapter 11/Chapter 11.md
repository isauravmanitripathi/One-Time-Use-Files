# Chapter 11

# Autoregressive Integrated Moving Average and Conditional Heteroskedastic Models

In the previous chapter we went into significant detail about the AR(p), MA(q) and ARMA(p,q) linear time series models. We used these models to generate simulated data sets, fitted models to recover parameters and then applied these models to financial equities data.

In this chapter we are going to discuss an extension of the ARMA model, namely the Autoregressive Integrated Moving Average model, or ARIMA(p,d,q) model as well as models that incorporate conditional heteroskedasticity, such as ARCH and GARCH.

We will see that it is necessary to consider the ARIMA model when we have non-stationary series. Such series occur in the presence of stochastic trends.

# 11.1 Quick Recap

We have steadily built up our understanding of time series with concepts such as serial correlation, stationarity, linearity, residuals, correlograms, simulation, model fitting, seasonality, conditional heteroscedasticity and hypothesis testing.

As of yet we have not carried out any prediction or forecasting from our models and so have not had any mechanism for producing a trading system or equity curve.

Once we have studied ARIMA we will be in a position to build a basic long-term trading strategy based on prediction of stock market index returns.

Despite the fact that I have gone into a lot of detail about models which we know will ultimately not have great performance (AR, MA, ARMA), we are now well-versed in the process of time series modeling.

This means that when we come to study more recent models (including those currently in the research literature) we will have a significant knowledge base on which to draw. This will allow effective evaluation of these models rather than treating them as a "turn key" prescription or "black box".

More importantly it will provide us with the confidence to extend and modify them on our own and understand what we are doing when we do it.

I would like to thank you for being patient so far as it might seem that these chapters on time series analysis theory are far away from the "real action" of actual trading. However true quantitative trading research is careful, measured and takes significant time to get right. There is no quick fix or "get rich scheme" in quant trading.

We are very nearly ready to consider our first trading model, which will be a mixture of ARIMA and GARCH. Hence it is imperative that we spend some time understanding the ARIMA model well.

Once we have built our first trading model we are going to consider more advanced models in subsequent chapters including state-space models (which we will solve with the Kalman Filter) and Hidden Markov Models, which will lead us to more sophisticated trading strategies.

# 11.2 Autoregressive Integrated Moving Average (ARIMA) Models of order p, d, q

#### 11.2.1 Rationale

ARIMA models are used because they can reduce a non-stationary series to a stationary series using a sequence of differencing steps.

We can recall from the previous chapter on white noise and random walks that if we apply the difference operator to a random walk series {xt} (a non-stationary series) we are left with white noise {wt} (a stationary series):

$$\nabla x_t = x_t - x_{t-1} = w_t \tag{11.1}$$

ARIMA essentially performs this function but does so repeatedly d times in order to reduce a non-stationary series to a stationary one. In order to handle other forms of non-stationarity beyond stochastic trends additional models can be used.

Seasonality effects such as those that occur in commodity prices can be tackled with the Seasonal ARIMA model (SARIMA). Unfortunately we will not be discussing SARIMA in this book. Conditional heteroskedastic effects such as volatility clustering in equities indexes can be tackled with ARCH and GARCH, which we will discuss later in this chapter.

We will first consider non-stationary series with stochastic trends and fit ARIMA models to these series. We will also finally produce forecasts for our financial series.

#### 11.2.2 Definitions

Prior to defining ARIMA processes we need to discuss the concept of an integrated series:

Definition 11.2.1. Integrated Series of order d. A time series {xt} is integrated of order d, I(d), if:

$$\nabla^d x_t = w_t \tag{11.2}$$

That is, if we difference the series d times we receive a discrete white noise series.

Alternatively it is possible to use the Backward Shift Operator B to provide an equivalent condition:

$$(1 - \mathbf{B}^d)x_t = w_t \tag{11.3}$$

Now that we have defined an integrated series we can define the ARIMA process itself:

Definition 11.2.2. Autoregressive Integrated Moving Average Model of order p, d, q. A time series {xt} is an autoregressive integrated moving average model of order p, d, q, ARIMA(p,d,q), if ∇<sup>d</sup>x<sup>t</sup> is an autoregressive moving average model of order p,q, ARMA(p,q).

That is, if the series {xt} is differenced d times, and it then follows an ARMA(p,q) process, then it is an ARIMA(p,d,q) series.

If we use the polynomial notation from the previous chapter on ARMA then an ARIMA(p,d,q) process can be written in terms of the Backward Shift Operator, B:

$$\theta_p(\mathbf{B})(1-\mathbf{B})^d x_t = \phi_q(\mathbf{B}) w_t \tag{11.4}$$

Where w<sup>t</sup> is a discrete white noise series.

There are some points to note about these definitions.

Since the random walk is given by x<sup>t</sup> = xt−<sup>1</sup> + w<sup>t</sup> it can be seen that I(1) is another representation, since ∇1x<sup>t</sup> = wt.

If we suspect a non-linear trend then we might be able to use repeated differencing (i.e. d > 1) to reduce a series to stationary white noise. In R we can use the diff command with additional parameters, e.g. diff(x, d=3) to carry out repeated differences.

#### 11.2.3 Simulation, Correlogram and Model Fitting

Since we have already made use of the arima.sim command to simulate an ARMA(p,q) process, the following procedure will be similar to that carried out in the previous chapter.

The major difference is that we will now set d = 1, that is, we will produce a non-stationary time series with a stochastic trending component.

As before we will fit an ARIMA model to our simulated data, attempt to recover the parameters, create confidence intervals for these parameters, produce a correlogram of the residuals of the fitted model and finally carry out a Ljung-Box test to establish whether we have a good fit.

We are going to simulate an ARIMA(1,1,1) model, with the autoregressive coefficient α = 0.6 and the moving average coefficient β = −0.5. Here is the R code to simulate and plot such a series, see Figure 11.1.

```
> set.seed(2)
> x <- arima.sim(list(order = c(1,1,1), ar = 0.6, ma=-0.5), n = 1000)
> plot(x)
```

Now that we have our simulated series we are going to try and fit an ARIMA(1,1,1) model to it. Since we know the order we will simply specify it in the fit:

```
> x.arima <- arima(x, order=c(1, 1, 1))
```

![](_page_3_Figure_0.jpeg)

Figure 11.1: Plot of simulated ARIMA(1,1,1) model with α = 0.6 and β = −0.5

```
Call:
arima(x = x, order = c(1, 1, 1))
Coefficients:
         ar1 ma1
      0.6470 -0.5165
s.e. 0.1065 0.1189
sigma^2 estimated as 1.027: log likelihood = -1432.09, aic = 2870.18
  The confidence intervals are calculated as:
```

> 0.6470 + c(-1.96, 1.96)\*0.1065 [1] 0.43826 0.85574 > -0.5165 + c(-1.96, 1.96)\*0.1189 [1] -0.749544 -0.283456

Both parameter estimates fall within the confidence intervals and are close to the true parameter values of the simulated ARIMA series. Hence we should not be surprised to see the residuals looking like a realisation of discrete white noise as given in Figure 11.2.

```
> acf(resid(x.arima))
```

Finally, we can run a Ljung-Box test to provide statistical evidence of a good fit:

```
> Box.test(resid(x.arima), lag=20, type="Ljung-Box")
```

![](_page_4_Figure_0.jpeg)

![](_page_4_Figure_1.jpeg)

Figure 11.2: Correlogram of the residuals of the fitted ARIMA(1,1,1) model

Box-Ljung test

```
data: resid(x.arima)
X-squared = 19.0413, df = 20, p-value = 0.5191
```

We can see that the p-value is significantly larger than 0.05 and as such we can state that there is strong evidence for discrete white noise being a good fit to the residuals. Thus the ARIMA(1,1,1) model is a good fit as expected.

#### 11.2.4 Financial Data and Prediction

In this section we are going to fit ARIMA models to Amazon, Inc. (AMZN) and the S&P500 US Equity Index (^GPSC, in Yahoo Finance). We will make use of the forecast library, written by Rob J Hyndman[54].

We can go ahead and install the library in R:

```
> install.packages("forecast")
```

```
> library(forecast)
```

Now we can use quantmod to download the daily price series of Amazon from the start of 2013. Since we will have already taken the first order differences of the series, the ARIMA fit carried out shortly will not require d > 0 for the integrated component:

> require(quantmod) > getSymbols("AMZN", **from**="2013-01-01") > amzn = diff(log(Cl(AMZN)))

As in the previous chapter we are now going to loop through the combinations of p, d and q, to find the optimal ARIMA(p,d,q) model. By "optimal" we mean the order combination that minimises the Akaike Information Criterion (AIC):

```
> azfinal.aic <- Inf
> azfinal.order <- c(0,0,0)
> for (p in 1:4) for (d in 0:1) for (q in 1:4) {
> azcurrent.aic <- AIC(arima(amzn, order=c(p, d, q)))
> if (azcurrent.aic < azfinal.aic) {
> azfinal.aic <- azcurrent.aic
> azfinal.order <- c(p, d, q)
> azfinal.arima <- arima(amzn, order=azfinal.order)
> }
> }
```

We can see that an order of p = 4, d = 0, q = 4 was selected. Notably d = 0, as we have already taken first order differences above:

### > azfinal.order [1] 4 0 4

If we plot the correlogram of the residuals we can see if we have evidence for a discrete white noise series, see Figure 11.3.

```
> acf(resid(azfinal.arima), na.action=na.omit)
```

There are two significant peaks, namely at k = 15 and k = 21, although we should expect to see statistically significant peaks simply due to sampling variation 5% of the time. Let us perform a Ljung-Box test and see if we have evidence for a good fit:

```
> Box.test(resid(azfinal.arima), lag=20, type="Ljung-Box")
```

Box-Ljung test

```
data: resid(azfinal.arima)
X-squared = 12.6337, df = 20, p-value = 0.8925
```

As we can see the p-value is greater than 0.05 and so we have evidence for a good fit at the 95% level.

We can now use the forecast command from the forecast library in order to predict 25 days ahead for the returns series of Amazon, which is provided in Figure 11.4.

#### > plot(forecast(azfinal.arima, h=25))

We can see the point forecasts for the next 25 days with 95% (dark blue) and 99% (light blue) error bands. We will be using these forecasts in our first time series trading strategy when we come to combine ARIMA and GARCH later in the book.

Let us carry out the same procedure for the S&P500. Firstly we obtain the data from quantmod and convert it to a daily log returns stream:

![](_page_6_Figure_1.jpeg)

Figure 11.3: Correlogram of residuals of ARIMA(4,0,4) model fitted to AMZN daily log returns

![](_page_6_Figure_3.jpeg)

Figure 11.4: 25-day forecast of AMZN daily log returns

```
> getSymbols("^GSPC", from="2013-01-01")
> sp = diff(log(Cl(GSPC)))
```

We fit an ARIMA model by looping over the values of p, d and q:

```
> spfinal.aic <- Inf
> spfinal.order <- c(0,0,0)
> for (p in 1:4) for (d in 0:1) for (q in 1:4) {
> spcurrent.aic <- AIC(arima(sp, order=c(p, d, q)))
> if (spcurrent.aic < spfinal.aic) {
> spfinal.aic <- spcurrent.aic
> spfinal.order <- c(p, d, q)
> spfinal.arima <- arima(sp, order=spfinal.order)
> }
> }
```

The AIC tells us that the "best" model is the ARIMA(2,0,1) model. Notice once again that d = 0, as we have already taken first order differences of the series:

### > spfinal.order [1] 2 0 1

We can plot the residuals of the fitted model to see if we have evidence of discrete white noise, see Figure [11.5.](#page-7-0)

```
> acf(resid(spfinal.arima), na.action=na.omit)
```

![](_page_7_Figure_6.jpeg)

<span id="page-7-0"></span>Figure 11.5: Correlogram of residuals of ARIMA(2,0,1) model fitted to S&P500 daily log returns

The correlogram looks promising, so the next step is to run the Ljung-Box test and confirm that we have a good model fit:

> Box.test(resid(spfinal.arima), lag=20, type="Ljung-Box")

Box-Ljung test

```
data: resid(spfinal.arima)
X-squared = 13.6037, df = 20, p-value = 0.85
```

Since the p-value is greater than 0.05 we have evidence of a good model fit.

Why is it that in the previous chapter our Ljung-Box test for the S&P500 showed that the ARMA(3,3) was a poor fit for the daily log returns?

Notice that I deliberately truncated the S&P500 data to start from 2013 onwards here, which conveniently excludes the volatile periods around 2007-2008. Hence we have excluded a large portion of the S&P500 where we had excessive volatility clustering. This impacts the serial correlation of the series and hence has the effect of making the series seem "more stationary" than it has been in the past.

This is a very important point. When analysing time series we need to be extremely careful of conditionally heteroscedastic series, such as stock market indexes. In quantitative finance, trying to determine periods of differing volatility is often known as "regime detection". It is one of the harder tasks to achieve.

Let us now plot a forecast for the next 25 days of the S&P500 daily log returns as given in Figure [11.6.](#page-8-0)

> plot(forecast(spfinal.arima, h=25))

![](_page_8_Figure_9.jpeg)

<span id="page-8-0"></span>Figure 11.6: 25-day forecast of S&P500 daily log returns

Now that we have the ability to fit and forecast models such as ARIMA we are very close to

being able to create strategy indicators for trading.

#### 11.2.5 Next Steps

In the next section we are going to take a look at the Generalised Autoregressive Conditional Heteroscedasticity (GARCH) model and use it to explain more of the serial correlation in certain equities and equity index series.

Once we have discussed GARCH we will be in a position to combine it with the ARIMA model and create signal indicators and thus a basic quantitative trading strategy.

# 11.3 Volatility

The main motivation for studying conditional heteroskedasticity in finance is that of volatility of asset returns. Volatility is an incredibly important concept in finance because it is highly synonymous with risk.

Volatility has a wide range of applications in finance:

- Options Pricing The Black-Scholes model for options prices is dependent upon the volatility of the underlying instrument
- Risk Management Volatility plays a role in calculating the VaR of a portfolio, the Sharpe Ratio for a trading strategy and in determination of leverage
- Tradeable Securities Volatility can now be traded directly by the introduction of the CBOE Volatility Index (VIX), and subsequent futures contracts and ETFs

If we can effectively forecast volatility then we will be able to price options more accurately, create more sophisticated risk management tools for our algorithmic trading portfolios and even design new systematic strategies that trade volatility directly.

We are now going to turn our attention to conditional heteroskedasticity and discuss what it means.

# 11.4 Conditional Heteroskedasticity

Let us first discuss the concept of heteroskedasticity and then examine the "conditional" part.

If we have a collection of random variables, such as elements in a time series model, we say that the collection is heteroskedastic if there are certain groups, or subsets, of variables within the larger set that have a different variance from the remaining variables.

For instance, in a non-stationary time series that exhibits seasonality or trending effects, we may find that the variance of the series increases with the seasonality or the trend. This form of regular variability is known as heteroskedasticity.

However, in finance there are many reasons why an increase in variance is correlated to a further increase in variance.

For instance, consider the prevalence of downside portfolio protection insurance employed by long-only fund managers. If the equities markets were to have a particularly challenging day (i.e. a substantial drop!) it could trigger automated risk management sell orders, which would further depress the price of equities within these portfolios. Since the larger portfolios are generally highly correlated anyway, this could trigger significant downward volatility.

These "sell-off" periods, as well as many other forms of volatility that occur in finance, lead to heteroskedasticity that is serially correlated and hence conditional on periods of increased variance. Thus we say that such series are conditional heteroskedastic.

One of the challenging aspects of conditional heteroskedastic series is that if we were to plot the correlogram of a series with volatility we might still see what appears to be a realisation of stationary discrete white noise. That is, the volatility itself is hard to detect purely from the correlogram. This is despite the fact that the series is most definitely non-stationary as its variance is not constant in time.

We are going to describe a mechanism for detecting conditional heteroskedastic series in this chapter and then use the ARCH and GARCH models to account for it, ultimately leading to more realistic forecasting performance, and thus more profitable trading strategies.

# 11.5 Autoregressive Conditional Heteroskedastic Models

We have now discussed conditional heteroskedasticity (CH) and its importance within financial series. We want a class of models that can incorporate CH in a natural way. We know that the ARIMA model does not account for CH, so how can we proceed?

Well, how about a model that utilises an autoregressive process for the variance itself ? That is, a model that actually accounts for the changes in the variance over time using past values of the variance.

This is the basis of the Autoregressive Conditional Heteroskedastic (ARCH) model. We will begin with the simplest possible case, namely an ARCH model that depends solely on the previous variance value in the series.

#### 11.5.1 ARCH Definition

Definition 11.5.1. Autoregressive Conditional Heteroskedastic Model of Order Unity.

A time series {t} is given at each instance by:

$$\epsilon_t = \sigma_t w_t \tag{11.5}$$

Where {wt} is discrete white noise, with zero mean and unit variance, and σ 2 t is given by:

$$\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 \tag{11.6}$$

Where α<sup>0</sup> and α<sup>1</sup> are parameters of the model.

We say that {t} is an autoregressive conditional heteroskedastic model of order unity, denoted by ARCH(1). Substituting for σ 2 t , we receive:

$$\epsilon_t = w_t \sqrt{\alpha_0 + \alpha_1 \epsilon_{t-1}^2} \tag{11.7}$$

#### 11.5.2 Why Does This Model Volatility?

I personally find the above "formal" definition lacking in motivation as to how it introduces volatility. However, you can see how it is introduced by squaring both sides of the previous equation:

$$\operatorname{Var}(\epsilon_t) = \operatorname{E}[\epsilon_t^2] - (\operatorname{E}[\epsilon_t])^2 \tag{11.8}$$

$$= \mathbf{E}[\epsilon_t^2] \tag{11.9}$$

$$= \mathbf{E}[w_t^2] \mathbf{E}[\alpha_0 + \alpha_1 \epsilon_{t-1}^2] \tag{11.10}$$

$$= \mathbf{E}[\alpha_0 + \alpha_1 \epsilon_{t-1}^2] \tag{11.11}$$

$$= \alpha_0 + \alpha_1 \operatorname{Var}(\epsilon_{t-1}) \tag{11.12}$$

Where I have used the definitions of the variance Var(x) = E[x 2 ] − (E[x])<sup>2</sup> and the linearity of the expectation operator E, along with the fact that {wt} has zero mean and unit variance.

Thus we can see that the variance of the series is simply a linear combination of the variance of the prior element of the series. Simply put, the variance of an ARCH(1) process follows an AR(1) process.

It is interesting to compare the ARCH(1) model with an AR(1) model. Recall that the latter is given by:

$$x_t = \alpha_0 + \alpha_1 x_{t-1} + w_t \tag{11.13}$$

You can see that the models are similar in form with the exception of the white noise term.

### 11.5.3 When Is It Appropriate To Apply ARCH(1)?

What approach can be taken in order to determine whether an ARCH(1) model is appropriate to apply to a series?

Consider that when we were attempting to fit an AR(1) model we were concerned with the decay of the first lag on a correlogram of the series. However if we apply the same logic to the square of the residuals and see whether we can apply an AR(1) to these squared residuals then we have an indication that an ARCH(1) process may be appropriate.

Note that ARCH(1) should only ever be applied to a series that has already had an appropriate model fitted sufficient to leave the residuals looking like discrete white noise. Since we can only tell whether ARCH is appropriate or not by squaring the residuals and examining the correlogram, we also need to ensure that the mean of the residuals is zero.

Crucially ARCH should only ever be applied to series that do not have any trends or seasonal effects, which are those that have no evident serial correlation. ARIMA is often applied to such a series (or even Seasonal ARIMA) at which point ARCH may be a good fit.

### 11.5.4 ARCH(p) Models

It is straightforward to extend ARCH to higher order lags. An ARCH(p) process is given by:

$$\epsilon_t = w_t \sqrt{\alpha_0 + \sum_{i=1}^p \alpha_p \epsilon_{t-i}^2} \tag{11.14}$$

You can think of ARCH(p) as applying an AR(p) model to the variance of the series.

An obvious question to ask at this stage is if we are going to apply an AR(p) process to the variance, why not a Moving Average MA(q) model as well? Or a mixed model such as ARMA(p,q)?

This is actually the motivation for the Generalised ARCH model, known as GARCH, which we will now define and discuss.

# 11.6 Generalised Autoregressive Conditional Heteroskedastic Models

#### 11.6.1 GARCH Definition

Definition 11.6.1. Generalised Autoregressive Conditional Heteroskedastic Model of Order p, q.

A time series {t} is given at each instance by:

$$\epsilon_t = \sigma_t w_t \tag{11.15}$$

Where {wt} is discrete white noise, with zero mean and unit variance, and σ 2 t is given by:

$$\sigma_t^2 = \alpha_0 + \sum_{i=1}^q \alpha_i \epsilon_{t-i}^2 + \sum_{j=1}^p \beta_j \sigma_{t-j}^2 \tag{11.16}$$

Where α<sup>i</sup> and β<sup>j</sup> are parameters of the model.

We say that {t} is a generalised autoregressive conditional heteroskedastic model of order p,q, denoted by GARCH(p,q).

Hence this definition is similar to that of ARCH(p) with the exception that we are adding moving average terms. That is, the value of σ <sup>2</sup> at t, σ 2 t , is dependent upon previous σ 2 <sup>t</sup>−<sup>j</sup> values.

Thus GARCH is the "ARMA equivalent" of ARCH, which only has an autoregressive component.

#### 11.6.2 Simulations, Correlograms and Model Fittings

We are going to begin with the simplest possible case of the model–GARCH(1,1). This means we are going to consider a single autoregressive lag and a single "moving average" lag. The model is given by the following:

$$\epsilon_t = \sigma_t w_t \tag{11.17}$$

$$\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + \beta_1 \sigma_{t-1}^2 \tag{11.18}$$

Note that it is necessary for α<sup>1</sup> + β<sup>1</sup> < 1 otherwise the series will become unstable.

We can see that the model has three parameters, namely α0, α<sup>1</sup> and β1. Let us set α<sup>0</sup> = 0.2, α<sup>1</sup> = 0.5 and β<sup>1</sup> = 0.3.

To create the GARCH(1,1) model in R we need to perform a similar procedure as for the original random walk simulations. We need to create a vector w to store our random white noise values, a separate vector eps to store our time series values and finally a vector sigsq to store the ARMA variances.

We can use the R rep command to create a vector of zeros that we will populate with our GARCH values:

```
> set.seed(2)
> a0 <- 0.2
> a1 <- 0.5
> b1 <- 0.3
> w <- rnorm(10000)
> eps <- rep(0, 10000)
> sigsq <- rep(0, 10000)
> for (i in 2:10000) {
> sigsq[i] <- a0 + a1 * (eps[i-1]^2) + b1 * sigsq[i-1]
> eps[i] <- w[i]*sqrt(sigsq[i])
> }
```

At this stage we have generated our GARCH model using the aforementioned parameters over 10,000 samples. We are now in a position to plot the correlogram, which is given in Figure 11.7.

#### > acf(eps)

Notice that the series looks like a realisation of a discrete white noise process. However, if we plot correlogram of the square of the series, as given in Figure 11.8,

> acf(eps^2)

we see substantial evidence of a conditionally heteroskedastic process via the decay of successive lags.

As in the previous chapter we now want to try and fit a GARCH model to this simulated series to see if we can recover the parameters. Thankfully a helpful library called tseries provides the garch command to carry this procedure out:

#### > require(tseries)

We can then use the confint command to produce confidence intervals at the 97.5% level for the parameters:

> eps.garch <- garch(eps, trace=FALSE) > confint(eps.garch)

![](_page_14_Figure_0.jpeg)

![](_page_14_Figure_1.jpeg)

Figure 11.7: Correlogram of a simulated GARCH(1,1) model with α<sup>0</sup> = 0.2, α<sup>1</sup> = 0.5 and β<sup>1</sup> = 0.3

![](_page_14_Figure_4.jpeg)

Figure 11.8: Correlogram of a simulated GARCH(1,1) models squared values with α<sup>0</sup> = 0.2, α<sup>1</sup> = 0.5 and β<sup>1</sup> = 0.3

```
2.5 % 97.5 %
a0 0.1786255 0.2172683
a1 0.4271900 0.5044903
b1 0.2861566 0.3602687
```

We can see that the true parameters all fall within the respective confidence intervals.

### 11.6.3 Financial Data

Now that we know how to simulate and fit a GARCH model we are going to to apply the procedure to some financial series. In particular let us try fitting ARIMA and GARCH to the FTSE100 index of the largest UK companies by market capitalisation. Yahoo Finance uses the symbol ^FTSE for the index. We can use quantmod to obtain the data:

- > require(quantmod)
- > getSymbols("^FTSE")

We can then calculate the differences of the log returns of the closing price:

```
> ftrt = diff(log(Cl(FTSE)))
```

Let us plot the values as given in Figure [11.9.](#page-15-0)

> plot(ftrt)

It is very clear that there are periods of increased volatility, particularly around 2008-2009, late 2011 and more recently in mid 2015:

![](_page_15_Figure_11.jpeg)

<span id="page-15-0"></span>![](_page_15_Figure_12.jpeg)

```
> ft <- as.numeric(ftrt)
> ft <- ft[!is.na(ft)]
```

The next task is to fit a suitable ARIMA(p,d,q) model. We saw how to do that in the previous chapter so the procedure will not be repeated here. Instead the code will simply be provided:

```
> ftfinal.aic <- Inf
> ftfinal.order <- c(0,0,0)
> for (p in 1:4) for (d in 0:1) for (q in 1:4) {
> ftcurrent.aic <- AIC(arima(ft, order=c(p, d, q)))
> if (ftcurrent.aic < ftfinal.aic) {
> ftfinal.aic <- ftcurrent.aic
> ftfinal.order <- c(p, d, q)
> ftfinal.arima <- arima(ft, order=ftfinal.order)
> }
> }
```

Since we have already differenced the FTSE returns once we should expect our integrated component d to equal zero, which it does:

#### > ftfinal.order [1] 4 0 4

Thus we receive an ARIMA(4,0,4) model. This contains four autoregressive parameters and four moving average parameters.

We are now in a position to decide whether the residuals of this model fit possess evidence of conditional heteroskedastic behaviour. To test this we need to plot the correlogram of the residuals, as given in Figure 11.10.

#### > acf(resid(ftfinal.arima))

This looks like a realisation of a discrete white noise process indicating that we have achieved a good fit with the ARIMA(4,0,4) model.

To test for conditional heteroskedastic behaviour we need to square the residuals and plot the corresponding correlogram, as given in Figure 11.11.

#### > acf(resid(ftfinal.arima)^2)

We can see clear evidence of serial correlation in the squared residuals, leading us to the conclusion that conditional heteroskedastic behaviour is present in the diff log return series of the FTSE100.

We are now in a position to fit a GARCH model using the tseries library.

The first command actually fits an appropriate GARCH model, with the trace=F parameter telling R to suppress excessive output.

The second command removes the first element of the residuals, since it is NA:

#### > ft.garch <- garch(ft, trace=F)

```
> ft.res <- ft.garch$res[-1]
```

To test for a good fit we can plot the correlogram of the GARCH residuals and the square GARCH residuals as given in Figure 11.12.

> acf(ft.res)

![](_page_17_Figure_1.jpeg)

Figure 11.10: Residuals of an ARIMA(4,0,4) fit to the FTSE100 diff log returns

![](_page_17_Figure_3.jpeg)

Figure 11.11: Squared residuals of an ARIMA(4,0,4) fit to the FTSE100 diff log returns

The correlogram looks like a realisation of a discrete white noise process indicating a good fit. Let us now try the squared residuals as given in Figure 11.13.

![](_page_18_Figure_1.jpeg)

Figure 11.12: Residuals of a GARCH(p,q) fit to the ARIMA(4,0,4) fit of the FTSE100 diff log returns

#### > acf(ft.res^2)

Once again we have what looks like a realisation of a discrete white noise process, indicating that we have "explained" the serial correlation present in the squared residuals with an appropriate mixture of ARIMA(p,d,q) and GARCH(p,q).

# 11.7 Next Steps

We are now at the point in our time series education where we have studied ARIMA and GARCH. This knowledge allows us to fit a combination of these models to a stock market index and determine if we have achieved a good fit or not.

The next step is to actually produce forecasts of future daily returns values from this combination and use it to create a basic trading strategy. We will discuss this in the Quantitative Trading Strategies part of the book.

![](_page_19_Figure_0.jpeg)

Figure 11.13: Squared residuals of a GARCH(p,q) fit to the ARIMA(4,0,4) fit of the FTSE100 diff log returns
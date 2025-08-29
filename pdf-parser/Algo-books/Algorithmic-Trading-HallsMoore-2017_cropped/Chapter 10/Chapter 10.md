# Chapter 10

# Autoregressive Moving Average Models

In the last chapter we looked at random walks and white noise as basic time series models for certain financial instruments, such as daily equity and equity index prices. We found that in some cases a random walk model was insufficient to capture the full autocorrelation behaviour of the instrument, which motivates more sophisticated models.

In this chapter we are going to discuss three types of model, namely the Autoregressive (AR) model of order p, the Moving Average (MA) model of order q and the mixed Autogressive Moving Average (ARMA) model of order p, q. These models will help us attempt to capture or "explain" more of the serial correlation present within an instrument. Ultimately they will provide us with a means of forecasting the future prices.

However, it is well known that financial time series possess a property known as volatility clustering. That is, the volatility of the instrument is not constant in time. The technical term for this behaviour is conditional heteroskedasticity. Since the AR, MA and ARMA models are not conditionally heteroskedastic, that is, they don't take into account volatility clustering, we will ultimately need a more sophisticated model for our predictions.

Such models include the Autogressive Conditional Heteroskedastic (ARCH) model, the Generalised Autogressive Conditional Heteroskedastic (GARCH) model and the many variants thereof. GARCH is particularly well known in quant finance and is primarily used for financial time series simulations as a means of estimating risk.

However, we will be building up to these models from simpler versions in order to see how each new variant changes our predictive ability. Despite the fact that AR, MA and ARMA are relatively simple time series models, they are the basis of more complicated models such as the Autoregressive Integrated Moving Average (ARIMA) and the GARCH family. Hence it is important that we study them.

One of our trading strategies later in the book will be to combine ARIMA and GARCH in order to predict prices n periods in advance. However, we will have to wait until we have discussed both ARIMA and GARCH separately before we apply them to this strategy.

# 10.1 How Will We Proceed?

In this chapter we are going to outline some new time series concepts that will be needed for the remaining methods, namely strict stationarity and the Akaike information criterion (AIC).

Subsequent to these new concepts we will follow the traditional pattern for studying new time series models:

- Rationale The first task is to provide a reason why we are interested in a particular model, as quants. Why are we introducing the time series model? What effects can it capture? What do we gain (or lose) by adding in extra complexity?
- Definition We need to provide the full mathematical definition (and associated notation) of the time series model in order to minimise any ambiguity.
- Second Order Properties We will discuss (and in some cases derive) the second order properties of the time series model, which includes its mean, its variance and its autocorrelation function.
- Correlogram We will use the second order properties to plot a correlogram of a realisation of the time series model in order to visualise its behaviour.
- Simulation We will simulate realisations of the time series model and then fit the model to these simulations to ensure we have accurate implementations and understand the fitting process.
- Real Financial Data We will fit the time series model to real financial data and consider the correlogram of the residuals in order to see how the model accounts for serial correlation in the original series.
- Prediction We will create n-step ahead forecasts of the time series model for particular realisations in order to ultimately produce trading signals.

Nearly all of the chapters written in this book on time series models will fall into this pattern and it will allow us to easily compare the differences between each model as we add further complexity.

We will begin by looking at strict stationarity and the AIC.

# 10.2 Strictly Stationary

We provided the definition of stationarity in the chapter on serial correlation. However, because we are going to be entering the realm of many financial series, with various frequencies, we need to make sure that our eventual models take into account the time-varying volatility of these series. In particular we need to consider their heteroskedasticity.

We will come across this issue when we try to fit certain models to historical series. Generally, not all of the serial correlation in the residuals of fitted models can be accounted for without taking heteroskedasticity into account. This brings us back to stationarity. A series is not stationary in the variance if it has time-varying volatility, by definition.

This motivates a more rigourous definition of stationarity, namely strict stationarity:

Definition 10.2.1. Strictly Stationary Series. A time series model, {xt}, is strictly stationary if the joint statistical distribution of the elements xt<sup>1</sup> , . . . , xt<sup>n</sup> is the same as that of xt1+m, . . . , xtn+m, ∀t<sup>i</sup> , m.

One can think of this definition as simply that the distribution of the time series is unchanged for any abritrary shift in time.

In particular, the mean and the variance are constant in time for a strictly stationary series and the autocovariance between x<sup>t</sup> and x<sup>s</sup> (say) depends only on the absolute difference of t and s, |t − s|.

We will be revisiting strictly stationary series in future chapters.

# 10.3 Akaike Information Criterion

I mentioned in previous chapters that we would eventually need to consider how to choose between separate "best" models. This is true not only of time series analysis, but also of machine learning and, more broadly, statistics in general.

The two main methods we will use, for the time being, are the Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC).

We will briefly consider the AIC, as it will be used in the next section when we come to discuss the ARMA model.

AIC is essentially a tool to aid in model selection. That is, if we have a selection of statistical models (including time series), then the AIC estimates the "quality" of each model, relative to the others that we have available.

It is based on information theory, which is a highly interesting, deep topic that unfortunately is beyond the scope of this book. It attempts to balance the complexity of the model, which in this case means the number of parameters, with how well it fits the data. Here is a definition:

Definition 10.3.1. Akaike Information Criterion. If we take the likelihood function for a statistical model, which has k parameters, and L maximises the likelihood, then the Akaike Information Criterion is given by:

$$AIC = -2\log(L) + 2k\tag{10.1}$$

The preferred model, from a selection of models, has the minimum AIC of the group. You can see that the AIC grows as the number of parameters, k, increases, but is reduced if the negative log-likelihood increases. Essentially it penalises models that are overfit.

We are going to be creating AR, MA and ARMA models of varying orders and one way to choose the "best" model fit for a particular dataset is to use the AIC.

# 10.4 Autoregressive (AR) Models of order p

The first model to be considered is the Autoregressive model of order p, often shortened to AR(p).

#### 10.4.1 Rationale

In the previous chapter we considered the random walk model, where each term, x<sup>t</sup> is dependent solely upon the previous term, xt−<sup>1</sup> and a stochastic white noise term, wt:

$$x_t = x_{t-1} + w_t \tag{10.2}$$

The autoregressive model is simply an extension of the random walk that includes terms further back in time. The structure of the model is linear, that is the model depends linearly on the previous terms, with coefficients for each term. This is where the "regressive" comes from in "autoregressive". It is essentially a regression model where the previous terms are the predictors.

Definition 10.4.1. Autoregressive Model of order p. A time series model, {xt}, is an autoregressive model of order p, AR(p), if:

$$x_t = \alpha_1 x_{t-1} + \ldots + \alpha_p x_{t-p} + w_t \tag{10.3}$$

$$= \sum_{i=1}^{p} \alpha_i x_{t-i} + w_t \tag{10.4}$$

Where {wt} is white noise and α<sup>i</sup> ∈ R, with α<sup>p</sup> 6= 0 for a p-order autoregressive process.

If we consider the Backward Shift Operator, B, then we can rewrite the above as a function θ of B:

$$\theta_p(\mathbf{B})x_t = (1 - \alpha_1 \mathbf{B} - \alpha_2 \mathbf{B}^2 - \dots - \alpha_p \mathbf{B})x_t = w_t \tag{10.5}$$

Perhaps the first thing to notice about the AR(p) model is that a random walk is simply AR(1) with α<sup>1</sup> equal to unity. As we stated above, the autogressive model is an extension of the random walk, so this makes sense.

It is straightforward to make predictions with the AR(p) model for any time t. Once the α<sup>i</sup> coefficients are determined the estimate simply becomes:

$$\hat{x}_t = \alpha_1 x_{t-1} + \ldots + \alpha_p x_{t-p} \tag{10.6}$$

Hence we can make n-step ahead forecasts by producing xˆt, xˆt+1, xˆt+2, . . . up to xˆt+n. In fact, once we consider the ARMA models later in the chapter, we will use the R predict function to create forecasts (along with standard error confidence interval bands) that will help us produce trading signals.

#### 10.4.2 Stationarity for Autoregressive Processes

One of the most important aspects of the AR(p) model is that it is not always stationary. Indeed the stationarity of a particular model depends upon the parameters. I have touched on this before in my other book, Successful Algorithmic Trading.

In order to determine whether an AR(p) process is stationary or not we need to solve the characteristic equation. The characteristic equation is simply the autoregressive model, written in backward shift form, set to zero:

$$\theta_p(\mathbf{B}) = 0 \tag{10.7}$$

We solve this equation for B. In order for the particular autoregressive process to be stationary we need all of the absolute values of the roots of this equation to exceed unity. This is an extremely useful property and allows us to quickly calculate whether an AR(p) process is stationary or not.

The following examples will make this idea concrete:

- Random Walk The AR(1) process with α<sup>1</sup> = 1 has the characteristic equation θ = 1−B. Clearly this has root B = 1 and as such is not stationary.
- AR(1) If we choose α<sup>1</sup> = 1 <sup>4</sup> we get x<sup>t</sup> = 1 4 xt−<sup>1</sup> + wt. This gives us a characteristic equation of 1 − 1 <sup>4</sup>B = 0, which has a root B = 4 > 1 and so this particular AR(1) process is stationary.
- AR(2) If we set α<sup>1</sup> = α<sup>2</sup> = 1 2 then we get x<sup>t</sup> = 1 2 xt−<sup>1</sup> + 1 2 xt−<sup>2</sup> + wt. Its characteristic equation becomes − 1 2 (B − 1)(B + 2) = 0, which gives two roots of B = 1, −2. Since this has a unit root it is a non-stationary series. However, other AR(2) series can be stationary.

#### 10.4.3 Second Order Properties

The mean of an AR(p) process is zero. However, the autocovariances and autocorrelations are given by recursive functions, known as the Yule-Walker equations. The full properties are given below:

$$\mu_x = E(x_t) = 0 \tag{10.8}$$

$$\gamma_k = \sum_{i=1}^p \alpha_i \gamma_{k-i}, \quad k > 0 \tag{10.9}$$

$$\rho_k = \sum_{i=1}^p \alpha_i \rho_{k-i}, \ \ k > 0 \tag{10.10}$$

Note that it is necessary to know the α<sup>i</sup> parameter values prior to calculating the autocorrelations.

Now that the second order properties have been states it is possible to simulate various orders of AR(p) and plot the corresponding correlograms.

### 10.4.4 Simulations and Correlograms

#### AR(1)

Let us begin with an AR(1) process. This is similar to a random walk, except that α<sup>1</sup> does not have to equal unity. Our model is going to have α<sup>1</sup> = 0.6. The R code for creating this simulation is given as follows:

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- 0.6*x[t-1] + w[t]
```

Notice that our for loop is carried out from 2 to 100, not 1 to 100, as x[t-1] when t = 0 is not indexable. Similarly for higher order AR(p) processes, t must range from p to 100 in this loop.

We can plot the realisation of this model and its associated correlogram using the layout function, given in Figure [10.1.](#page-5-0)

```
> layout(1:2)
> plot(x, type="l")
> acf(x)
```

![](_page_5_Figure_7.jpeg)

<span id="page-5-0"></span>Figure 10.1: Realisation of AR(1) Model, with α<sup>1</sup> = 0.6 and Associated Correlogram.

We can now try fitting an AR(p) process to the simulated data that we have just generated to see if we can recover the underlying parameters. You may recall that we carried out a similar procedure in the previous chapter on white noise and random walks.

R provides a useful command ar to fit autoregressive models. We can use this method to firstly tell us the best order p of the model (as determined by the AIC above) and provide us with parameter estimates for the α<sup>i</sup> , which we can then use to form confidence intervals.

For completeness we recreate the x series:

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- 0.6*x[t-1] + w[t]
```

Now we use the ar command to fit an autoregressive model to our simulated AR(1) process, using maximum likelihood estimation (MLE) as the fitting procedure.

We will firstly extract the best obtained order:

```
> x.ar <- ar(x, method = "mle")
> x.ar$order
[1] 1
```

The ar command has successfully determined that our underlying time series model is an AR(1) process.

We can then obtain the α<sup>i</sup> parameter(s) estimates:

#### > x.ar\$ar

#### [1] 0.5231187

The MLE procedure has produced an estimate, αˆ<sup>1</sup> = 0.523, which is slightly lower than the true value of α<sup>1</sup> = 0.6.

Finally, we can use the standard error, with the asymptotic variance, to construct 95% confidence intervals around the underlying parameter. To achieve this we simply create a vector c(-1.96, 1.96) and then multiply it by the standard error:

```
x.ar$ar + c(-1.96, 1.96)*sqrt(x.ar$asy.var)
[1] 0.3556050 0.6906324
```

The true parameter does fall within the 95% confidence interval. This is to be expected since the realisation has been generated from the model specifically.

How about if we change the α<sup>1</sup> = −0.6? The plot is given in Figure 10.2.

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- -0.6*x[t-1] + w[t]
> layout(1:2)
> plot(x, type="l")
> acf(x)
   As before we can fit an AR(p) model using ar:
> set.seed(1)
```

```
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- -0.6*x[t-1] + w[t]
> x.ar <- ar(x, method = "mle")
> x.ar$order
[1] 1
> x.ar$ar
[1] -0.5973473
```

![](_page_7_Figure_0.jpeg)

Figure 10.2: Realisation of AR(1) Model, with α<sup>1</sup> = −0.6 and Associated Correlogram.

#### > x.ar\$ar + c(-1.96, 1.96)\*sqrt(x.ar\$asy.var) [1] -0.7538593 -0.4408353

Once again we recover the correct order of the model, with a very good estimate αˆ<sup>1</sup> = −0.597 of α<sup>1</sup> = −0.6. We also see that the true parameter falls within the 95% confidence interval once again.

#### AR(2)

Let us add some more complexity to our autoregressive processes by simulating a model of order 2. In particular, we will set α<sup>1</sup> = 0.666, but also set α<sup>2</sup> = −0.333. Here's the full code to simulate and plot the realisation, as well as the correlogram for such a series, given in Figure 10.3.

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 3:100) x[t] <- 0.666*x[t-1] - 0.333*x[t-2] + w[t]
> layout(1:2)
> plot(x, type="l")
> acf(x)
```

As before we can see that the correlogram differs significantly from that of white noise, as we would expect. There are statistically significant peaks at k = 1, k = 3 and k = 4.

Once again we are going to use the ar command to fit an AR(p) model to our underlying AR(2) realisation. The procedure is similar as for the AR(1) fit:

> set.seed(1)

![](_page_8_Figure_0.jpeg)

Figure 10.3: Realisation of AR(2) Model, with α<sup>1</sup> = 0.666, α<sup>2</sup> = −0.333 and Associated Correlogram.

```
> x <- w <- rnorm(100)
> for (t in 3:100) x[t] <- 0.666*x[t-1] - 0.333*x[t-2] + w[t]
> x.ar <- ar(x, method = "mle")
Warning message:
In arima0(x, order = c(i, 0L, 0L), include.mean = demean) :
  possible convergence problem: optim gave code = 1
> x.ar$order
[1] 2
> x.ar$ar
[1] 0.6961005 -0.3946280
```

The correct order has been recovered and the parameter estimates αˆ<sup>1</sup> = 0.696 and αˆ<sup>2</sup> = −0.395 are not too far off the true parameter values of α<sup>1</sup> = 0.666 and α<sup>2</sup> = −0.333.

Notice that we receive a convergence warning message. Notice also that R actually uses the arima0 function to calculate the AR model. As we will learn in subsequent chapters, AR(p) models are simply ARIMA(p, 0, 0) models, and thus an AR model is a special case of ARIMA with no Moving Average (MA) or Integrated (I) component.

We will also be using the arima command to create confidence intervals around multiple parameters, which is why we have neglected to do it here.

Now that we have created some simulated data it is time to apply the AR(p) models to financial asset time series.

### 10.4.5 Financial Data

#### Amazon Inc.

Let us begin by obtaining the stock price for Amazon (AMZN) using quantmod as in the previous chapter:

| ><br>require(quantmod)  |        |        |        |        |         |        |
|-------------------------|--------|--------|--------|--------|---------|--------|
| ><br>getSymbols("AMZN") |        |        |        |        |         |        |
| ><br>AMZN               |        |        |        |        |         |        |
|                         |        |        |        |        |         |        |
|                         |        |        |        |        |         |        |
| 2015-08-12              | 523.75 | 527.50 | 513.06 | 525.91 | 3962300 | 525.91 |
| 2015-08-13              | 527.37 | 534.66 | 525.49 | 529.66 | 2887800 | 529.66 |
| 2015-08-14              | 528.25 | 534.11 | 528.25 | 531.52 | 1983200 | 531.52 |

The first task is to always plot the price for a brief visual inspection. In this case we will be using the daily closing prices. The plot is given in Figure [10.4.](#page-9-0)

#### > plot(Cl(AMZN))

You'll notice that quantmod adds some formatting for us, namely the date, and a slightly prettier chart than the usual R charts.

![](_page_9_Figure_7.jpeg)

<span id="page-9-0"></span>Figure 10.4: Daily Closing Price of AMZN.

We are now going to take the logarithmic returns of AMZN and then the first-order difference of the series in order to convert the original price series from a non-stationary series to a (potentially) stationary one.

This allows us to compare "apples to apples" between equities, indexes or any other asset, for use in later multivariate statistics, such as when calculating a covariance matrix.

Let us create a new series, amznrt, to hold our differenced log returns:

> amznrt = diff(log(Cl(AMZN)))

Once again, we can plot the series, as given in Figure [10.5.](#page-10-0)

> plot(amznrt)

![](_page_10_Figure_5.jpeg)

<span id="page-10-0"></span>Figure 10.5: First Order Differenced Daily Logarithmic Returns of AMZN Closing Prices.

At this stage we want to plot the correlogram. We are looking to see if the differenced series looks like white noise. If it does not then there is unexplained serial correlation, which might be "explained" by an autoregressive model. See Figure 10.6.

> acf(amznrt, na.action=na.omit)

We notice a statististically significant peak at k = 2. Hence there is a reasonable possibility of unexplained serial correlation. Be aware though, that this may be due to sampling bias. As such, we can try fitting an AR(p) model to the series and produce confidence intervals for the parameters:

```
> amznrt.ar <- ar(amznrt, na.action=na.omit)
> amznrt.ar$order
[1] 2
> amznrt.ar$ar
[1] -0.02779869 -0.06873949
> amznrt.ar$asy.var
```

![](_page_11_Figure_1.jpeg)

Figure 10.6: Correlogram of First Order Differenced Daily Logarithmic Returns of AMZN Closing Prices.

[,1] [,2] [1,] 4.59499e-04 1.19519e-05 [2,] 1.19519e-05 4.59499e-04

Fitting the ar autoregressive model to the first order differenced series of log prices produces an AR(2) model, with αˆ<sup>1</sup> = −0.0278 and αˆ<sup>2</sup> = −0.0687. I have also output the aysmptotic variance so that we can calculate standard errors for the parameters and produce confidence intervals. We want to see whether zero is part of the 95% confidence interval, as if it is, it reduces our confidence that we have a true underlying AR(2) process for the AMZN series.

To calculate the confidence intervals at the 95% level for each parameter, we use the following commands. We take the square root of the first element of the asymptotic variance matrix to produce a standard error, then create confidence intervals by multiplying it by -1.96 and 1.96 respectively, for the 95% level:

```
> -0.0278 + c(-1.96, 1.96)*sqrt(4.59e-4)
[1] -0.0697916 0.0141916
> -0.0687 + c(-1.96, 1.96)*sqrt(4.59e-4)
[1] -0.1106916 -0.0267084
```

Note that this becomes more straightforward when using the arima function, but we will wait until the next chapter before introducing it properly.

Thus we can see that for α<sup>1</sup> zero is contained within the confidence interval, while for α<sup>2</sup> zero is not contained in the confidence interval. Hence we should be very careful in thinking that we really have an underlying generative AR(2) model for AMZN.

In particular we note that the autoregressive model does not take into account volatility clustering, which leads to clustering of serial correlation in financial time series. When we consider the ARCH and GARCH models in later chapters, we will account for this.

When we come to use the full arima function in the trading strategy section of the book we will make predictions of the daily log price series in order to allow us to create trading signals.

#### S&P500 US Equity Index

Along with individual stocks we can also consider the US Equity index, the S&P500. Let us apply all of the previous commands to this series and produce the plots as before:

| ><br>getSymbols("^GSPC") |         |         |         |         |            |         |
|--------------------------|---------|---------|---------|---------|------------|---------|
| ><br>GSPC                |         |         |         |         |            |         |
|                          |         |         |         |         |            |         |
|                          |         |         |         |         |            |         |
| 2015-08-12               | 2081.10 | 2089.06 | 2052.09 | 2086.05 | 4269130000 | 2086.05 |
|                          |         |         |         |         |            |         |
| 2015-08-13               | 2086.19 | 2092.93 | 2078.26 | 2083.39 | 3221300000 | 2083.39 |
| 2015-08-14               | 2083.15 | 2092.45 | 2080.61 | 2091.54 | 2795590000 | 2091.54 |
|                          |         |         |         |         |            |         |

We can plot the prices, as given in Figure [10.7.](#page-12-0)

> plot(Cl(GSPC))

![](_page_12_Figure_7.jpeg)

<span id="page-12-0"></span>Figure 10.7: Daily Closing Price of S&500.

As before we will create the first order difference of the log closing prices:

#### > gspcrt = diff(log(Cl(GSPC)))

Once again we can plot the series. It is given in Figure 10.8.

![](_page_13_Figure_1.jpeg)

Figure 10.8: First Order Differenced Daily Logarithmic Returns of S&500 Closing Prices.

It is clear from this chart that the volatility is not stationary in time. This is also reflected in the plot of the correlogram, given in Figure 10.9. There are many peaks, including k = 1 and k = 2, which are statistically significant beyond a white noise model.

In addition we see evidence of long-memory processes as there are some statistically significant peaks at k = 16, k = 18 and k = 21:

#### > acf(gspcrt, na.action=na.omit)

Ultimately we will need a more sophisticated model than an autoregressive model of order p. However, at this stage we can still try fitting such a model. Let us see what we get if we do so:

```
> gspcrt.ar <- ar(gspcrt, na.action=na.omit)
> gspcrt.ar$order
[1] 22
> gspcrt.ar$ar
[1] -0.111821507 -0.060150504 0.018791594 -0.025619932 -0.046391435
[6] 0.002266741 -0.030089046 0.030430265 -0.007623949 0.044260402
[11] -0.018924358 0.032752930 -0.001074949 -0.042891664 -0.039712505
[16] 0.052339497 0.016554471 -0.067496381 0.007070516 0.035721299
[21] -0.035419555 0.031325869
```

Using ar produces an AR(22) model, i.e. a model with 22 non-zero parameters! What does this tell us? It is indicating that there is likely a lot more complexity in the serial correlation than a simple linear model of past prices can really account for.

![](_page_14_Figure_1.jpeg)

Figure 10.9: Correlogram of First Order Differenced Daily Logarithmic Returns of S&500 Closing Prices.

However we already knew this because we can see that there is significant serial correlation in the volatility. For instance looking at the chart of returns displays the highly volatile period around 2008.

This motivates the next set of models, namely the Moving Average MA(q) and the Autoregressive Moving Average ARMA(p, q). We will learn about both of these in the next couple of sections of this chapter. As is repeatedly mentioned these models will ultimately lead us to the ARIMA and GARCH family of models, both of which will provide a much better fit to the serial correlation complexity of the S&P500.

This will allows us to improve our forecasts significantly and ultimately produce more profitable strategies.

# 10.5 Moving Average (MA) Models of order q

In the previous section we considered the Autoregressive model of order p, also known as the AR(p) model. We introduced it as an extension of the random walk model in an attempt to explain additional serial correlation in financial time series.

Ultimately we realised that it was not sufficiently flexible to truly capture all of the autocorrelation in the closing prices of Amazon Inc. (AMZN) and the S&P500 US Equity Index. The primary reason for this is that both of these assets are conditionally heteroskedastic, which means that they are non-stationary and have periods of "varying variance" or volatility clustering, which is not taken into account by the AR(p) model.

In the next chapter we will consider the Autoregressive Integrated Moving Average (ARIMA)

model, as well as the conditional heteroskedastic models of the ARCH and GARCH families. These models will provide us with our first realistic attempts at forecasting asset prices.

In this section, however, we are going to introduce the Moving Average of order q model, known as MA(q). This is a component of the more general ARMA model and as such we need to understand it before moving further.

#### 10.5.1 Rationale

A Moving Average model is similar to an Autoregressive model, except that instead of being a linear combination of past time series values, it is a linear combination of the past white noise terms.

Intuitively, this means that the MA model sees such random white noise "shocks" directly at each current value of the model. This is in contrast to an AR(p) model, where the white noise "shocks" are only seen indirectly, via regression onto previous terms of the series.

A key difference is that the MA model will only ever see the last q shocks for any particular MA(q) model, whereas the AR(p) model will take all prior shocks into account, albeit in a decreasingly weak manner.

#### 10.5.2 Definition

Mathematically the MA(q) is a linear regression model and is similarly structured to AR(p):

Definition 10.5.1. Moving Average Model of order q. A time series model, {xt}, is a moving average model of order q, MA(q), if:

$$x_t = w_t + \beta_1 w_{t-1} + \ldots + \beta_q w_{t-q} \tag{10.11}$$

Where {wt} is white noise with E(wt) = 0 and variance σ 2 .

If we consider the Backward Shift Operator, B then we can rewrite the above as a function φ of B:

$$x_t = (1 + \beta_1 \mathbf{B} + \beta_2 \mathbf{B}^2 + \ldots + \beta_q \mathbf{B}^q) w_t = \phi_q(\mathbf{B}) w_t \tag{10.12}$$

We will make use of the φ function in subsequent chapters.

#### 10.5.3 Second Order Properties

As with AR(p) the mean of a MA(q) process is zero. This is easy to see as the mean is simply a sum of means of white noise terms, which are all themselves zero.

Mean: 
$$\mu_x = E(x_t) = \sum_{i=0}^{q} E(w_i) = 0$$
 (10.13)

Var: 
$$\sigma_w^2 (1 + \beta_1^2 + \ldots + \beta_q^2)$$
 (10.14)

ACF: 
$$\rho_k = \begin{cases} 1 & \text{if } k = 0\\ \sum_{i=0}^{q-k} \beta_i \beta_{i+k} / \sum_{i=0}^{q} \beta_i^2 & \text{if } k = 1, \dots, q\\ 0 & \text{if } k > q \end{cases}$$

Where β<sup>0</sup> = 1.

We are now going to generate some simulated data and use it to create correlograms. This will make the above formula for ρ<sup>k</sup> somewhat more concrete.

#### 10.5.4 Simulations and Correlograms

#### MA(1)

Let us start with a MA(1) process. If we set β<sup>1</sup> = 0.6 we obtain the following model:

$$x_t = w_t + 0.6w_{t-1} \tag{10.15}$$

As with the AR(p) model we can use R to simulate such a series and then plot the correlogram. Since we have had a lot of practice in the previous sections of carrying out plots, I will write the R code in full, rather than splitting it up:

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- w[t] + 0.6*w[t-1]
> layout(1:2)
> plot(x, type="l")
> acf(x)
```

The output is given in Figure 10.10.

As we saw above in the formula for ρk, for k > q, all autocorrelations should be zero. Since q = 1, we should see a significant peak at k = 1 and then insignificant peaks subsequent to that. However, due to sampling bias we should expect to see 5% (marginally) significant peaks on a sample autocorrelation plot.

This is precisely what the correlogram shows us in this case. We have a significant peak at k = 1 and then insignificant peaks for k > 1, except at k = 4 where we have a marginally significant peak.

This is a useful way of determining whether an MA(q) model is appropriate. By taking a look at the correlogram of a particular series we can see how many sequential non-zero lags exist. If q such lags exist then we can legitimately attempt to fit a MA(q) model to a particular series.

Since we have evidence from our simulated data of a MA(1) process we are now going to try and fit a MA(1) model to our simulated data. Unfortunately there is no equivalent ma command to the autoregressive model ar command in R.

Instead we must use the more general arima command and set the autoregressive and integrated components to zero. We do this by creating a 3-vector and setting the first two components (the autogressive and integrated parameters, respectively) to zero:

![](_page_17_Figure_0.jpeg)

Figure 10.10: Realisation of MA(1) Model, with β<sup>1</sup> = 0.6 and Associated Correlogram

```
> x.ma <- arima(x, order=c(0, 0, 1))
> x.ma
Call:
arima(x = x, order = c(0, 0, 1))
Coefficients:
        ma1 intercept
     0.6023 0.1681
s.e. 0.0827 0.1424
```

sigma^2 estimated as 0.7958: log likelihood = -130.7, aic = 267.39

We receive some useful output from the arima command. Firstly, we can see that the parameter has been estimated as βˆ <sup>1</sup> = 0.602, which is very close to the true value of β<sup>1</sup> = 0.6. Secondly, the standard errors are already calculated for us, making it straightforward to calculate confidence intervals. Thirdly, we receive an estimated variance, log-likelihood and Akaike Information Criterion (necessary for model comparison).

The major difference between arima and ar is that arima estimates an intercept term because it does not subtract the mean value of the series. Hence we need to be careful when carrying out predictions using the arima command. We will return to this point later.

As a quick check we are going to calculate confidence intervals for βˆ 1:

> 0.6023 + c(-1.96, 1.96)\*0.0827

#### [1] 0.440208 0.764392

We can see that the 95% confidence interval contains the true parameter value of β<sup>1</sup> = 0.6 and so we can judge the model a good fit. Obviously this should be expected since we simulated the data in the first place.

How do things change if we modify the sign of β<sup>1</sup> to -0.6? We can perform the same analysis:

```
> set.seed(1)
> x <- w <- rnorm(100)
> for (t in 2:100) x[t] <- w[t] - 0.6*w[t-1]
> layout(1:2)
> plot(x, type="l")
> acf(x)
```

The output is given in Figure [10.11.](#page-18-0)

![](_page_18_Figure_5.jpeg)

<span id="page-18-0"></span>Figure 10.11: Realisation of MA(1) Model, with β<sup>1</sup> = −0.6 and Associated Correlogram

We can see that at k = 1 we have a significant peak in the correlogram, except that it shows negative correlation, as we would expect from a MA(1) model with negative first coefficient. Once again all peaks beyond k = 1 are insignificant. Let us fit a MA(1) model and estimate the parameter:

```
> x.ma <- arima(x, order=c(0, 0, 1))
> x.ma
```

Call: arima(x = x, order = c(0, 0, 1)) Coefficients: ma1 intercept -0.7298 0.0486 s.e. 0.1008 0.0246

sigma^2 estimated as 0.7841: log likelihood = -130.11, aic = 266.23

βˆ <sup>1</sup> = −0.730, which is a small underestimate of β<sup>1</sup> = −0.6. Finally, let us calculate the confidence interval:

> -0.730 + c(-1.96, 1.96)\*0.1008 [1] -0.927568 -0.532432

We can see that the true parameter value of β<sup>1</sup> = −0.6 is contained within the 95% confidence interval, providing us with evidence of a good model fit.

#### MA(3)

We can run through the same procedure for a MA(3) process. This time we should expect significant peaks at k ∈ {1, 2, 3}, and insignificant peaks for k > 3.

We are going to use the following coefficients: β<sup>1</sup> = 0.6, β<sup>2</sup> = 0.4 and β<sup>3</sup> = 0.3. Let us simulate a MA(3) process from this model. I have increased the number of random samples to 1000 in this simulation, which makes it easier to see the true autocorrelation structure at the expense of making the original series harder to interpret:

```
> set.seed(3)
> x <- w <- rnorm(1000)
> for (t in 4:1000) x[t] <- w[t] + 0.6*w[t-1] + 0.4*w[t-2] + 0.3*w[t-3]
> layout(1:2)
> plot(x, type="l")
> acf(x)
```

The output is given in Figure 10.12.

As expected the first three peaks are significant. However, so is the fourth. But we can legitimately suggest that this may be due to sampling bias as we expect to see 5% of the peaks being significant beyond k = q.

We can now fit a MA(3) model to the data to try and estimate parameters:

```
> x.ma <- arima(x, order=c(0, 0, 3))
> x.ma
Call:
arima(x = x, order = c(0, 0, 3))
Coefficients:
        ma1 ma2 ma3 intercept
     0.5439 0.3450 0.2975 -0.0948
s.e. 0.0309 0.0349 0.0311 0.0704
```

```
sigma^2 estimated as 1.039: log likelihood = -1438.47, aic = 2886.95
```

![](_page_20_Figure_0.jpeg)

Figure 10.12: Realisation of  $MA(3)$  Model and Associated Correlogram

The estimates  $\hat{\beta}_1 = 0.544$ ,  $\hat{\beta}_2 = 0.345$  and  $\hat{\beta}_3 = 0.298$  are close to the true values of  $\beta_1 = 0.6$ ,  $\beta_2 = 0.4$  and  $\beta_3 = 0.3$ , respectively. We can also produce confidence intervals using the respective  $standard \ errors$ 

 $> 0.544 + c(-1.96, 1.96) *0.0309$ [1] 0.483436 0.604564  $> 0.345 + c(-1.96, 1.96) *0.0349$ [1] 0.276596 0.413404  $> 0.298 + c(-1.96, 1.96) * 0.0311$ [1] 0.237044 0.358956

In each case the  $95\%$  confidence intervals do contain the true parameter value and we can conclude that we have a good fit with our  $MA(3)$  model, as should be expected.

#### $10.5.5$ Financial Data

In the previous section we considered Amazon Inc.  $(AMZN)$  and the S&P500 US Equity Index. We fitted the  $\text{AR}(p)$  model to both and found that the model was unable to effectively capture the complexity of the serial correlation, especially in the case of the  $S\&P500$ , where conditional heteroskedastic and long-memory effects seem to be present.

#### $\text{Amazon Inc. (AMZN)}$

Let us begin by trying to fit a selection of MA(q) models to AMZN, namely with  $q \in \{1, 2, 3\}$ . As in the previous section we will use **quantmod** to download the daily prices for AMZN and then convert them into a log returns stream of closing prices:

```
> require(quantmod)
```

- > getSymbols("AMZN")
- > amznrt = diff(log(Cl(AMZN)))

Now that we have the log returns stream we can use the arima command to fit MA(1), MA(2) and MA(3) models and then estimate the parameters of each. For MA(1) we have:

```
> amznrt.ma <- arima(amznrt, order=c(0, 0, 1))
> amznrt.ma
Call:
arima(x = amznrt, order = c(0, 0, 1))
Coefficients:
        ma1 intercept
     -0.030 0.0012
s.e. 0.023 0.0006
```

sigma^2 estimated as 0.0007044: log likelihood = 4796.01, aic = -9586.02 We can plot the residuals of the daily log returns and the fitted model given in Figure [10.13.](#page-21-0) > acf(amznrt.ma\$res[-1])

![](_page_21_Figure_6.jpeg)

<span id="page-21-0"></span>Figure 10.13: Residuals of MA(1) Model Fitted to AMZN Daily Log Prices

Notice that we have a few significant peaks at lags k = 2, k = 11, k = 16 and k = 18, indicating that the MA(1) model is unlikely to be a good fit for the behaviour of the AMZN log returns, since this does not look like a realisation of white noise.

```
Let us try a MA(2) model:
> amznrt.ma <- arima(amznrt, order=c(0, 0, 2))
> amznrt.ma
Call:
arima(x = amznrt, order = c(0, 0, 2))
Coefficients:
         ma1 ma2 intercept
     -0.0254 -0.0689 0.0012
s.e. 0.0215 0.0217 0.0005
```

```
sigma^2 estimated as 0.0007011: log likelihood = 4801.02, aic = -9594.05
```

Both of the estimates for the β coefficients are negative. Let us plot the residuals once again, given in Figure [10.14.](#page-22-0)

> acf(amznrt.ma\$res[-1])

![](_page_22_Figure_4.jpeg)

<span id="page-22-0"></span>Figure 10.14: Residuals of MA(2) Model Fitted to AMZN Daily Log Prices

We can see that there is almost zero autocorrelation in the first few lags. However, we have five marginally significant peaks at lags k = 12, k = 16, k = 19, k = 25 and k = 27. This is suggestive that the MA(2) model is capturing a lot of the autocorrelation, but not all of the long-memory effects. How about a MA(3) model?

> amznrt.ma <- arima(amznrt, order=c(0, 0, 3))

```
> amznrt.ma
Call:
arima(x = amznrt, order = c(0, 0, 3))
Coefficients:
        ma1 ma2 ma3 intercept
     -0.0262 -0.0690 0.0177 0.0012
s.e. 0.0214 0.0217 0.0212 0.0005
```

```
sigma^2 estimated as 0.0007009: log likelihood = 4801.37, aic = -9592.75
   Once again, we can plot the residuals, as given in Figure 10.15.
```

```
> acf(amznrt.ma$res[-1])
```

![](_page_23_Figure_3.jpeg)

<span id="page-23-0"></span>Figure 10.15: Residuals of MA(3) Model Fitted to AMZN Daily Log Prices

The MA(3) residuals plot looks almost identical to that of the MA(2) model. This is not surprising as we are adding a new parameter to a model that has seemingly explained away much of the correlations at shorter lags, but that won't have much of an effect on the longer term lags.

All of this evidence is suggestive of the fact that an MA(q) model is unlikely to be useful in explaining all of the serial correlation in isolation, at least for AMZN.

#### S&P500

If you recall in the previous section we saw that the first order differenced daily log returns structure of the S&P500 possessed many significant peaks at various lags, both short and long. This provided evidence of both conditional heteroskedasticity (i.e. volatility clustering) and longmemory effects. It lead us to conclude that the AR(p) model was insufficient to capture all of the autocorrelation present.

As we have seen above the MA(q) model was insufficient to capture additional serial correlation in the residuals of the fitted model to the first order differenced daily log price series. We will now attempt to fit the MA(q) model to the S&P500.

One might ask why we are doing this is if we know that it is unlikely to be a good fit. This is a good question. The answer is that we need to see exactly how it is not a good fit. This is the ultimate process we will be following when we review more sophisticated models that are potentially harder to interpret.

Let us begin by obtaining the data and converting it to a first order differenced series of logarithmically transformed daily closing prices as in the previous section:

```
> getSymbols("^GSPC")
```

> gspcrt = diff(log(Cl(GSPC)))

We are now going to fit a MA(1), MA(2) and MA(3) model to the series, as we did above for AMZN. Let us start with MA(1):

```
> gspcrt.ma <- arima(gspcrt, order=c(0, 0, 1))
> gspcrt.ma
```

Call: arima(x = gspcrt, order = c(0, 0, 1))

Coefficients:

Coefficients:

|      | ma1     | intercept |
|------|---------|-----------|
|      | -0.1284 | 2e-04     |
| s.e. | 0.0223  | 3e-04     |

sigma^2 estimated as 0.0001844: log likelihood = 6250.23, aic = -12494.46

Let us make a plot of the residuals of this fitted model, as given in Figure 10.16.

```
> acf(gspcrt.ma$res[-1])
```

The first significant peak occurs at k = 2, but there are many more at k ∈ {5, 10, 14, 15, 16, 18, 20, 21}. This is clearly not a realisation of white noise and so we must reject the MA(1) model as a potential good fit for the S&P500.

Does the situation improve with MA(2)?

```
> gspcrt.ma <- arima(gspcrt, order=c(0, 0, 2))
> gspcrt.ma
Call:
arima(x = gspcrt, order = c(0, 0, 2))
```

ma1 ma2 intercept

![](_page_25_Figure_1.jpeg)

Figure 10.16: Residuals of MA(1) Model Fitted to S&P500 Daily Log Prices

|      | -0.1189 | -0.0524 | 2e-04 |
|------|---------|---------|-------|
| s.e. | 0.0216  | 0.0223  | 2e-04 |

sigma^2 estimated as 0.0001839: log likelihood = 6252.96, aic = -12497.92

Once again we can make a plot of the residuals of this fitted MA(2) model as given in Figure 10.17.

```
> acf(gspcrt.ma$res[-1])
```

While the peak at k = 2 has disappeared (as we would expect) we are still left with the significant peaks at many longer lags in the residuals. Once again we find the MA(2) model is not a good fit.

We should expect for the MA(3) model to see less serial correlation at k = 3 than for the MA(2). We should also expect no reduction in further lags.

```
> gspcrt.ma <- arima(gspcrt, order=c(0, 0, 3))
> gspcrt.ma
Call:
arima(x = gspcrt, order = c(0, 0, 3))
Coefficients:
         ma1 ma2 ma3 intercept
     -0.1189 -0.0529 0.0289 2e-04
s.e. 0.0214 0.0222 0.0211 3e-04
```

![](_page_26_Figure_1.jpeg)

Figure 10.17: Residuals of MA(2) Model Fitted to S&P500 Daily Log Prices

#### sigma^2 estimated as 0.0001838: log likelihood = 6253.9, aic = -12497.81

Finally we can make a plot of the residuals of this fitted MA(3) model as given in Figure 10.18.

> acf(gspcrt.ma\$res[-1])

This is precisely what we see in the correlogram of the residuals. Hence the MA(3) as with the other models above is not a good fit for the S&P500.

#### 10.5.6 Next Steps

We have now examined two major time series models in detail, namely the Autogressive model of order p, AR(p) and then Moving Average of order q, MA(q). We have seen that they are both capable of explaining away some of the autocorrelation in the residuals of first order differenced daily log prices of equities and indices, but volatility clustering and long-memory effects persist.

It is finally time to turn our attention to the combination of these two models, namely the Autoregressive Moving Average of order p, q, ARMA(p,q) to see if it will improve the situation any further.

![](_page_27_Figure_1.jpeg)

Figure 10.18: Residuals of MA(3) Model Fitted to S&P500 Daily Log Prices

# 10.6 Autogressive Moving Average (ARMA) Models of order p, q

We have introduced Autoregressive models and Moving Average models in the two previous sections. Now it is time to combine them to produce a more sophisticated model.

Ultimately this will lead us to the ARIMA and GARCH models that will allow us to predict asset returns and forecast volatility. These models will form the basis for trading signals and risk management techniques.

If you've read the previous sections in this chapter you will have seen that we tend to follow a pattern for our analysis of a time series model. I'll repeat it briefly here:

- Rationale Why are we interested in this particular model?
- Definition A mathematical definition to reduce ambiguity.
- Correlogram Plotting a sample correlogram to visualise a models behaviour.
- Simulation and Fitting Fitting the model to simulations, in order to ensure we have understood the model correctly.
- Real Financial Data Apply the model to real historical asset prices.

However, before delving into the ARMA model we need to discuss the Bayesian Information Criterion and the Ljung-Box test, two essential tools for helping us to choose the correct model and ensuring that any chosen model is a good fit.

#### $10.6.1$ **Bayesian Information Criterion**

In the previous section we looked at the Akaike Information Criterion (AIC) as a means of helping us choose between separate "best" time series models.

A closely related tool is the **Bayesian Information Criterion** (BIC). Essentially it has similar behaviour to the AIC in that it penalises models for having too many parameters. This may lead to *overfitting*. The difference between the BIC and AIC is that the BIC is more stringent with its penalisation of additional parameters.

**Definition 10.6.1.** Bayesian Information Criterion. If we take the likelihood function for a statistical model, which has  $k$  parameters, and  $L$  maximises the likelihood, then the *Bayesian*  $Information\ Criterion\ is\ given\ by:$ 

$$BIC = -2\log(L) + k\log(n) \tag{10.16}$$

Where  $n$  is the number of data points in the time series.

We will be using the AIC and BIC below when choosing appropriate  $ARMA(p,q)$  models.

#### $10.6.2$ $\text{Ljung-Box Test}$

The **Ljung-Box test** is a classical (in a statistical sense) hypothesis test that is designed to test whether a set of autocorrelations of a fitted time series model differ significantly from zero. The test does  $not$  test each individual lag for randomness, but rather tests the randomness over a  $\text{group of lags. Formally:}$ 

**Definition 10.6.2.** Ljung-Box Test. We define the null hypothesis  $\mathbf{H_0}$  as: The time series data at each lag are independent and identically distributed (i.i.d.), that is, the correlations between the population series values are zero.

We define the alternate hypothesis  $\mathbf{H}_{a}$  as: The time series data are not i.i.d. and possess serial correlation.

We calculate the following test statistic,  $Q$ :

$$Q = n(n+2) \sum_{k=1}^{h} \frac{\hat{\rho}_k^2}{n-k}$$
 (10.17)

Where n is the length of the time series sample,  $\hat{\rho}_k$  is the sample autocorrelation at lag k and  $h$  is the number of lags under the test.

The decision rule as to whether to reject the null hypothesis  $\mathbf{H_0}$  is to check whether  $Q > \chi^2_{\alpha,h}$ , for a chi-squared distribution with h degrees of freedom at the  $100(1-\alpha)$ th percentile.

While the details of the test may seem slightly complex we can simply use R to calculate the test for us.

Now that we have discussed the BIC and the Ljung-Box test we are ready to discuss our first mixed model-the Autoregressive Moving Average of order  $p, q, \text{ or } \text{ARMA}(p,q)$ .

#### 10.6.3 Rationale

To date we have considered autoregressive processes and moving average processes.

The former model considers its own past behaviour as inputs for the model. It attempts to capture market participant effects such as momentum and mean-reversion in stock trading. The latter model is used to characterise "shock" information to a series such as a surprise earnings announcements. A good example of "shock" news would be the BP Deepwater Horizon oil spill.

An ARMA model attempts to capture both of these aspects when modelling financial time series. Note however that it does not take into account volatility clustering, which is a key empirical phenomena of many financial time series. It is not a conditional heteroskedastic model. For that we will need to wait for the ARCH and GARCH models.

#### 10.6.4 Definition

The ARMA(p,q) model is a linear combination of two linear models and thus is still linear:

Definition 10.6.3. Autoregressive Moving Average Model of order p, q. A time series model, {xt}, is an autoregressive moving average model of order p, q, ARMA(p,q), if:

$$x_t = \alpha_1 x_{t-1} + \alpha_2 x_{t-2} + \ldots + w_t + \beta_1 w_{t-1} + \beta_2 w_{t-2} \ldots + \beta_q w_{t-q}$$
(10.18)

Where {wt} is white noise with E(wt) = 0 and variance σ 2 .

If we consider the Backward Shift Operator, B then we can rewrite the above as a function θ and φ of B:

$$\theta_p(\mathbf{B})x_t = \phi_q(\mathbf{B})w_t \tag{10.19}$$

We can straightforwardly see that by setting p 6= 0 and q = 0 we recover the AR(p) model. Similarly if we set p = 0 and q 6= 0 we recover the MA(q) model.

One of the key features of the ARMA model is that it is parsimonious and redundant in its parameters. That is, an ARMA model will often require fewer parameters than an AR(p) or MA(q) model alone. In addition if we rewrite the equation in terms of the BSO then the θ and φ polynomials can sometimes share a common factor leading to a simpler model.

### 10.6.5 Simulations and Correlograms

As with the autoregressive and moving average models we will now simulate various ARMA series and then attempt to fit ARMA models to these realisations. We carry this out because we want to ensure that we understand the fitting procedure, including how to calculate confidence intervals for the models, as well as ensure that the procedure does actually recover reasonable estimates for the original ARMA parameters.

In the previous sections we manually constructed the AR and MA series by drawing N samples from a normal distribution and then crafting the specific time series model using lags of these samples.

However, there is a more straightforward way to simulate AR, MA, ARMA and even ARIMA data, simply by using the arima.sim method in R.

We can start with the simplest possible non-trivial ARMA model–the ARMA(1,1) model. This is an autoregressive model of order one combined with a moving average model of order one. Such a model has only two coefficients, α and β, which represent the first lags of the time series itself and the "shock" white noise terms. The model is given by:

$$x_t = \alpha x_{t-1} + w_t + \beta w_{t-1} \tag{10.20}$$

We need to specify the coefficients prior to simulation. Let us take α = 0.5 and β = −0.5:

```
> set.seed(1)
> x <- arima.sim(n=1000, model=list(ar=0.5, ma=-0.5))
> plot(x)
```

The output is given in Figure [10.19.](#page-30-0)

![](_page_30_Figure_5.jpeg)

<span id="page-30-0"></span>Figure 10.19: Realisation of an ARMA(1,1) Model, with α = 0.5 and β = −0.5

Let us also plot the correlogram, as given in Figure 10.20.

> acf(x)

We can see that there is no significant autocorrelation, which is to be expected from an ARMA(1,1) model.

Finally, let us try and determine the coefficients and their standard errors using the arima function:

> arima(x, order=c(1, 0, 1))

![](_page_31_Figure_0.jpeg)

![](_page_31_Figure_1.jpeg)

Figure 10.20: Correlogram of an ARMA(1,1) Model, with α = 0.5 and β = −0.5

```
Call:
arima(x = x, order = c(1, 0, 1))
Coefficients:
         ar1 ma1 intercept
     -0.3957 0.4503 0.0538
s.e. 0.3727 0.3617 0.0337
```

sigma^2 estimated as 1.053: log likelihood = -1444.79, aic = 2897.58

We can calculate the confidence intervals for each parameter using the standard errors:

> -0.396 + c(-1.96, 1.96)\*0.373 [1] -1.12708 0.33508 > 0.450 + c(-1.96, 1.96)\*0.362 [1] -0.25952 1.15952

The confidence intervals do contain the true parameter values for both cases but we should note that the 95% confidence intervals are very wide. This is a consequence of the reasonably large standard errors.

Let us now try an ARMA(2,2) model. That is, an AR(2) model combined with a MA(2) model. We need to specify four parameters for this model: α1, α2, β<sup>1</sup> and β2. Let us take α<sup>1</sup> = 0.5, α<sup>2</sup> = −0.25 β<sup>1</sup> = 0.5 and β<sup>2</sup> = −0.3:

```
> set.seed(1)
> x <- arima.sim(n=1000, model=list(ar=c(0.5, -0.25), ma=c(0.5, -0.3)))
```

#### > plot(x)

The output of our ARMA(2,2) model is given in Figure [10.21.](#page-32-0)

![](_page_32_Figure_2.jpeg)

<span id="page-32-0"></span>Figure 10.21: Realisation of an ARMA(2,2) Model, with α<sup>1</sup> = 0.5, α<sup>2</sup> = −0.25, β<sup>1</sup> = 0.5 and β<sup>2</sup> = −0.3

And the corresponding autocorelation, as given in Figure 10.22.

> acf(x)

We can now try fitting an ARMA(2,2) model to the data:

```
> arima(x, order=c(2, 0, 2))
```

```
Call:
```

```
arima(x = x, order = c(2, 0, 2))
```

```
Coefficients:
```

|      | ar1    | ar2     | ma1    | ma2     | intercept |
|------|--------|---------|--------|---------|-----------|
|      | 0.6529 | -0.2291 | 0.3191 | -0.5522 | -0.0290   |
| s.e. | 0.0802 | 0.0346  | 0.0792 | 0.0771  | 0.0434    |

sigma^2 estimated as 1.06: log likelihood = -1449.16, aic = 2910.32

We can also calculate the confidence intervals for each parameter:

> 0.653 + c(-1.96, 1.96)\*0.0802 [1] 0.495808 0.810192 > -0.229 + c(-1.96, 1.96)\*0.0346

![](_page_33_Figure_0.jpeg)

![](_page_33_Figure_1.jpeg)

Figure 10.22: Correlogram of an ARMA(2,2) Model, with α<sup>1</sup> = 0.5, α<sup>2</sup> = −0.25, β<sup>1</sup> = 0.5 and β<sup>2</sup> = −0.3

[1] -0.296816 -0.161184 > 0.319 + c(-1.96, 1.96)\*0.0792 [1] 0.163768 0.474232 > -0.552 + c(-1.96, 1.96)\*0.0771 [1] -0.703116 -0.400884

Notice that the confidence intervals for the coefficients for the moving average component (β<sup>1</sup> and β2) do not actually contain the original parameter value. This outlines the danger of attempting to fit models to data, even when we know the true parameter values.

However for trading purposes we only need to have a predictive power that reasonably exceeds chance, producing sufficient trading revenue above transaction costs in order to be profitable in the long run.

Now that we have seen some examples of simulated ARMA models we need a mechanism for choosing the values of p and q when fitting to the models to real financial data.

### 10.6.6 Choosing the Best ARMA(p,q) Model

In order to determine which order p, q of the ARMA model is appropriate for a series, we need to use the AIC (or BIC) across a subset of values for p, q, and then apply the Ljung-Box test to determine if a good fit has been achieved, for particular values of p, q.

To show this method we are going to firstly simulate a particular ARMA(p,q) process. We will then loop over all pairwise values of p ∈ {0, 1, 2, 3, 4} and q ∈ {0, 1, 2, 3, 4} and calculate the AIC. We will select the model with the lowest AIC and then run a Ljung-Box test on the residuals to determine if we have achieved a good fit.

Let us begin by simulating an ARMA(3,2) series:

```
> set.seed(3)
```

> x <- arima.sim(n=1000, model=list(ar=c(0.5, -0.25, 0.4), ma=c(0.5, -0.3)))

We will now create an object final to store the best model fit and lowest AIC value. We loop over the various p, q combinations and use the current object to store the fit of an ARMA(i,j) model, for the looping variables i and j.

If the current AIC is less than any previously calculated AIC we set the final AIC to this current value and select that order. Upon termination of the loop we have the order of the ARMA model stored in final.order and the ARIMA(p,d,q) fit itself (with the "Integrated" d component set to 0) stored as final.arma:

```
> final.aic <- Inf
> final.order <- c(0,0,0)
> for (i in 0:4) for (j in 0:4) {
> current.aic <- AIC(arima(x, order=c(i, 0, j)))
> if (current.aic < final.aic) {
> final.aic <- current.aic
> final.order <- c(i, 0, j)
> final.arma <- arima(x, order=final.order)
> }
> }
  Let us output the AIC, order and ARIMA coefficients:
> final.aic
[1] 2863.365
> final.order
[1] 3 0 2
> final.arma
Call:
arima(x = x, order = final.order)
Coefficients:
        ar1 ar2 ar3 ma1 ma2 intercept
     0.4470 -0.2822 0.4079 0.5519 -0.2367 0.0274
s.e. 0.0867 0.0345 0.0309 0.0954 0.0905 0.0975
```

sigma^2 estimated as 1.009: log likelihood = -1424.68, aic = 2863.36

We can see that the original order of the simulated ARMA model was recovered, namely with p = 3 and q = 2. We can plot the corelogram of the residuals of the model to see if they look like a realisation of discrete white noise (DWN), as given in Figure 10.23.

> acf(resid(final.arma))

![](_page_35_Figure_1.jpeg)

Figure 10.23: Correlogram of the residuals of the best fitting ARMA(p,q) Model, p = 3 and q = 2

The corelogram does indeed look like a realisation of DWN. Finally, we perform the Ljung-Box test for 20 lags to confirm this:

```
> Box.test(resid(final.arma), lag=20, type="Ljung-Box")
```

Box-Ljung test

```
data: resid(final.arma)
X-squared = 13.1927, df = 20, p-value = 0.869
```

Notice that the p-value is greater than 0.05, which states that the residuals are independent at the 95% level and thus an ARMA(3,2) model provides a good model fit.

Clearly this should be the case since we have simulated the data ourselves. However this is precisely the procedure we will use when we come to fit ARMA(p,q) models to the S&P500 index in the following section.

### 10.6.7 Financial Data

Now that we have outlined the procedure for choosing the optimal time series model for a simulated series it is rather straightforward to apply it to financial data. For this example we are going to once again choose the S&P500 US Equity Index.

Let us download the daily closing prices using quantmod and then create the log returns stream:

```
> require(quantmod)
```

```
> getSymbols("^GSPC")
> sp = diff(log(Cl(GSPC)))
```

Let us perform the same fitting procedure as for the simulated ARMA(3,2) series above on the log returns series of the S&P500 using the AIC:

```
> spfinal.aic <- Inf
> spfinal.order <- c(0,0,0)
> for (i in 0:4) for (j in 0:4) {
> spcurrent.aic <- AIC(arima(sp, order=c(i, 0, j)))
> if (spcurrent.aic < spfinal.aic) {
> spfinal.aic <- spcurrent.aic
> spfinal.order <- c(i, 0, j)
> spfinal.arma <- arima(sp, order=spfinal.order)
> }
> }
```

The best fitting model has order ARMA(3,3):

### > spfinal.order [1] 3 0 3

Let us plot the residuals of the fitted model to the S&P500 log daily returns stream, as given in Figure [10.24:](#page-36-0)

```
> acf(resid(spfinal.arma), na.action=na.omit)
```

![](_page_36_Figure_7.jpeg)

<span id="page-36-0"></span>Figure 10.24: Correlogram of the residuals of the best fitting ARMA(p,q) Model, p = 3 and q = 3, to the S&P500 daily log returns stream

Notice that there are some significant peaks, especially at higher lags. This is indicative of a poor fit. Let us perform a Ljung-Box test to see if we have statistical evidence for this:

```
> Box.test(resid(spfinal.arma), lag=20, type="Ljung-Box")
```

Box-Ljung test

```
data: resid(spfinal.arma)
X-squared = 37.1912, df = 20, p-value = 0.0111
```

As we suspected the p-value is less than 0.05 and thus we cannot say that the residuals are a realisation of discrete white noise. Hence there is additional autocorrelation in the residuals that is not explained by the fitted ARMA(3,3) model.

# 10.7 Next Steps

As we have discussed all along in this part of the book we have seen evidence of conditional heteroskedasticity (volatility clustering) in the S&P500 series, especially in the periods around 2007-2008. When we use a GARCH model in the next chapter we will see how to eliminate these autocorrelations.

In practice, ARMA models are never generally good fits for log equities returns. We need to take into account the conditional heteroskedasticity and use a combination of ARIMA and GARCH. The next chapter will consider ARIMA and show how the "Integrated" component differs from the ARMA model we have been considering in this chapter.
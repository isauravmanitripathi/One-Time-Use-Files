## Chapter 7

# Introduction to Time Series Analysis

In this chapter methods from the field of time series analysis will be introduced. These techniques are extremely important in quantitative finance. A substantial amount of asset modelling in the financial industry continues to make extensive use of these statistical models.

We will now examine what time series analysis is, outline its scope and learn how we can apply the techniques to various frequencies of financial data in order to predict future values or infer relationships, ultimately allowing us to develop quantitative trading strategies.

### 7.1 What is Time Series Analysis?

Firstly, a time series is defined as some quantity that is measured sequentially in time over some interval.

In its broadest form, time series analysis is about inferring what has happened to a series of data points in the past and attempting to predict what will happen to it in the future.

However, we are going to take a quantitative statistical approach to time series, by assuming that our time series are realisations of sequences of random variables. That is, we are going to assume that there is some underlying generating process for our time series based on one or more statistical distributions from which these variables are drawn.

Time series analysis attempts to understand the past and predict the future.

Such a sequence of random variables is known as a discrete-time stochastic process (DTSP). In quantitative trading we are concerned with attempting to fit statistical models to these DTSPs to infer underlying relationships between series or predict future values in order to generate trading signals.

Time series in general, including those outside of the financial world, often contain the following features:

• Trends - A trend is a consistent directional movement in a time series. These trends will either be deterministic or stochastic. The former allows us to provide an underlying rationale for the trend, while the latter is a random feature of a series that we will be unlikely to explain. Trends often appear in financial series, particularly commodities prices, and many Commodity Trading Advisor (CTA) funds use sophisticated trend identification models in their trading algorithms.

- Seasonal Variation Many time series contain seasonal variation. This is particularly true in series representing business sales or climate levels. In quantitative finance we often see seasonal variation in commodities, particularly those related to growing seasons or annual temperature variation (such as natural gas).
- Serial Dependence One of the most important characteristics of time series, particularly financial series, is that of serial correlation. This occurs when time series observations that are close together in time tend to be correlated. Volatility clustering is one aspect of serial correlation that is particularly important in quantitative trading.

### 7.2 How Can We Apply Time Series Analysis in Quantitative Finance?

Our goal as quantitative researchers is to identify trends, seasonal variations and correlation using statistical time series methods, and ultimately generate trading signals or filters based on inference or predictions.

Our approach will be to:

- Forecast and Predict Future Values In order to trade successfully we will need to accurately forecast future asset prices, at least in a statistical sense.
- Simulate Series Once we identify statistical properties of financial time series we can use them to generate simulations of future scenarios. This allows us to estimate the number of trades, the expected trading costs, the expected returns profile, the technical and financial investment required in infrastructure, and thus ultimately the risk profile and profitability of a particular strategy or portfolio.
- Infer Relationships Identification of relationships between time series and other quantitative values allows us to enhance our trading signals through filtration mechanisms. For example, if we can infer how the spread in a foreign exchange pair varies with bid/ask volume, then we can filter any prospective trades that may occur in a period where we forecast a wide spread in order to reduce transaction costs.

In addition we can apply classical or Bayesian statistical tests to our time series models in order to justify certain behaviours, such as regime change in equity markets.

### 7.3 Time Series Analysis Software

In my two previous books we made exclusive use of C++ and Python for our trading strategy implementation and simulation. Both of these languages are "first class environments" for writing an entire trading infrastructure from research through to execution. They contain many libraries and allow an end-to-end construction of a trading system solely within that language.

Unfortunately, C++ and Python do not yet possess extensive statistical libraries. This is one of their shortcomings. For this reason we will be using the R statistical environment as a means of carrying out time series research. R is well-suited for the job due to the availability of time series libraries, statistical methods and straightforward plotting capabilities.

We will learn R in a problem-solving fashion, whereby new commands and syntax will be introduced as needed. Fortunately, there are plenty of extremely useful tutorials for R availabile on the internet and I will point them out as we go through the sequence of time series analysis chapters.

### 7.4 Time Series Analysis Roadmap

We have previously discussed Bayesian statistics and how it will form the basis of many of our time series and machine learning models. Eventually we will utilise Bayesian tools and machine learning techniques in conjunction with the following time series methods in order to forecast price level and direction, act as filters and determine "regime change", that is, determine when our time series have changed their underlying statistical behaviour.

Our time series roadmap is as follows. Each of the topics below will form its own chapter. Once we've examined these methods in depth, we will be in a position to create some sophisticated modern models for examining financial data across different assets.

- Time Series Introduction This chapter outlines the area of time series analysis, its scope and how it can be applied to financial data.
- Serial Correlation An absolutely fundamental aspect of modeling time series is the concept of serial correlation. We will define it, visualise it and outline how it can be used to fit time series models.
- Random Walks and White Noise In this chapter we will look at two basic time series models that will form the basis of the more complicated linear and conditional heteroskedastic models of later chapters.
- ARMA Models We will consider linear autoregressive, moving average and combined autoregressive moving average models as our first attempt at predicting asset price movements.
- ARIMA and GARCH Models We will extend the ARMA model to use differencing and thus allowing them to be "integrated", leading to the ARIMA model. We will also discuss non-stationary conditional heteroskedastic (volatility clustering) models.
- Cointegration We have considered multivariate models in Successful Algorithmic Trading, namely when we studied mean-reverting pairs of equities. In this chapter we will more rigourously define cointegration and look at further tests for it.
- State-Space Models State Space Modelling borrows from a long history of modern control theory used in engineering. It allows us to model time series with rapidly varying parameters, such as the β slope variable between two cointegrated assets in a linear regression. In particular, we will consider the famous Kalman Filter and the Hidden Markov Model. These will be two of the major uses of Bayesian analysis for time series in this book.

### 7.5 How Does This Relate to Other Statistical Tools?

My goal with QuantStart has always been to try and outline the mathematical and statistical framework for quantitative analysis and quantitative trading, from the basics through to the more advanced modern techniques.

In previous books we have spent the majority of the time on introductory and intermediate techniques. However, we are now going to turn our attention towards recent advanced techniques used in quantitative firms.

This will not only help those who wish to gain a career in the industry, but it will also give the quantitative retail traders among you a much broader toolkit of methods, as well as a unifying approach to trading.

Having worked full-time in the industry previously I can state with certainty that a substantial fraction of quantitative fund professionals use very sophisticated techniques to "hunt for alpha".

However, many of these firms are so large that they are not interested in "capacity constrained" strategies, i.e. those that aren't scalable above 1-2million USD. As retailers, if we can apply a sophisticated trading framework to these areas, coupled with a robust portfolio management system and brokerage link, we can achieve profitability over the long term.

We will eventually combine our chapters on time series analysis with the Bayesian approach to hypothesis testing and model selection, along with optimised R and Python code, to produce non-linear, non-stationary time series models-based systematic trading strategies.

The next chapter will discuss serial correlation and why it is one of the most fundamental aspects of time series analysis.
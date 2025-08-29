# Chapter 9

# Statistical Learning

The goal of the Modelling section within this book is to provide a robust quantitative framework for identifying relationships in nancial market data that can be exploited to generate protable trading strategies. The approach that will be utilised is that of Statistical Learning. This chapter describes the philosophy of statistical learning and associated techniques that can be used to create quantitative models for nancial trading.

# 9.1 What is Statistical Learning?

Before discussing the theoretical aspects of statistical learning it is appropriate to consider an example of a situation from quantitative nance where such techniques are applicable. Consider a quantitative fund that wishes to make long term predictions of the S&P500 stock market index. The fund has managed to collect a substantial amount of fundamental data associated with the companies that constitute the index. Fundamental data includes price-earnings ratio or book value, for instance. How should the fund go about using this data to make predictions of the index in order to create a trading tool? Statistical learning provides one such approach to this problem.

In a more quantitative sense we are attempting to model the behaviour of an outcome or response based on a set of predictors or features assuming a relationship between the two. In the above example the stock market index value is the response and the fundamental data associated with the constituent rms are the predictors.

This can be formalised by considering a response Y with p dierent features x1, x2, ..., xp. If we utilise vector notation then we can dene X = (x1, x2, ..., xp), which is a vector of length p. Then the model of our relationship is given by:

$$Y = f(X) + \epsilon \tag{9.1}$$

Where f is an unknown function of the predictors and represents an error or noise term. Importantly, is not dependent on the predictors and has a mean of zero. This term is included to represent information that is not considered within f. Thus we can return to the stock market index example to say that Y represents the value of the S&P500 whereas the x<sup>i</sup> components represent the values of individual fundamental factors.

The goal of statistical learning is to estimate the form of f based on the observed data and to evaluate how accurate those estimates are.

# 9.1.1 Prediction and Inference

There are two general tasks that are of interest in statistical learning - prediction and inference.

Prediction is concerned with predicting a response Y based on a newly observed predictor, X. If the model relationship has been determined then it is simple to predict the response using an estimate for f to produce an estimate for the response:

$$\hat{Y} = \hat{f}(X) \tag{9.2}$$

The functional form of f is often unimportant in a prediction scenario assuming that the estimated responses are close to the true responses and is thus accurate in its predictions. Dierent estimates of f will produce various accuracies of the estimates of Y . The error associated with having a poor estimate ˆf of f is called the reducible error. Note that there is always a degree of irreducible error because our original specication of the problem included the error term. This error term encapsulates the unmeasured factors that may aect the response Y . The approach taken is to try and minimise the reducible error with the understanding that there will always be an upper limit of accuracy based on the irreducible error.

Inference is concerned with the situation where there is a need to understand the relationship between X and Y and hence its exact form must be determined. One may wish to identify important predictors or determine the relationship between individual predictors and the response. One could also ask if the relationship is linear or non-linear. The former means the model is likely to be more interpretable but at the expense of potentially worse predictability. The latter provides models which are generally more predictive but are sometimes less interpretable. Hence a trade-o between predictability and interpretability often exists.

In this book we are less concerned with inference models since the actual form of f is not as important as its ability to make accurate predictions. Hence a large component of the Modelling section within the book will be based on predictive modelling. The next section deals with how we go about constructing an estimate ˆf for f.

# 9.1.2 Parametric and Non-Parametric Models

In a statistical learning situation it is often possible to construct a set of tuples of predictors and responses of the form {(X1, Y1),(X2, Y2), ...,(X<sup>N</sup> , Y<sup>N</sup> )}, where X<sup>j</sup> refers to the jth predictor vector and not the jth component of a particular predictor vector (that is denoted by x<sup>j</sup> ). A data set of this form is known as training data since it will be used to train a particular statistical learning method on how to generate ˆf. In order to actually estimate f we need to nd a ˆf that provides a reasonable approximation to a particular Y under a particular predictor X. There are two broad categories of statistical models that allow us to achieve this. They are known as parametric and non-parametric models.

#### Parametric Models

The dening feature of parametric methods is that they require the specication or assumption of the form of f. This is a modelling decision. The rst choice is whether to consider a linear or non-linear model. Let's consider the simpler case of a linear model. Such a model reduces the problem from estimation of some unknown function of dimension p to that of estimating a coecient vector β = (β0, β1, ..., βp) of length p + 1.

Why p + 1 and not p? Since linear models can be ane, that is they may not pass through the origin when creating a "line of best t", a coecient is required to specify the "intercept". In a one-dimensional linear model (regression) setting this is often represented as α. For our multi-dimensional linear model, where there are p predictors, we need an additional value β<sup>0</sup> to represent our intercept and hence there are p + 1 components in our βˆ estimate of β.

Now that we have specied a (linear) functional form of f we need to train it. "Training" in this instance means nding an estimate for β such that:

$$Y \approx \hat{\beta}^T X = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p \tag{9.3}$$

In the linear setting we can use an algorithm such as ordinary least squares (OLS) but other methods are available as well. It is far simpler to estimate β than t a (potentially non-linear) f. However, by choosing a parametric linear approach our estimate ˆf is unlikely to be replicating the true form of f. This can lead to poor estimates because the model is not exible enough. A potential remedy is to consider adding more parameters, by choosing alternate forms for ˆf. Unfortunately if the model becomes too exible it can lead to a very dangerous situation known as overtting, which we will discuss at length in subsequent chapters. In essence, the model follows the noise too closely and not the signal.

#### Non-Parametric Models

The alternative approach is to consider a non-parametric form of ˆf. The benet is that it can potentially t a wider range of possible forms for f and is thus more exible. Unfortunately non-parametric models suer from the need to have an extensive amount of observational data points, often far more than in a parametric settings. In addition non-parametric methods are also prone to overtting if not treated carefully, as described above.

Non-parametric models may seem like a natural choice for quantitative trading models as there is seemingly an abundance of (historical) data on which to apply the models. However, the methods are not always optimal. While the increased exibility is attractive for modelling the non-linearities in stock market data it is very easy to overt the data due to the poor signal/noise ratio found in nancial time series.

Thus a "middle-ground" of considering models with some degree of exibility is preferred. We will discuss such problems in the chapter on Optimisation later in the book.

# 9.1.3 Supervised and Unsupervised Learning

A distinction is often made in statistical machine learning between supervised and unsupervised methods. In this book we will almost exclusively be interested in supervised techniques, but unsupervised techniques are certainly applicable to nancial markets.

A supervised model requires that for each predictor vector X<sup>j</sup> there is an associated response Y<sup>j</sup> . The "supervision" of the procedure occurs when the model for f is trained or t to this particular data. For example, when tting a linear regression model, the OLS algorithm is used to train it, ultimately producing an estimate βˆ to the vector of regression coecients, β.

In an unsupervised model there is no corresponding response Y<sup>j</sup> for any particular predictor X<sup>j</sup> . Hence there is nothing to "supervise" the training of the model. This is clearly a much more challenging environment for an algorithm to produce results as there is no form of "tness function" with which to assess accuracy. Despite this setback, unsupervised techniques are extremely powerful. They are particularly useful in the realm of clustering.

A parametrised clustering model, when provided with a parameter specifying the number of clusters to identify, can often discern unanticipated relationships within data that might not otherwise have been easily determined. Such models are generally fall within the domain of business analytics and consumer marketing optimisation but they do have uses within nance, particularly in regards to assessing clustering within volatility, for instance.

This book will predominantly concentrate on supervised learning methods since there is a vast amount of historical data on which to train such models.

# 9.2 Techniques

Statistical machine learning is a vast interdisciplinary eld, with many disparate research areas. The remainder of this chapter will consider the techniques most relevant to quantitative nance and algorithmic trading in particular.

# 9.2.1 Regression

Regression refers to a broad group of supervised machine learning techniques that provide both predictive and inferential capabilities. A signicant portion of quantitative nance makes use of regression techniques and thus it is essential to be familiar with the process. Regression tries to model the relationship between a dependent variable (response) and a set of independent variables (predictors). In particular, the goal of regression is to ascertain the change in a response, when one of the independent variables changes, under the assumption that the remaining independent variables are kept xed.

The most widely known regression technique is Linear Regression, which assumes a linear relationship between the predictors and the response. Such a model leads to parameter estimates (usually denoted by the vector βˆ) for the linear response to each predictor. These parameters are estimated via a procedure known as ordinary least squares (OLS). Linear regression can be used both for prediction and inference.

In the former case a new value of the predictor can be added (without a corresponding response) in order to predict a new response value. For instance, consider a linear regression model used to predict the value of the S&P500 in the following day, from price data over the last ve days. The model can be tted using OLS across historical data. Then, when new market data arrive for the S&P500 it can be input into the model (as a predictor) to generate a predicted response for tomorrow's daily price. This can form the basis of a simplistic trading strategy.

In the latter case (inference) the strength of the relationship between the response and each predictor can be assessed in order to determine the subset of predictors that have an eect on the response. This is more useful when the goal is to understand why the response varies, such as in a marketing study or clinical trial. Inference is often less useful to those carrying out algorithmic trading, as the quality of the prediction is fundamentally more important than the underlying relationship. That being said, one should not solely rely on the "black box" approach due to the prevalence of over-tting to noise in the data.

Other techniques include Logistic Regression, which is designed to predict a categorical response (such as "UP", "DOWN", "FLAT") as opposed to a continuous response (such as a stock market price). This technically makes it a classication tool (see below), but it is usually grouped under the banner of regression. A general statistical procedure known as Maximum Likelihood Estimation (MLE) is used to estimate the parameter values of a logistic regression.

# 9.2.2 Classication

Classication encompasses supervised machine learning techniques that aim to classify an observation (similar to a predictor) into a set of pre-dened categories, based on features associated with the observation. These categories can be un-ordered, e.g. "red", "yellow", "blue" or ordered, e.g. "low", "medium", "high". In the latter case such categorical groups are known as ordinals. Classication algorithms - classiers - are widely used in quantitative nance, especially in the realm of market direction prediction. In this book we will be studying classiers extensively.

Classiers can be utilised in algorithmic trading to predict whether a particular time series will have positive or negative returns in subsequent (unknown) time periods. This is similar to a regression setting except that the actual value of the time series is not being predicted, rather its direction. Once again we are able to use continuous predictors, such as prior market prices as observations. We will consider both linear and non-linear classiers, including Logistic Regression, Linear/Quadratic Discriminant Analysis, Support Vector Machines (SVM) and Articial Neural Networks (ANN). Note that some of the previous methods can actually be used in a regression setting also.

# 9.2.3 Time Series Models

A key component in algorithmic trading is the treatment and prediction of nancial time series. Our goal is generally to predict future values of time series based on prior values or external factors. Thus time series modelling can be seen as a mixed-subset of regression and classication. Time series models dier from non-temporal models because the models make deliberate use of the temporal ordering of the series. Thus the predictors are often based on past or current values, while the responses are often future values to be predicted.

There is a large literature on diering time series models. There are two broad families of time series models that interest us in algorithmic trading. The rst set are the linear autoregressive integrated moving average (ARIMA) family of models, which are used to model the variations in the absolute value of a time series. The other family of time series are the autoregressive conditional heteroskedasticity (ARCH) models, which are used to model the variance (i.e. the volatility) of time series over time. ARCH models use previous values (volatilities) of the time series to predict future values (volatilities). This is in contrast to stochastic volatility models, which utilise more than one stochastic time series (i.e. multiple stochastic dierential equations) to model volatility.

All of the raw historical price time series are discrete in that they contain nite values. In the eld of quantitative nance it is common to study continuous time series models. In particular, the famous Geometric Brownian Motion, the Heston Stochastic Volatility model and the Ornstein-Uhlenbeck model all represent continuous time series with diering forms of stochastic behaviour. We will utilise these time series models in subsequent chapters to attempt to characterise the behaviour of nancial time series in order to exploit their properties to create viable trading strategies.
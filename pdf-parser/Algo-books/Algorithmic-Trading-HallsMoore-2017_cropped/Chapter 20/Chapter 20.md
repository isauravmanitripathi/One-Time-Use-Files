# Chapter 20

# Model Selection and Cross-Validation

In this chapter I want to discuss one of the most important and tricky issues in machine learning, that of model selection and the bias-variance tradeoff. The latter is one of the most crucial issues in helping us achieve profitable trading strategies based on machine learning techniques.

Model selection refers to our ability to assess performance of differing machine learning models in order to choose the best one.

The bias-variance tradeoff is a particular property of all (supervised) machine learning models that enforces a tradeoff between how "flexible" the model is and how well it performs on new, unseen data. The latter is known as a models generalisation performance.

# 20.1 Bias-Variance Trade-Off

We will begin by understanding why model selection is important and then discuss the biasvariance tradeoff qualitatively. We will wrap up the chapter by deriving the bias-variance tradeoff mathematically and discuss measures to minimise the problems it introduces.

In this chapter we are considering supervised regression models. That is, models which are trained on a set of labelled training data and produce a quantitative response. An example of this would be attempting to predict future stock prices based on other factors such as past prices, interest rates or foreign exchange rates.

This is in contrast to a categorical or binary response model as in the case of supervised classification. An example of classification would be attempting to assign a topic to a text document from a finite set of topics, as was discussed in the previous chapter on support vector machines. The bias-variance tradeoff and model selection situations for classification are extremely similar to the regression setting and simply require modification to handle the differing ways in which errors and performance are measured.

### 20.1.1 Machine Learning Models

As with most of our discussions in machine learning the basic model is given by the following:

$$y = f(\mathbf{x}) + \epsilon \tag{20.1}$$

This states that the response vector y is given as a function f of the predictor vector x with a set of normally distributed error terms, which are often assumed to have mean zero and a standard deviation of one.

What does this mean in practice?

As an example the vector x could represent a set of lagged financial prices. This is similar to the time series autoregressive models we considered earlier in the book. It could also represent interest rates, derivatives prices, real-estate prices, word-frequencies in a document or any other factor that we consider useful in making a prediction.

The vector y could be single or multi-valued. In the former case it might simply represent tomorrow's stock price, in the latter case it might represent the next week's daily predicted prices.

f represents our view on the underlying relationship between y and x. This could be linear, in which case we may estimate f via a linear regression model. It may be non-linear, in which case we may estimate f with a SVM or a spline-based method, for instance.

The error terms represent all of the factors affecting y that we have not taken into account with our function f. They are essentially the "unknown" components of our prediction model. It is commmon to assume that these are normally distributed with mean zero and a standard deviation of one, although other distributions can be used.

In this section we are going to describe how to measure the performance of an estimate for the unknown function f. Such an estimate uses "hat" notation. Hence, ˆf can be read as "the estimate of f".

In addition we will describe the effect on the performance of the model as we increase its flexibility. Flexibility describes the degrees of freedom available to the model to "fit" to the training data. We will see that the relationship between flexibility and performance error is non-linear. Thus we need to be extremely careful when choosing the "best" model.

Note that there is never a "best" model across the entirety of statistics, time series or machine learning. Different models have varying strengths and weaknesses. One model may work very well on one dataset, but may perform badly on another. The challenge in statistical machine learning is to pick the "best" model for the problem at hand with the data available.

In fact this notion of there being no "best" model in supervised learning situations is formally encapsulated in what is known as the "No Free Lunch" Theorem.

#### 20.1.2 Model Selection

When trying to ascertain which statistical machine learning method is best for a particular situation we need a means of characterising the relative performance between models. In the time series section we considered the Akaike Information Criterion and the Bayesian Information Criterion. In this section we will consider other methods.

To determine model suitability we need to compare the known values of the underlying relationship with those that are predicted by an estimated model.

For instance, if we are attempting to predict tomorrow's stock prices, then we wish to evaluate how close our models predictions are to the true value on that particular day.

This motivates the concept of a loss function, which quantitatively compares the difference between the true values with the predicted values.

Assume that we have created an estimate ˆf of the underlying relationship f. ˆf might be a linear regression or a Random Forest model, for instance. ˆf will have been trained on a particular data set, τ , which contains predictor-response pairs. If there are n such pairs then τ is given by:

$$\tau = \{(\mathbf{x}_1, y_1), ..., (\mathbf{x}_n, y_n)\}\tag{20.2}$$

The x<sup>i</sup> represent the prediction factors, which could be prior lagged prices for a series or some other factors, as mentioned above. The y<sup>i</sup> could be the predictions for our stock prices in the following period. In this instance, n represents the number of days of data that we have available.

The loss function is denoted by L(y, ˆf(x)). Its job is to compare the predictions made by ˆf at particular values of x to their true values given by y. A common choice for L is the absolute error :

$$L(y, \hat{f}(\mathbf{x})) = |y - \hat{f}(\mathbf{x})| \tag{20.3}$$

Another popular choice is the squared error :

$$L(y, \hat{f}(\mathbf{x})) = (y - \hat{f}(\mathbf{x}))^2 \tag{20.4}$$

Note that both choices of loss function are non-negative. Hence the "best" loss for a model is zero, that is, there is no difference between the prediction and the true value.

#### Training Error versus Test Error

Now that we have a loss function we need some way of aggregating the various differences between the true values and the predicted values. One way to do this is to define the Mean Squared Error (MSE), which is simply the average, or expectation value, of the squared loss:

$$MSE := \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{f}(\mathbf{x}_i))^2$$
 (20.5)

The definition simply states that the Mean Squared Error is the average of all of the squared differences between the true values y<sup>i</sup> and the predicted values ˆf(xi). A smaller MSE means that the estimate is more accurate.

It is important to realise that this MSE value is computed using only the training data. That is, it is computed using only the data that the model was fitted on. Hence, it is actually known as the training MSE.

In practice this value is of little interest to us. What we are really concerned about is how well the model can predict values on new unseen data.

For instance, we are not really interested in how well the model can predict past stock prices of

the following day, we are only concerned with how it can predict the following days stock prices going forward. This quantification of a models performance is known as its generalisation performance.

Mathematically if we have a new prediction value x<sup>0</sup> and a true response y0, then we wish to take the expectation across all such new values to come up with the test MSE:

$$\text{Test MSE} := \mathbb{E}\left[ (y_0 - \hat{f}(\mathbf{x}_0))^2 \right] \tag{20.6}$$

Where the expectation is taken across all new unseen predictor-response pairs (x0, y0).

Our goal is to select the model where the test MSE is lowest across choices of other models. Unfortunately it is difficult to calculate the test MSE. This is because we are often in a situation where we do not have any test data available.

In general machine learning domains this can be quite common. In quantitative trading we are (usually) in a "data rich" environment and thus we can retain some of our data for training and some for testing. In the next section we will discuss cross-validation, which is one means of utilising subsets of the training data in order to estimate the test MSE.

A pertinent question to ask at this stage is "Why can we not simply use the model with the lowest training MSE?". The simple answer is that there is no guarantee that the model with the lowest training MSE will also be the model with the lowest test MSE. Why is this so? The answer lies in a particular property of supervised machine learning methods known as the bias-variance tradeoff.

#### 20.1.3 The Bias-Variance Tradeoff

Consider a slightly contrived example situation where we know the underlying "true" relationship between y and x = x, which is given by a sinusoidal function, f = sin, such that y = f(x) = sin(x). Note that in reality we will not ever know the underlying f, which is why we are estimating it in the first place!

For this situation I have created a set of training points, τ , given by y<sup>i</sup> = sin(xi) + <sup>i</sup> , where <sup>i</sup> are draws from a standard normal distribution (mean of zero, standard deviation equal to one). This can be seen in Figure 20.1. The black curve is the "true" function f, restricted to the interval [0, 2π], while the circled points represent the y<sup>i</sup> simulated data values.

We can now try to fit a few different models to this training data. The first model, given by the green line, is a linear regression fitted with ordinary least squares estimation. The second model, given by the blue line, is a polynomial model with degree m = 3. The third model, given by the red curve is a higher degree polynomial with degree m = 20. Between each of the models I have varied the flexibility, that is, the degrees of freedom (DoF). The linear model is the least flexible with only two DoF. The most flexible model is the polynomial of order m = 20. It can be seen that the polynomial of order m = 3 is the apparent closest fit to the underlying sinusoidal relationship.

For each of these models we can calculate the training MSE. It can be seen in Figure 20.2 that the training MSE (given by the green curve) decreases monotonically as the flexibility of the model increases. This makes sense since polynomials of increasing degree are as flexible as we need them to be in order to minimise the difference between their values and those of the sinusoidal data.

![](_page_4_Figure_0.jpeg)

Figure 20.1: Various estimates of the underlying sinusoidal model, f = sin

![](_page_4_Figure_2.jpeg)

Figure 20.2: Training MSE and Test MSE as a function of model flexibility.

However if we plot the test MSE, which is given by the blue curve, the situation is quite different. The test MSE initially decreases as we increase the flexibility of the model but eventually starts to increase again after we introduce more flexibility. Why is this? By increasing the model flexibility we are letting it fit to unique "patterns" in the training data.

However as soon as we introduce new test data the model cannot generalise well because these "patterns" are only random artifacts of the training data and are not an underlying property of the true sinusoidal form. We are in a situation of overfitting. Colloquially, the model is fitting itself to the noise and not the signal.

In fact this property of a "u-shaped" test MSE as a function of model flexibility is an intrinsic property of supervised machine learning models known as the bias-variance tradeoff.

It can be shown (see below in the Mathematical Explanation section) that the expected test MSE, where the expectation is taken across many test sets, is given by:

$$\mathbb{E}(y_0 - \hat{f}(\mathbf{x}_0))^2 = \text{Var}(\hat{f}(\mathbf{x}_0)) + \left[\text{Bias}\hat{f}(\mathbf{x}_0)\right]^2 + \text{Var}(\epsilon) \tag{20.7}$$

The first term on the right hand side is the variance of the estimate across many testing sets. It determines how much the average model estimation deviates as different testing data are used. In particular a model with high variance is suggestive that it is overfit to the training data.

The middle term is the squared bias, which characterises the difference between the averages of the estimate and the true values. A model with high bias is not capturing the underlying behaviour of the true functional form well. One can imagine the situation where a linear regression is used to model a sine curve (as above). No matter how well "fit" to the data the model is, it will never capture the non-linearity inherant in a sine curve.

The final term is known as the irreducible error. It is the minimum lower bound for the test MSE. Since we only ever have access to the training data points (including the randomness associated with the values) we cannot ever hope to get a "more accurate" fit than what the variance of the residuals offer.

Generally as flexibility increases we see an increase in variance and a decrease in bias. However it is the relative rate of change between these two factors that determines whether the expected test MSE increases or decreases.

As flexibility is increased the bias will tend to drop quickly (faster than the variance can increase) and so we see a drop in test MSE. However, as flexibility increases further, there is less reduction in bias (because the flexibility of the model can fit the training data easily) and instead the variance rapidly increases, due to the model being overfit.

Our ultimate goal in supervised machine learning is to try and minimise the expected test MSE, that is we must choose a supervised machine learning model that simultaneously has low variance and low bias.

If you wish to gain a more mathematically precise definition of the bias-variance tradeoff then you can read the following section, otherwise it may be skipped.

#### A More Mathematical Explanation

We have now qualitatively outlined the issues surrounding model flexibility, bias and variance. In this section we are going to carry out a mathematical decomposition of the expected prediction error for a particular model estimate, ˆf(x) with prediction vector x = x<sup>0</sup> using the squared-error loss:

The definition of the squared error loss, at the prediction point x0, is given by:

$$Err(\mathbf{x}_0) = \mathbb{E}\left[\left(y_0 - \hat{f}(\mathbf{x}_0)\right)^2 \mid \mathbf{x} = \mathbf{x}_0\right]$$
 (20.8)

However we can expand the expectation on the right hand side into three terms:

$$\operatorname{Err}(\mathbf{x}_0) = \sigma_{\epsilon}^2 + \left[ \mathbb{E}\hat{f}(\mathbf{x}_0) - f(\mathbf{x}_0) \right]^2 + \mathbb{E} \left[ \hat{f}(\mathbf{x}_0) - \mathbb{E}\hat{f}(\mathbf{x}_0) \right]^2 \tag{20.9}$$

The first term on the RHS is known as the irreducible error. It is the lower bound on the possible expected prediction error.

The middle term is the squared bias and represents the difference in the average value of all predictions at x0, across all possible testing sets, and the true mean value of the underlying function at x0.

This can be thought of as the error introduced by the model in not representing the underlying behaviour of the true function. For example, using a linear model when the phenomena is inherently non-linear.

The third term is known as the variance. It characterises the error that is introduced as the model becomes more flexible, and thus more sensitive to variation across differing training sets, τ .

$$Err(\mathbf{x}_0) = \sigma_{\epsilon}^2 + \text{Bias}^2 + \text{Var}(\hat{f}(\mathbf{x}_0))$$
(20.10)

= Irreducible Error + Bias<sup>2</sup> + Variance (20.11)

It is important to remember that σ 2 represents an absolute lower bound on the expected prediction error. While the expected training error can be reduced monotonically to zero (just by increasing model flexibility), the expected prediction error will always be at least the irreducible error, even if the squared bias and variance are both zero.

# 20.2 Cross-Validation

In this section we will attempt to find a partial remedy to the problem of an overfit machine learning model using a technique known as cross-validation.

Firstly, we will define cross-validation and then describe how it works. Secondly, we will construct a forecasting model using an equity index and then apply two cross-validation methods to this example: the validation set approach and k-fold cross-validation. Finally we will discuss the code for the simulations using Python with Pandas, Matplotlib and Scikit-Learn.

Our goal is to eventually create a set of statistical tools that can be used within a backtesting framework to help us minimise the problem of overfitting a model and thus constrain future losses due to a poorly performing strategy based on such a model.

### 20.2.1 Overview of Cross-Validation

Recall from the section above the definitions of test error and flexibility:

- Test Error The average error, where the average is across many observations, associated with the predictive performance of a particular statistical model when assessed on new observations that were not used to train the model.
- Flexibility The degrees of freedom available to the model to "fit" to the training data. A linear regression is very inflexible (it only has two degrees of freedom) whereas a high-degree polynomial is very flexible (and as such can have many degrees of freedom).

With these concepts in mind we can now define cross-validation.

The goal of cross-validation is to estimate the test error associated with a statistical model or select the appropriate level of flexibility for a particular statistical method.

Recall that the training error associated with a model can vastly underestimate the test error of the model. Cross-validation provides us with the capability to more accurately estimate the test error, which we will never know in practice.

Cross-validation works by "holding out" particular subsets of the training set in order to use them as test observations. In this section we will discuss the various ways in which such subsets are held out. In addition we will implement the methods using Python on an example forecasting model based on prior historical data.

#### 20.2.2 Forecasting Example

In order to make the following theoretical discussion concrete we will consider the development of a new trading strategy based on the prediction of price levels of Amazon, Inc. Equally we could pick the S&P500 index, as in the time series sections, or any other asset with pricing data.

For this approach we will simply consider the closing price of the historical daily Open-High-Low-Close (OHLC) bars as predictors and the following day's closing price as the response. Hence we are attempting to predict tomorrow's price using daily historic prices. This is similar to an autoregressive model from the time series section except that we will use both a linear regression and a non-linear polynomial regression as our machine learning models.

An observation will consist of a pair, x<sup>i</sup> and y<sup>i</sup> , which contain the predictor values and the response value respectively. If we consider a daily lag of p days, then x<sup>i</sup> has p components. Each of these components represents the closing price from one day further behind. x<sup>p</sup> represents today's closing price (known), while xp−<sup>1</sup> represents the closing price yesterday, while x<sup>1</sup> represents the price p − 1 days ago.

y<sup>i</sup> contains only a single value, namely tomorrow's closing price, and is thus a scalar. Hence each observation is a tuple (x<sup>i</sup> , yi). We will consider a set of n observations corresponding to n days worth of historical pricing information for Amazon (see Fig 20.3).

Our goal is to find a statistical model that attempts to predict the price level of Amazon based on the previous days prices. If we were to achieve an accurate prediction, we could use it to generate basic trading signals.

We will use cross-validation in two ways: Firstly to estimate the test error of particular statistical learning methods (i.e. their separate predictive performance), and secondly to select the optimal flexibility of the chosen method in order to minimise the errors associated with bias and variance.

![](_page_8_Figure_1.jpeg)

Figure 20.3: Amazon, Inc. - Price History

We will now outline the differing ways of carrying out cross-validation, starting with the validation set approach and then finally k-fold cross validation. In each case we will use Pandas and Scikit-Learn to implement these methods.

#### 20.2.3 Validation Set Approach

The validation set approach to cross-validation is very simple to carry out. Essentially we take the set of observations (n days of data) and randomly divide them into two equal halves. One half is known as the training set while the second half is known as the validation set. The model is fit using only the data in the training set, while its test error is estimated using only the validation set.

This is easily recognisable as a technique often used in quantitative trading as a mechanism for assessing predictive performance. However, it is more common to find two-thirds of the data used for the training set, while the remaining third is used for validation. In addition it is more common to retain the ordering of the time series such that the first two-thirds chronologically represents the first two-thirds of the historical data.

What is less common when applying this method is randomising the observations into each of the two separate sets. Even less common is a discussion as to the subtle problems that arise when this is carried out.

Firstly, and especially in situations with limited data, the procedure can lead to a high variance for the estimate of the test error due to the randomisation of the samples. This is a typical "gotcha" when carrying out the validation set approach to cross-validation. It is all too possible to achieve a low test error simply through blind luck on receiving an appropriate random sample split. Hence the true test error (i.e. predictive power) can be significantly underestimated.

Secondly, note that in the 50-50 split of testing/training data we are leaving out half of all observations. Hence we are reducing information that would otherwise be used to train the model. Thus it is likely to perform worse than if we had used all of the observations, including those in the validation set. This leads to a situation where we may actually overestimate the test error for the full data set.

Thirdly, time series data (especially in quantitative finance) possesses a degree of serial correlation. This means that each observation is not independent and identically distributed (iid). Thus the process of randomly assigning various observations to separate samples is not strictly valid and will introduce its own error, which must be considered.

In order to reduce the impact of these issues we will consider a more sophisticated splitting of the data known as k-fold cross validation.

#### 20.2.4 k-Fold Cross Validation

K-fold cross-validation improves upon the validation set approach by dividing the n observations into k mutually exclusive, and approximately equally sized subsets known as "folds".

The first fold becomes a validation set, while the remaining k − 1 folds (aggregated together) become the training set. The model is fit on the training set and its test error is estimated on the validation set. This procedure is repeated k times, with each repetition holding out a fold as the validation set, while the remaining k − 1 are used for training.

This allows an overall test estimate, CVk, to be calculated that is an average of all the individual mean-squared errors, MSE<sup>i</sup> , for each fold:

$$CV_k = \frac{1}{k} \sum_{i=1}^{k} MSE_i$$
 (20.12)

The obvious question that arises at this stage is what value do we choose for k? The short answer (based on empirical studies) is to choose k = 5 or k = 10. The longer answer to this question relates to both computational expense and the bias-variance tradeoff.

#### Leave-One-Out Cross Validation

We can actually choose k = n, which means that we fit the model n times, with only a single observation left out for each fitting. This is known as leave-one-out cross-validation (LOOCV). It can be very computationally expensive, particularly if n is large and the model has an expensive fitting procedure, as fitting must be repeated n times.

While LOOCV is beneficial in reducing bias, due to the fact that nearly all of the samples are used for fitting in each case, it actually suffers from the problem of high variance. This is because we are calculating the test error on a single response each time for each observation in the data set.

k-fold cross-validation reduces the variance at the expense of introducing some more bias, due to the fact that some of the observations are not used for training. With k = 5 or k = 10 the bias-variance tradeoff is generally optimised.

# 20.2.5 Python Implementation

We are quite lucky when working with Python and its library ecosystem as much of the "heavy lifting" is done for us. Using Pandas, Scikit-Learn and Matplotlib, we can rapidly create some examples to show the usage and issues surrounding cross-validation.

#### Obtaining the Data

The first task is to obtain the data and put it in a format we can use. I have actually carried out this procedure in my previous book Successful Algorithmic Trading but I would like to have this section as self-contained as possible. Hence you can use the following code to obtain historical data from any financial time series available on Yahoo Finance, as well as their associated daily predictor lag values:

```
from __future__ import print_function
import datetime
import pprint
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import sklearn
def create_lagged_series(symbol, start_date, end_date, lags=5):
    """
    This creates a pandas DataFrame that stores
    the percentage returns of the adjusted closing
    value of a stock obtained from Yahoo Finance,
    along with a number of lagged returns from the
    prior trading days (lags defaults to 5 days).
    Trading volume, as well as the Direction from
    the previous day, are also included.
    """
    # Obtain stock information from Yahoo Finance
    ts = web.DataReader(
        symbol,
        "yahoo",
        start_date - datetime.timedelta(days=365),
        end_date
    )
    # Create the new lagged DataFrame
    tslag = pd.DataFrame(index=ts.index)
    tslag["Today"] = ts["Adj Close"]
```

```
tslag["Volume"] = ts["Volume"]
# Create the shifted lag series of
# prior trading period close values
for i in range(0,lags):
    tslag["Lag%s" % str(i+1)] = ts["Adj Close"].shift(i+1)
# Create the returns DataFrame
tsret = pd.DataFrame(index=tslag.index)
tsret["Volume"] = tslag["Volume"]
tsret["Today"] = tslag["Today"].pct_change()*100.0
# If any of the values of percentage
# returns equal zero, set them to
# a small number (stops issues with
# QDA model in scikit-learn)
for i,x in enumerate(tsret["Today"]):
    if (abs(x) < 0.0001):
        tsret["Today"][i] = 0.0001
# Create the lagged percentage returns columns
for i in range(0,lags):
    tsret["Lag%s" % str(i+1)] = tslag[
        "Lag%s" % str(i+1)
    ].pct_change()*100.0
# Create the "Direction" column
# (+1 or -1) indicating an up/down day
tsret["Direction"] = np.sign(tsret["Today"])
tsret = tsret[tsret.index >= start_date]
return tsret
```

Note that we are not storing the direct close price values in the "Today" or "Lag" columns. Instead we are storing the close-to-close percentage return from the previous day.

We need to obtain the data for Amazon daily prices along some suitable time frame. I have chosen Jan 1st 2004 to Oct 27th 2016. However this is an arbitrary choice. You can adjust the time frame as you see fit. To obtain the data and place it into a Pandas DataFrame called lags we can use the following code:

```
if __name__ == "__main__":
    symbol = "AMZN"
    start_date = datetime.datetime(2004, 1, 1)
    end_date = datetime.datetime(2016, 10, 27)
    lags = create_lagged_series(
        symbol, start_date, end_date, lags=10
    )
```

At this stage we have the necessary data to begin creating a set of statistical machine learning models.

#### Validation Set Approach

..

Now that we have the financial data we need to create a set of predictive regression models we can use the above cross-validation methods to obtain estimates for the test error.

The first task is to import the models from Scikit-Learn. We will choose a linear regression model with polynomial features. This provides us with the ability to choose varying degrees of flexibility simply by increasing the degree of the features' polynomial order. Initially we are going to consider the validation set approach to cross validation.

Scikit-Learn provides a validation set approach via the train\_test\_split method found in the cross\_validation module. We will also need to import the KFold method for k-fold cross validation later, as well as the linear regression model itself. We need to import the MSE calculation as well as Pipeline and PolynomialFeatures. The latter two allow us to easily create a set of polynomial feature linear regression models with minimal additional coding:

```
..
from sklearn.cross_validation import train_test_split, KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
..
```

Once the modules are imported we can create a Pandas DataFrame that uses ten of the prior lagging days of Amazon returns as predictors. We can then create ten separate random splittings of the data into a training and validation set.

Finally, for multiple degrees of the polynomial features of the linear regression, we can calculate the test error. This provides us with ten separate test error curves, each value of which shows the test MSE for a differing degree of polynomial kernel:

```
..
def validation_set_poly(random_seeds, degrees, X, y):
    """
    Use the train_test_split method to create a
    training set and a validation set (50% in each)
    using "random_seeds" separate random samplings over
    linear regression models of varying flexibility
    """
    sample_dict = dict(
        [("seed_%s" % i,[]) for i in range(1, random_seeds+1)]
    )
    # Loop over each random splitting into a train-test split
    for i in range(1, random_seeds+1):
        print("Random: %s" % i)
```

```
# Increase degree of linear
    # regression polynomial order
    for d in range(1, degrees+1):
        print("Degree: %s" % d)
        # Create the model, split the sets and fit it
        polynomial_features = PolynomialFeatures(
            degree=d, include_bias=False
        )
        linear_regression = LinearRegression()
        model = Pipeline([
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression)
        ])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.5, random_state=i
        )
        model.fit(X_train, y_train)
        # Calculate the test MSE and append to the
        # dictionary of all test curves
        y_pred = model.predict(X_test)
        test_mse = mean_squared_error(y_test, y_pred)
        sample_dict["seed_%s" % i].append(test_mse)
    # Convert these lists into numpy
    # arrays to perform averaging
    sample_dict["seed_%s" % i] = np.array(
        sample_dict["seed_%s" % i]
    )
# Create the "average test MSE" series by averaging the
# test MSE for each degree of the linear regression model,
# across all random samples
sample_dict["avg"] = np.zeros(degrees)
for i in range(1, random_seeds+1):
    sample_dict["avg"] += sample_dict["seed_%s" % i]
sample_dict["avg"] /= float(random_seeds)
return sample_dict
```

We can use Matplotlib to plot this data. We need to import pylab and then create a function to plot the test error curves:

.. ..

```
..
import pylab as plt
..
..
def plot_test_error_curves_vs(sample_dict, random_seeds, degrees):
    fig, ax = plt.subplots()
    ds = range(1, degrees+1)
    for i in range(1, random_seeds+1):
        ax.plot(
            ds,
            sample_dict["seed_%s" % i],
            lw=2,
            label='Test MSE - Sample %s' % i
        )
    ax.plot(
        ds,
        sample_dict["avg"],
        linestyle='--',
        color="black",
        lw=3,
        label='Avg Test MSE'
    )
    ax.legend(loc=0)
    ax.set_xlabel('Degree of Polynomial Fit')
    ax.set_ylabel('Mean Squared Error')
    fig.set_facecolor('white')
    plt.show()
..
..
```

We have selected the degree of our polynomial features to vary between d = 1 to d = 3, thus providing us with up to cubic order in our features. Figure 20.4 displays the ten different random splittings of the training and testing data along with the average test MSE (the black dashed line).

It is immediately apparent how much variation there is across different random splits into a training and validation set. Since it is not easy to obtain a predictive signal in using previous days historical close prices of Amazon, we see that as the degree of the polynomial features increases the test MSE increases as well.

In addition it is clear that the validation set suffers from high variance. In order to minimise this issue we will now implement k-fold cross-validation on the same Amazon dataset.

#### 20.2.6 k-Fold Cross Validation

Since we have already taken care of the imports above, I will simply outline the new functions for carrying out k-fold cross-validation. They are almost identical to the functions used for the

![](_page_15_Figure_0.jpeg)

Figure 20.4: Test MSE curves for multiple training-validation splits for a linear regression with polynomial features of increasing degree

training-test split. However, we need to use the KFold object to iterate over k "folds".

In particular the KFold object provides an iterator that allows us to correctly index the samples in the data set and create separate training/test folds. I have chosen k = 10 for this example.

As with the validation set approach we create a pipeline of polynomial feature transformations and then apply a linear regression model. We then calculate the test MSE and construct separate test MSE curves for each fold. Finally we create an average MSE curve across folds:

```
..
..
def k_fold_cross_val_poly(folds, degrees, X, y):
    """
    Use the k-fold cross validation method to create
    k separate training test splits over linear
    regression models of varying flexibility
    """
    # Create the KFold object and
    # set the initial fold to zero
    n = len(X)
    kf = KFold(n, n_folds=folds)
    kf_dict = dict(
        [("fold_%s" % i,[]) for i in range(1, folds+1)]
    )
```

```
# Loop over the k-folds
for train_index, test_index in kf:
    fold += 1
    print("Fold: %s" % fold)
    X_train, X_test = X.ix[train_index], X.ix[test_index]
    y_train, y_test = y.ix[train_index], y.ix[test_index]
    # Increase degree of linear regression polynomial order
    for d in range(1, degrees+1):
        print("Degree: %s" % d)
        # Create the model and fit it
        polynomial_features = PolynomialFeatures(
            degree=d, include_bias=False
        )
        linear_regression = LinearRegression()
        model = Pipeline([
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression)
        ])
        model.fit(X_train, y_train)
        # Calculate the test MSE and append to the
        # dictionary of all test curves
        y_pred = model.predict(X_test)
        test_mse = mean_squared_error(y_test, y_pred)
        kf_dict["fold_%s" % fold].append(test_mse)
    # Convert these lists into numpy
    # arrays to perform averaging
    kf_dict["fold_%s" % fold] = np.array(
        kf_dict["fold_%s" % fold]
    )
# Create the "average test MSE" series by averaging the
# test MSE for each degree of the linear regression model,
# across each of the k folds.
kf_dict["avg"] = np.zeros(degrees)
for i in range(1, folds+1):
    kf_dict["avg"] += kf_dict["fold_%s" % i]
kf_dict["avg"] /= float(folds)
return kf_dict
```

fold = 0

..

We can plot these curves with the following function:

```
..
..
def plot_test_error_curves_kf(kf_dict, folds, degrees):
    fig, ax = plt.subplots()
    ds = range(1, degrees+1)
    for i in range(1, folds+1):
        ax.plot(
            ds,
            kf_dict["fold_%s" % i],
            lw=2,
            label='Test MSE - Fold %s' % i
        )
    ax.plot(
        ds,
        kf_dict["avg"],
        linestyle='--',
        color="black",
        lw=3,
        label='Avg Test MSE'
    )
    ax.legend(loc=0)
    ax.set_xlabel('Degree of Polynomial Fit')
    ax.set_ylabel('Mean Squared Error')
    fig.set_facecolor('white')
    plt.show()
..
```

..

..

The output is given in Figure 20.5.

Notice that the variation among the error curves is much lower than for the validation set approach (even accounting for the high value of Fold 4). This is the desired effect of carrying out cross-validation.

Cross-validation generally provides a much better estimate of the true test MSE, at the expense of some slight bias. This is usually an acceptable trade-off in machine learning applications.

## 20.2.7 Full Python Code

The full Python code for cross\_validation.py is given below:

```
# cross_validation.py
```

**from** \_\_future\_\_ **import** print\_function

![](_page_18_Figure_0.jpeg)

Figure 20.5: Test MSE curves for multiple k-fold cross-validation folds for a Linear Regression with polynomial features of increasing degree

```
import datetime
import pprint
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import pylab as plt
import sklearn
from sklearn.cross_validation import train_test_split, KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
def create_lagged_series(symbol, start_date, end_date, lags=5):
    """
    This creates a pandas DataFrame that stores
    the percentage returns of the adjusted closing
    value of a stock obtained from Yahoo Finance,
    along with a number of lagged returns from the
    prior trading days (lags defaults to 5 days).
```

```
Trading volume, as well as the Direction from
the previous day, are also included.
"""
# Obtain stock information from Yahoo Finance
ts = web.DataReader(
    symbol,
    "yahoo",
    start_date - datetime.timedelta(days=365),
    end_date
)
# Create the new lagged DataFrame
tslag = pd.DataFrame(index=ts.index)
tslag["Today"] = ts["Adj Close"]
tslag["Volume"] = ts["Volume"]
# Create the shifted lag series of
# prior trading period close values
for i in range(0,lags):
    tslag["Lag%s" % str(i+1)] = ts["Adj Close"].shift(i+1)
# Create the returns DataFrame
tsret = pd.DataFrame(index=tslag.index)
tsret["Volume"] = tslag["Volume"]
tsret["Today"] = tslag["Today"].pct_change()*100.0
# If any of the values of percentage
# returns equal zero, set them to
# a small number (stops issues with
# QDA model in scikit-learn)
for i,x in enumerate(tsret["Today"]):
    if (abs(x) < 0.0001):
        tsret["Today"][i] = 0.0001
# Create the lagged percentage returns columns
for i in range(0,lags):
    tsret["Lag%s" % str(i+1)] = tslag[
        "Lag%s" % str(i+1)
    ].pct_change()*100.0
# Create the "Direction" column
# (+1 or -1) indicating an up/down day
tsret["Direction"] = np.sign(tsret["Today"])
tsret = tsret[tsret.index >= start_date]
```

```
def validation_set_poly(random_seeds, degrees, X, y):
    """
    Use the train_test_split method to create a
    training set and a validation set (50% in each)
    using "random_seeds" separate random samplings over
    linear regression models of varying flexibility
    """
    sample_dict = dict(
        [("seed_%s" % i,[]) for i in range(1, random_seeds+1)]
    )
    # Loop over each random splitting into a train-test split
    for i in range(1, random_seeds+1):
        print("Random: %s" % i)
        # Increase degree of linear
        # regression polynomial order
        for d in range(1, degrees+1):
            print("Degree: %s" % d)
            # Create the model, split the sets and fit it
            polynomial_features = PolynomialFeatures(
                degree=d, include_bias=False
            )
            linear_regression = LinearRegression()
            model = Pipeline([
                ("polynomial_features", polynomial_features),
                ("linear_regression", linear_regression)
            ])
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.5, random_state=i
            )
            model.fit(X_train, y_train)
            # Calculate the test MSE and append to the
            # dictionary of all test curves
            y_pred = model.predict(X_test)
            test_mse = mean_squared_error(y_test, y_pred)
            sample_dict["seed_%s" % i].append(test_mse)
        # Convert these lists into numpy
        # arrays to perform averaging
```

```
sample_dict["seed_%s" % i] = np.array(
            sample_dict["seed_%s" % i]
        )
    # Create the "average test MSE" series by averaging the
    # test MSE for each degree of the linear regression model,
    # across all random samples
    sample_dict["avg"] = np.zeros(degrees)
    for i in range(1, random_seeds+1):
        sample_dict["avg"] += sample_dict["seed_%s" % i]
    sample_dict["avg"] /= float(random_seeds)
    return sample_dict
def k_fold_cross_val_poly(folds, degrees, X, y):
    """
    Use the k-fold cross validation method to create
    k separate training test splits over linear
    regression models of varying flexibility
    """
    # Create the KFold object and
    # set the initial fold to zero
    n = len(X)
    kf = KFold(n, n_folds=folds)
    kf_dict = dict(
        [("fold_%s" % i,[]) for i in range(1, folds+1)]
    )
    fold = 0
    # Loop over the k-folds
    for train_index, test_index in kf:
        fold += 1
        print("Fold: %s" % fold)
        X_train, X_test = X.ix[train_index], X.ix[test_index]
        y_train, y_test = y.ix[train_index], y.ix[test_index]
        # Increase degree of linear regression polynomial order
        for d in range(1, degrees+1):
            print("Degree: %s" % d)
            # Create the model and fit it
            polynomial_features = PolynomialFeatures(
                degree=d, include_bias=False
            )
            linear_regression = LinearRegression()
```

```
model = Pipeline([
                ("polynomial_features", polynomial_features),
                ("linear_regression", linear_regression)
            ])
            model.fit(X_train, y_train)
            # Calculate the test MSE and append to the
            # dictionary of all test curves
            y_pred = model.predict(X_test)
            test_mse = mean_squared_error(y_test, y_pred)
            kf_dict["fold_%s" % fold].append(test_mse)
        # Convert these lists into numpy
        # arrays to perform averaging
        kf_dict["fold_%s" % fold] = np.array(
            kf_dict["fold_%s" % fold]
        )
    # Create the "average test MSE" series by averaging the
    # test MSE for each degree of the linear regression model,
    # across each of the k folds.
    kf_dict["avg"] = np.zeros(degrees)
    for i in range(1, folds+1):
        kf_dict["avg"] += kf_dict["fold_%s" % i]
    kf_dict["avg"] /= float(folds)
    return kf_dict
def plot_test_error_curves_vs(sample_dict, random_seeds, degrees):
    fig, ax = plt.subplots()
    ds = range(1, degrees+1)
    for i in range(1, random_seeds+1):
        ax.plot(
            ds,
            sample_dict["seed_%s" % i],
            lw=2,
            label='Test MSE - Sample %s' % i
        )
    ax.plot(
        ds,
        sample_dict["avg"],
        linestyle='--',
        color="black",
        lw=3,
```

```
label='Avg Test MSE'
    )
    ax.legend(loc=0)
    ax.set_xlabel('Degree of Polynomial Fit')
    ax.set_ylabel('Mean Squared Error')
    fig.set_facecolor('white')
    plt.show()
def plot_test_error_curves_kf(kf_dict, folds, degrees):
    fig, ax = plt.subplots()
    ds = range(1, degrees+1)
    for i in range(1, folds+1):
        ax.plot(
            ds,
            kf_dict["fold_%s" % i],
            lw=2,
            label='Test MSE - Fold %s' % i
        )
    ax.plot(
        ds,
        kf_dict["avg"],
        linestyle='--',
        color="black",
        lw=3,
        label='Avg Test MSE'
    )
    ax.legend(loc=0)
    ax.set_xlabel('Degree of Polynomial Fit')
    ax.set_ylabel('Mean Squared Error')
    fig.set_facecolor('white')
    plt.show()
if __name__ == "__main__":
    symbol = "AMZN"
    start_date = datetime.datetime(2004, 1, 1)
    end_date = datetime.datetime(2016, 10, 27)
    lags = create_lagged_series(
        symbol, start_date, end_date, lags=10
    )
    # Use ten prior days of returns as predictor
    # values, with "Today" as the response
```

```
X = lags[[
    "Lag1", "Lag2", "Lag3", "Lag4", "Lag5",
    "Lag6", "Lag7", "Lag8", "Lag9", "Lag10",
]]
y = lags["Today"]
degrees = 3
# Plot the test error curves for validation set
random_seeds = 10
sample_dict_val = validation_set_poly(
    random_seeds, degrees, X, y
)
plot_test_error_curves_vs(
    sample_dict_val, random_seeds, degrees
)
# Plot the test error curves for k-fold CV set
folds = 10
kf_dict = k_fold_cross_val_poly(
    folds, degrees, X, y
)
plot_test_error_curves_kf(
    kf_dict, folds, degrees
)
```
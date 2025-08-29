# **Predicting the Markets with Basic Machine Learning**

In the last chapter, we learned how to design trading strategies, create trading signals, and implement advanced concepts, such as seasonality in trading instruments. Understanding those concepts in greater detail is a vast field comprising stochastic processes, random walks, martingales, and time series analysis, which we leave to you to explore at your own pace.

So what's next? Let's look at an even more advanced method of prediction and forecasting:

statistical inference and prediction. This is known as machine learning, the fundamentals of

which were developed in the 1800s and early 1900s and have been worked on ever since. Recently, there has been a resurgence in interest in machine learning algorithms and applications owing to the availability of extremely cost-effective processing power and the easy availability of large datasets. Understanding machine learning techniques in great detail is a massive field at the intersection of linear algebra, multivariate calculus, probability theory, frequentist and Bayesian statistics, and an in-depth analysis of machine learning is beyond the scope of a single book. Machine learning methods, however, are surprisingly easily accessible in Python and quite intuitive to understand, so we will explain the intuition behind the methods and see how they find applications in algorithmic trading. But first, let's introduce some basic concepts and notation that we will need for the rest of this chapter.

This chapter will cover the following topics:

- Understanding the terminology and notations
- Creating predictive models that predict price movement using linear regression methods

Creating predictive models that predict buy and sell signals using linear classification methods

### **Understanding the terminology and notations**

To develop ideas quickly and build an intuition regarding supply and demand, we have a simple and completely hypothetical dataset of height, weight, and race of a few random samples obtained from a survey. Let's have a look at the dataset:

| Height (inches) | Weight (lbs) | Race (Asian/African/Caucasian) |  |
|-----------------|--------------|--------------------------------|--|
| 72              | 180          | Asian                          |  |
| 66              | 150          | Asian                          |  |
| 70              | 190          | African                        |  |
| 75              | 210          | Caucasian                      |  |
| 64              | 150          | Asian                          |  |
| 77              | 220          | African                        |  |
| 70              | 200          | Caucasian                      |  |

| 65 | 150 | African |
|----|-----|---------|

Let's examine the individual fields:

- Height in inches and weight in lbs are continuous data types because they can take on any values, such as 65, 65.123, and 65.3456667.
- Race, on the other hand, would be an example of a categorical data type, because there are a finite number of possible values that can go in the field. In this example, we assume that possible race values are Asian, African, and Caucasian.

Now, given this dataset, say our task is to build a mathematical model that can *learn* from the data we provide it with. The task or objective we are trying to learn in this example is to find the relationship between the weight of a person as it relates to their height and race. Intuitively, it should be obvious that height will have a major role to play (taller people are much more likely to be heavier), and race should have very little impact. Race may have some impact on the height of an individual, but once the height is known, knowing their race also provides very little additional information in guessing/predicting a person's weight. In this particular problem, note that in the dataset, we are also provided the weight of the samples in addition to their height and race.

Since the variable we are trying to learn how to predict is known, this is known as a **supervised learning problem**. If, on the other hand, we were not provided with the weight variable and were asked to predict whether, based on height and race, someone is more likely to be heavier than someone else, that would be an unsupervised learning problem. For the scope of this chapter, we will focus on supervised learning problems only, since that is the most typical use case of machine learning in algorithmic trading.

Another thing to address in this example is the fact that, in this case, we are trying to predict weight as a function of height and race. So we are trying to predict a continuous variable. This is known as a regression problem, since the output of such a model is a continuous value. If, on the other hand, say our task was to predict the race of a person as a function of their height and weight, in that case, we would be trying to predict a categorical variable type. This is known as a classification problem, since the output of such a model will be one value from a set of finite discrete values.

When we start addressing this problem, we will begin with a dataset that is already available to us and will *train* our model of choice on this dataset. This process (as you've already guessed) is known as training your model. We will use the data provided to us to guess the parameters of the learning model of our choice (we will elaborate more on what this means later). This is known as statistical inference of these parametric learning models. There are also non-parametric learning models, where we try to remember the data we've seen so far to make a guess as regards new data.

Once we are done training our model, we will use it to predict weight for datasets we haven't seen yet. Obviously, this is the part we are interested in. Based on data in the future that we haven't seen yet, can we predict the weight? This is known as testing your model and the datasets used for that are known as test data. The task of using a model where the parameters were learned by statistical inference to actually make predictions on previously unseen data is known as statistical prediction or forecasting.

We need to be able to understand the metrics of how to differentiate between a good model and a bad model. There are several well known and well understood performance metrics for different models. For regression prediction problems, we should try to minimize the differences between predicted value and the actual value of the target variable. This error term is known as residual errors; larger errors mean worse models and, in regression, we try to minimize the sum of these residual errors, or the sum of the square of these residual errors (squaring has the effect of penalizing large outliers more strongly, but more on that later). The most common metric for regression problems is *R^2*, which tracks the ratio of explained

variance vis-à-vis unexplained variance, but we save that for more advanced texts.

In the simple hypothetical prediction problem of guessing weight based on height and race, let's say the model predicts the weight to be 170 and the actual weight is 160. In this case, the error is *160-170 = -10*, the absolute error is *|-10| = 10*, and the squared error is *(-10)^2 = 100*. In classification problems, we want to make sure our predictions are the same discrete value as the actual value. When we predict a label that is different from the actual label, that is a misclassification or error. Obviously, the higher the number of accurate predictions, the better the model, but it gets more complicated than that. There are metrics such as a confusion matrix, a receiver operating characteristic, and the area under the curve, but we save those for more advanced texts. Let's say, in the modified hypothetical problem of guessing race based on height and weight, that we guess the race to be Caucasian while the correct race is African. That is then considered an error, and we can aggregate all such errors to find the aggregate errors across all predictions, but we will talk more on this in the later parts of the book.

So far, we have been speaking in terms of a hypothetical example, but let's tie the terms we've encountered so far into how it applies to financial datasets. As we mentioned, supervised learning methods are most common here because, in historical financial data, we are able to measure the price movements from the data. If we are simply trying to predict that, if a price moves up or down from the current price, then that is a classification problem with two prediction labels – *Price goes up* and *Price goes down*. There can also be three prediction labels since *Price goes up*, *Price goes down*, and *Price remains the same*. If, however, we want to predict the magnitude and direction of price moves, then this is a regression problem where an example of the output could be *Price moves +10.2 dollars*, meaning the prediction is that the price will move up by \$10.2. The training dataset is generated from historical data, and this can be historical data that was not used in training the model and the live market data during live trading. We measure the accuracy of such models with the metrics we listed above in addition to the PnL generated from the trading strategies. With this introduction complete, let's now look into these methods in greater detail, starting with regression methods.

#### **Exploring our financial dataset**

Before we start applying machine learning techniques to build predictive models, we need to perform some exploratory data wrangling on our dataset with the help of the steps listed here. This is often a large and an underestimated prerequisite when it comes to applying advanced methods to financial datasets.

1. **Getting the data**: We'll continue to use Google stock data that we've used in our previous chapter:

```
import pandas as pd
from pandas_datareader import data
def load_financial_data(start_date, end_date, output_file):
 try:
 df = pd.read_pickle(output_file)
 print('File data found...reading GOOG data')
 except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 df = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 df.to_pickle(output_file)
 return df
```

In the code, we revisited how to download the data and implement a method, load\_financial\_data, which we can use moving forward. It can also be invoked, as shown in the following code, to download 17 years' of daily Google data:

goog\_data = load\_financial\_data( start\_date='2001-01-01', end\_date='2018-01-01', output\_file='goog\_data\_large.pkl')

The code will download financial data over a period of 17 years from GOOG stock data. Now, let's move on to the next step.

2. **Creating objectives/trading conditions that we want to predict**: Now that we know how to download our data, we need to operate on it to extract our target for the predictive models, also known as a response or dependent variable; effectively, what we are trying predict.

In our hypothetical example of predicting weight, weight was our response variable. For algorithmic trading, the common target is to be able to predict what the future price will be so that we can take positions in the market right now that will yield a profit in the future. If we model the response variable as future price-current price, then we are trying to predict the direction of the future price with regard to the current price (does it go up, does it go down, or does it remain the same), as well as the magnitude of the price change. So, these variables look like +10, +3.4, -4, and so on. This is the response variable methodology that we will use for regression models, but we will look at it in greater detail later. Another variant of the response variable would be to simply predict the direction but ignore the magnitude, in other words, +1 to signify the future price moving up, -1 to signify the future price moving down, and 0 to signify that the future price remains the same as the current price. That is the response variable methodology that we will use for classification models, but we will explore that later. Let's implement the following code to generate these response variables:

```
def create_classification_trading_condition(df):
 df['Open-Close'] = df.Open - df.Close
 df['High-Low'] = df.High - df.Low
 df = df.dropna()
 X = df[['Open-Close', 'High-Low']]
 Y = np.where(df['Close'].shift(-1) > df['Close'], 1, -1)
 return (X, Y)
```

In this code, the following applies:

The classification response variable is +1 if the close price tomorrow is higher than the close price today, and -1 if the close price tomorrow is lower than the close price today.

For this example, we assume that the close price tomorrow is not the same as the close price today, which we can choose to handle by creating a third categorical value, 0.

The regression response variable is *Close price tomorrow-Close price today for each day*. Let's have a look at the code:

```
def create_regression_trading_condition(df):
 df['Open-Close'] = df.Open - df.Close
 df['High-Low'] = df.High - df.Low
 df = df.dropna()
 X = df[['Open-Close', 'High-Low']]
 Y = df['Close'].shift(-1) - df['Close']
 return (X, Y)
```

In this code, the following applies:

- It is a positive value if the price goes up tomorrow, a negative value if the price goes down tomorrow, and zero if the price does not change.
- The sign of the value indicates the direction, and the magnitude of the response variable captures the magnitude of the price move.
- 3. **Partitioning datasets into training and testing datasets**: One of the key questions regarding a trading strategy is how it will perform on market conditions or datasets that the trading strategy has not seen. Trading performance on datasets that have not been used in training the predictive model is often referred to as out-sample performance for that trading strategy. These results are considered representative of what to expect when the trading strategy is run in live markets. Generally, we divide all of our available datasets into multiple partitions, and then we evaluate models trained on one dataset over a dataset that wasn't used in training it (and optionally validated on yet another dataset after that). For the purpose of our models, we will be partitioning our dataset into two datasets: training and testing. Let's have a look at the code:

```
from sklearn.model_selection import train_test_split
def create_train_split_group(X, Y, split_ratio=0.8):
 return train_test_split(X, Y, shuffle=False, train_size=split_ratio)
```

In this code, the following applies:

- We used a default split ratio of 80%, so 80% of the entire dataset is used for training, and the remaining 20% is used for testing.
- There are more advanced splitting methods to account for distributions of underlying data (such as we want to avoid ending up with a training/testing dataset that is not truly representative of actual market conditions).

## **Creating predictive models using linear regression methods**

Now that we know how to get the datasets that we need, how to quantify what we are trying to predict (objectives), and how to split data into training and testing datasets to evaluate our trained models on, let's dive into applying some basic machine learning techniques to our datasets:

- First, we will start with regression methods, which can be linear as well as non-linear.
- **Ordinary Least Squares** (**OLS**) is the most basic linear regression model, which is where we will start from.
- Then, we will look into Lasso and Ridge regression, which are extensions of OLS, but which include regularization and shrinkage features (we will discuss these aspects in more detail later).
- Elastic Net is a combination of both Lasso and Ridge regression methods.
- Finally, our last regression method will be decision tree regression, which is capable of fitting non-linear models.

#### **Ordinary Least Squares**

Given observations of the target variables, rows of features values, and each row of dimension , OLS seeks to find the weights of dimension that minimize the residual sum of squares of differences between the target variable and the predicted variable predicted by linear approximation:

, which is the best fit for the equation , where is the matrix of feature values, is the matrix/vector of weights/coefficients assigned to each of the feature values, and is the matrix/vector of the target variable observation on our training dataset.

Here is an example of the matrix operations involved for and :

|     | x00                                                    | x01 |       | , $x_0$ ' |  |
|-----|--------------------------------------------------------|-----|-------|-----------|--|
| min | $\begin{vmatrix} x10 & x11 \\ x20 & x21 \end{vmatrix}$ |     | $w_0$ | $x_1$     |  |
|     |                                                        |     |       | $x_2$     |  |
|     | x30                                                    | x31 |       | $x_3$     |  |

- Intuitively, it is very easy to understand OLS with a single feature variable and a single target variable by visualizing it as trying to draw a line that has the *best fit*.
- OLS is just a generalization of this simple idea in much higher dimensions, where is tens of thousands of observations, and is thousands of features values.
- The typical setup in is much larger than (many more observations in comparison to the number of feature values), otherwise the solution is not guaranteed to be unique.
- There are closed form solutions to this problem where but, in practice, these are better implemented by iterative solutions, but we'll skip the details of all of that for now.
- The reason why we prefer to minimize the sum of the squares of the error terms is so that massive outliers are penalized more harshly and don't end up throwing off the entire fit.

There are many underlying assumptions for OLS in addition to the assumption that the target variable is a linear combination of the feature values, such as the independence of feature values themselves, and normally distributed error terms. The following diagram is a very simple example showing a relatively close linear relationship between two arbitrary variables. Note that it is not a perfect linear relationship, in other words, not all data points lie perfectly on the line and we have left out the X and Y labels because these can be any arbitrary variables. The point here is to demonstrate an example of what a linear relationship visualization looks like. Let's have a look at the following diagram:

![](_page_11_Figure_0.jpeg)

1. Let's start by loading up Google data in the code, using the same method that we introduced in the previous section:

```
goog_data = load_financial_data(
 start_date='2001-01-01',
 end_date='2018-01-01',
 output_file='goog_data_large.pkl')
```

2. Now, we create and populate the target variable vector, Y, for regression in the following code. Remember that what we are trying to predict in regression is magnitude and the direction of the price change from one day to the next:

```
goog_data, X, Y = create_regression_trading_condition(goog_data)
```

3. With the help of the code, let's quickly create a scatter plot for the two features we have: High-Low price of the day and Open-Close price of the day against the target variable, which is Price-Of-Next-Day - Price-Of-Today (future price):

```
pd.plotting.scatter_matrix(goog_data[['Open-Close', 'High-Low', 'Target']], grid=True, diagonal='kde')
```

This code will return the following output. Let's have a look at the plot:

![](_page_12_Figure_0.jpeg)

4. Finally, as shown in the code, let's split 80% of the available data into the training feature value and target variable set (X\_train, Y\_train), and the remaining 20% of the dataset into the outsample testing feature value and target variable set (X\_test, Y\_test):

```
X_train,X_test,Y_train,Y_test=create_train_split_group(X,Y,split_ratio=0.8)
```

5. Now, let's fit the OLS model as shown here and observe the model we obtain:

```
from sklearn import linear_model
ols = linear_model.LinearRegression()
ols.fit(X_train, Y_train)
```

6. The coefficients are the optimal weights assigned to the two features by the fit method. We will print the coefficients as shown in the code:

```
print('Coefficients: \n', ols.coef_)
```

This code will return the following output. Let's have a look at the coefficients:

```
Coefficients:
[[ 0.02406874 -0.05747032]]
```

7. The next block of code quantifies two very common metrics that test goodness of fit for the linear model we just built. Goodness of fit means how well a given model fits the data points observed in training and testing data. A good model is able to closely fit most of the data points and errors/deviations between observed and predicted values are very low. Two of the most popular metrics for linear regression models are mean\_squared\_error , which is what we explored as our objective to minimize when we introduced OLS, and R-squared ( ), which is another very popular metric that measures how well the fitted model predicts the target variable when compared to a baseline model whose prediction output is always the mean

of the target variable based on training data, that is, . We will skip the exact formulas for computing but, intuitively, the closer the value to 1, the better the fit, and the closer the value to 0, the worse the fit. Negative values mean that the model fits worse than the baseline model. Models with negative values usually indicate issues in the training data or process and cannot be used:

```
from sklearn.metrics import mean_squared_error, r2_score
# The mean squared error
print("Mean squared error: %.2f"
 % mean_squared_error(Y_train, ols.predict(X_train)))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y_train, ols.predict(X_train)))
# The mean squared error
print("Mean squared error: %.2f"
 % mean_squared_error(Y_test, ols.predict(X_test)))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y_test, ols.predict(X_test)))
```

This code will return the following output:

```
Mean squared error: 27.36
Variance score: 0.00
Mean squared error: 103.50
Variance score: -0.01
```

8. Finally, as shown in the code, let's use it to predict prices and calculate strategy returns:

```
goog_data['Predicted_Signal'] = ols.predict(X)
goog_data['GOOG_Returns'] = np.log(goog_data['Close'] / goog_data['Close'].shift(1))
def calculate_return(df, split_value, symbol):
 cum_goog_return = df[split_value:]['%s_Returns' % symbol].cumsum() * 100
 df['Strategy_Returns'] = df['%s_Returns' % symbol] * df['Predicted_Signal'].shift(1)
 return cum_goog_return
def calculate_strategy_return(df, split_value, symbol):
 cum_strategy_return = df[split_value:]['Strategy_Returns'].cumsum() * 100
 return cum_strategy_return
cum_goog_return = calculate_return(goog_data, split_value=len(X_train), symbol='GOOG')
cum_strategy_return = calculate_strategy_return(goog_data, split_value=len(X_train), symbol='GOOG')
def plot_chart(cum_symbol_return, cum_strategy_return, symbol):
 plt.figure(figsize=(10, 5))
 plt.plot(cum_symbol_return, label='%s Returns' % symbol)
 plt.plot(cum_strategy_return, label='Strategy Returns')
 plt.legend()
plot_chart(cum_goog_return, cum_strategy_return, symbol='GOOG')
def sharpe_ratio(symbol_returns, strategy_returns):
 strategy_std = strategy_returns.std()
 sharpe = (strategy_returns - symbol_returns) / strategy_std
 return sharpe.mean()
print(sharpe_ratio(cum_strategy_return, cum_goog_return))
```

This code will return the following output:

#### 2.083840359081768

Let's now have a look at the graphical representation that is derived from the code:

![](_page_14_Figure_2.jpeg)

Here, we can observe that the simple linear regression model using only the two features, Open-Close and High-Low, returns positive returns. However, it does not outperform the Google stock's return because it has been increasing in value since inception. But since that cannot be known ahead of time, the linear regression model, which does not assume/expect increasing stock prices, is a good investment strategy.
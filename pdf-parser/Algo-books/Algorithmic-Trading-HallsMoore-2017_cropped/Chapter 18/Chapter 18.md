## Chapter 18

# Tree-Based Methods

In this chapter a group of algorithms that make use of an underlying technique called a Decision Tree will be considered. Decision Trees (DTs) are a supervised learning technique that predict values of responses by learning decision rules derived from features. They can be used in both a regression and a classification context. For this reason they are sometimes also referred to as Classification And Regression Trees (CART).

DT/CART models are an example of a more general area of machine learning known as adaptive basis function models. These models learn the features directly from the data, rather than being prespecified, as in some other basis expansions. Unlike linear regression these models are not linear in the parameters. This means that it is only possible to compute a locally optimal maximum likelihood estimate (MLE) for the parameters[71], rather than a guaranteed global optimum.

DT/CART models work by partitioning the feature space into a number of simple rectangular regions divided up by axis parallel splits. In order to obtain a prediction for a particular observation the mean or mode of the rectangle in feature space to which the observation belongs is used.

One of the primary benefits of using an individual DT/CART is that by construction it produces interpretable if-then-else decision rulesets, which are akin to graphical flowcharts. The main disadvantage of a decision tree lies in the fact that it is often uncompetitive with other supervised techniques such as support vector machines or deep neural networks in terms of prediction accuracy.

However they become extremely competitive when used in an ensemble setting such as with bootstrap aggregation ("bagging"), Random Forests or boosting.

In quantitative finance ensembles of DT/CART models are used in forecasting both future asset prices and liquidity of certain instruments.

## 18.1 Decision Trees - Mathematical Overview

Under a probabilistic adaptive basis function specification the model f(x) is given by[71]:

$$f(\mathbf{x}) = \mathbb{E}(y \mid \mathbf{x}) = \sum_{m=1}^{M} w_m \phi(\mathbf{x}; \mathbf{v}_m)$$
 (18.1)

Where w<sup>m</sup> is the mean response in a particular region, Rm, and v<sup>m</sup> represents how each variable is split at a particular threshold value. These splits define how the feature space in R p is carved into M separate "hyperblock" regions.

## 18.2 Decision Trees for Regression

Consider an abstract example of regression problem with two feature variables (X1, X2) and a numerical response y. The two-dimensional setting allows straightforward visualisation of the partitioning carried out by the tree.

A pre-grown tree is shown in Figure [18.1:](#page-1-0)

![](_page_1_Figure_4.jpeg)

<span id="page-1-0"></span>Figure 18.1: A Decision Tree with six separate regions

It can be seen that at the first "branch" the question is asked as to whether the feature X<sup>1</sup> is less than some threshold value t1. If so, the next branch is considered and a further question is asked as to whether X<sup>2</sup> is less than another threshold parameter t2. If so, the value ends up in region 1, R1, otherwise it ends up in region 2, R2.

Similarly if X<sup>1</sup> is initially greater than or equal to t<sup>1</sup> in the first branch, a further subbranching occurs in subsequent layers. Eventually this defines regions R<sup>3</sup> to R6. In this fashion it is the threshold values t<sup>1</sup> to t<sup>5</sup> that determine how the feature space is carved into rectangular regions.

Figure 18.2 depicts a subset of R 2 trained on this hypothetical example data. Notice how the domain is partitioned using axis-parallel splits. That is, every split of the domain is aligned with one of the feature axes.

The concept of axis parallel splitting generalises straightforwardly to dimensions greater than two. For a feature space of dimension p–a subset of R <sup>p</sup>–the space is divided into M regions, each denoted by Rm, which are all p-dimensional "hyperblocks".

If a new unseen test feature vector is given it will lie somewhere in one these M regions. The response given to this feature vector is determined by the mean or mode response of the training values within the particular partition that the test vector lies in within feature space.

![](_page_2_Figure_0.jpeg)

Figure 18.2: The resulting partition of the subset of R 2 into six regional "blocks"

This shows how a tree makes predictions once created. However it has not yet been shown how such a tree is "grown" or "trained". The following section outlines the algorithm for carrying this out.

### 18.2.1 Creating a Regression Tree and Making Predictions

The basic outline for utilising a DT is as follows:

- Given p features, partition the p-dimensional feature space (a subset of R p ) into M mutually distinct regions that fully cover the subset of feature space and do not overlap. These regions are given by R1, ..., RM.
- Any new observation that falls into a particular partition R<sup>m</sup> has the estimated response given by the mean of all training observations with the partition, denoted by wm.

However, this process doesn't actually describe how to form the partition in an algorithmic manner! For that it is necessary to use a technique known as Recursive Binary Splitting (RBS)[59].

#### Recursive Binary Splitting

The goal with supervised learning algorithms is to minimise some form of error criterion. In this particular instance it is necessary to minimise the Residual Sum of Squares (RSS), an error measure described in the chapter on linear regression. The RSS in the case of a partitioned feature space with M partitions is given by:

$$RSS = \sum_{m=1}^{M} \sum_{i \in R_m} (y_i - \hat{y}_{R_m})^2$$
 (18.2)

The first task is to sum across all partitions of the feature space (the first summation sign) and then sum across all test observations (indexed by i) in a particular partition (the second summation sign). This is followed by taking the squared difference of the response y<sup>i</sup> of a particular testing observation with the mean response yˆR<sup>m</sup> of the training observations within partition m.

Unfortunately it is too computationally expensive to consider all possible partitions of the feature space into M rectangles (in fact the problem is [NP-complete\)](https://en.wikipedia.org/wiki/NP-completeness). Hence it is necessary to use a less computationally intensive, but more sophisticated search approach. This is where RBS comes in.

RBS approaches the problem by beginning at the top of the tree and splitting it into two branches. This creates two initial partitions of the feature space. It carries out this particular split at the top of the tree multiple times and chooses the split of the features that minimises the (current) RSS.

At this point the tree creates a new branch in a particular partition and carries out the same procedure, that is, evaluates the RSS at each split of the partition and chooses the best performing split.

This makes it a greedy algorithm, meaning that it carries out the evaluation for each iteration of the recursion, rather than "looking ahead" and continuing to branch before making the evaluations. It is this "greedy" nature of the algorithm that makes it computationally feasible and thus practical for use[71], [59].

At this stage a termination criterion has not been presented. There are a number of possibilities for stopping criteria that could be considered, including limiting the maximum depth of the tree, ensuring sufficient training examples in each region and/or ensuring that the regions are sufficiently homogeneous such that the tree is relatively "balanced".

However, as with all supervised machine learning methods, it is necessary to be constantly aware of the danger of overfitting the model. This motivates the concept of "pruning" the tree.

### 18.2.2 Pruning The Tree

Because of the ever-present dangers of overfitting and the bias-variance tradeoff it is necessary to adjust the tree splitting process so that it may generalise well to test sets.

Since it is too costly to use cross-validation directly on every possible sub-tree combination while growing the tree an alternative approach is desired that still provides sufficiently acceptable test error.

A common approach is to grow the full tree to a prespecified depth and carry out a procedure known as "pruning". One approach termed cost-complexity pruning is described in detail in James et al (2013)[59] and, to a greater mathematical depth, in Hastie et al (2009)[51]. By introducing an additional tuning parameter, denoted by α, that balances the depth of the tree and its goodness of fit to the training data, it is possible to obtain good results. The approach used is similar to the LASSO technique developed by Tibshirani[95].

The implementation details of tree pruning are beyond the scope of the book. Thankfully the Python Scikit-Learn machine learning library helpfully abstracts away the complexity.

## 18.3 Decision Trees for Classification

In this chapter we have concentrated almost exclusively on the regression case, but decision trees work equally well for classification.

The only difference, as with all classification regimes, is that we are now predicting a categorical rather than continuous response value. In order to actually make a prediction for a categorical class we have to instead use the mode of the training region to which an observation belongs, rather than the mean value. That is, we take the most commonly occurring class value and assign it as the response of the observation.

In addition we need to consider alternative criteria for splitting the trees as the usual RSS score is not applicable in the categorical setting. There are three that we will consider, which include the Hit Rate, the Gini Index and Cross-Entropy[71], [59], [51].

### 18.3.1 Classification Error Rate/Hit Rate

Rather than calculating how far a numerical response is away from the mean value, as in the regression setting, it is possible instead to define the Hit Rate as the fraction of training observations in a particular region that do not belong to the most widely occuring class. That is, the error is given by:

$$E = 1 - \operatorname{argmax}_{c}(\hat{\pi}_{mc}) \tag{18.3}$$

Where πˆmc represents the fraction of training data in region R<sup>m</sup> that belong to class c.

### 18.3.2 Gini Index

The Gini Index is an alternative error metric that is designed to show how "pure" a region is. "Purity" in this case means how much of the training data in a particular region belongs to a single class. If a region R<sup>m</sup> contains data that is mostly from a single class c then the Gini Index value will be small:

$$G = \sum_{c=1}^{C} \hat{\pi}_{mc} (1 - \hat{\pi}_{mc}) \tag{18.4}$$

### 18.3.3 Cross-Entropy/Deviance

A third alternative, similar to the Gini Index, is known as the Cross-Entropy or Deviance:

$$D = -\sum_{c=1}^{C} \hat{\pi}_{mc} \log \hat{\pi}_{mc} \tag{18.5}$$

This motivates the question as to which error metric to use when growing a classification tree. Anecdotally the Gini Index and Deviance are used more often than the Hit Rate in order to maximise for prediction accuracy. The reasons for this will not be considered directly here but a good discussion can be found in the books provided in the references within this chapter.

## 18.4 Advantages and Disadvantages of Decision Trees

As with all machine learning methods there are both advantages and disadvantages to using DT/CARTs over other models:

### 18.4.1 Advantages

- DT/CART models are easy to interpret since they generate automatic "if-then-else" rules
- The models can handle categorical and continuous features in the same data set
- The method of construction for DT/CART models means that feature variables are automatically selected, rather than having to use subset selection or similar dimensionality reduction techniques
- The models are able to scale effectively on large datasets

### 18.4.2 Disadvantages

- Poor relative prediction performance compared to other ML models
- DT/CART models suffer from instability, which means they are very sensitive to small changes in the feature space. In the language of the bias-variance trade-off, they are high variance estimators.

While DT/CART models themselves suffer from poor prediction performance they are extremely competitive when utilised in an ensemble setting, via bootstrap aggregation ("bagging"), Random Forests or boosting, which will now be discussed.

## 18.5 Ensemble Methods

In this section it will be shown how combining multiple decision trees in a statistical ensemble will vastly improve the predictive performance on the combined model. These statistical ensemble techniques are not limited to DTs and are in fact applicable to many regression and classification machine learning models. However, DTs provide a natural setting to discuss ensemble methods and they are often commonly associated together.

Once the theory of ensemble methods has been discussed they will be implemented in Python using the Scikit-Learn library, on financial data. Later in the book it will be shown how to apply such ensemble methods to an intraday trading strategy.

However before discussing the ensemble techniques of bagging, Random Forests and boosting, it is necessary to outline a technique from frequentist statistics known as The Bootstrap.

### 18.5.1 The Bootstrap

Bootstrapping[39] is a statistical resampling technique that involves random sampling of a dataset with replacement. It is often used as a means of quantifying the uncertainty associated with a machine learning model.

For quantitative finance purposes bootstrapping is extremely useful as it allows generation of new samples from a population without having to go and collect additional training data. In quantitative finance applications it is often impossible to generate more data (in the case of financial asset pricing series) as there is only one history to draw from.

The basic idea is to repeatedly sample, with replacement, data from the original training set in order to produce multiple separate training sets. These are then used to allow meta-learner methods to reduce the variance of their predictions, thus greatly improving their predictive performance.

Two of the following ensemble techniques–bagging and Random Forests–make heavy use of bootstrapping techniques, and they will now be discussed.

### 18.5.2 Bootstrap Aggregation

One of the main drawbacks of DTs is that they suffer from being high-variance estimators. The addition of a small number of extra training points can dramatically alter the prediction performance of a learned tree, despite the training data not changing to any great extent.

This is in contrast to a low-variance estimator, such as linear regression, which is not hugely sensitive to the addition of extra points–at least those that are relatively close to the remaining points.

One way to minimise this problem is to utilise a concept known as bootstrap aggregation or bagging. The basic idea is to combine multiple leaners (such as DTs) all fitted on separate bootstrapped samples and average their predictions in order to reduce the overall variance of these predictions.

Why does this work? James et al (2013)[59] point out that if N independent and identically distributed (iid) observations Z1, . . . , Z<sup>N</sup> are given, each with a variance of σ 2 then the variance of the mean of the observations, Z¯ is σ <sup>2</sup>/N. That is, if the average of these observations is taken the variance is reduced by a factor equal to the number of observations.

However in quantitative finance datasets it is often the case that there is only one set of training data. This means it is difficult, if not impossible, to create multiple separate independent training sets. This is where The Bootstrap comes in. It allows the generation of multiple training sets that all use one larger set.

Using the notation from James et al (2013)[59] and the Random Forest article at Wikipedia[16], if B separate bootstrapped samples of the training set are created, with separate model estimators ˆf b (x), then averaging these leads to a low-variance estimator model, ˆfavg:

$$\hat{f}_{\text{avg}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} \hat{f}^b(\mathbf{x}) \tag{18.6}$$

This procedure is known as bagging[26]. It is highly applicable to DTs because they are high-variance estimators. It provides one mechanism to reduce the variance substantially.

Carrying out bagging for DTs is straightforward. Hundreds or thousands of deeply-grown (non-pruned) trees are created across B bootstrapped samples of the training data. They are combined in the manner described above to significantly reduce the variance of the overall estimator.

One of the main benefits of bagging is that it is not possible to overfit the model solely by increasing the number of bootstrap samples, B. This is also true for Random Forests but not the method of Boosting.

Unfortunately this gain in prediction accuracy comes at a price–significantly reduced interpretability of the data. However in quantitative trading research interpretability is often less important than raw prediction accuracy.

Note that there are specific statistical methods to deduce the important variables in bagging but they are beyond the scope of this book.

### 18.5.3 Random Forests

Random Forests[27] are very similar to the procedure of bagging except that they make use of a technique called feature bagging. Feature bagging significantly decreases the correlation between each DT and thus increases total predictive accuracy, on average.

Feature bagging works by randomly selecting a subset of the p feature dimensions at each split in the growth of individual DTs. This may sound counterintuitive, after all it is often desired to include as many features as possible initially in order to gain as much information for the model. However it has the purpose of deliberately avoiding (on average) very strong predictive features that lead to similar splits in trees.

That is, if a particular feature is strong in the response value, then it will be selected for many trees and thus a standard bagging procedure can be quite correlated. Random Forests avoid this by deliberately leaving out these strong features in many of the grown trees.

If all p values are chosen in the Random Forest setting then this simply corresponds to bagging. A rule-of-thumb is to use <sup>√</sup><sup>p</sup> features, suitably rounded, at each split.

In the Python section below it will be shown how Random Forests compare to bagging in their performance.

### 18.5.4 Boosting

Another general machine learning ensemble method is known as boosting. Boosting differs somewhat from bagging as it does not involve bootstrap sampling. Instead models are generated sequentially and iteratively. It is necessary to have information about model i before iteration i + 1 is produced.

Boosting was motivated by Kearns and Valiant (1989)[63]. They asked whether it was possible to combine, in some fashion, a selection of weak machine learning models to produce a single strong machine learning model. Weak, in this instance means a model that is only slightly better than chance at predicting a response. Correspondingly, a strong learner is one that is well-correlated to the true response.

This motivated the concept of boosting. The idea is to iteratively learn weak machine learning models on a continually-updated training data set and then add them together to produce a final, strong learning model. This differs from bagging, which simply averages the models on separate bootstrapped samples.

The basic algorithm for boosting, which is discussed at length in James et al (2013)[59] and Hastie et al (2009)[51], is given in the following:

- 1. Set the initial estimator to zero, that is ˆf(x) = 0. Also set the residuals to the current responses, r<sup>i</sup> = y<sup>i</sup> , for all elements in the training set.
- 2. Set the number of boosted trees, B. Loop over b = 1, . . . , B:

- (a) Grow a tree  $\hat{f}^b$  with k splits to training data  $(x_i, r_i)$ , for all i.
- (b) Add a scaled version of this tree to the final estimator:  $\hat{f}(\mathbf{x}) \leftarrow \hat{f}(\mathbf{x}) + \lambda \hat{f}^b(\mathbf{x})$
- (c) Update the residuals to account for the new model:  $r_i \leftarrow r_i \lambda \hat{f}^b(x_i)$

3. Set the final boosted model to be the sum of individual weak learners:  $\hat{f}(\mathbf{x}) = \sum_{b=1}^{B} \lambda \hat{f}^b(\mathbf{x})$ 

Notice that each subsequent tree is fitted to the *residuals* of the data. Hence each subsequent iteration is slowly improving the overall strong learner by improving its performance in poorlyperforming regions of the feature space.

It can be seen that this procedure is strongly dependent on the order in which the trees are grown. This process is said to "learn slowly". Such slow learning procedures tend to produce well-performing machine learning models.

There are three hyperparameters to the boosting algorithm described above. Namely, the depth of the tree k, the number of boosted trees B and the shrinkage rate  $\lambda$ . Some of these parameters can be set by cross-validation, the details of which are outlined in a subsequent chapter.

One of the computational drawbacks of boosting is that it is a sequential iterative method. This means that it cannot be easily parallelised, unlike bagging, which is straightforwardly parallelisable.

Many boosting algorithms exist, including AdaBoost, XGboost and LogitBoost. Prior to the increased prevalence of deep convolutional neural networks, boosted trees were often some of the best "out of the box" classification tools in existence.

It will now be shown how boosting compares with bagging, at least for the decision tree case, in the subsequent section.

#### Python Scikit-Learn Implementation $18.5.5$

In this section the above three ensemble methods will be applied to the task of predicting the daily returns for Amazon stock (AMZN), using the prior three days of lagged returns data.

This is a challenging task, not least because liquid stocks such as AMZN have a low signalto-noise ratio, but also because such data is *serially correlated*. This means that the samples chosen are not truly independent of each other, which can have unfortunate consequences for the statistical validity of the procedure. This must be considered when using a standard trainingtesting split of the data, as will be carried out below.

The end result will be a plot of the Mean Squared Error (MSE) of each method (bagging, Random Forest and boosting) against the number of estimators used in the sample. It will be clearly shown that bagging and Random Forests do not overfit as the number of estimators increases, while AdaBoost significantly overfits.

As always the first task is to import the correct libraries and objects. For this task many modules are required, the majority of which are in the Scikit-Learn library. In particular the "usual suspects" are imported, namely Matplotlib, NumPy, Pandas and Seaborn for data analysis and  $plotting. In addition the BaggingRegressor, RandomForestRegressor and AdaBoostRegressor$ ensemble methods are all included. Finally the mean\_squared\_error metric, the train\_test\_split cross-validation tool, preprocessing tool and DecisionTreeRegressor itself are all imported:

#### <pre># ensemble\_prediction.py</pre>

```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import seaborn as sns
import sklearn
from sklearn.ensemble import (
    BaggingRegressor, RandomForestRegressor, AdaBoostRegressor
)
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeRegressor
```

The next task is to use Pandas to create the DataFrame of lagged values. This particular piece of code has been utilised widely in Successful Algorithmic Trading and in other parts of this book. Hence it will not be explained in depth. It creates a DataFrame containing three days of lagged returns data from a particular Yahoo Finance asset time series along with the daily trading volume:

```
def create_lagged_series(symbol, start_date, end_date, lags=3):
    """
    This creates a pandas DataFrame that stores
    the percentage returns of the adjusted closing
    value of a stock obtained from Yahoo Finance,
    along with a number of lagged returns from the
    prior trading days (lags defaults to 3 days).
    Trading volume is also included.
    """
    # Obtain stock information from Yahoo Finance
    ts = web.DataReader(
        symbol, "yahoo", start_date, end_date
    )
    # Create the new lagged DataFrame
    tslag = pd.DataFrame(index=ts.index)
    tslag["Today"] = ts["Adj Close"]
    tslag["Volume"] = ts["Volume"]
    # Create the shifted lag series of
    # prior trading period close values
    for i in range(0,lags):
```

```
tslag["Lag%s" % str(i+1)] = ts["Adj Close"].shift(i+1)
```

```
# Create the returns DataFrame
tsret = pd.DataFrame(index=tslag.index)
tsret["Volume"] = tslag["Volume"]
tsret["Today"] = tslag["Today"].pct_change()*100.0
# Create the lagged percentage returns columns
for i in range(0,lags):
    tsret["Lag%s" % str(i+1)] = tslag[
        "Lag%s" % str(i+1)
    ].pct_change()*100.0
tsret = tsret[tsret.index >= start_date]
return tsret
```

In the \_\_main\_\_ function the parameters are set. Firstly a random seed is defined to make the code replicable on other work environments. n\_jobs controls the number of processor cores to use in bagging and Random Forests. Boosting is not parallelisable so does not make use of this parameter.

n\_estimators defines the total number of estimators to use in the graph of the MSE, while the step\_factor controls how granular the calculation is by stepping through the number of estimators. In this instance axis\_step is equal to 1000/10 = 100. That is, 100 separate calculations will be performed for each of the three ensemble methods:

```
# Set the random seed, number of estimators
# and the "step factor" used to plot the graph of MSE
# for each method
random_state = 42
n_jobs = 1 # Parallelisation factor for bagging, random forests
n_estimators = 1000
step_factor = 10
axis_step = int(n_estimators/step_factor)
```

The following code downloads ten years worth of AMZN prices and converts them into a return series with lags using the above mentioned function create\_lagged\_series. Missing values are dropped (a consequence of the lag procedure) and the data is scaled to exist between -1 and +1 for ease of comparison. This latter procedure is common in machine learning and helps features with large differences in absolute sizes be comparable to the models:

```
# Download ten years worth of Amazon
# adjusted closing prices
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2015, 12, 31)
amzn = create_lagged_series("AMZN", start, end, lags=3)
amzn.dropna(inplace=True)
```

```
# Use the first three daily lags of AMZN closing prices
# and scale the data to lie within -1 and +1 for comparison
```

```
X = amzn[["Lag1", "Lag2", "Lag3"]]
y = amzn["Today"]
X = scale(X)
y = scale(y)
```

The data is split into a training set and a test set, with 70% of the data forming the training data and the remaining 30% performing the test set. Once again, note that financial time series data is serially correlated, so this procedure will introduce some error by not accounting for it, however it serves the purpose for comparison across procedures in this chapter:

```
# Use the training-testing split with 70% of data in the
# training data with the remaining 30% of data in the testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=random_state
)
```

The following NumPy arrays store the number of estimators at each axis step, as well as the actual associated MSE for each of the three ensemble methods. They are all initially set to zero and are filled in subsequently:

```
# Pre-create the arrays which will contain the MSE for
# each particular ensemble method
estimators = np.zeros(axis_step)
bagging_mse = np.zeros(axis_step)
rf_mse = np.zeros(axis_step)
boosting_mse = np.zeros(axis_step)
```

The first ensemble method to be utilised is the bagging procedure. The code iterates over the total number of estimators (1-1000 in this case, with a step-size of 10), defines the ensemble model with the correct base model (in this case a regression tree), fits it to the training data and then calculates the Mean Squared Error on the test data. This MSE is then added to the bagging MSE array:

```
# Estimate the Bagging MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Bagging Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
    )
    bagging = BaggingRegressor(
        DecisionTreeRegressor(),
        n_estimators=step_factor*(i+1),
        n_jobs=n_jobs,
        random_state=random_state
    )
    bagging.fit(X_train, y_train)
    mse = mean_squared_error(y_test, bagging.predict(X_test))
    estimators[i] = step_factor*(i+1)
    bagging_mse[i] = mse
```

The same approach is carried out for Random Forests. However, since Random Forests implicitly use a regression tree as their base estimators, there is no need to specify it in the ensemble constructor:

```
# Estimate the Random Forest MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Random Forest Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
    )
    rf = RandomForestRegressor(
        n_estimators=step_factor*(i+1),
        n_jobs=n_jobs,
        random_state=random_state
    )
    rf.fit(X_train, y_train)
    mse = mean_squared_error(y_test, rf.predict(X_test))
    estimators[i] = step_factor*(i+1)
    rf_mse[i] = mse
```

Similarly for the AdaBoost boosting algorithm, with the exception that n\_jobs is not present due to the lack of parallelisability of boosting techniques. The learning rate, or shrinkage factor, λ has been set to 0.01. Adjusting this value has a large impact on the absolute MSE calculated for each estimator total:

```
# Estimate the AdaBoost MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Boosting Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
    )
    boosting = AdaBoostRegressor(
        DecisionTreeRegressor(),
        n_estimators=step_factor*(i+1),
        random_state=random_state,
        learning_rate=0.01
    )
    boosting.fit(X_train, y_train)
    mse = mean_squared_error(y_test, boosting.predict(X_test))
    estimators[i] = step_factor*(i+1)
    boosting_mse[i] = mse
```

The final snippet of code simply plots these arrays against each other using Matplotlib but with Seaborn's default colour scheme. This is more visually pleasing than the Matplotlib defaults:

```
# Plot the chart of MSE versus number of estimators
plt.figure(figsize=(8, 8))
plt.title('Bagging, Random Forest and Boosting comparison')
```

```
plt.plot(estimators, bagging_mse, 'b-', color="black", label='Bagging')
plt.plot(estimators, rf_mse, 'b-', color="blue", label='Random Forest')
plt.plot(estimators, boosting_mse, 'b-', color="red", label='AdaBoost')
plt.legend(loc='upper right')
plt.xlabel('Estimators')
plt.ylabel('Mean Squared Error')
plt.show()
```

The output is given in Figure [18.3.](#page-13-0) It is very clear how increasing the number of estimators for the bootstrap-based methods (bagging and Random Forests) eventually leads to the MSE "settling down" and becoming almost identical between them. However, for the AdaBoost boosting algorithm it can be seen that as the number of estimators is increased beyond 100 or so, the method begins to significantly overfit.

![](_page_13_Figure_2.jpeg)

<span id="page-13-0"></span>Figure 18.3: Bagging, Random Forest and AdaBoost MSE comparison vs number of estimators in the ensemble

When constructing a trading strategy based on a boosting ensemble procedure this fact must be borne in mind otherwise it is likely to lead to significant underperformance of the strategy when applied to out-of-sample financial data.

In a subsequent chapter ensemble models will be utilised to predict asset returns. It will be

seen whether it is feasible to produce a robust strategy that can be profitable above the higher frequency transaction costs necessary to carry it out.

## 18.6 Bibliographic Note

A gentle introduction to tree-based methods can be found in James et al (2013)[59], which covers the basics of both DTs and their associated ensemble methods.

A more rigourous account, pitched at the late undergraduate/early graduate mathematics/statistics level can be found in Hastie et al (2009)[51].

Murphy (2012)[71] provides a discussion of Adaptive Basis Function Models, of which DT/- CART models are a subset. The book covers both the frequentist and Bayesian approach to these models.

For the practitioner working on "real world" data (such as quants!), Kuhn et al (2013)[67] is an appropriate text pitched at a simpler level.

## 18.7 Full Code

```
# ensemble_prediction.py
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import seaborn as sns
import sklearn
from sklearn.ensemble import (
    BaggingRegressor, RandomForestRegressor, AdaBoostRegressor
)
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeRegressor
def create_lagged_series(symbol, start_date, end_date, lags=3):
    """
    This creates a pandas DataFrame that stores
    the percentage returns of the adjusted closing
    value of a stock obtained from Yahoo Finance,
    along with a number of lagged returns from the
    prior trading days (lags defaults to 3 days).
    Trading volume is also included.
```

```
# Obtain stock information from Yahoo Finance
    ts = web.DataReader(
        symbol, "yahoo", start_date, end_date
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
    # Create the lagged percentage returns columns
    for i in range(0,lags):
        tsret["Lag%s" % str(i+1)] = tslag[
            "Lag%s" % str(i+1)
        ].pct_change()*100.0
    tsret = tsret[tsret.index >= start_date]
    return tsret
if __name__ == "__main__":
    # Set the random seed, number of estimators
    # and the "step factor" used to plot the graph of MSE
    # for each method
    random_state = 42
    n_jobs = 1 # Parallelisation factor for bagging, random forests
    n_estimators = 1000
    step_factor = 10
    axis_step = int(n_estimators/step_factor)
    # Download ten years worth of Amazon
    # adjusted closing prices
    start = datetime.datetime(2006, 1, 1)
    end = datetime.datetime(2015, 12, 31)
```

"""

```
amzn = create_lagged_series("AMZN", start, end, lags=3)
amzn.dropna(inplace=True)
# Use the first three daily lags of AMZN closing prices
# and scale the data to lie within -1 and +1 for comparison
X = amzn[["Lag1", "Lag2", "Lag3"]]
y = amzn["Today"]
X = scale(X)
y = scale(y)
# Use the training-testing split with 70% of data in the
# training data with the remaining 30% of data in the testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=random_state
)
# Pre-create the arrays which will contain the MSE for
# each particular ensemble method
estimators = np.zeros(axis_step)
bagging_mse = np.zeros(axis_step)
rf_mse = np.zeros(axis_step)
boosting_mse = np.zeros(axis_step)
# Estimate the Bagging MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Bagging Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
    )
    bagging = BaggingRegressor(
        DecisionTreeRegressor(),
        n_estimators=step_factor*(i+1),
        n_jobs=n_jobs,
        random_state=random_state
    )
    bagging.fit(X_train, y_train)
    mse = mean_squared_error(y_test, bagging.predict(X_test))
    estimators[i] = step_factor*(i+1)
    bagging_mse[i] = mse
# Estimate the Random Forest MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Random Forest Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
```

```
)
    rf = RandomForestRegressor(
        n_estimators=step_factor*(i+1),
        n_jobs=n_jobs,
        random_state=random_state
    )
    rf.fit(X_train, y_train)
    mse = mean_squared_error(y_test, rf.predict(X_test))
    estimators[i] = step_factor*(i+1)
    rf_mse[i] = mse
# Estimate the AdaBoost MSE over the full number
# of estimators, across a step size ("step_factor")
for i in range(0, axis_step):
    print("Boosting Estimator: %d of %d..." % (
        step_factor*(i+1), n_estimators)
    )
    boosting = AdaBoostRegressor(
        DecisionTreeRegressor(),
        n_estimators=step_factor*(i+1),
        random_state=random_state,
        learning_rate=0.01
    )
    boosting.fit(X_train, y_train)
    mse = mean_squared_error(y_test, boosting.predict(X_test))
    estimators[i] = step_factor*(i+1)
    boosting_mse[i] = mse
# Plot the chart of MSE versus number of estimators
plt.figure(figsize=(8, 8))
plt.title('Bagging, Random Forest and Boosting comparison')
plt.plot(estimators, bagging_mse, 'b-', color="black", label='Bagging')
plt.plot(estimators, rf_mse, 'b-', color="blue", label='Random Forest')
plt.plot(estimators, boosting_mse, 'b-', color="red", label='AdaBoost')
plt.legend(loc='upper right')
plt.xlabel('Estimators')
plt.ylabel('Mean Squared Error')
plt.show()
```
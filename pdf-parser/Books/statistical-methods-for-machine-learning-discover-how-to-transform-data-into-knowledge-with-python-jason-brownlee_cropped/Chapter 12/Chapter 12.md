# Chapter 12

# Covariance and Correlation

There may be complex and unknown relationships between the variables in your dataset. It is important to discover and quantify the degree to which variables in your dataset are dependent upon each other. This knowledge can help you better prepare your data to meet the expectations of machine learning algorithms, such as linear regression, whose performance will degrade with the presence of these interdependencies. In this tutorial, you will discover that correlation is the statistical summary of the relationship between variables and how to calculate it for different types variables and relationships. After completing this tutorial, you will know:

- How to calculate a covariance matrix to summarize the linear relationship between two or more variables.
- How to calculate the covariance to summarize the linear relationship between two variables.
- How to calculate the Pearson's correlation coefficient to summarize the linear relationship between two variables.

Let's get started.

## 12.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- What is Correlation?
- Test Dataset
- Covariance
- Pearson's Correlation

## 12.2 What is Correlation?

Variables within a dataset can be related for lots of reasons. For example:

One variable could cause or depend on the values of another variable.

- One variable could be lightly associated with another variable.
- Two variables could depend on a third unknown variable.

It can be useful in data analysis and modeling to better understand the relationships between variables. The statistical relationship between two variables is referred to as their correlation. A correlation could be positive, meaning both variables move in the same direction, or negative, meaning that when one variable's value increases, the other variables' values decrease. Correlation can also be neural or zero, meaning that the variables are unrelated.

- Positive Correlation: Both variables change in the same direction.
- Neutral Correlation: No relationship in the change of the variables.
- Negative Correlation: Variables change in opposite directions.

The performance of some algorithms can deteriorate if two or more variables are tightly related, called multicollinearity. An example is linear regression, where one of the offending correlated variables should be removed in order to improve the skill of the model. We may also be interested in the correlation between input variables with the output variable in order provide insight into which variables may or may not be relevant as input for developing a model.

The structure of the relationship may be known, e.g. it may be linear, or we may have no idea whether a relationship exists between variables or what structure it may take. Depending what is known about the relationship and the distribution of the variables, different correlation scores can be calculated. In this tutorial, we will look at one score for variables that have a Gaussian distribution and a linear relationship and another that does not assume a distribution and will report on any monotonic (increasing or decreasing) relationship.

## 12.3 Test Dataset

Before we look at correlation methods, let's define a dataset we can use to test the methods. We will generate 1,000 samples of two two variables with a strong positive correlation. The first variable will be random numbers drawn from a Gaussian distribution with a mean of 100 and a standard deviation of 20. The second variable will be values from the first variable with Gaussian noise added with a mean of a 50 and a standard deviation of 10.

We will use the randn() function to generate random Gaussian values with a mean of 0 and a standard deviation of 1, then multiply the results by our own standard deviation and add the mean to shift the values into the preferred range. The pseudorandom number generator is seeded to ensure that we get the same sample of numbers each time the code is run.

```
# generate related variables
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
# seed random number generator
seed(1)
# prepare data
```

```
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
# plot
pyplot.scatter(data1, data2)
pyplot.show()
```

Listing 12.1: Example of preparing a test dataset with correlated variables.

Running the example first prints the mean and standard deviation for each variable.

```
data1: mean=100.776 stdv=19.620
data2: mean=151.050 stdv=22.358
```

Listing 12.2: Sample output from preparing a test dataset with correlated variables.

A scatter plot of the two variables is created. Because we contrived the dataset, we know there is a relationship between the two variables. This is clear when we review the generated scatter plot where we can see an increasing trend.

![](_page_2_Figure_7.jpeg)

Figure 12.1: Scatter plot of the test correlation dataset.

Before we look at calculating some correlation scores, we must first look at an important statistical building block, called covariance.

## 12.4 Covariance

Variables can be related by a linear relationship. This is a relationship that is consistently additive across the two data samples. This relationship can be summarized between two variables, called the covariance. It is calculated as the average of the product between the values from each sample, where the values haven been centered (had their mean subtracted). The calculation of the sample covariance is as follows:

$$cov(x,y) = \frac{1}{n} \times \sum_{i=1}^{n} (x_i - mean(x)) \times (y_i - mean(y)) \qquad (12.1)$$

The use of the mean in the calculation suggests the need for each data sample to have a Gaussian or Gaussian-like distribution. The sign of the covariance can be interpreted as whether the two variables change in the same direction (positive) or change in different directions (negative). The magnitude of the covariance is not easily interpreted. A covariance value of zero indicates that both variables are completely independent. The cov() NumPy function can be used to calculate a covariance matrix between two or more variables.

```
...
# calculate the covariance between two samples
covariance = cov(data1, data2)
```

Listing 12.3: Example of calculating covariance between two samples.

The diagonal of the matrix contains the covariance between each variable and itself. The other values in the matrix represent the covariance between the two variables; in this case, the remaining two values are the same given that we are calculating the covariance for only two variables. We can calculate the covariance matrix for the two variables in our test problem. The complete example is listed below.

```
# calculate the covariance between two variables
from numpy.random import randn
from numpy.random import seed
from numpy import cov
# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
# calculate covariance matrix
covariance = cov(data1, data2)
print(covariance)
```

Listing 12.4: Example of calculating covariance on the test dataset.

The covariance and covariance matrix are used widely within statistics and multivariate analysis to characterize the relationships between two or more variables. Running the example calculates and prints the covariance matrix. Because the dataset was contrived with each variable drawn from a Gaussian distribution and the variables linearly correlated, covariance is a reasonable method for describing the relationship. The covariance between the two variables is 389.75. We can see that it is positive, suggesting the variables change in the same direction as we expect.

| [[385.33297729 389.7545618 ] |  |
|------------------------------|--|
| [389.7545618 500.38006058]]  |  |

Listing 12.5: Sample output from calculating covariance on the test dataset.

A problem with covariance as a statistical tool alone is that it is challenging to interpret. This leads us to the Pearson's correlation coefficient next.

## 12.5 Pearson's Correlation

The Pearson's correlation coefficient (named for Karl Pearson) can be used to summarize the strength of the linear relationship between two data samples. The Pearson's correlation coefficient is calculated as the covariance of the two variables divided by the product of the standard deviation of each data sample. It is the normalization of the covariance between the two variables to give an interpretable score.

Pearson's correlation coefficient = 
$$\frac{cov(x,y)}{stdev(x) \times stdev(y)}$$
 (12.2)

The use of mean and standard deviation in the calculation suggests the need for the two data samples to have a Gaussian or Gaussian-like distribution. The result of the calculation, the correlation coefficient can be interpreted to understand the relationship. The coefficient returns a value between -1 and 1 that represents the limits of correlation from a full negative correlation to a full positive correlation. A value of 0 means no correlation. The value must be interpreted, where often a value below -0.5 or above 0.5 indicates a notable correlation, and values below those values suggests a less notable correlation. See the table below to help with interpretation the correlation coefficient.

| $\mathbf{L} \mathbf{L} \mathbf{L} \mathbf{L} \mathbf{L}$ |                                           |  |  |  |  |
|----------------------------------------------------------|-------------------------------------------|--|--|--|--|
| Correlation Coefficient<br>for an Indirect Relationship  | Relationship Strength<br>of the Variables |  |  |  |  |
| 0.0                                                      | None/trivial                              |  |  |  |  |
| $-0.1$                                                   | Weak/small                                |  |  |  |  |
| $-0.3$                                                   | Moderate/medium                           |  |  |  |  |
| $-0.5$                                                   | Strong/large                              |  |  |  |  |
| $-1.0$                                                   | Perfect                                   |  |  |  |  |
|                                                          |                                           |  |  |  |  |

| TABLE 7.1 |  |  |
|-----------|--|--|
|           |  |  |

Figure 12.2: Table of correlation coefficient values and their interpretation. Taken from Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach.

The Pearson's correlation is a statistical hypothesis test that does assume that there is no relationship between the samples (null hypothesis). The p-value can be interpreted as follows:

- p-value ≤ alpha: significant result, reject null hypothesis, some relationship (H1).
- p-value > alpha: not significant result, fail to reject null hypothesis, no relationship (H0).

The pearsonr() SciPy function can be used to calculate the Pearson's correlation coefficient between two data samples with the same length. We can calculate the correlation between the two variables in our test problem. The complete example is listed below.

```
# calculate the pearson's correlation between two variables
from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr
# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
# calculate Pearson's correlation
corr, p = pearsonr(data1, data2)
# display the correlation
print('Pearsons correlation: %.3f' % corr)
# interpret the significance
alpha = 0.05
if p > alpha:
 print('No correlation (fail to reject H0)')
else:
 print('Some correlation (reject H0)')
```

Listing 12.6: Example of calculating correlation on the test dataset.

Running the example calculates and prints the Pearson's correlation coefficient and interprets the p-value. We can see that the two variables are positively correlated and that the correlation is 0.888. This suggests a high level of correlation (as we expected).

Pearsons correlation: 0.888 Some correlation (reject H0)

Listing 12.7: Sample output from calculating correlation on the test dataset.

The Pearson's correlation coefficient can be used to evaluate the relationship between more than two variables. This can be done by calculating a matrix of the relationships between each pair of variables in the dataset. The result is a symmetric matrix called a correlation matrix with a value of 1.0 along the diagonal as each column always perfectly correlates with itself.

# 12.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Generate your own datasets with positive and negative relationships and calculate both correlation coefficients.
- Write functions to calculate Pearson's correlation coefficient for a provided dataset.
- Load a standard machine learning dataset and calculate correlation coefficients between all pairs of real-valued variables.

If you explore any of these extensions, I'd love to know.

# 12.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 12.7.1 API

- numpy.cov API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html>
- scipy.stats.pearsonr API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html>

#### 12.7.2 Articles

- Correlation and dependence on Wikipedia. [https://en.wikipedia.org/wiki/Correlation\\_and\\_dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence)
- Covariance on Wikipedia. <https://en.wikipedia.org/wiki/Covariance>
- Pearson's correlation coefficient on Wikipedia. [https://en.wikipedia.org/wiki/Pearson\\_correlation\\_coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

# 12.8 Summary

In this tutorial, you discovered that correlation is the statistical summary of the relationship between variables and how to calculate it for different types variables and relationships. Specifically, you learned:

- How to calculate a covariance matrix to summarize the linear relationship between two or more variables.
- How to calculate the covariance to summarize the linear relationship between two variables.
- How to calculate the Pearson's correlation coefficient to summarize the linear relationship between two variables.

#### 12.8.1 Next

In the next section, you will discover how to calculate statistical hypothesis tests in Python.
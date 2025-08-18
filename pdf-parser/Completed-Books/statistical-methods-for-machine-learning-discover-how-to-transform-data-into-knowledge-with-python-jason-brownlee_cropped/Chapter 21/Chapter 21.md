# Chapter 21

# Confidence Intervals

Much of machine learning involves estimating the performance of a machine learning algorithm on unseen data. Confidence intervals are a way of quantifying the uncertainty of an estimate. They can be used to add a bounds or likelihood on a population parameter, such as a mean, estimated from a sample of independent observations from the population. In this tutorial, you will discover confidence intervals and how to calculate confidence intervals in practice. After completing this tutorial, you will know:

- That a confidence interval is a bounds on an estimate of a population parameter.
- That the confidence interval for the estimated skill of a classification method can be calculated directly.
- That the confidence interval for any arbitrary population statistic can be estimated in a distribution-free way using the bootstrap.

Let's get started.

## 21.1 Tutorial Overview

This tutorial is divided into 3 parts; they are:

- 1. What is a Confidence Interval?
- 2. Interval for Classification Accuracy
- 3. Nonparametric Confidence Interval

## 21.2 What is a Confidence Interval?

A confidence interval is a bounds on the estimate of a population variable. It is an interval statistic used to quantify the uncertainty on an estimate.

A confidence interval is used to contain an unknown characteristic of the population or process. The quantity of interest might be a population property or "parameter", such as the mean or standard deviation of the population or process.

— Page 3, Statistical Intervals: A Guide for Practitioners and Researchers, 2017.

A confidence interval is different from a tolerance interval that describes the bounds of data sampled from the distribution. It is also different from a prediction interval that describes the bounds on a single observation. Instead, the confidence interval provides bounds on a population parameter, such as a mean, standard deviation, or similar. In applied machine learning, we may wish to use confidence intervals in the presentation of the skill of a predictive model.

For example, a confidence interval could be used in presenting the skill of a classification model, which could be stated as:

Given the sample, there is a 95% likelihood that the range x to y covers the true model accuracy.

or

The accuracy of the model was x +/- y at the 95% confidence level.

Confidence intervals can also be used in the presentation of the error of a regression predictive model; for example:

There is a 95% likelihood that the range x to y covers the true error of the model.

or

The error of the model was x +/- y at the 95% confidence level.

The choice of 95% confidence is very common in presenting confidence intervals, although other less common values are used, such as 90% and 99.7%. In practice, you can use any value you prefer.

The 95% confidence interval (CI) is a range of values calculated from our data, that most likely, includes the true value of what we're estimating about the population.

— Page 4, Introduction to the New Statistics: Estimation, Open Science, and Beyond, 2016.

The value of a confidence interval is its ability to quantify the uncertainty of the estimate. It provides both a lower and upper bound and a likelihood. Taken as a radius measure alone, the confidence interval is often referred to as the margin of error and may be used to graphically depict the uncertainty of an estimate on graphs through the use of error bars. Often, the larger the sample from which the estimate was drawn, the more precise the estimate and the smaller (better) the confidence interval.

- Smaller Confidence Interval: A more precise estimate.
- Larger Confidence Interval: A less precise estimate.

We can also say that the CI tells us how precise our estimate is likely to be, and the margin of error is our measure of precision. A short CI means a small margin of error and that we have a relatively precise estimate [...] A long CI means a large margin of error and that we have a low precision

— Page 4, Introduction to the New Statistics: Estimation, Open Science, and Beyond, 2016.

Confidence intervals belong to a field of statistics called estimation statistics that can be used to present and interpret experimental results instead of, or in addition to, statistical significance tests.

Estimation gives a more informative way to analyze and interpret results. [...] Knowing and thinking about the magnitude and precision of an effect is more useful to quantitative science than contemplating the probability of observing data of at least that extremity, assuming absolutely no effect.

— Estimation statistics should replace significance testing, 2016.

Confidence intervals may be preferred in practice over the use of statistical significance tests. The reason is that they are easier for practitioners and stakeholders to relate directly to the domain. They can also be interpreted and used to compare machine learning models.

These estimates of uncertainty help in two ways. First, the intervals give the consumers of the model an understanding about how good or bad the model may be. [...] In this way, the confidence interval helps gauge the weight of evidence available when comparing models. The second benefit of the confidence intervals is to facilitate trade-offs between models. If the confidence intervals for two models significantly overlap, this is an indication of (statistical) equivalence between the two and might provide a reason to favor the less complex or more interpretable model.

— Page 416, Applied Predictive Modeling, 2013.

Now that we know what a confidence interval is, let's look at a few ways that we can calculate them for predictive models.

## 21.3 Interval for Classification Accuracy

Classification problems are those where a label or class outcome variable is predicted given some input data. It is common to use classification accuracy or classification error (the inverse of accuracy) to describe the skill of a classification predictive model. For example, a model that makes correct predictions of the class outcome variable 75% of the time has a classification accuracy of 75%, calculated as:

$$accuracy = \frac{\text{total correct predictions}}{\text{total predictions made}} \times 100 \tag{21.1}$$

This accuracy can be calculated based on a hold-out dataset not seen by the model during training, such as a validation or test dataset. Classification accuracy or classification error is a proportion or a ratio. It describes the proportion of correct or incorrect predictions made by the model. Each prediction is a binary decision that could be correct or incorrect. Technically, this is called a Bernoulli trial, named for Jacob Bernoulli. The proportions in a Bernoulli trial have a specific distribution called a binomial distribution. Thankfully, with large sample sizes (e.g. more than 30), we can approximate the distribution with a Gaussian.

In statistics, a succession of independent events that either succeed or fail is called a Bernoulli process. [...] For large N, the distribution of this random variable approaches the normal distribution.

— Page 148, Data Mining: Practical Machine Learning Tools and Techniques, Second Edition, 2005.

We can use the assumption of a Gaussian distribution of the proportion (i.e. the classification accuracy or error) to easily calculate the confidence interval. In the case of classification error, the radius of the interval can be calculated as:

$$interval = z \times \sqrt{\frac{error \times (1 - error)}{n}} \tag{21.2}$$

In the case of classification accuracy, the radius of the interval can be calculated as:

$$interval = z \times \sqrt{\frac{accuracy \times (1 - accuracy)}{n}} \tag{21.3}$$

Where interval is the radius of the confidence interval, error and accuracy are classification error and classification accuracy respectively, n is the size of the sample, and z is a critical value from the Gaussian distribution. Technically, this is called the Binomial proportion confidence interval. Commonly used critical values from the Gaussian distribution and their corresponding significance level are as follows:

- 1.64 (90%)
- 1.96 (95%)
- 2.33 (98%)
- 2.58 (99%)

Consider a model with an error of 20%, or 0.2 (error = 0.2), on a validation dataset with 50 examples (n = 50). We can calculate the 95% confidence interval (z = 1.96) as follows:

```
# binomial confidence interval
from math import sqrt
# calculate the interval
interval = 1.96 * sqrt( (0.2 * (1 - 0.2)) / 50)
print('%.3f' % interval)
```

Listing 21.1: Example of calculating a confidence interval with 50 samples.

Running the example, we see the calculated radius of the confidence interval calculated and printed.

0.111

Listing 21.2: Sample output from calculating a confidence interval with 50 samples.

We can then make claims such as:

The classification error of the model is 20% +/- 11% The true classification error of the model is likely between 9% and 31%.

We can see the impact that the sample size has on the precision of the estimate in terms of the radius of the confidence interval.

```
# binomial confidence interval
from math import sqrt
interval = 1.96 * sqrt( (0.2 * (1 - 0.2)) / 100)
print('%.3f' % interval)
```

Listing 21.3: Example of calculating a confidence interval with 100 samples.

Running the example shows that the confidence interval drops to about 7%, increasing the precision of the estimate of the models skill.

#### 0.078

Listing 21.4: Sample output from calculating a confidence interval with 100 samples.

Remember that the confidence interval is a likelihood over a range. The true model skill may lie outside of the range.

In fact, if we repeated this experiment over and over, each time drawing a new sample S, containing [...] new examples, we would find that for approximately 95% of these experiments, the calculated interval would contain the true error. For this reason, we call this interval the 95% confidence interval estimate

— Page 131, Machine Learning, 1997.

The proportion confint() Statsmodels function an implementation of the binomial proportion confidence interval. By default, it makes the Gaussian assumption for the Binomial distribution, although other more sophisticated variations on the calculation are supported. The function takes the count of successes (or failures), the total number of trials, and the significance level as arguments and returns the lower and upper bound of the confidence interval. The example below demonstrates this function in a hypothetical case where a model made 88 correct predictions out of a dataset with 100 instances and we are interested in the 95% confidence interval (provided to the function as a significance of 0.05).

```
# calculate the confidence interval
from statsmodels.stats.proportion import proportion_confint
# calculate the interval
lower, upper = proportion_confint(88, 100, 0.05)
print('lower=%.3f, upper=%.3f' % (lower, upper))
```

Listing 21.5: Example of calculating a confidence interval with a function.

Running the example prints the lower and upper bounds on the model's classification accuracy.

lower=0.816, upper=0.944

Listing 21.6: Sample output from calculating a confidence interval with a function.

## 21.4 Nonparametric Confidence Interval

Often we do not know the distribution for a chosen performance measure. Alternately, we may not know the analytical way to calculate a confidence interval for a skill score.

The assumptions that underlie parametric confidence intervals are often violated. The predicted variable sometimes isn't normally distributed, and even when it is, the variance of the normal distribution might not be equal at all levels of the predictor variable.

#### — Page 326, Empirical Methods for Artificial Intelligence, 1995.

In these cases, the bootstrap resampling method can be used as a nonparametric method for calculating confidence intervals, nominally called bootstrap confidence intervals. The bootstrap is a simulated Monte Carlo method where samples are drawn from a fixed finite dataset with replacement and a parameter is estimated on each sample. This procedure leads to a robust estimate of the true population parameter via sampling. The bootstrap method was covered in detail in Chapter 17. We can demonstrate this with the following pseudocode.

```
statistics = []
for i in bootstraps:
 sample = select_sample_with_replacement(data)
 stat = calculate_statistic(sample)
 statistics.append(stat)
```

Listing 21.7: Pseudocode for estimating a statistic using the bootstrap.

The procedure can be used to estimate the skill of a predictive model by fitting the model on each sample and evaluating the skill of the model on those samples not included in the sample. The mean or median skill of the model can then be presented as an estimate of the model skill when evaluated on unseen data. Confidence intervals can be added to this estimate by selecting observations from the sample of skill scores at specific percentiles.

Recall that a percentile is an observation value drawn from the sorted sample where a percentage of the observations in the sample fall. For example, the 70th percentile of a sample indicates that 70% of the samples fall below that value. The 50th percentile is the median or middle of the distribution. First, we must choose a significance level for the confidence level, such as 95%, represented as 5.0% (e.g. 100 - 95). Because the confidence interval is symmetric around the median, we must choose observations at the 2.5th percentile and the 97.5th percentiles to give the full range.

We can make the calculation of the bootstrap confidence interval concrete with a worked example. Let's assume we have a dataset of 1,000 observations of values between 0.5 and 1.0 drawn from a uniform distribution.

```
...
# generate dataset
dataset = 0.5 + rand(1000) * 0.5
```

Listing 21.8: Example of generating Gaussian random numbers.

We will perform the bootstrap procedure 100 times and draw samples of 1,000 observations from the dataset with replacement. We will estimate the mean of the population as the statistic we will calculate on the bootstrap samples. This could just as easily be a model evaluation.

```
...
# bootstrap
scores = list()
for _ in range(100):
 # bootstrap sample
 indices = randint(0, 1000, 1000)
 sample = dataset[indices]
 # calculate and store statistic
 statistic = mean(sample)
 scores.append(statistic)
```

Listing 21.9: Example of estimating the mean using the bootstrap.

Once we have a sample of bootstrap statistics, we can calculate the central tendency. We will use the median or 50th percentile as we do not assume any distribution.

... # calculate the median print('median=%.3f' % median(scores))

Listing 21.10: Example of printing the median.

We can then calculate the confidence interval as the middle 95% of observed statistical values centered around the median.

```
...
# calculate 95% confidence intervals (100 - alpha)
alpha = 5.0
```

Listing 21.11: Define the level of confidence.

First, the desired lower percentile is calculated based on the chosen confidence interval. Then the observation at this percentile is retrieved from the sample of bootstrap statistics.

```
...
# calculate lower percentile (e.g. 2.5)
lower_p = alpha / 2.0
# retrieve observation at lower percentile
lower = max(0.0, percentile(scores, lower_p))
```

Listing 21.12: Example of calculating the lower-bound on the confidence interval.

We do the same thing for the upper boundary of the confidence interval.

```
...
# calculate upper percentile (e.g. 97.5)
upper_p = (100 - alpha) + (alpha / 2.0)
# retrieve observation at upper percentile
upper = min(1.0, percentile(scores, upper_p))
```

Listing 21.13: Example of calculating the upper-bound on the confidence interval.

The complete example is listed below.

```
# bootstrap confidence intervals
from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
```

```
from numpy import mean
from numpy import median
from numpy import percentile
# seed the random number generator
seed(1)
# generate dataset
dataset = 0.5 + rand(1000) * 0.5
# bootstrap
scores = list()
for _ in range(100):
 # bootstrap sample
 indices = randint(0, 1000, 1000)
 sample = dataset[indices]
 # calculate and store statistic
 statistic = mean(sample)
 scores.append(statistic)
print('50th percentile (median) = %.3f' % median(scores))
# calculate 95% confidence intervals (100 - alpha)
alpha = 5.0
# calculate lower percentile (e.g. 2.5)
lower_p = alpha / 2.0
# retrieve observation at lower percentile
lower = max(0.0, percentile(scores, lower_p))
print('%.1fth percentile = %.3f' % (lower_p, lower))
# calculate upper percentile (e.g. 97.5)
upper_p = (100 - alpha) + (alpha / 2.0)
# retrieve observation at upper percentile
upper = min(1.0, percentile(scores, upper_p))
print('%.1fth percentile = %.3f' % (upper_p, upper))
```

Listing 21.14: Example of calculating a confidence interval using the bootstrap.

Running the example summarizes the distribution of bootstrap sample statistics including the 2.5th, 50th (median) and 97.5th percentile.

```
50th percentile (median) = 0.750
2.5th percentile = 0.741
97.5th percentile = 0.757
```

Listing 21.15: Sample output from calculating a confidence interval using the bootstrap.

We can then use these observations to make a claim about the sample distribution, such as:

There is a 95% likelihood that the range 0.741 to 0.757 covers the true statistic median.

## 21.5 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Test each confidence interval method on your own small contrived test datasets.
- Find 3 research papers that demonstrate the use of each confidence interval method.

 Develop a function to calculate a bootstrap confidence interval for a given sample of machine learning skill scores.

If you explore any of these extensions, I'd love to know.

# 21.6 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 21.6.1 Books

- Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis, 2011. <http://amzn.to/2oQW6No>
- Introduction to the New Statistics: Estimation, Open Science, and Beyond, 2016. <http://amzn.to/2HhrT0w>
- Statistical Intervals: A Guide for Practitioners and Researchers, 2017. <http://amzn.to/2G8w3IL>
- Applied Predictive Modeling, 2013. <http://amzn.to/2Fmrbib>
- Machine Learning, 1997. <http://amzn.to/2tr32Wb>
- Data Mining: Practical Machine Learning Tools and Techniques, Second Edition, 2005. <http://amzn.to/2G7sxhP>
- An Introduction to the Bootstrap, 1996. <http://amzn.to/2p2zUPl>
- Empirical Methods for Artificial Intelligence, 1995. <http://amzn.to/2FrFJgg>

#### 21.6.2 Papers

- Estimation statistics should replace significance testing, 2016. <https://www.nature.com/articles/nmeth.3729>
- Bootstrap Confidence Intervals, Statistical Science, 1996. [https://projecteuclid.org/download/pdf\\_1/euclid.ss/1032280214](https://projecteuclid.org/download/pdf_1/euclid.ss/1032280214)

#### 21.6.3 API

 statsmodels.stats.proportion.proportion confint API. [http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.prop](http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportion_confint.html)ortion\_ [confint.html](http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportion_confint.html)

#### 21.6.4 Articles

- Interval estimation on Wikipedia. [https://en.wikipedia.org/wiki/Interval\\_estimation](https://en.wikipedia.org/wiki/Interval_estimation)
- Confidence interval on Wikipedia. [https://en.wikipedia.org/wiki/Confidence\\_interval](https://en.wikipedia.org/wiki/Confidence_interval)
- Binomial proportion confidence interval on Wikipedia. [https://en.wikipedia.org/wiki/Binomial\\_proportion\\_confidence\\_interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)
- Confidence interval of RMSE on Cross Validated. <https://stats.stackexchange.com/questions/78079/confidence-interval-of-rmse>
- Bootstrapping on Wikipedia. [https://en.wikipedia.org/wiki/Bootstrapping\\_\(statistics\)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))

# 21.7 Summary

In this tutorial, you discovered confidence intervals and how to calculate confidence intervals in practice. Specifically, you learned:

- That a confidence interval is a bounds on an estimate of a population parameter.
- That the confidence interval for the estimated skill of a classification method can be calculated directly.
- That the confidence interval for any arbitrary population statistic can be estimated in a distribution-free way using the bootstrap.

#### 21.7.1 Next

In the next section, you will discover prediction intervals for the likely range for a point prediction.
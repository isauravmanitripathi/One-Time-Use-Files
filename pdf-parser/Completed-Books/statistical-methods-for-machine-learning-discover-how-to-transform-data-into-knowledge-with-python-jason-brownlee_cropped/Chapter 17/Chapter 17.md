# Chapter 17

# Estimation with Bootstrap

The bootstrap method is a resampling technique used to estimate statistics on a population by sampling a dataset with replacement. It can be used to estimate summary statistics such as the mean or standard deviation. It is used in applied machine learning to estimate the skill of machine learning models when making predictions on data not included in the training data.

A desirable property of the results from estimating machine learning model skill is that the estimated skill can be presented with confidence intervals, a feature not readily available with other methods such as cross-validation. In this tutorial, you will discover the bootstrap resampling method for estimating the skill of machine learning models on unseen data. After completing this tutorial, you will know:

- The bootstrap method involves iteratively resampling a dataset with replacement.
- That when using the bootstrap you must choose the size of the sample and the number of repeats.
- The scikit-learn provides a function that you can use to resample a dataset for the bootstrap method.

Let's get started.

### 17.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- 1. Bootstrap Method
- 2. Configuration of the Bootstrap
- 3. Worked Example
- 4. Bootstrap in Python

# 17.2 Bootstrap Method

The bootstrap method is a statistical technique for estimating quantities about a population by averaging estimates from multiple small data samples. Importantly, samples are constructed by drawing observations from a large data sample one at a time and returning them to the data sample after they have been chosen. This allows a given observation to be included in a given small sample more than once. This approach to sampling is called sampling with replacement. The process for building one sample can be summarized as follows:

```
1. Choose the size of the sample.
2. While the size of the sample is less than the chosen size
 2.1 Randomly select an observation from the dataset
 2.2 Add it to the sample
```

Listing 17.1: Pseudocode for sampling.

The bootstrap method can be used to estimate a quantity of a population. This is done by repeatedly taking small samples, calculating the statistic, and taking the average of the calculated statistics. We can summarize this procedure as follows:

```
1. Choose a number of bootstrap samples to perform
2. Choose a sample size
3. For each bootstrap sample
 3.1 Draw a sample with replacement with the chosen size
 3.2 Calculate the statistic on the sample
4. Calculate the mean of the calculated sample statistics.
```

Listing 17.2: Pseudocode for the bootstrap for estimating a statistic.

The procedure can also be used to estimate the skill of a machine learning model.

The bootstrap is a widely applicable and extremely powerful statistical tool that can be used to quantify the uncertainty associated with a given estimator or statistical learning method.

— Page 187, An Introduction to Statistical Learning, 2013.

This is done by training the model on the sample and evaluating the skill of the model on those samples not included in the sample. These samples not included in a given sample are called the out-of-bag samples, or OOB for short. This procedure of using the bootstrap method to estimate the skill of the model can be summarized as follows:

```
1. Choose a number of bootstrap samples to perform
2. Choose a sample size
3. For each bootstrap sample
 3.1 Draw a sample with replacement with the chosen size
 3.2 Fit a model on the data sample
 3.3 Estimate the skill of the model on the out-of-bag sample.
4. Calculate the mean of the sample of model skill estimates.
```

Listing 17.3: Pseudocode for the bootstrap for estimating model skill.

The samples not selected are usually referred to as the "out-of-bag" samples. For a given iteration of bootstrap resampling, a model is built on the selected samples and is used to predict the out-of-bag samples.

— Page 72, Applied Predictive Modeling, 2013.

Importantly, any data preparation prior to fitting the model or tuning of the hyperparameter of the model must occur within the for-loop on the data sample. This is to avoid data leakage where knowledge of the test dataset is used to improve the model. This, in turn, can result in an optimistic estimate of the model skill. A useful feature of the bootstrap method is that the resulting sample of estimations often forms a Gaussian distribution. In additional to summarizing this distribution with a central tendency, measures of variance can be given, such as standard deviation and standard error. Further, a confidence interval can be calculated and used to bound the presented estimate. This is useful when presenting the estimated skill of a machine learning model.

# 17.3 Configuration of the Bootstrap

There are two parameters that must be chosen when performing the bootstrap: the size of the sample and the number of repetitions of the procedure to perform.

#### 17.3.1 Sample Size

In machine learning, it is common to use a sample size that is the same as the original dataset.

The bootstrap sample is the same size as the original dataset. As a result, some samples will be represented multiple times in the bootstrap sample while others will not be selected at all.

— Page 72, Applied Predictive Modeling, 2013.

If the dataset is enormous and computational efficiency is an issue, smaller samples can be used, such as 50% or 80% of the size of the dataset.

#### 17.3.2 Repetitions

The number of repetitions must be large enough to ensure that meaningful statistics, such as the mean, standard deviation, and standard error can be calculated on the sample. A minimum might be 20 or 30 repetitions. A smaller number of repeats can be used, which will further add variance to the estimated statistic. Ideally, the sample of estimates would be as large as possible given the time resources, with hundreds or thousands of repeats.

### 17.4 Worked Example

We can make the bootstrap procedure concrete with a small worked example. We will work through one iteration of the procedure. Imagine we have a dataset with 6 observations:

```
[0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
```

#### 17.5. Bootstrap in Python 139

The first step is to choose the size of the sample. Here, we will use 4. Next, we must randomly choose the first observation from the dataset. Let's choose 0.2.

sample = [0.2]

Listing 17.5: Example of sampling one value from the dataset.

This observation is returned to the dataset and we repeat this step 3 more times.

sample = [0.2, 0.1, 0.2, 0.6]

Listing 17.6: Example of a subsample with replacement from the dataset.

We now have our data sample. The example purposefully demonstrates that the same value can appear zero, one or more times in the sample. Here the observation 0.2 appears twice. An estimate can then be calculated on the drawn sample.

statistic = calculation([0.2, 0.1, 0.2, 0.6])

Listing 17.7: Example of calculating a statistic on the subsample.

Those observations not chosen for the sample may be used as out of sample observations.

oob = [0.3, 0.4, 0.5]

Listing 17.8: Example of the out of bag (oob) subsample.

In the case of evaluating a machine learning model, the model is fit on the drawn sample and evaluated on the out-of-bag sample.

train = [0.2, 0.1, 0.2, 0.6] test = [0.3, 0.4, 0.5] model = fit(train) statistic = evaluate(model, test)

Listing 17.9: Example of training and evaluating a model.

That concludes one repeat of the procedure. It can be repeated 30 or more times to give a sample of calculated statistics.

statistics = [...]

Listing 17.10: Example of a list of sample statistics.

This sample of statistics can then be summarized by calculating a mean, standard deviation, or other summary values to give a final usable estimate of the statistic.

estimate = mean([...])

Listing 17.11: Example of estimating the population statistic from the sample statistics.

## 17.5 Bootstrap in Python

We do not have to implement the bootstrap method manually. The scikit-learn library provides an implementation that will create a single bootstrap sample of a dataset. The resample() scikit-learn function can be used. It takes as arguments the data array, whether or not to sample with replacement, the size of the sample, and the seed for the pseudorandom number generator used prior to the sampling. For example, we can create a bootstrap that creates a sample with replacement with 4 observations and uses a value of 1 for the pseudorandom number generator.

```
...
# resample with replacement
boot = resample(data, replace=True, n_samples=4, random_state=1)
```

Listing 17.12: Example of resampling with replacement.

Unfortunately, the API does not include any mechanism to easily gather the out-of-bag observations that could be used as a test set to evaluate a fit model. At least in the univariate case we can gather the out-of-bag observations using a simple Python list comprehension.

```
...
# out of bag observations
oob = [x for x in data if x not in boot]
```

Listing 17.13: Example of collecting an out of bag subsample.

We can tie all of this together with our small dataset used in the worked example of the prior section.

```
# scikit-learn bootstrap
from sklearn.utils import resample
# data sample
data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# prepare bootstrap sample
boot = resample(data, replace=True, n_samples=4, random_state=1)
print('Bootstrap Sample: %s' % boot)
# out of bag observations
oob = [x for x in data if x not in boot]
print('OOB Sample: %s' % oob)
```

Listing 17.14: Example of estimating a population statistic with the bootstrap.

Running the example prints the observations in the bootstrap sample and those observations in the out-of-bag sample.

Bootstrap Sample: [0.6, 0.4, 0.5, 0.1] OOB Sample: [0.2, 0.3]

Listing 17.15: Example output from estimating a population statistic with the bootstrap.

# 17.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- List 3 summary statistics that you could estimate using the bootstrap method.
- Find 3 research papers that use the bootstrap method to evaluate the performance of machine learning models.
- Implement your own function to create a sample and an out-of-bag sample with the bootstrap method.

If you explore any of these extensions, I'd love to know.

# 17.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 17.7.1 Books

- Applied Predictive Modeling, 2013. <http://amzn.to/2Fmrbib>
- An Introduction to Statistical Learning, 2013. <http://amzn.to/2FkHqvW>
- An Introduction to the Bootstrap, 1994. <http://amzn.to/2G0Yatr>

#### 17.7.2 API

- sklearn.utils.resample API. <http://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html>
- sklearn.model selection API. [http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model\\_selection](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)

#### 17.7.3 Articles

- Resampling (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Resampling\\_\(statistics\)](https://en.wikipedia.org/wiki/Resampling_(statistics))
- Bootstrapping (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Bootstrapping\\_\(statistics\)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
- Rule of thumb for number of bootstrap samples, CrossValiated. <https://stats.stackexchange.com/questions/86040/rule-of-thumb-for-number-of-bootstrap-samples>

# 17.8 Summary

In this tutorial, you discovered the bootstrap resampling method for estimating the skill of machine learning models on unseen data. Specifically, you learned:

- The bootstrap method involves iteratively resampling a dataset with replacement.
- That when using the bootstrap you must choose the size of the sample and the number of repeats.
- The scikit-learn provides a function that you can use to resample a dataset for the bootstrap method.

#### 17.8.1 Next

In the next section, you will discover the k-fold cross-validation for estimating the skill of a learning model when making predictions on unseen data.
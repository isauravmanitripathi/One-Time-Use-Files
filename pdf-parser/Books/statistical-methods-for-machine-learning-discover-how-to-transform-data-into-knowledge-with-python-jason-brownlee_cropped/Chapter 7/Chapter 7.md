# Chapter 7

## Law of Large Numbers

We have an intuition that more observations are better. This is the same intuition behind the idea that if we collect more data, our sample of data will be more representative of the problem domain. There is a theorem in statistics and probability that supports this intuition that is a pillar of both of these fields and has important implications in applied machine learning. The name of this theorem is the law of large numbers. In this tutorial, you will discover the law of large numbers and why it is important in applied machine learning. After completing this tutorial, you will know:

- The law of large numbers supports the intuition that the sample becomes more representative of the population as its size is increased.
- How to develop a small example in Python to demonstrate the decrease in error from the increase in sample size.
- The law of large numbers is critical for understanding the selection of training datasets, test datasets, and in the evaluation of model skill in machine learning.

Let's get started.

## 7.1 Tutorial Overview

This tutorial is divided into 3 parts; they are:

- 1. Law of Large Numbers
- 2. Worked Example
- 3. Implications in Machine Learning

## 7.2 Law of Large Numbers

The law of large numbers is a theorem from probability and statistics that suggests that the average result from repeating an experiment multiple times will better approximate the true or expected underlying result.

The law of large numbers explains why casinos always make money in the long run.

— Page 79, Naked Statistics: Stripping the Dread from the Data, 2014.

We can think of a trial of an experiment as one observation. The standalone and independent repetition of the experiment will perform multiple trials and lead to multiple observations. All sample observations for an experiment are drawn from an idealized population of observations.

- Observation: Result from one trial of an experiment.
- Sample: Group of results gathered from separate independent trials.
- Population: Space of all possible observations that could be seen from a trial.

Using these terms from statistics, we can say that as the size of the sample increases, the mean value of the sample will better approximate the mean or expected value in the population. As the sample size goes to infinity, the sample mean will converge to the population mean.

... a crowning achievement in probability, the law of large numbers. This theorem says that the mean of a large sample is close to the mean of the distribution.

— Page 76, All of Statistics: A Concise Course in Statistical Inference, 2004.

This is an important theoretical finding for statistics and probability, as well as for applied machine learning.

### 7.2.1 Independent and Identically Distributed

It is important to be clear that the observations in the sample must be independent. This means that the trial is run in an identical manner and does not depend on the results of any other trial. This is often reasonable and easy to achieve in computers, although can be difficult elsewhere (e.g. how do you achieve identically random rolls of a dice?). In statistics, this expectation is called independent and identically distributed, or IID, iid, or i.i.d. for short. This is to ensure that the samples are indeed drawn from the same underlying population distribution.

### 7.2.2 Regression to the Mean

The law of large numbers helps us understand why we cannot trust a single observation from an experiment in isolation. We expect that a single result or the mean result from a small sample is likely. That is close to the central tendency, the mean of the population distribution. It may not be; in fact, it may be very strange or unlikely. The law reminds us to repeat the experiment in order to develop a large and representative sample of observations before we start making inferences about what the result means.

As we increase the sample size, the finding or mean of the sample will move back toward the population mean, back toward the true underlying expected value. This is called regression to the mean or sometimes reversion to the mean. It is why we must be skeptical of inferences from small sample sizes, called small n.

### 7.2.3 Law of Truly Large Numbers

Related to the regression to the mean is the idea of the law of truly large numbers. This is the idea that when we start investigating or working with extremely large samples of observations, we increase the likelihood of seeing something strange. That by having so many samples of the underlying population distribution, the sample will contain some astronomically rare events.

Again, we must be wary not to make inferences from single cases. This is especially important to consider when running queries and investigating big data.

## 7.3 Worked Example

We can demonstrate the law of large numbers with a small worked example. First, we can design an idealized underlying distribution. We will use a Gaussian distribution with a mean of 50 and a standard deviation of 5. The expected value or mean of this population is therefore 50. Below is some code that generates a plot of this idealized distribution.

```
# idealized population distribution
from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
# x-axis for the plot
xaxis = arange(30, 70, 1)
# y-axis for the plot
yaxis = norm.pdf(xaxis, 50, 5)
# plot ideal population
pyplot.plot(xaxis, yaxis)
pyplot.show()
```

Listing 7.1: Example of an idealized Gaussian distribution.

Running the code creates a plot of the designed population with the familiar bell shape.

![](_page_3_Figure_1.jpeg)

Figure 7.1: Line plot of an idealized Gaussian distribution.

Now, we can pretend to forget everything that we know about the population and make independent random samples from the population. We can create samples of different sizes and calculate the mean. Given our intuition and the law of large numbers, we expect that as the size of the sample is increased, the sample mean will better approximate the population mean. The example below calculates samples of different sizes, estimates the mean and plots the errors in the mean from the expected mean (50).

```
# demonstrate the law of large numbers
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import array
from matplotlib import pyplot
# seed the random number generator
seed(1)
# sample sizes
sizes = list()
for x in range (10, 20000, 200):
 sizes.append(x)
# generate samples of different sizes and calculate their means
means = [mean(5 * randn(size) + 50) for size in sizes]
# plot sample mean error vs sample size
pyplot.scatter(sizes, array(means)-50)
```

#### pyplot.show()

Listing 7.2: Example of estimating the mean from different sized samples.

Running the example creates a plot that compares the size of the sample to the error of the sample mean from the population mean. Generally, we can see that larger sample sizes have less error, and we would expect this trend to continue, on average. We can also see that some sample means overestimate and some underestimate. Do not fall into the trap of assuming that the underestimate will fall on one side or another.

![](_page_4_Figure_4.jpeg)

Figure 7.2: Scatter plot of the error in the population mean vs sample size.

## 7.4 Implications in Machine Learning

The law of large numbers has important implications in applied machine learning. Let's take a moment to highlight a few of these implications.

### 7.4.1 Training Data

The data used to train the model must be representative of the observations from the domain. This really means that it must contain enough information to generalize to the true unknown and underlying distribution of the population. This is easy to conceptualize with a single input

variable for a model, but is also just as important when you have multiple input variables. There will be unknown relationships or dependencies between the input variables and together, the input data will represent a multivariate distribution from which observations will be drawn to comprise your training sample.

Keep this in mind during data collection, data cleaning, and data preparation. You may choose to exclude sections of the underlying population by setting hard limits on observed values (e.g. for outliers) where you expect data to be too sparse to model effectively.

### 7.4.2 Test Data

The thoughts given to the training dataset must also be given to the test dataset. This is often neglected with the blind use of 80/20 spits for train/test data or the blind use of 10-fold cross-validation, even on datasets where the size of 1/10th of the available data may not be a suitable representative of observations from the problem domain.

### 7.4.3 Model Skill Evaluation

Consider the law of large numbers when presenting the estimated skill of a model on unseen data. It provides a defense for not simply reporting or proceeding with a model based on a skill score from a single train/test evaluation. It highlights the need to develop a sample of multiple independent (or close to independent) evaluations of a given model such that the mean reported skill from the sample is an accurate enough estimate of population mean.

## 7.5 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Brainstorm two additional areas of machine learning where the law of large numbers applies.
- Find five research papers where you are skeptical of the results given the law of large numbers.
- Develop your own ideal distribution and samples and plot the relationship between sample size and sample mean error.

If you explore any of these extensions, I'd love to know.

## 7.6 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

### 7.6.1 Books

 Naked Statistics: Stripping the Dread from the Data, 2014. <http://amzn.to/2F5tVnX>

 All of Statistics: A Concise Course in Statistical Inference, 2004. <http://amzn.to/2FNFQns>

## 7.6.2 API

- scipy.stats.norm API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html>
- numpy.random.seed API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html>
- numpy.random.randn API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html>
- numpy.mean API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html>

## 7.6.3 Articles

- Law of large numbers on Wikipedia. [https://en.wikipedia.org/wiki/Law\\_of\\_large\\_numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
- Independent and identically distributed random variables on Wikipedia. [https://en.wikipedia.org/wiki/Independent\\_and\\_identically\\_distributed\\_rand](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables)om\_ [variables](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables)
- Law of truly large numbers on Wikipedia. [https://en.wikipedia.org/wiki/Law\\_of\\_truly\\_large\\_numbers](https://en.wikipedia.org/wiki/Law_of_truly_large_numbers)
- Regression toward the mean. [https://en.wikipedia.org/wiki/Regression\\_toward\\_the\\_mean](https://en.wikipedia.org/wiki/Regression_toward_the_mean)

## 7.7 Summary

In this tutorial, you discovered the law of large numbers and why it is important in applied machine learning. Specifically, you learned:

- The law of large numbers supports the intuition that the sample becomes more representative of the population as its size is increased.
- How to develop a small example in Python to demonstrate the decrease in error from the increase in sample size.
- The law of large numbers is critical for understanding the selection of training datasets, test datasets, and in the evaluation of model skill in machine learning.

## 7.7.1 Next

In the next section, you will discover the central limit theorem.
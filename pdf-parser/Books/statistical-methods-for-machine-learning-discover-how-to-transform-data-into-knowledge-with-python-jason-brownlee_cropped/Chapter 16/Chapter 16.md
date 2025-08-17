# Chapter 16

## Introduction to Resampling

Data is the currency of applied machine learning. Therefore, it is important that it is both collected and used effectively. Data sampling refers to statistical methods for selecting observations from the domain with the objective of estimating a population parameter. Whereas data resampling refers to methods for economically using a collected dataset to improve the estimate of the population parameter and help to quantify the uncertainty of the estimate. Both data sampling and data resampling are methods that are required in a predictive modeling problem. In this tutorial, you will discover statistical sampling and statistical resampling methods for gathering and making best use of data. After completing this tutorial, you will know:

- Sampling is an active process of gathering observations with the intent of estimating a population variable.
- Resampling is a methodology of economically using a data sample to improve the accuracy and quantify the uncertainty of a population parameter.
- Resampling methods, in fact, make use of a nested resampling method.

Let's get started.

### 16.1 Tutorial Overview

This tutorial is divided into 2 parts; they are:

- 1. Statistical Sampling
- 2. Statistical Resampling

### 16.2 Statistical Sampling

Each row of data represents an observation about something in the world. When working with data, we often do not have access to all possible observations. This could be for many reasons; for example:

It may difficult or expensive to make more observations.

- It may be challenging to gather all observations together.
- More observations are expected to be made in the future.

Observations made in a domain represent samples of some broader idealized and unknown population of all possible observations that could be made in the domain. This is a useful conceptualization as we can see the separation and relationship between observations and the idealized population. We can also see that, even if we intend to use big data infrastructure on all available data, that the data still represents a sample of observations from an idealized population. Nevertheless, we may wish to estimate properties of the population. We do this by using samples of observations.

Sampling consists of selecting some part of the population to observe so that one may estimate something about the whole population.

— Page 1, Sampling, Third Edition, 2012.

#### 16.2.1 How to Sample

Statistical sampling is the process of selecting subsets of examples from a population with the objective of estimating properties of the population. Sampling is an active process. There is a goal of estimating population properties and control over how the sampling is to occur. This control falls short of influencing the process that generates each observation, such as performing an experiment. As such, sampling as a field sits neatly between pure uncontrolled observation and controlled experimentation.

Sampling is usually distinguished from the closely related field of experimental design, in that in experiments one deliberately perturbs some part of the population in order to see what the effect of that action is. [...] Sampling is also usually distinguished from observational studies, in which one has little or no control over how the observations on the population were obtained.

— Pages 1-2, Sampling, Third Edition, 2012.

There are many benefits to sampling compared to working with fuller or complete datasets, including reduced cost and greater speed. In order to perform sampling, it requires that you carefully define your population and the method by which you will select (and possibly reject) observations to be a part of your data sample. This may very well be defined by the population parameters that you wish to estimate using the sample. Some aspects to consider prior to collecting a data sample include:

- Sample Goal. The population property that you wish to estimate using the sample.
- Population. The scope or domain from which observations could theoretically be made.
- Selection Criteria. The methodology that will be used to accept or reject observations in your sample.
- Sample Size. The number of observations that will constitute the sample.

Some obvious questions [...] are how best to obtain the sample and make the observations and, once the sample data are in hand, how best to use them to estimate the characteristics of the whole population. Obtaining the observations involves questions of sample size, how to select the sample, what observational methods to use, and what measurements to record.

— Page 1, Sampling, Third Edition, 2012.

Statistical sampling is a large field of study, but in applied machine learning, there may be three types of sampling that you are likely to use: simple random sampling, systematic sampling, and stratified sampling.

- Simple Random Sampling: Samples are drawn with a uniform probability from the domain.
- Systematic Sampling: Samples are drawn using a pre-specified pattern, such as at intervals.
- Stratified Sampling: Samples are drawn within pre-specified categories (i.e. strata).

Although these are the more common types of sampling that you may encounter, there are other techniques.

#### 16.2.2 Sampling Errors

Sampling requires that we make a statistical inference about the population from a small set of observations. We can generalize properties from the sample to the population. This process of estimation and generalization is much faster than working with all possible observations, but will contain errors. In many cases, we can quantify the uncertainty of our estimates and add errors bars, such as confidence intervals. There are many ways to introduce errors into your data sample. Two main types of errors include selection bias and sampling error.

- Selection Bias. Caused when the method of drawing observations skews the sample in some way.
- Sampling Error. Caused due to the random nature of drawing observations skewing the sample in some way.

Other types of errors may be present, such as systematic errors in the way observations or measurements are made. In these cases and more, the statistical properties of the sample may be different from what would be expected in the idealized population, which in turn may impact the properties of the population that are being estimated. Simple methods, such as reviewing raw observations, summary statistics, and visualizations can help expose simple errors, such as measurement corruption and the over- or underrepresentation of a class of observations. Nevertheless, care must be taken both when sampling and when drawing conclusions about the population while sampling.

#### 16.3 Statistical Resampling

Once we have a data sample, it can be used to estimate the population parameter. The problem is that we only have a single estimate of the population parameter, with little idea of the variability or uncertainty in the estimate. One way to address this is by estimating the population parameter multiple times from our data sample. This is called resampling.

Statistical resampling methods are procedures that describe how to economically use available data to estimate a population parameter. The result can be both a more accurate estimate of the parameter (such as taking the mean of the estimates) and a quantification of the uncertainty of the estimate (such as adding a confidence interval). Resampling methods are very easy to use, requiring little mathematical knowledge. They are methods that are easy to understand and implement compared to specialized statistical methods that may require deep technical skill in order to select and interpret.

The resampling methods [...] are easy to learn and easy to apply. They require no mathematics beyond introductory high-school algebra, but are applicable in an exceptionally broad range of subject areas.

— Page xiii, Resampling Methods: A Practical Guide to Data Analysis, 2005.

A downside of the methods is that they can be computationally very expensive, requiring tens, hundreds, or even thousands of resamples in order to develop a robust estimate of the population parameter.

The key idea is to resample form the original data — either directly or via a fitted model — to create replicate datasets, from which the variability of the quantiles of interest can be assessed without long-winded and error-prone analytical calculation. Because this approach involves repeating the original data analysis procedure with many replicate sets of data, these are sometimes called computer-intensive methods.

— Page 3, Bootstrap Methods and their Application, 1997.

Each new subsample from the original data sample is used to estimate the population parameter. The sample of estimated population parameters can then be considered with statistical tools in order to quantify the expected value and variance, providing measures of the uncertainty of the estimate. Statistical sampling methods can be used in the selection of a subsample from the original sample.

A key difference is that process must be repeated multiple times. The problem with this is that there will be some relationship between the samples as observations that will be shared across multiple subsamples. This means that the subsamples and the estimated population parameters are not strictly identical and independently distributed. This has implications for statistical tests performed on the sample of estimated population parameters downstream, i.e. paired statistical tests may be required. Two commonly used resampling methods that you may encounter are k-fold cross-validation and the bootstrap.

 Bootstrap. Samples are drawn from the dataset with replacement (allowing the same sample to appear more than once in the sample), where those instances not drawn into the data sample may be used for the test set.

 k-fold Cross-Validation. A dataset is partitioned into k groups, where each group is given the opportunity of being used as a held out test set leaving the remaining groups as the training set.

The k-fold cross-validation method specifically lends itself to use in the evaluation of predictive models that are repeatedly trained on one subset of the data and evaluated on a second held-out subset of the data.

Generally, resampling techniques for estimating model performance operate similarly: a subset of samples are used to fit a model and the remaining samples are used to estimate the efficacy of the model. This process is repeated multiple times and the results are aggregated and summarized. The differences in techniques usually center around the method in which subsamples are chosen.

— Page 69, Applied Predictive Modeling, 2013.

The bootstrap method can be used for the same purpose, but is a more general and simpler method intended for estimating a population parameter.

#### 16.4 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- List two examples where statistical sampling is required in a machine learning project.
- List two examples when statistical resampling is required in a machine learning project.
- Find a paper that uses a resampling method that in turn uses a nested statistical sampling method (hint: k-fold cross-validation and stratified sampling).

If you explore any of these extensions, I'd love to know.

#### 16.5 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 16.5.1 Books

- Sampling, Third Edition, 2012. <http://amzn.to/2HNgJAQ>
- Sampling Techniques, 3rd Edition, 1977. <http://amzn.to/2FMh8XF>
- Resampling Methods: A Practical Guide to Data Analysis, 2005. <http://amzn.to/2G6gMKP>

- An Introduction to the Bootstrap, 1994. <http://amzn.to/2praHye>
- Bootstrap Methods and their Application, 1997. <http://amzn.to/2FVsmVY>
- Applied Predictive Modeling, 2013. <http://amzn.to/2Fmrbib>

#### 16.5.2 Articles

- Sample (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Sample\\_\(statistics\)](https://en.wikipedia.org/wiki/Sample_(statistics))
- Simple random sample on Wikipedia. [https://en.wikipedia.org/wiki/Simple\\_random\\_sample](https://en.wikipedia.org/wiki/Simple_random_sample)
- Systematic sampling on Wikipedia. [https://en.wikipedia.org/wiki/Systematic\\_sampling](https://en.wikipedia.org/wiki/Systematic_sampling)
- Stratified sampling on Wikipedia. [https://en.wikipedia.org/wiki/Stratified\\_sampling](https://en.wikipedia.org/wiki/Stratified_sampling)
- Resampling (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Resampling\\_\(statistics\)](https://en.wikipedia.org/wiki/Resampling_(statistics))
- Bootstrapping (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Bootstrapping\\_\(statistics\)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
- Cross-validation (statistics) on Wikipedia. [https://en.wikipedia.org/wiki/Cross-validation\\_\(statistics\)](https://en.wikipedia.org/wiki/Cross-validation_(statistics))

## 16.6 Summary

In this tutorial, you discovered statistical sampling and statistical resampling methods for gathering and making best use of data. Specifically, you learned:

- Sampling is an active process of gathering observations intent on estimating a population variable.
- Resampling is a methodology of economically using a data sample to improve the accuracy and quantify the uncertainty of a population parameter.
- Resampling methods, in fact, make use of a nested resampling method.

#### 16.6.1 Next

In the next section, you will discover the bootstrap method for estimating population parameters from samples.
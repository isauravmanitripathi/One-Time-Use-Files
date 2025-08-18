# Chapter 19

# Introduction to Estimation Statistics

Statistical hypothesis tests can be used to indicate whether the difference between two samples is due to random chance, but cannot comment on the size of the difference. A group of methods referred to as new statistics are seeing increased use instead of or in addition to p-values in order to quantify the magnitude of effects and the amount of uncertainty for estimated values. This group of statistical methods is referred to as estimation statistics. In this tutorial, you will discover a gentle introduction to estimation statistics as an alternate or complement to statistical hypothesis testing. After completing this tutorial, you will know:

- Effect size methods involve quantifying the association or difference between samples.
- Interval estimate methods involve quantifying the uncertainty around point estimations.
- Meta-analyses involve quantifying the magnitude of an effect across multiple similar independent studies.

Let's get started.

### 19.1 Tutorial Overview

This tutorial is divided into 5 parts; they are:

- 1. Problems with Hypothesis Testing
- 2. Estimation Statistics
- 3. Effect Size
- 4. Interval Estimation
- 5. Meta-Analysis

## 19.2 Problems with Hypothesis Testing

Statistical hypothesis testing and the calculation of p-values is a popular way to present and interpret results. Tests like the Student's t-test can be used to describe whether or not two samples have the same distribution. They can help interpret whether the difference between two sample means is likely real or due to random chance. Although they are widely used, they have some problems. For example:

- Calculated p-values are easily misused and misunderstood.
- There's always some significant difference between samples, even if the difference is tiny.

Interestingly, in the last few decades there has been a push back against the use of p-values in the presentation of research. For example, in the 1990s, the Journal of Epidemiology banned the use of p-values. Many related areas in medicine and psychology have followed suit. Although p-values may still be used, there is a push toward the presentation of results using estimation statistics.

## 19.3 Estimation Statistics

Estimation statistics refers to methods that attempt to quantify a finding. This might include quantifying the size of an effect or the amount of uncertainty for a specific outcome or result.

... 'estimation statistics', a term describing the methods that focus on the estimation of effect sizes (point estimates) and their confidence intervals (precision estimates).

— Estimation statistics should replace significance testing, 2016.

Estimation statistics is a term to describe three main classes of methods. The three main classes of methods include:

- Effect Size. Methods for quantifying the size of an effect given a treatment or intervention.
- Interval Estimation. Methods for quantifying the amount of uncertainty in a value.
- Meta-Analysis. Methods for quantifying the findings across multiple similar studies.

We will look at each of these groups of methods in more detail in the following sections. Although they are not new, they are being called the new statistics given their increased use in research literature over statistical hypothesis testing.

The new statistics refer to estimation, meta-analysis, and other techniques that help researchers shift emphasis from [null hypothesis statistical tests]. The techniques are not new and are routinely used on some disciplines, but for the [null hypothesis statistical tests] disciplines, their use would be new and beneficial.

— Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis, 2012.

#### 19.4. Effect Size 153

The main reason that the shift from statistical hypothesis methods to estimation systems is occurring is the results are easier to analyze and interpret in the context of the domain or research question. The quantified size of the effect and uncertainty allows claims to be made that are easier to understand and use. The results are more meaningful.

Knowing and thinking about the magnitude and precision of an effect is more useful to quantitative science than contemplating the probability of observing data of at least that extremity, assuming absolutely no effect.

— Estimation statistics should replace significance testing, 2016.

Where statistical hypothesis tests talk about whether the samples come from the same distribution or not, estimation statistics can describe the size and confidence of the difference. This allows you to comment on how different one method is from another.

Estimating thinking focuses on how big an effect is; knowing this is usually more valuable than knowing whether or not the effect is zero, which is the fours of dichotomous thinking. Estimation thinking prompts us to plan an experiment to address the question, "How much...?" or "To what extent...?" rater than only the dichotomous null hypothesis statistical tests] question, "Is there an effect?"

— Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis, 2012.

### 19.4 Effect Size

The effect size describes the magnitude of a treatment or difference between two samples. Note that effect size was covered in detail in Chapter 14. A hypothesis test can comment on whether the difference between samples is the result of chance or is real, whereas an effect size puts a number on how much the samples differ. Measuring the size of an effect is a big part of applied machine learning, and in fact, research in general.

I am sometimes asked, what do researchers do? The short answer is that we estimate the size of effects. No matter what phenomenon we have chosen to study we essentially spend our careers thinking up new and better ways to estimate effect magnitudes.

— Page 3, The Essential Guide to Effect Sizes: Statistical Power, Meta-Analysis, and the Interpretation of Research Results, 2010.

There are two main classes of techniques used to quantify the magnitude of effects; they are:

- Association. The degree to which two samples change together.
- Difference. The degree to which two samples are different.

For example, association effect sizes include calculations of correlation, such as the Pearson's correlation coefficient, and the r 2 coefficient of determination. They may quantify the linear or monotonic way that observations in two samples change together. Difference effect size may include methods such as Cohen's d statistic that provide a standardized measure for how the means of two populations differ. They seek a quantification for the magnitude of difference between observations in two samples.

An effect can be the result of a treatment revealed in a comparison between groups (e.g., treated and untreated groups) or it can describe the degree of association between two related variables (e.g., treatment dosage and health).

— Page 4, The Essential Guide to Effect Sizes: Statistical Power, Meta-Analysis, and the Interpretation of Research Results, 2010.

### 19.5 Interval Estimation

Interval estimation refers to statistical methods for quantifying the uncertainty for an observation. Intervals transform a point estimate into a range that provides more information about the estimate, such as its precision, making them easier to compare and interpret.

The point estimates are the dots, and the intervals indicate the uncertainty of those point estimates.

— Page 9, Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis, 2012.

There are three main types of intervals that are commonly calculated. They are:

- Tolerance Interval: The bounds or coverage of a proportion of a distribution with a specific level of confidence.
- Confidence Interval: The bounds on the estimate of a population parameter.
- Prediction Interval: The bounds on a single observation.

A tolerance interval may be used to set expectations on observations in a population or help to identify outliers. A confidence interval can be used to interpret the range for a mean of a data sample that can become more precise as the sample size is increased. A prediction interval can be used to provide a range for a prediction or forecast from a model. For example, when presenting the mean estimated skill of a model, a confidence interval can be used to provide bounds on the precision of the estimate. This could also be combined with p-values if models are being compared.

The confidence interval thus provides a range of possibilities for the population value, rather than an arbitrary dichotomy based solely on statistical significance. It conveys more useful information at the expense of precision of the P value. However, the actual P value is helpful in addition to the confidence interval, and preferably both should be presented. If one has to be excluded, however, it should be the P value.

— Confidence intervals rather than P values: estimation rather than hypothesis testing, 1986.

### 19.6 Meta-Analysis

A meta-analysis refers to the use of a weighting of multiple similar studies in order to quantify a broader cross-study effect. Meta studies are useful when many small and similar studies have been performed with noisy and conflicting findings. Instead of taking the study conclusions at face value, statistical methods are used to combine multiple findings into a stronger finding than any single study.

... better known as meta-analysis, completely ignores the conclusions that others have drawn and looks instead at the effects that have been observed. The aim is to combine these independent observations into an average effect size and draw an overall conclusion regarding the direction and magnitude of real-world effects.

— Page 90, The Essential Guide to Effect Sizes: Statistical Power, Meta-Analysis, and the Interpretation of Research Results, 2010.

Although not often used in applied machine learning, it is useful to note meta-analyses as they form part of this trust of new statistical methods.

### 19.7 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Describe three examples of how estimation statistics can be used in a machine learning project.
- Locate and summarize three criticisms against the use of statistical hypothesis testing.
- Search and locate three research papers that make use of interval estimates.

If you explore any of these extensions, I'd love to know.

## 19.8 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 19.8.1 Books

- Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis, 2012. <http://amzn.to/2HxDjgC>
- Introduction to the New Statistics: Estimation, Open Science, and Beyond, 2016. <http://amzn.to/2FEudOI>
- The Essential Guide to Effect Sizes: Statistical Power, Meta-Analysis, and the Interpretation of Research Results, 2010. <http://amzn.to/2p8Ckfs>

#### 19.8.2 Papers

- Estimation statistics should replace significance testing, 2016. <https://www.nature.com/articles/nmeth.3729>
- Confidence intervals rather than P values: estimation rather than hypothesis testing, 1986. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1339793/>

#### 19.8.3 Articles

- Estimation statistics on Wikipedia. [https://en.wikipedia.org/wiki/Estimation\\_statistics](https://en.wikipedia.org/wiki/Estimation_statistics)
- Effect size on Wikipedia. [https://en.wikipedia.org/wiki/Effect\\_size](https://en.wikipedia.org/wiki/Effect_size)
- Interval estimation on Wikipedia. [https://en.wikipedia.org/wiki/Interval\\_estimation](https://en.wikipedia.org/wiki/Interval_estimation)
- Meta-analysis on Wikipedia. <https://en.wikipedia.org/wiki/Meta-analysis>

# 19.9 Summary

In this tutorial, you discovered a gentle introduction to estimation statistics as an alternate or complement to statistical hypothesis testing. Specifically, you learned:

- Effect size methods involve quantifying the association or difference between samples.
- Interval estimate methods involve quantifying the uncertainty around point estimations.
- Meta-analyses involve quantifying the magnitude of an effect across multiple similar independent studies.

#### 19.9.1 Next

In the next section, you will discover tolerance intervals for quantifying likely values in a distribution.
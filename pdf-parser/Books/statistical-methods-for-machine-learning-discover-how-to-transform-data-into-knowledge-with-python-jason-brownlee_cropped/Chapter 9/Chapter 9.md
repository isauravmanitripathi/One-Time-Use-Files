# Chapter 9

# Statistical Hypothesis Testing

Data must be interpreted in order to discover meaning. We can interpret data by assuming a specific structured outcome and use statistical methods to confirm or reject the assumption. The assumption is called a hypothesis and the statistical tests used for this purpose are called statistical hypothesis tests. Whenever we want to make claims about the distribution of data or whether one set of results are different from another set of results in applied machine learning, we must rely on statistical hypothesis tests.

In this tutorial, you will discover statistical hypothesis testing and how to interpret and carefully state the results from statistical tests. After completing this tutorial, you will know:

- Statistical hypothesis tests are important for quantifying answers to questions about samples of data.
- The interpretation of a statistical hypothesis test requires a correct understanding of p-values and critical values.
- Regardless of the significance level, the finding of hypothesis tests may still contain errors.

Let's get started.

# 9.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- 1. Statistical Hypothesis Testing
- 2. Statistical Test Interpretation
- 3. Errors in Statistical Tests
- 4. Degrees of Freedom

# 9.2 Statistical Hypothesis Testing

Data alone is not interesting. It is the interpretation of the data that we are really interested in. In statistics, when we wish to start asking questions about the data and interpret the results, we use statistical methods that provide a confidence or likelihood about the answers. In general, this class of methods is called statistical hypothesis testing, or significance tests.

The term hypothesis may make you think about science, where we investigate a hypothesis. This is along the right track. In statistics, a hypothesis test calculates some quantity under a given assumption. The result of the test allows us to interpret whether the assumption holds or whether the assumption has been violated. Two concrete examples that we will use a lot in machine learning are:

- A test that assumes that data has a normal distribution.
- A test that assumes that two samples were drawn from the same underlying population distribution.

The assumption of a statistical test is called the null hypothesis, or hypothesis zero (H0 for short). It is often called the default assumption, or the assumption that nothing has changed. A violation of the test's assumption is often called the first hypothesis, hypothesis one or H1 for short. H1 is really a short hand for some other hypothesis, as all we know is that the evidence suggests that the H0 can be rejected.

- Hypothesis 0 (H0): Assumption of the test fails to be rejected.
- Hypothesis 1 (H1): Assumption of the test does not hold and is rejected at some level of significance.

Before we can reject or fail to reject the null hypothesis, we must interpret the result of the test.

# 9.3 Statistical Test Interpretation

The results of a statistical hypothesis test must be interpreted for us to start making claims. This is a point that may cause a lot of confusion for beginners and experienced practitioners alike. There are two common forms that a result from a statistical hypothesis test may take, and they must be interpreted in different ways. They are the p-value and critical values.

### 9.3.1 Interpret the p-value

We describe a finding as statistically significant by interpreting the p-value. For example, we may perform a Student's t-test on two data samples and find that it is unlikely that the samples have the same mean. We reject the null hypothesis that the samples have the same mean at a chosen level of statistical significance (or confidence). A statistical hypothesis test may return a value called p or the p-value. This is a quantity that we can use to interpret or quantify the result of the test and either reject or fail to reject the null hypothesis. This is done by comparing the p-value to a threshold value chosen beforehand called the significance level.

The significance level is often referred to by the Greek lower case letter alpha (α). A common value used for alpha is 5% or 0.05. A smaller alpha value suggests a more robust interpretation of the result, such as 1% or 0.1%. The p-value is compared to the pre-chosen alpha value. A result is statistically significant when the p-value is less than or equal to alpha. This signifies a change was detected: that the default or null hypothesis can be rejected.

- p-value ≤ alpha: significant result, reject null hypothesis (H1).
- p-value > alpha: not significant result, fail to reject the null hypothesis (H0).

The significance level can be inverted by subtracting it from 1 to give a confidence level of the hypothesis given the observed sample data.

$$\text{confidence level} = 1 - \text{significance level} \tag{9.1}$$

### 9.3.2 "Reject" vs "Failure to Reject"

The p-value is probabilistic. This means that when we interpret the result of a statistical test, we do not know what is true or false, only what is likely. Rejecting the null hypothesis means that there is sufficient statistical evidence that the null hypothesis does not look likely. Otherwise, it means that there is not sufficient statistical evidence to reject the null hypothesis.

We may think about the statistical test in terms of the dichotomy of rejecting and accepting the null hypothesis. The danger is that if we say that we accept the null hypothesis, the language suggests that the null hypothesis is true. Instead, it is safer to say that we fail to reject the null hypothesis, as in, there is insufficient statistical evidence to reject it. When reading reject vs fail to reject for the first time, it is confusing to beginners. You can think of it as reject vs accept in your mind, as long as you remind yourself that the result is probabilistic and that even an accepted null hypothesis still has a small probability of being wrong.

### 9.3.3 Common p-value Misinterpretations

This section highlights some common misinterpretations of the p-value in the results of statistical tests.

#### True or False Null Hypothesis

The interpretation of the p-value does not mean that the null hypothesis is true or false. It does mean that we have chosen to reject or fail to reject the null hypothesis at a specific statistical significance level based on empirical evidence and the chosen statistical test. You are limited to making probabilistic claims, not crisp binary or true/false claims about the result.

#### p-value as Probability

A common misunderstanding is that the p-value is a probability of the null hypothesis being true or false given the data. In probability, this would be written as follows:

$$Pr(hypothesis|data)$$
 (9.2)

This is incorrect. Instead, the p-value can be thought of as the probability of the data given the pre-specified assumption embedded in the statistical test.

Again, using probability notation, this would be written as:

$$Pr(data | hypothesis)$$
 (9.3)

It allows us to reason about whether or not the data fits the hypothesis. Not the other way around. The p-value is a measure of how likely the data sample would be observed if the null hypothesis were true.

#### Post-Hoc Tuning

It does not mean that you can re-sample your domain or tune your data sample and re-run the statistical test until you achieve a desired result. It also does not mean that you can choose your p-value after you run the test. This is called p-hacking or hill climbing and will mean that the result you present will be fragile and not representative. In science, this is at best unethical, and at worst fraud.

### 9.3.4 Interpret Critical Values

Some tests do not return a p-value. Instead, they might return a test statistic value from a specific data distribution that can be interpreted in the context of critical values. A critical value is a value from the distribution of the test statistic after which point the result is significant and the null hypothesis can be rejected.

- Test Statistic < Critical Value: not significant result, fail to reject null hypothesis (H0).
- Test Statistic ≥ Critical Value: significant result, reject null hypothesis (H1).

It requires that you know the distribution of the test statistic and how to sample the distribution to retrieve the critical value. This is demonstrated for standard distributions in Chapter 11. The p-value is calculated from the critical value.

Again, the meaning of the result is similar in that the chosen significance level is a probabilistic decision on the rejection or failure of rejection of the base assumption of the test given the data. Results are presented in the same way as with a p-value, as either significance level or confidence level. For example, if a normality test was calculated and the test statistic was compared to the critical value at the 5% significance level, results could be stated as:

The test found that the data sample was normal, failing to reject the null hypothesis at a 5% significance level.

Or:

The test found that the data was normal, failing to reject the null hypothesis at a 95% confidence level.

# 9.4 Errors in Statistical Tests

The interpretation of a statistical hypothesis test is probabilistic. That means that the evidence of the test may suggest an outcome and be mistaken. For example, if alpha was 5%, it suggests that (at most) 1 time in 20 that the null hypothesis would be mistakenly rejected because of the statistical noise in the data sample. Given a small p-value (reject the null hypothesis) either means that the null hypothesis false (we got it right) or it is true and some rare and unlikely event has been observed (we made a mistake). If this type of error is made, it is called a false positive. We falsely believe the rejection of the null hypothesis.

Alternately, given a large p-value (fail to reject the null hypothesis), it may mean that the null hypothesis is true (we got it right) or that the null hypothesis is false and some unlikely event occurred (we made a mistake). If this type of error is made, it is called a false negative. We falsely believe the null hypothesis or assumption of the statistical test.

Each of these two types of error has a specific name.

- Type I Error: The incorrect rejection of a true null hypothesis, called a false positive.
- Type II Error: The incorrect failure of rejecting a false null hypothesis, called a false negative.

All statistical hypothesis tests have a chance of making either of these types of errors. False findings or false discoveries are more than possible; they are probable. Ideally, we want to choose a significance level that minimizes the likelihood of one of these errors. E.g. a very small significance level. Although significance levels such as 0.05 and 0.01 are common in many fields of science, harder sciences, such as physics, are more aggressive.

It is common to use a significance level of 3 × 10<sup>−</sup><sup>7</sup> or 0.0000003, often referred to as 5-sigma. This means that the finding was due to chance with a probability of 1 in 3.5 million independent repeats of the experiments. To use a threshold like this may require a much large data sample. Nevertheless, these types of errors are always present and must be kept in mind when presenting and interpreting the results of statistical tests. It is also a reason why it is important to have findings independently verified.

# 9.5 Degrees of Freedom in Statistics

When we calculate statistics, we often must include some information about the size of the data sample. The way we do this is via the degrees of freedom. The degrees of freedom is the number of independent pieces of information that are used to estimate a parameter or calculate a statistic from the data sample.

The degrees of freedom may be written as df or dof and in an equation may use the Greek lowercase letter nu (ν). The degrees of freedom will always be equal to or less than the size of the sample, often denoted as n. If the statistic being calculated makes use of another statistic in an intermediate step, then the number of degrees of freedom must be corrected via making a subtraction. For example, when we calculate the sample mean as an estimate of the population mean, we can use the sample size as the degrees of freedom:

$$mean(x) = \frac{1}{n} \times \sum_{i=1}^{n} x_i \tag{9.4}$$

#### 9.6. Extensions 76

When we calculate the sample variance as an estimate of the population variance, we must correct the degrees of freedom because the sample mean is used in the calculation.

$$variance(x) = \frac{1}{n-1} \times \sum_{i=1}^{n} (x_i - mean(x))^2 \tag{9.5}$$

The correction updates the degrees of freedom for the single intermediate statistic used that itself can introduce some additional uncertainty into the calculation. We will see mention and use of the degrees of freedom as a parameter or correction in a suite of statistical hypothesis tests.

# 9.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Find an example of a research paper that does not present results using p-values.
- Find an example of a research paper that presents results with statistical significance, but makes one of the common misinterpretations of p-values.
- Find an example of a research paper that presents results with statistical significance and correctly interprets and presents the p-value and findings.

If you explore any of these extensions, I'd love to know.

# 9.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

### 9.7.1 Articles

- Statistical hypothesis testing on Wikipedia. [https://en.wikipedia.org/wiki/Statistical\\_hypothesis\\_testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
- Statistical significance on Wikipedia. [https://en.wikipedia.org/wiki/Statistical\\_significance](https://en.wikipedia.org/wiki/Statistical_significance)
- p-value on Wikipedia. <https://en.wikipedia.org/wiki/P-value>
- Critical value on Wikipedia. [https://en.wikipedia.org/wiki/Critical\\_value](https://en.wikipedia.org/wiki/Critical_value)
- Type I and type II errors on Wikipedia. [https://en.wikipedia.org/wiki/Type\\_I\\_and\\_type\\_II\\_errors](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
- Data dredging on Wikipedia. [https://en.wikipedia.org/wiki/Data\\_dredging](https://en.wikipedia.org/wiki/Data_dredging)

- Misunderstandings of p-values on Wikipedia. [https://en.wikipedia.org/wiki/Misunderstandings\\_of\\_p-values](https://en.wikipedia.org/wiki/Misunderstandings_of_p-values)
- What does the 5 sigma mean? <http://www.physics.org/article-questions.asp?id=103>

# 9.8 Summary

In this tutorial, you discovered statistical hypothesis testing and how to interpret and carefully state the results from statistical tests. Specifically, you learned:

- Statistical hypothesis tests are important for quantifying answers to questions about samples of data.
- The interpretation of a statistical hypothesis test requires a correct understanding of p-values.
- Regardless of the significance level, the finding of hypothesis tests may still contain errors.

### 9.8.1 Next

In the next section, you will discover the three key distributions that you need to know well when working with statistical hypothesis tests.
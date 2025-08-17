# Chapter 11 Critical Values

It is common, if not standard, to interpret the results of statistical hypothesis tests using a p-value. Not all implementations of statistical tests return p-values. In some cases, you must use alternatives, such as critical values. In addition, critical values are used when estimating the expected intervals for observations from a population, such as in tolerance intervals. In this tutorial, you will discover critical values, why they are important, how they are used, and how to calculate them in Python using SciPy. After completing this tutorial, you will know:

- Examples of statistical hypothesis tests and their distributions from which critical values can be calculated and used.
- How exactly critical values are used on one-tail and two-tail statistical hypothesis tests.
- How to calculate critical values for the Gaussian, Student's t, and Chi-Squared distributions.

Let's get started.

# 11.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- 1. Why Do We Need Critical Values?
- 2. What Is a Critical Value?
- 3. How to Use Critical Values
- 4. How to Calculate Critical Values

# 11.2 Why Do We Need Critical Values?

Many statistical hypothesis tests return a p-value that is used to interpret the outcome of the test. Some tests do not return a p-value, requiring an alternative method for interpreting the calculated test statistic directly. A statistic calculated by a statistical hypothesis test can be interpreted using critical values from the distribution of the test statistic. Some examples of statistical hypothesis tests and their distributions from which critical values can be calculated are as follows:

- Z-Test: Gaussian distribution.
- Student's t-Test: Student's t-distribution.
- Chi-Squared Test: Chi-Squared distribution.
- ANOVA: F-distribution.

Critical values are also used when defining intervals for expected (or unexpected) observations in distributions. Calculating and using critical values may be appropriate when quantifying the uncertainty of estimated statistics or intervals such as confidence intervals and tolerance intervals. Note, a p-value can be calculated from a test statistic by retrieving the probability from the test statistics cumulative density function (CDF).

## 11.3 What Is a Critical Value?

A critical value is defined in the context of the population distribution and a probability. An observation from the population with a value equal to or lesser than a critical value with the given probability. We can express this mathematically as follows:

$$Pr[X \le \text{critical value}] = \text{probability} \tag{11.1}$$

Where Pr is the calculation of probability, X are observations from the population, critical value is the calculated critical value, and probability is the chosen probability. Critical values are calculated using a mathematical function where the probability is provided as an argument. For most common distributions, the value cannot be calculated analytically; instead it must be estimated using numerical methods. Historically it is common for tables of pre-calculated critical values to be provided in the appendices of statistics textbooks for reference purposes. Critical values are used in statistical significance testing. The probability is often expressed as a significance, denoted as the lowercase Greek letter alpha (α), which is the inverted probability.

$$probability = 1 - alpha \tag{11.2}$$

Standard alpha values are used when calculating critical values, chosen for historical reasons and continually used for consistency reasons. These alpha values include:

- 1% (alpha=0.01)
- 5% (alpha=0.05)
- 10% (alpha=0.10)

Critical values provide an alternative and equivalent way to interpret statistical hypothesis tests to the p-value.

## 11.4 How to Use Critical Values

Calculated critical values are used as a threshold for interpreting the result of a statistical test. The observation values in the population beyond the critical value are often called the critical region or the region of rejection.

Critical Value: A value appearing in tables for specified statistical tests indicating at what computed value the null hypothesis can be rejected (the computed statistic falls in the rejection region).

— Page 265, Handbook of Research Methods: A Guide for Practitioners and Students in the Social Sciences, 2003.

A statistical test may be one-tailed or two-tailed.

#### 11.4.1 One-Tailed Test

A one-tailed test has a single critical value, such as on the left or the right of the distribution. Often, a one-tailed test has a critical value on the right of the distribution for non-symmetrical distributions (such as the Chi-Squared distribution). The statistic is compared to the calculated critical value. If the statistic is less than or equal to the critical value, the null hypothesis of the statistical test rejected or it is failed to be rejected. We can summarize this interpretation as follows:

- Test Statistic < Critical Value: not significant result, fail to reject null hypothesis (H0).
- Test Statistic ≥ Critical Value: significant result, reject null hypothesis (H0).

#### 11.4.2 Two-Tailed Test

A two-tailed test has two critical values, one on each side of the distribution, which is often assumed to be symmetrical (e.g. Gaussian and Student-t distributions.). When using a twotailed test, a significance level (or alpha) used in the calculation of the critical values must be divided by 2. The critical value will then use a portion of this alpha on each side of the distribution. To make this concrete, consider an alpha of 5%. This would be split to give two alpha values of 2.5% on either side of the distribution with an acceptance area in the middle of the distribution of 95%.

We can refer to each critical value as the lower and upper critical values for the left and right of the distribution respectively. Test statistic values more than or equal to the lower critical value and less than or equal to the upper critical value indicate the failure to reject the null hypothesis. Whereas test statistic values less than the lower critical value and more than the upper critical value indicate rejection of the null hypothesis for the test. We can summarize this interpretation as follows:

 Lower CR < Test Statistic > Upper CR: not significant result, fail to reject null hypothesis (H0).

 Test Statistic ≤ Lower CR OR Test Statistic ≥ Upper CR: significant result, reject null hypothesis (H0).

If the distribution of the test statistic is symmetric around a mean of zero, then we can shortcut the check by comparing the absolute (positive) value of the test statistic to the upper critical value.

- |Test Statistic| < Upper Critical Value: not significant result, fail to reject null hypothesis (H0), distributions same.
- |Test Statistic| ≥ Upper Critical Value: significant result, reject null hypothesis (H0), distributions differ.

Where |Test Statistic| is the absolute value of the calculated test statistic.

## 11.5 How to Calculate Critical Values

Density functions return the probability of an observation in the distribution. Recall the definitions of the PDF and CDF as follows:

- Probability Density Function (PDF): Returns the probability for an observation having a specific value from the distribution.
- Cumulative Density Function (CDF): Returns the probability for an observation equal to or lesser than a specific value from the distribution.

In order to calculate a critical value, we require a function that, given a probability (or significance), will return the observation value from the distribution. Specifically, we require the inverse of the cumulative density function, where given a probability, we are given the observation value that is less than or equal to the probability. This is called the percent point function (PPF), or more generally the quantile function.

 Percent Point Function (PPF): Returns the observation value for the provided probability that is less than or equal to the provided probability from the distribution.

Specifically, a value from the distribution will equal or be less than the value returned from the PPF with the specified probability. Let's make this concrete with three distributions from which it is commonly required to calculate critical values. Namely, the Gaussian distribution, Student's t-distribution, and the Chi-Squared distribution. We can calculate the percent point function in SciPy using the ppf() function on a given distribution. It should also be noted that you can also calculate the ppf() using the inverse survival function called isf() in SciPy. This is mentioned as you may see use of this alternate approach in third party code.

#### 11.5.1 Gaussian Critical Values

The example below calculates the percent point function for 95% on the standard Gaussian distribution.

```
# gaussian percent point function
from scipy.stats import norm
# define probability
p = 0.95
# retrieve value <= probability
value = norm.ppf(p)
print(value)
# confirm with cdf
p = norm.cdf(value)
print(p)
```

Listing 11.1: Example of calculating critical values for the Gaussian distribution.

Running the example first prints the value that marks 95% or less of the observations from the distribution of about 1.65. This value is then confirmed by retrieving the probability of the observation from the CDF, which returns 95%, as expected. We can see that the value 1.65 aligns with our expectation with regard to the number of standard deviations from the mean that cover 95% of the distribution in the 68-95-99.7 rule (linked in the Further Reading section).

```
1.6448536269514722
0.95
```

Listing 11.2: Sample output from calculating critical values for the Gaussian distribution.

#### 11.5.2 Student's t Critical Values

The example below calculates the percentage point function for 95% on the standard Student's t-distribution with 10 degrees of freedom.

```
# student t-distribution percent point function
from scipy.stats import t
# define probability
p = 0.95
df = 10
# retrieve value <= probability
value = t.ppf(p, df)
print(value)
# confirm with cdf
p = t.cdf(value, df)
print(p)
```

Listing 11.3: Example of calculating critical values for the t distribution.

Running the example returns the value of about 1.812 or less that covers 95% of the observations from the chosen distribution. The probability of the value is then confirmed (with minor rounding error) via the CDF.

```
1.8124611228107335
0.949999999999923
```

Listing 11.4: Sample output from calculating critical values for the t distribution.

## 11.5.3 Chi-Squared Critical Values

The example below calculates the percentage point function for 95% on the standard Chi-Squared distribution with 10 degrees of freedom.

```
# chi-squared percent point function
from scipy.stats import chi2
# define probability
p = 0.95
df = 10
# retrieve value <= probability
value = chi2.ppf(p, df)
print(value)
# confirm with cdf
p = chi2.cdf(value, df)
print(p)
```

Listing 11.5: Example of calculating critical values for the Chi-Squared distribution.

Running the example first calculates the value of 18.3 or less that covers 95% of the observations from the distribution. The probability of this observation is confirmed by using it as input to the CDF.

```
18.307038053275143
0.95
```

Listing 11.6: Sample output from calculating critical values for the Chi-Squared distribution.

# 11.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Calculate critical values for 90%, 95% and 99% for each of the Gaussian, Student's t, and Chi-Squared distributions.
- Develop an example to calculate critical values from another distribution, such as the F distribution.
- Write code to calculate a p-value from a critical value for each of the Gaussian, Student's t, and Chi-Squared distributions.

If you explore any of these extensions, I'd love to know.

# 11.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 11.7.1 Books

 Handbook of Research Methods: A Guide for Practitioners and Students in the Social Sciences, 2003. <http://amzn.to/2G4vG4k>

## 11.7.2 API

- scipy.stats.norm API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html>
- scipy.stats.t API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html>
- scipy.stats.chi2 API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html>

## 11.7.3 Articles

- Critical value on Wikipedia. [https://en.wikipedia.org/wiki/Critical\\_value](https://en.wikipedia.org/wiki/Critical_value)
- P-value on Wikipedia. <https://en.wikipedia.org/wiki/P-value>
- One- and two-tailed tests on Wikipedia. [https://en.wikipedia.org/wiki/One-\\_and\\_two-tailed\\_tests](https://en.wikipedia.org/wiki/One-_and_two-tailed_tests)
- Quantile function on Wikipedia. [https://en.wikipedia.org/wiki/Quantile\\_function](https://en.wikipedia.org/wiki/Quantile_function)
- 68-95-99.7 rule on Wikipedia. [https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7\\_rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule)

# 11.8 Summary

In this tutorial, you discovered critical values, why they are important, how they are used, and how to calculate them in Python using SciPy. Specifically, you learned:

- Examples of statistical hypothesis tests and their distributions from which critical values can be calculated and used.
- How exactly critical values are used on one-tail and two-tail statistical hypothesis tests.
- How to calculate critical values for the Gaussian, Student's t, and Chi-Squared distributions.

### 11.8.1 Next

In the next section, you will discover how to quantify the relationship between samples of data.
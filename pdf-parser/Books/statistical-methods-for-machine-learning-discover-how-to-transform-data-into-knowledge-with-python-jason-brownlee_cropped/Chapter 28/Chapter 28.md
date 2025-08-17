# Chapter 28

# Rank Significance Tests

In applied machine learning, we often need to determine whether two data samples have the same or different distributions. We can answer this question using statistical significance tests that can quantify the likelihood that the samples have the same distribution.

If the data does not have the familiar Gaussian distribution, we must resort to nonparametric version of the significance tests. These tests operate in a similar manner, but are distribution free, requiring that real valued data be first transformed into rank data before the test can be performed. In this tutorial, you will discover nonparametric statistical tests that you can use to determine if data samples were drawn from populations with the same or different distributions. After completing this tutorial, you will know:

- The Mann-Whitney U test for comparing independent data samples: the nonparametric version of the Student's t-test.
- The Wilcoxon signed-rank test for comparing paired data samples: the nonparametric version of the paired Student's t-test.
- The Kruskal-Wallis H and Friedman tests for comparing more than two data samples: the nonparametric version of the ANOVA and repeated measures ANOVA tests.

Let's get started.

## 28.1 Tutorial Overview

This tutorial is divided into 6 parts; they are:

- 1. Nonparametric Statistical Significance Tests
- 2. Test Data
- 3. Mann-Whitney U Test
- 4. Wilcoxon Signed-Rank Test
- 5. Kruskal-Wallis H Test
- 6. Friedman Test

## 28.2 Nonparametric Statistical Significance Tests

Nonparametric statistics are those methods that do not assume a specific distribution to the data. Often, they refer to statistical methods that do not assume a Gaussian distribution. They were developed for use with ordinal or interval data, but in practice can also be used with a ranking of real-valued observations in a data sample rather than on the observation values themselves. A common question about two or more datasets is whether they are different. Specifically, whether the difference between their central tendency (e.g. mean or median) is statistically significant.

This question can be answered for data samples that do not have a Gaussian distribution by using nonparametric statistical significance tests. The null hypothesis of these tests is often the assumption that both samples were drawn from a population with the same distribution, and therefore the same population parameters, such as mean or median.

If after calculating the significance test on two or more samples the null hypothesis is rejected, it indicates that there is evidence to suggest that samples were drawn from different populations, and in turn the difference between sample estimates of population parameters, such as means or medians may be significant. These tests are often used on samples of model skill scores in order to confirm that the difference in skill between machine learning models is significant.

In general, each test calculates a test statistic, that must be interpreted with some background in statistics and a deeper knowledge of the statistical test itself. Tests also return a p-value that can be used to interpret the result of the test. The p-value can be thought of as the probability of observing the two data samples given the base assumption (null hypothesis) that the two samples were drawn from a population with the same distribution. The p-value can be interpreted in the context of a chosen significance level called alpha. A common value for alpha is 5% or 0.05. If the p-value is below the significance level, then the test says there is enough evidence to reject the null hypothesis and that the samples were likely drawn from populations with differing distributions.

- p-value ≤ alpha: significant result, reject null hypothesis, distributions differ (H1).
- p-value > alpha: not significant result, fail to reject null hypothesis, distributions same (H0).

## 28.3 Test Dataset

Before we look at specific nonparametric significance tests, let's first define a test dataset that we can use to demonstrate each test. We will generate two samples drawn from different distributions. We will use the rand() NumPy function to generate two samples of 100 uniform random numbers between 50-59 and 51-60 respectively. We expect the statistical tests to discover that the samples were drawn from differing distributions, although the small sample size of 100 observations per sample will add some noise to this decision. The complete code example is listed below.

```
# generate data samples
from numpy.random import seed
from numpy.random import rand
# seed the random number generator
seed(1)
```

```
# generate two sets of univariate observations
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# summarize
print('data1: min=%.3f max=%.3f' % (min(data1), max(data1)))
print('data2: min=%.3f max=%.3f' % (min(data2), max(data2)))
```

Listing 28.1: Example generating a small test dataset.

Running the example generates the data samples, then calculates and prints the min and max values for each sample, confirming their different distribution.

| data1: min=50.001 max=59.889 |  |
|------------------------------|--|
| data2: min=51.126 max=60.973 |  |

Listing 28.2: Example output from creating a small test dataset.

## 28.4 Mann-Whitney U Test

The Mann-Whitney U test is a nonparametric statistical significance test for determining whether two independent samples were drawn from a population with the same distribution. The test was named for Henry Mann and Donald Whitney, although it is sometimes called the Wilcoxon-Mann-Whitney test, also named for Frank Wilcoxon, who also developed a variation of the test.

The two samples are combined and rank ordered together. The strategy is to determine if the values from the two samples are randomly mixed in the rank ordering or if they are clustered at opposite ends when combined. A random rank order would mean that the two samples are not different, while a cluster of one sample values would indicate a difference between them.

— Page 58, Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach, 2009.

The default assumption or null hypothesis is that there is no difference between the distributions of the data samples. Rejection of this hypothesis suggests that there is likely some difference between the samples. More specifically, the test determines whether it is equally likely that any randomly selected observation from one sample will be greater or less than a sample in the other distribution. If violated, it suggests differing distributions.

- Fail to Reject H0: Sample distributions are equal.
- Reject H0: Sample distributions are not equal.

For the test to be effective, it requires at least 20 observations in each data sample. We can implement the Mann-Whitney U test in Python using the mannwhitneyu() SciPy function. The functions takes as arguments the two data samples. It returns the test statistic and the p-value. The example below demonstrates the Mann-Whitney U test on the test dataset.

```
# example of the mann-whitney u test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import mannwhitneyu
# seed the random number generator
seed(1)
# generate two independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# compare samples
stat, p = mannwhitneyu(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
 print('Same distribution (fail to reject H0)')
else:
 print('Different distribution (reject H0)')
```

Listing 28.3: Example of calculating the Mann-Whitney U test on the test dataset.

Running the example calculates the test on the datasets and prints the statistic and p-value. The p-value strongly suggests that the sample distributions are different, as is expected.

Statistics=4077.000, p=0.012 Different distribution (reject H0)

Listing 28.4: Example output from calculating the Mann-Whitney U test on the test dataset.

## 28.5 Wilcoxon Signed-Rank Test

In some cases, the data samples may be paired. There are many reasons why this may be the case, for example, the samples are related or matched in some way or represent two measurements of the same technique. More specifically, each sample is independent, but comes from the same population. Examples of paired samples in machine learning might be the same algorithm evaluated on different datasets or different algorithms evaluated on exactly the same training and test data. The samples are not independent, therefore the Mann-Whitney U test cannot be used. Instead, the Wilcoxon signed-rank test is used, also called the Wilcoxon t-test, named for Frank Wilcoxon. It is the equivalent of the paired Student's t-test, but for ranked data instead of real valued data with a Gaussian distribution.

The Wilcoxon signed ranks test is a nonparametric statistical procedure for comparing two samples that are paired, or related. The parametric equivalent to the Wilcoxon signed ranks test goes by names such as the Student's t-test, t-test for matched pairs, t-test for paired samples, or t-test for dependent samples.

— Pages 38-39, Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach, 2009.

The default assumption for the test, the null hypothesis, is that the two samples have the same distribution.

- Fail to Reject H0: Sample distributions are equal.
- Reject H0: Sample distributions are not equal.

For the test to be effective, it requires at least 20 observations in each data sample. The Wilcoxon signed-rank test can be implemented in Python using the wilcoxon() SciPy function. The function takes the two samples as arguments and returns the calculated statistic and p-value. The complete example is below, demonstrating the calculation of the Wilcoxon signed-rank test on the test problem. The two samples are technically not paired, but we can pretend they are for the sake of demonstrating the calculation of this significance test.

```
# example of the wilcoxon signed-rank test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import wilcoxon
# seed the random number generator
seed(1)
# generate two independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# compare samples
stat, p = wilcoxon(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
 print('Same distribution (fail to reject H0)')
else:
 print('Different distribution (reject H0)')
```

Listing 28.5: Example of calculating the Wilcoxon Signed-Rank test on the test dataset.

Running the example calculates and prints the statistic and prints the result. The p-value is interpreted strongly suggesting that the samples are drawn from different distributions.

Statistics=1937.000, p=0.043 Different distribution (reject H0)

Listing 28.6: Example output from calculating the Wilcoxon Signed-Rank test on the test dataset.

## 28.6 Kruskal-Wallis H Test

When working with significance tests, such as Mann-Whitney U and the Wilcoxon signed-rank tests, comparisons between data samples must be performed pairwise. This can be inefficient if you have many data samples and you are only interested in whether two or more samples have a different distribution. The Kruskal-Wallis test is a nonparametric version of the one-way analysis of variance test or ANOVA for short. It is named for the developers of the method, William Kruskal and Wilson Wallis. This test can be used to determine whether more than two independent samples have a different distribution. It can be thought of as the generalization of the Mann-Whitney U test.

The default assumption or the null hypothesis is that all data samples were drawn from the same distribution. Specifically, that the population medians of all groups are equal. A rejection of the null hypothesis indicates that there is enough evidence to suggest that one or more samples dominate another sample, but the test does not indicate which samples or by how much.

When the Kruskal-Wallis H-test leads to significant results, then at least one of the samples is different from the other samples. However, the test does not identify where the difference(s) occur. Moreover, it does not identify how many differences occur. To identify the particular differences between sample pairs, a researcher might use sample contrasts, or post hoc tests, to analyze the specific sample pairs for significant difference(s). The Mann-Whitney U-test is a useful method for performing sample contrasts between individual sample sets.

— Page 100, Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach, 2009.

- Fail to Reject H0: All sample distributions are equal.
- Reject H0: One or more sample distributions are not equal.

Each data sample must be independent, have 5 or more observations, and the data samples can differ in size. We can update the test problem to have 3 data samples, each of which has a slightly different sample mean. We would expect the test to discover the difference and reject the null hypothesis.

```
...
# generate three independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
data3 = 52 + (rand(100) * 10)
```

Listing 28.7: Example of updated dataset with multiple independent samples.

The Kruskal-Wallis H-test can be implemented in Python using the kruskal() SciPy function. It takes two or more data samples as arguments and returns the test statistic and p-value as the result. The complete example is listed below.

```
# example of the kruskal-wallis h-test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import kruskal
# seed the random number generator
seed(1)
# generate three independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
data3 = 52 + (rand(100) * 10)
# compare samples
stat, p = kruskal(data1, data2, data3)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
```

```
print('Same distributions (fail to reject H0)')
else:
 print('Different distributions (reject H0)')
```

Listing 28.8: Example of calculating the Kruskal-Wallis H test on the test dataset.

Running the example calculates the test and prints the results. The p-value is interpreted, correctly rejecting the null hypothesis that all samples have the same distribution.

Statistics=34.747, p=0.000 Different distributions (reject H0)

Listing 28.9: Example output from calculating the Kruskal-Wallis H test on the test dataset.

## 28.7 Friedman Test

As in the previous example, we may have more than two different samples and an interest in whether all samples have the same distribution or not. If the samples are paired in some way, such as repeated measures, then the Kruskal-Wallis H test would not be appropriate. Instead, the Friedman test can be used, named for Milton Friedman. The Friedman test is the nonparametric version of the repeated measures analysis of variance test, or repeated measures ANOVA. The test can be thought of as a generalization of the Kruskal-Wallis H Test to more than two samples. The default assumption, or null hypothesis, is that the multiple paired samples have the same distribution. A rejection of the null hypothesis indicates that one or more of the paired samples has a different distribution.

- Fail to Reject H0: Paired sample distributions are equal.
- Reject H0: Paired sample distributions are not equal.

The test assumes two or more paired data samples with 10 or more samples per group.

The Friedman test is a nonparametric statistical procedure for comparing more than two samples that are related. The parametric equivalent to this test is the repeated measures analysis of variance (ANOVA). When the Friedman test leads to significant results, at least one of the samples is different from the other samples.

— Pages 79-80, Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach, 2009.

We can implement the Friedman test in Python using the friedmanchisquare() SciPy function. This function takes as arguments the data samples to compare and returns the calculated statistic and p-value. This significance test can be demonstrated on the same variation of the test dataset as was used in the previous section. Namely three samples, each with a slightly different sample mean. Although the samples are not paired, we expect the test to discover that not all of the samples have the same distribution. The complete code example is listed below.

```
# example of the friedman test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import friedmanchisquare
# seed the random number generator
seed(1)
# generate three independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
data3 = 52 + (rand(100) * 10)
# compare samples
stat, p = friedmanchisquare(data1, data2, data3)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
 print('Same distributions (fail to reject H0)')
else:
 print('Different distributions (reject H0)')
```

Listing 28.10: Example of calculating the Friedman test on the test dataset.

Running the example calculates the test on the three data samples and prints the test statistic and p-value. The interpretation of the p-value correctly indicates that at least one sample has a different distribution.

Statistics=36.240, p=0.000 Different distributions (reject H0)

Listing 28.11: Example output from calculating the Friedman test on the test dataset.

## 28.8 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Update all examples to operate on data samples that have the same distribution.
- Create a flowchart for choosing each of the statistical significance tests given the requirements and behavior of each test.
- Consider 3 cases of comparing data samples in a machine learning project, assume a non-Gaussian distribution for the samples, and suggest the type of test that could be used in each case.

If you explore any of these extensions, I'd love to know.

# 28.9 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 28.9.1 Books

 Nonparametric Statistics for Non-Statisticians: A Step-by-Step Approach, 2009. <http://amzn.to/2CZcXBz>

#### 28.9.2 Books

- scipy.stats.mannwhitneyu API. [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitn](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)eyu. [html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)
- scipy.stats.wilcoxon API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html>
- scipy.stats.kruskal API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html>
- scipy.stats.friedmanchisquare API. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html>

#### 28.9.3 Articles

- Nonparametric statistics on Wikipedia. [https://en.wikipedia.org/wiki/Nonparametric\\_statistics](https://en.wikipedia.org/wiki/Nonparametric_statistics)
- Paired difference test on Wikipedia. [https://en.wikipedia.org/wiki/Paired\\_difference\\_test](https://en.wikipedia.org/wiki/Paired_difference_test)
- Mann-Whitney U test on Wikipedia. [https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney\\_U\\_test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- Wilcoxon signed-rank test on Wikipedia. [https://en.wikipedia.org/wiki/Wilcoxon\\_signed-rank\\_test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test)
- Kruskal-Wallis one-way analysis of variance on Wikipedia. [https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis\\_one-way\\_analysis\\_of\\_variance](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance)
- Friedman test on Wikipedia. [https://en.wikipedia.org/wiki/Friedman\\_test](https://en.wikipedia.org/wiki/Friedman_test)

#### 28.9.4 Summary

In this tutorial, you discovered nonparametric statistical tests that you can use to determine if data samples were drawn from populations with the same or different distributions. Specifically, you learned:

- The Mann-Whitney U test for comparing independent data samples: the nonparametric version of the Student's t-test.
- The Wilcoxon signed-rank test for comparing paired data samples: the nonparametric version of the paired Student's t-test.

 The Kruskal-Wallis H and Friedman tests for comparing more than two data samples: the nonparametric version of the ANOVA and repeated measures ANOVA tests.

#### 28.9.5 Next

In the next section, you will discover how to calculate tests of independence for categorical variables.
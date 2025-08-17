# Chapter 23

# Rank Data

A large portion of the field of statistics and statistical methods is dedicated to data where the distribution is known. Samples of data where we already know or can easily identify the distribution of are called parametric data. Often, parametric is used to refer to data that was drawn from a Gaussian distribution in common usage. Data in which the distribution is unknown or cannot be easily identified is called nonparametric.

In the case where you are working with nonparametric data, specialized nonparametric statistical methods can be used that discard all information about the distribution. As such, these methods are often referred to as distribution-free methods. In this tutorial, you will discover nonparametric statistics and their role in applied machine learning. After completing this tutorial, you will know:

- The difference between parametric and nonparametric data.
- How to rank data in order to discard all information about the data's distribution.
- Example of statistical methods that can be used for ranked data.

Let's get started.

## 23.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- 1. Parametric Data
- 2. Nonparametric Data
- 3. Ranking Data
- 4. Working with Ranked Data

## 23.2 Parametric Data

Parametric data is a sample of data drawn from a known data distribution. This means that we already know the distribution or we have identified the distribution, and that we know the parameters of the distribution. Often, parametric is shorthand for real-valued data drawn from a Gaussian distribution. This is a useful shorthand, but strictly this is not entirely accurate. If we have parametric data, we can use parametric methods. Continuing with the shorthand of parametric meaning Gaussian. If we have parametric data, we can harness the entire suite of statistical methods developed for data assuming a Gaussian distribution, such as:

- Summary statistics.
- Correlation between variables.
- Significance tests for comparing means.

In general, we prefer to work with parametric data, and even go so far as to use data preparation methods that make data parametric, such as data transforms, so that we can harness these well-understood statistical methods.

## 23.3 Nonparametric Data

Data that does not fit a known or well-understood distribution is referred to as nonparametric data. Data could be nonparametric for many reasons, such as:

- Data is not real-valued, but instead is ordinal, intervals, or some other form.
- Data is real-valued but does not fit a well understood shape.
- Data is almost parametric but contains outliers, multiple peaks, a shift, or some other feature.

There are a suite of methods that we can use for nonparametric data called nonparametric statistical methods. In fact, most parametric methods have an equivalent nonparametric version. In general, the findings from nonparametric methods are less powerful than their parametric counterparts, namely because they must be generalized to work for all types of data. We can still use them for inference and make claims about findings and results, but they will not hold the same weight as similar claims with parametric methods. Information about the distribution is discarded.

In the case of ordinal or interval data, nonparametric statistics are the only type of statistics that can be used. For real-valued data, nonparametric statistical methods are required in applied machine learning when you are trying to make claims on data that does not fit the familiar Gaussian distribution.

## 23.4 Ranking Data

Before a nonparametric statistical method can be applied, the data must be converted into a rank format. As such, statistical methods that expect data in rank format are sometimes called rank statistics, such as rank correlation and rank statistical hypothesis tests. Ranking data is exactly as its name suggests. The procedure is as follows:

- Sort all data in the sample in ascending order.
- Assign an integer rank from 1 to N for each unique value in the data sample.

For example, imagine we have the following data sample, presented as a column:

0.550

0.184

0.431

0.020

0.620

#### Listing 23.1: Example of a small dataset.

We can sort it as follows:

0.020 0.184

0.431

0.550

0.620

#### Listing 23.2: Example of a sorted dataset.

Then assign a rank to each value, starting at 1:

|  | 1 = 0.021055 |
|--|--------------|
|  | 2 = 0.404622 |
|  | 3 = 0.488733 |
|  | 4 = 0.618510 |
|  | 5 = 0.832803 |

Listing 23.3: Example of a ranked sorted dataset.

We can then apply this procedure to another data sample and start using nonparametric statistical methods. There are variations on this procedure for special circumstances such as handling ties, using a reverse ranking, and using a fractional rank score, but the general properties hold. The SciPy library provides the rankdata() function to rank numerical data, which supports a number of variations on ranking. The example below demonstrates how to rank a numerical dataset.

```
# example of ranking real-valued observations
from numpy.random import rand
from numpy.random import seed
from scipy.stats import rankdata
# seed random number generator
seed(1)
# generate dataset
data = rand(1000)
```

```
# review first 10 samples
print(data[:10])
# rank data
ranked = rankdata(data)
# review first 10 ranked samples
print(ranked[:10])
```

Listing 23.4: Example of ranking a sample dataset.

Running the example first generates a sample of 1,000 random numbers from a uniform distribution, then ranks the data sample and prints the result.

```
[4.17022005e-01 7.20324493e-01 1.14374817e-04 3.02332573e-01
1.46755891e-01 9.23385948e-02 1.86260211e-01 3.45560727e-01
3.96767474e-01 5.38816734e-01]
[408. 721. 1. 300. 151. 93. 186. 342. 385. 535.]
```

Listing 23.5: Example output from ranking a sample dataset.

## 23.5 Working with Ranked Data

There are statistical tools that you can use to check if your sample data fits a given distribution. For example, if we take nonparametric data as data that does not look Gaussian, then you can use statistical methods that quantify how Gaussian a sample of data is and use nonparametric methods if the data fails those tests.

Three examples of statistical methods for normality testing, as it is called, are:

- Shapiro-Wilk Test.
- D'Agostino's K<sup>2</sup> Test.
- Anderson-Darling Test.

Once you have decided to use nonparametric statistics, you must then rank your data. In fact, most of the tools that you use for inference will perform the ranking of the sample data automatically. Nevertheless, it is important to understand how your sample data is being transformed prior to performing the tests. In applied machine learning, there are two main types of questions that you may have about your data that you can address with nonparametric statistical methods.

### 23.5.1 Relationship Between Variables

Methods for quantifying the dependency between variables are called correlation methods. Two nonparametric statistical correlation methods that you can use are:

- Spearman's Rank Correlation.
- Kendall's Rank Correlation.
- Goodman and Kruskal's Rank Correlation.
- Somers' Rank Correlation.

## 23.5.2 Compare Sample Means

Methods for quantifying whether the mean between two populations is significantly different are called statistical significance tests. Three nonparametric statistical significance tests that you can use are:

- Mann-Whitney U Test.
- Wilcoxon Signed-Rank Test.
- Kruskal-Wallis H Test.
- Friedman Test.

## 23.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- List three examples of when you think you might need to use nonparametric statistical methods in an applied machine learning project.
- Develop your own example to demonstrate the capabilities of the rankdata() function.
- Write your own function to rank a provided univariate dataset.

If you explore any of these extensions, I'd love to know.

## 23.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

## 23.7.1 Books

- All of Nonparametric Statistics, 2007. <http://amzn.to/2oGv2A6>
- Practical Nonparametric Statistics, 1999. <http://amzn.to/2CXUe9y>
- Applied Nonparametric Statistics, 2000. <http://amzn.to/2t9iMN6>

## 23.7.2 API

 scipy.stats.rankdata API. <http://scipy.github.io/devdocs/generated/scipy.stats.rankdata.html>

## 23.7.3 Articles

- Parametric statistics on Wikipedia. [https://en.wikipedia.org/wiki/Parametric\\_statistics](https://en.wikipedia.org/wiki/Parametric_statistics)
- Nonparametric statistics on Wikipedia. [https://en.wikipedia.org/wiki/Nonparametric\\_statistics](https://en.wikipedia.org/wiki/Nonparametric_statistics)
- Ranking on Wikipedia. <https://en.wikipedia.org/wiki/Ranking>
- Rank correlation on Wikipedia. [https://en.wikipedia.org/wiki/Rank\\_correlation](https://en.wikipedia.org/wiki/Rank_correlation)
- Normality test on Wikipedia. [https://en.wikipedia.org/wiki/Normality\\_test](https://en.wikipedia.org/wiki/Normality_test)

## 23.8 Summary

In this tutorial, you discovered nonparametric statistics and their role in applied machine learning. Specifically, you learned:

- The difference between parametric and nonparametric data.
- How to rank data in order to discard all information about the data's distribution.
- Example of statistical methods that can be used for ranked data.

### 23.8.1 Next

In the next section, you will discover statistical methods for determining whether a sample of data was drawn from a Gaussian distribution or not.
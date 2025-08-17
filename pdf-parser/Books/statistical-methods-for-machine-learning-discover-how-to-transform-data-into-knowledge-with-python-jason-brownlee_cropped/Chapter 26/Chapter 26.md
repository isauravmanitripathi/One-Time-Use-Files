# Chapter 26

## 5-Number Summary

Data summarization provides a convenient way to describe all of the values in a data sample with just a few statistical values. The mean and standard deviation are used to summarize data with a Gaussian distribution, but may not be meaningful, or could even be misleading, if your data sample has a non-Gaussian distribution. In this tutorial, you will discover the five-number summary for describing the distribution of a data sample without assuming a specific data distribution. After completing this tutorial, you will know:

- Data summarization, such as calculating the mean and standard deviation, are only meaningful for the Gaussian distribution.
- The five-number summary can be used to describe a data sample with any distribution.
- How to calculate the five-number summary in Python.

Let's get started.

### 26.1 Tutorial Overview

This tutorial is divided into 4 parts; they are:

- 1. Nonparametric Data Summarization
- 2. Five-Number Summary
- 3. How to Calculate the Five-Number Summary
- 4. Use of the Five-Number Summary

## 26.2 Nonparametric Data Summarization

Data summarization techniques provide a way to describe the distribution of data using a few key measurements. The most common example of data summarization is the calculation of the mean and standard deviation for data that has a Gaussian distribution. With these two parameters alone, you can understand and re-create the distribution of the data. The data summary can compress as few as tens or as many as millions individual observations.

The problem is, you cannot easily calculate the mean and standard deviation of data that does not have a Gaussian distribution. Technically, you can calculate these quantities, but they do not summarize the data distribution; in fact, they can be very misleading. In the case of data that does not have a Gaussian distribution, you can summarize the data sample using the five-number summary.

### 26.3 Five-Number Summary

The five-number summary, or 5-number summary for short, is a nonparametric data summarization technique. It is sometimes called the Tukey 5-number summary because it was recommended by John Tukey. It can be used to describe the distribution of data samples for data with any distribution.

As a standard summary for general use, the 5-number summary provides about the right amount of detail.

— Page 37, Understanding Robust and Exploratory Data Analysis, 2000.

The five-number summary involves the calculation of 5 summary statistical quantities: namely:

- Median: The middle value in the sample, also called the 50th percentile or the 2nd quartile.
- 1st Quartile: The 25th percentile.
- 3rd Quartile: The 75th percentile.
- Minimum: The smallest observation in the sample.
- Maximum: The largest observation in the sample.

A quartile is an observed value at a point that aids in splitting the ordered data sample into four equally sized parts. The median, or 2nd Quartile, splits the ordered data sample into two parts, and the 1st and 3rd quartiles split each of those halves into quarters. A percentile is an observed value at a point that aids in splitting the ordered data sample into 100 equally sized portions. Quartiles are often also expressed as percentiles.

Both the quartile and percentile values are examples of rank statistics that can be calculated on a data sample with any distribution. They are used to quickly summarize how much of the data in the distribution is behind or in front of a given observed value. For example, half of the observations are behind and in front of the median of a distribution. Note that quartiles are also calculated in the box and whisker plot, a nonparametric method to graphically summarize the distribution of a data sample.

### 26.4 How to Calculate the Five-Number Summary

Calculating the five-number summary involves finding the observations for each quartile as well as the minimum and maximum observed values from the data sample. If there is no specific value in the ordered data sample for the quartile, such as if there are an even number of observations and we are trying to find the median, then we can calculate the mean of the two closest values, such as the two middle values.

We can calculate arbitrary percentile values in Python using the percentile() NumPy function. We can use this function to calculate the 1st, 2nd (median), and 3rd quartile values. The function takes both an array of observations and a floating point value to specify the percentile to calculate in the range of 0 to 100. It can also takes a list of percentile values to calculate multiple percentiles; for example:

```
...
# calculate quartiles
quartiles = percentile(data, [25, 50, 75])
```

Listing 26.1: Example of calculating quartiles.

By default, the function will calculate a linear interpolation (average) between observations if needed, such as in the case of calculating the median on a sample with an even number of values. The NumPy functions min() and max() can be used to return the smallest and largest values in the data sample; for example:

```
...
# calculate min and max
data_min, data_max = data.min(), data.max()
```

Listing 26.2: Example of calculating min and max.

We can put all of this together. The example below generates a data sample drawn from a uniform distribution between 0 and 1 and summarizes it using the five-number summary.

```
# calculate a 5-number summary
from numpy import percentile
from numpy.random import seed
from numpy.random import rand
# seed random number generator
seed(1)
# generate data sample
data = rand(1000)
# calculate quartiles
quartiles = percentile(data, [25, 50, 75])
# calculate min/max
data_min, data_max = data.min(), data.max()
# display 5-number summary
print('Min: %.3f' % data_min)
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3: %.3f' % quartiles[2])
print('Max: %.3f' % data_max)
```

Listing 26.3: Example of calculating a 5 number summary of a data sample.

Running the example generates the data sample and calculates the five-number summary to describe the sample distribution. We can see that the spread of observations is close to our expectations showing 0.252 for the 25th percentile 0.508 for the 50th percentile, and 0.751 for the 75th percentile, close to the idealized values of 0.250, 0.500, and 0.750 respectively.

Min: 0.000 Q1: 0.252 Median: 0.508 Q3: 0.751 Max: 0.997

Listing 26.4: Example output from calculating a 5 number summary of a data sample.

### 26.5 Use of the Five-Number Summary

The five-number summary can be calculated for a data sample with any distribution. This includes data that has a known distribution, such as a Gaussian or Gaussian-like distribution. I would recommend always calculating the five-number summary, and only moving on to distribution specific summaries, such as mean and standard deviation for the Gaussian, in the case that you can identify the distribution to which the data belongs.

### 26.6 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Describe three examples in a machine learning project where a five-number summary could be calculated.
- Generate a data sample with a Gaussian distribution and calculate the five-number summary.
- Write a function to calculate a 5-number summary for any data sample.

If you explore any of these extensions, I'd love to know.

## 26.7 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 26.7.1 Books

 Understanding Robust and Exploratory Data Analysis, 2000. <https://amzn.to/2Gp2sNW>

#### 26.7.2 API

 numpy.percentile API. <https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.percentile.html>

- numpy.ndarray.min API. [https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.min](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.min.html). [html](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.min.html)
- numpy.ndarray.max API. [https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.max](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.max.html). [html](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.max.html)

### 26.7.3 Articles

- Five-number summary on Wikipedia. [https://en.wikipedia.org/wiki/Five-number\\_summary](https://en.wikipedia.org/wiki/Five-number_summary)
- Quartile on Wikipedia. <https://en.wikipedia.org/wiki/Quartile>
- Percentile on Wikipedia. <https://en.wikipedia.org/wiki/Percentile>

## 26.8 Summary

In this tutorial, you discovered the five-number summary for describing the distribution of a data sample without assuming a specific data distribution. Specifically, you learned:

- Data summarization, such as calculating the mean and standard deviation, are only meaningful for the Gaussian distribution.
- The five-number summary can be used to describe a data sample with any distribution.
- How to calculate the five-number summary in Python.

#### 26.8.1 Next

In the next section, you will discover how to quantify the relationship between two samples regardless of their distribution.
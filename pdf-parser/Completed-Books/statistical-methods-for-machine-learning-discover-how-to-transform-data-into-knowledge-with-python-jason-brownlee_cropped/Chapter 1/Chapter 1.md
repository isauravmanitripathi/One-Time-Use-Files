# Chapter 1

# Introduction to Statistics

Statistics is a collection of tools that you can use to get answers to important questions about data. You can use descriptive statistical methods to transform raw observations into information that you can understand and share. You can use inferential statistical methods to reason from small samples of data to whole domains. In this chapter, you will discover clearly why statistics is important in general and for machine learning and generally the types of methods that are available. After reading this chapter, you will know:

- Statistics is generally considered a prerequisite to the field of applied machine learning.
- We need statistics to help transform observations into information and to answer questions about samples of observations.
- Statistics is a collection of tools developed over hundreds of years for summarizing data and quantifying properties of a domain given a sample of observations.

Let's get started.

## 1.1 Statistics is Required Prerequisite

Machine learning and statistics are two tightly related fields of study. So much so that statisticians refer to machine learning as applied statistics or statistical learning rather than the computer-science-centric name. Machine learning is almost universally presented to beginners assuming that the reader has some background in statistics. We can make this concrete with a few cherry picked examples. Take a look at this quote from the beginning of a popular applied machine learning book titled Applied Predictive Modeling:

... the reader should have some knowledge of basic statistics, including variance, correlation, simple linear regression, and basic hypothesis testing (e.g. p-values and test statistics).

— Page vii, Applied Predictive Modeling, 2013.

Here's another example from the popular Introduction to Statistical Learning book:

We expect that the reader will have had at least one elementary course in statistics.

— Page 9, An Introduction to Statistical Learning with Applications in R, 2013.

Even when statistics is not a prerequisite, some primitive prior knowledge is required as can be seen in this quote from the widely read Programming Collective Intelligence:

... this book does not assume you have any prior knowledge of [...] or statistics. [...] but having some knowledge of trigonometry and basic statistics will help you understand the algorithms.

— Page xiii, Programming Collective Intelligence: Building Smart Web 2.0 Applications, 2007.

In order to be able to understand machine learning, some basic understanding of statistics is required. To see why this is the case, we must first understand why we need the field of statistics in the first place.

## 1.2 Why Learn Statistics?

Raw observations alone are data, but they are not information or knowledge. Data raises questions, such as:

- What is the most common or expected observation?
- What are the limits on the observations?
- What does the data look like?

Although they appear simple, these questions must be answered in order to turn raw observations into information that we can use and share. Beyond raw data, we may design experiments in order to collect observations. From these experimental results we may have more sophisticated questions, such as:

- What variables are most relevant?
- What is the difference in an outcome between two experiments?
- Are the differences real or the result of noise in the data?

Questions of this type are important. The results matter to the project, to stakeholders, and to effective decision making. Statistical methods are required to find answers to the questions that we have about data. We can see that in order to both understand the data used to train a machine learning model and to interpret the results of testing different machine learning models, that statistical methods are required. This is just the tip of the iceberg as each step in a predictive modeling project will require the use of a statistical method.

## 1.3 What is Statistics?

Statistics is a subfield of mathematics. It refers to a collection of methods for working with data and using data to answer questions.

Statistics is the art of making numerical conjectures about puzzling questions. [...] The methods were developed over several hundred years by people who were looking for answers to their questions.

— Page xiii, Statistics, Fourth Edition, 2007.

It is because the field is comprised of a grab bag of methods for working with data that it can seem large and amorphous to beginners. It can be hard to see the line between methods that belong to statistics and methods that belong to other fields of study. Often a technique can be both a classical method from statistics and a modern algorithm used for feature selection or modeling. Although a working knowledge of statistics does not require deep theoretical knowledge, some important and easy-to-digest theorems from the relationship between statistics and probability can provide a valuable foundation.

Two examples include the law of large numbers and the central limit theorem; the first aids in understanding why bigger samples are often better and the second provides a foundation for how we can compare the expected values between samples (e.g mean values). When it comes to the statistical tools that we use in practice, it can be helpful to divide the field of statistics into two large groups of methods: descriptive statistics for summarizing data and inferential statistics for drawing conclusions from samples of data.

Statistics allow researchers to collect information, or data, from a large number of people and then summarize their typical experience. [...] Statistics are also used to reach conclusions about general differences between groups. [...] Statistics can also be used to see if scores on two variables are related and to make predictions.

— Pages ix-x, Statistics in Plain English, Third Edition, 2010.

#### 1.3.1 Descriptive Statistics

Descriptive statistics refer to methods for summarizing raw observations into information that we can understand and share. Commonly, we think of descriptive statistics as the calculation of statistical values on samples of data in order to summarize properties of the sample of data, such as the common expected value (e.g. the mean or median) and the spread of the data (e.g. the variance or standard deviation). Descriptive statistics may also cover graphical methods that can be used to visualize samples of data. Charts and graphics can provide a useful qualitative understanding of both the shape or distribution of observations as well as how variables may relate to each other.

#### 1.3.2 Inferential Statistics

Inferential statistics is a fancy name for methods that aid in quantifying properties of the domain or population from a smaller set of obtained observations called a sample. Commonly, we think of inferential statistics as the estimation of quantities from the population distribution, such as the expected value or the amount of spread.

More sophisticated statistical inference tools can be used to quantify the likelihood of observing data samples given an assumption. These are often referred to as tools for statistical hypothesis testing, where the base assumption of a test is called the null hypothesis. There are many examples of inferential statistical methods given the range of hypotheses we may assume and the constraints we may impose on the data in order to increase the power or likelihood that the finding of the test is correct.

## 1.4 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 1.4.1 Books

- Applied Predictive Modeling, 2013. <https://amzn.to/2InAS0T>
- An Introduction to Statistical Learning with Applications in R, 2013. <https://amzn.to/2Gvhkqz>
- Programming Collective Intelligence: Building Smart Web 2.0 Applications, 2007. <https://amzn.to/2GIN9jc>
- Statistics, Fourth Edition, 2007. <https://amzn.to/2pUA0tU>
- All of Statistics: A Concise Course in Statistical Inference, 2004. <https://amzn.to/2H224Tp>
- Statistics in Plain English, Third Edition, 2010. <https://amzn.to/2Gv0A2V>

#### 1.4.2 Articles

- Statistics on Wikipedia. <https://en.wikipedia.org/wiki/Statistics>
- Portal:Statistics on Wikipedia. <https://en.wikipedia.org/wiki/Portal:Statistics>
- List of statistics articles on Wikipedia. [https://en.wikipedia.org/wiki/List\\_of\\_statistics\\_articles](https://en.wikipedia.org/wiki/List_of_statistics_articles)
- Mathematical statistics on Wikipedia. [https://en.wikipedia.org/wiki/Mathematical\\_statistics](https://en.wikipedia.org/wiki/Mathematical_statistics)
- History of statistics on Wikipedia. [https://en.wikipedia.org/wiki/History\\_of\\_statistics](https://en.wikipedia.org/wiki/History_of_statistics)

- Descriptive Statistics on Wikipedia. [https://en.wikipedia.org/wiki/Descriptive\\_statistics](https://en.wikipedia.org/wiki/Descriptive_statistics)
- Statistical Inference on Wikipedia. [https://en.wikipedia.org/wiki/Statistical\\_inference](https://en.wikipedia.org/wiki/Statistical_inference)

## 1.5 Summary

In this chapter, you discovered clearly why statistics is important in general and for machine learning, and generally the types of methods that are available. Specifically, you learned:

- Statistics is generally considered a prerequisite to the field of applied machine learning.
- We need statistics to help transform observations into information and to answer questions about samples of observations.
- Statistics is a collection of tools developed over hundreds of years for summarizing data and quantifying properties of a domain given a sample of observations.

#### 1.5.1 Next

In the next section, you will discover the tight relationship and differences between machine learning and statistics.
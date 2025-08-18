# Chapter 7

# Understand Your Data Using Descriptive Statistics

You must become intimate with your data. Any machine learning models that you build are only as good as the data that you provide them. The first step in understanding your data is to actually look at some raw values and calculate some basic statistics. In this lesson you will discover how you can quickly get a handle on your dataset with descriptive statistics examples and recipes in R.

After completing this lesson you will know 8 techniques that you can use in order to learn more about your data:

- How to quickly understand your data by looking at the raw values, dimensions, data types and class distributions.
- How to understand the distribution of your data with summary statistics, standard deviations and skew.
- How to understand the relationships between attributes by calculating correlations.

These recipes are perfect if you only know a little bit about statistics. Let's get started.

### 7.1 You Must Understand Your Data

Understanding the data that you have is critically important. You can run techniques and algorithms on your data, but it is not until you take the time to truly understand your dataset that you can fully understand the context of the results you achieve.

#### 7.1.1 Better Understanding Equals Better Results

A deeper understanding of your data will give you better results. Taking the time to study the data you have will help you in ways that are less obvious. You build an intuition for the data and for the entities that individual records or observations represent. These can bias you towards specific techniques (for better or worse), but you can also be inspired. For example, examining your data in detail may trigger ideas for specific techniques to investigate:

- Data Cleaning : You may discover missing or corrupt data and think of various data cleaning operations to perform such as marking or removing bad data and imputing missing data.
- Data Transforms : You may discover that some attributes have familiar distributions such as Gaussian or exponential giving you ideas of scaling or other transforms you could apply.
- Data Modeling : You may notice properties of the data such as distributions or data types that suggest the use (or to not use) specific machine learning algorithms.

#### 7.1.2 Use Descriptive Statistics

You need to look at your data. And you need to look at your data from different perspectives. Inspecting your data will help you to build up your intuition and prompt you to start asking questions about the data that you have. Multiple perspectives on your data will challenge you to think about the data differently, helping you to ask more and better questions.

The first and best place to start is to calculate basic summary descriptive statistics on your data. You need to learn the shape, size, type and general layout of the data that you have. Let's look at some ways that you can summarize your data using R. In the next section you will discover 8 quick and simple ways to summarize your dataset.

### 7.2 Peek At Your Data

The very first thing to do is to just look at some raw data from your dataset. If your dataset is small you might be able to display it all on the screen. Often it is not, so you can take a small sample and review that.

```
# load the package
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# display first 20 rows of data
head(PimaIndiansDiabetes, n=20)
```

Listing 7.1: Display first 20 rows of data.

The head() function will display the first 20 rows of data for you to review and think about.

|    |    |     |    |    |   |          |       |    | pregnant glucose pressure triceps insulin mass pedigree age diabetes |  |
|----|----|-----|----|----|---|----------|-------|----|----------------------------------------------------------------------|--|
| 1  | 6  | 148 | 72 | 35 |   | 0 33.6   | 0.627 | 50 | pos                                                                  |  |
| 2  | 1  | 85  | 66 | 29 |   | 0 26.6   | 0.351 | 31 | neg                                                                  |  |
| 3  | 8  | 183 | 64 | 0  |   | 0 23.3   | 0.672 | 32 | pos                                                                  |  |
| 4  | 1  | 89  | 66 | 23 |   | 94 28.1  | 0.167 | 21 | neg                                                                  |  |
| 5  | 0  | 137 | 40 | 35 |   | 168 43.1 | 2.288 | 33 | pos                                                                  |  |
| 6  | 5  | 116 | 74 | 0  |   | 0 25.6   | 0.201 | 30 | neg                                                                  |  |
| 7  | 3  | 78  | 50 | 32 |   | 88 31.0  | 0.248 | 26 | pos                                                                  |  |
| 8  | 10 | 115 | 0  | 0  |   | 0 35.3   | 0.134 | 29 | neg                                                                  |  |
| 9  | 2  | 197 | 70 | 45 |   | 543 30.5 | 0.158 | 53 | pos                                                                  |  |
| 10 | 8  | 125 | 96 | 0  | 0 | 0.0      | 0.232 | 54 | pos                                                                  |  |
| 11 | 4  | 110 | 92 | 0  |   | 0 37.6   | 0.191 | 30 | neg                                                                  |  |
| 12 | 10 | 168 | 74 | 0  |   | 0 38.0   | 0.537 | 34 | pos                                                                  |  |
| 13 | 10 | 139 | 80 | 0  |   | 0 27.1   | 1.441 | 57 | neg                                                                  |  |
| 14 | 1  | 189 | 60 | 23 |   | 846 30.1 | 0.398 | 59 | pos                                                                  |  |

| 15 | 5 | 166 | 72 | 19 | 175 25.8 | 0.587<br>51 | pos |
|----|---|-----|----|----|----------|-------------|-----|
| 16 | 7 | 100 | 0  | 0  | 0 30.0   | 0.484<br>32 | pos |
| 17 | 0 | 118 | 84 | 47 | 230 45.8 | 0.551<br>31 | pos |
| 18 | 7 | 107 | 74 | 0  | 0 29.6   | 0.254<br>31 | pos |
| 19 | 1 | 103 | 30 | 38 | 83 43.3  | 0.183<br>33 | neg |
| 20 | 1 | 115 | 70 | 30 | 96 34.6  | 0.529<br>32 | pos |

Listing 7.2: Output of first 20 rows.

### 7.3 Dimensions of Your Data

How much data do you have? You may have a general idea, but it is much better to have a precise figure. If you have a lot of instances, you may need to work with a smaller sample of the data so that model training and evaluation is computationally tractable. If you have a vast number of attributes, you may need to select those that are most relevant. If you have more attributes than instances you may need to select specific modeling techniques.

```
# load the packages
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# display the dimensions of the dataset
dim(PimaIndiansDiabetes)
```

Listing 7.3: Calculate dimensions.

This shows the number of rows and columns in your loaded dataset.

[1] 768 9

Listing 7.4: Output dimensions.

### 7.4 Data Types

You need to know the types of the attributes in your data. The types will indicate the types of further analysis, types of visualization and even the types of machine learning algorithms that you can use. Additionally, perhaps some attributes were loaded as one type (e.g. integer) and could in fact be represented as another type (e.g. a categorical factor). Inspecting the types helps expose these issues and spark ideas early.

```
# load package
library(mlbench)
# load dataset
data(BostonHousing)
# list types for each attribute
sapply(BostonHousing, class)
```

Listing 7.5: Calculate data types.

This lists the data type of each attribute in your dataset.

| crim                | zn                            | indus | chas | nox                                                                                      | rm | age | dis | rad | tax |
|---------------------|-------------------------------|-------|------|------------------------------------------------------------------------------------------|----|-----|-----|-----|-----|
|                     | ptratio                       | b     |      |                                                                                          |    |     |     |     |     |
|                     |                               |       |      | "numeric" "numeric" "numeric" "factor" "numeric" "numeric" "numeric" "numeric" "numeric" |    |     |     |     |     |
|                     | "numeric" "numeric" "numeric" |       |      |                                                                                          |    |     |     |     |     |
| lstat               | medv                          |       |      |                                                                                          |    |     |     |     |     |
| "numeric" "numeric" |                               |       |      |                                                                                          |    |     |     |     |     |

Listing 7.6: Output data types.

## 7.5 Class Distribution

In a classification problem you must know the proportion of instances that belong to each class label. This is important because it may highlight an imbalance in the data, that if severe may need to be addressed with rebalancing techniques. In the case of a multi-class classification problem it may expose a class with a small or zero instances that may be candidates for removing from the dataset.

```
# load the packages
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# distribution of class variable
y <- PimaIndiansDiabetes$diabetes
cbind(freq=table(y), percentage=prop.table(table(y))*100)
```

Listing 7.7: Calculate class breakdown.

This recipe creates a useful table showing the number of instances that belong to each class as well as the percentage that this represents from the entire dataset.

freq percentage neg 500 65.10417 pos 268 34.89583

Listing 7.8: Output class breakdown.

# 7.6 Data Summary

There is a most valuable function called summary() that summarizes each attribute in your dataset in turn. The function creates a table for each attribute and lists a breakdown of values. Factors are described as counts next to each class label. Numerical attributes are described using the properties:

- Min
- 25th percentile
- Median
- Mean

- 75th percentile
- Max

The breakdown also includes an indication of the number of missing values for an attribute (marked N/A).

```
# load the iris dataset
data(iris)
# summarize the dataset
summary(iris)
```

Listing 7.9: Calculate the summary of the attributes.

You can see that this recipe produces a lot of information for you to review. Take your time and work through each attribute in turn.

```
Sepal.Length Sepal.Width Petal.Length Petal.Width Species
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100 setosa :50
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300 versicolor:50
Median :5.800 Median :3.000 Median :4.350 Median :1.300 virginica :50
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
```

Listing 7.10: Output of the summary of attributes.

### 7.7 Standard Deviations

One thing missing from the summary() function above are the standard deviations. The standard deviation along with the mean are useful to know if the data has a Gaussian (or nearly Gaussian) distribution. For example, it can be useful for a quick and dirty outlier removal tool, where any values that are more than three times the standard deviation from the mean are outside of 99.7% of the data.

```
# load the packages
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# calculate standard deviation for all attributes
sapply(PimaIndiansDiabetes[,1:8], sd)
```

Listing 7.11: Calculate standard deviations.

This calculates the standard deviation for each numeric attribute in the dataset.

| pregnant | glucose | pressure | triceps | insulin                                                                               | mass | pedigree | age |
|----------|---------|----------|---------|---------------------------------------------------------------------------------------|------|----------|-----|
|          |         |          |         | 3.3695781 31.9726182 19.3558072 15.9522176 115.2440024 7.8841603 0.3313286 11.7602315 |      |          |     |

Listing 7.12: Output of standard deviations

## 7.8 Skewness

If a distribution looks nearly-Gaussian but is pushed far left or right it is useful to know the skew. Getting a feeling for the skew is much easier with plots of the data, such as a histogram or density plot. It is harder to tell from looking at means, standard deviations and quartiles. Nevertheless, calculating the skew up-front gives you a reference that you can use later if you decide to correct the skew for an attribute.

```
# load packages
library(mlbench)
library(e1071)
# load the dataset
data(PimaIndiansDiabetes)
# calculate skewness for each variable
skew <- apply(PimaIndiansDiabetes[,1:8], 2, skewness)
# display skewness, larger/smaller deviations from 0 show more skew
print(skew)
```

Listing 7.13: Calculate skewness.

The further the distribution of the skew value from zero, the larger the skew to the left (negative skew value) or right (positive skew value).

pregnant glucose pressure triceps insulin mass pedigree age 0.8981549 0.1730754 -1.8364126 0.1089456 2.2633826 -0.4273073 1.9124179 1.1251880

Listing 7.14: Output of skewness.

### 7.9 Correlations

It is important to observe and think about how attributes relate to each other. For numeric attributes, an excellent way to think about attribute-to-attribute interactions is to calculate correlations for each pair of attributes.

```
# load the packages
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# calculate a correlation matrix for numeric variables
correlations <- cor(PimaIndiansDiabetes[,1:8])
# display the correlation matrix
print(correlations)
```

Listing 7.15: Calculate correlations.

This creates a symmetrical table of all pairs of attribute correlations for numerical data. Deviations from zero show more positive or negative correlation. Values above 0.75 or below -0.75 are perhaps more interesting as they show a high correlation or high negative correlation. Values of 1 and -1 show full positive or negative correlation.

pregnant glucose pressure triceps insulin mass pedigree age pregnant 1.00000000 0.12945867 0.14128198 -0.08167177 -0.07353461 0.01768309 -0.03352267 0.54434123

| glucose    |                                                                                        |  |  |  |  | 0.12945867 1.00000000 0.15258959 0.05732789 0.33135711 0.22107107 0.13733730 |                                                                                |
|------------|----------------------------------------------------------------------------------------|--|--|--|--|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| 0.26351432 |                                                                                        |  |  |  |  |                                                                              |                                                                                |
|            | pressure 0.14128198 0.15258959 1.00000000 0.20737054 0.08893338 0.28180529 0.04126495  |  |  |  |  |                                                                              |                                                                                |
|            | 0.23952795                                                                             |  |  |  |  |                                                                              |                                                                                |
|            | triceps -0.08167177 0.05732789 0.20737054 1.00000000 0.43678257 0.39257320 0.18392757  |  |  |  |  |                                                                              |                                                                                |
|            | -0.11397026                                                                            |  |  |  |  |                                                                              |                                                                                |
|            | insulin -0.07353461 0.33135711 0.08893338 0.43678257 1.00000000 0.19785906 0.18507093  |  |  |  |  |                                                                              |                                                                                |
|            | -0.04216295                                                                            |  |  |  |  |                                                                              |                                                                                |
| mass       |                                                                                        |  |  |  |  | 0.01768309 0.22107107 0.28180529 0.39257320 0.19785906 1.00000000 0.14064695 |                                                                                |
|            | 0.03624187                                                                             |  |  |  |  |                                                                              |                                                                                |
|            | pedigree -0.03352267 0.13733730 0.04126495 0.18392757 0.18507093 0.14064695 1.00000000 |  |  |  |  |                                                                              |                                                                                |
|            | 0.03356131                                                                             |  |  |  |  |                                                                              |                                                                                |
| age        |                                                                                        |  |  |  |  |                                                                              | 0.54434123 0.26351432 0.23952795 -0.11397026 -0.04216295 0.03624187 0.03356131 |
|            | 1.00000000                                                                             |  |  |  |  |                                                                              |                                                                                |

Listing 7.16: Output of correlations.

### 7.10 Tips To Remember

This section gives you some tips to remember when reviewing your data using summary statistics.

- Review the numbers : Generating the summary statistics is not enough. Take a moment to pause, read and really think about the numbers you are seeing.
- Ask why : Review your numbers and ask a lot of questions. How and why are you seeing specific numbers. Think about how the numbers relate to the problem domain in general and specific entities that observations relate to.
- Write down ideas : Write down your observations and ideas. Keep a small text file or note pad and jot down all of the ideas for how variables may relate to each other, for what numbers mean, and ideas for techniques to try later. The things you write down now while the data is fresh will be very valuable later when you are trying to think up new things to try.

### 7.11 Summary

In this lesson you discovered the importance of describing your dataset before you start work on your machine learning project. You discovered 8 different ways to summarize your dataset using R:

- Peek At Your Data.
- Dimensions of Your Data.
- Data Types.
- Class Distribution.
- Data Summary.

- Standard Deviations.
- Skewness.
- Correlations.

You do not need to be good at statistics. The statistics used in this lesson are very simple, but you may have forgotten some of the basics. You can quickly browse through Wikipedia for topics like Mean, Standard Deviation and Quartiles to refresh your knowledge.

#### 7.11.1 Next Step

This lesson was all about techniques that you can use to understand your dataset analytically. Up next you will discover techniques that you can use to better understand your data quantitatively using data visualization.
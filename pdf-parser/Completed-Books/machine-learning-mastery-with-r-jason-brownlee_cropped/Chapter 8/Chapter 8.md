# Chapter 8

# Understand Your Data Using Data Visualization

You must understand your data to get the best results from machine learning algorithms. Data visualization is perhaps the fastest and most useful way to summarize and learn more about your data. In this lesson you will discover exactly how you can use data visualization to better understand your data for machine learning using R. After completing this lesson, you will know:

- 1. How to create plots in order to understand each attribute standalone.
- 2. How to create plots in order to understand the relationships between attributes.

Let's get started.

# 8.1 Understand Your Data To Get The Best Results

A better understanding of your data will yield better results from machine learning algorithms. You will be able to clean, transform and best present the data that you have. The better that the data exposes the structure of the problem to the machine learning algorithms, the more accurate your models will be. Additionally, a deeper understanding of your data may even suggest at specific machine learning algorithms to try on your data.

### 8.1.1 Visualize Your Data For Faster Understanding

The fastest way to improve your understanding of your dataset is to visualize it. Visualization means creating charts and plots from the raw data. Plots of the distribution or spread of attributes can help you spot outliers, strange or invalid data and give you an idea of possible data transformations you could apply.

Plots of the relationships between attributes can give you an idea of attributes that might be redundant, resampling methods that may be needed and ultimately how difficult a prediction problem might be. In the next section you will discover how you can quickly visualize your data in R. This lesson is divided into three parts:

 Visualization Packages: A quick note about your options when it comes to R packages for visualization.

- Univariate Visualization: Plots you can use to understand each attribute standalone.
- Multivariate Visualization: Plots that can help you to better understand the interactions between attributes.

# 8.2 Visualization Packages

There are many ways to visualize data in R, but a few packages have surfaced as perhaps being the most generally useful.

- graphics package: Excellent for fast and basic plots of data.
- lattice package: More pretty plots and more often useful in practice.
- ggplot2 package: Beautiful plots that you want to generate when you need to present results.

I recommend that you stick with simple plots from the graphics package for quick and dirty visualization, and use wrappers around lattice (via the caret package) for more useful multivariate plots. I think ggplot2 plots are excellent and look lovely, but overkill for quick and dirty data visualization.

# 8.3 Univariate Visualization

Univariate plots are plots of individual attributes without interactions. The goal is to learn something about the distribution, central tendency and spread of each attributes.

### 8.3.1 Histograms

Histograms provide a bar chart of a numeric attribute split into bins with the height showing the number of instances that fall into each bin. They are useful to get an indication of the distribution of an attribute.

```
# load the data
data(iris)
# create histograms for each attribute
par(mfrow=c(1,4))
for(i in 1:4) {
 hist(iris[,i], main=names(iris)[i])
}
```

Listing 8.1: Calculate histograms.

You can see that most of the attributes show a Gaussian or multi-modal Gaussian distribution. You can see the measurements of very small flowers in the Petal width and length column.

![](_page_2_Figure_1.jpeg)

Figure 8.1: Histogram Plot in R

### 8.3.2 Density Plots

We can smooth out the histograms to lines using a density plot. These are useful for a more abstract depiction of the distribution of each variable.

```
# load packages
library(lattice)
# load dataset
data(iris)
# create a panel of simpler density plots by attribute
par(mfrow=c(1,4))
for(i in 1:4) {
 plot(density(iris[,i]), main=names(iris)[i])
}
```

Listing 8.2: Calculate density plots.

Using the same dataset from the previous example with histograms, we can see the double Gaussian distribution with petal measurements. We can also see a possible exponential (Lapacianlike) distribution for the Sepal width.

### 8.3.3 Box And Whisker Plots

We can look at the distribution of the data a different way using box and whisker plots. The box captures the middle 50% of the data, the line shows the median and the whiskers of the plots show the reasonable extent of data. Any dots outside the whiskers are good candidates for outliers.

```
# load dataset
data(iris)
# Create separate boxplots for each attribute
par(mfrow=c(1,4))
for(i in 1:4) {
 boxplot(iris[,i], main=names(iris)[i])
```

![](_page_3_Figure_1.jpeg)

Figure 8.2: Density Plots in R

![](_page_3_Figure_3.jpeg)

We can see that the data all has a similar range (and the same units of centimeters). We can also see that Sepal width may have a few outlier values for this data sample.

![](_page_3_Figure_5.jpeg)

Figure 8.3: Box and Whisker Plots in R

### 8.3.4 Bar Plots

}

[caption=Calculate bar plots.] In datasets that have categorical rather than numeric attributes, we can create bar plots that given an idea of the proportion of instances that belong to each category.

```
# load the package
library(mlbench)
```

### 8.3. Univariate Visualization 51

```
# load the dataset
data(BreastCancer)
# create a bar plot of each categorical attribute
par(mfrow=c(2,4))
for(i in 2:9) {
 counts <- table(BreastCancer[,i])
 name <- names(BreastCancer)[i]
 barplot(counts, main=name)
}
```

We can see that some plots have a good mixed distribution and others show a few labels with the overwhelming number of instances.

![](_page_4_Figure_3.jpeg)

Figure 8.4: Bar Plots in R

### 8.3.5 Missing Plot

Missing data can have a big impact on modeling. Some techniques ignore missing data, others break. You can use a missing plot to get a quick idea of the amount of missing data in your dataset. The x-axis shows attributes and the y-axis shows instances. Horizontal lines indicate missing data for an instance, vertical blocks represent missing data for an attribute.

| # load packages                                        |
|--------------------------------------------------------|
| library(Amelia)                                        |
| library(mlbench)                                       |
| # load dataset                                         |
| data(Soybean)                                          |
| # create a missing map                                 |
| missmap(Soybean, col=c("black", "grey"), legend=FALSE) |
|                                                        |

![](_page_5_Figure_2.jpeg)

We can see that some instances have a lot of missing data across some or most of the attributes.

![](_page_5_Figure_4.jpeg)

Figure 8.5: Missing Map in R

# 8.4 Multivariate Visualization

Multivariate plots are plots of the relationship or interactions between attributes. The goal is to learn something about the distribution, central tendency and spread over groups of data, typically pairs of attributes.

### 8.4.1 Correlation Plot

We can calculate the correlation between each pair of numeric attributes. These pair-wise correlations can be plotted in a correlation matrix to given an idea of which attributes change together.

```
# load package
library(corrplot)
# load the data
data(iris)
# calculate correlations
correlations <- cor(iris[,1:4])
# create correlation plot
corrplot(correlations, method="circle")V
```

Listing 8.5: Calculate correlation plot.

A dot-representation was used where blue represents positive correlation and red negative. The larger the dot the larger the correlation. We can see that the matrix is symmetrical and that the diagonal attributes are perfectly positively correlated (because it shows the correlation of each attribute with itself). We can see that some of the attributes are highly correlated.

![](_page_6_Figure_6.jpeg)

Figure 8.6: Correlation Matrix Plot in R

### 8.4.2 Scatterplot Matrix

A scatterplot plots two variables together, one on each of the x- and y-axises with points showing the interaction. The spread of the points indicates the relationship between the attributes. You can create scatter plots for all pairs of attributes in your dataset, called a scatterplot matrix.

```
# load the data
data(iris)
# pair-wise scatterplots of all 4 attributes
pairs(iris)
```

![](_page_7_Figure_4.jpeg)

Note that the matrix is symmetrical, showing the same plots with axises reversed. This aids in looking at your data from multiple perspectives. Note the linear (diagonal line) relationship between petal length and width.

![](_page_7_Figure_6.jpeg)

Figure 8.7: Scatterplot Matrix Plot in R

### 8.4.3 Scatterplot Matrix By Class

The points in a scatterplot matrix can be colored by the class label in classification problems. This can help to spot clear (or unclear) separation of classes and perhaps give an idea of how

difficult the problem may be.

```
# load the data
data(iris)
# pair-wise scatterplots colored by class
pairs(Species~., data=iris, col=iris$Species)
```

Listing 8.7: Calculate scatterplot matrix by class.

Note the clear separation of the points by class label on most pair-wise plots.

![](_page_8_Figure_5.jpeg)

Figure 8.8: Scatterplot Matrix Plot By Class in R

### 8.4.4 Density Plots By Class

We can review the density distribution of each attribute broken down by class value. Like the scatterplot matrix, the density plot by class can help see the separation of classes. It can also help to understand the overlap in class values for an attribute.

```
# load the package
library(caret)
# load the data
data(iris)
# density plots for each attribute by class value
```

```
x <- iris[,1:4]
y <- iris[,5]
scales <- list(x=list(relation="free"), y=list(relation="free"))
featurePlot(x=x, y=y, plot="density", scales=scales)
```

Listing 8.8: Calculate density plots by class.

We can see that some classes do not overlap at all (e.g. Petal Length) where as with other attributes there are hard to tease apart (e.g. Sepal Width).

![](_page_9_Figure_4.jpeg)

Figure 8.9: Density Plot By Class in R

### 8.4.5 Box And Whisker Plots By Class

We can also review the boxplot distributions of each attribute by class value. This too can help in understanding how each attribute relates to the class value, but from a different perspective to that of the density plots.

```
# load the package
library(caret)
# load the iris dataset
data(iris)
```

```
# box and whisker plots for each attribute by class value
x <- iris[,1:4]
y <- iris[,5]
featurePlot(x=x, y=y, plot="box")
```

Listing 8.9: Calculate box and whisker plots by class.

These plots help to understand the overlap and separation of the attribute-class groups. We can see some good separation of the Setosa class for the Petal Length attribute.

![](_page_10_Figure_4.jpeg)

Figure 8.10: Box and Whisker Plots By Class in R

# 8.5 Tips For Data Visualization

- Review Plots. Actually take the time to look at the plots you have generated and think about them. Try to relate what you are seeing to the general problem domain as well as specific records in the data. The goal is to learn something about your data, not to generate a plot.
- Ugly Plots, Not Pretty. Your goal is to learn about your data not to create pretty

visualizations. Do not worry if the graphs are ugly. You a not going to show them to anyone.

 Write Down Ideas. You will get a lot of ideas when you are looking at visualizations of your data. Ideas like data splits to look at, transformations to apply and techniques to test. Write them all down. They will be invaluable later when you are struggling to think of more things to try to get better results.

# 8.6 Summary

In this lesson you discovered the importance of data visualization in order to better understand your data. You discovered a number of methods that you can use to both visualize and improve your understanding of attributes standalone using univariate plots and their interactions using multivariate plots.

- Univariate Plots: Histograms, Density Plots, Box And Whisker Plots, Bar Plots and Missing Plot
- Multivariate Plots: Correlation Plot, Scatterplot Matrix, Scatterplot Matrix By Class, Density By Class and Box And Whisker Plots By Class.

## 8.6.1 Next Step

You have now seen two ways that you can use to learn more about your data: data summarization and data visualization. In the next lesson you will start to use this understanding and pre-process your data in order to best expose the structure of the problem to the learning algorithms.
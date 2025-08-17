# Chapter 5

# Simple Data Visualization

Sometimes data does not make sense until you can look at in a visual form, such as with charts and plots. Being able to quickly visualize your data samples for yourself and others is an important skill both in applied statistics and in applied machine learning. In this tutorial, you will discover the five types of plots that you will need to know when visualizing data in Python and how to use them to better understand your own data. After completing this tutorial, you will know:

- How to chart time series data with line plots and categorical quantities with bar charts.
- How to summarize data distributions with histograms and box plots.
- How to summarize the relationship between variables with scatter plots.

Let's get started.

## 5.1 Tutorial Overview

This tutorial is divided into 7 parts; they are:

- 1. Data Visualization
- 2. Introduction to Matplotlib
- 3. Line Plot
- 4. Bar Chart
- 5. Histogram Plot
- 6. Box and Whisker Plot
- 7. Scatter Plot

## 5.2 Data Visualization

Data visualization is an important skill in applied statistics and machine learning. Statistics does indeed focus on quantitative descriptions and estimations of data. Data visualization provides an important suite of tools for gaining a qualitative understanding. This can be helpful when exploring and getting to know a dataset and can help with identifying patterns, corrupt data, outliers, and much more. With a little domain knowledge, data visualizations can be used to express and demonstrate key relationships in plots and charts that are more visceral to yourself and stakeholders than measures of association or significance.

Data visualization and exploratory data analysis are whole fields themselves and I will recommend a deeper dive into some the books mentioned at the end. In this tutorial, let's look at basic charts and plots you can use to better understand your data. There are five key plots that you need to know well for basic data visualization. They are the Line Plot, Bar Chart, Histogram Plot, Box and Whisker Plot, and the Scatter Plot. With a knowledge of these plots, you can quickly get a qualitative understanding of most data that you come across. For the rest of this tutorial, we will take a closer look at each plot type.

## 5.3 Introduction to Matplotlib

There are many excellent plotting libraries in Python and I recommend exploring them in order to create presentable graphics. For quick and dirty plots intended for your own use, I recommend using the Matplotlib library. It is the foundation for many other plotting libraries and plotting support in higher-level libraries such as Pandas. The Matplotlib provides a context, one in which one or more plots can be drawn before the image is shown or saved to file. The context can be accessed via functions on pyplot. The context can be imported as follows:

```
# import matplotlib context
from matplotlib import pyplot
...
```

Listing 5.1: Example of importing the Matplotlib context.

There is some convention to import this context and name it plt; for example:

```
# import matplotlib context
import matplotlib.pyplot as plt
...
```

Listing 5.2: Example of alternate way of importing the Matplotlib context.

We will not use this convention, instead we will stick to the standard Python import convention. Charts and plots are made by making and calling on context; for example:

```
...
# create a plot
pyplot.plot(...)
```

Listing 5.3: Example of creating a plot.

Elements such as axis, labels, legends, and so on can be accessed and configured on this context as separate function calls. The drawings on the context can be shown in a new window by calling the show() function:

... # display the plot pyplot.show()

Listing 5.4: Example of displaying a plot.

Alternately, the drawings on the context can be saved to file, such as a PNG formatted image file. The savefig() function can be used to save images.

```
...
# save plot to file
pyplot.savefig('my_image.png')
```

Listing 5.5: Example of saving a plot to file.

This is the most basic crash course for using the Matplotlib library. For more detail, see the User Guide and other resources at the end of the tutorial.

## 5.4 Line Plot

A line plot is generally used to present observations collected at regular intervals. The x-axis represents the regular interval, such as time. The y-axis shows the observations, ordered by the x-axis and connected by a line. A line plot can be created by calling the plot() function and passing the x-axis data for the regular interval, and y-axis for the observations.

... # create line plot pyplot.plot(x, y)

Listing 5.6: Example of creating a line plot.

Line plots are useful for presenting time series data as well as any sequence data where there is an ordering between observations. The example below creates a sequence of 100 floating point values as the x-axis and a sine wave as a function of the x-axis as the observations on the y-axis. The results are plotted as a line plot.

```
# example of a line plot
from numpy import sin
from matplotlib import pyplot
# consistent interval for x-axis
x = [x*0.1 for x in range(100)]
# function of x for y-axis
y = sin(x)
# create line plot
pyplot.plot(x, y)
# show line plot
pyplot.show()
```

Listing 5.7: Example creating a line plot from data.

Running the example creates a line plot showing the familiar sine wave pattern on the y-axis across the x-axis with a consistent interval between observations.

![](_page_3_Figure_1.jpeg)

Figure 5.1: Example of a line plot of data.

## 5.5 Bar Chart

A bar chart is generally used to present relative quantities for multiple categories. The x-axis represents the categories and are spaced evenly. The y-axis represents the quantity for each category and is drawn as a bar from the baseline to the appropriate level on the y-axis. A bar chart can be created by calling the bar() function and passing the category names for the x-axis and the quantities for the y-axis.

... # create bar chart pyplot.bar(x, y)

Listing 5.8: Example of creating a bar chart.

Bar charts can be useful for comparing multiple point quantities or estimations. The example below creates a dataset with three categories, each defined with a string label. A single random integer value is drawn for the quantity in each category.

```
# example of a bar chart
from random import seed
from random import randint
from matplotlib import pyplot
```

```
# seed the random number generator
seed(1)
# names for categories
x = ['red', 'green', 'blue']
# quantities for each category
y = [randint(0, 100), randint(0, 100), randint(0, 100)]
# create bar chart
pyplot.bar(x, y)
# show line plot
pyplot.show()
```

![](_page_4_Figure_2.jpeg)

Running the example creates the bar chart showing the category labels on the x-axis and the quantities on the y-axis.

![](_page_4_Figure_4.jpeg)

Figure 5.2: Example of a bar chart of data.

## 5.6 Histogram Plot

A histogram plot is generally used to summarize the distribution of a data sample. The x-axis represents discrete bins or intervals for the observations. For example observations with values between 1 and 10 may be split into five bins, the values [1,2] would be allocated to the first bin, [3,4] would be allocated to the second bin, and so on. The y-axis represents the frequency or count of the number of observations in the dataset that belong to each bin. Essentially, a data sample is transformed into a bar chart where each category on the x-axis represents an interval of observation values.

Histograms are density estimates. A density estimate gives a good impression of the distribution of the data.[...] The idea is to locally represent the data density by counting the number of observations in a sequence of consecutive intervals (bins) ...

— Page 11, Applied Multivariate Statistical Analysis, 2015.

A histogram plot can be created by calling the hist() function and passing in a list or array that represents the data sample.

```
...
# create histogram plot
pyplot.hist(x)
```

Listing 5.10: Example of creating a histogram plot.

Histograms are valuable for summarizing the distribution of data samples. The example below creates a dataset of 1,000 random numbers drawn from a standard Gaussian distribution, then plots the dataset as a histogram.

```
# example of a histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# random numbers drawn from a Gaussian distribution
x = randn(1000)
# create histogram plot
pyplot.hist(x)
# show line plot
pyplot.show()
```

Listing 5.11: Example creating a histogram plot from data.

Running the example, we can see that the shape of the bars shows the bell-shaped curve of the Gaussian distribution. We can see that the function automatically chose the number of bins, in this case splitting the values into groups by integer value.

![](_page_6_Figure_1.jpeg)

Figure 5.3: Example of a histogram plot of data.

Often, careful choice of the number of bins can help to better expose the shape of the data distribution. The number of bins can be specified by setting the bins argument; for example:

```
...
# create histogram plot with specified bins
pyplot.hist(x, bins=100)
```

Listing 5.12: Example of creating a histogram plot with a specific number of bins.

## 5.7 Box and Whisker Plot

A box and whisker plot, or boxplot for short, is generally used to summarize the distribution of a data sample. The x-axis is used to represent the data sample, where multiple boxplots can be drawn side by side on the x-axis if desired.

The y-axis represents the observation values. A box is drawn to summarize the middle 50% of the dataset starting at the observation at the 25th percentile and ending at the 75th percentile. The median, or 50th percentile, is drawn with a line. A value called the interquartile range, or IQR, is calculated as 1.5 \* the difference between the 75th and 25th percentiles. Lines called whiskers are drawn extending from both ends of the box with the length of the IQR to demonstrate the expected range of sensible values in the distribution. Observations outside the whiskers might be outliers and are drawn with small circles.

The boxplot is a graphical technique that displays the distribution of variables. It helps us see the location, skewness, spread, tile length and outlying points. [...] The boxplot is a graphical representation of the Five Number Summary.

— Page 5, Applied Multivariate Statistical Analysis, 2015.

Boxplots can be drawn by calling the boxplot() function passing in the data sample as an array or list.

... # create box and whisker plot pyplot.boxplot(x)

Listing 5.13: Example of creating a box and whisker plot.

Boxplots are useful to summarize the distribution of a data sample as an alternative to the histogram. They can help to quickly get an idea of the range of common and sensible values in the box and in the whisker respectively. Because we are not looking at the shape of the distribution explicitly, this method is often used when the data has an unknown or unusual distribution, such as non-Gaussian.

The example below creates three boxplots in one chart, each summarizing a data sample drawn from a slightly different Gaussian distribution. Each data sample is created as an array and all three data sample arrays are added to a list that is padded to the plotting function.

```
# example of a box and whisker plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# random numbers drawn from a Gaussian distribution
x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]
# create box and whisker plot
pyplot.boxplot(x)
# show line plot
pyplot.show()
```

Listing 5.14: Example creating a box and whisker plot from data.

Running the example creates a chart showing the three box and whisker plots. We can see that the same scale is used on the y-axis for each, making the first plot look squashed and the last plot look spread out. In this case, we can see the black box for the middle 50% of the data, the orange line for the median, the lines for the whiskers summarizing the range of sensible data, and finally dots for the possible outliers.

![](_page_8_Figure_1.jpeg)

Figure 5.4: Example of a box and whisker plot of data.

## 5.8 Scatter Plot

A scatter plot, or scatterplot, is generally used to summarize the relationship between two paired data samples. Paired data samples means that two measures were recorded for a given observation, such as the weight and height of a person. The x-axis represents observation values for the first sample, and the y-axis represents the observation values for the second sample. Each point on the plot represents a single observation.

Scatterplots are bivariate or trivariate plots of variables against each other. They help us understand relationships among the variables of a dataset. A downwardsloping scatter indicates that as we increase the variable on the horizontal axis, the variable on the vertical axis decreases.

— Page 19, Applied Multivariate Statistical Analysis, 2015.

Scatter plots can be created by calling the scatter() function and passing the two data sample arrays.

... # create scatter plot pyplot.scatter(x, y)

Listing 5.15: Example of creating a scatter plot.

Scatter plots are useful for showing the association or correlation between two variables. A correlation can be quantified, such as a line of best fit, that too can be drawn as a line plot on the same chart, making the relationship clearer. A dataset may have more than two measures (variables or columns) for a given observation. A scatter plot matrix is a cart containing scatter plots for each pair of variables in a dataset with more than two variables. The example below creates two data samples that are related. The first is a sample of random numbers drawn from a standard Gaussian. The second is dependent upon the first by adding a second random Gaussian value to the value of the first measure.

```
# example of a scatter plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# first variable
x = 20 * randn(1000) + 100
# second variable
y = x + (10 * randn(1000) + 50)
# create scatter plot
pyplot.scatter(x, y)
# show line plot
pyplot.show()
```

Listing 5.16: Example creating a scatter plot from data.

Running the example creates the scatter plot, showing the positive relationship between the two variables. We will learn more about describing the relationships between variables in Chapter 12.

![](_page_10_Figure_1.jpeg)

Figure 5.5: Example of a scatter plot of data.

## 5.9 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Select one example and update it to use your own contrived dataset.
- Load a standard machine learning dataset and plot the variables.
- Write convenience functions to easily create plots for your data, including labels and legends.

If you explore any of these extensions, I'd love to know.

## 5.10 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 5.10.1 Books

- The Visual Display of Quantitative Information, 2001. <http://amzn.to/2pbC14o>
- Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython, 2017. <http://amzn.to/2Gt8Pgt>
- Applied Multivariate Statistical Analysis, 2015. <http://amzn.to/2Dtykv7>

#### 5.10.2 API

- Matplotlib library. <https://matplotlib.org/>
- Matplotlib User Guide. <https://matplotlib.org/users/index.html>
- matplotlib.pyplot API. [https://matplotlib.org/api/pyplot\\_api.html](https://matplotlib.org/api/pyplot_api.html)
- matplotlib.pyplot.show API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.show.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html)
- matplotlib.pyplot.savefig API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.savefig.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html)
- matplotlib.pyplot.plot API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.plot.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html)
- matplotlib.pyplot.bar API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.bar.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html)
- matplotlib.pyplot.hist API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.hist.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html)
- matplotlib.pyplot.boxplot API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.boxplot.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html)
- matplotlib.pyplot.scatter API. [https://matplotlib.org/api/\\_as\\_gen/matplotlib.pyplot.scatter.html](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html)

#### 5.10.3 Articles

- Data visualization on Wikipedia. [https://en.wikipedia.org/wiki/Data\\_visualization](https://en.wikipedia.org/wiki/Data_visualization)
- Bar chart on Wikipedia. [https://en.wikipedia.org/wiki/Bar\\_chart](https://en.wikipedia.org/wiki/Bar_chart)

- Histogram on Wikipedia. <https://en.wikipedia.org/wiki/Histogram>
- Box plot on Wikipedia. [https://en.wikipedia.org/wiki/Box\\_plot](https://en.wikipedia.org/wiki/Box_plot)
- Interquartile range on Wikipedia. [https://en.wikipedia.org/wiki/Interquartile\\_range](https://en.wikipedia.org/wiki/Interquartile_range)
- Scatter plot on Wikipedia. [https://en.wikipedia.org/wiki/Scatter\\_plot](https://en.wikipedia.org/wiki/Scatter_plot)

## 5.11 Summary

In this tutorial, you discovered a gentle introduction to visualization data in Python. Specifically, you learned:

- How to chart time series data with line plots and categorical quantities with bar charts.
- How to summarize data distributions with histograms and boxplots.
- How to summarize the relationship between variables with scatter plots.

#### 5.11.1 Next

In the next section, you will discover how to generate samples of random numbers using Python and NumPy.
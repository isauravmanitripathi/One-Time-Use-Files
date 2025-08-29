# **Chapter 7. Data Visualization**

Use a picture. It's worth a thousand words. Arthur Brisbane (1911)

This chapter is about the basic visualization capabilities of the [matplotlib](http://www.matplotlib.org) and [plotly](http://plot.ly) packages.

Although there are more visualization packages available, matplotlib has established itself as the benchmark and, in many situations, a robust and reliable visualization tool. It is both easy to use for standard plots and flexible when it comes to more complex plots and customizations. In addition, it is tightly integrated with NumPy and pandas and the data structures they provide.

matplotlib only allows for the generation of plots in the form of bitmaps (for example, in PNG or JPG format). On the other hand, modern web technologies — based, for example, on the [Data-Driven](https://d3js.org/) Documents (D3.js) standard — allow for nice interactive and also embeddable plots (interactive, for example, in that one can zoom in to inspect certain areas in greater detail). A package that makes it convenient to create such D3.js plots with Python is plotly. A smaller additional library, called Cufflinks, tightly integrates plotly with pandas DataFrame objects and allows for the creation of popular financial plots (such as candlestick charts).

This chapter mainly covers the following topics:

### *"Static 2D Plotting"*

This section introduces matplotlib and presents a selection of typical 2D plots, from the most simple to some more advanced ones with two scales or different subplots.

### *"Static 3D Plotting"*

Based on matplotlib, a selection of 3D plots useful for certain financial applications are presented in this section.

### *"Interactive 2D Plotting"*

This section introduces plotly and Cufflinks to create interactive 2D plots. Making use of the QuantFigure feature of Cufflinks, this section is also about typical financial plots used, for example, in technical stock analysis.

This chapter cannot be comprehensive with regard to data visualization with Python, matplotlib, or plotly, but it provides a number of examples for the basic and important capabilities of these packages for finance. Other examples are also found in later chapters. For instance, Chapter 8 shows in more depth how to visualize financial time series data with the pandas library.

# **Static 2D Plotting**

Before creating the sample data and starting to plot, some imports and customizations: In [1]: **import matplotlib as mpl** In [2]: mpl.\_\_version\_\_ Out[2]: '3.0.0' In [3]: **import matplotlib.pyplot as plt** In [4]: plt.style.use('seaborn') In [5]: mpl.rcParams['font.family'] = 'serif' In [6]: %matplotlib inline

Imports matplotlib with the usual abbreviation mpl.

The version of matplotlib used.

Imports the main plotting (sub)package with the usual abbreviation plt.

Sets the [plotting](http://bit.ly/2KaPFhs) style to seaborn.

Sets the font to be serif in all plots.

### **One-Dimensional Data Sets**

The most fundamental, but nevertheless quite powerful, plotting function is plt.plot(). In principle, it needs two sets of numbers:

### *x values*

A list or an array containing the *x* coordinates (values of the abscissa)

### *y values*

A list or an array containing the *y* coordinates (values of the ordinate)

The number of *x* and *y* values provided must match, of course. Consider the following code, whose output is presented in Figure 7-1:

```
In [7]: import numpy as np
In [8]: np.random.seed(1000)
In [9]: y = np.random.standard_normal(20)
In [10]: x = np.arange(len(y))
         plt.plot(x, y);
```

Fixes the seed for the random number generator for reproducibility.

Draws the random numbers (*y* values).

Fixes the integers (*x* values).

Calls the plt.plot() function with the x and y objects.

<span id="page-4-0"></span>![](_page_4_Figure_0.jpeg)

plt.plot() notices when an ndarray object is passed. In this case, there is no need to provide the "extra" information of the *x* values. If one only provides the *y* values, plt.plot() takes the index values as the respective *x* values. Therefore, the following single line of code generates exactly the same output (see [Figure](#page-4-0) 7-2):

```
In [11]: plt.plot(y);
```

![](_page_5_Figure_0.jpeg)

### **NUMPY ARRAYS AND MATPLOTLIB**

You can simply pass NumPy ndarray objects to matplotlib functions. matplotlib is able to interpret the data structures for simplified plotting. However, be careful to not pass a too large and/or complex array.

<span id="page-6-0"></span>Since the majority of the ndarray methods return an ndarray object, one can also pass the object with a method (or even multiple methods, in some cases) attached. By calling the cumsum() method on the ndarray object with the sample data, one gets the cumulative sum of this data and, as to be expected, a different output (see [Figure](#page-6-0) 7-3): In [12]: plt.plot(y.cumsum());

![](_page_7_Figure_0.jpeg)

In general, the default plotting style does not satisfy typical requirements for reports, publications, *etc.* For example, one might want to customize the font used (e.g., for compatibility with LaTeX fonts), to have labels at the axes, or to plot a grid for better readability. This is where plotting styles come into play. In addition, matplotlib offers a large number of functions to customize the plotting style. Some are easily accessible; for others one has to dig a bit deeper. Easily accessible, for example, are those functions that manipulate the axes and those that relate to grids and labels (see Figure 7-4): In [13]: plt.plot(y.cumsum()) plt.grid(False) plt.axis('equal');

Turns off the grid.

Leads to equal scaling for the two axes.

![](_page_8_Figure_0.jpeg)

Other options for plt.axis() are given in [Table](#page-8-0) 7-1, the majority of which have to be passed as a str object.

<span id="page-8-0"></span>

| Parameter                     | Description                                                 |
|-------------------------------|-------------------------------------------------------------|
| Empty                         | Returns<br>current<br>axis<br>limits                        |
| off                           | Turns<br>axis<br>lines<br>and<br>labels<br>off              |
| equal                         | Leads<br>to<br>equal<br>scaling                             |
| scaled                        | Produces<br>equal<br>scaling<br>via<br>dimension<br>changes |
| tight                         | Makes<br>all<br>data<br>visible<br>(tightens<br>limits)     |
| image                         | Makes<br>all<br>data<br>visible<br>(with<br>data<br>limits) |
| [xmin, xmax, ymin, ymax] Sets | limits<br>to<br>given<br>(list<br>of)<br>values             |

| Table<br>7-1. | Options | for | plt.axis() |
|---------------|---------|-----|------------|
|---------------|---------|-----|------------|

<span id="page-9-0"></span>In addition, one can directly set the minimum and maximum values of each axis by using plt.xlim() and plt.ylim(). The following code provides an example whose output is shown in [Figure](#page-9-0) 7-5: In [14]: plt.plot(y.cumsum()) plt.xlim(-1, 20) plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1);

![](_page_10_Figure_0.jpeg)

For the sake of better readability, a plot usually contains a number of labels e.g., a title and labels describing the nature of the *x* and *y* values. These are added by the functions plt.title(), plt.xlabel(), and plt.ylabel(), respectively. By default, plot() plots continuous lines, even if discrete data points are provided. The plotting of discrete points is accomplished by choosing a different style option. Figure 7-6 overlays (red) points and a (blue) line with line width of 1.5 points: In [15]: plt.figure(figsize=(10, 6)) plt.plot(y.cumsum(), 'b', lw=1.5) plt.plot(y.cumsum(), 'ro') plt.xlabel('index') plt.ylabel('value') plt.title('A Simple Plot');

Increases the size of the figure.

Plots the data as a line in blue with line width of 1.5 points.

Plots the data as red (thick) dots.

Places a label on the x-axis.

Places a label on the y-axis.

Places a title.

![](_page_11_Figure_6.jpeg)

*Figure 7-6. Plot with typical labels*

By default, plt.plot() supports the color abbreviations in Table 7-2.

| Table<br>7-2.<br>Standard<br>color<br>abbreviations |       |  |
|-----------------------------------------------------|-------|--|
| Character                                           | Color |  |
| b                                                   | Blue  |  |
| g                                                   | Green |  |

| r | Red     |
|---|---------|
| c | Cyan    |
| m | Magenta |
| y | Yellow  |
| k | Black   |
| w | White   |

In terms of line and/or point styles, plt.plot() supports the characters listed in [Table](#page-12-0) 7-3.

<span id="page-12-0"></span>

| Table | 7-3.<br>Standard<br>style |
|-------|---------------------------|
|       | characters                |

| Character | Symbol                    |
|-----------|---------------------------|
| -         | Solid<br>line<br>style    |
| --        | Dashed<br>line<br>style   |
| -.        | Dash-dot<br>line<br>style |
| :         | Dotted<br>line<br>style   |
|           | Point<br>marker           |
| ,         | Pixel<br>marker           |
| o         | Circle<br>marker          |
| v         | Triangle_down<br>marker   |
| �0�       | Triangle_up<br>marker     |
| <         | Triangle_left<br>marker   |
| >         | Triangle_right<br>marker  |
| 1         | Tri_down<br>marker        |
| 2         | Tri_up<br>marker          |

| 3   | Tri_left<br>marker        |
|-----|---------------------------|
| 4   | Tri_right<br>marker       |
| s   | Square<br>marker          |
| p   | Pentagon<br>marker        |
| �0� | Star<br>marker            |
| h   | Hexagon1<br>marker        |
|     | Hexagon2<br>marker        |
| H   |                           |
| �0� | Plus<br>marker            |
| x   | X<br>marker               |
| D   | Diamond<br>marker         |
| d   | Thin<br>diamond<br>marker |
|     | Vline<br>marker           |

Any color abbreviation can be combined with any style character. In this way, one can make sure that different data sets are easily distinguished. The plotting style is also reflected in the legend.

# **Two-Dimensional Data Sets**

Plotting one-dimensional data can be considered a special case. In general, data sets will consist of multiple separate subsets of data. The handling of such data sets follows the same rules with matplotlib as with one-dimensional data. However, a number of additional issues might arise in such a context. For example, two data sets might have such a different scaling that they cannot be plotted using the same y-and/or x-axis scaling. Another issue might be that one might want to visualize two different data sets in different ways, e.g., one by a line plot and the other by a bar plot.

The following code generates a two-dimensional sample data set as a NumPy ndarray object of shape with standard normally distributed pseudorandom numbers. On this array, the method cumsum() is called to calculate the cumulative sum of the sample data along axis 0 (i.e., the first dimension): In [16]: y = np.random.standard\_normal((20, 2)).cumsum(axis=0)

In general, one can also pass such two-dimensional arrays to plt.plot(). It will then automatically interpret the contained data as separate data sets (along axis 1, i.e., the second dimension). A respective plot is shown in Figure 7-7: In [17]: plt.figure(figsize=(10, 6)) plt.plot(y, lw=1.5) plt.plot(y, 'ro') plt.xlabel('index') plt.ylabel('value') plt.title('A Simple Plot');

![](_page_15_Figure_0.jpeg)

*Figure 7-7. Plot with two data sets*

In such a case, further annotations might be helpful to better read the plot. You can add individual labels to each data set and have them listed in the legend. The function plt.legend() accepts different locality parameters. 0 stands for *best location*, in the sense that as little data as possible is hidden by the legend.

Figure 7-8 shows the plot of the two data sets, this time with a legend. In the generating code, the ndarray object is not passed as a whole but the two data subsets (y[:, 0] and y[:, 1]) are accessed separately, which allows you to attach individual labels to them: In [18]: plt.figure(figsize=(10, 6)) plt.plot(y[:, 0], lw=1.5, label='1st') plt.plot(y[:, 1], lw=1.5, label='2nd') plt.plot(y, 'ro') plt.legend(loc=0) plt.xlabel('index') plt.ylabel('value') plt.title('A Simple Plot');

Defines labels for the data subsets.

Places a legend in the "best" location.

![](_page_16_Figure_0.jpeg)

Further location options for plt.legend() include those presented in [Table](#page-16-0) 7-4.

<span id="page-16-0"></span>

| Table<br>7-4.<br>Options<br>for<br>plt.legend() |                  |  |
|-------------------------------------------------|------------------|--|
| Loc                                             | Description      |  |
| Default                                         | Upper<br>right   |  |
| 0                                               | Best<br>possible |  |
| 1                                               | Upper<br>right   |  |
| 2                                               | Upper<br>left    |  |
| 3                                               | Lower<br>left    |  |
| 4                                               | Lower<br>right   |  |
| 5                                               | Right            |  |

| 6  | Center<br>left  |
|----|-----------------|
| 7  | Center<br>right |
| 8  | Lower<br>center |
| 9  | Upper<br>center |
| 10 | Center          |

Multiple data sets with a similar scaling, like simulated paths for the same financial risk factor, can be plotted using a single y-axis. However, often data sets show rather different scalings and the plotting of such data with a single yscale generally leads to a significant loss of visual information. To illustrate the effect, the following example scales the first of the two data subsets by a factor of 100 and plots the data again (see Figure 7-9): In [19]: y[:, 0] = y[:, 0] \* 100 In [20]: plt.figure(figsize=(10, 6)) plt.plot(y[:, 0], lw=1.5, label='1st') plt.plot(y[:, 1], lw=1.5, label='2nd') plt.plot(y, 'ro') plt.legend(loc=0) plt.xlabel('index') plt.ylabel('value') plt.title('A Simple Plot');

Rescales the first data subset.

<span id="page-18-0"></span>![](_page_18_Figure_0.jpeg)

*Figure 7-9. Plot with two differently scaled data sets*

Inspection of [Figure](#page-18-0) 7-9 reveals that the first data set is still "visually readable," while the second data set now looks like a straight line with the new scaling of the y-axis. In a sense, information about the second data set now gets "visually lost." There are two basic approaches to resolve this problem through means of plotting, as opposed to adjusting the data (e.g., through rescaling):

- Use of two y-axes (left/right)
- Use of two subplots (upper/lower, left/right)

```
The following example introduces a second y-axis to the plot. Figure 7-10 now
has two different y-axes. The left y-axis is for the first data set while the right y-
axis is for the second. Consequently, there are also two legends: In [21]: fig,
ax1 = plt.subplots() plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro') plt.legend(loc=8) plt.xlabel('index')
plt.ylabel('value 1st') plt.title('A Simple Plot') ax2 =
ax1.twinx() plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro') plt.legend(loc=0) plt.ylabel('value 2nd');
```

Defines the figure and axis objects.

Creates a second axis object that shares the x-axis.

![](_page_20_Figure_0.jpeg)

*Figure 7-10. Plot with two data sets and two y-axes*

The key lines of code are those that help manage the axes: fig, ax1 = plt.subplots() ax2 = ax1.twinx()

By using the plt.subplots() function, one gets direct access to the underlying plotting objects (the figure, subplots, etc.). It allows one, for example, to generate a second subplot that shares the x-axis with the first subplot. In Figure 7-10, then, the two subplots actually *overlay* each other.

```
Next, consider the case of two separate subplots. This option gives even more
freedom to handle the two data sets, as Figure 7-11 illustrates: In [22]:
plt.figure(figsize=(10, 6)) plt.subplot(211) plt.plot(y[:, 0],
lw=1.5, label='1st') plt.plot(y[:, 0], 'ro') plt.legend(loc=0)
plt.ylabel('value') plt.title('A Simple Plot') plt.subplot(212)
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd') plt.plot(y[:, 1], 'ro')
plt.legend(loc=0) plt.xlabel('index') plt.ylabel('value');
```

Defines the upper subplot 1.

![](_page_21_Figure_1.jpeg)

Defines the lower subplot 2.

*Figure 7-11. Plot with two subplots*

The placing of subplots in a matplotlib figure object is accomplished by the use of a special coordinate system. plt.subplot() takes as arguments three integers for numrows, numcols, and fignum (either separated by commas or not). numrows specifies the number of *rows*, numcols the number of *columns*, and fignum the number of the *subplot*, starting with 1 and ending with numrows \* numcols. For example, a figure with nine equally sized subplots would have numrows=3, numcols=3, and fignum=1,2,...,9. The lower-right subplot would have the following "coordinates": plt.subplot(3, 3, 9).

Sometimes, it might be necessary or desired to choose two different plot types to visualize such data. With the subplot approach one has the freedom to combine arbitrary kinds of plots that matplotlib offers. 1

Figure 7-12 combines a line/point plot with a bar chart: In [23]:

```
plt.figure(figsize=(10, 6)) plt.subplot(121) plt.plot(y[:, 0],
lw=1.5, label='1st') plt.plot(y[:, 0], 'ro') plt.legend(loc=0)
plt.xlabel('index') plt.ylabel('value') plt.title('1st Data Set')
plt.subplot(122) plt.bar(np.arange(len(y)), y[:, 1], width=0.5,
color='g', label='2nd') plt.legend(loc=0) plt.xlabel('index')
plt.title('2nd Data Set');
```

Creates a bar subplot.

![](_page_22_Figure_3.jpeg)

*Figure 7-12. Plot combining line/point subplot with bar subplot*

# **Other Plot Styles**

When it comes to two-dimensional plotting, line and point plots are probably the most important ones in finance; this is because many data sets embody time series data, which generally is visualized by such plots. Chapter 8 addresses financial time series data in detail. However, this section sticks with a twodimensional data set of random numbers and illustrates some alternative, and for financial applications useful, visualization approaches.

The first is the *scatter plot*, where the values of one data set serve as the *x* values for the other data set. Figure 7-13 shows such a plot. This plot type might be used, for example, for plotting the returns of one financial time series against those of another one. This example uses a new two-dimensional data set with some more data: In [24]: y = np.random.standard\_normal((1000, 2)) In [25]: plt.figure(figsize=(10, 6)) plt.plot(y[:, 0], y[:, 1], 'ro') plt.xlabel('1st') plt.ylabel('2nd') plt.title('Scatter Plot');

Creates a larger data set with random numbers.

Scatter plot produced via the plt.plot() function.

<span id="page-24-0"></span>![](_page_24_Figure_0.jpeg)

*Figure 7-13. Scatter plot via plt.plot() function*

matplotlib also provides a specific function to generate scatter plots. It basically works in the same way, but provides some additional features. Figure 7-14 shows the corresponding scatter plot to [Figure](#page-24-0) 7-13, this time generated using the plt.scatter() function: In [26]: plt.figure(figsize= (10, 6)) plt.scatter(y[:, 0], y[:, 1], marker='o') plt.xlabel('1st') plt.ylabel('2nd') plt.title('Scatter Plot');

Scatter plot produced via the plt.scatter() function.

![](_page_25_Figure_0.jpeg)

*Figure 7-14. Scatter plot via plt.scatter() function*

Among other things, the plt.scatter() plotting function allows the addition of a third dimension, which can be visualized through different colors and be described by the use of a color bar. Figure 7-15 shows a scatter plot where there is a third dimension illustrated by different colors of the single dots and with a color bar as a legend for the colors. To this end, the following code generates a third data set with random data, this time consisting of integers between 0 and 10: In [27]: c = np.random.randint(0, 10, len(y)) In [28]: plt.figure(figsize=(10, 6)) plt.scatter(y[:, 0], y[:, 1], c=c, cmap='coolwarm', marker='o') plt.colorbar() plt.xlabel('1st') plt.ylabel('2nd') plt.title('Scatter Plot');

Includes the third data set.

Chooses the color map.

Defines the marker to be a thick dot.

![](_page_27_Figure_0.jpeg)

*Figure 7-15. Scatter plot with third dimension*

Another type of plot, the *histogram*, is also often used in the context of financial returns. Figure 7-16 puts the frequency values of the two data sets next to each other in the same plot: In [29]: plt.figure(figsize=(10, 6)) plt.hist(y, label=['1st', '2nd'], bins=25) plt.legend(loc=0) plt.xlabel('value') plt.ylabel('frequency') plt.title('Histogram');

Histogram plot produced via the plt.hist() function.

![](_page_28_Figure_0.jpeg)

*Figure 7-16. Histogram for two data sets*

Since the histogram is such an important plot type for financial applications, let's take a closer look at the use of plt.hist(). The following example illustrates the parameters that are supported: plt.hist(x, bins=10, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, \*\*kwargs)

Table 7-5 provides a description of the main parameters of the plt.hist() function.

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| x         | list object(s),<br>ndarray object            |
| bins      | Number<br>of<br>bins                         |
| range     | Lower<br>and<br>upper<br>range<br>of<br>bins |
|           |                                              |

*Table 7-5. Parameters for plt.hist()*

| normed              | Norming<br>such<br>that<br>integral<br>value<br>is<br>1                 |
|---------------------|-------------------------------------------------------------------------|
| weights             | Weights<br>for<br>every<br>value<br>in<br>x                             |
| cumulative          | Every<br>bin<br>contains<br>the<br>counts<br>of<br>the<br>lower<br>bins |
| histtype            | Options<br>(strings):<br>bar,<br>barstacked,<br>step,<br>stepfilled     |
| align               | Options<br>(strings):<br>left,<br>mid,<br>right                         |
| orientation Options | (strings):<br>horizontal,<br>vertical                                   |
| rwidth              | Relative<br>width<br>of<br>the<br>bars                                  |
| log                 | Log<br>scale                                                            |
| color               | Color<br>per<br>data<br>set<br>(array-like)                             |
| label               | String<br>or<br>sequence<br>of<br>strings<br>for<br>labels              |
| stacked             | Stacks<br>multiple<br>data<br>sets                                      |

Figure 7-17 shows a similar plot; this time, the data of the two data sets is stacked in the histogram: In [30]: plt.figure(figsize=(10, 6)) plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20, alpha=0.5) plt.legend(loc=0) plt.xlabel('value') plt.ylabel('frequency') plt.title('Histogram');

![](_page_30_Figure_0.jpeg)

*Figure 7-17. Stacked histogram for two data sets*

Another useful plot type is the *boxplot*. Similar to the histogram, the boxplot allows both a concise overview of the characteristics of a data set and easy comparison of multiple data sets. Figure 7-18 shows such a plot for our data sets: In [31]: fig, ax = plt.subplots(figsize=(10, 6)) plt.boxplot(y) plt.setp(ax, xticklabels=['1st', '2nd']) plt.xlabel('data set') plt.ylabel('value') plt.title('Boxplot');

Boxplot produced via the plt.boxplot() function.

Sets individual *x* labels.

![](_page_31_Figure_0.jpeg)

*Figure 7-18. Boxplot for two data sets*

This last example uses the function plt.setp(), which sets properties for a (set of) plotting instance(s). For example, consider a line plot generated by: line = plt.plot(data, 'r')

The following code changes the style of the line to "dashed": plt.setp(line, linestyle='--')

This way, one can easily change parameters after the plotting instance ("artist object") has been generated.

As a final illustration in this section, consider a mathematically inspired plot that can also be found as an example in the [matplotlib](http://www.matplotlib.org/gallery.html) gallery. It plots a function and highlights graphically the area below the function from a lower and to an upper limit — in other words, the integral value of the function between the lower and upper limits. The integral (value) to be illustrated is with , , and . Figure 7-19 shows the resulting plot and demonstrates that matplotlib seamlessly handles LaTeX typesetting for the

inclusion of mathematical formulae into plots. First, the function definition, with integral limits as variables and data sets for the *x* and *y* values: In [32]: **def** func(x): **return** 0.5 \* np.exp(x) + 1 a, b = 0.5, 1.5 x = np.linspace(0, 2) y = func(x) Ix = np.linspace(a, b) Iy = func(Ix) verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]

The function definition.

The integral limits.

The *x* values to plot the function.

The *y* values to plot the function.

The *x* values within the integral limits.

The *y* values within the integral limits.

The list object with multiple tuple objects representing coordinates for the polygon to be plotted.

```
Second, the plotting itself, which is a bit involved due to the many single objects
to be placed explicitly: In [33]: from matplotlib.patches import Polygon
fig, ax = plt.subplots(figsize=(10, 6)) plt.plot(x, y, 'b',
linewidth=2) plt.ylim(bottom=0) poly = Polygon(verts,
facecolor='0.7', edgecolor='0.5') ax.add_patch(poly)
plt.text(0.5 * (a + b), 1, r'$\int_a^b f(x)\mathrm{d}x$',
horizontalalignment='center', fontsize=20) plt.figtext(0.9,
0.075, '$x$') plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a, b)) ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)]) ax.set_yticklabels(('$f(a)$',
'$f(b)$'));
```

Plots the function values as a blue line.

Defines the minimum *y* value for the ordinate axis.

Plots the polygon (integral area) in gray.

Places the integral formula in the plot.

Places the axis labels.

Places the *x* labels.

Places the *y* labels.

![](_page_33_Figure_12.jpeg)

*Figure 7-19. Exponential function, integral area, and LaTeX labels*

# **Static 3D Plotting**

There are not too many fields in finance that really benefit from visualization in three dimensions. However, one application area is volatility surfaces showing implied volatilities simultaneously for a number of times-to-maturity and strikes of the traded options used. See also Appendix B for an example of value and vega surfaces being visualized for a European call option. In what follows, the code artificially generates a plot that resembles a volatility surface. To this end, consider the parameters:

- *Strike values* between 50 and 150
- *Times-to-maturity* between 0.5 and 2.5 years

This provides a two-dimensional coordinate system. The NumPy np.meshgrid() function can generate such a system out of two one-dimensional ndarray objects: In [34]: strike = np.linspace(50, 150, 24) In [35]: ttm = np.linspace(0.5, 2.5, 24) In [36]: strike, ttm = np.meshgrid(strike, ttm) In [37]: strike[:2].round(1) Out[37]: array([[ 50. , 54.3, 58.7, 63. , 67.4, 71.7, 76.1, 80.4, 84.8, 89.1, 93.5, 97.8, 102.2, 106.5, 110.9, 115.2, 119.6, 123.9, 128.3, 132.6, 137. , 141.3, 145.7, 150. ], [ 50. , 54.3, 58.7, 63. , 67.4, 71.7, 76.1, 80.4, 84.8, 89.1, 93.5, 97.8, 102.2, 106.5, 110.9, 115.2, 119.6, 123.9, 128.3, 132.6, 137. , 141.3, 145.7, 150. ]]) In [38]: iv = (strike - 100) \*\* 2 / (100 \* strike) / ttm In [39]: iv[:5, :3] Out[39]: array([[1. , 0.76695652, 0.58132045], [0.85185185, 0.65333333, 0.4951989 ], [0.74193548, 0.56903226, 0.43130227], [0.65714286, 0.504 , 0.38201058], [0.58974359, 0.45230769, 0.34283001]])

The ndarray object with the strike values.

The ndarray object with the time-to-maturity values.

The two two-dimensional ndarray objects (grids) created.

The dummy implied volatility values.

```
The plot resulting from the following code is shown in Figure 7-20: In [40]:
from mpl_toolkits.mplot3d import Axes3D fig = plt.figure(figsize=
(10, 6)) ax = fig.gca(projection='3d') surf =
ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2,
cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('strike') ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility') fig.colorbar(surf,
shrink=0.5, aspect=5);
```

Imports the relevant 3D plotting features, which is required although Axes3D is not directly used.

Sets up a canvas for 3D plotting.

Creates the 3D plot.

Sets the x-axis label.

Sets the y-axis label.

Sets the z-axis label.

Creates a color bar.

![](_page_36_Figure_0.jpeg)

*Figure 7-20. 3D surface plot for (dummy) implied volatilities*

[Table](#page-36-0) 7-6 provides a description of the different parameters the plt.plot\_surface() function can take.

| Parameter       | Description                                                     |
|-----------------|-----------------------------------------------------------------|
| X, Y, Z         | Data<br>values<br>as<br>2D<br>arrays                            |
| rstride         | Array<br>row<br>stride<br>(step<br>size)                        |
| cstride         | Array<br>column<br>stride<br>(step<br>size)                     |
| color           | Color<br>of<br>the<br>surface<br>patches                        |
| cmap            | Color<br>map<br>for<br>the<br>surface<br>patches                |
| facecolors Face | colors<br>for<br>the<br>individual<br>patches                   |
| norm            | Instance<br>of<br>Normalize to<br>map<br>values<br>to<br>colors |
| vmin            | Minimum<br>value<br>to<br>map                                   |

<span id="page-36-0"></span>*Table 7-6. Parameters for plot\_surface()*

| vmin  | Minimum<br>value<br>to<br>map                   |  |
|-------|-------------------------------------------------|--|
| vmax  | Maximum<br>value<br>to<br>map                   |  |
| shade | Whether<br>to<br>shade<br>the<br>face<br>colors |  |

As with two-dimensional plots, the line style can be replaced by single points or, as in what follows, single triangles. [Figure](#page-37-0) 7-21 plots the same data as a 3D scatter plot but now also with a different viewing angle, using the view\_init() method to set it: In [41]: fig = plt.figure(figsize=(10, 6)) ax = fig.add\_subplot(111, projection='3d') ax.view\_init(30, 60) ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^') ax.set\_xlabel('strike') ax.set\_ylabel('time-to-maturity') ax.set\_zlabel('implied volatility');

Sets the viewing angle.

Creates a 3D scatter plot.

<span id="page-37-0"></span>![](_page_37_Figure_6.jpeg)

*Figure 7-21. 3D scatter plot for (dummy) implied volatilities*

# **Interactive 2D Plotting**

matplotlib allows you to create plots that are static bitmap objects or of PDF format. Nowadays, there are many libraries available to create interactive plots based on the D3.js standard. Such plots enable zooming in and out, hover effects for data inspection, and more. They can in general also be easily embedded in web pages.

A popular platform and plotting library is [plotly](http://plot.ly). It is dedicated to visualization for data science and is in widespread use in the data science community. Major benefits of plotly are its tight integration with the Python ecosystem and the ease of use — in particular when combined with pandas DataFrame objects and the wrapper package [Cufflinks](http://github.com/santosjorge/cufflinks).

For some functionality, a free [account](https://plot.ly/accounts/login/?action=login#/) is required. Once the credentials are granted they should be stored locally for permanent use. For details, see the ["Getting](https://plot.ly/python/getting-started/) Started with Plotly for Python" guide.

This section focuses on selected aspects only, in that Cufflinks is used exclusively to create interactive plots from data stored in DataFrame objects.

# **Basic Plots**

To get started from within a Jupyter Notebook context, some imports are required and the *notebook mode* should be turned on: In [42]: **import pandas as pd** In [43]: **import cufflinks as cf** In [44]: **import plotly.offline as plyo** In [45]: plyo.init\_notebook\_mode(connected=True)

Imports Cufflinks.

Imports the offline plotting capabilities of plotly.

Turns on the notebook plotting mode.

**REMOTE OR LOCAL RENDERING** With plotly, there is also the option to get the plots rendered on the plotly servers. However, the notebook mode is generally much faster, in particular when dealing with larger data sets. That said, some functionality, like the streaming plot service of plotly, is only available via communication with the server.

The examples that follow rely again on pseudo-random numbers, this time stored in a DataFrame object with DatetimeIndex (i.e., as time series data):

```
In [46]: a = np.random.standard_normal((250, 5)).cumsum(axis=0)
In [47]: index = pd.date_range('2019-1-1',
                           freq='B',
                           periods=len(a))
In [48]: df = pd.DataFrame(100 + 5 * a,
                       columns=list('abcde'),
                       index=index)
In [49]: df.head()
Out[49]: a b c d e
       2019-01-01 109.037535 98.693865 104.474094 96.878857 100.621936
       2019-01-02 107.598242 97.005738 106.789189 97.966552 100.175313
       2019-01-03 101.639668 100.332253 103.183500 99.747869 107.902901
       2019-01-04 98.500363 101.208283 100.966242 94.023898 104.387256
       2019-01-07 93.941632 103.319168 105.674012 95.891062 86.547934
```

The standard normally distributed pseudo-random numbers.

The start date for the DatetimeIndex object.

The frequency ("business daily").

The number of periods needed.

A linear transform of the raw data.

The column headers as single characters.

The DatetimeIndex object.

The first five rows of data.

Cufflinks adds a new method to the DataFrame class: df.iplot(). This method uses plotly in the backend to create interactive plots. The code examples in this section all make use of the option to download the interactive plot as a static bitmap, which in turn is embedded in the text. In the Jupyter Notebook environment, the created plots are all interactive. The result of the following code is shown in Figure 7-22:

```
In [50]: plyo.iplot(
             df.iplot(asFigure=True),
             # image='png',
             filename='ply_01'
         )
```

This makes use of the offline (notebook mode) capabilities of plotly.

The df.iplot() method is called with parameter asFigure=True to allow for local plotting and embedding.

The image option provides in addition a static bitmap version of the plot.

The filename for the bitmap to be saved is specified (the file type extension is added automatically).

![](_page_42_Figure_0.jpeg)

As with matplotlib in general and with the pandas plotting functionality, there are multiple parameters available to customize such plots (see Figure 7-23):

```
In [51]: plyo.iplot(
             df[['a', 'b']].iplot(asFigure=True,
                      theme='polar',
                      title='A Time Series Plot',
                      xTitle='date',
                      yTitle='value',
                      mode={'a': 'markers', 'b': 'lines+markers'},
                      symbol={'a': 'circle', 'b': 'diamond'},
                      size=3.5,
                      colors={'a': 'blue', 'b': 'magenta'},
                                 ),
             # image='png',
             filename='ply_02'
         )
```

Selects a theme (plotting style) for the plot.

Adds a title.

Adds an x-axis label.

Adds a y-axis label.

Defines the plotting *mode* (line, marker, etc.) by column.

Defines the symbols to be used as markers by column.

Fixes the size for all markers.

Specifies the plotting color by column.

![](_page_43_Figure_12.jpeg)

*Figure 7-23. Line plot for two columns of the DataFrame object with customizations*

Similar to matplotlib, plotly allows for a number of different plotting types. Plotting types available via Cufflinks are chart, scatter, bar, box, spread, ratio, heatmap, surface, histogram, bubble, bubble3d, scatter3d, scattergeo, ohlc, candle, pie, and choropleth. As an example of a plotting type different from a line plot, consider the histogram (see [Figure](#page-44-0) 7-24):

```
In [52]: plyo.iplot(
             df.iplot(kind='hist',
                      subplots=True,
                      bins=15,
                      asFigure=True),
             # image='png',
             filename='ply_03'
         )
```

Specifies the plotting type.

Requires separate subplots for every column.

Sets the bins parameter (buckets to be used = bars to be plotted).

<span id="page-44-0"></span>![](_page_44_Figure_8.jpeg)

![](_page_44_Figure_9.jpeg)

*Figure 7-24. Histograms per column of the DataFrame object*

# **Financial Plots**

The combination of plotly, Cufflinks, and pandas proves particularly powerful when working with financial time series data. Cufflinks provides specialized functionality to create typical financial plots and to add typical financial charting elements, such as the Relative Strength Index (RSI), to name but one example. To this end, a persistent QuantFig object is created that can be plotted the same way as a DataFrame object with Cufflinks.

This subsection uses a real financial data set, time series data for the EUR/USD exchange rate (source: FXCM Forex Capital Markets Ltd.):

```
In [54]: raw = pd.read_csv('../../source/fxcm_eur_usd_eod_data.csv',
                        index_col=0, parse_dates=True)
In [55]: raw.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 1547 entries, 2013-01-01 22:00:00 to 2017-12-31 22:00:00
        Data columns (total 8 columns):
        BidOpen 1547 non-null float64
        BidHigh 1547 non-null float64
        BidLow 1547 non-null float64
        BidClose 1547 non-null float64
        AskOpen 1547 non-null float64
        AskHigh 1547 non-null float64
        AskLow 1547 non-null float64
        AskClose 1547 non-null float64
        dtypes: float64(8)
        memory usage: 108.8 KB
In [56]: quotes = raw[['AskOpen', 'AskHigh', 'AskLow', 'AskClose']]
        quotes = quotes.iloc[-60:]
        quotes.tail()
Out[56]: AskOpen AskHigh AskLow AskClose
        2017-12-25 22:00:00 1.18667 1.18791 1.18467 1.18587
        2017-12-26 22:00:00 1.18587 1.19104 1.18552 1.18885
        2017-12-27 22:00:00 1.18885 1.19592 1.18885 1.19426
        2017-12-28 22:00:00 1.19426 1.20256 1.19369 1.20092
        2017-12-31 22:00:00 1.20092 1.20144 1.19994 1.20144
```

Reads the financial data from a CSV file.

The resulting DataFrame object consists of multiple columns and more than 1,500 data rows.

Selects four columns from the DataFrame object (Open-High-Low-Close, or OHLC).

Only a few data rows are used for the visualization.

Returns the final five rows of the resulting data set quotes.

During instantiation, the QuantFig object takes the DataFrame object as input and allows for some basic customization. Plotting the data stored in the QuantFig object qf then happens with the qf.iplot() method (see Figure 7-25):

```
In [57]: qf = cf.QuantFig(
                  quotes,
                  title='EUR/USD Exchange Rate',
                  legend='top',
                  name='EUR/USD'
         )
In [58]: plyo.iplot(
             qf.iplot(asFigure=True),
             # image='png',
             filename='qf_01'
         )
```

The DataFrame object is passed to the QuantFig constructor.

This adds a figure title.

The legend is placed at the top of the plot.

This gives the data set a name.

![](_page_48_Figure_0.jpeg)

*Figure 7-25. OHLC plot of EUR/USD data*

Adding typical financial charting elements, such as Bollinger bands, is possible via different methods available for the QuantFig object (see Figure 7-26):

```
In [59]: qf.add_bollinger_bands(periods=15,
                                boll_std=2)
In [60]: plyo.iplot(qf.iplot(asFigure=True),
              # image='png',
              filename='qf_02'
         )
```

The number of periods for the Bollinger band.

The number of standard deviations to be used for the band width.

![](_page_49_Figure_0.jpeg)

*Figure 7-26. OHLC plot of EUR/USD data with Bollinger band*

Certain financial indicators, such as RSI, may be added as a subplot (see Figure 7-27):

```
In [61]: qf.add_rsi(periods=14,
                   showbands=False)
In [62]: plyo.iplot(
              qf.iplot(asFigure=True),
              # image='png',
              filename='qf_03'
         )
```

Fixes the RSI period.

Does not show an upper or lower band.

![](_page_50_Figure_1.jpeg)

*Figure 7-27. OHLC plot of EUR/USD data with Bollinger band and RSI*

# **Conclusion**

matplotlib can be considered both the benchmark and an all-rounder when it comes to data visualization in Python. It is tightly integrated with NumPy and pandas, and the basic functionality is easily and conveniently accessed. However, matplotlib is a mighty library with a somewhat complex API. This makes it impossible to give a broad overview of all the capabilities of matplotlib in this chapter.

This chapter introduces the basic functions of matplotlib for 2D and 3D plotting useful in many financial contexts. Other chapters provide further examples of how to use the package for visualization.

In addition, this chapter covers plotly in combination with Cufflinks. This combination makes the creation of interactive D3.js plots a convenient affair since only a single method call on a DataFrame object is necessary in general. All technicalities are taken care of in the backend. Furthermore, Cufflinks provides with the QuantFig object an easy way to create typical financial plots with popular financial indicators.
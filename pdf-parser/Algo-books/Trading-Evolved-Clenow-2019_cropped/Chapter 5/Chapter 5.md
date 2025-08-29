## **Bring out the Pandas**

I told you before that I'm going to drop you right into the deep end. It's more interesting to learn if you see some real use for your knowledge early on. So let's move right along here, and get something useful done.

The **Pandas** library is an absolute game changer in the world of Python. There are entire books written just about **Pandas** , most notably the book Python for *Data Analysis* , by the guy who actually wrote the **Pandas** library to begin with, Wes McKinney (McKinney, 2017). I won't go into anywhere near the kind of details that he does, but I will keep using his brilliant library over and over in this book.

The **Pandas** , commonly spelled in all lower caps for reasons that I haven't fully understood and therefore refuse to comply with, is a library to handle structured data. Most importantly for us traders, it excels at dealing with time series data.

For our next trick, we will read time series data from a file, calculate a moving average on this and then show a graph. That sounds a little more complex than the loop stuff you did before, right?

The first question is, where we get the data from. If you pick up any random Python book written before 2017, they probably show you how to automatically get data from Yahoo or Google in a single line of code. Well, as it turns out, that did not work out very well, no fault of the authors. Both Yahoo and Google decided to shut down these services without prior notice, leaving thousands of code samples in books and websites permanently bricked.

For this first exercise, I will assume that you have a local comma separated file with some data that we can use. If you don't have one handy, download one from my website **www.followingthetrend.com/trading-evolved** . Keeping our first time series experiment simple, the layout of your file has two columns

only. The first one with dates and the second with prices. Here is how my file looks.

Date,SP500 2009-06-23,895.1 2009-06-24,900.94 2009-06-25,920.26 2009-06-26,918.9 2009-06-29,927.23 2009-06-30,919.32 2009-07-01,923.33 2009-07-02,896.42 2009-07-06,898.72 2009-07-07,881.03 2009-07-08,879.56 2009-07-09,882.68 2009-07-10,879.13 2009-07-13,901.05 2009-07-14,905.84 2009-07-15,932.68 2009-07-16,940.74 2009-07-17,940.38 2009-07-20,951.13 ...

> In case you reside on the other side of the Pond from me, you may take issue with my choice of date format. I use yyyy-mm-d d format, which is common around my parts but might not be where you live. No worries. It does not matter. Use whatever date format you are comfortable with. Pandas will figure it out for you later.

> For convenience, place this csv file in the same folder where you will save the Python code. You can put it anywhere you like of course, but if it's not in the same folder you will have to specify a path in the code, so that we can find the file.

> Now we are ready to build the code. Get back to **Jupyter Notebook** and make a new file. This time, we will learn a few more new concepts. The first one is to import a library to use with our code, in this case the **Pandas** .

> To read this data, calculate a moving average and show a chart, all we have to do is the following code.

%matplotlib inline import pandas as pd data = pd.read\_csv('sp500.csv', index\_col='Date', parse\_dates=['Date']) data['SMA'] = data['SP500'].rolling(50).mean() data.plot()

That's really not bad, is it? Consider how easy that was, compared to what it would take in most other programming environments.

Here is what this code does. The first quirky looking row, %matplotlib inlin e , is something you will see a lot from now on. The details of why this row is needed are not important at the moment, but this row is required to make sure that graphs will be shown in the notebook. If you forget that row, you will only get text output and no graph.

Next, we tell our code that we want to use the **Pandas** library, import pandas as p d . As is common, we make an alias for **Pandas** , so that we can refer to it by p d , instead of panda s . That's just to avoid having to type the whole word over and over again, as this library is likely to be used a lot going forward. You will see this alias often, and whenever code in this book refers to p d , that would be a reference to the **Pandas** library.

After this we see the following row: data = pd.read\_csv('sp500.csv', index\_col='Date', parse\_dates=['Date'] ) , reads the file from disk into the variable called dat a . We specify here that the column with the header Dat e is the index, and that we want **Pandas** to parse the date format of this column. See, I told you that your choice of date format does not matter. Even though the European one is clearly superior. This is where **Pandas** will sort it out for you.

Then we have the next row, data['SMA'] = data['SP500'].rolling(50).mean( ) , which adds a moving average, or as it's usually referred to by fancy data scientists, a rolling mean. As you may already surmise, there are a plethora of other functions that can be applied on a rolling window this way, using the same syntax.

The rolling mean here is calculated on the column sp50 0 . In case you are wondering where that name comes from, the answer is simple. Look at the layout of my sample csv file again. That was the name of the second column, the one containing the index closing prices.

**Pandas** will read the names of the headers, and you can refer to them later in this manner. The object that we created by reading the csv file is called a **DataFrame** . That's an important **Pandas** concept that we will return to many times in this book.

Think of a **DataFrame** as a spreadsheet. Just better. It has rows and columns, just like a spreadsheet, and you can easily perform mathematical functions on it. A **DataFrame** has an index, which can be either just row numbers or something more useful such as dates in the case of time series. Columns can have named headers, making it easy to refer to them.

And the final row of our code? It creates a chart of our data, using the simple function call plot( ) . The output should look pretty much like Figure 6‑1.

![](_page_3_Figure_4.jpeg)

*Figure 6*‑*1 Our first Chart*

That's pretty neat, right? We pulled in data, parsed dates, calculated analytics and built a chart, and all in just a few lines of code. I hope at this point, if you are new to all of this, that the value of Python should start to become clearer.

The really interesting row here is really the one that calculates the rolling mean. Obviously the math is dead simple, but that's beside the point. The really exciting thing here is how it's done. That we can simply take a time series, get a rolling window and do math on this directly.

To understand why this is so neat, take a moment to consider how you would have done the same thing in Excel.

Opening the csv file in Excel is no issue of course. You would then scroll down to the 50 th data point, probably on row 51 since you have column headers at top. There, you would write a formula like =AVERAGE(B51:OFFSET(B51,-49,0) ) . Then you would need to copy this all the way down. This means that you will have a large number of individual functions in your sheet already. And don't forget that Excel keeps recalculating every single formula, any time you change anything in the spreadsheet. That being one of major issues with Excel of course.

The offset in Excel would need to be 49 and not 50, as the starting cell, B51, is counted as well.

Using Python, we can apply a function on an entire time series at once. In this case, it's simple math, but as you will see later, it works the same way with complex calculations.

| C51 | $\overline{w}$ |        | $f_x$    |   | =AVERAGE(B51:OFFSET(B51,-49,0)) |   |   |
|-----|----------------|--------|----------|---|---------------------------------|---|---|
| A.  | Α              | B      | C        | D | E                               | F | G |
| 50  | 1990-03-12     | 338.67 |          |   |                                 |   |   |
| 51  | 1990-03-13     | 336    | 335.755  |   |                                 |   |   |
| 52  | 1990-03-14     | 336.87 | 335.2986 |   |                                 |   |   |
| 53  | 1990-03-15     | 338.07 | 334.8848 |   |                                 |   |   |
| 54  | 1990-03-16     | 341.91 | 334,6096 |   |                                 |   |   |
| 55  | 1990-03-19     | 343.53 | 334,4362 |   |                                 |   |   |
| 56  | 1990-03-20     | 341.57 | 334.1918 |   |                                 |   |   |
|     |                |        |          |   |                                 |   |   |

*Figure 6*‑*2 Moving Average in Excel*

With Excel, this simple task requires thousands of individual

formulas and the mixing of data and logic in the same file. Now imagine if we want to shift between many different financial time series, and many different analytics. The Excel file would grow increasingly complex and would quickly get unmaintainable. The Python way is far superior.

# **Documentation and Help**

After seeing that code sample in the previous section, it would be fair to ask how you could possibly know what argument to use in order to get Pandas to set an index column, or to parse the dates. Not to mention how you could know what other possible arguments there are.

You could approach this in two ways, which will probably yield the same information in the end. One way would be to search the internet, which will likely give you both the official documentation and various usage samples in the first few returns from your search engine of choice.

Then again, you might as well just look up the details in the built-in documentation. It's all there, and will pop up on your screen if you say the magic words. All, or at least the vast majority of Python libraries have this kind of built in documentation. As a demonstration, let's use **Pandas** to find out about what it is, how it works, what functions are available and finally how exactly to use read\_csv( ) .

Open up a new Jupyter Noteboo k again. Or if you're feeling really lazy, download the sample from the book website, as all code samples are available there. First import Pandas, the same way as we've done before.

```
import pandas as pd
```

Now we can refer to is by the alias p d . In the next cell, simply run this line of code.

help(pd)

That will show you an overview of what **Pandas** is, which version you're using and some technical information that you're probably not too interested in at the moment. Your output should look more or less like the text below.

Help on package pandas:

### NAME

pandas

#### DESCRIPTION

pandas - a powerful data analysis and manipulation library for Python =====================================================================

\*\*pandas\*\* is a Python package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, \*\*real world\*\* data analysis in Python. Additionally, it has the broader goal of becoming \*\*the most powerful and flexible open source data analysis / manipulation tool available in any language\*\*. It is already well on its way toward this goal.

#### Main Features

-------------

Here are just a few of the things that pandas does well:

- Easy handling of missing data in floating point as well as non-floating point data
- Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
- Automatic and explicit data alignment: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let `Series`, `DataFrame`, etc. automatically align the data for you in computations
- Powerful, flexible group by functionality to perform split-apply-combine operations on data sets, for both aggregating and transforming data
- Make it easy to convert ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects
- Intelligent label-based slicing, fancy indexing, and subsetting of large data sets
- Intuitive merging and joining data sets
- Flexible reshaping and pivoting of data sets
- Hierarchical labeling of axes (possible to have multiple labels per tick)
- Robust IO tools for loading data from flat files (CSV and delimited), Excel files, databases, and saving/loading data from the ultrafast HDF5 format
- Time series-specific functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions,

date shifting and lagging, etc.

The help function gives us some overview information about the **Pandas** library, but it lacks the details about what objects are in there, and how they work. No worries, we can go deeper in the documentation.

We can run the same help function on the **DataFrame** as well. Try executing the following line in the **Jupyter Notebook** .

### help(pd.DataFrame)

...

That will give you quite a long list of functionality built into the **DataFrame** object. As general rule, for now you can safely ignore all the built in functions starting with underscores. The text that comes up tells you what a **DataFrame** is, what purpose it has, and it lists functions and features.

You can take this help business a step further and ask for the details on the **read\_csv()** function itself.

help(pd.read\_csv)

Executing that line will show you all possible arguments that can be used for reading a csv file, what the default values of these are as well as a description of each argument. That should tell you all that you need to know about how to use this function.

In the example here, we were looking for information on the index column and the date parsing. So let's look closer at what this documentation says about those.

index\_col : int or sequence or False, default None Column to use as the row labels of the DataFrame. If a sequence is given, a MultiIndex is used. If you have a malformed file with delimiters at the end of each line, you might consider index\_col=False to force pandas to \_not\_ use the first column as the index (row names)

This tells us that we could decide on index columns by providing a number or a name, but we can also decide not to have a number. If you use a number, remember that everything in Python

world is zero based, so the first column in your file would have number 0.

Then we'll check the same documentation for parsing dates. That expression refers to having the code analyze the text string and figure out how to make a date out of it.

parse\_dates : boolean or list of ints or names or list of lists or dict, default False

\* boolean. If True -> try parsing the index.

- \* list of ints or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3 each as a separate date column.
- \* list of lists. e.g. If [[1, 3]] -> combine columns 1 and 3 and parse as a single date column.

\* dict, e.g. {'foo' : [1, 3]} -> parse columns 1, 3 as date and call result 'foo'

If a column or index contains an unparseable date, the entire column or index will be returned unaltered as an object data type. For non-standard datetime parsing, use ``pd.to\_datetime`` after ``pd.read\_csv``

This text tells us that if we want to parse dates, one way would be to simply set parse\_dates=Tru e . If we do that, **Pandas** will try to make dates out of the index column. Sometimes we may want to tell it to parse other columns, so we also have the option to specify which columns should be analyzed as dates and parsed, by providing a list of column numbers or names.

This way of obtaining documentation can be used for practically anything. If you get lost, either type the function name into a search engine, or use the built in help functionality.

## **Simple Python Simulation**

Now we are going to step this up a bit with another little demo of how quickly Python can get useful. For this demo, we will use the same S&P 500 data and build a simulation. What would happen if we

would go long when a 50 day moving average crosses above a 100 day moving average, and close when it crosses back down?

No, I'm not saying that's a good strategy to trade. This is merely an example, and one which is very easy to code. Also, we are not aiming for realism here. Not in this chapter. This is after all the Python intro chapter. So for now, things are going to be kept fairly simple.

For this simulation, we are going to use the **Pandas** library again, as well as one more very useful and very common library. **Numpy** , short for Numerical Python, is a library with all kinds of useful mathematical functions. They make life in Python Land easier, as well as quicker. Just as **Pandas** is usually aliased as p d , **Numpy** is usually aliased as n p . That's the way I will do it here, and throughout the book.

While **Numpy** is most likely already installed in your root environment, you could always verify in **Anaconda Navigator** , as we looked at in chapter 5. If it's not installed, go ahead and install it. This is another library which you will probably be using quite a lot.

We will do this step by step, to make sure you follow the logic. And trust me, this is not complex stuff. At least not yet. We are going to about 10 rows of code here, no more. It could be done with less even.

# Make sure the plot shows up %matplotlib inline

# Import libraries that we need import pandas as pd import numpy as np

Ok, so those initial lines should be clear by now. First that row to make sure that the graphs appear in the notebook, and then a couple of import statements, so that we can use the functionality of **Numpy** and **Pandas** .

Well, this one we have seen before. We are reading the data from a file, into a **Pandas DataFrame** .

```
# Calculate two moving averages
data['SMA50'] = data['SP500'].rolling(50).mean()
data['SMA100'] = data['SP500'].rolling(100).mean()
```

These lines of code calculate the two moving averages that we are going to use for the simulation. As you see, they just reference a rolling time window of 50 and 100 rows respectively, and calculates a mean of those.

```
# Set to 1 if SMA50 is above SMA100
data['Position'] = np.where(data['SMA50'] > data['SMA100'], 1, 0)
```

The next line checks which days we should be long, and which days we should be flat. The strategy being that we will be long if the faster moving average is above the slower. That is, when the column SMA5 0 is above SMA10 0 , we will be long. Else we are going to be flat.

What the line above does is to set the column Positio n to 1 where SMA5 0 is higher than SMA10 0 , and set all other days as 0 .

But, here's an important part in terms of the logic. At this point in the code, the position column changes the same day as the average crosses over. That is, we trade instantly at the closing price, the same value that we base our average calculation on, and thereby our signal. That's clearly cheating. To make this even reasonably fair, we need to delay the trade to the day after the signal. Luckily, this is very easily done.

# Buy a day delayed, shift the column data['Position'] = data['Position'].shift()

Next we calculate how many percent per day the strategy changes. This is easy, if you think about it. We know how many percent the index moves per day. And we know that we will be long 100% of the index if the 50 day moving average is above the 100. If that's not the case, we are not owning any.

We take the daily percent change of the index, and multiply by the Positio n column that we just created. Remember that this column will be 1 if we should be long, else 0.

Notice how easily you can get the percentage return from the index. We just refer to that column in our Pandas **DataFrame** , and call the function pct\_change( ) .

```
# Calculate cumulative returns
data['Strategy'] = (data['StrategyPct'] + 1).cumprod()
```

Next it's time to calculate the return of our strategy. We already know the daily return numbers, and we just need to make a time series out of it. The simplest way would be to add the number 1 to all the percentage returns, and then use the Pandas function cumprod( ) . This will calculate a cumulative product of the series.

Note in the above line of code that we can add a number to each row in the column, simply by using the plus sign. Other programming languages would complain that we are mixing concepts, trying to add a static number to a list of numbers. But Pandas will figure out what we mean, and add the number to every single row.

```
# Calculate index cumulative returns
data['BuyHold'] = (data['SP500'].pct_change(1) + 1).cumprod()
```

It would be useful to plot the buy and hold alternative, next to the strategy, so that we can compare the two. The method here is the same as when we calculated the strategy returns, we just base it on the actual S&P time series instead.

# Plot the result data[['Strategy', 'BuyHold']].plot()

Finally, the last row, plotting the two lines. Last time we plotted something, we did not specify which columns we wanted to plot, because there were only two columns and we wanted to plot them both. If we don't specify which columns to plot, we would get all of them. And that would look like spaghetti. All we care about here is to show the equity curve of our strategy next to the buy and hold

benchmark, and that's what this does.

![](_page_13_Figure_1.jpeg)

*Figure 6*‑*3 Simple Simulation Results*

Given the black and white nature of this book, and the fact that we haven't yet learnt how to make dashed or dotted lines in a Python plot. We'll get to that later. But in case you're wondering that's our strategy at the bottom in the chart. Showing lower returns, but also seemingly lower volatility. Clearly a graph like this is not enough to decide if the strategy is any good, but that's not what we care about at the moment.

You just made your first Python backtest. Congratulations!

Most of you are probably far more familiar with Excel than with **Pandas DataFrames** , and it may be helpful to see how the columns we calculated would have looked in Excel. The **Dataframe** that we created will be structured as in Figure 6‑4. The first column, SP500, comes straight from the data file, while all others are calculated. Depending on if the SMA50 is higher than SMA100, the column Positio n will show either 1 or 0. If it shows 1, we assume that the strategy is holding a position of 100% of the portfolio value, and multiply the previous strategy value with the day's percent change in the index.

| Date       | SP500    | SMA50    | SMA100   |   | Position StrategyPct | Strategy | BuyHold |
|------------|----------|----------|----------|---|----------------------|----------|---------|
| 2010-06-03 | 1,102.83 | 1,158.66 | 1,137.63 | 1 | 0.41%                | 1.00     | 1.23    |
| 2010-06-04 | 1,064.88 | 1,156.60 | 1,136.81 | 1 | -3.44%               | 0.97     | 1.19    |
| 2010-06-07 | 1,050.47 | 1,154.29 | 1,135.95 | 1 | $-1.35\%$            | 0.96     | 1.17    |
| 2010-06-08 | 1,062.00 | 1,152.20 | 1,135.11 | 1 | 1.10%                | 0.97     | 1.19    |
| 2010-06-09 | 1,055.69 | 1,149.85 | 1,134.18 | 1 | -0.59%               | 0.96     | 1.18    |
| 2010-06-10 | 1,086.84 | 1,148.12 | 1,133.69 | 1 | 2.95%                | 0.99     | 1.21    |
| 2010-06-11 | 1,091.60 | 1,146.57 | 1,133.11 | 1 | 0.44%                | 0.99     | 1.22    |
| 2010-06-14 | 1,089.63 | 1,144.80 | 1,132.62 | 1 | $-0.18\%$            | 0.99     | 1.22    |
| 2010-06-15 | 1,115.23 | 1,143.35 | 1,132.61 | 1 | 2.35%                | 1.02     | 1.25    |
| 2010-06-16 | 1,114.61 | 1,141.86 | 1,132.84 | 1 | -0.06%               | 1.01     | 1.25    |
| 2010-06-17 | 1,116.04 | 1,140.53 | 1,133.03 | 1 | 0.13%                | 1.02     | 1.25    |
| 2010-06-18 | 1,117.51 | 1,139.15 | 1,133.28 | 1 | 0.13%                | 1.02     | 1.25    |
| 2010-06-21 | 1,113.20 | 1,137.53 | 1,133.44 | 1 | -0.39%               | 1.01     | 1.24    |
| 2010-06-22 | 1,095.31 | 1,135.50 | 1,133.55 | 1 | $-1.61\%$            | 1.00     | 1.22    |
| 2010-06-23 | 1,092.04 | 1,133.40 | 1,133.73 | 1 | -0.30%               | 0.99     | 1.22    |
| 2010-06-24 | 1,073.69 | 1,130.66 | 1,133.58 | 0 | 0.00%                | 0.99     | 1.20    |
| 2010-06-25 | 1,076.76 | 1,127.96 | 1,133.31 | 0 | 0.00%                | 0.99     | 1.20    |
| 2010-06-28 | 1,074.57 | 1,125.61 | 1,133.08 | 0 | 0.00%                | 0.99     | 1.20    |
| 2010-06-29 | 1,041.24 | 1,122.48 | 1,132.86 | 0 | 0.00%                | 0.99     | 1.16    |
| 2010-06-30 | 1,030.71 | 1,118.95 | 1,132.51 | 0 | 0.00%                | 0.99     | 1.15    |
| 2010-07-01 | 1,027.37 | 1,115.38 | 1,132.22 | 0 | 0.00%                | 0.99     | 1.15    |
| 2010-07-02 | 1,022.58 | 1,111.66 | 1,131.74 | 0 | 0.00%                | 0.99     | 1.14    |
| 2010-07-06 | 1,028.06 | 1,107.88 | 1,131.34 | 0 | 0.00%                | 0.99     | 1.15    |
| 2010-07-07 | 1,060.27 | 1,104.84 | 1,131.15 | 0 | 0.00%                | 0.99     | 1.18    |
| 2010-07-08 | 1,070.25 | 1,102.57 | 1,131.10 | 0 | 0.00%                | 0.99     | 1.20    |
| 2010-07-09 | 1,077.96 | 1,100.30 | 1,130.93 | 0 | 0.00%                | 0.99     | 1.20    |

*Figure 6*‑*4 Excel Table View of Simple Simulation Data*

If you followed this example so far, you are hopefully getting a bit impressed over how Python can get things done really quickly and easily. Then again, perhaps you are already starting to pick this example apart and question the validity of this simulation.

Some would now question if this really a legitimate simulation, given how it does not account for transactions costs, for example. Well, if that was your concern regarding validity, you missed the big one. We are 'trading' the S&P 500 Index here. That's not a tradeable security. You can't trade an index. And that's not the only issue.

So no, this simulation we just did, is hardly built for realism. There are plenty of issues with it, and there are good reasons for why we don't just do all our simulations with such simple logic. But that was of course not the point here. The point is to demonstrate some

neat things with the language Python.

Before moving on to realistic simulations, we are going to look at a few more easy and fun examples to get everyone up to speed on Python and the neat things it can do for us.

# **Making a Correlation Graph**

There are a couple of more common concepts that I would like to demonstrate to you before moving on. Open up a new file in **Jupyter Notebook** . This time we are going to make a graph showing correlation over time between the S&P 500 and the Nasdaq.

The most important point that I want to demonstrate this time is how functions work in Python. We are going to make a flexible and reusable function for fetching data from disk. This function can then be used to read the different csv files. Once we have that data, we will use that data to calculate rolling correlations, before plotting the result. Easy.

When it comes to calculating correlations, you will likely notice that most practitioners prefer to use log returns. The reason for that is that it can be very convenient to work with log returns when processing and analyzing time series data, but it has no discernable impact on the end result.

The point here is to demonstrate concepts, and for now I will stick to good old percentage returns. Nothing wrong with that. What's important to understand however is that for correlations to make sense, you do need to use one of these two alternatives. Either log returns or percentage returns. Calculating correlations on the price levels themselves wouldn't make logical sense, and neither would using the dollar change.

Here is the code for our correlation plot program.

#### %matplotlib inline

import pandas as pd

def get\_returns(file):

""" This function get\_data reads a data file from disk and returns percentage returns. """

return pd.read\_csv(file + '.csv', index\_col=0, parse\_dates=True).pct\_change()

```
# Get the S&P time series from disk
df = get_returns('SP500')
```

# Add a column for the Nasdaq df['NDX'] = get\_returns('NDX')

```
# Calculate correlations, plot the last 200 data points.
df['SP500'].rolling(50).corr(df['NDX'])[-200:].plot()
```

Notice how in this code, there are comments that help explain what is going on. It's a good idea to write comments in the code, both for yourself to remember things and for others to be able to read it.

As you see here, there are two ways of making comments. One is a block comment, which is bookended by triple quotation marks. Anything written between the triple quotes will be deemed a comment.

The second way is to use a hash sign, and everything after that character will become a comment.

To the actual code. See that row starting with the keyword de f ? That defines a function. A function is a piece of code, encapsulating some functionality which hopefully can be reused. This simple function, get\_return s , takes a file name as an argument. We give that function a file name, and it will read that file from disk, if it exists in the same folder as the program, and returns daily percent returns. We have seen this before.

We are going to call this function twice. First to read the S&P 500 data from disk into a **Pandas DataFrame** , and then again to add the Nasdaq data to that **DataFrame** .

When you try this out, you could either use your own data for

This is the layout that I used for my files:

Date,SP500 1990-01-02,359.69 1990-01-03,358.76 1990-01-04,355.67 1990-01-05,352.2 1990-01-08,353.79 1990-01-09,349.62 1990-01-10,347.31 1990-01-11,348.53 1990-01-12,339.93 1990-01-15,337 1990-01-16,340.75 1990-01-17,337.4 1990-01-18,338.19 ...

> After this, it gets interesting. This row is meant to teach you something about **Pandas** , and how easily you can do calculations on it.

> Once we have the **DataFrame** with the two time series, we use a single line of code for multiple, complex operations. In a single row, the last row of that code sample, we do the following:

- Apply a correlation formula on a rolling 50 day window of the percent returns for the indexes.
- Discard all data except the last 200 rows.
- Draw a plot of the result.

Now imagine doing the same thing in Microsoft Excel. You would need a very large number of formulas. One for each individual calculation. But with Python, you just got the task done in a single line.

The function here, get\_returns(file ) , is not executed until some other code calls it. Even though the code is run in order, from the top down, the function is skipped over, until some other code requests it.

As you see we can call the same function many times, using different arguments to read different files, instead of writing this code over and over every time. That cuts down on the amount of code we need and makes it easier to maintain and find errors.

Now, after calling the function twice, once for each file that we are reading, the variable d f holds a **DataFrame** with our daily percent return data. The file would look more or less like Table 6.1. That's an important point to keep in mind here, that a **DataFrame** can be thought of as a table, or a spreadsheet if you like.

| Date       | SP500                  | NDX                   |
|------------|------------------------|-----------------------|
| 1990-01-03 | -0.0025855597875948932 | -0.007135799758480665 |
| 1990-01-04 | -0.008613000334485421  | -0.006125608137992011 |
| 1990-01-05 | -0.009756234711952194  | -0.007008877912021982 |
| 1990-01-08 | 0.004514480408858601   | 0.0017925965761405038 |
| 1990-01-09 | -0.011786653099296274  | -0.010557394649727048 |
| 1990-01-10 | -0.0066071735026600464 | -0.02091057057600143  |

*Table 6.1 Daily Percent Returns Data*

The source data files, SP500.cs v and NDX.cs v , contain in my case data from 1990 onwards. That's a lot of data points, and we only want to plot the last 200 rows here. This is daily data, so one row per day.

We will do this by using a powerful concept called slicing. We are going to slice the data. With this trick, we can refer to part of a **DataFrame** , and the same logic works for many other types of objects as well.

The basics are very simple. You can slice an object by using the syntax [start:stop:step ] after the object. This is important, so we will take a moment to look at that. Slicing is something that you really want to understand.

For a sequence of data, such as a **DataFrame** , we can select a part of it using this concept. If we wanted to just refer to just a part of the object refs that we just created, or any similar object, we could use

this slicing.

If we have an object called data and wanted to refer to a segment starting at the 100 th row and ending at the 200 th row, taking every second row between those, we would use data[100:200:2 ] . Simple and straight forward. We don't have to supply all three, if we don't want to. Leave out the step number, and you will get all the rows.

The syntax data[50:60 ] will give you all rows from row 50 to row 60. If you write data[-50:-20 ] you will get rows starting from the 50 th from the end, to the 20 th from the end. And if you simply say data[-10: ] you will get data from the tenth last, to the very last row.

In his example, I want to plot the last 200 points only, simply to make the graph easy to read. We can do this by using a negative value to refer to the starting point, which **Pandas** will interpret as number of points from the end, instead of from the start.

Remember that the variable we have created in the example is called d f , a completely arbitrary name of course. So if we type df[-200: ] that would refer to the last 200 points of the d f object. We need that colon sign in there, to make it clear that we are going for a slice. If you would simply write df[200 ] we would just get one single row, the 200 th row.

But we are not plotting the d f objects itself. We want to plot the correlations based on the data in d f .

Look at that last row in the code sample, df['SP500'].rolling(50).corr(df['NDX'])[-200:].plot( ) . It actually does multiple things in one line. It starts with the column 'SP500 ' , references a rolling window of 50 rows. It then calculates the correlation against column 'NDX ' . That's a very easy way to make a time series of correlations.

Next you see the brackets, which is where we slice the data. We start at row -200, until the end of the series. Finally, we plot this series. And the output should look like Figure 6‑5.

![](_page_20_Figure_0.jpeg)

*Figure 6*‑*5 Correlation Graph*

I hope by this point that you are starting to see how useful Python can be for working with financial data. You should start to get a hang of the basics on how to deal with time series, and as this book progresses, I will introduce more concepts, tools and tricks for you to use.

Regardless of what technical knowledge you started this book with, my intention is that by the end of it, you should be able to feel comfortable with financial modelling in Python and be able to use your own creativity and solve the tasks that matter to you.

Perhaps most importantly, you should be able to construct realistic trading backtests to test and validate your own trading ideas.

### **Prettier Graphs**

We have made a few simple graphs so far, and we have seen just how simple that can be. Once we have our data in a neat **DataFrame** , we simply tag a .plot( ) on the end, and Bob's your uncle.

That way of making a visual representation of something is really useful for such ad-hoc calculations that you just want to take a quick look at. But it's really quite rudimentary. Often you may want to

make more complex and nicer looking graphs, and you want to be able to control every aspect of the presentation.

In the previous section of this chapter, we installed **matplotlib** , and that's what we are going to use here. With this library, you can make very detailed and very complex plots, if that's your inclination. Sometimes when working with Python, all you want is a quick graphical output to eyeball. Other times, you want something that can impress in presentation material or something very clear for colleagues to be able to interpret and use.

This is still an introductory chapter, and we are going to keep things relatively simple. We are going to use the same data as for the correlation example above. This time, we will plot three subplots, or chart panes if you like. The first will show a rebased comparison of the two indexes, recalculated with the same starting value of 1. This will be shown on a semi logarithmic scale.

The second subplot will show relative strength of the Nasdaq to the S&P 500, and the third the correlation between the two. Mathematically very simple stuff.

As with all code examples in this book, the intention is to keep it easy to read and understand, not to make the most efficient or pretty code. There is a value in making highly efficient and pretty code, but first you need to understand the basics.

I will show you the code bit by bit and explain what's important, and by the end of this section I will show you the complete code all together.

In the code below, we are using similar techniques as previous examples to calculate the data that we need. There are two functions in the code, both of which should at this point seem familiar and understandable.

```
def get_data(file):
  """
  Fetch data from disk
  """
```

```
data = pd.read_csv(file + '.csv', index_col='Date', parse_dates=['Date'])
  return data
def calc_corr(ser1, ser2, window):
  """
  Calculates correlation between two series.
  """
  ret1 = ser1.pct_change()
  ret2 = ser2.pct_change()
  corr = ret1.rolling(window).corr(ret2)
  return corr
```

The first function, get\_dat a simply reads the data from file and hands back to us. The second, calc\_cor r takes two time series as input as well as a time window, and then calculates and returns the resulting correlation series.

Then we set a number of data points that we are planning to plot. If you change this value, the output plot will change accordingly.

```
# Define how many points we intend to plot. Points in this case would be trading days.
points_to_plot = 300
```

# Go get the log return data. data = get\_data('indexes')

> Look at the part below where we rebase the data. Rebasing is about making the data series start at the same initial value, so that they can be visually compared when we plot them. There are some neat tricks there which I wanted to demonstrate.

```
# Rebase the two series to the same point in time, starting where the plot will start.
for ind in data:
  data[ind + '_rebased'] = (data[-points_to_plot:][ind].pct_change() + 1).cumprod()
```

In this code, we loop through each column in the **DataFrame** . For each of them, we create a new column for the rebased value. What we want to achieve here is to have the two series start with the same value, so that they can be compared visually in a graph. Usually when rebasing, you would recalculate all series to start at either 1 or 100.

In this example, we only want to plot the last 300 points, as we defined earlier in the code. The point of rebalancing is to make it look nice in the graph and make it easy to visually compare. Therefore, we

recalculate everything to start at 300 points from the end, all starting with a value of 1.

Note how we used the same slicing concept as previously to select the data. In this code, we use the same syntax to slice off the last 300 points, and then get the percent return of one column at a time, and add the number one. When we add that number, it's added to every single row. So after that operation, every row contains the daily percentage chance, plus one. But the row is not even over yet.

Now on that we run cumprod( ) , calculating the cumulative product, which gives us a rebased series starting at 1. All of this in a single, simple row of code.

Look at that row of code again. Reading the text describing it may seem complicated, but the code is amazingly simple. Think of it as an Excel spreadsheet. We take one column at a time. Calculate percent change, row by row. Add one to that, and calculate a running cumulative product. That is, we start from the beginning and multiply these rows by each other, all the way down.

After this operation, the **DataFrame** data should look more or less as in Table 6.2. We added two new columns, with the rebased values.

| Date       | SP500   | NDX      | SP500_rebased | NDX_rebased |
|------------|---------|----------|---------------|-------------|
| 2017-05-26 | 2415.82 | 5788.359 | 1.00031055    | 1.001727995 |
| 2017-05-30 | 2412.91 | 5794.632 | 0.999105616   | 1.002813594 |
| 2017-05-31 | 2411.8  | 5788.802 | 0.998646002   | 1.00180466  |
| 2017-06-01 | 2430.06 | 5816.511 | 1.006206859   | 1.006599954 |
| 2017-06-02 | 2439.07 | 5881.458 | 1.0099376     | 1.017839621 |
| 2017-06-05 | 2436.1  | 5878.117 | 1.008707822   | 1.01726143  |
| 2017-06-06 | 2429.33 | 5856.769 | 1.005904591   | 1.013566965 |
| 2017-06-07 | 2433.14 | 5877.59  | 1.007482185   | 1.017170228 |
| 2017-06-08 | 2433.79 | 5885.296 | 1.007751328   | 1.018503821 |
| 2017-06-09 | 2431.77 | 5741.944 | 1.006914913   | 0.993695458 |
| 2017-06-12 | 2429.39 | 5708.18  | 1.005929435   | 0.987852292 |
| 2017-06-13 | 2440.35 | 5751.817 | 1.010467605   | 0.99540407  |
|            |         |          |               |             |

*Table 6.2 DataFrame Contents*

| 2017-06-14 | 2437.92 | 5727.066 | 1.009461423 | 0.991120686 |
|------------|---------|----------|-------------|-------------|
| 2017-06-15 | 2432.46 | 5700.885 | 1.007200619 | 0.986589826 |
| 2017-06-16 | 2433.15 | 5681.479 | 1.007486325 | 0.983231442 |
| 2017-06-19 | 2453.46 | 5772.223 | 1.01589602  | 0.998935514 |
| 2017-06-20 | 2437.03 | 5726.311 | 1.009092904 | 0.990990026 |
| 2017-06-21 | 2435.61 | 5782.394 | 1.008504929 | 1.000695697 |
| 2017-06-22 | 2434.5  | 5779.87  | 1.008045315 | 1.000258896 |

Calculating the relative strength is easy, just one series divided by the other. The correlation calculation should also be very familiar by now.

```
# Relative strength, NDX to SP500
data['rel_str'] = data['NDX'] / data['SP500']
```

```
# Calculate 50 day rolling correlation
data['corr'] = calc_corr(data['NDX'], data['SP500'], 100)
```

Now all the data we need is there in our **DataFrame** , calculated and ready to be displayed. At this point, you might want to stop and inspect the data, to make sure it looks as you expected. And of course, there are some useful little tools for that.

In the code sample file that you can download from the book website, I have divided up the code into different cells to make it easy to manage. The code you saw so far in this section is in one cell, which fetches and calculates the data without visualizing it.

If you, after having executed this first cell, make a new cell below, you can stop and take a look at how the DataFram e looks.

One way would be to copy the entire **DataFrame** into clipboard, so that you could paste it into Excel and take a closer look.

```
# You could use this copy the DataFrame to clipboard,
# which could easily be pasted into Excel or similar
# for inspection.
data.to_clipboard()
```

But perhaps you just want to make sure that the layout is as it should and that the values seem reasonable. You could use head( ) or tail( ) to view just the first or the last part of the **DataFrame** .

# We can take a look at the data in the DataFrame # Using head or tail to print from the start or the bottom. data.tail(20)

If you're happy with how the **DataFrame** looks now, we'll move on to slicing the data, effectively discarding all but the last 300 data points, using the slicing logic from before.

```
# Slice the data, cut points we don't intend to plot.
plot_data = data[-points_to_plot:]
```

Now we have all the data ready, and all we need to do is to create a nice looking graph. As you can see here, we have more freedom to format and configure the graph, compared to just the simple .plot( ) which we used before.

In this case, we start by saying that we would like a larger figure, defining the exact size.

```
# Make new figure and set the size.
fig = plt.figure(figsize=(12, 8))
```

Another important point here is the subplo t function, where we give three values. As you see here, the first time we call this function, we give the numbers 311. That means that we intend to build a figure which is three sub plots high, and just one wide. The final number 1 states that we are now defining the first of these three sub plots.

For the first chart pane, or figure as it's called here, as opposed to the entire plot, we first set a title, and then add two semi-log plots. Note how we set one to be solid line and the other dashed, using linestyl e , as well as setting labels and line widths.

```
# The first subplot, planning for 3 plots high, 1 plot wide, this being the first.
ax = fig.add_subplot(311)
ax.set_title('Index Comparison')
ax.semilogy(plot_data['SP500_rebased'], linestyle='-', label='S&P 500', linewidth=3.0)
ax.semilogy(plot_data['NDX_rebased'], linestyle='--', label='Nasdaq', linewidth=3.0)
ax.legend()
ax.grid(False)
```

To make the second figure, we call add\_subplot( ) again, this time providing the numbers 312, showing that we are working on a plot

that's three figures high and one figure wide, and this is the second one.

The second time we call it, we give the numbers 312, declaring that this time we intend to define how the second subplot should look. Here we add the relative strength, and add a label for it. Lastly, we add the third figure and we're all set.

```
# Second sub plot.
ax = fig.add_subplot(312)
ax.plot(plot_data['rel_str'], label='Relative Strength, Nasdaq to S&P 500', linestyle=':',
linewidth=3.0)
ax.legend()
ax.grid(True)
# Third subplot.
ax = fig.add_subplot(313)
ax.plot(plot_data['corr'], label='Correlation between Nasdaq and S&P 500', linestyle='-.',
linewidth=3.0)
ax.legend()
ax.grid(True)
```

Also note in the code that we add legends to the figures, as well as add gridlines to the last two. Again, I added those things just to show you how.

The output of this code should show a figure with three sub plots, each under the next. We have defined names for each line and a name for the overall figure. The first subplot is set to semi logarithmic axes, and we want a grid on the last two subplots. When running this, you should see something very similar to Figure 6‑6.

![](_page_27_Figure_0.jpeg)

The full code in one go would look like this right below.

```
import pandas as pd
import matplotlib.pyplot as plt
```

```
def get_data(file):
  """
  Fetch data from disk
  """
  data = pd.read_csv(file + '.csv', index_col='Date', parse_dates=['Date'])
  return data
```

```
def calc_corr(ser1, ser2, window):
  """
  Calculates correlation between two series.
  """
  ret1 = ser1.pct_change()
  ret2 = ser2.pct_change()
  corr = ret1.rolling(window).corr(ret2)
  return corr
```

# Define how many points we intend to plot. Points in this case would be trading days. points\_to\_plot = 300

```
# Go get the data.
data = get_data('indexes')
```

```
# Rebase the two series to the same point in time, starting where the plot will start.
for ind in data:
  data[ind + '_rebased'] = (data[-points_to_plot:][ind].pct_change() + 1).cumprod()
# Relative strength, NDX to SP500
data['rel_str'] = data['NDX'] / data['SP500']
# Calculate 50 day rolling correlation
data['corr'] = calc_corr(data['NDX'], data['SP500'], 100)
# Slice the data, cut points we don't intend to plot.
plot_data = data[-points_to_plot:]
# Make new figure and set the size.
fig = plt.figure(figsize=(12, 8))
# The first subplot, planning for 3 plots high, 1 plot wide, this being the first.
ax = fig.add_subplot(311)
ax.set_title('Index Comparison')
ax.semilogy(plot_data['SP500_rebased'], linestyle='-', label='S&P 500', linewidth=3.0)
ax.semilogy(plot_data['NDX_rebased'], linestyle='--', label='Nasdaq', linewidth=3.0)
ax.legend()
ax.grid(False)
# Second sub plot.
ax = fig.add_subplot(312)
ax.plot(plot_data['rel_str'], label='Relative Strength, Nasdaq to S&P 500', linestyle=':',
linewidth=3.0)
ax.legend()
ax.grid(True)
# Third subplot.
ax = fig.add_subplot(313)
ax.plot(plot_data['corr'], label='Correlation between Nasdaq and S&P 500', linestyle='-.',
linewidth=3.0)
ax.legend()
ax.grid(True)
```

This is still fairly simplistic graphs of course, but it's meant to demonstrate that there is quite a bit of flexibility in how you visualize data. Now you have seen the basics, and hopefully got a feel for the way things work. We are going to make plenty of more graphs through the book.
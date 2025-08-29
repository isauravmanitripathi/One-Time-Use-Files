# **Analyzing Backtest Results**

Running a backtest and analyzing the results are two quite different tasks. In chapter 7 we wrote some simple backtests, but we did not bother much with analyzing the results.

Analyzing time series is a core strength of Python and we have no shortage of options of what to do with the backtest results. It would be pointless to ask if we can calculate your favorite analytic, because we can of course calculate and visualize just about anything we can think of.

There are two ways we could approach analyzing the backtest results. We could install and use purpose built libraries, or we could build something more custom. In this chapter, we will look at both possibilities and aim to provide you with the tools and knowledge that you will need to figure out if your backtest is any good or not. Simply plotting an equity curve is easy enough, but it rarely tells enough of a story to serve as the basis of real decision making.

### **Installing PyFolio**

The makers of the Zipline backtesting library have also made a useful library to analyze backtest results. This library, **PyFolio** , makes for a good entry gateway to backtest analysis. For many, it may be the only thing you need. For others, it may be a good start and something you can learn from and improve upon.

To install **PyFolio** , we need to use a different method than we have been using before. In the interest of keeping things consistent, I would have preferred to keep using the same way of installing libraries, but as of writing this, a technical issue prevents it.

Instead, we will use a different installation method. Again,

open the terminal with the zip3 5 environment activated. The easiest way is through **Anaconda Navigator** , selecting the correct environment and then starting a terminal window from there. Then enter the following to install **PyFolio** .

pip install pyfolio

As you explore later on your own, you will find that **PyFolio** can do quite a bit of reporting for you. As a demonstration, we are going to create something which **PyFolio** calls a returns tear sheet. That is, an overview analysis of the returns of the strategy. To do this, we first need an algorithm, a trading strategy to analyze.

# **Portfolio Algorithm to Analyze**

We could of course take one of the algorithms that we looked in in the previous chapter, but that wouldn't be much fun. Instead, I will take the portfolio model on the same static Dow Jones that we constructed earlier, and change things around a little.

By using a different trading logic, I can take this chance to teach you something new on that side as well. There are some neat little tricks that I'd like to show you along the way, as we construct a new variant of our Dow Jones trading model.

The model that we will use for analyzing results will also be based on the Dow Jones stocks, but it will use a simple momentum approach. We will check the trading rules only once per month this time, to create a long term investment algorithm which does not have excess costs in terms of commission and tax.

The Dow Jones Industrial Average consists of 30 stocks. Our algorithm here will measure the return in the past month for these 30 stocks, sort them from best to worst performance and buy the top 10. They will be equal weighted again, so each stock would have a weight of 10%.

Fire up a new **Jupyter Notebook** for your zip3 5 environment, and build away. If you already feel comfortable enough with Python, go ahead and try to create these rules yourself. It's not that hard.

On top of writing these new trading rules, there is also the small matter of the actual purpose of this chapter; analyzing backtest results. For that, we need to import the **PyFolio** library that we just installed.

By now you may have noticed the seemingly odd object called contex t . This is a Zipline specific convenience. You can add anything you like to this context object, and it will stay persistent so that you can access it later on. In this case, I tag on a list of stocks to trade and some model settings in the initialize routine. I then read these settings again in the daily trading logic. Note how the context object is passed to our scheduled handle\_dat a routine.

Those familiar with programming may ask why we are not just putting these settings up top, as global objects. Sure, that works fine too, if that's what you prefer. In fact, I do prefer that myself as it tends to result in code that's easier to read and modify, and I will show you how that works in later code in this book. For now, I just wanted to show how you can use the context object, in case you find it of use.

```
# Import a few libraries we need
from zipline import run_algorithm
from zipline.api import order_target_percent, symbol, \
  schedule_function, date_rules, time_rules
from datetime import datetime
import pytz
import pyfolio as pf
def initialize(context):
  # Which stocks to trade
  dji = [
    "AAPL",
    "AXP",
    "BA",
    "CAT",
    "CSCO",
    "CVX",
    "DIS",
    "DWDP",
```

| "GS",   |
|---------|
| "HD",   |
| "IBM",  |
| "INTC", |
| "JNJ",  |
| "JPM",  |
| "KO",   |
| "MCD",  |
| "MMM",  |
|         |
| "MRK",  |
| "MSFT", |
| "NKE",  |
| "PFE",  |
| "PG",   |
| "TRV",  |
| "UNH",  |
| "UTX",  |
| "V",    |
|         |
| "VZ",   |
| "WBA",  |
| "WMT",  |
| "XOM",  |
|         |

]

# Make symbol list from tickers context.universe = [symbol(s) for s in dji]

# History window context.history\_window = 20

# Size of our portfolio context.stocks\_to\_hold = 10

# Schedule the daily trading routine for once per month schedule\_function(handle\_data, date\_rules.month\_start(), time\_rules.market\_close())

def month\_perf(ts): perf = (ts[-1] / ts[0]) - 1 return perf

def handle\_data(context, data): # Get history for all the stocks. hist = data.history(context.universe, "close", context.history\_window, "1d")

# This creates a table of percent returns, in order.

perf\_table = hist.apply(month\_perf).sort\_values(ascending=False)

# Make buy list of the top N stocks buy\_list = perf\_table[:context.stocks\_to\_hold]

# The rest will not be held. the\_rest = perf\_table[context.stocks\_to\_hold:]

# Place target buy orders for top N stocks. for stock, perf in buy\_list.iteritems(): stock\_weight = 1 / context.stocks\_to\_hold

# Place order if data.can\_trade(stock): order\_target\_percent(stock, stock\_weight)

# Make sure we are flat the rest. for stock, perf in the\_rest.iteritems(): # Place order if data.can\_trade(stock): order\_target\_percent(stock, 0.0)

def analyze(context, perf): # Use PyFolio to generate a performance report returns, positions, transactions = pf.utils.extract\_rets\_pos\_txn\_from\_zipline(perf) pf.create\_returns\_tear\_sheet(returns, benchmark\_rets=None)

# Set start and end date start = datetime(2003, 1, 1, tzinfo=pytz.UTC) end = datetime(2017, 12, 31, tzinfo=pytz.UTC)

# Fire off the backtest result = run\_algorithm(start=start, end=end, initialize=initialize, analyze=analyze, capital\_base=10000, data\_frequency = 'daily', bundle='quandl' )

As you can see in this backtest code, we trade only once per month and we use a new way to define that. Look at the last line of code in the initializ e function. There we set a scheduler, so that the trading code in the function handle\_dat a will be run at the start of every month. This is an easy and convenient way of setting your trading frequency, and it can be used for other purposes as well.

In the initializ e function, we first define a list of stock tickers in the DJI. We then make a list of corresponding symbol objects, and store in the context. A symbol object is a Zipline concept, which represents a particular stock.

Later in the handle\_dat a function, you can see how we use a single line of code to pull data for all these stocks at once. This is much faster, not to mention much cleaner and more convenient than looping through them as we did earlier.

```
hist = data.history(context.universe, "close", context.history_window, "1d")
```

The next step in the trading logic really shows off the beauty of Python. Pay attention to this one. It's a really useful trick.

What we are doing is to calculate a ranking table based on percentage returns for our 30 stocks. The code row in question is this.

```
perf_table = hist.apply(month_perf).sort_values(ascending=False)
```

Even if you are familiar with other programming languages, this line may seem confusing to you. It may be a novel concept to many, but it's fairly easy to understand and use.

From the code row before this, we have created the **DataFrame** object his t , by requesting historical closing prices for the stocks in the Dow Jones Index. Now we apply a function on this set of data.

The function in question simply calculates the percentage return between the first and the last data point. As we requested 20 trading days' worth of history, we get the performance for about a month back. The function, month\_per f , was defined in the code as shown just below this paragraph. As you see, we just take the last, i.e. latest data point, divide it by the first data point and deduct one. Or in plain English, we just check the percent difference.

```
def month_perf(ts):
  perf = (ts[-1] / ts[0]) - 1
  return perf
```

What happens when we apply the function on the **DataFrame** is really clever. The percentage return will now be calculated for each stock, and a table will be returned with each stock and the percentage return. In just one line of code, we applied this function and got the table back.

Since we are interested in the order of the percentage returns, we should also sort the data. That's what the last part of this row does, the sort\_values( ) part. As you can see here, I supply the argument ascending=False. Since ascending sorting would be the default, if we don't supply this argument we would get the worst performers on top. Now we have a ready-to-use ranking table, and it would look something like Table 8.1, with symbols and percentage returns.

| Equity(1576 |          |
|-------------|----------|
| [JPM])      | 0.044764 |
| Equity(2942 |          |
| [UNH])      | 0.031656 |
| Equity(482  |          |
| [CAT])      | 0.021828 |
| Equity(2213 |          |
| [PG])       | 0.020453 |
| Equity(3156 |          |
| [XOM])      | 0.020132 |
| Equity(2204 |          |
| [PFE])      | 0.019069 |
| Equity(3056 |          |
| [WBA])      | 0.018613 |
| Equity(2975 |          |
| [UTX])      | 0.010518 |
| Equity(3045 |          |
| [VZ])       | 0.006263 |

*Table 8.1 Ranking Table*

In this example, we applied a very simple percentage return function on our data. This is meant to demonstrate the principle, and

later on we are going to use this the same logic to perform more complex and more useful calculations.

Remember our stated rules; that we are to buy the top 10 performing stocks. Well, that should be easy at this point. Just slice the data, with the usual syntax of object[start:stop:step ] . In this case as below. Note that we don't have to explicitly state the zero in front of the colon, nor do we have to specify step if we are fine with leaving it at the default value of 1.

```
buy_list = perf_table[:context.stocks_to_hold]
```

Now we know which stocks to hold and which not to hold. All we have to do now is to go over the stocks in the buy list and set their target weight to 10%, and to set the target weight of the rest to 0%.

That's the entire model code. That's all we need to get the performance data we need, and in the next section we will look at how to analyze it.

# **Analyzing Performance with PyFolio**

Creating a **PyFolio** analysis of the results requires surprisingly little code. In fact, it was already added to the code of the sample model in the previous section. It's so little code required that you might not even have noticed that I already put it in there.

The entire code to get a **PyFolio** report consist of importing the library, extracting the relevant data, and requesting a report. Three lines. We do need to have the **PyFolio** library itself installed in our zip3 5 environment of course, as explained earlier in this chapter.

First up, we need to import the library in this particular piece of code. As usual, we do that at the beginning of the code, as you have seen many times by now.

Now we just need wait for the backtest to complete, and for the analyz e function to kick in. You have seen in previous examples how this function is automatically run after a backtest, if it was specified in run\_algorith m part.

Lucky for us, the **PyFolio** library is built to be used with Zipline. It can actually be used with other backtesting engines as well, but it's particularly easy to use with Zipline.

The second line of code needed for a **PyFolio** report is about extracting the information that we need from the backtest results. Specifically the returns, positions and transactions, using a **PyFolio** utility made for that purpose.

```
returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(perf)
```

In that code above, you see another handy feature of Python. A function can return more than one variable, which is not the case with most other common languages.

```
def analyze(context, perf):
```

returns, positions, transactions = pf.utils.extract\_rets\_pos\_txn\_from\_zipline(perf) pf.create\_returns\_tear\_sheet(returns, benchmark\_rets=None)

**PyFolio** has various types of built in tear sheets, meant to show certain aspects of the results. Go ahead and explore the various features included on your own, but for now we will use the returns tear sheet.

I'll save you the hassle of going back to check the code of the complete model, and give it to you here again.

# Import a few libraries we need from zipline import run\_algorithm from zipline.api import order\_target\_percent, symbol, \ schedule\_function, date\_rules, time\_rules from datetime import datetime import pytz import pyfolio as pf

def initialize(context): # Which stocks to trade

| dji | =<br>[  |  |  |
|-----|---------|--|--|
|     | "AAPL", |  |  |
|     | "AXP",  |  |  |
|     | "BA",   |  |  |
|     | "CAT",  |  |  |
|     | "CSCO", |  |  |
|     | "CVX",  |  |  |
|     | "DIS",  |  |  |
|     | "DWDP", |  |  |
|     | "GS",   |  |  |
|     | "HD",   |  |  |
|     | "IBM",  |  |  |
|     | "INTC", |  |  |
|     | "JNJ",  |  |  |
|     | "JPM",  |  |  |
|     | "KO",   |  |  |
|     | "MCD",  |  |  |
|     | "MMM",  |  |  |
|     | "MRK",  |  |  |
|     | "MSFT", |  |  |
|     | "NKE",  |  |  |
|     | "PFE",  |  |  |
|     | "PG",   |  |  |
|     | "TRV",  |  |  |
|     | "UNH",  |  |  |
|     | "UTX",  |  |  |
|     | "V",    |  |  |
|     | "VZ",   |  |  |
|     | "WBA",  |  |  |
|     | "WMT",  |  |  |
|     | "XOM",  |  |  |
| ]   |         |  |  |

# Make symbol list from tickers context.universe = [symbol(s) for s in dji]

# History window context.history\_window = 20

# Size of our portfolio context.stocks\_to\_hold = 10

# Schedule the daily trading routine for once per month schedule\_function(handle\_data, date\_rules.month\_start(), time\_rules.market\_close())

```
def month_perf(ts):
```

perf = (ts[-1] / ts[0]) - 1 return perf

def handle\_data(context, data): # Get history for all the stocks. hist = data.history(context.universe, "close", context.history\_window, "1d")

# This creates a table of percent returns, in order. perf\_table = hist.apply(month\_perf).sort\_values(ascending=False)

# Make buy list of the top N stocks buy\_list = perf\_table[:context.stocks\_to\_hold]

# The rest will not be held. the\_rest = perf\_table[context.stocks\_to\_hold:]

# Place target buy orders for top N stocks. for stock, perf in buy\_list.iteritems(): stock\_weight = 1 / context.stocks\_to\_hold

# Place order if data.can\_trade(stock): order\_target\_percent(stock, stock\_weight)

# Make sure we are flat the rest. for stock, perf in the\_rest.iteritems(): # Place order if data.can\_trade(stock): order\_target\_percent(stock, 0.0)

def analyze(context, perf): # Use PyFolio to generate a performance report returns, positions, transactions = pf.utils.extract\_rets\_pos\_txn\_from\_zipline(perf) pf.create\_returns\_tear\_sheet(returns, benchmark\_rets=None)

# Set start and end date start = datetime(2003, 1, 1, tzinfo=pytz.UTC) end = datetime(2017, 12, 31, tzinfo=pytz.UTC)

# Fire off the backtest result = run\_algorithm(start=start, end=end, initialize=initialize, analyze=analyze, capital\_base=10000,

When you execute this Python backtest in **Jupyter Notebook** , you should get quite a nice display of information coming back to you. It should first show you some overview information and statistics, and then some useful graphs.

| Annual<br>return             | 9.60%   |
|------------------------------|---------|
| Cumulative<br>returns        | 295.20% |
| Annual<br>volatility         | 18.20%  |
| Sharpe<br>ratio              | 0.6     |
| Calmar<br>ratio              | 0.17    |
| Stability                    | 0.78    |
| Max<br>drawdown              | -58.20% |
| Omega<br>ratio               | 1.12    |
| Sortino<br>ratio             | 0.86    |
| Skew                         | 0.19    |
| Kurtosis                     | 10.14   |
| Tail<br>ratio                | 0.97    |
| Daily<br>value<br>at<br>risk | -2.20%  |

| Table | 8.2<br>PyFolio | Key | Ratios |
|-------|----------------|-----|--------|
|-------|----------------|-----|--------|

If you are not familiar with all the analytics in Table 8.2, you may want to read up a little about them. It could very well be that some of them are not overly interesting to you and your approach to the markets but it does not hurt to know more about such things.

For a quick overview of a strategy's performance, there are a few that you probably want to look at right away. The annualized return is the first thing most people would look at, though it tells only a small part of the story. High returns are generally better than low returns, but return alone is a useless number without context.

The annualized volatility as well as Sharpe ratio and maximum drawdown helps to put the annualized return figure into some context. These figures take volatility and downside risk into account.

What you should be looking for here are good numbers, but more importantly realistic numbers. All too often, I see how retail

traders aim for fantasy numbers only to crash and burn when reality comes knocking. If your backtest numbers look too good to be true, they almost certainly are not true.

In real life, you are unlikely to compound over 15% per year over any longer period of time. You are unlikely to achieve a Sharpe ratio of over 1 and you will probably see a maximum drawdown of three times your long term annualized return. These are very broad guidelines of course. Perhaps you can do a little better, perhaps not.

But if your backtest shows you annualized returns of 50%, with a maximum drawdown of 5% and a Sharpe ratio of 10, you have a problem with the backtest. Those are not achievable numbers in the real world.

The key ratios are only the first part of this return tear sheet. Next we find a drawdown table, which shows the top five drawdown periods, their percent loss, dates and recovery time, as shown here in Table 8.3. Again, this is displayed in my local date format, yyyy-mm-d d , and would probably look different on your own screen.

| Worst<br>drawdown<br>periods | Net<br>drawdown<br>in<br>% | Peak<br>date   | Valley<br>date | Recovery<br>date | Duration |
|------------------------------|----------------------------|----------------|----------------|------------------|----------|
| 0                            | 58.17                      | 2007-10-<br>31 | 2009-03-<br>09 | 2013-03-22       | 1408     |
| 1                            | 12.98                      | 2015-07-<br>16 | 2015-08-<br>25 | 2016-03-11       | 172      |
| 2                            | 11.09                      | 2004-03-<br>05 | 2004-08-<br>06 | 2004-10-06       | 154      |
| 3                            | 10.16                      | 2007-07-<br>19 | 2007-08-<br>16 | 2007-10-29       | 73       |
| 4                            | 10.00                      | 2003-01-<br>06 | 2003-03-<br>11 | 2003-03-21       | 55       |

*Table 8.3 PyFolio Drawdown Periods*

The returns tear sheet also outputs quite a few graphs, designed to give you an overview of how the strategy behaves over time. A few of these graphs are shown below, to give you an idea of what this library will auto generate for you, and to let you see how this

*Figure 8*‑*1 Pyfolio Cumulative Returns*

momentum strategy on the Dow performed.

![](_page_13_Figure_2.jpeg)

![](_page_14_Figure_0.jpeg)

*Figure 8*‑*4 PyFolio Monthly and Yearly Returns*

As you see, the **PyFolio** library can generate a standard report which for many readers is probably all you need most of the time. A few lines of code, and you will get this report automatically. This should save you quite a bit of time.

# **Custom Analysis**

You could also get all sorts of custom analysis. This is after all the beauty of Python, and the Pandas library. It makes it very simple to extract, manipulate and analyze time series data.

If you look back again at the code for the sample model that we are using for analysis here, you'll see that in the final row we store the results in a variable which we called simply resul t . Take a quick look at what this variable actually stores. This variable, resul t , is actually a **Pandas DataFrame** , and that greatly simplifies analysis. You can see that row again just here below.

# Fire off the backtest result = run\_algorithm( start=start, end=end, initialize=initialize, analyze=analyze, capital\_base=10000, data\_frequency = 'daily', bundle='quandl' )

> Assuming you just ran the model above in **Jupyter Notebook** , you can now continue to analyze simply by making a new cell below. Click the plus sign in the toolbar, and you get a new cell where you can write code, below the previous one.

> You can run each cell separately and they can access the variables created in the previous cell. This way, you don't have to rerun the backtest, but can go right on to analyzing the result of the test you already did.

> First you might want to check what kind of columns this **DataFrame** has. This can be done with this simple code.

for column in result: print(column)

That will print out the names of all the columns you have in the

**DataFrame** , and your output will looks something like this.

algo\_volatility algorithm\_period\_return alpha benchmark\_period\_return benchmark\_volatility beta capital\_used ending\_cash ending\_exposure ending\_value excess\_return gross\_leverage long\_exposure long\_value longs\_count max\_drawdown max\_leverage net\_leverage orders period\_close period\_label period\_open pnl portfolio\_value positions returns sharpe short\_exposure short\_value shorts\_count sortino starting\_cash starting\_exposure starting\_value trading\_days transactions treasury\_period\_return

> This will give you some idea of what is there, and how to work with it. But go ahead and go one step further. This **DataFrame** will contain one row for every day of the backtest run. That means that we can pick any individual day and check the state of the backtest on that particular day. We can output the values for an individual day easily, and even if this way of displaying the result is not very helpful for analytics, it does give us a clue to what is possible.

You can use .lo c to locate something inside a **DataFrame** based on simple criteria as shown below, or more complex logic once you get accustomed to it.

#### result.loc['2010-11-17']

That would output the field values, and you should see this kind of result.

| algo_volatility         | 0.218396                                                      |
|-------------------------|---------------------------------------------------------------|
| algorithm_period_return | 0.983227                                                      |
| alpha                   | 2.63224                                                       |
| benchmark_period_return | 1.4927e+08                                                    |
| benchmark_volatility    | 0.0132004                                                     |
| beta                    | -1.05027                                                      |
| capital_used            | 0                                                             |
| ending_cash             | 141.915                                                       |
| ending_exposure         | 19690.4                                                       |
| ending_value            | 19690.4                                                       |
| excess_return           | 0                                                             |
| gross_leverage          | 0.992844                                                      |
| long_exposure           | 19690.4                                                       |
| long_value              | 19690.4                                                       |
| longs_count             | 10                                                            |
| max_drawdown            | -0.443695                                                     |
| max_leverage            | 1.00518                                                       |
| net_leverage            | 0.992844                                                      |
| orders                  | []                                                            |
| period_close            | 2010-11-17<br>21:00:00+00:00                                  |
| period_label            | 2010-11                                                       |
| period_open             | 2010-11-17<br>14:31:00+00:00                                  |
| pnl                     | -96.598                                                       |
| portfolio_value         | 19832.3                                                       |
| positions               | [{'sid':<br>Equity(290<br>[AXP]),<br>'amount':<br>48,<br>'las |
| returns                 | -0.00484714                                                   |
| sharpe                  | 0.50684                                                       |
| short_exposure          | 0                                                             |
| short_value             | 0                                                             |
| shorts_count            | 0                                                             |
| sortino                 | 0.743699                                                      |
| starting_cash           | 141.915                                                       |
| starting_exposure       | 19786.9                                                       |
| starting_value          | 19786.9                                                       |
| trading_days            | 1985                                                          |
| transactions            | []                                                            |
| treasury_period_return  | 0                                                             |
| Name:<br>2010-11-17     | 00:00:00+00:00,<br>dtype:<br>object                           |

# **Day Snapshot**

Looking at just an equity curve, the portfolio value development over the course of the backtest, can often create more questions than it answers. You may see some strange moves up or down, and now you wonder what could have caused this. The equity curve won't tell you, but you can always inspect the details of the days in question. That's usually a good way to check if the model is behaving the way it should, if it's trading the way you would expect, and holding the kind of positions you would expect.

Make a new cell in the Notebook below the previous one and try the following code.

# Let's get a portfolio snapshot

# Import pandas and matplotlib import pandas as pd import matplotlib.pyplot as plt

# Select day to view day = '2009-03-17'

# Get portfolio value and positions for this day port\_value = result.loc[day,'portfolio\_value'] day\_positions = result.loc[day,'positions']

# Empty DataFrame to store values df = pd.DataFrame(columns=['value', 'pnl'])

# Populate DataFrame with position info for pos in day\_positions: ticker = pos['sid'].symbol df.loc[ticker,'value'] = pos['amount'] \* pos['last\_sale\_price'] df.loc[ticker,'pnl'] = df.loc[ticker,'value'] - (pos['amount'] \* pos['cost\_basis'])

# Add cash position df.loc['cash', ['value','pnl']] = [(port\_value - df['value'].sum()), 0]

# Make pie chart for allocations fig, ax1 = plt.subplots(figsize=[12, 10]) ax1.pie(df['value'], labels=df.index, shadow=True, startangle=90) ax1.axis('equal') ax1.set\_title('Allocation on {}'.format(day))

plt.show()

# Make bar chart for open PnL fig, ax1 = plt.subplots(figsize=[12, 10]) pnl\_df = df.drop('cash') ax1.barh( pnl\_df.index, pnl\_df['pnl'], align='center', color='green', ecolor='black') ax1.set\_title('Open PnL on {}'.format(day)) plt.show()

Here we pick a date at the top, where we want to see the current allocation and open position profit and loss. At first, we use the helpful .loc to locate the matching date. With this tool, we can find a specific column value for a specific row, with this syntax .loc[row, column ] . Note that this simple code has no error handling yet, in case you pick a date that's not part of the result object, such as a weekend.

Based on the row that matches the date we gave, we can now find the info needed to make some graphs. As you saw earlier, there is a row in the result object which holds a list of positions. What this code does it to iterate through those positions and make a **DataFrame** with the value and the open profit and loss. This could be done more elegantly, but this book is about clarity and not elegance.

For an allocation pie chart to make sense, we also need to add any cash position. We are dealing with equities here, so the cash holdings would simply be the total portfolio value minus the value of the stocks we hold. After we have added this, we can draw a nice pie using the **MatPlotLib** , just as we have done earlier in this book.

Making a horizontal bar graph for the open profit and loss per position is just as easy, and that's what the last section of the code sample does.

This is just meant to demonstrate the relative ease of zooming in on a particular day and getting a feel for how the portfolio looked at that time.

![](_page_20_Figure_0.jpeg)

*Figure 8-5 Day Snapshot Allocation* 

![](_page_21_Figure_0.jpeg)

Figure 8‑6 Day Snapshot Open Profit and Loss

#### **Custom Time Series Analytics**

Time series analytics is where Python really shines. The only thing stopping you here is your own creativity. The more you work with backtesting the more you will find yourself wondering about various aspects of the return curves that comes out on the other end.

To give you an idea of how quickly and easily you can calculate various analytics, I will show an example here. We are going to make a graph with four sub plots. The first will show a semi-log graph of the equity curve itself. The second will show the exposure held over time. So far, those are time series that we already have. But

the next two we need to calculate.

The third plot will show half a year rolling returns, on an annualized basis. I have chosen this analytic because it makes for a good learning exercise. That means that we need to stop a moment to think about what this is.

We all know, or least we should all know, what annualized return refers to. Normally, you would probably look at the annualized return over the course of the entire backtest. You may at times see the term Compound Annual Growth Rate, or CAGR, which is the same thing.

If for instance, you started out with \$10,000 and managed to achieve an annualized return of 10% for ten years, you would end up with \$25,937.

Or to turn it around, if you started out with \$10,000 and ended up with \$25,937 after ten years, you could easily find the annualized rate of return.

$$\left(\frac{25,937}{10,000}\right)^{1/10} - 1 = 10\%$$

But such a number may move up and down a lot during a backtest, and it can be useful to see what the annualized return would have been on a shorter time frame, on a rolling basis.

This is very basic financial math and very simple when you are dealing in full years. It can be a very useful tool to be able to calculate annualized numbers on shorter or longer time periods than a full year, and that's a more realistic scenario. In the real world, you will almost always be dealing with such time series.

Let me therefore give you a more generic formula for dealing with this. I will give you the formula first, and then you will see in the code below how easily we apply this math to a Python series.

Using this simple math, you can quickly find the annualized return, whether time period in question is longer or shorter than a year. Now look at how we can make a generic function to calculate this.

```
def ann_ret(ts):
  return np.power((ts[-1] / ts[0]), (year_length/len(ts))) -1
```

In this function, we feed in a time series, and get an annualized return rate back. The only thing we need to define is just how many days we are assuming in a full year. As you will see in my code, I tend to assume 252 trading days, which is pretty close to most years' actual days. Some prefer 256 days, as it makes can calculations easier.

The reason that I'm defining a separate function for this is that it makes it so much simpler to apply it to a rolling time window, as we will soon see in the code.

For the same reason, I'm making a function to calculate the maximum drawdown on a time window as well.

def dd(ts):

return np.min(ts / np.maximum.accumulate(ts)) - 1

Here we provide a time series window, and get back the value for the deepest drawdown during this period.

The rest of the code is mostly about formatting a nice looking graph. I will assume here that you are working in **Jupyter** , and that you have just run the model in the previous section. Any model will do, actually. Now make a new cell just below, where we will write the new code.

As always, you can find this code as well at the book website, **[www.followingthetrend.com/trading-evolved/](http://www.followingthetrend.com/python-book/)** .

Here is the code we need to calculate the mentioned analytics.

```
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
# Format for book image
font = {'family' : 'eurostile',
     'weight' : 'normal',
     'size' : 16}
matplotlib.rc('font', **font)
# Settings
window = 126
year_length = 252
# Copy the columsn we need
df = result.copy().filter(items=['portfolio_value', 'gross_leverage'])
# Function for annualized return
def ann_ret(ts):
  return np.power((ts[-1] / ts[0]), (year_length/len(ts))) -1
# Function for drawdown
def dd(ts):
  return np.min(ts / np.maximum.accumulate(ts)) - 1
# Get a rolling window
rolling_window = result.portfolio_value.rolling(window)
# Calculate rolling analytics
df['annualized'] = rolling_window.apply(ann_ret)
df['drawdown'] = rolling_window.apply(dd)
# Drop initial n/a values
```

df.dropna(inplace=True)

After the required import statements, you see some odd looking rows about font. I have included this just to show you how I formatted the graphs to be displayed in this book. You can safely skip this if you like, it's just left there in case you are curious about fond and size formatting.

```
# Format for book image
font = {'family' : 'eurostile',
     'weight' : 'normal',
     'size' : 16}
rc('font', **font)
```

Then there are two settings. The window setting defines what

length of rolling time window we want to analyze. The number in the code, 126 days, represents approximately half a year. Change it to anything you like.

The second setting is for how many business days a year we are assuming, and this should be approximately 252 days.

# Settings calc\_window = 126 year\_length = 252

> Then we construct a **DataFrame** , simply by copying the only two columns that we need from the **DataFrame** that was created by the backtest earlier. Remember that we made a simple backtest earlier in this chapter, which returned a variable called resul t . We have no need for most of what is in this variable, so we just copy portfolio\_valu e and gross\_leverag e into a new **DataFrame** .

```
# Copy the columsn we need
df = result.copy().filter(items=['portfolio_value', 'gross_leverage'])
```

You will find two functions in the code, one to calculate annualized return and one to calculate drawdown.

```
# Function for annualized return
def ann_ret(ts):
  return np.power((ts[-1] / ts[0]), (year_length/len(ts))) -1
# Function for drawdown
```

```
def dd(ts):
  return np.min(ts / np.maximum.accumulate(ts)) - 1
```

Follow the code down a bit from there, and you see how we are defining a rolling time window of data, and using the same apply logic as we have seen previously to get rolling time series of both analytics.

```
# Get a rolling window
rolling_window = result.portfolio_value.rolling(calc_window)
```

# Calculate rolling analytics df['annualized'] = rolling\_window.apply(ann\_ret) df['drawdown'] = rolling\_window.apply(dd)

Now we have a **DataFrame** with everything calculated for us,

and all we need to do is to visualize it.

```
# Make a figure
fig = plt.figure(figsize=(12, 12))
# Make the base lower, just to make the graph easier to read
df['portfolio_value'] /= 100
# First chart
ax = fig.add_subplot(411)
ax.set_title('Strategy Results')
ax.plot(df['portfolio_value'],
     linestyle='-',
     color='black',
     label='Equity Curve', linewidth=3.0)
# Set log scale
ax.set_yscale('log')
# Make the axis look nicer
ax.yaxis.set_ticks(np.arange(df['portfolio_value'].min(), df['portfolio_value'].max(), 500 ))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
# Add legend and grid
ax.legend()
ax.grid(False)
# Second chart
ax = fig.add_subplot(412)
ax.plot(df['gross_leverage'],
     label='Strategy exposure'.format(window),
     linestyle='-',
     color='black',
     linewidth=1.0)
# Make the axis look nicer
ax.yaxis.set_ticks(np.arange(df['gross_leverage'].min(), df['gross_leverage'].max(), 0.02 ))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))
# Add legend and grid
ax.legend()
ax.grid(True)
# Third chart
ax = fig.add_subplot(413)
ax.plot(df['annualized'],
     label='{} days annualized return'.format(window),
     linestyle='-',
     color='black',
     linewidth=1.0)
```

# Make the axis look nicer ax.yaxis.set\_ticks(np.arange(df['annualized'].min(), df['annualized'].max(), 0.5 )) ax.yaxis.set\_major\_formatter(ticker.FormatStrFormatter('%0.1f'))

```
# Add legend and grid
ax.legend()
ax.grid(True)
```

```
# Fourth chart
ax = fig.add_subplot(414)
ax.plot(df['drawdown'],
     label='{} days max drawdown'.format(window),
     linestyle='-',
     color='black',
     linewidth=1.0)
```

```
# Make the axis look nicer
ax.yaxis.set_ticks(np.arange(df['drawdown'].min(), df['drawdown'].max(), 0.1 ))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
```

# Add legend and grid ax.legend() ax.grid(True)

> The output of this should be four graphs, similar to what you see in Figure 8‑7. As you start getting comfortable with constructing backtesting models in Python, you will probably find yourself creating all kinds of custom analytics and graphs to visualize what is important to you, to locate issues or learn more about the behavior of the models you have built.

![](_page_28_Figure_0.jpeg)
## **Performance Visualization and Combinations**

In the previous sections you have seen various tables and graphs, showing the performance of backtests. This being a fully transparent book and all, I will show you just how those visualizations were made. These are really simple things to get done in Python. All we need is a time series to work with, and we can build all kinds of graphs, analytics, tables and other outputs.

## **Storing Model Results**

In chapter 8 we looked at some ways of extracting results from a Zipline backtest and constructing some analytics and charts based on that. The same principles apply here, but the difference is that it would be helpful to store the backtests for further analysis later on.

As you have seen by now, when we run a Zipline backtest we get the results returned to us. In the sample models earlier in this book, this tends to look something like this.

```
perf = zipline.run_algorithm(
  start=start, end=end,
  initialize=initialize,
  analyze=analyze,
  capital_base=millions_traded * 1000000,
  data_frequency = 'daily',
  bundle='futures' )
```

In this case, after the backtest run is completed, the variable per f will hold all the results. This is a **DataFrame** , consisting of quite a lot of different data which was collected or calculated during the run. If you are looking to store just the portfolio value for each day in the backtest, you can do that very easily. This is stored in the column

portfolio\_valu e and that means that we can simply save it as a comma separated file in this one row of code.

```
perf.portfolio_value.to_csv('model_performance.csv')
```

That's all that it takes, and that one line will save the portfolio value, often called the equity curve, of the backtest to a file with the specified name. If you are looking to analyze other aspects of the backtests, you can save the trades done and any other data you will find in per f .

This trick, saving a **DataFrame** to a comma separated file, can be very useful in many instances. Another somewhat related tool that may be particularly helpful at times during debugging, is .to\_clipboard( ) . Instead of saving to disk, this will place the **DataFrame** in memory, in the clipboard. It will be in the correct format so that you can paste it straight into Excel, if that's your intention. Being able to quickly copy something out to Excel for visual inspection can be quite helpful when debugging.

## **How the Model Performance Analysis was done**

To calculate and visualize the performance analytics for each of the model chapters, I started off with a Jupyter Notebook. As discussed earlier in the book, it makes sense to separate different pieces of logic into different cells in the Notebook. Lower cells can access data that you fetched or calculated in the higher level ones.

After running the backtests, I saved the historical portfolio value to a local CSV file. The performance analysis notebook then reads one of these CSV files, as well as the benchmark data for the S&P 500 Total Return Index for comparison. This is what the first cell of my notebook does.

```
import matplotlib.pyplot as plt
import pandas as pd
# Where the data is
path = 'data/'
# Set benchmark to compare with
bm = 'SPXTR'
bm_name = 'S&P 500 Total Return'
# These are the saved performance csv files from our book models.
strat_names = {
  "trend_model" : "Core Trend Strategy",
  "time_return" : "Time Return Strategy",
  "counter_trend" : "Counter Trend Strategy",
  "curve_trading" : "Curve Trading Strategy",
  "systematic_momentum" : "Equity Momentum Strategy",
}
# Pick one to analyze
strat = 'curve_trading'
# Look up the name
strat_name = strat_names[strat]
# Read the strategy
df = pd.read_csv(path + strat + '.csv', index_col=0, parse_dates=True, names=[strat] )
# Read the benchmark
df[bm_name] = pd.read_csv(bm + '.csv', index_col=0, parse_dates=[0] )
# Limit history to end of 2018 for the book
df = df.loc[:'2018-12-31']
# Print confirmation that all's done
print("Fetched: {}".format(strat_name))
```

After that is done, we have the data that we need in a neatly organized **DataFrame** . The next thing I wanted to do was to make a nice looking table of monthly returns. The Python code for aggregating performance on monthly, as well as yearly frequencies does not take much work. As so often is the case, someone else has already written code for this, and there is no need to reinvent the wheel. In this case, I will use the library **Empyrical** , as that should already be installed on your computer if you followed previous chapters. It comes bundled with the **PyFolio** library that we used earlier in chapter 8.

Therefore, calculating monthly and yearly returns takes only one line of code each. The rest of the following cell is about constructing a neat formatted table. For that, I settled on using good old HTML, just to make sure it looks the way I want to for this book. If you simply want to dump the monthly values in text, most of the next cell is redundant. Most of the following code is just about formatting an HTML table for pretty display.

```
# Used for performance calculations
import empyrical as em
# Used for displaying HTML formatted content in notebook
from IPython.core.display import display, HTML
# Use Empyrical to aggregate on monthly and yearly periods
monthly_data = em.aggregate_returns(df[strat].pct_change(),'monthly')
yearly_data = em.aggregate_returns(df[strat].pct_change(),'yearly')
# Start off an HTML table for display
table = """
<table id='monthlyTable' class='table table-hover table-condensed table-striped'>
<thead>
<tr>
<th style="text-align:right">Year</th>
<th style="text-align:right">Jan</th>
<th style="text-align:right">Feb</th>
<th style="text-align:right">Mar</th>
<th style="text-align:right">Apr</th>
<th style="text-align:right">May</th>
<th style="text-align:right">Jun</th>
<th style="text-align:right">Jul</th>
<th style="text-align:right">Aug</th>
<th style="text-align:right">Sep</th>
<th style="text-align:right">Oct</th>
<th style="text-align:right">Nov</th>
<th style="text-align:right">Dec</th>
<th style="text-align:right">Year</th>
</tr>
</thead>
<tbody>
<tr>"""
first_year = True
first_month = True
yr = 0
```

mnth = 0

```
# Look month by month and add to the HTML table
for m, val in monthly_data.iteritems():
  yr = m[0]
  mnth = m[1]
  # If first month of year, add year label to table.
  if(first_month):
     table += "<td align='right'><b>{}</b></td>\n".format(yr)
     first_month = False
  # pad empty months for first year if sim doesn't start in January
  if(first_year):
     first_year = False
     if(mnth > 1):
       for i in range(1, mnth):
          table += "<td align='right'>-</td>\n"
  # Add the monthly performance
  table += "<td align='right'>{:+.1f}</td>\n".format(val * 100)
  # Check for December, add yearly number
  if(mnth==12):
```

```
table += "<td align='right'><b>{:+.1f}</b></td>\n".format(yearly_data[yr] * 100)
table += '</tr>\n <tr> \n'
first_month = True
```

```
# add padding for empty months and last year's value
if(mnth != 12):
  for i in range(mnth+1, 13):
     table += "<td align='right'>-</td>\n"
     if(i==12):
       table += "<td align='right'><b>{:+.1f}</b></td>\n".format(
          yearly_data[yr] * 100
       )
       table += '</tr>\n <tr> \n'
```

# Finalize table table += '</tr>\n </tbody> \n </table>'

# And display it. display(HTML(table))

> That should output a table looking just like the ones you have seen a few times in this book, for each of the strategy analysis chapters. Next there is the performance chart. In the earlier sections, I used a logarithmic chart to compare each strategy to the equity index.

It may not make much sense to compare your strategy to the S&P 500, but it's highly likely that others will compare you to it, whether it's logical or not.

In the same chart image, I also had a drawdown plot as well as a 6 months rolling correlation. These are very easy to calculate, and you should already know how to make the graphs. There is also some code in there to make the next really big and to get the lines to be black and grey for the book.

```
import matplotlib
# Assumed trading days in a year
yr_periods = 252
# Format for book display
font = {'family' : 'eurostile',
     'weight' : 'normal',
     'size' : 16}
matplotlib.rc('font', **font)
# Rebase to first row with a single line of code
df = df / df.iloc[0]
# Calculate correlation
df['Correlation'] = df[strat].pct_change().rolling(window=int(yr_periods /
2)).corr(df[bm_name].pct_change())
# Calculate cumulative drawdown
df['Drawdown'] = (df[strat] / df[strat].cummax()) - 1
# Make sure no NA values are in there
df.fillna(0, inplace=True)
# Start a plot figure
fig = plt.figure(figsize=(15, 12))
# First chart
ax = fig.add_subplot(311)
ax.set_title('Strategy Comparisons')
ax.semilogy(df[strat], '-',label=strat_name, color='black')
ax.semilogy(df[bm_name] , '--', color='grey')
ax.legend()
# Second chart
```

ax = fig.add\_subplot(312)

ax.fill\_between(df.index, df['Drawdown'], label='Drawdown', color='black') ax.legend()

```
# Third chart
ax = fig.add_subplot(313)
ax.fill_between(df.index,df['Correlation'], label='6M Rolling Correlation', color='grey')
ax.legend()
```

Finally, for each chapter I did a so called holding period table, that shows your percentage return if you started it in January of a given year, and held for a certain number of full years. Again I elected to use HTML output to ensure that it can be displayed nicely for this book. Since the width of these pages is limited, I also rounded the numbers down to full percent.

```
def holding_period_map(df):
  # Aggregate yearly returns
  yr = em.aggregate_returns(df[strat].pct_change(), 'yearly')
  yr_start = 0
  #Start off table
  table = "<table class='table table-hover table-condensed table-striped'>"
  table += "<tr><th>Years</th>"
```

```
# Build the first row of the table
for i in range(len(yr)):
  table += "<th>{}</th>".format(i+1)
table += "</tr>"
```

```
# Iterate years
for the_year, value in yr.iteritems():
  # New table row
  table += "<tr><th>{}</th>".format(the_year)
```

```
# Iterate years held
  for yrs_held in (range(1, len(yr)+1)): # Iterates yrs held
     if yrs_held <= len(yr[yr_start:yr_start + yrs_held]):
       ret = em.annual_return(yr[yr_start:yr_start + yrs_held], 'yearly' )
       table += "<td>{:+.0f}</td>".format(ret * 100)
  table += "</tr>"
  yr_start+=1
return table
```

## **How the Combined Portfolio Analysis was done**

In chapter 19 we looked at the diversification benefits of combining models and trading portfolios of models. The method used in that chapter was to rebalance at the start of every month, resetting the weight of each strategy at that interval. In the code shown here, I will also give you another method of rebalancing. As you will see in the next code segment, you can also trigger the rebalance on percentage divergence, if the market developments have pushed any strategy to be more than a certain percent off.

This is a somewhat advanced topic, and really goes beyond what I was planning to show in this book. I include this source code here anyhow, in the interest of being transparent. I will however avoid the potentially lengthy discussion of how this code is constructed and the reason for it. It uses some tricks to enhance performance, making use of **Numpy** to speed things up.

Once you feel comfortable with Python and backtesting, this is a topic you may want to dig deeper into. How to use optimize complex operations and speed code up. But it's out of scope for this book.

```
import pandas as pd
import numpy as np
base_path = '../Backtests/'
# Rebalance on percent divergence
class PercentRebalance(object):
  def __init__(self, percent_target):
     self.rebalance_count = 0
     self.percent_target = percent_target
```

```
def rebalance(self, row, weights, date):
```

```
total = row.sum()
     rebalanced = row
     rebalanced = np.multiply(total, weights)
     if np.any(np.abs((row-rebalanced)/rebalanced) > (self.percent_target/100.0)):
       self.rebalance_count = self.rebalance_count + 1
       return rebalanced
     else:
       return row
# Rebalance on calendar
class MonthRebalance(object):
  def __init__(self, months):
     self.month_to_rebalance = months
     self.rebalance_count = 0
     self.last_rebalance_month = 0
  def rebalance(self, row, weights, date):
     current_month = date.month
     if self.last_rebalance_month != current_month:
       total = row.sum()
       rebalanced = np.multiply(weights, total)
       self.rebalance_count = self.rebalance_count + 1
       self.last_rebalance_month = date.month
       return rebalanced
     else:
       return row
# Calculate the rebalanced combination
def calc_rebalanced_returns(returns, rebalancer, weights):
  returns = returns.copy() + 1
  # create a numpy ndarray to hold the cumulative returns
  cumulative = np.zeros(returns.shape)
  cumulative[0] = np.array(weights)
  # also convert returns to an ndarray for faster access
  rets = returns.values
  # using ndarrays all of the multiplicaion is now handled by numpy
  for i in range(1, len(cumulative) ):
     np.multiply(cumulative[i-1], rets[i], out=cumulative[i])
     cumulative[i] = rebalancer.rebalance(cumulative[i], weights, returns.index[i])
```

```
# convert the cumulative returns back into a dataframe
cumulativeDF = pd.DataFrame(cumulative, index=returns.index, columns=returns.columns)
```

# finding out how many times rebalancing happens is an interesting exercise print ("Rebalanced {} times".format(rebalancer.rebalance\_count))

# turn the cumulative values back into daily returns

```
rr = cumulativeDF.pct_change() + 1
  rebalanced_return = rr.dot(weights) - 1
  return rebalanced_return
def get_strat(strat):
  df = pd.read_csv(base_path + strat + '.csv', index_col=0, parse_dates=True, names=[strat] )
  return df
# Use monthly rebalancer, one month interval
rebalancer = MonthRebalance(1)
# Define strategies and weights
portfolio = {
  'trend_model': 0.2,
  'counter_trend': 0.2,
  'curve_trading': 0.2,
  'time_return': 0.2,
  'systematic_momentum' : 0.2,
}
# Read all the files into one DataFrame
df = pd.concat(
     [
       pd.read_csv('{}{}.csv'.format(
               base_path,
               strat
               ),
               index_col=0,
               parse_dates=True,
               names=[strat]
              ).pct_change().dropna()
       for strat in list(portfolio.keys())
     ], axis=1
)
# Calculate the combined portfolio
df['Combined'] = calc_rebalanced_returns(
  df,
  rebalancer,
  weights=list(portfolio.values())
  )
df.dropna(inplace=True)
# Make Graph
import matplotlib
import matplotlib.pyplot as plt
include_combined = True
include_benchmark = True
benchmark = 'SPXTR'
```

```
if include_benchmark:
  returns[benchmark] = get_strat(benchmark).pct_change()
#returns = returns['2003-1-1':]
normalized = (returns+1).cumprod()
font = {'family' : 'eurostile',
     'weight' : 'normal',
     'size' : 16}
matplotlib.rc('font', **font)
fig = plt.figure(figsize=(15, 8))
# First chart
ax = fig.add_subplot(111)
ax.set_title('Strategy Comparisons')
dashstyles = ['-','--','-.','.-.', '-']
i = 0
for strat in normalized:
  if strat == 'Combined':
     if not include_combined:
       continue
     clr = 'black'
     dash = '-'
     width = 5
  elif strat == benchmark:
     if not include_benchmark:
       continue
     clr = 'black'
     dash = '-'
     width = 2
  #elif strat == 'equity_momentum':
  # continue
  else:
     clr = 'grey'
     dash = dashstyles[i]
     width = i + 1
     i += 1
  ax.semilogy(normalized[strat], dash, label=strat, color=clr, linewidth=width)
```

ax.legend()
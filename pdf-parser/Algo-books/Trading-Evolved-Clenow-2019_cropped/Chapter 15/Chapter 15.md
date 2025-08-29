## **Time Return Trend Model**

The time return trend model is probably the simplest trend model you will ever see. It may be the simplest trading model of any kind that you will encounter. At least if you only count reasonably well performing models. There is nothing wrong with the results from this model. It's not the most practical model to trade, but the returns have been nothing short of stellar, given how simple the rules really are. And of course, I'm about to give you all the source code.

The aim of this model is to capture long term trends while avoiding common problem of early stop out. All too often, classic trend following models suffer from taking their stops too early on short term pullbacks, only to see prices return back to the trend again. While these classic trend models tend to show strong long term performance despite this issue, the time return trend model is not susceptible to the problem at all.

The rules are so simple that it's easy to dismiss this model at first glance. I would urge you to take it seriously though. There is plenty to be learned from understanding this model.

You should bear in mind from the start that this particular model is not very practical to trade. For most readers, it simply is not possible to trade it. To actually implement this model, you will need a substantial sum of money, a large number of positions would be open at any given time and you would constantly run on a very high margin to equity ratio.

But, this model remains a very valuable learning tool. If you understand the mechanics, you can adapt the model and make it more practical. This version that I will show you is for learning, not for you to go and implement.

#### **Investment Universe**

Just as with the previous model, we will use a very broad investment universe. A model like this is completely dependent on diversification and will not perform well on a small investment universe. If you try rules like this on any given market, or a small number of markets, you'll likely see results ranging from poor to mediocre. The effect comes from trading a broad set of markets, all at once.

For this model, we're going to trade the same set of broad futures markets that we used in the previous model. We're covering equity indexes, commodities, currencies, treasuries and money markets.

## **Trading Frequency**

With this particular model, we only trade once per month. We completely ignore anything that happens during that month. No matter how large the moves, no action is taken during the month. No stop point, no profit targets. Just make your trades at the start of the month and go fishing for a while.

Actually, there is one thing that we need to do between the monthly trade points. As we are dealing with futures here, we do need to check for rolls daily. That is, we need to make sure that we are holding the correct contract, as liquidity shifts from one contract delivery to another. Just like for any futures model, this is something that we won't get away from.

## **Position Allocation**

For this model, we will use the same position allocation logic

as we employed for the previous model. We measure volatility using standard deviation, and set position sizes based on inverse volatility logic. That is, we have a lower face value amount of something more volatile, and vice versa, in an attempt to target an approximate equal volatility, or risk if you will, per position.

To keep the logic simple here, no regular rebalancing of position sizes is done, nor is any more complex volatility targeting technique employed. Both of these make more sense for institutional portfolio management than for individual accounts.

#### **Trading Rules**

As already mentioned, this model trades only once per month. At that time we check only two things.

Is the price higher or lower than a year go?

Is the price higher or lower than half a year ago?

That's all we care about here. For this model, there are no breakout indicators, no moving averages, and no indicators of any kind. It is, quite purposely, an extremely simple trend model.

Note that we do the calculations here based on the continuations, as we did in the previous model, not on individual contracts. That's generally how we need work with futures models, as the individual contracts have such limited time series history.

## **Dynamic Performance Chart**

Since this model is quite simple, this seems like a good place to throw in a new neat little trick to teach you. If you have replicated the models and run the backtests in the previous chapters, you will have noticed by now that it sometimes takes a little while to finish them. I

showed you earlier simple ways to output some text, such as last month's performance during the run. But this is neither pretty, nor very informative.

Wouldn't it be nice if we could get a dynamically updating graph while we wait? A graph showing the ongoing performance of the simulation, as it happens. It's a well-known trick that people are less annoyed with waiting times if there is something to look at or listen to. That's after all why they have mirrors in elevators.

As it turns out, it's not only possible but even quite simple to have a dynamic chart display as you run the backtest. From now on in this book, I will use this way to output results as the backtests are under way.

To set up these dynamic charts in the **Jupyter Notebook** environment, we need to do three simple things.

First, until now we have been using the line %matplotlib inlin e at the top of our code. That tells the charting library, **matplotlib** , to show the graphs in the output as images when they are requested by our code. But using that does not allow for interactive charts.

To be able to get interactive charts, we need to change that line to %matplotlib noteboo k .

Second, we need to add some brief code to make a **DataFrame** for storing the charting data, as well as initializing the chart.

```
# DataFame for storing and updating the data that we want to graph
dynamic_results = pd.DataFrame()
# Init figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_title('Time Return Performance')
```

Now the only thing left is to update the data as we move along in the backtest. To keep it clean, I added a separate scheduled function in this example. Keep in mind that if you are looking for pure speed, using a dynamic graph will slow you down, and the more so the more often you update it.

I added this row to our initializ e function, which will update the graph once a month. If you have really short attention span you could update this daily, but performance will suffer.

schedule\_function(update\_chart, date\_rules.month\_start(), time\_rules.market\_close())

And then this new function to store and update the graph.

def update\_chart(context,data): # This function continuously update the graph during the backtest today = data.current\_session.date() dynamic\_results.loc[today, 'PortfolioValue'] = context.portfolio.portfolio\_value

if ax.lines: # Update existing line ax.lines[0].set\_xdata(dynamic\_results.index) ax.lines[0].set\_ydata(dynamic\_results.PortfolioValue) else: # Create new line ax.semilogy(dynamic\_results)

```
# Update scales min/max
ax.set_ylim(
  dynamic_results.PortfolioValue.min(),
  dynamic_results.PortfolioValue.max()
)
ax.set_xlim(
  dynamic_results.index.min(),
  dynamic_results.index.max()
)
```

# Redraw the graph fig.canvas.draw()

#### **Time Return Source Code**

The code for this model is really quite simple. Even if you don't really know anything about programming, you can still figure it out. Compared to most programming languages, Python is quite easy to read and understand.

As usual, the very top you will find some import statements, telling our code which libraries we intend to use. Then there are a few

parameters defined. Feel free to play around with these. You can change the risk factor, the volatility calculation window, liquidity filter, and trend windows.

You will notice that there are two settings for trend window. One short and one long. One is set to 125 days and the other 250, or approximately half a year and a full year respectively. The rules, as you see, requires positive return over both time periods for a long position, or negative over both for a short position.

In the Initializ e function we can enable or disable cost and slippage. Again, test it out and see how it changes things. It wouldn't make much sense for me to simply tell you. Trust me, you will learn much more if you get this code up and running locally, and see for yourself.

Then, in the same function, the investment universe is defined before we set schedulers to run the rebalancing monthly and the futures roll check daily.

In the monthly rebalancing, we first check if a position is already open or not for each market. If there is no position on, we check if yesterday's price is higher than both a year ago and half a year ago. If so, buy. If it's lower than both those two points in time, go short. And else, hold no position at all.

```
%matplotlib notebook
```

import zipline from zipline.api import future\_symbol, \ set\_commission, set\_slippage, schedule\_function, date\_rules, \ time\_rules, continuous\_future, order\_target from datetime import datetime import pytz import matplotlib.pyplot as plt import matplotlib import pyfolio as pf import pandas as pd import numpy as np from zipline.finance.commission import PerShare, PerTrade, PerContract from zipline.finance.slippage import VolumeShareSlippage, \ FixedSlippage, VolatilityVolumeShare

"""

Model Settings """ starting\_portfolio = 10000000 risk\_factor = 0.0015 vola\_window = 60 short\_trend\_window = 125 long\_trend\_window = 250

"""

Prepare for dynamic chart """ dynamic\_results = pd.DataFrame() fig = plt.figure(figsize=(10, 6))

```
ax = fig.add_subplot(111)
ax.set_title('Time Return Performance')
```

```
def initialize(context):
  """
  Cost Settings
  """
  context.enable_commission = True
  context.enable_slippage = True
```

```
if context.enable_commission:
  comm_model = PerContract(cost=0.85, exchange_fee=1.5)
else:
  comm_model = PerTrade(cost=0.0)
```

set\_commission(us\_futures=comm\_model)

```
if context.enable_slippage:
  slippage_model=VolatilityVolumeShare(volume_limit=0.2)
else:
  slippage_model=FixedSlippage(spread=0.0)
```

set\_slippage(us\_futures=slippage\_model)

currencies = [ 'AD', 'BP', 'CD', 'CU', 'DX', 'JY',

| 'NE',                      |  |
|----------------------------|--|
| 'SF',                      |  |
|                            |  |
| ]                          |  |
| agriculturals<br>=<br>[    |  |
| 'BL',                      |  |
|                            |  |
| 'BO',                      |  |
| '_C',                      |  |
|                            |  |
| 'CC',                      |  |
| 'CT',                      |  |
| 'FC',                      |  |
|                            |  |
| 'KC',                      |  |
| 'LB',                      |  |
| 'LC',                      |  |
|                            |  |
| 'LR',                      |  |
| 'LS',                      |  |
| '_O',                      |  |
|                            |  |
| '_S',                      |  |
| 'SB',                      |  |
| '_W',                      |  |
|                            |  |
| ]                          |  |
| nonagriculturals<br>=<br>[ |  |
|                            |  |
| 'CL',                      |  |
| 'GC',                      |  |
| 'HG',                      |  |
|                            |  |
| 'HO',                      |  |
| 'LG',                      |  |
| 'NG',                      |  |
| 'PA',                      |  |
|                            |  |
| 'PL',                      |  |
| 'RB',                      |  |
| 'SI',                      |  |
|                            |  |
| ]                          |  |
| equities<br>=<br>[         |  |
| 'ES',                      |  |
|                            |  |
| 'NK',                      |  |
| 'NQ',                      |  |
| 'TW',                      |  |
|                            |  |
| 'VX',                      |  |
| 'YM',                      |  |
| ]                          |  |
|                            |  |
| rates<br>=<br>[            |  |
| 'ED',                      |  |
| 'FV',                      |  |
|                            |  |
| 'TU',                      |  |
| 'TY',                      |  |
| 'US',                      |  |
|                            |  |
| ]                          |  |
|                            |  |

# Join sector lists into one list

markets = currencies + agriculturals + nonagriculturals + equities + rates

```
# Make a list of all continuations
context.universe = [
  continuous_future(market, offset=0, roll='volume', adjustment='mul')
     for market in markets
]
```

```
# Schedule daily trading
schedule_function(rebalance, date_rules.month_start(), time_rules.market_close())
```

# Schedule daily roll check schedule\_function(roll\_futures,date\_rules.every\_day(), time\_rules.market\_close())

```
# Schedule monthly chart update
schedule_function(update_chart,date_rules.month_start(), time_rules.market_close())
```

def update\_chart(context,data):

# This function continuously update the graph during the backtest today = data.current\_session.date() dynamic\_results.loc[today, 'PortfolioValue'] = context.portfolio.portfolio\_value

if ax.lines: # Update existing line ax.lines[0].set\_xdata(dynamic\_results.index) ax.lines[0].set\_ydata(dynamic\_results.PortfolioValue) else: # Create new line ax.semilogy(dynamic\_results)

```
# Update scales min/max
ax.set_ylim(
  dynamic_results.PortfolioValue.min(),
  dynamic_results.PortfolioValue.max()
)
ax.set_xlim(
  dynamic_results.index.min(),
  dynamic_results.index.max()
)
```

```
# Redraw the graph
fig.canvas.draw()
```

def roll\_futures(context,data): today = data.current\_session.date() open\_orders = zipline.api.get\_open\_orders() for held\_contract in context.portfolio.positions:

```
if held_contract in open_orders:
  continue
days_to_auto_close = (held_contract.auto_close_date.date() - today).days
if days_to_auto_close > 10:
  continue
```

```
# Make a continuation
continuation = continuous_future(
     held_contract.root_symbol,
     offset=0,
     roll='volume',
     adjustment='mul'
     )
continuation_contract = data.current(continuation, 'contract')
```

```
if continuation_contract != held_contract:
  pos_size = context.portfolio.positions[held_contract].amount
  order_target(held_contract, 0)
  order_target(continuation_contract, pos_size)
```

```
def position_size(portfolio_value, std, pv, avg_volume):
  target_variation = portfolio_value * risk_factor
  contract_variation = std * pv
  contracts = target_variation / contract_variation
  return int(np.nan_to_num(contracts))
```

```
def rebalance(context, data):
  # Get the history
  hist = data.history(
     context.universe,
     fields=['close', 'volume'],
     frequency='1d',
     bar_count=long_trend_window,
  )
```

# Make a dictionary of open positions open\_pos = {pos.root\_symbol: pos for pos in context.portfolio.positions}

# Loop all markets for continuation in context.universe: # Slice off history for this market h = hist.xs(continuation, 2) root = continuation.root\_symbol

# Calculate volatility std = h.close.diff()[-vola\_window:].std() if root in open\_pos: # Position is already open p = context.portfolio.positions[open\_pos[root]] if p.amount > 0: # Long position if h.close[-1] < h.close[-long\_trend\_window]: # Lost slow trend, close position order\_target(open\_pos[root], 0) elif h.close[-1] < h.close[-short\_trend\_window]: # Lost fast trend, close position order\_target(open\_pos[root], 0) else: # Short position if h.close[-1] > h.close[-long\_trend\_window]: # Lost slow trend, close position order\_target(open\_pos[root], 0) elif h.close[-1] > h.close[-short\_trend\_window]: # Lost fast trend, close position order\_target(open\_pos[root], 0)

else: # No position open yet. if (h.close[-1] > h.close[-long\_trend\_window]) \ and \ (h.close[-1] > h.close[-short\_trend\_window]): # Buy new position contract = data.current(continuation, 'contract') contracts\_to\_trade = position\_size( \ context.portfolio.portfolio\_value, \ std, \ contract.price\_multiplier, \ h['volume'][-20:].mean())

```
order_target(contract, contracts_to_trade)
elif (h.close[-1] < h.close[-long_trend_window]) \
  and \
  (h.close[-1] < h.close[-short_trend_window]):
     # New short position
     contract = data.current(continuation, 'contract')
     contracts_to_trade = position_size( \
                    context.portfolio.portfolio_value, \
                    std, \
                    contract.price_multiplier, \
                    h['volume'][-20:].mean())
```

order\_target(contract, contracts\_to\_trade \*-1)

start = datetime(2001, 1, 1, 8, 15, 12, 0, pytz.UTC) end = datetime(2018, 12, 31, 8, 15, 12, 0, pytz.UTC) perf = zipline.run\_algorithm( start=start, end=end, initialize=initialize, capital\_base=starting\_portfolio, data\_frequency = 'daily', bundle='futures' )

# **Time Return Model Performance**

Our model is so incredibly simple that it couldn't possibly show any sort of interesting performance. Right? Well, as it turns out, trend following does not have to be complex. Sure, this model is still overly simplified and can easily be improved upon, but even in this simple state it still works.

A quick glance at the monthly return table and the long term chart should tell us that we should at least not dismiss this kind of approach out of hand. We can see a few interesting features. First, it tends to perform well during bear markets. We only had two severe bear markets during this time span, but the model handled both really well. Second, we can see that the model appears to be showing quite strong long term performance, at acceptable drawdowns.

![](_page_12_Figure_0.jpeg)

Figure 16-1 - Time Momentum Performance

| Year | Jan    | Feb     | $\mathbf{Mar}$ | Apr    | May     | Jun     | Jul     | Aug     | Sep     | Oct     | Nov     | Dec     |
|------|--------|---------|----------------|--------|---------|---------|---------|---------|---------|---------|---------|---------|
| 2001 | -0.9   | $+8.0$  | $+6.3$         | -5.7   | $+2.4$  | $+1.6$  | $-4.6$  | $+2.2$  | $+9.8$  | $+4.8$  | -3.4    | $-1.6$  |
| 2002 | $+2.6$ | $+1.8$  | -9.7           | -1.4   | $+8.0$  | $+6.5$  | $+2.4$  | $+5.4$  | $+9.8$  | -2.6    | $-0.4$  | $+13.4$ |
| 2003 | $+8.9$ | $+6.7$  | -7.6           | $+0.9$ | $+6.7$  | $-1.7$  | -7.8    | $+0.7$  | $+6.0$  | $+11.7$ | $+5.5$  | $+3.3$  |
| 2004 | $+4.2$ | $+9.4$  | $+2.3$         | -11.8  | -3.1    | -2.9    | $+2.3$  | -1.4    | $+4.4$  | $+5.0$  | $+3.7$  | -0.6    |
| 2005 | -2.4   | $+3.2$  | $+1.3$         | -3.5   | $-4.4$  | $-0.5$  | -2.7    | $+2.7$  | $+0.6$  | -6.7    | $+8.0$  | $+4.3$  |
| 2006 | $+9.7$ | -2.4    | $+6.9$         | $+2.4$ | -6.5    | -3.9    | $-0.1$  | $+4.0$  | -3.3    | $+1.5$  | $+1.2$  | -2.0    |
| 2007 | $+1.2$ | -2.2    | $-0.8$         | $+8.0$ | $+1.2$  | $+4.2$  | $-1.5$  | $+4.7$  | $+13.0$ | $+9.4$  | $+2.3$  | $+2.3$  |
| 2008 | $+8.9$ | $+32.7$ | $-17.4$        | $-1.1$ | $+1.5$  | $+15.9$ | $-17.2$ | $-13.0$ | -3.1    | $+16.3$ | $+11.2$ | $+1.7$  |
| 2009 | $+2.2$ | $+3.3$  | $-4.2$         | -5.5   | -9.6    | $-1.0$  | -0.6    | $+5.8$  | $+5.6$  | -0.9    | $+10.3$ | $+0.8$  |
| 2010 | -5.4   | $+2.9$  | $+2.5$         | $+1.9$ | $-14.0$ | -4.9    | $-4.4$  | $+4.8$  | $+6.1$  | $+13.7$ | -2.4    | $+21.1$ |
| 2011 | $+5.5$ | $+8.7$  | $-0.6$         | $+8.1$ | -7.8    | -7.4    | $+7.8$  | $+2.2$  | $-13.1$ | -6.3    | $+4.7$  | $+0.8$  |
| 2012 | $+1.4$ | $-4.3$  | $-1.2$         | $+0.8$ | -4.9    | -8.2    | $+3.3$  | -6.2    | $-4.2$  | -3.5    | $+1.7$  | -2.7    |
| 2013 | $+6.0$ | -2.7    | $+1.5$         | $+4.3$ | -3.0    | -0.3    | $-1.2$  | $-0.5$  | $+1.8$  | $+1.5$  | $+2.3$  | $+0.6$  |
| 2014 | $-4.3$ | $+0.1$  | $-1.1$         | $+3.0$ | $-0.3$  | $+5.9$  | $-1.3$  | $+4.1$  | $+5.3$  | $+7.7$  | $+13.2$ | $+3.8$  |
| 2015 | $+8.1$ | -4.9    | $+12.5$        | -8.1   | $+7.8$  | -7.1    | $+12.5$ | -3.1    | $+3.8$  | -6.8    | $+8.6$  | -3.3    |
| 2016 | $+5.5$ | $+2.0$  | -7.4           | -3.3   | -3.1    | $+10.8$ | -1.8    | -2.6    | $+3.5$  | -5.0    | $-4.3$  | -0.4    |
| 2017 | $-1.3$ | $+1.6$  | -5.0           | -0.8   | -1.6    | $+2.5$  | $-1.4$  | $-0.5$  | $+0.6$  | $+5.6$  | $+2.4$  | $+3.4$  |
| 2018 | $+8.2$ | -6.1    | $+0.6$         | $+4.1$ | -3.6    | $+1.3$  | $+0.1$  | $+3.9$  | $+1.7$  | -8.9    | -0.9    | $-11.1$ |

*Table 16.1 - Time Return, Monthly Figures* 

What we have here is certainly not the best possible model in any kind, but it's not utterly crazy either. The volatility is quite high, and most likely far too high for most people's appetite. But this kind of performance with such extremely simple rules should tell you something about the nature of trend following.

There are no indicators at all used here. No moving averages, no RSI, no Stochastics, no MACD, no technical analysis terms of any kind required. All we are doing is checking two price points. And we only do that once every month. Keep that in mind the next time someone offers to sell you some amazing trend following system.

| Years | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2001  | +19 | +29 | +31 | +26 | +20 | +17 | +22 | +22 | +20 | +20 | +18 | +14 | +13 | +15 | +15 | +14 | +13 | +12 |
| 2002  | +39 | +38 | +28 | +20 | +17 | +22 | +23 | +20 | +20 | +18 | +13 | +13 | +15 | +15 | +13 | +13 | +11 |     |
| 2003  | +36 | +23 | +14 | +12 | +19 | +20 | +18 | +18 | +16 | +11 | +11 | +13 | +13 | +12 | +11 | +10 |     |     |
| 2004  | +10 | +4  | +5  | +15 | +17 | +15 | +16 | +13 | +8  | +9  | +11 | +12 | +10 | +10 | +8  |     |     |     |
| 2005  | -1  | +3  | +16 | +19 | +16 | +16 | +14 | +8  | +8  | +11 | +12 | +10 | +10 | +8  |     |     |     |     |
| 2006  | +7  | +26 | +27 | +21 | +20 | +17 | +9  | +10 | +13 | +13 | +11 | +11 | +9  |     |     |     |     |     |
| 2007  | +49 | +38 | +26 | +24 | +19 | +10 | +10 | +13 | +14 | +12 | +11 | +9  |     |     |     |     |     |     |
| 2008  | +28 | +16 | +17 | +12 | +3  | +5  | +9  | +10 | +8  | +8  | +6  |     |     |     |     |     |     |     |
| 2009  | +5  | +11 | +7  | -2  | +0  | +6  | +8  | +6  | +6  | +4  |     |     |     |     |     |     |     |     |
| 2010  | +19 | +9  | -4  | -1  | +7  | +8  | +6  | +6  | +4  |     |     |     |     |     |     |     |     |     |
| 2011  | -0  | -14 | -6  | +4  | +7  | +4  | +4  | +2  |     |     |     |     |     |     |     |     |     |     |
| 2012  | -25 | -9  | +5  | +8  | +5  | +5  | +2  |     |     |     |     |     |     |     |     |     |     |     |
| 2013  | +10 | +25 | +22 | +14 | +12 | +8  |     |     |     |     |     |     |     |     |     |     |     |     |
| 2014  | +41 | +29 | +16 | +13 | +7  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2015  | +18 | +5  | +5  | +0  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2016  | -7  | -1  | -5  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2017  | +5  | -4  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2018  | -12 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

#### *Table 16.2 Holding Period Analysis*

But there is one more observation that you should have made by now. Have we not seen this return profile before? Is this not a little similar to something we have seen earlier?

Yes, dear reader. And that's exactly the point that I'm somewhat slowly trying to make.

Trend following returns come from a simple concept. Most trend following models have very high correlation to each other. Or in other words, there are not a whole lot of different ways that you can follow trends. And that's why most trend following trading models have high correlation, and why most trend following hedge funds look very similar over time. The biggest differentiators are asset mix and

time frame, and in this case I purposely kept both models more or less the same.

As seen in Figure 16‑2, these two very different models have far from perfect correlation, but over time they tend to even out and deliver more or less the same result. You could easily make scores of seemingly different trend models, and they will probably all look very similar when compared on an equal basis.

![](_page_15_Figure_2.jpeg)

The first and foremost conclusion we have to draw from this is that trend following, as a phenomenon is quite simple. The bulk of trend following returns can be captured with rules that could be summarized in a single sentence.

As for the returns, if you just look at the yearly numbers they are remarkably strong. Since 2000, only three years ended in the red. No year lost more than 25%, while the best year doubled the money. If you had placed 100,000 in such a strategy in January 2000, you would have over two and a half million in 2016. But of course, no one gets to trade real money on historical simulations.

While this strategy may seem quite attractive when you look back at a long term simulation, it's far from a polished strategy. The volatility for this model is at times far above acceptable levels. The volatility always needs to be taken into account when analyzing a trading model, and in chapter 22 you will get a better insight into how to do this.

The drawdown in 2008 is also a bit worrying. What happened there was that first the model made large gains, and then it much of it was given back. Looking at a simulation, that may not seem like a big deal. Easy come, easy go, right? Perhaps so, if you have the benefit of hindsight in picking your entry into the strategy. If you had invested into this strategy just after the gains, you would just have seen the losses and it would have taken three years to recover them. In reality, you never know when the drawdown will come. Assume it will happen at the worst possible time. Because that's how reality rolls.

Before going too deep into analyzing the returns of this simple 12 months return model, we should identify and fix a couple of deficiencies.

#### **Rebalancing**

This is a very long term trading model with an average holding period of about half a year. Such a model absolutely needs a rebalancing mechanism. Without one, the position risk, and in extension the portfolio risk, would eventually be quite random.

The position allocation for this model is based on recent

volatility. Remember how we look at past volatility and calculate position sizes with the aim of allocating an equivalent amount of risk to each position. Optimally, we would like every position to have an equal possibility to impact the portfolio on a daily basis. That means buying more of slow moving markets and buying less of the more volatile markets.

But of course, the markets are not going to just politely maintain the same volatility level just to make your calculations easier. Volatility is not static and therefore your allocation can't be either.

The solution to this is to reset the position sizes on a regular basis. If you don't, you lose control over position risk and that will cause some nasty spikes in the equity curve.

There are two ways that the actual position risk can change over time. The volatility of the market can, and will change over time. If you would like to build upon this model and improve it, the first order of business should probably be to look at rebalancing and maintaining risk targets.
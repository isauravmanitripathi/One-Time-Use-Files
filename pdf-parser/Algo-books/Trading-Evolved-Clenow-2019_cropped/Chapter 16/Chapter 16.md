# **Counter Trend Trading**

Perhaps trend following is not your cup of tea. After all, it can be quite a frustrating type of strategy to trade at times. Even if results in the long run tends to turn out well, anyone who has done some serious trend following trading can tell you how it often feels like you could make money from doing the exact opposite.

One thing in particular that most trend followers see time and again is how prices fall back to the trailing stops, only to move right back into the trend soon after you are stopped out. Out of necessity, trend following models need to stop out at some point. It's something unavoidable for that type of strategy. You may think that the solution is to simply move the trailing stop distance for the trend models further away, but it's not that easy. That will result in a longer term trend model, and you still have the same issue on a different time horizon.

This is quite an interesting and easily observable market phenomenon. As usual, we can only speculate as to why this happens and no matter how good of an explanation we come up with, we can never be sure if it's the real reason or not. Short of installing listening devices in the homes and workplaces of all the world's traders, we simply can't know why market participants react the way that they do, and it would appear as if Amazon Alexa is already way ahead of us in that game.

But, the inability to verify or even make practical use of an origin theory of a market phenomenon shouldn't prevent us from fabricating some. A successful trading model often has a good story behind it. Sometimes that story may help create confidence in the approach, and sometimes it may help raise the necessary assets to trade it. Often a solid trading model starts off with such a theory, with the broad idea of what you want to take advantage of, and why. Surprising as it may seem, it can actually help if there is a logical

reason for your trades.

In this case, there is a possible explanation that comes to mind. The trend following industry was once a niche trading variant which few took very seriously. As the success of this strategy became hard to ignore, it attracted increasing amounts of both new traders and investors. At this time, there is in excess of a quarter of a trillion dollars under management with such strategies.

It would be reasonable to assume that this kind of size has a serious market impact. Trend followers were once passive market followers. Now, one could argue, they are not merely following market price moves but creating them.

Contrary to some public perception, being large enough to move market prices is rarely an advantage. It's not like you can snap your fingers and make prices lower before you want to buy. The case is more likely that you would like to buy, but as you start doing so, your order sizes push the prices higher and gives you a significantly worse execution price. It can be a real problem to have too much money in this business. Should David Harding by any chance be reading this book, I'm perfectly willing to be a good friend and help out by taking over some of those assets, Dave.

In my first book, I demonstrated that most trend following hedge funds employ very similar strategies. This would imply that they all have mechanisms similar to trailing stop losses. If this is true, that would mean that they all trade at very similar times.

If we had a nice bull market trend in the oil market for instance, it would reasonable to assume that most if not all trend followers are long. Now imagine that the price of oil starts to decline for whatever reason. At some point, trend followers start exit. And that can push the price a bit further down, perhaps even triggering stops for other trend followers.

Given the sheer size of trend following capital, this can create a situation where a small market correction is amplified by their stop

loss orders. This could result in two things. First that the market is pushed further back than it otherwise would be. Second, that when trend followers are done stopping out, there could be a snap back, as the prices had been artificially depressed by the stops.

Perhaps we could model this and see if there is any money in exploiting such a phenomenon.

## **Counter Model Logic**

The general idea here is to reverse the logic of trend following models. What we want to do is to figure out more or less where trend models stop out, and then enter positions about that time. This mean reversion style model will try to enter during those pullbacks, betting on the price moving up again. Clearly, with this type of model, the entry timing is the most important element.

When exploring trading ideas, it can often help to try to isolate the part of the strategy that appears most important, as an initial test. That's what we are going to try to do here. We are going to explore if there is a predictive value to enter into the kind of pullbacks where trend followers usually stop out.

As with all trading models in this book I want to again stress, once again, that I'm trying to teach and demonstrate concepts. These are not production grade models and they are not meant to be. The point here is for you to learn how to construct models, and giving you exact rules to copy and trade would very much defeat that purpose. Study these models, learn from them and built your own production grade models.

The parameters are not optimized or selected to show the best possible result. They are quite deliberately a bit of middle of the road kind of settings. They are picked more or less randomly, from a range of reasonable values.

So, having gotten that out of the way, now take a look at the entry rules. We are only looking to buy dips in bull markets. In my view, the dynamics of bear market rallies tend to be so different from bull market dips that we can't use the same logic, or at least not the same settings. In order to keep things reasonably simple, we are going to focus on bull market dips.

That means that we need to know if there is a bull market on. We need to define what a bull market is.

I will define a bull market here as when the 40 day exponential moving average is above the 80 day exponential moving average. Exponential moving averages are quite popular among technical analysts as they are said to react faster. What they do is to up-weight recent observations compared to older ones. I use it here, not because it's better, but because it can be a useful tool and sooner or later someone will come around to asking how to calculate exponential moving average in Python.

![](_page_3_Figure_3.jpeg)

*Figure 17*‑*1 Exponential Moving Average*

There is a very important thing to understand when working with exponential moving averages though. This is a classic source of confusion with many technical analysis indicators. The age old

question about why your exponential moving average is not the same as mine. While it may sound as if a 40 day exponential moving average only uses and only needs 40 daily closes, that's not the case. The exponential weighting starts with the previous value, and that means that it never really drops data points. It merely down-weights them into oblivion over time.

What is important to understand here is that you will get a slightly different value for a 40 day exponential moving average if you apply it on a half year time series history for a market, than if you apply it on ten years' worth of history for the same market. I guess that what I'm trying to say here is, please refrain from sending me emails about why your EMA is a little different from mine.

# **Quantifying Pullbacks**

Once we know that we are in a bull market, we will look for pullbacks. An easy way to quantify pullbacks is to measure the distance from a recent high, but this needs to be put into some sort of a context. Clearly it wouldn't make sense to trigger a trade on a pullback of ten dollars for instance, as a ten dollar pullback in gold is quite different from the same in gasoline. Neither would percentage pullbacks make any sense, given the vastly varying volatility across the futures markets.

No, what we need to do is to standardize the pullback to the volatility of each market. If you think about it, we already have a good tool for this. We have been using standard deviation as a volatility proxy in previous models for the purpose of position sizing. There is nothing stopping us from reusing this analytic for standardizing pullbacks.

So in this model we will use a 40 day standard deviation of price changes both for position sizing purposes and for pullback. A pullback will be measured as the difference between current price and the highest close in the past twenty days, divided by the standard

deviation. That will tell us how many standard deviations we are away from the highest price in about a month.

This results in an analytic that can be compared across markets. You could use the same process for stocks, bonds, commodities and other markets, as it takes the volatility into account. In this model, we are going to buy to open if we are in a bull market, as defined by the moving averages described above, and we see a pullback of three times the standard deviation.

In the Python code, we calculate this pullback with just a few lines. The snippet below is from the source code for the model, which you will find in its entirety later in this chapter. As you see, this code first checks if we have a positive trend. If so, we calculate the difference between the latest close value and the highest for 20 days back, the high\_windo w variable, and divide this by the standard deviation.

```
if h['trend'].iloc[-1]:
   pullback = (
     h['close'].values[-1] - np.max(h['close'].values[-high_window:])
     ) / std
```

As for the exit, we are going to use a really simple logic, just to demonstrate the entry idea. I want to show that what is important with this kind of model is the entry. That does not mean that everything else is unimportant, but a mean reversion style model like this is very much dependent on a solid entry logic. That's not the case for many other types of strategies.

To see if there is any predictive value in the entry method described, we are going to use two simple exit criteria. First, if the trend as defined by the two moving averages turns bearish, we exit on the following day. Second, if that does not happen we hold the position for 20 trading days, approximately one month. Then we exit.

You are probably wondering why there is no stop loss point and no target exit price here. Those things may very well make sense, and I encourage you to try it out. The goal here is to teach you concepts and provide ideas for further research. Replicate what is

shown here, try it out, modify it and make it your own.

# **Rules Summary**

Long positions are allowed if the 40 day exponential moving average is above the 80 day exponential moving average. If the price in a bull market falls back three times its standard deviation from the highest closing price in the past 20 days, we buy to open. If the trend turns bearish, we exit. If the position has been held for 20 trading days, we exit. Position size is volatility parity, based on standard deviation.

### **Counter Trend Source Code**

In the previous model, the time return model, we learnt how to make a dynamically updating graph during the backtest, showing the portfolio value as it is being calculated. This time around, I will keep that, but also add an updating chart to show how the exposure changes over time.

```
import zipline
from zipline.api import future_symbol, \
  set_commission, set_slippage, schedule_function, date_rules, \
  time_rules, continuous_future, order_target
from datetime import datetime
import pytz
import pyfolio as pf
import pandas as pd
import numpy as np
from zipline.finance.commission import PerTrade, PerContract
from zipline.finance.slippage import FixedSlippage, VolatilityVolumeShare
```

# These lines are for the dynamic text reporting from IPython.display import display import ipywidgets as widgets out = widgets.HTML() display(out)

```
"""
Model Settings
"""
starting_portfolio = 20000000
vola_window = 40
slow_ma = 80
fast_ma = 40
risk_factor = 0.0015
high_window = 20
days_to_hold = 20
dip_buy = -3
def report_result(context, data):
  context.months += 1
  today = zipline.api.get_datetime().date()
  # Calculate annualized return so far
  ann_ret = np.power(context.portfolio.portfolio_value / starting_portfolio,
           12 / context.months) - 1
```

```
# Update the text
out.value = """{} We have traded <b>{}</b> months
and the annualized return is <b>{:.2%}</b>""".format(today, context.months, ann_ret)
```

```
def initialize(context):
  """
```

```
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
set_commission(us_futures=comm_model)
```

```
if context.enable_slippage:
  slippage_model=VolatilityVolumeShare(volume_limit=0.3)
else:
  slippage_model=FixedSlippage(spread=0.0)
```

```
set_slippage(us_futures=slippage_model)
```

agricultural = [ 'BL', 'CC',

| 'CT',                     |  |  |
|---------------------------|--|--|
| 'FC',                     |  |  |
| 'KC',                     |  |  |
| 'LB',                     |  |  |
| 'LR',                     |  |  |
| 'OJ',                     |  |  |
| 'RR',<br>'_S',            |  |  |
| 'SB',                     |  |  |
| 'LC',                     |  |  |
| 'LS',                     |  |  |
| ]                         |  |  |
| nonagricultural<br>=<br>[ |  |  |
| 'CL',                     |  |  |
| 'GC',                     |  |  |
| 'HG',                     |  |  |
| 'HO',                     |  |  |
| 'LG',                     |  |  |
| 'PA',                     |  |  |
| 'PL',<br>'RB',            |  |  |
| 'SI',                     |  |  |
| 'NG',                     |  |  |
| 'LO',                     |  |  |
| ]                         |  |  |
| currencies<br>=<br>[      |  |  |
| 'AD',                     |  |  |
| 'BP',                     |  |  |
| 'CD',                     |  |  |
| 'CU',                     |  |  |
| 'DX',<br>'NE',            |  |  |
| 'SF',                     |  |  |
| 'JY',                     |  |  |
| ]                         |  |  |
| equities<br>=<br>[        |  |  |
| 'ES',                     |  |  |
| 'NK',                     |  |  |
| 'NQ',                     |  |  |
| 'YM',<br>]                |  |  |
| rates<br>=<br>[           |  |  |
| 'ED',                     |  |  |
| 'FV',                     |  |  |
| 'TU',                     |  |  |
| 'TY',                     |  |  |
| 'US',                     |  |  |
| ]                         |  |  |
|                           |  |  |

```
context.universe = \
  [
  continuous_future(market, offset=0, roll='volume', adjustment='mul') \
  for market in markets
  ]
```

# Dictionary used for keeping track of how many days a position has been open. context.bars\_held = {market.root\_symbol: 0 for market in context.universe}

```
# Schedule daily trading
schedule_function(daily_trade, date_rules.every_day(), time_rules.market_close())
```

# We'll just use this for the progress output # during the backtest. Doesn't impact anything. context.months = 0

```
# Schedule monthly report output
schedule_function(
  func=report_result,
  date_rule=date_rules.month_start(),
  time_rule=time_rules.market_open()
)
```

def roll\_futures(context, data): open\_orders = zipline.api.get\_open\_orders()

for held\_contract in context.portfolio.positions: # don't roll positions that are set to change by core logic if held\_contract in open\_orders: continue

```
# Save some time by only checking rolls for
# contracts expiring in the next week
days_to_auto_close = (
  held_contract.auto_close_date.date() - data.current_session.date()
).days
if days_to_auto_close > 5:
  continue
```

# Make a continuation continuation = continuous\_future( held\_contract.root\_symbol, offset=0,

```
roll='volume',
adjustment='mul'
)
```

# Get the current contract of the continuation continuation\_contract = data.current(continuation, 'contract')

if continuation\_contract != held\_contract: # Check how many contracts we hold pos\_size = context.portfolio.positions[held\_contract].amount # Close current position order\_target(held\_contract, 0) # Open new position order\_target(continuation\_contract, pos\_size)

def position\_size(portfolio\_value, std, pv): target\_variation = portfolio\_value \* risk\_factor contract\_variation = std \* pv contracts = target\_variation / contract\_variation # Return rounded down number. return int(np.nan\_to\_num(contracts))

def daily\_trade(context, data):

open\_pos = {pos.root\_symbol: pos for pos in context.portfolio.positions}

```
hist = data.history(
  context.universe,
  fields=['close', 'volume'],
  frequency='1d',
  bar_count=250,
)
```

# Calculate the trend hist['trend'] = hist['close'].ewm(span=fast\_ma).mean() > hist['close'].ewm(span=slow\_ma).mean()

for continuation in context.universe: root = continuation.root\_symbol

# Slice off history for this market h = hist.xs(continuation, 2)

# Calculate volatility std = h.close.diff()[-vola\_window:].std()

if root in open\_pos: # Check open positions first. context.bars\_held[root] += 1 # One more day held

```
if context.bars_held[root] >= 20:
  # Held for a month, exit
  contract = open_pos[root]
  order_target(contract, 0)
```

elif h['trend'].iloc[-1] == False: # Trend changed, exit. contract = open\_pos[root] order\_target(contract, 0)

```
else: # Check for new entries
  if h['trend'].iloc[-1]:
```

# Calculate the pullback pullback = ( h['close'].values[-1] - np.max(h['close'].values[-high\_window:]) ) / std

if pullback < dip\_buy: # Get the current contract contract = data.current(continuation, 'contract')

```
# Calculate size
contracts_to_trade = position_size( \
               context.portfolio.portfolio_value, \
               std, \
               contract.price_multiplier)
# Trade
order_target(contract, contracts_to_trade)
```

# Reset bar count to zero context.bars\_held[root] = 0

# Check if we need to roll. if len(open\_pos) > 0: roll\_futures(context, data)

start = datetime(2001, 1, 1, 8, 15, 12, 0, pytz.UTC)

end = datetime(2018, 12, 31, 8, 15, 12, 0, pytz.UTC)

perf = zipline.run\_algorithm( start=start, end=end, initialize=initialize, capital\_base=starting\_portfolio, data\_frequency = 'daily', bundle='futures' )

#### **Counter Trend Results**

Once again we see that a simple set of rules can show pretty good results, as long as there is a solid underlying premise. There are a few worrying negative months, as seen in Table 17.1, but given the wonky stop logic in this demo model that shouldn't be too surprising. What we see is a strategy that can get pretty volatile at times, but which has delivered strong risk adjusted returns over time.

Not bad for such a simple model. The takeaway here is that there seem to be a value in this kind of entry logic. The conclusion is not that you should run to your broker and bet all of your cash on this, but rather that this could be an interesting research topic to develop further. If this simple logic can result in pretty interesting returns, surely you can make it better, adapt it to your own needs, add some features to it and create a proper production grade model.

| Year | Jan   | Feb   | Mar  | Apr   | May  | Jun  | Jul  | Aug  | Sep  | Oct   | Nov  | Dec   | Year  |
|------|-------|-------|------|-------|------|------|------|------|------|-------|------|-------|-------|
| 2001 | -2.0  | -1.1  | +1.2 | -2.0  | -1.5 | -1.3 | +1.3 | -2.1 | +3.8 | +3.1  | -1.0 | -1.4  |       |
| 2002 | -1.6  | +4.6  | -2.5 | +2.5  | +4.3 | +4.3 | +1.9 | +8.4 | +2.9 | +1.8  | -2.1 | +11.3 | +41.2 |
| 2003 | +14.5 | -2.9  | -4.3 | -2.1  | +0.4 | -0.8 | -0.6 | +6.9 | -0.1 | -11.7 | +9.6 | +2.6  | +9.3  |
| 2004 | +5.8  | +11.9 | +0.6 | -12.9 | -2.1 | -2.6 | +2.8 | +2.5 | +7.4 | +3.2  | -0.9 | +1.4  | +16.1 |
| 2005 | -2.1  | +6.0  | +0.9 | -4.9  | -2.1 | -0.4 | +0.5 | +8.8 | +5.8 | -1.5  | +4.8 | +1.3  | +17.4 |
| 2006 | +2.9  | -2.2  | -2.4 | +4.3  | -3.7 | -5.4 | +0.3 | +1.0 | -1.1 | -0.7  | +3.3 | -2.4  |       |
| 2007 | -0.9  | +2.1  | +1.8 | +5.4  | +0.1 | +2.9 | +1.1 | -5.6 | +5.9 | +14.6 | -4.8 | +6.1  | +30.9 |
|      |       |       |      |       |      |      |      |      |      |       |      |       |       |

*Table 17.1 - Counter Trend Monthly Returns*

| 2008 | $+9.2$ | $+19.0$ | -3.7   | $+4.5$ | $+2.3$ | $+5.3$  | -4.8   | -9.5   | -2.1   | -1.6    | $+2.4$  | $-0.2$ +   |        |
|------|--------|---------|--------|--------|--------|---------|--------|--------|--------|---------|---------|------------|--------|
| 2009 | $+0.1$ | $-1.7$  | $+1.3$ | $+0.1$ | $+4.8$ | $+0.1$  | $+2.0$ | $+3.5$ | $+7.9$ | $+8.7$  | $+14.4$ | -4.0       | $+$    |
| 2010 | -1.9   | $+7.0$  | -2.1   | $+2.5$ | -26.1  | $+1.5$  | $+1.9$ | $+2.6$ | $+8.4$ | $+12.2$ | -5.9    | $+15.5$    | $\sim$ |
| 2011 | $+6.8$ | $+9.5$  | $+0.5$ | $+8.1$ | -1.4   | -4.7    | $+7.7$ | -4.8   | -11.5  | $+1.0$  | $+3.2$  | -0.8       | $+$    |
| 2012 | $+6.6$ | -1.5    | $-0.5$ | -1.5   | -12.0  | $-0.7$  | $+6.4$ | -0.2   | $+1.6$ | -5.8    | $+0.5$  | $+0.3$     |        |
| 2013 | $+2.8$ | -4.3    | $+1.8$ | $+0.1$ | -6.7   | $-2.1$  | $+3.3$ | $+0.7$ | $+3.8$ | $+6.1$  | $+0.4$  | $+0.6$     |        |
| 2014 | -0.0   | $+9.2$  | $+1.4$ | $+7.2$ | $+1.0$ | $+9.2$  | -8.0   | $+4.4$ | $-0.4$ | $-0.4$  | $+1.6$  | -2.1   +   |        |
| 2015 | $+7.4$ | $-0.0$  | $+0.3$ | $-0.1$ | $+0.2$ | $+2.1$  | -4.3   | -5.0   | $+2.6$ | $-0.3$  | -2.5    | -1.6       |        |
| 2016 | -5.7   | $+2.1$  | $+3.4$ | $+5.3$ | -3.7   | $+12.4$ | $-0.4$ | -4.1   | $+6.9$ | -4.3    | $+1.6$  | $-1.3$ +   |        |
| 2017 | $+0.5$ | $+4.3$  | -2.5   | $+1.1$ | $+1.6$ | $+2.7$  | $+5.1$ | $+4.1$ | -7.0   | -0.2    | $+6.0$  | $+1.1$   + |        |

The equity curve in Figure 17-2 shows us a strategy with a clear positive bias. It tends to have a fairly low correlation to the equity markets, and it usually underperforms during long term bull markets. That's not necessarily a problem though, as it shows strong performance during bear markets, and a substantial outperformance in the long run.

![](_page_14_Figure_0.jpeg)

*Figure 17*‑*2 Counter Trend Simulation Results*

In Table 17.2 you can see what would have happened if you started this strategy at a given year, and kept trading it for a number of years from that point. This can be a useful way to quickly get an overview of how the initial staring time sometimes can matter quite a lot for a trading model. The numbers show annualized return over the number of years displayed on the x-axis.

While the long term return looks attractive, this kind of graph can quickly show us that there are starting years where you may not have been as happy. If you would have started this strategy in 2011, you would only have annualized about 4% after 8 years. But on the other hand, had you started in 2007, you would have seen an annualized gain of 16% after the same number of years.

*Table 17.2 Holding period analysis for the counter trend*

#### *model*

| Years | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2001  | -3  | +17 | +14 | +15 | +15 | +11 | +14 | +15 | +17 | +17 | +16 | +14 | +13 | +14 | +13 | +13 | +13 |
| 2002  | +41 | +24 | +21 | +20 | +15 | +17 | +17 | +20 | +19 | +18 | +16 | +15 | +15 | +14 | +14 | +14 | +12 |
| 2003  | +9  | +13 | +14 | +9  | +13 | +14 | +18 | +16 | +16 | +13 | +13 | +14 | +12 | +12 | +13 | +10 |     |
| 2004  | +16 | +17 | +8  | +14 | +15 | +19 | +18 | +17 | +14 | +13 | +14 | +13 | +12 | +13 | +10 |     |     |
| 2005  | +17 | +5  | +13 | +14 | +20 | +18 | +17 | +14 | +13 | +14 | +12 | +12 | +13 | +10 |     |     |     |
| 2006  | -6  | +11 | +14 | +20 | +18 | +17 | +13 | +12 | +13 | +12 | +12 | +12 | +9  |     |     |     |     |
| 2007  | +31 | +25 | +30 | +25 | +22 | +17 | +15 | +16 | +14 | +14 | +14 | +11 |     |     |     |     |     |
| 2008  | +19 | +30 | +23 | +20 | +14 | +12 | +14 | +12 | +12 | +12 | +9  |     |     |     |     |     |     |
| 2009  | +42 | +25 | +20 | +13 | +11 | +13 | +11 | +11 | +12 | +8  |     |     |     |     |     |     |     |
| 2010  | +9  | +11 | +4  | +5  | +8  | +6  | +7  | +8  | +5  |     |     |     |     |     |     |     |     |
| 2011  | +12 | +2  | +3  | +8  | +6  | +7  | +8  | +4  |     |     |     |     |     |     |     |     |     |
| 2012  | -8  | -1  | +7  | +4  | +6  | +8  | +3  |     |     |     |     |     |     |     |     |     |     |
| 2013  | +6  | +15 | +9  | +9  | +11 | +5  |     |     |     |     |     |     |     |     |     |     |     |
| 2014  | +24 | +10 | +11 | +12 | +5  |     |     |     |     |     |     |     |     |     |     |     |     |
| 2015  | -2  | +4  | +9  | +1  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2016  | +11 | +14 | +2  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2017  | +17 | -2  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2018  | -19 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

This model clearly showed lower returns in the past few years. The final year of the backtest certainly had an impact, as it ended at about 15 percent in the red. Some readers may be surprised about this, as books tend to show models that performed remarkably well for the entire period, or at the very least the most recent years. It would have been easy for me to tweak the settings of the backtest until such a result was achieved, but that would really be contrary to the brief of this book.

If you want to curve fit this backtest, go ahead and tweak the settings until you get the results you like to see. Just keep in mind that it's not terribly likely to result in any meaningful predictive value. The settings used here are picked not based on the backtest results they yield, but for their symmetry to the trend model shown earlier. The reason for that, is simply that it makes it easier to explain the

underlying rationale of this trading approach.

While curve fitting is a bad idea, that does not mean that you should go ahead and trade these exact settings either. What you need to do is think long and hard about what you want to achieve with a model. It's not just a matter of aiming for high returns. It's a matter of finding a desired return profile, and that does not always mean highest possible returns. In fact, it very rarely means that.

No, a much more interesting way to see a mean reversion model like this, is as a portfolio component, traded alongside with trend following models. But I'm getting ahead of myself. More on that later on.
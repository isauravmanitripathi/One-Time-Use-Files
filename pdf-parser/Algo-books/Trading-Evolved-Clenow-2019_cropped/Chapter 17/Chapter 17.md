# **Trading the Curve**

When I set out to write this book, my primary stated purpose was to broaden the horizon of retail traders. To show things that they might not be aware of, to make them see new possibilities and ways of working that they might not otherwise have thought of. Hopefully the concept in this chapter will be such a lesson, showing a type of trading which many readers probably had not considered.

What I intend to demonstrate here is a method of trading futures without using any historical data. Yes, we will still use systematic, algorithmic trading, but we won't need any price history for the trading logic. All we need is the current prices.

We are going to calculate the cost of carry and use this as the sole input for trade selection. This means that we need to look at not just the front contract, but at contracts further out. Most futures based trading models trade only the front contract, and nothing else. For this model here, we won't trade the front at all, only further out points.

The term I use here is curve trading, and that's how I refer to this trading approach. To be clear, what we will be doing here is to trade carry. The cost of carry is implied by the shape of the term structure curve. Depending on what terminology you are used to, you may be of the view that curve trading means taking offsetting positions on the curve, long one month and short another. That's a highly related concept, and if you understand the model presented in this chapter you can easily expand to such calendar spread type models, as they are often called, later on. But for now, we are simply trading carry.

#### **Term Structure Basics**

Some readers already know exactly where I'm heading with

this, but others may prefer to get a little refresher course on term structures first.

Futures contracts have a limited life span. There is a date when each contract ceases to exist. This means that there is not just one futures gold contract, but a rather large amount of them. At any given time, there will be one specific contract that has the highest liquidity. Most people would trade the contract that's closest to expiry, as long as it has not passed the first notice date.

The first notice date, usually a month before expiry, refers to the date when a contract becomes deliverable, and someone still holding it can be called upon to make or take delivery. As traders, we don't really want to be part of that, but it's not really a risk in reality. Your broker won't let you keep positions open after that date anyhow. First notice date is a concept primarily in commodity futures, and that's the only sector which we are going to trade in this chapter. It's in the commodity sector that term structure trading is of most interest.

Figure 18‑1 shows how the term structure for soybeans looked at the time of writing this. As with any financial data, this is ever changing of course. This figure shows the expiry dates on the x-axis, and corresponding price and open interest for each contract. These are the contracts currently trading, again at the time of writing this.

![](_page_2_Figure_0.jpeg)

*Figure 18*‑*1 Term Structure in Contango*

In this example, you can see that each consecutive point on the curve is a little higher up than the previous one. That's, contracts are more expensive the longer time there is until they expire. That situation is called **contango** . The reversed, if each point would get cheaper, would be called **backwardation** , which is what you see in Figure 18‑2.

![](_page_2_Figure_3.jpeg)

The closest contracts tends to be traded fairly close to the underlying asset. The less time left to expiry, the closer the price tends to be. The reason for that is simple. At expiry time, the value of the contract is the same as the value of the underlying, as it will be settled for it. But when there is plenty of time left, other factors take the driver's seat.

There are multiple reasons for why the price further out in the future is different, but as quantitative traders we rarely need to dig deep into these reasons. Factors in play include interest rates, cost of storage and seasonality.

What matters is how to interpret this pattern. Here is a simple way to think about it. If the term structure is in contango, as in Figure 18‑1, there is a bearish bias. Why? Because the closer a contract gets to expiry, the closer the price will be to the underlying. So if the underlying stays exactly the same, each point on the curve in Figure 18‑1 would have to slowly move down until it finally hits the underlying asset's price.

The reverse is therefore true for backwardation, which then has a built in bullish bias. The underlying would need to move down simply for the points on the backwardation structure to stay the same. If the underlying does not move, the contracts need to come up to meet it.

Now if you understand the general idea, you are probably already thinking about how to quantify this effect.

## **Quantifying Term Structure Effect**

While there are different ways to quantify the term structure, I will demonstrate a methodology which I believe makes intuitive sense. This involves calculating an implied annual yield, or cost of carry if you will. It needs to be annualized, so that the resulting number can be compared across different delivery dates. As always in

finance, time matters. If a contract three months out is traded at a 2% discount that is more significant than if a contract 12 months out is traded at the same 2% discount. Just like how it's preferable to make a hundred dollars today than in a year from now.

We will use the same data as for Figure 18‑1 in this example. First I will show you how to calculate one point manually and then we will look at how to get this done easily for the entire curve.

The first point in the curve, the closest contract, expires on the 14 th of March 2019. That contract, the SH9, is currently traded at 907.50 cents per bushel. No, you don't really need to know much about bushels to trade soybeans. The next contract out is the SK9, expiring on May 14 th the same year, and that's traded at 921.50 cents per bushel.

The SK9 expires 61 days after SH9. If the underlying, cash soybean, does not move at all, the SK9 would need to move from 921.50 down to 907.50 in the next 61 days. That makes for a loss of 1.52%. A loss of 1.52% in 61 days, would be the equivalent of an annualized loss of 8.75%.

This gives us a number that we can both relate to and compare across markets and expiration dates. We have a quantifiable, comparable yearly yield number.

Getting this sort of thing done quickly on a futures chain is very simple. First we will start off with a standard Pandas **DataFrame** with the prices and expiry dates. The data in Table 18.1 is the same as we used for the term structure figure just earlier, and it shows a market in contango. If you did not skip the Python introduction in the first part of this book, you should have no problem getting this data into a **Pandas DataFrame** .

*Table 18.1 Term Structure Data*

|  | expiry | price | open_interest |
|--|--------|-------|---------------|
|  |        |       |               |

| 0 | 14<br>March<br>2019     | 907.50 | 295,414 |
|---|-------------------------|--------|---------|
| 1 | 14<br>May<br>2019       | 921.50 | 206,154 |
| 2 | 12<br>July<br>2019      | 935.00 | 162,734 |
| 3 | 14<br>August<br>2019    | 940.25 | 14,972  |
| 4 | 13<br>September<br>2019 | 943.50 | 7,429   |
| 5 | 14<br>November<br>2019  | 952.00 | 75,413  |
| 6 | 14<br>January<br>2020   | 961.50 | 7,097   |

Assuming you have the above table in a **DataFrame** called simply d f , you could get the analytic we are looking for step by step like this.

```
df['day_diff'] = (df['expiry'] - df.iloc[0]['expiry']) / np.timedelta64(1, 'D')
df['pct_diff'] = (df.iloc[0].price / df.price) - 1
df['annualized_carry'] = (np.power(df['pct_diff'] + 1, (365 / df.day_diff))) – 1
```

As you should have figured out about Python at this point, you could of course do all of this in a single row if you like. The ability of Python to perform multiple complex operations in a single row can at times be great, but it also tends to make the code more difficult to follow.

Running this code, and adding these columns should result in a **DataFrame** like the one below in Table 18.2. Now we have something useful. This is a table that we can use directly for trading logic.

|   | expiry                  | price  | open_interest | day_diff | pct_diff | annualized_carry |
|---|-------------------------|--------|---------------|----------|----------|------------------|
| 0 | 14<br>March<br>2019     | 907.50 | 295,414       | 0        | 0.00%    | 0.00%            |
| 1 | 14<br>May<br>2019       | 921.50 | 206,154       | 61       | -1.52%   | -8.75%           |
| 2 | 12<br>July<br>2019      | 935.00 | 162,734       | 120      | -2.94%   | -8.68%           |
| 3 | 14<br>August<br>2019    | 940.25 | 14,972        | 153      | -3.48%   | -8.11%           |
| 4 | 13<br>September<br>2019 | 943.50 | 7,429         | 183      | -3.82%   | -7.47%           |
| 5 | 14<br>November<br>2019  | 952.00 | 75,413        | 245      | -4.67%   | -6.88%           |
| 6 | 14<br>January<br>2020   | 961.50 | 7,097         | 306      | -5.62%   | -6.66%           |

*Table 18.2 Annualized Carry*

A table like this tells you where on the curve you would theoretically get the best return. But you also need to take liquidity

into account. Often you will find that there is a substantial theoretical gain to be made by trading far out on the curve, but that there simply is no liquidity available.

But in this case, we see that there seem to be a nearly 9% negative yield in the May contract, which is the second closest delivery and it seems to have sufficient liquidity to consider.

This logic forms the basis of what our next trading model will do.

#### **Curve Model Logic**

We are going to make quite a simple model, based on the logic just described. We are going to trade only commodities, and only a set of fairly liquid ones. This is not a strategy that can be used in any market, and it would be little use trying the same methodology on currency futures or low liquidity markets.

In this version, we attempt to find a contract one year out on the curve to trade. That is, a contract expiring one year later than the current front contract. Trading is only done once per week at which point we go over each market we cover, identify the contract one year out and calculate the annualized carry.

Having calculated this for all the markets we cover, the model sorts the markets on the carry and picks the top 5 backwardation to go long and the top 5 contango to go short.

By default here, we attempt to trade an equal notional amount of each contract. Why, you may ask, after my previous rants on this book on the value of volatility parity allocation. Two reasons. First, I figured that I may have already confused readers enough with this very different way of constructing a model and I want to keep the logic simple and easy to follow. And second, for this particular approach, it's not going to make a whole lot of difference. We are

only trading one asset class and the volatility differences won't be enormous.

As opposed to other models in this book, we are now dealing with potentially low liquidity markets, and that requires some extra consideration. Even if the gold front contract is heavily traded, the contract one year out will probably not be.

This means that we need to ensure that our model, or rather our backtester, can handle it realistically. We simply can't assume that we will get filled on open on any size. Luckily, Zipline is pretty good at this, and the model will use a slippage condition to ensure that we never trade more than 20% of daily volume.

The model will then take a maximum of 20% of the volume, and leave the remainder of the open order for the following trading day. Large orders will be spread out over several days, when needed.

But I will also put in one extra liquidity condition, to be on the safe side. Consider if for instance the coffee contract one year out has an average daily volume of 100 contracts, and your model decides it's a good idea to place an order for 1,000 contracts. The Zipline logic will model the fills each day, and it may take you a couple of weeks or more to get completely filled. Realistic perhaps, but that's not what we want to see here.

For that reason, we'll put a condition to check the average daily volume on the contract we want to trade, and refrain from placing any order larger than 25% of that. It may still take a couple of days sometimes to get filled, but it shouldn't take more. This condition will limit the maximum size of the orders.

As you will see in the source code, the default version that I'm showing you here will attempt to build an exposure of 150% long and 150% short, for a near zero net exposure. Of course, you can't expect to be "delta neutral" by for instance having a short soybean position offsetting a long crude oil position. The term delta neutral stems from the options markets and means that you, at least in theory, lack a

directional exposure to the markets.

Don't expect a perfect hedge of any kind, but of course it does help a bit with the overall risk to have a long and a short leg. All in all, the gross exposure level of 300% is not out of proportion for a reasonably diversified futures model.

As previously, all major settings are up top in the code, so that you can easily try your own variations once you have set up your local Python modelling environment.

# **Curve Trading Source Code**

By now you should be quite familiar with the general structure of Zipline backtest code. I will show you the key parts of this particular model first, and then as usual, at the end of this section you will find the complete source code.

First up, the settings for the model.

```
# settings
spread_months = 12
pos_per_side = 5
target_exposure_per_side = 1.5
initial_portfolio_millions = 1
volume_order_cap = 0.25
```

With these settings we can switch things up a bit and easily try variations. The first setting, spread\_month s , sets how far out on the curve we are targeting. In the default case, we're looking for contracts a full month out.

The second setting, pos\_per\_sid e , is for now many markets do we want to be long, and how many we want to be short. In the current implementation, this number sets both long and short positions.

Next setting, target\_exposure\_per\_sid e , sets percent exposure per side. At the default value of 1.5, we are trying to build an exposure of 150% long and 150% short.

Next we set how many millions we want to start off with, and lastly we set a volume order cap. That last setting can be quite important for this particular model. Trading these less liquid contracts with longer to expiry means that we need to be careful with liquidity. We are not able to trade too large, and we should always make sure that there is enough capacity.

At the default 0.25 value for volume\_order\_ca p , our trading code will limit orders to 25% of the average daily volume. This will make sure that we don't try to place orders far larger than the market can handle, and end up spending weeks trying to get it executed.

The trading logic is done once a week, which is the only time when we are adjusting our portfolio composition. Since we are trading specific contracts here, and not trying to stay with the front contract as is otherwise common, there is no need for roll logic.

Let's look at the logic step by step, to see what operations are performed each month for this model.

First we merely create an empty **DataFrame** , using the list of markets in our investment universe. We're going to populate this **DataFrame** with our calculated carry analytics in a moment.

```
def weekly_trade(context, data):
  # Empty DataFrame to be filled in later.
  carry_df = pd.DataFrame(index = context.universe)
```

Once we have that empty **DataFrame** , we are going to loop through all the markets we cover, get the front contract and the contract one year out, calculate the carry and store it in the **DataFrame** . Here is it, step by step.

This first part starts the loop, gets the contract chain and transforms it into a **DataFrame** with contracts and corresponding expiry dates.

```
for continuation in context.universe:
  # Get the chain
  chain = data.current_chain(continuation)
```

# Transform the chain into dataframe df = pd.DataFrame(index = chain) for contract in chain: df.loc[contract, 'future'] = contract df.loc[contract, 'expiration\_date'] = contract.expiration\_date

Next we locate the contract closest to our target date. As the default setting here is to trade 12 months out, we're looking for a contract expiring in one year. While it is quite probable that we'll find a contract at 12 months out, it is not certain that all markets will have a contract 3 or 9 months out, and therefore this logic to ensure that the model can handle such variations.

closest\_expiration\_date = df.iloc[0].expiration\_date target\_expiration\_date = closest\_expiration\_date + relativedelta(months=+spread\_months) df['days\_to\_target'] = abs(df.expiration\_date - target\_expiration\_date) target\_contract = df.loc[df.days\_to\_target == df.days\_to\_target.min()]

The contract that we located there, target\_contrac t , is the one expiring closest to what we're looking for. The logic above first checks what exact date it is X months from the front contract expiry, where X is 12 by default. Then we make a column for all contracts in the chain showing how many days difference they have to that target date. Finally, we pick the contract with the least difference.

Now we need to get the last closing prices for the front contract as well as the target contract, and calculate the annualized carry.

```
# Get prices for front contract and target contract
prices = data.current(
  [
     df.index[0],
     target_contract.index[0]
  ],
  'close'
)
```

# Check the exact day difference between the contracts days\_to\_front = int( (target\_contract.expiration\_date - closest\_expiration\_date)[0].days )

# Calculate the annualized carry annualized\_carry = (np.power(

```
(prices[0] / prices[1]), (365 / days_to_front))
) - 1
```

If you've paid attention so far in the book, you may have noticed that the formula for calculating annualized yield is a little familiar. It is of course the same logic as we used to calculate annualized momentum scores in chapter 12.

Now we have the data that we need to populate that **DataFrame** we created at the start. In order to compare all the markets, and pick the most attractive carry situations, we need to know which one is the front contract, which is the target contract, and what the annualized carry is.

```
carry_df.loc[continuation, 'front'] = df.iloc[0].future
carry_df.loc[continuation, 'next'] = target_contract.index[0]
carry_df.loc[continuation, 'carry'] = annualized_carry
```

Now sort them, and get rid of any potentially empty rows.

```
# Sort on carry
carry_df.sort_values('carry', inplace=True, ascending=False)
carry_df.dropna(inplace=True)
```

This **DataFrame** object, called carry\_df in the code, now holds the analytics we need to decide what to trade. Now we can start by picking the top and bottom five contracts, the ones we should be long and short.

```
# Contract Selection
for i in np.arange(0, pos_per_side):
  j = -(i+1)
```

# Buy top, short bottom long\_contract = carry\_df.iloc[i].next short\_contract = carry\_df.iloc[j].next

```
new_longs.append(long_contract)
new_shorts.append(short_contract)
```

What this code does is to loop through the numbers 0 through 4, picking five contracts from the top and five from the bottom of the deck. Now that we know which contracts we want to be long and

which we want to be short, all we need to do is to figure out how much of each to trade and then execute.

In order to figure this out, we need to pull some historical data. As we said earlier, we are going to limit our orders to 25% of average daily volume, so obviously we need to know what the average daily volume is.

```
# Get data for the new portfolio
new_portfolio = new_longs + new_shorts
hist = data.history(new_portfolio, fields=['close','volume'],
  frequency='1d',
  bar_count=10,
  )
```

We also said we are doing an equal weighted allocation. If you are inclined to tinkering, the allocation part is something you may want to work further with on your own.

```
# Simple Equal Weighted
target_weight = (
  target_exposure_per_side * context.portfolio.portfolio_value
  ) / pos_per_side
```

At this point, we are all set to loop through the markets which we want to hold for the next week. Here's what we're going to do. For each market, we calculate target contracts to hold, enforce a limit based on the average volume and execute.

```
# Trading
for contract in new_portfolio:
  # Slice history for contract
  h = hist.xs(contract, 2)
```

```
# Equal weighted, with volume based cap.
contracts_to_trade = target_weight / \
  contract.price_multiplier / \
  h.close[-1]
```

```
# Position size cap
contracts_cap = int(h['volume'].mean() * volume_order_cap)
```

# Limit trade size to position size cap. contracts\_to\_trade = min(contracts\_to\_trade, contracts\_cap) # Negative position for shorts if contract in new\_shorts: contracts\_to\_trade \*= -1

# Execute order\_target(contract, contracts\_to\_trade)

That leaves only one final part of housekeeping. Can you think of what we didn't do yet?

We analyzed the markets, we selected contracts, we constructed a new portfolio, calculated position sizes and we traded. But we didn't close the old positions yet. The only thing that's left is to loop through all open positions, and close those that are not part of next week's portfolio.

# Close any other open position for pos in context.portfolio.positions: if pos not in new\_portfolio: order\_target(pos, 0.0)

As with the previous models, I will show the complete model code used here below. As you will see, I used the dynamically updating chart during the simulation run, as we have seen earlier. This time, I added a drawdown chart, just to show how that is done.

%matplotlib notebook

import zipline from zipline.api import future\_symbol, \ set\_commission, set\_slippage, schedule\_function, \ date\_rules, time\_rules, continuous\_future, order\_target

from datetime import datetime import pytz import matplotlib.pyplot as plt import pyfolio as pf import pandas as pd import numpy as np

from zipline.finance.commission import PerTrade, PerContract from zipline.finance.slippage import FixedSlippage, VolatilityVolumeShare

# We'll use this to find a future date, X months out.

from dateutil.relativedelta import relativedelta

```
# settings
spread_months = 12
pos_per_side = 5
target_exposure_per_side = 1.5
initial_portfolio_millions = 1
volume_order_cap = 0.25
```

# DataFame for storing and updating the data that we want to graph dynamic\_results = pd.DataFrame()

```
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(211)
ax.set_title('Curve Trading')
ax2 = fig.add_subplot(212)
ax2.set_title('Drawdown')
```

```
def initialize(context):
  """
```

```
Friction Settings
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
set_slippage(us_futures=slippage_model)
```

```
"""
Markets to trade
"""
most_liquid_commods = [
  'CL','HO','RB','NG','GC','LC','_C','_S','_W','SB', 'HG', 'CT', 'KC'
]
```

```
context.universe = [
  continuous_future(market, offset=0, roll='volume', adjustment='mul')
```

for market in most\_liquid\_commods ]

schedule\_function(weekly\_trade, date\_rules.week\_start(), time\_rules.market\_close())

schedule\_function(update\_chart,date\_rules.month\_start(), time\_rules.market\_close())

def update\_chart(context,data): # This function continuously update the graph during the backtest today = data.current\_session.date() pv = context.portfolio.portfolio\_value exp = context.portfolio.positions\_exposure

dynamic\_results.loc[today, 'PortfolioValue'] = pv

drawdown = (pv / dynamic\_results['PortfolioValue'].max()) - 1 exposure = exp / pv dynamic\_results.loc[today, 'Drawdown'] = drawdown

if ax.lines:

```
ax.lines[0].set_xdata(dynamic_results.index)
  ax.lines[0].set_ydata(dynamic_results.PortfolioValue)
  ax2.lines[0].set_xdata(dynamic_results.index)
  ax2.lines[0].set_ydata(dynamic_results.Drawdown)
else:
  ax.plot(dynamic_results.PortfolioValue)
```

ax2.plot(dynamic\_results.Drawdown)

```
ax.set_ylim(
  dynamic_results.PortfolioValue.min(),
  dynamic_results.PortfolioValue.max()
)
ax.set_xlim(
  dynamic_results.index.min(),
  dynamic_results.index.max()
)
ax2.set_ylim(
  dynamic_results.Drawdown.min(),
  dynamic_results.Drawdown.max()
)
ax2.set_xlim(
  dynamic_results.index.min(),
  dynamic_results.index.max()
)
```

fig.canvas.draw()

```
def weekly_trade(context, data):
  # Empty DataFrame to be filled in later.
  carry_df = pd.DataFrame(index = context.universe)
  for continuation in context.universe:
     # Get the chain
     chain = data.current_chain(continuation)
     # Transform the chain into dataframe
     df = pd.DataFrame(index = chain)
     for contract in chain:
       df.loc[contract, 'future'] = contract
       df.loc[contract, 'expiration_date'] = contract.expiration_date
     # Locate the contract closest to the target date.
     # X months out from the front contract.
     closest_expiration_date = df.iloc[0].expiration_date
     target_expiration_date = closest_expiration_date + relativedelta(months=+spread_months)
     df['days_to_target'] = abs(df.expiration_date - target_expiration_date)
     target_contract = df.loc[df.days_to_target == df.days_to_target.min()]
```

```
# Get prices for front contract and target contract
prices = data.current(
  [
     df.index[0],
     target_contract.index[0]
  ],
  'close'
)
```

```
# Check the exact day difference between the contracts
days_to_front = int(
  (target_contract.expiration_date - closest_expiration_date)[0].days
)
```

```
# Calculate the annualized carry
annualized_carry = (np.power(
            (prices[0] / prices[1]), (365 / days_to_front))
            ) - 1
```

```
carry_df.loc[continuation, 'front'] = df.iloc[0].future
carry_df.loc[continuation, 'next'] = target_contract.index[0]
carry_df.loc[continuation, 'carry'] = annualized_carry
```

# Sort on carry carry\_df.sort\_values('carry', inplace=True, ascending=False) carry\_df.dropna(inplace=True)

new\_portfolio = [] new\_longs = [] new\_shorts = []

# Contract Selection for i in np.arange(0, pos\_per\_side): j = -(i+1)

# Buy top, short bottom long\_contract = carry\_df.iloc[i].next short\_contract = carry\_df.iloc[j].next

```
new_longs.append(long_contract)
new_shorts.append(short_contract)
```

```
# Get data for the new portfolio
new_portfolio = new_longs + new_shorts
hist = data.history(new_portfolio, fields=['close','volume'],
  frequency='1d',
  bar_count=10,
  )
```

```
# Simple Equal Weighted
target_weight = (
  target_exposure_per_side * context.portfolio.portfolio_value
  ) / pos_per_side
```

# Trading for contract in new\_portfolio: # Slice history for contract h = hist.xs(contract, 2)

```
# Equal weighted, with volume based cap.
contracts_to_trade = target_weight / \
  contract.price_multiplier / \
  h.close[-1]
```

```
# Position size cap
contracts_cap = int(h['volume'].mean() * volume_order_cap)
```

# Limit trade size to position size cap. contracts\_to\_trade = min(contracts\_to\_trade, contracts\_cap)

# Negative position for shorts if contract in new\_shorts: contracts\_to\_trade \*= -1

# Execute order\_target(contract, contracts\_to\_trade)

# Close any other open position for pos in context.portfolio.positions: if pos not in new\_portfolio: order\_target(pos, 0.0)

start = datetime(2001, 1, 1, 8, 15, 12, 0, pytz.UTC) end = datetime(2018, 12, 30, 8, 15, 12, 0, pytz.UTC)

```
perf = zipline.run_algorithm(
  start=start, end=end,
  initialize=initialize,
  capital_base=initial_portfolio_millions * 1000000,
  data_frequency = 'daily',
  bundle='futures' )
```

## **Curve Trading Results**

This is an algorithmic trading model which does not use historical price series. That's rather unusual, and if you are not previously familiar with the concept of term structure or calendar trading, this may seem to be a very weird idea. But as you will see from the backtest results, even a simple implementation like this can actually work fairly well.

Glance through the monthly table first to get a feel for how the strategy behaves over time. For a model with no historical data, no stop losses, no targets, no indicators and simple equal weighting, it's really not all that bad.

*Table 18.3 Curve Trading Monthly Returns*

| Year | Jan  | Feb   | Mar   | Apr  | May   | Jun  | Jul   | Aug   | Sep   | Oct   | Nov  | Dec  | Year  |
|------|------|-------|-------|------|-------|------|-------|-------|-------|-------|------|------|-------|
| 2001 | +4.2 | +1.4  | +5.8  | +2.5 | +2.7  | +2.5 | -3.0  | +7.7  | -3.1  | -7.0  | -2.3 | -0.1 | +10.7 |
| 2002 | +0.6 | +3.0  | -6.0  | +6.1 | -2.1  | -1.0 | +4.1  | +0.8  | +0.9  | -3.7  | -2.6 | +2.2 | +1.7  |
| 2003 | +5.1 | +11.4 | -5.5  | -1.5 | +5.6  | +0.3 | -0.8  | -3.8  | +0.3  | -0.3  | -2.0 | +0.1 | +8.1  |
| 2004 | -4.2 | +4.2  | -0.3  | +5.3 | -0.5  | +3.1 | +15.3 | -2.1  | +12.9 | +11.7 | -2.0 | -5.7 | +41.2 |
| 2005 | +5.7 | -0.6  | +10.6 | -0.2 | +3.5  | +4.5 | +0.5  | +6.0  | +4.3  | -0.2  | +7.3 | +1.2 | +51.1 |
| 2006 | -1.6 | +0.4  | +3.1  | +3.1 | -1.2  | +7.5 | -1.5  | -4.7  | -0.7  | -1.9  | +1.2 | +1.0 | +4.2  |
| 2007 | +1.2 | +2.5  | +1.1  | +4.8 | -2.6  | +0.4 | -1.6  | +5.3  | +1.9  | +5.1  | +2.2 | +2.0 | +24.2 |
| 2008 | -1.0 | +3.8  | +5.2  | +2.7 | +15.2 | -1.1 | -11.4 | -4.5  | +5.9  | -6.8  | +8.9 | +9.7 | +26.3 |
| 2009 | +5.9 | +6.0  | -5.4  | +0.1 | -6.7  | +1.2 | +1.6  | +10.5 | -1.3  | -4.8  | +0.8 | +0.8 | +7.3  |
| 2010 | +6.4 | -3.0  | +0.4  | -1.6 | +6.0  | +3.0 | -8.3  | +6.8  | +7.9  | +14.3 | -5.2 | +6.6 | +36.1 |
| 2011 | +4.2 | +2.5  | +0.3  | -2.9 | +0.5  | +6.6 | +3.6  | +1.2  | +0.0  | +2.8  | +0.0 | +3.0 | +23.9 |
| 2012 | +0.3 | +6.4  | +3.4  | +1.5 | -6.5  | +5.7 | +1.6  | +1.6  | -3.3  | +1.2  | +3.1 | -0.1 | +15.2 |
| 2013 | +2.2 | -2.0  | +1.7  | -0.8 | +3.7  | +2.3 | +3.5  | +2.0  | -2.1  | +1.4  | +0.0 | +1.2 | +13.6 |
| 2014 | +0.2 | -8.4  | -3.1  | -2.5 | +6.8  | +2.6 | -0.5  | -1.5  | +5.8  | -13.5 | -2.9 | +1.4 | -16.1 |
| 2015 | -1.2 | +0.0  | +6.7  | -1.8 | +2.9  | -5.6 | +4.8  | +3.0  | -0.8  | +3.1  | +0.0 | +7.3 | +19.4 |
| 2016 | -3.9 | +2.9  | -3.3  | -8.5 | -3.6  | +1.2 | +8.3  | -4.3  | -0.3  | -1.5  | +2.0 | -3.5 | -14.5 |
| 2017 | -0.5 | +0.9  | +0.4  | +4.7 | -2.3  | -1.5 | -4.6  | +5.2  | +0.1  | +7.7  | +4.2 | +4.5 | +19.6 |
| 2018 | +1.6 | +1.1  | +4.4  | +3.1 | +3.7  | +9.0 | -1.3  | +8.1  | +3.4  | -8.6  | -6.0 | +0.8 | +19.1 |

Looking at the equity curve in Figure 18‑3 you see that it's surprisingly smooth. It shouldn't be surprising however that it shows no discernible correlation to the equity index. This strategy is very much a so called uncorrelated strategy. That term is thrown around a lot in the industry, and refers to strategies which are at least in theory uncorrelated to the equity markets.

![](_page_20_Figure_0.jpeg)

*Figure 18*‑*3 Curve Trading Returns*

Table 18.4 shows the holding period returns, or what your percentage return would have looked like if you started this strategy by the beginning of a given year, and held for a certain number of years. What you see here are fairly good long term numbers for most starting points. Even picking the worst possible starting years, you see how recovery does not take too long, and soon surpasses traditional investment approaches.

| Years | 1  | 2 | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|-------|----|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 2001  | 11 | 6 | 7  | 14 | 21 | 18 | 19 | 20 | 18 | 20 | 20 | 20 | 19 | 16 | 17 | 14 | 15 | 15 |
| 2002  | 2  | 5 | 16 | 24 | 20 | 20 | 21 | 19 | 21 | 21 | 21 | 20 | 17 | 17 | 15 | 15 | 15 |    |
|       |    |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

*Table 18.4 Holding Period Returns - Curve Trading*

| 2003 | 8   | 24 | 32 | 25 | 24 | 25 | 22 | 24 | 24 | 23 | 22 | 18 | 18 | 16 | 16 | 16 |  |
|------|-----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|--|
| 2004 | 41  | 46 | 31 | 29 | 28 | 25 | 26 | 26 | 25 | 24 | 19 | 19 | 16 | 16 | 17 |    |  |
| 2005 | 51  | 25 | 25 | 25 | 22 | 24 | 24 | 23 | 22 | 17 | 17 | 14 | 15 | 15 |    |    |  |
| 2006 | 4   | 14 | 18 | 15 | 19 | 20 | 19 | 18 | 14 | 15 | 12 | 12 | 13 |    |    |    |  |
| 2007 | 24  | 25 | 19 | 23 | 23 | 22 | 21 | 15 | 16 | 12 | 13 | 13 |    |    |    |    |  |
| 2008 | 26  | 16 | 23 | 23 | 21 | 20 | 14 | 15 | 11 | 12 | 12 |    |    |    |    |    |  |
| 2009 | 7   | 21 | 22 | 20 | 19 | 12 | 13 | 9  | 10 | 11 |    |    |    |    |    |    |  |
| 2010 | 36  | 30 | 25 | 22 | 13 | 14 | 10 | 11 | 12 |    |    |    |    |    |    |    |  |
| 2011 | 24  | 19 | 17 | 8  | 10 | 6  | 8  | 9  |    |    |    |    |    |    |    |    |  |
| 2012 | 15  | 14 | 3  | 7  | 2  | 5  | 7  |    |    |    |    |    |    |    |    |    |  |
| 2013 | 14  | -2 | 4  | -1 | 3  | 6  |    |    |    |    |    |    |    |    |    |    |  |
| 2014 | -16 | 0  | -5 | 1  | 4  |    |    |    |    |    |    |    |    |    |    |    |  |
| 2015 | 19  | 1  | 7  | 10 |    |    |    |    |    |    |    |    |    |    |    |    |  |
| 2016 | -14 | 1  | 7  |    |    |    |    |    |    |    |    |    |    |    |    |    |  |
| 2017 | 20  | 19 |    |    |    |    |    |    |    |    |    |    |    |    |    |    |  |
| 2018 | 19  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |  |

### **Model Considerations**

It can't be overly stressed that this model is highly sensitive to liquidity. As you have seen in the source code for this model, only a single million was used as basis for trading. That's an exceedingly small amount to trade futures models with, but this is a type of model where you have a small guy advantage. It's possible to grind out quite high returns with lower capital deployments, but the game changes dramatically if you want to trade nine figures.

I do realize of course than many readers balk at my assortment that a million is a tiny bit of money. Of course it's an enormous amount of money, out in the real world. But as far as professional futures trading goes, it's really not much.

This model can be scaled up and down a bit. It can be traded with a bit less, and with a bit more, and still show interesting returns. But serious institutional size money would struggle.

This model implementation here is highly simple, again to teach a concept and demonstrate a way of approaching algorithmic

modelling. The source code made available to you here should enable you to experiment with your own versions of it, adapting and improving based on your own situation and requirements.

Generally speaking, you will find a bit better liquidity closer on the curve, to the left side. This implementation trades 12 months out, and there is usually quite limited trading there. If you trade for instance three months out, you will find a little better liquidity. Your slippage assumptions and preferences on how aggressive you want to trade will greatly impact your results.

Be careful with your modelling here. It would be very easy to change a couple of numbers in the code, and end up with a 50 percent per year or more return. But a simulation is only as good as the assumptions that go into it, and you are not likely to realize such returns in live trading.

Another area of research would be to look at combining this term structure information with other analytics. The approach shown here is purely looking at the implied yield, or cost of carry, but there is no reason why your models would need to be so pure in real life. Yes, I'm just going to throw that out there and let you do the homework.
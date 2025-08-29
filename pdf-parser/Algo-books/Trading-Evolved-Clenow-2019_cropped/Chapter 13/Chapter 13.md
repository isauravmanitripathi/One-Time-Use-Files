# **Futures Modeling and Backtesting**

Backtesting strategies for equities and for futures are two very different things. Even if your high level, conceptual trading rules are similar, the model logic and code are by necessity not. The most important difference comes from the fact that futures contracts have a limited life span. This has multiple implications. The most obvious one being that we have to keep track of which exact contract delivery to trade, and when to switch to another one. But that's just scratching the surface of this issue.

Technically speaking, we don't have long term time series in futures world. Any given futures contract has a limited life span and only has sufficient liquidity to matter for a few months at the most. Quantitative trading models however usually need to rely on a substantially longer time series to analyze. Take something as simple as a long-term moving average. It just is not possible to calculate, using actual market data.

As an example, look at Figure 14‑1, which shows the price and open interest of the February 2003 crude oil futures contract. Remember that open interest tells you how many futures contracts are open at the moment. When you buy a contract, that number goes up by one. When you sell it again, the number goes down by one. This is a good indication of how liquid a contract is.

This contract started trading, or at least was possible to trade from the fall of 2000, but as you can see in the graph, it really had no trading to speak of until late 2002. Even though we have pricing for the contract for years, most of that data is irrelevant. As it was not traded in any meaningful volume, we can't rely on such a price series or draw any conclusions at all from it. The historical data for the contract only becomes interesting when there is enough market participation to ensure proper pricing and sufficient liquidity for actual trading.

![](_page_1_Figure_0.jpeg)

As you see in Figure 14‑1 the contract, February 2003 crude oil, is only really relevant for a very brief period of time. That's how it normally looks. In the next graph, Figure 14‑2, you should get a better view of what is really going on here. This shows five consecutive deliveries of crude oil, for the same time period. Here you can see how the liquidity moves forward, from contract to contract, over time. In the bottom chart pane, you see how the October 2002 holds the most liquidity, but how it slowly gives ground to the November contract. After a month, the November contract fades, and December takes over. This circle will keep repeating, at a fairly predictable pattern.

![](_page_2_Figure_0.jpeg)

*Figure 14*‑*2 Liquidity Moving from Contract to Contract*

It's important to understand that, from an analytics point of view, that each contract only really matters during that brief time that it's the king of the hill, the one with the highest liquidity. That leaves us with a whole lot of short time series, from different contracts, and no long term history.

A surprisingly common rookie mistake is to make a long term time series by simply putting one contract after another. Just using the same time series as they are, and switching between contracts as we go. The problem with this is that this method will create a flawed representation of what actually happened in the market. It will plain

and simply be wrong.

The price of November crude oil and the December crude will be different. It's simply not the same thing, and can't be compared on the same basis. One is for delivery in November and the other for delivery in December. The fair price for these two contracts will always be different.

In Figure 14‑3 you can see how the same underlying asset, in this case still crude oil, is priced differently on the same day, depending on the delivery date. This kind of difference is normal, and it has real world reasons. It has to do with cost of carry, as this represents the hedging cost, and thereby fair pricing. Financing cost and storage cost are major factors here.

![](_page_3_Figure_3.jpeg)

*Figure 14*‑*3 Comparing Contracts*

Some market data vendors still provide time series where the contracts are just put one after another, without any adjustments. Even some of the extremely overpriced market data vendors, those charging around two thousand bucks a month, do this. Just because someone sells you data at a high cost, does not mean that the data is accurate or

useful.

The effect of using a long term time series of contracts simply placed after each other, without adjustment, is the introduction of false gaps. As this so called continuation switches from one contract to another, it will appear as if the market jumped up or down. But no such move actually occurred. If you had been long the first contract, sold it and rolled into the next contract, you wouldn't have experienced the gain or loss of a gap that this flawed continuation would imply.

So be very careful with your data when it comes to long term time series for futures.

### **Continuations**

The most commonly used method of constructing long term futures continuations is to back adjust. What that means is that each time you roll to a new contract, you adjust the entire series back in time. Usually this is done by preserving the ratios. That's to make the percentage moves of the continuation reflect actual percentage moves.

The point with this method is to arrive at a time series which roughly reflects the experience that a real life trader would have had if he had bought and rolled the position, month after month and year after year. Such a continuation is used for long term price analysis, but clearly can't be traded by itself. It's not a real series, it's just constructed for analytical purposes. You can't run a 200 day moving average on a single contract, but you can do it on a properly constructed continuation.

What most backtesting software will do, is to trade this artificially constructed continuation and pretend that it's a real asset. That has been the go-to solution to the futures problem on the retail side for decades, and it's also quite common on the professional side. While that's a good enough solution for most tasks, it does have some

drawbacks.

One issue with this standard approach is that the longer you go back in time, the more the calculated continuation will diverge from the actual market price. If you keep tacking on adjustment after adjustment for a long period of time, you will end up with a price quite far from the market price at the time.

The regular method of making such a continuation means that the entire series is calculated on the day when you run your backtest. That often results in the kind of discrepancies that we see in Figure 14‑4. The solid line on top, the one that spikes up to nearly 700, is the back adjusted series, while the lower one, that never moves much above 100 is the unadjusted series. Neither of these two series can be said to be right, just like neither is really wrong. Depending on your point of view.

The adjusted series is meant to reflect percentage moves that would have been experienced by a trader or investor holding a long exposure over time. But clearly, the price of oil was never up around the 700 mark. This distortion is the effect of adjusting for the basis gap over many years.

![](_page_5_Figure_4.jpeg)

If the purpose with the continuation is to measure the trend for instance, that wouldn't pose much of an issue. This type of purpose is the reason for making a continuation. But the way most retail backtesting software works, the program will assume that the continuation is an actual tradable instrument. It will buy and sell the continuation itself, which clearly is not possible in real life.

That leads to some potential issues. Crude oil futures has a multiplier of 1000, meaning that a price move of one dollar will impact your mark-to-market valuation with 1,000 dollars. This is something that's normally taken into account when deciding position sizes, and can lead some potentially flawed conclusions for smaller portfolios.

Assume for a moment that your backtest is running a portfolio of one million dollars, and that you are targeting a daily variation per position of 0.2%. That is, you want each position to have an approximate daily impact on your portfolio of \$2,000.

The backtest is trying to buy a position in oil, which as mentioned has a point value, or multiplier of 1,000, and which has an average daily price variation of about one percent. Running your backtest on the adjusted series some years back, the adjusted oil price was \$400, and tends to vary by about \$4 per day.

As the contract has a multiplier of 1,000, each contract fluctuates by a value of \$4,000 per day. But we wanted to take a position that fluctuates by \$2,000 per day, and therefore the conclusion is that we are unable to trade. It's simply not granular enough.

But if we look at the actual contract at the time, it was traded around \$40, in unadjusted terms. With a daily change of about one percent, that means that each contract fluctuates by about \$400 per day, and we are able to buy 5 whole contracts.

This is something that you have to be careful with. You could usually find ways to compensate for such issues, but it does mean that

you need keep in mind what kind of distortions are possible and find ways to address them.

Another problematic aspect of using such continuations is that they are not static. The traditional way of using continuation involves recalculating the entire series, adjusting all points back in time when we roll to a new contract. Usually this is done by applying a ratio to the entire existing time series. Stop and think about the implications of that for a moment.

It can have some rather worrying implications. Consider a long term trading model that you constructed a year ago. Back then, you ran a complete backtest of the model, and you were happy with the results. Now, a year later, you run another backtest of the same rules on the same markets. And you find that the results are not the same anymore. This can very well happen, again depending on what analytics you apply on the time series, and whether or not you have taken this phenomenon into account.

A fellow market practitioner who was kind enough to give early comments and suggestions for this book pointed out that I'm being too harsh on the use of continuations, and he is probably right. If you really know what you are doing, and fully understand how your continuations are calculated and the implications of those calculations, you can make sure that your model code does not do anything silly. But I would still maintain that you can achieve a higher level of realism using individual contracts, or with dynamically calculated continuations. And going forward in this book, we will use both.

## **Zipline Continuation Behavior**

If nothing else, the way Zipline handles futures is reason enough to choose this backtester over others. I would like to take some credit for this, as I advised Quantopian a few years ago on how to best handle futures, but I suspect that they were merely humoring me and that they already had plans in this direction.

Their Zipline backtesting engine has a neat solution to the age old continuation issue. The Zipline continuations are generated on the fly, on each day of the backtest. That means that the continuation will look as it would have, if calculated on that day. At each day the backtest processes, the continuations will be freshly generated from that day, so that the 'current' prices in the continuation reflect actual current prices in the market.

The regular, or perhaps we should call it the old school way of calculating a continuation is done in advance, usually as of the real life time that the backtest is performed. Zipline has a clever solution to this, by calculating a continuation each time it's requested in the backtest, based only on data available up until that point in time. The results are more realistic and less prone to errors.

Zipline also solves another common issue relating to continuations. As mentioned, most backtesting solutions available to retail traders will pretend to trade the continuation itself. That's clearly not possible in the real world, as the continuation is no more a real tradable instrument than a moving average. There can be some unexpected implications of simulating trading on the continuation itself, and this can have a real impact on the realism and accuracy of your backtest if you are not careful.

Zipline solves this by trading only actual contracts, just like you would in reality. Clearly this is the better solution, but is also means that you need to provide the backtesting engine with historical data for each individual contract. It could end up to be quite a few of them. For the purposes of this book, I used a database of around twenty thousand individual contracts.

This way of working with futures is far superior to what is normally available to retail traders. It's not only more realistic, but it opens up for brand new possibilities such as calendar spreads or term structure based trading. Yes, I'm just going to throw those words out there and let you think about it for a while.

The flipside is of course that it gets a little more complicated.

We need to feed substantially more data to the backtester. Not just the historical time series data, but also metadata. For each contract, we need to know things like expiry date, last trading date and more.

When building a backtest, we need to keep track of which contract to trade at any given time. And of course, we need to keep track of when it's time to roll to the next contract.

It may sound much more complicated, but it's really not that difficult to set up.

## **Contracts, Continuations and Rolling**

From the equity section of this book, you should already be familiar with how to access data in a Zipline backtest. There are few new things in this regard when it comes to futures, and it has to do with the fact that in futures land, we have to deal with both continuations and individual contracts.

A continuation can be created easily, by providing a root symbol and a few basic settings. The line below shows how to create a continuation for the big S&P 500 futures, root symbol SP.

```
sp_continuation = continuous_future('SP', offset=0, roll='volume', adjustment='mul')
```

With this continuation object, we can then request historical time series, check which contract is currently active, and we can even pull the complete chain of traded contracts, as we will do in later chapters.

You can request the time series history the same way as we did earlier for stocks.

```
continuation_hist = data.history(
  sp_continuation,
  fields=['open','high','low','close'],
  frequency='1d',
```

bar\_count=100,

)

This time series is what would typically be used for analytics. Here we get the adjusted series back in time, using only data available at the time the backtest made the request.

But to be able to trade, we need to get hold of an actual, individual contract. Most, but certainly not all, futures models trade the most active contract. If that's the case, we can just ask the continuation which underlying contract it's using at the moment.

#### contract = data.current(cont, 'contract')

Once we have a contract, placing orders works the same way as we saw earlier for stocks. We can order a set number of contracts, target a fixed notional amount, or target a certain percent exposure.

```
order(contract, 100) # Buys 100 contracts
order_value(contract, 1000000) # Buys a million dollar notional, or closest.
order_target(contract, 10000) # Adjusts current position, if any to 10,000 contracts
order_target_value(contract, 1000000) # Adjust to target a million dollar notional.
order_target_percent(contract, 0.2) # Adjusts current position to target 20% exposure
```

As mentioned previously, the hassle with trading individual contracts is that they have a short life span. It's not just a matter of deciding which one to pick when we enter the position. We also have to keep track of when the contract that we hold is no longer active. At that time, we need to roll to the next contract.

If the intention is to stay with the most active contract, the easiest way is to run a daily check, comparing currently held contracts with the ones that the continuations use at the moment.

```
def roll_futures(context, data):
  open_orders = zipline.api.get_open_orders()
  for held_contract in context.portfolio.positions:
     # don't roll positions that are set to change by core logic
     if held_contract in open_orders:
```

# Make a continuation

continue

```
continuation = continuous_future(
     held_contract.root_symbol,
     offset=0,
     roll='volume',
     adjustment='mul'
     )
```

# Get the current contract of the continuation continuation\_contract = data.current(continuation, 'contract')

if continuation\_contract != held\_contract: # Check how many contracts we hold pos\_size = context.portfolio.positions[held\_contract].amount # Close current position order\_target\_percent(held\_contract, 0.0) # Open new position order\_target(continuation\_contract, pos\_size)

As you will see in the futures models, we will use this code or variations thereof to ensure that we keep rolling the contracts when needed, and stay with the active one.
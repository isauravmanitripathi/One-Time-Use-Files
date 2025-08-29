# **Futures Trend Following**

Some years ago I wrote a book called *Following the Trend* (Clenow, Following the Trend, 2013). In that book I presented a rather standard trend following model, which I used to explain what trend following is and how it works. I demonstrated that the bulk of the returns from the managed futures industry can be explained by a very simple trend following model. In retrospect, my only regret is not making the demonstration model even simpler.

I wanted to include various features in the model to demonstrate how they work and what impact they can have. Had I kept the model rules even simpler, I might have been able to avoid the occasional misunderstanding that this model was some sort of *Secret Trend Following Super System* .

The rules I presented were not exactly secret, as they had been known for decades prior to my book. What I attempted to do was to explain it in a hopefully new way and give people outside of our industry a feeling for what it is that we do for a living. There are far too many inaccurate myths around the business.

Later in this book, I will correct that mistake by presenting an incredibly simple trend following model. One that rightfully should shock people. It sounds so dumb that most would dismiss it out of hand. But it still shows pretty good returns in a backtest.

But I would assume that people who read my first book want to know what is going on with the Core Model, as I called it in that book. It's fair to ask if those rules have worked out, or if they crashed and burned. The short story is that the approach did just fine.

I suspect that many of the readers of this book also read the first one. Still, I don't want to assume that all of you did, so I will be sure to include enough information here that you are not forced to go buy the other book. I'm not going to repeat the entire thing of course,

but I will try to repeat as much as is needed to follow the lessons of this book.

The model from *Following the Trend* had quite an interesting ride. As it turns out, my book was published just as a few rough years for trend following started. The last year covered in the book was 2011, which was a generally poor year for trend following strategies. Of course, 2012 and 2013 were also quite poor years for trend models.

Every time trend following has a bad year or two, there are pundits coming out of the woodwork to declare the strategy dead. It really does not matter how many times this happens and how many times they are wrong.

The thing is that trend following, like every other strategy, has good years and bad years. If you find a strategy that has not had a poor run, there is probably something that you overlooked. The only person who never had trading losses is Bernie M.

But then came the great 2014, when trend following did really well. The losses of the past three years wiped out and brand new alltime highs made. It was a really good year and the people who called the end of trend following were nowhere to be seen.

With trend following, you always need to keep in mind that it's a long term strategy. You might see several years in a row of losses, just as you will in most strategies. This is the reason why you should trade in reasonable size. Sooner or later, any strategy will have a couple of consecutive losing years.

Every time trend following has a few bad years, a lot of players get shaken out. Those who stay the course have always been rewarded in the long run.

## **Principles of Trend Following**

The idea of trend following is really quite simple. Most robust

trading ideas are quite simple. This of course does not mean that it's simple to implement, simple to make money from or even necessarily simple to code. Simple, means that the idea itself is simple. The concept is easily understood and explained.

This is something worth considering when you design a strategy. If you are unable to explain the idea behind your trading strategy in a simple, brief and understandable manner, then there is a clear risk that you have overcomplicated and over fitted rules to match data, and that there is little to no predictive value.

Trend following is based on the empirical observation that prices often move in the same direction for a sustained period of time. The strategy aims to capture the bulk of such moves, while not attempting in any way to time valleys or peaks. It simply waits for prices to start moving in a certain direction, and then jumps onboard in the same direction, attempting to ride the trend. Most commonly, a trailing stop loss is employed, meaning that we wait until the market starts moving against us before exiting.

Trend following trades fail most of the time. But that's ok. Trend following tends to have a fairly large amount of losing trades, often as high as 70 percent. It's not a strategy for those who like to be proven right all the time. What is important however is the long term value development of the portfolio as a whole. Trend following tends to have a large amount of small losses, and a small amount of large gains. As long as the net expected value of this works out to a positive number, we are all good.

There are myriads of methods to choose from when designing and implementing a trend following model. If you get the fifty best trend following traders together to spill their secrets, most likely they will have fifty very different set of rules. But as I demonstrated in *Following the Trend* , the bulk of trend following returns can be explained by very simple rules.

In that book, I showed how an extremely simple rule set has very high correlation to the returns of the world's leading trend

following hedge funds. I did not do that to diminish the impressive work of any of these people. I did it to explain trend following as a phenomenon, and educate readers on where the returns come from and potentially how to go about replicating it.

Trend following can in practice be a very frustrating strategy to trade. You will always enter late into a breakout, buying after the price has already rallied. Quite often, the price simply falls right back down after you enter, resulting in a swift loss. When the price does take off and trend for you, the trailing stop logic ensures that you will always lose money from the peak reading of your position, until the stop is hit. And of course, sometimes, trend following simply does not work very well for a year, or even several years.

Well, all of that is just part of the cost of doing business in the trend following field. It's not for everyone. It's not an amazing nolose, get-rich-quick strategy that everyone should bet all of their money on. But it is a strategy which has empirically performed remarkably well for decades.

## **Revisiting the Core Trend Model**

The Core model that I presented some years ago in *Following the Trend* aims to capture medium term trends across all market sectors. It's a very deliberate middle-of-the-road type of model. There is nothing particularly remarkable about this model. The fact that it's not only profitable, but quite handsomely profitable is what is remarkable. The fact that the return stream is very highly correlated to the trend following hedge funds of the world is what should catch your attention here.

What this should tell you is that the bulk of trend following returns can be captured with quite simplistic models. Constructing a simulation that performs similarly to some of the world's best hedge funds is not all that hard. Implementing is of course a different story, but for now we are focusing on the modelling.

Constructing a basic trend model like this is a good exercise, in part to learn how to write the code but even more importantly to understand the core logic of trend following.

## **Model Purpose**

The idea with the core trend model is to guarantee participation in any medium to long term trend across all the major futures sectors.

There has been much mystique around trend following and a great deal of people without industry background were making money selling system rules to gullible retail traders. I wanted to introduce you to the man behind the curtain.

But don't mistake the simplicity of the rules for a recipe to get rich quick. Understanding trend following and successfully implementing it are two very different things. For one thing, the proverbial devil tends to be in the details. While you can replicate the bulk of trend following returns with simple rules, you may require added complexity to control volatility, maintain acceptable risk and to develop a strategy that can be successfully marketed and funded.

Then of course there is the pesky little detail of capital requirements. In *Following the Trend* , I argued that you need an account size of at least a million dollars to implement a diversified trend following model. That's probably the sentence in that book that generated the most emails. I can't even begin to count how many people sent me email asking if it could be done with a much smaller account size.

I will be generous here and say that perhaps you can do it on half that account size. Perhaps. I will even concede that you could, in theory, do it on a lot less by simply pretending to have the money.

Yes, pretending. When you trade futures models, you don't actually need to put up all of the cash, as you would for equity trading.

So in theory, you could have an account of a hundred thousand dollars and simply pretend that you have a million. Trade it as if the base account size is a full million.

But that would be a very bad idea. A drawdown of ten percent would wipe you out.

This is the problem with trading diversified futures models. That they require quite a large account size. This stems from the fact that most futures contracts are quite large. While you can buy a single stock for a few bucks, the notional exposure on a futures contract can be in the tens or hundreds of thousands.

Even if you don't currently have a million dollars on your account, or have realistic plans of acquiring it in the next few hours, you can still benefit from understanding trend following. So please don't stop reading just yet. After all, you have already paid for this book.

#### **Investment Universe**

All else being equal, a large investment universe usually helps the end results. It can be difficult to trade and manage a large universe, but in practice it's the best way to go. That's why you need to take great care when you start cutting down the universe to fit what you are able to trade.

We will use about forty markets in this demonstration. This investment universe covers agricultural commodities, metals, energies, equities, currencies, fixed income and money markets. I will use only USD denominated markets. Not because that's somehow better, because it really is not. Clearly there are more interesting markets trading in USD than in any other currency, but there is a clear benefit in including international markets. It can greatly help with diversification and improve long term results.

No, the reason for only using dollar based futures markets here is that the backtester used for demonstration in this book, Zipline, does not yet support international futures. There is no mechanism to take the currency effects into account.

With futures this is much less of an issue than with stocks. When dealing with international futures, you don't have an open currency exposure on the notional amount. The face value of your contract in a foreign currency is not impacting your currency exposure. Remember that you haven't actually paid for this contract, as you do with stocks. You just have a margin requirement.

## **Trading Frequency**

The model operates on daily data and checks every day for trading signals. There may not be anything to trade each day, but we check to make sure on a daily basis. No action is taken intraday, and no stop orders are placed in the market. All logic operates on closing prices, and trading always occurs a day after the signal.

Note that two separate tasks are performed each day. First we check if any position should be closed or opened. After that, we check if any position should be rolled. The roll logic and reason for it are all explained in chapter 14.

## **Position Allocation**

The position sizes taken for this model aim to take an equal amount of risk per position. And no, risk has nothing at all to do with how much money you lose if your stop loss point is triggered. That's unfortunately a common explanation of risk found in many trading books, but it has really nothing to do with risk as the word is used in the finance industry.

Risk is somewhat controversial word inside the business as well. In this context I'm using a slightly simplified but still valid definition, based on expected average daily profit or loss impact.

Since we have really no reason to believe that one position is more important or will be more profitable than another, this model aims to put more or less the same risk in each position. The first and obvious thing to point out is that we can't simply buy an equal amount of each. That does not even work for reasonably similar instruments like stocks. Futures can show extreme differences in how they move, and if you hold an equal amount of each you would have a highly skewed risk.

For some markets, like oil for instance, a 3% moves in a day happens quite often. These days, you barely see a headline in the news about such a move. It's just too common. But for the US 10 year treasury futures to move 3% in a day, it would take a cataclysmic event. If you placed \$100,000 in each, you would clearly have significantly more risk on the oil position than the treasury position.

A common method of solving this is to look at recent volatility for each market, and scale positions based on that. Daily volatility being a far proxy for risk in this context.

What we want to achieve is to have an approximate equal daily impact on the overall portfolio from each position. We are simply trying to give every position an equal vote. The same ability to impact the overall portfolio profit and loss bottom line.

Volatility can be measured in many ways. In *Following the Trend* , I used Average True Range (ATR) as a measurement of how much a market tends to move up and down on an average day. As I'm always in favor of expanding one's toolkit, I'm going to use a different measurement here.

Please don't email me to ask which is best, because that would be missing the point. I'm not the guy who will give you exact instructions on how to do things the best way. Mostly because I find

that type of advice detrimental, at best. I want to help you built a skill set and an understanding of various types of methods and tools. A foundation which you can build upon and actually learn how methods work, how to incorporate them into your trading ideas and hopefully how to construct your own tools.

Instead of using ATR, this time around I'm going to use standard deviation. Not the usual annualized standard deviation in percent, but rather standard deviation of price changes. It's a measurement not all that different from ATR. As it uses only closing prices, we will have a little less data to bother with, and a little simpler logic. The standard deviation here is calculated based on the daily dollar and cent changes from day to day, over a span of 40 days. Note that we are talking about price changes, not price. Using a standard deviation of the actual price levels would produce a rather nonsensical result in this context. 40 days here, roughly measures the past two months' volatility. Feel free to experiment with other settings.

Lucky for us, calculating standard deviation of price changes is really simple in Python. You can do it in a single line, if you like. The code below is all that you need to calculate the standard deviation of price changes for the past two months, assuming you have a DataFram e with a column called clos e .

#### std\_dev = df.close.diff()[-40:].std()

Let's break that row down to its parts, to make sure you understand what is going on here. The variable d f here is a **DataFrame** with a column called clos e . The first part of the statement simply gets the day by day changes, by using the function diff( ) . That by itself just gives us another time series, with the difference between each day.

After that, we slice off the last 40 days, and request a standard deviation calculation based on that, with the built in function .std( ) . Now try replicating this one line of code in your other favorite programming language, and you will quickly see just how much simpler Python can be.

Suppose that we would like each position in the portfolio to have an average daily impact equivalent to 0.2% of the entire portfolio value. The number 0.2% in this example, is referred to as a risk factor. This is a completely arbitrary number which we can toggle up or down to increase or decrease risk. It's our primary risk guidance tool for the demo model in this chapter.

Here is the formula we would apply to calculate the volatility based position size.

This formula assumes that everything is in the same currency. If you are dealing with international futures, you also need to translate foreign currencies to your base currency.

Suppose that we have a portfolio with a total balance of \$5,000,000 and we would like to apply a risk factor of 20 basis points. The expression basis points in this context refers to fractions of a percent, so 20 basis points is the same as 0.2%. We are now about to buy crude oil, which in our example is currently trading at \$43.62 and has a 40 day standard deviation of \$1.63. Here is our formula.

In this case, we end up buying only 6 contracts, for a portfolio of 5 million dollars. Well, I already warned you that this might not be the exact rules you will be implementing. Stay with me. This model is meant to teach you how things work.

What is key at the moment is that you understand the logic

behind this type of position sizing. The idea being that in this case, we want every position to have a daily average impact on the portfolio of about \$10,000, and from there we will figure out how many contracts we need to trade.

There are alternative ways to do volatility parity allocation, which is the fancy pants name for what we are really doing here. The other methods you may have in mind are probably fine a well. But the concept is important.

The code for the position size calculation can be found below. Inputs are current portfolio mark-to-market value, standard deviation and point value. The risk factor is already defined in the settings section of the model, as you'll see in the complete code later on. Output is number of contracts that we should trade.

```
def position_size(portfolio_value, std, point_value):
  target_variation = portfolio_value * risk_factor
  contract_variation = std * point_value
  contracts = target_variation / contract_variation
  return int(np.nan_to_num(contracts))Trend Filter
```

A good old dual moving average is used for this model, but not for trend signals. Instead, this is used as a filter to determine the trend direction.

We are using a combination of a 40 day exponential moving average and a longer one of 80 days. If the 40 day average is higher than the 80 day average, we determine that the trend direction is positive. If it's the other way around, with the faster EMA lower than the slower, we will call the trend negative.

This by itself does not trigger any trades. We will just use it as a filter. We will only take long entry signals if the trend is positive, and conversely we will only take short entry signals if the trend is negative.

In case you are wondering why the numbers 40 and 80 were selected, the answer is, perhaps not too unexpectedly at this point that they were picked rather frivolously. These numbers are reasonable, as

are many others. Feel free to try other combinations. Just keep in mind the general purpose, of determining if the market is moving up or down at the moment.

You may also wonder why an exponential moving average was selected, instead of a regular simple moving average. The primary motivation for selecting that here is to show you how to an exponential moving average is calculated using Python.

Figure 15‑1 demonstrate the idea of this trend filter. As the faster EMA is higher, the trend is deemed to be positive, else negative.

![](_page_11_Figure_3.jpeg)

### **Entry Rules**

The trading rules for this model are symmetrical. That means that we are treating the long and short side equally, simply reversing the sign for the trading logic.

That might not be the best way to trade. Bullish trends and bearish trends tend to behave quite differently and may require different parameter sets. But for now, we will keep the model simple and straight forward.

Entry rules are based on simple breakout logic. When a market hits a new 50 day extreme in the direction of the trend, we will enter.

For a long entry, we first require the trend filter to be positive. The 40 day exponential average must be higher than the 80 day equivalent. That means that we have a green light to take long entry signals if and when they come around.

When the price makes a new 50 day high, we enter long on the following day.

To figure out the short entries, simply reverse the logic. If the trend filter is negative, and we get a new 50 day low, we go short.

### **Exit Rules**

This simple trend model uses a trailing stop. That means that the stop moves along with the price, making sure that we don't give back too much after a good run. What we want to do here is aim for a certain amount of giveback of profit.

Keep in mind that we are dealing with a trend following model here. Trend models always give back part of the profit before closing. These models don't aim at buying at the bottom and selling at the top. That's not what trend following is about. Other types of strategies may attempt that, but what we are doing here is quite different. We are looking to buy high and sell higher. Not to buy low and sell high.

For this model, we have no profit target. We want to be in the position as long as possible. We simply stay in the position as long as it keeps moving in our direction. If it makes a significant move against us, we close it down. Naturally, the key word here is *significant* .

Using a percentage loss on the position is not going to help you. Remember that we are dealing with many different markets across many asset classes. The base volatility level will be quite different so you can't compare percentages.

For oil and platinum, a 2% move is not a big deal. It happens all the time. But for the US 2 year treasury futures, that's a huge move. For money markets, it's practically unheard of. No, we need something better than percentages to measure moves. We need to normalize the moves to volatility, so that they can be compared.

Earlier we discussed standard deviation in the context of position sizing. That measurement works fine for use in this context as well. What the standard deviation tells us is approximately how much a market tends to move in a day, on average.

The exit rule here is based on this standard deviation value. From the peak reading of the position, that's at the time of the largest unrealized gain, we let the position lose three times the standard deviation value before closing it.

This is not an intraday stop, placed in the markets. This is a trigger based on daily prices, with the actual trade executed the day after. This just to keep the rules simple and easy to replicate. Most of you can probably source daily data with little to no problem, whereas historical intraday series can get expensive.

There is an added benefit of using a stop level based on standard deviation in this case. Earlier in the example, we used a risk factor of 20 basis points to set the position size. The formula, as explained earlier aims to make the average daily variation of the position impact the portfolio with about 20 basis points.

So if the market moves by one standard deviation, the overall portfolio impact will be 0.2%. And since we now set the stop at three times the standard deviation value, we now know that every position will lose about 0.6% of the portfolio value before it's closed out. That is, lose 60 basis points from the peak reading. That's the amount of

profit we will give back before a position is closed, if there was a profit to give back.

### **Costs and Slippage**

Zipline has quite a complex built-in modeling of cost and slippage, much more so than even most commercial grade solutions. If you dig into the details, you will find a range of highly configurable algorithms for taking these important variables into account. I very much encourage you to try variations, model different assumptions and see how it impacts your results.

For this demo model, I have chosen a slippage model which takes traded volume into account. It will, in this case, make sure that we never trade more than 20% of the daily volume, and model slippage based on that. Of course, this slippage model works even better on intraday data.

For costs, I have set an assumed commission per contract of 0.85 dollar, as well as an exchange fee of 1.5 dollar. Assuming you trade with a low cost online broker, these cost assumptions should be reasonably realistic.

I have left settings in the code, so that you can turn on or off slippage and commissions and experiment with how much of an impact these things have.

## **Interest on Liquidity**

As you should be aware by now, futures are traded on margin. Most professional futures managers tend to hang out in the 10-20 percent margin-to-equity range, and that means that some 80-90 percent of your capital is not actually needed at the moment.

Professional futures managers use that excess cash to buy short

term government paper. There are two reasons for this. The most obvious is that it can earn an interest, while being the very definition of risk free. In the good old days of futures trading, the 80s, 90s and even part of the 00's, this interest could have a substantial impact on the result of the strategy.

And of course, the best part here is that as a hedgie, you get paid a performance fee on the return you generate for your clients. Even if part of that return came from risk free interest. Yep, those were the days.

Unfortunately, these days you get so little return on these instruments that it really has no performance impact. But you still do it. For the other reason.

The other reason has to do with fiduciary responsibility. If your bank or broker goes belly-up overnight, your cash holdings are likely gone. Sure, segregated accounts and so on, but in reality your cash is most likely going poof.

Your securities however are very likely to be returned to you, sooner or later. If you're dealing with a fraud situation, all bets are off, but if it's a regular case of greed, irresponsibility and some run-of-themill corporate corruption, you will likely see your securities returned at some point.

I'm going to keep the simulations simple here, and disregard this part. When deploying futures models in reality, you really do want to look closer at cash management. Both for fiduciary reasons, and for economic reasons.

Properly accounting for the historical impact of cash management, the simulation results would be a little bit higher. Some years, it made a substantial difference, when risk free returns were high.

## **Trend Model Source Code**

The general structure of a Zipline simulation should be familiar to you by now, unless of course you skipped over the equity part of this book. As you will see in this code, the major difference with futures comes down to dealing with the dual concept of continuations versus contracts.

A continuation is a calculated time series, based on time series from individual contracts. Contract after contract are stitched together to form a long term time series, aiming to be as close as possible to the actual price impact of long term holding of the futures market. As we don't have real long term series in the futures space, this is the best we can do to make something that we can run longer term time series analytics on. But you can't trade a continuation. It's just a calculation.

For trading, we need to figure out which contract is the relevant one to trade at the moment. That usually means the most liquid contract. What we do here is to construct a continuation which always uses the most traded contract as the current, and then when trading we ask the continuation to tell us which exact contract it's using at the moment. That's the one we will trade.

As futures contracts have a limited life span, this also means that we need to check every day if any positions need rolling.

The trading logic is not overly complicated. We start off by calculating the trend filter and the volatility measurement. Then we go over each market, one by one. If we already have an open position in a market, we check if either of two possible stop conditions are met. Either if the price moved against us by three times the standard deviation, or if the trend direction flipped.

If there is no position held, we check if there is a new 50 day extreme in the direction of the trend, and if so we trade to open.

As before, I'll show you the key parts of the code bit by bit, with explanations, and in the end of this section you'll get the full source all at once.

At the top, we have various import statements as usual. Much of this should be familiar if you read the equity chapter and studied that code. This time however, there are a few futures specific functionality imported.

%matplotlib inline

| import<br>zipline                                                          |
|----------------------------------------------------------------------------|
| from<br>zipline.api<br>import<br>future_symbol,<br>\                       |
| set_commission,<br>set_slippage,<br>schedule_function,<br>date_rules,<br>\ |
| time_rules,<br>continuous_future,<br>order_target                          |
| from<br>datetime<br>import<br>datetime                                     |
| import<br>pytz                                                             |
| import<br>matplotlib.pyplot<br>as<br>plt                                   |
| import<br>pyfolio<br>as<br>pf                                              |
| import<br>pandas<br>as<br>pd                                               |
| import<br>numpy<br>as<br>np                                                |
| from<br>zipline.finance.commission<br>import<br>PerTrade,<br>PerContract   |
| from<br>zipline.finance.slippage<br>import<br>VolumeShareSlippage,<br>\    |
| FixedSlippage,<br>VolatilityVolumeShare                                    |

In the equity momentum model, we were outputting a lot of text as the model was running, mostly to have something to look at for the minutes it takes to run the backtest. This doesn't affect anything apart from elevating boredom for those of us with short attention span.

In this model, I thought I'd show you another way of doing the same. Following this book's theme of incremental increase in complexity, this time I will show you how to update the text output, without printing a new row each time.

The equity momentum model prints one row per month, resulting in quite a few text lines to scroll down in the end. The approach here will update the same text, dynamically.

First we need to set it up, by importing the required libraries and creating an output variable which we can update during the backtest run.

<sup>#</sup> These lines are for the dynamic text reporting from IPython.display import display import ipywidgets as widgets out = widgets.HTML() display(out)

Now that this is set up, we can dynamically change the output text by setting out.valu e , which we'll do in a separate function as the backtest runs. The function below will be called every day.

We've seen before that the Zipline object called contex t can store just about anything you like for you during the backtest run. In this case, we'll use it to keep track of how many month's we've been trading so far. For this, all we need to do is to set context.months = 0 in initializ e . In the same startup routine, we'll schedule a monthly output report.

# We'll just use this for the progress output # during the backtest. Doesn't impact anything. context.months = 0

```
# Schedule monthly report output
schedule_function(
  func=report_result,
  date_rule=date_rules.month_start(),
  time_rule=time_rules.market_open()
```

The reporting routine itself only has a few lines of code. We update the number of months traded, calculate the annualized return so far, and update the text. That's all that's required to have a dynamic text update while we run the backtest.

```
def report_result(context, data):
  context.months += 1
  today = zipline.api.get_datetime().date()
  # Calculate annualized return so far
  ann_ret = np.power(context.portfolio.portfolio_value / starting_portfolio,
            12 / context.months) - 1
```

# Update the text out.value = """{} We have traded <b>{}</b> months and the annualized return is <b>{:.2%}</b>""".format(today, context.months, ann\_ret)

So far, that's all just import statements and a bit of reporting, but we're getting to the actual model logic. As with the previous models, we have the initializ e routine, where we set up commission, slippage and various other settings. With the equity model earlier, we needed a dynamic investment universe to reflect the stocks that would

realistically have been on your radar in the past. With futures, it gets easier.

Here we just define the markets that we want to trade. It's a valid assumption that you would have picked more or less the same markets ten years ago.

In the equity model in chapter 12, we used a list of **symbol** objects as our investment universe. In Zipline logic, the **symbol** object applies only to stocks. For futures, we instead have two related concepts. We have **future\_symbol** and **continuous\_future** . The former refers to a specific futures contract, while the second refers to a calculated, long term price continuation based on many individual contracts.

As you can see in the initialize below, what we do here is to make a list of **continuous\_future** objects, one for each market.

def initialize(context):

```
"""
Cost Settings
"""
if enable_commission:
  comm_model = PerContract(cost=0.85, exchange_fee=1.5)
else:
  comm_model = PerTrade(cost=0.0)
```

set\_commission(us\_futures=comm\_model)

```
if enable_slippage:
  slippage_model=VolatilityVolumeShare(volume_limit=0.2)
else:
  slippage_model=FixedSlippage(spread=0.0)
```

set\_slippage(us\_futures=slippage\_model)

""" Markets to trade """ currencies = [

| 'AD',<br>'BP',<br>'CD',<br>'CU',<br>'DX',<br>'JY',<br>'NE',<br>'SF', |  |  |
|----------------------------------------------------------------------|--|--|

agricultural = [ 'BL', '\_C', 'CT', 'FC', 'KC', 'LR', 'LS', '\_O', '\_S', 'SB', 'SM', '\_W', ] nonagricultural = [ 'CL', 'GC', 'HG', 'HO', 'LG', 'NG', 'PA', 'PL', 'RB', 'SI', ] equities = [ 'ES', 'NK', 'NQ', 'TW', 'VX', 'YM', ] rates = [ 'ED', 'FV', 'TU', 'TY', 'US',

]

```
# List of all the markets
markets = currencies + agricultural + nonagricultural + equities + rates
```

```
# Make a list of all continuations
context.universe = [
  continuous_future(market, offset=0, roll='volume', adjustment='mul')
     for market in markets
]
```

```
# We'll use these to keep track of best position reading
# Used to calculate stop points.
context.highest_in_position = {market: 0 for market in markets}
context.lowest_in_position = {market: 0 for market in markets}
```

# Schedule the daily trading schedule\_function(daily\_trade, date\_rules.every\_day(), time\_rules.market\_close())

# We'll just use this for the progress output # during the backtest. Doesn't impact anything. context.months = 0

```
# Schedule monthly report output
schedule_function(
  func=report_result,
  date_rule=date_rules.month_start(),
  time_rule=time_rules.market_open()
)
```

We have a few helper functions here, just as we've seen in the equity chapter. There is the logic for checking if any contract needs to be rolled, which was discussed in the previous chapter. The logic for position size was also just explained in the section above on position allocation.

Now, what you're probably more eager to see is the code for the daily trading logic. We start off the daily\_trad e routine by getting about a year's worth of continuous data for all the markets.

```
# Get continuation data
hist = data.history(
  context.universe,
```

```
fields=['close','volume'],
frequency='1d',
bar_count=250,
```

)

Next we'll calculate the trend, and mentioned earlier we're calling bull if the 40 day EMA is higher than the 80 day EMA, as defined in our settings.

# Calculate trend hist['trend'] = hist['close'].ewm(span=fast\_ma).mean() > hist['close'].ewm(span=slow\_ma).mean()

After we have the data and the trend info, we can iterate each market, one by one. When we iterate market by market, we first check if there is a position on or not. If a position is held, we check if it's long or short and run the applicable logic. If a position is not held, we check if there is a bull market or a bear market at the moment, and run the relevant code to see if a position should be opened or not.

Here is it, bit by bit. First we start the loop and prepare the data we need, including a standard deviation calculation.

# Iterate markets, check for trades for continuation in context.universe:

# Get root symbol of continuation root = continuation.root\_symbol

# Slice off history for just this market h = hist.xs(continuation, 2)

# Get standard deviation std = h.close.diff()[-vola\_window:].std()

Then we process long positions.

if root in open\_pos: # Position is open

# Get position p = context.portfolio.positions[open\_pos[root]]

if p.amount > 0: # Position is long if context.highest\_in\_position[root] == 0: # First day holding the position

```
context.highest_in_position[root] = p.cost_basis
else:
  context.highest_in_position[root] = max(
     h['close'].iloc[-1], context.highest_in_position[root]
  )
```

```
# Calculate stop point
stop = context.highest_in_position[root] - (std * stop_distance)
# Check if stop is hit
if h.iloc[-1]['close'] < stop:
  contract = open_pos[root]
  order_target(contract, 0)
  context.highest_in_position[root] = 0
# Check if trend has flipped
elif h['trend'].iloc[-1] == False:
  contract = open_pos[root]
  order_target(contract, 0)
  context.highest_in_position[root] = 0
```

#### Process short positions.

```
else: # Position is short
  if context.lowest_in_position[root] == 0: # First day holding the position
     context.lowest_in_position[root] = p.cost_basis
  else:
     context.lowest_in_position[root] = min(
       h['close'].iloc[-1], context.lowest_in_position[root]
     )
```

```
# Calculate stop point
stop = context.lowest_in_position[root] + (std * stop_distance)
```

```
# Check if stop is hit
if h.iloc[-1]['close'] > stop:
  contract = open_pos[root]
  order_target(contract, 0)
  context.lowest_in_position[root] = 0
# Check if trend has flipped
elif h['trend'].iloc[-1] == True:
  contract = open_pos[root]
  order_target(contract, 0)
  context.lowest_in_position[root] = 0
```

#### If no position is on, we deal with bull market scenario.

else: # No position on if h['trend'].iloc[-1]: # Bull trend # Check if we just made a new high

```
if h['close'][-1] == h[-breakout_window:]['close'].max():
  contract = data.current(continuation, 'contract')
```

```
contracts_to_trade = position_size( \
                       context.portfolio.portfolio_value, \
                       std, \
                       contract.price_multiplier)
```

# Limit size to 20% of avg. daily volume contracts\_cap = int(h['volume'][-20:].mean() \* 0.2) contracts\_to\_trade = min(contracts\_to\_trade, contracts\_cap)

# Place the order order\_target(contract, contracts\_to\_trade)

#### And finally, we deal with bear markets.

```
else: # Bear trend
  # Check if we just made a new low
  if h['close'][-1] == h[-breakout_window:]['close'].min():
     contract = data.current(continuation, 'contract')
     contracts_to_trade = position_size( \
```

```
context.portfolio.portfolio_value, \
std, \
contract.price_multiplier)
```

```
# Limit size to 20% of avg. daily volume
contracts_cap = int(h['volume'][-20:].mean() * 0.2)
contracts_to_trade = min(contracts_to_trade, contracts_cap)
```

```
# Place the order
order_target(contract, -1 * contracts_to_trade)
```

Finally, still in the daily\_trad e routine, if there are positions open, we execute the function to check if anything needs to be rolled. This was explained more in detail in chapter 14.

```
# If we have open positions, check for rolls
if len(open_pos) > 0:
  roll_futures(context, data)
```

As your Python skills should be continuingly improving throughout this book, I will increasingly rely on comments in the code and not explain every line with text. If I did, this book would go from

around 500 pages to the double. I focus instead on explaining new concepts and important segments.

Now that we have looked at the individual parts of the code, you may want to have a look at the complete model code below. As with all other code in this book, you can download it from the book website, **[www.followingthetrend.com/trading-evolved](http://www.followingthetrend.com/python-book)** .

#### %matplotlib inline

import zipline from zipline.api import future\_symbol, \ set\_commission, set\_slippage, schedule\_function, date\_rules, \ time\_rules, continuous\_future, order\_target from datetime import datetime import pytz import matplotlib.pyplot as plt import pyfolio as pf import pandas as pd import numpy as np from zipline.finance.commission import PerTrade, PerContract from zipline.finance.slippage import VolumeShareSlippage, \ FixedSlippage, VolatilityVolumeShare

```
# These lines are for the dynamic text reporting
from IPython.display import display
import ipywidgets as widgets
out = widgets.HTML()
display(out)
```

"""

```
Model Settings
```

```
"""
starting_portfolio = 50000000
risk_factor = 0.0015
stop_distance = 3
breakout_window = 50
vola_window = 40
slow_ma = 80
fast_ma = 40
enable_commission = True
enable_slippage = True
```

```
def report_result(context, data):
  context.months += 1
  today = zipline.api.get_datetime().date()
  # Calculate annualized return so far
```

ann\_ret = np.power(context.portfolio.portfolio\_value / starting\_portfolio, 12 / context.months) - 1

# Update the text out.value = """{} We have traded <b>{}</b> months and the annualized return is <b>{:.2%}</b>""".format(today, context.months, ann\_ret)

def roll\_futures(context, data): open\_orders = zipline.api.get\_open\_orders()

for held\_contract in context.portfolio.positions: # don't roll positions that are set to change by core logic if held\_contract in open\_orders: continue

# Save some time by only checking rolls for # contracts stopping trading in the next days days\_to\_auto\_close = ( held\_contract.auto\_close\_date.date() - data.current\_session.date() ).days if days\_to\_auto\_close > 5: continue

```
# Make a continuation
continuation = continuous_future(
     held_contract.root_symbol,
     offset=0,
     roll='volume',
     adjustment='mul'
     )
```

# Get the current contract of the continuation continuation\_contract = data.current(continuation, 'contract')

if continuation\_contract != held\_contract: # Check how many contracts we hold pos\_size = context.portfolio.positions[held\_contract].amount # Close current position order\_target(held\_contract, 0) # Open new position order\_target(continuation\_contract, pos\_size)

def position\_size(portfolio\_value, std, point\_value): target\_variation = portfolio\_value \* risk\_factor contract\_variation = std \* point\_value

contracts = target\_variation / contract\_variation return int(np.nan\_to\_num(contracts))

def initialize(context):

```
"""
Cost Settings
"""
if enable_commission:
  comm_model = PerContract(cost=0.85, exchange_fee=1.5)
else:
  comm_model = PerTrade(cost=0.0)
```

set\_commission(us\_futures=comm\_model)

```
if enable_slippage:
  slippage_model=VolatilityVolumeShare(volume_limit=0.2)
else:
  slippage_model=FixedSlippage(spread=0.0)
```

```
set_slippage(us_futures=slippage_model)
```

```
"""
Markets to trade
"""
currencies = [
   'AD',
   'BP',
   'CD',
   'CU',
   'DX',
   'JY',
   'NE',
   'SF',
]
```

| agricultural<br>=<br>[ |  |  |  |
|------------------------|--|--|--|
| 'BL',                  |  |  |  |
| '_C',                  |  |  |  |
| 'CT',                  |  |  |  |
| 'FC',                  |  |  |  |
| 'KC',                  |  |  |  |
| 'LR',                  |  |  |  |
| 'LS',                  |  |  |  |
| '_O',                  |  |  |  |
|                        |  |  |  |

```
'_S',
   'SB',
   'SM',
   '_W',
]
nonagricultural = [
   'CL',
   'GC',
   'HG',
   'HO',
   'LG',
   'NG',
   'PA',
   'PL',
   'RB',
   'SI',
]
equities = [
   'ES',
   'NK',
   'NQ',
   'TW',
   'VX',
   'YM',
]
rates = [
   'ED',
   'FV',
   'TU',
   'TY',
   'US',
]
```

```
# Make a list of all the markets
markets = currencies + agricultural + nonagricultural + equities + rates
```

```
# Make a list of all continuations
context.universe = [
  continuous_future(market, offset=0, roll='volume', adjustment='mul')
     for market in markets
```

```
]
```

# We'll use these to keep track of best position reading # Used to calculate stop points. context.highest\_in\_position = {market: 0 for market in markets} context.lowest\_in\_position = {market: 0 for market in markets}

# Schedule the daily trading schedule\_function(daily\_trade, date\_rules.every\_day(), time\_rules.market\_close())

```
# We'll just use this for the progress output
# during the backtest. Doesn't impact anything.
context.months = 0
```

```
# Schedule monthly report output
schedule_function(
  func=report_result,
  date_rule=date_rules.month_start(),
  time_rule=time_rules.market_open()
)
```

```
def analyze(context, perf):
```

returns, positions, transactions = pf.utils.extract\_rets\_pos\_txn\_from\_zipline(perf) pf.create\_returns\_tear\_sheet(returns, benchmark\_rets=None)

```
def daily_trade(context, data):
  # Get continuation data
  hist = data.history(
     context.universe,
     fields=['close','volume'],
     frequency='1d',
     bar_count=250,
  )
```

```
# Calculate trend
  hist['trend'] = hist['close'].ewm(span=fast_ma).mean() >
hist['close'].ewm(span=slow_ma).mean()
```

```
# Make dictionary of open positions
open_pos = {
  pos.root_symbol: pos
  for pos in context.portfolio.positions
}
```

# Iterate markets, check for trades for continuation in context.universe:

# Get root symbol of continuation root = continuation.root\_symbol

# Slice off history for just this market h = hist.xs(continuation, 2)

```
# Get standard deviation
std = h.close.diff()[-vola_window:].std()
```

if root in open\_pos: # Position is open

# Get position p = context.portfolio.positions[open\_pos[root]]

```
if p.amount > 0: # Position is long
  if context.highest_in_position[root] == 0: # First day holding the position
     context.highest_in_position[root] = p.cost_basis
  else:
     context.highest_in_position[root] = max(
       h['close'].iloc[-1], context.highest_in_position[root]
     )
```

```
# Calculate stop point
stop = context.highest_in_position[root] - (std * stop_distance)
# Check if stop is hit
if h.iloc[-1]['close'] < stop:
  contract = open_pos[root]
  order_target(contract, 0)
  context.highest_in_position[root] = 0
# Check if trend has flipped
elif h['trend'].iloc[-1] == False:
  contract = open_pos[root]
  order_target(contract, 0)
  context.highest_in_position[root] = 0
```

```
else: # Position is short
  if context.lowest_in_position[root] == 0: # First day holding the position
     context.lowest_in_position[root] = p.cost_basis
  else:
     context.lowest_in_position[root] = min(
       h['close'].iloc[-1], context.lowest_in_position[root]
     )
```

```
# Calculate stop point
stop = context.lowest_in_position[root] + (std * stop_distance)
```

# Check if stop is hit if h.iloc[-1]['close'] > stop:

```
contract = open_pos[root]
  order_target(contract, 0)
  context.lowest_in_position[root] = 0
# Check if trend has flipped
elif h['trend'].iloc[-1] == True:
  contract = open_pos[root]
  order_target(contract, 0)
  context.lowest_in_position[root] = 0
```

else: # No position on if h['trend'].iloc[-1]: # Bull trend # Check if we just made a new high if h['close'][-1] == h[-breakout\_window:]['close'].max(): contract = data.current(continuation, 'contract')

> contracts\_to\_trade = position\_size( \ context.portfolio.portfolio\_value, \ std, \ contract.price\_multiplier)

# Limit size to 20% of avg. daily volume contracts\_cap = int(h['volume'][-20:].mean() \* 0.2) contracts\_to\_trade = min(contracts\_to\_trade, contracts\_cap)

# Place the order order\_target(contract, contracts\_to\_trade)

```
else: # Bear trend
  # Check if we just made a new low
  if h['close'][-1] == h[-breakout_window:]['close'].min():
     contract = data.current(continuation, 'contract')
```

contracts\_to\_trade = position\_size( \ context.portfolio.portfolio\_value, \ std, \ contract.price\_multiplier)

# Limit size to 20% of avg. daily volume contracts\_cap = int(h['volume'][-20:].mean() \* 0.2) contracts\_to\_trade = min(contracts\_to\_trade, contracts\_cap)

# Place the order order\_target(contract, -1 \* contracts\_to\_trade)

# If we have open positions, check for rolls

if len(open\_pos) > 0: roll\_futures(context, data)

start = datetime(2001, 1, 1, 8, 15, 12, 0, pytz.UTC) end = datetime(2019, 1, 31, 8, 15, 12, 0, pytz.UTC)

perf = zipline.run\_algorithm( start=start, end=end, initialize=initialize, analyze=analyze, capital\_base=starting\_portfolio, data\_frequency = 'daily', bundle='futures' )

### **Core Trend Model Results**

After running the model, the first thing to do is to check the general shape of the equity curve. That's of course not a valid or measurable basis for decisions, but it does give a general overview of whether or not a model is worth investigating any further. You will find that you can often discard ideas and concepts after a glance at the equity curve. Sometimes it will give you much more information about what a strategy will do than the usual ratios, such as Sharpe, annualized return or maximum drawdowns.

| Year | Jan  | Feb   | Mar   | Apr  | May   | Jun   | Jul  | Aug  | Sep   | Oct   | Nov  | Dec  |
|------|------|-------|-------|------|-------|-------|------|------|-------|-------|------|------|
| 2001 | -4.6 | +0.8  | +9.3  | -9.3 | +0.5  | -2.8  | +0.5 | +1.9 | +6.1  | +7.4  | -3.9 | -1.3 |
| 2002 | -3.3 | -2.1  | -3.5  | -1.8 | +7.4  | +12.6 | +6.1 | +0.3 | +4.5  | -6.1  | -2.2 | +6.4 |
| 2003 | +3.5 | +7.2  | -8.4  | +1.1 | +4.2  | -2.9  | +1.3 | -4.0 | +2.4  | +8.3  | -3.4 | +8.5 |
| 2004 | +0.2 | +3.5  | +0.6  | -7.1 | +0.9  | -0.4  | +1.9 | -2.4 | +0.3  | +3.1  | +3.9 | -1.6 |
| 2005 | -6.7 | +0.1  | +0.7  | -0.4 | -0.2  | -4.2  | +1.8 | +1.5 | +2.4  | -1.9  | +7.4 | -1.2 |
| 2006 | +7.6 | -1.6  | +1.9  | +9.6 | +2.1  | -4.4  | -3.8 | +7.1 | -2.2  | +2.7  | +2.4 | -4.6 |
| 2007 | -0.1 | -5.7  | -3.0  | +6.4 | +0.0  | +5.4  | -1.5 | +1.9 | +8.2  | +2.0  | +2.7 | +1.8 |
| 2008 | +5.7 | +21.0 | -11.6 | +0.9 | +3.2  | +0.5  | -8.9 | +6.0 | +12.0 | +28.4 | +3.5 | +3.3 |
| 2009 | -2.2 | +2.7  | -8.4  | -1.4 | +14.9 | -9.9  | +1.1 | +5.0 | +2.6  | -5.1  | +5.5 | -3.0 |
|      |      |       |       |      |       |       |      |      |       |       |      |      |

*Table 15.1 - Core Trend Monthly Returns*

| 2010 | -2.0  | +0.3 | +2.3 | -0.3  | -3.0  | -2.4 | +1.4 | +3.8  | +9.4  | +8.7 | -7.5  | +9.3 |
|------|-------|------|------|-------|-------|------|------|-------|-------|------|-------|------|
| 2011 | +1.9  | +1.3 | -0.4 | +14.6 | -7.5  | -4.9 | +3.1 | -2.7  | +2.5  | -8.8 | -0.5  | -1.8 |
| 2012 | +0.4  | +4.2 | +1.3 | -1.8  | +13.5 | -7.7 | +9.1 | +1.2  | -0.5  | -7.3 | -1.0  | +0.8 |
| 2013 | +1.3  | -2.2 | +1.3 | +0.5  | +3.3  | +2.4 | -5.4 | -3.4  | -2.3  | -0.9 | +1.5  | +3.8 |
| 2014 | -7.5  | +2.5 | -4.5 | -2.2  | +0.7  | +0.0 | +2.4 | +13.3 | +20.7 | -2.9 | +8.3  | +9.9 |
| 2015 | +6.7  | -7.0 | -2.6 | -2.8  | -0.2  | -1.0 | +4.4 | -0.7  | +0.1  | -5.3 | +2.7  | +0.2 |
| 2016 | +1.7  | +1.0 | -3.5 | +3.1  | -2.3  | +0.2 | -0.9 | -2.7  | -2.4  | +1.9 | +13.8 | +0.6 |
| 2017 | -6.9  | +1.6 | -5.2 | -1.8  | -2.2  | -1.5 | +4.2 | +0.3  | -2.5  | +7.0 | +3.5  | +3.0 |
| 2018 | +16.7 | -2.2 | -5.1 | +0.8  | -0.8  | +3.8 | -0.6 | +3.7  | -0.6  | -2.7 | +1.5  | +8.6 |

Figure 15‑2 shows the backtest performance of this simple trend model, compared to that of the S&P 500 Total Return Index. This basic visual overview gives a few important pieces of information. The most obvious being that it seems as if this strategy has a higher long term performance than the S&P 500. But that's almost irrelevant. You could even argue that it's an irrelevant comparison to begin with. After all, this is not an equity related strategy in any way.

Simply having a higher long term performance is not a measurement of quality. Keep in mind that in a simulation like this, we could simply scale position risk sizes up or down to change the end cumulative performance numbers. Comparing the start and end points only does not make much sense. We need to consider how we got there.

Next we can see in the same figure how the performance tends to come at different times than the stock markets. There were two major equity bear markets during this period and both times the futures strategy did well. This should really not be a surprise to anyone who has been following the trend following space. The approach has historically done very well during periods of market crisis.

This also means that the trend model at times severely

underperforms during bull markets, and that can be a bigger problem than one might think. The stock market is used as a benchmark in this figure, even though the strategy really has very little to do with that sector. The point is that the public at large and even financial professionals tend to compare everything with the stock markets.

If you manage other people's money, this is something you will quickly notice. Even if you have a strategy which really should be unrelated to the stock markets, you will still always be compared to it. If you lose ten percent and the stock market loses 15 percent, no one will complain. If you gain ten percent and the stock market gains 15, you may find that some clients are unhappy. Like it or not, the stock market is the de facto benchmark.

![](_page_34_Figure_2.jpeg)

While having a low correlation to equity markets during bull

markets can be problematic, having a low correlation during bear markets is of vital importance. This is where a strategy like this really shines. People like making money, but there is nothing like making money while your neighbor loses his.

The return chart also shows a somewhat worrying aspect. A quick glance tells you that returns seem to be going down. We are seeing deeper and longer lasting drawdowns. Yes, this is true. And there are good reasons for this. The environment for trend following has not been optimal in the past few years.

The low volatility situation is one issue. Trend following thrives on high volatility markets and has performed remarkably well during volatile bear markets. But we have seen a ten year bull market with fairly low volatility, and that has reduced earning potential for diversified futures strategies.

The low interest environment has also been a concern. Historically, trend following made outsized returns on simply being long bonds, treasuries and money market futures, capitalizing on the slowly decreasing yields. As yields came down to historically low levels and stagnated, that source of income dwindled.

It would however be a mistake to take the last few years as a sign of trend following demise. Just like it was a mistake to take the extreme returns of 2008 and extrapolate that into the future. What we do know is that this highly simplified type of strategy has worked well for decades. It has outperformed traditional investment approaches and it has shown very strong performance during bear markets and times of market distress. It would be a reasonable assumption that it will perform well during the next bear market.

Years **1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18** 2001 +3 +10 +13 +10 +8 +9 +10 +17 +15 +15 +13 +13 +12 +14 +13 +12 +12 +12 2002 +18 +18 +12 +9 +10 +12 +19 +17 +17 +15 +14 +13 +15 +13 +13 +12 +13 2003 +17 +10 +6 +9 +10 +19 +16 +17 +14 +14 +12 +15 +13 +13 +12 +12 2004 +2 +1 +6 +9 +20 +16 +17 +14 +13 +12 +15 +13 +12 +11 +12 2005 -1 +7 +11 +25 +19 +19 +15 +15 +13 +16 +14 +13 +12 +13 2006 +17 +18 +35 +25 +24 +18 +17 +15 +18 +15 +15 +13 +14 2007 +19 +45 +28 +26 +19 +17 +15 +18 +15 +14 +13 +14 2008 +76 +32 +28 +19 +17 +14 +18 +15 +14 +12 +13 2009 -1 +9 +4 +6 +5 +10 +8 +8 +7 +9 2010 +20 +7 +8 +6 +13 +9 +9 +8 +10 2011 -5 +3 +2 +11 +7 +8 +6 +8 2012 +11 +5 +17 +11 +10 +8 +10 2013 -1 +20 +10 +10 +8 +10 2014 +44 +16 +14 +10 +13 2015 -6 +1 +0 +6 2016 +10 +4 +10 2017 -1 +10 2018 +24

*Table 15.2 Holding Period Returns Core Trend Model*

The holding period return overview in Table 15.2 provides a different way of looking at the returns. This shows you what your annualized return would be if you bought at the start of a given year, and held for a certain number of years. If you want to see what would have happened if you had started this strategy in January of 2004 and held for four years, go to the row with that year and four columns out. That will tell you that you would have made an annualized gain of 9% during this period.

While this graph tells you little about important details, such as the volatility and drawdowns it took to get those returns, it can help provide a long term perspective.
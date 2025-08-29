## **Constructing ETF Models**

Building ETF trading models is a great way to learn the basics. It's simple for several reasons. There are not many of them. That makes things much easier than for something like stocks. There are more stocks out there than anyone cares to count. Having a very large set of instruments to pick from has both advantages and disadvantages, but it clearly adds a level of complication. Even with the boom of the ETF business and new funds popping up all over, the extent of the tradable ETF universe is fairly limited.

ETFs are, much like stocks, cash instruments. That's another factor that makes things simple for us. In the financial world, cash instruments are the most simple. You generally pay up front for what you want to buy, you have a linear payoff and the percent change in the instrument is your profit or gain. Very easy, compared to the likes of futures, options, swaps, forwards and other derivatives.

Many ETFs, at least most of the good ones, are clear and transparent. They usually track a specified index, so you know exactly what is in it and thereby you know what to expect from the returns. Naturally you don't know what to expect in terms of exact returns, but you can analyze the underlying index and gain an understanding of the volatility and return profile in various market climates.

There are downsides with trading ETFs as well, even if you stick to just the good ETFs and not the structured product kind. A common mistake is to think that ETFs can simply replace futures in creating diversified strategies. That's just not true. The asset class coverage just is not good enough to replace futures, but the cash nature of ETFs is the real killer. The point with diversified futures strategies is that you can trade anything, in any asset class, without worrying about cash constraints.

While futures traders can focus solely on the risk and

completely disregard notional exposure, an ETF trader can't afford such luxury. When cash runs out, it runs out. Leveraging up from there is restrictive and expensive.

Most ETFs are fairly low volatility. Take something like a classic index tracker. If the underlying index consists of 500 stocks, the index tracker will naturally have a lower volatility than most constituent stocks. That in itself is not a problem, but in combination with the cash constraint it can be.

Taking on lots of volatility or a high notional exposure in a portfolio is not necessarily a good thing. But it's a good thing to have the option of doing so, if that's what you need.

In the futures world, there is no worry about notional exposure. A good example of when this way of working is useful is in the money markets. To be clear, money market refers to the short term interest rate sector. Not to the currency markets, which is a very different thing.

Money market instruments have a very low volatility, due to their short duration. At this point, it's not too important to understand why, just that in this sector a 0.1% daily moves is considered large and 1% daily move is practically unheard of.

Trading such slow moving markets is not a problem in futures space. You just buy more of it. In futures world, the limit to how much you can buy is defined by how much risk you want to take, rather than how much cash is in your portfolio. In theory, the margin requirements set the limit for how much risk you can take with futures, but it's quite unlikely that you would like to take that much risk on. For ETFs though, the situation is very different.

Slow moving, low volatility ETFs, will hog a lot of cash for very little return. The cash availability is limited, and if you use it to buy an instrument that barely moves a few basis points a day, you are simply locking up capital. You just can't leverage up the same way as you could for futures.

Still, because of the relative simplicity of ETFs, it's a well suited area to start learning about constructing trading models.

## **Asset Allocation Model**

It its simplest form, an asset allocation model is simply a mix of broad asset classes, held at a certain predetermined weight. This type of model is more of a long term investment approach than trading, but can make a lot of sense for capital allocation.

An age old allocation approach would be to place 70 percent of your money in bonds and 30 percent in stocks. That's the rule that Warren Buffet famously recommends for retirement savings. Many readers of this book will surely think that this sounds incredibly boring. Perhaps, but having at least part of your overall net worth in something like this kind of allocation model might not be a bad idea, in the long run.

Whether you are interested in implementing such a portfolio or not, does not really matter. It makes for a good exercise in constructing Python based backtests. The 70/30 asset mix suggested by Buffett is just one example, and in our first model here we will use a slightly broader allocation.

Important to understand is that the point here is to demonstrate concepts, not exact rules. The approach used here is absolutely valid, but which ETFs you would chose and at which weights is more a matter of preference than anything.

The rules of this first ETF model are the following. We will use five ETFs to allocate our assets to. Each ETF will have a target weight, and at the beginning of each month we will reset the allocation to this target weight.

The model will hold the S&P 500 Index tracker, SPY, at a weight of 25%. On the bond side, we will have the long term 20 Year

Treasure ETF, TLT, at a weight of 30% as well as the medium term 7- 10 Year Treasury ETF, IEF, at a weight of 30%. We will also add some commodities, with the gold tracker GLD at 7.5% and the general commodity tracker DBC, also at 7.5%.

Now this should not be too hard to model. If you feel confident enough with the earlier lessons on backtesting, go ahead and build this code by yourself. It's really quite simple.

The actual code needed for this model is very brief. It does after all have very simple rules. The logic of what we are doing is as follows. In our initialization, we define a dictionary of ETF tickers and target weights. This is essentially our intended portfolio allocation. Then we schedule a monthly rebalance.

In the monthly rebalance, we loop through the dictionary, and set the target weight accordingly. And that's pretty much it.

First, I will show you the code for what was just described, along with the now standard piece of code at the bottom to fire off the backtest. The code below performs the entire backtest, but does not output any sort of results.

The results, as you can see when the backtest is fired off in the code, will be stored in variable I called resul t . To demonstrate an often convenient way of working with backtests, I suggest you put this code in a Jupyter Notebook cell by itself, and execute it. Then we can analyze the results in the next cell later.

You may notice in the code here, that I used a bundle called ac\_equities\_db. This is a custom bundle, constructed as explained in chapters 23 and 24. We are reaching the limit to what can be done with free data sources like Quandl, and that's why I'm moving to custom bundles.

That means that you may need to find your own data source to replicate code from hereon in the book. I cannot provide that data for you, as that would breech all kinds of license agreements, but the later

## chapters in the book will explain how to connect your own data.

%matplotlib inline import zipline from zipline.api import order\_target\_percent, symbol, schedule\_function, date\_rules, time\_rules from datetime import datetime import pytz from matplotlib import pyplot as plt import pandas as pd

def initialize(context): # Securities and target weights

context.securities = { 'SPY': 0.25, 'TLT': 0.3, 'IEF': 0.3, 'GLD': 0.075, 'DBC': 0.075

}

# Schedule rebalance for once a month schedule\_function(rebalance, date\_rules.month\_start(), time\_rules.market\_open())

def rebalance(context, data): # Loop through the securities for sec, weight in context.securities.items(): sym = symbol(sec) # Check if we can trade if data.can\_trade(sym): # Reset the weight order\_target\_percent(sym, weight)

# Set start and end start = datetime(1997, 1, 1, 8, 15, 12, 0, pytz.UTC) end = datetime(2018, 12, 31, 8, 15, 12, 0, pytz.UTC)

# Fire off backtest result = zipline.run\_algorithm( start=start, # Set start end=end, # Set end initialize=initialize, # Define startup function capital\_base=100000, # Set initial capital data\_frequency = 'daily', # Set data frequency bundle='ac\_equities\_db' ) # Select bundle

As you see, this code is very straight forward. Constructing models like this is quick, easy and painless. I also used a new concept in there, which I hope you already picked up from glancing the code.

Previously in chapter 5 we worked with lists, which are as the name implies just lists of any kind of stuff. In this case, I instead used a dictionary, something you may remember from the same chapter. As a brief reminder, lists are created by putting things in brackets, much like below.

```
some_list = ['some text', 'some other text', 5, 8.217]
```

A list can contain any type of variable or value, and above you see a mix of text and numbers, just to demonstrate this.

A dictionary on the other hand, can hold pairs of information, to be used as a lookup table, and it's enclosed in curly brackets.

```
a_dictionary = {'one': 1, 'two': 2, 'three': 3}
```

A dictionary matches two items. A key and a value. As you see in the code for the ETF model above, we use strings as keys and weights as values in context.securitie s . Then later in the rebalanc e routine, we iterate this object using a very simple syntax.

```
for sec, weight in context.securites.items():
```

This way we can in a very fast and easy way go over each security in the dictionary, check the target weight and make the necessary trades.

But now are you probably wondering if this model is worth trading or not. When you see the actual results, you may very well be disappointed. This is not a model that attempts to grind out a maximum of return. This is a variant of what Mr. B suggested as a retirement saving scheme. Low returns, low risks.

Since you have already learned about how to visualize output from backtests in chapter 8, you can apply the same logic to get a feel

for how this simple strategy performed. As you will notice if you run the code segment above, after the backtest run it simply outputs a line of text to inform you that it's ready for analysis. Now you can make a new cell in the Notebook, below the backtest, and write something to visualize the output. Revert to chapter 8 if you need a refresher.

![](_page_6_Figure_1.jpeg)

So how do we interpret this? Clearly a graph like this does not hold sufficient information for any in-depth study, but we can still make out a few interesting observations. The first segment, the equity

curve, seems to show a reasonably smooth and well behaving profile. Without looking too closely at the scale, it seems at least worthwhile to study further.

The second graph should raise an eyebrow. At least I included it in hopes that you will react to it. Did we not just make portfolio allocations that always add up to 100 percent? Why is the exposure level going up in steps?

This is an issue with ETFs which can cause some headache. Most ETFs haven't really been around that long. I still remember back in the later part of the 1990's when the first ETFs, such as the SPY and the QQQ were first launched. Only a handful have such long history. Most ETFs were launched in the past ten to fifteen years. That makes it a little difficult to build proper long term backtests in the ETF space.

So the reason why you see the exposure going up in steps is that from the start of the backtest, the only available ETF was the SPY. Then the bond ETFs were launched. Then the gold tracker, and finally the general commodity tracker.

The sparse availability of long term ETF time-series is something we need to take into account when constructing ETF models. There is simply not enough data. The obvious danger is to build models on just a few years' worth of data, which may not have statistical significance or predictive value.

A common beginner mistake is to simply look at the end results of a model, without digging into the details of how you got there. The issue here, that we only have a very limited amount of historical data for some ETFs is but one of many that can arise from not paying attention to the details.

The third segment shows the annualized return, as we discussed earlier, this time showing a full year rolling window. This is just a simple visualization to show what kind of returns you may be looking at over time. While this sometimes spikes up even to the 15%

range, we are seeing an average value of a little over 3%. Well, I did tell you that it was a slow moving model.

Yes, it's not a terribly exciting model, but that's not the purpose. It is after all an asset allocation model. But making these kind of models serves a purpose. For one thing, most people should have some sort of longer term, stable investment portfolio which is not subjected to the kind of risks that shorter term trading is prone to. You could also use allocation models like this as a realistic alternative to trading, to be used as benchmark indexes and compared to your trading models.
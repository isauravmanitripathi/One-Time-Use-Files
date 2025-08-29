## **Systematic Momentum**

Momentum is a market phenomenon that has been working well for decades. It has been confirmed both by academics and practitioners and is universally known as a valid approach to the financial markets. It's also based on a very simple principle.

Slightly simplified, momentum is the principle that stocks that moved up strongly in the recent past are a little more likely to do better than other stocks in the near future. Yes, we simply buy stocks that have had a good run. The trick is in finding a method of identifying the stocks to buy, and how to construct a portfolio from them and knowing when not to buy.

In this chapter we will construct a momentum model, step by step. While the concept itself is very simple, there are some details that can be quite important in arriving at a model which will be able to show stable long term performance.

The aim here is to show a solid approach that you can build upon, modify and improve as you wish. We are not talking about some sort of magical trading system to beat all trading systems. You will have to look for that in other trading books. Here we will deal with real life quantitative trading models. The purpose of this book is to teach methods and approaches, not to peddle some supposedly magical trading systems.

# **Replicating this Model**

Up until this point in the book, it has been reasonably easy to replicate the models and run the code by yourself. By easy, I mean that it didn't require any special data or unorthodox technical solutions.

Dealing with equities, does however require some complex solutions. There is one complication in this chapter which could potentially cause a bit of a headache, and that is universe selection. How we, from a technical point of view, solve the issue of which exact stocks we are able to trade.

The aim here, with this model and this chapter, is to limit the stock selection to the historical membership of the S&P 500 Index. We want to make sure that the model is aware, for each day, which exact stocks were members of that index, and only trade those.

This of course requires you to have such information available, and to find a solution for how to store it and how to access it. My own preferred approach is to store this kind of data in a local securities database, something which is explained in more detail in chapter 24. Not all readers are likely to go the full nine yards and getting your own database, so I will offer an easier solution, along with that probably misused American sports reference which I really don't understand myself.

The solution I will show you here is based on having a local comma separated file with an updated index composition for each day where it has changed. The code, as you will soon see, will then fetch the index membership list for the closest prior date to the current trading day.

This added complication of universe selection, of deciding which stocks were possible or probable to be selected for trading in the past, is unique for equities. That is one of the main reasons why equity models are usually more complex from a technical point of view.

This may sound surprising, but for most readers of this book, it will be easier to replicate the futures models later in this book, as the survivorship bias does not play in there the same way.

## **Momentum Model Rules Summary**

- Trading is only done monthly.
- Only stocks in the S&P 500 will be considered.
- Momentum slope will be calculated using 125 days.
- Top 30 stocks will be selected.
- Weights will be calculated for these 30 stocks according to inverse volatility.
- Volatility is calculated using 20 day standard deviation.
- Trend filter calculated based on a 200 day average of the S&P 500 index.
- If the trend filter is positive, we are allowed to buy.
- Minimum required momentum value is set to 40.
- For each of the 30 selected stocks, if the stock has a momentum value higher than 40, we buy it. If not, we leave that calculated weight for that stock in cash.
- We sell stocks if they fall below the minimum required momentum value, or if they leave the index.
- Each month we rebalance and repeat.

#### **Investment Universe**

First we need to settle on an investment universe. That is, decide which stocks are eligible for selection. In my book *Stocks on the Move* (Clenow, Stocks on the Move, 2015), I used the constituent stocks of the S&P 500 index as investment universe. Not the current members of course, but the historical composition. On any given trade

date, the model would check which stocks were part of the index on that day and consider only those stocks. This is to avoid, or at least reduce survivorship bias.

This way of limiting the investment universe is effective and fairly easy to implement. You could find other ways of accomplishing similar results, such as limiting based on market capitalization or trading volume, but if you have access to historical index joiners and leavers information, this is a simple way to do it.

For the momentum models here, we will use the same methodology as in my previous book; limiting stocks based on historical index membership. As the S&P 500 is probably the most widely followed market index in the world, I'm going to stick to that index in this demonstration. But that's not to say that this index somehow produces better results. If you could really use the word better in such a context. It all depends on what you want to accomplish. What kind of return profile to you need. There is no 'better'.

As long as you have a broad enough index, with at least a few hundred available stocks to choose from, the same principles and logic should be applicable. Before asking whether or not the same model works on your own local market index, go ahead and try it out. Replicate what this book does, get the data, run the backtests.

I want you to learn ideas from this book. Then I want you to go out and test variations of those ideas. See what you like and what you don't. I'm giving you the tools for learning, not exact rules to follow.

#### **Momentum Ranking**

Next we need a way to identify stocks to buy. There are many types of momentum analytics and most will show a fairly similar ranking. What we want to do here is to make a list of well performing stocks. How hard can that be?

The simplest way of doing this is to measure percent return over a given time frame. So we could take our 500 stocks, measure the difference between yesterday's price and the price of say, half a year ago, and rank them accordingly. After that, all we have to do is to start buying from the top of the list.

While such a simple concept could show decent returns, we are going to do things a little more complex here. The problem with the simple percent return is it does not take account just how the returns happened.

If we simply rank stocks based on the percent return, we will likely end up with an over representation of really wild situations. We would see extremely volatile stocks which could gain or lose large amounts in short periods of time, or we could get takeover situations where the stock price suddenly made huge jumps. This is not really what momentum should be about.

While there are several valid ways of calculating stock momentum, I will use my own momentum score. My concept is simply a variation of well-established momentum calculations, but it's one that I believe holds some value. What I do is to measure the momentum using exponential regression slope, and then multiply it by the coefficient of determination. No, that's not as complicated as it sounds.

```
momentum_score = Annualized Exponential Regression Slope * R2
```

Let's take that one step at a time. The difference between linear regression, which most are more familiar with, and exponential regression is that while the linear regression slope is expressed in dollars, in the case of USD denominated financial markets, the exponential slope is expressed in percent. Linear regression wouldn't be very useful, unless of course every single stock has the same price to begin with, which is not overly likely.

Regression is a method of fitting a line to a series of observations. It aims at finding a line that fits the best. That does not

mean that it necessarily fits perfectly, but we will get to that. What is important to understand is that we are trying to fit a line to the data, in our case the daily stock prices. To draw a line, we need a slope and an intercept. But we are not really interesting in actually drawing the line, we just need to know the slope. That is, the trend.

![](_page_5_Figure_1.jpeg)

A linear regression slope tells us how many units, in the case of American stocks that means dollars, the regression line slopes up or down per day. So if the same trend continues, the slope would tell us how many dollars per day we should expect to gain or lose on average.

But such a measurement is not very useful for our purposes. A stock with a current price of 500 will show very different numbers than a stock priced at 10. If both are showing a current linear regression slope of 1 dollar, that means two very different things. It means that the stock priced at 500 is moving very slowly, while the

stock priced at 10 is moving very fast. Regression is useful, but not necessarily linear regression.

If we instead look at exponential regression, things get more interesting. The exponential regression slope tells us how many percent up or down that the line is sloping. That means that if you draw an exponential regression slope on a regular, linear scale graph, you would get a parabolic curve.

![](_page_6_Figure_2.jpeg)

*Figure 12*‑*2 Exponential Regression*

What makes exponential regression so much more useful is that we can now compare it across multiple stocks, regardless of their base price. The exponential regression slope can be a little hard to relate to, as it's usually a very small decimal number. After all, how many percent per day do you really expect a stock to move?

For instance, you might end up calculating an exponential regression slope of 0.0007394. Tough to remember. But it's much easier to relate to if you annualize it. That is, calculate what this daily

slope means on a yearly basis, should the current trend persist for that long. Keep in mind that we don't actually expect that to happen. That's not important. We annualize the number to make it easier to relate to.

So take that number again, 0.0007394, and annualize it. The math for that is easy.

That means that now we have a stock which has a positive trend equivalent of about 20.5% per year. That should be a bit easier to relate to.

The reason we raised that number to the power of 252 is that we assume 252 trading days in a year. If we move up by 0.07394% per day for 252 days in a row, we will end up gaining about 20.5%. I told you that the math would be easy.

But just using the exponential regression slope alone does not tell us anything about how well this line fits. An extreme example would be where the price went absolutely sideways, and then made a 50% single day jump on a takeover announcement.

![](_page_8_Figure_0.jpeg)

*Figure 12*‑*3 Low Regression Fit*

The exponential regression value will likely be very high. But that's not the kind of situation that we are looking for. The same, but slightly less extreme, goes for very volatile stocks. The line may not fit very well there either. We need to compensate for this.

A very important concept in finance is that volatility is, for lack of a better word, bad. It's not possible to avoid volatility, but you need to be compensated for it. All returns need to be viewed in the light of the volatility it took to achieve it. Therefore, we need to adjust our exponential regression slope for this. While there are many ways of looking at volatility, in this particular case, the coefficient of determination is a great tool.

This analytic, commonly denominated R 2 , tells us how well our regression line fit the data. If it's a perfect fit, with all observations exactly on the line, the R <sup>2</sup> will be exactly 1. If it's utterly random noise, and the line does not fit in any way whatsoever, the R <sup>2</sup> value

will be 0. Therefore this analytic will always be between 0 and 1. The better the fit, the higher the value.

What we will do is simply to take the annualized regression slope, and multiply it by the R 2 . Effectively, we are punishing stocks that are more volatile. Stocks that are moving up in a smooth trend will have a higher R <sup>2</sup> value and their slope won't take too much of a hit. But in the example of the takeover situation mentioned earlier, the R <sup>2</sup> will be very low and greatly reduce the slope value.

So how do you calculate exponential regression? If you want the big scary looking formula, you will have to look it up yourself. If you are the kind of guy, or gal, who is interested in a complex looking formula, you will either already know it or at least you will have no problem finding it. It's not exactly secret information. Instead, I will show you how to use Python to calculate the result.

```
from scipy import stats
def momentum_score(ts):
  """
  Input: Price time series.
  Output: Annualized exponential regression slope,
       multiplied by the R2
  """
  # Make a list of consecutive numbers
  x = np.arange(len(ts))
  # Get logs
  log_ts = np.log(ts)
  # Calculate regression values
  slope, intercept, r_value, p_value, std_err = stats.linregress(x, log_ts)
  # Annualize percent
  annualized_slope = (np.power(np.exp(slope), 252) - 1) * 100
  #Adjust for fitness
  score = annualized_slope * (r_value ** 2)
  return score
```

Here is what the function above does. The expected input here, the variable t s , is a time series. Throw your time series at this function, and you get the momentum value back.

Step by step. First we calculate a natural log series from the price time series we gave it. That's because the easiest way to

calculate exponential regression is to just do a regular linear regression based on the log values.

log\_ts **=** np **.** log **(** ts **)**

To calculate regression, we need two axes. One is of course the price observations. The other is just a constantly incrementing series. 1, 2, 3, 4 and so on. After all, the price observations are at equal distances. We have one observation per day. Using date values or any other numbers makes no differences, so we will use a neat **Numpy** function called arang e . No, that's not misspelled.

This function, arang e , simply returns a series of the same length as the input, with the values 0, 1, 2, 3, 4 … up until the full length. So we very easily get a matching x-axis for our regression calculation this way. By default, arang e will give you a zero based list, though you could provide a start and stop if you like. In this case, it really does not matter.

x = np.arange(len(ts))

Now we have two series. One with log values of the prices and the other with an equal spaced x-series. That means that we can now do the regression math. But of course, we don't have to reinvent the wheel here. No need to write the standard regression formula ourselves. Just use the one built into the statistics library **scipy** , which is short for Scientific Python. Remember to import it, at the top of the code.

#### from scipy import stats

Using the pre-built function in this library, stats.linregres s , we can output the values associated with regression. As you see, in one line we get five values; **slope** , **intercept** , **r-value** , **p-value** and **standard error** . All we need here is the **slope** and the **r-value** .

slope **,** intercept **,** r\_value **,** p\_value **,** std\_err **=** stats **.** linregress **(** x **,** log\_ts **)**

The following row is important to understand. This is where we transform the slope into something we can use, and relate to. Breaking

it down to its parts we get this. Start with np.exp(slope ) . That will give us the percentage slope of the exponential regression line, telling us how many percent up or down per day it moves. Then we raise it to the power of 252, arriving at an annualized number. Multiply by 100 to get a number that's easier to relate to.

Ok, so some of you are now asking yourselves the obvious question. Why we would need to be able to relate to the number, when computer code does the interpretation and trading. Well, during development and testing, you will likely want to output this number, or graph it. And if this is transformed into something that makes intuitive sense, such as a yearly number, you will much easier be able to spot issues and identify opportunities. But sure, it makes no difference for the algo per se.

```
ann_slope = ( np . power ( np . exp ( slope ), 252 ) - 1 ) * 100
```

And then, finally, we have only one more thing to do. Multiply it with the R2, before returning the result. We got the **r-value** before, so just square it, multiply the annualized slope with it, and return the result. As you see in the code just below, we can square a number using the double multiplier syntax.

```
return annualized_slope * ( r_value ** 2 )
```

And that's how we calculate the momentum score used for this model.

### **Position Allocation**

The most common way of allocating to positions is to base it on volatility. Perhaps I should qualify that statement. Volatility based allocation is most common in the professional, quantitative side of the financial industry. Among hobby traders and traditional asset managers, equal sizing remains most prevalent.

If we want to take on an approximate equal risk in a number of

positions, we would normally look at how volatile they are and allocate accordingly. A more volatile stock gets a smaller weight. Slower moving stocks get a higher weight. The rationale behind this is simple. As we don't have any reason for assuming that any of the selected stocks will perform better or worse than any other, we want to give them an equal chance.

If we put the same weight on all stocks, that is allocate the same amount of money to each, we would get a portfolio geared towards the most volatile ones. If some stocks tend to move 4-5 percent per day, and others only half a percent on a normal day, the more volatile ones will drive the portfolio. No matter how well the slow moving stocks do, they just wouldn't have the same chance to make a dent in the bottom line.

The most important thing is that you understand the concept here. We are buying different amounts of each stock, but the purpose is to allocate approximately the same risk to each. The volatility serves here as a proxy for risk. The more volatile the stock, the less of it we buy.

Volatility can be measured in a few different ways. In my previous books, I kept things a bit simple by using Average True Range (ATR) as a volatility measurement. It's a concept that's well known in the retail trading space and it has been used for a long time. ATR is part of the old school technical analysis toolkit. Much of this toolkit is highly simplistic, as the math was done with pen and paper in the old days. Lack of computing power meant that everything had to be simple.

The ATR measurement is perfectly adequate for most retail traders, and there really is not anything wrong with it. Having said that, as this is a book leaning more towards the quant spectrum, the models here will use a different measurement, one that you will see more on the professional side of the industry.

The basis of our volatility calculations will be standard deviation. The main source of confusion when using standard

deviation seems to come from the most basic question of what exactly we measure standard deviation of.

Clearly, it won't be helpful to measure standard deviation of prices themselves. This goes back to the same issue as we looked at earlier, in regards to regression. The base price of stocks can be very different, and we need to normalize for that somehow. The dollar variation of a stock trading at 500 and one trading at 10 can't be directly compared. But the percentage variation can.

We will therefore use daily percentage change as a basis for calculating the standard deviation, and use that as a proxy for volatility. In the financial industry, there are multiple ways of measuring volatility, but for our purposes here there is really no need to complicate matters. If you like, you could add a smoothing factor, such as exponentially weighted moving average of standard deviation, which is quite common. But a simple standard deviation measurement of percentage returns will do just fine for this model.

Luckily, calculating this is extremely simple in Python. We can do it in one single line of code. For the sake of convenience, we will make a function to use in the momentum trading model.

```
def volatility(ts):
  return ts.pct_change().rolling(vola_window).std().iloc[-1]
```

This function takes a price time series as input. That one line of code there shows the beauty of Pandas. This line of code does a few things for us. First, it calculates the percent difference between consecutive days. Then it gets a rolling window of that time series, the length of which is set by the model input factor vola\_windo w , as you will see at the top of the complete source for the model later in this chapter.

We then calculate the standard deviation of this rolling window, and finally get the last data point of that calculation and return it. All in one single line. Remember that we can slice off the last data point using the syntax [-1 ] .

### **Momentum Model Logic**

Now that you understand the momentum ranking logic and the volatility measurement that we need, it's time to construct a fully working momentum model. In my books, I always try to make clear that the models I present are meant as teaching tools. What I show are functioning models. The backtests are real. Well, valid anyhow. It would perhaps be a bit far to refer to any backtest as 'real'.

But I never tried to represent them as the Clenow Amazing Super System. Most of what I write is known by a lot of people in the investment management community. What I add is to try to make it more accessible, to teach a wider group of readers. I do try to add my own flair to things, but it's important not to confuse my demonstration models with the various claims out there to have secret and near magical trading systems which makes everyone millions and millions. Which of course will be sold to you for a few thousand bucks.

My models are not revolutionary. They are not meant to be the best possible way of doing things. They are teaching tools, explaining methodology you need to understand in order to develop industry grade strategies. I want you to understand the ideas and concepts well enough to build your own models, and expand your toolbox as an algorithmic trading professional. All models presented in this book can be improved upon, and I very much encourage you to attempt to do so.

The purpose of this particular model is to capture medium to long term momentum in the American stock markets. I want this model to be easy to manage, so we will only trade once a month. We are going to leave everything alone for an entire month at a time. This has a couple of advantages to higher frequency trading models. It allows a retail investor who has a day job to implement the rules without being overloaded with work. It also cuts down on turnover, which both reduces trading costs and more importantly reduces capital gains taxes, should you be unlucky enough to live in a jurisdiction that

has such taxes.

Our stock selection will be based entirely on the momentum score described earlier, using a time window of 125 days for calculation.

What I have come to realize in the past when writing about model settings, is that some readers tend to see the demonstration settings as recommended, or even the best possible settings. That's never the case. Most of the time when demonstrating models, I deliberately chose middle of the road kind of settings. I pick them more or less at random, from a set of reasonable values. The point is for you to try your own variations, and arrive at settings and tweaks which fits your own way of trading and your own requirements.

After all, the reason why I'm showing you all the source code in this book is so that you can test variations, take what you like and discard the rest.

Before I tell you the exact parameters we are going to use, I want to tell you why I have picked them. The logical thing to do would be to pick the best looking parameters, right? The ones that make the strategy look the best. Just run an optimization, fit the 'best' parameters and show the result. No, I'm not going to do that.

If I just showed you a curve fitted model, it wouldn't be all that useful. It would make things look great in a book, but it may not have much bearing on reality, nor would it be much of a learning experience. Instead, I'm going to show you a version of this momentum model which quite deliberately will not use the 'best' parameters, if there even is such a thing. The model here is meant for you to improve upon yourself.

Now, for this demonstration, I will use a momentum score of 125 days, meant to roughly represent half a year.

For this model, we are going to have a set target number of stocks. We need a reasonable diversification and for that more than

just a handful of stocks are required. So we will set the target number of stocks to 30. The number is chosen because it's reasonable. If we only hold 10 stocks, the single stock event risk would be quite high. A freak event in a single stock would have a very large impact on the overall results. That risk is mitigated when holding a broader portfolio. If we would pick too many stocks, we would have more work in executing and monitoring the portfolio and there would be a risk that the quality would suffer due to the inclusion of so many stocks.

All trading is done monthly, to keep costs and taxes reasonable. At the start of the backtest, we are going to rank the stocks in our universe based on the momentum score, and buy the top 30 stocks in the list, provided that they have a momentum score higher than 40.

This fairly arbitrary number, is to ensure that we are not buying flat or negative stocks. The idea is to buy strong stocks, not stocks that are falling less than others. If there are not enough positive momentums stocks at the moment, there is no point in buying the least bad ones.

The shorter momentum period you use, the more extreme the momentum score will be. That's because short term events are then extrapolated on a yearly basis, and can result in extreme numbers. So a filter based on the absolute level of momentum like this needs to be set higher for shorter momentum windows. Good to know if you want to experiment with the code yourself with setting different minimum required momentum levels.

While we initially buy the top ranked 30 stocks, we are not replacing all stocks with the current top list each month. We could do that, but it would likely result in a bit unnecessary trading. Consider a stock which keeps moving between position 30 and 31 on the ranking list. Would it really make sense to keep buying and selling due to such small ranking changes?

What we will do instead, is to keep our positions as long as they still have a momentum score of above 40 when it's time for the

monthly rebalancing. We will also sell stocks that left the index, which helps keep the backtest a bit more realistic.

#### **Downside Protection**

A well-known phenomenon is that momentum strategies tend to suffer in bear markets. Not just lose money, but often suffer substantially worse than the overall market. That's why many momentum ETFs you might see are looking a little weak over the long run. They take an outsized beating during bear markets and struggle to make up for it during bull runs.

One way of dealing with this is to use an index level trend filter. In a similar model for my book Stocks on the Move, I used simple 200 day moving average, or rolling mean to use the fancy pants data sciency name for it. The idea is to simply not allow any new buys when the index is below the 200 day rolling mean of the daily closing price. That does not mean that current holdings are sold because the index dipped into bear mode, just that new stocks are not bought.

There is valid criticism of such an approach though. Some may argue that using such a crude trend filter is in itself a severe curve fitting. The gist of the argument is that we already know from experience that using such a long term trend filter will greatly mitigate damage from the two major bear markets of our generation. The question is of course if that has any predictive value in terms of avoiding the next.

The other point one could make is that if you include such a trend filter, you are really looking at two strategies, and not just one. There is a momentum strategy and a market timing strategy. Whether or not you want to use a trend filter is really a personal preference in the end.

For the model in this chapter, I won't employ such a trend filter

but I will post a version of on the book website, **[www.followingthetrend.com/trading-evolved](http://www.followingthetrend.com/python-book)** , where you can see how that could easily be done. This also helps keep the code amount down in this chapter, and should make it easier to absorb the information.

If you try it out and enable this trend filter, you will find that the performance improves. But again, you would need to decide for yourself if that amounts to cheating and curve fitting or not.

We do have some downside protection for this model though. We are relying on the minimum required momentum score, as explained earlier, to scale us out of the market in times of distress. As the general risk climate out there changes, and stocks start to fall, there will be fewer and fewer stocks available with sufficient momentum and we will automatically start scaling out at rebalance time. This strategy can theoretically be anywhere from 100% invested, to holding only cash.

In real life, holding large amounts of cash is almost always a bad idea. There was a time when you could be excused for viewing cash in a bank account as safe. But as someone who gets PTSD flashbacks from the number 2008, I can assure you that this is not the case anymore. People forget fast, unfortunately. There were a few weeks in 2008 where it seemed like any bank could go under at any time. When we were all hustling to move cash holdings, or overnight depos, from bank to bank at the end of business every day. Trying to pick the banks that are most likely to survive one more day.

The strategy we are looking at here scales out of stocks during bear markets, which of course tends to be when banks are more vulnerable than normal. Just imagine having made the right call and sold all your stocks early in 2008, holding cash and feeling smart, until you realize that all your cash was with Lehmann and now you are broke.

If your bank or broker goes poof, you will most likely recover any securities you held. Most likely. In case of fraud, anything can

happen. But in the much more common case of greed mixed with incompetence, your securities will be returned to you when the lawyers are done. The cash however, at least any amount exceeding government deposit guarantees, has gone on to the happy hunting grounds.

For that reason, you may want to look into ways to avoid or at least reduce holding cash. When there otherwise would be excess cash available on the books, one way would be to buy a fixed income ETF. For instance, putting excess capital in the 7-10 year treasury ETF (IEF). Where you want park your cash depends on what kind of risk you want to take. If the purpose is to take minimal risk, pick something short end like the 1-3 year treasury ETF (SHY). If you are happy to take on some price risk in the bond market, you could go with a longer duration vehicle like the 20+ year treasury ETF (TLT).

I will keep it clean here though, and let the model stay in actual cash. I would encourage you to take the code here, modify it to add cash management and see how it impacts the results.

#### **Momentum Model Source Code**

When reading the source code section of this chapter, or for the later chapters as well for that matter, it may help if you are by a computer and can open the actual source files in front of you. You can of course do without that and just skip back and forth between looking at the text and the code segments of this chapter, but it may be easier by a computer. If this is your first read through this book, you may want to simply skip this section for now, and return to it later.

In order to actually run this code, you would need to obtain your own data from a data provider and ingest the data to Zipline, which is described more in detail in chapter 23, as well as getting index membership data as we discussed earlier in this chapter.

In case you are wondering why I don't simply provide this data

on my website, so that you can run the code right away, the reason is that I would rather avoid spending the next year or so fending off law suits.

You can download the full source code for this model, as well as for anything else in this book from **[www.followingthetrend.com/trading-evolved](http://www.followingthetrend.com/python-book)** . But sadly not the price data.

The full source is at the end of this sector, but first have a look at interesting individual bits of it. At the top, as always, we import a bunch of libraries that we will have use for later on. After that, I've put the model settings. Having them right up on top makes it easy to try model variations, changing things around without having to touch the actual code.

#### %matplotlib inline

```
import zipline
from zipline.api import order_target_percent, symbol, \
  set_commission, set_slippage, schedule_function, \
  date_rules, time_rules
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import pyfolio as pf
import pandas as pd
import numpy as np
from scipy import stats
from zipline.finance.commission import PerDollar
from zipline.finance.slippage import VolumeShareSlippage, FixedSlippage
```

```
"""
```

Model Settings """ intial\_portfolio = 100000 momentum\_window = 125 minimum\_momentum = 40 portfolio\_size = 30 vola\_window = 20

""" Commission and Slippage Settings """ enable\_commission = True commission\_pct = 0.001

enable\_slippage = True slippage\_volume\_limit = 0.025 slippage\_impact = 0.05

In the next section of the code, you will find a few helper functions. Tools really, do accomplish specific and limited tasks for us.

The first one is the momentum score calculations, and that has already been discussed earlier in this chapter.

```
def momentum_score(ts):
  """
  Input: Price time series.
  Output: Annualized exponential regression slope,
       multiplied by the R2
  """
  # Make a list of consecutive numbers
  x = np.arange(len(ts))
  # Get logs
  log_ts = np.log(ts)
  # Calculate regression values
  slope, intercept, r_value, p_value, std_err = stats.linregress(x, log_ts)
  # Annualize percent
  annualized_slope = (np.power(np.exp(slope), 252) - 1) * 100
  #Adjust for fitness
  score = annualized_slope * (r_value ** 2)
  return score
```

Second, the volatility calculation, which we will use for position sizing and which has also been explained in this chapter.

```
def volatility(ts):
  return ts.pct_change().rolling(vola_window).std().iloc[-1]
```

And third, there is a helper function for all of us with short attention span. The next function will be called once a month, and it will simply output the percentage return for the previous month. We're not using that for anything, but it will give you something to look at while the backtest runs. Later in the book, we'll get to how you can make a bit fancier progress output.

def output\_progress(context):

"""

Output some performance numbers during backtest run This code just prints out the past month's performance

so that we have something to look at while the backtest runs. """

# Get today's date today = zipline.api.get\_datetime().date()

# Calculate percent difference since last month perf\_pct = (context.portfolio.portfolio\_value / context.last\_month) - 1

# Print performance, format as percent with two decimals. print("{} - Last Month Result: {:.2%}".format(today, perf\_pct))

# Remember today's portfolio value for next month's calculation context.last\_month = context.portfolio.portfolio\_value

Once we've gotten past these things, we're getting to the actual trading simulation. And the first part of that, just as before, is the startup routine. In initializatio n , we set the commission and slippage, if enabled, and then schedule a monthly rebalancing routine.

But we do one more important thing here. Do you remember in the beginning of this chapter how I mentioned that you need to care of historical index membership? Here, the code is assuming that you have a CSV file with this data. In this startup routine, initializatio n , we read this file from disk, and store in the contex t object so that we can easily access it during the backtest.

```
"""
Initialization and trading logic
"""
def initialize(context):
  # Set commission and slippage.
  if enable_commission:
    comm_model = PerDollar(cost=commission_pct)
  else:
```

```
comm_model = PerDollar(cost=0.0)
```

```
set_commission(comm_model)
```

```
if enable_slippage:
    slippage_model=VolumeShareSlippage(volume_limit=slippage_volume_limit,
price_impact=slippage_impact)
```

else: slippage\_model=FixedSlippage(spread=0.0) set\_slippage(slippage\_model)

# Used only for progress output. context.last\_month = intial\_portfolio

# Store index membership context.index\_members = pd.read\_csv('sp500.csv', index\_col=0, parse\_dates=[0])

#Schedule rebalance monthly. schedule\_function( func=rebalance, date\_rule=date\_rules.month\_start(), time\_rule=time\_rules.market\_open() )

After this, we are getting down to business. Next comes the monthly rebalance routine, and that, as they say on Cribs, is where the magic happens.

Remember that we scheduled rebalanc e to run once at the start of every month. The first thing we'll do in this routine is to print out the performance since last month, using the helper function we saw just earlier in this section.

```
def rebalance(context, data):
  # Write some progress output during the backtest
  output_progress(context)
```

Next we need to figure out which stocks were in the index on this trading day, so that we know which ones to analyze for momentum. This could easily be done in one line of code, but I'll break it up into multiple rows, just to make it easier to follow.

First, get today's date. By today in this context, I mean the current date in the backtest of course.

# First, get today's date today = zipline.api.get\_datetime()

Remember that we have already fetched and stored all the historical index compositions in initializ e . We read it from disk and stored in a variable which we called context.index\_member s , and we know that this variable contains a **DataFrame** with a date index for every date where the index changed, and a single column containing a comma separated text string with stock tickers.

Now we're going to first get all rows prior to the today's date.

# Second, get the index makeup for all days prior to today. all\_prior = context.index\_members.loc[context.index\_members.index < today]

Next we'll located the last row and the first column. The last row because that would be the latest date, and as we previously got rid of all dates higher than today, we now have the last known index composition date for the backtest. The **DataFrame** only contains one column, and as always we can access the first column by referencing the number zero.

```
# Now let's snag the first column of the last, i.e. latest, entry.
latest_day = all_prior.iloc[-1,0]
```

Now we have a long comma separated text string which we need to split into a list.

```
# Split the text string with tickers into a list
list_of_tickers = latest_day.split(',')
```

But it's not a list of stock tickers that we need, but a list of Zipline symbol objects. Easily done.

# Finally, get the Zipline symbols for the tickers todays\_universe = [symbol(ticker) for ticker in list\_of\_tickers]

All those lines of code will step by step get us the relevant list of stock symbols which were part of the index, and by our model rules are eligible to be traded. As I mentioned earlier, I broke this logic up into many rows to make it easier to follow. But we could have just as well done the entire thing in one line of code, like this below.

```
todays_universe = [
  symbol(ticker) for ticker in
  context.index_members.loc[context.index_members.index < today].iloc[-1,0].split(',')
```

Fetching historical data for all these stocks only takes a single row. There are 500 stocks in the index, but we can fetch all the historical close prices in this one row.

# Get historical data hist = data.history(todays\_universe, "close", momentum\_window, "1d")

Since we made a helper function earlier which calculates momentum score, we can now apply this function to the entire set of historical prices, again in a single row. The line below is very clever and a great part of how Python works. From the previous row, we have an object which contains historical pricing for about 500 stocks. The one line below will result in a sorted table of ranking score for all of them.

```
# Make momentum ranking table
ranking_table = hist.apply(momentum_score).sort_values(ascending=False)
```

That means that we now have the analytics we need to figure out our portfolio. We have the momentum ranking table, and that's the core part of the logic.

With portfolio models, it's generally easier to first figure out what to exit, and then figure out what to enter. That way, we know how much we need to buy to replace closed positions. Therefore, we'll loop through all the open positions, if any, and see which to close and which to keep.

""" Sell Logic

```
First we check if any existing position should be sold.
```

"""

]

```
kept_positions = list(context.portfolio.positions.keys())
for security in context.portfolio.positions:
```

if (security not in todays\_universe):

order\_target\_percent(security, 0.0)

```
kept_positions.remove(security)
```

```
elif ranking_table[security] < minimum_momentum:
```

<sup>\*</sup> Sell if stock is no longer part of index.

<sup>\*</sup> Sell if stock has too low momentum value.

order\_target\_percent(security, 0.0) kept\_positions.remove(security)

Now we have sold the positions that no longer qualified. Note how we first reacted a list of all the stocks in the portfolio, and then as any stock either dropped from the index or failed to maintain sufficient momentum, we closed it and removed it from the list of kept stocks.

After having closed positions we no longer want, it's time to decide which stocks should be added.

"""

Stock Selection Logic

```
Check how many stocks we are keeping from last month.
Fill from top of ranking list, until we reach the
desired total number of portfolio holdings.
"""
replacement_stocks = portfolio_size - len(kept_positions)
buy_list = ranking_table.loc[
  ~ranking_table.index.isin(kept_positions)][:replacement_stocks]
```

```
new_portfolio = pd.concat(
  (buy_list,
   ranking_table.loc[ranking_table.index.isin(kept_positions)])
)
```

The stock selection logic above first checks how many stocks we need to find. That'd be the difference between the target portfolio size of 30, and the number of stocks we're keeping from the previous month.

One of those rows may require an additional explanation. This row below, broken into two rows to make it display better in this book, uses some clever Python tricks.

```
buy_list = ranking_table.loc[
  ~ranking_table.index.isin(kept_positions)][:replacement_stocks]
```

The variable replacement\_stock s , calculated just earlier, tells us how many stocks we need to buy, to replace those that were sold. The variable ranking\_tabl e holds a list of all stocks in the index, sorted by the

momentum score. What we want to do is to pick stocks from the top of the ranking list, but without picking stocks which we already own and want to keep for the next month.

The first part of this row filters ranking\_tabl e to remove stocks which we intend to keep, so that we don't select them again. We do that with the tilde sign, ~, which is the logical equivalent of not. That means that ranking\_table.loc[~ranking\_table.index.isin(kept\_positions) ] will give us the stocks in the sorted ranking table, but without those that are to be kept. From there, we simply slice it as before, using the object[start:stop:step ] logic, starting from the beginning and stopping at the number of stocks we want. Easy, now that you know how, right?

Now we get the top ranked stocks in the momentum score list, excluding those that we already have, until we've filled up the target 30 stocks. Then combined the list of the buy list with the stocks that we already own, and presto, there's our new target portfolio.

But wait, we haven't traded yet. No, and we haven't even calculated trade sizes. Well, that's the only part left in this model.

We need to calculate the target weights for each stock, and place the order. Remember that we are using inverse volatility to scale position sizes. Each month we are recalculating all weights, and rebalancing all positions. That means that we are adjusting size for existing stocks as well.

Step number one would be to make a volatility table for all the stocks, using the volatility helper function we saw just earlier. After inverting these numbers, we can calculate how large each position should be, as a fraction of inverse volatility to the sum of the inverse volatility for all selected stocks. And now we have a table with target weights.

""" Calculate inverse volatility for stocks, and make target position weights. """ vola\_table = hist[new\_portfolio.index].apply(volatility) inv\_vola\_table = 1 / vola\_table

sum\_inv\_vola = np.sum(inv\_vola\_table) vola\_target\_weights = inv\_vola\_table / sum\_inv\_vola

```
for security, rank in new_portfolio.iteritems():
  weight = vola_target_weights[security]
  if security in kept_positions:
     order_target_percent(security, weight)
  else:
     if ranking_table[security] > minimum_momentum:
       order_target_percent(security, weight)
```

Having made a table of target weights, we can now go over the selected stocks on by one, and make the necessary trades. For stocks we already own, we just rebalance the size. If the stock is a new entry into the portfolio, we first check if it has sufficient momentum. If it does, we buy it. If not, we skip it and leave the calculated weight in cash.

We calculated the target weights based on arriving at 100% allocation for all 30 stocks. But as can be seen here, we might not end up buying all 50, if some fail the momentum criterion. That's by design. The space in the portfolio reserved for a stock that does not make the momentum cut, is then simply left in cash.

This acts as a risk reduction mechanism during bear markets. If there are not enough well performing stocks to buy, this model will start scaling down exposure, and it can go all the way down to zero exposure during prolonged bear market periods.

Here is the complete source code for the entire model.

%matplotlib inline import zipline from zipline.api import order\_target\_percent, symbol, \ set\_commission, set\_slippage, schedule\_function, \ date\_rules, time\_rules from datetime import datetime import pytz import matplotlib.pyplot as plt import pyfolio as pf import pandas as pd import numpy as np from scipy import stats

from zipline.finance.commission import PerDollar from zipline.finance.slippage import VolumeShareSlippage, FixedSlippage

""" Model Settings """ intial\_portfolio = 100000 momentum\_window = 125 minimum\_momentum = 40 portfolio\_size = 30 vola\_window = 20 """ Commission and Slippage Settings """ enable\_commission = True commission\_pct = 0.001 enable\_slippage = True slippage\_volume\_limit = 0.025 slippage\_impact = 0.05 """ Helper functions. """ def momentum\_score(ts): """ Input: Price time series. Output: Annualized exponential regression slope, multiplied by the R2 """ # Make a list of consecutive numbers x = np.arange(len(ts)) # Get logs log\_ts = np.log(ts) # Calculate regression values slope, intercept, r\_value, p\_value, std\_err = stats.linregress(x, log\_ts) # Annualize percent annualized\_slope = (np.power(np.exp(slope), 252) - 1) \* 100 #Adjust for fitness score = annualized\_slope \* (r\_value \*\* 2) return score def volatility(ts): return ts.pct\_change().rolling(vola\_window).std().iloc[-1] def output\_progress(context): """ Output some performance numbers during backtest run

This code just prints out the past month's performance

so that we have something to look at while the backtest runs. """

# Get today's date today = zipline.api.get\_datetime().date()

# Calculate percent difference since last month perf\_pct = (context.portfolio.portfolio\_value / context.last\_month) - 1

# Print performance, format as percent with two decimals. print("{} - Last Month Result: {:.2%}".format(today, perf\_pct))

# Remember today's portfolio value for next month's calculation context.last\_month = context.portfolio.portfolio\_value

"""

Initialization and trading logic """

def initialize(context):

```
# Set commission and slippage.
if enable_commission:
  comm_model = PerDollar(cost=commission_pct)
else:
  comm_model = PerDollar(cost=0.0)
set_commission(comm_model)
```

```
if enable_slippage:
    slippage_model=VolumeShareSlippage(volume_limit=slippage_volume_limit,
price_impact=slippage_impact)
  else:
    slippage_model=FixedSlippage(spread=0.0)
  set_slippage(slippage_model)
```

# Used only for progress output. context.last\_month = intial\_portfolio

```
# Store index membership
context.index_members = pd.read_csv('sp500.csv', index_col=0, parse_dates=[0])
```

#Schedule rebalance monthly. schedule\_function( func=rebalance,

date\_rule=date\_rules.month\_start(), time\_rule=time\_rules.market\_open()

)

def rebalance(context, data): # Write some progress output during the backtest output\_progress(context)

# Ok, let's find which stocks can be traded today.

# First, get today's date today = zipline.api.get\_datetime()

# Second, get the index makeup for all days prior to today. all\_prior = context.index\_members.loc[context.index\_members.index < today]

# Now let's snag the first column of the last, i.e. latest, entry. latest\_day = all\_prior.iloc[-1,0]

# Split the text string with tickers into a list list\_of\_tickers = latest\_day.split(',')

# Finally, get the Zipline symbols for the tickers todays\_universe = [symbol(ticker) for ticker in list\_of\_tickers]

# There's your daily universe. But we could of course have done this in one go. """

# This line below does the same thing, # using the same logic to fetch today's stocks.

todays\_universe = [ symbol(ticker) for ticker in context.index\_members.loc[context.index\_members.index < today].iloc[-1,0].split(',') ] """

# Get historical data hist = data.history(todays\_universe, "close", momentum\_window, "1d")

# Make momentum ranking table ranking\_table = hist.apply(momentum\_score).sort\_values(ascending=False) """ Sell Logic

First we check if any existing position should be sold. \* Sell if stock is no longer part of index. \* Sell if stock has too low momentum value. """ kept\_positions = list(context.portfolio.positions.keys()) for security in context.portfolio.positions: if (security not in todays\_universe): order\_target\_percent(security, 0.0) kept\_positions.remove(security) elif ranking\_table[security] < minimum\_momentum: order\_target\_percent(security, 0.0) kept\_positions.remove(security)

"""

Stock Selection Logic

Check how many stocks we are keeping from last month. Fill from top of ranking list, until we reach the desired total number of portfolio holdings. """ replacement\_stocks = portfolio\_size - len(kept\_positions) buy\_list = ranking\_table.loc[ ~ranking\_table.index.isin(kept\_positions)][:replacement\_stocks]

new\_portfolio = pd.concat( (buy\_list, ranking\_table.loc[ranking\_table.index.isin(kept\_positions)]) )

"""

Calculate inverse volatility for stocks, and make target position weights. """ vola\_table = hist[new\_portfolio.index].apply(volatility) inv\_vola\_table = 1 / vola\_table sum\_inv\_vola = np.sum(inv\_vola\_table) vola\_target\_weights = inv\_vola\_table / sum\_inv\_vola

```
for security, rank in new_portfolio.iteritems():
  weight = vola_target_weights[security]
  if security in kept_positions:
     order_target_percent(security, weight)
  else:
     if ranking_table[security] > minimum_momentum:
       order_target_percent(security, weight)
```

def analyze(context, perf):

perf['max'] = perf.portfolio\_value.cummax() perf['dd'] = (perf.portfolio\_value / perf['max']) - 1 maxdd = perf['dd'].min()

ann\_ret = (np.power((perf.portfolio\_value.iloc[-1] / perf.portfolio\_value.iloc[0]),(252 / len(perf)))) - 1

print("Annualized Return: {:.2%} Max Drawdown: {:.2%}".format(ann\_ret, maxdd))

return

```
start = datetime(1997, 1, 1, 8, 15, 12, 0, pytz.UTC)
end = datetime(2018, 12, 31, 8, 15, 12, 0, pytz.UTC)
perf = zipline.run_algorithm(
  start=start, end=end,
  initialize=initialize,
  analyze=analyze,
  capital_base=intial_portfolio,
  data_frequency = 'daily',
  bundle='ac_equities_db' )
```

#### **Performance**

This is where I intend to disappoint you, dear reader. Yes, you have made it all the way here, this far into the book, and now I will hold back some of the information from you. I won't give you the usual type of performance data for this model. I won't show a table with annualized return, maximum drawdown, Sharpe ratio and the usual. But I have good reasons for this. And it has nothing to do with being secretive, and everything to do with actually wanting to help you for real. Hear me out here.

If you want to learn for real, you need to do the work and crunch these numbers yourself. You need to properly understand what is going on. You need to learn every detail about how a model works, how it performs, what it's sensitive to or not, how it can be modified and a whole lot more. Simply taking my word for it, and trading the rules I described above would be a very bad idea. You wouldn't learn a thing.

I will put some graphs and tables with performance data, and you could figure out some from that. But I will refrain from the usual performance statistics, at least for now, in the hopes that you will be curious enough to try it out. After all, I'm giving you all you need in this book to replicate all this research.

This is a practical book, meant to teach you how to do things yourself. You get the full source code and you get full explanations. That's more than most trading books can claim. But this is not a book where you are supposed to simply trust the claims of the author and go follow his trading rules.

For this, and other models in the book, I will give you some idea of how it performs. I will show you the general profile of the performance and discuss the characteristics of the returns. This will give you a sufficient understanding of the model performance.

Avoiding these usual suspects of performance numbers up front also serves to reduce risks of another classic trap. If I published these numbers, some readers would immediately start comparing. First of course, which of the models in this book performs the 'best'. If there is such a thing. Next, how do these models stack up compared to some other book.

Neither of those comparisons would be helpful at this point. No matter who would 'win'. Such a comparison would simply be missing the plot. Comparing models across different books by different authors, likely using very different methodology would be pointless. Comparing within the book would likely lead you to be more interested in one model than another, for all the wrong reasons.

Backtests can be geared up and down to fit the return numbers you are looking for. And keep in mind that I could easily make the numbers like annualized return higher or lower, simply by choosing which year to start and end the backtest. The general profile and characteristics of the returns are a lot more interesting, and will help you properly understand the model.

Ok, so having said all of that, you will actually get a comparison between models, including the numbers you are likely looking for, later in this book. I would just prefer not to distract you with that at the moment.

And even more importantly, this book actually does offer an excellent method of evaluating trading model performance. But that's not written by me. My fellow author and friend Robert Carver has kindly contributed a guest chapter on that topic, chapter 22.

As for now, we just need to figure out if all the hassle of this chapter was worth it or not. If there seems to be any value in this sort of approach to trading, or if we should just abandon it and move on.

## **Equity Momentum Model Results**

Starting by taking a first glance at the monthly return numbers, as shown in Table 12.1, it looks promising. We can see that an overwhelming amount of years are positive. Many showing very strong numbers. There are double digit negative years, which is to be expected from a long only equity model, but no disaster years.

You can also clearly see that this model, while performing quite well in the past few years, performed quite a bit better in the earlier years of this backtest. This may be an interesting topic of research, for those at home who don't mind doing some extra homework.

| Year | Jan    | Feb     | $\mathbf{Mar}$ | $\mathbf{A}\mathbf{p}\mathbf{r}$ | May     | Jun     | Jul     | Aug     | Sep     | Oct     | Nov     | Dec     |
|------|--------|---------|----------------|----------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|
| 1997 | $+7.9$ | $-1.4$  | -3.0           | $+5.4$                           | $+5.9$  | $+4.0$  | $+10.7$ | $-0.5$  | $+5.2$  | -7.9    | $+0.2$  | $+0.1$  |
| 1998 | $-1.5$ | $+4.1$  | $+5.9$         | $+1.2$                           | $-2.1$  | $+8.0$  | $+1.4$  | $-13.5$ | $+10.3$ | $-1.0$  | $+1.3$  | $+5.8$  |
| 1999 | $+2.8$ | $-4.1$  | $+5.2$         | $+1.3$                           | $-1.0$  | $+9.2$  | $-1.6$  | $+0.1$  | -1.8    | $+0.6$  | $+12.9$ | $+14.6$ |
| 2000 | $-2.3$ | $+26.2$ | $-0.4$         | -3.3                             | -6.6    | $+12.3$ | -6.1    | $+4.4$  | $+1.5$  | $+1.4$  | $-4.6$  | $+9.3$  |
| 2001 | -7.4   | $+2.9$  | -2.0           | $+5.1$                           | $+3.2$  | $-0.7$  | $-0.5$  | -2.9    | $-11.0$ | $-1.1$  | $+3.5$  | $+0.8$  |
| 2002 | $-0.7$ | $+1.1$  | $+2.1$         | -0.9                             | $-0.0$  | -3.1    | $-12.0$ | $-2.5$  | $-0.2$  | $+0.4$  | $+0.7$  | -0.6    |
| 2003 | -6.3   | $-0.7$  | $+0.5$         | $+13.8$                          | $+11.1$ | $+1.8$  | $+1.6$  | $+4.7$  | $-1.1$  | $+10.0$ | $+4.7$  | -1.9    |
| 2004 | $+5.6$ | $+3.7$  | -0.6           | -2.9                             | $+2.1$  | $+3.4$  | $-3.5$  | $-1.6$  | $+2.7$  | $+3.1$  | $+8.1$  | $+0.3$  |
| 2005 | -3.0   | $+4.8$  | -2.4           | -5.6                             | $+3.5$  | $+5.4$  | $+3.2$  | -0.6    | $+3.8$  | -5.5    | $+3.9$  | $+1.6$  |
| 2006 | $+8.8$ | $-1.7$  | $+3.9$         | $-1.1$                           | -6.5    | $-0.7$  | -3.3    | $+1.2$  | $+0.1$  | $+1.6$  | $+2.4$  | $+0.9$  |
| 2007 | $+3.4$ | $-0.3$  | $+2.3$         | $+1.6$                           | $+4.4$  | -1.0    | -2.4    | $+1.3$  | $+5.3$  | $+3.7$  | $-4.8$  | $-0.3$  |
| 2008 | -9.7   | $+1.0$  | -0.8           | $+2.6$                           | $+1.2$  | -0.8    | $-10.2$ | -3.6    | -8.3    | -6.6    | $-0.3$  | $+0.1$  |
| 2009 | $-0.0$ | $-0.4$  | $+0.5$         | -1.0                             | $-1.0$  | $+0.2$  | $+10.1$ | $+5.1$  | $+4.5$  | -5.2    | $+5.1$  | $+7.6$  |
| 2010 | $-4.5$ | $+6.7$  | $+9.8$         | $+2.2$                           | -6.8    | -5.1    | $+3.2$  | -1.6    | $+4.6$  | $+1.2$  | $+0.5$  | $+2.7$  |
| 2011 | $-0.5$ | $+4.0$  | $+3.0$         | $-0.1$                           | -2.8    | -1.7    | $-1.5$  | -2.1    | -2.9    | $+1.2$  | $+0.2$  | -0.3    |
| 2012 | $+0.3$ | $+3.0$  | $+4.6$         | $+0.7$                           | $-10.0$ | $+3.7$  | $+0.1$  | $-0.4$  | $+1.1$  | -3.4    | $+1.8$  | $+1.5$  |
| 2013 | $+6.4$ | $+0.4$  | $+7.8$         | $-0.2$                           | $+6.3$  | -1.8    | $+5.6$  | -1.8    | $+5.5$  | $+6.2$  | $+4.0$  | $+1.8$  |
| 2014 | $+0.0$ | $+6.6$  | -0.8           | $+1.0$                           | $+1.6$  | $+2.8$  | $-2.1$  | $+5.2$  | -2.4    | $+0.6$  | $+3.4$  | $+0.8$  |
| 2015 | $+0.4$ | $+4.2$  | $+0.3$         | -3.7                             | $+2.8$  | $-0.6$  | $+0.5$  | -3.8    | $-0.0$  | $+4.3$  | $-0.4$  | $-0.8$  |
| 2016 | $-2.3$ | $+0.2$  | $+2.7$         | $-2.1$                           | $+0.6$  | $+6.1$  | $+2.7$  | -3.9    | $+1.7$  | $-4.1$  | $+7.1$  | $-0.2$  |
| 2017 | $+1.5$ | $+3.0$  | -2.4           | $+0.3$                           | $+4.2$  | -2.7    | $+2.1$  | $+1.3$  | $+0.8$  | $+4.3$  | $+3.3$  | $+1.1$  |
| 2018 | $+6.5$ | -3.8    | $-0.2$         | $+0.9$                           | $+0.5$  | $+0.3$  | $+0.5$  | $+5.1$  | $-0.2$  | -8.1    | $+1.4$  | $-8.1$  |

*Table 12.1 Equity Momentum Monthly Returns* 

The equity curve of the backtest, shown in Figure 12-4, gives you a broad picture of how this model behaves. The top two lines show the backtest portfolio value over time as well as the  $S\&P$  500 Total Return Index, for comparison. The middle chart pane plots the drawdown, and at the bottom you will find a rolling six month correlation between the strategy and the index.

You should not make the mistake of just checking if the strategy outperforms the index. That's not the most important information here. There are other details that will tell you much more about this strategy. One thing to look at is how the return curve levels out at times. This is when the exposure scales down, when there are not enough number of stocks available which fulfil the momentum criterion.

Second, look at the drawdown pattern. As could be expected, the drawdowns correspond quite well with known periods of market difficulties. That shouldn't be terribly surprising. After all, we are dealing with a long only equity strategy. And that leads to the bottom chart pane, which is vital to understand here.

The bottom pane shows the rolling correlation to the index. And as you see, this is usually very high. This is something that you really can't get away from, when you are building long only equity portfolio strategies. That means that it's unrealistic to expect them to perform well during times of market distress, and it's unrealistic to expect too large deviation from the market.

![](_page_38_Figure_0.jpeg)

*Figure 12*‑*4 Return curve for the equity momentum model*

Another way to get a feeling for long term performance of a strategy, is to make a holding period map, such as in Table 12.2. This shows what your annualized return would have been, had you had started this strategy at the start of a given year, as shown in the leftmost column, and held it for a certain number of years. The values are rounded to the nearest percent, mostly to make it fit on the pages of this book. If for instance the model had started in 1997 and traded for 10 years, it would have seen a compounded annualized gain of 16% per year. Not bad. But on the other hand, if it had started in January of 2001 and continued for 10 years, it would only have seen an annualized gain of 5%.

This type of table can help give you a different perspective on the returns than a simple graph can show. Later in this book, I will

show how to calculate such a table.

| Years | 1     | 2                                       | 3     | 4                      | 5     | 6                 | 7                            | 8         | 9     | 10                         | 11        | 12            | 13    | 14    | 15        | 16    | 17                 | 18    | 19      |  |
|-------|-------|-----------------------------------------|-------|------------------------|-------|-------------------|------------------------------|-----------|-------|----------------------------|-----------|---------------|-------|-------|-----------|-------|--------------------|-------|---------|--|
|       |       | $+28 +23 +30 $                          |       |                        |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 1997  |       |                                         |       |                        |       |                   | $+30 +21 +14 +17 $           |           |       | $+18 +17 +16 +15 +11 +12 $ |           |               |       |       |           |       | $+12 +11 +10 +12 $ | $+12$ | $+12 +$ |  |
| 1998  |       | +19 +30 +31 +19 +11 +16 +17 +16 +14 +14 |       |                        |       |                   |                              |           |       |                            |           | +9 +11 +11    |       | $+10$ |           |       | $+9 +11 +12 +11 $  |       | $+11 +$ |  |
| 1999  | $+43$ | $+37$                                   | $+19$ |                        |       |                   | $+9 +15 +16 +15 +14 +14 $    |           |       |                            |           | $+8 +10 +10 $ | $+9$  |       | $+8 +11 $ |       | $+11 +11 $         | $+10$ | $+11 +$ |  |
| 2000  | $+31$ | $+8$                                    | -0    |                        |       |                   | $+9 +11 +11 +10 +11$         |           | $+5$  | $+7$                       | $+7$      | $+6$          | $+6$  | $+9$  | +9        | $+9$  | $+9$               | $+9$  | $+8$    |  |
| 2001  | -11   | -13                                     | $+3$  | $+7$                   | $+7$  | $+7$              | $+8$                         | $+2$      | $+5$  | $+5$                       | $+4$      | $+4$          | $+7$  | $+8$  | $+7$      | $+8$  | $+8$               | $+7$  |         |  |
| 2002  | -15   |                                         |       | $+10 +14 +12 +11 +11 $ |       |                   | $+4$                         | $+7$      | $+7$  | $+6$                       | $+6$      | $+9$          | $+9$  | +9    | +9        | $+9$  | $+8$               |       |         |  |
| 2003  | $+43$ |                                         |       | $+32 +24 +19 $         | $+18$ | $+8$              |                              | $+10 +10$ | $+9$  |                            | $+8 +11 $ | $+12$         | $+11$ | $+11$ | $+11$     | $+10$ |                    |       |         |  |
| 2004  | $+22$ | $+15$                                   | $+12$ | $+12$                  | $+2$  | $+6$              | $+6$                         | $+5$      | $+5$  | $+8$                       | $+9$      | $+9$          | +9    | $+9$  | $+8$      |       |                    |       |         |  |
| 2005  | $+9$  | $+7$                                    | +9    | -3                     | $+3$  | $+4$              | $+3$                         | $+3$      | $+7$  | $+8$                       | $+8$      | $+8$          | $+8$  | $+7$  |           |       |                    |       |         |  |
| 2006  | $+5$  | $+9$                                    | -6    | $+1$                   | $+3$  | $+2$              | $+2$                         | $+7$      | $+8$  | $+8$                       | $+8$      | $+8$          | $+7$  |       |           |       |                    |       |         |  |
| 2007  | $+14$ | -12                                     | -0    | $+3$                   | $+2$  | $+2$              | $+7$                         | $+8$      | $+8$  | $+8$                       | $+9$      | $+7$          |       |       |           |       |                    |       |         |  |
| 2008  | -31   | -6                                      | -1    | -1                     | -1    | $+6$              | $+8$                         | $+7$      | $+7$  | $+8$                       | $+7$      |               |       |       |           |       |                    |       |         |  |
| 2009  | $+27$ | $+20$                                   | $+11$ |                        |       |                   | $+9 +16 +16 +14 +13 $        |           | $+14$ | $+12$                      |           |               |       |       |           |       |                    |       |         |  |
| 2010  | $+12$ | $+4$                                    | $+3 $ |                        |       |                   | +13 +14 +12 +11 +12          |           | $+10$ |                            |           |               |       |       |           |       |                    |       |         |  |
| 2011  | -4    |                                         |       |                        |       |                   | $-1$ +13 +14 +12 +11 +12 +10 |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2012  | $+2$  | $+23$                                   | $+21$ |                        |       | $+16 +15 +15 +12$ |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2013  | $+47$ |                                         |       | $+32 +21 +18 +18 +13$  |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2014  | $+18$ | $+10$                                   | $+9$  | $+11$                  | $+8$  |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2015  | $+3$  | $+5$                                    | +9    | $\pm 5$                |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2016  | $+8$  | $+13$                                   | $+6$  |                        |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2017  | $+18$ | $+5$                                    |       |                        |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |
| 2018  | -6    |                                         |       |                        |       |                   |                              |           |       |                            |           |               |       |       |           |       |                    |       |         |  |

<table>

 Table 12.2 Holding period returns for equity momentum
 model
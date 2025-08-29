# **Developing Trading Models**

Trading strategies can be broken down to a set of components. These components are always part of a trading strategy, or at least they should be. Failure to pay attention to all of them is likely to result in a flawed and non-performing model.

Too often, people pay far too much attention to just one of these components, and glossing over the rest. The one that seems to get the most attention is the entry method. How to decide when to open a position.

The fact of the matter is that the importance of entry method varies greatly. For some types of trading strategies, the entry method is critical. For other methods, it does not matter all that much. For a long term trend following model for instance, the exact entry method and timing is not very important. For a short term mean reversal model, the entry approach is critical.

## **Model Purpose**

Yes, your model needs to have a purpose. And no, that purpose is not " *to make money* ". Any trading model worth its salt is designed for a specific purpose, trading a specific market phenomenon to achieve a specific goal. If you don't know what your model purpose is, odds are that all you have got is a bunch of indicators thrown together and varied until a simulation showed some positive returns. A set of over optimized rules, which are very likely to fail in reality. A solid model trades a real market phenomenon, aiming for a certain type of return profile.

What you really want to avoid is what I would refer to as accidental models. From what I have seen, a large part of models developed by non-professionals are in fact accidental models.

An accidental model is what happens when you set out without a plan. When your purpose is simply to come up with something which makes money. Throw some indicator together, tweak settings, run optimizers, switch around indicators, values and instruments until, presto, you have got yourself a backtest that shows strong returns.

It's not all that difficult to build a backtest that shows great returns. The trick is to find predictive value going forward. If you just experimented with settings until the results looked good, all you have done is fitted the algorithm to the known data. That has no predictive value and is highly unlikely to continue to yield attractive returns on real life data, going forward.

A proper trading model needs to start off with a theory about market behavior. It needs to have a clearly stated purpose in what market phenomenon it's trading. A *raison d'etre* .

I have to confess that when I was first told about this idea, I thought it was hogwash. Whether I read it or was told, I do remember that it was sometime in the mid 90's. The question was put to me on what I believe about the market. It sounded like total nonsense. After all, all I believed about the market was that I could get rich quickly if I just figured out the right combination of indicators and settings for a trading system. The idea that I would somehow have a theory about exploitable market behavior seemed more than a little far-fetched at the time.

No need to worry if your initial reaction is the same. You will figure it out.

There are two common ways of looking at model purpose. One way may seem surprising for those who have not yet worked in the financial industry.

The first way is fairly straight forward. What you might expect. You start off with a theory of some sort. Perhaps something you have observed in the market, or something you read about. Now you want to test if it really works, and you formulate mathematical rules to test

that hypothesis. This is how most successful trading models start out.

The second and perhaps surprising way is based on a perceived need or business opportunity. Someone working full time with developing trading algorithms may not have the luxury of dreaming up anything he or she wants. You may have a specific brief, based on what the firm needs or what it thinks the market may need.

That brief may for example be to construct a long only equities model, where holding periods are long enough to qualify for long term capital gains tax, while having reasonably low correlation to existing equity strategies and have a downside protection mechanism. Or perhaps the brief is to study a type of strategy where competing asset management firms seem to be expanding and see if we can join in the competition for those allocations.

Often the return potential of a trading model may be of relatively low importance. The purpose may simply be to achieve a near zero or negative correlation to a currently used approach, while being able to scale to hundreds of millions, and preferably showing a modest positive expected return of a couple of percent per year. A model like that can greatly improve diversification for a large firm, and thereby enhance the overall long term performance of the firm's asset.

In particular at larger quant trading firms, model briefs are likely to start out with a business need. It's not a matter of finding a way to generate maximum return, as that rarely makes business sense.

The concept of starting from scratch with no specific requirements and just coming up with a model that makes the most amount of money is something very rare. This is a business like most others. In the auto industry, it wouldn't make sense for everyone to attempt to make a faster car than Bugatti. There is greater demand for Hyundai style of cars.

Either way, you need to start out with a plan, before you start thinking about trading rules or data.

## **Rules and Variations**

Generally speaking, you should aim for as few rules as possible and as few variations as possible.

Once you have arrived at a model purpose, you need to figure out how to formulate this purpose in terms of trading rules. These rules should be as simple and as few as you can muster. Robust trading models, those that work over the long run, tend to be the ones that keep things simple.

Any complexity you add needs to pay off. You should see complexity as something inherently bad, something which needs to justify its existence. Any complexity you want to add to your model needs to have a clear and meaningful benefit.

Moreover, any complication or rule that you add needs to have a real life explanation. You can't just add a rule just because it seems to improve backtest performance. The rule needs to fit into the logic of the model purpose and play a clear rule in achieving that purpose.

Once you have arrived at a set of rules for testing your market theory, you probably want to try some variations. Note that there is a world apart between testing variations and optimization.

As an example, let's assume that you want to test a mean reversion type of strategy. You believe that when a stock has fallen four standard deviations below its 60 day linear regression line, it tends to bounce two standard deviations up again.

Now you already have multiple parameters in play. Modeling and testing these rules is a fairly simple task. You could try a few variations of this, perhaps to expect the bounce by three or five standard deviations, using 30 or 90 day regression or a variation in the target bounce distance.

Making a few variations like this can be useful, both for testing parameter stability and to actually trade some variations of the rules to

mitigate over-fitting risks.

What you don't want to do is to run an optimizer to figure out that the optimal entry is at 3.78 standard deviations, on a 73 day regression, using a target of 1.54 standard deviations. Such data is absolute rubbish.

Optimizers will tell you what the perfect parameters was for the past. They will also con you into a false sense of security, and make you believe that they have any sort of predictive value. Which they don't.

No, skip the optimization. But make a few variations of the rules, using reasonable, sensible numbers.

### **Handling Data**

The process for how to use data for developing trading strategies, testing strategies and evaluating them is a controversial subject. It's also a subject which deserves books all by itself, and this book does not aim to go into any real depth on the subject.

A few things are important to understand in this context. Most important is to understand that the more you test strategies on a set of time-series data, the more biased your test will be. Whether conscious or not, you will be fitting your model to past data.

A simple example of this would be handling of 2008. If you are developing long equity models, you will quickly realize that what seemed to work great up until 2007 will suddenly show a massive drawdown in 2008. That was a pretty eventful year, and if there are readers here who are too young to be aware of it, all I can say is lucky you.

So now you probably just slap a filter of some sort on there to avoid this horrible year. That filter may have reduced profitability in earlier years, but in the long run it paid off.

This would be a great example of Brownian motion. No, not that sort. As in Doc Emmet Brown. As in time travel. No, I'm not going to apologize for that gag, no matter how bad it may be.

Adding a specific rule to deal with 2008 makes your backtests look great, but it may constitute over-fitting. The simulated 'track record', if you can call it that, will indicate that you would have performed amazingly during this exceptionally difficult year. But would you really?

Had the model been developed before that year, you would likely not have accounted for the possibility of a near implosion of the global financial system.

While there are various methods of alleviating risks of these sort of mistakes, the easiest is to use part of the data series for fitting and part of it for testing. That is, you only use a part of your timeseries data for developing your rules, and when you are done you test it on the unused part.

This is a subject which I recommend that you dig into deeper, but also a subject which would take up too much of this book if I go into too much details. Besides, Robert Carver (Carver, Systematic Trading, 2015) has already written a great book which covers this subject better than I could anyhow.

#### **Asset Class**

There are different perspectives you can take when classifying asset classes. It would be perfectly valid for instance to say that the main asset classes are stocks, bonds, currencies and commodities. For most market participants, that way of looking at asset classes makes the most sense.

But for systematic, quantitative traders, another definition may be more practical. When looking at the various markets we have

available to us, we can group them in different ways. One way to group asset classes would be to look at the type of instruments used to trade them. The type of instrument is, for a systematic trader, often more important than the properties of the underlying market.

This becomes particularly clear with futures, as we will soon see, where you can trade just about anything in a uniform manner. Futures behave quite differently than stocks, from a mechanical point of view, and that's important when building trading models.

The currency space is an interesting demonstration of this concept. You can trade spot currencies or you can trade currency futures. It's really the same underlying asset, but the mechanics of the two types of instruments is very different, and would need to be modeled in different ways.

For that reason, asset classes are in the context of this book based on the mechanical properties of the instruments.

We are mostly going to deal with equities and futures in this book. There are two reasons for that, which happily coincide. First, the backtesting software which will be introduced in this book supports only these two asset classes. Second, these happens to be the asset classes which I personally prefer and have most experience with.

#### **Investment Universe**

The investment universe is the set of markets you plan to trade. It's a very important factor to consider for your trading strategy. The assumption through this book is that you aim to trade a set of markets, and not just a single one. It's usually a bad idea to trade a single market and most professional grade strategies are designed as portfolio strategies.

If you would start off by picking a single market to trade, you have already made the most important decision. When someone sets

out to make a great model for capturing bull runs in the Dow Jones Index, he has already limited himself. Perhaps the strategy he designed is just fine, but this particular market may perform poorly for the next few years. No, diversification is the way to go. Apply your trading strategy on multiple markets, and your probabilities of success are much improved.

How you select your investment universe is of very high importance. What most people do, conscious or not, is to select markets that did very well in the recent past.

Investment universe selection works differently for different asset classes. Every asset class has unique issues and solutions, and we will look at specifics later on, in each asset class section of this book. One thing to keep in mind though, is that the greatest potential for catastrophic error in this regard lies in the equity sector.

### **Allocation and Risk Level**

Allocation is about how much risk you want to allocate to something. To a position, to a trading model, to a variation of a trading model, to a portfolio etc. It's a much wider topic than simple position sizing.

Ultimately, the question you want to answer is how much of an asset you should be holding. The way you get to the answer can be quite complex, and there may be many moving parts in play.

When you consider what approach to allocation to take, you need to think if in terms of risk. By risk, I mean the way the term is used in finance. This is a topic which is all too often misunderstood by retail traders.

Chapter 4 will deal more with financial risk, and this is an important topic. If you want to move from hobby trading to the world of professionals, the most important point to understand is risk and

how it relates to allocation.

The models in this book will aim for risk levels which are generally considered to be in the acceptable range for institutional asset management. They will aim for attractive enough return to be worth bothering with, while keeping the risk profile on a level which could be used in professional setting.

If on the other hand, you are looking for something spicier, I would recommend that you take a look at (Carver, Leveraged Trading, 2019). Yes, that's the second recommendation for the same author so either I really like his books or I'm being coerced to writing this book while being held in Rob's basement for the past year and plugging his books is the only way out.

### **Entry and Exit Rules**

This is the first thing that most people think of when designing a trading model. It's the most obvious part, but it's not necessarily the most important part.

Naturally any trading model needs rules for when to initiate a position and when to close it. For some types of strategies, the exact timing of these events can be of critical importance. But there are also strategies, often of longer time horizon, where the exact entry and exit points are of subordinate importance.

It wouldn't be fair to say that entry and exit rules are not important. Just keep in mind that they are not the only parts of a strategy that matters. Many portfolio based models rely more on what mix of positions you have at any given time than exactly when you opened them.

# **Rebalancing**

The rebalancing part is an often neglected part of trading models. While not necessary for many shorter term trading models, it can have a significant impact on models with a longer holding period.

Rebalancing is about maintaining a desired allocation. If you would get invited to look at the trade blotter for a systematic trading shop, you will likely see that there are a lot more trades done than you might expect. Even if the strategy is long term trend following, you may see that there position sizes are adjusted often, perhaps even every day. Small changes, up and down, back and forth, for no apparent reason.

You may see a long position opened in January one year and closed out in September. But in between those points, there may be a large amount of smaller trades, changing the position size up and down. You might wonder what caused the position to be increased or decreased. But that's not what happened.

These trades were rebalancing trades, aiming at maintaining the desired risk level. They were not changing the positon, merely maintaining it. Remember that most professional trading models aim to hold a certain amount of portfolio risk on a position. The risk calculation involves things like volatility of the instrument and the size of the portfolio. These things are not static.

As the volatility changes in a market, or your portfolio as a whole changes due to other positions, your position risk would change, and you would need to make adjustments just to maintain the same risk. That's what rebalancing is about.

Not every model requires rebalancing, and even if you decide not to employ it, you should still understand the concept and the implications of not rebalancing.
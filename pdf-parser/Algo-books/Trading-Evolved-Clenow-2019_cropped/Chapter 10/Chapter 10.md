### **Equities**

In the brilliant book Liars' Poker (Lewis, 1989), Michael Lewis writes about his time as a trainee at Salomon Brothers and how no one wanted to work in equities. The reason stated was that if you work in equities, your mother will understand what you do for a living.

Equities seems on the surface as the easiest asset class. Something that everyone understands and can participate in. At first glance, this may very well be true. But make no mistake. It's in no way easier to make money in equities than in other asset classes. And it is not easier to construct trading models for equities, at least not if you plan on doing it right.

As with most asset classes, equities have a few unique problematic aspects that you need to deal with. Since you made it this far into the book, it's a fair assumption that you actually plan to take quant modeling seriously and that means that we need to have a talk about equity methodology.

## **The Most Difficult Asset Class**

Stocks are a curious asset class in that they are both the easiest asset class to understand and the hardest to trade.

We all know what stocks are. It's not exactly like the CDS market which everyone has spent years pretending to understand after they almost blew up the world. No, stocks are simple and straight forward. A business builds something, sells it and makes money. And we are buying a part of that.

When we buy shares in a company, we are proud co-owners of the firm. But unless your name is Buffett, the percentage of your ownership share is likely so small that it's barely even theoretical.

That part is not all that important though. What is important is that we know what we are buying, or at least we think we do.

You like your iPhone and you get your three balanced meals a day from McDonalds like most people. So you go and buy shares in Apple and Mickey Dee. You know and like their products and understand what they do.

This is the part that's easy. To gain a high level understanding of what the company does and what it means to buy shares of it. Unfortunately, this is just an illusion.

The fact that you like a company's products does not in any way have an impact on the future share price, as so many enthusiastic buyers of Private Media Group found out the hard way.

Unless you are part of the top management or on the board of directors, your knowledge of the firm isn't unique and does not give you an edge. And if you happen to be in those categories, there are some pesky little laws against trading on it anyhow.

It's not that it's impossible to figure things out about a company and trade based on your views of their business. Not at all impossible. But it takes a whole lot more work than tasting the latte before investing in Starbucks. If you are just a casual observer, even a loyal customer or a long term employee, whatever you think you know about the company is known by everyone else as well and won't help you. It will more likely do just the opposite.

This illusion of special knowledge is just one of the dangers of the stock markets. The other danger is much more severe. The problem is that stocks are stocks and they tend to move more or less the same way.

When the stock markets are in a bullish state, almost all stocks move up. They also tend to move up on the same days, and down on the same days. Then a bear market comes along and they all move down at the same time.

Some stocks do better than others, but stock investing is generally a relative game. What that means is that you are really competing with the equity index. Obviously we all like to make money from an absolute point of view, but equity strategies tend to be at the mercy of the overall health of the markets. You can't realistically expect to see the same returns in a bull market and in a bear market, or to see the same type of strategies working in all market conditions.

The fact that stocks tend to move up and down at the same time means that they have a very high internal correlation. That means that, as a group, stocks are quite uniform. The real issue here is that we have a very limited diversification effect.

If you buy one stock, you have no diversification. If you buy a basket of 50 stocks, you have some diversification, but you are still just holding stocks. Your main risk factor is how the overall stock market index is doing. This is the main problem with stocks, and why it's the most difficult asset class. Some stocks are better than others, but in the end they are all just stocks.

This is not to say that it's a bad asset class to trade. It's just different and you need to be aware of the relative nature of it.

#### **A word on Methodology**

Methodology matters. It's a really horribly boring word and it sounds like something that the mid office should take care of for you, but unless you work for a large bank that's not likely to be the case. If you perform your research with flawed methodology, you will get flawed results. So we will take a moment first to look at how the simulations in the equity section of this book are done before showing the results. No, don't skip ahead. This is important.

There are two primary pitfalls when it comes to constructing equity models. The first has to do with deciding which stocks are

possible to trade, and the second concerns dividends. You will need to properly handle both of these issues, or your backtesting will be all for nothing.

## **Equity Investment Universe**

For equity portfolio type of models, you have a vast number of markets to choose from, in theory. To increase realism, you need to ensure that your algorithm only considers trading stocks which would reasonably have been considered in reality at the time.

It's easy to pick stocks that you know and are familiar with, say like Google, Apple and the like. The obvious problem here is that you know these stocks because they have strongly increased in value. You probably didn't pick Global Crossing, Enron or Lehmann Brothers for your backtest, did you?

This is a very common mistake. Most people would instinctively pick a basket of stocks that they are familiar with and then make the logical leap of thinking that these are the same stocks you would have traded ten years ago. That's not terribly likely.

One solution to this would be to pick an index and trade the stocks in that index. But there is a trap here as well. If you were to pick the S&P 500 for instance, and then trade the constituent stocks, that might alleviate the issue somewhat. It would be logical to assume that a major index like this would have been a plausible pick even ten or twenty years ago. But only if you take the index joiners and leavers into account.

The current S&P 500 index constituents are not the same as the index's members ten years ago. Consider for a moment how an index, any index, is designed. Why the stocks are in there in the first place.

For almost all indexes, the stocks became members primarily because they fulfilled certain market capitalization criteria. That is,

they were suddenly worth enough to be considered. And how do you think that happened?

Stocks are included in an index because they have had strong performance in the past. It's hard to imagine these days, but Apple was once a tiny garage company run by a couple of hippies who made innovative products, did their own design and paid taxes. At one point their share price had moved up enough for them to get into small cap indexes. After a while longer of strong share price performance, they made their way into the mid-caps.

Much later, after they have already become one of the largest companies in the world, everyone dreams of having bought them 30 years earlier. It would be dangerous to allow a simulation such wishful thinking.

What we do here is instead to pick an index, and then consider only stocks that were members of that index on any given day. The simulations here are aware of when stocks joined and left the index, and are only allowed to hold stocks that were really part of the index on the relevant day.

This aims to reduce the effect of so called survivorship bias. It can be a little tricky to implement, and that's probably the most difficult aspect of developing trading models for stocks. While this can be approached in multiple ways, you will find one possible solution in chapter 24, which deals with data and databases.

You could of course work with other types of data to achieve more or less the same thing. One way would be to look at historical market capitalization or traded volume to construct an investment universe which would be a reasonable approximation of what you may have considered at a given point in time.

# **Dividends**

Next we need to deal with dividends. There are other things to adjust for as well, such as splits and similar corporate actions, but you generally don't really need to worry about those. Everything but cash dividends is easy and it's very likely that any stock price history you will ever look at is already adjusted for the rest. When a stock has a 2:1 split, you won't see the share price take a 50% nose dive. Instead, you see the history back in time automatically adjusted for you, so that the split does not have an impact. Splits and similar are simple events with simple solutions and they don't impact your profit or loss at all.

What you do need to worry about is cash dividends. There is no easy answer here, but there are various ways to deal with the issue. Clearly, the worst way to deal with it is to pretend that they don't exist. Over multiple years, dividends will have a significant impact.

There are two different methods for dealing with dividends. The easiest would be to use total return series. The total return series for a stock shows you, as the name aptly implies, the total return you would have realized in the stock, assuming all dividends are directly reinvested into the same stock. So you are holding 200 shares of ACME Inc. trading at 10 dollars a share. Now there is a dividend of 50 cents, and you are the lucky recipient of a crisp Ben Franklin. The total return series assume that Mr. Franklin is immediately used to shop for more ACME at market.

To reflect this in the time series, the entire series back in time will now be adjusted so that the percent gain or loss on buying and holding the stock matches. Note that this means that if you check the price of the stock a year ago, or ten years ago, it may greatly deviate from the actual nominal price at the time. The time series now reflects price and dividend, assuming full reinvestment.

The other way might be easier to relate to, and is even more realistic, but can be a little tricky to model. This method assumes that when dividends are paid, they are actually paid in cash. Just like in real life. We leave the price series alone and just credit the cash holdings with the appropriate amount.

Since we don't change the price series, the charts will reflect the actual prices in the markets, and not the artificially adjusted price that the total return method would present. We are also presented with the very real problem of what to actually do with new cash. They can drop in on the account when you least want them, and now you need to decide how to deal with it. Realistic, but potentially complex to model if your software is not already set up for it, and if you lack proper dividend data.

The total return method is good enough for the most part and very easy to model. The downside is that total return series are hard to come by for free. The usual suspects of free stock history providers on the internet are not likely to give it to you.

The second method is better and worth doing if you want to have a more realistic backtest. The good news is that Zipline, the backtester that I'm using for the purpose of this book, can handle the dividends for us. We just need to make sure that the dividend data is supplied, and the logic is then done by the backtester.

You will find a detailed technical explanation of how to import your stock pricing data, as well as dividend data, in chapters 23 and 24.
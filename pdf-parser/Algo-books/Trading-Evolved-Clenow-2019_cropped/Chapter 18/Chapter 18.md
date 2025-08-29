## **Comparing and Combining Models**

On the futures side, we have now looked at a few different approaches. First, a standard trend model with trend filter, trailing stop, and breakout logic. Second, a simple time return model that only compares a monthly price with that of a year and half a year prior. Third, counter trend, or mean reversion approach which aims to enter when trend followers stop out, operating on a shorter time period. And finally a carry based trading model, looking only at the shape of the term structures curve.

We also started off with a systematic equity momentum model, which trades only the long side of equities and should have quite a different return profile from absolute return futures models.

In the chapter about each of these models, you have probably noticed that I did not show the usual return statistics. That was very much on purpose, as I have come to realize that many readers stare too much as such figures, and miss the bigger picture. It's a bit like handing out slide printouts before a live presentation. No one is going to listen to what you have to say after that.

But now that you have presumably already worked your way through the previous chapters, it should be safe enough to show you the stats. The data you are looking for is in Table 19.1, where the strategies that we looked at earlier are listed, as well as the same statistics for the S&P 500 Total Return Index, all covering the backtesting period from the start of 2001 to the end of 2018.

|                     | Annualized<br>Return | Max<br>Drawdown | Annualized<br>Volatility | Sharpe<br>Ratio | Calmar<br>Ratio | Sortino<br>Ratio |
|---------------------|----------------------|-----------------|--------------------------|-----------------|-----------------|------------------|
| trend_model         | 12.12%               | -25.48%         | 19.35%                   | 0.69            | 0.48            | 0.98             |
| counter_trend       | 11.00%               | -30.09%         | 18.55%                   | 0.66            | 0.37            | 0.92             |
| curve_trading       | 14.89%               | -23.89%         | 18.62%                   | 0.84            | 0.62            | 1.22             |
| time_return         | 11.78%               | -40.31%         | 21.09%                   | 0.63            | 0.29            | 0.9              |
| systematic_momentum | 7.84%                | -39.83%         | 16.48%                   | 0.54            | 0.2             | 0.76             |
| SPXTR               | 5.60%                | -55.25%         | 18.92%                   | 0.38            | 0.1             | 0.5              |

*Table 19.1 Futures Strategies Statistics*

Clearly the curve trading model is the best one, right? And the momentum isn't worth bothering with? Well, conclusions like that are the reason why I did not show these simple statistics earlier. Evaluating trading models is a more complex undertaking than simply looking at a table like this. You need to study the details, and study the long term return profile. And of course scalability. At the sharp end of the business, you often look for a specific behavior in the return profile, often relative to other factors. The answer to which model is more promising depends on what you happen to be looking for at the moment, and what would fit or complement your current portfolio of models.

All of these models are simple demo models. They are teaching tools, not production grade models. But they all show potential, and they can be polished up to become production grade models.

You can also see that all of them are orders of magnitudes more attractive than a buy and hold, stock market approach. Some readers may be surprised to see just how meager the return of the stock markets are over time. In this period, from 2001 to 2018, the S&P 500 returned less than 6% per year, even with dividends included and even with the last ten years of bull market included. And that was

at a peak drawdown of over half.

Another point that may surprise some is the level of the Sharpe ratios. None are over 1. There is an unfortunate misconception that a Sharpe of less than one is poor. That's not necessarily so. In fact, for systematic strategies it's unusual to see realized Sharpe ratios of over one.

![](_page_2_Figure_2.jpeg)

*Figure 19*‑*1 Comparing Futures Models*

Figure 19‑1 shows the long term development of these five strategies, compared to that of the stock market. On such a long time scale, the index comparison hardly seems fair. But the fact is that in the shorter run, you will always be compared to it. This is the curse of the business.

Remember that the reason that these backtests start in 2001 is that a current, and hopefully soon addressed issue in Zipline makes it tricky to use pre-2000 data. The fact that the equity index starts off with a nose dive might make this comparison a little unfair, and for that reason, I will also show you the same graph starting in 2003, the bottom of the bear market. I won't do one from the bottom of the 2008-2009 bear market. That would just be plain silly. Comparing

perfect market timing into the longest lasting bull market of a generation with alternative strategies does not make any sense.

![](_page_3_Figure_1.jpeg)

*Figure 19*‑*2 Comparison, starting from 2003*

Even if we would have had the foresight of buying the index with impeccable timing at the bottom of the tech crash, the index would still have shown lower return and deeper drawdowns.

## **Combining the Models**

Everyone knows that diversification is beneficial. At least everyone should know that. But most people think of diversification only in terms of holding multiple positions. That's all fine and well, but you can also find added value in diversifying trading styles. Think of a single trading model as a portfolio component.

What you may find is that an overall portfolio of models can perform significantly better than any of the individual strategies that goes into it. I will demonstrate this with a simple portfolio, consisting of the five trading models we have seen so far.

As we have five models, we will allocate an equal weight of 20% of our capital to each. The rebalance period is monthly, meaning that we would need to adjust all positions accordingly each month, resetting the weight to the target 20%. Such a rebalance frequency on a model level can be both difficult and time consuming for smaller accounts, but is perfectly reasonable on a larger scale. Feel free to repeat this experiment with yearly data if you like. Making portfolio calculations like this is an area where Python shines compared to other languages.

You can read about how this portfolio combination was calculated and see the code for it in chapter 20.

|                     | Annualized<br>Return | Max<br>Drawdown | Annualized<br>Volatility | Sharpe<br>Ratio | Calmar<br>Ratio | Sortino<br>Ratio |
|---------------------|----------------------|-----------------|--------------------------|-----------------|-----------------|------------------|
| trend_model         | 12.12%               | -25.48%         | 19.35%                   | 0.69            | 0.48            | 0.98             |
| counter_trend       | 11.00%               | -30.09%         | 18.55%                   | 0.66            | 0.37            | 0.92             |
| curve_trading       | 14.89%               | -23.89%         | 18.62%                   | 0.84            | 0.62            | 1.22             |
| time_return         | 11.78%               | -40.31%         | 21.09%                   | 0.63            | 0.29            | 0.9              |
| systematic_momentum | 7.84%                | -39.83%         | 16.48%                   | 0.54            | 0.2             | 0.76             |
| Combined            | 14.92%               | -17.55%         | 11.81%                   | 1.24            | 0.85            | 1.79             |

*Table 19.2 Portfolio of Futures Models*

Table 19.2 shows a comparison of the performance of each individual model, as well as the overall stock market, to that of the combined portfolio. These numbers should be abundantly clear. The combined portfolio far outperformed each individual strategy, at lower volatility. We got a higher annualized return, a lower maximum drawdown, lower volatility, higher Sharpe, etc.

I hope this will help clarify my insistence on that you need to look at the detailed return profile when evaluating a new trading model. It's not necessarily the return per se that you are after, but

rather the profile of it, and how well it fits your existing models.

You may find a model with a low expected return over time, but which also has a low or negative correlation to other models, and thereby can greatly help your overall, combined portfolio of trading models.

![](_page_5_Figure_2.jpeg)

*Figure 19*‑*3 Portfolio of Trading Models*

You will also see in Figure 19‑3 as well as Table 19.3 that the overall return profile seems significantly more attractive, once the models are combined. As the individual models often have their gains and losses as different times from each other, they complement each other well and help smooth out long term volatility. The drawdowns become subdued, resulting in a higher long term return.

While it was a close call some years, in the end, not a single year of this combined portfolio ended up losing money.

| Years | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|-------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 2001  | 8  | 13 | 17 | 18 | 17 | 16 | 18 | 19 | 19 | 20 | 18 | 17 | 17 | 17 | 17 | 16 | 16 | 15 |
| 2002  | 18 | 22 | 22 | 20 | 17 | 19 | 21 | 20 | 21 | 20 | 18 | 18 | 18 | 17 | 16 | 16 | 15 |    |
| 2003  | 27 | 24 | 21 | 17 | 20 | 21 | 21 | 21 | 20 | 18 | 18 | 18 | 17 | 16 | 16 | 15 |    |    |

*Table 19.3 Holding Period Analysis for Combined Model*

| 2004 | 21 | 18 | 14 | 18 | 20 | 20 | 21 | 19 | 17 | 17 | 17 | 17 | 16 | 15 | 14 |  |  |
|------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|--|--|
| 2005 | 15 | 11 | 17 | 20 | 20 | 21 | 19 | 16 | 16 | 17 | 16 | 15 | 15 | 14 |    |  |  |
| 2006 | 7  | 18 | 21 | 21 | 22 | 19 | 17 | 16 | 17 | 16 | 15 | 15 | 14 |    |    |  |  |
| 2007 | 29 | 29 | 26 | 26 | 22 | 18 | 18 | 19 | 17 | 16 | 16 | 14 |    |    |    |  |  |
| 2008 | 29 | 24 | 24 | 20 | 16 | 16 | 17 | 16 | 15 | 14 | 13 |    |    |    |    |  |  |
| 2009 | 20 | 22 | 17 | 13 | 14 | 15 | 14 | 13 | 13 | 12 |    |    |    |    |    |  |  |
| 2010 | 25 | 16 | 11 | 12 | 14 | 13 | 12 | 12 | 11 |    |    |    |    |    |    |  |  |
| 2011 | 8  | 5  | 8  | 12 | 11 | 10 | 10 | 9  |    |    |    |    |    |    |    |  |  |
| 2012 | 1  | 8  | 13 | 12 | 10 | 11 | 9  |    |    |    |    |    |    |    |    |  |  |
| 2013 | 16 | 20 | 16 | 13 | 13 | 11 |    |    |    |    |    |    |    |    |    |  |  |
| 2014 | 24 | 16 | 12 | 12 | 10 |    |    |    |    |    |    |    |    |    |    |  |  |
| 2015 | 9  | 6  | 8  | 7  |    |    |    |    |    |    |    |    |    |    |    |  |  |
| 2016 | 4  | 8  | 6  |    |    |    |    |    |    |    |    |    |    |    |    |  |  |
| 2017 | 13 | 7  |    |    |    |    |    |    |    |    |    |    |    |    |    |  |  |
| 2018 | 2  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |  |  |

## **Implementing a Portfolio of Models**

While a demonstration like this may seem to show a simple solution to all your investment vows, implementation may not be as easy. Each of these models require millions to trade. Clearly, trading them all requires even more millions. I recognize that not every reader of this book has a spare hundred million laying around to be traded. But even if you are one of those unfortunate few non-billionaires out there, understanding the power of combining different approaches can be greatly helpful.

Insufficient funds is not the only potential problem with building portfolios of models. It can be highly complex in practice to implement the model combination shown in this chapter. As the complexity rises, you lack the simple overview which is possible with a single model, and you may need more sophisticated software to keep

track of positions, signals, risk allocation etc.

A professional trading organization can build the capability of trading such complex combinations, to monitor the risk and build proper reporting and analysis. For individual traders, this may not be a possibility.

Of course, there is another way to look at it. An understanding of how complex portfolios of models can be constructed and implemented can help you acquire the skillset needed to land a good job in the industry. Working at the sharp end of the industry has the potential to earn you far more money than you could possibly make trading your own portfolio.

Never forget that the interesting money in this business is made from trading other people's money. Whether or not you personally have the money to trade such models is not the important part. Well, it would be nice to have that of course. But you can still make use of this kind of knowledge and you can still profit from it. If you land a good job with a hedge fund or similar, you will probably get paid far more by working for them than you could by trading your own money anyhow.
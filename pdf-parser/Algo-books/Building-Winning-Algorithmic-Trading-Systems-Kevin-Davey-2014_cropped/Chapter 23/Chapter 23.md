# The Ins and Outs of Monitoring a Live Strategy

 $\mathbf{T}$ n factories, when a machine makes parts, the operations are closely monitored and the dimensions closely checked. The idea is to ensure that the part-making process is going smoothly, and to give an early warning signal when things are beginning to go bad. The same process holds true in evaluating live trading systems. I use a variety of tools to monitor strategies I am trading or that I am incubating.

The first chart I use is what I call a "bird's-eye view" chart, as shown in Figure 23.1. It tells me, at a glance, how my strategy has performed historically and in real time. To keep consistency, I use the same data source for all the data. In my case, it is the Trade List provided by TradeStation. You can get similar data from just about every trading platform. This is **not** actual real money data, which will be covered in later charts and metrics.

The point of this chart will be to gauge the general overall effectiveness of realtime performance (the portion of the curve on the right). Are the real-time data consistent with the historical test and the incubation period data? If not, there may be something amiss. Maybe the strategy has stopped working correctly, due to market conditions, for example. Or maybe the assumptions made in the strategy about limit order fills are not realistic. This could especially be true in scalping-type strategies, although really you may need actual real-money results to check that. Bad assumptions or strategy development technique up front may not show up in

![](_page_1_Figure_0.jpeg)

 **FIGURE 23.1** Bird's‐Eye Equity Chart

historical or incubation tests, but they certainly will be revealed when real money is on the line.

 I update this chart every few weeks and quickly review it. This gives me a general feeling whether my strategy is performing as expected. If it is, I can quickly move on to the next chart.

 If you don't know how to create an equity chart as shown in Figure 23.1 , here is how to create it.

## ■ **How to Build an Equity Curve (and a Drawdown Curve, Too!)**

 Sometimes, after 20‐plus years of trading, some tasks become so rote and routine to me that I forget that I had to learn them at one point. Such is the case with creating equity and drawdown curves. It is simple to me, but to someone who has never done it before, it can be a daunting task. So, I'll go through the math behind creating an equity curve and a drawdown curve.

#### **Equity Curve**

 The equity curve can be built on a closed trade‐by‐trade basis, or on any time scale you wish. I like using a daily equity chart, in part to eliminate the noise from intraday price changes. You can use your daily account statement to get your current equity balance.

Here is exactly how to build an equity curve based on daily data:

 Day 0 equity = Initial starting balance Day 1 equity = Day 0 equity + Change in equity during day 1 Day 2 equity = Day 1 equity + Change in equity during day 2 And so on …

Then, you simply plot the day X equity values, and you have your equity curve.

### **Drawdown Curve**

 The drawdown curve is the diff erence, on any given day, between that day's equity, and the *maximum* equity up to that point. So, let's say an account starts out with \$10,000 on day 0. On day 1, it hits a new equity high of \$10,500. The drawdown on day 1, since it is a new equity high, is \$0. On day 2, let's say the equity falls to \$9,700. Now, the drawdown on day 2 is \$10,500 − \$9,700 = \$800. And so it goes through the rest of the days. On days where a new equity is reached, the drawdown will simply be \$0. On all other days, the drawdown will be the diff erence between that day's equity and the maximum equity up until that point.

 Day X drawdown = Minimum of \$0 or (Day X equity − Max equity from day 0 to day X)

 A spreadsheet to create equity and drawdown curves is included at the web site (www.wiley.com/go/algotradingsystems) and the resource web site for this book.

## ■ **Monthly Summary Chart**

 When I used to work in aerospace (or the "real world," as I sometimes refer to it), our small company (\$250 million annual sales) would have a weekly sales and production meeting called "How We Doin'." Incorrect grammar aside, it was an excellent way for the managers of the company to quickly see how sales were for the month and quarter, what quality and production problems were occurring, and just a general sense of where the company currently stood.

 Now, fast‐forward a few years. I am trading full time, working alone. But I still want to see at a glance "how I'm doin'" with my strategies and trading. Obviously, my account statements and equity curve tell the overall story, but that is not enough detail for me. What strategies are doing well? Which are underperforming? Of strategies I am incubating, how do they look? Should I make some changes in what I am trading? This "how I'm doin'" report can help me answer all of these questions.

|                    | Expected<br>Ann<br>Return | Actual Ann<br>Return | Notional<br>Capital | Expected<br>Annual Gain | Actual Annual<br>Gain | Return<br>Efficiency | Worst<br>Drawdown | Actual<br>Monthly DD | Drawdown<br>Efficiency | Expected<br>Return/DD                          |
|--------------------|---------------------------|----------------------|---------------------|-------------------------|-----------------------|----------------------|-------------------|----------------------|------------------------|------------------------------------------------|
| 59 System          | 64%                       | 125%                 | \$12,500            | \$7.956                 | \$15,625              | 214%                 | $-4.812$          | $-4.538$             | 6%                     | 1.7                                            |
| 60 System 3        | 40%                       | 70%                  | \$150,000           | \$59,976                | \$105,576             | 198%                 | $-15,000$         |                      | 100%                   | 4.0                                            |
| 32 System 4        | 88%                       | 74%                  | \$25,000            | \$21,996                | \$18,472              | 146%                 | $-20,205$         | $-11.330$            | 44%                    | 1.1                                            |
| 3 System 6         | 253%                      | 12196                | \$15,000            | \$37,932                | \$18,130              | 88%                  | $-30,143$         | $-13,691$            | 55%                    | 1.3                                            |
| 64 System 5        | 144%                      | 108%                 | \$8,500             | \$12,268                | \$9,211               | 83%                  | $-1,700$          | $-1.028$             | 40%                    | 7.2                                            |
| 35 System 2        | 63%                       | 23%                  | \$12,500            | \$7.884                 | \$2.826               | 45%                  | $-14.205$         | $-4.159$             | 71%                    | 0.6<br>--------------------------------------- |
| Sub TRADED REAL \$ | 66%                       | 76%                  | \$223,500           | \$148,012               | \$169,840             | 115%                 | ( \$86, 065)      | (534, 746)           | 60%                    |                                                |

 **FIGURE 23.2** Monthly Summary Chart

 I developed a spreadsheet to help me with this task. It tells me at a glance how my strategies are performing, and I can easily drill down and see detail if I need to.

 First, there is a summary page, shown in Figure 23.2 . I include every strategy I am trading live on this page. I also include, in another section, the strategies I am currently incubating. This summary sheet collects all the data I am interested in (of course, if you did this yourself, you'd likely pick diff erent metrics than I did). This summary sheet gets the data from the individual sheets, which I will describe a bit later.

 To keep things simple, I base everything on one contract being traded, even though that is usually not what I am actually trading. Why? My goal with this spreadsheet is to see how my strategies are doing compared to how I thought (calculated) they'd be doing. If I included position sizing, it would muddy up the view for me.

Of all the numbers on this sheet, I am primarily interested in two columns:

- 1. *Return effi ciency.* How am I doing, compared to my expectations? That is how I defi ne return effi ciency, and it is simply my actual return divided by my expected return. If my strategy is performing exactly as I had calculated, it will be 100 percent. Obviously, I want this to be close to or above 100 percent. Typically, when I take all the strategies together, I fi nd my effi ciency is somewhere between 70 and 100 percent. So this says that if my historical testing says I should make \$10 a year, I am actually making somewhere between \$7 and \$10.
- 2. *Drawdown effi ciency.* This is how I am doing with regard to drawdown. Just like with return effi ciency, I calculate this as my actual drawdown divided by my expected drawdown. I then subtract the result from 1, to make the number 100 percent the ideal value. It is a bit backwards to do this, but I do it that way so that both effi ciency numbers have 100 percent as their ideal value. Then, the closer the effi ciencies get to zero, the worse off things are.

 Once a month, I go through and update each of the individual system sheets with performance data, and that automatically updates the main sheet.

 The monthly summary sheet reveals my current performance for all strategies. It gets data from the individual strategy sheets. I have one page of my spreadsheet for each of the strategies I am currently trading or incubating. Figure 23.3 shows the individual strategy summary sheet. It is pretty simple, yet pretty eff ective. I can see at a quick glance how a strategy is performing, compared to my expectations (which,

| Jan-<br>13<br>Cum Actual<br>(\$1,028)<br>0\$<br>Dec-<br>12<br>\$10,000<br>\$15,000<br>\$5,000<br>8<br>-\$5,000<br>(\$1,028)<br>Actual<br>S<br>TS reports, acct stmt<br>2013-02 EDandN<br>StratOpt WFP<br>TradeStation<br>Cum Expected<br>8/20/2013<br>(\$1,700)<br>2 strats<br>\$2,045<br>\$1,022<br>\$8,500<br>\$1,022<br>99<br>2<br>Jan-13<br>Feb-13<br>Dec-1<br>Max Intraday Drawdown:<br>Expected Monthly Profit:<br>Real Money Traded:<br>Actual Data Source:<br>Walk-forward Type:<br>Workspace Name:<br>Notional Capital:<br>Real Start Date:<br>Subscribers at:<br>Strategy Name:<br>Month |                  | Mar-<br>13<br>Feb-<br>13 | Jun- Jul-13 Aug-<br>13<br>1.1.1.<br>May-<br>١,<br>Apr- | Dec-<br>13<br>Nov-<br>Oct-<br>Sep- | Feb<br>14<br>I,<br>Jan-<br>14 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------------|--------------------------------------------------------|------------------------------------|-------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          |                                                        |                                    |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          | Expected Ann Return:                                   | 144%                               |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                  |                          | Actual Ann Return:                                     | %86                                |                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \$331<br>\$1,359 | N                        |                                                        |                                    |                               |
| (\$169)<br>(\$500)<br>\$3,067<br>13<br>Mar-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                  | $\mathfrak{S}$           | Expected Annual Gain:                                  | \$12,268                           |                               |
| \$249<br>\$418<br>\$4,089<br>Apr-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                  |                          | Actual Annual Gain:                                    | \$8,318                            |                               |
| \$2,280<br>\$2,031<br>\$5,112<br>May-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                  | w                        | Return Efficiency:                                     | 68%                                |                               |
| \$5,301<br>\$3,021<br>\$6,134<br>13<br>Jun-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                  | ω                        |                                                        |                                    |                               |
| 96,056<br>\$755<br>\$7,156<br>Jul-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                  |                          | Worst Drawdown:                                        | -\$1,700                           |                               |
| \$7,559<br>\$1,503<br>88,179<br>13<br>Aug-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                  | 00                       | Actual Worst Monthly DD:                               | -\$1,028                           |                               |
| 919.7\$<br>\$118<br>\$9,201<br>13<br>Sep-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                  | Ø                        | Drawdown Efficiency                                    | 40%                                |                               |
| \$6,932<br>(\$745)<br>\$10,223<br>Oct-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                  | ₽                        |                                                        |                                    |                               |
| \$11.246<br>Nov-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                  | $\equiv$                 | Min Ann Gain, 1,2 yrs, all                             | \$7,562                            |                               |
| \$12,268<br>Dec-13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                  | 4                        | Notes:                                                 |                                    |                               |

 **FIGURE 23.3** Individual System Monthly Chart

of course, are based on historical performance). When you have 30 to 50 strategies to keep track of, a quick summary like this is really invaluable.

 For many strategies I trade, that is all the information I need—a quick view at performance. If something catches my eye, I can always dig deeper.

 On a monthly basis, the only number I have to update is in the "actual" column. This represents the actual profi t or loss for the strategy for that particular month. It can be taken from trading statements, after adjusting for the number of contracts, or it can be taken from the strategy performance report. I typically do the latter. The expected numbers can all be obtained from walk‐forward historical testing.

 The max drawdown is obtained from the strategy report. Note that this is an intraday value, where the drawdown the spreadsheet calculates is on a monthly basis. This obviously is not totally correct, as ideally you would want to compare drawdowns over the same length of time. But for my purposes it is adequate.

 One way that the individual monthly performance chart can be of great assistance is by identifying strategies that are performing too well. Too well? Yes, performance that is too good can be a bad thing.

 An example is shown in Figure 23.4 . I started incubating this strategy a while back, and it took off .

 It was "too good to be true"—way above its historical norm. For that reason I decided to keep incubating it. The next few months are shown in Figure 23.5 .

 Now the strategy is in line with historical norms, but the standard deviation of monthly performance is a *killer* (look at the down‐month performances). I looked into it further and saw that the system was not acting normal. So I decided to keep incubating. Figure 23.6 shows what happened.

 This is a good example of (1) performance that is too good being a bad thing, (2) standard deviation of results (high degree of variability seen from visual inspection) being an early warning sign that things were not quite right, and (3) the monthly performance

![](_page_5_Figure_9.jpeg)

 **FIGURE 23.4** Superb Incubation Performance

![](_page_6_Figure_0.jpeg)

**FIGURE 23.5** Most Strategies Eventually Revert to Their Mean

report showing all this information in an easy-to-digest format. As an epilogue: I am still incubating this particular strategy but have not traded it with real money.

So far, I have discussed a few different ways to track the performance of a strategy. These tools are excellent for assessing the longer-term performance of a systemover a significant period of time (months to years), is the strategy performing as it should? While this "view from 35,000 feet" is useful to have, you also need to have measurements at the weekly or daily level. This helps answer the question: is my new strategy performing to expectations? I use a couple of different methods to review the shorter-term performance. There is a simple way and a complicated way. First, I'll look at the simple way.

![](_page_6_Figure_4.jpeg)

FIGURE 23.6 Incubating Even Longer

 The only data you need for this is the average trade or average daily result. If you have the standard deviation of this value, then you can do even more.

 All you do is plot your results, along with the equation "*n* \* *avg*" where *n* is the trade number/day, and "*avg*" is the average value. You'll get a chart like the one shown in Figure 23.7 .

 If you are above the average line, your strategy is doing better than you thought. If you are below, your strategy is worse.

 This chart becomes really useful as time goes on. Over 30 or more periods, you'd expect the strategy to be right around the average line. That is how I use it. Then, at a quick glance, I know the general state of the strategy. This chart is very similar to the monthly tracking chart shown earlier. It is nice, but it doesn't convey a lot of information, especially early on in the life of a live strategy. To get more insight, add two lines for the +/− standard deviation curves:

Upper curve: *n* \* *avg* + *sqrt*(*n*) \* (*std dev* ) \* *X*

Avg curve: 
$$n * avg$$

Lower curve: *n* \* *avg* − *sqrt*(*n*) \* (*std dev* ) \* *X*

where

*n* = The trade number

*avg* = The average profi t per trade

*std dev* = Standard deviation of the avg trade

*X* = Standard deviation multiplier

![](_page_7_Figure_12.jpeg)

 **FIGURE 23.7** Daily Performance Review

 What this tells you is that roughly 68 percent ( *X* = 1) or 95 percent ( *X* = 2) of the time, your equity curve should be within the upper or lower bands. Most well‐performing strategies will have their equity curve within the standard deviation bands. If the equity curve is outside of those bands, maybe there is something wrong with your strategy.

 Figure 23.8 shows a sample strategy, with *X* = 2 bands. The most interesting point here is the bottom curve, the −2 standard deviation line. Look as it starts negative and stays negative. Imagine that! A winning (positive expectancy) system can still have negative results for quite a while. Pure random chance (the order of trade results) can lead a winning system to appear to be a losing system.

 Of course, over time, the positive expectancy starts to dominate, and the lower curve will eventually turn positive. This has *huge* implications for the trader who "tweaks" his method if, after fi ve trades, he is not showing a profi t. He may well have just changed a winning system! This lower curve really shows that it takes time for even a winning system to show profi ts.

 Here is a great quote that explains it better than I can. It is from the book *Trading Bases* by Joe Peta (Penguin Books, 2013):

> Well, if you had the opportunity to invest in a venture with a positive expected value, like ownership of a roulette wheel, would you prefer to own it for one hour or nine and a half hours? Funny things can happen in one hour; there is no guarantee of a profi t even with the house edge. But over nine and a half hours, the natural fl uctuations inherent in the game will smooth out, and the chances of losing money will be very small, approaching zero over time.

![](_page_8_Figure_5.jpeg)

 **FIGURE 23.8** Daily Performance Review with Performance Bands

 Astute readers will recognize that the graph in Figure 23.8 uses standard deviation and therefore assumes the trade results have a normal distribution. In reality, most trading systems do not have a normal distribution. Rather, the distribution will likely have a spike in negative territory, where a stop loss might be placed, and they will have an extended tail on the profi t side, or a spike in positive territory, corresponding to a profi t target. An example of a real trading system histogram, versus the normally distributed version, is shown in Figure 23.9 . Depending on the specifi cs of the actual trades, assuming a normal distribution may be a bad idea.

 To alleviate this concern, we can simply take the Monte Carlo results from numerous runs and use percentiles based on them. This will provide a more accurate representation of the expected bounds of the trading system.

 A simple example can help explain this approach, before I apply it to the actual trading data. Assume that we have a trading system that averages \$100 per day, with a standard deviation of plus or minus \$50. With two standard deviation bands, we expect roughly 95 percent of the values to fall in between the upper and lower curves, or the 97.7 percentile on the upper end and 2.3 percentile on the lower end. If we then run Monte Carlo analysis on a trade‐by‐trade basis, for each trading day we simply select the values at the 2.3 and 97.7 percentiles. Since these values use the actual data, not an assumed normal distribution, they should be more accurate and representative of the actual trading system. The drawback is that the curves will not be smooth and could change if the simulation is rerun. Such are the penalties for using Monte Carlo analysis.

 If we run the day‐by‐day Monte Carlo analysis on the euro trading system, how do the curves compare? There is a good, but not perfect, match between the standard

![](_page_9_Figure_4.jpeg)

 **FIGURE 23.9** Histogram of a Typical Real Trading System

deviation and the Monte Carlo lines. Either is probably acceptable for tracking purposes. I personally like the Monte Carlo version, since it does not make any assumptions about the underlying data.

## ■ **How to Use This Graph**

 The daily tracking graph can be used to help you quit trading a system. For example, if the real‐time performance of your strategy falls below the lower 10 percent line, it could mean that your system is no longer working. After all, the odds were 90 percent that your strategy should be performing better than this. An example of a real‐world system should make this crystal clear.

 Figure 23.10 shows a sample case of a real‐world system I traded with my own money.

**Curve 1:** The system performance after 140 days. Barely positive, and close to the −1 Sigma line. That means, at that point, only 16 percent of the randomly generated equity curves, based on the historical back‐test trades, would have been worse than this.

 I'm sure most people would have stopped trading at this point. I did not, since I knew that even with the bad performance there was a chance that the system was not fundamentally broken.

**Curve 2:** The curve for the next 200+ days (Figure 23.11 ). I kept the system running, and now it is performing closer to its expected value.

 As I explained earlier, I use Monte Carlo simulation to determine if a strategy is performing to expectations. It is basically the same result as with using mean and

![](_page_10_Figure_8.jpeg)

 **FIGURE 23.10** 140‐Day Daily Performance

Y

![](_page_11_Figure_0.jpeg)

 **FIGURE 23.11** 200‐Day Daily Performance

standard deviation, except that you can include "boundary condition" eff ects with Monte Carlo (like quitting after a certain percentage drawdown or quitting when account gets blown out).

## ■ **Tracking Expected and Actual Performance**

 In all the examples I have shown in this chapter, I have used the performance numbers generated by the back‐testing software, which was TradeStation in my case. These numbers have built in certain assumptions about:

- Amount of slippage per trade.
- Amount of commissions per trade.
- Fill logic for limit orders.
- "Perfect" trading versus real‐world trading.

 Depending on your trading system and the values you put in the back‐test software, you may or may not have a realistic view of how your system will perform in the real world. I'm sure you've experienced this—you see a terrifi c‐looking equity curve only to fi nd out later that the creator did not include commissions or slippage in the performance data. Or you discovered an unbeatable scalping system for the mini S&P, only to discover, upon further review, that your back‐test engine assumed limit order fills as soon as the price was just touched, not when the limit order price was exceeded (this is a very common mistake, especially with many so‐called trading simulators out there). Finally, you will have Internet outages, data delays, and all sorts of other little gremlins. The point is that the performance you expect is not the performance that you'll get.

 If you are treating your trading as a business, it is imperative that you track actual performance and compare it to predicted performance. After all, when your actual performance is below your expected performance, isn't that akin to something or someone stealing from you? It sure feels that way to me—I fully anticipate to achieve the predicted performance or better, and when I don't, I search for and correct the reason.

 I track my actual performance on the daily tracking graph. I also keep a running table of actual versus predicted performance. Most of the time, the actual performance does slightly better than the predicted performance. This is a very good thing, as it shows that my assumptions for commissions, slippage, and the like were a bit on the conservative side. I'd rather be conservative in my estimates and be pleasantly surprised with actual performance, as opposed to underestimating slippage and later being disappointed.

Y
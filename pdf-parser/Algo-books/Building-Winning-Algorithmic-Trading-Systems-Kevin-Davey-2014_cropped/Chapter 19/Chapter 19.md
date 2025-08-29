# Monte Carlo Testing and Incubation

 $\mathcal{T}$ ith the walk-forward testing complete, based on the results I am confident I have a viable strategy. The equity curve for walk-forward testing looks nice, but at the same time I realize that there is no possible way the future equity curve will look exactly like the past equity curve. My hope, and the hope of all developers at this stage, is that the components of the equity curve (i.e., individual trades) are roughly the same as the walk-forward history. The easiest way to imagine this is to think about the average trade profit and its standard deviation (scatter). If either of these values significantly changes, the system might fail in the future. If, for example, the average trade turns negative, future performance will obviously be negative. Similarly, if the standard deviation increases, the drawdowns will likely be much more severe, the system will be harder to trade with position sizing, and the resulting equity curve will probably give you more ulcers.

Assuming, then, that the walk-forward trade performance will continue in the future, it becomes useful to see how the future performance might vary over time. For this analysis, I simulate one year's worth of trades with Monte Carlo analysis.

#### **Euro Day Strategy**

As previously discussed in Chapter 7, the only information required to do a simple Monte Carlo analysis is:

- Starting equity
- Quitting-point equity

163

- Number of trades in one year
- Individual trade results

 For any simulations that you run, you might want to simulate more than one year's worth of trades, or you might want to include position sizing, or you may even want to eliminate the quitting‐point equity—the point at which you stop trading. These particulars will be something you develop over time, as you determine what you like and don't like in the simulation. The exact method I use may not suit you, and that is fi ne.

 Once I have all the inputs for the Monte Carlo simulation, I simply enter them in the spreadsheet and press the "Calculate" button. Results are as shown in Figure 19.1 . For the day strategy, if I keep the risk of ruin below 10 percent (my personal threshold for ruin), I fi nd I need \$6,250 to begin trading this system, and in an "average" year I can expect:

- 23.7 percent maximum drawdown 129 percent return
- 5.45 return/drawdown ratio

 Other points of interest are that I have a 4 percent chance of ruin in that fi rst year, where my equity would drop below \$3,000. I also have a 94 percent probability of making money in that fi rst year (i.e., ending the year with more than \$6,250).

 Based on my goals and objectives, all of these parameters are acceptable, and I consider the Monte Carlo simulation results successful. Note that, based on your goals and objectives, this system—with the \$6,250 starting equity—may not be good enough for you. For example, many people want a near 0 percent chance of risk of ruin. Others may feel that 25.5 percent maximum drawdown is too high. The point is that what is right for me might not be right for you. That is why I think it is so important that you come up with your own goals and objectives. In the end, you need to feel comfortable trading what you have developed, and trading something that does not fi t you is a sure recipe for disaster.

# ■ **Euro Night Strategy**

 Now, I will perform the exact same procedure on the euro night strategy. Results are as shown in Figure 19.2 . For the night strategy, if I again keep the risk of ruin below 10 percent, I fi nd I need \$6,250 to begin trading this system, and in an "average" year I can expect:

- 25.0 percent maximum drawdown
- 52 percent return
- 2.0 return/drawdown ratio

M

![](_page_2_Figure_0.jpeg)

![](_page_2_Figure_1.jpeg)

![](_page_3_Figure_0.jpeg)

 **FIGURE 19.2** Monte Carlo Results, Euro Night Strategy

 Other points of interest are that I have a 6 percent chance of ruin in that fi rst year, where my equity would drop below \$3,000. I also have an 85 percent probability of making money in that fi rst year (i.e., ending the year with more than \$6,250).

 Note that this strategy is nowhere near as good as the euro day strategy. I expected this because of the goals of the night strategy. If you will recall, I was looking for a higher winning percentage strategy here, not one with necessarily a lot of profi t. Even so, the night strategy by itself meets my goals, although the return/drawdown ratio of only 2.0 is on the low end of acceptability. But since it meets my criteria, I can proceed to the fi nal Monte Carlo step.

# ■ **Euro Day and Night Strategy**

 While it is nice to know that either strategy, by itself, meets my performance criteria, what really matters to me is how the combined day and night strategy performs. Before I perform the Monte Carlo analysis, however, I have to do some data manipulation. In the previous simulations, I used individual trades for the inputs, which worked fi ne. But with the combined strategy, how do I ensure that the correct ratio and distribution of trades is taken to refl ect what really occurs when I trade both strategies together? Some days, only one strategy will trade, and on other days, both strategies will trade. I want to preserve this with the combined simulation.

 The solution to combining strategies into one strategy is to use the daily results, instead of the individual trade results. Then the net results on a given day will be considered as the results of one system. An example of how that works is shown in the "Combined" column of Table 19.1 .

 By utilizing this technique, we have preserved the characteristics of each strategy's trades, and just combined them into daily trades. A similar approach can be used to combine any two or more systems into one strategy. Simply compile results into daily results, and use that in the simulation.

 Once I have the trade data compiled into daily results, I can perform the Monte Carlo analysis on the combined euro day and night strategy. Results are as shown in Figure 19.3 . For the combined strategy, if I again keep the risk of ruin below

| TABLE 19.1 | Combine Daily Results on Multiple Systems to Get<br>"One" Combined System |            |          |
|------------|---------------------------------------------------------------------------|------------|----------|
| Date       | Euro Day                                                                  | Euro Night | Combined |
| 9/9/2013   | +\$100                                                                    |            | +\$100   |
| 9/10/2013  |                                                                           | +\$600     | +\$600   |
| 9/11/2013  | +\$100                                                                    | +\$250     | +\$350   |
| 9/12/2013  | −\$400                                                                    | −\$50      | −\$450   |
| 9/13/2013  |                                                                           | +\$100     | +\$100   |

![](_page_5_Figure_0.jpeg)

 **FIGURE 19.3** Monte Carlo Results, Both Strategies Combined

10 percent, I fi nd I need \$6,250 to begin trading this system, and in an "average" year I can expect:

 25.8 percent maximum drawdown 176 percent return 6.6 return/drawdown ratio

 Other points of interest are that I have a 5 percent chance of ruin in that fi rst year, where my equity would drop below \$3,000. I also have a 95 percent probability of making money in that fi rst year (i.e., ending the year with more than \$6,250).

 The most interesting aspect of this combined analysis is that the combined system is better than each system by itself. I'll repeat that: *the combined system is better than each by itself.* This is due to the diversifi cation eff ect, which I discussed in Chapter 15 . The return‐ to‐drawdown ratio, my primary metric in Monte Carlo analysis, increases from 5.5 to 6.6, which is a considerable increase. This is because by trading both systems, I get the combined return of the strategies, but on the downside the drawdowns do not combine. Rather, when one strategy is experiencing a drawdown, the other might be hitting new equity highs (or at least not new maximum drawdowns). Diversifi cation, by trading uncorrelated strategies, is what makes this possible.

 Looking at the Monte Carlo analysis as a whole, all my performance goals and objectives are met for the combined system. Therefore, I consider this analysis a "pass" and can now proceed to the next step: incubation.

### ■ **Incubation**

 At this point, I have 3.5 or so years of walk‐forward back‐test history. On top of that, I have about 5 months of "incubation" results, watching the euro day and night systems perform real time, with no changes to the original code (other than regularly scheduled reoptimizations).

 Walk‐forward results: July 2009–March 2013 Incubation results: March 2013–August 2013

 If the incubation results of the last 5 months "look" similar to the walk-forward results, I should feel comfortable going live with the strategy.

### ■ **Are Results Similar?**

 Here is how I determine if incubation and walk‐forward data "match." Keep in mind that I am not a statistician, so I tend to keep things simple, at the risk of not being 100 percent mathematically and scientifi cally rigorous. What I do passes a common‐ sense test, though. I use three methods to check for a match:

 1. *Student's t distribution test.* This statistical test will tell you if two data groups (the walk‐ forward results and the incubation results) are signifi cantly diff erent from each other.

 You can pretty easily do this in Excel (with the TTest function), or you can fi nd on online t‐test by searching with Google.

 When I run this test, it tells me that there is a 56 percent chance that these distributions are not diff erent. This gives me reasonable assurance that the strategies are performing in real time as they did historically. If, however, the chances of the strategies being diff erent were 0 to 20 percent, I might seriously wonder if I made a testing development mistake.

2. *Data distribution comparison.* I create two histograms of the data. The fi rst one is the actual data, and I lay the walk‐forward and the incubation results on top of each other. Do they look like they overlap? The second chart plots a theoretical normal curve histogram, based on the mean and standard deviation. I see a good amount of overlap in Figure 19.4 .

![](_page_7_Figure_6.jpeg)

 **FIGURE 19.4** Incubation Results—Data Distribution Comparison

![](_page_8_Figure_0.jpeg)

 **FIGURE 19.5** Incubation Results—Equity Curve Comparison

 3. *Equity curve comparison.* This is my favorite method, but it is not very scientifi c or mathematical. I simply plot all the data and create an equity curve. When I do that, can I see where the walk‐forward ends and incubation begins? If I can, that suggests something happened when incubation started, and that is usually a bad thing. If you wonder about this method, just create a strategy with optimized parameters, and then let it run live for a while. Most times, you'll notice a change in the curve. I do not see a radical change in the incubation portion of the curve, shown in Figure 19.5 . This is a good sign!

 Based on this analysis, I'd say the system is performing in incubation the same as it performed in its walk‐forward test. In fact, incubation is better than walk‐forward, which does concern me a bit (usually it is the other way around). But it is close enough to give me confi dence that I did not screw up during testing in development. It does not guarantee that when I go live, the system will be profi table—that is important to remember.

### ■ **Final Information**

 Once all the tests are complete, I can make a decision on whether to proceed with trading the system. Even if the strategy passes all the development steps, I still might decide not to trade it. Position sizing and correlation with other strategies are two possible reasons I might decide not to trade a specifi c strategy.

### ■ **Position Sizing**

 Although I discussed position sizing in more detail in Chapter 16 , I did not design the strategy specifi cally for any position sizing method. Of course, it is an important item to think about before I start trading with real money. A strategy can be great, but if reasonable position sizing cannot be applied to it, it just may not be worth trading with real money. This can occur when single contract losses are too big, and the account size needed to trade the strategy is prohibitively large.

 An example of this is a system very similar to one I developed and have been trading for a number of years. This system wins \$5,000 per contract on 50 percent of trades, and loses \$3,000 per contract on the other 50 percent. The average profi t/loss per trade is therefore \$1,000, and the Tharp expectancy is 0.33, which is indicative of a pretty good system. But how much money do you need to trade such a system? Assuming the strategy trades 20 times per year, and the quitting equity point is \$3,000, you need a \$20,000 account to have only a 6 percent chance of ruin. Plus, your maximum drawdown is likely to be 33 percent. That is just too much for many of us. To get a drawdown below 25 percent, one would need a \$35,000 account. This probably puts this system out of reach for most traders. Remember, this is trading only one contract. Using any kind of position sizing will make these drawdown and ruin numbers much worse. Thus, in your development process you may end up with a profi table system that you just can't trade.

# ■ **Correlation with Other Strategies**

 Before I start trading a strategy live, I always check the performance of the new system with systems I am already trading. I run a simple correlation of daily returns. This will tell me if the new strategy is highly correlated to any of my existing strategies. Obviously, trading two strategies that are highly correlated isn't a good idea unless you cut the position sizing of each in half. Otherwise, you may end up with too much exposure in a particular market or to a particular trading style. Many times, for strategies developed independently, this is not an issue, but it is always good to check.

# ■ **Monte Carlo—Consistency**

 One of the interesting side benefi ts of performing Monte Carlo analysis is that you can get an idea of your profi t consistency. Imagine you were manager of a casino. Over the course of fi ve minutes, your casino might make or lose money at the gambling tables. There is some randomness to the results, so even the house could lose money in a given short time frame. As the time increases, your chances of profi tability go up, and eventually approach near certainty. Your casino probably makes money

 The concept of a casino got me thinking that I'd really like to be profi table over a week, month, or year with my trading systems. Obviously, that is a function of my "roulette wheel"—my trading system and how much of an edge it provides. If I assume that my historical results will match my future results, I can use the Monte Carlo analysis to determine my odds of profi tability. From that number, I can determine how consistently profi table I am over any given time period.

 Using this idea, I ran the analysis on my euro day and night system. Before I reveal the results, keep in mind that this system on average will generate \$10,000 to \$12,000 profi t per year. It is a pretty good system. But will it provide a steady return stream? Here is what the results show:

- *Weekly* —59.6 percent of weeks should be profi table. So, within one year's time, I should make money 31 weeks and lose money 21 weeks. That's okay, but not really a great way to try to make a living.
- *Monthly* —74.8 percent of months should be profi table. In one year, three months will be down months. Again, not very steady returns—what if all three down months came in a row?
- *Quarterly* —86.2 percent of quarters should be profi table. I like that.
- *Yearly* —98.8 percent of years should be profi table. One losing year in a 30‐ to 40‐year trading career. That is very nice. The analysis says if I can live with the weekly and monthly uncertainty, then I'll be rewarded almost every year with at least some profi t.

 Obviously, before I ran this analysis I had to make some simplifying assumptions. For example, on average there are 151 trades per year in my trading system. That equates to three trades per week, on average. However, the actual number in any week could be zero, fi ve, or anywhere in between. Forcing it to be three every week leads to some error. But I don't think it would change the results by much. If I am looking for 90 percent of my weeks to be profi table, then my strategy obviously won't cut it, regardless of the assumptions I made.

 The next obvious question is: "What numbers should I require for each time period?" That will depend on the trader and his goals and objectives. A trader used to living paycheck to paycheck may require 95 percent winning weeks, or three losing weeks per year. He might know that more losing weeks than that will lead to eviction. A professional Commodity Trading Advisor (CTA) is measured on a monthly basis, so she might desire 95 percent of months to be profi table. A longer‐term trader, though, might care only about winning quarters or winning years. It all depends on the trader's circumstances.

 To take the whole analysis a step further, as you add good systems to your portfolio, your chances for profi table periods goes up. Sort of like the casino adding new table games to complement the roulette wheel.

# ■ **Eliminating Big Days**

 Eliminating the outlier trades from the history makes a huge diff erence in the results. In the history, there are 614 trading days represented. There are 20 days of profi ts greater than \$1,000. In one year of trading, I'd expect to see 5 of those "big" days. If they don't come, the system on average becomes only slightly profi table. My conclusion is that I am in deep trouble without those big winning days. The question is: is there a reason why I should not expect these kinds of days in the future? Maybe my system rules and variables basically were curve fi t to fi nd these big trades. With 10 to 20 big trades, I suppose that is a distinct possibility. However, it is not like these trades are due to a data anomaly or some back-test issue. Strategy 2 (euro day) was specifi cally set up to let profi ts run, and not to cap it. If I saw only a handful of large‐ profi t trades, I might suspect some sort of data or back‐test issue.

 One other interesting question: since I am relying on these "outliers" to generate most of the profi t, how likely is it that I even see many of them in a given year?

### ■ **Outlier Days**

 Since I know that the performance of my system is going to be driven by large‐ winning trades (outliers), it is interesting to see how many of these I could expect in a trading year. Here's what I found:

- In a year's time, I am likely to see four to six large‐winning trades. That is only one large‐winning trade every other month!
- There is less than a 10 percent (actually, 6.6 percent) chance of seeing eight or more large‐winning trades in a year.
- There is a 13.6 percent chance that I will have only zero, one, or two big winners in a year's time.

 This analysis is a bit sobering, and it does make one thing crystal clear: if I am to succeed with this system, I have to take every single trade because the one I miss just may be the big winner that only comes around once a year.

 Based on this data, my expectation for the system is a lot of fl at to slightly up or slightly down periods, punctuated by a large winner every once in a while. Why is this important to know? Having proper expectations is crucial to long‐term success. I can't get discouraged or lose confi dence in the system when I am not immediately making money. Knowing what to expect will help me a great deal, especially if I see very little happening day to day.
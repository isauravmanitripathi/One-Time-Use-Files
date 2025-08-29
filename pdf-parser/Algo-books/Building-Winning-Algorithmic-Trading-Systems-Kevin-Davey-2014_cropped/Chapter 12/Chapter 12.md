# Limited Testing

t this point, I'll assume you have the strategy coded, debugged, and ready to  $\boldsymbol{\Lambda}$  test. Unfortunately, when they get to this step, many traders will just test the strategy over the whole market history that they are interested in and see how profitable the strategy is. Some will go a step beyond this and actually run thousands or even millions of optimization iterations as part of this. What better way to see how good strategy can be than by running it to its extreme?

As you may have guessed, I am firmly against running these kinds of comprehensive tests. These tests may lead to a few great-looking optimized back tests but will almost always fail in real-time trading. Since successful real-time trading is the goal, shouldn't that be our success criteria, rather than a nice-looking back test?

The other major problem with testing on all the data is that once you test the data, you "burn" it. This means that any subsequent retests will be just a bit more curve fit, a bit more optimized. Think about it: You run strategy A over all your data. It looks good, but not great. You make a few minor tweaks and rule changes to your strategy and then test the new strategy B. Now, it yields much better results. You are ecstatic. But do you realize you just optimized? No, you did not optimize in the sense of running strategy A with optimized parameters, which is how most trading software describes optimization. But you certainly did optimize, as you tested both strategy A and strategy B, and picked the best one. Even though in this case strategy B has a better back test than strategy A, I'd believe the results of strategy A more (unless strategy B is much, much better than A), since A was run with untouched data.

Theoretically, you should run a strategy on a set of data one time, and one time only. If it works, great, but if it doesn't work, you should just move on to the next data set or instrument. That original data are tainted by your testing, to a degree. This is the point where theory and practice deviate. In actual practice, you will eventually test multiple strategies over the same data, maybe not right away, but eventually it

is inevitable. That is why you need to be careful. In my testing, I like to follow the teachings of Don Juan described in the book *Journey to Itxlan: The Lessons of Don Juan* (Simon & Schuster, 1972): "He taps it lightly, stays for as long as he needs to, and then swiftly moves away leaving hardly a mark."

 If you treat the data as fragile, you are more likely to avoid this issue. Treat your data with utmost care!

 Since testing with all the data is a no‐no, what is a reasonable and acceptable way to test a strategy? On one hand, you want to see if the core idea you developed has any merit to it; but on the other hand, you want the ability to add or change rules to the strategy, without falling victim to curve fi tting or hindsight bias. Also, you want to leave as much data in your dataset untouched as possible, since this will create a better and more realistic walk‐forward test (walk‐forward testing will be discussed in the next chapter).

 Given all these competing forces, I have found it best to do preliminary testing on a chunk of historical data, but not the whole data set. For example, if I have 10 years of data for my full test, I will do the preliminary limited testing described below on one or two years' worth of data. I try to use as little as possible, while still getting enough trades to be statistically meaningful. I will try to take the two years of data at random, not using the same data all the time or favoring any particular years.

 Some traders advocate testing fi rst on the "most interesting" data. For most commodities and futures, that would be the 2007–2009 time frame, when the world markets nearly collapsed. Their point is that if a system performs badly at this time, it will likely perform poorly at the next market shock. While I understand their approach, I respectfully disagree. I would try to avoid preliminary testing during the fi nancial crisis, since it may lead me to a system that performs well only during severe shocks and panics. While a system such as this might be nice at those times, I'd fear that the system would lose a lot more during the more prevalent "normal" times.

 If I take my two‐year chunk of data and adhere to the following process, I'll end up fairly certain whether my idea has any merit. The objective at the limited testing phase isn't to determine if a system is tradable; rather, it is used as a hurdle to see if the trading system has any potential. Frequently, I have trading strategies that survive the limited two‐year test but later fail the more rigorous tests. Only infrequently does the reverse occur, where I dismiss a strategy because of the limited results, and it turns out later to be a fantastic strategy.

# ■ **Entry Testing**

 The fi rst thing I usually want to know when testing a trading system is whether the entry has any usefulness. Many times, what looks like a good entry appears that way only because of the exits. Frequently it is diffi cult to know the true impact of entries when tested as a whole system.

When I evaluate entries by themselves, I typically perform the analysis three ways:

- Fixed‐stop and target exit
- Fixed‐bar exit
- Random exit

# **Fixed‐Stop and Target Exit**

 For the fi xed‐stop and target exit test, I simply choose a set stop‐loss and profi t target that is appropriate for the instrument and time frame I am trading. For a swing‐ type system lasting a few days, \$500 to \$1,500 is a reasonable amount for a stop‐loss. Similarly, I set an appropriate profi t target. All things being equal, if you set the stop and target to the same dollar amount, before commissions and slippage you should prevail on 50 percent of your trades, assuming that your entry is no better than random. Using set dollar amounts for stop and profi t, I simply create a strategy with my entry signal, set stop-loss, and set profi t target.

# **Fixed‐Bar Exit**

 For the fi xed‐bar exit test, I create an exit condition that closes the trade after X number of bars pass. The idea behind this is that most good trades show profi t right away and could be exited with a profi t almost immediately. If your entries don't show profi t until 10 or more bars, for example, perhaps your entry is too early and should be delayed. This test really helps to check if the entry signal gets you going in the correct direction.

# **Random Exit**

 For the random exit test, I typically use this as part of the "monkey test" process, described later. However, sometimes I use it right at the beginning of testing. The concept is based on eliminating the impact of any exit and just seeing the ability of the entry to generate winning trades. If an entry is always profi table with a randomly generated exit, then chances are much better that there is an edge there.

# **Entry Evaluation Criteria**

 For each of the three test techniques just described, there are a few ways to look at and analyze the results. Winning percentage, for example, is a very valid way to compare entries. If you test without slippage and commissions, your entry should be able to win more than 50 percent of the time, since that is what a random entry would give you. In my experience, I have found that 52 to 60 percent is achievable, and values that high suggest a worthwhile entry technique is present.

 The counterargument to using winning percentage is that, while it is nice to be right, it is even better to make money. A 60 percent winning percentage might make less money than a 40 percent winning percentage, especially if the entry is a trend‐ following entry. Trend‐following entries, such as breakouts and moving average crossovers, are generally much lower winning percentage systems. They get their revenge on high‐win‐percentage systems by yielding few big winners and many small losers, with the win amount easily outpacing the loss amount. In these situations, therefore, the average profi t per trade becomes useful.

 Since both winning percentage and average profi t give meaningful information, I use them both. Since this is preliminary testing, I do not worry about drawdown or any other metric. All I want to know at this point is if my entry seems to have any edge. These two metrics can help tell me that.

 You may be wondering about optimization at this point. Should you use it? I will, but when I look at the results, I will not just look at the best iterations. Instead, I look at all of them. For example, let's say I run 100 iterations, with various values for my entry input parameters. If only a handful of iterations are profi table or have a winning percentage above 50 percent, I will likely discard that system. But, if 70 percent or more of the iterations are favorable, then I will consider the entry as having successfully passed the test.

# ■ **Exit Testing**

 In a similar fashion to entry testing, there are a few diff erent ways to test an exit. Where it gets complicated is when the exit is tied to the entry is some fashion. An example of this might be using support lines for entries, and resistance lines for exits. It is hard to separate the two. In these cases, I might choose not to even test exits by themselves, and rather proceed to a complete system test, discussed later.

When I do evaluate exits by themselves, I typically perform the analysis two ways:

- Similar‐approach entry
- Random entry

# **Similar‐Approach Entry**

 The core idea behind testing exits by themselves is to see if they can help give you an edge. Most people see edges as being applicable only when you enter, but really, exits have just as much, if not more, impact on the bottom line. A carefully designed exit, it has been shown, can make even bad entry systems profi table!

 Since I will be testing the actual entry with the actual exit a bit later, at this point I want to see how the exit performs. To do this, I create an entry similar to the entry I want to use. This usually falls in one of two primary categories: trend following and countertrend following. Since I know what type of entry I have, I just create a generic one similar to it. For a trend‐following approach, for example, I may just employ an X‐bar breakout strategy. For a countertrend strategy, maybe I will use a relative strength index (RSI)‐based entry. In either case, I create an entry that is comparable to my actual entry. Then I test it with my exit strategy. A robust exit strategy that is profi table to my similar‐approach entries will likely also be profi table with my actual entry. This is a way to test an exit without involving the entry.

# **Random Entry**

 Discussed in a later section, if you have an exit strategy that works well with a random entry, you might have a really good system when you combine it with a solid entry technique. I do not use this approach as much as I used to, but occasionally I do like to see how a new exit technique works with random, no‐edge entries.

# ■ **Exit Evaluation Criteria**

 When I test exits by themselves, I generally do not look at winning percentages at all, and just focus on overall profi tability. In addition, I will use maximum favorable excursion (MFE) and maximum adverse excursion (MAE) as measurement criteria. With these metrics, the idea is that you do not want the exit to get you into too much trouble (adverse excursion), and you do not want it to give back too much of the potential profi t (found by comparing actual profi t to the favorable excursion). The trouble with these metrics, I have found, is that it becomes too easy to design just to these values, and in my experience that doesn't necessarily lead to better systems. They are good, though, to see the potential of your system.

# ■ **Core System Testing**

 Although there are benefi ts to testing the entry and exit signals by themselves (one being that you can always fi le away good entries and exits for use with another system), the interaction of entries and exits, as previously mentioned, is usually quite important. Regardless of whether I test entries and exits by themselves, I always test the complete core system during the preliminary phase.

 My objective in testing the whole system is to see whether, on a limited history of data, the strategy performs well. The main criteria I use at this point is net profi t, and I like to see profi table results over a wide range of variables and over most of the iterations. For example, if I have a simple breakout with 10 possible values of the breakout amount, and 10 stop‐loss/profi t values, that creates 10 × 10 = 100 iterations. I would expect a good strategy to be profi table over 70 or more of these iterations on the small data set. If I do see this type of behavior, I generally will run the monkey test shown later, and then go on to more in-depth testing.

Most of the time, the number of profitable iterations is on the order of 30 to 70 percent of total cases. This puts me in a "no man's land"—obviously, the strategy is not good enough as is, but there may be something there to work with. In situations like this, I may decide to add a rule, a filter, or otherwise change the entry and exit. Unfortunately, there is no set protocol for doing this. Many times, I'll use extra rules or conditions that I have had previous success with. Once I make some minor changes, I reevaluate my sample results.

The downside to this iterative process of modifying the rules is that you run the risk of fitting the system to the historical data. One or two modifications may be okay, but if you spend a lot of time modifying your strategy to get better results, you may very well fall into the "create a great-looking back test, but the real world performance suffers"-type scenario. Most times, if the first or second modification doesn't dramatically improve things, then the strategy is best left for the scrap heap.

As I have stated, when I do the preliminary testing with limited optimization, I like to see 70 percent or higher of cases with net profit, and I will work with the 30 to 70 percent cases a bit to see if I can improve them. But, what about strategies that are just awful, with less than 30 percent of iterations generating any profit? In these cases I use the George Costanza approach: if everything I built is bad, then the opposite must be good! I will reverse the signals and buy when I was selling, and vice versa. Depending on the strategy logic, this doesn't always produce the exact opposite result, but in many cases it is close. Without a doubt, though, this opposite effect is really apparent only before commissions and slippage are added in. Why is that? Well, take a trading system that has  $-$50$  average profit per trade, after \$30 commissions and slippage. That might be a decent candidate for an opposite approach, since many people will assume that it would average  $50 - 30 = 20$  per trade. But in reality, the opposite trade would be  $a - 10$  loser. When reversing systems, you must add in double the commissions and slippage. Here is the math:

-\$50 average trade, after slippage and commissions

 $+$ \$30 commission and slippage

 $-$20$  average trade, no slippage or commissions

Now flip the system to produce the opposite result, and then add commissions and slippage back in

+\$20 average trade, no slippage or commissions

 $-$30$  commission and slippage

 $-$10$  average trade, opposite system, with slippage and commissions

 I believe when people ponder trading the opposite system, they neglect to add in the commissions and slippage correctly. This is why most "opposite" systems, while appealing on the surface, rarely if ever work in the real world.

 At this point in the process, if my strategy has performed successfully, I will have tested the entry, the exit, and the core system, with all results suggesting that a tradable system *might* be achievable (remember, we have many more steps to go through before deciding a system is indeed tradable). This is just preliminary testing, the fi rst hurdle, but when I even make it this far, I am somewhat encouraged. At this point, it is on to the last step in the preliminary process. This step involves animals, at least on a fi gurative level.

# ■ **Monkey See, Monkey Do**

 One of the last tests I like to run is what I call "Monkey See, Monkey Do." The essence of the test is to see if my strategy does better than a dart‐throwing monkey. In 1973, a book by Burton Malkiel claimed that "throwing darts at a newspaper's fi nancial pages could select a portfolio that would do just as well as one carefully selected by experts." The book, "*A Random Walk Down Wall Street"* (W. W. Norton, 1973), is a classic for investors and traders, and the monkey idea resonated with many people. After all, no one wants to perform worse than a monkey! I personally don't subscribe to all the talk about markets being random—if I did, I would really have no business searching for a trading edge. Since prolonged edges would not exist in random markets, I fi nd the monkey test a very useful one.

 With any strategy I create, the strategy's performance better be signifi cantly improved over what any monkey could do by just throwing darts. If it is not, then I have no desire to trade such a strategy. I use three diff erent monkey tests and two diff erent time frames for testing. Passing all of the tests gives me confi dence I have something better than random.

# **Test 1: "Monkey Entry"**

 The fi rst test I run is to see if the entry I developed is better than random. I simply replace the entry in my strategy with an entry than creates a randomly generated entry. I run the random entry, with the rest of my strategy intact, 8,000 times. This generates 8,000 unique performance reports, since each run will have diff erent randomly generated entries. By adjusting the frequency of the entry signals, I ensure that I get close to the same number of trades as my walk‐forward history. Also, I try to match the percentage of long and short trades. These two conditions mean that the "monkey" trades as often as my system does, and in roughly the same proportion of long and short trades.

 Typically, a good strategy will beat the monkey 9 times out of 10 in net profi t and in maximum drawdown. For my 8,000 monkey trials, that means approximately 7,200 must have net profi t worse than my results, and the same number of runs with higher maximum drawdown than my walk‐forward results. If I don't reach these goals, I really have to wonder if my entry is truly better than random.

# **Test 2: "Monkey Exit"**

 The second test I run is to see if the exit I developed is better than random. It is much like the entry test, obviously, except in this case the monkey randomly exits the position. I control the random exit primarily by keeping the number of bars in a trade the same as my walk‐forward history. For example, if my walk‐forward history has an average of four bars per trade and always exits at the end of the day, I will tune the random exit to be on average the same. Also, it will always exit at the end of the day, if that is my criterion.

 As with the monkey entry, I look for my walk‐forward results to be better than 90 percent of the monkey exits.

# **Test 3: "Monkey Entry, Monkey Exit"**

 After determining that my strategy is better than both a monkey entry and a monkey exit, I like to see that my strategy is better than a monkey entry *and* exit. I do this because sometimes my edge is in the interaction of the entry and exit. For example, it might be that my entry is valid only because I set the exit near a support or resistance zone. It might be that the entry, taken alone, or the exit, taken alone, isn't enough without the other.

 In this test, I replace all entry and exit code with random monkey code. I adjust the parameters of the random entry and exit to match my strategy in the following ways:

- Number of trades
- Ratio of long trades to short trades
- Average bars spent in a trade

 Note that these conditions are the same I apply to the other monkey tests. Then I run the monkey entry, monkey exit strategy 8,000 times, just like the other tests, and compare results the same way.

# **Time Frames**

 The fi rst time I run the monkey tests is in the development stage, as one more hurdle for a strategy to overcome. Most of the time, though, running these tests over the walk‐forward time frame will almost always yield good results. This is because bad strategies will likely never get this far in the development process. Still, though, I like to see my strategy pass this test. It gives me confidence that I may indeed have an edge.

 The other time frame I use to run the monkey tests is when running the strategy live. I take the results of the past 6 to 12 months (3 months may also be a good number, although the validity may be questionable if the number of trades is low). If, in that 6‐ to 12‐month time period, the monkeys became a lot better, I know that my assumed edge has either degraded or disappeared completely. It might then be time for me to quit trading that system.

# **Monkey Testing—Example**

 To give you an idea of how the monkey test works, in both the walk‐forward history and the real‐time history, I will provide an example in this section.

 Figure 12.1 shows the walk‐forward performance of the as‐developed system, along with the performance after initial development. The system did quite well for a while, but eventually endured some signifi cant drawdowns. The question is: could the 6‐month monkey test have shown that the edge in this system was gone, and that trading should have ceased? To answer that question, I will perform monkey tests at the points shown on the graph.

![](_page_8_Figure_5.jpeg)

 **FIGURE 12.1** Sample System Walk‐Forward Performance

| TABLE 12.1<br>Baseline Performance      |                     |
|-----------------------------------------|---------------------|
| Parameter                               | Value               |
| Time period                             | 3/19/2007–11/1/2011 |
| Net profit                              | \$72,650            |
| Maximum intraday drawdown               | −\$22,270           |
| Number of trades                        | 430                 |
| Percentage of long trades               | 40 percent          |
| Average bars in trade                   | 2.5                 |
| Number of trading days                  | 1,165               |
| Number of trades/Number of trading days | 0.37                |

 The code, in TradeStation Easy Language, for the baseline strategy, and the three monkey strategies, are shown in Appendix A.

 The fi rst step in creating random strategies that are comparable to the baseline strategy is to gather the pertinent statistics of the baseline strategy. These are shown in Table 12.1 .

 All of the information in Table 12.1 can be obtained from the performance report. The two parameters I will use to compare to random strategies are the net profi t and the maximum intraday drawdown. All other parameters listed will be used to "tune" the random strategy. The goal with tuning is to have roughly the same numbers of trades, the same percentage of long and short trades, and the same average time in trades for the random strategy as for the baseline strategy. Doing this will allow a fair comparison of the two strategies.

 Once the random strategies all yield roughly the same number of trades as the baseline strategy, I can run each random strategy 8,000 times. Then I can compare the results. These results are shown in Table 12.2 .

 The results are pretty clear—the baseline strategy is much, much better than any random strategy. Score one for the humans over the monkeys! Based on this information, the baseline strategy clearly passes the random test.

| Test Period: 3/19/2007 to<br>11/1/2011 | Percentage of Cases with<br>Net Profit Worse than<br>Baseline Case | Percentage of Cases with<br>Maximum Intraday Drawdown<br>Worse than Baseline Case |
|----------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Random entry, baseline exit            | 100%                                                               | 99%                                                                               |
| Baseline entry, random exit            | 99%                                                                | 94%                                                                               |
| Random entry, random exit              | 99%                                                                | 99%                                                                               |

 **TABLE 12.2 Random "Monkey" Test 1** 

#### TABLE 12.3 Random "Monkey" Test 2

| Test Period: 3/1/2011 to<br>3/1/2012 | <b>Percentage of Random</b><br><b>Cases with Net Profit Worse</b><br>than Baseline Case (\$780) | Percentage of Kandom Cases<br>with Maximum Intraday<br>Drawdown Worse than<br><b>Baseline Case (-\$15,680)</b> |
|--------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Random entry, baseline exit          | 49%                                                                                             | 73%                                                                                                            |
| Baseline entry, random exit          | 99%                                                                                             | 100%                                                                                                           |
| Random entry, random exit            | 60%                                                                                             | 95%                                                                                                            |

But how does the baseline strategy compare to the random strategies a few months later? Referring to Figure 12.1, the baseline strategy ran into some difficulty around February–March 2012. Assuming an end date of March 1, 2012, over the previous 12 months, the strategy had a net profit of \$780, and a maximum intraday drawdown of  $-$15,680$ . How does that compare with the random strategies? After  $8,000$  runs, here are the results (see Table 12.3).

The results should present some cause for concern. Clearly, the baseline strategy has performed only slightly better than a random strategy, depending on the number you focus on. Personally, I look at all the numbers as a group, and if I see most of them at or below 60 to 70 percent, I become concerned. If most of the numbers are below 50 percent, I become very concerned, since by all measures, my strategy is not performing better than the monkeys.

In this particular case, with only one value below 50 percent, and two values below 70 percent, I'd probably let the strategy continue trading. More conservative traders might decide to stop trading at this point, and that is a reasonable decision, too.

The next time the baseline strategy caused concern was in May 2013. Over the year ending May 1, 2013, the baseline strategy lost  $-$1,105$ , with a maximum intraday drawdown of  $-$15,100$ . How does that compare to the random monkey systems? See Table 12.4.

#### **TABLE 12.4** Random "Monkey" Test 3

| Test Period: 5/1/2012 to<br>5/1/2012 | Percentage of Random<br><b>Cases with Net Profit Worse</b><br>than Baseline Case (-\$1,105) | Percentage of Random Cases<br>with Maximum Intraday<br>Drawdown Worse than<br><b>Baseline Case (-\$15,100)</b> |
|--------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Random entry, baseline exit          | 50%                                                                                         | 64%                                                                                                            |
| Baseline entry, random exit          | 1%                                                                                          | 1%                                                                                                             |
| Random entry, random exit            | 49%                                                                                         | 72%                                                                                                            |

 The results here are much clearer now. On average, the monkey systems are equal to or better than the baseline strategy. This indicates that any edge the strategy originally had is gone or is certainly on hiatus. Wise traders would stop trading this system near the beginning of May 2013. In this case, judging from the performance of the baseline strategy after May 1, 2013, that was a good decision.

 Comparison of your strategy to randomly generated strategies can be useful, too. In the preceding example system, the analysis was able to show that the strategy as developed was signifi cantly better than a random, monkey‐throwing‐darts system. That is nice to know, as it gives you confi dence as you begin to trade.

 Unfortunately, running this analysis when you develop the strategy tells you nothing about how well the strategy will work going forward. The strategy itself could be defective, leading to real‐time losses. Or the characteristics of the market may have changed, and your strategy cannot adapt to it. In either case, periodically comparing the baseline strategy results to the random monkey results can help you decide whether the strategy is broken. As the earlier analysis shows, the random test can be an early warning detection method of sorts, and can suggest that you stop trading the strategy until performance becomes better than random. Thus, it can be a useful tool in deciding when to stop trading a strategy.
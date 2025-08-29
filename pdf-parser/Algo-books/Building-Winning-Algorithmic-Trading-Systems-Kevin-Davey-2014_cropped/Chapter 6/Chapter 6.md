## Preliminary Analysis

 $\mathbf{N}$  ow that we have examined the primary ways to test a trading strategy and produce a trading performance report, I'll share with you what I think is important in these reports. A typical summary performance report is shown in Figure 6.1. A complete TradeStation-produced performance report spans at least seven pages and includes hundreds of calculated parameters, trade lists, and performance graphs. The amount of information supplied is frankly overwhelming. Most of the results, it turns out, are not all that important when time comes to evaluate the trading system. Maybe a performance metric for "drawdown—coefficient of variation" matters to some people but certainly not to me.

As with most aspects of trading, I try to keep my performance report analysis simple. A few numbers are typically all that I need to conduct a cursory review of any trading system. Once I find something I like, then I will delve deeper.

First, a few ground rules are in order. The performance report should be based either on live data or on a walk-forward test. Optimized back tests should not even be analyzed, as their results are bogus and misleading. Next, there should be multiple years of data, with a multitude of trades. A good rule of thumb is 5 to 10 years of data, and 30 to 100 trades for each trading rule in the system. Third, I usually review performance reports without position sizing applied. As you review many performance reports, it will be important to compare "apples to apples." If you look at one performance report based on single-contract trades and try to compare it to another report that uses multiplecontract-position sizing, a fair comparison is all but impossible. Plus, a bad strategy can be made to look appealing by position sizing. To keep it simple, I look at position sizing only after I feel confident the strategy is viable trading one contract at a time.

Finally, accurate assumptions for commission and slippage must be included in the report. Many times I see performance reports without these values added in, with the flippant response from the creator, "Those costs can be added in

| TradeStation Performance Summary                                                                           |                             |                    | Expand <sup>≫</sup> |
|------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------|---------------------|
|                                                                                                            | All Trades                  | <b>Long Trades</b> | <b>Short Trades</b> |
| Total Net Profit                                                                                           | \$34,932.50                 | \$18,660.00        | \$16,272.50         |
| Gross Profit                                                                                               | \$88,760.00                 | \$44,435.00        | \$44,325.00         |
| Gross Loss                                                                                                 | (\$53,827.50)               | (\$25,775.00)      | (\$28,052.50)       |
| Profit Factor                                                                                              | 1.65                        | 1.72               | 1.58                |
| Total Number of Trades                                                                                     | 411                         | 203                | 208                 |
| Percent Profitable                                                                                         | 49.39%                      | 53.20%             | 45.67%              |
| Winning Trades                                                                                             | 203                         | 108                | 95                  |
| Losing Trades                                                                                              | 208                         | 95                 | 113                 |
| <b>Even Trades</b>                                                                                         | 0                           | 0                  | 0                   |
| Avg. Trade Net Profit                                                                                      | \$84.99                     | \$91.92            | \$78.23             |
| Avg. Winning Trade                                                                                         | \$437.24                    | \$411.44           | \$466.58            |
|                                                                                                            |                             |                    |                     |
| Avg. Losing Trade                                                                                          | (\$258.79)                  | (\$271.32)         | (\$248.25)          |
| Ratio Avg. Win: Avg. Loss                                                                                  | 1.69                        | 1.52               | 1.88                |
| Largest Winning Trade                                                                                      | \$2,407.50                  | \$1,620.00         | \$2,407.50          |
| Largest Losing Trade                                                                                       | (\$442.50)                  | (\$442.50)         | (\$442.50)          |
| Max. Consecutive Winning Trades                                                                            | 8                           | 8                  | 8                   |
| Max. Consecutive Losing Trades                                                                             | 9                           | 5                  | 9                   |
| Avg. Bars in Winning Trades                                                                                | 4.79                        | 5.09               | 4.45                |
| Avg. Bars in Losing Trades                                                                                 | 2.56                        | 2.52               | 2.59                |
| Avg. Bars in Even Trades                                                                                   | 0.00                        | 0.00               | 0.00                |
| Max. Shares/Contracts Held                                                                                 | 1                           | 1                  | 1                   |
| Total Shares/Contracts Held                                                                                | 411                         | 203                | 208                 |
| Account Size Required                                                                                      | \$3,522.50                  | \$2,370.00         | \$2,565.00          |
| Return on Initial Capital                                                                                  | 34.93%                      |                    |                     |
| Annual Rate of Return                                                                                      | 6.29%                       |                    |                     |
|                                                                                                            |                             |                    |                     |
| Return Retracement Ratio                                                                                   | 0.36                        |                    |                     |
| RINA Index                                                                                                 | 5068.08                     |                    |                     |
| Trading Period                                                                                             | 4 Yrs, 9 Mths, 5 Dys, 5 Hrs |                    |                     |
| Percent of Time in the Market                                                                              | 2.64%                       |                    |                     |
| Max. Equity Run-up                                                                                         | \$36,030.00                 |                    |                     |
| Max. Drawdown (Intra-day Peak to Valley)                                                                   |                             |                    |                     |
| Value                                                                                                      | (\$4,160.00)                | (\$2,792.50)       | (\$3,052.50)        |
| Net Profit as % of Drawdown                                                                                | 839.72%                     | 668.22%            | 533.09%             |
| Max. Drawdown (Trade Close to Trade Close)                                                                 |                             |                    |                     |
| Value                                                                                                      | (\$3,522.50)                | (\$2,370.00)       | (\$2,565.00)        |
| Net Profit as % of Drawdown                                                                                | 991.70%                     | 787.34%            | 634.41%             |
| Performance Summary Trade Analysis Trades List Periodical Returns Performance Graphs Trade Graphs Settings |                             |                    |                     |

 **FIGURE 6.1** Sample Performance Report

later, no problem." Not including commissions and slippage, beyond being highly unethical—if not immoral—due to the way these costs impact a trading system, suggests that the developer doesn't really understand proper strategy development. It can easily be shown how testing without commissions and slippage leads one to select trading systems that trade more often, with lower average profi t per trade. For example, if you optimize based on net profi t or something similar, the optimizer will usually give you a best set of parameters that make you trade too much. Here is an example:

## **Without Slippage or Commission**

 Parameter Setting 1: Gross profi t/trade = \$25, 1,000 trades, gross profi t = \$25,000 Parameter Setting 2: Gross profi t/trade = \$50, 300 trades, gross profi t = \$15,000

The optimizer will select Setting 1 as superior.

## **With \$25 Slippage and Commission**

 Parameter Setting 1: Net profi t/trade = \$0, 1,000 trades, gross profi t = \$0 Parameter Setting 2: Net profi t/trade = \$25, 300 trades, net profi t = \$7,500

The optimizer will now select Setting 2 as superior.

 Which approach is better? Well, in the fi rst scenario, such a system in the real world will churn the average trader until his account is depleted. It is defi nitely not as simple as "you can add commissions and slippage in later." The second scenario, however, produces a result that is far more realistic and believable. So, all other things being equal, optimizing with slippage and commissions is an approach much closer to reality and should always be used.

 With these basic ground rules in place, the first number I look at is the total net profit. This seems self‐evident, since if there is no profit, why bother looking at the report any further? It may be that the net profit shown is not worthwhile, either due to the time period involved or the drawdown that has to be endured, but there should be profit nonetheless. In my experience, with a walk‐forward back test, the annual net profit should be \$5,000 per year per contract minimum, preferably \$10,000 or more. Any amount less than this will likely not be worthwhile on a risk‐adjusted basis or will not have enough trades to be significant.

 Profi t factor is the next number I review. Obviously, higher numbers are better here. Many people say that only profi t factors greater than 2.0 are acceptable, but I don't share this view. To me, anything over 1.0 has at least some merit, so I don't discard any systems between 1.0 and 2.0 just based on this number. I do fi nd that profi t factors below 1.5 generally have a hard time making it through the rest of the steps in the development process, though.

 I always review total number of trades to ensure that enough trades are being taken during the test period. If, for example, the report contains only 5 trades, just how valid can the results actually be? I generally use a rough guide of 30 to 100 trades minimum per strategy rule. So, for example, if I have four strategy rules, I'd like to see at least 120 to 400 trades in the report. Obviously, the more trades the better.

 Average trade net profi t is the next performance number I look at. Since this number is after commissions and slippage, it is a great and easy way to compare trading systems. I generally like to see \$50 or more per trade average, based on trading one contract. For average trade values less than \$50, the system might still be viable, but the closer you ride to that \$0 breakeven line, the less leeway you allow for errors, mistakes, slight changes in performance, and the like.

 The next number I review is average losing trade, which I combine with the average trade net profi t to calculate expectancy. There is a lot of confusion about expectancy and how to calculate it, so I will explain it here.

Many traders calculate expectancy in this way:

 Expectancy = average \$ winners \* win % + average \$ losers \* lose % = average trade

where average \$ losers is a negative number

 Note that this is also the average trade net profi t. So calculating an expectancy using this equation does not provide any additional information beyond what is already known with the average trade net profi t.

An alternative expectancy can be calculated as follows:

 Expectancy = (average \$ winners \* win % + average \$ losers \* lose %)/ (−average \$ losers)

 This metric is useful since it is a risk‐adjusted value. It basically states for every dollar you risk, what is your expected return? So with an expectancy of 0.2, you'd expect to receive 20 cents in gains for every \$1 you put at risk. This expectancy has been heavily touted by trading psychologist and educator Dr. Van Tharp, so to avoid future confusion, I will refer to this calculation as "Tharp Expectancy." To me, it is much more valuable than the fi rst method of calculating expectancy.

 For the Tharp Expectancy, I generally look for values greater than 0.1. Anything below this threshold will be diffi cult to trade and likely will demand too much risk for too little reward.

 The next numbers I look at in the performance report are total slippage and total commission. If the numbers are \$0, I immediately discard the report and ignore all other results I may have seen. There is no such thing as cost‐free trading, so any performance report showing that is bogus. In general, I need to see \$5 per round turn trade per contract for commissions. That is a typical value charged by a discount broker, after all exchange fees, National Futures Association fees, and so on are added in. Commissions can be less than this, especially if you do a lot of volume or if you are an exchange member, but the \$5 fi gure is appropriate for most retail traders.

 Total slippage is an even more critical number than total commission. Many developers, especially those who have never traded before, consistently underestimate the amount of slippage experienced in the real world. I defi ne slippage as the diff erence between what the software strategy back‐test engine gives for fi lls and what your actual fills are. For example, many strategy engines assume buy fills at the bid, when in real trading you'll buy at the ask. The diff erence is what I consider slippage. Based on my experience, I assume the following slippage values for heavily traded markets:

- Market orders: 1 to 2 ticks slippage per round turn.
- Stop orders: 1 to 2 ticks slippage per round turn.
- Limit orders: 0 ticks slippage.

 The tricky part is that a typical trading strategy will have some mix of market, limit, and stop orders. In that case, if you can apply only one slippage value to each trade, what should it be? I fi nd being conservative in this situation helps. I will generally apply 1.5 to 2.0 ticks of slippage per round turn trade for these mixed‐ order‐type strategies. I fi nd this generally a bit pessimistic, but it is better than underestimating the slippage costs and being disappointed with real‐world results.

 The fi nal number I look at in the performance report is maximum drawdown. I have no set criteria for a drawdown limit, but if I see a \$10,000 maximum drawdown for a strategy that produces only \$15,000 net profi t, alarm bells go off . In the back of my mind, I look at the drawdown knowing that I can expect to see an even larger drawdown at some point during live trading. If I can't handle the drawdown, I'll discard the system immediately. Otherwise, I know that high risk, low rewards will be tossed out during later steps, so I don't eliminate the strategy just yet.

 There are arguably other important numbers in the performance report, to be certain. Many people, for example, put a lot of faith in winning percentage, or Sharpe ratio, or one of the hundreds of other metrics. The fact is that all metrics are important to an extent, and the developer should try to fi nd ones he or she is comfortable with. Ultimately, any metrics relied upon should prove themselves by leading to successful real‐time strategies.

 Once I am done reviewing the performance report, I generally take a look at some of the trade graphs. I am interested in one chart in particular: the closed trade equity graph. If you are a visual learner, just looking at an equity curve either a closed trade equity curve or a daily equity curve (shown in Figure 6.2 ) might tell you all you need to know. Here are the main things I look for in an equity chart.

 The fi rst thing I look for in an equity curve is the slope. If the chart is not steadily going from lower left to upper right, it may not be a very good strategy. The problem is that the chart can be distorted by the scaling used. So it is also important to look at the end equity, and then divide that by the number of years in the curve. That will give you an annual average profi t and a good indication of whether the strategy is at all worthwhile.

![](_page_5_Figure_0.jpeg)

 **FIGURE 6.2** Sample Equity Curve

 After the slope, I like to look for fl at periods. Flat periods are obviously better than periods of drawdown, but many periods, punctuated by rapid rises, should be cause for concern. Such an equity curve suggests that the strategy may have caught only a few good trades, possibly because of curve fi tting or overoptimization. Flat periods could also be caused by government intervention, for example the United States quantitative easing programs (QE, QE2, QE3) in the 2009–2013 time frame. In this case, it might be okay to assume that performance will improve when government intervention ends. Of course, when, if ever, will some sort of government intervention end, and who can predict it?

 The third major item I look for is drawdown periods. How severe are the drawdowns, and how long does the strategy take to recover from these drawdowns? Answers to these questions will give you an idea of what to expect if you trade this strategy for real. Drawdowns in the future may be more severe, and may last longer—your position sizing and money management should assume that both of these things will happen—but you can at least get a sense of what to expect.

 The absence of any drawdowns on the equity curve should also be cause for concern. I know of no real system, except for money deposited in a savings account, that has only a small or no drawdown. Again, the curve has to "look" realistic. Reward with no risk is not realistic.

 A fi nal item I review on equity charts is the "fuzziness" of the curve. This cannot be seen on a closed equity chart, but it can be seen on a daily equity chart. The fuzzier the curve, the more the daily results jump around, moving up and down short term, even if the longer‐term trend is up. Curves that are very fuzzy are harder to trade, harder to position size, and harder to emotionally deal with. Think about it: if System A gains \$200 on day 1, loses \$200 on day 2, and gains \$75 on day 3, is that preferable to System B, which gains a steady \$25 per day? Both have the same end result, but the fuzziness of System A makes it less appealing than System B.

 Obviously, just looking at an equity curve is by no means a very scientific or very rigorous way to evaluate a trading system. But it can be useful for preliminary analysis. There is no need to look at performance report details if you do not like the look of the equity curve. In those cases, you can save a lot of time by spending a few seconds staring at the equity curve and then rejecting a system you do not like.

 The discussion thus far has focused on simple, quick numbers and methods to evaluate the performance of a trading system. Such analysis is useful in the early stages of development, where most strategies are junk, and a fast, cursory review can eliminate them, freeing up more time for you as the developer to create new systems. But, eventually, you will need to do in‐depth analysis of performance results. That is a whole diff erent animal.
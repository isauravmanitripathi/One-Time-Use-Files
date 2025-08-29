# CHAPTER 10 - LET'S GET STARTED – A SIMPLE SAMPLE ALGO

In this chapter, I am going to walk through a simple algo trading example. Note that my focus here is on using the trading software – regardless of the platform you use, you really must be able to do these basic tasks.

This example is NOT an example of the proper, or only, steps to develop a solid algorithm. That is beyond the scope of this short book. But this example will at least get you started with the concepts laid out in this book.

Treat this chapter as an interactive guide. For each step I take, try to duplicate it with your trading software. Go to the next step only when you have mastered the first step.

**NOTE:** This strategy, as presented, is NOT a tradable strategy – it has weak out-of-sample performance. It is merely an illustrative example. The steps shown do not represent the strategy development process I use for my own trading (my trademarked Strategy Factory® process). The key here is if you feel comfortable performing each of the steps I have detailed in this chapter, you have graduated from beginner algo level, and you can now be a serious algo strategy developer.

# Call Up A Chart

Let's start out with a simple task. Open a daily continuous chart of Soybeans from 2007 to today. Have the start date of January 1, 2007 and end date of December 31, 2016.

![](_page_1_Figure_2.jpeg)

*Figure 25- Can You Create A Chart Like This In Your Platform?*

# Get A Trading Idea

A simple trading idea is usually the best. In this case, I'll create a basic breakout system. The idea is that higher prices can only occur by exceeding previous high prices – pretty simple!

At the close of every bar, if the highest price is the highest closing price of the last "xbars," and the 15 bar ADX (a technical indicator measure of trendiness) is above 20, then go long. Do the opposite for short trades. I'll also include a simple stop loss, with no profit target (let winning trades run!). This type a system is good for trends, but will likely experience a lot of whipsaw during non-trending markets.

# Program It

Program this simple strategy in your own platform. Code for Tradestation Easy Language is below. Include \$5 round turn trade for commissions, and \$25 round turn for slippage (VERY important!).

![](_page_3_Picture_2.jpeg)

*Figure 26- Code This Strategy In Your Platform*

# Apply It To The Chart

Now, use your software to attach/apply that strategy to the previously built chart.

![](_page_4_Figure_2.jpeg)

*Figure 27- Can You See Trades On Your Chart?*

# Optimize A Bit

Optimization is a dirty word, but when used in moderation it can be useful. Try to optimize the variable "xbar." Use a minimum value of 5 (short term) up to 30 (medium term) in steps of 5. Also, optimize the stop loss, from 500 to 1500 in steps of 500 dollars.

|    |                     |                                             |                             | TradeStation Strategy Optimization Report - @S Daily [CBOT] Soybeans Continuous Contract [Jul18] |                      |                     |                                    |        |                             |                             |                         |                  |
|----|---------------------|---------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------|----------------------|---------------------|------------------------------------|--------|-----------------------------|-----------------------------|-------------------------|------------------|
|    |                     |                                             | 🖫 🧁 🔓 🔛 💹 🐱 🖬 🏜 🔹 🐼 Alidata |                                                                                                  |                      |                     | Robustness Idx Avg: N/A            |        | WFO Suitability: N/A        |                             | 8                       |                  |
|    | AlgoBook<br>02 xbar | CJD2018-04 CJD2018-04<br>AlgoBook<br>02: sl | Test                        | All: Net Profit                                                                                  | All: Total<br>Trades | All %<br>Profitable | All: Winning All: Losing<br>Trades | Trades | All Avg<br>Winning<br>Trade | All: Avg<br>Losing<br>Trade | AL<br>Win/Loss<br>Ratio | All Avg<br>Trade |
|    | 20                  | 1,000                                       | 10                          | 85,571.250                                                                                       | 82                   | 19.51               | 16                                 | 66     | 9,038.75                    | $-894.68$                   | 10.10                   | 1,043.55         |
|    | 25                  | 500                                         |                             | 77.122.500                                                                                       | 93                   | 16.13               | 15                                 | 78     | 7.868.33                    | $-524.39$                   | 15.00                   | 829.27           |
|    | 20                  | 500                                         |                             | 77.070.000                                                                                       | 116                  | 14.66               | 17                                 | 99     | 7,476.62                    | -505.38                     | 14.79                   | 664.40           |
|    | 20                  | 1,500                                       | 16                          | 74,728.750                                                                                       | 73                   | 21.92               | 16                                 | 57     | 8.983.28                    | $-1.210.59$                 | 7.42                    | 1.023.68         |
|    | 25                  | 1.000                                       | 11                          | 73,432.500                                                                                       | 71                   | 19.72               | 14                                 | 57     | 9.009.29                    | -924.52                     | 9.74                    | 1.034.26         |
| 6  | 15                  | 1,500                                       | 15                          | 70.205.000                                                                                       | 94                   | 23.40               | 22                                 | 72     | 7.184.77                    | $-1.220.28$                 | 5.89                    | 746.86           |
|    | 15                  | 1,000                                       |                             | 61,103.750                                                                                       | 113                  | 18.58               | 21                                 | 92     | 6.800.95                    | -888 22                     | 7.66                    | 540.74           |
| 8  | 25                  | 1.500                                       | 17                          | 58,875.000                                                                                       | 65                   | 21.54               | 14                                 | 51     | 8.994.11                    | $-1.314.56$                 | 6.84                    | 905.77           |
| 9  | 30                  | 500                                         |                             | 57,600,000                                                                                       | 85                   | 12.94               | 11                                 | 74     | 8,783.64                    | $-527.30$                   | 16.66                   | 677.65           |
| 10 | 10                  | 1,000                                       |                             | 56.375.000                                                                                       | 150                  | 26.00               | 39                                 | 111    | 4,197.88                    | -967.05                     | 4.34                    | 375.83           |
| 11 | 30                  | 1,000                                       | 12                          | 55.738.750                                                                                       | 61                   | 18.03               | 11                                 | 50     | 9.305.23                    | -932.38                     | 9.98                    | 913.75           |
| 12 | 30                  | 1.500                                       | 18                          | 50.982.500                                                                                       | 56                   | 19.64               | 11                                 | 45     | 10.056.36                   | $-1.325.28$                 | 7.59                    | 910.40           |
| 13 | 10                  | 1.500                                       | 14                          | 47, 802.500                                                                                      | 132                  | 31.06               | 41                                 | 91     | 4.115.12                    | $-1.328.76$                 | 3.10                    | 362.14           |
| 14 | 15                  | 500                                         |                             | 41,485.000                                                                                       | 163                  | 12.88               | 21                                 | 142    | 5.381.90                    | -503.77                     | 10.68                   | 254.51           |
| 15 | 5                   | 1,000                                       |                             | 38.253.750                                                                                       | 313                  | 25.56               | 80                                 | 233    | 3.002.66                    | $-866.78$                   | 3.46                    | 122.22           |
| 16 |                     | 1.500                                       | 13                          | 19.277.500                                                                                       | 287                  | 29.27               | 84                                 | 203    | 2 935.33                    | $-1.119.66$                 | 2.62                    | 67.17            |
| 17 |                     | 500                                         |                             | 19,148.750                                                                                       | 404                  | 16.34               | 66                                 | 338    | 2,861.67                    | -502.13                     | 5.70                    | 47.40            |
| 18 | 10                  | 500                                         |                             | 11,888.750                                                                                       | 226                  | 15.93               | 36                                 | 190    | 3,218.96                    | -547.34                     | 5.88                    | 52.61            |

*Figure 28- Optimization Results*

### Look At Results

Take a look at the optimization results. There are 18 iterations (runs), and all of them are profitable. This is generally a good sign. The dilemma becomes, which parameter set to choose? Highest Net Profit? Average Return on Account? Minimum Winning Percentage? Just ask that question in a trading forum, and be prepared for a slew of answers, with pointed and sharp opinions. The truth is there is no "perfect" criteria to use – it is a matter of personal preference and experience.

The choices for what to pick are pretty much endless, which is one reason I follow a set criteria when I do my development, which includes walkfoward testing.

For now, let's assume that we will pick a "median" Net Profit – not the best, not the worst. That is iteration #9, with value of xbar=30, stop=500.

#### Run Out-Of-Sample

Once we have our parameters chosen, it is time to run the strategy in 2017 and 2018. To do that, we simply change the chart end date, then review the updated Performance Report (not shown). The results, while not horrible (if 2017-8 results were really poor it would suggest we overoptimized or curve fit too much), are not really good enough for trading. At this point, the strategy should probably just be abandoned, since if we test again and again, our out-of-sample results are no longer truly out-of-sample.

![](_page_7_Figure_2.jpeg)

*Figure 29- Sample Strategy, Out-Of-Sample Results*

# Automate it

For this strategy, based on the out-of-sample performance, I would not trade it. But assume you wanted to trade it. What steps would you take to turn it on and automate it? Here is the step by step process for Tradestation:

| Name                                                                                                                            |        | Input Values                  | Status | Buy | Sell | Sell Short | Buy to<br>Cover | Format.             |
|---------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------|--------|-----|------|------------|-----------------|---------------------|
| KJD2014-09 Rug01 AH                                                                                                             | 1.true |                               | On     | On  | On   | On         | On 💌<br>٠       | Properties for All. |
|                                                                                                                                 |        |                               |        | 2   |      |            |                 | Status              |
|                                                                                                                                 |        |                               |        |     |      |            |                 | Move Up             |
|                                                                                                                                 |        |                               |        |     |      |            |                 | Move Down           |
|                                                                                                                                 |        |                               |        |     |      |            |                 | Edit EasyLanguage   |
|                                                                                                                                 |        |                               |        |     |      |            |                 | Remove              |
|                                                                                                                                 |        |                               |        |     |      |            |                 |                     |
|                                                                                                                                 |        | ш.                            |        |     |      |            |                 |                     |
| +<br>Automation:<br>Generate strategy orders for display in TradeManager's Strategy Orders tab<br>Automate execution using<br>4 |        | account with confirmation Off |        |     |      |            |                 |                     |

*Figure 30- Steps To Automate A Strategy, Tradestation*
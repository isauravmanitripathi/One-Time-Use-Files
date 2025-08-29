# Detailed Analysis

s the development of a trading strategy progresses, the analysis also progresses,  $\boldsymbol{\varLambda}$  and the performance hurdles a strategy must meet to be considered viable get more stringent. My primary method of analysis at the later stages is Monte Carlo analysis. But before I explain how I run the analysis and what I look for in results, I'll first briefly describe the process.

#### **What Is Monte Carlo Analysis?**

Monte Carlo analysis, or simulation, sounds like a daunting topic, but actually it is not. With the Monte Carlo spreadsheet I created, which you can download for free (www.wiley.com/go/algotradingsystems), the analysis is pretty simple. But what is it actually?

Think about the individual trades in your strategy. These trades taken sequentially, in the order they occurred, yield the strategy equity curve. But what if the order of those was different? Could the drawdown become more severe? Could the end equity be different? These are the questions Monte Carlo analysis can answer.

In its simplest form, you can think of it this way: First, get a number of little pieces of paper, one for each trade in your strategy. Then, write down one trade result on each piece of paper. Once you have all trades accounted for, put all the pieces in a hat. Randomly choose one. That is your first trade. Record it, adding it to your initial equity, and then put the piece of paper back in the hat (this is referred to as random sampling with replacement). Then, pick another piece of paper, record its value, and add it to the existing equity curve you are building.

If you do this for a number of trades, you'll have a possible equity curve. If you perform the whole analysis many, many times, you'll have a family of equity curves. Each one represents a possible way that trades in your strategy could have occurred. Using the family of possible curves, you can get statistics about your trading system. These statistics can help you evaluate a strategy, determine a position sizing approach, and give you realistic scenarios for what you might face if you actually trade the strategy live. Of course, this all assumes that the historically derived trades will be the same as the trades in the future. If your historical trades are based on fl awed development, future results will be garbage.

 Obviously, there are some potentially serious drawbacks to this analysis. First, the analysis assumes that the trades in your performance report are the only possible trades that can happen. This is obviously false, since when you start trading live, any result is possible for a particular trade. But, if the distribution (overall mean and standard deviation) of the trades is accurate, then the Monte Carlo approach can yield meaningful results.

 A second drawback is that this analysis assumes that each trade is independent of the previous trade, a condition commonly referred to as serial or auto correlation. For most trading strategies, this is not an issue. However, if you have a strategy in which the trade results depend on each other, simple Monte Carlo analysis is not appropriate. An example of such a situation would be if the trade B signal is dependent on the outcome of the previous trade A. You ideally should check for it before using the Monte Carlo analysis. One method for checking for serial correlation is the Durbin Watson statistic. Although it is beyond the scope of this book, you can fi nd details, examples, and spreadsheets on this calculation on the Internet.

 If you fi nd that your trades do exhibit serial correlation, the simple Monte Carlo analysis may not be appropriate to use. In such cases, you could try to use a Monte Carlo simulation that included serial correlation eff ects, or you could gather statistics from a method called "start trade analysis" or "moving start analysis." In this analysis, you simulate the start of trading at each trade, and gather the statistics for return and drawdown. For example, if you have 10 trades, *i*, *i + 1, … i + 9* in your sample, you'd fi rst create an equity curve starting with trade *i* . From the resulting curve, you could get the drawdown *d i* . Then, start the equity curve at trade *i + 1* . This curve would give you the drawdown *d i*+1 . If you continue through all the trades, you can analyze the set of drawdowns *d.* This method may be a bit more cumbersome than Monte Carlo, but it is a better way to analyze the data when you have serial correction, since trade sequence will be mostly preserved.

 Assuming you can live with the drawbacks listed, Monte Carlo can help you answer the following questions:

- What is my risk of ruin for a given account size?
- What are the chances of my system's having a maximum drawdown of X percent?
- What kind of annual return can I expect from this trading system?
- Is the risk I am taking to trade this strategy appropriate for the return I am receiving?

 Each of these questions will be addressed in the discussion that follows. To simplify the narrative, I will assume the reader is using my Monte Carlo spreadsheet. Any Monte Carlo simulator available to the public should be able to give the same results, although some of the terminology and assumptions used may be diff erent. Therefore, whether you use the simulator or not, the discussion will still be useful for you.

## ■ **Inputs to Monte Carlo Simulator**

 There are only a few required inputs to perform Monte Carlo simulation. These are listed below, and are shown in Figure 7.1 .

*Base Starting Equity.* This is the starting amount of your account, in dollars.

*Stop Trading if Equity Drops Below \$.* This is the amount of capital below which you will cease trading. For example, if you enter \$3,500 here, once your equity, on a closed‐trade basis, drops below \$3,500, you will not be permitted to trade anymore. Your account will be considered "ruined." At a minimum, this value must be greater than the initial margin for one contract of the instrument your system is trading. In the preceding example, you could trade only products that had an initial margin below \$3,500. If you wanted to trade a higher‐margin instrument, such as gold (currently at \$8,800 initial margin), you would have to increase this minimum amount. As a rule, I never recommend trading with

![](_page_2_Figure_5.jpeg)

 **FIGURE 7.1** Monte Carlo Simulator Inputs

only enough capital to just meet the margin requirement, but for this simulation, the assumption is acceptable.

- *# Trades, 1 Year.* This is simply the number of trades that your system takes in a one‐year period. My simulator is designed to trade for only one year, so each equity curve generated will consist of this number of trades. That is, of course, assuming the ruin point is not hit fi rst.
- *Individual Trade Results.* This column of data contains all the trade data, one trade per row. All trades should be based on the same reference point, that is, per contract, per day, and so on. You cannot mix some trades that were based on one contract with trades that had multiple contracts.

## ■ **Limitations of the Simulator**

 To keep things simple, the simulator makes a few assumptions. First, it is assumed that one contract is traded for each trade. There is no position sizing built into the simulator. Second, the simulator assumes one year of trading. Both of these assumptions can be changed in the Excel macro code by anyone who understands macro programming language.

 In the discussion that follows, a "run" or iteration is defi ned as the generation of one single equity curve. In a "simulation," there will be a number of runs—in the simulator discussed, this is 2,500 runs. To generate statistics, such as risk of ruin or median return, the results of a simulation (2,500 individual runs) are used.

## ■ **Simulator Output**

 Once the simulator runs, a table of output values and corresponding curves will be generated, as depicted in Figure 7.2 . Following is an explanation of each output value, how to interpret it, and what values I consider appropriate for a tradable system.

#### **Starting Equity**

 This is the size of your account at the start of the Monte Carlo analysis. All rates of return are calculated based on this number, and risk of ruin and maximum drawdown are both heavily infl uenced by it. The simulator uses a range of diff erent starting equities in order to generate the table and the output curves.

#### **Risk of Ruin**

 This statistic tells you the chances (probability) that within a year's time, your account will be wiped out (i.e., fall below the "Stop Trading if Equity Drops

![](_page_4_Figure_0.jpeg)

FIGURE 7.2 Monte Carlo Simulator Outputs

Below \$"). For example, if the risk of ruin is 12 percent, that means within the first year of trading the system, you have a 12 percent chance of having to cease trading.

Risk of ruin is an extremely important statistic, especially for traders with small accounts. The risk of ruin can be significant for small accounts, even if the system is a winning system! Here is an example that should make that clear:

Let's say you have a very good day trading system. It trades two times a day. Winning trades are \$200 after all costs, 50 percent of the time. When it loses the other 50 percent of the time, it loses \$175 net.

Per day, on average, you'd make \$25 a day. In a year, you'd make \$6,300 per contract. If you traded this with a \$10,000 account, always with one contract, you'd make a 63 percent annual return, with somewhere around 15 percent maximum drawdown. By most measures that is really good.

Now, let's say you take this positive expectancy system and trade it with a small account, \$5,000 and under. Let's say your broker allows \$500 day trading margin, so that is your "ruin" point—if your account drops below \$500, you are ruined and you quit trading.

In one year of trading, how likely are you to be ruined (drop below \$500 and cease trading)? The results, depicted in Figure 7.3, might surprise you.

The question is: where do you feel most comfortable being on this curve? The person with \$1,500 is probably panicking after each loss, since he doesn't have much wiggle room. But the trader with \$5,000—still a small account, only 3.3 times the first trader's account—is 20 times less likely to be ruined.

![](_page_5_Figure_0.jpeg)

 **FIGURE 7.3** Account Size and Risk of Ruin

 The conclusion is that being underfunded can be disastrous, *even with a winning system.* So I pay a lot of attention to the risk‐of‐ruin number that the simulator outputs. Any value above 10 percent means, for me, that I am trying to trade the system with too little capital, and that I should increase the amount of capital to get below 10 percent. Obviously, systems with 0 to 1 percent probability of ruin are the best, but as with anything in trading, it is a trade‐off with rate of return. In my experience, I have found that simulation results with less than 10 percent risk of ruin are fairly safe, while still providing an acceptable rate of return.

#### **Median Drawdown**

 This statistic can be a bit confusing at fi rst. It is actually the median value of the maximum drawdown. Are you confused yet? Perhaps breaking it into pieces will help.

 First, the maximum drawdown is the maximum percentage drop in account size from an equity peak. It should always be measured from the previous equity peak. Figure 7.4 gives an example of three diff erent drawdowns:

- Drawdown 1: \$5,000 drawdown, after peak equity of \$20,000 = \$5,000/ \$20,000 = 25 percent drawdown
- Drawdown 2: \$10,000 drawdown, after peak equity of \$30,000 = \$10,000/ \$30,000 = 33 percent drawdown
- Drawdown 3: \$15,000 drawdown, after peak equity of \$60,000 = \$15,000/ \$60,000 = 25 percent drawdown

![](_page_6_Figure_0.jpeg)

 **FIGURE 7.4** Maximum Drawdown Explained

 In this example, the maximum percentage drawdown occurs during drawdown 2 and is 33 percent. It is interesting to note that it is the maximum percentage drawdown, not the absolute dollar maximum drawdown (drawdown 3, in dollar amounts, is higher than drawdown 2).

 For every simulation run, there will be a corresponding maximum percentage drawdown. Over a great number of simulation runs, there will be a distribution of maximum drawdowns, varying from 0 percent (no drawdown at all, a hopelessly pie‐in‐the‐sky case), to 100 percent (a complete ruin from the peak equity point, down to \$0 equity). This distribution will have a median value, which means that 50 percent of the drawdown values exceed the median, and 50 percent are below it. Therefore, in the term "median maximum drawdown," the word *maximum* refers to the largest drawdown in a particular simulation run, and *median* refers to the midpoint of maximum drawdowns over a large number of simulation runs.

 There is no magic in selecting the median maximum drawdown to be the output value for the simulation. It could easily be the 30 percent, 60 percent, 90 percent, and so on, percentile value, too. I chose the median value just to use for comparison purposes to other systems. If I instead wanted a worst‐case value, I could have used the 95th percentile value of drawdown, meaning only 5 percent of maximum drawdowns are worse than this value.

 Based on my own personal preference, I generally accept up to a 40 percent median maximum drawdown. That is, within 1 year I have a 50 percent chance of reaching a 40 percent maximum drawdown. This may be too extreme for most people, but it suits my objectives and my personality.

 One thing to keep in mind with maximum drawdown is that traders, especially new traders, have a tendency to greatly overestimate their ability to withstand a drawdown. Based on my conversations with various traders, I have found that traders can generally handle half the maximum drawdown they think they can handle. For instance, if a trader decides before trading a system that he can handle a 30 percent maximum drawdown, when real money is on the line, he will start to panic, and likely quit or change the system, at the 15 percent drawdown point. I have coined a phrase for this phenomenon: "half of what you think it is." Just remember to keep this in mind when you establish your personal maximum allowable drawdown.

#### **Median \$ Profi t, Median Return**

 As with the drawdown, over a full simulation of 2,500 runs, there will be a distribution of results. This distribution is used to calculate the median profi t and median return. Median \$ profi t is simply the fi nal equity minus the initial equity, after one year's worth of trades. Over the course of 2,500 runs, a median level can be calculated. This is the median \$ profi t. The median return is calculated in a similar fashion, although it is the fi nal equity divided by the initial equity, in order to get it into percentage terms.

 For my personal trading, I have no set goal for median \$ profi t. I do like to see median returns above 50 percent, especially since I stated earlier that I would allow up to 40 percent median drawdown values. It would not be wise of me to set the return threshold at 20 percent with a 40 percent drawdown. To keep me aware of this relationship between risk and reward, I also calculate the return/ drawdown ratio.

#### **Return/Drawdown**

 Of all the statistics produced by the Monte Carlo analysis, I feel this number is the most important. It is referred to in fi nancial literature as the Calmar ratio when it is calculated over a three‐year period. Since I am only simulating one year of performance, the simulator result is not exactly a Calmar ratio. The spreadsheet‐produced number is simply the median annual percentage return divided by the median maximum percentage drawdown.

 One way to think about this ratio is "it takes Y risk to make X." In this case, Y is the drawdown, and X is the profit return. Obviously, high values of this ratio are better. I generally look for return/drawdown ratios above 2.0, although I will accept lower values in special circumstances. In my experience, I find that ratios above 2.0 will usually produce acceptable results in the real world of trading live.

#### **Prob > 0**

 This gives you the probability, expressed as a percentage, that the system will make money in the fi rst year of trading. For example, if Prob > 0 equals 89 percent, that means you will have an 89 percent chance of showing profi t in the fi rst year. Of course, this is all based on your historical test results, so if they are not accurate, this result will not be either.

## ■ **Summary**

 Now that we have discussed the performance report, equity curve, and Monte Carlo simulator, we can summarize the uses of all the values and threshold values for acceptability (Table 7.1 ).

| Parameter                                       | Source                 | Utilized During | Threshold                                                                        |
|-------------------------------------------------|------------------------|-----------------|----------------------------------------------------------------------------------|
| Total net profit                                | Performance report     | Initial review  | ∼\$10K per year per contract                                                     |
| Profit factor                                   | Performance report     | Initial review  | >1.0 OK, >1.5 ideal                                                              |
| Average trade net profit                        | Performance report     | Initial review  | >\$50 per contract                                                               |
| Tharp Expectancy                                | Performance report     | Initial review  | >0.10                                                                            |
| Slippage and<br>commission                      | Performance report     | Initial review  | Discard if \$0, otherwise<br>\$5 commission 1–2 ticks<br>slippage per round turn |
| Maximum drawdown                                | Performance report     | Initial review  | Should<br>be much smaller than<br>total net profit                               |
| Equity curve slope                              | Equity curve           | Initial review  | Ideally rises at 45‐degree angle                                                 |
| Equity curve flat periods                       | Equity curve           | Initial review  | Short in duration                                                                |
| Equity curve drawdown,<br>depth and<br>duration | Equity curve           | Initial review  | Proportional to overall<br>curve                                                 |
| Equity curve fuzziness                          | Equity curve           | Initial review  | Small is ideal                                                                   |
| Risk<br>of ruin                                 | Monte Carlo simulation | Detailed review | <10%                                                                             |
| Median maximum<br>drawdown                      | Monte Carlo simulation | Detailed review | <40%                                                                             |
| Median % return                                 | Monte Carlo simulation | Detailed review | >40%                                                                             |
| Return/drawdown ratio                           | Monte Carlo simulation | Detailed review | >2.0                                                                             |

 **TABLE 7.1 Important Performance Parameters**
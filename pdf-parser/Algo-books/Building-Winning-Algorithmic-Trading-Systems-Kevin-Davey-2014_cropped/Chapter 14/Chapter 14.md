## Monte Carlo Analysis and Incubation

nce you have the walk-forward strategy set up, and you are satisfied with the results, it is time to evaluate the strategy in a Monte Carlo simulation. This is an important step because random simulations may show dramatically different profits and drawdown. It may be that the way the historical trades lined up, the maximum drawdown was very small. But since history isn't likely to repeat itself, it is important to see what type of maximum drawdown you could possibly incur trading this strategy.

As stated earlier in Chapter 7, I use an Excel spreadsheet to do the Monte Carlo analysis. You can download this tool for yourself at the book resource web site (www .wiley.com/go/algotradingsystems). There are also numerous free and paid Monte Carlo simulators available on the Internet, should you choose to go that route. One good free simulator is Equity Monaco by NeoTick (equitymonaco.software.informer .com/). A good pay tool is @Risk (www.palisade.com/). All of these choices will give you the same basic results, and you might prefer the presentation of results and capabilities of one over the other. The key is to get simulation results that you can base your decision on.

If you use the simulator spreadsheet I created, you simply copy trade results from your strategy performance report, paste them in the spreadsheet, enter your initial capital, quitting-point capital, and number of trades in a year, and then press calculate. The spreadsheet will calculate the simulated equity curves for 2,500 iterations, and

129

present you with summary results. These results will be based on one year of trading. Sample output of the spreadsheet was shown earlier in Figure 7.2. I typically focus on the return to max drawdown ratio (ret/DD), and I like to see values above 2.0 for an acceptable strategy. Anything below 2.0 suggests that the strategy is taking on too much risk for the reward attained and might not be worth trading.

 If you are profi cient in writing macros in Excel, you can easily take the Monte Carlo spreadsheet I have created and modify it to suit your own needs. You could add position sizing, for example, or you could change which results are presented. In the end, the point of the simulation is to give you results that you can understand and interpret. I have told you what works for me; maybe that will work for you, but maybe you'll think of something better.

## ■ **Incubation**

 One of the most crucial steps in strategy development, in my opinion, is also the toughest psychologically to implement. Before I discuss this last step, let's review where we have been in the strategy development process:

- 1. We have established goals and objectives for our completed strategy and also goals for the steps along the way. In this manner, we can quickly eliminate strategies before spending too much time on them.
- 2. We have developed a trading idea for our strategy that we feel has an edge. We have also defi ned the market, time frame, and other important factors for our testing.
- 3. We have performed limited testing with the strategy, and we are happy with the results. We believe we might have an edge.
- 4. We have conducted in‐depth testing, using walk‐forward testing if possible. Again, we are happy with the performance results obtained.
- 5. We have performed Monte Carlo testing, to help us establish probabilities for the strategy performance and also to give us realistic future scenarios of performance.

 These completed fi ve steps represent a lot of work and likely caused us to discard tens or hundreds of strategies before fi nding success. To get through the last step, Monte Carlo testing, is certainly an accomplishment. When this happens, you likely will be so excited you will want to trade immediately! That, of course, would be the wrong thing to do. Incubation is the right thing to do.

 What exactly is incubation? Simply put, it is watching and waiting. With incubation, you wait three to six months before you start live trading. During this time, you occasionally monitor the performance of the strategy, as if it is another out‐of‐ sample test period. I like to check on my incubated strategies once per month.

Why is it important to incubate a strategy? Here are a few reasons:

- When you fi nish Monte Carlo testing, you are at an emotional high. Your "baby" has survived and has a lot of promise. You have a lot of emotional capital invested in this strategy, as well as your time and eff ort. You want it to succeed. You may even *need* it to succeed. Of course, this leads to a fragile emotional state. If you immediately start trading it with real money, you might not think clearly if things start out bad for the strategy, as so often seems to happen. This could lead you to quit the strategy early, or worse yet, haphazardly increase size when performance starts out bad ("doubling down").
- By waiting for a while before live trading, you will forget about the blood, sweat, and tears you expended to create the strategy, and you will look at it more objectively. If it passes incubation, great—but if it doesn't, you won't be distraught. Remember, short‐term hardship is sometimes the price for long‐term success, and that defi nitely holds true with trading systems.
- As I have shown, the system development process is diffi cult and complicated. There are probably a thousand diff erent mistakes you can make along the way. Some can be blatant, like overoptimizing, while others may be subtle, such as using hindsight bias to develop your strategy rules. The point is that, because of development mistakes, there can be no way to know for sure if you have done something wrong until you test your strategy on live, unseen data. Major mistakes will show up in live results almost immediately, and by keeping your cash on the sidelines during this period, you will save a great deal of money.
- Incubating gives you a chance to see how a strategy performs in real time. You may fi nd out that you do not like the strategy, even if it makes money. For example, maybe your strategy sells every pivot high. In historical back testing, that may not bother you. But in real time, watching your strategy fi ght every market high might not be your cup of tea. It is far better to realize that now, rather than after you commit money to trading it.

 I generally perform incubation without real money. This is because, over time, I have concluded that the way I place orders, the bar types I use, and so on all can be fairly well replicated by the strategy back‐test engine. There are times, however, where you may want to commit real money on a small scale. For example, if your strategy relies on limit orders for entries, you may want to test with real money to ensure that your fills match strategy engine fills. With some software packages, this might not be the case. Also, if you use exotic bar types, back‐test results and real‐ money results can be totally diff erent. You might need a live real‐money test to check this, but once you confi rm an issue, you will be able to avoid those bar types in later strategies. Sometimes the only way to see if a back test is accurate is by testing the strategy with real money.

 As I mentioned, I normally do not need to perform real‐money testing during incubation. One reason is that I avoid back tests that show or contain the following:

- Any buy fills at the low of a bar or sell fills at the high of a bar. Rare will be the day this occurs in real life, but many unscrupulous system vendors and naive developers develop strategies that frequently show this phenomenon.
- Limit orders that fill when price is touched. On occasion, maybe 0 to 30 percent of the time, you will get fi lled at your limit price, when it is just touched. Most of the time, though, the price has to penetrate your price to guarantee a fill.
- Any exotic bars, such as Renko, Kase, and even point‐and‐fi gure. Due to the way the bars are built from history, your strategy fills many times cannot be believed. Better to just avoid these bars, except for real‐time discretionary trading.
- Strategies that exit on same bar as entry or that have stops and targets so tight that a profi t and loss exit could occur on the same bar. My experience is that it is easy to trick a strategy engine, even with tick data, when exits or entry and exits occur on the same bar. This is due to the assumptions the strategy engine must make regarding price travel. Usually, the results will be overly optimistic when compared to real live trading.

## ■ **Evaluating Incubation**

 My goals with incubation are to give me reasonable assurance that I made no major mistakes during development, to remove my emotions from the process, and also to see if real‐time performance is appealing enough to trade. Later in this book, I'll share some techniques I use to see if these goals are indeed met.
# Let's Talk about Data

 $\mathbf{W}$  ith the entry, exit, market, and time frame/bar length decided, now comes one of the most important, most underappreciated, yet least understood aspects of testing: market data. People take data for granted, and that can be a big mistake. I've seen huge differences in strategy performance just due to different data sources. I'll make the grand assumption that your data are clean, without bad data points, missing data, and so on. Of course, that is not the case at all, practically regardless of vendor. But most people understand that data may have errors; what most do not understand is the impact behind the answers to these data-related questions:

- How much data should you use?
- Should you use pit data or electronic data?
- Should you use continuous contract data?
- Did the advent of electronic trading impact market data?
- How do you test with foreign exchange (forex) data?

Now, before you start testing, is the time to look at all these issues, and make some decisions. To go back and retest with different a data structure typically means you will be using tainted data, and that is not good.

#### How Much?

If you are like me, you've probably done the "eyeball" test more than a few times. You look at a chart and, knowing your entry and exit criteria, perform a quick test of the past few days or weeks of data. After a few trades, if you see a lot of profit, you get excited and venture into more in-depth testing. If you have losses, you either abandon the strategy or tweak it a bit and try again.

 Hopefully, you realize the futility of such a simple test. Not enough trades, not enough market conditions, just not enough of anything to make an informed decision period. To attain long‐term success, you must look at more data than this.

 So what is an acceptable amount of data? When I am asked this question, I almost always reply, "As much as possible." More data provides more market conditions more bull markets, more bear markets, more fl at markets. It also provides more quiet periods and more volatile periods. As you make more trades, and your system remains profi table, it becomes less and less likely that the results were due to just chance. Think of a coin fl ip. If you fl ip it once, chances are 50/50 that it will be heads. If you fl ip a coin 10 times, the chances of heads' coming up at least once is quite good. Flip the coin 100 times, and you are practically guaranteed that heads will appear at least once. More fl ips leads to more certainty, just as more trades leads to more confidence.

 For daily bar systems, which tend to be swing systems (trades lasting days to weeks), I fi nd that 10 years of data is a good compromise. It allows your strategy to see many diff erent market conditions and works well with walk‐forward testing (which requires some initialization time).

 For intraday or short‐term systems, I also like using 10 years of data. Practical considerations, though, such as the introduction of electronic data, may make this a diffi cult task. So, in many cases I will use only 5 years of data, realizing that my results may not be as robust as a 10‐year tested system.

 For some people, 5 to 10 years of data is too long a time period to test, or the data are not available. In such cases, I recommend the following rules of thumb: for each rule and parameter you have in your strategy, have at least 30 to 100 trades. As an example, consider a strategy with two entry conditions, and two exit conditions. For such a system, I'd like to see 120 to 400 trades. Anything less than this might be acceptable but also runs the risk of the strategy's being "matched" or fi tted to the data.

 The drawback to using as much data as possible is that it makes development much tougher. Let's face it—at best, most trading systems out there are probably breakeven before commissions and slippage. This means the longer you test it, the more likely it is that gross profi ts will revert back to zero. I'm sure you witnessed this before, when a strategy has fantastic performance in a one‐, three‐, or six‐month period, only to give it all back in the next period. So, in the end, ask yourself if you want a long‐running positive system, or do you want a great performer over a short period of time? The former is much tougher to fi nd, and the latter is much more likely to lead to real‐time losses.

### ■ **Pit or Electronic Data?**

 Back in the old days of pit trading, knowing what data to use was easy—just use the pit data because that was all there was! Today, with electronic data taking over, there are multiple options:

- Pit data only
- Electronic data only
- Pit and electronic data together
- Data during traditional pit times only
- Data during all hours
- Data during day session/evening session

 The choice for data going forward might be easy—electronic data are the best because that is where the volume currently is, but what do you do when you are historically testing a strategy?

 I'll give you a simple example to highlight the dilemma. Let's say you are trading gold, and you want to use 20 years (excellent choice!) of data, with 60‐minute bars. Twenty years ago, the pit was the only data source, so you have to use that. In a daily pit session, there were probably six to eight bars roughly (since pit trading hours over the years changed, the number of 60‐minute bars per day will change, too). For your strategy, let's say you use a 14‐period moving average. This will typically represent two trading days.

 Now, fast‐forward to today's electronic markets. Today's markets trade for roughly 23 hours per day. If you still use a 14‐period moving average, that will only equate to a half trading day, instead of the previous two trading days. Do you think that can radically infl uence your historical tests? It sure can!

 How do you handle this? Typically, I rely heavily on daily data, especially the daily settlement prices. Pit and electronic settlements are identical. I do not like using daily highs and lows, since the average range between pit high and low will usually be less than electronic day high and low. If this sounds confusing, just think of an overnight price shock that lasts for an hour before reverting to the previous price level. In the old pit days, such a shock would never have shown up in the data, since it happened overnight. For electronic data, though, the daily high would include this price shock. Therefore, your strategy may perform quite a bit diff erently in the old days versus today's market.

 One trick that helps make all the data the same is to select a standard daily session time, and apply it to your complete historical database. For currencies, for example, the pit used to be open from 8:20 a.m. to 3:00 p.m. Eastern time. To keep this time intact in the electronic era, I simply create a special "currency pit" session from 8:20 a.m. to 3:00 p.m. for all the historical data. Then all my data are consistent.

 With all the available options with data, I highly recommend you take time and think about the data you are using. Making sure it is consistent throughout your test history is defi nitely the best way to test. It may not be that easy to create those data, though.

### ■ **Continuous Contracts**

 One concept that stymies most junior system developers is the use of continuous contracts in futures market testing. Continuous contracts are needed because each futures contract has a limited life, and continuous contracts create a never‐ending data stream. The concept is simple—just artifi cially stitch together expiring futures contracts to create one continuous data stream—but the implementation path is peppered with pitfalls, just waiting to catch the unwary. I'll discuss these pitfalls for the three major techniques of futures data selection.

 The purest way to test with futures data is just to use the raw contract data. Then you don't have to worry about continuous contracts at all. The problem is that most trading software is not set up to easily accomplish this. Let's say, for example, that you want to test a strategy on the euro currency. If you were testing in 2013, from January 1 to approximately March 15, you would use the March contract, 6EH13. From March 15 to June 15, you'd use the June contract, 6EM13. In this way, you'd progress through all the years of your data. But you'd have some problems in testing this way. First, you'd have to put in logic to (1) determine the proper end date for each contract (i.e., before fi rst notice day or last trading day, whichever comes fi rst) and (2) "roll over" the current position from the current contract to the new contract. Certainly, this could be accomplished, but it would require some detailed programming. The bigger issue is if you wanted to optimize the strategy over all these contracts. Most trading software requires an optimization on one chart of data. With multiple contracts of data, you cannot optimize without doing it manually, a tedious and painstaking process.

 To get around these limitations of testing with the individual contracts, many people splice the contract data together in a continuous contract. There are two primary (and numerous less popular) ways to create a continuous contract, and, of course, both have some serious pitfalls. The fi rst type of continuous contract is a nonadjusted continuous contract. Using the preceding example, on March 15 the contract data would switch from March to June. The nice thing about this method is that the original data are preserved—no adjustments have been made to the data. The pitfall with these data is that, at rollover, rarely if ever will the two contracts be the exact same price. Frequently, the front month will have a signifi cant discount or premium to the next month. An example of this is shown in Figure 11.1 . Using these data as is will create false signals and false profi ts and losses. Assume you are long November soybeans, and then you roll over to the May soybeans. With a spread of 38 points, with an unadjusted continuous contract, a trading strategy will think that gap is real and that you profi ted from it. The reality, though, is that you would not actually benefit from the gap. The gap exists only because the contract month has changed.

 Many people get around this artifi cial gap by using what is called a *back‐adjusted contract.* With this type of contract, the gaps are subtracted out, and all previous data

![](_page_4_Figure_0.jpeg)

 **FIGURE 11.1** Contract Prices Will Be Diff erent for Diff erent Months

are adjusted appropriately. An example would be as follows: Suppose on March 15, June euro closes at 1.3512, and March euro closes at 1.3516, a diff erence of .0004. To remove this gap of .0004, all data from March and before must have .0004 added to it. This will remove the gap from all data, and provide a nice continuous data stream. It seems like the ideal solution.

 Of course, no method is perfect, and this technique has a couple of problems, one of which practically no one talks about, at least that I've ever seen. The fi rst problem is that constantly accounting for gaps at every rollover leads to a situation where the historical data actually become negative. An example of this is shown in Figure 11.2 . Clearly, crude oil never had a negative price, but that is what the continuous contract shows and what your strategy will test with. Although the continuous data may seem strange (don't show your friends your "Holy Grail" trading system with these market data, since they'll think you are crazy for testing with negative prices!), the results are accurate, provided you do not fall victim to the second pitfall.

 The second pitfall with continuous back‐adjusted contracts is also the issue most likely to lead to invalid trading results. In a nutshell, you cannot have any indicators

![](_page_5_Figure_0.jpeg)

 **FIGURE 11.2** Back‐Adjusted Continuous Contracts Can Have Negative Prices

that divide or multiply prices when you use back‐adjusted contracts. An example best shows the point:

 Suppose you have a strategy that uses the percentage change in day‐to‐day close, closei /close i <sup>−</sup>1 . On March 10, you are using the March contract, and the close is 1.3500. The previous day close is 1.3420. The percentage change calculation is then 1.3500/1.3420 = 1.00596.

 Fast‐forward to March 20, when the June contract is the front contract. When you performed the continuous contract back adjusting, .0030 was added to it. This is an extreme amount for rollover adjustment, just to prove my point. Thus, now the March 10 close is 1.353, the previous day close is 1.345, and the ratio is now 1.353/1.345 = 1.00595. The ratio for the same date has changed! Plus, it will change again at every rollover in the future. This means that when you back test a strategy with ratios, your back‐test signals will be diff erent than real‐ time signals. The diff erence may not be much, but it will certainly be there. The question will then be "can you rely on performance histories that you know will change in the future?"

 If this seems like a subtle distinction, just imagine what happens when the price data approach zero, the other known pitfall on back‐adjusted data. Dividing by zero or a number close to zero will lead to a huge result! Clearly, that would never happen in real time—unless, of course, the actual price of the instrument in question went to zero. Just do not count on that ever happening!

 The only way around this pitfall is to take special care that division or multiplication is not used with price data in back‐adjusted continuous contracts. Both ratios of prices and percentage changes in prices are no‐nos. If you choose not to follow this rule, do not be surprised when (1) your historical performance results change over time and (2) that your historical results and future results do not match.

### ■ **The Impact of Electronic Markets**

 Many trading system developers test strategies only on electronic data. They ignore any pit data, so their strategies typically only test for the past few years. Their reasoning is that the markets fundamentally changed when electronic markets came on the scene, so strategies that work now don't necessarily have to work in the long‐forgotten pit era. To that argument, I both agree and disagree.

 Electronic markets have undoubtedly changed the futures markets. Without a pit full of traders, the whole dynamic of pricing has been altered. In fact, many former pit traders, who made a very good living while on the fl oor, struggled mightily when they moved to electronic trading. Most were trying to trade as they did on the fl oor, and the market had changed enough that those techniques were no longer profi table. Add in today's high‐frequency trading fi rms, and the short‐term market is certainly diff erent than the old pit trading days.

 On a longer‐term scale, though, almost all commodities are dictated by the law of supply and demand. The venue for trading—electronic, pit, or a combination of the two—doesn't have a long‐term impact. It doesn't make sense to think that high‐ frequency traders, who are in a trade for only a few seconds, have an impact on the price two or three months from now.

 With those contrasting views in mind, I still use pit‐traded data, and the history they provide, for my longer‐term swing‐trading development. That way, my strategy is able to experience more market conditions. If a strategy I develop for soybeans works well in the 1990s, 2000s, and 2010s, I am more confi dent and impressed with the system. Some people would even go back to the 1970s and 1980s! For shorter‐term systems, especially intraday ones, using only the electronic data may make sense. If it also works on pit data, that is great, but I probably would not make it a requirement.

## ■ **Testing with Forex Data**

 If you are testing a forex system, there are two major concerns you need to be aware of. The fi rst issue is that not all forex data are the same. In fact, since the forex is decentralized, there is no offi cial price stream like there is for futures markets. That means that each broker will have its own unique price data set. Of course, if you back test with the same data source that you will use going forward, then there is no issue. But if you test with data from broker A, and then want to trade it live with broker B, the system will now have diff erent data to deal with. In that case, you can basically toss all your back tests out the window, as they are no longer valid. Depending on the data diff erences, your results might be better, and they might be worse. The point is, though, that you have invalidated all your testing by changing data sources.

 The second issue with testing forex data is in the types of orders you use. If you are testing your system with forex data, you really need to be careful with how your strategy places orders. Because of the issue I show later, I only use market orders for entry and exits. My forex strategies never have limit or stop orders in them. Of course, I always add the spread cost into the fi nal profi t/loss on each trade, but by using market orders, I never have to worry about "phantom" fills.

 What is the pitfall to using limit and/or stop orders with forex data? In futures markets, there is one price data stream, which always represents the traded price. With forex, however, there is both a bid data stream and an ask data stream. The difference between these two data streams is the current spread, which is typically a few pips. By defi nition, you can only buy at the ask and sell at the bid.

 The problem with testing a trading strategy with forex data is that the data stream shown on the chart is typically the bid data stream. Although you could alternatively show the ask data stream (if available), most trading software back‐test engines can use only one to calculate trade results. If your trading software can calculate fi lls using bid and ask data simultaneously, you may not encounter this issue. For example, non‐object‐oriented TradeStation can only test with bid *or* ask data. MultiCharts, on the other hand, can test with both bid *and* ask data. It is a good idea to check your software fi rst, though, before assuming this is not a potential issue for you. If it is a potential issue for you, here is an example of how it could be a problem:

 Suppose you are trading the EURUSD forex pair. The current price is 1.3502/1.3505 (I am using an unrealistically high three‐pip spread for this example, but the principle holds for even smaller spreads). That means the bid is at 1.3502, and the ask is at 1.3505. Remember, you can buy at the ask but not below, and you can sell at the bid but not above. Let's also assume your trading software shows you the bid data, so currently it shows 1.3502.

 For this example, your strategy places an order to buy at 1.3500. Shortly after your order, the price drops to 1.3499/1.3502. Since the price on the chart is now 1.3499, and your buy price is 1.3500, the software strategy engine thinks you were fi lled at 1.3500. It thinks you are currently long, but the ask price only hit 1.3502, so in real life you would never be fi lled.

"Big deal!" you might say. "How often can this possibly happen?" Well, it will never happen for losing trades, since for losers the price will keep falling and you will get fi lled in real life, just as your back‐test engine got fi lled. But for winning trades that turn profi table before the ask price hits 1.3500, you will never get filled. Depending on your trading methodology, it could lead to a huge discrepancy between back‐test

engine results and real‐world results. At the very least, your back‐test report will *always* be on the optimistic side. Since you use that information to develop your strategy, you could be basing your trading decisions on some very suspect results. Although the example I presented is for limit orders, the same type of situation occurs with stop orders. You will have stops fi lled at prices that never show up on the bid data chart.

 To get around this issue, you cannot just add slippage to each trade like you can with futures. This is because the bid/ask problem is not a situation of slightly worse fi lls—it is a case of fi lls or no fi lls. Or your software platform may off er advanced order techniques and methods (TradeStation refers to the method as "price series providers"). The key is to be able to back test the same way you trade live. That is precisely why I use market orders for all my forex strategies. Since I use orders such as "sell next bar at market," I can have some losses that are much bigger than a stop‐loss would be, and that is the big disadvantage of market orders. Just imagine, for example, how much the price could change in a fi ve‐minute bar around a Federal Reserve announcement. In the long run, though, I know market orders will always be fi lled, and they back test the same, after accounting for the spread, as they trade in live accounts. Therefore, I have found this situation to be acceptable, since it provides back‐test results that match real market fi lls fairly well.

### ■ **Summary**

 As you can see, the issues behind market data are much more complex than the trading software leads you to believe. It is critical that you put in the time and eff ort up front to examine and understand the market data you are using. Utilizing the wrong data, or using the right data incorrectly, can lead to completely bogus test results. In most cases, unfortunately, you will not even realize there is an issue at all. I recommend that you spend as much time in the beginning reviewing your market data as you do in formulating your entry and exit criteria.
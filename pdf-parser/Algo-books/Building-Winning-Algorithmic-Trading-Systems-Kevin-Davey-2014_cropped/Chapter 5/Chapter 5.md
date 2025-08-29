# Testing and Evaluating a Trading System

 $\mathbf{T}$ f you are going to design trading systems, it is critical that you know how to evalu-Late the performance metrics of a trading system. This is not always as easy as it sounds. To show you what I mean, take a look at Figure 5.1. This equity curve is for a futures trading system, typical of what you might produce if you tested strategies yourself, or one you might find publicly available on the Internet. This curve was produced with TradeStation software, but results from other popular programs, such as MultiCharts and NinjaTrader, are basically the same. All good trading software gives you a variety of important (and, in my opinion, many unimportant) metrics to review and examine. Most of the time, the equity curve and performance report bring up more questions than they answer. Are the results good or bad? Are the results believable? Do the results have any predictive value? Finally, how do you separate the wheat from the chaff? I'll answer these questions and more in this chapter.

The first point to realize and understand when looking at performance reports, equity curves, or trade data is the old adage "if it is too good to be true, it probably is." As a general rule, future performance of a trading system is almost never as good as its historical performance. In fact, the better a trading system tests historically, the less likely it is to perform that well in the future. Of course, there are exceptions to this rule, and after developing trading strategies for a while, these exceptions become easier to find.

![](_page_1_Figure_0.jpeg)

 **FIGURE 5.1** Trading System Results—Is This Believable?

 Why do historical test results usually look better than future results? Some of it has to do with survivorship bias, meaning only the good historical trading systems are typically shown. Why would a vendor sell a system with poor historical performance? Why would you trade a poor system that you created yourself? The simple answer is that in both cases the bad results would be discarded, leaving only the remaining good results.

 It is also possible that the historical test results are indeed valid and that the system developer has uncovered a true edge in the market. Over time, though, this edge may disappear, either due to others fi nding it, market changes, or a host of diff erent reasons. The trading system will then revert to the mean, which would be a breakeven strategy before commissions and trading costs.

 Historical test results also can look better than future results due to the method of the historical testing. Most people test and evaluate systems incorrectly. Later in the book, you'll learn one correct way to test and evaluate systems, but for now just realize that the standard accepted way of testing is wrong. This faulty testing leads to overoptimistic results and trading systems that are sure to disappoint the end user. Of course, experienced traders know how to test systems. The question is: when looking at historical results, how do you know what to believe?

 Figure 5.2 depicts what I call a "BS" meter for performance results. It gives you an idea of who, if anyone, you can trust with providing you trading results.

 At the very top of the scale—the group with the most BS to sling—are trading system vendors. I put this group at the top, even though I have been part of this

![](_page_2_Figure_0.jpeg)

 **FIGURE 5.2** BS Meter for Trading System Results

group (although I trade my systems with my own money, unlike most in this group). In general, any performance information you receive from someone wanting to sell you signals, a black box system, a subscription, trading room, and so on should *not* be trusted. An excellent general rule is: don't believe any of it.

 This approach is extreme, I realize, but given the probability of a vendor's selling a great trading system, as opposed to a vendor's selling you a good‐looking but actually terrible system, this is sound advice. You will save a lot of money by avoiding anyone off ering you a fantastic trading system. Anyone off ering a great trading system for only a little money just doesn't pass my "smell" test—the vendor should be trading it himself, raking in the big bucks, not hawking the system on the Internet for pennies. That is why trading system vendors top the BS list.

 Since trading system vendors typically provide worthless junk, you may be inclined to go the "do‐it‐yourself " (DIY) route. For the DIYers out there, there are dozens of trading platforms that will help you analyze, test, and optimize any type of trading system you want to create. On the surface, this seems to be a great way to go, relying just on yourself, your ideas, and the trading software. The problem, to be discussed in great detail later, is that developing trading systems is not as easy as the software vendors would lead you to believe. In fact, new developers following the approach suggested by the software will inevitably create an overoptimized, curve‐fi t trading system. Such a system will produce a great back test, but will almost never perform well in the real‐time future. So novice DIY developers rank just below trading system vendors on the BS scale.

 If buying from a vendor is fraught with hazard, and novice DIYers not much better, what options are left? If you are convinced that you have to have someone else provide you with a trading system or signals, using a broker‐supplied system or a Commodity Trading Advisor (CTA) system is a much better approach. Let's take a quick look at what they off er, and the advantages and disadvantages.

 Many futures brokers now off er what they call "Broker Assist" or "Follow the Signals"–type services. Two groups that off er these services are Striker Securities (www.striker.com) and World Cup Advisor (www.worldcupadvisor.com). (Full disclosure: I have in the past, or plan in the future, to off er signals through these two brokers. Based on my personal experience, I believe they are reputable.) For a monthly fee, you can "follow" trading signals from a signal provider. The signals provider will typically have an account at the broker and will be placing live trades. So the results shown are typically actual results, a *huge* step above the nonsense most trading system vendors show as "real."

 Of course, just because the results provided by these services are from a traded account, it does not mean you will get the same results. Even real results should be treated as hypothetical. In fact, my general rule is that unless the results actually happened in your account, you *must* treat the results as hypothetical. As you well know, hypothetical leaves the door open for a lot of variation in actual results, which you should be prepared for. That is one disadvantage of the broker services.

 Another possible disadvantage of a broker‐supplied signal service is that something can go wrong with either the developer providing the signals to the broker or the broker itself. For example, if the developer uses a discretionary approach to trade, a personal crisis might throw his/her trading off , and a trading approach that was once good now becomes bad. On the broker side, a quick and sudden fraud, à la the PFG Best corruption and bankruptcy in 2012, might put your account at risk.

 If you choose to follow a CTA, it is reassuring to know that the group is audited by regulators and accounting fi rms and that trading results shown are by‐and‐large accurate. Of course, some unethical bad apples always slip into the bunch, and they may produce stellar results for many years, before being destroyed in an explosion of fraud and deceit. Bernie Madoff and his fi rm, while not a CTA, is a good example of a trusted investment company actually being a complete fraud.

 If you can't believe trading system vendors, with inexperienced DIY trading system developers not being much better, and brokers and CTAs being much better but not without risk, what can you do? What is the low group on the BS totem pole?

 My opinion is that an experienced DIY trading system developer is the least susceptible to BS or otherwise invalid performance reports. I claim this for a few reasons. First, an experienced developer knows his trading back‐test software and knows all the ways to fool it. He knows to avoid these software limitations, where many trading system vendors actively seek out these limitations and use them to produce their faulty, extremely good‐looking performance reports.

 A second reason an experienced developer, creating his own systems, is lowest on the BS scale, is that he is in charge of the process. He can eliminate many potential issues, such as faulty or missing market data, incorrect forward‐looking rules, and overoptimization and curve fi tting. Being in charge of the complete process is an enormous responsibility, but an experienced developer will be quick to fi x issues, since he ultimately is solely responsible for his results.

 Of course, just developing trading systems for many years does not make one an expert. The key is to develop systems and then verify the performance in real time. Over the course of a few years, a good developer will get better and better at producing historical results for trading systems that have a better and better chance of holding up in the future. Certainly, when done correctly, an experienced DIY developer can be pretty low on the BS scale.

 At this point, a few readers are probably asking, "Why even bother testing? All it does is prove something worked in the past. It has no bearing on future performance." This is an argument that has some validity, up to a point. It is defi nitely true that "past performance is not indicative of future results," which is why the U.S. government requires this disclaimer when discussing trading system performance. But does it therefore mean that historical testing has *no* validity? I don't think so.

 Here is a case in point. Let's say you want to build a model of the sun rising. Every day for a month, you get up before dawn, and wait for the sun to appear. Every day, it rises in the east. So, you build you model, run it for tomorrow, and it "predicts" the sun will rise in the east. Will it? Who knows for certain? Some strange axis switching or earth rotation reversing could occur overnight, and the sun could rise in the north, south, or west. Highly unlikely, yes, but so was the fl ash crash of 2010 or the fi nancial crisis of 2008. Outlier and unexpected events can and do happen.

 If such a calamity occurs, does it mean that the model is useless and never should have been built? No, but certainly you'd have to now take into account that the world you modeled has changed dramatically. It is the same for trading systems. Completely new market conditions could render your trading strategy useless tomorrow, or next week or next month, or maybe not at all. But I contend that having a model based on history is much better than completely guessing. With guessing, you are likely to be looking the wrong way when the sun rises tomorrow morning.

 In evaluating trading systems and their performance report and equity curves, it is important to distinguish *how* the results were obtained. There are four main ways to produce results:

- Historical back testing
- Out‐of‐sample testing
- Walk‐forward testing
- Real‐time testing

Each of these is discussed in turn next.

## ■ **Historical Back Testing**

 Historical back testing is the most common method of testing. It is also the easiest to perform, and the easiest to abuse and misuse. The developer simply enters the start date and the end date (usually today's date), includes any parameters to optimize, and then lets the strategy engine do all the calculations. The end result will be the best set of parameters for that period of time, which can then be used in real live trading.

 Unfortunately, there is a major problem when performing a back test in this manner. Assuming that the results are not due to overoptimization—too many rules, too many parameters, and/or too many parameter values—the historical results are by definition going to look great. After all, those results come from optimizing! There is virtually no chance that the results in the future will be close to the optimized results. The results are just too "tuned" to the data used in the test.

 A great example of this is shown in Figure 5.3 . Looking at just the optimized results of a simple trading system, it looks like this is a viable system. But this is because what you see was optimized. Take any other set of parameters and the system will look worse. Going forward, which result do you think is more likely—the one optimized good result or the many poor results? I hope the answer is crystal clear: the poor results are a truer refl ection of the actual system performance. The deceiving part in all this is that sometimes these systems perform well for a time after

![](_page_5_Figure_4.jpeg)

 **FIGURE 5.3** Optimized Results Frequently Fall Apart after Testing

optimizing. In general, though, the more optimization that is done, the less likely the system will work well going forward.

## ■ **Out-of-Sample Testing**

 Only the most inexperienced and naive developers test and optimize their trading system over the whole historical data set. If that has been your approach up until now, this statement may make you mad. But odds are that your real‐time trading results have not been good, or at least not consistently good. Much of that can be attributed to evaluating the strategy's performance on the same data it was optimized on. It is just not a very good practice. Trust me, I know—I used to do it all the time before the market told me, via taking money out of my account, that I was doing things incorrectly!

 Some developers get around this by including an out‐of‐sample period. This is shown in Figure 5.4 . An out‐of‐sample period will be 10 to 20 percent of the data reserved for review after optimization. Typically, the data left for out‐of‐sample testing will be the most recent data. I have, however, seen people apply it to data before their optimization data. The theory behind that alternative approach is that the optimization should include the most recent data, so the strategy is "tuned" to current market conditions.

![](_page_6_Figure_4.jpeg)

 **FIGURE 5.4** Out‐of‐Sample Testing Results

 Conducting a test with out‐of‐sample data is a magnitude or two better than optimizing over all the data, especially if the out‐of‐sample period has a signifi cant number of trades in it. If the optimized results look good with the out‐of‐sample data, there is much more confidence in the optimized results. It will likely perform better in real time.

 One problem with the out‐of‐sample approach is that the optimized parameters are set forever. So, for example, if you optimize your trading system and get values X, Y, and Z as the best inputs to your system, those inputs should never change. But, perhaps due to changing market conditions, you do want the ability to change your input parameters, or at least check them on an ongoing basis. In this manner, the out‐of‐sample test idea can be taken one step further. The resulting analysis, walk‐ forward analysis, is much better, and much closer to reality.

## ■ **Walk-Forward Analysis**

 Walk‐forward analysis is much more cumbersome than traditional back tests, but the results are usually worth the eff ort. Walk‐forward analysis can be done by hand, in conjunction with trading software optimization. This was the method I used to be a top fi nisher in the World Cup contest, and I encourage you to try it by hand a few times to fully understand the process. After that, many trading software packages now include walk‐forward analysis in their available tools.

 The idea behind walk‐forward analysis is simple: the performance results and the optimized results are based on two diff erent data sets. This can be seen in Figure 5.5 .

![](_page_7_Figure_5.jpeg)

 **FIGURE 5.5** Walk‐Forward Analysis

![](_page_8_Figure_0.jpeg)

 **FIGURE 5.6** Walk‐Forward Testing Results

Walk‐forward analysis is simply the aggregate of many out‐of‐sample periods, stitched together.

 Results of walk‐forward analysis, when done correctly, can be much closer to reality than a simple optimized test. A sample of this is given in Figure 5.6 , which shows that the walk‐forward analysis, and the live results are pretty comparable. There is no dramatic shift in performance between live and walk‐ forward results.

 Walk‐forward analysis is a great tool when there are a lot of historical data to analyze. It is my recommended method. But in cases where there is not much historical data, the best approach may be to test and evaluate the trading system in real time.

## ■ **Real-Time Analysis**

 Some very successful traders eschew all forms of back testing due to inherent confl icts and issues in such testing. These folks simply test strategies in real time, possibly even with real money. The obvious advantage to such a method is that fi tting rules to past data and using hindsight bias is just not possible. One big disadvantage is that you can only gather data at market speed. It is impossible to gather statistics over many years until you have tested in real time for many years. Most people do not have the patience to wait for such a test to complete. Another disadvantage is that anytime the strategy is changed, the clock goes back to zero, and the evaluation starts fresh. This can really prolong the test period.

 For the reasons cited, most people do not consider real‐time testing, even with its advantages, as a viable solution. In the trading system development method shown later in this book, however, real‐time analysis is used and provides useful verifi cation of a trading system.
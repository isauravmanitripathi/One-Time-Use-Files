# Trading Idea

nce you have firmly established goals, you are ready to start developing a trading system. At the end of the process, you'll have a trading system ready to test. To get to that point, however, you first have to address the following topics:

- Entry rules
- Exit rules
- Market selection
- Time frame/bar size
- Programming
- Data considerations

The important points in each of these areas are discussed in the next two chapters.

#### How Will You Enter a Market?

Entry rules are the easiest part of designing a trading system for most people. Think of all the trading articles, advertisements, and information you have seen recently. What is usually the focus? "80 percent winning signals!" "Unique neural network entry techniques!" "Never-fail indicators!" "A former rocket scientist develops a foolproof technique for finding winning stocks!" The list goes on and on. Most traders are obsessed with getting the proper entry. Solve that problem, and everything else is a piece of cake, or so they think. The entry lovers love to point to the stock market and say, "Look what would have happened if you had bought Microsoft way back when." These folks tend to ignore the drawdowns during the trade, as long as the entry was correct.

 There is an even more fundamental reason, I believe, for entries being the focus of most traders. The time before entry is really the only time you feel in complete control. You tell the market, "Mr. Market, you must do this, that, and the other before I place a trade to enter. If you do not follow my rules, Mr. Market, I will not enter a trade. I am in charge here." That feels nice, as opposed to the time spent in a trade, where many times you hope and pray the market roller coaster will go your way!

 Entries, of course, are just one piece of the trading strategy puzzle. For ages, people have argued that entries were the most important aspect of a system, or that entries were the least important part. Dr. Van Tharp did a study years ago with random entries, and created successful trading systems by carefully designing the exits. However, I'm sure some people have also created good systems with random exits.

 In my experience, the importance of the entry is directly related to the time you spend in a trade. If you are a long‐term swing trader, with trades lasting weeks to months, you don't need pinpoint accuracy on the entry. An entry a few days early or a few days late will probably not ruin the profi tability of your strategy. If you are scalping, however, then entry becomes very important. An entry off by a tick or two could turn a winning system into a piece of garbage. Keep that in mind when you design your system. Know how exact your entry needs to be before you develop it.

 Many people have trouble developing entry ideas, and that is a shame because entry ideas are all around us. I have a very good trader friend who uses magazine covers as part of his decision process. When he sees a few magazine covers talking about the upcoming drought or the shortage of physical gold, for example, he knows this might be a great time to enter the impacted markets—in the opposite direction, of course!

 I provided some sources for entries in an earlier chapter, and I suggest you keep the list handy when you run out of inspiration. The key, once you have this list of ideas, is to turn them into solid entries that can be back tested. This is where discretion has no place. An algorithmic strategy, by defi nition, consists of an algorithm, a set of rules that defi ne behavior. If your entry rules cannot be defi ned rigidly, then creating an algorithmic system is not appropriate.

 Once you have your entry idea, you need to convert it to computer language. If you do not know how to program in your trading back‐test software, you will likely have to hire someone to do the work for you. Before you do that, it is best to put the rule into what is called *pseudo code.* This is simply the entry instruction, given in plain English. Here is an example:

If close this bar is the highest close of last X bars, then buy next bar at market.

 Converting to a language such as TradeStation's Easy Language would yield the following:

If close = highest (close, X) then buy next bar at market.

 Creating pseudo code is a really important step, since it will help you clarify your entry rule, and help you identify any important variables that you want to optimize ("X" in the preceding example).

A few pointers on creating a good entry:

- *Keep it simple.* If you cannot explain the rule in plain English, you will have a tough time converting it to computer code, and chances are that what you program may not be what you really want.
- *Limit the number of input parameters.* If you have two or three conditions to your entry, it is easy to have 5, 10, or even more parameters you feel should be optimized. Remember, though, that for every parameter you optimize, the more you run the risk of overfi tting your model. Keep it simple. I personally like to use only 1 or 2 optimizable parameters for my entries.
- *Try to think diff erently.* Moving average crossovers have been tested ad nauseum by professionals and amateurs alike. Try to develop an entry unlike any you've ever seen—one that very few others might have tried.
- *Use a single rule at fi rst.* If you want an entry with multiple conditions, fi rst start out with just one condition. Then, slowly add new conditions only if they signifi cantly improve performance. You will likely fi nd that many entry conditions you thought were important really were not.

### ■ **How Will You Exit a Market?**

 Compared to entries, exits are the red‐headed stepchildren of trading strategies. Most people, myself included from time to time, pay very little attention to exits. I suppose it has to do with the lack of control mentioned earlier, since during a trade Mr. Market is in control. It can also be uneasy for many people to think of diff erent ways to escape a losing trade, since the whole point of trading is to have money making trades, right?

 Exits, simply put, have a huge impact on overall profi tability, and a trader really needs to spend a great deal of time preparing proper exits. Just as with entries, there are many diff erent ways to exit. The most common ways are listed below:

- *Stop and reverse.*Your entry signal for a new position also becomes your exit signal for your existing position. Many people like to be in the market at all times, and this method accomplishes just that.
- *Technical‐based exits.* Support/resistance lines, moving averages, candlestick patterns, and the like can all be formed into viable exit rules. The key with using such rules is to make sure they coordinate with the entry rules. Otherwise, exits could trigger immediately after entries triggered.

- *Breakeven stops.* Many people swear by a breakeven stop, where as soon as practical, you move the stop‐loss to a breakeven level. This may indeed be useful for the psyche of discretionary traders or for those obsessed with "winning," who don't want to see a winning trade turn into a loser. In my experience, though, breakeven stops always seem to limit profi t potential, since they typically exit on a retracement, with the market then resuming its earlier trend.
- *Stop‐losses.* Some people swear *by* stop‐losses, and some people swear *at* stop‐losses. I look at it this way: if a stop‐loss, even one far away from your entry, signifi cantly reduces your strategy's performance, perhaps your entry signal is the real problem. Stop‐losses, when coupled with good entries, can help prevent catastrophe. Can you imagine trading the mini S&P, without a stop, right before a terrorist attack? True, you can get excessive slippage with stop‐losses, but barring a market shutdown, at least you can get out, and live to trade another day. Stop‐losses can be dollar based, chart based (i.e., exit near support/resistance), or based on parameters such as average true range. A simple stop‐loss can become very complicated, indeed.
- *Profi t targets.* The old adage "let your profi ts run" is a tried‐and‐true trading malapropism. But letting profi ts run is not always the optimum way to trade. Sometimes it is better to hit a target, profi t based or chart based, and then set up for the next entry signal. I tend to test with profi t targets, but I also allow for a huge profi t on the upper end. Many times, this becomes the best alternative.
- *Trailing stops.* As the market rises in your favor, you keep a certain percentage of the profi t. This really is a moving stop‐loss, but instead of the stop leading to a loss, it leads to a smaller profi t. The one problem with trailing stops is that they can have many parameters that need optimization. The extra parameters may not be worth the eff ort in live trading, although they will certainly make a back test look better.

### ■ **What Markets Will You Trade?**

 One of the toughest decisions you will make when designing your system is which market or markets to trade. There are really two schools of thought in this area, and I'll describe the advantages and disadvantages of each.

 The fi rst method is to design a system for all markets. This would be a "one size fi ts all" approach, where the rules for the system never change as you move from market to market. The parameters, though, could be tuned (or not) for each market. The advantage to this approach is that if one single strategy works well on all markets, then it likely has a high degree of robustness. This may make the system less vulnerable to market changes, since the system has likely seen many types of diff erent markets across the tested history. The big disadvantage to such an approach is that development becomes infi nitely more diffi cult. Designing a system for one market is tough enough. If you now demand that the system work for many markets, you will struggle to fi nd an acceptable strategy. In such situations, developers typically do one of two things: (1) they relax their acceptance criteria, or (2) they test on all markets, and then select the best 5 to 10 performers to trade.

 Realize that both of these compromises, while likely necessary to create a multimarket system, are very bad. Relaxing acceptance criteria will lead you to abandon the system early, as you realize with real money that the strategy does not meet your initial objectives. Testing on multiple markets, and then "cherry picking" the best performers to trade, is just another, albeit sneaky, way of optimizing.

 Creating a strategy for one particular market is the other popular approach. One advantage to this method is that it can be customized to the characteristics of the market. For example, it is known that currencies tend to trend well, so maybe a breakout‐type system is appropriate. Or, for the equity markets, a mean‐reverting strategy with a long bias might be best. Another advantage is that, as mentioned earlier, it is always easier to create a system for one market than for multiple markets. That doesn't mean it is a better system, though; it just means it is easier to create. The disadvantage to creating a single‐market system is that when you create a system knowing the characteristics of the market, you are assuming those characteristics will remain the same forever. While that may be true, what if it isn't? How will your trend‐following currency system perform when currencies, for whatever reason, become mean‐reverting markets?

 As you can see, there are valid points for and against each approach to market selection. I personally have used both over the years. When I fi nished fi rst or second in the World Cup Championship of Futures Trading three straight years, I used a "one size fi ts all" system, traded on roughly a half‐dozen to a dozen markets. That worked well. Currently, about half of the systems I trade are of this variety. I also like single‐ market systems, not only because they are easier to create, but also because I can mix and match them for diversifi cation. In any given year, some of these systems will underperform, some will be around breakeven, and some will outperform. Having a multitude of single‐market approaches makes this more manageable, especially when strategies have to be retired.

### ■ **What Type of System Do You Want?**

 Whenever I begin looking at a new strategy, I almost always see if it can be made into a day‐trading strategy. I defi ne "day trading" as in and out of a trade, or multiple trades, in a single session. There are some nice benefi ts to such a strategy:

- No overnight risk from unexpected events, since you are fl at.
- Reduced margin requirements, making it easier to trade with large size (although most people should not be doing this, as the higher leverage can lead to a greater chance of disaster).

 ■ A "working job"–type feeling. You fi re up the computer in the morning, trade a while, make your daily nut, turn off the computer, and go home and play with your kids the rest of the day—a very satisfying way to live.

 Usually, when I start development, I select short time frame bars (one‐ to fi ve‐ minute), throw in the "set exit on close" statement to exit at the end of the day, and jump into development. Nine times out of 10, though, the strategy fails. Regardless of the entry idea (trend, countertrend, whatever) and exit scheme (fi xed stops, moving stops, breakeven stops, profi t targets, etc.), nothing ever seems to work consistently.

 Inevitably, if I like the strategy idea, I'll then open up the time frame to 60‐minute bars, 240‐minute bars, daily bars. I want to see if my idea has any validity at all. What almost always happens? Performance gets better! Maybe the performance still doesn't meet my goals, but the performance on a daily chart is almost always better than on a 1‐minute chart. I've seen it enough times to realize it is more than a coincidence. The question then becomes: why do I see this behavior? Here's what I have come up with:

- Number of trades and trading costs. Let's say I have a daily bar strategy that trades 1 time per month, or once every 20 bars. That will cost me roughly \$25 in trading costs. If I go down to 1‐minute bars, the same strategy might trade 10 times per day (once every 120 bars), leading to \$250 in trading costs. That is a huge difference in costs that must be overcome. Add in the fact that 1‐minute moves are smaller than daily moves, and it gets even harder.
- There seems to be more randomness in the data as you go to smaller time frame bars. Look at a 1‐minute chart of the mini S&P futures (symbol ES) and most days it is just narrow range noise. It is harder to fi nd the true price path when the random noise level is high. Daily bars, as an alternative, seem to have more trends. Of course, where I see random noise in data could just be due to other biases I have fl oating around in my brain.
- Entry and exits become a much more important part of the system when you have small stops and targets, as most day‐trading systems are set up to be. So I must have really great entries and exits, ones with very good edges. But the better the entry, the harder it is to fi nd during development. Plus, miss the entry by a tick, and you may lose a good percentage of your profi t. If you are swing trading with daily bars, a tick or two at entry probably won't mean as much, relative to overall size of an average trade.
- With tick charts or 1‐ to 5‐minute charts, think about who you are trading against. Many times, it is high‐frequency trading fi rms, which probably have better entries than you and have a speed advantage over you. I feel that the impact of the pros is less noticeable at higher time frames, although I realize many pros trade daily bars, too.

 ■ With most strategies, as I mentioned before, I fi nd the fewer trades there are, the better. This could be due to trading costs, but it also could be due to a very bad reason: maybe you think you have an edge, but with fewer trades, the statistical confidence that you have an edge is a lot lower. Put another way, if I had 2 strategies that averaged a \$50 profi t per trade, and one had 100 trades over the past 10 years, and another had 1,000, I'd always pick the 1,000‐trade strategy (so would every rational person). But the reality is that the 100‐trade strategies are a lot easier to fi nd—maybe because they aren't really edges at all, but just temporarily lucky strategies?

 I really wish that all my strategies were day‐trading‐type strategies. In actuality, probably 9 out of 10 are the exact opposite. My best strategy over the past four or fi ve years holds a position for weeks to months—defi nitely not a day‐trading approach.

### ■ **What Time Frame/Bar Size Will You Trade?**

 Almost as important as the market you will trade is the time frame(s) you select. For most people who look at bar charts, this is simply the length of time for each bar. Of course, strategies will perform radically diff erently on diff erent time frames, so it is best to select a time frame that meets your objectives. Do you want to be in and out quickly? Maybe a 1‐minute or a tick‐based chart is best. Do you prefer long‐term swing trading? If so, maybe a daily or even weekly time frame is what you need. The point is to select a time frame that matches your interest.

 One important factor to realize with time frame is that typically shorter time frames lead to more trades. If you have small transaction costs, with many quick trades, this is terrifi c—just witness the success of all the high‐frequency trading fi rms. Even a small edge can yield big profi ts when repeated enough times. But, for most of us retail traders, higher transactions costs are just part of the game, making quick strategies that much tougher to succeed with.

 When settling on a time size for a bar, an approach that many developers use is what I call *time frame contraction and dilation.* The concept is to test a strategy with a 10‐minute time frame. If it is successful, the thinking goes, then testing on a 9‐minute bar and an 11‐minute bar should also be profi table. One minute either way should not destroy the strategy, and good performance in these contraction and dilated periods suggests robustness.

 I personally have had little success with this approach, and I believe there are two reasons for it. First, by changing the time length of a bar, over the course of a day there are now a diff erent number of bars to evaluate. In the preceding example, changing a 10‐minute bar by 1 minute leads to 9 percent more bars or fewer bars. This can heavily infl uence the performance of indicators you may employ. The other issue I have with this approach is that many traders make their decisions on the close

of a standard period bar. Think of all the people trading off charts, most of them using standard time periods of 5, 10, 15, or more minutes. If your system is trading at a diff erent time, your results can vary widely from the results with a standard (i.e., 10‐minute) bar.

 Putting my personal objections aside, if you have success with 9‐, 10‐, and 11‐minute charts, then I'd agree that your system has robustness in it. It would give me extra confidence. At the same time, though, if 10‐minute performance was good, but 9‐ and 11‐minute performances were awful, I would not necessarily throw out the baby with the bathwater.

 If you decide to test with tick charts, one important consideration with bar size and time frame is the amount of historical data available. I discuss the question "how much data to use" in a later section, but for now realize that many data vendors provide only six months of data. This can also be an issue with short time frame bars (1‐ to 5‐minute), where orders are triggered intrabar. Tick data are also important for specialty bars, such as point‐and‐fi gure charts, Kase bars, Renko bars, and so on. The important point is that if you rely on tick charts or tick data, think carefully about the implications of limited historical data before you test.

 One fi nal important consideration involves the daily settlement price and the daily last price traded, which is important if you are using daily bars. "What is the problem," you ask, "aren't closing/settlement prices and the last price traded the same thing?" In some markets, yes, and in some markets no. Plus, the meaning of these terms has changed with the advent of 24‐hour trading. The gold market is a good example. Back in the days when gold was only pit traded (which may easily be part of your historical testing period), the market closed at 1:30 p.m . Eastern time, and the last trade of the day was usually very close, but not necessarily identical to, the exchange published settlement price. Now, however, the gold market trades electronically, and it trades until 5:00 p.m . Eastern time. Unfortunately, the exchange settlement price is derived from the trading that occurs from 1:28 to 1:30 p.m. You can imagine how the price at 1:29 p.m. , the settlement time, can vary widely from the last price traded at 5:00 p.m . The price action on Wednesday, September 18, 2013, is a great example, as shown in Figure 10.1 . A Federal Reserve announcement at 2:00 p.m., after the settlement price had been established, roiled the markets. The settlement price and the last traded price were dramatically diff erent!

 Data vendors diff er on how they treat settlement prices and last traded prices. As of the time of this writing, TradeStation, for example, uses the exchange settlement as the closing price for daily and weekly bars. For X minute bars, the close of the last bar of the day is also the last traded price. Kinetick, a provider for NinjaTrader, follows the same approach. Another popular data vendor, CQG, however, uses the last price traded as its daily bar close.

 How can this be a problem in your testing? Well, say, for example, you are testing with daily bars, and your strategy uses the instruction "sell the bar at close." Your strategy

![](_page_8_Figure_0.jpeg)

 **FIGURE 10.1** Don't Assume that Settlement Price = Last Price Traded

dutifully executes the command at 4:59 p.m., and you are fi lled. But later, when the exchange settlement price is applied to the data, the strategy will think you were fi lled at the settlement price (which is now the daily bar closing price), but you were actually fi lled near the last traded price. This is just one of the ways back‐test results can fool you.

## ■ **How Will You Program the Strategy?**

 Once you have your basic entry and exit rules thought out; you have selected a market, time frame, and bar size to test; and you have obtained the desired amount of historical data, it is time to put together your strategy for testing. The question for most people at this point is "can I program the strategy myself?" The answer for a true do‐it‐yourselfer is undoubtedly "yes." But if you have never programmed before in the language of your strategy‐testing software, you might fi nd this to be a daunting task. Here are a few tips that might help you out.

 If you are completely clueless about computer programming, and you have no desire to learn how to do it, your programming tasks are best left in the hands of professionals. You can hire an expert at an hourly rate or even a team of experts so that no one developer knows all your trading secrets. The drawback here is that every time you need a code change, even a small one, you will have to wait for the developer to do it, and you'll likely be charged extra for the privilege. The extra time and cost associated with changes, updates, enhancements, and the like can add up quickly. If you still feel that a programmer is the right choice, you can fi nd them at various trading forums, or by contacting your software vendor.

 An alternative is to partner with a programming expert, ideally someone who will be interested in trading the fi nished project. You won't have to worry about your partner's stealing your idea, and the collaboration can lead to far more profi table systems. I have done this before, usually as the programming expert, and it is really satisfying when it works. The problem is in fi nding people you can trust enough to help you.

 My preferred and recommended approach is that you should program everything by yourself. All the trading software packages out there have classes, books, online tutorials, and sample strategies to help you develop your skills. By going this route, you will not have to worry about people stealing your "secret sauce." Plus, as you learn the programming aspect, you will get more familiar with the idiosyncrasies of the back‐test engine. This is really important when results look too good to be true. Once you know the software and programming well enough, you'll never have to wonder if you have only fooled the back‐test engine but not the real world.
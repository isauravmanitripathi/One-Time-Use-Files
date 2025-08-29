# CHAPTER 4 – THE MANY ADVANTAGES OF ALGO TRADING

At this point, you hopefully have a decent idea on what algo trading is, and what it isn't. But you still may be wondering "why should I algo trade?" This chapter will discuss the many advantages for retail algo traders.

### Advantage #1 - No Charlatans With Questionable Trades

A few years ago, I sat in on the webinar of an alleged "trading guru." This person – I won't even call him a trader, since I highly doubt he even actively traded – was a so called expert on trendline trading.

Trendline trading, for those of you unfamiliar with the term, is a method where you draw lines on price charts to capture the major trends. Special significance is given to times where the price touches a trendline and bounces off it, and also to times where the price touches the trendline and then keeps on going through it. In the first instance, the trendline is supposedly "respected" and in the second case, the trendline is "rejected." Both are purportedly meaningful.

This is not the time or place to talk about the validity of such an approach – maybe randomly drawn lines would also sometimes show significance – but the point it is a trading method out there the many people use. Most people using trendlines are likely discretionary traders, where the trendline is just one of the factors (including trader judgment) that influence trade signals. They have rules, but sometimes the rules are fuzzy – not suitable for algo trading.

Anyhow, at one point in the webinar, the presenter showed the following chart:

![](_page_2_Figure_0.jpeg)

*Figure 11- Trendline "Guru" Trade*

"Just look at this example," the carnival barking presenter exclaimed, "This shows the greatness and perfection of trendline trading! A perfect entry, a perfect exit, no danger of a stop being hit, lots of profit. Truly a great trade! Follow my teachings and I'll show you many, many more of these."

No doubt, on the surface, this seems like a great trade. And most of the people in that room were fooled by it, likely plunking down thousands of dollars for "trendline secrets."

But the alleged guru was actually a charlatan. A charlatan showing fantastical, fake trades. How can I say this? Well, let's look a little deeper at this "trade."

First, this trade – if you can even call it that – is purely the result of hindsight bias. This occurs from looking at a completed chart, and then going back and picking a great looking trade. It is easy to do, and hard to "unsee" once you've done it.

Just look at the entry. It is almost at the upper trend line, and based on that it looks valid. But how could that upper trendline have even been drawn? A few bars before the alleged entry, a proper trendline would have

looked like the line in red, not the line in blue. There was no way to draw the blue upper trendline until AFTER the entry occurred. How are you supposed to trade that way? (Answer: you can't!)

![](_page_3_Figure_1.jpeg)

*Figure 12- Hindsight Bias Makes For Great Looking Trendlines!*

That is the charlatan's first sleight of hand – using hindsight bias.

But the shenanigans of this pretend trader do not stop there. Let's assume for a second that the improperly drawn hindsight bias trendline was correct, and take a closer look at the entry. Note how the price does not even touch the trendline at the entry point. In other words a phantom entry! How close does the price have to be to the trendline to count as an entry?

![](_page_4_Figure_0.jpeg)

*Figure 13- A "Close Enough" Entry*

So mistake #2 is assuming a "close enough" entry is valid – you can't do that with a computer tested algo!

Of course, since the guru cheated on the trendline, and gave a phantom entry, is there any reason to believe he got the exit right? Take a look…

![](_page_4_Figure_4.jpeg)

*Figure 14- Incorrect Lower Trendline Changes The Exit Point!*

No surprise here – the guru drew the lower trendline incorrectly, which made the trade appear profitable. But when the trendline is drawn correctly (shown in red in figure above), the profit target NEVER gets hit!

That is the charlatan's third sleight of hand – drawing an incorrect trendline to fake a profitable exit.

So, the charlatan's perfect trade was anything but. Bad trendlines, bad entry and bad exit. In other words, a complete farce of a trade.

**Why is this important to algo trading?** In algo trading, the rules are programmed, and can be accurately tested. No phantom trades, no "close enough" scenarios. The rules in an algo strategy are clear, and the results are unambiguous. The Performance Report can be brutal in its truthfulness, and it does not lie.

Most trading education charlatans (and there are a ton of them) hate algo trading for just this reason. When their supposed awesome techniques are put to a proper test, their approach usually fails miserably.

### Advantage #2 – Increased Confidence Through Backtesting

Just as charlatan approaches are revealed through proper testing, historical backtesting can help you immensely with your strategies. This is a HUGE advantage. Think about the options you have before deciding to trade a particular strategy:

- **A. Trading a strategy where someone else told you "this strategy is great"**
- **B. Trading a strategy you have not tested that you think might be profitable**
- **C. Trading a strategy you have tested and found to lose money historically**
- **D. Trading a strategy you have tested and determined has made money historically**

This might seem like an easy question to answer, and it might even seem ridiculous to you that I even ask it. But, in the real world, you would be amazed at how many people pick the first three options! Let's take a look:

#### **A. Trading a strategy where someone else told you "this strategy is great"**

This is the most common approach to trading. Some guru will tell you how great his or her strategy is, and may even show some hypothetical equity curves to prove it. The strategy could be from a book or a magazine. Or, maybe the strategy itself is kept secret, with resulting signals provided in a chat or trade room.

As far as strategies you might see in a book or a trading magazine, before you trade it, realize that the results shown will ALWAYS be good. Think about it for a second – would you buy a magazine which reveals a trading strategy that lost money? Of course not. So magazine article authors will do everything they can to show profitable results for their strategy. Unfortunately, that usually leads to poor real time performance, since their

strategy was developed based on false pretenses.

The end result with this option is that many people rely on someone else to have done the dirty work – the testing. The question then becomes "Are you willing to risk your hard earned money based on the word of another person?"

#### **B. Trading a strategy you have not tested that you think might be profitable**

This sounds crazy – trading a strategy where you really have no idea if it is profitable or not. An example would be buying any stock that hits a 52 week high, on the theory that it is moving up. This is a reasonable theory, but who knows? Shouldn't you test it first?

#### **C. Trading a strategy you have tested and found to lose money historically**

With the third option, we are getting closer to something good. You take a strategy, and then test it on historical data, to see if it works. That is good. Unfortunately, what many people do is first they see unprofitable results, and second they ignore the results. That sounds crazy, but many people have a "pet" idea, and they are determined that it is valid, regardless of what a historical backtest might say.

#### **D. Trading a strategy you have tested and determined has made money historically**

This final option is the only truly sensible option, and it is what you want to do with your algos. You create an algo, program it in your trading platform (you could also program and test by hand, but it is laborious), and then test it on historical data (backtest it). If it is profitable, you consider trading it. If it is not profitable, you simple discard the strategy, and create another, different, strategy.

The theory here is that if a strategy worked in the past, it is more likely to work in the future. Note I said "more likely." It is far from a guarantee of future performance. It could be that the market could change somehow, or that you made mistakes during the historical test, and that the future

performance of the strategy might be terrible.

But all things being equal, don't you think it is best to at least have a strategy that you have verified has performed well in the past, compared to the other options? That is a major advantage to algo trading – the ability to test. Knowing a strategy was properly tested with profitable results gives you a lot of confidence when you start live trading. None of the options A-C above can give you that type of assurance.

### Advantage #3 – Diversification

There is no "Holy Grail" in trading. There is no strategy or algorithm that will work forever, generating profits consistently with little or no drawdown. Most professional traders know this.

But, diversification comes close to the Holy Grail, at least closer than anything else I have ever seen in my 25+ years of trading.

Why is diversification an advantage with algo trading? The answer is volume. With algo trading, once you have a solid development process established – one that produces profitable trading strategies – you simply create more and more strategies, creating a large library of strategies.

There are two keys when you do this, both related. First, you will diversify by markets. With futures, for examples, there are approximately 40 different markets to choose from in the US. These are broadly grouped into 6 different sectors:

Stock Market Indices Agricultural Products and Softs Currencies Precious Metals Interest Rates Energies

By creating multiple strategies in multiple markets, you create a diversified portfolio. Maybe one week currency strategies will not work well, for instance, but that could be offset by good performance in metals or energies.

The second key is to create different types of algorithms, for different market regimes and behaviors. You will create trend following algos, and also counter trend (mean reverting) strategies. These tend to balance each other out over time.

To be successful with multiple algorithms, in different markets and with different trading styles, one requirement is paramount: the strategy results should have low correlation with each other. It does little good to have a

gold algorithm that has up and down periods at the exact same times as a crude oil strategy. That high amount of correlation would increase, rather than decrease, your portfolio risk.

The reason diversification works is, with uncorrelated algorithms, drawdowns and rough patches occur at different times for different strategies. Maybe a Euro strategy is in a drawdown, but at the same time a Soybean strategy is hitting new equity highs. This is shown in the figure below, where as more and more algorithmic strategies are added, the cumulative equity curve becomes steeper, and the equity curve gets smoother.

![](_page_10_Figure_2.jpeg)

*Figure 15- With Multiple Uncorrelated Strategies, Profits Add, But Drawdowns Do Not*

With the help of trading software, diversification is fairly easy with algorithms. Since they can be automated, it is not difficult for trading

software to monitor 10, 20 or even 100's of trading strategies, entering and exits according to each strategies' own rules. That can become a major advantage.

### Advantage #4 - No Computer Vision Syndrome

If you have been around for a while, I'm sure you've heard about the "screen zombies" – traders who are glued to their computer screen during stock market hours, or maybe all night for Japanese or European hours. These people don't lose focus of the emerging price patterns, even forgoing eating and bathroom breaks.

![](_page_12_Picture_2.jpeg)

*Figure 16- Is This How You Want To Trade?*

That doesn't sound like too much fun for me. But, I guess if it works for them…

Algo trading is completely different. Sure, you will still spend time at the computer, testing new ideas, monitoring positions, etc. But algo trading does not require constant viewing of a trading screen. In fact, given human nature to overrule algorithms, staring at a screen while algo trading is not even desired.

The freedom from the computer screen that algo trading gives you is a major advantage.

## Advantage #5 – Total Control

When you create and trade algorithms, you are in control. You decide all of the following:

- ü What markets to trade
- ü What types of algos to trade
- ü Specifics performance characteristics of each algo (profit, drawdown, expectancy, etc)
- ü How and when to turn algos on and off
- ü Position sizing each algo, in a portfolio
- ü When you will be in trades, when you will not (weekends, overnight)

The list above is not even complete, but you get the idea. You can pick and choose the characteristics of what you are trading, and how you are trading. No more relying on anyone else for black box strategies, signals, etc.

This feeling of control becomes important during the inevitable down periods. Why? Consider two traders:

- Trader A trades a black box strategy. He has no idea what goes into it. It could include random guessing, for all he knows. Sometimes, he has seen it take trades that he disagrees with. It starts to go into a drawdown.
- Trader B trades an algorithm he created. He knows how the strategy was created, knows when it will likely trade, and also knows how long it will likely take to recover. It also starts to go into a drawdown.

Most traders, when given a choice, would undoubtedly prefer to be Trader B. The more you know about an algorithm, and how it was developed, the more comfort you will have, because of the confidence you have in the algorithm construction. It is difficult to be confident of an algorithm where most of its important characteristics are secret.

Of course, all this freedom can be overwhelming, especially to a trader brand new to algo trading. But all these features do not have to be addressed from the start. Starting off with trading one or two algorithms, with one

contract each (or a small share size in the case of stocks), is a great way to "dip your toes in the water" of algo trading, without being overwhelmed. Then, as time goes on, and profits (hopefully) accumulate, a trader can start to explore the advanced topics the come with portfolio trading.

Control over your trading, then, is a major advantage to algo trading.

### Advantage #6 – Always Ready and Willing To Work

Imagine that you are a business owner, running a fast food franchise. To be successful, you need employees. Some of your employees are great, and you are lucky to have them working for your business.

But other employees mainly cause problems. They show up late for work, they steal from you, they insult your customers. Sometimes you wonder "do I really need all this hassle?"

The human factor can be a big factor in the success of your business. Not so with trading algorithms, though.

Your algorithms are your workers. They do what they are told. They do not take off for sick time. They can work 24 hours a day, 6 days a week – whenever the markets are open. They are always ready to go. They do not get scared in volatile markets. They do not get bored and miss trades in flat markets.

Sure, some algos will "steal" from you, causing you to lose money, but for the most part, the algorithms are reliable, loyal employees. Your job will be to pick the right ones!

\*\*\*\*\*

After reading through these major advantages, hopefully you can see why algos appeal to so many traders. You might, in fact, be ready to jump in right now and start trading algos. Not so fast, though – read the next chapter first.
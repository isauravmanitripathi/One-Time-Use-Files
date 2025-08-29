# CHAPTER 6 – HOW TO BEGIN ALGO TRADING ON YOUR OWN

Since you have read this far, I offer you my congratulations. You already know more about algo trading than probably 90% of people out there. You have learned what it is, what it looks like and what kind of personalities are best suited for it.

You have also been exposed to the advantages and disadvantages of this style of trading, and hopefully the downside has not scared you away. Algo trading can be a fun and rewarding experience, but it is not easy. But as I always say, sometimes the best things in life are the hardest things to do. If algo trading was easy, everyone would do it, and there would be no longer be any financial incentive.

Algo trading can definitely help you compete with the "big boys," but it is not automatically a "supertrader" creator. There is no easy way to trade, and algo trading is no exception. Rest assured there are retail algo traders out there surviving against the hedge funds, commodity trading advisors, etc.

At this point, it is time to set aside theory and words, and get down to business: the business of actually starting to algo trade. The next 3 chapters in this book will get you started:

- Beginning Algo Trading On Your Own
- Selecting A Trading Platform
- Info On Popular Platforms

Following that, I'll give you a simple algo example, followed by tips for successful trading, and finishing up with recommended steps to take after

reading this book. When you put it all together, you'll be in a good position to seriously implement algo trading for yourself.

So, let's get started!

## What Is The Best Way To Test?

Last year, I met a trader from Atlanta, Georgia in the US. Based on our discussions, I knew he was a knowledgeable trader. Of course, I did not know for sure if he was a profitable trader (who ever knows for sure, unless you see verified trading records?), but it seemed like he was. In any event, I wanted to pick his brain a bit, as I do with many traders I talk to.

I asked this trader "how do you historically backtest?" His reply shocked me. "I don't believe in backtesting," he explained, "since there are so many ways to cheat. I find historical backtesting useless. So, I do not do it, ever." I was flabbergasted. How can someone trade a strategy without at least testing it first, to see if it even produces a profit?

Apparently, this trader saw no need for historical testing, and as crazy as I personally think it is, to each his own, I suppose. I'll assume, though, that you want to historically test your trading algorithms, which is the exact approach I use. How do you do it?

There are four major ways to test a strategy. I'll highlight the pros and cons of each method, before settling on what I think it the best long term solution for a new algo trader. Any of the methods I discuss, though, could work well.

# Perform Manual Testing

Even in this digital age of computers, many people are scared of computers. While increased knowledge of computers usually makes them less intimidating, let's assume that some people just do not want to test their trading algorithm with a computer. How can they do it?

The answer brings me back to my early days of trading, where I wrote closing prices on a piece of paper, and calculated moving average with a simple handheld calculator. So I know it can be done.

Manual testing involves the trader looking at each bar, making calculations by hand, and manually recording trades as the algorithm he or she is testing gives signals. If that sounds like a slow and painful process, then I have described it well. Manual testing is slow, cumbersome and very prone to errors.

Do you remember earlier when we saw the trendline trader with his "phantom" trades? Someone manually testing might very well count that as a profitable trade. "Close enough" is employed by many a manual tester, especially when profits are involved. It is just human nature – to always look for the optimistic outcome for a trade. The issue is that those optimistic backtest trades usually do not pan out in real time trading.

## **Manual Testing – Pros**

- Trader gets an intimate feel for their algo strategy
- Trader feels confident in results, since he meticulously created them **Manual Testing – Cons**
- Very time consuming
- Prone to errors
- Extremely easy to cheat, miss bad trades, accept "close enough" trades
- Easy to jump from strategy to strategy after a short test period, instead of testing each strategy the same (no consistency)

**Verdict:** Not Recommended, unless you only have one strategy to test – ever!

# Hire a Programmer/Tester

Probably once a week, I get an e-mail from an aspiring trader. Full of excitement, they want me to program and test their "Holy Grail" trading strategy. Unfortunately, though, they lack the programming skills to do themselves, but they'd be willing to let me trade their creation for free if I just program and test it, again for free.

I always decline, since I know the probable outcome. The strategy probably will not backtest well, and then endless tweaks (remember how bad they are?) and modifications are attempted in a desperate attempt to salvage the alleged Holy Grail. When that fails, new strategies are proposed for programming, and the cycle repeats.

This is why hiring a programmer or tester is usually bad. Programmers are expensive, and if you are serious about algo trading, you will have dozens, if not hundreds, of strategies to program and test. The bill for this effort will be substantial.

The benefit to going this route is that if your strategy is complicated, and your programming skills are weak, a good programmer can finish the job a lot more quickly and efficiently than you ever could. And chances are, with an experienced tester, the results will be believable.

### **Hiring Programmer/Tester – Pros**

- Quality work
- Likely faster than doing it yourself

## **Hiring Programmer/Tester – Cons**

- Large budget needed to program lots of strategies
- Your time required to provide detail work requirements to programmer and tester
- Tendency for simple changes to workscope usually leads to drastically increased costs
- No guarantee what is produced will be useful
- Most programmers and testers are not traders, so the end product may look good, but might also be untradeable

**Verdict:** Recommended only if you do not have time to program and test

on your own, and if you have plenty of money to spend on a programmer

## Create Your Own Backtester

Back in the early home computer days, I bought a laptop that I used for work during the day, and trading system evaluation at night. Being on a shoestring budget, I could not afford the premier testing software from Omega Research (later renamed Tradestation). So, since I had some programming knowledge in Fortran and Visual Basic, and advanced knowledge of spreadsheets (Microsoft Excel, Lotus 1-2-3 and Borland Quattro Pro), I decided to create my own backtesting program.

As the months went by, I found that I had a pretty neat little backtest test package. I kept adding on features to make testing go faster, to automate testing, to simulate real conditions, etc. But as the software kept growing, I realized I did not have any finished algos I could trade!

That was a problem, obviously. Somewhere along the line my goal became developing a great backtesting program, instead of developing some trading algorithms.

That is the trap you'll run into if you try to develop your own backtester. Sure, it will be customized to your requirements, but you'll also spend a ton of time working on the software itself, rather than developing strategies. That is true even for advanced programming languages like Python or R. Many open source modules are available in these software languages, giving you a big head start, but you will still spend a lot of time integrating, testing and modifying the pieces.

For a person who is more interested in writing test software, and less so in developing algos, this is a good route to take.

#### **Develop Your Own Backtester – Pros**

- You control the look, feel and functionality
- You can trust the results, since you know the programming code intimately (assuming you programmed things correctly, of course!)
- You may be able to test ideas that many retail platforms struggle with (spread trading, options)

## **Develop Your Own Backtester – Cons**

You need to have programming expertise

- You need trading expertise, so your test engine replicates the real world
- Easy for the software development itself, not trading, to become focus
- Time consuming

**Verdict:** Recommended for hardcore programmers who want a custom trading solution

# Use Retail Trading Software

The final alternative is probably the best one for most retail traders. In today's market, there are literally dozens of trading software packages designed for the retail trader. All have pros and cons, obviously, but the best of them allow traders with little programming knowledge to successfully develop their own trading algorithms.

The great thing about the retail software option is that once you know how to operate the software, and do some simple strategy programming, your focus can be on developing algorithms – exactly where it should be.

### **Retail Trading Software – Pros**

- Most platforms are easy to use and learn
- Used and debugged by other traders, so you can trust results
- Relatively inexpensive, some platforms are even free
- Easy to share strategies with other traders using same software **Retail Trading Software – Cons**
- Easy to trick most packages into giving false results
- With so many choices, hard to pick "right" platform
- If software company goes out of business, algos might be useless

**Verdict:** Recommended for most retail traders. The available software is just too powerful and convenient to disregard.

In case you are wondering, I started out my trading career with the first option, manual backtesting. What a pain! As soon as I had access to a personal computer at night, outside of my regular career working hours, I switched to option 3 – building my own backtesting platform. I did that for a number of years, and had more success in programming the platform than I did in building the algorithms.

I had a few decent algos – or so I thought – but after talking to some more experienced traders, I realized there were issues with my bespoke platform that I was not accounting for properly (for example, some of the intricacies of rollovers). I realized I had to make a drastic change.

Eventually, I decided to go the retail platform route, and I got a copy of Tradestation. I was very scared and intimidated at first by the package (for example, for years I trusted only "buy/sell next bar at market" orders), but eventually I came to understand and felt comfortable with strategy development. And guess what? The algo strategies I started to build became a lot better!

Today, I have been using Tradestation for over 10 years. And baring some unforeseen circumstances, I see myself using it for years to come.
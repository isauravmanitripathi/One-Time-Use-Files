# CHAPTER 1 - THE DIFFERENT TYPES OF TRADING

"Algos" and "algorithms." These two words strike fear into the hearts of many a trader. Visions of computer programs running wild, buying and selling with reckless abandon, are a common nightmare. A trader goes to sleep flat, and wakes up to find a rogue robot algorithm frittered away his or her account, buying and selling all night, due to a simple programming bug.

![](_page_0_Picture_2.jpeg)

*Figure 3- A Trading Robot Run Amuck?*

Or worse yet, the trader wakes up to find he is short 100 ES (mini S&P) contracts, when he only wanted to be short one contract!

Maybe instead your nightmare vision is of hedge funds, executing "killer bot" algos with lightning speed, draining the accounts of all the slower

traders.

The truth, of course, is that trading algos can do those things, and worse. Horror stories abound of these sorts of account killing computer codes. These exact nightmare scenarios have happened. But, properly designed algos can also be friendly, too.

I obviously will focus on the friendly algos!

But before I dive into details of algos, it is important to discuss some of the different types of trading. That will help you understand what an algo is, what it can do, and most importantly, what it cannot do.

#### Discretionary Trading

Most retail people out there are discretionary traders. Discretionary simply means traders use some sort of judgment to enter and exit trades.

For example, a trader hears about a hot stock on CNBC, and immediately decides to buy some. That is discretionary trading.

Another trader has a chart that she stares at all day. It may be filled with indicators, trendlines, moving averages, etc. Or it may be naked, except for price data. Once that trader makes a trade decision based on all she sees, that is a discretionary trade.

Our third trader has a DOM ladder only, a visual tool which shows all the resting buy and sell orders along with prices. He trades based on this tool. He is likely a discretionary trader, too.

At the end of the day, if you asked any of these traders about why they took certain trades, and why they avoided taking other trades (that may have looked exactly the same), they might give you a "deer in the headlights" look, or a vague response like "I don't know, it just felt right!"

The truth is discretionary traders may or may not have rules, they may or may not follow these rules, and they may not be consistent in applying these rules. Heck, they might not even be able to describe the rules that caused them to trade.

I remember being in a trading room with a "price action" guru a while back. He was calling the market live, and it went something like this: "yes, the market is looking weak, and there is a short setup here that I usually take, so I am just waiting for a short entry…waiting…waiting…no, it's a long trade! I just got out with a profit!"

Huh?

When asked about it later, the guru could not explain how a textbook (according to him) short entry suddenly turned into a profitable long scalp trade. "It just felt right," he explained.

It made me wonder if he was even live trading, but that is another story. The point is that he was trading (likely simulated trading) in a discretionary fashion.

Discretionary trading, then, involves trading decisions that involve some

degree of human judgment. Maybe it is intuition, or a sixth sense, or even random guessing, but the trade selection usually includes something that can't quite be defined or tested.

Now, that type of trading might sound wrong to you ("who trades based on intuition?") or it may sound appealing ("great, I get to use my brain to help me decide!"). But the fact is many people do it, and some people are successful at it. It is a legitimate way to trade.

Yet discretionary trading is definitely NOT algorithmic trading.

I'm guessing, if you are reading this book, chances are you might have already tried and failed at discretionary trading. Don't feel bad, I count myself in your ranks – I was never a good discretionary trader. That is the main reason I dove into algo trading.

## Algorithmic Trading

Algo trading is all about rules. In fact, it is nothing but rules. No discretion. No human judgment.

Trading algorithms can be as simple as you want, or as complicated as you want.

How simple? Here is a basic 2 line strategy:

*If close < average close of last 5 bars, go long If close > average close of last 5 bars, go short*

![](_page_4_Figure_5.jpeg)

*Figure 4- Buy/Sell Signals For A Simple Algo*

Over the past 13 years, this strategy would have made over \$92,000 after slippage and commissions, trading just one contract! And it makes money on both the long and short side! Don't get too excited though, the last few years have not been kind to this strategy…

![](_page_5_Figure_1.jpeg)

*Figure 5- A Simple (But Not Consistently Profitable) Algo Equity Curve*

| 2 🛱 🖍 🥘 Account (US Dollar)<br>86   | All data       |                    | 2                   |
|-------------------------------------|----------------|--------------------|---------------------|
| Display: Column View ▼              |                |                    |                     |
| TradeStation Performance Summary    |                |                    | Collapse ☆          |
|                                     | All Trades     | <b>Long Trades</b> | <b>Short Trades</b> |
| Total Net Profit                    | \$92,512.50    | \$84,702.50        | \$7,810.00          |
| <b>Gross Profit</b>                 | \$446,087.50   | \$231,695.00       | \$214,392.50        |
| Gross Loss                          | (\$353,575.00) | (\$146,992.50)     | (\$206, 582.50)     |
| Profit Factor                       | 1.26           | 1.58               | 1.04                |
| Roll Over Credit                    | \$0.00         | \$0.00             | \$0.00              |
| Open Position P/L                   | (\$1.085.00)   | \$0.00             | (\$1,085.00)        |
| Select Total Net Profit             | \$107,590.00   | \$110,475.00       | (\$2,885.00)        |
| Select Gross Profit                 | \$409,512.50   | \$221,292.50       | \$188,220.00        |
| Select Gross Loss                   | (\$301,922.50) | (\$110, 817.50)    | (\$191, 105.00)     |
| Select Profit Factor                | 1.36           | 2.00               | 0.98                |
| Adjusted Total Net Profit           | \$53,462.06    | \$58,355.78        | (\$21,011.18)       |
| Adjusted Gross Profit               | \$427,799.70   | \$218,823.06       | \$201,369.08        |
| Adjusted Gross Loss                 | (\$374,337.64) | (\$160,467.28)     | (\$222,380.26)      |
| Adjusted Profit Factor              | 1.14           | 1.36               | 0.91                |
| Total Number of Trades              | 885            | 443                | 442                 |
| Percent Profitable                  | 67.23%         | 73.14%             | 61.31%              |
| Winning Trades                      | 595            | 324                | 271                 |
| Losing Trades                       | 290            | 119                | 171                 |
| Even Trades                         | 0              | 0                  | O                   |
| Avg. Trade Net Profit               | \$104.53       | \$191.20           | \$17.67             |
| Avg. Winning Trade                  | \$749.73       | \$715.11           | \$791.12            |
| Avg. Losing Trade                   | (\$1,219.22)   | (\$1,235.23)       | (\$1,208.08)        |
| Ratio Avg. Win:Avg. Loss            | 0.61           | 0.58               | 0.65                |
| Largest Winning Trade               | \$5,405.00     | \$4,442.50         | \$5,405.00          |
| Largest Losing Trade                | (\$8,982.50)   | (\$8,520.00)       | (\$8,982.50)        |
| Largest Winner as % of Gross Profit | 1.21%          | 1.92%              | 2.52%               |
| Largest Loser as % of Gross Loss    | 2.54%          | 5.80%              | 4.35%               |

*Figure 6- Typical Algo Performance Report*

That was a very simple algo. In contrast, algorithmic strategies can also be extremely complicated, too. There are traders with single algorithms that run 25,000 lines of code or more – real rocket science stuff!

There are two keys to trading algorithms:

1. They can be tested. Most algorithms can be historically tested, commonly referred to as a backtest. This turns out to be a major advantage of creating algorithms, which I'll describe later. For algos that cannot be historically tested, they almost always can be live tested in simulation mode, with proper precautions and some caveats. In either case, the trader can usually determine the acceptability of the strategy BEFORE trading it with real money.

2. Algorithms are rigidly defined. If the algorithm sees a long setup today, it will tell you to go long. If it sees that same setup tomorrow, it will tell you to go long again. The algo only looks at what it was programmed to look at. It doesn't care what the Fed thinks, does not care about the news, and does not care that Jim Cramer screamed that a certain stock was a buy last night – unless, of course, you program those types of rules into your algorithm. The algo is consistent in how it follows the rules.

Many traders speak of "black boxes," a special type of algorithm. With black boxes, the rules (the algorithm) remain hidden to the trader. He or she only gets the entry and exit signals, and has no idea how those signals were produced.

That type of algorithm might sound unappealing or scary, but many people like that approach. It is really hard to interfere with computer code you cannot even see!

#### Some Examples Of Algo Trading

So what does an algo trader look like? Here are some typical examples: - A retail trader, trading at home. He works full time, so trading is his hobby. Every night, he downloads the latest prices, calculates his signals either by hand or on a computer, and places trades according to the rules. He may or may not check positions during the day, but since he places orders during non-work hours, he knows he is following his strategies each and every day.

- A prop trader, trading full time. He enters and exits trades all day long, again according to set rules. He never, ever deviates from the rules, since he knows his boss spot checks his trades for adherence to the rules.

- A hedge fund computer code, written by numerous PhDs in math, statistics and physics. The computer code they run has 50,000 lines of code, and does everything – enter trades, exits trades, calculates position sizing, automatically performs rollovers, etc. A junior trader is always nearby, monitoring trades in case of a malfunction, but the computer controls the show. The strategies they run can be on the order of microseconds (in and out quickly), to day trades of a few hours, to swing trades lasting weeks.

- A professional retail trader, using a standard retail platform, Tradestation. He creates strategies, then lets Tradestation run those strategies automated. He is usually closely monitoring positions, because as Tradestation personnel say "automated trading does not mean unattended trading." He can trade quite a few automated strategies, assuming he has enough capital, and if his strategies are diversified enough.

What makes these people algorithmic traders is that they follow strict rules for entry and exit. That is the real key – they are 100% rule followers. With those strict rules, they can historically backtest their approaches, and while "past performance is not indicative of future results" (as a U.S. government disclaimer correctly states), it is very nice to realize that the

strategies traded have worked in the past.

Many traders can't commit to 100% rule following, so they fall into the last major category – hybrid trading.

## Hybrid Trading

Now that I have discussed discretionary trading, and algorithmic trading, it is time to bring another type of trading into the mix – what I call hybrid trading.

Hybrid trading is simply a mix of discretionary and algo trading. Some examples:

- Entries are based on technical indicators and rules, but exits are left to the discretion of the trader
- Entries are based on trader judgment, but once in a trade, an automated exit "bot" controls the trade, with no trader intervention
- Entries and exits are both well defined by rules, but the trader has discretion to overrule. For example, a trader might decide to ignore long stock signals after a natural or manmade disaster. Or a trader might decide to go flat before major world events (Brexit vote, Trump election night).

The advantage in hybrid trading is that the trader can still have some discretionary influence on the trade. That is also a disadvantage! One thing I have noticed with my own algo trading is that some of my best algo trades turn out to be ones that my "human judgment" absolutely hated! If I treated those trades as hybrid trades, I would have negated all the good effects of the algo.

\*\*\*\*\*

Reading the last section, you might wonder "what are the professional traders out there doing, and how can I possibly compete with them?" Great question! Pros are using all of the methods detailed above. You can compete by treating trading as a serious endeavor. Don't wish for "I have 15 minutes a day for trading" type systems. Wish for being the best you can be at trading – then you'll be good competition for the pros.

Of all these types of trading, it is hard to decide which trading route is for you. Throughout the book, I'll discuss some of the characteristics and

traits that make for good algorithmic traders, but for now I will assume that you already know algo trading is the path you want to pursue. If you still aren't sure, though, keep reading and maybe by the end of the book you will be sure!
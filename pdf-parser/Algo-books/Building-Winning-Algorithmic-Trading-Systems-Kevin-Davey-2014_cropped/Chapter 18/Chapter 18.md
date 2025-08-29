## Goals, Initial and Walk-Forward Testing

N ow that I've walked you through the strategy development process I use, I think  $\mathsf{N}$  it will be instructive and informative for me to walk you through the development of two strategies I created in March 2013 and started real-money trading in August 2013. If you go to the web site (www.wiley.com/go/algotradingsystems) you will see updates for these strategies, assuming I am still trading them, or a postmortem analysis if I decide to stop trading them.

The next chapters will walk you through the process, and after that Chapter 24 will give running commentary and updates as I trade it live.

## Developing a New Strategy

As with all new trading strategies, first I start out with a SMART goal:

"I want to create a trading system for the euro currency that is an intraday strategy that can earn 50 percent annual return with a median maximum drawdown (determined by Monte Carlo simulation) of 25 percent or less, which is a return to drawdown ratio of 2.0 or better. The system (which may include more than one independent strategy) should make money on 55 percent or more of the days it trades. This trading system will take no more than two trades per day. I will give myself one month of development to complete this task (end of March 2013), and if I do not have a system at that time, I will move on to the next idea."

Is this goal suffi cient for a SMART goal? Let's take a look:

- *Specifi c.* Intraday euro strategy, with specifi c performance goals. Yes, it is specifi c. In fact, it may be too specifi c—it is a pretty long goal statement.
- *Measurable.* 50 percent annual return, less than 25 percent drawdown, return/ drawdown ratio greater than 2.0, 55 percent winning days. Yes, it will easy to measure performance against these benchmarks.
- *Attainable.* 50 percent annual return, less than 25 percent drawdown, return/ drawdown ratio greater than 2.0. When I fi rst started developing systems, these goals were very ambitious. It turns out that developing a strategy the *correct* way is pretty diffi cult. Many people will scoff at these numbers, since they seem small compared to what a decent optimized strategy looks like. Remember, though, that a great‐looking back test does not always mean too much. So, yes, the goals here are attainable. The toughest part will be making the system an intraday strategy.
- *Relevant.* Everything in my goal statement relates to development of this system. Yes, it is relevant.
- *Time bound.* Since I limit myself to one month of development time, this is a time‐bound goal. This time limit will also prevent me from making too many changes to a decent strategy, which will prevent overfi tting and other bad development habits.

 Once I had the SMART goal identifi ed, I could proceed to developing my trading idea.

 From past development experience, I know that intraday systems are diffi cult to develop, much more so than a longer‐term swing system. The best intraday systems, in my experience, are those that trade infrequently and tend to ride winners (trends) as long as possible. That leads me in the direction of a strategy that cuts losses relatively quickly, but keeps winners until the end of the day. To get the biggest bang for the buck, then, this system should trade during the U.S. day session, as many of the big moves occur during this very liquid time period. The problem with this approach is that a system with many small losses and a few big winners will inevitably have a low winning percentage. To counteract this, I will likely need another strategy, one that has small winners, larger losers, and a high winning percentage.

 As you can see, just thinking about the kind of system I want really helped me figure out the best way to proceed. After some more thought, I ended up with the following:

Create two strategies for the euro currency, using continuous contract @EC:

*Strategy 1: Nighttime strategy "euro night."* Runs on 105‐minute bars, from 6 p.m. ET to 7 a.m. ET. All trades are exited by 7 a.m. , so they do not interfere with strategy 2. This strategy will focus on small wins, larger losses, and will initiate trades only until 1 a.m . ET (I have to sleep sometime, in case I do not automate this strategy).

 For the test period, since I am using small bars, I will test back only to January 1, 2009. Typically, for swing systems I use 5 to 10 years of historical data, which means this is a slightly diff erent approach for me. This also avoids my having to test during the 2008 fi nancial crisis, which would likely make development tougher. So note that, in a way, I am taking some shortcuts with this strategy development, since I am (1) using only about 4 years of historical data, and (2) avoiding a major market event. I realize that these shortcuts will lead to a system that is not as robust as it could be, but that is a sacrifi ce I am willing to accept. Strategy development is full of these trade‐off s, and there is not always a correct way to resolve them. Sometimes you just have to try and see what happens, and that is what I am doing here.

 Now that I have the preliminary information established, I can go ahead with the entry and exit rules. I'll start with the exit rules, since those will be relatively fi xed, compared to the entries. For both strategies, I want to lose no more than \$450 per trade, after slippage and commission of \$17.50 per trade. This equates to a loss of 34 ticks. When I go to detailed development, I will allow this stop amount to be lower than 34 ticks, but never more.

 For profi t, with both strategies I will allow the profi t target to be optimized for euro night strategy, and fi xed at \$5,000 for the euro day strategy. Since there has never been a \$5,000 intraday move in euro, the \$5,000 limit is eff ectively saying, "Go for as much profi t as you can, and hold until the end of the trading session."

 The fi nal exit for both strategies will be to close all open trades at the end of the session. This will be a rigid exit, with no optimization needed.

 With the simple exits fi rmly established, the trick to making these strategies successful will lie in the entries. After some cursory examination and testing, it became apparent that reversal‐type entries would be the best thing for both strategies. With a reversal entry, an example of which is shown in Figure 18.1 , the idea is to catch an excursion up or down, before it stops and reverses. This makes these strategies a type of mean reversion, since you are entering against a trend and banking on its reversing before turning into a trend in the opposing direction.

 For strategy 1, the euro night strategy, the long entry is based on the average high of the previous X bars, reduced by a multiplier of the average true range. Of course, the exact opposite entry is true for a short entry. See Figure 18.1 .

 For strategy 2, the euro day strategy, when a highest high of the past Y bars is hit, and the X bar momentum is down, then a limit order to sell short will be placed Z ticks above the current high. The opposite logic holds for long trades. Thus, to get fi lled, the strategy is planning on one more price thrust before the price reverses. An example entry is shown in Figure 18.2 .

![](_page_3_Figure_0.jpeg)

 **FIGURE 18.1** Reversal Entry Example

 What do I think my edge actually is? Based on the reversal entries I am employing, I feel my edge is in identifying very‐short‐term (for night strategy 1) and medium‐ term (for day strategy 2) areas where the price is likely to reverse. By having limit orders away from the current market, I liken my edge to a rubber band. It keeps stretching and stretching until I get my limit fi ll, then it bounces back, giving me profi t. Of course, if the rubber band keeps stretching after my order is filled, that means my premise was wrong, and I pay the price with a full stop‐loss or a loss at the end of the trading session.

![](_page_4_Figure_0.jpeg)

 **FIGURE 18.2** Euro Day Strategy Entry Example

 With all the basic structure of the strategy, along with the entry and exit in place, I can now start the preliminary testing.

## ■ **Limited Testing**

 For limited testing, I chose to look at the results for just 2009. Since my full‐size test will be 2009–present, I am using about 25 percent of the data to do my initial tests. This will give me a good indication of whether my strategy is viable. Remember,

with these tests I am looking for a general indication that my entries, exits, and entries and exits combined are working well.

*Entry test—fi xed‐stop and target.* The results of this test, and all other limited tests are shown in Table 18.1 . All results are acceptable, which allows me to proceed to the in‐depth testing phase.

*Entry test—fi xed‐bar exit.* The results look good and lead me to think I possibly have some sort of edge here with my entry.

*Exit test—similar‐approach entry.* To test the exit, I created an entry condition similar in style (mean‐reverting limit order) to the one I am using. If the results are good, it gives me just a bit more confidence in the exit I have chosen. Results do indeed look good.

*Core system test.* This test is a gentle optimization of the whole system, with entry and exit conditions working together. Results show that the system performs pretty well and is acceptable for further investigation.

*Monkey testing.* This random testing can be very useful it certain situations. Other times, it really doesn't provide any additional information. Such is the case here.

*Limited testing summary.* Both strategies passed all the tests I ran, so the strategies can proceed further through the process. Note that this is the exception, not the rule. Most times, the results will be so poor that no further testing is required, and you can simply move on to the next idea. In a minority of situations, the results will be so‐so, and you may add a rule or fi lter to get better results. In very rare cases, strategies will be acceptable the fi rst time through, which is what happened here. As you develop experience creating and testing ideas, you will fi nd that more and more of your strategies fall into this third category. At the start of your development

|                                      | Euro Night                                                | Euro Day                                                  |
|--------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Entry Test—Fixed‐Stop<br>and Target  | 82% of optimizations<br>profitable                        | 76% of optimizations<br>profitable                        |
| Entry Test—Fixed‐Bar<br>Exit         | Exit<br>after one<br>to<br>five bars >> good              | Exit<br>after one<br>to<br>five<br>bars<br>>> good        |
| Exit Test—Similar‐<br>Approach Entry | Generic mean reversion limit<br>order entry >> acceptable | Generic mean reversion limit<br>order entry >> acceptable |
| Core System Test                     | 85% of optimizations<br>profitable                        | 81% of optimizations<br>profitable                        |
| Monkey Testing                       | Entry better than random                                  | Entry better than random                                  |
|                                      | Exit better than random                                   | Exit better than random                                   |

 **TABLE 18.1 Limited Testing Summary, Euro Day and Night System** 

journey, though, plan on discarding a lot of garbage strategies and adding rules and conditions to most of the rest.

## ■ **Walk-Forward Testing**

 With the limited testing complete, I can now proceed to the detailed walk‐forward testing. This consists of running a full optimization, and then running through the walk‐forward analysis. Figure 18.3 shows the process.

![](_page_6_Figure_3.jpeg)

 **FIGURE 18.3** Walk‐Forward Testing, Euro Day and Night Strategy
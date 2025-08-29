## Trading Psychology

Frequently, I hear from discretionary traders, and the conversation goes something like this:

- **Discretionary Trader:** "I am sick of losing. I am too emotional to trade and make trading decisions at the same time. I want to try algorithmic trading."
- **Me:** "That is good you realized a need to change your losing ways. Why do you think algorithmic trading will work?"
- **Discretionary Trader:** "Because I can be a brain‐dead button pusher and just follow the system. Kind of like that episode of *The Simpsons,* where Homer sets up a drinking bird to continuously tap the "y" key on his keyboard, so he would not have to do any actual work. I want to be the drinking bird, just following the system."
- **Me:** "You do realize that the drinking bird eventually stopped and almost caused a nuclear meltdown, right?"

## **Discretionary Trader:** "Huh?"

 That pretty much sums it up—many people think there is no emotion involved in mechanical trading. Emotions manifest diff erently in algorithmic trading, as opposed to discretionary trading, but they are there, in many diff erent aspects of trading. The nice thing about algorithmic trading is that your emotions theoretically should not matter for entry and exit signals. The key word, of course, is theoretically. In reality, emotions can creep in many diff erent areas of mechanical, 100 percent rules‐based trading. In this chapter, I'll point out some of these major areas and provide tips for how to minimize their impact because, just as with discretionary trading, emotions can really kill the performance of an algorithmic trader.

## ■ When to Begin Trading

Most people, when deciding to go live with an algorithmic strategy, never think about when to actually enter that first position until they do it. But, as I've said before, entering a position in the middle of an open trade can be emotional. Also, what if your system had six consecutive winners—do you wait for a losing trade or two before you start trading? There are really two questions to address:

- Should you start trading your system after looking at its equity curve? 1.
- 2. Should you start trading your system in the middle of a trade, or wait for the next new entry signal?

As with most decisions in trading, there is no absolute right or wrong answer. But if you look at the problem beforehand and make consistent decisions, you can eliminate much of the emotion when starting out.

Let's say you've created a trading system with the equity curve shown in Figure 21.1 (it is from an actual system I have traded with real money). This is a pretty good equity curve for a walk-forward test, and it passed the incubation test you just ran for a few months. The system is at an equity peak, and you are very excited (there is the emotional part!) to begin trading.

At first glance, you see the new high and immediately think, "It is a runaway train, I have to get on now!" That is certainly understandable. At some point, though, that

![](_page_1_Figure_7.jpeg)

**FIGURE 21.1** Sample Walk-Forward Equity Curve

train will slow down or even reverse direction. It is a terrible feeling to start trading a new system at an equity high, only to endure a drawdown right off the bat. So maybe it is better to wait for a small pullback in the equity curve and then begin trading. Of course, you run the risk of there never being a signifi cant pullback, and then think of all the profi ts you'll miss out on!

 Both approaches, starting at or near a new high, or starting after a pullback, have their emotional advantages and disadvantages. On any given system, no one really knows the best approach to take. Over many systems, it probably does not matter all that much—some strategies will continue being profi table right after you start, and other strategies will immediately go into drawdown. For me personally, it seems that most systems go immediately into drawdown, but I think that I forget about the ones whose equity curve takes off and just remember the immediate drawdown systems.

 Given the emotional charge inherent in either approach, the simplest thing to do is to make a decision for all future systems you start trading and then stick to it. For example, you could decide to begin trading after four months of successful incubation, regardless of whether the equity curve is at an equity high, recovering from a drawdown, or somewhere in between. That way, sometimes you'll be right, and sometimes you'll be wrong, but it should be an emotionless task to begin trading.

 Once you have decided on an approach to start trading, you'll realize that there is an existing position that needs to be accounted for. Should you wait for the next new signal? Or should you enter the current winning or losing position? Again, emotion can enter into this decision. As with the equity curve decision, it is best to decide up front and keep emotion out of it.

 Part of the decision to enter an existing trade depends on your software and your trading style. Some automated platforms may have trouble recognizing a manually entered position. This could lead to your exit signal's not being triggered. If this is the case with your software, it is best to just wait for the next fresh entry signal.

 Your trading style also plays a role in entering an existing position. In a fast‐paced day‐trading system, with multiple trades per day, the answer is easy: just wait for the next entry signal. Since they happen often, there will be little to be gained or lost. A diff erent story exists, though, for strategies that have positions on for days, weeks, or months at a time. What is the best approach here? If the position is close to breakeven, just enter it manually. It may cost you or make you a few extra dollars, but in the long run it does not matter.

 The decision gets a little trickier with open positions that are currently big winners or big losers. What approach is best here? Some people will want to enter an open winning trade, on the theory that winning trades will keep on winning. That makes sense, except that you may be incurring much more risk to enter a winner. Let's look at an example. Let's say your trade is set up to yield either a \$500 profi t or a \$250 loss, and you never change the profi t target or stop‐loss. It is now midway through the trade, and you have a \$300 open profi t. Should you enter? Well, initially you had a 2:1 reward‐to‐risk ratio, and by entering mid‐ trade, you have a 200:550 or 0.36:1 reward‐to‐risk ratio. Although the likelihood of your getting a \$200 gain before a \$550 loss is much better than the original likelihood of \$500 gain or \$250 loss, I'd focus more on the downside. Instead of losing \$250 on the trade, you could lose \$550. Ask yourself whether you want to risk that extra loss.

 The same logic applies to open losing trades. In this case, however, your loss would be less by entering midtrade, and your potential gain could be a lot larger. This is the approach I use when starting to trade a new system: if the current open trade is a loser, I enter it. If it is a winning trade, I wait for the next signal, or until the position pull backs in profi t to near breakeven. This is the approach that makes me comfortable. I am not emotional about it, I don't worry if I made the right decision, I just consistently execute the plan. To me, that is the important point.

 As you can see, going "live" with an algorithmic system leaves you with a few conundrums and questions. Over the years, I have probably fi ddled with all combinations of the choices of when to start trading a strategy. I've been through the sheer disappointment of waiting for a pullback in the equity curve, only to see the system go up for months on end. I've also entered open positions and suff ered losses right off the bat, when waiting for the next entry signal would have been better. Similarly, sometimes the opposite occurred, and I "won" at these decisions. Overall, I don't think it has improved my situation at all but has defi nitely led to lost emotional capital. So now I have a plan, known in advance, and I start every system the same way. This eliminates all emotion from the equation.

## ■ **When to Quit**

 Once you've settled on an approach to start trading a system, you've completed half the battle. But, do you know when you'll stop following that new system? Emotions can play a huge role here. Whether you are following your own trading system or following an adviser, newsletter, or some other service, if you don't have an exit plan for discontinuing it, you really need to.

 Why? Studies have shown that when people are under stress, many times they make poor decisions. Certainly, if you were losing money with your systems, you would be stressed. Consequently, you might make a knee‐jerk reaction to the losses, or you may stick your head in the sand and avoid a decision all together. Both scenarios can be dangerous. So the time when you are losing is a bad time to determine when to stop trading a strategy.

 Ideally, you determined when to stop trading when you fi rst decided to trade the system. If not, it is not too late. Just determine the metric(s) that are most important to you. They could include such things as:

- Maximum drawdown.
- Consecutive losers in a row.
- Amount lost in a week/month/year.
- Overall profi t after X months.
- Overall winning percentage dips below XX percent.
- Signifi cant break in your personal equity trend line or equity moving average.
- New highs, or breaking of another "good" metric (yes, some people try to quit at the top).
- Anything that can be measured and monitored.
- Statistical Process Control techniques—for advanced users only.

 The exact condition you select probably is not as important as writing it down and sticking to it. That is the key. It needs to be solid, defi nitive, and written down. Ideally, you'll also tell your spouse or a friend, too, since it is harder to back out when you make the proclamation public.

 I've heard that one money management fi rm's exit criterion is 1.5 times the maximum drawdown, and a 24‐month commitment. Those aren't bad, but the best one is the one that you feel comfortable with—one you can stick with.

 You'll defi nitely worry less about your system's performance if you write down and follow your exit plan.

 Once you have decided on an approach to start with real money trading of a strategy, and formulated an approach to cease trading should things go bad, all you have to do is turn on the system and let it run, right? You can sleep well, go to your day job, and just let the system run, without any emotional expenditure on your part, correct? Certainly, that is how the gurus selling automated "robots" or "advisers" make it sound. That's how they lure many people in: the siren song of emotionless trading. Unfortunately, much like the sailors in ancient Greece who lost their lives sailing to the sound, many a trader has been undone by the emotions involved in so‐called emotionless algorithmic trading.

 Emotions bubble to the surface in mechanical trading in many diff erent ways. The most common time for emotions to come into play is in the decision to take every trade or not. Clearly, if you've tested a strategy and concluded it is worthwhile, then you need to follow it exactly as tested. That sounds easy until a drawdown is incurred, or a number of consecutive losing trades occurs. That is when doubt and fear

creep in. "The last fi ve trades have been losers, and that only happened two times in the walk‐forward back‐test historical testing," says the little voice in your head. "Skip this trade, and wait for a winner fi rst." Unfortunately, this is how the mind works, at least for me. It takes nerves of steel sometimes to overrule the voice in your head. But for any chance of long‐term success, you need to keep taking signals without question. Otherwise, by picking and choosing which trades to take, and which to reject, you have completely invalidated all the testing and analysis behind the system. In other words, you are just gambling, and that almost never ends well.

 Once you get a good feel for your strategy, you'll begin to know ahead of time when a signal is likely to be triggered. For example, at the close of each bar if you are expecting a buy on an upward moving average cross, if the current bar is trending higher, you'll know the cross will occur at the close of the current bar. Greed can take hold here—why not enter now, before the bar closes? Extra profi t might be yours, with no real additional risk. But just like "cherry picking" certain trades, this "jumping the gun" scenario is a really bad idea. There will be times where it doesn't work out, and times it will. You can waste a lot of emotional capital stressing over whether to enter (or exit) early or not. Just remember, though, that when you don't take the entries and exits exactly as your system says, you should not rely on historical results at all. What you've created is a new strategy, with no real historical basis.

 In both of the preceding scenarios, emotions can come in when you make decisions contrary to the strategy rules. So in both of these cases, the emotions can be eliminated by strict discipline—following the rules of the system without question, without fail. This discipline takes time to develop, especially if you are trading only one strategy. Your tendency will be to watch that strategy carefully, think about it often, and inevitably ponder overruling the strategy. My advice in this case is to trade multiple strategies if you can. Once you are trading three or more strategies, it becomes hard *not* to follow the rules. This is akin to the serial liar, who tells so many lies to so many people that eventually the truth comes out. You'll get so confused by what you are actually doing and what you should be doing that just following the rules will be much, much easier.

 In automated trading, I occasionally have to deal with emotions at a stressful time—when something goes wrong. It could be an Internet connection lost, a manual order placed incorrectly, a broker issue, forgetting to roll over, or one of a thousand diff erent "gotchas" that can spring up. Once you notice the issue, or the position mismatch, your stress level goes through the roof. At least mine does. What should I do—exit everything, wait for a better price and reenter, do nothing, run around the room babbling like an idiot? These are all possible reactions to an unforeseen problem; heaven knows I've done my share of incoherent screaming and shouting at times. Emotions can take hold, and terrible decisions can be made in the heat of the moment.

 The solution to eliminating emotions at stressful times like this is surprisingly simple, yet many times tough to implement. Simply sync your real‐world position and your strategy's position as quickly as possible. Don't try to get a better price, fi nesse the order, or any nonsense like that. Just get back in with market orders. Don't think about this decision, don't react to any external stimuli—just execute and get positions to match. Sounds simple, yes, but in reality it can be impossible to do. Just keep it unemotional, and in the long run you'll be much better off .

 I've mentioned it before, but it bears repeating: the key to successful algorithmic trading is discipline. You need to be disciplined enough to follow signals without fail. You have to avoid the temptation to enter early or jump the gun and exit early. Plus, when things go wrong, you absolutely need to get your system back in line with its rules as soon as possible. Your ability to do this will be determined by the amount of discipline you have. Just remember, though, when your emotions take over and you do not follow the rules, you are basically just gambling. Gamblers in the market usually lose.
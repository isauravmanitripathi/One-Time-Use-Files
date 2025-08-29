# Account and Position Sizing

 $\bigvee$  Tow that I've developed a strategy, watched it in real time for a while, and decided to trade it with my own money, then what? How do I determine how much to fund the account with? How do I position size? Do I start small or big? Do I have a position-sizing scheme? If things go bad, when do I quit trading the system?

At the end of the incubation period in mid-August 2013, I truly have no idea how this system will do over the next few months. My hope, as always, is that it will do great, but as with any strategy, I am always prepared to cut my losses and stop trading it if need be.

To avoid confusion later on, here is a summary of my strategies:

#### Two Trading Strategies in Euro Trading System:

- Strategy 1: Euro Night. Trades overnight session, has high winning percentage, lots of little wins, and an occasional big loser. Uses 105-minute bars.
- Strategy 2: Euro Day. Trades day session, lower win percentage, primary profit generator. Uses 60-minute bars.

Both strategies are independent, and I'll be in only one at any given time. Market: Euro Currency Futures (6E).

#### When to Quit

Now that I have decided to start trading my euro strategies live starting on Monday, August 20, 2013, I have to address the question that everyone likes to avoid when starting to trade a new strategy: if things go bad, when do I quit trading the strategy?

 There are probably a million diff erent conditions you could use as a basis for quitting a trading system. You could set a dollar amount or possibly wait until you get a margin call, or wait until you run out of money. You could stop after X losers in a row, or X losing months. There is no "one" right or wrong answer.

But there are three keys to setting a quitting point:

- 1. It should be based on the system you are trading. It makes no sense, for example, to quit after a 10 percent drawdown, if historically the system had 25 percent drawdowns before. This seems obvious, but you'd be amazed at how many people make arbitrary decisions like this, without taking the characteristics of the actual system into account.
- 2. Write it down. Refer to it often. Remember it. This may save you from disaster one day.
- 3. Follow it. If/when the written criteria are (unfortunately) met, *stop trading.* This is a simple, but *very* diffi cult, step to follow.

 I don't always use the same criteria for fi nding my quitting point, but here is how I am doing it for the euro system:

- A. Look at walk‐forward history, and fi nd the worst drawdown that occurred (daily basis). Multiply it by 1.5, since the worst drawdown is almost always in the future. For my system, that worst drawdown comes out to be \$3,265. Multiply this by 1.5 to get \$4,898.
- B. Use Monte Carlo simulation to fi nd the 95 percent level max drawdown. That means, in a year's worth of trading, 95 percent of the time my maximum drawdown will be less than this amount. This turns out to be \$5,082. (If I wanted to be more conservative, I could use the 99 percent level. That drawdown is \$6,512.)

 I should point out those drawdown fi gures assume one contract being traded the whole time. Yet, I will hopefully be trading more than one contract as time goes on. This could get confusing—my actual drawdown (with multiple contracts) could be a lot bigger than my drawdown limit (based on one contract). I just have to remember to calculate the one‐contract drawdown, and compare than to the \$5,000 limit. This will be clearer later, when I set up my monitoring system.

 Using results from points A and B above, I will take the average, and stop trading when the single contract drawdown reaches \$5,000 (slightly rounded).

I have followed points 1 and 2 above. Time will tell if I follow point 3— I better if I need to!

 For this particular system, the only quit point I am considering is the single‐ contract drawdown. This is simple, and pretty robust. If I am trading the system years from now, with many contracts (my hope, of course), I will still have that \$5,000 maximum drawdown per contract limit.

 In the past, I have used the Monte Carlo simulation results to help me decide when to quit. I have also examined, but never implemented, a temporary quit point based on market volatility. When the market gets super‐crazy, it may be best to take a break. I don't think there is a wrong metric or combination of metrics to use to decide when to quit trading. There is probably no "one size fi ts all" optimum, either. The key, in my mind, is to select some criteria that you are comfortable with, write it down, and then follow it exactly. Then, if your system fails, there should be no tears. You knew the system could break, and you quit at a preordained spot.

 I think where people get in trouble is in not having a "quit point," or their quit point is when their money runs out. Speaking from personal experience in the late 1990's, having to quit trading when your money is gone is not a pleasant way to quit.

 What happens when the system performance isn't bad enough to hit your quitting point, and it is not great either, but is somewhere in between? Maybe it is making money, or breaking even, and it is within the bounds of what Monte Carlo simulation says is possible. When do you quit, or otherwise cease trading the system? My general philosophy is to watch the downside and let the upside take care of itself. In this case, I watch the max drawdown and, as long as that is not hit, let the system perform. I do this because I never know month to month or year to year what particular systems I am trading will do good, which will do bad, and which will just tread water. Normally, I'll just let system be and not turn them off or on.

 But a couple of times a year I rebalance systems I am trading—add in new ones and cull the underperformers and possibly adjust the position sizing. If capital becomes an issue, I might very well stop trading and swap out a mildly profi table but underperforming system for a system that I feel has more potential. The analysis details are never the same, and I don't have strict rules on this. I might, for example, stop trading a system because I no longer like it for some reason—maybe it just doesn't fi t me anymore.

 I realize that I am sort of talking out both sides of my mouth here. On one side I say, "Maximum drawdown is my only quitting criteria." On the other side I say, "Unless I come up with another legitimate reason to cease trading it." I rationalize this by saying the maximum drawdown is a hard, solid, worst‐case criterion and will not be violated. At the same time, though, other circumstances may arise that cause the system to fall out of favor. These circumstances might cause me to quit earlier. That is a big gray area, as unfortunately most things are with trading.

 I can say my plan at the start of trading includes only maximum drawdown as the sole criterion for quitting. With the small size and account size I am using to trade this system, I can't foresee needing the capital for a better system. But I am also fl exible enough to realize that circumstances may cause me to alter my quitting point at some time.

### ■ **Minimum Funding Size**

 At this point, I have fi gured out (1) that I will begin live trading the euro day and night system, and (2) I will quit trading if my single‐contract drawdown hits \$5,000. Now I will determine account size. This point is pretty important. Too little capital to start, and I may run out of money before the quitting point. Too much capital and I will have a lower rate of return, as well as an ineffi cient allocation of capital. Currently, the exchange initial margin on euro currency is \$2,750. So, add this to my "quitting point" drawdown, and I get \$7,750. This is the minimum account size I should start with. This will allow me to trade up until my max drawdown is reached.

A few important points to consider:

- I am assuming my broker requires exchange margin, even for day trading. If I had access to day‐trading rates, I could get by with less. This is always a risky proposition, though, since many people just increase their size because of the lower day‐trade margin rates. This is usually not a good idea.
- Margins can and do change. If the exchange required margin goes up, I may be forced to stop trading before hitting my quitting point.
- I am assuming that I am trading a single contract all the time.

 As it turns out, I will want more than \$7,750 in my account, for position‐sizing reasons. I am going to use \$8,500, for reasons that will be revealed later.

# ■ **Position Sizing**

 If you have a good trading system, eventually you will want to start trading it with multiple contracts. There are tons of position‐sizing schemes out there (Van Tharp wrote a huge book on the topic), so there is no right way to do it. There is no Holy Grail position‐sizing technique, though, where you get more reward for no extra risk. The simple way to put it is this way: if you trade more contracts, your reward goes up, but so does your risk.

 Here is what I am doing (at least for a while; hopefully, once my size gets big, I'll become less aggressive):

 As always, I start out with only one contract. Why? Going live almost always reveals issues that back tests, sim tests, and incubation tests keep hidden. For example, if my strategy is automated, what if some quirk in my code sends multiple orders or otherwise goofs up? Or what if my slippage estimates are way off , and real‐world slippage actually makes my strategy unprofi table? My experience is that starting with one contract is the cheapest way to fi nd out and correct any live trading issues.

 A second reason I like starting with one contract is that I want to remain emotionally detached as much as possible from the strategy performance. One‐contract profi t‐and‐loss swings won't impact me or my emotions. Ten contracts, right off the bat, would freak me out a bit—I'd be watching the system too much and have too emotion invested in it. As profi ts (hopefully) accumulate, I can add contracts at a comfortable level, and not be emotionally disturbed by it. If things go really well, in six months or even a year or two, trading 10 contracts at a time with this proven system will seem natural to me.

 Some people would say, "If you have an edge, exploit it fast and furiously by trading maximum size right off the bat. Edges disappear, so take advantage while it exists." That is a good argument, and I understand the concept. But I also know how I best operate, and going "all in" at the start is not good psychologically for me. Of course, you should choose the approach that you feel most comfortable with.

 A fi nal reason I like starting with one contract is that I like the strategy to be self‐generating—profi ts will build the account, leading to more contracts, building it further, leading to even more contracts, and so on. No profi ts mean no increase in size. That just makes sense to me; why allocate more money to a system that isn't generating profi ts?

 One drawback to this approach is that it can take a long time to add that second contract. For example, if you decide to trade one contract for each \$10,000 in your account, you will have to have 100 percent return to add one contract. Then you'll need another 50 percent gain to add a third contract. That can take a long time. Some position‐sizing techniques take this into account (fi xed ratio sizing comes to mind), but these approaches have some negative characteristics I do not like.

I get around this dilemma by sizing my account for roughly 1.5 to 2 contracts at the start. This would be equivalent to starting with \$15,000 in the example I gave just above. Then, I need only a 50 percent gain to add a second contract. This still forces the system to perform well, but at the same time I get contract growth sooner. For me, it is a great trade‐off .

With all that in mind, here are the details:

For my euro system, I have decided to use fi xed fractional sizing.

$$N_{\text{contracts}} = X * \text{Equity}/\text{BigLoss}$$

where

 *N*contracts = Integer number of contracts, always round numbers down.

*X* = Fixed fraction, which I determined through Monte Carlo analysis. For this system, I am using 0.175 (I'll explain later how I got this value).

 Equity = Current equity value. BigLoss = Largest daily loss, \$885 for my euro system.

Using the preceding, I can create Table 20.1 .

 Note that my fi xed fraction of 0.175 might seem awfully high. It may be for most people. I determine it based on risk of ruin, annual return, and max drawdown. I use my Monte Carlo spreadsheet to calculate all that. Based on the position‐sizing analysis so far, I determined that using fi xed fractional sizing with *X* = ff = 0.175 was my best alternative. Please realize that this is my personal preference, based on my personal goals and objectives, and that amount probably would not be right for you.

 The question is, how did I arrive at this figure? Why not just trade one contract all the time, or use a fi xed fractional value of .01 or .02 or 0.10 or 0.50? To determine the position‐sizing scheme that is right for me, I use my Monte Carlo simulator, the basic (one‐contract) version of which you can download for free at the web site (www .wiley.com/go/algotradingsystems). For a given trading system, it will estimate the probabilities of risk of ruin, median max drawdown, and median annual return for the fi rst year of trading.

 The baseline version of this calculator assumes one contract traded throughout the year, but the macro code can be edited to simulate diff erent position‐sizing techniques, which is what I am doing here.

There are four performance numbers I look at:

 1. *Risk of ruin.* How likely am I to hit my defi ned lower cash balance. I want this number low.

| TABLE 20.1 | Position‐Sizing Table |  |  |
|------------|-----------------------|--|--|
| ff =       | 0.175                 |  |  |
| Equity     | Ncontracts            |  |  |
| < \$10,114 | 1                     |  |  |
| \$10,114   | 2                     |  |  |
| \$15,171   | 3                     |  |  |
| \$20,229   | 4                     |  |  |
| \$25,286   | 5                     |  |  |
| \$30,343   | 6                     |  |  |
| \$35,400   | 7                     |  |  |
| \$40,457   | 8                     |  |  |
| \$45,514   | 9                     |  |  |
| \$50,571   | 10                    |  |  |

T AND POSI

TION SIZING

- 2. *Median maximum drawdown.* I have roughly a 50 percent chance of hitting this maximum drawdown sometime during the year. That of course means my maximum drawdown could be much greater than this value, and it could be less. I want it as low as possible, with a personal upper limit I have determined from doing this exercise a bunch of times.
- 3. *Annual return.* As with drawdown, I have a 50 percent chance of reaching this annual return, and it could be much higher or much lower. I want it as high as possible, but I have no lower‐limit threshold acceptable value (although 40 percent is a good value).
- 4. *Return/Drawdown ratio.* Astute readers will recognize this as the Calmar ratio, although true Calmar is calculated over three years, not just one year. I want this value as high as possible, and I have a lower limit for acceptability. (Just for reference, for professional Commodity Trading Advisors a Calmar above 1 is considered pretty good. That means if you want 25 percent annual return, you have to be willing to accept a 25 percent drawdown).

 Using these criteria, I can try a few diff erent position‐sizing approaches, with some diff erent parameter values. Note that this is not all‐encompassing; I have not analyzed many other potential position‐sizing schemes. Maybe one would work better than what I chose.

 Before I reveal the results, I should mention that I played around with the starting balance a bit, although I am not showing those interim results. Basically, by adjusting the initial account size, I was striking a balance between having too much money in the account, being able to add on a second contract relatively quickly (without doubling my account size fi rst), and keeping risk of ruin low. I eventually settled on \$8,500 as the start balance, a good trade‐off among all competing metrics.

 Here are the results, with the one I chose highlighted ("ff " is the fi xed fractional amount) (see Figure 20.1 ).

 My selection meets all my criteria, and I am comfortable with it. This position scheme is the right one for me, right now. *But,* depending on how things go, I might change it down the road, either to a diff erent scheme altogether, or a smaller value of ff (i.e., I will become less aggressive as the account grows). I'll let the performance of the system dictate if and when that happens.

 With the fi xed fractional sizing I have chosen, results say that in an "average" year (meaning, 50 percent of years will be worse, and 50 percent of years will be better), I expect to make \$30,735 profi t in that year and hit a maximum drawdown of 38.1 percent sometime during the year. That profi t number seems a little too good to be true … and my motto is "if something seems too good to be true, it probably is." And that profi t number does seem too good to be true—362 percent rate of return in that fi rst year seems too high, and that makes me suspicious. Remember,

| Start Equity | Ruin | Median<br>Drawdown | Median \$<br>Prof | Median<br>Return | Return/DD | Sizing Method               |
|--------------|------|--------------------|-------------------|------------------|-----------|-----------------------------|
| \$8,500      | 1%   | 19.6%              | \$11,960          | 141%             | 7.12      | 1 contract always           |
| \$8,500      | 1%   | 37.8%              | \$31,598          | 372%             | 9.64      | add at 10K, and every 5K up |
| \$8,500      | 0%   | 22.0%              | \$13,189          | 155%             | 6.81      | $ff = 0.1$                  |
| \$8,500      | 1%   | 32.3%              | \$21,155          | 249%             | 7.86      | $ff = 0.15$                 |
| \$8,500      | 1%   | 38.1%              | \$30,735          | 362%             | 9.55      | $\text{ff} = 0.175$         |
| \$8,500      | 1%   | 43.6%              | \$39,074          | 460%             | 10.44     | $ff = 0.2$                  |
| \$8,500      | 4%   | 53.9%              | \$60,688          | 714%             | 13.38     | $ff = 0.25$                 |

FIGURE 20.1 Position-Sizing Results

though, the actual rate of return could be just about anywhere on the spectrum. It is just that the 362 percent is the median value.

I now look at a histogram of possible returns, shown in Figure 20.2. It will be interesting to see if the year 1 results are anywhere close to the median ending equity (black vertical line). If they are, I will be very happy. I'll still be happy if I even hit the 25 percent mark, which is a final equity of about \$21,000, or a 147 percent return for the year. Almost in "too good to be true" region, but it is a possibility.

![](_page_7_Figure_4.jpeg)

FIGURE 20.2 Histogram of Possible First Year Returns

## ■ **Unequal Position Sizing**

 I am using the same position sizing for the two strategies in my euro day and night system, even though strategies 1 and 2 are for the most part diff erent. The only thing they have in common is the stop‐loss point, around \$425 (34 ticks) per contract. Given their diff erent trade distributions, is the equal position size approach correct? Maybe the position sizing should be diff erent for the two strategies. Possibly, that would improve overall performance metrics.

 As with any trading idea or thought that pops up, I reserve judgment on it until I test and analyze it. The numbers will tell me if this is a good thing to do or not. No emotion is the point, I suppose. I'll spare you some of the minutiae of my analysis, but I primarily looked at "trade two contracts of strategy 1 for every one contract of strategy 2."

#### **Results**

 Current method (identical sizing, both strategies) Acct size: \$8,500 Max DD: 38.1 percent Annual return: 362 percent 2/1 Sizing method Acct size: \$12,500 Max DD: 38.3 percent (same as current method) Annual return: 255 percent

**Conclusion:** I would need more money in the account to trade a 2‐to‐1 ratio, and my annual return would go down. So it does not make sense.

*Note:* I performed a pretty simple analysis to conclude this. Really, what I should do is let the fi xed fractional sizing for each strategy fl oat, and fi nd the optimum for each.
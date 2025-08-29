# Other Considerations before Going Live

 $\mathbf{T}$ n addition to starting with the right account size, knowing when to quit, and set- $\mathbf{I}$  ting up a position-sizing scheme, there are other considerations that you must think about before going live. The list of potential items is long, so here I just highlight some of the issues I have found most important when going live.

#### Accounting, Trading Brokers

I trade multiple systems live right now, and I use various accounts at various brokers. I do this for a few reasons. First, doing all the bookkeeping and accounting gets confusing when multiple systems are all lumped into the same account. More than once, "orphan" positions that I forgot to close pop up. Having one trading system per trading account makes things a lot easier from a management standpoint.

The second reason I use multiple brokers is that sometimes brokers go belly up or walk away with your money. I lost some money when PFG Best went out of business in 2012, when its founder revealed he had been forging bank statements for years. I still have only gotten back about a third of my money, and I doubt I'll ever see it all. I'm no longer mad about it, but when I go back and look at the interview I did on Fox Business Channel right when the scandal broke

(http://video.foxbusiness.com/v/1729212213001/pfgbest-victim-unable-totrade-with-account-frozen), it is clear to me I was in a pissed‐off state of mind. I do not need that aggravation again. To me, spreading my risk around will keep me trading even if one broker fails.

 The drawbacks to my approach are obvious. If I am worried about brokers failing, having more accounts with more brokers just increases the chances of my running into a bad broker, right? My approach may not be better than fi nding the best broker and just putting all my eggs in that basket. The second drawback is that using multiple brokers leads to a less‐than‐optimal use of capital (margin) situation. This leads to less return, since more of my money is not put to use. That, to me, is an acceptable trade‐off .

So, for my euro day and night system, I will open a new trading account.

 After looking at my automation requirements, and the fact that all my code is written in TradeStation Easy Language, it makes the most sense to either use Trade-Station as the broker or a NinjaTrader broker. For the Ninja option, there is a neat little feature in NinjaTrader that will take TradeStation‐generated signals, run them thru NinjaTrader, and then send the signals on to a Ninja Broker. I've used it before with success, so it is a good option. The TradeStation option is the cleanest and easiest, of course.

# ■ **Automation, Unattended, VPS, Where Are Orders Kept?**

 Here are some other topics I had to consider when taking my euro day and night strategy live:

#### **Backup Plans**

 In an ideal world, computers never crash, Internet connections never go down, your broker always is up, and so on. In the real world, lots of things can go wrong. Some things to consider—do you need any of these?

- Backup PC
- Backup data storage (off site and onsite)
- Backup Internet provider
- Backup power supply
- Backup phone line
- Backup broker
- Backup trading desk

 There is more, I know, but having backups (and possibly even backups for the backups) for everything on this list will get you a long way.

#### **To Automate or Not to Automate?**

 During incubation, I manually traded my strategies in simulation mode for a while. I had to have TradeStation alert me, after which I would manually place orders in another platform. Over time, I missed a few trades, made a few mistakes, forgot to cancel open orders, and so on. Overall, I don't think these mistakes cost me any simulation "money." In fact, they may have saved me a few bucks. But that isn't the point. The point is that I want to trade the system as I developed it. So, automation makes the most sense for me. Therefore, I will trade it automated.

#### **Attended, Unattended?**

 TradeStation always warns its clients that "automated trading does not mean unattended trading." This is pretty sound advice, since issues pop up from time to time, Internet connections go down, orders get missed, and so on. I plan on usually being around the PC when this strategy is running, so I'd say it qualifi es as "semiattended." If my account grows and my contract size gets signifi cant, I'll revisit this approach.

#### **VPS**

 Many people use virtual private servers (VPSs) for their trading, to keep the downtime and data lag to a minimum, and their reliability high. I personally do not use any VPS services currently, but I am always monitoring my situation for reasons to use it. In the past year, I've lost Internet connection only twice, and once was on a weekend. If my systems traded more than a few times a day, or if I were running a high‐speed scalping strategy, I'd defi nitely use a VPS.

#### **Where Orders Are Kept**

 I bring this up because many people don't know where their orders are. When your automated strategy fi res an order, is it kept on your machine? On the broker's servers? At the exchange? Plus, diff erent types of orders (limit, stop) may have different routing. For example, limit orders might be sent directly to the exchange, but stop orders may be held at the broker.

 My point in bringing this up is that you should know where your orders are and have plans in place in case something goes wrong. You might think you have an order at the exchange, but after your Internet goes down and a fill was missed, you might realize it was really held on your PC. Emergency situations are not a good time to fi nd out answers to these questions.

# ■ **Rollover Considerations**

 Many traders have diffi culties accounting for rollovers. They wrongly assume they'll have to "eat" the premium between the old and new months, or that they'll pay multiple spreads to accomplish the roll. If you do it correctly, you don't have to pay a premium, but you may have to pay two bid/ask spread costs instead of one, and you'll have to pay the equivalent of one round turn commission. A lot of people are under the mistaken impression that they always lose or gain premium during a rollover. While this might be true for strategies such as scale trading, it does not have to be true for algorithmic systems with a simple rollover. I'll explain all of that with a real‐world example.

 First, it is worth explaining *why* a rollover is necessary. For intraday traders, where positions are closed at the end of each trading day, rollover should never be an issue. On the day of rollover, those traders simply start trading the new front contract month. For swing traders, however, the situation is a bit more complicated. Before fi rst notice day or last trading day, whichever comes fi rst, the trader must "roll" his position from the old contract month into the new contract month. For instance, if you are long September euros, you'll want to sell the September euros, closing you out of that position, and buy the December euros. Not surprisingly, the devil is in the details, and an example is the best way to show the process.

 Let's say I have a system that trades the euro. I use the back‐adjusted continuous contract to calculate all parameters for the strategy. I am currently trading the September contract, but let's say I roll to December this afternoon

 Based on the signal from my continuous contract chart, I bought the September contract at 1.3272 a few days ago. At that time, September was the front month; the continuous contract thinks I entered at 1.3272.

 This system has a \$625 stop‐loss, and a \$1,250 profi t target. So my stop loss is at 1.3222, and my profi t target is at 1.3372. Both of those are based on the September contract, which is what was the lead contract at initial entry.

 Now, a few days later, I have to roll the position into December. Let's fi rst look at the math, and what happens to the continuous contract, and why I don't lose the premium (diff erence) between the two contracts when I roll over. Right at rollover, let's say December was at 1.3303, while September was at 1.3299. This is a diff erence of .0004, which is what the back‐adjusted continuous contract needs to know. To adjust the continuous contract to have December as the front month, you simply have to add .0004 to each price point in the existing continuous contract. So we do this and now have a continuous contract, with December as the front month.

 Now, if you have your trading strategy applied to the updated continuous contract, the strategy will think you bought at 1.3276, with a stop‐loss at 1.3226 and a profi t target of 1.3376. "But wait!" you say. "I didn't buy at 1.3276. I somehow got screwed!" Here's the math, neglecting the bid/ask spread and the commission costs, just for this example.

#### **Real World—What Your Actual Trading Account Sees**

 You bought September at 1.3272. You sold September at 1.3299. Profi t = \$337.50.

You bought December at 1.3303. Current price is 1.3303. Profi t = \$0.

In the real world, you have a closed profi t of \$337.50, an open profi t of \$0.

If your new stop‐loss gets hit, you will lose (1.3226 − 1.3303) \* 125,000 = −962.50.

Add that to the previously closed profi t of \$337.50, and your total loss is \$625. If your new profi t target gets hit, you will gain (1.3376 − 1.3303) \* 125,000 =

+912.50. Add that to the previously closed profi t of \$337.50, and your total gain is \$1,250.

### **Strategy World—What Your Strategy, Acting on a Back‐Adjusted Continuous Contract, Thinks Is Happening**

- For the original continuous contract scenario, the continuous contract thinks I entered at 1.3272.
- This system has a \$625 stop‐loss, and a \$1,250 profi t target. So my stop‐loss is at 1.3222, and my profi t target is at 1.3372.
- For the new rolled‐over continuous contract scenario, the continuous contract thinks I entered at 1.3276.
- This system has a \$625 stop loss, and a \$1,250 profi t target. So my stop loss is at 1.3226, and my profi t target is at 1.3376.
- As you can see, the profi t and loss from the real world and the strategy world is exactly the same.
- Suppose you are long the September euro contract at 1.3222, and it is getting to the time in mid‐September when you must roll over to the December contract. When you have to perform this rollover in an algorithmic strategy, how do you actually accomplish it? I usually do it one of three diff erent ways. Each one has its advantages and disadvantages.

## **Method 1: Quick Roll (Most Expensive Typically)**

 In this approach, you enter a sell order at the market in September euro, and enter a buy order at the market in December euro. Since both orders are market orders, they will be immediately executed. Using the prices above, here is the math:

 Sell September at 1.3299 (bid price) Buy December at 1.3304 (ask price) Closed profi t = \$962.50 − \$5.00 commission = \$957.50 Open profi t = Long from 1.3304 Advantages: Guaranteed fi ll, quick, easy

 Disadvantages: You pay two bid/ask spreads, and if you are not quick with second order, market could run away from you, costing you money.

#### **Method 2: Leg in Roll (Cheapest Method Typically if Done Correctly)**

 In this approach, you enter a sell order at the market in September euro, and try to work a buy order at the bid price in December euro. The sell is immediately executed, and the buy is a limit order, which hopefully will get filled at the price you want. You could also do this in reverse: sell on a limit order, and then when you are filled, immediately buy with a market order. You probably should use the limit order on the side with the biggest spread, and the market order on the tight spread. Using the prices above, here is the math:

Sell September at 1.3299 (bid price)

Buy December at 1.3303 (bid price)

Closed profi t = \$962.50 − \$5.00 commission = \$957.50

Open profi t = Long from 1.3303

 Advantages: You save yourself \$12.50 by getting in the December contract one tick better than you did with method 1.

 Disadvantages: More complicated, plus you may have to chase the market up to get the December fi ll. You can easily lose more than one tick by trying to be too greedy with your limit order.

#### **Method 3: Exchange Supported Spread Roll (Cost Usually between Methods 1 and 2)**

 The exchanges have a great tool to help spreaders—a dedicated quote feed and tradable symbol for executing spread orders, which is what a rollover is. In this case, you are buying or selling the spread, not the individual legs. You get simultaneously fi lled on both legs at the same time. Using the prices above, here is the math:

 Buy spread at 4.5 (ask price). Note that this doesn't tell you the actual execution prices. You'll see these on your statement, and they are really irrelevant. So, we will just assume some prices, keeping the spread fi ll price correct:

Sell September at 1.3329

Buy December at 1.3329 + .00045 = 1.33035

Closed profi t = \$962.50 − \$5.00 commission = \$957.50

Open profi t = Long from 1.33035

 Advantages: Simple, no chance of only one leg executing, cost usually in between methods 1 and 2.

 Disadvantages: Some brokers don't support this. For example, TradeStation's main platform for automated trading does not allow this. You can do it manually in TradeStation Futures 4.0 platform, but that platform is not made for algorithmic strategies. It is also easy to screw up the order, and buy the spread instead of selling it. You have to be careful. Also, don't think that just because you are trading the spread symbol, you'll pay only one commission. Some people think this is true, and I guess those folks don't read their statements very closely. When the brokerage does its accounting, it splits the spread into a separate buy and sell fi ll for each leg. When this happens, commission is charged for each. There is no free lunch, commission‐ wise, with this method!

 You can see from the above example there is \$12.50 cost diff erence between all three methods, with method 1 being the most expensive, method 2 being the cheapest, and method 3 in between the other two. This is not always the case, but is true in general.

 One method I did not mention above is to use limit orders on both sides of the spread. Astute readers have probably already thought about this method, and how it could save the spread on each side of the rollover. There is a reason I have not included it, and that is because it is a *terrible* thing to do. In theory, the approach saves you two spreads, but in reality one spread will be fi lled and the price will more often than not run away from your second limit order, leaving you with half a rollover (in other words, fl at). Thus, the times this approach does work are completely overshadowed by times the approach does not work. In the end, it will cost you much more to try and save a few dollars in spread costs. Therefore, I recommend one of the three methods above, completing the rollover quickly, and then moving on to other trading endeavors.

 That is how a rollover is actually accomplished. Whenever I can, I use the exchange‐supported spreads to do my rollovers. I can do this with systems where I enter orders manually. For my fully automated systems, I generally use method 1, even though it is the most expensive. When I use method 2, I sometimes fi nd myself chasing the market with my order, or worse yet, I forget about the rollover for a while, leaving me temporarily doubly exposed, until I fi x it.
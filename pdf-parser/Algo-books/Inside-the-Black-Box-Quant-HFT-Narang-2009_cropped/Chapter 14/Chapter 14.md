# CHAPTER 74

# **High-Speed Trading**

In skating over thin ice our safety is in our speed. --Ralph Waldo Emerson

s we delve into the subject of high-frequency trading, we must first clarify A a number of important topics. Foremost among these is the difference between high-*speed* trading and high-*frequency* trading. These two concepts are conflated almost continuously by the press, by regulators, and even by reasonably savvy investors. And it is understandable, because the first, which is necessary and inevitable, gives rise very naturally to the second. So highspeed trading and high-frequency trading are cousins, but not synonymous.

High-speed trading is also known as low-latency trading. It refers to the need, on the part of various types of traders, to access the markets with minimal delays, and to be able to act on decisions with minimal delays. In this chapter, we will address why speed is important for many kinds of traders, far beyond HFTs, and also what the sources of latency are and how they can be addressed.

Speed has always, throughout the history of any marketplace, been an important part of separating weaker competitors from stronger ones. There is a good, self-evident reason that equity trading firms and brokerage houses established themselves near the exchanges in New York, and that futures trading firms located themselves near the exchanges in Chicago. The same thing can be found in almost every market center in almost every instrument class around the world. Physical proximity is a good start at being fast, and so is having fast communications between market centers. In 1815, the Rothschild bank in London famously used carrier pigeons to find out about Napoleon having lost the battle of Waterloo. They used this information to go short French bonds and made an enormous sum of money. The founder of Reuters, one of the world's leading news and data vendors, got his start

in 1845 by setting up a carrier pigeon network in London, and within five years, his service was the lowest latency source of information about what was happening in Paris' bourses.1

# Why Speed Matters

In modern electronic markets, the best way to understand why speed matters is to see how it matters for various kinds of orders. After all, regardless of the types of alpha, risk, or portfolio construction models, orders are how strategies get implemented. While there are many kinds of orders especially when we account for all of the various kinds of exchanges around the world—orders can generally be understood as being passive or being active. Furthermore, some orders (passive ones) can be canceled once they are placed. As such, we will describe the three broad cases that capture most of the world's order types as: placing passive orders, placing aggressive orders, and canceling passive orders.

First, a few definitions: *Passive orders* are limit orders that cannot be immediately filled. For example, if the best offer on XYZ is 100 shares at \$100.01, and a trader enters a limit order to buy 100 shares of XYZ at \$100.00 or lower, this is a passive order, because it cannot be immediately filled. In most markets, passive orders are aggregated into an exchange's "limit order book," which shows all of the passive orders for a given ticker on the exchange at a single point in time. An illustration of an order book might look something like Exhibit 14.1.

For this hypothetical market, the limit order book shows a price/time priority. This means that the highest priority goes to orders at the best price (highest price for a buy order and lowest price for a sell order). If two orders have the same price, then the time at which they arrived at market is the tie‐ breaker. Other markets (for example, eurodollar futures) have a price/size

| ID   | Size  | Bid    | Offer  | Size  | ID     |
|------|-------|--------|--------|-------|--------|
| Bid1 | 55    | 100.00 | 100.01 | 2,000 | Offer1 |
| Bid2 | 1,000 | 100.00 | 100.02 | 2,950 | Offer2 |
| Bid3 | 3,100 | 99.99  | 100.02 | 600   | Offer3 |
| Bid4 | 200   | 99.99  | 100.03 | 300   | Offer4 |
| Bid5 | 5,000 | 99.98  | 100.04 | 1,000 | Offer5 |

Exhibit 14.1 Mockup of an Order Book for a Fictitious Ticker

| Size  | Bid    | Offer  | Size  | ID     |  |  |  |
|-------|--------|--------|-------|--------|--|--|--|
| 55    | 100.00 | 100.02 | 1,950 | Offer2 |  |  |  |
| 1,000 | 100.00 | 100.02 | 600   | Offer3 |  |  |  |
| 3,100 | 99.99  | 100.03 | 300   | Offer4 |  |  |  |
| 200   | 99.99  | 100.04 | 1,000 | Offer5 |  |  |  |
| 5,000 | 99.98  |        |       |        |  |  |  |
|       |        |        |       |        |  |  |  |

Exhibit 14.2 Mockup of an Order Book for a Fictitious Ticker after a Large Market Order to Buy

prioritization, which puts larger orders at a higher priority than smaller orders at the same price (the best price would always be the first test).

*Aggressive orders* are immediately actionable orders. There are two major types of aggressive orders. Market orders are always aggressive, because they are instructions to buy (or sell) a specific amount, without regard to price. Thus, if the limit order book looks like Exhibit 14.1, and a market order is entered to buy 3,000 shares, there would be two separate fills. First, the market order would use up the 2,000 share offer at \$100.01 (Offer1), and then the market order would use up 1,000 of the shares offered at \$100.02 (Offer2). Immediately after this trade, assuming no other orders have been filled, the order book would be as shown in Exhibit 14.2.

A second type of aggressive order would be a limit order made at the best offered price (for a buy order). Building from Exhibit 14.2, a limit order to sell 1,000 shares at \$100.00 would use up the first 55 shares bid at \$100.00, and 945 of the next 1,000 shares bid at \$100.00. The order book would now be as shown in Exhibit 14.3, assuming no other orders came in.

In this example, 55 shares (which were from Exch1 in the original example) were filled first, and then the sell order was exhausted by taking 945 of the Exch2's bid at \$100.00, leaving 55 shares at \$100.00 as the new best bid. This limit order to sell was aggressive, because it was immediately actionable.

| ID   | Size  | Bid    | Offer  | Size  | ID     |  |  |  |  |
|------|-------|--------|--------|-------|--------|--|--|--|--|
| Bid2 | 55    | 100.00 | 100.02 | 1,950 | Offer2 |  |  |  |  |
| Bid3 | 3,100 | 99.99  | 100.02 | 600   | Offer3 |  |  |  |  |

Bid4 200 99.99 100.03 300 Offer4 Bid5 5,000 99.98 100.04 1,000 Offer5

Exhibit 14.3 Mockup of an Order Book for a Fictitious Ticker after a Limit Order to Sell at the Bid

| ID<br>Size<br>Bid<br>Offer<br>Size<br>Bid2<br>55<br>100.00<br>100.02<br>1,950 |        |  |  |  |  |  |  |  |
|-------------------------------------------------------------------------------|--------|--|--|--|--|--|--|--|
|                                                                               | ID     |  |  |  |  |  |  |  |
|                                                                               | Offer2 |  |  |  |  |  |  |  |
| Bid3<br>3,100<br>99.99<br>100.02<br>600                                       | Offer3 |  |  |  |  |  |  |  |
| Bid4<br>200<br>99.99<br>100.02<br>1,000                                       | Offer6 |  |  |  |  |  |  |  |
| Bid5<br>5,000<br>99.98<br>100.03<br>300                                       | Offer4 |  |  |  |  |  |  |  |
| 100.04<br>1,000                                                               | Offer5 |  |  |  |  |  |  |  |

Exhibit 14.4 Mockup of an Order Book for a Fictitious Ticker after a Limit Order to Sell, Which Joins the Best Offer

A couple of other terms that bear definition are *joining* and *improving*. To join implies that one adds to the size of the best bid (or offer), which is also known as the first level of the order book, or the inside market. An example of joining is shown in Exhibit 14.4, in which we imagine an additional 1,000 shares are added to the offer side of the book at \$100.02 (Offer6).

We can see that this new order has a lower priority than the 600 shares that were previously offered at \$100.02 (Offer3), because it came in later. This is obviously always true of an order to join: It will always have a lower time‐priority. Orders to join are also always passive as they are not immediately actionable.

Finally, we illustrate improving in Exhibit 14.5. Here, we see a new passive limit order to sell (Offer7) which narrows the bid/offer spread by improving the best offer price from \$100.02 to \$100.01. Because it has the best price of any offer, it receives the highest priority, even though it is the most recent of all of them.

Note that many practitioners tend to confuse passive orders with the notion of providing liquidity, and aggressive orders with the notion of taking liquidity. It is an understandable mistake, because liquidity is often confused

| ID   | Size  | Bid    | Offer  | Size  | ID     |
|------|-------|--------|--------|-------|--------|
| Bid2 | 55    | 100.00 | 100.01 | 2,000 | Offer7 |
| Bid3 | 3,100 | 99.99  | 100.02 | 1,950 | Offer2 |
| Bid4 | 200   | 99.99  | 100.02 | 600   | Offer3 |
| Bid5 | 5,000 | 99.98  | 100.02 | 1,000 | Offer6 |
|      |       |        | 100.03 | 300   | Offer4 |
|      |       |        | 100.04 | 1,000 | Offer5 |

Exhibit 14.5 Mockup of an Order Book for a Fictitious Ticker after a Limit Order to Sell, which Improves the Best Offer

with either volume or the size of the order book. However, as we learned from both the flash crash and the August 2007 quant liquidation, increased volumes do not always imply increased liquidity. In fact, in both instances, imbalances in the volumes of buys versus sells led to incredible illiquidity for anyone on the wrong side of those moves (for example, owners of SPY who wanted to sell into the downdraft on May 6, 2010). On the other hand, aggressive orders to buy units at a time when there are many sellers might be extremely additive to liquidity, even if they technically remove units from the order book. It is our view that this confusion stems from an inaccurate definition of liquidity, and this is itself understandable. Even peer‐reviewed academic journals have inconsistent definitions of liquidity, so it is clearly a concept that can be defined many ways.

We define *liquidity* at any point in time as being the *immediate availability of units to be transacted at a fair price*. This is a useful definition because it accounts for all of the important dimensions of the topic immediacy, size, and a fair price—without being plagued by the problems associated with volume or order‐book dominated approaches. It allows us to understand that an execution strategy to acquire a huge position mostly passively is still removing liquidity from the market. On the other hand, an aggressive order, which nominally reduces the number of units in the order book, is sometimes adding liquidity, if it helps push prices toward a fairer level.

Fairness of price deserves a brief explanation. Here, we refer to a price as fair if it (a) is broadly reflective of the fundamentals of the instrument's underlying economic exposure, or (b) is sensible with regard to other instruments that are similar to it. For example, imagine some company is massively profitable, growing nicely, and trading around \$100 per share. If nothing changes in its business, and the price immediately drops to \$2 per share, it is highly improbable that the test of fairness was met. In this case, we could say that this company's stock became illiquid when the price moved so far without reason. As to the second test, if the index that the company is a part of, or if the other companies in its sector are moving in a similar way, then the price may well be fair (we explain this last concept in more detail when we describe HFT arbitrage strategies in Chapter 15).

With this background, we can now illustrate the importance of speed for passive orders to buy, passive orders to sell, and cancellations of passive orders. There is a single, unifying theme that bears mentioning, and it is known as *adverse selection*. This is a concept that has broad applications in finance (and life). Imagine that we post a job listing for a role that sounds perfectly standard. However, the compensation we offer is extremely low relative to other similar job openings that are on the market. It is probable that we will receive resumes mainly from below‐average candidates. This is because few self‐respecting candidates would apply for an underpaying job. The better candidates, and even most of the average candidates, will apply for the other job openings. And we, rather than drawing a random distribution of good, bad, and average candidates, will be biasing our candidate pool toward the bad side.

Just so, in trading adverse selection is a significant problem that specifically relates to speed.

## The Need for Speed in Placing Passive Orders

Anytime one places a passive order there is a risk of adverse selection. Consider what is really happening when you place a passive order: You're showing the world that you're willing to buy, for example, some number of shares of XYZ at \$100.00. A prospective seller knows this (because your bid is in the order book), but you don't know what information this seller might possess. That seller's information might make you rue buying those shares. Of course, passive orders give the trader the opportunity to earn the bid‐offer spread. Furthermore, some exchanges pay rebates for filled passive orders, and posters of passive orders can earn additional profit by virtue of these rebates. According to internal research conducted by Tradeworx, it is estimated that the average return of all passive orders on the most liquid stocks (above \$50 million in dollar volume per day) for the year 2010 was approximately –0.2 cents per share. This assumes that one can exit the trade at no cost (at the mid‐market price, which is the simple average of the best bid and the best offer, without regard to the size of the bid or offer) *one minute* after entering it. In other words, buying the bid and selling the offer is a money‐losing proposition in the absence of liquidity provision rebates.

So where does the need for speed come into play? Let's start with another imaginary order book for XYZ, as shown in Exhibit 14.6.

Imagine that you place an order to buy 1,000 shares of XYZ at \$100.00 (Bid4). Further, let's imagine that there are a large number of shares bid just after yours at the same price (Bid5). This is shown in Exhibit 14.7.

| ID   | Size  | Bid   | Offer  | Size  | ID     |
|------|-------|-------|--------|-------|--------|
| Bid1 | 3,100 | 99.99 | 100.01 | 2,000 | Offer1 |
| Bid2 | 200   | 99.99 | 100.02 | 2,950 | Offer2 |
| Bid3 | 5,000 | 99.98 | 100.02 | 600   | Offer3 |
|      |       |       | 100.03 | 300   | Offer4 |
|      |       |       | 100.04 | 1,000 | Offer5 |

Exhibit 14.6 Mockup of an Order Book for a Fictitious Ticker

| ID   | Size  | Bid    | Offer  | Size  | ID     |
|------|-------|--------|--------|-------|--------|
| Bid4 | 1,000 | 100.00 | 100.01 | 2,000 | Offer1 |
| Bid5 | 6,000 | 100.00 | 100.02 | 2,950 | Offer2 |
| Bid1 | 3,100 | 99.99  | 100.02 | 600   | Offer3 |
| Bid2 | 200   | 99.99  | 100.03 | 300   | Offer4 |
| Bid3 | 5,000 | 99.98  | 100.04 | 1,000 | Offer5 |

Exhibit 14.7 Mockup of an Order Book for a Fictitious Ticker with Additional Bids

If an aggressive order comes into the market to sell 1,000 shares, you will be filled, and you are now long 1,000 shares of XYZ at \$100.00. However, the best bid remains \$100.00, because there were other orders behind you indicating a willingness to buy at \$100.00. Here, the odds are not bad that you bought at a good price, at least in the extreme near term. This is illustrated in Exhibit 14.8.

But now let's imagine that you place the same 1,000‐share order to buy XYZ, and instead of being at the top of the queue, your order is the last one in the book at \$100.00, with thousands of shares in front of you. Orders to sell come into the market, and eventually, yours ends up being filled. But now, the best bid is lower, at \$99.99 (Bid1), and most likely, the best offer is \$100.00 (Offer6). So, yes, you did technically buy at the bid, but the bid immediately went down and the price you received immediately became the subsequent best offer. This is shown in Exhibit 14.9.

The impact of queue placement was examined empirically by Tradeworx. They found that there is approximately a 1.7 cents per share difference in the profitability of being first versus being last at a given price. This is a truly staggering figure, considering that all passive orders average roughly –0.2 cents per share.

| ID   | Size  | Bid    | Offer  | Size  | ID     |
|------|-------|--------|--------|-------|--------|
| Bid5 | 6,000 | 100.00 | 100.01 | 2,000 | Offer1 |
| Bid1 | 3,100 | 99.99  | 100.02 | 2,950 | Offer2 |
| Bid2 | 200   | 99.99  | 100.02 | 600   | Offer3 |
| Bid3 | 5,000 | 99.98  | 100.03 | 300   | Offer4 |
|      |       |        | 100.04 | 1,000 | Offer5 |

Exhibit 14.8 Mockup of an Order Book for a Fictitious Ticker after 1,000 Shares Have Been Removed from the Bid

| ID   | Size  | Bid   | Offer  | Size  | ID     |
|------|-------|-------|--------|-------|--------|
| Bid1 | 3,100 | 99.99 | 100.00 | 2,000 | Offer6 |
| Bid2 | 200   | 99.99 | 100.01 | 2,000 | Offer1 |
| Bid3 | 5,000 | 99.98 | 100.02 | 2,950 | Offer2 |
|      |       |       | 100.02 | 600   | Offer3 |
|      |       |       | 100.03 | 300   | Offer4 |
|      |       |       | 100.04 | 1,000 | Offer5 |

Exhibit 14.9 Mockup of an Order Book for a Fictitious Ticker after All \$100.00 Shares Have Been Removed from the Bid

Thus, when placing any passive order it is clear that speed is important to the near‐term profitability of the trade. It has been argued by some that long‐term investors (who hold positions for years and hope for profits on the order of dollars per share) should not care about the loss of a penny or two per share by virtue of being a slow, passive trader. But this is an oversimplification. A pension fund with a multiyear time horizon is making a mistake if it ignores the cost of trading, especially if the number of shares transacted is very large. On the other hand, reaching the top tier of speed for a given market costs a great deal of money, and this does not get factored into simple calculations of cents per share. So there is clearly a trade‐off, and the need for speed among passive orders is a function of:

- **1.** Adverse selection metrics (such as those described here)
- **2.** Volume of shares traded
- **3.** The cost of building and maintaining top‐tier speed

Typically, the smaller and longer‐term the investor, the less is the need for higher speed. However, for many strategies (including quantitative alpha strategies such as those described in this book) and many sophisticated large long‐ term funds, transaction volumes are sufficiently high as to warrant at least some investment in faster speeds. This explains the boom in the institutional execution technology business that has occurred since approximately 2007.

## The Need for Speed in Placing Aggressive Orders

Traders placing aggressive orders are willing to pay the bid‐offer spread because they have a reason to get the trade done with more certainty. As we have already shown, there are two kinds of aggressive orders. One is an aggressive limit order, which interacts with an order already resting in the limit order book. The other is a market order. The need for speed is different in each situation, and we will detail both.

In the case of an aggressive limit order, speed is important because you are specifying the price at which you are willing to trade, but others may beat you to that price. As such, the price can move away from you before you are able to complete your trade. Let us begin again with the order book shown in Exhibit 14.6. Imagine that two traders each want to buy 2,000 shares at \$100.01 and they both enter limit orders to that effect. The first order to reach the market will interact with the resting \$100.01 offer for 2,000 shares. The second offer will not get filled immediately, but will become the new best bid at \$100.01 (Bid4). This is illustrated in Exhibit 14.10.

The new best bid belongs to the second order. The first bid interacted with the \$100.01 offer of 2,000 shares and was filled completely. If the price continues to climb, and the trader whose order came to market second continues to lag behind other participants, one of three scenarios may apply to his order: (1) it will be filled at \$100.01 but is subject to adverse selection biases; (2) it will be filled at a higher price if he cancels and replaces with a higher‐priced bid; or (3) it will end up not being filled at all. In any case, this is a bad outcome versus simply having been the first one to bid \$100.01.

The second case is that of a market order. Here, we do not have to worry about getting filled, as market orders will basically always be filled. However, with market orders we have very little control over the price of the fill. Speed matters here because a slowly transmitted market order suffers from adverse selection. If our order to buy is slow in reaching the market, it is less likely that there are other buyers immediately behind us, and we will most likely end up with a worse fill than had we been faster. (This is similar to adverse selection in limit orders.)

In addition, market orders also unfortunately have slippage issues. Let's imagine our order is to buy 2,000 shares of XYZ, and that the order book is that of Exhibit 14.6. Here, if another trader's order (a limit order to buy 2,000 shares at \$100.01, or a market order to buy 2,000 shares regardless

| ID   | Size  | Bid    | Offer  | Size  | ID     |
|------|-------|--------|--------|-------|--------|
| Bid4 | 2,000 | 100.01 | 100.02 | 2,950 | Offer2 |
| Bid1 | 3,100 | 99.99  | 100.02 | 600   | Offer3 |
| Bid2 | 200   | 99.99  | 100.03 | 300   | Offer4 |
| Bid3 | 5,000 | 99.98  | 100.04 | 1,000 | Offer5 |

Exhibit 14.10 Mockup of an Order Book for a Fictitious Ticker after Two 2,000 Share Bids at \$100.01

of price) reaches the queue and gets filled first, our market order incurs slippage and will be filled at \$100.02. This may not be a total disaster in a slow‐moving market, but as we have seen in any very fast‐moving markets, getting filled first can have extremely large consequences in the slippage we pay. What's more, the greater the accuracy of the forecasts (from the alpha model) that drove the desire to trade in the first place, the larger our concern over slippage. After all, a more accurate forecast is more likely to move in the direction we expect, which means that our best trading ideas are also the most important to implement well, when utilizing market orders.

# The Need for Speed in Canceling Passive Orders

The cancelation of passive orders that have already been placed is also highly sensitive to latency. If I send a passive limit order to sell 2,000 shares of XYZ at \$100.00, this order is simply added to the order book. Let's imagine that the current best offer is to sell at \$99.98, two cents better than my offer. I might expect that my order will eventually get filled by virtue of some small fluctuation in XYZ's price. After all, my order is only approximately 0.02 percent away from the current best offer. However, if the market begins moving quickly (as it has a tendency to do at the most inopportune times), it is highly likely that my order will have the same adverse selection problem as any high‐latency order that gets placed. Thus, though I would want to lift my order as quickly as possible, by the time I succeed in doing so, XYZ might well be on its way up to well above my \$100.00 offer price. If I'd been able to cancel this order quickly and replace it with a higher‐priced offer, I might have saved myself money on this trade. Similarly, if similar or correlated instruments begin to rally (e.g., due to some favorable macroeconomic news), it is highly probable that my offer will be lifted and the price at which I sold would be inferior to what I could have sold at if I was (a) aware of the upward pressure in these other instruments, and (b) fast enough to cancel my current offer and replace it with a higher‐priced one.

Perhaps on one 2,000 share order, this difference is not something I care about. But to repeatedly suffer from adverse selection by virtue of a slow cancellation capability will no doubt cost me dearly over the course of a year. There is some controversy regarding the rate of cancelations in U.S. equities (and some other markets), which we will address in Chapter 16.

# Sources of Latency

Having established that it is clearly important for any trader responsible for a reasonably large amount of volume to have access to a low-latency trading platform, we now turn our attention to the potential sources of latency that can be controlled by the trader, and what can be done about each of these sources of latency.

#### Transmission to and from Market Centers

The first potential source of delay for an algorithmic execution engine comes from the time it takes to get data from and orders to market centers. Much of the work of a good execution engine involves reacting quickly to changes in the marketplace; having as close to a real‐time access to those changes is logically the first order of business. Furthermore, getting your orders to the exchange soon after you've decided what to do allows orders to be fresh (as opposed to stale, which is what practitioners call orders that haven't been refreshed very recently).

Information coming from or going to a given venue will arrive fastest if it is going to a location that is physically near the exchange's matching engine itself. The *matching engine* is the software used by the exchange to time‐stamp and prioritize all inbound orders, provide the logic that puts buyers and sellers together, and broadcast the data about all of this activity. This software is physically housed on servers in various data centers (there is usually one data center per exchange). These data centers almost always openly offer space within the same physical location to anyone willing to pay for it. When a trading firm colocates its server (which contains its trading algorithms) in the same facility as an exchange's matching engine, the connection between its server and that matching engine is known as a *cross‐ connect*. In some cases—either because a facility does not allow colocation or because it is too expensive to colocate in a large number of data centers—quants can elect to host nearby (with nearby being a totally arbitrary term here). This is known as *proximity hosting*.

The difference between being near the exchange and being far away can be material in terms of making sure that the orders that are driven off of that data don't suffer from adverse selection. To put some metrics on it, imagine that a given market's data center is in New York. Rather than colocating your servers alongside the exchange's matching engine in New York, you choose to put your servers in San Francisco. A reasonable expectation of the time for information to travel on a relatively fast fiber optic connection between New York and San Francisco is about 50 milliseconds each way, or about 100 milliseconds round trip. To make a decision and place an order, information has to travel from the exchange to your servers and back to the exchange. Thus the total time needed to place an order is about 100 milliseconds. (It will take some time to process and handle this information, but let's assume that this time is negligible for now. It is in any case a constant whether you colocate in New York or use a data center in San Francisco.)

A lot can happen within these 100 milliseconds. For example, in the space of 100 milliseconds there are between zero and more than 40 messages (at the 99th percentile) posted to the various order books for EBAY (just to take a single example).2 The largest number of messages are posted during the more liquid times of day. This implies that almost any sensible trading algorithm will concentrate its activities during the times when the number of messages is highest. If your trading algorithm located in San Francisco trades during these times, your orders will be very far behind other orders, given the 100 millisecond delay. For this reason, we care far more about the message rate and activity at the 99th percentile than we do about the median level, for example. This is an effect we will describe in more detail in "Data Bursts."

It also bears mentioning that data handling software, order generation software, and everything in between resides on servers. These servers must be located somewhere. One possibility is to locate them on your own premises. In addition to the problem with latency described above, an office building rarely has adequate power, cooling (servers generate an extreme amount of heat), network speed, and emergency backup capabilities to ensure continuity. As such, most people locate expensive, mission critical servers in data centers (also known as colocation facilities). If you're going to colocate a server, the least arbitrary and most useful place to do so is at or near the exchange.

#### Transmission between Market Centers

Another potential source of latency for an algorithmic execution algorithm comes from the aggregation of data between market centers. Even for a single instrument class there are often multiple venues on which to transact these securities. For example, in the case of U.S. equities there are 13 different official exchanges on which investors can trade, and dozens more (approximately 60 as of the writing of this book) dark pools as well. When information arrives from multiple venues, it has to be aggregated into one big set of data. (Although there are services that consolidate the data for you, these consolidated data feeds contain substantial latency. It is far better to consolidate the data yourself, if you can do it well.) We will address the issue of consolidation separately, but in order to consolidate the data, all of the data have to be in one place physically. The connections between the various exchanges can be visualized as a *mesh*. As in the previous section, the further away a given market's various data centers are from one another in the mesh, the more natural latency there is in the system, and the harder it is to consolidate all of the data into one place physically. All of the points made in the previous section apply here: The further away a given market's various data centers are from one another, the more natural latency there will be, and the harder it is to solve this problem.

Let us further look at the problem of consolidating data between market centers. Many strategies look across instrument classes to make trades. For example, most market makers in U.S. equities (which generally trade in the vicinity of New York City) are very keen to know, with minimal latency, what the S&P E‐Mini futures contract (called the "ES" futures contract) is doing in Chicago. This is because the ES tends to lead both the SPY (an extremely important ETF that tracks the S&P 500 index) and the independently traded constituents of the S&P 500 index.3

The most important long‐distance problems in the finance world are getting information back and forth between Chicago and New York, and between New York and London.4 Data travel at the speed of light, but the problem is that one must transmit data over some medium. Data can't be beamed through the air (in the form of light) in a "straight line" over thousands of miles due to the curvature of the earth and a wide variety of potential physical obstacles along the way (e.g., buildings, airplanes, birds). If this were somehow possible, it would take just under four milliseconds for data to reach New York from Chicago (and vice versa). As of the writing of this book, a typical commercially available solution for low-latency communications between Chicago and New York has a one‐way latency of seven to eight milliseconds. This is over a fiber optic network, which (a) transmits data through glass (the material that fiber optics are essentially made from), and (b) is somewhat circuitous, as there is no telecommunications company with a direct route between Chicago and New York. Light travels about 1.3 times faster through the air than through glass—this explains some of the extra latency. The indirect route a conventional fiber optic network takes between Chicago and New York explains most of the rest, and the small remainder is attributable to suboptimal hardware.

To solve this problem, a company called Spread Networks undertook a fascinating endeavor to make a much more direct path between Chicago and New York. They leased and bought tracts of land along this path, and found the straightest path possible (cutting through mountains in some cases). They used the best equipment that money could buy. They reportedly employed 126 four‐person crews to lay a one‐inch‐wide line. Ultimately they reduced the distance over which light had to travel by more than 100 miles.5 In order to use their service (which immediately sold out), customers had to sign multiyear contracts rumored to cost on the order of \$10 million. In exchange, the one‐way latency between Chicago and New York was reduced to about 6.5 milliseconds—1 millisecond faster than the more conventional telecommunications solution described earlier.

But this arms race to zero (as the pursuit of minimum latency is less‐ than‐affectionately known) scarcely ended with Spread Networks' unveiling. Several firms, including Thesys technologies (a subsidiary of Tradeworx) and McKay Brothers, are planning microwave solutions (which bounce microwave transmissions between towers) in a still‐straighter path between Chicago and New York. McKay claims to have a one‐way latency of around 4.5 milliseconds, and Thesys expects a latency of 4.25 milliseconds. These latencies are achievable because microwaves tend to move faster through the air than photons move through glass (as with fiber optic cables).6

There is some light (no pun intended) at the end of the tunnel, however. The arms race to zero appears to be nearing an end. The potentially faster microwave solution may not be as reliable as a closely monitored, dedicated fiber optic line, due to weather and other factors. Furthermore, the amount of information that can be transmitted via microwave is also quite small.

The state of the art connection between London and New York for some years was Global Crossing's AC‐1 transatlantic cable, with one‐way transmissions with approximately 65 milliseconds of latency. However, Hibernia Atlantic spent some \$300 million laying a transatlantic fiber optic cable that allows for one‐way latencies of 59.6 milliseconds. This translates into a latency reduction of approximately five milliseconds.7 The line was activated in May 2012, and reportedly was sold out far in advance to a handful of trading customers.

#### Building Order Books

The data that a given exchange broadcasts to traders is actually in the form of messages (new orders, cancellations, and trades), not in the form of an order book. It is the job of the quant to build an order book from these messages. This turns out to be a very challenging task. In order to have an accurate order book at a given point in the day, every message from the beginning of the day onward must be processed. There can be no dropped messages. Furthermore, this processing has to be very fast; otherwise, latency is introduced. As we all know, there is a trade‐off between speed and accuracy that is difficult to overcome. And this is no exception. Worse still, there are a number of algorithmic solutions that solve this problem, and none are considered industry standard.

A subtler part of this problem (which relates to our next topic) is time stamping. Each stream of messages from each exchange has its own timestamp. It is crucial to have the sequence of these messages accurately recorded as well. So, not only are we processing the messages themselves, but the timestamps of each message.

#### Consolidating Order Books

For markets that are fragmented (as in the case of U.S. equities), we have multiple streams of messages that need to be aggregated into one consolidated order book. The challenges described above are compounded by the task of combining these multiple information sources correctly. For example, even if we have an accurate order book for two different exchanges on which XYZ is traded, and even if we have the messages correctly ordered for each of these two, there can still be problems. The messages from the second exchange may be presented to us with greater latency than the first, and this must be accounted for when building the consolidated order book. Otherwise, it will appear that things happened in a sequence that is incorrect.

#### Data Bursts

One of the most significant (and somewhat unique) challenges facing someone building a high‐speed trading infrastructure is the fact that messages do not arrive at an even rate throughout the day. This is an extremely sneaky problem that bears some discussion.

The pioneers of the mathematics of traffic engineering were involved in engineering telephone networks. They assumed that rates of consumption of bandwidth would be basically stationary within some reasonable interval, like minutes or seconds. There is a concept in mathematics called the Poisson‐distribution (after a French statistician who introduced it in the nineteenth century) that is tailor‐made for this application. This assumption made sense in engineering phone networks, where average rates could be assumed to be stationary over some intervals. For example, Mother's Day has an incredibly high average call rate, but basically you could assume that call arrival rate was constant and calls arrived independently over the busiest hour on Mother's Day.

However, in trading, the very action of one person trading causes another to take action (for example in the placement or cancelation of orders). This results in a positive feedback loop, and there is absolutely no stationarity in the message rates inside anything that a normal person would consider a reasonable period. To further elaborate, the average of the message arrival rate in the one‐second time frame tells you very little about the arrival rate in the one‐millisecond time frame.

Let's return to the example of EBAY. Exhibit 14.11 shows the number of messages at various percentiles, for various slices of time from one second down to 1 millisecond.

What is most interesting about this table is that it shows directly and empirically how nonstationary the message rates are. At each percentile, you would expect to see one‐tenth the number of messages in one row as

|                  | 50th<br>Percentile | 99th<br>Percentile | 99.9th<br>Percentile | 99.99th<br>Percentile | 99.999th<br>Percentile |
|------------------|--------------------|--------------------|----------------------|-----------------------|------------------------|
| 1 second         | 13                 | 259                | 546                  | 1,755                 | 4,179                  |
| 100 milliseconds | 0                  | 13                 | 84                   | 863                   | 1,306                  |
| 10 milliseconds  | 0                  | 1                  | 7                    | 269                   | 557                    |
| 1 millisecond    | 0                  | 0                  | 1                    | 56                    | 106                    |

Exhibit 14.11 Breakdown of Messages at Various Intervals and Percentiles for EBAY on July 20, 2012

in the preceding row. For example, if there are 259 messages per 1 second at the 99th percentile, you would expect to see about 26 messages per 100 milliseconds (because there are 10 separate 100 millisecond periods in each second). Instead, we see that there are 13 messages at the 99th percentile per 100 milliseconds. By contrast, when we get out to the 99.99th percentile, the situation is dramatically different. There are 1,755 messages per second in the top 0.01 percent of seconds in the trading day. Thus, you might expect to see 176 or so messages per 100 milliseconds at the top 0.01 percent of millisecond periods during the same trading day. Instead, we see 863, about five times the expectation.

Comparing 1‐second intervals to 1‐millisecond intervals is even more interesting. At the 99.99th percentile, you would expect about 2 messages per 1 millisecond, given the number of messages at the 99.99th percentile per 1 second (1,755 divided by 1,000—the number of milliseconds in a single second—is 1.755). In reality, we find that the number of messages per 1 millisecond at the 99.99th percentile is 56! Even comparing message rates per 10 milliseconds to message rates per 1 millisecond yields surprising results (around double the number of messages are transmitted at the 1 millisecond level versus what you would expect from looking at the 10 millisecond level.

One could argue that it is silly to worry about the 99.99th percentile. Events in this realm happen far less than 1 percent of the time. But consider that there are about 23.4 million milliseconds in a 6 ½ hour trading day. This means that there are 234,000 observations that occur with 1 percent probability during the day. So a system that is designed to capture "only" 99 percent of all messages transmitted during the day may miss the busiest 234,000 milliseconds worth of data. This should self‐evidently be a massive problem for any algorithmic system. There are 2,340 millisecond intervals that constitute the busiest 0.01 percent of observations in a single trading day. This is itself a big number. Whereas the tails of the distribution of messages per 10‐seconds are relatively well‐behaved, the tails of the distribution of messages per millisecond are incredibly badly behaved.

Why is this a problem? Because if you are trying to engineer a system to be responsive at a given timescale, you need to be able to handle arrival rates at around the same timescale. So if you only care about millisecond response times, then you can be satisfied with understanding and handling the message rates at the one‐millisecond level. But if you care (as many high‐frequency traders do) about tenths of a millisecond, you must be able to handle message arrival rates at the level of tenths of a millisecond. Here the variability is of course even greater. Compounding the problem is the fact that there is a seasonality of busyness within each day. On a typical day, the period just before the close is the busiest, and the period just after the open is the second busiest. Otherwise things are fairly quiet. This means that on a typical day you have to handle outlier amounts of data simultaneously across all tickers. And during other busy times (e.g., after a Federal Reserve rate announcement or some other big news), the same data‐burst problem reoccurs.

A quant system that is able to handle these problems must deal with potential problems in any number of areas: the connection between the HFT's server and the exchange's matching engine (known as a *cross‐connect*), the network switch, connections between the colocation facilities of the various exchanges, and the data feed handler for each exchange—just to name a few. Moreover, bursts of data that might have been handled individually could become overwhelming as one aggregates order books from multiple exchanges to re-create a real‐time consolidated book.

And if this wasn't enough of a challenge already, the models used by HFTs to process the data and come up with trading signals add latency. It takes time to decide exactly what to do. The preferred approach of implementing trading signals is to split them up across multiple servers. But this in itself is a further challenge. There are issues with hardware, software, and network engineering. How do you distribute consolidated data in a timely manner to various servers, for example, when each server is charged with computing and running the actual trading strategy? Distributing data to various servers adds varying amounts of latency. The better one handles these kinds of issues, the less latency introduced during data bursts. The worse one handles them, the more latency there is during times of high‐message traffic.

#### Signal Construction

Once data have been properly handled and distributed, a reaction to that data needs to be properly constructed and implemented. Broadly speaking, we can define two categories of strategies that can be implemented within such a system: execution algorithms (covered in Chapter 7) and an HFT strategy. These strategies can be widely varying in the degree of their complexity. For example, an HFT strategy attempting to control for risk factors continuously throughout the day would obviously be more complex than an alpha model with an intraday time horizon but no risk management. Even alpha models with intraday horizons can vary tremendously in their complexity. (We detail the kinds of strategies that HFTs employ in the next chapter.) But even if we take two exactly identical HFT strategies, there are (in most cases) multiple algorithms that can be used to calculate the signals. And not all of these algorithms are equally fast.

To give an example, index arbitrage is a widely known HFT strategy. This strategy involves trading the value of the SPY ETF against the values of the 500 stocks that constitute it. (Note that index arbitrage can be traded on any index versus its constituents, and we use the SPY simply as an illustrative and well‐known example.) If you know that the S&P 500 index consists of 500 stocks and 500 weights, you should be able to compute a bottom‐up estimate of the value of the S&P index. If, however, you find that the actual value of the SPY ETF, after accounting for expense ratios and other similar structural differences between the ETF and a basket of stocks, is trading at a different value, then theoretically free money is to be had by virtue of buying whichever side is undervalued and selling short whichever side is overvalued. As you might imagine, there's a lot of competition for free money. This means that you have to make decisions about what is overvalued or undervalued very quickly. As simple as it sounds, comparing the SPY ETF to the basket of stocks that compose it at very high speeds is not trivial. There are a number of algorithmic solutions for this, and they don't all do the computations equally quickly.

As a sidebar, it is this kind of strategy that you often see in HFT. Very simple ideas, very simple calculations, but that require astoundingly fast infrastructure to capture. It is therefore very ironic when we hear the press talk about "sophisticated, complicated algorithms." The difficulty is not in understanding what's being done, but in doing it very quickly.

#### Risk Checks

The last step before sending an order to the marketplace (in some markets, such as U.S. equities) is submitting the order to what's known as a regulatory risk check. Regulators (under the Market Access Rule) have indicated that broker‐dealers (who give trading firms access to the marketplace) are responsible for ensuring that each trade is (a) within the means of the trader, (b) not in error, and (c) compliant with regulatory requirements. They also mandate that the risk‐checking software should be in the full and exclusive control of the broker‐dealer whose customer is trying to make a trade. This rule was adopted in July 2011 as a response to criticism of HFT and concerns over the stability of a marketplace without such rules. Elaborating a bit further on the kinds of things that need to be checked before an order is sent to market:

- Does the trader's buying power allow for the order(s) in question to be made?
- Does the number of open orders seem to be valid, or does it appear that the trader has a bug that leads to an excessive number of open orders?
- Does this individual trade seem too large to be intentional?

Prior to the adoption of the Market Access Rule, most broker‐dealers operated in accordance with the rule anyway. But a small number of very‐ high‐volume trading firms operated differently. These firms engaged in what is called *naked access*. This meant that customers of the broker‐dealer were allowed direct access to the market if the broker was ultimately comfortable enough (after performing many checks of its own) with the client's risk‐checking technology. Why does this matter? Because a risk check provided by the broker generally resides on a broker's server. For a trade to go through a risk check, it must be transmitted by the customer to the broker before going out to the market.

This added *hop* (in network engineering terms) adds more latency for two reasons. First, there is another connection between servers that must take place (between the customer's trading server and the broker's risk‐ checking server). Second, the broker's risk‐checking software is generally going to be inferior to that designed by a speed‐sensitive trader. This could be for any number of reasons, including the presence of superior talent at the best HFTs or quant trading firms versus the typical brokerage firm, or simply different goals. The broker generally cares a lot more about issues like scalability than being hyper‐fast. By contrast, speed‐obsessed HFT engineers (who are willing to tackle all the issues above) want the *tick‐to‐ trade* total latency to be as little as 10 microseconds (0.1 milliseconds). They are scarcely going to be satisfied with an added risk‐check latency of 50 microseconds.

Thus, some HFT firms opted to send their trades directly to the exchange after utilizing their own in‐house risk checks. Not many brokers were willing to accept an arrangement like that because the broker ultimately bears responsibility if there is a problem with the customer's risk check. However, some brokers made a business of providing naked access to HFTs, and these firms definitely enjoyed a speed advantage for several years. With the Market Access Rule, the SEC banned this practice, and now one must use a broker‐dealer's risk check. This drove some of the largest HFTs to build out their own broker‐dealer units so that they could continue to use their own risk checks with additional regulatory overhead. It also drove a new arms race to create the fastest commercial risk checks. As of today's writing, there are roughly three top‐tier solutions; the others lag well behind. Solving the risk check problem remains an area where some HFTs (and, primarily, their service providers) focus on reducing latency.

# Summary

In this chapter, we have elaborated on the reasons that high speed (or low latency) trading matters, as well as the sources of latency. Depending on the type of trade or trading strategy being implemented, there are differing reasons for the emphasis on speed. And, while this has received a significant amount of negative attention in the press, it is absolutely no different from the situation in any other industry. If an advantage can be developed within the rules of a competitive game, then the most competitive players will seek to develop that edge. But, as is the case for quant trading in general, there is clearly a double standard when it comes to HFT and low-latency trading. People seem to be really angry that HFTs, having solved the incredibly difficult problems enumerated above, have achieved a (completely legal, ethical, and fair) competitive advantage over other traders.

The irony, as we will discuss further in Chapter 16, is that low‐latency trading is like any other enterprise in a reasonably free‐enterprise system: Taking risk does not imply that one will succeed. Countless HFTs have invested enormous sums of time and money into infrastructure, only to find that they lack the ability simply to generate acceptable returns. Many more HFTs either cannot afford the huge investment of resources, or simply lack the expertise, to create their own infrastructure. A typical *build versus buy* decision is made, and some firms end up utilizing commercial vendors for many or all parts of this infrastructure. Some firms advertise themselves as "HFT‐in‐a‐Box" solutions, which allow a strategist with a good idea to implement her strategy without having to build all of these other elements. Unfortunately, few of these vendors deliver what is advertised (just as is true in basically any industry). The result is that when the opportunities to add value are the most plentiful (when trading activity is at its most frenzied level), relatively few vendors are able to deliver true low-latency solutions. To quote Mike Beller, CTO of Tradeworx, who helped me with this chapter: "Be suspicious of anyone who quotes averages, or even averages and standard deviations. Responsible people engineer for the 99th percentile."

Even firms that have the resources and that have been successful are subject to substantial risks. While detractors of HFT have pointed to the near‐death experience of Knight Capital in 2012 as evidence that HFTs cause instability in the markets, the reality is extremely different: Knight made a change to its software that introduced a bug. It was a mistake of its own doing. And who suffered? Knight. It nearly went out of business and had to secure emergency funding to stay afloat, at the expense of a large portion of the value of its business. While it's sad for Knight and those who own their stock, it is exactly fair. Knight made a mistake, and Knight paid the price. No mom and pop investors, no pensioners, no market systems were harmed. And all of this is in pursuit of what amounts to a \$0.001 per share profit expectation.

This point is perhaps the most important to remember. A tenth of a penny per share is the expected profit margin of a *successful* U.S. equity high‐frequency trader. In exchange for this, these traders take on the risks associated with the capital and time expenditures of competing in a hypercompetitive space. For traders who are expecting to hold positions for a year and make 25 percent or more on that trade, HFTs add liquidity. That they might make \$0.001 per share to provide that liquidity is both inconsequential and totally fair. We now turn to the kinds of strategies that HFTs employ.

# Notes

- 1. Christopher Steiner, "Wall Street's Speed War," *Forbes*, September 27, 2010.
- 2. All message traffic statistics in this section are courtesy of Tradeworx, Inc. proprietary research, September 2012.
- 3. In case you were wondering *why* the ES futures tend to lead SPY ETFs, the reason is primarily that the ES futures are where the largest dollar volumes exist. This is probably for two reasons. The first is that ES futures have been around a lot longer than SPY ETFs, so some of this is just incumbency, both because of habit (once an instrument becomes the instrument of choice for a given exposure, it tends to retain that title with a large amount of inertia on its side), and because it is a pain in the neck to change one's infrastructure to trade stocks (ETFs are listed and traded the same way as stocks, for all intents and purposes) when one is already trading futures. Second, the futures markets do offer a couple of structural advantages over ETFs. Profits on many futures contracts are subject to less onerous taxes than profits on equity or ETF trades. Also, futures contracts offer a fairly substantial amount of leverage, so whether a trader wants to make a big bet or simply doesn't want to spend a lot of money to put on that bet, futures can be an efficient way to implement the trade. However, the gap has been narrowing somewhat, driven by the migration of retail investors away from actively managed mutual funds into passive ETFs, and partially by virtue of the fact that, in many ways, the ETFs are often cheaper (in aggregate) to transact.
## **Section 1: Introduction and Environment Setup**

In this section, you will be introduced to algorithmic trading and setting up the environment required to perform tasks throughout the book. You will learn the key components of trading and the questions you need to ask before embarking on a robot trading project.

This section comprises the following chapter:

Chapter 1, *Algorithmic Trading Fundamentals*

## **Algorithmic Trading Fundamentals**

Algorithmic trading, or automated trading, works with a program that contains a set of instructions for trading purposes. Compared to a human trader, this trade can generate profits and losses at a higher speed. In this chapter, this will be your first time being exposed to trading automation. We will walk you through the different steps to implement your first trading robot. You will learn the trading world and the technical trading components behind it. We will also go into detail about the tools that you will use and, by the end of this chapter, you will be capable of coding your first native trading strategy in Python. We will cover the following topics in this chapter:

- Why are we trading?
- Introducing algorithm trading and automation
- What the main trading components are
- Setting up your first programming environment
- Implementing your first native strategy

### **Why are we trading?**

From the Roman era through to the present day, trading is an inherent part of humankind. Buying raw materials when the price is low to resell it when the price is high has been a part of many cultures. In ancient Rome, the rich Romans used the *Roman Forum* to exchange currencies, bonds, and investments. In the 14th century, traders negotiated government debts in Venice. The earliest form of the stock exchange was created in Antwerp, Belgium, in 1531. Traders used to meet regularly to exchange promissory notes and bonds. The conquests of new worlds entailed a high cost, but also a good return. The Dutch East India Company in 1602 opened their capital for investors to participate in this costly project with a high potential return. During the same time period, a well-known tulip was sold everywhere in the world, creating a profitable market for investors and sellers. A future contract was created for this reason, since many people speculated regarding the price of this flower.

A hundred years later, a French expedition to Louisiana was also attracting many investors, creating the dream of making a lot of money. The Mississippi Company was created to handle all the investments based on potential wealth in Louisiana. Many other investment opportunities arose across the centuries, including the British railroad and the conquest of Latin America.

All these events had a common root: wealthy people willing to make more money. If we want to answer the question *Why are we trading?*, the answer is to potentially make more money. However, all the previous historical examples ended pretty badly. Investments turned out to be bad investments or, most of the time, the value was over-estimated and traders ended up losing their money. This is actually a good lesson for the readers of this book. Even if trading can sound a profitable business, always keep in mind the ephemeral part of profitability (it can work sometimes, but not always) and also taking into account the inherent risk that goes with investment.

## **Basic concepts regarding the modern trading setup**

This section will cover the basics of trading and what drives market prices, as well as supply and demand.

As we touched upon in the previous section, trading has been around since the beginning of time, when people wanted to exchange goods between one another and make profits while doing so. Modern markets are still driven by basic economic principles of supply and demand. When demand outweighs supply, prices of a commodity or service are likely to rise higher to reflect the relative shortage of the commodity or service in relation to the demand for it. Conversely, if the market is flooded with a lot of sellers for a particular product, prices are likely to drop. Hence, the market is always trying to reflect the equilibrium price between available supply and demand for a particular product. We will see later how this is the fundamental driver of price discovery in today's markets. With the evolution of modern markets and available technology, price discovery becomes increasingly efficient.

Intuitively, you may draw a parallel with the fact that with the advances in online retail businesses, prices of products have become increasingly efficient across all sellers, and the best offers are always the ones that customers are buying because the information (price discovery) is so easily accessible. The same is true for modern trading. With advances in technology and regulations, more and more market participants have access to complete market data that makes price discovery much more efficient than in the past. Of course, the speed at which participants receive information, the speed at which they react, the granularity of the data that they can receive and handle, and the sophistication with which each participant draws trading insights from the data they receive, is where the competition lies in modern trading, and we will go over these in the subsequent sections. But first, let's introduce some basic concepts regarding the modern trading setup.

### **Market sectors**

In this section, we will briefly introduce the concepts of what different types of market sectors are and how they differ from the concept of asset classes.

Market sectors are the different kinds of underlying products that can be traded. The most popular market sectors are commodities (metals, agricultural produce), energy (oil, gas), equities (stocks of different companies), interest rate bonds (coupons you get in exchange for debt, which accrues interest, hence the name), and foreign exchange (cash exchange rates between currencies for different countries):

![](_page_5_Figure_0.jpeg)

### **Asset classes**

Asset classes are the different kinds of actual vehicles that are available for trading at different exchanges. For example, cash interest rate bonds, cash foreign exchange, and cash stock shares are what we described in the previous section, but we can have financial instruments that are derivatives of these underlying products. Derivatives are instruments that are built on top of other instruments and have some additional constraints, which we will explore in this section. The two most popular derivatives are futures and options, and are heavily traded across all derivatives electronic exchanges.

We can have future contracts pertaining to underlying commodities, energy, equities, interest rate bonds, and foreign exchanges that are tied to the prices of the underlying instruments, but have different characteristics and rules. A simple way to think of a future contract is that it is a contract between a buyer and a seller in which the seller promises to sell a certain amount of the underlying product at a certain date in the future (also known as the expiry date), and where the buyer agrees to accept the agreed-upon amount at the specific date at the specific price.

For example, a producer of butter might want to protect themselves from a potential future spike in the price of milk, on which the production costs of butter directly depend, in which case, the butter producer can enter into an agreement with a milk producer to provide them with enough milk in the future at a certain price. Conversely, a milk producer may worry about possible buyers of milk in the future and may want to reduce the risk by making an agreement with butter producers to buy at least a certain amount of milk in the future at a certain price, since milk is perishable and a lack of supply would mean a total loss for a milk producer. This is a very simple example of a future contract trade; modern future contracts are much more complex than this.

Similar to future contracts, we can have options contracts for underlying commodities, energy, equities, interest rate bonds, and foreign exchanges that are tied to the prices of the underlying instruments, but have different characteristics and rules. The difference in an options contract compared to a futures contract is that the buyer and seller of an options contract have the option of refusing to buy or sell at the specific amount, at the specific date, and at the specific price. To safeguard both counterparties involved in an options trade, we have the concept of a premium, which is the minimum amount of money that has been paid upfront to buy/sell an options contract.

A call option, or the right to buy, but not an obligation to buy at expiration, makes money if the price of the underlying product increases prior to expiration because now, such a party can exercise their option at expiration and buy the underlying product at a price lower than the current market price. Conversely, if the price of the underlying product goes down prior to expiration, such a party now has the option of backing out of exercising their option and thus, only losing the premium that they paid for. Put options are analogous, but they give the holder of a put contract the right to sell, but not an obligation to sell, at expiration.

We will not delve too deeply into different financial products and derivatives since that is not the focus of this book, but this brief introduction was meant to introduce the idea that there are a lot of different tradeable financial products out there and that they vary significantly in terms of their rules and complexity.

### **Basics of what a modern trading exchange looks like**

Since this book is primarily designed to introduce what modern algorithmic trading looks like, we will focus on trying to understand how a modern electronic trading exchange appears. Gone are the days of people yelling at one another in the trading pits and making hand signals to convey their intentions to buy and sell products at certain prices. These remain amusing ideas for movies, but modern trading looks significantly different.

Today, most of the trading is done electronically through different software applications. Market data feed handlers process and understand market data disseminated by the trading exchanges to reflect the true state of the limit book and market prices (bids and offers). The market data is published in a specific market data protocol previously agreed upon by the exchange and the market participants (FIX/FAST, ITCH, and HSVF). Then, the same software applications can relay that information back to humans or make decisions themselves algorithmically. Those decisions are then again communicated to the exchange by a similar software application (order entry gateways) that informs the exchange of our interest in a specific product and our interest in buying or selling that product at specific prices by sending specific order types (GTDs, GTCs, IOCs, and so on). This involves understanding and communicating with the exchange in an exchange order entry protocol previously agreed upon by the exchange and participants at the exchange (FIX, OMEX, OUCH).

After a match takes place against available market participants, that match is conveyed back to the software application again via the order entry gateways and relayed back to the trading algorithm or the humans, thereby completing a transaction, often wholly electronically. The speed of this round trip varies a lot based on the market, the participant, and the algorithms themselves. This can be as low as under 10 microseconds all the way up to seconds, but we will discuss this in greater detail later.

The following diagram is a descriptive view of the flow of information from an electronic trading exchange to the market participants involved, and the flow of information back to the exchange:

![](_page_9_Figure_1.jpeg)

As shown in the preceding diagram, the trading exchange maintains a book of client buy orders (bids) and client ask orders (asks), and publishes market data using market data protocols to provide the state of the book to all market participants. Market data feed handlers on the client side decode the incoming market data feed and build a limit order book on their side to reflect the state of the order book as the exchange sees it. This is then propagated through the client's trading algorithm and then goes through the order entry gateway to generate an outgoing order flow. The outgoing order flow is communicated to the exchange via order entry protocols. This, in

turn, will generate further market data flow, and so the trading information cycle continues.

## **Understanding algorithmic trading concepts**

We introduced a lot of new concepts in the previous section, such as exchange order books (consisting of different kinds of orders sent by market participants), exchange matching algorithms, exchange market data protocols, and exchange order entry protocols. Let's formally discuss these in greater detail here.

### **Exchange order book**

The exchange order book maintains all incoming buy and sell orders placed by clients. It tracks all attributes for incoming orders—prices, number of contracts/shares, order types, and participant identification. Buy orders (or bids) are sorted from the highest price (best price) to the lowest price (worst price). Bids with higher prices have a higher priority as far as matching is concerned. Bids at the same price are prioritized depending on the matching algorithm. The simplest FIFO (First In First Out) algorithm uses the intuitive rule of prioritizing orders at the same price in the order in which they came in. This will be important later on when we discuss how sophisticated trading algorithms use speed and intelligence to get higher priorities for their orders and how this impacts profitability. Sell orders (or asks) are sorted from the lowest price (best price) to the highest price (worst price). Again, as regards asks at the same price, the matching prioritization method depends on the matching algorithm adopted by the exchange for the specific product, which we will expand upon in greater detail in the next section. Market participants are allowed to place new orders, cancel existing orders, or modify order attributes such as price and the number of shares/contracts, and the exchange generates public market data in response to each order sent by participants. Using the market data distributed by the exchange, market participants can get an accurate idea of what the order book at the exchange looks like (depending on what information the exchange chooses to hide, but we ignore that nuance for now).

### **Exchange matching algorithm**

When incoming bids are at or above the best (lowest price) ask orders, then a match occurs. Conversely, when incoming asks are at or below the best (highest price) bid orders, then a match occurs. Incoming aggressive orders continue to match against existing passive orders in the book until one of these two conditions is met. Either the new aggressive order is fully matched, or the other possibility is that the remaining orders on the opposite side have prices worse than the incoming order price and, hence, the match cannot occur. This is because of the fundamental rule that an order cannot be matched at a price worse than the limit price it was entered at. Now, as far as orders at the same price level are concerned, the order of matching is dictated by what matching algorithm rules the exchange adopts.

### **FIFO matching**

We briefly described the FIFO algorithm previously, but let's expand on it by showing an example. Assume the following state of an order book when the exchange bid orders A, B, and C were entered at price 10.00 in that order in time. So, at the same price, order A has a higher priority than order B, which has a higher priority than order C. Bid order D is at a worse price, 9.00. Similarly, on the ask side, order X was entered at price 11.00 before order Y, also at price 11.00. Hence, order X has a higher priority than order Y, and then ask order Z was entered at a worse price, 12.00:

| BIDS                   | ASKS                    |
|------------------------|-------------------------|
| Order A: Buy 1 @ 10.00 | Order X: Sell 1 @ 11.00 |
| Order B: Buy 2 @ 10.00 | Order Y: Sell 2 @ 11.00 |
| Order C: Buy 3 @ 10.00 | Order Z: Sell 2 @ 12.00 |
| Order D: Buy 1 @ 9.00  |                         |

Assume an incoming sell order K for 4 shares @ 10.00 would match against order A for 1 share, order B for 2 shares, and order C for 1 share, in that order, under FIFO matching. At the end of the matching, order C would still have the remaining size of 2 shares at price 10.00 and will have the highest priority.

### **Pro-rata matching**

Pro-rata matching comes in a variety of flavors and is usually implemented in slightly different ways. For the scope of this book, we provide some intuition behind this matching algorithm and provide a hypothetical matching scenario.

The underlying intuition between pro-rata matching is that it favors larger orders over smaller orders at the same price and ignores the time at which the orders were entered. This changes the market's microstructure quite a bit, and the participants are favored to enter larger orders to gain priority instead of entering orders as fast as possible:

| BIDS                     | ASKS                      |
|--------------------------|---------------------------|
| Order A: Buy 100 @ 10.00 | Order X: Sell 100 @ 11.00 |
| Order B: Buy 200 @ 10.00 | Order Y: Sell 200 @ 11.00 |
| Order C: Buy 700 @ 10.00 | Order Z: Sell 200 @ 12.00 |
| Order D: Buy 100 @ 9.00  |                           |

Consider a market state as shown earlier. For the sake of this example, the hypothetical order sizes have been raised by a factor of 100. Here, bid orders A, B, and C are at the same price, 10.00. However, when an incoming sell order of size 100 comes in for price 10.00, order C gets a fill for 70 contracts, order B gets a fill for 20 contracts, and order A gets a fill for 10 contracts, proportional to how big they are at that level. This is an overly simplified example that excludes complications related to fractional match sizes and breaking ties between orders with the same size, and so on. Also, some exchanges have a mix of pro-rata and FIFO, where part of the incoming aggressor matches using pro-rata, and part matches in FIFO order. But this should serve as a good basic understanding of how different prorata matching is compared to FIFO matching. A detailed examination of pro-rata matching and its impact is beyond the scope of this book, so we exclude it.

### **Limit order book**

A limit order book is very similar in spirit to the exchange order book. The only difference is that this is built by the market participants based on the market data that is being sent out by the exchange in response to market participants sending orders to it. The limit order book is a central concept in all algorithmic trading, and one often found in all other forms of trading as well. The purpose is to collect and arrange bids and offers in a meaningful way to gain insight into the market participants present at any particular time, as well as gain insight regarding what the equilibrium prices are. We will revisit these in the next chapter when we dig deeper into technical analysis. Depending on what information the exchange decides to make available to all market participants via public market data, the limit order book that the client builds can be slightly different from what the order book at the exchange matching engine looks like.

### **Exchange market data protocols**

Exchange market data protocols are not the focus of this book, so a rigorous treatment of this topic is beyond the scope of this book. These market data protocols are outgoing communication streams from the exchange to all market participants that are well-documented for new participants to build their software applications to subscribe, receive, decode, and check for errors and network losses. These are designed with latency, throughput, error tolerance, redundancy, and many other requirements in mind.

### **Market data feed handlers**

Market data feed handlers are software applications that market participants build with a view to interfacing with the specific exchange market data protocol. These are able to subscribe, receive, decode, and check for errors and network losses, and are designed with latency, throughput, error tolerance, redundancy, and many other requirements in mind.

## **Order types**

Most exchanges support a variety of orders that they accept from market participants. We will discuss a few of the most common types in this section.

## **IOC – Immediate Or Cancel**

These orders never get added to the book. They either match against existing resting orders to a maximum of the IOC order size, or the rest of the incoming order gets canceled. If no resting order is available at a price that the IOC can match against, then the IOC is canceled in its entirety. IOC orders have the benefit of not resting in the book post matching and causing additional complexity with order management in trading algorithms.

## **GTD – Good Till Day**

These orders get added to the book. If they match fully against existing resting orders in the book, then they don't get added, otherwise the remaining quantity on the order (which can be the entire original quantity if there's no partial match) gets added to the book and sits as resting orders that the incoming aggressors can match against. The benefits of GTD orders are that they can take advantage of FIFO matching algorithms by having better priorities than orders that just showed up in the book, but require more complex order management in trading algorithms.

# **Stop orders**

Stop orders are orders that aren't in the book until a specific price (called the stop price) is traded in the market, at which point they become regular GTD orders at a pre-specified price. These orders are great as exit orders (either to liquidate a losing position or to realize profit on a winning position). We will revisit these orders after we have explained what having a losing or winning position means and what exiting a position means.

### **Exchange order entry protocols**

Exchange order entry protocols are how market participant software applications send order requests (new, cancels, modifies) and how the exchange replies to these requests.

### **Order entry gateway**

Order entry gateways are the market participant client applications that communicate with the exchange matching engine over the order entry protocols. These have to deal with order flow in a reliable manner, sending orders to the exchange, modifying and canceling those orders, and getting notifications when these orders are accepted, canceled, executed, and so on. Oftentimes, market participants run a second variant of order entry gateways that simply receive order-executed notifications to check consistency against the primary order entry gateway order flow. These are called drop-copy gateways.

## **Positions and profit and loss (PnL) management**

Orders that get executed cause market participants to have positions in the instrument that they got executed, for the amount the order executed, and at the price of the execution (limit orders can match at better prices than they were entered for, but not worse). A buy side execution is called having a long position, while a sell side execution is called having a short position. When we have no position at all, this is referred to as being flat. Long positions make money when market prices are higher than the price of the position, and lose money when market prices are lower than the price of the position. Short positions, conversely, make money when market prices go down from the price of the position and lose money when market prices go up from the price of the position, hence, the well-known ideas of buy low, sell high, and buy high, sell higher, and so on.

Multiple buy executions, or multiple sell executions for different amounts and prices, cause the overall position price to be the volume weighted average of the execution prices and quantities. This is called the **Volume Weighted Average Price** (**VWAP**) of the position. Open positions are marked to market to get a sense of what the unrealized **Profit and Loss** (**PnL**) of the position is. This means that current market prices are compared to the price of the position; a long position where market prices have gone up is considered unrealized profit, and the opposite is considered unrealized loss. Similar terms apply to short positions. Profit or loss is realized when an open position is closed, meaning you sell to close a long position and you buy to close a short position. At that point, the PnL is given the term *realized PnL*. The total PnL at any point is the total of the realized PnLs so far and the unrealized PnLs for open positions at the market price.

## **From intuition to algorithmic trading**

Here, we will discuss how trading ideas are born and how they are turned into algorithmic trading strategies. Fundamentally, all trading ideas are driven by human intuition to a large extent. If markets have been moving up/down all the time, you might intuitively think that it will continue to move in the same direction, which is the fundamental idea behind trendfollowing strategies. Conversely, you might argue that if prices have moved up/down a lot, it is mispriced and likely to move in the opposite direction, which is the fundamental idea behind mean reversion strategies. Intuitively, you may also reason that instruments that are very similar to one another, or loosely dependent on one another, will move together, which is the idea behind correlation-based trading or pairs trading. Since every market participant has their own view of the market, the final market prices are a reflection of the majority of market participants. If your views are aligned with the majority of the market participants, then that particular strategy is profitable in that particular instance. Of course, no trading idea can be right all the time, and whether a strategy is profitable or not depends on how often the idea is correct versus how often it is not correct.

## **Why do we need to automate trading?**

Historically, human traders implemented such rule-based trading to manually enter orders, take positions, and make profits or losses through the day. Over time, with advances in technology, they've moved from yelling in the pits to get orders executed with other pit traders, to calling up a broker and entering orders over the telephone, to having GUI applications that allow entering orders through point and click interfaces.

Such manual approaches have a lot of drawbacks – humans are slow to react to markets so they miss information or are slow to react to new information, they can't scale well or focus on multiple things at a time, humans are prone to making mistakes, they get distracted, and they feel a fear of losing money and a joy of making money. All of these drawbacks cause them to deviate from a planned trading strategy, severely limiting the profitability of the trading strategy.

Computers are extremely good at rule-based repetitive tasks. When designed and programmed correctly, they can execute instructions and algorithms extremely quickly, and can be scaled and deployed across a lot of instruments seamlessly. They are extremely fast at reacting to market data, and they don't get distracted or make mistakes (unless they were programmed incorrectly, which is a software bug and not a drawback of computers themselves). They don't have emotions, so don't deviate from what they are programmed to do. All of these advantages make computerized automated trading systems extremely profitable when done right, which is where algorithmic trading starts.

### **Evolution of algorithmic trading – from rule-based to AI**

Let's take a simple example of a trend-following strategy and see how that has evolved from a manual approach all the way to a fully automated algorithmic trading strategy. Historically, human traders are used to having simple charting applications that can be used to detect when trends are starting or continuing. These can be simple rules, such as if a share rises 5% every day for a week, then it is something we should buy and hold (put on a long position), or if a share price has dropped 10% in 2 hours, then that is something we should sell short and wait for it to drop further. This would be a classic manual trading strategy in the past. As we discussed previously, computers are very good at following repetitive rule-based algorithms. Simpler rules are easier to program and require less development time, but computer software applications are only limited by the complexity that the software developer programming the computer can handle. At the end of this chapter, we will deal with a realistic trading strategy written in Python, but for now, we will continue to introduce all the ideas and concepts required prior to that.

Here is some pseudo code that implements our trend-following, human intuition trading idea. This can then be translated into whatever language of our choosing based on our application's needs.

We can use trend-following, which means, buying/selling when the price changes by 10% in 2 hours. This variable tracks our current position in the market:

Current\_position\_ = 0;

This is the expected profit threshold for our positions. If a position is more profitable than this threshold, we flatten the position and the unrealized profit to realized profit:

PROFIT\_EXIT\_PRICE\_PERCENT = 0.2;

This is the maximum loss threshold for our positions. If a position is losing more than this threshold, we flatten the position and convert the unrealized loss to realized loss. Why would we close a position if it's losing money? The idea is simply to not lose all of our money on one bad position, but rather cut our losses early so that we have capital to continue trading. More on this when we dive into risk management practices in more detail. For now, we define a parameter that is the maximum allowed loss for a position in terms of the price change from the entry price for our position:

LOSS\_EXIT\_PRICE\_PERCENT = -0.1;

Note that in the thresholds we saw, we expect to make more money on our winning/profitable positions than we expect to lose on our losing positions. This is not always symmetrical, but we will address the distributions of winning and losing positions when we look into these trading strategies in greater detail later in this book. This is a method/callback that is invoked every time the market prices change. We need to check whether our signal causes an entry and whether one of our open positions needs to be closed for PnL reasons:

```
def OnMarketPriceChange( current_price, current_time ):
```

First, check whether we are flat and prices have moved up more than 10%. This is our entry signal to go long, so we will send a buy order and update our position. Technically, we should not update our position until the exchange confirms that our order matched, but for the sake of simplicity in this first-pass pseudo code, we ignore that complexity and address it later:

```
If Current_position_ == 0 AND ( current_price - price_two_hours_ago ) / current_price >; 10%:
 SendBuyOrderAtCurrentPrice();
 Current_position_ = Current_position_ + 1;
```

Now, check whether we are flat and prices have moved down more than 10%. This is our entry signal to go short, so we will send a sell order and update our position:

```
Else If Current_position_ == 0 AND ( current_price - price_two_hours_ago ) / current_price < -10%:
 SendSellOrderAtCurrentPrice();
 Current_position_ = Current_position_ - 1;
```

If we are currently long, and market prices have moved in a favorable direction, check whether this position's profitability exceeds predetermined thresholds. In that case, we will send a sell order to flatten our position and convert our unrealized profit to realized profit:

```
If Current_position_ >; 0 AND current_price - position_price >; PROFIT_EXIT_PRICE_PERCENT:
 SendSellOrderAtCurrentPrice();
 Current_position_ = Current_position_ - 1;
```

If we are currently long, and market prices have moved against us, check whether this position loss exceeds predetermined thresholds. In that case, we will send a sell order to *flatten* our position and convert our unrealized loss to realized loss.

```
Else If Current_position_ >; 0 AND current_price - position_price < LOSS_EXIT_PRICE_PERCENT::
 SendSellOrderAtCurrentPrice();
 Current_position_ = Current_position_ - 1;
```

If we are currently short, and market prices have moved in a favorable direction, check whether this position profitability exceeds predetermined thresholds. In that case, we will send a buy order to *flatten* our position and convert our unrealized profit to realized profit:

```
Else If Current_position_ < 0 AND position_price - current_price >; PROFIT_EXIT_PRICE_PERCENT:
 SendBuyOrderAtCurrentPrice();
 Current_position_ = Current_position_ - 1;
```

If we are currently short, and market prices have moved against us, check whether this position loss exceeds predetermined thresholds. In that case, we will send a buy order to *flatten* our position and convert our unrealized loss to realized loss:

```
Else If Current_position_ < 0 AND position_price - current_price < LOSS_EXIT_PRICE_PERCENT:
 SendBuyOrderAtCurrentPrice();
 Current_position_ = Current_position_ - 1;
```

## **Components of an algorithmic trading system**

In an earlier section, we provided a top-level view of the entire algorithmic trading setup and many of the different components involved. In practice, a complete algorithmic trading setup is divided into two sections, as shown in the following diagram:

- Core infrastructure deals with exchange-facing market data protocol integration, market data feed handlers, internal market data format normalization, historical data recording, instrument definition recording and dissemination, exchange order entry protocols, exchange order entry gateways, core side risk systems, broker-facing applications, back office reconciliation applications, addressing compliance requirements, and others.
- Algorithmic trading strategy components deal with using normalized market data, building order books, generating signals from incoming market data and order flow information, the aggregation of different signals, efficient execution logic built on top of statistical predictive abilities (alpha), position and PnL management inside the strategies, risk management inside the strategies, backtesting, and historical signal and trading research platforms:

![](_page_33_Figure_0.jpeg)

### **Market data subscription**

These components are responsible for interacting with the feed handler components that publish normalized data. This data can be delivered over a network or locally using a variety of **Inter-Process Communication** (**IPC**) mechanisms from the feed handlers. We do not go into great detail about this here. Low latency delivery and scalability are the major driving design decisions in this regard.

### **Limit order books**

Once the trading strategy gets normalized market data, it uses that data to build and maintain limit order books for each instrument. Depending on the sophistication and complexity of the limit order books, it can be simple enough such that it tells us how many participants there are on each side, or sophisticated enough to track market participant order priorities as well as track our own orders in the limit order book.

## **Signals**

Once limit order books are built, every time they are updated due to new incoming market data information, we build signals using the new information.

Signals are called by various names—signals, indicators, predictors, calculators, features, alpha, and so on—but they all have roughly the same meaning.

A trading signal is a well-defined piece of intelligence that is derived from incoming market data information, limit order books or trade information that allows a trading strategy to get a statistical edge (advantage) vis-à-vis other market participants and, thus, increased profitability. This is one of the areas where a lot of trading teams focus much of their time and energy. The key is to build a lot of signals in order to have an edge over the competition as well as keep adapting existing signals and adding new signals to deal with changing market conditions and market participants. We will revisit this in one of the later chapters, as this will be a large focus of this book.

## **Signal aggregators**

Often, a lot of algorithmic trading systems combine a lot of different kinds of signals in order to gain a bigger edge than individual signals provide. The approach is to essentially combine different signals that have different predictive abilities/advantages under different market conditions. There are many different ways to combine individual signals. You can use classical statistical learning methods to generate linear and non-linear combinations to output classification or regression output values that represent a combination of individual signals. Machine learning is not the focus of this book, so we avoid diving too deep into this topic, but we will revisit it briefly in a later section.

## **Execution logic**

Another key component of algorithmic trading is quickly and efficiently managing orders based on signals in order to gain an edge over the competition. It is important to react to changing market data, changing signal values in a fast but intelligent manner. Oftentimes, speed and sophistication are two competing goals, and good execution logic will try to balance the two objectives in an optimal manner. It is also extremely important to disguise our intentions/intelligence from other market participants so that we get the best executions possible.

Remember that other market competitors can observe what orders are sent to the exchange and assess the potential impact it might have, so this component needs to be intelligent enough to not make it obvious what our trading strategy is doing. Slippage and fees are also very important factors as far as execution logic design is concerned.

Slippage is defined as the difference in the expected price of a trade and the price at which the trade is actually executed. This can happen for predominantly two reasons:

- If the order reaches the exchange later than expected (latency), then it might end up either not executing at all, or executing at a worse price than you might expect.
- If the order is very large such that it executes at multiple prices, then the VWAP of the entire execution may be significantly different from the market price observed when the order was sent.

Slippage obviously causes losses that might not have been correctly factored in, in addition to difficulty liquidating positions. As the position sizes for trading algorithms scale up, slippage becomes a larger problem.

Fees are another issue with executing orders efficiently. Typically, there are exchange fees and broker fees proportional to the size of the orders and the

total volume traded.

Again, as the position sizes for trading algorithms scale up, trading volumes typically increase and fees increase along with it. Oftentimes, a good trading strategy can end up being non-profitable because it trades too much and accumulates a lot of trading fees. Again, a good execution logic seeks to minimize the fees paid.

### **Position and PnL management**

All algorithmic trading strategies need to track and manage their positions and PnLs effectively. Depending on the actual trading strategy, this can often range in complexity.

For more sophisticated trading strategies, such as pairs trading (curve trading is another similar strategy), you have to track positions and PnLs on multiple instruments and often, these positions and PnLs offset one another and introduce complexity/uncertainty as regards determining true positions and PnLs. We will explore these issues when we talk in detail about these strategies in Chapter 4, *Classical Trading Strategies Driven by Human Intuition*, but for now, we won't discuss this in too much detail.

### **Risk management**

Good risk management is one of the cornerstones of algorithmic trading. Bad risk management practices can turn potential profitable strategies into non-profitable ones. There is an even bigger risk of violating rules and regulations at trading exchanges that can often lead to legal actions and huge penalties. Finally, one of the biggest risks with high-speed automated algorithmic trading is that poorly programmed computer software is prone to bugs and errors. There are many instances of entire firms shutting down due to automated high-speed algorithmic trading systems that run amok. Hence, risk management systems need to be built to be extremely robust, feature rich, and have multiple layers of redundancy. There also needs to be a very high level of testing, stress testing, and strict change management to minimize the possibility of risk systems failing. In Chapter 6, *Managing the Risk of Algorithmic Strategies*, of this book, we will have an entire section dedicated to best risk management practices so as to maximize the profitability of trading strategies as well as avoid common pitfalls resulting in losses or bankruptcy.

### **Backtesting**

When researching an automated trading strategy for expected behavior, a key component in a good algorithmic trading research system is a good backtester. A backtester is used to simulate automated trading strategy behavior and retrieve statistics on expected PnLs, expected risk exposure, and other metrics based on historically recorded market data. The basic idea is to answer the question: given historical data, what kind of performance would a specific trading strategy have? This is built by recording historical market data accurately, having a framework to replay it, having a framework that can accept simulated order flow from potential trading strategies, and mimicking how a trading exchange would match this strategy's order flow in the presence of other market participants as specified in the historical market data. It is also a good place to try out different trading strategies to see what ideas work before deploying them to market.

Building and maintaining a highly accurate backtester is one of the most complicated tasks involved in setting up an algorithmic trading research system. It has to accurately simulate things such as software latencies, network latencies, accurate FIFO priorities for orders, slippage, fees, and, in some cases, also the market impact caused by the order flow for the strategy under consideration (that is, how the other market participants may react in the presence of this strategy's order flow and trading activity). We will revisit backtesting at the end of this chapter and then again in later chapters in this book. Finally, we explain practical issues faced in setting up and calibrating a backtester, their impact on an algorithmic trading strategy, and what approaches best minimize damage caused due to inaccurate backtesting.

## **Why Python?**

Python is the most widely used programming language in the world (onethird of new software development uses this language):

![](_page_43_Figure_2.jpeg)

This language is very simple to learn. Python is an interpreted, high-level programming language with type inference. Unlike C/C++, where you need to focus on memory management and the hardware features of the machine you are using to code, Python takes care of the internal implementation, such as memory management. As a result, this type of language will ease the focus on coding trading algorithms. Python is versatile; it can be used in any domain for any application development. Since Python has been widely used for years, the community of programmers is large enough to get many

critical libraries for your trading strategy, ranging from data analytics, machine learning, data extraction, and runtime to communication; the list of open source libraries is gigantic. Additionally, on the software engineering side, Python includes paradigms used in other languages, such as objectoriented, functional, and dynamic types. The online resources for Python are unlimited, and tons of book will drive you through any domains where you can use Python. Python is not the only language using in trading. We will preferably use Python (or eventually R) to do data analysis and to create trading models. We will use C, C++, or Java in trading for production code. These language will compile source code into executable or byte codes. Consequently, the software will be one hundred times faster than Python or R. Even if these three last languages are faster than Python, we will use all of them to create libraries. We will wrap these libraries to be used with Python (or R).

When choosing Python, we also need to choose the version of the language. While Python 2 is the most commonly used Python standard, Python 3 should take over in a few years. The Python community develops Python 3 libraries. Tech firms have started their migration toward this version. After 2020, Python 2.X will no longer be maintained. Therefore, if you are a new programmer, it is recommended to learn Python 3 over Python 2.

Both Python and R are among the most popular languages for assisting quantitative researchers (or quantitative developers) in creating trading algorithms. It provides a ton of support libraries for data analysis or machine learning. Choosing between these two languages will depend on which side of the community you are on. We always associate Python with a generalpurpose language with an understandable syntax and simplicity, while R was developed with statisticians as an end user by giving emphasis to data visualization. Even if Python can also give you the same visualization experience, R was designed for this purpose.

R is not significantly more recent than Python. It was released in 1995 by the two founders, Ross Ihaka and Robert Gentleman, while Python was released in 1991 by Guido Van Rossum. Today, R is mainly used by the academic and research world.

Unlike many other languages, Python and R allows us to write a statistical model with a few lines of code. Because it is impossible to choose one over the other, since they both have their own advantages, they can easily be used in a complementary manner. Developers created a multitude of libraries capable of easily using one language in conjunction with the other without any difficulties.

## **Choice of IDE – Pycharm or Notebook**

While RStudio became the standard **IDE** (**Integrated Development Environment**) for R, choosing between JetBrains PyCharm and Jupyter Notebook is much more challenging. To begin with, we need to talk about the features of these two different IDEs. PyCharm was developed by the Czech company JetBrains, and is a text editor providing code analysis, a graphical debugger, and an advanced unit tester. Jupyter Notebook is a nonprofit organization that created a web-based interactive computational environment for the following three languages: Julia, Python, and R. This software helps you to code Python by giving you a web-based interface where you will run the Python code line by line.

The major difference between these two IDEs is that PyCharm became a reference IDE among programmers, since the version control system and the debugger are an important part of this product. Additionally, PyCharm can easily handle a large code base and has a ton of plugins.

Jupyter Notebook is a friendly choice when data analysis is the only motivation, while PyCharm doesn't have the same user-friendly interface to run code line by line for data analytics. The features that PyCharm provides are the most frequently used in the Python programming world.

## **Our first algorithmic trading (buy when the price is low, and sell when the price is high)**

You may now feel that you are impatient to make money, and you may also be thinking *When can you start doing so?*

We have talked about what we will address in this book. In this section, we will start building our first trading strategy, called **buy low, sell high**.

Building a trading strategy takes time and goes through numerous steps:

- 1. You need an *original* idea. This part will use a well-known moneymaking strategy: we buy an asset with a price lower than the one we will use to sell it. For the purpose of illustrating this idea, we will be using Google stock.
- 2. Once we get the idea, we need data to validate the idea. In Python, there are many packages that we can use, to get trading data.
- 3. You will then need to use a large amount of historical data to backtest your trading strategy assuming this rule: what worked in the past will work in the future.

### **Setting up your workspace**

For this book, we have picked PyCharm as the IDE. We will go through all the examples using this tool.

You can find videos on the JetBrains website: https://blog.jetbrains.com/pychar [m/2016/01/introducing-getting-started-with-pycharm-video-tutorials/](https://blog.jetbrains.com/pycharm/2016/01/introducing-getting-started-with-pycharm-video-tutorials/).

# **PyCharm 101**

Once PyCharm is loaded, you will need to create a project and choose an interpreter. As we previously discussed, you will need to choose a version of Python 3. At the time of writing this book, the most up-to-date version is Python 3.7.0, but feel free to start with a more recent version than this one. Once the project is open, you need to create a Python file that you will call buylowsellhigh.py. This file will contain the code of your first Python implementation.

### **Getting the data**

Many libraries can help download financial data; our choice though is to use the pandas library. This software Python library is well known for data manipulation and analysis. We will use the DataReader function, which is capable of connecting to a financial news server such as Yahoo, Google, and many others, and then downloading the data that you will need for the example of this book. DataReader takes four arguments in this example:

- 1. The first one is the symbol (our example uses GOOG for Google) you would like to use for analysis.
- 2. The second specifies the source for retrieving the data, and then you will specify the range of days to get the data.
- 3. The third specifies the starting data from which to fetch historical data.
- 4. The fourth and final argument specifies the end data for the historical data series:

```
# loading the class data from the package pandas_datareader
from pandas_datareader import data
# First day
start_date = '2014-01-01'
# Last day
end_date = '2018-01-01'
# Call the function DataReader from the class data
goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)
```

The goog\_data variable is the data frame containing the Google data from January 1, 2014 to January 1, 2018. If you print the goog\_data variable, you will see the following:

```
print(goog_data)
 High Low ... Volume Adj Close
Date ...
2010-01-04 312.721039 310.103088 ... 3937800.0 311.349976
2010-01-05 311.891449 308.761810 ... 6048500.0 309.978882
2010-01-06 310.907837 301.220856 ... 8009000.0 302.164703
2010-01-07 303.029083 294.410156 ... 12912000.0 295.130463
```

If you would like to see all the columns, you should change the option of the pandas library by allowing more than four displayed columns:

```
import pandas as pd
pd.set_printoptions(max_colwidth, 1000)
pd.set_option('display.width', 1000)
 High Low Open Close Volume Adj Close
Date 
2010-01-04 312.721039 310.103088 311.449310 311.349976 3937800.0 311.349976
2010-01-05 311.891449 308.761810 311.563568 309.978882 6048500.0 309.978882
2010-01-06 310.907837 301.220856 310.907837 302.164703 8009000.0 302.164703
2010-01-07 303.029083 294.410156 302.731018 295.130463 12912000.0 295.130463
```

As per the previous output, there are six columns:

- High: The highest price of the stock on that trading day.
- Low: The lowest price of the stock on that trading day.
- Close: The price of the stock at closing time.
- Open: The price of the stock at the beginning of the trading day (closing price of the previous trading day).
- Volume: How many stocks were traded.
- Adj Close: The closing price of the stock that adjusts the price of the stock for corporate actions. This price takes into account the stock splits and dividends.

The adjusted close is the price we will use for this example. Indeed, since it takes into account splits and dividends, we will not need to adjust the price manually.

### **Preparing the data – signal**

The main part of a trading strategy (or a trading algorithm) is to decide when to trade (either to buy or sell a security or other asset). The event triggering the sending of an order is called a signal. A signal can use a large variety of inputs. These inputs may be market information, news, or a social networking website. Any combination of data can be a signal.

From the section entitled *Our first algorithmic trading (buy when the price is low, and sell when the price is high)*, for the *buy low sell high* example, we will calculate the difference in the adjusted close between two consecutive days. If the value of the adjusted close is negative, this means the price on the previous day was higher than the price the following day, so we can buy since the price is lower now. If this value is positive, this means that we can sell because the price is higher.

In Python, we are building a pandas data frame getting the same dimension as the data frame containing the data. This data frame will be called goog\_data\_signal:

goog\_data\_signal = pd.DataFrame(index=goog\_data.index)

Following the creation of this data frame, we will copy the data we will use to build our signal to trade. In this case, we will copy the values of the Adj Close column from the goog\_data data frame:

```
goog_data_signal['price'] = goog_data['Adj Close']
```

Based on our trading strategy, we need to have a column, daily\_difference, to store the difference between two consecutive days. In order to create this column, we will use the diff function from the data frame object:

```
goog_data_signal['daily_difference'] = goog_data_signal['price'].diff()
```

As a sanity check, we can use the print function to display what goog\_data\_signal contains:

```
print(goog_data_signal.head())
 price daily_difference
Date 
2014-01-02 552.963501 NaN
2014-01-03 548.929749 -4.033752
```

|  | 2014-01-06 555.049927 | 6.120178  |
|--|-----------------------|-----------|
|  | 2014-01-07 565.750366 | 10.700439 |
|  | 2014-01-08 566.927673 | 1.177307  |

We can observe that the daily\_difference column has a non-numerical value for January 2, since it is the first row in this data frame.

We will create the signal based on the values of the column, daily\_difference. If the value is positive, we will give the value 1, otherwise, the value will remain 0:

```
goog_data_signal['signal'] = 0.0
goog_data_signal['signal'] = np.where(goog_data_signal['daily_difference'] >; 0, 1.0, 0.0)
 price daily_difference signal
Date 
2014-01-02 552.963501 NaN 0.0
2014-01-03 548.929749 -4.033752 0.0
2014-01-06 555.049927 6.120178 1.0
2014-01-07 565.750366 10.700439 1.0
2014-01-08 566.927673 1.177307 1.0
```

Reading the column signal, we have 0 when we need to buy, and we have 1 when we need to sell.

Since we don't want to constantly buy if the market keeps moving down, or constantly sell when the market is moving up, we will limit the number of orders by restricting ourselves to the number of positions on the market. The position is your inventory of stocks or assets that you have on the market. For instance, if you buy one Google share, this means you have a position of one share on the market. If you sell this share, you will not have any positions on the market.

To simplify our example and limit the position on the market, it will be impossible to buy or sell more than one time consecutively. Therefore, we will apply diff() to the column signal:

```
goog_data_signal['positions'] = goog_data_signal['signal'].diff()
 price daily_difference signal positions
Date 
2014-01-02 552.963501 NaN 0.0 NaN
2014-01-03 548.929749 -4.033752 0.0 0.0
2014-01-06 555.049927 6.120178 1.0 1.0
2014-01-07 565.750366 10.700439 1.0 0.0
2014-01-08 566.927673 1.177307 1.0 0.0
2014-01-09 561.468201 -5.459473 0.0 -1.0
2014-01-10 561.438354 -0.029846 0.0 0.0
2014-01-13 557.861633 -3.576721 0.0 0.0
```

We will buy a share of Google on January 6 for a price of 555.049927, and then sell this share for a price of 561.468201. The profit of this trade is 561.468201-

555.049927=6.418274.

### **Signal visualization**

While creating signals is just the beginning of the process of building a trading strategy, we need to visualize how the strategy performs in the long term. We will plot the graph of the historical data we used by using the matplotlib library. This library is well known in the Python world for making it easy to plot charts:

1. We will start by importing this library:

import matplotlib.pyplot as plt

2. Next, we will define a figure that will contain our chart:

```
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
```

3. Now, we will plot the price within the range of days we initially chose:

goog\_data\_signal['price'].plot(ax=ax1, color='r', lw=2.)

4. Next, we will draw an *up* arrow when we buy one Google share:

```
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index,
 goog_data_signal.price[goog_data_signal.positions == 1.0],
 '^', markersize=5, color='m')
```

5. Next, we will draw a *down* arrow when we sell one Google share:

```
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index,
 goog_data_signal.price[goog_data_signal.positions == -1.0],
 'v', markersize=5, color='k')
plt.show()
```

This code will return the following output. Let's have a look at the following plot:

![](_page_55_Figure_0.jpeg)

Up to this point, we introduced the trading idea, we implemented the signal triggering buy and sell orders, and we talked about the way of restricting the strategy by limiting the position to one share on the market. Once these steps are satisfactory, the following step is backtesting.

#### **Backtesting**

Backtesting is a key phase to get statistics showing how effective the trading strategy is. As we previously learned, the backtesting relies on the assumption that the past predicts the future. This phase will provide the statistics that you or your company consider important, such as the following:

- **Profit and loss** (**P and L**): The money made by the strategy without transaction fees.
- **Net profit and loss** (**net P and L**): The money made by the strategy with transaction fees.
- **Exposure**: The capital invested.
- **Number of trades**: The number of trades placed during a trading session.
- **Annualized return**: This is the return for a year of trading.
- **Sharpe ratio**: The risk-adjusted return. This date is important because it compares the return of the strategy with a risk-free strategy.

While this part will be described in detail later, for this section, we will be interested in testing our strategy with an initial capital over a given period of time.

For the purpose of backtesting, we will have a portfolio (grouping of financial assets such as bonds and stocks) composed of only one type of stock: Google (GOOG). We will start this portfolio with \$1,000:

initial\_capital = float(1000.0)

Now, we will create a data frame for the positions and the portfolio:

positions = pd.DataFrame(index=goog\_data\_signal.index).fillna(0.0) portfolio = pd.DataFrame(index=goog\_data\_signal.index).fillna(0.0)

Next, we will store the GOOG positions in the following data frame:

positions['GOOG'] = goog\_data\_signal['signal']

Then, we will store the amount of the GOOG positions for the portfolio in this one:

portfolio['positions'] = (positions.multiply(goog\_data\_signal['price'], axis=0))

Next, we will calculate the non-invested money (cash):

portfolio['cash'] = initial\_capital - (positions.diff().multiply(goog\_data\_signal['price'], axis=0)).cumsum()

The total investment will be calculated by summing the positions and the cash:

portfolio['total'] = portfolio['positions'] + portfolio['cash']

When we draw the following plot, we can easily establish that our strategy is profitable:

![](_page_57_Figure_0.jpeg)

When we create a trading strategy, we have an initial amount of money (cash). We will invest this money (holdings). This holding value is based on the market value of the investment. If we own a stock and the price of this stock increases, the value of the holding will increase. When we decide to sell, we move the value of the holding corresponding to this sale to the cash amount. The sum total of the assets is the sum of the cash and the holdings. The preceding chart shows that the strategy is profitable since the amount of cash increases toward the end. The graph allows you to check whether your trading idea can generate money.

## **Summary**

During this chapter, you were introduced to the trading world. You learned why people trade and you are capable of describing the critical actors and the trading systems with which you will interact during your life as an algorithm trading designer. You were exposed to the tools you will use in this book to build your trading robot. Finally, you encountered your first implementation of algorithmic trading by coding your first trading strategy implementing the economic idea of buying low and selling high. We observed that this strategy was far from being a profitable and safe strategy.

In the next chapter, we will address how to make a strategy more advanced, linked to more sophisticated trading ideas, while implementing these strategies in Python.
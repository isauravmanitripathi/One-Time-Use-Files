![](_page_0_Figure_1.jpeg)

Orders are the fundamental building block for any trading strategy.

#### 4.1 Introduction

Orders represent execution instructions. They allow investors and traders to communicate their requirements, both from the type of order chosen as well as with a range of additional conditions and directions. This chapter focuses on the basic mechanics of these various order types and conditions.

The two main order types are market orders and limit orders. In terms of liquidity provision, these are complete opposites. Market orders demand liquidity; they require immediate trading at the best price available. Whereas limit orders provide liquidity, they act as standing orders with inbuilt price limits, which must not be breached (a maximum price for buys and a minimum price for sells).

The conditions that may be applied to each order allow the trader to control many features of the execution, for example:

- Both how and when it becomes active.
- Its lifetime/duration ٠
- Whether it may be partially filled  $\bullet$
- Whether it should be routed to other venues or linked to other orders

A wide range of trading styles can be achieved just by combining these conditions with limit and market orders. Indeed, many venues have gone on to support an even broader spectrum of orders, all essentially derived from basic market and limit orders. These include:

- Hybrid orders, such as market-to-limit
- Conditional orders, such as stops and trailing stops ٠
- $\bullet$ Hidden and iceberg orders
- $\bullet$ Discretional orders, such as pegged orders
- Routed orders, such as pass-through orders

New order types are continuing to evolve. Some venues even offer orders that behave like algorithms, such as targeting the VWAP or participating in a set percentage of the market volume. Indeed, the line between them and trading algorithms is becoming increasingly blurred. Dynamic order types are very similar to trading algorithms, since they both alter based on market conditions. One way of differentiating between the two is that dynamic orders generally only focus on one specific variable, often the current market price (e.g. stop orders, pegging orders). Whereas trading algorithms base their decisions on a range of conditions, from volume to volatility. For the purposes of this text, we shall adopt this classification, so trading strategies such as VWAP and volume participation will be discussed further in Chapter 5. We shall also discuss how orders are actually used to implement algorithms and trading strategies in Chapter 9.

The examples in this chapter are broadly based on examples from the major exchanges. Some venues, notably the London Stock Exchange (LSE) (2006) and the Chicago Mercantile Exchange (CME) (2006), provide excellent materials with detailed examples for their order types. So it is always worth checking for such documentation. Another useful guide to the various types of orders is Larry Harris's (1999) book 'Trading and Exchanges'.

Finally, before we start covering the different order types and conditions in more detail, it is worth noting a few of the key assumptions made in the examples for this chapter. Firstly, they are all based around order books. Fundamentally, all trading involves order books, whether it is a phone-based OTC transaction or electronic trading via DMA, RFQ or a trading algorithm. The only real difference is that for quote-driven markets the order book is completely private and belongs to the market maker, whereas for order-driven markets the order book is usually centralised and much more transparent. Secondly, the examples generally cater for continuous trading periods, although some separate ones are highlighted for call auctions. This is simply because for most of these order types continuous trading is the most relevant period. Also for convenience, we usually assume that an execution will occur when we place an order that matches. Obviously, in real markets hundreds of participants can be issuing orders at the same time so regardless of a match our orders will sometimes be beaten to it. Lastly, the examples generally assume that the marketplace adopts a price/time priority, though for some cases the effect of different priorities is also highlighted.

So let's start by reviewing the mechanism of market and limit orders in more detail.

#### 4.2 Market orders

The market order is an instruction to trade a given quantity at the best price possible. The focus is on completing the order with no specific price limit, so the main risk is the uncertainty of the ultimate execution price.

Market orders demand liquidity, a buy market order will try to execute at the offer price, whilst a sell order will try to execute at the bid price. The immediate cost of this is half the bid offer spread. We can see this using the sample order book shown in Figure 4-1.

|               |         | Buys  |       | Sells |       |         |    |  |  |
|---------------|---------|-------|-------|-------|-------|---------|----|--|--|
| $\text{1d}$   | Time    | Size  | Price | Price | Size  | Time    | ld |  |  |
| $\mathbf{B}1$ | 8:25:00 | 1,000 | 100   | 101   | 1,000 | 8:25:00 | S  |  |  |
| B2            | 8:20:20 | 1.500 | 99    | 102   | 800   | 8:20:25 | S2 |  |  |
| B3            | 8:24:00 | 900   | 98    | 102   | 1.200 | 8:24:09 | S3 |  |  |

## Figure 4-1 An example order book

A market order to buy 1,000 ABC can cross with sell order (S1) achieving a price of 101. We should then he able to immediately close out this position with an equivalent order to sell, which crosses with the buy order (B1) at 100. Hence the overall cost of both our market orders has been  $(101 - 100)$  which equals the spread, or half the spread each way.

For orders that are larger than the current best bid or offer size, most venues allow market

orders to "walk the book". If they cannot fill completely from the top level of the order book, they then progress deeper into the book (increasing the price for buys, or decreasing for sells) until the order is completed. If the order still cannot be completed some venues will cancel it, such as the LSE, whilst others may leave the residual market order on the order book, e.g. Euronext.

Thus, the execution price achieved depends on both the current market liquidity and the size of the market order. For example, if we issue a market order to buy 2,000 ABC, the order book in Figure 4-2(a) shows that this can potentially cross with the sell orders S1 and S2. Receiving fills of 1,000 at 101 from order S1, and 1,000 at 102 from S2 gives an average execution price of 101.5. The resultant order book (b) shows that order S1 has been completed and S2 now only has 500 on offer (the buy side is unchanged and so is omitted).

| Buys         |       |       |       | Sells   |             |  | Sells     |       |         |             |
|--------------|-------|-------|-------|---------|-------------|--|-----------|-------|---------|-------------|
| Size         | Price | Price | Size  | Time    | $\text{Id}$ |  | Price     | Size  | Time    | 1d          |
| 1,000        | 100   | 101   | 1,000 | 8:25:00 | S1          |  | 101       | 1,000 | 8:25:00 | $\text{S}1$ |
| 800          | 99    | 102   | 1,500 | 8:20:25 | S2          |  | 102       | 1.000 | 8:20:25 | \$2         |
| 1.500        | 98    | 104   | 2,000 | 8:19:09 | S3          |  | 102       | 500   | 8:20:25 | S2          |
|              |       | 106   | 3,000 | 8:15:00 | S4          |  | 104       | 2,000 | 8:19:09 | S3          |
|              |       |       |       |         |             |  | 106       | 3,000 | 8:15:00 | S4          |
| $(a)$ hefore |       |       |       |         |             |  | (b) after |       |         |             |

Figure 4-2 The effect of a market order on the order book

In this example, as well as paying half the spread there is an additional cost that corresponds to the price jump from 101 to 102, resulting in a higher average execution price. This additional cost represents the market impact of our order. It is dependent on both the size of the order and the current market conditions, particularly the liquidity. For instance, if the example had been for an order of 5,000 we can see from Figure 4-2(a) that it would require crossing with orders S1 to S4, resulting in an average execution price of 103. Consequently, large orders often have a greater market impact than smaller ones.

Market conditions can also change rapidly. Again using the example from Figure 4-2 let's assume the owner of order S2 suddenly cancelled just before our market order to buy 2,000 hit the order book. In which case, our market order must now cross with order S3, the fill of  $1,000$  at 104 raises the average execution price to  $102.5$ .

Sometimes market orders can actually achieve better prices than expected. This price improvement could be because the market order executed against a hidden order, such as an iceberg order, so a better price may be possible than the order book suggests. We will cover these order types later on in this chapter.

With no price limit, the performance of market orders is clearly dependent on current market conditions. Similarly, large market orders can have significant market impact, so it may be worth splitting such orders into smaller ones. If performance is more important than the speed (and certainty) of execution then a limit order may be a hetter choice.

#### $4.3$ Limit orders

A limit order is an instruction to buy or sell a given quantity at a specified price or better. A buy limit order must execute at or below this limit price, whereas a sell order must execute at or above it.

Limit orders will try to fill as much of the order as they can, without breaking the price

limit. If there are no orders that match at an acceptable price then the order is left in place on the order book until it expires or is cancelled. If the order is partially executed then any residual quantity will remain on the order book. This helps provide liquidity since other traders can see we are willing to trade at a given price and quantity.

This persistence makes limit orders quite versatile. They may be used with an aggressive limit price, in which case they act like a market order demanding liquidity. The firm price limit gives added price protection compared to a market order, although there is the risk of failing to execute. Alternatively, limit orders may be issued with more passive limits, such as when trying to capture gains from future price trends or reversions, as shown in Figure 4-3.

![](_page_3_Figure_3.jpeg)

Figure 4-3 Limit orders intended to gain from future price trends

For example, by placing a limit order to sell at 93.5, at time t, when the last traded price was 93 we are hoping that the price does not suddenly drop, otherwise our order will expire unexecuted. Alternatively, we might place a buy order with a limit of 92, just in case the price reverts as shown in pathway (a). Note that even if the price reaches our limit there is still no guarantee of execution, since other orders may have priority over ours.

Let's consider a more detailed example: If we issue a buy limit order for 1,000 ABC at 100, as shown in Figure 4-4, there is no order that can immediately be crossed with this.

| Buvs          |            |       |       |       | Sells |               | Buys      |       |       |  |
|---------------|------------|-------|-------|-------|-------|---------------|-----------|-------|-------|--|
| ld            | Time       | Size  | Price | Price | Size  | 1d            | Time      | Size  | Price |  |
| $\mathbf{B1}$ | 8:25:00    | 500   | 100   | 101   | 1,000 | $\mathbf{B1}$ | 8:25:00   | 500   | 100   |  |
| B2            | 8:20:25    | 1,500 | 99    | 102   | 800   | B4            | 8:28:00   | 1.000 | 100   |  |
| B3            | 8:24:09    | 2,000 | 98    | 102   | 1,500 | B2            | 8:20:25   | 1,500 | 99    |  |
|               |            |       |       |       |       | B3            | 8:24:09   | 2,000 | 98    |  |
|               | (a) before |       |       |       |       |               | (b) after |       |       |  |

Figure 4-4 The effect of a limit order on the order book

Thus, our order is left on the order book as B4. Note its position, it is placed after order B1 since it has less time priority, but is placed ahead of order B2 because it has price priority. So any incoming sell orders that would cross at a price of 100 will first match with order B1, then with B4 (unless pro-rata based matching is used).

To see how limit orders differ from market orders lets do a similar trade to the example in Figure 4-2, using instead a limit order to buy 2,000 ABC at the current best offer (i.e. 101). This is shown in Figure 4-5.

|             |         | Buys  |       | Sells |       |         |    |  |  |
|-------------|---------|-------|-------|-------|-------|---------|----|--|--|
| 1d          | Time    | Size  | Price | Price | Size  | Time    | ĺd |  |  |
| $\text{B1}$ | 8:25:01 | 1,000 | 100   | 101   | 1,000 | 8:25:00 | S1 |  |  |
| B2          | 8:20:02 | 800   | 99    | 102   | 1,500 | 8:20:25 | S2 |  |  |
| B3          | 8:24:09 | 1,500 | 98    | 104   | 2,000 | 8:19:09 | S3 |  |  |
|             |         |       |       |       |       |         |    |  |  |

(a) before

|             |         | Buvs  |       | Sells |       |         |    |  |  |
|-------------|---------|-------|-------|-------|-------|---------|----|--|--|
| ld          | Time    | Size  | Price | Price | Size  | Time    | ld |  |  |
| B4          | 8:28:00 | 1,000 | 101   | 101   | 1.000 | 8:25:00 | S1 |  |  |
| $\text{B1}$ | 8:25:01 | 1,000 | 100   | 102   | 1,500 | 8:20:25 | S2 |  |  |
| B2          | 8:20:02 | 800   | 99    | 104   | 2,000 | 8:19:09 | S3 |  |  |
| B3          | 8:24:09 | 1,500 | 98    |       |       |         |    |  |  |

(b) after

## Figure 4-5 A partially executed limit order

We can see from this that order S1 can be immediately crossed with our buy order. However, we cannot cross with sell order S2 because its price of 102 breaks our limit condition. The remaining 1,000 will be left on the order book as a buy at 101, shown as order B4. Due to price priority, our order is placed at the top of the order book, resulting in shifting the spread to 101-102, up from 100-101.

If the owner of order S1 suddenly cancelled just before our order hit the order book then since we cannot cross with order S2 the whole 2,000 would have been left on the order book as order B4 to buy at 101.

In comparison with the market order, we have sacrificed complete execution to ensure our price, so instead of filling 2,000 at 101.5 we have achieved 1,000 at exactly 101. Whilst if we had changed our limit price to be 102 we could have matched with the sell order S2, giving the same average price as the market order.

So the main risk with limit orders is this lack of execution certainty. The market price may never reach our limit or even if it does, it may still not be executed since other orders may have time priority. This emphasises the need to make a careful choice between the requirements for immediacy and price.

![](_page_4_Figure_11.jpeg)

Figure 4-6 Viewing the order book in terms of price

The limit price is also an important means of classifying limit orders, since it reflects their

probability of immediate execution. Figure 4-6 tries to show this by twisting the order book from Figure 4-5(a) to align all the orders by increasing limit price. Limit orders with the highest probability of execution are often termed marketable orders, since their limit prices are such that they can potentially cross immediately with an order on the other side of the book. Hence, a marketable buy order has a limit equal to or greater than the current best offer price, whilst a marketable sell order has a limit price greater than or equal to the best bid.

Orders that are placed "at the market" correspond to buys with a limit of the best bid or sells with a limit at the best offer. The traders who placed these orders are said to be making the market. Whilst the most passively priced limit orders are termed "behind the market". Their prices mean that they are likely to remain on the order book as standing limit orders until the best bid or offer price moves closer to them.

#### **Optional order instructions** $4.4$

Order instructions are conditions that cater for the various requirements for a wide range of trading styles. As we can see in the summary in Table 4-1, they allow control over how and when orders become active, how they are filled and can even specify where (or to whom) they are sent to.

| Type                     | <b>Example Instructions</b>                                                       |
|--------------------------|-----------------------------------------------------------------------------------|
| Duration                 | Good for the day, Good 'til date, Good 'til cancel, Good after<br>time/date       |
| Auction/Crossing session | On-open, On-close, Next-auction                                                   |
| Fill                     | Immediate-or-cancel, Fill-or-kill, All-or-none,<br>Minimum-volume, Must-be-filled |
| Preferencing             | Preferenced, Directed                                                             |
| Routing                  | Do-not-route, Directed-routing, Inter-market sweeps, Flashing                     |
| Linking                  | One-cancels-other, One-triggers-other                                             |
| Miscellaneous            | Identity, Short sales, Odd lots, Settlement                                       |

# **Table 4-1 Order instruction conditions**

In the following sub-sections, we will see how each of these instruction types may be used.

# **Duration instructions**

Generally, orders are assumed to be valid from their creation until they are completely filled or cancelled, or it reaches the end of the current trading day. These are known as day orders or "good for the day" (GFD) orders.

Specific instructions may be used to alter this duration, such as:

- "good 'til date" (GTD):
- "good 'til cancel" (GTC)  $\bullet$
- "good after time/date" (GAT)

As the names suggest, a "good 'til date" order will remain active until the end of trading on the given date. Some venues even support variants such as "good this week" (GTW) and "good this month" (GTM).

A "good 'til cancel' instruction means the associated order should stay active until the

The "good after time/date" instruction is somewhat less common. Clearly, it allows control over when the order actually becomes active. This instruction is more often used for broker systems where clients may choose to spread orders throughout the day, rather than for actual exchange orders. Most trading algorithms support similar behaviour by using a start time parameter.

# Auction/Crossing session instructions

Auction/session instructions are used to mark an order for participation in a specific auction, or trading either at the open, close or intraday. They can also be used for the intraday crosses, which some exchanges have started introducing to compete with external crossing networks and ATSs.

Like normal market orders, auction market orders are intended to maximise the probability of execution, since in the auction matching they will always have price priority. Whereas auction limit orders will only be executed if the auction price equals or is better than their limit price, as we saw in Chapter 2.

On-open orders may be submitted during the pre-open period for participation in the opening auction. If the matching volume is sufficient then market-on-open (MOO) orders will execute at the auction price. For any unfilled MOO orders, some venues convert them to a limit order at the auction price, whilst others simply cancel them. Whereas limit-on-open (LOO) orders will only execute if there is sufficient volume and the auction price is equal to or better than their price limit.

On-close orders may be submitted during the pre-close period. Market-on-close (MOC) orders will execute at the closing price, given sufficient matching volume. Any unfilled orders will be cancelled. Again limit-on-close (LOC) orders will only fill given sufficient matching volume and an auction price equal to or better than their specific limit.

Venues with intraday auctions generally support an intraday auction or a "next auction" type. This is able to roll to the next valid auction, whether that is an intraday, open or close. A similar approach is often adopted for daily crossings or "mid point" matches.

In addition to the session instructions, NASDAQ also provides "imbalance-only" opening and closing orders. These are intended to allow liquidity providers to add orders to offset the extant on-open and on-close orders without adding to the overall imbalance.

## Fill instructions

Traditionally, fill instructions were used to try to minimize the clearance and settlement costs for trades. But they are now more commonly used as part of liquidity seeking strategies. Instructions such as immediate-or-cancel enable orders to demand liquidity without leaving an obvious footprint on the order book.

Table 4-2 summarises the range of fill instructions that are available, most markets support a subset of these.

#### Immediate-or-cancel

This instruction means any portion of the order that cannot execute immediately against existing orders will be cancelled. Any limit price will be enforced, so it will execute as much of the required quantity as is available within the specified limit. This can result in only partially filling the order.

| Instruction         | Partial execution<br>allowed | Unexecuted part<br>added to the book? | Expires                         |
|---------------------|------------------------------|---------------------------------------|---------------------------------|
| Immediate-or-cancel | Yes                          | No                                    | Immediately after<br>submission |
| Fill-or-kill        | No                           | No                                    | Immediately after<br>submission |
| All-or-none         | No                           | No                                    | End of day                      |
| Minimum-volume      | Yes                          | Yes                                   | End of day                      |
| Must-be-filled      | No                           | N/A                                   | After submission                |

#### **Table 4-2 Order fill instruction types**

Immediate or cancel (IOC) order instructions are also sometimes referred to as execute and climinate, fill and kill, good on sight, immediate liquidity access and accept orders, across a range of execution venues. Such a variety of naming standards is clearly confusing; it is always worth carefully checking the documentation to confirm the exact behaviour. Note that for some venues immediate may actually correspond to being within a set time period (up to a few seconds); so again, it is vital to check the specifications.

As an example, if we issue an IOC limit order to buy 1,500 ABC at 101, we can see from the order book in Figure 4-7 that this can immediately cross with the sell orders S1 and S2. Order S3 is priced at 102 so no more of the order may be filled within the price limit. Therefore our buy order is now immediately cancelled, although 500 remains unfilled. We have obtained 1,000 ABC at 101 and left no residual order on the book.

| Buvs                                 |       |       |       | Sells   |    | Sells                                                                                        |       |         |    |
|--------------------------------------|-------|-------|-------|---------|----|----------------------------------------------------------------------------------------------|-------|---------|----|
| Size                                 | Price | Price | Size  | Time    | ld | Price                                                                                        | Size  | Timc    | ld |
| 1,000                                | 100   | 101   | 400   | 8:20:00 | S  | 101                                                                                          | 400   | 8:20:00 | SI |
| 800                                  | 99    | 101   | 600   | 8:22:25 | S2 | 101                                                                                          | 600   | 8:22:25 | S2 |
| 2,500                                | 98    | 102   | 1.200 | 8:24:09 | S3 | 102                                                                                          | 1.200 | 8:24:09 | S3 |
|                                      |       |       |       |         |    |                                                                                              |       |         |    |
| $\angle \mathbf{1} \cdot \mathbf{1}$ |       |       |       |         |    | $\mathcal{L} \mathbf{1} \cdot \mathbf{1} \cdot \mathbf{1} \cdot \mathbf{1} \cdot \mathbf{1}$ |       |         |    |

(a) before

(b) after

![](_page_7_Figure_8.jpeg)

Orders using this type of instruction have also been termed "Immediate Liquidity Access", which is an appropriate name since that is exactly what it has done. The IOC instruction makes an order grab available liquidity; unlike a market order, it also maintains our price limit. Thus, the IOC instruction is often used by algorithms when probing for liquidity.

NYSE's Area offers a novel twist on the concept of immediate-or-cancel orders. Their "NOW" order instruction means that if an order cannot be immediately executed then it will be routed to a dedicated liquidity provider.

#### Fill-or-kill

A fill-or-kill (FOK) instruction ensures that the order either executes immediately in full or not at all. Effectively, it is an IOC instruction combined with a 100% completion requirement. Any limit price takes precedence, so if it cannot fill the order within the given limit then it will cancel it. This instruction is also sometimes referred to as a complete

volume (CV) order. Note that some venues use the term fill-and-kill, but, as always, it is important to check their documentation since this may actually refer to an immediate-orcancel style behaviour.

Figure 4-8 shows an example FOK limit order to buy 1,000 ABC at 101. Again, we can see from the order book in that this can immediately cross this with the sell order S1. Also note that just like IOC orders, the fill-or-kill instruction makes an order non-persistent, so if someone else managed to cross with sell order S1 first then our order would be cancelled, since we cannot cross with order S2 because of its price.

| Buys       |       |       |       | Sells   |    |        | Sells     |       |         |    |
|------------|-------|-------|-------|---------|----|--------|-----------|-------|---------|----|
| Size       | Priee | Price | Size  | Time    | ld |        | Price     | Size  | Time    | 1d |
| 1,000      | 100   | 101   | 1,000 | 8:25:00 | S1 |        | 101       | 1,000 | 8:25:00 | S1 |
| 1,200      | 99    | 102   | 900   | 8:20:25 | S2 |        | 102       | 900   | 8:20:25 | S2 |
| 2,000      | 98    | 102   | 1,800 | 8:24:00 | S3 |        | 102       | 1.800 | 8:24:00 | S3 |
|            |       |       |       |         |    | $\sim$ |           |       |         |    |
| (a) before |       |       |       |         |    |        | (b) after |       |         |    |

Figure 4-8 The effect of an FOK order on the order book

## All-or-none

The all-or-none (AON) instruction enforces a 100% completion requirement on an order. Unlike the fill-or-kill instruction there is no requirement for immediacy, so all-or-none orders may persist for some time. This can pose a problem for order book based systems, since the asset could well end up trading below the price of an AON buy order, or above the price of an AON sell, particularly if the AON order is large. Thus, AON orders are given a lower priority for execution, and are often handled by storing them on a separate conditional order book. This additional complexity has meant that many of the markets which once supported all-or-none instructions, such as NYSE, Euronext and the ASX, have switched to using IOC or fill-or-kill orders instead.

## Minimum-volume

This is also sometimes referred to as a minimum fill or minimum acceptable quantity instruction. A minimum-volume ensures that the order will only match if the quantity is sufficient. As we saw with AON orders, this constraint could mean that minimum volume orders are left behind by the market. Hence, some markets, such as Euronext, cancel the order if it cannot immediately fill for the minimum quantity.

Minimum-volume constraints are also supported for call auctions in some markets, for example, NASDAQ. Figure 4-9 shows a simplified call auction for asset ABC where several of the sell orders have minimum quantity instructions.

|         | Buvs   |       |       |        | Sells               |             |        |       |
|---------|--------|-------|-------|--------|---------------------|-------------|--------|-------|
| Time    | Size   | Price | Price | Size   | Notes               | $\text{Id}$ | Weight | Alloc |
| 7:25:00 | 15,000 | MO    | MO    | 3,000  | $\text{Min } 1,000$ | S1          | 1,500  | 2,100 |
|         |        |       | MO    | 5,000  | Min 1,000           | S2          | 2,500  | 3,500 |
|         |        |       | MO    | 9,000  | Min 5,000           | S3          | 4,500  |       |
|         |        |       | MO    | 13,000 |                     | S4          | 6,500  | 9,400 |
|         |        |       | MO    | 5,000  |                     |             |        |       |
|         |        |       | 107   | 7,000  |                     |             |        |       |

Figure 4-9 An example call auction with minimum volume instructions

The "Weight" column shows how the allocations might have been assigned. Note that sell order S3 has a minimum volume constraint of 5,000. This is more than the assigned weighting of 4,500, so order S3 is excluded from the crossing. Consequently, the allocations we actually see in the "Alloc" column are quite different, since the 4,500 is redistributed amongst the other sell orders.

Note that in this example lot sizes of 100 are applied so there is a residual of 200. When assigning any residual amounts some auctions will favour orders with the lowest minimum quantity, so in this case the allocation for order S4 is increased to 9,400.

## Must-be-filled

Unlike some of the other fill instructions, failure to fully execute is really not an option for must-be-filled (MBF) orders. Indeed, on Euronext they used to trigger a volatility interruption, a sudden intraday halt followed by a call auction, if they were not filled.

Nowadays must-be-filled orders are generally associated with trading to fulfil expiring futures or option contracts. A separate trading session is established on the day before expiration, so for options this is often the third Thursday of each month. Traders may place orders to offset their expiring positions. For instance, an uncovered option writer for an inthe-money call must buy the underlying in readiness for its exercise the next day. MBF orders are effectively treated as market orders, although they are exempted from any short sale regulations. They will then be crossed as part of the following morning's opening auction. Some exchanges publish an MBF imbalance to ensure liquidity providers place sufficient orders for the MBF orders to complete.

# Preferencing and directed instructions

Order preferencing and directed instructions permit bilateral trading, since they direct orders to a specific broker or dealer. One controversy with both directed and preferenced orders is the fact that they bypass any execution priority rules. So other orders which may have time priority will lose out to the directed market maker.

Preferenced orders prioritise a specific market maker; generally, they are handled alongside normal order flow. On some venues, such as NASDAQ, preferenced orders behave more like a directed fill-or-kill order, since they are cancelled if the chosen market maker is not quoting at the best price.

Directed orders are routed to a specified market maker or dealer who may accept or reject them. On both the International Securities Exchange (ISE) and the Boston Options Exchange (BOX), market makers can offer price improvement for directed orders. The ISE has a dedicated price improvement mechanism, which is a special one-second auction.

Note that NASDAQ used to offer directed orders via SelectNet, but retired this in 2005. Directed non-liability orders allowed the market maker five seconds to accept, partially accept, decline or issue a counter offer for the order. Now when NASDAQ refers to directed orders it is in terms of routing instructions for specific venues.

## Routing instructions

Execution venues have often catered for additional routing instructions for orders. Thus providing a gateway service that allows orders to be routed to other venues as well as handling them locally.

In the U.S. equities market, the introduction of Regulation-NMS has made routing instructions even more important. In particular, the Order Protection Rule means that brokers and venues are now responsible for protecting orders to ensure they achieve the best price.

So if an order might "trade-through" the best price available at another venue, the host venue should either reject the order or forward it on to the venue where it can achieve the better price. However, such automated order routing is not always appropriate, especially for traders or systems that are simultaneously executing across a range of venues. Therefore, instructions such as do-not-route and inter-market sweep allow better control over the order routing. Clearly, when using such instructions it becomes the trader's or system's responsibility to ensure it is still complying with Regulation-NMS.

In section 4.5, we will cover some additional order types that cater for even more complex routing strategies.

#### Do-not-route

This instruction ensures that the execution venue will handle the order locally and not route it to another venue. They are also referred to as do-not-ship instructions on NYSE and postno-preference orders on NYSE Area.

In terms of Regulation-NMS, this means that if an order is placed at a venue, but a better price is available elsewhere then it should be rejected. In all other respects, orders with this instruction behave as normal.

#### **Directed-routing**

Directed-routing provides an associated destination for where the order should be routed to. Effectively, the host venue acts as a gateway to route such orders on to their chosen destination. The advantage of this approach is that orders may be routed to venues for which we do not have a membership, although the host venue will levy routing fees for such orders.

#### Inter-market sweeps

Under Regulation-NMS, flagging an order as an inter-market sweep allows the order to sweep, or walk down, the order book at a single venue. It means the broker/trader must ensure that the order protection and best execution requirements are met. So an inter-market sweep order will generally be part of a group of orders, issued simultaneously, to a range of execution venues (hence the name).

For example, let's consider the consolidated market order book for asset ABC shown in Figure 4-10. For simplicity, the market has only two venues, exchange Exch-1 and ECN-1.

|                 | Buys  |       |       | Sells |                 |
|-----------------|-------|-------|-------|-------|-----------------|
| Venue           | Size  | Price | Price | Size  | Venue           |
| ECN-1           | 800   | 50.00 | 50.01 | 1,500 | $\text{Exch-1}$ |
| $\text{Exch-1}$ | 1,500 | 50.00 | 50.01 | 500   | $ECN-1$         |
| $ECN-1$         | 1.000 | 49.99 | 50.02 | 1,200 | $\text{Exch-1}$ |
| $\text{Exch-1}$ | 700   | 49.99 | 50.02 | 800   | $ECN-1$         |
| $ECN-1$         | 1,200 | 49.98 | 50.03 | 2,200 | $\text{Exch-1}$ |

Figure 4-10 An example market consolidated order book

We could send a buy order for 3,000 at 50.03 to the exchange and leave it to decide whether any of the order needs to be routed to alternate venues. Alternatively, if we also have access to ECN-1 we could save routing fees by sending a buy for 2,000 at 50.02 to Exch-1 and a buy for 1,000 at 50.02 to ECN-1.

If we use standard orders for this, each venue will apply their own logic to ensure that any matches do not "trade through" better prices at other venues. For example, let's assume the order book for Exch-1 looks like Figure  $4-11(a)$ . Our order to buy 2,000 can immediately

| $\text{Exch-1}$ | Sells |    | $\text{Exch-1}$ | Sells                |     | $\text{Exch-1}$ | Sells                  |     |
|-----------------|-------|----|-----------------|----------------------|-----|-----------------|------------------------|-----|
| Price           | Size  | Id | Price           | Size                 | Id  | Price           | Size                   | Id  |
| 50.01           | 500   | S1 | 50.01           | 500                  | \$1 | 50.01           | 500                    | \$1 |
| 50.01           | 1.000 | S2 | 50.01           | 1.000                | \$2 | 50.01           | 1.000                  | \$2 |
| 50.02           | 500   | S3 | 50.02           | 500                  | S3  | 50.02           | 500                    | \$3 |
| 50.02           | 700   | S4 | 50.02           | 700                  | S4  | 50.02           | 700                    | S4  |
| (a) Before      |       |    |                 | (b) Exchange routing |     |                 | (c) Inter-market sweep |     |

Figure 4-11 Example execution for an inter-market sweep

cross with orders S1 and S2 since they are priced at 50.01, which is the best price available across all the market venues. For the remaining amount, there are no more orders on the exchange at this price level.

Before matching at a new price level, the exchange needs to check whether any orders at 50.01 are quoted at other venues. Based on the consolidated order book the exchange would need to route the remaining 500 to ECN-1. So the resultant order book for Exch-1 is shown in Figure  $4-11(b)$ .

Given that we know we have already routed a separate order to ECN-1, we clearly do not want the exchange to try to route part of our order to ECN-1. Instead, we just want to sweep the book at Exch-1 for all 2,000. So we must flag our order to Exch-1 as an inter-market sweep. Consequently, it will no longer seek to route the order and just fill versus orders S1 to S3, as shown in Figure  $4-11(c)$ .

By using an inter-market sweep, we get better control over exactly how and where our orders are placed, something that becomes vital when systems are working different orders simultaneously across many venues. It also allows us to save any additional routing charges that venues may apply.

## Flashing

As their name suggests, flash orders are displayed on the source venue for an instant before either being routed on to another destination. The timescales involved are often around 25-30 milliseconds, although some variants may last for up to half a second.

In the U.S equities market, the Regulation-NMS order protection rule means orders must be routed to the venue displaying the hest bid price, although routing charges may be applied. There may also be fees for taking liquidity from the destination venue. So the intention of flash orders was to offer traders the potential for achieving the best market price, in this case, the national best bid and offer (NBBO), without having to pay any extra charges. Similarly, for execution venues, they provide the chance to fill orders locally instead of routing them to a competitor.

This was achievable because each venue provides their own market data feed/s in addition to the national quotation system. During the flash period, market participants with the right data feeds could see and potentially trade with these orders, before they were routed on or cancelled. This has made them controversial, with much talk of creating a "two-tiered" market; despite the fact that venues offering flash orders made their data feeds readily available. In fact, many of the U.S. equity venues have now withdrawn their flash orders.

In part, this controversy simply reflects the pace of change of technology: The old intermarket system (ITS), which was replaced by the order protection rule, allowed a 30-second time window for an order to be acted on. Only time will tell whether flash orders become more widely accepted (for equities or any other asset classes).

## Linking Instructions

Linking instructions provide a means of introducing dependencies between orders.

A one-cancels-other (OCO) instruction may be used to make two orders mutually exclusive, often this is used to close out of a position. For instance, to capitalise from any gains on a long position we could place a sell order at a high price. If the market moves against us, it makes sense to also have a separate stop order at a lower price. Clearly, we do not want both orders to execute since this would not only flatten our position but could actually reverse it, leading to a short position. By linking the two sells with an OCO instruction, we can ensure that if either of the sell orders executes then the other will immediately be cancelled. Note that if one of the OCO orders is cancelled the other remains unaffected.

A One-triggers-other (OTO) instruction links a supplementary order that will only be created upon the successful execution of the main order. For example, a successful buy order could automatically spawn a stop order as protection from any losses. The secondary order is contingent on the main order, and so is sometimes referred to as an if-done order. Note that if the primary order is cancelled then the secondary order will also be cancelled; however, this linkage does not work the other way around.

Some venues even allow orders to be grouped. For example, the SAXESS trading platform supports both linked and combination orders. Linked orders effectively provide an "OR" logie, so for a given amount we can buy assets ABC, DEF or XYZ. As an order fills for one asset, the other orders all reduce their sizes proportionally. Combination orders provide "AND" logic linking both the prices and sizes for two distinct orders, effectively allowing spread trading. We shall go through these order-contingent types in more detail in section  $4.5$ .

# Miscellaneous instructions

So far, we have focussed on the instructions that are commonly adopted across most execution venues. There are also more specialised options, which tend to be more venue specific. As always, it is worth carefully checking each venue's documentation to see exactly what additional instructions are supported. Some of the more common miscellaneous instructions are:

Identity details: Many venues offer anonymity by default. Although some others still allow anonymous identifiers to be used, for instance, using the SIZE identifier on NASDAQ.

Short-sales: This flag must be set for markets that enforce short sales regulations. This is used to enforce tick-sensitive trading, i.e. selling only on an uptick or even tick.

*Odd-lots:* Some venues incorporate odd-lot trading together with the normal trading mechanism. This instruction allows round lot orders to be matched with odd-lots.

Settlement instructions: Generally, non-standard settlement instructions require negotiation, and depending on the conditions may incur higher broker fees or may not even he possible. However, some reasonably common non-standard instructions are supported, such as foreign currency settlement. Cash settlement is the most common alternative for equities. This is often used to achieve same day settlement, rather than T+1 or T+3. Typically, eash settlement is needed in order to become the shareholder of record before dividends, rights issues or stock splits, as Larry Harris (1999) points out. Clearly, though, this benefit will attract additional costs, to compensate the provider.

#### Other order types $4.5$

In addition to the default market and limit order types, there are a wide range of other orders available across the various execution venues. Table 4-3 summarises these, classified by function:

| Class            | Order types                                     |
|------------------|-------------------------------------------------|
| Standard         | Market, Limit                                   |
| Hybrid           | Market-to-limit, Market-with-protection         |
| Conditional      | Stop, Trailing stop, Contingent, Tick sensitive |
| Hidden           | Hidden, Iceberg / reserve                       |
| Discretional     | Not-held, Discretionary, Pegged                 |
| Routed           | Pass-through, Routing-strategy                  |
| Crossing         | Uncommitted, Negotiated, Alerted                |
| Order-contingent | Linked-alternatives, Contingent, Implied        |

#### **Table 4-3 Order type classifications**

The hybrid, conditional, hidden and discretional order types are common across many venues. Regulation and the proliferation of new venues means that routed order types are also becoming more common. The success of "dark pools" has also led many exchanges to offer more specialised crossing orders, in order to compete. Finally, order contingent orders are less common and tend to be reasonably venue specific. In the following sections, we will go through each class in turn, examining the associated order types in more detail.

# Hybrid order types

In many ways, market orders and limit orders represent different ends of the spectrum. Market orders offer immediacy but cannot guarantee the execution price, whilst limit orders offer price control but their execution is uncertain. Hybrid orders use a variety of mechanisms to try to offer the best of both limit and market orders.

## Market-to-limit orders

Market-to-limit orders are indeed a hybrid: a market order with a strong implicit price limit. When the order first arrives, it behaves like a market order, seeking liquidity at the hest available price, which then becomes its price limit. Unlike a traditional market order, it will not just sweep the order hook, instead if there is insufficient liquidity available at the best price it will convert into a standing limit order for the residual amount.

For example, if we issue a market-to-limit order to buy 2,000 ABC, as shown in Figure 4-12, the initial market order will immediately cross with the order S1. This price now becomes the order's price limit; therefore, it is unable to cross with order S2. Thus, a partial fill of 1,000 at 101 is achieved and the order now converts to a limit order at this last executed price, as shown in Figure  $4{\text -}12(c)$  as order B4.

|               |         | Buys  |       | Sells |       |         |    |  |  |  |
|---------------|---------|-------|-------|-------|-------|---------|----|--|--|--|
| Id            | Time    | Size  | Price | Price | Size  | Time    | ſd |  |  |  |
| $\mathbf{B1}$ | 8:25:10 | 1,200 | 100   | 101   | 1,000 | 8:25:00 | SI |  |  |  |
| B2            | 8:20:15 | 800   | 99    | 102   | 1,500 | 8:20:25 | S2 |  |  |  |
| B3            | 8:24:10 | 2,100 | 98    | 103   | 700   | 8:24:09 | S3 |  |  |  |
|               |         |       |       |       |       |         |    |  |  |  |

Sells Price Size  $\text{Id}$ 1,000 \$1 101 102 1.500  $S2$ 700 S3 103

(b) MO crosses

(a) hefore

|             |         | Buys  |       |       | Sells |         |             |
|-------------|---------|-------|-------|-------|-------|---------|-------------|
| ld          | Time    | Size  | Pricc | Price | Size  | Time    | ld          |
| $\text{B4}$ | 8:28:00 | 1,000 | 10t   | 101   | 1.000 | 8:25:00 | $\text{S}1$ |
| $\text{B1}$ | 8:25:10 | 1,200 | 100   | 102   | 1,500 | 8:20:25 | S2          |
| B2          | 8:20:15 | 800   | 99    | 103   | 700   | 8:24:09 | S3          |
| B3          | 8:24:10 | 2.100 | 98    |       |       |         |             |

(c) after

# Figure 4-12 The effect of a market to limit order on the order book

Admittedly, a marketable limit order priced at 101 would have achieved the same thing. But what if the owner of order S1 suddenly cancelled their order just before our market to limit order was processed?

Using a marketable limit order at 101 we would fail to match with order S2, and so remain in full on the order book. Conversely, a market order would have executed with both orders S2 and S3 completing with an average price of 102.25. In comparison, our market-to-limit order would have crossed with order S2 resulting in executing 1,500 at 102 and leaving the residual 500 as a limit order to buy at 102.

Hence, market-to-limit orders offer a middle ground between market orders and marketable fill orders. Their initial market order behaviour means that they offer more certainty of execution than a marketable limit order, but slightly less certainty of the execution price.

#### Market-with-protection orders

A market-with-protection order offers the immediacy of a market order together with the protection of an inbuilt price limit. Effectively, it is an extension of the market-to-limit order with a limit price further away from the last execution price.

For example, let's issue a market-with-protection order to buy 3,500 ABC as shown in Figure 4-13. We will assume the price limit equates to 103, so our market order can cross with orders S1, S2 and S3. Since order S4 is priced at 104 we are unable to cross and so the residual 500 is left on the order book as limit order B1 with a limit price of 103.

Market-with-protection orders help to ensure that execution is not achieved at any cost. Provided that a reasonable protection limit is set, they strike a balance between certainty of execution and certainty of price.

Note for the CME all market orders are actually implemented as market-with-protection orders. The price limit is calculated for buy orders by adding predefined protection points to the best offer, whilst for sells they are subtracted from the best bid. The protection points are equal to half of the asset's "no-bust range".<sup>1</sup>

<sup>&</sup>lt;sup>1</sup> The no-bust range is a limit intended to protect market participants, within this range orders may not be cancelled.

## Orders

| Buys               |       | Sells |       |         |             |  |
|--------------------|-------|-------|-------|---------|-------------|--|
| Time<br>Size<br>Id | Price | Price | Size  | Time    | $\text{Id}$ |  |
| 8:25:00<br>1,000   | 100   | 101   | 1,000 | 8:25:00 | S1          |  |
| 8:20:25<br>900     | 100   | 102   | 1,500 | 8:09:25 | S2          |  |
| 8:21:00<br>2,000   | 99    | 103   | 500   | 8:14:09 | S3          |  |
| 8:22:00<br>1,500   | 99    | 104   | 1,000 | 8:16:00 | S4          |  |
| 8:14:00<br>800     | 98    | 105   | 1,300 | 8:13:00 | S5          |  |

Sells Price Size 1d 101 1.000 S1 102 1,500 \$2 S3 103 500 104 1,000  $S4$ 105 1.300 S5

(a) before

(b) MO crosses

|         |       |       | Sells |       |         |             |  |
|---------|-------|-------|-------|-------|---------|-------------|--|
| Time    | Size  | Price | Price | Size  | Time    | $\text{ld}$ |  |
| 8:28:00 | 500   | t03   | 104   | 1,000 | 8:16:00 | S4          |  |
| 8:25:00 | 1,000 | 100   | 105   | 1.300 | 8:13:00 | S5          |  |
| 8:20:25 | 900   | 100   |       |       |         |             |  |
| 8:21:00 | 2,000 | 99    |       |       |         |             |  |
|         |       | Buys  |       |       |         |             |  |

(c) after

# **Conditional order types**

Conditional orders base their validity on a set condition, often the market price. Only when the condition is met will it result in an actual order being placed. Thus, stops and contingent orders only become active when a threshold price is breached. Trailing stop orders are similar, although they use a dynamic threshold. Finally, tick-sensitive orders base their validity by comparing the current best price with the last traded price.

## **Stop orders**

Slop orders are contingent on an activation (or stop) price. Once the market price reaches or passes this point, they are transformed into active market orders. In continuous trading, the price being tracked is generally the last traded price,  $2$  whilst in an auction it is usually the clearing price. Activation occurs for buys when the market price hits the stop price or moves above, whilst for sells it is when the market price hits or moves below the stop.

![](_page_15_Figure_12.jpeg)

Figure 4-14 An example sell stop order

 $^{2}$  On some exchanges, e.g. the CME, the stop price tracks the market bid and offer as well as the last traded price.

Stops are sometimes also referred to as stop-loss orders. Since as sells (buys) they are generally used as a safety net to protect profits, by closing out long (short) positions should the market move against us, as we can see in Figure 4-14. So, for example, let's assume a long position was initiated at 92; once the price reaches 93 a stop sell order is placed (at 93) as protection. If the price trend reverts at time t, as shown in pathway (a), then the stop will be triggered. Alternatively, if the price continues to trend favourably (b) the stop will remain inactive.

Note that the market order generated by a stop gives no guarantees on the price achieved. This is important since the very nature of stops means that they are only activated when the market price becomes unfavourable. They offer the lesser of two evils; a poor price may be achieved, but if the market does not revert, the alternative is even worse.

Stop limit orders replace the market order with a limit order. The stop price activates the order, whilst the limit price controls the triggered order. Although this offers some price protection by controlling the price of the triggered order, it also introduces a risk of failing to execute. Unfortunately, fast market conditions often heighten this risk.

The market-with-protection order type acts as a halfway house between market orders and a limit orders. Stop orders with protection use this order type to increase the probability of execution whilst still having a limit for some price control. The limit price is based on the stop price and the specified protection limit. Nevertheless, it is still fundamentally a limit order, so if the price shifts are severe enough to breach the protection limit then the position will remain exposed.

Therefore, if closing out of a position is a must then there is no real choice other than by using a pure stop order. It may also be worth considering other means of hedging the position, such as with options or futures.

Whilst stop orders are a useful tool, they can also have considerable market impact, in particular when the market is at its most vulnerable. Upon activation, all stop orders tend to accelerate the price trend that triggered them. For instance, a sell stop order is trying to sell when there has already been a significant fall in the price. Such a drop is most likely due to an imbalance between the order book volume to buy and sell. The stop order is effectively looking for liquidity when it has already decreased. If it manages to execute then the imbalance will be even greater.

#### Trailing stop orders

A stop order uses an absolute stop price, whereas for a trailing stop order the stop price follows (or pegs) favourable moves in the market price. A trailing offset is either specified as

![](_page_16_Figure_9.jpeg)

Figure 4-15 The price latching behaviour of a trailing stop order

an actual amount or sometimes as a percentage change. For a sell order, as the market price rises the trailing stop price will rise by a similar amount. However, when the market price falls the stop price does not change, as shown in Figure 4-15. Once the market price becomes less favourable, the stop price remains fixed until the market price actually reaches the stop and triggers it. The order then behaves exactly like a stop order or a stop limit order. This price latching mechanism allows profits to be locked-in without having to try to predict the best price level to set the stop at.

## Contingent / if-touched orders

Contingent, or if-touched, orders are effectively the opposite of stops. For foreign exchange, they are sometimes called entry orders since they are generally used to establish positions.

As with stops, there are two main types, a market if-touched order and a limit if-touched. Note that a limit if-touched order is similar to a standing limit order, except that is hidden from the order book until activated.

Their operation is extremely similar to stops; both remain hidden until the market price moves sufficiently to activate them, whereupon they create a corresponding order. But the activation logic is the reverse of that for stops. So a buy if-touched order is triggered when the market price hits the target price or moves below, whilst a sell triggers when the market price hits the target or moves above.

Some venues even allow if-touched orders that are contingent on the price of a completely different asset, such as a stock index.

## **Tick sensitive orders**

Tick-sensitive instructions introduce a validity condition based on the last traded price. If the current price is the same as the last trade it is referred to as a zero tick, above it is an up tick and below is a downtick. (Note zero ticks may be further classified as zero up and downticks by comparing with the last different trade price).

Thus, a buy downtick order may only be crossed on a downtick or zero downtick price. Likewise, a sell up tick order may only be crossed on an up tick or a zero uptick. Larry Harris (1999) points out that tick sensitive orders are essentially limit orders with dynamically adjusting limit prices. Tick sensitive orders employ a similar price latching mechanism to trailing stops; a downtick order will raise its dynamic limit price only when the price increases, whilst an uptick order will only decrease its limit when the price falls.

Tick sensitive orders have no immediate market impact. The tick dependency means that immediacy is sacrificed in order to obtain a price one tick better. Harris observes that they are therefore most useful when the tick size is large. In fact, the decimalisation of the U.S. stock markets in 2000 actually reduced the appeal of tick dependency, since it meant that for most stocks the tick size decreased from a sixteenth to just 1 cent.

Tick dependent orders exist mainly because of regulation, in part to try to curb the downward price momentum due to hidden stop orders being triggered. Consequently, some venues enforce a rule that short sales must be on an uptick. In other words, an uncovered sale is only allowed when the current price is above the last traded price.

## Hidden order types

Efficient markets need to satisfy the needs of a range of users. Whilst transparency allows traders to easily see the available supply and demand, it poses problems for large orders. Many markets and venues provide hidden order types that allow traders to work larger orders without attracting undue attention. This ensures that liquidity remains available at the execution venue, rather than shifting to an alternative liquidity pool or crossing network.

A few years ago, completely hidden orders had all but been phased out. Hidden orders were viewed to increase the uncertainty of execution, and so affect the quality of price formation. They were also thought to act as a disincentive for placing limit orders, possibly leading to increased spreads. Transparency was viewed as being more important, and so venues, such as Euronext and the ASX, switched to providing iceberg orders instead. These offer a reasonable compromise, since a portion of the order is still visible. Still, the success of ATS venues providing "dark pools" of liquidity has led to resurgence in the popularity of hidden orders. Indeed exchanges, such as NASDAQ, AMEX and NYSE's Arca, are now introducing hidden orders in order to retain their liquidity and to compete with the ATSs.

#### Hidden orders

Hidden, undisclosed or non-displayed orders allow traders to participate without giving away their position. For example, Figure 4-16(a) shows the order book before a market order to buy 1,000 ABC arrives. Afterwards we can see that the order book has not changed as much as we might have expected. From the subsequent trade reports, we can see that 1,000 filled at 101, but on the order book we can only see order S1 filled and there were no new incoming orders, so where did the other 500 come from?

|    | Buys       |       |       |       | Sells |         |             |  | Sells     |       |     |
|----|------------|-------|-------|-------|-------|---------|-------------|--|-----------|-------|-----|
| 1d | Time       | Size  | Price | Price | Size  | Time    | $\text{1d}$ |  | Price     | Size  | 1d  |
|    | 8:25:00    | 1,000 | 100   | 101   | 500   | 8:20:00 | S1          |  | 101       | 500   | \$1 |
|    | 8:20:25    | 900   | 99    | 102   | 1,000 | 8:22:25 | S2          |  | 102       | 1.000 | S2  |
|    | 8:24:09    | 1,400 | 98    | 102   | 800   | 8:24:09 | S3          |  | 102       | 800   | S3  |
|    | 8:24:20    | 2,000 | 97    | 102   | 1,500 | 8:25:00 | S4          |  | 102       | 1.500 | S4  |
|    | (a) before |       |       |       |       |         |             |  | (b) after |       |     |

(a) before

Figure 4-16 A hidden order?

There may be hidden volume available at 101, or it may have all been consumed. The only way to know is to see the result of the next buy order. Hence the popularity of "liquidity pinging" using IOC orders. By issuing an IOC limit order to buy 1,000 at 101 we can try to cross with any hidden orders. That said, other participants are likely to have the same idea, so it is a question of speed of response.

One important consideration when using hidden orders is that they are usually given lower priority than visible orders. Otherwise, everyone would simply use hidden orders, making it much harder to determine the market price.

As hidden orders become more popular again there will doubtless be new variations. For instance, the London stock exchange is planning on supporting minimum order sizes, which should offer some protection from small liquidity-seeking orders.

#### Iceberg / reserve orders

As its name suggests, an iceberg order comprises of a small visible peak and a significantly larger hidden volume. The peak (or display) size is configurable, although some venues stipulate a minimum, often a percentage of the normal market size (NMS). The visible portion of the order is indistinguishable from any other limit order. Each time this displayed order is fully executed the venue's trading system splits a new order from the hidden volume, until the whole iceberg order is completed. Therefore, each displayed order has normal time priority within the order book whilst the hidden volume just has price priority. teeberg orders are also sometimes called reserve orders or drip orders.

For example, if we look at Figure 4-17(a), we can see sell order S1 for 1,000 at 101. This is actually the display size of the iceberg order H1 that has another 9,000 hidden volume. Obviously, the hidden volume is not actually visible on the order book, but just for these examples it shown (in light grey) to emphasize that it still has price priority in the order book. Thus, order S3 will not manage to cross with any other orders until our hidden volume H1 is exhausted.

| Buys       |       |       | Sells |         |     |           |       | Sells   |             |
|------------|-------|-------|-------|---------|-----|-----------|-------|---------|-------------|
| Size       | Price | Pricc | Size  | Time    | ld  | Price     | Size  | Time    | 1d          |
| 1,000      | 100   | 101   | 1,000 | 8:20:00 | S1  | 101       | 1,000 | 8:20:00 | $\text{S}1$ |
| 900        | 99    | 101   | 1,000 | 8:21:25 | S2  | 101       | 500   | 8:21:25 | \$2         |
| 1,500      | 98    | i0i   | 9,000 | 8:10:09 | III | 101       | 500   | 8:21:25 | S2          |
|            |       | 102   | 1,500 | 8:24:09 | S3  | 101       | 1.000 | 8:27:00 | S4          |
|            |       |       |       |         |     | 101       | 8,000 | 8:10:09 | 111         |
|            |       |       |       |         |     | 102       | 1,500 | 8:24:09 | S3          |
| (a) helore |       |       |       |         |     | (h) oftar |       |         |             |

(a) before

 $(b)$  after

## Figure 4-17 Crossing with the display portion of an iceberg order

When a market order to buy 1,500 ABC hits the order book:

- Our iceberg's displayed order S1 immediately crosses with it for 1,000
- Next, the remaining 500 is filled by partially crossing with order S2.  $\bullet$
- Since our displayed order is completed, a new order is split from the hidden ٠ quantity as sell S4.

Continuing this example with a second market order to buy another 2,200 ABC, is shown in Figure 4-18.

| Buys       |       |       |         | Sells   |    |                                                             |       | Sells   |     |
|------------|-------|-------|---------|---------|----|-------------------------------------------------------------|-------|---------|-----|
| Size       | Price | Price | Size    | Time    | ld | Price                                                       | Size  | Time    | ld  |
| 1,000      | 100   | 101   | 500     | 8:21:25 | S2 | 101                                                         | 500   | 8:21:25 | S2  |
| 900        | 99    | 101   | 1,000   | 8:27:00 | S4 | 101                                                         | 1,000 | 8:27:00 | \$4 |
| 1,500      | 98    | 101   | 8. OOKA | 8:10:09 | HI | 101                                                         | 700   | 8:28:09 | \$5 |
|            |       | 102   | 1,500   | 8:24:09 | S3 | 101                                                         | 300   | 8:28:09 | S5  |
|            |       |       |         |         |    | 101                                                         | 7,000 | 8:10:09 | III |
|            |       |       |         |         |    | 102                                                         | 1,500 | 8:24:09 | S3  |
| (a) bafama |       |       |         |         |    | $\langle 1, \mathcal{N} \rangle = \mathcal{L}_{\text{max}}$ |       |         |     |

(a) before

(b) after

## Figure 4-18 Another crossing with the iceberg order

So we can see that:

- The remaining 500 of order S2 is immediately executed.
- The 1,000 from our iceberg's order S4 is also filled.
- A new order S5 for another 1,000 is split from our hidden volume H1.
- The remaining 700 of the market order is filled from the newly created order S5 that has price priority over order S3.

The meehanism is just the same if we have multiple iceberg orders on the order book. For instance, let's consider the order book shown in Figure 4-19 which has two iceberg orders.

| Buys     |       |       |       | Sells   |             |   |                               |       |         |     | Sells |  |  |  |
|----------|-------|-------|-------|---------|-------------|---|-------------------------------|-------|---------|-----|-------|--|--|--|
| Size     | Price | Priee | Size  | Time    | $\text{Id}$ |   | Price                         | Size  | Time    | 1d  |       |  |  |  |
| 1,000    | 100   | 10t   | 1,000 | 8:20:25 | S1          |   | 101                           | 1,000 | 8:20:25 | St  |       |  |  |  |
| 900      | 99    | 101   | 500   | 8:21:25 | S2          |   | 101                           | 500   | 8:21:25 | \$2 |       |  |  |  |
| 1,200    | 98    | 101   | 1,500 | 8:23:00 | S3          |   | 101                           | 1,500 | 8:23:00 | \$3 |       |  |  |  |
|          |       | 101   | 6.000 | 8:20:09 | HI          | ٠ | 101                           | 200   | 8:25:02 | \$5 |       |  |  |  |
|          |       | 101   | 9,000 | 8:23:00 | 112         |   | 101                           | 800   | 8:25:02 | \$5 |       |  |  |  |
|          |       | 102   | 1,800 | 8:24:10 | S4          |   | 101                           | 1,500 | 8:25:02 | S6  |       |  |  |  |
|          |       |       |       |         |             |   | 101                           | 5,000 | 8:20:09 | 111 |       |  |  |  |
|          |       |       |       |         |             |   | 101                           | 7,500 | 8:23:00 | 112 |       |  |  |  |
|          |       |       |       |         |             |   | 102                           | 1,800 | 8:24:10 | S4  |       |  |  |  |
| $\sim 1$ |       |       |       |         |             |   | $\langle 1 \rangle$ - $C_1$ - |       |         |     |       |  |  |  |

(a) before

(b) after

Figure 4-19 Crossing with multiple iceberg orders

The first iceberg is currently displaying sell order S1 with a hidden volume H1 of 6,000, whilst the second has a greater hidden volume of 9,000, but it also uses a greater display size of  $1,500$  for its order S3. So when a market order to buy  $3,200$  arrives:

- The first iceberg's order S1 will be completely filled.
- As will standing limit order S2.  $\bullet$
- The second iceberg's displayed order S3 is also filled, leaving 200 remaining on  $\bullet$ the market order.
- New orders S5 and S6 will then be split for each iceberg.
- The last 200 of the market order will be crossed with the first iceberg's newly  $\bullet$ split order S5, since this iceberg has time priority.

This also highlights the importance of the iceberg's display size. Even though the second iceberg H2 has lower time priority, each time it splits a new order it is for 1,500, so it will fill quicker than H1.

These examples have all shown how the hidden volume on the order book participates in the order matching mechanism. This is the key difference between native exchange based iceberg orders and an external order-slicing mechanism, where the hidden volume resides outside the order book. External mechanisms are reliant on receiving execution confirmations to show that the previous order has completed, only then will a new order be created. This may occur some time after the order book crossing has finished, so an external mechanism will not be able to respond in time. Hence, in order to fill the market order the order book will instead cross with other standing limit orders, such as S4 in Figure 4-19. This means that order-slicing approaches may take longer to execute than native iceberg orders. However, it also enables them to have more scope for price improvement; we shall go through this in more detail in Chapter 9.

# Discretional order types

Traditionally, discretional order types afforded the trader more freedom in how a particular order should be worked, since they are the expert. This is perhaps best typified by the Notheld instruction that basically gives the trader carte blanche. Computerisation has resulted in the evolution of more rules-based approaches, such as pegged and discretionary orders. These offer more quantifiable steps, compared to the rather vague "do the best you can".

# Not-held orders

A not-held order gives complete discretion to the trader about how the order is worked.

Generally, these are used for floor traders since in less transparent markets they will have the best knowledge of market conditions. The quality of execution relies on them choosing the best time to trade.

# **Discretionary orders**

A discretionary order is a limit order with a slightly more flexible limit price. The limit that is displayed on the order book may be augmented by an additional amount when conditions are appropriate. For a buy order, the real price limit is actually the limit price plus this discretionary amount, whilst for a sell it is the limit price minus the discretionary. The true limit is taken into account only when a matching order comes within the discretionary range. Therefore, the order may execute at any price between the displayed limit and the true limit. Note that any visible orders will still have priority over the discretionary order.

For example, let's issue a buy limit order for ABC at with a limit of 100 and a discretionary range of 1, as shown by buy B1 in Figure  $4-20(a)$ .

|             |         | Buys  |       | Sells |       |         |    |  |
|-------------|---------|-------|-------|-------|-------|---------|----|--|
| ld          | Time    | Size  | Price | Priee | Size  | Time    | fd |  |
| $\text{B1}$ | 8:25:01 | 1,000 | 100   | 102   | 1,000 | 8:25:00 | St |  |
|             | 8:20:05 | 800   | 99    | 103   | 2,000 | 8:20:25 | S2 |  |
|             | 8:24:00 | 1.200 | 98    | 104   | 900   | 8:24:09 |    |  |
|             |         |       |       |       |       |         |    |  |

(a) before

|                         |         | Buys  |       |       | Sells  |         |     |
|-------------------------|---------|-------|-------|-------|--------|---------|-----|
| ld                      | Time    | Size  | Price | Price | Size   | Time    | ld  |
| $\text{B1}$             | 8:25:01 | 500   | 101   | 101   | $-500$ | 8:28:00 | \$4 |
| $\mathbf{B} \mathbf{1}$ | 8:29:00 | 500   | 100   | 102   | 1,000  | 8:25:00 | S1  |
|                         | 8:20:05 | 800   | 99    | 103   | 2,000  | 8:20:25 | S2  |
|                         | 8:24:00 | 1,200 | 98    | 104   | 900    | 8:24:09 |     |

(b) after

### Figure 4-20 The effect of a discretionary order on the order book

Initially, there is no order that can immediately be crossed, so order B1 simply rests on the order book with a visible limit price of 100. When sell order S4 is added at a price of 101, this is now within our discretionary range. So we can match this. The remaining 500 for order B1 remains on the order book, still with a visible limit of 100.

Some venues, such as NASDAQ and NYSE Area, support a minimum quantity as well, so that the discretionary order will only stretch its price limit for orders above this size.

#### Pegged orders

Pegged orders provide a dynamic limit price; therefore, they can help reduce the inherent miss-pricing risk of standing limit orders. A pegged order's limit price may track the best bid, offer or even mid price, applying an additional offset amount. For instance, Figure 4-21 shows the trajectory of a pegged limit order tracking the best bid price. A firm price limit may still be applied which will prevent the order pegging beyond this limit.

For example, let's issue a buy limit order for ABC pegging from the best bid with an offset of 1. Initially, our order B2 will be placed with a limit of 99, I away from the current best bid, as shown in Figure 4-22(a). When a new order B4 joins the book, the best bid moves up to 101, so in response our order is updated with a new limit of 100 to keep pace

![](_page_22_Figure_1.jpeg)

Figure 4-21 Pegging the best bid price

|    | Buys    |       | Sells |       |       |
|----|---------|-------|-------|-------|-------|
| ĺd | Time    | Size  | Price | Price | Size  |
| BI | 8:20:00 | 1,000 | 100   | 102   | 900   |
| B2 | 8:25:25 | 1,200 | 99    | 103   | 1,000 |
| B3 | 8:24:09 | 800   | 98    | 104   | 1,500 |

|               | Buys    |       |       |  |
|---------------|---------|-------|-------|--|
| ld            | Time    | Size  | Price |  |
|               | 8:27:00 | 500   | 101   |  |
| $\text{B}1$   | 8:20:00 | 1,000 | 100   |  |
|               |         | .200  |       |  |
| $\mathbf{B3}$ | 8:24:09 | 800   | 98    |  |

(b) spread narrows

(a) before

|               |         | Buys  |       | Sells |       |         |    |  |  |
|---------------|---------|-------|-------|-------|-------|---------|----|--|--|
| 1d            | Time    | Size  | Price | Price | Size  | Time    | ld |  |  |
| B4            | 8:27:00 | 500   | 101   | 102   | 900   | 8:28:00 |    |  |  |
| $\mathbf{B1}$ | 8:20:00 | 1.000 | 100   | 103   | 1,000 | 8:25:00 |    |  |  |
| B2            | 8:27:25 | .200  | 100   | 104   | 1.500 | 8:20:25 |    |  |  |
| B3            | 8:24:09 | 800   | 98    |       |       |         |    |  |  |
| $\sim$        |         |       |       |       |       |         |    |  |  |

(c) after

# Figure 4-22 The effect of a pegged order on the order book

with the best bid.

As for discretionary orders, some venues, such as NYSE, support a minimum quantity, so that pegging is not triggered by small orders. Instinet even offers pegged order types that can have an associated display size, just like an iceberg order.

# Scale orders

These may be used to layer child orders throughout the order book at a range of price levels.

|               |         | Buys  |       | Sells |       |         |    |  |
|---------------|---------|-------|-------|-------|-------|---------|----|--|
| ld            | Time    | Size  | Price | Price | Size  | Time    | ld |  |
| B5            | 8:25:00 | 900   | 100   | 101   | 1.000 | 8:24:20 | S3 |  |
| B2            | 8:20:25 | 1,500 | 99    | 101   | 800   | 8:25:00 | S5 |  |
| B4            | 8:24:09 | 2,000 | 98    | 102   | 1,200 | 8:24:25 | S4 |  |
| $\mathbf{B}1$ | 8:20:25 | 1,200 | 97    | t02   | 2,000 | 8:24:20 | S2 |  |
| B3            | 8:24:00 | 700   | 97    | 103   | 1,000 | 8:24:20 | SI |  |

|  |  |  | Figure 4-23 An example set of scale orders |  |  |  |  |
|--|--|--|--------------------------------------------|--|--|--|--|
|--|--|--|--------------------------------------------|--|--|--|--|

For instance, we might specify a sell order for 4,000 ABC, scaled with 25% at 101, 50% at 102 and 25% at 103, as shown in Figure 4-23. Alternatively, set amounts may be specified for the various price levels. In a fast moving market, this approach has the advantage that our orders are already in place, and so receive time priority. But if the price keeps trending favourably, better prices might be achieved by waiting. We will revisit these layering tactics in Chapter 9.

## Routed order types

Routed order types are becoming more and more common; they can be an important means of seeking additional liquidity in today's increasingly fragmented markets.

As we have already seen, there are order instructions that cater for routing, allowing orders to be sent to specific venues or to stay at a single venue. The natural progression is increasingly complex order routing strategies, leading to "smart order routing". The simplest of which is represented by pass-through orders. These allow liquidity to be accessed from two venues. There is also a range of strategies allowing routing back and forth between venues, and even participating in special sessions such as the opening auction. As these continue to evolve, the line between them and trading algorithms is becoming increasingly blurred.

## **Pass-through orders**

As their name suggests, pass-through orders allow an order to initially pass-through the hosting venue on the way to their ultimate destination, often the primary exchange. Effectively, they act like two sequential orders, an IOC order at the initial host venue followed by an order for the remainder sent to the destination venue.

This allows an order to consume liquidity from the hosted order book before routing any residual to the chosen destination. In comparison, a standard limit order that sweeps the order book will just leave any remainder as a standing order. Therefore, they are typically provided by crossing networks or venues seeking to attract additional liquidity.

For example, let's consider an order to sell 1,500 of asset ABC at 100. Figure 4-24 shows the order books for both the ECN (ECN-1) and the primary exchange (Exch-1).

|                 |       |       |       | $ECN-1$ |  |             |       |       |       | ECN-1           |  |
|-----------------|-------|-------|-------|---------|--|-------------|-------|-------|-------|-----------------|--|
| Buys            |       | Sells |       |         |  |             | Buys  |       | Sells |                 |  |
| Size            | Price | Price | Size  | Id      |  | Size        | Price | Price | Size  | 1d              |  |
| 500             | 100   | 101   | 1,200 | SI      |  | 500         | 100   | 101   | 1,200 | St              |  |
| 1,000           | 99    | t02   | 900   | S2      |  | 1,000       | 99    | 102   | 900   | S2              |  |
| 800             | 98    | 102   | 1,500 | S3      |  | 800         | 98    | 102   | 1,500 | S3              |  |
| $\text{Exch-1}$ |       |       |       |         |  |             |       |       |       | $\text{Exch-1}$ |  |
| Buys            |       | Sells |       |         |  |             | Buys  |       | Sells |                 |  |
| Size            | Price | Price | Size  | Id      |  | Size        | Price | Price | Size  | td              |  |
| 1,000           | 99    | 101   | 800   | S1      |  | 1.000       | 99    | 100   | 1,000 | S4              |  |
| 900             | 99    | 102   | 1,500 | S2      |  | 900         | 99    | 101   | 800   | S1              |  |
| 1,400           | 98    | 102   | 2,000 | S3      |  | 1,400       | 98    | 102   | 1,500 | S2              |  |
|                 |       |       |       |         |  |             |       | 102   | 2,000 | S3              |  |
| (a) before      |       |       |       |         |  | $(h)$ after |       |       |       |                 |  |

#### Figure 4-24 An example pass-through order

We can see from Figure  $4-24(a)$  that there are 500 available at ECN-1. Hence, we can

issue a pass-through order, which will try to cross with the liquidity available at ECN-1 before routing to the primary exchange, Exch-1. Having consumed the available liquidity at 100, our order will now become a standing limit order S4 at Exch-1.

Although Figure 4-24 shows an example of routing between two visible order books, it does not take a huge leap of imagination to replace ECN-1 with a "dark pool" ATS. When placing our sell order we can no longer see what liquidity is available, but we know it will try to cross before routing to the primary exchange, Exch-1. This is quite a convenient way of providing additional liquidity for the ATS. Typically, ATSs have been keen to have brokers route retail flow through in this way since there is less chance of information leakage.

#### Routing-strategy orders

Routing-strategy orders extend the straightforward concept of pass-through orders to allow more complex routing instructions. These may enable orders to participate in auctions, or be routed to additional venues before reaching their final destination. For example, Table 4-4 shows some of the routing strategies offered by NASDAQ.

| Name | Strategy                                                     |
|------|--------------------------------------------------------------|
| MOPP | Route to all protected quotes for display size only          |
|      | Post any residual on NASDAQ                                  |
|      | Sweep NASDAQ for NBBO or better                              |
| DOTI | Route any residual to NYSE or AMEX                           |
|      | Sweep NASDAQ for NBBO or better                              |
| SKIP | Route to Reg NMS protected venues                            |
|      | Post any residual on NASDAQ                                  |
|      | Sweep NASDAQ for NBBO or better                              |
| SCAN | Route to alternate execution venues                          |
|      | Post any residual on NASDAQ                                  |
|      | As SCAN                                                      |
| STGY | Residual will route if NASDAQ subsequently locked or crossed |

Source: NASDAQ (2008a)

## Table 4-4 Example NASDAQ routing strategies

The MOPP strategy takes advantage of liquidity visible at other venues by routing to access the Regulation NMS (Reg NMS) protected quotes for their displayed size. Any residual amount is then posted on the NASDAQ order book.

In comparison, the DOTI strategy first sweeps the NASDAQ order book, trying to beat or match the national best bid and offer (NBBO). It then routes the any residual amount on to either NYSE or AMEX. Note that once the order reaches its final destination, it will remain there until it is completely filled or cancelled.

The SKIP strategy extends the DOTI approach by being able to route the residual to any of the venues that offer Reg NMS protected quotes. After this routing, the SKIP strategy finally posts any remainder on NASDAQ.

The SCAN strategy takes a similar approach to SKIP, first sweeping NASDAQ then routing the residual. The list of possible destinations for the residual is even wider than for SKIP since it also includes a range of alternative venues. The STGY strategy is based on similar rules to SCAN; although, it will re-route the residual order if the NASDAQ order book subsequently becomes locked or crossed.

More strategies are also based on these. For instance, DOTM behaves similarly to STGY; although it requires orders to be non-attributable and accepts on-open and on-close orders.

Other venues have their own specific order routing strategies, but the above examples give an idea of what is commonly offered. No doubt, other innovative strategies will develop over time.

# Crossing order types

Many venues already provide orders allowing traders to report off order hook crosses. New order types are also being introduced to allow crossing to actually take place on the order book. These have become increasingly important as venues compete for "dark pool" liquidity. A nice summary of the order types and flows is provided by Gabriel Butler's (2007) review of crossing networks. He classifies the available order types as:

- Committed orders, firm orders available for immediate execution
- $\bullet$ Uncommitted orders, requiring confirmation before execution
- $\bullet$ Negotiated orders
- Pass-through orders, routed on their way to another venue .

As we saw in Chapters 2 and 3, crossing networks vary widely in their actual mechanisms. These types are not supported by every venue; however, they encompass most of the various kinds of mechanism that are available.

Committed orders are essentially just standard market or limit orders. Uncommitted orders are similar to indications of interest (IOIs), whilst negotiated orders provide a bilateral trading mechanism. As we have already seen, pass-through orders act as a means of providing additional liquidity for crossing. Note an indication of interest (IOI) is a nonbinding interest in buying (or selling) an asset. These may be sent between the buy-side and sell-side to discover interested counterparties.

There is one additional order type worth mentioning, that is the alerted order. Venues may also use indications to advertise the availability of liquidity. Some even provide separate order types, allowing traders and investors to choose whether they wish to use this mechanism.

## Uncommitted orders

Uncommitted orders are similar to indications of interest (IOIs) combined with a mechanism which enables them to convert to firm orders. They are also sometimes referred to as conditional orders, such as on BIDS.

Uncommitted orders can cross with each other or with firm orders. If a potential cross is discovered, the owner will be sent a notification, at which point they can then decide whether to convert them to a firm order. This allows investors/traders to leave an uncommitted order on the crossing network whilst they try to work the same order on other venues, knowing that they will not get any unexpected fills.

Some venues also allow additional sensitivity parameters, which may be used to specify discretionary price/volume limits at which we may be prepared to trade. These are incorporated into the matching logic, so when a notification is received for a potential match a structured negotiation can take place.

When firm orders are being matched with uncommitted ones, it is important to also provide some protection for the owner of the firm order. To ensure fairness, and prevent predatory trading, a reasonably large minimum order size is often required for uncommitted orders. BIDS also uses its scorecard mechanism to ensure that both participants have a sufficient success rate from prior crossings. Otherwise, predatory traders could simply "ping" for liquidity using uncommitted orders.

#### **Negotiated orders**

Negotiated orders are used by venues to provide a structured negotiation environment. Essentially, they provide a bilateral trading mechanism, as we saw in Chapter 2. Each counterparty has an idea of the price and size they are prepared to trade at, so they must simply alter these until they both agree a deal. Alternatively, they can just walk away since there is no obligation to trade.

One of the interesting things about crossing networks is that the negotiation is anonymous. Both participants may be investors, or one may be a liquidity provider. A common solution is to allow the participants to be able to gauge each other, by providing them with a scorecard that shows the historical success rate of their previous crossings.

#### Alerted orders

These orders use indications, or alerts, to try to improve the probability of execution by broadcasting a message that notifies other market participants of interest in a particular asset. This is particularly important for "dark pool" crossing networks where the order book is completely invisible.

For example, the Millennium ATS has an opt-in Plus order type which triggers an alert to their Liquidity Partners (PLPs). These represent a mix of buy-side institutions, other "dark pool" ATSs and broker internalization engines. Note that this process is fully automated, so the alerts are not visible to traders. The PLPs must therefore use automated systems to respond to any alerts, detailing their available liquidity to Millennium, which then looks for any matches. If a match is found, the corresponding PLP must then reply with a firm order.

The ISE also provides an advertised order, which it calls a Solicitation of Interest. This activates a block trading mechanism that notifies the exchange members of the asset's ticker symbol. They may then enter responses that detail the price and size at which they are willing to trade with a block order. At the end of this period (10 seconds), any orders that are priced better than the block execution price will execute. Priority is given first to orders on the exchange, then member responses and non-customer orders.

## Order-contingent order types

Orders can easily be linked together, as we saw using linking instructions. Venues often use these to allow orders to either cancel or even trigger another order. Order-contingent orders extend this concept by allowing orders to adjust their price and/or size, based on other orders. In the case of linked-alternative orders, they adjust their size based on how much the other alternative orders have filled. Contingent and implied orders vary their price and size based on the best market quotes and a predetermined spread. Contingent orders also enforce an execution dependency to make certain they are all fully executed.

## Linked-alternative orders

This relatively uncommon order type allows a list of alternative orders to be linked so that if one order receives fills then the other orders will be reduced by an equivalent amount. Effectively, it enables simultaneous trading of assets ABC or DEF or HIJ, so this order type is sometimes referred to as linked or "OR" orders. Obviously, one of the main precautions when handling such orders is to ensure that several of the grouped orders do not simultaneously fill, potentially causing an over-fill.

| Asset      | Side | Original<br>Size | Extant<br>size | Filled |
|------------|------|------------------|----------------|--------|
| KLM        | Buy  | 1,000            | 1,000          |        |
| NOP        | Buy  | 3,000            | 3,000          |        |
| ORS        | Buy  | 800              | 800            |        |
| TUV        | Buy  | 2,000            | 2,000          |        |
| (a) before |      |                  |                |        |

For example, in Figure  $4-25(a)$  a sample set of linked orders is shown. When we receive a fill of 500 for our KLM buy we have effectively 50% completed our order.

| size      | Filled |
|-----------|--------|
| 500       | 500    |
| .500      | 0      |
| 400       | 0      |
| 1.000     | (      |
| (b) after |        |

Extant ......

Figure 4-25 An example set of linked alternative orders

Hence, the extant order sizes for the other linked orders are all reduced to 50%, as we can see in Figure 4-25(b). The SAXESS platform, used by some of the Nordic exchanges, can link up to 8 orders in this way.

#### **Contingent orders**

Some venues allow even more dynamic linking between orders spanning multiple assets. Such contingent orders ensure that a match is only possible when all the other dependent orders may also be matched. Typically, this functionality is offered by futures exchanges to support spread trading, whereby simultaneous long and short positions are traded to try to profit from any price differences between two assets. It may also be employed to cater for more complex, multi-leg derivatives trading strategies.

For example, in Figure 4-26(a) we can see the order books for assets JKL and XYZ. Let's assume we wish to buy the spread, and so buy 1,000 JKL whilst selling 1,000 XYZ, but only when the spread reaches -0.2. So we could place a combined order to buy 1,000 JKL and sell 1,000 XYZ with a spread of -0.2.

At present the spread is actually -0.5, since the best offer buy for JKL is 50.8 and the best bid of XYZ is 50.3. So we must use more passively priced limit orders and wait for the spread to narrow, as we can see in Figure 4-26(b). In terms of pricing, our buy order B4 is dependent on the sell order S4, and vice-versa. The price of B4 is based on the best bid for XYZ and the spread, i.e.  $(50.3 - 0.2) = 50.5$ .

| ٠. |  |
|----|--|

| .           |         |       |       |       |       |               |         |       |       |  |
|-------------|---------|-------|-------|-------|-------|---------------|---------|-------|-------|--|
|             | Buvs    |       |       |       | Sells |               | Buvs    |       |       |  |
| Id          | Time    | Size  | Price | Price | Size  | ld            | Time    | Size  | Price |  |
| $\text{B}1$ | 8:24:00 | 1,000 | 50.6  | 50.8  | 1,500 | $\text{B}1$   | 8:24:00 | 1,000 | 50.6  |  |
| B2          | 8:22:25 | 800   | 50.6  | 50.9  | 900   | B2            | 8:22:25 | 800   | 50.6  |  |
| B3          | 8:23:09 | 1.200 | 50.5  | 50.9  | 2,000 | B3            | 8:23:09 | 1.200 | 50.5  |  |
|             |         |       |       |       |       | $\mathbf{B4}$ | 8:26:00 | 1,000 | 50.5  |  |

XYZ

| Buys       |       |       |       | Sells   |    |             |       | Sells   |    |
|------------|-------|-------|-------|---------|----|-------------|-------|---------|----|
| Size       | Price | Price | Size  | Time    | Id | Price       | Size  | Time    | ld |
| 1,000      | 50.3  | 50.5  | 1,000 | 8:25:40 | S1 | 50.5        | 1,000 | 8:25:40 | S1 |
| 600        | 50.3  | 50.6  | 1,200 | 8:21:05 | S2 | 50.6        | 1,200 | 8:21:05 | S2 |
| 1.500      | 50.2  | 50.6  | 700   | 8:22:49 | S3 | 50.6        | 700   | 8:22:49 | S3 |
|            |       |       |       |         |    | 50.6        | .000  | 8:26:00 | S4 |
| (a) before |       |       |       |         |    | $(b)$ after |       |         |    |

Figure 4-26 An example pair of combined orders

Similarly, our sell order S4 is based on the best offer price for JKL, i.e.  $(50.8 + -0.2)$  = 50.6. If one of our orders is matched then the other order will immediately change its price in order to ensure it is filled. So, if B4 can be filled then order S4 will simultaneously re-price to  $50.3$  in order to complete.

Clearly, our orders need to update to adjust to new market prices and sizes to ensure the required spread is maintained. If there is insufficient volume available for one of the assets then the size of the other order must be reduced by a corresponding amount. For example, if the order to buy 1,000 XYZ at 50.3 was suddenly cancelled we would need to change the size for our orders. For more sophisticated handling of such spread orders, we could use pairs trading algorithms, which we shall discuss in more detail in Chapter 5.

## Implied orders

As we saw in the previous section, one way of handling combined orders is to use the current market prices and the desired spread to imply their current price and size. Therefore, real orders are dynamically adjusted to ensure they keep in line with the required spread.

Implied orders represent the next evolution of this approach. Spread trading is so commonplace for futures that many venues allow them to be traded as standalone orders. So we can buy a JUN-SEP spread, just as we might buy or sell the June or September futures contracts. This is usually handled by having separate order books dedicated to spread trading or handling complex strategies. However, over the last few years more and more venues have started to link their standard order books with these complex books. This has allowed the creation of implied orders, which are able to span both types of order book. An implied spread may be derived from the combination of outright orders for different contracts, whilst implied orders may be derived from the combination of spread orders and outright orders.

The importance of such implied trading in futures markets is highlighted in a nice piece by John Blank (2007): In relatively new markets, such as NYMEX energy, up to 44.6% of the trades are achieved via implied trading. Even in mature markets, such as the CME Eurodollars, around 16% of the trading is attributable to implied orders (11.5% of the volume). Consequently, implied orders are an important source of additional liquidity.

Figure 4-27 shows an example of how an implied IN order is created. For simplicity only the orders which create the implied order are shown, namely the buy for the June futures contract (B1) and the sell order for the equivalent September future (S1). Hence, we can sell a June futures contract at 96.5 and buy a September future for 96.0, in other words we can sell the spread for  $(96.5 - 96.0) = 0.5$ . This implies there is a bid of 0.5 available to buy the spread. The size is determined by whichever order is smallest (between orders B1 and S1) and so is 10. As we can see in Figure 4-27, these two orders result in the implied order 11.

| JUN future | Id | Bid size | $\text{Bid}$ | Offer | Offer Size | Id |
|------------|----|----------|--------------|-------|------------|----|
|            | Bl | 10       | 96.50        |       |            |    |
|            |    |          |              |       |            |    |
| SEP future | ſd | Bid size | $\text{Bid}$ | Offer | Offer Size | Id |
|            |    |          |              | 96.00 | 15         | S1 |
| JUN-SEP    | fd | Bid size | $\text{Bid}$ | Offer | Offer Size | ſd |
|            |    |          | 0.50         |       |            |    |

Figure 4-27 Creating an implied IN order

Conversely, a sell order for the June contract will combine with a buy order for the September future to create a JUN-SEP spread offer price and size.

Likewise, by deconstructing a firm spread order into its constituents we can create an implied OUT order. For example, in Figure 4-28 we can see S2, a firm order to sell the SEP-DEC spread at 0.6. By combining this with the firm buy order B1 for the September contract, we can imply the price of a December future. In other words, there must be an equivalent buy order for the December future at  $(95.7-0.6) = 95.1$ , shown as implied order I2.

![](_page_29_Figure_3.jpeg)

Figure 4-28 Creating an implied OUT order

Also notice that there is already a bid (B2) at this price. When matching trades, most venues will assign priority to actual orders, any residual is then matched with the implied orders.

Implied orders may also be combined with actual orders to create second-generation implied orders. So the implied orders I1 and I2 may in turn be used to create other implied spreads or orders.

Butterfly spreads may also be used to create implied orders. These are effectively pairs of spread trades. For example, selling the JUN-SEP-DEC butterfly means selling a JUN-SEP spread and buying a SEP-DEC one. In effect, this results in buying two September contracts and selling both a June and a December one. Again, there is a separate order book dedicated to handling these butterfly spreads, which may in turn be combined with standard orders to create more implied orders. Although complex, this is clearly an effective way of increasing liquidity on the main order book.

#### 4.6 Summary

- Orders are the fundamental building block for any trading strategy.
- щ Orders represent execution instructions. There are two main types:
  - Market orders buy or sell a given quantity at the best price possible. They focus on completing the order with no specific price limit, and so demand liquidity.
  - Limit orders buy or sell a given quantity at a specified price or better. The price limit must not be breached, even at the risk of failing to execute. They persist until executed or cancelled and so provide liquidity.

- A range of optional conditions allow control over factors such as:
  - How and when the order becomes active.
  - Its lifetime/duration.
  - Whether it may be partially filled.
  - Participation in auction/crossing sessions.  $\sim$
  - Whether it should be directed to specific venues or even market makers. \_
  - Linking with other orders. \_
  - Miscellaneous factors, such as odd lots and settlement handling. \_
- More specialised order types (derived from both market and limit orders) offer:
  - Hybrid orders, such as market-to-limit, which try to offer the best of both limit and \_ market orders.
  - Conditional orders, such as stops, which base their validity on a set condition. Only when the condition is met will it result in an actual order being placed.
  - Hidden orders try to reduce signalling risk for large orders.
  - Discretional orders offer more dynamic handling of limit prices. -
  - Routed orders allow more complex routing logic than possible via conditions. \_
  - Order-contingent orders, which offer more complex linking relationships. ---------------------------------------
- New order types are continuing to evolve. Some venues even offer orders that behave like algorithms, such as targeting the VWAP or participating in a set percentage of the market volume. Indeed, the line between them and trading algorithms is becoming increasingly blurred.
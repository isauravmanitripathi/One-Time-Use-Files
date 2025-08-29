![](_page_0_Picture_1.jpeg)

Execution tactics focus on the micro level decisions that need to be made when trading. They are responsible for the actual execution, monitoring the order book and managing order submission.

#### Introduction 9.1

Execution tactics represent the micro-level choices that must be made during trading. Typically, this means order placement and management. The division of labour between trading algorithms and execution tactics is clearest for the earlier schedule based algorithms. For example, in an all day VWAP algorithm the trading schedule might be based around 15 minute volume "buckets". During the first period, it might aim to trade 3,000, then 2,000 in the next and so on. So for each 15-minute period an execution tactic may be tasked with trading a specific amount. It might simply choose to place a single limit order at the best bid or offer; alternatively, it could slice the amount into a series of smaller orders, as shown in Figure 9-1. In some ways, an execution tactic may be thought of as a mini-algorithm, with a trading horizon of seconds or minutes rather than hours.

![](_page_0_Figure_5.jpeg)

Figure 9-1 Comparing trading algorithm and execution tactic horizons

In order to achieve their objectives, execution tactics often adopt a range of common trading mechanisms. As we saw in Chapter 4, dynamic orders are becoming increasingly sophisticated, so there are often crossovers between common trading tactics and the actual underlying order types. For instance, pegging is obviously related to pegged orders, whilst hiding relies on iceberg and hidden order types. Though, not all venues support these order types, so trading tactics can provide a convenient abstraction. The tactics can then either use the native order types, or adopt an order placement strategy that essentially mimics the required behaviour for venues that do not support them. Alternatively, trading tactics may also employ more complex logic than is currently available via native order types.

As trading algorithms have evolved, many now track market conditions on a tick-by-tick basis. One way of adapting to changing conditions is to use different execution tactics. When market conditions are favourable, an aggressive approach may be employed; then as they become less favourable, it could switch back to using a more passive one.

Note that it is important to realise that there does not have to be a one-to-one relationship between trading algorithms and execution tactics. Some algorithms may use several execution tactics in parallel, leaving passive ones to trade over a longer horizon whilst quicker, more aggressive techniques take advantage of favourable prices.

#### 9.2 Designing execution tactics

The simplest execution tactics are static; so all the logic resides with the trading algorithm. Effectively, these merely consist of splitting child orders to the market with an appropriate price. Passive approaches will adopt limit orders priced at or behind the market whilst aggressive ones use either market or marketable limit orders.

Neutral tactics are more flexible. They may start out passively, seeking price improvement, but if they fail to execute within a certain amount of time they will update or cancel the extant orders, replacing them with more aggressively priced ones. The deadline for execution may just be a fixed period (say five minutes). Alternatively, it could be determined from a limit order model, as we saw in Chapter 8.

Tactics that are more dynamic tend to consider market conditions when making order placement choices. For example, as we saw in Chapter 8, the order book conditions that generally tend to encourage traders to place less aggressively priced orders are:

- wider spreads
- ٠ sufficient depth, or prices further apart, on the opposite side of the order book
- ٠ insufficient depth, or prices close together, on our side of the order book

Given favourable conditions, a passive price-driven tactic may well price its orders further from the market, seeking price improvement. Alternatively, risk/cost-driven tactics may opt to weigh up the potential costs and decide whether it is better to wait or take an immediate hit. Opportunistic tactics may trade aggressively to take advantage of the current conditions.

So, broadly speaking, execution tactics may be classified based on the goals that drive their usage, just as we categorised trading algorithms in Chapter 5. Some common examples arc shown in Table 9-1.

In general, impact-driven tactics seek to further reduce market impact by splitting the order into smaller quantities or by hiding a portion of it. Price/risk-driven approaches strive to dynamically adjust based on the market conditions. Similarly, the opportunistic ones look to take advantage when conditions are favourable.

| Impact-driven     | Price/Risk-driven   | Opportunistic/<br>Liquidity-driven |
|-------------------|---------------------|------------------------------------|
| Slicing<br>Hiding | Layering<br>Pegging | Seeking<br>Sniping                 |
|                   | Catching            | Routing<br>Pairing                 |

| <table>  Table 9-1 Common trading tactics/mechanisms</table> |  |  |  |
|--------------------------------------------------------------|--|--|--|
|--------------------------------------------------------------|--|--|--|

Note that a lot of the functionality is applicable amongst the various types so these categorisations are merely guidelines; different approaches may well use them in a "pick 'n mix" fashion. It is important to remember that the trading algorithm is still the main driver of the trading strategy, but by selecting the most appropriate execution tactics, we can further enhance performance.

# Impact-driven tactics

Just as impact-driven trading algorithms break down the order into smaller quantities, these tactics apply a similar approach to order placement. Order slicing usually creates tranches that are placed sequentially. Alternatively, the child orders may be hidden, either with the appropriate order types or by sending the order to an opaque ATS.

## Slicing

Order slicing is essentially the precursor to the early schedule-driven algorithms. That said, it can still be a useful approach. Reducing the size of an order can lower its market impact and any associated signalling risk, albeit at the cost of execution probability.

Execution tactics usually focus on a much smaller timeframe than a trading algorithm. For example, an over the day VWAP algorithm might need to trade 100,000 of ABC. Though, in a ten-minute period, it may only need the execution tactic to work 3,000. Depending on the market, 3,000 could still be too large to place as a single order, therefore order slicing can be used to reduce this to a series of less noticeable sizes. Randomisation is a way of further reducing signalling risk. This applies to both the quantities to be split and the time between each child order. Otherwise, a very predictable trading pattern emerges, which might be taken advantage of by other market participants. For instance, Figure 9-2 shows two different

![](_page_2_Figure_9.jpeg)

Figure 9-2 Two alternative order splitting tactics

tactics to split an order for 1,000 ABC over the same time period. Clearly, the more random second strategy is harder to second-guess.

Used sequentially, order slicing effectively acts as a hiding mechanism. It may be adopted to create synthetic iceberg orders for venues that do not natively support this order type. Note that there is a key difference between order slicing and native iceberg orders, as we saw in Chapter 4: For native iceberg orders, the hidden portion is still part of the order book, and so may still participate fully in the trade crossing mechanism, albeit with only price priority. Whereas an order slicing mechanism relies on execution confirmations to know when next to send another order slice. Since these are dispatched after the matching process, we will potentially miss out on some crossing opportunities.

For example, consider a requirement to sell 10,000 ABC, from which we have split an initial child order for  $1,000$  at 101 as S1. Figure 9-3(a-c) shows how an incoming market order to buy 2,200 affects the order book, whilst (d) shows the alternative outcome for a native iceberg.

|             |         | Buys  |       | Sells |       |         |    |  |  |
|-------------|---------|-------|-------|-------|-------|---------|----|--|--|
| $\text{Id}$ | Time    | Size  | Price | Price | Size  | Time    | ld |  |  |
|             | 8:25:00 | 1,000 | 100   | 101   | 1,000 | 8:20:00 | SI |  |  |
|             | 8:20:25 | 2,000 | 99    | 101   | 800   | 8:25:25 | S2 |  |  |
|             | 8:24:20 | 1,500 | 98    | 102   | 2,500 | 8:24:09 | S3 |  |  |

(a) before

|    |         | Buys   |       | Sells |       |         |     |  |  |  |
|----|---------|--------|-------|-------|-------|---------|-----|--|--|--|
| 1d | Time    | Size   | Price | Price | Size  | Time    | ld  |  |  |  |
|    | 8:25:00 | 10,000 | 100   | 101   | 1,000 | 8:20:00 | S1  |  |  |  |
|    | 8:20:25 | 50,000 | 99    | 101   | 800   | 8:25:25 | \$2 |  |  |  |
|    | 8:24:09 | 25,500 | 98    | 102   | 400   | 8:24:09 | \$3 |  |  |  |
|    |         |        |       | 101   | 850   | 8:26:00 | S6  |  |  |  |
|    |         |        |       | 102   | 2,100 | 8:24:09 | S3  |  |  |  |

(c) after for a synthetic iceberg

Figure 9-3 An order slicing example

The incoming market order will immediately cross 1,000 with our order S1, whilst another 800 will cross with order S2. Since there are no more orders at 101, it will now have to cross the remaining 400 at 102 with order S3. The venue will send out confirmations for these fills. Once the order confirmation is received, we now split another order (S6), this time for 850.

In comparison, for a native iceberg order its price priority would mean the hidden size completed the market order at 101. As we can see in Figure 9-3(d), a new display size would still have been split as order S6, 400 of which completes the incoming market order. The remaining 600 (assuming a display size of 1,000) stays on the order book, and now has price priority. Therefore, an exchange's native iceberg orders can offer both faster execution, and a higher probability of completion.

Clearly, the main disadvantage with order slicing is that we may miss out on crossing opportunities, since our order placement is reliant on the dispatch of execution notifications that take place afterwards. In this example, we only managed to cross 1,000 with the market order, since the crossing mechanism completes the market order by filling with S3 before we are notified that order S1 filled. Note that when selling in an upward trending market missing execution opportunities is less of an issue, but in a downward market this would have

2,100 (b) MO crosses

Sells

Size

1,000

800

400

Id

SI

\$2

\$3

S3

Price

101

101

102

102

|       | Sells            |     |
|-------|------------------|-----|
| Price | Size             | Id  |
| 101   | 1,000            | \$1 |
| 101   | 800              | \$2 |
| 101   | 400              | \$6 |
| 101   | 600              | S6  |
| 102   | 2,500            | S3  |
|       | (d) for a native |     |

resulted in a loss.

The main advantage of order slicing is that we have much more control of the display size, so our second order can be split with a random size, rather than simply splitting 1,000 each time (in this case 850 was used). Order book information and price trend indicators may be used to select the optimal display quantity and even limit price.

Order slicing may also be applied in parallel, allowing simultaneous trading across several execution venues. Similarly, it may also be used to split orders across a range of prices; effectively this is the layering tactic, which we shall discuss shortly. Such versatility means that order slicing can still be a useful tactic, despite its simplicity.

#### Hiding

Hiding is all about reducing signalling risk. Generally, it is used for orders that would otherwise provide liquidity, namely standing limit orders. This risk reflects the potential losses we can incur from the information that our trading pattern relays to the other market participants. For instance, placing a large buy order gives away our requirements; other traders will then react to this, most likely by raising the price at which they are prepared to sell. They may even cancel their orders to see if we are prepared to go even higher.

Note that in some multi-venue marketplaces hiding can be as straightforward as routing the order to a less obvious venue, where it will face less competition. This applies in particular for U.S. equities since the order protection rule introduced for Regulation NMS means that orders placed at the top of the order book should not be traded through.

Algorithmic orders are implicitly hidden, since most strategies only release a small portion of the order for immediate trading. However, signalling risk is dependent on both the order size and the asset's liquidity. In fact, for illiquid assets even a small order can result in the price shifting away as other traders try to second-guess our requirements. We can further reduce the signalling risk by using hidden order types, as shown in Figure 9-4.

|       | Sells            |    |       | Sells       |     | Sells |                  |     |  |
|-------|------------------|----|-------|-------------|-----|-------|------------------|-----|--|
| Price | Size             | ld | Price | Size        | Id  | Price | Size             | ld  |  |
| 101   | 1,000            | SI | 101   | 2,000       | S1  | 101   | 1,000            | SI  |  |
| 101   | 3,000            | S2 | 101   | 3,000       | S2  | 101   | 2,000            | S2  |  |
| 102   | 4,000            | S3 | 101   | 1,000       | S3  | 101   | 4,000            | 111 |  |
| 102   | 2,000            | S4 | 101   | 7.000       | 111 | 102   | 1,000            | S4  |  |
|       |                  |    | 102   | 4,000       | S4  |       |                  |     |  |
|       | (a)Discretionary |    |       | (b) Iceberg |     |       | (c) Fully hidden |     |  |

Figure 9-4 Hidden order types

Discretionary orders, although fully visible, allow us to hide our actual limit price. For example, in Figure 9-4(a) we have hidden our true intentions by displaying our order S3 with a limit price of 102, even though we are prepared to trade at 101. Admittedly, we could increase the discretionary amount to shift our order deeper into the order book; however, this will place even more orders in front of us in terms of execution priority. The full size is also visible; hence, discretionary orders are generally more suited for smaller orders.

Iceberg orders go further and allow us to display only a portion of the order, whilst the remaining hidden portion retains price priority. For instance, in Figure 9-4(b) we have set the display size to 1,000, again shown as order S3. The remaining 7,000 will remain hidden until order S3 is completed, although it will maintain price priority over order S4. Note that it is important to get the right balance when selecting a display size. Too small a quantity and the order will take longer to complete, since only the visible portion will have both price and time priority. Conversely, selecting too large a display size will allow for faster completion, but at a greater exposure risk. Another factor to consider is the predictability of the display size. In a study of trading on XETRA, Angelika Esser and Burkart Mönch (2007) observed a distinct preference to use a display size of 10% of the parent order. Clearly, this will vary across both assets and markets; however, human nature also plays a part; people will often prefer to use a round number that is easy to calculate. For venues that do not support iceherg orders, we can create synthetic icebergs using randomised order slicing, as we saw in the previous section.

Fully hidden orders can further reduce signalling risk, so in Figure  $9-4(c)$  our entire order H1 is hidden. Some exchanges, such as the Australian Stock Exchange (ASX) used to offer fully hidden orders; however, in an effort to balance the needs of both institutional and retail users many have replaced them with iceberg orders. That said, the introduction of new "dark pools" via alternative trading systems (ATSs) means that fully hidden orders are now making a comeback.

It is important to remember that even the best hiding mechanisms can only really delay the inevitable. Other market participants will undoubtedly be constantly monitoring the order book state and comparing this with the reported trades to try to find hidden liquidity.

# **Price/Risk-driven tactics**

Price-driven tactics may be based on changes in the spread and short-term price trends. For instance, as the gap between best bid and offer narrows we can afford to pay the spread, and so the tactic can issue more marketable limit orders or even market orders. As soon as the spread widens, more passive pricing is used.

Likewise, for price trends, these tactics can react much like the adaptive trading algorithms we saw in Chapter 5. Thus, a passive trading style tends to rely on trends persisting, pricing its orders even further from the market during favourable price trends, to try to maximise price improvement. Conversely, during unfavourable price trends it may price orders closer to the market to try to stem potential losses. Aggressive price-based tactics often rely on price trends mean reverting, and so they behave in the opposite fashion to passive ones, aggressively taking advantage of favourable prices. The price trends may be based on forecasts or inferred from the order book imbalance. For example, a surplus of sell volume on the order book may indicate the price will soon decrease.

Risk-driven tactics may also consider the asset's price volatility and how much time they have left to execute. These may be combined to create a timing factor, which can then be incorporated into the order placement decision. Hence, for a liquid asset at the start of its execution the timing factor is fairly minor; however, it increases as time progresses. For less liquid assets, this factor is more important, and so is more likely to encourage placing more aggressive orders.

In terms of common mechanisms, orders may be layered throughout the order book to try to maximise both execution probability and the potential for price improvement. Alternatively, they may simply be pegged to a market price, or linked with a cost-based latching mechanism to reduce risk.

## Layering

The layering tactic simultaneously maintains a range of standing limit orders. The orders are spread throughout the order book, usually with different limit prices. This approach aims to take advantage of favourable price movements. Also for venues where matching is based on

price/time priority, the layering tactic helps preserve the time priority for each order. This is because when the market price moves a new order may be split, rather than just updating an existing order to match the new level. This allows the other layered orders to maintain their time priority in the order book queue.

As Michael Aitken *et al.* (2007) point out, time priority is particularly important for liquid stocks that have densely populated order books. The high turnover of orders means that if time priority is lost, the only way to regain it is with a more aggressive price. For example, the order book in Figure 9-5(a) shows our three layered orders S1, S2 and S5 for ABC, ranging in price from 101 to 103. Compared to the single order S3 our combined orders offer more potential for price improvement, should an aggressive order walk up the order book.

| Buys  |       |       |        | Sells   |    |       | Sells |         |    |
|-------|-------|-------|--------|---------|----|-------|-------|---------|----|
| Size  | Price | Price | Size   | Time    | Id | Price | Size  | Time    | 1d |
| 1,000 | 99    | 101   | 000, 1 | 8:25:20 | S5 | 100   | 500   | 8:26:20 | S7 |
| 500   | 99    | 101   | 800    | 8:25:00 | S4 | 101   | 1,000 | 8:25:20 | S5 |
| 1,800 | 98    | 102   | 2,500  | 8:24:25 | S3 | 101   | 800   | 8:25:00 | S4 |
| 2,400 | 98    | 102   | 500    | 8:24:09 | S2 | 102   | 2,500 | 8:24:25 | S3 |
| 900   | 97    | 103   | 1.000  | 8:23:00 | S1 | 102   | 500   | 8:24:09 | S2 |
| 2,500 | 97    |       |        |         |    | 102   | 3,000 | 8:26:05 | S6 |
|       |       |       |        |         |    | 103   | 1,000 | 8:23:00 | SI |

(a) before

(b) a new price level is set

## Figure 9-5 Layered orders

Admittedly, some execution probability is sacrificed, but the layered orders also allow us more scope to modify orders without losing time priority. For instance, when new orders S6 and S7 arrive, a new price level is set at 100. Assuming we want to participate at this new level, we have several options. If our requirement allows placing an additional order then we can simply split a new order S8 at 100. Though, if we do not want to increase our exposure then we shall need to adjust our existing orders. So we could either:

- 1. Undate the limit price on order S5 to be 100.
- 2. Reduce the quantity of S5 and use this to split a new order S8 at 100.
- 3. Reduce the quantities of S1 and S2, then again split a new order S8.
- 4. Reduce the quantity just for S1 and split a new order S8.

All these options allow us to participate at 100; in comparison a single order, such as S3, has fewer alternatives in such a situation. Option 1 leaves us with no presence on the order book at 101. If the price reverts slightly we could miss an opportunity to execute. Option 2 addresses this issue, nevertheless, we have still reduced the size of the order that was second most likely to execute.  $1$  To resolve this problem options 3 and 4 source the required volume using orders further away from the market, reducing the impact on our overall execution probability. Overall, option 4 is probably the best approach  $^{2}$  since it modifies the order least likely to execute.

So layering orders is useful for highly liquid assets with dense order books where achieving time priority is difficult. Pegging the price of orders to keep up with the market would be an expensive option since it would keep reducing our priority. Whereas by layering orders across the book we can track price moves without significantly affecting our overall

<sup>&</sup>lt;sup>1</sup> Reducing the size would have more effect in a venue using price/pro-rata order matching.

<sup>&</sup>lt;sup>2</sup> This holds true regardless of whether the venue uses price/time priority or price/pro-rata for its order matching.

execution probability.

Layering is useful for illiquid assets as well, since there is more scope for price improvement, it also improves the visible depth. Deeper hooks with a lower range of prices tend to promote more aggressive orders from the opposite side. Thus, by filling gaps we can reduce the expected market impact and so try to encourage participants on the other side to place more favourably priced orders. Note that filling gaps means just that, it does not mean filling an empty order book for an illiquid asset with layered orders to give the illusion of depth.

# Pegging

Pegged orders are a convenience, they provide dynamically updating limit prices that reduce the risk of mispricing for standing limit orders. Often this tactic is used with passive orders that are trying to benefit from price improvement. Pegging may also be based on the price of another asset, for instance, in pair trading, or versus a market index. Similarly, for options, delta-adjusted orders are effectively pegged based on the price of the underlying asset and the option's delta.

Care must be taken when using pegging since regular trading patterns can lead to considerable signalling risk. Pegging every 30 seconds 0.5 away from the mid is nearly as predicable as the order slicing we saw in Figure 9-2. Hence, randomisation is important to reduce the predictability of pegged trading, both for when updates are made as well as for their size. Two other potential issues with pegging were pointed out by David Brown and Craig Holden (2005): Pegged orders can contribute to momentum since they continually shift liquidity with the prevailing trend. They also generally have a lower execution probability, since in a price/time priority based venue changing the limit price will often place them at the end of the queue (unless a new price level is set).

A more adaptive approach to pegging could incorporate market conditions or short-term price predictions in the decision of whether to peg the order. Note that pegging can just as easily be applied to order sizes. Thus trading based on the available order book depth might peg orders to the best bid or offer size. Note that most venues will allow an order to be reduced in size without losing priority. Increasing the size of an order would clearly disadvantage other similarly priced orders behind it in the order book queue, so to ensure fairness such an update often results in the order losing its priority. Alternatively, it may be better to adopt an order layering tactic.

# Catching

This tactic is based on cutting our losses when the price looks to be trending away from us. In some ways, it may be thought of as a visible trailing stop. To start with, we shall adopt a fairly passive latching mechanism, as we can see in Figure 9-6.

Essentially, this is a means of dynamically adjusting our limit price based on the current market price. The main difference from pegging is that it works only in one direction. Generally, price latches are used to try to keep any potential gains from market moves. Consequently, this mechanism is used by both trailing stops and tick-sensitive orders. A positive latch will only move when the price rises (e.g. trailing stop sells and downtick orders); whilst a negative one only tracks price drops (e.g. trailing stop huys and uptick orders).

Figure 9-6 shows a buy order positively latching to the best bid; hence, its limit price only changes when the best bid rises. In addition to the latch, we can assign a trigger limit, much like for a stop order. When the market price reaches this point we will become more aggress-

![](_page_8_Figure_1.jpeg)

ive, to try to stem any losses. This is the point labelled trigger in Figure 9-6. So our order will now be priced based on the best offer, paying the spread to prevent any further losses. Alternatively, a market order might even be used, risking further market impact to guarantee execution.

## Opportunistic/Liquidity-driven tactics

As with the opportunistic trading algorithms, these tactics tend to strive to maximise the benefits of favourable market conditions, such as liquidity. The seeking tactic aims to source additional liquidity from hidden orders. Tactics may also focus on reducing signalling risk. Clearly, any orders we place will change the available order book depth and so affect the overall order imbalance. For example, if we need to buy but there is already an imbalance skewed towards buy volume then adding another buy order will only increase the probability of a price rise. Sniping tries to take advantage of available liquidity without giving away our own requirements. Finally, routing corresponds to choosing the best destinations to send orders to, based on a variety of criteria.

## Seeking

The seeking tactic is all about finding hidden liquidity. Market participants are constantly monitoring the state of the order book and comparing this with the reported trades to try to spot hidden liquidity. Based on this data we can create models to estimate the probability of how much volume is hidden at the various price levels throughout the order book, as we saw in Chapter 8. Note that these are just estimates; the only way we shall really know if there is any hidden liquidity is by issuing an order and, hopefully, being filled with a better price.

Another important concern when searching for liquidity is keeping our own orders hidden; otherwise, we may be exposed to considerable signalling risk. We want to fill our own orders at the best price possible without giving away information about our actual requirements. So a persistent order will not do, instead we will need to use either market orders or marketable limit orders with specific fill instructions. Assuming we want to be able to control our market impact then we can rule out market orders. So the choice is now between the various fill instructions available for limit orders: Of these only immediate-or-cancel and fill-or-kill are suitable, since the others all leave residual orders on the order book. The main difference between the two instructions is that immediate-or-cancel allows partial fills whereas fill-orkill has a strict 100% execution requirement.

Having identified potential sites in the order book with hidden liquidity, all we need to do

now is issue appropriate orders. For instance Figure 9-7(a) shows an example order book for asset ABC. In this example, our estimates suggest that there may be 6,000 hidden to sell at 101 (labelled H1). By sizing our order larger than the visible volume on the order book we are seeking hidden liquidity. If our order is filled then there may well be hidden liquidity at that price point. If sufficient liquidity is not available then our order is immediately cancelled, leaving no trace on the order book. Figure 9-7(b) shows our estimate of what the order book will look like after issuing a limit order to buy 3,000 ABC at 101.

| Buys       |       |       |       | Sells   |     |           |       | Sells   |     |
|------------|-------|-------|-------|---------|-----|-----------|-------|---------|-----|
| Size       | Price | Pricc | Size  | Time    | Id  | Price     | Size  | Time    | ld  |
| 800        | 100   | 101   | 1,000 | 8:25:00 | S1  | 101       | 1.000 | 8:25:00 | \$1 |
| 1,000      | 99    | 101   | 6.000 | 8:20:25 | III | 101       | 2.000 | 8:20:25 | Ħ   |
| 2,500      | 98    | 102   | 2,000 | 8:21:25 | S2  | 101       | 1,000 | 8:28:00 | S4  |
|            |       | 102   | 1,500 | 8:24:09 | S3  | 101       | 3,000 | 8:20:25 | III |
|            |       |       |       |         |     | 102       | 2,000 | 8:21:25 | S2  |
| (a) before |       |       |       |         |     | (b) after |       |         |     |

Figure 9-7 An example search for hidden liquidity

In the case of an iceberg order, a new tranche may be issued, such as order S4. Though, neither this, nor a successful execution guarantees that there is any more hidden liquidity. We still need to carefully check the order book state before and after; since potentially we could have crossed with another visible order which hit the order book the same time as ours.

If sufficient hidden liquidity is available then the behaviour of our liquidity seeking order will be the same, regardless of whether we use an immediate-or-eancel or a fill-or-kill instruction. However, let's now assume that the hidden size shown in H1 is only for 1,500. An immediate-or-cancel instruction would mean that our order fills 2,500 ABC at 101, with the best offer becoming order S2 at 102. Having consumed all the hidden liquidity that was available at 101, we can also feedback this size into our hidden order models to help improve future estimates. In comparison, a fill-or-kill order would have failed to cross since there is insufficient hidden liquidity; therefore, the order would be immediately cancelled leaving the order book still looking like Figure 9-7(a). Unfortunately, all this has told us is that there is not sufficient ABC hidden at 101.

Thus, immediate-or-cancel orders offer a way of probing for hidden liquidity that minimises their footprint on the order book and may partially fill, even if our estimate for the amount of hidden liquidity is wrong. Fill-or-kill orders are less forgiving in this last respect due to their 100% completion requirement. Partial fills are important since by the time we resubmit an order someone else may have already found and consumed any hidden liquidity.

# Sniping

Sniping is a tactic for capturing liquidity whilst minimising signalling risk. Effectively, it is a way for liquidity demanders to hide their strategy. Alternatively, it is just a version of the seeking tactic for visible liquidity. To reduce the potential for signalling risk we will use marketable limit orders with specific fill instructions. This gives us price control and limits our footprint on the order book.

When liquidity becomes available, an aggressive order is used to cross with it. For instance, Figure 9-8 shows the order book as new order S1 arrives, offering to sell 1,000 ABC at 101.

| Buvs   |       |       |       | Sells   |             |       |       | Sells   |    |
|--------|-------|-------|-------|---------|-------------|-------|-------|---------|----|
| Size   | Price | Price | Size  | Time    | $\text{1d}$ | Price | Size  | Time    | Id |
| 000, 1 | 100   | 101   | 1.000 | 8:25:00 | S1          | 101   | 900   | 8:25:00 | S1 |
| 1,700  | 99    | 102   | 800   | 8:20:25 | S2          | 101   | 100   | 8:25:00 | S1 |
| 2,200  | 98    | 104   | 1.100 | 8:19:09 | S3          | 102   | 800   | 8:20:25 | S2 |
|        |       |       |       |         |             | 104   | 1,100 | 8:19:09 | S3 |

(a) before

(b) after

| Figure 9-8 An example sniping order |  |  |  |  |
|-------------------------------------|--|--|--|--|
|-------------------------------------|--|--|--|--|

In order to grab this newly available liquidity we issue a fill-or-kill order to buy 900 at 101. By sizing our order just less than the best offer size, we should leave a remainder on the order book, therefore the bid offer spread remains undisturbed at 100-101. This is a reasonable approach since the order book imbalance is currently tilted towards the buys, so if we had taken the whole volume at 101 it is quite possible that the spread would have shifted up to a less favourable 101-102. Note that for sniping either immediate-or-cancel or fill-orkill instructions can be equally useful, based on whether we want partial fills or not.

Sniping can also adjust to the available liquidity. For example, if order S2 in Figure 9-8 had been priced at 101 we could have executed 1,700 without altering the spread.

## Routing

Routing is important for markets that have a range of execution venues. When choosing where to send orders, many different factors should be analysed. Obviously, the price and quantity available are key to the decision, but other important considerations are the probability of hidden liquidity, the likelihood of successful execution, latency and any venue specific costs or fces. Routing mechanisms constantly make these decisions, based on the available data, to try to ensure orders are sent to the optimal destination.

As we saw for liquidity-based trading algorithms, a common way of tackling the difficulty of trading in fragmented markets is to use liquidity aggregation. A virtual order book can be created by collecting data from all the possible execution venues. From this, we can then make more balanced decisions about how much to trade and at what price level. Having decided this we then need to convert our requirements into actual orders. This transformation may be performed by the actual trading algorithm; alternatively, it can be delegated to a routing based execution tactic.

Figure 9-9 shows an extension of the example we saw in Chapter 5 for liquidity based trading algorithms. The virtual order book has been decomposed back into its constituents. These are ordered by price, probability of execution and size. The hidden orders are only estimates, and so are placed after visible orders. Each entry is also flagged with the venue it originated from, whether it is from the primary exchange (Exch-1), an alternative trading system (ATS) or an electronic crossing network (ECN).

We can then use this view to translate order requirements into actual orders. For instance, if price is our key concern then we should clearly try to capture any hidden liquidity at 101 on ECN-2. If we are more concerned about the probability of execution then we should focus on the orders available on Exch-1, ECN-2 and ATS-2. For larger quantities, we shall need to route orders to a wider range of venues.

For example, if we need to immediately sell 10,000 ABC, we could focus on just the visible liquidity, sending the following child orders:

> ATS-2: Sell 700 ABC at 100 ECN-2: Sell 1,500 ABC at 100

|       | Aggregated Buys |        |                 | Buys  |       | $\text{Exch-1}$ |     |
|-------|-----------------|--------|-----------------|-------|-------|-----------------|-----|
| Price | Size            | Prob % | #               | Price | Size  | Prob %          | ld  |
| 101   | 1,000           | 7      | Ĭ               | 100   | 1,000 | 85              | X1  |
| 100   | 4,200           | 80     | 4               | 100   | 6,000 | 10              | III |
| 100   | 11.000          | 11     | 4               | 99    | 4,000 | 85              | X2  |
| 99    |                 |        |                 | 99    | 3,000 | 18              | H2  |
|       | 7,000           | 79     | 2               | 98    | 2,000 | 85              | X3  |
| 99    | 6.000           | 17     | 2               |       |       |                 |     |
| 98    | 2,500           | 82     | 2               | Buys  |       | $ATS-1$         |     |
|       |                 |        |                 | Price | Size  | Prob %          | 1d  |
|       |                 |        |                 | 100   | 1,000 | 15              | H3  |
|       | Buys            |        |                 |       |       |                 |     |
| Price | Size            | Prob   | Venue           | Buys  |       | $ATS-2$         |     |
| 101   | 1,000           | 7      | ECN-2           | Price | Size  | Prob %          | 1d  |
| 100   | 700             | 90     | $ATS-2$         | 100   | 700   | 90              | A2  |
|       |                 | 85     | Exch-1          | 100   | 2,000 | 10              | 114 |
| 100   | 1,000           |        |                 | 99    | 3,000 | 16              | 115 |
| 100   | 1,500           | 80     | ECN-2           |       |       |                 |     |
| 100   | 1,000           | 70     | ECN-1           | Buys  |       | ECN-1           |     |
| 100   | 1.000           | 15     | ATS-1           | Price | Size  | Prob %          | Id  |
| 100   | 2.000           | 13     | $ECN-2$         | 100   | 1,000 | 70              | E1  |
| 100   | 6,000           | 10     | Exch-1          | 99    | 3,000 | 70              | E2  |
| 100   | 2,000           | 10     | $ATS-2$         | 98    | 500   | 70              | E3  |
| 99    | 4,000           | 85     | $\text{Exch-1}$ |       |       |                 |     |
| 99    | 3,000           | 70     | ECN-1           | Buys  |       | $ECN-2$         |     |
| 99    | 3,000           | 18     | $Exch-I$        | Price | Size  | Prob %          | Id  |
| 99    | 3,000           | 16     | ATS-2           | 101   | 1.000 | 7               | 116 |
| 98    | 2,000           | 85     | Exch-1          | 100   | 1,500 | 80              | E4  |
|       |                 |        |                 |       |       |                 |     |

Figure 9-9 An aggregated order book and its breakdown

Exch-1: Sell 5,000 ABC at 99 ECN-1: Sell 2,800 ABC at 99

Alternatively, we could try to consume some of the hidden liquidity by creating orders based on a mix of the probability of execution and the estimated hidden liquidity:

| ATS-1: Sell 1,000 ABC at 100  |  |
|-------------------------------|--|
| ATS-2: Sell 1,500 ABC at 100  |  |
| ECN-1: Sell 1,000 ABC at 100  |  |
| ECN-2: Sell 3,000 ABC at 100  |  |
| Exch-1: Sell 3,500 ABC at 100 |  |

Hence, we are able to easily route orders using various criteria, in an effort to achieve the best execution based on our requirements.

## Pairing

As we saw in Chapter 4, some execution venues support a range of contingent order types and conditions; however, the majority of venues do not provide these. Thus, one of the key aspects of the pairing tactic is to emulate this behaviour in order to be able to link orders.

When trading pairs (or baskets) of assets, the trading algorithm focuses on the trigger, i.e. whether the ratio or spread is favourable. Ensuring that each of the assets are successfully bought or sold can be delegated to an execution tactic. Since execution cannot be guaranteed, legging is an important consideration. This is the difference in value in the traded positions for each asset. Certainly, legging often drives the execution for these tactics.

If a reasonable amount of legging is permitted then each order can almost be worked separately. The execution tactic can choose to use standard mechanisms, much like any other static, price or liquidity-based approach. Only when the legging reaches its limit will it need to try to intervene.

For example, let's consider buying 2,000 of asset JKL and selling 2,000 of XYZ. For convenience, we will assume both these assets are priced around \$50. Our legging limit is set to \$5,000, therefore it equates to around 100 of either JKL or XYZ. So if we have already executed 400 JKL, but only 300 XYZ then we need to address this legging before we can think about buying any more JKL. Similarly, any extant orders for JKL should be cancelled to ensure we do not get even more legged. In order to try to catch up and reduce the legging we can convert any extant orders for XYZ to more aggressive ones, so long as the price of XYZ remains within our limits.

If a negligible amount of legging is allowed then each order will be contingent on the other. Figure 9-10 shows the order books for each asset. Hence, the:

- Buy order for 2,000 JKL (B4) is dependent on being able to sell XYZ at 50.5
- Sell order for 2,000 XYZ (S9) is dependent on being able to buy JKL at 50.8

| $J_{\text{L}}$ |       |       |       |       |    |               |       |       |       |       |    |
|----------------|-------|-------|-------|-------|----|---------------|-------|-------|-------|-------|----|
| Buvs           |       |       | Sells |       |    |               | Buys  |       | Sells |       |    |
| ld             | Size  | Price | Price | Size  | ld | ĺd            | Size  | Price | Price | Size  | ld |
| $\mathbf{B1}$  | ,500  | 50.6  | 50.8  | 2,500 | S1 | $\mathbf{B1}$ | 1,500 | 50.6  | 50.8  | 2,500 | S1 |
| B2             | 2,000 | 50.6  | 50.9  | 1,000 | S2 | B2            | 2,000 | 50.6  | 50.9  | 1,000 | S2 |
| B3             | 800   | 50.5  | 50.9  | 900   | S3 | B3            | 800   | 50.5  | 50.9  | 900   | S3 |
| B4             | 2,000 | 50.5  |       |       |    | $\mathbf{B4}$ | 1,000 | 50.5  |       |       |    |

XYZ

IKI

|    | Buys  |       |       | Sells |    |               | Buys  |       |       | Sells |    |
|----|-------|-------|-------|-------|----|---------------|-------|-------|-------|-------|----|
| ld | Size  | Price | Price | Size  | ld | ld            | Size  | Price | Price | Size  | td |
| B6 | 2,000 | 50.5  | 50.6  | .000  | S6 | $\mathbf{B6}$ | 2,000 | 50.5  | 50.6  | 1,000 | S6 |
| B7 | ,000  | 50.5  | 50.7  | 900   | S7 | B7            | ,000  | 50.5  | 50.7  | 900   | S7 |
| B8 | 500   | 50.4  | 50.7  | 1,500 | S8 | B8            | 500   | 50.4  | 50.7  | 1,500 | S8 |
|    |       |       | 50.8  | 2,000 | S9 |               |       |       | 50.8  | 1.000 | S9 |

(a) before

(b) after

## Figure 9-10 An example of contingent orders

Therefore, when the buy order B6 for XYZ is suddenly cancelled, we can no longer be sure of selling 2,000 XYZ at 50.5, so we need to modify our buy order B4 for JKL, reducing it to be for  $1,000$ , as shown in Figure 9-10(b). Essentially, each order is pegging to what is available on the same side of the order book for the other asset. Note that this can also involve changing the price as well as the size.

In turn, these orders are also linked to the outcome of each other, like the contingent orders that we saw in Chapter 4. This means that we may also need to adjust the size of our sell order S9 for XYZ. Otherwise, we could end up with around \$50,000 of legging.

The relative liquidity of each asset is also important: If one asset is significantly less liquid than the other then this becomes a bottleneck. In fact, the orders for the least liquid asset tend to drive the whole process.

#### **Algorithm selection** 9.3

In Chapter 5, we saw how various investment objectives could be translated into a range of trading algorithms. In turn, these may then use execution tactics to actually achieve their aims. This division of responsibility helps keep both the algorithms and the execution tactics simpler. Note that it is important to remember that the trading algorithm drives the execution tactics, and not the other way around. For example, a VWAP algorithm that uses pricedriven execution tactics is still trying to track the VWAP. The target quantities and hard price limits are still determined by the algorithm. The choice of execution tactic simply makes it slightly more price sensitive in the way it places its orders.

This "divide and conquer" approach also makes it easier to reuse the same logic between different markets or even across asset classes. For instance, we might well be able to "port" a VWAP or implementation shortfall algorithm built to trade U.S. equities to also work in Europe or Asia. Though, as we saw in Chapter 3, the world's financial marketplaces still have some substantial differences. So we shall only get the best performance if we fine-tune the algorithm for each specific region or market. Fundamentally, we are still tackling the same problem so much of the trading algorithm logic can stay the same. However, the actual order execution may need to be quite different. Therefore, we could create execution tactics that are customised for specific regions or markets. These in turn could be reused, potentially allowing us to port other algorithms to new markets much more quickly. This approach could even be extended to port equities-based algorithms to other asset classes, such as futures or FX.

Execution tactics also allow common trading mechanisms to be shared amongst a wide range of algorithms. This is particularly useful given the increasing need for customisation and rapid turnaround of new trading algorithms. For example, modern VWAP and implementation shortfall algorithms may well share some of the same execution tactics, even though at the algorithm level their objectives are very different.

| Algorithm          |                               | <b>Tactics</b>   |                      |                             |
|--------------------|-------------------------------|------------------|----------------------|-----------------------------|
|                    |                               | Impact<br>driven | Price/Risk<br>driven | Opportunistic/<br>Liquidity |
|                    | Time Weighted Average Price   |                  | O                    |                             |
| Impact             | Volume Weighted Average Price |                  | 0                    | 0                           |
|                    | Percentage Of Volume          |                  | 0                    | 0                           |
|                    | Minimal impact                |                  | 0                    | $\cap$                      |
| Cost               | Implementation Shortfall      |                  |                      | 0                           |
|                    | Adaptive Shortfall            |                  |                      | 0                           |
|                    | Market On Close               |                  |                      | 0                           |
| Oppor-<br>tunistic | Price Inline                  |                  |                      | O                           |
|                    | Liquidity-driven              | 0                | 0                    |                             |
|                    | Pairs / Spread trading        | 0                | 0                    |                             |
|                    |                               | often used       |                      | $\circ$ sometimes used      |

Table 9-2 summarises some of the typical combinations.

**Table 9-2 Execution tactics used by trading algorithms** 

Note that the relationship between trading algorithms and execution tactics does not have to be strictly one-to-one; in fact, some algorithms may use multiple execution tactics in parallel.

Impact-driven algorithms essentially use order slicing to try to minimise the overall market impact. They may simply be driven by time (TWAP), a historical volume profile (VWAP) or the actual market volume (POV). Thus, the algorithm just needs the execution tactics to work the order as best they can. So we could really use any of these approaches. For instance, a VWAP or POV algorithm using stealth-based or opportunistic tactics might prove to be a good way of reducing market impact.

Cost-driven algorithms have quite a difficult goal to achieve; they need to take account of market impact, timing risk, and even factors such as price trends. So it is important that the execution tactics are attuned to this and do not miss opportunities or incur additional costs. Hence, these algorithms may well adopt multiple tactics. They may switch between approaches, or even run tactics in parallel.

Opportunistic algorithms are focussed on taking advantage whenever the market conditions are favourable; they are less concerned about completing the whole order. So they are much more similar to execution tactics than the other two classes of algorithm. For instance, liquidity-driven algorithms tend to adopt liquidity or stealth-based tactics. Similarly, pair trading implies a pair based, or order contingent approach, although if the legging is sufficient it might also be implemented with a mix of seeking (for illiquid assets) and sniping (for the more liquid ones). Price inline algorithms tend to adopt a wider range, since they are essentially based on an underlying impact-driven algorithm.

## Factors affecting the choice of execution tactics

Each trading algorithm bases its trading approach on a wide range of factors, encompassing the investor's goals, the order details and asset-specific information. In Chapter 7 we saw how these factors affect the actual choice of trading algorithm. For execution tactics the main factors affecting their choice are more straightforward. Essentially, this depends on both the current market conditions and how well the algorithm is actually performing.

## Market conditions

As trading algorithms have evolved many now track market conditions on a tick-by-tick basis. Internally, they may use this information to alter their target trading patterns. They may also choose to trade more or less aggressively based on whether the market conditions are favourable or not, as we saw for the adaptive shortfall and price inline algorithms.

In terms of their choice of execution tactics, the controlling algorithms may decide to switch between more or less aggressive approaches, based on their perception of the current market conditions. For instance, if the current price trend is favourable the algorithm may adopt a more passive approach, seeking price improvement.

Some algorithms may use multiple execution tactics in parallel. For example, a passive price-based approach might be left running to try to achieve price improvement whilst more aggressive stealth-based tactics might be used to take advantage of any opportunities that arise.

Liquidity is another important factor. Although this is primarily an asset-specific characteristic, we can also characterise this at the market/venue level based on their average spreads and trade sizes.

#### Average spread

The bid offer spread is one of the most visible indicators of liquidity. Table 9-3 shows the average spreads in basis points for a range of different venues and asset classes.

| Asset class  |                     | Venue                     | Average<br>spread / bps |  |
|--------------|---------------------|---------------------------|-------------------------|--|
|              | Stocks              | NASDAO                    |                         |  |
|              |                     | Euronext Paris            | 13                      |  |
|              |                     | Italy SE                  | 22                      |  |
| Equity       |                     | LSE                       | 32                      |  |
|              |                     | Hong Kong Ex <sup>3</sup> | 47                      |  |
|              |                     | Singapore SE <sup>3</sup> | 61                      |  |
|              | U.S Treasury 2yr    |                           | $\sim 3$                |  |
| Fixed income | U.S Treasury 10yr   |                           | ~6                      |  |
|              | Corporate bonds     | TRACE                     | $25 \pm$                |  |
| FX           | Spot                | EBS                       | $-1-3$                  |  |
| Derivatives  | S&P 500 E-mini futs | CME                       | $\sim 2$                |  |

Source: Equity: EDHEC (2007), FT Mandate (2006), Fixed Income: Edwards, Harris and Piwowar (2007) and author's own estimates

#### **Table 9-3 Average spreads**

For markets where a few key assets are highly traded, such as FX or U.S. Treasuries, competition ensures that the spreads are generally much lower. Indeed spreads for these have been as little as 1 or 2 bps or even less. As the liquidity decreases brokers/dealers cover their risk by increasing the spread. For really illiquid assets, spreads may be measured in hundreds of basis points.

Spreads are also closely linked to volatility; since, as we saw in Chapter 2, they represent a premium that market makers apply to protect themselves from the risk of adverse selection. During the 2007-09 financial crisis, spreads increased considerably: Spreads for many stocks doubled, illiquid shares saw even higher rises. Similar increases occurred for other asset classes, pretty much preserving the relative proportions shown in Table 9-3.

There can also be significant geographical differences in the average spread cost. Across Europe, spreads are traditionally somewhat higher than those of the U.S., whilst those in Asia are often even higher. Consequently, aggressive trading tactics can be a lot more expensive in these regions.

When spreads are high it can be worth adopting a more passive trading style to reduce the overall spread cost. Therefore, pegging or layering orders may be used to try to maximise the price improvement. If risk is a significant factor then a catching mechanism might be adopted to reduce the potential losses if the market suddenly moves away.

#### Average trade size

When we are considering the difficulty of an order it is usual to compare its overall size to the average daily volume (ADV). Thus, an order that is less than 5% of the ADV should be reasonably straightforward to execute. However, it is also worth considering the average trade size. Table 9-4 shows some of the average trade sizes and values for a range of assets and venues.

 $^{3}$  Median figures

| Asset class  |                    | Venue          | Average<br>trade<br>size | Average<br>trade value<br>(\$1000s) |
|--------------|--------------------|----------------|--------------------------|-------------------------------------|
|              | Stocks             | NASDAO         | 330                      | 9                                   |
| Equity       |                    | NYSE           | 301                      | 13                                  |
|              |                    | Euronext       | 956                      | 36                                  |
|              |                    | LSE            | 6,335                    | 64                                  |
|              |                    | Hong Kong Exch | 39,544                   | 18                                  |
| Fixed income | U.S Treasury 2yr   | ICAP BrokerTec | -                        | 8,342                               |
|              | U.S Treasury 5yr   | ICAP BrokerTec |                          | 2,974                               |
| FX           | Spot               | EBS            | -                        | $\sim 3.000$                        |
| Derivatives  | Index futures      | CME            | 3                        |                                     |
|              | Interest rate futs | LIFFE          | 10                       |                                     |

Source: WFE (2008), Fixed Income: Fleming and Mizrach (2008), FX: Euromoney (2006a)

#### **Table 9-4 Average trade sizes**

Electronic trading has helped significantly decrease order sizes, particularly for orderdriven venues. Consequently, the lowest average trade sizes/values in Table 9-4 are for the world's stock and listed derivative markets. In comparison, the fixed income and FX markets still have much larger average trade sizes. That said, actual trade sizes might be much lower than these averages. For instance, Galen Burghardt, in a report for the FIA (2006), showed that the most common trade size for E-mini S&P 500 futures was for a single lot.

When dealing with very low average trade sizes, signalling risk can be a major issue. Hence, we should consider splitting orders to ensure they are not significantly larger than those already on the order book. So we will need to use slicing or layering, alternatively we might need to hide them.

## Algorithm performance

Internally, most trading algorithms continually track their own performance. This might be versus a target executed quantity or as a comparison of its average executed price versus its benchmark. Therefore the algorithm can easily tell whether it is performing ahead or behind of its own targets.

The algorithm's reaction to under-performance will depend on whether market conditions are favourable and how much time there is left to trade. If conditions are unfavourable, it will probably employ more aggressive trading tactics to try to stem its losses. Conversely, if the conditions are favourable it might hold out for a while longer to see if the extant orders can achieve significant price improvement. Similarly, if there is not much time left to execute the algorithm may revert to using more aggressive execution tactics.

# Other factors affecting tactic choice

So far, the focus has been on targeting the specific investment/trading goals. Though, at the micro-level we must also consider market characteristics, such as its fundamental trading mechanism and latency.

## Trading mechanism

Clearly, whether a market is quote-driven or order-driven will have a substantial impact on the choice of trading tactic. Indeed, most of the mechanisms we have covered require specialised order types and so need an order-driven or hybrid market. They simply are not viable for request-driven markets. For purely quote-driven markets, we might still use order slicing to spread the order amongst several brokers, but that is about it. Likewise, most of the trading tactics we have covered are primarily intended for continuous trading periods.

The precedence rules that are used for order-driven markets are also significant. If priority is given in terms of price and time then it is important for orders to maintain their position in the queue. Thus, tactics such as layering become more valuable. Conversely, if the secondary priority is assigned on a pro-rata basis, such as for many futures markets, then it is important to have orders with sufficient size at that price level.

#### Latency

Latency corresponds to the time lag that can occur between sending an order and it reaching its intended destination, and so be able to participate in trading. This lag may be due to delays in the various systems that process the order, as well as the time it takes to actually transmit the information between locations. Latency has the most effect on order routing decisions, but it can also affect dynamic tactics, such as pegging or eatching.

A few years ago, latencies were measured in seconds. Although this can still be the case in some emerging markets, the major venues are all now vying to offer platforms with latencies measured in milliseconds or less. Finding an impartial comparison of latencies can be quite difficult, since each venue is keen to stress the speed of their platform. Table 9-5 shows the results of a round-trip test by Exponential-e (2009) for their routing service. This gives an idea of the order transmission times to some key market locations. Latency will be significantly higher for request-driven markets.

| From:    | To:       | Latency |  |
|----------|-----------|---------|--|
|          |           | ms      |  |
|          | Frankfurt | 10      |  |
| London   | New York  | 68      |  |
|          | Chicago   | 85      |  |
|          | Toronto   | 25      |  |
| New York | Zurich    | 90      |  |
|          | Tokyo     | 246     |  |
|          | Sydney    | 260     |  |

Source: Exponential-e (2009)

#### Table 9-5 A snapshot latency roundtrip comparison for some key locations

Clearly, sending orders to remote markets can add a considerable amount of latency. Hence, a number of venues now offer co-location services, whereby space is made available for client machines to reduce any transmission delays.

Latency reduces the probability of execution since by the time we have been able to respond another market participant will probably have beaten us to it. Therefore, a tactic like pegging is not suitable for higher latency venues since its reactive nature exacerbates the problem. Instead, it is better to adopt the order layering tactic, so if the market does move orders are already in place at a range of different price levels. The catching tactic may also be used when latency is high, to stem potential losses.

#### 9.4 Summary

- Execution tactics focus on the micro level choices that need to be made for the actual execution, monitoring the order book and managing order submission. They provide common mechanisms to achieve the goals of trading algorithms.
- ٠ Tactics are often based around existing order types, for instance, pegging and hiding. For venues that do not natively support these dynamic order types the tactic can adopt an order placement strategy that essentially mimics the required behaviour. They may also employ more complex logic than is currently available via native order types.
- A wide range of common trading mechanisms may be adopted:  $\blacksquare$ 
  - Slicing is a straightforward means of lowering impact. -
  - Hiding takes advantage of hidden order types or using an opaque ATS.
  - Layering places orders throughout the book to maximise execution probability and \_ the potential for price improvement.
  - Pegging provides dynamic adjustments, adjusting the price or even size of orders.
  - Catching uses a price latch to cut losses when the market moves away from us.
  - Seeking actively searches for hidden liquidity. \_
  - Sniping takes available liquidity without giving away our own requirements.  $-$
  - Routing determines the best destination for an order based on a range of criteria. -
- The main factors affecting the choice of execution tactic depend on both the current market conditions and how well the algorithm is actually performing.
- Trading algorithms may adapt to changing conditions by switching between execution tactics. Alternatively, they may use several tactics in parallel.
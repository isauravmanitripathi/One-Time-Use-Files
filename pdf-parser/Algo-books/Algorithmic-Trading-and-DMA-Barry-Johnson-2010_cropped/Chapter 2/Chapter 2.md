# *Chapter 2* Market microstructure

Market microstructure focuses on the key mechanisms involved in trading. It also helps explain many of the costs that arise.

#### Introduction $2.1$

Economics tends to abstract itself from the underlying mechanics of trading. Similarly, assetpricing theory focuses solely on the fundamental values of assets. Whereas the field of market microstructure<sup>1</sup> concentrates on the actual trading process, analysing how specific mechanisms affect both observed prices and traded volumes. Market microstructure helps explain many of the costs that prevent assets from achieving their fundamental values.

Interest in market microstructure has grown rapidly over the last two decades, alongside the rapid changes in the structure and technology of the world markets. Structural shifts have arisen due to globalization, the demutualization of many exchanges (to become profit-based enterprises) and increasing intra-market competition. Regulation has also played its part. For example, in the U.S., Securities and Exchange Commission (SEC) governance led to the creation of ECNs (Electronic Communications Networks), which have aggressively competed with exchanges for market share. The pace of technological change has also helped, as tools like DMA and algorithmic trading open up markets, lowering the barriers for entry and altering the balance between investors, brokers and dealers.

What topics does market microstructure actually cover? We can break down the theory into three key areas:

- Market structure and design ●
- Trading mechanism research .
- . Transaction cost measurement and analysis

The purpose of this overview is to provide a basic introduction to these key areas. For further reading, a concise practitioner's guide is given by Ananth Madhavan (2002). Whilst comprehensive reviews of the academic literature are provided by Bruno Biais, Larry Glosten and Chester Spatt (2005), Hans Stoll (2001) and an earlier work by Madhavan (2000). A more detailed conceptual review of trading and markets in general may be found in Larry Harris's (1999) book 'Trading and Exchanges'.

<sup>&</sup>lt;sup>1</sup> Mark Garman (1976) first used the term "market microstructure" in an article on market making. However, published market microstructure research dates back to the 17<sup>th</sup> Century, when Joseph De la Vega (1688) was analysing trading practices and pricing on the Amsterdam stock exchange.

#### $2.2$ Fundamentals

Before covering the key concepts of market microstructure in more detail, let's first address some of the fundamental features of trading and markets.

Markets exist to accommodate trade. A marketplace is intended to bring different participants together, allowing them to trade. Since supply and demand are not always evenly balanced, most markets also rely on intermediaries, such as brokers or dealers, to facilitate trading.

Liquidity characterizes the ease of trading on a given market or for a specific asset. Trading in highly liquid markets is much casier, and more efficient, than trading in illiquid ones. Given the importance of trade, and particularly given its increasingly global nature, it is useful to be able to compare markets in terms of their efficiency. The cost of an asset is not necessarily a fair measure since many other economic factors, such as currencies, interest rates or inflation, may affect this. Therefore, measures based on liquidity are often used instead.

#### Market function

The fundamental purpose of a market is to bring buyers and sellers together. Broadly speaking, the capital markets may be categorised into primary and secondary markets, based on the two stages of an asset's lifecycle. <sup>2</sup> The primary market deals with the issuance of new assets/securities. Subsequent trading of these assets takes place on the secondary markets.

New government bonds are generally issued via specialised auctions. For equities, the primary market is concerned with initial public offerings (IPOs), follow-on offerings and rights issues. Similarly, new corporate debt is generally placed using underwriters (usually a syndicate of banks).

Historically, the secondary market for bonds has often been "over the counter" (OTC), although there are now also substantial inter-dealer and dealer-to-customer markets. The situation is similar for the trading of foreign exchange and many derivative assets. Whilst for equities the main marketplaces are exchanges, although increasingly these must now compete with other venues such as ECNs and Alternative Trading Systems (ATSs).

The secondary markets are vital since investors will be more willing to provide capital if they know the assets may readily be traded. This flexibility allows them to withdraw capital when needed and to switch between assets. Thus, market microstructure research has mainly focussed on the efficiency of the secondary markets. In particular, examining the diverse range of market structures and trading mechanisms, as we will see in sections 2.3 and 2.4.

#### Participants

Conventionally, market roles have been defined by trading needs. The "buy-side" corresponds to the traditional customers, namely institutional and individual investors. Whilst the "sell-side" represents the brokers, dealers and other financial intermediaries who service customer needs. Brokers act as agents to facilitate the actual trading, whilst dealers (or market makers) trade on their own behalf trying to profit from offering liquidity. Speculators act independently, trading for themselves.

In comparison, the market microstructure models in academic literature tend to classify the participants based on the information they possess:

 $2$  Note this distinction is less meaningful for foreign exchange and derivatives.

- "Informed traders" are assumed to have private information, which enables them to accurately determine an asset's true value.
- "Liquidity traders" must trade in order to fulfil certain requirements, such as to release capital or to adjust the balance of a portfolio.

The models also often incorporate the style of trading: Active traders are classified as those who demand immediate execution of their orders (immediacy) and push prices in the direction of their trading, whereas passive traders effectively supply immediacy and so stabilize prices. Unsurprisingly, microstructure models have shown that over the long-run liquidity traders generally lose if they trade with informed traders. Likewise, passive traders tend to profit from active traders. Still, informed traders do not have it all their own way; they are vulnerable to information-leakage. Consequently, informed traders try to minimise this by seeking to trade anonymously or even altering their trading patterns to look more like a liquidity trader.

| Microstructure<br>model trader types |         | Actual<br>participants   |  |  |
|--------------------------------------|---------|--------------------------|--|--|
| Informed                             |         | Investors                |  |  |
| Liquidity                            | Active  | Investors<br>Speculators |  |  |
|                                      | Passive | Dealers<br>Investors     |  |  |

**Table 2-1 Microstructure model participants** 

Table 2-1 tries to map the model participants to their real world counterparts. The clearest link is for dealers. They act as passive liquidity traders, benefiting from offering liquidity to active traders, but at risk of losing to more informed ones; hence, their pricing tries to balance this information risk; The gains made from active traders should offset any potential losses. Conversely, speculators tend to take a more active, or aggressive, trading style. They often take advantage of short-term price moves, which may be contrary to longer-term expectations. For investors, the mapping is less clearly defined, since for any particular situation some investors will have more relevant, or valuable, information than others will. Hence, sometimes investors may actually be acting as liquidity traders, compared to other better-informed investors. The only way to tell is their ultimate profit (or loss).

#### Liquidity

Trading generally means converting an asset into cash or vice versa. How much this conversion actually costs may be represented by the liquidity of the asset, or the market it was traded on. This view of liquidity dates back to Harold Demsetz (1968). He expressed liquidity in terms of immediacy, which reflects the ability to trade immediately by executing at the best available price.

An asset's price is closely linked to its liquidity. For example, newly issued U.S. treasury bonds often have higher prices than older issues (termed "off-the-run") for the same maturity. This liquidity premium reflects the value of being able to readily convert the asset back to cash.

A liquid market or asset should have a lower cost for immediacy, i.e. trading costs. Liquid markets or assets will also usually have higher trading volumes. For instance, the stock market is generally more liquid than the real estate market.

Overall, we can characterise a market's liquidity  $^3$  in terms of three main features:

- $\bullet$ Depth
- Tightness ٠
- Resiliency  $\bullet$

Depth indicates the total quantity of buy and sell orders that are available for the asset, around the equilibrium price. Thus, a deep market enables us to trade large volumes without causing sizeable price movements (or impacts). Conversely, a shallow market means it is much harder to trade; often we will have to alter our price to attract buyers or sellers.

Tightness refers to the bid offer spread. That is to say, it is the difference between the prices to buy and sell an asset. A tight spread means that the trading costs are low (for average quantities) and so it is relatively easy to trade in and out of a position.

Resiliency determines how quickly the market recovers from a shock. A resilient market will suffer less price discrepancies from trading. So changes in price do not affect the overall level of trading, or availability of orders.

These three factors are closely related: deeper markets generally have narrower bid offer spreads (so are tighter) since they are easier to trade in, and so less risky. This also makes them more likely to be resilient.

Another potential factor, *Diversity*, is suggested by Avinash Persaud (2001). His study of market crises, titled 'Liquidity Black Holes', highlighted the importance of a diverse range of market views amongst investors and traders. Without such diversity, everyone wants to buy or sell at the same time or price, so liquidity is bound to disappear. Fortunately, for most markets, there is generally a great deal of diversity in opinions. Though, as Persaud points out, periodically a convergence of market sentiment helps trigger crises, such as the 1987 stock market crash or the 2007-09 financial crisis.

#### Market structure and design 2.3

For markets to work well, their design must accommodate the needs of institutional (or individual) investors, dealers and speculators. Therefore, a successful market allows investors to trade when they want, and minimizes the costs of trading orders whilst still making it worthwhile for dealers and speculators.

The key characteristics of market architecture  $^{4}$  may be defined as:

- $\bullet$ Market type
- Order types  $\bullet$
- ٠ Trading protocols
- Transparency
- Off-market trading

These characteristics can significantly influence factors such as liquidity and the speed of

<sup>&</sup>lt;sup>3</sup> As outlined by Fisher Black (1971) and Albert Kyle (1985) in their papers on continuous auction markets.

<sup>&</sup>lt;sup>4</sup> Based on a list by Madhavan (2002).

price discovery, which in turn can affect the overall cost of trading. However, no two markets are the same, even if they are based on the same design, since local regulations may differ, as will the universe of traded assets.

# **Types of markets**

Historically, the two most important properties for classifying markets are their trading mechanism and the actual frequency of trading:

# Trading mechanism

Markets are generally thought of as being either quote-driven, order-driven or a mix (or hybrid) of the two. A purely quote-driven market means traders must transact with a dealer (or market maker) who quotes prices at which they will buy and sell a given quantity. Orderdriven markets allow all traders to participate equally, placing orders on an order book that are then matched using a consistent set of rules. Figure 2-1 tries to highlight these differences.

| Market maker's two-way quote:<br>Off size<br>Offer<br><b>Bid size</b><br>$\text{Bid}$<br><b>Bid size</b><br>Bid<br>52.0<br>500<br>52.0<br>53.5<br>1,000<br>500<br>"Take the offer"<br>1.<br>1.<br>Place buy market order,<br>or buy limit order matching best<br>Off size<br>Bid size<br>Bid<br>Offer<br>offer |                            |  |  |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--|--|--|--|
|                                                                                                                                                                                                                                                                                                                | Best bid and offer orders: |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                | Off size<br>Offer          |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                | 53.5<br>1,000              |  |  |  |  |
| 52.0<br>500<br>53.5<br>1,000                                                                                                                                                                                                                                                                                   |                            |  |  |  |  |
| "Hit the bid"<br>2.<br>2.<br>Place sell market order,<br>or sell limit order matching best<br>Off size<br>Bid size<br>Bid<br>Offer<br>bid<br>Potential actions<br>52.0<br>53.5<br>500<br>1,000                                                                                                                 |                            |  |  |  |  |
| Place passive sell order<br>3.<br>3a.<br>Negotiate,<br>or leave limit order                                                                                                                                                                                                                                    |                            |  |  |  |  |
| <b>Bid</b> size<br>$\text{Bid}$                                                                                                                                                                                                                                                                                | Off size<br>Offer          |  |  |  |  |
| 52.0<br>500                                                                                                                                                                                                                                                                                                    | 53.5<br>1,000              |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                | 54.0<br>1,000              |  |  |  |  |
| $3h$ .<br>Set market with new sell order                                                                                                                                                                                                                                                                       |                            |  |  |  |  |
| <b>Bid size</b><br>Bid                                                                                                                                                                                                                                                                                         | Offer<br>Off size          |  |  |  |  |
| 52.0<br>500                                                                                                                                                                                                                                                                                                    | 53.0<br>1,000              |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                | 53.5<br>1,000              |  |  |  |  |

## Figure 2-1 Comparing quote-driven and order-driven trading mechanisms

For a quote-driven market, when faced with a two-way quote we can choose to "take the offer", "hit the bid", renegotiate or just leave it. Choosing to "take the offer" results in a buy

execution priced at their offer, whilst hitting the bid results in a sell. The market maker's two-way quote provides a guaranteed execution at that price, for a set size.

With an order-driven market, the prices are established by actual orders. The best bid price represents the highest priced buy order, whilst the best offer is set by the lowest priced sell order. A trade may only occur when a buy order matches (or betters) the current best offer price, whilst for a sell order the best bid price is the target. So instead of responding to the market maker's two-way quote we react to the available liquidity on the order book. The outcome also depends on the type of order used. A market order tries to guarantee execution regardless of price, whilst a limit order sticks to a strict price limit but sacrifices execution certainty. The equivalent to "taking the offer" is to place cither a market order, or a limit order priced to match the best offer. Its size should be equal to or less than the available offer size. Conversely, we can "hit the bid" by placing a sell market order, or a limit order priced to match the best bid. Note that there are no guarantees, since at any moment many other traders will also be issuing new orders, updating existing ones and cancelling stale ones. By the time we react and place an order, it is quite possible that another order has already matched with the current best bid or offer. Hence, a buy (sell) market order may execute but potentially at a higher (lower) price than the currently displayed best offer. Alternatively, a limit order may fail to execute, in which case it will stay on the order book until it matches with another order or is cancelled. Therefore, for order-driven markets the best bid and offer prices are indicative rather than guaranteed like a dealer's firm two-way quote.

Whilst the immediacy of the two-way quote is useful, the persistence of orders within order-driven systems is also beneficial since they provide visible liquidity, which enhances price discovery. Order-driven markets also offer more control over order choice. Orders may be placed for any preferred price and size without the need for negotiation. For example, believing that the price will rise, we may choose to issue a more passive sell order priced just above the current best offer. Effectively, this will join the queue behind the best sell order, as shown in panel 3a. Alternatively, we may choose to set a new market level, at a price slightly lower than the best offer, shown in panel 3b.

Negotiation is a key difference between order-driven and quote-driven markets. Many quote-driven markets, even electronic ones, provide a mechanism that allows both counterparties to negotiate the size and/or price. The creation of new crossing systems and ATSs, such as Liquidnet, which also incorporate negotiation mechanisms mean that this is no longer limited to purely dealer-based markets. However, there is no direct equivalent to this mechanism for purely order-driven markets. The closest approximation is to place an order for our desired size and price, and then closely monitor and update it to try to ensure it is executed. But this is still far from entering into a bilateral negotiation. In fact, this difference is so fundamental that it can be used as a key factor in the categorisation of trading mechanisms.

Despite these differences, Figure 2-1 also highlights some clear similarities between a dealer's two-way quotes and using orders. A market where dealers must provide continuous firm quotes effectively forces them to constantly offer limit orders. In many ways, this may be thought of as a hybrid market. Indeed, markets such as NASDAQ, which used to be purely quote-driven, have since shifted to become truly hybrid markets, incorporating much of the same functionality as order-driven markets. In comparison, a market where the dealers' quotes are only indicative remains a purely quote-driven market, since we must still request a separate firm quote.

## Trading frequency

The frequency of trading is the other main classifier for the structure of markets, since this determines when requirement matches (whether they are from quotes or orders) are actually turned into executions. Generally, markets provide one or more of the following types:

- Continuous trading  $\bullet$
- Periodic trading  $\bullet$
- ٠ Request-driven trading

Continuous trading provides a convenient and efficient means of execution. Although such immediacy can lead to price volatility, particularly when there is an imbalance between supply and demand. Periodic trading is generally scheduled for specific time/s in the day. The time period beforehand permits more considered price formation, it also allows liquidity to accumulate. Request-driven trading means requesting a quote from a market maker, whilst it may be convenient it is not necessarily as efficient in terms of the price achieved.

## **Classifying major market types**

Based on these two key properties, a wide range of market types is possible; some examples are highlighted in Table 2-2.

|           |                         |                                                                                           |                                                                                           | Mechanism                                                                |                                                                                    |
|-----------|-------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|           |                         | Order-driven                                                                              |                                                                                           | Hybrid                                                                   | Negotiation-based                                                                  |
|           | Continuous              | $\bullet$ CDA<br>Cont. blind<br>crosses/ATS<br>Instinct CBX<br>LeveL<br>Internal crossing | CDA w/LP<br>CME<br>Continuous<br>advertised<br>crosses/ATS<br>Pipeline<br>ITG POSIT Alert | Cont. dealer<br>(firm quote)<br>MTS<br>$\bullet$ RFS                     | Cont. dealer<br>(indicative quote)<br>Cont. negotiated<br>crosses/ATS<br>Liquidnet |
| Frequency | Continuous<br>with call | • CDA<br>Tokyo SE                                                                         | CDA w/LP<br>Euronext,<br>LSE,<br>Eurex                                                    | Hybrid dealer/<br>order book<br>NYSE,<br>NASDAQ<br>ICAP BrokerTec<br>EBS |                                                                                    |
|           | Scheduled<br>Call       | Call auction<br>Euronext illiquid<br>Crossing sys<br>ITG POSIT.<br>Instinct crosses       |                                                                                           |                                                                          |                                                                                    |
|           | Request                 | Dealer limit<br>order                                                                     |                                                                                           |                                                                          | Dealer RFQ<br>"Upstairs"<br>trading                                                |

## Table 2-2 Market types organised by their mechanism and trading frequency

The corners of this table correspond to the extremes, whilst the centre shows the more hybrid "mix 'n match" approach. Notice that the trading mechanism classification actually uses "negotiation-based" which encompasses the quote-driven approach. Before we move on to consider other factors in market design, it is worth briefly reviewing some of the key market types shown in Table 2-2:

CDA stands for Continuous Double Auction; this is simply an order-driven continuous auction market. Its name is derived from the fact that it supports simultaneous buy and sell auctions. The CDA mechanism is synonymous with Central Limit Order books (CLO) which form the basis for most order-driven markets. As each new order arrives, is updated or cancelled the matching process checks the order book for any orders that match.

Continuous dealer markets ensure that the market makers constantly update two-way quotes to reflect their latest prices. They may be subdivided into those where the dealers provide either firm or indicative quotes. Markets based on firm quotes, including Requestfor-streaming (RFS) mechanisms, effectively force the dealers to constantly maintain limit orders. This corresponds to a more hybrid mechanism, which may even be able to cater for anonymous trading. As mentioned carlier, venues where indicative quotes are used represent a more negotiation-based (or quote-driven) approach.

At the other end of the spectrum are request-driven mechanisms such as single dealer Request-for-quote (RFQ) platforms. Likewise, the traditional "upstairs" trading for large block orders is purely request-driven. Whilst requesting a limit order from a dealer effectively places an order on their private order book.

Scheduled, or periodic, call auctions are generally set for specific time/s in the day. The period before the auction allows orders (and so liquidity) to accumulate. The auction process then matches buy and sell orders, usually by attempting to find a single clearing price that maximizes the amount executed. By forcing trading interest to wait, orders may accumulate ready for the auction call, helping to reduce volatility. The successful pooling of liquidity also means they are often used for less liquid assets.

Hybrid markets offer elements of both order-driven and negotiation-based markets. Notice that in Table 2-2 the hybrid mechanism column is actually sub-divided. This loosely represents the markets that were originally based on either an order-driven or a negotiationbased approach. Hence, CDA markets, such as Euronext, which have become hybrid by allowing dedicated Liquidity Providers (w/LP) to improve their overall liquidity, are shown on the left hand side. In comparison, NASDAQ effectively converted itself from a quotedriven market into a hybrid order book by extending its multiple dealer platform to support displayed limit orders. So, NASDAQ is shown on the right hand side of this column.

Many markets now incorporate both continuous and call auctions. Combining these two mechanisms types offers the convenience of continuous execution with the stabilising effect of the call. Therefore, many continuous auction markets now use call auctions for their most volatile periods, namely the open and close, and after trading halts for liquidity or price suspensions. Some markets even incorporate additional intraday call auctions.

The scheme shown in Table 2-2 may also be used to categorise the various types of "dark pool" Alternative Trading Systems (ATSs). Essentially, this follows the approach outlined by Jeromee Johnson from the TABB Group (2006), which classifies crossings as scheduled or continuous and either blind, negotiated, advertised or internal. Scheduled crosses, such as ITG's POSIT, are similar to scheduled call auctions, except the liquidity is hidden. Continuous blind crosses, such as Instinet's CBX, are effectively a CDA where the order book remains completely opaque. A similar mechanism is adopted for brokers' internal crossing systems. Continuous negotiated crossing platforms constantly search for potential matches notifying each participant when one is found. This then allows them to enter into an anonymous bilateral negotiation for both the size and price. Continuous advertised crossing systems, such as Pipeline, highlight when liquidity is present, without giving away the size.

This allows participants to place firm orders to execute with it.

In general, the trend for market design seems to be towards the centre of Table 2-2. In other words, continuous trading based on hybrid mechanisms, often with additional call auctions to help start and/or close the market. This approach is increasingly being adopted by the world's leading market venues. That said, notable innovations are also occurring in other areas, mainly due to the advent of crossing systems and ATSs. Exactly what the markets of the future will look like is still far from certain.

## Order types

Orders also play an important role in market structure. An order is simply an instruction to buy or sell a specific quantity of a given asset. Market microstructure tends to differentiate orders both by their liquidity-effect and by their associated risks. The two main types are:

- Market orders these are directions to trade immediately at the best price available. Hence, they demand liquidity and risk execution price uncertainty.
- $\bullet$ Limit orders - these have an inbuilt price limit that must not be breached, a maximum price for buys and a minimum price for sell orders. Thus, limit orders can help provide liquidity but risk failing to execute.

Note that markets may also differ in terms of the behaviour of these order types. For instance, a limit order placed with a dealer may be kept hidden until the market conditions are right, in which case it does not provide visible liquidity. Whereas in a pure order-driven market such a limit order immediately goes on the central order book and is visible, provided that the order book is sufficiently transparent.

A wide range of conditions may also be applied to each order. These allow control over when each order becomes active, their duration and whether they may be partially filled. Conditions may even be set which direct the order to specific dealers or venues.

Using these conditions and incorporating additional special behaviours has enabled venues to offer a wide range of order types. For example, hybrid orders such as market-to-limit orders actually have some of the properties of both market orders and limit orders. Whilst conditional orders allow orders to become active, only once a specific condition is true. For instance, stop orders are activated when the market price exceeds their internal stop limit, Hidden and iceberg orders are also becoming increasingly important, as traders try to achieve the best price for their orders without disclosing all the associated liquidity.

Each market supports a diverse set of conditions and order types. In Chapter 4, we shall cover these in much more detail.

## **Trading Protocols**

Markets need to provide a "fair and orderly" trading environment. They achieve this by defining suitable trading rules or protocols and then applying them rigorously. The rules cover everything from:

- $\bullet$ order precedence
- requirements for trade sizes  $\bullet$
- pricing increments  $\bullet$
- specifying how the market actually opens and closes
- mandating how it reacts to asset and market-wide events

So they can have a considerable effect on the efficiency of trading on a given market.

Order precedence: These rules specify how incoming orders execute with existing orders or dealer quotes. Generally, markets give most priority to orders with the best price, with secondary priority based on the time of order entry. Alternatively, some give secondary priority based on order size.

Minimum trade quantities: Also known as lot-sizes, these limits can vary from a single unit to a thousand or more. Retail investors prefer the flexibility of smaller lot sizes, so markets can use lot-size rules to help control the mix of institutional and retail investors.

Minimum price increments: Also known as tick-sizes, these limits affect the spread between the bid and offer prices. Larger increments increase the spread and so make it more profitable to provide liquidity (both for dealers and for users of limit orders). But if the tick size is too small then time-based order priority can become meaningless, as noted by Larry Harris (1991). Setting a new market price is cheap for small ticks, so the temptation is to step in front of other orders in order to maintain priority. In the U.S., this is often referred to as "pennying".

Opening/closing procedures: The specifics of how (and when) the market opens and closes, and what constitutes the official opening and closing prices. Microstructure research has shown that price discovery can be made more efficient by batching orders in periodic call auctions. Many types of markets now use call auctions to open and/or close the market.

Trading halts and circuit-breakers: A trading halt may be called for regulatory reasons, for example, just before a company makes an announcement that may significantly affect its stock price. Alternatively, it may also be triggered by a large price move. Halting the trading allows the market time to assess the new information, and may reduce the impact when trading restarts. Alternatively, trading may be switched temporarily to a special call auction to reduce the volatility of trading. Circuit-breakers concern market-wide events, they are designed to protect against mass selling during large market declines. For example, the NYSE has breakers set at thresholds for 10, 20 and 30% of the Dow Jones Industrial Average (DJIA). If these are reached, the market may halt for 1-2 hours or even completely close.

#### Transparency

Transparency represents the amount of market information that is available before and after a trade has occurred. Pre-trade information corresponds to the prices and sizes of quotes or orders. Post-trade information relates to actual trade execution details, namely the time, size and price.

Quote-driven markets tend to be less transparent than order-driven ones since they only ever show a broker's best bid and offer. The bilateral nature of quote-driven trading means that both parties usually know who they are dealing with. Multi-broker markets improve visibility slightly by making it easier to compare quotes from a range of market makers. If the market makers provide firm quotes then there is also the possibility of anonymous trading.

Order-driven markets tend to offer much higher visibility. Certainly, the most transparent market is a fully displayed order book, which shows the owners of each order and with no hidden order volume, where trades are reported promptly and publicly. Still, such complete transparency is not appealing to all users. In particular, institutional traders generally need to reduce the potential impact of large orders, which is difficult if each of their orders is clearly

identifiable. A common solution is to make the order book anonymous. Increasingly, markets are also allowing hidden orders, providing traders control over the visibility of their total order volume.

Venues which specialise in handling large block orders, such as the "dark pool" ATSs, tend to be opaque. This allows traders to place large orders without fear of signalling their intentions to other market participants. Obviously, it is much more difficult to discover the market price for an asset when limited information is available. Therefore, these opaque venues tend to be most successful when there is also a large and highly visible market from which fair market prices may be determined. Hence, ATSs have so far seen the most success in the U.S. equity marketplace, although they are rapidly spreading globally.

In general, the trend across most markets, and asset classes, appears to he increasing transparency but with anonymity. In fact, several markets, which had fully disclosed broker identities, have now moved back to voluntary identification or completely anonymous trading. Nevertheless, the success of ATSs means that there will also continue to be a large and growing number of completely opaque markets.

#### After-hours and off-market trading

The globalisation of investment and trading means that there is an increasing demand for access to trade 24x7. So the provision of after-hours and off-market trading is another key differentiator for markets.

After-hours trading can be particularly useful for cross-border trading, helping to compensate for time zone differences. Large block traders also sometimes take advantage of the extra trading opportunities. Though, a different trading approach may be required, since out-of-hours liquidity may be substantially lower. Price changes during after-hours trading can also act as an indicator for the next days open.

Off-market trading takes two main forms, the same assets can be traded on a range of venues in the same country, alternatively new assets may be created to permit dual listing in foreign markets. For instance, taking the US equities market as an example, stocks may be listed on exchanges, such as NYSE and NASDAQ. Links between the venues allow trading most NYSE stocks on the other exchanges as well as across a range of ECNs and ATSs. The same applies for NASDAQ listed stocks. For non-U.S. companies depository receipts allow their stocks to be effectively traded on US venues.

Having such a wide range of possible execution venues has led the US equity market to be described as fragmented. Hans Stoll (2001) provides a valuable discussion of the issues between market centralisation and fragmentation. Essentially, centralisation benefits from two factors, economies of scale and network externalities. Both of these factors offer the most advantage to the "first-mover"; hence, well-established primary markets tend to benefit most. For example, high trade volumes allow a venue to reduce its average cost per trade duc to economies of scale. Similarly, the trade volume and number of participants affect the probability of trading. Again, this makes established markets more attractive to traders since they offer a higher likelihood of successful execution.

On the other hand, market fragmentation benefits from a range of closely related factors:

- Market transparency
- Technological changes  $\bullet$
- Regulatory policy  $\bullet$

As we saw in the previous section, market transparency enables venues (such as ATSs) to reliably guarantee to match the main market best prices. Without this, traders must participate on the main market just to discover the price. Likewise, technological improvements have made it easier to distribute prices and orders between venues. Many regulatory bodies are also mandating transparency in order to encourage competition. In the U.S. equities markets, regulation has also encouraged markets to link together, allowing other venues to compete directly with the main markets. Thus, traders can participate with a range of venues either directly or indirectly.

To capture order flow from more established markets the competing venues often have to offer additional functionality, such as anonymity or better handling for block orders. Some even offer inducements, either through reduced costs for liquidity providers (giving rebates for orders which supply liquidity) or via direct payments to brokers to capture order flow (which has been criticised since the payment does not go to the customer).

As Stoll (2001) points out, so long as markets are linked then the consequences of market fragmentation can be relatively minor. One of the main issues is that fragmented markets are only really capable of supporting price priority. Though, this can be broken when a large order "walks the book" and trades through a range of prices at one venue. Secondary priorities, such as time, are not fully supportable across multiple linked markets at present. Note that liquidity-driven trading algorithms and smart order routing can be used to cope with this.

Most markets are in a state of constant flux; new trading venues keep appearing whilst fierce competition has resulted in many either merging or failing. The only certainty is that existing markets will have to keep adapting to cope with these changes.

# Other important market design features

Although the trading mechanism and frequency arc the main determinants of market structure, other market features can still have a marked effect, namely:

Means of price discovery: Most markets have an inbuilt price discovery mechanism. For instance, a market maker's two-way quote or the best buy and sell orders on an order-driven market, which reflect the current best bid and offer prices. However, some markets do not have a dedicated pricing mechanism; instead, they take reference prices from another market (generally from the principal market). This approach tends to be more suitable for block trading.

Intraday breaks: Some markets remain closed around lunchtime, such as the Hong Kong, Singapore and Tokyo stock exchanges.

Automation: A high level of automation helps reduce the distinction between market makers and other traders. Less automated or manually handled markets offer delays, which give dealers opportunities to become more informed (cither from new information, new orders or new trades).

Segmentation: A "one size fits all" approach does not generally work well for all assets. Thus, many markets now employ a more segmented approach, using a continuous orderdriven mechanism for the most liquid assets and a periodic call auction for the least liquid.

Market design is constantly evolving, driven by competition, regulation and technology. In the future, other market design features may well become more important. For instance, complex order books are able to deal with linked orders between assets; these allow derivative and even multi-asset trading strategies to be adopted.

#### 2.4 Trading mechanism research

The trading process can be broken down into three key stages:

- 1. Price formation
- 2. Price discovery / trade execution
- 3. Reporting, clearing & settlement

In other words, we first need to decide on the price we are willing to trade at, referred to as price formation. Secondly, for a trade to occur we need to find a counterparty that is prepared to trade with us at this price, also termed price discovery or trade execution. Finally, the trades are reported and the clearing and settlement processes handle the required cash flows and transfers of ownership.

Most research has focussed on the first two phases, trying to determine the relationships between market structure, trading volume, prices and trading costs.

#### Price formation

Investors tend to have different views on the future value of an asset; in part, this is because they have varying levels of information. Consequently, their valuations target diverse prices. Therefore, price formation for an asset is usually based on supply and demand conditions. It is also affected by the fundamental market mechanism, i.e. quote-driven or order-driven. Market microstructure researchers have used a wide range of models to investigate this process; Chapter 8 provides a more detailed review of these.

Ouote-driven markets are a perfect starting point for analysis into price formation since the very nature of market makers is to quote prices. Information-based models assume that some participants have a definite information advantage over others. The bid offer spread represents the cost for which market makers are prepared to trade. Essentially, this spread should generate enough returns to cover their costs and any losses from trading with more informed traders. Inventory-based models derive the dealer's quote based on their inventory (or position). This just needs to be sufficient to service any incoming orders. So the market maker's bid offer spread often tends to increase as their position moves further from their ideal inventory.

For order-driven markets, price formation is more complex since there are many more participants, each with their own opinion. Order-driven markets are generally based around a central limit order book, which contains every live order for the asset. The screenshot shown in Figure 2-2 displays a typical order book trading screen. Orders are arranged by their limit price with the best prices at the top. The top buy order has the highest buy limit price, in this case 336,00, whilst the top sell order has the lowest sell limit price, at 336.75.

Note that the best bids and offers shown in Figure 2-2 are actually aggregated totals, designed to quickly show the quantity available at each price point. The outermost column shows the number of orders in each total; it may also show any specific owner identifiers, such as FIRM, CMPY. So the 10,800 available to sell at 337.25 is actually composed of two separate orders. Figure 2-3 shows an alternate view of this order book, expanding it to illustrate each of the underlying orders (in this case S6 and S8) which make up these totals.

Clearly, the transparency of the order book has a marked effect on the price formation. If only the best bid and offer quotes are displayed, as shaded in Figure 2-3, then effectively the order book is reduced to being like a market maker's two-way quote. This adds a degree of uncertainty since traders cannot tell what other liquidity might be available. This additional risk could lead to orders being priced more aggressively than is necessary.

|                                   | Listed Company                                                                 |                                                                           | LCPY                                                                           |                       | P                                                       | Close                                                                    | 336                                                                         | GBX                          |
|-----------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------|---------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------|
| NMG 25,000                        |                                                                                | Segment SET2                                                              |                                                                                |                       |                                                         | Sector FT25                                                              | ISIN<br>YVel                                                                | GE0009529859<br>1.00m        |
| Last<br>Prev                      | 336<br>AT<br>336<br>335AT                                                      | at<br>08:45<br>335AT                                                      | Vol<br>335AT                                                                   | 7.807<br>336AT        |                                                         |                                                                          |                                                                             |                              |
| Trade Hi<br>Trade Lo<br>Total Vol | 337<br>335<br>107,899                                                          | Open<br>WWAP                                                              | SETS Vol.                                                                      | 336<br>335%<br>52,807 |                                                         | Current<br>Current Hi<br>Current Lo                                      | 336<br>336<br>335                                                           | $\pm 0$<br>$\pm \beta$<br>-1 |
| BU'                               | 109,537<br>TVol<br>MOVal                                                       |                                                                           | Base 336                                                                       |                       |                                                         | TVol<br>MOVol                                                            | 62,892                                                                      | SELL                         |
|                                   |                                                                                | 8,000                                                                     |                                                                                | 336 - 3363/4          |                                                         |                                                                          | 2,700                                                                       |                              |
| CMPY<br>FIRM                      | 8,000<br>23,000<br>24.082<br>34.082<br>59.082<br>109,082<br>134,082<br>135.082 | 8,000<br>15,000<br>1.082<br>10.000<br>25.000<br>50,000<br>25,000<br>1,000 | 336<br>334<br>$333\frac{1}{2}$<br>332<br>329<br>325<br>$324\frac{1}{2}$<br>300 |                       | 336%<br>337<br>337 %<br>340<br>345<br>350<br>365<br>420 | 2,700<br>25,000<br>10,800<br>25,000<br>10,000<br>1,000<br>7,000<br>6,000 | 2.700<br>27,700<br>38,500<br>63,500<br>73,500<br>74.500<br>81,500<br>87,500 | FIRM<br>2<br>CMPY            |

Source: © LSE (2006a)

Reproduced with permission from London Stock Exchange PLC

Figure 2-2 A typical order book trading screen

|             |         | Buys   |       | Sells  |        |         |             |
|-------------|---------|--------|-------|--------|--------|---------|-------------|
| td          | Time    | Size   | Price | Price  | Size   | Time    | $\text{Id}$ |
| B8          | 8:25:00 | 8,000  | 336.0 | 336.75 | 2,700  | 8:25:00 | S7          |
| $\text{B1}$ | 8:20:25 | 15,000 | 334.0 | 337.0  | 25,000 | 8:25:30 | S9          |
| B5          | 8:23:25 | 1,082  | 333.5 | 337.25 | 4,000  | 8:23:00 | S6          |
| B7          | 8:24:09 | 10,000 | 332.0 | 337.25 | 6.800  | 8:25:25 | S8          |
| B3          | 8:20:25 | 25,000 | 329.0 | 340.0  | 25,000 | 8:20:25 | S2          |
| B4          | 8:21:00 | 50,000 | 325.0 | 345.0  | 10,000 | 8:20:42 | S3          |
| B6          | 8:24:05 | 25,000 | 324.5 | 350.0  | 1,000  | 8:21:50 | S4          |
| B2          | 8:20:40 | 1,000  | 300.0 | 365.0  | 7,000  | 8:22:20 | S5          |
|             |         |        |       | 420.0  | 6,000  | 8:20:00 | S1          |

Figure 2-3 A simplified representation of an order book

On the other hand, if the entire order book is visible, or even just the best five orders, traders can immediately see the range of available prices and volumes. By using the visible liquidity, they can then adjust their valuations to determine their own price for the asset.

Note that sometimes the best bid and offer price might temporarily be the same, in which case the market is said to be "locked". If the best offer price is below the best bid, it is termed "crossed". These situations can arise in some markets where the prices are based on multiple dealers, or take feeds from other venues. Each market will have its own way of dealing with this, getting the order book back to normal as quickly as possible.

# Price discovery / trade execution

Price discovery is synonymous with trade execution, it occurs when supply and demand requirements cross. The actual price at which this happens is determined by the mechanism. There are three main types of discovery mechanism:

- Bilateral trading  $\bullet$
- Continuous auction  $\bullet$
- Call auction

Bilateral trading is mainly used for quote-driven and negotiation-based trading, whereas order-driven and hybrid markets adopt more multilateral auction-based mechanisms. The main difference between the two types of auction is the frequency. Unlike continuous auctions, call based auctions allow orders to accumulate for some time before the actual discovery (or matching) takes place.

Note that some markets do not have an independent price discovery mechanism: An auction takes place, but the execution price is derived externally (often from the primary market). As an example, we will see how a mid-point match works for continuous auctions.

#### **Bilateral trading**

As its name suggests, bilateral trading represents one-to-one trading mechanisms. Therefore, it is mainly used for quote-driven and negotiation-based trading, although some hybrid markets also support this method.

A market maker's two-way quote states both the prices and quantities that they are willing to trade at. The bid price represents what they will pay to buy an asset whilst the offer is what they will sell it for. As we saw in Figure 2-1, price discovery only occurs if a client is prepared to deal at these prices. In which case, they may then "hit the bid" (sell) or "take the offer" (buy). Alternatively, they can try to renegotiate a new price, often for a different quantity, or simply walk away.

The one-to-one nature of bilateral trading means that each party generally knows the other's identity. This allows the market maker to tailor their quote based on the client. In particular, they can estimate the risk of adverse selection and incorporate this into their quote. Note that some protection is given to clients by the two-way quote, since they do not have to immediately disclose whether they are buyers or sellers, which could prejudice the market maker's price.

Multi-dealer systems do not change the fundamentals of a bilateral trading mechanism, but they can help speed it up. As Figure 2-4 shows, by aggregating the market maker quotes a customer can easily see the available prices and sizes without having to contact them individually. For simplicity, each broker is shown on a separate row, together with a shaded row for the best bid and offer quotes. Although many systems allow this view to be sorted by price, so that it looks like an order book.

| $\mathrm{Id}$    | $\text{Bid}$<br>size | Bid  | Offer | Offer<br>size | td                  |
|------------------|----------------------|------|-------|---------------|---------------------|
| BrokerC          | 700                  | 52.1 | 53.4  | 900           | <b>BrokerD</b>      |
| BrokerA          | 500                  | 52.0 | 53.5  | 800           | BrokerA             |
| BrokerB          | 1,000                | 52.0 | 53.5  | 1,000         | Broker <sub>B</sub> |
| $\text{BrokerC}$ | 700                  | 52.1 | 53.6  | 500           | $\text{BrokerC}$    |
| $\text{Broker}D$ | 800                  | 52.0 | 53.4  | 900           | $\text{Broker}D$    |
| $\n  BrokerE\n$  | 1,000                | 51.9 | 53.5  | 700           | BrokerE             |

Figure 2-4 An example multi-dealer quote view

Price formation is still done by the dealers, although in a multi-dealer environment they will often need to provide continuous updates. This gives us a better idea of their prices, without even having to contact dealers, and so give away our interest. For markets where they are obliged to make firm quotes, such as NASDAQ, we can then immediately hit or lift a quote to trade. Some hybrid markets also support special order types that allow clients to direct orders to specific market makers. For example, NASDAQ used to provide a directed non-liability order that could be routed to a specific market maker. They were then allowed to choose whether they accepted the order. The market maker could also opt to accept part of the order, try to renegotiate a deal or just decline the order, all within a fixed time limit (5s).

For some multi-dealer systems, the price quotes are merely indicative, so we must click on a broker to issue a "request for quote" (RFQ). This will then signal our interest to the market maker, who will then give a quote, as shown in Figure 2-5.

![](_page_15_Figure_3.jpeg)

Figure 2-5 An example Request For Quote (RFQ) mechanism

Note that Figure 2-5 depicts a two-way quote, but many RFQ systems only support oneway quoting, so the client must also state whether they wish to buy or sell the asset.

Streaming quotes via "request for stream" (RFS) is another alternative. With RFS, we are actually requesting a stream of updates rather than a single one-off quote, as shown in Figure 2-6. Since each new update is a firm quote, we can decide whether to trade with the dealer by hitting or lifting. Alternatively, we can opt to wait and see whether the price improves for subsequent updates. Whilst it is still not quite the same as trading on a continuous order book, this is a much more dynamic approach than RFQ-based trading, since the onus has now shifted to the dealer to provide a continuously updating stream of firm quotes.

Typically, these request-driven approaches are used in the fixed income (mainly RFQ) and foreign exchange (both RFQ and RFS) markets.

Anonymous bilateral mechanisms have also been introduced, most notably Liquidnet's crossing service. Requirements for buys or sells are entered anonymously. If the system finds a potential match, it then creates a negotiation session between the two parties. Each counterparty can see a scorecard for the other. This summarises their history of previously successful negotiations, allowing them to gauge the validity of each other. They can then negotiate the quantity, whilst the price is often set by the primary market, such as the U.S. National Best Bid and Offer (NBBO). Only after successful execution may their actual identities become known.

![](_page_16_Figure_1.jpeg)

3. For each new quote client must decide whether to hit/lift or ignore

## Figure 2-6 An example Request For Stream (RFS) mechanism

## **Continuous auction**

The continuous auction mechanism consistently applies the matching rules each time an order is added, updated or cancelled. This is a multilateral process with many different traders all placing and amending orders. Therefore, a queuing system is needed to ensure that each order is processed in turn, as shown in Figure 2-7.

![](_page_16_Figure_6.jpeg)

Figure 2-7 An example continuous auction mechanism

For each order, the following steps are applied:

- $\bullet$ The order instruction is added to the internal order book
- $\bullet$ Trade matching rules are then used to see if any matches are now possible
- The order book is updated to reflect any changes  $\sim$
- Execution notifications are sent for any resultant matches  $\bullet$

Then the cycle simply starts all over again for the next order instruction in the queue. In terms of the actual trade matching, strictly defined rules are consistently applied. Typically, markets give the highest priority to orders based on price, but a variety of approaches is used for the secondary priority. The two most common are time and pro-rata, some markets also give priority to the first order at a set price point whilst others may even give priority to specific users.

Price/time based trade matching is common in most equities markets. The highest priced buy orders and the lowest priced sells are rewarded with the highest probabilities of execution. For orders at the same price, the time they were placed is then used to distinguish between them, thus favouring earlier orders.

Price/pro-rata trade matching is more common in futures markets. Again, the best priced buy and sell orders take priority, but allocation between orders at the same price point is done on a pro-rata basis. So each order is allocated based on its proportion of the total volume of orders at that price. Thus, rewarding larger orders rather than those placed earlier.

For example, let's look at how a market order to buy 1,000 EEE might be handled for the order book shown in Figure 2-8. Adopting a price/time based priority, we can see that the orders are already arranged in terms of their price and time. The earlier sell order S1 takes priority over the similarly priced S2 and S3 and the higher priced S4.

|    |         | Buvs  |       | Sells |       |         |             |
|----|---------|-------|-------|-------|-------|---------|-------------|
| ld | Time    | Size  | Price | Price | Size  | Time    | $\text{1d}$ |
|    | 8:20:00 | 500   | 100   | 101   | 750   | 8:21:00 | S1          |
|    | 8:20:25 | 1,000 | 100   | 101   | 250   | 8:21:25 | S2          |
|    | 8:21:09 | 400   | 99    | 101   | 1,000 | 8:22:05 | S3          |
|    | 8:20:04 | 200   | 99    | 102   | 800   | 8:19:09 | S4          |

| (a) Before |
|------------|
|            |

|       | Price/time |     |   | <i>Price/pro-rata</i> |      |             |                |
|-------|------------|-----|---|-----------------------|------|-------------|----------------|
| Sells |            |     |   | Sells                 |      |             | $\text{Alloc}$ |
| Pricc | Size       | ld  |   | Price                 | Size | $\text{Id}$ |                |
| 101   | 750        | 51  |   | 101                   | 375  | S1          | 375            |
| 101   | 250        | \$2 | ٠ | 101                   | 125  | S2          | 125            |
| 101   | 1,000      | S3  | ٠ | 101                   | 500  | S3          | 500            |
| 102   | 800        | S4  |   | 102                   | 800  | S4          |                |
| After |            |     |   |                       |      |             |                |

# Figure 2-8 An example buy order matched with different priorities

Based on the size of the incoming market order, we can see that order S1 will be filled completely, as will the next order S2. Afterwards, order S3 now has both price and time priority for any new incoming buy orders.

In comparison, using a price/pro-rata based approach the allocation (labelled Alloc) is based on order size, since orders S1, S2 and S3 all have the same price priority. The proportions allocated are based on each order's size divided by the total amount available at that price. So order S3 will be allocated  $(1,000 / 2,000) = 50\%$  of the incoming order. Order S1 will get  $(750/2000) = 37.5\%$ , leaving the remaining 12.5% for order S2. The net result is that all three orders receive partial execution and remain on the order book ready for the next execution. The residual amounts are highlighted in Figure 2-8(b), confirming that this approach rewards size nearly as much as price.

Some continuous markets do not have an independent price discovery mechanism. Instead, the execution price is derived externally (usually from the primary market). Often this is the midpoint of the external best bid and offer prices. If market orders are supported, they execute at the mid-point whenever there is sufficient volume available on the other side of the order book. Limit orders will only match when the mid-point price is better than their limit. So the limit prices shown in Figure 2-9 actually refer to this mid-point.

|             |         | Buvs  |       | Sells |       |         |    |
|-------------|---------|-------|-------|-------|-------|---------|----|
| Id          | Time    | Size  | Price | Price | Size  | Time    | Id |
| $\text{B}1$ | 8:25:00 | 1,000 |       | 101   | 1,000 | 8:25:00 | S1 |
| B2          | 8:20:25 | 5,000 | 99    | 102   | 3,000 | 8:20:25 | S2 |
| B3          | 8:24:09 | 2,500 | 98    | 102   | 1,500 | 8:24:09 | S3 |
|             |         |       |       |       |       |         |    |

(a) before, external mid-point is  $100$ 

|              |         | Buys  |       | Sells |       |         |    |
|--------------|---------|-------|-------|-------|-------|---------|----|
| $\text{1d}$  | Time    | Size  | Price | Price | Size  | Time    | Id |
| $\mathbf{B}$ | 8:25:00 | 1.000 | 101   | 101   | 1,000 | 8:25:00 | SI |
| B2           | 8:20:25 | 5,000 | 99    | 102   | 3,000 | 8:20:25 | S2 |
| B3           | 8:24:09 | 2,500 | 98    | 102   | 1.500 | 8:24:09 | S3 |
|              |         |       |       |       |       |         |    |

(b) after mid-point becomes 101

#### Figure 2-9 An example mid-point match

On a normal continuous auction, the market order B1 would simply have crossed with order S1. But it is unable to do so because the external best bid and offer is 99-101, which is below the mid-point limit of 101 for order S1. As soon as the external mid-point shifts to 101, B1 can cross with order S1 since the mid-point is now sufficient. Note that both orders achieve the mid-point price, so unlike a normal market order B1 has not had to pay half the spread; though, it has sacrificed immediacy for this price improvement. This mechanism is generally used to support continuous crossing for block-size orders, hence the order book shown in Figure 2-9 would be completely opaque.

Clearly, a wide variety of continuous trade matching mechanisms are in use. In Chapter 8, we will review some of these in more detail.

## **Call auction**

A call auction may occur as little as once a day or as frequently as every 10 to 15 minutes throughout the trading day. Essentially, the process is similar to Figure 2-7 in that orders are queued up and applied to the auction order book. Still, trade matching is not instantaneous; it is carried out at a set auction time. The goal is to ensure that the maximum possible volume of orders is crossed at the auction price. Hence, orders accumulate before the auction takes place, allowing longer for price formation. This can be particularly useful when there is more uncertainty about what the price should actually be. In fact, many markets that use continuous auctions often choose to open and close the market with a separate call auction in an effort to reduce price volatility.

Before the crossing begins, the venue may also publish information about the overall imbalance between the buy and sell orders. They may even offer an indicative auction price to help traders to decide on pricing for their auction orders.

The auction crossing begins by checking that the order book is crossed; in other words, either the book contains market orders (MO) or there are buy orders with limit prices higher than some of the sell orders. It will then try to determine the best price for the auction. For the example order book shown in Figure  $2{\text -}10(a)$ , the best crossing price is 104.

|         | Buys  |       | Sells |       |         |
|---------|-------|-------|-------|-------|---------|
| Time    | Size  | Price | Price | Size  | Time    |
| 7:25:00 | 7,000 | MO    | MO    | 2,000 | 7:25:00 |
| 7:20:25 | 3.000 | 105   | 101   | 3,000 | 7:25:00 |
| 7:24:09 | 1,000 | 104   | 102   | 5,000 | 7:20:25 |
| 7:20:25 | 2,000 | 102   | 104   | 1,000 | 7:20:25 |
| 7:21:00 | 1,000 | 101   | 105   | 5,000 | 7:24:09 |

(a) order book crossing

| Buys    |       | Sells |       |       |         |
|---------|-------|-------|-------|-------|---------|
| Time    | Size  | Pricc | Price | Size  | Time    |
| 7:20:25 | 2,000 | 102   | 105   | 5,000 | 7:24:09 |
| 7:21:00 | 000,  | 101   |       |       |         |

(b) once crossing completed

## Figure 2-10 An example call auction crossing

Note that this auction price is generally determined independently, although for some crossing systems it may actually be derived from another market. Alternatively, if a single best price cannot be found then the price will be based on a reference price; generally, this is the last traded price (so last night's close for an opening auction or the last trade for a closing auction). We shall cover the specific criteria for determining the auction price in more detail in Chapter 8.

Once an auetion price is determined, the order book is then processed to match any orders that will execute within this price limit. These rows are shaded in the example order book shown in Figure 2-10(a). Note that many venues use time as a secondary priority, this rewards the early entry of auction orders.

Having completed the auction, the order book is then updated for the matched orders and trade notifications are sent out. Note that if this was the opening auction for a continuous double auction market, then Figure 2-10(b) shows the order book as it will be when the market officially opens for continuous trading. Alternatively, if this was for the close or an intraday/batch call auction then the orders will either be cancelled or left for the next auction crossing (although this depends on the market).

## Reporting, clearing and settlement

The final stages of the trading mechanism are reporting, clearing and settlement. Once a trade has been executed, detailed confirmations of the deal must be reported to the associated counterparties, the market authorities may also need to be informed.

The next stage of the process is clearing, which is basically a preparatory step before actual settlement. Clearing involves validating the trade and settlement details, as well as ensuring that the buyer and seller have the required assets/funds to be able to proceed. Often, a specific clearing agent will be mandated for trades at regulated venues such as exchanges.

The settlement process represents the actual exchange of assets and funds. The details for the buyer and seller are matched; a payment is made from the buyer's account and the asset's ownership is reassigned. Nowadays, most financial assets are dematerialised, so this literally means updating a book entry to reflect the change in ownership. However, for some assets, such as commodities, it can still involve a physical delivery. Generally, this process is handled by security depositories or dedicated custodians, financial institutions that specialise in the safekeeping of assets. Custodians also manage any associated interest or dividend payments, and even handle corporate actions for the holdings. Many security depositories and custodians have now become international, catering for a wide range of markets and allowing cross border trading.

The clearing and settlement process has become increasingly automated to keep up with electronic trading. Straight-through-processing (STP) offers the prospect of a fully electronic trading, clearing and settlement pathway. Gradually, more and more markets are migrating to support electronic clearing and settlement. Settlement dates used to commonly be five working days after the actual execution, denoted as  $T+5$ . This is gradually shifting to  $T+1$ , and ultimately towards  $T+0$ .

Increasingly, execution venues are adopting a central counterparty (CCP) approach for their clearing and settlement. This effectively splits each deal into two parts; each half is then transacted versus the CCP. So the buyer actually pays the CCP in return for the asset, whilst the seller must deliver the asset to the CCP in return for payment. This helps reduce counterparty risk as well, since the central counterparty now bears the risk of default. The CCP mechanism also allows for fully anonymous trading, since each party will only need to deal with the CCP. The buyer and seller just need to provide sufficient collateral to cover their trades. This also means clearing can be netted across all a participant's trades for an asset, resulting in a single net trade versus the CCP. Clearly, such netting means much less transfers and settlements and so can lead to substantial cost savings. It can also help reduce the required margin (or collateral) commitments needed to cover credit risk. Many central counterparties support margining across different assets, so the margin for a futures position may be reduced by a corresponding holding in the underlying asset. This can help reduce the costs of funding/position management.

For more information on the clearing and settlement processes, the review by Marco Pagano and Jorge Padilla (2005) is a good starting point.

#### $2.5$ Transaction cost measurement and analysis

Transaction costs are the last key area for market microstructure research. They are unavoidable, and are incurred each time an asset is bought or sold. Costs can have a considerable effect on investment returns and so affect market efficiency. Increased costs mean that investors must seek higher returns, and so they reduce the number of potential trading opportunities. In turn, this means that investors may hold positions for longer periods, helping to reduce trading volumes and so decreasing overall market liquidity. Electronic trading has helped increase market access to a wider range of participants. In so doing, it has improved market efficiency and led to a reduction in overall transaction costs.

By carefully measuring and analysing transaction costs, we can try to minimise them. Hence understanding how and why they occur has become a key factor in achieving significant investment returns. Clearly, the first stage is accurately measuring the overall costs. Post-trade analysis has also proved important for performance analysis, enabling comparison of both trading styles and individual brokers/traders.

Further research has broken down transaction costs into separate components, such as market impact and timing risk. A combination of theoretical models and empirical analysis has allowed accurate cost models to be created. These can be used for pre-trade analysis to estimate the potential cost, and so may be used to choose the most appropriate trading strategy.

## Cost measurement

Cost measurement has focussed predominantly on spreads and henchmark prices. Both measures are easy to calculate and can give meaningful insights.

#### Using spreads

Spreads have long been a popular measure for cost measurement, in part due to the simplicity of determining them. They have also been used as a measure of overall market efficiency. Many academic studies have compared the average spreads for various market types. Table 2-3 shows the key spreads which are commonly used:

| Type                                                  | Measures       | From:                                                                                 |  |  |  |
|-------------------------------------------------------|----------------|---------------------------------------------------------------------------------------|--|--|--|
| Quoted<br>spread                                      | Market quality | Difference between best bid and offer price                                           |  |  |  |
| Effective<br>spread                                   | Execution cost | Signed difference between trade price and<br>quote midpoint when order was received   |  |  |  |
| Realized<br>Trading intermediary<br>spread<br>profits |                | Signed difference between trade price and<br>quote midpoint 5 minutes after the trade |  |  |  |

#### Table 2-3 The different types of spreads

As we have already seen, the bid offer spread can be attributed to a range of factors. Market makers use it to compensate themselves for the fixed costs incurred by trading, as well as to protect themselves from the risk of adverse selection. Similarly, spreads arise in purely order-driven markets as a function of the available supply and demand.

The effective spread represents the difference between the achieved trade price and the mid point between the bid and offer when the order was first received. It measures the actual cost our order incurred by executing in the market.

The realized spread compares the difference between the trade price and the mid price five minutes later. It is sometimes used as a measure of the potential profits that may be made by trading intermediaries, i.c. market makers, dealers, brokers.

Note that to compare effective and realized spreads with the quoted spread the cost differences need to be doubled, since they are both calculated using the mid price.

#### Using benchmarks

Price benchmarks are extensively used to monitor the performance of trades. They have also become a key factor in measuring transaction costs. Performance is often measured in basis points (bps), which are hundredths of a percent.

A wide variety of benchmarks may be used, ranging from opening and closing prices to averages such as the Volume Weighted Average Price (VWAP). One way of choosing between them is based on when they may be determined. Post-trade henchmarks will not be available until after the close of trading. Likewise, intraday benchmarks that span the whole trading day will not have a definitive value until the close. Nevertheless, interim values may be calculated throughout the day. Pre-trade benchmarks are available before the main trading session starts. Table 2-4 summarises the different benchmarks based on this categorisation:

| Type        | Name                                 |
|-------------|--------------------------------------|
| Post-Trade  | Close                                |
|             | Future Close                         |
| Intraday    | Open-High-Low-Close (OHLC)           |
|             | Time Weighted Average Price (TWAP)   |
|             | Volume Weighted Average Price (VWAP) |
| $Pre-Trade$ | Previous Close                       |
|             | Opening Price                        |
|             | <b>Decision Price</b>                |
|             | Arrival Price                        |

**Table 2-4 Classifying benchmark types** 

Post-trade benchmarks are generally closing prices. Most commonly, the current day's closing price (or close) is taken, although other future prices may also be used. Closing prices have long been a popular benchmark, in particular because they are often used as a milestone for marking to market and for profit and loss (P&L) calculations.

Intraday benchmarks use an average price to more accurately reflect market conditions. This is because markets tend to be more active at the close, so the closing price will not necessarily reflect the actual conditions throughout the day. One of the first popular intraday benchmarks was the Open High Low Close (OHLC) average. More accurate averages have also been adopted, as tick-by-tick price and volume market data has become more widely available. For instance, the Time Weighted Average Price (TWAP) applies an equal weighting to all the day's trade prices. Alternatively, the Volume Weighted Average Price (VWAP) weights each trade price by its corresponding size, so the average will most reflect the largest trades. This ability to accurately reflect intraday market conditions has made VWAP an extremely popular benchmark.

Pre-trade benchmarks are also useful since they are both easily determined and readily available. As the use of transaction cost analysis has become more widespread implementation shortfall is increasingly used as a measure of performance. Effectively, this represents the difference between the average price achieved in execution, and the market price when the investor's decision was first made (the decision price). Pre-trade benchmarks correspond well to the decision price, hence their popularity.

#### Analysing the components of transaction costs

Transaction costs incorporate much more than just broker commissions and the bid offer spread. The market trend to un-bundle research fees has helped make it much easier to quantify the actual transaction costs.

The different cost components are commonly termed as either explicit or implicit. Likewise, they represent fixed overheads or a variable amount that will differ based on the asset, the order, market conditions and the trading strategy.

The explicit costs are clearly identifiable and easily measured. They are commissions, fees and taxes. Often, these will be quoted in advance of trading as percentages of the traded value or as basis points. They may be reduced to a certain extent, based on negotiation between the investor and the brokers. The rates offered will usually depend on the client's trading volumes and the level of service they require.

The implicit costs are generally associated with the actual trading process, and are harder to quantify, since they are less directly observable. They tend to be more variable, but often have a greater impact on the overall performance. Indeed, they are often represented as the hidden part of an iceberg (9/10<sup>ths</sup> below the surface). Wayne Wagner and Mark Edwards (1993) proposed separating the implicit trading costs into the following components:

- Timing cost (due to price trends and timing risk)
- Delay cost  $\bullet$
- Impact  $\bullet$
- Opportunity cost e

All of these are price related and correspond to decisions that the investor and trader must make, based on knowledge of the order and current market conditions. Figure 2-11 provides a view of these costs based on the relative visibility of each component. Note that the size of each cost component will vary based on the asset, order size and trading style so Figure 2-11 is not drawn to any particular scale.

![](_page_23_Figure_8.jpeg)

Figure 2-11 Transaction cost components

Starting from the most visible components, we have:

Commissions: This is most obvious cost component, representing the broker's compensation for providing the trading service. In particular, this should cover both their capital and labour costs.

*Fees:* Charges may be levied by floor brokers and exchanges as well as any costs associated with clearing and settlement. Note that fees are often rolled into the overall commission charge.

*Taxes:* Generally, taxes are an investment cost, applied to any realized profits from capital gains. However, some markets also apply additional duties for trading. For example, the U.K. stock market applies a  $0.5\%$  stamp duty on share purchases.

*Spread cost:* The bid offer spread compensates traders for providing liquidity. The spread

usually reflects the liquidity of an asset. There are noticeable differences in average spreads across the capital markets. For instance, decimalisation in the U.S. equity market has resulted in considerably lower average spreads than in either Europe or Asia. Spread may be classed as a visible cost, although it is not always as easily measurable as fees or commissions. For single executions, it is obviously straightforward to measure, but for trades that are split up and worked over the day we must track the spread for each child order.

Delay cost: This reflects any price change from when the initial decision to invest is made and when an order is actually sent for execution. This may be because the decision was made before the market open; alternatively, time may be spent identifying the best way to trade the order. Delay cost can be a substantial proportion of overall costs, particularly for assets which are volatile or whose price is trending unfavourably. Therefore, to monitor this cost it is important for investors to record the market mid-price when the initial decision is made and when an order is dispatched.

*Market impact:* This represents how much effect the order has on the asset's price. Larger orders result in a larger impact compared to smaller ones; however, the effect decreases significantly with asset liquidity. Market impact consists of both a temporary effect and a permanent one. The temporary market impact reflects the overall cost incurred by demanding immediacy (when combined with the spread cost). Whereas the permanent impact signifies the long-term information cost of the trade, based on how it affects the asset's overall order buy/sell imbalance.

*Price trend:* Asset prices may sometimes exhibit broadly consistent trends. An upward trend implies that costs will increase when buying an asset, whilst savings will be accrued if selling, whereas the opposite is true for a downward price trend.

Timing risk: This cost reflects uncertainty, in particular for volatility in both the asset's price and its liquidity. The more volatile an asset then the more likely its price will move away and so increase the transaction costs. Similarly, if liquidity suddenly falls then market impact costs will rise. Timing risk may be considerable, especially for volatile assets and for orders that have a long trading horizon.

Opportunity cost: Orders are not always fully completed, maybe due to passive trading or unfavourable market conditions. This cost represents the missed opportunity, since the next day prices may move even further away.

Clearly, there is a lot more to transaction costs than just the explicit costs. In Chapter 6, we will cover this topic in much more detail using worked examples to provide in-depth post-trade analysis of sample orders. We will also cover the increasingly important field of pre-trade transaction cost analysis, which is used to compare potential trading strategies.

#### Summarv $2.6$

Market microstructure concentrates on the actual trading process, analysing how specific designs or mechanisms affect both observed prices and traded volumes as well as helping to explain the associated costs.

- Liquidity represents the east for converting an asset into eash or vice versa.
- Markets may be classified in terms of two main mechanisms:
  - Purely quote-driven markets, where traders must transact with a dealer (or market maker), who quotes prices at which they will buy and sell a given quantity.
  - Purely order-driven markets, where traders participate equally, by placing orders. These are then matched on the order book using a consistent set of rules.
  - Increasingly markets are actually hybrids of these two approaches.
- Trading may be broken down into three main stages:  $\blacksquare$ 
  - Price formation
  - Price discovery / trade execution
  - Reporting, elearing & settlement
- $\blacksquare$ There are three key methods for trade execution:
  - Bilateral trading, which is a one-to-one negotiation often with a market maker.
  - Continuous auctions, where matching rules are applied each time an order is added, updated or cancelled to determine whether there is a resultant execution.
  - Call auctions, where orders are allowed to accumulate for a set time before the matching rules are applied, and so helping to reduce price volatility.
- $\mathbf{m}$ Transaction costs are unavoidable, they are incurred each time an asset is bought or sold. Cost measurement has focussed predominantly on spreads and benchmark prices. Costs may be broken down into two main classes:
  - Explicit costs, such as commissions, fees and taxes, are clearly identifiable and easily measured.
  - Implicit costs, such as market impact and timing risk, are generally associated with the actual trading process and are harder to identify and measure.
### **CHAPTER 3**

# Market Microstructure, Orders, and Limit Order Books

The study of market microstructure originated over four decades ago, and the core principles remain true today: most market participants rely on limit orders and market orders. These core order types remain most used despite an explosion of various derivative order types. Despite the continuity of these key principles still, much has changed. In the 1980s At one time, the peculiarities differentiating tick data dynamics from daily and monthly data were observed, but there was no way to incorporate the differences into a trading strategy. Today, that tick data can be captured easily and trades initiated quickly, it is possible to build trading strategies taking into account market microstructures. This chapter delves into the modern microstructure of markets, describing orders, matching processes, and rebate structures, among other issues defining today's markets.

### Types of Markets

Financial markets are venues that allow investors and other market participants to buy and sell securities with a peace of mind that all transactions will be properly accounted and settled. In this respect, financial markets are not that different from markets for other nonfinancial products, such as a neighborhood grocer. When a customer enters a grocery store, he expects immediate execution of his transaction, an exchange of his money for merchandise—food. The grocer's cash register takes on the settlement function: the receipt itemizes the produce the customer bought and the total amount of money the grocer collected, nowadays most often from the customer's account rather than in cash form.

Furthermore, the grocery customer expects that the food he acquires is in good condition and that the transaction is permanent: that the grocer has full

rights to sell the customer the product. Most centralized financial markets incorporate similar quality control for financial products: the products offered for purchase and sale on the floors of each market tend to be standardized, and their quality can be ensured via a thorough prelaunch due-diligence process as well as via the real-time data distribution to all market participants. For example, futures contracts traded on exchanges have a specific well-defined structure. Initial public offerings for stocks tend to be well scrutinized. Yet, just like grocers do not evaluate suitability of particular foods to each person, financial markets are unaware of a client's risk profile or accreditation, leaving the risk of investing decisions to the traders themselves.

Since the beginning of trading history, most financial and nonfinancial markets have been organized by product type. In nonfinancial settings, stores carrying lumber differ from stores selling clothes. Food markets used to be highly fragmented by type as well: fishmongers, bakers, butchers, and ice-cream makers all used to have their own shops, if not districts. Similarly, financial markets have been historically organized by the type of the traded instrument, each trading only equities, futures, options, or other securities. Recently, however, nonfinancial markets have been gearing toward megastores to increase their efficiency and take advantage of common distribution and procurement frameworks and skills. Similarly, many trading venues are now venturing in the cross-asset space, with the traditional foreign exchange player iCap launching a fixed-income trading offering, and equity exchange Best Alternative Trading Systems (BATS) considering entering the foreign exchange trading space.

The history of the financial exchanges is not always linear. The New York Stock Exchange (NYSE), for example, was first formed as a for-profit entity at the end of the eighteenth century, when two dozen stockbrokers signed an agreement to stop undercutting each other's commissions and instead retain at least 0.25 percent of each trade. In subsequent years, as the U.S. economy grew, more public listings became available, and the interest in investing grew from the U.S. public, stockbroking became increasingly lucrative and seats on the NYSE rose in value.

During major recessions, however, lavish lifestyles of stockbrokers drew the scrutiny of money-losing investors and regulators. In 1934, in the midst

of the Great Depression, the NYSE was required to register and accept oversight from the then newly formed U.S. Securities and Exchange Commission (SEC). In 1971, during the post–Vietnam War recession, the NYSE was converted into a not-for-profit entity in a bid to cap excessive compensation of brokers and transfer some of their intake to the investors. The nonprofit mandate failed to live up to its expectation, with exchangeregistered brokers creating a secondary market for their seats on the exchange that by the 1990s had reached multiple-million-dollar price tags.

The past two decades have witnessed increasing competition in the exchange space, and these competitive market forces appear to have succeeded in helping investors retain a larger share their earnings away from brokers. New exchanges, such as Nasdaq, deployed technology in lieu of bonus-collecting human traders, transferring some of the resulting savings into the pockets of investors and producing other benefits in the process. Technology has lowered error rates, increased execution times, and, perhaps most importantly, increased transparency of process to investors. Other early exchanges, such as the Chicago Mercantile Exchange, followed trajectories similar to that of NYSE, and today face competition from relatively new exchange entrants, such as the Intercontinental Commodity Exchange (ICE).

Today's equity markets comprise over a dozen various exchange venues, run by now-industry stalwarts such as the NYSE and Nasdaq, and relatively recent arrivals, such as BATS, DirectEdge, and others. Since all equity exchanges are subject to U.S. SEC oversight and trade standardized products, exchanges presently compete to differentiate their offerings mainly on liquidity and costs. In a bid to attract liquidity (more on this later in this chapter), most exchanges have done away with membership fees and now offer free registration. In addition, equity exchanges are differentiating themselves on price structures, not only rewarding large traders but also segmenting traders based on whether they place market orders or limit orders.

In addition to the regular exchanges, a new breed of matching venues has emerged, known as *dark pools.* Unlike an exchange, where the entire limit order book is available for observation, dark pools do not disclose their limit order books, instead keeping them "in the dark." Trading in a dark

limit order book has appealed to large investors who are concerned about the information they may reveal by placing their orders in a traditional exchange, a *lit* market. Liquidnet is an example of an equities dark pool.

### Limit Order Books

The cumulative trade size of all limit orders available to meet incoming market orders at any given time on a specific trading venue is known as *liquidity.* The larger the number of limit order traders available on the exchange, and the larger the size of each trader's limit orders, the more liquid the given trading venue. Liquidity is also necessarily finite in today's markets: the number of limit orders is measurable, and each limit order has a finite size. Liquidity was first defined by Demsetz (1968).

To account for limit orders, the majority of contemporary exchanges are organized as so-called centralized limit order books (CLOBs), also referred to as a double-sided auction. The CLOBs were pioneered in the United States in the early 1970s and adopted in Europe in the 1980s. In a CLOB model, all incoming limit orders are recorded in a "book": a table with columns corresponding to sequential price increments, and rows recording sizes of limit orders posted at each price increment. Figure 3.1 illustrates the idea. The limit order book information can be distributed to all other market participants as Level II data, discussed in detail in Chapter 4.

**Figure 3.1** Sample Snapshot of a Limit Order Book. All limit buy orders are on the left-hand side of the book; all limit sell orders are on the righthand side of the book.

![](_page_4_Figure_1.jpeg)

In theory, limit order books are often assumed to be symmetric about the market price, with the distribution of limit buy orders mirroring that of limit sell orders. Furthermore, in many risk management applications, order books are also assumed to follow normal bell-curve distributions. Neither of the assumptions tends to hold: order books are seldom normal and are often asymmetric.

As Figure 3.2 shows, when a new limit order arrives, it is placed into a *limit order queue* corresponding to its price. Since all prices in today's markets are subject to a minimum increment, or *tick*, price-based bins are clearly delineated. The limit buy orders at the highest price form the best bid, with the price of these orders reflected in the best bid price, and the aggregate size reported as the best bid size. Similarly, the limit sell orders posted at the lowest price form the best ask, with respective price and size information. Best ask is sometimes referred to as *best offer.* At any given moment of time, there exists a finite aggregate size of all limit orders posted at each price.

![](_page_5_Figure_0.jpeg)

#### **Figure 3.2** Sample Dynamics in a Limit Order Book

When a market buy order arrives, it is matched with the limit sell orders, beginning with those placed at the best ask price. If the size of the incoming market buy order is greater than the size of the best ask queue, the market order "sweeps" through other offer queues in the direction of increasing price, "eating up" liquidity available at those price ticks. Sweeping leaves a significant gap in limit orders on the ask side, instantaneously increasing the bid-ask spread, and potentially inducing slippage in subsequent market buy orders. The order-matching process is similar for market sell orders that end up matched with the available limit buy orders aggregated on the bid size of the book. Limit buy orders with the prices equal or higher than the

prevailing best bid are executed like market buy orders. Similarly, lowpriced limit sell order are usually treated as market sell orders.

If the size of the incoming buy order is smaller than the size of the best ask, and the aggregate best ask queue is composed of several limit sell orders placed at the best ask price, the decision of which of the limit sell orders is matched against the market buy order may differ from one exchange to another. While most exchanges at present practice price-time priority, also known as the first-in-first-out (FIFO) execution schedule for limit orders, several other exchanges now match a fixed proportion of each limit order at a given price in a process known as pro-rata matching.

<span id="page-6-1"></span>In time-price priority, or FIFO, execution, the limit order that arrived first is also the first of that price bin to be matched with the incoming market order. [Figure 3.3](#page-6-0) illustrates the FIFO matching process. FIFO, known as the continuous auction, has been shown to enhance transparency of trading via the following measures (see Pagano and Roell, 1996; Jain, 2005; and Harris, 2003):

<span id="page-6-0"></span>![](_page_6_Figure_3.jpeg)

- Reducing information asymmetry—all traders have access to the limit order book information.
- Enhancing liquidity—a CLOB structure incentivizes traders to add limit orders, thereby increasing market liquidity.
- CLOB's organization supports efficient price determination by providing a fast and objective order-matching mechanism.
- Uniform rules for all market participants ensure operational fairness and equal access.

While most execution venues are based on FIFO, some exchanges, like Chicago Mercantile Exchange (CME), Chicago Board Options Exchange (CBOE), Philadelphia Stock Exchange (PHLX), and Intercontinental Commodity Exchange (ICE) have switched to pro-rata execution schedules. CME's pro-rata schedule matches an incoming market buy order with a fixed proportion of each limit order posted at the best ask. Similarly, an incoming sell order is matched with equal fractions of all of the limit orders posted at the best bid. The larger the limit order at the best bid and the best ask, therefore, the larger the fill of that order. [Figure 3.4](#page-7-0) shows the pro-rata process.

<span id="page-7-1"></span><span id="page-7-0"></span>![](_page_7_Figure_5.jpeg)

The main advantage of the pro-rata matching from the exchange point of view is the built-in incentives for traders to place large limit orders, and, therefore, to bring liquidity to the exchange. The pro-rata matching encourages traders to post large limit orders without special compensation like rebates discussed below, thereby increasing exchange profitability. In addition, pro-rata matching eliminates incentives to place and then cancel limit orders with the intent to secure time priority of execution, reducing message traffic to and from the exchange.

In a nutshell, the pro-rata incentive works as follows: a trader desiring to execute a limit order knows that only a fraction of his order will be filled under the pro-rata schedule. The exact size of the filled portion of the order will depend on the cumulative size of limit orders placed at the same price by other limit order traders. The higher the aggregate size of limit orders in a specific price bin, the lower the percentage of all orders that will be filled in response to an incoming market order of the opposite sign. To increase his chances of filling the entire order, therefore, the trader is likely to place a limit order with a larger size than his intended order, with the explicit hope that the fraction of the order that will get filled is of the exact size as his intended order.

### Aggressive versus Passive Execution

Orders can be described as passive or aggressive. Aggressive orders do not mean malicious orders, and passive orders do not indicate orders that are destined to be taken advantage of. Instead, the aggressiveness or passivity of orders refers to the proximity of the order price to the prevailing market price. [Figure 3.5](#page-8-0) illustrates the concept.

<span id="page-8-1"></span><span id="page-8-0"></span>![](_page_8_Figure_4.jpeg)

A limit order far away from the market price (a low-priced limit buy order, or a high-priced limit sell order) is considered passive. The closer the limit order is to the market price, the more aggressive is the order. A market order is the most aggressive order, "crossing the spread" to be matched with the best-priced limit order on the opposite side of the limit order book. Limit orders crossing the spread are treated like market orders in the execution queue, and are also considered aggressive.

While market orders enjoy immediate and nearly guaranteed fills, market orders cross and pay the spread, incur transaction fees of the exchange and broker-dealers, and face price uncertainty. In today's markets, price uncertainty can be the costliest component associated with the market order execution. From the time the market order is placed to the time the execution is recorded, the market price may "slip," resulting in worse execution than the prevailing price at the time the market order was placed. The slippage may be due to several factors:

- Several market orders may arrive at the exchange and be executed between the time a given market order is placed and the time it is executed. Each of the arriving market orders may deplete the matching liquidity in the order book, adversely moving the market price. Such a situation is particularly common at times of news releases, when many traders and their algorithms simultaneously process information and place orders in the same direction.
- A market order that is large relative to the available depth of the order book may sweep through the book, executing fractional pieces of the order against limit orders at different price levels.
- Additional market conditions, such as market disruptions, may also result in significant slippage.

By contrast, the price of a limit order is fixed when the order is placed. A limit order is added to the limit order book, where it "sits" until the prevailing market price reaches it and a market order is executed against it. Limit orders also generally avoid "crossing the spread," a cost of paying the market spread incurred by market orders. Highly aggressive limit orders executed as market orders cross the spread, but obtain as good or better execution price than their specified limit price. Limit orders are also subject

to positive or negative transaction costs, which vary from one trading venue to another.

For all their price advantages, limit orders are subject to an important risk —the risk of nonexecution. A limit order is executed only when it is matched with a market order of the opposite direction. A market price may quickly move away from a limit order, leaving it unexecuted. An unexecuted limit order may present a particular problem when placed to close a position, and misses the opportunity to eliminate market risk of the trade. And yet, unexecuted limit orders placed to open a position also incur a cost, that of the opportunity to engage in the trading strategy.

## Complex Orders

In response to competition from new entrants in the matching business, trading venues have diversified their order offerings. For example, in response to competition from dark pools, selected exchanges expanded the number of available orders, creating so-called *iceberg orders*. Iceberg orders allow limit-order traders to display only a portion of their order in the limit order book, and keep the rest of their liquidity in the dark. In FIFO limit order books, iceberg orders are executed on a time priority basis: when matched against a smaller order, the nonexecuted part of the iceberg is being placed back at the end of their limit-order book queue. Unlike the orders in a dark pool, the size information of an iceberg is revealed after the iceberg is matched in part or in full: the matched size is disseminated to other traders as a trade tick. As a rule, iceberg orders cost more than do limit and market orders.

Other specialized orders have sprung up as well, to generate additional revenues from higher transaction costs and to serve the following potential needs of customers:

*Limit risk*. Most trading venues and broker-dealers now offer a range of orders for containing market risk. The order examples include hard and trailing stop orders, where the position is liquidated when a price move exceeds the predetermined threshold in the adverse direction (see Chapter 14 for more information on stops).

- *Speed of execution.* Orders in this category try to enable the fastest execution possible and include, in addition to the vanilla market order, a market-on-close order that often guarantees to catch the closing price, a midpoint match order that bests the best bid limit order by attempting to negotiate crossing only half of the prevailing spread, and the sweepto-fill order simultaneously clears the order book of the size requested in the order. The sweep-to-fill order may be executed faster than the market order, since a large market order is often executed by sweeping the limit order book gradually over time.
- *Price improvement.* Such orders include a block order in options that improves the price by obtaining large-volume discounts on transaction costs.
- *Privacy.* Privacy-providing orders deliver dark liquidity, and include iceberg orders and hidden orders, among others. The hidden order, as its name suggests, is not displayed in the limit order books. The iceberg order displays a limited portion of the order in the limit order book, as discussed in the beginning of this section.
- *Time to market.* Orders in the time-to-market group include fill-or-kill orders for market orders desiring the most immediate liquidity. A fillor-kill order is canceled if the matching liquidity is not immediately available. Conversely, a good-till-canceled limit order falling in the same order category is kept in the limit order book until it is canceled or another maximum period of time set by the trading venue (e.g., a quarter).
- *Advanced trading.* These orders include additional quantitative triggers, such as implied volatility in options.
- *Algorithmic trading.* Orders in this category offer execution via orderslicing algorithms, such as percentage of volume (POV), described in detail in Chapter 17.

## Trading Hours

Traditionally, many trading venues operated from 9:30 a.m. to 4:00 p.m. Eastern time. In today's globalized markets, more effort is placed on expanding accessibility of trading. As a result, many exchanges today offer

premarket trading and afterhours trading, cumulatively known as *extendedhours trading.* Extended hours in equities, for example, allow market access from 4:00 a.m. to 8:00 p.m. Eastern time. The extended-hours volume is considerably thinner than that observed during the normal trading hours. Still, selected brokers use the after-hours trading to fill their customers' market-on-close orders.

# Modern Microstructure: Market Convergence and Divergence

The electronization of markets has left an indelible footprint on all modern markets, streamlining some aspects of trading and fragmenting others. Among the trends in market convergence are the following developments:

- Most markets today can be accessed via Financial Information eXchange (FIX) messaging protocol. The FIX protocol is an XML-like specification that allows market participants to send and receive quotes, orders, and order cancellation and execution acknowledgments, among other messages necessary for fast and efficient trading. The FIX protocol is administered by an independent not-for-profit body, further facilitating proliferation of the protocol.
- Most markets worldwide are now designed as limit order books (LOBs). The Singaporean Stock Exchange was one of the last entities to use a different market structure, but converted to LOB in the past decade.

Among the key trends in market divergence is the progressing fragmentation of markets among the asset classes:

- Equities are subject to the National Best Bid and Offer (NBBO) rule, whereas all equities are to be executed at the aggregated and disseminated NBBO or better price. If the exchange is unable to execute an incoming market order at the NBBO, the exchange is obligated to route the order to an exchange with NBBO quotes.
- Futures exchanges do not have centralized pricing, but are subject to unique margining and daily mark-to-market requirements.

- Foreign exchange markets do not have centralized quotes or exchanges at all. All trades are continued to be negotiated over the counter (OTC), even though many OTC platforms are now fully electronic. Yet selected large market participants may be granted access to an interdealer network, an exchange-like entity.
- Option markets are numerous, with little activity on average.
- Following the Dodd-Frank regulation, new asset classes such as fixed income and swaps will be coming online or expanding in electronic forms. Each of the asset classes has distinct peculiarities, resulting in further fragmentation of the overall securities frontier.

Fragmentation exists within each asset class as well. The following sections discuss peculiarities within selected asset classes.

### Fragmentation in Equities

U.S. equities can be traded in dark pools and on lit exchanges. Dark pools are exchange-like entities where the order book is "dark"—not displayed to any participant of that pool. According to Pragma Securities (2011), about 22 percent of the U.S. aggregate equity volume is presently traded in the dark pools. The singular advantage of dark pools lies in their ability to match large orders without revealing information associated with the order size, as the orders are not observable. The frequently cited disadvantages of dark pools include the lack of transparency and related issues. Unlike "lit" exchanges, dark pools do not offer differentiated pricing for limit and market orders—the dark pool limit order book is not disclosed to market participants.

The remaining 78 percent of the U.S. equity volume is executed on "lit" exchanges—venues where the order book is fully transparent and can be disseminated in full to interested market participants. But even within the lit markets category, the landscape is quite fragmented as the exchanges compete to set optimal fees.

In the lit exchanges, the U.S. equities are required to be executed at the NBBO or better quotes, compiled from the best bid and ask quotes available on all the member exchanges and disseminated by the Securities Information Processor (SIP). The aggregated best quotes are then

disseminated back to exchanges as NBBO references. The NBBO execution rule was put forth by the Securities and Exchange Commission (SEC) in 2005 under the Regulation NMS, with the explicit purpose of leveling the playing field: under the NBBO rule, every best limit order, whether placed by a large institution or an individual investor, has to be displayed to all market participants. (Prior to the NBBO rule, individual investors were at the mercy of broker-dealers, who often failed to route investors' limit orders to exchanges, even when said limit orders were at the top of the market better than the best quote available at the time.) Under the NBBO rule, exchanges that cannot execute at the NBBO due to the dearth of liquidity are required to route incoming market orders to other exchanges where the NBBO is available. As a result, traders placing market orders on lit exchanges are guaranteed that their orders are executed at the best possible prices available nationwide. Dark pools are exempt from the NBBO requirement.

Under the NBBO rule, exchanges can match trades only when they can execute at the NBBO, that is, when the NBBO-priced limit orders are recorded within their limit order books. Such NBBO limit orders can be achieved using two distinct approaches:

1. The exchange can compete to attract the top-of-the-book liquidity limit orders priced at NBBO or better.

2. The exchange can compete to attract market orders, while simultaneously serving as a proprietary market maker posting NBBO limit orders.

The two business models of exchanges readily translate into the new fee structures of exchanges. In addition to clearing fees, exchanges now offer divergent pricing for suppliers of liquidity and takers of liquidity. Depending on whether the exchange follows the business model 1 or 2, the exchange may pay liquidity providers for posting limit orders, or pay takers of liquidity for bringing in market orders. Such payments, amounting to negative transaction costs, are known as *rebates.*

The two different business models have driven the exchanges into two distinct camps, "normal" and "inverted" exchanges, based on their fee structure. The normal exchanges offer the following fees: normal exchanges charge traders for placing market orders, taking away liquidity, and offer

rebates for placing limit orders, bringing in liquidity. The NYSE, for example, charges \$0.21 for a 100-share market order, and pays anywhere from \$0.13 to \$0.20 for a 100-share limit order. The exact value of the NYSE rebate is determined by the aggregate monthly volume of the trader —the higher the volume, the higher the rebate. The NYSE fee structure displayed online on May 14, 2012, is shown in [Figure 3.6](#page-15-0).

<span id="page-15-0"></span>**[Figure 3.6](#page-15-1)** Fee Structure of Orders Placed and Routed to and from NYSE *Source:* NYSE web site

|                   |                                                                             | TAPE A<br>(NYSE-LISTED)              |                     |                                 |                               |
|-------------------|-----------------------------------------------------------------------------|--------------------------------------|---------------------|---------------------------------|-------------------------------|
| Tier              | Tier Requirement(s)                                                         | Rebate<br>for<br>Adding <sup>1</sup> | Fee for<br>Removing | Routing to<br>NYSE <sup>2</sup> | Routing<br>to Other<br>Venues |
| Tier 1            | NYSE Arca Daily<br>Adding as of % of<br>US CADV in excess<br>of 0.70%       | \$(0.30)                             | \$0.30              | \$0.21/\$0.23                   | \$0.30                        |
| Tier 2            | NYSE Arca Daily<br>Adding as of % of<br>US CADV in excess<br>of 0.30%       | \$ (0.29)                            | \$0.30              | \$0.21/\$0.23                   | \$0.30                        |
| Tier 3            | NYSE Arca Daily<br>Adding as of % of<br>US CADV in excess<br>of 0.20%       | \$ (0.25)                            | \$0.30              | \$0.21/\$0.23                   | \$0.30                        |
| Step-Up<br>Tier 1 | NYSE Arca Daily<br>Adding as % of US<br>CADV in excess of<br>0.15% over the | \$ (0.295)                           | \$0.30              | \$0.21/\$0.23                   | \$0.30                        |

<span id="page-15-1"></span>

In contrast, the so-called "inverted" exchanges pay traders small rebates to remove liquidity (place market orders), and charge fees to place limit orders. Boston Exchange (Nasdaq OMX BX) is an example of an inverted exchange. There, traders with market orders for fewer than 3.5 million

shares per day are paid \$0.0005 per share, while traders placing market orders for 3.5 million or more shares per day are paid \$0.0014 per share. Traders adding displayed limit orders under 25,000 per day are charged \$0.0015 to \$0.0018 per share. Yet, large limit order traders—traders placing limit orders for 25,000 shares per day or more—are paid rebates at the rate of \$0.0014 per share. The snapshot of distribution of trading costs on the BX as of October 10, 2012, is shown in [Figure 3.7.](#page-16-0)

<span id="page-16-0"></span>**[Figure 3.7](#page-16-1)** Fees on Nasdaq OMX BX, an Inverted Exchange

*Source:* Nasdaq web site

<span id="page-16-1"></span>

|                                                                                                      | Www.nasdagtrader.com/Trader.aspx?id=bx_pricing.                                                                                                       | ☆ ≡                                                    |  |  |  |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|--|--|--|
|                                                                                                      | Suggested Sites 🗔 Web Slice Gallery [9] Gmail - (no subject)  🗀 Historical data 🏿 P Pandora Radio - List 🗋 vedicssols 🥃 Park & Bond                   | <sup>39</sup> Other bookmarks                          |  |  |  |
| 53<br>Add/Romove Rates<br>$\mathbf{G}$<br><b>Participation Fees</b><br>8<br><b>Connectivity Fees</b> | NASDAQ OMX BX Price List - Trading & Connectivity<br>PSX Pricing BX Options Pricing NOM Pricing PHLX Pricing NFX Pricing<br>NASDAQ Pricing IX Pricing |                                                        |  |  |  |
| <b>Risk Management</b>                                                                               | All U.S. Equities                                                                                                                                     |                                                        |  |  |  |
| $\mathbf{G}$<br>Secure Data Fees                                                                     | (Per Share Executed)                                                                                                                                  |                                                        |  |  |  |
| NASDAQ Testing Facility                                                                              | Rebate to Remove Liquidity                                                                                                                            |                                                        |  |  |  |
| <b>View or Print</b>                                                                                 | MPIDs removing greater than 3.5 million shares per day or adding greater than                                                                         |                                                        |  |  |  |
| Additional Resources                                                                                 | 25,000 shares per day<br>All other MPIDs                                                                                                              | S0 0005                                                |  |  |  |
|                                                                                                      | Fee to Remove Liquidity                                                                                                                               |                                                        |  |  |  |
|                                                                                                      | Liquidity-removing orders that execute against a midpoint                                                                                             | Free                                                   |  |  |  |
|                                                                                                      | Fee to Add Displayed Liquidity per MPID                                                                                                               |                                                        |  |  |  |
|                                                                                                      | MPIDs meeting the QLP program criteria                                                                                                                | S0 0015                                                |  |  |  |
|                                                                                                      | All other MPIDs                                                                                                                                       | \$0.0018                                               |  |  |  |
|                                                                                                      | Fee to Add Non-Displayed Liquidity per MPID                                                                                                           |                                                        |  |  |  |
|                                                                                                      | All MPIDs                                                                                                                                             | \$0.0018                                               |  |  |  |
|                                                                                                      | Shares Executed Below \$1.00                                                                                                                          | (Per Share Executed)                                   |  |  |  |
|                                                                                                      | Rebate to Add Liquidity                                                                                                                               | \$0.00                                                 |  |  |  |
|                                                                                                      | Fee to Remove Liquidity                                                                                                                               | 0.10% (i.e. 10 basis points)<br>of total dollar volume |  |  |  |

As a result of the regulatory framework and pricing divergence among equity exchanges in the United States, various exchanges show different rates of availability of NBBO on their order books as well as different market shares. As the intuition would suggest, the exchanges able to provide the highest occurrence of NBBO quotes are the ones able to secure the highest market share. [Figure 3.8](#page-16-2) displays the relationship between the NBBO availability rates and the market share rates. As shown in [Figure 3.8](#page-16-2), Nasdaq and NYSE on average have the highest availability of NBBO and obtain the highest share of trades.

<span id="page-16-3"></span><span id="page-16-2"></span>**[Figure 3.8](#page-16-3)** Availability of NBBO versus Share Volume

*Source:* Pragma Securities (2011)

![](_page_17_Figure_0.jpeg)

Figure 3.9 illustrates what happens when the NBBO is available on all or only some exchanges. When the best bid and the best ask at NBBO are available on all exchanges, over 30 percent of trade volume is executed at the BX, where the inverted fee structure attracts market order traders seeking NBBO liquidity. When every exchange except for BX has the NBBO limit orders, a similarly high number trades is routed to the BATS Y-Exchange (BYX). BYX, like BX, offers inverted fee structure, but with much smaller fees and rebates for removing liquidity. When the NBBO is not available solely on BX and BYX, the 30+ percent market share moves to Direct Edge's EDGA, an exchange with normal but low fee structure. When the NBBO is available everywhere except for BX, BYX, and EDGA, the trading volume moves on largely to the NYSE, although Nasdaq and BATS also benefit from the flow. The economic incentives associated with inverted price structures clearly work: the asymmetric order flow enjoyed by BX creates the first-taker advantage for Nasdaq, the parent company of BX.

### **Figure 3.9** Percentage of Trades Executed at Each Trading Venue When NBBO Is Present at Certain Venues

#### *Source:* Pragma Securities (2011)

![](_page_18_Figure_3.jpeg)

High market share of trades does not alone contribute to the profitability of the exchange, as other fees can provide significant contributions to the bottom line of the exchanges. For example, both normal and inverted exchanges charge traders' fees for routing orders to other trading venues when the NBBO is not available on the current exchange. Thus, even an exchange with lowest proportion of NBBO can remain profitable by attracting enough orders and charging fees for routing said orders elsewhere.

### Fragmentation in Futures

Futures exchanges operated in a manner similar to equity exchanhes, but without rebate pricing implemented or foreseeable at the time this book was written. In a bid to attract liquidity, and unlike the rebate structure prevalent in equities, futures exchanges have been deploying pro-rata matching, discussed earlier. Other differences among futures exchanges are predominantly based on their operational and risk management decisions, such as when to draw the circuit breakers and so on, described in detail in Chapter 13.

## Fragmentation in Options

Various options exchanges have sprung up over the past decade. A majority of the exchanges, however, operate on similar principles and are driven by the same group of market makers.

Due to the sheer number of options with different expiration dates and strike price combinations, most options are barely traded. The same 10 or so broker-dealers tend to provide liquidity on most equity options markets, with large spreads being common.

The relative lack of activity in options trading enables market surveillance for insider information. A large trade in the long-dated option or an option with a strike price far away from the current market price of the underlying usually represents a bet on someone's special knowledge, not yet revealed to the rest of the markets.

## Fragmentation in Forex

In Forex, interdealer brokers begin competing with broker-dealers for direct access to end traders. The traditionally interdealer brokers Currenex and iCAP, for example, now accept selected institutional customers. In breaking with other exchanges, iCAP offers a 250-microsecond validity on all of its top-of-the-book foreign exchange (forex) quotes.

### Fragmentation in Fixed Income

While most fixed income traditionally traded OTC, some signs point to a potential near-term exchange-ization of the fixed-income market. Thus, iCAP has planned to launch a fixed-income matching engine using the Nasdaq OMX technology. The iCAP offering would further target institutional investors by providing a one-second validity of all top-of-thebook quotes.

## Fragmentation in Swaps

Swaps have also traditionally traded OTC, with privately negotiated contracts. Under the Dodd-Frank Act, swaps are required to be standardized and traded electronically on exchanges. A new class of trading venues, collectively known as *swaps execution facilities* (SEFs), was jointly shaped by the industry and regulators at the time this book was written.

### Summary

Modern markets are complex businesses ever concerned with streamlining their operations with the goal of delivering the most immediate, costeffective service to their customers. The competition of trading venues has led to the innovation and evolution in methods, pricing, and service models of exchanges and alternative trading systems. While technology remains the key driver in development of faster and leaner offerings, the solutions are becoming more customer-centric, producing trading products customized to clients' unique execution needs.

## End-of-Chapter Questions

1. What is the difference between the normal and inverted exchanges?

2. What type of orders would you use to buy a large quantity? Why?

3. You are given the task of developing an algorithm optimizing liquidation (selling) of a large equity position. Your aim is to develop an algorithm that maximizes execution costs while minimizing speed of liquidation process. How would you develop such an algorithm giving normal and inverted price structures of modern equity exchanges?

4. You are receiving Level I and Level II data on a certain futures contract from a well-known exchange. At 13:45:00:01:060 GMT, the aggregate liquidity reported at the best bid of 12.7962 comprises 325 contracts. The next tick of data is a trade print with a timestamp of 13:45:00:01:075 GMT, recording a trade of 900 contracts at 12.7962. The following tick is

a 13:45:00:01:095 GMT quote citing the best bid of 12.7962 with the size of 325 contracts. What has happened in the market from 13:45:00:01:060 GMT to 13:45:00:01:095 GMT?

5. The current right-hand side of the limit order book for a particular stock on a given exchange shows the following information: Best Ask: 100 shares at 35.67, 200 shares at 35.68, 100 shares at 35.69. What is the average price per share you are likely to receive on your market buy order of 250 shares if the National Best Bid is advertised as 35.67? What if the National Best Bid is 35.65 instead?

6. Is an iceberg order passive or aggressive?

7. The last recorded trade price in a given options market is 2.83. The prevailing best bid is 2.65 and the prevailing best ask is 2.90. Is a limit order to buy 10 contracts at 2.85 passive or aggressive? Why?

8. A quantitative researcher ("quant") develops his investing models using daily closing prices. What order types should an execution trader use to execute the quant's buy-and-sell decisions?
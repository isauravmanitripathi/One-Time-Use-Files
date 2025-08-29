#### **CHAPTER 12**

# Additional HFT Strategies, Market Manipulation, and Market Crashes

As Chapters 8 through 11 illustrate, high-frequency trading (HFT) by and large automates human trading. The opponents of HFT, however, perceive a range of adverse HFT outcomes that have the potential to negatively impact market dynamics. This chapter discusses these perceived threats in detail, along with methods that enable detection of high-frequency market manipulation and future market crashes.

Opinions on HFT continue to run the gamut. On one end of the spectrum we find employers in the financial services industry. Just open the "Jobs" page in "Money and Investment" section in the *Wall Street Journal,* and you will mostly find job postings seeking talent for HFT roles. The advertising employers are the whitest shoe investment banks like Morgan Stanley. These careful firms generally invest resources into something they deem worthwhile and legitimate. The extent of their hiring (often the only hiring advertised in the *Wall Street Journal*) implies that the industry is enormously profitable and here to stay.

At the other extreme we find individuals such as Mark Cuban, a successful Dallas-based businessman, who recently proclaimed that he is afraid of high-frequency traders. Mr. Cuban's fears are based on his belief that high-frequency traders are nothing more than "hackers," seeking to game the markets and take unfair advantage of systems and investors.

So how can Mr. Cuban and Morgan Stanley have such divergent views of the high-frequency world? For one, Mr. Cuban has likely fallen prey to some unscrupulous uncompetitive financial services providers making a scapegoat out of high-frequency traders. Opponents of high-frequency traders identify a range of purported HFT strategies that are supposedly evidence of how HFT destroys the markets. Purportedly malicious HFT strategies compiled by one of the workgroups of the Commodity Futures

Trading Commission's (CFTC) subcommittee on HFT included such ominous names as *spread scalping, market ignition,* and *sniping,* just to name a few.

As this chapter shows, strategies thought to be malicious and often associated with HFT fall into one of the following categories:

- Legitimate strategies serving price discovery.
- Strategies not feasible in "lit" markets–regulated exchanges; the same strategies can be feasible in dark pools.
- Strategies that are a direct consequence of pump-and-dump activity, a market manipulation technique that is banned in most financial markets.

The CFTC subcommittee on HFT tasked with identifying undesirable HFT strategies identified the following instances:

- Latency arbitrage
- Spread scalping
- Rebate capture
- Quote matching
- Layering
- Ignition
- Pinging/Sniping/Sniffing
- Quote stuffing
- Spoofing
- Pump-and-dump manipulation
- Machine learning

Each of the proposed activities is discussed in detail in the following sections. While some market participants claim that HFTs can also manipulate markets via special front-running order types, such advanced orders typically carry a heavier price tag that annihilates any excess profitability of such orders in the long term, rendering the orders unprofitable to HFT. This chapter also discusses methodologies for detection of pump-and-dump activity.

### Latency Arbitrage

*Latency arbitrage* is often pinpointed by the opponents of HFT as the most direct example of the technological arms race, and one without obvious consequences. To succeed in latency arbitrage, unlike other HFT strategies discussed in Chapters 8 through 11, deployment of the fastest technology is pivotal. Contrary to the belief of some, however, latency arbitrage has a well-defined market benefit, described next.

An important concept of financial theory is the Law of One Price. The Law states that in well-functioning markets, a given financial instrument always has the same price, regardless of the characteristics of markets where the financial instrument trades. The Law of One Price then serves to assure low-frequency investors that their trading will always be at the fair market price, no matter in which market they decide to trade. In other words, in ideal theoretical market conditions, the price of the IBM stock in London should always be the same as the price of IBM in New York, after adjusting for foreign exchange.

When prices of the same financial instrument in different markets diverge for whatever reason, high-frequency latency arbitrageurs jump in and trade away the price discrepancies. For example, HF latency traders sell IBM in the market where the stock is temporarily overpriced, while simultaneously buying it where the stock trades too cheaply. In the process, the demand and supply produced by the high-frequency traders serves to equilibrate the market prices in previously divergent markets. The high-frequency trader then quickly reverses his position to capture the gain, and investors of all frequencies can be assured that prices on traded financial instruments are consistent across the globe, upholding the Law of One Price.

Latency arbitrage is an example of a trading strategy that is based on taking advantage of high speeds. A question commonly asked by market participants and regulators alike is how much speed is enough? When does the race end? Should there be a limit on how much speed is acceptable in the markets? From the economic point of view, the race for speed will end as soon as there is equilibrium between increasing technological capacity and trading profitability: when an additional dollar spent on technology no

longer generates extra return. Until that time, competition among highfrequency traders will continue to foster innovation in the area of trading.

### Spread Scalping

High-frequency *spread scalping* often refers to an automated marketmaking activity that some market participants think is simple: a continuous two-sided provision of liquidity that generates or "scalps" the spread value for the account of the HFT. As discussed in Chapter 10, such activity is subject to extensive inventory and adverse selection risks and can hardly be profitable in its simplest incarnation. Even in a nearly stagnant market, market making is subject to inventory risk, whereby the market maker's accumulated positions rise and fall with variations in the markets. In the absence of opposing market orders, the market maker may not be able to profitably liquidate his positions. Significant analysis of market conditions, presented in Chapters 10 and 11, is necessary to ensure profitability of seemingly naïve spread-capturing strategies.

As discussed in Chapter 11, even in their normal state, markets are fraught with informational asymmetries, whereby some traders know more than the market maker. Better-informed traders may have superior information about industry fundamentals or just superior forecasting skills. In such situations, better-informed traders are bound to leave the market maker on the losing end of trades, erasing all other spread-scalping profits the market maker may have accumulated.

For a specific example, consider a news announcement. Suppose an alleggedly spread-scalping HFT has positions on both sides of the market, ahead of the impending announcement on the jobs figures—information on how many jobs were added or lost during the preceding month. A betterinformed trader, whether of the low- or high-frequency variety, may have forecasted with reasonable accuracy that the jobs number is likely to have increased. Suppose the better-informed trader next decides to bet on his forecast, sending a large market buy order to the market. The presumed spread-scalping market maker then takes the opposite side of the informedtrader's order, selling large quantities in the market that is just about to rise considerably on the news announcement. In a matter of seconds, and due to

activity of lower-frequency traders, our high-frequency market maker may end up with a considerable loss in his portfolio.

In summary, spread scalping may seem like a predatory strategy to some market participants, yet it is hardly profitable in its most naïve incarnation. Spread scalping enhanced with inventory and informational considerations is what most market participants call market making, a legitimate activity that is the integral part of market functionality. Without limit orders sitting on either side of the spread, traders desiring immediacy would not be capable of executing their market orders. Compensation of a spread is a tiny profit comparable to the amount of work required to be able to provide the limit orders on both sides of the market on the daily basis.

### Rebate Capture

Another strategy often put forth as an example of the dangers of HFT is the *rebate capture.* Under this strategy, high-frequency traders are presumed to generate profit simply by arbitraging the costs and benefits of limit and market orders on various exchanges. The strategy is thought to be an empty exercise with no economic value, and a frequent example of what is wrong with market fragmentation. In reality, as this section illustrates, rebates help improve the profitability of trading strategies, but cannot deliver profitability without other forecasting methodologies, such as the ones presented in Chapters 8 through 11.

To be profitable, a high-frequency trader needs to execute an order and hold a position long enough to realize a gain. As outlined in Chapter 3, rebates for limit and market orders presently exist only in equities, where a myriad of exchanges seek to differentiate them from the rest of the pack. The minimum gain per trade in most U.S. equity markets is currently \$0.01. In normal rebate markets, the exchanges pay rebates to traders posting limit orders, and providing liquidity by doing so. The New York Stock Exchange (NYSE), for example, pays \$0.13 to \$0.30 for every 100 shares to traders posting limit orders. Consider a trader who estimates ahead of each trade the directional probability of a stock going up 1 tick or \$0.01 is *pup* . In the current NYSE environment, a rational high-frequency trader will post a

limit buy order only when the marginal cumulative rebate value exceeds the trader's expected return:

(1)

where \$*rebate* is the value of the rebate per share, and \$(*transaction costs*) represents the costs the trader needs to pay per share to execute his trades. Transaction costs in equities may include a clearing fee, a transaction fee, a FINRA pass-through fee, and a NYSE pass-through fee, in addition to broker-dealer commissions.

Equation (1) is equivalent to

(2)

As the inequality (2) shows, in the absence of rebates, a limit order– posting trader has to predict direction of the price correctly with probability greater than 50 percent. A broker-dealer advertises that transaction costs for selling 30 million shares without considering NYSE rebates run about \$50,000, or \$0.0016 per share. When executed as a market order, the 30 million shares incur the additional NYSE fee, a negative rebate, for removing liquidity of about \$70,000 or another \$0.0023 per share. To be profitable under such cost structure, a rational high-frequency trader needs to have forecasting that reliably predicts probability of market movement, *pup* , to be at least 70 percent:

(3)

When posting the same 30 million shares as limit orders, the trader receives \$60,000 in rebates or \$0.0020 per share, offsetting the nonrebate transaction costs and generating about \$10,000 or \$0.0003 in profit per trade. This rebate-driven profitability allows the high-frequency trader to lower his required probability of correct directional forecasting, but just to 48 percent:

(4)

In other words, while rebates decrease the required accuracy of highfrequency forecasts, and the respective probability of forecast correctness, the rebates do not allow random trading strategies to be profitable. As with

the spread-scalping strategy, a successful rebate capture is a complex market-making operation, with rebates serving as a minor improvement of performance, and not as a primary source of profitability.

### Quote Matching

In a so-called quote-matching strategy, a high-frequency trader is thought to mimic the limit orders of another trader. A high-frequency trader is then thought to ride the market impact the original orders generate. If feasible, such a strategy could negatively impact block trades of a large investor by amplifying the market impact and worsening the pricing the investor obtains on subsequent child trades. The strategy assumes that the highfrequency trader is capable of identifying which limit orders always move the markets in the certain direction in the short term, allowing the highfrequency trader to quickly take advantage of the move, reversing positions and capturing the profit. Specifically, the success of the strategy is predicated on the high-frequency trader's ability to foresee which limit orders generate positive or negative market impact.

The key assumption of the strategy is the primary reason for its infeasibility. Most of today's exchanges are anonymous: They protect the identity of traders, disallowing the HFTs the ability to tag and follow orders of a specific entity. Furthermore, as discussed in Chapter 5, while many buy orders are followed by a positive price movement in the short term, the movement is by no means guaranteed. In the case of limit orders, while the market impact following a limit buy order is positive on average, it is very small even for top-of-the-book orders, and can be mostly negative or not statistically persistent for orders behind the market price. As a result, a quote matching strategy solely relying on copying other trader's limit orders is likely to be a disappointment.

## Layering

In *layering,* a high-frequency trader enters limit orders at different price levels away from the market price, often to cancel the orders in the near

future, and then to resubmit the orders again. The objectives of layering often confound casual observers, who in turn suspect wrongdoing.

Some layering may indeed be manipulative. The manipulative layering is one-sided: a market participant "layers" either buy or sell side of the order book with limit orders and then promptly cancels the orders with the intent of changing other traders' inferences about available supply and demand, The Securities and Exchange Commission (SEC) penalized such layering in highly publicized cases in September 2012.

Much of layering, however, is a legitimate strategy, practiced by many executing brokers as well as market makers in limit order books with pricetime priority, described in Chapter 3. In most layering, a broker or a market maker leaves "placeholder" limit orders at different price points with the intent of securing a time priority in a given price queue of a limit order book. When the market price reaches a broker's order, the broker may pursue one of two paths:

- The broker may use his priority to execute a slice of an order, securing a preferential price for his customer.
- In the absence of customer orders, the broker may simply cancel the placeholder order.

Similarly, a market maker may decide to execute on the order or cancel it, depending on his estimates of inventory and information risks.

As such, most incarnations of the layering strategy are not manipulative but do create unwanted noise in the markets by clogging the networks and the matching engine with order cancellations. A successful solution implemented by the Chicago Mercantile Exchange (CME), for example, changes the execution of the matching engine from the price-time priority to a pro-rata schedule. As described in Chapter 3, under the pro-rata schedule, all limit orders posted at a given price level are executed at the same when the price level becomes the best bid or the best ask. Each limit order in the given price queue is matched partially, proportional to the size of each limit order. Such strategy eliminates the need to secure the time priority in the given queue, and, as a result, entirely removes the need for layering as means of securing priority of execution.

### Ignition

In an *ignition* strategy, a high-frequency trader is thought to detect the location of long-term investors' stop-loss orders and match against them, or "ignite" them. Next, the strategy assumes that large stop-loss positions will have a substantial impact on the market, allowing the high-frequency trader to ride the market impact wave, swiftly closing out his positions, all the while capturing small gains at the expense of long-term investors' losses.

In today's exchanges and other "lit" trading venues, such a strategy may work only as a result of market manipulation, such as pump-and-dump. To match against someone's orders placed well away from the market price, one needs to move the market price substantially in the direction of said stop loss orders. Market manipulation has always been illegal and can be screened using methodology described later in the chapter.

While a manipulation-free ignition strategy is not feasible in lit trading venues, such as all regulated exchanges, it can be deployed in dark pools. The dark pools, however, have been created for sophisticated institutional investors, explicitly without regulatory protection, and operate under the "buyer beware" principle.

### Pinging/Sniping/Sniffing/Phishing

*Pinging, sniping, sniffing,* and *phishing* monikers typically refer to the same general type of strategy. The pinging strategy, much like the ignition strategy, identifies hidden pools of limit orders and matches against those orders, creating and riding temporary market impact for small gains. Much like the ignition strategy, such a strategy is often observed in dark pools. Some dark pools, for example, Citibank's Automated Trading Desk, have designed ways to screen for pingers and charge them for pinging behavior. Such charges render pinging unprofitable and discourage pingers with market mechanisms.

While pinging is feasible in dark pools, it is not generally possible in lit markets, such as exchanges, unless it is accompanied by illegal market manipulation. Just as in the case of ignition strategies, in lit markets traders cannot selectively execute at random price levels away from the present

market price, unless they expressly move the price away from the market first. Such price movements construe market manipulation.

As discussed later in this chapter, some market conditions are more conducive to market manipulation than others. Avoiding conditions favorable to market manipulation may help traders to eliminate risks associated with ignition and other variants of pinging strategies.

### Quote Stuffing

*Quote stuffing* refers to a purported high-frequency strategy whereby a trader intentionally clogs the networks and the matching engine with a large number of limit orders and order cancellations. Unlike layering, where the high-frequency trader is seeking to ensure execution priority in the order book queues, quote-stuffing traders are thought to send in rapid orders and cancellations with the expressed purpose of slowing down other traders, and thus manipulating markets. Quote-stuffing traders are further thought to do so to delay other traders, ensure quote stuffers' priority access to the matching engine and the quote stream, and then effectively front-run other traders.

The idea of the quote-stuffing strategy contains one critical flaw: as any network engineer will confirm, an individual network account cannot selectively slow down network communication for some participants, while still receiving high-speed access to the trading venue. When a matching engine gets clogged with orders and cancellations, it is equally clogged for all market participants, irrespective of who caused the problem. Obviously, such network-clogging exercises do little for traders equipped with fast technology; if anything, network clogging only voids the benefits of fast technology. However, the network-clogging maneuver may be advantageous for low-frequency traders, those who indeed desire to slow down matching capabilities. If anyone can be suspected of intentionally clogging up the lines (a market manipulation), the natural trail leads to lowfrequency culprits unequipped with fast technology, for whom such manipulation may indeed result in increased profitability.

### Spoofing

The *spoofing* strategy is similar to layering but executed with a radically different intent. In spoofing, the trader intentionally distorts the order book without execution; in the process, the trader changing other traders' inferences about available supply and demand, and resulting prices. In principle, spoofing can be screened for and detected in most lit markets: while layering calls for fairly balanced entry of limit orders across all price ranges, spoofing would show one-sided peaks of limit orders in selected trading accounts. Spoofing has been made expressly illegal in the United States under the Dodd-Frank Act, and has been actively prosecuted. In 2011, for example, the U.S. CFTC fined Bunge Global Markets \$550,000 for spoofing at the market's open.

In summary, most strategies considered to be illicit HFT activity and reasoned to be the cause for which HFTs should be banned do not exist or are a direct consequence of already illegal activity, such as market manipulation. Identification of market manipulation activity and the market conditions conducive to market manipulation are discussed in the following section.

### Pump-and-Dump

*Pump-and-dump* is a truly adverse activity, whether implemented at high or low frequencies. The low-frequency pump-and-dump was well portrayed in the film *Boiler Room,* where unscrupulous brokers "pumped" or raised the value of a particular financial instrument just to dump it at the first opportunity, realizing a profit at the expense of other investors. The flip side of the pump-and-dump is the *bear raid,* whereby the trader artificially depresses the price of a financial instrument, only to close his position at a profit at the first available opportunity, all while leaving other investors in the dust.

In the high-frequency pump-and-dump, computer-assisted traders are thought to momentarily drive up or down the prices of securities, only to promptly reverse their positions and capitalize on false momentum at the expense of other traders. Huberman and Stanzl (2004) and Gatheral (2010)

have developed necessary conditions for the absence of high-frequency pump-and-dump opportunities: the posttrade permanent market impact function should be symmetric in size for buyer-initiated and seller-initiated trades. When the posttrade permanent market impact for buyer-initiated trades exceed that for seller-initiated trades, for example, a high-frequency trader could "pump" the security price through repeated purchases to a new high level and then "dump" the security, closing out his positions at a profit. The gain would originate solely from the asymmetric market impact: the absolute value of market impact following buy trades would differ from that following sell trades. On the other hand, when pump-and-dump is *not* feasible, the price change following a sell-initiated trade of size *V* is equal to the negative of the price change following a buy-initiated trade of size *V*, as shown in Figure 12.1. A pump-and-dump arbitrage opportunity exists when the "no-pump-no-dump" condition is violated.

**Figure 12.1** Market Impact that Rules Out High-Frequency Pump-and-Dump Manipulation

![](_page_12_Figure_1.jpeg)

Aldridge (2012e) formally describes pump-and-dump strategies using a measure of permanent market impact *f(V<sup>t</sup> )* of a trade of size *V<sup>t</sup>* processed at time *t,* where *Vt>*0 indicates a buyer-initiated trade and *Vt<*0 describes a seller-initiated trade. If *f(V) >* -*f(*-*V)*, a trader could artificially pump and then dump by first buying and then selling at the same trade size *V*. Conversely, if *f(V) <* -*f(*-*V)*, the trader could manipulate the markets by first selling and then buying the securities back.

To examine the evolution of market impact over time, we consider market impact within different event windows, where the length of the window is determined by a number of trade ticks before and after the market order event, as shown in Figure 12.2.

**Figure 12.2** Sequence of Events Used in Market Impact Computation

Denoting market impact function *f*, we obtain the following specification:

To evaluate the feasibility of the pump and dump, we use a linear specification for the market impact as a function of trading volume, *V*, consistent with Breen, Hodrick, and Korajczyk (2002); Kissell and Glantz (2002); and Lillo, Farmer, and Mantegna (2003), following Huberman and Stanzl (2004) and Gatheral (2010):

(5)

where *V<sup>t</sup>* is the size of trade executed at time *t*, *β<sup>τ</sup>* is the trade size–dependent market impact, and *α<sup>τ</sup>* is the trade size–independent impact of each trade recorded at time *t*. If the high-frequency pump-and-dump is feasible, *β<sup>τ</sup>* for buyer-initiated trades will be different from –*β<sup>τ</sup>* estimated for seller-initiated trades. The null hypothesis, that pump-and-dump exists in trading activity of a financial instrument, can then be specified as follows:

(6)

And the alternative hypothesis ruling out pump and dump can be specified as:

(7)

The framework above allows for straightforward screening for market manipulative activity in various financial instruments.

What does pump-and-dump detect? The example in Figure 12.3 illustrates the analysis on a sequence of Eurex Eurobund futures (symbol FGBL) trades, recorded sequentially and time-stamped with millisecond granularity. In addition to the timestamp, the data includes the trade price and trade size. The data is the "official" copy of the Eurex trading tape, and is commercially distributed to traders. The data does not contain best

bid/offer information or identification of whether the trades were initiated by the buyer or seller. To identify whether the trade was initiated by a market buy or a market sell, a tick rule discussed in Chapter 3 is used.

![](_page_14_Figure_1.jpeg)

<span id="page-14-1"></span>![](_page_14_Figure_2.jpeg)

In computing market impact (MI), overnight returns are treated as missing observations, ensuring that the MI on a specific day is a function of data recorded on that day only.

<span id="page-14-2"></span>[Table 12.1](#page-14-0) reports estimates of equation (5) for trades of all sizes by month of 2009–2010 period. [Figure 12.3](#page-14-1) graphically illustrates the relationship of volume coefficients for buy and sell trades. Figure 12.4 shows the results of the difference tests of volume coefficients observed for buy and sell trades.

<span id="page-14-0"></span>**[Table 12.1](#page-14-2)** Estimation of Size-Dependent Market Impact for Large and Small Trades in Eurobund Futures, by Month

|        | Buys, All Trade Sizes |                  |           |           |           | Sells, All Trade Sizes |                           |           |                         |           |
|--------|-----------------------|------------------|-----------|-----------|-----------|------------------------|---------------------------|-----------|-------------------------|-----------|
|        | $\text{\# obs}$       | $\alpha_{\rm c}$ | $t$ -stat | $\beta_s$ | $t$ -stat | # obs                  | $\alpha$                  | $t$ -stat | $\beta_5$               | $t$ -stat |
| 200901 | 373631                | $1.6E-5$         | 50.7      | $1.6E-7$  | 24.1      | 367857                 | $-2E-5$                   | $-50.5$   | $-1.4E-7 -18.6$         |           |
| 200902 | 332584                | $1.4E-5$         | 37.4      | $1.3E-7$  | 20.0      | 334078                 | $-1.7E-5$                 | $-46.0$   | $-1.1E-7$ $-17.6$       |           |
| 200903 | 400829                | $1.5E-5$         | 54.8      | $3E-8$    | 11.8      | 402137                 | $-1.6E-5$ $-55.5$         |           | $-4.8E-8 - 17.4$        |           |
| 200904 | 319454                | $1.0E-5$         | 39.5      | $1.8E-7$  | 37.3      | 318556                 | $-1.4E-5$                 | $-46.2$   | $-1E-7$                 | $-21.8$   |
| 200905 | 298859                | $1.2E-5$         | 37.1      | $1.1E-7$  | 23.3      | 300020                 | $-1.4E-5$ $-41.4$         |           | $-1.2E-7$ $-23.4$       |           |
| 200906 | 348640                | $1.2E-5$         | 32.4      | $3.8E-8$  | 11.9      | 341341                 | $-1.5E-5$                 | $-38.5$   | $-2.6E-8$               | $-7.7$    |
| 200907 | 310745                | $7.5E-6$         | 20.8      | $1.4E-7$  | 22.8      | 303278                 | $-1.2E-5$ $-29.3$         |           | $-1.1E-7$ $-17.1$       |           |
| 200908 | 284896                | $8.6E-6$         | 23.1      | $1.2E-7$  | 20.1      | 285690                 | $-1.3E-5$ $-30.3$         |           | $-1.2E-7$ $-17.0$       |           |
| 200909 | 331673                | $9.5E-6$         | 43.5      | $1.8E-8$  | 12.4      | 325211                 | $-1.1E-5$ $-42.5$         |           | $-2.9E-8$ $-15.0$       |           |
| 200910 | 337226                | $7.2E-6$         | 35.6      | $8.4E-8$  | 32.4      | 330927                 | $-8.1E-6$ $-38.2$         |           | $-8.3E-8$ $-28.9$       |           |
| 200911 | 283547                | $7.5E-6$         | 35.1      | $7.6E-8$  | 29.6      | 281327                 | $-9.6E-6$ $-39.2$ $-5E-8$ |           |                         | $-18.6$   |
| 200912 | 249533                | $8.6E-6$         | 23.2      | $1.4E-8$  | 6.4       | 248061                 | $-1.3E-5$ $-36.1$         |           | $-1.1E-8$               | $-5.1$    |
| 201001 | 247741                | $5.7E-6$         | 14.9      | $9.9E-8$  | 21.0      | 247258                 | $-1.1E-5$ $-22.7$         |           | $-6.9E-8$ $-12.1$       |           |
| 201002 | 298294                | $6.5E-6$         | 16,9      | $8.1E-8$  | 19.8      | 295019                 | $-1.1E-5$ $-29.5$         |           | $-5.4E-8$ $-14.1$       |           |
| 201003 | 295452                | $6.6E-6$         | 26.4      | $2.9E-8$  | 16.4      | 297502                 | $-9.5E-6$ $-34.8$         |           | $-1.9E-8$ $-11.9$       |           |
| 201004 | 297115                | $6.4E-6$         | 23.1      | $8.3E-8$  | 26.2      | 298106                 | $-8.3E-6$ $-31.7$         |           | $-7.3\text{E-8} - 24.6$ |           |
| 201005 | 413507                | $1.1E-5$         | 33.5      | $1.1E-7$  | 22.9      | 409226                 | $-1.3E-5$ $-45.1$         |           | $-8E-8$                 | $-20.3$   |
| 201006 | 393351                | $1.1E-5$         | 41.1      | $2.5E-8$  | 11.8      | 387231                 | $-1.4E-5$                 | $-45.8$   | $-2.1E-8$               | $-9.0$    |
| 201007 | 314054                | $6.3E-6$         | 18.5      | $1.2E-7$  | 23.9      | 307322                 | $-1.1E-5$ $-29.4$         |           | $-1.1E-7$ $-20.4$       |           |
| 201008 | 299741                | $7.1E-6$         | 17.4      | $9.9E-8$  | 18.6      | 296117                 | $-1.2E-5$                 | $-26.9$   | $-6.6E-8 -12.4$         |           |
| 201009 | 422772                | $1.3E-5$         | 61.0      | $2.5E-8$  | 15.5      | 419480                 | $-1.4E-5$ $-55.0$         |           | $-2.9E-8 -17.0$         |           |
| 201010 | 345432                | 8.7E-6           | 41.6      | $1.0E-7$  | 35.5      | 328033                 | $-9.6E-6$                 | $-42.2$   | $-1.1E-7$ $-35.2$       |           |
| 201011 | 447795                | $1.1E-5$         | 55.6      | $1.0E-7$  | 33.8      | 426999                 | $-1.3E-5$ $-52.9$         |           | $-9.3E-8$ $-27.8$       |           |
| 201012 | 305279                | $1.4E-5$         | 45.2      | $2.2E-8$  | 8.8       | 302936                 | $-1.8E-5$ $-49.3$ $-3E-8$ |           |                         | $-9.3$    |

Note: Coefficients for the entire sample, large trades and small trades, were estimated using the following linear regressions:  $\textit{MI}_{t+\Gamma}(\textit{V}) = \alpha_{\Gamma} + \beta_{\Gamma} \textit{V}_{t} + \epsilon_{t+\Gamma}$ , where the observations were separated into buys and sells.

**Figure 12.4** Difference in Volume-Attributable Market Impact, of Buyer-Initiated Trades Less That of Seller Initiated Trades

![](_page_16_Figure_1.jpeg)

The observed differences in buyer-initiated and seller-initiated market impact change from month to month and lack statistical significance. Based on the results, the FGBL futures data does not support the possibility of high-frequency pump-and-dump.

The results presented in Table 12.1 indicate another interesting phenomenon: trade-size-related MI does not begin to register until the trade size rises to about 100 contracts. The unexplained variation, intercept *α*, in the market impact equation is large (on the order of 10–5 ), and the traderelated MI is on the order of 10–7 , a single trade of up to 100 contracts may incur as much impact as a trade of 1 contract. This is great news for institutions and other large fund managers who are concerned about the impact of their trades—in the FGBL futures market, a single trade of a size considerably larger than the median trading size on average leaves no trace. Unlike the equities markets, the Eurex FGBL market is resilient to a much larger capacity.

To check whether the results are robust, several auxiliary explanatory variables can be added to the analysis: volatility, spread, and intertrade duration. Other studies found such additional explanatory variables for temporary market impact.

For example, in futures, Burghardt, Hanweck, and Lei (2006) show that posttrade MI is also dependent on liquidity characteristics, such as the market depth. Other studies have focused on equities. Breen, Hodrick, and Korajchyk (2002); Lillo, Farmer, and Mantegna (2003); and Almgren, Thum, Hauptmann, and Li (2005) showed that the permanent MI function in equities is dependent on stock-specific liquidity characteristics. Dufour and Engle (2000) find that longer intertrade duration leads to lower MI, and vice versa. Ferraris (2008) reports that several commercial models for equity MI use volatility and bid-ask spread prevailing at the time of the trade as predictive inputs to forecasts of MI of the trade. In the current study, we find that volatility, spread, and intertrade duration help explain market impact in futures as well. None of the auxiliary variables, however, change the symmetry between the volume-dependent MI coefficient created by buyer-initiated and seller-initiated trades. The auxiliary variables also do not alter the value or the statistical significance of the trade size– independent component, the intercept, leaving the dominant sizeindependent market impact unexplained.

### Machine Learning

Machine learning is often cited as one of the most worrisome event accompanying HFT. A CNBC commentator, Doug Kass, for example, in the conversation about HFT proposed that investors should shut down machines before machines attack investors. The belief that machines are capable of independent reasoning and intelligence similar to Arnold Schwarzenegger's *Terminator* film character resonates among some traditional market participants with little exposure to the fundamentals of technology. Machine learning is then cited as evidence of such machine intelligence.

In reality, machine learning originates in control theory and is often a series of nested analyses. Each analysis can be parametric, as basic as a simple linear regression, or nonparametric, a set free-form functional estimators. Independent of the type of the analysis used, the nature of machine learning remains the same: uncover patterns in data. As a result,

machine learning is less threatening intelligence, and more basic data mining.

Machine learning can be broken down into two major categories: supervised learning and unsupervised learning. Supervised learning is the iterative estimation of data relationships, whereby each subsequent iteration seeks to minimize the deviations from the previous analysis. Models used to fit data in supervised learning models may range from regression to neural networks to boosting algorithms discussed below. Unsupervised learning seeks to identify patterns in so-called unstructured data, devoid of any relationships. Techniques used to distill information under an unsupervised learning umbrella include identification of important signals by observing clustering of data points.

A supervised boosting algorithm, for example, works as follows: a dependent variable *Y*, for instance, a time series of returns on a particular financial instrument, is fitted with a function *G*, expressing dependence of *Y* on returns of another financial instrument, *X*, and parameters *θ*:

(8)

Next, the boosting error term is computed as follows:

(9)

where *I st<>0* is the indicator function taking on value of 0 when *G(X<sup>t</sup> , θ)* matches *Y<sup>t</sup>* precisely, and 1 when *t* is not equal to 0. The time series *w<sup>t</sup>* represents boosting weights assigned to each observation time, with all weights in the first iteration set to 1, and weights in later iterations recomputed according to the following calculation:

(10)

where

$$\alpha = \log \left( \frac{1 - s_t}{s_t} \right)$$

This machine learning methodology ultimately produces a function *G(X<sup>t</sup> , θ)* that closely fits *Y<sup>t</sup>* . Human researchers running the machine learning simulation select the parameters such window sizes for training and testing, additional predictors, etc.

Machine learning algorithms may suffer from a critical flaw: data mining devoid of economic underpinnings may produce relationships that may have been stable in the past, but are not stable in the long term. Such accidental relationships are known as *spurious* inferences, and are not reliable predictors for future behavior of dependent variables. At the time this book was written, no machine learning algorithm was capable of intelligence beyond its immediate trading application and was certainly not threatening to humans.

#### Summary

This chapter discusses algorithms often presented as evidence of adverse outcomes from HFT. As the chapter illustrates most of the fears surrounding HFT strategies are unwarranted. Some strategies, however, are a direct consequence of high-frequency market manipulation, yet even those strategies can be screened for, greatly reducing the risks to all market participants.

### End-of-Chapter Questions

1. What is latency arbitrage?

2. Suppose a stock of IBM is simultaneously trading at 125.03 on the NYSE and at 125.07 in Tokyo. Does latency arbitrage deliver positive or negative impact on the price of IBM from the market efficiency point of view?

3. What is spread scalping? What is rebate capture?

4. What kind of layering is manipulative? What kind of layering is benign?

5. How can one detect pump-and-dump high-frequency manipulation?

6. What is machine learning?
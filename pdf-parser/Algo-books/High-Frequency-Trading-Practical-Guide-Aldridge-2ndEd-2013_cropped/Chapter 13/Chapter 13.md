### **CHAPTER 13**

#### **Regulation**

At the time this book was written, high-frequency trading (HFT) was already a heavily regulated market activity, tracked at the broker-dealer level. Current regulation of HFT follows much the same rules as other forms of trading in a given financial instrument. Indeed, as this book shows, HFT is little more than automation of traditional trading processes and should be regulated as such. Proponents of HFT regulation, however, call for stricter monitoring of machines, citing examples of market failures such as the flash crash of May 6, 2010; the botched initial public offering (IPO) of electronic ATS BATS (Best Alternative Trading System) on March 23, 2012; and the spectacular \$10-million-per-minute loss of Knight Capital Group on August 1, 2012. This chapter discusses modern legislation relevant to HFT, traditional and current approaches, and likely imminent directions.

# Key Initiatives of Regulators Worldwide

Currently, main issues on the regulatory table include:

- Jurisdiction
- Stability of systems
- Investor protection
- Efficient trade matching
- Market structure

This section considers each of the issues in detail.

### Jurisdiction

The long shadow cast by market regulators covers HFT as part of their mandate to provide legal oversight to markets at large. Roles and objectives of market regulators have evolved on a regional basis due to philosophies and histories of individual jurisdictions.

Most of U.S. regulation represents a rule-based approach, in which regulators prescribe specific remedies as well as punishments for certain behaviors observed in the markets. By contrast, regulators of the European Union have established a principle-based regulatory system, whereby each regulatory case is evaluated in its conformance with the general principles of desired market systems. The differences between the U.S. and EU regulatory models can be traced to the philosophical differences that exist between regulatory systems in the two regions. In the United States, the objective of regulation has been to level the playing field, allowing equal access to the markets for large investors and for "widows and orphans" alike. Behaviors blocking fair access are considered to go against the grain of the U.S. markets. Such behaviors are actively identified, documented, and dealt with. In the European Union, however, the main tenet of regulation can be distilled to fairness of gains—an action that is deemed unfair to a contingent of traders may run afoul of European regulators.

Other countries have developed their own regulatory styles. The key objective of Australian regulators, for example, tends to be market integrity. The U.K. government has taken more of a forward-looking approach to regulation, working to anticipate future developments and then assessing the resulting impact. Canadian regulators seek to conform to the international standards of financial regulation, and, specifically those promulgated by the International Organization of Securities Commissions (IOSCO).

Jurisdictional issues arise within each country, as well. In the United States, for example, regulatory rules for various markets are developed and adopted by several agencies. The Securities and Exchange Commission (SEC) oversees trading in equities and related products, like equity options, exchange-traded funds, and so on. The Commodity Futures Trading Commission (CFTC) deals with futures contracts and related markets, such as options on futures. Swaps and futures on fixed income and foreign exchange also fall under the jurisdiction of the CFTC, even though foreign exchange itself is not regulated outside of basic common investor frameworks. In addition to the SEC and CFTC, the U.S. regulatory system includes industry self-regulatory organizations (SROs). Financial Industry Regulatory Authority (FINRA) navigates the world of equities. In this role,

FINRA administers industry licensing examinations and maintains firstlevel supervision of market abuses. Potential cases of market manipulation detected by FINRA are next sent over to the SEC for further examination. The Futures Industry Association (FIA) is the futures equivalent to FINRA and promotes best practices among futures traders.

Regulatory approaches can vary dramatically from one asset regulator to the next. The U.S. equities, for example, have been subject to three groundbreaking regulations in the past 15 years. The 1997 Order Display Rule required exchanges to display limit orders of all customers, no matter how small. The rule for the first time allowed all sorts of trading entities, including individuals, to make markets. Previously, such privileges were bestowed only on members of the exchange and selected broker-dealers paying dearly for such ability. Regulation Automated Trading Systems (Reg ATS), that went into force in 1998, further mandated electronization of exchanges and has led to the ability to receive, process and store quotes electronically, bringing in great transparency of prices at tick levels. Regulation National Market Systems (Reg NMS), enacted in 2005, further enhanced an investor's ability to track a broker-dealer's execution. In the 1980s, a client executing a market order had only the daily open, high, low, and close quotes, printed in the next day's newspaper, as a reference for the price given by the broker. Under Reg NMS, all investors can be assured of validity of their execution prices within a minute from trade prints recorded in the centralized ticker-data tape, Securities Information Processor (SIP). The one-minute window for submitting quotes into SIP under Reg NMS may seem too large by now. After all, most broker-dealers in the United States can guarantee the execution of a market order in as little as onehundredth of a second (10 milliseconds) or faster, while selected U.S. exchanges can receive a market order, match it, and send back the acknowledgment in as little as a quarter of a one-thousandth of a second (250 microseconds). Still, even with a 1-minute window Reg NMS delivers investors and end traders much needed execution benchmark prices.

Reg NMS has introduced another structure peculiar to equities: the National Best Bid and Offer rule (NBBO). Under NBBO, all equity exchanges may only execute at the price distributed in SIP or better. If a given exchange does not have enough limit orders on hand to execute an

incoming market order at the NBBO, the exchange must route the market order to another exchange.

The order-forwarding rule of the Reg NMS created a new line of differentiation for exchanges: flash orders. When a U.S. exchange does not possess limit orders satisfying the NBBO, the exchange may choose to broadcast or "flash" the incoming and instantly departing market orders to the subscribers of the exchange data. At present, most exchanges have voluntarily banned flash orders, yet some exchanges, such as DirectEdge, persist in flash order executions. The flashing is really a negotiation tactic for traders choosing to place their orders on the DirectEdge exchange: when DirectEdge does not have NBBO, the traders flash their intent to execute, and invite matching limit orders with potential price improvements over contemporary NBBO to the table. Most orders from DirectEdge are typically forwarded to Boston OMX, where flash order observers at DirectEdge can immediately direct their orders, should they be inclined to take on the orders flashing on DirectEdge. While the flash order system as a whole is not set up for investors with slow communication, the system is fair as it is based on voluntary participation: only the traders desiring to flash or be flashed trade at DirectEdge, rendering DirectEdge a special negotiation venue and separating the exchange from the pack. A study by Brodsky (2011), for example, confirms that flash orders result in price improvements, yet disincentivize liquidity provision on flashing exchanges, reducing the traded volume.

The U.S. SEC has also taken steps to ban *naked access,* also known as *sponsored access* and *direct market access* (DMA). Under DMA, brokerdealers would lend traders their identification information and allow traders to use the information to access exchanges directly, without any risk checks. DMA makes complete sense to sophisticated traders, who can develop their own execution systems (discussed in Chapter 15 of this book) and avoid paying fees to broker-dealers. At present, however, most exchanges use broker-dealer identification to stamp the trades. When many traders use the same broker-dealer's ID without a broker-dealer's checks and records under DMA, the exchanges or the ID-lending broker-dealers are unable to discern which trader caused which type of market reaction, complicating existing surveillance. The legal entity identifier (LEI), discussed in the following

section, is likely to resolve this issue by granting the exchanges the ability to track and measure risks of end traders numbered with individual LEIs. Once implemented, the LEI initiative may lead to reinstatement of DMA privileges, this time with even smaller involvement by broker-dealers.

The U.S. CFTC has also taken on co-location and proximity services. As discussed in Chapter 2, co-location implies that the location of a trader's machine in the same facility as the exchange's servers. Proximity hosting, however, leaves traders' machines in a building in the proximity of the exchange, but not in the same exact facility. To ensure transparent pricing and fair access, in June 2010 the CFTC recommended that all co-location and proximity hosting facilities implement uniform fees to all their customers, and to disclose their longest, shortest, and average latencies to all current and prospective clients.<sup>1</sup>

Following the flash crash, the SEC and CFTC introduced clear rules under which erroneous trades can be corrected or "busted." The new rules were successfully applied in the Knight Capital fiasco of August 2012.

European regulators have generally followed the U.S. model; they have voted against naked access, flash orders, and quote stuffing, discussed in Chapter 12. They have also called for risk and error controls for algorithmic systems, minimum quote life, and equal access to co-location services. Overall, however, the Europeans have treaded lightly on the HFT. In light of European financial woes, HFT has been viewed by some as the source of free money for all. A transaction taxation proposal, introduced by Greek parliamentarians and recently ratified by the broader EU Parliament, calls for a small tax on all trading activity. The proposal finds substantial riches in the European financial markets and considers that the trading activity will shrink little in response to the tax.

Given today's mobility of international capital, however, such a tax is likely to backfire. Most of today's trading systems communicate using Financial Information eXchange (FIX), a computer mark-up language discussed in detail in Chapter 6. Changing from trading in one country to trading in another takes as little as changing a few lines in FIX code; after such a minute change, the trader can execute in a jurisdiction free of transaction taxes. Even if all the countries around the world agree to impose an identical transaction tax, the measure would likely fail as the temptation

and the instantaneous benefits from breaking the agreement would be just too high—the first jurisdiction to defect the agreement would collect all the global trading activity that can move quickly, generating great trading and settlement premia.

The U.K. regulators have taken a most proactive approach, that of creating rules for envisioned future of computer trading. The U.K. government has identified the following four dimensions of instability potentially caused by computer trading:

1. Nonlinear sensitivities to change, whereby small perturbations in code of trading systems or matching engines have large system-wide impact.

2. Incomplete information, where some market participants are able to assemble a more accurate picture of the markets than others.

3. Normalization of variance, where unexpected and risky events can be seen increasingly as normal.

<span id="page-5-1"></span>4. Internal risks amplified by system-wide feedback loops that include risk-management systems, changes in market volatility, market news, and a delay in obtaining reference data, as illustrated in [Figure 13.1.](#page-5-0)

<span id="page-5-0"></span>**[Figure 13.1](#page-5-1)** Key Findings of the U.K. Foresight Initiative on Computerized Trading: Problem-Amplifying Feedback Loops

*Source:* Zigrand, Cliff, Hendershott (2011)

![](_page_6_Figure_0.jpeg)

![](_page_7_Figure_0.jpeg)

### Stability of Systems: Detecting Error-Prone Algorithms

The stability of systems refers to the ideal operational scenario of markets: trading free of inadvertent algorithmic errors. Nothing in recent memory illustrates the host of issues surrounding erroneous algorithms better than the recent "incident" of Knight Capital Group, when a poorly tested and illoperated algorithm wreaked havoc in the markets. A whopping 45 minutes after the start of trading, employees at the New York Stock Exchange noticed that Knight Capital's system was losing on average US\$10 million every minute. (Employees at Knight Capital still appeared to be oblivious to the fact at that moment.)

In the case of Knight Capital, it was the portfolio of Knight Capital itself that bore the brunt of the incident. However, it is easy to imagine how a similar scenario could have affected other market participants. To limit or eliminate the occurrences of such rampant algo issues, regulators are naturally mulling ways to police markets with the goal of ensuring stability, much like the highway patrol polices roads for errant drivers who may present dangers to themselves and others.

The surveillance for erroneous algos is best performed in real time. As the example of Knight Capital shows, even a 45-minute delay before pinpointing Knight's problem cost Knight's shareholders US\$440 million. Modern regulators, however, are ill equipped for such a task. In the United States, both FINRA and CFTC currently collect volumes of tick data from every executed transaction the following business day, or "on the T+1 basis."<sup>2</sup> While the T+1 data is perfectly suitable for identification of market manipulation or other activity requiring multiday recurrence, as discussed in the next subsection, next-day data cannot detect algorithmic problems in real time.

Instead of implementing complex data screening systems for real-time surveillance at their offices, however, regulators may be much more productive in the field. At the level of clearing firms, for example, regulators can observe all the counterparties and their trades. Yet, most clearing happens at the end of the trading day, and such surveillance would be tardy for many fast-moving markets. Surveillance at the executing firm

level, that is, broker-dealers, is also feasible, yet can be complicated, as many traders utilize services of multiple brokers, and aggregating trades across brokers in real time can be a challenge. Surveillance at the matching level may prove to be the best solution, with exchanges best positioned to observe and detect market irregularities across multiple accounts in real time. After all, in the case of the Knight Capital Group debacle, it was the exchange, NYSE, that was first to sound an alarm about unusual behavior of Knight's trading. While it took the NYSE 45 minutes to establish erroneous trading patterns on the exchange, modern technology can detect patterns in much shorter time frames.

Still, unresolved issues surrounding exchange-level surveillance persist: for example, how to aggregate data among exchanges to track cross-asset trading strategies. Some proposed synchronizing timestamps of exchanges using equipment used in global positioning systems (GPSs). The opponents of time synchronization, however, cite market participants' reluctance to forfeit freedom to deploy technology of choice. In addition, the opponents point to the latency inherent in GPS-based synchronization: depending on the location of the exchange, even GPS-wound clocks may differ by several microseconds—an issue in today's fast-paced markets.

### Currently Deployed Measures for System Stability

At present, most exchanges have already enabled some forms of real-time surveillance. All exchanges today, for example, are required to implement circuit breakers that halt trading in a selected financial instrument for several minutes following an intraday price drop of several percentage points. Futures exchanges like the CME and the Intercontinental Commodity Exchange (ICE) have also introduced the following measures described in detail next:

- Interval price limits
- No-cancel range
- Protection points
- Cancel orders on system disconnect
- Message throttle limits
- Maximum quantity limits
- Real-time position validation

Price reasonability

## Interval Price Limits

*Interval price limits* (IPLs) are circuit breakers that are triggered by extreme short-term moves. The IPL-based halts work as follows. For each traded financial instrument, the exchange computes a moving average price level and a "normal" variation determined on the highs and lows evidenced in the moving data window used in computation. The moving average price plus and minus the variation parameter define the upper and lower IPLs, illustrated in [Figure 13.2.](#page-10-0) As shown in [Figure 13.2,](#page-10-0) when the price falls below the lower IPL, the trading is halted until one of the two following situations occur:

<span id="page-10-1"></span><span id="page-10-0"></span>**[Figure 13.2](#page-10-1)** Illustration of Interval Price Limits

*Source:* ICE

![](_page_10_Figure_5.jpeg)

- The price reverts to a higher level above the lower IPL.
- The IPL computational period shifts and the new IPL is lower than the previous limit, allowing trading.

The width of the window used for computing the price bands is determined by the trading frequency of the financial instrument: the price bands for a frequently traded instrument will be recomputed more often than those for the instrument with little activity.

## No-Cancel Range

*No-cancel range* refers to the depth of quotes in the limit order book, where the limit orders cannot be cancelled for a predetermined period of time. When the no-cancel range comprises only the best bid and the best ask, the measure is also known as the minimum quote life (MQL). At the foreign exchange interdealer broker EBS, for example, limit orders placed at the best bid and the best ask cannot be canceled for 250 milliseconds (ms) from the time the order was placed. As a result, within the quarter of a second, the best bid and best ask quotes may change only when the limit orders are matched with an incoming market order. The ICE has also instituted a measure whereby limit orders falling in the no-cancel range may not be canceled altogether. In the case of both EBS and ICE, the limit orders can be canceled as soon as they fall out of the no-cancel range due to natural price movements.

Introduction of MQL appears to be of little consequence to the markets. A study by Chaboud (2012), for example, showed that the markets were much more impacted by overhaul in the EBS matching algorithm than the introduction of MQL. The no-cancel range may gain popularity with other exchanges or be mandated in the near future.

### Protection Points

*Protection points* stipulate the maximum number of price levels or ticks a large incoming market order can sweep through in the limit order book. When a market buy order sweeps through the maximum number of price levels and is still not filled in its entirety, the unfilled remainder of the order is automatically converted into a limit buy order. Protection points are

currently in use on the CME. Protection points were created in response to a previously common occurrence in the futures markets—large market orders that could sweep as many as 100 ticks of the order book at once. The sweeps disadvantaged the traders and the markets alike: traders received poor average prices on their large orders, and markets were left bare, with little or no liquidity, as a result of the sweeps. Today, protection points are welcomed by the trading community.

## Cancel Orders on System Disconnect

Exchanges and broker-dealers alike continuously monitor "heartbeat" messages from their clients, as described in Chapter 16. When a client fails to check in with the regular heartbeat, and then misses further scheduled "pings," the client connection is assumed to have been terminated. Exchanges such as CME take cancel limit orders of disconnected clients as a protective measure. The cancellation of limit orders is performed to ensure that the clients do not execute orders when they are unable to monitor their positions, reducing the incidence of unwanted trade executions.

## Message Throttle Limits

The *message throttle limits,* also known as *minimum fill ratios,* dictate the maximum ratio of order cancellations to order executions. For example, a trader may be required to execute at least 1 order for every 10 canceled orders. At the ICE, the message throttle limits are determined on a case-bycase basis in consultation with each trader. Appropriate message throttle limits ensure that the limits detect algorithmic problems without impacting properly operating trading strategies.

## Maximum Quantity Limits

*Maximum quantity limits* help prevent human and algorithmic "fat finger" errors by enforcing the maximum order sizes and trading positions. Maximum quantities are often determined in consultation with algorithm designers, in order to take into account optimal operation of the trading system.

## Real-Time Position Validation

At present, futures markets are uniquely positioned to withstand blow-ups of clients' trading systems, like the one incurred by Knight Capital. The secret to stable futures markets is the continuous real-time check of position market values vis-à-vis credit worthiness of trading account. When the market value in a given account exceeds the critical margin limit, the client's trading algorithm is prohibited from entering into new positions. In extreme situations, some of the account holdings may be liquidated to satisfy margin requirements. In most equity markets, similar checks are performed only at the end of each trading day.

## Price Reasonability

Under *price reasonability,* exchanges allow orders only at price levels within a predetermined range away from the market price. On most U.S. exchanges, traders may not place limit orders higher or lower than 10 percent away from the prevailing market price. The rule was instituted after the flash crash to prevent market orders in crisis from executing at unreasonably low prices, known as *stub quotes.*

Overall, many existing exchange measures are robust in catching errant algorithms. Wider proliferation of measures, as well as additional near-term measures, described next, will ensure that the markets identify and deter errant algorithms before problems occur.

### Near-Term Surveillance Measures

Both regulators and exchanges are seeking to further improve market surveillance and stability with the following measures, expected to be rolled out in the near future:

- Kill switches
- Legal entity identifiers

#### Kill Switches

Kill switches are designed to automatically block and unblock order entry at the following levels:

- Execution firm
- Account
- Asset class
- Side of market
- Product
- Exchange

At the execution firm's level, a kill switch allows termination of all flow from a broker-dealer whose algorithms are determined to be corrupt. In the Knight Capital case, an execution-firm-level kill switch would have stopped all Knight's trading upon detection of irregularities. An account-level kill switch disables trading by a specific account, while the asset-class kill switch disallows trading in a specific type of financial instrument, for instance, options, potentially allowing trading in other markets. The side-ofmarket kill switch turns off buying or selling capability. The product kill switch bars trading in one particular financial instrument, while the exchange kill switch takes away ability to trade on a given execution venue.

Kill switches may be operated by exchanges following some specific risk guidelines. In addition, API-based kill switches may be programmed directly into a client's algorithm, shutting down trading ability whenever the algorithm's particular risk tolerance conditions are exceeded. Various risktolerance metrics are described in Chapter 14.

#### Legal Entity Identifiers

Real-time regulatory surveillance at the exchange level is further likely to be aided by one of the key new regulatory initiatives: legal entity identifiers (LEIs). An LEI is a unique identifier assigned to all market participants:

- Financial intermediaries
- Banks
- Finance companies
- All listed companies
- Hedge funds
- Proprietary trading organizations
- Pension funds
- Mutual funds
- Private equity funds

#### Other entities

There are expected to be no thresholds (capitalization or other) required to obtain an LEI. Such configuration will extend the LEI-based surveillance to all trading entities, except for natural persons.

Presently proposed LEIs are composed of 20 alphanumeric characters, with special sequencing of digits that can be validated using a check character system. Each LEI will be associated with the official name of the legal entity or with the fund manager for pooled investments, the address of the headquarters, the country of incorporation, the date of the first LEI assignment, the date of last update of LEI information, and the date of expiry, if any.

The LEI system will be administered by the International Organization for Standardization (ISO). The ISO will take on validation of LEI applications, assignment of LEIs, maintenance of LEI registry, as well as the annual review of LEI records. The LEI system is expected to operate on an international level; in addition to the U.S. regulators, authorities in Canada, Hong Kong, and Australia have already expressed intention to apply the LEI system in their respective jurisdictions.

The LEIs are expected to phase in by asset class, beginning with over-thecounter (OTC) derivatives, like credit default swaps, and later extending to all asset classes. The U.S. CFTC already requires the use of LEIs for all dealers executing OTC derivative transactions.

### Investor Protection

Investor protection is one of the explicit goals of several regulators, like the U.S. SEC. The SEC and most other regulators seek to safeguard traders and investors by minimizing the following activities in the markets:

- Market manipulation
- Front-running
- Market crashes

This section considers each of these issues.

### Detecting Intentional Market Manipulation

Whole classes of strategies attributed to high-frequency market distortions often prove ill thought through, as discussed in Chapter 12. Having said that, HFT market manipulation is as feasible in principle as is the screening and detection of such manipulation.

From the regulatory perspective, establishing credible market manipulation requires two principles:

1. The activity should be recurrent.

2. The activity was performed with the intent of manipulating markets.

In other words, to credibly detect market-manipulating activity, regulators need to establish a pattern of intentional market manipulation. To do so, after observing an instance of potentially harmful activity, regulators need to consider previous and subsequent market activity by the same entity and detect a sequence of actions along the same trajectory.

Manipulation can be detected following the blueprints discussed in Chapter 12. As shown in the previous section on stability of systems, the extent of market manipulation can be measured by the symmetry of a market impact following buy-and-sell market orders of equal size. Investors and regulators alike can successfully monitor markets for high-frequency manipulation by screening markets in real-time for asymmetric market impact. Account-level trading in asymmetric markets can next be examined for high-frequency manipulation.

### Front-Running

Naturally, unscrupulous brokers possessing order-flow data may choose to front-run their own clients whenever they detect a large impending price move. The regulation has tried to deal with this problem. Under the Volcker rule, for example, banks were forced to dispose of their proprietary trading operations, with the intent of minimizing incentives for using client orderflow information, to ensure stability of the banking sector. In some banks, however, the proprietary trading operations of high-frequency nature were not shut down. Instead, the HFT was moved directly into the execution area with a new moniker of *prehedging* function, where the same HFT strategies are now executed with clients' money on the banks' behalf. The Dodd-Frank rule further complicates the problem by proposing to exempt brokers from their obligation to execute in customer interests first, essentially creating a

front-running bonanza at any broker-dealer's execution desk. To prevent front-running, clients can take matters into their own hands and diversify brokers, effectively limiting the information each broker has about the client's order flow. Small traders are at a disadvantage, however, as few have enough capital to establish positions with various brokers.

The Australian regulators have placed the goal of market integrity above all other issues. One of the key initiatives on the table of the Australian regulators is the requirement for pretrade transparency, designed to stem front-running. The Australian Securities and Investment Commission (ASIC) has specifically concerned itself with detecting shifts in liquidity in response to orders, moving market prices before traders obtained execution but after they placed their orders.

### Predicting Market Crashes

Following the flash crash of May 6, 2010, a considerable body of research focused on advanced prediction of such events going forward. Two main streams of crash predictability have emerged:

- 1. Based on asymmetry of liquidity in the limit order books.
- 2. Based on abnormal trading patterns.

Crash Prediction Based on Asymmetry of Liquidity in the Limit Order Books

The first stream of research first developed by Easley, Lopez de Prado, and O'Hara (2011) takes root in the observation that the May 6, 2010, crash was a direct result of asymmetric liquidity in the markets: the limit orders on the bid side of E-minis, for example, were "eaten up" by incoming market sell orders a few hours before the market activity precipitated into a full-blown crash.

To estimate the incidence of a crash, the authors develop a volume-based probability of informed trading, or VPIN metric:

$$(1)^{VPIN} \approx \frac{\sum_{\tau=1}^{n} \left| V_{\tau}^{S} - V_{\tau}^{B} \right|}{nV}$$

where and are volumes initiated by sell and buy market orders, respectively, computed within each volume-based clock unit. Easley, Lopez

de Prado, and O'Hara (2011) consider volume clocks where each "time" unit corresponds to 50 E-mini contracts: within each volume-clock unit *τ*, then, contracts. The authors show that extreme asymmetry in trading volume as measured by VPIN is capable of predicting extreme crashes a few hours ahead of crash time. Tudor Investment Corporation has applied for a patent in *VPIN*, and may require fees for utilization of the methodology.

#### Crash Prediction Based on Abnormal Trading Patterns

A separate stream of literature considers "normal" patterns in trading and uses deviations from those normalities as the predictors of crashes. Normal market movements are calibrated to fit the Mandelbrot-like growth parameter, known as the *Hurst exponent.* A Hurst exponent of returns of 0.5 describes the market where the returns evolve in a completely random manner. A lower Hurst coefficient indicates a mean-reverting market, while a higher Hurst value points to a trending market. Florescu et al. (2012) shows that in most normal real-life markets, the Hurst exponent value has been shown to be about 0.6. A heightened value of Hurst exponent is likely to precede a crash. For example, Florescu et al. (2012) shows that ahead of financial services mini-crash of March 2008, Hurst exponent values in financial services stocks reached 0.85. Aldridge 2012f develops a separate crash-predicting methodology that can be shown to identify onset of market crashes hours and sometimes days ahead of the events.

### Efficient Trade Matching

Regulators are actively encouraging internalization, seeking to minimize the situations where broker-dealers execute trades against their own orders. Such incidents are known as *wash trades.* An example of a wash trade may consist of a broker-dealer's placing an order for one customer at the best bid of the exchange, only to match it with a market sell order for another customer. Wash trades have been deemed feasible for money laundering and are closely monitored and discouraged.

## Market Structure

Regulatory dimensions surrounding market structure presently span two main areas: new markets, such as swap execution facilities, and "lit" versus "dark" pools. This section briefly considers the issues on the table.

## Swap Execution Facilities

Following the Dodd-Frank regulation, swaps are a new asset class to be traded electronically in the United States The newly established computerized swap trading falls under the jurisdiction of the CFTC, and will trade in specialized swap-execution facilities (SEFs) that will have a new market structure, are bound to attract high-frequency traders due to their electronic nature, and will require new regulatory rules.

### "Lit" and "Dark" Pools

Regulation Alternative Trading Systems (Reg ATS) introduced by the SEC in 1998 streamlined definitions and applicability of lit and dark pools. The term *pool* refers to a trading venue attracting or "pooling" trading capital for matching less formal than a regulator-supervised exchange. The terms *lit pool* and, more often, *lit market* usually refer to a traditional exchange-like trading venue, where the limit order book is observable by all engaged market participants. While the transparency of the lit order book may induce confidence in some investors, it may disadvantage others, particularly those desiring to trade large volumes and seeking to avoid order-related market impact and other information leakage. As discussed in Chapter 11, lit order books contain information about impending directions of the market price and order flow, items many market participants prefer to retain in secret.

Dark pools are largely unregulated trading venues that do not disclose their limit order books. By keeping their order books "in the dark," dark pools create advantages to large investors and market makers. Large investors are enticed by limited information signaling associated with their orders. The orders are revealed only when executed—trade prints are disseminated to all participants of a given market.

Large investors are not the only group benefiting from dark pools. Market makers also tend to earn more in dark pools than in lit markets. According to the research of Boulatov and George (2011), for instance, market makers are able to hide informational revisions to their quotes, discussed in Chapter 11, trading longer on their information. Examples of dark pools include Citigroup's Automated Trading Desk (ATD) and Liquidnet's offerings.

Even though dark pools tend to offer higher profitability to market participants than do lit venues, an equilibrium controls proportion of market makers engaged in dark pools versus lit trading operations. Once the majority of market makers' moves to the dark pools, lit venues become less competitive and market makers in these lit venues earn higher rents. When the value of the market makers' rents in the lit markets exceeds the informational advantages in the dark markets, more market-makers moves from dark to lit venues, until an equilibrium is reached. [Figure 13.3](#page-20-0) illustrates the mechanism by which the equilibrium between the dark and lit markets is achieved.

<span id="page-20-0"></span>![](_page_20_Figure_2.jpeg)

<span id="page-20-1"></span>![](_page_20_Figure_3.jpeg)

Canadian regulators have singled out dark pools as trading venues suitable only to large investors trading amounts greater than a cut-off "Dark Order Size Threshold." In the United States, the NYSE went the opposite direction and created a segregated dark pool for small investors, the success of which is yet to be determined.

## Summary

Regulators worldwide are proactively tackling issues relating to HFT. New ideas have emerged to monitor markets in real time and screen for issues such as market manipulation and market crashes. Expanding monitoring activity at the exchange level will likely deliver most substantial improvements of current enforcement; the legal entity identifier initiative is bound to be helpful in the process.

# End-of-Chapter Questions

1. What are the latest key regulatory developments in the United States? In the United Kingdom? In Canada? In Australia?

2. What kind of HFT protection mechanisms are already deployed in selected U.S. markets?

3. What is the interval price limit? How does it work?

4. What is the message throttle limit? How is it determined?

5. What is a legal entity identifier?

<sup>1</sup> At the time this book was finalized, the U.S. Senate Committee on Banking was weighing in on disallowing co-location altogether, with the idea that co-location offers unfair data advantage to technologically savvy market participants. The Senate hearings tend to focus only on the negative aspects of co-location and ignore most positives. As detailed in Chapter 2, however, co-location provides an enormous benefit to all market participants: security of trading communications. In co-located operations, the trader's machine has a dedicated private line to the exchange's computer. Most of the trading traffic in today's markets is sent

in plain text; sending it over co-located networks ensures secrecy of communications. Without co-location, one can imagine an outright attack on financial markets: a computer bandit may intercept trading communication, redirecting funds to his personal accounts and outright annihilating trading venues, broker-dealers, and traders in the process. A ban on co-location, therefore, would create a tremendous gap in market security and stability of financial systems worldwide.

<sup>2</sup> The SEC does not obtain tick data and is commonly cited as lacking funds to do so. Part of the reason behind the SEC's reluctance to build the data capability is the agency's implicit agreement with FINRA. At present, FINRA detects potential instances of market manipulation and forwards them to the SEC. The SEC on average prosecutes every eighth case forwarded by FINRA.
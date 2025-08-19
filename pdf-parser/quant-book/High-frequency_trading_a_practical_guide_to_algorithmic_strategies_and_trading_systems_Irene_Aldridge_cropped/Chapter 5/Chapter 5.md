# Trading Costs

rading costs can make or break the profitability of a high-frequency trading strategy. Transaction costs that may be negligible for long-term strategies are amplified dramatically in a high-frequency setting.

This chapter focuses on the transparent and implicit costs that impact high-frequency trading.

#### Overview of Execution Costs

According to classical finance, markets are seamless, that is, they possess the following characteristics:

- Markets are uniform in their structure.
- Markets are consolidated; a price of a specific financial instrument is instantaneously updated wherever the instrument is traded.
- Prices immediately reflect all fundamental information.
- No transaction costs exist.
- Orders of all sizes can be executed instantaneously—markets are infinitely liquid, with each price queue in the limit order book containing infinite number of limit orders.
- Traders have unlimited borrowing power.
- No short-sale constraints exist.
- Market price is invariant to order size.

In real life, securities markets have frictions: prices incorporate information over time, markets differ in their structure and depth, markets can be highly fragmented, and issues like transaction costs further distort markets away from their textbookperfect models. Costs known prior to trading activity are referred to as *transparent* or *explicit,* and costs that have to be estimated are known as *latent* or *implicit.* Likewise, the transparent costs are known with certainty prior to trading, and implicit costs are not known before trading takes place, yet implicit costs can be estimated from the costs' historical distribution inferred from the data of past trades.

## ■ **Transparent Execution Costs**

Transparent execution costs are generally known ahead of trading; they comprise broker commissions, exchange fees, and taxes. This section considers each of the transparent costs in detail.

# **Broker Commissions**

Brokers charge commissions for

- Providing connectivity to exchanges, dark pools, and other trading venues.
- Facilitating "best execution" of client orders: executing client orders according to client specifications.
- Serving as the opposite side, or counterparty, to clients' orders in over-the-counter (OTC) arrangements.
- Providing custody of assets.
- Clearing trades from their execution to settlement and reporting trading activity.
- Delivering leverage and margin to clients.
- Other custom services.

Some broker-dealers may charge their customers additional fees for access to streaming market data and other premium information, such as proprietary research. Paid-for broker research is becoming increasingly obsolete as customers compete by retaining secrecy of their investment strategies. And while best execution presently accounts for a significant percentage of revenues for many brokers, clients with understanding of high-frequency data often choose to move away from brokers' best execution models, preferring to build their proprietary execution engines in-house instead. The latest best execution models are discussed in Chapters 15 of this book.

Broker fees can be fixed per order or month, or variable per trade size, trade value, or monthly volume. Broker commissions may also depend on the total business the broker receives from a given firm, various trade "bundling" options, and the extent of "soft-dollar," or implicit, transactions that the broker provides in addition to direct execution services. Broker commissions are negotiated well in advance of execution. The differences in cost estimates from one executing broker to another can be significant and are worth understanding to ensure favorable pricing.

Figure 5.1 shows the broker costs for metals trading offered by Interactive Brokers.

![](_page_2_Figure_0.jpeg)

**FIGURE 5.1** Broker Commissions on Metal Trading Off ered by Interactive Brokers *Source:* Interactive Brokers web site

# **exchange Fees**

Exchanges match orders from diff erent broker-dealers or electronic communication networks (ECNs) and charge fees for their services. The core product of every exchange is the liquidity, or presence of open buy-and-sell interest, that traders are looking to transact on the exchange.

Liquidity is created by open limit orders; limit buy orders placed at prices below the current ask provide liquidity, as do limit sell orders placed at prices above the current bid. Market orders, on the other hand, are matched immediately with the best limit orders available on the exchange, consuming liquidity. Limit orders can also consume liquidity; a limit buy placed at or above the market ask price will be matched immediately with the best available limit sell, thus removing the sell order from the exchange. similarly, a limit sell placed at or below the market bid price will be immediately matched with the best available bid, as a market sell would.

To attract liquidity, exchanges may charge fees or pay rebates for orders consuming liquidity or for orders supplying liquidity. As discussed in Chapter 3, exchanges that charge for liquidity-removing orders and pay for liquidity-supplying orders are known as *normal* exchanges. Exchanges that pay for orders that remove liquidity and charge for orders that supply liquidity are called *inverted.* At the time this book was written, most U.s. equity exchanges deployed rebates in either normal or inverted models. selected exchange ECNs in other countries now also off er rebate-based programs.

Exchange fees and fees of other trading venues can also vary by order type. Complicated orders, such as hidden-size orders like iceberg orders, or algo-enabled orders, like volume-weighted average price (VWAP) orders, carry associated cost premium.

Like broker commissions, exchange fees are negotiated in advance of execution.

# **taxes**

According to Benjamin Franklin, "in this world nothing can be said to be certain, except death and taxes." Taxes are charged from the net profi ts of the trading operation by the appropriate jurisdiction in which the operation is domiciled. High-frequency trading generates short-term profi ts that are usually subject to the full tax rate, unlike investments of one year or more, which fall under the reduced-tax capital gains umbrella in most jurisdictions. A local certified or chartered accountant should be able to provide a wealth of knowledge pertaining to proper taxation rates. Appropriate tax rates can be determined in advance of trading activity.

Proposals to tax individual trading transactions surface and fade over time, with most jurisdictions deciding against transaction taxes in the long run. Aldridge (2012b) estimates that a 0.05 percent tax imposed on every transaction of IBM stock, for example, is likely to wipe out as much as one third of trading volumes, ultimately resulting in severe contractions of economic growth.

## ■ **Implicit Execution Costs**

At the tick level of data, transparent costs are being increasingly dominated by implicit costs of the opportunity cost of investment, the bid-ask spread, latency or slippage, and related market impact. Additional implicit costs tracked by researchers and traders include the costs of price appreciation and market timing.

# **Bid-Ask Spreads**

Bid-ask spreads are not known in advance. Instead, they are stochastic or random variables that are best characterized by the shape of the distribution of their historical values.

The bid-ask spread is the difference between the best ask and the best bid at any given point in time, and represents the cost of instantaneous liquidation of a trading position. The spread can also be seen as the premium paid by traders desiring immediate execution via market orders. On the flip side of the argument, the spread is the compensation paid to the patient traders providing liquidity through limit orders. The limit order traders take considerable risk of entering a losing position in the markets, the risk that increases with market volatility. As a result, limit traders' compensation also has to rise in times of higher uncertainty, a fact reflected in variability of the bid-ask spread in relation to volatility. Bid-ask spreads are discussed in detail in Chapter 4.

# **Slippage or Latency Costs**

Latency cost, commonly known as *slippage,* is the adverse change in the market price of the traded security that occurs from the time an investment decision is made until the time the trade is executed. Slippage often accompanies market orders and refers to the difference between the best quote observed by the trader immediately prior to placing the order and the realized market price. The following example illustrates the concept of the latency cost or slippage. The trading strategy identifies a stock (e.g., IBM) to be a buy at \$56.50, but by the time the market buy order is executed, the market price moves up to \$58.00. In this case, the \$1.50 differential between the desired price and the price obtained on execution is the cost of latency.

In the media, slippage is often portrayed as the evidence of the great divide between the haves and have-nots of the technological arms race. In reality, slippage is not solely dependent on the speed of trading activity. Instead, slippage is also a direct function of the a) liquidity available in the market and b) the number of market orders that have arrived to consume that liquidity. When many market participants simultaneously place market orders, the orders erode the fi nite liquidity and move the market price at high speeds in the process, as Figure 5.2 illustrates. As a result, slippage is typically larger during periods of high trading activity, for example, at market open

![](_page_4_Figure_1.jpeg)

**FIGURE 5.2** slippage Illustration

and market close times, as well as times immediately following major macroeconomic announcements. The activity of other market participants can be forecasted in a probabilistic framework in the context of market impact, discussed next.

Still, latency due to technology alone can have a substantial impact on traders' performance. Stoikov and Rolf (2012), for example, find that ultra-fast trading infrastructure delivers significant profitability under certain forecasting assumptions. Specifically, Stoikov and Rolf (2012) define cost of latency as the expected value of dollar-denominated savings resulting from executing with slow and fast (lowlatency) infrastructures:

$$COL = \mathbb{E} \left[ S_{t+1} - S_t \right] \tag{1}$$

where S*<sup>t</sup>*+*<sup>l</sup>* is the price obtained at time *t* with latency *l* and S*<sup>t</sup>* is the price obtained on the same financial instrument at the same time *t* when latency *l* approaches zero. The authors observe that the cost of 10 milliseconds of communication delay is about twice that of an algorithm configured to run on only 1 millisecond of latency. In turn, 100 milliseconds of latency result in threefold latency cost as compared to that of an algo using 1 millisecond execution latency. An algorithm using infrastructure with a delay of 1 minute incurs an associated cost of four times greater than the algorithm with just 1 millisecond latency.

The shortcomings of technology resulting in latency costs may or may not reside in the trader's domain. Specifically, latency can occur in any of the following nodes of order routing:

- 1. *Trader's systems.* Slow systems and network architecture cause delays in processing and interpreting quotes.
- 2. *Networks.* Congestion and interruptions in network communications may disrupt timely execution and can delay transmission of orders. In addition, geographic differences between the location of the trader's servers and the location of the execution venue can cause latency by virtue of physical communication delays. Distances increase the time each quote or trade has to travel to their destinations, increasing trading latency. Latencies between major financial centers of the world are reported in Chapter 2. Co-location and private network connections with trading venue servers may help alleviate these issues.
- 3. *Broker-dealers.* Delays in broker-dealer routing engines prompted innovations of direct market access.
- 4. *Execution venues.* Execution venues may experience overloads of simultaneous orders resulting in an order-processing backlog and subsequent delay in execution. Such situations most often occur in high-volatility environments.

While latency costs are random and cannot be known with precision in advance of a trade, distribution of latency costs inferred from past trades can produce the expected cost value to be used within the trading strategy development process. Fast infrastructure, backup communication systems, and continuous human supervision of trading activity can detect network problems and route orders to their destinations along alternative backup channels, ensuring a continuous transmission of trading information.

# **Price Appreciation and Timing Risk Costs**

Both price appreciation and timing risk costs describe market risk incurred during execution of a large position broken down into a series of child orders (see Chapter 15 for a discussion of child orders).

The price appreciation cost refers to the forecasted loss of investment value during the execution of a large position. The timing cost refers to random, unforecasted price movement ahead of execution of a child order.

The following EUR/USD trade illustrates the concept of a price appreciation cost. A trading strategy determines that EUR/USD is undervalued at 1.3560, and a buy order of \$100 million EUR/USD is placed that must be executed over the next three minutes. The forecast turns out to be correct, and EUR/USD appreciates to 1.3660 over the following two minutes. The price appreciation cost is therefore 50 bps per minute. The price appreciation cost is due to the fundamental appreciation of price, not the trading activity in EUR/USD.

The cost of timing risk describes by how much, on average, the price of the traded security can randomly appreciate or depreciate within 1 second, 10 seconds, 1 minute, and so on from the time an investment decision is made until the market order is executed. The timing risk cost applies to active market timing activity, usually executed using market orders. The timing risk cost does not apply to limit orders, where the execution price is fixed.

# **Opportunity Costs**

The opportunity cost is the cost associated with inability to complete an order. Most often, opportunity cost accompanies limit order–based strategies, when the market price does not cross the specified limit price. However, market orders can also fail to execute, for example, when the market does not have the liquidity sufficient to fulfill the order. On a U.S. equity exchange, a market order may fail to execute when the exchange does not have the limit orders posted at the National Best Bid and Offer (NBBO), as discussed in Chapter 3. The opportunity cost is measured as the profit expected to be generated had the order been executed.

# **Market Impact Costs**

Market impact cost measures the adverse change in the market price following an order. Market impact is rapidly becoming the dominant transaction cost. In equities, according to the ITG Global Trading Cost Review (2010), market impact consumed 0.387 percent of the total dollar amount traded. Per report, the total amount of trading costs averaged 0.476 percent of turnover, with only 0.089 percent of the dollar volume spent on commissions. These figures were comparable in the U.S., EU, U.K., and Japanese equity markets; higher transaction costs were reported in emerging markets. In futures, both market impact and transaction costs appear lower, yet market impact costs still dominate: according to Aldridge (2012c), market impact observed in Eurobund futures (FGBL) on Eurex is 0.020 percent of the dollar volume. Institutional transaction costs in the futures and forex markets tend to be in the \$5 to \$10 per every \$1 million volume traded, or 0.0005 to 0.0010 percent of executed dollar volume. This section considers the cause and estimation of market impact.

## ■ **Background and Definitions**

All trades and orders convey information. The mere fact that a trader is placing his own money or reputation on the line to bet on a particular direction of the market informs other market participants of the trader's belief.

The information contained in a trade observation is much more potent than that in an opinion of a news analyst. Analysts are typically compensated via a salary, often irrespective of whether their prognoses come true. At the same time, traders are usually compensated via a percentage of profits they derive from their trading, with each trade having direct implications on the trader's welfare. As a result, trades are viewed as potent signals about beliefs of impending market moves. The larger the order, the more credible the trading signal.

Both aggressive and passive orders (market orders and limit orders) are credible signals—market orders are commitments to buy or sell a security immediately at the best market price, and limit orders are commitments to buy or sell at a predefined price when the opposite market trade is available. As such, both market orders and limit orders emit market impact. Unlike market orders, however, limit orders can be canceled. As a result, limit orders make less credible signals than market orders, and the intensity and even the direction of market and limit orders may differ.

The idea of an order as a credible signal was first published in 1971. The thought of signaling in the markets was so revolutionary at the time that the author of the research dared to publish the theory only under an assumed name, Bagehot, after a famous English nineteenth-century journalist covering topics in economics.

The mere existence of market impact runs against core principles of classical finance. In the idealized financial world, under the concept of market efficiency, considered to be the optimal steady state in most classical asset pricing models, the following conditions are assumed to hold:

- Everyone simultaneously receives the same information.
- Everyone interprets information in identical way.
- Only the fundamental information, such as earnings announcements or interest rates, affects security prices. Past price trends and other nonfundamental information has no relevance to security prices.
- All the relevant information is impounded into prices immediately upon information arrival, resulting in a sharp step function of security prices moving from one fundamental level to the next. Trades themselves carry no information, as all the information is already contained in prices. Figure 5.3 illustrates the perfect markets' response to an arrival of positive fundamental news, as well as to periods without any news arrivals.

![](_page_8_Figure_0.jpeg)

**FIGURE 5.3** Classical Finance View on How Perfect Markets Incorporate Fundamental Information

In reality, traders interpret news differently, a result of divergent investment horizons, education, effort and experiences. On the subject of the impending price movement, opinions of long-term investors are likely to differ from those of short-term investors (see Hasbrouck, 1991, for example), a fact that has allowed both short-term and long-term investors to coexist without eating each other's proverbial lunch. similarly, investors deploying technical market analysis disagree with quants and fundamental analysts. Traders poring over the information 15 hours a day are also likely to have an opinion different from a casual investor briefly analyzing his mutual fund statements only quarterly. Finally, a seasoned professional may have a point of view divergent from that of a newbie. All of these factors contribute to the markets' deviation from idealized conditions, and make trades and even orders able to carry information to other market participants.

In addition, most information is impounded into prices gradually, as fi rst noted by Kyle (1985), and not instantaneously, as the study of classical fi nance would prefer. Every trade is a result of a buy order meeting a sell order. Often, a trade is a product of one market order meeting an opposing limit order, although two price-meeting limit orders of opposite direction may also be matched to form a trade. A trade is a product of opposing forces: supply and demand, and, in theory, each trade does not move the markets much. In the short-term reality, however, the opposite holds:

■ Market buy orders are on average followed by a rise in prices of the traded securities, while market sell orders on average result in lower prices.

■ Limit buy-and-sell orders also generate a market impact in anticipation of a future trade (see Harris, 1997; Parlour and seppi, 2007; Boulatov and george, 2008; and rosu, 2010). As a result, limit orders have also been shown to be followed by a persistent price change (see Eisler, Bouchaud, and Kockelkoren, 2009; and Hautsch and Huang, 2011). While a completed trade is an irreversible and most credible signal, limit orders are cancelable indications of trading interest, and, as a result, are smaller in magnitude than that for market orders. Hautsch and Huang (2011) and Aldridge (2012c) estimate the market impact of a limit order to be about 25 percent of that of a similar market order. The direction of the price change following a limit order may be reversed relative to that of a comparable market order, depending on how far is the limit order price away from the market price.

Figure 5.4 illustrates gradual adjustment of prices in response to positive news and no news observed in actual trading conditions. When positive news arrives, the market price tends to overshoot its fundamental level, with the overshoot component gradually settling or decaying to its fundamental level.

Information leakage accompanying orders and trades is hardly new: for years, broker-dealers and other market participants with access to tick-level data competed on being able to "read the ticker tape" and infer short-term price forecasts from that. By continuously watching the ticker tape, manual market makers would learn the information content of trades and adjust their quotes according to their short-term predictions—in the process resembling a manual variant of today's high-frequency trading. As markets become increasingly computerized, however, the ticker tape is moving increasingly fast, and it is now literally impossible for a human eye to parse ticker-tape information in real time.

![](_page_9_Figure_3.jpeg)

**FIGURE 5.4** Price reaction to Trades Observed in real Life

This phenomenon of real-life price changes following news and orders is known as *market impact* (MI). MI can be attributed to several factors including:

- In the trading world with heterogeneous traders possessing diff erent beliefs and information, MI is the negotiation or tâtonnement process via which traders' information and beliefs are impounded into the security prices.
- Both market and limit orders represent traders' commitments of money and reputation, and therefore form credible signals to other market participants who may choose to trade in the same direction.
- Every market buy (sell) order temporarily depletes liquidity supply on the ask (bid) side of the order book, driving the next market buy (sell) order to be matched against a higher (lower) best available limit order price.

## ■ **Estimation of Market Impact**

The metric of MI answers the question, "How much would the trader move the price if he were to make the trade?" Figure 5.5 illustrates the MI determination for a single order. The impact of the order incoming to the exchange at time *t\**, for example, can be measured as the price change observed after time *t\** relative to the last trade price recorded before *t\**, as illustrated in Figure 5.5. The selected postorder reference trade time *t* can be measured in clock time, trade time, tick time, or volume time. In clock time, time *t* is selected as *x* time units, say 10 seconds, post order arrival time *t\**. In trade time, the MI is measured *y* number of trades following the order observed at *t\**. In tick time, the impact is computed *z* ticks, quote revisions or trades, past the order. Finally, in volume time, the impact is measured when the aggregate trade volume following the order of interest reaches at least *V* trading units (e.g., shares or contracts). Tick-time and trade-time MI is computationally easier to estimate than clock-time or volume-time impact.

While the exact impact following a future trade can never be known in advance of the trade, the *expected* MI can be estimated using historical data and trade-specifi c characteristics. The logic for estimating expectation of MI is similar to the logic used to forecast price levels: while the exact future price can never be pinpointed with full precision,

![](_page_10_Figure_7.jpeg)

**FIGURE 5.5** Estimation of Market Impact for an Order Arriving at an Exchange at Time *t\**

an expectation of the future price can be formed based on some auxiliary metrics. The expected MI can be measured in an event-study framework using recent historical data.

MI can turn a profitable strategy into a losing one. A strategy that relies on repeating trades, for example, may be distorted by MI, with sequential trades obtaining much worse prices than expected.

As noted earlier, MI is a function of order size: the larger the trade, the more credible the information conveyed by the trade, the higher the impact the trade generates. The exact evolution or functional form of MI is important: a trader can increase the size of his investment while remaining profitable when the MI grows slowly with trade size (see Farmer, Gerig, Lillo, and Waelbroeck, 2009). Glosten (1987) and Easley and O'Hara (1987) were the first to note that MI can be broken down into two distinct functional parts: permanent and temporary MI. Permanent MI impounds fundamental information into prices in a manner consistent with the classical financial theory and the efficient market hypothesis (see Fama, 1970). Temporary MI is the noise component that first overshoots the fundamental price level and then decays with time until the fundamental price level is reached.

The precise shapes of permanent and temporary MI functions have been subjects of competing theories. Breen, Hodrick and Korajczyk (2002) and Kissell and Glantz (2002), for example, suggested that MI is a linear function of the order size ( $MI_r \propto$  $V_{t*}$ ).Lillo, Farmer, and Mangegna (2003), however, detected a power law specification ( $MI_{r} \propto (V_{r*})^{\beta}$ ). The latest research on the topic (see Huberman and Stanzl, 2004; and Gatheral, 2009), however, reconciles the linear and power-law specifications by finding an order-size-based linear relationship for the permanent MI and time-based power-law decay for temporary impact, as shown in Figure 5.6.

For market orders, the MI appears strongly concave in the order size, and the signs of market orders are autocorrelated in time: market buy orders tend to follow other market buy orders, and vice versa. A model unifying the preceding facts expresses the MI function as follows (Eisler, Bouchaud, and Kockelkoren, 2009):

$$P_{t} = \sum_{t^{*} < t} [G(t, t^{*}) \epsilon t^{*} (v_{t^{*}})^{\theta} + n_{t^{*}}] + p_{\infty}$$
 (2)

![](_page_11_Figure_6.jpeg)

FIGURE 5.6 Functional Form of Market Impact: Permanent and Temporary Components

where:

 $v_{t^*}$  is the volume of the trade at time  $t^*$ 

 $\epsilon_{t^*}$  is the sign of the trade at time  $t^*$ 

 $n_{\cdot}$  is the independent noise term that models any price change not induced by news

 $G(t, t^*)$  is the propagator function, which describes, on average, how prices respond to a single trade over time;  $G(t, t^*)$  decays with time

The MI of an individual order recorded at time  $t^*$  is then

$$MI_{t^*} = G(t, t^*) \epsilon_{t^*} (v_{t^*})^{\theta} + n_{t^*}$$
(3)

The MI propagator function  $G(t, t^*)$  has to decay with time, and in a specific way, to satisfy the high autocorrelation of direction of subsequent trades. If  $G$  did not decay, price returns would be proportional to the signs of the trades and returns would be highly autocorrelated in time. According to Eisler, Bouchaud and Kockelkoren  $(2009)$ , G decays as follows:

$$G(t,t^*) \sim |t-t^*|^{-\beta} \tag{4}$$

where  $\equiv \frac{1-\gamma}{2}$ , and  $\gamma < 1$  is the decay parameter in the correlation of subsequent trade signs:

$$C(l) = (\epsilon_{t}\epsilon_{t+1}) \sim (l)^{-\gamma} \tag{5}$$

 $G(t, t^*)$  further has the following boundary properties:

$$G\left(t \to t^*\right) = \frac{\partial p_t}{\partial \xi_t} \tag{6}$$

where  $\xi_t = \epsilon_{t} v_t^{\theta} \sim N(0, \sigma)$  is normally distributed with mean zero and standard deviation  $\sigma$ .

In addition to trade size and time, however, MI has been empirically shown to depend on other variables. In equities, MI has been shown to depend on:

- Intertrade durations (see Dufour and Engle, 2000)
- Stock-specific characteristics, such as industry and earnings of the issuing company (see Breen, Hodrick, and Korajchyk, 2002; Lillo, Farmer, and Mantegna, 2003; and Almgren, Thum, Hauptmann, and Li, 2005)
- Volatility and spread (Ferraris, 2008)

In futures, MI has been found to vary with:

- Liquidity (see Burgardt, Hanweck, and Lei, 2006)
- Intertrade durations and volatility (see Aldridge, 2012c)

The size and the direction of MI of a limit order has been found to depend on the size of the order as well as on the order's proximity to the best quote on the opposing side of the market. For buy limit orders placed on Nasdaq within the spread (see Hautsch and Huang, 2011, for details), orders than went on to be matched with the best ask experienced a positive MI, just as market buy orders would. Buy limit orders placed within the spread that became the best bid quotes on average experienced a negative MI of the size comparable to that of the orders matched with the best ask. The MI of a limit buy order that was posted inside the spread and became the best bid, however, varied with the size of the order:

- small-sized buy limit orders, with a size matching the depth at the bid, placed inside the spread that became best bids were on average followed by *negative* MI.
- Midsized (seven times larger than depth at the bid) were followed by a small *positive* MI, about 20 percent of the absolute MI experienced by small orders.
- Large orders (15 times larger than depth at the bid) were followed by a medium *positive* MI, about 50 percent of the absolute MI experienced by small orders.

Figure 5.7 summarizes the fi ndings.

## ■ **Empirical Estimation of Permanent Market Impact**

# **Data preparation**

MI can be estimated using both Level I and Level II tick data, as well as data containing trade stamps only. Level II data allow one to precisely pinpoint arrivals of limit and market orders: an increase in the aggregate size at a specifi c price level on the bid size indicates an arrival of a limit buy order. A decrease in the top-of-the-book liquidity on the bid side indicates an arrival of a market sell order.

![](_page_13_Figure_8.jpeg)

**FIGURE 5.7** Market Impact of Limit Orders Observed on Nasdaq *Source:* Hautsch and Huang (2011)

When using Level I or trade data, however, one comes across the challenge of separating buyer- and seller-initiated orders and trades. Over the years, researchers have developed several methodologies to separate buys and sells: tick, quote, Lee-Ready, and bulk volume classification, discussed in detail in Chapter 4.

### **Basic Estimation Model**

Data points separated into buys and sells are ready for estimation of permanent MI. Under the assumption of linear functional form, the permanent MI can be estimated using a linear regression with the following specification:

$$\Delta P_{t,\tau} = \alpha_{\tau} + \beta_{\tau} V_t + \beta_{\tau-1} V_{t+1} + \ldots + \beta_1 V_{t+\tau-1} + \varepsilon_{t,\tau}$$
(7)

where t is the time of the trade,  $\tau$  is the number of posttrade ticks or time units in the event window at which the trade impact is measured,  $V_t$  is the size of the trade observed at time *t*, and  $\Delta P_{t,\tau}$  is the normalized price change from time *t* to time  $\tau$ and can be expressed as shown in equation  $(8)$ :

$$\Delta P_{t,\tau} = \ln(P_{\tau}) - \ln(P_{t}) \tag{8}$$

Figures 5.8 and 5.9 show  $\widehat{\alpha}_s$  and  $\widehat{\beta}_5$  estimated five trade ticks following each trade on tick data of every trading day in 2009 and 2010 for Eurobund futures (FGBL), per Aldridge (2012c). As Figure 5.8 and 5.9 show, buyer-initiated trades

![](_page_14_Figure_7.jpeg)

**FIGURE 5.8** Daily Intercept  $\hat{\alpha}_s$  of Model (7) Estimated on Buyer-Initiated Trades in Eurobund Futures, 2009–2010

![](_page_15_Figure_0.jpeg)

**FIGURE 5.9** Daily Size Coefficient  $\hat{\beta}$  of Model (7) Estimated on Buyer-Initiated Trades in Eurobund Futures, 2009–2010

display the following properties. The 5-tick market impact of buy trades exhibits very strong positive dependency on trade size: the *t*-statistics of  $\beta_{5}$  often reach 10, as shown on the right axis of Figure 5.9, indicating that the dependency on trade size is 99.999 percent statistically significant. While the MI's dependency on trade size is highly persistent, the actual value of the coefficient estimate,  $\beta_{\scriptscriptstyle{5}}$  , is small: as the left axis shows,  $\hat{\beta}_5$  is on the order of  $10^{-7}$ , in other words, for every 100 contracts of Eurobund futures traded, the futures price directly attributable to the trading size on average rose by only 0.001 percent five ticks after each trade. The observed results are largely invariant from one day to the next, with clear exceptions at the end of each quarter when the statistical significance of the estimates appears to dip to zero, possibly due to regular rollovers of futures.

Figure 5.8 plots daily estimates of  $\hat{\alpha}_s$ , the average increase in FGBL price observed following buyer-initiated trades that cannot be attributed to trade sizes. As the  $\widehat{\alpha}_{\circ}$  value (left) axis in Figure 5.8 shows, the average size-independent component of price increase following buy trades is on the order of 10<sup>-5</sup>, or about 100 times larger than the price change attributable to trade size. As such, the size-independent market impact dominates size-dependent impact for trades under 100 Eurobund futures contracts, resulting in the following Eurobund-futures specific feature: FGBL trades of 1 or 100 contracts incur comparable market impact! Trades larger than 100 FGBL contracts, however, generate substantial size-dependent impact. The observed sizeindependent impact  $\widehat{\alpha}_{\circ}$  is highly statistically persistent, with accompanying *t*-ratios ranging from about 5 to 20, as the right axis of Figure 5.8 notes. Seller-initiated

![](_page_16_Figure_0.jpeg)

trades incur a similar scale of market impact, yet in the opposite direction, as Figures 5.10 and 5.11 show.

**FIGURE 5.10** Daily Intercept  $\hat{\alpha}_s$  of Model (7) Estimated on Seller-Initiated Trades in Eurobund Futures, 2009–2010

![](_page_16_Figure_3.jpeg)

**FIGURE 5.11** Daily Size Coefficient  $\widehat{\beta}$  of Model (7) Estimated on Seller-Initiated Trades in Eurobund Futures, 2009–2010

The statistical meaningfulness, or the explanatory power, of model in the equation (7) applied to buyer-initiated trades is quite low, however, as measured by the adjusted r-squared of the model and ranging from 1 to 2 percent, as Figure 5.12 illustrates. To put the 1 to 2 percent adjusted r-squared in perspective, though, one needs to consider the adjusted r-squared on predictive power of generalized autoregressive conditional heteroskedasticity (gArCH), a popular volatility estimation model used in many commercial applications. The r-squared of predictive power of gArCH usually hits only about 5 percent. In other words, while the r-squared of the model of equation (7) is quite low in principle, it is comparable to r-squared estimates of other popular models.

Additional Explanatory Variables The strong signifi cance of the intercept <sup>α</sup> 5 in the model of equation (7) invites questions about what kind of additional variables, if any, can help the unexplained variation captured by <sup>α</sup> <sup>5</sup> . Commercial models for estimation of market impact often deploy additional explanatory variables, such as the observed spread, short-term volatility, and intertrade durations. To analyze the potential impact of these variables, one can extend the model of equation (7) as follows:

$$\Delta P_{t,\tau} = \alpha_{\tau} + \beta_{V,\tau} V_t + \beta_{\sigma,\tau} \hat{\sigma}_t + \beta_{S,\tau} \hat{S}_t + \beta_{T,\tau} \hat{T}_t + \varepsilon_{t,\tau}$$
(9)

where:

■ As before, ∆*Pt*,τ represents the τ-tick change in price,

$$\Delta P_{t,\tau} = \ln(P_{\tau}) - \ln(P_{t-\tau}) \tag{10}$$

![](_page_17_Figure_6.jpeg)

![](_page_17_Figure_7.jpeg)

- $V_t$  denotes the size of the trade recorded at t
- $\sigma_t$  is the estimate of short-term volatility, and can be measured in several ways, as standard deviation, or as a log change of high and low prices during a predefined pretrade period beginning  $\mathcal{T}^*$  ticks before the trade tick t, as first suggested by Garman and Klass (1980):

$$\sigma_{t} = \ln \left( P_{High, [t-\tau^*, t-1]} \right) - \ln \left( P_{Low, [t-\tau^*, t-1]} \right) \tag{11}$$

 $S_t$  is the average spread observed during the  $T^*$  ticks preceding each trade. In data containing quotes, the average spread is the mean difference between the best offer and the best bid:

$$s_t = \frac{1}{\tau - 1} \sum_{j=t-\tau}^{t-1} \text{Ask}_j - \text{Bid}_j \tag{12}$$

■ When quote data is unavailable, the average effective spread can still be estimated by assuming that sequential price changes occur at intervals equal to the effective spread. Such an assumption generally holds true whenever a buy follows a sell and vice versa, as the market buy is executed at the best ask, and the market sell hits the best bid. The resulting expression for the average effective spread is shown in equation  $(19)$ , an approximation noted by Aldridge  $(2012c)$ :

$$s_{t} = \frac{1}{\tau - 1} \sum_{j=t-\tau}^{t-1} |\ln(P_{j}) - \ln(P_{j-1})| \text{ where } P_{j} \neq P_{j-1}$$
(13)

Finally,  $\hat{T}_t$  is the average clock time between every two subsequent trades:

$$T_{t} = \frac{1}{\tau - 1} \sum_{j=t-\tau}^{t-1} t_{j} - t_{j-1}$$
 (14)

Aldridge (2012c) estimates equation (9) in FGBL data. In FGBL, the additional explanatory variables influence the resulting market impact, but do not eliminate the statistical significance of the intercept, or change the value of the trade size coefficient,  $\beta_{V,\tau}$ . The impact of intertrade durations,  $T_t$ , is consistent with that described by Dufour and Engle (2000): MI is lower when average intertrade durations are shorter. According to Dufour and Engle (2000), the observation is likely due to the following: shorter intertrade durations allow more gradual impounding of information into prices, resulting in lower price changes in response to each trade.

**Causality** The estimates of MI coefficients obtained from models of equations  $(7)$ and (9) can be questioned from the following perspective: since MI is measured several ticks after each trade, is it possible that other trade ticks determine the impact and its relationship with trading volume? For example, could the size of a trade truly impact the size and directions of the following trades, which in turn would exaggerate market impact and make it appear dependent on the original trade size, instead of the follow-up trade sizes?

To answer these questions, one can deploy the so-called vector autoregressive (VAR) model (different from value-at-risk,VaR, model), first proposed by Hasbrouck (1991), and later extended by Dufour and Engle (2000). The VAR model answers the following key cause-and-effect question: does MI influence direction of subsequent trades, or does direction and size of trades influence MI to a greater degree? In addition, the VAR model allows us to test for auxiliary effects, such as any persistent irregularities during different times of day.

The Dufour and Engle (2000) specification of the VAR model that ascertains causality within five ticks from the time of each trade can be written as follows:

$$\Delta P_{t} = \sum_{j=1}^{5} a_{j} \Delta P_{t-j} + \sum_{t=8}^{18} \gamma_{t} D_{t,i} + \sum_{j=0}^{5} b_{j} Q_{i-j} + \varepsilon_{i}$$
(15)

$$Q_{i} = \sum_{j=1}^{5} c_{j} \Delta P_{t-j} + \sum_{t=8}^{18} \delta_{t} D_{t,i} + \sum_{j=1}^{5} d_{j} Q_{i-j} + \vartheta_{i}$$
(16)

where

 $R_i$  is the instantaneous market impact following a trade tick *i*, calculated as a onetick log return, that is, as a difference of logarithms of the price of tick  $i$ , and the price of the previous trade tick  $i$ -1.

$$\Delta P_t = \ln(P_t) - \ln(P_{t-1}) \tag{17}$$

 $Q_i$  is the direction of the trade *i*, with  $Q_i = 1$  when a trade is a result of a buy market order, and  $Q_i = -1$  for seller-initiated trades

 $D_{t,i}$  is a "dummy" variable indicating the hour of the day:

$$D_{t,i} = \begin{cases} 1, \text{if trade } i \text{ occurs in hour } t \\ 0, \text{otherwise} \end{cases} \tag{18}$$

 $b_i$  and  $d_i$ , in turn, are functions of trade size:

$$b_{j} = \alpha_{j} + \beta_{j} \ln(V_{j}) \tag{19}$$

$$d_j = \theta_j + \rho_j \ln(V_j) \tag{20}$$

Equation (15) measures dependency of posttrade one-tick MI  $R_i$  on the following data: lagged one-tick market impact of five preceding trades, time of day when each trade occurred, contemporaneous and lagged direction of five preceding trades, Q, and the product of contemporaneous and lagged trade direction and trade size  $QV$ . Equation (16) considers how well the same explanatory variables predict the direction of the next trade. In other words, equation (16) considers whether the past five one-tick returns, time of day, directions and sizes of the previous five trades can predict the direction of the impending trade.

Tables 5.2 and 5.3 show results of estimation of equations (15) and (16), respectively, on Eurobund futures data for May 6, 2009, a regular trading day exactly one

| (FGBL) Trade Tick Data for May 6, 2009 Ri |                |                             |                     |    |                                |  |  |  |  |
|-------------------------------------------|----------------|-----------------------------|---------------------|----|--------------------------------|--|--|--|--|
| Independent Variable: Ri−j                |                | Independent Variable: Q i−j |                     |    | Independent Variable: Vi Q i−j |  |  |  |  |
|                                           |                | α0                          | 4.1 E-05 (67.4)     | β0 | 1.9 E-07 (25.9)                |  |  |  |  |
| a1                                        | 0.347 (71.1)   | α1                          | –1.3 E-05 (–18.6)   | β1 | 8.5 E-09 (1.0)                 |  |  |  |  |
| a2                                        | 0.151 (29.0)   | α2                          | –2.8 E-06 (–3.9)    | β2 | 2.7 E-08 (3.5)                 |  |  |  |  |
| a3                                        | 0.080 (15.2)   | α3                          | 2.7 E-06 (3.8)      | β3 | 2.5 E-08 (3.2)                 |  |  |  |  |
| a4                                        | 0.061 (11.8)   | α4                          | 7.7 E-06 (11.0)     | β4 | 8.4 E-09 (1.0)                 |  |  |  |  |
| a5                                        | –0.306 (-62.5) | α5                          | –2.4 E-05 (–37.6)   | β5 | –1.1 E-07 (–14.8)              |  |  |  |  |
|                                           |                |                             | Adj. R2<br>= 46.25% |    |                                |  |  |  |  |

**Table 5.2 Results of OLS Estimation of VAR model, Equation (15), on Eurobund futures** 

Dependent variable is the one-tick return, *Ri* . *T*-statistics are reported in parentheses, bold-font values represent statistical significance of 99.999 percent and higher. *Source: Aldridge (2012d).*

year prior to the "flash crash." As shown in Table 5.2, instantaneous MI is indeed determined by MI accompanying previous trades, contemporaneous and lagged trade sign, and concurrent trade size. Trade sizes of previous trades have shown to produce little impact on future MI. The hourly dummy variable measuring the effects of the time of day was statistically significant only for the 10 to 11 GMT time period. The trades executed between 10 and 11 GMT had a lower market impact than trades executed at other hours of the day. This could, potentially be due to price trending in response to macroeconomic news. Interestingly, the explanatory power of the regression, measured by *Adj. R*<sup>2</sup> , was 46.25 percent—a substantial figure.

As Table 5.3 shows, neither the trade size nor the market impact generated by past trades (except the most recent trade) play a significant role in determining direction of upcoming trades. Instead, the direction of the subsequent trades is almost entirely determined by the direction of immediately preceding trades, buy or sell, independent of the size of those trades or the market impact each of the preceding trades generates. Specifically, according to the estimates presented in Table 5.3, on May 6, 2009, an FGBL trade immediately following a buy had a 46.2 percent likelihood of also being a buy; while a trade following two consecutive buys had a 62.5 percent probability of being a buy. A trade following three consecutive buys was 69.3% likely to be buyer initiated, and after four sequential buy trades, the probability of observing a buy rose to 72.5 percent, a large number. The hourly dummy in the trade

| Tabl<br>e 5.3 | Results of OLS Estimation of VAR<br>Model, Equation (16), on FGBL Trade Tick Data |  |  |  |  |
|---------------|-----------------------------------------------------------------------------------|--|--|--|--|
|               | for May 6, 2009 Qi                                                                |  |  |  |  |
|               |                                                                                   |  |  |  |  |

| Independent Variable: Ri−j |                | Independent Variable: Q i−j |              | Independent Variable: Vi Q i−j |                |  |  |
|----------------------------|----------------|-----------------------------|--------------|--------------------------------|----------------|--|--|
| c1                         | –841.5 (–18.1) | θ1                          | 0.462 (75.8) | ρ1                             | 2.0 E-04 (2.8) |  |  |
| c2                         | –94.1 (–1.8)   | θ2                          | 0.163 (24.6) | ρ2                             | 1.6 E-04 (2.1) |  |  |
| c3                         | 184.5 (3.6)    | θ3                          | 0.068 (10.1) | ρ3                             | 1.4 E-04 (1.9) |  |  |
| c4                         | 55.7 (1.1)     | θ4                          | 0.032 (4.7)  | ρ4                             | 1.3 E-04 (1.8) |  |  |
| c5                         | –10.2 (–0.2)   | θ5                          | 0.010 (1.7)  | ρ5                             | 2.4 E-04 (3.3) |  |  |
| Adj. R2<br>= 39.29%        |                |                             |              |                                |                |  |  |

Dependent variable is trade direction, *Q i* . *T*-statistics are reported in parentheses and bold-font values represent statistical significance of 99.999 percent and higher. *Source: Aldridge (2012d).*

sign equation happened to be only significant from 16 to 17 GMT (11:00 a.m. to noon ET). The hourly dummy from 16 to 17 GMT was positive, indicating a preponderance of buy FGBL trades during that hour on May 6, 2009. As with the estimates of the return equation (15), equation (16) showed a high adjusted *R*<sup>2</sup> of nearly 40 percent, indicating a high explanatory power of the given variables.

A question that begs further investigation is whether market conditions change dramatically one year later during the flash crash of May 6, 2010. Tables 5.4 and 5.5 present the answers: May 6, 2010 (flash crash), values exhibit little difference from a regular market day May 6, 2009, one year prior.

As shown in Aldridge (2012c), estimates of equation (15) recorded on May 6, 2009, are very similar to those estimated on the data of the flash crash, implying that the MI model performs well in most market conditions. As Aldridge (2012c) also shows, the model of equation (15) makes robust out-of-sample predictions of future market impact, delivering 99.9 percent accurate predictions of MI based on parameters estimated as much as 30 minutes ahead of a given trade.

## ■ **Summary**

Transaction costs present a considerable hurdle for high-frequency trading systems. Among all costs, however, market impact accounts for the most significant proportion of costs. Understanding and measuring the current cost structure is imperative to designing profitable systems.

## ■ **End-of-Chapter Questions**

- 1. What costs are present in the financial markets?
- 2. What are latent costs? How do they differ from transparent costs?
- 3. Which type of cost is most dominant in today's markets?
- 4. What kind of tax structure do high-frequency traders face?
- 5. What is market impact? Why does it exist?
- 6. Can market impact following a market buy order be zero? Explain.
- 7. Can expected market impact of a buy order be negative? Explain.
- 8. What is a permanent market impact? How different is it from temporary market impact?
- 9. What market impact accompanies limit orders?
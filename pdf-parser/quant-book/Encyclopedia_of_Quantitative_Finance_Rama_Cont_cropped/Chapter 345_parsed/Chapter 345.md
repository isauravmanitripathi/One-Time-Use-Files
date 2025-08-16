# **Order Types**

Most modern financial markets are *limit order markets* and use a continuous double-auction mechanism [5]. On these markets, investors can choose between different *order types* when they wish to buy or sell stocks. Each of them have specific characteristics that make them appropriate for certain types of investors or in certain situations.

The number of different order types supported on the different exchanges is actually quite large and brokers might also add complexity and propose yet more sophisticated order types to their customers. This article only reviews the most frequently used order types. As a conclusion, some empirical facts on order placement and the performance of market *versus* limit orders are highlighted.

### **Market Orders**

The simplest order type is perhaps the *market order*: the investor chooses to buy or sell at the current best available price. As long as there are willing buyers and sellers, the order is guaranteed to be executed. An important property of a market order is that the investor only specifies which quantity he/she wants to trade, not at which price. Indeed, on fast-moving markets, he/she may well obtain an execution price that differs from the best price quoted at the moment he/she decided to send the order. It may also happen that he/she receives different prices for parts of the order, in particular for large orders.

#### **Limit Orders**

Unlike a market order, a *limit order* is an order to buy or sell at a specific price. A buy (sell) limit order can only be executed at the limit price or lower (higher). Thus, the investor has some control over the execution price that he/she will obtain, but the order might not be filled. One can distinguish two types of limit orders: limit orders that are submitted at or above the market price and those that are not. The first ones, sometimes called *marketable limit orders*, are immediately executed. Those of the second kind are stored in a queue called the *limit order book*. They are executed if they are hit by market orders from the opposite side.

#### **Stop Orders**

A *stop order* is an example of a conditional order: a market order is sent once the price of a stock reaches a specified level. This type of order is used by investors who want to avoid big losses or protect profits without having to monitor the stock performance for an extended period of time. For instance, if an investor has a short position, he/she might decide to buy it back once his/her losses reach a threshold, that is, when the stock price exceeds a certain level. In the same way, he/she can limit his/her profits by buying the stocks when the price drops below a specified price. Stop orders might also be limit orders. In that case, a limit order is sent when the price reaches a level.

#### **Hidden Orders and Iceberg Orders**

Investors who wish to submit a large limit order might be concerned when their order gets noticed. A possibility is then to submit the *hidden order*. Such an order is not visible in the order book, but has usually lower time priority, that is, regular limit orders at the same price that are submitted later will be executed first. An *iceberg* (or *reserve*) order is similar except that it is not fully hidden: a fraction of the order size, called *peak volume*, is publicly disclosed. When the visible volume is filled and a hidden volume is still available, a new peak volume enters the book. On exchanges where iceberg orders are allowed, they can be quite frequent. For example, according to studies of iceberg orders on Euronext [1], 30% of the book volume is hidden.

#### **Immediate or Cancel Orders**

If a market participant wants to profit from a trading opportunity that he/she expects to last only a short period of time, he/she can consider sending a *immediate or cancel* order. This order either (partially) gets filled or is else cancelled. Thus, it never goes into the book and leaves no visible trace if it cannot be executed. This order type is similar to the *all or nothing* (sometimes called *fill or kill*) order. Orders of the latter type must be completely executed or not at all. In this way, the investor avoids revealing his intention to trade if the entire quantity was not available.

## **Day Orders and Good 'Til Canceled Orders**

An investor might want his/her order to expire if it is not executed. He/she can then submit a *day order*. Such an order is canceled if it is not executed on the day the order is placed. On the other hand, if he/she submits a good 'til canceled order (GTC), the order will remain active until the investor cancels it. Typically, his/her broker will, however, set a maximum time limit of 30–90 days after which the broker cancels the order.

#### **Market-on-close Orders**

A market-on-close (MOC) order is a market order that is submitted to execute as close to the closing price as possible. If a double-sided closing auction takes place at the end of the day (such as on the New York Stock Exchange (NYSE) or the Tokyo Stock Exchange), the order will participate in the auction. Investors might want to trade near the close because they expect liquidity to be high. Another reason might be that closing prices are widely used as a reference price (for instance, for the valuation of mutual fund shares or the determination of the payoffs to cash-settled derivatives [5]). An MOC order is then a way to obtain an execution price close to the reference price. There also exist *limit on close* orders, that is, limit orders submitted at the close. Finally, there are limit order that become market orders at the close (in Japan called *Funari* orders).

#### **Reg NMS Order Types**

In reaction to recent National Market System regulations (Reg NMS) promulgated by the United States Securities and Exchange Commission (SEC), several American exchanges developed new order types. In fact, according to Reg NMS brokers should respect the so-called Order Protection Rule, which states that one cannot ignore the top-of-book best bid and offers. This rule came into effect during the year 2007. Suppose that the best ask price for a given security is \$123.45 on Nasdaq, \$123.46 on the NYSE, and \$123.46 or more on the other market centers where it is quoted. The \$123.45 quote on Nasdaq is then protected and cannot be traded through, that is, if one sends a buy market order to the NYSE, the exchange has in principle to route it to Nasdaq. A new order type that is Reg.NMS compliant is a *do not ship* order, an order that is to be executed at one exchange. If the order would route to another market center, it will be cancelled. Another example is a Intermarket Sweep Order (ISO). This is a limit order designated to be executed exclusively at one market center. The sender fulfills the Reg NMS obligations by sending other orders to any market center quoting better prices. For more examples, see [9].

#### **Peg Orders**

With the competition between liquidity pools in the US and in Europe, some recently created venues such as Chi-X or BATS have introduced *peg orders*. These are orders that "follow" quotes from other exchanges (either the primary exchange or the best bid or offers). The venues thus hope to attract trading volume. For market participants, a peg order is convenient because they do not need to monitor the quotes on other exchanges and replace their order themselves if the price moves away. Also, alternative trading systems might be cheaper (lower exchange fees) and faster (lower latency).

#### **Empirical Studies of Order Placement**

The question of how investors submit their orders determines how the price is formed at the microstructure level. It has recently received much interest, triggered by the availability of huge datasets of order book data.

The probability that a limit order is sent at a price *p* has been shown to decay with the distance from the best price. However, the decay is slow, that is, algebraic [7]. It can be fitted by a Student distribution [6]. The distribution is symmetric, centered around the best price and the same for buying and selling. The probability that an order will is cancelled also decreases with its distance from the best price. These findings have been observed across different markets such as the London Stock Exchange, Euronext, and Instinet and are expected to be to some degree "universal". The distribution of the time to fill for executed limit orders and the time to cancel for canceled ones was studied in [2].

## **Performance of Market** *versus* **Limit Orders**

The performance of the different order types is an issue of interest for both the practitioners and academic researchers. Although the cost of a market order can be considered to be half the bid-ask spread, the cost of a limit order is not unambiguously defined. In case the order is not executed because of adverse price movement, one should in some way add the cost of the missed opportunity. Moreover, if the order does get filled, it might have been hit by an investor with more information about the future price, a phenomenon that is called *adverse selection*.

In an early study, Harris and Hasbrouck [4] suggest that limit orders are performing better, even taking into account some penalty for nonexecuted orders. According to Handa *et al.* [3], the orderdriven market is an ecological system with a competition between market and limit orders. This idea has been made more quantitative in [8], where it was suggested that on average limit orders and market orders have equal costs. Imposing that strategies that participate in a infinitesimal fraction of all market or limit orders have at best a marginal profit, one obtains a linear relation between bidask spread and the instantaneous impact of market orders, which is empirically verified. Thus, an investor who would try to earn from the spread by putting limit orders in the book would actually not make money due to the impact of incoming market orders.

#### **References**

- [1] D'Hondt, C., De Winne, R. & Fran¸cois-Heude, A. (2003). *Hidden Orders on Euronext: Nothing is Quite as it Seems*, working paper.
- [2] Eisler, Z., Kertesz, J., Lillo, F. & Mantegna, R.N. (2007). *Diffusive Behavior and the Modeling of Characteristic Times in Limit Order Executions*, Technical Report, arXiv:physics/0701335.
- [3] Handa, P., Schwartz, R.A. & Tiwari, A. (1998). The ecology of an order-driven market, *Journal of Portfolio Management* **24**(2), 47–55.
- [4] Harris, L. & Hasbrouck, J. (1996). Market vs. limit order: the SuperDOT evidence on order submission strategy, *The Journal of Financial and Quantitative Financial Analysis* **31**(2), 213–231.
- [5] Hasbrouck, J. (2007). *Empirical Market Microstructure*, Oxford University Press.
- [6] Mike, S. & Farmer, J.D. (2008). An empirical behavioral model of liquidity and volatility, *Journal of Economic Dynamics and Control* **32**, 200–234.
- [7] Potters, M. & Bouchaud, J.P. (2002). More statistical properties of order books and price impact, *Physica A* **324**(1–2), 133–140.
- [8] Wyart, M., Bouchaud, J.P., Kockelkoren, J., Potters, M. & Vettorazzo, M. (2008). Relation between bid-ask spread, impact and volatility in order-driven markets, *Quantitative Finance* **8**(1), 41–57.
- [9] www.nyse.com/pdfs/nyse regnms updates final.pdf; www.nasdaqtrader.com/content/marketregulation/ regnms/mopp.pdf (accessed Oct 2008).

#### **Related Articles**

**Algorithmic Trading**; **Limit Order Markets**; **Order Flow**.

JULIEN KOCKELKOREN
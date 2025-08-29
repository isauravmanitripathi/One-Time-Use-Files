![](_page_0_Picture_0.jpeg)

igh-frequency trading aims to identify and arbitrage temporary market inefficiencies that are created by the competing interests of market participants. Understanding the types of orders that traders can place to achieve their goals allows insights into the strategies of various traders. Ultimately, this understanding can inform the forecasting of impending actions of market participants, which itself is key to success in high-frequency trading. This chapter examines various types of orders present in today's markets.

# ORDER TYPES

Contemporary exchanges and electronic communication networks (ECNs) offer a vast diversity of ordering capabilities. The order types differ as to execution price, timing, size, and even disclosure specifications. This section considers each order characteristic in detail.

# **Order Price Specifications**

**Market Orders versus Limit Orders** Orders can be executed at the best available price or at a specified price. Orders to buy or sell a security at the best available price when the order is placed are known as market orders. Orders to buy or sell a security at a particular price are known as limit orders

When a market order arrives at an exchange or an ECN, the order is immediately matched with the best available opposite order or several best orders, depending on the size of the arriving order. For example, if a market order to sell 100,000 shares of SPY arrives at an exchange, and the exchange has the following buy orders outstanding from best to worst: 10,000 shares at \$935, 40,000 shares at \$930, and 50,000 at \$925, then the arriving market sell order is "walked through the order book" until it is filled: the first 10,000 shares are sold at \$935, the next 40,000 shares at \$930 and the final 50,000 shares at \$925, capturing the weighted-average price of \$928 per share:

$$P = \frac{10,000 \times \$935 + 40,000 \times \$930 + 50,000 \times \$925}{100,000} = \$928$$

Transaction costs, such as the broker-dealer and exchange fees, are accounted for separately, further reducing the profitability of the trade. For details on cost types and values, please see Chapter 19.

Limit orders are executed at a specified limit price or at a better price, if one is available. When a limit order arrives at an exchange or an ECN, the order is first compared with the best available opposite orders to determine whether the newly arrived order can be filled immediately. For example, when a limit order to sell SPY at 930 arrives at an exchange, the exchange first checks whether the exchange already has matching orders to buy SPY at or above 930. If orders to buy SPY at 930 or at a higher price are present, the arriving order is treated as a regular market order; it is filled immediately and charged the market order fees. If no matching orders exist, the arriving limit order is placed in the limit order book, where it remains until it becomes the best available order and is matched with an incoming market order.

The aggregate size of limit orders available in the limit order book is often thought to be the liquidity of the market. The total size of limit orders available at a particular price is referred to as the market depth. The number of different price points at which limit orders exist in the limit order book is known as the breadth of the market. Figure 6.1 illustrates components of the liquidity in the limit order book, according to Bervas (2006).

Limit orders can be seen as pre-commitments to buy or sell a specified number of shares of a particular security at a prespecified price, whereas market orders are requests to trade the specified quantity of a given security as soon as possible at the best price available in the market. As a result, market orders execute fast, with certainty, at uncertain prices and relatively high transaction costs. Limit orders, on the other hand, have a positive probability of no execution, lower transaction costs, and

![](_page_2_Figure_1.jpeg)

**FIGURE 6.1** Aspects of market liquidity (Bervas, 2006). The bid price and the ask price are defined for liquidity quantities OA and OA that represent market depths at bid and ask prices, respectively.

encompass an option to resubmit the order at a different price. Table 6.1 key outlines key differences between market and limit orders.

Market orders specify the desired exchange for the order, the exchange code of the security to be traded, the quantity of the security to be bought or sold, and whether the order is to buy or to sell. Limit orders specify the same parameters as do market orders along with the desired execution price.

**Profitability of Limit Orders** A trader placing a buy limit order writes a put option available freely, with no premium, to the market. Similarly, a trader placing a sell limit order writes a free call option on the security. In addition to foregoing the premium on the option, the limit trader opens himself up to being "picked off" by better-informed traders. For

|                    | Market Orders | Limit Orders                |
|--------------------|---------------|-----------------------------|
| Order Execution    | Guaranteed    | Uncertain                   |
| Time to Execution  | Short         | Uncertain                   |
| Execution Price    | Uncertain     | Certain                     |
| Order Resubmission | None          | Infinite prior to execution |
| Transaction Costs  | High          | Low                         |

| TABLE 6.1 | Limit Orders versus Market Orders |  |  |  |
|-----------|-----------------------------------|--|--|--|
|-----------|-----------------------------------|--|--|--|

example, suppose that the limit trader places a limit buy order on a security at \$30.00, and that another, better-informed, trader knows that \$30.00 is the maximum price the security can reach within the time interval under consideration. The better-informed trader then jumps at the opportunity to sell the security to the limit trader, leaving the limit trader in a losing position.

Despite the seeming lack of profitability of limit order traders, limit trading has prospered. Most exchanges now offer limit order capabilities, and limit order–based exchange alternatives known as the electronic communication networks (ECNs) experience a boom. The ability of exchanges and ECNs to attract numerous limit order traders suggests that limit order trading is profitable for many market participants.

Handa and Schwartz (1996) examine the profitability of limit order traders, also known as liquidity traders, and find that limit order strategies can capture economic rents in excess of market order strategies. Specifically, Handa and Schwartz (1996) find that the buy limit order strategies allow limit traders to obtain a premium of 0.1 percent to 1.6 percent per trade on average, depending on the type of the limit order strategy. Handa and Schwartz (1996) consider four types of buy limit order strategies: those with buy limit orders placed at prices 0.5 percent, 1 percent, 2 percent, and 3 percent below the corresponding market price.

To measure the profitability of limit order trades, Handa and Schwartz (1996) conducted the following experiment:

- The authors break down the trading data into equally spaced profitability evaluation periods.
- In every evaluation period, the simulated market trader executes all trades at the opening price of the evaluation period.
- The limit order trader sets limit orders at prices *x* percent below the market opening price.
- The limit order is considered executed when it is crossed by the market price.
- If the limit orders are not executed within the evaluation period, the limit trader is forced to execute his orders at the opening price of the next evaluation period.

Handa and Schwartz (1996) measure the profitability of the limit order strategy as the average difference between the prices obtained using the limit order strategy and the prices obtained using the market order strategy during each evaluation period.

The limit order strategy is profitable if the average cost of realized limit orders is lower than that of realized market orders. The profitability of the buy limit order strategy within each evaluation period is then measured according to equation (6.1):

$$\Pi_t = P_{t,M} - P_{t,L} \tag{6.1}$$

where *<sup>t</sup>* is the profitability of the buy limit order strategy in evaluation period *t*, *Pt,M* is the opening price of the evaluation period at which the market buy order is executed, and *Pt,L* is the obtained limit price—either a price obtained when the market price crosses the best limit sell order or the opening price of the next evaluation period, as defined previously. The average buy limit order profitability is then computed as an average of profitability for individual evaluation periods:

$$\overline{\Pi}_{t} = \frac{1}{T} \sum_{t=1}^{T} \left( P_{t,M} - P_{t,L} \right) \tag{6.2}$$

Handa and Schwartz (1996) assess the performance of the following buy limit orders: orders with prices set 0.5 percent, 1 percent, 2 percent, and 3 percent below the opening market price in each evaluation period. The authors run their experiments on stocks of 30 Dow Jones Industrial firms that traded on the NYSE and find that, on average, limit order strategies outperform market orders. Table 6.2 replicates the average results for limit order strategies appearing in Handa and Schwartz (1996). The results show the average percentage value by which the limit order strategy outperforms the market order strategy.

In summary, limit order strategies can bring clear profitable outcomes to traders. The limit order strategy works particularly well in the volatile range-bound markets, such as those we are currently experiencing.

**Delays in Limit Order Execution** Limit orders, when executed, are usually executed at prices more favorable than otherwise identical

| TABLE 6.2                | Average Profitability of Limit Order Strategies in Excess of the Market<br>Order Strategies |                                                                                                      |                |                |  |
|--------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------|----------------|--|
|                          |                                                                                             | The Distance of Limit Order Prices Away (in the Favorable<br>Direction) from the Market Order Prices |                |                |  |
|                          | 0.5 percent                                                                                 | 1 percent                                                                                            | 2 percent      | 3 percent      |  |
| Average<br>profitability | 0.100 percent                                                                               | 0.361 percent*                                                                                       | 0.516 percent* | 1.605 percent* |  |

\*Indicates statistical significance at the 95 percent confidence level.

market orders that are executed with certainty in most cases. The time duration of limit orders, however, is unpredictable; limit orders can be "hit" by market orders right away or can fail to be executed if the market price moves away from the price of the limit order. Failure to execute a limit order can be quite costly when the limit order is placed to close a position, particularly when the position is a loss that needs to be liquidated. For example, consider a trading strategy that is currently long USD/CAD. Suppose that the position was opened with a market buy order at 1.2005, the current market price is 1.1955, and a stop-loss order arrives to close the position. If the stop-loss order is placed as a market order, the order is executed with probability 1 at or below the current market price. If the order is placed as a limit order, and if the market price for USD/CAD suddenly drops, the order never gets filled and the losses exacerbate dramatically. As a result, stop-losses are most often executed at market to ensure that the negative exposure is reliably limited.

Failure to execute a limit order can also be costly when the order is placed to open a position, because the trading strategy incurs the opportunity cost corresponding to the average expected gain per trade. For example, consider a trading strategy that is "flat," or fully in cash, at time 0. Suppose further that at time 1, a buy order arrives to buy USD/CAD while USD/CAD is at 1.2005. If the buy order is placed as a market order, the order will be executed with a probability of 100 percent but at 1.2005 at best (latency in execution and other slippage issues may push the price even further in the adverse direction). On the other hand, if the buy order is placed as a limit order at 1.2000, the order may be executed at 1.2000 if the market price drops to that level, or it may not be executed at all if the market price stays above the limit level. If the limit order never gets hit, the system loses the trade opportunity value equal to the gain from the trade initiated at the market price.

Foucault (1999) and Parlour (1998) model dynamic conditions that ensure that limit orders get hit by market orders, while resulting in the profitable outcome for the trader placing the limit orders. The main questions answered by the two research articles are

- **1.** At what prices will traders post limit orders?
- **2.** How often do traders modify their limit orders?

Such issues in order flow dynamics impact the traders' bargaining power and affect their profitability through transaction costs. The main finding of the studies is that limit orders are preferred to market orders in high-volatility conditions. Thus, in high-volatility situations, the proportion of limit orders in the marketplace increases, simultaneously reducing cumulative profitability of agents resulting from a larger number of trades that are left not executed, as well as from the increased market bid-ask spreads. Parlour (1998) further explains the diagonal effect observed in Biais, Hillion and Spatt (1995): a market buy reduces the liquidity available at the ask, inducing sellers to post additional limit sell orders instead of market sell orders and subsequently triggering more market buy orders. Thus, serial autocorrelation in order flow arises from liquidity dynamics in addition to dynamics in informed trading. Ahn, Bae, and Chan (2001) find that the volume of limit orders increases with increases in volatility on the Stock Exchange of Hong Kong.

Both Foucault, Kadan, and Kandel (2005) and Rosu (2005) assume that investors care about execution time and submit orders based on their expectations of execution time.

Kandel and Tkatch (2006) find that investors indeed take execution delay into account when submitting limit orders on the Tel-Aviv Stock Exchange. The duration of limit orders appears to decrease with increases in aggressiveness of the limit orders (the distance of the limit orders from the current market price), as shown by survival analysis of Lo, MacKinlay, and Zhang (2002).

Goettler, Parlour, and Rajan (2005) extend the analysis to a world where investors can submit multiple limit orders, at different prices and with different order quantities. Lo and Sapp (2005) test the influence of order size along with order aggressiveness in the foreign exchange markets and find that aggressiveness and size are negatively correlated.

Hasbrouck and Saar (2002) document that limit order traders may post fleeting limit orders; according to Rosu (2005), the fleeting orders are offers to split the difference made by patient investors on one side of the book to the patient investors on the other side of the book.

Traders who are confident in their information may choose to place limit orders during the time they expect their information to impact prices. Keim and Madhavan (1995), for example, show that informed traders whose information decays slowly tend to use limit orders. The proportion of limit orders used by a particular trader or trading strategy, therefore, can be used to measure the traders' confidence in their information. The confidence variable may then be used in extracting additional information from the observed trading decisions and order flow of the traders.

**Limit Orders and Bid-Ask Spreads** A trader may also gear towards limit orders whenever the bid-ask spreads are high. The bid-ask spread may be a greater cost than the opportunity cost associated with non-execution of position entry orders placed as limit orders. Biais, Hillion, and Spatt (1995) show that on the Paris Bourse the traders indeed place limit orders whenever the bid-ask spread is large and market orders whenever the bid-ask spread is small. Chung, Van Ness, and Van Ness (1999) further show that the proportion of traders entering limit orders increases whenever bidask spreads are wide.

**Limit Orders and Market Volatility** Bae, Jang, and Park (2003) examine traders' propensity to place market and limit orders in varying volatility conditions. They find that the number of limit orders increases following a rise in intra-day market volatility, independently of the relative bid-ask spread size. Handa and Schwartz (1996) show that transitory volatility, the volatility resulting from uninformed or noise trading, induces a higher propensity of traders to place limit orders than do permanent volatility changes, given that traders can get compensated for providing liquidity while limiting the probability of being picked off. Foucault (1999), however, finds that limit orders are always more optimal than market orders, even when the probability of being picked off increases.

# **Order Timing Specifications**

Both market and limit orders can be specified as valid for different lengths of time and even at different times of the trading day. The "good till canceled" orders (GTC) remain active in the order book until completely filled. The "good till date" orders (GTD) remain in the order book until completely filled or until the specified expiry date. The GTC and GTD orders can be "killed," or canceled, by the exchange or the ECN after a predefined time period (e.g., 90 days), whenever certain corporate actions are taken (e.g., bankruptcy or delisting), or as a result of structural changes on the exchange (e.g., a change in minimum order sizes).

The "day" orders, also known as the "good for the day" (GFD) orders, remain in the order book until completely filled or until the end of the trading day, defined as the end of normal trading hours. The "good for the extended day" (GFE) orders allow the day orders to be executed until the end of the extended trading session. Orders even shorter in duration that are particularly well suited for high-frequency trading are the "good till time" (GTT) orders. The GTT orders remain in the order book until completely filled or until the specified expiry date and time and can be used to specify short-term orders. The GTT orders are especially useful in markets where order cancellation or order change fees are common, such as in the options markets. When market conditions change, instead of canceling or changing the order and thus incurring order cancellation or change fees, traders can let their previous orders expire at a predetermined time and place new orders instead.

## **Order Size Specifications**

The straightforward or plain "vanilla," order size specification in both limit and market orders is a simple number of security contracts geared for execution. Vanilla order sizes are typically placed in "round lots"—that is, the standard contract sizes traded on the exchange. For example, a round lot for common stocks on the New York Stock Exchange (NYSE) is 100 shares. Smaller orders, known as "odd lots," are filled by a designated odd lot dealer (on a per-security basis), and are normally charged higher transaction costs than the round-lot orders. Both market and limit orders can be odd lots.

Orders bigger than round lots, yet not in round-lot multiples, are known as "mixed lots." Mixed-lot orders are typically broken down into the round lots and the odd lots on the exchange and are executed accordingly by a regular dealer and the odd-lot dealer.

When large market orders are placed, there may not be enough liquidity to fill the order, and subsequent liquidity may be attainable only at prices unacceptable to the trader placing the market order. To address the problem, most exchanges and ECNs accept "fill or kill" (FOK) orders that specify that the order be filled immediately in full, or in part, with the unfilled quantity killed in its entirety. If the partial fill of the market order is unacceptable to the trader, the order can be specified as a "fill and kill" (FAK) order, to be either filled immediately in full or killed in its entirety. Alternatively, if the immediacy of the order execution is not the principal concern but the size is, the order can be specified as an "all or none" (AON) order. The AON orders remain in the order book with their original time priorities until they can be filled in full.

#### **Order Disclosure Specifications**

The amount of order information that is disclosed varies from exchange to exchange and from ECN to ECN. On some exchanges and ECNs, all market and limit orders are executed with full transparency to all market participants. Other exchanges, such as the NYSE, allow market makers to decide how much of an incoming market order should be executed at a given price. Other exchanges show limit orders only for a restricted set of prices that are near the current market price. Still others permit "iceberg" orders—that is, orders with only a portion of the order size observable to other market participants.

A "standard iceberg" (SI) order is a limit order that specifies a total size and a disclosed size. The disclosed size is revealed as a limit order. Once the disclosed size is completely executed, the new quantity becomes disclosed, and it is instantaneously made available for matching with time priority corresponding to the release time.

An order is often placed anonymously, without disclosing the identity of the trader or the trading institution to other market participants on the given exchange or ECN. Anonymous orders are particularly attractive to traders processing large orders, as any identifying information may trigger adverse price offers from other market participants.

#### **Stop-Loss and Take-Profit Orders**

In addition to previously discussed specifications of order execution, some exchanges offer stop-loss and take-profit order capability. Both the stoploss and take-profit orders become market or limit orders to buy or sell the security if a specified price, known as the stop price, is reached, or passed.

### **Administrative Orders**

A change order is an order to change a pending limit order, whether a limit open or limits for take-profit or stop-loss. The change order can specify the change in the limit price, the order type (buy or sell), and the number of units to process. A change order can also be placed to cancel an existing limit order. Some execution counterparties may charge a fee for a change order.

A margin call close order is one order traders probably want to avoid. It is initiated by the executing counterparty whenever a trader trades on margin and the amount of cash in the trader's account is not sufficient to cover two times the losses of all open positions. The margin call close is executed at market at the end of day, which varies depending on the financial instrument traded.

Most broker-dealers and ECNs provide phone support for clients. If customer computer system or network connectivity breaks down for whatever reason, a customer can phone in an order. Such phone-in orders are sometimes referred to as "orders by hand," and are often charged a transaction cost premium relative to the electronic ordering.

Finally, several cancel orders can be initiated either by the customer or by the executing counterparty. An insufficient funds cancel can be enacted by the executing broker in the event that the customer does not have enough funds to open a new position. Limit orders can be canceled if the price of the underlying instrument moves outside the preselected bounds; such orders are known as bound violation cancel orders.

### **ORDER DISTRIBUTIONS**

Order statistics, such as Oanda's FX Trade presented in Table 6.3, are seldom, if ever, distributed to the public. It should be noted, however, that the mean and median size of Oanda FXTrade transactions indicate that the majority of Oanda's customers are retail and that the numbers are thus not necessarily representative of order flows at broker-dealers and ECNs. Nevertheless, the data offers an interesting point for comparison.

As Table 6.3 shows, on an average day between October 1, 2003 and May 14, 2004, the most common orders—both by number of orders and by volume—were stop-loss or take-profit (22 percent and 23 percent,

| Transaction Record       | Percentage of<br>Orders per<br>Order Count | Mean Daily<br>Trading<br>Volume in EUR | Percentage of<br>Orders by<br>Trade Volume |
|--------------------------|--------------------------------------------|----------------------------------------|--------------------------------------------|
| Buy Market (open)        | 13.10 percent                              | 167,096                                | 14.13 percent                              |
| Sell Market (open)       | 10.61 percent                              | 135,754                                | 11.48 percent                              |
| Buy Market (close)       | 8.27 percent                               | 110,461                                | 9.34 percent                               |
| Sell Market (close)      | 10.27 percent                              | 140,263                                | 11.86 percent                              |
| Limit Order: Buy         | 5.41 percent                               | 61,856                                 | 5.23 percent                               |
| Limit Order: Sell        | 4.76 percent                               | 48,814                                 | 4.13 percent                               |
| Buy Limit Order          | 3.22 percent                               | 23,860                                 | 2.02 percent                               |
| Executed (open)          |                                            |                                        |                                            |
| Sell Limit Order         | 2.92 percent                               | 14,235                                 | 1.20 percent                               |
| Executed (open)          |                                            |                                        |                                            |
| Buy Limit Order          | 0.46 percent                               | 6,091                                  | 0.52 percent                               |
| Executed (close)         |                                            |                                        |                                            |
| Sell Limit Order         | 0.46 percent                               | 6,479                                  | 0.55 percent                               |
| Executed (close)         |                                            |                                        |                                            |
| Buy Take-Profit (close)  | 3.14 percent                               | 12,858                                 | 1.09 percent                               |
| Sell Take-Profit (close) | 3.49 percent                               | 19,401                                 | 1.64 percent                               |
| Buy Stop-Loss (close)    | 2.18 percent                               | 19,773                                 | 1.67 percent                               |
| Sell Stop-Loss (close)   | 2.55 percent                               | 23,391                                 | 1.98 percent                               |
| Buy Margin Call (close)  | 0.12 percent                               | 733                                    | 0.06 percent                               |
| Sell Margin Call (close) | 0.17 percent                               | 1,213                                  | 0.10 percent                               |
| Change Order             | 3.01 percent                               | 61,229                                 | 5.18 percent                               |
| Change Stop-Loss or      | 22.36 percent                              | 268,568                                | 22.71 percent                              |
| Take-Profit              |                                            |                                        |                                            |
| Cancel Order by Hand     | 2.41 percent                               | 44,246                                 | 3.74 percent                               |
| Cancel Order:            | 0.28 percent                               | 10,747                                 | 0.91 percent                               |
| Insufficient Funds       |                                            |                                        |                                            |
| Cancel Order: Bound      | 0.20 percent                               | 860                                    | 0.07 percent                               |
| Violation                |                                            |                                        |                                            |
| Order Expired            | 0.65 percent                               | 4,683                                  | 0.40 percent                               |
| Total:                   | 100.04 percent                             | 1,182,611                              | 100.00 percent                             |

**TABLE 6.3** Daily Distributions of Trades per Trade Category in FX Spot of Oanda FXTrade, a Toronto-Based Electronic FX Brokerage, as Documented by Lechner and Nolte (2007)

| TABLE 6.4 | Popularity of Orders as a Percentage of Order Number and Total<br>Volume among Orders Recorded by Oanda between October 1, 2003<br>and May 14, 2004 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

| Order Type                                        | Number of Orders,<br>Daily Average | Total Volume<br>in EUR |
|---------------------------------------------------|------------------------------------|------------------------|
| Percent of All Open Orders That Are Buy<br>Orders | 55 percent                         | 55 percent             |
| Percent of Market Orders That Are Buy<br>Orders   | 55 percent                         | 55 percent             |
| Percent of Open Buy Limit Orders Executed         | 60 percent                         | 39 percent             |
| Percent of Open Sell Limit Orders Executed        | 61 percent                         | 29 percent             |
| Total Long Positions Opened per Day               | 1,647                              | 190,956                |
| Closing the Long Position                         |                                    |                        |
| Sell Market (close)                               | 63 percent                         | 73 percent             |
| Sell Take-Profit (close)                          | 21 percent                         | 10 percent             |
| Sell Stop-Loss (close)                            | 16 percent                         | 12 percent             |
| Sell Limit Order Executed (close)                 | 3 percent                          | 3 percent              |
| Sell Margin Call (close)                          | 1 percent                          | 1 percent              |
| Total Short Positions Opened per Day              | 1,367                              | 149,989                |
| Closing the Short Position                        |                                    |                        |
| Buy Market (close)                                | 61 percent                         | 74 percent             |
| Buy Take-Profit (close)                           | 23 percent                         | 9 percent              |
| Buy Stop-Loss (close)                             | 16 percent                         | 13 percent             |
| Buy Limit Order Executed (close)                  | 3 percent                          | 4 percent              |
| Buy Margin Call (close)                           | 1 percent                          | 0 percent              |

respectively), buy market open (13 percent and 14 percent), sell market open (11 percent), and sell market close (10 percent and 12 percent by order number and volume, respectively).

Aggregating the data by buy and sell order types provides insightful statistics on the distribution of orders. As Table 6.3. further shows, 55 percent of both market or limit open orders were buy orders. The numbers reflect a slight preference of smaller customers to enter into long positions.

Out of the total number of open limit orders placed, 60 percent and 61 percent were "hit" or executed across both buy limit opens and sell limit opens (three hits for every five orders). By volume, however, the hit percentage on limit orders was significantly lower. Out of all the buy limit open orders, only 39 percent were hit (EUR 390 hit for every EUR 1,000 in buy limit open orders). Out of all the sell limit open orders, the hit rate was even lower: just 29 percent (EUR 290 hit out of every EUR 1,000 sell limit open orders placed). The observed discrepancy probably reflects the relative propensity of higher-volume traders to seek bargains—that is to place limit open orders farther away from the market in the hope of entering a position at a lower buy or a higher sell.

Among the opened positions, long and short, discrepancies persisted relating to the position closing method. A comparison of columns 2 and 3 in Table 6.4 shows that larger customers were less likely to close their positions using take-profit and stop-loss orders than were smaller customers and that larger customers preferred to close their positions using market orders instead. This finding may reflect the relative sophistication of larger customers: since all the take-profit and stop-loss orders may be artificially triggered by Oanda's proprietary trading team, larger customers may be posting well-timed market orders instead. However, among those customers using take-profit and stop-loss provisions, smaller customers had a higher success ratio: by the number of orders, customers took profit on 21 percent of orders and experienced stop-losses on 16 percent of orders. By volume, customers took profit on only 9 percent of orders and experienced stop-losses on 13 percent of orders.

### **CONCLUSION**

Diversity of order types allows traders to build complex trading strategies by changing price, timing, transparency, and other parameters of orders. Still, simple market and limit orders retain their popularity in the trading community because of their versatility and ease of use.
# CHAPTER 18

# **Executing and** Monitoring **High-Frequency** Trading

nce a high-frequency trading system is designed and back-tested. it is applied to live capital (i.e., executed). The execution process can be complex, particularly as the capital allocated to the strategy grows and the adverse cost of market impact begins to take effect. To maximize trading performance and minimize costs, the best high-frequency trading systems are executed through optimization algorithms. To ensure that all algorithms of the trading system work as intended, a strict monitoring process is deployed.

This chapter discusses the best contemporary practices in the execution and monitoring of high-frequency trading systems.

Execution optimization algorithms tackle the following questions:

- Should a particular order issued by the trading strategy be executed in full or in smaller lots?
- Should the order be optimally processed as a market or a limit order?
- Is there an order-timing execution strategy that delivers a better-thanexpected order fill price, given current market conditions?

The optimization algorithms can be developed internally or purchased off the shelf. Off-the-shelf algorithms are often cheaper, but they are less transparent than internally developed platforms. Both external and internal execution optimization systems, however advanced, may possess unexpected defects and other skews in performance and result in costly execution blunders.

To detect undesirable shifts in costs and other trading parameters during execution, all execution processes must be closely monitored. Even the

most miniscule problems in execution may have fast and dramatic effects on performance; timely identification of potential issues is a nonnegotiable necessity in high-frequency operations.

#### **EXECUTING HIGH-FREQUENCY TRADING SYSTEMS**

#### **Overview of Execution Algorithms**

Optimization of execution is becoming an increasingly important topic in the modern high-frequency environment. Before the introduction of computer-enabled trading optimization algorithms, investors desiring to trade large blocks of equity shares or other financial instruments may have hired a broker-dealer to find a counterparty for the entire order. Subsequently, broker-dealers developed "best execution" services that split up the order to gradually process it with limited impact on the price. The advent of algorithmic trading allowed institutional traders to optimize trading on their own, minimizing the dominance of broker-dealers and capturing a greater profit margin as a result.

Optimization algorithms take into account a variety of current market conditions as well as characteristics of the orders to be processed: order type, size, and frequency. Bertsimas and Lo (1998) developed optimization strategies to take advantage of contemporary price changes. Engle and Ferstenberg (2007) examined the risks embedded in execution. Almgren and Chriss (2000) and Alam and Tkatch (2007), among others, studied the effects of "slicing" up orders into batches of smaller size. Obizhaeva and Wang (2005) optimize execution, assuming that post-trade liquidity is not replenished immediately. Kissell and Malamut (2006) adapt the speed of order processing to traders' current beliefs about the impending direction of market prices.

In addition to algorithms optimizing the total execution cost of trading, algorithms have been developed to optimize liquidity supply, hedge positions, and even to optimize the effort extended in monitoring position changes in the marketplace. See Foucault, Roell and Sandas (2003) for an example of the latter. In this chapter, we consider three common forms of executing optimization algorithms:

- **1.** Trading-aggressiveness selection algorithms, designed to choose between market and limit orders for optimal execution
- **2.** Price-scaling strategies, designed to select the best execution price according to the prespecified trading benchmarks

**3.** Size-optimization algorithms that determine the optimal ways to break down large trading lots into smaller parcels to minimize adverse costs (e.g., the cost of market impact)

#### **Market-Aggressiveness Selection**

Aggressive execution refers to high trading frequency and to short trading intervals that may lead to high market impact. Aggressive execution most often skews toward the heavy use of market orders. Passive trading, on the other hand, is lower frequency, depends more on limit orders, but may be subject to non-execution risk should the market move adversely. To balance passive and aggressive trading, Almgren and Chriss (1999) propose the following optimization:

$$\min_{\alpha} \text{ Cost}(\alpha) + \lambda \text{ Risk}(\alpha) \tag{18.1}$$

where α is the trading rate often calculated as a percentage of volume (POV) or liquidity that the strategy absorbs during the trading period and λ is the coefficient of risk aversion of the investor. Plotting cost/risk profiles for various algorithms identifies efficient trading frontiers that are wellsuited for comparisons of algorithm efficiencies and for determining the suitability of a particular algorithm to the trading needs of a particular investor.

According to Kissell and Malamut (2005), market aggressiveness (POV or α) can be varied using a combination of market and limit orders. Market orders tend to increase the POV or α, whereas limit orders decrease market aggressiveness.

The cost and risk functions used in the optimization equation (18.1) are defined as follows:

$$Cost(\alpha) = E_0 [P(\alpha) - P_b]$$
(18.2)

$$\text{Risk}(\alpha) = \sigma(\varepsilon(\alpha)) \tag{18.3}$$

$$P(\alpha) = P + f(X, \alpha) + g(X) + \varepsilon(\alpha) \tag{18.4}$$

- where *E*<sup>0</sup> denotes the ex-ante expectation at the start of the trading period,
  - P*<sup>b</sup>* is the benchmark execution price,
  - P(α) is the realized execution price defined in equation (18.4),
  - ε(α) is a random deviation of the trading outcome, *E*[ε(α)] = 0, Var[ε(α)] = σ2(α).

 $P$  is the market price at the time of order entry,

- $f(X, \alpha)$  is a temporary market impact due to the liquidity demand of trading, and
- $g(X)$  is the permanent price impact due to information leakage during order execution.

#### **Price-Scaling Strategies**

The main objective of so-called price-scaling execution algorithms is to obtain the best price for the strategy. The best price can be attained relative to a benchmark—for example, the average daily price for a given security. The best price can also be attained given the utility function of the end investor or a target Sharpe ratio of a portfolio manager.

The algorithm that minimizes the cost of execution relative to a benchmark is known as a Strike algorithm. The Strike is designed to capture gains in periods of favorable prices; the algorithm is aggressive (executes at market prices) in times of favorable prices and passive (places limit orders) in times of unfavorable prices. The Strike strategy dynamically adjusts the percent of volume rate  $\alpha$  used to process market orders of the strategy to minimize the quadratic execution cost of the strategy:

$$\min_{\alpha_t} E_t \left[ P_{t+1}(\alpha_t) - P_{b,t} \right]^2 \tag{18.5}$$

where  $P_{t+1}(\alpha_t)$  is the realized price obtained using the trading aggressiveness level  $\alpha_t$  decided upon at time t, and  $P_{b,t}$  is the benchmark price at time  $t$  used to compare the trading performance.

The Plus algorithm maximizes the probability of outperforming a specified benchmark while minimizing risk. To do so, the algorithm maximizes the following Sharpe ratio-like specification:

$$\max_{\alpha_{t}} \frac{E_{t} \left[ P_{t+1}(\alpha_{t}) - P_{b,t} \right]}{\left( V(P_{t+1}(\alpha_{t}) - P_{b,t}) \right)^{1/2}} \tag{18.6}$$

where, as before,  $P_{b,t}$  is the benchmark price at time t used to compare the trading performance, and  $P_{t+1}(\alpha_t)$  is the realized price obtained using the trading aggressiveness level  $\alpha_t$  decided upon at time t.

Finally, the Wealth algorithm maximizes investor wealth in the presence of uncertainty. The Wealth algorithm is passive during periods of favorable prices, but acts aggressively during periods of unfavorable prices with the goal of preserving the investor's wealth in adverse conditions. The Wealth strategy is obtained by optimizing the following expression:

$$\max_{\alpha} \log E_t \left[ U(P_{t+1}(\alpha_t)) \right] \tag{18.7}$$

where *U*(.) is a utility function approximating the risk-return preferences of the investor. The utility function may be the one shown in equation (18.8):

$$U(x) = E[x] - \lambda V[x] \qquad (18.8)$$

where *x* is the realized payoff and λ is the risk aversion coefficient of the investor. The risk-aversion coefficient λ is 0 for a risk-neutral investor, or an investor insensitive to risk. A risk-averse investor will have λ greater than 0; λ of 0.5 and above would characterize a highly risk-averse investor.

The profitability of execution algorithms depends on concurrent market conditions. Kissell and Malamut (2005) compared the three execution strategies in detail and found that all three strategies consistently outperform random, nonsystematic execution. Among the algorithms, the Strike method delivers a lower average cost but ignores participation in favorable price conditions. The Plus strategy also delivers a low average cost, but increases the risk of unfavorable prices. Finally, the Wealth strategy is able to capture a greater proportion of favorable price conditions but at the expense of higher average prices.

#### **Slicing Large Orders**

Kyle (1985) and Admati and Pfleiderer (1988) were the first to suggest that for informed investors to profit from their information, they need to trade in a fashion that precludes other market participants from recognizing the informed investors' order flow. Should other investors recognize the order flow of informed investors, they could front-run the informed parties, diluting their profitability. Barclay and Warner (1993) argue that for institutions to trade with their positions undetected, their large order packets need to be broken up into parcels of medium size—not too big and not too small—in order to minimize other trading participants' ability to distinguish these orders from other, "noise," orders. Chakravarty (2001) studies the impact of stealth trading—that is, trading by breaking down large trading blocks into small order parcels with the intent of causing the least market impact. Chakravarty (2001) finds that, consistent with the hypotheses of Barclay and Warner (1993), medium-sized orders indeed are followed by disproportionally large price changes, relative to all price and overall proportion of trades and volume.

Alam and Tkatch (2007) analyzed data from the Tel-Aviv Stock Exchange to study the performance of institutional investors who slice their orders into blocks of equal size in order to avoid being detected and picked off by other traders. Alam and Tkatch (2007) detect these orders as groups of equally sized, equally priced same-direction orders placed within two minutes of each other. Alam and Tkatch (2007) report that sliced orders have a median of four "slices" or consecutively streaming components.

Out of all the slice orders submitted, about 79 percent are executed and 20 percent are canceled by the trader prior to execution. The execution rate of slice orders compares favorably with the execution rate of all orders; only 63 percent of all orders, including sliced and non-sliced orders, are executed.

Another metric of slice efficiency is order fill rate. The order fill rate measures the proportion of the order that was "hit" or executed. Completely executed orders have a fill rate of 100 percent; the order that failed to execute has a fill rate of 0 percent. Regular, non-sliced, orders may encounter a partial fill, depending on the order size. Alam and Tkatch (2007) show that non-sliced orders have a fill rate of 40 percent, while sliced orders have a fill rate of 48 percent. Slicing particularly improves the fill rate of limit orders; regular limit orders have a fill rate of 42 percent, while sliced limit orders have a fill rate of 77 percent.

Sliced orders are executed more quickly. Alam and Tkatch (2007) report that the mean execution time for a fully filled sliced order is 3 minutes and 29 seconds, while the mean execution time for a regular order is 11 minutes and 54 seconds.

Execution is costly not only in terms of the average transaction costs but in terms of risks associated with execution. The risk embedded in execution comprises primarily two types of risk: (1) the uncertainty of the price at which market orders are executed and (2) the uncertainty in the timing of the execution of limit orders and the associated opportunity cost. Extreme examples of such costs include the possible failure to execute a limit order and an insufficient market depth at a reasonable range of prices for market order execution.

Execution risk creates an additional dimension for portfolio risk/return optimization and has to be taken into account. Engle and Ferstenberg (2006) propose that the study of possible execution risks is necessary to determine the following aspects of portfolio management:

- Is risk-neutral portfolio management optimal in the presence of execution risks?
- Is execution risk diversifiable in a portfolio of several financial instruments?
- Can execution risk be hedged?

Instead of executing the total order size at the same time, institutions employ strategies to minimize market impact by, for example, splitting the total order size into discrete blocks executed over time, often several days. The identification of impending trading periods with extensive liquidity, therefore, becomes an important problem for optimization of execution. Several recent studies have characterized properties of liquidity that may assist managers in forecasting liquidity going forward; specifically, liquidity has been shown to be time varying, yet persistent from one period to the next. These studies include those of Chordia, Roll, and Subrahmanyam (2001, 2002); Hasbrouck and Seppi (2001); and Huberman and Halka (2001).

Obizhaeva and Wang (2005) analytically derive optimal execution sizes depending on the execution horizon of the trade and the "speed of recovery" of the limit order book for a given security. The speed of recovery is a measure of how fast the limit order book absorbs the market impact generated by the previous lot in the execution sequence. Obizhaeva and Wang (2005) find that for securities with a reasonable speed of limit order book recovery, the optimal trading strategy is to process large lots at the beginning and at the end of the execution period with small lots spaced in between. The spacing of smaller lots depends on whether the speed of recovery for the traded security is uniform throughout the day. If the speed of recovery is not uniform throughout the day, larger lots should be processed at times with higher speeds of recovery.

Nevmyvaka, Kearns, Papandreou, and Sycara (2006) have developed an algorithm for optimizing execution through a dynamic combination of market and limit orders. The optimization is focused on a specific task: to acquire *V* shares of a particular financial security within *T* seconds of the order. The authors compare the following three market and limit order execution scenarios to obtain a certain number of shares, *V*:

- **1.** Submit a market order for *V* shares immediately at the beginning of the trading period, time 0. This approach guarantees execution, but the liquidity required to fulfill the order may be costly; the trader may need to explore the depth of the book at suboptimal prices and wide bid-ask spreads.
- **2.** Wait until the end of the trading period and submit a market order for *V* shares at time *T*. This strategy may improve upon the obtained price, but it is also subject to market volatility risks. Full bid-ask spread is present.
- **3.** Submit a limit order for *V* shares at the beginning of the trading period (time 0) and a market order for the unexecuted shares (if any) at the end of the trading period (time *T*). This strategy avoids paying bid-ask spread if the limit order is executed. The worst-case outcome of this strategy is that presented in case 2.

In all three scenarios, the trading period ends with the same number of shares, *V*. In each scenario, however, the *V* shares can potentially be obtained at a different cost.

Nevmyvaka, Kearns, Papandreou, and Sycara (2006) found that the best strategy is strategy 3, with limit orders placed at the beginning of the trading period and besting the market price by one tick size. For example, if we want to buy 500 shares of IBM within 300 seconds, the current market bid and offer prices are \$93.63 and \$93.67, and the minimum tick size is  $$0.01$ , the optimal strategy will be to submit a limit buy order at  $$93.64$ , one tick better than the best limit buy currently available on the market. The unfilled portion of the order is then executed at market at the end of the  $300$ -second period.

# MONITORING HIGH-FREQUENCY EXECUTION

Monitoring high-frequency execution involves a two-part process:

- First, allowable ranges of trading and other run-time parameters are identified through pre-trade analysis.
- Next, the run-time performance is continuously compared to the pretrade estimates; the decisions to shut down the system are made in cases when the run-time parameters breach pre-trade guidelines.

The sections that follow detail the key considerations in pre-trade analysis and run-time monitoring.

# **Pre-Trade Analysis**

Pre-trade analysis is designed to accomplish the following objectives:

- Estimate expected execution costs given current market conditions.
- Estimate expected execution risks:
  - The risk of non-execution at a desired price
  - The risk of non-execution due to insufficient liquidity
  - The risk of non-execution due to system breakdown

The estimates are then included in the determination of run-time stopgain and stop-loss parameters.

Solid high-frequency systems specify and monitor the following microlevel deviations

- Allowable versus realized deviations in price of the traded instrument
- Allowable versus realized deviations in market volume or security volume
- Maximum allowable versus realized trade duration.

# **Monitoring Run-Time Performance**

High-frequency trading is particularly vulnerable to deviations of trading behavior from the expected norm. Even the smallest deviations in trading costs, for example, can destroy the profitability of high-frequency trading strategies capturing minute bursts of price movements. As a result, run-time monitoring of trading conditions is critical to successful implementation of high-frequency strategies.

Monitoring trading performance can be delegated to a designated human trader armed with an array of dynamically updated performance gauges. Kissell and Malamut (2005) list the following metrics of trading performance as desirable tools for performance monitoring:

- **1.** Allowable deviation in the price of the traded instrument from the target execution price ensures that the execution is suspended whenever the market impact costs become too high for the strategy to remain profitable. For example, a strategy with an average net per-trade gain of 5 bps or pips can sustain the maximum market impact costs of 4 bps or pips. A market impact cost of 5 bps or more renders the strategy unprofitable.
- **2.** Processing market orders in high-volume conditions limits the market impact of the strategy and increases profitability. Specifying the minimum level of volume allowable to run the strategy caps market impact costs.
- **3.** The longer the limit orders have been outstanding, the higher is the probability that the market price has moved away from the limit order prices, increasing the risk of non-execution. Specifying the maximum allowable duration of orders reduces the risk of non-execution: if a limit order is not executed within the prespecified time period, the order is either canceled or executed at market.

# **CONCLUSION**

Successful execution is key to ensuring profitability of high-frequency strategies. Various algorithms have been developed to optimize execution. Furthermore, a human trader tasked with observing the trading parameters should have strict directions for termination of outstanding positions. Such oversight ensures smooth operation and swift reaction to disruptive and potentially costly events.

# CHAPTER 19 **Post-Trade** Profitability Analysis

 $\bullet$  rading costs can make and break the profitability of a highfrequency trading strategy. Transaction costs that may be negligible for long-term strategies are amplified dramatically in a high-frequency setting.

If market movements are compared to ocean wave patterns, long-term investment strategies can be thought of as surfers riding the trough to crest waves. High-frequency strategies are like pebbles thrown parallel to the ocean floor and grazing small ripples near the shore. Small changes in the wave pattern do not make a significant difference in the surfer's ability to tame large waves. On the other hand, a minute change in the wave structure can alter the pebble's trajectory. The smaller the pebble, the higher the influence of the wave shape, size, and speed. Transaction costs can be thought of as the market wave properties barely perceivable to the low-frequency strategies seeking to ride large market movements. At the same time, transaction costs substantially affect the profitability of high-frequency trades, seeking to capture the smallest market ripples. This chapter focuses on the transparent and latent costs that impact highfrequency trading. The roles of inventory and liquidity on the structure of a market and on realized execution are discussed, as are order slicing and other trading-optimization techniques that allow traders to obtain the best price. In addition to identification and management of trading costs, the chapter also reviews common approaches to analyzing post-trade performance.

Post-trade analysis has two parts:

- 1. **Cost analysis**—realized execution costs for all live trading strategies
- 2. **Performance analysis**—execution performance relative to a benchmark.

Post-trade analyses can be run after each trade, as well as at the end of each trading day. The analyses are often programmed to start and run automatically and to generate consistent daily reports. The reports are generated for each trading strategy and are studied by every portfolio manager or strategist and every trader, if any are involved in the execution process. Cost analysis and benchmarking analysis are discussed in the sections that follow.

#### POST-TRADE COST ANALYSIS

Analysis of execution costs begins with identification and estimation of costs by type and as they are incurred in an individual trade, in a trading strategy, by a portfolio manager, or by an execution trader. Execution costs are the trading fees or commissions paid by either the buyer or the seller but not received by the buyer or the seller. A novice may assume that trading costs comprise only the broker commissions and exchange fees. In reality, most trades incur at least nine types of cost, most of which are not observable directly and require a rigorous estimation process. The most common execution costs are the following:

- Transparent execution costs:
  - Broker commissions—fixed and variable components
  - Exchange fees
  - Taxes
- Latent execution costs:
  - Bid-ask spread
  - Investment delay
  - Price appreciation
  - Market impact
  - Timing risk
  - Opportunity cost

Costs known prior to trading activity are referred to as "transparent" or "explicit," and costs that have to be estimated are known as "latent" or "implicit." According to Kissell and Glantz (2003), while the transparent costs are known with certainty prior to trading, latent costs can only be estimated from the costs' historical distribution inferred from the data of past trades. The goal of estimating latent cost values is to remove the pre-trade uncertainty about these costs during execution. Once all applicable execution costs have been identified and estimated, cost information is relayed to the trading team to find ways to deliver better, more cost-efficient execution. At a minimum, the cost analysis should produce cost estimates in the format shown in Table 19.1. The mechanics of identification and estimation of each type of execution cost are described in the following sections.

#### **Transparent Execution Costs**

**Broker Commissions** Brokers charge fees and commissions to cover the costs of their businesses, which provide connectivity to different exchanges and inter-dealer networks. Broker commissions can have both fixed and variable components. The fixed component can be a flat commission per month or a flat charge per trade, often with a per-trade minimum. The variable component is typically proportional to the size of each trade, with higher trade sizes incurring lower costs.

Brokers set custom price schedules to differentiate their businesses. The differences in cost estimates from one executing broker to another can be significant, because some brokers may quote lower fees for a particular set of securities while charging premium rates on other trading instruments.

Broker commissions may also depend on the total business the broker receives from a given firm, as well as on the extent of "soft-dollar" transactions that the broker provides in addition to direct execution services. Brokers' commissions typically cover the following services:

- Trade commissions
- Interest and financing fees
- Market data and news charges
- Research
- Other miscellaneous fees

Some broker-dealers may charge their customers additional fees for access to streaming market data and other premium information, such as proprietary research. Others may charge separately for a host of incremental miscellaneous fees.

Broker commissions generally come in two forms—bundled and unbundled. Bundled commissions are fixed all-in prices per contract and may include the fees of the exchanges through which equity, futures, or commodity trades are executed. For example, a fixed bundled fee can be USD

| 9.1<br>TABLE 1       | mple Cost Reporting Worksheet<br>A Sa |                      |                     |      |         |                 |          |
|----------------------|---------------------------------------|----------------------|---------------------|------|---------|-----------------|----------|
|                      |                                       | Strategy/            |                     |      |         | Characteristics |          |
| Metric               | Financial<br>Security                 | Portfolio<br>Manager | Executing<br>Broker | Mean | Std Dev | wness<br>Ske    | Kurtosis |
| Broker Fees and      |                                       |                      |                     |      |         |                 |          |
| missions<br>m<br>Co  |                                       |                      |                     |      |         |                 |          |
| Exchange Fees        |                                       |                      |                     |      |         |                 |          |
| Taxes                |                                       |                      |                     |      |         |                 |          |
| Bid-Ask Spread       |                                       |                      |                     |      |         |                 |          |
| ment Delay<br>Invest |                                       |                      |                     |      |         |                 |          |
| Price Appreciation   |                                       |                      |                     |      |         |                 |          |
| mpact<br>Market I    |                                       |                      |                     |      |         |                 |          |
| ming Risk<br>Ti      |                                       |                      |                     |      |         |                 |          |
| Opportunity Cost     |                                       |                      |                     |      |         |                 |          |

0.10 per stock share. The unbundled fees account for exchange fees and broker commissions separately. Since exchanges charge different rates, the unbundled fee structures allow investors to minimize the commissions they pay. Equity brokers charge USD 0.0001 to USD 0.003 commissions per share of stock traded through them in addition to the exchange fees, discussed in the following section. Similarly, in foreign exchange, some broker-dealers offer "no commission" platforms by pricing all costs in the increased bid-ask spreads. Others go to the opposite extreme and price all trades according to the "unbundled" list of minute trade features.

Broker-dealers also differ on the interest they pay their clients on cash accounts as well as on the financing fees they charge their clients for services such as margin financing and other forms of leverage. The cash account is the portion of the total capital that is not deployed by the trading strategy. For example, if the total size of the account a firm custodies with a broker-dealer is \$100,000,000, and out of this amount one actively trades only \$20,000,000, the remaining \$80,000,000 remains "in cash" in the account. Brokers typically use this cash to advance loans to other customers. Brokers pay the cash account owners interest on the passive cash balance; the interest is often the benchmark rate less a fraction of a percent. The benchmark rate is typically the Fed Funds rate for the USD-denominated cash accounts and the central-bank equivalents for deposits in other currencies. A sample rate may be quoted as LIBOR minus 0.1 percent, for example. Brokers usually charge the benchmark rate plus a spread (0.05 percent – 1 percent) for financing borrowing investors' leverage and generate income on the spread between their borrowing and lending activities. The spread ideally reflects the creditworthiness of the borrower.

Broker commissions are negotiated well in advance of execution. Detailed understanding of broker commission costs allows optimization of per-order cost structures by bundling orders for several strategies together or by disaggregating orders into smaller chunks.

**Exchange Fees** Exchanges match orders from different broker-dealers or electronic communication networks (ECNs) and charge fees for their services. The core product of every exchange is the inventory of open buy and sell interest that traders are looking to transact on the exchange. To attract liquidity, exchanges charge higher fees for orders consuming liquidity than for orders supplying liquidity. In an effort to attract liquidity, some exchanges go as far as paying traders that supply liquidity, while charging only the traders that consume liquidity.

Liquidity is created by open limit orders; limit buy orders placed at prices below the current ask provide liquidity, as do limit sell orders placed at prices above the current bid. Market orders, on the other hand, are matched immediately with the best limit orders available on the exchange, consuming liquidity. Limit orders can also consume liquidity; a limit buy placed at or above the market ask price will be immediately matched with the best available limit sell, thus removing the sell order from the exchange. Similarly, a limit sell placed at or below the market bid price will be immediately matched with the best available bid, as a market sell would.

Like broker commissions, exchange fees are negotiated in advance of execution.

**Taxes** According to Benjamin Franklin, "In this world nothing can be said to be certain, except death and taxes." Taxes are charged from the net profits of the trading operation by the appropriate jurisdiction in which the operation is domiciled. High-frequency trading generates short-term profits that are usually subject to the full tax rate, unlike investments of one year or more, which fall under the reduced-tax capital gains umbrella in most jurisdictions. A local certified or chartered accountant should be able to provide a wealth of knowledge pertaining to proper taxation rates. Appropriate tax rates can be determined in advance of trading activity.

#### **Latent Execution Costs**

**Bid-Ask Spreads** A bid-ask spread is the price differential between the market bid (the highest price at which market participants are willing to buy a given security) and the market ask (the lowest price at which the market participants agree to sell the security). Most commonly, the bidask spread compensates the market participants for the risk of serving as counterparties and cushions the impact of adverse market moves. A full discussion of the bid-ask spread is presented in detail in Chapters 6, 9, and 10.

Bid-ask spreads are not known in advance. Instead, they are stochastic or random variables that are best characterized by the shape of the distribution of their historical values. The objective of the cost analysis, therefore, is to estimate the distributions of the bid-ask spreads that can be used to increase the accuracy of bid-ask spread forecasts in future simulations and live trading activity.

To understand the parameters of a bid-ask distribution, the trader reviews key characteristics of bid-ask spreads, such as their mean and standard deviation. Approximate locations of the spreads based on historical realizations are made by computing statistical characteristics of spreads grouped by time of day, market conditions, and other factors potentially affecting the value of the spread.

**Investment Delay Costs** The cost of investment delay, also referred to as the latency cost, is the adverse change in the market price of the traded security that occurs from the time an investment decision is made until the time the trade is executed. The following example illustrates the concept of the investment delay cost. The trading strategy identifies a stock (e.g., IBM) to be a buy at \$56.50, but by the time the market buy order is executed, the market price moves up to \$58.00. In this case, the \$1.50 differential between the desired price and the price obtained on execution is the cost of the investment delay.

In systematic high-frequency trading environments, investment delay costs are generated by the following circumstances:

- **1.** Interruptions in network communications may disrupt timely execution and can delay transmission of orders.
- **2.** The clearing counterparty may experience an overload of simultaneous orders, resulting in an order-processing backlog and subsequent delay in execution. Such situations most often occur in high-volatility environments. In the absence of large-scale disruptions, delays due to high trading volume can last for up to a few seconds.

The cost of investment delays can range from a few basis points in less volatile markets to tens of basis points in very liquid and volatile securities such as the EUR/USD exchange rate. The investment delay costs are random and cannot be known with precision in advance of a trade. Distribution of investment delay costs inferred from past trades, however, can produce the expected cost value to be used within the trading strategy development process.

While the investment delay costs cannot be fully eliminated, even with current technology, the costs can be minimized. Backup communication systems and continuous human supervision of trading activity can detect network problems and route orders to their destinations along alternative backup channels, ensuring a continuous transmission of trading information.

**Price Appreciation Costs** The price appreciation cost refers to the loss of investment value during the execution of a large position. A position of considerable size may not be immediately absorbed by the market and may need to be "sliced" into smaller blocks.1 The smaller blocks are then executed one block at a time over a certain time period. During execution,

<sup>1</sup>Chan and Lakonishok (1995), for example, show that if a typical institutional trade size were executed all at once, it would account for about 60 percent of the daily trading volume, making simultaneous execution of the order expensive and difficult, if not impossible.

the price of the traded security may appreciate or depreciate as a result of natural market movements, potentially causing an incremental loss in value. Such loss in value is known as price appreciation cost and can be estimated using information on past trades. The price appreciation cost is different from the market impact cost, or the adverse change in price generated by the trading activity itself, discussed subsequently.

For an example of the price appreciation cost, consider the following EUR/USD trade. Suppose that a trading strategy determines that EUR/USD is undervalued at 1.3560, and a buy order of \$100 million EUR/USD is placed that must be executed over the next three minutes. The forecast turns out to be correct, and EUR/USD appreciates to 1.3660 over the following two minutes. The price appreciation cost is therefore 50 bps per minute. Note that the price appreciation cost is due to the fundamental appreciation of price, not the trading activity in EUR/USD.

**Market Impact Costs** Market impact cost measures the adverse change in the market price due to the execution of a market order. More precisely, the cost of market impact is the loss of investment value caused by the reduction in liquidity following market order–driven trades.

Every market order reduces available liquidity and causes a change in the price of the traded security. A market buy order reduces the available supply of the security and causes an instantaneous appreciation in the price of the security. A market sell order decreases the demand for the security and causes an instantaneous depreciation in the price of the security.

The market impact may be due to the imbalances in inventories created by the order, to the order pressures on the supply or demand, or to the informational content of the trades signaling an undervalued security to other market participants. Market impact is most pronounced when large orders are executed. Breaking orders into smaller, standard-size "clips" or "rounds" has been shown to alleviate the market impact. The properties of market impact can be described as follows:

- **1.** When the limit order book is not observable, ex-ante expectations of market impact are the same for buy and sell orders in normal trading conditions. In other words, in the absence of information it can with reasonable accuracy be assumed that the number of limit buys outstanding in the market equals the number of limit sells. However, if the limit order book can be observed, market impact can be calculated precisely based on the limit orders present in the order book by "walking" the order through the order book.
- **2.** Market impact is proportional to the size of the trade relative to the overall market volume at the time the trade is placed.

- **3.** Market impact due to inventory effects is transient. In other words, if any price appreciation following a buy order is due to our executing broker's "digestion" of the order and not to market news, the price is likely to revert to its normal levels after the executing broker has finished "digesting" the order. Whether the market impact cost is transient or permanent depends on the beliefs and actions of other market participants.
- **4.** Market impact accompanies market orders only; limit orders do not incur market impact costs.
- **5.** The informational content of market impact is canceled out by opposing orders.

In ideal market conditions, the market impact cost is measured as the difference in the market price of the security between two states of the market:

- **State 1—**the order was executed; execution was initiated at time *t*0, and the execution was completed at time *t*1.
- **State 2—**the order was not executed (the market was left undisturbed by the order from *t*<sup>0</sup> to *t*1).

In real-life conditions, simultaneous observations of both the undisturbed market and the effects of the trade execution on the market are hardly feasible, and the true value of the market impact may not be readily available. Instead, according to Kissell and Glantz (2003), the market impact is estimated as the difference between the market price at *t*<sup>0</sup> and the average execution price from *t*<sup>0</sup> to *t*1:

$$MI = P_0 - \frac{1}{N} \sum_N P_{\tau, n}$$
 (19.1)

where *MI* stands for "market impact," *P*<sup>0</sup> is the market price immediately prior to execution at time *t*0, *N* is the total number of trades required to process the entire position size from *t*<sup>0</sup> to *t*1, and *P*τ,*<sup>n</sup>* is the price at which the *n*th trade was executed at time τ , τ ∈ [*t*0,*t*1].

While the costs of market impact are difficult to measure both preand post-trade, market impact costs can be estimated as a percentage of the total market liquidity for a given security. The higher the percentage of market liquidity the strategy consumes, the higher the adverse price movement following the trades, and the higher the market impact cost incurred by subsequent trades in the same direction.

Consumed liquidity can be approximated as a percentage of the observed market volume that is directly due to market-order execution. Since market orders are processed at the latest market prices, market orders consume available liquidity and create market impact costs that may make subsequent trades in the same direction more expensive. Limit orders, on the other hand, supply liquidity, are executed only when "crossed" by a market order, and generate little market impact at the time the order is executed. Limit orders, however, may fail to execute and present a significant risk in case the markets move adversely.

A combination of market and limit orders can help balance the costs of market impact with the risks of non-execution. The optimal proportion of market and limit orders may depend on the risk-aversion coefficient of the trading strategy: Almgren and Chriss (1999), for example, specify the market versus limit optimization problem as follows:

$$\min_{\alpha} \text{MICost}(\alpha) + \lambda \text{Risk}(\alpha) \tag{19.2}$$

where α is the trading rate calculated as a percentage of market volume due to market orders placed by the strategy, λ is the coefficient of risk aversion of the strategy, and *MICost* stands for the market impact cost function. As usual, a risk aversion of 0.5 corresponds to a strategy for a conservative wealth-preserving investor, while a risk aversion of 0 corresponds to a risk-neutral strategy that is designed to maximize returns with little consideration for risk. The optimization of equation (19.2) can be solved by plotting *MICost*/Risk profiles for various strategies; the resulting efficient trading frontier identifies the best execution strategies.

According to Kissell and Malamut (2005), market impact costs can also be optimized using dynamic benchmarking, often referred to as "pricescaling." For example, a "strike" price–scaling strategy dictates that there is an increase in the proportion of market orders whenever prices are better than the benchmark and a decrease in market orders whenever prices are worse than the benchmark. A feasible alternative strategy, known as the "wealth" strategy, posts limit orders during favorable prices and market orders during adverse market conditions to minimize exposure to the adverse changes in the traded security. A "plus" strategy maximizes the probability of outperforming a benchmark within a risk/return framework. Each of the price-scaling strategies is discussed in detail in Chapter 18.

In dark pools of liquidity and similar trading environments where the extent of the order book cannot be observed directly, Kissell and Glantz (2003) propose to estimate the cost of market impact using the following expression:

$$k(x) = \frac{I}{X} \sum_{j} \frac{x_j^2}{x_j + 0.5v_j}$$
 (19.3)

where  $I$  is the instantaneous market impact cost for security  $i, X$  is the order size for security *i*,  $x_i$  is the order size of the parcel of security *i* traded at time  $j$  (assuming that the total order was broken down into smaller parcels), and  $v_i$  is the expected volume for security *i* at time *j*. Equation  $(19.3)$  accounts for the trade size relative to the total inventory of the security; the smaller the size of an individual parcel order relative to the total market volume of the security, the smaller the realized market impact of the order. The 0.5 coefficient preceding the market volume at time j,  $v_i$ , reflects the naïve expectation of a balanced order book in the absence of better order book details; a guess of an equal number of buy and sell orders results in half the book being relevant for each trade parcel.

To estimate the ex-ante risk of the market impact for a portfolio of several securities due to be executed simultaneously, Kissell and Glantz  $(2003)$  compute liquidity risk as variance of the potential market impact as follows:

$$\sigma^{2}(k(x)) = \sum_{i} \left(\frac{I_{i}}{X_{i}}\right)^{2} \sum_{j} \frac{x_{ij}^{4} \sigma^{2}(v_{ij})}{4(x_{ij} + 0.5v_{ij})^{4}} \tag{19.4}$$

The term  $\sigma^2(v_{ij})$  in equation (19.4) refers to expected variance in volume of security  $i$  at time  $j$ .

Other approaches, such as proposed by Lee and Ready (1991), are available for estimation of potential market depth and the corresponding market impact when the true market depth and market breadth values are not observable.

**Timing Risk Costs** Timing risk costs are due to random, unforecasted price movements of the traded security that occur while the execution strategy is waiting to pinpoint or "hit" the optimal execution price. The cost of timing risk describes by how much, on average, the price of the traded security can randomly appreciate or depreciate within 1 second, 10 seconds, 1 minute and so on from the time an investment decision is made until the market order is executed. The timing risk cost applies to active market timing activity, usually executed using market orders. The timing risk cost does not apply to limit orders. Timing risk captures several sources of execution uncertainty:

- Price volatility of the traded asset
- Volatility of liquidity of the asset
- Uncertainty surrounding the potential market impact of the order

Like other costs that are due to the price movements of the underlying security, timing risk costs can be estimated from historical trade data. While the timing risk costs tend to average to zero, the costs nevertheless impact the risk profile of trading strategies with their volatility. The timing risk is modeled as a distribution, with the worst-case scenarios being estimated using the value-at-risk (VaR) framework.

**Opportunity Costs** The opportunity cost is the cost associated with inability to complete an order. Most often, opportunity cost accompanies limit order-based strategies, but it can also be present in market-order execution. The inability to fulfill an order can be due to one of several factors:

- The market price never crossed the limit price.
- The market did not have the liquidity (demand or supply) sufficient to fulfill the order at the desired price.
- The price moved away so quickly that fulfilling the order would render the transaction unprofitable, and the transaction was canceled as  $a \text{ result.}$
- The opportunity cost is measured as the profit expected to be generated had the order been executed.

#### **Cost Variance Analysis**

Cost variance analysis summarizes deviations of realized costs from the cost averages. The latest realized costs are compared against population distributions of previously recorded costs with matching transaction properties—same financial security, same strategy or portfolio manager, and same executing broker. Over time, cost variance analysis gives portfolio managers a thorough understanding of the cost process and improves the system's ability to manage trading costs during strategy run-time.

Suppose that a particular trade in USD/CAD driven by strategy  $i$  and executed by broker j generated cost  $\varsigma_{ij}$ , and that the population mean and standard deviation for costs of all USD/CAD trades on record generated by the same strategy  $i$  and executed by the same broker  $j$  is represented by  $\bar{\zeta}_{ij}$  and  $\sigma_{\zeta,ij}$ , respectively. Then the deviation of the realized cost from its population mean is  $\Delta \varsigma_{ij} = \varsigma_{ij} - \bar{\varsigma}_{ij}$ . Whenever the deviation of the realized cost from population mean falls outside one standard deviation,

$$\Delta\varsigma_{ij}\notin[\bar{\varsigma}_{ij}-\sigma_{\varsigma,ij},\bar{\varsigma}_{ij}+\sigma_{\varsigma,ij}]$$

the reason for the deviation should be investigated and noted.

Often deviations can be due to unusual market conditions, such as an unexpected interest rate cut that prompts exceptional market volatility. High-cost conditions that occur independently of unusual market events may signal issues at the broker-dealer's and should be paid close attention.

#### **Cost Analysis Summary**

While transparent costs are readily measurable and easy to incorporate into trading models, it is the costs that are latent and unobservable directly that have the greatest impact on trading profitability, according to Chan and Lakonishok (1995) and Keim and Madhavan (1995, 1996, and 1998), among others. Understanding the full cost profile accompanying execution of each security improves the ability to successfully model trading opportunities, leading to enhanced profitability of trading strategies.

#### **POST-TRADE PERFORMANCE ANALYSIS**

#### **Efficient Trading Frontier**

Transaction costs may vary from strategy to strategy, portfolio manager to portfolio manager, and executing broker to executing broker. Some strategies may be designed to execute in calm market conditions when slippage is minimal. Other strategies may work in volatile markets, when latency impact is palpable and makes up the bulk of transaction costs.

Performance can be further compared to differentiate value added and non–value added execution. Almgren and Chriss (2000) propose that the evaluation of execution be based on the "efficient trading frontier" methodology. Reminiscent of the efficient frontier of Markowitz (1952) used in portfolio optimization, the efficient trading frontier (ETF) identifies the lowest execution cost per level of market risk at the time the order was executed. The ETF is computed for each security, strategy, executing broker, and cost type. Figure 19.1 illustrates this idea.

The efficient frontier is traced across all executed transactions in a given security; it can be broken down by type of the transaction cost, strategy, executing broker, and so forth. The goal of the exercise is to use execution with the most optimal trading frontier going forward. Depending on the scope of the analysis, the transaction cost can be measured as the implementation shortfall (IS) (discussed further along in this chapter) or as an individual cost component as shown in Table 19.1. The market risk at the time of execution can be measured as the volatility of an aggregate market index, such as the S&P 500. Alternatively, the market risk at the time of execution can be specific to each security traded and can be measured in the following ways: as a historical volatility of the mid price over a prespecified number of seconds or minutes, or as a size in bid-ask spread during the time of execution, among other methods. The bid-ask spread, while easy to estimate from the historical data, may be a biased measure specific to the executing broker (some brokers have higher

![](_page_23_Figure_1.jpeg)

Market risk at the time of execution

![](_page_23_Figure_3.jpeg)

spreads than do other brokers throughout the entire spectrum of market conditions).

In Figure 19.1, the efficient trading frontier is traced by trades A and B. Trade C is not efficient, and the causes of the deviation of trade C from the efficient trading frontier should be investigated. If trades A, B, and C are recorded for the same security and strategy but different executing brokers, the costs of the broker responsible for trade C should be addressed, or the bulk of trading should be moved from the broker that traded C to the brokers that traded A and B.

#### **Benchmarked Analysis**

In the benchmarked analysis, the dollar value of the executed position is compared to the dollar value of the position executed at a certain price, known as the benchmark price. The benchmarks typically fall into one of the following categories:

- Pre-trade
- Post-trade
- Intra-trade

The pre-trade benchmarks are known at the time the trading begins and are usually the market prices at the outset of the trading period—or, for lower trading frequencies, the daily opening prices. Pre-trade benchmarks may also be based on the trade decision price, the price at which the trading system makes the decision to execute the trade. Benchmarking to the trade decision prices is often referred to as "implementation shortfall," and is discussed in detail later in this chapter.

The post-trading benchmarks can be any prices recorded after the trading period. A market price at the end of an intra-day trading period can be a post-trading benchmark, as can be the daily close. Perold (1988) points out that to the extent that the trading system places trades correctly—buys a security that rises through the remainder of the trading period, for example—comparing execution price with the closing price for the trading period will make execution look exceptionally, but unjustifiably, good.

Intra-trading benchmarks include various weighted price averages. The most popular benchmarks are the volume-weighted average price (VWAP, pronounced "vee-wop") and the time-weighted average price (TWAP, pronounced "tee-wop"). Other benchmarks include averages of the open, high, low, and close prices (OHLC) within the given trading interval that are designed to proxy for the intra-period range of price movement and measure the algorithm's capability to navigate volatility.

Both the VWAP and the TWAP benchmarks can be based on daily, hourly, or even higher-frequency price data surrounding the trade. The VWAP for a particular security *i* on day *T* is computed as follows:

$$VWAP_{i} = \frac{\sum_{t} v_{it} p_{it}}{\sum_{t} v_{it}}, \ \{t\} \in T \tag{19.5}$$

where v*it* is the volume of security *i* traded at time *t*, and *pit* is the market price of security *i* at time *t*.

VWAP is often thought to be a good indicator of market price throughout the period under consideration (a minute, an hour, a day, etc.). Execution geared to outperform VWAP typically succeeds at minimizing market impact, and VWAP-based performance measures reflect the success of cost minimization strategies. On the other hand, VWAP-based performance metrics do not assess the performance of strategies trying to minimize risk or other variables other than market cost.

TWAP benchmarking measures the ability of the execution algorithm to time the market. TWAP benchmark price computes the price that would be obtained if the order were split into equal-sized parcels and traded one parcel at a time at equally spaced time intervals within the designated trading time period:

$$TWAP_{i} = \frac{1}{T} \sum_{t=1}^{T} p_{it}, \ \{t\} \in T \tag{19.6}$$

where *pit* is the market price of security *i* at time *t*.

Finally, the OHLC benchmark is a simple average of the open, high, low, and close prices recorded during the trading period of interest:

$$OHLC_i = \frac{1}{4} \left( p_{it}^O + p_{it}^H + p_{it}^L + p_{it}^C \right), \ \{t\} \in T \tag{19.7}$$

where  $p_{it}^O$ ,  $p_{it}^H$ ,  $p_{it}^L$  and  $p_{it}^C$  are the market open, high, low, and close prices of security *i* during the time interval *t*. The OHLC benchmark incorporates the intra-period price volatility by including the high and low price values. The OHLC benchmark does not, however, account for volume or liquidity available on the market.

Kissell and Malamut (2005) point out that different investors may have natural preferences for different benchmarks. Value investors may want to execute at their decision price or better, mutual fund managers may need to execute at the daily closing prices to facilitate the fund's accounting, and others may prefer VWAP, the below-average price for the pre-specified trading period. It is informative to compare performance of an algorithm against all benchmarks.

Overall, Kissell and Glantz (2003) caution that the benchmarked evaluation of execution performance may not be thoroughly useful for the following reasons:

- 1. Benchmarked assessment does not lend itself to execution comparisons across asset classes, a comparison that may be desirable in assessing performance of different executing brokers.
- 2. Benchmarked assessments are geared to minimization of execution prices; other execution-related performance characteristics may be plausible optimization candidates.
- 3. Furthermore, according to Kissell and Glantz (2003), benchmarked assessment strategies can be manipulated to show better performance than is warranted by the actual execution, making the portfolio manager incur higher costs at the same time.

#### **Relative Performance Measurement**

To address the flaws of the benchmarked performance measurement, Kissell and Glantz  $(2003)$  propose "relative performance measurement" as an alternative to the benchmarked analysis. The relative performance measure is based on either volume or the number of trades and determines the proportion of volume or trades for which the market price throughout the trading time period (a minute, an hour, a day, etc.) was more favorable than the execution price. In other words, the relative performance measure assesses at what percentage of volume or trades throughout the specified period of time the trade could have been executed on even better terms than it was actually executed. Specifically, relative performance measure (RPM) is computed as follows:

$$\text{RPM}(\text{volume}) = \frac{\text{Total volume } | \text{ price better than execution price}}{\text{Total volume}}$$
$$\text{RPM}(\text{trades}) = \frac{\text{Total # of trades } | \text{ price better than execution price}}{\text{Total # of trades}}$$
(19.8)

According to Kissell and Glantz (2003), the relative performance measure allows a comparison of execution performance across different financial instruments as well as across time. Unlike the benchmarked approach that produces performance assessments in dollars and cents, the relative performance measure outputs results in percentages ready for crosssectional comparisons. For example, suppose we would like to compare performance of execution of two stocks, IBM and AAPL, within a given hour. Suppose further that the benchmarked approach tells us that IBM outperformed its VWAP by 0.04, whereas AAPL outperformed its VWAP by 0.01. The two measures are not comparable, as neither one takes into account the relative prices of the securities traded. The relative performance measure, on the other hand, produces the following numbers—50 percent for IBM and 5 percent for AAPL—and allows us to objectively deduce that AAPL execution maximized its market advantage during the trading window, while execution of IBM can be improved further.

#### **Implementation Shortfall**

The implementation shortfall (IS) measure due to Perold (1988) measures the efficiency of executing investment decisions. The IS is computed as the difference between the realized trades and the trades recorded in paper trading. The paper trading process usually runs in parallel with the live process and records all the trades as if they were executed at desirable price at optimal times.

The paper-trading system of Perold (1988) executes all trades at the mid-point between the market bid and ask quotes, ignoring all transaction costs (spreads, commissions, etc.). The paper-trading system also assumes that unlimited volume can be processed at any point in time at the market price, ignoring the market depth or liquidity constraints and the associated slippage and market impact. The IS metric then measures the cost of running the trading system in real market conditions as compared to the costs incurred in the idealized paper-trading environment.

As Perold  $(1988)$  notes, the observed IS can be due to several factors:

- Liquidity constraints
- Price movement due to information imputed in market prices
- Random price oscillations
- Latency in execution
- Market impact
- Commissions
- Fees
- Spreads
- Taxes

The IS delivers a bundled estimate of the component costs and the estimate is difficult to disaggregate into individual cost centers. As a result, the IS methodology of Perold (1988) has been subject to criticism. To measure the costs of execution with greater precision, Wagner and Banks (1992) and Wagner and Edwards (1993) adjust IS by known transaction costs.

Furthermore, the implementation shortfall analysis can help in calculating the cost of market impact. A paper-trading system run concurrently with production can note two types of orders in parallel:  $(1)$  market orders at the market prices when the order decisions are made and  $(2)$  limit orders when the market price crosses the limit price. Such analysis will help assess the probability of hitting a limit order for a particular strategy, as shown by equation  $(19.9)$ :

$$\Pr(\text{Limit Execution}) = \frac{\text{\# of Executed Limit Orders}}{\text{\# of Orders Placed}} \tag{19.9}$$

For example, if out of 75 orders placed as limit orders, only 25 were executed, the probability of executing a limit order for a given strategy is 33 percent.

The analysis will also help describe the opportunity cost of missing profits for limit orders that are never hit, as shown in equation  $(19.10)$ :

$$\text{Opp Cost per Limit Order} = -\frac{\sum \text{Gain}_{\text{Market Orders}} - \sum \text{Gain}_{\text{Limit Orders}}}{\text{\# of Orders Placed}}$$

$$(19.10)$$

Both the probability and the opportunity costs accompanying limit orders are useful tools in designing and updating future trading systems. The opportunity cost associated with a limit order failing to execute should be taken into account when deciding whether to send a particular order as a limit or as a market order. As usual, the decision should be based on the expected gain of the limit order, computed as shown in equation (19.11):

$$E[\text{Gain}_{\text{Limit Orders}}] = (\text{Opp Cost per Limit Order}) \times$$
  

$$Pr(\text{Limit Execution}) + (1 - Pr(\text{Limit Execution})) \times$$
  

$$\frac{\sum \text{Gain}_{\text{Limit Orders}}}{\text{# of Executed Limit Orders}}$$
(19.11)

An order should be executed on limit instead of on market if the expected gain associated with limit orders is positive.

For example, suppose that a particular trading system on average executes two limit orders for every three limit orders placed. In this case, Pr(*LimitExecution*) = 66.7 percent. In addition, suppose that every executed limit order on average gains 15 bps and every executed market order gains 12 bps. Then the opportunity cost on 100 orders placed can be computed as follows:

Opp Cost per Limit Order =

$$-\frac{12 \text{ bps} \times 100 \text{ orders} - 15 \text{ bps} \times 100 \text{ orders} \times 66.7\%}{100 \text{ orders}} = -2 \text{ bps}$$
$$E[\text{Gain}_{\text{Limit Orders}}] = (-2 \text{ bps}) \times 66.7\% + (1 - 66.7\%) \times 15 \text{ bps} = 3.67 \text{ bps}$$

The limit orders will continue being placed as limit orders (as opposed to market orders) for as long as *E*[GainLimit Orders] remains positive.

### **Performance Analysis Summary**

Both cost and performance analyses, performed post-trade, generate insights critical to understanding the real-life trading behavior of trading models. The results of the analyses provide key feedback ideas for improving existing trading methodologies.

# **CONCLUSION**

Post-trade analysis is an important component of high-frequency trading. At low trading frequencies, where the objective is to capture large gains over extended periods of time, transaction costs and variations in execution prices are negligible in comparison with the target trade gain. High-frequency trading, however, is much more sensitive to increases in costs and decreases in performance. At high frequencies, costs and underperformance accumulate rapidly throughout the day, denting or outright eliminating trading profitability. Understanding, measuring, and managing incurred costs and potential performance shortcomings become paramount in the high-frequency setting.

The issues of costs and execution-related performance are bound to become more pronounced as the field of high-frequency trading expands. With multiple parties competing to ride the same short-term price oscillations, traders with the most efficient cost and performance structures will realize the biggest gains.
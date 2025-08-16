# **Volume-weighted Average Price (VWAP)**

The volume-weighted average price (VWAP) and its close cousin, the time-weighted average price (TWAP), are commonly used measures of the average price of a security over a period of time. VWAP and TWAP are used by traders and other investment professionals as reference prices, an indication of the average transaction price over an interval of time. So, for example, if the TWAP of a security is \$10 on a given day and a trader had bought a sizeable block of shares at \$9.50, we might conclude that the trader had added value in that he or she obtained a better than a na¨ıve program that mechanically sends out orders in the market at a steady rate throughout the day.

## **Mathematical Definition**

More formally, the VWAP of a security over a specified trading horizon (e.g., from market open to close) is defined as the ratio of the total transaction value in that security (i.e., the sum, over all trades in the specified horizon, of the product of each trade's share volume and the corresponding price) to the total volume of shares traded (i.e., the sum of all shares traded in the trading horizon). When the trading horizon is typically a trading day, intraday or multiday VWAP measures are also computed. A related concept is the TWAP, defined as the average price over a particular time interval with no explicit volume weighting. Traders use TWAP over VWAP for securities where the temporal pattern of volume exhibits considerable variation, for example, in less-active securities.

Formally, given *N* trades in the relevant interval, let *S*1*,...,SN* be the shares transacted with corresponding prices *P*1*,...,PN* . Then, we have

$$VWAP = \frac{\sum_{i=1}^{N} P_i S_i}{\sum_{i=1}^{N} S_i}$$
 (1)  
$$TWAP = \frac{\sum_{i=1}^{N} P_i}{N}$$
 (2)

Subtleties in the computation of VWAP/TWAP include (i) the choice of volume definition (e.g., primary market volume or composite volume), (ii) the treatment of certain trades (e.g., block trades that might be negotiated off market), and (c) the decision whether to include volumes at the open and close of the market.

## **Uses**

VWAP is commonly used as an approximation to the price that could be realized by a trader who passively participates in trading activity. As such, the performance of traders can be measured by their ability to execute orders at prices better than the VWAP benchmark prevailing over the trading horizon.

The computational simplicity of the VWAP is a major factor in its popularity in measuring trade execution, especially in markets where detailed trade level data is difficult or expensive to obtain. VWAP can be misleading as a benchmark in certain situations where the trader's objective is to control the slippage from a given strike or decision price, or where the strategy is not passive. In such cases, for example, if the trader has short-term alpha, the mechanical application of a VWAP strategy (i.e., trading in parallel to historical volume patterns) can lead to significant opportunity costs in terms of slippage. VWAP is not appropriate when the trader's executions are large relative to market volumes. In this case, VWAP might conceal a large price impact because the trader's own trades constitute the bulk of the reported volume. Finally, if traders have discretion over whether to execute or not, the VWAP benchmark can be gamed by selectively timing executions.

An important application is to so-called VWAP strategies, typically algorithmic trading strategies that automatically break up an order and send trades to the market to match the historical volume pattern or profile (see, e.g., [1]) of a security. See, for example, [2] for a discussion of the uses of VWAP in trading strategies and algorithms. The goal of a VWAP strategy is to obtain an execution price close to the VWAP for the day. Some brokers also guarantee VWAP execution, essentially taking on the execution risk for a fee.

## **References**

- [1] Hobson, D. (2006). VWAP and volume profiles, *Journal of Trading*, **1**(2), Spring, 38–42.
- [2] Madhavan, A. (2002). VWAP Strategies, in *Transaction Performance: The Changing Face of Trading*, Handbook Series in Finance, B. Bruce, ed, Institutional Investor Inc.

## **Related Articles**

**Automated Trading**; **Execution Costs**; **Price Impact**.

ANANTH N. MADHAVAN
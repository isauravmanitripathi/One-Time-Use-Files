## **CHAPTER 15**

#### **Minimizing Market Impact**

*Algorithmic execution,* also known as *algo execution* or *smart order routing,* refers to a set of programmatic computer methodologies used to determine the optimal way to parcel and execute an order. An ideal execution algo would consistently execute the customer's buy order at the lowest price available during a given period of time and transmit the sell when the price is at its peak, delivering "best execution." Given the difficulties of precisely pinpointing the price lows and the highs within a period of time, a good algo produces a certain price improvement according to prespecified optimality conditions. The optimality conditions may be based on the trader's risk aversion, concurrent market state, the benchmark chosen by the trader, and a range of other features, discussed in detail for the remainder of this part of the book. The execution algorithms can be built "in-house" by a buy-side trader, purchased "off-the-shelf" from the algorithm provider, or licensed on a one-off execution basis from the trader's broker. The brokers may provide algos for a commission or in exchange for a portion of the cost savings delivered by the algorithm relative to some executional benchmark.

Algo execution evolved naturally from human-driven best execution practice. For decades, brokers competed for client order flow by promising unique ability to pinpoint market highs and lows, and to negotiate preferred terms for the clients. Algorithmic execution builds on the human broker practice in developing an automated human-free approach.

From the point of view of classical finance and the quantitative portfolio management, best execution algorithms exist to smooth out natural market imperfections.

# Why Execution Algorithms?

Execution algorithms have become essential for all investors, as execution algos help traders accumulate or liquidate large positions by breaking up

orders into pieces, and reducing market impact and visibility of orders. To avoid being "picked off" in the markets, algos deploying limit orders cancel many of the orders when the orders fail to execute. The orders are then resubmitted almost immediately, often at a price closer to the market.

Different algorithms have been shown to substantially lower execution costs, in different ways. Execution costs comprise exchange and brokerdealer fees, bid-ask spread, opportunity cost associated with nonexecution of a limit order, and market impact (MI), to name a few. According to Engle, Russell, and Ferstenberg (2007), for example, the costs delivered by an algorithm depend on the level of order aggressiveness the algo produces: passive orders "save" investor capital by avoiding the spread, yet may aggravate costs whenever passive orders fail to execute. Other design aspects of the algo, such as the timing of the order parcels and size of each parcel relative to the market depth, also impact the obtained execution costs.

In addition to net execution costs, traders may consider the costs associated with the risk of the algorithms. The risk of nonexecution can be the largest risk component in algorithmic execution, but can be minimized with market orders at the expense of higher execution costs, resulting from crossing the spread, higher MI, transaction costs, and so on. Other risk metrics used in algo execution may include variability of the execution price of order slices, and value-at-risk (VaR) measure designed to contain execution costs below certain maximum limit.

To compare the performance of several algorithms, Almgren and Chriss (2000) proposed the concept of an efficient trading frontier. Like the efficient markets frontier developed in the framework of the capital asset pricing model (CAPM), the efficient trading frontier provides a convenient graphical representation of performance of various execution algorithms per unit of risk incurred by each algorithm. A sample efficient trading frontier is shown in Figure 15.1. Analytically, it can be described as in equation (1):

![](_page_2_Figure_0.jpeg)

![](_page_2_Figure_1.jpeg)

<sup>(1)</sup> 

where

- *α* is a measure of order aggressiveness, for example, counting the number of ticks away from the market each child order is placed.
- *Cost*(*α*) is the aggregate expected execution cost, including expected market impact, for all child orders of the strategy executed at the aggressiveness level *α*.
- *Risk*(*α*) is the cumulative risk associated with all the child orders placed at aggressiveness level *α*.
- *λ* is the degree of risk aversion, specific to the trader. A risk aversion level *λ*=0 indicates a trader who does not care about the execution risk. A risk aversion level *λ*=0.5 indicates a fairly risk-averse trader.

# Order-Routing Algorithms

Order-routing algorithms are designed to seamlessly navigate various issues differences between securities markets and deliver investors a cost-effective

execution schedule that would fit the investors' risk profile. As such, the order-routing algorithms target the following objectives:

- Minimize execution costs
- Obtain best price
- Maximize execution speed
- Maximize trading size
- Minimize trade footprint

To minimize costs, algorithms select appropriate venues and market conditions. Venue selection can reduce the fee structure, and picking the right time to execute a trade can pick periods of low bid-ask spreads, and help reduce or eliminate slippage and subsequent market impact (more on these later). To obtain best price, sophisticated algorithms perform shortterm forecasting to ensure the sell orders are processed during times with higher market prices and vice versa. To maximize the execution speed for clients desiring to capture present market conditions, the algos seek venues with appropriate market participation and minimal trade impact. To maximize trading size and minimize trade footprint, the algos slice the order into a series of smaller parcels or "child orders," all according to the latest scientific advances and investor's preferences. Large trading size can be particularly important to funds with large positions or strategy capacity. Minimal footprint of the trade ensures minimal detection of the order by outside parties, and helps thwart traders attempting to infer the informational content of orders.

Performance of execution algorithms is typically measured relative to some benchmarks. A benchmark may be the closing price observed at the end of the trading day, an average of the daily open, high, low, and close prices, the daily open, or other, more complex metrics, such as several commonly used execution algorithms.

Algorithmic benchmarks and the daily close are most common algo benchmarks. The daily close is an easy reference for any investor building his forecasting models on daily data, as is often the case with low-frequency quantitative modelers. Daily data analysis is nearly always performed on daily closing prices, and the developed forecasts usually predict future daily closes, too. As a result, algos that consistently outperform the daily close are in high demand by traders of daily close–based models, who are willing

to pay a portion of their execution algo-induced gains to the algorithm provider.

Yet the betterment of the closing price is notoriously difficult to achieve. Unlike other benchmarks, closing prices are not at all known in advance, and the only way to approximate them ahead of time is to deploy short-term price-forecasting models. Short-term forecasting utilizes the high-frequency trading models discussed in Chapters 8-11, and requires thorough understanding of the complexities of HFT modeling. is difficult As a consequence, traders often deploy other common algorithms as suitable algo performance benchmarks.

The following sections discuss each of the objectives of algo execution in detail.

#### Minimize Execution Costs

Trading costs comprise several major components:

- Broker commissions, both fixed and variable
- Exchange fees
- Taxes
- Bid-ask spread
- Slippage
- Opportunity cost
- Market impact

## Obtain Best Price

The core principle of the best price trading is "buy low, sell high." Due to the natural price moves, the direction of the price can be difficult to predict, and advanced short-term forecasting models are required for the purpose.

The best price execution is further complicated by additional factors. Consider the following example. It is 9:30 a.m., and a client wants to buy 10,000 shares of IBM at most at the closing price recorded at 4:00 p.m. later that day. The naturally arising issues create the following questions:

Given the market uncertainty, what will the execution price be at 4:00 p.m. that day?

- The client's desired execution size is considerably bigger than normal trading size. Should the order be broken into smaller parcels? If so, how should the order be split?
- If the client's 10,000-share order is broken into smaller child orders, how frequently are the child orders executed?
- Each buy trade (sell trade) will deplete some of the liquidity on the offer side (bid side). The resulting liquidity gaps will lead to adverse prices for subsequent child orders. Can this effect, known as market impact, be eliminated or minimized?
- Other market participants may observe trading footprint of the client, and decide to trade in the same direction, further moving the price in an adverse direction. Can the trading footprint be minimized?

## Maximize Execution Speed

Fast execution helps capture current market conditions. Market orders can be executed most rapidly in the most liquid markets. To maximize the speed of execution of market orders, therefore, investors may poll various exchanges for their available liquidity, and send their orders to the exchange with the most liquidity first. Limit orders, however, are executed most rapidly in the least liquid conditions. As a result, limit orders are best executed on the markets with the fewest limit orders available. Figure 15.2 illustrates a sample process of polling multiple exchanges for their liquidity levels and selecting the proper exchange for a given order or order slice.

<span id="page-6-0"></span>![](_page_6_Figure_0.jpeg)

In the example shown in [Figure 15.2,](#page-6-0) there are three exchanges: Exchange 1 has available bid-side liquidity of 2,000 trading units (shares, contracts, and so on, available at the best bid); Exchange 2 has liquidity of 3,000 units; and Exchange 3 has available liquidity off 500 units only. To minimize his trading footprint, a trader placing market sell orders would first go to Exchange 2 and place an order for 3,000 or fewer units there. Placing an order equal to or smaller than the top-of-the book matching liquidity available at the exchange ensures that the market order does not move or only slightly moves the market, leaving little or no footprint.

After exhausting the top-of-the-book liquidity on Exchange 2, the market order trader would turn to the next most liquid exchange: in our example, this is Exchange 1, with the top-of-the-book bid-side liquidity equal to 2,000 units. The trader would then place his order on Exchange 1 for 2,000 units or less, and then proceed to Exchange 3 and trade against the available liquidity there.

A trader desiring to execute limit buy orders, however, would first place a limit order with Exchange 3, as that exchange has the lowest aggregate size of buy limit orders available at the best bid. The trader next would place a

limit buy order at Exchange 1, the exchange with the next lowest number of aggregate limit buy orders available at the top of the book. At this point, the limit order trader may or may not proceed to place a buy limit order at Exchange 2, currently the most competitive exchange for buy limit orders.

The underlying rationale for selection of the exchange is this: place limit orders wherever the limit orders are fewest, and place market orders wherever the limit orders are most numerous. Such process ensures that the orders have the highest probability of fast execution. The process is known as the minimal impact algorithm.

### Minimize Footprint

In addition to maximizing execution speed, the MI algorithm can be used to minimize trading footprint, or the disturbance registered in the markets following an order. The exact causes of the disturbance are discussed in Chapter 5. The intuition behind the disturbance can be explained as follows: every order is a credible signal as it reveals the trader's true beliefs committed to trader's capital. As a result, every order carries information about the current views of the trader. Other market participants may desire to trade on these views as well, without necessarily knowing the information content beyond the observed action of placing an order. In such situations, placing child orders of sizes comparable to the sizes available at the best bid or offer at different exchanges minimizes the resulting change in market quotes, and reveals the least information associated with each order slice.

## Maximize Trading Size

The ability to process large trading volume is critical to investors deploying sizable capital in their strategies. For example, a large pension fund needs to be able to buy and sell large quantities of securities without incurring much additional cost in order to successfully reallocate pension fund's positions. To maximize the trading size, the large trader may use a combination of market and limit orders in processing each individual order. To do so, a trader seeking to execute a large buy order may first exhaust the top-of-thebook ask liquidity on all accessible markets by sequentially polling for the

best ask size available, and placing the market buy orders matching or smaller than the best ask liquidity at each exchange, beginning with the most liquid one. Subsequently, the trader may switch to limit orders and increase the bid-side liquidity by placing the best top-of-the-book buy orders at all the exchanges, beginning with the least liquid and rotating among the exchanges in the direction of increasing bid-liquidity. [Figure](#page-8-0) [15.3](#page-8-0) illustrates such strategy.

<span id="page-8-1"></span><span id="page-8-0"></span>**[Figure 15.3](#page-8-1)** Maximizing Trading Size Implementation of Execution Algorithms

![](_page_8_Figure_2.jpeg)

Most researchers develop execution algorithms in the following sequence: 1. Researchers explore published and not-yet-published academic research in the area of optimal execution algorithm design and implementation. Some traders may be skeptical of using publicly available research, fearing that all known research has been arbitraged in the markets. In reality, a change in parameterization of the algorithm

may result in an algo with an entirely different, yet still valuable, output.

2. The researchers model the algorithm in econometric languages such as MatLab or R and, as a result, transition their code to faster programming languages like C++ or optimized Java.

3. The algorithm is tested on historical tick data utilizing assumptions and predictions about price movement generated by the algorithms, own orders.

4. If the previous step results in a satisfactory execution schedule and price, cost, and risk outcome, the algorithm is moved into production, where it is enabled to communicate in real time using quote-receiving and -sending languages such as FIX, ITCH, OUCH, FAST, and the like.

Slicing large orders is imperative: research of Chan and Lakonishok (1995), for example, shows that if a typical institutional trade size were executed all at once, it would account for about 60 percent of the daily trading volume, making simultaneous execution of the order expensive and difficult, if not impossible. The smaller "child" orders are then executed one slice at a time over a certain time period.

<span id="page-9-1"></span>According to Gatheral, Schied, and Slynko (2012), algorithmic execution can be broken down into three distinct layers, as shown in [Figure 15.4.](#page-9-0) The first layer, called the *macro trader,* allows us to answer the following questions:

<span id="page-9-0"></span>**[Figure 15.4](#page-9-1)** Layers of Algorithmic Execution

*Source:* Gatheral, Schied and Slynko (2012)

![](_page_10_Figure_0.jpeg)

- How to slice the order: What is the general rule behind the algo's order slicing mechanism?
- When the algo should trade: How frequently and at what time of the day should be algo initiate its child trades?
- In what size the algo should trade: How large should each child order be?
- For how long the algo should trade: What is the horizon of the algo? When does the algo stop?

The second layer, which can be described as the *micro trader,* defines additional properties for each child order. In particular, the micro trader is responsible for deciding whether to execute the child order as a limit or market order, and, for limit orders, what price to set.

Finally, the *smart order router* decides to which venues to send the child orders.

Over the past two years, significant progress has been made in developing mathematical solutions for best execution. The decisions of the macro trader, the micro trader, and the smart order router can all be tailored with great precision to the given market conditions. Optimal execution solutions can be classified into static and dynamic strategy groups. A static strategy is completely determined ahead of trading: it is based on past market conditions. A volume-weighted average price (VWAP) is an example of a static strategy. In contrast, a dynamic strategy is determined and refined

during the course of execution. As such, dynamic strategies depend on contemporary market conditions. A simple delta hedge is an example of a dynamic strategy. At first glance, dynamic strategies may seem to always outperform static strategies, since dynamic strategies respond to current market conditions and static strategies do not. In reality, certain static strategies perform well, but only under specific market assumptions.

The performance of both static and dynamic strategies is often compared using benchmarks, for example, the following simple metrics:

• Average realized price compares the actual prices per unit traded received under different algos:

$$(2)^{\overline{p}} = \frac{1}{\sum_{j}^{V} \sum_{j}^{V} p_{j} \,\forall j \in J}$$

where  $P_j$  is the realized price for slice or child order *j*, and  $V_j$  is the size of child order *j*.

- Pretrade price  $P_{0}$  is the market price prevailing at the time the order  $j$ was placed.
- Posttrade price  $P_{i,post}$  is the price of the security after the temporary liquidity effects, induced by trading stream, have disappeared. To identify  $P_{i,post}$ , Almgren et al. (2005) regress  $\Delta P_{t}$  on  $\Delta t$ , and pinpoint the time  $\Delta t_{\tiny post}$  when dependency of  $\Delta P_{\tiny \mbox{\tiny $t$}}$  on  $\Delta t$  ceases to be statistically significant. Then, the price  $P$  recorded at  $t_{post}$  is the  $P_{i,post}$ .
- Total trade size  $V=\Sigma V_i$  allows comparison of algorithms used to process large trading volumes relative to available liquidity. In such conditions, some algorithms may perform better than others.
- Similarly, volume-adjusted trade size  $V\!/\!V_{\tiny\textit{Daily}}$ , where  $V_{\tiny\textit{Daily}}$  is the total trading volume on a particular day, allows comparison of algorithms' ability to take advantage of available liquidity.

In addition, common benchmarks for evaluating performance of execution algos include other common execution algos, such as timeweighted average price (TWAP), percentage of volume (POV), MI, VWAP, implementations shortfall, and various intraday price benchmarks, discussed in subsequent sections of this chapter.

<span id="page-12-1"></span>According to Kissell and Glantz (2005), order execution benchmarks can be grouped into three broad categories: pretrade, intratrade, and posttrade. [Table 15.1](#page-12-0) summarizes this classification. The pretrade category includes benchmarks known ahead of execution, such as:

<span id="page-12-0"></span>**[Table 15.1](#page-12-1)** Order Execution Benchmarks

| Pretrade       | Intratrade | Posttrade    |
|----------------|------------|--------------|
| Decision price | VWAP       | Future close |
| Previous close | TWAP       |              |
| Opening price  | OHLC       |              |
| Arrival price  |            |              |

*Source:* Kissel and Glantz (2005)

- Trading decision price, the price at which the trader or portfolio manager decided was advantageous for trading.
- Previous day's close price, which can be used as a benchmark for traders working with daily.
- Daily open price.
- Arrival price, the price that was prevalent when the executing broker received the order.

The intratrade category includes the following benchmarks:

- VWAP, determined using intraday prices.
- TWAP, also determined on the basis of prices throughout the day.
- The average of daily open, high, low, and close prices (OHLC)

The posttrade category includes the future close, the price not known in advance.

## TWAP

TWAP attempts to conceal the order flow by breaking a large order into equally sized parcels, which are then sent out at equally spaced time intervals. Mathematically, TWAP executes a fixed portion 1/*T* of the order every predetermined unit of time. The resulting TWAP price is the arithmetic average of prices sampled at the regular unit time intervals:

$$\text{(3)} \quad \text{TWAP} = \frac{1}{T} \sum_{1}^{T} \text{Pt}$$

<span id="page-13-1"></span>The TWAP algorithm is illustrated in [Figure 15.5.](#page-13-0) When a trader chooses to execute a large order of size *S* using TWAP, the trader also needs to decide on the total number *N* of child orders or slices to execute, and the total execution time *T*. Next, an order slice of size *S/N* is sent to the market every *T/N* seconds, until the entire order of size *S* is processed. The total number of slices *N* and the execution time *T* are best determined using characteristics specific to the traded security. These characteristics may include historical variation in volume throughout the trading day, market depth at the beginning of execution, and a host of other variables. The overarching objective is to select slices small enough so that each child order does not significantly move the market, yet large or frequent enough so that the entire large order can be executed within a reasonable time *T*. The resulting TWAP order flow can be represented as in Figure 15.6, with each child order drawn as an arrow.

<span id="page-13-0"></span>![](_page_13_Figure_1.jpeg)

![](_page_13_Figure_2.jpeg)

#### VWAP

The VWAP algorithm is currently one of the most popular execution methodologies. The principle of VWAP is straightforward: break up a large order in such a way that VWAP child orders are larger when the trading volume is higher, and child orders are smaller when trading volume is lower. Higher trading volume is likely to provide larger pool of matching orders and result in faster and more cost-effective execution.

<span id="page-14-1"></span>To determine the execution schedule, the VWAP algorithm uses a map of historical averages of intraday volume variations, such as the one shown for equities in [Figure 15.7.](#page-14-0) The map is often computed using preceding month of trading data: for every 15-minute (or other duration) interval of the trading day, the VWAP map shows the average volume over the past trading month. With the VWAP map in hand, the sizes of the child orders are determined as follows: for every trading period throughout the day, the total order size *S* is scaled by the VWAP proportion of volume historically observed during that time period, as shown in equation (3). Figure 15.8 diagrams the VWAP algorithm.

![](_page_14_Figure_3.jpeg)

<span id="page-14-0"></span>**[Figure 15.7](#page-14-1)** Map of Historical Volume Averages for Futures *Source:* Almgren and Chriss (2000)

![](_page_15_Figure_0.jpeg)

The resulting benchmark VWAP price can be determined as follows:

$$VWAP = \frac{\sum_{\tau \in T} \overline{V_{\tau}} p_{\tau}}{\sum_{\tau \in T} \overline{V_{\tau}}}$$

The VWAP map is based solely on historical data and does not accurately reflect concurrent market conditions. Even so, on average, a VWAP algorithm can deliver an allocation of child orders that efficiently utilizes the intraday liquidity. Such relative success of VWAP is based on persistence of the intraday volume patterns: specific markets possess their own intraday volume variations that change little from one month to the next. For example, Figure 15.9 illustrates the hourly VWAP map for Eurobund futures, computed using data for April 2009 and April 2010. While the average hourly trading volumes in the Eurobund futures have grown from 2009 to 2010, the shape of the VWAP map remained largely the same: an uptick in volume at the open of the European and the U.S. trading sessions, followed by a lull post–U.S. lunchtime, followed by a spike of activity at the market close.

![](_page_17_Figure_0.jpeg)

**Figure 15.9** Persistence of Intraday Volume Distribution, Eurobund futures (FGBL) POV

According to the joint U.S. Commodity Futures Trading Commission (CFTC) and Securities and Exchange Commission (SEC) report on the causes of the flash crash (2010), it was the POV algorithm that created the mayhem in the markets on May 6, 2010. The examination discovered that the significant volatility in market prices first started to occur when "a large fundamental trader" initiated a trade of \$4.1 billion of E-minis with POV set at 9 percent of volume over the previous minute.

Figure 15.10 illustrates the algorithm behind the POV. Like TWAP and VWAP, the POV algorithm sends child orders at regular time intervals. Unlike TWAP and VWAP, the size of each POV child order is determined

dynamically and set to a fixed percentage of the trading volume recorded during a previous predefined period of time, for example, 10 minutes. The execution next continues until the entire large order is processed. The previous period's trading volume used in calculation of POV child order should exclude the volume generated by the POV trader himself:

![](_page_18_Figure_1.jpeg)

**Figure 15.10** POV Process

(6)

While the joint SEC and CFTC report did not mention whether the POV algorithm used by the large fundamental trader accounted for the volume generated by the trader himself, failure to account for his own volume would generate exponentially increasing child orders, and could have caused the crisis of flash crash proportions.

When properly programmed, POV has one distinct advantage over TWAP and VWAP: POV dynamically adjusts to present market conditions, instantaneously responding to such events as shifts in liquidity.

# Issues with Basic Models

TWAP, VWAP, and POV execution models discussed in the previous sections were developed in the 1990s and are still widely popular, but suffer from serious shortcomings:

1. These models can be shown to be optimal only in specific, not-verycommon market conditions.

2. The models are easy to spot with advanced mathematical tools.

# Optimality Conditions for Earlier Models

Under limited assumptions about market dynamics, like martingale pricing or arithmetic Brownian motion (ABM), TWAP, and VWAP can be shown to be optimal. Both martingales and ABM, however, assume that the market does not trend, a hardly realistic condition. One can also show that VWAP is optimal in rapidly trending markets, where the trend completely dominates short-term noise-induced volatility.

In most market conditions where both the trend and the volatility are sizable, however, these models lose their optimality. The later sections of this chapter describe the latest advanced execution models applicable to most market conditions.

## Security of Earlier Models

Popular models like TWAP, VWAP, and POV also lack security. The models' primary mission is to break up and hide the order flow in general markets. Due to the regular nature of the child orders these strategies send, their child orders can be surprisingly easy to spot with simple tools like autocorrelation and advanced tools like Fourier analysis.

TWAP, for example, does little to hide the order flow from anyone familiar with the basics of digital signal processing, a core study of electrical engineering that is often deployed to remedy scratched CDs. As shown in Figure 15.6, TWAP comprises the regularly spaced orders of identical size. To detect market TWAP orders in the stream of tick data, therefore, one needs to:

1. Tag all recent market trade tick data as either buys and sells as discussed in Chapter 4.

2. Separate all buy trade ticks into virtual "buckets" by trade size; do the same for sell ticks.

3. Within each bucket, identify trades that occurred at identical time intervals from one another.

This process can be continuously repeated in real time, allowing systems to predict the time and size of the next TWAP installment, and thereby eliminating the original purpose of TWAP orders.

VWAP may seem more secure as the trades are not uniform in size; instead, the VWAP trades are scaled by the time-specific trade volume or volatility observed during the previous trading day or averaged over the previous week or month. While such scaling may appear to prevent reverseengineering of VWAP order flow, in reality, VWAP flow can be just as transparent as TWAP.

<span id="page-20-1"></span>To see the limitations of security VWAP, consider an equity VWAP process as shown in [Figure 15.11.](#page-20-0) Descaling all the trade ticks observed by the same scaling volume or volatility function as the one used in the VWAP-generating process of Figure 15.8 transforms VWAP into TWAP, and subsequently enables TWAP-like identification of the order flow.

<span id="page-20-0"></span>![](_page_20_Figure_3.jpeg)

VWAP scaling functions used by different traders may differ by the number of days used in averaging either volume or volatility, as well as by the width of time bars over which the intraday averages are computed. Even so, repeating the descaling analysis over the complete order flow several times using different precomputed scaling functions will identify orders sent in with a given scaling function.

The order flow sent via POV algorithms can be similarly identified. Regular spacing of orders, coupled with predictable functional form of order sizes, gives away the order flow. In the case of POV, the functional form of order flow is dependent on the volume executed during the time elapsed since the previous POV order.

In response to such security issues, some market participants and brokerdealers randomize sizes and timing of orders to reduce transparency of the basic algos. While the randomization may restrict other market participants' ability to observe the order flow with the basic methodology described earlier, the orders will still be traceable with advanced digital signal processing techniques, such as Fourier analysis.

*Fourier analysis* is often used to identify repetitive signals "buried" in the noise. Digital Fourier analysis models are routinely used to restore scratched music CDs or to "correct" the slightly off-key voice of pop singers. Likewise, Fourier analysis can be used to detect slightly randomized order flow of basic algorithms.

The key concept in Fourier analysis is Fourier transform, a mathematical construct connecting time and frequency domains. Continuous (as opposed to digital) forms of the Fourier transform are specified as follows:

(7) 
$$f(x) = \int_{-\infty}^{\infty} F(k)e^{2\pi i kx} dk$$
$$F(k) = \int_{-\infty}^{\infty} f(x)e^{-2\pi i kx} dx$$
(8)

where *x* represents a time-based variable, and *F*(*k)* is a frequency-domain function. Figures 15.12 through 15.15 illustrate the capabilities of Fourier analysis. Figure 15.12 shows a simple continuous cyclical process that can be generated by a time-dependent sinusoid function with frequency of 50 Hz (hertz, or repetition of 50 cycles per second). Figure 15.13 shows the same process transformed with Fourier analysis. The perfectly repeating cycles in time domain become a single clear spike in frequency domain. Furthermore, the spike falls directly onto the frequency of the cycles: 50 Hz.

![](_page_22_Figure_0.jpeg)

#### **Figure 15.12** Sample Recurrent Process

![](_page_23_Figure_0.jpeg)

**Figure 15.13** Fourier Representation of the Process Shown in Figure 15.12

![](_page_24_Figure_0.jpeg)

**Figure 15.14** Signal Corrupted with Zero-Mean Random Noise

![](_page_25_Figure_0.jpeg)

<span id="page-25-1"></span>**[Figure 15.15](#page-25-0)** Single-Sided Amplitude Spectrum of *y*(*t*)

Figure 15.14 shows a different time-based function: two sinusoids generated at 50 Hz and 120 Hz corrupted by noise. The noise may represent a random stream of data, such as other traders' orders mixed in with the TWAP or VWAP. The cycles in Figure 15.14 are hard to identify just by eyeballing the chart. However, a pass through the Fourier transform delivers a clear representation of the periodicity, shown in [Figure 15.15:](#page-25-1) clear peaks at 50 Hz and 120 Hz dominate the frequency domain of this example. Similar ideas extend to identification of periodic order flow in the sea of "noise" orders, placing the usefulness of TWAP and VWAP into question.

<span id="page-25-0"></span>Over the past few years, advanced models have been developed to overcome issues embedded in TWAP, VWAP, and POV algorithms. The latest algorithms are discussed in the next section.

# Advanced Models

To use realistic market assumptions and to avoid transparency of order flow induced by the basic TWAP, VWAP, and POV algorithms, researchers have developed advanced models that work under normal market conditions with a mixture of trend and volatility. Under these conditions, it can be shown that the optimal trading strategy is the one that induces a constant rate of order book replenishment.

The order book replenishment refers to the process of repopulation of the book following a market order. [Figure 15.16](#page-26-0) illustrates an example of replenishment in a limit order book.

<span id="page-26-1"></span>![](_page_26_Figure_3.jpeg)

<span id="page-26-0"></span>![](_page_26_Figure_4.jpeg)

Stylized replenishment function assumes that the order book possesses a "shadow" form, a structure to which the book reverts after some liquidity has been taken away. The shadow order book is assumed to exist independent of the current price level—the shadow book slides up and down the price axis with the movement of the price. The reversion of liquidity in the order book to the book's shadow form is referred to as resilience of the book.

The order book's resilience,  $h(E)$ , is a function of the trading process and is specified as follows:

$$E_t = X_t - \int_0^t h(E_s) ds$$

where  $E_i$  is the aggregate size of limit orders available at  $p$  ticks away from prevailing market price *P* at time *t*,  $X_t$  is the aggregate order flow,  $E_0 = 0$ , and  $\Delta X = \Delta E$ , for  $0 \le t \le T$ . The function  $h(E)$  measures how fast the order book *p* ticks away from the market recovers following an order of size  $\Delta X_{p}$ , and satisfies the following properties:

- The function is strictly increasing in X, and
- The function is a locally Lipschitz function on  $[0,∞)$ :  $|h(x)-h(y)| \leq C|x-y|$ for all *x* and *y*, where *C* is a constant independent of *x* and *y*, and the function has a bounded first derivative  $\frac{d\mathbf{r}}{dx} < \infty$ . The trader's execution strategy  $X$  measures the amount of the total order still left to be processed in the market. As such,  $x_0 = X$  and  $x_T = 0$ . The trader's rate of trading is defined as

$$(10)^{v_t} = -\frac{\partial x_t}{\partial t}$$

Price process of the traded instrument,  $S_{i}$ , can be assumed to follow any continuous process. Independent of the shape of the price process  $S_{\nu}$ , the expected impact inflicted by strategy  $X$  on price  $S$  can always be measured as cost C:

$$C = \int_{0}^{T} S_t dx_t$$

The expected value of MI cost can be expressed via integration by parts as follows:

$$(12) \mathbb{E}[C] = \mathbb{E}\left[\int_{0}^{T} S_t dx_t\right] = \mathbb{E}\left[S_T x_T - S_0 x_0 - \int_{0}^{T} x_t dS_t\right]$$

The most recent stream of research on best execution has focused on developing optimal execution algorithms under the following rigorous assumptions:

1. Geometric Brownian motion, the specification most commonly used in modern asset pricing.

2. Generalized price functions that can be used to describe any empirically observed price evolutions in an MI framework.

This section reviews the latest models developed under the two price evolution models.

## When Price Follows Geometric Brownian Motion

Most security pricing models assume that prices follow geometric Brownian motion with price increments *dS<sup>t</sup>* exhibiting dependency on the contemporary price level *S<sup>t</sup>* , as well as incurring drift μ:

(13)

The vanilla execution cost function, not incorporating any risk optimization measures, can then be specified as follows (see Forsyth et al., 2011):

$$C = \eta \int_{0}^{T} v_t^2 dt + \lambda \sigma \int_{0}^{T} S_t^2 x_t^2 dt$$
(14)

where, as before, the optimal rate of execution is . Under the assumption of geometric Brownian motion, the costs and the resulting optimal solution of the cost minimization problem are dependent on the price of the price path. However, as Forsyth et al. (2011) show, many strategies lead to the almost identical outcome.

Euler-Lagrange equations produce the following closed-form solution for optimal cost-minimizing trading strategy:

$$x_{t}^{*} = \frac{T-t}{T} \left[ X - \frac{\lambda T}{4} \int_{0}^{t} S_{u} du \right]$$
  
(15)  

$$x_{t}^{*} = \frac{T-t}{T} \left[ X - \frac{\lambda T}{4} \int_{0}^{t} S_{u} du \right]$$
  
The resulting expected minimal cost,  

$$\mathbb{E} \left[ \mathbb{C}_{\min} \left( x^{*} \right) \right] = \mathbb{E} \int_{0}^{T} \left( \langle x_{t}^{*} \rangle^{2} + \lambda x_{t}^{*} \xi_{t} \rangle \text{d}x \right]$$
  
becomes  

$$\mathbb{E} \left[ C_{\min} \left( x^{*} \right) \right] = \frac{X^{2}}{T} + \frac{\lambda T X S_{0}}{2} - \frac{\lambda^{2}}{8\sigma^{6}} S_{0}^{2} \left( e^{\sigma^{2} T} - 1 - \sigma^{2} T - \frac{\sigma^{4} T^{2}}{4} \right)$$
  
See Forsyth et al. (2011) for derivation.

## When Price Follows a Generalized Market Impact– Based Function

While most now-traditional asset-pricing models, such as Black-Scholes, assume Geometric Brownian motion as the model accurately describing evolution of security prices, a new breed of models proposes to model short-term price changes closer to their empirical roots. In such models, the price level at time *t* is expected to evolve as follows (see Gatheral, 2011):

(17)

where the risk or noise component is the price-level independent . The impact of prior trading is quantified using the execution strategy *X* trading rate dynamics and the function measuring resiliency of the order book *h*(*E*<sup>t</sup> ). The expected execution cost can next be expressed as

$$\mathbb{E}[C] = \frac{1}{2} \int_{0}^{T} \int_{0}^{t} h(E_s) dX_s dX_t$$

To minimize expected cost [C], one is required to solve the following equation:

$$(19) \frac{\partial}{\partial t} \frac{\partial \mathbb{E}[C]}{\partial u_t} = 0$$

which can be interpreted as follows: the optimal value of cost requires cost invariance with trading rate. Since the cost is directly dependent on volume

impact  $E$ , the optimality condition requires that volume impact stays constant:

(20)  $E_t = const$ 

See Obizaeva and Wang (2005), Alfonsi and Schied (2010), and Gatheral (2011) for details.

### Case 1: Exponential Market Resiliency

When the market resiliency can be assumed to follow exponential form,  $h(E) = e^{-pt}$ , the equation (20) then can be rewritten as:

(21) 
$$S_{t} = S_{0} + \eta \int_{0}^{t} u_{s} e^{-\rho(t-s)} ds + \int_{0}^{t} \sigma dZ_{s}$$

from where the expected execution cost of a trading strategy  $X$  can be expressed as

$$\mathbb{E}[C] = \eta \int\limits_{0}^{T} u_t \int\limits_{0}^{t} e^{-\rho(t-s)} ds \, dt$$

To derive suitable conditions for  $E_{\nu}$ , Obizhaeva and Wang (2005) note that  $E_{\cdot}$  can be expressed as

(23) 
$$E_{t} = \int_{0}^{t} E_{0+} e^{-\rho(t-s)} ds$$

where  $E_{0}$  measures the residual impact of trading prior to the chosen time 0. Integration by parts then yields:

$$E_{t} = E_{0}e^{-\rho t} + \rho \int_{0}^{t} e^{-\rho(t-s)} ds$$
(24)

Normalizing  $E_{0}$  by  $E_{0} = 1$ , the optimality condition with constant volume impact becomes

$$(25) \ E_t = E_0 = 1$$

Equation  $(25)$  then translates into

$$(26) \frac{e^{-\rho t} + \rho \int_{0}^{t} e^{-\rho(t-s)} ds = 1}{e^{-\rho t} + \rho \int_{0}^{t} e^{-\rho(t-s)} ds = 1}$$

The original optimality condition for the execution cost [equation (21)] can then be expanded

$$(27)\frac{\partial \mathbb{E}\left[C\right]}{\partial u_{t}} = \eta \int_{0}^{t} u_{s} e^{-\rho(t-s)} ds + \eta \int_{t}^{T} u_{s} e^{-\rho(t-s)} ds = \eta \int_{0}^{T} u_{s} e^{-\rho|t-s|} ds = const$$

Substituting the volume impact component from equation (27) into equation (26) produces the following result:

(28) 
$$e^{-\rho t} + \rho \int_{0}^{t} e^{-\rho(t-s)} ds = \int_{0}^{T} u_s e^{-\rho |t-s|} ds$$

The optimal trading rate *u<sup>t</sup>* can then be determined as

$$(29) u_t^* = \delta(t) + \rho + \delta(t - T)$$

Equation (29) can be interpreted as follows: when the market resiliency function can be assumed to be exponential, the optimal execution strategy is composed of:

- A large block trade of size *δ* at the beginning of execution process.
- A large block trade of size *δ* at the end of execution horizon, *T.*
- <span id="page-31-1"></span>A continuum of TWAP-like small orders placed at trading rate *ρ*, where *ρ* is the parameter in the exponential market resiliency function, *h*(*E<sup>t</sup>* )=*e*-*ρ*t.

The resulting optimal execution strategy for *T*=1 and exponential market resiliency with *ρ* = 0.1 is illustrated in [Figure 15.17.](#page-31-0) Figure 15.18 illustrates optimal execution strategies for different trading frequencies.

<span id="page-31-0"></span>**[Figure 15.17](#page-31-1)** Optimal Execution in a Market with Linear Permanent Market Impact and Exponential Decay of Temporary Impact *Source:* Gatheral, Shied and Slynko (2011)

![](_page_32_Figure_0.jpeg)

#### Case 2: Power-Law Market Resiliency

When the market resiliency can be assumed to fit the power-law function, *h*(*E<sup>t</sup>* )=*t*-*γ*, the optimal strategy can once again be derived via the constant volume impact requirement, equation (30):

$$E_t = \int_0^T u(s) |t - s|^{-\gamma} ds = const$$

The optimal trading rate is then

(31)

with *γ* representing a parameterized constant from *h*(*E<sup>t</sup>* )=*t*-*γ*, and *δ* analytically determined from equation (32):

$$X = \int_{0}^{T} u(t)dt = \delta\sqrt{\pi} \left(\frac{T}{2}\right)^{\gamma} \frac{\Gamma\left(\frac{1+\gamma}{2}\right)}{\Gamma\left(1+\frac{\gamma}{2}\right)}$$
(32)

where gamma function is defined as for discrete *n*, and for continuous *z.* The resulting optimal strategy is continuous with large singular block trades at the beginning and the end of execution times 0 and *T.* The optimal execution schedule is illustrated in Figure 15.19.

#### **Figure 15.18** Optimal Execution with Exponential Resiliency for Different Trading Frequencies

*Source:* Obizhaeva and Wang (2005)

![](_page_33_Figure_2.jpeg)

![](_page_33_Figure_3.jpeg)

![](_page_34_Figure_0.jpeg)

#### <span id="page-34-1"></span>Case 3: Linear Market Resiliency

When the market resiliency fits a straight line until the markets are restored, the market resiliency function is described as  $h(E) = (1 - \rho t)^{+}$ , and the optimal strategy can yet again be deduced via the constant volume impact requirement, equation (33):

(33) 
$$E_t = \int_0^T u(s)(1-\rho|t-s|)^+ ds = const$$

The optimal trading strategy comprises harmonic block trades with notrading intervals between the blocks, as shown in <u>Figure 15.20</u>.

<span id="page-34-0"></span>**Figure 15.20** Optimal Execution in a Market with Linear Permanent Market Impact and Linear Decay of Temporary Impact *Source:* Gatheral, Shied and Slynko (2011)

![](_page_35_Figure_0.jpeg)

The aggregate execution schedule is broken down into 2*N* trades each of the size , so that the total trading size *X* satisfies (34)

# Practical Implementation of Optimal Execution Strategies

To determine the optimal order slices per the framework presented in the previous section, the execution trader can go through the following steps:

1. Estimate the empirical MI function.

2. Fit distributions of temporary and permanent MI of the traded security.

3. Derive optimal allocation on the basis of step 1.

4. Back test the execution strategy.

5. Put the strategy to use in real-life production environment.

The resulting strategies perform well in chosen market conditions.

# Summary

Algorithmic order execution is inseparable from today's markets. It is a necessary function that delivers considerable value to all investors, large and small. With plummeting technology costs, most investors today can afford to build and use advanced order routing and best execution algos, previously available only to a select few market participants. Services such as co-location provide added benefits of security and speed.

# End-of-Chapter Questions

1. The best offer on exchange A contains 300 units of instrument X, the best offer on exchange B contains 500 units, and the best offer on exchange C contains just 100 units. Your customer wants you to buy 550 units on his behalf. How would you break up the customer's order and send them to exchanges under the minimal impact algorithm?

- 2. What is TWAP? VWAP? POV? Explain.
- 3. What are the main shortcomings of TWAP, VWAP, and POV?
- 4. How can the disadvantages of TWAP, VWAP, and POV be remedied?
- 5. What is resilience of the order book?
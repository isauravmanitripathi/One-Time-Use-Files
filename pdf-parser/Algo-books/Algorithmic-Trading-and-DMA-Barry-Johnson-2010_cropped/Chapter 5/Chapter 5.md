![](_page_0_Picture_1.jpeg)

Trading algorithms are predefined sets of rules for execution, each targeting a specific goal, whether it is matching the VWAP or seeking liauidity.

#### Introduction $5.1$

An algorithm is basically a set of instructions for accomplishing a given task. Therefore, a trading algorithm simply defines the steps required to execute an order in a specific way. Brokers/vendors provide a range of trading algorithms, each with distinct goals. Some strive to match or beat a specific benchmark, or try to minimise overall transaction costs whilst others seek to trade more opportunistically. To achieve these goals, some approaches rigidly adhere to a given trading schedule whilst others are more dynamic, adapting to everchanging market conditions.

Although the individual rules may be quite straightforward, the wide array of different events and possibilities that must be catered for mean algorithms can rapidly become quite complex. A common way of tackling this complexity has been to split the problem in two. For instance, Vladimir Kazakov (2003) decomposes VWAP trading into determining the optimum trading strategy and then realising this with optimal execution. The strategy concentrates on the trading schedule and benchmark, whilst the execution focuses on choosing appropriate orders to achieve this. Similarly, Robert Kissell and Roberto Malamut (2005) propose breaking algorithmic trading down into macro and micro level decisions. Again, the macro level makes strategic choices, based on the overall objectives. The micro level considers more tactical details, such as the specifics of order submission.

As an example, let's take a simple order to buy 6,000 of asset ABC over the next hour and time-slice its execution so that we trade 1,000 every ten minutes. We can represent this task with some pseudo-code:

```
for timer = 1 to 6
      quantity = 1000trade (quantity)
      sleep(10 minutes)
```

This code will not win any awards, but it does highlight that we are following a specific trading schedule until the order is completed. Obviously, we can make the trading algorithm more sophisticated by incorporating historical data or live market conditions. For instance, the quantity could be based on the best bid or offer size rather than just setting it to 1,000.

Exactly how we trade is a separate decision, for which the  $trade()$  function simply acts as a placeholder. A variety of approaches might be adopted, so the  $trade()$  function could:

- always place market orders
- $\bullet$ always place limit orders
- dynamically choose the optimal order type based on market conditions  $\bullet$

By separating the execution logic from the trading pattern in this way, we can create a common set of functions, which we will refer to as execution tactics. These are then available for all trading algorithms, and may be used interchangeably. This makes it much easier to customise our trading strategies. For example, we might default to a more passive execution style, but then change to use a more aggressive one when we get behind target or when conditions become more favourable.

So trading algorithms deal with the big picture, they primarily focus on how best to break up the order for execution. At the micro level are the actual mechanisms for managing order submission. We shall cover such execution tactics in more detail in Chapter 9.

#### **Categorising algorithms** 5.2

Although there are a wide variety of trading algorithms out there, if we strip off the customisations, we can start to see a small set of core strategies that are commonly provided by most brokers/vendors.

One way of classifying these algorithms is based on the benchmarks that they use. For example, the benchmark for implementation shortfall algorithms is predetermined, whilst for VWAP it is dynamic, and Market-on-Close seeks to match a future closing price.

Another way of classifying algorithms is based on their fundamental mechanisms. Ian Domowitz and Henry Yegerman (2005a) describe these as a continuum, which ranges from unstructured strategies, such as liquidity seeking algorithms, to highly structured approaches, such as a VWAP algorithm. Jian Yang and Brett Jiu (2006) go on to extend this approach by splitting this continuum into three main categories, namely:

- Schedule-driven
- $\bullet$ Evaluative
- $\bullet$ Opportunistic

Purely schedule-driven algorithms follow a strictly defined trading trajectory, generally created statically from historical data. For instance, historical volume profiles have often been used to implement VWAP algorithms; they represent intra-day historical volume averages. These profiles may then be used as a template for how the order should be split over time.

At the other end of the spectrum, opportunistic algorithms are completely dynamic. They react to favourable market conditions, trading more aggressively to take advantage of them. Then as conditions become less favourable, they trade more passively, if at all. Hence, liquidity-seeking algorithms are a good fit for this category.

Evaluative algorithms represent the middle ground between these two extremes. Often they combine aspects of each approach. Indeed, Yang and Jiu (2006) suggest that at the macro level they may behave in a more schedule-driven fashion whilst at the micro-level they focus on balancing the trade-off between cost and risk. Algorithms targeting implementation shortfall are good fit for the evaluative category.

This mechanistic style of classification focuses more on how algorithms are implemented,

whereas a trader or investor makes their decisions based on set objectives or goals. To better reflect these we can adopt a slightly modified scheme using three main types, namely:

- Impact-driven
- $\bullet$ Cost-driven
- $\bullet$ Opportunistic

Table 5-1 shows some common trading algorithms grouped using these categories. It also shows some of the specific factors which trading algorithms are most affected by, or are sensitive to.

|               |                  |                               |              | Benchmark        | Sensitivity |           |
|---------------|------------------|-------------------------------|--------------|------------------|-------------|-----------|
| Type          | Key<br>focus     | Algorithms                    | Dynamic      | Pre<br>determine | Price       | Volume    |
|               | Time             | Time Weighted Average Price   | $\checkmark$ |                  |             |           |
|               |                  | Volume Weighted Average Price | $\checkmark$ |                  |             |           |
| Impact-driven | Volume           | Percentage Of Volume          |              | $\checkmark$     |             | $\bullet$ |
|               | Impact           | Minimal impact                | $\checkmark$ |                  | O           | O         |
|               |                  | Implementation Shortfall      |              | $\checkmark$     | 0           | 0         |
| Cost-driven   | Price/<br>Risk   | Adaptive Shortfall            |              | $\checkmark$     |             | 0         |
|               |                  | Market On Close               | /            |                  | 0           | O         |
|               | Price            | Price Inline                  |              | $\checkmark$     |             | O         |
| Opportunistic | Liquidity        | Liquidity-driven              |              | $\checkmark$     | 0           | O         |
|               | Ratio/<br>Spread | Pair / Spread trading         |              | $\checkmark$     |             |           |

• often o sometimes

### Table 5-1 Algorithm classification

Impact-driven algorithms aim to minimise the overall market impact. In other words, they try to reduce the effect trading has on the asset's price. Therefore, large orders will often be split into much smaller ones, trading them over a longer period. This is best typified by the VWAP algorithm.

Cost-driven algorithms try to reduce the overall trading costs. Therefore, they need to take account of market impact, timing risk, and even factors such as price trends. Implementation shortfall is therefore an important performance benchmark for these. Consequently, this has become the name of the most commonly used cost-driven algorithm.

Opportunistic algorithms, as with Yang and Jiu (2006), take advantage whenever the market conditions are favourable. So these algorithms are generally price or liquidity-driven or involve pair/spread trading.

Clearly, Table 5-1 is not a definitive list of every possible trading algorithm. To see a summary of the algorithms each broker offers both the A-Team Group (2009) and Advanced Trading<sup>1</sup> publish directories, which are readily available. Still, Table 5-1 covers most of the

<sup>&</sup>lt;sup>1</sup> Advanced Trading directories are available at www.advancedtrading.com/directories

basic different types of functionality. Generally speaking, more exotic algorithms may be constructed by using one (or more) of these core strategies as the basis. For example, pair trading may act as the core for some multi-asset class trading, which we will cover in more detail in Chapter 13.

Note that this chapter focuses on trading algorithms that might be used by institutions and investors. We shall also cover some of the potential arbitrage strategies in Chapter 13. However, in general, algorithms that are predominantly used for market making or highfrequency trading / statistical arbitrage are beyond the scope of this book.

Before we go through each of these classes of algorithm in more detail, the following section outlines some features that are common to all algorithms.

#### 5.3 Common features of algorithms

Algorithmic trading is evolving in a similar fashion to electronic trading. Initially, each broker offered standalone solutions, adopting their own style of naming and controls. Gradually, these have started to become more standardised as they have been integrated into Execution Management Systems (EMS) and Order Management Systems (OMS). This allows investors and traders to switch between vendors more easily. However, the constant evolution of new algorithms and the increasing need for customisation means that there will be a continual cycle of innovation and consolidation.

Despite their different goals, there is still a significant amount of commonality between trading algorithms. In particular, this may be seen for their parameters, which are their equivalents of the optional instructions we saw for orders.

## Algorithm parameters

Trading algorithms may be controlled by a range of parameters. These provide the algorithms with limits or guidelines; they can be algorithm specific or generic.

Specific parameters may be used to specify how much a VWAP algorithm may deviate from the historical volume profile, or the participation required for a percent of volume algorithm.

Generic parameters represent common details, such as when to start and stop and whether to enforce a limit price etc. The following list summarises most of the parameters that are commonly supported, although various names may be used:

Start/End Times: Algorithms generally accept specific start and end times, instead of conditions such as "good for the day". Some algorithms, mainly the cost-based ones, may derive their own optimal trading horizons, although the start and end times should still act as hard limits. Certain algorithms might require a minimum amount of time to trade, so orders with too short a horizon may be rejected. Note that when start or end times are undefined, defaults are usually applied: For end time, the default is usually the market close, whilst the start time will be now (or the market open). Also, remember that when using times it is important to check that they are transmitted and interpreted correctly, particularly for foreign time zones. For algorithms that support multi-day trading, the end date becomes equally important.

Duration: Some vendors may actually forgo end times, instead using a duration parameter.

*Must-be-filled:* Generally, trading algorithms aim for complete execution, excluding the

more opportunistic ones. Market conditions may mean that this goal cannot always be achieved. Hence, a must-be-filled parameter will ensure that the algorithm trades any residual amounts. Often this will invoke specialised finish up logic, which takes quite an aggressive approach to ensure completion. This may affect the overall cost/performance.

*Execution style:* Usually, this represents passive, aggressive or neutral trading. Aggressiveness is a function of both size and price, so an aggressive algorithm will often execute more quickly, but at a higher impact cost than a passive one.

*Limit price:* A hard price limit offers price protection just as it would for a limit order. This is particularly useful for algorithms that do not have an inbuilt sensitivity to price.

Volume limit (maximum): This prevents an algorithm from trading more than a certain percent of the actual market volume. If this is being used to prevent signalling risk, it may be better to use a minimal impact or a liquidity-driven algorithm.

Volume limit (minimum): Care needs to be taken when enforcing minimum levels of trading since it could have a substantial effect on market impact costs.

Volume limit (child): Some algorithms may even support limits on the size of any child orders that are split off, or even the number of orders that can be extant at any one time. Again, if this is being used to reduce signalling risk it may be better to switch to a minimal impact or a liquidity-driven algorithm.

*Auctions:* This flag may be used to specify whether the order may participate in opening, closing and any intraday auctions. There may even be parameters to state this as a percentage of the order size.

As algorithms develop, there will doubtless be new common parameters, but the above list gives an idea of their scope. In the following sections, each of the different classes of algorithm will be reviewed in more depth, as well as detailing any specific parameters. For consistency, we will generally use the same sample order, to buy 10,000 of a reasonably liquid asset ABC, for each algorithm.<sup>2</sup> This approach should make it easier to compare the trading algorithms.

#### Impact-driven algorithms 5.4

Impact-driven algorithms evolved from simple order slicing strategies. By splitting larger orders into smaller child orders, they try to reduce the effect trading has on the asset's price, and so minimise the overall market impact costs.

The average price based algorithms, namely TWAP and VWAP, represent the first generation of impact-driven algorithms. Although intended to minimise impact costs, their main focus is their respective benchmarks. These are predominantly schedule-based algorithms, and so they usually track statically created trajectories with little or no sensitivity to conditions such as price or volume. Their aim is to completely execute the order within the given timeframe, irrespective of market conditions.

The natural progression from these static approaches has been the adoption of more dynamic methods. This has also resulted in a gradual shift towards more opportunistic

 $\rm ^2$  Obviously, trading volumes are significantly different between asset classes. So an overall order size of 10,000 is small for most equities but quite large for some futures or bonds. However, the same principles apply regardless.

trading. Percentage-of-volume (POV) algorithms are based on the actual market volume rather than relying on statically created schedules. These have further evolved into minimal impact algorithms, which take a more stealthy approach, aiming for zero market impact.

## Time Weighted Average Price (TWAP)

The Time Weighted Average Price (TWAP) benchmark is an average price, which reflects how the asset's market price has changed over time. Therefore, trading algorithms that attempt to match this benchmark are usually based on a uniform time-based schedule. They are unaffected by any other factors, such as market price or volume. TWAP algorithms are the natural extension of the earliest time slicing based approaches.

## **Basic Mechanism**

The simplest version of a TWAP algorithm is based on time slicing. Figure 5-1 shows two such orders, each to buy 10,000 of asset ABC. Order 1 issues child orders for 500 every fifteen-minute period for 5 hours, whilst order 2 trades double that over half the time.

![](_page_5_Figure_6.jpeg)

Figure 5-1 Two example TWAP orders

Clearly, both trading patterns are extremely uniform, and independent of both market volume and price. Unsurprisingly, the idealised completion rate charts for both orders are straight lines, as shown in Figure 5-2.

Trading in such a predictable way can lead to considerable signalling risk. Indeed, the only thing the other market participants do not know is the total size of the order. Even if other participants do not "game" this strategy it can still suffer poor execution quality due to its rigid adherence to the time schedule, in particular when prices become unfavourable or the available liquidity suddenly drops.

Alternatively, we can use the linear nature of the target completion profile to adopt a more flexible trading approach. At any given time, we can determine the target quantity the order should have achieved just by looking up the corresponding value on the completion rate chart. For instance, a 2-hour TWAP should have 25% of the order executed after half an hour. So instead of following the strict time slieing pattern we could adopt a slightly more random approach. By constantly comparing our progress with the ideal target quantity, we can then see how far behind (or ahead of) the schedule we are. Thus, we may now vary both the frequency and size of trading whilst still tracking the same target completion profile. This enables us to trade with a much less obvious trading pattern.

![](_page_6_Figure_2.jpeg)

Figure 5-2 Completion rate for sample TWAP orders

For example, Figure 5-3 shows a randomised TWAP order to buy 10,000 ABC:

![](_page_6_Figure_5.jpeg)

Figure 5-3 A more randomised TWAP order

The child orders are split randomly throughout the day, with some periods not even issuing an order. Table 5-2 shows how the traded quantities for each 15-minute period compare with the idealised targets. Sometimes the trading lags behind the target quantities, although it can also get slightly ahead of schedule, for instance at 8:15 and 9:45.

This may be seen more clearly in a comparison of the completion rate charts, as shown in Figure 5-4. Evidently, the randomised order still tracks the linear target completion rate quite closely, which gives it a good chance of matching the TWAP benchmark.

| Time         | 08:00 | 08:15 | 08:30 | 08:45 | 09:00 | 09:15 | 09:30 | 09:45 |  |
|--------------|-------|-------|-------|-------|-------|-------|-------|-------|--|
| Trade        | 300   | 400   | 50    | 200   | 300   | 400   | 200   | 450   |  |
| Total        | 300   | 700   | 850   | 1050  | 1350  | 1750  | 1950  | 2400  |  |
| Target total | 290   | 570   | 860   | 1140  | 430   | 1710  | 2000  | 2290  |  |
| Difference   | 10    | 130   | -10   | -90   | $-80$ | 40    | -50   | 110   |  |

Table 5-2 The trading pattern for a more randomised TWAP order

![](_page_7_Figure_5.jpeg)

Figure 5-4 Completion rate for a randomised TWAP order

This slightly randomised approach also allows more flexibility in the trading strategy, although it can increase the risk of missing the TWAP benchmark. It also enables a more dynamic approach, for example, we could adjust the order aggressiveness based on how far ahead or behind schedule we are. Hence, a more passive order placement strategy is possible, allowing for some degree of price improvement. In addition, this approach allows us to ignore unfavourable market conditions (small best bid/offer sizes, large price jumps), or even spurious ones which might correspond to gaming attempts. That said, such enhancements mean we are now trying to beat the TWAP benchmark rather than match it.

#### **Common variations**

Some versions may allow an additional factor to be applied to the trading schedule, which tilts it and so making it trade either more aggressively or more passively, as shown in Figure 5-5. A more aggressive stance will issue more orders early on, helping reduce timing risk, whilst a more passive approach should result in lower market impact costs.

A price adaptive TWAP algorithm might even adjust its schedule dynamically based on the market price (although arguably this makes it a simple price inline algorithm).

![](_page_8_Figure_1.jpeg)

Figure 5-5 Completion rates for a "tilted" TWAP

#### **Special Parameters:**

*Tracking:* Some variants may have custom parameters that allow control over how closely they track the target completion profile. This might just be an on/off switch or actual limits for how far it may go ahead (or behind) schedule (either as a percentage or possibly a cash value). This could even be inferred from an execution style parameter.

Interval frequency: Some versions may allow control over how frequently it trades and whether it uses randomisations to vary the intervals.

# Volume Weighted Average Price (VWAP)

The VWAP (volume weighted average price) benchmark for a given time span is the total traded value divided by the total traded quantity. As a benchmark, it rapidly became ubiquitous since it gives a fair reflection of market conditions throughout the day and is simple to calculate. This led to algorithms that tracked the VWAP benchmark becoming extremely popular.

## **Basic Mechanism**

As its name suggests, VWAP is a volume-weighted average, it corresponds to the overall turnover divided by the total volume. Given n trades in a day, each with a specific price  $p_n$ and size  $v_n$  we can express the daily VWAP as:

$$VWAP = \frac{\sum_{n} v_n p_n}{\sum_{n} v_n}$$

Thus, large trades will have more impact on the benchmark price than small ones. Whereas approximating the TWAP was simply a matter of trading regularly throughout the day, for VWAP we will also need to trade in the correct proportions. Though, since these are based on the day's trading volume we do not know beforehand what these proportions should be.

A common solution to this problem has been to use historical volume profiles. These are

averages of historical traded volume for fixed time intervals throughout the day. If the day is broken down into  $i$  periods then the daily VWAP may be expressed as:

$$VWAP = \sum_{j} u_{j} \overline{p}_{j}$$

where  $u_j$  is the percentage of daily volume traded and  $\overline{p_j}$  is the average price in each period. Robert Kissell and Morton Glantz (2003) show that the optimal trading schedule to meet the VWAP benchmark may be based on this percentage. In other words, the target quantity  $x_i$  for each period j is:

$$x_{i} = u_{i}X \tag{5-1}$$

where  $X$  is the total size of the order. Hence, we can use this equation to predetermine our ideal trading pattern. This approach has formed the basis for most VWAP algorithms. Note that it clearly assumes that the day's trading volume follows a similar pattern to the historical profile. Provided that the historical profile is based on sufficient data this is a reasonable assumption for many liquid assets. In Chapter 10, we shall discuss historical volume profiles in more detail.

Continuing with our example order to buy 10,000 ABC, Figure 5-6 shows a sample daily VWAP trading pattern. Notice that in this example the trading is dependent on the historical volume profile. It is not affected by the actual market volume or by price changes.

![](_page_9_Figure_7.jpeg)

Figure 5-6 An example VWAP order

To see how the trading pattern was determined, Table 5-3 shows the historical volume profile for each fifteen-minute period, together with the target size based on it. For example, from  $8:00$  to  $8:15$  the historical volume profile shows an average volume of 2,600, out of a total of 49,780. This corresponds to  $5.2\%$ , so using equation 5-1 and given that we are trading for the entire day then our target size for this time period is 520.

| Time      | 08:00 | 08:15 | 08:30 | 08:45 | 09:00 | 09:15 | 09:30 | 09:45 | 10:00 |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Hist Volm | 2600  | 2560  | 2700  | 2800  | 2500  | 2080  | 1560  | 960   | 640   |
| % of day  | 5.2   | 10.4  | 15.8  | 21.4  | 26.4  | 30.6  | 33.7  | 35.7  | 37.0  |
| Target    | 520   | 510   | 540   | 560   | 500   | 420   | 310   | 190   | 130   |
| Time      | 10:15 | 10:30 | 10:45 | 11:00 | 11:15 | 11:30 | 11:45 | 12:00 | 12:15 |
| Hist Volm | 400   | 440   | 360   | 280   | 400   | 480   | 400   | 520   | 320   |
| % of day  | 37.8  | 38.7  | 39.4  | 39.9  | 40.7  | 41.7  | 42.5  | 43.6  | 44.2  |
| Target    | 80    | 90    | 70    | 60    | 80    | 100   | 80    | 100   | 60    |
| Time      | 12:30 | 12:45 | 13:00 | 13:15 | 13:30 | 13:45 | 14:00 | 14:15 | 14:30 |
| Hist Volm | 480   | 480   | 640   | 800   | 960   | 1040  | 960   | 1120  | 1280  |
| % of day  | 45.2  | 46.1  | 47.4  | 49.0  | 50.9  | 53.0  | 55.0  | 57.2  | 59.8  |
| Target    | 100   | 100   | 130   | 160   | 190   | 210   | 190   | 220   | 260   |
| Time      | 14:45 | 15:00 | 15:15 | 15:30 | 15:45 | 16:00 | 16:15 | 16:30 |       |
| Hist Volm | 1400  | 1920  | 2200  | 2400  | 2600  | 2800  | 3000  | 3700  |       |
| % of day  | 62.6  | 66.5  | 70.9  | 75.7  | 80.9  | 86.5  | 92.6  | 100.0 |       |
| Target    | 280   | 390   | 440   | 480   | 520   | 560   | 600   | 740   |       |

Table 5-3 Volume profile data for an example VWAP order

Throughout the day, the trading algorithm then just needs to place sufficient orders in each interval to keep up with this target execution profile. Assuming this is achieved, the resultant chart of percentage completion is shown in Figure 5-7.

![](_page_10_Figure_4.jpeg)

Figure 5-7 Percentage completion for an example VWAP order

Modern VWAP algorithms often incorporate complex logic to determine whether they may get ahead of their schedule, and how best to catch up if they are behind their target. Overall, their performance is based on how well they track the target, but also on how well they predict market volume. Therefore, the way the historical volume profiles are compiled can also have a marked effect. Note for fragmented markets aggregated data may be used.

Broadly speaking, for this example the historical and actual market volumes are

reasonably similar, so our trading pattern should be a fair approximation for the day's VWAP (without accounting for market impact and other such slippage costs). Obviously, if the market volume is significantly different to the historical volume profile then performance may well suffer.

Another way of visualising this is to group the day's market volume by its price. For instance, using the same data from our example trade to buy 10,000 ABC, Table 5-4 shows the total market (and historical) volumes grouped by the average price for each hour of the trading day. From this, we can calculate an approximate VWAP for the whole trading day,

 $VWAP = Total Value / Quantity = 332360 / 60300 = 5.5118$ 

Instead of using the actual market volumes, we can also calculate a theoretical VWAP based purely on the volumes from the historical profile. This gives a VWAP<sub>hist</sub> =  $274400 /$  $49780 = 5.5123$ . Hence, in this example our historical volume profile is indeed an acceptable fit, using it to guide our trading patterns results in an average price within one basis point of the daily VWAP.

| Price          | 5.49 | 5.495 | 5.5  | 5.505 | 5.51  | 5.515 | 5.52  | 5.525 | Σ     |
|----------------|------|-------|------|-------|-------|-------|-------|-------|-------|
| Mkt<br>Volm    | 600  | 2000  | 4700 | 14200 | 11300 | 8600  | 11600 | 7300  | 60300 |
| Hist<br>Volm   | 480  | 1360  | 3280 | 10780 | 10000 | 7660  | 9720  | 6500  | 49780 |
| Ideal<br>Trade | 100  | 330   | 780  | 2350  | 1870  | 1430  | 1920  | 1210  | 10000 |
| Hist<br>Trade  | 100  | 270   | 660  | 2170  | 2010  | 1540  | 1950  | 1310  | 10000 |

Table 5-4 Market and historical volumes from example trade

## **Common variations**

The dependence on historical data means that VWAP algorithms can be vulnerable to sudden shifts in trading volume or liquidity. These can cause considerable deviations from VWAP. Therefore, some versions may also monitor current market conditions. Effectively, this makes them a hybrid between a static VWAP algorithm and the more dynamic volume participation approach.

Some variants may offer a more adaptive approach that tracks short-term price and volume trends and dynamically adjusts their target execution profile accordingly. Though, such customisations mean they are not really true VWAP algorithms anymore.

### **Special Parameters:**

*Tracking:* Some VWAP algorithms allow control over how closely they track the target completion profile. Usually, this is via custom parameters or just inferred from an execution style parameter.

Start time/End time: These can be specified to trade the VWAP for a specific interval; otherwise most algorithms will default to trading over the whole day.

*Trending/Tilting:* Generally, VWAP is an acceptable benchmark to trade towards if we have no specific view on the asset's price. But if we expect the price to trend throughout the day then this could prove to be an expensive option. Some versions may provide parameters that let the target execution profile be tilted towards either the start or the end of the day. A

more detailed example is given in Kissell and Glantz (2003). Note that it may also be worth considering an alternative algorithm in such cases.

# Percent of Volume (POV)

Percent of volume (POV) algorithms "go along" with the market volume; hence, they are also sometimes called volume inline, participation, target volume or follow algorithms. Ideally, the net result should be that if a million shares of XYZ trade in a day then a POV algorithm tracking a 20% participation rate should have executed 200,000 of those.

## Basic Mechanism

Unlike algorithms, such as TWAP and VWAP, where a trading schedule may be predetermined, for POV algorithms the trading schedule is dynamically determined. The algorithm tries to participate in the market at a given rate, in proportion with the market volume. For example, Figure 5-8 shows our example order to buy 10,000 ABC using a POV algorithm with a 20% participation rate. Notice that there is no relationship between the trading pattern and the market price. As Table 5-5 shows, the target trade size is driven solely by the observed market volume.

![](_page_12_Figure_6.jpeg)

Figure 5-8 An example POV order

| Time     | 08:00 | 08:15 | 08:30 | 08:45 | 09:00 | 09:15 | 09:30 | 09:45 |                   |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|-------------------|
| Mkt Volm | 3100  | 3000  | 3200  | 3600  | 2800  | 2000  | 1600  | 200   | $\bullet \bullet$ |
| Target   | 520   | 600   | 640   | 720   | 560   | 400   | 320   | 240   |                   |

Table 5-5 Market volume data for the example POV order

Also, notice that the order completes by 4pm. The POV algorithm completes as soon as the market volume allows, or at its specified end time (whichever is sooner). The percentage completion profile is shown in Figure 5-9. In comparison, a VWAP order will spread itself out to take all the available time. Broadly speaking, though, the POV trading pattern still looks fairly similar to the example VWAP order we saw in Figure 5-6. This is because the order represents around a fifth of the day's historical volume, and the historical and market volume profiles are fairly similar. So the example VWAP order from Figure 5-6 is almost a proxy for 20% participation.

![](_page_13_Figure_2.jpeg)

Figure 5-9 Percentage completion for an example POV order

It is important to note that although POV algorithms are dynamic, they still cannot predict market volume. They react to reported trades to keep in line with the observed volume. For instance, Table 5-6 shows a more detailed breakdown of the market trades for our example order, for the 8:15-8:30 time interval, with our executions highlighted.

| Time     | Trade<br>pricc | Trade<br>size | Accum.<br>market<br>volume | Target<br>position | Quantity<br>behind |
|----------|----------------|---------------|----------------------------|--------------------|--------------------|
| 08:16:02 | 5.56           | 500           | 500                        | 100                | 100                |
| 08:19:24 | 5.56           | 1000          | 1500                       | 300                | 300                |
| 08:23:09 | 5.57           | 200           | 1700                       | 340                | 340                |
| 08:25:15 | 5.55           | 400           | 2100                       | 420                | 20                 |
| 08:27:06 | 5.56           | 300           | 2400                       | 480                | 80                 |
| 08:28:26 | 5.56           | 400           | 2800                       | 560                | 160                |
| 08:29:21 | 5.56           | 200           | 3000                       | 600                |                    |

Table 5-6 A breakdown of the market trades for the example POV order

As we saw in Table 5-5, for this period the market volume is 3,000, of which we would like to be 600. Therefore, by 08:23 when 1,700 of ABC has already traded we would like to have seen 20% of this, or 340. Though, rather than respond to each individual trade we can set trigger points, for instance, we catch up at 08:25 by filling an order for 400. Note that since we are reacting to executed volume, when calculating our actual order sizes we need to adjust our participation rate slightly to account for our own trading. This is because when we see 1,000 has executed, if we then trade another 200, we have changed the overall volume, and so this will not actually be  $20\%$  participation any more:

Participation rate =  $200 / (1000 + 200) = 16.667\%$ 

Therefore, we can approximate the required trade size by using the adjustment factor  $1/(1-p)$ , where p is our participation rate. In the case of our example order, we actually need  $1/(1-0.2) = 25\%$  of each observed new trade (excluding our own trades). For example, when a trade of 1000 has executed, splitting a child order for another 250 gives:

Participation rate =  $250 / (1000 + 250) = 20\%$ 

This highlights a common concern about POV algorithms: If several are competing for an illiquid asset, they could start driving each other on, like two bidders in an auction desperate to buy the last lot. Potentially, this could lead to significant market impact. To try to protect from such situations firm price limits may be applied to POV orders, since the algorithm itself has no inhuilt price sensitivity. This will at least control the execution price, although it might well lead to the order failing to execute fully.

Another consideration is how the POV algorithm actually responds to reported volume. If it simply splits a new child order each time there is a trade then the resultant trading pattern is nearly as predictable as simple order slicing, as Tom Middleton (2005) highlights. To prevent such signalling risk we can keep track of the target volume and trade more periodically, as we do in the example shown in Table 5-6. Trading in this fashion allows us to vary the order placement, and adjust the aggressiveness of our execution tactics based on how far behind we are.

Similarly, although it is based on real-time data, POV can still be quite a reactive approach. Sudden volume surges are difficult to predict so even if the algorithm has been keeping ahead of the target participation rate, a sharp increase in volume will inevitably put it behind target. If the increase was due to a few large trades, it may well be too late to participate. Hence, most POV algorithms use a variety of safeguards to prevent themselves from chasing volume spikes, such as comparing the target trade size with the currently available volume on the order book. Some versions may allow control over the market volume calculations, either to exclude block prints or to set a maximum permissible trade size. Fragmented markets also complicate things, since there are multiple volumes to track.

As with VWAP algorithms, the performance of POV algorithms depends on the techniques they employ to track their targets. It must be remembered that one of the key goals is to minimise overall market impact. In practice, POV algorithms may well take account of other factors, such as liquidity, to help determine how best they should trade.

#### Common variations

Some POV algorithms may incorporate forecasting to try and better anticipate the upcoming trading volume. Generally, such approaches are based on a mixture of historical volume profiles, current observed volume and quantitative analytics.

Price adaptive versions of POV algorithms are also starting to appear. These adjust the participation rate based on how the current market price compares to a benchmark. Some variants can even adapt to the relative price changes for other assets, such as sector or market indices or even ETFs.

Corporate buyback programs in the U.S. often use the "safe harbour" provision granted by the SEC's Rule 10h-18, which protects issuers against liability for market manipulation. This mandates strict timing, price and volume conditions, designed to minimise the market impact of repurchases. Some brokers/vendors provide dedicated corporate buyback algorithms that adhere to these requirements. Often these are in fact based on modified POV algorithms. One of the key changes is to add a price condition that ensures the algorithm does not issue orders that end up making the market, so they do not allow their child orders to be priced more than the last trade or the current best bid.

#### **Special Parameters:**

*Participation rate:* Clearly, this percentage is the key parameter for POV algorithms.

Tracking: Some POV algorithms allow control over how closely they track the target participation rate. It may even be possible to dictate how far ahead and behind it can get, so we might allow it plenty of leeway for being ahead, but almost none should it fall behind. Effectively, this becomes a tilting mechanism for the target participation rate. Also for variants that allow a more dynamic adjustment of the participation rate there will need to be additional parameters, which allow us to specify what the benchmark is and exactly how the participation rate should change in relation to this.

*Volume filters:* These help prevent the algorithm needlessly chasing volume. Some versions allow block trades to be excluded; alternatively maximum trade size limits may be set. In the U.S., some vendors even allow control over whether the volume being tracked is from the primary exchange or a composite volume total for all the common execution venues.

*Start time:* Note that POV algorithms only track market volume while they are active, they will not try to catch up with volume traded since the open.

*End time:* Since POV algorithms are driven by market volume not by a schedule, their actual end time is variable. The end time just acts as a firm limit, although there is no guarantee that the order will be completed by then. Conversely, if the market volume spikes then the order could complete sooner than expected.

*Must-be-filled:* As we saw for end time, the variable nature of POV means that we need to flag if 100% completion is required. This allows the algorithm to change its trading style when it is running out of time.

Limit price: POV algorithms have no intrinsic price dependency; therefore, a firm price limit may be used. Note that although POV algorithms normally track all trading volume when a limit price is applied it should ignore any trades that are out of range of this limit. Otherwise, every time that the price moves back within the limit it will behave as if there had been a sudden volume spike.

*Execution style:* Some POV algorithms may support an execution-style parameter, which allows fine-tuning of its trading behaviour. A more passive approach may be used to try to achieve price improvement, whereas an aggressive style will track the participation rate more closely. Essentially, this is another form of the tracking parameter. This choice may also be dictated by the asset's liquidity, for instance, for illiquid assets more aggressive trading may he necessary to prevent getting behind its targets.

## **Minimal impact**

Minimal impact algorithms represent the next logical progression from VWAP and POV algorithms. Rather than seeking to track a market-driven benchmark they focus solely on minimising market impact.

Signalling risk is an important consideration for these algorithms. This represents the potential losses due to information that our trading pattern relays to the other market participants. It is dependent on both our order size and the asset's liquidity. Thus, algorithms focus on taking advantage of the facilities offered by "dark pool" ATSs and broker's internal crossing networks as well as using hidden order types to reduce this risk.

#### **Basic Mechanism**

The simplest version of a minimal impact algorithm is to route the entire order to a "dark pool" ATS and just leave it there. Although the actual hit ratios on some ATSs can be quite low, so many algorithms may also work a small portion of the order separately to ensure a reasonable level of execution. For example, we might leave 80% on the ATS and trade the remainder using a passive VWAP or POV algorithm, or even a liquidity-driven one. Alternatively, some variants may dynamically adjust the total size available on the ATS each time the algorithm decides to split of another child order. Note that for ATSs, which support conditional orders or IOIs, an indication could be left for the entire order whilst in parallel child orders could be worked in the markets. Therefore, the overall trading pattern is very much dependent on fills from the ATS. Hence, this is much more variable than some of the other algorithms we have already seen, so Figure 5-10 is just one possibility:

![](_page_16_Figure_4.jpeg)

Figure 5-10 An example minimal impact order

The sizable fills in Figure 5-10 correspond to successful crossings on the ATS, which are generally done at the mid price for the main market. The remaining fills correspond to trading on the main market and other venues.

Overall, the completion rate chart for this example looks fairly similar to the ones for the VWAP and POV algorithms, as Figure 5-11 shows. Note that for this example 80% of the order was filled from the ATS. If these fills had not occurred, the algorithm would have had to make up as much as it could on the other venues whilst still trying to minimise impact costs. Thus, it is possible that the order would only have partially completed.

![](_page_17_Figure_1.jpeg)

Figure 5-11 Completion rate for sample minimal impact order

#### Common variations

Some versions may incorporate models to estimate the probability of being filled on the ATS, using this to determine how much of the order should be left there. Likewise, impact cost models may be used to forecast the overall potential cost, which may then be used as a target benchmark. In many ways, there is a lot of crossover between these algorithms and those of the more cost-based ones, which we will review in the next section. Similarly, the stealth-based approaches used to reduce impact mean they share a lot of the same logic as the liquidity-driven algorithms, which we shall see in more detail in section 5.6.

### **Special Parameters:**

Visibility: How much of the order may actually be displayed at execution venues. No visibility implies the order is only worked in "dark pool" ATSs whilst low visibility ensures that only hidden order types or IOC orders are used at other venues.

*Must-be-filled:* The minimal impact algorithm is focussed solely on reducing this cost at the risk of failing to fully execute, much like a limit order. If there is a requirement to fully fill the order, it may be more appropriate to use a cost-hased algorithm instead.

#### $5.5$ Cost-driven algorithms

Cost-driven algorithms seek to reduce the overall transaction costs. As we saw in Chapter 2, these are much more than just commissions and spreads. Implicit costs such as market impact and timing risk are important components of the overall cost.

We have already seen that market impact may be minimised by splitting the trading over a long period of time. However, this exposes orders to a much greater timing risk, particularly for volatile assets. Therefore, cost-driven algorithms need to somehow reduce timing risk as well. Figure 5-12 highlights these differing requirements by plotting how the various costs change over time. Clearly, time has an opposite effect on market impact and timing risk.

![](_page_18_Figure_1.jpeg)

Figure 5-12 Trading strategy costs

In order to minimise the overall transaction costs we need to somehow strike a balance between market impact and the overall exposure to timing risk. As we saw in Chapter 1, this is what Kissell and Glantz (2003) refer to as the trader's dilemma: Trading too aggressively may result in considerable market impact, whilst trading too passively incurs timing risk. In order to strike the right balance we must also take into account the investor's level of urgency, or risk aversion.

Early cost-driven algorithms evolved from impact-driven ones by incorporating factors such as timing risk. Increasingly, though, cost-driven algorithms have been built from scratch using complex market models to estimate potential transaction costs and so determine the optimum trading strategy for each order.

Implementation shortfall represents a purely cost-driven algorithm. It seeks to minimise the shortfall between the average trade price and the assigned benchmark, which should reflect the investor's decision price.

Adaptive shortfall algorithms are just more opportunistic derivatives of implementation shortfall. In general, they are more price sensitive, although liquidity-driven variants are also starting to appear.

Market-on-close algorithms strive to beat an undetermined benchmark, namely the future closing price. Unlike TWAP or VWAP where the average evolves through the day, it is harder to predict where the closing price will actually be. Again, the key goal for this algorithm is to strike a balance between impact cost and timing risk. Effectively, it is the reverse of implementation shortfall: Instead of determining an optimal end time, we need to calculate the optimal starting time.

In the following sections, we will see how each of these handles our example order.

## Implementation Shortfall (IS)

Implementation shortfall represents the difference between the price at which the investor decides to trade and the average execution price that is actually achieved. Their decision price acts as the benchmark, although often it is not specified so instead the mid price when the order reaches the broker is used as a default.

#### Basic Mechanism

The aim of implementation shortfall algorithms is to achieve an average execution price that minimises the shortfall when compared with the decision price. As we saw in Figure 5-12, the key to accomplishing this is to strike the right balance between market impact and timing risk. Often, this means the algorithms tend to take only as long as is necessary to prevent significant market impact.

Since achieving this goal is more complicated, there is a lot more variety in how brokers/vendors tackle implementation shortfall compared to simpler algorithms. As Middleton (2005) reports, some of these algorithms are essentially enhanced versions of VWAP or POV algorithms. These use cost models to determine an optimal trading horizon, which is incorporated as either a model determined end time or an optimal participation rate. Modern versions have often been built from the ground up, to react more opportunistically to price and liquidity.

For simplicity, we shall focus on examples based on an optimal trading horizon. These may be split into two main approaches; one based on statically created trading schedules whilst the other adopts a more dynamic mechanism reacting to market volume.

The first step is to actually determine the optimal trade horizon, which needs to account for factors such as the order size and the time available for trading. It must also incorporate asset specific information such as its liquidity and volatility. In addition, we must also take account of the investor's urgency, or risk aversion. Quantitative models will then be used to take all these factors and derive the optimal trade horizon. Generally, a shorter trade horizon is due to:

- Assets with high volatility, also those with low bid offer spreads
- $\bullet$ High risk aversion
- Smaller order size, so less potential impact

We will cover the effects of these factors in more detail in Chapter 7. For the purposes of this section, we shall assume that our example asset ABC is liquid with a moderate volatility resulting in an optimal end time of 14:30 for an order to buy 10,000.

Having calculated the trade horizon our example static version will then determine the trading schedule, whilst the dynamic one will determine the most appropriate participation rate. Since their benchmark is predetermined, both approaches tend to favour trading more at the beginning of an order, while the price is closest to the benchmark, as Tracy Black and Owain Self (2005) note. Hence, a tilt factor may be used to try to shift the trading to the beginning, aiming to reduce the timing risk without causing excessive market impact.

Let's start first with the static version. Broadly speaking, this is similar to a tilted VWAP algorithm. Figure 5-13 shows the resultant trading pattern for an example order to buy 10,000 ABC.

The historical volume profile is used with the optimal end time to determine a basic trading profile. For our example, the historical volume information from 8:00 to 14:30 is used to generate new target percentages for this time window. These are shown for each interval in Table 5-7, labelled as "% of window". With fewer intervals, these targets are all higher, so whilst for the full day VWAP the interval from 8:45 to 9:00 accounted for 5.8% of the total historical volume, now it accounts for 9.4%.

Next, a tilt factor is applied to further increase trading at the start of order. For simplicity, we will use a factor that ranges from  $1.3$  down to  $0.7$  and decreases by  $0.1$  each hour.

![](_page_20_Figure_1.jpeg)

Figure 5-13 An example statically determined IS order

| Time        | 08:00 | 08:15 | 08:30 | 08:45 | 09:00 | 09:15 | 09:30 | 09:45 | 10:00 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Hist Volm   | 2600  | 2560  | 2700  | 2800  | 2500  | 2080  | 1560  | 960   | 640   |
| % of window | 8.7   | 8,6   | 9.1   | 9.4   | 8.4   | 7.0   | 5.2   | 3.2   | 2.2   |
| Tilt        | 1.3   | 1.3   | 1.3   | 1.3   | 1.2   | 1.2   | 1.2   | 1.2   | 1.1   |
| Target Volm | 1140  | 1120  | 1180  | 1220  | 1010  | 840   | 630   | 390   | 240   |
| Time        | 10:15 | 10:30 | 10:45 | 11:00 | 11:15 | 11:30 | 11:45 | 12:00 | 12:15 |
| Hist Volm   | 400   | 440   | 360   | 280   | 400   | 480   | 400   | 520   | 320   |
| % of window | 1.3   | 1.5   | 1.2   | 0.9   | 1.3   | 1.6   | 1.3   | 1.7   | 1.1   |
| Tilt        | 1.1   | 1.1   | 1.1   |       |       |       |       | 0.9   | 0.9   |
| Target Volm | 150   | 160   | 130   | 90    | 130   | 160   | 130   | 160   | 100   |

Table 5-7 Trading schedule extract for a static implementation shortfall

Although simplistic, it still gives a reasonable trading profile, as we can see from Figure 5-13, finishing just ahead of the optimal end time. Trading is more aggressive, especially for the first hour, and then it gradually tails off as market volumes decrease around midday.

For a more dynamic approach, the trading pattern may be based on inline participation with the market volume, as we saw for POV algorithms. In fact, an implementation shortfall algorithm using a dynamic mechanism may be likened to a tilted POV algorithm. Figure 5-14 shows an example IS trading pattern generated by a dynamic mechanism. Using the end time of 14:30 the historical volume profile suggests that usually around 30,000 has traded by then. Given our order size of 10,000, this implies an optimal participation rate of 33.33%.

Again, we can apply a simplified tilt factor to this, starting with  $+3\%$  and decreasing by a percent each hour. Table 5-8 shows some of the resultant targets. The target participation rate is also shown in Figure 5-15.

![](_page_21_Figure_1.jpeg)

Figure 5-14 An example dynamically determined IS order

| Time        | 08:00 | 08:15 | 08:30 | 08:45 | 09:00 | 09:15 | 09:30 | 09:45 | 10:00 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Mkt Volm    | 3100  | 3000  | 3200  | 3600  | 2800  | 2000  | 1600  | 1200  | 800   |
| % particip  | 36    | 36    | 36    | 36    | 35    | 35    | 35    | 35    | 34    |
| Target Volm | 1130  | 1090  | 1160  | 1310  | 990   | 710   | 570   | 420   | 270   |
| Time        | 10:15 | 10:30 | 10:45 | 11:00 | 11:15 | 11:30 | 11:45 | 12:00 | 12:15 |
| Mkt Volm    | 600   | 800   | 600   | 400   | 800   | 600   | 500   | 800   | 400   |
| % particip  | 34    | 34    | 34    | 33    | 33    | 33    | 33    | 32    | 32    |
| Target Volm | 210   | 270   | 210   | 130   | 270   | 200   | 170   | 260   | 130   |

Table 5-8 Trading schedule extract for a dynamic implementation shortfall

Note that the high participation rates are chosen to try to magnify the visual effect for this example. In reality, lower rates might often be used; otherwise, there could be considerable signalling risk and market impact. Spreading the order amongst multiple venues would also help.

Because the historical profile is a relatively good fit for the example asset's market volume, both the static and dynamic approaches give similar trading patterns, as can be seen by the similarity between Figure 5-13 and Figure 5-14. However, the dynamic version is more adaptable to changes in market conditions, and as we can see in Figure 5-15 it finishes earlier. This was because the actual market volume was higher than the estimate from the historical volume profile.

Admittedly, these examples use simplistic tilting mechanisms. Still, they both give reasonable approximations for how implementation shortfall algorithms work. Modern versions may employ much more complex logic; incorporating factors such as the asset's volatility or spread and the investor's risk aversion.

![](_page_22_Figure_1.jpeg)

Figure 5-15 Percentage completion for IS orders

To cope with changing market conditions, the trading horizon may be dynamically reoptimised if specific constraints, such as a limit price, are reached, as Middleton (2005a) suggests. The quality of the cost model is also a key determinant for the performance of any given version. In Chapter 10, we shall cover cost models in more detail.

Many of the newer generation of implementation shortfall (IS) algorithms were designed from the ground up, huilt around intricate market models, which can be used to predict transaction costs. Some may be based on optimal participation rates, although these are constantly adjusted based on market conditions and cost estimates. Other versions achieve the optimal trading strategy by constantly monitoring market conditions, and performing detailed cost analysis before each and every order is placed, as Niall McIntyre (2006) suggests. These more advanced versions cope much better with unexpected conditions. However, under general conditions their resultant trading patterns will probably still be reasonably similar to Figure 5-14.

#### **Common variations**

Adapting to market conditions, such as liquidity or price has become a key focus for many algorithms. Price adaptive implementation shortfall algorithms have become sufficiently important that the following sub-section is dedicated to them. IS algorithms which have access to "dark pools" of liquidity are also available.

Volatility is another key factor for IS algorithms. Some versions actually adjust to changes in short-term price volatility; when the volatility falls, they can afford to trade more passively. Other variants may also use alternative estimates for volatility. For example, Instinct's Wizard algorithm uses the implied volatility from the options markets as a more accurate gauge of intraday volatility.

## **Special Parameters:**

*Benchmark price*: This allows the investor to specify their decision price; otherwise, this generally defaults to the arrival price (midpoint) when the order was received.

 $^{3}$  In Chapter 10, we will see how short-term forecasts may be made for market conditions, such as price and volume.

Risk aversion: This represents an investor's level of urgency. A high-risk aversion suggests that the position is more subject to price risk, so the algorithm will use a shorter time horizon, adopting more aggressive execution tactics. Some versions may only support passive, aggressive or neutral, whilst others may allow a finer grained setting (say from 1-10).

*Execution style:* Essentially, this is replaced by Risk aversion, although for some variants it may actually provide the risk aversion setting.

*End time:* This acts as an absolute deadline. Though, as we have seen, many IS algorithms are driven by determining an optimal trading horizon. Note that it is important to check with pre-trade analytics/models that the specified end time is not actually before the optimal time, otherwise performance may suffer.

*Limit prices:* These are supported, but it is important to note that implementation shortfall algorithms are optimised to work towards their benchmark, which is the arrival price.

*Volume limits:* In order to minimise timing risk, IS algorithms often start by trading fairly aggressively. Their internal models are trying to balance potential market impact versus this risk. Placing too stringent a volume limit may actually affect the performance of the algorithm. If the volume limit is being used to reduce signalling risk then a minimal impact or liquidity-driven algorithm may be a better choice.

## Adaptive Shortfall (AS)

Adaptive shortfall represents a new subclass of algorithms derived from implementation shortfall. The adaptive moniker refers to the addition of adaptive behaviour; predominantly this is a reaction to the market price. Effectively, this means price adaptive shortfall algorithms behave more opportunistically.

A useful naming scheme for price adaptive algorithms was suggested by Robert Kissell, Andrew Freyre-Sanders and Carl Carrie (2005). This is based on the concept of price 'moneyness', taken from options nomenclature.

![](_page_23_Figure_9.jpeg)

Source: Kissell and Malamut (2005b)

Reproduced with permission from Institutional Investor

Figure 5-16 Comparison of price adaptation trading rates

Figure 5-16 illustrates this by plotting the target trading rate versus the market price for an example buy order. An aggressive in-the-money (AIM) strategy trades more aggressively with favourable prices and less when they become adverse. For a buy order, favourable conditions correspond to when the market price drops below the benchmark, with the opposite for a sell. So in Figure 5-16 its trading rate only increases when the market price falls significantly below the benchmark price  $(P<sub>b</sub>)$ . Whereas a passive in-the-money (PIM) tactic is the opposite, it becomes more passive when prices are favourable. Hence, in Figure 5-16 its trading rate only increases when the price rises significantly above the benchmark.

Note the Target strategy shown in Figure 5-16 is similar to a price-inline algorithm, since it does not account for timing risk, we will cover this further in section 5.6.

Another way of looking at price adaptive strategies is based on how they handle overall price trends. An AIM strategy assumes that trends are short-lived and will soon revert, whereas a PIM approach relies on the trend persisting. Thus, AIM trading will immediately try to take advantage of any favourable prices, and hope that unfavourable prices will revert. Conversely, PIM trading will react aggressively to stem any potential losses from an unfavourable trend, but it will be passive during favourable trends, hoping to achieve further price improvement.

#### Basic Mechanism

Essentially, this is still an implementation shortfall algorithm, so the basic behaviour will follow an IS approach. But in addition, the algorithm dynamically adapts to market conditions. Effectively, this is like having a tilt function that adjusts in real-time based on the current market conditions.

Initially, a baseline target for volume participation may be determined, based on the estimated optimal trade horizon. During trading, the adaptive portion is then used to modify this rate. The results for an example trade to buy 10,000 ABC using both AIM and PIM approaches is shown in Figure 5-17.

![](_page_24_Figure_7.jpeg)

Figure 5-17 Example price adaptive shortfall orders

Algorithm overview

With an AIM strategy, a favourable price trend will result in additional participation. Some variants may also apply a tilt to encourage earlier trading. For this example, the baseline participation was set as 30%, with the first hour raised to 35%. A short-term momentum indicator was used to vary this by up to 10%, dependent on the price and the trading strategy. Again, these participation rates are chosen to magnify the difference between the two approaches for this example. In reality, these would often be lower and the adjustment would probably depend on the asset's volatility. The effect this has on the target participation rate is shown in Figure 5-18. Clearly, as the price becomes increasingly favourable, from around 10:00, the AIM capitalises on this by increasing its participation rate, whilst the PIM strategy does the opposite. Then, from 11:00 to 12:00 when the price starts to rise again, the reverse happens. Finally, as both orders reach completion the participation rates tail off towards zero.

![](_page_25_Figure_2.jpeg)

Figure 5-18 Target participation rate adaptations

The overall completion rates may be seen in Figure 5-19. For this example, the market price showed more mean reverting behaviour rather than a consistent trend. Therefore, the aggressive in-the-money approach benefited from this, completing before the passive in-themoney strategy. Had this been a sell order we would have seen the opposite.

Overall, Kissell, Freyre-Sanders and Carrie (2005) found that the AIM strategy achieves better prices, but at a slightly higher risk. The PIM strategy is quicker to cut losses short so achieves a slightly lower risk, but may achieve poorer prices than AIM.

#### Common variations

Just as these algorithms react to the market price, we could also add behaviour that reacts to changes in the order book depth or overall liquidity measures. Increasingly, they are also accessing liquidity from "dark pool" ATSs.

## **Special Parameters:**

In general, adaptive shortfall algorithms will have the same parameters as implementation shortfall. Obviously, there is one key addition:

*Adaptation type:* Either aggressive in-the-money (AIM) or passive in-the-money (PIM).

![](_page_26_Figure_1.jpeg)

Figure 5-19 Percent completion for price adaptive shortfall orders

Note that unlike price inline algorithms there generally is not much provision for parameters to control exactly how much it reacts to actual price moves. This is because fundamentally it is based on an implementation shortfall algorithm. Even though it adapts to market prices, the optimal trading rate is still a function of its balancing market impact with timing risk.

## Market Close (MC)

The close price is often used for marking to market, and calculating net asset values and daily returns/profit and loss. Hence, many institutions are still interested in the close price as a benchmark. Though, trading at the close can be costly. David Cushing and Ananth Madhavan (2001) found prices are more sensitive to order flows at the close. They also noted price reversals after days with significant auction imbalances. Whilst call auctions have helped reduce the end of day volatility, the liquidity premium can still be considerable around the close.

#### **Basic Mechanism**

Clearly, the main issue for a market close algorithm is the fact that the benchmark is unknown until the end of the trading day. Unlike for VWAP or TWAP it is not an average based on the days trading, so we cannot simply slice the order into portions in an attempt to match the benchmark. If we start trading too early, we could be exposed to a substantial amount of timing risk, due to variability in the closing price. Whereas trading too late may cause significant market impact.

Many market close algorithms determine an optimal trading horizon using quantitative models, which incorporate estimates of an asset's volatility, and trading volume. So just as implementation shortfall algorithms determine an optimal end time market close algorithms can calculate an optimal start time, as Middleton (2005) points out. Figure 5-20 shows the resultant trading pattern for our example market close order.

Assuming a target participation rate of 30%, we therefore need 33,333 of ABC to trade. By working backwards our modified historical model shows that to meet this requirement we should start trading at 11:45, as we can see in Figure 5-20.

![](_page_27_Figure_1.jpeg)

Figure 5-20 An example market close order

Since market close orders are often submitted during trading hours this also enables us to see how today's market volume actually compares with the historical volume profile. For instance, from our example data the opening market volumes appear to be around 15% more than the historical values. Assuming this trend continues we can adjust our historical volume profile accordingly.

For this simple example, adjusting the historical volume profile by 15% gives a good match for the actual market volumes. By targeting a 30% participation rate our order comfortably completes, as shown in Figure 5-21.

![](_page_27_Figure_5.jpeg)

Figure 5-21 Percent completion for a market close order

In reality, we would need to constantly monitor the market volume and adjust the participation rate accordingly. In this example, the price trend is in our favour so there is no real need to tilt the participation rate. Clearly, this will not always be the case so we need to regularly estimate the impact of current market price trends and adjust our participation accordingly. Effectively, this is similar to what a passive in-the-money adaptive shortfall algorithm would do.

## **Common variations**

Some algorithms are now being termed departure price algorithms. These provide a more generic mechanism which will trade to any given end time, rather than just the market close. For example, should we want to ensure a position is achieved by midday we could set the end time accordingly and leave the algorithm to find the optimal start time.

## **Special Parameters:**

In general, market close algorithms will have similar parameters to implementation shortfall, although there are some obvious differences:

Risk aversion: A high risk aversion signifies that the trade is more subject to price risk and so should be traded more quickly. Still, in terms of a market close algorithm, this generally means an optimal start time closer to the market close. Therefore, if there is genuine price risk for an asset it may make more sense to use a shortfall algorithm rather than a market close one.

*End time:* As noted in the common variations, some versions allow control over the end time, giving a much more flexible approach.

Auction participation: There may also be parameters to specify the minimum and/or maximum order size allowed to participate in the close auction.

#### Opportunistic algorithms 5.6

Opportunistic algorithms have evolved from a range of trading strategies. They all take advantage of favourable market conditions, whether this is based on price, liquidity or another factor.

Price inline algorithms are essentially based on an underlying impact-driven strategy such as VWAP or POV. What they add is price sensitivity, which enables them to modify their trading style based on whether the current market price is favourable or not. So a focus on market impact has given way to a more opportunistic approach.

Similarly, liquidity-driven algorithms are an evolution of simpler rule-based order routing strategies. The trading is driven by the available liquidity, although cost is also a factor. Whilst pair trading is effectively a market neutral strategy, so risk is less of a concern. Instead, the key driver is when the spread or ratio between the assets is favourable.

Note that for each of these algorithms price is still an important factor. Target benchmarks provide a baseline that allows them to gauge whether the market conditions are favourable or not. Since they are so dynamic, opportunistic algorithms tend to be much more closely aligned to their underlying execution tactics than other algorithms, as we will see in Chapter 9. In the following sections, we shall examine each of the opportunistic algorithms in some more depth.

## Price inline (PI)

A price inline algorithm adapts its trading to the market price in a similar way to how POV algorithms adjust to market volume. A benchmark price is defined and trading is then altered based on how the market price compares to this. Note that if no benchmark is specified then the mid price when the order arrives is generally used instead. Clearly, a favourable price for a buy order means the market price is less than the benchmark, with the opposite for sells.

To describe its price-adaptation mechanism, we will reuse the price 'moneyness' naming scheme from Kissell, Freyre-Sanders and Carrie (2005). So, as we saw for Adaptive Shortfall algorithms, aggressive in-the-money (AIM) strategies trade more aggressively with favourable prices whilst passive in-the-money (PIM) tactics behave in the opposite manner. Note that usually when people refer to price inline algorithms they mean an AIM approach. but increasingly there are versions offering both types.

#### **Basic Mechanism**

A price inline algorithm consists of a basic trading mechanism combined with the price adaptive functionality. Hence, it could be based on a static VWAP algorithm or a more dynamic percent of volume approach. The actual price adaptation may directly track the difference between the market price and the benchmark, or it might even include other factors such as momentum.

Figure 5-22 shows a simple price inline algorithm, based on an underlying percent of volume strategy. The price adaptation is a straightforward adjustment to the participation rate based on the difference between the market price and the benchmark.

![](_page_29_Figure_7.jpeg)

Figure 5-22 Example price inline orders

The reverting price favours early completion by the AIM approach. We can see how the price changes affect the participation rate more clearly in Figure 5-23. As the price becomes increasingly favourable, from around 10:00, the AIM increases its participation rate, whilst the PIM strategy does the opposite.

![](_page_30_Figure_1.jpeg)

Figure 5-23 Target participation rate changes with price

These continue to oscillate inline with the price changes. Finally, as the AIM strategy reaches completion, its participation rate tails off to nothing. Figure 5-24 shows how this affects the overall completion rates.

![](_page_30_Figure_4.jpeg)

Figure 5-24 Percent completion for example price inline orders

As with the other algorithms, modern variants will differ in terms of they how they respond to being behind their target, and whether they permit going ahead of the target.

## **Common variations**

Some versions may even allow the price adaptation to be based on the price of other assets, sectors, market indices or even ETFs.

#### **Special Parameters:**

*Adaptation type:* Either aggressive in-the-money (AIM) or passive in-the-money (PIM).

*Benchmark price:* If the benchmark is related to another asset, index or ETF then details will also need to be provided for this to allow the algorithm to make a real-time price subscription for this.

*Participation rate:* For algorithms based on a dynamic POV type mechanism, a baseline participation rate will be needed.

*Participation adjustment:* This specifies how much to alter the participation rate by for a given price move, for instance, 5% every \$0.50. Note some versions may allow these to be asymmetrical, e.g.  $+5\%$  for favourable prices, but only  $-2\%$  for unfavourable ones.

*Price levels:* These specify the size of price moves for the participation adjustments, e.g. every \$0.50 or even every 20 basis points (bps). Again, some variants may allow these to be set separately for favourable and adverse conditions.

## **Liquidity-driven**

Liquidity represents the ease of trading a specific asset, so it has a considerable effect on overall transaction costs. Highly liquid assets tend to trade in greater volume, and so often will have lower spreads and more depth available. Whereas for illiquid assets, activity is much lower, the spread higher and order book may have little visible depth. So finding liquidity is an important means of reducing costs, particularly for illiquid assets.

Originally, liquidity-based trading simply meant making decisions based on the available order book depth, rather than just the best bid and offer. In today's fragmented markets liquidity-seeking has become more complicated. For example, the U.S. equity market has dozens of possible execution venues, with the number continuing to increase. In such an environment, visualising the available liquidity becomes non-trivial. If a trading strategy focuses on just one execution venue, there is a danger that it will miss opportunities on the other venues and so achieve a poorer execution price. Hence, for fragmented markets liquidity aggregation has become an important tool. Essentially, just as multi-broker systems pooled dealer quotes, we gather as much order book data as possible from every venue and aggregate these into a virtual order book. Figure 5-25 shows an example that pools the orders from the primary exchange (Exch-1) and several electronic crossing networks (ECNs) and "dark pool" alternative trading systems (ATSs).

Liquidity aggregation can be as simple as summing the available orders at each price point across all the different venues. For assets such as futures or options, this might also mean accounting for liquidity "implied" from more complex spread strategies. However, as we saw in Chapter 4, venues are increasingly adopting implied order types to make such liquidity more easily available. Still, there are some further complications such as fees and latencies. Venues have their own fee structures, so the algorithm needs to consider this when comparing prices. Latency is also an issue, since any time lag between our orders being sent and processed could significantly reduce the probability of execution.

Given that execution is not guaranteed, it is also important to deal with execution probability when choosing between venues. Notice that in Figure 5-25 the time field has been replaced by a percentage. This represents the overall probability of execution for that volume. For order E1, on ECN-1, we estimate a 70% chance of crossing with this order if we now dispatched an order to sell at 100. This percentage is based on a range of factors, including the probability of cancellation, latency and historical results.

Hidden liquidity is another important consideration. For hidden orders (shaded in Figure 5-25), the probability is primarily based on the likelihood of there being hidden volume at that price. Thus on ATS-1 order H3 corresponds to a 15% probability that this "dark pool"

|     | ATS-1   |       | Buys  |
|-----|---------|-------|-------|
| ld  | Prob %  | Size  | Price |
| 113 | 15      | 1.000 | 100   |
|     |         |       |       |
|     | $ATS-2$ |       | Buys  |
| ld  | Prob %  | Size  | Price |
| Α2  | 90      | 700   | 100   |
| 114 | 10      | 2,000 | 100   |
| 115 | 16      | 3,000 | 99    |
|     | $ECN-1$ |       | Buys  |
| ld  | Prob %  | Size  | Price |
| E1  | 70      | 1,000 | 100   |
| E2  | 70      | 3,000 | 99    |
| E3  | 70      | 500   | 98    |
|     |         |       |       |
|     | $ECN-2$ |       | Buys  |
| ld  | Prob %  | Size  | Price |
| 116 | 7       | 1.000 | 101   |
| E4  | 80      | 1,500 | 100   |
|     |         |       |       |

Figure 5-25 Aggregating order data from multiple venues

ATS has a hidden buy order for at least 1,000 ABC at 100. These are all then aggregated into a virtual order book, where the priority is based on price then probability (rather than time). Clearly, when placing orders, preference will be given to venues with the best price and the highest probability of execution.

Finding hidden volume is a case of continually tracking reported trades and matching these to the order book state. When trades are reported with a better price than the order book suggests, this may be due to hidden liquidity. For instance, Figure 5-26 shows the visible order book before and after trades for 2,000 ABC at 100 are reported.

|    | Buvs    |       |       |       | Sells  |               | Buys    |       |       |  |
|----|---------|-------|-------|-------|--------|---------------|---------|-------|-------|--|
| ld | Time    | Size  | Price | Price | Volume | ١d            | Time    | Size  | Price |  |
| B3 | 8:25:00 | ,000  | 100   | 101   | 800    | B3            | 8:25:00 | 1,000 | 100   |  |
| B4 | 8:25:25 | 500   | 100   | 102   | 1,500  | $\mathbf{B4}$ | 8:25:25 | 500   | 100   |  |
| B1 | 8:20:25 | 2,000 | 99    |       |        | B5            | 8:26:05 | 1,000 | 100   |  |
| B2 | 8:24:09 | ,500  | 98    |       |        | $\text{B1}$   | 8:20:25 | 2,000 | 99    |  |

(a) before

(b) after

#### Figure 5-26 Order book before and after trade reports for ABC

The buy orders B3 and B4 only account for 1,500 of the trade; so unless a new order suddenly arrived, 500 was potentially filled from a hidden order. Also, the new order B5 may be the display size for an iceberg order, or it may just be a new standalone limit order. Only by tracking the order book over a long period of time can we start to estimate which possibility is more likely. With more historical data, we can even start to predict what the hidden size might be, hence giving the sort of estimates we saw in Figure 5-25.

So by using historical data and closely monitoring the order book, we can create models for the estimation of hidden liquidity. We can then tailor our order placement strategy to try to take advantage of this. Usually, this is with immediate-or-cancel or fill-or-kill limit orders, so no standing orders are left on the limit book. Sometimes this is referred to as pinging for liquidity, much like a radar or sonar signal. We will go into the mechanics of hidden order placement and seeking in more detail in Chapters 8 and 9.

The last main consideration for liquidity-based algorithms is signalling risk. For illiquid assets, even a small order can result in the price shifting away as other traders try to secondguess our requirements. To counter this, we can adopt a similar strategy of using immediateor-cancel style (IOC) orders. So when liquidity becomes available an aggressive order is used to cross with it, sometimes referred to as sniping. In order to leave the best price unaffected, some strategies only take a portion of the available size. Alternatively, hidden orders may be used, either iceberg orders or discretionary orders, although these will leave a certain display size on the order book. Again, we will cover this in more detail in Chapter 9.

## **Basic Mechanism**

Liquidity is closely related to market depth and price. Therefore, a liquidity-seeking algorithm will react strongest when there is plenty of market depth and the price is favourable. This is reasonably similar to the aggressive in-the-money style trading we saw for price inline and adaptive shortfall algorithms.

Instead of making the algorithm react to traded volume, we will create a market depth measure that reflects the volume available at a favourable price point. Figure 5-27 shows an example order to buy 10,000 ABC with a liquidity-seeking algorithm using this metric.

![](_page_33_Figure_6.jpeg)

Figure 5-27 An example liquidity seeking order

Therefore, when the price and market depth are favourable, the algorithm trades aggressively to consume liquidity, as may be seen by the participation spikes shown in Figure 5-28. One of the benefits of fragmented markets is that a higher level of participation may be achieved by spreading the execution across a wide range of venues.

Note that this example shows a purely liquidity-driven approach, so when market conditions are unfavourable it then does not trade at all. Hence, the participation falls to zero several times in the middle of the day as the liquidity falls to low levels. It is also zero when

![](_page_34_Figure_1.jpeg)

Figure 5-28 Target participation rate for a liquidity seeking order

the price becomes unfavourable, such as towards the close. Though, this could be avoided by setting a looser price limit or target benchmark. Other versions may simply reduce their participation when the price becomes unfavourable, much like a price inline algorithm.

A side effect of this purely opportunistic approach is that in this example the order does not fully complete, as shown in Figure 5-29. In this case, it was due to the price becoming unfavourable, since there was sufficient liquidity. In practice, brokers may well offer versions that support a base level of participation or finish-up logic to help ensure the order executes fully.

![](_page_34_Figure_5.jpeg)

Figure 5-29 Percent completion for a liquidity seeking order

Although liquidity seeking algorithms may be used for any asset, they were originally intended for more illiquid assets and fragmented markets. The example in Figure 5-27 was for a reasonably liquid asset. In comparison, Figure 5-30 shows an example order to buy 10,000 NOP, a much less liquid asset. Again, we can see a similar pattern of comparatively aggressive trading as soon as the price and depth are favourable. With illiquid assets, signalling risk is an even more important concern and more of the liquidity is hidden. Hence,

149

![](_page_35_Figure_1.jpeg)

Figure 5-30 A liquidity seeking order for a more illiquid asset

tactics such as seeking and sniping using IOC type orders become important, as we will see in Chapter 9. Also, note that these examples merely give a flavour of how this problem might be tackled. As with implementation shortfall, the complexity of successfully seeking liquidity means there is a lot of variety in how they achieve their goals.

### **Common variations**

Liquidity-driven algorithms are often used in fragmented markets. Clients may want their orders to only participate at specific venues, such as only certain "dark pool" ATSs. In addition, they may (or not) want their orders to be included in the broker's internalisation stream. Brokers/vendors often tailor versions for each client's specific requirements.

### **Special Parameters:**

Visibility: This specifies how much of the order may actually be displayed at execution venues. Low visibility implies hidden order types or IOC orders should be used, alternatively it might mean that the order is only worked in "dark pool" ATSs. Higher visibility may be used to leave orders exposed, trying to encourage trading for illiquid assets.

*Benchmark price:* This may be used to decide whether the price is favourable enough to warrant participation.

# Pair trading

Pair trading involves buying one asset whilst simultaneously selling another. Therefore, this is a market neutral strategy; the risks from each asset should hedge or offset each other. This makes the trading less affected by market-wide moves, provided that the asset prices are sufficiently correlated. The ideal situation is that the asset we bought increases in price, whilst the one we sold falls. Although so long as the profit on one side of the trade outweighs any loss on the other side, we should still come out ahead. The profits may then be locked in by trading the reverse pair to flatten our positions. Note that the timescales involved here could be anything from minutes to days, weeks, months or even longer.

There are two main types of pair trading, namely statistical arbitrage and risk (or merger) arbitrage. Statistical arbitrage is based on relative asset valuations whilst risk arbitrage is more equity specific, it revolves around the probability of a merger happening. A common approach for statistical arbitrage is based on the expectation of mean-reversion. This assumes that the spread or ratio for the prices of two highly correlated assets will generally oscillate around its mean.

![](_page_36_Figure_3.jpeg)

Figure 5-31 An example statistical arbitrage pair trading strategy

As Figure 5-31 shows, when the spread significantly diverts from the mean this signifies a trading opportunity. A typical trade entry signal occurs when we expect the spread to return to the mean; in this case, the band is based on two standard deviations above and below the mean. If the spread continues in this fashion, we can then exit the position at the mean. On the other hand, if it fails to revert and continues to diverge then we stand to make losses. This may be because the assets are not as correlated as we thought, or the relationship between them may have fundamentally changed.

The quantitative methods for identifying pairs for statistical arbitrage are beyond the scope of this hook, since algorithmic trading kicks in once the pairs have already been found. For those interested in this topic the book 'Pairs Trading: Quantitative Methods and Analysis' by Ganapathy Vidyamurthy (2004) is a good place to start.

### **Basic Mechanism**

Pair trading algorithms focus on trading for a pre-determined benchmark, which is either the spread between two assets or the ratio of their prices.

The simplest example of a pair trade is based on the spread between two asset prices. When the difference in prices between the two assets exceeds a specified threshold, trading is activated. This may be based on the mid prices, or the bid price for the asset to be bought and the offer price for the asset to be sold, or even all possible combinations.

For example, let's assume that historical data has shown assets XYZ and EFG to be highly correlated, following the trend we saw in Figure 5-31. Sometime after time T, we expect the two standard deviation bands to be breached and the spread and ratio to start to return to their historical means, this breach will be our trigger. Figure 5-32 shows the intraday prices, spread and ratio. Note that the spread shown in Figure 5-32 is an absolute value, it is just the mid price of XYZ minus the mid price of EFG.

![](_page_37_Figure_1.jpeg)

Figure 5-32 Pair spread and ratio for XYZ and EFG

Based on historical data, the trigger spread is 0.24 (mean minus two standard deviations). So we will place a pair trade to buy 10,000 XYZ and sell 12,000 EFG with a spread less than or equal to  $0.24$ . This is shown in Figure 5-33.

Note that the ratio of quantities for our trade is 1.2; this is sometimes referred to as the execution ratio. For this example, it was set based on the current price ratio, but any reasonable value may be used.

![](_page_37_Figure_5.jpeg)

Figure 5-33 An example spread based pair trade

Initially, the spread continues to widen (a separate pair trade may already be taking advantage of this (selling XYZ and buying EFG)). However, just after midday the spread crosses the two standard deviation band, presumably on its way back towards the historical mean. Hence, the pair trade starts executing. Though, notice the blip around 3pm when the spread temporarily increases again, causing the pair trade to pause.

An alternative way of specifying the trade is to use a price ratio as the trigger. Again based on historical data we shall set the ratio trigger as 1.2. Figure 5-34 shows an example order to buy 10,000 XYZ and sell EFG when the ratio is less than or equal to 1.2.

![](_page_38_Figure_3.jpeg)

Figure 5-34 An example ratio based pair trade

This time the ratio dips under 1.2 at 12:30 and just stays at or under this for the rest of the day, so there is no interruption to the algorithm. Another difference is that this ratio order is cash balanced, so no execution ratio is used. Instead, each leg of the pair trade is balanced in terms of their value, Table 5-9 shows this more clearly. Note that generally it is more common to specify cash balanced trades in terms of their value, i.e. buy \$500,000 XYZ and sell EFG. As its name suggests, the cash balanced order keeps the trade more market neutral than the non-balanced one.

For both these examples, we have kept the trading of each asset closely linked. In practice, this constraint may be loosened, so that each asset may be traded slightly more autonomously. Clearly, it is important for the algorithm to incorporate the liquidity of each asset, since there could be a substantial difference between the two. In such cases, the algorithm will need to make the trading more dependent on the less liquid asset.

### Common variations

Risk arbitrage pairs can generally use the same approach as the statistical arbitrage ones. The trading strategy is to sell the shares of the bidding company and buy those of the target company. If the merger happens, the position may then be unwound. The profit is from the difference in spreads; generally the spread is wider before the merger then tightens as the

|        |       |       | Spread based trade |          |       |       | Cash balanced ratio trade |          |
|--------|-------|-------|--------------------|----------|-------|-------|---------------------------|----------|
|        |       | XYZ   |                    | EFG      |       | XYZ   |                           | EFG      |
| Time   | Trade | Value | Trade              | Value    | Trade | Value | Trade                     | Value    |
| 12:30  | 180   | 260   | -220               | -270     | 180   | 260   | -220                      | -270     |
| 12:45  | 230   | 340   | $-280$             | -340     | 240   | 350   | -280                      | $-340$   |
| 13:00  | 260   | 380   | $-310$             | -380     | 270   | 390   | -320                      | $-400$   |
| 13:15  | 350   | 510   | -420               | -520     | 350   | 510   | -420                      | -520     |
| 13:30  | 470   | 680   | -560               | -690     | 480   | 690   | -560                      | $-690$   |
| 13:45  | 530   | 770   | -640               | $-800$   | 540   | 780   | -630                      | -790     |
| 14:00  | 470   | 680   | -560               | -690     | 480   | 690   | -560                      | $-690$   |
| 14:15  | 440   | 630   | -530               | -660     | 460   | 660   | -530                      | -660     |
| 14:30  | 530   | 770   | -640               | -800     | 540   | 790   | -630                      | -790     |
| 14:45  | 530   | 780   | -640               | -790     | 530   | 780   | -630                      | -780     |
| 15:00  | 0     | 0     | 0                  | ()       | 700   | 1040  | -840                      | $-1050$  |
| 15:15  | 0     | 0     | 0                  | 0        | 880   | 1300  | -1050                     | $-1300$  |
| 15:30  | 850   | 1250  | $-1020$            | $-1250$  | 850   | 1250  | $-1020$                   | $-1250$  |
| 15:45  | 880   | 1280  | $-1060$            | $-1320$  | 900   | 1310  | $-1060$                   | $-1320$  |
| 16:00  | 930   | 1370  | $-1120$            | $-1390$  | 940   | 1380  | $-1120$                   | $-1390$  |
| 16:15  | 930   | 1370  | $-1120$            | $-1390$  | 940   | 1390  | $-1120$                   | $-1390$  |
| 16:30  | 1140  | 1690  | $-1350$            | $-1670$  | 720   | 1070  | -860                      | $-1070$  |
| Totals | 8720  | 12760 | $-10470$           | $-12990$ | 10000 | 14660 | $-11850$                  | $-14700$ |

**Table 5-9 Comparison of execution values for example pair trades** 

deal reaches completion.

Some versions may also support a cash adjustment, which may be applied before the ratio, or spread is calculated.

### **Special Parameters:**

*Spread/Ratio:* Clearly, this acts as the benchmark for the relationship. Note it is often necessary to specify how it is based, so whether it is an A-B spread or A/B ratio, or B-A or B/A. This can be a useful sanity check to ensure the target is correctly defined.

*Order identifier:* It may be that each leg of the pair needs to be sent separately, in which case some sort of common identifier is necessary to link the two leg orders.

Legging: This allows control over how autonomously each leg may be traded. A small value will constrain the trading, but will also protect us from exposure to price risk.

*Volume limit:* In these examples, the participation rate was capped at 25%. Some variants may allow specific volume constraints for each side of the pair trade.

#### Other trading algorithms $5.7$

So far, all the algorithms we have considered are relatively generic, within reason they could be applied to any asset class. Still, there are also some algorithms based on the unique properties of certain asset classes. For example, we have already seen how some brokers/vendors provide algorithms for handling corporate buyback programs (SEC's Rule 10b-18) for U.S. equities, based on modified POV algorithms.

As algorithmic trading continues to expand outside of the equities markets, it must address

the common trading problems found in each new market. There will undoubtedly be more asset-class specialisations in the future. Ultimately, these may even take advantage of the fungible nature of some of these assets. For instance, an algorithm might select the optimal bond to trade based on its yield to maturity, or an option based on specific risk factors.

In the near-term some of the areas in which further development is most likely are:

- $\bullet$ Multi-leg trading
- . Volatility driven trading
- Targeting new benchmarks ٠

Algorithms often mimic existing trading strategies. For bonds and derivatives, this means multi-leg trading strategies such as barbells, butterflies or condors. The fundamental drivers can also vary across different asset classes. Most of the algorithms we have seen so far have focussed on factors such as price, volume or liquidity; but other factors can also be important. For example, derivatives are affected by the price of their underlying assets, as well as interest rates, and volatility estimates. Price shifts may occur even when there does not appear to be a significant change in the levels of liquidity, supply and demand. Trading algorithms must take this into account if they are to maintain best execution. Therefore, algorithms may need to be completely rethought for trading some of these assets. Hence, some options algorithms may be driven by implied volatility levels rather than price. Similarly, new benchmarks, such as the GWAP (gamma weighted average price) may be more appropriate.

# Multi-leg

Trading strategies for bonds, futures and options often involve multiple legs. Each leg represents an order for a specific asset. These might be as simple as a two-way spread trade, although they may have three or four legs or be even more complex. However complex they might be, these are still usually relative value trades, seeking to take advantage of differences in pricing between assets. Overall, they go long the currently under valued asset/s, hoping that in the future the prices will rebalance netting us a profit. Essentially, they are much the same as pairs (or spread) trading, although they may consist of baskets (or portfolios) of trades.

For instance, Table 5-10 shows some example trading strategies for bonds. Although these examples have 2-3 legs each, we can view them simply in terms of the overall buys and sells.

| Type                         | Side A (buys)                   | Side B (sells)        |
|------------------------------|---------------------------------|-----------------------|
| Coupon Rolls, On/Off the-run | New issue                       | Current issue         |
| Barbell                      | Long maturity<br>Short maturity |                       |
| Butterfly (Bullet-barbell)   | Long maturity<br>Short maturity | Intermediate maturity |

## Table 5-10 Multi-leg bond-based strategies

Bond positions may be rolled when new issues occur as investors might decide to swap (or roll) their investments into them. In which ease they may need to buy the new issue and sell their current position. Investors may also adopt a barbell strategy, by buying both shortterm and long-term bonds. Alternatively, they may take a view on interest rates based on the yield curve. For instance, the butterfly strategy shown in Table 5-10 is structured to take advantage of a future increase in curvature. If rates for intermediate maturity bonds rise, the price of our intermediate bonds will fall giving our short position a profit. Conversely, if the yield curve is expected to flatten the opposite positions may be taken.

For futures, spread trading is so well established that most exchanges support dedicated order books just for spreads. In a sense, the spreads are almost treated as assets in their own right. Table 5-11 shows some of the types of multi-leg strategy which may be used with futures contracts.

| Type                    | Side A (buys)                                              | Side B (sells)                          |
|-------------------------|------------------------------------------------------------|-----------------------------------------|
| Spread (bull)           | Nearby contract e.g. JAN09                                 | Deferred contract e.g. MAR09            |
| Butterfly spread (long) | Nearby contract e.g. JAN09<br>Deferred contract e.g. MAY09 | Next contract (x2) e.g. MAR09           |
| Condor spread (long)    | Nearby contract e.g. JAN09<br>Deferred contract e.g. JUL09 | Next two contracts e.g. MAR09,<br>MAY09 |

### Table 5-11 Multi-leg futures-based strategies

Spread trades may be calendar-based, such as the example in Table 5-11. They may also be traded between contracts for different underliers, or even contracts from other venues. A bull spread tries to take advantage of increasing prices for the near contract in a typically bullish market. Butterfly spreads are essentially two calendar spreads combined, trading the spread between spreads. In the given example, a JAN-MAR bull spread is combined with a MAR-MAY bear spread. The strategy will benefit if the spread between these widens or becomes more positive. A condor is an extension of this approach with a wider hody. From the example in Table 5-11 we now sell two different dated contracts. Again this strategy benefits if the spread widens; conversely, for a short condor the positions would be reversed and it would gain from the spread narrowing. More examples of futures spread trading may be found in a nice overview by the CME (2006a).

Options add extra degrees of complexity since we can buy or sell both calls and puts. In addition, each contract has a specific strike price and maturity. Some example strategies are shown in Table 5-12.

Option spreads may also be strike-based (vertical) as well as calendar spreads. For example, the butterfly and condor long call strategies shown in Table 5-12 are based on calls all with the same expiry, but different strike prices. The payoff for these examples is dependent on the price of the underlying asset staying around the middle strike price. Onesided strategies are also possible since we can buy a put rather than risk writing a call. So the long straddle example will benefit if a marked price shift occurs (in either direction), essentially profiting from volatility. A strangle benefits in a similar way, although this is for prices outside a set range since the put and the call have different strike prices. Options strategies could easily fill a book in their own right. Sheldon Natenberg's (1994) book 'Option volatility and pricing' provides a more detailed review of these trading strategies.

In terms of executing these multi-leg strategies, we could tackle each leg separately. Still, this can expose us to considerable legging risk. For example, we might end up with the desired long position, but only half of the target shorts. Therefore, linking the legs and trading them simultaneously is often a safer option. In some cases this might be as simple as using the linked order types we saw in Chapter 4.

| Type                     | Side A (buys)                                                                         | Side B (sells)                                                                      |
|--------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Call spread (bull)       | Call $(x1)$ e.g. Aug 50                                                               | Call $(x1)$ at higher strike e.g. Aug 55                                            |
| Put spread (bear)        | Put(x1)                                                                               | Put $(x1)$ at higher strike                                                         |
| Call ratio spread        | Call(x)                                                                               | Call $(x2)$ at higher strike                                                        |
| Calendar spread          | Call $(x1)$ e.g. Mar 50                                                               | Call $(x1)$ at later expiration e.g. Jul 50                                         |
| Collar                   | Put(x1)                                                                               | $\text{Call (x1)}$ at higher strike                                                 |
| Butterfly (long)<br>call | Call $(x1)$ at lower strike e.g. Sep 50<br>Call $(x1)$ at higher strike e.g. Sep 60   | Call $(x2)$ e.g. Sep 55                                                             |
| Condor (long) call       | Call $(x1)$ at lowest strike e.g. Aug 45<br>Call $(x1)$ at highest strike e.g. Aug 60 | Call $(x1)$ at lower strike e.g. Aug 50<br>Call $(x1)$ at higher strike e.g. Aug 55 |
| Straddle (long)          | Call(x1)<br>Put $(x1)$ at same strike                                                 |                                                                                     |
| Strangle (long)          | Call(x1)<br>Put $(x1)$ at lower strike                                                |                                                                                     |

#### Table 5-12 Multi-leg options-based strategies

Alternatively, a dedicated algorithm could offer more sophisticated handling, varying the legging based on both risk and the current market conditions. These multi-leg trading examples may also be viewed as one or two-sided portfolio trades. In Chapter 12, we shall address some of these considerations in more detail when we consider portfolio trading.

Multi-leg trading can also span across asset classes. In Chapter 13, we will review some of these strategies, including both hedging (beta, delta, gamma and duration) and arbitrage (dividend, ADR, indices, futures and options).

# Volatility-driven

The algorithms we have considered so far have generally been driven by market conditions for the required asset, whether this is the price, volume or liquidity. However, derivatives are contracts based on an underlying asset, so price moves in the underlying are an important factor. Some brokers/vendors have started to take this into account offering algorithms that can effectively peg to the underlying price.

The prices of options contracts are usually generated by models, which may be based on pricing formulas such as the Black Scholes (1973) model. For instance, a call option's price  $(C)$  may be defined as a function of the price of its underlying asset  $(S)$  and the time left to  $\text{expiry}(T)$ :

$$C(S,T) = SN(d_1) - Ke^{-rT}N(d_2)$$

$$(5-2)$$

where K is the option's strike price, r is the interest rate and  $N()$  is the standard normal cumulative distribution function. The factors  $d_1$  and  $d_2$  are defined by:

$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \qquad d_2 = d_1 - \sigma\sqrt{T}$$

where  $\sigma$  is the asset's price volatility. Thus, the option's price is dependent on the underlying asset, its time to maturity and interest rates. Note that this is its theoretical price, or fair value. Just as with any other type of asset, the market price will be slightly different from this. These differences reflect the views (and inventories) of the other market participants (dealers). Given that the time to maturity and interest rates are pretty much fixed, this leaves volatility as the main variable. Hence, an alternative way of viewing these price differences is to treat them as differing estimates for the volatility of the underlying asset. By reversing the pricing logic, we can therefore determine implied volatilities based on these market prices. For example, Figure 5-35 shows an order book with September 09 call options for asset EFG with a strike price of 50. The current price of EFG is 47.

| Buys              |       |       |      | Sells   |    |                                 |      | Sells   |    |
|-------------------|-------|-------|------|---------|----|---------------------------------|------|---------|----|
| Size              | Price | Price | Size | Time    | ld | Implied Vol.                    | Size | Time    | Id |
| 50                | 3.78  | 3.93  | 10   | 9:02:00 | S1 | 25.00%                          | 10   | 9:02:00 | SI |
|                   |       | 3.98  | 25   | 9:02:05 | S2 | 25.25%                          | 25   | 9:02:05 | S2 |
|                   |       | 4.03  | 20   | 9:02:19 | S3 | 25,50%                          | 20   | 9:02:19 | S3 |
|                   |       |       |      |         |    |                                 |      |         |    |
| $\sim \mathbf{D}$ |       |       |      |         |    | $\angle 1 \setminus \Upsilon$ 1 |      |         |    |

(a) Prices

(b) Implied vols

#### Figure 5-35 A sample option order book together with a view of the implied volatilities

Figure  $5-35(b)$  shows how the market prices have been converted back to their implied volatilities. Now let's consider the situation nearly an hour later.

| Buys     |       |       |      | Sells   |    |  |                                                                                                       |      | Sells   |    |
|----------|-------|-------|------|---------|----|--|-------------------------------------------------------------------------------------------------------|------|---------|----|
| Size     | Price | Price | Size | Time    | Id |  | Implied Vol.                                                                                          | Size | Time    | Id |
| 20       | 3.95  | 4.09  | 15   | 9:51:00 | S4 |  | 24.50%                                                                                                |      | 9:51:00 | S4 |
|          |       | 4.20  |      | 9:51:45 | S5 |  | 25.10%                                                                                                |      | 9:51:45 | S5 |
|          |       | 4.23  | 30   | 9:52:19 | S6 |  | 25.25%                                                                                                | 30   | 9:52:19 | S6 |
|          |       |       |      |         |    |  |                                                                                                       |      |         |    |
| $\wedge$ |       |       |      |         |    |  | $\mathcal{I} \mathbf{1} \mathbf{1} \mathbf{1} \mathbf{1} \mathbf{1} \mathbf{1} \mathbf{1} \mathbf{1}$ |      |         |    |

(a) Prices

(b) Implied vols

#### Figure 5-36 A later snapshot of the order book from Figure 5-35

The price of EFG has risen to 47.5, hence the call option prices have also increased. Though, based on implied volatility we can see that order S4 now actually has a slightly lower value. In effect, this order may be viewed as being "cheaper" in terms of volatility. We can explain this by plugging this volatility into the option price calculation together with the original underlying price of 47. This gives an option a price of 3.84, which is considerably less than any of the prices available an hour before in Figure 5-35.

When comparing option prices it is important to remember that they are being driven by a lot of factors. Consequently, traders may prefer to base their decisions on implied volatility rather than just the current price. In turn, brokers and vendors are starting to offer trading algorithms that adopt a similar approach, effectively driving the algorithm from a modified order book, as shown in Figure 5-35(b).

This approach may also be extended to trading option spreads. Effectively, this is similar to what we discussed for pair trading and multi-leg algorithms, just replacing prices with implied volatilities. Note that it is somewhat more complicated than simple pair trading since other risk factors such as time decay will also need to be taken into account.

Basing the trading decisions on volatility also makes it possible to consider trading different contracts. Given that there can be hundreds (or even thousands) of contracts for a specific asset, each of these will have much lower liquidity. By viewing them in terms of their implied volatility, we can potentially fulfil our requirements with other contracts. For instance, in the previous example we might have also traded some August contracts, or some with another strike price. That said, this approach can add further complications, since different contracts can bring exposure to other risks. Therefore if a portfolio of options contracts is being generated it is important to consider the risk factors (or "Greeks") to make sure that there are no surprises in terms of risk exposure.

As algorithms expand further into the derivatives markets, incorporating these risk factors into trading algorithms is likely to become a much more common requirement. In Chapter 13 we will briefly review how some risk factors (such as delta and gamma) may be hedged.

# Gamma Weighted Average Price (GWAP)

Implementation shortfall has become ubiquitous in the equities markets, although there is still a large contingent of traders and investors who also track benchmarks such as VWAP. Still, VWAP is not necessarily a universal benchmark, particularly for fragmented markets or illiquid assets. The Gamma Weighted Average Price (GWAP) is an alternative benchmark outlined by Scott Larison (2008). It is designed to tackle some of the shortcomings of VWAP for the options markets: A single asset may have thousands of related options contracts, so the liquidity of any one contract will generally be significantly lower than that of the underlying asset. As Larison points out, this lower trading activity makes benchmarks like VWAP less meaningful for options. A further complication is the fact that complex multi-leg strategies represent a considerable volume in the options markets. Thus, prices may also be influenced by those of other contracts. So the GWAP benchmark also takes into account the VWAP of the underlying asset. It may be represented as:

$$G_{wap}(call) = P + [\Delta' * \lambda_{roc}] \qquad G_{wap}(put) = P - [\Delta' * \lambda_{roc}]$$

where P is the option price,  $\Delta'$  is the adjusted delta and  $\lambda_{rec}$  is the rate of change price. In turn, the rate of change price  $(\lambda_{roc})$  is based on the VWAP of the underlying asset:

$$\lambda_{roc} = S_{vwap} - S_0$$

where  $S_0$  is the reference price of the underlying asset, for example, the arrival price or the previous close, and  $S_{vwap}$  is the VWAP average for the specified interval.

The delta is one of the "Greeks"; it is a measure that represents the risk in terms of price moves by the underlying asset.<sup>4</sup> A delta of 1.0 means that for every rise (fall) of \$1 in the underlying asset the option's price will also rise (fall) by \$1. Conversely, a negative delta means that the option's price moves in the opposite direction. In the GWAP calculation, the adjusted delta ( $\Delta$ ') is based on the option's implied delta ( $\Delta$ ) and gamma (y) from when the order was entered:

$$\Delta'_{(call)} = \Delta + (\lambda_{roc} * \gamma) \qquad \Delta'_{(put)} = \Delta - (\lambda_{roc} * \gamma)$$

Gamma is a second derivative risk measure. It quantifies how much the delta will change when the underlying asset's price moves by one unit, e.g. \$1. For example, let's consider a call option priced at \$6 with a delta 0.5 and a gamma of 0.1. When the underlying asset price increases by \$1, the delta means the call option will increase to \$6.5, whilst its delta will increase to 0.6 because of the gamma. We shall cover both of these in more detail in Chapter 13 in the review of delta and gamma hedging strategies.

Larison (2008) goes on to give an example of how the GWAP may be calculated. Based

<sup>&</sup>lt;sup>4</sup> The delta for a call is actually  $N(d_i)$  from equation 5-2.

on this, let's assume that the underlying asset ABC starts with a benchmark price  $(S_0)$  of \$45.0. Throughout the day from 9:30 to 4:00pm, it achieves a VWAP of \$46.00. The price of a September 09 call option with a strike of 50 starts out at \$2,15, with an implied delta of  $38\%$  and a gamma of  $4\%$ .

| Therefore the rate of change of price: | $\lambda_{roc} = 46.0 - 45.0 = 1.0.$             |
|----------------------------------------|--------------------------------------------------|
| The adjusted delta:                    | $\Delta' = 38\% + (1.0 * 4\%) = 42\%.$           |
| Giving a GWAP for our call option:     | $G_{\text{wap}} = $2.15 + [38 \% * 1.0] = $2.53$ |

Consequently, the target benchmark is based on the price moves in the underlying asset rather than those from the option market.

The CBOE have partnered with Pipeline to provide a benchmark crossing based on the GWAP. If this proves successful we may well start to see option algorithms trying to track the GWAP in real-time.

As algorithms continue to spread to more markets we may well see other new benchmarks being adopted.

#### 5.8 Summary

- $\blacksquare$ A trading algorithm is simply a set of instructions used to execute an order.
- Trading algorithms may be broadly categorised into three main groups hased on the target objectives. These are impact-driven, cost-driven or opportunistic.
- $\mathbf{r}$ Impact-driven algorithms seek to minimise the overall market impact costs, usually by splitting larger orders into smaller child orders.
  - -TWAP (time weighted average price) is often driven by a time-hased schedule.
  - VWAP (volume weighted average price) often uses historical volumes as a guide. -
  - Percent of volume (POV) algorithms "go along" with the market volume. ...
  - Minimal impact algorithms use ATSs and "dark pools" to reduce signalling risk. \_
- B Cost-driven algorithms aim to reduce the overall trading costs.
  - Implementation shortfall (IS) seeks to achieve a balance between cost and risk. -
  - \_ Adaptive shortfall algorithms extend this, adapting to the market price (or liquidity).
  - Market-on-close algorithms target the future closing price.
- Opportunistic algorithms strive to take best advantage of favourable market conditions.
  - Price inline algorithms are price-sensitive variants of impact-driven algorithms.
  - Liquidity-driven algorithms are an evolution of simpler rule-based order routing.
  - Pair trading is a market neutral strategy driven by a favourable spread or ratio.
- Most of these algorithms will work across asset classes. Still, the unique features of  $\blacksquare$ some asset classes mean that completely new types may also be needed. For instance:
  - Multi-leg trading for bonds and derivatives
  - -Algorithms driven by factors such as interest rates or volatility
  - Handling fungible assets, so specification-based trading rather than explicit assets
  - Targeting new more appropriate benchmarks -
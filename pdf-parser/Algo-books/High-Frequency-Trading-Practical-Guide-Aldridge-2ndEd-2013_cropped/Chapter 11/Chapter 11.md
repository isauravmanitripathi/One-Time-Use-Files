## **CHAPTER 11**

#### **Automated Market Making II**

Inventory market-making models, discussed in Chapter 10, explain and help manage transitory variations in prices resulting from the imbalances in a dealer's book, or portfolio. The models usually start with a "sweet spot" inventory, an inventory level sufficient to satisfy immediate client demand, and proceed to adjust the inventory according to client demand and the market's conditions. Such models do not consider actions and information available to other market participants.

By contrast, information-based market-making models addressed in this chapter carefully evaluate the trading patterns of various market participants, deduce the news available to them, and optimize marketmaking process by responding to available supply and demand in the markets. The models account for present and expected future trading, including the shape of limit order book, order flow, as well as histories of orders and trading outcomes.

# What's in the Data?

Publicly available data carries information that is sufficient to detect shortterm price movements and manage one's positions accordingly. This section presents four cases for illustration. The figures accompanying the cases show sample market situations observable by all market participants subscribing to Level I data from a given trading venue. The cases apply to all trading venues that deploy a centralized limit order book for its matching operation.

In all figures, the horizontal axis is time. The solid lines are the best bid and the best ask, a.k.a. best offer, observed at the given point in time, and the dashed line shows the midquote: the simple average between the best bid and the best ask. The stars indicate the price and timing of trades: some trades occur at ask, some at bid, and some may occur in the vicinity of either bid or ask.

#### Case 1: Market Does Not Move

<span id="page-1-1"></span>In [Figure 11.1,](#page-1-0) the trades are recorded in the following sequence: the first trade occurred at the best bid, then at the best ask, and finally at the best bid again. Neither the best bid nor the best ask moved. What is the dynamic at work in the market shown in [Figure 11.1?](#page-1-0)

![](_page_1_Figure_2.jpeg)

<span id="page-1-0"></span>**[Figure 11.1](#page-1-1)** The Market Does Not Move in Response to Trades

A short answer to this question is "none." In the market shown in [Figure](#page-1-0) [11.1,](#page-1-0) nothing interesting or unusual is happening. The first order that arrived and resulted in the trade was a market sell—the trade was recorded at the bid, as market sell orders would be. The market sell order was smaller in size than the size at the best bid at the time the order arrived—following the trade, the best bid did not move. The order did not carry any information, at least not from the broader market perspective: the best bid and the best ask quotes remained at their original levels. Had other market participants been concerned about the specialized knowledge of the trader or the imminent movement of the market, they would have likely revised their quotes to minimize their risk.

Following the first sell order, [Figure 11.1](#page-1-0) shows that two additional orders are executed shortly afterward: a market buy order and a market sell order. The buy order is identified as such because it is recorded at the best ask market buy orders would be matched with the ask side of the limit order book. The next trade is recorded at the best bid and, therefore, must be a

sell. Once again, Figure 11.1 shows no changes in prices following either order, implying that

- The size of both orders was small in comparison with aggregate sizes at the best bid and the best ask.
- The orders were not perceived to have any special informational advantages.

### Case 2: Market Moves and Rebounds

<span id="page-2-1"></span>[Figure 11.2](#page-2-0) presents a different scenario: a trade is recorded at the bid. Following the bid, the quotes drop lower, yet gradually recovers over time.

<span id="page-2-0"></span>![](_page_2_Figure_5.jpeg)

![](_page_2_Figure_6.jpeg)

The trade in [Figure 11.2](#page-2-0) occurred at the bid, and was, therefore, triggered by a market sell order. The subsequent drop in the quotes that was followed by gradual recovery suggests that:

1. The trade size was large relative to the size available at the best bid; the market sell order had to "sweep" through the book to be fully matched.

2. Despite its large size, the trade did not move the fundamentals that drive the price—the quotes slowly recovered to their original levels; the trade carried no information.

In [Figure 11.2,](#page-2-0) the best ask quote also drops following the sell. This may be due to the market makers' activity seeking to disgorge the inventory just

acquired via the sell trade. By lowering the best ask quote, a market maker can promptly sell the newly purchased inventory, realizing a quick profit.

#### <span id="page-3-1"></span>Case 3: A Trade Moves Markets

The trade in [Figure 11.3](#page-3-0) also occurred at the bid. Unlike Case 2 above, where the quotes recovered following the trade, in [Figure 11.3](#page-3-0) the trade substantially shifted both bid and ask quotes downward. No immediate recovery of quotes is observed.

<span id="page-3-0"></span>![](_page_3_Figure_3.jpeg)

![](_page_3_Figure_4.jpeg)

The most likely explanation of market activity in [Figure 11.3](#page-3-0) is information. The trade once again came in at the bid and was hence a sell. The markets interpreted the sell, however, as a trade containing enough information to warrant a permanent price decline. Unlike Case 2 above, the quotes did not recover to their original levels, but instead remained at their new lows. The new persistent price level is most likely the result of fundamental information carried by the sell trade.

The market makers may determine that the sell trade possessed information in several ways. Often, the broker-dealer of the trader who placed the sell market order may observe that the trader possesses superior research skills and routinely places profitable orders ahead of other traders. In such situations, the trader's broker-dealer may be the first to adjust the quotes after the trade is executed to protect himself against accepting further trades with a losing counterparty. Such activity is perfectly legal, and is often referred to as *prehedging.* Alternatively, the broker-dealer and

other market participants may determine the probabilistic presence of informed traders through information-extracting models described later in this chapter.

#### Case 4: The Quotes Widen

<span id="page-4-1"></span>[Figure 11.4](#page-4-0) illustrates yet another scenario: a case where spreads widen following a trade.

<span id="page-4-0"></span>**[Figure 11.4](#page-4-1)** The Quotes Widen Following a Trade

![](_page_4_Figure_4.jpeg)

The scenario depicted in [Figure 11.4](#page-4-0) is most often a result of increased uncertainty in the markets. An example of such uncertainty can be the time preceding a major scheduled news announcement, where the news, once released, is likely to move the markets considerably one way or the other. Market makers' natural response is to avoid being run over by betterinformed traders and to pull orders closest to the market price, a practice known as *quoting wide,* shown in [Figure 11.4](#page-4-0).

Cases 1 through 4 illustrate predictable market maker behavior following distinct situations. Other scenarios are also possible. Market makers' behavior following specific market events, observable in public quote data, helps automated trading systems to extract information available solely to other market makers.

# Modeling Information in Order Flow

The remaining sections of the chapter describe four classes of techniques that have been developed to identify impending market moves based on the behavior of other market participants. The described models take into account:

- Order flow autocorrelation
- Order flow aggressiveness
- Shape of the order book
- Sequential evolution of quotes

## Autocorrelation of Order Flow as a Predictor of Market Movement

Order flow is a result of end customers receiving and acting on information. Information models are trained to observe order flow and extract and then trade upon information available to various market participants.

Order flow is the difference in trade volume between trades initiated with market buy orders and trades triggered by market sell orders, all noted within a predetermined period of time. Trades begun with a market buy order are known as *buyer initiated.* Similarly, trading volume caused by market sell orders is referred to as *seller initiated.* Equation (1) illustrates the definition of order flow:

(1)

where is the trading volume resulting from market buy orders being matched with the ask side of the order book, and is the trading volume triggered by market sell orders hitting the bid side of the order book.

According to academic research, order flow is directly responsible for at least 50 percent of information impounded into market prices. Around news releases, order flow becomes highly directional. For example, Love and Payne (2008) estimate that following a major Eurozone and the U.S. news announcement, the order flow surrounding the EUR/USD exchange rate closely follows the directionality of the announcement. Thus, "good" U.S. news, expected to lift the U.S. dollar, is dominated by "buy U.S. dollar" or "sell Euro" orders. Other studies with similar findings about various

securities include Lyons (1995), Perraudin and Vitale (1996), Evans and Lyons (2002a), and Jones, Kaul, and Lipson (1994).

According to Lyons (2001), order flow is informative for three reasons:

1. Order flow can be thought of as market participants exposing their equity to their own forecasts. Market orders are irrevocable commitments to buy or sell, and therefore carry most powerful information. Limit orders can also be executed and be costly and, as a result, carry information. Order flow therefore reflects market participants' honest beliefs about the upcoming direction of the market.

2. Order flow data is decentralized with limited distribution. Brokers can directly observe the order flow of their clients and interdealer networks. End investors seldom see any direct order flow at all, but can partially infer the order flow information from market data, as described in this section. Exchanges possess order flow data they receive from brokers and other market participant. The exchange data may, however, miss significant numbers of investor orders, as brokerdealers increasingly seek to match orders internally, in the process called *internalization of the order flow.* The internalization is presently viewed as a necessary function to contain broker costs by avoiding exchanges whenever possible. Because the order flow is not available to everyone, those who possess full order flow information or successfully model it are in a unique position to exploit it before the information is impounded into market prices.

3. Order flow shows large and nontrivial positions that will temporarily move the market regardless of whether the originator of the trades possesses any superior information, due to market impact. Once again, the traders observing or modeling the order flow are best positioned to capitalize on the market movements surrounding the transaction.

Lyons (2001) further distinguishes between transparent and opaque order flows, with transparent order flows providing immediate information, and opaque order flows failing to produce useful data or subjective analysis to extract market beliefs. According to Lyons (2001), order flow transparency encompasses the following three dimensions:

- Pretrade versus posttrade information
- Price versus quantity information

Public versus dealer information

Brokers observing the customer and interdealer flow firsthand have access to the information pretrade, can observe both the price and the quantity of the trade, and can see both public and dealer information. End customers can generally see only the posttrade price information by the time it becomes public or available to all customers. Undoubtedly, dealers are much better positioned to use the wealth of information embedded in the order flow to obtain superior returns, given the appropriate resources to use the information efficiently.

#### Order Flow Is Directly Observable

As noted by Lyons (1995), Perraudin and Vitale (1996), and Evans and Lyons (2002b), among others, order flow was previously dispersed among market participants but can be viewed centrally by the broker-dealer or a trading venue. Order flow for a particular financial security at any given time is formally measured as the difference between buyer-initiated and seller-initiated trading interest. Order flow is sometimes referred to as *buying or selling pressure.* When the trade sizes are observable, the order flow can be computed as the difference between the cumulative size of buyer-initiated trades and the cumulative size of seller-initiated trades. When trade quantities are not directly observable (as is often the case in foreign exchange), order flow can be measured as the difference between the number of buyer-initiated trades and seller-initiated trades in each specific time interval.

Both trade-size-based and number-of-trades-based measures of order flow have been used in the empirical literature. These measures are comparable since most orders are transmitted in "clips," or parcels of a standard size, primarily to avoid undue attention and price run-ups that would accompany larger trades. Jones et al. (1994) actually found that order flow measured in number of trades predicts prices and volatility better than order flow measured in aggregate size of trades.

The importance of order flow in arriving at a new price level following a news announcement has been verified empirically. Love and Payne (2008), for example, examine the order flow in foreign exchange surrounding macroeconomic news announcements and find that order flow directly

accounts for at least half of all the information impounded into market prices.

<span id="page-8-1"></span>Love and Payne (2008) studied the impact of order flow on three currency pairs: USD/EUR, GBP/EUR, and USD/GBP. The impact of the order flow on the respective rates found by Love and Payne (2008) is shown in [Table](#page-8-0) [11.1.](#page-8-0) The authors measure order flow as the difference between the number of buyer-initiated and the number of seller-initiated trades in each oneminute interval. Love and Payne (2008) document that at the time of news release from Eurozone, each additional buyer-initiated trade in excess of seller-initiated trades causes USD/EUR to increase by 0.00626 or 0.626 percent.

<span id="page-8-0"></span>**[Table 11.1](#page-8-1)** Average Changes in One-Minute Currency Returns Following a Single Trade Increase in the Number of Buyer-Initiated Trades in Excess of Seller-Initiated Trades

|                                                                              | USD/EUR Return | GBP/EUR Return | USD/GBP Return |
|------------------------------------------------------------------------------|----------------|----------------|----------------|
| $Flow_t$ at a time coinciding with a news<br>release from Eurozone           | $0.00626*$     | 0.000544       | 0.00206        |
| $Flow_t$ at a time coinciding with a news<br>release from the United Kingdom | 0.000531       | 0,00339***     | 0.00322        |
| $Flow_t$ at a time coinciding with a news<br>release from the United States  | 0.00701***     | 0.00204        | 0.00342**      |

## Order Flow Is Not Directly Observable

Order flow is not necessarily transparent to all market participants. For example, executing brokers can directly observe buy-and-sell orders coming from their customers, but generally the customers can see only the bid and offer prices, and, possibly, the depth of the market.

As a result, various models have sprung up to extract order flow information from the observable data. The most basic algorithm tests autocorrelation of trade signs. First, the algorithm separates all trades recorded over the past period of time *T*, say, 30 minutes, into buys and sells. The identification of trades can be performed using the Lee-Ready or volume clock rule described in Chapter 4 of this book. Trades identified as buys are assigned "trade direction value" of +1, and each sell trades is noted as –1. Next, the algorithm computes the autocorrelation function (ACF) for lagged trade direction variable, *x<sup>t</sup>* :

$$(2) \rho_{t,t+r} = \frac{1}{N} \sum_{t=1}^{N} x_t x_{t+r}$$

where *t* is the sequential number of a given trade tick in the chosen evaluation interval *T*, and *N* is the total number of ticks within the time interval. An ACF plot, linking the computed autocorrelation with a lag , reveals trade dependencies.

<span id="page-9-1"></span>[Figure 11.5](#page-9-0) shows comparative autocorrelation figures for two financial instruments.

<span id="page-9-0"></span>![](_page_9_Figure_3.jpeg)

![](_page_9_Figure_4.jpeg)

Hasbrouck (1991), in estimating order autocorrelation, adjusts for returns caused by previously placed orders as well as effects of the time of day:

(3) 
$$x_t = \alpha_x \sum_{k=1}^K \beta_k t_{t-k} + \sum_{m=1}^M \gamma_m x_{t-m} + \sum_{t=1}^T \delta D_t + \varepsilon$$

where *x<sup>t</sup>* is the order flow observed at time *t*, set to +1 when the given trade was estimated originate from a market buy order and –1 otherwise; *r<sup>t</sup>* is a one-trade return; and *D*<sup>t</sup> is the dummy indicator controlling for the time of day into which time *t* falls.

Ellul, Holden, Jain, and Jennings (2007) interpret short-term autocorrelation in high-frequency order flows as waves of competing order flows responding to current market events within liquidity depletion and replenishment. Ellul et al. (2007) confirm strong positive serial correlation in order flow at high frequencies, but find negative order firm correlation at lower frequencies. Other studies of order autocorrelation include Hedvall,

Niemeyer, and Rosenqvist (1997); Ranaldo (2004); Hollifield, Miller, and Sandas (2004); Foucault, Kadan, and Kandel (2005); Rosu (2005); and Biais, Hillion, and Spatt (1995).

Order flow information is easy to trade profitably. A disproportionately large number of buy orders will inevitably push the price of the traded security higher; placing a buy order at the time a large buy volume is observed will result in positive gains. Similarly, a large number of sell orders will depress prices, and a timely sell order placed when the sell order flow is observed will generate positive results.

## Order Aggressiveness as a Predictor of Market Movement

To extract the market information from the publicly available data, Vega (2007) proposes monitoring the aggressiveness of trades. Aggressiveness refers to the percentage of orders that are submitted at market prices, as opposed to limit prices. The higher the percentage of market orders, the more aggressive is the trader in his bid to capture the best available price and the more likely the trader is to believe that the price of the security is about to move away from the market price.

The results of Vega (2007) are based on those of Foster and Viswanathan (1996), who evaluate the average response of prices in a situation where different market participants are informed to a different degree. For example, before an expected economic announcement is made, it is common to see "a consensus forecast" that is developed by averaging forecasts of several market analysts. The consensus number is typically accompanied by a range of forecasts that measures the dispersion of forecasts by all analysts under consideration. For example, prior to the announcement of the January 2009 month-to-month change in retail sales in the United States, Bloomberg LP reported the analysts' consensus to be –0.8 percent, while all the analysts' estimates for the number ranged from –2.2 percent to 0.3 percent (the actual number revealed at 8:30 a.m. on February 12, 2009, happened to be +1.0 percent).

Foster and Viswanathan (1996) show that the correlation in the degree of informativeness of various market participants affects the speed with which

information is impounded into prices, impacts profits of traders possessing information, and also determines the ability of the market participants to learn from each other. In other words, the narrower the analysts' forecast range, the faster the market arrives at fair market prices of securities following a scheduled news release. The actual announcement information enters prices through active trading. Limit orders result in more favorable execution prices than market orders; the price advantage, however, comes at a cost—the wait and the associated risk of nonexecution. Market orders, on the other hand, are executed immediately but can be subject to adverse pricing. Market orders are used in aggressive trading, when prices are moving rapidly and quick execution must be achieved to capture and preserve trading gains. The better the trader's information and the more aggressive his trading, the faster the information enters prices.

As a result, aggressive orders may themselves convey information about the impending direction of the security price move. If a trader executes immediately instead of waiting for a more favorable price, the trader may convey information about his beliefs about where the market is going. Vega (2007) shows that better-informed market participants trade more aggressively. Mimicking aggressive trades, therefore, may result in a consistently profitable trading strategy. Measures of aggressiveness of the order flow may further capture informed traders' information and facilitate generation of short-term profits.

Anand, Chakravarty, and Martell (2005) find that on the New York Stock Exchange (NYSE), institutional limit orders perform better than limit orders placed by individuals, orders at or better than market price perform better than limit orders placed inside the bid-ask spread, and larger orders outperform smaller orders. To evaluate the orders, Anand et al. (2005) sampled all orders and the execution details of a three-month trading audit trail on the NYSE, spanning November 1990 through January 1991.

Anand et al. (2005) use the following regression equation to estimate the impact of various order characteristics on the price changes measured as *Diff.*, the difference between the bid-ask midpoints at times  $t$  and  $t + n$ :

(4)  $\text{Diff}_{t} = \beta_{0} + \beta_{1} \text{Size}_{t} + \beta_{2} \text{Aggressiveness}_{t} + \beta_{3} \text{Institutional}_{t} + D_{1t} + \ldots + D_{n-1,t} + \varepsilon_{t}$ 

where  $t$  is the time of the order submission,  $n$  equals 5 and then 60 minutes after order submission. Size is the number of shares in the particular order divided by the mean daily volume of shares traded in the particular stock over the sample period. For buy orders, *Aggressiveness* is a dummy that takes the value 1 if the order is placed at or better than the standing quote and zero otherwise. *Institutional* is a dummy variable that takes the value 1 for institutional orders and 0 for individual orders. *D*<sup>1</sup> to *D*n-1 are stockspecific dummies associated with the particular stock that was traded.

<span id="page-12-1"></span>[Table 11.2](#page-12-0), from Anand et al. (2005), summarizes the results of robustness regressions testing for a difference in the performance of institutional and individual orders. The regression equation controls for stock selection by institutional and individual traders. The dependent variable in the regression is the change in the bid-ask midpoint 5 and then 60 minutes after order submission.

<span id="page-12-0"></span>**[Table 11.2](#page-12-1)** Summary of Robustness Regressions Testing for a Difference in the Performance of Institutional and Individual Orders

|                              | Intercept | Size     | Aggressiveness | Institutional |
|------------------------------|-----------|----------|----------------|---------------|
| $\text{Panel A: 97 stocks}$  |           |          |                |               |
| 5 min after order placement  | 0.005     | $0.010*$ | $0.016*$       | $0.004*$      |
| 60 min after order placement | $0.020**$ | $0.020*$ | $0.012*$       | $0.006*$      |
| Panel B: 144 stocks          |           |          |                |               |
| 5 min after order placement  | 0.006     | $0.012*$ | $0.014*$       | $0.004*$      |
| 60 min after order placement | $0.021**$ | $0.023*$ | $0.012*$       | $0.004*$      |

According to several researchers, market aggressiveness exhibits autocorrelation that can be used to forecast future realizations of market aggressiveness. The autocorrelation of market aggressiveness is thought to originate from either of the following sources:

- Large institutional orders that are transmitted in smaller slices over an extended period of time at comparable levels of market aggressiveness
- Simple price momentum

Research into detecting autocorrelation of market aggressiveness was performed by Biais et al. (1995), who separated orders observed on the Paris Bourse by the degree of aggressiveness—from the least aggressive market orders that move prices to the most aggressive limit orders outside the current book. The authors found that the distribution of orders in terms

of aggressiveness depends on the state of the market and that order submissions are autocorrelated. The authors detected a "diagonal effect" whereby initial orders of a certain level of aggressiveness are followed by other orders of the same level of aggressiveness. Subsequent empirical research confirmed the findings for different stock exchanges. See, for example, Griffiths, Smith, Turnbull, and White (2000) for the Toronto Stock Exchange; Ranaldo (2004) for the Swiss Stock Exchange; Cao, Hansch, and Wang (2004) for the Australian Stock Exchange; Ahn, Bae, and Chan (2001) for the Stock Exchange of Hong Kong; and Handa et al. (2003) for the CAC40 stocks traded on the Paris Bourse.

## Shape of the Order Book as a Predictor of Market Direction

Several studies have considered how the limit order book can be used to predict short-term price moves. Cao et al. (2004), for example, find that a liquidity peak close to the market price, for example, tends to push the market price away from the peak. However, a liquidity peak away from the market price tends to "pull" the market price toward the peak. Cohen, Maier, Schwartz, and Whitcomb (1981), call this phenomenon a "gravitational pull" of quotes. [Figure 11.6](#page-13-0) shows the sample evolution of the market depth and the associated liquidity.

<span id="page-13-0"></span>**[Figure 11.6](#page-13-1)** An Asymmetric Liquidity Peak Near the Market Price Tends to Push the Market Price Away from the Peak

<span id="page-13-1"></span>![](_page_13_Figure_4.jpeg)

Rosu (2005) determines that the shape of the limit order book depends on the probability distribution for arriving market orders. High probabilities of large market orders lead to hump-shaped limit order books. Foucault, Moinas, and Theissen (2005) find that the depth of the limit order book can forecast future volatility of asset prices: the lower the depth, the lower the expected volatility. Berber and Caglio (2004) find that limit orders carry private information around events such as earnings announcements: a concentration of limit orders far away from the current market price is likely to reflect someone's postannouncement valuation of the traded instrument.

Cont, Kukanov, and Stoikov (2011) suggest that even Level I data can be used to generate successful predictions of the impending price movements. To predict the price movement, Cont et al. (2011) define a new variable, order flow imbalance (OFI):

(5) 
$$OFL_k = \sum_{n=N(t_k-1)+1}^{N(t_k)} e_n$$

where  $e_{n}$  represents an instantaneous change in the top-of-the-book liquidity, and is defined as follows:

$$(6) \ e_n = I_{\{P^{\mathbf{a}}_n \geq P^{\mathbf{a}}_{n-1}\}} q^B_n - I_{\{P^{\mathbf{a}}_n \leq P^{\mathbf{a}}_{n-1}\}} q^B_{n-1} - I_{\{P^{\mathbf{a}}_n \leq P^{\mathbf{a}}_{n-1}\}} q^A_n + I_{\{P^{\mathbf{a}}_n \geq P^{\mathbf{a}}_{n-1}\}} q^A_{n-1}$$

where  $I$  is the indicator function, equal to 1 when the bracketed condition is true, and 0 otherwise, and  $q^{\text{B}}$  and  $q^{\text{A}}$  are the sizes at the best bid and the best ask, respectively.

Equations (5) and (6) can be interpreted as follows: Order Flow Imbalance depends on the instantaneous change in the top-of-the-book liquidity, which in turn depends on the tick-to-tick change in best bid and best offer prices. If the best bid price increased, the Order Flow Imbalance increases by the size at the *new* best bid. If the best bid price decreases from one tick to the next, the associated OFI is reduced by the best bid size recorded at the *previous* tick. Similarly, if the ask price decreases, the OFI is decremented by the size at the *new* best ask. If the ask price increases from last tick to the present tick, the OFI is increased by the size recorded at the *previous* best ask.

To ascertain predictive power of the OFI, Cont et al. (2011) next map the OFI figures vis-à-vis short-term price changes, and obtain a linear relationship, as shown in <u>Figure 11.7</u>.

**Figure 11.7** Order-Flow Imbalance versus Short-Term Price Changes

*Source: Cont, Kukanov, and Stoikov (2011)*

![](_page_15_Figure_2.jpeg)

## Evolution of Tick Data as a Predictor of Market Movement

The advanced class of information models specifically addresses the intent and future actions of various market participants. Such models include game-theoretic approaches to reverse-engineer quote and trade flows to discover the information a market maker possesses. Information models also use observed or inferred order flow to make informed trading decisions.

At their core, information models describe trading on information flow and possible informational asymmetries arising during the dissemination of information. Differences in information flow persist in different markets. Information flow is comparably faster in transparent centralized markets, such as most equity markets and electronic markets, and slower in the opaque markets, such as foreign exchange and over-the-counter (OTC) markets in bonds and derivatives.

Asymmetric information present in the markets leads to adverse selection, or the ability of informed traders to "pick off" uninformed market participants. According to Dennis and Weston (2001) and Odders-White and Ready (2006), the following measures of asymmetric information have been proposed over the years:

- Quoted bid-ask spread
- Effective bid-ask spread
- Information-based impact
- Adverse-selection components of the bid-ask spread
- Probability of informed trading

# Quoted Bid-Ask Spread

The quoted bid-ask spread is the crudest, yet most readily observable measure of asymmetric information. First suggested by Bagehot (1971) and later developed by numerous researchers, the bid-ask spread reflects the expectations of market movements by the market maker using asymmetric information. When the quoting dealer receives order flow that he suspects may come from an informed trader and may leave the dealer at a disadvantage relative to the market movements, the dealer increases the spread he quotes in order to compensate himself against potentially adverse uncertainty in price movements. As a result, the wider the quoted bid-ask spread, the higher is the dealer's estimate of information asymmetry between his clients and the dealer himself. Given that the dealer has the same access to public information as do most of the dealer's clients, the quoted bid-ask spread may serve as a measure of asymmetric information available in the market at large at any given point in time.

# Effective Bid-Ask Spread

The effective bid-ask spread is computed as twice the difference between the latest trade price and the midpoint between the quoted bid and ask prices, divided by the midpoint between the quoted bid and ask prices:

$$(7) \quad S_t^e = \left(\frac{4S_t}{S_t^a + S_t^b} - 1\right)$$

The effective spread measures how far, in percentage terms, the latest realized price fell away from the simple midquote. When markets are balanced and no information streams through, the true midquote is the natural trading price. When the limit order book is skewed or imbalanced in some other way, the traded price moves closer to the side with excess limit orders located at or near the top of the book.

## Information-Based Impact

The information-based impact measure of asymmetric information is attributable to Hasbrouck (1991). Brennan and Subrahmanyam (1996) specify the following vector autoregressive (VAR) model for estimation of the information-based impact measure,  $λ$ :

$$(8) \begin{aligned} V_{i,t} &= \theta_{i,0} + \sum_{k=1}^{K} \beta_{i,k} \Delta P_{i,t-k} + \sum_{m=1}^{M} \gamma_{i,m} V_{i,t-m} + \tau_{i,t} \\ (9) \ \Delta P_{i,t} &= \phi_{i,0} + \phi_{i,1} sign(\Delta P_{i,t}) + \lambda_{i} \tau_{i,t} + \varepsilon_{i,t} \end{aligned}$$

where  $\Delta P_{i,t}$  is the change in price of security *i* from time *t*–1 to time *t*,  $V_{i,t}$ =sign( $\Delta P_{i,t}$ ).  $v_{i,t}$ , and  $v_{i,t}$  is the volume recorded in trading the security *i* from time  $t - 1$  to time  $t$ . Brennan and Subrahmanyam (1996) propose five lags in estimation of equation (8):  $K = M = 5$ .

# Adverse Selection Components of the Bid-Ask Spread

The adverse selection components of the bid-ask spread is attributable to Glosten and Harris (1988). The model separates the bid-ask spread into the following three components:

- Adverse selection risk
- Order-processing costs
- Inventory risk

Models in a similar spirit were proposed by Roll (1984); Stoll (1989); and George, Kaul, and Nimalendran (1991). The version of the Glosten and Harris (1988) model popularized by Huang and Stoll (1997) aggregates inventory risk and order-processing costs and is specified as follows:

$$(10) \Delta P_{i,t} = (1 - \lambda_i) \frac{S_{i,t}}{2} sign(\Delta P_{i,t}) + \lambda_i \frac{S_{i,t}}{2} sign(\Delta P_{i,t}). v_{i,t} + \varepsilon_{i,t}$$

where  $\Delta P_{i}$  is the change in price of security *i* from time  $t - 1$  to time *t*,  $V_{i} = sign(\Delta P_{i})$ .  $v_{i}$ ,  $v_{i}$  is the volume recorded in trading the security *i* from time  $t - 1$  to time  $t$ ,  $S_{i,t}$  is the effective bid-ask spread as defined previously, and  $\lambda$  is the fraction of the traded spread due to adverse selection.

#### Probability of Informed Trading

Easley, Kiefer, O'Hara, and Paperman (1996) propose a model to distill the likelihood of informed trading from sequential quote data. The model reverse-engineers the quote sequence provided by a dealer to obtain a probabilistic idea of the order flow seen by the dealer.

The model is built on the following concept. Suppose an event occurs that is bound to impact price levels but is observable only to a select group of investors. Such an event may be a controlled release of selected information or a research finding by a brilliant analyst. The probability of such an event is  $\alpha$ . Furthermore, suppose that if the event occurs, the probability of its having a negative effect on prices is  $\delta$  and the probability of the event's having a positive effect on prices is  $(1 - \delta)$ . When the event occurs, informed investors know of the impact the event is likely to have on prices; they then place trades according to their knowledge at a rate  $\mu$ . Thus, all the investors informed of the event will place orders on the same side of the market—either buys or sells. At the same time, investors uninformed of the event will keep placing orders on both sides of the market at a rate  $\omega$ . The probability of informed trading taking place is then determined as follows:

$$\mathit{PI} = \frac{\alpha\mu}{\alpha\mu + 2\omega}$$

The parameters  $\alpha$ ,  $\mu$  and  $\omega$  are then estimated from the following likelihood function over *T* periods of time:

(12) 
$$L(B, S | \alpha, \mu, \omega, \delta) = \prod_{t=1}^{T} \ell(B, S, t | \alpha, \mu, \omega, \delta)$$

where  $\ell(B,S,t|\alpha,\mu,\omega,\delta)$  is the likelihood of observing *B* buys and *S* sells within a specific period of time:

$$\ell(B, S, t \mid \alpha, \mu, \omega, \delta) = (1 - \alpha) \left[ \exp(-\omega T) \frac{(\omega T)^{B}}{B!} \right] \left[ \exp(-\omega T) \frac{(\omega T)^{S}}{S!} \right]$$
$$+ \alpha (1 - \delta) \left[ \exp(-(\omega + \mu)T) \frac{((\omega + \mu)T)^{B}}{B!} \right] \left[ \exp(-\omega T) \frac{(\omega T)^{S}}{S!} \right]$$
$$(13)$$

# Summary

Understanding the type and motivation of each market participant can unlock profitable trading strategies. For example, understanding whether a particular market participant possesses information about impending market movement may result in immediate profitability from either engaging the trader if he is uninformed or following his moves if he has superior information.

# End of Chapter Questions

1. If the quotes widen following a trade, and then revert to their original levels, what can be said about the informational content of the trade? Explain.

2. What is order flow? How is it measured? How can it be estimated from tick data?

3. Does the order-flow imbalance metric developed by Cont, Kukanov, and Stoikov (2011) increase when the size at the best bid increases? Explain.

4. Suppose you observe a high autocorrelation of order flow in MSFT. Who is most likely trading and why? How can your algorithm utilize the information to generate positive gains?

5. What is adverse selection? When the risk of adverse selection falls, what does this mean for a market-making algorithm?
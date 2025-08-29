# CHAPTER 12

# **Event Arbitrage**

ith news reported instantly and trades placed on a tick-by-tick basis, high-frequency strategies are now ideally positioned to profit from the impact of announcements on markets. These highfrequency strategies, which trade on the market movements surrounding news announcements, are collectively referred to as event arbitrage. This chapter investigates the mechanics of event arbitrage in the following order:

- Overview of the development process
- Generating a price forecast through statistical modeling of
  - Directional forecasts
  - Point forecasts
- Applying event arbitrage to corporate announcements, industry news, and macroeconomic news
- Documented effects of events on foreign exchange, equities, fixed income, futures, emerging economies, commodities, and REIT markets

# DEVELOPING EVENT ARBITRAGE TRADING STRATEGIES

Event arbitrage refers to the group of trading strategies that place trades on the basis of the markets' reaction to events. The events may be economic or industry-specific occurrences that consistently affect the securities of interest time and time again. For example, unexpected increases in the Fed Funds rates consistently raise the value of the U.S. dollar, simultaneously raising the rate for USD/CAD and lowering the rate for AUD/USD. The announcements of the U.S. Fed Funds decisions, therefore, are events that can be consistently and profitably arbitraged.

The goal of event arbitrage strategies is to identify portfolios that make positive profit over the time window surrounding each event. The time window is typically a time period beginning just before the event and ending shortly afterwards. For events anticipated ex-ante, such as scheduled economic announcements, the portfolio positions may be opened ahead of the announcement or just after the announcement. The portfolio is then fully liquidated shortly after the announcement.

Trading positions can be held anywhere from a few seconds to several hours and can result in consistently profitable outcomes with low volatilities. The speed of response to an event often determines the trade gain; the faster the response, the higher the probability that the strategy will be able to profitably ride the momentum wave to the post-announcement equilibrium price level. As a result, event arbitrage strategies are well suited for high-frequency applications and are most profitably executed in fully automated trading environments.

Developing an event arbitrage trading strategy harnesses research on equilibrium pricing and leverages statistical tools that assess tick-by-tick trading data and events the instant they are released. Further along in this chapter, we will survey academic research on the impact of events on prices; now we investigate the mechanics of developing an event arbitrage strategy.

Most event arbitrage strategies follow a three-stage development process:

- **1.** For each event type, identify dates and times of past events in historical data.
- **2.** Compute historical price changes at desired frequencies pertaining to securities of interest and surrounding the events identified in Step 1.
- **3.** Estimate expected price responses based on historical price behavior surrounding past events.

The sources of dates and times for specified events that occurred in the past can be collected from various Internet sites. Most announcements recur at the same time of day and make the job of collecting the data much easier. U.S. unemployment announcements, for example, are always released at 8:30 A.M. Eastern time. Some announcements, such as those of the U.S. Federal Open Markets Committee interest rate changes, occur at irregular times during the day and require greater diligence in collecting the data.

## **WHAT CONSTITUTES AN EVENT?**

The events used in event arbitrage strategies can be any releases of news about economic activity, market disruptions, and other events that consistently impact market prices. Classic financial theory tells us that in efficient markets, the price adjusts to new information instantaneously following a news release. In practice, market participants form expectations about inflation figures well before the formal statistics are announced. Many financial economists are tasked with forecasting inflation figures based on other continuously observed market variables, such as prices on commodity futures and other market securities. When such forecasts become available, market participants trade securities on the basis of the forecasts, impounding their expectations into prices well before the formal announcements occur.

All events do not have the same magnitude. Some events may have positive and negative impacts on prices, and some events may have more severe consequences than others. The magnitude of an event can be measured as a deviation of the realized event figures from the expectations of the event. The price of a particular stock, for example, should adjust to the net present value of its future cash flows following a higher- or lower-than-expected earnings announcement. However, if earnings are in line with investor expectations, the price should not move. Similarly, in the foreign exchange market, the level of a foreign exchange pair should change in response to an unexpected change—for example, in the level of the consumer price index (CPI) of the domestic country. If, however, the domestic CPI turns out to be in line with market expectations, little change should occur.

The key objective in the estimation of news impact is the determination of what actually constitutes the unexpected change, or news. The earliest macroeconomic event studies, such as those of Frenkel (1981) and Edwards (1982), considered news to be an out-of-sample error based on the one-step-ahead autoregressive forecasts of the macroeconomic variable in question. The thinking went that most economic news develops slowly over time, and the trend observed during the past several months or quarters is the best predictor of the value to be released on the next scheduled news release day. The news, or the unexpected component of the news release, is then the difference between the value released in the announcement and the expectation formed on the basis of autoregressive analysis.

Researchers such as Eichenbaum and Evans (1993) and Grilli and Roubini (1993) have been using the autoregressive framework to predict the decisions of the central bankers, including the U.S. Federal Reserve. Once again, the main rationale behind the autoregressive predictability of the central bankers' actions is that the central bankers are not at liberty to make drastic changes to economic variables under their control, given that major changes may trigger large-scale market disruptions. Instead, the central bankers adopt and follow a longer-term course of action, gradually adjusting the figures in their control, such as interest rates and money supply, to lead the economy in the intended direction.

The empirical evidence of the impact of news defined in the autoregressive fashion shows that the framework indeed can be used to predict future movements of securities. Yet the impact is best seen in shorter terms—for example, on intra-day data. Almeida, Goodhart, and Payne (1998) documented a significant effect of macroeconomic news announcements on the USD/DEM exchange rate sampled at five-minute intervals. The authors found that news announcements pertaining to the U.S. employment and trade balance were particularly significant predictors of exchange rates, but only within two hours following the announcement. On the other hand, U.S. non-farm payroll and consumer confidence news announcements caused price momentum lasting 12 hours or more following an announcement.

Lately, surprises in macroeconomic announcements have been measured relative to published averages of economists' forecasts. For example, every week *Barron's* and the *Wall Street Journal* publish consensus forecasts for the coming week's announcements. The forecasts are developed from a survey of field economists.

#### **FORECASTING METHODOLOGIES**

Directional and point forecasts are the two approaches to estimating the price response to an announcement. A directional forecast predicts whether the price of a particular security will go up or down, whereas a point forecast predicts the level to which the new price will go. The following two sections consider directional and point forecast methodologies in detail. The last section of the chapter discusses event study results that have been documented in the academic literature to date.

#### **Directional Forecasts**

Directional forecasts of the post-event price movement of the security price can be created using the sign test. The sign test answers the following question: does the security under consideration consistently move up or down in response to announcements of a certain kind?

The sign test assumes that in the absence of the event, the price change, or the return, is equally likely to be positive or negative. When an event occurs, however, the return can be persistently positive or negative, depending on the event. The sign test aims to estimate whether a persistently positive or negative sign of the response to a specific event exists and whether the response is statistically significant. If the sign test produces a statistically significant result, an event arbitrage trading strategy is feasible.

MacKinlay  $(1997)$  specifies the following test hypotheses for the sign test:

- The null hypothesis,  $H_0: p \le 0.5$ , states that the event does *not* cause consistent behavior in the price of interest—that is, the probability  $p$  of the price moving consistently in one direction in response to the event is less than or equal to  $50$  percent.
- The alternative hypothesis,  $H_A: p > 0.5$ , is that the event *does* cause consistent behavior in the price of the security of interest—in other words, the probability  $p$  of the price moving consistently in one direction in response to the event is greater than  $50$  percent.

We next define  $N$  to be the total number of events and let  $N^+$  denote the number of events that were accompanied by positive return of the security under our consideration. The null hypothesis is rejected, and the price of the security is determined to respond consistently to the event with statistical confidence of  $(1 - \alpha)$  if the asymptotic test statistic  $\theta > \Phi^{-1}(\alpha)$ , where  $\theta = \left\lceil \frac{N^+}{N} - 0.5 \right\rceil \frac{\sqrt{N}}{0.5} \sim N(0, 1)$ .

Example: Trading USD/CAD on U.S. Inflation Announcements The latest figures tracking U.S. inflation are released monthly at 8:30 A.M. on prespecified dates. On release, USD/CAD spot and other USD crosses undergo an instantaneous one-time adjustment, at least in theory. Identifying when and how quickly the adjustments happen in practice, we can construct profitable trading strategies that capture changes in price levels following announcements of the latest inflation figures.

Even to a casual market observer, the movement of USD/CAD at the time inflation figures are announced suggests that the price adjustment may not be instantaneous and that profitable trading opportunities may exist surrounding U.S. inflation announcements. When the sign test is applied to intra-day USD/CAD spot data, it indeed shows that profitable trading opportunities are plentiful. These opportunities, however, exist only at high frequencies.

The first step in identification of profitable trading opportunities is to define the time period from the announcement to the end of the trading opportunity, known as the "event window." We select data sample windows surrounding the recent U.S. inflation announcements in the ticklevel data from January 2002 through August 2008. As all U.S. inflation announcements occur at 8:30 A.M. EST, we define 8 A.M. to 9 A.M. as the trading window and download all of the quotes and trades recorded during that time. We partition the data further into 5-minute, 1-minute, 30-second, and 15-second blocks. We then measure the impact of the announcement on the corresponding 5-minute, 1-minute, 30-second, and 15-second returns of USD/CAD spot.

According to the purchasing power parity (PPP), a spot exchange rate between domestic and foreign currencies is the ratio of the domestic and foreign inflation rates. When the U.S. inflation rate changes, the deviation disturbs the PPP equilibrium and the USD-based exchange rates adjust to new levels. When the U.S. inflation rate rises, USD/CAD is expected to increase instantaneously, and vice versa. To keep matters simple, in this example we will consider the inflation news in the same fashion as it is announced, ignoring the market's pre-announcement adjustment to expectations of inflation figures.

The sign test then tells us during which time intervals, if any, the market properly and consistently responds to announcements during our "trading window" from 8 to 9 A.M. The sample includes only days when inflation rates were announced. The summary of the results is presented in Table 12.1.

Looking at 5-minute intervals surrounding the U.S. inflation announcements, it appears that USD/CAD reacts persistently only to decreases in the U.S. inflation rate and that reaction is indeed instantaneous. USD/CAD decreases during the 5-minute interval from 8:25 A.M. to 8:30 A.M. in response to announcements of lower inflation with 95 percent statistical confidence. The response may potentially support the instantaneous adjustment hypothesis; after all, the U.S. inflation news is released at 8:30 A.M., at which point the adjustment to drops in inflation appears to be completed. No statistically significant response appears to occur following rises in inflation.

| Estimation Frequency | U.S. Inflation Up | U.S. Inflation Down |
|----------------------|-------------------|---------------------|
| 5 minutes            | 0                 | 0                   |
| 1 minute             | 1                 | 0                   |
| 30 seconds           | 4                 | 1                   |
| 15 seconds           | 5                 | 6                   |

| TABLE 12.1 | Number of Persistent Trading Opportunities in USD/CAD Following |
|------------|-----------------------------------------------------------------|
|            | the U.S. Inflation Rate Announcements                           |

Higher-frequency intervals tell us a different story—the adjustments occur in short-term bursts. At 1-minute intervals, for example, the adjustment to increases in inflation can now be seen to consistently occur from 8:34 to 8:35 A.M. This post-announcement adjustment, therefore, presents a consistent profit-taking opportunity.

Splitting the data into 30-second intervals, we observe that the number of tradable opportunities increases further. For announcements of rising inflation, the price adjustment now occurs in four 30-second postannouncement intervals. For the announcements showing a decrease in inflation, the price adjustment occurs in one 30-second post-announcement time interval.

Examining 15-second intervals, we note an even higher number of time-persistent trading opportunities. For rising inflation announcements, there are five 15-second periods during which USD/CAD consistently increased in response to the inflation announcement between 8:30 and 9:00 A.M., presenting ready tradable opportunities. Six 15-second intervals consistently accompany falling inflation announcements during the same 8:30 to 9:00 A.M. time frame.

In summary, as we look at shorter time intervals, we detect a larger number of statistically significant currency movements in response to the announcements. The short-term nature of the opportunities makes them conducive to a systematic (i.e., black-box) approach, which, if implemented knowledgeably, reduces risk of execution delays, carrying costs, and expensive errors in human judgment.

# **Point Forecasts**

Whereas directional forecasts provide insight about direction of trends, point forecasts estimate the future value of price in equilibrium following an announcement. Development of point forecasts involves performing event studies on very specific trading data surrounding event announcements of interest.

Event studies measure the quantitative impact of announcements on the returns surrounding the news event and are usually conducted as follows:

- **1.** The announcement dates, times, and "surprise" changes are identified and recorded. To create useful simulations, the database of events and the prices of securities traded before and after the event should be very detailed, with events categorized carefully and quotes and trades captured at high frequencies. The surprise component can be measured in following ways:
  - As the difference between the realized value and the prediction based on autoregressive analysis

- As the difference between the realized value and the analyst forecast consensus obtained from Bloomberg or Thomson Reuters.
- **2.** The returns corresponding to the times of interest surrounding the announcements are calculated for the securities under consideration. For example, if the researcher is interested in evaluating the impact of CPI announcements on the 5-minute change in USD/CAD, the 5-minute change in USD/CAD is calculated from 8:30 A.M. to 8:35 A.M. on historical data on past CPI announcement days. (The 8:30 to 8:35 A.M. interval is chosen for the 5-minute effect of CPI announcements, because the U.S. CPI announcements are always released at 8:30 A.M. ET.)
- **3.** The impact of the announcements is then estimated in a simple linear regression:

$$R_t = \alpha + \beta \Delta X_t + \varepsilon_t$$

where *Rt* is the vector of returns surrounding the announcement for the security of interest arranged in the order of announcements; *Xt* is the vector of "surprise" changes in the announcements arranged in the order of announcements; ε*<sup>t</sup>* is the idiosyncratic error pertaining to news announcements; α is the estimated intercept of the regression that captures changes in returns due to factors other than announcement surprises; and, finally, β measures the average impact of the announcement on the security under consideration.

Changes in equity prices are adjusted by changes in the overall market prices to account for the impact of broader market influences on equity values. The adjustment is often performed using the market model of Sharpe (1964):

$$R_t^a = R_t - \hat{R}_t \tag{12.1}$$

where *R*ˆ*<sup>t</sup>* is the expected equity return estimated over historical data using the market model:

$$R_t = \alpha + \beta R_{m,t} + \varepsilon_t \tag{12.2}$$

The methodology was first developed by Ball and Brown (1968), and the estimation method to this day delivers statistically significant trading opportunities.

Event arbitrage trading strategies may track macroeconomic news announcements, earnings releases, and other recurring changes in the economic information. During a typical trading day, numerous economic announcements are made around the world. The news announcements may be related to a particular company, industry, or country; or, like macroeconomic news, they may have global consequences. Company news usually includes quarterly and annual earnings releases, mergers and acquisitions announcements, new product launch announcements, and the like. Industry news comprises industry regulation in a particular country, the introduction of tariffs, and economic conditions particular to the industry. Macroeconomic news contains interest rate announcements by major central banks, economic indicators determined from government-collected data, and regional gauges of economic performance.

With the development of information technology such as RSS feeds, alerts, press wires, and news aggregation engines such as Google, it is now feasible to capture announcements the instant they are released. A welldeveloped automated event arbitrage system captures news, categorizes events, and matches events to securities based on historical analysis.

#### **TRADABLE NEWS**

#### **Corporate News**

Corporate activity such as earnings announcements, both quarterly and annual, significantly impacts equity prices of the firms releasing the announcements. Unexpectedly positive earnings typically lift equity prices, and unexpectedly negative earnings often depress corporate stock valuation.

Earnings announcements are preceded by analyst forecasts. The announcement that is materially different from the economists' consensus forecast results in a rapid adjustment of the security price to its new equilibrium level. The unexpected component of the announcements is computed as the difference between the announced value and the mean or median economists' forecast. The unexpected component is the key variable used in estimation of the impact of an event on prices.

Theoretically, equities are priced as present values of future cash flows of the company, discounted at the appropriate interest rate determined by Capital Asset Pricing Model (CAPM), the arbitrage pricing theory of Ross (1976), or the investor-specific opportunity cost:

equity price = 
$$\sum_{t=1}^{\infty} \frac{E[\text{Earnings}_t]}{(1 + R_t)^t}$$
(12.3)

where *E*[*Earningst*] are the expected cash flows of the company at a future time *t*, and *Rt* is the discount rate found appropriate for discounting time *t* dividends to present. Unexpected changes to earnings generate rapid price responses whereby equity prices quickly adjust to new information about earnings.

Significant deviations of earnings from forecasted values can cause large market movements and can even result in market disruptions. To prevent large-scale impacts of earnings releases on the overall market, most earnings announcements are made after the markets close.

Other firm-level news also affects equity prices. The effect of stock splits, for example, has been documented by Fama, Fisher, Jensen, and Roll (1969), who show that the share prices typically increase following a split relative to their equilibrium price levels.

Event arbitrage models incorporate the observation that earnings announcements affect each company differently. The most widely documented firm-level factors for evaluation include the size of the firm market capitalization (for details, see Atiase, 1985; Freeman, 1987; and Fan-fah, Mohd, and Nasir, 2008).

#### **Industry News**

Industry news consists mostly of legal and regulatory decisions along with announcements of new products. These announcements reverberate throughout the entire sector and tend to move all securities in that market in the same direction. Unlike macroeconomic news that is collected and disseminated in a systematic fashion, industry news usually emerges in an erratic fashion.

Empirical evidence on regulatory decisions suggests that decisions relaxing rules governing activity of a particular industry result in higher equity values, whereas the introduction of rules constricting activity pushes equity values down. The evidence includes the findings of Navissi, Bowman, and Emanuel (1999), who ascertained that announcements of relaxation or elimination of price controls resulted in an upswing in equity values and that the introduction of price controls depressed equity prices. Boscaljon (2005) found that the relaxation of advertising rules by the U.S. Food and Drug Administration was accompanied by rising equity values.

#### **Macroeconomic News**

Macroeconomic decisions and some observations are made by government agencies on a predetermined schedule. Interest rates, for example, are set by economists at the central banks, such as the U.S. Federal Reserve or the Bank of England. On the other hand, variables such as consumer price indices (CPIs) are typically not set but are observed and reported by statistics agencies affiliated with the countries' central banks.

Other macroeconomic indices are developed by research departments of both for-profit and nonprofit private companies. The ICSC Goldman store sales index, for example, is calculated by the International Council of Shopping Centers (ICSC) and is actively supported and promoted by the Goldman Sachs Group. The index tracks weekly sales at sample retailers and serves as an indicator of consumer confidence: the more confident consumers are about the economy and their future earnings potential, the higher their retail spending and the higher the value of the index. Other indices measure different aspects of economic activity ranging from relative prices of McDonalds' hamburgers in different countries to oil supplies to industry-specific employment levels.

Table 12.2 shows an ex-ante schedule of macroeconomic news announcements for Tuesday, March 3, 2009, a typical trading day. European news is most often released in the morning of the European trading session while North American markets are closed. Most macroeconomic announcements of the U.S. and Canadian governments are distributed in the morning of the North American session that coincides with afternoon trading in Europe. Most announcements from the Asia Pacific region, which includes Australia and New Zealand, are released during the morning trading hours in Asia.

Many announcements are accompanied by "consensus forecasts," which are aggregates of forecasts made by economists of various financial institutions. The consensus figures are usually produced by major media and data companies, such as Bloomberg LP, that poll various economists every week and calculate average industry expectations.

Macroeconomic news arrives from every corner of the world. The impact on currencies, commodities, equities, and fixed-income and derivative instruments is usually estimated using event studies, a technique that measures the persistent impact of news on the prices of securities of interest.

## **APPLICATION OF EVENT ARBITRAGE**

#### **Foreign Exchange Markets**

Market responses to macroeconomic announcements in foreign exchange were studied by Almeida, Goodhart, and Payne (1998); Edison (1996); Andersen, Bollerslev, Diebold, and Vega (2003); and Love and Payne (2008), among many others.

Edison (1996) studied macroeconomic news impact on daily changes in the USD-based foreign exchange rates and selected fixed-income securities, and finds that foreign exchange reacts most significantly to news about real economic activity, such as non-farm payroll employment figures.

| Time (ET)  | Event                                      | Prior Value  | Consensus<br>Forecast | Country     |
|------------|--------------------------------------------|--------------|-----------------------|-------------|
| 1:00 A.M.  | Norway Consumer<br>Confidence              | −13.3        |                       | Norway      |
| 1:45 A.M.  | GDP Q/Q                                    | 0.0 percent  | −0.8 percent          | Switzerland |
| 1:45 A.M.  | GDP Y/Y                                    | 1.6 percent  | −0.1 percent          | Switzerland |
| 2:00 A.M.  | Wholesale Price<br>Index M/M               | −3.0 percent | −2.0 percent          | Germany     |
| 2:00 A.M.  | Wholesale Price<br>Index Y/Y               | −3.3 percent | −6.3 percent          | Germany     |
| 3:00 A.M.  | Norway PMI SA                              | 40.8         | 40.2                  | Norway      |
| 4:30 A.M.  | PMI Construction                           | 34.5         | 34.2                  | UK          |
| 7:45 A.M.  | ICSC Goldman Store<br>Sales                |              |                       | U.S.        |
| 8:55 A.M.  | Redbook                                    |              |                       | U.S.        |
| 9:00 A.M.  | Bank of Canada Rate                        | 1.0 percent  | 0.5 percent           | Canada      |
| 10:00 A.M. | Pending Home Sales                         | 6.3 percent  | −3.0 percent          | U.S.        |
| 1:00 P.M.  | Four-Week Bill Auction                     |              |                       | U.S.        |
| 2:00 P.M.  | Total Car Sales                            | 9.6M         | 9.6M                  | U.S.        |
| 2:00 P.M.  | Domestic Car Sales                         | 6.8M         | 6.9M                  | U.S.        |
| 5:00 P.M.  | ABC/Washington Post<br>Consumer Confidence | v48          | −47                   | U.S.        |
| 5:30 P.M.  | AIG Performance of<br>Service Index        | 41           |                       | Australia   |
| 7:00 P.M.  | Nationwide Consumer<br>Confidence          | 40           | 38                    | UK          |
| 7:30 P.M.  | GDP Q/Q                                    | 0.1 percent  | 0.1 percent           | Australia   |
| 7:30 P.M.  | GDP Y/Y                                    | 1.9 percent  | 1.1 percent           | Australia   |
| 9:00 P.M.  | ANZ Commodity Prices                       | −4.3 percent |                       | New Zealand |

**TABLE 12.2** Ex-Ante Schedule of Macroeconomic Announcements for March 3, 2009

"SA" stands for "seasonally adjusted"; "NSA" indicates non–seasonally adjusted data.

In particular, Edison (1996) shows that for every 100,000 surprise increases in non-farm payroll employment, USD appreciates by 0.2 percent on average. At the same time, the author documents little impact of inflation on foreign exchange rates.

Andersen, Bollerslev, Diebold, and Vega (2003) conducted their analysis on foreign exchange quotes interpolated based on timestamps to create exact 5-minute intervals—the procedure outlined in Chapter 9 of this book. The authors show that average exchange rate levels adjust quickly and efficiently to new levels according to the information releases. Volatility, however, takes longer to taper off after the spike surrounding most news announcements. The authors also document that bad news usually has a more pronounced effect than good news.

Andersen, Bollerslev, Diebold, and Vega (2003) use the consensus forecasts compiled by the International Money Market Services (MMS) as the expected value for estimation of surprise component of news announcements. The authors then model the 5-minute changes in spot foreign exchange rate  $R_t$  as follows:

$$R_{t} = \beta_{0} + \sum_{i=1}^{I} \beta_{i} R_{t-i} + \sum_{k=1}^{K} \sum_{j=0}^{J} \beta_{kj} S_{k,t-j} + \varepsilon_{t}, \ t = 1, \ldots, T \tag{12.4}$$

where  $R_{t-i}$  is *i*-period lagged value of the 5-minute spot rate,  $S_{k,t-i}$  is the surprise component of the  $k^{\text{th}}$  fundamental variable lagged j periods, and  $\varepsilon_t$ is the time-varying volatility that incorporates intra-day seasonalities. Andersen, Bollerslev, Diebold, and Vega  $(2003)$  estimate the impact of the following variables:

- GDP (advance, preliminary, and final figures)
- Non-farm payroll
- Retail sales
- Industrial production
- Capacity utilization
- Personal income
- Consumer credit
- Personal consumption expenditures
- New home sales
- Durable goods orders
- Construction spending
- Factory orders
- Business inventories
- Government budget deficit
- Trade balance
- $\bullet$  Producer price index
- Consumer price index
- Consumer confidence index
- Institute for Supply Management (ISM) index (formerly, the National Association of Purchasing Managers [NAPM] index)
- Housing starts
- Index of leading indicators
- Target Fed Funds rate
- Initial unemployment claims

- Money supply (M1, M2, M3)
- Employment
- Manufacturing orders
- Manufacturing output
- Trade balance
- Current account
- Producer prices
- Wholesale price index
- Import prices
- Money stock M3

Andersen, Bollerslev, Diebold, and Vega (2003) considered the following currency pairs: GBP/USD, USD/JPY, DEM/USD, CHF/USD, and EUR/USD from January 3, 1992 through December 30, 1998. The authors document that all currency pairs responded positively, with 99 percent significance, to surprise increases in the following variables: non-farm payroll employment, industrial production, durable goods orders, trade balance, consumer confidence index, and NAPM index. All the currency pairs considered responded negatively to surprise increases in the initial unemployment claims and money stock M3.

Love and Payne (2008) document that macroeconomic news from different countries affects different currency pairs. Love and Payne (2008) studied the impact of the macroeconomic news originating in the United States, the Eurozone, and the UK on the EUR/USD, GBP/USD, and EUR/GBP exchange-rate pairs. The authors find that the U.S. news has the largest effect on the EUR/USD, while GBP/USD is most affected by the news originating in the UK. Love and Payne (2008) also document the specific impact of the type of news from the three regions on their respective currencies; their findings are shown in Table 12.3.

| Currency, per Love and Payne (2008) |                                |                               |                              |  |  |
|-------------------------------------|--------------------------------|-------------------------------|------------------------------|--|--|
|                                     |                                | <b>News Announcement Type</b> |                              |  |  |
| Region of News<br>Origination       | Increase in Prices<br>or Money | Increase of Output            | Increase in Trade<br>Balance |  |  |
| Eurozone, Effect<br>on EUR          | Appreciation                   | Appreciation                  |                              |  |  |
| UK, Effect on GBP                   | Appreciation                   | Appreciation                  | Appreciation                 |  |  |
| U.S., Effect on<br>USD              | Depreciation                   | Appreciation                  | Appreciation                 |  |  |

| <b>TABLE 12.3</b> Effect of Region-Specific News Announcements on the Respective |
|----------------------------------------------------------------------------------|
| Currency, per Love and Payne (2008)                                              |

## **Equity Markets**

A typical trading day is filled with macroeconomic announcements, both domestic and foreign. How does the macroeconomic news impact equity markets?

According to classical financial theory, changes in equity prices are due to two factors: changes in expected earnings of publicly traded firms, and changes in the discount rates associated with those firms. Expected earnings may be affected by changes in market conditions. For example, increasing consumer confidence and consumer spending are likely to boost retail sales, uplifting earnings prospects for retail outfits. Rising labor costs, on the other hand, may signal tough business conditions and decrease earnings expectations as a result.

The discount rate in classical finance is, at its bare minimum, determined by the level of the risk-free rate and the idiosyncratic riskiness of a particular equity share. The risk-free rate pertinent to U.S. equities is often proxied by the 3-month bill issued by the U.S. Treasury; the risk-free rate significant to equities in another country is taken as the short-term target interest rate announced by that country's central bank. The lower the riskfree rate, the lower the discount rate of equity earnings and the higher the theoretical prices of equities.

How does macroeconomic news affect equities in practice? Ample empirical evidence shows that equity prices respond strongly to interest rate announcements and, in a less pronounced manner, to other macroeconomic news. Decreases in both long-term and short-term interest rates indeed positively affect monthly stock returns with 90 percent statistical confidence for long-term rates and 99 percent confidence for short-term rates. Cutler, Poterba, and Summers (1989) analyzed monthly NYSE stock returns and found that, specifically, for every 1 percent decrease in the yield on 3-month Treasury bills, monthly equity returns on the NYSE increased by 1.23 percent on average in the 1946–1985 sample.

Stock reaction to nonmonetary macroeconomic news is usually mixed. Positive inflation shocks tend to induce lower stock returns independent of other market conditions (see Pearce and Roley, 1983, 1985 for details). Several other macroeconomic variables produce reactions conditional on the contemporary state of the business cycle. Higher-than-expected industrial production figures are good news for the stock market during recessions but bad news during periods of high economic activity, according to McQueen and Roley (1993).

Similarly, unexpected changes in unemployment statistics were found to cause reactions dependent on the state of the economy. For example, Orphanides (1992) finds that returns increase when unemployment rises, but only during economic expansions. During economic contractions, returns drop following news of rising unemployment. Orphanides (1992) attributes the asymmetric response of equities to the overheating hypothesis: when the economy is overheated, increase in unemployment actually presents good news. The findings have been confirmed by Boyd, Hu, and Jagannathan (2005). The asymmetric response to macroeconomic news is not limited to the U.S. markets. Loflund and Nummelin (1997), ¨ for instance, observe the asymmetric response to surprises in industrial production figures in the Finnish equity market; they found that higherthan-expected production growth bolsters stocks in sluggish states of the economy.

Whether or not macroeconomic announcements move stock prices, the announcements are usually surrounded by increases in market volatility. While Schwert (1989) pointed out that stock market volatility is not necessarily related to volatility of other macroeconomic factors, surprises in macroeconomic news have been shown to significantly increase market volatility. Bernanke and Kuttner (2005), for example, show that an unexpected component in the interest rate announcements of the U.S. Federal Open Market Committee (FOMC) increase equity return volatility. Connolly and Stivers (2005) document spikes in the volatility of equities constituting the Dow Jones Industrial Average (DJIA) in response to U.S. macroeconomic news. Higher volatility implies higher risk, and financial theory tells us that higher risk should be accompanied by higher returns. Indeed, Savor and Wilson (2008) show that equity returns on days with major U.S. macroeconomic news announcements are higher than on days when no major announcements are made. Savor and Wilson (2008) consider news announcements to be "major" if they are announcements of Consumer Price Index (CPI), Producer Price Index (PPI), employment figures, or interest rate decisions of the FOMC. Veronesi (1999) shows that investors are more sensitive to macroeconomic news during periods of higher uncertainty, which drives asset price volatility. In the European markets, Errunza and Hogan (1998) found that monetary and real macroeconomic news has considerable impact on the volatility of the largest European stock markets.

Different sources of information appear to affect equities at different frequencies. The macroeconomic impact on equity data appears to increase with the increase in frequency of equity data. Chan, Karceski, and Lakonishok (1998), for example, analyzed monthly returns for U.S. and Japanese equities in an arbitrage pricing theory setting and found that idiosyncratic characteristics of individual equities are most predictive of future returns at low frequencies. By using factor-mimicking portfolios, Chan, Karceski, and Lakonishok (1998) show that size, past return, bookto-market ratio, and dividend yield of individual equities are the factors that move in tandem ("covary") most with returns of corresponding equities. However, Chan, Karceski, and Lakonishok (1998, p. 182) document that "the macroeconomic factors do a poor job in explaining return covariation" at monthly return frequencies. Wasserfallen (1989) finds no impact of macroeconomic news on quarterly equities data.

Flannery and Protopapadakis (2002) found that daily returns on the U.S. equities are significantly impacted by several types of macroeconomic news. The authors estimate a GARCH return model with independent variables and found that the following macroeconomic announcements have significant influence on both equity returns and volatility: consumer price index (CPI), producer price index (PPI), monetary aggregate, balance of trade, employment report, and housing starts figures.

Ajayi and Mehdian (1995) document that foreign stock markets in developed countries typically overreact to the macroeconomic news announcements from the United States. As a result, foreign equity markets tend to be sensitive to the USD-based exchange rates and domestic account balances. Sadeghi (1992), for example, notes that in the Australian markets, equity returns increased in response to increases in the current account deficit, the AUD/USD exchange rate, and the real GDP; equity returns decreased following news of rising domestic inflation or interest rates.

Stocks of companies from different industries have been shown to react differently to macroeconomic announcements. Hardouvelis (1987), for example, pointed out that stocks of financial institutions exhibited higher sensitivity to announcements of monetary adjustments. The extent of market capitalization appears to matter as well. Li and Hu (1998) show that stocks with large market capitalization are more sensitive to macroeconomic surprises than are small-cap stocks.

The size of the surprise component of the macroeconomic news impacts equity prices. Aggarwal and Schirm (1992), for example, document that small surprises, those within one standard deviation of the average, caused larger changes in equities and foreign exchange markets than did large surprises.

#### **Fixed-Income Markets**

Jones, Lamont, and Lumsdaine (1998) studied the effect of employment and producer price index data on U.S. Treasury bonds. The authors find that while the volatility of the bond prices increased markedly on the days of the announcements, the volatility did not persist beyond the announcement day, indicating that the announcement information is incorporated promptly into prices.

Hardouvelis (1987) and Edison (1996) note that employment figures, producer price index (PPI), and consumer price index (CPI) move bond prices. Krueger (1996) documents that a decline in U.S. unemployment causes higher yields in bills and bonds issued by the U.S. Treasury.

High-frequency studies of the bond market responses to macroeconomic announcements include those by Ederington and Lee (1993); Fleming and Remolona (1997, 1999); and Balduzzi, Elton and Green (2001). Ederington and Lee (1993) and Fleming and Remolona (1999) show that new information is fully incorporated in bond prices just two minutes following its announcement. Fleming and Remolona (1999) estimate the high-frequency impact of macroeconomic announcements on the entire U.S. Treasury yield curve. Fleming and Remolona (1999) measure the impact of 10 distinct announcement classes: consumer price index (CPI), durable goods orders, gross domestic product (GDP), housing starts, jobless rate, leading indicators, non-farm payrolls, producer price index (PPI), retail sales, and trade balance. Fleming and Remolona (1999) define the macroeconomic surprise to be the actual number released less the Thomson Reuters consensus forecast for the same news release.

All of the 10 macroeconomic news announcements studied by Fleming and Remolona (1999) were released at 8:30 A.M. The authors then measure the significance of the impact of the news releases on the entire yield curve from 8:30 A.M. to 8:35 A.M., and document statistically significant average changes in yields in response to a 1 percent positive surprise change in the macro variable. The results are reproduced in Table 12.4. As Table 12.4 shows, a 1 percent "surprise" increase in the jobless rate led on average to a 0.9 percent drop in the yield of the 3-month bill with 95 percent

| Announcement         | 3-Month Bill | 2-Year Note | 30-Year Bond |
|----------------------|--------------|-------------|--------------|
| CPI                  | 0.593*       | 1.472†      | 1.296†       |
| Durable Goods Orders | 1.275†       | 2.180†      | 1.170†       |
| GDP                  | 0.277        | 0.379       | 0.167        |
| Housing Starts       | 0.670†       | 1.406†      | 0.731†       |
| Jobless Rate         | −0.939*      | −1.318†     | −0.158       |
| Leading Indicators   | 0.411†       | 0.525*      | 0.271*       |
| Non-Farm Payrolls    | 3.831†       | 6.124†      | 2.679*       |
| PPI                  | 0.768†       | 1.879†      | 1.738        |
| Retail Sales         | 0.582*       | 1.428†      | 0.766†       |
| Trade Balance        | −0.138       | 0.027       | −0.062       |

**TABLE 12.4** Effects of Macroeconomic News Announcements Documented by Fleming and Remolona (1999)

The table shows the average change in percent in the yields of the 3-month U.S. Treasury bill, the 2-year U.S. Treasury note, and the 30-year U.S. Treasury bond, corresponding to a 1 percent "surprise" in each macroeconomic announcement. \* and † indicate statistical significance at the 95 percent and 99 percent confidence levels, respectively. The estimates were conducted on data from July 1,1991 to September 29,1995.

statistical confidence and a 1.3 percent drop in the yield of the 2-year note with 99 percent confidence. The corresponding average drop in the yield of the 30-year bond was not statistically significant.

# **Futures Markets**

The impact of the macroeconomic announcements on the futures market has been studied by Becker, Finnerty, and Kopecky (1996); Ederington and Lee (1993); and Simpson and Ramchander (2004). Becker, Finnerty, and Kopecky (1996) and Simpson and Ramchander (2004) document that news announcements regarding the PPI, merchandise trade, non-farm payrolls, and the CPI move prices of bond futures. Ederington and Lee (1993) find that news-induced price adjustment of interest rate and foreign exchange futures happens within the first minute after the news is released. Newsrelated volatility, however, may often persist for the following 15 minutes.

# **Emerging Economies**

Several authors have considered the impact of macroeconomic news on emerging economies. For example, Andritzky, Bannister, and Tamirisa (2007) study how macroeconomic announcements affect bond spreads. The authors found that the U.S. news had a major impact, whereas domestic announcements did not generate much effect. On the other hand, Nikkinen, Omran, Sahlstrom, and ¨ Aij ¨ o (2006) conducted similar analysis ¨ on equity markets and found that while mature equity markets respond almost instantaneously to U.S. macroeconomic announcements, emerging equity markets are not affected. Kandir (2008) estimated macroeconomic impact on monthly returns of equities trading on the Istambul Stock Exchange, and found that the Turkish Lira/USD exchange rate, the Turkish interest rate, and the world market returns significantly affect Turkish equities, while domestic variables such as industrial production and money supply had little effect. Muradoglu, Taskin, and Bigan (2000) found that emerging markets were influenced by global macroeconomic variables, depending on the size of the emerging market under consideration and the degree of the market's integration with the world economy.

ASEAN countries, however, appear to be influenced predominantly by their domestic variables. Wongbangpo and Sharma (2002) find that local GNPs, CPIs, money supplies, interest rates, and the USD-based exchange rates of ASEAN countries (Indonesia, Malaysia, Philippines, Singapore, and Thailand) significantly influence local stock markets. At the same time, Bailey (1990) found no causal relation between the U.S. money supply and stock returns of Asian Pacific markets.

#### **Commodity Markets**

Empirical evidence in the commodity markets includes the findings of Gorton and Rouwenhorst (2006), who document that both real activity and inflation affect commodity prices. The effect of the news announcements, however, can be mixed; higher-than-expected real activity and inflation generally have a positive effect on commodity prices, except when accompanied by rising interest rates, which have a cooling impact on commodity valuations. See Bond (1984), Chambers (1985), and Frankel (2006) for more details on the relation between commodity prices and interest rates.

## **Real Estate Investment Trusts (REITS)**

Equity real estate investment trusts (REITs) are fairly novel publicly traded securities, established by the U.S. Congress in 1960. The market capitalization of all U.S.-based REITs was about \$9 million in 1991 and steadily grew to \$300 billion by 2006. A REIT is traded like an ordinary equity, but it is required to have the following peculiar structure: at least 75 percent of the REIT's assets should be invested in real estate, and the REIT must pay out at least 90 percent of its taxable earnings as dividends. Because of their high payout ratios, REITs may respond differently to macroeconomic news announcements than would ordinary equities.

The impact of inflation on REIT performance has been documented by Simpson, Ramchander, and Webb (2007). The authors found that the returns on REITs increase when inflation unexpectedly falls as well as when inflation unexpectedly rises. Bredin, O'Reilly, and Stevenson (2007) examine the response of REIT returns to unanticipated changes in U.S. monetary policy. The authors find that the response of REITs is comparable to that of equities—increase in the Federal Funds rates increases the volatility of REIT prices while depressing the REIT prices themselves.

## **CONCLUSION**

Event arbitrage strategies utilize high-frequency trading since price equilibrium is reached only after market participants have reacted to the news. Short trading windows and estimation of the impact of historical announcements enable profitable trading decisions surrounding market announcements.
### **CHAPTER 9**

#### **Directional Trading Around Events**

Many traditional low-frequency quantitative models assume several idealized market conditions. The following condition is assumed particularly often: markets instantaneously incorporate all relevant public information as soon as the information is available. Fair long-term quantitative valuation, the theory goes, is feasible only when the prices always reflect all fundamental information (see rational expectations of Muth, 1961, and the efficient markets hypotheses, Fama, 1970, for details).

Anyone who has watched the evolution of real-life financial prices surrounding a major news release has noted that the price adjustment to news is hardly instantaneous. In fact, the news "impoundment" into prices can be described as follows: volatile swings of the price that eventually settle within a certain range. The price never settles on a constant price level because a degree of volatility, however small, accompanies all market conditions. The process of the market finding its optimal postannouncement price band is often referred to as *tâtonnement,* from the French for "trial and error."

The tâtonnement toward a new optimal price happens through the implicit negotiation among buyers and sellers that is occurring in the order flow.

With news reported instantly and trades placed on a tick-by-tick basis, high-frequency traders are ideally positioned to profit from the impact of announcements on markets. By arbitraging price fluctuations surrounding each news release, HFTs high-frequency strategies further deliver a common good: they bring real-life markets ever closer to their idealized state whereby all prices are instantaneously updated with the latest news. The high-frequency strategies presented in this chapter trade on the market movements surrounding market-wide events, such as news announcements and other occurrences.

# Developing Directional Event-Based Strategies

*Directional event-based strategies* refer to the group of trading strategies that place trades on the basis of the markets' reaction to events. The events may be economic, industry, or even instrument-specific occurrences that consistently affect the instrument(s) of interest time and time again. For example, unexpected increases in the Fed Funds rates consistently raise the value of the U.S. dollar, simultaneously raising the rate for USD/CAD and lowering the rate for AUD/USD. The announcements of the U.S. Fed Funds decisions, therefore, are events that can be consistently and profitably arbitraged.

The goal of event arbitrage strategies is to identify portfolios that make positive profit over the time window surrounding each event. The time window is typically a time period beginning just before the event and ending shortly afterwards. For events anticipated ex-ante, such as scheduled economic announcements, the portfolio positions may be opened ahead of the announcement or just after the announcement. The portfolio is then fully liquidated shortly after the announcement.

Trading positions can be held anywhere from a fraction of a second to several hours and can result in consistently profitable outcomes with low volatilities. The speed of response to an event often determines the trade gain; the faster the response, the higher the probability that the strategy will be able to profitably ride the momentum wave to the post-announcement equilibrium price level. As a result, event arbitrage strategies are well suited for high-frequency applications and are most profitably executed in fully automated trading environments.

Developing an event arbitrage trading strategy harnesses research on equilibrium pricing and leverages statistical tools that assess tick-by-tick trading data and events the instant they are released. Further along in this chapter, we will survey academic research on the impact of events on prices; now we investigate the mechanics of developing an event arbitrage strategy.

Most event arbitrage strategies follow a three-stage development process:

1. For each event type, identify dates and times of past events in historical data.

2. Compute historical price changes at desired frequencies pertaining to securities of interest and surrounding the events identified in step 1.

3. Estimate expected price responses based on historical price behavior surrounding past events.

The sources of dates and times for specified events that occurred in the past can be collected from various Internet sites. Most announcements recur at the same time of day and make the job of collecting the data much easier. U.S. unemployment announcements, for example, are always released at 8:30 a.m. Eastern time. Some announcements, such as those of the U.S. Federal Open Markets Committee interest rate changes, occur at irregular times during the day and require greater diligence in collecting the data. Firms such as Reuters, Dow Jones, RavenPack, SemLab, HFTIndex.com and AbleMarkets.com distribute news and other tradeable data in machinereadable formats, further simplifying automation of event-driven trading strategies.

### What Constitutes an Event?

The events used in event arbitrage strategies can be any releases of news about economic activity, market disruptions, and other events. The key requirement for event suitability is that the chosen events are repetitive. The recurrence of events allows researchers to estimate historical impact of the events and project the effect into the future.

All events do not have the same magnitude. Some events may have positive and negative impacts on prices, and some events may have more severe consequences than others. The magnitude of an event can be measured as a deviation of the realized event figures from the expectations of the event. In economics, the deviation is frequently referred to as a "surprise." The price of a particular stock, for example, should adjust to the net present value of its future cash flows following a higher- or lower-thanexpected earnings announcement. However, if earnings are in line with investor expectations, the price should not move. Similarly, in the foreign exchange market, the level of a foreign exchange pair should change in

response to an unexpected change—for example, in the level of the consumer price index (CPI) of the domestic country. If, however, the domestic CPI turns out to be in line with market expectations, little change should occur.

Market participants form expectations about event figures well before the formal statistics are announced. Many financial economists are tasked with forecasting inflation, earnings, and other figures based on other continuously observed market and political variables, as well as pure news. When event-related forecasts become available, market participants trade securities on the basis of the forecasts, impounding their expectations into prices well before the formal announcements occur.

One of the key steps in the estimation of news impact is separating the unexpected change, or news, from the expected and priced-in component. The earliest macroeconomic event studies (see Frenkel, 1981, and Edwards, 1982, for example) assumed that most economic news developed slowly over time, and the trend observed during the past several months or quarters was the best predictor of the value to be released on the next scheduled news release day. The news, or the unexpected component of the news release, was then the difference between the value released in the announcement and the expectation formed on the basis of autoregressive analysis.

Later researchers such as Eichenbaum and Evans (1993) and Grilli and Roubini (1993) have been using such a framework to predict the decisions of the central bankers, including the U.S. Federal Reserve. Once again, the main rationale behind the autoregressive predictability of the central bankers' actions is that the central bankers are not at liberty to make drastic changes to economic variables under their control, given that major changes may trigger large-scale market disruptions. Instead, the central bankers adopt and follow a longer-term course of action, gradually adjusting the figures in their control, such as interest rates and money supply, to lead the economy in the intended direction.

The empirical evidence of the impact of news defined in the autoregressive fashion shows that the framework indeed can be used to predict future movements of securities. Yet the impact is best seen in shorter terms. Almeida, Goodhart, and Payne (1998) documented a significant

effect of macroeconomic news announcements on the USD/DEM exchange rate sampled at five-minute intervals. The authors found that news announcements pertaining to the U.S. employment and trade balance were particularly significant predictors of exchange rates, but only within two hours following the announcement. However, U.S. non-farm payroll and consumer confidence news announcements caused price momentum lasting 12 hours or more following an announcement.

Surprises in macroeconomic announcements can be measured relative to published averages of economists' forecasts. For example, every week *Barron's* and the *Wall Street Journal* publish consensus forecasts for the coming week's announcements, as do Bloomberg and Reuters. The forecasts are developed from a survey of field economists.

# Forecasting Methodologies

Development of forecasts involves event studies on very specific trading data surrounding event announcements of interest. Event studies measure the quantitative impact of announcements on the returns surrounding the news event and are usually conducted as follows:

1. The announcement dates, times, and "surprise" changes are identified and recorded. To create useful simulations, the database of events and the prices of securities traded before and after the event should be very detailed, with events categorized carefully and quotes and trades captured at high frequencies. The surprise component can be measured in two ways:

- As the difference between the realized value and the prediction based on autoregressive analysis.
- As the difference between the realized value and the analyst forecast consensus.

2. The returns corresponding to the times of interest surrounding the announcements are calculated for the securities under consideration. For example, if the researcher is interested in evaluating the impact of CPI announcements on the 1-second change in USD/CAD, the onesecond change in USD/CAD is calculated from 8:30:00 to 8:30:01 a.m.

on historical data on past CPI announcement days. (The U.S. CPI announcements are always released at 8:30 a.m. ET.)

3. The impact of the announcements is then estimated in a simple linear regression:

where *R<sup>t</sup>* is the vector of returns surrounding the announcement for the security of interest arranged in the order of announcements *ΔX<sup>t</sup>* is the vector of "surprise" changes in the announcements arranged in the order of announcements; ε*<sup>t</sup>* is the idiosyncratic error pertaining to news announcements; α is the estimated intercept of the regression that captures changes in returns due to factors other than announcement surprises; and, finally, β measures the average impact of the announcement on the security under consideration.

Changes in equity prices are adjusted by changes in the overall market prices to account for the impact of broader market influences on equity values. The adjustment is often performed using the market model of Sharpe (1964):

(1)

where the "hat" notation expresses the average estimate and is the expected equity return estimated over historical data using the market model:

(2)

The methodology was first developed by Ball and Brown (1968), and the estimation method to this day delivers statistically significant trading opportunities.

During a typical trading day, numerous economic announcements are made around the world. The news announcements may be related to a particular company, industry, or country; or, like macroeconomic news, they may have global consequences. Company news usually includes quarterly and annual earnings releases, mergers and acquisitions announcements, new product launch announcements, and the like. Industry news comprises industry regulation in a particular country, the introduction of tariffs, and economic conditions particular to the industry. Macroeconomic news contains interest rate announcements by major central banks, economic

indicators determined from government-collected data, and regional gauges of economic performance.

With the development of information technology such as RSS feeds, alerts, press wires, and news aggregation engines such as Google, it is now feasible to capture announcements the instant they are released. A welldeveloped automated event arbitrage system captures news, categorizes events, and matches events to securities based on historical analysis. Various companies offer machine-readable streams of data that can be readily parsed by a computer and used as an input to event-driven strategies. The companies with machine-readable offerings include Thomson Reuters, Dow Jones, and a large number of smaller players.

### A Practical Example

The latest figures tracking U.S. inflation are released monthly at 8:30 a.m. on prespecified dates. On release, USD/CAD spot and other USD crosses undergo an instantaneous one-time adjustment, at least in theory. Identifying when and how quickly the adjustments happen in practice, we can construct profitable trading strategies that capture changes in price levels following announcements of the latest inflation figures.

The first step in identification of profitable trading opportunities is to define the time period from the announcement to the end of the trading opportunity, known as the *event window.* We select data sample windows surrounding the recent U.S. inflation announcements in the tick-level data from January 2002 through August 2008. As all U.S. inflation announcements occur at 8:30 a.m. EST, we define 8:00 to 9:00 a.m. as the trading window and download all of the quotes and trades recorded during that time. We partition the data further into 5-minute, 1-minute, 30-second, and 15-second blocks. We then measure the impact of the announcement on the corresponding 5-minute, 1-minute, 30-second, and 15-second returns of USD/CAD spot.

According to the purchasing power parity (PPP), a spot exchange rate between domestic and foreign currencies is the ratio of the domestic and foreign inflation rates. When the U.S. inflation rate changes, the deviation disturbs the PPP equilibrium and the USD-based exchange rates adjust to new levels. When the U.S. inflation rate rises, USD/CAD is expected to

increase instantaneously, and vice versa. To keep matters simple, in this example we will consider the inflation news in the same fashion as it is announced, ignoring the market's preannouncement adjustment to expectations of inflation figures.

The sign test then tells us during which time intervals, if any, the market properly and consistently responds to announcements during our "trading window" from 8 to 9 a.m. The sample includes only days when inflation rates were announced. The summary of the results is presented in [Table 9.1.](#page-7-0)

| Estimation Frequency | U.S. Inflation Up | U.S. Inflation Down |
|----------------------|-------------------|---------------------|
| 5 minutes            | 0                 | 0                   |
| 1 minute             | 1                 | 0                   |
| 30 seconds           | 4                 | 1                   |
|                      |                   |                     |

15 seconds 5 6

<span id="page-7-1"></span><span id="page-7-0"></span>**[Table 9.1](#page-7-1)** Number of Persistent Trading Opportunities in USD/CAD Following the U.S. Inflation Rate Announcements

Looking at five-minute intervals surrounding the U.S. inflation announcements, it appears that USD/CAD reacts persistently only to decreases in the U.S. inflation rate and that reaction is indeed instantaneous. USD/CAD decreases during the five-minute interval from 8:25 to 8:30 a.m. in response to announcements of lower inflation with 95 percent statistical confidence. The response may potentially support the instantaneous adjustment hypothesis; after all, the U.S. inflation news is released at 8:30 a.m., at which point the adjustment to drops in inflation appears to be completed. No statistically significant response appears to occur following rises in inflation.

Higher-frequency intervals tell us a different story—the adjustments occur in short-term bursts. At one-minute intervals, for example, the adjustment to increases in inflation can now be seen to consistently occur from 8:34 to 8:35 a.m. This postannouncement adjustment, therefore, presents a consistent profit-taking opportunity.

Splitting the data into 30-second intervals, we observe that the number of tradable opportunities increases further. For announcements of rising inflation, the price adjustment now occurs in four 30-second postannouncement intervals. For the announcements showing a decrease in

inflation, the price adjustment occurs in one 30-second postannouncement time interval.

Examining 15-second intervals, we note an even higher number of timepersistent trading opportunities. For rising inflation announcements, there are five 15-second periods during which USD/CAD consistently increased in response to the inflation announcement between 8:30 and 9:00 a.m., presenting ready tradable opportunities. Six 15-second intervals consistently accompany falling inflation announcements during the same 8:30 to 9:00 a.m. time frame.

In summary, as we look at shorter time intervals, we detect a larger number of statistically significant currency movements in response to the announcements. The short-term nature of the opportunities makes them conducive to a systematic (i.e., black-box) approach, which, if implemented knowledgeably, reduces risk of execution delays, carrying costs, and expensive errors in human judgment.

## Tradable News

This section summarizes various event types and their impact on specific financial instruments. The impact of events is drawn from various academic sources. The time frames for the impact of the news may have shrunk considerably since the studies were first published due to proliferation of machine-readable news and general interest in this set of trading strategies. The described impact is, however, based on strong fundamental factors, and is likely to persist, even if for shorter periods of time. Some of the included studies estimate impact using low-frequency data; the high-frequency response of the variables used in studies tends to be comparable or even more pronounced.

### Corporate News

Corporate activity such as earnings announcements, both quarterly and annual, significantly impacts equity prices of the firms releasing the announcements. Unexpectedly positive earnings typically lift equity prices, and unexpectedly negative earnings often depress corporate stock valuation.

Earnings announcements are preceded by analyst forecasts. The announcement that is materially different from the economists' consensus forecast results in a rapid adjustment of the security price to its new equilibrium level. The unexpected component of the announcements is computed as the difference between the announced value and the mean or median economists' forecast. The unexpected component is the key variable used in estimation of the impact of an event on prices.

Theoretically, equities are priced as present values of future cash flows of the company, discounted at the appropriate interest rate determined by the capital asset pricing model (CAPM), the arbitrage pricing theory of Ross (1977), or the investor-specific opportunity cost:

(3) Equity price = 
$$\sum_{t=1}^{\infty} \frac{E[Earnings_t]}{(1 + R_t)^t}$$

where *E*[*Earnings<sup>t</sup>* ] are the expected cash flows of the company at a future time *t*, and *R*<sup>t</sup> is the discount rate found appropriate for discounting time *t* dividends to present. Unexpected changes to earnings generate rapid price responses whereby equity prices quickly adjust to new information about earnings.

Significant deviations of earnings from forecasted values can cause large market movements and can even result in market disruptions. To prevent large-scale impacts of earnings releases on the overall market, most earnings announcements are made after the markets close.

Other firm-level news also affects equity prices. The effect of stock splits, for example, has been documented by Fama, Fisher, Jensen, and Roll (1969), who show that the share prices typically increase following a split relative to their equilibrium price levels.

Event arbitrage models incorporate the observation that earnings announcements affect each company differently. The most widely documented firm-level factors for evaluation include the size of the firm market capitalization (for details, see Atiase, 1985; Freeman, 1987; and Fan-fah, Mohd, and Nasir, 2008).

### Industry News

Industry news consists mostly of legal and regulatory decisions along with announcements of new products. These announcements reverberate throughout the entire sector and tend to move all securities in that market in the same direction. Unlike macroeconomic news that is collected and disseminated in a systematic fashion, industry news usually emerges in an erratic fashion.

Empirical evidence on regulatory decisions suggests that decisions relaxing rules governing activity of a particular industry result in higher equity values, whereas the introduction of rules constricting activity pushes equity values down. The evidence includes the findings of Navissi, Bowman, and Emanuel (1999), who ascertained that announcements of relaxation or elimination of price controls resulted in an upswing in equity values and that the introduction of price controls depressed equity prices. Boscaljon (2005) found that the relaxation of advertising rules by the U.S. Food and Drug Administration was accompanied by rising equity values.

#### Macroeconomic News

Macroeconomic decisions and some observations are made by government agencies on a predetermined schedule. Interest rates, for example, are set by economists at the central banks, such as the U.S. Federal Reserve or the Bank of England. On the other hand, variables such as CPIs are typically not set but are observed and reported by statistics agencies affiliated with the countries' central banks.

Other macroeconomic indices are developed by research departments of both for-profit and nonprofit private companies. The ICSC Goldman store sales index, for example, is calculated by the International Council of Shopping Centers (ICSC) and is actively supported and promoted by the Goldman Sachs Group. The index tracks weekly sales at sample retailers and serves as an indicator of consumer confidence: the more confident consumers are about the economy and their future earnings potential, the higher is their retail spending and the higher is the value of the index. Other indices measure different aspects of economic activity ranging from relative

prices of McDonald's hamburgers in different countries to oil supplies to industry-specific employment levels.

<span id="page-11-1"></span>[Table 9.2](#page-11-0) shows an ex-ante schedule of macroeconomic news announcements for Tuesday, March 3, 2009, a typical trading day. European news is most often released in the morning of the European trading session while North American markets are closed. Most macroeconomic announcements of the U.S. and Canadian governments are distributed in the morning of the North American session that coincides with afternoon trading in Europe. Most announcements from the Asia Pacific region, which includes Australia and New Zealand, are released during the morning trading hours in Asia.

| Time (ET)           | Event                                   | Prior Value | Forecast | Country        |
|---------------------|-----------------------------------------|-------------|----------|----------------|
| 1:00 a.m.           | Norway Consumer Confidence              | $-13.3$     |          | Norway         |
| $1:45 \text{ a.m.}$ | GDP Q/Q                                 | 0.0%        | $-0.8\%$ | Switzerland    |
| $1:45 \text{ a.m.}$ | GDPY/Y                                  | 1.6%        | $-0.1\%$ | Switzerland    |
| 2:00 a.m.           | Wholesale Price Index $M/M$             | $-3.0\%$    | $-2.0\%$ | Germany        |
| 2:00 a.m.           | Wholesale Price $\text{Index}Y/Y$       | $-3.3\%$    | $-6.3\%$ | Germany        |
| 3:00 a.m.           | Norway PMI SA                           | 40.8        | 40.2     | Norway         |
| 4:30 a.m.           | PMI Construction                        | 34.5        | 34.2     | United Kingdom |
| 7:45 a.m.           | ICSC Goldman Store Sales                |             |          | United States  |
| 8:55 a.m.           | Redbook                                 |             |          | United States  |
| 9:00 a.m.           | Bank of Canada Rate                     | 1.0%        | 0.5%     | Canada         |
| 10:00 a.m.          | Pending Home Sales                      | 6.3%        | $-3.0\%$ | United States  |
| 1:00 p.m.           | Four-Week Bill Auction                  |             |          | United States  |
| $2:00 \text{ p.m.}$ | Total Car Sales                         | 9.6M        | 9.6M     | United States  |
| 2:00 p.m.           | Domestic Car Sales                      | 6.8M        | 6.9M     | United States  |
| 5:00 p.m.           | ABC/Washington Post Consumer Confidence | v48         | $-47$    | United States  |
| 5:30 p.m.           | AIG Performance of Service Index        | 41          |          | Australia      |
| 7:00 p.m.           | Nationwide Consumer Confidence          | 40          | 38       | United Kingdom |
| 7:30 p.m.           | GDP Q/Q                                 | 0.1%        | $0.1\%$  | Australia      |
| 7:30 p.m.           | $GDP \tY/Y$                             | 1.9%        | 1.1%     | Australia      |
| 9:00 p.m.           | ANZ Commodity Prices                    | $-4.3\%$    |          | New Zealand    |

<span id="page-11-0"></span>**[Table 9.2](#page-11-1)** Ex-Ante Schedule of Macroeconomic Announcements for March 3, 2009

Many announcements are accompanied by "consensus forecasts," which are aggregates of forecasts made by economists of various financial institutions. The consensus figures are usually produced by major media

and data companies, such as Bloomberg LP, that poll various economists every week and calculate average industry expectations.

Macroeconomic news arrives from every corner of the world. The impact on currencies, commodities, equities, and fixed-income and derivative instruments is usually estimated using event studies, a technique that measures the persistent impact of news on the prices of securities of interest.

## Application of Event Arbitrage

Event trading is applicable to many asset classes, yet the impact of each event may be different for every financial instrument. This section considers documented persistent impact of events on various financial instruments.

### Foreign Exchange Markets

Market responses to macroeconomic announcements in foreign exchange were studied by Almeida, Goodhart, and Payne (1997); Edison (1996); Andersen, Bollerslev, Diebold, and Vega (2003); and Love and Payne (2008), among many others.

Edison (1996) finds that foreign exchange reacts most significantly to news about real economic activity, such as nonfarm payroll employment figures. In particular, Edison (1996) shows that for every 100,000 surprise increases in nonfarm payroll employment, USD appreciates by 0.2 percent on average. At the same time, the author documents little impact of inflation on foreign exchange rates.

Andersen et al. (2003) conducted their analysis on foreign exchange quotes interpolated based on timestamps to create exact five-minute intervals. The authors show that average exchange rate levels adjust quickly and efficiently to new levels according to the information releases. Volatility, however, takes longer to taper off after the spike surrounding most news announcements. The authors also document that bad news usually has a more pronounced effect than good news.

Andersen et al. (2003) use the consensus forecasts compiled by the International Money Market Services (MMS) as the expected value for estimation of surprise component of news announcements. The authors then model the five-minute changes in spot foreign exchange rate *R<sup>t</sup>* as follows:

$$R_{t} = \beta_{0} + \sum_{i=1}^{I} \beta_{i} R_{t-i} + \sum_{k=1}^{K} \sum_{j=0}^{J} \beta_{kj} S_{k,t-j} + \varepsilon_{t}, t = 1, \dots, T$$

where *Rt-i* is *i*-period lagged value of the five-minute spot rate, *Sk,t-j* is the surprise component of the *k* th fundamental variable lagged *j* periods, and is the time-varying volatility that incorporates intraday seasonalities. Andersen et al. (2003) estimate the impact of the following variables:

- GDP (advance, preliminary, and final figures)
- Nonfarm payroll
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
- Producer price index
- Consumer price index
- Consumer confidence index
- Institute for Supply Management (ISM) index (formerly the National Association of Purchasing Managers [NAPM] index)
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
- CPI
- Producer prices
- Wholesale price index
- Import prices
- Money stock M3

Andersen, Bollerslev, Diebold, and Vega (2003) considered the following currency pairs: GBP/USD, USD/JPY, DEM/USD, CHF/USD, and EUR/USD from January 3, 1992, through December 30, 1998. The authors document that all currency pairs responded positively, with 99 percent significance, to surprise increases in the following variables: nonfarm payroll employment, industrial production, durable goods orders, trade balance, consumer confidence index, and the National Association of Purchasing Managers (NAPM) index. All the currency pairs considered responded negatively to surprise increases in the initial unemployment claims and money stock M3.

Love and Payne (2008) document that macroeconomic news from different countries affects different currency pairs. Love and Payne (2008) studied the impact of the macroeconomic news originating in the United States, the Eurozone, and the United Kingdom on the EUR/USD, GBP/USD, and EUR/GBP exchange-rate pairs. The authors find that the U.S. news has the largest effect on the EUR/USD, while GBP/USD is most affected by the news originating in the United Kingdom. Love and Payne (2008) also document the specific impact of the type of news from the three regions on their respective currencies; their findings are shown in [Table 9.3.](#page-14-0)

<span id="page-14-1"></span><span id="page-14-0"></span>**[Table 9.3](#page-14-1)** Effect of Region-Specific News Announcements on the Respective Currency, per Love and Payne (2008)

|                               | News Announcement Type      |                    |                           |
|-------------------------------|-----------------------------|--------------------|---------------------------|
| Region of News Origination    | Increase in prices or money | Increase of output | Increase in trade balance |
| Eurozone, Effect on EUR       | Appreciation                | Appreciation       |                           |
| United Kingdom, Effect on GBP | Appreciation                | Appreciation       | Appreciation              |
| United States, Effect on USD  | Depreciation                | Appreciation       | Appreciation              |

### Equity Markets

A typical trading day is filled with macroeconomic announcements, both domestic and foreign. How do the macroeconomic news impact equity markets?

According to classical financial theory, changes in equity prices are due to two factors: changes in expected earnings of publicly traded firms, and changes in the discount rates associated with those firms. Expected earnings may be affected by changes in market conditions. For example, increasing consumer confidence and consumer spending are likely to boost retail sales, uplifting earnings prospects for retail outfits. Rising labor costs, however, may signal tough business conditions and decrease earnings expectations as a result.

The discount rate in classical finance is, at its bare minimum, determined by the level of the risk-free rate and the idiosyncratic riskiness of a particular equity share. The risk-free rate pertinent to U.S. equities is often proxied by the three-month bill issued by the U.S. Treasury; the risk-free rate significant to equities in another country is taken as the short-term target interest rate announced by that country's central bank. The lower the risk-free rate, the lower is the discount rate of equity earnings and the higher are the theoretical prices of equities.

How does macroeconomic news affect equities in practice? Ample empirical evidence shows that equity prices respond strongly to interest rate announcements and, in a less pronounced manner, to other macroeconomic news. Decreases in both long-term and short-term interest rates indeed positively affect monthly stock returns with 90 percent statistical confidence for long-term rates and 99 percent confidence for short-term rates. (See Cutler, Poterba, and Summers,1989, for example.) Anecdotal evidence suggests that most adjustments of prices occur within seconds or minutes of the announcement time.

Stock reaction to nonmonetary macroeconomic news is usually mixed. Positive inflation shocks tend to induce lower stock returns independent of other market conditions (see Pearce and Roley, 1983, 1985, for details). Several other macroeconomic variables produce reactions conditional on the contemporary state of the business cycle. Higher-than-expected industrial production figures are good news for the stock market during recessions but bad news during periods of high economic activity, according to McQueen and Roley (1993).

Similarly, unexpected changes in unemployment statistics were found to cause reactions dependent on the state of the economy. For example, Orphanides (1992) finds that returns increase when unemployment rises, but only during economic expansions. During economic contractions, returns drop following news of rising unemployment. Orphanides (1992) attributes the asymmetric response of equities to the overheating hypothesis: when the economy is overheated, increase in unemployment actually presents good news. The findings have been confirmed by Boyd, Hu, and Jagannathan (2005). The asymmetric response to macroeconomic news is not limited to the U.S. markets. Löflund and Nummelin (1997), for instance, observe the asymmetric response to surprises in industrial production figures in the Finnish equity market; they found that higherthan-expected production growth bolsters stocks in sluggish states of the economy.

Whether or not macroeconomic announcements move stock prices, the announcements are always usually surrounded by increases in market volatility. While Schwert (1989) pointed out that stock market volatility is not necessarily related to volatility of other macroeconomic factors, surprises in macroeconomic news have been shown to significantly increase market volatility. Bernanke and Kuttner (2005), for example, show that an unexpected component in the interest rate announcements of the U.S. Federal Open Market Committee (FOMC) increase equity return volatility. Connolly and Stivers (2005) document spikes in the volatility of equities comprising the Dow Jones Industrial Average (DJIA) in response to U.S. macroeconomic news. Higher volatility implies higher risk, and financial theory tells us that higher risk should be accompanied by higher returns. Indeed, Savor and Wilson (2008) show that equity returns on days with

major U.S. macroeconomic news announcements are higher than on days when no major announcements are made. Savor and Wilson (2008) consider news announcements to be "major" if they are announcements of consumer price index (CPI), producer price index (PPI), employment figures, or interest rate decisions of the FOMC. Veronesi (1999) shows that investors are more sensitive to macroeconomic news during periods of higher uncertainty, which drives asset price volatility. In the European markets, Errunza and Hogan (1998) found that monetary and real macroeconomic news has considerable impact on the volatility of the largest European stock markets.

Different sources of information appear to affect equities at different frequencies. The macroeconomic impact on equity data appears to increase with the increase in frequency of equity data. Chan, Karceski, and Lakonishok (1998), for example, analyzed monthly returns for U.S. and Japanese equities in an arbitrage pricing theory setting and found that idiosyncratic characteristics of individual equities are most predictive of future returns at low frequencies. By using factor-mimicking portfolios, Chan et al. (1998) show that size, past return, book-to-market ratio, and dividend yield of individual equities are the factors that move in tandem ("covary") most with returns of corresponding equities. However, Chan et al. (1998, p. 182) document that "the macroeconomic factors do a poor job in explaining return covariation" at monthly return frequencies. Wasserfallen (1989) finds no impact of macroeconomic news on quarterly equities data.

Flannery and Protopapadakis (2002) found that daily returns on the U.S. equities are significantly impacted by several types of macroeconomic news. The authors estimate a generalized autoregressive conditional heteroskedasticity (GARCH) return model with independent variables and found that the following macroeconomic announcements have significant influence on both equity returns and volatility: CPI, PPI, monetary aggregate, balance of trade, employment report, and housing starts figures.

Ajayi and Mehdian (1995) document that foreign stock markets in developed countries typically overreact to the macroeconomic news announcements from the United States. As a result, foreign equity markets tend to be sensitive to the USD-based exchange rates and domestic account

balances. Sadeghi (1992), for example, notes that in the Australian markets, equity returns increased in response to increases in the current account deficit, the AUD/USD exchange rate, and the real gross domestic product (GDP); equity returns decreased following news of rising domestic inflation or interest rates.

Stocks of companies from different industries have been shown to react differently to macroeconomic announcements. Hardouvelis (1987), for example, pointed out that stocks of financial institutions exhibited higher sensitivity to announcements of monetary adjustments. The extent of market capitalization appears to matter as well. Li and Hu (1998) show that stocks with large market capitalization are more sensitive to macroeconomic surprises than are small-cap stocks.

The size of the surprise component of the macroeconomic news impacts equity prices. Aggarwal and Schirm (1992), for example, document that small surprises, those within one standard deviation of the average, caused larger changes in equities and foreign exchange markets than did large surprises.

#### Fixed-Income Markets

Jones, Lamont, and Lumsdaine (1998) studied the effect of employment and PPI data on U.S. Treasury bonds. The authors find that while the volatility of the bond prices increased markedly on the days of the announcements, the volatility did not persist beyond the announcement day, indicating that the announcement information is incorporated promptly into prices.

Hardouvelis (1987) and Edison (1996) note that employment figures, PPI, and CPI move bond prices. Krueger (1996) documents that a decline in the U.S. unemployment causes higher yields in bills and bonds issued by the U.S. Treasury.

High-frequency studies of the bond market responses to macroeconomic announcements include those by Ederington and Lee (1993); Fleming and Remolona (1997, 1998, 1999); and Balduzzi, Elton, and Green (2001). Ederington and Lee (1993) and Fleming and Remolona (1998) show that new information is fully incorporated in bond prices just two minutes following its announcement. Fleming and Remolona (1999) estimate the high-frequency impact of macroeconomic announcements on the entire

U.S. Treasury yield curve. Fleming and Remolona (1999) measure the impact of 10 distinct announcement classes: CPI, durable goods orders, GDP, housing starts, jobless rate, leading indicators, nonfarm payrolls, PPI, retail sales, and trade balance. Fleming and Remolona (1999) define the macroeconomic surprise to be the actual number released less the Thomson Reuters consensus forecast for the same news release.

<span id="page-19-1"></span>All of the 10 macroeconomic news announcements studied by Fleming and Remolona (1999) were released at 8:30 a.m. The authors then measure the significance of the impact of the news releases on the entire yield curve from 8:30 to 8:35 a.m., and document statistically significant average changes in yields in response to a 1 percent positive surprise change in the macro variable. The results are reproduced in [Table 9.4](#page-19-0). As [Table 9.4](#page-19-0) shows, a 1 percent "surprise" increase in the jobless rate led on average to a 0.9 percent drop in the yield of the 3-month bill with 95 percent statistical confidence and a 1.3 percent drop in the yield of the 2-year note with 99 percent confidence. The corresponding average drop in the yield of the 30 year bond was not statistically significant.

| Announcement         | 3-Month Bill | 2-Year Note | 30-Year Bond |
|----------------------|--------------|-------------|--------------|
| CPI                  | $0.593*$     | 1.472**     | 1.296**      |
| Durable goods orders | $1.275**$    | $2.180**$   | $1.170**$    |
| GDP                  | 0.277        | 0.379       | 0.167        |
| Housing starts       | $0.670**$    | 1.406**     | $0.731**$    |
| Jobless rate         | $-0.939*$    | $-1.318**$  | $-0.158$     |
| Leading indicators   | $0.411**$    | $0.525*$    | $0.271*$     |
| Nonfarm payrolls     | $3.831**$    | $6.124**$   | 2.679*       |
| $\text{PPI}$         | $0.768**$    | $1.879**$   | 1.738        |
| Retail sales         | $0.582*$     | $1.428**$   | $0.766**$    |
| Trade balance        | $-0.138$     | 0.027       | $-0.062$     |

<span id="page-19-0"></span>**[Table 9.4](#page-19-1)** Effects of Macroeconomic News Announcements Documented by Fleming and Remolona (1999)

#### Futures Markets

The impact of the macroeconomic announcements on the futures market has been studied by Becker, Finnerty, and Kopecky (1996); Ederington and

Lee (1993); and Simpson and Ramchander (2004). Becker, Finnerty and Kopecky (1996) and Simpson and Ramchander (2004) document that news announcements regarding the PPI, merchandise trade, nonfarm payrolls, and the CPI move prices of bond futures. Ederington and Lee (1993) find that news-induced price adjustment of interest rate and foreign exchange futures happens within the first minute after the news is released. Newsrelated volatility, however, may often persist for the following 15 minutes.

### Emerging Economies

Several authors have considered the impact of macroeconomic news on emerging economies. For example, Andritzky, Bannister, and Tamirisa (2007) study how macroeconomic announcements affect bond spreads. The authors found that the U.S. news had a major impact, whereas domestic announcements did not generate much effect. However, Nikkinen, Omran, Sahlström, and Äijö (2006) conducted similar analysis on equity markets and found that while mature equity markets respond almost instantaneously to U.S. macroeconomic announcements, emerging equity markets are not affected. Kandir (2008) estimated macroeconomic impact on the Istambul Stock Exchange, and found that the Turkish lira/USD exchange rate, the Turkish interest rate, and the world market returns significantly affect Turkish equities, while domestic variables such as industrial production and money supply had little effect. Muradoglu, Taskin, and Bigan (2000) found that emerging markets were influenced by global macroeconomic variables, depending on the size of the emerging market under consideration and the degree of the market's integration with the world economy.

Association of Southeast Asian Nations (ASEAN) countries, however, appear to be influenced predominantly by their domestic variables. Wongbangpo and Sharma (2002) find that local gross national products (GNPs), CPIs, money supplies, interest rates, and the USD-based exchange rates of ASEAN countries (Indonesia, Malaysia, Philippines, Singapore, and Thailand) significantly influence local stock markets. At the same time, Bailey (1990) found no causal relation between the U.S. money supply and stock returns of Asian Pacific markets.

### Commodity Markets

Empirical evidence in the commodity markets includes the findings of Gorton and Rouwenhorst (2006), who document that both real activity and inflation affect commodity prices. The effect of the news announcements, however, can be mixed; higher-than-expected real activity and inflation generally have a positive effect on commodity prices, except when accompanied by rising interest rates, which have a cooling impact on commodity valuations. See Bond (1984), Chambers (1985), and Frankel (2006) for more details on the relationship between commodity prices and interest rates.

#### Real Estate Investment Trusts

Equity real estate investment trusts (REITs) are fairly novel publicly traded securities, established by the U.S. Congress in 1960. The market capitalization of all U.S.-based REITs was about \$9 million in 1991 and steadily grew to \$300 billion by 2006. A REIT is traded like an ordinary equity, but it is required to have the following peculiar structure: at least 75 percent of the REIT's assets should be invested in real estate, and the REIT must pay out at least 90 percent of its taxable earnings as dividends. Because of their high payout ratios, REITs may respond differently to macroeconomic news announcements than would ordinary equities.

The impact of inflation on REIT performance has been documented by Simpson, Ramchander, and Webb (2007). The authors found that the returns on REITs increase when inflation unexpectedly falls as well when inflation unexpectedly rises. Bredin, O'Reilly, and Stevenson (2007) examine the response of REIT returns to unanticipated changes in U.S. monetary policy. The authors find that the response of REITs is comparable to that of equities —increase in the Federal Funds rates increases the volatility of REIT prices while depressing the REIT prices themselves.

## Summary

Directional trading around events generates profitability in narrow windows immediately following the news and preceding the reaction of

other market participants. Estimation of the impact of historical announcements enable profitable trading decisions surrounding market announcements.

## End-of-Chapter Questions

1. Which of the following is/is not a tradable event in the HFT sense? Why?

a. The S&P 500 registers a positive gain on market open relative to previous close.

b. Announcement of the QE3 (quantitative easing led by the U.S. Fed).

c. Regular announcement of employment figures.

2. What financial instruments can be traded on events in HFT setting?

3. Suppose a particular stock usually rises within 15 minutes of an announcement of positive changes to the U.S. nonfarm payroll. The latest announcement figures have just been released, and the change is negative. How can your system trade on the announcement?

4. Intuitively, why does something like a change in CPI affect futures prices in the short term?

5. Does high-frequency directional trading on events make markets more or less efficient?
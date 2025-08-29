# Chapter 10 **Enhancing trading** strategies

Traders routinely base their decisions on a mix of current market conditions as well as anticipating how these might change in the future. Incorporating such logic into algorithmic trading strategies is a key to enhancing their performance.

# 10.1 Introduction

Having gone through the basics of both trading algorithms and execution tactics, this chapter aims to highlight some of the ways in which they may be enhanced. These mechanisms are rule-based approaches that respond to market conditions. Though, we can only ever estimate what conditions might be like in the future.

In Chapter 5, we used charts to compare the typical order placement patterns for different trading algorithms. However, during the execution it is important to remember that we just cannot tell what the future holds, as Figure 10-1 tries to show.

![](_page_0_Figure_6.jpeg)

Figure 10-1 Uncertain market conditions

From time T to the close, we do not know exactly what will happen to the market price, volume or liquidity. Hence, trading algorithms and execution tactics are inherently reactive. If a sudden shift occurs in the marketplace, such a reactive approach can be caught out and forced to play catch up, at less favourable prices.

One way of enhancing computerised trading strategies is to incorporate short-term prediction models for key market conditions, such as volume and price. These allow strategies to take a more proactive approach, placing more passively priced orders (provided the forecasts are correct). For instance, a percent of volume (POV) algorithm that only ever trades in response to market volume could incur significant market impact, since it would always be chasing the market. A short-term prediction of trading volume allows the algorithm to layer orders, ensuring it takes part in the market volume rather than simply responding to it. Similarly, for price adaptive trading algorithms, a short-term price prediction will allow them to place appropriate limit orders to take advantage of price trends. If the prediction proves to be inaccurate, the orders may be cancelled.

Estimating potential transaction costs has also become more important, particularly for cost-based algorithms such as implementation shortfall. Many of these cost models are based on a framcwork by Robert Almgren and Neil Chriss (2000) which uses a random walk model to estimate the current market price in terms of costs.

Another potential enhancement is better handling of specific events, which in turn may be either predictable or not. For example, futures have finite lifetimes, so expiration is a predictable factor for these contracts. Whilst on witching days when major derivatives contracts expire, such as for the S&P 500 index, there will be sizable increases in trading volume, and short-term volatility, on the stock markets. Changes to stock indices are another example, since announcements are made some time before they occur. Given how many investment firms track the major indices, these changes have relatively predictable effects on the short-term trading for the affected stocks, depending on whether they are being added or removed from the index. Unpredictable events are generally triggered by information or news. They may be harder to forecast, but their short-term effects can still be quantified. For instance, trading interruptions, such as halts or volatility auctions, are usually followed by periods of much higher volatility and volumes, although these often dissipate after a few hours. In Chapter 14, we will cover the impact of news in more detail.

# 10.2 Forecasting market conditions

Traders and investors and have sought to predict prices for as long as markets have existed. Forecasting other market conditions such as volume, liquidity and volatility have also become more important.

Longer-term predictions are more useful for investment decisions. Execution is generally more focussed on short-term price trends. Therefore, the focus of this section is on shortterm predictions, typically intraday. Short-term changes in market conditions are closely related to market liquidity. Factors such as order book depth and imbalance can give vital insights for how trade flow will react in the immediate future. In fact, many short-term predictions may be based just on recent market conditions. In Chapter 15, we will see how artificial intelligence can also be used for forecasting.

# Predicting asset prices

At the simplest level, an asset's price merely represents what someone else is willing to pay. Imbalances in supply and demand can be a useful indicator for short-term price movements.

An excess of supply (or sells) should lead to a price drop whilst an excess of demand should result in a price hike. Empirical research has considered imbalances in both traded volume and order book depth to test their effectiveness.

A positive correlation between trade imbalances and subsequent price changes was found by Joey Yang (2005) in a study of trades on the Australian Stock Exchange (ASX). He confirmed that the price is more likely to rise if more of the last 30 trades were due to demand on the buy-side, as we might expect.  $\frac{1}{2}$ 

Imbalances in the best hid and offer sizes were also analysed by Yang (2005) for orders on the ASX. Using an ordered probit model, he established a strong link between future price changes and the logarithms of the best bid and offer sizes. A larger bid size implied price rises were more likely, whilst price drops were more probable when the ask size was larger. Similarly, in an earlier study, Sergei Maslov and Mark Mills (2001) tracked the best quotes on NASDAO. They focussed on the average price changes around periods when significant imbalances between best bid and offer sizes occurred.<sup>2</sup> Effectively, they were monitoring the short-term market impact of large trades, as shown in Figure 10-2.

![](_page_2_Figure_4.jpeg)

![](_page_2_Figure_5.jpeg)

Copyright © Elsevier 2001

## Figure 10-2 The market impact of a large imbalance in best bid and offer size

The positive impacts reflect a surplus of demand for the stock, whilst the negative ones represent an excess supply. Note that the effect is magnified, and more volatile, for the lower volume stocks, Broadcom Corp. (BRCM) and JDS Uniphase Corp. (JDSU), compared to that of Cisco Systems Inc. (CSCO). By normalising their data, they found an approximately linear relationship between the imbalances and short-term average price changes. Given the

 $\frac{1}{2}$  Note a potential problem with studies based on trade imbalances is the determination of whether the trade was driven by buyers or sellers, as reported by Ekkehart Boehmer and Julie Wu (2006). Most studies adopt the Lee and Ready (1991) algorithm to determine this, although this is not guaranteed to be 100% accurate. For instance, Charles Lee and Balkrishna Radhakrishna (2000) showed that up to 40% of trades observed on the NYSE could not be classified, whilst 7% were incorrectly classified. So caution must be taken when using trade-based imbalances.

 $2$  Ideally, the limits for this should be based on the average daily volume of each stock; however, for their results they found that a wholesale limit of 10,000 shares gave satisfactory results.

relatively short timescales involved (less than a minute), such trends may be more easy for a computerised system to take advantage of than a busy trader.

Several groups have studied the effect of imbalances for the whole order book. The imbalance  $I_i$  for each level j of the order book is just the value of sell orders (supply) minus the value of the corresponding buy orders (demand):

$$I_j = Q_j^s P_j^s - Q_j^d P_j^d$$

where  $Q_i$  is the quantity available at a given price  $P_i$  and the superscripts s and d correspond to supply and demand. In comparison, the weighted price  $WP_i$  is simply the average price based on the available supply and demand at a given level of the order book:

$$WP_j = \frac{Q_j^s P_j^s + Q_j^d P_j^d}{Q_j^s + Q_j^d}$$

The weighted price may also be calculated for specific portions of the order hook:

$$WP_{n_1 - n_2} = \frac{\sum_{j = n_1}^{n_2} (Q_j^s P_j^s + Q_j^d P_j^d)}{\sum_{j = n_1}^{n_2} (Q_j^d + Q_j^s)}$$

where  $n_1$  is a higher level than  $n_2$ , e.g.  $WP_{1-5}$  represents the weighted price for the first five levels of the order book. An example order book is shown in Figure 10-3 together with the associated imbalances and weighted prices for each level.

| Buys |       |       | Sells |       |          |       | Value (thousands) |           | $\text{WP}$ |
|------|-------|-------|-------|-------|----------|-------|-------------------|-----------|-------------|
| 1d   | Size  | Price | Price | Size  | ld       | Buys  | Sells             | Imbalance |             |
| DI   | 2,000 | 100   | 102   | 3,000 | S1       | 200   | 306               | 106       | 101.20      |
| D2   | 6,000 | 100   | 103   | 2,000 | S2       | 594   | 206               | $-388$    | 100.00      |
| 1)3  | 4,000 | 99    | 103   | 5,000 | S3       | 392   | 520               | 128       | 101.33      |
| D4   | 3,000 | 99    | 104   | 1,000 | S4       | 291   | 105               | $-186$    | 99.00       |
| D5   | 5,000 | 98    | 104   | 6,000 | S5       | 480   | 636               | 156       | 101.45      |
|      |       |       |       |       | $\nabla$ | 1,957 | 1,773             | $-184$    | 100.81      |

#### Figure 10-3 An example order book with its associated imbalances and weighted prices

So for the top of the order book in Figure 10-3 the imbalance and weighted prices are determined as:

 $I_1 = (3,000 \times 102) - (2,000 \times 100) = 106,000$  $WP_1 = ((2,000 \times 100) + (3,000 \times 102)) / (2,000 + 3,000) = 101.2$  $WP_{1-5} = (1,957,000 + 1,773,000) / (20,000 + 17,000) = 100.81$ 

Overall, the imbalance for the first live levels of this order book is \$-184,000, so at the moment the demand is outweighing the available supply.

Short-term returns on the ASX were examined by Charles Cao, Oliver Hansch and Xiaoxin Wang (2008). They calculated liquidity measures based on the difference between the weighted price  $WP_{nl-n2}$  and the mid-price. They concluded that there is a strong link between these imbalances and future short-term returns. Predominantly, this was for the best bid and offer, but imbalances across the rest of the order book also had an effect.

A similar approach was adopted by Jörgen Hellström and Ola Simonsen (2006) to study returns on the Stockholm Stock Exchange. They modelled the order book shape using weighted price measures  $(WP_{n!-n2} - \text{mid price})$  together with a time-adjusted variant. Their results showed that a positive skew in the order book imbalance (a surplus of supply from sell orders) increased the probability of a subsequent decrease in price. Conversely, a surplus of demand from buy orders was linked to subsequent price increases. Though, these relationships were found to be quite short lived, often less than a minute. They also confirmed that, whilst most of this effect could be explained by imbalances at the best bid and offer, taking into account the rest of the order book did have some effect.

The importance of gaps in the order book was highlighted in a study of large price changes on the London Stock Exchange by J. Doyne Farmer et al. (2004). A reasonable assumption for such changes might be large market orders sweeping deep into the order book. Still, their analysis showed that around 85% of the market orders that caused price changes matched the size at the best price. Essentially, they found the price fluctuations caused by market orders to be independent of the volume of orders. Instead, they revealed that the price jumps could be accounted for by liquidity fluctuations caused by gaps in the order book. So an order would take the available volume at the best price, leading to a price shift because the next entry in the order book was at a significantly different level. Interestingly, they found this issue affected even the most liquid stocks, although it was more prevalent for illiquid ones. They went on find that the distribution of gaps in the order book exhibited nontrivial correlations with the position in the book. This highlights the importance of looking past the best hid and offer if we do not want to noticeably affect the current price.

# Predicting trading volume

Forecasts for trading volume have generally been based on historical data, or so-called volume profiles. Whilst these can give a reasonable forecast of intraday volume trends, there is still a wide range of factors that can affect daily trading volumes. These range from seasonal factors, such as the summer holidays, to asset specific ones such as news, corporate actions or contract expiration. To improve the relevancy of these forecasts some researchers have decomposed trading volume into both market and asset-specific components.

Volume prediction is important for algorithmic trading, particularly for those algorithms based on statically determined trading schedules such as the original VWAP. If today's trade flow differs considerably from this then the algorithm may well struggle to meet its benchmark. So the performance of a VWAP algorithm often relies on the accuracy of its historical volume profile. Similarly, these are in important input for implementation shortfall models, allowing them to determine the optimal trading horizon for a given order. Short-term trading volume prediction can also be important for purely dynamic algorithms, such as percent of volume (POV). These are driven by market volume and so there is no danger of them following a target trajectory that is out of sync with the market. However, if they only ever issue orders in response to market volume, they could end up chasing the market, and so incur substantial market impact. Short-term volume predictions enable algorithms to effectively place orders in a more proactive fashion, hopefully achieving price improvement.

## Volume profiles

A common starting point when predicting trading volume is to create a volume profile based on historical data. As we saw for the VWAP algorithm in Chapter 5, this is just a matter of defining a fixed time interval and then measuring the volume of trading for each period. For example, in Figure 10-4 the daily trading volumes for Mattel Inc. are shown over 30 minute periods in terms of a percentage of the daily total, taken from a study by Dana Hobson (2006). Clearly, there can be considerable variation from day to day.

![](_page_5_Figure_2.jpeg)

Source: Hobson (2006)

Reproduced with permission from Institutional Investor

Figure 10-4 Volume profiles for Mattel Inc. in 2005

Though, when these are averaged over longer periods, e.g. a month, the commonality becomes more evident. In this case, as a U.S. stock it exhibits the typical U-shaped curve with higher volumes around the open and close, something like we can see in Figure 10-5.

![](_page_5_Figure_7.jpeg)

Figure 10-5 An average volume profile based on Figure 10-4

Obviously, the exact shape of the volume profile will differ for each asset and will also depend on the number of days chosen for the average. Over time, these patterns may well change. Therefore, one way of viewing them is a 3-dimensional plot of the historical trading volume. Figure 10-6, shows a plot for a large-cap firm, GlaxoSmithKline, taken from a

![](_page_6_Figure_1.jpeg)

Figure 10-6 Historical volume profiles for GlaxoSmithKline PLC

review by Tracy Black and Owain Self (2005). The trading volumes exhibit a relatively uniform pattern over time, with a clear increase in volume towards the close. Figure 10-7 shows the equivalent plot for the mid-cap technology firm, Logica CMG.

![](_page_6_Figure_4.jpeg)

![](_page_6_Figure_5.jpeg)

Figure 10-7 Historical volume profiles for Logica CMG PLC

In comparison, for the mid-cap firm, the high levels of variation in daily trading volumes are obvious, so much so that it is difficult to spot a daily volume trend. Also note the difference in volume scales. Overall, more liquid assets tend to have more stable daily volumes, whereas higher growth assets may exhibit much more volatility in their trading volumes. Consequently, historical trading volumes are likely to be more useful as predictors for liquid assets.

## Factors affecting trading volume

A wide range of factors can affect daily trading volumes: from general factors which apply across whole regions, or countries, to more localised, market- and asset-specific ones. Examples of general factors are seasonal and calendar-based anomalies, such as summer holidays and the "day of the week" effect. Market holidays and macroeconomic announcements are more market-specific, although they may also have regional and even global effects. Asset-specific factors tend to be based on the asset class, so for stocks this might be news announcements, corporate actions, dividends, mergers and stock splits. Expiration will be a consideration for assets that have fixed maturities such as bonds and futures.

In their aptly titled report, 'Gone Fishin': Seasonality in trading activity and asset prices', Harrison Hong and Jialin Yu (2006) studied the relationship between stock market turnover and vacations for 51 stock markets. They found that trading activity was, on average, 7.9% lower during the summer than during the rest of the year. Note that summer is defined as O3 (July, August and September) for countries in the Northern Hemisphere and Q1 (January, February and March) for those in the south. The effect was strongest for countries furthest from the equator, where summer vacations are more likely. So, the largest observed falls were 15.6% for Europe and 13.2% for North America. In Asia, they only noted a fall of 3.4%, whilst Australia and New Zealand saw a decline of 6.7% in their O1 summer. Closer to the equator, the effect was much less, for instance, only a 1.8% drop was observed for Latin American countrics.

The "day of the week" effect can also influence turnover. A study of stock market volatility and trading volume for the U.S., Canada and U.K by Halil Kiymaz and Hakan Berument (2003) found average volumes to be consistently lower on Mondays. This also ties in with an earlier study of U.K stocks by Paul Draper and Krishna Paudyal (2002), who observed lower trading volumes on Mondays as well. For currency futures, Pci Hwang Wei and Susan Zee (1998) found volumes to be lower on Mondays and Fridays. Analysis of NYSE stock trading also showed a strong "day of the week" effect, although Tarun Chordia, Richard Roll and Avanidhar Subrahmanyam (2000) noted this more as a decline of liquidity and trading activity on Fridays and an increase on Tuesdays. Many studies have found the middle of the week to have the highest volumes, for instance, Kiymaz and Berument (2003) noted that Wednesdays were the peak for the U.S. whilst it was Thursday for Canada and the U.K.

Specific holidays, such as Christmas, have a noticeable affect as well. Generally, trading volumes drop significantly on the day before the holiday. For example, Figure 10-8 shows a normalised view of trading volume for the Royal Bank of Scotland (RBS) created by Serge Darolles and Gaëlle Le Fol (2003). The proximity of Christmas and the New Year's Day means that the abnormal trading volume can persist for over a week. Note, Figure 10-8 also shows the breakdown of the volume into both stock-specific and common (or market) components, which we shall cover in the next sub-section.

In addition to seasonal effects, asset-specific factors considerably alter trading volumes. Many of these are specific events, which we will cover in more detail in section 10.3. For example, there is generally be an increased turnover on witching days, or when stocks are added to major indices. Similarly, for bonds or futures which are about to expire, there is usually a sudden decline in their trading volumes.

![](_page_8_Figure_1.jpeg)

Source: © Darolles and Le Fol (2003) Reproduced with permission from authors

Figure 10-8 Shift in trading volumes over Christmas holiday

One way of coping with these effects is to determine separate adjustments that compensate for them. These may then be applied to the historical volume profile, and compared with current market conditions to check they are reasonable. Alternatively, custom profiles could be adopted which may more accurately represent the current market trends. Although by using fewer data points, there is more risk in the estimation.

Historical volume profiles are often based on data for the previous weeks or even months. So these factors not only affect current trading, but they also alter the historical averages. For instance, the increased volumes on days when special events occur, such as triple witching, can distort the historical volume profiles for normal days. Hence, they may be excluded from the average volume calculations. Corporate actions, in particular stock splits, also pose a specific problem for the historical volume profile for stocks. Stock splits are usually used to reduce the share price of growth companies, and so encourage more trading. Splitting a \$100 share into two \$50 shares should lead to significantly higher average daily volumes. Thus, when stock splits occur we need to adjust the historical volumes accordingly, otherwise they will not properly reflect the new levels of trading.

# Decomposing trading volume

An alternative method of estimating trading volume is to break it down into its components, namely market volume and asset-specific volume. Essentially, this is the same approach as used for prices in the Capital Asset Pricing Model (CAPM). The CAPM expresses an asset's returns in terms of the expected returns from the market and those of a risk-free asset. Based on this, portfolio risk may be split into both systematic, or market, risk and idiosyncratic risk.

A two-factor model for trading volume was proposed by Andrew Lo and Jiang Wang (2000). Using this approach, turnover models were created by Serge Darolles and Gaëlle Le Fol (2003), and K.J. Cremers and Jianping Mei (2007). Both groups decomposed turnover<sup>3</sup>

<sup>&</sup>lt;sup>3</sup> Note that turnover is used as a more normalised version of trading volume. Turnover is the ratio of the traded volume to the total number of shares outstanding, so it allows for better comparisons between assets than trading volume alone.

into systematic and idiosyncratic components using principal components analysis (PCA). Darolles and Le Fol (2003) applied their model to empirical data for U.K. FTSE stocks, whilst Cremers and Mei (2007) studied NYSE and AMEX stocks.

The market component represents the normal volume that is common across all the traded assets. This should incorporate all the seasonal effects, and so is a non-stationary series (its statistical properties change over time). It may also be viewed as the long-term trading volume of the asset.

The idiosyncratic, or specific, component remains a random, or stochastic, process much like the asset price. It represents the asset-specific unexpected changes in volume.

A later study by Jedrzej Białkowski, Serge Darolles and Gaëlle Le Fol (2007) gives a detailed example of this decomposition for French CAC-40 stocks, one of which is shown in Figure 10-9.

![](_page_9_Figure_5.jpeg)

Reproduced with permission from Elsevier

Copyright © Elsevier 2007

Figure 10-9 Daily volume components for Total on September 9-10 2003

The overall turnover for the energy company Total is displayed in the top charts. This is followed by the common (or market) volume, which was determined as a historical average across all the CAC-40 stocks. Note that this common volume is identical on both days and adopts the common U-shaped pattern. The bottom charts illustrate the stock-specific volumes, which are significantly different between the two days. Thus, the daily differences may clearly be related to the specific component.

Białkowski, Darolles and Le Fol (2007) used two statistical methods for estimating these specific volumes. One was based on autoregressive moving averages (ARMA); the other used a self-extracting threshold autoregressive model (SETAR). Overall, they found that the SETAR model gave the best predictions of daily volume, although both methods were found to be better than a simple historical average. They attributed the performance of the SETARbased estimations as being due to the ability to discriminate between both turbulent and flat market periods.

# Predicting liquidity

In Chapter 8, we saw how limit order models could be used to predict the probability of execution of various limit orders. Short-term predictions of liquidity can allow trading strategies to decide whether they should be more or less aggressive when taking advantage of current market conditions.

Market depth often tends to increase throughout the day. Alexander Kempf and Daniel Mayston (2008) found this for trading on Xetra, as did Catherine D'Hondt, Rudy De Winne and Alain Francois-Heude (2004) for CAC-40 stocks on Euronext Paris. We can also see this trend in Figure 10-10, which is from a study of the Spanish Stock Exchange (SIBE) by David Abad, Sonia Sanabria and José Yagüe (2005).

![](_page_10_Figure_5.jpeg)

Source: © Abad, Sanabria and Yagüe (2005) Reproduced with permission from authors

# Figure 10-10 Intraday patterns of liquidity, trading activity in the Spanish stock market in 2002

The dashed lines highlight three distinct phases throughout the trading day. Thus, at the start of the day a period of lower liquidity lasts for around two hours, with higher spreads and relatively low quoted depths. This is then followed by an intermediate period where liquidity improves and volatility decreases. The last period is at around 3:30 pm, which coincides with the U.S. open. This leads to a considerable increase in trading volume, although there is only a slight improvement in overall liquidity.

This chart also shows the characteristic U-shaped volume profile. So, just as historical averages are used to predict intraday trading volumes, a similar approach may be taken for liquidity estimates. In periods of lower liquidity, trading strategies can estimate when the depth might improve. They may then evaluate whether the timing risk is sufficiently low to justify waiting; alternatively, they will have to issue more aggressive orders, and risk paying higher market impact costs.

Short-term liquidity predictions are also vital when seeking hidden liquidity, as we saw in Chapter 8. The concealed nature of this liquidity means that all such trading is based on estimates. This is particularly important when trying to choose between execution venues. Again, the availability of hidden liquidity often seems to increase throughout the day. Hendrik Bessembinder, Marios Panayides and Kumar Venkataraman (2008) and D'Hondt, De Winne and Francois-Heude (2004) both found this for hidden orders on Euronext. A similar trend was reported for the Spanish Stock Exchange by Ángel Pardo and Roberto Pascual (2006).

# Predicting volatility

Price volatility is an important factor for many trading strategies as it helps determine the execution probability of limit orders. Higher volatility increases the likelihood of execution since it means the observed price range is likely to be wider. However, it also means orders are more likely to become mispriced, and so increases the risk of adverse selection. Higher volatility also makes hidden order usage more likely. Hence, volatility is an important factor for limit order models, used to determine order placement, and the cost models used by shortfall-based algorithms to determine the optimal trading horizon.

As with any market condition, short-term volatility fluctuates intraday, often increasing around the market open and close, as we saw back in Figure 10-10. There are two main ways of estimating volatility, these are based on either historical data or implying it from the prices of options contracts.

# Predicting volatility with statistical methods

Historical measurement of volatility may be for a wide range of timescales, from intra-day to monthly, quarterly or even annual values. The volatility  $\sigma$  of an asset's price may be calculated from the standard deviation of its returns, using the following formula:

$$\sigma = \sqrt{\frac{1}{N-1} \sum_{t=1}^{N} (R_t - \overline{R})^2}$$
(10-1)

where  $R_t$  are the returns at time t and  $\overline{R}$  is the mean of the returns for N days. The variance is  $\sigma^2$ .

The simplest model for estimating future volatility is just to base it on the previous day's value, often referred to as the random walk model. A slight enhancement of this approach is to determine an estimate based on the average from of a range of historical volatilities. This might simply be the mean of previously calculated volatilities. Alternatively, it might be based on a moving average that just tracks the last 50 days. Exponentially weighted moving averages (EMA) give more weight to the recent values. The EMA method is used by RiskMetrics to model volatility. A detailed summary of all these techniques is provided by Ser-Huang Poon and Clive Granger (2003). They point out that one of the key issues to achieving useful estimates with these two moving average based methods is finding the optimal lag length (e.g. 50 days) or weighting scheme.

Another forecasting method is to create models based on previous values of volatility. The AutoRegressive (AR) model determines the volatility  $\sigma_i$  from the previous value  $\sigma_{i,l}$  using the following formula:

$$\sigma_{\bar{l}} = c + \sum_{i=1}^{p} a_i \sigma_{t-i} + \varepsilon_t$$

where c is a constant, each  $a_i$  is a parameter of the model and  $\varepsilon_i$  is an error term. The parameters may be estimated by carrying out least squares regressions on the data series. ARMA (AutoRegressive Moving Average) models are an extension of this approach that include a separate model based on the past volatility errors  $\varepsilon_{t-1}$ :

$$\sigma_{t} = \varepsilon_{t} + \sum_{i=1}^{p} a_{i} \sigma_{t-i} + \sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}$$

where  $\theta_i$  are the parameters for this error model.

The ARCH (AutoRegressive Conditional Heteroskedasticity) family of models represent a more sophisticated approach. The first ARCH model was proposed by Robert Engle (1982). Instead of using sample standard deviations, the ARCH model uses a common statistical method (maximum likelihood estimation) to determine the best fit for its model, for a given probability distribution. A simple ARCH model determines the conditional variance as a function of past squared returns. The Generalised ARCH (GARCH) model was initially proposed by Tim Bollerslev (1986) and Stephen Taylor (1986). GARCH allows additional dependencies on lagged values; it also assumes a Normal distribution. Poon and Granger note that GARCH is the most popular model for many time series. This has led to a range of extensions such as the exponential, EGARCH, model.

In terms of overall accuracy, the historical volatility based averages tend to give similar results to GARCH models, although some of the later models, such as EGARCH, outperform GARCH. However, Poon and Granger note that the best overall results for volatility forecasts appear to be from implied volatility.

Note this is obviously a very brief introduction to the statistical models for estimating volatility. Indeed, there are even more methods, such as stochastic volatility frameworks and regime-switching models. For further details on these, Poon and Granger (2003) is a good starting point. Also in Chapter 15, we shall see how artificial intelligence is being used to predict volatility.

## Using implied volatility

Implied volatility is based on the market prices of options contracts. Option pricing models, such as Black Scholes, allow us to determine what the market price for an option should be, given a certain asset price as well as other factors such as the maturity and interest rates. Therefore, by reversing this process we can use market prices to determine what level of volatility was used to generate them, hence the term implied volatility.

Figure 10-11 highlights the potential differences between a purely historical volatility measurement and an implied one, taken from an example for Instinet's (2006) implementation shortfall algorithm (Wizard).

![](_page_13_Figure_1.jpeg)

Figure 10-11 Historical and implied volatility, from Instinct (2006)

The chart shows the volatilities and the stock price for CV Therapcutics Inc. (CVTX) in the period 2005-6. Notice how the implied volatility suddenly jumped in early January, coinciding with the company waiting for FDA approval for its new drug. The implied volatility accurately reflects the uncertainty from the options market.

In comparison, the historical volatility based on the stock price is purely backward looking and does not reflect this risk. So investors or traders unaware of the imminent news release might underestimate the potential volatility of the stock if they focus solely on historical volatility. Hence, Instinct uses a weighted average of both historical and implied volatility for its risk estimates.

Implied volatility is not without its own problems, though. As Poon and Granger (2003) point out, the implied volatility reflects the market's expectation of what the volatility will be for the underlying asset over the option's maturity. Thus, options for the same asset, but with differing maturities, will have different implied volatilities. In practice, there are also often significant differences in the implied volatilities for options that have the same maturity but different strike prices. This phenomenon is the characteristic "volatility smile", as shown in Figure 10-12(a). If we then expand this to take account of the different maturities, we get a volatility surface, as shown in Figure  $10-12(b)$ .

Poon and Granger (2003) describe two of the main theoretical explanations for this effect, namely the distributional assumption and stochastic volatility; they also outline other potential factors, such as market microstructure and measurement errors.

The distributional assumption refers to the fact that the Black Scholes model assumes the price of the underlying asset has a Log-Normal distribution. But for many risky assets the probability of outliers is higher than expected; the distribution is said to have "fat tails" (or is leptokurtic). So, deeply out-of-the-money options can actually have a probability of exercise which is higher than that expected by the Normal distribution, leading to higher prices than predicted by Black Scholes.

Price/return distributions vary from asset to asset, but the differences are particularly strong across different asset classes. Some nice examples are illustrated in a review by Gunter Meissner and Noriko Kawano (2001). For instance, in the currency and commodities markets, returns often have symmetrical, "fat tailed" distributions. Therefore, deeply out-of-

![](_page_14_Figure_1.jpeg)

Figure 10-12 An example implied volatility (a) smile and its (b) surface

the-money options have higher volatilities for both high and low strike prices. In comparison, for the stock and bond markets distributions tend to be less symmetrical, with the "fat tails" more predominant on the left hand side of the distribution. This gives rise to a corresponding volatility skew (or grimace) with much lower implied volatilities at high strikes than at low ones.

## Using volatility indices

Volatility indices provide a measure of the market expectations for near-term volatility, often hased on the prices of stock index options. Potentially, we can also decompose volatility into market and specific components, as we did for trading volume.

The best-known volatility index is the CBOE's VIX, which was started in 1993 and has also been dubbed the "fear index". Originally, the VIX was based on the S&P 100, but in 2003 it was switched to the S&P 500, to be more representative of the U.S. market as a whole. At the same time, a more sophisticated calculation was adopted. The VIX estimation derives the expected volatility for the next 30 days by averaging the weighted prices of a wide range of puts and calls for the index. It is constantly calculated in real-time; in fact, futures and options contracts are now available based solely on the VIX.

Figure 10-13 shows the historical closes for the VIX (based on the new calculation method). The volatility during the 2007-09 financial crisis is easy to see; it is also interesting to compare this to the much smaller spikes from 2001 and 2003. Indeed, October 2008 saw the VIX reach an all time high of 89. Before this, anything over 30 had been considered high. Although it is based on the S&P 500, the VIX has become the de-facto standard for global market volatility. That said, more localised variants are also starting to appear: The VXN caters for the NASDAQ 100, and in Europe there are now indices for the DAX, FTSE 100, CAC 40 and several other major indices. There are even indices for oil, gold and the euro. Over time, the coverage of such indices will probably continue to expand.

Hence, we can also use a volatility index to provide a short-term estimate for future market volatility. This may then be combined with asset-specific estimates to generate a more accurate estimate of an asset's future volatility.

![](_page_15_Figure_1.jpeg)

Figure 10-13 VIX closing prices

# 10.3 Estimating transaction costs

Transaction cost models are essential for providing estimates of potential costs. In his guide to market microstructure for practitioners, Ananth Madhavan (2002) points out three key requirements for successful cost estimation models:

- 1. Distinguishing between permanent and temporary price impact, since current trades will affect the prices of future ones
- 2. Incorporating both order specific (size, trading horizon) and asset specific (liquidity, volatility, price level, market) factors
- 3. Varying estimates with the style of trading, so aggressive tactics which use market orders will incur higher costs than more passive ones

The basis for many of these models is a framework suggested by Robert Almgren and Neil Chriss (2000). This uses a random walk model to estimate the current market price in terms of costs, such as permanent market impact, price trending and volatility. Robert Kissell, Morton Glantz, and Roberto Malamut (2004) express this as:

$$p_{n} = p_{0} + \underbrace{\sum_{j=1}^{n} h(x_{j}) e^{-(n-j)c}}_{\substack{\text{Temporary} \\ \text{matrix} \\ \text{matrix}}} + \underbrace{\sum_{j=1}^{n} g(x_{j})}_{\substack{\text{Permanent} \\ \text{parameter} \\ \text{mapact}}} + \underbrace{\sum_{j=1}^{n} \Delta p_{j}}_{\substack{\text{Price} \\ \text{projection} \\ \text{volatility}}} + \underbrace{\sum_{j=1}^{n} \varepsilon_{j}}_{\substack{\text{Price} \\ \text{volutility}}}$$
(10-2)

where  $p_n$  is the current market price,  $p_0$  is the initial price,  $p_i$  is the price and  $x_i$  is the trade size for a transaction in period j. The functions  $g()$  and  $h()$  determine permanent and temporary impact respectively and  $\varepsilon$  represents random noise. Notice that the temporary impact is dissipated by the function  $e^{-(n-j)c}$  where c represents the rate of decay.

# Market impact

The price model shown in equation 10-2 is path dependent. As Kissell, Glantz, and Malamut (2004) point out, using it to estimate market impact requires accurate estimations of both the temporary and permanent impacts.

Early models assumed market impact functions were linear. In particular, Albert Kyle's (1985) model derived linear equilibriums from fundamental principles. Similarly, Almgren and Chriss's (2000) first impact models were also based on a linear approach.

The reality is probably something more complex and non-linear. Joel Hasbrouck (1991) reported a good fit for a square root relationship. Fabrizio Lillo, J. Doyne Farmer and Rosario Mantegna (2003) found a significant dependence on the market capitalisation. For low-cap stocks on the NYSE, they found a square root relationship held, whilst for large-cap stocks and for those listed on the LSE they noted that the relationship was more like a power law, with an exponent between 0.2 and 0.3. In the next sub-section, we will review in more detail a model by Almgren *et al.* (2005), which can cater for both linear and non-linear solutions.

Another way of tackling this problem is a more top-down approach. Kissell and Glantz (2003) adopt a cost allocation technique to estimate an average market impact cost based on aggregated trade imbalances. They then allocate this to specific trading periods rather than to individual trades. We shall review this method in more detail later.

## A trade level approach

Robert Almgren *et al.* (2005) created a model for market impact estimation using empirical data. This was based on earlier work by Almgren and Chriss (2000) and Almgren (2003). Both the permanent impact function  $g()$  and the temporary one  $h()$  were modelled as power laws:

$$g(v) = \pm \gamma \left| v \right|^{\alpha} \tag{10-3}$$

$$h(v) = \pm \eta \left| v \right|^\beta \tag{10-4}$$

where  $\nu$  is the trade rate (the order size divided by the available time). The coefficients  $\gamma$ and  $\eta$  and the exponents  $\alpha$  and  $\beta$  may be determined from linear or non-linear regressions of empirical data. Thus, one of the aims was to confirm the nature of these functions: whether they were truly linear, or were square roots or had another form.

Their empirical data consisted of a large private dataset of U.S. institutional orders from the Citigroup U.S. equity trading desks. This data also allowed details such as order side and large transactions to be identified. <sup>4</sup> Large orders were excluded, so the dataset was limited to only include orders up to 10% of the ADV. Other simplifications were to assume a constant rate of trading and to ignore co-movement between asset prices.

The model assumes that the price change is actually based on an arithmetic Brownian motion (B). Given an initial market price  $p_m$ , the permanent impact function  $g()$  determines the price drift  $(dp)$  for a given trade rate  $(v)$ :

<sup>&</sup>lt;sup>4</sup> Many academic studies have used publicly available data, often from the NYSE. Though, there are several issues with using such data. Firstly, buys and sells must be estimated, often using the Lee and Ready (1991) algorithm, since the data does not carry this information. Unfortunately, such estimations (based on comparing the order price with the best bid and offer at that time) are not 100% accurate. Also, public data does not contain any linkages between orders so large transactions may not easily be traced.

Enhancing trading strategies

$$dp = p_m g(v) d\tau + p_m \sigma \, dB \tag{10-5}$$

where  $\sigma$  is the volatility and  $\tau$  represents "volume time" (the fractional average of the ADV which has executed so far). The temporary impact function  $h()$  is used to determine the average execution price  $(\overline{p})$ :

$$\overline{p}(\tau) = p(\tau) + p_m h\left(\frac{X}{T}\right) \tag{10-6}$$

where  $X$  is the order size and  $T$  is the time.

Impact cost models were derived by integrating equations 10-5 and 10-6. They were then normalised so as to be able to use them across the wide range of assets from their dataset. Hence, the asset specific volatility ( $\sigma$ ) was included, and the trading rate (X/T) was adjusted by dividing by the average daily volume  $(V)$ . The resultant models for permanent and temporary impact  $(I)$  are:

$$I_{perm} = \sigma T g \left(\frac{X}{VT}\right) + (noise) \tag{10-7}$$

$$I_{temp} = I_{real} - \mu I_{perm} = \sigma h \left(\frac{X}{VT}\right) + (noise) \tag{10-8}$$

Notice that temporary impact is expressed in terms of the realised and permanent impacts. Almgren *et al.* (2005) assume that the adjustment factor  $\mu = 0.5$ . The generic noise factor represents an error expression for each of the estimations.

In addition to normalising the impact functions, they also checked for any asset specific dependencies. They discovered that an additional liquidity factor  $(L)$  was required for the permanent impact cost function. <sup>5</sup> This factor is based on the shares outstanding  $(\Theta)$  and the average daily volume  $(V)$  (effectively this is the inverse turnover):

$$L = \left(\frac{\Theta}{V}\right)^{\delta}$$

No such modifications were found to be required for the temporary impact function.

Finally, the power law impact functions, 10-3 and 10-4, were substituted into equations 10-7 and 10-8 to give:

$$\frac{I_{\text{perm}}}{\sigma} = \gamma T \operatorname{sign}(X) \left| \frac{X}{VT} \right|^{\alpha} \left( \frac{\Theta}{V} \right)^{\delta} + (noise) \tag{10-9}$$

$$\frac{I_{real} - \mu I_{perm}}{\sigma} = \eta \, sign(X) \left| \frac{X}{VT} \right|^{\beta} + (noise) \tag{10-10}$$

To solve the values of the exponents Almgren et al. (2005) used a modified Gauss-Newton optimization algorithm. For their data sct, this resulted in the approximate values:  $\alpha \approx 0.89$ 

<sup>&</sup>lt;sup>5</sup> Almgren et al (2005) also considered market capitalisation but only observed a weak dependence on the price effect so they opted to use the simpler shares outstanding measure.

$$\begin{array}{c} \beta \approx 0.60 \\ \delta \approx 0.27 \end{array}$$

They concluded that a linear function for permanent impact was feasible, since  $\alpha$  was so close to one. These results also confirmed the concave nature of the temporary impact function since  $\beta < 1$ . However, they found in favour of a 3/5ths power law, rather than the square root model. The liquidity factor  $\delta$  also seems reasonable, suggesting that impact costs are higher for assets with lower average daily volumes.

These exponents were then used to determine the coefficients  $\gamma$  and  $\eta$ . Almgren *et al.* (2005) termed these the "universal coefficients of market impact" since they found them to hold for their entire data set:

$$\begin{array}{l}\n\gamma \approx 0.314 \\
\eta \approx 0.142\n\end{array}$$

Therefore, by substituting these values into equations 10-9 and 10-10 they were able to accurately estimate market impact costs for any asset from their dataset using the following:

$$I_{perm} = \gamma \sigma \frac{X}{V} \left(\frac{\Theta}{V}\right)^{1/4} + (noise) \tag{10-11}$$

$$I_{real} = \mu I_{perm} + sign(X) \eta \sigma \left| \frac{X}{VT} \right|^{3/5} + (noise)$$
 (10-12)

It is important to note that their study was for U.S. equities. They concluded that the coefficients, possibly the exponents and maybe even the functional forms might be significantly different across different markets as well as over time. For this reason, such models require careful calibration for each market before use.

**Example 10-1:** Almgren *et al.* (2005) provide an example estimating the impact costs of buy orders equivalent to 10% of the ADV of IBM and DRI, as shown in Table 10-1, Using their cost model, let's work through these calculations for the potential market impact costs:

In this case, IBM is assumed to have an ADV of 6.561 million, from an outstanding total of 1,728 million shares, and a daily volatility of 1.57%.

Therefore, we can estimate the permanent impact by inputting these values into equation  $10-11:$ 

 $I_{perm} = 0.314 * 1.57 * 0.1 * (1,728/6.561)^{1/4} = 0.20 = 20$  bps.

Similarly, the realized market impact may then be determined using equation 10-12. If we try to work the trade over half the trading day then  $T=0.5$ :

$$I_{real} = 0.5 * 0.20 + (\text{sign}(0.6561) * 0.142 * 1.57 * 0.1/0.5]^{3/5}) = 0.18 = 18 \text{ bps}.$$

The temporary market impact may then be calculated using equation 10-8:

$$I_{temp} = 0.18 - (0.5 * 0.20) = 0.08 = 8$$
 bps

Table 10-1 shows the market impact estimates for both IBM and DRI for a range of trade durations, from 0.1 to 0.5 of a day. The costs for DRI are higher than those for IBM; this is mainly due to its higher volatility. If we normalise the market impacts, by dividing them by the relative volatilities, we can see that the order DRI should actually have a lower permanent impact cost. This makes sense, since DRI has a larger turnover so trading 10% of the ADV should have less impact than for IBM. Therefore, DRI has a lower normalised permanent impact  $(0.096)$  compared to IBM  $(0.126)$ . The normalised temporary impacts are the same, since the cost is not dependent on asset specific properties.

|                                           |                   |        | IBM   |                   |       | $\text{DRI}$ |       |
|-------------------------------------------|-------------------|--------|-------|-------------------|-------|--------------|-------|
| Average daily volume                      | $6.561 \text{ M}$ |        |       | $1.929 \text{ M}$ |       |              |       |
| Shares outstanding                        | $\Theta$          | 1728 M |       |                   | 168 M |              |       |
| Inverse turnover                          | $\Theta/V$        | 263    |       |                   | 87    |              |       |
| Daily volatility( $\%$ )                  | $\sigma$          | 1.57   |       |                   | 2.26  |              |       |
| Normalized trade size                     | X/V               | 0.1    |       |                   | 0.1   |              |       |
| Norm. perm impact<br>$I_{perm}/\sigma$    |                   | 0.126  |       |                   | 0.096 |              |       |
| Permanent impact bps<br>perm              |                   | 20     |       |                   | 22    |              |       |
| Trade duration (days)                     |                   | 0.1    | 0.2   | 0.5               | 0.1   | 0.2          | 0.5   |
| Normalized temporary<br>$I_{temp}/\sigma$ |                   | 0.142  | 0.094 | 0.054             | 0.142 | 0.094        | 0.054 |
| Temporary impact bps                      | $I_{temp}$        | 22     | t5    | 8                 | 32    | 21           | 12    |
| Realized impact bps                       | $I_{real}$        | 32     | 25    | 18                | 43    | 32           | 23    |

Source: Atmgren et al. (2005)

# Table 10-1 Cost estimate details for Example 10-1

# A cost allocation approach

Kissell and Glantz (2003) take the opposite approach, using a top-down cost allocation model to estimate market impact. This method has proven capable of estimating costs at both the asset and portfolio level. The following provides a brief summary of this model, but for more detailed analysis please see Kissell and Glantz (2003).

The market impact portion of equation 10-2 consists of a permanent impact function  $g(x)$ and a temporary impact function  $h(x)$ :

$$MI(x_j) = \sum_{j=1}^{n} h(x_j) e^{-(n-j)c} + \sum_{j=1}^{n} g(x_j)$$
(10-13)

The Kissell and Glantz (2003) model relies on the following assumptions:

- Market impact costs are the same for buys and sells.<sup>6</sup>
- Temporary market impact does not persist beyond the current period.  $\bullet$
- Only liquidity demanding orders pay temporary market impact. ٠
- All orders have permanent impact.

Based on these assumptions, they then derive average costs for both temporary  $(h)$  and permanent  $(\overline{g})$  impact in \$/share:

<sup>&</sup>lt;sup>6</sup> Although there is evidence that sells may be more costly, they note that the estimates may be corrected with an adjustment to accommodate this.

$$\overline{h} = \frac{\sum_{j \in side} x_j h}{\sum_{j \in side} x_j} = \frac{b_1 I}{V_{side}} \quad \overline{g} = \frac{\sum_{j=1}^n \sum_{i=1}^j x_i g}{\sum_{j=1}^n x_j} = \frac{(1 - b_1)I}{Q}$$

where I is the total impact cost and Q is the net imbalance between buys and sells. They note that only liquidity demanders pay temporary impact cost, so  $V_{side}$  is the traded volume from liquidity demanders (on the same side as the imbalance or  $j \in side$ ). The factor  $b_1$ represents the percentage of temporary impact, so  $(1 - b_1)$  equals the percentage of permanent impact.

These averages may then be used to describe the market impact:

$$MI_{\$}(X) = X \cdot \left(\frac{b_1 I}{V_{side}} + \frac{(1 - b_1)I}{Q}\right) \tag{10-14}$$

Kissell and Glantz found that the proportion of temporary impact in any given trading period k was equal to the percentage imbalance at that time  $(a_k/O)$ :

$$MI_{\$}(x_k) = \sum_{k=1}^{n} x_k \left(\frac{q_k}{Q} \cdot \frac{b_1 I}{V_{side}} + \frac{(1-b_1)I}{Q}\right)$$

The market impact may be restated in terms of just order details and expected market volume by using the following assumptions:

- the imbalance is equal to the order size  $(Q = X)$
- market volume is distributed evenly between buys and sells

Thus, the liquidity demander volume  $v_{side}$  may be restated in terms of the order size  $x_k$  and the expected volume for that period  $v_k^7$ , i.e.  $v_{side} = x_k + 0.5 v_k$ . Therefore:

$$MI_{\$}(x_k) = \sum_{k=1}^{n} x_k \left( \frac{b_1 I x_k}{X \cdot (x_k + 0.5v_k)} + \frac{(1 - b_1)I}{X} \right)$$

Finally, this may be rearranged to show the temporary and permanent components more clearly:

$$MI_{\S}(x_k) = \underbrace{\sum_{k=1}^{n} \frac{b_1 I x_k^2}{X \cdot (x_k + 0.5v_k)}}_{Temporary} + \underbrace{(1 - b_1)I}_{Permanent}$$
(10-15)

Equation 10-15 may be used to determine the market impact solely from the impact  $I$ , the order details (total size X and order size  $x_k$  for period k) and the expected volume for that period  $v_k$ .

In order to actually estimate the model parameters, Kissell and Glantz rearranged the market impact cost for an order (equation 10-14) to be the product of two functions, allowing

 $7$  Kissell and Glantz (2003) also discuss alternatives for situations where market volumes are not evenly distributed between buys and sells.

estimation using non-linear regressions. This is achieved by assuming the order runs over a whole day, with a quantity X equal to the net imbalance O, and by substituting  $n^{-1} = O/V_{\text{side}}$ . Hence, equation 10-14 may be rearranged to:

$$MI_{\$}(X=Q) = \frac{b_1 IQ}{V_{side}} + (1-b_1)I = I(Q,\sigma) \cdot (b_1 \eta^{-1} + (1-b_1))$$

Finally, both the cost and imbalance are normalised to allow estimation across a wider range of data. The imbalance is restated as Z, a percentage of the ADV, and the cost (in basis points) may be expressed as the product of both an instantaneous impact function  $(I_{bp}^*(Z,\sigma))$  and a dissipation function  $(d(\eta))$ :

$$MI_{bp} = I_{bp}^{\dagger}(Z, \sigma) \cdot d(\eta) \tag{10-16}$$

Three possible structures for this instantaneous market impact function were investigated by Kissell and Glantz (2003):

Linear: 
$$I_{bp}^{*}(Z,\sigma) = a_{1}Z + a_{2}\sigma + a_{3} = (8Z + 0.30\sigma + 90)$$
  
Non linear:  $I_{bp}^{*}(Z,\sigma) = a_{1}Z^{a_{2}} + a_{3}\sigma + a_{4} = (35Z^{0.65} + 0.30\sigma + 15)$  (10-17)  
Power function:  $I_{bp}^{*}(Z,\sigma) = a_{1}Z^{a_{2}}\sigma^{a_{3}} = (25Z^{0.38}\sigma^{0.28})$ 

They used non-linear regression to derive estimates for each of these models, from samples with a range of sizes, volatilities and participation rates. The preferred results for each model are shown on the right hand side. Interestingly, the regression errors were found to be lower for the non-linear and power function based models, implying that the true relationship between impact cost and size is indeed non-linear.

The results proved to be consistent for both size and volatility; but as with any model, we still need to recalibrate it to find the most suitable estimates for specific markets.

Kissell and Glantz (2003) also determined an estimate for the dissipation function as:

$$d(\eta) = (0.95\eta^{-1} + 0.05)$$

The 95% was found in most of their regressions, and appeared to be time invariant and independent of size. Substituting this back into equation 10-16 gives:

$$\hat{I}_{\$} = I_{\$} \cdot (0.95\eta^{-1} + 0.05) = \underbrace{0.95I_{\$} \cdot \eta^{-1}}_{Temporary \; impact} + \underbrace{0.05I_{\$}}_{Permanent \; impact} \tag{10-18}$$

So 95% of the total market impact costs are temporary, the cost of demanding liquidity. Therefore, regardless of trading strategy, a 5% permanent impact will result, reflecting the information content of the order.

Let's now put this in practice with an example, loosely based on ones from Kissell and Glantz (2003).

Example 10-2: Consider an order to buy 100,000 EFG, assuming a current price of \$50, a daily volatility of 200 bps and an ADV of 1,000,000.

In order to estimate the market impact we will first need a figure for the instantaneous

impact cost. Using the estimates shown for equation 10-17, we can substitute Z with 10 (since 100,000 is 10% of the ADV) and  $\sigma$  is 200 bps:

 $I^* = (8*10 + (0.3*200) + 90) * 10^{-4} * 50 * 100,000 = $115,000$ Linear: Non-linear:  $I^* = (35*10^{0.65} + (0.3*200) + 15) * 10^{-4} * 50 * 100,000 = $115,670$  $I^* = (25*10^{0.38} * 200^{0.28}) * 10^{-4} * 50 * 100.000 = $132.190$ Power:  $I^* = 120.953$ Average

Thus, the average instantaneous market impact is approximately \$120,000.

We can now feed this instantaneous market impact into equation 10-15 to estimate the overall market impact. Table 10-2 shows an example trading strategy together with the expected market volumes.

| Period                                 |         |         |         |         |         |           |
|----------------------------------------|---------|---------|---------|---------|---------|-----------|
| Shares                                 | 20,000  | 15,000  | 10,000  | 25,000  | 30.000  | 100,000   |
| $E(Mkt \text{ volume})$                | 250,000 | 150.000 | 100,000 | 250,000 | 250,000 | 1,000,000 |
| Temporary order<br>$\text{impact ($)}$ | 3.145   | 2,850   | 1,900   | 4.750   | 6.619   | 19.264    |

Table 10-2 Execution details for Example 10-2

Based on this, and using equation 10-15, we can then determine each child order's temporary impact, as shown in the last row. For instance, in the first period the order size  $x_k$ is 20,000, whilst the expected volume  $v_k$  is 250,000. Therefore, using equation 10-15 the temporary impact for period  $(1)$  is defined as:

Temporary impact (1) =  $0.95 \times 120,000 \times (20,000)^2$ /  $100.000 \times (20,000 + 0.5 \times 250,000)$  $=$  \$3,145

Note, this assumes we continue to use the same  $0.95:0.05$  ratio as we saw in equation 10-18, so  $b_1 = 0.95$ .

As we can see from Table 10-2, the total temporary impact is \$ 19,264. Estimating the permanent impact is much easier since it is just a fixed proportion of the instantaneous impact. Therefore:

| Temporary impact | $=$ \$ 19,264                                      |
|------------------|----------------------------------------------------|
| Permanent impact | $= (1-0.95) * 120,000 = 6,000$                     |
| Market impact    | $=$ \$ 19,264 + \$ 6,000 $=$ \$ 25,264 $=$ 50 bps. |

So with a minimum of required data (price, volatility, ADV) we are able to use the Kissell and Glantz model to provide estimates for both the permanent and temporary market impact.

# Timing risk

Timing risk reflects the uncertainty of the transaction cost estimate. Price volatility and liquidity risk are the two main sources of this uncertainty, although other factors such as spread risk may also be considered.

To make the determination of timing risk slightly easier Kissell and Glantz (2003) assume that volume and price movement are independent. This enables them to determine the price volatility and liquidity risk separately:

Enhancing trading strategies

$$\Re(\phi) = \sqrt{\frac{\sigma^2(\mu(x_k))}{\text{Price volatility}} + \frac{\sigma^2(\kappa(x_k))}{\text{Liquidity risk}}}$$
(10-19)

The price risk for a trading strategy represents the volatility exposure for the remaining position. Hence, for a discrete trading strategy Kissell and Malamut (2005b) define this as:

$$\Re(x_k) = p_0 \sqrt{\sum_{j=1}^n r_j^2 \cdot \frac{t\sigma^2}{n}}$$

where r is the residual position and  $t\sigma^2/n$  is the per period variance.

The liquidity risk accounts for the variability of liquidity during the trading period. In turn, this affects the market impact estimations. For example, a sudden drop in liquidity will mean orders incur higher market impacts than expected. Kissell and Glantz use the unadjusted temporary impact function from equation 10-15 to determine the liquidity risk. This is beyond the scope of this book, but more details may be found in Kissell and Glantz (2003).

# 10.4 Handling special events

Computerised trading strategies can react to changing market conditions extremely quickly. We have already seen how short-term predictions can enable them to make more proactive decisions about order placement. Another way of achieving this is to build in rules to recognise and react to specific market events. For instance, a futures contract has a set expiry date; we know from empirical evidence that approaching this date much of the trading volume will switch to the next contract. Therefore, adjustments may be built in to ensure that as it reaches maturity the trading volume estimates are realistic.

These events may be highly predictable, such as contract expiration, or they may be more unexpected, such as a trading interruption due to news. Often they result in sudden rises in volatility and corresponding drops in liquidity. However, once the event has been recognised we can use historical reactions as a guideline, providing short-term predictions for how market conditions will change, and how long this might last. This should help the strategy react more like a real trader might.

# Predictable events

Some events happen at set dates or they are pre-announced, so there is a high degree of certainty about them. Thus, it is relatively easy to create custom rules to be applied on these dates. Good examples of this are:

- New bond issues
- Futures contract expiration
- $\bullet$ Witching days, when futures and options expire together
- Stock index rebalances

In the following sub-sections, we shall look at empirical examples of these events and examine how they affect market conditions.

# New bond issues

For regular issuers of bonds, most typically governments, new issues tend to attract higher levels of liquidity than the contracts that they have effectively replaced. For example, the

U.S. Treasury distributes new issues of 1, 3 and 6-month bills every week, whilst issuance of 2 and 5-year notes is monthly, 10-year notes is quarterly and 30-year bonds is semi-annual. The current issue of any given U.S. Treasury is said to be "on the run". So every week, month or quarter a new batch of Treasury securities become "on the run" and the bills/notes/bonds they have replaced are said to be "off the run".

A study by Michael Barclay, Terrence Hendershott, and Kenneth Kotz (2006) found that once Treasuries become "off the run" their trading volume rapidly drops by 90% within a matter of days. This is illustrated in Figure 10-14, which is based on average trading volumes between January 2001 and November 2002.

![](_page_24_Figure_3.jpeg)

Source: Barclay, Hendershott, and Kotz (2006), Journal of Finance, Wiley-Blackwell Reproduced with permission from publisher

## Figure 10-14 Trading volume for ou- and off-the-run U.S. Treasuries

The liquidity of new issues means they can attract a slight premium over their "off the run" equivalents. David Goldreich, Bernd Hanke and Purnendu Nath (2005) found an average premium of 1.5 basis points (bps) for 2-year notes. This dissipates to zero by the time of the next monthly issue. A higher premium of around 12 bps was observed for 30year bonds by Arvind Krishnamurthy (2002).

## Futures contract expiration

Futures have a specific expiration date; just prior to this the exchanges re-designate the lead contract, such as transferring from the June to the September. Changing the lead causes a considerable shift in trading volume as hedgers roll their positions onto the new contract.

Figure 10-15 illustrates this effect for the CME S&P 500 futures contract, taken from a study by Adam Schwartz and Bonnie and Robert Van Ness (2004). On the right hand side we can see that a brand new futures contract starts out with relatively low trading volumes. When the lead (or front-month) future has eight days left to maturity the lead is then switched to the next to expire (next-out) contract. The volume for the former lead contract has a final flurry before suddenly declining, shown at the eight-day marker in Figure 10-15.

For the new lead future, there will be a corresponding surge in trading volume, which we can see at the 98 days to expiry marker. During these crossovers the combined volume of

![](_page_25_Figure_1.jpeg)

Source: Schwartz, Van Ness and Van Ness (2004), Journal of Futures Markets Copyright 2004 John Wiley & Sons, Inc. Reprinted with permission of John Wiley & Sons, Inc.

#### Figure 10-15, The daily volume and open interest of $S\&P$ 500 futures for 1999-2000

both contracts can actually see a net increase of around 30%, as observed for the S&P 500 by Ira Kawaller, Paul Koch and John Peterson (2001). They also found that the volatility of the contracts is closely linked to their trading volume. Hence, the lead contract has consistently lower volatility than the next-out contract.

Figure 10-15 also displays the open interest, which reflects the actual number of outstanding contracts. Again, we can see this suddenly climbs around the 98-day marker, and falls around the eight-day marker. In between these two peaks, the open interest remains relatively static over this period, whilst the trading volume is noticeably lower. This phase represents the secondary trading of contracts.

One way of handling this expiry-related seasonality for trading volume data is provided by Phil Holmes and Jonathan Rougier (2005). They used the change in open interest as an adjustment for the trading volume, so when a contract becomes lead there will be a negative adjustment. This approach was successfully used to interpret the significance of trading volumes for the S&P 500, U.K. long gilts and Brent crude contracts.

# Witching days

Witching days occur when several classes of derivatives, for the same underlying asset, all expire on the same date. This is best typified for stock indices where the expiration of index futures and options as well as equity options is known as "triple witching". The introduction of single stock futures has added even more volume, together with the more cumbersome moniker "quadruple witching". The largest witching day is in the U.S., when the quarterly expirations of S&P 500 derivatives converge. A detailed review of this, and its effects on trading at both NYSE and NASDAQ, is provided by Michael Barclay, Terrence Hendershott and Charles Jones (2006). The volumes involved on witching days can be huge, for instance, in terms of S&P 500 futures alone they note that since late 2004 between \$50-75 billion are settled on each witching day.

Arbitrageurs account for a sizeable proportion of the volume during witching days. They maintain hedged positions in the cash and derivative markets, since the derivatives usually settle in cash. At expiration, they need to closeout their cash market positions. To make a profit they must target the settlement price of the derivative contracts. Therefore, on witching days the cash markets receive considerable additional order flow from arbitrageurs. For

instance, Barclay, Hendershott and Jones (2006) note their activity can increase up to 50 times on witching days, taking normal arbitrage volumes of \$0.24 million per stock up to \$12.74 million on NYSE, based on data from 2003 to O3 2005. These shifts can significantly alter the normal balance between supply and demand, potentially causing large, but transient, price changes.

The short-term effects on trading volume for both NYSE and NASDAQ are shown in Figure 10-16. This plots the ratio of witching day volume compared to normal volumes, based on averages for each quarter from 1998 to Q3 2004. Thus, on witching days they found the NYSE opening trade volume was, on average, around seven times larger.

![](_page_26_Figure_3.jpeg)

![](_page_26_Figure_4.jpeg)

## Figure 10-16 Relative Witching day trading volume

The 2005 NYSE and t figures actually showed a ten times increase in volumes, with average opening volumes worth \$15 million per stock. Similarly, on NASDAO pre-open volumes reached over five times their usual levels. In both markets, a higher volume persisted after the open. Though, this dissipated rapidly with volumes returning back to their normal levels by around 10am.

A similar effect was observed for short-term volatility, as shown in Figure 10-17. Again, both markets saw a considerable jump in volatility on the morning of the witching. For the NYSE, Barclay, Hendershott and Jones (2006) determined an average increase of nearly 28 bps, whilst an excess of 64 bps was found for NASDAO. As with volume, both markets also saw a rapid reduction in the excess volatility once the opening auction was completed. Though, by around 10am both markets returned to normal.

The study by Barclay, Hendershott and Jones (2006) is clearly also an interesting comparison between the two major U.S. markets. Some of the differences, particularly in terms of volatility, may be attributed to the variety of companies traded on each exchange.

They also note that the NASDAQ's introduction of an opening call auction in 2004 significantly improved its efficiency at handling witching days. In fact, they suggest that this may have contributed to the 50% jump in open interest in the  $\&P$  500 which occurred in November 2004. This may have also helped triple the witching volume on the NYSE.

![](_page_27_Figure_1.jpeg)

![](_page_27_Figure_2.jpeg)

# Figure 10-17 Excess Witching day volatility

## Index Rebalancing

Stock indices are important benchmarks. In order to accurately reflect the markets they serve periodic rebalances are required. These ensure stocks that now meet the requirements for the index are added, and those that fail to meet them are removed. Hence, by rebalancing indices, such as the FTSE 100 or the S&P 500, manage to keep representing the major stocks for their respective markets.

Since so many investment firms track the major stock indices any such changes are publicised well before they actually happen. This gives the investors sufficient warning to realign their portfolios. To minimize their tracking error, index funds buy stocks added to the index, and sell those that are removed. So being included in a major index can lead to a sudden increase in demand for a company's shares. This can lead to a permanent improvement in its liquidity, in addition to improved coverage by analysts. Numerous studies have found that stocks that are added to an index see an abnormal increase in their returns whilst the stocks that are removed see a decrease.

A lot of research has focussed on the S&P 500, which is hardly surprising given the vast amount of assets that are benchmarked to this index.<sup>8</sup> Since 1989 Standard and Poor's have pre-announced adjustments a week in advance. Honghui Chen, Gregory Noronha and Vijay Singal (2006) analysed the returns for stocks involved in a rebalance, from before the initial announcement to over two months after the index change. Figure 10-18 shows the effect on the prices of these stocks for the period 1989-2002.

On announcement day, abnormal returns were, on average, +5.12% for additions, experienced by over 94% of the sample firms. This increased to  $+8.37\%$  for the day of the actual rebalance. In contrast, stocks being removed from the index saw, on average, an 8% drop in returns by the day of the announcement, followed by a further decline to  $-14\%$  on the effective date. Unlike the additions, though, this price effect did not appear to be permanent,

<sup>&</sup>lt;sup>8</sup> Madhavan and Ming (2003) give a conservative estimate of over \$830 billion.

![](_page_28_Figure_1.jpeg)

Source: Chen, Noronha and Singal (2006) Reproduced with permission from JOIM

Figure 10-18 Average price responses to S&P 500 rebalances (1989-2002)

The negative effect disappeared within 60 days of the rebalance.

Similar results for the period between the announcement and the effective date were observed by Ananth Madhavan and Kewei Ming (2003) and Anthony Lynch and Richard Mendenhall (1997). Though, after the effective date Lynch and Mendenhall (1997) only noted a partial reversion in prices. Chen, Noronha and Singal (2006) explain that this difference is most likely due to their study using larger samples, as well as tracking the returns for longer after the event. They also suggested that increased awareness was a potential explanation for the permanent increase in returns for additions. They reason that investors do not suddenly become less aware of stocks which are removed from the index, hence the asymmetry in the returns.

Madhavan and Ming (2003) focussed on the July 19 2002 S&P 500 rebalance when seven non-U.S. companies were replaced. They found that by trading in the period leading up to the actual rebalance investors could dramatically reduce their trading costs without exposing their portfolios to substantial tracking error risk.

Madhavan (2002a) found an equivalent effect for the annual rebalances of the Russell 3000 index. He noted that the subsequent return reversals in July suggested that price pressure might have been an important determinant in generating the abnormal returns. He also concluded that the low liquidity of the stocks being removed might explain some of the asymmetry in the returns between the additions and the deletions.

Comparable short-term abnormal returns were also observed for rebalances of the U.K. FTSE-100 by Bryan Mase (2006). Though, he found no equivalent permanent price effects for additions. Instead, he noted that a reversal occurred for both additions and deletions, within a month their returns were back to normal.

In terms of trading volume, Chen, Noronha and Singal (2006) found turnovers to be over three times higher for affected stocks on the S&P 500 announcement days. They also saw turnovers jump to over 12 times normal levels on the effective dates. After the rebalance, the volumes returned to normal for the newly added stocks, but those removed from the index saw a decline in their volumes. In their study of the S&P 500, Lynch and Mendenhall (1997) reported significantly higher volumes on the day before the effective date. Similarly, Mase (2006) found peaks in trading volume on the day before FTSE-100 rebalances. The peaks

applied to both additions and deletions; although post-rebalance there was an appreciable decline in the volumes for the stocks removed from the index.

The impact of index changes have also been analysed for the equity options markets. A study of the S&P 500 by Rong Qi and Libo Sui (2007) tracked the prices and trading volumes for stock options with strikes within 5% of the market price and maturities of 30-117 days. They found that on the day of the announcement call options for the additions saw a considerable price rise whilst the cost of puts fell. For the deletions, the put options saw an even greater price rise, whilst their calls became cheaper. They note that between the announcement and effective dates the highest abnormal return was for put options on the deletions, although the call options on additions also saw a positive return. Again, the price changes seemed to be permanent for the additions, whilst a partial reversal occurred within around 30 days of the effective date for the deletions. Interestingly, they also observed that the option prices started to change up to ten days before the announcement and accelerated at five days before, suggesting that the option market could be a useful leading indicator. Qi and Sui (2007) also reported similar volume spikes. On announcement day, they found up to a 30-times increase for put options on the additions and deletions, up to 50-times for call options on the deletions and around 17-times for call options on the additions. They noted that the open-interest level increased dramatically from announcement to the effective date, then suddenly dropped back to normal levels. Clearly, only so much volume is due to indexfunds, they attributed much of the increase to arbitrageurs.

## Unpredictable events

Events triggered by information or news are much less predictable. Whilst they may be harder to forecast, their short-term effects can still be quantified. For example, trading interruptions, such as halts or volatility auctions, may be followed by periods of much higher volatility and volumes, although these often dissipate after a few hours.

# Trading interruptions

Excessive volatility poses a serious problem for market participants. In an attempt to prevent this, most markets adopt a variety of different methods to try to control things when new information suddenly becomes available, namely:

- Trading halts ۰
- $\bullet$ Price limits
- ٠ Volatility auctions

Trading halts are imposed by the market authorities; they cease trading for a set period whilst new information is made public. Often these are followed by a call auction to provide a more stable reopening for the affected asset. Price limits act as trading ranges, any trades that would shift the price outside of these are simply not permitted. Alternatively, volatility auctions switch continuous trading to a call auction for a short period. Essentially, they are like micro-halts since they often only last for around five minutes; however, they are generally triggered by set price rules, much like a price limit. This is a key difference between these mechanisms since both volatility auctions and price limits may be maintained automatically by market monitoring systems. Their rule-based nature makes them much easier to predict, In fact, a study by David Abad and Roberto Pascual (2006) even determines the probability of hitting such limits. In comparison, trading halts are more subjective and so harder to predict.

Trading halts are commonly adopted in the U.S. equity markets, whereas price limits are

used more in European and Asian stock markets, as well as the U.S. futures markets. Volatility auctions are becoming increasingly popular, especially in Europe. They have also been incorporated into NYSE as Liquidity Replenishment Points (LRPs).

Researchers are still divided over which mechanism is best. Overall, trading halts seem to be preferred over price limits, whilst some studies find volatility auctions more effective than halts. For example, Yong Kim, José Yagüe and J. Jimmy Yang (2008) compared the effect of price limits and halts for trading on the Spanish stock exchange. They concluded that after both interruptions there was increased trading activity. Though, they noted that after trading halts volatility remained the same and the bid-offer spread actually reduced, whereas after price limit hits both the volatility and spread increased.

Note that the main focus of this section is on asset-specific interruptions, since these occur much more frequently than market-wide halts. For instance, in their NYSE study Bidisha Chakrabarty, Shane Corwin and Marios Panayides (2007) analysed 4,020 halts between January 2002 and December 2005, an average of over four a day.

# **Trading halts**

Trading halts may be broken down into two main types, those driven by news and those that arise from order imbalances. Exchange officials instigate news halts when information due to be released is expected to have a significant impact on prices. The halt allows time for this to be disseminated to traders and investors. Order imbalance halts are triggered by a market specialist when the imbalance between buys and sells is too large. During the halt traders may modify, cancel and place new orders, after the halt trading then reopens with a call auction.

NYSE supports both types of halts. In their study, Shane Corwin and Marc Lipson (2000) found the average NYSE halt lasted over 80 minutes. News halts took around 86 minutes whilst order imbalance halts lasted an average of 56 minutes. During this time they noted that order activity increased significantly, both for submissions of new orders and cancellations of existing ones. Hence, by the time the market reopens the order book mainly consists of orders submitted during the halt. Though, due to the uncertainty surrounding halts, they also noted that the depth near the quotes falls to unusually low levels during the halt, even though specialists and floor traders provide additional liquidity. They also observed that order flow could remain at elevated levels for several hours after the halt. Importantly, they found that the market-clearing price after the reopening call auction was a good predictor of future prices. In their sample data, 36% of news halts led to price rises, 43% led to drops and 21% remained unchanged. Whilst for order imbalance halts, 48% led to rises, 41% to drops and 11% were stable. Overall, the average absolute return after a halt was just under 4%.

NASDAQ caters for news-driven halts. William Christie, Shane Corwin, and Jeffrey Harris (2002) found that these led to substantial increases in both volume and volatility. Trading volume and the number of trades were over six times the normal levels for the half hour after the halt, and remained unusually high for up to two hours afterwards. Intraday halts mean market makers cannot start posting prices until five minutes before the resumption of trading. These were found to result in up to nine times the normal levels of volatility, whilst the bid offer spread more than doubled. In comparison, for halts that occur after 4pm there is an extended 90 minute opening the following day. The volatility associated with such openings was significantly lower and the bid offer spread was virtually unaffected. They concluded that there is a clear benefit to allowing more time for price discovery after any halts.

#### **Price limits**

Price limits are generally adopted in order-driven markets. They may be static and/or dynamic. Static thresholds are usually applied to a benchmark price, such as the open or the previous close. So a 10% limit from the open restricts the price range between 36 and 44 for an asset that opened at 40. Dynamic thresholds are more versatile and are often based on the last traded price. For example, a 5% limit on an asset whose last traded price was 100 allows a price range of 95.00-105.00. If the next trade is at 104, the allowed price range will shift to 98.8-109.2.

The rules intervene for any trades that would break these ranges and send the market price either above the high limit or below the low. Such trades may then simply not be permitted, in which case the trader must decide whether to alter their price or not trade, forcing them to re-evaluate the market conditions.

Research on the effectiveness of price limits has not been conclusive. Certainly, there are as many studies that find price limits to be inefficient are there are ones finding them beneficial. A good example is an analysis of the Tokyo Stock Exchange by Kenneth Kim and S. Ghon Rhee (1997). They found that price limits could actually lead to higher volatility and volatility spillover on subsequent days. One of the problems with price limits is that the same price rule is often applied to all the assets within a certain market. This can pose issues for illiquid assets, since these can have significantly wider spreads, which can lead to them triggering the limits more often. This is illustrated in a study of the Chinese stock market by Gong-Meng Chen, Kenneth Kim and Oliver Rui (2005), who conclude that wider limits may be appropriate for the less liquid B-shares.

#### Volatility auctions

Volatility auctions shift continuous trading into a short period call auction, often lasting only about five minutes. This gives traders a brief respite before continuous trading recommences, allowing time for a new price level to be determined. The limits that trigger volatility auctions are usually much less than any daily price limits and so volatility auctions occur more frequently.

These are now in use at NYSE, Euronext and the London Stock Exchange, as well as a variety of other markets. A detailed study of the efficiency of volatility auctions on the Spanish stock exchange is provided by David Abad and Roberto Pascual (2007). They found that volatility started to increase half an hour beforehand, peaking in the ten-minute window around the call auction. In this period volatility levels could shift over six standard deviations away from normal levels. Though, they also noted that volatility rapidly dissipated reaching normal levels again within 90 minutes.

A similar effect was observed for trading volumes, whilst they found that the bid-offer spread was slightly wider for 30 minutes after the auction. However, no marked effect on the displayed order book depth was found. Since the recovery periods were shorter than those observed for NYSE or NASDAQ, they concluded that volatility auctions are an effective means of handling such situations.

#### Corporate announcements

Corporate announcements can be another relatively unpredictable event. Releases of details, such as company earnings or dividend payments, are often scheduled, but firms are free to change the dates. So, both the information they relay and when they occur can be hard to predict.

A study of dividend announcements for NYSE stocks was carried out by John Graham,

Jennifer Koski, and Uri Loewenstein (2003). Overall, they observed a decrease in liquidity immediately beforehand for notices that were well anticipated. As we might expect, the available depth decreased as traders prepared for the announcement. Afterwards, things returned to normal, although how long this took depended on how well the new information was received. For completely unanticipated announcements, the changes in liquidity were less noticeable beforehand. They observed a considerable and sudden increase in the spread that lasted for up to an hour after the news. The time taken for the available depth to recover also seemed to be longer for such events. Interestingly, they also found that unanticipated events were preceded by abnormal trading volumes. The consistency of this pre-event volume suggested some anticipation by informed traders. Though, their study focused on public news, rather than any other sources of market information or rumours.

Whether the announcement is on time can also give away important information. Firms tend to be keen to announce good news and defer issuing bad news. Mark Bagnoli, William Kross and Susan Watts (2004) analysed this effect for U.S. companies. They found that for each day of delay from the expected date of the announcement there was a fall of one penny/share below the consensus forecasts. In addition to these losses, they also noted that the market reaction on the actual day of the announcement depended on how late it had been. Thus, firms that reported late saw even more adverse reactions to bad results than those with similar results who reported on time. In comparison, they found that the market reaction to bc more aggressive for early announcements.

The relatively unstructured format of news can make it very difficult for computer systems to analyse and interpret. In Chapter 14, we will examine methods to overcome these difficulties and analyse the impact of news in much more detail, covering both corporate and macroeconomic news.

# 10.5 Summary

- Trading algorithms and execution tactics are rule-based approaches responding to market conditions. So generally they are reactive. To enhance their performance we can:
  - Incorporate short-term prediction models for conditions such as price and volume.
  - Improve their spotting and handling of specific events, such as witching or halts.
- Short-term forecasting models for key market conditions enable trading strategies to be slightly more proactive and so take advantage of price improvement by placing more passively priced orders than they might otherwise.
  - Price forecasts may only be for the next few minutes, based on:
    - Imbalances in supply and demand.
    - Gaps in the order book, which trigger price jumps.
    - Volume forecasts tend to be for longer periods, based on:
      - Daily historical trading volume profiles. These may be further adjusted to account for seasonal factors or even specific holidays or events.
      - Volumes may also be decomposed into market and asset-specific components.
  - Liquidity measures, such as the bid offer spread or order book depth may be forecast using intraday averages.
  - Volatility forecasts help determine execution probability for orders, using:

- Statistical estimates, based on methods like EMA, ARMA or GARCH.
- Implied volatility, inferred from the market prices of options. \_
- Market volatility, estimated using indices such as the VIX. -
- Transaction cost estimation helps to gauge the balance between cost and risk. Many of these models are based on a framework by Almgren and Chriss (2000):
  - Market impact models adopt a bottom-up approach. -
  - Cost allocation models take a top-down view based on aggregated trade imbalances.
- Identifying specific market events can also enhance performance. For instance:  $\blacksquare$ 
  - New bond issues lead to lower liquidity for the newly "off the run" assets.
  - Expiration of futures, as liquidity rolls from the current contract to the new one. \_
  - Witching days often lead to increases in trading volume and short-term volatility. \_
  - Additions and removals from stock indices lead to increased activity in these stocks.
  - Trading halts and volatility auctions also lead to increases in volatility and volume. \_
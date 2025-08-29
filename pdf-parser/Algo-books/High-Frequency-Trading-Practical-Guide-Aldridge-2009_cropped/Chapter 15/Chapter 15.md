# CHAPTER 15

# **Back-Testing Trading Models**

nce a trading idea is formed, it needs to be tested on historical data. The testing process is known as a back test. This chapter describes the key considerations for a successful and meaningful back test.

The purpose of back tests is twofold. First, a back test validates the performance of the trading model on large volumes of historical data before being used for trading live capital. Second, the back test shows how accurately the strategies capture available profit opportunities and whether the strategies can be incrementally improved to capture higher revenues.

Optimally, the trading idea itself is developed on a small set of historical data. The performance from this sample is known as "in-sample" performance. One month of data can be perfectly sufficient for in-sample estimation, depending on the chosen strategy. To draw any statistically significant inferences about the properties of the trading model at hand, the trading idea should be verified on large amounts of data that was not used in developing the trading model itself. Having a large reserve of historical data (at least two years of continuous tick data) ensures that the model minimizes the data-snooping bias, a condition that occurs when the model overfits to a nonrecurring aberration in the data. Running the back test on a fresh set of historical data is known as making "out-of-sample" inferences

Once the out-of-sample back-test results have been obtained, they must be evaluated. At a minimum, the evaluation process should compute basic statistical parameters of the trading idea's performance: cumulative and average returns, Sharpe ratio, and maximum drawdown, as explained in Chapter 5.

For the purposes of accuracy analyses, trading systems can be grouped into those that generate point forecasts and those that generate directional forecasts. Point forecasts predict that the price of a security will reach a certain level, or point. For example, a system that determines that the S&P 500 index will rise from the current 787 level to 800 within the following week is a point forecast system; the point forecast in this case is the 800 number predicted for the S&P 500. Directional systems make decisions to enter into positions based on expectations of the system going up or down, without specific target forecasts. A directional system may predict that USD/CAD will rise from its current level without making a specific prediction about how far USD/CAD will rise.

## **EVALUATING POINT FORECASTS**

The simplest way to evaluate the validity of point forecasts is to run a regression of realized values from the historical data against the out-ofsample forecasts. For example, suppose that the trading model predicts future price levels of equities. Regressing the realized equity prices on the forecasted ones shows the degree of usefulness of the forecast.

Specifically, the model evaluation regression is specified as follows:

$$Y_t = \alpha + \beta X_t + \varepsilon_t \tag{15.1}$$

where Y is the realized price level, X is the forecasted price level, α and β are parameters estimated by the regression, and ε is a normally distributed error term. Whenever the forecast perfectly predicts the realized values, β = 1 and α = 0. The deviation of the α and β parameters from the optimal β = 1 and α = 0 itself indicates the reliability and usefulness of the forecasting model. In addition, the *R*<sup>2</sup> coefficient obtained from the regression shows the percentage of realized observations explained by the forecasts. The higher the realized *R*2, the greater the accuracy of the forecasting model.

The accuracy of point forecasts can also be evaluated by comparing the forecasts with the realized values. Methods for forecast comparisons include:

- Mean squared error (MSE)
- Mean absolute deviation (MAD)

- Mean absolute percentage error (MAPE)
- Distributional performance
- Cumulative accuracy profiling

If the value of a financial security is forecasted to be  $x_{F,t}$  at some future time t and the realized value of the same security at time t is  $x_{R,t}$ , the forecast error for the given forecast,  $\varepsilon_{F,t}$ , is computed as follows:

$$\varepsilon_{F,t} = x_{F,t} - x_{R,t} \tag{15.2}$$

The mean squared error (MSE) is then computed as the average of squared forecast errors over  $T$  estimation periods, analogously to volatility computation:

$$MSE = \frac{1}{T} \sum_{\tau=1}^{T} \varepsilon_{F,\tau}^{2}$$
 (15.3)

The mean absolute deviation (MAD) and the mean absolute percentage error (MAPE) also summarize properties of forecast errors:

$$\textit{MAD} = \frac{1}{T} \sum_{\tau=1}^{T} |\varepsilon_{F,\tau}| \tag{15.4}$$

$$MAPE = \frac{1}{T} \sum_{\tau=1}^{T} \left| \frac{\varepsilon_{F,\tau}}{x_{R,\tau}} \right| \tag{15.5}$$

Naturally, the lower each of the three metrics (MSE, MAD, and MAPE), the better the forecasting performance of the trading system.

The distributional evaluation of forecast performance also examines forecast errors  $\varepsilon_{F,t}$  normalized by the realized value,  $x_{R,t}$ . Unlike MSE, MAD, and MAPE metrics, however, the distributional performance metric seeks to establish whether the forecast errors are random. If the errors are indeed random, there exists no consistent bias in either direction of price movement, and the distribution of normalized errors  $\left\{\frac{\varepsilon_{F,t}}{x_{F,t}}\right\}$  should fall on the uniform  $[0, 1]$  distribution. If the errors are nonrandom, the forecast can be improved. One test that can be used to determine whether the errors are random is a comparison of errors with the uniform distribution using the Kolmogorov-Smirnov statistic.

The accuracy of models can be further considered in asymmetric situations. For example, does the MSE of negative forecast errors exceed the MSE of positive errors? If so, the model tends to err by underestimating the subsequently realized value and needs to be fine-tuned to address the asymmetric nature of forecast accuracy. Similarly, the accuracy of forecast errors can be examined when the errors are grouped based on various market factors:

- Market volatility at the time the errors were measured
- Magnitude of the errors
- Utilization rate of computer power in generating the forecasts, among other possible factors

The objective of the exercise is to identify the conditions under which the system persistently errs and to fix the error-generating issue.

# EVALUATING DIRECTIONAL FORECASTS

Testing the accuracy of directional systems presents a greater challenge. Yet, accuracy evaluation of the directional systems can be similar to that of the point forecast systems, with binary values of  $1$  and  $0$  indicating whether the direction of the forecast matches the direction of the realized market movement or not. As with the forecasts themselves, directional accuracy estimates are much less accurate than the accuracy estimates of the point forecasts.

Aldridge  $(2009a)$  proposes the trading strategy accuracy (TSA) method to measure the ability of a trading strategy to exploit the gain that opportunities present to the strategy in the market. As such, the method evaluates not only the market value of trading opportunities realized by the system but the market value of trading opportunities that the system missed. The methodology of the test is based on that of the cumulative accuracy profile, also known as Gini curve or power curve. To the author's best knowledge, the cumulative accuracy profile has not been applied to the field of trading strategy evaluation to date.

The TSA methodology evaluates trading strategies in back-testing that is, in observing the strategy run on historical data. The methodology comprises the following three steps:

- 1. Determination of model-driven trade signals in the historical data
- 2. Ex-ante identification of successful and unsuccessful trades in the historical data
- 3. Computation of the marginal probabilities of the trade signals obtained in Step 2 predicting trading outcomes obtained in Step  $1$

| Date          | Time       | Buy a Unit<br>of Security? | Sell a Unit<br>of Security? |  |
|---------------|------------|----------------------------|-----------------------------|--|
| March 9, 2009 | 6:00 A.M.  | 1                          | 0                           |  |
| March 9, 2009 | 7:00 A.M.  | 0                          | 0                           |  |
| March 9, 2009 | 8:00 A.M.  | 1                          | 0                           |  |
| March 9, 2009 | 9:00 A.M.  | 0                          | 0                           |  |
| March 9, 2009 | 10:00 A.M. | 0                          | 0                           |  |
| March 9, 2009 | 11:00 A.M. | 0                          | 1                           |  |
| March 9, 2009 | 12:00 P.M. | 0                          | 0                           |  |
| March 9, 2009 | 1:00 P.M.  | 0                          | 0                           |  |

#### **TABLE 15.1** Model-Generated Trading Behavior

#### **Determination of Model-Driven Trade Signals**

This step is similar to a standard back test for a trading strategy on a single security. The trading model is run on data of the selected frequency. The buy and sell trading signals that the model generates are recorded in Table 15.1, where 1 corresponds to a decision to execute a trade and 0 denotes the absence of such a decision.

## **Ex-Ante Identification of Successful and Unsuccessful Trades in the Historical Data**

This step involves dividing all trading opportunities in the historical data into profitable and unprofitable buys and sells. At each trade evaluation time, the evaluation process looks ahead in the historical data of a given security to determine whether a buy or a sell entered into for the security at that point in time is a success—that is, a profitable trade.

The frequency of the buy or sell decision times corresponds to the frequency of the portfolio-rebalancing decisions in the trading strategy being evaluated. Some strategies are designed to make portfolio rebalancing decisions at the end of each day; other higher-frequency strategies make decisions on whether to place a buy or a sell on the given security following each quote tick. The ex-ante identification of successful and unsuccessful trades proceeds in tandem with the frequency of the trading strategy studied.

The trade's profitability is determined based on the position closing rules—the stop-gain and stop-loss parameters—decided on in advance. The stop-gain parameter determines at what realized gain the system should close the position. The stop-loss parameter determines the maximum allowable loss for each position and triggers liquidation of the position whenever the trading strategy hits the stop-loss threshold. For example, a stop gain of 40 pips (0.004) and a stop loss of 20 pips for a long position in EUR/USD exchange rate entered at 1.2950 would result in closing the position should EUR/USD either reach 1.2990 or trip 1.2930. Identifying the trades with the desired characteristics entails separating potential trades into those that encounter the stop gain prior to encountering the stop loss—the successful ones—and those that encounter a stop loss prior to encountering stop gain.

In evaluating the trading opportunities based on regular time intervals (e.g., one hour), care should be taken to ensure that the stop losses are recorded whenever they are triggered, which can happen at times other than when the closing prices are posted for the period. One way to approach this issue is to evaluate the stop losses with the period lows for long positions, and with the period highs for short positions. Thus, a position in EUR/USD that opened with a buy at 1.2950 should be considered stop-lossed whenever a low during any hour drops to 1.2930 or below.

The output of this step is shown in Table 15.2, where 1 indicates a trade that hit the stop gain prior to tripping the stop loss.

Out of eight hours of profitability assessment in the example shown in Table 15.2, three were entry points for profitable buy-initiated trades, and one was an entry point for profitable sell-initiated trade for given levels of stop-gain and stop-loss parameters. Based on these eight hours of assessment, profitable buy trades existed 3/8 or 37.5 percent of time, and profitable sell trades existed 1/8 or 12.5 percent of time.

Eight trades are hardly enough of a sample for meaningful characterization of trade opportunities, as the sample may not converge to a statistically significant description of potential trade population. Just as with back

| Date          | Time       | Profitable<br>Buy Trade? | Profitable<br>Sell Trade? |  |
|---------------|------------|--------------------------|---------------------------|--|
|               |            |                          |                           |  |
| March 9, 2009 | 6:00 A.M.  | 1                        | 0                         |  |
| March 9, 2009 | 7:00 A.M.  | 1                        | 0                         |  |
| March 9, 2009 | 8:00 A.M.  | 0                        | 0                         |  |
| March 9, 2009 | 9:00 A.M.  | 0                        | 0                         |  |
| March 9, 2009 | 10:00 A.M. | 1                        | 0                         |  |
| March 9, 2009 | 11:00 A.M. | 0                        | 1                         |  |
| March 9, 2009 | 12:00 P.M. | 0                        | 0                         |  |
| March 9, 2009 | 1:00 P.M.  | 0                        | 0                         |  |

#### **TABLE 15.2** Trade Profitability Characterization

tests, it is desirable to produce analysis on data of the desired frequency spanning two years or more.

Figures 15.1–15.4 show the results of the potential profitability analysis of EUR/USD on the hourly data sample ranging from January 2001 through December 2008. Figures 15.1 and 15.2 show probabilities of successful buy and sell trades in hourly EUR/USD data with values of stop-gain and stoploss parameters ranging from 25 to 300 pips (0.0025 to 0.03) in 25-pip intervals. Figures 15.3 and 15.4 show the surface of the average gain per trade for hourly EUR/USD buy and sell decisions for various stop-gain and stoploss values.

As Figures 15.1 and 15.2 show, the higher the absolute value of the stop-loss parameter relative to the stop-gain, the higher the probability of hitting a successful trade. However, high probabilities of a gain do not necessarily turn into high average gain values per trade, as Figures 15.3 and 15.4 illustrate. Over the 2001–2008 sample period, long EUR/USD trades with high stop-gain and stop-loss parameters achieved higher average gains than short EUR/USD trades, the observation being due to the underlying appreciation of EUR/USD over the period.

![](_page_6_Figure_4.jpeg)

**FIGURE 15.1** Probability of successful buy-initiated trades in hourly EUR/USD data for different levels of stop-gain and stop-loss parameters.

![](_page_7_Figure_1.jpeg)

**FIGURE 15.2** Probability of successful sell-initiated trades in hourly EUR/USD data for different levels of stop-gain and stop-loss parameters.

![](_page_7_Figure_3.jpeg)

**FIGURE 15.3** Average gain per buy-initiated trade in hourly EUR/USD data for different levels of stop-gain and stop-loss parameters.

![](_page_8_Figure_1.jpeg)

**FIGURE 15.4** Average gain per sell-initiated trade in hourly EUR/USD data for different levels of stop-gain and stop-loss parameters.

## **Computation of Marginal Probabilities**

The next step involves matching the results of Steps 1 and 2 in the preceding list to determine the percentage of trade signals that resulted in positive gains as well as the percentage of positive gains that remained undetected by the system. In its most basic approach, this task can be accomplished as follows:

- **1.** Compute the "hit ratio," the percentage of trade signals that resulted in the positive gain. To compute the hit ratio, sum up the number of buy trades with positive outcomes determined in Step 2, the times of which corresponded to the times of buy trades determined by the model presented in Step 1 in the preceding list. Divide the matched number of buy trades with positive outcomes by the total number of buy trades generated by the model in Step 1. Repeat the process for sell trades.
- **2.** Compute the "miss ratio," the percentage of positive outcomes determined in Step 2 that were *not* matched by trades in Step 1.

Although the hit and miss ratio statistics alone are indicative of the relative capabilities of the trading model to exploit market conditions, a graphical representation of trading strategy accuracy generates even stronger and more intuitive comparative insights.

### **Accuracy Curves**

Accuracy curves, also known as Lorenz, Power, or Gini curves, provide a way to graphically compare the accuracy of probabilistic forecasts of trade signals. An accuracy curve plots probabilistic hit rates of different forecasting models versus the ideal (100 percent accurate) forecast.

The trading strategy accuracy (TSA) curves plot the cumulative distribution of the "hits" of the trading models versus the "miss" signals. A "hit" is an outcome whereby the trade signal that generated the outcome is a profitable trade. For example, if following a buy signal on EUR/USD, the currency pair appreciates, allowing us to capture a predetermined gain, the forecast was a "hit." A "miss" outcome is the opposite situation; it is a trade signal that led to a loss. The determination of whether the forecast was a hit or a miss is carried out after the trade has been completed and the trade profitability is fully observable.

Figure 15.5 shows sample accuracy curves. The thick black line extending from (0, 0), first vertically and then horizontally to (100, 100), is the plot of the ideal forecast—that is, the forecast that would ex-ante identify all the hits as hits and all the misses as misses.

The line bisecting the chart at the 45-degree angle corresponds to a completely random forecast—a forecast that is equally likely to be a hit

![](_page_9_Figure_7.jpeg)

**FIGURE 15.5** Trade model evaluation using trading strategy accuracy (TSA) curves.

and a miss. All the other models are then evaluated by locations of their TSA curves relative to the ideal and random forecasts. Model A, for example, is worse than the random forecast. Model B is better than the random forecast, and model C is even better (closer to the ideal) than model B.

A TSA curve is a plot of the cumulative distribution of correctly forecasted losses followed by one of correctly forecasted wins. An ideal model will have a 100 percent hit ratio in all of its forecasts; all the gains will be ex-ante forecasted as gains, and all the losses will be ex-ante forecasted as losses. The model with the TSA curve closest to the ideal curve is the best model. A TSA curve is generated as follows:

- **1.** Gather information on all trade outcomes and their ex-ante forecasts. A winning trade can be identified as a "1," while a losing trade can be identified as a "0." Similarly, a hit ex-ante forecast that predicted a win and resulted in a win can be identified as a "1," and so can an ex-ante hit predicting a loss and resulting in a loss. An ex-ante miss of either the forecasted win resulting in a loss or a forecasted loss resulting in a win can be identified as "0." Table 15.3 shows the resulting data structure for several sample trades.
- **2.** Calculate the total number of hits, *H*, and misses, *M*, among all trade outcomes. In our example, there were two hits and three misses. Next, define *N* as the maximum of the two numbers: *N* = max(*H*, *M*). In our example, *N* = 3.
- **3.** Compute cumulative hit and miss rates for each trade. The cumulative hit rate for the *i*th trade, *Hi* is determined as follows:

$$H_i = \begin{cases} H_{i-1} + 1/N & \text{if } \text{if } \text{if } \text{at} \text{ is a hit} \\ H_{i-1} & \text{otherwise} \end{cases}$$
  
$$M_i = \begin{cases} M_{i-1} + 1/N & \text{if } \text{if } \text{at} \text{ is a miss} \\ M_{i-1} & \text{otherwise} \end{cases}$$

| Trade<br>ID | Date     | Forecast/<br>Trade Open<br>Time | Ex-Ante<br>Forecast | Trade<br>Realization | Gain<br>(Loss)<br>MM | Trade<br>Outcome | Hit or<br>Miss |
|-------------|----------|---------------------------------|---------------------|----------------------|----------------------|------------------|----------------|
| 1           | 3/9/2009 | 6:00 A.M. ET                    | Win                 | Win                  | 59                   | 1                | 1              |
| 2           | 3/9/2009 | 7:00 A.M. ET                    | Loss                | Win                  | 70                   | 1                | 0              |
| 3           | 3/9/2009 | 8:00 A.M. ET                    | Win                 | Loss                 | (25)                 | 0                | 0              |
| 4           | 3/9/2009 | 9:00 A.M. ET                    | Loss                | Loss                 | (66)                 | 0                | 1              |
| 5           | 3/9/2009 | 10:00 A.M. ET                   | Loss                | Win                  | 30                   | 1                | 0              |

#### **TABLE 15.3** Assessing Trade Outcomes and Forecast Hits and Misses

| Trade ID | Trade<br>Outcome | Hit or Miss | Cumulative<br>Hit Rate | Cumulative<br>Miss Rate |
|----------|------------------|-------------|------------------------|-------------------------|
| 1        | 1                | 1           | 33.3 percent           | 0 percent               |
| 2        | 1                | 0           | 33.3 percent           | 33.3 percent            |
| 3        | 0                | 0           | 33.3 percent           | 66.7 percent            |
| 4        | 0                | 1           | 66.7 percent           | 66.7 percent            |
| 5        | 1                | 0           | 66.7 percent           | 100 percent             |

| TABLE 15.4 | Cumulative Hit and Miss Rates |  |  |
|------------|-------------------------------|--|--|
|------------|-------------------------------|--|--|

Table 15.4 shows the cumulative hit and miss trades for our example. Trade characteristics have been omitted to save space.

**4.** We are now ready to plot our sample TSA curve. On the chart, the cumulative miss rate for each trade is plotted on the vertical axis, and the cumulative hit rate is plotted on the vertical axis. Starting at the lower-left corner, at point (0, 0), we now draw the line through the points characterizing the hit and miss rate pairs in our example and then continue the line to the upper-right corner (100 percent, 100 percent) point. Figure 15.6 illustrates the outcome.

The accuracy of the forecast is determined as the total area under the TSA curve. For our example, the area under the curve (shaded region) amounts to 44.4 percent of the total area of the box, indicating a

![](_page_11_Figure_6.jpeg)

**FIGURE 15.6** Trading strategy accuracy (TSA) curve for the foregoing sample trades.

44.4 percent accuracy of our forecasts. Our sample forecasting model performs worse than the random forecasting model, the diagonal. The random forecasting model has an accuracy of 50 percent. Note that in small samples like our example, the accuracy of the estimation will depend on the order of hits and misses within the sample. Depending on the order of hits and misses, the accuracy will vary around its true value.

The TSA curve described here is of the simplest kind; it illustrates the hit ratios without any consideration for the actual profitability of winning versus losing trades. A more advanced version of the TSA curve remedies the situation by splitting all gains into two or more buckets of profitability and splitting all losses into comparable buckets of loss values.

In addition to comparisons of accuracy among different trading models, analyzing potential outcomes of trading systems helps to strengthen and calibrate existing models as well as to evaluate the performance of a combination of different models with mutually exclusive signals. Aldridge (2009a) develops a quantitative methodology of applying hit and miss ratio analyses to enhance the accuracy of predictions of trading models.

# **CONCLUSION**

Various back-test procedures illuminate different aspects of strategy performance on historical data and are performed before the trading strategy is applied to live capital. Observing parameters of strategy performance in back tests allows high-frequency managers to identify the best strategies to include in their portfolio. The same parameters allow modelers to tweak their strategies to obtain even more robust models. Care should be taken to avoid "overfitting"—using the same data sample in repeated testing of the model.
# CHAPTER 7

**Market Inefficiency** and Profit **Opportunities at** Different Frequencies

 $\bullet$  he key feature that unites all types of high-frequency trading strategies is persistence of the underlying tradable phenomena. This part of the book addresses the ways to identify these persistent trading opportunities.

High-frequency trading opportunities range from microsecond price moves allowing a trader to benefit from market-making trades, to severalminute-long strategies that trade on momentum forecasted by microstructure theories, to several-hour-long market moves surrounding recurring events and deviations from statistical relationships. Dacorogna et al. (2001) emphasize a standard academic approach to model development:

- 1. Document observed phenomena.
- 2. Develop a model that explains the phenomena.
- 3. Test the model's predictive properties.

The development of high-frequency trading strategies begins with identification of recurrent profitable trading opportunities present in highfrequency data. The discourse on what is the most profitable trading frequency often ends once the question of data availability emerges and researchers cannot quantify the returns of strategies run at different frequencies. Traders that possess the data shun the public limelight because they are using the data to successfully run high-frequency strategies. Other sources tend to produce data from questionable strategies.

The profitability of a trading strategy is bound by the chosen trading frequency. At the daily trading frequency, the maximum profit and loss are

limited by the daily range of price movements. At the hourly frequency, the possible range of the price movement shrinks, but the number of hourly ranges in the day increases to 7 in most equities and 24 in foreign exchange. The total potential gain is then the sum of all intra-hour ranges recorded during the day. At even higher frequencies, the ranges of price movements tighten further, and the number of ranges increases to provide even higher profitability.

Table 7.1 shows the maximum gain potential and other high-frequency range statistics for SPY (S&P 500 Depository Receipts ETF) and EUR/USD at different frequencies recorded for April 21, 2009. The maximum gain is calculated as the sum of price ranges at each frequency. The maximum gains of SPY and EUR/USD are then normalized by the daily open prices of SPY and EUR/USD, respectively, to show the relative gain in percentages. The maximum gain potential at every frequency is determined by the sum of all per-period ranges at that frequency.

The gain potential in the high-frequency space is nothing short of remarkable, as is the maximum potential loss, which is equal to the negative maximum gain. Careful strategy design, extensive back testing, risk management, and implementation are needed to realize the high-frequency gain potential.

The profitability of a trading strategy is often measured by Sharpe ratios, a risk-adjusted return metric first proposed by Sharpe (1966). As Table 7.2 shows, maximum Sharpe ratios increase with increases in trading frequencies. From March 11, 2009, through March 22, 2009, the maximum possible annualized Sharpe ratio for EUR/USD trading strategies with daily position rebalancing was 37.3, while EUR/USD trading strategies that held positions for 10 seconds could potentially score Sharpe ratios well over the 5,000 mark.

The maximum possible intra-day Sharpe ratio is computed as a sample period's average range divided by the sample period's standard deviation of the range, adjusted by square root of the number of observations in a year:

$$SR = \frac{E[\text{Range}]}{\sigma[\text{Range}]} \times \sqrt{\text{(\# Intra-day Periods)} \times \text{(\# Trading Days in a Year)}}$$
(7.1)

Note that high-frequency strategies normally do not carry overnight positions and, therefore, do not incur the overnight carry cost often proxied by the risk-free rate in Sharpe ratios of longer-term investments.

In practice, well-designed and -implemented strategies trading at the highest frequencies tend to produce the highest profitability with the double-digit Sharpe ratios. Real-life Sharpe ratios for well-executed strategies with daily rebalancing typically fall in the 1–2 range.

| mu<br>Maxi<br>TABLE 7.1                                                      | m Gain Potential and Other Range Statistics for SPY and EUR/USD at Di |                     |                    | fferent Frequencies on April | 21, 2009          |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------|---------------------|--------------------|------------------------------|-------------------|
| SPY                                                                          |                                                                       |                     |                    |                              |                   |
|                                                                              |                                                                       |                     | Period Duration    |                              |                   |
| Statistic                                                                    | 0 sec<br>1                                                            | 1 min               | 0 min<br>1         | 1 hour                       | 1 day             |
| m of<br>m Gain Potential per Day (Su<br>All per-Period Ranges)<br>mu<br>Maxi | 96.33 percent                                                         | 44.59 percent       | 13.96 percent      | 5.66 percent                 | 1.09 percent      |
| mber of Intra-Day Periods<br>Average Range per Period<br>Nu                  | 0.04 percent<br>2340                                                  | 0.11 percent<br>390 | 0.35 percent<br>39 | 0.81 percent<br>7            | 1.09 percent<br>1 |
| EUR/USD                                                                      |                                                                       |                     |                    |                              |                   |
|                                                                              |                                                                       |                     | Period Duration    |                              |                   |
| Statistic                                                                    | 0 sec<br>1                                                            | min<br>1            | min<br>0<br>1      | 1 hour                       | 1 day             |
| m of<br>m Gain Potential per Day (Su<br>All per-Period Ranges)<br>mu<br>Maxi | 9.23 percent<br>31                                                    | 90.07 percent       | 8.48 percent<br>1  | 6.44 percent                 | 0.57 percent      |
| Average Range per Period                                                     | 0.04 percent                                                          | 0.06 percent        | 0.13 percent       | 0.27 percent                 | 0.57 percent      |
| mber of Intra-Day Periods<br>Nu                                              | 8640                                                                  | 440<br>1            | 44<br>1            | 24                           | 1                 |

| TABLE 7.2  | Comparison of Maximum Sharpe Ratios Achievable by an Ideal<br>Strategy with Perfect Predictability of Intra-Period Price Movement in<br>EUR/USD. (The results are computed ex-post with 20/20 hindsight<br>on the data for 30 trading days from February 9, 2009 through<br>March 22, 2009.) |                                              |                                                      |                                       |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------|---------------------------------------|
|            | Average<br>Maximum Gain<br>(Range) per<br>Period                                                                                                                                                                                                                                             | Range<br>Standard<br>Deviation<br>per Period | Number of<br>Observations<br>in the Sample<br>Period | Maximum<br>Annualized<br>Sharpe Ratio |
| 10 seconds | 0.04 percent                                                                                                                                                                                                                                                                                 | 0.01 percent                                 | 2,592,000                                            | 5879.8                                |
| 1 minute   | 0.06 percent                                                                                                                                                                                                                                                                                 | 0.02 percent                                 | 43,200                                               | 1860.1                                |
| 10 minutes | 0.12 percent                                                                                                                                                                                                                                                                                 | 0.09 percent                                 | 4,320                                                | 246.4                                 |
| 1 hour     | 0.30 percent                                                                                                                                                                                                                                                                                 | 0.19 percent                                 | 720                                                  | 122.13                                |

1 day 1.79 percent 0.76 percent 30 37.3

## **PREDICTABILITY OF PRICE MOVES AT HIGH FREQUENCIES**

## **Predictability and Market Efficiency**

Every trader and trading system aims to generate trading signals that result in consistently positive outcomes over a large number of trades. In seeking such signals, both human traders and econometricians designing systematic trading platforms are looking to uncover sources of predictability of future price movements in selected securities. Predictability, both in trading and statistics, is the opposite of randomness. It is, therefore, the objective of every trading system to find ways to distinguish between predictable and random price moves and then to act on the predictable ones.

While the future is never certain, history can offer us some clues about how the future may look given certain recurring events. All successful trading systems, therefore, are first tested on large amounts of past historical data. Technical analysts, for example, pore over historical price charts to obtain insights into past price behaviors. Fundamental analysts often run multiple regressions to determine how one fundamental factor influences another. High-frequency trading system developers run their models through years of tick data to ascertain the validity of their trading signals.

A more scientific method for analyzing a particular financial security may lie in determining whether price changes of the security are random or not. If the price changes are indeed random, the probability of detecting a consistently profitable trading opportunity for that particular security is small. On the other hand, if the price changes are nonrandom, the financial security has persistent predictability, and should be analyzed further.

![](_page_4_Figure_1.jpeg)

**FIGURE 7.1** Incorporation of information in efficient and inefficient markets.

The relative availability of trading opportunities can be measured as a degree of market inefficiency. An efficient market (Fama, 1970) should instantaneously reflect all the available information in prices of the traded securities. If the information is impounded into the securities slowly, then arbitrage opportunities exist, and the market is considered to be inefficient. Figure 7.1 illustrates the idea of efficient versus inefficient markets. To identify markets with arbitrage opportunities is to find inefficient markets. The arbitrage opportunities themselves are market inefficiencies.

In Figure 7.1, panel (a) shows efficient and inefficient market responses to "good" information that pushes the price of the security higher, while panel (b) shows efficient and inefficient market responses to "bad" information that lowers the price of the security. The price of the security in the efficient market adjusts to the new level instantaneously at the time the news comes out. The price of the security in the inefficient market begins adjusting before the news becomes public ("information leakage"), and usually temporarily overreacts ("overshoots") once the news becomes public. Many solid trading strategies exploit both the information leakage and the overshooting to generate consistent profits.

## **Testing for Market Efficiency and Predictability**

The more inefficient the market, the more predictable trading opportunities become available. Tests for market efficiency help discover the extent of predictable trading opportunities. This chapter considers several tests for market efficiency designed to help the researchers to select the most profitable markets. The chapter by no means considers all the market efficiency tests that have been proposed in the academic literature; rather, it summarizes key tests with varying degrees of complexity, from the simplest to the most advanced.

The market efficiency hypothesis has several "levels": weak, semistrong, and strong forms of market efficiency. Tests for the weak form of market efficiency measure whether returns can be predicted by their past prices and returns alone. Other forms of market efficiency restrict the kinds of information that can be considered in forecasting prices. The strong form deals with all kinds of public and nonpublic information; the semistrong form excludes nonpublic information from the information set. As in most contemporary academic literature on market efficiency, we restrict the tests to the weak form analysis only.

**Non-Parametric Runs Test** Several tests of market efficiency have been developed over the years. The very first test, constructed by Louis Bachelier in 1900, measured the probability of a number of consecutively positive or consecutively negative price changes, or "runs." As with tossing a fair coin, the probability of two successive price changes of the same sign (a positive change followed by a positive change, for example) is 1/(22) = 0.25. The probability of three successive price changes of the same sign is 1/(23) = 0.125. Four successive price changes of the same sign are even less likely, having the probability of 1/(24) = 0.0625 or 6.25 percent. Several price changes of the same sign in a row present a trading opportunity at whichever frequency one chooses to consider, the only requirement being the ability to overcome the transaction costs accompanying the trade.

The test works as follows:

**1.** Within a sample containing price moves of the desired frequency, note the number of sequences consisting strictly of price moves of the same sign. If the desired frequency is every tick, then a run can be a sequence of strictly positive or strictly negative price increments from one tick to the next. If the desired frequency is one minute, a run can be a sequence of strictly positive or strictly negative price increments measured at 1-minute intervals. Table 7.3 shows 1-minute changes in the AUD/USD exchange rate that occurred from 16:00 GMT to 16:20 GMT on June 8, 2009.

The 1-minute changes are calculated as follows: if the closing price for AUD/USD recorded for a given minute is higher than that for the previous minute, the change for the given minute is recorded to be positive. If the closing price for AUD/USD recorded for a given minute is lower than that for the previous minute, the change for the given minute is recorded to be negative. As shown in Table 7.3, from 16:00 GMT to 16:20 GMT, there were in total nine minutes with positive change in AUD/USD, eight minutes with negative change in AUD/USD, and three minutes with 0 change in AUD/USD. Altogether, there were six positive runs whereby the price of AUD/USD increased, and four negative runs where the price of AUD/USD decreased. Positive runs are marked "P" in the "Runs" column, and negative runs are marked "N." Thus, minutes marked "P2" correspond to the second run of sequential positive changes, and minutes marked "N1" correspond to the first run of negative changes.

- **2.** Denote the total number of runs, both positive and negative, observed in the sample as *u*. Furthermore, denote as *n*<sup>1</sup> the number of positive 1-minute changes in the sample, and as *n*<sup>2</sup> the number of negative 1-minute changes in the sample. In the sample shown in Table 7.3, *u* = 10, *n*<sup>1</sup> = 9, and *n*<sup>2</sup> = 8.
- **3.** If price changes were completely random, it can be shown that the expected number of runs in a random sample is ¯*x* = <sup>2</sup>*n*1*n*<sup>2</sup> *<sup>n</sup>*<sup>1</sup> <sup>+</sup> *<sup>n</sup>*<sup>2</sup> + 1, with the standard deviation of runs being

$$s = \sqrt{\frac{2n_1n_2(2n_1n_2 - n_1 - n_2)}{(n_1 + n_2)^2(n_1 + n_2 - 1)}}.$$

In the example of Table 7.3, ¯*x* = 9.47, and *s* = 1.99.

| DATE     | TIME  | Close  | 1-Minute<br>Change | Sign of the<br>Change | Runs |
|----------|-------|--------|--------------------|-----------------------|------|
| 6/8/2009 | 16:00 | 0.7851 |                    |                       |      |
| 6/8/2009 | 16:01 | 0.7853 | 0.0002             | +                     | P1   |
| 6/8/2009 | 16:02 | 0.7848 | −0.0005            | −                     | N1   |
| 6/8/2009 | 16:03 | 0.7841 | −0.0007            | −                     | N1   |
| 6/8/2009 | 16:04 | 0.784  | −1E-04             | −                     | N1   |
| 6/8/2009 | 16:05 | 0.7842 | 0.0002             | +                     | P2   |
| 6/8/2009 | 16:06 | 0.7844 | 0.0002             | +                     | P2   |
| 6/8/2009 | 16:07 | 0.7845 | 1E-04              | +                     | P2   |
| 6/8/2009 | 16:08 | 0.7845 | 0                  |                       |      |
| 6/8/2009 | 16:09 | 0.7847 | 0.0002             | +                     | P3   |
| 6/8/2009 | 16:10 | 0.7849 | 0.0002             | +                     | P3   |
| 6/8/2009 | 16:11 | 0.7846 | −0.0003            | −                     | N2   |
| 6/8/2009 | 16:12 | 0.7845 | −1E-04             | −                     | N2   |
| 6/8/2009 | 16:13 | 0.7839 | −0.0006            | −                     | N2   |
| 6/8/2009 | 16:14 | 0.7841 | 0.0002             | +                     | P4   |
| 6/8/2009 | 16:15 | 0.7841 | 0                  |                       |      |
| 6/8/2009 | 16:16 | 0.7837 | −0.0004            | −                     | N3   |
| 6/8/2009 | 16:17 | 0.7842 | 0.0005             | +                     | P5   |
| 6/8/2009 | 16:18 | 0.784  | −0.0002            | −                     | N4   |
| 6/8/2009 | 16:19 | 0.784  | 0                  |                       |      |
| 6/8/2009 | 16:20 | 0.7842 | 0.0002             | +                     | P6   |

**TABLE 7.3** One-Minute Closing Price Data on AUD/USD Recorded on June 8, 2009, from 16:00 to 16:20 GMT

4. Next, we test whether the realized number of runs indicates statistical nonrandomness. The runs at the selected frequency are deemed predictable, or nonrandom, with 95 percent statistical confidence if the number of runs is at least 1.654 standard deviations  $s$  away from the mean  $\bar{x}$ . The number of runs is not random if the two-tailed test based on Z-score is rejected. The Z-score is computed as  $Z = \frac{|u - \bar{x}| - 0.5}{s}$ . In other words, the randomness of runs is rejected with 95 percent statistical confidence whenever  $Z$  is greater than 1.645. The randomness of runs cannot be rejected if  $Z < 1.645$ .

In the example of Table 7.3,  $Z = 0.0147$ ; therefore, randomness of 1minute changes in the sample cannot be rejected.

Table 7.4 summarizes runs test  $Z$ -scores obtained for several securities on data of different frequency for all data of June  $8, 2009$ . As Table  $7.4$ shows, the runs test rejects randomness of price changes at 1-minute frequencies, except for prices on S&P 500 Depository Receipts (SPY). The results imply strong market inefficiency in 1-minute data for the securities shown. Market inefficiency measured by runs test decreases or disappears entirely at a frequency lower than 10 minutes.

**Tests of Random Walks** Other, more advanced tests for market efficiency have been developed over the years. These tests help traders evaluate the state of the markets and reallocate trading capital to the markets with the most inefficiencies—that is, the most opportunities for reaping profits.

When price changes are random, they are said to follow a "random walk." Formally, a random walk process is specified as follows:

$$\ln P_t = \ln P_{t-1} + \varepsilon_t \tag{7.2}$$

where  $\ln P_t$  is the logarithm of the price of the financial security of interest at time t, ln  $P_{t-1}$  is the logarithm of the price of the security one time

|         | TOUR CONTINUES I COLUMBIC TO BACK OUT TALLOND DECALLED ALLO<br>Frequencies Recorded on June 8, 2009. |     |       |     |         |             |
|---------|------------------------------------------------------------------------------------------------------|-----|-------|-----|---------|-------------|
| Ticker  | Data Frequency                                                                                       | N1  | $N_2$ | u   | z       | Result      |
| SPY     | 1 minute                                                                                             | 179 | 183   | 193 | 1.11    | Random      |
| SPY     | $10 \text{ minutes}$                                                                                 | 21  | 17    | 20  | $-0.10$ | Random      |
| Т       | 1 minute                                                                                             | 142 | 138   | 187 | 5.45    | Predictable |
| т       | $10 \text{ minutes}$                                                                                 | 18  | 17    | 20  | 0.35    | Random      |
| USD/JPY | 1 minute                                                                                             | 558 | 581   | 775 | 12.11   | Predictable |
| USD/JPY | $10 \text{ minutes}$                                                                                 | 68  | 64    | 82  | 2.55    | Predictable |
| XAU/USD | 1 minute                                                                                             | 685 | 631   | 778 | 6.61    | Predictable |
| XAU/USD | $10 \text{ minutes}$                                                                                 | 75  | 66    | 76  | 0.73    | Random      |

TARLE 7.4 Non-Parametric Runs Test Applied to Data on Various Securities and

interval removed at a predefined frequency (minute, hour, etc.), and  $\varepsilon_t$  is the error term with mean 0. From equation (7.2), log price changes  $\Delta \ln P_t$ are obtained as follows:

$$\Delta \ln P_t = \ln P_t - \ln P_{t-1} = \varepsilon_t$$

At any given time, the change in log price is equally likely to be positive and negative. The logarithmic price specification ensures that the model does not allow prices to become negative (logarithm of a negative number does not exist).

The random walk process can drift, and be specified as shown in equa- $\text{tion } (7.3)$ :

$$\ln P_t = \mu + \ln P_{t-1} + \varepsilon_t \tag{7.3}$$

In this case, the average change in prices equals the drift rather than  $0$ , since  $\Delta \ln P_t = \ln P_t - \ln P_{t-1} = \mu + \varepsilon_t$ . The drift can be due to a variety of factors; persistent inflation, for example, would uniformly lower the value of the U.S. dollar, inflicting a small positive drift on prices of all U.S. equities. At very high frequencies, however, drifts are seldom noticeable.

Lo and MacKinlay (1988) developed a popular test for whether or not a given price follows a random walk. The test can be applied to processes with or without drift. The test procedure is built around the following principle: if price changes measured at a given frequency (e.g., one hour) are random, then price changes measured at a lower frequency (e.g., two hours) should also be random. Furthermore, the variances of the 1-hour and 2-hour changes should be deterministically related. Note that the reverse does not apply; randomness in 1-hour price changes does not imply randomness in 10-minute price changes, nor does it imply a relationship in variances between the 1-hour and 10-minute samples.

The test itself is based on the following estimators:

$$\hat{\mu} = \frac{1}{2n} \sum_{k=1}^{2n} \left( \ln P_k - \ln P_{k-1} \right) = \frac{1}{2n} (\ln P_{2n} - \ln P_0) \tag{7.4}$$

$$\hat{\sigma}_a^2 = \frac{1}{2n} \sum_{k=1}^{2n} \left( \ln P_k - \ln P_{k-1} - \hat{\mu} \right)^2 \tag{7.5}$$

$$\hat{\sigma}_b^2 = \frac{1}{2n} \sum_{k=1}^n \left( \ln P_{2k} - \ln P_{2k-2} - 2\hat{\mu} \right)^2 \tag{7.6}$$

If the error term  $\varepsilon_t$  in equations (7.2) or (7.3) is a sequence of independent, identically normally distributed numbers with mean 0 and variance  $\sigma_0^2$ ,  $\varepsilon_t \sim i.i.d.N(0, \sigma_0^2)$ , then Lo and MacKinlay (1988) show that the differences in parameters  $\sigma_0^2$ ,  $\hat{\sigma}_a^2$  (7.5), and  $\hat{\sigma}_b^2$  (7.6) are asymptotically distributed as follows:

$$\sqrt{2n}(\hat{\sigma}_a^2 - \sigma_0^2) \stackrel{a}{\sim} N(0, 2\sigma_0^4)$$
(7.7)

$$\sqrt{2n}(\hat{\sigma}_b^2 - \sigma_0^2) \stackrel{a}{\sim} N(0, 4\sigma_0^4) \tag{7.8}$$

The test for market efficiency is then performed as specified by equation  $(7.9)$ :

$$J_r \equiv \frac{\hat{\sigma}_b^2}{\hat{\sigma}_a^2} - 1, \ \sqrt{2n} J_r \stackrel{a}{\sim} N(0, 2) \tag{7.9}$$

Lo and MacKinlay (1988) subsequently use the test on daily, weekly, and monthly equity data and conclude that while market efficiency cannot be rejected for weekly and monthly frequency, daily equity prices are not efficient.

Table 7.5 summarizes the results of the variance ratio test applied to several foreign exchange instruments across different frequencies. The rows represent the estimated values for the variance ratio test  $J_r$ , as defined by equation  $(7.9)$ . The parentheses show the value of the test statistic measuring the deviation of  $J_r$  from 0. If the time series follows a random walk, then the test statistic  $J_r$  will have a normal distribution.

When applied to daily data of the S&P 500 index, the variance ratio test produced mean  $J_r$  of 0.7360 with the corresponding test statistic of 13.84, significant at 0.001 percent. As Table 7.5 shows, each of the six major USD crosses are more efficient than the  $S\&P$  500: deviations of the variance ratio test statistic,  $J_r$ , from 0 are less statistically significant for major USD crosses and their derivatives than they are for S&P 500, even at high frequencies. The relative inefficiency of S&P  $500$  signifies that S&P  $500$  has more arbitrage opportunities than do the six USD currencies.

According to Table 7.5, daily spot in USD/CAD is the most efficient currency pair with the fewest number of arbitrage opportunities among the six major USD-crosses. USD/CAD together with USD/JPY are the most efficient USD-based pairs in put options written on JPY/USD and CAD/USD futures with the nearest expiration date.

As Table 7.5 shows, the efficiency of spot instruments decreases—that is, the number of arbitrage opportunities increases—with increases in data sampling frequency. For example, the inefficiency of EUR/USD daily spot rate is higher when EUR/USD is measured at 1-hour intervals than when it is measured at daily intervals, as evidenced by a higher t-statistic accompanying the daily and hourly estimates.

| TABLE 7.5     | level of significance. The esti<br>The variance ratios<br>mber 2008.<br>Dece | with asterisks indicate that the corresponding variance ratios are statistically di<br>value of Jr is 0 and the test statistics have a standard nor<br>statistics z*(q) given in parentheses i<br>Jr | defined by equation (7.9) are reported in the ro<br>mediately belo<br>mation was conducted<br>m | on data spanning the two-<br>w each ro<br>mal | w. Under the rando<br>distribution (asy<br>ws, | mptotically). Test statistics marked<br>with the heteroscedasticity-robust test<br>m 0 at the 5 percent<br>m walk null hypothesis, the<br>month period of Nove<br>fferent fro | and<br>mber         |
|---------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Currency Pair | Daily Spot                                                                   | min Spot<br>5-                                                                                                                                                                                       | min Spot<br>15-                                                                                 | 1-Hr Spot                                     | Futures<br>1-Hr                                | 1-Hr Call<br>Options                                                                                                                                                          | 1-Hr Put<br>Options |
| AUD/USD       | 0.6354                                                                       | 0.7320                                                                                                                                                                                               | 0<br>0.731                                                                                      | 0.7128                                        | 76<br>0.71                                     | 0.6851                                                                                                                                                                        | 0.6937              |
|               | (2.27)*                                                                      | (8.74)*                                                                                                                                                                                              | (9.21)*                                                                                         | (4.90)*                                       | (5.48)*                                        | (3.72)*                                                                                                                                                                       | (3.75)*             |
| USD/CAD       | 0.5672                                                                       | 0.7301                                                                                                                                                                                               | 0.7278                                                                                          | 0.7124                                        | 81<br>0.71                                     | 9<br>0.691                                                                                                                                                                    | 4<br>0.661          |
|               | (1.89)                                                                       | (7.97)*                                                                                                                                                                                              | (8.61)*                                                                                         | (4.90)*                                       | (5.48)*                                        | (3.87)*                                                                                                                                                                       | (2.98)*             |
| USD/CHF       | 0.6356                                                                       | 0.7325                                                                                                                                                                                               | 0.7315                                                                                          | 0.7123                                        | 0.6952                                         | 0.6796                                                                                                                                                                        | 0.6850              |
|               | (2.27)*                                                                      | (8.85)*                                                                                                                                                                                              | (9.77)*                                                                                         | (5.00)*                                       | 4)*<br>(4.1                                    | (3.57)*                                                                                                                                                                       | (3.80)*             |
| EUR/USD       | 0.6355                                                                       | 0.7359                                                                                                                                                                                               | 0.7337                                                                                          | 0.7135                                        | 89<br>0.71                                     | 0.6912                                                                                                                                                                        | 0.6836              |
|               | (2.27)*                                                                      | (15.07)*                                                                                                                                                                                             | 0.08)*<br>(1                                                                                    | (5.00)*                                       | (5.57)*                                        | (3.87)*                                                                                                                                                                       | (3.77)*             |
| GBP/USD       | 0.6658                                                                       | 0.7346                                                                                                                                                                                               | 0.7263                                                                                          | 0.7068                                        | 0.6927                                         | 0.6962                                                                                                                                                                        | 0.6871              |
|               | (2.27)*                                                                      | (11.00)*                                                                                                                                                                                             | (7.01)*                                                                                         | (4.84)*                                       | (3.72)*                                        | (3.88)*                                                                                                                                                                       | (3.81)*             |
| USD/JPY       | 0.6353                                                                       | 0.7386                                                                                                                                                                                               | 0.7322                                                                                          | 0.7129                                        | 0.7123                                         | 0.6580                                                                                                                                                                        | 0.6384              |
|               | (2.27)*                                                                      | 7.37)*<br>(1                                                                                                                                                                                         | (9.83)*                                                                                         | (5.00)*                                       | (5.36)*                                        | (2.88)*                                                                                                                                                                       | (2.61)*             |

As Table 7.5 further shows, spot foreign exchange rates at daily frequencies have the fewest number of persistent trading opportunities. Surprisingly, 1-hr put and call options have fewer trading opportunities than do spot and futures at the same frequency. Higher frequency markets, however, show more persistent profit pockets, further strengthening the case for already popular high-frequency trading styles.

As documented in Table 7.5, even in foreign exchange, value opportunities exist at high frequencies. Extracting that value requires much ingenuity, speed, and precision and can be a time-consuming and expensive process. The tests for market efficiency save traders time and money by enabling the selection of the most profitable financial instruments and frequencies prior to committing to development of trading models.

**Autoregression-Based Tests** Trading strategies perform best in the least efficient markets, where abundant arbitrage opportunities exist. Perfectly efficient markets instantaneously incorporate all available market information, allowing no dependencies from past price movements. One way to measure the relative degree of market efficiency, therefore, is to estimate the explanatory power of past prices. Mech (1993) and Hou and Moskowitz  $(2005)$ , for example, propose to measure market efficiency as the difference between  $Adjusted R^2$  coefficients of an unrestricted model attempting to explain returns with lagged variables and of a restricted model involving no past data.

The unrestricted model is specified as follows:

$$r_{i,t} = \alpha_i + \beta_{i,1}r_{i,t-1} + \beta_{i,2}r_{i,t-2} + \beta_{i,3}r_{i,t-3} + \beta_{i,4}r_{i,t-4} + \varepsilon_{i,t}$$
(7.10)

where  $r_{i,t}$  is the return on security i at time t (see Chapter 8 for a detailed discussion on the computation of returns).

The restricted model restricts all coefficients  $\beta_{i,j}$  to be 0:

$$r_{i,t} = \alpha_i + \varepsilon_{i,t} \tag{7.11}$$

Market inefficiency is next calculated as the relative difference between Ordinary Least Squares (OLS)  $R^2$  coefficients of the two models:

$$Market\ Inefficiency = 1 - \frac{R_{\text{Restricted}}^2}{R_{\text{Unrestricted}}^2} \tag{7.12}$$

The closer the difference is to  $0$ , the smaller the influence of past price movements and the higher the market efficiency.

#### Market Efficiency Tests Based on the Martingale Hypothesis $A$

classic definition of market efficiency in terms of security returns is due to

Samuelson (1965), who showed that properly anticipated prices fluctuate randomly in an efficient market. In other words, if all of the news is incorporated instantaneously into the price of a given financial security, the expected price of the security given current information is always the current price of the security itself. This relationship is known as a martingale. Formally, a stochastic price process {*Pt*} is a martingale within information set *It* if the best forecast of *Pt*+<sup>1</sup> based on current information *It* is equal to *Pt*:

$$E[P_{t+1}|I_t] = P_t \tag{7.13}$$

Applying the martingale hypothesis to changes in price levels, we can express "abnormal," or returns in excess of expected returns given current information, as follows:

$$Z_{t+1} = \Delta P_{t+1} - E[\Delta P_{t+1}|I_t] \tag{7.14}$$

A market in a particular financial security or a portfolio of financial securities is then said to be efficient when abnormal return *Zt*+<sup>1</sup> is a "fair game"—that is,

$$E[Z_{t+1}|I_t] = 0 \t\t(7.15)$$

LeRoy (1989) provides an extensive summary of the literature on the subject.

A financial securities market characterized by fair game returns is efficient as it lacks consistent profit opportunities. As Fama (1991) pointed out, in a market with trading costs, equation (7.15) will hold within trading cost deviations.

Fama (1991) also suggested that the efficient markets hypothesis is difficult to test for the following reason: the idea of a market fully reflecting all available information contains a joint hypothesis. On the one hand, expected values of returns are a function of information. On the other hand, differences of realized returns from their expected values are random. Incorporating both issues in the same test is difficult. Nevertheless, martingale-based tests for market efficiencies exist.

Froot and Thaler (1990), for example, derive a specification for a test of market efficiency of a foreign exchange rate. In equilibrium, foreign exchange markets follow the uncovered interest rate parity hypothesis that formulates the price of a foreign exchange rate as a function of interest rates in countries on either side of the interest rate. Under the uncovered interest rate parity, an expected change in the equilibrium spot foreign exchange rate *S*, given that the information set *It* is a function of the interest rate differential between domestic and foreign interest rates,  $r_t - r_t^d$  and risk premium  $\xi_t$  of the exchange rate:

$$E[\Delta S_{t+1}|I_t] = r_t - r_t^d + \xi_t \tag{7.16}$$

where the risk premium  $\xi_t$  is zero for risk-neutral investors and is diversifiable to zero for others.

In addition, following the martingale hypothesis, realized spot exchange rate at time  $t+1$ ,  $S_{t+1}$  is related to its ex-ante expectation  $E[S_{t+1}|I_t]$ as follows:

$$S_{t+1} = E[S_{t+1}|I_t] + u_{t+1} \tag{7.17}$$

where  $E[u_{t+1}|I_t] = 0$ . Combining equations (7.16) and (7.17) yields the following, information-independent test for market efficiency of a foreign exchange rate:

$$\Delta S_{t+1} = r_t - r_t^d + \varepsilon_{t+1} \tag{7.18}$$

where  $\{\varepsilon_t\}$  series is independent, identically distributed with mean 0.

Taking exponents of both sides of equation  $(7.18)$ , the test can be specified in a forward-rate form as follows:

$$\log S_{t+1} = \log F_t + \upsilon_{t+1} \tag{7.19}$$

where mean of  $\nu_t$  is  $E[\nu_t] = 0$  and variance of  $\nu_t$  is  $\sigma_{\nu}^2$ .

The specification of equation  $(7.19)$  produces a testable hypothesis at low frequencies as forward contracts and their open market counterparts (i.e., futures) typically mature once a quarter. Most low-frequency tests reject predictability of spot rates with forward rates. For example, Hodrick  $(1987)$  notes that none of the pre-1987 tests involving forward rates to forecast spot rates fit the data. Engel (1996) supports Hodrick's (1987) conclusions and further notes that even when the risk premium in the specification of equation  $(7.18)$  is assumed to differ from 0, the risk premium fails to explain the lack of predictability of the forward model. Alexakis and Apergis (1996), however, find that the forward rates indeed accurately predict spot rates when predictability is measured in an ARCH specification (ARCH is discussed in Chapter 8). A high-frequency specification, nonetheless, is easy to derive as a differential between two subsequent realizations of equation  $(7.19)$ :

$$\log\left[\frac{S_{t+1}}{S_t}\right] = \log\left[\frac{F_t}{F_{t-1}}\right] + \Delta \upsilon_{t+1} \tag{7.20}$$

with mean of  $\Delta v_t$  is  $E[\Delta v_t] = 0$  and variance of  $\Delta v_t$  is  $2\sigma_v^2$ .

88

**Cointegration-Based Tests of Market Efficiency** Another test of market efficiency is based on the Engle and Granger (1987) representation theorem that suggests that cointegration between two variables implies systematic predictability. For example, if some market factor *X*, say log forward rate, predicts spot exchange rate *S* according to specification *St* = *b*<sup>0</sup> + *b*1*Xt* + ε*t*, where ε*<sup>t</sup>* is stationary (has a consistent distribution over time) and *E*[ε*t*] = 0, then a cointegration-based test for ascertaining dependency of *S* on *X* has the following specification:

$$\Delta S_t = \alpha (b_0 + b_1 X_{t-1} - S_{t-1}) + \beta \Delta X_{t-1} + \gamma \Delta S_{t-1} + \eta_t \tag{7.21}$$

where η*<sup>t</sup>* is an independent, identically distributed error term with mean 0, α measures the speed of the model's adjustment to its long-term equilibrium, and β and γ measure short-term impact of lagged changes in *X* and *S*.

Evidence of cointegration on daily closing rates of three or more currency pairs has been documented by Goodhart (1988), Hakkio and Rush (1989), Coleman (1990), and Alexander and Johnson (1992), among others.

Literature on the efficient markets hypothesis in foreign exchange further distinguishes between speculative and arbitraging efficiencies. The speculative efficiency hypothesis due to Hansen and Hodrick (1980) proposes that the expected rate of return from speculation in the forward market conditioned on available information is zero. The arbitraging efficiency hypothesis puts forward that the expected return on a portfolio composed of long one unit of currency and short one future contract on that unit of currency is zero. The arbitrage strategy of buying one unit of currency and selling one futures contract is known as uncovered interest arbitrage. The strategy attempts to arbitrage the uncovered interest parity.

## **CONCLUSION**

The tests of market efficiency illuminate different aspects of a security's price and return dependency on other variables. Taking advantage of market inefficiency requires an understanding of the different tests that identified the inefficiency in the first place.

The same security may be predictable at one frequency and fully random at another frequency. Various combinations of securities may have different levels of efficiency. While price changes of two or more securities may be random when securities are considered individually, the price changes of a combination of those securities may be predictable, and vice versa.
# CHAPTER 13 **Statistical** Arbitrage in **High-Frequency** Settings

tatistical arbitrage (stat-arb) exploded on the trading scene in the late 1990s, with PhDs in physics and other "hard" sciences reaping double-digit returns using simple statistical phenomena. Since then, statistical arbitrage has been both hailed and derided. The advanced returns generated before 2007 by many stat-arb shops popularized the technique. Yet some blame stat-arb traders for destabilizing the markets in the  $2007$  and  $2008$  crises. Stat-arb can lead to a boon in competent hands and a bust in semi-proficient applications.

The technique is a modern cousin of a technical analysis strategy utilizing "Bollinger Bands" that was used to indicate maximum highs and lows at any given point in time by plotting a two-standard deviation envelope around the simple moving average of the price. Despite the recent explosive popularity of stat-arb strategies, many misconceptions about the technique are prevalent. This chapter examines the stat-arb technique in detail.

At its core, stat-arb rests squarely on data mining. To begin with, statarb analysts sift through volumes of historical data with the objective of identifying a pervasive statistical relationship. Such a relationship may be between the current price level of the security and the price level of the same security in the recent past. The relationship may also be between price levels of two different securities, or the price level of one security and the volatility of another. The critical point in the identification process is that the relationship has to hold with at least 90 percent statistical confidence, 90 percent being the lowest acceptable confidence threshold in most statistical analyses.

Once a statistically significant relationship is detected, a stat-arb trading model is built around the following assumption: if at any point in time the statistical relationship is violated, the relationship will mean-revert to its natural historical level and the trade should be placed in the meanreverting direction. The tendency to mean-revert is assumed to increase whenever the relationship is violated to a large extent.

The degree of violation of the historical relationship can be measured by the number of standard deviations the relationship has moved away from the historical mean of values characterizing the relationship. For example, if the variable of interest is price and the price level of USD/CAD rises by two or more standard deviations above its average historical price difference with the level of USD/CHF in a short period of time, the statarb strategy assumes that the unusually large move of USD/CAD is likely to reverse in the near future, and the trading strategy enters into a short position in USD/CAD. If the mean-reversion indeed materializes, the strategy captures a gain. Otherwise, a stop loss is triggered, and the strategy books a loss.

## **MATHEMATICAL FOUNDATIONS**

Mathematically, the steps involved in the development of stat-arb trading signals are based on a relationship between price levels or other variables characterizing any two securities. A relationship based on price levels *Si*,*<sup>t</sup>* and *Sj*,*<sup>t</sup>* for any two securities *i* and *j* can be can be arrived at through the following procedure:

- **1.** Identify the universe of liquid securities—that is, securities that trade at least once within the desired trading frequency unit. For example, for hourly trading frequency choose securities that trade at least once every hour.
- **2.** Measure the difference between prices of every two securities, *i* and *j*, identified in step (1) across time *t*:

$$\Delta S_{ij,t} = S_{i,t} - S_{j,t}, \ t \in [1, T]$$
(13.1)

where *T* is a sufficiently large number of daily observations. According to the central limit theorem (CLT) of statistics, 30 observations at selected trading frequency constitute the bare minimum. The intra-day data, however, has high seasonality—that is, persistent relationships can be observed at specific hours of the day. Thus, a larger *T* of at least 30 daily observations is strongly recommended. For robust inferences, a *T* of 500 daily observations (two years) is desirable.

**3.** For each pair of securities, select the ones with the most stable relationship—security pairs that move together. To do this, Gatev, Goetzmann, and Rouwenhorst (2006) perform a simple minimization of the historical differences in returns between every two liquid securities:

$$\min_{i,j} \sum_{t=1}^{T} (\Delta S_{ij,t})^2 \tag{13.2}$$

The stability of the relationship can also be assessed using cointegration and other statistical techniques.

Next, for each security *i*, select the security *j* with the minimum sum of squares obtained in equation (13.2).

**4.** Estimate basic distributional properties of the difference as follows. Mean or average of the difference:

$$E[\Delta S_t] = \frac{1}{T} \sum_{t=1}^T \Delta S_t$$

Standard deviation:

$$\sigma[\Delta S_t] = \frac{1}{T-1} \sum_{t=1}^T \left(\Delta S_t - E[\Delta S_t]\right)^2$$

**5.** Monitor and act upon differences in security prices: At a particular time τ , if

$$\Delta S_{\tau} = S_{i,\tau} - S_{j,\tau} > E[\Delta S_{\tau}] + 2\sigma[\Delta S_{\tau}]$$

sell security *i* and buy security *j*. On the other hand, if

$$\Delta S_{\tau} = S_{i,\tau} - S_{j,\tau} < E[\Delta S_{\tau}] - 2\sigma[\Delta S_{\tau}]$$

buy security *i* and sell security *j*.

**6.** Once the gap in security prices reverses to achieve a desirable gain, close out the positions. If the prices move against the predicted direction, activate stop loss.

Instead of detecting statistical anomalies in price levels, statistical arbitrage can be applied to other variables, such as correlation between two securities and traditional fundamental relationships. The details of implementation of statistical arbitrage based on fundamental factors are discussed in detail in the following text.

Stat-arb strategies can be trained to dynamically adjust to changing market conditions. The mean of the variable under consideration, to which the identified statistical relationships are assumed to tend, can be computed as a moving weighted average with the latest observations being given more weight than the earliest observations in the computation window. Similarly, the standard deviation used in computations can be computed using a limited number of the most recent observations, reflecting the latest economic environment.

The shortcomings of statistical arbitrage strategies are easy to see; often enough, detected statistical relationships are random or "spurious" and have little predictive staying power. Yet other statistical relationships, those validated by academic research in economics and finance, have consistently produced positive results for many traders. Thorough understanding of economic theory helps quantitative analysts distinguish between solid and arbitrary relationships and, in turn, improves the profitability of trading operations that use stat-arb methodology.

In addition to the issues embedded in the estimation of statistical relationships, statistical arbitrage strategies are influenced by numerous adverse market conditions.

- The strategies face a positive probability of bankruptcy of the parties issuing one or both of the selected financial instruments. Tough market conditions, an unexpected change in regulation, or terrorist events can destroy credible public companies overnight.
- Transaction costs may wipe out all the profitability of stat-arb trading, particularly for investors deploying high leverage or limited capital.
- The bid-ask spread may be wide enough to cancel any gains obtained from the strategy.
- Finally, the pair's performance may be determined by the sizes of the chosen stocks along with other market frictions—for example, price jumps in response to earnings announcements.

Careful measurement and management of risks, however, can deliver high stat-arb profitability. Gatev, Goetzmann, and Rouwenhorst (2006) document that the out-of-sample back tests conducted on the daily equity data from 1967 to 1997 using their stat-arb strategy delivered Sharpe ratios well in excess of 4. High-frequency stat-arb delivers even higher performance numbers.

## **PRACTICAL APPLICATIONS OF STATISTICAL ARBITRAGE**

#### **General Considerations**

Most common statistical arbitrage strategies relying solely on statistical relationships with no economic background produce fair results, but these relationships often prove to be random or spurious. A classic example of a spurious relationship is the relationship between time as a continuous variable and the return of a particular stock; all publicly listed firms are expected to grow with time, and while the relationship produces a highly significant statistical dependency, it can hardly be used to make meaningful predictions about future values of equities. Another extreme example of a potentially spurious statistical relationship is shown by Challe (2003), who documents statistical significance between the occurrence of sunspots and the predictability of asset returns.

High-frequency statistical arbitrage based on economic models has ex-ante longer staying power, because it is based on solid economic principles. The stat-arb strategies arbitraging deviations in economic equations can be called fundamental arbitrage models in that they exploit deviations from fundamental economic principles.

The prices of the pair of securities traded often will be related in some fashion or other, but they can nevertheless span a variety of asset classes and individual names. In equities, the companies issuing securities may belong to the same industry and will therefore respond similarly to changes in the broad market. Alternatively, the securities may actually be issued by the same company. Companies often issue more than one class of shares, and the shares typically differ by voting rights. Even shares of the same class issued by the same company but trading on different exchanges may have profitable intra-day deviations in prices. In foreign exchange, the pair of securities chosen can be a foreign exchange rate and a derivative (e.g., a futures contract) on the same foreign exchange rate. The same underlying derivative trading strategy may well apply to equities and fixed-income securities. Passive indexes, such as infrequently rebalanced ETFs, can be part of profitable trades when the index and its constituents exhibit temporary price deviations from equilibrium. In options, the pair of securities may be two options on the same underlying asset but with different times to expiration.

This section discusses numerous examples of statistical arbitrage applied to various securities. Table 13.1 itemizes the strategies discussed subsequently. The selected strategies are intended to illustrate the ideas of fundamental arbitrage. The list is by no means exhaustive, and many additional fundamental arbitrage opportunities can be found.

#### **Foreign Exchange**

Foreign exchange has a number of classic models that have been shown to work in the short term. This section summarizes statistical arbitrage applied to triangular arbitrage and uncovered interest rate parity models. Other fundamental foreign exchange models, such as the flexible price

| Asset Class                      | Fundamental Arbitrage Strategy              |  |  |  |
|----------------------------------|---------------------------------------------|--|--|--|
| Foreign Exchange                 | Triangular Arbitrage                        |  |  |  |
| Foreign Exchange                 | Uncovered Interest Parity (UIP) Arbitrage   |  |  |  |
| Equities                         | Different Equity Classes of the Same Issuer |  |  |  |
| Equities                         | Market Neutral Arbitrage                    |  |  |  |
| Equities                         | Liquidity Arbitrage                         |  |  |  |
| Equities                         | Large-to-Small Information Spillovers       |  |  |  |
| Futures and the Underlying Asset | Basis Trading                               |  |  |  |
| Indexes and ETFs                 | Index Composition Arbitrage                 |  |  |  |
| Options                          | Volatility Curve Arbitrage                  |  |  |  |

**TABLE 13.1** Summary of Fundamental Arbitrage Strategies by Asset Class Presented in This Section

monetary model, the sticky price monetary model, and the portfolio model can be used to generate consistently profitable trades in the statistical arbitrage framework.

**Triangular Arbitrage** Triangular arbitrage exploits temporary deviations from fair prices in three foreign exchange crosses. The following example illustrates triangular arbitrage of EUR/CAD, following a triangular arbitrage example described by Dacorogna et al. (2001). The strategy arbitrages mispricings between the market prices on EUR/CAD and "synthetic" prices on EUR/CAD that are computed as follows:

$$\begin{array}{l} \text{EUR}/\text{CAD}_{\text{Synthetic, bid}} = \text{EUR}/\text{USD}_{\text{Market, bid}} \times \text{USD}/\text{CAD}_{\text{Market, bid}} \\\\ \text{EUR}/\text{CAD}_{\text{Synthetic, ask}} = \text{EUR}/\text{USD}_{\text{Market, ask}} \times \text{USD}/\text{CAD}_{\text{Market, ask}} \end{array} \tag{13.4}$$

If market ask for EUR/CAD is lower than synthetic bid for EUR/CAD, the strategy is to buy market EUR/CAD, sell synthetic EUR/CAD, and wait for the market and synthetic prices to align, then reverse the position, capturing the profit. The difference between the market ask and the synthetic bid should be high enough to at least overcome two spreads—on EUR/USD and on USD/CAD. The USD-rate prices used to compute the synthetic rate should be sampled simultaneously. Even a delay as small as one second in price measurement can significantly distort the relationship as a result of unobserved trades that affect the prices in the background; by the time the dealer receives the order, the prices may have adjusted to their noarbitrage equilibrium levels.

**Uncovered Interest Parity Arbitrage** The uncovered interest parity (UIP) is just one such relation. Chaboud and Wright (2005) find that the UIP best predicts changes in foreign exchange rates at high frequencies and daily rates when the computation is run between 4 P.M. ET and 9 P.M. ET. The UIP is specified as follows:

$$1 + i_t = (1 + i_t^*) \frac{E_t \left[ S_{t+1} \right]}{S_t}$$
(13.5)

where  $i_t$  is the one-period interest rate on the domestic currency deposits,  $i_t^*$  is the one-period interest rate on deposits denominated in a foreign currency, and  $S_t$  is the spot foreign exchange price of one unit of foreign currency in units of domestic currency. Thus, for example, if domestic means United States-based and foreign means Swiss, the UIP equation, equation  $(13.5)$ , can be used to calculate the equilibrium CHF/USD rate as follows:

$$1 + i_{t, USD} = (1 + i_{t, CHF}^*) \frac{E_t \left[ S_{t+1, CHF/USD} \right]}{S_{t, CHF/USD}}$$
(13.6)

The expression can be conveniently transformed to the following regression form suitable for linear estimation:

$$\ln(S_{t+1,CHF/USD}) - \ln(S_{t,CHF/USD}) = \alpha + \beta(\ln(1 + i_{t,USD})$$
$$- \ln(1 + i_{t,CHF}^*)) + \varepsilon_{t+1} \tag{13.7}$$

A statistical arbitrage of this relationship would look into the statistical deviations of the two sides of equation  $(13.7)$  and make trading decisions accordingly.

#### **Equities**

Examples of successful statistical arbitrage strategies involving fundamental equities models abound. This section reviews the following popular trading pair trading strategies: different equity classes of the same issuer, market-neutral pairs trading, liquidity arbitrage, and large-to-small information spillovers.

Arbitraging Different Equity Classes of the Same Issuer It is reasonable to expect stocks corresponding to two common equity classes issued by the same company to be trading within a relatively constant price range from each other. Different classes of common equity issued by the same company typically diverge in the following two characteristics only: voting rights and number of shares outstanding.

Shares with superior voting rights are usually worth more than the shares with inferior voting rights or non-voting shares, given that shares with wider voting privileges allow the shareholders to exercise a degree of control over the direction of the company—see Horner (1988) and Smith and Amoako-Adu (1995), for example. Nenova (2003) shows that the stock price premium for voting privileges exists in most countries. The premium varies substantially from country to country and depends on the legal environment, the degree of investor protection, and takeover regulations, among other factors. In countries with the greatest transparency, such as Finland, the voting premium is worth close to 0, whereas in South Korea, the voting premium can be worth close to 50 percent of the voting stock's market value.

Stocks with a higher number of shares outstanding are usually more liquid, prompting actively trading investors to value them more highly; see Amihud and Mendelson (1986, 1989); Amihud (2002); Brennan and Subrahmanyam (1996); Brennan, Chordia and Subrahmanyam (1998); and Eleswarapu (1997). At the same time, the more liquid class of shares is likely to incorporate market information significantly faster than the less liquid share class, creating the potential for information arbitrage.

A typical trade may work as follows: if the price range widens to more than two standard deviations of the average daily range without a sufficiently good reason, it may be a fair bet that the range will narrow within the following few hours.

The dual-class share strategy suffers from two main shortcomings and may not work for funds with substantial assets under management (AUM).

- **1.** The number of public companies that have dual share classes trading in the open markets is severely limited, restricting the applicability of the strategy. In January 2009, for example, Yahoo! Finance carried historical data for two equity classes for just eight companies trading on the NYSE: Blockbuster, Inc.; Chipotle; Forest City Entertainment; Greif, Inc.; John Wiley & Sons; K V Pharma; Lennar Corp.; and Moog, Inc.
- **2.** The daily volume for the less liquid share class is often small, further restricting the capacity of the strategy. Table 13.2 shows the closing price and daily volume for dual-class shares registered on the NYSE on January 6, 2009. For all names, Class B daily volume on January 6, 2009 does not reach even one million in shares and is too small to sustain a trading strategy of any reasonable trading size.

**Market-Neutral Arbitrage** Market arbitrage refers to a class of trading models that are based on classical equilibrium finance literature. At core, most market arbitrage models are built on the capital asset pricing

| Company Name      | Ticker<br>Class A | Class A<br>Close | Class A<br>Volume<br>(MM<br>Shares) | Ticker<br>Class B | Class B<br>Close | Class B<br>Volume<br>(MM<br>Shares) |
|-------------------|-------------------|------------------|-------------------------------------|-------------------|------------------|-------------------------------------|
| Blockbuster, Inc. | BBI               | 1.59             | 2.947                               | BBI-B             | 0.88             | 0.423                               |
| Chipotle          | CMG               | 60.38            | 0.659                               | CMG-B             | 55.87            | 0.156                               |
| Forest City       | FCE-A             | 8.49             | 1.573                               | FCE-B             | 8.41             | 0.008                               |
| Entertainment     |                   |                  |                                     |                   |                  |                                     |
| Greif, Inc.       | GEF               | 35.42            | 0.378                               | GEF-B             | 35.15            | 0.016                               |
| John Wiley & Sons | JW-A              | 36.82            | 0.237                               | JW-B              | 36.63            | 0.005                               |
| K V Pharma        | KV-A              | 3.68             | 0.973                               | KV-B              | 3.78             | 0.007                               |
| Lennar Corp.      | LEN               | 11.17            | 8.743                               | LEN-B             | 8.5              | 0.074                               |
| Moog, Inc.        | MOG-A             | 37.52            | 0.242                               | MOG-B             | 37.9             | 0.000                               |

**TABLE 13.2** Closing Price and Daily Volume of Dual-Class Shares on NYSE on January 6, 2009

model (CAPM) developed by Sharpe (1964), Lintner (1965), and Black (1972).

The CAPM is based on the idea that returns on all securities are influenced by the broad market returns. The degree of the co-movement that a particular security may experience with the market is different for each individual security and can vary through time. For example, stocks of luxury companies have been shown to produce positive returns whenever the broad market produces positive returns as well, whereas breweries and movie companies tend to produce higher positive returns whenever the overall market returns are downward sloping.

The CAPM equation is specified as follows:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{M,t} - r_{f,t}) + \varepsilon_t \tag{13.8}$$

where *ri*,*<sup>t</sup>* is the return on security *i* at time *t*, *rM*,*<sup>t</sup>* is the return on a broad market index achieved in time period *t*, and *r <sup>f</sup>*,*<sup>t</sup>* is the risk-free interest rate, such as Fed Funds rate, valid in time period *t*. The equation can be estimated using Ordinary Least Squares (OLS) regression. The resulting parameter estimates, ˆα and βˆ, measure the abnormal return that is intrinsic to the security ( ˆα) and the security's co-movement with the market (βˆ).

The simplest example of CAPM-based pair arbitrage in equities is trading pairs with the same response to the changes in the broader market conditions, or beta, but different intrinsic returns, or alpha. This type of strategy is often referred to as a market-neutral strategy, with the idea that going long and short, respectively, in two securities with similar beta would neutralize the resulting portfolio from broad market exposure.

Often, the two securities used belong to the same or a similar industry, although this is not mandatory. The alpha and beta for two securities i and j are determined from the CAPM equation (13.8). Once the point estimates for alphas and betas of the two securities are produced, along with standard deviations of those point estimates, the statistical significance of difference in alphas and betas is then determined using the difference in the means test, described here for betas only:

$$\Delta \hat{\beta} = \hat{\beta}_i - \hat{\beta}_j \tag{13.9}$$

$$\hat{\sigma}_{\Delta\beta} = \sqrt{\frac{\sigma_{\beta i}^2}{n_i} + \frac{\sigma_{\beta j}^2}{n_j}} \tag{13.10}$$

where  $n_i$  and  $n_j$  are the numbers of observations used in the estimation of equation (13.8) for security  $i$  and security  $j$ , respectively.

The standard *t*-ratio statistic is then determined as follows:

$$\text{Student}_{\beta} = \frac{\Delta \hat{\beta}}{\hat{\sigma}_{\Delta\beta}} \tag{13.11}$$

The difference test for alphas follows the same procedure as the one outlined for betas in equations  $(13.9)$ – $(13.11)$ .

As with other *t*-test estimations, betas can be deemed to be statistically similar if the  $t$  statistic falls within one standard deviation interval:

$$t_{\beta} \in [\Delta \hat{\beta} - \hat{\sigma}_{\Delta \beta}, \Delta \hat{\beta} + \hat{\sigma}_{\Delta \beta}] \tag{13.12}$$

At the same time, the difference in alphas has to be both economically and statistically significant. The difference in alphas has to exceed trading costs,  $TC$ , and the *t*-ratio has to indicate a solid statistical significance, with 95 percent typically considered the minimum:

$$\Delta \hat{\alpha} > TC \tag{13.13}$$

$$|t_{\alpha}| > [\Delta \hat{\alpha} + 2\hat{\sigma}_{\Delta\alpha}] \tag{13.14}$$

Once a pair of securities satisfying equations  $(13.12)$ – $(13.14)$  is identified, the trader goes long in the security with the higher alpha and shorts the security with the lower alpha. The position is held for the predetermined horizon used in the forecast.

Variations on the basic market-neutral pair trading strategy include strategies accounting for other security-specific factors, such as equity fundamentals. For example, Fama and French (1993) show that the following three-factor model can be successfully used in equity pair trading:

$$r_{i,t} = \alpha_i + \beta_i^{MKT} MKT_t + \beta_i^{SMB} SMB_t + \beta_i^{HML} HML_t + \varepsilon_t \tag{13.15}$$

where  $r_{i,t}$  is the return on stock i at time t,  $MKT_t$  is the time-t return on a broad market index,  $SMB_t$  (small minus big) is the time-t difference in returns between market indices or portfolios of small and big capitalization stocks, and  $HML_t$  (high minus low) is the return on a portfolio constructed by going long in stocks with comparatively high book-to-market ratios and going short in stocks with comparatively low book-to-market ratios.

**Liquidity Arbitrage** In classical asset pricing literature, a financial security that offers some inconvenience to the prospective investors should offer higher returns to compensate investors for the inconvenience. Limited liquidity is one such inconvenience; lower liquidity levels make it more difficult for individual investors to unwind their positions, potentially leading to costly outcomes. On the flipside, if liquidity is indeed priced in asset returns, then periods of limited liquidity may offer nimble investors highly profitable trading opportunities.

In fact, several studies have documented that less liquid stocks have higher average returns: see Amihud and Mendelson (1986); Brennan and Subrahmanyam (1996); Brennan, Chordia, and Subrahmanyam (1998); and Datar, Naik, and Radcliffe (1998). Trading the illiquid stocks based exclusively on the information that they are illiquid, however, delivers no positive abnormal returns. The relatively high average returns simply compensate prospective investors for the risks involved in holding these less liquid securities.

Pástor and Stambaugh  $(2003)$ , however, recognize that at least a portion of the observed illiquidity of financial securities may be attributed to market-wide causes. If the market-wide liquidity is priced into individual asset returns, then market illiquidity arbitrage strategies may well deliver consistent positive abnormal returns on the risk-adjusted basis.

Pástor and Stambaugh  $(2003)$  find that in equities, stocks whose returns have higher exposure to variability in the market-wide liquidity indeed deliver higher returns than stocks that are insulated from the marketwide liquidity. To measure sensitivity of stock  $i$  to market liquidity, Pástor and Stambaugh (2003) devise a metric  $\gamma$  that is estimated in the following  $OLS$  specification:

$$r_{i,t+1}^{e} = \theta + \beta r_{i,t} + \gamma \ sign(r_{i,t}^{e}) \cdot v_{i,t} + \tau_{t+1}$$
(13.16)

where  $r_{i,t}$  is the return on stock i at time t,  $v_{i,t}$  is the dollar volume for stock *i* at time *t*, and  $r_{i,t}^e$  is the return on stock *i* at time *t* in excess of the market return at time  $t$ :  $r_{i,t}^e = r_{i,t} - r_{m,t}$ . The sign of the excess return  $r_{i,t}^e$ proxies for the direction of the order flow at time  $t$ ; when stock returns are positive, it is reasonable to assume that the number of buy orders in the market outweighs the number of sell orders, and vice versa. The prior time-period return  $r_{i,t}$  is included to capture the first-order autocorrelation effects shown to be persistent in the return time series of most financial securities.

**Large-to-Small Information Spillovers** Equity shares and other securities with relatively limited market capitalization are considered to be "small." The precise cutoff for "smallness" varies from exchange to exchange. On the NYSE in 2002, for example, "small" stocks were those with market capitalization below \$1 billion; stocks with market capitalization of \$1 billion to \$10 billion were considered to be "medium," and "large" stocks were those with market cap in excess of \$10 billion.

Small stocks are known to react to news significantly more slowly than large stocks. Lo and MacKinlay (1990), for example, found that returns on smaller stocks follow returns on large stocks. One interpretation of this phenomenon is that large stocks are traded more actively and absorb information more efficiently than small stocks. Hvidkjaer  $(2006)$  further documents "an extremely sluggish reaction" of small stocks to past returns of large stocks and attributes this underreaction to the inefficient behavior of small investors.

A proposed reason for the delay in the response of small stocks is their relative unattractiveness to institutional investors who are the primary source of the information that gets impounded into market prices. The small stocks are unattractive to institutional investors because of their size. A typical size of a portfolio of a mid-career institutional manager is \$200 million; if a portfolio manager decides to invest into small stocks, even a well-diversified share of an institutional portfolio will end up moving the market for any small stock significantly, cutting into profitability and raising the liquidity risk of the position. In addition, ownership of 5 percent or more of a particular U.S. stock must be reported to the SEC, further complicating institutional investing in small stocks. As a result, small stocks are traded mostly by small investors, many of whom use daily data and traditional "low-tech" technical analysis to make trading decisions.

The market features of small stocks make the stocks illiquid and highly inefficient, enabling profitable trading. Llorente, Michaely, Saar, and Wang  $(2002)$  studied further informational content of trade volume and found that stocks of smaller firms and stocks with large bid-ask spreads exhibit momentum following high-volume periods. Stocks of large firms and firms with small bid-ask spread, however, exhibit no momentum and sometimes exhibit reversals following high-volume time periods. Profitable trading strategies, therefore, involve trading small stocks based on the results of correlation or cointegration with lagged returns of large stocks as well as the volume of large and small stocks' records during preceding periods.

## **Futures**

Statistical arbitrage can also be applied to pairs consisting of a security and its derivative. The derivative of choice is often a futures contract since futures prices are linear functions of the underlying asset:

$$F_t = S_t \exp[r_t(T-t)]$$

where *Ft* is the price of a futures contract at time *t*, *St* is the price of the underlying asset (e.g., equity share, foreign exchange rate, or interest rate) also at time *t*, *T* is the time the futures contract expires, and *rt* is the interest rate at time *t.* For foreign exchange futures, *rt* is the differential between domestic and foreign interest rates.

**Basis Trading** The statistical arbitrage between a futures contract and the underlying asset is known as "basis trading." As with equity pairs trading, the basis-trading process follows the following steps: estimation of the distribution of the contemporaneous price differences, ongoing monitoring of the price differences, and acting upon those differences.

Lyons (2001) documents results of a basis-trading strategy involving six currency pairs: DEM/USD, USD/JPY, GBP/USD, USD/CHF, FRF/USD, and USD/CAD. The strategy bets that the difference between the spot and futures prices reverts to its mean or median values. The strategy works as follows: sell foreign currency futures whenever the futures price exceeds the spot price by a certain predetermined level or more, and buy foreign currency futures whenever the futures price falls short of the spot price by at least a prespecified difference. Lyons (2001) reports that when the predetermined strategy trigger levels are computed as median basis values, the strategy obtains a Sharpe ratio of 0.4–0.5.

**Futures/Equity Arbitrage** In response to macroeconomic news announcements, futures markets have been shown to adjust more quickly than spot markets. Kawaller, Koch, and Koch (1993), for example, show that prices of the S&P 500 futures react to news faster than prices of the S&P 500 index itself, in the Granger causality specification. A similar effect was documented by Stoll and Whaley (1990): for returns measured in 5-minute intervals, both S&P 500 and money market index futures led stock market returns by 5 to 10 minutes.

The quicker adjustment of the futures markets relative to the equities markets is likely due to the historical development of the futures and equities markets. The Chicago Mercantile Exchange, the central clearinghouse for futures contracts in North America, rolled out a fully functional electronic trading platform during the early 1990s; most equity exchanges still relied on a hybrid clearing mechanism that involved both human traders and machines up to the year 2005. As a result, faster informationarbitraging strategies have been perfected for the futures market, while systematic equity strategies remain underdeveloped to this day. By the time this book was written, the lead-lag effect between futures and spot markets had decreased from the 5- to 10-minute period documented by Stoll and Whaley (1990) to a 1- to 2-second advantage. However, profit-taking opportunities still exist for powerful high-frequency trading systems with low transaction costs.

#### **Indexes and ETFs**

Index arbitrage is driven by the relative mispricings of indexes and their underlying components. Under the Law of One Price, index price should be equal to the price of a portfolio of individual securities composing the index, weighted according to their weights within the index. Occasionally, relative prices of the index and the underlying securities deviate from the Law of One Price and present the following arbitrage opportunities. If the price of the index-mimicking portfolio net of transaction costs exceeds the price of the index itself, also net of transaction costs, sell the index-mimicking portfolio, buy index, hold until the market corrects its index pricing, then realize gain. Similarly, if the price of the index-mimicking portfolio is lower than that of the index itself, sell index, buy portfolio, and close the position when the gains have been realized.

Alexander (1999) shows that cointegration-based index arbitrage strategies deliver consistent positive returns and sets forth a cointegrationbased portfolio management technique step by step:

- **1.** A portfolio manager selects or is assigned a benchmark. For a portfolio manager investing in international equities, for example, the benchmark can be a European, Asian, or Far East (EAFE) Morgan Stanley index and its constituent indexes. Outperforming the EAFE becomes the objective of the portfolio manager.
- **2.** The manager next determines which countries lead EAFE by running the error-correcting model (ECM) with log(EAFE) as a dependent variable and log prices of constituent indexes in local currencies as independent (explanatory) variables:

$$EAFE_t = \alpha + \beta_1 x_{1,t} + \ldots + \beta_n x_{n,t} + \varepsilon_t \tag{13.17}$$

where the statistically significant β<sup>1</sup> ...β<sup>n</sup> coefficients indicate optimal allocations pertaining to their respective country indices *x*<sup>1</sup> ... *x*n, and α represents the expected outperformance of the EAFE benchmark if the residual from the cointegrating regression is stationary. β<sup>1</sup> ...β<sup>n</sup> can be constrained in estimation, depending on investor preferences.

An absolute return strategy can further be obtained by going long in the indexes in proportions identified in step 2 and shorting EAFE.

## **Options**

In options and other derivative instruments with a nonlinear payoff structure, statistical arbitrage usually works between a pair of instruments written on the same underlying asset but having one different characteristic. The different characteristic is most often either the expiration date or the strike price of the derivative. The strategy development proceeds along the steps noted in the previous sections.

# **CONCLUSION**

Statistical arbitrage is powerful in high-frequency settings as it provides a simple set of clearly defined conditions that are easy to implement in a systematic fashion in high-frequency settings. Statistical arbitrage based on solid economic theories is likely to have longer staying power than strategies based purely on statistical phenomena.
# Statistical Arbitrage Strategies

Like human trading, high-frequency trading (HFT) strategies can be broken down into three major categories (per Harris, 1998):

- 1. *Statistical arbitrage or stat-arb, also known as value-motivated strategies.* Stat-arb traders wait for security prices to become cheap relative to their proprietary valuations of security based on fundamental or purely statistical indicators. These traders run models to determine the fair value of each financial instrument. Stat-arb traders might be traditional, low-frequency institutional money managers, as well as high-frequency managers, arbitraging short-term valuation discrepancies. Stat-arb traders may deploy market orders for fast-dissolving price discrepancies as well as limit orders to capture slowly evolving misvaluations (see Kaniel and Liu, 2006; and Angel, 1994).
- 2. *Directional strategies, also known as informed trading.* Directional traders successfully estimate the direction of an impending market move. Directional traders are often high-frequency money managers and other proprietary traders with superior access to information and skill in assessing immediate market situations. Their information can include analyses from paid-for news sources, like Bloomberg, not yet available to the general public; forecasts based on market microstructure; and other sources.

Directional traders' forecasts tend to be time sensitive. Forecasts may be related to an event scheduled to occur at a specific time, after which the forecasts cease to be useful. Information obtained from premium sources may soon be distributed to the public, reducing its potency. As a result, directional traders are impatient and typically execute using market orders or "aggressive" limit orders set at prices close to market (see Vega, 2007). Directional event-based strategies are discussed in Chapter 9.

**131**

 3. *Market-making, also known as liquidity trading.* Market makers have no material market insights and aim to profi t from providing liquidity. When using highfrequency algorithms, liquidity traders deploy automated market-making strategies, discussed in Chapters 10 and 11. Market makers are most likely to use limit orders, although selected situations may call for market orders as well.

Figure 8.1 illustrates distributions of order aggressiveness and trader types relative to the market price in the limit order book.

Statistical arbitrage (stat-arb) exploded on the trading scene in the 1990s, with traders reaping double-digit returns using simple statistical phenomena. This chapter discusses common stat-arb strategies deployed in the HFT space.

Stat-arb is named after its primary function: detection of statistically persistent phenomena, most often, with fundamental roots. Such statistically persistent relationships may exist between the current price level of equity and the recently reported earnings of the traded company. The relationships may also be between price levels of multiple fi nancial instruments, linked by some fundamental variables, the price level of one fi nancial instrument and the volatility of another, and many other values.

The critical point in the identifi cation process of fi nancial instruments suitable for stat-arb is that the relationship among the variables has to hold with at least 90 or higher percent statistical confi dence. This level of statistical confi dence is observed when the numerical variation in the tested relationship remains within two standard deviations from its average value. Thus, in a way, stat-arb is a modern and sophisticated cousin of a technical analysis strategy utilizing "Bollinger bands" that showed a two-standard-deviation envelope around the simple moving average of the price, suggesting the likely near-term price path bounds.

Stat-arb models measuring statistical persistence of shown economic phenomena tend to have higher profi tability and longer staying power than models detecting statistical persistence based on data mining alone. An example of stat-arb based on solid economic principles is the exchange-traded fund (eTF) or index arbitrage: by the Law of One Price of fi nance, a traded index or eTF should have the same price as a basket of individual fi nancial instruments comprising the eTF

![](_page_1_Figure_6.jpeg)

**FIGURE 8.1** graphical representation of Order Aggressiveness and Trader Type Distributions in the Limit Order Book

and weighed accordingly. If a mismatch between the do-it-yourself basket and the traded ETF exists, a trader can profitably arbitrage the mismatch, as discussed later in this chapter.

By contrast, a statistical relationship observed between prices of two completely unrelated stocks may be purely random, or "spurious." While the relationship produces a highly significant statistical dependency, it can hardly be used to make meaningful predictions about future values of the stocks under consideration. From a trading strategy point of view, such a relationship is not too different from the statistical relationships shown by Challe (2003), who illustrates the following outrageous spurious relationship: a statistically significant link between the occurrence of sunspots and the predictability of asset returns.

This chapter explores techniques developed for detecting stat-arb relationships, as well as presents specific cases of proven dependencies.

## ■ **Practical Applications of Statistical Arbitrage**

# **General Considerations**

The prices of two or more financial instruments traded in stat-arb models often will be fundamentally related in some fashion or other, but they can nevertheless span a variety of asset classes and individual names. In equities, the companies issuing securities may belong to the same industry and will therefore respond similarly to changes in the broad market. Alternatively, the securities may actually be issued by the same company. Companies often issue more than one class of shares, and the shares typically differ by voting rights. Even shares of the same class issued by the same company but trading on different exchanges may have profitable intraday deviations in prices. In foreign exchange, the pair of instruments chosen can be a foreign exchange rate and a derivative (e.g., a futures contract) on the same foreign exchange rate. The same underlying derivative trading strategy may well apply to equities and fixed-income securities. Passive indices, such as infrequently rebalanced ETFs, can be part of profitable trades when the index and its constituents exhibit temporary price deviations from equilibrium. In options, the pair of instruments may be two options on the same underlying asset but with different times to expiration.

This section discusses numerous examples of statistical arbitrage applied to various financial instruments. Table 8.1 itemizes the strategies discussed subsequently. The selected strategies are intended to illustrate the ideas of fundamental arbitrage. The list is by no means exhaustive, and many additional fundamental arbitrage opportunities can be found.

# **Equities**

Examples of successful statistical arbitrage strategies involving fundamental equities models abound. This section reviews the following popular equity stat-arb trading strategies: pairs, different equity classes of the same issuer, market-neutral pairs trading, liquidity arbitrage, and large-to-small information spillovers.

| <b>TABLE 8.1</b> | Section | Summary of Fundamental Arbitrage Strategies by Asset Class Presented in This |  |  |
|------------------|---------|------------------------------------------------------------------------------|--|--|
| Asset Class      |         | Fundamental Arbitrage Strategy                                               |  |  |
| Equities         |         | Pairs trading                                                                |  |  |
| Equities         |         | Different equity classes of the same issuer                                  |  |  |
| Equities         |         | Risk arbitrage                                                               |  |  |
| Equities         |         | Liquidity rbitragea                                                          |  |  |
| Foreign exchange |         | Triangular arbitrage                                                         |  |  |
| Foreign exchange |         | Uncovered interest parity (UIP) arbitrage                                    |  |  |
| Indices and ETFs |         | Index composition arbitrage                                                  |  |  |
| Options          |         | Volatility curve arbitrage                                                   |  |  |
| Cross-asset      |         | Futures basis trading                                                        |  |  |
| $Cross-asset$    |         | Futures/ETF arbitrage                                                        |  |  |

**Pairs Trading** Pairs trading is the simplest and most commonly used stat-arb strategy. Mathematically, the steps involved in the development of stat-arb trading signals are based on a relationship between price levels or other variables characterizing any two financial instruments. A relationship based on price levels  $S_{i,t}$  and  $S_{i,t}$  for any two instruments *i* and *j* can be can be arrived at through the following procedure:

- 1. Identify the universe of liquid financial instruments: instruments that trade at least once within the desired trading frequency unit. For example, for hourly trading frequency choose securities that trade at least once every hour.
- 2. Measure the difference between prices of every two securities, *i* and *j*, identified in step  $(1)$  across time *t*:

$$\Delta S_{ij,t} = S_{i,t} - S_{j,t}, t \in [1,T]$$
$$\tag{1}$$

where  $T$  is a sufficiently large number of daily observations. According to the central limit theorem (CLT) of statistics, 30 observations at selected trading frequency constitute the bare minimum. The intra-day data, however, may have high seasonality—that is, persistent relationships can be observed at specific hours of the day. Thus, a larger  $T$  of at least 30 daily observations is strongly recommended. For robust inferences, a  $T$  of 500 daily observations (two years) is desirable.

3. For each pair of securities, select the ones with the most stable relationshipsecurity pairs that move together. To do this, Gatev, Goetzmann and Rouwenhorst (1999) perform a simple minimization of the historical differences in returns between every two liquid securities:

$$\min_{i,j} \sum_{t=1}^{T} (\Delta S_{ij,t})^2 \tag{2}$$

The stability of the relationship can also be assessed using cointegration and other statistical techniques.

Next, for each security  $i$ , select the security  $j$  with the minimum sum of squares obtained in equation (2).

4. Estimate basic distributional properties of the difference as follows. Mean or average of the difference:

$$E[\Delta S_t] = \frac{1}{T} \sum_{t=1}^{T} \Delta S_t$$

Standard deviation:

$$\sigma[\Delta S_t] = \frac{1}{T-1} \sum_{t=1}^{T} (\Delta S_t - E[\Delta S_t])^2$$

5. Monitor and act upon differences in security prices: At a particular time  $\tau$ , if

$$\Delta S_{\tau} = S_{i,\tau} - S_{j,\tau} > E[\Delta S_{\tau}] + 2\sigma[\Delta S_{\tau}]$$

sell security  $i$  and buy security  $j$ . However, if

$$\Delta S_{\tau} = S_{i,\tau} - S_{i,\tau} < E[\Delta S_{\tau}] - 2\sigma[\Delta S_{\tau}]$$

buy security  $i$  and sell security  $j$ .

6. Once the gap in security prices reverses to achieve a desirable gain, close out the positions. If the prices move against the predicted direction, activate stop loss.

Instead of detecting statistical anomalies in price levels, statistical arbitrage can be applied to other variables, such as correlation between two securities and traditional fundamental relationships. The details of implementation of statistical arbitrage based on fundamental factors are discussed in detail in the following text.

Pairs-trading strategies can be trained to dynamically adjust to changing market conditions. The mean of the variable under consideration, to which the identified statistical relationships are assumed to tend, can be computed as a moving weighted average with the latest observations being given more weight than the earliest observations in the computation window. Similarly, the standard deviation used in computations can be computed using a limited number of the most recent observations, reflecting the latest economic environment.

Statistical relationships validated by academic research in economics and finance may consistently produce positive results for many traders. Thorough understanding of economic theory helps quantitative analysts distinguish between solid and arbitrary relationships and, in turn, improves the profitability and reduces risk of trading operations that use stat-arb methodology.

In addition to the issues embedded in the estimation of statistical relationships, statistical arbitrage strategies are influenced by numerous adverse market conditions.

Arbitraging Different Equity Classes of the Same Issuer It is reasonable to expect stocks corresponding to two common equity classes issued by the same company to be trading within a relatively constant price range from each other. Different classes of common equity issued by the same company typically diverge in the following two characteristics only: voting rights and number of shares outstanding.

Shares with superior voting rights are usually worth more than the shares with inferior voting rights or nonvoting shares, given that shares with wider voting privileges allow the shareholders to exercise a degree of control over the direction of the company—see Horner (1988) and Smith and Amoako-Adu (1995), for example. Nenova (2003) shows that the stock price premium for voting privileges exists in most countries. The premium varies substantially from country to country and depends on the legal environment, the degree of investor protection, and takeover regulations, among other factors. In countries with the greatest transparency, such as Finland, the voting premium is worth close to zero, whereas in South Korea, the voting premium can be worth close to 50 percent of the voting stock's market value.

Stocks with a higher number of shares outstanding are usually more liquid, prompting actively trading investors to value them more highly (see Amihud and Mendelson, 1986, 1989; Amihud, 2002; Brennan and Subrahmanyam, 1996; Brennan, Chordia, and Subrahmanyam, 1998; and Eleswarapu, 1997). At the same time, the more liquid class of shares is likely to incorporate market information significantly faster than the less liquid share class, creating opportunities for information arbitrage.

A typical trade may work as follows: if the price range widens to more than two standard deviations of the average daily range without a sufficiently good reason, it may be a fair bet that the range will narrow within the following few hours.

The dual-class share strategy suffers from two main shortcomings and may not work for funds with substantial assets under management (AUM).

- 1. The number of public companies that have dual share classes trading in the open markets is severely limited, restricting the applicability of the strategy. In January 2009, for example, Yahoo! Finance carried historical data for two equity classes for just eight companies trading on the New York Stock Exchange (NYSE): Blockbuster, Inc.; Chipotle; Forest City Entertainment; Greif, Inc.; John Wiley & Sons; K V Pharma; Lennar Corp.; and Moog, Inc.
- 2. The daily volume for the less liquid share class is often small, further restricting the capacity of the strategy. Table 8.2 shows the closing price and daily volume for dual-class shares registered on the NYSE on January 6, 2009. For all names, Class B daily volume on January 6, 2009, does not reach even one million in shares and is too small to sustain a trading strategy of any reasonable trading size.

| Company Name              | Ticker Class A | Class A Close | Class A Volume<br>(MM Shares) | Ticker<br>Class B | Class B<br>Close | Class B Volume<br>(MM Shares) |  |  |  |
|---------------------------|----------------|---------------|-------------------------------|-------------------|------------------|-------------------------------|--|--|--|
| Blockbuster, Inc.         | BBI            | 1.59          | 2.947                         | BBI-B             | 0.88             | 0.423                         |  |  |  |
| Chipotle                  | CMG            | 60.38         | 0.659                         | CMG-B             | 55.87            | 0.156                         |  |  |  |
| Forest City Entertainment | FCE-A          | 8.49          | 1.573                         | FCE-B             | 8.41             | 0.008                         |  |  |  |
| Greif, Inc.               | GEF            | 35.42         | 0.378                         | GEF-B             | 35.15            | 0.016                         |  |  |  |
| John Wiley & Sons         | JW-A           | 36.82         | 0.237                         | JW-B              | 36.63            | 0.005                         |  |  |  |
| K V Pharma                | KV-A           | 3.68          | 0.973                         | KV-B              | 3.78             | 0.007                         |  |  |  |
| Lennar Corp.              | LEN            | 11.17         | 8.743                         | LEN-B             | 8.5              | 0.074                         |  |  |  |
| Moog, Inc.                | MOG-A          | 37.52         | 0.242                         | MOG-B             | 37.9             | 0.000                         |  |  |  |

**Table 8.2 Closing Price and Daily Volume of Dual-Class Shares on NYSE on January 6, 2009**

**Risk Arbitrage** Risk arbitrage or market-neutral arbitrage refers to a class of trading models that are based on classical equilibrium finance literature. At core, most market-neutral models are built on the capital asset pricing model (CAPM) developed by Sharpe (1964), Lintner (1965), and Black (1972).

The CAPM is based on the idea that returns on all securities are influenced by the broad market returns. The degree of the co-movement that a particular security may experience with the market is different for each individual security and can vary through time. For example, stocks of luxury companies have been shown to produce positive returns whenever the broad market produces positive returns as well, whereas breweries and movie companies tend to produce higher positive returns whenever the overall market returns are downward sloping.

The CAPM equation is specified as follows:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{M,t} - r_{f,t}) + \varepsilon_t \tag{3}$$

where  $r_{i,t}$  is the return on security *i* at time *t*,  $r_{M,t}$  is the return on a broad market index achieved in time period  $t$ , and  $r_{f,t}$  is the risk-free interest rate, such as Fed Funds rate, valid in time period  $t$ . The equation can be estimated using ordinary least squares (OLS) regression. The resulting parameter estimates,  $\alpha$  and  $\beta$  , measure the abnormal return that is intrinsic to the security ( $\hat{\alpha}$ ) and the security's comovement with the market ( $\beta$ ).

The simplest example of CAPM-based pair arbitrage in equities is trading pairs with the same response to the changes in the broader market conditions, or beta, but different intrinsic returns, or alpha. This type of strategy is often referred to as a market-neutral strategy, with the idea that going long and short, respectively, in two securities with similar beta would neutralize the resulting portfolio from broad market exposure.

Often, the two securities used belong to the same or a similar industry, although this is not mandatory. The alpha and beta for two securities  $i$  and  $j$  are determined from the CAPM equation (3). Once the point estimates for alphas and betas of the two securities are produced, along with standard deviations of those point estimates, the statistical significance of difference in alphas and betas is then determined using the difference in the means test, described here for betas only:

$$\Delta \hat{\beta} = \hat{\beta}_i - \hat{\beta}_j \tag{4}$$

$$\hat{\sigma}_{\Delta\beta} = \sqrt{\frac{\sigma_{\beta_i}^2}{n_i} + \frac{\sigma_{\beta_j}^2}{n_j}} \tag{5}$$

where  $n_i$  and  $n_j$  are the numbers of observations used in the estimation of equation (3) for security  $i$  and security  $j$ , respectively.

The standard  $t$ -ratio statistic is then determined as follows:

Student 
$$t_{\beta} = \frac{\Delta \hat{\beta}}{\hat{\sigma}_{\Delta \beta}}$$
 (6)

The difference test for alphas follows the same procedure as the one outlined for betas in equations  $(4)$  through  $(6)$ .

As with other  $t$ -test estimations, betas can be deemed to be statistically similar if the  $t$  statistic falls within one standard deviation interval:

$$t_{\beta} \in [\Delta \widehat{\beta} - \widehat{\sigma}_{\Delta \beta}, \Delta \widehat{\beta} + \widehat{\sigma}_{\Delta \beta}] \tag{7}$$

At the same time, the difference in alphas has to be both economically and statistically significant. The difference in alphas has to exceed trading costs, TC, and the  $t$ -ratio has to indicate a solid statistical significance, with 95 percent typically considered the minimum:

$$\Delta \hat{\alpha} > TC \tag{8}$$

$$\left| t_{\alpha} \right| > \left[ \Delta \widehat{\alpha} + 2 \widehat{\sigma}_{\Delta \alpha} \right] \tag{9}$$

Once a pair of securities satisfying equations  $(7)$  through  $(9)$  is identified, the trader goes long in the security with the higher alpha and shorts the security with the lower alpha. The position is held for the predetermined horizon used in the forecast.

Variations on the basic market-neutral pair trading strategy include strategies accounting for other security-specific factors, such as equity fundamentals. For example, Fama and French (1993) show that the following three-factor model can be successfully used in equity pair trading:

$$r_{i,t} = \alpha_i + \beta_i^{MKT} MKT_t + \beta_i^{SMB} SMB_t + \beta_i^{HML} HML_t + \varepsilon_t$$
 (10)

where  $r_{i,t}$  is the return on stock *i* at time *t*,  $MKT_t$  is the time-*t* return on a broad market index,  $SMB_t$  (small minus big) is the time-t difference in returns between market indices or portfolios of small and big capitalization stocks, and  $HML_t$  (high minus low) is the return on a portfolio constructed by going long in stocks with comparatively high book-to-market ratios and going short in stocks with comparatively low book-to-market ratios.

**Liquidity Arbitrage** In classical asset pricing literature, a financial security that offers some inconvenience to the prospective investors should offer higher returns to compensate investors for the inconvenience. Limited liquidity is one such inconvenience; lower liquidity levels make it more difficult for individual investors to unwind their positions, potentially leading to costly outcomes. On the flip side, if liquidity is indeed priced in asset returns, then periods of limited liquidity may offer nimble investors highly profitable trading opportunities.

In fact, several studies have documented that less liquid stocks have higher average returns: see Amihud and Mendelson (1986); Brennan and Subrahmanyam (1996); Brennan, Chordia, and Subrahmanyam (1998); and Datar, Naik, and Radcliffe (1998). Trading the illiquid stocks based exclusively on the information that they are illiquid, however, delivers no positive abnormal returns. The relatively high average returns simply compensate prospective investors for the risks involved in holding these less liquid securities.

Pastor and Stambaugh (2003), however, recognize that at least a portion of the observed illiquidity of financial securities may be attributed to market-wide causes. If the market-wide liquidity is priced into individual asset returns, then market illiquidity arbitrage strategies may well deliver consistent positive abnormal returns on the risk-adjusted basis.

Pastor and Stambaugh (2003) find that in equities, stocks whose returns have higher exposure to variability in the market-wide liquidity indeed deliver higher returns than stocks that are insulated from the market-wide liquidity. To measure sensitivity of stock *i* to market liquidity, Pastor and Stambaugh (2003) devise a metric  $\gamma$  that is estimated in the following OLS specification:

$$r_{i,t+1}^{e} = \theta + \beta r_{i,t} + \gamma sign(r_{i,t}^{e}).v_{i,t} + \tau_{t+1}$$
(11)

where  $r_{i,t}$  is the return on stock *i* at time *t*,  $v_{i,t}$  is the dollar volume for stock *i* at time *t*, and  $r_{i,t}^e$  is the return on stock *i* at time *t* in excess of the market return at time *t*:  $r_{i,t}^e = r_{i,t} - r_{m,t}$ . The sign of the excess return  $r_{i,t}^e$  proxies for the direction of the order flow at time  $t$ ; when stock returns are positive, it is reasonable to assume that the number of buy orders in the market outweighs the number of sell orders, and vice versa. The prior time-period return  $r_{i,t}$  is included to capture the first-order autocorrelation effects shown to be persistent in the return time series of most financial securities.

**Large-to-Small Information Spillovers** Equity shares and other securities with relatively limited market capitalization are considered to be "small." The precise cutoff for "smallness" varies from exchange to exchange. On the NYSE in 2002, for example, "small" stocks were those with market capitalization below \$1 billion; stocks with market capitalization of \$1 billion to \$10 billion were considered to be "medium," and "large" stocks were those with market cap in excess of \$10 billion.

Small stocks are known to react to news significantly more slowly than large stocks. Lo and MacKinlay (1990), for example, found that returns on smaller stocks follow returns on large stocks. One interpretation of this phenomenon is that large stocks are traded more actively and absorb information more efficiently than small stocks. Hvidkjaer (2006) further documents "an extremely sluggish reaction" of small stocks to past returns of large stocks and attributes this underreaction to the inefficient behavior of small investors.

A proposed reason for the delay in the response of small stocks is their relative unattractiveness to institutional investors who are the primary source of the information that gets impounded into market prices. The small stocks are unattractive to institutional investors because of their size. A typical size of a portfolio of a midcareer institutional manager is \$200 million; if a portfolio manager decides to invest into small stocks, even a well-diversified share of an institutional portfolio will end up moving the market for any small stock significantly, cutting into profitability and raising the liquidity risk of the position. In addition, ownership of 5 percent or more of a particular U.S. stock must be reported to the Securities and Exchange Commission (SEC), further complicating institutional investing in small stocks. As a result, small stocks are traded mostly by small investors, many of whom use daily data and traditional "low-tech" technical analysis to make trading decisions.

The market features of small stocks make the stocks illiquid and highly inefficient, enabling profitable trading. Llorente, Michaely, Saar, and Wang (2002) studied further informational content of trade volume and found that stocks of smaller firms and stocks with large bid-ask spreads exhibit momentum following high-volume periods. Stocks of large firms and firms with small bid-ask spread, however, exhibit no momentum and sometimes exhibit reversals following highvolume time periods. Profitable trading strategies, therefore, involve trading small stocks based on the results of correlation or cointegration with lagged returns of large stocks as well as the volume of large and small stocks' records during preceding periods.

# **Foreign Exchange**

Foreign exchange has a number of classic models that have been shown to work in the short term. This section summarizes statistical arbitrage applied to triangular arbitrage and uncovered interest rate parity models. Other fundamental foreign exchange models, such as the flexible price monetary model, the sticky price monetary model, and the portfolio model can be used to generate consistently profitable trades in the statistical arbitrage framework.

Triangular Arbitrage Triangular arbitrage exploits temporary deviations from fair prices in three foreign exchange crosses. The following example illustrates triangular arbitrage of EUR/CAD, following a triangular arbitrage example described by Dacorogna et al. (2001). The strategy arbitrages mispricings between the market prices on EUR/CAD and "synthetic" prices on EUR/CAD that are computed as follows:

$$EUR/CAD_{Sunthetic, bid} = EUR/USD_{Market, bid} \times USD/CAD_{Market, bid}$$
(12)

$$EUR/CAD_{Sunthetic, ask} = EUR/USD_{Market, ask} \times USD/CAD_{Market, ask}$$
(13)

If market ask for EUR/CAD is lower than synthetic bid for EUR/CAD, the strategy is to buy market EUR/CAD, sell synthetic EUR/CAD, and wait for the market and synthetic prices to align, then reverse the position capturing the profit. The difference between the market ask and the synthetic bid should be high enough to at least overcome two spreads—on EUR/USD and on USD/CAD. The USD-rate prices used to compute the synthetic rate should be sampled simultaneously. Even a delay as small as one second in price measurement can significantly distort the relationship as a result of unobserved trades that affect the prices in the background; by the time the dealer receives the order, the prices may have adjusted to their noarbitrage equilibrium levels.

**Uncovered Interest Parity Arbitrage** The uncovered interest parity (UIP) is just one such relation. Chaboud and Wright (2005) find that the UIP best predicts changes in foreign exchange rates at high frequencies and daily rates when the computation is run between 4:00 p.m. ET and 9:00 p.m. ET. The UIP is specified as follows:

$$1 + i_t = (1 + i_t^*) \frac{E_t[S_{t+1}]}{S_t}$$
(14)

where  $i_t$  is the one-period interest rate on the domestic currency deposits,  $i_t^*$  is the one-period interest rate on deposits denominated in a foreign currency, and  $S_t$  is the spot foreign exchange price of one unit of foreign currency in units of domestic currency. Thus, for example, if domestic means United States–based and foreign means Swiss, the UIP equation, equation (14), can be used to calculate the equilibrium CHF/USD rate as follows:

$$1 + i_{t,USD} = (1 + i_{t,CHF}^*) \frac{E_t [S_{t+1,CHF/USD}]}{S_{t,CHF/USD}}$$
(15)

The expression can be conveniently transformed to the following regression form suitable for linear estimation:

$$\ln(S_{t+1,CHF/USD}) - \ln(S_{t,CHF/USD}) = \alpha + \beta(\ln(1 + i_{t,USD}) - \ln(1 + i_{t,CHF}^*)) + \varepsilon_{t+1} \qquad (16)$$

A statistical arbitrage of this relationship would look into the statistical deviations of the two sides of equation (16) and make trading decisions accordingly.

#### Indices and ETFs

Index arbitrage is driven by the relative mispricings of indices and their underlying components. Under the Law of One Price, index price should be equal to the price of a portfolio of individual securities composing the index, weighted according to their weights within the index. Occasionally, relative prices of the index and the underlying securities deviate from the Law of One Price and present the following arbitrage opportunities. If the price of the index-mimicking portfolio net of transaction costs exceeds the price of the index itself, also net of transaction costs, sell the index-mimicking portfolio, buy index, hold until the market corrects its index pricing, then realize gain. Similarly, if the price of the index-mimicking portfolio is lower than that of the index itself, sell index, buy portfolio, and close the position when the gains have been realized.

Alexander (1999) shows that cointegration-based index arbitrage strategies deliver consistent positive returns and sets forth a cointegration-based portfolio management technique step by step:

1. A portfolio manager selects or is assigned a benchmark. For a portfolio manager investing in international equities, for example, the benchmark can be a European, Asian, or Far East (EAFE) Morgan Stanley index and its constituent indices. Outperforming the EAFE becomes the objective of the portfolio manager.

2. The manager next determines which countries lead EAFE by running the errorcorrecting model (ECM) with log(EAFE) as a dependent variable and log prices of constituent indices in local currencies as independent (explanatory) variables:

$$\textit{EAFE}_{t} = \alpha + \beta_{1}x_{1,t} + \ldots + \beta_{n}x_{n,t} + \varepsilon_{t}$$

$$\tag{17}$$

where the statistically significant b1…bn coefficients indicate optimal allocations pertaining to their respective country indices *x*1…*x*n, and a represents the expected outperformance of the EAFE benchmark if the residual from the cointegrating regression is stationary. b1…bn can be constrained in estimation, depending on investor preferences.

An absolute return strategy can further be obtained by going long in the indices in proportions identified in step 2 and shorting EAFE.

# **Options**

In options and other derivative instruments with a nonlinear payoff structure, statistical arbitrage usually works between a pair of instruments written on the same underlying asset but having one different characteristic. The different characteristic is most often either the expiration date or the strike price of the derivative. The strategy development proceeds along the steps noted in the previous sections.

# **Cross-Asset**

Statistical arbitrage is not limited to a single asset class. Instead, statistical arbitrage can apply to pairs consisting of a financial instrument and its derivative, or two financial instruments sharing fundamental values.

Basis Trading Futures are financial instruments of choice in many cross-market stat-arb models. Futures prices are linear functions of the underlying asset and are easy to model:

$$F_t = S_t \exp[r_t(T - t)] \tag{18}$$

where *Ft* is the price of a futures contract at time *t*, *St* is the price of the underlying asset (e.g., equity share, foreign exchange rate, or interest rate) also at time *t*, *T* is the time the futures contract expires, and *rt* is the interest rate at time *t.* For foreign exchange futures, *rt* is the differential between domestic and foreign interest rates.

The statistical arbitrage between a futures contract and the underlying asset is known as "basis trading." As with equity pairs trading, the basis-trading process follows the following steps: estimation of the distribution of the contemporaneous price differences, ongoing monitoring of the price differences, and acting upon those differences.

Lyons (2001) documents results of a basis-trading strategy involving six currency pairs: DEM/USD, USD/JPY, GBP/USD, USD/CHF, FRF/USD, and USD/CAD. The strategy bets that the difference between the spot and futures prices reverts to its mean or median values. The strategy works as follows: sell foreign currency futures whenever the futures price exceeds the spot price by a certain predetermined level or more, and buy foreign currency futures whenever the futures price falls short of the spot price by at least a prespecified difference. Lyons (2001) reports that when the predetermined strategy trigger levels are computed as median basis values, the strategy obtains a Sharpe ratio of 0.4 to 0.5.

Futures/ETF Arbitrage In response to macroeconomic news announcements, futures markets have been shown to adjust more quickly than spot markets. Kawaller, Koch, and Koch (1993), for example, show that prices of the S&P 500 futures react to news faster than prices of the S&P 500 index itself, in the Granger causality specification. A similar effect was documented by Stoll and Whaley (1990): for returns measured in 5-minute intervals, both S&P 500 and money market index futures led stock market returns by 5 to 10 minutes.

The quicker adjustment of the futures markets relative to the equities markets is likely due to the historical development of the futures and equities markets. The Chicago Mercantile Exchange, the central clearinghouse for futures contracts in North America, rolled out a fully functional electronic trading platform during the early 1990s; most equity exchanges still relied on a hybrid clearing mechanism that involved both human traders and machines up to the year 2005. As a result, faster information-arbitraging strategies have been perfected for the futures market, while systematic equity strategies remain underdeveloped to this day. By the time this book was written, the lead-lag effect between futures and spot markets had decreased from the 5- to 10-minute period documented by Stoll and Whaley (1990) to a 1- to 2-second advantage. However, profit-taking opportunities still exist for powerful HFT systems with low transaction costs.

Cointegration of Various Financial Instruments/Asset Classes Stat-arb models can also be built on two or more financial instruments, potentially from drastically different asset classes. Often, such multi-instrument multiasset models are developed using cointegration. *Cointegration* refers to a condition whereby prices of two or more financial instruments move in tandem according to a simple specification, parameterized on historical data. A two-instrument cointegration model can be specified as follows:

$$P_{1,t} = \alpha + \beta P_{2,t} + \varepsilon_t \tag{19}$$

where *P*1*,t* is the price of the first financial instrument, *P2,t* is the price of the second financial instrument under consideration, and α and β are coefficients in a simple OLS regression. Instruments 1 and 2 and said to be cointegrated whenever the generated error term <sup>ε</sup> *<sup>t</sup>* is stationary, that is, mean reverting. Several tests for stationarity of error terms exist. Perhaps the simplest test works as follows: if at least 90 percent of error observations,<sup>ε</sup> *<sup>t</sup>* , lie within two standard deviations of<sup>ε</sup> *<sup>t</sup>* away from the mean of <sup>ε</sup> *<sup>t</sup>*, the error series<sup>ε</sup> *<sup>t</sup>* can be considered stationary.

To further fine-tune statistical dependencies between any two securities, a stat-arb researcher may include lagged realizations of price changes in a vector-autoregressive framework to detect stat-arb relationships several time periods ahead of trading time:

$$P_{1,t} = \alpha + \beta_0 P_{2,t} + \beta_1 (P_{2,t} - P_{2,t-1}) + \beta_2 (P_{2,t-1} - P_{2,t-2}) + \dots + \beta_k (P_{2,t-k+1} - P_{2,t-k}) + \varepsilon_t$$

$$(20)$$

$$P_{2,t} = \gamma + \delta_0 P_{1,t} + \delta_1 (P_{1,t} - P_{1,t-1}) + \delta_2 (P_{1,t-1} - P_{1,t-2}) + \dots + \delta_k (P_{1,t-k+1} - P_{1,t-k}) + \omega_t$$

$$(21)$$

The number of lags, *k*, used in the regressions (20) and (21), is typically determined based on statistical significance of the coefficients β*<sup>k</sup>* and<sup>δ</sup> *<sup>k</sup>* . As a rule of thumb, if the absolute value of *t*-ratios accompanying β*<sup>k</sup>* and<sup>δ</sup> *<sup>k</sup>* drop off to less than two, the of the *k*th lag is considered nonexistent, and the *k*th lag becomes the terminal lag in the regressions.

Yet another common way to enhance performance of stat-arb models is to extend the regression of equation (19) with additional financial instruments:

$$P_{1,t} = \alpha + \beta P_{2,t} + \gamma P_{3,t} + \dots + \delta P_{n,t} + \varepsilon_t$$
 (22)

As in equation (19), the key stat-arb criterion of the multi-instrument cointegration is the stationarity of the error terms,<sup>ε</sup> *<sup>t</sup>* . Similar to equations (20) and (21), equation (22) can be extended to include lagged observations of prices.

## ■ **Summary**

Statistical arbitrage is powerful in high-frequency settings as it provides a simple set of clearly defined conditions that are easy to implement in a systematic fashion in high-frequency settings. Statistical arbitrage based on solid economic theories is likely to have longer staying power than strategies based purely on statistical phenomena.

## ■ **End-of-Chapter Questions**

- 1. What are the three types of traders present in financial markets? How do they differ and coexist?
- 2. What are the key principles behind statistical arbitrage? Discuss.
- 3. You are considering trading SPY and E-mini futures on the S&P 500 contracts in a stat-arb model. According to equation (18), prices of SPY and E-mini futures are theoretically linked by a mathematical relationship. Suppose that the shortterm estimate of the cointegration models of equations (20) and (21) generates negative and statistically significant coefficients b1 and δ1. How can SPY and Emini futures on the S&P 500 be arbitraged in this scenario?

- 4. Suppose that, over a long range, high-frequency returns on two stocks are linked by the market-neutral framework of equations (3) through (10) (same b, different α: α1 > α2). In the short term, however, this relationship has reversed, and now α2 > α1 over the past 30 minutes. How can one statistically arbitrage such an occurrence?
- 5. A particular ETF is updated daily. Suppose you are interested in arbitraging the ETF against the basket of securities it comprises. To do so, you run cointegration models pitching the high-frequency ETF returns against returns of a large universe of stocks and pick up some statistically significant dependencies. How do you arbitrage your findings?
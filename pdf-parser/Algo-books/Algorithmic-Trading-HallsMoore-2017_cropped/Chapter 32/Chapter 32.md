# Chapter 32

# Strategy Decay

In this chapter the issue of when to retire a trading strategy will be considered. It will present brief reasons why strategies eventually end up underperforming. It will discuss how this can be measured over time and then describe an implementation in QSTrader that provides this functionality. The methodology will then be applied to some of the previous strategies presented within the book in order to gauge their recent effectiveness.

Strategy decay is one of the trickiest aspects to manage within the realm of quantitative trading. It involves previously well-performing strategies that gradually, and sometimes rapidly, lose their performance characteristics and end up becoming unprofitable.

Quantitative trading strategies almost unilaterally rely on the concept of forecasting and/or statistical mispricing. As more and more trading entities–retail or institutional–implement similar systematic strategies the mispricings give way to price efficiency. The gain derived from such strategies is eroded and then usually falls to the level of transaction costs required to carry it out, making them unprofitable.

This means that quantitative trading is not a "set and forget" activity. In reality quant traders need to have a portfolio of strategies that are slowly "rotated out" over time once any arbitrage opportunities begin to erode. Thus constant research is required to continually develop new profitable "edges" that replace those that have been "arbitraged away".

However some systematic strategies often have large periods of mediocre returns and extensive drawdown. This is particularly prevalent in strategies based on daily data since they tend to have far fewer positively-expected trading "bets". Thus a major challenge for quant researchers lies in identifying when a strategy is truly underperforming due to erosion of edge or whether it is a "temporary" period of poorer performance.

This motivates the need for an effective trailing metric that captures current performance of the strategy in relation to its previous performance. One of the most widely used measures–at least in the institutional quant world–is the annualised rolling Sharpe ratio.

The Sharpe ratio of a strategy is designed to provide a measure of mean excess returns of a strategy as a ratio of the volatility "endured" to achieve those returns. It is a "broad brush" measure of the reward-to-risk ratio of a strategy. The annualised rolling Sharpe ratio simply calculates this value on the previous year's worth of trading data. It provides a continuallyupdated, albeit rearward-looking view of current reward-to-risk.

A low Sharpe ratio (below 1.0) implies that substantial returns volatility is being endured for minimal mean return. A negative Sharpe ratio implies that one would have been better off holding an instrument representing the risk-free rate used in the calculation (often US treasury bills). Not only are the mean returns of the strategy below those achieved by the risk-free rate in this case, but volatility in those underperforming returns is being endured as well!

Hence one way of determining whether a strategy should be considered for retirement is to track its annualised rolling Sharpe and see whether this value trends towards zero, or even into negative territory.

Clearly this does not cover the whole story of risk management. The Sharpe ratio only captures one aspect of risk (its ratio to excess returns) and is a rearward-looking indicator. For instance the Sharpe ratio would provide absolutely no information about unexpected regulatory change, or a data centre crash in a few week's time.

Despite these shortcomings it is a useful indicator of whether a strategy is likely to underperform in the future. It is also sometimes found on an external capital-raising investment prospectus, since a relatively constant trailing Sharpe implies strategy reward-to-risk consistency.

## 32.1 Calculating the Annualised Rolling Sharpe Ratio

The standard Sharpe ratio for strategy returns is given by the following formula:

$$S = \frac{\mathbb{E}(r_s - r_b)}{\sqrt{\text{Var}(r_s - r_b)}}\tag{32.1}$$

It is the ratio of the expectation of the excess returns of the strategy to the standard deviation of those excess returns. In essence it captures the ratio of reward-to-risk, where risk is defined as returns volatility.

In order to calculate an annualised rolling Sharpe ratio it is necessary to make two modifications to this formula. The first is to reduce the set of returns to the last trailing number of annualised trading periods (e.g. for daily data this means take the last 252 close-to-close returns). The second is to multiply the value by the square root of the number of annual trading periods. For strategies trading on a daily timeframe the number of periods is equal to 252, the (approximate) number of trading days in the US:

$$S_{t} = \sqrt{k} \frac{\mathbb{E}(r_{s,t-k} - r_{b,t-k})}{\sqrt{\text{Var}(r_{s,t-k} - r_{b,t-k})}}$$
(32.2)

Where rs,t−<sup>k</sup> refers to the previous k truncated strategy returns rather than the entire history of returns over the strategy lifetime.

This value is calculated every trading period once k results have been generated. The annualised rolling Sharpe is not suitable for calculation unless a year's worth of trading periods have been accumulated. This is because the ratio can be extremely large in the first few periods due to high returns and low variance, thus leading to inflated and unrealistic Sharpe ratios.

It should be noted that the Sharpe ratio is an imperfect measure of "risk", not only for the reasons outlined above, but also because it also penalises upward volatility of returns. That is if the variance of the returns rise strongly in the upward direction the Sharpe ratio will be reduced due to the large denominator.

It should be well remembered that large unexpected upward moves are just as dangerous as large downward moves since they reflect unanticipated behaviour of the strategy. For instance, a large upward performance jump could imply a new regulatory regime that has benefited the strategy. This must now be taken into account in any subsequent strategy development in order to maintain consistency of performance.

# 32.2 Python QSTrader Implementation

The implementation of the annualised rolling Sharpe ratio is now part of the QSTrader codebase and is originally due to [@nwillemse.](https://github.com/nwillemse)

The addition of the annualised rolling Sharpe ratio necessitated an update to the minimum required version of the Pandas library used by QSTrader, which is now 0.18.0. Hence if you wish to use this feature you may need to update your Pandas version to 0.18.0 or greater.

The annualised rolling Sharpe feature is provided as a chart that sits underneath the equity curve in the tearsheet visual output. It is optional and can be activated by setting rolling\_sharpe=True in the instantiation of the TearsheetStatistics class in the backtest. In the class itself it can be seen that it is simply implemented as a member flag:

```
class TearsheetStatistics(AbstractStatistics):
```

```
def __init__(
    self, config, portfolio_handler,
    title=None, benchmark=None, periods=252,
    rolling_sharpe=False
):
    ..
    ..
    self.rolling_sharpe = rolling_sharpe
    ..
    ..
```

To calculate the annualised rolling Sharpe it is necessary to obtain the rolling object by using the rolling method on the strategy returns series, with a lookback window equal to the number of trading periods (self.periods).

The calculation simply multiplies the square root of trading periods by the ratio of the rolling mean to the rolling standard deviation. Note that there is no risk-free rate included here. Zero returns are considered the risk-free alternative. The same is carried out for the benchmark. All of this occurs in the get\_results method of the TearsheetStatistics class:

```
def get_results(self):
    # Equity
    equity_s = pd.Series(self.equity).sort_index()
    # Returns
    returns_s = equity_s.pct_change().fillna(0.0)
    # Rolling Annualised Sharpe
    rolling = returns_s.rolling(window=self.periods)
```

```
rolling_sharpe_s = np.sqrt(self.periods) * (
    rolling.mean() / rolling.std()
)
..
..
statistics["rolling_sharpe"] = rolling_sharpe_s
# Benchmark statistics if benchmark ticker specified
if self.benchmark is not None:
    equity_b = pd.Series(self.equity_benchmark).sort_index()
    returns_b = equity_b.pct_change().fillna(0.0)
    rolling_b = returns_b.rolling(window=self.periods)
    rolling_sharpe_b = np.sqrt(self.periods) * (
        rolling_b.mean() / rolling_b.std()
    )
    ..
    ..
    statistics["rolling_sharpe_b"] = rolling_sharpe_b
    ..
    ..
return statistics
```

To plot the annualised rolling Sharpe a new method \_plot\_rolling\_sharpe has been created. It is very similar to the \_plot\_equity method. It produces a similar plot to the equity curve using identical colours to help distinguish the strategy performance from the benchmark performance. The only minor addition is a dashed vertical line placed at k periods into the strategy simulation to represent the first point at which the trailing ratio is calculated:

```
def _plot_rolling_sharpe(self, stats, ax=None, **kwargs):
```

```
..
..
sharpe = stats['rolling_sharpe']
..
..
if self.benchmark is not None:
    benchmark = stats['rolling_sharpe_b']
    benchmark.plot(
        lw=2, color='gray', label=self.benchmark,
        alpha=0.60, ax=ax, **kwargs
    )
sharpe.plot(
    lw=2, color='green', alpha=0.6, x_compat=False,
```

```
label='Backtest', ax=ax, **kwargs
)
ax.axvline(
    sharpe.index[self.periods],
    linestyle="dashed", c="gray", lw=2
)
ax.set_ylabel('Rolling Annualised Sharpe')
..
..
```

The plot\_results code is modified to include the rolling Sharpe graph if the self.rolling\_sharpe flag is set to True. This is carried out using an offset\_index. The index is used to let Matplotlib know if there are five or six vertical sections in the chart, and if so, to adjust the plot placement:

```
def plot_results(self, filename=None):
    ..
    ..
    if self.rolling_sharpe:
        offset_index = 1
    else:
        offset_index = 0
    vertical_sections = 5 + offset_index
    fig = plt.figure(figsize=(10, vertical_sections * 3.5))
    fig.suptitle(self.title, y=0.94, weight='bold')
    gs = gridspec.GridSpec(vertical_sections, 3, wspace=0.25, hspace=0.5)
    stats = self.get_results()
    ax_equity = plt.subplot(gs[:2, :])
    if self.rolling_sharpe:
        ax_sharpe = plt.subplot(gs[2, :])
    ax_drawdown = plt.subplot(gs[2 + offset_index, :])
    ax_monthly_returns = plt.subplot(gs[3 + offset_index, :2])
    ax_yearly_returns = plt.subplot(gs[3 + offset_index, 2])
    ax_txt_curve = plt.subplot(gs[4 + offset_index, 0])
    ax_txt_trade = plt.subplot(gs[4 + offset_index, 1])
    ax_txt_time = plt.subplot(gs[4 + offset_index, 2])
    self._plot_equity(stats, ax=ax_equity)
    if self.rolling_sharpe:
        self._plot_rolling_sharpe(stats, ax=ax_sharpe)
    self._plot_drawdown(stats, ax=ax_drawdown)
```

.. ..

In order to use the annualised rolling Sharpe in a strategy backtest it remains to turn on the flag in a strategy backtest file where the tearsheet is instiated:

```
..
..
# Use the Tearsheet Statistics
title = ["Example Systematic Trading Strategy"]
statistics = TearsheetStatistics(
    config, portfolio_handler, title,
    benchmark="SPY", rolling_sharpe=True
)
..
..
```

In the next section a selection of updated tearsheets will be generated for various strategies that have been presented in the book so far.

## 32.3 Strategy Results

All of the strategies displayed here are found within previous chapters of the book. The results will simply be redisplayed with the addition of the annualised rolling Sharpe ratio tearsheet visualisation.

#### 32.3.1 Kalman Filter Pairs Trade

Figure 32.1 displays the performance of the Kalman Filter Pairs Trade strategy.

The rolling annualised Sharpe ratio calculation for the strategy begins just over midway into 2010, after 252 trading periods. The Sharpe ratio initially trends up in excess of 2.0 through mid-2011 but a period of large returns volatility, culminating in flat and subsequently dwindling performance through 2012 reduces the Sharpe ratio heavily in this period to negative territory.

After the strategy picks up again in mid-2013 the annualised Sharpe slowly recovers back towards 2.0. Although by the end of 2016 it is unclear if the strategy is beginning to decay once again.

Note how difficult it would have been at the end of 2012, in a live implementation, to determine if the strategy would need retiring due to the long downward trend in annualised Sharpe. This highlights how important it is to have a solid understanding of the statistical behaviour of the returns distribution in a backtest.

#### 32.3.2 Aluminum Smelting Cointegration Strategy

Figure 32.2 displays the performance of the Aluminum Smelting Cointegration strategy.

Since this strategy is carried out over a relatively short time frame (just under two years) the rolling annualised Sharpe is only calculated for a short period.

Initially the Sharpe ratio is high at approximately 2.25. This is a consequence of the rapid increase in performance in early 2015, which soon flattens out. Once these high return periods have "fallen out" of the rolling calculation the Sharpe ratio rapidly decreases to -0.5 during the early half of 2016, which it remains at through to the end of 2016.

![](_page_6_Figure_1.jpeg)

Figure 32.1: Kalman Filter Pairs Trade - TLT/IEI

Such a substantial drop in risk-adjusted performance is a clear indication that the strategy should be considered for retirement. Either any particular alpha/edge previously associated with its predictions has now been arbitraged away, or the underlying structural relationship has changed.

In this example it could be that the aluminum refining firm introduced its own aluminum smelting hedging strategy by trading natural gas prices on its own account. This would have the effect of diminishing the impact of natural gas prices on its own profitability, thus rendering this strategy difficult, if not impossible, to implement profitably.

![](_page_7_Figure_1.jpeg)

Figure 32.2: Aluminum Smelting Strategy - ARNC/UNG

#### 32.3.3 Sentdex Sentiment Analysis Strategy

Figure 32.3 displays the performance of the Sentdex Sentiment Analysis strategy applied to defence stocks.

In the previous chapter for this particular strategy three separate simulations were carried out, one for tech stocks, one for energy and one for defence. This particular example uses the set of defence stocks, which include BA, GD, LMT, RTN and NOC–all components of the S&P500.

It can be seen that the strategy had a significant upward period in 2013 which gives rise to a high trailing annualised Sharpe of 2.5, exceeding 3.5 by the start of 2014. However the strategy performance remained flat through 2014, which caused a gradual reduction in the annualised

![](_page_8_Figure_1.jpeg)

Figure 32.3: Sentiment Sentdex Strategy - Defence Stocks

rolling Sharpe since the volatility of returns was largely similar. By the start of 2015 the Sharpe was between 0.5 and 1.0, meaning more risk was being taken per unit of return at this stage. By the end of 2015 the Sharpe had risen slightly to around 1.5, largely due to some consistent upward gains in the latter half of 2015.

Note that the Sharpe ratio of both the benchmark and the strategy were broadly similar from mid-2014 onwards, suggesting that there was little to be gained (from a reward-to-risk point of view) by investing in the strategy as opposed to buying and holding SPY. Although this of course ignores the initial gains made by the strategy in 2013.
<http://ssrn.com/abstract=1748633> .

### **Notes**

1 I would like to thank Professor Peter Carr (New York University) for his contributions to this chapter.

2 The strategy may still be the result of backtest overfitting, but at least the trading rule would not have contributed to that problem.

3 The trading rule *R* could be characterized as a function of the three barriers, instead of the horizontal ones. That change would have no impact on the procedure. It would merely add one more dimension to the mesh (20 × 20 × 20). In this chapter we do not consider that setting, because it would make the visualization of the method less intuitive.

# **CHAPTER 14**

# **Backtest Statistics**

# **14.1 Motivation**

In the previous chapters, we have studied three backtesting paradigms: First, historical simulations (the walk-forward method, Chapters 11 and 12). Second, scenario simulations (CV and CPCV methods, Chapter 12). Third, simulations on synthetic data (Chapter 13). Regardless of the backtesting paradigm you choose, you need to report the results according to a series of statistics that investors will use to compare and judge your strategy against competitors. In this chapter we will discuss some of the most commonly used performance evaluation statistics. Some of these statistics are included in the Global Investment Performance Standards (GIPS), <sup>1</sup> however a comprehensive analysis of performance requires metrics specific to the ML strategies under scrutiny.

# **14.2 Types of Backtest Statistics**

Backtest statistics comprise metrics used by investors to assess and compare various investment strategies. They should help us uncover potentially

problematic aspects of the strategy, such as substantial asymmetric risks or low capacity. Overall, they can be categorized into general characteristics, performance, runs/drawdowns, implementation shortfall, return/risk efficiency, classification scores, and attribution.

# **14.3 General Characteristics**

The following statistics inform us about the general characteristics of the backtest:

- **Time range:** Time range specifies the start and end dates. The period used to test the strategy should be sufficiently long to include a comprehensive number of regimes (Bailey and López de Prado [2012]).
- **Average AUM:** This is the average dollar value of the assets under management. For the purpose of computing this average, the dollar value of long and short positions is considered to be a positive real number.
- **Capacity:** A strategy's capacity can be measured as the highest AUM that delivers a target risk-adjusted performance. A minimum AUM is needed to ensure proper bet sizing (Chapter 10) and risk diversification (Chapter 16). Beyond that minimum AUM, performance will decay as AUM increases, due to higher transaction costs and lower turnover.
- **Leverage:** Leverage measures the amount of borrowing needed to achieve the reported performance. If leverage takes place, costs must be assigned to it. One way to measure leverage is as the ratio of average dollar position size to average AUM.
- **Maximum dollar position size:** Maximum dollar position size informs us whether the strategy at times took dollar positions that greatly exceeded the average AUM. In general we will prefer strategies that take maximum dollar positions close to the average AUM, indicating that they do not rely on the occurrence of extreme events (possibly outliers).
- **Ratio of longs:** The ratio of longs show what proportion of the bets involved long positions. In long-short, market neutral strategies, ideally this value is close to 0.5. If not, the strategy may have a position bias, or the backtested period may be too short and unrepresentative of future market conditions.
- **Frequency of bets:** The frequency of bets is the number of bets per year in the backtest. A sequence of positions on the same side is considered part of the same bet. A bet ends when the position is flattened or flipped to the opposite side. The number of bets is always smaller than the number

of trades. A trade count would overestimate the number of independent opportunities discovered by the strategy.

- **Average holding period:** The average holding period is the average number of days a bet is held. High-frequency strategies may hold a position for a fraction of seconds, whereas low frequency strategies may hold a position for months or even years. Short holding periods may limit the capacity of the strategy. The holding period is related but different to the frequency of bets. For example, a strategy may place bets on a monthly basis, around the release of nonfarm payrolls data, where each bet is held for only a few minutes.
- **Annualized turnover:** Annualized turnover measures the ratio of the average dollar amount traded per year to the average annual AUM. High turnover may occur even with a low number of bets, as the strategy may require constant tuning of the position. High turnover may also occur with a low number of trades, if every trade involves flipping the position between maximum long and maximum short.
- **Correlation to underlying:** This is the correlation between strategy returns and the returns of the underlying investment universe. When the correlation is significantly positive or negative, the strategy is essentially holding or short-selling the investment universe, without adding much value.

Snippet 14.1 lists an algorithm that derives the timestamps of flattening or flipping trades from a pandas series of target positions ( tPos ). This gives us the number of bets that have taken place.

### **SNIPPET 14.1 DERIVING THE TIMING OF BETS FROM A SERIES OF TARGET POSITIONS**

Snippet 14.2 illustrates the implementation of an algorithm that estimates the average holding period of a strategy, given a pandas series of target positions ( tPos ).

### **SNIPPET 14.2 IMPLEMENTATION OF A HOLDING PERIOD ESTIMATOR**

# **14.4 Performance**

Performance statistics are dollar and returns numbers without risk adjustments. Some useful performance measurements include:

- **PnL:** The total amount of dollars (or the equivalent in the currency of denomination) generated over the entirety of the backtest, including liquidation costs from the terminal position.
- **PnL from long positions:** The portion of the PnL dollars that was generated exclusively by long positions. This is an interesting value for assessing the bias of long-short, market neutral strategies.

- **Annualized rate of return:** The time-weighted average annual rate of total return, including dividends, coupons, costs, etc.
- **Hit ratio:** The fraction of bets that resulted in a positive PnL.
- **Average return from hits:** The average return from bets that generated a profit.
- **Average return from misses:** The average return from bets that generated a loss.

### **14.4.1 Time-Weighted Rate of Return**

Total return is the rate of return from realized and unrealized gains and losses, including accrued interest, paid coupons, and dividends for the measurement period. GIPS rules calculate time-weighted rate of returns (TWRR), adjusted for external cash flows (CFA Institute [2010]). Periodic and sub-periodic returns are geometrically linked. For periods beginning on or after January 1, 2005, GIPS rules mandate calculating portfolio returns that adjust for dailyweighted external cash flows.

We can compute the TWRR by determining the value of the portfolio at the time of each external cash flow. <sup>2</sup> The TWRR for portfolio *i* between subperiods [ *t* − 1, *t* ] is denoted *r<sup>i</sup> , <sup>t</sup>* , with equations

$$\begin{split} r_{i,t} &= \frac{\pi_{i,t}}{K_{i,t}} \\ \pi_{i,t} &= \sum_{j=1}^{J} [(\Delta P_{j,t} + A_{j,t}) \theta_{i,j,t-1} + \Delta \theta_{i,j,t} (P_{j,t} - \overline{P}_{j,t-1})] \\ K_{i,t} &= \sum_{j=1}^{J} \tilde{P}_{j,t-1} \theta_{i,j,t-1} + \max \left\{ 0, \sum_{j=1}^{J} \overline{\tilde{P}}_{j,t} \Delta \theta_{i,j,t} \right\} \end{split}$$

where

- π *<sup>i</sup>* , *<sup>t</sup>* is the mark-to-market (MtM) profit or loss for portfolio *i* at time *t.*
- *K <sup>i</sup> , <sup>t</sup>* is the market value of the assets under management by portfolio *i* through subperiod *t.* The purpose of including the max{.} term is to fund additional purchases (ramp-up).

- $A_{j,t}$  is the interest accrued or dividend paid by one unit of instrument  $j$  at time t.
- $P_{j,t}$  is the clean price of security *j* at time *t*.
- $\theta_{i,j,t}$  are the holdings of portfolio *i* on security *j* at time *t*.
- $\tilde{P}_{j,t}$  is the dirty price of security *j* at time *t*.
- $\overline{P}_{i,t}$  is the average transacted clean price of portfolio *i* on security *j* over subperiod *t*.
- $\overline{\tilde{P}}_{j,t}$  is the average transacted dirty price of portfolio *i* on security *j* over subperiod *t*.

Cash inflows are assumed to occur at the beginning of the day, and cash outflows are assumed to occur at the end of the day. These sub-period returns are then linked geometrically as

$$\varphi_{i,T} = \prod_{t=1}^{T} (1 + r_{i,t})$$

The variable  $\varphi_{i,T}$  can be understood as the performance of one dollar invested in portfolio *i* over its entire life,  $t = 1, ..., T$ . Finally, the annualized rate of return of portfolio *i* is

$$R_i = (\varphi_{i,T})^{-y_i} - 1$$

where  $y_i$  is the number of years elapsed between  $r_{i,1}$  and  $r_{i,T}$ .

### 14.5 Runs

Investment strategies rarely generate returns drawn from an IID process. In the absence of this property, strategy returns series exhibit frequent runs. Runs are uninterrupted sequences of returns of the same sign. Consequently, runs increase downside risk, which needs to be evaluated with proper metrics.

### 14.5.1 Returns Concentration

Given a time series of returns from bets,  $\{r_t\}_{t=1,\dots,T}$ , we compute two weight series,  $w^-$  and  $w^+$ :

$$\begin{split} r^+ &= \{r_t | r_t \ge 0\}_{t=1,\ldots,T} \\ r^- &= \{r_t | r_t < 0\}_{t=1,\ldots,T} \\ w^+ &= \left\{ r_t^+ \Bigg(\sum_t r_t^+ \Bigg)^{-1} \right\}_{t=1,\ldots,T} \\ w^- &= \left\{ r_t^- \Bigg(\sum_t r_t^- \Bigg)^{-1} \right\}_{t=1,\ldots,T} \end{split}$$

Inspired by the Herfindahl-Hirschman Index (HHI), for  $|| w^+ || > 1$ , where  $||.||$  is the size of the vector, we define the concentration of positive returns as

$$h^{+} \equiv \frac{\sum_{t} \left(w_{t}^{+}\right)^{2} - ||w^{+}||^{-1}}{1 - ||w^{+}||^{-1}} = \left(\frac{\mathbf{E}\left[\left(r_{t}^{+}\right)^{2}\right]}{\mathbf{E}\left[r_{t}^{+}\right]^{2}} - 1\right) \left(||r^{+}|| - 1\right)^{-1}$$

and the equivalent for concentration of negative returns, for  $|| w^- || > 1$ , as

$$h^{-} \equiv \frac{\sum_{t} \left(w_{t}^{-}\right)^{2} - ||w^{-}||^{-1}}{1 - ||w^{-}||^{-1}} = \left(\frac{\mathbf{E}\left[\left(r_{t}^{-}\right)^{2}\right]}{\mathbf{E}\left[r_{t}^{-}\right]^{2}} - 1\right)(||r^{-}|| - 1)^{-1}$$

From Jensen's inequality, we know that E[ $r^+_{t}$ ]<sup>2</sup>  $\leq$  E[( $r^+_{t}$ )<sup>2</sup>]. And because  $\frac{\mathrm{E}[(r_t^+)^2]}{\mathrm{E}[r_t^+]^2} \leq ||r^+||, \text{ we deduce that } \mathrm{E}[\ r^+_{\ t}]^2 \leq \mathrm{E}[(\ r^+_{\ t})^2] \leq \mathrm{E}[\ r^+_{\ t}]^2||\ r^+||, \text{ with an equivalent boundary on negative bet returns. These definitions have a few}$ interesting properties:

1. 
$$0 \le h^+ \le 1$$
  
2.  $h^+ = 0 \Leftrightarrow w^+_{t} = ||w^+||^{-1}$ ,  $\forall t$  (uniform returns)  
3.  $h^+ = 1 \Leftrightarrow \exists i | w_i^+ = \sum_t w_t^+$  (only one non-zero return)

It is easy to derive a similar expression for the concentration of bets across months, *h* [ *t* ]. Snippet 14.3 implements these concepts. Ideally, we are interested in strategies where *bets* ' returns exhibit:

- high Sharpe ratio
- high number of bets per year, ||*r <sup>+</sup>* || + ||*r <sup>−</sup>* || = *T*
- high hit ratio (relatively low ||*r <sup>−</sup>* ||)
- low *h <sup>+</sup>* (no right fat-tail)
- low *h <sup>−</sup>* (no left fat-tail)
- low *h* [*t* ] (bets are not concentrated in time)

### **SNIPPET 14.3 ALGORITHM FOR DERIVING HHI CONCENTRATION**

### **14.5.2 Drawdown and Time under Water**

Intuitively, a drawdown (DD) is the maximum loss suffered by an investment between two consecutive high-watermarks (HWMs). The time under water (TuW) is the time elapsed between an HWM and the moment the PnL exceeds the previous maximum PnL. These concepts are best understood by reading Snippet 14.4. This code derives both DD and TuW series from either (1) the series of returns ( dollars = False ) or; (2) the series of dollar performance ( dollar = True ). Figure 14.1 provides an example of DD and TuW.

![](_page_8_Figure_0.jpeg)

**Figure 14.1** Examples of drawdown (DD) and time under water + (TuW)

#### **SNIPPET 14.4 DERIVING THE SEQUENCE OF DD AND TuW**

### **14.5.3 Runs Statistics for Performance Evaluation**

Some useful measurements of runs statistics include:

- **HHI index on positive returns:** This is getHHI(ret[ret > = 0]) in Snippet 14.3.
- **HHI index on negative returns:** This is getHHI(ret[ret < 0]) in Snippet 14.3.
- **HHI index on time between bets:** This is getHHI(ret.groupby (pd.TimeGrouper (freq = 'M')).count()) in Snippet 14.3.
- **95-percentile DD:** This is the 95th percentile of the DD series derived by Snippet 14.4.
- **95-percentile TuW:** This is the 95th percentile of the TuW series derived by Snippet 14.4.

# **14.6 Implementation Shortfall**

Investment strategies often fail due to wrong assumptions regarding execution costs. Some important measurements of this include:

**Broker fees per turnover:** These are the fees paid to the broker for turning the portfolio over, including exchange fees.

- **Average slippage per turnover:** These are execution costs, excluding broker fees, involved in one portfolio turnover. For example, it includes the loss caused by buying a security at a fill-price higher than the midprice at the moment the order was sent to the execution broker.
- **Dollar performance per turnover:** This is the ratio between dollar performance (including brokerage fees and slippage costs) and total portfolio turnovers. It signifies how much costlier the execution could become before the strategy breaks even.
- **Return on execution costs:** This is the ratio between dollar performance (including brokerage fees and slippage costs) and total execution costs. It should be a large multiple, to ensure that the strategy will survive worsethan-expected execution.

# **14.7 Efficiency**

Until now, all performance statistics considered profits, losses, and costs. In this section, we account for the risks involved in achieving those results.

### **14.7.1 The Sharpe Ratio**

Suppose that a strategy's excess returns (in excess of the risk-free rate), { *r<sup>t</sup>* } *<sup>t</sup>* = 1, …, *T* , are IID Gaussian with mean μ and variance σ <sup>2</sup> . The Sharpe ratio (SR) is defined as

$$SR = \frac{\mu}{\sigma}$$

The purpose of SR is to evaluate the skills of a particular strategy or investor. Since μ, σ are usually unknown, the true SR value cannot be known for certain. The inevitable consequence is that Sharpe ratio calculations may be the subject of substantial estimation errors.

# **14.7.2 The Probabilistic Sharpe Ratio**

The probabilistic Sharpe ratio (PSR) provides an adjusted estimate of SR, by removing the inflationary effect caused by short series with skewed and/or fattailed returns. Given a user-defined benchmark <sup>3</sup> Sharpe ratio ( *SR* \*) and an observed Sharpe ratio , PSR estimates the probability that is greater than a hypothetical *SR* \*. Following Bailey and López de Prado [2012], PSR can be estimated as

$$\widehat{PSR}\left[SR^*\right] = Z \left[ \frac{\left(\widehat{SR} - SR^*\right)\sqrt{T - 1}}{\sqrt{1 - \hat{\gamma}_3 \widehat{SR} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{SR}^2}} \right]$$

where *Z* [.] is the cumulative distribution function (CDF) of the standard Normal distribution, *T* is the number of observed returns, is the skewness of the returns, and is the kurtosis of the returns ( for Gaussian returns). For a given *SR* \*, increases with greater (in the original sampling frequency, i.e. non-annualized), or longer track records ( *T* ), or positively skewed returns ( ), but it decreases with fatter tails ( ). Figure 14.2 plots for , and *SR* \* = 1.0 as a function of and *T.*

![](_page_12_Figure_0.jpeg)

![](_page_12_Figure_1.jpeg)

#### **14.7.3 The Deflated Sharpe Ratio**

The deflated Sharpe ratio (DSR) is a PSR where the rejection threshold is adjusted to reflect the multiplicity of trials. Following Bailey and López de Prado [2014], DSR can be estimated as , where the benchmark Sharpe ratio, *SR* \*, is no longer user-defined. Instead, *SR* \* is estimated as

$$SR^* = \sqrt{V\left[\left\{\widehat{SR}_n\right\}\right]}\left((1-\gamma)Z^{-1}\left[1-\frac{1}{N}\right] + \gamma Z^{-1}\left[1-\frac{1}{N}e^{-1}\right]\right)$$

<span id="page-13-1"></span>where is the variance across the trials' estimated SR, *N* is the number of independent trials, *Z* [.] is the CDF of the standard Normal distribution, γ is the Euler-Mascheroni constant, and *n* = 1, …, *N* . [Figure 14.3](#page-13-0) plots *SR* \* as a function of and *N* .

![](_page_13_Figure_1.jpeg)

<span id="page-13-0"></span>**[Figure 14.3](#page-13-1)** *SR* \* as a function of and *N*

The rationale behind DSR is the following: Given a set of SR estimates, , its expected maximum is greater than zero, even if the true SR is zero. Under the null hypothesis that the actual Sharpe ratio is zero, *H <sup>0</sup>* : *SR* = 0, we know that the expected maximum can be estimated as the *SR* \*. Indeed, *SR* \* increases quickly as more independent trials are attempted ( *N* ), or the trials involve a greater variance . From this knowledge we derive the third law of backtesting.

# **SNIPPET 14.5 MARCOS' THIRD LAW OF BACKTESTING. MOST DISCOVERIES IN FINANCE ARE FALSE BECAUSE OF ITS VIOLATION**

"Every backtest result must be reported in conjunction with all the trials involved in its production. Absent that information, it is impossible to assess the backtest's 'false discovery' probability."

Marcos López de Prado

*Advances in Financial Machine Learning* (2018)

### **14.7.4 Efficiency Statistics**

Useful efficiency statistics include:

- **Annualized Sharpe ratio:** This is the SR value, annualized by a factor , where *a* is the average number of returns observed per year. This common annualization method relies on the assumption that returns are IID.
- **Information ratio:** This is the SR equivalent of a portfolio that measures its performance relative to a benchmark. It is the annualized ratio between the average excess return and the tracking error. The excess return is measured as the portfolio's return in excess of the benchmark's return. The tracking error is estimated as the standard deviation of the excess returns.
- **Probabilistic Sharpe ratio:** PSR corrects SR for inflationary effects caused by non-Normal returns or track record length. It should exceed 0.95, for the standard significance level of 5%. It can be computed on absolute or relative returns.
- **Deflated Sharpe ratio:** DSR corrects SR for inflationary effects caused by non-Normal returns, track record length, and multiple testing/selection bias. It should exceed 0.95, for the standard significance level of 5%. It can be computed on absolute or relative returns.

# **14.8 Classification Scores**

In the context of meta-labeling strategies (Chapter 3, Section 3.6), it is useful to understand the performance of the ML overlay algorithm in isolation. Remember that the primary algorithm identifies opportunities, and the

secondary (overlay) algorithm decides whether to pursue them or pass. A few useful statistics include:

**Accuracy:** Accuracy is the fraction of opportunities correctly labeled by the overlay algorithm,

$$accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

where TP is the number of true positives, TN is the number of true negatives, FP is the number of false positives, and FN is the number of false negatives.

**Precision:** Precision is the fraction of true positives among the predicted positives,

$$precision = \frac{TP}{TP + FP}$$

**Recall:** Recall is the fraction of true positives among the positives,

$$recall = \frac{TP}{TP + FN}$$

**F1** : Accuracy may not be an adequate classification score for metalabeling applications. Suppose that, after you apply meta-labeling, there are many more negative cases (label '0') than positive cases (label '1'). Under that scenario, a classifier that predicts every case to be negative will achieve high accuracy, even though recall=0 and precision is undefined. The F1 score corrects for that flaw, by assessing the classifier in terms of the (equally weighted) harmonic mean of precision and recall,

$$F_1 = 2 \frac{precision \cdot recall}{precision + recall}$$

As a side note, consider the unusual scenario where, after applying metalabeling, there are many more positive cases than negative cases. A classifier that predicts all cases to be positive will achieve TN=0 and FN=0, hence accuracy=precision and recall=1. Accuracy will be high, and F1 will not be smaller than accuracy, even though the classifier is not able to discriminate between the observed samples. One solution would be to

switch the definitions of positive and negative cases, so that negative cases are predominant, and then score with F1.

**Negative log-loss:** Negative log-loss was introduced in Chapter 9, Section 9.4, in the context of hyper-parameter tuning. Please refer to that section for details. The key conceptual difference between accuracy and negative log-loss is that negative log-loss takes into account not only whether our predictions were correct or not, but the probability of those predictions as well.

<span id="page-16-1"></span>See Chapter 3, Section 3.7 for a visual representation of precision, recall, and accuracy. [Table 14.1](#page-16-0) characterizes the four degenerate cases of binary classification. As you can see, the F1 score is not defined in two of those cases. For this reason, when Scikit-learn is asked to compute F1 on a sample with no observed 1s or with no predicted 1s, it will print a warning ( UndefinedMetricWarning ), and set the F1 value to 0.

### <span id="page-16-0"></span>**[Table 14.1](#page-16-1) The Four Degenerate Cases of Binary Classification**

| Condition        | Collapse | Accuracy   | Precision | Recall | F1    |
|------------------|----------|------------|-----------|--------|-------|
| Observed all 1s  | TN=FP=0  | =recall    | 1         | [0,1]  | [0,1] |
| Observed all 0s  | TP=FN=0  | [0,1]      | 0         | NaN    | NaN   |
| Predicted all 1s | TN=FN=0  | =precision | [0,1]     | 1      | [0,1] |
| Predicted all 0s | TP=FP=0  | [0,1]      | NaN       | 0      | NaN   |

When all observed values are positive (label '1'), there are no true negatives or false positives, thus precision is 1, recall is a positive real number between 0 and 1 (inclusive), and accuracy equals recall. Then, .

When all predicted values are positive (label '1'), there are no true negatives or false negatives, thus precision is a positive real number between 0 and 1 (inclusive), recall is 1, and accuracy equals precision. Then, .

# **14.9 Attribution**

The purpose of performance attribution is to decompose the PnL in terms of risk classes. For example, a corporate bond portfolio manager typically wants to understand how much of its performance comes from his exposure to the following risks classes: duration, credit, liquidity, economic sector, currency, sovereign, issuer, etc. Did his duration bets pay off? What credit segments does he excel at? Or should he focus on his issuer selection skills?

These risks are not orthogonal, so there is always an overlap between them. For example, highly liquid bonds tend to have short durations and high credit rating, and are normally issued by large entities with large amounts outstanding, in U.S. dollars. As a result, the sum of the attributed PnLs will not match the total PnL, but at least we will be able to compute the Sharpe ratio (or information ratio) per risk class. Perhaps the most popular example of this approach is Barra's multi-factor method. See Barra [1998, 2013] and Zhang and Rachev [2004] for details.

Of equal interest is to attribute PnL across categories within each class. For example, the duration class could be split between short duration (less than 5 years), medium duration (between 5 and 10 years), and long duration (in excess of 10 years). This PnL attribution can be accomplished as follows: First, to avoid the overlapping problem we referred to earlier, we need to make sure that each member of the investment universe belongs to one and only one category of each risk class at any point in time. In other words, for each risk class, we split the entire investment universe into disjoint partitions. Second, for each risk class, we form one index per risk category. For example, we will compute the performance of an index of short duration bonds, another index of medium duration bonds, and another index of long duration bonds. The weightings for each index are the re-scaled weights of our investment portfolio, so that each index's weightings add up to one. Third, we repeat the second step, but this time we form those risk category indices using the weights from the investment universe (e.g., Markit iBoxx Investment Grade), again re-scaled so that each index's weightings add up to one. Fourth, we compute the performance metrics we discussed earlier in the chapter on each of these indices' returns and excess returns. For the sake of clarity, in this context the excess return of a short duration index is the return using (re-scaled) portfolio weightings (step 2) minus the return using (re-scaled) universe weightings (step 3).

### **Exercises**
# **Predictability of Asset Prices**

Predictability can be interpreted in many ways in finance. The fundamental issue in asset pricing is to determine the relationship between risk and reward. To quantify such a relationship, an economic model is built to "predict" how the expected asset returns should vary with their risk measures. In this case, predictability means contemporaneous association between the expected return of an asset and the expected returns of different risk factors. For example, the capital asset pricing model (CAPM) predicts that a security's expected risk premium is proportional to the expected return from the market factor, where the proportionality reflects the systematic risk measure. This type of predictability is not the focus of this article. Instead, the focus is on whether future security returns can be predicted from current known information.

One important assumption used to build a rational asset pricing model is the market efficiency (*see* **Efficient Market Hypothesis**), in which security prices reflect all available information quickly and fairly. This was interpreted literally in the 1950s and 1960s as saying that any lagged variables possess no power in predicting current or future security prices or returns. The modern finance theory, however, has a different interpretation for the evidence of return predictability. In fact, researchers have recognized since 1980s that the expected returns can vary over time due to changes in investors' risk tolerance and/or investment opportunities [30] over business cycles. If business cycles are predictable to some degree, returns can also be predictable, which poses no challenge to the efficient market hypothesis (EMH). Under this view, one should not rely solely on the historical average returns to estimate expected returns in assisting our investment decisions. In other words, the task of estimating the expected returns precisely largely depends on our ability to predict future stock returns.

Given the fact that the serial correlations for aggregate stock returns are weak especially in the recent decade, the quest for additional predictors goes on. Many financial variables have been shown to possess predictive power for stock returns. A partial list of these variables can be characterized as variables that are related to interest rates: relative interest rate [7], term spread and the default spread [7, 16, 23], inflation rate [14, 18]; variables that are related to "one over the price": dividend yield [10], payout yield [4], earning–price ratio and dividend–earnings (payout) ratio [26], book-to-market ratio [25, 32]; and other variables including aggregate net issuing activity [2] and consumption–wealth–income ratio [27].

Although the focus is on the rational explanation for predictability, the evidence has also been interpreted differently under different views. Their differences are illustrated by the following story. Once there were four students walking on a street with their professor. A dollar bill lying on the sidewalk quickly caught the professor's eyes. The professor asked the four students why nobody was picking up the dollar bill. The first student answered although the dollar bill was real, people just pretended not seeing it. The second student argued that the dollar bill was just an illusion (or a statistical illusion). The third student said that, even though the dollar bill was real, no one would bother to pick it up because it was too costly to pick it up (or transactions costs). The last student's answer was that the dollar bill was real. Someone left it there for a needy person. Generally speaking, the first student is a behaviorist; the second and third students hold the traditional efficient market view; and the last student holds the modern view on the EMH. No matter which student's answer represents your view, predictability cannot be too large. There is an old saying: if you can predict the market, why aren't you rich!

The existence of predictability is crucial in testing the conditional asset pricing models [19], in return decomposition [8], in asset allocation [22], and so on. Because of the theoretical foundation for predictability, this article focuses primarily on aggregate market returns. Predictability is also related to anomalies. An anomaly is defined as the deviation from an asset pricing model. In most empirical studies, anomalies are tied to a specific part of the market, such as small firms, firms with low book-to-market ratios, and so on, or particular sample periods, such as January, weekends, and so on. A detailed review on anomalies can be found in [35].

This article intends to offer a perspective on both the evidence and the reasons for return predictability. A detailed discussion about the economic reasons for predictability is given in the section Economic Interpretation of Predictability. Recent empirical studies have uncovered many useful predictors, which are summarized in the section Understanding Some Useful Predictors. Predictability is not without controversy. Many of the statistical issues in testing the predictability are discussed in the section Statistical Issues, followed by conclusion in the last section.

# **Evidence on Predictability**

The most simple form of predictability is the return autocorrelation. To gain a perspective on the magnitude of the serial correlation, returns of different frequencies and over different sample periods are examined. Owing to the availability of daily returns, the whole sample period is from 1962 to 2006. The summary statistics is listed in Table 1 for both value-weighted and equal-weighted NYSE/AMEX/NASDAQ composite index returns.

For the whole sample period, the average valueweighted index daily return is 0*.*044% with a volatility of 0*.*859%. Such a large difference between average return and volatility implies a very low Sharpe ratio of 5%. If returns are autocorrelated, the "true" Sharpe ratio should be larger.a For the value-weighted index returns, the autocorrelation is about 13%. Such a large autocorrelation further increases to 31% when an equal-weighted index is used. If we fit an *AR(*1*)* model to the equal-weighted index returns, we see an *R*<sup>2</sup> of 9*.*61%! The autocorrelation difference in the two types of index returns suggests that small stocks are more predictable than large stocks. To see whether such a predictability is stable over time, the whole sample period is split into two. From Table 1, it is clear that most of the predictability from past returns concentrates in the early sample period from 1962 to 1984, with autocorrelations as high as 22*.*4 and 38*.*5% for value-weighted and equal-weighted indices, respectively.

Predictability in daily returns might be subject to market microstructure effects discussed in the section The Economic Interpretation of Predictability. One way to alleviate such effects is to examine the behavior of monthly returns. For both value- and equal-weighted index returns, the autocorrelations have been substantially attenuated. For example, over the whole sample period, autocorrelation for value-weighted index returns is only 4*.*3%, almost negligible. For the equal-weighted index, however, the autocorrelation is still as large as 17*.*6% for the whole sample period and is stable over the two subsample periods. Therefore, it can be concluded that return serial correlations are more likely to occur in small stocks. Given there are still substantial serial correlations in low-frequency small stock return data, market microstructure effects cannot be the only factor.

If future returns can only be weakly predicted by past returns, are there other variables that help to predict returns? In Table 2, we further study return predictability using three other variables—the dividend yield, the repurchasing yield, and the relative interest rate. Our sample starts in 1952 after a major shift in the interest rate regime by the Federal Reserve. To be representative, we focus on the value-weighted index returns. During the first 17 years from 1952 to 1978, both the dividend yield and the relative interest rate

**Table 1** Autocorrelations in index returns

| Sample<br>period         | Value weighted |       |       | Equal weighted |       |       |
|--------------------------|----------------|-------|-------|----------------|-------|-------|
|                          | Mean           | SD    | Corr. | Mean           | SD    | Corr. |
| Panel A: daily returns   |                |       |       |                |       |       |
| 1962–2006                | 0.044          | 0.859 | 13.2  | 0.069          | 0.744 | 31.0  |
| 1962–1984                | 0.035          | 0.794 | 22.4  | 0.068          | 0.787 | 38.5  |
| 1985–2006                | 0.053          | 0.922 | 6.1   | 0.071          | 0.696 | 21.0  |
| Panel A: monthly returns |                |       |       |                |       |       |
| 1962–2006                | 0.929          | 4.216 | 4.3   | 1.186          | 5.345 | 17.6  |
| 1962–1984                | 0.772          | 4.422 | 6.0   | 1.285          | 6.252 | 16.4  |
| 1985–2006                | 1.079          | 4.010 | 1.9   | 1.092          | 4.312 | 20.0  |

This table reports the characteristics of NYSE/AMEX/NASDAQ composite index returns over different samples periods and for different frequencies. "Corr." stands for the first-order autocorrelation; "SD" is the standard deviation

| Dependent<br>variable | $r_t$                              | $(D/P)_t$ | $(F/P)_t$ | $rrel_t$ | Adjusted<br>$R^2$ |
|-----------------------|------------------------------------|-----------|-----------|----------|-------------------|
|                       | Panel A: sample period 1952–1978   |           |           |          |                   |
| $r_{t+1}$             | 0.061                              | 10.90     | 0.675     | $-11.67$ | 0.062             |
| $(D/P)_{t+1}$         | $-0.000$                           | 0.966     | 0.003     | 0.042    | 0.956             |
| $(F/P)_{t+1}$         | $-0.001$                           | 0.038     | 0.943     | 0.034    | 0.898             |
| $rrel_{t+1}$          | 0.000                              | 0.032     | 0.005     | 0.731    | 0.529             |
|                       | Panel A: sample period $1979-2005$ |           |           |          |                   |
| $r_{t+1}$             | 0.030                              | 0.461     | 3.508     | $-0.801$ | 0.009             |
| $(D/P)_{t+1}$         | $-0.000$                           | 0.994     | $-0.009$  | 0.005    | 0.985             |
| $(F/P)_{t+1}$         | $-0.001$                           | 0.029     | 0.971     | 0.071    | 0.960             |
| $rrel_{t+1}$          | $-0.000$                           | 0.009     | $-0.010$  | 0.751    | 0.560             |

**Table 2** VAR results for index returns

This table reports the VAR results for the four variables including the value-weighted NYSE/AMEX/NASDAQ composite index return, dividend yield, repurchasing yield, and the relative interest rate over different sample periods. The bold face number indicates that the estimate is statistically significant at a 5% level

have helped to predict returns, with an adjusted  $R^2$ of  $6.2\%$ . In contrast, the repurchasing yield becomes more important over the next 17 years from 1979 to 2005, with an adjusted  $R^2$  of 0.9%. The evidence suggests that returns are predictable even if not by their past returns. Despite large persistence of all three predictors as shown in Table 2, statistical adjustment for estimates will not likely take away the predictive power of the three variables (see the section Statistical Issues).

### **Predictability and Market Efficiency**

Historically, predictability has been associated with market inefficiency. According to the fundamental law of valuation, a security price should reflect its expected fundament value for risk-neutral investors with zero interest rate:

$$P_{t} = E[V^{*}|\mathcal{I}_{t}], \quad P_{t+1} = E[V^{*}|\mathcal{I}_{t+1}] \quad (1)$$

where  $V^*$  is the fundamental value and  $\mathcal{I}_t$  is the information set at time t. Since the information set  $\mathcal{I}_t$ is included in the information set  $\mathcal{I}_{t+1}$ , the following result is obtained by the law of iterated expectations:

$$P_{t} = E[V^{*}|\mathcal{I}_{t}] = E[E(V^{*}|\mathcal{I}_{t+1})|\mathcal{I}_{t}] = E[P_{t+1}|\mathcal{I}_{t}]$$
(2)

Equation (2) suggests that security prices should follow a Martingale process.<sup>b</sup> The best predictor for

future prices is the current price. In other words, we have

$$\text{Cov}[(P_{t+j} - P_{t+i}), (P_{t+l} - P_{t+k}) | \mathcal{I}_t] = 0 \qquad (3)$$

where  $i < j < k < l$ . In other words, the nonoverlapping price changes are uncorrelated at all leads and lags. If we interpret the price difference as a return, it means that returns should be unpredictable.

This analysis defines the notion of EMH. Financial markets are said to be efficient if security prices rapidly reflect all relevant information about asset values, and all securities are fairly priced in light of the available information. In other words, the EMH describes how security prices should react to available information and how prices should evolve over time. Under this framework, return predictability serves as evidence against the EMH.

Does the EMH indeed exclude predictability? To answer this question, we focus on a stronger version of the Martingale process, which is the random walk process, and assume that investors are risk averse. The random walk process was first used by Bachelier (1900) to model stock prices in his dissertation, and was rekindled by Merton in the late 1960s. For convenience, we use log price  $p_t$ 

$$p_{t+1} = \mu + p_t + \epsilon_{t+1} \tag{4}$$

where  $\mu$  is the expected price change. If we define return as  $r_{t+1} = p_{t+1} - p_t$ , equation (4) can be expressed as

$$r_{t+1} = \mu + \epsilon_{t+1} \tag{5}$$

Strictly speaking, the EMH only puts a restriction on the residual  $\epsilon_{t+1}$  to satisfy the condition of  $E[\epsilon_{t+1}|I_t] = 0$  at any time *t* in either equation (4) or (5). Since  $\mu$  is determined by an asset pricing model, such as the CAPM, the traditional view on the  $EMH$ implicitly assumes that  $\mu$  is constant. The modern finance theory, however, has offered a different view on  $\mu$ . For example, Fama and French [17] have suggested that the risk premium might be higher in the economic downturn than in the peak of a business cycle. This evidence suggests that the expected return might be time varying. In fact, many asset pricing models since Merton have emphasized the idea of changing investment opportunities, which requires additional risk compensation over time. Alternatively, investors' risk tolerance might change over time, which will cause the investors to demand different levels of risk premium. No matter which scenario is more likely, one should allow  $\mu$  to be time varying:

$$r_{t+1} = \mu_{t+1} + \epsilon_{t+1} \tag{6}$$

Although under the EMH, we still have the condition of  $E[\epsilon_{t+1}|\mathcal{I}_t] = 0$ ,  $E[\mu_{t+1}|\mathcal{I}_t]$  is not necessarily constant. For example, if risk premia changes with the business cycle and the business cycle is predictable, return should also be predictable. This analysis opens a channel for the predictability to coexist with the EMH.

Returns from a buy-and-hold strategy on the market portfolio correspond to returns for a representative investor. Predictability means that someone can implement a trading strategy that requires a full investment in some periods and a zero or a short position in other periods in order to earn higher returns than those from a buy-and-hold strategy. Clearly, this investment strategy cannot be implemented by the representative investor since he/she has to fully invest in the equity market. Although such a strategy will pay off in a long run, it is not without risk in short term. The success of this strategy depends on the degree of predictability. Therefore, predictability cannot be too large in order to prevent too many investors defecting from being representative investors.

# The Economic Interpretation of Predictability

Without assuming irrationality and market inefficiency, how can we interpret predictability under the traditional framework? Most explanations focus on market microstructure effects and transactions costs. This section reviews the bid-ask bounce, nonsynchronous trading, and transactions costs in explaining the return autocorrelation.

#### Bid-ask Bounce

Returns tend to be negatively autocorrelated in a short-run. One possible explanation is offered by Roll [34] from the perspective of bid and ask price differences. In the absence of information, sell orders and buy orders arrive with the same probabilities. In other words, a buy order is likely to follow a sell order, which results in a negative autocorrelation. In particular, let  $P_t^*$  be the fundamental value:

$$P_t = P_t^* + I_t(s/2) \tag{7}$$

$$I_t = \begin{cases} +1 & \text{if buy order with prob} = 0.5\\ -1 & \text{if sell order with prob} = 0.5 \end{cases} \tag{8}$$

where  $s$  is the bid-ask spread. This implies a price change of  $\Delta P_t = \Delta P_t^* + (I_t - I_{t-1})s/2$ . In other words, autocorrelation is related to the spread  $s$  in the following way:

$$\text{Cov}(\Delta P_{t-1}, \Delta P_t) = -s^2/4 \tag{9}$$

Since the bid-ask spreads tend to be larger for small company stocks than for large stocks, autocorrelation will be stronger for small firms than for large stocks, other things being equal. Equation (9) can also be used to back out the implied bid-ask spread.

If the autocorrelation is due to differences in the bid and ask prices, the effect should be smaller if the average bid and ask prices are used to compute returns instead of the actual closing prices. Similarly, low-frequency returns, such as monthly returns, should have weaker autocorrelation than high-frequency returns, such as daily returns, which is true in general. We should also see a drop in autocorrelations over time when the average bid-ask spread shrinks, especially after decimalization. This is confirmed in Table 1. In general, investors cannot design a trading strategy to obtain excess returns in this case, since the bid and ask effect is due to the market friction.

5

#### Nonsynchronous Trading

Although individual stock returns might exhibit negative serial correlation, portfolio returns tend to be positively autocorrelated. Lo and MacKinlay [29] have offered "nonsynchronous trading" as a mechanism in generating such a positive autocorrelation. In practice, not all stocks, especially small stocks, are traded at any given moment. On the arrival of market wide news, these stocks that are not traded currently will have similar returns to those traded today when trading resumes next period, which will make the portfolio with all stocks look like autocorrelated.

To illustrate the idea, suppose that there are two stocks  $A$  and  $B$  following random walk processes, implying no autocorrelation in their own returns. At the release of a market wide news at time  $t = 0$ , we would have observed returns of  $R_1^A$  and  $R_1^B$  for stocks  $A$  and  $B$ , respectively. Owing to the commonality of the news, we assume  $\text{Cov}(R_1^A, R_1^B) > 0$ . If stock A is not traded and stock  $B$  is traded, however, we will only observe  $\hat{R}_1^A = 0$  and  $\hat{R}_1^B = R_1^B$ . Similarly, there is a common news released at  $t = 1$ . Both stocks are traded this time, resulting in returns of  $R_2^A$  and  $R_2^B$  for the two stocks. Owing to the random walk assumption on individual stocks, we have  $\text{Cov}(R_1^A, R_2^A) = 0$  and  $\text{Cov}(R_1^B, R_2^B) = 0$ . This structure can be summarized as follows:

Stock A : | 
$$\hat{R}_{1}^{A} = 0$$
 |  $\hat{R}_{2}^{A} = R_{1}^{A} + R_{2}^{A}$  |  
Stock B : |  $\hat{R}_{1}^{B} = R_{1}^{B}$  |  $\hat{R}_{2}^{B} = R_{2}^{B}$  |  
 $t = 0$   $t = 1$   $t = 2$  (10)

Now, consider an equal-weighted portfolio of the two stocks. The portfolio returns in the two periods are  $\hat{R}_1^P = \frac{1}{2}R_1^B$  and  $\hat{R}_2^P = \frac{1}{2}(R_2^B + R_1^A + R_2^A)$ . It is easy to see that  $\text{Cov}(\hat{R}_1^{\tilde{P}}, \hat{R}_2^{\tilde{P}}) = \frac{1}{2}\text{Cov}(R_1^A, R_1^B) > 0.$ The same idea applies to the case when different stocks are traded at different times. Using daily returns from 1962 to 1985 to form 20 size portfolios, Lo and MacKinlay reported the following first-order autocorrelations and the probability of nontrading (Table 3):

Clearly, a large autocorrelation of  $35\%$  in small stock portfolio returns can be supported by a 29% likelihood of nontrading in small stocks.<sup>c</sup> However, it is difficult to justify the 17% autocorrelation in large stock portfolio returns by the corresponding likelihood of nontrading. In addition, the cross autocorrelation of 33% from the large stock portfolio to the small stock portfolio is also consistent with

**Table 3** The probability of nontrading; adopted from Lo and Mackinlay [29]

| $t \mid t + 1$ | Small | Medium | Large | Probability<br>nontrading |
|----------------|-------|--------|-------|---------------------------|
| Small          | 0.35  | 0.21   | 0.02  | 0.291                     |
| Medium         | 0.39  | 0.31   | 0.09  | 0.025                     |
| Large          | 0.33  | 0.36   | 0.17  | 0.008                     |

the nontrading in small stocks. Under this view, no money can be made even with a positive return autocorrelation.

#### Transactions Costs

Nontrading is a bit of an econometrics device. Instead, security prices could be slow to update in the arrival of information due to transactions costs. In other words, transactions costs put a wedge in how prices might change over time. Let  $P_t^*$  be investors' correct valuation. They will trade only when the price cover the transactions costs. In other words, there will be a bound around the current price. Only when  $P^*$ accumulates to the degree that overcomes the bound, we will see a price change. Otherwise, there will be zero excess demand within the bound. Such a slow adjustment will create a positive autocorrelation in security returns.

#### Cross Autocorrelation

The evidence of large stock returns predicting small stock returns seems to be persuasive since it existed in both daily and monthly stock returns. Although one might attribute the phenomenon to the nonsynchronous trading story on the daily frequency, nontrading is less likely for monthly returns. In response, Boudoukh *et al.* [5] offered an alternative explanation that utilizes the serial correlation and the contemporaneous correlation to explain the cross correlation.

Suppose that security *i*'s return follows an  $AR(1)$ process of the following form:

$$r_{i,t+1} = \mu + \theta r_{i,t} + \epsilon_{i,t+1} \tag{11}$$

It is easy to see that  $\theta = \text{Corr}(r_{i,t+1}, r_{i,t})$ . Multiplying both sides of equation (11) by  $r_{j,t}$  and assuming that  $\text{Cov}(\epsilon_{i,t+1}, r_{j,t}) = 0$ , we have the following relation:

$$\operatorname{Corr}(r_{i,t+1}, r_{j,t}) = \operatorname{Corr}(r_{i,t+1}, r_{i,t}) \operatorname{Corr}(r_{i,t}, r_{j,t})$$
(12)

|                     |      | Portfolio Small $_{t+1}$ Medium $_{t+1}$ Large $_{t+1}$ |      | $\text{Small}_{t}$ Large, |      |
|---------------------|------|---------------------------------------------------------|------|---------------------------|------|
| $Small_{\ell}$      | 0.36 | 0.19                                                    | 0.03 |                           |      |
| $\text{Medium}_{t}$ | 0.35 | 0.22                                                    | 0.06 | 0.89                      |      |
| $\text{Large}_{t}$  | 0.28 | 0.21                                                    | 0.07 | 0.72                      | 0.91 |

Table 4 Portfolio correlations adopted from Boudoukh et al. [5]

This table reports cross- and auto-correlations among size portfolios

As seen from equation  $(12)$ , the cross autocorrelation is essentially the self-autocorrelation acted on contemporaneous correlation. Using a different sample period, Boudoukh et al. [5] found that results are consistent with equation (12) (Table 4).

Applying equation  $(12)$ , we can compute the predicted cross autocorrelations as

$$\text{Corr}^*(r_{\text{small},t+1}, r_{\text{large},t})$$
  
= 
$$\text{Corr} (r_{\text{small},t+1}, r_{\text{samll},t}) \text{Corr}(r_{\text{small},t}, r_{\text{large},t})$$
  
= 
$$0.36 \times 0.72 = 0.26 \qquad (13)$$
  
$$\text{Corr}^*(r_{\text{large},t+1}, r_{\text{small},t})$$

$$= \text{Corr } (r_{\text{large},t+1}, r_{\text{large},t}) \text{Corr}(r_{\text{large},t}, r_{\text{small},t})$$
$$= 0.07 \times 0.72 = 0.05 \tag{14}$$

These numbers are very close to the actual cross autocorrelations shown in the table. Therefore, we do not need frequent nontrading to justify the observed cross autocorrelation. However, we still need to understand the serial correlation.

#### Time-varying Expected Returns

The mechanism for the observed autocorrelation, discussed in the previous sections, largely relies on market frictions. As discussed in the section Predictability and Market Efficiency, an alternative rational explanation for predictability is the time-varying expected return. Given the unobservability nature of expected returns, Conrad and Kaul [13] proposed to characterize the movement in expected returns as following a simple  $AR(1)$ process of

$$r_{t+1} = E_t(r_{t+1}) + \epsilon_{t+1} \tag{15}$$

$$E_t(r_{t+1}) = \bar{r} + \phi E_{t-1}(r_t) + u_t \tag{16}$$

Note that the coefficients in equations  $(15)$  and  $(16)$ can be estimated using the Kalman filter procedure. Testing the hypothesis of time-varying expected return is equivalent to test whether  $\phi = 0$  in the above models. Using the 10 size-sorted weekly (Wednesday to Tuesday) portfolio returns from 1962 to 1985, Conrad and Kaul [13] found that the autocorrelations coefficients are 41 and 9% for the small and the large decile portfolios, respectively, which are both statistically significant when compared to the confidence bound of  $1/\sqrt{T} = 0.03$ . Although the persistence parameter estimates ( $\hat{\phi}$ ) of 0.589 and 0.087 for small and large portfolios, respectively, are very different, they are statistically significant at a  $1\%$ level.

It is important to understand why expected returns change over time. In the CAPM world, it is implicitly assumed that a firm will continue to produce the same widgets and face the same uncertainty when selling these widgets in the market. In other words, the risk structure in future cash flows (CFs) is fixed. Thus, the comovement with the overall market is fixed. At the same time, investors' attitude toward risk does not change, which implies constant expected returns. Such a model structure may reasonably describe the real world over a short period of time

Over a longer horizon, however, investment opportunities can change due to either technological advances or changes in consumers' preference toward goods and services. For example, Apple used to be in the business of making personal computers and software 10 years ago. Today, a significant portion of Apple's business is in the consumer electronics including music players and cell phones. Under this view, both the risk environment of a firm and the risk tolerance of investors could change over time. Therefore, the observed predictability may simply provide compensation for investors' exposure to the risk of change in investment opportunities or reflect the differences in the required risk compensation due to change in the risk tolerance over different economic conditions. In this case, a representative investor will not try to utilize the predictability to alter his/her asset allocations. For example, if he/she knows that the next period stock return will likely be high, he/she should allocate more assets to stocks. However, if he/she understands that the high return is associated with high expected return due to his/her increased risk aversion next period, he/she would not increase his/her holding of the risky stocks.

# **Understanding Some Useful Predictors**

In an interesting paper by Boudoukh *et al.* [5], it is argued that the observed autocorrelation in returns neither is due to market inefficiency nor can be attributed to time-varying expected returns. If autocorrelation in the returns of an index, such as the *S*&*P*500, is due to market inefficiency or timevarying expected returns, the same autocorrelation should be observed in the *S*&*P*500 future contract returns too, but they did not find supportive evidence.d This result seems to kill the predictability associated with autocorrelation, but does not necessarily provide evidence against other form of predictability. Moreover, autocorrelation in returns is a sufficient condition for predictability. It is not a necessary condition. There could exist nonreturn-based predictors. Suppose that the return generating process is as follows:

$$r_{t+1} = \beta z_t + \epsilon_{t+1} \tag{17}$$

where *zt* is a predictor with Cov*(zt, t*<sup>+</sup>1*)* = 0 and Cov*(t, t*<sup>+</sup>1*)* = 0. Since Cov*(rt*<sup>+</sup>1*, rt)* = *β*Cov*(zt, rt)* + Cov*(t*<sup>+</sup>1*, rt)* ≈ *β*Cov*(zt, rt)*, autocorrelation could be close to zero as long as Cov*(zt, rt)* is small, which is usually the case.

Therefore, recent literature has focused its attention on predictors other than past returns. For example, an incomplete list includes short-term interest rate, term spread, default spread, inflation rate, dividend yield, book-to-market ratio, consumption–wealth–income ratio, repurchasing yield, and so on. It is important to know why these variables predict returns in the first place. Without theory, a variable found to be useful in predicting stock returns could be a result of data mining.

A closer look at these predictors reveals that they are either related to business cycles or associated with stock prices. Since expected returns could vary with business cycles, variables that predict business cycles such as the term spread or the default spread should be useful predictors. Many significant predictors, such as the dividend yield, book-to-market ratio, and repurchasing yield, contain the element of one over price. This common feature comes from the fact that security prices reflect investors' expectations, and expectations are good predictors of future values. To further illustrate this rationale, we can use mathematical models to relate returns to prices or other variables.

#### *The Dividend–price Ratio—Log-linearization*

Perhaps the most frequently used predictor is the dividend–price ratio or the dividend yield. This is also the variable that has been scrutinized the most [1]. Despite many statistical issues discussed in the following section, it is important to understand why the dividend–price ratio should predict future returns. We start from the following return identity:

$$R_{t+1} = \frac{P_{t+1} + D_{t+1}}{P_t} = \frac{P_{t+1}}{D_{t+1}} \frac{D_t}{P_t} \frac{D_{t+1}}{D_t} \left[ 1 + \frac{D_{t+1}}{P_{t+1}} \right]$$
(18)

It is difficult to allow time-varying expected return due to the nonlinearity in equation (18). We, thus, take natural log on both sides of equation (18) and apply Taylor series expansion around the steady state. After simplifying [8], we obtain the following equation:

$$d_t - p_t = \text{const} + \rho (d_{t+1} - p_{t+1}) + r_{t+1} - \Delta d_{t+1}$$
(19)

where *ρ* = 1*/(*1 + *D/P )* = 1*/*1*.*04 = 0*.*96 (with *D/P* being the steady-state dividend–price ratio), *dt*<sup>+</sup><sup>1</sup> = *dt*<sup>+</sup><sup>1</sup> − *dt* , and lowercase variables represent log of the corresponding uppercase variables. Under the assumption of stationary dividend–price ratio, we can solve equation (19) forward,

$$d_{t} - p_{t} = \text{const} + \sum_{j=0}^{\infty} \rho^{j} (-\Delta d_{t+1+j} + r_{t+1+j})$$
(20)

Equation (20) implies that a high dividend–price ratio must mean either a low future dividend growth or a high future return. In addition, dividends and returns that are closer to the present are more influential than dividends and returns far in the future due to the fact that *ρ* is less than 1.

From an empirical perspective, we can compute the volatility of dividend–price ratio by multiplying both sides of equation (20) by *(dt* − *pt)*

$$\operatorname{Var}(d_{t} - p_{t}) = -\operatorname{Cov}\left(d_{t} - p_{t}, \sum_{j=0}^{\infty} \rho^{j} \Delta d_{t+1+j}\right) + \operatorname{Cov}\left(d_{t} - p_{t}, \sum_{j=0}^{\infty} \rho^{j} r_{t+1+j}\right)$$
(21)

Since the volatility of *(dt* − *pt)* is positive, it is clear that the dividend–price ratio will forecast either dividend growth or future returns. Empirical evidence suggests that the *(d* − *p)* variable does not forecast future dividend growth. Therefore, the *(d* − *p)* ratio must forecast future returns. Again, such a predictability does not imply market inefficiency in predicting *t*<sup>+</sup><sup>1</sup> in equation (6). A testing strategy based on equation (21) is to regress the sum of future returns on the dividend–price ratio:

$$r_{t+1} + \cdots + r_{t+\tau} = \alpha + \beta(\tau)(d_t - p_t) + \epsilon_{t+1, t+\tau}$$

$$(22)$$

where *τ* is the number of future periods. Table 5 is adapted from Campbell *et al.* [9] on monthly NYSE/AMEX/NASDAQ composite index returns. Clearly, the degree of predictability measured by *R*<sup>2</sup> increases monotonically with the return horizon. For example, *R*2s are 0*.*7, 8*.*6, 21*.*7, and 41*.*9% over 1 month, 1 year, 2 years, and 4 years, respectively, in the early sample period of 1927–1951. Similarly, *R*2s continue to be impressive with 1*.*8, 18*.*8, 32*.*2, and 41*.*7% over 1 month, 1 year, 2 years, and 4 years, respectively, in the later sample period from 1952 to 1994.

### *Issues with Long-horizon Regressions*

Long-horizon regressions, such as equation (22), were first advocated by Fama and French [15]. Despite the impressive magnitude of *R*2s, the power of the associated long-horizon tests is doubtful. The issue involves the use of overlapping observations due to the availability of data [33]. In general, overlapping samples could lead to large efficiency gains when the independent variables in a predictive regression are serially uncorrelated. However, most predictors are highly autocorrelated, which implies limited efficiency gains when using overlapping observations. For example, for the 60 years of returns used in the Fama and French [15] study, although the nominal sample size is large using overlapping returns, the effective sample size is not much larger than 12

**Table 5** Long-horizon results for index returns

| Forecast<br>horizon | 1<br>Month                       | 3<br>Months | 12<br>Months | 24<br>Months | 48<br>Months |
|---------------------|----------------------------------|-------------|--------------|--------------|--------------|
|                     |                                  |             |              |              |              |
|                     | Panel A: sample period 1927–1994 |             |              |              |              |
| β(τ )               | 0.016                            | 0.043       | 0.200        | 0.386        | 0.654        |
| t (τ )              | 1.553                            | 1.420       | 2.257        | 4.115        | 3.870        |
| R2(τ )              | 0.007                            | 0.014       | 0.073        | 0.143        | 0.261        |
|                     | Panel A: sample period 1927–1951 |             |              |              |              |
| β(τ )               | 0.024                            | 0.054       | 0.304        | 0.667        | 1.085        |
| t (τ )              | 0.980                            | 0.793       | 1.915        | 3.841        | 3.693        |
| R2(τ )              | 0.007                            | 0.011       | 0.086        | 0.217        | 0.419        |
|                     | Panel A: sample period 1951–1994 |             |              |              |              |
| β(τ )               | 0.027                            | 0.080       | 0.327        | 0.579        | 0.843        |
| t (τ )              | 3.118                            | 3.152       | 3.181        | 3.072        | 3.508        |
| R2(τ )              | 0.018                            | 0.049       | 0.188        | 0.322        | 0.417        |

This table reports results from regressing future *τ* months returns on current dividend–price ratio for the value-weighted NYSE/AMEX/NASDAQ composite index return. The regression model is given as follows:

$$r_{t+1}+\cdots+r_{t+\tau}=\alpha+\beta(\tau)(d_t-p_t)+\epsilon_{t+1,t+\tau}$$

(the nonoverlapping 5-year sample) due to the highly persistent regressor. As pointed out by Boudoukh *et al.* [6], if an innovation in an independent variable happens to coincide with the next period return, this relationship will be repeated many times in the longhorizon regression since the shock will not die out for many periods and the particular return will appear many times in the overlapping return series.

Under the null hypothesis of no autocorrelation in returns, that is, *β(τ )* = 0*,* ∀*τ* in equation (22), Kirby [24] has shown the following asymptotic result for the *R*<sup>2</sup> from a predictive regression:

$$T \times R^2 \xrightarrow{d} \chi^2(K) \tag{23}$$

where *T* is the number of observations and *K* is the number of independent variables in the regression. Let us use a numerical example to illustrate the point. For a univariate regression with *K* = 1 and *T* = 12, what would we expect to see?

- Since the mean of a *χ*<sup>2</sup>*(*1*)* random variable is 1, we have *E(*12*R*<sup>2</sup>*)* = 1, which implies that *E(R*<sup>2</sup>*)* = 8*.*3%.
- The 95% cutoff for *R*<sup>2</sup> is expected to be 32% since the critical value for a *χ*<sup>2</sup>*(*1*)* distribution under the same confidence level is 3*.*84. In other words, we can expect to see *R*2s as high as 32% even though there is no predictability.

Therefore, long-horizon regression results are avoided in this article.

### *The Payout Ratio or the Repurchasing Yield*

Recently, Boudoukh *et al.* [4] have proposed to use the total payout ratio as a predictor for stock returns. The importance of the new predictor can be illustrated by its impressive *R*<sup>2</sup> of 26% using annual data over the sample period from 1926 to 2003. The use of payout ratio can be justified since investors' total wealth could also be affected by share repurchasing. In fact, representative investors should care about the total distribution, which includes both the direct dividend distributions and repurchases. If there are rational reasons to believe that dividend yield predicts stock returns, the payout yield should play a similar role. In fact, the implementation of the SEC rule 10*b* − 18 in 1982 gives firms an incentive to rely more on repurchases due to the tax advantages for investors.

**Payout Ratio.** Repurchasing could be used either to reduce the effect of stock option exercise or to substitute for dividends. To construct a measure that reflects the latter, Boudoukh *et al.* [4] used change in treasury stock adjusted for potential asynchronicity between the repurchase and option exercise as a measure of repurchasing (TS). They also used total repurchasing from the CF statement. Results are summarized in Table 6. Clearly, the predictive power of the dividend–price ratio (*D/P*) has gone down when comparing *R*2s from the two sample periods. In particular, *R*<sup>2</sup> has decreased from 13 to 8% when including the recent sample period.

|             | ln(D/P ) | ln(CF/M) | ln(TS/M) | ln(0.1 + Net payout) |
|-------------|----------|----------|----------|----------------------|
| 1926–2003   |          |          |          |                      |
| Coef        | 0.116    | 0.209    | 0.172    | 0.759                |
| t-ratio     | 2.240    | 3.396    | 2.854    | 5.311                |
| R2          | 0.055    | 0.091    | 0.080    | 0.262                |
| Sim p-value | 0.083    | 0.011    | 0.020    | 0.000                |
| 1926–1984   |          |          |          |                      |
| Coef        | 0.296    | 0.280    | 0.300    | 0.794                |
| t-ratio     | 3.666    | 3.688    | 3.741    | 5.342                |
| R2          | 0.130    | 0.121    | 0.135    | 0.300                |
| Sim p-value | 0.044    | 0.054    | 0.043    | 0.001                |

**Table 6** Dividend yield and payout ratio

This table reports results from predictive regressions using various predictors. "CF/M" is the total repurchasing from cash flow statement (CF) over the total market value, while "TS/M" is change in treasury stock adjusted for potential asynchronicity between the repurchase and option exercise as a measure of repurchasing (TS) over the total market value. "*D/P*" is the usual dividend–price ratio for the value-weighted NYSE/AMEX/NASDAQ composite index

|                      | 1952–2005  |            | 1952–1978  |            | 1979–2005  |            |
|----------------------|------------|------------|------------|------------|------------|------------|
| Frequency            | D/P        | F/P        | D/P        | F/P        | D/P        | F/P        |
| Monthly<br>Quarterly | 0.5<br>1.9 | 1.0<br>2.5 | 1.9<br>5.6 | 0.0<br>0.0 | 0.0<br>0.7 | 1.7<br>5.6 |

**Table 7** The adjusted *R*2s for predictive regression using the dividend yield (D/P) and/or the repurchasing yield (F/P) over different sample periods

In contrast, the repurchasing yield (measured as the ratio between repurchasing and market capitalization) is impressive. No matter how it is measured, the explanatory power is much larger than the pure dividend–price ratio. Moreover, when using the net payout yield (measured as the ratio between repurchasing minus new issuing plus dividend and the market capitalization), *R*<sup>2</sup> is as high as 26%. Although the payout yield is important empirically, its significance is overstated in Boudoukh *et al.* [4]. The most significant contributor to the predictive power of the payout yield is the new issuing yield when examining their accounting-based measures separately. Furthermore, the predictive power of new issuing yield largely comes from the two outliers of 1929 and 1930. In other words, the new issuing yield offers no explanatory power once the sample period starts from 1931 instead of 1926.

**An Alternative Approach to Construct the Repurchasing Yield.** The conventional approach of computing returns ignores changes in the market capitalization associated with changes in the total number of share outstanding. When the number of shares changes over time due to either repurchasing or seasonal offering, capital gains do not purely reflect growth potential. From an asset pricing perspective, it is more important to consider different components of returns from a representative investor's perspective. In other words, we can decompose returns from the stand point of a representative investor instead of a buy-and-hold investor. In particular, we can rewrite the return identity as the following:

$$R_{t+1} \equiv \frac{S_{t+1}D_{t+1}}{S_t P_t} + \frac{(S_t - S_{t+1})(P_{t+1} + D_{t+1})}{S_t P_t} + \frac{S_{t+1}P_{t+1}}{S_t P_t}$$
(24)

where *St* is the number of share outstanding at time *t*. Equation (24) can be interpreted in the following way:

- *first term*: dividend yield (*D/P*) for a representative shareholder;
- *second term*: net repurchasing yield (*F/P*) at the before ex-dividend day price; and
- *third term*: change in market capitalization, which reflects growth.

Using NYSE/AMEX/NASDAQ index returns, we can construct both the smoothed dividend yield (*D/P*) and the repurchasing yield (*F/P*) over the past 12 months. Table 7 reports the adjusted *R*2s for various predictive regressions.

For the whole sample period from 1952 to 2005, quarterly returns are more predicable than monthly returns. Overall, the repurchasing yield has higher predictive power than the dividend yield. When we split the sample into two, it becomes clear that the two predictors have played very different roles. Almost all the predictive power in the first half of the sample comes from the dividend yield, whereas majority predictive power in the second half of the sample is due to the repurchasing yield. This evidence is consistent with the observation of a decreasing trend in the dividend yield and the increasing role played by repurchases.

# **Statistical Issues**

The use of many predictors can be controversial. In many cases, the issue lies in the statistical inference due to the persistence in predictors. These issues include spurious regression, biased estimates due to correlations between innovations to predictors and stock returns, and error in variables when using imperfect predictors.

## *Spurious Regression*

When regressing one nonstationary random variable on another independent nonstationary random variable, we often observe a significant relationship between the two variables. This is because, in a finite sample, both variables are likely to be perceived trending. Spurious regression is first discussed by Granger and Newbold [21]. At a first glance, spurious regression may not seem to be likely for a predictive regression since stock returns on the left-hand side of a regression are not persistent at all. However, if we consider stock returns as containing a persistent expected return component, the predictive regression could be spurious [20]. This problem can even be more severe when researchers are mining for predictors because highly persistent series are more likely to be found significant in the search for predictors. Their simulation results suggest that many of the useful predictors found in the literature could be subject to this criticism.

### *Predictive Regression*

Owing to persistence in the predictors and a correlation between innovations to predictors and stock returns, Stambaugh [36] has suggested that both the coefficient estimate and the *t*-ratio in a predictive regression are biased. For example, when the current stock price is high, the current return will also be high, whereas the current dividend–price ratios will be low since the *D/P* ratio has a price in the denominator. Such an association implies a negative relationship between innovations to *D/P* ratios and innovations to returns. Such a negative correlation will couple with the typical downside bias in the persistence parameter estimate of the *D/P* ratio to make the predictive regression coefficient bias upward. More specifically, suppose that we have the following system:

$$r_{t+1} = \beta z_t + \epsilon_{t+1} \tag{25}$$

$$z_{t+1} = \psi z_t + u_{t+1} \tag{26}$$

where *zt* is the predictor. It can be shown [28] that

$$E(\hat{\beta} - \beta) = \gamma(\hat{\psi} - \psi) \tag{27}$$

where *γ* is from the regression of *t* = *γ ut* + *vt* . Since *γ* is negative in the case of dividend–price ratio and *ψ*ˆ is typically biased downward, equation (27) suggests that the beta estimate is biased upward. Therefore, Stambaugh concluded that the predictive power of dividend yield is exaggerated.

While Stambaugh's bias adjustment is based on the well-known bias result of *ψ*ˆ being −*(*1 + 3*ψ)/T* , Lewellen [28] observes that such a bias typically occurs in the data that appear to mean-revert more strongly than they truly do. However, predictors such as the dividend yield are hardly mean-reverting. They contain roots very close to unity. Instead, Lewellen [28] proposed to use *ψ* = 1 as the true value in equation (27) in order to derive a conservative adjustment. For example, using NYSE returns and log dividend–price ratio over the ample period from 1946 to 2000 in equation (25), the least-squares estimate of *β* is 0.92, with a standard error of 0.48. When applying Stambaugh [36] bias correction, the estimate becomes 0.20 with a one-sided *p*-value of 0.308. In contrast, using Lewellen's conservative bias adjustment, the estimate becomes 0.66 with a *t*-ratio of 4.67.

### *Implied Constraint*

To push the idea of incorporating prior knowledge as in Lewellen [28], Cochrane [12] argued that the coefficients from predictive regressions of returns, dividend growth, and dividend–price ratio using the lagged dividend–price ratio should be constrained. In particular, if we run the following regressions,

$$r_{t+1} = a_r + b_r(d_t - p_t) + \epsilon_{r,t+1} \quad (28)$$

$$\Delta d_{t+1} = a_d + b_d(d_t - p_t) + \epsilon_{d,t+1} \quad (29)$$

$$d_{t+1} - p_{t+1} = a_{dp} + \psi(d_t - p_t) + \epsilon_{dp, t+1} \tag{30}$$

the regression coefficients *br*, *bd* , and *ψ* should be related. In fact, by substituting equations (28) through (30) into equation (19), we have the following results:

$$b_r = 1 - \rho \psi + b_d \tag{31}$$

$$\epsilon_{r,t+1} = \epsilon_{d,t+1} - \epsilon_{dp,t+1} \tag{32}$$

Since *ρ <* 1 and *ψ <* 1, equation (31) implies that one cannot test the joint hypothesis of *br* = 0 and *bd* = 0 at the same time. In other words, if we fail to reject the hypothesis of *bd* = 0, we cannot ignore the evidence that *br* is positive in the predictive

|         |           |        |                  |    | Correlation |      |            |
|---------|-----------|--------|------------------|----|-------------|------|------------|
|         | Estimates | σ (b)ˆ | Implied<br>value |    | r           | d    | dp         |
| bˆr     | 0.097     | 0.050  | 0.101            | r  | 19.6        |      | 66.0 −70.0 |
| bˆ<br>d | 0.008     | 0.044  | 0.004            | d  | 66.0        | 14.0 | 7.5        |
| ψˆ      | 0.941     | 0.047  | 0.945            | dp | −70.0       | 7.5  | 15.3       |

**Table 8** The actual parameter estimates and the implied parameters; adopted from Cochrane [12]

regression of equation (28). As shown in Table 8 (adapted from [12]), the *b*ˆ *<sup>d</sup>* estimate is very close to zero with a large standard error. Therefore, *br* is probably close to 0*.*101 as implied by equation (31) using *ρ* = 0*.*9638, which is close to the actual estimate of 0*.*097.

At the same time, equation (32) suggests that shocks to returns and the dividend–price ratio are highly correlated with each other, which are indeed true from Table 8. For example, the negative correlation is as high as 70%. Table 8 also shows that the estimated coefficients *br*, *bd* , and *ψ* and their corresponding implied values from equation (31) are amazingly close.

## *Error in Variables*

If predictability is driven by time-varying expected returns, predictors should predict the expected return. In other words, the conventional predictive regression implicitly assumes that the expected return is a linear function of the predictors. However, from the small magnitude of predictability, it is clear that predictors can only be noisy estimates of the true expected returns. In other words, the predictive regressions are subject to error-in-variables problem, which will bias estimates. To overcome the problem, Pastor and Stambaugh [31] proposed to model the expected return as an unobservable component and to allow its innovation being correlated with innovations in predictors. Specifically, they propose the following model:

$$r_{t+1} = \mu_t + \epsilon_{t+1} \tag{33}$$

$$\mu_{t+1} = \mu_0 + \phi \mu_t + u_{t+1} \tag{34}$$

$$z_{t+1} = \psi z_t + v_{t+1} \tag{35}$$

where *µt* is the expected return and *zt* is the predictor. In this system, predictors affect the expected return through a correlation between *ut*<sup>+</sup><sup>1</sup> and *vt*+1. In other words, information in the predictors helps to improve the "quality" of the expected return estimates in the spirit of the classical SUR (seemingly unrelated) regression. Since the system of equations (33)– (35) can be reduced to a predictive regression when *µt* = *zt* , it should perform at least as good as the predictive regression. Additional constraints can be imposed to improve the estimation efficiency. For example, when there is a positive shock to the expected return, future expected returns will be high due to the persistence, which will result in a low price, or equivalently a low return. Therefore, we can incorporate this prior constraint of the negative correlation between *ut*<sup>+</sup><sup>1</sup> and *t*+1. Using quarterly data and imposed economic prior in a Bayesian framework, Pastor and Stambaugh [31] found that the dividend yield is a very useful predictor.

In Pastor and Stambaugh [31], a predictor affects the expected return through an indirect channel by improving the precision of the expected return estimate as in the same spirit of the SUR regression. To push the idea further, Baranchuk and Xu [3] studied both the direct and indirect effects of predictors on the expected return. In particular, equations (34) and (35) are replaced by

$$\mu_{t+1} = \mu_0 + \phi \mu_t + \delta m_t + u_{t+1} \tag{36}$$

$$z_{t+1} = m_t + \eta_{t+1} \tag{37}$$

$$m_{t+1} = \alpha m_t + v_{t+1} \tag{38}$$

where *mt* is the expected predictor. In this framework, the expected predictor directly affects the level of expected return, whereas the unexpected predictor continues to influence the efficiency of the timevarying expected return through its correlation with the innovation to the expected return. Using both the dividend yield and repurchasing yield, Baranchuk and Xu [3] were able to demonstrate the very different role played by the two predictors. The repurchasing yield affects the expected return directly, whereas dividend yield works through the indirect channel affecting the precision in the estimate of the expected return. From a technical perspective, such an elaborated model structure also avoids the potential spurious regression and possesses the ability to incorporate economic prior.

### *Out-of-sample Predictive Power*

If predictability is due to time-varying expected returns, a representative investor will not attempt to make abnormal returns since both his/her risk exposure and risk tolerance change over time. However, a nonrepresentative (isolated) investor might be able to take the advantage of return predictability in order to outperform the market. Goyal and Welch [37] have run a horse racing on the out-of-sample predictive power for a model based on unconditional forecast *versus* models with conditional forecast using different predictors including the following:

- the dividend–price ratio and the dividend yield [10];
- the earnings price ratio and dividend–earnings (payout) ratio [26];
- the short-term interest rate [7];
- the term spread and the default spread [7, 16, 23];
- the inflation rate [14, 18];
- the book-to-market ratio [25, 32];
- the consumption, wealth, and income ratio [27]; and
- the aggregate net issuing activity [2].

After comparing the (conditional) root-mean-squared errors (RMSEs) with respect to the predicted returns to the (unconditional) RMSEs using a simple sample mean, Goyal and Welch [37] concluded that in-sample predictability can be very different from out-of-sample performance. In most cases, the unconditional RMSEs are smaller than the conditional RMSEs. Therefore, they believe that most results from predictive regressions are just statistical illusions.

Similar to the idea of using prior information to improve the predictive power for future returns as in [12], prior economic constraints are valuable information and should be used simultaneously. Campbell and Yogo [11] recognized that if we are really predicting the expected returns in a predictive regression, we should throw out the negative predicted returns since the expected returns should always be positive. By constraining the predicted returns to be nonnegative, Campbell and Yogo [11] found that most predictors in the above list are indeed useful in predicting future returns even out of sample.

In a related study, Xu [38] recognized that, given the low *R*2s in predictive regressions, it is very difficult to provide accurate prediction about the *magnitude* of future returns due to errors in the parameter estimates. One has to at least estimate two parameters in a predictive regression, while a sample mean corresponds to only one parameter estimate. The additional estimation error could easily overwhelm the benefit of using predictors. Therefore, in out-of-sample studies, a more useful question to ask is whether we are able to predict the *direction* of future market movement. On the basis of this idea, Xu [38] had studied the economic significance of the following trading strategy:

*Trading strategy:* Invest in a risky asset today only if the predicted future asset return is positive.

Under the *t*-distributed return assumption, there exists a moderate condition, under which the trading strategy will outperform a buy-and-hold strategy. Using inflation, relative interest rate, and dividend–price ratio as predictors, Xu [38] had shown that such a trading strategy could potentially double the performance of a buy-and-hold strategy over the sample period from 1952 to 1998.

# **Concluding Comments**

Given the vast literature on predictability, in this article attention was focused on the questions of the existence of predictability and the interpretation of predictability. Return predictability has always been a challenge to the EMH. The traditional view on the evidence is either denying the evidence with the help of statistical methods or attributing the phenomenon to market frictions. For example, most predictors, except for the past returns, are persistent. Such a statistical property may result in a spurious regression. Predictors are also imperfect, which will bring in an error-in-variables problem in estimation. Many market microstructure effects, such as bid–ask bounce and nonsynchronous trading, may induce autocorrelation in a short-run and among small stocks. The modern view, however, takes a more positive approach by recognizing the time-varying risk premium due to changes in either investment opportunities or investors' risk tolerance. If this is indeed the case, many variables that predict business cycles should also help to predict returns, for example, the interest rate. Other variables that contain a price component can also predict returns because prices reflect expectations and should summarize all future changes in the expected return or CF distributions.

Many statistical issues can be dealt with a more elaborated model structure and the use of economic prior. For example, if predictability is due to changes in the risk premium, we can model the expected returns explicitly as following an *AR(*1*)* process and impose the nonnegativity constraint. We can also alleviate the market microstructure effects by using low-frequency returns such as monthly or quarterly returns. From an empirical perspective, however, we should not expect to find huge return predictability. It seems to be odd that some economic agents do not try to explore economic profits, even though they are not subject to the kind of risks that a representative investor might expose to. Indeed, many studies tend to find economically weak but statistically significant evidence of predictability.

Overall, we believe that the evidence points to the direction of predictable returns even under careful statistical inference. If this is the case, will evidence on predictability have any implications on asset pricing? The answer is yes as evident from the literature on testing the conditional asset pricing models. Predictability also has implications on investors' asset allocation decisions [22]. If returns are positively correlated over time, investors might want to allocate less wealth to equity. This is because a risk averse investor understands that he/she will be subject to even larger downside risk if today's return is low. This is still an active area of research.

# **End Notes**

a*.* Suppose returns follow the following *AR(*1*)* process,

$$r_t - \mu = \theta(r_{t-1} - \mu) + \epsilon_t$$

the true Sharpe ratio defined as *µ/σ* can be expressed as

$$\frac{\mu}{\sigma_{\epsilon}} = \frac{1}{\sqrt{1 - \theta^2}} \frac{\mu}{\sigma_y}$$

b*.* When the discount rate is not zero, we can define a discounted process such that it is a martingale.

c*.* The positive autocorrelation in the equal-weighted index shown in Table 1 is also consistent with the nonsynchronous trading story.

d*.* Since holdings in the future contracts are much smaller than the market capitalization of the 500 largest companies, the evidence could be consistent with our argument that the representative investors will not try to trade on the predictability, while nonrepresentative investor in a segment of the market could.

# **References**

- [1] Ang, A. & Bekaert, G. (2007). Stock return predictability: is it there? *Review of Financial Studies* **20**, 651–707.
- [2] Baker, M. & Wurgler, J. (2000). The equity share in new issues and aggregate stock returns, *Journal of Finance* **55**, 2219–2257.
- [3] Baranchuk, N. & Xu, Y. (2007). *What Predicts Stock Returns?—The Role of Expected versus Unexpected Predictors*. working paper, University of Texas at Dallas.
- [4] Boudoukh, J., Michaely, R., Richardson, M.P. & Roberts, M.R. (2007). On the importance of measuring payout yield: implications for empirical asset pricing, *Journal of Finance* **62**, 877–915.
- [5] Boudoukh, J., Richardson, M.P. & Whitelaw, R.F. (1994). Tale of three schools: insights on autocorrelations of short-horizon stock returns, *Review of Financial Studies* **7**, 539–573.
- [6] Boudoukh, J., Richardson, M. & Whitelaw, R.F. (2008). The myth of long-horizon predictability, *Review of Financial Studies* **21**, 1533–1575.
- [7] Campbell, J.Y. (1987). Stock returns and term structure, *Journal of Financial Economics* **18**, 373–399.
- [8] Campbell, J.Y. (1991). A variance decomposition for stock returns, *Economic Journal* **101**, 157–179.
- [9] Campbell, J.Y., Lo, A.W. & MacKinlay, C.A. (1997). *The Econometrics of Financial Markets*, Princeton University Press, Princeton.
- [10] Campbell, J.Y. & Shiller, R. (1988). Stock prices, earnings, and expected dividends, *Journal of Finance* **43**, 661–676.
- [11] Campbell, J.Y. & Yogo, M. (2006). Efficient tests of stock return predictability, *Journal of Financial Economics* **81**, 27–60.
- [12] Cochrane, J.H. (2008). The dog that did not bark: a defense of return predictability, *Review of Financial Studies* **21**, 1533–1575.
- [13] Conrad, J. & Kaul, G. (1988). Time-variation in expected returns, *The Journal of Business* **61**, 409–425.
- [14] Fama, E. (1981). Stock returns, real activity, inflation, and money, *American Economic Review* **71**, 545–565.
- [15] Fama, E. & French, K. (1988). Permanent and temporary components of stock prices, *Journal of Finance* **96**, 246–273.
- [16] Fama, E. & French, K. (1989). Business conditions and expected returns on stock and bonds, *Journal of Financial Economics* **25**, 23–49.
- [17] Fama, E. & French, K. (1996). Multifactor explanations of asset pricing anomalies, *Journal of Finance* **51**, 55–84.
- [18] Fama, E. & Schwert, G.W. (1977). Asset returns and inflation, *Journal of Financial Economics* **5**, 115–146.
- [19] Ferson, W.E. & Harvey, C.R. (1991). The variation of economic risk premiums, *Journal of Political Economy* **99**, 385–415.
# Roll Model

In his 1984 article entitled "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market", Roll [4] developed a model that made it possible to measure an estimate of the bid-ask spread. This estimate depended only on the firstorder serial covariance of price changes over time. As one of the first theoretical models to estimate the bid-ask spread, Roll's model has served as a strong foundation upon which many future expansions and improvements have emerged to estimate the spread and its determinants.

#### **Bid-Ask Bounce**

One of the key concepts considered in the development of the Roll model is the idea of a "bid-ask bounce". When a trade is undertaken by a market maker, it is generally executed at a price different from the actual market value of the asset. Instead a trader's purchase from the market maker will be completed at the market maker's ask price, while a sale to a market maker will be completed at the market maker's bid price. The difference between the ask and the bid prices is referred to as the *spread*.

To estimate the bid-ask spread using the observed transaction prices, Roll assumed that the probability that the next transaction is a buy is equal to the probability of it being a sell. If the market maker's previous transaction was a purchase at the bid price, then there is an equal probability that the next transaction will be executed at either the bid or the ask. The same logic holds if the market maker's previous transaction were to be a sale to a customer at the ask price. For example, assume that the market maker's trade at time  $t-1$  was executed at the ask price, then there is an equal probability that the next trade at time  $t$  will be at the bid or the ask. If at time  $t$ , the trade is again at the ask, then the change in price is zero. However, if it is at the bid, then the change in price is equal to the spread " $-s$ " (Figure 1), where  $s$  is the difference between the bid and the ask prices.

Figure 1 shows the possible sequence of trades given that a trade at time  $t - 1$  takes place at the ask price. The fundamental value of the asset,  $P^*$ , is at the midpoint between the bid and the ask prices and it follows a random walk.  $P_t^* = P_{t-1}^* + \tilde{\eta}_t$ , where  $\tilde{\eta}_t$ is white noise such that

a

$$E[\eta_t] = 0, \text{Var}[\tilde{\eta}_t] = \sigma^2$$
  
and  $E[\tilde{\eta}_t \tilde{\eta}_{t-s}] = 0 \quad \forall t \neq s$  (1)

Given Roll's assumption that it is equally likely for the next trade to be at the bid or the ask, the probabilities associated with successive price changes are given in Table 1. The probabilities are based on the observation that there are a total of eight paths from  $t-1$  to  $t+1$ , starting from either the ask or the bid prices. Therefore, each path has a probability of 1/8. Each path is associated with joint price changes of  $\Delta P_t$  (where  $\Delta P_t = P_t - P_{t-1}$ ) and  $\Delta P_{t+1}$  that is a combination of  $0$ ,  $s$ , and  $-s$ . For example, there is only one path for  $\Delta P_t = 0$  and  $\Delta P_{t+1} =$  $-s$  starting from the ask price at  $t-1$ . Hence, the probability of this joint event is  $1/8$ . Similarly, we can find the probabilities for each combination of price changes.

On the basis of Table 1, the serial covariance of price changes  $SCov(\Delta P_t, \Delta P_{t+1})$  is  $-s^2/4$  and  $s = 2\sqrt{-S\text{Cov}(\Delta P_t, \Delta P_{t+1})}$ . With this equation, an estimate of the spread can be obtained based on the estimate for the serial covariance of successive price changes. The standard serial covariance estimator used is the mean cross product:  $\widehat{\text{SCov}} =$  $\frac{1}{n}\sum_{t=1}^{n}\Delta P_{t}\Delta P_{t+1}-\overline{\Delta P}^{2}$ , where  $\overline{\Delta P}$  is the sample mean of  $P_t$ . Initially, Roll's model was developed to estimate bid-ask spread from transaction prices. However, there are some drawbacks to its practical use. Some of the model's assumptions are very specific and may not carry over to real-life application. For example, the Roll estimator is based on the assumption that the stock's fundamental value follows a random walk and that there is an equal probability that the next trade will be a buy or sell. Hence, the probability of a future trade at the ask or the bid prices is independent of the prior trade direction. However, there is some evidence that the probability of a trade continuation might be different from a trade reversal. The model also assumes that the spread is entirely due to order processing costs and does not include adverse selection or inventory costs, implying that  $\Delta P_t$  is independent of whether the transaction at time  $t$  is at the bid or the ask. Harris [2] provided a detailed analysis of the small sample properties of the Roll serial covariance estimator

![](_page_1_Figure_1.jpeg)

**Figure 1** Possible sequence of trades given that the trade at time  $t-1$  takes place at the ask price (based on Roll [4])

**Table 1** Joint price change distribution for  $\Delta P_t$  and  $\Delta P_{t+1}$  (based on Roll [4])

|                  |      | $\Delta P_t$ |     |      |
|------------------|------|--------------|-----|------|
|                  |      | $+s$         | 0   | $-s$ |
| $\Delta P_{t+1}$ | $+s$ | 0            | 1/8 | 1/8  |
|                  | 0    | 1/8          | 1/4 | 1/8  |
|                  | $-s$ | 1/8          | 1/8 | 0    |

for the bid-ask spread. He concluded that the serial covariance estimator is very noisy in daily data and is biased downward in small samples. Using weekly data would reduce the bias, but it will also lead to smaller sample sizes. He also found that the bias from Jensen's inequality is very serious in daily and weekly data.

## **Bid-Ask Spread-induced Bias in Volatility** Estimator

Stock return volatility estimates based on transaction prices will lead to an upward bias due to the bid-ask bounce. The transaction price,  $P_t$ , consists of the unobserved "true" price  $P_t^*$ , and the half-spread,  $+\frac{s}{2}$ if the transaction was at the ask price and  $-\frac{s}{2}$  if the transaction was at the bid price. Therefore,  $\bar{P}_t$  $P_t^* + \frac{s}{2} \tilde{D}_t$ , where  $\tilde{D}_t$  is the buy/sell indicator, which is equal to 1 with probability 0.5 (buyer-initiated trade) and equal to  $-1$  with probability 0.5 (sellerinitiated trade).

If we assume that  $P_t^*$  evolves as a random walk, such that  $P_t^* = P_{t-1}^* + \tilde{\eta}_t$ , then the variance of the price change based on transaction prices can be written as

$$\operatorname{Var}(\Delta P_{t}) = \operatorname{Var}(\tilde{\eta}_{t}) + \operatorname{Var}\left(\frac{s}{2}\Delta\tilde{D}_{t}\right)$$
$$= \sigma^{2} + \frac{s^{2}}{4}\operatorname{Var}(\Delta\tilde{D}_{t}) = \sigma^{2} + \frac{s^{2}}{2} \quad (2)$$

where  $\Delta P_t = P_t - P_{t-1}$  and  $\Delta \tilde{D}_t = \tilde{D}_t - \tilde{D}_{t-1}$ .

Since the variance calculated using transaction prices will include both the variance from the bid-ask bounce as well as the actual price variance, the calculated variance will overstate the fundamental volatility by  $\frac{s}{2}$ .

The magnitude of the bid-ask bounce-induced volatility remains the same whether we look at short-interval (high-frequency) or long-interval (lowfrequency) returns. However, volatility due to the bid-ask bounce becomes a larger proportion of the fundamental return volatility with a decrease in the return horizon. French and Roll [1] provided a variance estimator that is unbiased but noisy.

## A Generalized Roll Model with Adverse Selection

Since the publication of Roll's paper in 1984, there have been many related papers that relax some of the assumptions made by Roll, and others have used Roll's model as a foundation to develop general models to include asymmetric information, inventory costs, price discreteness, and other microstructure related effects. We can generalize the Roll model to include the adverse selection cost as follows.

The unobserved fundamental value  $P_t^*$  is given as

$$P_t^* = P_{t-1}^* + \tilde{\eta}_t + (1 - \pi) \left(\frac{s}{2}\tilde{D}_t\right) \tag{3}$$

where  $(1 - \pi)$  is the fraction of the half-spread due to adverse selection and  $\tilde{\eta}_t$  is a serially uncorrelated public information shock. If the fraction of the half-spread due to order processing is  $\pi$ , then the transaction price is given as

$$P_t = P_t^* + \pi \left(\frac{s}{2}\tilde{D}_t\right) \tag{4}$$

If  $\pi$  is set to equal 1, we get back to the original Roll model. Under this model, it can be shown that  $\text{SCov}(\Delta P_t, \Delta P_{t-1}) = -\pi \frac{s^2}{4}$ . Hence, only when  $\pi = 1$  (i.e., no adverse selection) can we obtain an unbiased estimator of "s" using the  $SCov(\Delta P_t, \Delta P_{t-1})$  as in [4]. A more detailed description of a generalized Roll model can be found in [3].

## Summary

Roll's 1984 article developed a relatively simple model to estimate the bid-ask spread based on observable trade prices. This model has been very useful in situations where direct bid-ask data were not available. The Roll model has been a foundation upon which several extensions and other models have emerged to estimate the spread and its determinants.

#### References

- [1] French, K.R. & Roll, R. (1986). Stock return variances: the arrival of information and reaction of traders, Journal of Financial Economics 17, 5–26.
- Harris, L. (1990). Statistical properties of the roll serial [2] covariance bid/ask spread estimator, Journal of Finance XLV(2), 579-590.
- [3] Hasbrouck, J. (2007). Empirical Market Microstructure, Oxford University Press.
- Roll, R. (1984). A simple implicit measure of the effective [4] bid-ask spread in an efficient market. *Journal of Finance* 39, 1127–1139.

### **Related Articles**

Adverse Selection; Bid-Ask Spreads; Glosten-Milgrom Models; High-frequency Data; Market Microstructure Effects.

MAHENDRARAJAH NIMALENDRAN
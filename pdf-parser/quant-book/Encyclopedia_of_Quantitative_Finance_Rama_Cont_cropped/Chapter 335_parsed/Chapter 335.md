# **Intraday Price Efficiency**

The efficient price of a security represents the present value of expected future cash flows conditional on current information. Although observed prices are estimates of this quantity, deviations can and will occur. Price efficiency measures summarize the extent of these deviations. The measures presented here focus on deviations that arise and are subsequently corrected over very short horizons within the day, and they facilitate comparisons through time as well as across securities and markets. As these measures are intended to evaluate the closeness of actual prices to efficient prices, they relate to transaction costs and describe an important dimension of overall market quality.

# **Measures<sup>a</sup>**

Measures of intraday price efficiency, either explicitly or implicitly, define the efficient price for a security as a random walk. New information may arrive continuously, and deviations from the random-walk benchmark can be considered to be inefficiencies. These inefficiencies arise from a variety of sources including discreteness, inventory control, and other non-information-based components of the bid–ask spread. In principle, inefficiencies could also arise from irrationality among market participants (e.g., overreacting to the size of a trade).

Hasbrouck [9] uses variance decomposition methodologies to assess inefficiencies. He defines the (log) transaction price, *pt* , as the sum of a random-walk component (the efficient price) *mt* , and a transitory, mean-zero pricing error, *st* , where *t* indexes transaction time:

$$p_t = m_t + s_t \tag{1}$$

The efficient price is unobservable and its innovations are new public information as well as the information content of order flow. Because the pricing error has a mean of zero, its standard deviation, *σs*, is a measure of its magnitude. Intuitively, *σs* summarizes how closely transaction prices follow the efficient price over time and serves as an inverse measure of price efficiency.

Hasbrouck proposes a general structure for the pricing error, where *st* is related to information in trades, non-trade-related public information, and a disturbance. To connect this model with the data, he uses a vector autoregression (VAR) system over {*rt, xt*}, where *rt* is the first difference of *pt* and *x<sup>t</sup>* is a vector of trading variables. This model is underidentified, so additional restrictions from the variance decomposition literature must be imposed. Specifically, the restriction of [1] effectively relates *st* only to the trading information contained in *x<sup>t</sup>* , and the vector moving average representation is used to estimate *σs*. Because of the restriction, the estimated pricing error is a lower bound. Factors that would cause *σs* to exceed this quantity must be uncorrelated with lagged returns as well as the set of trade variables.

There is no formal model describing the conditioning information in *xt* , but it should be constructed to explain meaningful variation in the true pricing error. Hasbrouck uses a 3 × 1 vector of the following trade variables: (i) a trade sign indicator, (ii) signed trading volume, and (iii) the signed square root of trading volume. This structure of *xt* allows for a nonlinear relationship between pricing error and the trade series. For some perspective, Hasbrouck uses a sample of NYSE stocks from 1989 to demonstrate that this specification increases the estimate for *σs* by about 40% over that from a simple univariate estimation of equation (1); the added explanatory power of the *xt* strengthens the lower bound and provides a more accurate estimate of *σs*.

In addition to the structure of *x<sup>t</sup>* , numerous methodological considerations arise. First, the VAR system must be truncated at some lag length beyond which serial dependencies are assumed negligible. There is no theoretical guidance for this decision, but one could determine a cutoff point *ad hoc* by inspecting VAR estimates over various lags. Second, trading information in *x<sup>t</sup>* will typically require the signing of trades. A common method compares prices to midpoint quotes [15]. Third, overnight returns are considered atypical due to the time delay as well as different trading mechanisms at the opening and therefore may be neglected in the analysis.

A number of empirical studies have used some variant of Hasbrouck's methodology in recent years. Kumar *et al.* [14] find that pricing errors decline for equities upon option listings. George and Hwang [6] extend the model to allow for heteroskedasticity in *st* , and they find that the pricing errors are similar at the opening and close of trading. Hotchkiss and Ronen [12] show that the price efficiency of bonds resembles that of the underlying stocks. Boehmer *et al.* [3] find that the price efficiency of NYSE stocks improved in 2002 when the contents of the limit order book were made available to traders off the exchange. Finally, Boehmer and Kelley [2] find that pricing errors decline with more institutional ownership and trading.

As an alternative to the variance decompositions, one may also measure intraday efficiency using the autocorrelation properties of the return series. Consider once again an efficient price that, by definition, follows a random walk. For a simple implementation, one can construct a series of price changes over fixed increments in time (say, 30 min) and estimate the autocorrelation. Since either positive or negative autocorrelation is a deviation from a random walk, a summary (inverse) efficiency measure is the absolute value of the autocorrelation.

A slightly more complex implementation involves variance ratios. *VR*(*n, m*) is the ratio of an *m*-period variance to an *n*-period variance, where both variances are scaled by the number of periods. For example, *VR*(5 min, 60 min) is the ratio of a 60-min return variance to a 5-min return variance, scaled by 60 and 5, respectively. Under a random walk, variance ratios will equal 1, so the summary (inverse) efficiency measure is |1 − *V R(n, m)*|. A variance ratio contains more information than a single autocorrelation, as *VR*(*n, m*) can be written as a linear combination of the first *n* − 1 autocorrelations (see [4], p. 49).

The use of autocorrelations or variance ratios also requires some methodological consideration. Most importantly, and in contrast to Hasbrouck's methodology, one needs to remove the bid–ask bounce described in [17]. The best way to do this is by computing returns according to bid–ask midpoints. In addition, for some securities, stale quotes may be a problem. One may mitigate stale quote issues by ignoring intervals over which no new quote was posted.

As a summary measure of price efficiency, the Hasbrouck approach is favorable for a couple of reasons. First, the variance decomposition methods differentiate between permanent and transient price changes and attribute deviations from a random walk to the latter alone. Nonzero autocorrelation, and hence variance ratios deviating from unity, can arise from either efficient or inefficient pricing. For example, order splitting by informed traders may lead to positive autocorrelation. Second, pricing errors are measured in trade time—the model is advanced by one period after each trade—whereas autocorrelations and variance ratios are based on returns computed in clock time. Measuring efficiency in trade time has the added benefit of granting more weight to periods of active information discovery. Moreover, the trade-time measure reflects the actual behavior of market participants and includes the information conveyed by each single trade.

It is also important to recognize that neither the variance decompositions nor the autocorrelationbased measures will pick up deviations from the efficient price persisting for more than a brief portion of the trading day, not to mention weeks or months. That is, only pricing errors that are quickly corrected will be measured. This approach ignores potential deviations from fundamentals in contexts such as long-term reversals as in [5], return momentum as in [13], or weekly return reversals as in [16].

Boehmer and Kelley [2] have estimated a variety of price-efficiency measures for all NYSE stocks for each quarter from 1983 to 2004. Figure 1 tracks the cross-sectional average for *σs* normalized by *σp* from equation (1) over the 22-year period. For comparison, the cross-sectional average of the absolute value of the first-order autocorrelation for a series of 30-min quote midpoint returns is also shown. Autocorrelations and variance ratios incorporating various other intraday horizons produce a similar picture. Both plots illustrate a general decline through time, which is interpreted as an overall *increase* in price efficiency. This matches a similar trend in other transactions costs such as execution costs. More importantly, an inspection of the plots reveals that both measures increase around the market crash of 1987, but there is a substantial drop in *σs* alone around the 16th pricing in 1997 and on decimalization in 2001—events that intuitively should lead to greater efficiency. Turning to the cross section, unreported tests show that the average cross-sectional correlation between the two measures is around 0.25, and that both measures generally decrease with firm size, execution costs, price, and trading activity.

# **The Evolution of the Efficient Price**

While this article focuses on the extent to which transaction prices resemble an efficient price, similar

![](_page_2_Figure_1.jpeg)

**Figure 1** Average price efficiency through time. The sample is based on NYSE-listed securities between 1983 and 2004. The solid line tracks the cross-sectional mean of *σs*/*σp*, which is the pricing error from Hasbrouck [9] divided by the standard deviation of transaction prices. The dashed line tracks the cross-sectional mean of |AC30|, which is the absoluted value of the 30-min return autocorrelation. The left and right vertical axes are for *σs*/*σp* and |AC30|, respectively

estimation techniques describe the evolution of the underlying efficient price itself.b Specifically, Hasbrouck [7, 8] starts with equation (1) and considers a VAR over returns and trades. In this case, however, prices and returns are based on quote midpoints (rather than transaction prices) and the trade at time *t* precedes the quote change indexed by *t*. Thus, the quote change at time *t* reflects information in the trade, but not *vice versa*. Hasbrouck [7] uses the impulse response function as a measure of the information content of a trade innovation. He also [8] uses variance decompositions similar to the ones used by him in [9] to develop two *summary measures* of trade informativeness. The first is the component of the random-walk variance attributable to trades, which serves as an absolute measure of the private information revealed by trading. The second is the first measure scaled by the total random-walk variance. It is interpreted as the importance of trade-based information relative to all public information for price discovery. These measures are superior to other metrics such as the quoted spread or the permanent price impact (as in [7]), which condition on trade size. Finally, Hasbrouck [10] provides a multiple market extension to assess the relative price discovery for each market in which a security trades. Here, there is a single random-walk efficient price and each market's information share is defined as the proportion of the random-walk variance attributable to its trades.

# **Summary**

Intraday price efficiency can be measured using variance decomposition methods or by various autocorrelation-based measures. Because they explicitly characterize price changes as permanent or temporary, and they employ useful transaction-time models, variance decomposition methods are preferred. Several studies using these measures are also described.

# **End Notes**

a*.* Much of this section is adapted from the discussion in [2]. b*.* See [11] for a survey.

# **References**

- [1] Beveridge, S. & Nelson, C. (1981). A new approach to the decomposition of economic time series into permanent and transitory components with particular attention to the measurement of the 'business cycle', *Journal of Monetary Economics* **7**, 151–174.
- [2] Boehmer, E. & Kelley, E. (2009). Institutional investors and the informational efficiency of prices, *Review of Financial Studies* **22**, 3563–3594.
- [3] Boehmer, E., Saar, G. & Yu, L. (2005). Lifting the veil: an analysis of pre-trade transparency at the NYSE, *Journal of Finance* **60**, 783–815.
- [4] Campbell, J.Y., Lo, A.W. & MacKinlay, A.C. (1997). *The Econometrics of Financial Markets*, Princeton University Press, Princeton, NJ.
- [5] DeBondt, W.F.M. & Thaler, R. (1985). Does the stock market overreact? *Journal of Finance* **40**, 793–805.
- [6] George, T. & Hwang, C. (2001). Information flow and pricing errors: a unified approach to estimation and testing, *Review of Financial Studies* **14**, 979–1020.
- [7] Hasbrouck, J. (1991). Measuring the information content of stock trades, *Journal of Finance* **46**, 179–207.
- [8] Hasbrouck, J. (1991). The summary informativeness of stock trades: an econometric analysis, *Review of Financial Studies* **4**, 571–595.
- [9] Hasbrouck, J. (1993). Assessing the quality of a security market: a new approach to transaction-cost measurement, *Review of Financial Studies* **6**, 191–212.
- [10] Hasbrouck, J. (1995). One security, many markets: determining the contributions to price discovery, *Journal of Finance* **50**, 1175–1199.

- [11] Hasbrouck, J. (2002). Stalking the "efficient price" in market microstructure specifications: an overview, *Journal of Financial Markets* **5**, 329–339.
- [12] Hotchkiss, E. & Ronen, T. (2002). The informational efficiency of the corporate bond market: an intraday analysis, *Review of Financial Studies* **15**, 1325–1354.
- [13] Jegadeesh, N. & Titman, S. (1993). Returns to buying winners and selling losers: implications for stock market efficiency, *Journal of Finance* **48**, 65–91.
- [14] Kumar, R., Sarin, A. & Shastri, K. (1998). The impact of options trading on the market quality of underlying securities: an empirical analysis, *Journal of Finance* **53**, 717–732.
- [15] Lee, C.M.C. & Ready, M. (1991). Inferring trade direction from intraday data, *Journal of Finance* **46**, 733–746.
- [16] Lehmann, B.N. (1990). Fads, martingales, and market efficiency, *Quarterly Journal of Economics* **105**, 1–28.
- [17] Roll, R. (1984). A simple implicit measure of the effective bid-ask spread in an efficient market, *Journal of Finance* **39**, 1127–1139.

# **Related Articles**

**Bid–Ask Spreads**; **Efficient Market Hypothesis**; **High-frequency Data**; **Liquidity**; **Price Impact**; **Roll Model**.

ERIC K. KELLEY
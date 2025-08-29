![](_page_0_Picture_1.jpeg)

Portfolio trading is not just about multi-tasking. Significant risk reductions can be achieved by tracking and managing portfolio risk.

# 12.1 Introduction

Portfolio trading provides investors with a cost-effective means of trading whole baskets of assets. This may be used to convert new cash flows, liquidate existing positions, or a combination of the two for portfolio rebalances. It may even be used to assist the transition of entire investment portfolios, also known as transition management.

Just as with single asset trading, portfolios are traded on either an agency or principal basis. Agency trades may simply be worked on "best efforts", or target benchmarks such as the VWAP or daily close. Principal trades are agreed for a specific strike time, at which point a snapshot of all the asset prices is taken. Quotes may be obtained from a number of brokers, although information leakage is obviously a key concern. Hence, trading may also be performed blind, in which case the broker is just given a description of the portfolio. This offers only an approximate value, number of assets, and factors such as weightings for the countries, indices and/or sectors. Clearly, with such blind trades the broker/s will tend to quote more conservatively to protect themselves from the additional uncertainty.

There are some hybrid trading types as well, namely incentive agency and guaranteed benchmark trades. An incentive agency trade means the broker's commission depends on the performance relative to the benchmark, whilst a guaranteed benchmark trade enforces a strict target that the broker must meet.

Portfolio trading is also an important tool for risk control and efficiency. Most brokers provide comprehensive pre-trade and real-time trading analytics, which allow investors to more precisely assess the impact of trading. This information may also be useful for their hedging strategies. Detailed post-trade analytics allow accurate performance measurement. The high level of automation associated with portfolio trading also enables the streamlining of post-trade allocation and settlement.

One of the key considerations when trading baskets of assets is portfolio risk. So we will start this chapter by reviewing this in more detail. Then after seeing how transaction cost analytics may be applied, we shall focus on optimal portfolio trading strategies. This includes techniques such as hedging and determining the optimal portfolio makeup. Finally, we will consider a how best to apply trading algorithms for executing portfolio trades.

# 12.2 Portfolio risk

A portfolio's return is the weighted sum of the returns for its constituent assets. So the associated portfolio's volatility is the standard deviation of these returns. Portfolio risk is somewhat harder to define. For the purposes of this book, we shall assume that this may be defined in terms of the portfolio volatility  $(\sigma_n)$  and an error term  $(\varepsilon)$ :

$$\textit{Portfolio risk} = \sigma_p + \varepsilon \tag{12-1}$$

The error term reflects the uncertainty associated with any risk estimates. Given that portfolio volatility forms the basis for this risk, the two terms are often used interchangeably.

Another important concept closely linked to portfolio risk is diversification. This is a significant risk reduction that occurs when the individual risks in the portfolio offset one another. Diversification helps to reduce the overall volatility of a portfolio's value, and so ensure a more consistent performance. Often this may be achieved simply by increasing the number of assets in the portfolio. For example, Figure 12-1 shows a plot of risk for portfolios of various sizes.

![](_page_1_Figure_6.jpeg)

Figure 12-1 A comparison of risk between various sizes of portfolio

A study of stock portfolios by Burton Malkiel (2004) confirmed this effect. Although he found that the risk reduction soon became negligible once portfolios were larger than 15 stocks (equivalent to the point  $N$  in Figure 12-1). The key to achieving diversification is to group together assets that are uncorrelated. This means that price rises/drops will not affect all the assets in the portfolio uniformly. Thus, Malkiel (2004) found that portfolios containing international stocks had much lower risk than those concentrated on U.S. stocks.

#### Portfolio volatility

The relationship between portfolio volatility and that of its constituent assets is actually nonlinear. So unlike the returns we cannot just determine it from the weighted sum of each asset's volatility. This was first pointed out by Harry Markowitz (1952) in his landmark paper "Portfolio Selection". He noted that each constituent's contribution to the overall

portfolio risk depends on three key factors:

- its proportion/weight in the portfolio
- the variance of its returns  $\bullet$
- the covariance of its returns with all other assets in the portfolio ٠

Covariance is a measure of how much two variables vary together.  $1$ Therefore, the portfolio volatility  $(\sigma_{\rho})$  may be defined as:

$$\sigma_p = \sqrt{\sum_{i=1}^n \omega_i^2 Var(r_i) + \sum_{i \neq j} \omega_i \omega_j Cov(r_i, r_j)}$$
(12-2)

where  $r_i$  is the return for constituent asset i and  $Var(r_i)$  is its variance,  $\omega_i$  and  $\omega_i$  represent the weights of specific assets i and j and  $Cov(r_i, r_i)$  is the covariance between their returns. Note that the covariance of a variable with itself equals its variance. We can further simplify equation 12-2 to:

$$\sigma_p = \sqrt{\sum_{j=1}^n \sum_{i=1}^n \omega_i \, \omega_j \, Cov(r_i, r_j)} \tag{12-3}$$

The overall volatility  $(\sigma_n)$  of a simple portfolio with two equally weighted assets, which have corresponding volatilities  $\sigma_1$  and  $\sigma_2$ , may be determined as:

$$\sigma_p = \sqrt{(0.5 \cdot \sigma_1)^2 + (0.5 \cdot \sigma_2)^2 + 2 \cdot (0.5 \cdot 0.5) \cdot Cov(\mathbf{l}, 2)}$$
(12-4)

**Example 12-1:** Let's examine the risk for a range of portfolios based on different compositions of two sample assets. Asset EFG has a volatility of 40% whilst HIJ has one of  $25\%$ . The covariance between these assets is 0.05.

So a portfolio that is 100% EFG will have 40% volatility, whilst one based solely on HIJ will have 25%.

Based on equation 12-4 a portfolio with  $50\%$  of each stock has a volatility of:

$$\sigma_p = \sqrt{(0.5 * 0.40)^2 + (0.5 * 0.25)^2 + 2 * (0.5 * 0.5) * 0.05} = 28\%$$

In comparison, the weighted sum of asset volatilities is  $32.5\%$ .

This lower volatility is due to the low covariance between the two assets. In other words, the overall risk is reduced because they are not perfectly correlated. If we plot the actual portfolio risk for all the potential mixes, we get the curve shown in Figure 12-2. Based on this, the lowest portfolio volatility of 24.74% may be achieved for a basket comprising of about 10% EFG and 90% HIJ.

 $1$  A positive covariance between two variables means they behave similarly, so if one is higher than expected then it is likely the other one will be as well. Conversely, a negative covariance means that they behave in opposite fashions, so a high value for one implies a lower expected value for the other. A covariance of zero shows that the items are completely independent, so no inference may be made from either value. For more details on calculating covariance see Addendum A at the end of this chapter.

![](_page_3_Figure_1.jpeg)

Figure 12-2 Portfolio risk for a range of portfolio compositions

The dotted line shown in Figure 12-2 marks the weighted averages for each portfolio composition. It corresponds to the risk that would be achieved if the two were 100% correlated.

The strength of the relationship between these two assets' returns may be quantified using a correlation coefficient ( $\rho$ ). Essentially, this is their covariance divided by the product of their standard deviations, as outlined in Addendum A at the end of this chapter.

Using equation 12-9, we can determine the actual correlation  $(\rho)$  between these assets:

$$\rho_{i,j} = \frac{Cov(I,J)}{\sigma_i \sigma_j} = \frac{0.05}{0.40 \times 0.25} = 50\%$$

Example 12-1 highlights the fact that the overall portfolio risk may be less than or equal to the weighted sum of the individual asset risks, and that this is largely due to the correlation between them. For instance, if the correlation between EFG and HIJ was zero the portfolio risk could be further reduced to around 20%.

Clearly, portfolios usually have more than just two constituents. Since they can in fact be quite large, matrices are often used to simplify the calculation of portfolio volatility. Thus an alternative notation for equation 12-3 is:

$$\sigma_p = \sqrt{w^T \Omega w} \tag{12-5}$$

where  $\Omega$  is the covariance matrix, w is the vector of asset weights and  $w^T$  is its transpose. The covariance matrix represents all the possible permuations across the portfolio, and for the purposes of this calculation is often expressed in terms of \$/share. Note, for more details on how to construct a covariance matrix sec Addendum A at the end of this chapter.

**Example 12-2:** Consider a simple portfolio with three assets. The portfolio is long 120 of asset ABC (volatility=0.245) and short 80 DEF (volatility=0.161) and 40 HIJ (volatility=0.387). The vector of asset weights (w) and the covariance matrix ( $\Omega$ ) are:

$$w = \begin{pmatrix} 120 \\ -80 \\ -40 \end{pmatrix} \quad \Omega = \begin{pmatrix} 0.060 & 0.033 & 0.021 \\ 0.033 & 0.026 & 0.002 \\ 0.021 & 0.002 & 0.150 \end{pmatrix}$$

Substituting these into equation 12-5, the expected portfolio volatility (in dollars) is:

$$\sigma_p = \sqrt{(120 \ -80 \ -40) \begin{pmatrix} 0.060 & 0.033 & 0.021 \\ 0.033 & 0.026 & 0.002 \\ 0.021 & 0.002 & 0.150 \end{pmatrix} \begin{pmatrix} 120 \\ -80 \\ -40 \end{pmatrix}} = $21.17$$

Consequently, our simple portfolio has an expected volatility of \$21.17.

Note that it is important to remember that all of these are simply estimates. They rely on forecasts for the individual volatilities and correlations, which will usually be based on historical data. Their accuracy depends on how well these forecasts match reality. Hence the importance of the error term  $(\varepsilon)$  in equation 12-1.

## Diversification

Diversification can result in a significant decrease in the overall portfolio risk, as we saw back in Figure 12-1. Indeed, its effect is probably best summed up by Burton Malkiel (2004) as the closest thing there is to a free lunch in finance.

![](_page_4_Figure_8.jpeg)

Figure 12-3 Portfolio risk for a range of different correlations

If we go back to our two-asset portfolio from Example 12-1, we can see how a lower correlation between the assets leads to a lower portfolio risk, as shown in Figure 12-3. This makes sense because with a correlation of  $-1.00$  the price rise of one asset will be offset by an equivalent drop in the price of the other. In comparison, a correlation of 1.00 means that both prices will rise, so there is no implicit hedging.

Successful diversification relies on grouping together assets that are uncorrelated, so their covariance is zero. Therefore, price rises/drops will not affect all the assets in the portfolio uniformly, reducing the overall volatility of the portfolio and ensuring a more consistent performance. For example, correlation should be lower for stocks across different sectors, industries or countries.

Another way of visualizing the relationship between correlation and risk is shown in Table 12-1 which directly maps the correlation to the proportion of diversifiable risk which may be eliminated:

| Intro-<br>portfolio<br>correlation | Percent of<br>diversifiable risk<br>eliminated |
|------------------------------------|------------------------------------------------|
| 1.00                               | 0.00                                           |
| 0.75                               | 12.50                                          |
| 0.50                               | 25.00                                          |
| 0.25                               | 37.50                                          |
| 0.00                               | 50.00                                          |
| $-0.25$                            | 62.50                                          |
| $-0.50$                            | 75.00                                          |
| $-0.75$                            | 87.50                                          |
| $-1.00$                            | 100.00                                         |

Source: Wikipedia (2006)

#### Table 12-1 The relationship between intra-portfolio correlation and the amount of diversifiable risk

This risk reduction may be harnessed to determine the optimal composition of portfolios, as Markowitz suggested. For each group of assets, the optimal composition may be discovered by altering the weightings of the constituents to find the solution with the lowest risk. This is effectively what we did in Example 12-1.

However, it is also important to take into account the returns for each asset; hence, we can plot a chart of risk versus returns for the various portfolio combinations. An example of this is shown in Figure 12-4, based on the assumption that the returns for assets EFG and HIJ are 10% and 5% respectively.

This type of portfolio risk curve is sometimes called a Markowitz efficient frontier. The shape of each curve is dependent on the correlation between the two assets: When the assets are perfectly correlated, the frontier forms a straight line. The curvature of this frontier increases as the assets become less correlated. Few assets exhibit perfect correlation, consequently diversification is possible. Note, few assets are perfectly negatively correlated either.

#### Decomposing portfolio risk

Portfolio risk may also be decomposed into simpler components, just as we did for transaction costs in Chapter 6. A common approach used for returns is the single factor model. This expresses returns in terms of an expected out-performance compared to a specific factor. In this case, the factor represents the performance of a key benchmark (or the market). Hence, the returns  $(r)$  may be expressed as:

![](_page_6_Figure_1.jpeg)

Figure 12-4 Example Markowitz efficient frontiers

$$r = \alpha + \beta r_R + \varepsilon$$

where  $\alpha$  represents the out-performance,  $r_B$  is the benchmark (or market) return and  $\varepsilon$  is an independent error factor. The beta  $(\beta)$  factor determines how much impact the benchmark has on the overall returns. In comparison, the out-performance ( $\alpha$ ) and the error factor represent returns that are uncorrelated with the benchmark (or market).

A similar approach may be used to model the variance of these returns, or portfolio risk. Nadine Gottschalk  $(2003)$  shows that the variance may be represented as:

$$\sigma_i^2 = \beta_i^2 \sigma_B^2 + Var(\varepsilon) \tag{12-6}$$

where  $\sigma_B$  is the variance of the benchmark (or market) returns and  $Var(\varepsilon)$  represents an independent error factor. So the portfolio risk may be broken down into two main components:

- a systematic benchmark (or market) risk ٠
- $\bullet$ a non-systematic or asset specific risk

The systematic (or market) risk represents the risk of a market move. Again, the beta factor determines how much impact this actually has on the overall portfolio, with higher betas implying more risk. Note that this also represents the baseline level of risk that may not he reduced by diversification. Although separate hedging strategies may still be used, for instance, trading futures to counteract the market risk.

The non-systematic (or specific) risk is actually the independent error factor in equation 12-6. It represents the risk that may be reduced by diversification.

#### Specific risk factors

Specific risk may in turn be broken down into a range of other common risk factors together with an asset specific residual risk. The common factors represent risks that may not be felt market-wide, but do exert an effect on specific groups of assets.

A common means of decomposing risk is to replace the single factor model with more complex multi-factor models. The study by Eugene Fama and Kenneth French (1993) is a well-known example of this. They analysed the returns for a mix of U.S. stocks and bonds (government and corporate). Overall, they found three common risks for stocks, namely the market and factors related to the firm size and book-to-market equity (which relates the firm's balance sheet value to its actual market value). For bonds, they noted common factors based on their maturity and default risk. Other common factors may correspond to the asset's country of issuance or currency; or for firms the industries or sectors with which they are most aligned. Hence, one way of viewing this breakdown of portfolio risk is shown in Figure 12-5.

![](_page_7_Figure_2.jpeg)

Figure 12-5 Separating out the components of portfolio risk

A nice illustration of the impact of some of these factors is provided by Ananth Madhavan and Jian Yang (2003). They analysed data from the annual reconstitution of the Russell indices, the results are shown in Figure 12-6. Overall, they note that in 2002 the active risk was more than  $2\%$  between the pre and post-reconstitution of the indices, based on market capitalisation. Whilst much of this risk was systematic or market risk, it is interesting to see how much was attributed other common factors. In particular, for both indices the stylebased Value/Growth factor was extremely important. Similarly, it is worth noting just how small the asset specific residual risk can be: For the Russell 1000, we can see it was merely equal to the combined industry and sector risk.

Clearly, such risk breakdowns will be different for each portfolio, but as Figure 12-6 shows, the common risk factors can play a significant role and so should be considered rather than focussing solely on asset specific risk.

![](_page_8_Figure_1.jpeg)

Reproduced with permission from ITG Inc. and Institutional Investor

Figure 12-6 A breakdown of portfolio risk factors

# Portfolio risk measures

Quantifying and tracking portfolio risk are vital in order to minimise it. A variety of risk measures are used in both pre and post-trade analytics. Some are even used during execution to track the ongoing performance. Based on the previous decomposition of risk, we can fairly easily divide portfolio risk into systematic (or market) and non-systematic (or specific) components.

Market risk may be tracked using the portfolio's overall beta coefficient, as we saw in equation 12-6. This allows us to quantify the level of non-diversifiable risk that we may need to hedge.

Tracking error provides a measure of how closely a portfolio follows a specific benchmark. If the benchmark corresponds to the market then the tracking error reflects the specific risk component. Thus, a high tracking error implies a considerable proportion of specific risk.

An alternative approach to risk measurement is offered by the marginal contribution to risk (MCR). This is measured for each constituent of a portfolio. It reflects how the overall portfolio risk might change if the position of a specific asset is increased. Therefore, the key to risk reduction is to target the constituents which have a high MCR.

#### Beta

The beta coefficient relates to the volatility of an asset's or portfolio's returns in comparison with the rest of the market. Essentially, it acts as a measure of the non-diversifiable market (or systematic) risk. A higher beta suggests greater volatility and so more risk.

The beta for an asset is based on the covariance of its returns with the market:

$$\beta_i = \frac{Cov(r_a, r_m)}{Var(r_m)}$$
(12-7)

where  $r_a$  corresponds to the asset's returns and  $r_m$  represents those of the market. Hence, it is the ratio of the covariance of the two sets of returns divided by the variance of the market's returns. Note the market will often be represented by a key benchmark price, such as that of a major stock index.

For example, an asset (or portfolio) whose returns change in line with the market has a beta of 1. Thus, a 10% increase in the market will also mean a 10% increase for the asset, whilst a 10% decrease will lead to a similar drop. A beta of 2 means that the price swings are twice as rapid for the asset as the market, so a 10% rise in the market now leads to a 20% rise in the asset. Conversely, a beta of 0.5 means the sensitivity is halved, so a market fall of 10% only results in a drop by  $5\%$  for the asset. Assets with a negative beta actually move in the opposite direction to the market. For instance, during market crises the prices for precious metals often increase, so firms whose income is dependent on this can exhibit negative betas. A beta of zero is harder to find, this means there is absolutely no correlation between the two sets of returns.

Equation 12-7 may also be used to determine the beta of a portfolio, based on the covariance of the portfolio's returns with those of the market. Alternatively, we can determine the portfolio beta from the weighted average of the betas of its constituent assets. For each constituent the beta is determined from its covariance with the other portfolio members. Using the matrix based notation we can express this as:

$$\beta_i = \frac{\sum_{j=1}^n \Omega_{i,j} w_j}{\sigma_p^2}$$

where  $\Omega_{i,j}$  is the covariance matrix,  $w_j$  is the weight of each asset (j) and  $\sigma_p^2$  is the variance of the entire portfolio.

In theory, if we could construct a portfolio of assets with a beta of zero it would have no non-diversifiable risk. Consequently, we could use diversification to reduce the overall risk to a negligible amount. Realistically, though, most assets have some degree of correlation with each other.

#### **Tracking error**

Many portfolios are managed to a benchmark, such as an index. Passive funds will often aim to match the returns of a specific benchmark index, whilst active funds will try to outperform them. Tracking error provides a measurement of how closely a given portfolio follows the benchmark. Therefore, managers of passive index tracking portfolios will seek to minimise their tracking error. In general, tracking error is calculated from the standard deviation of the difference between the portfolio and index returns:

$$TE = \sqrt{\frac{\sum_{i=1}^{n} (R_P - R_B)^2}{N - 1}}$$

where  $R_P$  represents the portfolio returns and  $R_B$  are those of the benchmark for N time periods. A high tracking error reflects a significant deviation from the benchmark. Essentially, it also reflects the active risk of a portfolio, which is a measurement more commonly adopted by active fund managers.

#### Marginal contribution to risk

The marginal contribution to risk (MCR) may be used by investors to determine the portfolio's risk sensitivity to a specific asset. It reflects the actual change in overall portfolio risk, so diversification is taken into account. Therefore, a comparatively risky asset may have a lower MCR than expected.

For any given portfolio the vector of marginal contributions to risk may be defined as:

$$MCR_{i} \equiv \frac{\partial \sigma_{p}}{\partial w_{i}} = \frac{(\Omega w)_{i}}{\sigma_{p}} = \frac{Cov(r_{i}, r_{p})}{\sigma_{p}}$$
(12-8)

where  $\Omega$  is the covariance matrix, w is the vector of asset weights,  $\sigma_p$  is the standard deviation of the entire portfolio and  $r_i$  and  $r_p$  are the returns of the asset (i) and the portfolio respectively.

Note that generally the MCR is measured by determining the effect of varying the existing position of the given asset by  $1\%$ . Thus, the standardized change in portfolio risk may simply be determined by dividing equation 12-8 by  $100$ .

Based on the similarity with equation 12-7 we can also express the MCR in terms of the asset's beta:

$$\frac{\partial \sigma_{p}}{\partial w_{i}} = \beta_{i} \cdot \sigma_{p}$$

So, the MCR is equivalent to a beta adjusted portfolio risk. Traders cannot vary the contents of a trade list; however, they can use the MCR as a guideline for how trading will affect the residual risk, as Robert Kissell and Morton Glantz (2003) point out. If a particular asset has a high MCR then trading it more quickly will help reduce the overall risk. Conversely, assets with negative MCRs actually act as natural hedges; therefore, it makes sense to trade these more slowly to prolong this benefit.

# **12.3 Transaction cost analysis for portfolios**

Portfolio risk and diversification mean that transaction cost analysis is slightly more complicated when dealing with portfolios. In the following sections, we will briefly consider how the cost estimates we saw in Chapter 10 may be extended to deal with this.

## Market impact

Market impact costs are additive, therefore the market impact calculation for a portfolio is just a case of summing all the constituent impacts. Using the Kissell and Glantz (2003) market impact model, we can express the market impact cost for a portfolio of  $m$  stocks as:

$$MI = \sum_{i=1}^{m} \sum_{j=1}^{n} \frac{0.95x_{ij}^{2}I_{i}}{X_{i}*(x_{ij}+0.5v_{ij})} + \sum_{i=1}^{m} \sum_{j=1}^{n} \frac{0.05x_{ij}I_{i}}{X_{i}}$$

where  $I_i$  is the instantaneous impact cost,  $X_i$  is the total order size for each asset and for each period j the order size is represented by  $x_{ij}$  whilst  $v_{ij}$  is the expected volume. Though easy to compute, the additive nature also means that market impact costs are not reduced by portfolio diversification. So impact costs are an important consideration for portfolios.

# **Timing Risk**

Just as in Chapter 6, timing risk for portfolios may still be split into separate price and liquidity risks. The price risk is based on the portfolio risk of the remaining positions. From equation 12-5 Robert Kissell and Roberto Malamut (2005b) define the price risk for a portfolio as:

$$\sigma(x_j) = \sqrt{\sum_j r_j^T C r_j}$$

where  $r_i$  is the vector of residual portfolio positions that are left to be traded for each period *j*, and  $C$  is the covariance matrix in  $\frac{\text{h}}{\text{h}}$ .

Liquidity risk represents the risk that our market impact estimations will be inaccurate due to unexpected market volumes. By assuming that any liquidity surprises are uncorrelated, Kissell and Glantz (2003) are able to base liquidity risk on the variance of their temporary market impact function. So, for any given asset the liquidity risk may be defined as  $\sigma(h(x))$ :

$$\sigma(h(x)) = \sqrt{\sigma^2 \left(\frac{I}{X} \sum_j \frac{x_j^2}{(x_j + 0.5\nu_j)}\right)}$$

where I is the instantaneous market impact, X is the total order size and for each period j the order size is represented by  $x_i$  whilst  $v_i$  is the expected volume.

Across an entire portfolio, the liquidity risk may be represented as the sum of these individual risks:

$$\sigma(x_j) = \sqrt{\sum_i \sigma^2(h(x_j))}$$

So as a whole, the portfolio timing risk may be expressed as:

$$\Re(x_j) = \sqrt{\sum_j r_j^T C r_j + \sum_i \sigma^2(h(x_j))}$$

Thus, the main difference to the portfolio volatility examples we saw in section 12.2 is the addition of liquidity risk. This is covered in some more detail in Kissell and Glantz (2003).

# 12.4 Optimal portfolio trading

In Chapter 7, we noted that achieving an optimal trading strategy requires us to meet the investor's specified trading objectives, which may be to:

- Minimize the expected cost for a given level of risk
- ٠ Achieve price improvement over a given level of cost
- Balance the trade-off between expected cost and risk ٠

The same principles apply for portfolio trading with the added complication of trying to maximise diversification, and so minimise the portfolio risk. Again, the set of optimal trading strategies is represented by the efficient trading frontier. This may be found by solving the following optimisation for the expected cost  $(E(x))$ :

 $\min(E(x) + \lambda V(x))$ 

where  $V(x)$  corresponds to the expected risk and  $\lambda$  is represents the level of risk aversion. To find the optimal solutions, mean-variance optimization techniques can help minimise the expected impact cost, whilst covariance or multi-factor risk models may be used to provide the expected portfolio risk.

That said, when trying to minimise the expected cost for a given level of risk, the optimal solutions are a constantly moving target. This is because the portfolio risk is based on the residual trading positions, and so it must be re-evaluated each time the portfolio changes. Hence, each change requires the creation of a new efficient trading frontier, from which the minimum cost may then be targeted. Consequently, the minimum impact costs will vary over time. So to maintain the same level of risk we may have to alter the pattern of our trading, as shown by the sample path in Figure 12-7.

![](_page_12_Figure_4.jpeg)

Source: Domowitz and Krowas (2004) Reproduced with permission from ITG Inc. and Institutional Investor

Figure 12-7 Tracking portfolio risk and cost over time

Likewise, achieving price improvement over a given level of cost faces the same problem. Effectively, both these goals now have to dynamically balance the trade-off between expected cost and portfolio risk. For example, from a cost perspective it may make sense to aggressively trade one of the assets. However, if this was acting as a natural hedge for the residual portfolio (a negative MCR) then the reduced diversification may lead to a significant increase in portfolio risk. Therefore, we need to determine which effect is more important and act accordingly.

Thus, finding the optimal trading strategy for a portfolio requires both cost-based

execution models and techniques from portfolio optimisation. Increasingly, these are converging to provide dedicated portfolio execution models.

## Additional goals for portfolio trading

Portfolio risk may be decomposed into a range of different factors, as we saw in Figure 12-5. Thus, portfolio managers may also track risk in terms of its market or asset specific components. So they may consider issues such as country, currency or sector risk. Alternatively, they might focus on minimising the tracking error for their fund. Therefore, investors often adopt a range of additional strategies to try to minimise risk for their portfolios, such as:

- ٠ Cash balancing
- Beta/Market neutrality
- Sector/Country neutrality  $\bullet$
- $\bullet$ Minimising index tracking error

The easiest of these approaches is cash balancing, which just halances the value of the long and short positions, making the portfolio cash neutral. Still, this can leave exposure to market risk. Therefore, market neutral hedging tries to ensure that the net beta of the portfolio is zero. Similarly, even market neutral portfolios may still be exposed to considerable risk from other common risk factors; hence, sector/country neutrality may be targeted. Each of these approaches requires careful halancing of the various groups. This also applies for tracking error, where a portfolio may be divided into the assets that help or hinder the index tracking. Clearly, if multiple goals are required this balancing act can become even more complicated; hence, it may be useful to prioritise them.

The portfolio manager needs to control the risk for the entire investment portfolio. This also includes the basket of assets that have been sent for trading. Brokers/traders may also need to be able to support these additional goals when trading portfolios. Otherwise, during the trading/transition process the investment portfolio could be exposed to unnecessary risk, particularly if trading spans days or even weeks. These goals may also enhance the overall performance. So, not only do portfolio trading strategies need to balance impact costs with portfolio risk, they may also need to take account of any such additional requirements.

## Hedging

Incorporating hedging requirements into a portfolio trading strategy can pose some difficulties. We need to strike the right balance between enforcing the hedging and allowing the constituent orders to trade optimally.

Essentially, this is similar to what we saw for the pair trading strategy, except that it can involve multiple groups. For instance, if the executed value for one group starts to lag behind then we may need to either:

- $\bullet$ Trade more aggressively for that group
- Slow down trading for the other group(s)

As a simple example, let's consider the following cash balanced trade list shown in Table 12-2, essentially we can view this as a three-asset portfolio. As long as we manage to trade each asset in line with each other, we should maintain this natural hedging. Thus, for the first period  $(t_1)$  we can issue 10% of each target position as a limit order.

Let's assume that by the end of this period only the orders for ABC and XYZ have completed, so the limit order for 50 HJK is still unfilled (or extant).

|      | Side<br>Asset | Price |        | Position at $t_1$ |        |  |  |
|------|---------------|-------|--------|-------------------|--------|--|--|
|      |               |       | Target | Sent              | Filled |  |  |
|      | ABC           |       | 500    | 50                |        |  |  |
| Buy  | HJK           |       | 500    | 50                |        |  |  |
| Sell | XYZ           |       | ,000   | 100               | 100    |  |  |
|      |               | Net   |        |                   | $-50$  |  |  |

**Table 12-2 A simple two-sided trading portfolio** 

So by the end of the first period our rudimentary hedging has already broken down. To remedy this we could:

- 1. Wait for the buy order for HJK to complete hefore placing more orders.
- 2. Convert the remaining buy to a more aggressive limit or market order.

Option 1 could prove to be expensive if the more liquid assets ABC and XYZ have unfavourable price trends. Effectively, we have stalled trading until the illiquid asset catches up, exposing ourselves to timing risk for the other constituents, Likewise, option 2 could also prove to be expensive, since we may simply not be able to buy any HJK within acceptable price limits. The cost of catching up, to become cash neutral again, could actually outweigh the benefits of hedging.

In this case, because we are only striving to be cash neutral, a possible short-term solution to this problem is to make up the balance by additionally buying another 50 of the more liquid ABC. Though, for more complex hedging requirements such an approach may not always be possible.

A common solution is to incorporate a legging value, much as we saw for pair trading. This allows one of the groups (in this case one side of the portfolio) to lag the other/s by a specific amount. This gives the trading strategy some breathing space before any remedial action is taken to enforce the hedging requirements. Otherwise, we could potentially miss out on good trading opportunities for some assets just because an order for a less liquid asset is struggling.

Note that if there is a significant mismatch in the liquidity of the portfolio constituents then cost effective hedging may be difficult to achieve. In some cases, it may well be worth handling the more illiquid assets separately. This highlights the importance of pre-trade analysis, to spot any such potential issues and determine how much of a problem they might pose before trading commences.

#### **Cash balancing**

Cash balancing obviously only applies for two-sided portfolios. The aim is to stay "dollar neutral" so that the two sides offset one another. Essentially, the proceeds from selling cover the costs of the purchases.

We have already seen a simple example of cash balancing, back in Table 12-2. Another example of a cash balanced trade list is shown in Table 12-3. The buy and sell sides are already balanced so we can split off child orders for the first period based on a percentage of their value. For the buy side, we have simply assigned the target for the first period as 10% of the position, as shown in the column labelled target  $(Tgt)$ . Whilst for the sell side, the target quantities have been assigned slightly more randomly. This allows us to take into account factors such as short-term liquidity or favourable prices. Though, in terms of remaining cash neutral, the sum of our target sell side positions still meets our target.

| Buys  |     |       |     |        | Sells |     |       |     |        |
|-------|-----|-------|-----|--------|-------|-----|-------|-----|--------|
| Asset | Prc | Pos   | Tgt | Value  | Asset | Prc | Pos   | Tgt | Value  |
| ABC   | 30  | 1,200 | 120 | 3,600  | PQR   | 20  | 1,300 | 104 | 2,080  |
| DEF   | 40  | 500   | 50  | 2,000  | STU   | 30  | 700   | 84  | 2,520  |
| GHI   | 60  | 800   | 80  | 4,800  | VWX   | 70  | 600   | 66  | 4,620  |
| JKL   | 50  | 600   | 60  | 3,000  | YZA   | 40  | 400   | 32  | 1,280  |
| MNO   | 80  | 200   | 20  | 1,600  | BCD   | 90  | 500   | 50  | 4,500  |
| Σ     |     |       |     | 15,000 | Σ     |     |       |     | 15,000 |

<table>

 Table 12-3 Example trading targets to maintain a cash balanced portfolio

Market prices change constantly, so it is unlikely to achieve perfect cash balancing simply by trading percentages. Adjustments will need to be made based on real time price changes. Though, it is impractical to constantly change the size of extant orders; particularly for venues where this would result in a loss of priority on the order book, or those that charge for order updates. Hence, strategies may incorporate minimum limits to ensure that the price change is large enough to warrant changing the orders.

This approach may also be used for portfolios that are not actually cash balanced. For instance, we could modify the trading strategy to bias the trading rates for the buy and sell sides to try to improve the balance. If the portfolio was net long, we could trade the buy side more aggressively until it balanced with the sell side. However, for very unbalanced portfolios Anna Bystrik and Richard Johnson (2005) suggest that it may be worth trading each side separately, since risk management techniques tend to be more effective for halanced portfolios.

#### Market-neutrality

A portfolio is typically said to be market-neutral if its net beta is zero. In other words, the portfolio returns must be uncorrelated with the market. This approach is popular with fund managers since it means general market risk is minimised, leaving them only exposed to the specific risks that they are focussed on.

Therefore, when trying to maintain a market-neutral approach the assets with a higher beta will often be traded faster than those with a lower one. For example, let's consider the trade list shown in Table 12-4.

| Buys |     |     |          | Residual     |        |          |         |                 |
|------|-----|-----|----------|--------------|--------|----------|---------|-----------------|
| i    | Prc | ß   | Position | $\beta$ -wgt | Target | Position | Mkt Val | $\beta$ -w $gt$ |
| ABC  | 30  | 2.0 | 1,200    | 0.480        | 480    | 720      | 21,600  | 0.384           |
| DEF  | 40  | 1.0 | 500      | 0.133        | 100    | 400      | 16,000  | 0.142           |
| GHI  | 60  | 1.5 | 800      | 0.480        | 240    | 560      | 33,600  | 0.448           |
| JKL  | 50  | 0.5 | 600      | 0.100        | 60     | 540      | 27,000  | 0.120           |
| MNO  | 80  | 0.5 | 200      | 0.053        | 20     | 180      | 14,400  | 0.064           |
| Σ    |     |     |          | 1.247        |        |          | 112,600 | 1.157           |

**Table 12-4 Example buy trading targets to maintain a market neutral portfolio** 

Assets ABC and GHI have the highest betas, combined with their relative positions this

means they contribute most to the overall net beta, as can be seen in the beta weight  $(\beta \text{-} wgt)$ column.

As a baseline, we can trade 20% of each of the assets in the next period. Though, this will do nothing to alleviate the relative beta imbalance. A simple way of changing this is to adjust this proportion by each asset's beta, so we actually trade 40% of ABC and only 10% of JKL. If these fully execute this leaves residual positions with a significantly lower net beta, as shown in Table 12-4. So it should reduce by around 8% from 1.247 to 1.157.

Although this simple beta adjustment works for single-sided trade lists (or portfolios), we need to be more careful with two-sided ones. For example, let's now assume that the sells shown in Table 12-5 represent the other half of our list.

| Sells |     |     |          | Residual     |        |          |         |                 |
|-------|-----|-----|----------|--------------|--------|----------|---------|-----------------|
| Asset | Prc | ß   | Position | $\beta$ -wgt | Target | Position | Mkt Val | $\beta$ -w $gt$ |
| PQR   | 20  | 1.5 | 1,300    | 0.260        | 390    | 910      | 18,200  | 0.243           |
| STU   | 30  | 0.8 | 700      | 0.112        | 112    | 588      | 17,640  | 0.126           |
| VWX   | 70  | 1.3 | 600      | 0.364        | 156    | 444      | 31,080  | 0.360           |
| YZA   | 40  | 1.5 | 400      | 0.160        | 120    | 280      | 11,200  | 0.150           |
| BCD   | 90  | 1.2 | 500      | 0.360        | 120    | 380      | 34,200  | 0.365           |
|       |     |     |          | 1,256        |        |          | 112,320 | 1.243           |

#### Table 12-5 Example sell trading targets to maintain a market neutral portfolio

Using the same beta adjusted approach we can reduce the net beta for this side to 1.243. The reduction is less marked because unlike the buys the betas are more evenly balanced.

This simple approach results in a buy side with a net beta of 1.157 and a sell side with 1.243. The market values are virtually the same; though, our residual list is still more exposed to market risk on the sell side. So it is important to also consider the net beta when handling two-sided lists/portfolios.

A different approach might be to trade 20% of the buy side, maintaining its net beta as 1.247. Whilst on the sell side the beta-adjusted approach may be used, reducing it to 1.243. Alternatively, we could also use a scaling factor to trade more of the higher beta assets on the sell side, to try to address the imbalance.

#### Categorised neutrality

Portfolios may also have substantial exposure to common factors, such as country, currency or sector risk. To reduce this we can try to trade the portfolio in such a way as to neutralise these risk factors.

For instance, Table 12-6 shows the country assignments for our example trade list, using the ISO Country codes for France (FR), Germany (DE) and the U.K. (GB). The net balances are shown in Table 12-7. Notice that the buys and sells are reasonably balanced, although there is more net exposure to U.K. assets than the other countries. Again, we shall aim to trade 10% of this list in the next period. To try to reduce the country risk we can bias trading towards the side that is largest for each country. So for the U.K., the focus will be on reducing the \$42,000 worth of assets to sell, whilst for France and Germany the focus will be on reducing the buys. Similarly, since the U.K. has the largest net imbalance we should also target these assets more than the others.

| Buys  |     |             |          | Residual |        |          |         |
|-------|-----|-------------|----------|----------|--------|----------|---------|
| Asset | Prc | Ctry        | Position | Mkt Val  | Target | Position | Mkt Val |
| ABC   | 30  | FR          | 1,200    | 36,000   | 90     | 1,110    | 33,300  |
| DEF   | 40  | $\text{GB}$ | 500      | 20,000   | 54     | 446      | 17,840  |
| GH1   | 60  | DE          | 800      | 48,000   | 88     | 712      | 42,720  |
| JKL   | 50  | FR          | 600      | 30,000   | 52     | 548      | 27,400  |
| MNO   | 80  | $\text{GB}$ | 200      | 16,000   | 28     | 172      | 13,760  |
| Σ     |     |             |          | 150,000  |        |          | 135,020 |

| Sells |     |             | Residual |         |        |          |         |
|-------|-----|-------------|----------|---------|--------|----------|---------|
| Asset | Prc | Ctry        | Position | Mkt Val | Target | Position | Mkt Val |
| POR   | 20  | FR          | 1,300    | 26,000  | 38     | 1,262    | 25,240  |
| STU   | 30  | FR          | 700      | 21,000  | 26     | 674      | 20,220  |
| VWX   | 70  | $\text{GB}$ | 600      | 42,000  | 150    | 450      | 31,500  |
| YZA   | 40  | FR          | 400      | 16,000  | 18     | 382      | 15,280  |
| BCD   | 90  | DE          | 500      | 45,000  | 25     | 475      | 42,750  |
| Σ     |     |             |          | 150,000 |        |          | 134,990 |

#### **Table 12-6 Example trading targets to aim for a category neutral portfolio**

One way of assigning the target trades is to base them purely on the imbalances. Given a sum total of \$30,000 for both buys and sells, we can assign half of this to redress the balance for U.K. assets, whilst the remainder is split evenly between France and Germany.

The net imbalances may then be used as a starting point, assigning this to the side that has the greatest value. The residual may then be split evenly between buys and sells. Hence, for the U.K. \$6,000 will target sells, leaving \$9,000 to split between them. So our target values are \$4500 for U.K. buys and \$10,500 for sell orders. The remaining target values are shown in Table 12-7.

|             |              | Market Value |          |       | Target Value | Residual Value |        |        |  |
|-------------|--------------|--------------|----------|-------|--------------|----------------|--------|--------|--|
| Ctry        | $Bt t \nu s$ | Sells        | Net      | Buvs  | Sells        | Buvs           | Sells  | Net    |  |
| DE          | 48,000       | 45,000       | 3.000    | 5,250 | 2,250        | 43,200         | 43,200 |        |  |
| FR          | 66,000       | 63,000       | 3,000    | 5,250 | 2,250        | 59,400         | 59,250 | 150    |  |
| $\text{GB}$ | 36,000       | 42,000       | $-6,000$ | 4,500 | 10,500       | 32,400         | 32,550 | $-150$ |  |

#### <table> Table 12-7 Net balances for a category neutral portfolio

Since the list is cash balanced, we will also try to preserve this, as there is no point introducing additional risks. In this example, the target buys and sells still add up to \$15,000 so there is no need to make any more changes.

Finally, we now need to convert the target balances into target shares for each of the assets. For simplicity, we shall evenly assign them for each country, although factors such as liquidity or price trends could also be taken into account. Adjustments could also be made to ensure quantities are rounded to meet their lot sizes. Sample target quantities are shown in Table 12-6.

Provided we manage to trade these targets, we can see from Table 12-7 that the net values for the residual list will be almost zero. Though, the need to balance other requirements

means that the category imbalances will often be reduced more gradually than this. Also, note that exactly the same principles may be used for other common factors such as currency or sector risk.

#### Minimising tracking error

Tracking error relates the portfolio returns to those of a specific benchmark. An alternative way of viewing this is to say that a portfolio with a minimal tracking error should have a net beta of 1.0. In other words, the performance of the portfolio exactly matches its benchmark, so changes in value are inline with each other.

We have also seen how adjustments could be made to try to achieve a net beta of 0.0 for market neutral portfolios. A similar approach may be used to minimise tracking error, except the target net beta is now 1.0. So again, we target the constituents with the highest beta weights, as we saw in Table 12-4.

#### Minimising the overall portfolio risk

We can also seek to minimise the overall portfolio risk based on the matrix formation we saw in equation 12-5. By using the first derivative of this equation, we can try to find a possible minimum:

$$\frac{\partial(Risk)}{\partial w} = \frac{w^T\Omega}{\sqrt{w^T\Omega w}} = 0 \quad \Rightarrow w^T\Omega = 0$$

where  $\Omega$  is the covariance matrix, w is the vector of asset weights and  $w^T$  is its transpose. Kissell and Glantz (2003) find that solving this for  $w$  yields:

$$w_{optimal} = A * B * w$$

where  $A$  and  $B$  are the following matrix operations:

and

 $A = \text{-}inverse(diagonal(\Omega))$  $B = \Omega + inverse(A)$ 

They stress the fact that this solution is only valid for the execution of a single asset. The resultant position change will affect the whole portfolio's risk, so for each subsequent trade a fresh solution must be recalculated.

As an example, let's reuse the portfolio and covariance matrix from Example 12-2:

$$w = \begin{pmatrix} 120 \\ -80 \\ -40 \end{pmatrix} \quad \Omega = \begin{pmatrix} 0.060 & 0.033 & 0.021 \\ 0.033 & 0.026 & 0.002 \\ 0.021 & 0.002 & 0.150 \end{pmatrix}$$

We can then use the appropriate matrix operations to determine the product:

$$A \ast B \ast w = \begin{pmatrix} 0.000 & -0.550 & -0.350 \\ -1.269 & 0.000 & -0.077 \\ -0.140 & -0.013 & 0.000 \end{pmatrix} \begin{pmatrix} 120 \\ -80 \\ -40 \end{pmatrix} = \begin{pmatrix} 58 \\ -149 \\ -16 \end{pmatrix} \implies v = \begin{pmatrix} 62 \\ 69 \\ -24 \end{pmatrix}$$

This implies that the optimal weightings are 58 of asset ABC, -149 of DEF and -16 of HIJ. Given our current positions, this implies the vector  $v$ , which represents the possible transitions to reach this optimal state. Note that we cannot trade any DEF since the optimal

position of -149 lies outside our permitted range. Thus, we may sell 62 of ABC or buy 24 HIJ.

Using equation 12-5, we can now apply each of these potential positions to confirm which gives the lowest risk. For example, inputting the values for ABC gives:

$$\sigma_p = \sqrt{(58 \quad -80 \quad -40) \begin{pmatrix} 0.060 & 0.033 & 0.021 \\ 0.033 & 0.026 & 0.002 \\ 0.021 & 0.002 & 0.150 \end{pmatrix} \begin{pmatrix} 58 \\ -80 \\ -40 \end{pmatrix}} = $14.74$$

Trading ABC reduces the portfolio risk to \$14.74 whereas trading HIJ only reduces it to \$18.97. Therefore, the optimal trade is to sell 62 shares of ABC.

As we saw back in Figure 12-7, the optimal solution when trying to minimise the expected cost for a given level of risk is a constantly moving target. Each trade changes the overall portfolio composition and so the overall risk. Therefore, to find the next optimal trades we must simply keep repeating this process until the execution is complete.

# 12.5 Portfolio trading with algorithms

Conventional trading algorithms may easily be used for trading portfolios, although clearly there are complications when trading lists that span multiple markets, currencies and/or time zones.

Another important consideration is how the chosen trading strategies affect portfolio risk, or achieve any of the other specific goals covered in the previous section. Standard single asset algorithms have no inbuilt mechanisms to accommodate this. Therefore, we will also look at some methods for tailoring algorithms to cope with these requirements.

## Portfolio trading with standard trading algorithms

In general, any of the single asset trading algorithms we saw in Chapter 5 may be used for portfolio trading. A trading list might comprise of tens, or even hundreds of assets, which might be buys, sells or a mixture of the two. These may all be traded with a single algorithm, targeting a benchmark such as VWAP or their arrival price. Alternatively, they might be for a range of different algorithms, depending on the relative difficulty of each order. The trading algorithms might be specified by the investor, or determined by the broker/dealer.

#### Can "one size fit all"?

When choosing trading algorithms for portfolios we should first consider whether a single algorithm is appropriate for all the constituents of the trading list. An interesting example is given by Ian Domowitz and Henry Yegerman (2005a) from ITG. This is based on a large portfolio transition that was benchmarked using the daily VWAP for each asset. The strategy resulted in transaction costs that were approximately double the estimate from pre-trade analysis. By analysing the volatility and order sizes of the constituents, they concluded that costs might have been reduced by adopting differing trading strategies, rather than a "one size fits all" approach. This is illustrated in Figure 12-8.

To find a better alternative they classified the orders into three main groups, based on each asset's volatility and the relative size of the order compared to the average daily volume (ADV). At the two extremes, they found small orders for volatile assets and large orders for assets with a much lower volatility.

![](_page_20_Figure_1.jpeg)

![](_page_20_Figure_2.jpeg)

As we saw in Chapter 7, volatile assets suit a more aggressive trading style, countering the associated timing risk. This is also helped by the small order size, which means lower market impact costs. Hence, Domowitz and Yegerman proposed an aggressive strategy for such orders. For example, we might use an implementation shortfall algorithm.

Conversely, for the larger orders a more passive approach makes sense, to try to reduce the overall market impact. Similarly, since the volatility of these assets is lower, the price risk will not he as significant. So a VWAP over the whole day may be an appropriate choice. That said, timing risk comprises of both price risk and liquidity risk, so liquidity can also be a considerable factor for large orders, as Domowitz and Yegerman point out. Thus, opportunistic trading may also be appropriate, depending on the uncertainty of the transaction cost estimates. Those orders, which are more than 40% of the ADV trading, may span multiple days. In such cases, a more aggressive strategy may be suitable for the first day, followed by more passive trading on any subsequent days.

Between these two extremes are orders that may be suitable for more opportunistic trading. In terms of trading algorithms, this might range from a VWAP with a short horizon, a percent of volume or a price inline. Alternatively, an implementation shortfall or even a liquidity-based algorithm might be used. The choice also depends on other factors such as investor risk aversion, liquidity and price momentum.

#### Standard trading algorithms and portfolio risk

Clearly, trading algorithms designed for executing single assets have no consideration of portfolio risk. They are solely focussed on optimising the execution of their individual orders. So the trader handling the list will have to do this manually. They may decide to split it into waves (or slices), each weighted to try to maintain the diversification. Alternatively, the riskier assets might be handled first; so trading algorithms may also be selected based on whether they are optimal for the portfolio as a whole, rather than for a specific order.

Only the simplest schedule-driven approaches, such as TWAP, provide a consistency of

trading across the whole portfolio. For instance, if all the orders are traded using TWAP, we know that halfway through trading we should have 50% of the desired positions for each and every constituent.

In comparison, using more dynamic algorithms will often lead to a shift in the portfolio composition as they are traded. For example, Figure 12-9 shows how different the resultant trading schedules can be for a range of orders using an implementation shortfall (IS) algorithm (in this case Instinet's Wizard algorithm).

![](_page_21_Figure_3.jpeg)

Source: @Instinet(2006)

Reproduced with permission from Instinet

Figure 12-9 Example implementation shortfall schedules

Since the implementation shortfall algorithm is trying to adopt the optimal trading strategy for each order, the resultant trading patterns are clearly very different. The larger orders (in terms of percentage of ADV) are allowed longer to trade to reduce the market impact, whilst a more aggressive approach is taken for the volatile assets to reduce timing risk. So, for this example, the relatively small orders for Cisco (CSCO) and Citigroup (C) should complete first, with the more volatile Cisco traded fastest. Next to complete should be the order for Continental Airlines (CAL), whose high volatility means that aggressive trading is required. Finally, the order for Medtronic (MDT) takes the longest, since its relatively low volatility allows the order to be traded more passively.

Taken in turn, each of these schedules may well be the optimal trading strategy for the corresponding order. Still, this does not necessarily mean it is the best trading strategy for the portfolio as a whole. Diversification is heavily dependent on portfolio makeup. So a significant change in the relative portfolio positions could lead to a considerable shift in the portfolio risk. For instance, let's compare the example portfolio in Figure 12-9 between time periods 1 and 3. Initially, the largest outstanding position is for Cisco, followed by Mcdtronic, Continental Airlines and finally Citigroup. By following the target schedules, at the start of period 3 the position for Cisco has fallen to be only the third largest position, just above Citigroup. So the residual portfolio is now dominated by Medtronic and Continental Airlines. Hence, the overall portfolio risk may be very different between these two periods.

Unsurprisingly, this problem is not unique to shortfall-based algorithms. Other trading algorithms will also face this issue, since trading is unlikely to be evenly balanced across the portfolio. In particular, this concerns dynamic algorithms that are driven by market conditions. It also affects schedule-driven algorithms like VWAP, since there is no guarantee that the volume profiles for the various assets will be similar enough to preserve the portfolio mix, Illiquid assets will also lag behind more actively traded ones. Again, this could reduce the overall diversification. Thus, a more aggressive trading strategy may be necessary to compensate for this.

Note that this issue is not just restricted to algorithm choice. A similar problem arises for portfolios that span multiple countries. Although marketplaces such as Europe are becoming more uniform, there can still be slight differences in market open and close times. Thus, some orders might begin trading before others, causing an imbalance. Explicit start and end times may be set to prevent this, although this obviously reduces the potential trading horizon. Things become even more complex for truly global portfolios where the time-zone differences make simultaneous trading difficult (if not impossible). For instance, during the European morning just after the Asian markets have closed and before the U.S. have opened.

However, maintaining a consistently weighted portfolio is not necessarily the best way to minimise portfolio risk. In fact, all it does is ensure that the portfolio risk stays consistent. Instead, we need to evaluate each order to determine how much it contributes to the overall risk. To minimise this overall risk we therefore need to focus on reducing the positions of those assets that contribute the most. Also, note that the largest risk contributors will not necessarily be the orders for the riskiest assets, since natural hedging will occur between the assets in the portfolio. So instead of selecting the optimal algorithm based on the specific order requirements we should try to determine the best approach for the entire portfolio.

# Tailoring algorithms for portfolio trading

Customising trading algorithms to incorporate portfolio risk makes a lot of sense. Although hedging requirements can prove quite complex, the potential risk reduction and related cost savings can be substantial.

Extending existing trading algorithms to incorporate portfolio models has been a typical (and logical) solution. As demand grows, some vendors are also creating sophisticated new algorithms, designed from the ground up to cater for portfolio trading.

An alternative approach is offered by Robert Kissell, Andrew Freyre-Sanders and Carl Carric (2005). They describe an "algorithm of algorithms" which manages the portfolio trading requirements whilst individual algorithms may still be used for each constituent order. The macro/micro-level split is similar to the division of labour we adopted between trading algorithms and execution tactics in Chapter 5. This offers the prospect of reusing existing single asset trading algorithms to provide a wide variety of trading styles.

In the following sections, we shall outline these two main approaches in some more detail. As the market for algorithmic portfolio trading grows, it will be interesting to see what other variants appear in the future.

#### Algorithms incorporating portfolio risk models

We can incorporate portfolio risk models into trading algorithms by extending existing algorithms or by creating new portfolio specific algorithms from scratch. Either way, shortfall-based algorithms, with their inbuilt cost models, provide a good starting point.

The core of any such approach is a centralised portfolio risk model. One way of achieving this is to have the algorithm for each constituent asset tracking a combination of its own market impact model together with this shared portfolio risk model. Thus, each algorithm is able to make decisions that take into account all the other current portfolio positions. Correlations between the assets may also be used to find natural hedges, and so maximise diversification. Adjustments may be made to try to preserve these relationships, minimising the overall portfolio risk. Since the portfolio risk must be re-evaluated as positions change, this also allows traders to take advantage of other opportunities, such as blocks from crossing networks.

![](_page_23_Figure_4.jpeg)

Source: ©Instinct (2006a)

Reproduced with permission from Instinct

Figure 12-10 Example portfolio optimised implementation shortfall schedules

For instance, Figure 12-10 shows an example two-sided portfolio, each order is traded in parallel using a portfolio optimised implementation shortfall algorithm (in this case Instinct's Wizard PRO<sup>2</sup> which incorporates Northfield Information Services' short-term factor risk model). Each algorithm adjusts its own optimal strategy based on correlations with the other constituents in order to help minimise the overall portfolio risk.

<sup>&</sup>lt;sup>2</sup> Note Instinct's Wizard PRO has since been replaced with their Portfolio IS algorithm.

In this example, the two airline stocks, Continental Airlines (CAL) and the AMR Corporation (AMR), are highly correlated. Hence, these orders actually act as effective hedges for each other since both CAL and AMR have similar prices and we are buying and selling equivalent amounts. The risk reduction achieved from this hedging allows us to trade them more passively, despite them being reasonably volatile stocks. As we can see in Figure 12-10, the trading for both orders is spread throughout the day, helping to reduce their market impact.

A similar level of correlation exists between Microsoft (MSFT) and Yahoo (YHOO). Though, since these are both buy orders the resultant sector concentration could actually increase the potential portfolio risk. Thus, both of these orders are executed reasonably quickly, more like a typical implementation shortfall algorithm. The illiquid Options Xpress (OXPS) has no natural hedges in the portfolio, so it left to trade throughout the day, primarily to minimise impact costs.

Clearly, if we compare this with a purely implementation shortfall based approach, which we saw back in Figure 12-9, one of the most noticeable differences is the fact that many of the orders are now traded throughout the day. This is because of the risk reduction afforded by diversification. It allows for more passive trading, to try to reduce the market impact costs.

Another way of viewing the effectiveness of portfolio-optimised algorithms is to compare their performance in terms of risk. For instance, Figure 12-11 shows an example from Olivier Thiriet (2006) at Credit Suisse. This charts the tracking error for a portfolio of 214 Japanese stocks, with 104 buys, worth \$20 million, and 110 sells, worth \$22 million. Their customised PHD (Portfolio Hedging Device) algorithm achieves a lower tracking error than using standard single asset market inline (effectively POV) algorithms, and much less than the ubiquitous VWAP.

![](_page_24_Figure_6.jpeg)

![](_page_24_Figure_7.jpeg)

# An "algorithm of algorithms"

The "algorithm of algorithms" is a portfolio-focussed approach outlined by Kissell, Freyre-

Sanders and Carrie (2005). It is responsible for managing the portfolio trading requirements whilst individual algorithms are still used for each constituent order. Therefore, a portfolio algorithm can track the overall risk, issuing adjustments to alter the trading patterns of the algorithms for the portfolio constituents.

This innovative approach should allow single asset trading algorithms to be used for optimal portfolio trading with the minimum of changes. The primary requirement is that they support dynamic updates of their parameters, allowing the portfolio algorithm to dynamically control them. Therefore, instead of adopting a "one size fits all" approach we can use the algorithm that is most appropriate for each constituent order, given factors such as the asset's volatility and the order's size. Thus, a portfolio might employ of a range of POV, VWAP, implementation shortfall or liquidity-based algorithms. The standalone portfolio algorithm tracks the progress of each of these orders, adjusting them when it becomes necessary in order to maintain the minimum overall risk.

Obviously, some algorithms are more suited to this approach than others. The target participation rate of POV algorithms makes them extremely easy to control, since the portfolio algorithm can alter the trading pattern simply by increasing or decreasing this target. A similar approach may be taken with algorithms with support a tilt factor, such as some TWAP or VWAP variants. For shortfall-based algorithms, the risk aversion parameter could be updated to trigger more or less aggressive trading. Alternatively, the portfolio algorithm could also slow algorithms down by setting, or modifying, price limits.

Over time, as the portfolio risk profile changes, the most appropriate algorithm for a constituent order might also change. So the portfolio algorithm might need to cancel the order for the original algorithm and replace it with a new order for the residual position. Thus, portfolio constituents might be swapped from a VWAP algorithm to a shortfall or liquidity based one.

In terms of the actual portfolio algorithm, clearly this needs to carefully track the portfolio risk of the residual positions, as well as determining the optimal trading strategy for each constituent order. In addition, it needs to ensure that the projected savings achieved from diversification outweigh any incurred by altering each individual order's optimal trading strategy.

An approach that lends itself well to this is based on the marginal contribution to risk (MCR) measure, as described by Bystrik and Johnson (2005). By determining the MCR for each constituent, we can quantify their effect on the portfolio risk. Hence, positions that have a large positive MCR should ideally be reduced sooner, whilst those with a negative MCR should be preserved since they are actually helping offset the overall risk. These adjustments may then be applied to the constituent trading algorithm.

For example, Figure 12-12 illustrates how the target participation rate might be varied over time for a range of different risks. Initially, the target participation rates are raised for the constituents that have a positive MCR, whilst they are lowered for those with a negative one. As trading progresses, the urgency to trade those with a positive MCR decreases, whilst it becomes more important for the others to eatch up.

Also, notice that no adjustments are needed for the constituents that have a negligible contribution to risk. Alternatively, where two constituents with different liquidities both have a similar positive MCR, it may be more cost effective to trade the liquid one faster, since aggressive trading of the illiquid one could lead to prohibitive costs.

![](_page_26_Figure_1.jpeg)

Source: Bystrik and Johnson (2005) Reproduced with permission from Miletus Trading and The Trade

Figure 12-12 Participation rates based on marginal contribution to risk

# 12.6 Summary

- Portfolio trading provides a cost-effective means of trading whole baskets of assets.  $\mathbb{R}$ Significant risk reductions can be achieved by tracking and managing portfolio risk.
- Portfolio volatility is simply the standard deviation of the portfolio's returns. However,  $\mathbb{R}$ the relationship between overall risk and each portfolio constituent is non-linear. Each constituent's contribution to the overall risk depends on its proportion/weight in the portfolio, the variance of its returns and the covariance of its returns with all other assets in the portfolio.
- Diversification reduces portfolio risk, it occurs because the individual risks can offset  $\blacksquare$ one another. Simply increasing the number of assets can reduce the overall risk.
- Portfolio risk may also be decomposed into:  $\blacksquare$ 
  - Systematic benchmark (or market) risk
  - Non-systematic (or asset specific) risk, which may be reduced by diversification
- Portfolio managers may have additional trading goals, since they might also track risk in  $\blacksquare$ terms of other components, such as market, sector or country risk:
  - Cash balancing
  - Beta/Market neutrality

- Sector/Country neutrality
- \_ Minimising index tracking error
- Optimal portfolio trading lowers portfolio risk by reducing the positions of those assets  $\blacksquare$ that contribute the most. Note that the largest risk contributors will not necessarily be the orders for the riskiest assets, due to natural hedging.
- $\blacksquare$ Conventional trading algorithms may easily be used for trading portfolios. Though, dynamic algorithms will often lead to a shift in the portfolio composition since portfolio risk is not considered.
- Portfolio optimised algorithms need to track risk for the whole portfolio. There are two  $\blacksquare$ main ways of doing this:
  - Extending existing algorithms to incorporate portfolio models
  - Adopting an "algorithm of algorithms" to manage the portfolio trading requirements whilst individual algorithms are still used for each constituent order
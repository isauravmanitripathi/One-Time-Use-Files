# **Style Analysis**

Asset allocation is a major determinant of the return variation in fund portfolios. Hence, an investor who delegates portfolio management to a fund manager is particularly interested in the exposure to different types of asset classes. These exposures characterize the *style* of a fund. Fund names and self-declared fund objectives stated in the prospectus are typically not very informative about the style of mutual funds. Moreover, funds often change their style over time (see, e.g., [2]). Investors therefore turn to alternative ways to infer fund style. Return-based style analysis, introduced by Nobel Prize laureate William F. Sharpe ([5, 6]), determines the style of a fund by regressing the fund returns against the returns of a set of benchmark indices. These benchmark indices typically include style indices for large and small capitalization stocks, value and growth stocks, and bond indices. The coefficients on the style benchmark indices measure the exposures to the risks of these asset classes. Holdings-based style analysis infers the style of a fund directly from the characteristics of the individual positions of the fund portfolio. Style analysis can help characterize the asset allocation, evaluate the performance, and monitor the style consistency of a fund.

# **Return-based Style Analysis**

### *Methodology*

Factor models are a common way in finance to decompose the forces that drive security returns into common and firm-specific influences. A factor model differs from a simple regression exercise in that the residual firm-specific influence for one asset is assumed to be uncorrelated with the residual of all other assets. Hence, the correlation of asset returns is due to their exposure to common factors. Returnbased style analysis is a special case of a *linear factor model*. The factors are returns on different asset classes, such as returns on stocks of different style or bond-market indices, which are also called *style benchmark indices*. Owing to this property, returnbased style analysis belongs to the category of *asset class factor models*. The return of a fund, *ri,t* , is decomposed into two parts: the fraction that can be explained by a linear combination of the factors, and a residual term that is uncorrelated with the factors. The residual of fund *i*, *ei,t* , is uncorrelated with the residual of any other fund *j* , *ej,t* . Sharpe's ([5, 6]) return-based style analysis differs in a few ways from a standard factor model: (i) There is no intercept; (ii) the loadings on asset classes sum up to 1 to provide an intuitive interpretation as allocations to the asset classes; (iii) in its original form, and when applied to mutual funds, the coefficients are required to be nonnegative to capture short-selling constraints. This last constraint (2) to nonnegative exposures can be relaxed for hedge funds (see, e.g., [4]). The coefficients *bi,n* of equation (1) are estimated by minimizing the variance of the error terms *ei,t* subject to these constraints.

$$r_{i,t} = b_{i,1}f_{1,t} + b_{i,2}f_{2,t} + \cdots + b_{i,N}f_{N,t} + e_{i,t} \ (1)$$

s.t. 
$$b_{i,n} \ge 0$$
 for  $n = 1, 2, ..., N$  (2)

$$\sum_{n=1}^{N} b_{i,n} = \mathbf{1} \tag{3}$$

The coefficients *bi,n* measure the exposure to the *n*th factor, *fn,t* . These coefficients help the investor to identify the *effective style* of an active portfolio manager. Return-based style analysis extends easily to a multimanager portfolio.

The *R*<sup>2</sup> from the constrained regression (1–3) measures the fraction of the variation in fund returns that can be explained by the variation of the style benchmark indices.

$$R^2 = 1 - \frac{Var(e_i)}{Var(r_i)}\tag{4}$$

When the set of style benchmarks is accurately defined, the difference (1 − *R***<sup>2</sup>**) serves as a measure of active management. Stock picking, sector bets, and timing the exposure to different style benchmark indices results in lower *R*2. To penalize the inclusion of additional style benchmarks and to favor a parsimonious specification, the adjusted *R*<sup>2</sup> or Akaike information criterion can be used as a maximization criterion instead of *R*<sup>2</sup> (see, e.g., [1]).

## *Selection of Style Benchmark Indices*

The choice of asset classes determines the quality of any asset class factor model:

- 1. Sharpe [5] recommends using a set of asset classes that are (i) mutually exclusive, (ii) comprehensive; and (iii) where correlations between different asset classes are preferably low.
- 2. When return-based style analysis is used to evaluate fund performance, a few more properties are desirable: asset classes should represent strategies that can be implemented (i) at low cost and (ii) by a passive, value-weighted, and investable portfolio, that is, the strategy can be implemented ex ante.

As an example, average returns on peer groups violate this last property since the median fund manager is not known at the beginning of the evaluation period.

Common choices for equity mutual funds include style indices along the two dimensions size and value/growth. Value (growth) stocks are defined by high (low) book-to-market ratios. Chan et al. [3] show that the two dimensions size and book-tomarket capture the essential style of mutual funds. The key is a parsimonious set of asset classes that explains the time-series variation of different fund returns, not necessarily their average returns. A larger number of asset classes increases coverage, but, at the same time, reduces the reliability of the estimated exposures.

#### Use as a Performance Measure

A style-consistent portfolio manager allocates constant fractions  $b_{i,n}$  of his or her investments to a given asset class  $n$ . The portfolio manager's performance can thus be evaluated against a passive portfolio with the same fractions invested in the  $N$ benchmark indices. The difference

$$e_{i,t} = r_{i,t} - b_{i,1}f_{1,t} + b_{i,2}f_{2,t} + \dots + b_{i,N}f_{N,t} \quad (5)$$

using the optimal weights for the factors, measures the *selection* skills of a manager. The part of the return that is explained by the manager's effective style,  $b_{i,1}f_{1,t} + b_2f_{2,t} + \cdots + b_{i,N}f_{N,t}$ , is called the *style benchmark return.* The standard deviation of the selection component  $e_{i,t}$  measures the *style bench*mark tracking error.

In a return-based style analysis, the nonfactor residuals  $e_{i,t}$  are determined in-sample. To evaluate the performance of a fund manager, we need to determine his or her style and then compare the fund's

out-of-sample return to a passive style benchmark. This requires estimating first the coefficients  $\vec{b}_{i,t-1}$  in equation (1) using the returns from  $t - 1 - k$  through  $t-1$ , where k is the length of the estimation window. Then, the fund's *selection return* for period  $t$  is measured by the difference

$$r_{i,t} - [\widetilde{b}_{1,t-1}f_{1,t} + \widetilde{b}_{2,t-1}f_{2,t} + \cdots + \widetilde{b}_{N,t-1}f_{N,t}]$$
(6)

A common approach to monitor style changes of a fund is to apply a rolling window. Typical choices are a 36-month or 60-month window.

## **Holdings-based Style Analysis**

A critique of return-based style analysis is that it does not necessarily uncover what the fund actually holds but rather how it behaves, as expressed by Sharpe's often quoted words "if it walks like a duck and quacks like a duck, it is a duck." Take a position in a hybrid security such as convertible bonds. It likely shows up simultaneously in the loadings of a bond and equity style benchmark index. Furthermore, return-based style analysis reflects the average style over the estimation window and for funds with style drift the coefficient estimates become noisy and less meaningful.

Alternatively, investors may scrutinize fund portfolio holdings. Prominent data providers in the mutual fund industry, such as Morningstar and Lipper, use portfolio holdings to classify funds along the two dimensions size and value/growth. A holdings-based style analysis provides a snapshot of the current asset allocation. Information on portfolio positions is more difficult to collect in a timely manner than that on returns on funds and style benchmark indices, it often lacks uniformity, and processing the information is not an easy task. Holdings may also be affected by window dressing, a behavior of fund managers to adjust their portfolio positions before disclosure at the end of a quarter in an attempt to mimic stock picking skills.

#### References

[1] Ben Dor, A., Jagannathan, R. & Meier, I. (2003). Understanding mutual fund and hedge fund styles using returnbased style analysis, Journal of Investment Management  $1(1), 94-134.$ 

- [2] Brown, S.J. & Goetzmann, W.N. (1997). Mutual fund styles, *Journal of Financial Economics* **43**(3), 373–399.
- [3] Chan, L.K.C., Chen, H.-L. & Lakonishok, J. (2002). On mutual fund investment styles, *Review of Financial Studies* **15**(5), 1407–1437.
- [4] Fung, W. & Hsieh, D.A. (1997). Empirical characteristics of dynamic trading strategies: the case of hedge funds, *Review of Financial Studies* **10**(2), 275–302.
- [5] Sharpe, W.F. (1988). Determining a fund's effective asset mix, *Investment Management Review* **2**(6), 59–69.
- [6] Sharpe, W.F. (1992). Asset allocation: management style and performance measurement, *Journal of Portfolio Management* **18**(2), 7–19.

# **Related Articles**

**Capital Asset Pricing Model**; **Factor Models**; **Performance Measures**.

IWAN MEIER
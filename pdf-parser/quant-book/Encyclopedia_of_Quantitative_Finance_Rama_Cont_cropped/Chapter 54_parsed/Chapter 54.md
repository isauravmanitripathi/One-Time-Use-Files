# **Capital Asset Pricing Model**

The 1990 Nobel Prize winner William Sharpe [49, 50] introduced one cornerstone of the modern finance theory with his seminal capital asset pricing model (CAPM) for which Black [9], Lintner [35, 36], Mossin [43], and Treynor [54] proposed analogous and extended versions. He then proposed an answer to the financial theory's question about the uncertainty surrounding any investment and any financial asset. Indeed, financial theory raised the question of how risk impacts the fixing of asset prices in the financial market (*see* **Modern Portfolio Theory**), and William Sharpe proposed an explanation of the link prevailing between risky asset prices and market equilibrium. The CAPM therefore proposes a characterization of the link between the risk and return of financial assets, on one side, and market equilibrium, on the other side. This fundamental relationship establishes that the expected excess return of a given risky asset (*see* **Expectations Hypothesis**; **Risk Premia**) corresponds to the expected market risk premium (i.e., market price of risk) times a constant parameter called *beta* (i.e., a proportionality constant). The beta is a measure of the asset's relative risk and represents the asset price's propensity to move with the market. Indeed, the beta assesses the extent to which the asset's price follows the market trend simultaneously. Namely, the CAPM explains that, on an average basis, the unique source of risk impacting the returns of risky assets comes from the broad financial market to which all the risky assets belong and on which they are all traded. The main result is that the global risk of a given financial asset can be split into two distinct components, namely, a market-based component and a specific component. This specific component vanishes within well-diversified portfolios so that their global risk summarizes to the broad market influence.

## **Framework and Risk Typology**

The CAPM provides a foundation for the theory of market equilibrium, which relies on both the utility theory (*see* **Utility Theory: Historical Perspectives**) and the portfolio selection theory (*see* **Markowitz, Harry**). The main focus consists of analyzing and understanding the behaviors and transactions of market participants on the financial market. Under this setting, market participants are assumed to act simultaneously so that they can invest their money in only two asset classes, namely, risky assets, which are contingent claims, and nonrisky assets such as the risk-free asset. The confrontation between the supply and demand of financial assets in the market allows, therefore, for establishing an equilibrium price (for each traded asset) once the supply of financial assets satisfies the demand of financial assets. The uncertainty surrounding contingent claims is so that the general equilibrium theory explains risky asset prices by the equality between the supply and demand of financial assets. Under this setting, Sharpe [49, 50] assumes that the returns of contingent claims depend on each other only due to a unique exogenous market factor called the *market portfolio*. The other potential impacting factors are assumed to be random.

Hence, the CAPM results immediately from Markowitz [37, 38] setting since it represents an equilibrium model of financial asset prices (*see* **Markowitz, Harry**). Basically, market participants hold portfolios, which are composed of the riskfree asset and the market portfolio (representing the set of all traded risky assets). The market portfolio is moreover a mean–variance efficient portfolio, which is optimally diversified and satisfies equilibrium conditions (*see* **Efficient Markets Theory: Historical Perspectives**; **Efficient Market Hypothesis**; **Risk–Return Analysis**). Consequently, holding a risky asset such as a stock is equivalent to holding a combination of the risk-free asset and the market portfolio, the market portfolio being the unique market factor.

## **The Capital Asset Pricing Model**

Specifically, Sharpe [49, 50] describes the uncertainty underlying contingent claims with a one-factor model—the CAPM. The CAPM illustrates the establishment of financial asset prices under uncertainty and under market equilibrium. Such equilibrium is partial and takes place under a set of restrictive assumptions.

## *Assumptions*

1. Markets are *perfect* and without frictions: no tax, no transaction costs (*see* **Transaction Costs**), and no possibility of manipulating asset prices in the market (i.e., perfect market competition).

- 2. Information is instantaneously and perfectly available in the market so that investors simultaneously access the same information set without any cost.
- 3. Market participants invest over *one time period* so that we consider a one-period model setting.
- 4. Financial assets are infinitely divisible and liquid.
- 5. Lending and borrowing processes apply the riskfree rate (same rate of interest), and there is no short sale constraint.
- 6. Asset returns are normally distributed so that expected returns and corresponding standard deviations are sufficient to describe the assets' behaviors (i.e., their probability distributions). The Gaussian distribution assumption is equivalent to a quadratic utility setting.
- 7. Investors are risk averse and rational. Moreover, they seek to maximize the expected utility of their future wealth/of the future value of their investment/portfolio (see **Expected Util**ity Maximization: Duality Methods; Expected Utility Maximization; and the two-fund separation theorem of Tobin [52]).
- 8. Investors build *homogeneous expectations* about the future variation of interest rates. All the investors build the same forecasts about the expected returns and the variance-covariance matrix of stock returns. Therefore, there is a unique set of optimal portfolios. Basically, investors share the same opportunity sets, which means they consider the same sets of accessible and "interesting" portfolios.
- 9. The combination of two distinct and independent risk factors drives the evolution of any risky return over time, namely, the broad financial market and the fundamental/specific features of the asset under consideration. Basically, the risk level embedded in asset returns results from the trade-off between a market risk factor and an idiosyncratic risk factor.

The market risk factor is also called *systematic* risk factor and nondiversifiable risk factor. It represents a risk factor, which is common to any traded financial asset. Specifically, the market risk factor represents the global evolution of the financial market and the economy (i.e., trend of the broad market, business cycle), and impacts any risky asset. Indeed, it characterizes the systematic fluctuations in asset prices, which result from the broad market. In a complementary way, the specific risk factor is also called idiosyncratic risk factor, unsystematic risk factor, or diversifiable risk factor. It represents a component, which is peculiar to each financial asset or to each financial asset class (e.g., small or large caps). This specific component in asset prices has no link with the broad market. Moreover, the systematic risk factor is priced by the market, whereas the idiosyncratic risk factor is not priced by the market. Specifically, market participants ascribe a nonzero expected return to the market risk factor, whereas they ascribe a zero expected return to the specific risk factor. This feature results from the fact that the idiosyncratic risk can easily be mitigated within a well-diversified portfolio, namely, a portfolio with a sufficient number of heterogeneous risky assets so that their respective idiosyncratic risks cancel each other. Thus, a diversified portfolio's global risk (i.e., total variance) results only from the market risk (i.e., systematic risk).

## *CAPM* equation

Under the previous assumptions, the CAPM establishes a linear relationship between a portfolio's expected risk premium and the expected market risk premium as follows:

$$E[R_P] = r_f + \beta_P \times \left( E[R_M] - r_f \right) \tag{1}$$

where  $R_M$  is the return of the market portfolio;  $R_P$  is the return of portfolio  $P$  (which may also correspond to a given stock i);  $r_f$  is the risk-free interest rate;  $\beta_P$  is the beta of portfolio P; and  $E[R_M] - r_f$  is the market price of risk. The market portfolio  $M$ is composed of all the available and traded assets in the market. The weights of market portfolio's components are proportional to their corresponding market capitalization relative to the global broad market capitalization. Therefore, the market portfolio is representative of the broad market evolution and its related systematic risk. Finally,  $\beta_P$  is a systematic risk measure also called *Sharpe coefficient* since it quantifies the sensitivity of portfolio  $P$  or stock  $i$  to the broad market. Basically, the portfolio's beta is written as

$$\beta_P = \frac{\text{Cov}(R_P, R_M)}{\text{Var}(R_M)} = \frac{\sigma_{PM}}{\sigma_M^2} \tag{2}$$

where  $\text{Cov}(R_P, R_M) = \sigma_{PM}$  is the covariance between the portfolio's return and the market return,

![](_page_2_Figure_1.jpeg)

**Figure 1** Security market line

and Var*(RM )* = *σ*<sup>2</sup> *<sup>M</sup>* is the market return's variance over the investment period. In other words, beta is the risk of covariation between the portfolio's and the market's returns normalized by the market return's variance. Therefore, beta is a relative risk measure. Under the Gaussian return assumption, the standard deviation, or equivalently the variance, is an appropriate risk metric for measuring the dispersion risk of asset returns.

Therefore, under equilibrium, the portfolio's expected return *RP* equals the risk-free rate increased by a risk premium. The risk premium is a linear function of the systematic risk measure as represented by the beta and the market price of risk as represented by the expected market risk premium. Such a relationship is qualified as the security market line (SML; see Figure 1). Since idiosyncratic risk can be diversified away, only the systematic risk component in asset returns matters.a Intuitively, diversified portfolios cannot get rid of their respective dependency to the broad market. From a portfolio management prospect, the CAPM relationship then focuses mainly on diversified portfolios, namely, portfolios or stocks with no idiosyncratic risk.

It then becomes useless to keep any idiosyncratic risk in a given portfolio since such a risk is not priced by the market. The beta parameter becomes subsequently the only means to control the portfolio's risk since the CAPM relationship (1) establishes the premium investors require to bear the portfolio's systematic risk. Indeed, the higher the dependency on the broad financial market is, the greater the risk premium required by investors becomes. Consequently, the beta parameter allows investors to classify assets as a function of their respective systematic risk level (see Table 1).

Assets with negative beta values are usually specific commodity securities such as gold-linked assets. Moreover, risk-free securities such as cash or Treasury bills, Treasury bonds, or Treasury notes belong to the zero-beta asset class. Risk-free securities are independent from the broad market and exhibit a zero variance, or equivalently a zero standard deviation. However, the class of zero-beta securities includes also risky assets, namely, assets with a nonzero variance, which are not correlated with the market.

**Table 1** Systematic risk classification

| Beta level                 | Classification                                                    |
|----------------------------|-------------------------------------------------------------------|
| β > 1                      | Offensive, cyclical asset<br>amplifying market<br>variations      |
| 0 <β< 1                    | Defensive asset absorbing<br>market variations                    |
| β = 1                      | Market portfolio or asset<br>mimicking market<br>variations       |
| β = 0                      | Asset with no market<br>dependency                                |
| β lies between −1<br>and 1 | Asset with low systematic<br>risk level                           |
| β  lies above 1            | Asset with a higher risk level<br>than the broad market's<br>risk |

## **Estimation and Usefulness**

The CAPM theory gives a partial equilibrium relationship, which is assumed to be stable over time. However, how can we estimate such a linear relationship in practice and how do we estimate a portfolio's beta? How useful is this theory to market participants and investors?

### *Empirical Estimation*

As a first point, under the Gaussian return assumption, beta coefficients can be computed while considering the covariance and variance of asset returns over the one-period investment horizon (see equation (2)). However, this way of computing beta coefficients does not work in a non-Gaussian world. Moreover, beta estimates depend on the selected market index, the studied time window, and the frequency of historical data [8].

As a second point, empirical estimations of the CAPM consider historical data and select a stock market index as a proxy for the CAPM market portfolio. Basically, the CAPM is tested while running two possible types of regressions based on observed asset returns (i.e., past historical data). Therefore, stocks' and portfolios' betas are estimated by regressing past asset returns on past market portfolio returns. We therefore focus on the potential existence of a linear relationship between stock/asset returns and market returns. The first possible estimation method corresponds to the market model regression as follows:

$$R_{it} - r_f = \alpha_i + \beta_i \times (R_{Mt} - r_f) + \varepsilon_{it} \tag{3}$$

where *Rit* is the return of asset *i* at time *t*; *RMt* is the market portfolio's return at time *t*, namely, the systematic risk factor as represented by the chosen market benchmark, which is the unique explanatory factor; *rf* is the short-term risk-free rate; *εit* is a Gaussian white noise with a zero expectation and a constant variance *σεi* 2; *αi* is a constant trend coefficient; and the slope coefficient *βi* is simply the beta of asset *i*. The trend coefficient *αi* measures the distance of the asset's average return to the security market line, namely, the propensity of asset *i* to overperform (i.e., *αi >* 0) or to underperform (i.e., *αi <* 0) the broad market. In other words, *αi* is the difference between the expected return forecast provided by the security market line and the average return observed on past history. The error term *εit* represents the diversifiable/idiosyncratic risk factor describing the return of asset *i*. Therefore, *RMt* and *εit* are assumed to be independent, whereas (*εit*) are supposed to be mutually independent. Regression equation (3) is simply the ex-post form of the CAPM relationship, namely, the application of CAPM to past observed data [27].

The second method for estimating CAPM betas is the characteristic line so that we consider the following regression:

$$R_{it} = a_i + b_i \times R_{Mt} + \varepsilon_{it} \tag{4}$$

where *ai* and *bi* are constant trend and slope regression coefficients, respectively [51]. Moreover, such coefficients have to satisfy the following constraints:

$$\alpha_i = a_i - (1 - b_i) \times r_f \tag{5}$$

$$\beta_i = b_i \tag{6}$$

Regression equations (3) and (4) are only valid under the strong assumptions that *αi* and *βi* coefficients are stationary over time (e.g., time stability), and that each regression equation is a valid model over each one-period investment horizon.

In practice, the market model (3) is estimated over a two-year window of weekly data, whereas the characteristic line (4) is estimated over a fiveyear window of monthly data. Basically, the market model and the characteristic line use, as a market proxy, well-chosen stock market indexes such as NYSE index and S&P500 index, respectively, which are adapted to the frequency of the historical data under consideration.

## *Practical Use*

A sound estimation process is very important insofar as the CAPM relationship intends to satisfy investors' needs. From this viewpoint, the main goal of CAPM estimation is first to use past-history beta estimates to forecast future betas. Specifically, the main objective consists of extracting information from past history to predict future betas. However, extrapolating past beta estimates to build future beta values may generate estimation errors resulting from outliers due to firmspecific events or structural changes either in the broad market or in the firm [10].

Second, the CAPM is a benchmark tool helping investors' decision. Specifically, the SML is used to identify overvalued (i.e., above SML) and undervalued (i.e., below SML) stocks under a fundamental analysis setting. Indeed, investors compare observed stock returns with CAPM required returns and then assess the performance of the securities under consideration. Therefore, the CAPM relationship provides investors with a tool for investment decisions and trading strategies since it provides buy and sell signals, and drives asset allocation across different asset classes.

Third, the CAPM allows for building classical performance measures such as Sharpe ratio (*see* **Sharpe Ratio**), Treynor index, or Jensen's alpha (*see* **Style Analysis**; **Performance Measures**). Finally, the CAPM theory can be transposed to firm valuation insofar as the equilibrium value of the firm is the discounted value of its future expected cash flows. The discounting factor is just mitigated by one identified risk factor affecting equity [20, 29, 30, 47]. According to the theorem proposed by Modigliani and Miller [40–42] (*see* **Modigliani–Miller Theorem**), the cost of equity capital for an indebted firm corresponds to the risk-free rate increased by an operating risk premium (independent from the firm's debt) times a leverage-specific factor. The firm's risk is therefore measured by the beta of its equity (i.e., equity's systematic risk), which also depends on the beta of the firm's assets and on the firm's leverage. Indeed, the leverage increases the beta of equity in a perfect market and therefore increases the firm's risk, which represents the probability of facing a default situation. However, an optimal capital structure may result from market imperfections such as taxes, agency costs, bankruptcy costs, and information asymmetry among others. For example, there exists a trade-off between the costs incurred by a financial distress (i.e., default) and the potential tax benefits inferred from leverage (i.e., debt). Consequently, applying the CAPM to establish the cost of capital allows for budget planning and capital budgeting insofar as choosing an intelligent debt level allows for maximizing the firm value. Namely, there exists an optimal capital structure.

## **Limitations and Model Extensions**

However, CAPM is only valid under its strong seminal assumptions and exhibits a range of shortcomings as reported by Banz [6], for example. However, in practice and in the real financial world, many of these assumptions are violated. As a result, the CAPM suffers from various estimation problems that impact its efficiency. Indeed, Campbell *et al.* [14] show the poor performance of CAPM over the 1990s investment period in the United States. Such a result does have several possible explanations among which missing explanatory factors, heteroscedasticity in returns or autocorrelation patterns, time-varying or nonstationary CAPM regression estimates. For example, heteroscedastic return features imply that the static estimation of the CAPM is flawed under the classic setting (e.g., ordinary least squares linear regression). One has, therefore, to use appropriate techniques while running the CAPM regression under heteroscedasticity or non-Gaussian stock returns (see [7], for example, and *see also* **Generalized Method of Moments (GMM)**; **GARCH Models**).

### *General Violations*

Basic CAPM assumptions are not satisfied in the market and engender a set of general violations. First, lending and borrowing rates of interest are different in practice. Generally speaking, it is more expensive to borrow money than to lend money in terms of interest rate level. Second, the risk-free rate is not constant over time but one can focus on its arithmetic mean over the one-period investment horizon. Moreover, the choice of the risk-free rate employed in the CAPM has to be balanced with the unit-holding period under consideration. Third, transactions costs are often observed on financial markets and constitute part of the brokers' and dealers' commissions. Fourth, the market benchmark as well as stock returns are often nonnormally distributed and skewed [44]. Indeed, asset returns are skewed, leptokurtic [55], and they exhibit volatility clusters (i.e., time-varying volatility) and long memory patterns [2, 45]. Moreover, the market portfolio is assumed to be composed of all the risky assets available on the financial market so as to represent the portfolio of all the traded securities. Therefore, the broad market proxy or market benchmark should encompass stocks, bonds, human capital, real estate assets, and foreign assets (see the critique of Roll [46]). Fifth, financial assets are not infinitely divisible so that only fixed amounts or proportions of shares, stocks, and other traded financial instruments can be bought or sold.

Finally, the static representation of CAPM is at odds with the dynamic investment decision process. This limitation gives birth to multiperiodic extensions of CAPM. Extensions are usually called *intertemporal capital asset pricing models* (*ICAPMs*), and extend the CAPM framework to several unitholding periods (see [11, 39]).

### *Trading, Information, and Preferences*

Insider trading theory assumes that some market participants hold some private information. Specifically, information asymmetry prevails so that part of existing information is not available to all investors. Under such setting, Easley and O'Hara [22] and Wang [56] show that the trade-off between public and private information affects any firm's cost of capital as well as the related return required by investors. Namely, the existence of private information increases the return required by uninformed investors. Under information asymmetry, market participants exchange indeed information through observed trading prices [18]. Moreover, heterogeneity prevails across investors' preferences. Namely, they exhibit different levels of risk tolerance, which drives their respective investments and behaviors in the financial market. Finally, homogeneous expectations are inconsistent with the symmetry in the motives of transaction underlying any given trade. For a transaction to take place, the buy side has to meet the sell side. Indeed, Anderson *et al.* [4] show that heterogeneous beliefs play a nonnegligible role in asset pricing.

### *Nonsynchronous Trading*

Often, the market factor of risk and stocks are not traded at the same time on the financial market, specifically at the daily frequency level. This stylized fact engenders the so-called nonsynchronous trading problem. When the market portfolio is composed of highly liquid stocks, the nonsynchronism problem is reduced within the portfolio as compared to an individual stock. However, for less liquid stocks or less liquid financial markets, the previous stylized fact becomes an issue under the CAPM estimation setting. To bypass this problem, the asset pricing theory introduces one-lag systematic risk factor(s) as additional explanatory factor(s) to describe asset returns [13, 21, 48].

### *Missing Factors*

The poor explanatory power of the CAPM setting [14] comes from the lack of information describing stock returns in the market among others. The broad market's uncertainty is described by a unique risk factor: the market portfolio. Indeed, considering the market portfolio as the unique source of systematic risk, or equivalently as the unique systematic risk information source is insufficient. To bypass this shortcoming, a wide academic literature proposes to add complementary factors to the CAPM in order to better forecast stock returns (*see* **Arbitrage Pricing Theory**; **Predictability of Asset Prices**; **Factor Models**). Those missing factors are often qualified as asset pricing anomalies [5, 24, 26, 31]. Namely, the absence of key explanatory factors generates misestimations in computed beta values.

For example, Fama and French [25] propose to consider two additional factors such as the issuing firm's size and book-to-market characteristics. Further, Carhart [16] proposes to add a fourth complementary factor called *momentum*. The stock momentum represents the significance of recent past stock returns on the current observed stock returns. Indeed, investors' sentiment and preferences may explain expected returns to some extent. In this prospect, momentum is important since investors make the difference between poor and high performing stocks over a recent past history. More recently, Li [34] proposed two additional factors to the four previous ones, namely, the earnings-to-price ratio and the share turnover as a liquidity indicator. Indeed, Acharya and Pedersen [1], Brennan and Subrahmanyam [12], Chordia *et al.* [19], and Keene and Peterson [32] underlined the importance of liquidity as an explanatory factor in asset pricing. Basically, the trading activity impacts asset prices since the degree of transactions' fluidity drives the continuity of observed asset prices. In other words, traded volumes impact market prices, and the impact's magnitude depends on the nature of market participants [17].

### *Time-varying Betas*

Some authors like Tofallis [53] questioned the soundness of CAPM while assessing and forecasting stock returns' performance. Indeed, the CAPM relationship is assumed to remain stable over time insofar as it relies on constant beta estimates over each unitholding period (i.e., reference time window). Such a process assumes implicitly that beta estimates remain stable in the near future so that ex-post beta estimates are good future risk indicators. However, time instability is a key feature of beta estimates. For example, Gen¸cay *et al.* [28] and Koutmos and Knif [33] support time-varying betas in CAPM estimation.

Moreover, CAPM-type asset pricing models often suffer from error-in-variables problems coupled with time-varying parameters features [15]. To solve such problems, authors like Amman and Verhoeven [3], Ellis [23], and Wang [57] among others advocate using conditional versions of the CAPM. Moreover, Amman and Verhofen [3] and Wang [57] show the efficiency of conditional asset pricing models and exhibit the superior performance of the conditional CAPM setting as compared to other asset pricing models.

## **End Notes**

a*.* Specifically, the systematic risk represents that part of returns' global risk/variance, which is common to all traded assets, or equivalently, which results from the broad market's influence.

## **References**

- [1] Acharya, V.V. & Pedersen, L.H. (2005). Asset pricing with liquidity risk, *Journal of Financial Economics* **77**(2), 375–410.
- [2] Adrian, T. & Rosenberg, J. (2008). *Stock Returns and Volatility: Pricing the Short-run and Long-run Components of Market Risk*, Staff Report No 254, Federal Reserve Bank of New York.
- [3] Amman, M. & Verhofen, M. (2008). Testing conditional asset pricing models using a Markov chain Monte Carlo approach, *European Financial Management* **14**(3), 391–418.
- [4] Anderson, E.W., Ghysels, E. & Juergens, J.L. (2005). Do heterogeneous beliefs matter for asset pricing? *Review of Financial Studies* **18**(3), 875–924.
- [5] Avramov, D. & Chordia, T. (2006). Asset pricing models and financial market anomalies, *Review of Financial Studies* **19**(3), 1001–1040.
- [6] Banz, R. (1981). The relationship between return and market value of common stocks, *Journal of Financial Economics* **9**(1), 3–18.
- [7] Barone Adesi, G., Gagliardini, P. & Urga, G. (2004). Testing asset pricing models with coskewness, *Journal of Business and Economic Statistics* **22**(4), 474–495.
- [8] Berk, J. & DeMarzo, P. (2007). *Corporate Finance*, Pearson International Education, USA.
- [9] Black, F. (1972). Capital market equilibrium with restricted borrowing, *Journal of Business* **45**(3), 444–455.
- [10] Bossaerts, P. & Hillion, P. (1999). Implementing statistical criterion to select return forecasting models: what do we learn? *Review of Financial Studies* **12**(2), 405–428.

- [11] Breeden, D. (1979). An intertemporal capital asset pricing model with stochastic consumption and investment opportunities, *Journal of Financial Economics* **7**(3), 265–296.
- [12] Brennan, M.J. & Subrahmanyam, A. (1996). Market microstructure and asset pricing: on the compensation for illiquidity in stock returns, *Journal of Financial Economics* **41**(3), 441–464.
- [13] Busse, J.A. (1999). Volatility timing in mutual funds: evidence from daily returns, *Review of Financial Studies* **12**(5), 1009–1041.
- [14] Campbell, J.Y., Lettau, M., Malkiel, B.G. & Xu, Y. (2001). Have individual stocks become more volatile? An empirical exploration of idiosyncratic risk, *Journal of Finance* **56**(1), 1–43.
- [15] Capiello, L. & Fearnley, T.A. (2000). *International CAPM with Regime Switching GARCH Parameters*. Graduate Institute of International Studies, University of Geneva. Research Paper No 17.
- [16] Carhart, M.M. (1997). On persistence in mutual fund performance, *Journal of Finance* **52**(1), 57–82.
- [17] Carpenter, A. & Wang, J. (2007). Herding and the information content of trades in the Australian dollar market, *Pacific-Basin Finance Journal* **15**(2), 173–194.
- [18] Chan, H., Faff, R., Ho, Y.K. & Ramsay, A. (2006). Asymmetric market reactions of growth and value firms with management earnings forecasts, *International Review of Finance* **6**(1–2), 79–97.
- [19] Chordia, T., Roll, R. & Subrahmanyam, A. (2001). Trading activity and expected stock returns, *Journal of Financial Economics* **59**(1), 3–32.
- [20] Cohen, R.D. (2008). *Incorporating default risk into Hamada's equation for application to capital structure*, *Wilmott Magazine* March, 62–68.
- [21] Dimson, E. (1979). Risk measurement when shares are subject to infrequent trading, *Journal of Financial Economics* **7**(2), 197–226.
- [22] Easley, D. & O'Hara, M. (2004). Information and the cost of capital, *Journal of Finance* **59**(4), 1553–1583.
- [23] Ellis, D. (1996). A test of the conditional CAPM with simultaneous estimation of the first and second conditional moments, *Financial Review* **31**(3), 475–499.
- [24] Faff, R. (2001). An Examination of the Fama and French three-factor model using commercially available factors, *Australian Journal of Management* **26**(1), 1–17.
- [25] Fama, E.F. & French, K.R. (1993). Common risk factors in the returns on stocks and bonds, *Journal of Financial Economics* **33**(1), 3–56.
- [26] Fama, E.F. & French, K.R. (1996). Multi-factor explanations of asset pricing anomalies, *Journal of Finance* **51**(1), 55–84.
- [27] Friend, I. & Westerfield, R. (1980). Co-skewness and capital asset pricing, *Journal of Finance* **35**(4), 897–913.
- [28] Gen¸cay, R., Sel¸cuk, F. & Whitcher, B. (2003). Systematic risk and timescales, *Quantitative Finance* **3**(1), 108–116.
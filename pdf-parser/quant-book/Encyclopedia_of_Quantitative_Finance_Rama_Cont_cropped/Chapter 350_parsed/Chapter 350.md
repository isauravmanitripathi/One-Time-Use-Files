# **Factor Models**

Factor models of security returns decompose the random return on each of a cross section of assets into factor-related and asset-specific returns. Letting  $r$  denote the vector of random returns on  $n$  assets, and assuming  $k$  factors, a factor decomposition has the form

$$r = a + Bf + \varepsilon \tag{1}$$

where B is an  $n \times k$ -matrix of factor betas, f is a random k-vector of factor returns, and  $\varepsilon$  is an *n*-vector of asset-specific returns. The  $n$ -vector of coefficients *a* is set so that  $E[\varepsilon] = 0$ . By defining *B* as the least squares projection  $B = cov(r, f)C_f^{-1}$ , it follows that  $cov(f, \varepsilon) = 0^{k \times n}$ .

The factor decomposition (1) puts no empirical restrictions on returns beyond requiring that the means and variances of  $r$  and  $f$  exist. So in this sense it is empty of empirical content. To add empirical structure, it is commonly assumed that the assetspecific returns  $\varepsilon$  are cross-sectionally uncorrelated,  $E[\varepsilon \varepsilon'] = D$  where D is a diagonal matrix. This implies that the covariance matrix of returns can be written as the sum of a matrix of rank  $k$  and a diagonal matrix:

$$cov(r, r') = Bcov(f, f')B' + D \tag{2}$$

This is called a *strict factor model*. Without loss of generality, one can assume that  $cov(f, f')$  has rank  $k$ , since otherwise one of the factors can be removed (giving a  $k-1$  factor model) without affecting the fit of the model.

An important (and often troublesome) feature of factor models is their rotational indeterminacy. Let  $L$ denote any nonsingular  $k \times k$ -matrix and consider the set of factors  $f^* = Lf$  and factor betas  $B^* = L^{-1}B$ . Note that  $f^*, B^*$  can be used in place of  $f, B$  since only their matrix product affects returns and the linear "rotation"  $L$  disappears from this product. This means that factors  $f$  and associated factor betas  $B$  are only defined up to a  $k \times k$  linear transformation. In order to empirically identify the factor model, one can set the covariance matrix of the factors equal to an identity matrix,  $E[ff'] = I_k$ , without loss of generality.

# **Approximate Factor Models**

Security market returns have strong comovements, but the assumption that returns obey a strict factor model is easily rejected. In practice, for any reasonable value of  $k$ , there will be at least some discernible positive correlations between the assetspecific returns of at least some assets. An approximate factor model (originally developed by Chamberlain and Rothschild [7]) weakens the strict factor model of exactly zero correlations between all asset-specific returns. Instead, it assumes that there is a large number,  $n$ , of assets and the proportion of the correlations that are nonnegligibly different from zero is close to zero. This condition is formalized as a bound on the eigenvalues of the asset-specific return covariance matrix:

$$\lim_{n \to \infty} \max \, eigval[cov(\varepsilon, \varepsilon')] < c \tag{3}$$

for some fixed  $c < \infty$ . Crucially, this condition implies that asset-specific returns are *diversifiable risk* in the sense that any well-spread portfolio  $w$  will have asset-specific variance near zero:

$$\lim_{n \to \infty} w' \operatorname{cov}(\varepsilon, \varepsilon') w = 0 \text{ for any } w$$
  
such that 
$$\lim_{n \to \infty} w' w = 0 \tag{4}$$

Note that an approximate factor model uses a "large  $n$ " modeling approach; the restrictions on the covariance matrix need only hold approximately as the number of assets  $n$  grows large.

Letting  $V = cov(\varepsilon, \varepsilon')$  which is no longer diagonal, and choosing the rotation so that  $cov(f, f') = I$ , we can write the covariance matrix of returns as

$$cov(r, r') = BB' + V \tag{5}$$

In addition to equation (4), it is appropriate to impose the condition that  $\lim \min \text{eigval}[BB']$  $=\infty$ . This ensures that each of the k factors represents a pervasive source of risk in the cross section of returns.

## **Statistical Factor Models**

Financial researchers differentiate between characteristic-based, macroeconomic, and statistical factor models [2]). In a characteristic-based model, the factor betas of asset are tied to observable characteristics of the securities, such as company size or the book-to-price ratio, or the industry categories to which each security belongs. In macroeconomic factor models, the factors are linked to the innovations in observable economic time series such as inflation and unemployment. In a statistical factor model, neither factors nor betas are tied to any external data sources and the model is identified from the covariances of asset returns alone.

Recall the convenient rotation  $E[ff'] = I$  that allows us to write the strict factor model  $(1)$  as

$$cov(r, r') = BB' + D \tag{6}$$

Assuming that the cross section of return is multivariate normal and independent and identically distributed (i.i.d.) through time, the sample covariance matrix  $\widehat{cov}(r, r')$  has a Wishart distribution. Imposing the strict factor model assumption  $(6)$  on the true covariance matrix, it is possible to estimate the set of parameters  $B, D$  by maximum likelihood. This maximum likelihood problem requires high-dimensional nonlinear maximization: there are  $nK + n$  parameters to estimate in  $B, D$ . There is also an inequality constraint on the maximization problem: the diagonal elements of  $D$  must be nonnegative, since they represent variances. The solution to the maximum likelihood problem yields estimates of  $B$  and  $D$ , which correspond to the systematic and unsystematic risk measures. It is often the case that estimates of the time series of factors,  $f$ , are of interest. These are called *factor scores* in the statistical literature and can be obtained through cross-sectional generalized least squares (GLS) regressions of  $r$  on  $\widehat{B}$ 

$$\widehat{f}_t = (\widehat{B}\widehat{D}^{-1}\widehat{B})^{-1}\widehat{B}\widehat{D}^{-1}r_t \tag{7}$$

See [5] for a review of the various iterative algorithms, which can be used to numerically solve the maximum likelihood factor analysis problem and estimate the factor scores. Roll and Ross [25] provide an early empirical application to equity returns data.

The first  $k$  eigenvectors of the return covariance matrix scaled by the square roots of their respective eigenvalues are called the  $k$  principal components of the covariance matrix. A restrictive version of the strict factor model is the *scalar fac*tor model, given by equation (2) plus the scalar matrix condition  $D = \sigma_s^2 I$ . Under the assumption of a scalar factor model, the maximum likelihood problem simplifies, and the principal components are the maximum likelihood estimates of the factor beta matrix  $B$  (the arbitrary choice of rotation is slightly different in this case). This provides a quick and simple alternative to maximum likelihood factor analysis, under the restrictive assumption  $D = \sigma_{\rm c}^2 I.$ 

### **Asymptotic Principal Components**

The maximum likelihood method of factor model estimation relies on a strict factor model assumption and a time-series sample which is large relative to the number of assets in the cross section. Standard principal components require the even stronger condition of a scalar factor model. Neither method is well suited for asset returns where the cross section tends to be very large. Connor and Korajczyk [11] develop an alternative method called asymptotic principal components, building on the approximate factor model theory of Chamberlain and Rothschild [7]. Connor and Korajczyk analyze the eigenvector decomposition of the  $T \times T$  cross product matrix of returns rather than that of the  $n \times n$  covariance matrix of returns. They show that given a large cross section, the first  $k$  eigenvectors of this cross-product matrix provide consistent estimates of the  $k \times T$  matrix of factor returns. Stock and Watson [31] extend the theory to allow both large time series and large crosssectional samples, time-varying factor betas, and provide a quasi-maximum likelihood interpretation of the technique. Bai [3] analyzes the large-sample distributions of the factor returns and factor beta matrix estimates in a generalized version of this approach.

#### **Macroeconomic Factor Models**

The rotational indeterminacy in statistical factor models makes these unsuitable for the application of factor models to many research problems. Statistical factor models do not allow the analyst to assign meaningful labels to the factors and betas; one can identify the  $k$  pervasive risks in the cross section of returns, but not what these risks represent in terms of economic and financial theory.

One approach to making the factor decomposition more interpretable is to rotate the statistical factors so that the rotated factors are maximally correlated with prespecified macroeconomic factors. If  $f_t$  is a *k*-vector of statistical factors and *mt* is a *k*-vector of macroeconomic innovations, we can regress the macroeconomic factors on the statistical factors:

$$m_t = \Pi f_t + \eta_t \tag{8}$$

As long as has rank *k*, the span of the rotated factors, *ft* , is the span of the original statistical factors, *ft* . However, the rotated factors can now be interpreted as the return factors that are correlated with the specified macroeconomic series. With this rotation the new factors are no longer orthogonal, in general. This approach is described in [12].

Alternatively, one can work with the prespecified macroeconomic series directly. Chan *et al.* [8] and Chen *et al.* [9] develop a macroeconomic factor model in which the factor innovations *f* are observed directly (using innovations in economic time series) and the factor betas are estimated via time-series regression of each asset's return on the time series of factors. They begin with the standard description of the current price of each asset, *pit,* as the present discounted value of its expected cash flows:

$$p_{it} = \sum_{s=1}^{\infty} \frac{E[c_{it}]}{(1+\rho_{st})^s}$$
(9)

where *ρst* is the discount rate at time *t* for expected cash flows at time *t* + *s.* Chen, Roll, and Ross note that the common factors in returns must be variables which cause pervasive shocks to expected cash flows *E*[*cit*] and/or risk-adjusted discount rates *ρst .* They propose inflation-, interest-rate-, and business-cyclerelated variates to capture these common factors. Shanken and Weinstein [29] find that empirically the model lacks robustness in that small changes in the included factors or the sample period have large effects on the estimates. Connor [10] argues that although macroeconomic factor models are theoretically attractive since they provide a deeper explanation for return comovement than statistical factor models, their empirical fit is substantially weaker than statistical and characteristic-based models. Vassalou [33] argues, on the other hand, that the ability of the Fama–French model (see below) to explain the cross section of mean returns can be attributed to the fact that Fama–French factors provide good proxies for macroeconomic factors.

# **Characteristic-based Factor Models**

A surprisingly powerful method for factor modeling of security returns is the characteristic-based factor model. Rosenberg [26] was the first to suggest that suitably scaled versions of standard accounting ratios (book-to-price ratio, market value of equity) could serve as factor betas. Using these predefined betas, he estimates the factor realizations *ft* by cross-sectional regression of time-*t* asset returns on the predefined matrix of betas.

In a series of very influential papers, Fama and French [16, 17, 18] propose a two-stage method for estimating characteristic-based factor models. In the first stage, they sort assets into fractile portfolios based on book-to-price and market value characteristics. They use the differences between returns on the top and bottom fractile portfolios as proxies for the factor returns. They also include a market factor proxied by the return on a capitalization-weighted market index. In the second stage, the factor betas of portfolios and/or assets are estimated by time-series regression of asset returns on the derived factors. Carhart [6] and Jegadeesh and Titman [22, 23] show that the addition of a momentum factor (proxied by high 12-month return minus low 12-month return) adds explanatory power to the Fama–French threefactor model, both in terms of explaining comovements and mean returns. Goyal and Santa-Clara [19] and Ang *et al.* [1, 2] also find evidence for an ownvolatility-related factor, for explaining both return comovements and mean returns.

# **Industry–Country Components Models**

One of the most empirically powerful factor decompositions for equity returns is an error-components model using industry affiliations. This involves setting the factor beta matrix equal to zero/one dummies, with row *i* containing a one in the *j* th column if and only if firm *i* belongs to industry *j* . This is the simplest type of characteristic-based factor model of equity returns.

The first statistical factor is dominant in equity returns, accounting for 80–90% of the explanatory power in a multifactor model. The standard specification of an error-components model does not isolate the "first" factor since its influence is spread across the factors. Heston and Rouwenhorst [20] describe an alternative specification in which this factor is separated from the  $k$  industry factors. They add a constant to the model, so that the expanded set of factors  $k + 1$  is not directly identified (this lack of identification is sometimes called the dummy variable trap, referring to a model that includes a full set of zero-one dummies plus a constant). Heston and Rouwenhorst, impose an adding-up restriction on the estimated  $k+1$  factors; the set of industry factors must sum to zero. This adding-up restriction on the factors restores statistical identification to the model, requiring constrained least squared in place of standard least squares estimation. It also provides a useful interpretation of the estimated factors: the factor associated with the constant term is the "marketwide" or "first" factor, and the factors associated with the industry dummies are the extra-market industry factors. This specification has been widely adopted in the literature.

Heston and Rouwenhorst's adding-up condition is particularly useful in a multicountry context. It allows one to include an overlapping set of country and industry dummies without encountering the problem of the dummy variable trap. Including a constant, an international industry-country factor model must impose adding-up conditions both on the estimated industry factors and on the estimated country factors. This type of country-industry specification is useful, for example, in measuring the relative contribution of cross-border and national influences to return comovements; see, for example, [21].

## **Determining the Number of Factors**

In the case of maximum likelihood estimation of a strict factor model, it is possible to test for the correct number of factors by comparing the likelihood of the model with k factors to that of a  $k + 1$  factor model. Under the standard assumptions, for large timeseries samples, the ratio of the log likelihoods has an approximate chi-squared distribution. There are drawbacks to this test in the context of asset returns data and its performance has been problematic; see, for example, [14, 15], and [28], in which the test is found to be unreliable. The test may rely too strongly on the assumption of a strict factor model (an exactly diagonal covariance matrix of asset-specific returns), which is at best a convenient fiction in the case of asset returns. Also, it tests the hypothesis that the correct number of factors has been prespecified, rather than optimally determining the best number of factors to use.

Connor and Korajczyk [13] derive a test for the number of factors, which is robust to having an approximate, rather than strict factor model. It is based on the decline in average idiosyncratic variance as additional factors are added.

Bai and Ng [4] take a different approach to the factor-number decision. They view the choice of the number of factors as a model selection problem. and build on the Akaike and Bayesian information criterea (BIC) information criteria-based tests for model selection. Bai and Ng compute the average asset-specific variance (both across time and across securities) in a model with  $k$  factors:

$$\sigma_{\varepsilon}^{2}(k) = \frac{1}{nT} \sum_{i=1}^{n} \sum_{t=1}^{T} \widehat{\varepsilon}_{it}^{2} \qquad (10)$$

The Bai-Ng procedure involves choosing  $k$  to minimize a degrees-of-freedom adjusted variant of average asset-specific variance:

$$k^* = \arg\min \sigma_s^2 + kg(n, T) \tag{11}$$

where the penalty function  $g(n, T)$  serves to compensate for the lost degrees of freedom when estimating the model with more factors.

#### **Factor Beta Pricing Theory**

A central concern in asset pricing theory is the determination of asset risk premia and their connection to sources of pervasive risk. Factor models have been central to this research area. In a factor beta pricing model, the expected return of each asset equals the risk-free return plus a linear combination of the factor betas of the assets, with the linear weights (factor risk premia) constant across securities:

$$E[r] = 1^n r_0 + B\pi \tag{12}$$

where  $r_0$  is the risk-free return and  $\pi$  is a k-vector of factor risk premia. Important special cases include the capital asset pricing model [30] (Treynor, J.L. (1961). Toward a Theory of Market Value of Risky Assets.(unpublished working paper).) [32], the arbitrage pricing theory [27], the Fama-French model [17, 18], and [24] intertemporal capital asset pricing model.

# **Acknowledgments**

Author Korajczyk would like to acknowledge financial support from the Zell Center for Risk Research and the Jerome Kenney Fund.

# **References**

- [1] Ang, A., Hodrick, R.J., Xing, Y. & Zhang, X. (2006). The cross-section of volatility and expected returns, *Journal of Finance* **61**, 259–299.
- [2] Ang, A., Hodrick, R.J., Xing, Y. & Zhang, X. (2009). High idiosyncratic risk and low returns: international and further U.S. evidence, *Journal of Financial Economics* **91**, 1–23.
- [3] Bai, J. (2003). Inferential theory for factor models of large dimension, *Econometrica* **71**, 135–171.
- [4] Bai, J. & Ng, S. (2002). Determining the number of factors in approximate factor models, *Econometrica* **70**, 191–221.
- [5] Basilevsky, A. (1994). *Statistical Factor Analysis and Related Methods*, Wiley, New York.
- [6] Carhart, M.M. (1997). On persistence in mutual fund performance, *Journal of Finance* **52**, 57–82.
- [7] Chamberlain, G. & Rothschild, M. (1983). Arbitrage, factor structure and mean–variance analysis in large asset markets, *Econometrica* **51**, 1305–1324.
- [8] Chan, K.C., Chen, N.-F. & Hsieh, D.A. (1985). An exploratory investigation of the firm size effect, *Journal of Financial Economics* **14**, 451–471.
- [9] Chen, N.-F., Roll, R. & Ross, S.A. (1986). Economic forces and the stock market, *Journal of Business* **59**, 383–403.
- [10] Connor, G. (1995). The three types of factor models: a comparison of their explanatory power, *Financial Analysts Journal* **51**, 42–46.
- [11] Connor, G. & Korajczyk, R.A. (1986). Performance measurement with the arbitrage pricing theory: a new framework for analysis, *Journal of Financial Economics* **15**, 373–394.
- [12] Connor, G. & Korajczyk, R.A. (1991). The attributes, behavior, and performance of U.S. mutual funds, *Review of Quantitative Finance and Accounting* **1**, 5–26.
- [13] Connor, G. & Korajczyk, R.A. (1993). A test for the number of factors in an approximate factor model, *Journal of Finance* **48**, 1263–1291.
- [14] Conway, D.A. & Reinganum, M.R. (1988). Stable factors in security returns: identification using crossvalidation, *Journal of Business & Economic Statistics* **6**, 1–15.
- [15] Dhrymes, P.J., Friend, I. & Gultekin, N.B. (1984). A critical reexamination of the empirical evidence on the arbitrage pricing theory, *Journal of Finance* **39**, 323–246.
- [16] Fama, E.F. & French, K.R. (1992). The cross-section of expected stock returns, *Journal of Finance* **47**, 427–465.

- [17] Fama, E.F. & French, K.R. (1993). Common risk factors in the returns on stocks and bonds, *Journal of Financial Economics* **33**, 3–56.
- [18] Fama, E.F. & French, K.R. (1996). Multifactor explanations of asset pricing anomalies, *Journal of Finance* **51**, 55–84.
- [19] Goyal, A. & Santa-Clara, P. (2003). Idiosyncratic risk matters, *Journal of Finance* **58**, 975–1007.
- [20] Heston, S.L. & Rouwenhorst, K.G. (1994). Does industrial structure explain the benefits of international diversification? *Journal of Financial Economics* **36**, 3–27.
- [21] Hopkins, P.J.B. & Miller, C.H. (2001). *Country, Sector and Company Factors in Global Equity Models*, The Research Foundation of AIMR and the Blackwell Series in Finance, Charlottesvile, VA.
- [22] Jegadeesh, N. & Titman, S. (1993). Returns to buying winners and selling losers: implications for stock market efficiency, *Journal of Finance* **48**, 65–91.
- [23] Jegadeesh, N. & Titman, S. (2001). Profitability of momentum strategies: an evaluation of alternative explanations, *Journal of Finance* **56**, 699–718.
- [24] Merton, R.C. (1973). An intertemporal capital asset pricing model, *Econometrica* **41**, 867–887.
- [25] Roll, R. & Ross, S. (1980). An empirical investigation of the arbitrage pricing theory, *Journal of Finance* **35**, 1073–1103.
- [26] Rosenberg, B. (1974). Extra-market components of covariance in security returns, *Journal of Financial and Quantitative Analysis* **9**, 263–274.
- [27] Ross, S. (1976). The arbitrage theory of capital asset pricing, *Journal of Economic Theory* **13**, 341–360.
- [28] Shanken, J. (1987). Nonsynchronous data and the covariance-factor structure of returns, *Journal of Finance* **42**, 221–231.
- [29] Shanken, J. & Weinstein, M.I. (2006). Economic forces and the stock market revisited, *Journal of Empirical Finance* **13**, 129–144.
- [30] Sharpe, W.F. (1964). Capital asset prices: a theory of market equilibrium under conditions of risk, *Journal of Finance* **19**, 425–442.
- [31] Stock, J.H. & Watson, M.W. (2002). Macroeconomic forecasting using diffusion indexes, *Journal of Business and Economic Statistics* **20**, 147–162.
- [32] Treynor, J.L. (1999). Towards a theory of market value of risky assets, in *Asset Pricing and Portfolio Performance: Models, Strategy, and Performance Metrics*, R.A. Korajczyk, ed, Risk Publications, London.
- [33] Vassalou, M. (2003). News related to future gdp growth as a risk factor in equity returns, *Journal of Financial Economics* **68**, 47–73.

# **Related Articles**

#### **Capital Asset Pricing Model**; **Style Analysis**.

GREGORY CONNOR & ROBERT KORAJCZYK
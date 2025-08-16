# **Arbitrage Pricing Theory**

The arbitrage pricing theory (APT) was introduced by Ross [10] as an alternative to the capital asset pricing model (CAPM). The model derives a multibeta representation  $of$  expected returns relative to a set of  $K$  reference variables under assumptions that may be described roughly as follows:

- 1. There exists no mean-variance arbitrage.
- The asset returns follow a  $K$ -factor model. 2.
- The reference variables and the factors are non-3. trivially correlated.<sup>a</sup>

The first assumption implies that there are no portfolios with arbitrarily large expected returns and unit variance. The second one assumes that the returns are a function of  $K$  factors common to all assets, and noise term specific to each asset. The third one identifies the sets of reference variables for which the model works.

The model predictions may have approximation errors. However, these errors are small for each portfolio that its weight on each asset is small (a welldiversified portfolio).

Early versions of the model unnecessarily assumed that the factors are equal to the reference variables. The extension of the model to arbitrary sets of reference variables comes at the cost of increasing the bound on the approximation errors by a multiplicative factor. However, when focusing on pricing of only well-diversified portfolios, this seems to be unimportant because each of the approximation error is small and a multiplicative factor does not change much the size of the error.

#### **Factor Representation**

Consider a finite sequence of random variables  $\{Z_i; i = 1, \ldots, N\}$  with finite variances that will be held fixed throughout the article. It is regarded as representing the excess<sup> $b$ </sup> returns of a given set of assets (henceforth "assets  $i = 1, \ldots, N$ "). Without any further assumptions

$$Z_i = b_{i,0} + \sum_{k=1}^K b_{i,k} f_k + e_i; \ i = 1, \dots, N$$

where  $f_1, \ldots, f_K$  are the first K factors in the principal component analysis (PCA) of the sequence

 $\{Z_i; i = 1, \ldots, N\}$ . The  $b_{i,k}$  are the factor loadings and the  $e_i$  are the residuals from projecting the  $Z_i$  on the factors.

The  $K + 1$  largest eigenvalue of the covariance matrix of the  $Z_i$ , denoted by  $\Lambda^2(K)$ , is interpreted as a measure of the extent to which our sequence of assets has a  $K$ -factor representation. The PCA selects the  $f_k$  so that  $\Lambda^2(K)$  is minimized. In addition,  $\Lambda^2(K)$  is also the largest eigenvalue of the covariance matrix of the  $e_i$ .

#### **Diversified Portfolios**

Let  $w \in R^N$  be a portfolio in assets  $i = 1, \ldots, N$ . Its excess return is

$$Z_w = \sum_{i=1}^N w_i Z_i.$$

Its representation as a linear function of the factors is

$$Z_w = b_{w,0} + \sum_{k=1}^{K} b_{w,k} f_k + e_u$$

where  $b_{w,k} = \sum_{i=1}^{N} w_i b_{i,k}$  are the factor loadings and  $e_w = \sum_{i=1}^N w_i \overline{e_i}$  is the residual which satisfies

$$\operatorname{Var}[e_w] < \Lambda^2(K) \sum_{i=1}^N w_i^2$$

A portfolio  $w = (w_1, \ldots)$  is called an (approximate) well-diversified portfolio if

$$\sum_{i=1}^{N} w_i^2 \approx 0 \tag{1}$$

Intuitively, a well-diversified portfolio is one with a large number of assets that has a small weight in many of them, and, in addition, there is no single asset for which the weight is not small.

The variance of the residual of a well-diversified portfolio is small and thus its excess return is approximately a linear function of the factors; that is,

$$Z_w \approx b_{w,0} + \sum_{k=1}^K b_{w,k} f_k \tag{2}$$

Although  $\sum_{i=1}^{N} w_i^2 \approx 0$ ,  $Z_w$  may not be small. For example, let  $w_i = 1/N$ , then we have  $\sum_{i=1}^N w_i^2 =$  $1/N$ , and  $b_{w,k} = (1/N) \sum_{k=1}^{K} b_{i,k}$ 

A further discussion on well-diversified portfolios can be found in  $[4]$ .

## **Multibeta Representation**

Throughout the article we consider a fixed set of *K reference variables* {*g*1*,...,gK*} with respect to which we derive an approximate *multibeta representation* defined as

$$E[Z_i] = \sum_{k=1}^{K} B_{i,k} \lambda_k + \rho_i \tag{3}$$

where

$$B_{i,k} = \text{Cov}(Z_i, g_k) \tag{4}$$

This means that

$$E[Z_i] \approx \sum_{k=1}^{K} B_{i,k} \lambda_k \tag{5}$$

where *ρi* is the approximation error in pricing asset *i*. The sum of the squares of these approximation errors, that is,

$$\sum_{i=1}^{N} \rho_i^2 = \Omega^2 \tag{6}$$

determines the quality of the approximation.

## **The APT Bound**

Huberman [3] showed that is finite for an infinite sequence of excess returns but did not derive a bound. Such bounds were derived by Chamberlain & Rothschild [1], in the case where the reference variables are the factors and by Reisman [7], in the general case. Reisman showed that

$$\Omega \le \Lambda S \Phi \Psi V \tag{7}$$

where 2(K) is the *K* + 1 largest eigenvalue of the covariance matrix of the *Zi*; *S* is the lowest upper bound on expected excess return among portfolios with unit variance; <sup>2</sup> = 1 − *R*<sup>2</sup> of the regression of the tangency portfolio on the reference variables; is an increasing function of the largest eigenvalue of *(Gt G)*<sup>−</sup>1, where *G* = Corr*(fn, gm)n,m*<sup>=</sup>1*,...,K* is the cross-correlation matrix of the factors and the reference variables; and *V* <sup>2</sup> is a bound on the variances of the *Zi*. See [5, 8] for further details.

What is important about the bound is that neither nor depends on the number of assets, *N*. This means that the size of the bound depends on the number of assets *N*, only through *(K), S*, and *V* , which may be bounded as this number increases to infinity.

## **The Pricing Errors**

The pricing error of any portfolio *w*,

$$\sum_{k=1}^{K} w_i \rho_i = \rho_w \tag{8}$$

satisfies

$$|\rho_w|^2 \le \Omega \sum_{i=1}^N w_i^2 \tag{9}$$

Provided is not large and *N* is large, the pricing error on each well-diversified portfolio is small. For a single asset *i*, we only get that most of the *ρi* are small. However, for a few of the assets the *ρi* may not be small.

## **Example**

Assume that each *Zi* is given by

$$Z_i = a_i + b_i f + e_i$$

where the *ei* are mutually uncorrelated and have zero mean, and *f* has a zero mean and unit variance and is uncorrelated with all the *ei*.

The APT implies that every random variable *g* for which cov(*g, f* ) is not zero can serve as a reference variable. Thus there exists a constant *λ* so that

$$E[Z_i] = \text{cov}(Z_i, gs)\lambda + \rho_i \text{ for each } i$$

In addition, for each well-diversified portfolio *w*, we have

$$E[Z_w] \approx \mathrm{cov}(Z_w, g)\lambda$$

In this example, = 1*/*corr*(f, g)*2; *(*1*)* and *S* and may take arbitrary values.

## **Empirical Studies**

Empirical studies attempted to find the sets of reference variables for which the hypothesis that

$$E[Z_i] = \sum\nolimits_{k=1}^K B_{i,k} \lambda_k$$

cannot be rejected. Roll and Ross [9] identified sets of macroeconomic variables that are believed to be responsible for stock price movements and tested whether they explain expected returns in the major US markets. Trzcinka [13] applied PCA to identify the factors. He showed that a small number of factors may explain most of the variation of the market. Then he tested the multibeta representation with these factors as reference variables.

## **Equilibrium APT**

The CAPM implies that the market portfolio is mean–variance efficient. If the market portfolio is a well-diversified one, then it is spanned by the factors. In that case, we get that if the reference variables are the factors, then is small, which implies that the approximation error for each asset in the sequence is small. Connor [2] and Wei [14] derived a related result which is called equilibrium APT.

## **Arbitrage and APT**

*S* measures the extent to which arbitrage in the meanvariance sense exists. It is equal to the maximal expected excess return per unit variance of portfolios in the *Zi*. A large *S* can be interpreted as some form of no arbitrage. However it is not an arbitrage in the standard sense as there are examples in which *S* is finite and arbitrage exists. See Reisman [6].

## **Testability**

It was pointed out by Shanken [11, 12] that an inequality of the type given in equation (7) is a tautology. That is, it is a mathematical statement and thus cannot be rejected.

Assume that we performed statistical tests that imply that the probability that the bound in equation (7) holds, is small. Then the only explanation can be that it was a bad sample. Since equation (7) is a tautology, there is no other explanation.

Nevertheless, this does not imply that the bound is not useful. The bound translates prior beliefs on the sizes of , *S*, and , into a prior belief on a bound on the size of the approximation error of each well-diversified portfolio.

The relationship between the sizes of , *S*, and , and the model assumptions is illustrated in the next section.

## **The APT Assumptions**

The model is derived under assumptions on the extent to which there exists

- 1. a factor structure with *K* factors;
- 2. no mean–variance arbitrage;
- 3. nontrivial correlation between our set of reference variables and the first *K* factors in the PCA.

The parameters , *S*, and are measures of the extent to which each of the above assumptions holds. The larger it is, the larger is the extent to which the related assumption does not hold.

What this says is that the model translates our beliefs on the extent to which the model assumptions hold to a belief on a bound on the size of the approximation errors in pricing well-diversified portfolios.

## **Summary**

The APT implies that each (approximate) welldiversified portfolio is (approximately) priced by a set of *K* reference variables.

What distinguishes this model from the *K*-factor CAPM is the set of reference variables that is implied by each of the models.

In the CAPM, the market portfolio is mean– variance efficient and its return must be equal to a linear function of the set of reference variables.

In contrast, in the APT, the reference variables are any set that is nontrivially correlated with the common factors of the returns and it may not span the mean–variance frontier.

## **End Notes**

a*.* The cross-correlation matrix is nonsingular.

b*.* The excess return is the return minus the risk-free rate.

## **References**

- [1] Chamberlain, G. & Rothschild, M. (1983). Arbitrage, factor structure, and mean variance analysis on large asset markets, *Econometrica* **51**, 1281–1304.
- [2] Connor, G. (1984). A unified beta pricing theory, *Journal of Economic Theory* **34**, 13–31.
- [3] Huberman, G. (1982). A simple approach to arbitrage pricing, *Journal of Economic Theory* **28**, 183–191.
- [4] Ingersoll Jr J.E. (1984). Some results in the theory of arbitrage pricing, *Journal of Finance* **39**, 1021–1039.
- [5] Nawalkha, S.K. (1997). A multibeta representation theorem for linear asset pricing theories, *Journal of Financial Economics* **46**, 357–381.
- [6] Reisman, H. (1988). A general approach to the Arbitrage Pricing Theory (APT), *Econometrica* **56**, 473–476.

- [7] Reisman, H. (1992). Reference variables, factor structure, and the approximate multibeta representation, *Journal of Finance* **47**, 1303–1314.
- [8] Reisman, H. (2002). Some comments on the APT, *Quantitative Finance* **2**, 378–386.
- [9] Roll, R. & Ross, S.A. (1980). An empirical investigation of the arbitrage pricing theory, *Journal of Finance* **35**, 1073–1103.
- [10] Ross, S.A. (1976). The arbitrage theory of capital asset pricing, *Journal of Economic Theory* **13**, 341–360.
- [11] Shanken, J. (1982). The arbitrage pricing theory: is it testable? *Journal of Finance* **37**, 1129–1140.
- [12] Shanken, J. (1992). The current state of the arbitrage pricing theory, *Journal of Finance* **47**, 1569–1574.

- [13] Trzcinka, C. (1986). On the number of factors in the arbitrage pricing model, *Journal of Finance* **41**, 347–368.
- [14] Wei, K. & John, C. (1988). An asset-pricing theory unifying CAPM and APT, *Journal of Finance*, **43**, 881–892.

## **Related Articles**

**Capital Asset Pricing Model**; **Correlation Risk**; **Factor Models**; **Risk–Return Analysis**; **Ross, Stephen**; **Sharpe, William F**.

HAIM REISMAN
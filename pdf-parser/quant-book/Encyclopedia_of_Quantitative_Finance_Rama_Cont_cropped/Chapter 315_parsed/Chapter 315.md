# **Correlation Risk**

## Correlation

Correlation is a well-known concept for measuring the linear relationship between two or more variables. It plays a major role in a number of classical approaches in finance: the capital asset pricing model (see Capital Asset Pricing Model) as well as arbitrage pricing theory (APT) rely on correlation as a measure for the dependence of financial assets (see [4]). In the multivariate Black-Scholes model correlation of the log-returns is used as a measure of the dependence between assets, [2, 5, 14]. The main reason for the importance of correlation in these frameworks is that the considered random variables  $(rvs)$  obey—under an appropriate transformation—a multivariate normal distribution. Correlation is moreover a key driver in portfolio credit models, and the term default correlation has been coined for this. Correlation as a measure of dependence fully determines the dependence structure for normal distributions and, more generally, elliptical distributions while it fails to do so outside this class. Even within this class, correlation has to be handled with care; while a correlation of zero for multivariate normally distributed rvs implies independence, a correlation of zero for, say,  $t$ -distributed rvs does *not* imply independence (compare the following paragraph on correlation pitfalls). More general measures of dependence help to avoid these pitfalls. Examples of more general measures for dependence are rank correlation, the coefficient of tail dependence, and association (see Copulas: Estimation).

Hence, approaches relying on multivariate Brownian motions and transformations thereof naturally determine the dependence structure via correlation. Extending this, there are a number of approaches generalizing the simple linear correlation to a timevarying and stochastic concept (see [3, 8] and references therein).

For two random variables  $X$  and  $Y$  with finite and positive variances, their *correlation* is defined as

$$Corr(X, Y) = \frac{Cov(X, Y)}{\sqrt{Var(X) \cdot Var(Y)}}$$
(1)

where

$$Cov(X, Y) = \mathbb{E}\Big[(X - \mathbb{E}(X)), (Y - \mathbb{E}(Y))\Big] \quad (2)$$

is the *covariance* of  $X$  and  $Y$ . We state some properties of correlation:  $Corr(X, Y)$  is a number in  $[-1, 1]$  and it is equal to 1 or  $-1$  if and only if X and Y are linearly related, that is,  $Y = a + b X$  for constants a, b with  $b \neq 0$ . The correlation is  $-1$  if  $b < 0$  and 1 if  $b > 0$ . For constants a, b

$$Corr(X + a, Y + b) = Corr(X, Y)$$
(3)

If X and Y are independent, then  $Corr(X, Y) = 0$ . On the other hand, if  $Corr(X, Y) = 0$ , X and Y are called *uncorrelated*. In the case when  $(X, Y)$  has a bivariate normal distribution, this implies independence of  $X$  and  $Y$ . Otherwise, this implication is typically wrong: even when  $X$  and  $Y$  are normally distributed (but  $(X, Y)$  does not have a bivariate normal distribution—compare copulas and dependence measurement for an exposition how this may be achieved using copulas),  $Corr(X, Y) = 0$  does not imply independence.

For two random variables belonging to a given class of elliptical distributions,<sup>a</sup> which includes the normal distribution and the Student  $t$ -distribution, correlation fully determines the dependence structure. However, note that uncorrelated  $t$ -distributed random variables are *not* independent.

If  $X$  is  $m$ -dimensional and  $Y$   $n$ -dimensional, then  $Cov(X, Y)$  is given by the  $m \times n$ -matrix with entries  $\text{Cov}(X_i, Y_i)$ .  $\Sigma = \text{Cov}(X, X)$  is called *covariance matrix*.  $\Sigma$  is symmetric and positive semidefinite, that is,  $x^{\top} \Sigma x > 0$  for all  $x \in \mathbb{R}^m$ . Moreover, one has

$$Cov(\mathbf{a} + BX, \mathbf{c} + DY) = B Cov(X, Y)D^{\top} \quad (4)$$

for  $\mathbf{a} \in \mathbb{R}^o$ ,  $\mathbf{c} \in \mathbb{R}^p$ ,  $B \in \mathbb{R}^{o \times m}$ ,  $D \in \mathbb{R}^{p \times n}$ . Similarly,  $Corr(X, Y)$  has the entries  $Corr(X_i, Y_i)$ ,  $1 <$  $i \leq m, 1 \leq j \leq n$ . The *correlation matrix* of X is  $Corr(X, X)$ . It is again symmetric and positive semidefinite. Correlation is invariant under linear increasing transformations such that

$$Corr(a + bX, c + dY) = Corr(X, Y)$$
(5)

if  $bc > 0$ . If  $bc < 0$  only the sign of the correlation changes.

## Correlation Pitfalls

When correlation is used as a measure of dependence a number of pitfalls arise; compare [7] or [13], Chapter 5.2.1 for a detailed exposition. In the following, we list the typical pitfalls and give a hint why difficulties may arise when linear correlation is used.

- 1. A correlation of 0 is not equivalent to inde*pendence.* For  $(X, Y)$  being jointly normal,  $Corr(X, Y) = 0$  implies independency of X and  $Y$ . In general this is not true; even perfectly related rvs can have zero correlation; consider  $X \sim \mathcal{N}(0, 1)$  and  $Y = X^2$ . Then  $\text{Corr}(X, Y) = 0$ and  $X$  and  $Y$  are clearly not independent.
- 2. Correlation is invariant under linear transformations, but not under general transformations. For example, two lognormal rvs have a different correlation than the underlying normal rvs; compare Example 5.26 in [13].
- 3. For given distributions of  $X$  and  $Y$  and some given correlation in  $[-1, 1]$  it is, in general, not possible to construct a joint distribution. For example, if  $X$  and  $Y$  are lognormally distributed, the interval of attainable correlations is a strict subset of  $[-1, 1]$  and becomes smaller with increasing volatility; compare again Example 5.26 in [13].
- 4. A small correlation does not imply a small degree of dependency. This is, in particular, implied by observation 3, and so it is, in general, wrong to deduce a small degree of dependency from a small correlation.

## Stylized Facts

Asset correlation shows two typical stylized feat $ures:<sup>b</sup>$ 

- 1. *Correlation clustering*: periods of high (low) correlation are likely to be followed by periods of high (low) correlation.
- 2. Asymmetry and comovement with volatility: high volatility in falling markets goes hand in hand with a strong increase in correlation, but this is not the case for rising markets; see [12] or [1].

In [15] the 1987 crash is analyzed and correlation risk is identified as a reason of simultaneous stockmarket declines and volatility increases. Notably, this reduces opportunities for diversification in stockmarket declines.

#### Estimating Correlation

The estimation of correlation in financial data is a delicate task as the underlying distribution typically has heavy tails. If this is the case, it is preferable to use robust methods in comparison to nonrobust methods like the sample correlation. Evidence of the efficiency of robust methods like Kendall's rank correlation coefficient is provided in [13], Section 3.3.4. Acknowledging that correlation changes over time, a number of approaches for dynamic correlation have been developed; see, for example, [3, 8] and references therein.

## **Correlation Risk**

*Correlation risk* refers to the risk of a financial loss when correlation in the market changes. It plays a central role in risk management and the pricing of basket derivatives.

#### Risk Management

In risk management, correlation risk refers to the risk of a loss in a financial position occurring due to a difference between anticipated correlation and realized correlation. In particular, this occurs when the estimate of correlation was wrong or the correlation in the market changed.

The risk management of a portfolio as well as portfolio optimization heavily depends on the used correlation. This is illustrated by the following simple example: assume that a financial position is given by portfolio weights  $w_1, \ldots, w_d$  and the distribution of the assets  $X$  is multivariate normal. Then the profit and loss (P&L) of the position is  $\sum_{i=1}^{d} w_i X_i$ , and is hence normally distributed with mean  $\sum_{i=1}^{d} w_i E(X_i)$ and variance

$$\sum_{i,j=1}^{d} w_i w_j \operatorname{Cov}(X_i, X_j) \tag{6}$$

which equals  $\sum_{i=1}^{d} w_i^2 \text{Var}(X_i)$  if the positions are uncorrelated. Otherwise, the Value at Risk depends on the correlations of all assets and therefore a change in the correlation may significantly alter the risk of the position.

In the elliptical world, the use of coherent risk measures is related to the Markowitz approach where the variance is used as a risk measure; see [13], Section 6.1.5. The effects of stochastic correlation on hedging strategies have also been considered in [9]. Section 5 therein also gives some examples on stochastic correlation.

## *Basket Derivatives*

If the pricing of basket derivatives (*see* **Foreign Exchange Basket Options**; **Basket Options**) is considered, the value of the derivative itself depends on the (unknown) correlation. In this case, correlation risk refers to the change in the value of the derivative with changing correlation. Note that in contrast to the first example, already the *value* of the derivative itself depends on the correlation. Options of this kind typically are traded in interest markets, foreign exchange markets, or credit markets, examples being quanto (*see* **Quanto Options**) options, rainbow options, spread options, or collateralized debt obligations (*see* **Collateralized Debt Obligations (CDO)**). In particular, in credit markets, the term *default correlation* has been coined and contagion and dependencies play a central role. For more references on the role of default correlation risk in credit risky markets, see [10, 11].

By analyzing prices of options on single names and on market indices, Driessen *et al.* [6] show that correlation risk is priced in the options markets. Practitioners trade priced correlation risk by using short positions in index options and long positions in individual options, which is called *dispersion trading* (*see* **Dispersion Trading**). A similar position can be taken with a correlation swap (*see* **Correlation Swap**).

In particular, in credit markets, contagion and dependencies play a central role. For more references on the role of default correlation risk in credit risky markets, see [10, 11].

## **End Notes**

a*.* Compare [13], Theorem 3.25. Section 3.3 therein gives a short introduction to elliptical distributions. b*.* See, for example, [16] and references therein.

**References**

[1] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Ebense, H. (2001). The distribution of realized stock return volatility, *Journal of Financial Economics* **61**, 43–76.

- [2] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [3] Campbell, R.A.J., Forbes, C.S., Koedijk, K.G. & Kofman, P. (2008). Increasing correlations or just fat tails, *Journal of Empirical Finance* **15**, 287–309.
- [4] Campbell, J.W., Lo, A.W. & MacKinlay, A.C. (1997). *The Econometrics of Financial Markets*, University Presses of CA.
- [5] Carmona, R. & Durleman, V. (2006). Generalizing the Black–Scholes formula to multivariate contingent claims, *Journal of Computational Finance* **9**, 43–67.
- [6] Driessen, J., Maenhout, P. & Vilkov, G. The Price of Correlation Risk: Evidence from Equity Options, *Journal of Finance*, forthcoming (June 2009).
- [7] Embrechts, P., McNeil, A.J. & Straumann, D. (2001). Correlation and dependency in risk management: properties and pitfalls, in *Risk Management: Value at Risk and Beyond*, M. Dempster & H.K. Moffatt, eds, Cambridge University Press, pp. 176–223.
- [8] Engle, R.F. (2002). Dynamic conditional correlation: a simple class of multivariate generalized autoregressive conditional heteroskedasticity models, *Journal of Business and Economic Statistics* **20**, 339–350.
- [9] Gozzi, F. & Vargiolu, T. (2002). Superreplication of European multiasset derivatives with bounded stochastic volatility, *Mathematical Methods of Operations Research* **55**, 69–91.
- [10] Gregory, J. & Laurent, J.P. (2004). In the core of correlation, *Risk* **17**(10), 87–91.
- [11] Lipton, A. & Rennie, A. (eds) (2007). *Credit Correlation: Life After Copulas*, World Scientific.
- [12] Longin, F. & Solnik, B. (2001). Extreme correlation of international equity markets, *Journal of Finance* **56**, 649–676.
- [13] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management: Concepts, Techniques and Tools*, Princeton University Press.
- [14] Merton, R. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [15] Rubinstein, R. (2001). Comments on the 1987 stockmarket crash: 11 years later, *Investment Accumulation Products of Financial Institutions*, The Society of Actuaries.
- [16] Skintzi, V.D. & Refenes, A.-P.N. (2005). Implied correlation index: a new measure of diversification, *The Journal of Future Markets* **25**, 171–1197.

# **Further Reading**

Merton, R. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**, 141–183.

# **Related Articles**

**Copulas: Estimation**; **Correlation Swap**; **Dispersion Trading**; **Levy Copulas ´** ; **Multivariate Distributions**.

THORSTEN SCHMIDT
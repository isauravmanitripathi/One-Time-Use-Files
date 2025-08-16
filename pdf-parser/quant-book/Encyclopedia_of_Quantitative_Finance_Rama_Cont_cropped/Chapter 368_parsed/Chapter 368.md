# **Copulas in Econometrics**

## **Copulas and Multivariate Models**

The knowledge of the multivariate (conditional) distribution (especially fat tails, asymmetry, positive or negative dependence) is essential in many important financial applications, including portfolio selection, option pricing, asset pricing models, Value-at-Risk (market risk, credit risk, liquidity risk) calculations, and forecasting. Copulas provide a general, flexible tool in modeling the complex dependence structure among multiple random variables and in building multivariate models from univariate models; see [6, 20, 26] for discussions and references on the applications of copulas in economics, finance, insurance, and risk management. Patton [23] provides an excellent review of copula models for financial time series.

A copula is a multivariate distribution function with uniform marginal distributions on  $[0, 1]$  that links together univariate distribution functions to form a multivariate distribution function. To simplify the exposition, the focus is on the bivariate case in this article. Let  $X, Y$  denote two scalar random variables with the joint distribution function  $H$  and marginal distribution functions  $F, G$ . The characterization theorem of Sklar [25] implies that there exists a copula  $C(u, v)$ :  $(u, v) \in [0, 1]^2$  such that

$$H(x, y) = C(F(x), G(y)) \text{ for all } (x, y) \in \mathbb{R}^2 \tag{1}$$

Conversely, for any marginal distributions  $F, G$ and any copula function  $C$ , the function  $C(F(\cdot), G(\cdot))$ is a bivariate distribution function with given marginal distributions  $F, G$ . This theorem provides the theoretical foundation for the widespread use of copulas in generating multivariate distributions (models) from univariate distributions (models).<sup>a</sup> The fact that the copula function  $C$ , the marginal distribution functions  $F, G$  in equation (1) are not necessarily of the same type allows the researcher a great deal of flexibility in specifying a multivariate distribution (model). For example, Chen and Fan [2] propose a general class of multivariate dynamic time series models by first modeling each individual time series by a univariate generalized autoregressive conditional heteroskedasticity (GARCH)-type model and then modeling the joint distribution of the innovations of the univariate models by a distribution with

a parametric copula and unknown marginal distributions. We refer the reader to [2] for details and related references.

Suppose that  $X, Y$  are continuous random variables. Then the copula function  $C$  in equation (1) is unique.<sup>b</sup> It extracts the dependence information on  $X, Y$  from their joint distribution  $H$  and is sometimes referred to as the *dependence function* of  $X, Y$ . The copula function of  $X, Y$  is invariant to monotone increasing transformations of  $X, Y$  and most rank dependence measures can be expressed in terms of the copula alone, including Kendall's  $\tau$ , Spearman's  $\rho$ , and tail dependence coefficients; for details, see [17] and [22]. It is to be noted, however, that Pearson's linear correlation coefficient cannot be expressed in terms of the copula alone; it also depends on the marginal distributions.

Suppose that the density function of  $(X, Y)$  exists and is denoted by  $h$ . Then equation (1) implies

$$h(x, y) = f(x)g(y)c(F(x), G(y))$$
  
$$\forall (x, y) \in \mathbb{R}^2$$
 (2)

where  $f, g$  are the marginal density functions and  $c$ is the copula density function. The decomposition of the joint density function  $h$  in equation (2) is the basis for the commonly used methods for estimating copula models. For a fully parametric copula model in which both the copula function and the marginal distribution functions are parameterized, both maximum likelihood (ML) method and two-step method can be used. Joe [17] and Nelsen [22] present numerous parametric copula functions including the Gaussian copula, Student's  $t$  copula, and Archimedean copulas. For a semiparametric copula model in which the copula function is parameterized, but the marginal distribution functions are not, both two-step method and sieve ML method have been developed; see  $[15]$  for details on the two-step method and [5] for details on the sieve ML method. To introduce the two-step approach and ML or sieve ML approach, suppose that we have a random sample  $\{X_i, Y_i\}_{i=1}^n$  from  $h(x, y)$ . Then equation (2) implies that the log-likelihood function is given as

$$\sum_{i=1}^{n} \ln f(X_i) + \sum_{i=1}^{n} \ln g(Y_i)$$
$$+ \sum_{i=1}^{n} \ln c(F(X_i), G(Y_i)) \qquad (3)$$

In the two-step approach, the marginal distribution functions  $F$  and  $G$  are estimated in the first step and the copula function is estimated in the second step. For example, for a semiparametric copula model, the marginal distribution functions are estimated in the first step by the corresponding (rescaled) empirical distribution functions denoted as  $\widehat{F}(x)$ ,  $\widehat{G}(y)$  and the copula function is estimated in the second step by maximizing  $\sum_{i=1}^{n} \ln c(\widehat{F}(X_i), \widehat{G}(Y_i)).$ We refer the reader to  $[15]$  for details on the two-step approach for random samples and [2, 3] for extensions to copula-based multivariate and univariate time series models, respectively. In the ML or sieve ML approach, the marginal distribution functions and the copula function are estimated simultaneously. For a fully parametric copula model, this is accomplished by maximum likelihood estimation (MLE) obtained from maximizing the log-likelihood function (3) with respect to parameters in both the marginal distribution functions and the copula function simultaneously, whereas for a semiparametric copula model, the maximization of the log-likelihood function (3) is carried out over respective sieve spaces approximating the spaces of marginal distribution functions  $F$  and  $G$ and the parameter space for the copula parameter; see [5] for details on sieve spaces and the sieve MLE. In general, the two-step estimator is asymptotically less efficient than the ML estimator in a parametric copula model or the sieve ML estimator in a semiparametric copula model.

In a parametric or semiparametric copula model in which the copula is parameterized, it is important to select an appropriate parametric copula and to evaluate how well the selected copula model fits the data at hand. Commonly used parametric copula families include the Gaussian copula family, Student's  $t$ copula family, Gumbel copula family, Clayton copula family, and Frank copula family. The latter three copula families are members of the general Archimedean copula family. These copula families have different dependence properties and are thus appropriate for modeling different dependence properties of economic and financial variables. For example, the Gaussian and Frank copula families have no tail dependence and are thus not appropriate for modeling financial variables that tend to take extreme values together. Instead, Student's  $t$  copula family has both lower and upper tail dependence and thus is appropriate for modeling economic or financial variables taking extremely large or small values together. On the other hand, the Gumbel copula family has upper tail dependence and no lower tail dependence, whereas the Clayton copula family has lower tail dependence and no upper tail dependence. Chen and Fan [2, 4] developed model selection tests for copula families and [13], among others, developed goodness-of-fit tests for copulas. For applications of estimation and model selection procedures for copula-based models, the reader is referred to [4, 7]. Additional references can be found in  $[23]$ .

## The General Fréchet Problem

In addition to its role in building multivariate models from univariate models, copulas have also proven to be useful in finding solutions to the general Fréchet problem. Broadly speaking, the Fréchet problem concerns the problem of finding sharp bounds on the distributions of functions of random variables  $X, Y$ such as  $X + Y$  and  $X - Y$  when the marginal distribution functions  $F$ ,  $G$  are fixed. The reader is referred to [24, 27] for discussions and references on the general Fréchet problem and its solutions, to [20] for its applications in finance and risk management, and to  $[11, 12]$  for its applications in program evaluation.

For  $(u, v) \in [0, 1]^2$ , let  $C^L(u, v) = \max(u + v -$ 1, 0) and  $C^{U}(u, v) = \min(u, v)$  denote the Fréchet-Hoeffding lower and upper bounds for a copula, that is,  $C^L(u,v) < C(u,v) < C^U(u,v)$ . Then for any  $(x, y) \in \mathbb{R}^2$ , the following inequality holds:

$$C^{L}(F(x), G(y)) \leq H(x, y) \leq C^{U}(F(x), G(y))$$
(4)

The bivariate distribution functions  $C^L(F(\cdot))$ ,  $G(\cdot)$  and  $C^U(F(\cdot), G(\cdot))$  are referred to as the Fréchet-Hoeffding lower and upper bounds for bivariate distribution functions with fixed marginal distributions  $F$  and  $G$ . They are distributions of perfectly negatively dependent and perfectly positively dependent random variables respectively; see [22] for more discussions. The inequality (4) directly implies sharp bounds on the correlation coefficient between *X* and *Y*:  $\rho_L \leq \rho \leq \rho_U$ , where

$$\rho_L = \frac{\int \int [C^L(F(x), G(y)) - F(x)G(y)] \, \mathrm{d}x \, \mathrm{d}y}{\sigma_X \sigma_Y}$$

$$\rho_U = \frac{\int \int [C^U(F(x), G(y)) - F(x)G(y)] \, \mathrm{d}x \, \mathrm{d}y}{\sigma_X \sigma_Y} \tag{5}$$

in which  $\sigma_X^2$  and  $\sigma_Y^2$  are variances of X and Y, respectively. It is known that  $\rho_L$  and  $\rho_U$  are sharp; see [9, 20] for detailed discussions on this result and other properties and pitfalls of the correlation coefficient as a dependence measure.

Although inequality (4) does not directly imply bounds on distribution functions of  $X + Y$  and  $X - Y$  $Y$ , copulas provide a useful tool in finding such bounds; see [14]. In what follows, sharp bounds on the distribution function of  $X - Y$  and sharp bounds on the quantile function of  $X + Y$  are provided and their applications pointed out.

Let  $\Delta = X - Y$ .  $\Delta$  is referred to as the *individual* treatment effect in the literature on program evaluation. In this context,  $X$  is the potential outcome from treatment and  $Y$  is the potential outcome without treatment; see [11, 12] for details. Denote the distribution function of  $\Delta$  by  $F_{\Delta}(\cdot)$ . Given the marginals F and G, sharp bounds on the distribution of  $\Delta$  can be found in [27]:  $F_{\Delta}^{L}(\delta) \leq F_{\Delta}(\delta) \leq F_{\Delta}^{U}(\delta)$ , where

$$F_{\Delta}^{L}(\delta) = \sup_{y} \max(F(y) - G(y - \delta), 0),$$
  
$$F_{\Delta}^{U}(\delta) = 1 + \inf_{y} \min(F(y) - G(y - \delta), 0) \quad (6)$$

Let  $\Lambda = X + Y$  and  $Q_{\Lambda}(p) \left(= F_{\Lambda}^{-1}(p) \right)$  denote its generalized quantile function at quantile level  $p$ :  $0 < p < 1$ . Given the generalized quantile functions  $F^{-1}$  and  $G^{-1}$ , sharp bounds on  $Q_{\Lambda}(p)$  can be found in [20, 27]:  $Q_{\Lambda}^{L}(p) \leq Q_{\Lambda}(p) \leq Q_{\Lambda}^{U}(p)$ , where

$$Q_{\Lambda}^{L}(p) = \inf_{u \in [p,1]} [F^{-1}(u) + G^{-1}(u-p+1)],$$
  

$$Q_{\Lambda}^{U}(p) = \sup_{u \in [0,p]} [F^{-1}(u) + G^{-1}(u-p)] \qquad (7)$$

McNeil *et al.* [20] discuss applications of equation (7) in risk management and provide an extensive list of references.

The expressions in equations  $(5)$ – $(7)$  share one common feature, that is, they depend only on the marginal distributions. As a result, they can be consistently estimated without requiring any dependence

information between  $X$  and  $Y$ , provided that univariate samples from  $F, G$  are available. For example, consider a linear portfolio  $\Lambda$  of market risk X and credit risk Y. Estimation of the Value-at-Risk of  $\Lambda$ requires a bivariate sample from the joint distribution of  $X, Y$ , which may not always be available. In contrast, equation (7) implies that the smallest and largest Value-at-Risk can be estimated with univariate samples from F, G. Inference on  $\rho$ ,  $F_{\Delta}(\delta)$ , and  $Q_{\Lambda}(p)$  belongs to the recent, but fast-growing area in econometrics, namely, inference for partially identified parameters. The reader is referred to [10] for discussion and references.

#### Conclusion

This article concludes with a mention of some recent work on the construction of higher dimensional copulas and the Fréchet problem in higher dimensions. Copulas have found to be most successful in bivariate modeling, as there are numerous parametric families of bivariate copulas that the researcher can choose from; see [17, 22]. Compared with bivariate parametric copulas, the number of higher dimensional parametric copulas is rather limited. So far, most applications in higher dimensions have focused on Gaussian copulas and Student's  $t$  copulas. It is well known that the construction of higher dimensional copulas is very difficult. Several methods have been proposed recently, including methods for constructing higher dimensional Archimedean copulas and the general pair-copula construction approach known as *vines*; see  $[1, 19]$  and the references therein.

The Fréchet problem in higher dimensions has drawn attention recently. The reader is referred to [8] for a brief account and references. Finally, the reader is referred to [21] and the associated discussions and rejoinder for a lively discussion on the value of copulas in multivariate modeling.

## **End Notes**

<sup>a.</sup> Joe [17] and Nelsen [22] provide a detailed introduction to copulas and their mathematical and statistical foundations. Kallsen and Tankov [18] present a version of Sklar's theorem that allows to construct a general multivariate Lévy process from arbitrary univariate Lévy processes and an arbitrary Lévy copula.

<sup>b.</sup> Genest and Nešlehova [16] present an excellent discussion on copulas for discrete data.

# **References**

- [1] Aas, K., Czado, C. Frigessi, A. & Bakken, H. (2009). Pair-copula constructions of multiple dependence, *Insurance, Mathematics, and Economics* **44**(2), 182–198.
- [2] Chen, X. & Fan, Y. (2006). Estimation and model selection of semiparametric copula-based multivariate dynamic models under copula misspecification, *Journal of Econometrics* **135**, 125–154.
- [3] Chen, X. & Fan, Y. (2006). Semiparametric estimation of copula-based time series models, *Journal of Econometrics* **130**, 307–335.
- [4] Chen, X. & Fan, Y. (2007). Model selection test for bivariate failure-time data, *Econometric Theory* **23**, 414–439.
- [5] Chen, X., Fan, Y. & Tsyrennikov, V. (2006). Efficient estimation of semiparametric multivariate copula models, *Journal of the American Statistical Association* **101**, 1228–1240.
- [6] Cherubini, U., Luciano, E. & Vecchiato, W. (2004). *Copula Methods in Finance*, John Wiley & Sons, England.
- [7] Dias, A. & Embrechts, P. (2003). *Dynamic Copula Models for Multivariate High-Frequency Data in Finance*, Mimeo.
- [8] Embrechts, P. (2008). Copulas: a personal view, Forthcoming in *Journal of Risk and Insurance*.
- [9] Embrechts, P., McNeil, A. & Straumann, D. (2002). Correlation and dependence properties in risk management: properties and pitfalls, in *Risk Management: Value at Risk and Beyond*, M. Dempster, ed., Cambridge University Press, pp. 176–223.
- [10] Fan, Y. & Park, S. (2007). *Confidence Sets for Some Partially Identified Parameters*, Manuscript, Vanderbilt University.
- [11] Fan, Y. & Park, S. (2009). Sharp bounds on the distribution of treatment effects and their statistical inference, Forthcoming in *Econometric Theory*.
- [12] Fan, Y. & Wu, J. (2007). *Partial Identification of the Distribution of Treatment Effects in Switching Regimes Models and its Confidence Sets*, Manuscript, Vanderbilt University.
- [13] Fermanian, J.-D. (2005). Goodness of fit tests for copulas, *Journal of Multivariate Analysis* **95**, 119–152.
- [14] Frank, M.J., Nelsen, R.B. & Schweizer, B. (1987). Bestpossible bounds on the distribution of a sum – a problem of Kolmogorov, *Probability Theory and Related Fields* **74**, 199–211.
- [15] Genest, C., Ghoudi, K. & Rivest, L. (1995). A semiparametric estimation procedure of dependence parameters in

multivariate families of distributions, *Biometrika* **82**(3), 543–552.

- [16] Genest, C. & Neslehova, J. (2007). A primer on copulas ˇ for count data, Forthcoming in *The ASTIN Bulletin* **37**, 475–515.
- [17] Joe, H. (1997). *Multivariate Models and Dependence Concepts*, Chapman & Hall/CRC.
- [18] Kallsen, J. & Tankov, P. (2006). Characterization of dependence of multidimensional Levy processes using ´ Levy Copulas, ´ *Journal of Multivariate Analysis* **97**, 1551–1572.
- [19] Kurowicka, D. & Cooke, R. (2006). *Uncertain Analysis with High Dimensional Dependence Modelling*, Wiley Series in Probability and Statistics, John Wiley & Sons, Ltd.
- [20] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management: Concepts, Techniques and Tools*, Princeton University Press, New Jersey.
- [21] Mikosch, T. (2006). Copulas: tales and facts, with discussion and rejoinder, *Extremes* **9**, 3–62.
- [22] Nelsen, R.B. (1999). *An Introduction to Copulas*, Springer.
- [23] Patton, A.J. (2007). Copula-based models for financial time series, in *Handbook of Financial Time Series*, T.G. Anderson, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer-Verlag, pp. 767–786.
- [24] Schweizer, B. & Sklar, A. (1983). *Probabilistic Metric Spaces*, North-Holland, New York.
- [25] Sklar, A. (1959). Fonctions de r'epartition 'a *n* dimensionset leurs marges, *Publications de l'. Institut de Statistiquede l' Universite de Paris* **8**, 229–231.
- [26] Trivedi, P. & Zimmer, D.M. (2007). Copula modeling: an introduction for practitioners, *Foundations and Trends in Econometrics* **1**(1), 1–110.
- [27] Williamson, R.C. & Downs, T. (1990). Probabilistic arithmetic I: numerical methods for calculating convolutions and dependency bounds, *International Journal of Approximate Reasoning* **4**, 89–158.

# **Related Articles**

**Copulas in Insurance**; **Copulas: Estimation**; **Correlation Risk**; **Levy Copulas ´** ; **Multivariate Distributions**.

YANQIN FAN
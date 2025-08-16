# **Credit Migration Models**

It is nowadays widely recognized that portfolio models are an essential tool for a proper and effective management of credit portfolios, be it from the perspective of a corporate bank, a mortgage bank, a consumer finance provider, or a fixed-income asset manager. Traditional credit management was, to a large extent, focused on the stand-alone analysis and monitoring of the credit quality of obligors or counterparties. Frequently, the credit process did also include *ad hoc* exposure-based limit-setting policies that were devised in order to prevent excessive risk concentrations. This approach was scrutinized in the 1990s, when the financial industry started to realize that univariate models for obligor default had to be extended to a portfolio context. It was recognized that credit rating and loss recovery models, although a crucial element in the assessment of credit risk, fail to explain some of the important stylized facts of credit loss distributions, if the stochastic dependence of obligor defaults is neglected. From a statistical point of view, not only the skewness and the relatively heavy upper tails of credit portfolio loss distributions, but also the historically observed variation of default rates and the clustering of bankruptcies in single sectors are clearly inconsistent with stochastic independence of defaults. From an economics point of view, it is plausible that default rates are connected to the intrinsic fluctuations of business cycles; relationships between default rates and the economic environment have indeed been established in numerous empirical studies [5]. All these insights supported the quest for tractable credit portfolio models that reflect these stylized facts.

Apart from an accurate statistical description of credit losses, a portfolio model can serve many more purposes. In contrast to a univariate approach, a credit portfolio framework allows to quantify the diversification effects between credit instruments. This makes it, for example, possible to evaluate the impact on the total risk when securities are added or removed from a portfolio. In the same vein, the risk numbers produced by a portfolio model help to identify possible hedges. Ultimately, the use of a portfolio model facilitates the active management of credit portfolios and the efficient allocation of capital. Less of a pure risk management matter is the use of portfolio models for risk-adjusted pricing (*see* **Loan Valuation**) or performance measurement. The total portfolio risk is commonly considered as a capital which the lender should hold in order to buffer large losses. For nontraded assets, such as loans or mortgages, the costs for holding this risk capital are typically transferred to the borrowers by means of a surcharge on interest rates. Calculating these surcharges necessitates that the total portfolio risk capital is broken down to borrower (or instrument) level risk contributions. Only in a portfolio model framework, where the dependence between obligors and the resulting diversification benefits are correctly captured, this risk contribution can be determined in an economically rational and fair fashion. We mention that risk contributions can also be applied in order to determine the *ex post* (historical) riskadjusted performance of instruments or subportfolios. Credit portfolio models also play an important role in the pricing of credit derivatives or structured products, such as credit default swaps or CDSs. For the correct pricing of many of these credit instruments, it is crucial that the dependence between obligor default times are well modeled.

## **Overview of Credit Migration-based Models**

This article gives a survey on migration-based portfolio models, that is, models that describe the joint evolution of credit ratings. The ancestor of all such models is CreditMetrics<sup>a</sup> , which was introduced by the US investment bank J.P. Morgan. In 1997, J.P. Morgan and cosponsors from the financial industry published a comprehensive technical document [13] on CreditMetrics, in an effort to set industry standards and to create more transparency in credit risk management. This publication attracted a lot of attention and proved to stimulate research in credit risk. To this date, the CreditMetrics or derivations thereof have been implemented by a large number of financial institutions. Before we turn to a detailed description of CreditMetrics, it might be worth to mention two related models. CreditPortfolioView by McKinsey & Co is creditmigration-based as well. However, in contrast to CreditMetrics, which assumes temporally constant transition matrices, it is endowed with an estimator of credit migration probabilities based on macroeconomic observables. is dedicated to its discussion. The second link concerns the longer standing KMV  $model.<sup>b</sup>$  An outline of the KMV methodology can be extracted from an article by Kealhofer and Bohn [16]. In both CreditMetrics and KMV, the obligor correlation is generated in a similar fashion, that is, with a dependence structure following a Gaussian copula. The main differences concern the number of credit states and the source of probabilities of default (PDs). The KMV model operates on a continuum of states, namely, the so-called expected default frequencies (Moody's KMV EDF<sup>™c</sup>), basically estimated PDs, whereas CreditMetrics is restricted to a finite number of credit rating states. For this reason, KMV is strictly spoken not a credit-migration-based model and therefore only touched in this article. As remarked by McNeil et al. [19], a discretization of EDF would translate KMV to a model which, apart from parametrization, is structurally equivalent to CreditMetrics. Secondly, while for Credit-Metrics rating transition matrices are the required exogenous inputs, the KMV counterparts, EDF of listed companies, are estimated through a proprietary method, which is basically an extension of the celebrated Merton model [20] for firm default. Inputs to the EDF model are historical time-series of equity prices together with company debt information, with which the unobserved asset value processes are reconstructed and a quantity called *distance* to *default*  $(DD)$  is calculated for every firm. This DD is used as a predictor of EDF; the relationship is determined by a nonlinear regression of historical default data against historical DD values. It is beyond the scope of this article to provide more details and so we refer to [2] or [17] for an account of the EDF methodology.

## The CreditMetrics Model

CreditMetrics models the distribution of the credit portfolio value at a future time, from which risk measures can be derived. The changes of portfolio value are caused by credit migrations of the underlying instruments. In the following, we describe the rationale of the main building blocks of CreditMetrics.

### Timescale

CreditMetrics was conceived as a discrete time model. It has a user-specified time horizon  $T$  that is reached in one step from the analysis time 0; typically the time horizon is 1 year. It is assumed that the portfolio is static, that is, its composition is not altered during the time period  $(0, T)$ .

#### Risk Factors and Valuation

In case of CreditMetrics, the basic assumption is that each instrument is tied to one or several obligors. The user furnishes obligors with a rating from a rating system with a finite number of classes and an absorbing default state. The obligor ratings are the main risk drivers. We index the obligors by  $i = 1, \ldots, n$  and assume a rating system with rating classes  $\{1, \ldots, K\}$ that are ordered with respect to the credit quality, and a default class 0. At time 0, the obligor  $i$  has the (known) initial rating  $S_i^{\text{init}}$ , which then becomes  $S_i^{\text{new}}$  at time T. The change from  $S_i^{\text{init}}$  to  $S_i^{\text{new}}$  happens in a random fashion, according to the so-called credit migration probabilities. These probabilities are assumed to be identical for obligors in the same rating class and can therefore be represented by a socalled credit migration (or rating transition) matrix  $\mathbf{M} = (m_{ik})_{i,k \in \{0,...,K\}}.$  Clearly,

$$\mathbb{P}(S_i^{\text{new}} = k | S_i^{\text{init}} = j) = m_{jk} \tag{1}$$

The credit migration matrix is an important input to CreditMetrics. In practice, one often uses rating systems supplied by agencies such as Moody's or Standard&Poor's. The model also allows to work in parallel with several rating systems, depending on the obligor. If public ratings are not available, financial institutions can resort to internal ratings; see Credit Rating; Internal-ratings-based Approach; Credit Scoring.

To treat specific positions, CreditMetrics must estimate values for the position contingent on the position's obligor being in each possible future rating state. This is equivalent to estimating the loss (or gain) on the position contingent on each possible rating transition. In the case of default, the recovery rate  $\delta_i$  determines the proportion of the position's principal that is paid back by the obligor.<sup>d</sup>

For the nondefault states, the standard implementation of the model is to value positions based on market factors: the risk-free interest rate curve and a spread curve corresponding to the rating state. For this reason, CreditMetrics is commonly referred to as a *mark-to-market model*. Importantly, the mark-tomarket approach incorporates a maturity effect into the model: other things being equal, a downward credit migration will have a greater impact on a long maturity bond than a short one, given the long bond's higher sensitivity (duration) to the spread widening that is assumed to accompany the migration. However, this approach does require relevant spread curves for positions of all possible rating states.

For positions where there is little market information, or where the mark-to-market approach is inconsistent with an institution's accounting scheme, it is possible to utilize policy-driven rather than marketdriven valuation. For example, if an institution has a reserves policy whereby loss reserves are determined by credit rating and maturity, then the change in required reserves can serve as a proxy for the loss on a position, contingent on a particular rating move. In this way, the model can still incorporate a maturity effect, even where a mark-to-market approach is not practical.

## Risk Factor Dynamics and Obligor Dependence Structure

In the original formulation of CreditMetrics, foreign exchange (FX) rates and interest rate and spread curves are assumed to be deterministic since one focuses on the rating as the main risk driver. In principle, this assumption could be relaxed.

The migration matrix in the CreditMetrics model specifies the rating dynamics of a single obligor, but it does not provide any information about the joint obligor credit migrations. In order to capture the obligor dependence structure. CreditMetrics borrows ideas from the Merton structural model for firm default, which links default to the obligor asset value falling short of its liabilities. The assumption of CreditMetrics is that the obligor rating transition is caused by changes of the obligor's asset value, or equivalently, the asset value return. The lower this random return, the lower the new rating; if the asset value return drops below a certain threshold, default occurs. Mathematically, this amounts to defining return buckets for each obligor; the thresholds bounding these buckets depend on the initial obligor rating, the transition probabilities, and the return distribution. The rating of an obligor is determined by the bucket its return falls into. Obviously, the bucket probabilities must coincide with the transition probabilities. Models of this type are also called *threshold models*.

More formally, if  $R_i$  denotes the asset return of obligor *i* over  $(0, T]$ , then the rating at time T is determined by

$$S_i^{\text{new}} = j \qquad \Longleftrightarrow \qquad d_j^{(i)} < R_i \le d_{j+1}^{(i)} \qquad (2)$$

The increasing thresholds  $d_i^{(i)}$  are picked such that the resulting migration probabilities coincide with the ones prescribed by the credit migration matrix. Consequently,

$$d_0^{(i)} = -\infty \quad \text{and} \quad d_{K+1}^{(i)} = +\infty$$
$$G_i(d_{j+1}^{(i)}) - G_i(d_j^{(i)}) = \mathbb{P}(S_i^{\text{new}} = j \mid S_i^{\text{init}}) \quad (3)$$

where  $G_i$  is the cumulative distribution function of  $R_i$ . We illustrate the rating transition mechanism in Figure 1, which shows the return distribution and the thresholds for an obligor with an initial rating  $2$ in a hypothetical rating system with four nondefault classes.

The dependence between obligor ratings stems from the dependence of the asset returns. CreditMetrics assumes that these returns follow a linear factor model with multivariate normal factors and independent Gaussian innovations. This means that

$$R_i = \alpha_i + \sum_{\ell=1}^p \beta_{i\ell} F_\ell + \sigma_i \epsilon_i \tag{4}$$

where the common factors  $\mathbf{F} = (F_1, \ldots, F_p)' \sim$  $\mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$  are multivariate Gaussian and the  $\epsilon_i$ 's are independent and identically distributed (i.i.d.) standard normal variables independent of the factors. The numbers  $\beta_{i\ell}$  are also called *factor exposures* or *load*ings,  $\sum_{\ell=1}^p \beta_{i\ell} F_\ell$  is the systematic return,  $\sigma_i$  is the volatility of idiosyncratic (or specific) return  $\sigma_i \epsilon_i$  of obligor *i*, and the real parameter  $\alpha_i$  is referred to as *alpha*. The dependence between the returns, and consequently the dependence between future ratings, is caused by the exposure of the obligors to the common factors. Usually one normalizes the returns  $R_i$ to unit variance; this does not alter the joint distribution of  $\mathbf{S}^{\text{new}} = (S_1^{\text{new}}, \dots, S_n^{\text{new}})'$  and leads to adjusted thresholds that are simpler. Not explicitly distinguishing between returns and normalized returns in our notation, equation  $(4)$  then reads as

$$R_{i} = \psi_{i}(\mathbf{F}) + \sqrt{1 - \text{Var}(\psi_{i}(\mathbf{F}))} \epsilon_{i} \sim \mathcal{N}(0, 1)$$
(5)

![](_page_3_Figure_1.jpeg)

Figure 1 Asset return distribution, thresholds and rating classes

for appropriate affine linear functions  $\psi_i$ . The adjusted thresholds are given by

$$d_j^{(i)} = d_j(S_i^{\text{init}}) \quad \text{with}$$
  
$$d_j(s) = \Phi^{-1} \left( \sum_{k=0}^{j-1} m_{sk} \right), \quad 0 < j \le K \qquad (6)$$

where  $\Phi$  is the standard normal distribution function.

As regards the recovery rates  $\delta_i$ , they are assumed to be independent of each other and of the obligor returns. One stipulates that they are beta-distributed with parameters  $(a_i, b_i)$ .

#### Obligor Dependence Structure from Copulas

As was first recognized by Frey et al. [9] (see also [8]), copulas provide an elegant means for describing the obligor dependence structure in credit portfolio models. By virtue of Sklar's theorem, the joint distribution of the random vector  $\mathbf{R} = (R_1, \ldots, R_n)'$ can be factorized as

$$G(r_1,\ldots,r_n) = \mathbb{P}(R_1 \le r_1,\ldots,R_n \le r_n)$$
$$= C(G_1(r_1),\ldots,G_n(r_n)) \qquad (7)$$

where  $C$ , the copula associated with **R**, is the distribution function of a random vector with standard uniform marginal distributions. From standard arguments (see e.g., Copulas: Estimation; Copulas in Econometrics; or Copulas in Insurance and references therein),

$$\mathbb{P}(S_{1}^{\text{new}} = s_{1}, \dots, S_{n}^{\text{new}} = s_{n})$$

$$= \mathbb{P}(d_{s_{1}}^{(1)} < R_{1} \leq d_{s_{1}+1}^{(1)}, \dots, d_{s_{n}}^{(n)} < R_{n} \leq d_{s_{n}+1}^{(n)})$$

$$= \int_{d_{s_{1}}^{(1)}}^{d_{s_{1}+1}} \dots \int_{d_{s_{n}}^{(n)}}^{d_{s_{n}+1}} dG(r_{1}, \dots, r_{n})$$

$$= \int_{G_{1}(d_{s_{1}}^{(1)})}^{G_{1}(d_{s_{1}}^{(1)})} \dots \int_{G_{n}(d_{s_{n}}^{(n)})}^{G_{n}(d_{s_{n}}^{(n)})} dC(u_{1}, \dots, u_{n})$$

$$(8)$$

Note that the integration limits  $G_i(d_{s_i}^{(i)}) =$  $\sum_{k=0}^{s_i-1} m_{S^{\text{init}},k}$  do not depend on  $G_i$ . This implies that the joint distribution of the ratings vector  $S^{new}$  is determined by the initial obligor ratings, the credit migration matrix  $M$  and the copula  $C$ ; the marginal distributions  $G_i$  do not matter.

This result helps to categorize threshold credit portfolio models; models using the same families of copulas can be considered as structurally equivalent. The copula associated with a Gaussian random vector

is called Gaussian copula and depends on the correlation matrix only. Since the returns  $\mathbf{R}$  are multivariate Gaussian, the original CreditMetrics model [13] is referred to as having a Gaussian copula. Replacing the Gaussian copula family by other families gives different models. Frey et al. [9] study the CreditMetrics model with Student- $t$  copulas and find that the tail of the loss distribution is considerably fatter as compared with the Gaussian copula with identical correlation parameters.

#### CreditMetrics as a Mixture Model

We now interpret the CreditMetrics model in a conditional fashion in order to better understand the meaning of the factors F. To this end, we look at the vector of default indicators  $\mathbf{D} = (D_1, \ldots, D_n)'$ , where  $D_i = I_{\{S_i^{\text{new}}=0\}}$ . We denote the default probabilities by  $\bar{p}_i = \mathbb{P}(D_i = 1)$ . Then conditional on the factors  $\mathbf{F}$ , the vector  $\mathbf{D}$  consists of *independent* Bernoulli random variables with success probabilities

$$p_{i}(\mathbf{F}) = \mathbb{P}(D_{i} = 1 \mid \mathbf{F})$$
$$= \Phi\left(\frac{\Phi^{-1}(\bar{p}_{i}) - \psi_{i}(\mathbf{F})}{\sqrt{1 - \text{Var}(\psi_{i}(\mathbf{F}))}}\right) \tag{9}$$

We deduce that one can simulate  $\mathbf{D}$  by first drawing  $\mathbf{F}$  from a multivariate Gaussian distribution and then generating independent Bernoulli random variables with success probabilities  $p_i(\mathbf{F})$ . From this angle,  $F$  represents the state of the economy that determines the obligor default probabilities. The distribution of  $\mathbf{D}$ , which is obtained from "mixing" the conditional distributions of  $\mathbf{D}$  by  $\mathbf{F}$ , is a so-called Bernoulli mixture:

$$\mathbb{P}(D_1 = d_1, \dots, D_n = d_n)$$
  
= 
$$\mathbb{E}\left(\mathbb{P}(D_1 = d_1, \dots, D_n = d_n \mid \mathbf{F})\right)$$
  
= 
$$\mathbb{E}\left(\prod_{i=1}^n p_i(\mathbf{F})^{d_i}(1 - p_i(\mathbf{F}))^{1-d_i}\right) \quad (10)$$

The conditional view offers computational advantages. Finger [6] exploits it for the determination of credit portfolio distributions. Using the Poisson approximation for sums of independent Bernoulli variables, various authors have shown that Credit-Metrics is approximated by a Poisson mixture model; this allows one to make a link to CreditRisk+ (see [3, 8, 11] for details).

## Asymptotic Behavior of CreditMetrics

In CreditMetrics, risk measures such as VaR (Value-at-Risk) or ES (expected shortfall) cannot be expressed in terms of simple closed formulas. For their estimation, one has to resort to Monte-Carlo (MC) simulation or other numerical methods (see Credit Portfolio Simulation). Although the topic of approximations in credit portfolio models is covered in **Large Pool Approximations**; Saddlepoint Approximation, we provide a brief discussion because the asymptotic results provide important qualitative insights.

Concerning approximation, research has dealt with strong limits of the relative portfolio loss and the tail behavior of the loss distribution when the number of obligors tends to infinity. While the derivation of strong limits consists of straightforward applications of the strong law of large numbers, the analysis of the tail behavior of the loss is more involved. For the tail behavior, we refer to [18] and a recent article by Glasserman et al. [10].

We next present the idea of the so-called large pool approximation. To this end, we work in a simplified framework that is adapted to loan portfolios. We assume that recovery rates, spreads, and interest rates are all equal to zero. Every obligor  $i$  has an outstanding loan of size  $e_i$ . Then the loss in the period  $(0, T]$  is given by

$$L_n = \sum_{i=1}^n e_i D_i \tag{11}$$

We define total exposure by  $e = \sum_{i=1}^{n} e_i$  and set  $\bar{L}_n = L_n/e$  for the relative loss of the portfolio. We want to verify to which extent the specific risk caused by the obligor-specific returns  $\epsilon_i$  is diversified away when the number of obligors grows. To this end, we decompose the relative loss into a systematic and an obligor-specific component:

$$\bar{L}_n = \mathbb{E}(\bar{L}_n \mid \mathbf{F}) + \Delta_n \tag{12}$$

It is straightforward to show that obligor-specific variance tends to zero as  $n \to \infty$ , provided the Herfindahl index, which measures exposure concentration, converges to zero:

$$\operatorname{Var}(\Delta_n) \to 0 \quad \text{ if } \quad H_n = \frac{1}{e} \sum_{i=1}^n e_i^2 \to 0 \quad (13)$$

The stronger property that  $\Delta_n$  converges almost surely to zero holds true (see e.g. [8] for a proof). This justifies the following approximation for large portfolios with no severe exposure concentration:

$$\bar{L}_n \approx \mathbb{E}(\bar{L}_n \mid \mathbf{F}) = \frac{1}{e} \sum_{i=1}^n p_i(\mathbf{F}) \qquad (14)$$

This means that for  $n$  large enough, the relative loss virtually coincides with its systematic component, or in other words, the idiosyncratic risks are diversified away and one is left with systematic risk (caused by  $\mathbf{F}$ ) only. The systematic risk cannot be diversified away other than by hedges that impact  $\mathbb{E}(\bar{L}_n | \mathbf{F})$ . Despite this positive result, one should be aware that the portfolio R-squared is typically significantly lower than the R-squared in long-only equity portfolios with a similar number of securities. This indicates that in credit portfolios the idiosyncratic risks are comparatively more important than in equity portfolios, or in other words, more securities are necessary to diversify a credit portfolio. This feature is due to the fact that the default correlations  $\text{Corr}(D_i, D_{i'})$  are very low (less than  $5\%$ ) for typical values of asset correlations (10–30%) and default probabilities.<sup> $e$ </sup>

The large pool approximation  $(14)$  lies at the core of the capital requirement in the Basel II internal ratings-based (IRB) approach. The IRB approach imposes a constant correlation Gaussian one-factor model, that is,  $\psi_i(\mathbf{F}) = \sqrt{\rho} \mathbf{F}$  in (5), and  $\mathbf{F} \sim \mathcal{N}(0, 1)$ is a latent (unobserved) factor. IRB assumes that the portfolio is infinitely fine-grained, that is, it neglects  $\Delta_n$  and calculates risk directly from  $\mathbb{E}(\bar{L}_n | \mathbf{F})$ . Since the latter is the sum of  $\text{comonotonic}^f$  (or perfectly positive dependent) obligor contributions, portfolio VaR is just the sum of the obligor VaR contributions. For an explanation of the additional multiplicative adjustments for maturities and rules for the choice of  $\rho_i$  applied by the IRB approach, we refer to **Internal**ratings-based Approach, [7, 12].

If the default probabilities in the constant correlation Gaussian one-factor model are constant and equal to  $\bar{p}$ , the limit  $\mathbb{E}(\bar{L}_n | \mathbf{F})$  is a so-called probitnormal random variable:

$$\bar{L}_n \approx p(\mathbf{F}) = \Phi\left(\frac{\Phi^{-1}(\bar{p}) - \sqrt{\rho}\mathbf{F}}{\sqrt{1-\rho}}\right) \tag{15}$$

This result goes back to [23, 24]. Studying the properties of the probit-normal distribution reveals that the tail behavior of  $\bar{L}_n$  is essentially governed by the correlation; the larger the  $\rho$ , the thicker the tail of the distribution of  $\bar{L}_n$ . Along the same lines one can analyze the tails of credit-migration-based models with non-Gaussian copulas, as was done by Lucas et al. [18].

## **Model Estimation**

Statistical inference poses a big challenge in CreditMetrics and related models. No estimation method that we know of is truly flawless because assumptions that are difficult to verify are ever involved. As we have seen, the model  $(2)$  is fully determined by the credit migration matrix and the matrix of asset correlations. In what follows, we take the existence of a credit migration matrix for granted (see Rating Transition Matrices) and restrict our discussion to the estimation of asset correlations. See also Portfolio Credit Risk: Statistical Methods for a general discussion of statistical methods for the calibration of credit portfolio models. We distinguish between *direct* and *indirect* approaches. The direct approaches start by estimating the exposures and variances in the factor model  $(4)$ , typically by regressions against certain predefined factors; the asset correlations are then easily derived. In the indirect approaches, asset correlations are inferred from historical default data.

CreditMetrics uses a direct approach. A major difficulty is that firm asset values cannot be directly observed, even for companies that have publicly traded equity. CreditMetrics circumvents this problem by assuming that asset return correlations are proxied by equity return correlations, or in other words, it regards the  $R_i$ 's in equation (4) as equity returns. The CreditMetrics technical document [13] suggests to use MSCI industry and country index returns as explanatory factors. In principle, one could work with any other set of factors. A nice benefit of letting equity returns drive the rating transitions is the fact that CreditMetrics can be naturally embedded into market risk models of the RiskMetrics<sup>g</sup> type because the CreditMetrics risk factors are already part of the RiskMetrics factor universe. This allows the aggregation of credit and market risks in a straightforward fashion.

So far we have explained the case of obligors with publicly traded equity. For private firms, the betas are mostly set by resorting to economic arguments. Often one uses the obligor's country and industry or sector affiliations. Say, a firm has two equally large lines of businesses, which belong to the US Information Technology and US Consumer Discretionary sectors, respectively. Then the betas with respect to the MSCI US Information Technology and MSCI US Consumer Discretionary sector index returns would both be set to 0*.*5, and all other betas to zero. Another piece to specify is the variance of the idiosyncratic term in equation (4), or equivalently, the R-squared. Here CreditMetrics stipulates that Rsquareds obey *R*<sup>2</sup> = 1*/(*1 + *Aγ* exp*(λ))*, where *A* is the book value of the firm's total assets and *γ* and *λ* are fixed parameters estimated from a cross-section of traded stocks; we refer to [14] for a critical appraisal of this method. Alternatively, R-squared can be set by the experienced user.

We mention that KMV uses a direct approach as well, but in contrast to CreditMetrics it reconstructs the asset values from the equity price history using the Merton model framework; see [17] for details about this reconstruction and [16] for a description of the structure of the KMV factor model.

The indirect approaches apply statistical inference to time-series of count data of defaults. These methods are constricted by the sparsity of clean data. Since defaults rarely happen and the time-series are short, one creates groups of obligors and assumes that asset correlations in these groups are constant. There exist several studies following an indirect approach. Bluhm *et al.* [1] back out asset correlations in rating classes from standard deviations of historical default rates. De Servigny and Renault [22] infer default correlation from observed joint defaults. Demey *et al.* [4] use maximum-likelihood estimation and reduce the number of parameters by assuming that both asset correlations between and within rating classes are constants. Hamerle and Rosch [15] ¨ also apply maximum-likelihood estimation, but advocate the use of lagged macroeconomic variables as additional predictors.

## **End Notes**

a*.* RiskMetrics and CreditMetrics are registered trademarks of RiskMetrics Group, Inc. and its affiliates.

b*.* Since the original development of the model, the KMV company was acquired by Moody's, Inc. and is now part of Moody's KMV.

c*.* Moody's KMV EDF, which we refer to as simply EDF, is a trademark of Moody's KMV. See www.moodyskmv.com. d*.* Equivalently, the loss is determined by the loss given default (LGD) specified for the position.

e*.* The picture is similar when R-squared is replaced by squared ratios of other risk measures.

f*.* See e.g., McNeil *et al.* [19] for formal definition of comonotonicity.

g*.* See Mina and Xiaao [21] for an introduction to RiskMetrics.

## **References**

- [1] Bluhm, C., Overbeck, L. & Wagner, C. (2003). *An Introduction to Credit Risk Modeling*, John Wiley & Sons.
- [2] Crosbie, P. & Bohn, J.R. (2003). *Modeling Default Risk*. Available at www.moodyskmv.com.
- [3] Crouhy, M., Galai, D. & Mark, R. (2000). A comparative analysis of current credit risk models, *Journal of Banking and Finance* **24**, 59–117.
- [4] Demey, P., Jouanin, J.-F., Roget, C. & Roncalli, T. (2004). Maximum likelihood estimate of default correlations, *Risk*, November, 104–108.
- [5] Duffie, D. & Singleton, K.J. (2003). *Credit Risk: Pricing, Measurement, and Management*, Princeton Series in Finance, Princeton University Press.
- [6] Finger, C.C. (1999). Conditional approaches for CreditMetrics portfolio distributions, *CreditMetrics Monitor* April, 14–33.
- [7] Finger, C.C. (2001). The one-factor CreditMetrics model in the new Basel Capital Accord, *RiskMetrics Journal* 9–18.
- [8] Frey, R. & McNeil, A.J. (2003). Dependent defaults in models of portfolio credit risk, *Journal of Risk* **6**(1), 59–92.
- [9] Frey, R., McNeil, A.J. & Nyfeler, M. (2002). Copulas and credit models, *Risk*, October, 111–114.
- [10] Glasserman, P., Kang, W. & Shahabuddin, P. (2007). Large deviations in multifactor portfolio credit risk, *Mathematical Finance* **17**(3), 345–379.
- [11] Gordy, M.B. (2000). A comparative anatomy of credit risk models, *Journal of Banking and Finance* **24**, 119–149.
- [12] Gordy, M.B. (2003). A risk-factor model foundation for ratings-based bank capital rules, *Journal of Financial Intermediation* **12**, 199–232.

- [13] Gupton, G.M., Finger, C.C. & Bhatia, M. (1997). *CreditMetrics–Technical Document*, J.P. Morgan & Co. Incorporated.
- [14] Hahnenstein, L. (2004). Calibrating the CreditMetrics correlation concept—empirical evidence from Germany, *Financial Markets and Portfoliomanagement* **18**, 358–381.
- [15] Hamerle, A. & Rosch, D. (2006). Parameterizing credit ¨ risk models, *Journal of Credit Risk* **2**(4), 101–122.
- [16] Kealhofer, S. & Bohn, J.R. (2001). *Portfolio Management of Default Risk*. Available at www.moodyskmv. com
- [17] Lando, D. (2004). *Credit Risk Modeling*, Princeton Series in Finance, Princeton University Press.
- [18] Lucas, A., Klaassen, P., Spreij, P. & Straetmans, S. (2001). An analytical approach to credit risk in large corporate bond and loan portfolios, *Journal of Banking and Finance* **2**, 1635–1664.
- [19] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management*, Princeton Series in Finance, Princeton University Press.

- [20] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [21] Mina, J. & Xiaao, J.Y. (2001). *Return to RiskMetrics: The Evolution of a Standard*, RiskMetrics Group.
- [22] de Servigny, A. & Renault, O. (2003). Correlation evidence, *Risk*, July, 90–94.
- [23] Vasicek, O.A. (1987). *Probability of Loss on Loan Portfolio*. Available at www.moodyskmv.com
- [24] Vasicek, O.A. (2002). Loan portfolio value, *Risk*, December, 160–162.

## **Related Articles**

**Exposure to Default and Loss Given Default**; **Gaussian Copula Model**; **Large Pool Approximations**; **Structural Default Risk Models**; **Rating Transition Matrices**.

> DANIEL STRAUMANN & CHRISTOPHER C. FINGER
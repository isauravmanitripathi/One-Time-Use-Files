# Portfolio Credit Risk: **Statistical Methods**

This article gives a brief overview over statistical methods for estimating the parameters of credit portfolio models from default data. The focus is on models for default probability and correlations; for recovery rates, (see **Recovery Rate**). First, a rather general model setting is introduced along the lines of the models of McNeil and Wendin [10] and others, who depict portfolio models as generalized linear mixed models (GLMMs). Then, we describe the most common estimation techniques, which are the method of moments and maximum likelihood. An excellent reference for other estimation techniques is [10], in particular for Bayes estimation.

#### A Single Obligor's Default Risk

Let  $D_{ti}$  denote an indicator variable for obligor *i*'s default in time period  $t$  such that

$$D_{ti} = \begin{cases} 1 & \text{borrower } i \text{ defaults in } t \\ 0 & \text{otherwise} \end{cases} \tag{1}$$

 $i \in \mathbb{N}_t, t = 1, \ldots, T$ , where  $\mathbb{N}_t$  is the set of firms under consideration at the beginning of time period t and  $n_t = |\mathbb{N}_t|$  is their cardinal number. The default indicator variable can be motivated in terms of a threshold approach wherein default is said to occur when a continuous variable falls below a threshold. This approach is based on the asset value model due to Merton [11] where the firm declares bankruptcy when the value of its asset is below the principal value of its debt at maturity. Let  $V_{ti}$ denote the asset value return of firm  $i$  at time  $t$  $(i \in \mathbb{N}_t, t = 1, \ldots, T)$ , or more generally a variable representing an obligor's credit quality. Then, the obligor defaults when  $V_{ti}$  falls below a threshold  $c_{ti}$ , that is,  $D_{ti} = 1 \Leftrightarrow V_{ti} < c_{ti}$ . Crucial parts in credit risk management now are the modeling of  $V_{ti}$ , the parameterization of  $c_{ti}$ , and finally the estimation of parameter. In most industry credit risk models, such as credit metrics, credit risk plus, and credit portfolio view, the triggering variable  $V_{ti}$  is driven by two sources of random factors. The first is a systematic random factor  $F_t$  following a distribution  $G$ , which affects all firms jointly and therefore cannot

be diversified away. The second is an idiosyncratic part  $\varepsilon_{ti}$  with variance  $\sigma^2$ , which is specific for each firm, independent between the firms and from the systematic factor. The default threshold  $c_{ti}$  is mostly modeled via credit ratings that reflect an aggregated summary of a firm's risk characteristics. In a simple case, both variables may be expressed as linear functions of the respective risk drivers, such that  $V_{ti} = -\omega F_t + \varepsilon_{ti}$  and  $c_{ti} = \alpha + \boldsymbol{\beta}' \mathbf{x}_{ti}$  where  $\alpha$ ,  $\boldsymbol{\beta}$ , and  $\omega$  are unknown parameters, and  $\mathbf{x}_{ti}$  is a design vector consisting of observable covariates for obligor  $i$ , which may be time- and obligor-specific (such as balance sheet ratios) or only time-specific (such as macroeconomic variables). Then the firm defaults if  $V_{ti} < \alpha + \boldsymbol{\beta}' \mathbf{x}_{ti}$ . As shown in [7], the aforementioned credit risk models mainly differ in the distributional assumptions regarding the common and the idiosyncratic random factors driving the firm value as discussed below.

The probability of the firm's default conditional on the random factor  $f_t$  can be expressed as

$$\begin{aligned} \textit{CPD}_{ti}(f_t) &= P(D_{ti} = 1 | \mathbf{x}_{ti}, f_t) \\ &= P(V_{ti} < \alpha + \boldsymbol{\beta}' \mathbf{x}_{ti} | \mathbf{x}_{ti}, f_t) \\ &= P(\varepsilon_{ti} < \alpha + \boldsymbol{\beta}' \mathbf{x}_{ti} + \omega f_t) \\ &= f\left(\alpha + \boldsymbol{\beta}' \mathbf{x}_{ti} + \omega f_t\right) \end{aligned} \tag{2}$$

which in statistical terms is a  $GLMM$ ; see [10] and the references cited therein.  $f_t$  is a realization of the systematic factor  $F_t$ , which is called the *time*specific random effect.  $f(.): \mathbb{R} \rightarrow (0, 1)$  denotes a response or link function given by the distribution of the idiosyncratic random error  $\varepsilon_{ti}$ . In the credit metrics model, the idiosyncratic errors are standard normally distributed ( $\sigma^2 = 1$ ), whereas in the credit portfolio view model the idiosyncratic error follows a logistic distribution ( $\sigma^2 = \pi^2/3$ ). This leads to the common link functions of the probit  $f(y) = \Phi(y)$ or the logit function  $f(y) = 1/(1 + \exp(-y))$ . In the credit risk plus approach, the systematic and the unsystematic factors are linked multiplicatively rather than linearly and their distributions are Gamma and Exponential, respectively. For details, we refer to [7].

The (with respect to the random effect unconditional) probability of default (PD) is given by the expectation

$$PD_{ti} = P(D_{ti} = 1 | \mathbf{x}_{ti})$$
  
=  $\int f(\alpha + \boldsymbol{\beta}' \mathbf{x}_{ti} + \omega f_t) \, \mathrm{d}G(f_t)$  (3)

which depends on the distribution of the random factor. For example, in the credit metrics model, the random effect is assumed to follow a standard normal distribution. Then, in the probit model, the simple expression for the unconditional PD

$$PD_{ti} = P(D_{ti} = 1 | \mathbf{x}_{ti}) = \Phi(\tilde{\alpha} + \tilde{\boldsymbol{\beta}}' \mathbf{x}_{ti}) = \Phi(\tilde{c}_{ti})$$
(4)

results, where  $\tilde{c}_{ti} = \tilde{\alpha} + \tilde{\boldsymbol{\beta}}' \mathbf{x}_{ti}$ ,  $\tilde{\alpha} = \alpha / \sqrt{1 + \omega^2}$  and  $\tilde{\boldsymbol{\beta}} = \boldsymbol{\beta}/\sqrt{1+\omega^2}$ . The correlation between the latent variables of obligor  $i$  and  $j$ ,  $i \neq j$  is given by  $\n\rho_{ij} \equiv \rho = \frac{\omega^2}{1 + \omega^2}\n$ , which is sometimes referred to as asset correlation since the latent variables are interpreted as asset value return. See [5] for a detailed description of correlations. For the aforementioned distributions in the credit portfolio view and the credit risk plus approach and the empirical estimation, compare [8].

## Portfolio Default Risk

The vector of default indicators of the portfolio is denoted by  $\mathbf{D}_t = (D_{t1}, \ldots, D_{tn})$ . Conditional on the systematic random factor and given the  $\mathbf{x}_{ti}$ , the defaults are independent. Then the joint distribution of defaults conditional on the systematic factor is given by

$$P(\mathbf{D}_{t} = \mathbf{d}_{t} | \mathbf{x}_{ti}, f_{t}) = \prod_{i \in \mathbb{N}_{t}} P(D_{ti} = 1 | \mathbf{x}_{ti}, f_{t})^{d_{ti}}$$
$$\times (1 - P(D_{ti} = 1 | \mathbf{x}_{ti}, f_{t}))^{1 - d_{ti}} \qquad (5)$$

which is also known as a *Bernoulli mixture model* [6]. The unconditional distribution (where unconditional refers w.r.t. the random effect) is obtained as

$$P(\mathbf{D}_t = \mathbf{d}_t | \mathbf{x}_{ti}) = \int P(\mathbf{D}_t = \mathbf{d}_t | \mathbf{x}_{ti}, f_t) \mathrm{d}G(f_t) \tag{6}$$

Extensions of model (5) include more than one random effect and are, therefore, called *multifactor* models.

A special case of this model results if the obligors are homogeneous in  $\mathbf{x}_{ti}$ , that is,  $\mathbf{x}_{ti} = \mathbf{x}_t$  and thus  $c_{ti} = c_t$  for all *i*. Then, all obligors exhibit the same conditional PD and the Bernoulli mixture distribution (5) drops to the binomial mixture distribution. Let  $D_t = \sum_{i \in \mathbb{N}_t} D_{ti}$  be the number of defaults. Then.

$$P(D_t = d_t | \mathbf{x}_t, f_t) = {n_t \choose d_t} P(D_{ti} = 1 | \mathbf{x}_t, f_t)^{d_t}$$
$$\times (1 - P(D_{ti} = 1 | \mathbf{x}_t, f_t))^{n_t - d_t} \tag{7}$$

with the unconditional distribution analogous to equation (6). Define the default rate  $p_t = d_t/n_t$  as the ratio of defaulting obligors divided by the total number of obligors. As shown in [15, 16], the distribution of the default rate converges against the "Vasicek"distribution if the random effect is standard normally distributed and the number of obligors goes to infinity. The density is then given as

$$f(p_t) = \frac{\sqrt{1-\rho}}{\sqrt{\rho}} \cdot \exp\left(\frac{1}{2}(\Phi^{-1}(p_t))^2 - \frac{1}{2\rho^2}(c_t - \sqrt{1-\rho^2} \cdot \Phi^{-1}(p_t))^2\right) \tag{8}$$

For a thorough description of large pool approximations, see [9].

#### **Estimation Techniques**

There are basically two ways of estimating the unknown model parameters. As the first way, one can use asset values and asset value returns as in the KMV approach [1]. Given the level of liabilities, the default probabilities can be derived. Correlation estimates are obtained by calculating historical correlations from asset value returns. As the crucial part of these methods is deriving the asset values and the capital structure of the firm rather than the statistical procedures, they are not discussed here in detail. Instead, we refer to [3] and the references cited therein. As the second way, the parameters can be estimated using time series  $\mathbf{d}_1, \ldots, \mathbf{d}_T$  of observed default events. The simplest methods can

be employed for the case of the homogeneous portfolio with time-constant parameters where closed-form solutions for the estimators exist. In the GLMM model, more advanced numerical techniques have to be used. Here, we briefly describe the method of moments and the maximum-likelihood method. For Bayes estimation, we refer to  $[10]$  and the references cited therein.

### Method of Moments

If the obligors in the portfolio or the segment are homogeneous and the parameters are constant, only two parameters are to be estimated, namely, the PD and the correlation. Gordy [7] applies the method of moments estimator to the probit model. He shows that expectation and variance of the conditional default probability are

$$E\left(CPD(F_t)\right) = PD\tag{9}$$

and

Var 
$$(CPD(F_t))$$
  
=  $\Phi_2 \left( \Phi^{-1}(PD), \Phi^{-1}(PD), \rho \right) - PD^2$  (10)

where  $\Phi_2(\cdot)$  is the bivariate normal cumulative distribution function for two random variates, with expectation zero and variance one each and correlation  $\rho$ . An unbiased estimator for the unconditional PD is given by the average default rate:

$$\bar{p} = \frac{1}{T} \sum_{t=1}^{T} p_t \tag{11}$$

The left-hand side of equation (10) can be estimated by the sample variance of the default rate:

$$s_p^2 = \frac{1}{T-1} \sum_{t=1}^T (p_t - \bar{p})^2 \tag{12}$$

Given the two estimates, the asset correlation  $\rho$ can be backed out numerically from equation (10). Gordy [7] also provides a finite sample adjustment for the estimator. However, this modified estimator turns out to perform similar to the simple estimator [3].

#### Maximum-likelihood Method

In the limiting case  $(8)$ , asymptotic maximumlikelihood estimators of the (homogeneous) PD and the (homogeneous) asset correlation can be derived as

$$\widehat{o} = \frac{m_2/T - m_1^2/T^2}{1 + m_2/T - m_1^2/T^2} \tag{13}$$

$$\widehat{PD} = \Phi(T^{-1}\sqrt{1-\widehat{\rho}}m_1) \tag{14}$$

where  $m_1 = \sum_{t=1}^{T} p_t$  and  $m_2 = \sum_{t=1}^{T} p_t^2$  [4].<br>In the general case of the GLMM where obligors

are heterogeneous, the log-likelihood is given via equation  $(6)$  as

$$l = \sum_{t=1}^{T} \ln \int \prod_{i \in \mathbb{N}_{t}} P(D_{ti} = 1 | \mathbf{x}_{ti}, f_{t})^{d_{ti}}$$
$$(1 - P(D_{ti} = 1 | \mathbf{x}_{ti}, f_{t}))^{1 - d_{ti}} \, \mathrm{d}G(f_{t}) \tag{15}$$

As the log-likelihood function includes solving several integrals, it is numerically optimized w.r.t. the unknown parameters for which several algorithms, such as the Newton-Raphson method, exist and are implemented in many statistical software packages. The integral approximation can be conducted by, for example, the adaptive Gaussian quadrature as described in [12]. Under usual regulatory conditions, the resulting estimators asymptotically exist, are consistent, and converge against normality. See [2], p.243, for a detailed discussion. Applications and estimation results can, for instance, be found in [6, 8, 13, 14]. For the extension of higher dimensional random effects, there are also some approximation methods that can be used, particularly penalized quasi-likelihood (PQL) and marginal quasi-likelihood (MQL) [10].

#### Bayes Estimation

Finally, Bayes estimation can be used for estimation as thoroughly shown in [10]. The joint prior distribution of  $F_t$ ,  $\beta$  (including a constant) and some hyperparameters  $\theta$  can be given as

$$p(\boldsymbol{\beta}, F_t, \theta) = p(F_t|\theta) \cdot p(\theta) \cdot p(\boldsymbol{\beta}) \qquad (16)$$

where *a priori* independence between  $\beta$  and  $\theta$  is assumed. Mostly, Markov chain Monte Carlo methods are applied, which can deal with even more complex models than shown here, such as autocorrelated random effects or multifactor models. For a detailed description, we refer to [10].

# **References**

- [1] Bohn, J. & Crosbie, P. (2003). *Modeling Default Risk*, *KMV Corporation*.
- [2] Davidson, R. & MacKinnon, J.G. (1993). *Estimation and Inference in Econometrics*, Oxford University Press, New York.
- [3] Duellmann, K., Kll, J. & Kunisch, M. (2008). *Estimating Asset Correlations from Stock Prices or Default Rates which Method is Superior?* Deutsche Bundesbank Discussion Paper, Series 2: Banking and Finance, Deutsche Bundesbank, Vol 04.
- [4] Duellmann, K. & Trapp, M. (2005). Systematic risk in recovery rates- an empirical analysis of U.S. corporate credit exposures, in *Recovery Risk: The Next Challenge in Credit Risk Management*, E.I. Altman, A. Resti & A. Sironi, eds. Deutsche Bundesbank.
- [5] Frey, R. (2009). Default correlation and asset correlation, *Encyclopedia of Quantitative Finance* **10**, 038.
- [6] Frey, R. & McNeil, A. (2003). Dependent defaults in models of portfolio credit risk, *Journal of Risk* **6**, 59–92.
- [7] Gordy, M.B. (2000). A comparative anatomy of credit risk models, *Journal of Banking and Finance* **24**, 119–149.

- [8] Hamerle, A. & Roesch, D. (2006). Parameterizing credit risk models, *Journal of Credit Risk* **3**, 101–122.
- [9] Kreinin, A. (2009). Large pool approximations for credit loss, *Encyclopedia of Quantitative Finance* **09**, 017.
- [10] McNeil, A.J. & Wendin, J.P. (2007). Bayesian inference for generalized linear mixed models of portfolio credit risk, *Journal of Empirical Finance* **14**, 131–149.
- [11] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [12] Pinheiro, J.C. & Bates, D.M. (1995). Approximations to the log-likelihood function in the nonlinear mixedeffects model, *Journal of Computational and Graphical Statistics* **4**, 12–35.
- [13] Roesch, D. (2005). An empirical comparison of default risk forecasts from alternative credit rating philosophies, *International Journal of Forecasting* **25**, 37–51.
- [14] Roesch, D. & Scheule, H. (2005). A multi-factor approach for systematic default and recovery risk, *Journal of Fixed Income* **15**, 63–75.
- [15] Vasicek, O.A. (1987). *Probability of Loss on Loan Portfolio*. Working paper, KMV Corporation.
- [16] Vasicek, O.A. (1991). *Limiting Loan Loss Distribution*. Working paper, KMV Corporation.

DANIEL ROSCH ¨
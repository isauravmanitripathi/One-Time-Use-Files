# **GARCH Models**

## **Univariate Models of Conditional** Heteroskedasticity

## The ARCH Model

Financial economists are concerned with modeling and forecasting volatility in asset returns. This is the case since volatility is considered a measure of risk, and investors want a premium for investing in risky assets. Marginal distributions of typical return series have heavy tails, and the series show clustering of volatility. Furthermore, these series have little or no autocorrelation, but they do display higher order dependence. For example, the squared returns are positively autocorrelated. The autoregressive conditional heteroskedasticity (ARCH) model and its variants have been found useful in describing data with these properties.

The original ARCH model, introduced by Engle [21], can be defined as follows. Let  $\varepsilon_t$  be a random variable that has a mean and a variance conditionally on the information set  $\mathcal{F}_{t-1}$  that contains all past information up until  $t-1$  and available at time t. The ARCH model of  $\varepsilon_t$  has the following properties. First, the conditional mean  $\mathsf{E}\{\varepsilon_t|\mathcal{F}_{t-1}\}=0$  and, second, the conditional variance  $h_t = \mathsf{E}\{\varepsilon_t^2 | \mathcal{F}_{t-1}\}\$  is a nontrivial positive-valued parametric function of  $\mathcal{F}_{t-1}$ . The sequence  $\{\varepsilon_t\}$  may be observed directly. In that case it may be, for example, a sequence of daily returns of an asset or an index. It may also be an unobserved error or innovation sequence of an econometric model. In the latter case,

$$\varepsilon_t = y_t - \mathsf{E}\{y_t | \mathcal{F}_{t-1}\}\tag{1}$$

where  $y_t$  is an observable random variable and  $\mathsf{E}\{y_t|\mathcal{F}_{t-1}\}\$  is the conditional mean of  $y_t$  given  $\mathcal{F}_{t-1}$ . Here, the focus is on  $h_t$  and it is assumed that  $\mathsf{E}\{y_t|\mathcal{F}_{t-1}\}=0.$ 

Engle assumed that  $\varepsilon_t$  can be decomposed as follows: 1 10

$$\varepsilon_t = z_t h_t^{1/2} \tag{2}$$

where  $\{z_t\}$  is a sequence of independent, identically distributed (iid) random variables with zero mean and unit variance. This implies  $\varepsilon_t | \mathcal{F}_{t-1} \sim \mathcal{D}(0, h_t)$ where  $\mathcal{D}$  stands for a distribution, assumed to be

either a normal distribution or a leptokurtic one, such as the *t*-distribution. The information set  $\mathcal{F}_{t-1}$  =  $\{\varepsilon_{t-j}: j \ge 1\}$ . The conditional variance of an ARCH model of order  $q$  has the following parametric form:

$$h_t = \alpha_0 + \sum_{j=1}^{q} \alpha_j \varepsilon_{t-j}^2 \tag{3}$$

where  $\alpha_0 > 0, \alpha_j \ge 0, j = 1, ..., q - 1, \text{ and } \alpha_q > 0.$ 

The parameter restrictions in equation  $(3)$  form a necessary and sufficient condition for positivity of the conditional variance. Suppose the unconditional variance  $\mathsf{E}\varepsilon_t^2 = \sigma^2 < \infty$ . The definition of  $\varepsilon_t$  through the decomposition (2) involving  $z_t$  then guarantees the white noise property of the sequence  $\{\varepsilon_t\}$ , since  $\{z_t\}$  is a sequence of iid variables. In fact, the ARCH model can be viewed as a special case of the family of models with uncorrelated observations but higher order dependence, such that the squared observations are correlated.

The ARCH model and its generalizations are applied to modeling, among other things, highfrequency data on interest rates, exchange rates and stock and stock index returns. "High frequency" in this context means weekly, daily, or intradaily observations. Bollerslev et al. [12] already listed a large variety of applications in their survey of these models, and their number has increased enormously since then. Forecasting volatility of these series is different from forecasting the conditional mean of a process because volatility, the object to be forecast, is not observed. The question then is how volatility should be measured. Using  $\varepsilon_t^2$  is an obvious solution, but it is not necessarily a good one if data of higher frequency are available. Andersen and Bollersley [3] and others recommend realized volatility (see Realized Volatility and Multipower Variation) for the purpose; for a review see  $[2]$ .

#### The Generalized ARCH Model and Extensions

Generalized ARCH. The ARCH model has since been extended by adding lagged conditional variances to equation (3). This extension, called the *generalized* ARCH (GARCH) model, proposed independently by Bollerslev [10] and Taylor [67], has since become very popular. The  $GARCH(p, q)$  model has the following form:

$$h_{t} = \alpha_{0} + \sum_{j=1}^{q} \alpha_{j} \varepsilon_{t-j}^{2} + \sum_{j=1}^{p} \beta_{j} h_{t-j} \qquad (4)$$

A sufficient condition for the conditional variance  $h_t$  in equation (4) to be positive is  $\alpha_0 > 0$ ,  $\alpha_i \ge 0$ ,  $j = 1, \ldots, q; \ \beta_j \ge 0, \ j = 1, \ldots, p.$  This condition is not necessary if either  $p$  or  $q$ , or both, exceed 1; see [56]. For the GARCH model to be identified if at least one  $\beta_i > 0$  (the model is a genuine GARCH model), it is required that also at least one  $\alpha_i > 0$ . If  $\alpha_1 = \ldots = \alpha_q = 0$ , the conditional and unconditional variances of  $\varepsilon_t$  are equal and  $\beta_1, \ldots, \beta_p$  are unidentified nuisance parameters. The  $GARCH(p,q)$  process is weakly stationary if and only if  $\sum_{j=1}^{q} \alpha_j + \sum_{j=1}^{p} \beta_j < 1.$ 

The overwhelmingly most frequently applied  $GARCH$  model has been the  $GARCH(1,1)$  model. The weakly stationary  $GARCH(1,1)$  model only contains three parameters, but one more parameter can be saved by "variance targeting". The idea is to replace the intercept  $\alpha_0$  in equation (4) by  $(1 - \alpha_1 - \beta_1)\sigma^2$ where  $\sigma^2 = \mathsf{E}\varepsilon_t^2$ . The estimate  $\widehat{\sigma}^2 = T^{-1} \sum_{t=1}^T \varepsilon_t^2$  is substituted for  $\sigma^2$  before estimating the other two parameters. As a result, the conditional variance converges toward the "long-run" unconditional variance, which may be considered a desirable property of the model.

Since its introduction, the GARCH model has been generalized and extended in various directions. This has been done in order to increase the flexibility of the original model. Because it only contains squared lags of  $\varepsilon_t$ , the response of the conditional variance to a shock  $\varepsilon_t$  is independent of the sign of the shock and just a function of its size. Several extensions of the GARCH model aim at accommodating the asymmetry in the response, caused by the *leverage effect* present in stock returns. The most frequently applied asymmetric GARCH model is the GJR-GARCH model of [32]. It is defined as follows:

$$h_{t} = \alpha_{0} + \sum_{j=1}^{q} \{\alpha_{j} + \delta_{j} I(\varepsilon_{t-j} > 0)\}\varepsilon_{t-j}^{2}$$
$$+ \sum_{j=1}^{p} \beta_{j} h_{t-j} \qquad (5)$$

where  $I(\varepsilon_{t-i} > 0)$  is an indicator function obtaining value 1 when the argument is true and 0 otherwise. The asymmetry in the data is modeled through the terms  $\delta_j I(\varepsilon_{t-j} > 0) \varepsilon_{t-j}^2$ ,  $j = 1, \ldots, q$ , in equation (5). Typically, in applications,  $p = q = 1$ . Other asymmetric GARCH models include the asymmetric GARCH (AGARCH) of [27] and the quadratic GARCH of [59]. Furthermore, the smooth transition GARCH (STGARCH) model, introduced by Hagerud [38] and Gonzalez-Rivera [33], can be used for describing asymmetries in return series. This model contains a continuum of regimes, whereas in the GJR- $GARCH(1,1)$  model there are only two regimes with the switch point at  $\varepsilon_t = 0$ . The GJR-GARCH model is still linear in parameters, which makes it easier to estimate than, say, the STGARCH model that is genuinely nonlinear in parameters.

There are other nonlinear GARCH models that have been applied in practice. Perhaps the most prominent example is the Markov-switching GARCH model. It contains a finite number (usually two) of regimes, and the GARCH process switches between them according to a latent random variable. It was originally introduced as an ARCH model (see [16] and  $[39]$ ) and is in that form defined as follows:

$$h_{t} = \sum_{i=1}^{k} \left( \alpha_{0}^{(i)} + \sum_{j=1}^{q} \alpha_{j}^{(i)} \varepsilon_{t-j}^{2} \right) I(s_{t} = i) \qquad (6)$$

where  $s_t$  is the discrete latent random variable obtaining values from the set  $S = \{1, \ldots, k\}$  of regime indicators. It follows a (usually first-order) homogeneous Markov chain:

$$\Pr\{s_t = j | s_t = i\} = p_{ij}, \quad i, j = 1, \dots, k \tag{7}$$

hence the name Markov-switching GARCH. The transition probabilities  $p_{ij}$  are parameters to be estimated. An argument put forward to motivate the use of these models is that they can be applied in situations where the conditional variance process contains breaks, that is, sudden changes in parameters. Augmenting the ARCH form (6) by lags of the conditional variance causes estimation problems; see  $[35, 42]$  and  $[37]$  for discussion and solutions.

Modeling the Conditional Standard Deviation. Models for the conditional variance constitute the most popular way of modeling conditional heteroskedasticity. Similar models, however, have also

been constructed for the conditional standard deviation. By replacing  $h_t$  in equation (4) by  $h_t^{1/2}$ ,  $h_{t-j}$  by  $h_{t-j}^{1/2}$ ,  $j=1,\ldots,p$ , and  $\varepsilon_{t-j}^2$  by  $|\varepsilon_{t-j}|$ ,  $j=$  $1, \ldots, q$ , one obtains the absolute-valued GARCH model. Doing this in the GJR-GARCH model yields the threshold GARCH (TGARCH) model that [71] considered. The TGARCH $(p, q)$  model is usually parameterized somewhat differently from the GJR-GARCH model:

$$h_t^{1/2} = \alpha_0 + \sum_{j=1}^q (\alpha_j^+ \varepsilon_{t-j}^+ - \alpha_j^- \varepsilon_{t-j}^-) + \sum_{j=1}^q \beta_j h_{t-j}^{1/2}$$
(8)

where  $\varepsilon_{t-i}^+ = \max(\varepsilon_{t-j}, 0), \varepsilon_{t-i}^- = \min(\varepsilon_{t-j}, 0),$  and  $\alpha_i^+, \alpha_i^-, j = 1, \ldots, q$ , are the corresponding parameters. Like the GJR-GARCH model, even the TGARCH model is linear in parameters. It can be generalized by assuming the switch point to be an unknown parameter, which makes the model nonlinear in parameters. This type of threshold ARCH model was introduced by Li and Li [46] who also considered a threshold autoregressive conditional mean, but it has not enjoyed the same popularity as the TGARCH or the GJR-GARCH model.

## Integrated and Fractionally Integrated GARCH. In applications it often occurs, if the time series is sufficiently long, that the estimated sum of the parameters $\alpha_1$ and $\beta_1$ in the GARCH(1,1) model (equation (4) with $p = q = 1$ ) is close to unity. Engle and Bollerslev [24], who first paid attention to this phenomenon, suggested imposing the restriction $\alpha_1$ + $\beta_1 = 1$ and called the ensuing model an *integrated* GARCH (IGARCH) model. The IGARCH process is not weakly stationary as $\mathsf{E}\varepsilon_t^2$ is not finite but it is,

however, strongly stationary.

The empirical fact that the estimate of the sum  $\alpha_1 + \beta_1$  often lies close to unity has prompted discussion of its causes. First Diebold [18] and later Lamoureux and Lastrapes [44] suggested that this often happens if the intercept of the GARCH process does not remain constant during the estimation period. This may not be surprising as it means that the underlying GARCH process is not stationary. This has aroused interest in testing parameter constancy and finding breaks in the GARCH process; see, for example [43, 52] and [8].

The integrated GARCH model has also served as a starting point for so-called fractionally integrated GARCH (FIGARCH) models. The GARCH(1,1) equation (4) can be written in the " $ARMA(1,1)$  form" as follows:

$$\varepsilon_t^2 = \alpha_0 + (\alpha_1 + \beta_1)\varepsilon_{t-1}^2 + \nu_t - \beta_1 \nu_{t-1} \qquad (9)$$

where  $\{v_t\} = \{\varepsilon_t^2 - h_t\}$  is a martingale difference sequence with respect to  $h_t$ . For the IGARCH process, equation (9) has the " $ARIMA(0,1,1)$  form"

$$(1 - \mathsf{L})\varepsilon_t^2 = \alpha_0 + \nu_t - \beta_1 \nu_{t-1} \tag{10}$$

where L is the lag operator,  $Lx_t = x_{t-1}$ . The FIG- $ARCH(1,d,0)$  model is obtained from equation (10) simply by assuming that the difference in equation (10) is *fractional* (see **Long Range Dependence**) instead of the conventional one:

$$(1 - \mathsf{L})^{d} \varepsilon_{t}^{2} = \alpha_{0} + \nu_{t} - \beta_{1} \nu_{t-1} \tag{11}$$

where  $d$  is the fractional order of integration. The FIGARCH equation (11) can be written as an infinite-order ARCH model by applying the definition  $v_t = \varepsilon_t^2 - h_t$  to it. This yields

$$h_t = \alpha_0 (1 - \beta_1)^{-1} + \lambda(\mathsf{L}) \varepsilon_t^2 \tag{12}$$

where  $\lambda(L) = \{1 - (1 - L)^d (1 - \beta_1 L)^{-1}\} \varepsilon_t^2 = \sum_{i=1}^{\infty} \cdot$  $\lambda_j \mathsf{L}^j \varepsilon_t^2$ , and  $\lambda_j \ge 0$  for all j. Expanding the fractional difference operator into an infinite sum yields the result that for long lags  $j$ ,

$$\lambda_j = \{ (1 - \beta_1) \Gamma(d)^{-1} \} j^{-(1-d)} = c j^{-(1-d)}, \quad c > 0$$
(13)

where  $d \in (0, 1)$  and  $\Gamma(d)$  is the gamma function. When  $d > 0.5$ , the FIGARCH model is not weakly stationary. From equation  $(13)$  it is seen that the effect of the lag  $\varepsilon_{t-i}^2$  on the conditional variance decays hyperbolically as a function of the lag length  $j$ . A very slow decay of the autocorrelation function of  $\{\varepsilon_t^2\}$  is a frequently encountered empirical fact in return series, and this is the reason for developing the FIGARCH model (see [5]). But then, it has been argued (see for example [54]) that the observed slow decay is due to breaks in the variance of the return process. The FIGARCH model thus offers a competing explanation of this empirical phenomenon.

The GARCH-in-mean Model. Since volatility is viewed as a measure of risk, GARCH models are used for assessing the risk of a portfolio. From this it follows that the GARCH type conditional variance could be useful as a representation of the timevarying risk premium in explaining excess returns, that is, returns compared to the return of a riskless asset. This extends the considerations to involve the conditional mean of the return process as well. An excess return would be a combination of the unforecastable difference  $\varepsilon_t$  between the *ex ante* and ex post rates of return and a function of the conditional variance of the portfolio. Thus, if  $y_t$  is the excess return at time  $t$ ,

$$y_t = \beta + g(h_t) + \varepsilon_t \tag{14}$$

where  $h_t$  is defined as a GARCH process (4) and  $g(h_t)$  is a well-defined function. Engle *et al.* [26] originally defined  $g(h_t) = \delta h_t^{1/2}, \delta > 0$ , which corresponds to the assumption that changes in the conditional variance appear less than proportionally in the mean. The alternative  $g(h_t) = \delta h_t$  has also appeared in the literature. Equations  $(4)$  and  $(14)$  form the GARCH-in-mean or GARCH-M model. It has been quite frequently applied in the applied econometrics and finance literature. It may be mentioned that Glosten *et al.* [32] developed the GJR-GARCH model in the framework of the GARCH-M model.

#### Family of Exponential GARCH Models

The standard GARCH model has some disadvantages. Parameter restrictions are required to ensure positivity of the conditional variance at every point of time. Furthermore, the model does not allow an asymmetric response to shocks. This disadvantage was overcome by the appearance of asymmetric GARCH models but this was an important reason for the introduction of the exponential GARCH (EGARCH) model by Nelson [55]. A family of EGARCH $(p, q)$ models may be defined as in equation  $(2)$  with

$$\ln h_t = \alpha_0 + \sum_{j=1}^q g_j(z_{t-j}) + \sum_{j=1}^p \beta_j \ln h_{t-j} \quad (15)$$

When  $g_i(z_{t-i}) = \alpha_i z_{t-i} + \psi_i(|z_{t-i}| - \mathsf{E}|z_{t-i}|),$  $j = 1, \ldots, q$ , model (15) becomes the EGARCH model of  $[55]$ . It is seen from equation  $(15)$  that no parameter restrictions are necessary to ensure positivity of  $h_t$ . Parameters  $\alpha_i$ ,  $j = 1, \ldots, q$ , make an asymmetric response to shocks possible.

As in the standard GARCH case, the first-order model  $(p = q = 1)$  is the most popular EGARCH model in practice. Nelson [55] derived existence conditions for moments of the general infinite-order exponential ARCH model. For the EGARCH model with  $g_i(z_{t-i})$  defined as above, these conditions imply that if the error process  $\{z_t\}$  has all moments and  $\sum_{i=1}^{p} \beta_i^2 < 1$  in equation (15), then all moments for the EGARCH process  $\{\varepsilon_t\}$  exist. For example, if  $\{z_t\}$  is a sequence of independent standard normal variables, then the restrictions on  $\beta_i$ ,  $j = 1, \ldots, p$ , are necessary and sufficient for the existence of all moments simultaneously. For GARCH models of the previous section, the moment conditions become more and more stringent for higher and higher even moments; see [40].

There is some similarity between the EGARCH model and the autoregressive stochastic volatility model (see Stochastic Volatility Models). Introducing a sequence  $\{s_t\}$  of continuous unobservable independent random variables mutually independent of  $\{z_t\}$  and substituting  $g_j(s_{t-j})$  for  $g_j(z_{t-j})$  in equation (15) leads to another class of models. Typically, in applications,  $p = q = 1$  and  $g_1(s_{t-1}) =$  $\delta s_{t-1}$  where  $\delta$  is a parameter to be estimated. This is called the *autoregressive stochastic volatility model*. Strictly speaking, it is not a model of conditional heteroskedasticity, because its information set at time  $t$ also contains  $\{s_{t-j}, j \ge 1\}.$ 

## Nonparametric and Semiparametric GARCH Models

Nonparametric GARCH models have been developed to remedy some of the disadvantages of the standard GARCH model mentioned earlier. A straightforward example is the model (2) in which  $h_t =$  $h(\varepsilon_{t-1}, \ldots, \varepsilon_{t-q})$  is a smooth positive-valued function estimated using nonparametric techniques. When  $q$  is large, however, this model suffers from the curse of dimensionality. This may be partly remedied by an additive function,  $h_t = \sum_{i=1}^{q} h_j(\varepsilon_{t-j})$ , where  $h_i(\varepsilon_{t-i}), j = 1, \ldots, q$ , are positive-valued functions that are estimated separately. Both of these models are ARCH models. Engle and Ng [27] introduced the following semiparametric GARCH model:

$$h_t = h(\varepsilon_{t-j}) + \beta h_{t-1} \tag{16}$$

where  $h(\cdot)$  is a smooth unknown function to be estimated. With  $i = 1$  this functional form is more flexible than the standard  $GARCH(1,1)$  model and allows modeling possible asymmetry in returns. For more discussion of nonparametric and semiparametric ARCH and GARCH models, see [50].

## Estimation of GARCH Models and Properties of **Estimators**

The parameters of the GARCH $(p, q)$  model (4) and its extensions may be estimated jointly by maximum likelihood. Asymptotic theory for the estimators has been developed over the years. Weiss [70] already proved consistency and asymptotic normality for maximum likelihood estimators in the  $ARCH(q)$ case under the assumption  $\mathsf{E}\varepsilon_t^4 < \infty$ , which implies  $\mathsf{E}z_t^4 < \infty$ . General results are provided by Berkes et al. [9] who showed the asymptotic normality of the quasi-maximum likelihood (QML) estimators of the parameters of the  $GARCH(p, q)$  model where only the moment restriction  $\mathsf{E} \left| z_{i}^{2} \right|^{2+\delta} < \infty, \ \delta > 0,$ is required. Francq and Zakoïan [30] proved asymptotic normality of QML estimators for yet another set of conditions, and their results included the ARMA-GARCH family of models. Straumann and Mikosch [66] derived conditions for asymptotic normality of the OML estimators for a class of GARCH models that also includes some nonlinear GARCH models. In particular, they verified these conditions for the estimators of the AGARCH model. The corresponding conditions for the GARCH-in-mean model have not been verified, although consistency of the maximum likelihood estimators has been proven; see [53].

Rather often, the parameters of GARCH models are estimated assuming a  $t$ -distribution for the errors. This choice is based on empirical observation suggesting that the residuals of the estimated GARCH models assuming normality tend to be leptokurtic. If the  $t$ -distribution is applied, its degrees-of-freedom parameter or its inverse is generally estimated as well.

The parameters of GARCH models have to be estimated numerically because the conditional variances are not observed and have to be estimated separately for each iteration, that is, conditionally on parameter estimates obtained from the previous iteration. The estimated unconditional variance is used as the starting value for  $h_0, h_{-1}, \ldots, h_{-(p-1)},$ whereas  $\widehat{\varepsilon}_0^2 = \ldots = \widehat{\varepsilon}_{-q+1}^2 = 0$ . In practice, the most popular algorithm for estimating GARCH models by maximum likelihood has been the so-called Berndt-Hall-Hall-Hausman (BHHH) algorithm. Its popularity is partly based on the fact that it does not require the second derivatives of the log-likelihood function. Those may be considered difficult to compute given their recursive structure. Nevertheless, Fiorentini et al. [29] worked out the analytical second derivatives of the log-likelihood function for the GARCH model. This makes iterative estimation of parameters by the Newton-Raphson algorithm possible.

Several econometric software packages contain a module for estimating GARCH models. Brooks *et al.* [15] studied a number of them, focusing on numerical accuracy of the estimates. Their conclusion was that the algorithms based on analytical derivatives are preferable to the other alternatives. The best performing package used both analytical first and second derivatives. The authors reported substantial differences in numerical accuracy between the packages considered.

The parameters of the EGARCH model are also estimated by maximum likelihood. Nelson [55] gives the log-likelihood function based on the assumption that the errors follow a generalized error distribution (GED) with mean zero. The normal distribution is a special case of the GED. Nelson also discusses the role of the starting values in the estimation. In his simulations, the use of other starting values rather than the unconditional mean of  $\ln h_t$  very rapidly leads to values of  $h_t$  obtained by starting from  $\mathsf{E} \ln h_t$ . As in the case of GARCH models, the precision of the estimates may be expected to depend heavily on whether or not analytical derivatives of the loglikelihood are used in iterative estimation.

Properties of the QML estimators of the EG- $ARCH(1,1)$  model have been considered by Straumann and Mikosch [66] who verified conditions for consistency of these estimators. The authors pointed out that verifying the corresponding conditions for asymptotic normality of the QML estimators is still an open question.

# **Multivariate Models of Conditional** Heteroskedasticity

#### General Multivariate GARCH Model

The univariate GARCH model has been generalized to the vector case, which makes it possible to model and forecast not only conditional variances of asset returns but covariances between returns as well. This has relevance in portfolio management. In the most general multivariate GARCH model, the socalled VEC-GARCH model of [14], every conditional variance and covariance is a linear function of all previous conditional variances and covariances. Assume a vector of returns  $\boldsymbol{\varepsilon}_t = (\varepsilon_{1t}, \dots, \varepsilon_{mt})'$  such that  $\mathsf{E}\boldsymbol{\varepsilon}_{t} = \mathbf{0}$  and  $\mathsf{E}(\boldsymbol{\varepsilon}_{t}\boldsymbol{\varepsilon}_{t}^{\prime}|\mathcal{F}_{t-1}) = \mathbf{H}_{t} = [h_{ijt}]$  where  $\mathbf{H}_{t}$  is positive definite almost surely. It follows that

$$\boldsymbol{\varepsilon}_t = \mathbf{H}_t^{1/2} \mathbf{z}_t \tag{17}$$

where  $\mathbf{z}_t \sim \text{iid}(\mathbf{0}, \mathbf{I}_m)$ . The VEC-GARCH $(p, q)$ model is defined as follows:

$$\operatorname{vech}(\mathbf{H}_{t}) = \boldsymbol{\omega} + \sum_{k=1}^{q} \mathbf{A}_{k} \operatorname{vech}(\boldsymbol{\varepsilon}_{t-k} \boldsymbol{\varepsilon}'_{t-k})$$
$$+ \sum_{k=1}^{p} \mathbf{B}_{k} \operatorname{vech}(\mathbf{H}_{t-k}) \qquad (18)$$

where  $\mathbf{A}_{k} = [\alpha_{kij}]$  and  $\mathbf{B}_{k} = [\beta_{kij}]$  are coefficient matrices with  $m(m + 1)/2$  rows and columns, and  $\omega$ is an  $(m(m + 1)/2) \times 1$  intercept vector with positive elements.

In equation  $(18)$ , the number of parameters increases rapidly with the dimension of  $\varepsilon_t$ . Besides, general conditions for positive definiteness of  $\mathbf{H}_t$  do not seem to exist. A simplified version in which the coefficient matrices  $\mathbf{A}_k$  and  $\mathbf{B}_k$  are diagonal has sometimes been applied. For this process, it is possible to work out the conditions for  $\mathbf{H}_t$  to be positive definite, at least in the first-order case. In many applications, however, this model is already too restrictive, because it excludes any interaction between the conditional variances and covariances.

Bollerslev *et al.* [14] considered estimation of the general model and concluded that under sufficient regularity conditions the maximum likelihood estimator of the parameter vector is consistent and asymptotically normal. They used the BHHH optimization algorithm for obtaining the maximum likelihood estimates. Estimation of the VEC-GARCH model is, however, computationally demanding. The number of parameters can be large. Furthermore, the matrix  $\mathbf{H}_{t}$ has to be inverted for each  $t$  in every iteration. It is likely that numerical considerations are at least as important here as they are in the univariate case. The use of analytical first- and second-order derivatives would thus be preferable if they are available.

## Constant Conditional Correlation Multivariate $GARCH$

There exist multivariate GARCH models with fewer parameters than the VEC-GARCH model. The conconditional correlation GARCH (CCCstant GARCH) model by Bollerslev [11] is built on the assumption that the conditional correlations between variables remain constant over time. This assumption is more parsimonious than the VEC-GARCH one, because the conditional covariances are determined through conditional variances and these correlations. Suppose again that  $\boldsymbol{\varepsilon}_t = (\varepsilon_{1t}, \ldots, \varepsilon_{mt})'$  such that  $\mathsf{E}\boldsymbol{\varepsilon}_{t} = \mathbf{0}$  and  $\mathsf{E}(\boldsymbol{\varepsilon}_{t}\boldsymbol{\varepsilon}_{t}^{\prime}|\mathcal{F}_{t-1}) = \mathbf{H}_{t} = [h_{ijt}]$  where  $\mathbf{H}_t$  is positive definite almost surely. The CCC-GARCH model has the following structure:

$$\mathbf{H}_t = \mathbf{D}_t \mathbf{P} \mathbf{D}_t \tag{19}$$

where  $\mathbf{D}_t = \text{diag}(h_{11t}^{1/2}, \dots, h_{mmt}^{1/2})$  and  $\mathbf{P} = [\rho_{ij}]$  is the positive definite correlation matrix, so that  $h_{ijt}$  =  $\rho_{ii}(h_{iit}h_{jit})^{1/2}$  for  $i, j = 1, \ldots, m$ . Each conditional variance is assumed to follow a standard univariate GARCH model (4). The most common choice is the first-order GARCH model:  $p = q = 1$ . In this case, a bivariate first-order CCC-GARCH model has 7 parameters compared to 21 in the corresponding VEC-GARCH model.

One of the attractions of the CCC-GARCH model is that the parameter estimation is not complicated. The (conditional) quasi log-likelihood function of any GARCH model with  $\boldsymbol{\varepsilon}_t | \mathcal{F}_{t-1} \sim \text{iid } \mathcal{N}(\mathbf{0}, \mathbf{H}_t)$  has the form

$$L(\boldsymbol{\theta}) = c - (1/2) \sum_{t=1}^{T} (\ln|\mathbf{H}_{t}| - \boldsymbol{\varepsilon}_{t}' \mathbf{H}_{t}^{-1} \boldsymbol{\varepsilon}_{t}) \qquad (20)$$

where  $\boldsymbol{\theta}$  is the parameter vector. As already mentioned, maximizing equation (20) can be computationally quite costly when the model is the VEC-GARCH model, because an  $m \times m$  matrix has to be inverted  $T$  times during a single iteration. The assumption of constant conditional correlations considerably simplifies things. Following Bollerslev [11], rewrite the conditional variances as  $h_{ijt} = k_i \sigma_{it}^2$ , where  $k_j > 0, j = 1, \ldots, m$ . Then one may partition the covariance matrix  $\mathbf{H}_t$  as follows:

$$\mathbf{H}_t = \mathbf{D}_t^* \mathbf{\Gamma} \mathbf{D}_t^* \tag{21}$$

where  $\mathbf{D}_{t}^{*} = \text{diag}(\sigma_{1t}, \ldots, \sigma_{mt})$  and  $\mathbf{\Gamma} = [\gamma_{ij}] =$  $[\rho_{ii}(k_i k_i)^{1/2}]$ . Applying equation (21) to equation (20) and keeping in mind that  $\mathbf{D}_{t}^{*}$  is a diagonal matrix yields

$$L(\boldsymbol{\theta}) = c - (T/2) \ln |\boldsymbol{\Gamma}| - \sum_{t=1}^{T} \sum_{j=1}^{m} \ln \sigma_{jt}$$
$$- (1/2) \sum_{t=1}^{T} \overline{\boldsymbol{\varepsilon}}_{t}^{\prime} \boldsymbol{\Gamma}^{-1} \overline{\boldsymbol{\varepsilon}}_{t} \qquad (22)$$

where  $\overline{\boldsymbol{\varepsilon}}_t = \mathbf{D}_t^{*-1} \boldsymbol{\varepsilon}_t$ . In the maximization of equation (22), only a single matrix inversion is needed for each iteration. Even here, the BHHH optimization algorithm has been recommended for maximizing the log-likelihood. The calculations can be made even simpler by concentrating the log-likelihood, but the derivatives of the original log-likelihood (22) are required for obtaining an estimate of the asymptotic covariance matrix of the estimators of the parameters. The correlations are recovered from the relationship  $\rho_{ii} = \gamma_{ii} (k_i k_i)^{-1/2}.$ 

Results on statistical properties of the OML estimators of a stationary CCC-GARCH model are available. Under appropriate regularity conditions, Jeantheau [41] proved consistency of these estimators and Ling and McAleer [49] verified conditions for their asymptotic normality.

### The Dynamic Conditional Correlation GARCH Model

The assumption of constant correlations, however, does not always hold in practice. Tse and Tsui [68] and Engle [23] have extended the CCC-GARCH model by introducing time variation in the correlation matrix, and the two models are quite similar. The dynamic conditional correlation (DCC-) GARCH model of [23] has the following  $GARCH(1,1)$  form:

$$q_{ijt} = \rho_{ij}(z) + \alpha^*(z_{i,t-1}z_{j,t-1} - \rho_{ij}(z))$$
  
+  $\beta^*(q_{ij,t-1} - \rho_{ij}(z))$   
=  $(1 - \alpha^* - \beta^*)\rho_{ij}(z) + \alpha^* z_{i,t-1}z_{j,t-1}$   
+  $\beta^* q_{ij,t-1}, \quad i \neq j$  (23)

where  $\rho_{ij}(z)$  is the unconditional correlation between  $z_{it}$  and  $z_{jt}$ , and  $\alpha^* + \beta^* < 1$ . If  $\mathsf{E}q_{ijt} < \infty$ , it follows that  $\mathsf{E}q_{iit} = \rho_{ii}(z)$ . The intercept is defined by variance targeting. The two "GARCH parameters"  $\alpha^*$  and  $\beta^*$  are the same for all correlations. This makes it possible to model a large number of assets at the same time. The estimated conditional correlations are obtained  $ex$  post by making use of the relationship

$$\rho_{ijt} = \frac{q_{ijt}}{\sqrt{q_{iit}q_{jjt}}} \tag{24}$$

When  $\alpha^* + \beta^* = 1$  in (23),  $\rho_{ijt}$  is determined by exponential smoothing.

Estimation of parameters of the DCC-GARCH model can be carried out as follows. The parameters of the individual GARCH equations contained in  $\mathbf{D}_t$  (see equation (19)) can be estimated equation by equation assuming that  $\mathbf{P} = \mathbf{I}_m$ . Conditionally upon the results, one can then estimate the correlation parameters using the estimated standardized residuals  $z_{it}$  in equation (23). For example, assuming the parameters in  $\mathbf{D}_t$  are known, the remaining parameters can be estimated by direct maximization of

$$L_T(\boldsymbol{\theta}_{\text{corr}}) = c - (1/2) \sum_{t=1}^T \ln |\mathbf{P}_t|$$
$$- (1/2) \sum_{t=1}^T \mathbf{z}_t' \mathbf{P}_t^{-1} \mathbf{z}_t \qquad (25)$$

where the elements of  $\mathbf{P}_t$  are defined as in equation  $(23)$ . Under regularity conditions, the estimators based on this two-step method are consistent but inefficient. Engle [23] also discusses simplified ways of obtaining estimates for the correlation parameters.

The CCC-GARCH model has other extensions that are not considered here. A few of them are based on the idea that the time-varying correlation matrix is a time-varying convex combination of two or more positive definite correlation matrices; see [7, 58] and [62, 63] for details.

#### The BEKK-GARCH Model

The BEKK-GARCH model (BEKK stands for Baba, Engle, Kraft and Kroner) is discussed in detail in [25]. It is another parsimonious GARCH model and has the property that the conditions of positive definiteness of the conditional covariance matrix are known. The

model is defined by completing equation  $(17)$  with

$$\mathbf{H}_{t} = (\mathbf{C}_{0}^{*})' \mathbf{C}_{0}^{*} + \sum_{k=1}^{K} \sum_{j=1}^{q} (\mathbf{A}_{jk}^{*})' \boldsymbol{\varepsilon}_{t-j} \boldsymbol{\varepsilon}_{t-j}^{'} \mathbf{A}_{jk}^{*}$$
$$+ \sum_{k=1}^{K} \sum_{j=1}^{p} (\mathbf{B}_{jk}^{*})' \mathbf{H}_{t-j} \mathbf{B}_{jk}^{*} \tag{26}$$

where  $\mathbf{C}_0^* = (\mathbf{c}_{01}', \dots, \mathbf{c}_{0m}')'$  is an  $m \times m$  triangular matrix, and  $\mathbf{A}_{ik}^* = [\alpha_{ik,il}^*]$  and  $\mathbf{B}_{ik}^* = [\beta_{ik,il}^*]$  are  $m \times m$  coefficient matrices. When  $\mathbf{C}_0^*$  is of full rank so that  $(\mathbf{C}_0^*)'\mathbf{C}_0^*$  is positive definite, it follows that  $\mathbf{H}_t$  is positive almost surely if the starting values  $\mathbf{H}_0, \mathbf{H}_{-1}, \ldots, \mathbf{H}_{-p+1}$  are positive semidefinite matrices, and  $\varepsilon_0, \varepsilon_{-1}, \ldots, \varepsilon_{-q+1} = \mathbf{0}$ . This is the main attraction of the BEKK-GARCH model. In applications, it is typically assumed that  $K = p = q = 1$ .

The log-likelihood function of the BEKK model is equation (20), and its partial derivatives are defined through equation (26). Engle and Kroner [25] remark that in the GARCH case (as opposed to ARCH) calculating analytical derivatives is complicated because it requires recursive computation of certain derivatives. They therefore recommend numerical derivatives and the BHHH algorithm. Nevertheless, Lucchetti [51] has worked out the analytical score for the first-order BEKK-GARCH model when  $K = 1$ . Given the results reported in  $[15]$  in the univariate case, it appears that making use of the analytical score in the estimation of the parameters of this model would be very useful. Conditions for the asymptotic normality of the QML estimators of the parameters of the BEKK-GARCH model can be found in [17].

#### Factor GARCH Models

Observable Factor GARCH Models. The BEKK-GARCH model may be used as a starting point in a search for even more parsimonious models. Assume that, for each k, the matrices  $\mathbf{A}_{ik}^*$  and  $\mathbf{B}_{ik}^*$  in equation (26) have rank one and the same  $m \times 1$  eigenvectors,  $\mathbf{g}_k$  for  $\mathbf{A}_{ik}^*$  and  $\mathbf{f}_k$  for  $\mathbf{B}_{ik}^*$ , respectively, with  $\mathbf{g}'_k \mathbf{f}_i = 0$ ,  $i \neq k$ , and  $\mathbf{g}'_k \mathbf{f}_k = 1$ . Then equation (26) collapses into

$$\mathbf{H}_{t} = \mathbf{\Omega} + \sum_{k=1}^{K} \mathbf{g}_{k} \mathbf{g}_{k}^{\prime} \left\{ \sum_{j=1}^{q} \alpha_{kj}^{2} \gamma_{k,t-j}^{2} + \sum_{j=1}^{p} \beta_{kj}^{2} h_{k,t-i}^{(f)} \right\}$$
(27)

where  $\mathbf{\Omega} = (\mathbf{C}_0^*)' \mathbf{C}_0^*$ ,  $\gamma_{kt} = \mathbf{f}_k' \boldsymbol{\varepsilon}_t$  and  $h_{kt}^{(f)} = \mathbf{f}_k' \mathbf{H}_t \mathbf{f}_k$ . This is the  $K$ -factor GARCH model of [28]. Each factor  $\gamma_{kt}$  has a univariate GARCH $(p, q)$  structure:  $\gamma_{kt}|\mathcal{F}_{t-1} \sim \mathcal{D}(0, h_{kt}^{(f)})$  where  $\mathcal{D}$  denotes a distribution, such that the conditional variance

$$h_{kt}^{(f)} = c_k + \sum_{j=1}^{q} \alpha_{kj}^2 \gamma_{k,t-j}^2 + \sum_{j=1}^{p} \beta_{kj}^2 h_{k,t-j}^{(f)} \qquad (28)$$

where  $c_k = \mathbf{f}'_k \mathbf{\Omega} \mathbf{f}_k$ . Writing  $\gamma_{kt} = z_{kt} (\mathbf{f}'_k \mathbf{H}_t \mathbf{f}_k)^{1/2}, k =$  $1, \ldots, K$ , where  $\{z_{kt}\} \sim \text{iid}(0, 1)$  such that  $\mathsf{E}z_{kt}z_{it} =$  $\omega_{kj}$ , it follows that  $\gamma_{kt}$  and  $\gamma_{jt}$  have a constant conditional correlation  $\omega_{ki}$ . The model consisting of equations (17) and (27) and characterizing  $\epsilon_t$ is just a linear combination of the  $K$  conditional variances of the univariate common factors  $\gamma_{kt}$ . It is important to note that the factors  $\gamma_{kt}$ ,  $k = 1, \ldots, K$ , are observable and not latent variables because  $\mathbf{f}_k$ ,  $k = 1, \ldots, K$ , are assumed known.

This model has an economic interpretation. Theories of asset pricing suggest that the risk premium of an asset depends on its covariance with other assets as well as its own variance. The factor GARCH model represents those covariances in a parsimonious way and makes it possible to simultaneously consider a larger number of asset returns than many other vector GARCH models would allow in practice. The  $K$ factors define as many portfolios of these assets. It is then reasonable to assume that the elements of  $\mathbf{f}_k$  are nonnegative and sum up to one.

The predetermined factors in this model can be correlated. There are also factor models with uncorrelated factors. The factors are obtained through a one-to-one transformation of  $\boldsymbol{\varepsilon}_t$ :

$$\boldsymbol{\varepsilon}_t = \mathbf{W} \mathbf{f}_t \tag{29}$$

where **W** is a nonsingular  $m \times m$  matrix. Each  $f_{it}$  in  $\mathbf{f}_t = (f_{1t}, \ldots, f_{mt})'$  is thus a function of the elements of  $\boldsymbol{\varepsilon}_t$  and is typically assumed to follow a GARCH process. The specification of  $W$  varies from one model to the next. Examples include [1, 69] and [45].

The parameters of the factor GARCH model (17) and (27) can be estimated by QML with restrictions  $\mathbf{g}'_k \mathbf{f}_i = 0, i \neq k$ , and  $\mathbf{g}'_k \mathbf{f}_k = 1$ , but this can be numerically difficult. The fact that the common conditional variances can be viewed as generated by univariate GARCH processes suggests two-step estimation of parameters. First,  $c_k$ ,  $\alpha_{kj}^2$  and  $\beta_{kj}^2$  and the common conditional variances  $h_{kt}^{(\widetilde{f})}$  are estimated from the K

univariate GARCH equations (28). Equation (27) is then rewritten as

$$\mathbf{H}_{t} = \left[h_{ijt}\right] = \left\{\boldsymbol{\Omega} - \sum_{k=1}^{K} c_{k} \mathbf{g}_{k} \mathbf{g}_{k}^{\prime}\right\} + \sum_{k=1}^{K} \mathbf{g}_{k} \mathbf{g}_{k}^{\prime} h_{kt}^{(f)}$$
(30)

At the second stage, the remaining parameters are estimated making use of equation  $(30)$  and the estimates of  $c_k$  and  $h_{kt}^{(f)}$ . Lin [48] considers the estimation of factor GARCH models, including these two methods, the QML and the two-step one. More details and references can be found in that paper.

Unobserved Factor Models. In the factor model  $(27)$ , the factors at time t, as can be seen from equation (30), are functions of observed variables  $\varepsilon_{t-j}, j \geq 1$ . Another strand of factor GARCH models has drawn inspiration from the factor analysis and builds on genuinely unobserved factors. In a general form, one may write

$$\boldsymbol{\varepsilon}_t = \mathbf{C}\mathbf{f}_t + \boldsymbol{\eta}_t \tag{31}$$

where  $\mathbf{f}_t$  is now a  $k \times 1$  vector of unknown factors such that  $\mathsf{E}\mathbf{f}_t = 0$  and  $\text{cov}(\mathbf{f}_t | \mathfrak{F}_{t-1}) = \mathbf{\Lambda}_t$  where  $\mathbf{\Lambda}_t$ is a time-varying covariance matrix, often assumed diagonal, and C is an  $m \times k$  matrix of factor loadings with rank  $k \leq m$ . Furthermore, for the disturbance vector,  $\mathsf{E}\boldsymbol{\eta}_t = 0$  and  $\text{cov}(\boldsymbol{\eta}_t | \mathfrak{F}_{t-1}) = \boldsymbol{\Sigma}_{\eta}$ , and  $\mathsf{E}\{\mathbf{f}_t\boldsymbol{\eta}'_t|\mathfrak{F}_{t-1}\}=\mathbf{0}.$  The information set  $\mathfrak{F}_{t-1}$  contains the unobservable variables  $\mathbf{f}_{t-j}, j \geq 1$ , unlike the econometrician's information set  $\mathcal{F}_{t-1}$  that only contains the observable variables  $\epsilon_{t-i}, j \ge 1$ . In [60], it is shown that there always exists a model of type  $(31)$  such that the observable factor model  $(27)$  is observationally equivalent to it.

Diebold and Nerlove [20] introduced a model of form (31), in which  $k = 1$  and  $\mathbf{f}_t$  has an ARCH structure. They use it to model the volatility of a set of weekly spot exchange rates. In their model,

$$\boldsymbol{\varepsilon}_{t} = \boldsymbol{\gamma} f_{t} + \boldsymbol{\eta}_{t}$$
$$\mathsf{E}(f_{t}|\mathfrak{F}_{t-1}) = h_{t}^{(f)} = \alpha_{0} + \sum_{j=1}^{q} \alpha_{j} f_{t-j}^{2} \qquad (32)$$

From equation  $(32)$  it follows that

$$\mathbf{H}_{t} = \mathsf{E}(\boldsymbol{\varepsilon}_{t}\boldsymbol{\varepsilon}_{t}^{\prime}|\mathfrak{F}_{t-1}) = h_{t}^{(f)}\boldsymbol{\gamma}\boldsymbol{\gamma}^{\prime} + \boldsymbol{\Sigma}_{\eta} \qquad (33)$$

The conditional variances and covariances are thus determined by a single factor. Diebold and Nerlove [20] estimated the parameters of  $(32)$  using the Kalman filter.

## **Final Remarks**

The literature on GARCH models is quite voluminous. Modern econometrics texts contain accounts of conditional heteroskedasticity. A number of surveys of GARCH models exist as well. Bollerslev et al. [13], Diebold and Lopez [19], Palm [57], and Guégan [36] survey developments till the early 1990s; see [31] for a very recent survey. Shephard [61] considers both univariate GARCH and stochastic volatility models. Gouriéroux [34] concentrates on ARCH models, both univariate and multivariate. The survey by Bollerslev *et al.* [12] also reviews applications to financial series. The focus in [65] is on estimation in models of conditional heteroskedasticity. Theoretical results on time series models with conditional heteroskedasticity are also reviewed in [47]. Engle [22] provides a selection of the most important articles on ARCH and GARCH models up until 1993. Recent surveys of multivariate GARCH models include [6] and [64]. Several articles in [4] provide detailed descriptions of various aspects of GARCH models and their use in applications.

### Acknowledgments

This work has been supported by the Danish National Research Foundation.

## References

- [1] Alexander, C. & Chibumba, A. (1996). Multivariate orthogonal factor GARCH, Discussion Papers in Mathematics, University of Sussex.
- [2] Andersen, T.G. (2009). Realized volatility, in *Handbook* of Financial Time Series, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, New York, pp. 555-575.
- [3] Andersen, T.G. & Bollerslev, T. (1998). Answering the skeptics: yes, standard volatility models provide accurate forecasts, International Economic Review 39, 885-905.
- Andersen, T.G., Davis, R.A., Kreiss, J.-P. & Mikosch, T. [4] (eds) (2009). Handbook of Financial Time Series, Springer, New York.

- [5] Baillie, R.T., Bollerslev, T. & Mikkelsen, H.O. (1996). Fractionally integrated generalized autoregressive conditional heteroskedasticity, *Journal of Econometrics* **74**, 3–30.
- [6] Bauwens, L., Laurent, S. & Rombouts, J.V.K. (2006). Multivariate GARCH models: a survey, *Journal of Applied Econometrics* **21**, 79–109.
- [7] Berben, R.-P. & Jansen, W.J. (2005). Comovement in international equity markets: a sectoral view, *Journal of International Money and Finance* **24**, 832–857.
- [8] Berkes, I., Gombay, E., Horvath, L. & Kokoszka, P. ´ (2004). Sequential change-point detection in GARCH (p,q) models, *Econometric Theory* **20**, 1140–1167.
- [9] Berkes, I., Horvath, L. & Kokoszka, P. (2003). GARCH ´ processes: structure and estimation, *Bernoulli* **9**, 201–227.
- [10] Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity, *Journal of Econometrics* **31**, 307–327.
- [11] Bollerslev, T. (1990). Modelling the coherence in shortrun nominal exchange rates: a multivariate generalized ARCH model, *Review of Economics and Statistics* **72**, 498–505.
- [12] Bollerslev, T., Chou, R.Y. & Kroner, K.F. (1992). ARCH modeling in finance. A review of the theory and empirical evidence, *Journal of Econometrics* **52**, 5–59.
- [13] Bollerslev, T., Engle, R.F. & Nelson, D.B. (1994). ARCH models, in *Handbook of Econometrics*, R.F. Engle & D.L. McFadden, eds, North-Holland, Amsterdam, Vol. 4, pp. 2959–3038.
- [14] Bollerslev, T., Engle, R.F. & Wooldridge, J. (1988). A capital asset-pricing model with time-varying covariances, *Journal of Political Economy* **96**, 116–131.
- [15] Brooks, C., Burke, S.P. & Persand, G. (2001). Benchmarks and the accuracy of GARCH model estimation, *International Journal of Forecasting* **17**, 45–56.
- [16] Cai, J. (1994). A Markov model of switching-regime ARCH, *Journal of Business and Economic Statistics* **12**, 309–316.
- [17] Comte, F. & Lieberman, O. (2003). Asymptotic theory for multivariate GARCH processes, *Journal of Multivariate Analysis* **84**, 61–84.
- [18] Diebold, F.X. (1986). Modeling the persistence of conditional variances: a comment, *Econometric Reviews* **5**, 51–56.
- [19] Diebold, F.X. & Lopez, J.A. (1995). Modeling volatility dynamics, in *Macroeconometrics: Developments, Tensions, and Prospects*, K.D. Hoover, ed, Kluwer Academic Publishers, Boston, pp. 427–472.
- [20] Diebold, F.X. & Nerlove, M. (1989). The dynamics of exchange rate volatility: a multivariate latent factor ARCH model, *Journal of Applied Econometrics* **4**, 1–21.
- [21] Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation, *Econometrica* **50**, 987–1007.
- [22] Engle, R.F. (ed) (1995). *ARCH Selected Readings*, Oxford University Press, Oxford.

- [23] Engle, R.F. (2002). Dynamic conditional correlation: a simple class of multivariate generalized autoregressive conditional heteroscedasticity models, *Journal of Business and Economic Statistics* **20**, 339–350.
- [24] Engle, R.F. & Bollerslev, T. (1986). Modeling the persistence of conditional variances, *Econometric Reviews* **5**, 1–50.
- [25] Engle, R.F. & Kroner, K.F. (1995). Multivariate simultaneous generalized ARCH, *Econometric Theory* **11**, 122–150.
- [26] Engle, R.F., Lilien, D.M. & Robins, R.P. (1987). Estimating time-varying risk premia in the term structure: the ARCH-M model, *Econometrica* **55**, 391–407.
- [27] Engle, R.F. & Ng, V.K. (1993). Measuring and testing the impact of news on volatility, *Journal of Finance* **48**, 1749–1777.
- [28] Engle, R.F., Ng, V.K. & Rotschild, M. (1990). FACTOR-ARCH covariance structure: empirical estimates for treasury bills, *Journal of Econometrics* **45**, 213–237.
- [29] Fiorentini, G., Calzolari, G. & Panattoni, L. (1996). Analytic derivatives and the computation of GARCH estimates, *Journal of Applied Econometrics* **11**, 399–417.
- [30] Francq, C. & Zako¨ıan, J.-M. (2004). Maximum likelihood estimation of pure GARCH and ARMA-GARCH processes, *Bernoulli* **10**, 605–637.
- [31] Giraitis, L., Leipus, R. & Surgailis, D. (2006). Recent advances in ARCH modelling, in *Long Memory in Economics*, A. Kirman & G. Teyssiere, eds, Springer, Berlin, pp. 3–38.
- [32] Glosten, L., Jagannathan, R. & Runkle, D. (1993). On the relation between expected value and the volatility of the nominal excess return on stocks, *Journal of Finance* **48**, 1779–1801.
- [33] Gonzalez-Rivera, G. (1998). Smooth transition GARCH models, *Studies in Nonlinear Dynamics and Econometrics* **3**, 161–178.
- [34] Gourieroux, C. (1997). ´ *ARCH Models and Financial Applications*, Springer, Berlin.
- [35] Gray, S.F. (1996). Modeling the conditional distribution of interest rates as a regime-switching process, *Journal of Financial Economics* **42**, 27–62.
- [36] Guegan, D. (1994). ´ *S´eries chronologiques nonlin´eaires `a temps discret*, Economica, Paris.
- [37] Haas, M., Mittnik, S. & Paolella, M.S. (2004). A new approach to Markov-switching GARCH models, *Journal of Financial Econometrics* **4**, 493–530.
- [38] Hagerud, G. (1997). *A New Non-Linear GARCH Model*, EFI Economic Research Institute, Stockholm.
- [39] Hamilton, J.D. & Susmel, R. (1994). Autoregressive conditional heteroskedasticity and changes in regime, *Journal of Econometrics* **64**, 307–333.
- [40] He, C. & Terasvirta, T. (1999). Properties of moments of ¨ a family of GARCH processes, *Journal of Econometrics* **92**, 173–192.
- [41] Jeantheau, T. (1998). Strong consistency of estimators for multivariate ARCH models, *Econometric Theory* **14**, 70–86.

- [42] Klaassen, F. (2002). Improving GARCH volatility forecasts with regime-switching GARCH model, *Empirical Economics* **27**, 363–394.
- [43] Kokoszka, P. & Leipus, R. (1999). Testing for parameter changes in ARCH models, *Lithuanian Mathematical Journal* **39**, 182–195.
- [44] Lamoureux, C.G. & Lastrapes, W.G. (1990). Persistence in variance, structural change and the GARCH model, *Journal of Business and Economic Statistics* **8**, 225–234.
- [45] Lanne, M. & Saikkonen, P. (2007). A multivariate generalized orthogonal factor GARCH model, *Journal of Business and Economic Statistics* **25**, 61–75.
- [46] Li, C.W. & Li, W.K. (1996). On a double threshold autoregressive heteroskedasticity time series model, *Journal of Applied Econometrics* **11**, 253–274.
- [47] Li, W.K., Ling, S. & McAleer, M. (2002). Recent theoretical results for time series models with GARCH errors, *Journal of Economic Surveys* **16**, 245–269.
- [48] Lin, W.-L. (1992). Alternative estimators for factor GARCH models—a Monte Carlo comparison, *Journal of Applied Econometrics* **7**, 259–279.
- [49] Ling, S. & McAleer, M. (2003). Asymptotic theory for a vector ARMA-GARCH model, *Econometric Theory* **19**, 280–310.
- [50] Linton, O.B. (2009). Semiparametric and nonparametric ARCH modelling, in *Handbook of Financial Econometrics*, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, New York, pp. 157–167.
- [51] Lucchetti, R. (2002). Analytical scores for multivariate GARCH models, *Computational Economics* **19**, 133–143.
- [52] Lundbergh, S. & Terasvirta, T. (2002). Evaluating ¨ GARCH models, *Journal of Econometrics* **110**, 417–435.
- [53] Meitz, M. & Saikkonen, P. (2008). Ergodicity, mixing, and existence of moments of a class of Markov models with applications to GARCH and ACD models, *Econometric Theory* **24**, 1291–1320.
- [54] Mikosch, T. & Starica, C. (2004). Nonstationarities in financial time series, the long-range dependence, and the IGARCH effects, *Review of Economics and Statistics* **86**, 378–390.
- [55] Nelson, D.B. (1991). Conditional heteroskedasticity in asset returns: a new approach, *Econometrica* **59**, 347–370.
- [56] Nelson, D.B. & Cao, C.Q. (1992). Inequality constraints in the univariate GARCH model, *Journal of Business and Economic Statistics* **10**, 229–235.
- [57] Palm, F.C. (1996). GARCH models of volatility, in *Handbook of Statistics 14: Statistical Methods in Finance*, G. Maddala & C. Rao, eds, Elsevier, Amsterdam, pp. 209–240.
- [58] Pelletier, D. (2006). Regime switching for dynamic correlations, *Journal of Econometrics* **131**, 445–473.
- [59] Sentana, E. (1995). Quadratic ARCH models, *Review of Economic Studies* **62**, 639–661.

- [60] Sentana, E. (1998). The relation between conditionally heteroskedastic factor models and factor GARCH models, *Econometrics Journal* **1**, 1–9.
- [61] Shephard, N.G. (1996). Statistical aspects of ARCH and stochastic volatility, in *Time Series Models. In Econometrics, Finance and Other Fields*, D.R. Cox, D.V. Hinkley & O.E. Barndorff-Nielsen, eds, Chapman & Hall, London, pp. 1–67.
- [62] Silvennoinen, A. & Terasvirta, T. (2005). Multivari- ¨ ate autoregressive conditional heteroskedasticity with smooth transitions in conditional correlations, *SSE/EFI Working Papers in Economics and Finance 577*, Stockholm School of Economics.
- [63] Silvennoinen, A. & Terasvirta, T. (2007). Modelling ¨ multivariate autoregressive conditional heteroskedasticity with the double smooth transition conditional correlation GARCH model, *SSE/EFI Working Paper Series in Economics and Finance 652*, Stockholm School of Economics.
- [64] Silvennoinen, A. & Terasvirta, T. (2009). Multivariate ¨ GARCH models, in *Handbook of Financial Time Series*, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, New York, pp. 201–229.
- [65] Straumann, D. (2004). *Estimation in Conditionally Heteroscedastic Time Series Models*, Springer, New York.
- [66] Straumann, D. & Mikosch, T. (2006). Quasi-maximumlikelihood estimation in conditionally heteroscedastic time series: a stochastic recurrence equations approach, *Annals of Statistics* **34**, 2449–2495.
- [67] Taylor, S.J. (1986). *Modelling Financial Time Series*, Wiley, Chichester.
- [68] Tse, Y.K. & Tsui, K.C. (2002). A multivariate generalized autoregressive conditional heteroscedasticity model with time-varying correlations, *Journal of Business and Economic Statistics* **20**, 351–362.
- [69] van der Weide, R. (2002). GO-GARCH: a multivariate generalized orthogonal GARCH model, *Journal of Applied Econometrics* **17**, 549–564.
- [70] Weiss, A.A. (1986). Asymptotic theory for ARCH models: estimation and testing, *Econometric Theory* **2**, 107–131.
- [71] Zako¨ıan, J.-M. (1994). Threshold heteroskedastic models, *Journal of Economic Dynamics and Control* **18**, 931–955.

# **Related Articles**

**Long Range Dependence**; **Realized Volatility and Multipower Variation**; **Volatility**.

TIMO TERASVIRTA ¨
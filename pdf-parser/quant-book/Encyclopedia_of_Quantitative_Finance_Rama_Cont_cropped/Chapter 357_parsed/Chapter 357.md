# **Risk Measures: Statistical Estimation**

The recent interest in the estimation of risk measures is explained by changes in regulations in finance and insurance industries [4]. Ten years ago, the regulation was applied to a rather limited scope of assets and firms and only consisted in fixing minimal reserve level to hedge risky investments. However, these levels were computed without clear reference to the underlying risk. The new regulations, known as *Basel 2* for the finance industry and *Solvency 2* for the insurance industry, have proposed to account for risk in computing the reserves (Pillar 1). They also insist on the need for introduction of internal models by banks or insurance companies to follow their risk (Pillar 2) and on transparency (Pillar 3). This is a coherent program, which concerns risk modeling as well as the creation or the improvement of databases, and has to account for the heterogeneous technological level in these industries. In this article, we focus on risk measures, their computation, and updating.

In the current implementation of Basel 2 and Solvency 2, the risk measure suggested by regulators and generally retained by firms is the Value-at-Risk (VaR). This measure has several drawbacks, but has the advantage of being easily understood by practitioners. It can be presented as follows. Let us consider a given portfolio of assets. This portfolio can concern stocks, corporate bonds, consumer loans, or life insurance contracts. In practice, it corresponds to a business line of a bank, a credit institution, or an insurance company. The value of this portfolio at date *t* is denoted by *Wt* , but at this date its future values *Wt*<sup>+</sup>*<sup>h</sup>* are unknown.a To hedge this uncertainty, some reserves *R* are introduced. With these reserves, the future portfolio value increases to *Wt*<sup>+</sup>*<sup>h</sup>* + *R*, which diminishes the potential loss. Let us fix a probability of loss *α* = 1*,* 5, or 10%, say; then, the reserve level can be chosen such that

$$P_t[W_{t+h} + R < 0] = \alpha \tag{1}$$

where *Pt* denotes the probability given the information available at time *t*. By solving equation (1), we see that the reserve level is the opposite of the *α*- quantile of the distribution of the future portfolio value. It depends on the selected loss probability *α*, investment horizon *h*, date *t*, information available at this date, and the set of selected assets. It can be denoted by *R(t, h*; *α)* and is written in a monetary unit as the dollar or the euro. For the determination of reserves, the admissible sets of assets, the level *α*, the horizon *h*, and the date of computations are imposed by the regulators. Other values can be selected by firms for internal use, especially for fixing and reallocating the so-called economic capital.

However, the portfolio value *(Wt)* generally features a nonstationary evolution, which can render difficulty in the determination of *R*. To circumvent this difficulty, it has been proposed to introduce the notion of VaR defined as

$$VaR(t, h; \alpha) = R(t, h; \alpha) + W_t \tag{2}$$

Thus, the VaR defined as

$$P_t[W_{t+h} - W_t < -VaR(t, h; \alpha)] = \alpha \qquad (3)$$

is the opposite of the conditional *α*-quantile of the change in portfolio value *(Wt*<sup>+</sup>*<sup>h</sup>* − *Wt)*, which is a much more stationary process.b This definition highlights the importance of the (conditional) quantile function for building risk measures.

In the following section, we discuss properties that are suitable for risk measures. This allows to define a large class of risk measures, called *distortion risk measure*s (*DRM*s), which is flexible and includes the VaR as a special case. In the section Nonparametric Estimation in the IID Framework, we consider the estimation of DRMs, when the portfolio returns are independent of the past and identically distributed (IID). Under the IID assumption, the estimated risk measures have simple expressions in terms of returns, and it is easy to estimate their accuracy. These simple computations, which involve only a ranking of returns plus some averaging, explains the success of this practice, called *historical simulation*.

Nevertheless, the IID assumption is not realistic (*see* **Stylized Properties of Asset Returns**). For instance, it would be preferable to account for volatility persistence, for cycle effects, and so on. The introduction of serial dependences when computing and analyzing conditional risk measures is not an easy task and is only in its infancy for regulation purposes. Finally, we discuss the validation of the approaches used to compute the reserves and the coherent definitions of reserves for several business lines.

# **Risk Measures**

First, we discuss the construction and the comparison of risk measures for a given date and a given horizon. For this reason, we do not indicate indexes *t* and *h*. Two axiomatic theories have been introduced in the literature to construct risk measures.

#### 1. **Coherent risk measures**

The first constructive approach to evaluate the capital requirement was proposed by Artzner *et al.* [2]. *R(W )* denotes the required reserve amount for a portfolio *W*, that is, for the future portfolio value *Wt*+*h.*

The axioms are as follows:

Distribution dependence: *R(W )* depends only on the distribution of *W*.

Monotonicity: If *W* is more risky than *W*<sup>∗</sup> by the stochastic dominance<sup>c</sup> of order 1, then *R(W )* ≥ *R(W*<sup>∗</sup>*)*.

Drift invariance: *R(W* + *c)* = *R(W )* − *c*, for any *W* and any deterministic *c*.

Positive homogeneity: *R(λW )* = *λR(W )*, for any *W* and any nonnegative scalar *λ*.

Subadditivity: *R(W* + *W*<sup>∗</sup>*)* ≤ *R(W )* + *R(W*<sup>∗</sup>*)*, for any *W* and *W*<sup>∗</sup>.

Note that the homogeneity and subadditivity properties imply the convexity of the coherent risk measure (*see* **Convex Risk Measures**).

#### 2. **The Wang axioms**

The next set of axioms were introduced in a series of papers by Wang and Young [27], for the purpose of analyzing losses in insurance. Thus, we restrict ourselves to losses that are negative *W*. The axioms are as follows:

Distribution dependence: *R(W )* depends on the distribution of *W* only.

Positivity: *R(W )* ≥ 0*.*

Deterministic loss: *R(c)* = −*c*, for any deterministic loss *c <* 0*.*

Positive homogeneity: *R(λW )* = *λR(W )* for any loss *W <* 0, and any nonnegative scalar *λ*.

Additivity for comonotonic risk: *R(W* + *W*<sup>∗</sup>*)* = *R(W )* + *R(W*<sup>∗</sup>*)* for any losses *W* and *W*<sup>∗</sup>, which are increasing deterministic transformations of the same underlying risk *Z*.

Some of the above-mentioned conditions are easily written in terms of quantile functions, by noting that

- the quantile function of *λW* is *λ* times the quantile function of *W* and
- the quantile function of the sum *W* + *W*<sup>∗</sup> of comonotonic risks is the sum of the quantile functions of *W* and *W*<sup>∗</sup>.

#### 3. **Distortion risk measures**

A reserve level can be considered as a measure of risk. The interpretation in terms of quantile functions of the homogeneity and additivity for comonotonic risk assumptions implies that a risk measure satisfying Wang's set of axioms can be written as a linear functional of the quantile function. By applying the Riesz theorem, this leads to the introduction of the so-called distortion risk measures (DRM) defined by Wang [25, 26]:

$$\Pi(Q, H) = -\int_0^1 Q(u) \, \mathrm{d}H(u) \tag{4}$$

where *Q* denotes the quantile function of the uncertain loss and *H* is a measure, called the *distortion measure*. The positivity axiom implies that *H* is a positive measure and the assumption of certain loss implies that *H* is a probability measure. Moreover, the DRM is coherent if *H* is concave. DRMs are the basis of the so-called "dual theory of choices under risk" [22, 27, 28]. Thus, a DRM is simply a weighted average of opposite quantile values. Well-known risk measures are derived by considering appropriate DRMs.

(a) VaR

When *H (u*; *α)* = 1l*(u*≥*α)*, with *α* ∈ *(*0*,* 1*),* we get

$$\Pi(Q, H(.; \alpha)) = -Q(\alpha) = VaR(\alpha) \tag{5}$$

(b) Tail-VaR

When *H (u, α)* = min*(u/α,* 1*)*, with *α* ∈ [0*,* 1], we get the equally weighted average of VaR on the interval [0*, α*]:

$$\Pi[Q, H(., \alpha)] = -\int_0^\alpha \frac{Q(u)}{\alpha} du\n$$

$$\n= -\frac{1}{\alpha} \int_0^\alpha u \, dF(u)\n$$

$$\n= E[-W|W < -VaR(\alpha)] \quad (6)$$

which is the opposite of the expected portfolio value when there is a loss; this measure is called the *Tail-VaR* at level *α*. This is a coherent risk measure since *H* is a concave function.

#### (c) Proportional hazard DRM

This risk measure is obtained for the power law transformation  $H(u; p) = u^p$ , where  $p > 0$  and has been introduced for the definition of insurance premium.

# Nonparametric Estimation in the IID Framework

In this section, we assume a sequence of IID returns concerning a given portfolio, and consider the estimation of the risk measures by their sample counterpart. Since these measures are defined from the quantile function, we first recall the asymptotic behavior of the empirical quantile. Then, we deduce the properties of estimated distortion risk measures.

#### The Empirical Quantile Function

 $y_1, \ldots, y_T$  denotes the sequence of IID returns, with a common distribution with pdf  $f$ , cdf  $F$ , and quantile function  $Q$ . The empirical cdf is defined as

$$\hat{F}_T(y) = \frac{1}{T} \sum_{t=1}^T \mathbf{1}_{y_t \le y} \tag{7}$$

whereas the empirical quantile function is

$$\hat{Q}_T(u) = \inf\{y : \hat{F}_T(y) \ge u\} \tag{8}$$

When the distribution is continuous with positive pdf, the empirical cdf and quantile functions are asymptotically related by means of the Bahadur representation [19, Section 4.3]:

$$\sqrt{T}[\hat{Q}_T(u) - Q(u)]$$
  
=  $-\frac{1}{f[Q(u)]}\sqrt{T}[\hat{F}_T[Q(u)] - u] + o_P(1)$  (9)

where  $o_P(1)$  is negligible in probability. This asymptotic equivalence allows for deriving the asymptotic behavior of the empirical quantile from the asymptotic behavior of the empirical cdf.

It is well known that the empirical cdf is strongly consistent with the true underlying cdf and converges weakly, that is, in distribution, to a Brownian bridge up to an appropriate standardization  $[23]$ :

$$\sqrt{T}[\hat{F}_T(Q(u)) - u] \Rightarrow B(u), u \in [0, 1] \qquad (10)$$

where  $\Rightarrow$  denotes weak convergence and *B* is a Brownian bridge, that is, a Gaussian process with zero mean and covariance: Cov  $[B(u_1), B(u_2)] =$  $\min(u_1, u_2) - u_1u_2$ . By applying the Bahadur representation  $(9)$ , we deduce that

$$\sqrt{T}[\hat{Q}_T(u) - Q(u)] \Rightarrow -\frac{1}{f[Q(u)]}B(u) \qquad (11)$$

## **Empirical Distortion Risk Measures**

Let us now consider a given risk measure:

$$\Pi(Q, H) - \int_0^1 Q(u) \, \mathrm{d}H(u) \tag{12}$$

where  $H$  is the distortion measure. Its empirical counterpart is given by

$$\hat{\Pi}_T(H) = \Pi(\hat{Q}_T, H) = -\int_0^1 \hat{Q}_T(u) \, \mathrm{d}H(u) \quad (13)$$

It is easily written in terms of observed returns. Let us consider the returns ranked in increasing order as  $y_1^* \le y_2^* < \cdots, < y_T^*$ , called the *order statistic*. We have

$$\hat{\Pi}_T(H) = -\sum_{t=1}^T \{y_t^*[H(t/T) - H((t-1)/T)]\}$$
(14)

This estimator is a linear combination of the order statistics  $y_1^* < \cdots < y_T^*$ , with weights depending on the sample size.<sup>d</sup>

Formula (14) is especially simple for estimating a VaR, that is, the opposite of the value of the  $\alpha$ quantile, when the sample size is well chosen. Indeed, let us assume, for instance, a risk level  $\alpha = 5\%$  and  $T = 200$ ; the estimated VaR (5%) is simply

$$\widehat{VaR}_{T}(5\%) = -y_{10}^{*} \tag{15}$$

(since  $5\% \times 200 = 10$ ).

### Asymptotic Behavior of Estimated DRM

The asymptotic behavior of the estimated DRM is directly deduced from the asymptotic behavior of the empirical quantile function. The estimator  $\hat{\Pi}_T(H)$  converges to the theoretical DRM,  $\Pi(Q; H)$ , and we have

$$\sqrt{T}[\hat{\Pi}_T(H) - \Pi(Q, H)]$$

$$\Rightarrow \int_0^1 \frac{1}{f[Q(u)]} B(u) \, \mathrm{d}H(u) \tag{16}$$

This means that the estimated DRM is asymptotically Gaussian, with zero mean and a variance given by

$$V_{\text{as}}\{\sqrt{T}(\hat{\Pi}_T(H) - \Pi(Q, H))\}$$
  
=  $\int_0^1 \int_0^1 \frac{\min(u_1, u_2) - u_1 u_2}{f[Q(u_1)] f[Q(u_2)]} \, \mathrm{d}H(u_1) \, \mathrm{d}H(u_2)$  (17)

This expression of the asymptotic variance can be difficult to use in practice, since it involves the pdf, which is rather difficult to estimate. It can **Example 1 (Sample VaR).** The VaR( $\alpha$ ) is obtained with the distortion measure equal to the point mass at  $\alpha$ . The distortion measure is not continuous and formula (19) cannot be applied. From the general result, we know that

$$\sqrt{T}[\widehat{VaR}_{T}(\alpha) - VaR(\alpha)] = -\sqrt{T}[\widehat{Q}_{T}(\alpha) - Q(\alpha)] \rightsquigarrow N\left[0, \frac{1}{f[Q(\alpha)]}\alpha(1-\alpha)\right]$$
(20)

The accuracy of this estimator depends not only on the risk level  $\alpha$  but also on the tail behavior of the distribution, since the density  $f$  (generally) tends to zero at infinity. Thus, the estimator of the VaR is not very accurate for small probability of loss  $\alpha$ , and the lack of accuracy increases with increase in magnitude of the tail.

**Example 2 (Sample Tail-VaR).** By applying formula (19), the asymptotic variance of the estimated Tail-VaR [15] is

$$V_{\text{as}}\{\sqrt{T}[T\widehat{Va}R(\alpha) - TVaR(\alpha)]\}$$
  
= 
$$\frac{V[Y|Y \leq -VaR(\alpha)] + (1-\alpha)[TVaR(\alpha) - VaR(\alpha)]^{2}}{\alpha}$$
 (21)

be simplified when the DRM is continuous with distortion density  $h$ . Indeed, we get

$$V_{\text{as}}\{\sqrt{T}[\hat{\Pi}_{T}(H) - \Pi(Q, H)]\}$$
  
=  $\int_{0}^{1} \int_{0}^{1} \frac{[\min(u_{1}, u_{2}) - u_{1}u_{2}]}{f[Q(u_{1})]f[Q(u_{2})]}$   
 $\times h(u_{1})h(u_{2}) du_{1} du_{2}$   
=  $\int_{0}^{1} \int_{0}^{1} [\min(u_{1}, u_{2}) - u_{1}u_{2}]$   
 $h(u_{1})h(u_{2}) dQ(u_{1}) dQ(u_{2})$  (18)

by noting that  $1/f[Q(u)]$  is the quantile density. Therefore, we get

$$V_{\text{as}}\{\sqrt{T}[\hat{\Pi}_{T}(H) - \Pi(Q, H)]\}$$
  
=  $\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} [\min[F(y_{1}), F(y_{2})] - F(y_{1})F(y_{2})]$   
 $\times h[F(y_{1})]h[F(y_{2})] \, \mathrm{d}y_{1} \, \mathrm{d}y_{2}.$  (19)

where TVaR denotes the Tail-VaR.

This asymptotic variance has two components. The first one measures the variability of the loss when a loss occurs, and the second one accounts for the expected loss beyond the VaR.

#### Estimated Accuracy of a Sample DRM

It is important to distinguish the case of continuous distortion measures, which exclude the VaR.

# 1. Continuous distortion measure

When  $H$  is continuous with density  $h$ , we can directly use the sample counterpart of formula (19) to derive a consistent estimator of the variance of  $\hat{\Pi}_T(H)$  [15, 18]. We get

$$\hat{V}_{\text{as}}(\sqrt{T}[\hat{\Pi}_{T}(H) - \Pi(Q; H)])$$

$$= \sum_{i=1}^{T-1} \sum_{j=1}^{T-1} \left\{ \left( \min\left(\frac{i}{T}, \frac{j}{T}\right) - \frac{i}{T} \frac{j}{T} \right) \right\}$$

$$\times h\left(\frac{i}{T}\right)h\left(\frac{j}{T}\right)\left(y_{i+1}^*-y_i^*\right)\left(y_{j+1}^*-y_j^*\right) \bigg\} \tag{22}$$

## 2. Discrete distortion measure

Formula (19) cannot be applied to the VaR. Since

$$V_{\rm as}\left(\sqrt{T}[\hat{Q}_T(\alpha) - Q(\alpha)]\right) = \frac{1}{f[Q(\alpha)]}\alpha(1-\alpha) \tag{23}$$

this variance can be estimated by

$$\hat{V}_{\text{as}}\left(\sqrt{T}[\hat{Q}_{T}(\alpha)-Q(\alpha)]\right) = \frac{1}{\hat{f}_{T}(\hat{Q}_{T}(\alpha)]}\alpha(1-\alpha) \tag{24}$$

where  $\hat{f}_T$  is, for instance, a kernel estimator of the density.

# **Dynamic Analysis**

Despite its success among practitioners, the computation and analysis of VaR and DRM in an IID framework is not realistic, and the (nonlinear) return dynamics should be taken into account. It arises in the computation of the risk measure itself, which depends on the conditional quantile function.<sup>e</sup> In this conditional framework, a nonparametric approach is difficult to follow, since the number of conditioning variables can be rather large, including current and lagged values of several asset returns, for instance. This explains why parametric or semiparametric approaches are generally considered, with the risk of using a misspecified model, that is, of introducing an additional model risk. In the first subsection, we consider a conditionally Gaussian model and derive the corresponding estimators of the DRM. The second subsection concerns the term structure of VaR. In the third subsection, we discuss dynamic models recently introduced for the purpose of computing dynamic VaR. These models are directly written in terms of conditional quantile functions.

## Parametric Dynamic Models

#### 1. Definition of the dynamic DRM

The dynamic model is generally written for the portfolio returns of interest  $y_1, \ldots, y_T$ . Let us assume that the conditional distribution of  $y_t$ , given observable variables  $z_{t-1}$ , say, is such that

$$y_t = m(z_{t-1}; \theta) + \sigma(z_{t-1}; \theta)u_t \tag{25}$$

where  $(u_t)$  are the IID standard Gaussian variables and  $\theta$  is an unknown parameter.  $m(z_{t-1}; \theta)$ (respectively,  $\sigma(z_{t-1};\theta)$ ) is the conditional drift (respectively, conditional volatility). The conditional quantile function is

$$Q_t(u) = m(z_{t-1}; \theta) + \sigma(z_{t-1}; \theta)\Phi^{-1}(u) \qquad (26)$$

where  $\Phi$  denotes the cdf of the standard normal. We deduce that a dynamic DRM can be written as

$$\Pi(Q_t, H) = -\int_0^1 Q_t(u) \, \mathrm{d}H(u) = -m(z_{t-1}; \theta) \n- \sigma(z_{t-1}; \theta) \int_0^1 \Phi^{-1}(u) \, \mathrm{d}H(u) \quad (27)$$

The DRM depends on the information by means of the conditional mean and volatility and is a linear combination of these summary statistics.

This type of analysis is usually applied with autoregressive conditionally heteroscedastic (ARCH) models or switching regime models [6], and is easily extended to error terms with no Gaussian distribution, such as the Student distribution.

For instance, such an approach is followed by J.P. Morgan with an IGARCH model defined by

$$y_t = \sigma_t u_t \tag{28}$$

where

$$\sigma_t^2 = \theta \sigma_{t-1}^2 + (1 - \theta) y_{t-1}^2 = (1 - \theta) \sum_{j=1}^{\infty} \theta^{j-1} y_{t-j}^2$$
(29)

and  $\theta = 0.95$ . Such an automatic dynamic, assumed valid for any portfolio return, is likely misspecified, and it is preferable to estimate the return dynamics separately for each portfolio.

## 2. Estimation of the dynamic DRM

The DRM is usually estimated in two steps. In the first step, the parameter  $\theta$  is estimated by (conditional) maximum likelihood (ML), that is, by maximizing

$$\hat{\theta}_T = \arg \max_{\theta} \sum_{t=1}^T \left\{ -\frac{1}{2} \log \sigma^2(z_{t-1}; \theta) - \frac{1}{2} \frac{[y_t - m(z_{t-1}; \theta)]^2}{\sigma^2(z_{t-1}; \theta)} \right\}$$
(30)

This estimator has the standard asymptotic properties of an ML estimator. Then, in the second step, the DRM is estimated as

$$\hat{\Pi}_{t,T} = -m(z_{t-1}; \hat{\theta}_T) - \sigma(z_{t-1}; \hat{\theta}_T) \int_0^1 \Phi^{-1}(u) \, \mathrm{d}H(u) \tag{31}$$

For instance, we have

$$\widehat{VaR}_{T}(t;\alpha) = -m(z_{t-1};\hat{\theta}_{T}) - \sigma(z_{t-1};\hat{\theta}_{T})\Phi^{-1}(\alpha)$$
(32)

The first step is valid for any type of DRM and can be applied to get a coherent set of estimated risk measures, such as VaR(1%), VaR(5%), VaR(10%), and TVaR(10%).

#### The Term Structure of VaR

Until now, we focused on the evolution of the dynamic risk measure, that is, on its dependence with respect to time for a fixed horizon  $h = 1$ . It is interesting to consider how the risk measure depends on the horizon h for a fixed date t. If  $y_{t+1}$  denotes the opposite change of portfolio value between  $t$  and  $t + 1$ , the opposite change of portfolio value between t and  $t + h$  is  $y_{t,h} = y_{t+1} + \cdots + y_{t+h}$ . Therefore, the conditional quantile function of interest  $Q_{t,h}$  is now associated with the conditional distribution of  $y_{t,h}$ given the information at time  $t$ .

The term structure of VaR is the mapping

$$h \to VaR(t, h; \alpha) = -Q_{t,h}(\alpha) \tag{33}$$

which can be defined for any date  $t$  and probability level  $\alpha$ .

In simple cases, the term structure of VaR is derived explicitly. For instance, let us assume a Gaussian autoregressive process of order 1 for the short-term opposite portfolio change

$$y_{t} = \mu + \varphi(y_{t-1} - \mu) + \sigma u_{t} \tag{34}$$

where  $\mu, \varphi, \sigma$  are the mean, autoregressive coefficient, and innovation variance, respectively, and  $(u_t)$ is a sequence of IID standard Gaussian variables. Thus, the conditional distribution of  $y_{t,h}$  is Gaussian, with mean

$$m(y_t, h) = \mu h + \varphi \frac{1 - \varphi^h}{1 - \varphi} (y_t - \mu) \qquad (35)$$

and variance

$$\sigma^{2}(h) = \frac{\sigma^{2}}{(1-\varphi^{2})} \left\{ h - 2\varphi(1-\varphi^{h}) + \varphi^{2} \frac{1-\varphi^{2h}}{1-\varphi^{2}} \right\}$$
(36)

We deduce the VaR at horizon  $h$  as

$$VaR(t, h; \alpha) = -m(y_t, h) - \sigma(h)\Phi^{-1}(\alpha) \tag{37}$$

The IID Gaussian framework is obtained when  $\varphi = 0$ . In this case, we have  $VaR(t, h; \alpha) = -\mu h - \mu$  $\sigma\sqrt{h}\Phi^{-1}(\alpha)$ , and the term structure involves both a linear and square-root function of the horizon  $h$ . This formula is often used by practitioners with  $\mu = 0$  to derive automatically the VaR at horizon  $h$  from the VaR at horizon 1 by  $VaR(t, h; \alpha) = \sqrt{h}VaR(t, 1; \alpha)$ . As seen earlier, this simplified formula is valid under very restrictive assumptions and has to be systematically avoided.

In fact, it is necessary to carefully compute the VaR at the different horizons case by case. In general, the term structure of  $VaR$  has no explicit expression, but can be derived by simulation, whenever the short-term quantile function  $Q_{t,1}$  has an explicit expression:  $Q_{t,1}(u) =$  $Q(u; y_{t-1})$ , say, if we assume for illustration, a Markov process. The simulation procedure is as follows:

1. Consider independent drawings  $u_{t+1}^s, \ldots, u_{t+h}^s$  in the standard uniform distribution on  $(0, 1)$ 

### 2. Apply the recursive formula

$$y_{t+1}^{s} = Q(u_{t+1}^{s}, y_{t})$$
  

$$y_{t+2}^{s} = Q(u_{t+2}^{s}, y_{t+1}^{s})$$
  

$$y_{t+h}^{s} = Q(u_{t+h}^{s}, y_{t+h-1}^{s})$$
 (38)

 $(y_{t+1}^s, \ldots, y_{t+h}^s)$  has the same conditional distribution as  $(y_{t+1}, \ldots, y_{t+h})$ .

3. Replicate  $s = 1, \ldots, S$ , and approximate  $Q_{t,h}(\alpha)$ by the empirical quantile distribution of  $y_{t h}^{s}$  =  $y_{t+1}^s + \cdots + y_{t+h}^s, s = 1, \ldots, S.$ 

### Dynamic Quantile Models

**Specification.** Since the dynamic DRM is easily written in terms of the conditional quantile function, it has been recently proposed to directly specify the dynamic model for  $(y_t)$  in terms of function  $Q_t$ , instead of using more standard (nonlinear) autoregressive specifications [11, 13]. For instance, a dynamic additive quantile (DAQ) model is

$$Q_{t}(u;\theta) = \sum_{k=1}^{K} a_{k}(\underline{y_{t-1}};\alpha_{k}) Q_{k}(u;\beta_{k}) + a_{0}(\underline{y_{t-1}};\alpha_{0})$$
(39)

where  $y_{t-1} = (y_{t-1}, y_{t-2}, \ldots), Q_k$  are path-independent baseline quantile functions with identical range  $(-\infty, +\infty)$  and  $a_k(y_{t-1}; \alpha_k), k = 1, \ldots, K$  are nonnegative functions of the past.  $\theta = (\alpha'_0, \ldots, \alpha'_K, \beta'_1, \beta'_1)$  $\ldots, \beta'_K$ ' is the vector of parameters. The positivity restrictions on functions  $a_k$  ensure that  $Q_t(:,\theta)$  is an increasing function and thus is compatible with the quantile interpretation.

The DAO model encompasses simple specifications of interest. For instance, specifications of the type

$$Q_t(u) = Q_0(u) + Q_1(u) \max(y_{t-1}, 0)$$
  
+  $Q_2(u) \max(-y_{t-1}, 0)$  (40)

or

$$Q_t(u) = \gamma_0(u) + \gamma_1(u)Q_{t-1}(u) + \gamma_2(u)|y_{t-1}|$$
  
=  $\frac{\gamma_0(u)}{1 - \gamma_1(u)} + \sum_{k=1}^{\infty} \gamma_2(u)\gamma_1(u)^h|y_{t-h}|$  (41)

are special cases of the conditional autoregressive variance at risk (CAViaR) models introduced by Engle and Manganelli [9]. A specification such as

$$Q_{t}(u) = m_{0} + m_{1}|y_{t-1} - \mu|$$
  
+  $(\sigma_{0,0} + \sigma_{0,1}|y_{t-1} - \mu|)^{1/2}\Phi^{-1}(u)$   
+  $(\sigma_{1,0} + \sigma_{1,1}|y_{t-1} - \mu|)^{1/2}tg[\pi(u - 1/2)]$   
(42)

defines a quantile mixture of a Gaussian distribution (with baseline quantile function  $\Phi^{-1}$ ) and a Cauchy distribution (with baseline quantile function  $tg[\pi(u \frac{1}{2}$ ), with ARCH effects in both scale parameters and a risk premium in the location parameter.

For a DAQ model, the dynamic DRM are immediately derived as

$$\Pi(Q_t, H) = \sum_{k=1}^{K} a_k(\underline{y_{t-1}}; \alpha_k) \int Q_k(u; \beta_k) \, \mathrm{d}H(u) \\
+ a_0(\underline{y_{t-1}}; \alpha_0) \tag{43}$$

They depend on the same set of dynamic summaries of the past  $a_k(y_{t-1};\alpha_k), k = 0, \ldots, K$ , with sensitivity coefficients equal to the baseline DRMs. These explicit expressions (see examples  $(40)$ – $(42)$ ) are appropriate for easily deriving the term structure of VaR by simulation (see the section The Term Structure of VaR).

**Estimation.** When the dynamic model is directly written in terms of a quantile function with a simple expression of  $Q_t$ , it can be numerically cumbersome to derive the conditional pdf  $f_t(y)$  =  $\left(\frac{\mathrm{d}\varrho_t}{\mathrm{d}u}[Q_t^{-1}(y)]\right)^{-1}$ , which requires the inversion of function  $Q_t$  at each observation date. As a consequence, it can be difficult to derive the maximum likelihood estimate of the parameter  $\theta$ .

Different estimation approaches have been proposed in the statistical literature.

1. When  $Q_t(u;\theta) = Q(u;\theta)$  is independent of the path, the parameter  $\theta$  can be estimated by calibrating on  $L$ -moments or trimmed  $L$ -moments [8, 17]. The theoretical  $L$ -moments or trimmed *L*-moments are of the type  $\int Q(u;\theta)P_l(u) du$ ,<br> $l = 1, \ldots, L$ , where  $P_l$  are well-chosen polynomials and their sample counterparts are  $\frac{1}{T} \sum_{i=1}^{T} y_i^* P_l(t/T), \text{ where } y_1^* < \dots < y_T^* \text{ is the}$ order statistic, that is, the observations  $y_1, \ldots, y_T$ are ranked in increasing order. This approach is easy to implement, but does not provide efficient estimators, and is difficult to extend to a dynamic framework [see the Generalized Method of L-Moments in [13, Section 4].

2. In the dynamic framework, the parameter  $\theta$  can also be consistently estimated by minimizing an objective function of the type in  $[20]$ :

$$\hat{\theta}_T = \arg\min_{\theta} \sum_{t=1}^T \{ \alpha \max[y_t - Q_t(\theta), 0]$$
  
+  $(1 - \alpha) \max[Q_t(\theta) - y_t, 0] \}$   
=  $\arg\min_{\theta} \sum_{t=1}^T \{ \alpha[y_t - Q_t(\theta)]^+$   
+  $(1 - \alpha)[y_t - Q_t(\theta)]^- \}$  (44)

where  $\alpha$  is a scalar between 0 and 1 (see the section The Control Problem for the interpretation of the objective function).

3. The estimation methods above are easy to apply, but are generally not efficient. They can be used as starting values in the optimization algorithm of the estimated inverse Kullback-Leibler information criterion (KLIC) :

$$\hat{\theta}_T = \arg \max_{\theta} \sum_{t=1}^T \left\{ \int_0^1 \log \left[ \frac{\mathrm{d}Q}{\mathrm{d}u}(u|y_{t-1};\theta) \right] + \int_0^1 \log \hat{f}_T[Q(u|y_{t-1};\theta)|y_{t-1}) \right\} \mathrm{d}u \tag{45}$$

where  $\hat{f}_T$  is a kernel estimator of the conditional pdf of  $y_t$  given  $y_{t-1}$ . The inverse KLIC estimator is asymptotically equivalent to the ML estimator and asymptotically efficient [13].

## **Control and Out-of-sample Validation**

The current regulations have at least three limitations: (i) the large use of the VaR to measure the risk and fix the required capital. This measure

accounts for the probability of loss, but not for the magnitude of the loss beyond the VaR. This drawback can be corrected by considering another DRM such as the Tail-VaR. (ii) The lack of coherency between the suggested (but often not followed) computation of the VaR as a conditional quantile, and the ex post validation of this computation by the regulator, which is generally based on a historical (that is unconditional) analysis. (iii) The computation of VaR is performed independently for each business line without taking into account the potential dependence between the risks of different lines.

The two latter limitations can be solved by considering the problem of the determination of reserves as a control problem [12, 16].

#### The Control Problem

The concept of VaR has been initially defined in a rather *ad hoc* way, but is the solution of an optimal control problem. More precisely, let us consider the objective function

$$\psi(t, z_t) = E_t[\alpha(y_{t+1} + z_t)^+ + (1 - \alpha)(y_{t+1} + z_t)^-]$$
(46)

where  $\alpha$  is the announced risk level. The decision criterion corresponds to an asymmetric loss function, which distinguishes two types of errors. When  $y +$  $z < 0$ , the reserve level is not large enough to hedge the loss; when  $y + z > 0$ , the reserve level is too high. The type I error has to be avoided from the prudential point of view of the regulator, whereas the type II error has to be avoided for the firm, since the reserves receive no the interest rate in the current regulation.

The solution of the optimization problem  $(46)$ [19],

$$\hat{z}_t = \arg\max_{z_t} E_t[\alpha(y_{t+1} + z_t)^+ + (1 - \alpha)(y_{t+1} + z_t)^-]$$
(47)

performed over the variables  $z_t$  function of the information, is

$$\hat{z}_t = -Q_t(\alpha) = VaR_t(\alpha) \tag{48}$$

Thus, the reserve level can be interpreted as a control variate and the conditional VaR as the optimal control variate.

In this control framework, the optimal value of the criterion function is given as  $[24]$ 

$$\begin{aligned} \psi(t,\hat{z}_{t}) &= \alpha P_{t}[y_{t+1} > -\hat{z}_{t}] \\ &\times E_{t}[(y_{t+1} + \hat{z}_{t})^{+}|y_{t+1} > -\hat{z}_{t}] + (1-\alpha) \\ &\times P_{t}[y_{t+1} < \hat{z}_{t}]E_{t}[(y_{t+1} + \hat{z}_{t})^{-}|y_{t+1} < -\hat{z}_{t}] \\ &= \alpha(1-\alpha)[TVar^{+}(\alpha) + TVaR^{-}(\alpha)] \end{aligned} \tag{49}$$

where  $TVaR^+$  and  $TVaR^-$  are the Tail-VaR associated with the right and left tails of the conditional distribution, respectively. Thus, if the VaR is used as the reserve level, the Tail-VaRs have also to be computed and provide the optimal value of the decision criterion.

#### Specification Test

In practice, it is usual to check the validity of the proposed reserve levels  $\widehat{VaR}_t$  by comparing the announced level  $\alpha$  with the frequency of exceedance dates with  $y_t + \widehat{VaR}_t < 0$ . This practice is misleading. Indeed, two different procedures for determining the reserves can give the same frequency, 5%, say, but the dates at which the reserves are not sufficient can be equally located with the first procedure and come in cluster with the second one. Clearly, if  $T = 100$ , the second procedure, in which losses will cumulate over five periods, say, is more risky. An appropriate validation has to distinguish these situations.

In fact, the first-order conditions of the control problem are as follows:

$$\frac{\partial \psi}{\partial z}(t,\hat{z}_t) = 0 \Leftrightarrow E_t \left[ \mathbf{1}_{y_{t+1} + \hat{z}_t < 0} \right] = \alpha \qquad (50)$$

which is the definition of the conditional VaR, that is,

$$P_t[y_{t+1} + \hat{z}_t < 0] = \alpha \tag{51}$$

The first-order condition  $(50)$  is a conditional moment restriction. As usual, it can be replaced by a set of unconditional moment restrictions by introducing instrumental variables  $g_t$ , which are observable functions of the past. We get

$$E[g_t(\mathbf{1}_{y_{t+1}+\hat{z}_t<0}-\alpha)] = 0 \quad \forall g_t \tag{52}$$

Specification tests can be constructed from the sample counterparts of these restrictions; the test compares the statistics  $(1/T) \sum_{t=1}^{T} g_t(\mathbf{1}_{y_{t+1}+\hat{z}_t<0} - \alpha)$ to zero, after an appropriate standardization.

The current practice, considering the historical frequency  $(1/T)\sum_{t=1}^{T}(\mathbf{1}_{y_{t+1}+\hat{z}_t<0}-\alpha)$ , thus, selects  $g_t = 1$  as the single instrumental variable. Clearly, other instrumental variables have also to be considered to detect the persistence in extreme losses, such  $as$ 

$$g_{1,t} = \mathbf{1}_{y_t + \hat{z}_{t-1} < 0}, g_{2,t} = \mathbf{1}_{y_{t-1} + \hat{z}_{t-2} < 0}, \dots \tag{53}$$

which indicate the lack of reserve in the past.

#### Dependent Business Lines

Let us consider two business lines, say,  $y_{1,t}$ ,  $y_{2,t}$ . The current regulation suggests to compute separately the VaR for the two lines, with the same  $\alpha$ , that is, to compute  $VaR_{1,t}(\alpha)$ ,  $VaR_{2,t}(\alpha)$ . Then, the total reserve is  $VaR_{1,t}(\alpha) + VaR_{2,t}(\alpha)$ . This regulation does not account for the dependence between the two risks. The question of reserve allocations between business lines is difficult. A possible solution introduced by Gourieroux and Liu [16] focuses on the definition of an appropriate decision criterion. By analogy with the control problem described in the section The Control Problem, we may consider the objective function:

$$\begin{aligned}\n\psi(t; z_{1t}, z_{2t}) \\
&= E_t \{ [\alpha(y_{1,t+1} + z_{1t})^+ + (1 - \alpha)(y_{1,t+1} + z_{1t})^-] \\
&\times [\alpha(y_{2,t+1} + z_{2t})^+ + (1 - \alpha)(y_{2,t+1} + z_{2t})^-] \} \n\end{aligned} \tag{54}$$

which distinguished four types of errors, which are type I and II errors cross with business lines. If the loss variables  $y_{1,t+1}$  and  $y_{2,t+1}$  are conditionally independent, the objective function is equal to the product:

$$E_{t}[\alpha(y_{1,t+1}+z_{1t})^{+}(1-\alpha)(y_{1,t+1}+z_{1t})^{-}]$$
  
× 
$$E_{t}[\alpha(y_{2,t+1}+z_{2t})^{+}+(1-\alpha)(y_{2,t+1}+z_{2,t})^{-}]$$
  
(55)

and the solutions of the control problem are simply the VaR computed per business line.

$$\hat{z}_{1,t} = VaR_{1,t}(\alpha), \hat{z}_{2,t} = VaR_{2,t}(\alpha) \tag{56}$$

If the loss variables are dependent, the optimization of the objective function (54) provides another solution, which accounts for the dependence between extreme risks. The advantage of this approach, based on the direct optimization of the control decision criterion, is that it is easy to extend to any number of business lines and can provide a solution without having to estimate or specify the joint distribution of  $(y_{1,t+1}, y_{2,t+1}).$ 

## **Concluding Remarks**

The new regulations have led to a rethink on the whole question of risk measures in term of reserve levels and to see the determination of reserves as a control problem. As a consequence, the standard volatility risk measure is progressively being replaced by the VaR, Tail-VaR, or another DRM for several financial problems such as portfolio management [1, 5, 10, 14, 21], performance comparisons [7], or even derivative pricing, especially in insurance [3, 25].

### Acknowledgments

The author gratefully acknowledges financial support of NSERC Canada and of the chair AXA/Risk Foundation "Large Risks in Insurance".

## **End Notes**

<sup>a.</sup>Thus, we implicitly assume that the current portfolio value is known. This assumption is satisfied for assets that are highly traded on the markets, but should be discussed for over-the-counter (OTC) products.

<sup>b.</sup>The portfolio returns  $(W_{t+h} - W_t)/W_t$  can be even more stationary; the corresponding  $\alpha$ -quantile becomes  $-VaR(t, h; \alpha)/W_t$ .

<sup>c</sup>. Equivalently if the cumulative distribution function (cdf) of  $W$  is smaller than the cdf of  $W^*$ .

<sup>d.</sup>This is called an  $L$ -statistic in the statistical literature.

<sup>e.</sup>It also arises when computing the VaR by historical simulation, since the asymptotic properties of the sample quantile, especially the asymptotic variance–covariance matrix, are modified under serial dependence.

## References

- Acerbi, C. & Simonetti, P. (2002). Portfolio Optimiza-[1] tion with Spectral Measure of Risk. DP. Abaxbank.
- [2] Artzner, P., Delbaen, F., Eber, J. & Heath, D. (1999). Coherent measures of risk, Mathematical Finance 9, 203-228.

- Basak, S. & Shapiro, A. (2001). Value-at-risk based [3] risk management: optimal policies and asset prices, The Review of Financial Studies 14, 371-405.
- [4] Basel Committee on Banking Supervision (1995). An Internal Model Based Approach to Market Risk Capital Requirements. Bank of International Settlements, Working Paper.
- [5] Bassi, F., Embrechts, P. & Kafetzaki, M., (1997). Risk management and quantile estimation, in *Practical Guide* to Heavy Tails. Adler. R., Feldman. K. & M., Taggu. eds. Birkhauser, Boston.
- [6] Billio, M. & Pelizzon, L. (2000). Value-at-risk: a multivariate switching regime approach, Journal of Empirical Finance 7, 531-554.
- Darolles, S., Gourieroux, C. & Jasiak, J. (2009). [7] L-Performance Measures with Application to Hedge Funds. CREST DP.
- Elamir, E. & Seheult, A. (2003). Trimmed [8] L-moments, Computational Statistics and Data Analysis 43. 299-314.
- Engle, R. & Manganelli, S. (2004). CAViaR: conditional [9] autoregressive value-at-risk by regression quantile, Journal of Business and Economic Statistics 22, 367-381.
- [10] Foellmer, H. & Leukert, P. (1999). Quantile hedging, Finance and Stochastics 3, 251-273.
- [11] Giacomini, R. & Komunjer, I. (2005). Evaluation and combination of conditional quantile forecasts, Journal of Business and Economic Statistics 23, 416-431.
- [12] Giacomini, R. & White, H. (2006). Test of conditional predictive ability, *Econometrica* **74**, 1545-1578.
- [13] Gourieroux, C. & Jasiak, J. (2008). Dynamic quantile model, Journal of Econometrics 147, 198-205.
- Gourieroux, C., Laurent, J.P. & Scaillet, O. (2000). Sen-[14] sitivity analysis of value-at-risk, Journal of Empirical Finance 7, 225-245.
- [15] Gourieroux, C. & Liu, W. (2007). Converting Tail-VaR to VaR: an Econometric Study. CREST-DP.
- Gourieroux, C. & Liu, W. (2009). Control and out-of-[16] sample validation of dependent risks, Journal of Risk and Insurance 75, 683-707.
- [17] Hosking, J. (1990). L-moments: analysis and estimation of distribution using linear combinations of order statistics, Journal of the Royal Statistical Society, B 52,  $105 - 124$ .
- [18] Jones, B. & Zitikis, R. (2003). Empirical estimation of risk measures and related quantities, North-American Actuarial Journal 7, 44-54.
- [19] Koenker, R. (2005). Quantile Regression, Cambridge University Press.
- [20] Koenker, R. & Xiao, Z. (2006). Quantile autoregression, JASA 101, 980-990.
- [21] Liu, W. (2007). Analysis of Risk Measures and Multidimensional Risk Dependence. PhD dissertation, University of Toronto.
- Schmeidler, D. (1989). Subjective probability and [22] expected utility without additivity, *Econometrica* 57, 571-587.

- [23] Shorack, G. & Wellner, J. (1986). *Empirical Processes with Applications to Statistics*, Wiley, New-York.
- [24] Uryasev, S. & Rockafellar, R. (2000). Optimization of conditional value-at-risk, *Journal of Risk* **2**, 21–41.
- [25] Wang, S. (1996). Premium calculation by transforming the layer premium density, *ASTIN Bulletin* **26**, 71–92.
- [26] Wang, S. (2000). A class of distortion operators for pricing financial and insurance risks, *Journal of Risk and Insurance* **67**, 15–36.
- [27] Wang, S. & Young, V. (1998). Ordering risks: expected utility theory versus Yaari's dual theory of risk, *Insurance: Mathematics and Economics* **22**, 145–161.
- [28] Yaari, M. (1987). The dual theory of choice under risk, *Econometrica* **55**, 95–115.

# **Further Reading**

Cont, R., Deguest, R. & Scandolo, G. (2007). *Robustness and Sensitivity Analysis of Risk Measurement Procedures*, Columbia University Financial Engineering Report No. 2007-06.

Koenker, R. & Zhao, Q., (1996). Conditional quantile estimation and inference for ARCH models, *Econometric Theory* **12**, 793–813.

# **Related Articles**

**Backtesting**; **Convex Risk Measures**; **Expected Shortfall**; **Market Risk**; **Model Validation**; **Multivariate Distributions**; **Regulatory Capital**; **Simulation-based Estimation**; **Spectral Measures of Risk**; **Stylized Properties of Asset Returns**; **Valueat-Risk**.

CHRISTIAN GOURIEROUX
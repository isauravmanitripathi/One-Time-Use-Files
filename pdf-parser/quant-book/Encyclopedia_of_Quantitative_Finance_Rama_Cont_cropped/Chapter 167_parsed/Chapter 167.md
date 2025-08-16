# **Structural Default Risk** Models

Structural models of default risk for individual firms originate from the seminal work of Merton [25]. Default is linked to the economic fundamentals of the considered firm via the assumption that default occurs if the value of the firm's assets, modeled as a geometric Brownian motion, falls below some default threshold (the firm's liabilities) at some future point in time (the maturity of a zero-coupon bond). A significant extension of this methodology was proposed by Black and Cox [7], who continuously test for default. Hence, in their model, the time of default is a first-passage time. Further generalizations address stochastic interest rates, more general assumptions on the default threshold, the definition of the default event, and discontinuous processes as model for the firm's assets [10, 12, 20-22, 34]. On a high level, these innovations aim at making the model-induced term structure of default probabilities flexible enough to allow for a precise fit of the model to observed bond prices and credit default swap (CDS) spreads.

The growing popularity of derivatives on credit portfolios, for example, collateralized debt obligations (CDOs) and  $n$ th to default baskets, and advanced demands on risk-management solutions produced a need for portfolio models that simultaneously explain the credit quality of multiple firms. Since corporate defaults in a globalized economy are not independent, a multivariate default model has to explain univariate default probabilities and the dependence among the default events. A natural assumption for a multivariate structural-default model is to introduce dependence by assuming correlated asset values, leading to dependent default events. Zhou [33] motivates this approach by the observation: "The fortunes of individual companies are linked together via industry-specific and/or general economic conditions." The first portfolio model of this class was formulated by Vasicek [31] and can be classified as a multivariate generalization of the work by Merton [25]. This model is discussed in some detail in the section "The Model of Vasicek", as it constitutes the basis for most of today's generalizations and is used to asses the regulatory capital for loan portfolios within the Basel II framework.

A major advantage of (multivariate) structuraldefault models is the appealing economic interpretation of the definition of default. Additionally, comovements of the individual firm-value processes might also be interpreted as being the result of common risk factors. Moreover, modeling the evolution of the firm's values as some multivariate stochastic process naturally implies a dynamic model, which is highly desirable in risk-management and pricing applications. The downside of this class of models is the mathematical challenge of computing the portfolio-loss distribution or even bivariate default correlations. Hence, most of the proposed models rely on simplifying assumptions or can be solved only *via* a Monte Carlo simulation.

## **Merton-type Models**

## The Model of Vasicek

In his short memo [31], Vasicek considers a portfolio of  $n$  loans with unit nominal and maturity  $T$ . Each individual firm-value process is modeled as a geometric Brownian motion defined by the stochastic differential equation:

$$\begin{aligned} \mathrm{d}V_t^i &= V_t^i(\gamma^i \mathrm{d}t + \sigma^i \mathrm{d}W_t^i), \\ V_0^i &> 0, \quad i \in \{1, \dots, n\} \end{aligned} \tag{1}$$

The first simplification, often referred to as *homo*geneous portfolio assumption, is to assume identical default probabilities for all firms. In the current setup, this assumption corresponds to identical parameters  $V_0 \equiv V_0^i$ ,  $\sigma \equiv \sigma^i$ , and  $\gamma \equiv \gamma^i$ . Moreover, an identical correlation across all bivariate pairs of Brownian motions  $W^i$  and  $W^j$  is assumed. Using Itô's formula and replacing the growth rate  $\gamma$  by the risk-free interest rate  $r$ , we find

$$V_T^i \stackrel{d}{=} V_0^i \exp((r - 0.5\sigma^2)T + \sigma\sqrt{T}X^i) \quad (2)$$

where  $X^i := W^i_T / \sqrt{T}$  follows a standard normal distribution. Given some default threshold  $d_T \equiv d_T^i$ , one can immediately compute the probability of default at time  $T$ , since the distribution of the firm value at time  $T$  is known explicitly. Moreover, since default can only happen at maturity, only the distribution of  $V_T^i$  is of importance and not the dynamic model leading to it. By scaling the

original default threshold, default can alternatively be expressed in terms of the standard normally distributed variable  $X^i$ . More precisely, assuming the default probability of firm  $i$  at time  $T$  is given by  $p^i$ , the default threshold with respect to  $X^i$  is  $K^{i} = \Phi^{-1}(p^{i})$ , where  $\Phi^{-1}$  is the quantile function of the standard normal distribution.

To incorporate correlation among the companies, one explains  $X^i$  by a common market factor M and an idiosyncratic risk factor  $\epsilon^i$ , that is,

$$X^{i} \stackrel{d}{=} \sqrt{\rho}M + \sqrt{1 - \rho}\epsilon^{i}, \quad \rho \in (0, 1) \tag{3}$$

where  $M$ ,  $\{\epsilon^i\}_{i=1}^n$  are independent standard normally distributed random variables. Consequently,  $\text{Cor}(X^i, X^j) = \rho$  for  $i \neq j$ , and each  $X^i$  is again distributed according to the standard normal law. By conditioning on the common market factor  $M$ , the firm's values and default events are independent. The result is the so-called *conditionally independent model.* We denote this conditional default probability by  $p^i(M)$  and obtain

$$p^{i}(m) = \mathbb{P}(X^{i} < K^{i}|M=m) = \Phi\left(\frac{K^{i} - \sqrt{\rho}m}{\sqrt{1-\rho}}\right)$$
(4)

Furthermore, all companies are assumed to have identical default probabilities  $p \equiv p^i$ . Now  $\Omega$  is defined as the random variable that describes the fraction of defaults in the portfolio up to time  $t$ . The distribution of  $\Omega$  depends on two parameters: the individual default probability  $p$  and the correlation  $\rho$ . In what follows, this distribution is denoted by  $F_{p,0}^{(n)}(x) = \mathbb{P}(\Omega \leq x)$ . It is crucial that firms are independent given  $M$ , since the probability that exactly  $k$  firms default can be derived by integrating out the market factor:

$$\mathbb{P}(n\Omega = k) = \int_{-\infty}^{\infty} \mathbb{P}(n\,\Omega = k|M = m)$$
$$\times \phi(m) \mathrm{d}m \qquad (5)$$
$$= \int_{-\infty}^{\infty} {n \choose k} p(m)^{k} (1 - p(m))^{n-k}$$
$$\times \phi(m) \mathrm{d}m \qquad (6)$$

where  $\phi$  is the density of a standard normal distribution and  $k \in \{0, \ldots, n\}$ . For large portfolios, evaluating the binomial coefficient is numerically critical and can be avoided by applying the law of large numbers; this approach is called *large portfolio approximation*. The key observation is that  $\mathbb{P}(\Omega \le x | M = m) \rightarrow$  $\mathbf{1}_{\{n(m)<\kappa\}}$  for  $(n \to \infty)$ . A straightforward calculation, see, for example, [29] for details, establishes

$$F_{p,\rho}^{(n)}(x)$$

$$\to F_{p,\rho}^{\infty}(x) := \Phi\left(\frac{\sqrt{1-\rho}\,\Phi^{-1}(x) - \Phi^{-1}(p)}{\sqrt{\rho}}\right),\,$$

$$(n \to \infty)$$
(7)

This approximation is continuous and strictly increasing in  $x$ . As it further maps the unit interval onto itself, it is a distribution function, too. It is also worth mentioning that the quality of this approximation is typically good; see [29] for a discussion.

#### The IRB Approach in Basel II

Vasicek's asymptotic loss distribution or, more precisely, its quantile function

$$K_{p,\rho}(y) := \Phi\left(\frac{\Phi^{-1}(y)\sqrt{\rho} + \Phi^{-1}(p)}{\sqrt{1-\rho}}\right) \quad (8)$$

plays a major role in today's regulatory world. The core of the first pillar of the Basel II accord [4] is the internal rating-based (IRB) approach for calculating capital requirements for loan portfolios. Within this framework, banks classify their loans by asset class and credit quality into homogeneous buckets and use their own internal rating systems to estimate risk characteristics such as loss-given default (LGD), the expected exposure at default (EAD), and the oneyear default probability (PD), that is,  $PD = p_1$ . It is worth mentioning that estimating LGD and PD independently contradicts the empirical observation that recovery rates and default rates are inversely related; see, for example, [2] and [11]. Still, banks are free to choose a certain internal rating system, as long as they can demonstrate its accuracy and meet certain data requirements. In the second step, these credit characteristics are used in the IRB formula to asses the minimum capital requirements for the unexpected loss via the factor

$$K_{\text{IRB}} = LGD \cdot \left( K_{PD,\rho}(99.9\%) - PD \right) \cdot MA \quad (9)$$

The risk-weighted assets  $(RWA)$  are then obtained by

$$RWA = \frac{K_{\text{IRB}} \cdot EAD}{0.08} = 12.5 \cdot K_{\text{IRB}} \cdot EAD \quad (10)$$

where  $0.08$  corresponds to the  $8\%$  minimum capital ratio. The very conservative one-year 99.9%-quantile in equation (9) is part of the Basel II accord and might be interpreted as some cushion regarding the underlying simplifications in Vasicek's model. The factor MA is the *maturity adjustment* and calculated *via* (some exceptions apply)

$$MA = \frac{1 + (M - 2.5) \cdot b(PD)}{1 - 1.5 \cdot b(PD)},$$
$$M = \min\left\{\frac{\sum_{t} t \cdot CF_t}{\sum_{t} CF_t}, 5\right\} \tag{11}$$

and  $b(PD) = (0.11852 - 0.05478 \cdot \log PD)^2$ , where  $CF_t$  denotes the expected cash-flow at time t. M accounts for the fact that loans with longer (shorter) maturity than one year require a higher (lower) capital charge. Finally, the crucial correlation parameter needs to be specified. Basel II uses a convex combination between some lower  $\rho^l$  and upper  $\rho^u$  correlation whose weights depend on the default probability of the respective loan, that is,

$$\rho = \rho^{l}a(PD) + \rho^{u}(1 - a(PD)),$$
  
$$a(x) = \frac{1 - e^{-50x}}{1 - e^{-50}}$$
 (12)

For corporate credits, the correlation-adjustment factor

$$SM_{\text{ad}}(S) = -0.04 \cdot \left(1 - \frac{\max\{5, S\} - 5}{45}\right) \times \mathbb{1}_{\{S \le 50\}}$$
(13)

is added to  $\rho$  for borrowers with reported annual sales  $S \le 50$ , measured in millions of Euros. The specific form of  $a(x)$  and the adjustment factor  $SM_{ad}(S)$ being negative stem from the empirical observation [23] that large firms that bear more systemic risk are more correlated compared to small firms that

are more likely to default due to idiosyncratic reasons.  $(\rho^l, \rho^u)$  depend on the type of loan and are specified as  $(0.12, 0.24)$  for sovereign, corporate, and bank loans;  $(0.12, 0.30)$  for highly volatile commercial real estate loans;  $\rho^l = \rho^u = 0.15$  for residential mortgages;  $\rho^l = \rho^u = 0.04$  for revolving retail loans such as credit cards; and finally  $(0.03, 0.16)$  for other retail exposures, where in this case the weight function  $a(x)$  is computed with exponents  $-35$  instead of  $-50$ .

The IRB approach is sometimes criticized for the strong assumptions that are required to derive Vasicek's distribution. However, one should recognize the IRB approach as a compromise that provides a common language for regulators, banks, and investors to communicate and establishes comparable risk estimates across banks. The IRB formula is discussed in depth in  $[5, 30]$ .

#### Generalizations Using Other Distributions

It is well known that the model [31] does not yield a satisfactory fit to market quotes of tranches of CDOs. More precisely, an implied correlation smile is present when the model is inverted for the correlation parameter tranche by tranche. Especially tail events with multiple defaults are underrepresented in a Gaussian world, making a precise fit to senior tranches of a CDO impossible. To overcome this shortcoming, a natural assumption is to give up normality in equation (3) and consider other heavier tailed distributions. For the derivation leading to  $F_{p,\rho}^{\infty}$  in equation (7), the stability of the normal distribution under convolutions is essential in equation (3). Hence, natural choices for generalizations are other infinitely divisible distributions, which are connected to Lévy processes; see, for example, [8]. These generalizations add flexibility to the model and can additionally imply a dependence structure with tail dependence, making multiple defaults more likely. Specific models in this spirit include, for example, the NIG model of Kalemanova et al. [17], the VG model of Moosbrucker [27], and the BVG model of Baxter [6]. Following [1], we now derive a large homogeneous portfolio approximation in a general Lévy framework.

Let  $X = \{X_t\}_{t \in [0,1]}$  be a Lévy process (see Lévy **Processes**) with  $X_1 \sim H_1$  for some infinitely divisible distribution  $H_1$ . Assume  $X_1$  to be standardized to zero mean and unit variance. Given a correlation

 $\rho \in (0, 1)$ , define in analogy to equation (3) for independent copies  $\{X^i\}_{i=1}^n$  of X the random variables  $V^i$ by

$$V' := X_{\rho} + X'_{1-\rho}, \quad i \in \{1, \dots, n\} \tag{14}$$

Here, the common market factor is represented by  $X_{\rho}$ , and the idiosyncratic risk of firm *i* is captured in  $X_{1-o}^i$ . Using the Lévy properties of X, each  $V^i$  is again distributed according to  $H_1$  and  $\text{Cor}(V^i, V^j) = \rho$  for  $i \neq j$ . In what follows, we denote by  $H_t^{-1}$  the inverse of the distribution function of  $X_t$ . The homogeneous portfolio assumption in the present setup translates to identical univariate default probabilities up to time  $T$ , abbreviated as  $p \equiv p^{i}$ , identical threshold levels  $K_{T} = H_{1}^{-1}(p) \equiv$  $K_T^i$ , and unit notional of each firm. The probability of exactly  $k$  defaults in the portfolio is then again obtained as

$$\mathbb{P}(n\Omega = k) = \int_{-\infty}^{\infty} \mathbb{P}(n\,\Omega = k | X_{\rho} = m) \mathrm{d}H_{\rho}(m),$$
  
$$k \in \{0, \dots, n\}$$
 (15)

Similar to Vasicek's model, the conditional distribution of the number of defaults given  $X_{\rho} = m$  is a binomial distribution with  $n$  trials and success probability  $p(m) = \mathbb{P}(V^i \leq K_T | X_\rho = m) = H_{1-\rho}(K_T - m)$  $m$ ). The large portfolio assumption, that is, letting the number of firms  $n$  tend to infinity, then gives

$$F_{p,\rho}^{\infty}(x) = 1 - H_{\rho}(H_1^{-1}(p) - H_{1-\rho}^{-1}(x)) \tag{16}$$

as distribution function of the fractional loss in an infinite granular portfolio; see [1] for a complete proof. Let us finally remark that evaluating  $H_t$  and  $H_t^{-1}$  requires numerical routines for most choices of  $X_1 \sim H_1.$ 

#### The Model of Willemann

The starting point for Willemann [32] is the univariate jump-diffusion model of Zhou [34]. This model assumes a discontinuous firm-value process of the form

$$dV_t = V_t((\gamma - \lambda \nu)dt + \sigma dW_t + (\Pi - 1)dN_t),$$
  
$$V_0 > 0$$
 (17)

where  $N_t$  is a Poisson process with intensity  $\lambda > 0$ and the jumps  $\Pi$  are log-normally distributed with

expected jump size  $\nu = \mathbb{E}[\Pi - 1]$ . The advantage of supporting negative jumps on a univariate level is that default events are no longer predictable, which translates to positive short-term credit spreads. Willemann [32] incorporates dependence to the individual firm-value processes by the classical decomposition of each Brownian motion into a market factor and an idiosyncratic component. Moreover, it is assumed that all firm-value processes jump together, that is, all processes are driven by the same Poisson process  $N_t$ . Consequently, this construction allows for two layers of correlation: diffusion and jump correlation; the latter being the main innovation of this setup.

The default threshold of firm *i* is set to  $K_t^i =$  $e^{-\phi^{i}t}K_{0}^{i}$  for some positive constants  $\phi^{i}$  and  $K_{0}^{i}$ . This declining form is chosen to increase short-term spreads, but might also imply that the fit to individual CDS gets worse with increase in time. To achieve semianalytical results for the portfolio-loss distribution, default is tested on a grid. The advantage of this simplification is that only the distribution of each firm-value process at the grid points is required, instead of functionals as  $\inf_{s\in[0,t]} V_s$ . Individual default probabilities up to time  $t$  can then be computed conditional on the number of jumps up to time  $t$ , which is a Poisson-distributed random variable. Since the specific choice of jump-size distribution is compatible to the Brownian motion of the model, this leads to an infinite sum of normally distributed random variables. Moreover, all default events are independent conditional on the market factor and the number of jumps. Hence, the portfolioloss distribution can be found by integrating out these common factors and using a recursion technique similar to [3, 16]. Willemann [32] demonstrates quite successfully how the model is simultaneously fitted (in seconds) to individual CDS spreads and the tranches of a CDO.

#### A Remark on Asset and Default Correlation

Modeling asset values as correlated stochastic processes introduces dependence to the resulting default times. Still, this relation is not trivial and deserves some caution, especially when it comes to estimating the model's asset-correlation parameter. We follow  $[24]$  in defining the default correlation of two firms (up to time  $t$ ) as

$$\rho_{t}^{D} := \text{Cor}(\mathbb{1}_{\{\tau^{1} \le t\}}, \mathbb{1}_{\{\tau^{2} \le t\}})\n$$

$$\n= \frac{\mathbb{P}(P_{t}^{1}, P_{t}^{2}) - \mathbb{P}(P_{t}^{1}) \mathbb{P}(P_{t}^{2})}{\sqrt{\mathbb{P}(P_{t}^{1})(1 - \mathbb{P}(P_{t}^{1}))} \sqrt{\mathbb{P}(P_{t}^{2})(1 - \mathbb{P}(P_{t}^{2}))}}\n$$
(18)

where  $P_t^i := \{\tau^i \le t\}, i \in \{1, 2\}.$  Most structuraldefault models share the commanality that evaluating  $\mathbb{P}(P_t^1, P_t^2)$ , the probability of a joint default of both firms up to time  $t$ , is quite difficult; an exception being the case of two companies with Gaussian factors coupled as described in equation (3). This example is, therefore, used to illustrate the nonlinear relation of asset and default correlation. A joint default in this setup corresponds to a simultaneous drop of both factors  $X^1$  and  $X^2$  below their respective default threshold  $K^i = \Phi^{-1}(p_t^i), i \in \{1, 2\}$ . Since the vector  $(X^1, X^2)$  follows a two-dimensional normal distribution with mean vector  $(0, 0)$  and the assetcorrelation  $\rho$  as correlation parameter, we obtain

$$\mathbb{P}(P_t^1, P_t^2) = \Phi_2(K^1, K^2; \rho) \tag{19}$$

which is used to produce Figure 1. This example illustrates that small asset correlations induce only a negligible default correlation.

![](_page_4_Figure_4.jpeg)

**Figure 1** Default correlation  $\rho_t^D$  as a function of asset correlation  $\rho \in [0, 1]$ , with  $\mathbb{P}(P_t^1) = \mathbb{P}(P_t^1) = 0.05$  and  $t = 1$ 

Being able to convert default to asset correlations (and *vice versa*) opens the possibility of estimating the model's asset correlation using historical default correlations (and vice versa); see, for example, [14]. This approach is relevant since asset values are not directly observable, making an estimation of asset correlations delicate. It is an ongoing debate whether indirectly observed changes in asset values, computed from changes in the respective firm's equity, or observed defaults are the better source of data for the estimation of the model's correlation parameter. In both cases, pointing out the respective limitations is much simpler than providing theoretical evidence for the methodology. Empirically estimating default correlations (based on groups of firms with similar characteristics) requires a large set of observations, since corporate defaults are rare events. This makes the approach vulnerable to structural changes such as new bankruptcy rules. On the other hand, daily equity prices are readily available for most firms. When this latter source of data is used, the difficulty lies in transforming equity to asset returns, see, for example, [9], from which the correlation might be estimated. In addition, one should be aware that equity prices might change for reasons that are not related to credit risk.

## **First-passage Time Models**

The starting point for most multivariate first passagetime models is equation (1). Compared to models in the spirit of the work by Merton [25], the time of default is now defined as suggested in  $[7]$ , that is,

$$\tau^{i} := \inf\{t \ge 0 : V^{i}_{t} \le d^{i}_{t}\}, \quad i \in \{1, \dots, n\} \quad (20)$$

where  $d_t^i$  is the default threshold of firm *i* at time  $t$ . From a modeling perspective, this definition overcomes the unrealistic assumption of default being restricted to maturity. This observation is even more crucial in a portfolio environment when bonds with different maturities are monitored simultaneously. More precisely, a first-passage model naturally induces a dynamic model for the default correlation (since the firm-value processes evolve dynamically over time) and allows the computation of consistent default correlations over any time horizon.

However, the main drawback of this model class is its computational intractability. This stems from the fact that the joint distribution of the minimum of several firm-value processes is required, which is already a challenging problem for univariate marginals. The following section collects models where analytical results or numerical routines are available to overcome this problem.

### The Model of Zhou

Zhou studies [33] a portfolio of two firms whose asset-value processes are modeled as in equation (1) with correlated Brownian motions. The default thresholds are assumed to be exponential, that is,  $d_t^i = e^{\lambda^i t} K^i$  for  $i \in \{1, 2\}$ . The degree of dependence of both firms is measured in terms of their *default correlation* up to time *t*, that is, as  $\text{Cor}(\mathbf{1}_{\{\tau^1 \le t\}}, \mathbf{1}_{\{\tau^2 \le t\}})$ . The key observation is that results of Rebholz [28] can be applied to give an analytical representation of the default correlation in terms of an infinite sum of indefinite integrals over modified Bessel functions. Sensitivity analysis of the model parameters indicates that the model-induced default correlations for short maturities are close to zero. This observation needs to be considered when portfolio derivatives with short maturities are priced within such a framework.

### The Model of Giesecke

Giesecke [13] considers a portfolio of  $n$  firms whose value processes evolve according to some vector-valued stochastic process  $(V^1, \ldots, V^n)$ , where default is again defined as in equation (20). The key innovation is to replace the vector of default thresholds by an initially unobservable random vector  $(d^1,\ldots,d^n)$  whose dependence structure is represented by some copula. It is shown that the modelinduced copula of default times is a function of the copula of default thresholds and the copula of the vector of historical lows of the firm-value processes.

On a univariate level, the assumption of an unobservable random threshold overcomes the predictability of individual defaults, which is responsible for vanishing credit spreads for short maturities; see [10] for a related model. Short-term spreads [13] are positive as long as the respective firm-value process is close to its historical low. The consequence of this construction on a portfolio level is also remarkable. Observing a corporate default  $\tau^i$  reveals the respective default threshold  $d^i$  to all investors. This

piece of information allows to update the knowledge on all other default thresholds, leading to contagious jumps in credit spreads of the remaining firms. Giesecke [13] also presents an explicit example of two firms with independent value processes modeled as geometric Brownian motions and default thresholds coupled via a Clayton copula. While this simplified example illustrates the desired contagion effect of the model, it also highlights the challenge of finding analytic results in a realistic framework.

#### Models Relying on Monte Carlo Simulations

This section briefly presents two first-passage time models that rely on Monte Carlo simulations for the pricing of CDOs.

The  $n$  firm-value processes [15] are defined as in equation (1): the model can therefore be considered as a generalization of Zhou's [33] bivariate model to larger portfolios. The default thresholds are rewritten in terms of the driving Brownian motions. Asset correlation is introduced by  $n_F$  risk factors, that is, the Brownian motion of firm  $i$  is replaced by

$$dW_t^i := \sum_{j=1}^{n_F} \alpha_{i,j} dF_t^j + (1 - \sum_{j=1}^{n_F} \alpha_{i,j}^2)^{\tfrac{1}{2}} dU_t^i,$$
  
$$i \in \{1, \dots, n\}$$
 (21)

where  $\alpha_{i,j}$  is the sensitivity of firm *i* to changes of the risk factor  $F^{j}$  and  $U^{i}$  is the idiosyncratic risk of this firm. All processes  $F^j$  and  $U^i$  are independent Brownian motions. Hull et al. [15] also consider extensions to stochastic correlations, stochastic recovery rates, and stochastic volatilities and compare these in terms of their fitting capability to CDO tranches. An interesting conclusion that also applies to similar first-passage time models is drawn when the model is compared to a copula model. It is argued that the default environment in a copula model is static for the whole life of the model, while the dynamic nature of equation (21) allows to have bad default environments in one year, followed by good environments later. Hence, the use of one or more common risk factors implies a sound economic model for cyclical correlation.

Kiesel and Scherer [18] present another multivariate extension of the work by Zhou [34]. They model the firm-value process of the company  $i$  as the exponential of a jump-diffusion process with twosided exponentially distributed jumps  $Y_{ij}$ , that is,

$$V_t^i = V_0^i \exp(X_t^i),$$
  

$$X_t^i = \gamma^i t + \sigma^i W_t^i + \sum_{j=1}^{N_t(b^i)} Y_{ij}, \quad V_0^i > 0 \quad (22)$$

where the Brownian motions of different firms are again correlated *via* a factor decomposition. The novelty in their approach is the use of a Poisson process  $N_t$  as ticker for jumps in the market that is thinned-out with probability  $(1-b^i)$  to induce jumps in  $V^i$ . Consequently, some but not necessarily all firms jump (and possibly default) together. As a result of common jumps, the model allows for default clusters that extend the cyclical correlation induced by common continuous factors. For this choice of jump distribution, the marginals of the model can be calibrated to CDS quotes using the Laplace transform of first-passage times of  $X^i$ , which is derived in [19]. The multivariate model is solved via a Brownianbridge Monte Carlo simulation in the spirit of the work by Metwally and Atiya [26].

## Conclusion

Structural-default models allow for an appealing interpretation of corporate default: companies operate as long as they have sufficient assets. A clear economic interpretation also holds for the way dependence is introduced to a portfolio of companies: comovements of the firm-value processes might be seen as the result of common risk factors, to which economic interpretations might also apply. This rationale can also be used to empirically estimate the correlation structure of the model from market data. Summarizing, the dependence structure and univariate marginals are simultaneously explained. Moreover, since each company is modeled explicitly, called *bottom-up approach*, it is also possible to price portfolio derivatives and individual risk consistently; a major advantage over *top-down models* that purely focus on the portfolio-loss process. In addition, the current asset level might be mapped to some credit rating, implying a dynamic model of rating changes including default. Finally, the dynamic nature of the modeled firm-value processes translates to a dynamic model for the default correlation and the portfolio-loss process; a desired property in riskmanagement solutions and for the pricing of (exotic) credit-portfolio derivatives.

The downside of multivariate structural-default models lies in the difficulty of translating the model to analytical formulas for default correlations and the portfolio-loss distribution. This becomes especially apparent when the simplifying assumption in [31] and its generalizations are reconsidered; the bottomup nature of structural-default models is entirely given up in order to compute the portfolio-loss distribution in closed form. The price to pay for a more realistic framework typically is a Monte Carlo simulation. However, if such a simulation is efficiently implemented, a realistic dynamic model for a portfolio of credit-risky assets is available.

#### Acknowledgments

Research support by Daniela Neykova, Technische Universität München, is gratefully acknowledged.

## References

- $[1]$ Albrecher, H., Ladoucette, S. & Schoutens, W. (2007). A generic one-factor Lévy model for pricing synthetic CDOs, in Advances in Mathematical Finance, M.C. Fu. R.A. Jarrow, J.J. Yen & R.J. Elliott, eds, Birkhaeuser.
- [2] Altman, E., Resti, A. & Sironi, A. (2004). Default recovery rates in credit risk modeling: a review of the literature and empirical evidence, *Economic Notes* **33**(2), 183-208.
- Andersen, L. & Sidenius, J. (2004). Extensions of the [3] Gaussian copula: random recovery and random factor loadings, Journal of Credit Risk 1(1), 29-70.
- Basel Committee on Banking Supervision (2004). Inter-[4] national Convergence of Capital Measurement and Capital Standards-A Revised Framework, retrieved from http://www.bis.org/publ/bcbs107.pdf.
- [5] Basel Committee on Banking Supervision (2005). An Explanatory Note on the Basel II IRB Risk Weight Functions, retrieved from http://www.bis.org/bcbs/irbriskweight.pdf.
- Baxter, M. (2006). *Dynamic Modelling of Single-name* [6] Credits and CDO Tranches. Working paper, Nomura Fixed Income Quant Group.
- Black, F. & Cox, J. (1976). Valuing corporate securities: [7] some effects of bond indenture provisions, Journal of Finance 31(2), 351-367.
- [8] Cont, R. & Tankov, P. (2004). Financial Modelling with Jump Processes, Financial Mathematics Series, Chapman and Hall/CRC.

# **8 Structural Default Risk Models**

- [9] Crosbie, P. & Bohn, J. *Modeling Default Risk*, KMV Corporation, retrieved from http://www.moodyskmv. com/research/files/wp/ModelingDefaultRisk.pdf.
- [10] Duffie, D. & Lando, D. (2001). The term structure of credit spreads with incomplete accounting information, *Econometrica* **69**, 633–664.
- [11] Frye, J. (2000). Depressing recoveries, *Risk* **13**(11), 106–111.
- [12] Geske, R. (1977). The valuation of corporate liabilities as compound options, *Journal of Financial and Quantitative Analysis* **12**(4), 541–552.
- [13] Giesecke, K. (2004). Correlated default with incomplete information, *Journal of Banking and Finance* **28**(7), 1521–1545.
- [14] Gordy, M. (2000). A comparative anatomy of credit risk models, *Journal of Banking and Finance* **24**(1), 119–149.
- [15] Hull, J., Predescu, M. & White, A. (2005). *The Valuation of Correlation-dependent Credit Derivatives using a Structural Model*. Working paper, retrieved from http://www.rotman.utoronto.ca/hull/DownloadablePublications/StructuralModel.pdf
- [16] Hull, J. & White, A. (2004). Valuation of a CDO and an n-th to default CDS without a Monte Carlo simulation, *Journal of Derivatives* **12**(2), 8–23.
- [17] Kalemanova, A., Schmid, B. & Werner, R. (2007). The normal inverse Gaussian distribution for synthetic CDO pricing, *Journal of Derivatives* **14**(3), 80–93.
- [18] Kiesel, R. & Scherer, M. (2007). *Dynamic Credit Portfolio Modelling in Structural Models with Jumps*. working paper, retrieved from http://www.uni-ulm.de/fileadmin/ website uni ulm/mawi.inst.050/ people/kiesel/publications/ Kiesel Scherer Dec07.pdf.
- [19] Kou, S. & Wang, H. (2003). First passage times of a jump diffusion process, *Advances in Applied Probability* **35**, 504–531.
- [20] Leland, H. (1994). Corporate debt value, bond covenants, and optimal capital structure, *Journal of Finance* **49**(4), 1213–1252.
- [21] Leland, H. & Toft, K. (1996). Optimal capital structure, endogenous bankruptcy, and the term structure of credit spreads, *Journal of Finance* **51**(3), 987–1019.
- [22] Longstaff, F. & Schwartz, E. (1995). A simple approach to valuing risky fixed and floating rate debt, *Journal of Finance* **50**(3), 789–819.
- [23] Lopez, J. (2004). The empirical relationship between average asset correlation, firm probability of default, and asset size, *Journal of Financial Intermediation* **13**(2), 265–283.
- [24] Lucas, D. (1995). Default correlation and credit analysis, *Journal of Fixed Income* **4**(4), 76–87.

- [25] Merton, R. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470. Reprinted as Chapter 12 in Merton, R. (1990) *Continuous-time Finance*, Blackwell.
- [26] Metwally, S. & Atiya, A. (2002). Using Brownian bridge for fast simulation of jump-diffusion processes and barrier options, *The Journal of Derivatives* **10**(1), 43–54.
- [27] Moosbrucker, T. (2006). *Pricing CDOs with Correlated Variance Gamma Distributions*. Research report, Department of Banking, University of Cologne.
- [28] Rebholz, J. (1994). *Planar Diffusions with Applications to Mathematical Finance*, PhD thesis, University of California, Berkeley.
- [29] Schonbucher, P. (2003). ¨ *Credit Derivatives Pricing Models: Models, Pricing, Implementation*, Wiley Finance.
- [30] Thomas, H. & Wang, Z. (2005). Interpreting the internal ratings-based capital requirements in Basel II, *Journal of Banking Regulation* **6**, 274–289.
- [31] Vasicek, O. (1987). *Probability of Loss on Loan Portfolio*, KMV Corporation, retrieved from http://www.moodyskmv.com/research/whitepaper/Probability of Loss on Loan Portfolio.pdf
- [32] Willemann, S. (2007). Fitting the CDO correlation skew: a tractable structural jump-diffusion model, *The Journal of Credit Risk* **3**(1), 63–90.
- [33] Zhou, C. (2001). An analysis of default correlations and multiple defaults, *Review of Financial Studies* **14**, 555–576.
- [34] Zhou, C. (2001). The term structure of credit spreads with jump risk, *Journal of Banking and Finance* **25**, 2015–2040.

# **Further Reading**

Lipton, A. (2002). Assets with jumps, *Risk* **15**(9), 149–153.

Lipton, A. & Sepp, A. (2009). Credit value adjustment for credit default swaps via the structural default model, *The Journal of Credit Risk* **5**(2), 125.

# **Related Articles**

**Default Barrier Models**; **Modeling Correlation of Structured Instruments in a Portfolio Setting**; **Gaussian Copula Model**; **Internal-ratings-based Approach**; **Reduced Form Credit Risk Models**.

RUDIGER ¨ KIESEL & MATTHIAS A. SCHERER
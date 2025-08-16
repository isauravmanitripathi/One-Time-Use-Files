# **Default Barrier Models**

The modeling of default from an economic point of view is a great challenge due to the binary and low probability nature of such an event. Default barrier models provide an elegant solution to this challenge since they link the default event to the point at which some continuously evolving quantity hits a known barrier. In structural models of credit risk (see **Structural Default Risk Models**) the process and the barrier are interpreted in terms of capital structure of the firm as the value of the firm and its liabilities. More generally, one can view the process and the barrier as state variables that need not necessarily observable.

## **Single-name Models**

In the classic Merton framework [12], the value of a firm (asset value) is considered to be stochastic and default is modeled as the point where the firm is unable to pay its outstanding liabilities when they mature. The asset value is modeled as a geometric Brownian motion:

$$\frac{\mathrm{d}V_t}{V_t} = \mu \mathrm{d}t + \sigma \mathrm{d}W \tag{1}$$

where  $\mu$  and  $\sigma$  represent the drift and volatility of the asset, respectively, and  $dW$  is a standard Brownian motion. The original Merton model assumes that a firm has issued only a zero-coupon bond and will not therefore default prior to the maturity of this debt as illustrated in Figure 1. Denoting the maturity and face value of the debt by  $T$  and  $D$  respectively, the default condition can then be written as  $V_T < D$ . Through option pricing arguments, Merton then provides a link between corporate debt and equity via pricing formulae based on the value of the firm and its volatility (analogously to options being valued from spot prices and volatility). The problem of modeling default is transformed into that of assessing the future distribution of firm value and the barrier where default would occur. Such quantities can be estimated nontrivially from equity data and capital structure information. This is then the key contribution of Merton approach in that low-frequency binary events can be modeling via a continuous process and calibrated using highfrequency data.

#### Practical Extensions of the Merton Approach

The classic Merton approach has been extended by many authors such as Black and Cox [2] and Leland [10]. Commercially, it has been developed by KMV<sup>™</sup> (now Moody's KMV) with the aim of predicting default via the assessment of 1-year default probability defined as  $EDF^{TM}$  (expected default frequency). A more recent and related, although simpler, approach is CreditGrades<sup>™</sup>.

Moody's KMV Approach. This approach [8, 9] was inspired by the Merton approach to default modeling and aimed to lift many of the stylized assumptions and model the evolution and future default of a company in a realistic fashion. A key aspect of this is to account for the fact that a firm may default at any time but will not necessarily default immediately when they are bankruptcy insolvent (when  $V_t < D$ ). Hence a challenge is to work out exactly where the default barrier is. KMV do this via considering both the short-term and long-term liabilities of the firm. Their approach can be broadly summarized in three stages:

- estimation of the market value and volatility of a firm's assets:
- calculation of the distance to default which is an . index measure of default risk; and
- scaling of the distance to default to the actual ٠ probability of default using a default database.

The distance to default (DD) measure, representing a standardized distance from which a firm is above its default threshold, is defined by<sup>a</sup>

$$DD = \frac{\ln(V/D) + (\mu - 0.5\sigma^2)T}{\sigma\sqrt{T}}$$
 (2)

![](_page_0_Figure_14.jpeg)

Figure 1 Illustration of the traditional Merton approach to modeling default based on the value of the firm being below the face value of debt at maturity

The default probability would then be given by *pd* = *-(*−*DD)*. A key element of the approach is to recognize the model risk inherent in this approach and rather to estimate the default probability empirically from many years of default history (and the calculated DD variables). We therefore ask ourselves the following question: for a firm with a DD of 4.0 (say), how often have firms with the same DD defaulted historically? The answer is likely to be considerably higher than the theoretical result of *-(*−4*.*0*)* = 0*.*003%. This mapping of DD to actual default probability could be thought of as an empirical correction for the non-Gaussian behavior of firm value.

**CreditGrades Approach.** The aim of CreditGrades is rather similar to that of KMV except that the modeling framework [3] is rather simpler, in particular without using empirical data in order to map to an eventual default probability. In the Credit Grades approach, the default barrier is given by

$$LD = \overline{L}De^{\lambda Z - \lambda^2/2} \tag{3}$$

where *Z* is a standard normal variable, *D* is the "debt per share", *L* is an average recovery level, and *λ* creates an uncertainty in the default barrier. The level of the default barrier and the asset return are independent. Hence the main differences between the traditional Merton approach and CreditGrades is that the latter approach assumes that default can occur at any time when the asset process has dropped to a level of *LD*, whereas the Merton framework assumes *L* = 1 and *λ* = 0 and no default prior to the maturity of the debt. CreditGrades recommends values of *L* = 0*.*5 and *λ* = 0*.*3. A sensitivity analysis of these parameters should give the user a very clear understanding of the uncertainties inherent in estimating default probability.

# **Portfolio Models**

While default barrier models have proved very useful for assessing single-name default probability and supporting trading strategies such as capital structure arbitrage, arguably an even more significant development has been their application in credit portfolio models. The basic strength of the default barrier approach is to provide the transformation necessary to model default events *via* a multivariate normal distribution driven by asset correlations. The intuition of the approach makes it possible to add complexities such as credit migrations and stochastic recovery rates into the model.

### *Default Correlation*

Consider modeling the joint default probability of two entities. Using the standard definition of a correlation coefficient, we can write the joint default probability as

$$p_{AB} = p_A p_B + \rho_{AB} \sqrt{p_A (1 - p_A) p_B (1 - p_B)} \quad (4)$$

where *pA* and *pB* are the individual default probabilities and *ρAB* is the default correlation. Assuming, without loss of generality, that *pA* ≤ *pB* and since the joint default probability can be no greater than the smaller of the individual default probabilities, we have

$$\rho_{AB} = \frac{p_{AB} - p_A p_B}{\sqrt{p_A (1 - p_A) p_B (1 - p_B)}}\n$$

$$\n\leq \frac{p_A - p_A p_B}{\sqrt{p_A (1 - p_A) p_B (1 - p_B)}}\n$$

$$\n= \sqrt{\frac{p_A (1 - p_B)}{p_B (1 - p_A)}}\n$$
(5)

This shows that the default correlation cannot be +1 (or indeed *via* a similar argument −1) unless the individual default probabilities are equal. There is therefore a maximum (and minimum) possible default correlation that changes with the underlying default probabilities. This suggests a need for more economic structure to model joint default probability.

#### *Default Barrier Approach*

Suppose that we write default as being driven by a standard Gaussian variable *Xi* being below a certain level *k* = *-*<sup>−</sup><sup>1</sup>*(p)*. We can interpret *X* as being an asset return in the classic Merton sense, with *k* being a default barrier. Now joint default probability is readily defined *via* a bivariate Gaussian distribution:

$$p_{AB} = \Phi_2 \left( \Phi^{-1}(p_A), \Phi^{-1}(p_B); \lambda_{AB} \right) \tag{6}$$

where *-*<sup>2</sup> is a cumulative bivariate cumulative distribution function and *λAB* is the "asset correlation".

![](_page_2_Figure_1.jpeg)

**Figure 2** Illustration of the mapping of default and credit migrations thresholds as used in the CreditMetrics approach. The default region is also shown with additional thresholds corresponding to different recovery values with *R*<sup>1</sup> *< R*<sup>2</sup> *< R*<sup>3</sup> *< R*<sup>4</sup>

Multiple names can be handled *via* a multivariate Gaussian distributionb with Monte Carlo simulation or various factor-type approaches used for the calculation of multiple defaults and/or losses.

Although there is a clear link between this simple approach and the multidimensional Merton model, we have ignored the full path of the asset value process and linked default to just a single variable *Xi*. A more rigorous time-dependent approach can be found in [7], which is much more complex and time consuming to implement. In practice, the oneperiod approach is rather similar to the full approach for relative small default probabilities.

#### *CreditMetrics*

CreditMetrics [6], first published in 1997, is a credit portfolio model based on the multivariate normal default barrier approach. This framework assumes a default barrier as described above and also considers the mapping of credit migration probabilities onto the same normal variable. A downgrade can therefore be seen as a less extreme move not causing default. In addition to credit migrations, one can also superimpose different recovery rates onto the same mapping so that there is more than one default barrier with lower barriers representing more severe default and therefore a lower recovery value; for example, see [1]. An illustration of the mapping is shown in Figure 2.

#### *Regulatory Approaches*

**Basel 2.** A key strength of the above framework is that defaults, credit migrations, and recovery rates can be modeled within a single intuitive framework with correlation parameters estimated from equity data. While other credit portfolio modeling frameworks have been proposed, the CreditMetrics style approach has been the most popular. Indeed, the Basel 2 formula [4] can be seen as arising from a simplified version of this approach with the following assumptions:

- no credit migration or stochastic recovery and
- infinitely large homogeneous portfolio.

**Rating Agency Approaches to Structured Finance.** With the massive growth of the collateralized debt obligation (CDO) came a need for rating agencies (*see* **Structured Finance Rating Methodologies**) to model the risk inherent in a CDO structure with a view to assigning a rating to some or all of the tranches of the CDO capital structure. Rating a tranche of a CDO is essentially the same problem as estimating capital on a credit portfolio and hence it may come as no surprise that the rating agencies models were based on default barrier approaches. The rating agencies models can be thought of as therefore heavily following the CreditMetrics approach. The credit crisis of 2007 brought very swift criticism of rating agency modeling approaches to rating all types of structure finance and CDO structures. This was related largely to poor assessment of the model parameters (specifically rather optimistic default probabilities and correlation assumptions) rather than a failure of the model itself.

#### *CDO Pricing*

A final and perhaps most exciting (although not for necessarily positive reasons) application of the default barrier approach is in the pricing of synthetic CDO structures. The market standard approach for pricing CDOs follows the work of Li [11] (*see* **Gaussian Copula Model**) who models time of default in a multivariate normal framework:

$$\Pr(T_A < 1, T_B < 1)$$
  
=  $\Phi_2 \left( \Phi^{-1}(F_A(T_A)), \Phi^{-1}(F_B(T_B)); \gamma \right)$  (7)

where *FA* and *FB* are the distribution functions for the survival times *TB* and *TB* and *γ* is a correlation parameter. At first glance, although this uses the same multivariate distribution, or copulac, this approach initially does not seem to be a default barrier model. However, as noted in [11], for a single period, the approaches are identical. Furthermore, as shown by Laurent and Gregory [5], the pricing of a synthetic CDO requires just the knowledge of loss distributions at each date up to the contractual maturity date (and not any further dynamical information). Hence, we can think of the Li approach as being again similard to the traditional framework of credit portfolio modeling, following CreditMetrics and ultimately inspired by the Merton approach to modeling default *via* the hitting time of a barrier. The recent strong criticism linking the model in [11] to the credit crisis [13] does not fairly consider the rather na¨ıve calibration use of the model that has caused many of the problems in structured finance.

# **Conclusions**

We have described the range of default barrier models used in default probability estimation, capital structure trading, credit portfolio management, regulatory capital calculations, and pricing and rating CDO products. The intuition that default can be modeled as a hitting of a barrier has been crucial to the rapid development of credit risk models. For credit portfolio risk in particular, the default barrier approach has been key to the development of models for many different purposes, driven from the same underlying structural framework. Given that some applications of the approach (most notably rating agency models and CDO pricing) have received large criticism, it is worth pointing out that one can only discredit the entire framework (including any multidimensional Merton approach) or realize that it is a misuse of the model rather than the model itself that lies at the heart of the problems.

# **End Notes**

a*.* In the proprietary Moody's KMV implementation, the default point is not the face value of debt but the current book value of their liabilities. This is often computed as short-term liabilities plus half long-term liabilities.

b*.* It should be noted that alternatives to a Gaussian distribution (e.g., student-*t*) can and have been considered although the Gaussian approach has remained most common.

c*.* This approach has become known as the *Gaussian copula model* which is perhaps confusing since the key point of the approach is the representation of the joint distribution of default times and not the choice of a Gaussian copula or multivariate distribution.

d*.* Li was at the time working at JP Morgan and so this is not surprising.

# **References**

- [1] Arvanitis, A., Browne, C. Gregory, J. & Martin, R. (1998). A credit risk toolbox, *Risk* December, 50–55.
- [2] Black, F. & Cox, J. (1976). Valuing corporate securities: some effects of bond indenture provisions, *Journal of Finance* **31**, 351–367.
- [3] Finger, C., Finkelstein, V., Pan, G., Lardy, J.P. & Tiemey, J. (2002). *Credit-Grades Technical Document*, RiskMetrics Group.
- [4] Gordy, M. (2003). A risk-factor model foundation for ratings-based bank capital rules, *Journal of Financial Intermediation* **12**, 199–232.

- [5] Gregory, J. & Laurent, J.-P. (2005). Basket default swaps, CDO's and factor copulas, *Journal of Risk* **7**(4), 103–122.
- [6] Gupton, G.M., Finger, C.C. & Bhatia, M. (1997). *CreditMetrics Technical Document*, Morgan Guaranty Trust Company, New York.
- [7] Hull, J., Predescu, M. & White, A. (2005). *The Valuation of Correlation-Dependent Credit Derivatives Using a Structural Model*, working paper, available at SSRN: http://ssrn.com/abstract=686481
- [8] Kealhofer, S. (2003). Quantifying default risk I: default prediction, *Financial Analysts Journal* **59**(1), 33–44.
- [9] Kealhofer, S. & Kurbat, M. (2002). *The Default Prediction Power of the Merton Approach, Relative to Debt Ratings and Accounting Variables*, KMV LLC, Mimeo.

- [10] Leland, H. (1994). Corporate debt value, bond covenants, and optimal capital structure, *Journal of Finance* **49**, 1213–1252.
- [11] Li, D.X. (2000). On default correlation: a Copula approach, *Journal of Fixed Income* **9**, 43–54.
- [12] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [13] Wired Magazine: 17.03 (2009). *Recipe for Disaster: The Formula That Killed Wall Street*.

# **Related Articles**

**Credit Risk**; **Structural Default Risk Models**.

JON GREGORY
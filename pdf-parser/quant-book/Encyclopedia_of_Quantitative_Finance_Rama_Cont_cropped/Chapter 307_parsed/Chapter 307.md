# **Operational Risk**

A basic ingredient of the Basel II guidelines of the Basel Committee on Banking Supervision is the introduction of the new risk class of operational risk (OR). OR is the risk of loss resulting from inadequate or failed internal processes, people, and systems or from external events. This definition includes legal risk, but excludes strategic and reputational risk. OR complements the more traditional risk classes of market risk (MR) and credit risk (CR), but it is more concerned with the overall quality assurance of banking operations, and as such borrows methodology more from such fields as reliability engineering and insurance mathematics. For the latter, see, for instance, McNeil et al. [17, Chapter 10] and Panjer [20]. The capital change for OR may range from 10 to 20%, say, of overall risk capital and for some banks top the charge for MR. Under the so-called Pillar I of Basel II, banks can choose among three increasingly quantitative approaches for the measurement of OR. The first two, namely, the basic indicator (BIA) and the standardized (SA) approach, yield volume-based measures for OR: risk capital is charged in proportion to gross income, either companywide in the case of the BIA or averaged across a number (typically 7) of business lines (BL) for the SA.

Larger international banks have to use the socalled advanced measurement approach (AMA), which, upon introduction in January 2008, is mainly referred to as the *loss distribution approach* (LDA). Under the Basel II setup, banks using the LDA have to prove to the local regulator that they have the necessary quantitative risk management environment. Further, insurance of OR losses up to 20% is allowed. Capital estimates are to be based on internal, external, as well as expert opinion data. Essentially, banks are free to choose their own analytic approach for the calculation of an LDA-based capital charge for OR. In the second section, we review some of the approaches used. The third section contains some comments on further work.

### The LDA Approach

Basel II prescribes the use of Value-at-Risk as a risk measure for OR, with a confidence level of 99.9% and a measurement horizon of 1 year. Hence,

denoting the total OR loss for the coming year  $T$  by  $L_T$ , the risk capital charge becomes

$$RC_{OR}^{T} = VaR_{99.9\%}^{T} (L_{T}) = F_{L_{T}}^{\leftarrow}(0.999) \qquad (1)$$

where  $F_{L_{T}}^{\leftarrow}$  denotes the generalized inverse of the distribution function (df) of the total loss random variable  $L_T$ . This function is also referred to as the *quantile function*. The variety of LDA models used by the industry now stems from the granularity of the stochastic frequency-severity models of  $L_T$ implemented, as well as from the extreme tail-fitting of  $F_{L_T}$  in order to estimate the 99.9% quantile.

For internal data of banks, the basic structure of the OR data warehouse is as follows:

$$\mathcal{X} = \{X_k^{T-i,b,r} : i = 1, \dots, n, \quad b = 1, \dots, B,$$
$$r = 1, \dots, R, \quad k = 1, \dots, N^{T-i,b,r} \} \quad (2)$$

where

i stands for the number of past observation years;  $\mathcal{B}$ stands for the different BL, typically  $B = 8$ ;  $R$ denotes the different risk types (RT); often  $R = 7$ :  $N$ (frequency) denotes the number of losses in year  $T - i$ , BL b, and RT r; and (severities) denotes the successive loss amounts  $X$ in these classes.

Finally, banks are allowed to cap the loss amounts recorded from below, for example, losses are only recorded above USD 20 000. As a consequence, the loss random variable (rv) to be modeled becomes

$$L_T = \sum_{b=1}^{B} \sum_{r=1}^{R} \sum_{k=1}^{N^{T,b,\ell}} X_{k,+}^{T,b,r} \tag{3}$$

where the " $+$ " denotes the above capping: a dauntful task indeed! It should be remarked at this point that the calculation of a capital charge for OR is methodologically very different from that for MR and CR. For MR, the confidence level is 99% and the modeling horizon is 10 days; this becomes 99.9% and 1 year for CR. Besides this, the underlying processes are totally different; for OR only losses are to be modeled and obviously, a bank does not "take positions" in OR. A consequence of this is that, in our opinion, regulators have moved a bit too fast up the hill of the ultimate risk management goal: a unified quantitative capital charge formula across all risk classes. We firmly believe that, before reaching this ultimate goal, we have to walk up and down the quantitative risk management hill a couple of times. The final satisfaction with the results obtained may crucially depend on this.

What have we learned so far from the various quantitative impact studies (QIS) presented by the regulators (see [18] and [8])? First of all, severity data are very heavy-tailed. Moscadelli [18] even reports infinite-mean models for several of the BLaggregated loss data. Data are furthermore very skewed. Finally, though frequency is no doubt important, it is mainly severity ("the one claim causes ruin"-type of paradigm) that calls the tune. In [18], extreme value theory (EVT) is used for the highquantile estimation of  $F_{L_r}^{\leftarrow}$  (0.999). On the other hand, Dutta and Perry [8] question the use of EVT, as the final capital charge may be very unstable with respect to the starting values of the resulting estimation procedure. See  $[5]$  and  $[19]$  for more information on this. Dutta and Perry [8] champion the use of the so-called  $g$ -and- $h$  df as a flexible family of loss severity models for OR data. An rv  $X$  has a  $g$ -and- $h$  df if for  $Z \sim N(0, 1)$ , and  $a, b, g, h \in \mathbb{R}$ ,

$$X = a + b \frac{e^{gZ} - 1}{g} e^{1/2hZ^2} \tag{4}$$

For a comparison of EVT versus  $g$ -and- $h$  based estimates of the OR capital charge, see [7], [6], and [15]. The first two references explain the methodological difficulties that would be present when using an EVT-based analysis for real  $g$ -and- $h$  data, whereas the latter reference, based on the industry OR data, claims that EVT-based risk capital calculations work well till a confidence level of about 95%, whereas for higher confidence levels the  $g$ -and- $h$  approach seems to deliver more reliable (acceptable) capital values. In our view, the jury is still out. For readers interested in a complete discussion of OR modeling in a large international bank, see  $[1]$ ; in this article, various modeling issues that we had to omit here because of space constraint have been touched upon. For early contributions to the LDA, see for instance [2, 13, 14].

So far, we have only briefly mentioned the stochastic modeling of the internal OR loss data. The regulators require a combination of internal with external and expert opinion data. Several companies are providing industrywide OR loss data on which banks can calibrate their internal loss distribution curves. At the moment, it is still early to comment on the validity and the ultimate effect of this. Furthermore, in the realm of OR, expert opinion is called for; it may be borne in mind that we are mainly estimating rare-frequency, high-severity events. As a consequence, a Bayesian approach presents itself. Within the (actuarial) realm of credibility theory, such an approach has for instance been worked out by Bühlmann et al. [4]. For a textbook treatment on credibility theory and its link to empirical Bayes, see [3]. Shevchenko and Wüthrich [21] and Lambrigger *et al.* [16] use the concept of conjugate priors within a Bayesian framework.

#### **Further Work**

The brief discussion above hopefully highlights some of the key issues/problems for the Pillar I quantitative modeling of OR. Our main concern is that for such extremely heavy-tailed data, VaR-based risk management is, at best breaking new ground and at worst not really applicable. This brings us to some of the recent research on using VaR as a one-fit-allsize risk management tool. For instance, many banks aggregate data BL-wise, estimate the resulting VaRs,  $\widehat{\text{VaR}}_1, \ldots, \widehat{\text{VaR}}_B$ , and add these to obtain

$$\text{VaR}_{+} = \sum_{b=1}^{B} \widehat{\text{VaR}}_{b}$$
 (5)

Then they have to come up with a so-called diversification-based capital reduction argument to yield

$$RC_{\mathbf{OR}}^{T} < VaR_{+} \tag{6}$$

A more careful look at this issue shows that one is in danger of running head on into the wall of potential nonsubadditivity of the VaR, that is,

$$\text{VaR} (L_1 + L_2) > \text{VaR} (L_1) + \text{VaR} (L_2) \quad (7)$$

in cases important for OR practice; see [19] and the references therein for a discussion on this.

A related mathematical problem we would like to point out at this point is the following: suppose  $X_1, \ldots, X_d$  are d one-period risks,  $\Psi: \mathbb{R}^d \to \mathbb{R}$ a function corresponding to a financial position  $\Psi(X_1,\ldots,X_d)$ , and  $\rho$  a risk measure so that we want to calculate (estimate)

$$\rho\left(\Psi\left(X_{1},\ldots,X_{d}\right)\right) \tag{8}$$

Full determination of equation (8) requires the knowledge of the joint df *FX*1*,...,Xd* which in many cases is not known. As a consequence, only upper and lower bounds on equation (8) can be calculated. This problem is dealt with in [9–11]. In [12], the authors discuss the difference between BL-wide aggregation of the VaR-estimates versus RT-wide aggregation. The final difference very much depends on the specific stochastic properties of the frequencyseverity models for each cell of the OR loss data matrix.

## **Conclusion**

The Pillar I based quantitative modeling of OR data still has numerous problems: lack of historical data, extreme heavy-tailedness leading to possible superadditivity of the VaR and hence, the questioning of diversification effects based on the VaR, and finally, the overall statistical uncertainty in the modeling of extremes for data of OR type. Before a sufficiently reliable method for OR capital estimation can be found, much more data-oriented work is needed.

## **References**

- [1] Aue, F. & Kalkbrener, M. (2006). LDA at work: Deutsche Bank's approach to quantifying operational risk, *Journal of Operational Risk* **1**(4), 49–93.
- [2] Baud, N., Frachot, A. & Roncalli, T. (2003). *How to Avoid Over-Estimating Capital Charge for Operational Risk*, OpRisk & Compliance.
- [3] Buhlmann, H. & Gisler, A. (2005). ¨ *A Course in Credibility Theory and its Applications*, Springer–Verlag, Berlin.
- [4] Buhlmann, H., Shevchenko, P.V. & W ¨ uthrich, M.V. ¨ (2007). A "toy" model for operational risk quantification using credibility theory, *Journal of Operational Risk* **2**(1), 3–19.
- [5] Chavez-Demoulin, V., Embrechts, P. & Neslehov ˇ a, J. ´ (2006). Quantitative models for operational risk: extremes, dependence and aggregation, *Journal of Banking and Finance* **30**, 2635–2658.
- [6] Degen, M. & Embrechts, P. (2008). EVT–based estimation of risk capital and convergence of high quantiles, *Advances of Applied Probability* **40**(3), 696–715.
- [7] Degen, M., Embrechts, P. & Lambrigger, D.D. (2007). The quantitative modelling of operational risk: between

*g*–and–*h* and EVT, *ASTIN Bulletin* **37**(2), 265–291.

- [8] Dutta, K. & Perry, J. (2006). *A Tale of Tails: An Empirical Analysis of Loss Distribution Models for Estimating Operational Risk Capital*, Federal Reserve Bank of Boston, Working Paper No. 6–13.
- [9] Embrechts, P. & Puccetti, G. (2006). Bounds for functions of dependent risks, *Finance and Stochastics* **10**, 341–352.
- [10] Embrechts, P. & Puccetti, G. (2006). Bounds for functions of multivariate risks, *Journal of Multivariate Analysis* **97**(2), 526–547.
- [11] Embrechts, P. & Puccetti, G. (2008). Aggregating risk capital, with an application to operational risk, *Geneva Risk and Insurance Review* **31**(2), 71–90.
- [12] Embrechts, P. & Puccetti, G. (2008). Aggregating operational risk across matrix structured loss data, *Journal of Operational Risk* **3**(2), 29–44.
- [13] Frachot, A., Moudoulaud, O. & Roncalli, T. (2003). Loss distribution approach in practice, in Chapter 15 of *The Basel Handbook: A Guide for Financial Practitioners*, M. Ong, ed., Risk Books.
- [14] Frachot, A., Roncalli, T. & Salomon, E. (2004). *Correlation and Diversification Effects in Operational Risk Modelling*, OpRisk & Compliance.
- [15] Jobst, A.A. (2007). Operational risk: the sting is still in the tail but the poison depends on the dose, *Journal of Operational Risk* **2**(2), 3–59.
- [16] Lambrigger, D.D., Shevchenko, P.V. & Wuthrich, M.V. ¨ (2007). The quantification of operational risk using internal data, relevant external data and expert opinion, *Journal of Operational Risk* **2**(3), 3–27.
- [17] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management: Concepts, Techniques, Tools*, Princeton University Press, Princeton.
- [18] Moscadelli, M. (2004). *The Modelling of Operational Risk: Experience with the Analysis of the Data Collected by the Basel Committee*. Temi di discussione, Banca d'Italia.
- [19] Neslehov ˇ a, J., Embrechts, P. & ´ Chavez-Demoulin, V. (2006). Infinite-mean models and the LDA for operational risk, *Journal of Operational Risk* **1**(1), 3–25.
- [20] Panjer, H.H. (2006). *Operational Risk*, John Wiley & Sons, Hoboken, NJ.
- [21] Shevchenko, P.V. & Wuthrich, M.V. (2006). The struc- ¨ tural modeling of operational risk via Bayesian inference, *Journal of Operational Risk* **1**(3), 3–26.

VALERIE ´ CHAVEZ-DEMOULIN & PAUL EMBRECHTS
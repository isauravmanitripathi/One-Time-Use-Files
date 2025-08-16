# **Internal-ratings-based Approach**

Within the new Basel capital rules for banks (*see* **Regulatory Capital**), the internal-ratings-based approach (IRBA) represents perhaps the most important innovation for regulatory minimum capital requirements. For the first time, subject to supervisory approval, banks are allowed to use their own risk assessments of credit exposures in order to determine the capital to be held against them. Within the IRBA, banks estimate the riskiness of each exposure on a stand-alone basis. The risk estimates serve as input for a supervisory credit risk model (implicitly given by risk weight functions) that provides a value for capital that is deemed sufficient to cover against the credit risk of the exposure, given the assumed portfolio diversification. In order to obtain supervisory approval for the IRBA, banks must apply for IRBA and fulfill a set of minimum requirements. Until approval is granted for the entire book or specific portfolios, banks must apply the simpler and less risk-sensitive standardized approach for credit risk, where minimum capital requirements are determined in dependence on asset class (sovereign, bank, corporate, or retail exposure) only and, if applicable, ratings by external credit assessment agencies like rating agencies or credit export agencies.

# **The Conception of Internal Rating Systems in Basel II**

Bank internal rating systems are, in the most general sense, risk assessment procedures, which are used for the assignment of internally defined borrower and exposure categories. A rating system is based on a set of predefined criteria to be evaluated for each borrower or exposure subject to the system, and result in a final "score" or "rating grade" for the borrower or exposure. The choice and weighting of the criteria can be manifold; there are no rules or guidance on which criteria to include or exclude. The main requirement on IRBA systems is that their rating grades or scores do indeed discriminate borrowers according to credit default risk.

In practice, rating systems are often designed as purely or partly statistical tools, for example, by identifying criteria (typically financial ratios) with good discriminatory power and combining them by means of statistical regression or other mathematical methods.

However, in order to use such tools, there must be sufficient historical data—both on defaulted and surviving borrowers and exposures— for determining the discrimination criteria and calibrating their weightings. In practice, obtaining such data often proves to be more difficult than the statistical analysis as such, either because historically borrower and exposure characteristics were not stored in a readily usable manner, or simply because for some portfolios there is not sufficient default data. In general, rating systems may include a set of quantitative and some qualitative criteria. The weighting of these criteria may also be determined by expert opinion rather than by statistical tools. In the extreme, for example, in international project finance where certain criteria are deal breakers for loan arrangements (i.e., the existence of sovereign risk coverage *via* export insurance for projects in regions with high political risk), there might be no predetermined weighting scheme at all.

Notions appear to be not entirely uniform in practice. Often, but not always, the notion of a "scoring system" or a "score card" is used for a purely statistical rating system or the statistical part of a mixed quantitative and qualitative rating system. Moreover, the notion of scores tends to be more often used for retail and small business portfolios, while for corporate, bank, and sovereign portfolios, the literature tends to speak of rating systems. From an IRBA perspective, there are no conceptual differences between these notions: they all depict different forms of IRBA systems. Likewise, there is no IRBA requirement for the number of rating systems a bank should apply. Usually, one would expect different systems for retail, small businesses and self-employed borrowers, corporates, specialized lending portfolios, sovereigns, and banks. Many of these asset classes might again see different rating systems, depending on, for example, product type (very common for retail portfolios, but not constrained to them) or sales volume and region (both common for corporate portfolios), because the different borrower and exposure categories might call for different sets of rating criteria. Within a large, internationally active and well-diversified bank, one might expect to see a large number of different rating systems.

## **IRBA Risk Parameters**

Credit risk per rating grade is quantified by probabilities of default (PDs), which give the probabilities of borrowers to default on their obligations, with regard to the Basel default definition, within 1 year's time. The PD per rating grade is usually estimated by the use of bank internal historical default data, which may be supplemented by external default data. A specific problem within the IRBA comes from the fact that not all institutions have readily available default data according to the Basel definition. In this case, adjustments to the estimates must be made.

PDs may be estimated just for the next year (point in time (PIT)) or as long term average PDs (through the cycle (TTC)). PIT estimates take into account the current state of the economy—as a consequence, PDs per rating grade might change over time—while TTC estimates do not. The Basel Accord seems to implicate TTC estimates. Nonetheless, many supervisors might be prepared to accept PD estimates that are more of PIT type because eliminating all cyclical effects from rating systems and PD estimates might be difficult to afford in practice.

In the Basel sense, an IRBA rating system contains two additional dimensions: an exposure at default (EAD) dimension, assessing the expected exposure at the point in time when the borrower defaults, and a loss given default (LGD) dimension, measuring the expected percentage of exposure that is lost in case a borrower defaults. The EAD dimension is mainly driven by product characteristics, for example, how easily lines can be drawn by the borrower or reduced by the bank prior to default, while the LGD dimension is heavily dependent on collateral, guarantees, and other risk mitigants. Here again, Basel notions slightly differ from literature and practice: in industry, the notion of a rating system often refers to the PD dimension only, while for Basel it includes all three dimensions. Within the IRBA, banks must provide a PD, LGD, and EAD for all their exposures. While the PD must always be estimated by the bank itself, banks can choose whether they want to use supervisory LGD and EAD estimates for given product and collateral types (thus applying the so-called foundation IRBA) or whether they want to estimate these values themselves, too (thus using the so-called advanced IRBA).

## **The Basel II Risk Weight Functions**

In order to assess the overall risk of a bank portfolio, credit portfolio risk models have to evaluate the portfolio composition and its diversification. Within the Basel II IRBA, banks are not allowed to use their own credit portfolio risk models and diversification estimates for minimum regulatory capital ratios. Rather, they must input the risk parameters PD, LGD, and EAD into a supervisory credit portfolio risk model. This model can be roughly described as Vasicek's [6] multivariate extension of Merton's [5] model of the default of a firm. In statistical terms, the model could be characterized as a one-factor probit model where the events to be predicted are the borrowers' defaults and the single factor reflects the state of the global economy. Moreover, the Basel model assumes an infinitely granular portfolio, such that all idiosyncratic single name risk is diversified away. In this sense, the Basel model is an asymptotic single risk factor (ASRF) model. For further details of the model, see [1, 4].

The assumptions of a single risk factor and of infinite granularity lead to the following characteristics of the Basel credit risk model:

1. The capital charge per exposure can be described in closed form by risk weight functions (cf [3], paragraphs 272 and 273 for corporate, sovereign, and bank exposures and paragraphs 328, 329, and 330 for retail exposures). The specifications of the risk weight function for the different exposure classes can be derived from the following generic formula for the capital requirement K per dollar of exposure:

$$K = LGD \left[ N \left( \frac{G(PD)}{\sqrt{1 - R}} + G(0.999) \sqrt{\frac{R}{1 - R}} \right) - PD \right] \frac{1 + (M - 2.5) b}{1 - 1.5 b} \tag{1}$$

In this equation,

- the probability of default PD and the loss given default LGD are measured as decimals;
- the *maturity adjustment* b is given by *(*0*.*11852 − 0*.*05478 ln*(*PD*))*2;

- $\bullet$  N denotes the standard normal distribution function:
- G denotes the inverse standard normal distribution function:
- the effective maturity M was fixed at 1 year for retail exposures, and assumes values between  $0$  and  $5$  years for other exposures as described in detail in paragraph 320 of [3].

The risk weight functions for the different exposure classes differ mostly in the specification of the *asset correlation R*. For the retail mortgage exposure class,  $R$  was fixed at 15%. For revolving retail credit,  $R$  is 4%. In contrast, in the corporate, sovereign, and bank exposure classes, R depends on PD by

$$R = 0.12 \frac{1 - e^{-50 \text{ PD}}}{1 - e^{-50}} + 0.24 \left(1 - \frac{1 - e^{-50 \text{ PD}}}{1 - e^{-50}}\right)$$
(2)

and also for other retail exposures,  $R$  is given as a function of PD by

$$R = 0.03 \frac{1 - e^{-35 \text{ PD}}}{1 - e^{-35}} + 0.16 \left(1 - \frac{1 - e^{-35 \text{ PD}}}{1 - e^{-35}}\right)$$
(3)

2. The capital charge per exposure depends only on the risk parameters PD, LGD, and EAD of the exposure, but not on the portfolio composition. Thus, the capital charge for each exposure is exactly the same, no matter which portfolio it is added to (portfolio invariance). From a supervisory point of view, portfolio invariance was an important characteristic in developing the Basel risk weight functions, as it ensures computational simplicity and the preservation of a level playing field between well diversified and specialized banks. The capital charge for the entire portfolio is the sum of the capital charges for individual exposures. The downside of portfolio invariance is that the Basel formula cannot account for risk concentrations. If it did, the capital charge for an exposure would again have to depend on the portfolio to which it is added. If banks are concerned about concentration effects. or want to measure the diversification benefits of their portfolio, they need to develop their own, fully fledged credit risk models.

- The capital charge for each exposure, given its 3. risk parameters, depends on the correlation with the single systematic risk factor and the socalled confidence level. The confidence level for minimum capital requirements was set by the Basel Committee to be 99.9%. As a consequence, the probability that the bank will suffer losses from the credit portfolio that exceed the capital requirements should be of an order of magnitude like  $0.1\%$ . The correlations were estimated from supervisory data bases and are assumed to decrease with decreasing creditworthiness.
- The ASRF takes only the default event as 4. stochastic and treats the loss in case of default as deterministic. As in practice loss amounts are stochastic as well, and potentially correlated with the drivers of the default events, banks are supposed to take account of this effect in their LGD estimates, by estimating the downturn LGDs instead of average LGDs.
- 5. Lastly, the ASRF is a default mode (DM) model that only accounts for losses due to defaults within a given time horizon (1 year) but not for losses due to rating migrations and future losses after 1 year. This simplification does not comply with modern accounting practice. It was therefore adjusted by introducing the maturity adjustments, which can be seen as an extension of the model toward a marked-to-market (MtM) mode.

#### **Minimum Requirements**

In order to apply the IRBA, banks must have explicit approval from their supervisors. Approval is subject to a set of minimum requirements aimed to ensure the integrity of the rating model, rating process, and thus of the risk parameters and capital charges. The minimum requirements ([3], Part 2, Section III. H) hence assemble around the following themes:

Rating system design. As mentioned before, . there are no regulatory requirements with regard to the rating criteria. Rating grades must, in a sensible way, discriminate for credit risk, and the onus of proof is with the bank. Moreover, there must be at least seven rating grades for performing and one grade for nonperforming

exposures in the PD dimension. No minimum grade numbers are given for the LGD and EAD dimension. Also, there is no requirement of a common master scale across all rating systems, although many banks develop such a scale for internal risk management and communication purposes.

- *Rating system operations.* By this set of minimum requirements, banks are asked to ensure the integrity of the rating process. Most notably, the rating assignments must be independent from any business units gaining from credit approval (e.g., the sales department). Moreover, there should be no "cherry picking" between rated and nonrated exposures (the latter being treated in the less risk-sensitive standardized approach), although a temporary partial use of IRBA, coupled with a supervisory approved implementation (roll-out plan) for bankwide IRBA use, and a permanent partial use for insignificant portfolios are allowed. Another important aspect is the integration of the ratings into day-to-day credit processes, including IT systems and input data availability.
- *Corporate governance and oversight.* This set of criteria requires banks to embed their rating systems into the overall governance structure of the bank. Most notably, senior management is supposed to buy into the systems and formally approve for wide use within the bank, such that the systems become accepted risk management tools at all levels in the organization. Also, the role of internal audit in regular rating audits is defined.
- *Use of internal ratings.* Banks will only receive IRBA approval if they use their ratings for a wide range of bank internal applications. Examples include credit approval, limit systems, risksensitive pricing and loss provisioning. Rating systems solely developed for regulatory purposes will not be recognized, as only the deep rooting into day-to-day credit risk management actions will ensure their integrity.
- *Risk quantification.* Banks need to quantify the risk parameters PD, LGD, and EAD, based on their rating grades and on the Basel default and loss definitions ([3], paragraphs 452, 453, and 460). In doing so, they should employ a variety of data sources: preferentially internal data, but

enhanced with external data sources and expert judgment if needed.

- *Validation of internal estimates.* The PD, LGD, and EAD estimates must be validated against actually observed default rates and losses. Owing to relatively short time series for the latter, validation remains one of the more difficult issues within the IRBA. For available statistical techniques see, for example, [2]. Where statistical validation is not reliable, banks should use more qualitative validation techniques, like ensuring good rating process governance, integrity of the input data, and so on.
- *Disclosure requirements.* Banks that use the IRBA must base their capital and risk disclosure requirements (the Third Pillar of Basel II) on their IRBA figures.

In practice, compliance with the minimum requirements often seems to prove much more difficult and costly than the development of the rating systems as such. The most difficult issues seem to be data availability, IT system implementation, and data feed, the actual rating of entire portfolios, which often require large amounts of data for all exposures to be fed into the systems (in the worst case manually, as often data not consistent with the rating criteria have been stored in the past) and, connected to this, the buy-in of senior management and the entire credit business into the more risk-sensitive and more transparent IRBA.

# **Implications for the Bank Internal Use of IRBA Figures**

Risk quantification *via* IRBA can be of great use for the bank internal credit risk measurement and management. However, there are some limitations. The most important of these is surely that due to the asymptotic single risk factor model, the IRBA provides no measure of risk concentrations, be they single name, industry, or regional concentrations. If banks are concerned about concentration effects or—as the other side of the same coin—want to measure the diversification benefits of their portfolio, they need to go further and develop their own, fullfledged credit risk models with more than one risk factor and their own correlation estimates. Likewise, the asymptotic assumption needs to be given up in order to capture idiosyncratic single name risk.

The most significant benefit of the IRBA for bank internal risk management lies in the standardized assessment and measurement of stand-alone borrower and exposure credit risk. Credit risk becomes much more transparent within the organization, and there is "one common currency" for risk, expressed by the risk parameters PD, LGD, and EAD and the regulatory capital charges based on them.

## **References**

- [1] BCBS (2004). *An Explanatory Note on the Basel II IRB Risk Weight Functions*. Basel Committee of Banking Supervision.
- [2] BCBS (2005). *Studies on the Validation of Internal Rating Systems*. Basel Committee of Banking Supervision, Working Paper No. 14.
- [3] BCBS (2006). *International Convergence of Capital Measurement and Capital Standards. A Revised Framework,*

*Comprehensive Version*. Basel Committee of Banking Supervision.

- [4] Gordy, M. (2003). A risk-factor model foundation for ratings-based bank capital rules, *Journal of Financial Intermediation* **12**(3), 199–232.
- [5] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**(2), 449–470.
- [6] Vasicek, O.A. (2002). The distribution of loan portfolio value, *Risk* **15**, 160–162.

### **Related Articles**

**Credit Rating**; **Credit Risk**; **Credit Scoring**; **Economic Capital**; **Exposure to Default and Loss Given Default**; **Large Pool Approximations**; **Regulatory Capital**.

KATJA PLUTO & DIRK TASCHE
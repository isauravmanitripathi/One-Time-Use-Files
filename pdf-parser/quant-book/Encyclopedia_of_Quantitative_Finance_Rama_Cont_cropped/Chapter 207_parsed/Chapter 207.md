# **Modeling Correlation of Structured Instruments in a Portfolio Setting**

Credit events are correlated. Corporate or retail loan portfolios can exhibit wide swings in losses as economic factors common to the underlying entities drive defaults or deterioration in credit quality. Though challenging, the modeling and data issues related to single-name credit instruments are well understood [9, 10]. However, the correlation of structured instruments remains much more complicated and less understood. Traditional approaches to modeling economic capital, credit-VaR (Value-at-Risk), or structured instruments whose underlying collateral is composed of structured instruments treat structured instruments as a single-name credit instrument (i.e., a loan-equivalent).a Though tractable, the loan-equivalent approach requires appropriate parameterization to achieve a reasonable description of the cross-correlation between the structured instrument and the rest of the portfolio. We address this challenge by calibrating the loanequivalent correlation parameters to the dynamics observed in a granular model of the structured instrument.

In the granular model, the underlying reference entities associated with the collateral pool are used to simulate collateral losses, which are translated to structured instrument loss using its subordination level. For ease of exposition, we assume passthrough waterfalls throughout the article; the waterfall structure and subordination level are completely determined by attachment and detachment points. The structured instrument is said to be in distress if it incurs a loss. Simulated losses are used to calculate a probability of distress and loss given distress for each structured instrument and a joint probability of distress (JPD) for the structured instrument and other instruments in the portfolio. The JPD and the individual probabilities of distress are then used to back out an implied "asset return" correlation associated with the structures' loan-equivalent reference entities (henceforth, *the loan-equivalent correlation*). By taking the probability of distress as the loan-equivalent probability of default (PD), the loss given distress as the loan-equivalent loss given default, and the deal maturity as the loan-equivalent maturity the parameterization of the loan-equivalent is complete.

In addition to the benefits of using loanequivalents in a portfolio setting, the simplicity associated with loan-equivalent correlations serves as a useful summary statistic for understanding portfolio-referent risk characteristics. For example, when the collateral pool is parameterized under a wide range of values, the resulting correlation of the structure instrument with the rest of the portfolio is far higher than that of the underlying collateral pool or for other classes of single-name instruments, such as corporate exposures. This is because the idiosyncratic shocks in a collateral pool offset one another, and the systematic portion is left to "run the show". Moreover, loan-equivalent correlations between two subordinated tranches can be substantially lower than their senior counterparts. The higher correlation exhibited between two credit instruments in the tail region of the loss distribution (the loss region of the collateral pool where a senior tranche enters distress) drives the difference. This is because a senior tranche distress is most likely driven by systematic shock, which makes it more likely that it will be accompanied by a distress in the other senior tranche.

Correlation among CDOs can also stem from the overlap in reference entities associated with their collateral pools. Although it is intuitive that loan-equivalent correlations increase with the degree of overlap, the effect is stronger for more junior tranches. This finding follows from the junior tranches' susceptibility to idiosyncratic noise. With a higher degree of overlap, the tranches share more of the idiosyncratic shocks.

Recent literature on structured instruments' correlation primarily addresses correlations between collateral pool reference entities and their effect on tranche pricing. For example, Agca and Islam [1] examines the impact of correlation increase among underlying assets on the value of a CDO equity tranche, and shows that CDO equity can be short on correlation. The normal copula model, studied in detail in [4], has become the industry standard for pricing structured instruments and often results in a market price-implied correlation smile. Several papers address this phenomenon; Moosbrucker [5] explains it using variance-gamma distributions. This article, however, focuses on the

![](_page_1_Figure_1.jpeg)

**Figure 1** ABS probability of distress changing with subordination for collateral parameters: *R*<sup>2</sup> = 10%, *LGD* = 70%, and collateral *PD* ranging from 10 basis points to 22%

correlation structure between a structured instrument and other instruments in the portfolio. This structured instrument correlation is a function of the correlation of the underlying collateral instruments among themselves and with other instruments in the portfolio, as well as of the deal's waterfall structure and the instrument's subordination level. Coval *et al.* [2] show that, similar to economic catastrophe bonds, structured instruments are highly correlated with the market, but offer far less compensation than economic catastrophe bonds. The authors suggest in [3] that this lower compensation occurs because rating agencies base their structured instrument ratings on distress probability and expected loss, ignoring the high correlation with the market.

### **Modeling the Correlation of Two ABSs**

Consider an asset-backed security (ABS) with a homogeneous collateral pool (e.g., similar risk California auto-loans). In a homogeneous pool, we can model the systematic portion of reference entity *i*'s asset return process (*ri*) using a single factor (*Z*) with a common factor loading (*R*):

$$r_i = R \cdot Z + \sqrt{1 - R^2} \cdot \varepsilon_i \tag{1}$$

Henceforth, we use the square form of the factor loading, *R*2, because of its interpretation as the proportion of asset return variation explained by the common factor *Z*. The single factor *Z* and the idiosyncratic portion *εi* are standard Brownian motion processes and, therefore, so is the asset return. A default occurs when the asset return process drops below a default threshold (DT), which happens with probability PD. These PDs and other parameters for the underlying instruments in the collateral pool are publicly available.b

In analyzing ABS characteristics, we made simplifying assumptions. We assumed a single period, and the analysis abstracted from subtleties such as reinvestment, collateralization, or wrapping. Collateral pools were composed of instruments with Loss Given Default (LGD) = 70% and reference entities with *R*<sup>2</sup> = 10%. Each deal consisted of seven ABSs at different subordination levels. Deal maturity was set at 1 year. All deals were simulated 100 000 times in Moody's KMV's RiskFrontier to obtain the ABSs' probabilities of distress and losses given distress, as well as to account for collateral pool correlations properly. See [8] for the methodology used in RiskFrontier.

Figure 1 demonstrates how the ABS 1-year distress probability changes with the subordination level for collateral pools; PD values range from as low as 10 basis points to as high as 22%, covering a

![](_page_2_Figure_1.jpeg)

Figure 2 ABS loan-equivalent reference entity's "asset return" correlation for collateral parameters:  $R^2 = 10\%$ .  $LGD = 70\%$ , and collateral PD ranging from 10 basis points to 22%

variety of instruments in varying economic environments—from prime loans in boom times to subprime mortgages during downturns. As expected, the ABS probability of distress is decreasing in the subordination level. Moreover, it appears that the distress probability curve starts out concave, switches. and then becomes convex. This convexity switch occurs at the maximum point of the bell-shaped collateral loss distribution function. Higher collateral PD pushes this maximum point to higher loss points.

To better understand the correlation structure of these ABSs, we compute the loan-equivalent reference entity's  $R^2$  for each deal. To this end, the simulation holds two similar copies of each ABS. Collateral pools for the two copies contain statistically similar instruments (but not the same instruments, i.e., different idiosyncratic shocks). The empirical JPD  $(JPD_{\text{sim}})$  of the similar ABS pairs is calculated from the simulation results. Using a normal copula, we choose the loan-equivalent reference entity's "asset return" correlation  $\rho_{12}^A$ , which results in the empirical JPD:

$$JPD(PD_1, PD_2, \rho_{12}^A) = JPD_{\text{sim}} \tag{2}$$

where  $JPD(PD_1, PD_2, \rho_{12}^A)$  is the joint, 1-year distress probability of the two ABSs in a normal copula with correlation  $\rho_{12}^A$  and 1-year default probabilities  $PD_1$ ,  $PD_2$ . To be clear, the "asset return" correlation  $\rho_{12}^A$  differs from the ABSs' distress correlation  $\rho_{12}^D$ . Of course, the two are related:

$$\rho_{12}^{D} = \frac{JPD(PD_1, PD_2, \rho_{12}^{A}) - PD_1 \cdot PD_2}{\sqrt{PD_1 \cdot (1 - PD_1) \cdot PD_2 \cdot (1 - PD_2)}} \tag{3}$$

Generally, ABS "asset return" correlations are much higher than those of the underlying collateral. In our example, the asset return correlation for any pair of auto-loans, one from each ABS, is 10%. However, the "asset return" correlation for ABS loan-equivalents is 29% for the junior note and low collateral PD and significantly increases with subordination (Figure 2). This shows that the average collateral correlation is a highly biased estimate for the loan-equivalent correlation, since most of the idiosyncratic noise in the collateral pools washes out as the idiosyncratic shocks in the pool offset one another, leaving the common systematic factor to drive dynamics.

Results in Figures 1 and 2 are based on collateral pools of, for example, homogeneous auto-loans that share exposure to the same systematic factor (e.g., all in California). Therefore, the initial correlation between pairs of auto-loans was high to begin with. To examine the significance of pool diversification, consider an example with 50 state factors

![](_page_3_Figure_1.jpeg)

Figure 3 ABS loan-equivalent reference entity's "asset return" correlation—diversified pool (50 factors) versus homogeneous pool (common factor) with collateral pool parameters:  $PD = 2\%, R^2 = 10\%, LGD = 70\%$ 

 $(Z_1, \ldots, Z_{50})$ , where the auto-loans are equally distributed between the states. Each auto loan  $i$  has an associated state factor  $k(i)$ , such that  $r_i = R$ .  $Z_{k(i)} + \sqrt{1 - R^2} \cdot \varepsilon_i$ . Using Moody's KMV's GCorr Retail<sup>™</sup>, we set the correlation between any two state factors to be 65% ( $\rho(Z_k, Z_l) = 0.65$  for any  $1 < k < l < 50$ ).<sup>c</sup> Figure 3 compares the ABS "asset return" correlations between the diversified pool (50 factors) and the homogeneous pool (common factor) for pools with collateral  $R^2 = 10\%$  corresponding with a range of retail loans including student loans and consumer loans [8]. Collateral PD was set to 2%.

Figure 3 demonstrates that the loan-equivalent reference entity associated with a diversified pool is less correlated than that of a homogeneous pool. This finding is not surprising, given that state factors are not perfectly correlated, allowing for diversification. This exercise is particularly important when modeling a CDO of ABSs whose collateral pools are focused on different geographic locations.

## **Collateralized Debt Obligation (CDO)** Correlations

Even though CDO deals are similar to ABS deals, several important dynamics specific to CDOs impact correlation structure. First, corporate entities have lower default probabilities and higher  $R^2$  than typical reference entities associated with ABS collateral instruments. Second, names commonly overlap

in collateral pools of different CDO deals. Thompson and Rajendra [7] show that some names appear in more than 50% of deals in Fitch's Synthetic CDO Index (Ford Motor Co  $-56.52\%$ , and General Motors Corp  $-52.40\%$ ). Third, credit portfolios commonly have overlapping names across the singlename portion of the portfolio and the CDO collateral pool.

This section is divided into two subsections. The first analyzes the correlation between a CDO and a single-named instrument whose reference entity does not overlap with the CDO collateral pool. The second analyzes the correlation between two CDOs with varying degrees of collateral overlap.

#### Correlation between a Collateralized Debt *Obligation (CDO) and a Single-name Instrument*

Morokoff [6] calculated the loan-equivalent reference entity  $R^2$  for a pass-through CDO tranche from the joint probability of tranche distress and single-name instrument default (outside the CDO's collateral pool), known henceforth as the joint default-distress probability. He considered a collateral pool of  $N$ homogeneous instruments in a single factor environment. The single-name instrument was assumed similar to the instruments in the homogeneous collateral pool. Morokoff's methodology relies on using the independence of defaults, conditional on the realization of systematic risk factors, to compute the conditional joint default probability and then the expectation is taken over the systematic risk factor:

![](_page_4_Figure_1.jpeg)

Figure 4 The effect of collateral overlap on tranche loan-equivalent reference entity's "asset return" correlation with collateral pool parameters:  $PD = 2\%, R^2 = 25\%, LGD = 70\%$ 

 $P(\text{Tranche distress and single default}) = E_Z(P(\text{Tranche distress and single default } |Z=z))$ 

$$= E_Z(P(\text{# defaults in pool } \ge \hat{a}|Z=z) \cdot p(z))$$

$$= E_Z\left(\left(1 - \sum_{k=0}^{\hat{a}-1} P(\text{# defaults in pool } = k|Z=z)\right) \cdot p(z)\right)$$

$$= E_Z\left(\left(1 - \sum_{k=0}^{\hat{a}-1} \binom{N}{k} p(z)^k (1-p(z))^{N-k}\right) \cdot p(z)\right)$$

$$= p - \sum_{k=0}^{\hat{a}-1} \binom{N}{k} E_z(p(z)^{k+1} (1-p(z))^{N-k}) \tag{4}$$

where  $\hat{a}$  is the required number of defaults in the pool to cause a distress to the tranche,  $p(z) =$  $\frac{N^{-1}(p) - R \cdot z}{\sqrt{1 - R^2}}$ represents the PD conditional on the common factor  $Z = z$ , and  $p = E_Z[p(Z)]$ .

Similar to our analysis of ABS correlations, one can infer an "asset return" correlation  $\rho$  from the default probability, distress probability, and joint default-distress probability using a normal copula:  $JPD = N(N^{-1}(\text{tranche distress prob}), N^{-1}(p), \rho).$ Finally,  $R_{\text{Loan equivalent}}^2$  can be computed as  $\frac{\rho^2}{R^2}$ .

Note that these calculations present an alternative to the simulations in the ABS section. However, the computation becomes infeasible for large pools and is, therefore, more suitable for CDOs. The normal approximation to the binomial distribution can alleviate the cumbersome calculations, but forsome values of the systematic factors  $z$ , the conditional default probability  $p(z)$  is too small for the normal approximation to work.

#### Correlation of Collateralized Debt Obligations (CDOs) with Overlapping Names

Intuitively, the degree of overlap associated with two CDO tranches increases their correlation. To better understand the quantitative impact of overlap, we used simulation methods similar to those in the section Modeling the Correlation of Two ABSs. The relevant difference is that a certain percentage of the collateral pool is assumed to overlap when analyzing the correlations across the deals. Figure 4

presents the tranche loan-equivalent asset return correlations computed using the methodology in the section Modeling the Correlation of Two ABSs. The analysis was conducted on a high-yield deal with typical high-yield CDO properties (*PD* = 2% and *R*<sup>2</sup> = 25%). Along the *x*-axis, the collateral overlap varies from 0 to 65%. Each curve represents a subordination level for the tranche. Interestingly, the loan-equivalent asset correlation increase with overlap is more substantial for junior tranches. This follows from the susceptibility of junior tranches to idiosyncratic shocks. After all, the junior tranche can easily experience distress even when the systematic shock is high; all it takes is a single reference entity to realize a particularly low idiosyncratic shock. On the other hand, senior tranches are extremely unlikely to experience distress when the systematic shock is high. Therefore, the degree of overlap, which only affects idiosyncratic shocks, has a much greater effect on junior tranches.

### **Acknowledgments**

We would like to thank Zhenya Hu for help with the simulations and Mikael Nyberg for his suggestions.

### **End Notes**

a*.* Exceptions include Moody's KMV RiskFrontier, which models the terms of the subordinated note along with the correlation structure of the underlying collateral pool as it relates to the other instruments in the portfolio. Please see [5] for additional details.

b*.* For example, *PD*, and *LGD* estimates are available through Moody's Economy.com, and *R*<sup>2</sup> estimates are available through Moody's KMV.

c*.* Moody's KMV's GCorr Retail provides pairwise correlations for retail counterparties defined by MSA in the UnitedStates (e.g., San Francisco or New York City) and product type (e.g., auto loan or student loan, etc.). The correlations are estimated using delinquency rates data from Equifax and Moody's Economy.com. For more details on Moody's KMV's GCorr Retail please see [8].

### **References**

- [1] Agca, S. & Islam, S. (2007). *Can CDO Equity Be Short on Correlation?* working paper.
- [2] Coval, J.D., Jurek, J.W. & Stafford, E. (2008). *Economic Catastrophe Bonds*, HBS Finance working paper No. 07–102, available at: http://ssrn.com/abstract=995249
- [3] Coval, J.D., Jurek, J.W. & Stafford, E. (2008). *Re-Examining the Role of Rating Agencies: Lessons from Structured Finance*. working paper.
- [4] Gregory, J. & Laurent, J.P. (2004). In the core of correlation, *Risk* October, 87–91.
- [5] Moosbrucker, T. (2006). Explaining the correlation smile using variance gamma distributions, *The Journal of Fixed Income* **16**(1), 71–87.
- [6] Morokoff, W. (2006). *Modeling ABS, RMBS, CMBS: 'Loan Equivalent' Approach in Portfolio Manager*. unpublished work done at Moody's KMV.
- [7] Thompson, A. & Rajendra, G. (2006). *Global CDO market 2005 review*. Deutsche Bank whitepaper.
- [8] Wang, J., Zhang, J. & Levy, A. (2008). *Modeling Retail Correlations in Credit Portfolios*. Moody's KMV research whitepaper
- [9] Zeng, B. & Zhang, J. (2001). *An Empirical Assessment of Asset Correlation Models*, Moody's KMV whitepaper, available at: http://www.moodyskmv.com/research/files/ wp/emp assesment.pdf
- [10] Zhang, J., Zhu, F. & Lee, J. (2008). *Asset Correlation, Realized Default Correlation, and Portfolio Credit Risk* , available at: http://www.moodyskmv.com/research/files/ wp/Asset Correlation and Portfolio Risk.pdf

TOMER YAHALOM, AMNON LEVY & ANDREW S. KAPLIN
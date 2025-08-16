# **Recovery Rate**

A recovery rate (RR) is the fraction of an obligor's debt that a creditor stands to recover in the event of default. Recovery rates are usually expressed as a percentage of the par value of the claim (RP). Alternatively, recovery rates can be expressed as a percentage of the market value of the claim prior to default (RMV), or as a percentage of an equivalent treasury bond (RT). Recovery rates are closely associated to the concept of loss-given-default (LGD) where *LGD* = 1 − *RR*. Recovery rates are not known prior to default and can vary between 0 (full loss) and 1 (full recovery). Recovery rate risk in credit portfolios exists because of the uncertainty regarding recovery rates in the event of default.

Along with the probability of default, recovery rates are important parameters in determining the loss distribution of a credit portfolio. For this purpose, the Basel II Accords expressly recommend that the calculation of regulatory capital on banking institutions include the estimated recovery rates on their credit portfolios. The most widespread methodologies for estimating recovery rates use historical averages that are conditioned on the type of credit instrument, seniority (priority of repayment), and collateral [3]. However, these estimation methods do not account for the fact that recovery rates are known to be negatively correlated to the probability of default [1, 2]. The correlation between recovery rates and default probabilities is important because it exacerbates potential losses on credit portfolios. To this effect, recent credit models have attempted to capture the endogenous nature of recovery rates [2, 4, 9, 11]. Furthermore, recent products in the credit derivatives market have enabled the extraction of recovery rates either directly [5] or indirectly [10, 14]. In addition, since 2003, major credit rating agencies have been offering recovery rate ratings based on proprietary models [8].

## **Historical Recovery Rates**

Historical recovery rates for different types of credit securities are considered as important parameters in many credit risk models. There are various ways to estimate historical recovery rates. The most common are value-weighted mean recovery rates, issuerweighted mean recovery rates, and issuer-weighted median recovery rates. The value-weighted mean recovery rate is the average recovery rate on all defaulted issuers weighted by the face value of those issues. Issuer-weighted mean recovery rates and the issuer-weighted median recovery rates are the average and median, respectively, of the recovery rates on each issuer. Varma *et al.* [17] report historical recovery rates from 1982 to 2003 internationally. Globally, the value-weighted mean recovery rate for all bonds over that period was 33.8%, whereas the issuer-weighted mean and median recovery rates were 35.4% and 30.9%, respectively. In the United States, the value-weighted mean recovery rate for all bonds over that period was 35.4%, whereas the issuer-weighted mean and median recovery rates were 35.4% and 31.6%, respectively. For sovereign bonds, the value-weighted mean recovery rate for all bonds over that period was 31.2%, whereas the issuer-weighted mean and median recovery rates were 34.4% and 39.8%, respectively. Furthermore, recovery rates will differ depending on seniority and collateral of the bond. For instance, senior secured corporate bonds have a value-weighted mean recovery rate of 50.3%, compared to 22.9% for junior subordinated bonds, over 1982–2003. Carayon *et al.* [7] find that recovery rates on European bonds tend to be smaller. For instance, over 1987–2007, they find that senior secured bonds in Europe recover (issuer weighted) 61% compared to 70.6% in North America. In the Asia-Pacific (excluding Japan) region, Tennant *et al.* [16] find lower recovery rates of 35.61% on senior secured bonds over the 1990–2007 period.

## **Recovery Rates and Default Risk**

The major problem for credit risk models is that there is a large body of empirical evidence suggesting that recovery rates are negatively correlated with default probabilities. High periods of default are associated with low recovery rates and *vice versa*. The correlation between default probabilities and recovery rates may be ascribed to at least two nonmutually exclusive reasons. First, economic downturns can simultaneously cause increases in the probability of default and lower the value of recovered assets. Second, the price at which recovered assets are sold will depend on the financial condition of peer firms [15]. Under the latter argument, in periods of high default, recovered assets are forced to be sold at "fire-sale" prices. Acharya et al. [1] find both theories to be at work in explaining recovery rates. Altman et al. [2] empirically estimate the relationship between recovery rates  $(v)$  and default rates  $(x)$  using one linear and three nonlinear specifications:

$$y = 0.51 - 2.61x; \quad R^2 = 0.51$$
  

$$y = 0.002 - 0.113 \ln(x); \quad R^2 = 0.63$$
  

$$y = 0.61 - 8.72x + 54.8x^2; \quad R^2 = 0.65$$
  

$$y = \frac{0.138}{x^{0.29}}; \quad R^2 = 0.65$$
 (1)

All these specifications show a strong negative relationship between default rates and recovery rates.

#### **Economic Features of Recovery Rates**

There are several economic features of recovery rates that are important:

- 1. As described above, recovery rates are negatively correlated with default rates. This is the case when the data is examined historically as shown in [2] as well as when implied from the data, as in [10].
- 2. Recovery rates are highly variable and depend on regime (see [12]). They vary within rating and seniority class as well.
- 3. Seniority and industry are statistically significant determinants of recovery rates, as shown by Acharya et al. [1]. These authors also find that, in industries with high asset-specificity, recovery rates are lower.

### Implied Recovery Rates

Recovery rates can also be implied from prices of certain credit derivatives. One then speaks of "implied" (or risk-neutral) recovery rates, which may not coincide with historically observed recovery rates. Recovery rate swaps are agreements to exchange a fixed recovery rate for the realized recovery rate allowing the market's expected recovery rate to be directly recovered [5]. Digital credit default swaps (DDS) are credit default swaps (CDSs) where the recovery rates on default are prespecified, irrespective of the final recovery rate. Arthur and Kapoor [6] show how recovery rates can be recovered using a DDS and a CDS. Finally, Pan and Singleton [14] and Das and Hanouna [10] use CDS with different maturities to extract default probabilities and recovery rates.

Approximately, if credit spreads are known, we may write the spread  $s$  as a function of default probability ( $\lambda$ ) and recovery rate ( $\phi$ ):  $s \approx \lambda(1 - \phi)$ , implying that recovery may we written in a reducedform setting as follows:

$$\phi = 1 - \frac{s}{\lambda} \tag{2}$$

More formalized and exact versions of this approximate relation may be derived from a CDS pricing model or a bond pricing model. Recovery may also be derived in the class of Merton [13] models. The expression for recovery rate is

$$E[\phi] = E\left[\frac{V_T}{D}|V_T < D\right] = \frac{1}{D}E\left[V_T|V_T < D\right]$$
$$= \frac{V_0}{D}e^{rT}\left\{1 - N(d_1)\right\}$$
$$d_1 = \frac{\ln(V_0/D) + (r + \frac{1}{2}\sigma_V^2)T}{\sigma\sqrt{T}}\tag{3}$$

where  $\{V_0, \sigma\}$  are the initial value and volatility of the firm,  $D$  is the face value of debt with maturity  $T$ , and r is the risk-free interest rate.  $N(\cdot)$  is the normal distribution function.

#### References

- $\lceil 1 \rceil$ Acharya, V., Bharath, S.r & Srinivasan, A. (2007). Does industry-wide distress affect defaulted firms? Evidence from creditor recoveries, Journal of Financial Economics 85(3), 787-821.
- [2] Altman, E., Brady, B., Resti, A. & Sironi, A. (2004). The link between default and recovery rates: theory, empirical evidence and implications, Journal of Business 76(6), 2203-2227.
- [3] Altman, E., Resti, A. & Sironi, A. (2003). Default Recovery Rates in Credit Risk Modeling: A Review of the Literature and Empirical Evidence, working paper, New York University.
- [4] Bakshi, G., Madan, D. & Zhang, F. (2001). Recovery in Default Risk Modeling: Theoretical Foundations and Empirical Applications, working paper, University of Maryland.

- [5] Berd, A.M. (2005). Recovery swaps, *Journal of Credit Risk* **1**(3), 1–10.
- [6] Berd, A. & Kapoor, V. (2002). Digital premium, *Journal of Derivatives* **10**(3), 66.
- [7] Carayon, J.-M., West, M., Emery, K. & Cantor, R. (2008). *European Corporate Default and Recovery Rates*, 1985–2007, Moody's investors service.
- [8] Chew, W.H. & Kerr, S.S. (2005). Recovery ratings: a new window on recovery risk, in *Standard and Poor's: A guide to the Loan Market*, Standard and Poor's.
- [9] Christensen, J. (2005). *Joint Estimation of Default and Recovery Risk: A Simulation Study*, working paper, Copenhagen Business School.
- [10] Das, S.R. & Hanouna, P. (2009). Implied Recovery, forthcoming, *Journal of Economic Dynamics and Control*.
- [11] Guo, X., Jarrow, R. & Zeng, Y. (2005). *Modeling the Recovery Rate in a Reduced Form Model*, working paper, Cornell University.
- [12] Hu, W. (2004). *Applying the MLE Analysis on the Recovery Rate Modeling of US Corporate Bonds*, Master's Thesis in Financial Engineering, University of California, Berkeley.

- [13] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *The Journal of Finance* **29**, 449–470.
- [14] Pan, J. & Singleton, Ken (2008). Default and recovery implicit in the term structure of sovereign CDS spreads, *Journal of Finance* **63**, 2345–2384.
- [15] Shleifer, A. & Vishny, R. (1992). Liquidation values and debt capacity: a market equilibrium approach, *Journal of Finance* **47**, 1343–1366.
- [16] Tennant, J., Emery, K., Cantor, R., Elliott, J. & Cahill, B. (2007). *Default and Recovery Rates of Asia-Pacific Corporate Bond, Moody's Investors Service and Loan Issuers, Excluding Japan*, 1990–1H200.
- [17] Varma, P., Cantor, Richard & Hamilton, David (2003). *Recovery Rates on Defaulted Corporate Bonds and Preferred Stocks*, 1982–2003, Moody's investors service.

## **Related Articles**

**Credit Default Swaps**; **Credit Risk**; **Exposure to Default and Loss Given Default**; **Recovery Swap**.

SANJIV R. DAS & PAUL HANOUNA
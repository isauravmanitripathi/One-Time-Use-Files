# **CDO Tranches: Impact on Economic Capital**

With the recent rapid growth in the collateralization debt obligation (CDO) market since its inception in the mid-1990s, many financial institutions, in particular banks, are holding CDO tranches of many different transactions in their credit portfolios. Thus, evaluation of the impact of CDO tranches on the economic capital of a credit portfolio is becoming increasingly important. This article discusses how to measure the impact of CDO tranches on economic capital and capital allocation in credit portfolios. The economic capital of a credit portfolio is the amount of capital reserved to pay for any unexpected losses up to a confidence level as required by the financial institution. The purpose of economic capital is to buffer the effect of large losses in the portfolio. Capital allocation measures the incremental economic capital requirement of a portfolio as a result of adding an asset, such as a CDO tranche. Economic capital and capital allocation are calculated from the probability distribution of portfolio losses. Monte Carlo simulation has been widely applied to calculate the probability distribution of portfolio loss in credit portfolios comprised of bonds and loans. However, it is only recently that Monte Carlo simulations are being used in credit portfolios that comprise CDO tranches in addition to bonds and loans. The methodology presented here addresses this important application in a consistent framework.

The article is organized as follows. In the section Monte Carlo Simulation of Credit Portfolios Comprised of Bonds, Loans, and Collateralization Debt Obligation (CDO) Tranches, a brief introduction is given to the methodology for calculating portfolio loss distribution of credit portfolios comprised of bonds, loans, and CDO tranches. The section Economic Capital and Capital Allocation discusses the calculation of economic capital and capital allocation from the portfolio loss distribution. In the section An Example of Calculating Portfolio Loss Distribution, an example is presented for calculating the probability distribution of portfolio loss for a portfolio comprised of loans and one synthetic CDO tranche. From the loss distribution, economic allocation to the tranche is calculated and compared with the capital allocation of a loan of the same maturity and similar credit quality.

# **Monte Carlo Simulation of Credit Portfolios Comprised of Bonds, Loans, and Collateralization Debt Obligation (CDO) Tranches**

In credit portfolio management, Monte Carlo methods are the industry standard approach for calculating risk figures from a portfolio loss distribution. Even though the synthetic index-based market has seen considerable development of analytic and semianalytic approaches, these methods do not fully apply to credit portfolio management. This is mainly a consequence of the heterogeneity of underlying assets and the need for default indicators at individual asset levels.

Following standard industry convention, we use a bottom-up approach to model correlated defaults in a pool of names by applying an asset value factor model first introduced by Merton [1] and Vasicek [4]. The calculation of correlated defaults in a pool composed of loans and CDO tranches consists of two basic steps. The first step is to determine the default or credit migration of bonds and loans in the portfolio together with the underlying assets of CDO tranches over a horizon. The second step is valuing the CDO tranches at horizon. For a CDO tranche, its value would be the sum of the cash flows received over the horizon plus a forward value calculated on the basis of the future credit state of its underlying assets at horizon. Cash flows received by a synthetic tranche over the horizon would consist mainly of interest payments, while those received by a cash CDO tranche would consist of interest payments and principal repayments. The loss of a tranche over a horizon is then calculated as the difference between the tranche value at horizon and its current value. This yields a loss distribution at horizon for a credit portfolio comprised of bonds, loans, and CDO tranches, from which its economic capital and capital allocation are calculated.

Although the methodology discussed here for the calculation of economic capital in a credit portfolio is conceptually simple, it is highly complex in practice because it requires nested Monte Carlo simulations. A nested Monte Carlo simulation consists of an outer simulation and an inner simulation at every scenario of the outer simulation. In the outer simulation, systematic and idiosyncratic risk factors are drawn within the interval defined by its lower edge,  $k_i^{r,\text{lower}}$ , and upper edge,  $k_i^{r,\text{upper}}$ , as follows:

$$\left[k_j^{r,\text{lower}}, k_j^{r,\text{upper}}\right] = \left[\Phi^{-1}\left(PD_j + \sum_k^{r-1} T_{j,k}\right), \Phi^{-1}\left(PD_j + \sum_k^r T_{j,k}\right)\right] \tag{2}$$

at each scenario over a horizon to calculate the defaults and new credit states of nondefaulted assets. The purpose of the inner simulation is to value a CDO tranche conditional on the credit states of its underlying assets at horizon. Valuation of the bonds and loans based on the future credit states of their obligors is also required at a horizon, but their valuation generally does not require a simulation. Even though development of efficient techniques to perform nested Monte Carlo simulations is an interesting and important area of research, a more thorough discussion would be well beyond the scope of the present article.

For the purpose of illustrating the Monte Carlo simulation methodology, we discuss an example of calculating the probability distribution of portfolio loss for a credit portfolio comprised of  $N$  loans and one CDO tranche,  $T_r$ , over a horizon of 1 year. Furthermore, we assume that the CDO is backed by these loans of the portfolio.

To determine the defaults and credit migrations of the loans at horizon, we calculate their asset value correlation with a single-factor model. The asset value and credit state of a loan in this article refer to those of its obligor. In the single-factor model framework, the sensitivity of the asset value of a loan,  $X_i$ , to the systematic risk factor is given in terms of the correlation parameter  $\rho_i$  as follows:

$$X_i = \rho_i Y + \sqrt{1 - \rho_i^2} Z_i \tag{1}$$

where  $Y$  and  $Z_i$  are the systematic risk factor and the idiosyncratic risk factor of the loan, respectively. Both  $Y$  and  $Z_i$  are independent and have standard normal distribution.

Furthermore, we assume that the calculation of the default and credit migration of a loan at horizon is based on the change of its asset value as given by equation (1). Specifically, a loan is defaulted if its asset value falls below its default threshold, which is defined by its default probability to horizon. Analogously, a loan  $i$  initially in the state  $j$  is migrated to a state  $r$  if its asset value at horizon falls where  $\Phi^{-1}[\bullet]$  is the inverse of the standard normal distribution and  $T_{i,k}$  is the probability for the transition from state  $j$  to state  $k$ . The calculation of the defaults and credit migrations of the portfolio's loans from this first step would be used to determine the loss of the portfolio over the horizon.

The contribution to the loss of portfolio value consists of the loss of the loans defaulted over the horizon and the loss in value of the loans which are not defaulted and the CDO tranche. The total loss of the portfolio at horizon is calculated as follows:

$$L_M = \sum_{N} \omega_i \times I_i^D \times LGD_i + \sum_{N,T_r} \omega_i \times (1 - I_i^D)$$
$$\times \left( PV_{i,t_0} \times DF_{t_0 \to H} - PV_{i,H} \right) \tag{3}$$

where  $\omega_i$  is the weight of the notional value of the loan relative to the total notional value of the portfolio.  $LGD_i$  is the fixed percentage loss of the notional value of the loan at default.  $I_i^D$  is the default indicator of the loan, which is defined as  $I_i^D = 1$ , if  $X_i < k_i^D$  and  $I_i^D = 0$ , if  $X_i \ge k_i^D$ .  $PV_{i,H}$  and  $PV_{i,t_0}$ are the values of asset  $i$  at  $H$  and  $t_0$ , respectively, and  $DF_{t \to H}$  is the discount factor from  $t_0$  to H. The first sum of equation (3) consists of the loss of the loans defaulted over the horizon and the second sum consists of the loss in value of the loans which are not defaulted and the CDO tranche.

Valuation of a loan at the horizon assumes that the future credit state of a loan sufficiently determine its value. Similarly, valuation of a CDO tranche at horizon assumes that the future credit states of its underlying assets at horizon sufficiently determine its value although the valuation could require another simulation.

Although the calculation of loss distribution discussed here is based on a single-factor asset value model, extension of the calculation to a multifactor asset model is fairly straightforward. Thus, employing a multifactor asset model in the calculation of loss distribution allows one to apply the methodology discussed in this article to portfolios with heterogeneous asset compositions.

## **Economic Capital and Capital Allocation**

Economic capital of a credit portfolio is defined as the loss exceeding the portfolio expected loss (EL) for the quantiles of the loss distribution to a given confidence level *α*, that is, *ECp(α)* = *q(α)* − *EL* with *q(α)* = min{*x* : *P (L < x)* ≥ *α*}. This confidence level is interpreted as the probability that the credit portfolio of a financial institution would suffer a loss, which will use up the institution's capital. Since capital exhaustion implies institutional failure, the confidence level *α* is equivalent to the default risk of an institution.

In the calculation of capital allocation for the CDO tranche of the credit portfolio discussed in the previous section, we apply the methodology of expected shortfall. The expected shortfall<sup>a</sup> of an asset, either of the loans or the CDO tranche, is defined in terms of the portfolio loss distribution as follows:

$$ES_{i} = \mathrm{E}[L_{i,H}|L_{\text{portfolio},H} > q(\alpha)] - \mathrm{E}[L_{i,H}] \quad (4)$$

where *Li,H* and *L*portfolio*,H* are the losses of asset *i* and the portfolio at *H*. Then, the capital allocation of the CDO tranche in terms of its expected shortfall *ES*tranche and the expected shortfalls of the loans in the portfolio is calculated as follows:

$$EC_{\text{tranche}}(\alpha) = EC_p(\alpha) \frac{ES_{\text{tranche}}}{\sum_{N,T_r} ES_i}$$
(5)

## **An Example of Calculating Portfolio Loss Distribution**

We discuss an example of calculating the portfolio loss distribution over a horizon of 1 year for a credit portfolio of loans and a CDO tranche.

#### *Data and Modeling Assumptions*

A credit portfolio is assumed to be composed of 125 loans and one synthetic CDO tranche. Each loan is a unique entity, which is taken from the entities of the iTraxx Europe S8 index. The iTraxx Europe index is a credit default swap (CDS) index composed of the most liquid 125 CDSs referencing European investment grade credits. Each loan assumes a notional amount of ¤1 million, a maturity of 1 year, and a fixed recovery rate of 25%. The synthetic CDO is based on a portfolio of 125 CDSs. Each CDS assumes a 5-year maturity, the same maturity as the CDO. Each CDS references the entity of one of the loans of the credit portfolio. Therefore, this example considers a case where there is a strong overlap between the credit portfolio's assets and the underlying assets of the CDO.

The nested Monte Carlo simulation as discussed in the section Monte Carlo Simulation of Credit Portfolios Comprised of Bonds, Loans, and Collateralization Debt Obligation (CDO) Tranches is applied to calculate the contribution of the synthetic CDO tranche to the portfolio loss distribution. At each scenario of the outer simulation, we determine which loan is defaulted and a future credit state for the one which is not defaulted. Then, since the loans mature at horizon, we calculate the loss in the notional value of the portfolio from the defaults of the loans over the horizon. To calculate the loss of the synthetic CDO tranche, we value the tranche at horizon based on the future credit states of its underlying assets and compare the value at horizon to its current value. In this example, the future credit states of the underlying assets are exactly those of the loans of the credit portfolio.

The standard industry practice is to use the riskneutral default probabilities of the underlying assets based on their future credit states to value the synthetic CDO tranche at horizon. One would calculate a mark-to-market (MTM) value of the tranche by using the risk-neutral default probabilities of the underlying assets calibrated to their market spreads and the correlation parameter calibrated to the pricing of tranches of similar structures.b The calculation is fairly straightforward once the parameters are determined. However, calculating an MTM value of the tranche at horizon is much more challenging because one must determine the future credit states of its underlying assets and apply them to derive their forward risk-neutral default probabilities.

Instead of calculating the loss of the CDO tranche at horizon from its MTM values, we approximate its loss at each scenario of the outer simulation by the conditional expected loss of the tranche. The conditional expected loss of the tranche at horizon in each scenario of the outer simulation is calculated as the average loss over the scenarios of the inner simulation. We employ the following assumptions in the calculation of conditional expected loss at horizon. First, the future credit state of a loan is represented by an S&P credit rating. The S&P credit rating of a loan at horizon is calculated from its current S&P credit rating with the empirical S&P transition matrix [2]. Second, the best estimation of the forward default probability of a loan at horizon is the forward default probability derived from the default term structure based on its S&P rating. We are assuming that default is a Markov process, but properly inhomogeneous in time. Lastly, we include only the loss of principal in the calculation of conditional expected loss, thereby neglecting any loss from interest payments to the tranche. In addition, we assume a zero interest rate. Under these assumptions, we use a semianalytical approach [3] to calculate the conditional expected loss of the CDO tranche at horizon instead of performing an inner simulation.

We calculate economic capital for the credit portfolio as the loss of its value exceeding the portfolio expected loss at the confidence level of 99% and calculate capital allocation based on expected shortfall methodology at the confidence level of 95%. We assume a correlation parameter of 31% for the underlying assets. We consider a synthetic CDO tranche with an attachment point of 0.0, 3, or 6% and a corresponding detachment point of 3, 6, or 9%. Table 1 shows the expected loss of a tranche as of today and at horizon and Table 2 shows the economic capital allocation of the tranche at different notional amounts. Expected loss of the tranche as of today is calculated with a 5-year cumulative default probability for the underlying assets based on their current S&P ratings. Expected loss of the tranche at horizon is calculated by averaging the conditional expected loss of the tranche at horizon over the scenarios of the outer simulation of the nested Monte Carlo simulation.

#### *Analysis of Results*

Now, we would like to discuss the results for the *EL* of the tranche and its capital allocation as shown in Tables 1 and 2. Table 1 clearly shows that

**Table 1** Tranche statistics

|               | 0–3%   | 3–6%  | 6–9%  |
|---------------|--------|-------|-------|
| EL today      | 34.71% | 2.61% | 0.23% |
| EL at horizon | 38.81% | 3.43% | 0.33% |

| Table 2 |  | Economic capital allocation to the CDO tranche |  |  |  |
|---------|--|------------------------------------------------|--|--|--|
|---------|--|------------------------------------------------|--|--|--|

| Notional<br>(MM) | Exposure<br>(MM) | 0–3%   | 3–6%   | 6–9%  |
|------------------|------------------|--------|--------|-------|
| 10               | 0.3              | 28.13% | 10.46% | 1.36% |
| 20               | 0.6              | 32.04% | 10.48% | 1.37% |
| 30               | 0.9              | 35.49% | 11.12% | 1.38% |
| 40               | 1.2              | 38.44% | 11.41% | 1.39% |
| 50               | 1.5              | 40.94% | 11.69% | 1.39% |

the *EL* values of the tranche at horizon are larger than the values as of today. In particular, for the 6–9% tranche, the difference is as much as 50%. However, the difference decreases with decreasing tranche subordination and becomes much smaller for the 0–3% tranche. This should suggest that calculating the correlated defaults of the underlying assets plays an important role in determining these results. The *EL* of the 6–9% tranche is more sensitive to default clusters in the portfolio than the *EL* of the 0–3% tranche.

Calculating the *EL* of a tranche as of today and at horizon requires modeling the assets defaults in the pool over the life of a transaction. The calculation of the *EL* of a tranche as of today is based on the approach of Merton [1]. We calculate the defaults of the underlying assets over a horizon of 5 years. The timing of the defaults is not required because the calculation of the expected loss assumes a zero interest rate. It is a one-step calculation of default since both the systematic and idiosyncratic risk factors are drawn once at each scenario of the Monte Carlo simulation. However, the calculation of the *EL* of the tranche at horizon assumes two steps although the calculation of the defaults in each of these steps is also based on the approach of Merton. It is a two-step calculation of default because both the systematic and idiosyncratic risk factors are drawn independently twice in the outer and inner simulations of the nested Monte Carlo simulation. As a result of calculating the default in a single step in the calculation of *EL* as of today and in two steps in the calculation of *EL* at horizon, one should expect the results to be different because of the difference in capturing the correlated defaults in the portfolio.c Since the calculation of portfolio loss distribution requires using this two-step approach in calculating defaults, we should adopt this approach in the calculation of *EL* of the tranche as of today and at

| Table 3 |  | Loan statistics |
|---------|--|-----------------|
|---------|--|-----------------|

|               | AA−   | BBB+  | BBB−  | BB    |
|---------------|-------|-------|-------|-------|
| EL today      | 0.30% | 1.45% | 3.71% | 7.49% |
| EL at horizon | 0.33% | 1.58% | 3.69% | 7.49% |

horizon. Consequently, both *EL*s would be calculated to have the same value.

The results in Table 3 also show that the *EL* of a 5-year loan at horizon is larger than its *EL* as of today for different S&P ratings although the difference is less than 10%. This is simply the consequence of using empirically measured S&P transition matrix and default probability term structures. However, since in comparing a CDO tranche to a loan of similar credit risk we have opted to measure credit risk by an asset's *EL* at horizon, this kind of discrepancy from using empirically measured transition matrix and default probability term structures should not affect the comparison of the results of this article.

In Table 2, we present the tranche's capital allocations at different notional values. Capital allocation is reported as per unit exposure of the tranche. Since the maximum loss of a tranche depends on its thickness defined as the difference between its detachment point and attachment point, it is more meaningful to report capital per unit of exposure rather than per unit of notional amount. These results clearly show that capital allocation per unit of exposure increases with increasing exposure. However, the increase is much larger for the 0–3% tranche than for the 6–9% tranche. This is because the 6–9% tranche is mostly sensitive to systematic risk, while the 0–3% tranche is sensitive to both systematic and idiosyncratic risks. An asset that is mostly sensitive to systematic risk and an asset in a very granular portfolio should have capital requirements that scale approximately the same extent with the size of exposures. Capital allocation per unit of exposure of an asset in a very granular portfolio is approximately constant independent of the asset's exposure size. Thus, as shown in Table 2, the capital allocation of a senior tranche increases slowly with exposure size as compared to a junior tranche.

Now, we would like to compare the capital allocation of a tranche with that of a loan of similar credit quality and the same maturity. In a separate calculation, we substitute the CDO tranche in the credit

**Table 4** Economic capital allocation to a loan substituting the CDO tranche

| Exposure<br>(MM) | AA−   | BBB+  | BBB−  | BB     |
|------------------|-------|-------|-------|--------|
| 0.3              | 0.87% | 3.88% | 5.94% | 11.03% |
| 0.6              | 1.11% | 4.49% | 6.95% | 12.55% |
| 0.9              | 1.18% | 4.85% | 7.53% | 13.35% |
| 1.2              | 1.24% | 5.03% | 7.95% | 13.66% |
| 1.5              | 1.24% | 5.10% | 8.24% | 14.49% |

portfolio with a loan of 5 years' maturity and re-run the Monte Carlo simulation to calculate the capital allocation of the substituted loan. Table 4 presents the capital allocations for the substituted loans with different S&P ratings.

To compare the capital allocation of a CDO tranche with that of its loan equivalent, we define a loan equivalent of a CDO tranche as a loan that has the same value of *EL* at horizon as the CDO tranche. We assume that a CDO tranche and its loan equivalent have similar credit risks as of today. For example, the loan with AA−rating of Table 4 is a loan equivalent of the 6–9% tranche. However, for the 3–6% tranche, we cannot find a loan from Table 4 with its *EL* at horizon matching that of the CDO tranche. For the purpose of comparing the capital allocation of the 3–6% tranche to its loan equivalent, we scale the capital allocations of the loan with BBB−rating by a ratio of the tranche's *EL* at horizon over the loan's *EL* at horizon. We assume that the scaled capital allocations are for the loan equivalent of the 3–6% tranche.

In Table 5, we compare the capital allocations of the 3–6% and 6–9% tranches with those of their loan equivalents. The results clearly show that the capital

**Table 5** Capital allocations: CDO tranche *versus* loan equivalent

| Exposure<br>(MM) | AA−   | 6–9%  | Scaled of<br>BBB−∗ | 3–6%   |
|------------------|-------|-------|--------------------|--------|
| 0.3              | 0.87% | 1.36% | 5.52%              | 10.46% |
| 0.6              | 1.11% | 1.37% | 6.46%              | 10.48% |
| 0.9              | 1.18% | 1.38% | 7.00%              | 11.12% |
| 1.2              | 1.24% | 1.39% | 7.39%              | 11.41% |
| 1.5              | 1.24% | 1.39% | 7.66%              | 11.69% |
|                  |       |       |                    |        |

<sup>∗</sup> Capital allocations calculated by multiplying a constant factor of 0.93 with the capital allocations of the loan with a BBB−rating

allocation of a CDO tranche can be larger than that of its loan equivalent by as much as 80%.

We can understand these results in terms of the increase in the systematic risk of the credit portfolio as a result of adding a CDO tranche or a loan. In general, a credit portfolio with larger systematic risk would require higher economic capital. A CDO transaction backed by a pool of assets is mostly sensitive to systematic risks since its exposures to idiosyncratic risk factors are already significantly reduced through the diversification of the assets in the pool. Therefore, adding CDO tranches to a credit portfolio could significantly increase the portfolio's systematic risk compared to adding a loan equivalent. As a result, one should expect that holding a CDO tranche in a credit portfolio would require extra economic capital compared to holding a loan of similar credit rating and the same maturity.

## **Conclusion**

In this article, we presented the methodology based on nested Monte Carlo simulation to measure the impact of CDO tranches on economic capital and capital allocation of credit portfolios. One of the advantages of using the methodology presented here is in the calculation of the correlated defaults of the assets in a portfolio. Calculation of correlated defaults is important in calculating economic capital for a portfolio especially for those holding CDO tranches because CDO tranches are mostly sensitive to systematic risk. As an example, we applied the methodology of calculating capital allocation to a synthetic CDO tranche in a credit portfolio. This portfolio also comprises of the loans to which the underlying assets of the CDO are referencing. The results of our calculation show that the capital allocation of adding a CDO tranche to a credit portfolio can be much larger than that of adding a loan of similar credit quality and the same maturity. In some cases, the increase in capital allocation is as much as 80%. Our finding clearly suggests that by treating a CDO tranche as a loan equivalent, only a poor approximation of economic capital is obtained. This explains why the methodology presented in this article is necessary to measure the impact of CDO tranches in credit portfolios.

## **Acknowledgments**

I would like to thank David Cao, Michele Freed, Saiyid Islam, and Liming Yang for many useful discussions. I especially want to thank Bill Morokoff and Christoff Goessl for careful reading of the manuscript and providing me with many useful comments. The views expressed in this paper are the author's own and do not necessarily represent those of Market & Investment Banking of the UniCredit Group, Lloyds TSB Group or Moody's KMV. All errors remain my responsibility.

## **End Notes**

a*.* The other approach of calculating capital allocation is based on marginal Value-at-Risk contribution. For a recent review of the two approaches of calculating capital allocation, please refer to the following paper: Glasserman, P. (2006). Measuring marginal risk contribution in credit portfolios, *Journal of Computational Finance* **9,** 2.

b*.* See Burtschell, X., Gregory, J. & Laurent, L.-P. (2005). *A Comparative Analysis of CDO Pricing Models*, Working paper, BNP-Paribas.

c*.* In valuing a synthetic CDO tranche, one can use a singlestep default model because the valuation is based on the calibration of asset correlation parameters to the pricing of similar tranches in the market.

## **References**

- [1] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [2] Okunev, P. (2005). *A Fast Algorithm for Computing Expected Loan Portfolio Tranche Loss in the Gaussian Factor Model*, LBNL-57676.
- [3] Standard & Poor's (1996). *Credit Week-April*.
- [4] Vasicek, O. (2002). Loan portfolio value, *Risk* **15**, 160–162.

## **Related Articles**

**Collateralized Debt Obligations (CDO)**; **Gaussian Copula Model**; **Monte Carlo Simulation**; **Value-at-Risk**.

YIM T. LEE
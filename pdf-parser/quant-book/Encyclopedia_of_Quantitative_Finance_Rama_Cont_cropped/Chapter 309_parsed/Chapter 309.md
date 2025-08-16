# **Economic Capital**

## **Role of Capital in Financial Institutions**

In contrast to a typical corporation, the key role of capital in a financial institution is not primarily one of providing a source of funding for the organization.a For example, banks usually have ready access to funding through their deposit-taking activities, which can be increased fairly fluidly. Instead, the primary role of capital in a bank, apart from the transfer of ownership, is to act as a buffer to

- absorb large unexpected losses;
- protect depositors and other claim holders; and
- provide confidence to external investors and rating agencies on the financial health and viability of the firm.

Typically, the sources of financial risk are classified as (*see* **Risk Exposures**)

- *credit risk* —losses associated with the default (or credit downgrades and upgrades) of an obligor (a counterparty, borrower, or debt issuer);
- *market risk* —losses associated with changes in market values; and
- *operational risk* —losses associated with operating failures.

Other types of risk faced by a financial institution include *liquidity risk*, *business* (or *strategic*) *risk*, *legal risk*, *insurance* and *liability risks*, etc. Capital provides a metric for aggregating risks across both different asset classes and across different risk types.

We can broadly classify capital into three types:

- *Book capital* —the actual physical capital held. While in its strictest definition this should be simply *equity capital*, more generally this might also include other assets such as liquid debt or hybrid instruments.
- *Regulatory capital* —the capital that a bank is required to hold by regulators in order to operate; this is defined by the regulatory authorities to act as a proxy for economic capital (EC).
- *Economic capital* —an estimate of the minimum level of capital that a firm requires to operate its business with a desired target solvency level. Sometimes this is also referred to as *risk capital*. b

EC is meant to reflect the true "fair market" value differential between assets and liabilities. In contrast, regulatory capital may be commonly defined in terms of accounting book value measures rather than market values.c The objectives of regulatory capital requirements are to safeguard the security of the financial system as a whole and to ensure its ongoing viability, as well as to create a level playing field across all institutions.

## **Economic Capital Definitions**

## *Economic Capital as a Buffer for Unexpected Losses*

EC represents the minimum buffer that provides protection against all risks faced by an institution at a target confidence level. Since it would be too costly to cover losses at the 100% level, EC is set at a lower confidence level (e.g., 99.9%). The choice of this level involves a trade-off between providing high returns on capital for shareholders and providing protection to the debt holders and other claim holders, such as depositors, while achieving a desired rating. For example, a firm's probability of default over one year should be at most 0.5% to achieve a BBB rating by S&P. Thus, it must have enough capital to sustain a "0.5% worst-case loss" over a one-year time horizon.

The approach commonly taken by practitioners is to define EC to absorb only *unexpected losses* up to a certain confidence level, with *reserves* set aside to absorb *expected losses* (EL). Thus, EC is estimated as the *Value at Risk* (VaR) (*see* **Value-at-Risk**; **Market Risk**) at an *α*% confidence level less the expected loss (see Figure 1):

$$EC_{\alpha} = VaR_{\alpha} - EL \tag{1}$$

Subtracting *EL* from the worse-case losses represents a simplifying approximation to estimate *EC* and generally leads to conservative estimates. More precisely, *EC* should measure loss relative to the portfolio's initial mark-to-market (MtM) value and *not* relative to the *EL* of its end-of-period distribution, and should account for the interest payments that must be made on the funding debt:

$$EC = A_0 - \frac{VaR_{\alpha}(A_1)}{(1 + r_D)}$$
 (2)

![](_page_1_Figure_1.jpeg)

**Figure 1** Loss distribution and capital

where *A*<sup>0</sup> is the market value of the assets at time 0, and *rD* the nominal return on the liabilities. The estimation of the interest compensation factor and of the MtM value of the portfolio generally requires the use of an asset pricing model.d

## *Economic Capital or "Risk Capital" as Insurance for the Value of the Firm*

Some economists have used the term *risk capital* to refer to the smallest amount that can be invested to insure the value of the firm's net assets against loss in value relative to a risk-free investment [4, 5]. For example, the risk capital of a long US Treasury bond position is the value of a *put option* with strike equal to the forward price of the bond.

## **Economic Capital as a Management Tool**

EC provides a consistent metric to determine risk aggregation, asset and business allocation, as well as performance measurement.

In addition to computing the total EC for a portfolio, it is important to *attribute* this capital *a posteriori* to various subportfolios such as the firm's activities, business units, counterparties or even individual transactions, and to *allocate* it *a priori* in an optimal manner, to maximize risk-adjusted returns (*see* **Economic Capital Allocation**). EC provides a useful basis for *risk-adjusted performance measurement* (RAPM), also referred to as *risk-adjusted return on* *capital* (*RAROC*) (*see* **Risk-adjusted Return on Capital (RAROC)**) since it defines a consistent metric that spans all asset and risk classes, thereby providing an "apples-to-apples" benchmark for evaluating the performance of alternative business opportunities. Each asset can be assessed on a consistent basis, with returns adjusted appropriately in the context of the amount of risk assumed.

## **Economic Capital Calculation**

Methods for calculating EC can be classified as *top–down* or *bottom–up* approaches. In addition to statistical methods, practitioners also commonly use *stress*-*testing* methods (*see* **Stress Testing**).

#### *Top–down Approaches*

EC can be estimated based on the aggregate information of the firm's performance. Such "top–down approaches" generally use information on either *earnings* or *stock prices*.

The earnings-based approach typically makes the simplifying assumption that the market value of capital is equal to the value of a perpetual stream of expected earnings. As the determination of *EC* is based on the ability to sustain a worst-case loss at a given confidence level, this leads to

$$EC_0 = EaR/k \tag{3}$$

where  $EaR$  is the difference between expected earnings and the earnings under the worst-case scenario at a confidence level, and  $k$  is the required return associated with the riskiness of the earnings. Often, this approach is used with the additional assumption that earnings are normally distributed; thus, the confidence level is determined as a multiple of the volatility (see [7]).

Limitations of the earnings approach include its requirement of reliable historical performance data, and its inability to link EC directly to the sources of risk.

An alternative top-down approach is based on the Black-Scholes-Merton option pricing framework (see Structural Default Risk Models). It assumes that the market value of capital can be modeled as a *call option* on the value of the firm's assets where the strike is the notional value of the debt. An advantage of this approach is the availability of stock market data. However, several simplifications regarding the capital structure and model assumptions must be made to apply this tool in practice. A key limitation is that it does not allow the allocation of capital into different risks or business lines.

#### *Bottom*–*up Approaches*

EC is estimated by modeling the individual transactions and businesses and then aggregating the risks using advanced statistical portfolio models and stress testing. The bottom-up approaches have now become the best practice and provide greater transparency in isolating risks and allocating capital.

The estimation of EC at the firm level requires consolidation of risks at two levels.

- First, one computes the market risk, credit risk, operational risk, and so on, at the enterprise level. To achieve this, a firm might use separate VaR models for market risk, credit risk, and operational risk.
- Then, at the second level, the firm consolidates the capital across these risks.

A simple method to aggregate capital in the second step is to add up the credit risk capital, market risk capital, and operational risk capital. This produces a conservative capital measure (essentially, assuming that the risks are perfectly correlated). More advanced approaches apply *copula functions* (see Copulas: **Estimation**) to aggregate risks, and many firms devote considerable effort to measure the correlations hetween these risks

### Stress Testing and Economic Capital

In addition to the VaR-based approaches, practitioners usually use stress testing as an important part of their EC methodology. Commonly, this involves the development of several specific adverse extreme scenarios and the assessment of portfolio losses against them. Stress scenarios may be based on historical experience or management judgment.

The combination of stress testing and statistical measures to develop EC measures is generally ad hoc, largely based on management's judgment. For example, an institution might assign the EC for market risk as 50% times the 99% VaR plus 50% the loss outcome from some stress scenarios (see Stress Testing).

## **End Notes**

<sup>a.</sup>For a more detailed discussion of economic capital, see  $[1, 6]$  and the references cited therein.

<sup>b.</sup> Alternatively, Matten [3] defines  $EC = \text{risk capital} +$ goodwill.

<sup>c</sup>.In some cases, accounting practice allows items to be reported on a market value basis.

<sup>d.</sup>This equation is derived by assuming that assets  $A_0$  are funded by debt,  $L_0$ , and equity,  $E_0: A_0 = L_0 + E_0$ . The amount owed at maturity will be  $L_0 \times (1 + r_D) = (A_0 E_0$ ) × (1 +  $r_D$ ). To match a given default probability  $\alpha$ , EC is  $E_0$  chosen so that this expression matches  $\text{VaR}_{\alpha}(A_1)$ , the  $\alpha$  percentile of the final asset value. For a detailed discussion, see  $[1, 2]$ .

### References

- [1] Aziz, A. & Rosen, D. (2004). Capital allocation and RAPM, Professional Risk Manager (PRM) Handbook, Chapter III.0, PRMIA Publications.
- [2] Kupiec, P. (2002). *Calibrating Your Intuition: Capital* Allocation for Market and Credit Risk, Working paper 99/02, IMF, at http://www.imf.org/external/pubs/ft/wp/ 2002/wp0299.pdf.
- [3] Matten, C. (2000). Managing Bank Capital, Wiley, Chichester.
- [4] Merton, R.C. & Perold, A.F. (1993). Theory of risk capital in financial firms, Journal of Applied Corporate Finance 6(Fall), 16-32.

## **4 Economic Capital**

- [5] Perold, A.F. (2005). Capital allocation in financial firms, *Journal of Applied Corporate Finance* **17**(3), 110–118.
- [6] Rosen, D. (2004). Credit risk capital calculation, *Professional Risk Manager (PRM) Handbook*, Chapter III.B.6, PRMIA Publications.
- [7] Saita, F. (2004). Measuring risk-adjusted performances for credit risk, in *Frontiers of Performance Measurement in Banking and Finance*, G. de Laurentis, ed, Egea.

## **Related Articles**

**Copulas: Estimation**; **Economic Capital Allocation**; **Structural Default Risk Models**; **Riskadjusted Return on Capital (RAROC)**; **Stress Testing**; **Value-at-Risk**.

DAN ROSEN & DAVID SAUNDERS
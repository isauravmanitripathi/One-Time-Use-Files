# **Base Correlation**

In the Gaussian copula model (*see* **Gaussian Copula Model**) for pricing collateralized debt obligation (CDO) tranches, the most important input is the correlation parameter defining the degree of dependence among the defaults in the portfolio. Given singlename default probabilities implied by credit default swap spreads and recovery assumptions, the Gaussian copula model thus establishes a correspondence between this correlation parameter and the spreads of CDO tranches. Using an analogy with the notion of Black–Scholes implied volatility of an equity option, one can define a notion of implied correlation for CDO tranches. Different notions of "implied correlation" are possible, but the one which ended up being adopted by the market has been the notion of *base correlation*, explained later.

In early applications of the Gaussian copula approach for valuation of CDO tranches, market participants were using different correlations for different tranches, leading to a correlation skew, similar to the implied volatility skew observed in equity and index options. Typically, the market tends to use higher correlation for senior tranches. This way of associating different correlations for different tranches is called a *compound correlation* method. However, this compound correlation approach of pricing each tranche using a different flat correlation is not self consistent. For example, the total loss of all tranches from a whole capital structure CDO might not add up to the total loss of the underlying portfolio. Another problem is that the implied compound correlation might not be unique since the correspondence between the correlation parameter in the Gaussian copula model and the tranche spread is not one-to-one for mezzanine tranches.

A more recent market development is to treat a CDO tranche as a call or put spread on the total loss of the underlying portfolio. For example, long a 3–7% tranche protection on the standard North America credit default swap spread index (CDX) is equivalent to long a call option on the total loss with a strike price of 3% of the total notional amount of the underlying portfolio and short a call with a strike price of 7% of the total notional amount of the underlying portfolio. Then we just need to price all equity tranches with different detachment levels or simply different equity tranche size since the attachment for the equity tranche is always equal to zero. Correspondingly, the implied correlation could be given just for equity tranche with different tranche sizes or detachment levels. This way of quoting correlation and pricing CDOs by associating a correlation curve with different equity tranche sizes is called the *base correlation method* first introduced by J. P. Morgan.

To illustrate the base correlation method, we use simple synthetic CDO structures in which the investor of a given tranche provides default protection against the total loss (*L*) of a portfolio over a certain range [*B,B* + ] and over a time period of [0*, t*]. The loss function for the protection seller is as follows:

$$L(B, \Delta, t) = \begin{cases} 0, & L(t) \le B \\ L(t) - B, & B < L(t) \le B + \Delta \\ \Delta, & L(t) > B + \Delta \end{cases} \tag{1}$$

This is similar to an insurance contract with a deductible of *B* and a ceiling of *B* + . We can look at this payoff function from an option perspective. Figure 1 depicts the payoff function of a 5-tranche CDO against the total loss distribution. Buying a super senior tranche is equivalent to selling a call option on the total loss of the portfolio with a strike of the attachedment point of the super senior tranche. Buying an equity tranche is equivalent to selling a put option with the strike price equal to the equity size. The investor of any middle tranche is equivalent to having an option strategy of *spread* in which he/she is long a call option with strike price of *B* + and short a call with strike price of *B*. Looking at a tranche from this angle gives us alternative views to the properties of CDO tranches.

From valuation perspective, we just need to value both premium leg and loss protection leg. We assume that the accumulative tranche loss up to time *t* is *L<sup>T</sup> (t)*, with the attachment level *B* and the detachment level *B* + , and the tranche size is = *KU* − *KL*. If we ignore the interest rate impact, the payoff of the tranche [*B,B* + ] can be expressed as follows:

$$L(B, \Delta, t) = \max(L(t) - B, 0) - \max(L(t) - (B + \Delta), 0) \quad (2)$$

The expected tranche loss is the area of the excess loss distribution bounded by the subordination levels

![](_page_1_Figure_1.jpeg)

**Figure 1** Tranche loss vs total loss

*B* and *B* + if we ignore the interest rate. This can be taken as the difference of two equity tranche [0*, B* + ] and [0*, B*]. We can value them by simply attaching a correlation number to the tranche size or detachment point expressed by a base correlation. That is,

$$E[L(B, \Delta, t)] = E[\max(L(t) - B, 0)|\rho(B)]$$
$$- E[\max(L(t) - (B - \Delta), 0)|\rho(B + \Delta)]$$
(3)

However, the base correlation method does not guarantee absence of arbitrage. To make any credit portfolio model arbitrage free, we have the following necessary conditions around tranche loss function:

$$L(B, \Delta, t) < L(B', \Delta, t) \quad \text{if } B < B' \quad \text{and}$$
  
$$L(B, \Delta, t_1) < L(B, \Delta, t_2) \quad \text{if } t_1 < t_2 \tag{4}$$

That is, for two tranches with everything else equal except its attachment point, the one with the higher attachment should have lower expected loss; for two tranches with everything else equal except the time interval over which we study the loss, the loss should become bigger as we increase the length of time over which we study the loss.

We have observed that for two tranches with the same tranche size, the one with more support or higher attachment level could have a break-even spread higher than the one with a lower attachment level in the base correlation framework. In addition, the base correlation method along with the Gaussian copula model does not tell us too much about how to price nonindex portfolio tranches, neither more complicated structures such as CDO squared or CDO trades with both long and short credits as collaterals. We still need to use various loss mapping algorithms to derive a base correlation curve for the bespoke portfolio from the base correlation curve from an index tranche market.

The current market benchmark method is to use Gaussian copula function along with a base correlation method. In this framework, there is a one-to-one relationship between the tranche spread and implied base correlation curve. From a given set of index tranche spreads, we can use calibration to obtain a base correlation curve. Table 1 provides the market quote for CDX 9 on September 29, 2008 when the CDX 9 is 180 bps.

The base correlation graph is given in Figure 2.

Usually, the base correlation curve is an up sloping curve. Recently, owing to the high uncertainties in the financial market, we very often have trouble to calibrate a base correlation curve. We use a random recovery assumption to calibrate the base correlation curve. More importantly, we should incorporate the volatilities of the spreads into the framework, which has yet been formulated.

However, this base correlation approach does not tell us how to price bespoke portfolio tranches using a base correlation curve obtained from the index

| Swap Level<br>Attachment (%) | 180.00<br>Detachment (%) | Bid     | Offer    | Mid     | Base<br>correlation (%) |
|------------------------------|--------------------------|---------|----------|---------|-------------------------|
|                              |                          |         |          |         |                         |
| 3.00                         | 7.00                     | 1097.00 | 1 105.00 | 1101    | 40.16                   |
| 7.00                         | 10.00                    | 492.00  | 497.00   | 494 1/2 | 46.53                   |
| 10.00                        | 15.00                    | 199.00  | 204.00   | 201 1/2 | 59.77                   |
| 15.00                        | 30.00                    | 92.00   | 96.00    | 94      | 84.78                   |

**Table 1** CDX 9 market quote and base correlation curve as of 29 September 2008

![](_page_2_Figure_3.jpeg)

**Figure 2** Base correlation curve as of September 29, 2008

tranche market. Practitioners in the market employ various mapping algorithms on the basis of the bespoke portfolio loss characteristics relative to the index portfolio loss to derive a bespoke portfolio base correlation curve from the index tranche market's base correlation curve. We provide a summary here and some general comments.

In the original copula function framework, we intend to study a portfolio problem in two stages. First, we use a credit curve to describe a single name default property. Second, we use a copula function to describe the default correlation problem. The correlation structures and correlation parameters are independent from the magnitude of single name default probabilities. That is why, we say that the correlation parameter is more rank-type correlation, which provides an order of default. In practice we often use a single correlation parameter. We have to emphasize that it is not the original framework that allows a single correlation parameter, but simply a convenient choice made by practitioners so that it is easy to communicate with each other about the correlation.

Under these constraints, it is quite difficult to compare one credit portfolio against another credit portfolio with respect to the correlation. We simply try to link the correlation with the total loss distribution characteristics. Here are three most commonly used base correlation mapping methods.

### 1. **Normalized strike (NS)**

In this approach, we simply link the correlation on the basis of the expected loss of the portfolio. The intuitive idea is as follows: a mezzanine tranche of a bespoke credit portfolio with higher spreads should behave like an equity tranche of the index. Then we can use the following mapping approach

$$\rho_{\text{bespoke}}(K) = \rho_{\text{index}} \left[ \frac{EL_{\text{index}}}{EL_{\text{bespoke}}} \cdot K \right] \qquad (5)$$

This is easy to implement. However, it does not fully consider the dispersion of a credit portfolio relative to the index. A few credits with a higher spreads could distort the scaling substantially. In addition, comparing two portfolios in terms of their expected values is a very simplistic comparison.

### 2. **Normalized loss ratio**

This approach uses the equity tranche loss, instead of the portfolio expected loss only, for the base correlation mapping. The formula is as follows:

$$\frac{EL_{\text{bespoke}}[0, K] \text{ with } \rho_{\text{bespoke}}(K)}{EL_{\text{bespoke}}}$$
$$= \frac{EL_{\text{index}}[0, K] \text{ with } \rho_{\text{index}}(K)}{EL_{\text{index}}} \tag{6}$$

This is still easy to implement. It makes the use of equity tranches loss with different sizes in addition to the portfolio expected loss. From the comparison of two portfolios in terms of loss distribution perspective, it provides more detailed comparison than the normalized strike method, but still does not capture the loss variations within a tranche. Sometimes, it is impossible to find a solution for this method.

3. **Percentile-to-percentile loss distribution mapping**

$$\Pr(L_{\text{bespoke}} > K_{\text{bespoke}}; \rho_{\text{index}}(K))$$
  
=  $\Pr(L_{\text{index}} > K; \rho_{\text{index}}(K))$  (7)

This approach compares the loss distribution of bespoke portfolio against that of an index portfolio directly by the percentile-to-percentile comparison. We simply find a corresponding strike for the bespoke portfolio whose excess loss probability at the strike (to be solved) is equal to that of the index portfolio while both excess probabilities are calculated at the same index base correlation at the index strike level. From loss distribution comparison perspective, it provides the most comprehensive comparison. Both average spread and the dispersion of spread should be captured by this method.

Although all these mapping algorithms based on loss distribution are intuitive, none of them are fully theoretically justifiable. Without fully using individual name information such as asset return volatilities and correlations, it is difficult to compare one portfolio against another portfolio as we do in equity portfolio.

## **Further Reading**

- Li, D.X. (2000). On default correlation: a copula function approach, *Journal of Fixed Income* **9**, 41–50.
- McGinty, L., Eric B., Rishad, A. & Martin, W. (2004). Introducing base correlation, *Credit Derivative Strategy*, J.P. Morgan.

## **Related Articles**

**Collateralized Debt Obligations (CDO)**; **Default Time Copulas**; **Modeling Correlation of Structured Instruments in a Portfolio Setting**; **Gaussian Copula Model**; **Random Factor Loading Model (for Portfolio Credit)**.

DAVID XIANGLIN LI
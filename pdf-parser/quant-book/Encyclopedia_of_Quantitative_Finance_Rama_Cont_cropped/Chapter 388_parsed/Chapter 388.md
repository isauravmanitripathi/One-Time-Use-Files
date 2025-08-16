# **Catastrophe Bonds**

Catastrophe bonds (also called cat bonds) were developed to facilitate direct transfer of catastrophe insurance risk (see **Insurance Risk Models**) from (re)insurers (see **Reinsurance**) and corporations (referred to as sponsors for the cat bonds) to investors. As a market innovation in the form of insurance risk securitization, cat bonds were designed to protect sponsoring companies from financial losses caused by large natural catastrophes (such as hurricanes and earthquakes), as an alternative or supplement to traditional reinsurance (see Reinsurance). From the sponsor's perspective, the fully collateralized nature of cat bonds provides an important alternative source of capital capacity. From the investors' perspective, the past performances of cat bonds have been very attractive and cat bonds provide further diversification relative to the typical financial asset portfolios.

Cat losses covered under the cat bond are often characterized by a loss-exceedance curve,  $S(x) =$  $\Pr\{X > x\}$ , that is, the probability that the cat loss  $X$  will exceed amount  $x$ . Investors of a cat bond are generally provided with a loss-exceedance curve  $S(x)$  that is obtained either

- by running company exposure data through commercially available cat modeling software, or
- by designing payout functions along some parametric indicators (e.g., the Richter scale of an earthquake at a specified location, an aggregate industry loss index, etc.).

The following information is embedded in a lossexceedance curve  $S(x)$ :

- the expected frequency of default (see Credit Risk); and
- the recovery rate, given default.

As compensation for credit risks (see Credit Risk), cat bonds normally offer investors yields that are higher than the risk-free interest rate (e.g., the London interbank offered rate (LIBOR); see Bond). The excess yields spread over the riskfree rate should more than compensate for the expected default rate, since it should also contain risk load for uncertainties associated with the default risk.

For investors, it is desirable to compare the relative attractiveness of the yields spreads between cat bonds and corporate bonds. In order to compare riskadjusted performance of various asset classes, what is needed is a common yardstick that is applicable to all types of risks. For mutual funds (*see Mutual Funds*), a popular measure of risk-adjusted performance is the Sharpe ratio (see Capital Asset Pricing Model), namely, the excess return per unit of volatility. The Sharpe ratio works well for assets whose returns follow normal distributions. However, for a single cat bond issue, the traditional Sharpe ratio concept is not applicable since the asset return is skewed and with jumps: most of the probability mass is centered at zero loss, although there is a small probability of potentially large negative returns. Other pricing methods have been developed for cat bonds to capture the characteristics of cat bond losses.

## **Lane Pricing Model**

Lane [1] proposed the following model for the cat bond yields:

$$\text{EER} = \gamma (\text{PFL})^{\alpha} (\text{CEL})^{\beta} \tag{1}$$

where probability of first loss (PFL) is the expected annual frequency of incurring a loss. Conditional expected loss (CEL) represents the average severity as percentage of principal given that a loss occurs. Expected excess return (EER) represents the adjusted spread over LIBOR, further net of expected loss (that is, PFL  $\times$  CEL). EER represents the risk loading.

Lane showed that his model (1) fits reasonably well to empirical prices for a dozen CAT bond transactions in 1999–2000, for which the best-fit parameters were  $\gamma = 55\%$ ,  $\alpha = 49\%$ , and  $\beta = 57\%$ .

#### **Probability Transform Method**

Wang [2] establishes a pricing method by directly applying the following Wang transform to convert a loss curve *S* to a price curve  $S^*$ :

$$S^{*}(y) = t(\Phi^{-1}(S(y)) + \lambda)$$
(2)

where  $t$  represents Student- $t$  distribution with degree of freedom  $k$ . The difference in the areas between  $S^*$  and S constitutes the risk load. Based on the same 1999–2000 cat bond transaction data as in [1], the estimated parameters of Wang transform in

### **2 Catastrophe Bonds**

equation (2) are *λ* = 0*.*454 and the degree of freedom *k* = 5. Here the student-*t* factor is essential to capture the low frequency and high-severity characteristic of credit losses associated with cat bonds.

### **References**

[1] Lane, M.N. (2000). Pricing risk transfer transactions, *ASTIN Bulletin* **30**(2), 259–293.

[2] Wang, S.S. (2004). *Cat Bond Pricing Using Probability Transforms*. The Geneva Papers on Risk and Insurance– Issues and Practice.

### **Related Articles**

**Arbitrage Pricing Theory**; **Credit Risk**; **Bond**; **Insurance Risk Models**; **Mutual Funds**; **Reinsurance**.

SHAUN WANG
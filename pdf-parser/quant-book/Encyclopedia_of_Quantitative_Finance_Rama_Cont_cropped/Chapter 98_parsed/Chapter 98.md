# **Ouanto Options**

A quanto option can be any cash-settled option whose payoff is converted into a third currency at maturity at a prespecified rate, called the *quanto* factor. There can be quanto plain vanilla, quanto barriers, quanto forward starts, quanto corridors, and so on. The arbitrage pricing theory and the fundamental theorem of asset pricing, also covered for example in [3] and [2], allow the computation of option values. Other references include **Options:** Basic Definitions; Option Pricing: General Principles; Foreign Exchange Markets.

## Foreign Exchange Quanto Drift Adjustment

We take the example of a gold contract with underlying XAU/USD in XAU-USD quotation that is quantoed into EUR. Since the payoff is in EUR, we let EUR be the numeraire or domestic or base currency and consider a Black-Scholes model

$$XAU-EUR: dS_t^{(3)} = (r_{EUR} - r_{XAU})S_t^{(3)} dt + \sigma_3 S_t^{(3)} dW_t^{(3)}$$
(1)

USD-EUR: 
$$dS_t^{(2)} = (r_{\text{EUR}} - r_{\text{USD}})S_t^{(2)} dt$$

$$+ \sigma_2 S_t^{(2)} \, \mathrm{d} W_t^{(2)} \tag{2}$$

$$dW_t^{(3)}dW_t^{(2)} = -\rho_{23} dt \tag{3}$$

where we use a minus sign in front of the correlation, because both  $S^{(3)}$  and  $S^{(2)}$  have the same base currency (DOM), which is EUR in this case. The scenario is displayed in Figure 1. The actual underlying is then

XAU-USD: 
$$S_t^{(1)} = \frac{S_t^{(3)}}{S_t^{(2)}}$$
 (4)

Using Itô's formula, we first obtain

$$\begin{split} \mathbf{d}\frac{1}{S_t^{(2)}} &= -\frac{1}{(S_t^{(2)})^2} \mathbf{d}S_t^{(2)} + \frac{1}{2} \cdot 2 \cdot \frac{1}{(S_t^{(2)})^3} \left(\mathbf{d}S_t^{(2)}\right)^2 \\ &= (r_{\text{USD}} - r_{\text{EUR}} + \sigma_2^2) \frac{1}{S_t^{(2)}} \mathbf{d}t - \sigma_2 \frac{1}{S_t^{(2)}} \mathbf{d}W_t^{(2)} \end{split} \tag{5}$$

and hence

$$\begin{split} \mathrm{d}S_{t}^{(1)} &= \frac{1}{S_{t}^{(2)}} \, \mathrm{d}S_{t}^{(3)} + S_{t}^{(3)} \, \mathrm{d} \frac{1}{S_{t}^{(2)}} + \, \mathrm{d}S_{t}^{(3)} \, \mathrm{d} \frac{1}{S_{t}^{(2)}} \\ &= \frac{S_{t}^{(3)}}{S_{t}^{(2)}} (r_{\text{EUR}} - r_{\text{XAU}}) \, \mathrm{d}t + \frac{S_{t}^{(3)}}{S_{t}^{(2)}} \sigma_{3} \, \mathrm{d}W_{t}^{(3)} \\ &+ \frac{S_{t}^{(3)}}{S_{t}^{(2)}} (r_{\text{USD}} - r_{\text{EUR}} + \sigma_{2}^{2}) \, \mathrm{d}t \\ &- \frac{S_{t}^{(3)}}{S_{t}^{(2)}} \sigma_{2} \, \mathrm{d}W_{t}^{(2)} + \frac{S_{t}^{(3)}}{S_{t}^{(2)}} \rho_{23} \sigma_{2} \sigma_{3} \, \mathrm{d}t \\ &= (r_{\text{USD}} - r_{\text{XAU}} + \sigma_{2}^{2} + \rho_{23} \sigma_{2} \sigma_{3}) S_{t}^{(1)} \, \mathrm{d}t \\ &+ S_{t}^{(1)} (\sigma_{3} \, \mathrm{d}W_{t}^{(3)} - \sigma_{2} \, \mathrm{d}W_{t}^{(2)}) \end{split} \tag{6}$$

Since  $S_t^{(1)}$  is a geometric Brownian motion with volatility  $\sigma_1$ , we introduce a new Brownian motion  $W^{(1)}_{\cdot}$  and find

$$dS_t^{(1)} = (r_{\text{USD}} - r_{\text{XAU}} + \sigma_2^2 + \rho_{23}\sigma_2\sigma_3)S_t^{(1)} dt + \sigma_1 S_t^{(1)} dW_t^{(1)}$$
(7)

Now Figure 1 and the *law of cosine* imply

$$\sigma_3^2 = \sigma_1^2 + \sigma_2^2 - 2\rho_{12}\sigma_1\sigma_2 \tag{8}$$

$$\sigma_1^2 = \sigma_2^2 + \sigma_3^2 + 2\rho_{23}\sigma_2\sigma_3 \tag{9}$$

which yields

$$\sigma_2^2 + \rho_{23}\sigma_2\sigma_3 = \rho_{12}\sigma_1\sigma_2 \tag{10}$$

As explained in the *currency triangle* in Figure 1,  $\rho_{12}$  is the correlation between XAU-USD and USD-EUR, whence  $\rho \stackrel{\Delta}{=} -\rho_{12}$  is the correlation between XAU-USD and EUR-USD. Inserting this into equation  $(7)$ , we obtain the usual formula for the drift adjustment

$$dS_t^{(1)} = (r_{\text{USD}} - r_{\text{XAU}} - \rho \sigma_1 \sigma_2) S_t^{(1)} dt + \sigma_1 S_t^{(1)} dW_t^{(1)}$$
(11)

This is the **risk neutral pricing** process that can be used for the valuation of any derivative depending on  $S_t^{(1)}$ , which is quantoed into EUR.

![](_page_1_Figure_1.jpeg)

Figure 1 XAU-USD-EUR FX quanto triangle. The arrows point in the direction of the respective base currencies. The length of the edges represents the volatility. The cosine of the angles  $\cos \phi_{ij} = \rho_{ij}$  represents the correlation of the currency pairs  $S^{(i)}$  and  $S^{(j)}$ , if the base currency (DOM) of  $S^{(i)}$  is the underlying currency (FOR) of  $S^{(j)}$ . If both  $S^{(i)}$  and  $S^{(j)}$  have the same base currency (DOM), then the correlation is denoted by  $-\rho_{ij} = \cos(\pi - \phi_{ij})$ 

#### Extensions to Other Models

The previous derivation can be extended to the case of term-structure of volatility and correlation. However, introduction of volatility smile would distort the relationships. Nevertheless, accounting for smile effects is important in real-market scenarios. See Foreign Exchange Smiles and Foreign **Exchange Smile Interpolation** for details. To do this, one could, for example, capture the smile for a multicurrency model with a *weighted Monte Carlo technique* as described in [1]. This would still allow to use the previous result.

#### **Ouanto Vanilla**

Common among foreign exchange options is a quanto plain vanilla paying

$$Q[\phi(S_T - K)]^+ \tag{12}$$

where K denotes the strike, T the expiration time,  $\phi$ the usual put-call indicator taking the value  $+1$  for a call and  $-1$  for a put, S the underlying in FOR-DOM quotation, and  $Q$  the quanto factor from the domestic currency into the quanto currency. We let

$$\tilde{\mu} \stackrel{\Delta}{=} r_{\rm d} - r_{\rm f} - \rho \sigma \tilde{\sigma} \tag{13}$$

be the *adjusted drift*, where  $r_{\rm d}$  and  $r_{\rm f}$  denote the riskfree rates of the domestic and foreign underlying currency pair, respectively,  $\sigma = \sigma_1$  the volatility of this currency pair,  $\tilde{\sigma} = \sigma_2$  the volatility of the currency pair DOM-OUANTO, and

$$\rho = \frac{\sigma_3^2 - \sigma^2 - \tilde{\sigma}^2}{2\sigma\tilde{\sigma}} \tag{14}$$

the correlation between the currency pairs FOR-DOM and DOM-QUANTO in this quotation. Furthermore, we let  $r_0$  be the risk-free rate of the quanto currency. With the same principles as in **pricing for**mulae for foreign exchange options, we can derive the formula for the value as

$$v = Q e^{-r_{\mathbb{Q}}T} \phi [S_0 e^{\tilde{\mu}T} \mathcal{N}(\phi d_+) - K \mathcal{N}(\phi d_-)] \tag{15}$$

$$d_{\pm} = \frac{\ln\frac{3_0}{K} + \left(\tilde{\mu} \pm \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}\tag{16}$$

where  $\mathcal{N}$  denotes the cumulative standard normal distribution function and  $n$  its density.

#### **Quanto Forward**

Similarly, we can easily determine the value of a quanto forward paying

$$Q[\phi(S_T - K)] \tag{17}$$

where K denotes the strike, T the expiration time,  $\phi$ the usual long-short indicator,  $S$  the underlying in FOR-DOM quotation, and  $O$  the quanto factor from the domestic currency into the quanto currency. Then the formula for the value can be written as

$$v = Q e^{-r_Q T} \phi [S_0 e^{\hat{\mu}T} - K] \tag{18}$$

This follows from the vanilla quanto value formula by taking both the normal probabilities to be 1. These normal probabilities are exercise probabilities under some measure. Since a forward contract is always exercised, both these probabilities must be equal to 1.

### **Quanto Digital**

A European-style quanto digital pays

$$QI\!I_{\{\phi S_T \ge \phi K\}} \tag{19}$$

**Table 1** Example of a quanto digital put. The buyer receives 100 000 EUR if at maturity, the European Central Bank fixing for USD–JPY (computed *via* EUR–JPY and EUR–USD) is below 108.65. Terms were created on January 12, 2004 with the following market data: USD–JPY spot reference 106.60, USD–JPY at-the-money volatility 8.55%, EUR–JPY at-the-money volatility 6.69%, EUR–USD at-the-money volatility 10.99% (corresponding to a correlation of −27.89% for USD–JPY against JPY–EUR), USD rate 2.5%, JPY rate 0.1%, and EUR rate 4%

| Notional               | 100 000 EUR           |  |  |
|------------------------|-----------------------|--|--|
| Maturity               | 3 months (92 days)    |  |  |
| European-style barrier | 108.65 USD–JPY        |  |  |
| Theoretical value      | 71 555 EUR            |  |  |
| Fixing source          | European Central Bank |  |  |

where *K* denotes the strike, *ST* is the spot of the currency pair FOR–DOM at maturity *T* , *φ* takes the values +1 for a digital call and −1 for a digital put, and *Q* is the prespecified conversion rate from the domestic to the quanto currency. The valuation of the European-style quanto digitals follows the same principle as in the quanto vanilla option case. The value is

$$v = Q e^{-r_Q T} \mathcal{N}(\phi d_-) \tag{20}$$

We provide an example of a European-style digital put in USD/JPY quantoed into EUR in Table 1.

## **Hedging of Quanto Options**

Hedging of quanto options can be done by running a multicurrency options book. All the usual Greeks can be hedged. **Delta hedging** is done by trading in the underlying spot market. An exception is the **correlation risk**, which can only be hedged with other derivatives depending on the same correlation. This is often difficult to do in practice. In FX, the correlation risk can be translated into vega positions as shown in [4, 5] or in **Foreign Exchange Basket Options**. We now illustrate this approach for quanto plain vanilla options.

#### *Vega Positions of Quanto Plain Vanilla Options*

Starting from equation (15), we obtain the sensitivities

$$\frac{\partial v}{\partial \sigma} = Q S_0 e^{(\tilde{\mu} - r_Q)T} \left[ n(d_+) \sqrt{T} - \phi \mathcal{N}(\phi d_+) \rho \tilde{\sigma} T \right],$$

$$\begin{split} \frac{\partial v}{\partial \tilde{\sigma}} &= -Q S_0 \mathrm{e}^{(\tilde{\mu}-r_Q)T} \phi \mathcal{N}(\phi d_+) \rho \sigma T, \\ \frac{\partial v}{\partial \rho} &= -Q S_0 \mathrm{e}^{(\tilde{\mu}-r_Q)T} \phi \mathcal{N}(\phi d_+) \sigma \tilde{\sigma} T, \\ \frac{\partial v}{\partial \sigma_3} &= \frac{\partial v}{\partial \rho} \frac{\partial \rho}{\partial \sigma_3} \\ &= \frac{\partial v}{\partial \rho} \frac{\sigma_3}{\sigma \tilde{\sigma}} \\ &= -Q S_0 \mathrm{e}^{(\tilde{\mu}-r_Q)T} \phi \mathcal{N}(\phi d_+) \sigma \tilde{\sigma} T \frac{\sigma_3}{\sigma \tilde{\sigma}} \\ &= -Q S_0 \mathrm{e}^{(\tilde{\mu}-r_Q)T} \phi \mathcal{N}(\phi d_+) \sigma_3 T \\ &= -Q S_0 \mathrm{e}^{(\tilde{\mu}-r_Q)T} \phi \mathcal{N}(\phi d_+) \sqrt{\sigma^2 + \tilde{\sigma}^2 + 2\rho \sigma \tilde{\sigma}} T \end{split} \tag{21}$$

Note that the computation is standard calculus and repeatedly uses the identity

$$S_0 e^{\tilde{\mu}T} n(\phi d_+) = K n(\phi d_-) \tag{22}$$

The understanding of these greeks is that *σ* and *σ*˜ are both risky parameters, independent of each other. The third independent risk is either *σ*<sup>3</sup> or *ρ*, depending on what is more likely to be known.

This shows exactly how the three vega positions can be hedged with plain vanilla options in all the three legs, provided there is a liquid vanilla options market in all the three legs. In the example with XAU–USD–EUR, the currency pairs XAU–USD and EUR–USD are traded; however, there is no liquid vanilla market in XAU–EUR. Therefore, the correlation risk remains unhedgeable. Similar statements would apply for quantoed stocks or stock indices. However, in FX, there are situations with all the legs being hedgeable, for instance, EUR–USD–JPY.

The signs of the vega positions are not uniquely determined in all the legs. The FOR–DOM vega is smaller than the corresponding vanilla vega in the case of a call and positive correlation or put and negative correlation, and larger in case of a put and positive correlation or call and negative correlation. The DOM–QUANTO vega takes the sign of the correlation in case of a call and its opposite sign in case of a put. The FOR–QUANTO vega takes the opposite sign of the put–call indicator *φ*.

We provide an example of pricing and vega hedging scenario in Table 2, where we notice that the dominating vega risk comes from the FOR–DOM pair, whence most of the risk can be hedged.

|                        |                    | Data set 1 | Data set 2 | Data set 3 |
|------------------------|--------------------|------------|------------|------------|
| FX pair                | FOR–DOM            | XAU–USD    | XAU–USD    | XAU–USD    |
| Spot                   | FOR–DOM            | 800.00     | 800.00     | 800.00     |
| Strike                 | FOR–DOM            | 810.00     | 810.00     | 810.00     |
| Quanto                 | DOM–QUANTO         | 1.0000     | 1.0000     | 1.0000     |
| Volatility             | FOR–DOM            | 10.00%     | 10.00%     | 10.00%     |
| Quanto volatility      | DOM–QUANTO         | 12.00%     | 12.00%     | 12.00%     |
| Correlation            | FOR–DOM–DOM–QUANTO | 25.00%     | 25.00%     | −75.00%    |
| Domestic interest rate | DOM                | 2.0000%    | 2.0000%    | 2.0000%    |
| Foreign interest rate  | FOR                | 0.5000%    | 0.5000%    | 0.5000%    |
| Quanto currency rate   | Q                  | 4.0000%    | 4.0000%    | 4.0000%    |
| Time in years          | T                  | 1          | 1          | 1          |
| 1 = call −1 = put      | FOR                | 1          | −1         | 1          |
| Quanto vanilla option  | Value              | 30.81329   | 31.28625   | 35.90062   |
| Quanto vanilla option  | Vega FOR–DOM       | 298.14188  | 321.49308  | 350.14600  |
| Quanto vanilla option  | Vega DOM–QUANTO    | −10.07056  | 9.38877    | 33.38797   |
| Quanto vanilla option  | Vega FOR–QUANTO    | −70.23447  | 65.47953   | −35.61383  |
| Quanto vanilla option  | Correlation risk   | −4.83387   | 4.50661    | −5.34207   |
| Quanto vanilla option  | Vol FOR–QUANTO     | 17.4356%   | 17.4356%   | 8.0000%    |
| Vanilla option         | Value              | 32.6657    | 30.7635    | 32.6657    |
| Vanilla option         | Vega               | 316.6994   | 316.6994   | 316.6994   |
|                        |                    |            |            |            |

**Table 2** Example of a quanto plain vanilla

## **Applications**

The standard applications are performance-linked deposits or performance notes as in [6]. Any time the performance of an underlying asset needs to be converted into the notional currency invested, and the exchange rate risk is with the seller, we need a quanto product. Naturally, an underlying like gold, which is quoted in USD, would be a default candidate for a quanto product, when the investment is in a currency other than USD.

#### *Performance-linked Deposits*

A performance-linked deposit is a deposit with a participation in an underlying market. The standard is that a GBP investor waives her coupon that the money market would pay and instead buys a EUR–GBP call with the same maturity date as the coupon, strike *K* and notional *N* in EUR. These parameters have to be chosen in such a way that the offer price of the EUR call equals the money market interest rate plus the sales margin. The strike is often chosen to be the current spot. The notional is often a percentage *p* of the deposit amount *A*, such as 50 or 25%. The annual coupon paid to the investor is then a predefined minimum coupon plus the participation

$$p \cdot \frac{\max[S_T - S_0, 0]}{S_0} \tag{23}$$

which is the return of the exchange rate viewed as an asset, where the investor is protected against negative returns. So, obviously, the investor buys a EUR call GBP put with strike *K* = *S*<sup>0</sup> and notional *N* = *pA* GBP or *N* = *pA/S*<sup>0</sup> EUR. Thus, if the EUR goes up by 10% against the GBP, the investor gets a coupon of *p* · 10% per annum in addition to the minimum coupon.

**Example 1** We consider the example shown in Table 3. In this case, if the EUR–GBP spot fixing is 0.7200, the additional coupon would be 0.8571% per annum. The breakeven point is at 0.7467, so this product is advisable for a very strong EUR bullish view. For a weakly bullish view, an alternative would

Table 3 Example of a performance-linked deposit, where the investor is paid  $30\%$  of the EUR-GBP return. Note that in GBP the day count convention in the money market is  $\text{act}^{(a)}/365$  rather than  $\text{act}/360$ 

| $5\,000\,000$ GBP                                                     |
|-----------------------------------------------------------------------|
| 3 June 2005                                                           |
| 2 September 2005 (91 days)                                            |
| 91                                                                    |
|                                                                       |
| $4.00\% \text{ act/365}$                                              |
|                                                                       |
| 0.7000                                                                |
|                                                                       |
| 2.00% act/365                                                         |
| $30\% \cdot \frac{100 \max[S_T - 0.7000, 0]}{0.7000} \text{ act/365}$ |
|                                                                       |
| EUR-GBP fixing on 31 August<br>2005 (88 days)                         |
| FCR                                                                   |
|                                                                       |

 $^{(a)}(act = actual number of days)$ 

be to buy an up-and-out call with barrier at 0.7400 and 75% participation, where we would find the best case to be 0.7399 with an additional coupon of 4.275% per annum, which would lead to a total coupon of 6.275% per annum.

#### Composition

- From the money market we get 49863.01 GBP . at the maturity date.
- The investor buys a EUR call GBP put with strike 0.7000 and with notional 1.5 million GBP.
- The offer price of the call is 26220.73 GBP, assuming a volatility of 8.0% and a EUR rate of 2.50%.
- The deferred premium is 24 677.11 GBP.
- The investor receives a minimum payment of 24 931.51 GBP.
- Subtracting the deferred premium and the minimum payment from the money market leaves a sales margin of 254.40 GBP (which is extremely poor).
- Note that the option the investor is buying must be cash-settled.

Variations. There are many variations of the performance-linked notes. Of course, one can think of the European style knock-out calls or window-barrier calls. For a participation in a downward trend, the investor can buy puts. One of the frequent issues in

foreign exchange, however, is the deposit currency being different from the domestic currency of the exchange rate, which is quoted in FOR-DOM (foreign-domestic), meaning how many units of domestic currency are required to buy one unit of foreign currency. So, if we have a EUR investor who wishes to participate in a EUR-USD movement, we need to *quanto* the *domestic* payoff currency (USD) into the foreign currency (EUR). The payoff of the EUR call USD put

$$[S_T - K]^+ \tag{24}$$

is in domestic currency (USD). Of course, this payoff can be converted into the foreign currency (EUR) at maturity, but the question is, at what rate? If we convert at rate  $S_T$ , which is what we could do in the spot market at no cost, then the investor buys a vanilla EUR call. But here, the investor receives a coupon given by

$$p \cdot \frac{\max[S_T - S_0, 0]}{S_T} \tag{25}$$

If the investor wishes to have performance of equation  $(23)$  rather than equation  $(25)$ , then the payoff at maturity is converted at a rate of 1.0000 into EUR, and this rate is set at the beginning of the trade. This is the *quanto factor*, and the vanilla is actually a *self*quanto vanilla, that is, a EUR call USD put, cash settled in EUR, where the payoff in USD is converted into EUR at a rate of 1.0000. This self-quanto vanilla can be valued by inverting the exchange rate, that is, looking at USD-EUR. This way the valuation can incorporate the smile of EUR-USD.

Similar considerations need to be taken into account if the currency pair to participate in does not contain the deposit currency at all. A typical situation is a EUR investor, who wishes to participate in the gold price, which is measured in USD, so the investor needs to buy a XAU call USD put quantoed into EUR. So the investor is promised a coupon as in equation  $(23)$  for a XAU–USD underlying, where the coupon is paid in EUR; this implicitly means that we must use a quanto plain vanilla with a quanto factor of 1,0000.

#### References

[1] Avellaneda, M., Buff, R., Friedman, C., Grandechamp, N., Kruk, L. & Newman, J. (2001). Weighted Monte Carlo: a new technique for calibrating asset-pricing models, *International Journal of Theoretical and Applied Finance* **4**(1), 91–119.

- [2] Hakala, J. & Wystup, U. (2002). *Foreign Exchange Risk*, Risk Publications, London.
- [3] Shreve, S.E. (2004). *Stochastic Calculus for Finance I*+*II*, Springer.
- [4] Wystup, U. (2001). *How the Greeks would have hedged correlation risk of foreign exchange options*, Wilmott Research Report, August 2001.
- [5] Wystup, U. (2002). How the Greeks would have hedged correlation risk of foreign exchange options, in *Foreign Exchange Risk*, Risk Publications, London.
- [6] Wystup, U. (2006). *FX Options and Structured Products*, Wiley Finance Series.

## **Related Articles**

**Black–Scholes Formula**; **Foreign Exchange Markets**; **Foreign Exchange Options**.

UWE WYSTUP
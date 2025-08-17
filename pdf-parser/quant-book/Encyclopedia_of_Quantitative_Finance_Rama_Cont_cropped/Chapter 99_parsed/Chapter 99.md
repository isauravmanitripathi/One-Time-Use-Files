# **Vanna–Volga Pricing**

The vanna–volga method, also called the *traders' rule of thumb*, is an empirical procedure that can be used to infer an implied-volatility smile from three available quotes for a given maturity. It is based on the construction of locally replicating portfolios whose associated hedging costs are added to corresponding Black–Scholes prices to produce smileconsistent values. Besides being intuitive and easy to implement, this procedure has a clear financial interpretation, which further supports its use in practice. In fact, SuperDerivatives has implemented a type of this method in their pricing platform, as one can read in the patent that SuperDerivatives has filed.

The vanna–volga method is commonly used in foreign exchange options markets, where three main volatility quotes are typically available for a given market maturity: the delta-neutral straddle, referred to as *at-the-money* (*ATM*); the risk reversal (RR) for 25 delta call and put; and the (vega-weighted) butterfly (BF) with 25 delta wings. The application of vanna–volga pricing allows us to derive implied volatilities for any option's delta, in particular for those outside the basic range set by the 25 delta put and call quotes. The notion of risk reversals and butterflies is explained in the article on foreign exchange (FX) market terminology (*see* **Foreign Exchange Markets**).

In the financial literature, the vanna–volga approach was introduced by Lipton and McGhee in [2], who compare different approaches to the pricing of double-no-touch (DNT) options, and by Wystup in [5], who describes its application to the valuation of one-touch (OT) options. The vanna–volga procedure is reviewed in more detail and some important results concerning the tractability of the method and its robustness are derived by Castagna and Mercurio in [1].

The following is based on the section *Traders' Rule of Thumb* by Wystup in [6].

The traders' rule of thumb is a method of traders to determine the cost of risk managing the volatility risk of exotic options with vanilla options. This cost is then added to the theoretical value (*TV*) in the Black–Scholes model and is called the *overhedge*. We explain the rule and then consider an example of a one-touch option.

Delta and vega are the most relevant sensitivity parameters for FX options maturing within one year. A delta-neutral position can be achieved by trading the spot. Changes in the spot are explicitly allowed in the Black–Scholes model. Therefore, model and practical trading have very good control over spot change risk. The more sensitive part is the vega position. This is not taken care of in the Black–Scholes model. Market participants need to trade other options to obtain a vega-neutral position. However, even a vega-neutral position is subject to changes of spot and volatility. For this reason, the sensitivity parameters *vanna* (change of vega due to change of spot) and *volga* (change of vega due to change of volatility) are of special interest. Vanna is also called *d vega/d spot*, volga is also called *d vega/d vol*. The plots for vanna and volga for a vanilla option are displayed in Figures 1 and 2. In this section, we outline how the cost of such a vanna and volga exposure can be used to obtain prices for options that are closer to the market than their theoretical Black–Scholes value.

## **Cost of Vanna and Volga**

We fix the rates *rd* and *rf* , the time to maturity *T* , and the spot *x* and define

cost of vanna 
$$\stackrel{\Delta}{=}$$
 exotic vanna ratio

× value of RR (1)

cost of volga = exotic volga ratio

× value of BF (2)

exotic vanna ratio 
$$\stackrel{\Delta}{=} B_{\sigma x}/RR_{\sigma x}$$
 (3)

exotic volga ratio = *Bσ σ /*BF*σ σ* (4)

value of 
$$\text{RR} \stackrel{\Delta}{=} [\text{RR}(\sigma_{\Delta}) - \text{RR}(\sigma_0)]$$
 (5)

value of BF 
$$\stackrel{\Delta}{=}$$
 [BF( $\sigma_{\Delta}$ ) – BF( $\sigma_{0}$ )] (6)

where *σ*<sup>0</sup> denotes the ATM (forward) volatility and *σ* denotes the wing volatility at the delta pillar , and *B* denotes the value function of a given exotic option. The values of risk reversals and butterflies are defined by

![](_page_1_Figure_1.jpeg)

Figure 1 Vanna of a vanilla option as a function of spot and time to expiration, showing the skew symmetry about the at-the-money line

![](_page_1_Figure_3.jpeg)

Figure 2 Volga of a vanilla option as a function of spot and time to expiration, showing the symmetry about the at-the-money line

$$RR(\sigma) \stackrel{\Delta}{=} call(x, \Delta, \sigma, r_d, r_f, T) - put(x, \Delta, \sigma, r_d, r_f, T)$$
(7)  
$$BF(\sigma) \stackrel{\Delta}{=} \frac{call(x, \Delta, \sigma, r_d, r_f, T) + put(x, \Delta, \sigma, r_d, r_f, T)}{2} - \frac{call(x, \Delta_0, \sigma_0, r_d, r_f, T) + put(x, \Delta_0, \sigma_0, r_d, r_f, T)}{2}$$
(8)

where vanilla $(x, \Delta, \sigma, r_d, r_f, T)$  means vanilla $(x, K,$  $\sigma, r_d, r_f, T$ ) for a strike K chosen to imply |vanilla<sub>x</sub>  $(x, K, \sigma, r_d, r_f, T) = \Delta$  and  $\Delta_0$  is the delta that produces the ATM strike. To summarize, we abbreviate

$$\mathsf{c}(\sigma_{\Delta}^{+}) \stackrel{\Delta}{=} \mathsf{call}(x, \Delta^{+}, \sigma_{\Delta}^{+}, r_{d}, r_{f}, T) \tag{9}$$

$$\mathsf{p}(\sigma_{\Delta}^{-}) \stackrel{\Delta}{=} \mathsf{put}(x,\,\Delta^{-},\,\sigma_{\Delta}^{-},\,r_{d},\,r_{f},\,T) \tag{10}$$

and obtain

cost of vanna

$$= \frac{B_{\sigma x}}{c_{\sigma x}(\sigma_{\Delta}^{+}) - p_{\sigma x}(\sigma_{\Delta}^{-})} \times \left[ c(\sigma_{\Delta}^{+}) - c(\sigma_{0}) - p(\sigma_{\Delta}^{-}) + p(\sigma_{0}) \right] \tag{11}$$

cost of volga

$$= \frac{2B_{\sigma\sigma}}{c_{\sigma\sigma}(\sigma_{\Delta}^{+}) + p_{\sigma\sigma}(\sigma_{\Delta}^{-})} \times \left[\frac{c(\sigma_{\Delta}^{+}) - c(\sigma_{0}) + p(\sigma_{\Delta}^{-}) - p(\sigma_{0})}{2}\right] \quad (12)$$

where we note that volga of the butterfly should actually be

$$\frac{1}{2} \left[ c_{\sigma\sigma}(\sigma_{\Delta}^{+}) + p_{\sigma\sigma}(\sigma_{\Delta}^{-}) - c_{\sigma\sigma}(\sigma_{0}) - p_{\sigma\sigma}(\sigma_{0}) \right] \tag{13}$$

but the last two summands are close to zero. The vanna-volga adjusted value of the exotic is then

$$B(\sigma_0) + p \times \text{[cost of vanna + cost of volga]}$$
 (14)

A division by the spot  $x$  converts everything into the usual quotation of the price in per cent of the underlying currency. The cost of vanna and volga is commonly adjusted by a number  $p \in [0, 1]$ , which is often taken to be the risk-neutral no-touch (NT) probability. The reason is that in the case of options that can knock out, the hedge is not needed anymore once the option has knocked out. The exact choice of  $p$  depends on the product to be priced; see Table 1. Taking  $p = 1$  as the default value would lead to overestimated overhedges for DNT options as pointed out in  $[2]$ .

The values of risk reversals and butterflies in equations  $(11)$  and  $(12)$  can be approximated by a first-order expansion as follows. For a risk reversal, we take the difference of the call with correct implied volatility and the call with ATM volatility minus the difference of the put with correct implied volatility and the put with ATM volatility. It is easy to see that this can be well-approximated by the vega of the ATM vanilla times the risk reversal in terms of volatility. Similarly, the cost of the butterfly can be approximated by the vega of the ATM volatility times the butterfly in terms of volatility. In formulae, this is

$$\begin{split} \mathsf{c}(\sigma_{\Delta}^{+}) - \mathsf{c}(\sigma_{0}) - \mathsf{p}(\sigma_{\Delta}^{-}) + \mathsf{p}(\sigma_{0}) \\ &\approx \mathsf{c}_{\sigma}(\sigma_{0})(\sigma_{\Delta}^{+} - \sigma_{0}) - \mathsf{p}_{\sigma}(\sigma_{0})(\sigma_{\Delta}^{-} - \sigma_{0}) \\ &= \sigma_{0}[\mathsf{p}_{\sigma}(\sigma_{0}) - \mathsf{c}_{\sigma}(\sigma_{0})] + \mathsf{c}_{\sigma}(\sigma_{0})[\sigma_{\Delta}^{+} - \sigma_{\Delta}^{-}] \\ &= \mathsf{c}_{\sigma}(\sigma_{0})\mathsf{RR} \end{split} \tag{15}$$

and, similarly,

$$\frac{\mathsf{c}(\sigma_{\Delta}^{+}) - \mathsf{c}(\sigma_{0}) + \mathsf{p}(\sigma_{\Delta}^{-}) - \mathsf{p}(\sigma_{0})}{2}$$
$$\approx \mathsf{c}_{\sigma}(\sigma_{0})\mathsf{BF} \tag{16}$$

Table 1 Adjustment factors for the overhedge for firstgeneration exotics

| Option       | p                                                                                               |
|--------------|-------------------------------------------------------------------------------------------------|
| KO           | No-touch probability                                                                            |
| RKO          | No-touch probability                                                                            |
| DKO          | No-touch probability                                                                            |
| OT           | $0.9 \times$ no-touch probability $- 0.5 \times$ bid-offer-<br>spread $\times$ (TV $-$ 33%)/66% |
| $\text{DNT}$ | 0.5                                                                                             |

KO, knock out; RKO, reverse knockout; DKO, double knockout; OT, one touch; DNT, double no touch

With these approximations, we obtain the formulae

$$\text{cost of vanna} \approx \frac{B_{\sigma x}}{c_{\sigma x}(\sigma_{\Delta}^{+}) - p_{\sigma x}(\sigma_{\Delta}^{-})} c_{\sigma}(\sigma_{0}) \text{RR} \quad (17)$$

$$\text{cost of volga} \approx \frac{2B_{\sigma\sigma}}{c_{\sigma\sigma}(\sigma_{\Delta}^{+}) + p_{\sigma\sigma}(\sigma_{\Delta}^{-})} c_{\sigma}(\sigma_{0}) \text{BF} \quad (18)$$

## Observations

- 1. The price supplements are linear in butterflies and risk reversals. In particular, there is no cost of vanna supplement if the risk reversal is zero and no cost of volga supplement if the butterfly is zero.
- 2. The price supplements are linear in the ATM vanilla vega. This means supplements grow with growing volatility change risk of the hedge instruments.
- 3. The price supplements are linear in vanna and volga of the given exotic option.
- 4. We have not observed any relevant difference between the exact method and its first-order approximation. Since the computation time for the approximation is shorter, we recommend using the approximation.
- 5. It is not clear up front which target delta to use for the butterflies and risk reversals. We take a delta of 25% merely on the basis of its liquidity.
- 6. The prices for vanilla options are consistent with the input volatilities as shown in Figures 3, 4, and  $5$ .
- 7. The method assumes a zero volga of risk reversals and a zero vanna of butterflies. This way the two sources of risk can be decomposed and hedged with risk reversals and butterflies. However, the assumption is actually not exact. For this reason, the method should be used with a lot of care. It causes traders and financial engineers to keep adding exceptions to the standard method

## **Consistency Check**

A minimum requirement for the vanna-volga pricing to be correct is the consistency of the method with vanilla options. We show in Figures 3, 4, and 5 that

![](_page_3_Figure_1.jpeg)

Figure 3 Consistency check of vanna-volga pricing. Vanilla option smile for a one-month maturity EUR/USD call, spot = 0.9060,  $r_d = 5.07\%$ ,  $r_f = 4.70\%$ ,  $\sigma_0 = 13.35\%$ ,  $\sigma_{\Lambda}^{+} = 13.475\%, \sigma_{\Lambda}^{-} = 13.825\%$ 

![](_page_3_Figure_3.jpeg)

Figure 4 Consistency check of vanna-volga pricing. Vanilla option smile for a one-year maturity EUR/USD call, spot = 0.9060,  $r_d = 5.07\%$ ,  $r_f = 4.70\%$ ,  $\sigma_0 = 13.20\%$ ,  $\sigma_{\Lambda}^{+} = 13.425\%, \, \sigma_{\Lambda}^{-} = 13.575\%$ 

the method does, in fact, yield a typical foreign exchange smile shape and produces the correct input volatilities ATM and at the delta pillars. We will now prove the consistency in the following way. Since the

![](_page_3_Figure_6.jpeg)

Figure 5 Consistency check of vanna-volga pricing. Vanilla option smile for a one-year maturity EUR/USD call, spot = 0.9060,  $r_d = 5.07\%$ ,  $r_f = 4.70\%$ ,  $\sigma_0 = 13.20\%$ ,  $\sigma_{\Lambda}^{+} = 13.425\%, \, \sigma_{\Lambda}^{-} = 13.00\%$ 

input consists only of three volatilities (ATM and two delta pillars), it would be too much to expect that the method produces correct representation of the entire volatility matrix. We can only check if the values for ATM and target- $\Delta$  puts and calls are reproduced correctly. To verify this, we check if the values for an ATM call, a risk reversal, and a butterfly are priced correctly. Of course, we only expect approximately correct results. Note that the number  $p$  is taken to be 1, which agrees with the risk-neutral NT probability for vanilla options.

For an ATM call, vanna and volga are approximately zero, and hence there are no supplements due to vanna or volga cost.

For a target- $\Delta$  risk reversal,

$$c(\sigma_{\Delta}^{+}) - p(\sigma_{\Delta}^{-}) \tag{19}$$

we obtain

cost of vanna

$$= \frac{\mathsf{c}_{\sigma x}(\sigma_{\Delta}^{+}) - \mathsf{p}_{\sigma x}(\sigma_{\Delta}^{-})}{\mathsf{c}_{\sigma x}(\sigma_{\Delta}^{+}) - \mathsf{p}_{\sigma x}(\sigma_{\Delta}^{-})}$$
$$\times \left[ \mathsf{c}(\sigma_{\Delta}^{+}) - \mathsf{c}(\sigma_{0}) - \mathsf{p}(\sigma_{\Delta}^{-}) + \mathsf{p}(\sigma_{0}) \right]$$
$$= \mathsf{c}(\sigma_{\Delta}^{+}) - \mathsf{c}(\sigma_{0}) - \mathsf{p}(\sigma_{\Delta}^{-}) + \mathsf{p}(\sigma_{0}) \qquad (20)$$

cost of volga

$$= \frac{2[\mathbf{c}_{\sigma\sigma}(\sigma_{\Delta}^{+}) - \mathbf{p}_{\sigma\sigma}(\sigma_{\Delta}^{-})]}{\mathbf{c}_{\sigma\sigma}(\sigma_{\Delta}^{+}) + \mathbf{p}_{\sigma\sigma}(\sigma_{\Delta}^{-})} \times \left[\frac{\mathbf{c}(\sigma_{\Delta}^{+}) - \mathbf{c}(\sigma_{0}) + \mathbf{p}(\sigma_{\Delta}^{-}) - \mathbf{p}(\sigma_{0})}{2}\right] (21)$$

and observe that the cost of vanna yields a perfect fit and the cost of volga is small, because in the first fraction we divide the difference of two quantities by the sum of the quantities, which are all of the same order.

For a target- $\Delta$  butterfly

$$\frac{c(\sigma_{\Delta}^{+}) + p(\sigma_{\Delta}^{-})}{2} - \frac{c(\sigma_{0}) + p(\sigma_{0})}{2} \tag{22}$$

we analogously obtain a perfect fit for the cost of volga and

cost of vanna

$$= \frac{c_{\sigma x}(\sigma_{\Delta}^{+}) - p_{\sigma x}(\sigma_{0}) - [c_{\sigma x}(\sigma_{0}) - p_{\sigma x}(\sigma_{\Delta}^{-})]}{c_{\sigma x}(\sigma_{\Delta}^{+}) - p_{\sigma x}(\sigma_{0}) + [c_{\sigma x}(\sigma_{0}) - p_{\sigma x}(\sigma_{\Delta}^{-})]} \times \left[c(\sigma_{\Delta}^{+}) - c(\sigma_{0}) - p(\sigma_{\Delta}^{-}) + p(\sigma_{0})\right]$$
(23)

which is again small.

The consistency can actually fail for certain parameter scenarios. This is one of the reasons that the traders' rule of thumb has been criticized repeatedly by a number of traders and researchers.

We introduce the abbreviations for first generation exotics listed as below.

KO, knock-out; KI, knock-in; RKO, reverse knock-out; RKI, reverse knock-in; DKO, double knock-out; OT, one-touch; NT, no-touch; DOT, double one-touch; DNT, double no-touch.

#### **Adjustment Factor**

The factor  $p$  has to be chosen in a suitable fashion. Since there is no mathematical justification or indication, there is a lot of dispute in the market about this choice. Moreover, the choices may also vary over time. An example for one of many possible choices of  $p$  is presented in Table 1.

For options with strike  $K$ , barrier  $B$  and type  $\phi = 1$  for a call and  $\phi = -1$  for a put, we use the following pricing rules, which are based on noarbitrage conditions:

- Knock in (KI) is priced *via*  $KI = \text{vanilla} KO$ .  $\bullet$
- Reverse knock in  $(RKI)$  is priced *via*  $RKI =$  $vanilla - RKO.$
- Reverse knockout (RKO) is priced *via* RKO( $\phi$ .  $(K, B) = KO(-\phi, K, B) - KO(-\phi, B, B) +$  $\phi(B - K) \text{NT}(B)$ .
- Double one touch (DOT) is priced *via* DNT.
- NT is priced via OT.

# **Volatility for Risk Reversals, Butterflies** and Theoretical Value

To determine the volatility and the vanna and volga for the risk reversal and butterfly, the convention is the same as for the building of the smile curve. Hence the 25% delta risk reversal retrieves the strike for 25% delta call and put with the spot delta and calculates the vanna and volga of these options using the corresponding volatilities from the smile.

The  $TV$  of the exotics is calculated using the ATM volatility, retrieving it with the same convention that was used to build the smile, to build the smile.

#### **Pricing Barrier Options**

Ideally, one would be in a situation to hedge all barrier contracts with a portfolio of vanilla options or simple barrier building blocks. In the Black-Scholes model, there are exact rules on how to statically hedge many barrier contracts. A state-of-the art reference is given in  $[3]$ . However, in practice, most of these hedges fail, because volatility is not constant.

For regular KO options, one can refine the method to incorporate more information about the global shape of the vega surface through time.

We chose *M* future points in time as  $0 < a_1\% <$  $a_2\% < \cdots < a_M\%$  of the time to expiration. Using the same cost of vanna and volga, we calculate the overhedge for the regular KO with a reduced time to expiration. The factor for the cost is the probability not to touch the barrier within the remaining times to expiration  $1 > 1 - a_1\% > 1 - a_2\% > \cdots > 1$  $a_M\%$  of the total time to expiration. Some desks believe that for ATM strikes, the long time to maturity should be weighted higher and for lowdelta strikes the short time to maturity should be weighted higher. The weighting can be chosen (rather arbitrarily) as

$$w = \tanh[\gamma(|\delta - 50\%| - 25\%)] \tag{24}$$

with a suitable positive *γ* . For *M* = 3, the total overhedge is given by

$$OH = \frac{OH(1 - a_1\%) \times w + OH(1 - a_2\%)}{+OH(1 - a_3\%) \times (1 - w)}$$
(25)

Which values to use for *M*, *γ* , and the *ai*, whether to apply a weighting and what kind, varies for different trading desks.

An additional term can be used for single-barrier options to account for glitches in the stop loss of the barrier. The theoretical value of the barrier option is determined with a barrier that is moved by four basis points and 50% of that adjustment is added to the price if it is positive. If it is negative, it is omitted altogether. The theoretical foundation for such a method is explained in [4].

## **Pricing Double-barrier Options**

Double-barrier options behave similar to vanilla options for a spot far away from the barrier and more like OT options for a spot close to the barrier. Therefore, it appears reasonable to use the traders' rule of thumb for the corresponding regular KO to determine the overhedge for a spot closer to the strike and for the corresponding OT option for a spot closer to the barrier. This adjustment is the intrinsic value of the RKO times the overhedge of the corresponding OT option. The border is the arithmetic mean between strike and the in-the-money barrier.

## **Pricing Double-no-touch Options**

For DNT options with lower barrier *L* and higher barrier *H* at spot *S*, one can use the overhedge

$$OH = \max{\text{vanna}-\text{volga-}OH; \delta(S-L)}$$
$$- TV - 0.5\%; \delta(H-S) - TV - 0.5\%}$$
(26)

where *δ* denotes the delta of the DNT option.

## **Pricing European-style Options**

#### *Digital Options*

Digital options are priced using the overhedge of the call/put spread with the corresponding volatilities.

#### *European Barrier Options*

European barrier options (EKO) are priced using the prices of European and digital options and the relationship

$$EKO(\phi, K, B) = \text{vanilla}(\phi, K) - \text{vanilla}(\phi, B)$$
$$- \text{digital}(B)\phi(B - K) \qquad (27)$$

## **No-touch Probability**

The NT probability is obviously equal to the nondiscounted value of the corresponding NT option paying at maturity (under the risk-neutral measure). Note that the price of the OT option is calculated using an iteration for the touch probability. This means that the price of the OT option used to compute the NT probability is itself based on the traders' rule of thumb. This is an iterative process that requires an abortion criterion. One can use a standard approach that ends either after 100 iterations or as soon as the difference of two successive iteration results is less than 10<sup>−</sup>6. However, the method is so crude that it actually does not make much sense to use such precision at just this point. Therefore, to speed up the computation, we suggest that this procedure is omitted and no iterations are taken, which means to use the nondiscounted TV of the no-touch option as a proxy for the NT probability.

# **The Cost of Trading and Its Implication on the Market Price of One-touch Options**

Now let us take a look at an example of the traders' rule of thumb in its simple version. We consider OT options, which hardly ever trade at *TV*. The tradable price is the sum of the TV and the overhedge. Typical examples are shown in Figure 6, one for an upper touch level in EUR/USD, and one for a lower touch level.

![](_page_6_Figure_1.jpeg)

**Figure 6** Overhedge of a one-touch option in EUR/USD for (a) an upper touch level and (b) a lower touch level, based on the traders' rule of thumb

Clearly, there is no overhedge for OT options with a TV of 0% or 100%, but it is worth noting that low-TV OT options can be twice as expensive as their TV, sometimes even more. The overhedge arises from the cost of risk managing the OT option. In the Black–Scholes model, the only source of risk is the underlying exchange rate, whereas the volatility and interest rates are assumed constant. However, volatility and rates are themselves changing, whence the trader of options is exposed to instable vega and rho (change of the value with respect to volatility and rates). For short-dated options, the interest rate risk is negligible compared to the volatility risk as shown in Figure 7. Hence the overhedge of an OT option is a reflection of a trader's cost occurring because of the risk management of his vega exposure.

## **Example**

We consider a one-year OT option in USD/JPY with payoff in USD. As market parameters, we assume a spot of 117.00 JPY per USD, JPY interest rate 0.10%, USD interest rate 2.10%, volatility 8.80%, 25-delta risk reversal −0*.*45%,a and 25-delta butterfly 0.37%.b

The touch level is 127.00, and the TV is at 28.8%. If we now only hedge the vega exposure, then we need to consider two main risk factors, namely,

- 1. the change of vega as the spot changes, often called vanna;
- 2. the change of vega as the volatility changes, often called volga or volgamma or vomma.

To hedge this exposure, we treat the two effects separately. The vanna of the OT option is 0.16%,

![](_page_7_Figure_1.jpeg)

**Figure 7** Comparison of interest rate and volatility risk for a vanilla option. The volatility risk behaves like a square-root function, whereas the interest rate risk is close to linear. Therefore, short-dated FX options have higher volatility risk than interest rate risk

and the vanna of the risk reversal is 0.04%. So we need to buy 4 (= 0*.*16*/*0*.*04) risk reversals, and, for each of them, we need to pay 0.14% of the USD amount, which causes an overhedge of −0*.*6%. The volga of the OT is −0*.*53%, and the volga of the butterfly is 0.03%. So we need to sell 18 (= −0*.*53*/*0*.*03) butterflies, each of which pays us 0.23% of the USD amount, which causes an overhedge of −4*.*1%. Therefore, the overhedge is −4*.*7%. However, we will get to the touch level with a risk-neutral probability of 28.8%, in which case we would have to pay to unwind the hedge. Therefore, the total overhedge is −71*.*2% × 4*.*7% = −3*.*4%. This leads to a midmarket price of 25.4%. Bid and offer could be 24.25%–36.75%. There are different beliefs among market participants about the unwinding cost. Other observed prices for OT options can be due to different existing vega profiles of the trader's portfolio, a marketing campaign, a hidden additional sales margin, or even the overall view of the trader in charge.

## **Further Applications**

The method illustrated above shows how important the current smile of the vanilla options market is for the pricing of simple exotics. Similar types of approaches are commonly used to price other exotic options. For long-dated options, the interest rate risk will take over the lead in comparison to short-dated options where the volatility risk is dominant.

## **End Notes**

a*.* This means that a 25-delta USD call is 0.45% cheaper than a 25-delta USD put in terms of implied volatility.

b*.* This means that a 25-delta USD call and 25-delta USD put is, on average, 0.37% more expensive than an ATM option in terms of volatility.

## **References**

- [1] Castagna, A. & Mercurio, F. (2007). The Vanna-Volga method for implied volatilities, *Risk* Jan. 106–111.
- [2] Lipton, A. & McGhee, W. (2002). Universal Barriers, *Risk*, **15**(5), 81–85.
- [3] Poulsen, R. (2006). Barrier options and their static hedges: simple derivations and extensions, *Quantitative Finance*, Vol. **6**(4), 327–335.
- [4] Schmock, U., Shreve, S.E. & Wystup, U. (2002). Dealing with dangerous digitals, in *Foreign Exchange Risk*, Risk Publications, London, http://www.mathfinance.com/ FXRiskBook/
- [5] Wystup, U. (2003). The market price of one-touch options in foreign exchange markets, *Derivatives Week*, London, **XII**(13), 8–9.
- [6] Wystup, U. (2006). *FX Options and Structured Products*, Wiley Finance Series.

## **Related Articles**

**Barrier Options**; **Foreign Exchange Markets**.

UWE WYSTUP
# **Credit Portfolio Insurance**

Credit portfolio insurance products such as credit constant proportion portfolio insurance (CPPI) and constant proportion debt obligations (CPDOs) utilize similar technologies that use leverage as a mechanism to enhance returns. Credit CPPIs and CPDOs evolved in the low credit spread environment witnessed recently, especially between the years 2004 to about mid-2007 as shown in Figure 1. For many investors, the tightness in investment grade spreads rendered investment grade return targets difficult to achieve other than through rule-based, leveraged credit strategies. Credit CPPIs and CPDOs are two alternative formats of gaining leverage in a similar class of investments,a with the first credit CPPI products being introduced in 2004 followed by CPDO products in 2006.

## **Credit CPPI**

Historically, the CPPI concept came into being in the context of equity portfolios. Some of the earlier works in this area are by Black and Jones [1], Black and Perold [2], and Black and Rouhani [3]. For a CPPI, the term *insurance* is a loosely defined expression that refers to principal protection of the issued CPPI notes. The principal component of the notes, called the *bond floor*, is secured by virtue of the fact that an appropriate portion of the note issuance proceeds is invested in risk-free assets. The remainder of the proceeds, called *cushion* or *reserve*, is used to take leveraged exposure to risky credit assets in the case of a credit CPPI. Combined earnings from the riskfree and risky assets generate the cashflows to pay the periodic interest and final principal on the CPPI notes.

A simple example of a CPPI would be a structure where proceeds from the CPPI note issuance are divided into two components—the first component is invested in a "risk-free" zero coupon bond with a face value equal to the principal of the CPPI note and the second component acts as a reserve account for taking exposure to more risky assets through credit default swaps (CDSs). The idea is that the risk-free bond will back the repayment of principal at maturity, while the more risky portfolio of CDS assets will be used to generate spread income and to pay the interest on the CPPI note.

Figure 2 describes the structure of a CPPI. The CPPI investor provides the initial funds equivalent to the notional amount of the issued CPPI notes and the proceeds are utilized to set up (i) a reserve account for investing in risky assets and (ii) a deposit account for investing in "risk-free" assets. Leverage is obtained on the risky portion of the balance sheet by taking positions that make the notional exposure to the risky assets to be some multiple of the reserve account balance. Although the choice of these risky assets can include all types of assets, for a credit CPPI the typical investment would be in the form of exposure to a credit index, standardized or bespoke synthetic CDOs, cash flow CDOs, equity default swaps (EDSs),b and so on.

Figure 3 shows the expected evolution of the *bond floor* and the more risky portfolio value over the term of the CPPI. The actual value of the risky portfolio and *bond floor* at a particular point in time will, however, depend on the evolution of credit CPPI risk factors such as movements in credit migrations, default events, interest rates, and loss given default. Moreover, the performance of the CPPI is quite sensitive to the leverage multiplier, and to mitigate this risk, the CPPI is often required to reduce leverage through rebalancing as losses on the risky portfolio eat into the reserve account.c

#### *Credit CPPI Risk Factors*

*Gap risk*: This is the possibility that rebalancing the risky portfolio may not happen at the speed of its market value deterioration. In such a scenario, a loss of principal could occur if a sudden loss in market value exceeds the reserve cash account in the form of the *cushion*. Moreover, the higher the leverage multiplier, the higher the gap risk. A less drastic scenario is when a loss on the risky portfolio nearly erases the *cushion* and leaves only risk-free assets in the portfolio—in that case although the principal is still protected, the promised CPPI note coupon can no longer be paid in full.

*Default risk*: Defaults in the more risky portfolio, both in terms of timing and loss given default, affect the expected returns and the principal protection of the CPPI notes. Some structures mitigate default risk by imposing restrictions on investments in subinvestment grade assets.

*Interest rate risk*: Changes in interest rates lead to fluctuations in the zero coupon *bond floor*, which

![](_page_1_Figure_1.jpeg)

**Figure 1** Evolution of the CDX North American Investment Grade (CDX.NA.IG) Index over the period July 2004 to July 2007

![](_page_1_Figure_3.jpeg)

\* These assets have no default risk but may be subject to interest rate or prepayment risk.

**Figure 2** Cash flow diagram describing a credit CPPI structure

in turn impacts the reserve available for taking leveraged exposure to credit risk assets. Since the objective of the credit CPPI is to limit downside while maximizing returns through dynamic rebalancing of the portfolio between "risk-free" and more risky assets, changes in the *bond floor* due to interest rate movements affect the rebalancing strategies.

*Performance risk*: The CPPI manager's ability in implementing the credit CPPI dynamic portfolio rebalancing strategy may also be important.

#### *Modeling a Credit CPPI*

A Monte Carlo simulation approach is an effective means of modeling the risk of a credit CPPI transaction. The four main features of a bottom-up

![](_page_2_Figure_1.jpeg)

**Figure 3** Expected value of the bond floor and the more risky portfolio over the life of a CPPI

credit CPPI model should include (i) single name CDS spread curve dynamics, (ii) correlation between spread movements and credit migrations across the names in the portfolio or index, (iii) losses due to defaults and associated recoveries, and (iv) interest rate dynamics for cash flow discounting, *bond floor* value estimation, and liability payment calculations.

Credit quality changes in the form of rating migrations may be modeled in a structural framework where the normalized asset return, *Ak* , of asset *k* can be decomposed into systematic and idiosyncratic components:

$$A_k = \sqrt{\rho}z + \sqrt{1 - \rho}\varepsilon_k \tag{1}$$

For a Gaussian copula framework, the systematic and idiosyncratic latent factors, that is, *z* and *εκ* , respectively, would have standard normal distributions and *ρ* would be the asset correlation parameter. The probability of asset *k* migrating from its current rating level *Ri* to a new rating level *Rj* would be given by the following expression in this case:

$$\sum_{m=1}^{j-1} \Pr(R_i \to R_j) \leq \Phi(A_k) < \sum_{m=1}^{j} \Pr(R_i \to R_j)$$
(2)

Credit spreads are often modeled as mean reverting processes, where the mean reversion speed and spread volatility could be made functions of rating levels. One such specification for the spread model could be

$$\log(S_k(t_{i+1})) = \delta \log(S_k(t_i)) + (1 - \delta)$$
  
 
$$\times \log(S^*(R_k(t_{i+1}))) + \sigma \sqrt{\delta \Delta t}$$
  
 
$$\times (\sqrt{\rho_s} A_k + \sqrt{1 - \rho_s} \varphi_k) \qquad (3)$$

where *δ* = exp*(*-*κt)*, *κ* is the mean reversion speed, *σ* is the spread volatility, *S*<sup>∗</sup> is the average spread associated with rating *R, Ak* is the asset return used in the credit migration simulation, *ρs* is the correlation between the asset return and the spread, and *ϕk* ∼ *N*(0,1).

One may also include a jump component in the above specification, or a regime switching module, for enhancing the possibility of more sudden and drastic spread moves for a more conservative estimation of gap risk. For example, Cont and Tankov [5] developed a model that includes jumps in the asset price process.

Lastly, an appropriate interest rate process based on any popular spot rate or forward rate model such as the one by Hull and White [7] or Heath *et al.* [6] can be incorporated in the above framework for cash flow discounting calculations.

## **CPDO**

CPDOs use a similar leveraging technology as described previously for CPPIs but with two major exceptions. First, there is no guaranteed return of principal and, second, rebalancing in the form of leverage changes is in the opposite direction to that of a CPPI, that is, CPDO rebalancing is based on a "buy low, sell high" strategy where a spread widening leads to an increase in the notional exposure to the more risky portfolio, subject to the maximum leverage cap. This is designed to allow the structure to compensate for the loss in value due to the spread widening by increasing the spread income from more risky assets in future periods.

The economics behind CPDO transactions backed by exposure to investment grade credits such as an index CPDO is the fact that investment grade names typically display an upward sloping term structure of spreads. The theory is that the CPDO can take exposure to a new on-the-run index series at a relatively high spread level (corresponding to 51 */*<sup>4</sup> years maturity) but trade out of the series at a significantly lower spread level (corresponding to 43 */*<sup>4</sup> years) as the index becomes off-the-run.d In the context of CPDOs, this dynamic is known as the *roll down the curve* benefit and the aim of the CPDO is to maximize this advantage by employing leverage.

Figure 4 describes a typical CPDO structure. Upon initiation, all cash proceeds from the CPDO investor are placed in a deposit account and get invested in short-term liquid instruments that earn interest at the risk-free benchmark rate, typically LIBOR. The deposit account also acts as the reserve account for taking exposure to a more risky credit portfolio of CDS assets (or a CDS index) where the credit portfolio notional = CPDO note notional<sup>∗</sup> leverage factor. The most popular choice for the risky assets is a portfolio providing equal exposure to the CDX North American Investment Grade (CDX.NA.IG) and the iTraxx Europe Investment Grade indices.e Moreover, to mitigate default and liquidity risk, such index CPDOs are generally required to sell protection only for "on-the-run" index series so that exposure to index constituents' names that get downgraded to below investment grade rating levels is automatically limited because of the substitution rules imposed when indices roll over every six months.

The deposit account is credited with interest from the liquid short-term assets, spread premia from

![](_page_3_Figure_9.jpeg)

**Figure 4** Cash flow diagram describing a CPDO structure

the CDS credit portfolio, and any positive mark-tomarket (m-t-m) settlements on the credit portfolio. The deposit account gets debited with coupon payments to the CPDO investor, management fees to the arranger, any negative m-t-m settlements, or credit loss payments due to defaults in the CDS portfolio. The performance of the CPDO thus depends on how the *net asset value* (*NAV* ) at time *t*, which is equal to the sum of the deposit account balance, the m-t-m of the CDS portfolio, and the accrued spread income, compares to the *target value* (*TV* ) at time *t*, which is the amount if invested at the risk-free rate would be sufficient to meet the CPDO coupon and principal payment obligations, as well as any fees.f The difference between *TV* (*t*) and *NAV* (*t*) is called the *shortfall*, that is,

$$Shortfall(t) = TV(t) - NAV(t)$$
(4)

The leverage employed in the CPDO transaction is a function of the ratio of the *shortfall* to the risky income calculated as the present value of the expected spread premium earnings. Note that this ratio quantifies the amount of the current shortfall when compared with the cash flow expected from the risky assets. More specifically, the transaction has predefined rules for estimating a target notional defined as

$$Target\ notional = Gearing\ factor$$

$$\times \frac{Shortfall}{PV\ (expected\ CDS\ premia)}$$
(5)

Some structures define a flat gearing factor, while others may employ a time-dependent gearing factor. Leverage is then simply the ratio of the target notional to the CPDO note notional. From equation (5), it can be seen that if spreads widen, causing the CPDO to incur m-t-m losses that increase the *shortfall* relative to the expected risky spread earnings, leverage increases. This is contrary to a CPPI leverage strategy where any m-t-m losses on the more risky portfolio lead to a delivering of the transaction.

At the commencement of a CPDO transaction, the *shortfall* is positive as *NAV* (*t*0) is simply the CPDO note notional proceeds *minus* any upfront structuring fees since the value of the CDS portfolio is zero at initiation and there are no accrued spread premium earnings yet. With time, however, the shortfall is expected to decrease to zero, in which case the CPDO is said to have a "cash-in" event. This implies that the structure no longer needs to take on any risky exposure and the reserve deposit account is large enough to meet all future interest, principal, and fee payment obligations by simply investing in risk-free assets. In adverse market conditions, however, frequent and large m-t-m losses on the portfolio and/or defaults may lead to severe erosion of the deposit reserve account. In some instances, the *NAV* may drop below a certain threshold, typically defined at 10% of the issued CPDO note notional. In this case, the CPDO transaction is unwound and is said to have suffered a "cash-out" event. The only other event possible is when the transaction fails to redeem the CPDO note at par upon maturity, in which case the CPDO investor incurs a loss, though not as severe as under a "cash-out" event.

#### *CPDO Risk Factors*

Similar to CPPIs, the main risk factors for a CPDO structure are as follows:

*Spread risk*: Sudden (and correlated) widening of spreads can lead to large m-t-m losses that eat into the cash reserve account. With index CPDOs, this risk may also be in the form of rollover risk, whereby index constituent names that deteriorate in credit (and show spread widening) get downgraded and get replaced with tighter spread names. Since the CPDO is generally required to roll over its exposure to the on-the-run index series, the effect of the rollover is twofold. On the one hand, riskier names have to be effectively unwound at wider spreads, resulting in m-t-m losses. On the other hand, these names get replaced in the index with higher rated names, implying lower spread earnings after the roll that would have ordinarily compensated for the m-t-m losses.g

*Default risk*: Similar to CPPIs, CPDO investors are exposed to default risk as protection sellers. However, generally speaking, this risk is greatly mitigated in index CPDOs due to the rollover every six months.

*Liquidity risk*: Since index CPDOs are required to roll their exposure to the index series every six months, they can be more prone to liquidity risk. Even though on-the-run index series are the most liquid, bid–offer spreads may widen at the time of rollover as dealers anticipate more one-sided trades.

*Interest rate risk*: In "normal" circumstances, a natural hedge exists since liabilities, that is, CPDO notes outstanding (paid LIBOR) are less than or equal to the cash reserve account (earns LIBOR). However, interest rate risk may become significant if large m-t-m (or default) losses eat into the reserve account, leading to a mismatch between the CPDO notes outstanding and the size of this reserve deposit account.

#### *Modeling a CPDO*

CPDOs can be modeled using a similar bottom-up Monte Carlo approach as described for CPPIs. For index CPDOs, the analysis should also include a means of modeling index changes to capture the impact of rollover risk on the CPDO note performance. This can be incorporated in the suggested framework by using the ratings-based credit migration model to analyze changes to the index by appropriate replacement of credits that get downgraded to below investment grade rating categories.

Cont and Jessen [4] provided an alternative modeling approach using a top-down method. In their framework, rollover effects are incorporated *via* jumps in the index spread at each roll date.

## **End Notes**

a*.* Some investors also consider synthetic CDO tranches as an alternative means of gaining leverage in this class of investments. We, however, differentiate CPPIs and CPDOs from synthetic tranches since the latter are correlation products.

b*.* EDSs have risk characteristics that are similar to CDSs and hence a CPPI with exposure to EDSs is classified as a credit CPPI.

c*.* Alternatively, an increase in the more risky portfolio value may result in an increase in the notional exposure to the more risky assets up to a predefined maximum leverage cap. For this reason, a credit CPPI strategy is also known as *buy high, sell low*.

d*.* This assumes that the average credit quality of the index remains more or less the same over the six-month period. e*.* This equally weighted combination of the CDX and iTraxx indices is frequently referred to as the *GLOBOXX index.* f*.* In other words, the *target value* is the present value of all

liabilities discounted at the risk-free rate. g*.*

In actual practice, the CPDO takes exposure to the index directly and not individual names, so the effect of the index rollover is a sudden drop in the index spread as the more risky names get replaced with the less risky ones.

## **References**

- [1] Black, F. & Jones, R. (1987). Simplifying portfolio insurance, *Journal of Portfolio Management* **14**, 48–51.
- [2] Black, F. & Perold, A. (1992). Theory of constant proportion portfolio insurance, *Journal of Economics, Dynamics and Control* **16**, 403–426.
- [3] Black, F. & Rouhani, R. (1989). *Constant Proportion Portfolio Insurance and the Synthetic Put Option: A Comparison*. Institutional Investor Focus on Investment Management, pp. 695–708.
- [4] Cont, R. & Jessen, C. (2009). *Constant Proportion Debt Obligations (CPDO): Modeling and Risk Analysis*. http://ssrn.com/abstract=1372414.
- [5] Cont, R. & Tankov, P. (2007). Constant proportion portfolio insurance in presence of jumps in asset prices, *Mathematical Finance* **19**(3), http://ssrn.com/abstract=1021084.
- [6] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology, *Econometrica* **60**(1), 77–105.
- [7] Hull, J. & White, A. (1990). Pricing interest rate derivative securities, *Review of Financial Studies* **3**(4), 573–592.

## **Related Articles**

#### **Constant Proportion Portfolio Insurance**; **Credit Migration Models**.

SAIYID S. ISLAM
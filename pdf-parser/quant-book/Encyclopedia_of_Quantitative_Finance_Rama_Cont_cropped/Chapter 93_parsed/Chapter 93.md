# **Foreign Exchange Markets**

The foreign exchange (FX) market has two major functionalities, one related to hedging and the other to investment.

In the age of globalization, it is essential for corporates and multinationals to hedge their FX exposure due to export/import activities. In addition, fund managers (institutional) need to hedge their FX risk in stocks or bonds if the stocks/bonds are quoted in a foreign currency. With hedging instruments, the FX exposure can be reduced and one can even benefit from certain market scenarios. This kind of participation brings us to the important class of investor-oriented products where the coupon depends on an FX rate or, at maturity, the pay-off (amount, currency) will be determined by an FX rate. This kind of product can be issued as a note, certificate, or bond.

For the major currencies such as USD, EUR, JPY, GBP, CHF, AUD, CAD, and NZD, the market has become more transparent over the last few years. For plain vanilla options, market data, especially volatilities for maturities below 1 year, are published by brokers or banks and are shown on Reuters pages (e.g., TTKLINDEX10, ICAPFXOP, GFIVOLS). For exotic products, new pricing tools, such as Superderivatives, LPA, Bloomberg, ICY, Fenics, and so on, are available for users, but the premium of the option will depend on the pricing model and the adjustments used. For the emerging market currencies such as PLN (Polish zloty), HUF (Hungarian forint), ZAR (South African rand), and so on, which are freely tradable but less liquid, the market data are less transparent. Currencies that are not freely tradable (the currency cannot be cash-settled offshore) such as BRL (Brazilian real) or CNY (Chinese yuan renmimbi) can be traded as a nondeliverable forward (NDF) or as a nondeliverable option (NDO) against a tradable currency. The NDF is a cash-settled product without exchange of notionals, which means that the intrinsic value at maturity will be paid in the free tradable currency based on a fixing source. The underlying of an NDO is the NDF, meaning that exercising the NDO results in an NDF, which will also be cash-settled. Another class of currencies is that of the fully cash-settled pegged ones, which means that their exchange rate is 100% correlated to a major currency, mostly the USD. If one expects that this peg will continue, hedges should be done in the correlated major currency. In the case of SAR (Saudi riyal) or AED (United Arab Emirates dirham), discussion has been ongoing about depegging the currencies. In case this is done, there could be an increasing interest in SARor AED-linked investments. This opens an increasing interest in SAR- or AED-linked investments to participate in the case that these currencies are depegged. For the "more exotic currencies" such as the GHC (Ghanaian cedi), there is no options market.

# **Quotation**

The exchange rate can be defined as the amount of domestic currency one gets if one sells one unit of foreign currency. If we take a look at an example of the EUR/USD exchange rate, the default quotation is EUR-USD, where USD is the domestic currency and EUR is the foreign currency. The terms *domestic* and *foreign* are not related to the location of the trader or any country, but it is more a question of the definition. Domestic and base are synonyms as are foreign and underlying. The common way is to denote the currency pair with a slash (/) and the quotation with a dash (−). The slash (/) does not mean a division.

For example, the currency pair EUR/USD can be quoted either in EUR-USD, which means how many USD one gets for selling one EUR, or in USD-EUR, which then means how many EUR one gets for selling one USD. There are certain market standard quotations; some of them are listed in Table 1.

In the FX market, two currencies are involved, which means that one needs to specify on which currency a particular call or put option is written. For

**Table 1** Market convention of some major currency pairs with sample spot price

| Currency pair | Quotation | Quote  |  |
|---------------|-----------|--------|--|
| EUR/USD       | EUR-USD   | 1.4400 |  |
| GBP/USD       | GBP-USD   | 1.9800 |  |
| USD/JPY       | USD-JPY   | 114.00 |  |
| USD/CHF       | USD-CHF   | 1.1500 |  |
| EUR/CHF       | EUR-CHF   | 1.6600 |  |
| EUR/JPY       | EUR-JPY   | 165.00 |  |
| EUR/GBP       | EUR-GBP   | 0.7300 |  |
| USD/CAD       | USD-CAD   | 0.9800 |  |

instance, in the currency pair EUR/USD, there can be a EUR call, which is equivalent to a USD put, or a EUR put, which is equivalent to a USD call.

#### **FX Terminology**

In the FX market, a million is called a  $buck$  and a billion a *vard*. This is because the word "billion" has different meanings in different languages. In French and German, it represents  $10^{12}$  and in English it stands for  $10^9$ 

Certain currency pairs have their own names in the market. For instance, GBP/USD is called a *cable*, because the exchange rate information used to be sent between England and America through a telephone cable in the Atlantic Ocean. EUR/JPY is called the cross, because it is the cross rate of the more liquidly traded USD/JPY and EUR/USD.

Some currency pairs also have their own names to make them short and unique in communication. New Zealand dollar, which is NZD/USD, is called Kiwi, and the Australian dollar, which is AUD/USD, is called Aussie. Among the Scandinavian currencies, NOK (Norwegian krone) is called Noki, SEK (Swedish krona) is called Stoki, and in combination with DKK (Danish krone) the three are called Scandies.

The exchange rates are usually quoted in five relevant figures, for example, in EUR-USD we would get a quote of  $1.4567$ . Sometimes one can get a quote up to six figures, but for the time being we focus on five figures. The last digit "7" is called the *pip* and the middle digit "5" is called the *big figure*, because the interbank spot trading tools show this digit in bigger size since it is the most important information. The figure to the left of the big figure is known anyway and the pips to the right of the big figures are sometimes "negligible". For example, a rise of EUR-JPY 165.00 by 40 pips is 165.40 or a rise by 3 big figures would be 168.00.

#### **Quotation of Option Prices**

Plain vanilla option prices are usually quoted in terms of implied volatility. If an option is priced in volatility, a delta exchange is necessary. The advantage is that the volatility does not usually move as quickly as the spot rate and one has the chance to

Table 2 Standard market quotation types for option premiums

| Symbol   | Description of symbol             | Result of example          |
|----------|-----------------------------------|----------------------------|
| $d$ pips | Domestic per unit<br>foreign      | 208.42 USD pips<br>per EUR |
| $f$ pips | Foreign per unit<br>domestic      | 97.17 EUR pips<br>per USD  |
| $\% f$   | Foreign per unit<br>foreign       | 1.4575% EUR                |
| $\%d$    | Domestic per unit<br>domestic     | 1.3895% USD                |
|          | Domestic amount<br>Foreign amount | 20 842 USD<br>14 575 EUR   |
|          |                                   |                            |

Foreign = EUR. domestic = USD.  $S_0 = 1.4300$ ,  $r_d = 5.0\%$ .  $r_f = 4.5\%$ , volatility = 8.0%,  $K = 1.5000$ ,  $T = 365$  days,  $EUR \text{ call } USD \text{ put, notional} = 1\,000\,000 \text{ EUR} = 1\,500\,000$  $USD$ 

compare the prices, especially in the broker market. On the basis of the spot rate on which the delta exchange is done, the premium of the plain vanilla option is calculated *via* the Black-Scholes formula. For exotic options, a price in volatility is not possible because each bank has its own pricing model for these.

The premium, value, or prices of options can be quoted in six different ways (Table 2). The Black-Scholes formula quotes in domestic pips per one unit of foreign notional. The others can be retrieved in the following manner:

$$d \text{ pips } \xrightarrow{\times \frac{1}{SK}} f \text{ pips } \xrightarrow{\times K} \%f \xrightarrow{\times \frac{S}{K}} \%d \qquad (1)$$

#### **Delta and Premium Convention**

The spot delta of a plain vanilla option can be retrieved in a straightforward way by using the Black-Scholes formula. It is called the raw spot *delta*,  $\delta_{raw}$ . One retrieves it in percentage of the foreign currency, but the delta in the second involved currency  $\delta_{raw}^{opposite}$  can be computed in the following manner:

$$\delta_{\text{raw}}^{\text{opposite}} = -\frac{S}{K} \delta_{\text{raw}} \tag{2}$$

The delta multiplied with the corresponding notional determines the amount that has to be bought or sold to hedge the spot risk of the option up to the first order.

An important question is whether the premium of the option needs to be included in the delta or not? An example, EUR-USD, for investigation is considered here. In this quotation, USD is the domestic currency and EUR is the foreign one. The Black-Scholes formula calculates the premium in domestic per 1 unit foreign currency, which in our example is in USD per 1 EUR. This premium is denoted by  $p$ . If the premium is paid in EUR, which means in the foreign currency, it includes an FX risk. The premium  $p$  in USD is equivalent to  $\frac{p}{S}EUR$ , which means that the amount of EUR that has to be bought to hedge the option needs to be reduced by this EUR premium and is given as

$$\delta_{\text{raw}} - \frac{p}{S} E U R \tag{3}$$

We denoted USD as domestic currency and EUR as foreign currency, but do all banks or trading places have this notion? What is the notional currency of the option and what is the premium currency? In the interbank market, there exists a fixed notion of the delta of the currency pair. Normally, it is the LHS delta in Fenics<sup>a</sup> if the option is traded in the LHS premium, which is mostly used, for example, for EUR/USD, USD/JPY, and EUR/JPY, and the RHS delta if it is the RHS premium, for example, for GBP/USD and AUD/USD. Most of the options traded in the market are out-of-the-money; therefore, the premium does not create a critical FX risk for the trader.

For the banks where the base currency is considered the risk-free currency, the market value of the option is in the base currency, and if the premium is in the risky currency, the premium needs to be included in the hedge. If the premium is in the risk-free (or the base) currency, the premium will be offset by the market value of the option. In the opposite case, where the risk-free currency is the underlying currency, if the premium is in the risky currency, the premium will be offset by the market value of the option. Only in the case of premium in risk-free currency, the amount needs to be included in the hedge.

Therefore, the delta hedge is invariant with respect to the risky currency notion of the bank; for example, for both banks, one is based in USD and the other in EUR, and the delta is the same.

**Table 3** One-year EUR call USD put, the strike is 1.4300 for a EUR-based bank

| Delta<br>currency | Premium<br>currency | Fenics     | Hedge                                                              | Delta    |
|-------------------|---------------------|------------|--------------------------------------------------------------------|----------|
| %EUR              | EUR                 | LHS        | $\delta_{raw} - P$                                                 | 48.35    |
| %EUR              | USD                 | RHS        | $\delta_{raw}$                                                     | 51.64    |
| $\%$ USD          | EUR                 | $RHS + F4$ | $-(\delta_{raw} - P)$                                              | $-48.35$ |
|                   |                     |            | S/K                                                                |          |
| $\%$ USD          | $\text{USD}$        | $LHS + F4$ | $-\delta_{\text{raw}}S/K$                                          | $-51.64$ |
|                   |                     |            | $S = 1.4300$ , $r_d = 5.0\%$ , $r_f = 4.5\%$ , volatility = 8.0\%, |          |
| $K = 1.4300$      |                     |            |                                                                    |          |

**Table 4** One-year EUR call USD put, the strike is 1.5000 for a EUR-based bank

| Delta<br>currency | Premium<br>currency | Fenics     | Hedge                                                       | Delta    |
|-------------------|---------------------|------------|-------------------------------------------------------------|----------|
| %EUR              | EUR                 | LHS        | $\delta_{raw} - P$                                          | 28.22    |
| %EUR              | USD                 | RHS        | $\delta_{raw}$                                              | 29.69    |
| %USD              | EUR                 | $RHS + F4$ | $-(\delta_{raw} - P)$                                       | $-26.91$ |
|                   |                     |            | S/K                                                         |          |
| $\%$ USD          | $\text{USD}$        | $LHS + F4$ | $-\delta_{\text{raw}}S/K$                                   | $-28.30$ |
| $K = 1.5000$      |                     |            | $S = 1.4300, r_d = 5.0\%, r_f = 4.5\%,$ volatility = 8.0\%, |          |

#### Examples

To see the different deltas used in practice, consider two examples discussed in Tables 3 and 4.

# Implied Volatility and Delta for a Given Strike

Implied volatility is not constant across strikes (see **Foreign Exchange Smiles**). The volatility  $\sigma$  depends on the corresponding delta of the option, but the delta depends on the price of the option and therefore on the used volatility. How can we retrieve the correct volatility for a given strike? For sure it is an iterative process. Initially, one uses the at-the-money (ATM) volatility  $\sigma_0$  and calculates the delta  $\Delta_1$ . On the basis of  $\Delta_1$ , a new volatility  $\sigma_1$  can be retrieved from the volatility matrix. This new volatility leads to a new delta and so on. Now one can define a convergence criterion to stop the iteration. In practice, a fixed number of iterations is used, usually five steps.

| Mat/ | 50%  | 45%  | 40%  | 35%  | 30%  | 25%  | 20%  | 15%  | 10%  | 5%   |
|------|------|------|------|------|------|------|------|------|------|------|
| O/N  | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 |
| 1W   | 0.06 | 0.06 | 0.05 | 0.05 | 0.05 | 0.04 | 0.04 | 0.03 | 0.02 | 0.01 |
| 1M   | 0.11 | 0.11 | 0.11 | 0.10 | 0.10 | 0.09 | 0.08 | 0.07 | 0.05 | 0.03 |
| 2M   | 0.16 | 0.16 | 0.15 | 0.15 | 0.14 | 0.13 | 0.11 | 0.09 | 0.07 | 0.04 |
| 3M   | 0.20 | 0.02 | 0.19 | 0.19 | 0.17 | 0.16 | 0.14 | 0.12 | 0.09 | 0.05 |
| 6M   | 0.28 | 0.28 | 0.27 | 0.26 | 0.25 | 0.23 | 0.20 | 0.17 | 0.13 | 0.07 |
| 9M   | 0.33 | 0.33 | 0.33 | 0.32 | 0.30 | 0.28 | 0.24 | 0.20 | 0.15 | 0.09 |
| 1Y   | 0.38 | 0.38 | 0.38 | 0.37 | 0.35 | 0.32 | 0.28 | 0.24 | 0.18 | 0.10 |
| 2Y   | 0.51 | 0.51 | 0.51 | 0.50 | 0.48 | 0.44 | 0.40 | 0.33 | 0.25 | 0.15 |
| 3Y   | 0.60 | 0.60 | 0.60 | 0.60 | 0.57 | 0.54 | 0.48 | 0.40 | 0.31 | 0.18 |
|      |      |      |      |      |      |      |      |      |      |      |

**Table 5** Vega matrix for standard maturities and delta values, expressed in percent of foreign notional

The matrix shows, for example, that 2Y EUR call USD put 35 delta can be hedged with two times 6M EUR call USD put 30 delta

# **Mapping of Delta on Vega**

From the Black–Scholes formula, it is clear that for a fixed delta, the vega *Pσ* does not depend on volatility or *rd* , and *Pσ* is therefore a function of only *rf* , maturity, and delta. This gives the trader the advantage of a moderately stable vega matrix. Such a matrix is shown in Table 5, with *rf* = 4*.*5%.

# **FX Smile**

The FX smile surface has a different setup or construction in comparison to equity.

Plain vanilla options with different maturities have different implied volatilities. This is called the *term structure* of a currency pair.

Plain vanilla options are quoted in terms of volatility for a given delta. The smile curve is usually set up on some fixed pillars and the points between these pillars are interpolated to get a smooth surface. In the direction of the term structure, the easiest way is to interpolate linearly in the variance. In addition, weights are introduced to highlight or lower the importance of some dates, for example, the release of nonfarm payrolls, local holiday, or a day before or after a weekend. In the direction of the moneyness or delta, one method of interpolation is the cubic spline. The pillars in that direction are 10-delta put, 25-delta put, ATM, 25-delta call, and 10-delta call. Sometimes the 35-delta put and 35-delta call are also used. Unlike equity, in the FX market, the smile surface is decomposed into the symmetric part by using butterflies or strangles and the skew part by using the risk reversals for the fixed deltas. This is because of the liquidity of these products in the FX market.

#### *Risk Reversal (RR)*

For instance, a 25-delta risk reversal is a combination of buying a 25-delta call and selling a 25-delta put. The payout profile is shown in Figure 1.

#### *Butterfly (BF)*

In the case of a 25-delta butterfly, it is the combination of buying 25-delta put, buying 25-delta call, selling ATM put, and selling ATM put (alternatively, 25-delta strangle is a 25-delta put and a 25-delta call). Payout profiles are shown in Figure 2.

The decomposition of a smile curve inspired by these products is shown in Figure 3.

![](_page_3_Figure_16.jpeg)

**Figure 1** Payout profile of a risk reversal

![](_page_4_Figure_1.jpeg)

**Figure 2** Payout profile of a butterfly

![](_page_4_Figure_3.jpeg)

**Figure 3** Decomposition of a smile curve

If we denote the ATM volatillity by *σ*0, the 25 delta put volatility by *σ*−, and the 25-delta call volatility by *σ*+, we get the following relationships:

$$RR = \sigma_{+} - \sigma_{-} \tag{4}$$

$$BF = \frac{1}{2}(\sigma_{+} + \sigma_{-}) - \sigma_{0} \tag{5}$$

$$\sigma_{+} = ATM + BF + \frac{1}{2}RR \tag{6}$$

$$\sigma_{-} = ATM + BF - \frac{1}{2}RR \tag{7}$$

It should be noted that the values RR and BF given above have nothing to do with the prices of actual risk reversal and butterfly contracts: rather they provide a convenient representation of the implied volatility smile in terms of its level (*σ*0), convexity *(BF )*, and skewness *(RR)*.

| Table 6 | EUR/USD 25-delta risk reversal (in %) |  |  |  |  |  |
|---------|---------------------------------------|--|--|--|--|--|
|---------|---------------------------------------|--|--|--|--|--|

| Date         | 1 month | 3 months | 1 year |
|--------------|---------|----------|--------|
| Dec 3, 2007  | −0.6    | −0.6     | −0.6   |
| Dec 4, 2007  | −0.525  | −0.55    | −0.525 |
| Dec 5, 2007  | −0.525  | −0.55    | −0.525 |
| Dec 6, 2007  | −0.525  | −0.55    | −0.525 |
| Dec 7, 2007  | −0.6    | −0.6     | −0.6   |
| Dec 10, 2007 | −0.6    | −0.6     | −0.6   |

**Table 7** EUR/USD 25-delta butterfly (in %)

| Date         | 1 month | 3 months | 1 year |
|--------------|---------|----------|--------|
| Dec 3, 2007  | 0.225   | 0.425    | 0.460  |
| Dec 4, 2007  | 0.225   | 0.425    | 0.460  |
| Dec 5, 2007  | 0.225   | 0.425    | 0.460  |
| Dec 6, 2007  | 0.225   | 0.425    | 0.460  |
| Dec 7, 2007  | 0.227   | 0.425    | 0.463  |
| Dec 10, 2007 | 0.227   | 0.425    | 0.463  |

Table 6 shows the 25-delta risk reversal in EUR/USD on different trading dates and the corresponding butterflies are listed in Table 7.

For the setup of the smile surface in a risk management or pricing tool, it is important to know which convention is used for a certain currency pair in the option market to define the notion of ATM.

# **At-the-money Definition**

There exist several definitions of ATM:

- ATM spot: Strike is equal to the spot.
- ATM forward: Strike is equal to the forward.
- Delta parity: The absolute value of the delta call is equal to the absolute value of the delta put.
- Fifty delta: Put delta is 50% and the call delta is 50%.
- Value parity: The premium of the delta put is equal to the delta call.

The most widely used one in the interbank market is the delta parity up to 1 year for the most liquid currencies. In emerging markets, (at-the-moneyforward) (ATMF) is used. For long-term options such as USD/JPY 15 years, the ATMF convention is used, but since this results in a delta position, a forward delta exchange will be done.

# **End Notes**

a*.* Fenics is an FX option pricing tool owned by the broker GFI and used in the interbank market (www.fenics.com).

# **Further Reading**

- Hakala, J. & Wystup, U. (2002). *Foreign Exchange Risk*, Risk Publications, London.
- Reiswich, D. & Wystup, U. (2009). *FX Volatility Smile Construction*, Research Report, Frankfurt School of Finance & Management, September 2009.
- Wystup, U. (2006). *FX Options and Structured Products*, Wiley Finance.

# **Related Articles**

**Black–Scholes Formula**; **Exchange Options**; **Foreign Exchange Options**; **Foreign Exchange Options: Delta- and At-the-money Conventions**; **Foreign Exchange Smiles**; **Foreign Exchange Smile Interpolation**.

MICHAEL BRAUN
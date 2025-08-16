# **Foreign Exchange Options: Delta- and At-the-money Conventions**

In financial markets, the value of a plain-vanilla European option is generally quoted in terms of its implied volatility, that is, the volatility that, when plugged into the Black–Scholes formula, gives the correct market price. By observation of market prices the implied volatility, however, turns out to be a function of the option's strike, thus giving rise to the so-called *volatility smile*.

In foreign exchange (FX) markets, it is common practice to quote volatilities for FX call and put options in terms of their delta sensitivities rather than in terms of their strikes or their moneyness. Volatilities and deltas are quoted by means of a table, the *volatility smile table*, consisting of rows for each FX option expiry date and columns for a number of delta values, as well as a column for the at-the-money (ATM) volatilities.

The definition and usage of a volatility smile table is complicated by the fact that FX markets have established various delta and ATM conventions. In this article, we summarize these conventions and highlight their intuition. For each delta convention, we give formulas and methods for the conversion of deltas to strikes and *vice versa*. We describe how to retrieve volatilities from the table for an arbitrary FX option that is to be priced in accordance with the information contained therein. We point out some mathematical problems and pitfalls when trying to do so and give criteria under which these problems surface.

# **Definitions**

# *FX Rate*

Before discussing the various delta conventions, we summarize some basic terms and definitions that we use in this article.

• *FX spot rate S(t)*: The FX spot rate *S(t)* is the *current* exchange rate at the present time *t*

("today") between the domestic and the foreign currency. It is specified as the number of units of domestic currency that an investor gets in exchange for one unit of foreign currency,

$$S(t) := \frac{\text{number of units of domestic currency}}{\text{one unit of foreign currency}}$$
(1)

• *FX forward rate F (t, T )*: The FX forward rate *F (t, T )* is the exchange rate between the domestic and the foreign currency at some *future* point of time *T* as observed at the present time *t (t < T )*. It is again specified as the number of units of domestic currency that an investor gets in exchange for one unit of foreign currency at time *T* .

Using arbitrage arguments, spot and forward FX rates are related by (see, for instance, [3]):

$$F(t,T) = S(t) \cdot \frac{D_{\text{for}}(t,T)}{D_{\text{dom}}(t,T)}$$
(2)

where *D*for := *D*for*(t, T )* is the foreign discount factor for time *T* (observed at time *t*) and *D*dom := *D*dom*(t, T )* is the domestic discount factor for time *T* (observed at time *t*).

Note that the terminology in FX transactions is always confusing. In this article, we refer to the "domestic" currency in the sense of a base currency in relation to which "foreign" amounts of money are measured (see also [4]). By definition (1), an amount *x* in foreign currency, for example, is equivalent to *x* · *S(t)* units of domestic currency at time *t*.

In the markets, FX rates are usually quoted in a standard manner. For example, the USD–JPY exchange rate is usually quoted as the number of Japanese yen an investor receives in exchange for 1 USD. For a Japanese investor, the exchange rate would fit the earlier definition, while a US investor would either need to look at the reverse exchange rate 1*/S(t)* or think of Japanese yen as the "domestic" currency.

## *Value of FX Forward Contracts*

When two parties agree on an FX forward contract at time *s*, they agree on the exchange of an amount of money in foreign currency at an agreed exchange rate

 $K$  against an amount of money in domestic currency at time  $T > s$ . When choosing  $K = F(s, T)$ , the FX forward contract has no value to either of the parties at time s.

As, in general, the forward exchange rate changes over time, at some time  $t$  ( $s < t < T$ ), the FX forward contract will have a nonzero value (in domestic currency) given by

$$v_f(t, T) = D_{\text{dom}} (F(t, T) - K)$$
  
=  $S(t)D_{\text{for}} - KD_{\text{dom}}$  (3)

### Value of FX Options

Upon deal inception, the holder of an FX option obtains the right to exchange a specified amount of money in domestic currency against a specified amount of money in foreign currency at an agreed exchange rate  $K$ . Assuming nonstochastic interest rates and the standard lognormal dynamics for the spot exchange rate, at time  $t$ , the domestic currency values of plain-vanilla European call and put FX options with strike  $K$  and expiry date  $T$  are given by their respective Black-Scholes formulas:

Call option: 
$$v_c(t,T) = D_{\text{dom}} F(t,T) \mathcal{N}(d_+)$$
  
-  $D_{\text{dom}} K \mathcal{N}(d_-)$  (4)

Put option:  $v_p(t, T) = (-1) \cdot [D_{\text{dom}} F(t, T) \mathcal{N}(-d_+)$  $- D_{\text{low}} K \mathcal{N}(-d) 1 \tag{5}$ 

$$= D_{\text{dom}} \ K \ (\mathcal{N}(d_{+}) - 1)$$
$$= D_{\text{dom}} \ K \ (\mathcal{N}(d_{-}) - 1) \ \ (6)$$

where

$$d_{\pm} = \frac{\ln\left(F(t,T)/K\right) \pm 1/2\sigma^2 \tau}{\sigma\sqrt{\tau}},$$

- $K$  : strike of the FX option,
- $\sigma$  : Black-Scholes volatility,
- $\tau = T t$ : time to expiry of FX option, and
- $\mathcal{N}(x)$  : cumulative normal distribution function (7)

Note that  $v_c(t, T)$  and  $v_p(t, T)$  as given earlier are measured in *domestic* currency. The option position, however, may also be held in foreign currency. We call the currency in which an option's value is measured as its *premium currency*.

Also note that the present value of call and put options are related by the  $put-call$  parity:

$$v_c - v_p = v_f = D_{\text{dom}} (F(t, T) - K)$$
 (8)

# **Definition of Delta Types**

This section summarizes the delta conventions used in FX markets and gives some of their properties. We outline the correspondence of each delta sensitivity with a particular delta hedge strategy the holder of an FX option chooses. FX options are peculiar in that the underlying coincides with the exchange rate. While, in general, it makes no sense to measure the value of an option in units of its underlying (e.g., in the number of shares of a company), the FX option position can be held either in domestic or in foreign currency. This gives rise to the premium-adjusted deltas.

For the ease of notation, we drop the time dependency of  $S(t)$  and  $F(t, T)$  in the following and denote the spot exchange rate as of time  $t$  by  $S$  and the forward exchange rate for time  $T$  as observed in  $t$ by  $F$ .

#### Unadjusted Deltas

#### Spot Delta.

**Definition 1** For FX options, the spot delta is defined as the derivative of the option price  $v_{c/p}$  with respect to the FX spot rate S:

$$\Delta_S^{c/p} := \frac{\partial v_{c/p}}{\partial S} \tag{9}$$

**Interpretation** Spot delta is the "usual" delta sensitivity that follows from the Black-Scholes equation. It can be derived by considering an FX option position that is held and hedged in *domestic* currency (see, for instance,  $[2, 3]$ ).

Note that  $\Delta_S$  is an amount in units of foreign currency. This makes sense from the hedging perspective: an amount of money in foreign currency is needed to make up for changes in the domestic currency value of an FX option (held in domestic currency), due to changes of the exchange rate. If, for example, an investor is long an FX call option, a decrease in the exchange rate will lead to a decrease in his option position. By having shorted  $\Delta_S$  units of foreign currency, the investor will make a hedge profit in domestic currency balancing his losses in the option position to first order.

#### Properties

Call option: 
$$\Delta_S^c = D_{\text{for}} \mathcal{N}(d_+)$$
 (10)  
Put option:  $\Delta_S^p = D_{\text{for}} \left\{ \mathcal{N}(d_+) - 1 \right\}$   
 $= -D_{\text{for}} \mathcal{N}(-d_+)$  (11)

*Put–call delta parity:*  $\Delta_S^c - \Delta_S^p = D_{\text{for}}$  $(12)$ 

#### **Forward Delta**

**Definition 2** The forward delta  $\Delta_F$  (also called driftless delta [4]) of an FX option is defined as the ratio of the option's spot delta and the delta of a long forward contract on the FX rate (where the forward price of the FX forward contract equals the strike of the  $FX$  option):

$$\Delta_F^{c/p} := \frac{\partial v_{c/p}/\partial S}{\partial v_f/\partial S} = \frac{\Delta_S^{c/p}}{\partial v_f/\partial S} \tag{13}$$

**Interpretation** The forward delta is not simply the derivative of the option price formula with respect to the forward FX rate  $F$ . The rationale for the abovementioned definition follows from the construction of a hedge portfolio using FX forward contracts as hedge instruments for the FX option position (both held in domestic currency). The forward delta gives the number of forward contracts that an investor needs to enter into to completely delta hedge his/her FX option position;  $\Delta_F$ , therefore, is simply a number without units.

#### Properties

Call option: 
$$\Delta_F^c = \frac{D_{\text{for}} \cdot \mathcal{N}(d_+)}{D_{\text{for}}} = \mathcal{N}(d_+) \quad (14)$$
  
Put option: 
$$\Delta_F^p = \frac{D_{\text{for}} \cdot (\mathcal{N}(d_+) - 1)}{D_{\text{for}}}$$
$$= \mathcal{N}(d_+) - 1 = -\mathcal{N}(-d_+) \quad (15)$$

*Put–call delta parity:* 

 $\Delta_F^c - \Delta_F^p = 1$  $(16)$ 

*Premium-adjusted Deltas* 

#### Spot Delta Premium Adjusted.

**Definition 3** The premium-adjusted spot delta is defined as

$$\Delta_{S, pa}^{c/p} := S \cdot \frac{\partial}{\partial S} \left( \frac{v_{c/p}}{S} \right) = \Delta_{S}^{c/p} - \frac{v_{c/p}}{S} \tag{17}$$

**Interpretation** The definition of the premiumadjusted spot delta follows from an FX option position that is held in *foreign* currency, while being hedged in *domestic* currency.

While  $v$  is the option's value in domestic currency,  $v/S(t)$  is the option's value converted to foreign currency (i.e., its premium currency) at time  $t$ . The term  $\partial (v/S(t))/\partial S \cdot dS$ , thus, gives the change of the option value (measured in *foreign* currency) with the underlying exchange rate. To complete a delta hedge in *domestic* currency, the derivative needs to be multiplied by  $S(t)$  from where the defining equation  $(17)$  for the premium-adjusted spot delta follows.

Note that the delta sensitivity is equal to spot delta, adjusted for the premium effect  $v/S(t)$ . This is easily interpreted as a delta that is corrected by a premium amount already paid in foreign currency. Also note that  $\Delta_{S, pa}$  itself is denominated in units of foreign currency.

## Properties

*Call option:* 

$$\Delta_{S, pa}^{c} = D_{\text{for}} \frac{K}{F} \mathcal{N}(d_{-}) \tag{18}$$

Put option:

$$\Delta_{S, pa}^{p} = D_{\text{for}} \frac{K}{F} \left\{ \mathcal{N}(d_{-}) - 1 \right\}$$
$$= -D_{\text{for}} \frac{K}{F} \left\{ \mathcal{N}(-d_{-}) \right\} \tag{19}$$

*Put–call delta parity:* 

$$\Delta_{S, pa}^{c} + \Delta_{S, pa}^{p} = D_{\text{for}} \frac{K}{F} \left( \mathcal{N}(d_{-}) - \mathcal{N}(-d_{-}) \right)$$
$$= 2\Delta_{S, pa}^{c} - D_{\text{for}} \frac{K}{F} \tag{20}$$

$$\Delta_{S, pa}^{c} - \Delta_{S, pa}^{p} = D_{\text{for}} \frac{K}{F}$$
 (21)

The defining equations for premium-adjusted deltas have interesting consequences: while put deltas are unbounded and strictly monotonous functions of  $K$ , call deltas are bounded (i.e.,  $\Delta_{S}^{c} \in [0; \Delta_{\text{max}}]$  with  $\Delta_{\text{max}} < 1$ ) and are *not* monotonous functions of K. Thus, the relationship between call deltas and strikes  $K$  is not one to one.

# Forward Delta Premium Adjusted.

**Definition 4** The premium-adjusted forward delta is defined in analogy to the unadjusted delta:

$$\Delta_{F, \, pa}^{c/p} = \frac{S \cdot \partial/\partial S \left(v_{c/p}/S\right)}{\partial \, v_f/\partial \, S} = \frac{\Delta_{S, \, pa}^{c/p}}{\partial \, v_f/\partial \, S} \quad (22)$$

**Interpretation** The intuition behind the definition of the premium-adjusted forward delta follows from an FX option position that is held in *foreign* currency and hedged by forward FX contracts in *domestic* currency. The premium-adjusted forward delta gives the number of forward contracts that are needed for the delta hedge in *domestic* currency of an FX option held in foreign currency. The derivation of the defining equation  $(22)$  is similar to the one for spot delta premium adjusted (cf. the section Spot Delta Premium Adjusted). Note that  $\Delta_{F, pa}$  is a pure number without units.

# Properties

*Call option:* 

$$\Delta_{F,\,pa}^c = \frac{K}{F} \mathcal{N}(d_-) \tag{23}$$

Put option:

$$\Delta_{F, pa}^{p} = \frac{K}{F} \cdot \left\{ \mathcal{N}(d_{-}) - 1 \right\} = -\frac{K}{F} \mathcal{N}(-d_{-}) \ (24)$$

 $Put\text{-}call\text{ delta parity:}$ 

$$\Delta_{F, pa}^{c} + \Delta_{F, pa}^{p} = \frac{K}{F} \left( \mathcal{N}(d_{-}) - \mathcal{N}(-d_{-}) \right)$$
$$= 2\Delta_{F, pa}^{c} - \frac{K}{F} \tag{25}$$

$$\Delta_{F, \, pa}^{c} - \Delta_{F, \, pa}^{p} = \frac{K}{F} \tag{26}$$

Also note the important remarks in the previous section on the domain, the range of values, and the relationship between call delta and option strike. They apply likewise to premium-adjusted forward deltas.

#### **Definition of At-the-money Types**

In this section, we summarize the various ATM definitions, comment on their financial interpretation, and give the relations between all relevant quantities in Table 1.

|                   | $\Delta$ -neutral                                             | $K_{\text{atm}} = F$                                                   | $\text{Vega/gamma} = \text{max}$                                                                                                                                                             | $\Delta = 50\%$                  |
|-------------------|---------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| ATM strike values |                                                               |                                                                        |                                                                                                                                                                                              |                                  |
| Spot delta        | $F \mathrm{e}^{1/2\sigma^2\tau}$                              | F                                                                      | $F \mathrm{e}^{1/2\sigma^2\tau}$                                                                                                                                                             |                                  |
| Fwd delta         | $F e^{1/2\sigma^2 \tau}$                                      | F                                                                      | $F \mathrm{e}^{1/2\sigma^2\tau}$                                                                                                                                                             | $F \mathrm{e}^{1/2\sigma^2\tau}$ |
| Spot delta p.a.   | $F \mathrm{e}^{-1/2\sigma^2\tau}$                             | F                                                                      | $F \mathrm{e}^{1/2\sigma^2 \tau}$                                                                                                                                                            |                                  |
| Fwd delta p.a.    | $F \mathrm{e}^{-1/2\sigma^2 \tau}$                            | F                                                                      | $F e^{1/2\sigma^2 \tau}$                                                                                                                                                                     |                                  |
| ATM delta values  |                                                               |                                                                        |                                                                                                                                                                                              |                                  |
| Spot delta        | $D_{\text{for}} \mathcal{N}(0)$                               | $D_{\text{for}} \mathcal{N}\left(\frac{1}{2}\sigma\sqrt{\tau}\right)$  | $D_{\text{for}} \mathcal{N}(0)$                                                                                                                                                              |                                  |
| Fwd delta         | $\mathcal{N}(0)$                                              | $\mathcal{N}\left(\frac{1}{2}\sigma\sqrt{\tau}\right)$                 | $\mathcal{N}(0)$                                                                                                                                                                             | $\mathcal{N}(0)$                 |
| Spot delta p.a.   | $D_{\text{for}} \text{ e}^{-1/2\sigma^2 \tau} \mathcal{N}(0)$ | $D_{\text{for}} \mathcal{N}\left(-\frac{1}{2}\sigma\sqrt{\tau}\right)$ |                                                                                                                                                                                              |                                  |
| Fwd delta p.a.    | $e^{-1/2\sigma^2\tau}\mathcal{N}(0)$                          | $\mathcal{N}\left(-\frac{1}{2}\sigma\sqrt{\tau}\right)$                | $D_{\text{for}} \,\mathrm{e}^{+1/2\sigma^2\tau} \mathcal{N}\left(-\frac{1}{2}\sigma\sqrt{\tau}\right)$ $\mathrm{e}^{+1/2\sigma^2\tau} \mathcal{N}\left(-\frac{1}{2}\sigma\sqrt{\tau}\right)$ |                                  |

<table>

 Table 1
 Strike values and delta values at the ATM point for the different FX delta conventions<sup>(a)</sup>

<sup>(a)</sup>Note that  $\mathcal{N}(0) = 1/2$ . The delta values are given for call options, the corresponding values for put options can be obtained, by replacing  $\mathcal{N}(x)$  with  $(\mathcal{N}(x) - 1)$ 

ATM Definition "Delta Neutral"

**Definition 5** The ATM point is defined as the strike  $K_{\text{atm}}$ , for which the delta of a call and a put option add up to zero:

$$\Delta_{\mathbf{r}}^{c}\left(K_{\text{atm}},\sigma_{\text{atm}}\right) + \Delta_{\mathbf{r}}^{p}\left(K_{\text{atm}},\sigma_{\text{atm}}\right) = 0 \quad (27)$$

Here,  $x$  represents any of the delta conventions defined in the section Definition of Delta Types.

**Interpretation** The definition follows directly from a "straddle" position where a long call and a long put option with the same strike are combined. If the strike is chosen appropriately, the change in value of the call and the put option compensate (to first order) when the underlying FX rate changes. The straddle position's value, thus, is insensitive ("delta neutral") to changes in the underlying FX rate. The reason for this choice is that traders can use straddles to hedge the vega of their position without upsetting the delta.

Properties The ATM definition mentioned earlier for delta neutral FX options is equivalent to  $\mathcal{N}(d_{+}) =$  $1/2$  in case of the unadjusted delta conventions and  $\mathcal{N}(d_{-}) = 1/2$  in case of the premium-adjusted delta conventions. From this, the relationships of Table 1 follow in a straightforward manner.

### ATM Definition via Forward

**Definition 6** The ATM point is defined as the strike equaling the forward exchange rate:

$$K_{\text{atm}} := F \tag{28}$$

**Interpretation** This definition reflects the view that (given the information at deal inception) an option is ATM when its strike is chosen equal to the expected exchange rate at option expiry. If the spot exchange rate, indeed, approached F as  $t \rightarrow T$  (as would be the case in a fully deterministic world by arbitrage arguments, cf. equation (2)), then the ATM strike would mark the dividing point between options that expire in-the-money (ITM) and out-of-the-money (OTM). From the put-call parity  $(8)$ , we see that this is also the strike at which put and call options have the same value. Thus, this ATM definition is also called *value parity* [4].

**Properties** The relationships of Table 1 can again be derived in a straightforward manner from the definitions

#### $ATM \nDefinition "vega = max"$

**Definition 7** The ATM point is defined as the strike  $K_{\text{atm}}$  for which vega of the FX option is at its maximum. Vega is the sensitivity of the FX option, with respect to the implied volatility of the underlying exchange rate. It is given by (cf.  $[4]$ )

$$vega_{c/p} = \frac{\partial v_{c/p}}{\partial \sigma} = S \ D_{\text{for}} \ \sqrt{\tau} \ n(d_+)$$
 (29)

where  $n(x)$  is the normal density distribution.

The ATM strike can be derived from  $\partial$  vega/ $\partial K =$  $0 \text{ as}$ 

$$K_{\text{atm}} = F \text{ e}^{1/2\sigma^2 \tau} \tag{30}$$

Properties Table 1 again summarizes the relevant quantities for this ATM definition. Note that in case of unadjusted deltas, this ATM definition is equivalent to the delta neutral ATM definition. This is, however, not the case for adjusted deltas.

# ATM Definition " $\gamma = max$ "

**Definition 8** The ATM point is defined as the strike  $K_{\text{atm}}$  for which the gamma sensitivity of the FX option is at its maximum.

We restrict the discussion to the case of gamma spot,

$$\gamma_S^{c/p} := \frac{\partial \Delta_S^{c/p}}{\partial S} = D_{\text{for}} \frac{n(d_+)}{S \sigma \sqrt{\tau}} \tag{31}$$

From  $\partial \gamma / \partial K = 0$ , the ATM strike can be derived as

$$K_{\text{atm}} = F \text{ e}^{1/2\sigma^2 \tau} \tag{32}$$

thus revealing the equivalence to the ATM definition "vega =  $max$ ".<sup>a</sup>

# ATM Definition "50%"

**Definition 9** According to this convention, the ATM point is defined by

$$\Delta^c = 0.5 \quad and \quad |\Delta^p| = 0.5 \tag{33}$$

This condition can only be true for the forward delta convention and, thus, does not apply to any of the other delta conventions.

#### Properties of ATM Definitions

Table 1 summarizes the properties of the ATM point for all possible combinations of ATM definitions and delta conventions.

In this context, it is interesting to note that, beside their financial interpretation, mathematically, the various definitions of the ATM point lead to three characteristic relationships between the strike  $K$  and the forward exchange rate  $F$ :

$$K = F \Rightarrow d_{\pm} = \pm \sigma \sqrt{\tau} \tag{34}$$

$$K = F e^{1/2\sigma^2 \tau} \Rightarrow d_+ = 0, \ d_- = -\sigma \sqrt{\tau} \qquad (35)$$

$$K = F e^{-1/2\sigma^2 \tau} \Rightarrow d_+ = \sigma \sqrt{\tau}, \ d_- = 0 \qquad (36)$$

# **Converting Deltas to Strikes and Vice** Versa

Quoting volatilities as a function of the options' deltas rather than as a function of the options' strikes brings about a problem when it comes to pricing FX options. Consider the case that we want to price a vanilla European option for a given strike  $K$ . To price this option, we have to find the correct volatility. As the volatility is given in terms of delta and delta itself is a function of volatility *and* strike, we have to solve an implicit problem, which, in general, has to be done numerically.

The following sections outline the algorithms that can be used to that end for the various delta conventions and directions of conversion. As the spot and forward deltas differ only by constant discount factors, we restrict the presentation to the forward versions of the adjusted and unadjusted deltas.

# Forward Delta

For unadjusted deltas, there are simple one-to-one relationships between put and call deltas, the put-call delta parities  $(12)$  and  $(16)$ . PUT deltas can therefore easily be translated into the corresponding CALL deltas and it is sufficient to perform all the calculations for call deltas here.

Conversion of Forward Delta to Strike. If volatilities are given as a function of forward delta, the strike corresponding to a given forward delta  $\Delta_F^c$ can be calculated analytically. Let  $\sigma(\Delta_F^c)$  denote the volatility associated with  $\Delta_F^c$ ;  $\sigma(\Delta_F^c)$  may either be quoted or interpolated from the volatility smile table.

With  $\Delta_F^c$  and  $\sigma(\Delta_F^c)$  given, we can directly solve equation  $(14)$ ,

$$\Delta_F^c = \mathcal{N}(d_+) = \mathcal{N}\left(\frac{\ln\left(F/K\right) + 1/2\sigma(\Delta_F^c)^2 T}{\sigma(\Delta_F^c)\sqrt{T}}\right) \tag{37}$$

for the strike  $K$ . We get

$$K = F \exp\left\{-\sigma(\Delta_F^c)\sqrt{T}\mathcal{N}^{-1}\left(\Delta_F^c\right) + \frac{1}{2}\sigma(\Delta_F^c)^2T\right\}$$
(38)

Conversion of Strike to Forward Delta. The reverse conversion from strikes to forward deltas is more difficult and can only be achieved numerically. The following algorithm can be shown to converge [1] and has empirically proven to be very efficient.

In the first step, calculate a zero-order guess  $\Delta_0$ by using the ATM volatility  $\sigma_{\text{atm}}$  in equation (14):

$$\Delta_0 = \Delta_F^c(K, \sigma_{\text{atm}}) = \mathcal{N}\left(\frac{\ln(F/K) + 1/2\sigma_{\text{atm}}^2 T}{\sigma_{\text{atm}}\sqrt{T}}\right) \tag{39}$$

In the second step, use this zero-order guess for delta to derive a first-order guess  $\sigma_1$  for the volatility by **interpolating** the curve  $\sigma(\Delta)$ :

$$\sigma_1 = \sigma \ (\Delta_0) \tag{40}$$

Finally, calculate the corresponding first-order guess for  $\Delta_F^c$  in the third step:

$$\Delta_{1} = \Delta_{F}^{c} (K, \sigma_{1}) = \mathcal{N} \left( \frac{\ln (F/K) + 1/2\sigma_{1}^{2}T}{\sigma_{1}\sqrt{T}} \right)$$
(41)

and repeat steps two and three until the changes in  $\Delta$ from one iteration to the next are below the specified accuracy.

#### Forward Delta Premium Adjusted

For the sake of clarity, we again restrict the discussion below to the case of call deltas. The algorithms for put deltas work analogously.

**Conversion of Forward Delta Premium Adjusted** to Strike. The conversion from forward delta premium adjusted to an absolute strike is more complicated than in the case of an unadjusted delta and cannot be formulated in a closed-form expression. The reason is that in the equation for the premiumadjusted call delta (23),

$$\Delta_{F, pa}^{c} = \frac{K}{F} \mathcal{N}(d_{-})$$
$$= \frac{K}{F} \mathcal{N}\left(\frac{\ln\left(F/K\right) - 1/2\sigma(\Delta_{F, pa}^{c})^{2}T}{\sigma(\Delta_{F, pa}^{c})\sqrt{T}}\right) \tag{42}$$

the strike  $K$  appears inside and outside the cumulative normal distribution function so that one cannot solve directly for K. Even though both  $\Delta_{F, pa}^{c}$  and  $\sigma(\Delta_{F, pa}^{c})$  are given, the problem has to be solved numerically.

So when converting a given call delta  $\Delta_{F, pa}^c$ , a root finder has to be used to solve for the correspondent strike  $K$ . This could, for example, be a simple bisection method where, for call deltas, the ATMstrike  $K_{\text{atm}}$  is the lower bound and some high (i.e., quasi infinite) value such as  $100 K_{\text{atm}}$  can be used as upper bound. Of course, a more elaborate root finder to solve this problem could (and should!) be used, but a discussion of the various methods lies beyond the scope of this article.

Note, however, that all these methods require that  $\Delta$  is a strictly monotonous function of K. We will see in section Ambiguities in the Conversion from  $\Delta$ to Strike for Premium-adjusted Deltas that this is not always the case.

**Conversion of Strike to Forward Delta Premium Adjusted.** The conversion of an absolute strike to forward delta premium adjusted can be done analogously to the conversion into an unadjusted forward delta as described in section Conversion of Strike to Forward Delta.

First, use the previous guess  $\Delta_{i-1}$  to obtain an improved guess  $\sigma_i$  for the volatility by interpolating

in the  $\sigma(\Delta)$  curve.

$$\sigma_i = \sigma \left( \Delta_{i-1} \right) \tag{43}$$

In the second step, calculate the corresponding guess  $\Delta_i$  by

$$\Delta_{i} = \Delta_{F, pa}^{c} (K, \sigma_{i}) = \frac{K}{F} \mathcal{N} \left( \frac{\ln (F/K) - 1/2\sigma_{i}^{2} T}{\sigma_{i} \sqrt{T}} \right)$$
(44)

Iterate these two steps until the change in  $\Delta$  from one step to the next is below the specified accuracy. A good initial guess for the volatility is, of course, again the ATM-volatility  $\sigma_{\text{atm}}$ .

#### **Using the Volatility Smile Table**

In FX markets, linear combinations of plain-vanilla FX options, such as "strangles", "risk reversals", and "butterflies", are liquidly traded. These instruments are composed of ATM and OTM plain-vanilla put and call options at specific values of delta (typically,  $0.25$ or  $0.1$ ). When aggregating this market information, one obtains a scheme called the **volatility smile table** consisting of rows for each FX option expiry date, a column for ATM volatilities, and two distinct sets of columns for volatilities of OTM put and call options. We call these sets the *put and call* sides of the table.

Thus, OTM options can be priced by retrieving volatilities from the respective side of the volatility smile table, for example, OTM calls are priced using volatilities from the call side. By virtue of the put-call parity, ITM options can be priced using volatilities from the opposite side of the table, that is, ITM calls are priced using volatilities from the put side.

To exemplify this, consider the case of an option with arbitrary time to maturity and strike. The typical procedure to retrieve this option's volatility from the smile table would be the following.

- 1. Determine the volatilities of the ATM point and the call and put sides at the option's expiry. For this, the volatilities of each delta column will, in general, have to be interpolated in time.
- 2. Decide which side of the table to use depending on the option's strike  $K$ : options with  $K >$

 $K_{\text{atm}}$  are either OTM calls or ITM puts and are therefore priced using volatilities from the call side. Accordingly, options with  $K < K_{\text{atm}}$  are priced using volatilities from the put side (cf. equation  $(4)$ ).

- 3. Convert the option's strike to delta. This depends on the side of the table chosen in the previous step: convert to a call delta if  $K > K_{\text{atm}}$ , and to a put delta if  $K < K_{\text{atm}}$ . See the section Converting Deltas to Strikes and vice versa for the details of these conversions.
- 4. Retrieve the volatility from the table by interpolating volatilities in delta.

Alternatively, one could also translate the full smile volatility table from deltas to strikes. The conversion of deltas to strikes would then be necessary for the grid points of the table only, thus, making steps 2 and 3 of the earlier listed procedure obsolete. The interpolation in step 4 would be done in strikes However, keep in mind that the strike grid points would vary from row to row.

It is important to note that the earlier procedure is based on the assumption that delta is a strictly monotonous function of the option's strike  $K$ : only in this case the option's delta and strike are equivalent measures of the option's moneyness, that is, only in this case we are guaranteed the equivalence

$$K > K_{\text{atm}} \Longleftrightarrow \Delta^c < \Delta_{\text{atm}}^c \tag{45}$$

In the following section, we will show that the assumption of monotonicity is not always true and derive the conditions under which it is violated.

## **Problems and Pitfalls**

# Interpolation in Time Dimension when Delta Conventions Change

In FX markets, it is common to switch delta conventions with an option's time to maturity. For example, volatilities for options with less than two years to maturity are often quoted in terms of spot deltas, whereas volatilities for longer expiries are usually quoted in terms of one of the forward delta conventions.

When conventions change from one expiry  $T_k$ to the next one, it is *a priori* unclear how an interpolation in time on a delta-volatility table should be performed. Which of the two conventions shall be used for options with expiries  $t$  within the range  $T_k < t < T_{k+1}$ ?

Some possibilities are as follows: convert the grid points at  $T_k$  into the convention used for  $T_{k+1}$ and do interpolation in the long-term convention or, conversely, convert the grid points at  $T_{k+1}$  into the convention used for  $T_k$  and interpolate in the shortterm convention. Another possibility would be to translate the delta grid into a strike grid and do the interpolation on strikes.

None of these approaches is *a priori* superior to the others. In real life, however, a choice has to be made. Even though the differences may be small, one should be aware that the choice is arbitrary.

#### ATM Delta Falling in the OTM Range

For long times to maturity, the delta of an ATM FX option may become smaller than the delta of the closest OTM option. In a sense, the ATM delta "crosses" the nearest OTM delta. In this case, it is unclear how the interpolation of volatilities (in delta) should be done or whether the ATM point or the crossed delta point should possibly be ignored.

The conditions under which this problem occurs vary with the delta and ATM types. In the following, we outline the derivation of these conditions for an exemplarily chosen combination (premium-adjusted spot deltas and forward ATM definition), summarize the results for other combinations, and finally discuss a typical numerical example for long-dated FX options.

Exemplary Derivation. We start from equation (17) for the ATM delta using  $K_{\text{atm}} = F$ :

$$\Delta_{S, pa}^{c} (F, \sigma_{\text{atm}}) = D_{\text{for}} \mathcal{N} \left( -\frac{\sigma_{\text{atm}}}{2} \sqrt{T} \right) \quad (46)$$

Obviously, the ATM delta will decrease with decreasing values of  $D_{\text{for}}$  and increasing values of  $\sigma_{\text{atm}}\sqrt{T}$ . Small values of  $D_{\text{for}}$  and/or large values of  $\sigma_{\text{atm}}\sqrt{T}$  will therefore lead to ATM deltas that are smaller than the nearest OTM point  $\Delta_1^c$  (which is usually  $\Delta_1^c = 0.25$ ).

From the expression mentioned earlier, it follows immediately that the ATM delta is larger than the first

|                    | ATM-type forward                                                                                                   | ATM-type delta neutral                                                                                    |
|--------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Spot delta         | $D_{\text{for}} > -2\Delta_1^p$                                                                                    | $D_{\text{for}} > 2\Delta_1^c$                                                                            |
|                    | $\sigma_{\rm atm} \, \sqrt{T} \, < \, 2 \mathcal{N}^{-1} \left( 1 + \frac{\Delta_1^{\, \nu}}{D_{\rm for}} \right)$ |                                                                                                           |
| Forward delta      | $\sigma_{\text{atm}}\sqrt{T} < 2\mathcal{N}^{-1}\left(1 + \Delta_1^p\right)$                                       | No constraint                                                                                             |
| Spot delta p.a.    | $D_{\text{for}} > 2\Delta_1^c$                                                                                     | $D_{\text{for}} > 2\Delta_1^c$                                                                            |
|                    | $\sigma_{\rm atm}\,\sqrt{T}\,<\,2\mathcal{N}^{-1}\left(1-\frac{\Delta_1^c}{D_{\rm for}}\right)$                    | $\sigma_{\text{atm}} \, \sqrt{T} \, < \, \sqrt{2 \ln \left( \frac{D_{\text{for}}}{2 \Delta_1^c} \right)}$ |
| Forward delta p.a. | $\sigma_{\text{atm}} \sqrt{T} < 2\mathcal{N}^{-1} \left(1 - \Delta_1^c\right)$                                     | $\sigma_{\text{atm}} \sqrt{T} < \sqrt{2 \ln \left( \frac{1}{2 \Delta_1^c} \right)}$                       |

<table>

 **Table 2** Restrictions on discount factors and ATM volatilities for various combinations
 of delta and ATM types<sup>(a)</sup>

(a) If these conditions are violated, the ATM point will cross the nearest OTM point. Note that the put delta  $\Delta_1^p$  is negative

OTM point  $\Delta_1^c$  only if

$$\sigma_{\text{atm}}\sqrt{T} < -2\mathcal{N}^{-1}\left(\frac{\Delta_1^c}{D_{\text{for}}}\right) = 2\mathcal{N}^{-1}\left(1 - \frac{\Delta_1^c}{D_{\text{for}}}\right) \tag{47}$$

This inequality has meaningful solutions only if the right-hand side is positive, that is, only if  $1 - \Delta_1^c/D_{\text{for}} > 1/2$ . We therefore have the additional constraint:

$$D_{\text{for}} > 2\Delta_1^c \tag{48}$$

The derivations for all other possible combinations are analogous. Their results are summarized in Table 2.

Numerical Example. To gain some intuition for these constraints, let us consider a numerical example for a relevant case. A typical combination of delta and ATM conventions for long-dated FX options is the ATM-type delta neutral for premiumadjusted forward deltas. Usually, the first OTM point is quoted at  $\Delta_1^c = 0.25$ . Inserting this value into the respective formula (see Table 2) yields the condition

$$\sigma_{\text{atm}}\,\sqrt{T} < \sqrt{2\ln\left(\frac{1}{2\Delta_1^c}\right)} = \sqrt{2\ln(2)} \approx 1.1774\tag{49}$$

For a 30-year option, this condition restricts the ATM volatility to a maximum of 21.5%, a value that—*a priori*—does not seem unattainable.

## Ambiguities in the Conversion from $\Delta$ to Strike for Premium-adjusted Deltas

Premium-adjusted deltas can cause further complications. Recall from the section Forward Delta Premium Adjusted

$$\Delta_F^c = \frac{K}{F} \mathcal{N}(d_-)$$
  
where  $d_- = \frac{\ln(F/K) - 1/2\sigma^2 \tau}{\sigma\sqrt{\tau}}$  (50)

and note that  $\Delta_F^c$  is **not** a monotonous function of the strike  $K$  and therefore not invertible for all strikes as illustrated by Figure 1(a). Thus, while  $\Delta_F^c$  can be calculated for any strike  $K$ , the reverse is not true: for any  $\Delta_F^c < \Delta_{\text{max}}$ , there are two strikes  $K_1 \neq K_2$ with  $\Delta_F^c(K_1) = \Delta_F^c(K_2)$ .

In case  $K_{\text{max}} < K_{\text{atm}}$ , there is no problem.  $\Delta_{F, pa}^{c}(K)$  is a monotone function of K for all  $K > K_{\text{atm}}$  and is therefore directly related to the option's moneyness: the smaller a call option's delta value, the higher its strike and the deeper it is OTM. If desired, the volatility smile table defined in terms of delta can be translated uniquely into a smile table in strikes. Besides, when retrieving volatilities from the call side of the volatility

![](_page_9_Figure_1.jpeg)

**Figure 1** (a) Premium adjusted (forward) call delta as a function of strike. (b) The function  $f_{\alpha}(x)$  as defined in equation (56) for  $\alpha = 0.7$  (broken line) and  $\alpha = 1.1$  (solid line)

smile table, this can be done by direct interpolation of the entries, possibly including the ATM point.

In case  $K_{\text{max}} > K_{\text{atm}}$ , however, the situation is more complicated.  $\Delta_{F, pa}^{c}(K)$  is no longer a monotonous function of  $K$  and the conversion of deltas to strikes is no longer unique for all OTM options. Thus, when translating a smile table in deltas into a smile table in strikes, particular care has to be taken. In addition, when retrieving the volatility for options with strikes  $K \in (K_{\text{atm}}; K_{\text{max}})$  from the volatility smile table, one has to extrapolate volatilities in delta beyond the ATM point which seems odd.

Note that the counterintuitive extrapolation in delta beyond the ATM point does not occur in case the volatility smile table in deltas is translated to a table in strikes on the grid points first (see the section Using the Smile Volatility Table) and the interpolation is done in strikes. This is possible as long as there is no crossing of the ATM point and the closest delta grid point as discussed in the section ATM Delta Falling in the OTM Range.

In the following discussion, we show that the case  $K_{\text{max}} > K_{\text{atm}}$  can, indeed, occur. We restrict ourselves to premium adjusted forward call deltas and ATM-type delta neutral. The conditions for the ATM-type forward can be derived analogously and we summarize the results at the end of this section. Similar arguments hold for premium-adjusted spot deltas, however, it is reasonable to assume that the problems outlined in the section ATM Delta Falling in the OTM Range surface beforehand.

Starting from the expressions for the ATM strike and the call delta, see Table 1,

$$K_{\text{atm}} = F e^{-1/2\sigma_{\text{atm}}^2 T} \tag{51}$$

$$\Delta_{\text{atm}}^c = \Delta_{F, pa}^c \left( K_{\text{atm}}, \sigma_{\text{atm}}^2 \right) = \frac{1}{2} e^{-1/2\sigma_{\text{atm}}^2 T} \quad (52)$$

we need to find conditions under which there is a second solution with strike  $K > K_{\text{atm}}$  that solves

$$\Delta_{\text{atm}}^{c} = \Delta_{F, \, pa}^{c} \left( K, \sigma(\Delta_{F, \, pa}^{c}) \right) \tag{53}$$

This may seem a difficult problem at first glance since the delta on the right-hand side depends on the volatility, which itself is given in terms of delta. It is, however, simplified considerably by the following argument: while we do not know the strike for the point that solves equation  $(53)$ , we do know the delta there: it is the ATM delta. As the volatility is given in terms of delta, we also know the volatility on the right-hand side of equation  $(53)$ : it must be the ATMvolatility  $\sigma_{\text{atm}}$ .

Therefore, the problem can be reformulated as follows: when does

$$\Delta_{\text{atm}}^{c} = \Delta_{F, \ pa}^{c} \left( K, \sigma_{\text{atm}} \right) \tag{54}$$

have a second solution with  $K > K_{\text{atm}}$  (besides the trivial one at  $K = K_{\text{atm}}$ ?

Inserting the expressions for the ATM delta and the premium-adjusted forward call delta into equation  $(54)$  we get

$$\frac{1}{2} e^{-1/2\sigma_{\text{atm}}^2 T} = \frac{K}{F} \mathcal{N} \left( \frac{\ln \left( F/K \right) - 1/2\sigma_{\text{atm}}^2 T}{\sigma_{\text{atm}} \sqrt{T}} \right) \tag{55}$$

With the definitions

$$\begin{split} \alpha &:= \sigma_{\text{atm}} \sqrt{T} \ , \ x &:= \frac{K}{F} \, \text{e}^{1/2 \sigma_{\text{atm}}^2 T} = \frac{K}{F} \, \text{e}^{\alpha^2/2} \end{split}$$

the problem is equivalent to finding the roots of

$$f_{\alpha}(x) := e^{-\alpha^2/2} \left\{ \frac{1}{2} - x\mathcal{N}\left(-\frac{\ln(x)}{\alpha}\right) \right\} \quad (56)$$

The condition  $K > K_{\text{atm}}$  in the previous equation corresponds to  $x > 1$ . Plotting  $f_{\alpha}(x)$  for various values of  $\alpha$ , see Figure 1(b), we make the following observation: for small values of  $\alpha$  the function increases monotonically, taking on only positive values for  $x > 1$ . For larger values of  $\alpha$ , the function decreases at first, thus, taking on negative values in a certain range, and then increases again, eventually reaching a second zero.

Therefore, the question reduces further to this: under which conditions does the function  $f_{\alpha}(x)$  have a negative slope at  $x = 1$ ? The first derivative of  $f_{\alpha}$ can easily be calculated,

$$f'_{\alpha}(x) = -e^{-\alpha^2/2} \left\{ \mathcal{N}\left(-\frac{\ln(x)}{\alpha}\right) - \frac{1}{\alpha} \mathcal{N}'\left(-\frac{\ln(x)}{\alpha}\right) \right\}$$
(57)

and the slope of  $f_{\alpha}$  at  $x = 1$  is now readily obtained as

$$f'_{\alpha}(x=1) = -e^{-\alpha^{2}/2} \left\{ \mathcal{N}(0) - \frac{1}{\alpha} \mathcal{N}'(0) \right\}$$
$$= -e^{-\alpha^{2}/2} \left\{ \frac{1}{2} - \frac{1}{\alpha} \frac{1}{\sqrt{2\pi}} \right\} \qquad (58)$$

The constraint that it has to be positive yields the condition

$$\alpha = \sigma_{\text{atm}} \sqrt{T} < \sqrt{\frac{2}{\pi}} \tag{59}$$

which restricts the ATM volatitity for a 30-year option to only  $14.6\%$ .

In other words, for a 30-year option, with ATM volatilities larger than 14.6%, the conversion between  $\Delta_{F, pa}$  and strikes becomes ambiguous.

A similar condition can be derived for the forward ATM type. The major difference is that the function  $f_{\alpha}(x)$  takes on a different form that ultimately yields the following expression for the turnover point  $\alpha$  at which the conversion becomes ambiguous:

$$\mathcal{N}\left(-\frac{\alpha}{2}\right) = \frac{1}{\alpha}\mathcal{N}'\left(-\frac{\alpha}{2}\right) \tag{60}$$

This equation can be solved numerically and vields the constraint

$$\alpha = \sigma_{\text{atm}} \sqrt{T} < 1.224 \tag{61}$$

so that for a 30-year option, ATM volatilities above 22.3% will lead to ambiguities.

### **End Notes**

<sup>a.</sup>It should be noted that equation (32) was obtained under the assumption that the slope of the volatility  $\sigma$  as a function of the strike  $K$  in equation (31) is 0 ATM. This is necessary as otherwise this ATM definition would become impracticable. In general, however, the volatility smile implies a nonzero slope and the maximum value of  $\gamma$  will not be found at the strike given by equation  $(32)$ .

### References

- [1] Borowski, B. (2005). Hedgingverfahren für Foreign Exchange Barrieroptionen, Diploma Thesis, Technical University of Munich.
- [2] Carr, P. & Bandyopadhyay, A. (2000). *How to derive the* Black-Scholes Equation Correctly? http://faculty.chicagogsb.edu/akash.bandyopadhyay/research/ (accessed Mar 2000).
- [3] Hull, J.C. (1997). Options, Futures and Other Derivative Securities, 3rd Edition, Prentice Hall, NJ.
- [4] Wystup, U. (2006). FX Options and Structured Products, Wilev.

#### **Related Articles**

Foreign Exchange Markets; Foreign Exchange Symmetries; Foreign Exchange Smile Interpolation.
# **Foreign Exchange** Symmetries

## Motivation

The symmetries of the foreign exchange (FX) market are the key features that distinguish this market from all others. With an EUR-USD exchange rate of 1.2500 USD per EUR, there is an equivalent USD-EUR exchange rate of 0.8000 EUR per USD, which is just the reciprocal. Any model  $S_t$  for an exchange rate at time t should guarantee that  $1/S_t$  is within the same model class. This is satisfied by the Black-Scholes model or local volatility models, but not for many stochastic volatility models.

The further symmetry is that both currencies pay interest, which we can assume to be continuously paid. The FX market is the only market where this really works.

In the EUR-USD market, any EUR call is equivalent to an USD put. Any premium in USD can be also paid in EUR, any delta hedge can be specified in the amount of USD to sell or, alternatively, the amount of EUR to buy.

Furthermore, if  $S_1$  is a model for EUR-USD and  $S_2$  is a model for USD-JPY, then  $S_3 = S_1 \cdot S_2$  should be a model for EUR-JPY. Therefore, besides the reciprocals, the products of two modeling quantities should also remain within the same model class.

Finally, the smile of an FX options market is summarized by Risk Reversals and Butterflies, the skew-symmetric part and the symmetric part of a smile curve.

In no other market are symmetries so prominent and so heavily used as in FX. It is this special feature that makes it hard for many newcomers to capture the way FX options market participants think.

# **Geometric Brownian Motion Model** for the Spot

We consider the model geometric Brownian motion

$$dS_t = (r_d - r_f)S_t dt + \sigma S_t dW_t \qquad (1)$$

for the underlying exchange rate quoted in foreigndomestic (FOR-DOM), which means that 1 unit of the foreign currency costs FOR-DOM units of the domestic currency. In the case of EUR-USD with a spot of  $1.2000$ , this means that the price of  $1 \text{ EUR}$  is 1.2000 USD. The notions of foreign and domestic do not refer to the location of the trading entity, but only to this quotation convention. We denote the (continuous) foreign interest rate by  $r_f$  and the (continuous) domestic interest rate by  $r_d$ . In an equity scenario,  $r_f$  would represent a continuous dividend rate. The volatility is denoted by  $\sigma$ , and  $W_t$  is a standard Brownian motion.

We consider this standard model, not because it reflects the statistical properties of the exchange rate (in fact, it does not), but because it is widely used in practice and front office systems and mainly serves as a tool to communicate prices in FX options. These prices are generally quoted in terms of volatility in the sense of this model.

# Vanilla Options

The payoff for a vanilla option (European put or call) is given by

$$F = [\phi(S_T - K)]^+ \tag{2}$$

where the contractual parameters are the strike  $K$ , the expiration time T and the type  $\phi$ , a binary variable, which takes the value  $+1$  in the case of a call and  $-1$  in the case of a put. The symbol  $x^+$  denotes the positive part of x, that is,  $x^+ = \max(0, x) = 0 \vee x$ .

#### Value

In the Black-Scholes model, the value of the payoff F at time t if the spot is at S is denoted by  $v(t, S)$ . The result is the Black-Scholes formula

$$v(S, K, T, t, \sigma, r_d, r_f, \phi)$$
  
=  $\phi e^{-r_d \tau} \left[ f \mathcal{N}(\phi \, \mathbf{d}_+) - K \mathcal{N}(\phi \, \mathbf{d}_-) \right]$ (3)

We abbreviate

- $S$ : current price of the underlying
- $\tau = T t$ : time to maturity
- $f = \mathbb{E}[S_T | S_t = S] = S e^{(r_d r_f)\tau}$ : forward price of the underlying

$$\bullet \qquad \theta_{\pm} = \frac{r_d - r_f}{\sigma} \pm \frac{\sigma}{2}$$

$$\bullet \quad d_{\pm} = \frac{\ln\frac{S}{K} + \sigma\theta_{\pm}\tau}{\sigma\sqrt{\tau}} = \frac{\ln\frac{f}{K} \pm \frac{\sigma^{2}}{2}\tau}{\sigma\sqrt{\tau}}$$

• 
$$n(t) = \frac{1}{\sqrt{2\pi}} e^{-2^{t}} = n(-t)$$

$$\bullet \quad \mathcal{N}(x) = \int_{-\infty}^{x} n(t) \, \mathrm{d}t = 1 - \mathcal{N}(-x)$$

## A Note on the Forward

The *forward price*  $f$  is the strike that makes the time zero value of the forward contract

$$F = S_T - f \tag{4}$$

equal to zero. It follows that  $f = \mathbb{E}[S_T] =$  $Se^{(r_d-r_f)\cdot T}$ , that is, the forward price is the expected price of the underlying at time  $T$  in a risk-neutral setup (drift of the geometric Brownian motion is equal to the cost of carry  $r_d - r_f$ ).

## Greeks

Greeks are derivatives of the value function with respect to model and contract parameters. They are an important information for traders and have become standard information provided by front-office systems. More details on Greeks and the relations among Greeks are presented in [5] or [6]. We now list some of them for vanilla options:

Spot delta. The spot delta shows how many units . of FOR in the spot must be traded to hedge an option with 1 unit of FOR notional.

$$\frac{\partial v}{\partial S} = \phi e^{-r_f \tau} \mathcal{N}(\phi d_+)$$
 (5)

• Forward delta. The forward delta shows how many units of FOR of a forward contract must be traded to hedge an option with 1 unit of FOR notional.

$$\phi \mathcal{N}(\phi \, \mathrm{d}_{+}) = I\!\!P \left[ \phi S_T \le \phi \frac{f^2}{K} \right] \qquad (6)$$

It is also equal to the risk-neutral exercise probability or in-the-money probability of the symmetric put (see Section  $1.4.3$ ).

• Gamma.

$$\frac{\partial^2 v}{\partial S^2} = e^{-r_f \tau} \frac{n(\mathbf{d}_+)}{S\sigma\sqrt{\tau}} \tag{7}$$

Vega.

$$\frac{\partial v}{\partial \sigma} = S e^{-r_f \tau} \sqrt{\tau} n(\mathbf{d}_+) \tag{8}$$

Dual delta.  $\bullet$ 

$$\frac{\partial v}{\partial K} = -\phi e^{-r_d \tau} \mathcal{N}(\phi d_-) \tag{9}$$

The forward dual delta

$$\mathcal{N}(\phi \, \mathrm{d}_{-}) = \mathit{IP}[\phi S_{T} \ge \phi K] \tag{10}$$

can also be viewed as the risk-neutral exercise probability.

Dual gamma.

$$\frac{\partial^2 v}{\partial K^2} = e^{-r_d \tau} \frac{n(\mathbf{d}_-)}{K \sigma \sqrt{\tau}} \tag{11}$$

#### Identities

Any computations with vanilla options often rely on the symmetry identities

$$\frac{\partial \mathbf{d}_{\pm}}{\partial \sigma} = -\frac{\mathbf{d}_{\mp}}{\sigma} \tag{12}$$

$$\frac{\partial \mathbf{d}_{\pm}}{\partial r_d} = \frac{\sqrt{\tau}}{\sigma} \tag{13}$$

$$\frac{\partial \mathbf{d}_{\pm}}{\partial r_{f}} = -\frac{\sqrt{\tau}}{\sigma} \tag{14}$$

$$S e^{-r_f \tau} n(d_+) = K e^{-r_d \tau} n(d_-)$$
 (15)

## Put-Call Parity

The *put-call parity* is the relationship,

$$v(S, K, T, t, \sigma, r_d, r_f, +1) - v(S, K, T, t, \sigma, r_d, r_f, -1) = Se^{-r_f \tau} - Ke^{-r_d \tau}$$
(16)

which is just a more complicated way to write the trivial equation  $x = x^+ - x^-$ . Taking the strike K to be equal to the forward price  $f$ , we see that the call and put have the same value. The forward is the center of symmetry for vanilla call and put values. However, this does not imply that the *deltas* are also symmetric about the forward price.

The  $put-call\ delta\ parity$  is

$$\frac{\partial v(S, K, T, t, \sigma, r_d, r_f, +1)}{\partial S} - \frac{\partial v(S, K, T, t, \sigma, r_d, r_f, -1)}{\partial S} = e^{-r_f \tau} \quad (17)$$

In particular, we learn that the absolute value of a put delta and a call delta do not exactly add up to 1, but only to a positive number  $e^{-r_f \tau}$ . They add up to 1 approximately if either the time to expiration  $\tau$  is short or if the foreign interest rate  $r_f$  is close to 0. For this reason, traders often prefer to work with forward deltas, because these are symmetric in the sense that a 25-delta call is a 75-delta put.

Although the choice  $K = f$  produces identical values for call and put, we seek the *delta-symmetric strike*  $\check{K}$ , which produces absolutely identical deltas (spot, forward, or driftless). This condition implies  $d_{+} = 0$  and thus

$$\check{K} = f e^{\frac{\sigma^2}{2}\tau} \tag{18}$$

in which case the absolute delta is  $e^{-r_f\tau}/2$ . In particular, we learn that always  $\check{K} > f$ , that is, there cannot be a put and a call with identical values and deltas. This is natural as the payoffs of calls and puts are not symmetric to start with: the call has unlimited upside potential, whereas the put payoff is always bounded by the strike. Note that the strike  $K$ is usually chosen as the middle strike when trading a straddle or a butterfly. Similarly the dual-deltasymmetric strike  $\hat{K} = f e^{-\frac{\sigma^2}{2}\tau}$  can be derived from the condition  $d_{-} = 0$ .

Note that the delta-symmetric strike  $\check{K}$  also maximizes gamma and vega of a vanilla option and is thus often considered as a center of symmetry.

# **Homogeneity-based Relationships**

#### Space Homogeneity

We may wish to measure the value of the underlying in a different unit. This will obviously effect the option pricing formula as follows:

$$av(S, K, T, t, \sigma, r_d, r_f, \phi)$$
  
=  $v(aS, aK, T, t, \sigma, r_d, r_f, \phi)$  for all  $a > 0$   
(19)

Differentiating both sides with respect to  $a$  and then setting  $a = 1$  yields

$$v = Sv_S + Kv_K \tag{20}$$

Comparing the coefficients of  $S$  and  $K$  in equations  $(3)$  and  $(20)$  leads to suggestive results for the delta  $v_S$  and dual delta  $v_K$ . This *space-homogeneity* is the reason behind the simplicity of the delta formulas, whose tedious computation can be saved this way.

## Time Homogeneity

We can perform a similar computation for the timeaffected parameters and obtain the obvious equation

$$v(S, K, T, t, \sigma, r_d, r_f, \phi)$$
  
=  $v\left(S, K, \frac{T}{a}, \frac{t}{a}, \sqrt{a}\sigma, ar_d, ar_f, \phi\right)$   
for all  $a > 0$  (21)

Differentiating both sides with respect to  $a$  and then setting  $a = 1$  yields

$$0 = \tau v_t + \frac{1}{2}\sigma v_{\sigma} + r_d v_{r_d} + r_f v_{r_f} \tag{22}$$

Of course, this can also be verified by direct computation. The overall use of such equations is to generate double checking benchmarks when computing Greeks. These homogeneity methods can easily be extended to other more complex options.

## Put-Call Symmetry

By  $put\text{-}call$  symmetry, we understand the relationship (see  $[1-4]$ )

$$v(S, K, T, t, \sigma, r_d, r_f, +1)$$

$$= \frac{K}{f} v\left(S, \frac{f^2}{K}, T, t, \sigma, r_d, r_f, -1\right) \quad (23)$$

The geometric mean of the strike of the put  $\frac{f^2}{K}$ and the strike of the call *K* is equal to  $\sqrt{\frac{f^2}{K}} \cdot K = f$ , the outright forward rate. Therefore, the outright forward rate can be interpreted as a *geometric mirror* reflecting a call into a certain number of puts. Note that for at-the-money (forward) options  $(K = f)$  the put-call symmetry coincides with the special case of the put-call parity where the call and the put have the same value.

## Rates Symmetry

Direct computation shows that the *rates symmetry* 

$$\frac{\partial v}{\partial r_d} + \frac{\partial v}{\partial r_f} = -\tau v \tag{24}$$

holds for vanilla options. This relationship, in fact, holds for all European options and a wide class of path-dependent options as shown in [6].

#### Foreign–Domestic Symmetry

One can directly verify the *FOR-DOM* symmetry

$$\frac{1}{S}v(S, K, T, t, \sigma, r_d, r_f, \phi)$$
$$= Kv\left(\frac{1}{S}, \frac{1}{K}, T, t, \sigma, r_f, r_d, -\phi\right) \quad (25)$$

This equality can be viewed as one of the faces of put-call symmetry. The reason is that the value of an option can be computed both in a domestic as well as in a foreign scenario. We consider the example of  $S_t$  modeling the exchange rate of EUR/USD. In New York, the call option  $(S_T - K)^+$  costs  $v(S, K, T, t, \sigma, r_{usd}, r_{eur}, 1)$  USD and hence  $v(S, K, T, t, \sigma, r_{usd}, r_{eur}, 1)/S$  EUR. This EUR call option can also be viewed as an USD put option with payoff  $K\left(\frac{1}{K}-\frac{1}{S_T}\right)^+$ . This option costs  $Kv\left(\frac{1}{S}, \frac{1}{K}, T, t, \sigma, r_{\text{eur}}, r_{\text{usd}}, -1\right)$  EUR in Frankfurt, because  $S_t$  and  $\frac{1}{S_t}$  have the same volatility. Of course, the New York value and the Frankfurt value must agree, which leads to equation (25). This can also be seen as a change of measure to the foreign discount bond as numeraire (see, e.g., in [7]).

## **Exotic Options**

In FX markets, one can use many symmetry relationships for exotic options.

## Digital Options

For example, let us define the payoff of digital options by

DOM paying: 
$$\mathbb{1}_{\{\phi S_T > \phi K\}}$$
 (26)

FOR paying: 
$$S_T \mathbb{1}_{\{\phi S_T \ge \phi K\}}$$
 (27)

where the contractual parameters are the strike  $K$ , the expiration time T, and the type  $\phi$ , a binary variable, which takes the value  $+1$  in the case of a call and  $-1$ in the case of a put. Then we observe that a DOMpaying digital call in the currency pair FOR-DOM with a value of  $v_d$  units of domestic currency must be worth the same as a FOR-paying digital put in the currency pair DOM-FOR with a value of  $v_f$  units of foreign currency. And since we are looking at the same product, we conclude that  $v_d = v_f \cdot S$ , where S is the initial spot of FOR-DOM.

#### **Touch Options**

This key idea generalizes from the path-independent digitals to touch products. Consider the value function for one-touch in EUR-USD paying 1 USD. If we want to find the value function of a one-touch in EUR-USD paying 1 EUR, we can price the one-touch in USD-EUR paying 1 EUR using the known value function with rates  $r_d$  and  $r_f$  exchanged, volatility unchanged, using the formula for a one-touch in EUR-USD paying 1 USD. We also note that an upper one-touch in EUR-USD becomes a lower onetouch in USD-EUR. The result we get is in domestic currency, which is EUR in USD-EUR notation. To convert it into an USD price, we just multiply by the  $EUR-USD$  spot  $S$ .

## Barrier Options

For a standard knockout barrier option, we let the value function be

$$v(S, r_d, r_f, \sigma, K, B, T, t, \phi, \eta) \tag{28}$$

where *B* denotes the barrier and the variable  $\eta$  takes the value  $+1$  for a lower barrier and  $-1$  for an upper barrier. With this notation at hand, we can state our FOR-DOM symmetry as

$$v(S, r_d, r_f, \sigma, K, B, T, t, \phi, \eta)$$
  
=  $v\left(\frac{1}{S}, r_f, r_d, \sigma, \frac{1}{K}, \frac{1}{B}, T, t, -\phi, -\eta\right) SK$   
(29)

Note that the rates  $r_d$  and  $r_f$  have been interchanged on purpose. This implies that if we know how to price barrier contracts with upper barriers, we can derive the formulas for lower barriers.

# **Ouotation**

Quotation of the Underlying Exchange Rate

Equation  $(1)$  is a model for the exchange rate. The quotation is a permanently confusing issue, so let us clarify this here. The exchange rate means how much of the *domestic* currency are needed to buy 1 unit of foreign currency. For example, if we take EUR/USD as an exchange rate, then the default quotation is EUR-USD, where USD is the domestic currency and EUR is the foreign currency. The term *domestic* is in no way related to the location of the trader or any country. It merely means the *numeraire* currency. The terms *domestic*, *numeraire*, or *base currency* are synonyms as are *foreign* and *underlying* . Commonly, we denote with the slash  $(/)$  the currency pair and with a dash  $(-)$  the quotation. The slash  $(/)$  does *not* mean a division. For instance, EUR/USD can also be quoted in either EUR-USD, which then means how many USD are needed to buy one EUR, or in USD-EUR, which then means how many EUR are needed to buy 1 USD. There are certain market standard quotations listed in Table 1.

#### Quotation of Option Prices

Values and prices of vanilla options may be quoted in the six ways explained in Table 2.

The Black-Scholes formula quotes an option value in units of domestic currency per unit of foreign notional. Since this is usually a small number, it is often multiplied with 10000 and quoted as domestic

Table 1 Standard market quotation of major currency pairs with sample spot prices

| Default quotation | Sample quote |
|-------------------|--------------|
| $\text{GPB-USD}$  | 1.8000       |
| GBP-CHF           | 2.2500       |
| EUR-USD           | 1.2000       |
| EUR-GBP           | 0.6900       |
| EUR-JPY           | 135.00       |
| EUR-CHF           | 1.5500       |
| USD-JPY           | 108.00       |
| USD-CHF           | 1.2800       |
|                   |              |

pips per foreign, in short, **d pips**. The others can be computed using the following instruction:

$$\mathbf{d} \ \mathbf{pips} \stackrel{\times \frac{1}{S}}{\longrightarrow} \mathcal{C} \mathbf{f} \stackrel{\times \frac{S}{K}}{\longrightarrow} \mathcal{C} \mathbf{d} \stackrel{\times \frac{1}{S}}{\longrightarrow} \mathbf{f} \ \mathbf{pips} \stackrel{\times SK}{\longrightarrow} \mathbf{d} \ \mathbf{pips} \qquad (30)$$

#### Delta and Premium Convention

The spot delta of a European option without premium-adjustment is well known. It will be called raw spot delta  $\delta_{raw}$  now and denotes the amount of FOR to buy when selling an option with 1 unit of FOR notional. However, the same option can also be viewed as an option with K units of DOM notional. The delta that goes with the same option, but 1 unit of DOM notional and tells how many units of DOM currency must be sold for the delta hedge is denoted by  $\delta_{\text{raw}}^{\text{reverse}}$ . In the market, both deltas can be quoted in either of the two currencies involved. The relationship is

$$\delta_{\text{raw}}^{\text{reverse}} = -\delta_{\text{raw}} \frac{S}{K} \tag{31}$$

The delta is used to buy or sell spot in the corresponding amount in order to hedge the option up

**Table 2** Standard market quotation types for option values. In the example, we take  $FOR = EUR$ ,  $DOM = USD$ ,  $S = 1.2000$ ,  $r_d = 3.0\%$ ,  $r_f = 2.5\%$ ,  $\sigma = 10\%$ ,  $K = 1.2500$ ,  $T = 1$  year,  $\phi = +1$  (call), notional = 1000000 EUR = 1 250 000 USD. For the pips, the quotation 291.48 USD pips per EUR is also sometimes stated as 2.9148% USD per 1 EUR. Similarly, the 194.32 EUR pips per USD can also be quoted as 1.9432% EUR per 1 USD

| Name                                                     | Symbol                                          | Value in units of                                                                        | Example                                                                          |  |  |
|----------------------------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--|--|
| Domestic cash                                            |                                                 | DOM                                                                                      | 29 148 USD                                                                       |  |  |
| Foreign cash                                             |                                                 | FOR                                                                                      | 24 290 EUR                                                                       |  |  |
| % domestic<br>% foreign<br>Domestic pips<br>Foreign pips | $\% \mathbf{d}$<br>$\%$ f<br>d pips<br>$f$ pips | DOM per unit of DOM<br>FOR per unit of FOR<br>DOM per unit of FOR<br>FOR per unit of DOM | 2.3318% USD<br>2.4290% EUR<br>291.48 USD pips per EUR<br>194.32 EUR pips per USD |  |  |

to first order. To interpret this relationship, note that the minus sign refers to selling DOM instead of buying FOR, and the multiplication by  $S$  adjusts the amounts. Furthermore, we divide by the strike, because a call on 1 EUR corresponds to  $K$  USD puts. More details on delta conventions are contained in Foreign Exchange Options: Delta- and At-themoney Conventions

For consistency, the premium needs to be incorporated into the delta hedge, since a premium in foreign currency will already hedge part of the option's delta risk. To make this clear, let us consider EUR-USD. In the standard arbitrage theory,  $v(S)$  denotes the value or premium in USD of an option with 1 EUR notional, if the spot is at S, and the raw delta  $v_S$ denotes the number of EUR to buy for the delta hedge. Therefore,  $Sv_S$  is the number of USD to sell. If now the premium is paid in EUR rather than in USD, then we already have  $\frac{v}{S}$  EUR, and the number of EUR to buy has to be reduced by this amount, that is, if EUR is the premium currency, we need to buy  $v_S - v/S$  EUR for the delta hedge or equivalently sell  $Sv_S - v$  USD.

To quote an FX option, we need to first sort out which currency is domestic, which is foreign, what is the notional currency of the option, and what is the premium currency. Unfortunately, this is not symmetric, since the counterparty might have another notion of domestic currency for a given currency pair. Hence, in the professional interbank market, there is one notion of delta per currency pair. Normally, it is the left-hand side delta of the  $Fenics<sup>a</sup>$  screen if the option is traded in left-hand side premium, which is normally the standard and right-hand side delta if it is traded with right-hand-side premium, for example, EUR/USD lhs, USD/JPY lhs, EUR/JPY lhs, AUD/USD rhs, and so on. Since OTM options are traded most of the time, the difference is not huge and hence does not create a huge spot risk.

Additionally, the standard delta per currency pair (left-hand-side delta in *Fenics* for most cases) is used to quote options in volatility. This has to be specified by currency pair.

This standard interbank notion must be adapted to the real delta risk of the bank for an automated trading system. For currency pairs where the riskfree currency of the bank is the domestic or base currency, it is clear that the delta is the raw delta of the option, and for risky premium this premium must be included. In the opposite case, the risky premium and the market value must be taken into account for the base currency premium, such that these offset each other. And for premium in underlying currency of the contract, the market value needs to be taken into account. In this way, the delta hedge is invariant with respect to the risky currency notion of the bank, for example, the delta is the same for a USD-based bank and an EUR-based bank.

# Example

We consider two examples in Tables 3 and 4 to compare the various versions of deltas that are used in practice.

# **Greeks in Terms of Deltas**

In FX markets, the moneyness of vanilla options is always expressed in terms of deltas and prices

**Table 3** 1 y EUR call USD put strike  $K = 0.9090$  for a EUR-based bank. Market data: spot  $S = 0.9090$ , volatility  $\sigma = 12\%$ , EUR rate  $r_f = 3.96\%$ , USD rate  $r_d = 3.57\%$ . The raw delta is 49.15%EUR and the value is 4.427%EUR

| Delta<br>currency          | Prem<br>currency  | Fenics                                                                      | Formula                                                                           | Delta                      |
|----------------------------|-------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------|
| % EUR<br>$\%$ EUR<br>% USD | EUR<br>USD<br>EUR | lhs<br>rhs<br>rhs<br>$\begin{bmatrix} \text{flip } \text{F4} \end{bmatrix}$ | $\delta_{\text{raw}} - P$<br>$\delta_{raw}$<br>$-(\delta_{\text{raw}} -$<br>P)S/K | 44.72<br>49.15<br>$-44.72$ |
| % USD                      | USD               | lhs<br>[flip F4]                                                            | $-(\delta_{\text{raw}})S/K$                                                       | $-49.15$                   |

**Table 4** 1 y call EUR call USD put strike  $K = 0.7000$  for a EUR-based bank. Market data: spot  $S = 0.9090$ , volatility  $\sigma = 12\%$ , EUR rate  $r_f = 3.96\%$ , USD rate  $r_d = 3.57\%$ . The raw delta is 94.82%EUR and the value is 21.88%EUR

| Delta<br>currency | Prem<br>currency | Fenics                                                                                                           | Formula                            | Delta     |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------|-----------|
| % EUR             | EUR              | lhs                                                                                                              | $\delta_{\text{raw}} - P$          | 72.94     |
| % EUR             | USD              | rhs                                                                                                              | $\delta_{raw}$                     | 94.82     |
| % USD             | EUR              | rhs                                                                                                              | $-(\delta_{\text{raw}} -$          | $-94.72$  |
| % USD             | USD              | $\begin{bmatrix} \text{flip } \text{F4} \end{bmatrix}$<br>lhs<br>$\begin{bmatrix} \text{flip } F4 \end{bmatrix}$ | P)S/K<br>$-\delta_{\text{raw}}S/K$ | $-123.13$ |

are quoted in terms of volatility. This makes a 10delta call a financial object as such independent of spot and strike. This method and the quotation in volatility makes objects and prices transparent in a very intelligent and user-friendly way. At this point, we list the Greeks in terms of deltas instead of spot and strike. Let us introduce the quantities

$$\Delta_{+} \stackrel{\Delta}{=} \phi e^{-r_f \tau} \mathcal{N}(\phi \, \mathrm{d}_{+}) \text{ spot delta} \tag{32}$$

$$\Delta_{-} \stackrel{\Delta}{=} -\phi e^{-r_d \tau} \mathcal{N}(\phi \, \mathrm{d}_{-}) \text{ dual delta} \qquad (33)$$

which we assume to be given. From these we can retrieve

$$d_{+} = \phi \mathcal{N}^{-1} (\phi e^{r_f \tau} \Delta_{+}) \tag{34}$$

$$d_{-} = \phi \mathcal{N}^{-1}(-\phi e^{r_d \tau} \Delta_{-}) \tag{35}$$

## Interpretation of Dual Delta

The dual delta introduced in equation  $(9)$  as the sensitivity with respect to strike has another-more practical—interpretation in an FX setup. Recall from equation  $(25)$  that for vanilla options the domestic value

$$v(S, K, \tau, \sigma, r_d, r_f, \phi) \tag{36}$$

corresponds to a foreign value

$$v\left(\frac{1}{S},\frac{1}{K},\tau,\sigma,r_f,r_d,-\phi\right) \tag{37}$$

up to an adjustment of the nominal amount by the factor  $SK$ . From a foreign point of view, the delta is thus given by

$$-\phi e^{-r_d \tau} \mathcal{N} \left( -\phi \frac{\ln\left(\frac{1/S}{1/K}\right) + \left(r_f - r_d + \frac{1}{2}\sigma^2 \tau\right)}{\sigma\sqrt{\tau}} \right)$$
$$= -\phi e^{-r_d \tau} \mathcal{N} \left( \phi \frac{\ln\left(\frac{S}{K}\right) + \left(r_d - r_f - \frac{1}{2}\sigma^2 \tau\right)}{\sigma\sqrt{\tau}} \right)$$
$$= \Delta_{-} \tag{38}$$

which means that the dual delta is the delta from the foreign point of view.

Now, we list value, delta, and vega in terms of  $S, \Delta_+, \Delta_-, r_d, r_f, \tau, \text{ and } \phi.$ 

• Value.

$$v(S, \Delta_{+}, \Delta_{-}, r_{d}, r_{f}, \tau, \phi)$$
  
=  $S\Delta_{+} + S\Delta_{-} \frac{\mathrm{e}^{-r_{f}\tau}n(\mathrm{d}_{+})}{\mathrm{e}^{-r_{d}\tau}n(\mathrm{d}_{-})}$  (39)

Spot delta.

$$\frac{\partial v}{\partial S} = \Delta_+ \tag{40}$$

Vega.

$$\frac{\partial v}{\partial \sigma} = S e^{-r_f \tau} \sqrt{\tau} n(\mathbf{d}_+) \tag{41}$$

Notice that vega does not require knowing the dual delta.

Table 5 Vega in terms of Delta for the standard maturity labels and various deltas. It shows that one can neutralize a vega position of a long 9M 35 delta call with 4 short 1M 20 delta puts. This offsetting, however, is not a static, but only a momentary hedge

| $\text{Matrix}/\Delta$ | 50% | 45% | 40% | 35% | 30% | 25% | 20% | 15% | 10% | 5% |
|------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|
| 1D                     |     | 2   | 1   | 2   | 2   | 1   |     |     |     |    |
| 1W                     |     |     |     |     |     |     |     |     |     |    |
| 1W                     |     | 8   |     |     |     | 6   |     |     |     |    |
| 1M                     |     | 11  |     | 11  | 10  | Q   |     |     |     |    |
| 2M                     | 16  | 16  | 16  | 15  | 14  | 13  | 11  | 9   |     | 4  |
| 3M                     | 20  | 20  | 19  | 18  | 17  | 16  | 14  | 12  |     |    |
| 6M                     | 28  | 28  | 27  | 26  | 24  | 22  | 20  | 16  | 12  |    |
| 9M                     | 34  | 34  | 33  | 32  | 30  | 27  | 24  | 20  | 15  | 9  |
| $1\text{Y}$            | 39  | 39  | 38  | 36  | 34  | 31  | 28  | 23  | 17  | 10 |
| 2Y                     | 53  | 53  | 52  | 50  | 48  | 44  | 39  | 32  | 24  | 14 |
| 3Y                     | 63  | 63  | 62  | 60  | 57  | 53  | 47  | 39  | 30  | 18 |

*Vega in Terms of Delta*

The mapping

$$\Delta \mapsto v_{\sigma} = S e^{-r_f \tau} \sqrt{\tau} n(\mathcal{N}^{-1}(e^{r_f \tau} \Delta)) \tag{42}$$

is important for trading vanilla options. Observe that this function does not depend on *rd* or *σ*, just on *rf* . Quoting vega in % foreign will additionally remove the spot dependence. This means that for a moderately stable foreign term structure curve, traders will be able to use a moderately stable vega matrix. For *rf* = 3%, the vega matrix is presented in Table 5.

The most important result of this paragraph is the fact that vega can be written in terms of delta, which is the main reason why the FX market uses implied volatility quotation based on deltas in the first place.

# **End Notes**

a*.* Fenics is one of the standard tools for FX option pricing (see http://www.fenics.com/)

# **References**

[1] Bates, D. (1988). *Crashes, Options and International Asset Substitutability*. PhD Dissertation, Economics Department, Princeton University.

- [2] Bates, D. (1991). The crash of 1987—was it expected? The evidence from options markets, *The Journal of Finance* **46**, 1009–1044.
- [3] Bowie, J. & Carr, P. (1994). Static simplicity, *Risk Magazine* (7), 45–49. http://www.riskpublications.com
- [4] Carr, P. (1994). *European Put Call Symmetry*, Cornell University Working Paper.
- [5] Hakala, J. & Wystup, U. (2002). *Foreign Exchange Risk*, Risk Publications, London. http://www.mathfinance.com/ FXRiskBook/.
- [6] Reiss, O. & Wystup, U. (2001). Efficient computation of option price sensitivities using homogeneity and other tricks, *The Journal of Derivatives* **9**(2), 41–53.
- [7] Shreve, S.E. (2004). *Stochastic Calculus for Finance II*. Springer.

# **Further Reading**

Wystup, U. (2006). *FX Options and Structured Products*, Wiley Finance Series, Wiley. http://fxoptions.mathfinance.com/.

# **Related Articles**

**Black–Scholes Formula**; **Foreign Exchange Options: Delta- and At-the-money Conventions**; **Foreign Exchange Markets**; **Put–Call Parity**.

UWE WYSTUP
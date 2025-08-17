# **Options: Basic Definitions**

A financial *option* is a contract conferring on the holder the right, but not the obligation, to engage in some transaction, on precisely specified terms, at some time in the future. When the holder does decide to engage in the transaction, he/she is said to *exercise the option*. There are two parties to an option contract, generally known as the *writer* and the *buyer* or *holder*. The "optionality" accrues to the buyer; the writer has the obligation to carry out his/her side of the transaction, should the buyer exercise the option. An option is *vulnerable* if there is considered to be nonnegligible risk that the writer will fail to do this, that is, he/she will default on his/her side of the contract.

The classic contracts are European call and put options. A **call option** entitles the holder to purchase a specified number *N* of units of a security at a fixed price *K* per unit, at a specified time *T* . If *ST* is the market price of the security at time *T* , the holder will exercise the option if and only if *ST > K* (otherwise, it would be cheaper to buy in the market). Since the holder has now acquired for *K* per unit something that is worth *ST* , he/she makes a profit of *N (ST* − *K)*. Thus, in general, the profit is *N*[*ST* − *K*] <sup>+</sup> = *N* max*(ST* − *K,* 0*)*. Similarly, the profit on a contract, entitling the holder to *sell* at *K*, is *N*[*K* − *ST* ] <sup>+</sup>. The asset on which the option is written is called the *underlying asset*. A call option is *in the money* if *ST > K*, *at the money* (*ATM*) if *ST* = *K* and *out of the money* if *ST < K*. These terms are also used at earlier times *t<T* (e.g., ATM if *St* = *K* etc.) even though the option cannot be exercised then. An option is *ATM forward* at time *t* if *K* = *F (t, T )* where *F (t, T )* is the **forward price** at time *t* for purchase at time *T* .

# **Option Contracts**

In general, several assets may underlie a given contract, as for example in an **exchange option** where the holder has the right to exchange one asset for another. Options are sometimes called *contingent claims* or *derivative securities*. These two synonymous terms include options, but refer more generally to any contract whose value is a function of the values of some collection of underlying assets.

There are several binary classifications that help define an option contract.

## *European/American*

An option is European if it must be exercised, if at all, on a specified date, or a specified sequence of dates (for example, a *cap* is an **interest-rate option** consisting of a sequence of call options on the Libor rate; each of these options is exercised when they fall due if in the money). In an **American option**, by contrast, the time of exercise is at the holder's discretion. The classic American option involves a fixed final time *T* and allows the holder to exercise at any time *T* ≤ *T* , leaving the holder with the problem of determining an exercise strategy that will maximize the value to him. This immediately implies three things: (i) the value of an American option that has not already been exercised at any time *t* can never be less than the *intrinsic value* ([*K* − *St*] <sup>+</sup> for a put option), since one possible strategy is always to exercise *now*, (ii) the value can never be less than the value of the corresponding European option, since another possible strategy is never to exercise before *T* , and (iii) the value is a nondecreasing function of the final maturity time, since for *T*<sup>1</sup> *< T*<sup>2</sup> the *T*<sup>1</sup> option is just the *T*<sup>2</sup> option with the additional restriction that it never be exercised beyond *T*1. The difference between the American and European values for the same contract is called the *early exercise premium*. Sometimes, American options have some restriction on the set of allowable exercise times; for example, the conversion option in **convertible bonds** often prohibits the investor from converting before a certain minimum time. Of course, any such restrictions reduce the value since they reduce the class of exercise strategies. A particular case is the *Bermuda option*, which can only be exercised at one of a finite number of times. This is the normal situation in interest-rate options, where there is a natural sequence of *coupon dates* at which exercise decisions may be taken. Bermuda options are presumably so called because Bermuda is somewhere between America and Europe—but much closer to America.

## *Traded/OTC*

Traded options are those where the parties trade through the medium of an organized exchange, while "over the counter" (OTC) options are bilateral agreements between market counterparties. Option exchanges have become increasingly globalized in recent years. They include the US–European consortium NYSE Euronext, Chicago Mercantile Exchange (CME), Eurex and EDX, all of which offer a range of financial contracts, and a number of specialist commodity exchanges such as NYMEX (oil), ICE, and the London Metal Exchange (LME). An exchange offers contracts on an underlying asset such as an individual stock or a stock index such as the S&P500, with a range of maturity times and strike values. New options are added as the old ones roll off, and the strikes offered are in a range around the spot price of the underlying asset at the time the contract is initiated (the options may turn out to be far in or out of the money at later times, of course). In a traded options market, prices are determined by supply and demand. If the exercise times are *Ti* and the strike values *Kj* then the matrix *V* = [*σ*ˆ*ij* ], where *σ*ˆ*ij* is the **implied volatility** corresponding to the *(Ti, Kj )* contract, defines the so-called **volatility surface** that plays a key role in option risk management.

All interest-rate options and most FX (foreign exchange) options are OTC, but many are, nevertheless, very liquidly traded and market information on implied volatilities is readily available.

## *Physical Settlement/Cash Settlement*

Many single-stock options, and **commodity options** are *physically settled*, that is, at exercise the holder pays the strike value and takes delivery of a share certificate or a barrel of oil. (One can, however, avoid physical delivery by selling the option shortly before final maturity.) The alternative is *cash settlement*, where the holder is simply paid a cash amount, such as [*ST* − *K*] <sup>+</sup> for a call option, at exercise. When the underlying is an index like the S&P500 this is the only way—one cannot deliver the index! In this case, the amount paid is *c* × [*IT* − *K*] <sup>+</sup> where *IT* is the value of the index and *c* is the contractually specified dollar value of one index point.

## *Liquid/Illiquid*

Like any other traded asset, an option contract is **liquid** if there is large market depth, that is, there are a significant number of active traders in the market, none of whom controls a significant proportion of the total supply. In these circumstances, the price is well established, since the last trade was never very long ago; bid/ask spreads will be tight, buyers and sellers can enter the market at will, and there is little room for price manipulation. By contrast, in an illiquid market, it may be hard to establish a market price when actual trades are infrequent and bid/ask spreads are wide. The liquid/illiquid classification is not immutable: a liquid market can suddenly become illiquid if there is some shock that forces everybody onto the same side of the market. Several wellrecorded disasters in the derivatives market have been due to this phenomenon.

## *(Plain) Vanilla/Exotic*

The simplest, most standard, and most widely traded options are often referred to as *plain vanilla* options. This would certainly include all exchange-traded options. An "exotic" option is an OTC option with nonstandard features of some kind, which requires significant modeling effort to value, and where different analysts could well come up with significantly different valuations. Exotic options often involve several underlying assets and complicated payment streams, but even a simple call option can be exotic if it poses significant hedging difficulties, as for example do long-dated equity options. On the other hand, barrier options, for example, which once would have been considered exotic, have now become vanilla in some markets such as FX, because they are so widely traded.

## *Path-dependent/Path-independent*

An option is path-dependent if its exercise value depends on the value of the underlying asset at more than one time. Examples are barrier and Asian options, and any American option. The exercise value of a path-independent option is a function only of the underlying price, say *ST* , at the maturity time *T* , as for example in **Black–Scholes**. Valuation then only requires specifying the one-dimensional risk-neutral distribution of *ST* , whereas for a path-dependent option a distribution in path space is required, making the valuation more computationally intensive and model dependent.

## **Option Definitions**

The purpose of this section is to collect together introductory definitions of various option contracts, or features of option contracts, found in the market. We refer to specialist articles in this encyclopaedia for a detailed treatment, and to standard textbooks such as Hull [1]. In these definitions, we use  $S_t$  to denote a generic underlying asset price, on which is written an option that starts at time 0 with final maturity at time  $T$ .

#### Asian

An Asian option is one whose exercise value depends on the *average price* over some range of times. Generally, this is an arithmetic average of the form  $\overline{S} = (1/n) \sum_{i=1}^{n} S_{t_i}$  and, of course, in reality, it is always a finite sum, although for purposes of analysis it is often convenient to consider continuous averaging  $\overline{S}^c = (1/T) \int_0^T S_t dt$ . Averaging may be over the entire length of the contract or some much shorter period. For example, in commodity options call option values are generally based on the 10day or one-month average price immediately prior to maturity, rather than on the spot price, to deter market manipulation.

#### Barrier

A **barrier option** involves one or both of two prices, a lower barrier  $L < S_0$  and an upper barrier  $U > S_0$ , a strike *K*, and a maturity time *T*. Let  $\tau_L = \inf\{t : S_t \leq$ L},  $\tau_U = \inf\{t : S_t \ge U\}$  and  $\tau_{LU} = \min(\tau_L, \tau_U)$ . A knockout option expires worthless if a specified one of these times occurs before  $T$ , while a knockin option expires worthless unless this time occurs before  $T$ . An *up-and-out* call is a knockout call option based on  $\tau_{U}$ , so formally its exercise value is  $\mathbf{1}_{(\tau_U>T)}[S_T-K]^+$ . Similarly, an up-and-in call has exercise value  $\mathbf{1}_{(\tau_U \leq T)}[S_T - K]^+$ . The sum is an ordinary call option. There are analogous definitions for down-and-out and down-and-in options based on  $\tau_L$ . Normally, these would be put options. A double barrier option knocks out or in at time  $\tau_{LU}$ . In the Black-Scholes model, there is an analytic formula for single-barrier options, based on the reflection principle for Brownian motion, but double barrier options require numerical methods.

Knockout options are cheaper than their plain vanilla counterparts because the exercise value is strictly less with positive probability. Essentially, the buyer of a vanilla option pays a premium for events he/she may regard as overwhelmingly unlikely. By buying a barrier option instead, he/she avoids paying this premium.

### Basket

Consider a portfolio containing  $w_i$  units of asset *i* for  $i = 1, \ldots, n$ . A **basket** call option then has exercise value  $[X - K]^+$  where  $X = \sum_i w_i S_i(T)$  is the portfolio value at time  $T$ . The main problem in valuing basket options is the enormous number of correlation coefficients involved, for even moderate portfolio size  $n$ .

#### Bermuda

These were already mentioned above. Probably the most common example is the Bermuda swaption, entitling the holder to enter a swap at an agreed fixedside rate at any one of a list of coupon dates (or, equivalently, the right to walk away from an existing swap contract).

#### Chooser

A chooser option involves three times 0,  $T_1$ ,  $T_2$ , and a strike  $K$ . The option is entered and the strike set at time 0, and at time  $T_1$ , the holder selects whether it is to be a put or a call. The appropriate exercise value is then evaluated and paid at  $T_2$ . Thus the value at  $T_1$  is the maximum of the put and call values at that time. Given this fact valuation is straightforward in the Black-Scholes model.

#### Digital

A digital option pays a fixed cash amount if some condition is realized. For example, an up-and-in digital barrier option with maturity  $T$  and barrier level U will pay a fixed amount X if  $\tau_U < T$ . Payment might be made at  $\tau_U$  or at T.

#### Exchange

An **exchange option** has exercise value  $[aS_2(T) S_1(T)^{+}$ , that is, the holder has the right to exchange one unit of asset 1 for *a* units of asset 2 at the maturity time *T* . Exchange options can be priced by the Margrabe formula, originally introduced in [2].

## *Forward-starts, Ratchets, and Cliquets*

A involves two times 0 *< T*<sup>1</sup> *< T*2. The premium is paid at time 0 and the exercise value at final maturity *T*<sup>2</sup> is [*ST*<sup>2</sup> − *mST*<sup>1</sup> ] <sup>+</sup>, where *m* is a contractually specified "moneyness" factor. If, for example, *m* = 1*.*05, then effectively the strike is set at *T*<sup>1</sup> in such a way that the option is 5% out of the money at that time. This is a pure volatility play in that the value essentially only depends on the forward volatility between *T*<sup>1</sup> and *T*2. A ratchet or **cliquet** is a string of forward start options over times *Ti, Ti*+1, so *Ti*<sup>+</sup><sup>1</sup> is the maturity date for option *i* and the start date for option *i* + 1.

## *Lookback*

Let *S*max*(t)* = max*u*≤*<sup>t</sup> S(u)* and *S*min*(t)* = min*u*≤*<sup>t</sup> S(u)*. The exercise values of a **lookback** call and a lookback put are [*S(T )* − *S*min*(T )*] and [*S*max*(T )*− *S(T )*], respectively. The holders of these options can essentially buy at the minimum price and sell at the maximum price. Black–Scholes valuation of these options uses the reflection principle for Brownian motion, in the same way as for barrier options.

## *Passport*

A passport option is a call option where the underlying asset is a traded portfolio, and the holder has the right to choose the trading strategy in this portfolio.

## *Quanto*

A **quanto** or *cross-currency* option is written on an underlying asset denominated in currency A, but the exercise value is paid in currency B. For example, we could have an option on the USD-denominated S&P index *I (t)* where the exercise value is GBP *c*[*I (T )* − *K*] <sup>+</sup>. We can write the constant as *c* = *c*1*c*<sup>2</sup> where *c*<sup>1</sup> is the conventional dollar value of an index point, while *c*<sup>2</sup> is an exchange rate (the number of pounds per dollar). Thus a quanto option is a combination of a "foreign"-denominated option plus an exchange-rate guarantee. Valuation amounts to deriving the state-price density applicable to a market model including foreign as well as domestic assets.

## *Russian*

A Russian option is a perpetual lookback option, that is, an American lookback option with no final maturity time.

# **References**

- [1] Hull, J.C. (2000). *Options, Futures and Other Derivatives*, 4th Edition, Prentice Hall.
- [2] Margrabe, W. (1978). The value of an option to exchange one asset for another, *Journal of Finance* **33**, 177–186.

MARK H.A. DAVIS
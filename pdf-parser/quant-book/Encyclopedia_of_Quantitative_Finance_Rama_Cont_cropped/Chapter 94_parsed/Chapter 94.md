# **Foreign Exchange Options**

# **Market Overview**

The importance of foreign exchange (FX) options for risk management and directional trades is gaining more and more recognition from companies and investors. Various banks have been adapting their products to this situation during the past years. Different risk and profit profiles can be generated with plain vanilla or exotic options as individual products, as well as in combination with various products such as structured products. Financial engineers call this as *playing with Lego bricks*. Linear combinations of basic products are used to build structured products. To price plain vanilla or exotic options and show their risk, many professional trading systems have been introduced and are being continuously developed. With these systems, the traders are able to evaluate the positions in the individual currency pair or in currency portfolios at any time. In the FX options market, options trading systems such as *Fenics, Murex,* or *SuperDerivates* are used. Owing to the very rapid development in this sector, some banks started developing and using systems of their own.

To comply with various customer requests, a successful trading desk in the interbank market is essential. This is mostly plain volatility trade. The market risk of a short-term FX options trading desk consists of changes in spot, volatility, and interest rates. Since spot risk is easily eliminated by **delta hedging** and the effect of rates is small compared to the risk of changing volatility in the short term up to two years, managing volatility risk is the main task of the trader. Since the relationship of volatility and price of call or put options is monotone, it is equivalent to quote the price of an option either by the price itself or by the volatility implied by the **Black–Scholes formula**. The established market standard is quoting this implied volatility, which is why it is often viewed as a traded quantity. In the case of plain vanilla options, a **vega** long position is given when buying (call or put); conversely, a vega short position is given when selling. Volatility difference between call and put with same expiry and same deltas is called a *risk reversal*. If the risk reversal is positive, the market is willing to pay more for calls than for puts; if the risk reversal is negative, the market favors put options. The butterfly measures the convexity of the "smile" of the volatility, that is, the volatility for the out-of-the-money and the inthe-money-options (*see* **Foreign Exchange Markets** for details).

If the **delta hedge** is done with an interbank partner at the same time the option is traded, the trader can focus on the vega position in his book. The **delta hedge** neutralizes the change of the option price caused by changes of the underlying. For longterm options with an expiry longer than two years or options with high interest rate sensitivity, the **delta hedge** should be replaced by a forward hedge, as the risk of interest rate sensitivity is mostly higher than the volatility risk in this case. This means that instead of neutralizing spot risk by trading in the spot market, one would trade a forward contract with maturities matching those of the cash flows of the option. This would simultaneously take care of the spot and the rate risk.

# **First-generation Exotic Options**

First-generation exotic options are all options beyond plain vanilla options that started trading in the 1990s, in particular, barrier options, digital and touch products, average rate or Asian options, and lookback and compound options. There is no strict separation between first- and second-generation exotics as the viewpoint on what is first and second varies by the person in charge. Exotic options are traded live in currency trading as opposed to plain vanilla options, which mostly trade through automated systems. Trading exotic options is done by quoting the bid and ask price of the product rather than the corresponding volatility, because the monotone relationship of volatility and price is often not guaranteed. When asking for a quote, the spot reference level is agreed upon at which the option is calculated and priced. This allows comparing quotes of the exotic options and is also the basis of the **delta hedge**. To keep the **vega** risk low when fixing a deal, a vega hedge can be done with the partner. In this case, plain vanilla options (calls/puts, at-the-money ATM straddles) are traded to offset the vega of the exotic option. The default vega hedge is done with a straddle—an outof-the-money call and an out-of-the-money put—the reason being that this product does not have any delta, so one offsets the vega position without touching

![](_page_1_Figure_1.jpeg)

**Figure 1** (a) Payoff profile of a EUR-USD knockout option that is not knocked out during its lifetime; (b) payoff profile of the EUR-USD risk reversal at expiry

the delta position. Normally, during the lifetime of the option, the risk is hedged dynamically across the entire option book.

The quoting bank (market maker) is the calculation agent. It stipulates the regulations under which predefined triggers are reached or how often the underlying is traded in certain predefined ranges. The market maker informs the market user about the trigger event.

#### *Barrier Options*

Barrier options are vanilla put and call options with additional barriers. In case of a knockout, the option expires worthless, if the spot ever trades at or beyond the prespecified barrier. In case of a knockin option, the option is only activated if the spot ever trades at or beyond the prespecified barrier. The barrier is valid at all times between inception of the trade and the maturity time of the option.

One can further distinguish regular barrier options, where the barrier is out-of-the-money, and reversebarrier options, where the barrier is in-the-money.

A regular knockout barrier option can basically be priced and semistatically hedged by a risk reversal (Lego-brick principle).

Figure 1 illustrates the example: EUR-USD Spot 1.4600 expiry six months, strike 1.5000, EUR CALL with regular knockout trigger at 1.4300.

Hedging a short regular knockout EUR call, we can go long a vanilla EUR call with the same strike and the same expiry and go short a vanilla EUR put with a strike such that the value of the hedge portfolio is zero if the spot is at the barrier. The long call and short put is called a *risk reversal* and its market price can be used as a proxy for the price of the regular knockout call. In our example, it would be a 1.3650 EUR put. If the trigger is not reached, then the put expires worthless and the call offsets the knockout call payoff. If the trigger is reached, the risk reversal can be canceled with approximately zero value. The delta of a knockout option is higher than the delta of the corresponding plain vanilla option, and the higher it is, the closer the trigger is to the underlying spot.

Reverse knockout and reverse knockin are more difficult to price and hedge as the risk profile of these options is difficult to replicate with other options. In this case, the trigger is in the money. The volatility risk of first and second order arising from these options can be hedged dynamically with risk reversals and butterflies (*see* **Vanna–Volga Pricing**). However, all sensitivities take extreme values when getting closer to the trigger and closer to maturity. Delta positions can be a multiple of the notional amount. Therefore, it is difficult for the trader to perform dynamic hedging strategies. To manage these risks, short-term reverse knockout barrier options are often removed from the global books and are matched as individual positions, or are closed two to three weeks before expiry. The risk surcharge paid in this case is often smaller than the cost of keeping to such positions and hedging them individually.

#### *Modifications and Extensions of Barrier Options*

Standard extensions of barrier options are *doublebarrier options*, where there is a barrier above and below the current spot. A double knockout option expires worthless if any of the two barriers are ever touched or crossed. A double knockin option only becomes a vanilla option if at least one of the two barriers is touched or crossed in the underlying.

A further modification of barrier options is called the *knockin/knockout* (*KIKO*) option. This option can knockout at any time; however, it must knockin to become alive. A short KIKO option can be statically hedged with a long knockout option and a short double knockout option, if the spot value is between the triggers, and with a long knockout option and a short knockout option, if the spot value is above both triggers (Lego-brick principle).

*Window barriers* (*partial barriers*) are additional modifications of barrier options. In case of a windowbarrier option, the trigger is valid only within a certain period of time. Commonly, this period of time is from inception of the trade until a specific date (*early ending*) or from a specific date during validity until expiry date of the option (*deferred start*). Arbitrary time intervals are possible.

For *European barrier options*, the triggers are only valid at maturity. They can be statically hedged with plain vanilla options and European digital options (Lego-brick principle).

#### *Binary Options/Digital Options*

Digital or binary options pay a fixed amount in a currency to be specified if the spot trades at or beyond a prespecified barrier or trigger. For European digitals, the trigger is valid only at maturity, whereas for American digitals, the trigger is valid during the entire lifetime of the trade. In FX-interbank trade American digitals are also called *one-touch* (if the fixed amount is paid at maturity) or *instant onetouch* (if the fixed amount is paid at first hitting time) options. Further touch options are the so-called *notouch* options, *double no-touch* options, and *double one-touch* options. A no-touch pays only if the spot never touches or crosses the prespecified trigger. A double no-touch pays only if neither the upper trigger nor the lower trigger is ever touched or crossed during the lifetime of the contract. A double one-touch pays only if at least one of the upper or the lower triggers is touched. When buying a double no-touch option, a vega short position is generated. This means that double no-touch options are cheap in phases of high volatility.

European digital options can be replicated with bull or bear spreads with large amounts. Their market price can thus be approximated by liquid vanilla options. However, this type of option is difficult to hedge as the delta hedge close to expiry is zero almost everywhere.

# **General Features When Pricing Exotic Options**

Most commercial software packages calculate the "theoretical value (TV)" of the exotic options, which is the value of the product in a **Black–Scholes model** with constant parameters.

Knowing the TV is important for trading partners as it serves as a checksum to ensure that both parties talk about the same product. The market value, however, often deviates from this value because of so-called overhedge costs, which arise when hedging the exotic option. Every trader must be aware of the risk arising from these options and should be able to control this risk dynamically in his books via the Greeks (price sensitivity with respect to market and model parameters). If a gain is generated by performing this hedge, the price of an exotic option must be higher than the TV. Conversely, if the hedge leads to a loss, the market price of the exotic option should be above TV.

A very important issue when trading exotic options is placing automatic spot orders at spot levels that could lead to a knockout or expiry of the option. This order eliminates the **delta hedge** of the option automatically when reaching the trigger. This explains the occasional very heavy spot movements during specific trigger events in the market.

The following vega structure is often found in options books as it stems from most of the **structured products** offered today in the FX range: ATM vega long and wing vega short. This is the reason for a long phase of low volatility and high butterflies for the past years. See also **Foreign Exchange Smiles**.

# **Second-generation Exotic Options**

We consider every exotic option as second generation if it is not a vanilla and not a first-generation product.

Some of the common examples in FX markets are *range accruals* and *faders*.

A range accrual is a sum of digital call spreads and pays an amount of a prespecified currency that depends on the number of currency fixings that come to fall inside a prespecified range. A fader is any basic option product like a vanilla or barrier option, whose notional amount depends on the number of currency fixings that come to fall inside a prespecified range. We distinguish fade-in products, where the notional grows with each fixing inside the range and fadeout products, where the notional decreases with each fixing inside the range.

Further extensions are target redemption products, whose notional amount increases until a certain gain is reached. A common example is a **target redemption forward** (TRF). We provide a description and an example here: We consider a TRF in which a counterpart sells EUR and buys USD at a much higher rate than current spot or forward rates. The key feature in this product is that counterpart has a total target profit that, once hit, knocks out all future settlements (in the example below, all weekly settlements), locking the gains registered until then.

The idea is to place the strike over 5.5 big figures above spot to allow the counterpart to quickly accumulate profits and have the trade knocked out after five or six weeks. The counterpart will start losing money if EUR-USD starts fixing above the strike. On a spot reference of 1.4760, consider a one year TRF, in which the counterpart sells 1 EUR 1 million per week at 1.5335, subject to a knockout condition: if the sum of the counterpart profits reaches the target, all future settlements are canceled. We let the target be 0.30 (i.e., 30 big figures), measured weekly as Profit = Max (0, 1.5335—EUR-USD Spot Fixing). As usual, this type of forward is also traded at zero cost:

Week 1 Fixing = 1*.*4800 Profit = 0*.*0535 Max (1.5335–1.4800, 0) Week 2 Fixing = 1*.*4750 Profit = 0*.*0585 Accumu-

lated profit = 0*.*1120 Week 3 Fixing = 1*.*4825 Profit = 0*.*0510 Accumu-

lated profit = 0*.*1630

Week 4 Fixing = 1*.*4900 Profit = 0*.*0435 Accumulated profit = 0*.*2065

Week 5 Fixing = 1*.*4775 Profit = 0*.*0560 Accumulated profit = 0*.*2625

Week 6 Fixing = 1*.*4850 Profit = 0*.*0485 Accumulated profit = 0*.*3110

The profit is capped at 0.30, so the counterpart only accumulates the last 3.75 big figures and the trade knocks out.

Each forward will be settled physically every week until trade knocks out (if the target is reached).

Another popular FX product is the *time option*, which is essentially a forward contract of American style, that is, the buyer is entitled and obliged to trade a prespecified amount at a prespecified strike, but can choose the time within a prespecified time interval.

The market is likely to continue to develop fast. Besides *Bermudan style options*, where early exercise is allowed at certain prespecified times, **basket options** and the corresponding structures are very much in demand in the market. Hybrid structures are exotic options whose payoff depends on underlying spots across different market sectors. We refer the reader to [1].

# **References**

[1] Wystup, U. (2006). *FX Options and Structured Products*, John Wiley & Sons.

> MARKUS CEKAN, ARMIN WENDEL & UWE WYSTUP
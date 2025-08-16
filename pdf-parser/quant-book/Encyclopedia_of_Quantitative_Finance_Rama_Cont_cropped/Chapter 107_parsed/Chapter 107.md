# **Barrier Options**

Barrier options are vanilla options with path-dependent payoffs, that is, the payoff is not only a function of stock level relative to option strike but also dependent upon whether or not the stock reaches certain prespecified barrier level before maturity. An example will illustrate the idea. Suppose an investor is long an up-and-in at-the-money call option on the S&P 500 index with barrier level at 110% of the initial S&P 500 index level. Before maturity, if the index never reaches 110% of the initial index level, the option never gets knocked in. The investor receives nothing at maturity. However, if the index level reaches 110% at some point before maturity, the investor receives a payoff identical to a vanilla at-themoney call option at maturity. In the latter scenario, the option is "knocked in" on the day when the index reaches 110% level.

There are many types of barrier options. We discuss two common ones, that is, knock-out and knockin barrier options. For knock-out barrier options, the option will be knocked out and become worthless if the underlying asset crosses a prespecified barrier level. For knock-in barrier options, the barrier option will be knocked in and become a vanilla option only if the underlying asset crosses the prespecified level before maturity. The example used earlier is a knockin barrier option.

Depending upon the barrier level relative to the initial underlying asset level, we can have an "up" barrier or a "down" barrier. If the barrier is above the initial underlying asset level, it is called an *up barrier*. If the barrier is below the initial underlying asset level, it is called a *down barrier*. Together, we can have four different variations of barrier options, that is, up-and-in, up-and-out, down-and-in, and downand-out options. Table 1 shows these four variations schematically.

# **Basic Features**

# *Up-and-in Call/Up-and-in Put*

This is the first kind of knock-in barrier options. The up-and-in barrier option has a knock-in barrier level, which is higher than the initial underlying asset level. Before maturity, if the underlying asset goes above the barrier level, the barrier option will be knocked in and become a vanilla option. Otherwise, the barrier option will expire worthless at maturity. Up-and-in calls are more common. This is because, when the underlying asset increases to knock-in barrier level, it would most likely stay above the initial underlying asset level. Therefore, call options will be more likely be in the money at maturity than put options. Bullish investors can buy up-and-in call options and pay a lower premium than that on the vanilla call options. This makes the on up-and-in calls more leveraged than vanilla calls.

# *Down-and-in Call/Down-and-in Put*

The down-and-in barrier option has a knock-in barrier level, which is below the initial underlying asset level. Before the maturity, if the underlying asset goes below the barrier level the barrier option will be knocked in and become a vanilla option. Otherwise, the barrier option will expire worthless at maturity. Down-and-in puts are more common in this case. Bearish investors can buy down-and-in puts and pay a lower premium than that on the vanilla put options.

# *Up-and-out Call/Up-and-out Put*

This is the first kind of knock-out barrier options. The up-and-out barrier option has a knock-out barrier level above the initial underlying asset level. Before maturity, if the underlying asset crosses the barrier level, the option will be knocked out and become worthless. Otherwise, the barrier option will just be a vanilla option. A bearish investor would buy up-andout puts to achieve more leverage by paying a lower premium than that on vanilla puts.

# *Down-and-out Call/Down-and-out Put*

The down-and-out barrier option has a knock-out barrier level below the initial underlying asset level. Before maturity, if the underlying asset goes below the barrier level, the option will be knocked out and become worthless. A bullish investor would buy down-and-out calls to achieve more leverage by paying a lower premium than that on vanilla calls.

# **Some Variations**

With increased popularity of barrier options and growth of its market, some other features are being

|              | Knock in         | Knock out         |
|--------------|------------------|-------------------|
| Up barrier   | Up-and-in call   | Up-and-out call   |
|              | Up-and-in put    | Up-and-out put    |
| Down barrier | Down-and-in call | Down-and-out call |
|              | Down-and-in put  | Down-and-out put  |
|              |                  |                   |

**Table 1** Common barrier types

introduced to better meet investors' needs. In the following, we discuss briefly some of the most popular variations to basic knock-in/knock-out barrier options.

# *Rebates*

It is fairly common that a knock-out barrier option pays a rebate on a knock-out event to compensate the investor for the loss of the option. The rebate is typically a small amount and paid either immediately or deferred to the maturity. For knock-in barrier options, a rebate will be paid out at maturity if the barrier is never knocked in.

# *Double Barrier*

A double barrier option is another variation that has two barriers, typically one up barrier and the other a down barrier. For example, investors seeking high leverage would consider double knock-out barrier options if they believe changes in the underlying asset level would be within a narrow range. The double knock-out barrier option would become worthless if the underlying asset drops below the down barrier or rises above the up barrier before maturity. Because of that, the double knock-out barrier option costs less than the single knock-out barrier option and thus provides more leverage.

Another popular variation of double barrier is the knock-in option with a knock-out barrier. The knockin barrier option can be knocked out either before or after the option is knocked in. If the option can be knocked out even before the option is knocked in, this is called *knock-out dominant barrier option*. Again, this type of double barrier options provides more leverage than a single barrier option because it costs less than the single knock-in barrier option.

# *Discrete Barrier*

The barrier specification varies from contract to contract. Many barrier options have the so-called continuous barrier or intraday barrier. This means that the barrier event can be triggered any time during intraday trading hours. However, some barrier options only allow the barrier event to be triggered by the end-of-day closing price. This is called *discrete barrier*. More generally, a discrete barrier is defined as any barrier type other than the continuous barrier.

# *American Style Exercise*

Although it is not very common, there are a few types of barrier options that have American exercise feature. One example would be a six-month at-themoney call option with installment premium, that is, the premium would be paid monthly instead of a lump sum upfront. The knock-out barrier is at 90% of the initial underlying asset level. The option will be knocked out if the underlying asset drops below the knock-out barrier level before maturity. In addition, the option would be terminated automatically if the investor stops paying the installment premium on monthly reset dates. This installment feature provides more flexible financing for investors because they pay the premium over a period of time instead of paying the lump sum up front. It also allows investors to re-evaluate the market condition and decide if it is optimal to continue the knock-out option or terminate it.

# **Valuation of Barrier Options**

Barrier options are less expensive than vanilla options because of the possibility that the barrier option would be knocked out or knocked in. There are many publications on how to price barrier options (see [2, 7] for a good summary). In general, the valuation of barrier options needs to take into account stock-level dependency of volatility dynamics, that is, local volatility surface. This requires using numerical methods like partial differential equations (*see* **Finite Difference Methods for Barrier Options**) or Monte Carlo simulation. In certain situations, the barrier options can be priced by using the static replication method (see [3, 4]).

# *In–Out Parity*

Similar to put–call parity for the vanilla options, there is an interesting relationship between knockin and knock-out barrier option. Using call options as example, an up-and-out call is complimentary to an up-and-in call if both have the same strike and barrier level. A portfolio of one up-and-in call and one up-and-out call will have the same payoff at maturity as a vanilla call option. The reason is simple. If the underlying asset stays below the barrier level before maturity, the up-and-in call will become worthless and the up-and-out call will become a vanilla call. On the other hand, if the underlying asset rises above the barrier level, the up-and-out call will become worthless and the up-and-in call will become a vanilla call. Therefore, for any given scenario of the underlying asset path before maturity, the portfolio will always have the same payoff as a vanilla call. The sum of an up-and-in call and an up-and-out call is the same as a vanilla call. This is so-called in–out parity for barrier options and applies to both the put and call options in the absence of rebates.

# *Constant Volatility*

In the limit of constant volatility, Merton [5] provided the first analytical formula for a down-and-out call option. Later on, Reiner and Rubinstein [6] extended the formula for all eight combinations of barriers (*see* **Pricing Formulae for Foreign Exchange Options**).

# *Adjustment for Discrete Barrier*

Often, the barrier option has a discrete barrier schedule but the exact valuation is only available for the case of continuous barrier. In the constant volatility case, Broadie *et al.* [1] proposed that, by adjusting the barrier level in the continuous barrier option valuation, one would obtain a good approximation of the discrete barrier option value. The adjustment to the barrier level is prescribed by the following formula:

$$X_{\text{adj}} = X e^{\alpha \sigma} \sqrt{T/m} \tag{1}$$

where *α* is 0.5826 for an "up" barrier and −0.5826 for a "down" barrier, *m* is the number of discrete samples of the underlying asset price over the term *T* of the barrier option, and *σ* is the constant volatility.

# **References**

- [1] Broadie, M., Glasserman, P. & Kou, S.G. (1997). A continuity correction for discrete barrier options, *Journal of Mathematical Finance* **7**, 325–349.
- [2] Briys, E., Bellalah, M., Mai, H.M. & de Varenne, F. (1998). *Options, Futures and Exotic Derivatives—Theory, Application and Practice*, Wiley Frontiers in Finance.
- [3] Carr, P. & Chou, A. (1997). Breaking barriers, *Risk Magazine* **10**, 139–144.
- [4] Derman, E., Ergener, D. & Kani, I. (1997). Static options replication, in *Frontiers in Derivatives*, Irwin Professional Publishing.
- [5] Merton, R. (1971). Theory of rational option pricing, *Bell Journal of Economics and Management* **4**, 141–183.
- [6] Reiner, E. & Rubinstein, M. (1991). Breaking down barriers, *Risk Magazine* **4**, 28–35.
- [7] Wilmott, P. (1998). *Derivatives—The Theory and Practice of Financial Engineering*, John Wiley & Sons.

# **Related Articles**

**Finite Difference Methods for Barrier Options**; **Pricing Formulae for Foreign Exchange Options**.

MICHAEL QIAN
# **Volatility Index Options**

Volatility index options are options on a volatility index. Volatility index options enable one to take a pure volatility exposure without the need to take positions in the index itself and without the need to delta-hedge. These features make these options very interesting for pure volatility trades and bets. They also allow one to trade the spread between realized and implied volatility, or to hedge the volatility exposure of other positions or businesses, without being contaminated by the index price dependence like in the standard index options. This explains their popularity among traders and hedge funds.

Originally, volatility index options were traded over the counter (OTC), and a large part is still traded OTC, through volatility and variance swaps (*see* **Variance Swap**). In February 2006, the Chicago board option exchange (CBOE) realized the interest in the financial community for exchanged standardized volatility index options and started offering standardized options first on the VIX (which is the CBOE volatility index) and later on the Russel 2000 volatility index. In Europe, although the major exchanges have already developed volatility on the major indexes (and futures on these) like the VDAX, FTSE 100 volatility index, VSTOXX, VCAC, or VSMI, they still do not offer any options on these indexes.

## **Volatility Index**

The underlying volatility index is computed from option prices to capture information from the options market by some means. The overall idea of index volatility is to provide a good estimate of the socalled implied volatility extracted from the options market, as opposed to the historical volatility. More precisely, the aim is to estimate the risk-neutral market's expectation of the future volatility. In the specific case of the VIX, the formula is public and weights the various options as follows:

$$\sigma^2 = \sum_i \frac{2\Delta K_i}{T_i K_i^2} e^{RT} Q(K_i) - \frac{1}{T_i} \left(\frac{F}{K_0} - 1\right)^2 \quad (1)$$

where *σ* is the *VIX/*100, or equivalently, *VIX* = 100*σ*, *Ti* the time to expiration of the *i*th option, *F*

the forward index level derived from option prices, *K*<sup>0</sup> the highest strike just below the forward index level, *F*, *Ki* the strike price of the *i*th option: a call if *Ki > K*0, a put if *Ki < K*<sup>0</sup> and both call and put for *Ki* = *K*0, *-Ki* the interval between strike prices, *R* the risk-free rate to expiration, and *Q(Ki)* the midpoint of the bid–ask spread for each options with strike *Ki*.

The CBOE calculates and publishes minute-tominute the VIX using real-time bid–ask market quotes of options on S & P500 index (SPX) with nearby and second nearby maturities and applying the multiplier of \$100. Overall, the VIX reflects market's view of the future short term volatility. A high value of the index indicates a more volatile market, while a low value indicates a less volatile environment. Often referred to as the *fear index*, it represents one measure of the market's expectation of volatility over the next 30-day period. In short term, bias can explain some key differences between the VIX and the overall market sentiment. This is particularly true at times when the most liquid options are in the range of 2–6 months to expiration. Therefore, VIX tries to quantify the market volatility, mainly focusing on short term, being unable to completely explain the market volatility, which is a complex concept.

It is worth noting that VIX is computed to be the square root of the par variance swap rate (*see* **Variance Swap**), and not the volatility swap rate (*see* **Volatility Swaps**). This is because variance swap can be perfectly, statically replicated through vanilla puts and calls, whereas volatility swap requires dynamic hedging [1]. We will discuss this point later in the section on pricing.

VIX options are European call and put options on the VIX index, with strikes ranging from 10 to 65 (with interval of 1 and 2.5 points for liquid and 5 points for less liquid points), while maturities are up to 6 months. Like many other listed options, VIX options are quoted with a multiplier of \$100. The expiration date is roughly speaking the third Wednesday of the expiry month. More details can be found on the CBOE website [3].

# **Pricing Models**

In terms of pricing, roughly speaking there are two methods to price index volatility options:

- a model-dependent approach that assumes a model for the index volatility diffusion and provides a closed-form formula of call and put options;
- a model-free approach that computes the cost of the static hedge to replicate the volatility index option.

Historically, the model-dependent approach has been the first to emerge. Successively, among others, Whaley [11], Grunbichler and Longstaff [6], Howison *et al.* [7], and Elliott *et al.* [5], and lately Sepp [9, 10], presented the model-dependent approaches to price volatility index options. They all assume an underlying stochastic process for the index volatility (or the index volatility futures) and explicitly compute the price of the call and put options.

The first model-dependent approach presented by Whaley [11] assumed a log normal diffusion for the VIX cash index and the VIX futures leading to a standard Black–Scholes formula for the VIX call options as follows:

$$C(T, F, K) = D_T \left[ FN(d_+) - KN(d_-) \right] \quad (2)$$

$$d_{\pm} = \frac{\ln\frac{F}{K} \pm \frac{1}{2}T\sigma^2}{\sqrt{T}\sigma} \tag{3}$$

where *C(T , F , K)* stands for the value of the call option with expiry time *T* , strike *K*, and forward price *F*, and where *σ* is the volatility of the futures price, *DT* is the discount factor expiring at time *T* , and *N (x)* is the cumulative normal distribution up to *x*. A straightforward drawback of the Whaley approach was the strong log normal underlying assumption. This motivated further research and led to many works. Grunbichler and Longstaff [6] proposed a mean-reverting square root process for the volatility process. Following the popularity of stochastic volatility, Howison [7] and Elliot [5] suggested to use stochastic volatility model for the index volatility to capture the risk of volatility for the index volatility. Moreover, because it is well known that index volatility is upward sloping, the stochastic volatility approach, which can cope with this important feature, was an appealing modeling choice. Figure 1, for instance, gives the VIX smile for 27 July 2009.

Lately, Sepp [9, 10] argued in favor of adding jumps to the stochastic volatility model to get a more realistic diffusion for the index volatility. This was supported by the econometric works that confirmed the evidence of jumps for the volatility index.

To sum up, the model-dependent approach aims at modeling the index volatility evolution as accurately as possible and providing a very consistent framework for pricing any type of option on index volatility. The strength is the flexibility in terms of pricing as there is no limitation for the types of options. The

![](_page_1_Figure_11.jpeg)

**Figure 1** VIX Smile

weakness is the strong assumption of a specific model and distribution for the index volatility.

Another approach initiated by Neuberger [8], Demeter *et al.* [4], Carr and Lee [1], and Carr and Wu [2] is to exhibit a static hedge and compute in a model free way the price of this hedge using call and put options on the index itself. In a very insightful paper, Demeter *et al.* [4] showed that a static portfolio of call and puts options on the volatility index can replicate a variance swap. Lately, Carr and Lee [1] and Carr and Wu [2] extended the closed form formula to the case of both the variance and the volatility swap. The starting point is to assume a pure diffusion given as follows:

$$dS_t = \mu_t S_t dt + \sigma(t, \ldots) S_t dW_t \tag{4}$$

where *µ* is the drift term and *σ (t, . . .)* is a very general volatility function (that can be assumed to be a local volatility for the clarity of the explanation). A trivial application of the Ito lemma on log ˆ *(St)* provides the main intuition and leads to the fact that one can relate the volatility to a log contract as follows:

$$\frac{\mathrm{d}S_t}{S_t} - \mathrm{d}\log(S_t) = \frac{1}{2}\sigma^2(t,\ldots)\,\mathrm{d}t\tag{5}$$

Like any function of the underlying asset, the log contract can be replicated by a series of call and put options. This leads, in particular, to the Par swap rate of a variance swap as follows (referred in the literature as the replication variance swap price):

$$K_{\text{Var}} = \frac{2}{T} \left[ rT - \left( \frac{S_0}{S_*} e^{rT} - 1 \right) - \log \left( \frac{S_*}{S_0} \right) \right. \\ + e^{rT} \int_0^{S_*} \frac{1}{K^2} P(K) \, \mathrm{d}K \\ + e^{rT} \int_{S_*}^{S_*} + \infty \frac{1}{K^2} C(K) \, \mathrm{d}K \right] \tag{6}$$

where *P (K)* and *C(K)*, respectively, denote the current fair value of a put and call option of strike *K*, *r* is the risk free rate, *T* is the maturity of the variance swap, *S*<sup>0</sup> is the initial spot value of the underlying asset, and *S*<sup>∗</sup> is an arbitrary point to do the split between the liquid call and put options. It is often chosen to be the forward value.

Unlike the previous model-dependent approaches, the model-free approach replicates the variance and the volatility swaps using market prices of volatility options as inputs. The resulting pricing consists in numerically computing the cost of the hedging strategy with the series of options as shown by the integrals of equation (6).

The obvious strength of this approach is to avoid any assumption on the underlying distribution of the index volatility. Primarily, the weaknesses are that the replication methods do not work for very specific index volatility options and that the discretization bias due to the lack of reliable liquid quotes for call and put options at any strikes can be of the same order of the magnitude as the misspecification of the index volatility distribution.

## **References**

- [1] Carr, P. & Lee, R. (2007). Realized volatility and variance: Options via swaps, *Risk* May, 76–83.
- [2] Carr, P. & Wu, L. (2009). Variance risk premiums, *Review of Financial Studies* **22**, 1311–1341.
- [3] CBOE (2009). *Vix Options CBOE*. www.cboe.com.
- [4] Demeterfi, K., Derman, E., Kamal, M. & Zou, J. (1999). *More than You Ever wanted to know about Volatility Swaps*, Goldman Sachs Quantitative Strategies, March 1999.
- [5] Elliott, R., Siu, T. & Chan, L. (2004). Pricing volatility swaps under heston's stochastic volatility model with regime switching, *Applied Mathematical Finance* **14**(1), 41–62.
- [6] Grunbichler, A. & Longstaff, F. (1996). Valuing futures and options on volatility, *Journal of Banking and Finance* **20**, 985–1001.
- [7] Howison, S., Rafailidis, A. & Rasmussen, H. (2004). On the pricing and hedging of volatility derivatives, *Applied Mathematical Finance* **11**(4), 317–346.
- [8] Neuberger, A. (1994). The log contract: a new instrument to hedge volatility, *Journal of Portfolio Management* **20**(2), 74–80.
- [9] Sepp, A. (2008). Pricing options on realized variance in the heston model with jumps in returns and volatility, *Journal of Computational Finance* **11**(4), 33–70.
- [10] Sepp, A. (2008). Vix option pricing in a jump-diffusion model, *Risk* April, 84–89.
- [11] Whaley, R. (1993). Derivatives on market volatility: hedging tools long overdue, *Journal of Derivatives* **1**, 71–84.

## **Further Reading**

Bergomi, L. (2008). Dynamic properties of smile models, in R. Cont ed. *Frontiers in Quantitative Finance: Volatility and Credit Risk Modeling*, Wiley, Chapter 3.

Cont, R. and Kokholm, T. (2009). *A Consistent Pricing Model for Index Options and Volatility Derivatives*. Available at SSRN: http://ssrn.com/abstract = 1474691.

## **Related Articles**

**Call Options**; **Corridor Variance Swap**; **Gamma Swap**; **Heston Model**; **Implied Volatility Surface**; **Realized Volatility and Multipower Variation**; **Realized Volatility Options**; **Stochastic Volatility Models**; **Variance Swap**; **Weighted Variance Swap**.

ERIC BENHAMOU & MARIAN CIUCA
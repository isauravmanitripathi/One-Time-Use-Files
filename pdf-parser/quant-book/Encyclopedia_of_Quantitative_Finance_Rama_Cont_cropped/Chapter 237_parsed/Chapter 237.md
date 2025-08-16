# **Inflation Derivatives**

The market for financial inflation products started with public sector bonds linked to some measure for inflation of prices of (mainly) goods and services. This dates back to as early as the first half of the eighteenth century when the state of Massachusetts issued bonds linked to the price of silver on the London Exchange [4]. Over time, and particularly, in the last 20 years or so, the dominant index used for inflation-linked bonds has become the consumer price index (CPI). A notable exception is the UK inflationindexed gilt market, which is linked to the retail price index (RPI).<sup>a</sup> The actual cash-flow structure of inflation-indexed bonds varies from issue to issue, including capital-indexed bonds (CIBs), interestindexed bonds, current pay bonds, indexed annuity bonds, indexed zero-coupon bonds, and others. By far the most common cash-flow structure is the CIB, on which we shall focus in the remainder of this article.

# **Bonds, Asset Swaps, and the Breakeven** Curve

Inflation-indexed bonds (of CIB type) are defined by

- $\bullet$  N—a notional;
- $\bullet$  *I*—the inflation index;
- $L$ —a lag (often three months);
- $T_i: \{1 \le i \le n\}$ —coupon dates;
- $c_i: \{1 \le i \le n\}$ —coupon at date  $T_i$  (usually, all  $c_i$  are equal); and
- $I(T_0 L)$ —the bond's base index value.

The bond pays the regular coupon payments

$$Nc_i \frac{I(T_i - L)}{I(T_0 - L)} \tag{1}$$

plus the inflation-adjusted final redemption, which often contains a capital guarantee according to

$$N \max\left(\frac{I(T_n - L)}{I(T_0 - L)}, 1\right) \tag{2}$$

Asset swap packages swapping the inflation bond for a floating leg are liquid in some markets such as for bonds linked to the CPTFEMU (also known as the  $HICP$ ) index. Since the present value of an inflationlinked bond can be decomposed into the value of each coupon

$$P_{T_i}(T_0) N c_i \frac{1}{I(T_0 - L)} \mathsf{E}_0^{\mathcal{M}(P_{T_i})} [I(T_i - L)] \tag{3}$$

wherein  $\mathsf{E}_{\tau}^{\mathcal{M}(X)}[\cdot]$  denotes expectation in filtration  $\mathcal{F}_{\tau}$  under the measure induced by choosing X as numéraire, and the value of the final redemption

$$P_{T_n}(T_0)N\frac{1}{I(T_0-L)} \times \mathsf{E}_0^{\mathcal{M}(P_{T_n})}[\max{(I(T_n-L), I(T_0-L))}] \tag{4}$$

these products give us a mechanism to calibrate the forward curve  $F(t, T)$ , where

$$F(t, T - L) :=$$
 The index forward for (payment)

time 
$$T$$
 seen at time  $t$   

$$:= \mathsf{E}_{t}^{\mathcal{M}(P_{T})}[I(T-L)] \tag{5}$$

The forward curve is often also referred to as the breakeven curve. The realized inflation index fixing level is thus naturally  $I(T) = F(T, T)$ . Note that while equation (4), strictly speaking, requires a stochastic model for consistent evaluation due to the convexity of the  $max(\cdot, 1)$  function, in practice, the  $\max(\cdot, 1)$  part is usually ignored, since its influence on valuation is below the level of price resolution.<sup> $b$ </sup>

If there were a multitude of inflation-linked bonds, or associated asset swaps, with well-dispersed coupon dates liquidly available for any given inflation index, then the above argument would be all that is needed for the construction of a forward index curve, that is, breakeven inflation curve. In reality, though, for many inflation markets, there is only a small number of reasonably liquid bonds or asset swaps available. This makes it necessary to use interpolation techniques for forward inflation levels or rates between the attainable index-linked bond's maturity dates. In some cases, this may mean that for the construction of a 10-year (or longer) inflation curve, only three bonds are available, and extreme care must be taken for the choice of interpolation. However, even when a sufficiently large number of bonds is traded, to have a forward inflation rate for each year determined by the bond market, sophisticated interpolation methods are still needed. This is because of inflation's seasonal nature. For instance, consumer prices tend to go up significantly more than the annual average just before Christmas and tend to drop (or rise less than the annual average) just after.

The most common approach to incorporate seasonality into the breakeven curve is to analyze the statistical deviation of the month-on-month inflation

rate from the annual average with the aid of historical data, and to overlay a seasonality adjustment on top of an annual inflation average curve in a manner such that, by construction, the annual inflation index growth is preserved. In addition, some authors used to suggest that one may want to add a long-term attenuation function (such as  $e^{-\lambda t}$ ) for the magnitude of seasonality. This was supposed to represent the view that, since we have very little knowledge about long-term inflation seasonality, one may not wish to forecast any seasonality structure. This idea has gone out of fashion though, probably partly based on the realization that, historically, the seasonality of inflation became *more* pronounced over time, not exponentially *less*.

#### **Inflation Derivatives**

#### Daily Inflation Reference

Ultimately, all inflation fixings are based on the publication of a respective index level by a government or cross-government funded organization such as Eurostat for the HICP index series in Europe, or the Bureau of Labor Statistics for the CPI-U in the United States. This publication tends to be monthly, and usually on the same day of the month with a small amount of variability in the publication date. In most inflation bond markets, index-linked bonds are written on the publication of these published index levels in a straightforward manner such as  $I(T_i)/I(T_0)$ times a fixed number as discussed in the previous section, with  $T_i$  indicating that a certain month's publication level is to be used. For some inflation bonds, however, the inflation reference level is not a single month's published fixing, but instead, an average over the two nearest fixings. In this manner, the fact that a bond's coupon is possibly paid between two index publication dates, and thus should really benefit from a value between the two levels, can be catered for. French OAT*i* and OAT $\in$ *i* bonds, for instance, use this concept of the daily inflation reference (DIR) defined as follows:

$$\text{DIR}(T) = I\left(T_{m(T)-3}\right) + \frac{n_{\text{day}}(T) - 1}{n_{\text{days}}\left(m(T)\right)} \times \left[I\left(T_{m(T)-2}\right) - I\left(T_{m(T)-3}\right)\right] \quad (6)$$

with  $m(T)$  indicating the month in which the reference date  $T$  lies,  $T_i$  the publication date of month i,  $n_{\text{day}}(T)$  the number of the day of date T in its month, and  $n_{\text{days}}(m(T))$  the number of days in the month in which  $T$  lies. For example, the DIR applicable to June 21st is  $\frac{10}{30}$  times the HICP for March plus  $\frac{20}{30}$  times the HICP for April. While the DIR is in itself not an inflation derivative, it is a common building block for derivatives in any market that uses the DIR in any bond coupon definitions. The DIR clause complicates the use of any model that renders inflation index levels as lognormal or similar, since any payoff depending on the DIR thus depends on the weighted sum of two index fixings.

## Futures

Futures on the Eurozone HICP and the US CPI have been traded on the Chicago Mercantile Exchange since February 2004. Eurex launched Euro inflation futures based on the Eurozone HICP in January 2008. Both exchanges show, to date, very little actual trading activity in these contracts. An inflation futures contract settles at maturity at

$$M\left(1 - \frac{1}{\Omega}\left(\frac{I(T-L)}{I(T-L-\Omega)} - 1\right)\right) \tag{7}$$

with M being a contract size multiplier and  $\Omega$  an additional time offset. The lag  $L$  is usually one month. The offset  $\Omega$  is three months for CPI-U (also known as CPURNSA) on the CME, that is,  $\Omega = 1/4$  above. For the HICP (also known as *CPT*-*FEMU*) on both Eurex and CME,  $\Omega = 1$ , that is, one year. Exactly why the inflation trading community has paid little attention to these futures is not entirely clear, though, one explanation may be the difference in inflation linkage between bonds and futures. Both HICP-linked bonds and US Treasury-Inflation Protected Securities (TIPS) pay coupons on an inflation-adjusted notional, that is, they are CIBs. In contrast, both CPI and HICP futures pay period-on-period inflation rates. As a consequence, a futures-based inflation hedge of a single CIB coupon would require a whole sequence of futures positions and would leave the position still exposed to realized period-on-period covariance.

#### Zero-coupon Swaps

This simple inflation derivative is as straightforward as the simplest derivative in other asset classes: two counterparties promise to exchange cash at an agreed date in the future. One counterparty pays a previously fixed lump sum, and the other counterparty pays an amount that is given by the published fixing of an agreed official inflation index (times an agreed fixed number). In the world of equity derivatives, this would be called a *forward contract* on the index. Since inflation trading is, by nature and origin, leaning on fixed income markets, this contract is referred to as a *swap*, which is the fixed income market equivalent of a forward contract. Conventionally, swaps are defined by repeated exchange of fixed for floating coupons. Since the inflation index forward contract has no cashflows during the life of the contract, and only at maturity money is exchanged, in analogy to the concept of a *zero-coupon bond*, the inflation index forward contract is commonly known as the *inflation index-linked zero-coupon swap*, or just *zero-coupon swap*<sup>c</sup> for short. More precisely speaking, zero-coupon swaps have two legs. The two legs of the swap pay

inflation leg: 
$$N \frac{I(T-L)}{I(T_0-L)}$$
  
fixed leg:  $N(1+K)^{T-T_0}$  (8)

where *N* is the notional, *T*<sup>0</sup> is the start date of the swap, *T* the maturity, and *K* the quote. These swaps appear in the market comparatively liquidly as hedges for the inflation bond exposure to the final redemption payment—they act as a mirror. However, this should not mask the fact that the true source of the liquidity is the underlying asset swap/inflation bond.

#### *The Vanilla Option Market*

In the inflation option market, the most liquid instruments are as follows.

• **Zero-coupon caps and floors:**

At maturity *T* , they pay

$$\left[\phi\left(\frac{I(T-L)}{I(T-L-\Omega)} - (1+K)^{\tau}\right)\right]_{+} \qquad (9)$$

where is the index offset, *L* is the index lag, *K* the annualized strike, *τ* the year fraction between *(T* − *L* − *)* and *(T* − *L)*, and *φ* is +1 for a cap and −1 for a floor. For most of those options, the index in the denominator is actually known (i.e., = *T* ), and the option premium depends only on the volatility of the index *I (T* − *L)*.

#### • **Year-on-year caps and floors:**

The option is a string of year-on-year caplets or floorlets individually paying according to equation (9) with = *τ* = 1 at increasing dates spaced by one year. Apart from the front period, these caplets and/or floorlets thus depend on one index forward in their payoff's numerator, and on a second one in their payoff's denominator, whence some authors refer to these products being subject to *convexity*, though this is not to be confused with the usual concept of convexity induced by correlation with interest rates (there is more on this in the section Two Types of Convexity). An alternative view of a year-on-year caplet/floorlet's volatility dependence is to consider *volatility of the year-on-year ratio* as the fundamental driver of uncertainty. In this framework, no convexity considerations are required. The payoff of an inflation caplet/floorlet resembles the payoff of a vanilla option on the return of a money market account if one replaces inflation rates with interest rates.

#### *The Swap Market*

A close cousin of inflation caps and floors is the inflation swap. The swap consists of a series of shorttenored *forward starting zero-coupon swaps* each of which pays

$$\frac{I(T-L)}{I(T-L-\Omega)} - (1+K)^{\tau} \tag{10}$$

at the end of its respective period. Just like an interest rate swap can be seen as a string of *forward interest rate agreements*, an inflation swap can be seen as a string of *forward inflation rate agreements*. Unlike vanilla interest rate swaps, though, the period an inflation swap's individual forward inflation rate agreement is linked to does not have to be equal to the period the associated coupon is nominally associated with. An example for this is an asset swap on an Australian (inflation-linked) government bond whose coupons are typically paid quarterly and are "indexed to the average percentage change in the CPI over the two quarters ending in the quarter that is two quarters prior to that in which the next interest payment falls" [4]. In other words, is six months, *τ* = 1*/*2, and *L* is in the range of one to three months for quarterly coupons.

#### Total Return Inflation Swaps

These structures pay out a fixed sum linked to an inflation measure over time. With growing inflation concerns in mid-2008, these, together with inflation caps, became increasingly popular with private as well as institutional investors.

#### The Limited Price Index

A limited price index (LPI) is an instrument that is used in the market to provide a hedge to inflation, but with limited upside and/or downside exposure. When period-on-period inflation is within an agreed range, the LPI grows at the same rate as its underlying official publication index. When period-on-period inflation is outside this range, the LPI grows at the, respectively, capped or floored rate. Given an underlying inflation index  $I$ , the LPI  $\tilde{I}$  is constructed using I, a base date  $T_b$ , a fixing time tenor (i.e., frequency period)  $\tau$ , an inflation capping level  $l_{\text{max}} \in$  $(0, \infty]$ , and an inflation flooring level  $l_{\min} \in [0, \infty)$ . Using  $T_b$  and  $\tau$ , we create a publication sequence for  $\hat{I}$ :

$$I_{\text{publication sequence}} = \{T_b, T_b + \tau, T_b + 2\tau, T_b + 3\tau, \ldots\}$$

$$(11)$$

The LPI  $\tilde{I}$  can be defined recursively, starting with  $\tilde{I}(T_b) = 1$ , and continuing with

whence an exact static replication argument based on inflation caps and floors is not attainable. As a consequence, LPIs require a fully fledged (stochastic) model for relative value comparison with inflation bonds, zero-coupon swaps, and inflation caps and floors.

#### The Inflation Swaption

This product is in its optionality very similar to a conventional interest rate swaption. However, the underlying swap can have a variety of special features. The start date of the swap  $T_{\text{start}}$  is on or after the expiry of the option. The swap has one inflation-rate-linked leg, and one (nominal) interest-rate-linked leg. For instance, the underlying swap could be agreed to be given by the following.

- The inflation leg is a sum of  $n$  annual forward inflation rate agreements, paid at dates  $T_1$ ,  $T_2, \ldots, T_{n-1}, T_n$  with  $T_n$  representing the final maturity of the underlying swap. Each inflation leg coupon pays  $k^{\text{DIR}(T_i)}/_{I_{\text{Bess}}}$ , with DIR $(T_i)$ being the daily inflation reference for date  $T_i$ . The leg also pays a final notional redemption floored at 0, which can of course be seen as an enlarged coupon plus a zero-coupon floor struck at 0.
- The Libor leg is a sequence of quarterly forward (nominal) interest rate agreements. A variation

$$\tilde{I}(T_{b} + (i+1)\tau) = \tilde{I}(T_{b} + i\tau) \begin{cases}\n1 + l_{\min} & \text{if} \\
\frac{I(T_{b} + (i+1)\tau)}{I(T_{b} + i\tau)} \le 1 + l_{\min} \\
\frac{I(T_{b} + (i+1)\tau)}{I(T_{b} + i\tau)} & \text{if} \\
1 + l_{\max} \le \frac{I(T_{b} + (i+1)\tau)}{I(T_{b} + i\tau)} \le 1 + l_{\max} \\
1 + l_{\max} & \text{if} \\
1 + l_{\max} \le \frac{I(T_{b} + (i+1)\tau)}{I(T_{b} + i\tau)}\n\end{cases}\n$$
(12)

Given the definition of the LPI, derivatives such as zero-coupon swaps and options on the LPI can be built. LPI-linked products are most common in the UK market. A common comparison made by trading and structuring practitioners is to view an LPI, especially if it is only one sided, as very similar to an inflation cap or floor. It is worth noting that the two structures do have different sensitivities to inflation curve autocorrelation assumptions

of this is for the interest rate leg to pay Libor plus a fixed margin, or Libor minus a fixed margin floored at zero, which makes this leg alone already effectively a nominal interest rate cap.

There are many variations of inflation-linked swaptions, such as swaptions on the real rate (the real rate is explained further on), but most of them are only traded over-the-counter and in moderate size.

#### Inflation Modeling

For vanilla products such as inflation zero-coupon caps and floors, and year-on-year caplets and floorlets, practitioners tend to use terminologies and conventions relating to the Black and Bachelier models. For instance, to translate the price of an option that pays  $(I_T - K)_+$ , that is, simply at some point in the future the level of the index minus a previously agreed fixed number, or zero, whichever is greater, practitioners tend to use the concept of implied volatility for the index as if the index evolved in a Black-Scholes modeling framework. For options that pay a year-on-year rate, either Black implied lognormal volatilities or, alternatively, Bachelier, that is, absolute normal volatilities may be used. The latter are also sometimes referred to as *basis points volatil*ities to indicate the fact that these are expressed in absolute, rather than relative terms (as Black volatilities would).

#### Jarrow-Yildirim

Most articles on inflation modeling start out with what is referred to as the Fisher equation. This is the definition that *real returns* are given by the relative increase in *buying power* on an investment, not by nominal returns [5]. In other words, the Fisher equation is the *definition* 

$$r_{\text{real}} = r - y \tag{13}$$

 $\alpha r$ 

$$r = r_{\text{real}} + y \tag{14}$$

with  $r$  being the continuously compounded nominal rate,  $y$  the continuously compounded inflation rate, and  $r_{\text{real}}$  represents a thus defined *real rate*. While this definition is, in practice, of no further consequence to any derivatives modeling, the terminology and concepts are useful to know since they pervade the inflation modeling literature.

One of the earliest publications suggesting a comprehensive set of dynamics for the evolution of inflation (rates) in relation to nominal interest rates is the Jarrow-Yildirim model [8]. The original article discusses the generic setting of a real economy, a nominal economy, and a translation index between the two, employing the mathematical no-arbitrage HJM apparatus [6]. This results in a framework that is completely analogous to a foreign exchange rate

model with foreign (the *real* economy's) interest rate dynamics, domestic (the *nominal* economy's) interest rate dynamics, and an exchange rate that represents the inflation index. A confusing aspect for people not used to inflation financials is the nomenclature to refer to observable real-world interest rates as nominal rates, and to nonobservable (derived) inflationadjusted return rates (i.e., to nominal interest rates minus inflation rates) as *real* rates. In practice, this model tends to be implemented with both individual economies' interest rate dynamics being given by an extended Vasicek [12] ([7], but also see Term Structure Models and Gaussian Interest-Rate Models) model, with locally geometric Brownian motion for the real/nominal FX rate, that is, the inflation index. In short, in the nominal money market measure, the dynamics of nominal zero-coupon bonds  $P_T(t)$ , real zero-coupon bonds  $P_{\text{real},T}(t)$ , and the inflation index  $X(t)$  are governed by the stochastic differential equations:

$$\frac{\mathrm{d}P_T(t)}{P_T(t)} = r(t)\,\mathrm{d}t + \sigma_P(t,T)\,\mathrm{d}W_P(t) \tag{15}$$

$$\frac{\mathrm{d}P_{\mathrm{real},T}(t)}{P_{\mathrm{real},T}(t)} = \left(r_{\mathrm{real}}(t) - \rho_{P_{\mathrm{real}},X}\sigma_{X}(t)\sigma_{P_{\mathrm{real}}}(t,T)\right)\mathrm{d}t$$

$$+ \sigma_{P_{\text{real}}}(t, T) \, \mathrm{d}W_{P_{\text{real}}}(t) \tag{16}$$

$$\frac{\mathrm{d}X(t)}{X(t)} = (r(t) - r_{\text{real}}(t)) \mathrm{d}t + \sigma_X(t) \mathrm{d}W_X(t)$$
(17)

with

$$\sigma_P(t,T) = \int_t^T \zeta(s) \mathrm{e}^{-\int_t^s \kappa(u) \, \mathrm{d}u} \, \mathrm{d}s \tag{18}$$

$$\sigma_{P_{\text{real}}}(t,T) = \int_{t}^{T} \varsigma_{\text{real}}(s) e^{-\int_{t}^{s} \varkappa_{\text{real}}(u) \, du} \, \text{d}s \quad (19)$$

The Jarrow-Yildirim model, initially, gained significant popularity with quantitative analysts, though, arguably, primarily because this model could be deployed for inflation derivatives comparatively rapidly since it was already available as a crosscurrency Hull-White model in the respective practitioners' group's analytics library. Its main drawbacks are that calibration and operation of the model requires specification of a set of correlation numbers between inflation index and (nominal) interest rates,

inflation index and real rates, and (nominal) interest rates and real rates, of which only the first one is directly observable. Also, this model requires volatility specifications for nonobservable (and nontradable) real rates.

## *Inflation Forward "Market" Modeling*

In an alternative model suggested by Belgrade *et al.* [2], inflation index forward levels *F (t, Ti)* for a discrete set of maturities {*Ti*} are permitted to evolve according to

$$\frac{\mathrm{d}F(t,T_i)}{F(t,T_i)} = \mu(t,T_i)\,\mathrm{d}t + \sigma(t,T_i)\,\mathrm{d}W_i(t) \qquad (20)$$

The drift terms *µ(t, Ti)* are determined as usual by no-arbitrage conditions, but the volatility functions *σ (t, Ti)* can be chosen freely, as can the correlations between all the Wiener processes *Wi*. The authors discuss a variety of different possible choices. When interest rates are deterministic, or assumed to be uncorrelated with forward inflation index levels, all drift terms vanish and the model reduces to a set of forward levels that evolve as a multivariate geometric Brownian motion. The main drawback of this model is that it permits highly undesirable forward inflation rate dynamics, specifically with respect to the breakeven curve's autocorrelation structure, unless complicated modifications of the instantaneous correlation and volatility functions are added. The model also introduces many free parameters that have to be calibrated, which is not ideal in a market that is as illiquid as the inflation option market.

## *The Exponential Mean-reverting Period-on-period Model*

When a model's purpose is predominantly for the pricing and hedging of contracts that only depend on year-on-year returns of the inflation index, a useful model is to consider the year-on-year ratio process:

$$Y(t) = F_Y(t) e^{-\frac{1}{2}V_0[x(t)] + x(t)}$$
(21)

$$dx(t) = -\kappa x(t) dt + \alpha(t) dW(t) \qquad (22)$$

with *V*0[*x(t)*] representing the variance of the inflation driver process *x* from time 0 to time *t*, and the deterministic function *FY (t)* is implicitly defined by the choice of measure, that is, it is calibrated such that the model reproduces the breakeven curve (and thus all inflation-linked bonds) correctly. This model is known as the *exponential mean-reverting year-onyear* model. Note that even though the year-on-year ratio process is formulated as a continuous process, it is really only monitored at annual intervals when relevant fixings become available, that is,

$$Y(T_i) = \frac{I(T_i)}{I(T_i - \Omega)}$$
(23)

The advantage of this model is its comparative simplicity and its reasonable inflation curve autocorrelation characteristics. This model can also be combined with simple interest rate dynamics (such as given by the Hull–White model). A further benefit is that it promotes the view of a future inflation index level fixing being the result of year-on-year return factors:

$$I(T_n) = I(T_0) \prod_{i=1}^{n} Y(T_i)$$
 (24)

The sequence of *Y (Ti)* fixings are a set of strongly positively correlated lognormal variables (even when interest rates are stochastic in a Hull–White setting) in analogy to the correlation structure of a set of forward starting zero coupon bonds in a standard Hull–White model. As such, they lend themselves very well to an approximation of independence conditional on one or two common factors [1, 3]. Conditional independence permits easy evaluation of the LPI [11]. For other inflation products, the model can also be written on shorter periodon-period returns and can be equipped with more than one inflation driver: *x(t)* → *x*1*(t)* + *x*2*(t)*, and so on.

## *The Multifactor Instantaneous Inflation Model with Stochastic Interest Rates*

For more complex products depending on more than just the period-on-period autocorrelation structure, the exponential period-on-period model with Hull–White interest rate dynamics can be taken to the limit of infinitesimal return periods, which makes it structurally similar to the Jarrow–Yildirim model, with the main difference being that we model inflation rates directly, rather than real rates. Dropping all lag-induced convexity considerations for clarity (i.e.,

assuming  $L = 0$  and no settlement delay), this gives us, for  $m$  inflation and one interest rate factor, in the  $T$ -forward measure,

data into unobservable "real rate" volatilities and autocorrelations.

$$I(t) = F(0, t) e^{-B_a(t, T) \text{Cov}_0 \left[ \sum_{i=1}^m X_i(t), z(t) \right] - \frac{1}{2} \text{V}_0 \left[ \sum_{i=1}^m X_i(t) \right] + \sum_{i=1}^m X_i(t)}$$
(25)

$$P_T(t) = \frac{P_T(0)}{P_t(0)} e^{-B_a(t,T) \left( z(t) - \frac{1}{2} B_a(t,T) \mathsf{V}_0[z(t)] \right)}$$
(26)

$$z(t) = \int_0^t e^{-a(t-u)} \sigma(u) dW^z(u)$$
 (27)

$$x_i(t) = \int_0^t e^{-x_i(t-u)} \alpha_i(u) \, \mathrm{d}W^i(u) \tag{28}$$

$$X_i(t) = \int_0^t x_i(s) \, \mathrm{d}s = \int_0^t B_{x_i}(u, T) \alpha_i(u) \, \mathrm{d}W^i(u) \tag{29}$$

$$B_{\mu}(t_1, t_2) = \int_0^{t_2 - t_1} e^{-\mu s} ds \tag{30}$$

wherein all  $x_i$  and  $z$  are standard Ornstein-Uhlenbeck processes under the T-forward measure, of numéraire  $P_T$ , the zero-coupon bond paying in T, and we assume flat mean reversions a and  $\kappa_i$ . It is naturally straightforward to translate these dynamics to other measures (see, e.g., Forward and Swap Measures).

A suitable choice of the different drivers' correlation, volatility, and mean reversion strength permits highly flexible calibration to the inflation curve's desired autocorrelation structure, which is another major advantage over the Jarrow-Yildirim model. For the specific case when there are two inflation factors, and the mean reversion strength of one of the factors, say  $x_1$ , is taken to the limit  $x_1 \rightarrow \infty$  while at the same time keeping  $\alpha_1^2/\kappa_1$  constant, the cumulative process  $X_1$  becomes a Brownian motion.<sup>d</sup> In this case, inflation has one geometric Brownian motion factor, and one mean-reverting inflation rate factor, in complete analogy to the Jarrow-Yildirim model. In this sense, the multifactor instantaneous inflation model with stochastic interest rates encompasses the Jarrow-Yildirim model's autocorrelation structure as a special case, but, in general, allows for more flexible calibration, while, at the same time, it avoids the need to translate market observable

#### Common Inflation Modeling Considerations

Two Types of Convexity. In the inflation market, when practitioners talk about *convexity* effects, confusingly, and differently from the derivatives market of most other asset classes, they might be referring to one of the two possible effects whose origins are rather distinct.

The first of the two convexity effects arises in the context of period-on-period inflation rate related products such as year-on-year caps and floors (and obviously also inflation futures). In this context, convexity is generated only if the fundamental observable of the underlying inflation market is considered to be the *inflation index* since period-onperiod payouts are always governed by the return factor

$$Y(T-L) = \frac{I(T-L)}{I(T-K-\Omega)}$$
(31)

which is *hyperbolic*, and thus convex, in the first of the two index fixings entering the return ratio  $Y(T L$ ). For inflation derivatives practitioners whose background is firmly in the area of exotic interest rate derivatives, and who prefer to view period-on-period rates, that is,  $(Y(T - L) - 1)/\Omega$  or similar, as the fundamental underlying, this convexity, quite naturally, does not exist, and is merely an artifact of

choice of fundamental variables. Given the fact that ultimately all inflation fixing data result in the publication of an inndex figure, that is, *I (T )*, and the impact this setting has on the mind-set of inflation investors, this *hyperbolicity* effect is worth bearing in mind.

The second of the two convexity effects is the same as can be observed in other asset classes due to correlation with interest rates. It arises from a *timing discrepancy* between the fixing (observation) time of a financial observable and the time at which a payoff based on it is actually paid out. For instance, if an inflation zero-coupon swap payment is to be made with a certain delay, any nonzero correlation with interest rates gives rise to a risk-neutral valuation difference. Intuitively, one can understand this without the use of any model by considering that, in any scenario of high inflation, assuming positive correlation with interest rates, a delay of the payment is likely to incur a higher-than-average discount factor attenuation since, in that scenario, interest rates are also likely to be high. As a consequence, *ab initio*, one would tend to value a delayed inflation payment lower than its nondelayed counterpart (if we assume positive correlation between inflation and interest rates).

Both the hyperbolicity effect's and the interest rate correlation induced convexity effect's valuation formulae depend of course on the specific model used but are, typically, in any tractable model, straightforward to derive.

**Fixing Lag Effects.** An inconvenient feature of the inflation market is that the prices of tradables, even in the simplest of all possible cases, do not, in general, converge to the level at which they finally settle when the last piece of relevant market information becomes available. Take, for instance, a forward contract on the one month return of a money market account with daily interest rate accrual at the overnight rate. Clearly, the amount of uncertainty in the settlement level of this forward contract decreases at least linearly as we approach the last day of the one month period. On the day before the final overnight rate becomes known, at worst, 1/30 (say) of the uncertainty is left as to where this contract will fix. In contrast, for a similar inflation rate contract, such as a month-on-month caplet or floorlet, the amount of uncertainty in the beginning of the one month period and at its end is very

similar. This is because only limited extra information as to where the inflation index will fix becomes available during the month. As a consequence, it is common practice to consider for all volatility and variance related calculations, the reference date, that is, the point in time assumed to be *t* = 0, to be the *last index publication date*. Arguably, this may or may not be seen as an inconsistency between the framework assumed within any used model and its application, but, in practice, this appears to be a usable compromise.

Another point worth noting for the implementation of models, which is rarely spoken about in publications on the subject, is that all fixing timing tends to be subject to lags, offsets, and so on. This seemingly innocuous feature can, in practice, turn out to require intricate attention to detail. Unfortunately, since inflation structures can have very long final maturities of up to one hundred years, these small differences, if systematically erroneous, can build up to major valuation differences and can thus not be ignored. A specific mistake that is exceptionally easy to make is to assume that a breakeven curve, traded and quoted as zero-coupon swap rates, relates to future inflation index fixing levels in their own *T* -forward measure, with *T* being the publication date of the respective index level. This is insidiously wrong since actual zero-coupon swaps pay at a date that is a given tenor after the day of inception, and this could be any day in the month. For instance, if we enter into a five-year zero-coupon swap on the first of a month, ignoring weekends, this will typically settle in five years on the third of the month, and pay the index level published (say) at the beginning of the month three months before the settlement month. If we enter into the same swap on the 26th of the month, it will settle on the 28th five years later, and pay the same index fixing level as the previous example. For an arbitrary zero-coupon swap with lag *L*, depending on the day of the month at which it is entered into, this means it may settle with an effective lag of *L* months, or almost *L* + 1 months, or anything in between. Any associated interest rate convexity considerations thus depend not only on time to expiry and nominal lag but also on the day of the month. This may not sound much for a short-maturity zero-coupon swap such as one or two years, but for a 50-year zero-coupon swap, the interest rate convexity incurred makes a prohibitively expensive difference!

**Backward Induction for Interest Rate/Inflation Products.** It is not uncommon for inflation products to contain elements of a more traditional interest rate derivatives nature as, for example, was mentioned for the comparatively benign inflation swaptions discussed in the section The Inflation Swaption. When more exotic products allow for easy valuation in a strictly forward looking manner, one can of course employ Monte Carlo simulation techniques. However, if a product such as an inflation swaption is equipped with a Bermudan callable feature, as a quantitative analyst, one faces the problem that interest rates are by their nature forward looking, whereas inflation rates are by their nature backward looking. What we mean is that, typically, a natural floating interest rate coupon's absolute value is known *at the beginning* of the period for which it is paid. In contrast, floating inflation coupons are always paid after their associated period has elapsed. In a conventional backwards induction implementation on any type of lattice (e.g., explicit finite differencing solver or tree), this poses the problem that, as one has rolled the valuation back to the beginning of an interest rate period, one has to compare the value of the so induced filtration specific spot Libor rate, in some kind of payoff formula, with the contemporaneous inflation rate, which is due to the inflation driver's evolution *in the past*, and thus *unknown* on the backwards induction lattice. The problem is ultimately very similar to the valuation of, say, a forward starting equity option. The paradox is that one needs to have simultaneous access to the effect of the interest rate driver's evolution over a future interval *and* to the inflation rate driver's evolution in the past, on any valuation node in the lattice. A practical solution to this dilemma is in fact very similar to the way in which the valuation of a hindsight, or, even simpler, Asian, option in an FX or equity setting can be implemented on a lattice [13]. By enlarging the state space by one dimension, which represents a suitably chosen extra state variable, one can indeed roll back future interest rates in tandem with past inflation rates. In practice, this is in effect nothing other than a parallel roll-back of *delayed equations*. The fact that this may become necessary for what appears to be otherwise relatively vanilla products is a unique feature of the inflation market.

**The Inflation Smile.** Similar to other asset classes, volatilities implied from inflation options, when visible in the market, tend to display what is known as "smile" and "skew", and several authors have suggested the pricing of inflation options with models that incorporate a smile, for example, see [9, 10]. Unlike many other asset classes, though, the liquidity in options for different strikes, at the time of this study, is extremely thin. It is therefore arguable whether a sophisticated model that reflects a full smile is really warranted for the management of exotic inflation derivatives structures, or whether a simpler, yet more robust, model, that only permits control over the skew, or possibly even only over the level of volatility, if managed prudently (i.e., conservatively), is perhaps preferable. As and when the inflation options market becomes more liquid, the value differences between management of a trading book with a smiling model and a mere skew model may be attainable by hedging strategies, and then the use of fully fledged smile model for inflation is definitely justified. Since the liquidity in options has not significantly increased in the last few years, it is not clear whether this day of sufficient option liquidity to warrant, for instance, stochastic volatility models for inflation, will come.

## **End Notes**

a*.* The main difference between CPI and RPI is that the latter includes a number of extra items mainly related to housing, such as council tax and a range of owner-occupier housing costs, for example, mortgage interest payments, house depreciation, buildings insurance, and estate agents' and conveyancing fees.

b*.* Note that for the max*(*·*,* 1*)* function to become active, *the average inflation over the life of the bond must be negative*. While inflation does, in practice, become negative for moderate periods of time, the market tends to assign no measurable value to the risk of inflation being negative on average for decades (the typical maturity of inflation bonds). Also note that inflation bond prices tend to be quoted with a four or five digit round-off rule, and that inflation indices themselves are published rounded (typically) to one digit after the decimal point, for example, the UK RPI for June 2008 was published as 216.8 (based on 1987 at 100).

c*.* This can be confusing to newcomers to the inflation market who come from a fixed income background since a zero-coupon swap, by definition as used in the interest rate market, is a contract to never exchange any money whatsoever.

d*.* This is a consequence of the fact that an Ornstein– Uhlenbeck process, in the limit → ∞ with *α*<sup>2</sup>*/* kept constant converges to the *white noise* process, which, in turn, is in law equal to the temporal derivative of standard Brownian motion.

## **References**

- [1] Andersen, L. Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *Risk* November, 67–72.
- [2] Belgrade, N. Benhamou, E. & Koehler, E. (2004). *A Market Model For Inflation*. Technical report, CDC Ixis Capital Markets and CNCE, January. ssrn.com/abstract= 576081.
- [3] Curran, M. (1994). Valuing Asian and portfolio options by conditioning on the geometric mean price, *Management Science* **40**, 1705–1711.
- [4] Deacon, M. Derry, A. & Mirfendereski, D. (2004). *Inflation-indexed Securities*. John Wiley & Sons. ISBN 0470868120.
- [5] Fisher, I. (1930). *The Theory of Interest*. The Macmillan Company.
- [6] Heath, D. Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates, *Econometrica* **61**(1), 77–105.
- [7] Hull, J. & White, A. (1990). Pricing interest rate derivative securities, *Review of Financial Studies* **3**(4), 573–592.
- [8] Jarrow, R. & Yildirim, Y. (2003). Pricing treasury inflation protected securities and related derivatives using

an HJM model, *Journal of Financial and Quantitative Analysis* **38**(2), 409–430. forum.johnson.cornell.edu/ faculty/jarrow/papers.html

- [9] Kruse, S. (2007). *Pricing of Inflation-Indexed Options Under the Assumption of a Lognormal Inflation Index as Well as Under Stochastic Volatility*. Technical report, S-University – Hochschule der Sparkassen-Finanzgruppe; Fraunhofer Gesellschaft – Institute of Industrial Mathematics (ITWM), April. ssrn.com/ abstract=948399
- [10] Mercurio, F. & Moreni, N. (2006). Inflation with a smile, *Risk* **19**(3), 70–75.
- [11] Ryten, M. (2007). *Practical Modelling For Limited Price Index and Related Inflation Products*. In *ICBI Global Derivatives Conference*, Paris.
- [12] Vasicek, O.A. (1977). An equilibrium characterisation of the term structure, *Journal of Financial Economics* **5**, 177–188.
- [13] Wilmott, P. (1998). *Derivatives*. John Wiley & Sons.

## **Further Reading**

Crosby, J. (2007). Valuing inflation futures contracts, *Risk* **20**(3), 88–90.

PETER JACKEL ¨ & JEROME BONNETON
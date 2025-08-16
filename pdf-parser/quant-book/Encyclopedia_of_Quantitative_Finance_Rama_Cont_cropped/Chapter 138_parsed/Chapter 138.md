# **Dupire Equation**

The Dupire equation is a partial differential equation (PDE) that links the contemporaneous prices of European call options of all strikes and maturities to the instantaneous volatility of the price process, assumed to be a function of price and time only. The main application of the equation is to compute (i.e., invert) local volatilities from market option prices to build a local volatility model, which many major banks currently use for option pricing.

If we assume that the price process  $S$  follows the stochastic differential equation,

$$\frac{\mathrm{d}S_t}{S_t} = \mu_t \mathrm{d}t + \sigma(S_t, t) \,\mathrm{d}W_t \tag{1}$$

Then if  $C(S, t, K, T)$  denotes the price at time t for an underlying price of  $S$  of the European call of strike K and maturity T that pays  $(S_T - K)^+$  at time  $T$ ,  $C$  satisfies, for a fixed  $(S, t)$ .

For a fixed  $(S, t)$ , the Dupire equation,

$$\frac{\partial C}{\partial T} = \frac{\sigma^2(K,T)}{2} K^2 \frac{\partial^2 C}{\partial K^2} - (r-q) K \frac{\partial C}{\partial K} - qC \tag{2}$$

where  $r$  is the interest rate,  $q$  is the dividend yield (or foreign interest rate in the case of a currency), and the boundary conditions are given by  $C(S, t, K, T) =$  $(S - K)^{+}$ .

This can be established by a variety of methods, including double integration of the Fokker-Plank equation, Tanaka formula, and replication strategy. It is commonly named the *forward equation*, as it indicates how current call prices are affected by an increase in maturity. This can be contrasted with the classical backward Black-Scholes PDE that applies to a European call of fixed strike and maturity:

$$\frac{\partial C}{\partial t} = -\frac{\sigma^2(S,t)}{2} S^2 \frac{\partial^2 C}{\partial S^2} - (r-q)S \frac{\partial C}{\partial S} + rC \quad (3)$$

# Interpretation

The backward Black-Scholes equation applies to a given call option and relates its time derivative to its convexity. It is a heat equation that defines the price at a given time as the discounted expectation of the call price an instant later and the Jensen convexity bias  $\theta$  depends on.

According to the forward Dupire equation, the cost of extending the maturity of a call depends on the probability of being at the strike at maturity and on the level of volatility there. It can be seen as relating the price of a calendar spread to the price of a butterfly spread.

#### Uses

The equation

$$\frac{\partial C}{\partial T} = \frac{\sigma^2(K,T)}{2} K^2 \frac{\partial^2 C}{\partial K^2} - (r-q) K \frac{\partial C}{\partial K} - qC \tag{4}$$

can be used in the following two ways:

1. If the local volatility  $\sigma(S, t)$  is known, the PDE can be used to compute the price today of all call options in a single sweep, starting from the boundary condition  $C(S, t, K, T) =$  $(S-K)^{+}$ . In contrast, the Black–Scholes backward equation requires one PDE for each strike and maturity.

In the case of calibrating a parametric form of  $\sigma(S, t)$  to a set of market option prices, one needs to compute the model price of all these options and the forward equation can accelerate the computation to a factor  $100$ .

2. If the call prices are known today, one can compute their derivatives and extract the local volatility by the following formula:

$$\sigma(K,T) = \sqrt{2\frac{\frac{\partial C}{\partial T} + (r-q)K\frac{\partial C}{\partial K} + qC}{K^2\frac{\partial^2 C}{\partial K^2}}}$$
(5)

This equation is also known as the stripping formula.

Starting from a finite set of listed option prices, a good interpolation in strike and maturities provides a continuum of option prices and we can apply the stripping formula to get the local volatilities. Here is an example on the NASDAQ, where interpolation/extrapolation is performed by first fitting a stochastic volatility Heston model to the listed option

![](_page_1_Figure_1.jpeg)

Figure 1 Implied volatility surface of the NASDAQ

![](_page_1_Figure_3.jpeg)

Figure 2 Local volatility surface of the NASDAQ

prices and then applying a nonparametric interpolation to the residuals.

Figure 1 displays the implied volatility surface of NASDAQ, and the associated local volatility surface is shown in Figure 2.

Once the local volatilities are obtained, one can price nonvanilla instruments with this calibrated local volatility model (Figure 3).

Properly accounting for the market skew can have a massive impact on the price of exotics. For instance, an up-and-out call option has a positive gamma close to the strike and a negative gamma close to the barrier. A typical equity negative skew corresponds to high local volatilities close to the strike, which adds value to the option due to the positive gamma and low local volatilities close to the barrier, which is also beneficial to the option holder as the gamma is negative there.

![](_page_1_Figure_9.jpeg)

Figure 3 Local volatilities give a way to price exotic options from European options

![](_page_1_Figure_11.jpeg)

Figure 4 Comparison of an up-and-out call option in the local volatility model and in Black-Scholes model with various volatilities

The combined effect is that the up-and-out call local volatility price may exceed the price of any Black-Scholes model, irrespective of the volatility input used (Figure 4).

### Local Volatilities as Forward Volatilities

The most common interpretation of local volatility is that it is the instantaneous volatility as a certain function of spot price and time that fits market prices. It gives the simplest model calibrated to the market but assumes a deterministic behavior of instantaneous volatility, a fact crudely belied by the market. As such, the local volatility model is an important step away from the Black–Scholes model, which assumes constant volatility, though it may not necessarily provide the most realistic dynamics for the price.

The second interpretation, as forward volatilities, is far more patent. More precisely, the square of the local volatility, the local variance, is the instantaneous forward variance conditional to the spot price being equal to the strike at maturity:

$$\sigma^2(K,T) = E[\sigma_t^2 | S_T = K] \tag{6}$$

This means that in a frictionless market where all strikes and maturities are available, it is possible to combine options into a portfolio that will lock these forward values. In other words, the local variance is not only a function calibrated to the market that allows to retrieve market prices but it is also the fair value of the fixed leg of a swap with a floating leg equal to the instantaneous variance at time *T* , with the exchange taking place only if the price at maturity is *K*. It can be seen as an infinitesimal forward corridor variance swap.

By way of consequence, if one disagrees with the forward variance, one can put on a trade (in essence calendar spread against butterfly spread) aligned with this view. Conversely, if one has no view but finds someone who disagrees with the forward view and accepts to trade at a different level, one can lock the difference.

Another important consequence of this relationship is that a stochastic volatility model (with no jumps) will be calibrated to the market if and only if the conditional expectation of the instantaneous variance is the local variance computed from the market prices. In essence, it means that a calibrated stochastic volatility model is a noisy version of the local volatility model, which is centered on it. In this sense, the local volatility model plays a central role.

Beyond the fit to the current market prices, these results have dynamic consequences. For example, they imply that in the absence of jumps, the atthe-money (ATM) implied volatility converges to the instantaneous volatility when the maturity shrinks to 0. The same relation indicates that for any stochastic volatility model calibrated to the market, the average level of the short-term ATM implied variance at any time in the future, conditioned on a price level, has to equal the local variance, which is dictated by the current market prices of calls and puts. Fitting to today's market strongly constrains future dynamics and, for instance, the backbone, defined as the behavior of the at-the-money volatility as a function of the underlying price, cannot be independently specified.

Once we get a perfect fit of option prices using equation (5), we can perturb the volatility surface, recalibrate, and conduct a sensitivity analysis. This provides a decomposition of the volatility risk of any structured product (or portfolio of) across strikes and maturities, because seeing the price as a function of the whole volatility surface provides through perturbation analysis the sensitivity to all volatilities.

# **Extensions**

There are numerous extensions of the forward PDE, with stochastic rates and dividends, stochastic volatility, jumps, to the Greeks (sensitivities) and to other products than European options, such as barrier options, compound options, Asian options, and basket options. However, until now, there is no satisfactory counterpart for American options.

# **Further Reading**

- Derman, E. & Kani, I. (1994). Riding on a smile, *Risk* **7**(2), 32–39, 139–145.
- Dupire, B. (1993). Model art, *Risk* **6**(9), 118–124.
- Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- Dupire, B. (1997). Pricing and hedging with smiles, in *Mathematics of Derivative Securities*, M.A.H. Dempster & S.R. Pliska, eds, Cambridge University Press.
- Dupire, B. (2004). A unified theory of volatility, working paper Paribas capital markets 1996, reprinted in *Derivatives Pricing: The Classic Collection*, P. Carr, ed., Risk Books, London.

# **Related Articles**

**Implied Volatility Surface**; **Local Times**; **Local Volatility Model**; **Markov Processes**; **Model Calibration**.

BRUNO DUPIRE
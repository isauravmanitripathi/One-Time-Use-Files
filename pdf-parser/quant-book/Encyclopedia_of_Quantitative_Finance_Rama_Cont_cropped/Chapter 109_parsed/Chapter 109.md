# **Lookback Options**

Lookback options are path-dependent options, introduced at first in [25] and [26], characterized by having their settlement based on the minimum or the maximum value of an underlying index as registered during the lifetime of the option. At maturity, the holder can "lookback" and select the most convenient price of the underlying that occurred during this period: therefore they offer investors the opportunity (at a price, of course) of buying a stock at its lowest price and selling a stock at its highest price. Since this scheme guarantees the best possible result for the option holder, he or she will never regret the option payoff. As a consequence, a lookback option is more expensive than a vanilla option with similar payoff function. However, these options do not offer a natural hedge for typical business and are used mainly by speculators. To mitigate their cost, sometimes the lookback feature is mixed with an average feature: for example, the payoff is the best or the worst of past average prices and they are offered as investment product under names such as *Everest*, *Napoleon*, and Altiplano.

In the section Payoff Function, we describe lookback options payoff. In the section Pricing, we illustrate the pricing of these options in the Black-Scholes setting and some results on the hedging problem. Thereafter, in the section Non-Gaussian Models, we consider the pricing problem under non-Gaussian models. Finally, in the section Related Payoff, we present payoffs related to lookback options.

# **Pavoff Function**

A lookback option can be structured as a put or call. The strike can be either fixed or floating. We now consider two lookback options written on the minimum value achieved by the underlying index during a fixed time window:

A fixed strike lookback put The payoff is given by the difference, if positive, between the strike price and the minimum price over the monitoring period. Therefore, the buyer of this option can sell the asset at the minimum price receiving the strike  $K$ 

A floating strike lookback call The payoff is given by the difference between the asset price at the option maturity, which represents the floating strike, and the minimum price over the monitoring period. Therefore, the buyer of this option can buy the underlying asset paying the minimum price.

Notice that floating strike options will always be exercised. Formulae for the payoffs are provided in Table 1, as well as versions involving the maximum and variants denominated *partial price* or *partial* time.

## Pricing

In this section, we discuss the pricing problem under the geometric Brownian motion (GBM) assumption, that is.

$$dS(t) = (r - q)S(t)dt + \sigma S(t)dW(t), S(0) = S_0$$
(1)

where  $r$  is the instantaneous risk-free rate;  $q$  is the instantaneous dividend yield;  $\sigma$  is the percentage volatility;  $S_0$  is the initial underlying price; and we are interested in the distribution of the minimum  $m(T)$ and maximum  $M(T)$ 

$$M(T) = \max_{0 \le u \le T} S(u), \text{ and } m(T) = \min_{0 \le u \le T} S(u)$$
(2)

Figure 1 illustrates a simulated path of the underlying asset according to the dynamics in equation 1 and the corresponding trajectories for the maximum and minimum price.

### Analytical Solution

Under the GBM assumption, the distribution law of  $m(T)$  (as well as the joint density of  $m(T)$  and  $S(T)$ ) is known in closed form. This allows one to obtain an analytical solution for standard lookback options as expected value of the discounted payoff; see, for example, [25, 26], and [15]. Therefore, we obtain the following pricing formula for the floating strike lookback call:

$$\mathbb{E}_{t,S_t} e^{-r(T-t)} (S(T) - m(T))$$
  
=  $S_t e^{-q(T-t)} - e^{-r(T-t)} \mathbb{E}_{t,S_t} m(T)$   
=  $S_t e^{-q(T-t)} \mathcal{N}(d_2)$ 

<table>

 **Table 1** Lookback option payoff function

|                       | Generic lookbacks<br>Minimum   | Maximum                            | Range                    |
|-----------------------|--------------------------------|------------------------------------|--------------------------|
|                       | $m(T) = \min_{0 < u < T} S(u)$ | $M(T) = \max_{0 \le u \le T} S(u)$ | $M(T) - m(T)$            |
| Standard lookbacks    |                                |                                    |                          |
|                       | Floating strike                | Fixed strike                       | Reverse strike           |
| Call                  | $(S(T) - m(T))^{+}$            | $(M(T)-K)^+$                       | $(m(T)-K)^{+}$           |
| $\text{Put}$          | $(M(T) - S(T))^{+}$            | $(K-m(T))^{+}$                     | $(K-M(T))^{+}$           |
| Nonstandard lookbacks |                                |                                    |                          |
|                       | Partial price                  | Partial time                       | conditions               |
| Call                  | $(S(T) - \lambda m(T))^{+}$    | $(S(T_2) - m(T_1))^+$              | $\lambda > 1, T_1 < T_2$ |
| $\text{Put}$          | $(\gamma M(T) - S(T))^{+}$     | $(M(T_1) - S(T_2))^+$              | $\mu < 1, T_1 < T_2$     |

![](_page_1_Figure_3.jpeg)

Figure 1 Geometric Brownian motion and its maximum and minimum to date

$$\begin{aligned} & -\mathrm{e}^{-r(T-t)}m_{t}\mathcal{N}\Big(d_{2}-\sigma\sqrt{T-t}\Big) \\ & + \frac{\sigma^{2}S_{t}}{2r}\bigg[\mathrm{e}^{-r(T-t)}\bigg(\frac{S_{t}}{m_{t}}\bigg)^{-2r/\sigma^{2}}\mathcal{N}(d_{3}) \\ & - \mathrm{e}^{-q(T-t)}\mathcal{N}(-d_{2})\bigg] \end{aligned} \tag{3}$$

with

$$d_2 = \frac{1}{\sqrt{\sigma^2(T-t)}} \left( \ln\left(\frac{S_t}{m_t}\right) + (r-q)(T-t) + \frac{1}{2}\sigma^2(T-t) \right),$$

$$d_3 = -d_2 + \frac{2(r-q)}{\sigma} \sqrt{T-t},$$
  
$$\mathcal{N}(x) = \int_{-\infty}^{x} e^{\frac{-u^2}{2}} du \tag{4}$$

Notice that the formula above admits a simplification when  $t = 0$ : indeed, in this case, we have  $S(0) = m(0)$ . Formula 3 suggests that the lookback call value is given by the sum of the premium of a plain vanilla call with strike equal to the current minimum and the premium of a so-called strike bonus option. This is the expected value of the cash flows necessary to exchange the initial option position for options with successively more favorable strikes. In other words, it measures the potential decrease in the price at which the option allows its holder to buy the security, if and when the security price attains a new minimum.

For pricing the fixed strike put option, we have

$$\begin{split} &\mathbb{E}_{t,S_{t}} \mathrm{e}^{-r(T-t)} \left( K - m(T) \right)^{+} \\ &= \mathbf{1}_{\left( K < m_{t} \right)} \bigg\{ -S_{t} \mathcal{N}(-d) + \mathrm{e}^{-r(T-t)} \\ &\times K \mathcal{N} \left( -d + \sigma \sqrt{T-t} \right) + \left( \frac{\sigma^{2}}{2r} \right) S_{t} \\ &\times \left[ \mathrm{e}^{-r(T-t)} \bigg( \frac{S_{t}}{K} \bigg)^{-2r/\sigma^{2}} \mathcal{N} \bigg( d_{1} \bigg) - \mathcal{N}(-d) \right] \bigg\} \\ &+ \mathbf{1}_{\left( K \geq m_{t} \right)} \bigg\{ \mathrm{e}^{-r(T-t)} (K - m_{t}) - S_{t} \mathcal{N}(-d_{2}) \end{split}$$

3

$$+ e^{-r(T-t)} m_t \mathcal{N}\left(-d_2 + \sigma \sqrt{T-t}\right) + \left(\frac{\sigma^2}{2r}\right) S_t$$
$$\times \left[ e^{-r(T-t)} \left(\frac{S_t}{m_t}\right)^{-2r/\sigma^2} \mathcal{N}(d_3) - \mathcal{N}(-d_2) \right] \right\} \tag{5}$$

with

$$d = \frac{1}{\sqrt{\sigma^2(T-t)}} \left( \ln\left(\frac{S_t}{K}\right) + (r-q)(T-t) + \frac{1}{2}\sigma^2(T-t) \right),$$
  
$$d_1 = \frac{-d+2(r-q)}{\sigma} \sqrt{T-t} \tag{6}$$

Lookback options on the maximum can be priced by exploiting the relation between maximum and minimum operators.

An important feature of lookbacks is the frequency of observation of the underlying assets for the purpose of identifying the best possible value for the holder. For example, the above expressions are consistent with the assumption that the underlying asset is monitored continuously. Instead, discrete monitoring refers to updating the maximum/minimum price at fixed times (e.g., daily, weekly, or monthly). In this case, we have to replace  $M(T)$  and  $m(T)$  by  $\widehat{M}(T)$ and  $\widehat{m}(T)$ , defined as

$$\widehat{M}(T) = \max_{0 \le i \le n} S(i\,\Delta), \text{ and } \widehat{m}(T) = \min_{0 \le i \le n} S(i\,\Delta) \tag{7}$$

where  $n$  is the number of monitoring dates and  $\Delta$  is the time distance between monitoring dates; with  $n\Delta = T$ . Nearly all closed-form expressions available for pricing path-dependent options are based on continuous-time paths, but many traded options are based on discrete price fixings. In general, a higher maximum/lower minimum occurs as long as the number  $n$  of monitoring dates increases. As noted by Heynen and Kat [29] and Aitsahlia and Leung [1], the discrepancy between option prices under continuous and discrete monitoring of the reference index may have significant effect on the prices of lookback options, but does not introduce new hedging problems. Indeed, the slow convergence of the discrete scheme to the continuous one as the number  $n$  of monitoring dates increases is well known. This figure is quantified in an order of proportionality of approximately  $1/\sqrt{n}$ .

For example, setting  $r = 0.1$ ,  $q = 0$ ,  $\sigma = 0.2$ ,  $T = 1$ ,  $S_0 = 100$ , the continuous formula returns 19.6456. Assuming a year consists of 250 days and that 10 monitoring dates are available (i.e., monitoring occurs approximately once a month), the discrete formula gives 17.0007: a percentage difference about 15% with respect to the continuous case. Using 10 000 monitoring dates (i.e., monitoring occurs once every 36 minutes), the discrete formula returns 19.5523, a small but still appreciable difference with respect to the continuous case.

Few papers have investigated the analytical pricing of discretely monitored lookback options. A correction to the continuously monitored formula based on the Riemann zeta function is given in [12]. The Riemann zeta function enters indeed in the computations of the moments of the discrete maximum/minimum; see, for example, [23, 27, 31, 32, 34], for different derivations and improvements of the above correction. New results for discrete options have been recently obtained exploiting the Wiener-Hopf factorization and the Spitzer's identity. For example, [5] and [27] present an exact analytical formula showing how to cast the pricing problem in terms of an integral equation of the Wiener-Hopf type. This equation can be solved in closed form in the Gaussian case. The computational cost is linear in the number of monitoring dates. A related approach based on the Spitzer's identity (the probabilistic interpretation of the solution of a Wiener-Hopf equation) has been advanced by Borovkov and Novikov [9] and by Petrella and Kou [39]. They propose an algorithm with a computational cost that is quadratic in the number of monitoring dates but has the advantages of being simply adapted to non-Gaussian models provided that they have independent identically distributed (i.i.d.) increments and the pricing formula of plain vanilla calls and puts are available.

Other approaches are mainly numerical and briefly detailed in the following subsections.

### Finite Difference Method

The numerical solution of the partial differential equation (PDE) satisfied by the lookback option price is discussed for example in [42] and a detailed treatment for the discrete case is given in [3]. Since lookback options are path-dependent options, their value  $V$  does not depend only on the current spot price and time, but also on the current realized minimum or maximum, and we can write  $V =$  $V(S, m, t)$  for options on the minimum (similar discussion holds for lookback on the maximum). Applying Ito's lemma and equating the expected return on the option to the return on a risk-free investment, it can be shown that  $V$  solves the following PDE:

$$\frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2} = rV \qquad (8)$$

which has to be solved for  $S \ge m$  and  $T \ge t \ge 0$ . The above PDE is the standard Black-Scholes PDE, with the change of the domain from  $S > 0$  to  $S > m$ . Here  $m$  appears as parameter delimiting the domain of the spot price. This implies that a boundary condition at  $S = m$  is needed. The important point is the observation that when the spot price is near to the running minimum, the probability that at expiry the minimum will be equal to the current minimum  $m$  is zero and therefore changes in  $m$  do not affect the option value. This allows one to set the boundary condition at  $S = m$ :

$$\frac{\partial V(S, m, t)}{\partial m} = 0 \text{ when } S = m \tag{9}$$

Together with the payoff condition at  $t = T$ , equations (8) and (9) allow us to fully characterize the lookback option premium. For discretely monitored lookback options, with monitoring at dates  $t_i = i\Delta$  the PDE (8) remains unchanged, while the boundary condition (9) does not apply anymore. Indeed, between monitoring dates, the spot price can freely move in  $(0, +\infty)$  and at monitoring dates, the solution is updated according to the rule

$$V(S, m, t_i^+) = V(S, \min(S, m), t_i^-) \qquad (10)$$

Equation (8) can be solved numerically using an appropriate numerical scheme such as the Crank–Nicolson one (*see* **Crank–Nicolson Scheme**). However, exploiting a change of numeraire, the PDE  $(8)$  can be simplified to a single state variable  $[3]$ .

#### Monte Carlo Simulation

Discretely monitored lookback options can be easily priced by standard Monte Carlo (MC) simulation. The underlying price is simulated at all monitoring dates exploiting the exact solution of the stochastic differential equation  $(1)$ :

$$S^{(j)}((i+1)\Delta) = S^{(j)}(i\Delta)e^{(r-0.5\sigma^2)\Delta + \sigma\sqrt{\Delta}\epsilon_i^{(j)}} \quad (11)$$

where  $\epsilon_i^{(j)}$  is a standard normal random variate and  $S^{(j)}(i\Delta)$  is the spot price at time  $t_i = i\Delta$  as sampled in the  $i$ th simulation.

The corresponding minimum price  $m^{(j)}(i\Delta)$  over the time interval  $t_{(i-1)\Delta}$ ,  $t_{i\Delta}$  is updated at each monitoring date according to the rule

$$\widehat{m}^{(j)}(i\,\Delta) = \min\left(S^{(j)}(i\,\Delta), \widehat{m}^{(j)}((i-1)\Delta)\right) \quad (12)$$

with a starting condition  $m_0^{(j)} = S_0$ . The MC price for a lookback is given by the average of the discounted payoff computed over  $J$  simulated sample paths. For a lookback option with fixed strike  $K$ , the MC price is

$$e^{-rt_n}\frac{1}{J}\sum_{j=1}^{J}\left(K-\widehat{m}^{(j)}(n\Delta)\right)^{+}$$
 (13)

Similarly, for a floating strike lookback option, the MC price is

$$e^{-rt_n}\frac{1}{J}\sum_{j=1}^{J}\left(S^{(n\Delta)}-\widehat{m}^{(j)}(n\Delta)\right) \qquad (14)$$

Unfortunately, the procedure cannot be immediately applied to continuously monitored options shrinking the time step  $\Delta$ . Indeed, owing to fact that we can only sample at discrete times, we lose information about the parts of the continuous-time path that lie between the sampling dates. This procedure will be systematically biased in the sense that the continuous minimum (maximum) will be always overestimated (underestimated). Andersen and Brotherton-Ratcliffe [4] show that for a one-year lookback with 256 discrete monitoring points this bias is around 5% of the option price and suggest a procedure to correct it.

#### Binomial and Tree Methods

As for PDEs, the implementation of a tree for path-dependent options involves two state variables and the need to keep track of current extreme values will cause the number of calculations to grow substantially faster than the number of nodes. However, under the GBM assumption and exploiting a change of numeraire, the pricing of lookback options can be reduced to one-state binomial model (having a reflecting barrier at 0); see, for instance, [6] and [14], as well as **Tree Methods**. Using such models cuts the amount of computation remarkably and also makes it straightforward to deal with the early exercise feature.

## *Hedging*

We conclude this section, mentioning the hedging problem of lookback options. When *r* = *q* + *σ*<sup>2</sup>*/*2, lookback options can be exactly replicated using a self-financing strategy based on straddles (an ordinary put plus an ordinary call) with an exercise price equal to the initial extremum (maximum or minimum) [25]. If, over the life of the option, the stock price never rises above or falls below its initial value, the initial straddle would exactly satisfy the writer's terminal obligation. When the stock price is at an extremum and then achieves a new maximum or minimum, the straddle should be sold and a new portfolio established, a straddle with exercise price equal to the new maximum (minimum). This strategy is self-financed and replicates the lookback option. However, in general, the replicating strategy requires the computation of the coefficient, that is, units of stocks needed to replicate the contingent claim, by taking the derivative of the pricing formula with respect to the current spot price. An alternative method is put forward by the use of the Malliavin calculus approach, and the main component for this method to work is a sort of representation theorem, called the *Clark–Ocone formula*. This formula allows us to identify a formal expression for the replicating portfolio of basically any contingent claim. This has been exploited in [8] to obtain the replicating portfolio.

A different approach is taken in [30] that finds bounds on the prices of the lookback option, in terms of the (market) prices of call options. This is achieved without making explicit assumptions about the dynamics of the price process of the underlying asset, but rather by inferring information about the potential distribution of asset prices from the call prices. Thus the bounds and the associated hedging strategies are model independent and represent limits on the possible price of the lookback, which are necessary for the absence of arbitrage.

# **Non-Gaussian Models**

The GBM model in equation (1) is one of the most successful and widely used models in financial economics. Unfortunately, deviations between the model and empirical evidence are well known in literature and therefore offer new opportunities for the development of more-realistic models and pricing formulas for exotic options. With reference to lookback options, extensions have been obtained replacing the GBM model by the constant elasticity of variance (CEV) model (*see* **Constant Elasticity of Variance (CEV) Diffusion Model**) or by an exponential Levy ´ model (*see* **Exponential Levy Models ´** ). In the following sections we discuss such extensions.

## *CEV*

The study of lookback options in the CEV model has started with [10] and [11]. Their approach consists in approximating the CEV process by a trinomial lattice and uses it to value barrier and lookback options numerically. A binomial tree is also used in [16]. While these approaches are purely numerical, in [20] closed-form solutions for the Laplace transforms of the probability distributions of the maximum and minimum are obtained. Lookback prices are recovered by inverting the Laplace transforms and integrating against the option payoff. An analytical inversion of the Laplace transforms for lookback options in terms of spectral expansions associated with the infinitesimal generator of the CEV diffusion is given in [36]. All these studies point out that the differences in prices of these exotic options under the CEV and geometric Brownian motion assumptions can be far more significant than the differences for standard European options.

### *L´evy Processes*

Lookback options have been priced also under Levy ´ processes. For example, in [13] a very powerful algorithm is proposed that can be adapted for pricing discrete lookback under a jump-diffusion model. For more general Levy processes, very efficient algo- ´ rithms have been proposed in [22, 39] and [24]. An analytical expression in terms of the Laplace transform is found for continuously monitored options, under a double-exponential model, in [35].

## **Related Pavoff**

Several exotic options can be thought of as a modification of lookback options. We have mentioned a few of them here.

In *partial lookback* options, the lookback feature is limited to only the first (for entry timing) or the last (for exit timing) part of the options' life. This product, even with a relatively short lookback periods, appears to offer a good solution to most timing problems at a reasonable price. Kat and Heynen [33] provide closed-form pricing formulas for such options. Analysis shows how the prices of such "partial lookback options" respond to a change in the monitoring period.

*Quanto lookback* refers to a payoff structure where the terminal payoff of the quanto option depends on the realized extreme value of a stock denominated in a foreign currency but the payoff is paid in a domestic currency. These contracts have been studied in [18].

Double lookbacks or Range options include calls and puts with the underlying being the difference between the maximum and minimum prices of one asset over a certain period, and calls or puts with the underlying being the difference between the maximum prices of two correlated assets over a certain period. Analytical expressions of the joint probability distribution of the maximum and minimum values of two correlated geometric Brownian motions are derived in [28] and used in the valuation of double lookbacks. An option on the spread between the maximum and minimum price of a single stock over a given interval of time captures the idea of an option on price volatility; see, for example, the related literature on financial econometrics devoted to estimate the volatility using range estimators. Therefore, such an option might be of interest to traders who want to bet on price volatility or hedge an existing position that is sensitive to price volatility.

*Quantile* options have a payoff at maturity depending on the order statistics of the underlying asset price. The *j*-quantile process  $q(n, j)$  is defined as the level at which the return process stays below for j periods out of n. In particular, we have  $q(n, n) =$  $\widehat{M}(n\Delta)$  and  $q(n,0) = \widehat{m}(n\Delta)$ . The quantile payoff is obtained replacing the extreme appearing in Table 1 by the quantile  $q(n, j)$ . These options can be priced by making use of what is known as the Dassios-Port-Wendel identity [19], that allows one to write the quantile as sum

$$q(n,j) \stackrel{a}{=} \widehat{m}((n-j)\,\Delta) + \widehat{M}(j\,\Delta) \qquad (15)$$

where  $\stackrel{d}{=}$  means equality in distribution and  $\widehat{m}((n (j)\Delta$ ) and  $\widehat{M}(j\Delta)$  are independent processes. From this identity, it follows that the density of the quantile is the convolution of the densities of  $\widehat{m}((n - j)\Delta)$ and  $\widehat{M}(j\Delta)$  and, at the issue date of the contract, the quantile price can be obtained as expected discounted payoff under the risk-neutral measure; see [5] and [19] for details. Another way of exploiting the Dassios-Port-Wendel identity consists in, conditioning on the minimum, representing the quantile option price as average of lookback option prices written on the maximum and with random strike. The average is taken with respect to the density of the discrete minimum. Finally, we remark that the pricing off the inception date is not straightforward, because the quantile process is non-Markovian. A discussion can be found in [19]. Other relevant references are [2, 38], and [7].

A drawdown (drawup) option is defined as the drop (increase) of the asset price from its running maximum (minimum),  $D(t) = M(t) - S(t)$ ,  $(U(t) =$  $S(t) - m(t)$ ). Maximum drawdown  $MDD(t)$  is defined as the maximal drop of the asset price from its running maximum over a given period of time:

$$MDD(t) = \max_{0 \le s \le t} D(s) \tag{16}$$

In a similar manner, we can define the maximum drawup. Maximum drawdown measures the worst loss of an investor who enters the market at a certain point and leaves it at some following point within a given time period; this means that he or she buys the asset at a local maximum and sells it at the subsequent lowest point, and this drop is the largest in the given time period. A derivative contract on the maximum drawdown, introduced in [41], can serve as an important risk measure indicator: when the market is in a bubble, it is reasonable to expect that the prices of drawdown contracts would be significantly higher. On the other hand, when the market is stable, or when it exhibits mean reversion behavior, the prices of drawdown contracts would become cheaper. When the market experiences a crash, the lookback option may expire close to worthless if the final asset value is near its running maximum. Momentum traders believe that the realized maximum drawdown (maximum drawup) will be larger than expected, and thus they are natural buyers of this contract. On the other hand, selling the (unhedged) contract is equivalent to taking the opposite strategy, namely, buying the asset when it is setting its new low. This is known as *contrarian trading*. Contrarian traders believe that the realized maximum drawdown (maximum drawup or range) will be smaller than expected, and they are natural sellers of this contract. The distribution of the maximum drawdown of Brownian motion is studied in [37].

*Russian options* are perpetual American Options with lookback payoff, introduced in [40]. Russian options can be regarded as a kind of perpetual American fixed strike lookback option with zero strike price and their pricing can be derived by using a probability approach [21], or a PDE approach [17].

Finally, we mention the class of structures named *mountain options*, having names such as Himalaya, Everest, Altiplano and so on (*see* **Atlas Option**; **Himalayan Option**; **Altiplano Option**). Here, the extrema over a given period of a given asset is replaced by the best or the worst performer over different periods of assets in a given basket. Sometimes, a global floor on the return of the product is also introduced. It is clear that MC simulation is needed to be able to price this type of products, that, in general, are very sensible to the crosscorrelation of the assets. In addition, the Greeks of these contracts can change markedly as the trade progresses.

# **References**

- [1] Aitsahlia, F. & Leung, L.T. (1998). Random walk duality and the valuation of discrete lookback options, *Applied Mathematical Finance* **5**(3/4), 227–240.
- [2] Akahori, J. (1995). Some formulae for a new type of path-dependent option, *Annals of Applied Probability* **5**, 383–388.
- [3] Andreasen, J. (1998). The pricing of discretely sampled Asian and lookback options: a change of numeraire approach, *Journal of Computational Finance* **2**(1), 5–30.
- [4] Andersen, L. & Brotherton-Ratcliffe, R. (1996). Exact exotics, *Risk Magazine* **9**, 85–89.
- [5] Atkinson, C. & Fusai, G. (2007). Discrete extrema of Brownian motion and pricing of exotic options, *Journal of Computational Finance* **10**(3), 1–43.
- [6] Babbs, S. (2000). Binomial valuation of lookback options, *Journal of Economic Dynamics and Control* **24**(11–12), 1499–1525.

- [7] Ballotta, L. & Kyprianou, A. (2001). A note on the Alpha-Quantile option, *Applied Mathematical Finance* **8**, 137–144.
- [8] Bermin, H.-P. (2000). Hedging lookback and partial lookback options using Malliavin calculus, *Applied Mathematical Finance* **39**, 75–100.
- [9] Borovkov, K. & Novikov, A. (2002). On a new approach for option pricing, *Journal of Applied Probability* **39**, 1–7.
- [10] Boyle, P.P. & Tian, Y. (1999). Pricing lookback and barrier options under the CEV process, *Journal of Financial and Quantitative Analysis* **34**, 241–264.
- [11] Boyle, P.P., Tian. Y. & Imai, J. (1999). Lookback options under the CEV process: a correction, *Journal of Finance and Quantitative Analysis* web site http://www.jfqa.org/. In: Notes, Comments, and Corrections.
- [12] Broadie, M., Glasserman, P. & Kou, S. (1999). Connecting discrete and continuous path-dependent options, *Finance and Stochastics* **3**, 55–82.
- [13] Broadie, M. & Yamamoto, Y. (2005). A doubleexponential fast Gauss transform algorithm for pricing discrete path-dependent options, *Operations Research* **53**(5), 764–779.
- [14] Cheuck, T.H.F. & Vorst, T.C.F. (1997). Currency lookback options and observation frequency: a binomial approach, *Journal of International Money and Finance* **16**(2), 173–187.
- [15] Conze, A. & Vishwanathan, R. (1991). Path-dependent options: the case of lookback options, *Journal of Finance* **46**, 1893–1907.
- [16] Costabile, M. (2006). On pricing lookback options under the CEV process, *Decisions in Economics and Finance* **29**, 139–153.
- [17] Dai, M. (2000). A closed-form solution for perpetual American floating strike lookback options, *Journal of Computational Finance* **4**(2), 63–68.
- [18] Dai, M., Kwok, Y.K. & Wong, H.Y. (2004). Quanto lookback options, *Mathematical Finance* **14**(3), 445–467.
- [19] Dassios, A. (1995). The distribution of the quantile of a Brownian motion with drift & the pricing of related path-dependent options, *Annals of Applied Probability* **5**, 389–398.
- [20] Davydov, D. & Linetsky, V. (2001). The valuation and hedging of barrier and lookback options under the CEV process, *Management Science* **47**, 949–965.
- [21] Duffie, D. & Harrison, J.M. (1993). Arbitrage pricing of Russian options and perpetual lookback options, *The Annals of Applied Probability* **3**(3), 641–651.
- [22] Feng, L. & Linetsky, V. (2009). Computing exponential moments of the discrete maximum of a Levy process and lookback options, *Finance and Stochastics*, available at SSRN:http://ssrn.com/abstract=1260934.
- [23] Fusai, G., Abrahams, I.D. & Sgarra, C. (2006). An exact analytical solution for discrete barrier options, *Finance and Stochastics* **10**(1), 1–26.

- [24] Fusai, G., Marazzina, D., Marena, M. & Ng, M. (2008). *Maturity Randomization and Option Pricing*. w.p. SEMeQ.
- [25] Goldman, M.B., Sosin, H.B. & Gatto, M.A. (1979). Path-dependent options: buy at the low, sell at the high, *Journal of Finance* **34**, 1111–1127.
- [26] Goldman, M.B., Sosin, H.B. & Shepp, L. (1979). On contingent claims that insure ex-post optimal stock market timing, *Journal of Finance* **34**, 401–413.
- [27] Green, R., Fusai, G. & Abrahams, I.D. (2009). The Wiener-Hopf technique & discretely monitored path dependent option pricing, *Mathematical Finance*, to appear.
- [28] He, H., Keirstead, W. & Rebholz, J. (1998). Double lookbacks, *Mathematical Finance* **8**, 201–228.
- [29] Heynen, R.C. & Kat, H.M. (1995). Lookback options with discrete and partial monitoring of the underlying price, *Applied Mathematical Finance* **2**, 273–284.
- [30] Hobson, D.G. (1998). Robust hedging of the lookback option, *Finance and Stochastics* **2**(4), 329–347.
- [31] Horfelt, P. (2003). Extension of the corrected bar- ¨ rier approximation by Broadie, Glasserman, and Kou, *Finance and Stochastics* **7**(2), 231–243.
- [32] Howison, S. & Steinberg, M. (2007). A matched asymptotic expansions approach to continuity corrections for discretely sampled options. Part 1: barrier options, *Applied Mathematical Finance* **14**, 63–89.
- [33] Kat, H.M. & Heynen, R.C. (1994). Selective memory. *Risk Magazine* **7**(11), 73–76.
- [34] Kou, S.G. (2003). On pricing of discrete barrier options, *Statistica Sinica* **13**, 955–964.

- [35] Kou, S.G. & Wang, H. (2003). First passage times of a jump diffusion process, *Advances in Applied Probability* **35**, 504–531.
- [36] Linetsky, V. (2004). Lookback options and diffusion hitting time: a spectral expansion approach, *Finance and Stochastics* **8**, 373–398.
- [37] Magdon-Ismail, M., Atiya, A., Pratap, A. & Abu-Mostafa, Y. (2004). On the maximum drawdown of a Brownian motion, *Journal of Applied Probability* **41**(1), 147–161.
- [38] Miura, R. (1992). A note on lookback options based on order statistics, *Hitotsubashi Journal of Commerce & Management* **27**, 15–28.
- [39] Petrella, G. & Kou, S.G. (2004). Numerical pricing of discrete barrier and lookback options via Laplace transforms, *Journal of Computational Finance* **8**, 1–37.
- [40] Shepp, L. & Shiryaev, A.N. (1993). The Russian option: reduced regret, *Annals of Applied Probability* **3**, 631–640.
- [41] Vecer, J. (2006). Maximum drawdown and directional trading, *Risk Magazine* **19**(12), 88–92.
- [42] Wilmott, P., Dewynne, J.N. & Howison, S. (1993). *Option Pricing: Mathematical Models and Computation*, Oxford Financial Press.

# **Related Articles**

**Barrier Options**; **Corridor Options**; **Discretely Monitored Options**; **Parisian Option**.

GIANLUCA FUSAI
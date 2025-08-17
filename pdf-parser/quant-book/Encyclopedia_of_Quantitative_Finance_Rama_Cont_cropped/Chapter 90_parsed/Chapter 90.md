## **Asian Options**

An Asian option is also known as a fixed-strike Asian option or an average price or average rate option. These options have a payoff based on the average of an underlying asset price over a specified time period. The Asian option has a payoff dependent on the average of the asset price and a strike that is fixed in advance. The other type of Asian option is the average strike option (or floating strike), where the payoff is determined by the difference between the underlying asset price and its average (see Average Strike **Options**). Asian options are path-dependent options as their payoff depends on the asset price path rather than just on the terminal value.

If the average is computed using a finite sample of asset price observations taken at a set of regularly spaced time points, we have a discrete Asian option. A continuous time Asian option is obtained by computing the average *via* the integral of the price path over an interval of time. In reality, contracts are based on discrete averaging; however, if there are a large number of averaging dates, there are advantages in working in continuous time. The average itself can be defined to be geometric or arithmetic. When the geometric average is used, the Asian option has a closed-form solution for the price, whereas the option with arithmetic average does not have a known closed-form solution.

One of the reasons Asian options were invented was to avoid price manipulation toward the end of the option's life. By making the payoff depend on the average price rather than on the price itself, such manipulations have little effect on the option value. For this reason, Asian options are usually of European style. The possibility of exercise before the expiration date would make the option more vulnerable to price manipulation; see [11]. The payoff of an Asian option cannot be obtained by combining other instruments such as vanilla options, forwards, or futures.

Asian options are commonly used for currencies, interest rates, and commodities, and more recently in energy markets. They are useful in corporate hedging situations, for instance, a company exchanging foreign currency for domestic currency at regular intervals. Each transaction could be hedged separately with derivatives or a single Asian option could hedge the "average" rate over the period during which the currency is transferred.

An advantage for the buyer of an Asian option is that it is often less expensive than an equivalent vanilla option. This is because the volatility of the average is lower than the volatility of the asset itself. Another advantage in thinly traded markets is that the payoff does not depend only on the price of the asset on a particular day.

Consider the standard Black-Scholes economy with a risky asset (stock) and a money market account. We also assume the existence of a riskneutral probability measure  $Q$  (equivalent to the real-world measure  $P$ ) under which discounted asset prices are martingales. Under measure  $Q$  we denote the expectation by  $E$ , and under  $Q$ , the stock price follows:

$$\frac{\mathrm{d}S_t}{S_t} = (r - \delta)\,\mathrm{d}t + \sigma\,\mathrm{d}W_t \tag{1}$$

where  $r$  is the constant continuously compounded interest rate,  $\delta$  is a continuous dividend yield,  $\sigma$  is the instantaneous volatility of asset return, and  $W$  is a  $O$ -Brownian motion. The reader is referred to Black-Scholes Formula for details on the Black-Scholes model and **Risk-neutral Pricing** for a discussion of risk-neutral pricing.

The Asian contract is written at time  $0$  and expires at  $T > t_0$ . The averaging begins at time  $0 \le t_0$  and occurs over the period  $[t_0, T]$ . (It is possible to have contracts where the averaging period finishes before maturity  $T$ , but this case is not covered here.) It is of interest to calculate the price of the option at the current time t, where  $0 \le t \le T$ . The position of t compared to the start of the averaging,  $t_0$ , may vary. If  $t \le t_0$ , the option is "forward starting". The special case  $t = t_0$  is called a *starting option* here. If  $t > t_0$ , the option is termed *in progress* as the averaging has begun.

We consider an Asian contract that is based on the value  $A_T^l$ , where we denote  $l = c$  for continuous averaging and  $l = d$  for discrete averaging. The continuous arithmetic average is given as

$$A_t^c = \frac{1}{t - t_0} \int_{t_0}^t S_u \, \mathrm{d}u, \quad t > t_0 \tag{2}$$

and by continuity, we define  $A_{t_0}^c = S_{t_0}$ . For the discrete arithmetic average, denote  $0 \le t_0 < t_1 < \dots <$  $t_n = T$ , and for current time  $t_m \le t < t_{m+1}$  (for integer  $0 \le m \le n$ ),

$$A_t^d = \frac{1}{m+1} \sum_{0 \le i \le m} S_{t_i} \tag{3}$$

The corresponding geometric average  $G_l^l; l = c, d$ is defined to be

$$G_t^c = \exp\left(\frac{1}{t - t_0} \int_{t_0}^t \ln S_u \, \mathrm{d}u\right) \tag{4}$$

for continuous averaging and

$$G_t^d = (S_{t_0}S_{t_1}...S_{t_m})^{1/(m+1)}$$
 (5)

for discrete averaging.

The payoff of an Asian call with arithmetic averaging is given as

$$(A_T^l - K)^+ \tag{6}$$

and the payoff of an Asian put with arithmetic averaging is given as

$$(K - A_T^l)^+ \tag{7}$$

where  $K$  is the fixed strike. Option payoffs depending on the geometric average are identical with  $A_T^l$ replaced by  $G_T^l$ .

By standard arbitrage arguments, the time- $t$  price of the Asian call is

$$e^{-r(T-t)}\mathbb{E}[(A_T^l - K)^{+}|\mathcal{F}_t] \tag{8}$$

and the price of the put is

$$e^{-r(T-t)}\mathbb{E}[(K-A_T^l)^+|\mathcal{F}_t] \tag{9}$$

It is worth noting that in pricing the Asian option, we need to consider only those cases where  $t \le t_0$ . For  $t > t_0$ , the option is in progress, and we can write  $e^{-r(T-t)}\mathbb{E}[(A_T-K)^+|\mathcal{F}_t]$  as

(documented in many papers including Levy [13]), so it is enough to consider the call option and derive the price of the put from this.

The main difficulty in pricing and hedging the Asian option is that the random variable  $A_T$  does not have a lognormal distribution. This makes the pricing very involved, and an explicit formula does not exist to date. This is an interesting mathematical problem and many research papers have been and still are written on the topic. The first of these was by Boyle and Emmanuel [3] in 1980.

Early methods for pricing the Asian option with arithmetic average involved replacing the arithmetic average  $A_T$  with the geometric average  $G_T$ , which is lognormally distributed; see [5, 10, 11, 15, 17]. This gives a simple formula, but it underprices the call significantly. However, it is worth noting that the formula leads to a scaling known as the  $1/\sqrt{3}$ *rule*, since for  $t > t_0$ , the volatility is scaled down by this factor. That is, the formula involves the term  $\sigma \frac{1}{\sqrt{2}}\sqrt{T-t}$ . This is a particularly useful observation if the averaging period is quite short relative to the life of the option. See [12], among others, for a description and more details.

The second class of methods used is to approximate the true distribution of the arithmetic average using an approximate distribution, usually lognormal with appropriate parameters. True moments for  $A_T$ are equated with those implied by a lognormal model, SO

$$\mathbb{E}A_T^n = \mathrm{e}^{n\alpha + 1/2n^2v^2} \tag{11}$$

for any integer n and  $\alpha$ , v are the mean and standard deviation of a normally distributed variable. This idea was used in a number of papers including

$$e^{-r(T-t)} \mathbb{E}_{t} \left[ \left( \frac{1}{T-t_{0}} \int_{t}^{T} S_{u} du + \frac{t-t_{0}}{T-t_{0}} A_{t} - K \right)^{+} \right]$$
  
$$= \frac{T-t}{T-t_{0}} e^{-r(T-t)} \mathbb{E}_{t} \left[ \left( \frac{1}{T-t} \int_{t}^{T} S_{u} du - \left( \frac{T-t_{0}}{T-t} K - \frac{t-t_{0}}{T-t} A_{t} \right) \right)^{+} \right]$$
(10)

where  $\mathbb{E}_t$  denotes the expectation conditional on information at time  $t$ . This is now the time  $t$  price of  $\frac{T-t}{T-t_0}$  times an Asian option with averaging beginning at time *t*, with modified strike  $\left(\frac{T-t_0}{T-t}K - \frac{t-t_0}{T-t}A_t\right)$ . The prices of Asian options also satisfy a put-call parity

[13]. Turnbull and Wakeman [19] also corrected for skew and kurtosis by expanding about the lognormal. The practical advantage of such approximations is their ease of implementation; however, typically these methods work well for some parameter values but not for others.

A further analytical technique in approximating the price of the Asian option is to establish price bounds. Curran [6] and Rogers and Shi [16] used conditioning to obtain a two-dimensional integral, which proves to be a tight lower bound for the option.

Much work has been done on pricing the Asian option using quasi-analytic methods. Geman and Yor [8] derived a closed-form solution for an "inthe-money" Asian call and a Laplace transform for "at-the-money" and "out-of-the-money" cases. Their methods are based on a relationship between geometric Brownian motion and time-changed Bessel processes. To price the option, one must invert the Laplace transform numerically; see [7]. Shaw [18] demonstrated that the inversion can be done quickly and efficiently for all reasonable parameter choices in Mathematica, making this a fast and effective approach. Linetsky [14] produced a quasi-analytic pricing formula using eigenfunction methods, with highly accurate results, also employing a package such as Mathematica.

Direct numerical methods such as Monte Carlo or quasi-Monte Carlo simulation and finite-difference partial differential equation (PDE) methods can be used to price the Asian option (*see* **Lattice Methods for Path-dependent Options**). In fact, given the popularity of such techniques, these methods were probably amongst the first used by practitioners (and remain popular today). Monte Carlo simulation was used to price Asian options by Broadie and Glasserman [4] and Kemna and Vorst [11], among many other more recent researchers. Simulation methods have the advantage of being widely used by practitioners to price derivatives, so no "new" method is required. Additional practical features such as stochastic volatility or interest rates can be incorporated without a significant increase in complexity. Control variates can often be used (e.g., using a geometric Asian option when pricing an arithmetic option). Additionally, simulation is often used as a benchmark price against which other methods are tested. The disadvantages are that it is computationally expensive, even when variance reduction techniques are used. Lapeyre and Temam [12] showed that Monte Carlo simulation can be competitive under the more advanced schemes they propose and with variance reduction techniques.

The Asian option is an exotic path-dependent option since the value at any point in time depends on the history of the underlying asset price. Specifically, the value of the option at *t* depends on the current level of the underlying asset *St* , time to expiry *T* − *t*, and the average level of the underlying up to *t*, *At* . Zvan *et al.* [21] presented numerical methods for solving this PDE. It turns out that the problem can be reduced to two variables (one state and the other time). Rogers and Shi [16], Alziary *et al.* [1], and Andreasen [2] formulated a one-dimensional PDE. The PDE approach is flexible in that it can handle market realities, but it is difficult to solve numerically as the diffusion term is very small for values of interest on the finite-difference grid. Vecer [20] reformulated the problem using analogies to passport options [9] to obtain an unconditionally stable PDE, which is more easily solved.

Methods based on discrete sampling become more appropriate when there are relatively few averaging dates. One simplistic approach is a scaling correction to volatility as described. Other possibilities include a Monte Carlo simulation or numerical solution of a sequence of PDEs [2]. Monte Carlo simulation can be quite efficient when there are only a small number of averaging dates, since the first "step" can take one straight to the averaging period (under the usual exponential Brownian motion model). Andreasen [2] priced discretely sampled Asian options using finitedifference schemes on a sequence of PDEs. This is particularly efficient if the averaging period is short and hence there are only a small number of PDEs to solve. He compared his PDE results to that of Monte Carlo simulation and showed that the finitedifference schemes get within a penny accuracy of the Monte Carlo simulation in less than a second of CPU time.

To conclude, there has been ongoing research into the methods for pricing the Asian option. It seems, however, the current-state-of-the-art pricing methods (good implementation of inversion of Laplace transform, eigenfunction and other expansions, stable PDE, and Monte Carlo simulation where appropriate) are fast, accurate, and adequate for most uses.

## **References**

[1] Alziary, B., Decamps, J.P. & Koehl, P.F. (1997). A PDE approach to Asian optons: analytical and numerical evidence, *Journal of Banking and Finance* **21**(5), 613–640.

- [2] Andreasen, J. (1998). The pricing of discretely sampled Asian and lookback options: a change of numeraire approach, *Journal of Computational Finance* **2**(1), 5–30.
- [3] Boyle, P. & Emanuel, D. (1980). *The Pricing of Options on the Generalized Mean*. Working paper, University of British Columbia.
- [4] Broadie, M. & Glasserman, P. (1996). Estimating security price derivatives using simulation, *Management Science* **42**, 269–285.
- [5] Conze, A. & Viswanathan, R. (1991). European path dependent options: the case of geometric averages, *Finance* **12**(1), 7–22.
- [6] Curran, M. (1992). Beyond average intelligence, *Risk* **5**, 60.
- [7] Fu, M., Madan, D. & Wang, T. (1999). Pricing continuous Asian options: a comparison of Monte Carlo and Laplace transform inversion methods, *Journal of Computational Finance* **2**(2), 49–74.
- [8] Geman, H. & Yor, M. (1993). Bessel processes, Asian options and perpetuities, *Mathematical Finance* **3**, 349–375.
- [9] Henderson, V. & Hobson, D. (2000). Local time, coupling and the passport option, *Finance and Stochastics* **4**(1), 69–80.
- [10] Jarrow, R.A. & Rudd, A. (1983). *Option Pricing*. Irwin, IL.
- [11] Kemna, A.G.Z. & Vorst, A.C.F. (1990). A pricing method for options based on average asset values, *Journal of Banking and Finance* **14**, 113–129.
- [12] Lapeyre, B. & Temam, E. (2000). Competitive Monte Carlo methods for the pricing of Asian options, *Journal of Computational Finance* **5**, 39–57.

- [13] Levy, E. (1992). Pricing European average rate currency options, *Journal of International Money and Finance* **11**(5), 474–491.
- [14] Linetsky, V. (2004). Spectral expansions for Asian (average price) options, *Operations Research* **52**(6), 856–867.
- [15] Ritchken, P., Sankarasubramanian, L. & Vijh, A.M. (1993). The valuation of path-dependent contracts on the average, *Management Science* **39**(10), 1202–1213.
- [16] Rogers, L.C.G. & Shi, Z. (1995). The value of an Asian option, *Journal of Applied Probability* **32**, 1077–1088.
- [17] Ruttiens, A. (1990). Classical replica, *Risk* February, 33–36.
- [18] Shaw, W. (2000). *A Reply to Pricing Continuous Asian Options by Fu, Madan and Wang*, Working paper.
- [19] Turnbull, S.M. & Wakeman, L.M. (1991). A quick algorithm for pricing European average options, *Journal of Financial and Quantitative Analysis* **26**(3), 377–389.
- [20] Vecer, J. (2001). A new PDE approach for pricing arithmetic average Asian options, *Journal of Computational Finance* **4**(4), 105–113.
- [21] Zvan, R., Forsyth, P. & Vetzal, K. (1998). Robust numerical methods for PDE models of Asian options, *Journal of Computational Finance* **2**, 39–78.

## **Related Articles**

**Average Strike Options**; **Black–Scholes Formula**; **Lattice Methods for Path-dependent Options**; **Risk-neutral Pricing**.

VICKY HENDERSON
## **Average Strike Options**

An average strike option is also known as an *Asian option* with floating strike. These options have a payoff based on the difference between the terminal asset price and the average of an underlying asset price over a specified time period. The other type of Asian option is the fixed-strike option, where the payoff is determined by the average of an underlying asset price and a fixed strike set in advance (*see* **Asian Options**).

If the average is computed using a finite sample of asset price observations taken at a set of regularly spaced time points, we have a discrete average strike option. A continuous time option is obtained by computing the average *via* the integral of the price path over an interval of time. The average itself can be defined to be geometric or arithmetic. As for the fixed strike Asian option, when the geometric average is used, the average strike option has a closedform solution for the price, whereas the option with arithmetic average does not have a known closedform solution.

We concentrate on the continuous time, average strike option of European style with arithmetic averaging. A discussion of the uses and rationale for introducing Asian contracts is given in **Asian Options**. Average strike options are closely related to these options, but are less commonly used in practice.

Consider the standard Black–Scholes economy with a risky asset (stock) and a money market account. We also assume the existence of a riskneutral probability measure *Q* (equivalent to the real-world measure *P*) under which discounted asset prices are martingales. We denote expectation under measure *Q* by *E*, and the stock price follows

$$\frac{\mathrm{d}S_t}{S_t} = (r - \delta) \,\mathrm{d}t + \sigma \,\mathrm{d}W_t \tag{1}$$

where *r* is the constant continuously compounded interest rate, *δ* is a continuous dividend yield, *σ* is the instantaneous volatility of asset return, and *W* is a *Q*-Brownian motion. The reader is referred to **Black–Scholes Formula** for details on the Black–Scholes model and **Risk-neutral Pricing** for a discussion of risk-neutral pricing.

We consider a contract that is based on the value *AT* , where *(At)t*<sup>≥</sup>*t*<sup>0</sup> is the arithmetic average

$$A_{t} = \frac{1}{t - t_{0}} \int_{t_{0}}^{t} S_{u} du, \quad t > t_{0}$$
 (2)

and by continuity, we define *At*<sup>0</sup> = *St*<sup>0</sup> . The corresponding geometric average *Gt* is defined as

$$G_t = \exp\left(\frac{1}{t - t_0} \int_{t_0}^t \ln S_u \, \mathrm{d}u\right) \tag{3}$$

The contract is written at time 0 (with 0 ≤ *t*0) and expires at *T >t*0. It is of interest to calculate the price of the option at the current time *t*, where 0 ≤ *t* ≤ *T* . The position of *t* compared to the start of the averaging, *t*<sup>0</sup> may vary, as described in **Asian Options**.

The payoff of an average strike call with arithmetic averaging is given as

$$(S_T - A_T)^+ \tag{4}$$

and the payoff of an average strike put with arithmetic averaging is

$$(A_T - S_T)^+ \tag{5}$$

Average strike option payoffs with geometric averaging are identical, with *AT* replaced by *GT* . The buyer of an average strike call is able to exchange the terminal asset price for the average of the asset price over a given period. For this reason, it is sometimes referred to as a *lookback* on the average (*see* **Lookback Options** for a discussion of the lookback option).

By standard arbitrage arguments, the time-*t* price of the average strike call is

$$e^{-r(T-t)}\mathbb{E}[(S_T - A_T)^{+}|\mathcal{F}_t] \tag{6}$$

and the price of the put is

$$e^{-r(T-t)}\mathbb{E}[(A_T - S_T)^{+}|\mathcal{F}_t] \tag{7}$$

It turns out that we need to consider only the case *t* ≥ *t*0, where the option is "in progress". The forward starting case (*t<t*0) can be rewritten as a modified option with averaging starting at *t*, today. This is in contrast to the Asian option with fixed strike, where the difficult case was when the option was forward starting. As for the Asian option, the average strike option satisfies a put–call parity; see [1] for details.

The average strike option is an exotic pathdependent option, as the price depends on the path of the underlying asset *via* the average. The distribution of the average *AT* is not lognormal, if the asset price is lognormal, and pricing is difficult because the joint law of *AT* and *ST* is needed. This is in contrast to the Asian option, which required only the law of the average. Perhaps because of this increased complexity, or their lesser popularity in practice, fewer methods exist for the pricing of average strike options. Just as for the Asian option, there are no closed-form solutions for the price of the average strike option.

Many of the methods that we discuss here for pricing are similar to those used to price the Asian option. An early technique to give an approximate price for the average strike option was to replace the arithmetic average *AT* with the geometric average *GT* . Since *GT* has a lognormal distribution, the (approximate) pricing problem becomes (for a call)

$$e^{-r(T-t)}\mathbb{E}[(S_T - G_T)^{+}|\mathcal{F}_t] \tag{8}$$

We recognize that this is exactly an exchange option (*see* **Exchange Options**), which can be priced *via* a change of measure, as in [9]. Levy and Turnbull [8] mentioned this connection to exchange options, but it was Conze and Viswanathan [3] who presented the results of this computation.

Other analytical approximations can be obtained by approximating the true joint distribution of the arithmetic average and asset price using an approximate distribution, usually jointly lognormal with appropriate parameters. Chung *et al.* [2] extended the linear approximations of Bouaziz *et al.* [1], Levy [7], and Ritchken *et al.* [10] (approximating distribution of {*AT , ST* } by joint lognormal) to include quadratic terms. Their approximation is no longer based on a geometric-type approximation.

Recently, symmetries of a similar style to that of the put-call symmetry have been found between fixed strike Asian options and average strike options. For forward starting average strike options, Henderson *et al.* [4] gave a symmetry with a starting Asian option. If the average strike option is starting, the special case of Henderson and Wojakowski [5] is recovered. If the average strike option is in progress, it cannot be rewritten as an Asian option, and Henderson *et al.* [4] derived an upper bound for the price of the average strike option. This bound is in terms of an Asian option with fixed strike and a vanilla option. The method gives an "exact" bound for forward starting and starting options and when expiry is reached.

Numerical methods can be used to price the average strike option. The discussion of Monte Carlo simulation in **Asian Options** is also relevant here, as simulation is often used as a benchmark price. Ingersoll [6] was the first to recognize that it is possible to reduce the dimension of the pricing problem for the average strike option using a transformation of variables. Despite the value of the average strike option at *t* depending on the current asset price, current value of the average, and time to expiry, a one-dimensional partial differential equation (PDE) can be derived by using Ingersoll's reduction of variables. However, the drawback is that the Dirac delta function appears as a coefficient of the PDE, making it prone to instabilities. Vecer's [12] PDE method for Asian options with fixed strike also applies to average strike options and gives a stable one-dimensional PDE. Some testing of this method for the average strike option is given in [11].

To conclude, research into pricing the average strike option is ongoing, with current PDE and bound methods being very efficient.

## **References**

- [1] Bouaziz, L., Briys, E. & Crouhy, M. (1994). The pricing of forward starting asian options, *Journal of Banking and Finance* **18**(5), 823–839.
- [2] Chung, S., Shackleton, M. & Wojakowski, R. (2003). Efficient quadratic approximation of floating strike Asian option values, *Finance* **24**(1), 49–62.
- [3] Conze, A. & Viswanathan, R. (1991). European path dependent options: the case of geometric averages, *Finance* **12**(1), 7–22.
- [4] Henderson, V., Hobson, D., Shaw, W. & Wojakowski, R. (2007). Bounds for in-progress floating-strike Asian options using symmetry, *Annals of Operations Research* **151**, 81–98.
- [5] Henderson, V. & Wojakowski, R. (2002). On the equivalence of fixed and floating-strike Asian options, *Journal of Applied Probability* **39**(2), 391–394.
- [6] Ingersoll, J. (1987). *Theory of Financial Decision Making*, Rowman and Littlefield Publishers, New Jersey.

- [7] Levy, E. (1992). Pricing European average rate currency options, *Journal of International Money and Finance* **11**(5), 474–491.
- [8] Levy, E. & Turnbull, S. (1992). Average intelligence, *Risk* **5**, 2.
- [9] Margrabe, W. (1978). The value of an option to exchange one asset for another, *Journal of Finance* **33**, 177–186.
- [10] Ritchken, P., Sankarasubramanian, L. & Vijh, A.M. (1993). The valuation of path-dependent contracts on the average, *Management Science* **39**(10), 1202–1213.
- [11] Shiuan, Y.J. (2001). *Pricing Floating-Strike Asian Options*. MSc dissertation, University of Warwick.

[12] Vecer, J. (2001). A new pde approach for pricing arithmetic average Asian options, *Journal of Computational Finance* **4**(4), 105–113.

## **Related Articles**

**Asian Options**; **Black–Scholes Formula**; **Exchange Options**; **Lookback Options**; **Risk-neutral Pricing**.

VICKY HENDERSON
# **Variance Swap**

# **Definition**

A variance swap is a volatility derivative that pays off on realized volatility of some underlying:

$$Payoff = (\sigma_R^2 - K_{\text{var}}) \times N \tag{1}$$

where *σ*<sup>R</sup> <sup>2</sup> is the realized variance, *K*var is the fair value of the realized variance at inception, and *N* is the notional amount, a leverage factor. The realized variance may be defined differently in different markets depending not only on the "default model" but also on specific contract specifications. One standard way for stocks [9] is to define realized variance as

$$\sigma_{\mathsf{R}}^{2} = \frac{252}{n} \sum_{i=1}^{n} u_{i}^{2}, \quad u_{i} = \ln \left( S_{i} \big/ S_{i-1} \right) \tag{2}$$

This requires *n* + 1 observations of the daily closing stock price *Si*. The factor 252 is the approximate number of business days in a year, which gives an annualized variance. Also note that this formula assumes the mean of the returns to be zero. This means that it is distinct from the statistical variance of the returns. The mean of returns is typically small and setting it to zero makes returns on variance swaps additive over time. Using log returns to measure variance makes this formula compatible with the standard Black–Scholes option pricing formula.

The long position in a variance swap receives *N* dollars for every point by which the stock's realized variance *σ*<sup>R</sup> <sup>2</sup> has exceeded the inception fair value *K*var. See [6] for one of the earliest, but most comprehensive, references on variance swaps. In this reference, the authors discuss replication problems due to strike spacing and gapping of the underlying, for example.

It is market practice to define the variance notional in volatility terms:

$$\text{Variance Notional} = \frac{\text{VegaNotional}}{2 \times \sigma_{\text{strike}}} \tag{3}$$

where the strike volatility *σ*strike is equal to the square root of the strike variance *K*var. With this adjustment, if the realized volatility is 1 percentage point above *σ*strike at maturity, the payoff is approximately equal to the vega notional.

Uses of variance swaps include trading the level of volatility (variance swaps are a more pure way to do this compared to straddles), trading the realized/ implied vol spread, hedging of volatility exposures, or trading volatility on a forward basis via forward variance swaps. See [1] for more details about variance swaps, market practices, and their use in vol spread trading and correlation trading.

# **Fair Value and Skew**

In [6], it is shown that a variance swap can be statically replicated with calls, puts, and a forward contract. The payoff for the variance swap then comes from delta hedging of this portfolio of options with the underlying. The fair value is determined by the cost of the replicating portfolio of options. The payoff in terms of realized volatility is achieved by delta hedging with the underlying. If the realized vol is exactly equal to the expected vol at inception, the hedging profits will be exactly equal to the cost of the option portfolio and the payout will be zero. As the portfolio of options (in theory) includes option of every strike, the fair value cost is affected significantly by the skew. The skew is defined to be the way the implied volatility changes as the strike changes, all else being equal.

The fair value can be derived using the volatility formula discussed in [4]. In this reference, the authors show the remarkable formula that the expected value of any smooth payoff function *f (ST )* in terms of the terminal stock price *ST* can be written in terms of stock and option prices.

$$E_t[f(S_T)] = f(\kappa)B_0 + f'(\kappa)[C_t(\kappa) - P_t(\kappa)]$$
$$+ \int_{-\infty}^{\kappa} f''(s)P_t(s)ds$$
$$+ \int_{\kappa}^{\infty} f''(s)C_t(s)ds \tag{4}$$

An application of Ito's lemma to the usual Black diffusion yields the variance differential:

$$2\left[\frac{\mathrm{d}S_t}{S_t} - \mathrm{d}(\log S_t)\right] = \sigma^2 \mathrm{d}t \tag{5}$$

Applying equation (4) to the log contract [11] in equation (5) shows that the replicating portfolio consists of out-of-the-money calls and puts of all strikes K, where each option has the weight  $1/K^2$ plus a dynamic delta hedge using a forward contract on the stock. The fair value of the variance strike is

$$K_{\text{var}} = \frac{2}{T} \left[ rT - \left( \frac{S_0}{S_*} e^{rT} - 1 \right) - \log \frac{S_*}{S_0} \right. \\ + \left. e^{rT} \int_0^{S_*} \frac{1}{K^2} P(K) \mathrm{d}K \right. \\ + \left. e^{rT} \int_{S_*}^{\infty} \frac{1}{K^2} C(K) \mathrm{d}K \right] \tag{6}$$

Here,  $C(K)$  and  $P(K)$  are the prices of the call and put, respectively, with strike  $K$ .

In [6], we find the following formulas for fair value in terms of simple skew models. For the skew that is linear in the strike,

$$\sigma(K) = \sigma_{\text{ATM}} - b \frac{K - S_F}{S_F} \tag{7}$$

the fair value is

$$K_{\text{var}} = \sigma_{\text{ATM}}^2 (1 + 3Tb^2 + \cdots) \tag{8}$$

For the skew that is linear in the delta (here  $\Delta_p$ is the put delta),

$$\sigma(\Delta_p) = \sigma_{\text{ATM}} + b\left(\Delta_p + \frac{1}{2}\right) \tag{9}$$

the fair value is

$$K_{\text{var}} = \sigma_{\text{ATM}}^2 \left( 1 + \frac{1}{\sqrt{\pi}} b \sqrt{T} + \frac{1}{12} \frac{b^2}{\sigma_{\text{ATM}}^2} + \cdots \right) \tag{10}$$

In [7], we have a particularly elegant formula for the fair value given directly in terms of the skew. Denote

$$z(k) = d_2 = -\frac{k}{\sigma_{\text{BS}}(k)\sqrt{T}} + \frac{\sigma_{\text{BS}}(k)\sqrt{T}}{2} \qquad (11)$$

Intuitively,  $z$  measures the log-moneyness of an option in implied standard deviations. Then

$$K_{\text{var}} = \int_{-\infty}^{\infty} dz \cdot N'(z) \sigma_{\text{BS}}^{2}(z) T \qquad (12)$$

# Market Risk

In [5], the authors derive general results on market risk for variance swaps. Because variance is additive, a variance swap partway through its life is valued partly by realized vol (already observed) and partly by unrealized/implied vol, which is yet to be observed.

$$V(t_0, T)(T - t_0) = \underbrace{V(t_0, t)}_{\text{Realized}} (t - t_0) + \underbrace{V(t, T)}_{\text{Unrealized}} (T - t) \quad (13)$$

It follows from this that at time  $t$  a variance swap with notional  $N$  has value

$$M(t) = N e^{-rT} [\lambda (V(t_0, t) - K_0)$$
  
+  $(1 - \lambda)(K_t - K_0)],$   
 $\lambda = (t - t_0)/(T - t_0)$  (14)

The first piece is just the time-weighted value of realized variance against the strike. The second piece is the time-weighted difference of fair value variance strikes. The same formula can be used to decompose the daily price change into three risk components: gamma, vega, and theta:

$$\Delta M(t) = M(t + \Delta t) - M(t)$$

$$= N \left( \underbrace{\frac{1}{\tau} V(t, t + \Delta t) \Delta t}_{\text{Gamma}} + \underbrace{(1 - \lambda_{t + \Delta t}) \cdot \Delta K}_{\text{Vega}} - \underbrace{\frac{1}{\tau} K_t \Delta t}_{\text{Theta}} \right) \qquad (15)$$

The biggest independent risk is in the fair value of the strike, which we have put in the vega component. This component also entails the skew risk.

#### **Volatility Swaps**

Although variance swaps can be statically replicated, volatility swaps (see Volatility Swaps) cannot. In [3], the authors show that there is an approximate dynamic replicating strategy for volatility swaps. Before this, volatility swap valuation had been thought to be highly model dependent [2]. See also [8, 10], where the authors give a closed formula for valuing vol swaps using a GARCH model.

# **References**

- [1] Bossu, S., Strasser, E. & Guichard, R. (2005). *Just What You Need to Know About Variance Swaps*, JP Morgan Equity Derivatives Research Publication.
- [2] Brockhaus, O. & Long, D. (2000). *Volatility Swaps Made Simple*, RISK Magazine, pp. 92–95.
- [3] Carr, P. & Lee, R. (2008). Robust replication of volatility derivatives, *Mathematics in Finance* Working Paper #2008-3. Courant Institute of Mathematical Sciences.
- [4] Carr, P. & Madan, D. (1998). Towards a theory of volatility trading, in *Volatility* ed., R.A. Jarrow, Risk Books.
- [5] Chriss, N. & Morokoff, W. (1999). *Market Risk for Volatility and Variance Swaps*, Risk Magazine.
- [6] Demeterfi, K., Derman, E., Kamal, M. & Zou, J. (1999). A guide to volatility and variance swaps, *Journal of Derivatives* **6**, 9–32.

- [7] Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*, Wiley Finance.
- [8] Haug, E.G. (2007). *Option Pricing Formulas*, 2nd Edition, McGraw Hill.
- [9] Hull, J. (2003). *Options, Futures, and other Derivatives*, 5th Edition, Prentice Hall.
- [10] Javaheri, A., Wilmott, P. & Haug, E.G. (2002). *Garch and Volatility Swaps*, published on Wilmott.com.
- [11] Neuberger, A. (1994). The log contract, *The Journal of Portfolio Management* **20**, 74–80.

# **Related Articles**

**Correlation Swap**; **Corridor Variance Swap**; **Gamma Swap**; **Realized Volatility and Multipower Variation**; **Realized Volatility Options**; **Volatility**; **Volatility Index Options**; **Volatility Swaps**; **Weighted Variance Swap**.

ERIC LIVERANCE
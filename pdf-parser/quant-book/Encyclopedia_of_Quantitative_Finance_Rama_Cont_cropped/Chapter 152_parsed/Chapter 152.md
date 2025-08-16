# **Hull-White Stochastic Volatility Model**

Even before practitioners started using the Black-Scholes formula extensively, one had identified the assumption of constant volatility as unrealistic. Empirical observation of equity vanilla option market shows, indeed, that the implied volatility level depends on the strike. This feature, commonly known as the volatility smile, violates the constant volatility assumption. This essential remark motivated the birth of stochastic volatility models (see Stochastic Volatility Models).

Among the first authors to tackle this issue, Hull and White proposed in 1987 a simple extension of Black-Scholes model [1]. This article aims at presenting a sound introduction to the Hull-White stochastic volatility model and at indicating its implications in terms of volatility behavior and correlation.

Hull and White describe the variance  $V = \sigma^2$  as a geometric Brownian motion. Therefore, the asset and variance satisfy the following stochastic differential equation:

$$dS = \phi S dt + \sigma S dw_t \tag{1}$$

$$dV = \mu V dt + \xi V dz_t \tag{2}$$

$$\mathrm{d}w_t,\ \mathrm{d}z_t = \rho\ \mathrm{d}t\tag{3}$$

In its general formulation, the parameter  $\phi$  may depend on S,  $\sigma$ , and t, while parameters  $\mu$  and  $\xi$  may depend on  $\sigma$  and t. One may find that many models fall under these dynamics, including the Heston **model** for  $\mu = \kappa \left(\theta/V - 1\right)$  and  $\xi = \left(\nu/\sqrt{V}\right)$ . As in [1], we will restrict to the constant parameters case (Hull and White studied the mean-reverting variance case in [2]).

# **Option Pricing**

Let  $f$  be the price of a security which depends on the stock price.  $f$  satisfies the **partial differential**  $equation (PDE)$ 

$$\frac{\partial f}{\partial t} + \frac{1}{2} \left[ \sigma^2 S^2 \frac{\partial^2 f}{\partial S^2} + 2\rho \sigma^3 \xi S \frac{\partial^2 f}{\partial S \partial V} + \xi^2 V^2 \frac{\partial^2 f}{\partial V^2} \right]$$

$$-rf = -rS\frac{\partial f}{\partial S} - \mu\sigma^2 \frac{\partial f}{\partial V} \tag{4}$$

Assuming volatility and stock price are uncorrelated, we derive an analytic solution to equation  $(4)$ through risk-neutral valuation procedure

$$f(S_t, \sigma_t^2, t) = e^{-r(T-t)}$$
$$\times \int_0^\infty f(S_T, \sigma_T^2, T) p(S_T | S_t, \sigma_t^2) \, dS_t \tag{5}$$

where T is the option maturity,  $S_t$  is the security at pricing time t,  $\sigma_t$  is the instantaneous volatility at time t, and  $p(S_T|S_t, \sigma_t^2)$  is the conditional distribution of  $S_T$  given the security price and variance at time t.

Introducing the mean variance over the option life  $\bar{V}$ .

$$\bar{V} = \frac{1}{T - t} \int_{t}^{T} \sigma_{\tau}^{2} \, \mathrm{d}\tau \tag{6}$$

we express the call option value as

$$C_{\rm HW}(S_t,\sigma_t^2,t) = \int_0^\infty C_{\rm BS}(\bar{V})h(\bar{V}|\sigma_t^2)\mathrm{d}\bar{V} \qquad (7)$$

where  $C_{\rm BS}$  is the Black-Scholes call option value and  $h(\cdot, \sigma_t^2)$  is the conditional density of  $\bar{V}$  given  $\sigma_t^2$ .

In some particular cases, such as when  $\mu$  and  $\sigma$ are constant, this expression admits an explicit Taylor expansion which converges quickly for small values of  $\xi^2(T - t)$ .

#### **Behavior of Volatility**

Assuming that parameters  $\mu$  and  $\xi$  are constant, the first two moments of the volatility process are given by

$$E[\sigma(t)] = \sigma(0) \times e^{\frac{1}{2} \left(\mu - \frac{1}{4}\xi^2\right)t} \tag{8}$$

$$V[\sigma(t)] = \sigma(0)^2 \times e^{\mu t} \left(1 - e^{\frac{1}{8}\xi^2 t}\right) \qquad (9)$$

For  $\mu < \frac{1}{4}\xi^2$ , the expectation of volatility converges to zero, whereas for  $\mu > \frac{1}{4}\xi^2$ , it diverges.<br>Regarding the variance of volatility, it increases unbounded if  $\mu > 0$ .

![](_page_1_Figure_1.jpeg)

**Figure 1** Implied volatility as a function of strike

When calibrating the model to the market, we are very likely to find *µ* ≤ 0, since variance of volatility is bounded. Hence, the expectation of volatility converges to either zero or its initial value.

#### *Implied Volatility Smile*

In Figure 1, we show implied volatility as a function of moneyness (strike divided by forward). The call option price has been computed using the Taylor expansion of equation (7) with *σ*<sup>0</sup> = 0*.*15, *µ* = 0, *ξ* = 0, and *r* = 0. Compared to the Hull–White model, the Black–Scholes model overprices at-themoney options and underprices in- and out-of-themoney options.

# **Correlation between Stock Returns and Changes in Volatility**

By introducing correlation between stock and variance Gaussian increments, Hull and White incorporate explicitly a cause of the volatility skew: the leverage effect. Even if they do not provide any analytic formula in the correlated case, one can still analyze the impact of correlation through numerical simulation.

As shown in Figure 2, this correlation has a huge impact since it enables to transform the smile into

![](_page_1_Figure_9.jpeg)

**Figure 2** Volatility smile for various correlation levels

a skew. In order to fit market data, it is crucial to correctly set the correlation parameter.

One drawback of the Hull–White model is the lack of mean-reverting behavior in the volatility process (*see* **Stochastic Volatility Models**).

## **References**

- [1] Hull, J. & White, A. (1987). The pricing of options on assets with stochastic volatilities, *The Journal of Finance* **17**(2), 281–300.
- [2] Hull, J & White, A. (1988). An analysis of the bias in option pricing caused by a stochastic volatility, *Advances in Futures and Options Research* **3**, 27–61.

## **Related Articles**

**Heavy Tails**; **Heston Model**; **Implied Volatility in Stochastic Volatility Models**; **Implied Volatility Surface**; **Partial Differential Equations**; **Stochastic Volatility Models**; **Stylized Properties of Asset Returns**.

> PIERRE GAUTHIER & PIERRE-YVES H. RIVAILLE
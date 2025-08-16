## **Lognormal Mixture Diffusion Model**

Let us denote the time- $t$  price of a given financial asset by  $S(t)$ , equivalently  $S_t$ . We say that S evolves according to a local-volatility model (see also **Local Volatility Model**) if, under the risk-neutral measure,

$$dS(t) = \mu S(t)dt + \sigma(t, S(t))S(t)dW(t),$$
  

$$S(0) = S_0$$
(1)

where  $S_0$  is a positive constant, W is a standard Brownian motion,  $\sigma$  is a well-behaved deterministic function, and  $\mu$  is the risk-neutral drift rate, which is assumed to be constant. For instance, in case of a stock paying a continuous dividend yield q,  $\mu =$  $r - q$ , where r is the (assumed constant) continuously compounded risk-free rate.

Brigo and Mercurio  $[1-3]$  find an explicit expression for the function  $\sigma$  such that the resulting process has a density that, at each time, is given by a mixture of lognormal densities. Their result is briefly reviewed in the following.

Let us consider N functions  $\sigma_i$ 's that are deterministic and bounded from above and below by positive constants, and corresponding lognormal densities

$$p_t^i(y) = \frac{1}{yV_i(t)\sqrt{2\pi}} \times \exp\left\{-\frac{1}{2V_i^2(t)} \left[ \ln \frac{y}{S_0} - \mu t + \frac{1}{2}V_i^2(t) \right]^2 \right\}$$
(2)

$$V_i(t) := \sqrt{\int_0^t \sigma_i^2(u) \mathrm{d}u} \tag{3}$$

**Proposition 1** Let us assume that each  $\sigma_i$  is also continuous and that there exists an  $\varepsilon > 0$  such that  $\sigma_i(t) = \sigma_0 > 0$ , for each t in [0,  $\varepsilon$ ] and  $i = 1, \ldots, N$ . Then, if we set

for  $(t, y) > (0, 0)$  and  $v(t, y) = \sigma_0$  for  $(t, y) =$  $(0, S_0)$ , the SDE

$$dS_t = \mu S_t dt + \nu(t, S_t) S_t dW_t \tag{5}$$

has a unique strong solution whose marginal density is given by the mixture of lognormals

$$p_t(y) = \sum_{i=1}^{N} \lambda_i \frac{1}{yV_i(t)\sqrt{2\pi}}$$
$$\times \exp\left\{-\frac{1}{2V_i^2(t)} \left[ \ln \frac{y}{S_0} - \mu t + \frac{1}{2}V_i^2(t) \right]^2 \right\}$$
(6)

*Moreover, for*  $(t, y) > (0, 0)$ *, we can write*  $v^2(t, y)$  $= \sum_{i=1}^{N} \Lambda_{i}(t, y)\sigma_{i}^{2}(t), \text{ where, for each } (t, y) \text{ and}$ <br> $i, \ \Lambda_{i}(t, y) \ge 0 \text{ and } \sum_{i=1}^{N} \Lambda_{i}(t, y) = 1. \text{ As a conse-}$ quence, for each  $t, y > 0$ ,

$$0 < \tilde{\sigma} := \inf_{t \ge 0} \left\{ \min_{i=1,\dots,N} \sigma_i(t) \right\} \le \nu(t,y) \le \hat{\sigma}$$
$$:= \sup_{t \ge 0} \left\{ \max_{i=1,\dots,N} \sigma_i(t) \right\} < +\infty \tag{7}$$

A proof of this proposition can be found in [2], and more formally in  $[5]$ .

The pricing of European options under the lognormal-mixture local-volatility model is quite straightforward (see also Risk-neutral Pricing; Black-Scholes Formula).

**Proposition 2** Consider a European option with maturity  $T$ , strike  $K$ , and written on the asset. The option value at the initial time  $t = 0$  is given by the following convex combination of Black–Scholes prices:

$$v(t, y) = \sqrt{\frac{\sum_{i=1}^{N} \lambda_{i} \sigma_{i}^{2}(t) \frac{1}{V_{i}(t)} \exp\left\{-\frac{1}{2V_{i}^{2}(t)} \left[\ln\frac{y}{S_{0}} - \mu t + \frac{1}{2}V_{i}^{2}(t)\right]^{2}\right\}}{\sum_{i=1}^{N} \lambda_{i} \frac{1}{V_{i}(t)} \exp\left\{-\frac{1}{2V_{i}^{2}(t)} \left[\ln\frac{y}{S_{0}} - \mu t + \frac{1}{2}V_{i}^{2}(t)\right]^{2}\right\}}$$
(4)

$$\pi(K,T) = \omega P(0,T) \sum_{i=1}^{N} \lambda_i$$
$$\times \left[ S_0 e^{\mu T} \Phi \left( \omega \frac{\ln \frac{S_0}{K} + \left(\mu + \frac{1}{2}\eta_i^2\right) T}{\eta_i \sqrt{T}} \right) - K \Phi \left( \omega \frac{\ln \frac{S_0}{K} + \left(\mu - \frac{1}{2}\eta_i^2\right) T}{\eta_i \sqrt{T}} \right) \right] \tag{8}$$

where  $P(0, T)$  is the discount factor for maturity  $T$ ,  $\Phi$ is the normal cumulative distribution function,  $\omega = 1$ *for a call and*  $\omega = -1$  *for a put, and* 

$$\eta_i := \frac{V_i(T)}{\sqrt{T}} = \sqrt{\frac{\int_0^T \sigma_i^2(t) \mathrm{d}t}{T}} \tag{9}$$

The main advantage of the lognormal-mixture local-volatility model is its tractability (explicit marginal density and option prices). This model can be successfully used in practice to calibrate smile-shaped implied volatility structures. Extensions allowing for nonzero slopes at the at-the-money level are introduced in  $[4]$ .

## References

- [1] Brigo, D. & Mercurio, F. (2000). A mixed-up smile, *Risk* September, 123-126.
- Brigo, D. & Mercurio, F. (2001). Displaced and mix-[2] ture diffusions for analytically-tractable smile models, in Mathematical Finance-Bachelier Congress 2000, H. Geman, D.B. Madan, S.R. Pliska & A.C.F. Vorst, eds, Springer Finance, Springer, Berlin, Heidelberg, New York.
- [3] Brigo, D. & Mercurio, F. (2002). Lognormal-mixture dynamics and calibration to market volatility smiles, International Journal of Theoretical and Applied Finance 5(4), 427-446.
- [4] Brigo, D., Mercurio, F. & Sartorelli, G. (2003). Alternative asset-price dynamics and volatility smile, Quantitative Finance 3(3), 173-183.
- [5] Sartorelli, G. (2004). Density Mixture Ito Processes. PhD thesis, Scuola Normale Superiore di Pisa.

FABIO MERCURIO
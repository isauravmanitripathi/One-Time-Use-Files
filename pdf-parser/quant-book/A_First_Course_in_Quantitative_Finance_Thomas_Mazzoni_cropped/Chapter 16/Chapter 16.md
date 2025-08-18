Stochastic volatility is the door to incomplete market architectures. In such a framework, the fair price of a derivative can no longer be determined uniquely by hedging arguments or switching to a unique equivalent martingale measure. The more realistic properties of stochastic volatility models come at a price. The volatility risk premium has to be determined by calibration, and more sophisticated tools like characteristic functions and the generalized *Fourier*-transform are required.

#### 16.1 The Consequence of Stochastic Volatility

One of the most obvious problems with volatility is that we cannot really specify what it is on a fundamental level. Is it the square root of the average quadratic deviation from the mean? Or is it the magnitude of the range in which say 95% of the logarithmic returns are observed? On the other hand we can clearly say what it is not. It is not a traded security, and hence the generic name incomplete market models, even though this class is much broader. Despite those fundamental concerns, we can take a technical perspective and ask: How can our stochastic model for the price process of the underlying be extended to allow for randomly changing volatility? The answer is by introducing another stochastic process, linked to our original model. A fairly general formulation of such a joint process is

$$dS_t = \mu S_t dt + \sigma_t S_t dW_{1,t} \tag{16.1}$$

$$d\sigma_t = f(S_t, \sigma_t, t)dt + g(S_t, \sigma_t, t)dW_{2,t}, \qquad (16.2)$$

where  $f(S, \sigma, t)$  and  $g(S, \sigma, t)$  are sufficiently smooth functions, not specified yet, and the covariance between the *Wiener*-processes is  $\text{Cov}[dW_1, dW_2] = E[dW_1 dW_2] = \rho dt$ . Thinking in terms of partial differential equations, any derivative contract is now a function of two spatial variables,  $V(S, \sigma, t)$ , and Itô's lemma yields the differential

$$dV = \frac{\partial V}{\partial S}dS + \frac{\partial V}{\partial \sigma}d\sigma + \frac{\partial V}{\partial t}dt + \frac{1}{2} \left(\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + 2\rho\sigma Sg \frac{\partial^2 V}{\partial S \partial \sigma} + g^2 \frac{\partial^2 V}{\partial \sigma^2}\right)dt,\tag{16.3}$$

where the arguments of the function  $g(S, \sigma, t)$  were omitted for brevity. The only new element in the  $It\hat{o}$ -Taylor-expansion is the covariance term, resulting from the fact that

Varl $dW_1 dW_2$  is of order  $dt^2$ . Hence, we can add the heuristic rule  $dW_1 dW_2 = \rho dt$  to our informal list for applying Itô's lemma.

If we try to set up a hedge-portfolio, we immediately run into trouble. Because we have two sources of randomness, it is not sufficient to only hedge with the underlying. We need at least one auxiliary contract, contingent on the same underlying, to establish the required portfolio. Assume for the moment that such an auxiliary contract exists and call it  $V_a(S, \sigma, t)$ . Then our hedge-portfolio has the form

$$\Pi = V - \Delta_1 S - \Delta_2 V_a. \n$$
(16.4)

We have now to follow the usual routine, which means applying Itô's lemma, choosing the hedge-ratios for  $\Delta_1$  and  $\Delta_2$  properly to eliminate the risk, and equating the resulting differential to the risk-free growth rate of  $\Pi$ . This is a very messy but straightforward computation and the details can be found in Wilmott (2006c, sect. 51.4). The result is that we end up with the equation

$$\frac{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}V}{\partial S^{2}} + \rho\sigma Sg\frac{\partial^{2}V}{\partial S\partial\sigma} + \frac{1}{2}g^{2}\frac{\partial^{2}V}{\partial\sigma^{2}} - rV}{\frac{\frac{\partial V}{\partial\sigma}}{\frac{\partial V}{\partial\sigma}}}\n$$

$$\n= \frac{\frac{\partial V_{a}}{\partial t} + rS\frac{\partial V_{a}}{\partial S} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}V_{a}}{\partial S^{2}} + \rho\sigma Sg\frac{\partial^{2}V_{a}}{\partial S\partial\sigma} + \frac{1}{2}g^{2}\frac{\partial^{2}V_{a}}{\partial\sigma^{2}} - rV_{a}}{\frac{\partial V_{a}}{\partial\sigma}}.\n$$
(16.5)

This looks horrible, but the good news is that the left hand side is only a function of V and the right hand side exclusively depends on  $V_a$ . Because both contracts have different nonlinear payoffs, we can conclude that each side of the equation separately has to be equal to an unknown function  $h(S, \sigma, t)$ . For reasons that become clear shortly, it is more convenient to reexpress this function in terms of a linear combination of f, g, and another unknown function  $\lambda$ ,  $h = \lambda g - f$ . We then finally obtain the Merton-Garman-equation

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + (f - \lambda g)\frac{\partial V}{\partial \sigma} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \rho \sigma Sg \frac{\partial^2 V}{\partial S \partial \sigma} + \frac{1}{2}g^2 \frac{\partial^2 V}{\partial \sigma^2} - rV = 0. \tag{16.6}$$

The unknown function  $\lambda(S,\sigma,t)$  is called the market price of volatility risk. What does that mean exactly? Suppose, we indeed build a hedge-portfolio, based only on a position in the option and a short position in the underlying

$$\Pi = V - \Delta S. \n$$
(16.7)

Applying Itô's lemma, we would obtain

$$d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \rho \sigma S g \frac{\partial^2 V}{\partial S \partial \sigma} + \frac{1}{2}g^2 \frac{\partial^2 V}{\partial \sigma^2}\right) dt + \left(\frac{\partial V}{\partial S} - \Delta\right) dS + \frac{\partial V}{\partial \sigma} d\sigma.$$
 (16.8)

We can hedge the market risk away by choosing  $\Delta = \frac{\partial V}{\partial S}$ , but the volatility risk remains. Computing the difference between the stochastic differential of the portfolio and the

| Model                  | Variable  | Drift f                  | Diffusion g   |  |
|------------------------|-----------|--------------------------|---------------|--|
| Hull and White (1987)  | 2<br>v =σ | f(v) = θv                | g(v) = αv     |  |
| Scott (1987)           | y = logσ  | −<br>f(y) = κ(θ<br>y)    | g = α         |  |
| Stein and Stein (1991) | σ         | −<br>f(σ)<br>= κ(θ<br>σ) | g = α<br>√    |  |
| Heston (1993)          | 2<br>v =σ | −<br>f(v) = κ(θ<br>v)    | g(v) = α<br>v |  |
| Hagan et al. (2002)    | σ         | f = 0                    | g(σ)<br>= ασ  |  |

**Table 16.1** Popular stochastic volatility models

risk-free growth rate yields

$$d\Pi - r\Pi dt = \left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + f\frac{\partial V}{\partial \sigma} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \rho\sigma Sg\frac{\partial^2 V}{\partial S\partial \sigma} + \frac{1}{2}g^2\frac{\partial^2 V}{\partial \sigma^2} - rV\right)dt + g\frac{\partial V}{\partial \sigma}dW_2$$
  
$$= g\frac{\partial V}{\partial \sigma}(\lambda dt + dW_2),$$
  
(16.9)

where we used (16.2) and (16.6). The presence of one unit of volatility risk *dW*<sup>2</sup> is compensated by an extra return λ*dt*, hence the name market price of volatility risk.

Of course a model in its full generality is not tractable. Thus, the functions *f* and *g* have to be specified in a reasonable way, to obtain a suitable model for derivative pricing. It is also possible to model the dynamics of the variance or another nonnegative quantity, instead of volatility. Table 16.1 reviews a small collection of popular stochastic volatility models. Probably the most prominent one is the *Heston*-model, which we will analyze in great detail shortly.

#### • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • **16.2 Characteristic Functions and the Generalized Fourier-Transform**

We have already learned that characteristic functions are very useful when adding independent random variables. In order to proceed, it is helpful to develop a deeper understanding of the concept of characteristic functions. From the definition

$$\varphi(u) = E[e^{iuX}] = \int_{-\infty}^{\infty} e^{iux} f(x) dx, \qquad (16.10)$$

we can see that there is a one-to-one correspondence between the characteristic function and the probability density function of an arbitrary random variable *X*, provided that the density exists. The integral on the right hand side of (16.10) is also the *Fourier*transform of the probability density *f*(*x*), as mentioned earlier. Let's now open another door, by applying the *Euler*-identity<sup>1</sup>

$$e^{iuX} = \cos(uX) + i\sin(uX). \tag{16.11}$$

<sup>1</sup> In case you are not familiar with complex analysis, a brief introduction is provided in Appendix A.

![](_page_3_Figure_1.jpeg)

**Fig. 16.1** 3D Characteristic function φ*X*(*u*) of *X* ∼ *N*(0, 1) and distribution of *uX*, wrapped around the complex unit circle for different *u*

For any given *u*, the random variable *X* is mapped onto the complex unit circle. This fact was used by Epps (1993) to give the characteristic function a geometric meaning. We can see clearly from (16.11) that the distribution of the scaled random variable *uX* is wrapped around the perimeter of the complex unit circle, and hence the characteristic function is the center of mass of the corresponding "probability density coil"; see Figure 16.1, based on the illustration of Epps (1993, p. 34). It is always bounded, because it is confined to the infinite complex tube with radius one. If the characteristic function itself is absolutely integrable from *u* = −∞ to *u* = ∞, then the corresponding probability distribution *F*(*x*) is absolutely continuous and has a density function *f*(*x*). Furthermore, from the trigonometric representation (16.11), we can immediately conclude that

$$\varphi(-u) = \varphi^*(u), \tag{16.12}$$

where φ ∗ (*u*) is the complex conjugate of the characteristic function.

**Quick calculation 16.1** Convince yourself that this statement is true by recalling that cosine is an even function and sine is odd.

An equally important result in applying characteristic functions is the *Fourier*inversion-theorem. It ensures that the original probability density can be recovered by the inverse transformation

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-iux} \varphi(u) du.$$
 (16.13)

Now you should be able to see, why absolute integrability of φ(*u*) is a necessary condition for the probability density function to exist. Most of the time we have to compute

such integrals numerically. Although we will discuss that issue at a later time, it is nice to derive a better suited representation. Once again, recall the *Euler*-identity (16.11) to realize that the real part of the characteristic function is

$$\text{Re}[\varphi(u)] = \frac{\varphi(u) + \varphi^*(u)}{2}.$$
 (16.14)

**Quick calculation 16.2** Confirm that also Im[ φ(*u*) ] = φ(*u*)−φ ∗ (*u*) 2*i* holds.

The same holds true of course for *e iux* itself. Let's now split the inversion integral in (16.13) and use (16.14) to obtain

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{0} e^{-iux} \varphi(u) du + \frac{1}{2\pi} \int_{0}^{\infty} e^{-iux} \varphi(u) du$$
  
$$= \frac{1}{2\pi} \int_{0}^{\infty} e^{iux} \varphi^{*}(u) du + \frac{1}{2\pi} \int_{0}^{\infty} e^{-iux} \varphi(u) du$$
  
$$= \frac{1}{\pi} \int_{0}^{\infty} \frac{(e^{-iux} \varphi(u))^{*} + e^{-iux} \varphi(u)}{2} du$$
  
$$= \frac{1}{\pi} \int_{0}^{\infty} \text{Re} \left[ e^{-iux} \varphi(u) \right] du.$$
  
(16.15)

As we will see, this is a far more convenient form for the application of numerical integration schemes.

The generalized *Fourier*-transform, sometimes also called the fundamental transform, uses the complex number *z*, instead of the real number *u*, as variable. We thus obtain the generalized characteristic function

$$\varphi(z) = E[e^{izX}] = \int_{-\infty}^{\infty} e^{izx} f(x) dx, \quad z \in \mathcal{S}.$$
 (16.16)

This formula needs some comment. First of all, the generalized characteristic function does not necessarily exist in the entire complex plane. But there is always a so-called strip of regularity S, where it does. A complex function is called regular, if it is single valued and analytic. This is guaranteed by a theorem of Lukacs (1970, theorem 7.1.1), also found in Lewis (2001).

**Theorem 16.1 (Strip of regularity)** *If a characteristic function* φ(*z*) *with z* ∈ C *is regular in the neighborhood of z* = 0, *then it is also regular in a horizontal strip* S *and can be represented in this strip by a Fourier*-*integral. This strip is either the whole z-plane, or it has one or two horizontal boundary lines. The purely imaginary points on the boundary of the strip of regularity (if this strip is not the whole plane) are singular points of* φ(*z*).

The statement of Theorem 16.1 is fairly general and applies to arbitrary distributions. In particular, we have φ(0) = 1, because every probability density function has to be normalized.

**Quick calculation 16.3** Confirm the last statement with the help of (16.16).

In derivative pricing, we have an additional condition because of the martingale pricing relation. Assume that the stochastic process *Y<sup>t</sup>* is the purely nonsystematic part of the return, and

$$\varphi_s(z) = E^{\mathcal{Q}}[e^{izY_t}|\mathcal{F}_s] \tag{16.17}$$

for *s* ≤ *t* is its generalized conditional characteristic function under the risk-neutral measure *Q*. We can then write the price process of the underlying as

$$S_t = S_0 e^{bt + Y_t} = S_0 e^{bt} e^{Y_t}, \t\t(16.18)$$

where *b* is the generalized cost-of-carry rate. Clearly *Y<sup>t</sup>* has to be a *Q*-martingale with *E Q* [ *e Yt* ] = 1. But this also means φ0(−*i*) = 1. This gives us a necessary condition for an appropriate return process under the risk-neutral measure *Q*. A "good" process *Y<sup>t</sup>* satisfies *Y*<sup>0</sup> = 0 and generates a risk-neutral probability density *qY*(*y*, *t*), whose conditional characteristic function φ0(*z*) exists within a strip of regularity S*<sup>Y</sup>* = { *z* = *u* + *iv* : *v* ∈ (α, β) } , with α < −1 and β > 0.

The generalized inverse *Fourier*-transform is similar to the ordinary inversion formula (16.13), but the integration is conducted along an arbitrary straight line parallel to the real axis, within the strip of regularity

$$f(x) = \frac{1}{2\pi} \int_{iv-\infty}^{iv+\infty} e^{-izx} \varphi(z) dz, \quad z \in \mathcal{S}.$$
 (16.19)

In most cases, properties of the ordinary *Fourier*-transform also hold for the generalized transform, without any modification.

### **16.3 The Pricing Formula in Fourier-Space**

It is not really necessary to use a generalized version of the *Fourier*-transform to obtain a pricing formula in *Fourier*-space; see for example the methods proposed by Heston (1993) or Carr and Madan (1999). But we will follow here the very elegant idea of Lewis (2000), which is modular in a certain sense, because it separates the payoff function and the conditional pricing density. Key to this approach is a theorem that can be found in Lewis (2001, theorem 3.2):

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

**Theorem 16.2 (Option Valuation)** *Let V*0(*K*,*T*) *be the current price of a European-style option with payoff function V*(*e x* , σ,*T*) = *w*(*x*), *where x<sup>t</sup>* = log *S<sup>t</sup> is the logarithmic price of the underlying. Assume that w*(*x*) *is Fourier*-*integrable in a strip* S*<sup>w</sup> and bounded for* |*x*| < ∞. *Let S<sup>t</sup>* = *S*0*e bt*+*Y<sup>t</sup>* , *where e<sup>Y</sup><sup>t</sup> is a Q*-*martingale, and assume that Y<sup>T</sup> has the analytic*

conditional characteristic function  $\varphi_0(z)$ , regular in the strip  $S_Y = \{z = u + iv : v \in (\alpha, \beta)\}$ , where  $\alpha < -1$  and  $\beta > 0$ . If  $S_V = S_w \cap S_v^*$  is not empty, then the option value at time  $t = 0$ is given by

$$V_0(K,T) = \frac{e^{-rT}}{2\pi} \int_{iv-\infty}^{iv+\infty} e^{-iz(\log S_0 + bT)} \varphi_0(-z) \hat{w}(z) dz, \quad z \in \mathcal{S}_V = \mathcal{S}_w \cap \mathcal{S}_Y^*.$$

*Moreover,*  $S_V$  *is not empty for the payoff function of a call or put option.* 

Let's see if we can understand how this formula arises. First of all, we have again adopted the hat notation  $\hat{w}(z)$ , to indicate the generalized *Fourier*-transform of  $w(x)$ . Next, from the martingale pricing principle, we know that

$$V_{0}(K,T) = e^{-rT} E^{Q} [w(x_{T})]$$
  

$$= \frac{e^{-rT}}{2\pi} E^{Q} \left[ \int_{iv-\infty}^{iv+\infty} e^{-izx_{T}} \hat{w}(z) dz \right]$$
  

$$= \frac{e^{-rT}}{2\pi} E^{Q} \left[ \int_{iv-\infty}^{iv+\infty} e^{-iz(\log S_{0} + bT)} e^{-izY_{T}} \hat{w}(z) dz \right], \quad z \in \mathcal{S}_{w}.$$
(16.20)

As always, the risk-neutral expectation is conditional on  $\mathcal{F}_0$ . The next step is to bring the expectation inside the integral, which is only a valid operation, if we can ensure that  $E^{\mathcal{Q}}[e^{-izY_T}] = \varphi_0(-z)$  exists. This is the case, if  $z \in \mathcal{S}_Y^*$ , but z is already confined to the strip  $S_w$ . Hence, the integrand exists and is regular if  $z \in S_V = S_w \cap S^*_V$ , with  $S^*_V = \{z =$  $u + iv : v \in (\alpha, \beta)$ , where now  $\alpha < 0$  and  $\beta > 1$ . We thus obtain the result in Theorem 16.2. Observe that even though the strip condition contains the conjugate strip  $\mathcal{S}_{v}^{*}$ ,  $\varphi(-z)$  is not the complex conjugate of the characteristic function  $\varphi(z)$ , but close to it.

**Quick calculation 16.4** Use Euler's identity to show that  $\varphi^*(z) = \varphi(-z^*)$  holds.

We still have to verify that the strip  $\mathcal{S}_V$  is not empty for call and put option payoffs. To this end, let's see what the generalized transforms of these functions are and in which strip they are regular. Start with the call payoff,

$$\hat{w}(z) = \int_{-\infty}^{\infty} e^{izx} (e^x - K)^+ dx \n= \int_{\log K}^{\infty} e^{izx} (e^x - K) dx \n= \left[ \frac{e^{(iz+1)x}}{iz + 1} - K \frac{e^{izx}}{iz} \right]_{x = \log K}^{x = \infty} .\n$$
(16.21)

It is not hard to see that the upper limit only exists, if  $\text{Im}[z] > 1$ . In this case both exponentials vanish at  $x = \infty$  and the result is

$$\hat{w}(z) = -\frac{K^{iz+1}}{z^2 - iz}, \quad z \in \mathcal{S}_w,$$
 (16.22)

with  $S_w = \{z = u + iv : v > 1\}.$ 

| <b>Table 16.2</b> Standard payoff functions |                 |                             |                                        |  |
|---------------------------------------------|-----------------|-----------------------------|----------------------------------------|--|
| Financial Claim                             | Payoff $w(x)$   | Transform $\hat{w}(z)$      | <b>Regular Strip</b> $\mathcal{S}_{w}$ |  |
| Call                                        | $(e^{x}-K)^{+}$ | $-\frac{K^{iz+1}}{z^2-iz}$  | $\text{Im}[z] > 1$                     |  |
| Put                                         | $(K-e^x)^+$     | $-\tfrac{K^{iz+1}}{z^2-iz}$ | $\text{Im}[z] < 0$                     |  |
| Binary Call                                 | $\theta(e^x-K)$ | $-\frac{K^{iz}}{iz}$        | $\text{Im}[z] > 0$                     |  |
| Binary Put                                  | $\theta(K-e^x)$ | $\frac{K^{iz}}{iz}$         | $\text{Im}[z] < 0$                     |  |
| Covered Call                                | $\min(e^x, K)$  | $\frac{K^{iz+1}}{z^2 - iz}$ | $0 < \text{Im}[z] < 1$                 |  |
| Arrow–Debreu                                | $\delta(e^x-K)$ | $K^{iz}$                    | entire $z$ -plane                      |  |

**Quick calculation 16.5** Confirm that the payoff transform of a put is regular for  $v < 0$ .

Interestingly, but not completely surprisingly, the transformed payoff  $(16.22)$  is also the result for the put option, but now the strip of regularity is  $S_w = \{z = u + iv : v < 0\}.$ Both strips intersect the conjugate strip  $\mathcal{S}_{V}^{*}$  in Theorem 16.2, and thus  $\mathcal{S}_{V}$  is not empty. Table 16.2 contains a small collection of transformed payoff functions and their associated strips of regularity.

The formula provided in Theorem 16.2 is not yet an explicit pricing equation, but more a blueprint for the construction of such an equation. Because calibrating a stochastic volatility model is usually done with plain vanilla European call and put options, we will derive the explicit formulas for those contracts. Plugging the call payoff transform  $(16.22)$  into the general formula of Theorem 16.2, one obtains

$$C_0(K,T) = -\frac{e^{-rT}K}{2\pi} \int_{iv_0-\infty}^{iv_0+\infty} \frac{e^{-izk}\varphi_0(-z)}{z^2 - iz} dz, \quad v_0 \in (1,\beta), \tag{16.23}$$

where  $k = \log(S_0/K) + bT$  is the forward log-moneyness. The integral in (16.23) is guaranteed to exist, because  $S_V = S_w \cap S_v^* = \{z = u + iv_0 : v_0 \in (1,\beta)\}$  is not empty as long as  $\beta > 1$ . It is indeed easy to see that the integrand

$$f(z) = \frac{e^{-izk}\varphi_0(-z)}{z(z-i)}$$
(16.24)

is regular in the entire strip  $S^*_{V}$  with exception of the two simple poles at  $z = 0$  and  $z = i$ . Thus, it might be a clever idea to shift the integration contour to  $0 < v_1 < 1$ , because every appropriate characteristic function has to be regular in this strip. Let  $I(v_0)$  be the integral in  $(16.23)$ . Then we know from Cauchy's residue theorem (Theorem A.4 on page 522) that

$$I(v_1) - I(v_0) = 2\pi i \operatorname{Res}_{z=i} f.$$
 (16.25)

This conclusion needs some comment. The situation is illustrated in Figure 16.2. The minus sign results from the counterclockwise orientation of the closed curve. The

![](_page_8_Figure_1.jpeg)

**Fig. 16.2** Strip of regularity S ∗ *Y* and simple poles at *z* = 0 and *z* = *i* – The integral along the closed curve can be computed with the residue theorem

contributions from the legs at *u* = ±∞ are zero and hence, the left hand side of (16.25) contains all correctly oriented contributions to the closed loop. To find the residue at *z* = *i*, define the function

$$g_1(z) = (z - i)f(z) = \frac{e^{-izk}\varphi_0(-z)}{z},\tag{16.26}$$

and evaluate it at *z* = *i*,

$$\operatorname{Res}_{z=i} f = g_1(i) = \frac{e^k}{i},\tag{16.27}$$

where again *k* = log(*S*0/*K*) + *bT*. Because of the martingale condition under the pricing measure, φ0(−*i*) = 1 holds. Combining (16.23), (16.25), and (16.27), one obtains

$$C_0(K,T) = e^{(b-r)T} S_0 - \frac{e^{-rT}K}{2\pi} \int_{iv_1-\infty}^{iv_1+\infty} \frac{e^{-izk}\varphi_0(-z)}{z^2 - iz} dz, \quad v_1 \in (0,1).$$
(16.28)

This is our preferred integration contour, because we can choose freely a value in the range 0 < *v*<sup>1</sup> < 1, without bothering about particular boundaries for different characteristic functions. To make this pricing formula concrete, choose for example *v*<sup>1</sup> = 1 2 and make the substitution *z* = *u* + *i* 2 to obtain

$$C_{0}(K,T) = e^{(b-r)T}S_{0} - \frac{e^{(\frac{b}{2}-r)T}\sqrt{S_{0}K}}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-iuk}\varphi_{0}(-u-\frac{i}{2})}{u^{2}+\frac{1}{4}} du$$
  
$$= e^{(b-r)T}S_{0} - \frac{e^{(\frac{b}{2}-r)T}\sqrt{S_{0}K}}{\pi} \int_{0}^{\infty} \frac{\text{Re}\left[e^{iuk}\varphi_{0}(u-\frac{i}{2})\right]}{u^{2}+\frac{1}{4}} du.$$
 (16.29)

Inside the real part in the second row of (16.29), we have changed the sign of *u*. That does not change the result, as long as we flip signs in both the phase factor and the characteristic function.

**Quick calculation 16.6** Use the fact that φ ( *z* ∗ ) = φ ∗ (−*z*) to convince yourself that this statement is true.

The integral in (16.29) converges more rapidly than a plain *Fourier*-integral, because of the *u* 2 -term in the denominator.

There is another surprising twist. Imagine, we shift the integration contour to *v*<sup>2</sup> ∈ (α, 0). In doing so, we pick up an additional residue at *z* = 0. To compute this one, define the function

$$g_2(z) = zf(z) = \frac{e^{-izk}\varphi_0(-z)}{z - i},$$
(16.30)

and evaluate it at *z* = 0,

$$\operatorname{Res}_{z=0} f = g_2(0) = -\frac{1}{i}.$$
 (16.31)

By an argument, completely analogous to the one illustrated in Figure 16.2, we can see immediately that

$$I(v_2) - I(v_1) = 2\pi i \operatorname{Res}_{z=0} f$$
 (16.32)

has to hold, where we used our previous notation for the integral along a particular contour. Using this condition in (16.28), one obtains

$$C_0(K,T) = e^{(b-r)T}S_0 - e^{-rT}K - \frac{e^{-rT}K}{2\pi} \int_{iv_2-\infty}^{iv_2+\infty} \frac{e^{-izk}\varphi_0(-z)}{z^2 - iz} dz, \quad v_2 \in (\alpha, 0). \tag{16.33}$$

But realizing that the last term in (16.33) is the fair price of the put option *P*0(*K*, *T*), we have recovered put-call parity in a truly amazing guise. We therefore have

$$P_{0}(K,T) = e^{-rT}K - \frac{e^{(\frac{b}{2}-r)T}\sqrt{S_{0}K}}{\pi} \int_{0}^{\infty} \frac{\text{Re}\left[e^{iuk}\varphi_{0}(u-\frac{i}{2})\right]}{u^{2}+\frac{1}{4}}du.$$
 (16.34)

### **16.4 The Heston–Nandi GARCH-Model**

As a prelude to the introduction of the important *Heston*-model for option pricing, let's consider a particular GARCH-model, suggested by Heston and Nandi (1997, 2000). Even though GARCH-models do not truly possess stochastic volatility, we can understand most ideas of the *Heston*-model in the simpler GARCH framework. In particular, we will restrict ourselves to analyzing the simplest possible member of the *Heston–Nandi*-class, which has the form

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\Delta x_t = r + \lambda h_t + \sqrt{h_t} z_t \tag{16.35}$$

$$h_t = \omega + \alpha \left( z_{t-1} - \gamma \sqrt{h_{t-1}} \right)^2 + \beta h_{t-1}.$$
 (16.36)

Again, *x<sup>t</sup>* = log *S<sup>t</sup>* is the logarithmic price process of a non-dividend paying stock and ∆*x<sup>t</sup>* = *x<sup>t</sup>* − *xt*−1. The random innovation *z<sup>t</sup>* is assumed standard normally distributed. Contrary to the *Duan*-model (15.23) on page 333, the risk premium in (16.35) is

assumed proportional to the variance, not to its square root. This is a necessary requirement for the model to belong to the so-called affine class of GARCH-models; we will learn shortly what that means. With the transformations

$$z_t^Q = z_t + \left(\lambda + \frac{1}{2}\right)\sqrt{h_t} \tag{16.37}$$

$$\gamma^{\mathcal{Q}} = \gamma + \lambda + \frac{1}{2},\tag{16.38}$$

the whole GARCH-model is transferred into the risk-neutral world, by switching from *z<sup>t</sup>* to *z Q t* . After some trivial rearrangements, one obtains

$$\Delta x_t = r - \frac{1}{2}h_t + \sqrt{h_t}z_t^Q \tag{16.39}$$

$$h_{t} = \omega + \alpha \left( z_{t-1}^{Q} - \gamma^{Q} \sqrt{h_{t-1}} \right)^{2} + \beta h_{t-1}.$$
 (16.40)

**Quick calculation 16.7** Check that the transformation is algebraically correct.

Now, (16.39) is identical to the first equation of the *Duan*-model (15.26) under the riskneutral measure *Q*. Of course in the GARCH-framework we have the luxury to fit the model under the physical measure *P* and hence, to obtain the risk premium. This is no longer possible for the true stochastic volatility *Heston*-model. But observe that the risk premium does not appear explicitly in (16.39) and (16.40) and thus, the model can be calibrated to the observed option prices without determining the risk premium in the first place.

Let's first bring the whole model into the right form *S<sup>t</sup>* = *S*0*e bt*+*Y<sup>t</sup>* . Because the underlying is a non-dividend paying stock, the generalized cost-of-carry rate is *b* = *r* and *e Yt* has to be a *Q*-martingale with *Y*<sup>0</sup> = 0. From (16.39) we conclude that *Y<sup>t</sup>* has to have the dynamics

$$Y_t = Y_{t-1} - \frac{1}{2}h_t + \sqrt{h_t}z_t^Q,$$
 (16.41)

with *h<sup>t</sup>* given by (16.40), and again *z Q <sup>t</sup>* ∼ *N*(0, 1) under the pricing measure *Q*.

**Quick calculation 16.8** Show that *e Yt* is indeed a *Q*-martingale by using the law of iterated expectations.

An affine class GARCH-model is defined by a particular form of its characteristic function. Under the risk-neutral measure *Q*, the conditional characteristic function has to be given by

$$\varphi_t(u) = E^{\mathcal{Q}}[e^{iuY_T}|\mathcal{F}_t] = e^{iuY_t + A_t(u) + B_t(u)h_{t+1}},\tag{16.42}$$

with  $A_T(u) = 0$  and  $B_T(u) = 0$ . The unknown complex valued functions  $A_t(u)$  and  $B_t(u)$ are yet to be determined. The key idea in finding these unknown functions is once again the use of the law of iterated expectations. We can use it to write the identity

$$\varphi_{t-1}(u) = E^{Q}[\varphi_{t}(u)|\mathcal{F}_{t-1}] = E^{Q}[e^{iuY_{t} + A_{t}(u) + B_{t}(u)h_{t+1}}|\mathcal{F}_{t-1}]. \tag{16.43}$$

**Quick calculation 16.9** Can you see why the first equality is correct?

The next step is to plug in (16.40) and (16.41) for  $h_{t+1}$  and  $Y_t$ . After applying some algebraic tricks and enduring rather tedious calculations, one ends up with three sorts of terms, simple terms, which are known from the information  $\mathcal{F}_{t-1}$ , terms which are also known but are multiplied by  $h_t$ , and those terms involving  $z_t$  and  $\sqrt{h_t}$ . We can move everything that is known out of the expectation to obtain the schematic expression

$$\varphi_{t-1}(u) = e^{iuY_{t-1} + \dots + (\dots)h_t} \cdot E^Q \left[ e^{\alpha B_t(u) \left( z_t + \left( \frac{iu}{2\alpha B_t(u)} - \gamma^Q \right) \sqrt{h_t} \right)^2} \middle| \mathcal{F}_{t-1} \right]. \tag{16.44}$$

Observe that  $z_t$  is an independent innovation which is not conditional on  $\mathcal{F}_{t-1}$ , and  $\sqrt{h_t}$ is already known. Thus, we can use the simple identity

$$E\left[e^{a(z+b)^{2}}\right] = e^{-\frac{1}{2}\log(1-2a) + \frac{ab^{2}}{1-2a}},\tag{16.45}$$

for arbitrary a and b with  $\text{Re}[a] \leq \frac{1}{2}$ , and standard normally distributed z. The restriction on  $a$  becomes in fact never binding. Computing the expectation in (16.44) generates again two types of terms, simple ones and terms multiplying  $h_t$ . So after another round of algebraic manipulations, we end up with an expression like

$$\varphi_{t-1}(u) = e^{iuY_{t-1} + \dots + (\dots)h_t}.$$
(16.46)

Comparing this result with  $(16.42)$ , we must conclude that we have indeed computed  $A_{t-1}$  and  $B_{t-1}$ . Recalling that  $Y_0 = 0$ , the desired conditional characteristic function is

$$\varphi_0(u) = e^{A_0(u) + B_0(u)h_1},\tag{16.47}$$

with  $A_0(u)$  and  $B_0(u)$  recursively computed by

$$A_{t-1}(u) = A_t(u) + \omega B_t(u) - \frac{1}{2} \log(1 - 2\alpha B_t(u))$$
(16.48)

$$B_{t-1}(u) = iu\left(\gamma^{Q} - \frac{1}{2}\right) - \frac{\gamma^{Q^{2}}}{2} + \beta B_{t}(u) + \frac{\frac{1}{2}(iu - \gamma^{Q})^{2}}{1 - 2\alpha B_{t}(u)},\tag{16.49}$$

and initial function values  $A_T(u) = 0$  and  $B_T(u) = 0$ . We have omitted most of the messy details of the derivation because they are purely technical. The important fact is that knowledge of  $\varphi_0(u)$  is enough to price a couple of plain vanilla contracts with the help

of the formalism developed earlier in this chapter. Of course we do not yet know how to compute the integrals in  $(16.29)$  and  $(16.34)$ , and we will postpone this discussion, until we have introduced the important stochastic volatility model of Heston (1993).

### The *Heston*-Model

Heston (1993) considered the following model for the dynamics of a non-dividend paying stock

$$dS_t = \mu S_t dt + \sqrt{v_t} S_t dW_{1,t} \tag{16.50}$$

$$dv_t = \kappa(\theta - v_t)dt + \alpha \sqrt{v_t}dW_{2,t},\tag{16.51}$$

where the covariance between the *Wiener*-processes is  $E[dW_1dW_2] = \rho dt$ . The variance equation (16.51) is the *Cox–Ingersoll–Ross*-model (CIR, Cox et al., 1985), also used as short rate model in pricing fixed-income products. If the *Feller*-condition (Feller, 1951)

$$2\kappa\theta \ge \alpha^2 \tag{16.52}$$

is satisfied, the variance process  $v_t$  stays positive for all times. Furthermore, it is mean reverting to the equilibrium variance  $\theta$ , also called the mean reversion level. The parameter  $\kappa$  controls the strength of the pull back to equilibrium and is called the mean reversion speed. Of course, we expect the correlation  $\rho$  to be negative, because of the leverage effect observed in real data.

Because there are now two sources of randomness, we need a second risk premium to account for the volatility risk. Precisely as in the *Heston–Nandi* GARCH-model, this risk premium is assumed proportional to the variance, and therefore we must have

$$\lambda(S, v, t) = \frac{\lambda}{\alpha} \sqrt{v} \tag{16.53}$$

in order to get it right after switching to O. We can find out how the model looks under the risk-neutral measure, by applying the two-dimensional *Girsanov*-transformation

$$\left. \frac{dQ}{dP} \right|_{\mathcal{F}_t} = \exp\left(-\int_0^t \frac{\mu - r}{\sqrt{v_s}} dW_{1,s} - \int_0^t \frac{\lambda}{\alpha} \sqrt{v_s} dW_{2,s} - \frac{1}{2} \int_0^t \frac{(\mu - r)^2}{v_s} + \frac{\lambda^2}{\alpha^2} v_s ds\right). \tag{16.54}$$

This transformation corresponds to switching to the risk-neutral *Wiener*-increments

$$dW_{1,t}^{Q} = dW_{1,t} + \frac{\mu - r}{\sqrt{v_t}}dt \tag{16.55}$$

$$dW_{2,t}^{Q} = dW_{2,t} + \frac{\lambda}{\alpha} \sqrt{v_t} dt. \qquad (16.56)$$

**Quick calculation 16.10** Prove that  $\text{Cov}[dW_1^Q, dW_2^Q] = \rho dt$  still holds.

### 16.5

If we use Itô's lemma to switch to log-prices  $x_t = \log S_t$  and apply the parameter transformations  $\kappa^Q = \kappa + \lambda$  and  $\theta^Q = \frac{\kappa \theta}{\kappa + \lambda}$ , then the *Heston*-model under the risk-neutral  $\text{probability measure } O \text{ becomes}$ 

$$dx_{t} = \left(r - \frac{1}{2}v_{t}\right)dt + \sqrt{v_{t}}dW_{1,t}^{Q}$$
 (16.57)

$$dv_t = \kappa^{\mathcal{Q}} (\theta^{\mathcal{Q}} - v_t) dt + \alpha \sqrt{v_t} dW_{2,t}^{\mathcal{Q}}, \tag{16.58}$$

with

$$\kappa^{Q} = \kappa + \lambda, \quad \theta^{Q} = \frac{\kappa \theta}{\kappa + \lambda}, \quad \text{and} \quad E[dW_{1}^{Q}dW_{2}^{Q}] = \rho dt.\n$$
(16.59)

**Quick calculation 16.11** Confirm that this transformation is algebraically correct.

We have again effectively eliminated the volatility risk premium under  $O$ , by introducing the new parameters  $\kappa^Q$  and  $\theta^Q$ . We can extract the important martingale process  $Y_t$  under O by simply eliminating the drift part, which is due to compounding with the risk-free interest rate  $r$  The result is

$$dY_t = -\frac{1}{2}v_t dt + \sqrt{v_t} dW_{1,t}, \qquad (16.60)$$

with  $(16.58)$  and  $(16.59)$  still unchanged. Observe that the last two steps are completely analogous to (16.39) to (16.41) in the *Heston–Nandi* GARCH-model.

We proceed by making an observation about the characteristic function. Remember that the unconditional expectation is with respect to the trivial  $\sigma$ -algebra  $\mathcal{F}_0$ . Therefore, by the law of iterated expectations, we must have

$$E^{\mathcal{Q}}[\varphi_t(u)] = E^{\mathcal{Q}}\left[E^{\mathcal{Q}}[e^{iuY_T}|\mathcal{F}_t]\middle|\mathcal{F}_0\right] = \varphi_0(u). \tag{16.61}$$

That means, the expectation of the characteristic function does not vary over time and thus, we must have also

$$E^{\mathcal{Q}}[d\varphi_t(u)] = 0. \tag{16.62}$$

But how do we get an idea of the dynamics of  $\varphi$ ? The answer might come as a shock, but  $\varphi$  is a smooth function of Y, v, and t, so we can apply Itô's lemma. The result is

$$d\varphi = \left( -\frac{v}{2} \frac{\partial \varphi}{\partial Y} + \kappa^{\mathcal{Q}} (\theta^{\mathcal{Q}} - v) \frac{\partial \varphi}{\partial v} + \frac{\partial \varphi}{\partial t} + \frac{v}{2} \frac{\partial^2 \varphi}{\partial Y^2} + \rho \alpha v \frac{\partial^2 \varphi}{\partial Y \partial v} + \frac{1}{2} \alpha^2 v \frac{\partial^2 \varphi}{\partial v^2} \right) dt + \sqrt{v} \frac{\partial \varphi}{\partial Y} dW_1 + \alpha \sqrt{v} \frac{\partial \varphi}{\partial v} dW_2, \tag{16.63}$$

where the function arguments t and  $u$  were suppressed for notational convenience. It is obvious that if we take the expectation of  $(16.63)$ , the terms in the second row

vanish. But since we know that the expectation of *d*φ is zero, the terms in the bracket, multiplying *dt*, must also vanish and we obtain

$$\frac{\partial\varphi}{\partial t} - \frac{v}{2}\frac{\partial\varphi}{\partial Y} + \kappa^{\mathcal{Q}}(\theta^{\mathcal{Q}} - v)\frac{\partial\varphi}{\partial v} + \frac{v}{2}\frac{\partial^2\varphi}{\partial Y^2} + \rho\alpha v\frac{\partial^2\varphi}{\partial Y\partial v} + \frac{1}{2}\alpha^2 v\frac{\partial^2\varphi}{\partial v^2} = 0.$$
 (16.64)

Now, let us make the educated guess that the characteristic function has the particular form

$$\varphi_t(u) = e^{iuY_t + A(t,u) + B(t,u)v_t}, \tag{16.65}$$

with the yet unknown functions *A*(*t*, *u*) and *B*(*t*, *u*). Does that remind you of something? If our guess is correct, the *Heston*-model belongs to the same affine model class as the *Heston–Nandi* GARCH-model. Plugging (16.65) into (16.64) and afterwards dividing by φ yields

$$\frac{\partial A}{\partial t} + \kappa^{\mathcal{Q}} \theta^{\mathcal{Q}} B + \nu \left( \frac{\partial B}{\partial t} - \frac{1}{2} iu - \kappa^{\mathcal{Q}} B - \frac{1}{2} u^2 + iu\rho\alpha B + \frac{1}{2}\alpha^2 B^2 \right) = 0. \tag{16.66}$$

There are two kinds of terms on the left hand side of this equation, simple ones, and those multiplying *v*. Since *v* is arbitrary, the terms inside and outside the bracket have to vanish separately. To see this convince yourself that (16.66) has to hold for both, *v* = 0 and *v* , 0. Thus, we obtain a system of two separate ordinary differential equations in *A* and *B*

$$\frac{\partial A}{\partial t} = -\kappa^{\mathcal{Q}} \theta^{\mathcal{Q}} B(t, u) \tag{16.67}$$

$$\frac{\partial B}{\partial t} = \frac{1}{2}(iu + u^2) + (\kappa^Q - iu\rho\alpha)B(t, u) - \frac{1}{2}\alpha^2 B^2(t, u). \tag{16.68}$$

The second one is an equation of the *Riccati*-type. Solving it is a delicate matter. Let's go through it step by step.

First let's simplify (16.68) to a schematic level and suppress the dependence on the variable *u* temporarily. The basic form is

$$B'(t) = p + qB(t) - rB^{2}(t), \qquad (16.69)$$

where the prime now indicates the derivative with respect to time. Remember that the coefficients are

$$p = \frac{1}{2}(iu + u^2), \quad q = (\kappa^Q - iu\rho\alpha), \quad \text{and} \quad r = \frac{1}{2}\alpha^2.$$
 (16.70)

At the end we will need to retrace our steps. We cannot solve (16.69) directly; we need the auxiliary second order differential equation

$$w''(t) = qw'(t) + prw(t).$$
 (16.71)

With the help of (16.71), we can express the solution of our initial *Riccati*-equation as

$$B(t) = \frac{w'(t)}{w(t)} \cdot \frac{1}{r}.$$
 (16.72)

**Quick calculation 16.12** Prove this statement by differentiating both sides of (16.72).

The auxiliary differential equation is a standard problem with the known solution

$$w(t) = c_1 e^{\frac{q+d}{2}t} + c_2 e^{\frac{q-d}{2}t},\tag{16.73}$$

with

$$d = \sqrt{q^2 + 4pr}.\tag{16.74}$$

The coefficients *c*<sup>1</sup> and *c*<sup>2</sup> are not yet determined. Plugging this solution into (16.72), one obtains

$$B(t) = \frac{c_1(q+d)e^{\frac{q+d}{2}t} + c_2(q-d)e^{\frac{q-d}{2}t}}{c_1e^{\frac{q+d}{2}t} + c_2e^{\frac{q-d}{2}t}} \cdot \frac{1}{2r}.$$
 (16.75)

It is now time to make use of the additional information that the final value of *B*(*t*) has to be *B*(*T*) = 0. This means, at time *T* the numerator of (16.75) has to vanish. This fact enables us to express one unknown coefficient in terms of the other. Concentrating on *c*1, one obtains

$$c_1 = -c_2 c e^{-d \cdot T},\tag{16.76}$$

where the new coefficient *c* was introduced as

$$c = \frac{q - d}{q + d}.\tag{16.77}$$

Using this new rule for the coefficient *c*1, all remaining coefficients *c*<sup>2</sup> cancel out of the equation and one obtains

$$B(t) = \frac{q-d}{2r} \cdot \frac{e^{\frac{q-d}{2}t} - e^{\frac{q+d}{2}t-d\cdot T}}{e^{\frac{q-d}{2}t} - ce^{\frac{q+d}{2}t-d\cdot T}} = \frac{q-d}{2r} \cdot \frac{1-e^{-d(T-t)}}{1 - ce^{-d(T-t)}}.$$
(16.78)

This is not quite the form originally derived by Heston (1993). We would have obtained the original form by solving for *c*<sup>2</sup> in (16.76). But as pointed out by Albrecher et al. (2007), this one is preferable for numerical reasons.

Now let's solve for the second function *A*(*t*). Integrating (16.67) with *A*(*T*) = 0 yields

$$A(t) = -\kappa^{Q} \theta^{Q} \int_{T}^{t} B(s)ds = \frac{\kappa^{Q} \theta^{Q}(q-d)}{2r} \int_{t}^{T} \frac{1 - e^{-d(T-s)}}{1 - ce^{-d(T-s)}} ds.$$
 (16.79)

Let's first focus on solving the integral. Make the substitution *x* = *e* −*d*(*T*−*t*) . This makes the increment *dx* = *d* · *e <sup>d</sup>*(*T*−*s*)*ds* = *d* · *x ds*, and the integral becomes

$$\frac{1}{d} \int_{e^{-d(T-t)}}^{1} \frac{1-x}{(1-cx)x} dx = \frac{1}{d} \int_{e^{-d(T-t)}}^{1} \left(\frac{1}{x} - \frac{1-c}{1-cx}\right) dx$$
$$= \frac{1}{d} \left[ \log x + \frac{1-c}{c} \log(1-cx) \right]_{x=e^{-d(T-t)}}^{x=1}$$
$$= (T-t) - \frac{1-c}{cd} \log\left(\frac{1-ce^{-d(T-t)}}{1-c}\right).$$
(16.80)

**Quick calculation 16.13** Verify the first equality.

Remember that *c* = *q*−*d q*+*d* and thus, the coefficient in front of the logarithm becomes

$$\frac{1-c}{cd} = \frac{1 - \frac{q-d}{q+d}}{\frac{q-d}{q+d}d} = \frac{2d}{(q-d)d} = \frac{2}{q-d}.$$
(16.81)

Putting all the pieces together, one obtains the desired expression

$$A(t) = \frac{\kappa^{\mathcal{Q}}\theta^{\mathcal{Q}}}{2r} \left( (q-d)(T-t) - 2\log\left(\frac{1 - ce^{-d(T-t)}}{1-c}\right) \right). \tag{16.82}$$

With this last piece, we are able to price options in the stochastic volatility *Heston*model. All we needed was an expression for the conditional characteristic function of the martingale process *Y<sup>t</sup>* , to feed into our pricing formula (16.29) or (16.34), respectively. This expression is given in the *Heston*-model by

$$\varphi_0(u) = e^{A(0,u) + B(0,u)v_0},\tag{16.83}$$

where

$$A(t,u) = \frac{\kappa^{\mathcal{Q}}\theta^{\mathcal{Q}}}{\alpha^2} \left( (\kappa^{\mathcal{Q}} - iu\rho\alpha - d)(T - t) - 2\log\left(\frac{1 - ce^{-d(T - t)}}{1 - c}\right) \right) \tag{16.84}$$

$$B(t,u) = \frac{\kappa^Q - iu\rho\alpha - d}{\alpha^2} \cdot \frac{1 - e^{-d(T-t)}}{1 - ce^{-d(T-t)}},$$
(16.85)

with

$$c = \frac{\kappa^Q - iu\rho\alpha - d}{\kappa^Q - iu\rho\alpha + d} \quad \text{and} \quad d = \sqrt{(\kappa^Q - iu\rho\alpha)^2 + \alpha^2(iu + u^2)}.$$
 (16.86)

Of course we have to show that the generalized characteristic function φ0(*z*) is regular in the complex strip S*<sup>Y</sup>* = { *z* = *u* + *iv* : *v* ∈ (α, β) } , with α < −1 and β > 0. This is far from trivial in the *Heston*-model, but the analysis of Lewis (2000, example II on p. 44) shows that it indeed is. So we are ready to go. The only thing missing is a method for computing the integrals in (16.29) and (16.34).

## Inverting the Fourier-Transform

There exist numerous methods to invert a *Fourier*-transformation numerically. Some of them, as for example the fast *Fourier*-transform (FFT), are highly sophisticated algorithms, with whole books written about them. We will use a *Gaussian* quadrature method instead, because it is easy to implement and the integrals in  $(16.29)$  and  $(16.34)$ converge rapidly. So what is the idea behind a quadrature method? Assume that  $f(x)$  is a smooth function that can be approximated sufficiently well by a polynomial of degree  $2N-1$ . Then the integral over  $f(x)$  with respect to a nonnegative weighting function  $w(x)$  can be evaluated exactly with the *Gaussian* quadrature rule

$$\int f(x)w(x)dx = \sum_{n=1}^{N} w_n f(x_n),$$
(16.87)

with properly chosen weights  $w_n$  and points  $x_n$ , not at all depending on  $f(x)$ ; see for example theorem 3.6.12 in Stoer and Bulirsch (1993, p. 153). But how are these weights and points chosen? Consider dividing  $f(x)$  by a very special polynomial  $p_N(x)$  of degree  $N$ , then one can write

$$f(x) = q(x)p_N(x) + r(x).$$
 (16.88)

Both the ratio  $q(x)$  and the residual  $r(x)$  are polynomials of degree not larger than  $N-1$ . If the *n*-th degree polynomials  $p_n(x)$ , for  $n = 0, \ldots, N$ , form an orthogonal basis with respect to the weighting function  $w(x)$ , which means  $p_0(x) = 1$  and

$$\langle p_n | p_m \rangle_w = \int p_n(x) p_m(x) w(x) dx = 0 \tag{16.89}$$

for  $n \neq m$ , then  $q(x)$  can always be represented as

$$q(x) = \sum_{n=0}^{N-1} q_n p_n(x),$$
 (16.90)

for some coefficients  $q_n$ , and the following equalities hold

$$\langle f|w\rangle = \sum_{n=0}^{N-1} q_n \langle p_n|p_N\rangle_w + \langle r|w\rangle = \langle r|w\rangle. \tag{16.91}$$

But from the quadrature rule  $(16.87)$ , we must have

$$\sum_{n=1}^{N} w_n f(x_n) = \sum_{n=1}^{N} w_n r(x_n) = \sum_{n=1}^{N} w_n (f(x_n) - q(x_n) p_N(x_n)), \qquad (16.92)$$

and thus the quadrature points  $x_n$  have to be chosen as the zeros of the polynomial  $p_N(x)$ . Because of the orthogonality of the polynomials  $p_n(x)$  with respect to  $w(x)$ , the weights are determined by the linear system of equations

$$\sum_{n=1}^{N} w_n p_k(x_n) = \begin{cases} \int w(x) dx & \text{for } k = 0\\ 0 & \text{for } 1 \le k < N. \end{cases}$$
 (16.93)

#### 370

16.6

### **Quick calculation 16.14** Can you see why this is true?

The fact that quadrature rules are exact as long as *f*(*x*) is a polynomial of degree not larger than 2*N* − 1 is absolutely remarkable, because it means that we can evaluate an integral over a cubic function by adding just two numbers, provided we know the correct quadrature points and weights.

Let's first focus on an integral over the interval [−1, 1], and take the weighting function *w*(*x*) = 1 √ 1−*x* 2 . The polynomials orthogonal with respect to this weighting function are the *Gauss–Chebyshev*-polynomials. What is special about them is that their weights and zeros are known explicitly,

$$w_n = \frac{\pi}{N} \quad \text{and} \quad x_n = \cos\left(\frac{2n-1}{2N}\pi\right). \tag{16.94}$$

What if there is no weighting function in the integrand? This can be remedied and as it turns out, the weight is modified to account for it. Assume there is only the function *f*(*x*) to be integrated. Then we can write

$$\int_{-1}^{1} f(x)dx = \int_{-1}^{1} \sqrt{1 - x^2} f(x)w(x)dx = \sum_{n=1}^{N} w_n \sqrt{1 - x_n^2} f(x_n).$$
 (16.95)

We have thus obtained a corrected weight, and furthermore, recall that the quadrature points are cosine functions. We can thus use the identity sin<sup>2</sup> *x* + cos<sup>2</sup> *x* = 1 to define the new weight

$$w_n = \frac{\pi}{N} \sin\left(\frac{2n-1}{2N}\pi\right),\tag{16.96}$$

to be used with the quadrature rule

$$\int_{-1}^{1} f(x)dx = \sum_{n=1}^{N} w_n f(x_n), \qquad (16.97)$$

where the quadrature points *x<sup>n</sup>* are still given by (16.94), but the weights are due to (16.96). The only thing left to do is to map our original boundaries of integration [0, *u*max] onto [−1, 1]. To achieve this goal, the transformation *u* = *u*max 2 *x* + *u*max 2 is applied internally, before the quadrature becomes effective. We then obtain

$$\int_{0}^{u_{\text{max}}} f(u) du = \sum_{n=1}^{N} w_{n} f(u_{n}), \qquad (16.98)$$

with

$$w_n = \frac{\pi u_{\text{max}}}{2N} \sin\left(\frac{2n-1}{2N}\pi\right) \quad \text{and} \quad u_n = \frac{u_{\text{max}}}{2} \cos\left(\frac{2n-1}{2N}\pi\right) + \frac{u_{\text{max}}}{2}.$$
 (16.99)

**Quick calculation 16.15** Can you see why the constant factor of the weights has changed?

To apply our quadrature rule, we have to fix the upper bound  $u_{\rm max}$  in a suitable way. First observe that the integral in both pricing formulas  $(16.29)$  and  $(16.34)$  is the same. The integrand is given by

$$f(u) = \frac{\text{Re}\left[e^{iuk}\varphi_0(u-\frac{i}{2})\right]}{u^2 + \frac{1}{4}}.$$
 (16.100)

We are not looking for a precise expression, but for a simple and robust approximation. Thus, let's assume that the annual volatility is approximately constant and given by  $\sigma$ . Then the conditional characteristic function of the associated martingale process is

$$\varphi_t(u) = e^{iuY_t - \frac{1}{2}(iu + u^2)\sigma^2(T - t)}.\t(16.101)$$

We have to evaluate this function for  $t=0$  at the point  $u-\frac{i}{2}$ . The integrand then becomes

$$f(u) = \frac{\text{Re}\left[e^{iuk}e^{-\frac{1}{2}(u^2 + \frac{1}{4})\sigma^2 T}\right]}{u^2 + \frac{1}{4}} = e^{-\frac{1}{2}(u^2 + \frac{1}{4})\sigma^2 T} \cdot \frac{\cos(uk)}{u^2 + \frac{1}{4}}.$$
(16.102)

This is an exponentially decaying function with a damped oscillation superimposed on it. We want to choose  $u_{\text{max}}$  such that  $|f(u_{\text{max}})| \leq \varepsilon$  for a small number  $\varepsilon$ . Observe that the oscillation term in (16.102) is largest for  $u = 0$ . We can thus estimate the desired upper bound by

$$\left| f(u_{\max}) \right| \le 4e^{-\frac{1}{2} \left( u_{\max}^2 + \frac{1}{4} \right) \sigma^2 T} = \varepsilon. \tag{16.103}$$

Of course this estimate is very conservative, but on the other hand, we can be sure that the error we made in assuming volatility to be constant, is very unlikely to have any effect. Solving (16.103) for  $u_{\text{max}}$  yields

$$u_{\text{max}} = \sqrt{\frac{2\log\frac{4}{\varepsilon}}{\sigma^2 T} - \frac{1}{4}}.\tag{16.104}$$

To get an impression of how quickly the integrals in the pricing equations converge, let's do a little computation. Let's assume that the annual volatility is  $\sigma = 25\%$  and the time to expiry is  $T = 1$  year. If we want the approximation error of the integrand to be smaller than  $\varepsilon = 10^{-6}$ , then the desired upper bound is  $u_{\text{max}} \approx 22$ . This is way smaller than infinity.

We have now all necessary tools for computing option prices within the *Heston*model. Of course, we first have to calibrate the parameters to a set of observed plain vanilla options. If this is done, we can valuate any exotic contract with European exercise right, by simulating random paths along the risk-neutral dynamics (16.57) to (16.59). But there is another interesting property of the model we can analyze. If we are able to compute the theoretical call price for every combination of moneyness and time to expiry, we can feed those prices back into the *Black–Scholes*-formula to obtain the implied volatility surface. Figure 16.3 shows the result for the *Heston*-model, calibrated to the DAX data of Chapter 15. Compare this figure to the interpolated

![](_page_20_Figure_1.jpeg)

**Fig. 16.3** 3D Implied volatility surface generated by the *Heston*-model calibrated to DAX data of mid-July 2012

volatility surface in Figure 15.3 on page 335, and also to the GARCH-parametrized surface in Figure 15.6 on page 351. The *Heston*-model captures the long-term skew quite well, but it fails to reproduce the steepness in the short-term smile. In particular the right wing is underestimated. This is typical for stochastic volatility models. The extreme short-term curvature and steepness is due to jump risk, which is not captured by those models. We will eventually encounter models that incorporate jumps, and we will learn what they add to the volatility surfaces in the next chapter. But before we do, let's talk about another stochastic volatility model, very popular with practitioners, because it allows easy fitting of the implied volatility smile.

### **16.7 Implied Volatility in the SABR-Model**

The SABR-model (stochastic alpha-beta-rho) suggested by Hagan et al. (2002) is different from any other model we have encountered so far, because its output is an explicit expression for the implied volatility. This volatility has to be fed into the *Black–Scholes*-formula afterwards to determine the price of the option. You may have observed that we plot the volatility surface with respect to the log-ratio of the strike price of the option and the forward price of the underlying. The reason for this is simple: the bottom of the implied volatility valley, called the backbone, does not drift horizontally along the forward moneyness. Hence, the dynamics in the SABR-model are specified with respect to the forward price. Our usual geometric *Brown*ian motion under the risk-neutral measure *Q* is

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$dS_t = rS_t dt + \sigma S_t dW_t. \tag{16.105}$$

How does this change, if we observe the forward price *F<sup>t</sup>* = *Ste r*(*T*−*t*) instead? From Itô's lemma we have

$$dF_t = rS_t \frac{\partial F}{\partial S} dt + \frac{\partial F}{\partial t} dt + \sigma S_t \frac{\partial F}{\partial S} dW_t + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 F}{\partial S^2} dt$$
  
$$= rF_t dt - rF_t dt + \sigma F_t dW_t$$
  
$$= \sigma F_t dW_t.$$
  
(16.106)

That is, the risk-neutral forward price is driftless. Hagan et al. (2002) studied a more general class of processes, called the CEV-model (constant elasticity of variance). In this model, the forward price has the dynamics

$$dF_t = \sigma_t F_t^{\beta} dW_{1,t} \tag{16.107}$$

$$d\sigma_t = \alpha \sigma_t dW_{2,t},\tag{16.108}$$

with 0 ≤ β ≤ 1 and *E*[*dW*1*dW*2] = ρ*dt*, hence the name SABR-model, because the parameters are α, β, and ρ. Observe that the volatility in (16.108) is not mean reverting. Thus, it can explode and eventually become infinite. The justification for such a framework is that there is not much difference in the volatility smile characteristics, no matter which particular stochastic volatility model is used, and the SABR-model is the simplest of all. The whole point is not to describe the volatility dynamics most realistically, but to provide a simple and efficient framework to parametrize implied volatility for a given time to expiry.

In order to derive an expression for the implied volatility, Hagan et al. (2002) relied heavily on a technique called singular perturbation theory. Perturbation theory is a not completely rigorous branch of mathematics, widely used in physics. Often a problem is solvable under some convenient assumptions. In reality these assumptions may not be exactly true, but close to. If the proper problem can be formulated by adding or multiplying a small quantity ε into the idealized problem, then one can compute a perturbation series to solve the proper problem, too. Perturbation theory is well beyond the scope of this book. We can nevertheless gain some intuition about the basic principles. Assume *y*<sup>0</sup> is the solution of a known problem *f*(*x*). What is the solution *y* to the problem *f*(*x* + ε)? Perturbation theory suggests that the solution can be represented as a *Taylor*-series

$$y = \sum_{n=0}^{\infty} \varepsilon^n y_n. \tag{16.109}$$

The trick that makes this work is that *Taylor*-series are unique in every coefficient. Which means after plugging (16.109) into the problem, we can equate term by term in powers of ε and solve successively. This is best understood by looking at an example.

#### **Example 16.1**

The (positive) solution to the problem *y* = 1 is known to be *y*<sup>0</sup> = 1. What is the solution to the problem

$$y = \sqrt{1.1}$$
,

to the orders ε and ε 2 , respectively?

#### Solution

First realize that we can rewrite the problem as

$$y = \sqrt{1 + \varepsilon}$$
,

where  $\varepsilon = 0.1$  can be considered small compared to the unperturbed problem. Of course we can solve this by simply putting it into a calculator and reading off the result  $v \approx$ 1.0488. But we can do better. To order  $\varepsilon$ , our approximate solution is  $v = v_0 + \varepsilon v_1$ . Plugging this into the pervious equation yields

$$(y_0 + \varepsilon y_1)^2 = y_0^2 + 2\varepsilon y_0 y_1 + \varepsilon^2 y_1^2 = 1 + \varepsilon.$$

We can now order terms according to their power in  $\varepsilon$ , where the  $O(\varepsilon^2)$  term is too small to be considered

$$\begin{array}{rcl} O(\varepsilon^0) & \rightarrow & y_0^2 - 1 = 0 \\ O(\varepsilon^1) & \rightarrow & 2y_0 y_1 - 1 = 0. \end{array}$$

Form this, we can successively deduce that  $y_0 = 1$  and  $y_1 = \frac{1}{2}$ . This is where the prior knowledge of  $y_0$  comes in, it determines that the positive root has to be taken. To order  $\varepsilon$ , we thus obtain  $y = 1 + \frac{\varepsilon}{2} = 1 + 0.05 = 1.05$ .

The solution to order  $\varepsilon^2$  is obtained analogously. It has the form  $y = y_0 + \varepsilon y_1 + \varepsilon^2 y_2$ . Plugging this solution into the original problem yields

$$(y_0 + \varepsilon y_1 + \varepsilon^2 y_2)^2 = 1 + \varepsilon.$$

Collecting all terms of order  $\varepsilon^2$  results in the additional equation

$$O(\varepsilon^2) \quad \to \quad y_1^2 + 2y_0 y_2 = 0.$$

All lower order equations remain intact so we can refine the perturbation series term by term. The new equation yields  $y_2 = -\frac{1}{8}$  and thus the  $O(\varepsilon^2)$  solution becomes  $y =$  $1 + \frac{\varepsilon}{2} - \frac{\varepsilon^2}{9} = 1 + 0.05 - 0.00125 = 1.04875.$ 

Perturbation theory is not a numerical method. Like a good burger, numerical methods make you happy until you learn what went into it. Perturbation theory is a method to obtain approximate analytical solutions. The degree of approximation is only limited by your willingness to compute another term of the series.

Hagan et al. (2002) assume that volatility itself, and the volatility of volatility are both small compared to the forward price. Thus, they substitute  $\sigma_t \to \varepsilon \sigma_t$  and  $\alpha \to \varepsilon \alpha$ in  $(16.107)$  and  $(16.108)$  to obtain

$$dF_t = \varepsilon \sigma_t F_t^{\beta} dW_{1,t} \tag{16.110}$$

$$d\sigma_t = \varepsilon \alpha \sigma_t dW_{2,t},\tag{16.111}$$

with  $\varepsilon = 1$ . This immediately implies that in the unperturbed solution, the forward price  $F_t$  remains constant for all times t. The particular steps in deriving an expression for

the implied volatility are very involved. Therefore, we state only the final result

$$\sigma_{\text{imp.}}(K,T) = \frac{\varepsilon \sigma_t}{(F_t K)^{\frac{1-\beta}{2}} \left(1 + \frac{(1-\beta)^2}{24} \log^2(F_t/K) + \frac{(1-\beta)^4}{1920} \log^4(F_t/K) + \cdots \right)} \cdot \frac{z}{\chi(z)}$$
$$\cdot \left(1 + \left(\frac{(1-\beta)^2}{24} \frac{\sigma_t^2}{(F_t K)^{1-\beta}} + \frac{1}{4} \frac{\beta \rho \alpha \sigma_t}{(F_t K)^{\frac{1-\beta}{2}}} + \frac{2 - 3\rho^2}{24} \alpha^2 \right) \varepsilon^2 (T-t) + \cdots \right). \tag{16.112}$$

with

$$z = \frac{\alpha}{\sigma_t} (F_t K)^{\frac{1-\beta}{2}} \log(F_t/K) \quad \text{and} \quad \chi(z) = \log \left( \frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho} \right). \tag{16.113}$$

Note that the term in the first row of (16.112) is already exact to order  $\varepsilon^2$ , because the next term in the perturbation series is  $O(\varepsilon^3)$ . By the same argument, including this term makes the result exact to order  $\varepsilon^4$ . Typically, the corrections from this term are  $about 1\%$ 

What is especially charming in the SABR-model is that the parameters control more or less isolated characteristics of the implied volatility. Let's for example analyze the role of the parameter  $\beta$ . To this end, let's compute the at-the-money implied volatility  $\sigma_{\text{imp}}(F_t, T)$ . Here we run into a little bit of trouble, because z, as well as  $\chi(z)$  approach zero, as  $K \rightarrow F_t$ . But with the help of l'Hôpital's rule, we have

$$\lim_{z \to 0} \frac{z}{\chi(z)} = \lim_{z \to 0} \frac{1}{\chi'(z)} = 1. \tag{16.114}$$

**Quick calculation 16.16** Check that the last equality holds.

So after plugging back in  $\varepsilon = 1$ , we obtain

$$\sigma_{\text{imp.}}(F_t, T) = \frac{\sigma_t}{F_t^{1-\beta}} + O(\varepsilon^3). \tag{16.115}$$

This is the position of the backbone. Its height for a particular forward price  $F_t$  is determined by  $\sigma_t$ . If  $\beta = 1$ , as usual in our geometric *Brownian* motion framework, the at-the-money implied volatility is given by  $\sigma_t$ . The backbone does not drift vertically, if  $F_t$  changes. For  $\beta < 1$ , the backbone also drifts vertically. To see this, observe that for  $\sigma_s = \sigma_t$  and  $F_s < F_t$ 

$$\sigma_{\text{imp.}}(F_s, T) > \sigma_{\text{imp.}}(F_t, T) \tag{16.116}$$

holds. We can thus deduce that  $\beta$  governs the drift behavior of the backbone, if the forward price  $F_t$  changes in time. Indeed the volatility smile and skew are largely unaffected by the choice of  $\beta$ . Because we are not interested in the dynamics of the implied volatility surface, but only in a snapshot, we choose  $\beta = 1$  in the sequel. Further analysis reveals that the smile is largely controlled by  $\alpha$  and the skew by the correlation coefficient  $\rho$ . Following our convenient notation, labeling today as time  $t = 0$ , we can state the simplified SABR-version

![](_page_24_Figure_1.jpeg)

**Fig. 16.4** 3D Implied volatility surface generated by the SABR-model calibrated to DAX data of mid-July 2012

$$\sigma_{\text{imp.}}(K,T) = \frac{\sigma_0 z}{\chi(z)} \left( 1 + \left( \frac{\rho \alpha \sigma_0}{4} + \frac{2 - 3\rho^2}{24} \alpha^2 \right) T \right) + O(\varepsilon^5),\tag{16.117}$$

with

$$z = \frac{\alpha}{\sigma_0} \log(F_0/K) \quad \text{and} \quad \chi(z) = \log\left(\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}\right). \tag{16.118}$$

What is very convenient about the SABR-model is that it is extraordinarily easy to calibrate to market data. This is due to the widely separated roles of the parameters. The price one has to pay is that the model can only be fitted to single slices in time to expiry. To obtain a representation of the whole implied volatility surface, one has to interpolate between the time slices appropriately. Figure 16.4 shows the result of this procedure for the DAX option data of Chapter 15. The surface is very similar to the one generated by the *Heston*-model, Figure 16.3 on page 373. In particular, the steepness of the smile for short-term contracts is underestimated. This is no surprise, because we have already learned that both the SABR-model and the *Heston*-model do not account for jump risk.

## **16.8 Further Reading**

### • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

A very comprehensive source including the fundamental transform is Lewis (2000). A good summary of stochastic volatility is provided in Wilmott (2006c, chap. 51). Volatility surface issues of the *Heston*-model are discussed in Gatheral (2006, chap. 3). Besides the *Heston*- and SABR-model, there are several other prominent stochastic volatility models. An incomplete list is Hull and White (1987), Scott (1987), and Stein and Stein (1991). A stochastic model for implied volatility itself is provided in Schönbucher (1999).

**16.9 Problems**

- **16.1** Derive the extended *Black–Scholes*-equation for the *Heston*-model.
- **16.2** Show that the fair price of a European plain vanilla call option can be represented as

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$C_0(K,T) = e^{(b-r)T}S_0 - e^{-rT}K(I_1(v) + I_2(v)),$$

where *I*1(*v*) and *I*2(*v*) are the complex line integrals

$$I_1(v) = \frac{1}{2\pi} \int_{iv-\infty}^{iv+\infty} e^{-izk} \varphi_0(-z) \frac{i}{z} dz \quad \text{and} \quad I_2(v) = -\frac{1}{2\pi} \int_{iv-\infty}^{iv+\infty} e^{-izk} \varphi_0(-z) \frac{i}{z-i} dz,$$

evaluated along the contour *v* ∈ (0, 1).

**16.3** Shifting the integration contours to *v* = 0 and *v* = 1, respectively, the complex line integrals in Problem 16.2 become principal value integrals and pick up one half of the associated residue. The result is

$$I_1(v) = \frac{1}{2} + \frac{1}{\pi} \int_0^\infty \text{Re}\left[\frac{e^{iku}\varphi_0(u)}{iu}\right] du$$
$$I_2(v) = \frac{e^k}{2} - \frac{e^k}{\pi} \int_0^\infty \text{Re}\left[\frac{e^{iku}\varphi_0(u-i)}{iu}\right] du,$$

where again *k* = log(*S*0/*K*) + *bT*. Show that the call price can be expressed in a completely analogous form to the generalized *Black–Scholes*-formula.

**16.4** Prove that the payoff function of a protective put position

$$w(x) = \max(e^x, K)$$

has no transformed payoff function *w*ˆ (*z*), regular in a connected strip S*<sup>w</sup>* = { *z* = *u* + *iv* : *v* ∈ (α, β) } .

**16.5** Polynomials, orthogonal with respect to the weighting function *w*(*x*) = 1 in the interval [−1, 1], are called the *Legendre*-polynomials. They are generated by

$$p_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x^2 - 1)^n.$$

Compute the *Legendre*-polynomials up to *N* = 2, as well as the associated quadrature points and weights.

**16.6** Consider the SABR-model with β = 1. Show that the at-the-money smile for *F*<sup>0</sup> = *K* ± δ, with small δ, is symmetric. Use that δ is so small that O(δ 2 ) terms can be neglected.
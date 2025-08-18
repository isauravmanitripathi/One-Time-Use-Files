✖

# **15 Deterministic Volatility**

Abandoning the idea of a constant volatility implies a considerable enrichment of the entire concept of derivative pricing. Whereas stochastic volatility naturally leads to incomplete market models, deterministic volatility preserves market completeness. Such models are very popular with practitioners, because they allow for arbitrage free pricing of standard and exotic contracts, with only few exceptions. Nevertheless, they do not unravel the mechanisms of volatility, but only generate a consistent snapshot of the momentary market expectations.

# **15.1 The Term Structure of Volatility**

The simplest possible relaxation of the *Black–Scholes*-assumption of constant volatility is to allow for a deterministic term structure. Going back to the roots, this means that the underlying follows a geometric *Brown*ian motion with time-dependent volatility

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$dS_t = \mu S_t dt + \sigma(t) S_t dW_t. \tag{15.1}$$

To emphasize that σ(*t*) is a deterministic function of time and not a stochastic process, the time variable is expressed explicitly as function argument and not as subscript. Girsanov's theorem is general enough to hold in this situation, and in switching from the physical probability measure *P* to the risk-neutral measure *Q*, the drift µ is simply replaced by the risk-free interest rate *r*, as before. On the other hand, following our earlier hedging argument, the *Black–Scholes*-equation becomes

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2(t)S\frac{\partial^2 V}{\partial S^2} - rV = 0,$$
(15.2)

and the solution for a European plain vanilla call option is

$$C_t(K,T) = S_t \Phi(d_1) - e^{-r(T-t)} K \Phi(d_2), \tag{15.3}$$

with

$$d_{1} = \frac{\log(S_{t}/K) + r(T-t) + \frac{1}{2} \int_{t}^{T} \sigma^{2}(s) ds}{\sqrt{\int_{t}^{T} \sigma^{2}(s) ds}} \quad \text{and} \quad d_{2} = d_{1} - \sqrt{\int_{t}^{T} \sigma^{2}(s) ds}. \tag{15.4}$$

The resemblance to the original result (13.79) on page 266 is striking. Let us call the volatility σ(*t*), prevailing in our model process (15.1) at time *t*, the **actual volatility**. We can then ask the question: what volatility would be implied, if we valuate the

contract in the standard *Black–Scholes*-framework? Comparing (13.79) and (15.4), we immediately see that this volatility is

$$\sigma_{\text{imp.}}(T) = \sqrt{\frac{1}{T - t} \int_{t}^{T} \sigma^2(s) ds}.$$
 (15.5)

We call this quantity the **implied volatility**. That is, the implied variance is the arithmetic mean over all actual variances. This is a very convenient result, but it does not hold in general. It is only true, if actual volatility is a deterministic function of time and nothing else. We will see at a later point that implied volatility can have a far more intriguing interpretation. The immediate question is: does volatility change over time? If the answer is yes, then the original geometric *Brown*ian motion is an inadequate model for the price process of the underlying. Look at the top row of Figure 15.1, where 20 years of daily prices of the S&P 500 index is indicated on the left. The right side shows an arbitrary simulated path of a geometric *Brown*ian motion, with the same expected growth rate and volatility as found in the data. At first sight it seems to have all the roughness and characteristics of the original price process. It can of course never be a carbon copy of the real process, because it represents only one possible state of the world ω∈ Ω. But in the bottom row of Figure 15.1, the daily returns of both processes are illustrated. Whereas the geometric *Brown*ian motion induces a very homogeneous

![](_page_1_Figure_4.jpeg)

**Fig. 15.1** Price process (top) and returns (bottom) of the S&P 500 stock index (left) and simulated geometric *Brown*ian motion (right)

white noise, the empirical result is quite bizarre. Not only does the volatility obviously change over time, but those changes seem to have a certain pattern. There are large segments, where volatility is moderate, and there are clusters, where volatility is exceedingly high. With a little historic background, you can link times with high volatility to financial market distress. There is the 1998 to 2003 segment of increased volatility, corresponding to a series of catastrophic events. In 1998, Russia defaulted on domestic debt and devalued the ruble. In 2000, the so-called dot-com crash occurred as a result of a bursting technology bubble. Finally, the devastating terrorist attack of September 11, 2001 affected financial markets worldwide, cumulating in the 2002 market downturn. In the 2008 to 2012 segment you can see the consequences of the sub-prime crisis and the European sovereign debt crisis. It is very plausible that market risk is higher in times of financial distress, because it becomes very hard to predict what happens next during a crisis. Because risk is linked to volatility, it is clear that we have to abandon the idea of constant volatility, if we are looking for an adequate and realistic model.

The volatility clustering phenomenon has an empirical side effect, called excess kurtosis. The kurtosis of a distribution is the standardized fourth central moment

$$K = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] = \frac{M_4}{\sigma^4}.\tag{15.6}$$

Equation (2.31) on page 19 tells us that a normal distribution always has kurtosis *K* = 3. If we estimate the kurtosis in financial return time series with daily or weekly frequency, we observe a much higher kurtosis, probably between six and nine. Of course excess kurtosis does not have to be caused by volatility clustering. It simply indicates that the unconditional distribution is not *Gauss*ian, but a distribution with heavier tails. There is another remarkable pattern encoded in the empirical data of financial time series, called the leverage effect. This effect describes the phenomenon that on average the volatility tomorrow, induced by a negative return today, is larger than the one induced by a positive return of the same magnitude. This effect is indeed found in most financial time series and is understood as additional evidence for the risk-averse attitude of most agents. We can thus state three stylized facts of financial return time series:

- excess kurtosis,
- volatility clustering,
- leverage effect.

It is also true that most financial return series, at least with daily or weekly sampling frequency, correspond to noise processes. That is, apart from a fixed expectation value µ, we cannot predict future returns based on our knowledge of present and past returns. Econometrics has found a quite effective way to deal with those stylized facts, which we will study next.

# **15.2 GARCH-Models**

The abbreviation GARCH stands for Generalized AutoRegressive Conditional Heteroscedasticity. The ingenious idea is due to Robert Engle (1982), who in 2003

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

received the Nobel Prize in economics for it, even though its generalized form was introduced by Tim Bollerslev (1986), who was Engle's graduate student at that time. Suppose you do not specify the general return distribution, but only the distribution conditional on your present knowledge. That may sound strange so let's see how it is done. Let *x<sup>t</sup>* = log *S<sup>t</sup>* be the logarithmic (daily) price of an arbitrary security. Then in a GARCH-framework, the dynamics of the logarithmic returns ∆*x<sup>t</sup>* = *x<sup>t</sup>* − *xt*−<sup>1</sup> are given by

$$\Delta x_t = \mu + \epsilon_t = \mu + \sqrt{h_t} z_t, \tag{15.7}$$

where *z<sup>t</sup>* ∼ *N*(0, 1) is independent of everything else. In accordance with tradition in time series analysis, we use small letters for random variables. The trick is that *h<sup>t</sup>* is F*t*−1-predictable. So conditioning on this information, the logarithmic return ∆*x<sup>t</sup>* is normally distributed with expectation µ and variance *h<sup>t</sup>* . We chose the letter *h* to represent the conditional variance mainly for two reasons. First, *h* stands for heteroscedasticity and so it automatically refers to the GARCH-model class. Second, even if *h<sup>t</sup>* has no dynamics, we would still have √ *h<sup>t</sup>* ,σ, because √ *ht* is naturally scaled on a daily basis, whereas σ is usually the volatility per year. The more interesting question is how the dynamics of *h<sup>t</sup>* are defined. In the simplest possible GARCH-model, the variance tomorrow is explained as a weighted arithmetic mean of the current, the past, and the distant future variance

$$h_{t+1} = \alpha \epsilon_t^2 + \beta h_t + \gamma h_\infty. \tag{15.8}$$

*h*<sup>∞</sup> = *E*[*ht*] is also called the stationary variance. It is the quantity you can simply estimate by computing the sample variance of all logarithmic returns.<sup>1</sup>

**Quick calculation 15.1** Can you see why the entire history of the process contributes in the computation of *ht*?

Of course we must have α, β, γ ≥ 0 and α + β + γ = 1. It is customary to introduce a new parameter ω= γ*h*<sup>∞</sup> and to write the GARCH-model as

$$\Delta x_t = \mu + \sqrt{h_t} z_t \tag{15.9}$$

$$h_{t} = \omega + \alpha \epsilon_{t-1}^{2} + \beta h_{t-1}, \qquad (15.10)$$

<sup>1</sup> We defined the GARCH-model such that it is guaranteed to be stationary and ergodic. The latter property ensures that both the time series and the cross-sectional sample moments converge to the same value. Because *z<sup>t</sup>* is independent and standard normally distributed, we have Var[∆*xt*] = *E*[*htz* 2 *t* ] = *E*[*ht*], and the claim follows immediately. In general, GARCH-models form a much broader class of models. We will exclusively analyze the GARCH(1,1)-member of this class.

where of course ϵ*<sup>t</sup>* = √ *htz<sup>t</sup>* with *z<sup>t</sup>* ∼ *N*(0, 1), and the variance equation is now in the typical AR-form. Note that in this parametrization, the stationary variance becomes

$$E[\epsilon_t^2] = h_\infty = \frac{\omega}{1 - \alpha - \beta}.$$
 (15.11)

Let us elaborate on a particular, quite subtle point. It is easy to see that the distribution of ∆*x<sup>t</sup>* , conditional on the information F*t*−<sup>1</sup> is *Gauss*ian, because *h<sup>t</sup>* is F*t*−1-predictable and is thus a known quantity at time *t*. But the unconditional distribution of ∆*x<sup>t</sup>* is far from *Gauss*ian. This might be puzzling so let's compute a characteristic and invariant quantity of a normal distribution, we know well: Its kurtosis. To simplify the computation assume that β = 0, which is the original ARCH-specification of Engle (1982). That makes the stationary variance *E* [ ϵ 2 *t* ] = *h*<sup>∞</sup> =ω/(1 − α). Let's first compute the unconditional fourth moment of ∆*x<sup>t</sup>*

$$M_{4} = E[\epsilon_{t}^{4}] = E[h_{t}^{2}]E[z_{t}^{4}] = 3E[(\omega + \alpha \epsilon_{t-1}^{2})^{2}]$$
  

$$= 3\omega^{2} + 6\frac{\alpha\omega^{2}}{1-\alpha} + 3\alpha^{2}E[\epsilon_{t-1}^{4}]$$
  

$$= \frac{3\omega^{2} + 3\alpha\omega^{2}}{1-\alpha} + 3\alpha^{2}E[\epsilon_{t-1}^{4}]$$
  

$$= \frac{3\omega^{2}(1+\alpha)}{1-\alpha} + 3\alpha^{2}E[\epsilon_{t-1}^{4}],$$
  
(15.12)

where we used that *z<sup>t</sup>* is independent of everything else and thus the expectations factorize. Because we are looking for the unconditional (stationary) fourth moment, we can use that *M*<sup>4</sup> = *E* [ ϵ 4 *t* ] = *E* [ ϵ 4 *t*−1 ] and rearrange (15.12) to obtain

$$M_4 = \frac{\omega^2}{(1-\alpha)^2} \cdot 3 \frac{(1+\alpha)(1-\alpha)}{1-3\alpha^2},\tag{15.13}$$

where we already organized terms in a convenient way. The kurtosis is *K* = *M*4/*h* 2 <sup>∞</sup>, but the first term on the right hand side of (15.13) is already *h* 2 <sup>∞</sup> and thus, we have

$$K = 3\frac{1 - \alpha^2}{1 - 3\alpha^2} \ge 3. \tag{15.14}$$

This is a very neat result, because for α = 0 we are back in a *Gauss*ian framework with *h<sup>t</sup>* =ω. But for 0 < α < 1/ √ 3, we have excess kurtosis, as observed in financial time series.

**Quick calculation 15.2** Verify that for *K* = 9 we have α = 1/2.

One of the most useful properties of GARCH-models is that their expected variance can be computed recursively. Suppose we have fitted a GARCH-model to past return

data, with daily frequency. Departing from *t* = 0, what variance do we expect at an arbitrary future day? Let's start by expressing the expected variance at day *t* in terms of the expected variance at day *t* − 1,

$$E[h_t] = \omega + \alpha E[h_{t-1}]E[z_{t-1}^2] + \beta E[h_{t-1}]$$
  
=  $\omega + (\alpha + \beta)E[h_{t-1}],$  (15.15)

where we have again used the independence of *z<sup>t</sup>* . We can iterate this result backwards right to the beginning to obtain

$$E[h_t] = \omega + \omega(\alpha + \beta) + (\alpha + \beta)^2 E[h_{t-2}]$$
  
$$= \omega \sum_{s=0}^{t-1} (\alpha + \beta)^s + (\alpha + \beta)^t h_0.$$
 (15.16)

Now recognize that the sum in (15.16) is a geometric series and use the definition of the stationary variance (15.11) to obtain

$$E[h_t] = \omega \frac{1 - (\alpha + \beta)^t}{1 - \alpha - \beta} + (\alpha + \beta)^t h_0$$
  
$$= h_{\infty} + (\alpha + \beta)^t (h_0 - h_{\infty}).$$
 (15.17)

That is again a very nice result. Because α + β < 1 has to hold, the initial variance *h*<sup>0</sup> decays exponentially to the stationary variance *h*∞. But we can do even more. Let's compute the average expected variance up to some terminal time *T*

$$\frac{1}{T+1} \sum_{t=0}^{T} E[h_t] = h_{\infty} + \frac{h_0 - h_{\infty}}{T+1} \cdot \sum_{t=0}^{T} (\alpha + \beta)^t$$
$$= h_{\infty} + \frac{h_0 - h_{\infty}}{T+1} \cdot \frac{1 - (\alpha + \beta)^{T+1}}{1 - \alpha - \beta}.$$
(15.18)

Recall that *T* is measured in days in the GARCH-framework. More precisely, time is measured in trading days. If we assume that one year has 252 trading days, we can use this conversion factor to provide a new GARCH-model based formula for the implied volatility of an option

$$\sigma_{\text{imp.}}(T) = \sqrt{252h_{\infty} + \frac{h_0 - h_{\infty}}{T + 1/252} \cdot \frac{1 - (\alpha + \beta)^{252T + 1}}{1 - \alpha - \beta}},\tag{15.19}$$

with *h*<sup>∞</sup> given by (15.11) and *T* now measured in years. This is a most convenient way to provide a term structure for the volatility that is realistically supported by empirical data. Unfortunately, there are two problems not yet accounted for. First, we have used the expected GARCH-variance to provide a volatility term structure, but the variance can deviate substantially from its expected value. Second, so far we have said nothing

about the leverage effect. There are far more effective ways to apply GARCH-models in option pricing.

#### 15.3 **Duan's Option Pricing Model**

In 1995, Jin-Chuan Duan came up with an approach for pricing derivatives, solely relying on a GARCH-model. We will discuss the components of this model, namely the GARCH-equations and the equivalent risk-neutral measure, which was called the locally risk-neutral valuation relationship (LRNVR) by Duan, separately. Let's first make an observation about the variance equation  $(15.10)$  on page 329.

We have already seen two possible specifications, the original ARCH-version ( $\beta = 0$ ), and its generalization. The ARCH-model was already able to generate excess kurtosis as observed in financial time series, but it cannot account for volatility clustering. The GARCH-version can incorporate this stylized fact, by introducing a dependence on past variances. Both versions cannot account for the leverage effect, because  $\epsilon_{i-1}^2$ is completely symmetric with respect to positive and negative random errors of the same magnitude. A surprising side effect of applying Duan's LRNVR-transformation is that the original GARCH-model turns into the nonlinear asymmetric GARCHspecification (NGARCH), introduced by Engle and Ng (1993). In this version the variance has the dynamics

$$h_{t} = \omega + \alpha \left(\epsilon_{t-1} - \sqrt{h_{t-1}}\gamma\right)^{2} + \beta h_{t-1}, \qquad (15.20)$$

with  $\gamma > 0$  and as usual  $\epsilon_{t-1} = \sqrt{h_{t-1}} z_{t-1}$ . To see that this specification indeed accounts for the leverage effect, let us compute the covariance between tomorrow's variance  $h_{t+1}$ and today's innovation  $z_t$ ,

$$\begin{aligned} \text{Cov}[h_{t+1}, z_t] &= E[h_{t+1}z_t] = E\left[\left(\omega + \alpha h_t(z_t - \gamma)^2 + \beta h_t\right)z_t\right] \\ &= E[-2\alpha\gamma h_t z_t^2] = -2\alpha\gamma h_\infty, \end{aligned} \tag{15.21}$$

which is clearly negative. So as claimed, a negative innovation today on average causes a larger volatility tomorrow.

**Quick calculation 15.3** Prove that in the NGARCH-model  $h_{\infty} = \frac{\omega}{1-\alpha(1+\nu^2)-\beta}$  holds.

The GARCH-model used by Duan (1995) is a discrete version of the  $It\hat{o}$ -process for  $x_t = \log S_t$ , where  $S_t$  follows the standard geometric *Brown*ian motion,

$$dx_t = \left(\mu - \frac{1}{2}\sigma^2\right)dt + \sigma dW_t. \tag{15.22}$$

In discretizing this process, Duan made three modifications. First, the time interval was set to  $\Delta t = 1$ , second, the fixed variance  $\sigma^2$  was replaced by the GARCH-variance  $h_t$ ,

and third, the expected daily return was expressed as the sum of a daily risk-free return and a risk premium, proportional to the actual volatility, µ = *r* + λ √ *ht* . The resulting *Duan*-model is thus

$$\Delta x_t = r - \frac{1}{2}h_t + \lambda \sqrt{h_t} + \sqrt{h_t}z_t \qquad (15.23)$$

$$h_t = \omega + \alpha h_{t-1} z_{t-1}^2 + \beta h_{t-1}, \qquad (15.24)$$

where again *z<sup>t</sup>* ∼ *N*(0, 1). Duan concluded that under the risk-neutral measure *Q*, the risk premium has to vanish, and thus he introduced the locally risk-neutral valuation relation (LRNVR)

$$z_t^Q = z_t + \lambda,\tag{15.25}$$

which is nothing else than a discrete version of the *Girsanov*-transformation (14.40) on page 304. Because *z<sup>t</sup>* is unconditionally normally distributed, the term "local" refers to the distribution of ∆*x<sup>t</sup>* , which is only conditionally normal, given the information F*t*−1. This is a mere formality, because the conditioning argument holds successively. Under the locally risk-neutral measure *Q*, the model reads

$$\Delta x_t = r - \frac{1}{2}h_t + \sqrt{h_t}z_t^Q \tag{15.26}$$

$$h_{t} = \omega + \alpha h_{t-1} (z_{t-1}^{Q} - \lambda)^{2} + \beta h_{t-1}, \qquad (15.27)$$

where of course *z Q <sup>t</sup>* ∼ *N*(0, 1) under *Q*.

**Quick calculation 15.4** Show that (15.26) implies *St*−<sup>1</sup> = *e* <sup>−</sup>*<sup>r</sup>E <sup>Q</sup>*[*S<sup>t</sup>* |F*t*−1].

What is especially charming in the *Duan*-model, is that the risk premium can be estimated under the physical measure *P*, and the change to measure *Q* introduces a leverage effect. It is easy to simulate the price process under *Q*, once the model is fitted to the available data under *P*. Thus, an arbitrary derivative can be valuated via Monte Carlo simulation. Figure 15.2 shows one simulated price and return path, driven by a NGARCH-model with parameters fitted to 20 years of S&P 500 data. Compare the characteristics with the real data and the simulated geometric *Brown*ian motion in Figure 15.1 on page 327. The NGARCH-model generates much more realistic path characteristics. We nevertheless have to pay a price. Option valuation with GARCH-models is computationally demanding, because we have to use Monte Carlo methods, and we have to keep track of two processes, *x<sup>t</sup>* and *h<sup>t</sup>* . There is a more efficient approach due to Heston and Nandi (1997, 2000), based on an affine class GARCH-model, we will encounter later. Option valuation with GARCH-models is

![](_page_8_Figure_1.jpeg)

Fig. 15.2 Simulated NGARCH price process (left) and returns (right) – Parameters fitted to S&P 500 data

not mainstream. Although the results are more realistic than in the traditional *Black*-*Scholes*-framework, they are still not entirely satisfactory. One potential reason for this may be the lack of jumps.

#### 15.4 Local Volatility and the *Dupire*-Equation

What is observed in reality is roughly the following: In the short term vanilla prices show a phenomenon called volatility smile. That means options which are roughly at the money  $(S_t = K)$ , have the lowest implied volatility, whereas options both in the money  $(S_t > K)$  and out of the money  $(S_t < K)$  have larger implied volatilities. The criteria for in and out of the money were given for call options here, in case of put options they are reversed. In the long term the volatility smile seems to flatten out and option prices are usually only determined by a skew, where implied volatility is larger when the contract is in the money and smaller if it is out of the money, or vice versa. A typical implied volatility surface is shown in Figure 15.3. In this case the surface was constructed from 466 plain vanilla index options on the "Deutscher Aktienindex" (DAX). The spatial units are provided in terms of inverse logarithmic forward moneyness, where  $F_0 = S_0 e^{rT}$  is the forward price of the underlying. The idea of **local volatility** is to find a deterministic function  $\sigma_{\text{loc.}}(S, t)$ , such that the stochastic process

$$dS_t = \mu S_t dt + \sigma_{\text{loc.}}(S_t, t) S_t dW_t \tag{15.28}$$

induces fair option prices, consistent with the observed implied volatility surface. This is a very subtle idea, even if it seems straightforward. At this point, it is not at all obvious that such a function exists. Furthermore, we have not the slightest clue what local and implied volatility really are in a local volatility setup.

Let's start our discussion with an observation due to Breeden and Litzenberger (1978). Departing from the *Feynman–Kac*-representation for the fair price of a plain vanilla European call option

$$C_t(K,T) = e^{-r(T-t)} E^{\mathcal{Q}} [(S_T - K)^+ | \mathcal{F}_t], \tag{15.29}$$

![](_page_9_Figure_1.jpeg)

**Fig. 15.3** 3D Interpolated implied volatility surface of the DAX at mid-July 2012

we can calculate the first derivative with respect to the exercise price *K*. Even though the payoff function is clearly not differentiable at *S<sup>T</sup>* = *K*, we can confidently assume that the conditional risk-neutral probability density is sufficiently rapidly decreasing, so that we can treat the payoff function as a generalized function. As already shown in Example (13.5) on page 259, the derivative of the maximum function is the *Heaviside*θ-function, and thus we obtain

$$\frac{\partial C_t}{\partial K} = -e^{-r(T-t)} E^Q [\theta(S_T - K)|\mathcal{F}_t]. \tag{15.30}$$

Applying exactly the same arguments again and differentiating one more time yields

$$\frac{\partial^2 C_t}{\partial K^2} = e^{-r(T-t)} E^{\mathcal{Q}} [\delta(S_T - K) | \mathcal{F}_t]. \tag{15.31}$$

But the expectation over the δ-function is an inner product of the δ-function and the conditional risk-neutral probability density function, ⟨δ*K*|*q*(*T*)⟩ = *q*(*K*,*T*), and thus we have

$$q(K,T) = e^{r(T-t)} \frac{\partial^2 C_t}{\partial K^2},\tag{15.32}$$

with initial condition *q*(*K*, *t*) = δ(*K* − *St*). Under local volatility, the risk-neutral probability density function has to obey the *Fokker–Planck*-equation

$$\frac{\partial}{\partial T}q(S,T) = -\frac{\partial}{\partial S}rSq(S,T) + \frac{1}{2}\frac{\partial^2}{\partial S^2}\sigma_{\text{loc.}}^2(S,T)S^2q(S,T)$$
  
=  $A^{\dagger}(S,T)q(S,T),$  (15.33)

where

$$A^{\dagger}(S,T) = -\frac{\partial}{\partial S}rS + \frac{1}{2}\frac{\partial^2}{\partial S^2}\sigma_{\text{loc.}}^2(S,T)S^2$$
(15.34)

is the Fokker-Planck-operator, and the initial condition is  $q(S, t) = \delta(S - S_t)$ . Going back to Equation (15.29) and differentiating with respect to  $T$ , one obtains

$$\begin{split} \frac{\partial C_t}{\partial T} &= -rC_t + e^{-r(T-t)} \int_0^\infty (S-K)^+ \frac{\partial}{\partial T} q(S,T) dS \\ &= -rC_t + e^{-r(T-t)} \int_0^\infty (S-K)^+ A^\dagger(S,T) q(S,T) dS \\ &= -rC_t + e^{-r(T-t)} \int_0^\infty \left( A(S,T)(S-K)^+ \right) q(S,T) dS, \end{split} \tag{15.35}$$

with the *Kolmogorov*-backward-operator

$$A(S,T) = rS\frac{\partial}{\partial S} + \frac{1}{2}\sigma_{\text{loc.}}^2(S,T)S^2\frac{\partial^2}{\partial S^2}.$$
 (15.36)

Using the generalized derivatives  $\frac{\partial}{\partial S}(S-K)^{+} = \theta(S-K)$  and  $\frac{\partial^{2}}{\partial S^{2}}(S-K)^{+} = \delta(S-K)$ , we obtain

$$\begin{split} \frac{\partial C_t}{\partial T} &= -rC_t + re^{-r(T-t)} \int_0^\infty S\theta(S-K)q(S,T)ds \\ &+ \frac{1}{2}\sigma_{\text{loc.}}^2(K,T)K^2 e^{-r(T-t)}q(K,T). \end{split} \tag{15.37}$$

Using that the maximum function can be written as  $(S - K)^{+} = (S - K)\theta(S - K)$ , the integral in  $(15.37)$  becomes

$$E^{\mathcal{Q}}[S_T\theta(S_T-K)|\mathcal{F}_t] = E^{\mathcal{Q}}[(S_T-K)^+|\mathcal{F}_t] + KE^{\mathcal{Q}}[\theta(S_T-K)|\mathcal{F}_t],\tag{15.38}$$

where we have switched back to conditional expectations. Now we have to put some pieces together. Remember that  $q(K,T) = E^{\mathcal{Q}}[\delta(S_T - K)|\mathcal{F}_t]$ , and consider the generalized derivatives (15.30) and (15.31), then we obtain the *Dupire*-equation (Dupire, 1994)

$$\frac{\partial C_t}{\partial T} = -rK \frac{\partial C_t}{\partial K} + \frac{1}{2} \sigma_{\text{loc.}}^2(K, T) K^2 \frac{\partial^2 C_t}{\partial K^2}.$$
 (15.39)

The remarkable thing about this equation is that it grants us immediate access to the local volatility surface by simply rearranging. Suppose today is time  $t = 0$ , then the complete local volatility surface, consistent with all call prices observed today, can be obtained by

$$\sigma_{\text{loc.}}(S,t) = \sqrt{\frac{\left.\frac{\partial C_0}{\partial T}\right|_{T=t} + rS\frac{\partial C_0}{\partial K}\right|_{K=S}}{\left.\frac{1}{2}S^2\frac{\partial^2 C_0}{\partial K^2}\right|_{K=S}}}.$$
(15.40)

Unfortunately, this relation is of rather limited use. If an option is far in or out of the money, we divide a small number by another very small number, which can cause

considerable numerical inaccuracies. What we really want is to express local volatility in terms of implied volatility. But before we come to this point, let's first try to understand what local volatility really is.

The subsequent exposition follows the very elegant argument of Derman and Kani (1998). Suppose the risk-neutral dynamics of the underlying are governed by the stochastic process

$$dS_t = \sigma_{\text{act.}}(S_t, t) S_t dW_t. \tag{15.41}$$

We have set the risk-free interest rate to  $r = 0$ , because we are solely interested in the volatility. The results are unaffected by this simplification. Actual volatility is a function of the random process  $S_t$ , and therefore random itself, but it is still adapted to the filtration  $\mathcal{F}_t$ , generated by  $W_t$ . Formal application of Itô's lemma to the function (S –  $K$ <sup>+</sup> at time  $t = T$  yields

$$d(S_T - K)^{+} = \frac{1}{2}\sigma_{\text{act.}}^2(S_T, T)S_T^2\delta(S_T - K)dT + \sigma_{\text{act.}}(S_T, T)S_T\theta(S_T - K)dW_T. \tag{15.42}$$

Taking conditional expectations and recalling that  $C_l(K,T) = E^Q[(S_T - K)^+|\mathcal{F}_l]$  holds for  $r = 0$ , we can express the dynamics of the call price as

$$dC_t = E^Q \left[ \frac{1}{2} \sigma_{\text{act.}}^2 (S_T, T) S_T^2 \delta(S_T - K) \middle| \mathcal{F}_t \right] dT. \tag{15.43}$$

The conditional expectation of the *Wiener*-term vanishes, because of the defining properties of the  $It\hat{o}$ -integral. Remember that actual volatility is random itself and thus, the expectation is with respect to the joint conditional probability density  $q(\sigma^2, S, T)$ . This joint density can be factorized into the conditional product  $q(\sigma^2|S,T)q(S,T)$  of densities.<sup>2</sup> Now  $(15.43)$  can be written as

$$\begin{split} \frac{\partial C_t}{\partial T} &= \frac{1}{2} \int_0^\infty E^Q [\sigma_{\text{act.}}^2(S_T, T) | \mathcal{F}_{t \to S}] S^2 \delta(S - K) q(S, T) dS \\ &= \frac{1}{2} E^Q [\sigma_{\text{act.}}^2(S_T, T) | \mathcal{F}_{t \to K}] K^2 \frac{\partial^2 C_t}{\partial K^2}, \end{split} \tag{15.44}$$

where in slight abuse of notation  $\mathcal{F}_{t\to K} = \mathcal{F}_t \cap \{S_T = K\}$  represents the information that the joint process starts at  $(S_t, \sigma_{\text{act.}}^2(S_t, t))$  at time *t* and ends at  $(K, \cdot)$  at time *T*. Comparing this result with the *Dupire*-equation (15.39) for  $r = 0$ , we can immediately conclude that

$$\sigma_{\text{loc.}}^2(K,T) = E^{\mathcal{Q}}[\sigma_{\text{act.}}^2(S_T,T)|\mathcal{F}_{t\to K}] \tag{15.45}$$

has to hold. That is, local variance is the risk-neutral expected actual variance, conditional on the underlying to end up precisely at the money.

<sup>&</sup>lt;sup>2</sup> The notation of conditional densities used here is of course far from rigorous, because conditioning is always with respect to a  $\sigma$ -algebra or an event and furthermore, T is not a random variable at all.

#### Implied Volatility and Most Likely Path 15.5

There is an easy and a most challenging answer to the question of what implied volatility truly is. Both answers are useful in a certain sense. The easy one is: Implied volatility is what you get, if you plug an observed option price into the *Black–Scholes*formula and solve for the volatility. This may seem trivial but it is extremely useful in expressing local volatility (15.40), as derived from the *Dupire*-equation, in terms of implied volatility. This is in principle a simple matter, because we only have to use the chain rule. For example the partial derivative of  $C_0$  with respect to the expiry time T becomes

$$\frac{\partial C_0}{\partial T} = \frac{\partial C_{\text{BS}}}{\partial T} + \frac{\partial C_{\text{BS}}}{\partial \sigma_{\text{imp.}}} \frac{\partial \sigma_{\text{imp.}}}{\partial T},\tag{15.46}$$

where  $C_{\text{BS}}$  is the *Black–Scholes*-price with respect to  $\sigma_{\text{imp}}$ . In reality, the computation is extremely tedious and we will only state the final result. The reader is referred for details to Gatheral (2006, p. 11) or van der Kamp (2009, sect. 2.3). For brevity, we drop the subscript "imp." and state the result in terms of  $K$  and  $T$ 

$$\sigma_{\text{loc.}}(K,T) = \sqrt{\frac{\sigma^2 + 2\sigma T \left(\frac{\partial\sigma}{\partial T} + rK\frac{\partial\sigma}{\partial K}\right)}{\left(1 + Kd_1\,\sqrt{T}\frac{\partial\sigma}{\partial K}\right)^2 + K^2\sigma T \left(\frac{\partial^2\sigma}{\partial K^2} - d_1\left(\frac{\partial\sigma}{\partial K}\right)^2\,\sqrt{T}\right)}},\tag{15.47}$$

with

$$d_1 = \frac{\log(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}.$$
 (15.48)

Equipped with this solution, we can in principle use an interpolated implied volatility surface like the one in Figure 15.3, to compute the local volatility at every desired point. If we evaluate (15.47) at  $K = S_t$  and  $T = t$ , the resulting local volatility can be fed straight into a Monte Carlo algorithm to valuate an arbitrary option contract. Of course the partial derivatives depend on the interpolation scheme we use. But that is not a major problem if there are enough traded options. The ultimate problem is that if we come back next week and again fit the implied and local volatility surface, both have changed. That means pricing contracts with forward starting features, like cliquet options for example, with local volatility methods is not a good idea. But besides that, the local volatility surface is a very useful tool for arbitrage free pricing. Now let's move on to the challenging part of the answer.

As before, we will assume without loss of generality that pricing is conducted at time  $t = 0$ . Furthermore, because we are again only interested in volatility, we assume the risk-free interest rate  $r = 0$  to obtain the risk-neutral dynamics (15.41) of the underlying. The results are again not affected by this simplification. The ideas explored in the rest of this section are due to Gatheral (2006, chap. 3), and were made completely rigorous by

a remark of Keller-Ressel and Teichmann (2009). The first step is to define a so-called "forward starting implied volatility," labeled as

$$\sigma_{\text{imp.}}(t, K, T). \tag{15.49}$$

This is the implied volatility we expect to be fed into the *Black–Scholes*-formula to price a plain vanilla contract correctly at time *t*. We will again rely exclusively on the European call option and because the risk-free interest rate is zero, we have

$$C_0(K,T) = E^{\mathcal{Q}}[(S_T - K)^+] = E^{\mathcal{Q}}\left[E^{\mathcal{Q}}[(S_T - K)^+|\mathcal{F}_t]\right] = E^{\mathcal{Q}}[C_t(K,T)].\tag{15.50}$$

The unconditional expectation is of course as always with respect to the information F0. The final risk-neutral expectation in (15.50) is the predicted *Black–Scholes*-price at time *t*, containing the forward starting implied volatility σimp.(*t*, *K*,*T*), based on the information available today at *t* = 0. We can assume that the forward starting implied volatility is a smooth function of *t*, and thus there has to be another deterministic function

$$\sigma^2(t, K, T) = -\frac{\partial}{\partial t} \left( \sigma_{\text{imp.}}^2(t, K, T) \cdot (T - t) \right). \tag{15.51}$$

From this argument, we can see immediately by rearranging and integrating that

$$\sigma_{\text{imp.}}(K,T) = \sigma_{\text{imp.}}(0,K,T) = \sqrt{\frac{1}{T} \int_0^T \sigma^2(t,K,T) dt}.$$
 (15.52)

This is in complete analogy to the case of volatility with pure term structure (15.5) on page 327. The truly remarkable fact is that σ 2 (*t*, *K*,*T*) is also deterministic. We will make considerable efforts to determine this key quantity.

In order to conduct the next step, we need the following observation. In the original *Black–Scholes*-model, there is a neat relation between the vega and the gamma of a European plain vanilla option

$$\frac{\partial V_t}{\partial \sigma} = \sigma (T - t) S_t^2 \frac{\partial^2 V_t}{\partial S^2}.$$
 (15.53)

We used the function *Vt*(*K*,*T*) for the *Black–Scholes*-price to emphasize that this relation holds for call and put options. In our implied volatility framework, however, σimp.(*t*, *K*,*T*) has a partial derivative with respect to *t* and we thus obtain

$$\frac{\partial}{\partial t}C_{t}(K,T) = \frac{\partial C_{t}}{\partial t} + \frac{\partial C_{t}}{\partial \sigma_{\text{imp.}}} \frac{\partial \sigma_{\text{imp.}}}{\partial t}$$
$$= -\frac{1}{2}\sigma_{\text{imp.}}^{2}(t,K,T)S_{t}^{2}\frac{\partial^{2}C_{t}}{\partial S^{2}} + \sigma_{\text{imp.}}(t,K,T)(T-t)S_{t}^{2}\frac{\partial^{2}C_{t}}{\partial S^{2}} \cdot \frac{\partial \sigma_{\text{imp.}}}{\partial t}$$
$$= -\frac{1}{2}\sigma^{2}(t,K,T)S_{t}^{2}\frac{\partial^{2}C_{t}}{\partial S^{2}}, \tag{15.54}$$

where we have used (15.51) in the final step. The first term in the second row is due to the *Black–Scholes*-equation for *r* = 0. On the other hand, applying Itô's lemma, we must have

$$C_T(K,T) - C_0(K,T) = \int_0^T \left( \frac{\partial C_t}{\partial S} dS_t + \frac{\partial C_t}{\partial t} dt + \frac{1}{2} \sigma_{\text{act.}}^2(S_t, t) S_t^2 \frac{\partial^2 C_t}{\partial S^2} dt \right). \tag{15.55}$$

Taking expectations on both sides of  $(15.55)$  with respect to the risk-neutral probability measure  $Q$ , and interchanging the order of integration yields

$$E^{Q}[(S_{T}-K)^{+}] - C_{0}(K,T) = \frac{1}{2} \int_{0}^{T} E^{Q} \left[ \left(\sigma_{\text{act.}}^{2}(S_{t},t) - \sigma^{2}(t,K,T)\right) S_{t}^{2} \frac{\partial^{2} C_{t}}{\partial S^{2}} \right] dt. \quad (15.56)$$

The left hand side of  $(15.56)$  obviously vanishes, because the risk-free interest rate is zero. But that means that the integral on the right hand side has to vanish, too. Furthermore, because  $E^Q[C_t(K,T)] = C_0(K,T)$ , we could have chosen any lower bound of integration  $t \leq T$ . Therefore, it is clear that the integrand itself has to vanish and we obtain

$$\sigma^2(t, K, T) = \frac{E^{\mathcal{Q}}[\sigma_{\text{act.}}^2(S_t, t)S_t^2\Gamma(S_t, t)]}{E^{\mathcal{Q}}[S_t^2\Gamma(S_t, t)]},\tag{15.57}$$

where we have replaced the second derivative of the call price with respect to the price of the underlying by the *Black–Scholes*-gamma,  $\frac{\partial^2 C_t}{\partial S^2} = \Gamma(S_t, t)$ . Note that in the special case of a pure term structure  $\sigma_{\text{act.}}(S_t, t) = \sigma(t)$ , we have

$$\sigma^2(t, K, T) = \frac{\sigma^2(t) E^{\mathcal{Q}}[S_t^2 \Gamma(S_t, t)]}{E^{\mathcal{Q}}[S_t^2 \Gamma(S_t, t)]} = \sigma^2(t). \tag{15.58}$$

It is possible to write  $(15.57)$  in a more elegant way. Following Lee  $(2004)$ , we can define a new family of equivalent probability measures  $G_t$  by the Radon–Nikodymderivatives

$$\frac{dG_t}{dQ} = \frac{S_t^2 \Gamma(S_t, t)}{E^Q [S_t^2 \Gamma(S_t, t)]},\tag{15.59}$$

think of it as of a family of stochastic discount factors, to obtain the representation

$$\sigma^2(t, K, T) = E^{\mathcal{Q}} \left[ \frac{dG_t}{dQ} \sigma^2_{\text{act.}}(S_t, t) \right] = E^{G_t} [\sigma^2_{\text{act.}}(S_t, t)]. \tag{15.60}$$

We can thus express the implied volatility as an average expectation value, with respect to the family of probability measures  $G_t$ ,

$$\sigma_{\text{imp.}}(K,T) = \sqrt{\frac{1}{T} \int_0^T E^{G_t} [\sigma_{\text{act.}}^2(S_t, t)] dt}.$$
 (15.61)

More precisely, implied variance is the average expected actual variance, with respect to a certain time-dependent probability measure  $G_t$ . Although the expression (15.61) is exact, it carries very little intuition about what this average really is.

Let's ask what the conditional probability density function, associated with that mysterious measure family  $G_t$  is. From (15.59) it is easy to see that the desired density has to be

$$g(\sigma^2, S, t) = \frac{S^2 \Gamma(S, t) q(\sigma^2, S, t)}{E^{\mathcal{Q}}[S^2 \Gamma(S, t)]},$$
(15.62)

where  $q(\sigma^2, S, t)$  is the joint risk-neutral probability density, conditional on  $\mathcal{F}_0$ . We can apply the same conditioning argument as before to factorize the new density  $g(\sigma^2, S, t)$ into  $q(\sigma^2|S, t)g(S, t)$ , with

$$g(S,t) = \frac{S^2 \Gamma(S,t) q(S,t)}{E^Q [S^2 \Gamma(S,t)]}.$$
(15.63)

With this factorization, we can go back and reexpress  $(15.60)$  as

$$\sigma^{2}(t, K, T) = \int_{0}^{\infty} E^{\mathcal{Q}} [\sigma_{\text{act.}}^{2}(S_{t}, t) | \mathcal{F}_{0 \to S}] g(S, t) dS$$
  
$$= \int_{0}^{\infty} \sigma_{\text{loc.}}^{2}(S, t) g(S, t) dS.$$
 (15.64)

In the first equality we have again used the notation  $\mathcal{F}_{0\rightarrow S}$  to indicate the information that the joint process originates at  $(S_0, \sigma^2_{\text{act.}}(S_0, 0))$ , and crosses through  $(S, \cdot)$  at time *t*. For the following steps, it is more convenient to switch to logarithmic prices  $x_t = \log S_t$ . This is not a difficult task, but we have to relabel our functions, at least with a subscript referring to x. However, to avoid notational overload, we will be a bit sloppy at this point and suppress the subscript. We then obtain

$$\sigma^2(t, K, T) = \int_{-\infty}^{\infty} \sigma_{\text{loc.}}^2(x, t) g(x, t) dx, \qquad (15.65)$$

with

$$g(x,t) = \frac{e^{2x}\Gamma(x,t)q(x,t)}{E^{\mathcal{Q}}[e^{2x}\Gamma(x,t)]}.$$
(15.66)

Figure 15.4 shows the density function  $g(x, t)$  for a standard European call option with fixed volatility. Obviously it is a kind of bridge density. At  $t = 0$ , the risk-neutral probability density is a  $\delta$ -function, concentrated at  $x_0 = \log S_0$ . At  $t = T$ , the *Black*-*Scholes*-gamma becomes a  $\delta$ -function, concentrated at  $x_T = \log K$ . Furthermore, the density is nearly perfectly symmetric at every time  $t$ . This can be used to expand the local volatility in a clever way. Gatheral (2006, p. 30) suggests to expand around the ridge of the bridge density, which is the most likely path  $\hat{x}_t$  of the logarithmic price process under the measure  $G_t$ . He argues that local volatility does not vary too rapidly over the relevant region of  $x_t$ . Thus, a linear *Taylor*-expansion yields

$$\sigma^{2}(t, K, T) \approx \sigma_{\text{loc.}}^{2}(\hat{x}_{t}, t) + \frac{\partial \sigma_{\text{loc.}}^{2}}{\partial x} \bigg|_{x = \hat{x}_{t}} \int_{-\infty}^{\infty} (x - \hat{x}_{t}) g(x, t) dx$$
$$= \sigma_{\text{loc.}}^{2}(\hat{x}_{t}, t) + \frac{\partial \sigma_{\text{loc.}}^{2}}{\partial x} \bigg|_{x = \hat{x}_{t}} E^{G_{t}}[x_{t} - \hat{x}_{t}]$$
$$\approx \sigma_{\text{loc.}}^{2}(\hat{x}_{t}, t) \tag{15.67}$$

![](_page_16_Figure_1.jpeg)

**Fig. 15.4** 3D Bridge density for call option with *S*<sup>0</sup> = \$100, *K* = \$120, *T*= 1 year, *r* = 5% and σ= 20%

In particular, if we assume that local volatility has negligible curvature at *x*ˆ*<sup>t</sup>* , the expansion is approximately correct up to third order.

**Quick calculation 15.5** Convince yourself that the last argument holds exactly if *g*(*x*, *t*) is symmetric around *x*ˆ*<sup>t</sup>* .

Using (15.67), we can now express implied volatility in terms of local volatility

$$\sigma_{\text{imp.}}(K,T) \approx \sqrt{\frac{1}{T} \int_0^T \sigma_{\text{loc.}}^2(\hat{x}_t, t) dt}.$$
 (15.68)

Thus, implied variance corresponds approximately to the average local variance along the most likely path from *S* = *S*<sup>0</sup> at *t* = 0, to *S* = *K* at *t* =*T*.

There is one subtle point worth discussing briefly. You might ask yourself what exactly the difference is between a local volatility model with diffusion term σloc.(*S<sup>t</sup>* , *t*)*StdW<sup>t</sup>* and the more general case with σact.(*S<sup>t</sup>* , *t*)*StdWt*? Both volatilities are functions of a random variable, at least so it seems. Local volatility is a deterministic function of *S* and *t*, which is supplied with the random price of the underlying *S<sup>t</sup>* at time *t*. That means, if you know *S<sup>t</sup>* , you need no more information to determine σloc.(*S<sup>t</sup>* , *t*). The function σact.(*S<sup>t</sup>* , *t*) on the other hand evolves according to the random path of the underlying. It can only be determined if we know the entire path history of *S<sup>t</sup>* , or in other words, we need the full information F*<sup>t</sup>* . Merely given the price *S<sup>t</sup>* at time *t*, actual volatility generally remains a random variable. A discrete time example for this situation is a GARCH-model. In the next chapter, we will encounter models with stochastic volatility. In this case σact.(*S<sup>t</sup>* , *t*) is not only a function of a random variable, but it is a random function itself. Some authors like to express the explicit randomness by writing σact.(*S<sup>t</sup>* , *t*, ω), but since we did not write *St*(ω) either, we will not do so. The important point is that in this case the volatility at time *t* cannot be

determined by knowing the entire path of *S<sup>t</sup>* . It is indeed not measurable with respect to the information F*<sup>t</sup>* . That is the reason why it is often delicate to handle stochastic volatility models.

#### • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • **15.6 Skew-Based Parametric Representation of the Volatility Surface**

In real markets, prices are not observable with arbitrary precision. There are two major obstacles, more or less obvious. The first one is the bid-offer spread and the second one is the fact that securities are not traded in a synchronized way. That is, all prices except the ones just coming in are obsolete. They belong to another volatility surface, prevailing at the particular moment the price was quoted. As a result of this problem Dumas et al. (1998) found that exhausting all pricing information available in a non- or highparametric way causes overfitting of the volatility surface, and the substantial pricing information is partly lost. Thus, it might be more effective to use a parsimonious parametric model of the volatility surface, and calibrate the few parameters to the available market data. In this section we will discuss the skew-based model suggested by Wilmott (2006c, chap. 50).

Suppose implied volatility is dominated by a nearly linear skew, which is not an unrealistic assumption if the option's time to expiry is not too short. Then a neat model for the implied volatility at *t* = 0 is

$$\sigma_{\text{imp.}}(K,T) = a(T)(K - S_0) + b(T). \tag{15.69}$$

The functions *a*(*T*) and *b*(*T*) are understood as parameters with a term structure over the different expiry time slices we can observe in the market. Usually, a simple linear interpolation scheme is used to fill the gaps. The information needed to determine *a*(*T*) and *b*(*T*) is contained in two special positions, an at-the-money straddle and a risk reversal. Let's see how it works.

Recall that the straddle is a long position of one call and one put with identical exercise price and time to expiry, Π*t*(*K*,*T*) = *Ct*(*K*,*T*) + *Pt*(*K*,*T*). The price of such a straddle is observable in the market. Using put-call parity, the price at time *t* = 0 can be expressed exclusively as a function of the call price

$$\Pi_0^{\text{Std}} = 2C_0(K, T) - S_0 + e^{-rT}K. \n$$
(15.70)

**Quick calculation 15.6** Confirm this result by using (11.17) on page 215.

After some simple rearrangements we can express the call price in terms of observable quantities

$$C_0(K,T) = \frac{1}{2} \left( \Pi_0^{\text{Std}} + S_0 - e^{-rT} K \right). \tag{15.71}$$

Recall that we are interested in an at-the-money straddle, which means  $S_0 = K$ . Use the *Black–Scholes*-formula for the call option and divide by  $S_0$  to obtain

$$\Phi(d_1) - e^{-rT}\Phi(d_2) = \frac{1}{2} \left(\frac{\Pi_0^{\text{Std}}}{S_0} + 1 - e^{-rT}\right). \tag{15.72}$$

Because at the money, the implied volatility (15.69) becomes  $\sigma_{\text{imp}}(K, T) = b(T)$ , we have

$$d_1 = \frac{(r + \frac{1}{2}b^2(T))\sqrt{T}}{b(T)} \quad \text{and} \quad d_2 = d_1 - b(T)\sqrt{T}.$$
 (15.73)

We can solve numerically for  $b(T)$ , because all other quantities in (15.72) are known. If this is done for all available expiry dates  $T_n$ , with  $n = 1, \ldots, N$ , we obtain a term structure  $b(T_n)$ , and we have gathered half the necessary information to parametrize the implied volatility surface.

The second half of the information comes from a risk reversal. A risk reversal is a long call and short put position entered simultaneously, with identical times to expiry and both options out of the money,

$$\Pi_t(K_1, K_2, T) = C_t(K_2, T) - P_t(K_1, T),\n$$
(15.74)

with  $K_1 < S_1 < K_2$ . If both strikes have the same distance to the current price of the underlying, we can write this position at time  $t = 0$  as

$$\Pi_0^{\text{RR}} = C_0(S_0 + \Delta K, T) - P_0(S_0 - \Delta K, T) \n= C_0(S_0 + \Delta K, T) - C_0(S_0 - \Delta K, T) + S_0 - e^{-rT}(S_0 - \Delta K), \n$$
(15.75)

where we have again used put-call parity in the second step. If  $\Delta K$  is small, and it usually is, we can do a linear *Taylor*-expansion of the call price at the money and obtain

$$\Pi_0^{\text{RR}} - S_0(1 - e^{-rT}) = \Delta K \left( 2 \frac{\partial C_0}{\partial K} \Big|_{K = S_0} + 2 \frac{\partial C_0}{\partial \sigma_{\text{imp.}}} \frac{\partial \sigma_{\text{imp.}}}{\partial K} \Big|_{K = S_0} + e^{-rT} \right)\n$$

$$\n= \Delta K \left( e^{-rT} (1 - 2\Phi(d_2)) + 2S_0 \sqrt{T} \phi(d_1) a(T) \right), \n$$
(15.76)

with  $d_1$  and  $d_2$  as in (15.73) and as usual  $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2}$ . Because  $b(T)$  is known from the market price of the straddle, we can solve for  $a(T)$  and obtain

$$a(T) = \frac{\Pi_0^{\text{RR}} - S_0(1 - e^{-rT})}{2\Delta K S_0 \sqrt{T} \phi(d_1)} - e^{-rT} \frac{1 - 2\Phi(d_2)}{2S_0 \sqrt{T} \phi(d_1)}.$$
 (15.77)

Instead of the whole implied volatility surface, we have now only to interpolate the time-dependent parameters between the different expiry time slices. The choice of an interpolation scheme is highly subjective and there is no correct or optimal method.

In this case most of the time a linear interpolation will be sufficient. We thus obtain for *T<sup>n</sup>* ≤ *T* <*Tn*+<sup>1</sup>

$$a(T) = \lambda(T)a(T_n) + (1 - \lambda(T))a(T_{n+1}), \qquad (15.78)$$

with

$$\lambda(T) = \frac{T_{n+1} - T}{T_{n+1} - T_n}.$$
(15.79)

Of course the same holds true for *b*(*T*) in complete analogy.

The only thing left to do is to write down the partial derivatives that go into the *Dupire*-formula (15.47). With the implied volatility model (15.69) and the definition of *a*(*T*) and *b*(*T*) we have

$$\frac{\partial \sigma_{\text{imp.}}}{\partial T} = \frac{(a(T_{n+1}) - a(T_n))(K - S_0) + b(T_{n+1}) - b(T_n)}{T_{n+1} - T_n},\tag{15.80}$$

and

$$\frac{\partial \sigma_{\text{imp.}}}{\partial K} = \frac{a(T_n)(T_{n+1} - T) + a(T_{n+1})(T - T_n)}{T_{n+1} - T_n},\tag{15.81}$$

for *<sup>T</sup><sup>n</sup>* <sup>≤</sup> *<sup>T</sup>*<sup>&</sup>lt; *<sup>T</sup>n*+1. The second partial derivative with respect to *<sup>K</sup>* vanishes, <sup>∂</sup> <sup>2</sup>σimp. <sup>∂</sup>*K*<sup>2</sup> = 0, due to (15.69).

**Quick calculation 15.7** Use (15.78) and (15.79) to confirm the partial derivative ∂σimp. ∂*K* .

# **15.7 Brownian Bridge and GARCH-Parametrization**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • The *Brown*ian bridge is another important stochastic process in finance. It can be derived from *Brown*ian motion by the following definition

$$B_t = \left(1 - \frac{t}{T}\right)b_0 + W_t - \frac{t}{T}(W_T - b_T),\tag{15.82}$$

where the starting point *B*<sup>0</sup> = *b*<sup>0</sup> and the endpoint *B<sup>T</sup>* = *b<sup>T</sup>* is fixed, hence the name *Brown*ian bridge. Of course the process requires anticipating knowledge of *WT*, but it is otherwise a *Gauss*ian random process between *t* = 0 and *t* = *T*. Its moments are easily derived from those of the *Brown*ian motion and one obtains

$$E[B_t] = \left(1 - \frac{t}{T}\right)b_0 + \frac{t}{T}b_T \quad \text{and} \quad \text{Var}[B_t] = t - \frac{t^2}{T}.$$
 (15.83)

**Quick calculation 15.8** Use Cov[*W<sup>s</sup>* , *Wt*] = min(*s*, *t*) to derive the variance of *B<sup>t</sup>* .

![](_page_20_Figure_1.jpeg)

**Fig. 15.5** *Brown*ian motion (left) and *Brown*ian bridge (right) with *b*<sup>0</sup> = 0 and *b*<sup>1</sup> = 1

Some simulated paths of a *Brown*ian motion and the corresponding *Brown*ian bridge are illustrated in Figure 15.5. The bridge process is started at *b*<sup>0</sup> = 0 and is forced to end at *b*<sup>1</sup> = 1. Additionally, the 95 % region of the *Gauss*ian path distribution is indicated. It is immediately clear that such a process is a natural candidate if we try to exploit the most likely path relation of local and implied volatility.

The lesson we learned from Duan's GARCH-model for option pricing is that under the local risk-neutral measure, the logarithmic price process *x<sup>t</sup>* = log *S<sup>t</sup>* has to satisfy

$$x_t = x_{t-1} + r - \frac{1}{2}h_t + \epsilon_t, \qquad (15.84)$$

with ϵ*<sup>t</sup>* = √ *htz<sup>t</sup>* and *z<sup>t</sup>* ∼ *N*(0, 1). Again, recall that *r* is the risk-free daily interest rate. For brevity, let's call the logarithmic exercise price log *K* = *k* so that in the GARCHframework local variance can be written as

$$\sigma_{\text{loc.}}^2(k,T) = E^{\mathcal{Q}}[h_T|\mathcal{F}_{0\to k}].\tag{15.85}$$

Our ultimate goal is to compute this expectation value under a bridge process, starting at (*x*0, *h*0) and terminating at (*k*, · ). To this end, we will give the conditional heteroscedasticity the *Q*-dynamics

$$h_{t} = \omega + \alpha(\epsilon_{t-1} - \gamma)^{2} + \beta h_{t-1}, \qquad (15.86)$$

first proposed by Engle (1990).

**Quick calculation 15.9** Can you see why this specification supports volatility clustering and the leverage effect?

The key in engineering a discrete *Brown*ian bridge process is to replace the *Gauss*ian innovation *z<sup>t</sup>* by a conditional *Gauss*ian random variable ζ*<sup>t</sup>* , with

$$E^{Q}[\zeta_{t}|\mathcal{F}_{t-1}] = \frac{1}{\sqrt{h_{t}}} \left(\frac{k - x_{t-1}}{T - (t-1)} - r\right) + \frac{1}{2}\sqrt{h_{t}},\tag{15.87}$$

and

$$\text{Var}[\zeta_t] = 1 - \frac{1}{T - (t - 1)} = \frac{T - t}{T - (t - 1)}.$$
 (15.88)

Replacing the original random error in (15.84) by ϵ*<sup>t</sup>* = √ *ht*ζ*<sup>t</sup>* generates a bridge process with *E Q* [ *xT*|F<sup>0</sup> ] = *k* and Var*<sup>Q</sup>*[ *xT*|F<sup>0</sup> ] = 0. Let's check that.

As usual, we will call the expectation value with respect to the information F<sup>0</sup> the unconditional expectation and omit the σ-algebra, if there is no potential for confusion. Let's start by computing the unconditional expectation of *x<sup>t</sup>* ,

$$E^{\mathcal{Q}}[x_t] = E^{\mathcal{Q}} \Big[ E^{\mathcal{Q}}[x_t | \mathcal{F}_{t-1}] \Big]$$
  
=  $\frac{1}{T - (t-1)} k + \frac{T - t}{T - (t-1)} E^{\mathcal{Q}}[x_{t-1}].$  (15.89)

In the first step, we used the law of iterated expectations and in the second step, we plugged the bridge error ϵ*<sup>t</sup>* = √ *ht*ζ*<sup>t</sup>* into (15.84) and used the property (15.87). We have now a recursive formula for the unconditional expectation of *x<sup>t</sup>* . Actually (15.89) is only the first element of the recursive pattern

$$E^{Q}[x_{t}] = \frac{n}{T - (t - n)}k + \frac{T - t}{T - (t - n)}E^{Q}[x_{t - n}],\tag{15.90}$$

for *n* ≤ *t*. A proof is straightforward by induction (see Mazzoni, 2015).

**Quick calculation 15.10** Confirm this claim by iterating (15.89) once more.

Ultimately, for *n* = *t* one obtains after trivial rearrangements

$$E^{Q}[x_{t}] = \left(1 - \frac{t}{T}\right)x_{0} + \frac{t}{T}k. \tag{15.91}$$

Compare this result to the expectation of the *Brown*ian bridge in (15.83). In particular it is clear that *E <sup>Q</sup>*[*xT*] = *k*. But to see that we have really created a bridge process by replacing the innovation *z<sup>t</sup>* by ζ*<sup>t</sup>* , we have to show that the variance of *x<sup>T</sup>* vanishes. To this end, one can use the variance decomposition<sup>3</sup>

$$\operatorname{Var}^{\mathcal{Q}}[x_{T}] = \operatorname{Var}^{\mathcal{Q}}\left[E^{\mathcal{Q}}[x_{T}|\mathcal{F}_{T-1}]\right] + E^{\mathcal{Q}}\left[\operatorname{Var}^{\mathcal{Q}}[x_{T}|\mathcal{F}_{T-1}]\right]$$
$$= \operatorname{Var}^{\mathcal{Q}}[k] + E^{\mathcal{Q}}[h_{T} \cdot 0] = 0.$$
(15.92)

Thus, we have indeed constructed a bridge process and we can emphasize this fact by conditioning on the information F0→*k*.

<sup>3</sup> For a random variable *X* and a σ-algebra F*<sup>t</sup>* ⊃ F0, the relation

Var[*X*] = Var[ *E*[*X*|F*t*] ] + *E* [ Var[*X*|F*t*] ]

holds (see for example Greene, 2003, theorem B.4), where unconditional expectations are with respect to F0.

Our ultimate goal is to determine the expectation *E Q* [ *hT*|F0→*<sup>k</sup>* ] , which is the local variance in our GARCH-framework. To accomplish this task it is a useful intermediate step to compute *E <sup>Q</sup>*[ϵ*<sup>t</sup>* |F0→*k*]. From (15.87) we have

$$E^{Q}[\epsilon_{t}|\mathcal{F}_{t-1\to k}] = \frac{k - x_{t-1}}{T - (t-1)} - r + \frac{1}{2}h_{t}.$$
 (15.93)

Taking conditional expectations with respect to F0→*<sup>k</sup>* on both sides and using (15.91) yields

$$E^{Q}[\epsilon_{t}|\mathcal{F}_{0\to k}] = \frac{k - x_{0}}{T} - r + \frac{1}{2}E^{Q}[h_{t}|\mathcal{F}_{0\to k}].$$
 (15.94)

**Quick calculation 15.11** Verify the last equation.

Using the GARCH-model (15.86), we are now in a position to compute the expectation of *h<sup>t</sup>* , conditional on F0→*k*, which means with respect to the bridge error ϵ*<sup>t</sup>* = √ *ht*ζ*<sup>t</sup>* ,

$$E^{\mathcal{Q}}[h_t] = \omega + \alpha E^{\mathcal{Q}} \left[ (\epsilon_{t-1} - \gamma)^2 \right] + \beta E^{\mathcal{Q}}[h_{t-1}]$$
  
$$= \omega + \alpha \text{Var}^{\mathcal{Q}}[\epsilon_{t-1}] + \alpha \left( E^{\mathcal{Q}}[\epsilon_{t-1}] - \gamma \right)^2 + \beta E^{\mathcal{Q}}[h_{t-1}]. \tag{15.95}$$

The conditioning argument was omitted to simplify the notation. We have further used the old trick Var[*X*] = *E* [ *X* 2 ] − *E*[*X*] 2 . It is not easy to compute the variance term in (15.95), but we can expect the variance of the conditional expectation (15.93) to be negligible compared to the variance of ϵ*<sup>t</sup>* itself for most *t* <*T*. Therefore, again using the variance decomposition, we obtain approximately

$$\operatorname{Var}^{\mathcal{Q}}[\epsilon_{t}] \approx E^{\mathcal{Q}}\left[\operatorname{Var}^{\mathcal{Q}}[\epsilon_{t}|\mathcal{F}_{t-1\to k}]\right] = E^{\mathcal{Q}}[h_{t}\operatorname{Var}[\zeta_{t}]]$$
$$= E^{\mathcal{Q}}[h_{t}]\frac{T-t}{T-(t-1)} \approx E^{\mathcal{Q}}[h_{t}].$$
(15.96)

That is, for most *t* < *T*, the relation between the variance of ϵ*<sup>t</sup>* and the expectation of *h<sup>t</sup>* is approximately the same as in the unbridged case, especially if *T* is large. We can now start to put the pieces together. Using (15.94) and (15.96), we can reexpress (15.95) as

$$E^{Q}[h_{t}] = \omega + \alpha E^{Q}[h_{t-1}] + \alpha \left(\eta + \frac{1}{2}E^{Q}[h_{t-1}]\right)^{2} + \beta E^{Q}[h_{t-1}], \qquad (15.97)$$

where the quantity η = *k*−*x*<sup>0</sup> *T* − (*r* + γ) was introduced, and still all expectations are with respect to the information F0→*k*. If we neglect terms of order O(*h* 2 *t* ) and their expectation, respectively, we obtain the recursive expression

$$E^{Q}[h_{t}|\mathcal{F}_{0\to k}] = a + bE^{Q}[h_{t-1}|\mathcal{F}_{0\to k}], \qquad (15.98)$$

with *a* =ω + αη<sup>2</sup> and *b* = α(1 + η) + β. This expression can be easily iterated backwards and for *t* =*T* one obtains

$$E^{Q}[h_{T}|\mathcal{F}_{0\to k}] = a\sum_{t=0}^{T-1} b^{t} + b^{T}h_{0}.$$
 (15.99)

Local volatility in the GARCH-framework is the square root of this expression, where we can additionally use the geometric series representation to simplify the sum on the right hand side

$$\tau_{\text{loc.}}(k,T) = \sqrt{a \cdot \frac{1 - b^T}{1 - b} + b^T h_0},\tag{15.100}$$

with

$$a = \omega + \alpha \eta^2$$
,  $b = \alpha (1 + \eta) + \beta$ , and  $\eta = \frac{k - x_0}{T} - (r + \gamma)$ . (15.101)

This expression makes perfect sense if we analyze the limits. For the short term, we have

$$\lim_{T \to 0} \sigma_{\text{loc.}}^2(k, T) = \begin{cases} h_0 & \text{for } k = x_0\\ \infty & \text{for } k \neq x_0. \end{cases}$$
 (15.102)

For  $|b| < 1$ , local volatility is flat in the limit  $T \rightarrow \infty$ , which means, it does not depend on  $k$  anymore.

To calibrate this simple model for local volatility to an observed implied volatility surface, we can use Gatheral's most likely path approximation. Assume that the most likely path is roughly a straight line in the  $(x, t)$ -plane. This is usually a very reasonable approximation and implied variance becomes

$$\sigma_{\text{imp.}}^2(k,T) = \frac{1}{T} \int_0^T \sigma_{\text{loc.}}^2 \left( \left( 1 - \frac{t}{T} \right) x_0 + \frac{t}{T} k, t \right) dt. \tag{15.103}$$

Translating this idea into our GARCH-framework, the straight line approximation leads to the relation

$$\sigma_{\text{imp.}}^2(k,T) = \frac{1}{T+1} \sum_{t=0}^T \sigma_{\text{loc.}}^2 \left( \left( 1 - \frac{t}{T} \right) x_0 + \frac{t}{T} k, t \right). \tag{15.104}$$

Observe two important points. First, the quantity  $\eta$ , as defined in (15.101), is the only component directly depending on k. Second,  $\eta$  as a function of k and T is invariant under the transformation

$$(k,T) \longrightarrow \left( \left( 1 - \frac{t}{T} \right) x_0 + \frac{t}{T} k, t \right). \tag{15.105}$$

Quick calculation 15.12 Prove this statement.

Using this fact and the definition of local volatility (15.100), implied variance can be written as

$$\sigma_{\text{imp.}}^{2}(k,T) = \frac{1}{T+1} \sum_{t=0}^{T} a \cdot \frac{1-b^{t}}{1-b} + b^{t}h_{0}$$
  
$$= \frac{a}{1-b} + \frac{1}{T+1} \left( h_{0} - \frac{a}{1-b} \right) \sum_{t=0}^{T} b^{t},$$
 (15.106)

with *a*, *b*, and η precisely as in (15.101). We can again use the geometric series formula to obtain the implied volatility in a closed form

$$\sigma_{\text{imp.}}(k,T) = \sqrt{\frac{a}{1-b} + \frac{1}{T+1} \left( h_0 - \frac{a}{1-b} \right) \frac{1-b^{T+1}}{1-b}},\tag{15.107}$$

where *a*, *b*, and η are again defined as in (15.101). Note that the same consistency argument as before applies here. In the limits *T* → 0 and *T* → ∞, implied and local volatility coincide. The only caveat is again that the parameters of the GARCH-model are scaled with respect to daily trading frequencies, whereas naturally, interest rates, volatilities, and times to expiry are given in years. To synchronize both model frameworks, we assume again that one year has 252 trading days and thus, the converted formulas are

$$\sigma_{\text{loc.}}(K,T) = \sqrt{252\left(a \cdot \frac{1 - b^{252T}}{1 - b} + b^{252T}h_0\right)}$$
(15.108)

$$\sigma_{\text{imp.}}(K,T) = \sqrt{\frac{252a}{1-b} + \frac{1}{T+1/252} \left(h_0 - \frac{a}{1-b}\right) \frac{1-b^{252T+1}}{1-b}},\tag{15.109}$$

with

$$a = \omega + \alpha \eta^2$$
,  $b = \alpha (1 + \eta) + \beta$ , and  $\eta = \frac{\log(K/S_0)}{252T} - \left(\frac{r}{252} + \gamma\right)$ . (15.110)

Because implied volatility is completely explicit, it is extraordinarily easy to fit the model to observed market data. Figure 15.6 shows the implied volatility surface calibrated to the DAX data we used earlier. Compare this surface to the nonparametrically interpolated surface in Figure 15.3 on page 335. All key features, like the decaying short-term smile and the long-term skew, are present. Furthermore, once the implied volatility surface is calibrated, one has immediate and explicit access to local volatility without using a complex formula, involving certain derivatives of the implied volatility.

![](_page_25_Figure_1.jpeg)

Fig. 15.6 ED GARCH-parametrized implied volatility surface based on DAX data of mid-July 2012

# **Further Reading**

For many concepts introduced in this chapter, the book of Jim Gatheral (2006) is an indispensable source. A compressed analysis of Dupire's work can be found in Ekstrand (2011, chap. 6). A very accessible introduction to deterministic volatility is Wilmott (2006c, chap. 50) and Hull (2012, chap. 10). For GARCH-models see the original work of Engle (1982) and Bollerslev (1986). A well written introduction is Engle (2001). For a technical treatment with multivariate extensions see McNeil et al. (2005, sect. 4.3 & 4.6). The skew-based parametrization of the volatility surface was introduced in Wilmott (2006c, sect. 50.7–50.11).

# 15.9

15.8

## Problems

15.1 Assume that actual variance has the mean reverting term structure

$$\frac{d\sigma^2(t)}{dt} = \lambda(\sigma^2_{\infty} - \sigma^2(t)),$$

where  $\sigma_{\infty}^2$  is the stationary variance and  $\sigma^2(0) = \sigma_0^2$ . What is the implied volatility of an option at time  $t = 0$ ?

**15.2** The solution to Problem  $15.1$  is

$$\sigma_{\text{imp.}}(T) = \sqrt{\sigma_{\infty}^2 + \frac{1 - e^{-\lambda T}}{\lambda T} (\sigma_0^2 - \sigma_{\infty}^2)}.$$

Show that this result is consistent in the limit  $T \rightarrow \infty$  and  $T \rightarrow 0$ .

**15.3** Show that the kurtosis in an ordinary  $GARCH(1,1)$ -model is

$$K = 3 \frac{1 - (\alpha + \beta)^2}{1 - 2\alpha^2 - (\alpha + \beta)^2}.$$

**15.4** The *Duan*-model is a modified version of the GARCH-in-mean specification

$$\Delta x_t = \mu + \lambda h_t + \epsilon_t,$$

where again ϵ*<sup>t</sup>* = √ *htz<sup>t</sup>* , and *z<sup>t</sup>* ∼ *N*(0, 1). Show that under the asymmetric variance dynamics

$$h_t = \omega + \alpha(\epsilon_{t-1} - \gamma)^2 + \beta h_{t-1},$$

the logarithmic return process ∆*x<sup>t</sup>* does not constitute a noise process, which means Cov[∆*xt*+1, ϵ*t*] , 0.

**15.5** The *Heston–Nandi*-model for option pricing (Heston and Nandi, 1997, 2000) is specified as

$$\begin{aligned} \Delta x_t &= r + \lambda h_t + \sqrt{h_t z_t} \\ h_t &= \omega + \alpha \left( z_{t-1} - \gamma \sqrt{h_{t-1}} \right)^2 + \beta h_{t-1}, \end{aligned}$$

where *z<sup>t</sup>* is again independent and identically standard normally distributed. In going from probability measure *P* to *Q*, the model can be written in unchanged algebraic form but with the substitutions λ → λ *<sup>Q</sup>*, *z<sup>t</sup>* → *z Q t* , and γ → γ *<sup>Q</sup>*. What are the modified quantities λ *<sup>Q</sup>*, *z Q t* , and γ *Q*?
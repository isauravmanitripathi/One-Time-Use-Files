# **Normal Inverse Gaussian** Model

The normal inverse Gaussian (NIG) process is an example of a Lévy process (see Lévy Processes) with no Brownian component.

We first discuss the NIG distribution and its main properties. The NIG process can be constructed either as process with NIG increments or, alternatively, defined via random time change of Brownian motion using the inverse Gaussian process to determine time. Further, we present the NIG market model and show how one can price European options under this model. Option pricing can be done using the NIG density function, the NIG Lévy characteristics, or the NIG characteristic function.

## The Normal Inverse Gaussian Distribution

The NIG distribution with parameters  $\alpha > 0, -\alpha <$  $\beta < \alpha$ , and  $\delta > 0$  has characteristic function (see [1])

$$\phi(u;\alpha,\beta,\delta) = \exp\left\{-\delta\left(\sqrt{\alpha^2 - (\beta + iu)^2} - \sqrt{\alpha^2 - \beta^2}\right)\right\} \tag{1}$$

We shall denote this distribution by  $NIG(\alpha, \beta, \delta)$ . The distribution is so named due to the fact that  $NIG(\alpha, \beta, \delta)$  is a variance-mean mixture of a normal distribution with the inverse Gaussian as the mixing distribution. It follows immediately from expression (1) that this distribution is infinitely divisible. The distribution is defined on the whole real line and has the density function

$$f(x; \alpha, \beta, \delta) = \alpha \delta \pi^{-1} \exp\left\{\delta \sqrt{\alpha^2 - \beta^2} + \beta x\right\}$$
$$K_1(\alpha \sqrt{\delta^2 + x^2}) \left(\sqrt{\delta^2 + x^2}\right)^{-1}, \quad x \in R \tag{2}$$

where  $K_1$  is the modified Bessel function of thirdorder and index 1. If a random variable  $X$  follows an  $NIG(\alpha, \beta, \delta)$  distribution and  $c > 0$ , then  $cX$ is  $NIG(\alpha/c, \beta/c, c\delta)$ -distributed. Further, if  $X \sim$  $NIG(\alpha, \beta, \delta_1)$  is independent of  $Y \sim NIG(\alpha, \beta, \delta_2)$ , then  $X + Y \sim NIG(\alpha, \beta, \delta_1 + \delta_2)$ . If  $\beta = 0$ , the distribution is symmetric. This can easily be seen from the characteristics of the NIG distribution given in Table 1.

Note that the NIG distribution is a special case of generalized hyperbolic distribution, and it can approximate most hyperbolic distributions very closely. In modeling, the NIG distribution can describe observations with considerably heavier tail behavior than the log linear rate of decrease that characterizes the hyperbolic shape (see [2]). The NIG distribution has semiheavy tails (see  $[3]$ )

$$f(x; \alpha, \beta, \delta) \sim const. |x|^{-3/2}$$
  
exp $\{-\alpha |x| + \beta x\}, \quad x \to \pm \infty$ 

## The Normal Inverse Gaussian Process

We define the NIG process

$$X^{(\text{NIG})} = \{X_t^{(\text{NIG})}, t \ge 0\} \tag{3}$$

as the Lévy process with stationary and independent NIG-distributed increments, where  $X_0^{(\text{NIG})} = 0$  with probability 1. To be precise,  $X_t^{(\text{NIG})}$  follows a NIG( $\alpha$ ,  $\beta$ ,  $\delta t$ ) law.

The Lévy measure of the NIG process is given by

$$\nu_{\text{NIG}}(\mathrm{d}x) = \delta\alpha\pi^{-1}\exp\{\beta x\}K_1(\alpha|x|)(|x|)^{-1}\mathrm{d}x\tag{4}$$

An NIG process has no Brownian component and its Lévy triplet is given by  $[\gamma, 0, \nu_{\text{NIG}}(dx)]$ , where

$$\gamma = 2\delta\alpha\pi^{-1} \int_0^1 \sinh(\beta x) K_1(\alpha x) \mathrm{d}x \qquad (5)$$

The NIG Lévy process may alternatively be represented via random time change of Brownian motion, using the inverse Gaussian (IG) process to determine time, as

$$X_t^{\text{NIG}} = \beta \delta^2 I_t + \delta W_{I_t} \tag{6}$$

where  $W = \{W_t, t \ge 0\}$  is a standard Brownian motion and  $I = \{I_t, t \ge 0\}$  is an IG process with parameters  $a = 1$  and  $b = \delta \sqrt{\alpha^2 - \beta^2}$ .

|          | $\text{NIG}(\alpha, \beta, \delta)$                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------|
| Mean     | $\delta\beta\left(\alpha^2-\beta^2\right)^{-1/2}$                                                                |
| Variance | $\alpha^2 \delta \left(\alpha^2 - \beta^2\right)^{-3/2}$                                                         |
| Skewness | $3\beta\alpha^{-1}\delta^{-1}(\alpha^2-\beta^2)^{-1/4}$                                                          |
| Kurtosis | $3\left(1 + \left(\alpha^2 + 4\beta^2\right)\delta^{-1}\alpha^{-2}\left(\alpha^2 - \beta^2\right)^{-1/2}\right)$ |

**Table 1** Mean, variance, skewness, and kurtosis of the normal inverse Gaussian distribution

# The NIG Model

The NIG model belongs to the class of exponential Lévy models (see **Time-changed Lévy Process**). Consider a market with a riskless asset (the bond), with a price process given by  $b_t = \exp{rt}$ , and one risky asset (the stock or index). The model for the risky asset is

$$S_t = S_0 \exp\{X_t^{\text{(NIG)}}\}\tag{7}$$

where the log returns  $\log (S_{t+s}/S_t)$  follow the *NIG*  $(\alpha, \beta, \delta s)$  distribution (i.e., the distribution of increments of length  $s$  of the NIG process).

## **Equivalent Martingale Measure**

Pricing financial derivatives requires that we work under an equivalent martingale measure. We present here two ways to attain equivalent martingale measures for the discounted price process  $\exp(-(r$  $q(t)S_t$ ,  $t > 0$ , where r is the risk-free continuously compounded interest rate and  $q$  is the continuously compounded dividend yield.

One can find at least one equivalent martingale measure  $O$  using the Esscher transform (see [6]). For the NIG model, the Esscher transform equivalent martingale measure follows an *NIG*( $\alpha, \theta^* + \beta, \delta$ ) law (see [12]), where  $\theta^*$  is the solution of the equation

$$r - q = \delta \left( \sqrt{\alpha^2 - (\beta + \theta)^2} - \sqrt{\alpha^2 - (\beta + \theta + 1)^2} \right)$$
(8)

Another way to obtain an equivalent martingale measure  $Q$  is by mean-correcting the exponential of the  $NIG(\alpha, \beta, \delta)$  process, that is, introducing the distribution  $NIG(\alpha, \beta, \delta, m)$  with the characteristic function

$$\phi(u;\alpha,\beta,\delta,m) = \phi(u;\alpha,\beta,\delta) \exp\{\mathrm{i}u m\} \qquad (9)$$

where

$$m = r - q + \delta \left( \sqrt{\alpha^2 - (\beta + 1)^2} - \sqrt{\alpha^2 - \beta^2} \right)$$
(10)

and  $\phi(u; \alpha, \beta, \delta)$  is defined by expression (1).

# **Pricing of European Options**

Given our NIG market model, we focus now on the pricing of European options whose payoffs are functions of the terminal asset value only. Denote the payoff of the option at its time of expiry  $T$  by  $G(S_T)$  and let  $F(X_T) = G(S_T)$ 

#### Pricing through Density Function

For a European call option with strike price  $K$  and time to expiration  $T$ , the value  $V_0$  at time 0 is given by the expectation of the payoff under the martingale measure  $O$ . If we take for  $O$  the Esscher transform equivalent martingale measure, the value at time  $0$  is given by

$$V_{0} = \exp\{-qT\}S_{0} \int_{c}^{\infty} f_{T}^{(\theta^{*}+1)}(x) dx$$
$$-\exp\{-rT\}K \int_{c}^{\infty} f_{T}^{(\theta^{*})}(x) dx \qquad (11)$$

where  $c = \ln(K/S_0)$ ,  $f_T^{(\theta^*)}(x)$  is the density function of the *NIG*( $\alpha, \theta^* + \beta, \delta$ ) distribution. Similar formulas can be derived for other derivatives with a payoff function that depends only on the terminal value at time  $t = T$ .

#### Pricing through the Lévy Characteristics

Another way to find the value  $V_t = V(t, X_t)$  at time  $t$  is by solving a partial integro-differential

equation (see Partial Integro-differential Equations (**PIDEs**). If  $V(t, x) \in C^{1,2}$  then the function  $V(t, x)$ solves

$$rV(t,x) = \gamma \frac{\partial}{\partial x} V(t,x) + \frac{\partial}{\partial t} V(t,x)$$
$$+ \int_{-\infty}^{+\infty} \left( V(t,x+y) - V(t,x) \right.$$
$$- y \frac{\partial}{\partial x} V(t,x) \left. \right) v^{\mathcal{Q}}(\mathrm{d}y)$$
$$V(T,x) = F(x) \tag{12}$$

where  $[\gamma, 0, \nu^Q(\mathrm{d}y)]$  is the Lévy triplet of the NIG process under the risk-neutral measure  $O$ .

#### Pricing through the Characteristic Functions

Pricing can also be done by using the characteristic function [4] (see Fourier Transform). Let  $\alpha$  be a positive constant such that the  $\alpha$ th moment of the stock price exists, then the value of the option is given by

$$V_{0} = \frac{\exp\{-\alpha \log(K)\}}{\pi}$$
$$\times \int_{0}^{+\infty} \exp\{-\mathrm{i}v \log(K)\}\varrho(v) \, \mathrm{d}v \quad (13)$$

where

$$\varrho(v) = \frac{\exp\{-rT\}E\left[\exp\{\mathrm{i}(v - (\alpha + 1)\mathrm{i})\log(S_T)\}\right]}{\alpha^2 + \alpha - v^2 + \mathrm{i}(2\alpha + 1)v}$$
$$= \frac{\exp\{-rT\}\varphi(v - (\alpha + 1)\mathrm{i})}{\alpha^2 + \alpha - v^2 + \mathrm{i}(2\alpha + 1)v} \tag{14}$$

and

$$\varphi(u) = E \left[ \exp\{ \mathrm{i}u \log(S_T) \} \right] \tag{15}$$

Other methods for the valuation of European options by applying characteristic functions can be found in [7] and [8].

# **Monte Carlo Simulations**

One can make use of the representation (6) to simulate an NIG process. In such a way, a sample path of the NIG is obtained by sampling a standard Brownian motion and an IG process. We refer to [5] for the details on the generation of an IG random number.

# Origin

The NIG distribution was introduced in [1]. The potential applicability of the NIG distribution and Lévy process for the modeling and analysis of statistical data from turbulence and finance is discussed in [2] and [3]. See also  $[9-11]$  for the application of the NIG distribution in modeling logarithmic asset returns.

## References

- [1] Barndorff-Nielsen, O.E. (1995). Normal Inverse Gaussian Distributions and the Modelling of Stock Returns, Research Report No. 300, Department of Theoretical Statistics, Aarhus University.
- Barndorff-Nielsen, O.E. (1997). Normal inverse Gaus-[2] sian distributions and stochastic volatility modelling, Scandinavian Journal  $of$ *Statistics*  $24(1),$  $1 - 13.$
- [3] Barndorff-Nielsen, O.E. (1998). Processes of normal inverse Gaussian type, Finance and Stochastics 2,  $41 - 68$
- [4] Carr, P. & Madan, D. (1998). Option valuation using the fast Fourier transform, Journal of Computational Finance 2, 61-73.
- Devroye, L. (1986). Non-Uniform Random Variate Gen-[5] eration, Springer.
- [6] Gerber, H.U. & Shiu, E.S.W. (1994). Option pricing by Esscher-transforms, Transactions of the Society of Actuaries 46, 99-191.
- [7] Lee, R.W. (2004). Option pricing by transform methods: extensions, unification, and error control, Journal of Computational Finance  $7(3)$ ,  $50-86$ .
- [8] Raible, S. (2000). Lévy Processes in Finance: Theory, Numerics, and Empirical Facts. PhD thesis, University of Freiburg, Freiburg.
- Rydberg, T. (1996). The Normal Inverse Gaussian [9] *Lévy Process: Simulations and Approximation*, Research Report No. 344, Department of Theoretical Statistics, Aarhus University.
- [10] Rydberg, T. (1996). *Generalized Hyperbolic Diffusions* with Applications Towards Finance. Research Report

No. 342, Department of Theoretical Statistics, Aarhus University.

- [11] Rydberg, T. (1997). A note on the existence of unique equivalent martingale measures in a Markovian setting, *Finance and Stochastics* **1**, 251–257.
- [12] Schoutens, W. (2003). *L´evy Processes in Finance— Pricing Financial Derivatives*, John Wiley & Sons, Chichester.

**Related Articles**

**Exponential Levy Models ´** ; **Fourier Transform**; **Partial Integro-differential Equations (PIDEs)**.

> HENRIK JONSSON ¨ , VIKTORIYA MASOL & WIM SCHOUTENS
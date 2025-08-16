# **Monte Carlo Greeks**

Monte Carlo simulation (see Monte Carlo Simulation) allows not only to compute option prices but can also be used to estimate their sensitivity parameters (delta, gamma, vega, etc.). The baseline estimator, the one which is to be improved, is known as the res*imulation estimator*. Resimulation consists of simply rerunning the simulation (using the same sequence of pseudorandom numbers) after perturbing the parameter or variable of interest. The corresponding estimator is then taken as the change in the value of the derivative divided by the magnitude of the perturbation. The purpose of most of the sophisticated methods that are discussed is primarily that resimulation can be very demanding computationally, while the desired information is in some way already contained in the original simulation data and can be extracted with much more modest amounts of computation than with resimulation. The focus of this article is on the two main such techniques, known as the pathwise and likelihood ratio methods.

The standard integration, or expectation, that represents the value of a derivative takes the form

$$V = \int \pi(S)\psi(S) \, \mathrm{d}S \tag{1}$$

where  $\pi$  ( $\bullet$ ) represents the payoff function and  $\psi$  ( $\bullet$ ) is the probability density of the underlying. The pathwise estimator is based on how the relevant parameter functionally enters into the payoff, whereas the likelihood ratio estimator is based on how the relevant parameter enters into the density function of the underlying(s), given the appropriate change of variable. We specialize this in what follows by assuming that normal variates are the drivers for all price changes and by including a vector of parameters  $\alpha$ , which may represent the initial prices of the underlying securities or rates, volatilities, time to expiration, dividend rates, and so on. In what follows, we give the specifics of the computation of these methods and give some examples of each.

#### **Pathwise Method**

The pathwise estimator is obtained with

$$V = \int \pi [S(z,\alpha)] \varphi(z) \, \mathrm{d}z \tag{2}$$

where  $\varphi(z)$  is the standard normal density. The desired sensitivities are then

$$\frac{\mathrm{d}V}{\mathrm{d}\alpha} = \frac{\mathrm{d}}{\mathrm{d}\alpha} \left\{ \int \pi [S(z,\alpha)] \varphi(z) \,\mathrm{d}z \right\} \tag{3}$$

or, exchanging the differentiation and integral

$$\frac{\mathrm{d}V}{\mathrm{d}\alpha} = \int \frac{\mathrm{d}}{\mathrm{d}\alpha} \left( \pi [S(z,\alpha)] \right) \varphi(z) \, \mathrm{d}z \tag{4}$$

The corresponding (unbiased) pathwise estimator can then be computed as

$$\left\{\frac{\mathrm{d}V}{\mathrm{d}\alpha}\right\}_{P} = \frac{1}{N} \sum_{i=1}^{N} \frac{\mathrm{d}}{\mathrm{d}\alpha} \left(\pi \left[S^{i}(z_{i}, \alpha)\right]\right) \qquad (5)$$

where the summation is taken over  $N$  simulation paths indexed by *i* and the  $z_i$  are independent and identically distributed standard normal variates. As an application of the pathwise methodology, we consider computing an estimate of vega for a European call option under the Black-Scholes model where

$$dS_t = S_t [(r - \delta) dt + \sigma dB_t]$$
 (6)

and  $S_t$  is the underlying asset price at time t, r is the domestic interest rate,  $\delta$  is the dividend rate or foreign interest rate,  $\sigma$  is the volatility, and  $B_t$  is standard Brownian motion. A European call option with expiration  $T$  and strike price  $K$  has value equal to

$$V = E\left[e^{-rT}\left(S_T - K\right)^+\right] \tag{7}$$

where  $E(\bullet)$  is the risk-neutral expectation operator. In the Black-Scholes model we have

$$S_T = S_0 \exp\left[\left(r - \delta - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}Z\right] \quad (8)$$

where  $Z$  is a realization of a standard normal variate. Therefore

$$\frac{\mathrm{d}S_T}{\mathrm{d}\sigma} = S_T \left( -\sigma T + \sqrt{T}Z \right)$$
$$= \frac{S_T}{\sigma} \left[ \ln \left( S_T / S_0 \right) - \left( r - \delta + \frac{\sigma^2}{2} \right) T \right] \tag{9}$$

Now we simply apply the chain rule

$$\frac{\mathrm{d}V}{\mathrm{d}\sigma} = E \left[ \frac{\mathrm{d}\pi}{\mathrm{d}S_T} \frac{\mathrm{d}S_T}{\mathrm{d}\sigma} \right] \tag{10}$$

where

$$\frac{\mathrm{d}\pi}{\mathrm{d}S_T} = \mathrm{e}^{-rT}I\left(S_T > K\right) \tag{11}$$

and  $I(\bullet)$  is the indicator function that takes on the value  $1$  if the argument is true and  $0$  otherwise. That is, the call payoff responds one-to-one with the underlying at expiration provided that the option finishes in-the-money. We then replace the expectation with a summation, as before, to obtain the pathwise estimator

$$\left\{\frac{\mathrm{d}V}{\mathrm{d}\sigma}\right\}_{P} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{e}^{-rT} \mathbb{1} \left(S_{T}^{i} > K\right) \frac{S_{T}^{i}}{\sigma}$$
$$\times \left[\ln\left(S_{T}^{i}/S_{0}^{i}\right) - \left(r - \delta + \frac{\sigma^{2}}{2}\right)T\right] \tag{12}$$

### Likelihood Ratio Method

For the likelihood ratio method, we perform a change of variables such that the dependence on  $\alpha$  in the integrand is put into the density function *via* 

$$\frac{\mathrm{d}V}{\mathrm{d}\alpha} = \int \pi \left( S \right) \frac{\mathrm{d}}{\mathrm{d}\alpha} \varphi(S;\alpha) \, \mathrm{d}S \tag{13}$$

or

$$\frac{\mathrm{d}V}{\mathrm{d}\alpha} = \int \pi \left( S \right) \frac{\frac{\mathrm{d}}{\mathrm{d}\alpha} \varphi(S;\alpha)}{\varphi(S;\alpha)} \varphi(S;\alpha) \, \mathrm{d}S \tag{14}$$

In this form, the calculation resembles the estimation of the price of a derivative with payoff

$$\chi(S;\alpha) \equiv \pi(S)\omega(S;\alpha) \tag{15}$$

where

$$\omega \equiv \frac{\frac{\mathrm{d}}{\mathrm{d}\alpha}\varphi(S;\alpha)}{\varphi(S;\alpha)}\tag{16}$$

so that we have

$$\frac{\mathrm{d}V}{\mathrm{d}\alpha} = \int \chi(S;\alpha) \varphi(S,\alpha) \,\mathrm{d}S \tag{17}$$

As with the pathwise method, we can convert this into a discrete sum suitable for a Monte Carlo implementation to obtain an unbiased estimator of

$$\left\{\frac{\mathrm{d}V}{\mathrm{d}\alpha}\right\}_{L} = \frac{1}{N} \sum_{i=1}^{N} \chi\left(S_{i}\left(z_{i}\right); \alpha\right) \tag{18}$$

In order to illustrate this technique, we again consider the vega calculation. For the normal density we get

$$\omega = \frac{\mathrm{d}}{\mathrm{d}\alpha} \varphi(S;\alpha) \tag{19}$$

$$=\frac{\ln\left(x/S_0\right) - \left(r - \delta - \sigma^2/2\right)T}{S_0\sigma^2T} \qquad (20)$$

and therefore the likelihood ratio estimator is

$$\left\{ \frac{\mathrm{d}V}{\mathrm{d}\sigma} \right\}_{L} = \sum_{i=1}^{N} \mathrm{e}^{-rT} \left( S_{T}^{i} \left( z_{i} \right) - K \right)^{+} \times \left[ \frac{\ln \left( x / S_{0} \right) - \left( r - \delta - \sigma^{2} / 2 \right) T}{S_{0} \sigma^{2} T} \right]$$
(21)

#### Comments

The interchange of the differentiation and integral operators that both the pathwise and likelihood ratio methods entail requires smoothness in the payoff functions and density functions, respectively. As financial derivative payoffs are often not smooth while densities generally are, the likelihood ratio method is more advantageous. For example, the call option payoff is not differentiable in the underlying asset price. The problem with the likelihood ratio method, however, is that the parameter of interest may not appear in the density function even after transformations are considered, although this is a fairly rare occurrence. For programming systems, a very significant advantage of the likelihood ratio method is that it can be coded in a modular way in that prior knowledge of the payoff is not required as made clear by equations  $(15-17)$ .

It should be noted that these methods can also be applied to path-dependent payoffs (which can complicate the application of the pathwise method) as well as non-Gaussian cases (which can complicate the application of the likelihood ratio method).

It may be mentioned that there are other methods, such as the equivalent entropy projection and Malliavin calculus approaches. The equivalent entropy projection method, instead of perturbing the parameters of interest, involves perturbing the probabilities of the simulated paths. The Malliavin calculus approach (*see* **Sensitivity Computations: Integration by Parts**) is a more elaborate or general version of, but arguably not superior, to the likelihood ratio method [1].

## **References**

[1] Chen, N. & Glasserman, P. (2007). Malliavin Greeks without Malliavin calculus, *Stochastic Processes and their Applications* **117**, 1723.

## **Further Reading**

Avellaneda, M. & Gamba, R. (2001). Conquering the Greeks in Monte Carlo: Efficient Calculation of the Market Sensitivities and Hedge Ratios of Financial Assets by Direct Numerical Simulation in *Quantitative Analysis in Financial Markets*, M. Avellaneda, ed., World Scientific, 336–364, Vol. III, www.math.nyu.edu/faculty/avellane/Conquering TheGreeks. pdf.

- Broadie, M. & Glasserman, P. (1996). Estimating security price derivatives using simulation, *Management Science* **42**(2), 269–285.
- Dupire, B. (ed) (1998). *Monte Carlo: Methodologies and Applications for Pricing and Risk Management*, Risk Publications.
- Fournie, E., Lasry, J.M., Lebuchoux, J., Lions, P.L. & Touzi, N. (1999). Applications of Malliavin Calculus to Monte Carlo methods in finance, *Finance and Stochastics* **3**(4), 391–412.
- Jackel, P. (2002). ¨ *Monte Carlo methods in finance*, John Wiley & Sons.
- Jackel, P. (2005). ¨ *More Likely than Not*, www.jaeckel.org.

## **Related Articles**

**Delta Hedging**; **Gamma Hedging**; **Monte Carlo Simulation**; **Monte Carlo Simulation for Stochastic Differential Equations**; **Sensitivity Computations: Integration by Parts**; **Stochastic Differential Equations: Scenario Simulation**; **Variance Reduction**;

MICHAEL CURRAN
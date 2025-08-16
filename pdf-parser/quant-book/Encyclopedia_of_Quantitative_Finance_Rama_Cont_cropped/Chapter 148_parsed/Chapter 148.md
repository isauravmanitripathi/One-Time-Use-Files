# **Constant Elasticity of** Variance (CEV) Diffusion Model

## The CEV Process

The constant elasticity of variance (CEV) model is a one-dimensional diffusion process that solves a stochastic differential equation (SDE)

$$dS_t = \mu S_t dt + aS_t^{\beta+1} dB_t \tag{1}$$

with the instantaneous volatility  $\sigma(S) = aS^{\beta}$  specified to be a power function of the underlying spot price. The model has been introduced by Cox [7] as one of the early alternative processes to the geometric Brownian motion to model asset prices. Here  $\beta$  is the elasticity parameter of the local volatility,  $d\sigma/dS = \beta \sigma/S$ , and *a* is the volatility scale parameter. For  $\beta = 0$ , the CEV model reduces to the constant volatility geometric Brownian motion process employed in the Black, Scholes, and Merton model. When  $\beta = -1$ , the volatility specification is that of Bachelier (the asset price has the constant diffusion coefficient, while the logarithm of the asset price has the  $a/S$  volatility). For  $\beta = -1/2$  the model reduces to the square-root model of Cox and Ross [8].

Cox [7] originally studied the case  $\beta < 0$  for which the volatility is a decreasing function of the asset price. This specification captures the leverage effect in the equity markets: the stock price volatility increases as the stock price declines. The result of this inverse relationship between the price and volatility is the implied volatility skew exhibited by options prices in the CEV model with negative elasticity. The elasticity parameter  $\beta$  controls the steepness of the skew (the larger the  $|\beta|$ , the steeper the skew), while the scale parameter  $a$  fixes the at-the-money volatility level. This ability to capture the skew has made the CEV model popular in equity options markets.

Emanuel and MacBeth [14] extended Cox's analysis to the positive elasticity case  $\beta > 0$ , where the asset price volatility is an increasing function of the asset price. The driftless process with  $\mu = 0$  and with positive  $\beta$  is a strict local martingale. It has been applied to modeling commodity prices that exhibit increasing implied volatility skews with the volatility

increasing with the strike price, but care should be taken when working with this model (see the discussion below).

The CEV diffusion has the following boundary characterization (see, e.g., [4] for Feller's boundary classification for one-dimensional diffusions). For  $-1/2 < \beta < 0$ , the origin is an exit boundary, and the process is killed the first time it hits the origin. For  $\beta < -1/2$ , the origin is a regular boundary point. The SDE  $(1)$  does not uniquely specify the diffusion process, and a boundary condition is needed at the origin. In the CEV model, it is specified as a killing boundary. Thus, the CEV process with  $\beta < 0$  naturally incorporates the possibility of bankruptcy—the stock price can hit zero with positive probability, at which time the bankruptcy occurs. For  $\beta > 0$ , the origin is an inaccessible natural boundary.

## Reduction to Bessel Processes, Transition Density, and Probability of Default

The CEV process is analytically tractable. Its transition probability density and cumulative distribution function are known in closed form.<sup>a</sup> It is closely related to Bessel processes and inherits their analytical tractability. The CEV process with drift ( $\mu \neq 0$ ) is obtained from the process without drift ( $\mu = 0$ ) via a scale and time change:

$$S_{t}^{(\mu)} = e^{\mu t} S_{\tau(t)}^{(0)}, \ \tau(t) = \frac{\left(e^{2\mu\beta t} - 1\right)}{2\mu\beta} \qquad (2)$$

Let  $\left\{R_t^{(\nu)}, t \ge 0\right\}$  be a Bessel process of index  $\nu$ .<br>Recall that for  $\nu \ge 0$ , zero is an unattainable entrance boundary. For  $v \le -1$ , zero is an exit boundary. For  $\nu \in (-1, 0)$ , zero is a regular boundary. In our application, we specify zero as a killing boundary to kill the process at the first hitting time of zero (see, e.g., [4, pp. 133–134], for a summary of Bessel processes). Before the first hitting time of zero, the CEV process without drift can be represented as a power of a Bessel process:

$$S_t^{(0)} = \left(a|\beta|R_t^{(\nu)}\right)^{-\frac{1}{\beta}}\tag{3}$$

where  $\nu = 1/(2\beta)$ .

The CEV transition density is obtained from the well-known expression for the transition density of the Bessel process (see [4, p. 115, 21, p. 446]). For the driftless process, it is given by

$$p_{(0)}(S_0, S_t; t) = \frac{S_t^{-2\beta - 3/2} S_0^{1/2}}{a^2 |\beta| t} I_{|\nu|} \left(\frac{S_0^{-\beta} S_t^{-\beta}}{a^2 \beta^2 t}\right) \times \exp\left(-\frac{S_0^{-2\beta} + S_t^{-2\beta}}{2a^2 \beta^2 t}\right) \quad (4)$$

where  $I_{\nu}$  is the modified Bessel function of the first kind of order  $\nu$ . From equation (2), the transition density with drift is obtained from the density equa- $(4)$  according to

$$p_{(\mu)}(S_0, S_t; t) = e^{-\mu t} p_{(0)}(S_0, e^{-\mu t} S_t; \tau(t))$$
(5)

The density  $(5)$  was originally obtained by Cox  $[7]$ for  $\beta < 0$  and by Emanuel and MacBeth [14] for  $\beta > 0$  on the basis of the result due to Feller [15].

For  $\beta$  < 0, in addition to the continuous transition density, we also have a positive probability for the process started at  $S_0$  at time zero to hit zero by time  $t \ge 0$  (probability of default or bankruptcy) that is given explicitly by

$$G\left(|\nu|, \frac{\mu S_0^{-2\beta}}{a^2 \beta \left(e^{2\mu\beta t} - 1\right)}\right) \tag{6}$$

where  $G(v,x) = (1/\Gamma(v)) \int_x^{\infty} u^{v-1} e^{-u} du$  is the complementary Gamma distribution function. This expression can be obtained by integrating the continuous density  $(5)$  from zero to infinity and observing that the result is less than one, that is, the density is defective. The defect is equal to the probability mass at zero equation  $(6)$ .

While killing the process at zero is desirable for stock price modeling, it may be undesirable in other contexts, where one would prefer the process that stays strictly positive (e.g., in stock index models). A regularized version of the CEV process that never hits zero has been constructed by Andersen and Andreasen [1] (see also [9]). The positive probability of hitting zero comes from the explosion of instantaneous volatility as the process falls toward zero. The regularized version of the CEV process fixes a small value  $\epsilon > 0$ . For  $S > \epsilon$ , the volatility is according to the CEV specification. For  $S \leq \epsilon$ , the volatility is fixed at the constant level  $a\epsilon^{\beta}$ . We thus have a sequence of regularized strictly positive processes indexed by  $\epsilon$  that converge to the CEV process in the limit  $\epsilon \to 0$ .

The CEV process with  $\beta > 0$  can similarly be regularized to prevent the volatility explosion as the process tends to infinity by picking a large value  $\mathcal{E} > 0$  and fixing the volatility above  $\mathcal{E}$  to equal  $a\mathcal{E}^{\beta}$ . The regularized processes with  $\mu = 0$  are true martingales, as opposed to the failure of the martingale property for the driftless CEV process with  $\beta > 0$  and  $\mu = 0$ , which is only a strict local martingale. The failure of the martingale property for the nonregularized process with  $\beta > 0$  can be explicitly illustrated by computing the expectation (using the transition density  $(5)$ ):

$$\mathbb{E}[S_t] = e^{\mu t} S_0 \left( 1 - G\left(\nu, \frac{\mu S_0^{-2\beta}}{a^2 \beta \left(e^{2\mu\beta t} - 1\right)}\right) \right) \tag{7}$$

## **CEV Options Pricing**

The closed-form CEV call option pricing formula with strike  $K$ , time to expiration  $T$ , and the initial asset price  $S$  can be obtained in closed form by integrating the call payoff with the risk-neutral CEV density (5) with the risk-neutral drift  $\mu = r - q$  (r is the risk-free interest rate and  $q$  is the dividend yield). The result can be expressed in terms of the complementary noncentral chi-square distribution function  $Q(z; v, k)$  ([7] for  $\beta < 0$ , [14] for  $\beta > 0$ ; see also [11, 22]):

$$C(S; K, T) = e^{-rT} \mathbb{E} \left[ (S_T - K)^+ \right]$$

$$= \begin{cases} e^{-qT} S Q \left( \xi; 2\nu, y_0 \right) & \beta > 0 \\ -e^{-rT} K \left( 1 - Q \left( y_0; 2(1+\nu), \xi \right) \right), \\ e^{-qT} S Q \left( y_0; 2(1+|\nu|), \xi \right) & \beta < 0 \\ -e^{-rT} K \left( 1 - Q \left( \xi; 2|\nu|, y_0 \right) \right), \end{cases}$$
(8)

where

$$\xi = \frac{2\mu S^{-2\beta}}{a^2 \beta \left(e^{2\mu\beta T} - 1\right)}, \ \ y_0 = \frac{2\mu K^{-2\beta}}{a^2 \beta \left(1 - e^{-2\mu\beta T}\right)} \ \ (9)$$

and  $S = S_0$  is the initial asset price at time zero. The price of the put option is obtained from the put-call parity relationship:

$$P(S; K, T) = C(S; K, T) + Ke^{-rT} - Se^{-qT} \quad (10)$$

The complementary noncentral chi-square distribution function can be expressed as the series of complementary Gamma distribution functions ([22, pp. 214]):

$$Q(z; v, k) = \sum_{n=0}^{\infty} e^{-k/2} \frac{(k/2)^n}{\Gamma(n+1)} G\left(n + \frac{v}{2}, \frac{z}{2}\right)$$
(11)

for  $k, z > 0$ . Further efficient numerical methods to compute the noncentral chi-square cumulative distribution function (CDF) can be found in  $[3, 12,$ 13, 221.

The first passage time problem for the CEV diffusion can be solved analytically and, hence, barrier and lookback options can be priced analytically under the CEV process. Davydov and Linetsky [9, 10] obtained the analytical expressions for the Laplace transforms of single- and double-barrier and lookback options pricing formulas in time to expiration. Davydov and Linetsky [10] and Linetsky [18] inverted the Laplace transforms for barrier options and lookback options in terms of eigenfunction expansions, respectively.

Other types of options under the CEV process, such as American options, require numerical treatment. The pricing partial differential equation (PDE) for European options reads as follows:

$$\frac{a^2}{2}S^{2\beta+2}\frac{\partial^2 V}{\partial S^2} + (r-q)S\frac{\partial V}{\partial S} + \frac{\partial V}{\partial t} = rV \quad (12)$$

The early exercise can be dealt with in the same way as for other diffusion models via dynamic programming, free boundary PDE formulations, or variational inequality formulations.

#### Jump-to-Default Extended CEV Model

While the CEV process can hit zero and, as a result, the CEV equity model includes the positive probability of bankruptcy, the term structure of credit spreads in the CEV model is such that the instantaneous credit spread vanishes. There is no element of surprise—the event of default is a hitting time. Moreover, the probability of default is too small for practical applications of modeling stocks of firms other than the highest rated investment grades. Carr and Linetsky [6] extend the CEV model by allowing a jump to default to occur from a positive stock price. They introduce a default intensity that is an affine function of the instantaneous variance:

$$\lambda(S) = b + c\sigma^2(S) = b + ca^2 S^{2\beta} \tag{13}$$

where  $b \ge 0$  is the constant part of the default intensity and  $c \ge 0$  is the sensitivity of the default intensity to the instantaneous variance. The predefault stock price follows a diffusion process solving the SDE:

$$dS_t = \left[\mu + \lambda(S_t)\right] S_t dt + a S_t^{\beta+1} dB_t \tag{14}$$

The addition of the default intensity in the drift compensates for the jump to default and makes the process with  $\mu = 0$  a martingale. The diffusion process with the modified drift  $(14)$  and killed at the rate (13) is called jump-to-default extended constant elasticity of variance (JDCEV) process. In the JDCEV model, the stock price evolves according to equation  $(14)$  until a jump to default arrives, at which time the stock price drops to zero and equity becomes worthless. The jump to default time has the intensity (13).

The JDCEV model can be reduced to Bessel processes similar to the standard CEV model. Consequently, it is also analytically tractable. Closed-form pricing formulas for call and put options and the probability of default can be found in [6]. The first passage time problem for the JDCEV process and the related problem of pricing equity default swaps are solved in [20]. Atlan and Leblanc [2] and Campi *et al.* [5] investigate related applications of the  $CEV$ model to hybrid credit-equity modeling.

#### **Volatility Skews and Credit Spreads**

Figure  $1(a)$  illustrates the shapes of the term structure of zero-coupon credit spreads in the CEV and JDCEV models, assuming zero recovery. The credit spread curves start at the instantaneous credit spread equal to the default intensity  $b + c\sigma_*^2$  ( $\sigma_*$  is the volatility at a reference level  $S^*$ ).<sup>b</sup> The instantaneous credit spreads for the CEV model vanish, while they are positive for the JDCEV model. Figure  $1(b)$  plots the Black-Scholes implied volatility against the strike price in the CEV and JDCEV models (we calculate the implied volatility by equating the price of an option under the Black-Scholes model to the corresponding option price under the (JD)CEV model). One can observe the decreasing and convex implied

![](_page_3_Figure_1.jpeg)

**Figure 1** (a) Term structures of credit spreads. Parameter values: *S* = *S*<sup>∗</sup> = 50, *σ*<sup>∗</sup> = 0*.*2, *β* = −1*/*2*,* −1*,* −2*,* −3, *r* = 0*.*05, *q* = 0. JDCEV: *b* = 0*.*02 and *c* = 1*/*2. CEV: *b* = 0 and *c* = 0. (b) Implied volatility skews. Parameter values: *S* = *S*<sup>∗</sup> = 50, *σ*<sup>∗</sup> = 0*.*2, *r* = 0*.*05, *q* = 0. For JDCEV model: *b* = 0*.*02, *c* = 1*/*2 and *β* = −1, the times to expiration are *T* = 0*.*25*,* 0*.*5*,* 1*,* 5 years. For CEV model: *b* = *c* = 0 , *β* = −1*,* −2 and times to expiration are *T* = 0*.*25*,* 5. Implied volatilities are plotted against the strike price

volatility skew with implied volatilities increasing for lower strikes, as the local volatility and the default intensity both increase as the stock price declines. The volatility elasticity *β* controls the slope of the skew in the CEV model. The slope of the skew in the JDCEV model is steeper and is controlled by *β*, as well as the default intensity parameters *b* and *c*.

#### Implied Volatility and the SABR model

By using singular perturbation techniques, Hagan and Woodward [17] obtained explicit asymptotic formulas for the Black-Scholes implied volatility  $\sigma_{\text{BS}}$ of European calls and puts on an asset whose forward price  $F(t)$  follows the CEV dynamics, that is,  $\mathrm{d}F_t = aF_t^{\beta+1}\,\mathrm{d}B_t,$ 

$$\sigma_{\rm BS} = a f_{\rm av}^{\beta} \left\{ 1 - \frac{\beta \left(\beta + 3\right)}{24} \left( \frac{F_0 - K}{f_{\rm av}} \right)^2 + \frac{\beta^2}{24} a^2 \tau f_{\rm av}^{2\beta} + \cdots \right\} \tag{15}$$

where  $\tau$  is time to expiration,  $f_{\text{av}} = (F_0 + K)/2$ and  $F_0$  is today's forward price (Hagan and Woodward's  $\beta$  is equal to our  $\beta + 1$ ). This asymptotics for the implied volatility approximates the exact CEV-implied volatilities well when the ratio  $F_0/K$ is not too far from one and when  $K$  and  $F_0$  are far away from zero. The accuracy tends to deteriorate when the values are close to zero since this asymptotic approximation does not take into account the killing boundary condition at zero.

Hagan et al. [16] introduced the SABR model, which is a CEV model with stochastic volatility. More precisely, the volatility scale parameter  $a$  is made stochastic, so that the forward asset price follows the dynamics:

$$dF_t = a_t F_t^{\beta+1} dB_t^{(1)} \quad \text{and}$$
  
$$da_t = \eta a_t dB_t^{(2)} \tag{16}$$

where  $dB_t^{(1)}, dB_t^{(2)} = \rho dt$ . Hagan *et al.* derive the asymptotic expression for the implied volatility in the SABR model.

# Introducing Jumps and Stochastic Volatility into the CEV Model

Mendoza *et al.* [19] introduce jumps and stochastic volatility into the JDCEV model by time changing the JDCEV process. Lévy subordinator time changes introduce state-dependent jumps into the process, while absolutely continuous time changes introduce stochastic volatility. The result is a flexible family of models that exhibit the leverage effect, default

intensity linked to the stock price volatility, jumps, and stochastic volatility. These models inherit the analytical tractability of the CEV and JDCEV models as long as the Laplace transform of the timechange process is analytically tractable. The stochastic volatility version of the CEV model obtained in this approach is different from the SABR model in two respects. The advantage of the time-change approach is that it preserves the analytical tractability for more realistic choices for the stochastic volatility process, such as the Cox-Ingersoll-Rand (CIR) process with mean-reversion. Another advantage is that jumps, including the jump to default, can also be incorporated. The weakness is that it is hard to incorporate the correlation between the price and volatility.

#### **End Notes**

<sup>a.</sup>In this article we present the results for the CEV model with constant parameters. We note that the process remains analytically tractable when  $\mu$  and  $a$  are taken to be deterministic functions of time [6].

<sup>b.</sup>It is convenient to parameterize the local volatility function as  $\sigma(S) = aS^{\beta} = \sigma_*(S/S^*)^{\beta}$  so that at some reference spot price level  $S = S^*$  (e.g., the at-the-money level at the time of model calibration) the volatility takes the reference value,  $\sigma(S^*) = \sigma_*$ . In the example presented here, the reference level is taken to equal the initial spot price level,  $S^* = S_0$ , and the volatility scale parameter is  $a = \sigma_*/(S_0^\beta).$ 

#### Acknowledgments

This research was supported by the National Science Foundation under grant DMS-0802720.

## References

- Andersen, L. & Andreasen, J. (2000). Volatility skew [1] and extensions of the LIBOR market model, Applied Mathematical Finance 7, 1-32.
- Atlan, M. & Leblanc, B. (2005). Hybrid equity-credit [2] modelling, Risk Magazine 18, 8.
- [3] Benton, D. & Krishnamoorthy, K. (2003). Computing discrete mixtures of continuous distributions: noncentral chi-square, noncentral  $t$  and the distribution of the square of the sample multiple correlation coefficient, Computational Statistics and Data Analysis 43, 249-267.

## **6 Constant Elasticity of Variance (CEV) Diffusion Model**

- [4] Borodin, A. & Salminen, P. (2002). *Handbook of Brownian Motion: Facts and Formulae*, Probability and Its Applications, 2nd rev Edition, Birkhauser Verlag AG.
- [5] Campi, L., Sbuelz, A. & Polbennikov, S. (2008). Systematic equity-based credit risk: A CEV model with jump to default, *Journal of Economic Dynamics and Control* **33**, 93–108.
- [6] Carr, P. & Linetsky, V. (2006). A jump to default extended CEV model: an application of Bessel processes, *Finance and Stochastics* **10**, 303–330.
- [7] Cox, J.C. (1975, 1996). Notes on option pricing I: constant elasticity of variance diffusions, *Reprinted in The Journal of Portfolio Management* **23**, 15–17.
- [8] Cox, J.C. & Ross, S.A. (1976). The valuation of options for alternative stochastic processes, *Journal of Financial Economics* **3**, 145–166.
- [9] Davydov, D. & Linetsky, V. (2001). Pricing and hedging path-dependent options under the CEV process, *Management Science* **47**, 949–965.
- [10] Davydov, D. & Linetsky, V. (2003). Pricing options on scalar DIFFUSIONS: an eigenfunction expansion approach, *Operations Research* **51**, 185–209.
- [11] Delbaen, F. & Shirakawa, H. (2002). A note of option pricing for constant elasticity of variance model, *Asia-Pacific Financial Markets* **9**, 85–99.
- [12] Ding, C.G. (1992). Computing the non-central *χ*<sup>2</sup> distribution function, *Applied Statistics* **41**, 478–482.
- [13] Dyrting, S. (2004). Evaluating the noncentral chi-square distribution for the Cox-Ingersoll-Ross process, *Computational Economics* **24**, 35–50.

- [14] Emanuel, D.C. & MacBeth, J.D. (1982). Further results on the constant elasticity of variance call option pricing model, *The Journal of Financial and Quantitative Analysis* **17**, 533–554.
- [15] Feller, W. (1951). Two singular diffusion problems, *The Annals of Mathematics* **54**, 173–182.
- [16] Hagan, P.S., Kumar, D., Lesniewski, A.S. & Woodward, D.E. (2002). Managing smile risk, *Wilmott Magazine* **1**, 84–108.
- [17] Hagan, P. & Woodward, D. (1999). Equivalent black volatilities, *Applied Mathematical Finance* **6**, 147–157.
- [18] Linetsky, V. (2004). Lookback options and diffusion hitting times: a spectral expansion approach, *Finance and Stochastics* **8**, 343–371.
- [19] Mendoza, R., Carr, P. & Linetsky, V. (2007). *Time Changed Markov Processes in Credit-Equity Modeling*, *Mathematical Finance*, to appear.
- [20] Mendoza, R. & Linetsky, V. (2008). *Equity Default Swaps under the Jump-to-Default Extended CEV Model*. *Working paper*.
- [21] Revuz, D. & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, Grundlehren Der Mathematischen Wissenschaften, Springer.
- [22] Schroder, M. (1989). Computing the constant elasticity of variance option pricing formula, *The Journal of Finance* **44**, 211–219.

VADIM LINETSKY & RAFAEL MENDOZA
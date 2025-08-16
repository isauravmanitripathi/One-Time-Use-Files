# **Exponential Lévy Models**

Exponential Lévy models generalize the classical Black and Scholes model by allowing the stock prices to jump while preserving the independence and stationarity of returns. There are ample reasons for introducing jumps in financial modeling. First, asset prices exhibit jumps, and the associated risks cannot be handled within continuous-path models. Second, the well-documented phenomenon of implied volatility smile in option markets shows that the risk-neutral returns are non-Gaussian and leptokurtic, all the more so for short maturities, a clear indication of the presence of jumps. In continuous-path models, the law of returns for shorter maturities becomes closer to the Gaussian law, whereas in reality and in models with jumps, returns actually become less Gaussian as the horizon becomes shorter. Finally, jump processes correspond to genuinely incomplete markets, whereas all continuous-path models are either complete or can be made so with a small number of additional assets. This fundamental incompleteness makes it possible to carry out a rigorous analysis of the hedging errors in discontinuous models and find ways to improve the hedging performance using additional instruments such as liquid European options.

#### Lévy Processes

Lévy processes (see Fundamental Theorem of Asset **Pricing**) [1, 3, 17] are stochastic processes with stationary and independent increments. The only Lévy process with continuous trajectories is the Brownian motion with drift; all others have paths with discontinuities in finite or (countably) infinite number. The simplest example of a Lévy process is the Poisson process (see Poisson Process): the increasing piecewise constant process with jumps of size 1 only and exponential waiting times between jumps. If  $(\tau_i)$  is a sequence of independent exponential random variables with intensity  $\lambda$  and  $T_k := \sum_{i=1}^k \tau_i$ , then the process

$$Z_t := \sum_i 1_{T_i \le t} \tag{1}$$

is called a *Poisson process* with intensity  $\lambda$ . A piecewise constant Lévy process with arbitrary jump sizes is called *compound Poisson* and can be written as

$$X_t = \sum_{k=1}^{Z_t} Y_i \tag{2}$$

where Z is a Poisson process and  $(Y_i)$  is an i.i.d. sequence of random variables. In general, the number of jumps of a Lévy process in a given interval need not be finite, and the process can be represented as a sum of a Brownian motion with drift and a limit of processes of the form in equation  $(2)$ :

$$X_t = \gamma t + B_t + N_t + \lim_{\varepsilon \downarrow 0} M_t^{\varepsilon} \tag{3}$$

where *B* is a *d*-dimensional Brownian motion,  $\gamma \in$  $\mathbb{R}^d$ , N is a compound Poisson process that includes the jumps of X with  $|\Delta X_t| > 1$ , and  $M_t^{\varepsilon}$  is a compensated compound Poisson process (compound Poisson minus its expectation) that includes the jumps of  $X$ with  $\varepsilon < |\Delta X_t| < 1$ . The law of a Lévy process is completely identified by its characteristic triplet—the positive definite matrix  $A$  (unit covariance of  $B$ ), the vector  $\gamma$  (drift), and the measure  $\nu$  on  $\mathbb{R}^d$ , called the Lévy measure, which determines the intensity of jumps of different sizes.  $\nu(A)$  is the expected number of jumps on the time interval  $[0, 1]$ , whose sizes fall in  $A$ . The Lévy measure satisfies the integrability condition

$$\int_{\mathbb{R}^d} 1 \wedge \|x\|^2 \nu(\mathrm{d}x) < \infty \tag{4}$$

and  $\nu(\mathbb{R}) < \infty$  if the process has finite jump intensity. The law of  $X_t$  at all times t is determined by the triplet and, in particular, the Lévy-Khintchine formula gives the characteristic function  $E[e^{iuX_t}] =$  $\exp[t\psi(u)]$  with

$$\psi(u) = i \langle \gamma, u \rangle + \frac{1}{2} \langle Au, u \rangle + \int_{\mathbb{R}^d} (e^{i \langle u, x \rangle} - 1$$
$$- i \langle u, x \rangle \mathbf{1}_{\|x\| < 1}) \nu(dx) \tag{5}$$

Conversely, any infinitely divisible law (see Infinite **Divisibility**) has a Lévy–Khintchine representation as above, so modeling with Lévy processes allows to pick any infinitely divisible distribution for the law (say, at time  $t = 1$ ) of the process.

#### Exponential Lévy Models

The Black-Scholes model

$$\frac{\mathrm{d}S_t}{S_t} = \mu \mathrm{d}t + \sigma \mathrm{d}W_t \tag{6}$$

can be equivalently rewritten in the exponential form  $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma W_t}$ . This gives us two possibilities to construct an exponential Lévy model starting from a (one-dimensional) Lévy process  $X$ , using the stochastic differential equation

$$\frac{\mathrm{d}S_t}{S_{t-}} = \mathrm{d}X_t \tag{7}$$

or using the ordinary exponential  $S_t = S_0 e^{X_t}$ . The solution to equation (7) with initial condition  $S_0 = 1$ is called the *stochastic exponential* of  $X$ . It can become negative if the process  $X$  has a big negative jump:  $\Delta X_s < -1$  for  $s \leq t$ . However, if X does not have jumps of size smaller than  $-1$ , then its stochastic exponential is positive, and the stochastic and the ordinary exponential yield the same class of positive processes. Given this result and the fact that ordinary exponentials are more tractable (in particular, we have the Lévy-Khintchine representation), they are more often used for modeling financial time series than the stochastic ones. In the rest of this article, we focus on the exponential Lévy model

$$S_t = S_0 e^{rt + X_t} \tag{8}$$

where  $X$  is a one-dimensional Lévy process with characteristic triplet  $(\sigma^2, \nu, \gamma)$  and r denotes the interest rate.

#### Examples

Exponential Lévy models fall into two categories. In the first category, called jump-diffusion models, the "normal" evolution of prices is given by a diffusion process, punctuated by jumps at random intervals. Here the jumps represent rare events—crashes and large drawdowns. Such an evolution can be represented by a Lévy process with a nonzero Gaussian component and a jump part with finitely many jumps:

$$X_t = \gamma t + \sigma W_t + \sum_{i=1}^{N_t} Y_i \tag{9}$$

In the *Merton model* (see **Jump-diffusion Models**) [16], which is the first model of this type, suggested in the literature, jumps in the log price  $X$  are assumed to have a Gaussian distribution:  $Y_i \sim N(\mu, \delta^2)$ . In the risk-neutral version (i.e., with the choice of drift such that  $e^{X}$  becomes a martingale), the characteristic exponent of the log stock price takes the following form:

$$\psi(u) = -\frac{\sigma^2 u^2}{2} + \lambda \{e^{-\delta^2 u^2/2 + i\mu u} - 1\}$$
$$-iu \left(\frac{\sigma^2}{2} + \lambda (e^{\delta^2/2 + \mu} - 1)\right) \qquad (10)$$

In the *Kou model* (see **Kou Model**) [13], jump sizes are distributed according to an asymmetric Laplace law with a density of the form

$$\nu_0(x) = [p\lambda_+ e^{-\lambda_+ x} 1_{x>0} + (1-p)\lambda_- e^{-\lambda_- |x|} 1_{x<0}]$$
(11)

with  $\lambda_{+} > 0$ ,  $\lambda_{-} > 0$  governing the decay of the tails for the distribution of positive and negative jump sizes and  $p \in [0, 1]$  representing the probability of an upward jump. The probability distribution of returns in this model has semiheavy (exponential) tails.

The second category consists of models with an infinite number of jumps in every interval, which we call *infinite activity* or *infinite intensity* models. In these models, one does not need to introduce a Brownian component since the dynamics of jumps is already rich enough to generate nontrivial small time behavior  $[4]$ .

There are several ways to define a parametric Lévy process with infinite jump intensity. The first approach is to obtain a Lévy process by subordinating a Brownian motion with an independent increasing Lévy process (called *subordinator*). Two examples of models from this class are the variance gamma process and the normal inverse Gaussian process. The variance gamma process (see Variance-gamma Model) [5, 15] is obtained by time changing a Brownian motion with a gamma subordinator and has the characteristic exponent of the form

$$\psi(u) = -\frac{1}{\kappa} \log \left( 1 + \frac{u^2 \sigma^2 \kappa}{2} - i \theta \kappa u \right) \tag{12}$$

The density of the Lévy measure of the variance gamma process is given by

$$\nu(x) = \frac{c}{|x|} e^{-\lambda_-|x|} 1_{x<0} + \frac{c}{x} e^{-\lambda_+ x} 1_{x>0} \tag{13}$$

where  $c = 1/\kappa$ ,  $\lambda_{+} = \frac{\sqrt{\theta^2 + 2\sigma^2/\kappa}}{\sigma^2} - \frac{\theta}{\sigma^2}$  and  $\lambda_{-} =$  $\frac{\sqrt{\theta^2+2\sigma^2/\kappa}}{\sigma^2}+\frac{\theta}{\sigma^2}.$ 

normal inverse Gaussian process (see Normal Inverse Gaussian Model) [2] is the result of time changing a Brownian motion with the inverse Gaussian subordinator and has the characteristic exponent

$$\psi(u) = \frac{1}{\kappa} - \frac{1}{\kappa} \sqrt{1 + u^2 \sigma^2 \kappa - 2i\theta u \kappa} \tag{14}$$

The second approach is to specify the Lévy measure directly. The main example of this category is the tempered stable process (see Tempered Stable **Process**), introduced by Koponen [12] and also known under the name of CGMY model [4]. This process has a Lévy measure with density of the form

$$\nu(x) = \frac{c_{-}}{|x|^{1+\alpha_{-}}} e^{-\lambda_{-}|x|} 1_{x<0} + \frac{c_{+}}{x^{1+\alpha_{+}}} e^{-\lambda_{+}x} 1_{x>0}$$
(15)

with  $\alpha_{+} < 2$  and  $\alpha_{-} < 2$ .

The third approach is to specify the density of increments of the process at a given time scale, say  $\Delta$ , by taking an arbitrary infinitely divisible distribution. Generalized hyperbolic processes (see Generalized **Hyperbolic Models**) [10] can be constructed in this way. In this approach, it is easy to simulate the increments of the process at the same time scale and to estimate parameters of the distribution if data are sampled with the same period  $\Delta$ , but, unless this distribution belongs to some parametric class closed under convolution, we do not know the law of the increments at other time scales.

# Market Incompleteness and Option Pricing

The exponential Lévy models correspond, in general, to arbitrage-free incomplete markets, meaning that options cannot be replicated exactly and, consequently, their price is not uniquely determined by the law of the underlying. This is good news: this means that the pricing model can be adjusted to take into account both the historical dynamics of the underlying and the market-quoted prices of European call and put options, a procedure known as *model* calibration (see Model Calibration). Once the riskneutral measure  $Q$  is calibrated, one can price an exotic option with payoff  $H_T$  at time T by taking the discounted expectation

$$P_0 = e^{-rT} E^{\mathcal{Q}}[H_T] \tag{16}$$

## **Fourier Transform Methods for Option Pricing and Model Calibration**

In exponential Lévy models, and in all models where the characteristic function of the log stock price  $\Phi_t(u) = E[e^{iuX_t}]$  is known explicitly, Fourier inversion provides a very efficient algorithm for pricing European options. This method was introduced in [5] and later improved and generalized in [14].

Consider a financial model of the form  $S_t =$  $S_0e^{rt+X_t}$ , where X is stochastic process whose characteristic function is known explicitly. To compute the price of a call option,

$$C(k) = S_0 E[(e^{X_T} - e^k)^+]$$
 (17)

where  $k = \log(K/S_0) - rT$  is the log forward moneyness, we would like to express its Fourier transform in terms of the characteristic function of  $X_T$  and then find the prices for a range of strikes by Fourier inversion. However, the Fourier transform of  $C(k)$ is not well defined because this function is not integrable, so we subtract the Black-Scholes call price with nonzero volatility  $\Sigma$  to obtain a function that is both integrable and smooth:

$$z_T(k) = C(k) - C_{BS}^{\Sigma}(k) \tag{18}$$

If *X* is a stochastic process such that  $E[e^{X_T}] = 1$  and  $E[e^{(1+\alpha)X_T}] < \infty$  for some  $\alpha > 0$ , then the Fourier transform of  $z_T(k)$  is given by

$$\zeta_T(v) = S_0 \frac{\Phi_T(v-i) - \Phi_T^{\Sigma}(v-i)}{iv(1+iv)} \tag{19}$$

where  $\Phi_T^{\Sigma}(v) = \exp(-\frac{\Sigma^2 T}{2}(v^2 + iv))$  is the characteristic function of log stock price in the Black-

Scholes model with volatility  $\Sigma$ . The exact value of  $\Sigma$  is not very important, and one can take, for example,  $\Sigma = 0.2$  for practical calculations.

Option prices are computed by evaluating numerically the inverse Fourier transform of  $\zeta_T$ :

$$z_T(k) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-ivk} \zeta_T(v) \, \mathrm{d}v \tag{20}$$

This integral can be efficiently computed for a range of strikes using the fast Fourier transform algorithm.

The Fourier-based fast deterministic algorithms for European option pricing can be used to calibrate exponential Lévy models to market-quoted option prices by penalized least squares as in [7]. Exponential Lévy models perform well for calibrating market option prices for a range of strikes and a single maturity, but fail to calibrate the entire implied volatility surface containing many maturities. This is due to the fact that the law of a Lévy process is completely determined by its distribution at a given date, so that if we know option prices for many strikes and a single maturity, we can readily reconstruct the law of the process at all dates, which may be incompatible with the other observations we may have. In particular, the implied volatility smile in exponential Lévy model flattens too fast for long-dated options (see Figure 1). Usually, a jump component can be included in a model to calibrate the short-maturity prices, and a stochastic volatility component is used to calibrate the skew at longer maturities.

#### PIDE Methods for Exotic Options

For contracts with barriers or American-style exercise, partial integro-differential equation (PIDE) methods provide an efficient alternative to Monte Carlo simulation. In diffusion models, the price of an option with payoff  $h(S_T)$  at time T solves the Black-Scholes partial differential equation (PDE)

$$\frac{\partial P}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 P}{\partial S^2} = rP - rS \frac{\partial P}{\partial S}$$
$$P(T, S) = h(S) \tag{21}$$

In an exponential Lévy model, there is a similar equation for the option price

$$P(t, S) = e^{-r(T-t)} E^{Q}[h(S_T)|S_t = S]$$
(22)

but due to the presence of jumps, an integral term appears in addition to the partial derivatives (see Partial Integro-differential Equations (PIDEs)):

$$\begin{split} \frac{\partial P}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 P}{\partial S^2} - rP + rS \frac{\partial P}{\partial S} \\ + \int_{\mathbb{R}} \nu(\mathrm{d}z) \Big\{ P(t, S\mathrm{e}^z) - P(t, S) \\ - S(\mathrm{e}^z - 1) \frac{\partial P}{\partial S}(t, S) \Big\} &= 0, \quad P(T, S) = h(S) \end{split} \tag{23}$$

![](_page_3_Figure_13.jpeg)

**Figure 1** Implied volatility surface in the Kou model with diffusion volatility  $\sigma = 0.2$  and only negative jumps with intensity  $\lambda = 10$  and average size  $\frac{1}{\lambda_{-}} = 0.05$ 

Different path-dependent characteristics of the payoff are translated into the boundary conditions of the equation: for example, for a down-and-out option with barrier *B*, we would impose *P (t, S)* = 0 for *S* ≤ *B* and all *t*. This equation and its numerical solution using finite differences is discussed in detail in [9] (*see* **Partial Integro-differential Equations (PIDEs)**).

### **Hedging**

In the Black–Scholes model, delta hedging is known to completely eliminate the risk of an option position. In the presence of jumps, delta hedging is no longer optimal: to hedge a jump of a given size, one should use the sensitivity to fluctuations of this particular size rather than the sensitivity to infinitesimal movements. Since the jump size is not known in advance, the risk associated with jumps cannot be hedged away completely. The model given by equation (8) therefore corresponds to an incomplete market except for the following two cases:

- no jumps in the stock price (*ν* ≡ 0, the Black– Scholes case) and
- no diffusion component (*σ* = 0) and only one possible jump size (*ν* = *δz*<sup>0</sup> *(z)*). In this case, the optimal hedging strategy is

$$\phi_t = \frac{P(S_t e^{z_0}) - P(S_t)}{S_t(e^{z_0} - 1)}$$
(24)

In all other cases, the hedging becomes an approximation problem: instead of *replicating* an option, one tries to *minimize* the residual hedging error. Many authors (see, e.g. [8, 11]) studied the quadratic hedging, where the optimal strategy is obtained by minimizing the expected squared hedging error. A particularly simple situation is when this error is computed under the martingale probability. The optimal hedge is then a weighted sum of the sensitivity of option price to infinitesimal stock movements, and the average sensitivity to jumps:

$$\phi^{*}(t, S_{t}) = \frac{\sigma^{2} \frac{\partial P}{\partial S} + \frac{1}{S_{t}} \int \nu(\mathrm{d}z)(\mathrm{e}^{z} - 1)(P(t, S_{t}\mathrm{e}^{z}) - P(t, S_{t}))}{\sigma^{2} + \int (\mathrm{e}^{z} - 1)^{2}\nu(\mathrm{d}z)}$$
(25)

For jump diffusions, if jumps are small, the Taylor decomposition of this formula gives

$$\phi_t \approx \frac{\partial P}{\partial S} + \frac{S_t}{2\Sigma^2} \frac{\partial^2 P}{\partial S^2} \int \nu(\mathrm{d}z) (\mathrm{e}^z - 1)^3$$
$$\Sigma^2 = \sigma^2 + \int (\mathrm{e}^z - 1)^2 \nu(\mathrm{d}z) \tag{26}$$

Therefore, the optimal strategy can be seen as a small and typically negative (since the jumps are mostly negative) correction to delta hedging. For pure-jump processes such as variance gamma, *(∂*<sup>2</sup>*P /∂S*<sup>2</sup>*)* may not be defined and the correction may be big.

Numerical studies of the performance of hedging strategies in the presence of jumps show that

- If the jumps are small, delta hedging works well and its performance is close to optimal.
- In the presence of a strong jump component, the optimal strategy is superior to delta hedging both in terms of hedge stability and residual error.
- If jumps are strong, the residual hedging error can be further reduced by adding options to the hedging portfolio.

To eliminate the remaining hedging error, a possible solution is to use liquid options as hedging instruments. Optimal quadratic hedge ratios in the case when the hedging portfolio may contain options can be found in [8].

### **Additional Reading**

For a more in-depth treatment, the reader may refer to the monographs [6, 18].

### **References**

- [1] Appelbaum, D. (2004). *L´evy Processes and Stochastic Calculus*, Cambridge University Press.
- [2] Barndorff-Nielsen, O. (1998). Processes of normal inverse Gaussian type, *Finance and Stochastics* **2**, 41–68.
- [3] Bertoin, J. (1996). *L´evy Processes*, Cambridge University Press, Cambridge.
- [4] Carr, P., Geman, H., Madan, D. & Yor, M. (2002). The fine structure of asset returns: an empirical investigation, *Journal of Business* **75**, 305–332.
- [5] Carr, P. & Madan, D. (1998). Option valuation using the fast Fourier transform, *Journal of Computational Finance* **2**, 61–73.

### **6 Exponential Levy Models ´**

- [6] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman & Hall/CRC Press.
- [7] Cont, R. & Tankov, P. (2006). Retrieving Levy processes ´ from option prices: regularization of an ill-posed inverse problem, *SIAM Journal on Control and Optimization* **45**, 1–25.
- [8] Cont, R., Tankov, P. & Voltchkova, E. (2007). Hedging with options in models with jumps. *Proceedings of the 2005 Abel Symposium in Honor of Kiyosi Itˆo*, F.E. Benth, G. Di Nunno, T. Lindstrom, B. Øksendal & T. Zhang, eds, Springer, pp. 197–218.
- [9] Cont, R. & Voltchkova E. (2005). A finite difference scheme for option pricing in jump-diffusion and exponential Levy models, ´ *SIAM Journal on Numerical Analysis* **43**, 1596–1626.
- [10] Eberlein, E. (2001). Applications of generalized hyperbolic Levy motion to Finance, in ´ *Levy Pro- ´ cesses—Theory and Applications*, O. Barndorff-Nielsen, T. Mikosch & S. Resnick, eds, Birkhauser, Boston, pp. ¨ 319–336.
- [11] Kallsen, J., Hubalek, F. & Krawczyk, L. (2006). Variance-optimal hedging for processes with stationary independent increments, *The Annals of Applied Probability* **16**, 853–885.
- [12] Koponen, I. (1995). Analytic approach to the problem of convergence of truncated Levy flights towards the ´ Gaussian stochastic process, *Physical Review E* **52**, 1197–1199.

- [13] Kou, S. (2002). A jump-diffusion model for option pricing, *Management Science* **48**, 1086–1101.
- [14] Lee, R.W. (2004). Option pricing by transform methods: extensions, unification and error control, *Journal of Computational Finance* **7**, 51–86.
- [15] Madan, D., Carr, P. & Chang, E. (1998),. The variance gamma process and option pricing, *European Finance Review* **2**, 79–105.
- [16] Merton, R. (1976). Option pricing when underlying stock returns are discontinuous, *Journal Financial Economics* **3**, 125–144.
- [17] Sato, K. (1999). *L´evy Processes and Infinitely Divisible Distributions*, Cambridge University Press, Cambridge.
- [18] Schoutens, W. (2003). *L´evy Processes in Finance: Pricing Financial Derivatives*, Wiley, New York.

### **Related Articles**

**Barndorff-Nielsen and Shephard (BNS) Models**; **Fourier Transform**; **Infinite Divisibility**; **Jump Processes**; **Jump-diffusion Models**; **Kou Model**; **Partial Integro-differential Equations (PIDEs)**; **Tempered Stable Process**; **Time-changed Levy ´ Process**; **Tempered Stable Process**.

PETER TANKOV
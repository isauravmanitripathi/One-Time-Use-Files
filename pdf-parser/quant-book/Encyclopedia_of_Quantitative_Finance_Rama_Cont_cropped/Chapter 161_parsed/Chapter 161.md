# **Kou Model**

It is well known that empirically asset return distributions have heavier tails (*see* **Heavy Tails**) than those of normal distributions, in contrast to the classical Black–Scholes model (*see* **Black–Scholes Formula**). Jump-diffusion models are among the most popular alternative models proposed to address this issue, and they are especially useful to price options with short maturities (*see* **Exponential Levy Mod- ´ els**). However, analytical tractability is one of the challenges faced by many alternative models. More precisely, although many alternative models can lead to analytical solutions for European call and put options, unlike the Black–Scholes model, it is difficult to do so for path-dependent options such as lookback (*see* **Lookback Options**), barrier (*see* **Barrier Options**), and American options, which are treated using numerical methods (*see* **Partial Integro-differential Equations (PIDEs)**). For example, the convergence rates of binomial trees and Monte Carlo simulation for path-dependent options are typically much slower than those for call and put options; see Boyle *et al.* [3].

The double exponential jump-diffusion model is a jump-diffusion model in which the jump size distribution follows a two-sided exponential distribution. It was introduced to further extend the analytical tractability of models with jumps.

In jump-diffusion models under the physical probability measure *P*, the asset price, *S(t)*, is modeled as

$$\frac{\mathrm{d}S(t)}{S(t-)} = \mu \,\mathrm{d}t + \sigma \,\mathrm{d}W(t) + \mathrm{d}\left(\sum_{i=1}^{N(t)} (V_i - 1)\right) \tag{1}$$

where *W (t)* is a standard Brownian motion, *N (t)* is a Poisson process with rate *λ*, and {*Vi*} is a sequence of independent identically distributed (i.i.d.) nonnegative random variables. All the sources of randomness, *N (t)*, *W (t)*, and *V* 's, are assumed to be independent. Solving the stochastic differential equation (1) gives the dynamics of the asset price:

$$S(t) = S(0) \exp\left\{ \left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W(t) \right\} \prod_{i=1}^{N(t)} V_i$$
(2)

In the Merton model [28], *Y* = log*(V )* has a normal distribution. In the double exponential jump-diffusion model [23] *Y* = log*(V )* has an asymmetric double exponential distribution with the density

$$f_Y(y) = p \cdot \eta_1 e^{-\eta_1 y} 1_{\{y \ge 0\}} + q \cdot \eta_2 e^{\eta_2 y} 1_{\{y < 0\}},$$
  
$$\eta_1 > 1, \ \eta_2 > 0 \tag{3}$$

where *p, q* ≥ 0, *p* + *q* = 1, represent the probabilities of upward and downward jumps. The requirement *η*<sup>1</sup> *>* 1 is needed to ensure that E*(V ) <* ∞ and E*(S(t)) <* ∞; it essentially means that the average upward jump cannot exceed 100%, which is quite reasonable [2].

As pointed out in [23], the jump part of the double exponential jump-diffusion model can be interpreted as the market response to outside developments; and the heavier tail and higher peak (in comparison to the standard normal distribution) of the double exponential distribution attempt to model market overreaction and underreaction, respectively. Ramezani and Zeng [29] independently proposed the double exponential jump-diffusion model from an econometric viewpoint as a way of improving the empirical fit of Merton's normal jump-diffusion model to stock price data.

Such models lead to incomplete markets in which the replication of an option payoff is impossible. The monograph by Cont and Tankov [10] discusses hedging issues for jump-diffusion models and resulting pricing measures. Alternatively, one can use the rational expectations in [27] and [32] to choose a risk-neutral measure to price derivative as in [23].

The double exponential jump-diffusion model belongs to the class of exponential Levy models ( ´ *see* **Exponential Levy Models ´** ). There is a large literature on Levy processes in finance, including several ´ excellent books, for example, the books by Cont and Tankov [10] and Kijima [22].

#### *Analytical Tractability*

The main advantage of the double exponential jumpdiffusion model is that it offers a rare case where we can derive the analytical solution of the joint distribution of the first passage time and *X(t)* = log*(S(t)/S(*0*))*, thereby making it possible to price path-dependent options such as lookback, barrier, and perpetual American options. An intuitive explanation for this follows.

![](_page_1_Figure_1.jpeg)

**Figure 1** A simulated sample path with the overshoot problem

To price lookback, barrier, and perpetual American options, it is pivotal to study the first passage times *τb* when the process crosses a flat boundary with a level *b*. Without loss of generality, assume that *b >* 0. When a jump-diffusion process crosses the boundary, sometimes it hits the boundary exactly and sometimes it incurs an "overshoot", *Xτb* − *b*, over the boundary as shown in Figure 1. The overshoot presents several problems if one wants to compute the distribution of the first passage time analytically. First, one needs the exact distribution of the overshoot, *Xτb* − *b*; particularly, *P (Xτb* − *b* = 0*)* and *P (Xτb* − *b > x)*, *x >* 0. Second, one needs to know the dependence structure between the overshoot, *Xτb* − *b*, and the first passage time *τb*.

These difficulties may be resolved under the assumption that the jump size *Y* has a double exponential distribution. Mathematically, this is because the exponential function has some very nice properties, such as the product of exponential functions is still an exponential function, and the derivatives of exponential functions are still exponential function. These nice properties enable us to solve related ordinary integro-differential equations (OIDE) explicitly, leading to analytical solutions for the marginal and joint distributions of the first passage times, and ultimately, analytical tractability for pricing lookback, barrier, and perpetual American options. More precisely, the infinitesimal generator of the return process *X(t)* is given by

$$\mathcal{L}u(x) = \frac{1}{2}\sigma^2 u''(x) + \tilde{\mu}u'(x)$$
$$+ \lambda \int_{-\infty}^{\infty} \left[ u(x+y) - u(x) \right] f_Y(y) \, \mathrm{d}y \tag{4}$$

for all twice continuously differentiable functions *u(x)*. When studying the first passage time, we encounter an OIDE with discontinuous regions as follows:

$$\begin{cases} (\mathcal{L}u)(x) = \alpha u(x), & x < x_0 \\ u(x) = g(x), & x \ge x_0 \end{cases}$$
(5)

where *α >* 0 and *g(x)* is a given function. Many times *x*<sup>0</sup> is a fixed number, but in the case of American options, *x*<sup>0</sup> is a parameter that needs to be determined by solving a free boundary problem. Note that *u(x)* solves the OIDE not for all *x* ∈ but only for *x<x*0. However, *u(x)* does involve the information on *x>x*0, as the integral inside the generator (4) depends on the function *g(x)*, thereby making itself more complicated. This OIDE can be solved explicitly under the double exponential jump-diffusion model, thereby leading to an analytical solution of the joint distribution of the first passage time *τb* and *Xt* ; see [25, 26], and [24].

In addition to pricing options related to the first passage times, the double exponential jump-diffusion models have been studied in many papers. What is detailed below is only a snapshot of some interesting results.

- 1. In terms of computational issues, see [11] and [12] for numerical methods *via* solving partial integro-differential equations (see Partial Integro-differential Equations (PIDEs)); Feng and Linetsky [17] and Feng et al. [16] showed how to price path-dependent options numerically *via* extrapolation and variational methods.
- 2. In terms of applications, see the references in  $[18]$  for applications in fixed income derivatives and term structure models, and the references in [9] for applications in credit risk and credit derivatives.
- 3. Double-barrier options (with both upper and lower barriers) are studied in  $[30]$  and  $[4]$ .
- 4. Statistical inference and econometric analysis for Lévy processes are discussed in [31].

### **Volatility Clustering Effect**

In addition to the leptokurtic feature, returns distributions also have an interesting dependent structure, called the *volatility clustering effect*; see [14]. More precisely, the volatility of returns (which are related to the squared returns) are correlated, but asset returns themselves have almost no autocorrelation. In other words, a large movement in asset prices, either upward or downward, tends to generate large movements in the future asset prices, although the direction of the movements is unpredictable.

In particular, any model for stock returns with independent increments (such as Lévy processes) cannot incorporate the volatility clustering effect. However, one can combine jump-diffusion processes with other processes [1, 13] or consider timechanged Brownian motion and Lévy processes (see Time Change) to incorporate the volatility clustering effect. More precisely, if  $\tau(t)$  contains a diffusion component (i.e., not a subordinator), then  $W(\tau(t))$  and  $X(\tau(t))$  may have dependent increments and no longer be Lévy processes; see [6, 7], and [8].

#### **Hyper-Exponential Jumps**

Although the main empirical motivation for using Lévy processes in finance comes from the fact that asset return distributions tend to have tails heavier than those of normal distribution, it is not clear how heavy the tail distributions are, as some people favor power-type distributions and others exponential-type distributions, although, as pointed out in [23, p. 1090], the power-type right tails cannot be used in models with continuous compounding as they lead to infinite expectation for the asset price. We stress that, quite surprisingly, it is very difficult to distinguish power-type tails from exponentialtype tails and from empirical data unless one has extremely large sample size perhaps in the order of tens of thousands or even hundreds of thousands [19]. Therefore, it is very difficult to choose a good model based on the limited empirical data alone.

A good intuition may be obtained by simply looking at the quantiles for both standardized Laplace (with a symmetric density  $f(x) =$  $\frac{1}{2}e^{-x}I_{[x>0]} + \frac{1}{2}e^{x}I_{[x<0]}$  and standardized t distributions with mean 0 and variance 1. The right quantiles for the Laplace and normalized  $t$  densities with degrees of freedom (DOF) from 3 to 7 are given in Table 1.

This table shows that the Laplace distributions may have higher tail probabilities than  $t$  distributions, even if asymptotically the Laplace distributions should have lighter tails than  $t$  distributions. For example, regardless of the sample size, the Laplace distribution may appear to be heavier tailed than a  $t$ -distribution with DOF 6 or 7, up to the 99.9th percentile. To distinguish the distributions it is necessary to use quantiles with very low  $p$  values and correspondingly large sample sizes for statistical inference. If the true quantiles have to be estimated from data, then the problem is even worse, as the sample standard deviations need to be considered, resulting in

**Table 1** The right quantiles of the Laplace and normalized *t*-distributions

| Prob.  | Laplace | t7   | t6   | t5    | t4    | t3    |
|--------|---------|------|------|-------|-------|-------|
| 1%     | 2.77    | 2.53 | 2.57 | 2.61  | 2.65  | 2.62  |
| 0.1%   | 4.39    | 4.04 | 4.25 | 4.57  | 5.07  | 5.90  |
| 0.01%  | 6.02    | 5.97 | 6.55 | 7.50  | 9.22  | 12.82 |
| 0.001% | 7.65    | 8.54 | 9.82 | 12.04 | 16.50 | 27.67 |

sample sizes typically in the tens of thousands or even hundreds of thousands necessary to distinguish power-type tails from exponential-type tails. For further discussion, see [20], in which is also discussed the implication in terms of risk measured.

The difficulty in distinguishing tail behavior motivated Cai and Kou [5] to extend the double exponential jump-diffusion model to a hyperexponential jump-diffusion model, in which the jump size  $\{Y_i :=$  $log(V_i)$ :  $i = 1, 2 \cdots$  is a sequence of i.i.d. hyperexponential random variables with density

$$f_Y(x) = \sum_{i=1}^m p_i \eta_i e^{-\eta_i x} I_{\{x \ge 0\}} + \sum_{j=1}^n q_j \theta_j e^{\theta_j x} I_{\{x < 0\}}$$
(6)

where  $p_i > 0$  and  $\eta_i > 1$  for all  $i = 1, \ldots, m, q_i > 0$ 0 and  $\theta_j > 0$  for all  $j = 1, \ldots, n$ , and  $\sum_{i=1}^m p_i +$  $\sum_{j=1}^{n} q_j = 1$ . Here the condition that  $\eta_i > 1$ , for all  $i = 1, \ldots, m$ , is imposed to ensure that the stock price  $S_t$  has a finite expectation.

The hyperexponential distribution is general enough to provide a link between various heavytail distributions, no matter which ones we prefer. In particular, any completely monotone distribution, for example, with a density  $f(x)$  satisfying the condition that all derivatives of  $f(x)$  exist and  $(-1)^n f^{(n)}(x) \ge$ 0 for all x and  $n \ge 1$ , can be approximated by hyperexponential distributions as closely as possible in the sense of weak convergence. Many distributions with tails heavier than those of the normal distribution are completely monotone. Here are some examples of completely monotone distributions frequently used in finance:

- Gamma distribution. The density of Gamma 1.  $(\alpha, \beta)$  is  $x^{\alpha-1}e^{-\beta x}$ , where  $\alpha, \beta > 0$ . When  $\alpha < 1$ , the distribution is completely monotone.
- Weibull distribution. The cumulative distribution 2. function of Weibull  $(c, d)$  is given by  $1$  $e^{-(x/d)^c}$ , where  $c, d > 0$ . When  $c < 2$ , it has heavier tails than the normal distribution.
- 3. *Pareto distribution*. The distribution of Pareto  $(a, b)$  is given by  $1 - (1 + bx)^{-a}$ , where  $a, b > 0$ .
- 4. Pareto mixture of exponential distribution (*PME*). The density of PME  $(a, b)$  is given by  $\int_0^{+\infty} f_{a,b}(y) y^{-1} e^{-x/y} dy$ , where  $f_{a,b}$  is the density of the Pareto  $(a, b)$ .

In summary, many heavy-tail distributions used in finance can be approximated arbitrarily closely by the hyperexponential distribution. Feldmann and Whitt [15] develop a numerical algorithm to approximate completely monotone distributions by the hyperexponential distribution.

Cai and Kou [5] show that the hyperexponential jump-diffusion model can lead to analytical solutions for popular path-dependent options, such as lookback, barrier, and perpetual American options. These analytical solutions are made possible mainly because we solve several high-order integro-differential equations related to first passage time problems and optimal stopping problems explicitly. Solving the high-order integro-differential equations is the main technical contribution of [5], which is achieved by discovering a connection between integro-differential equations and homogeneous ordinary differential equations in the case of the hyperexponential jump-diffusion generator.

#### Multivariate Version

A significant drawback of most of the Levy processes discussed in the literature is that they are one dimensional, whereas many options traded in markets have several underlying assets. To overcome this, Huang and Kou [21] introduced a multivariate jumpdiffusion model in which, under the physical measure  $P$ , the following stochastic differential equation is proposed to model the asset prices  $S(t)$ :

$$\frac{\mathrm{d}S(t)}{S(t-)} = \mu \,\mathrm{d}t + \sigma \,\mathrm{d}W(t) + \mathrm{d}\left(\sum_{i=1}^{N(t)} (V_i - 1)\right) \tag{7}$$

where  $W(t)$  is an *n*-dimensional standard Brownian motion,  $\sigma \in R^{n \times n}$  with the covariance matrix  $\Sigma =$  $\sigma \sigma^T$ . The rate of the Poisson process  $N(t)$  process is  $\lambda = \lambda_c + \sum_{k=1}^n \lambda_k$ ; in other words, there are two types of jumps, common jumps for all assets with jump rate  $\lambda_c$  and individual jumps with rate  $\lambda_k$ ,  $1 \le k \le n$ , only for the *k*th asset.

The logarithms of the common jumps have an  $m$ -dimensional asymmetric Laplace distribution  $\mathcal{AL}_n(m_c, J_c)$ , where  $m_c = (m_{1,c}, \dots, m_{n,c})' \in R^n$ and  $J_c \in \mathbb{R}^{n \times n}$  is positive definite. For the individual jumps of the  $k$ th asset, the logarithms of the jump sizes follow a one-dimensional asymmetric Laplace distribution,  $\mathcal{AL}_1(m_k, v_k^2)$ . In summary,

$$Y = \log(V) \sim \begin{cases} \mathcal{AL}_{n}(m_{c}, J_{c}), & \text{with prob. } \lambda_{c}/\lambda \\ (\underbrace{0, \ldots, 0}_{k-1}), & \mathcal{AL}_{1}(m_{k}, v_{k}^{2}), \underbrace{0, \ldots, 0}_{n-k}), & \text{with prob. } \lambda_{k}/\lambda, & 1 \leq k \leq n \end{cases}$$
(8)

The sources of randomness,  $N(t)$ ,  $W(t)$  are assumed to be independent of the jump sizes  $V_i$ . Jumps at different times are assumed to be independent. Note that in the univariate case, the above model degenerates to the double exponential jump-diffusion model [23] but with  $p\eta_1 = q\eta_2$ .

In the special case of a two-dimensional model, the two-dimensional jump-diffusion return process  $(X_1(t), X_2(t))$ , with  $X_i(t) = \log(S_i(t)/S(0))$ , is given by

$$X_1(t) = \mu_1 t + \sigma_1 W_1(t) + \sum_{i=1}^{N(t)} Y_i^{(1)}$$
  
$$X_2(t) = \mu_2 t + \sigma_2 \left[ \rho W_1(t) + \sqrt{1 - \rho^2} W_2(t) \right]$$
  
$$+ \sum_{i=1}^{N(t)} Y_i^{(2)}$$
 (9)

Here all the parameters are risk-neutral parameters;  $W_1(t)$  and  $W_2(t)$  are two independent standard Brownian motions; and  $N(t)$  is a Poisson process with rate  $\lambda = \lambda_c + \lambda_1 + \lambda_2$ . The distribution of the logarithm of the jump sizes  $Y_i$  is given by

$$Y_{i} = (Y_{i}^{(1)}, Y_{i}^{(2)})'$$
  

$$\sim \begin{cases} \mathcal{AL}_{2}(m_{c}, J_{c}), & \text{with prob. } \lambda_{c}/\lambda \\ (\mathcal{AL}_{1}(m_{1}, v_{1}^{2}), 0)', & \text{with prob. } \lambda_{1}/\lambda \\ (0, \mathcal{AL}_{1}(m_{2}, v_{2}^{2}))', & \text{with prob. } \lambda_{2}/\lambda \end{cases}$$
(10)

where the parameters for the common jumps are

$$m_{c} = \begin{pmatrix} m_{1,c} \\ m_{2,c} \end{pmatrix} \quad \text{and} \quad J_{c} = \begin{pmatrix} v_{1,c}^{2} & cv_{1,c}v_{2,c} \\ cv_{1,c}v_{2,c} & v_{2,c}^{2} \end{pmatrix}$$
(11)

The infinitesimal generator of  $\{X_1(t), X_2(t)\}$  is given by

$$\begin{split} \mathcal{L}u &= \mu_1 \frac{\partial u}{\partial x_1} + \mu_2 \frac{\partial u}{\partial x_2} \\ &+ \frac{1}{2} \sigma_1^2 \frac{\partial^2 u}{\partial x_1^2} + \frac{1}{2} \sigma_2^2 \frac{\partial^2 u}{\partial x_2^2} + \rho \sigma_1 \sigma_2 \frac{\partial^2 u}{\partial x_1 \partial x_2} \\ &+ \lambda_c \int_{y_2 = -\infty}^{\infty} \int_{y_1 = -\infty}^{\infty} \left[ u(x_1 + y_1, x_2 + y_2) - u(x_1, x_2) \right] \\ &\times f_{(Y^{(1)}, Y^{(2)})}^c(y_1, y_2) \, \mathrm{d}y_1 \, \mathrm{d}y_2 \\ &+ \lambda_1 \int_{y_1 = -\infty}^{\infty} \left[ u(x_1 + y_1, x_2) - u(x_1, x_2) \right] f_{Y^{(1)}}(y_1) \, \mathrm{d}y_1 \\ &+ \lambda_2 \int_{y_2 = -\infty}^{\infty} \left[ u(x_1, x_2 + y_2) - u(x_1, x_2) \right] \\ &\times f_{Y^{(2)}}(y_2) \, \mathrm{d}y_2 \end{split} \tag{12}$$

for all continuous twice differentiable function  $u(x_1, x_2)$ , where  $f_{(Y^{(1)}, Y^{(2)})}^c(y_1, y_2)$  is the joint density of correlated common jumps  $\mathcal{AL}_2(m_c, J_c)$ , and  $f_{Y^{(i)}}(y_i)$  is the individual jump density of  $\mathcal{AL}_1(m_i, J_i), i = 1, 2.$ 

One difficulty in studying the generator is that the joint density of the asymmetric Laplace distribution has no analytical expression. Therefore, the calculation related to the joint density and generator becomes complicated. See [21] for change of measures from a physical measure to a risk-neutral measure, analytical solutions for the first passage times, and pricing formulae for barrier and exchange options.

#### References

- Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-[1] Gaussian Ornstein-Uhlenbeck based models and some of their uses in financial economics (with discussion), Journal of Royal Statistical Society, Series B 63, 167-241.
- [2] Boyarchenko, S. & Levendorskii, S. (2002). Non-Gaussian Merton-Black-Scoles Theory, World Scientific, Singapore.

- [3] Boyle, P., Broadie, M. & Glasserman, P. (1997). Monte Carlo methods for security pricing, *Journal of Economic Dynamics and Control* **21**(89), 1267–1321.
- [4] Cai, N., Chen, N. & Wan, X. (2008). *Pricing Double Barrier Options Under a Flexible Jump Diffusion Model*, Hong Kong University of Science and Technology. Preprint.
- [5] Cai, N. & Kou, S.G. (2008). *Option Pricing Under a HyperExponential Jump Diffusion Model*, Columbia University. Preprint.
- [6] Carr, P., Geman, H., Madan, D. & Yor, M. (2002). The fine structure of asset returns: an empirical investigation, *Journal of Business* **75**, 305–332.
- [7] Carr, P., Geman, H., Madan, D. & Yor, M. (2003). Stochastic volatility for Levy processes, ´ *Mathematical Finance* **13**, 345–382.
- [8] Carr, P. & Wu, L. (2004). Time-changed levy processes ´ and option pricing, *Journal of Financial Economics* **71**, 113–141.
- [9] Chen, N. & Kou, S.G. (2005). Credit spreads, optimal capital structure, and implied volatility with endogenous default and jump risk, *Mathematical Finance* Preprint, Columbia University. To appear.
- [10] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, 2nd Printing, Chapman & Hall/CRC Press, London.
- [11] Cont, R. & Voltchkova, E. (2005). Finite difference methods for option pricing in jump-diffusion and exponential Levy models, ´ *SIAM Journal of Numerical Analysis* **43**, 1596–1626.
- [12] d'Halluin, Y., Forsyth, P.A. & Vetzal, K.R. (2003). *Robust Numerical Methods for Contingent Claims under Jump-diffusion Processes*, Working paper, University of Waterloo.
- [13] Duffie, D., Pan, J. & Singleton, K. (2000). Transform analysis and asset pricing for affine jump-diffusions, *Econometrica* **68**, 1343–1376.
- [14] Engle, R. (1995). *ARCH: Selected Readings*, Oxford University Press.
- [15] Feldmann, A. & Whitt, W. (1998). Fitting mixtures of exponentials to long-tail distributions to analyze network performance models, *Performance Evaluation* **31**, 245–279.
- [16] Feng, L., Kovalov, P., Linetsky, V. & Marcozzi, M. (2007). Variational methods in derivatives pricing, in *Handbook of Financial Engineering*, J. Birge & V. Linetsky, eds, Elsevier, Amsterdam.
- [17] Feng, L. & Linetsky, V. (2008). Pricing options in jumpdiffusion models: an extrapolation approach, *Operations Research* **52**, 304–325.
- [18] Glasserman, P. & Kou, S.G. (2003). The term structure of simple forward rates with jump risk, *Mathematical Finance* **13**, 383–410.
- [19] Heyde, C.C. & Kou, S.G. (2004). On the controversy over tailweight of distributions, *Operations Research Letters* **32**, 399–408.

- [20] Heyde, C.C., Kou, S.G. & Peng, X.H. (2008). *What is a Good Risk Measure: Bridging the Gaps Between Robustness, Subadditivity, Prospect Theory, and Insurance Risk Measures*, Columbia University. Preprint.
- [21] Huang, Z. & Kou, S.G. (2006). *First Passage Times and Analytical Solutions for Options on Two Assets with Jump Risk*, Columbia University. Preprint.
- [22] Kijima, M. (2002). *Stochastic Processes with Applications to Finance*, Chapman & Hall, London.
- [23] Kou, S.G. (2002). A jump-diffusion model for option pricing, *Management Science* **48**, 1086–1101.
- [24] Kou, S.G., Petrella. G. & Wang, H. (2005). Pricing path-dependent options with jump risk via Laplace transforms, *Kyoto Economic Review* **74**, 1–23.
- [25] Kou, S.G. & Wang, H. (2003). First passage time of a jump diffusion process, *Advances in Applied Probability* **35**, 504–531.
- [26] Kou, S.G. & Wang, H. (2004). Option pricing under a double exponential jump-diffusion model, *Management Science* **50**, 1178–1192.
- [27] Lucas, R.E. (1978). Asset prices in an exchange economy, *Econometrica* **46**, 1429–1445.
- [28] Merton, R.C. (1976). Option pricing when underlying stock returns are discontinuous, *Journal of Financial Economics* **3**, 125–144.
- [29] Ramezani, C.A. and Zeng, Y. (2002). *Maximum Likelihood Estimation of Asymmetric Jump-Diffusion Process: Application to Security Prices*, Working Paper, Department of Mathematics and Statistics, University of Missouri, Kansas City.
- [30] Sepp, A. (2004). Analytical pricing of double-barrier options under a double exponential jump diffusion process: applications of Laplace transform, *International Journal of Theoretical and Applied Finance* **7**, 151–175.
- [31] Singleton, K. (2006). *Empirical Dynamic Asset Pricing*, Princeton University Press.
- [32] Stokey, N.L. & Lucas, R.E. (1989). *Recursive Methods in Economic Dynamics*, Harvard University Press.

# **Further Reading**

Hull, J. (2005). *Options, Futures, and Other Derivatives*, Prentice Hall.

## **Related Articles**

**Barrier Options**; **Exponential Levy Models ´** ; **Jump Processes**; **Lookback Options**; **Partial Integrodifferential Equations (PIDEs)**; **Wiener–Hopf Decomposition**.

STEVEN KOU
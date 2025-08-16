# **Simulation of Square-root** Processes

Square-root diffusion processes are popular in many branches of quantitative finance. Guaranteed to stay nonnegative, yet almost as tractable as a Gaussian process, the mean-reverting square-root process has found applications ranging from short-rate modeling of the term structure of interest rates, to credit derivative pricing, and to stochastic volatility models, just to name a few.

A thorough description of the theoretical properties of square-root processes as well as their generalization into multifactor affine jump-diffusion processes can be found in [7] where a full literature survey is also available. While we shall rely on some of these results in the remainder of this article, our focus here is on the problem of generating Monte Carlo paths for the one-factor square-root process, first in isolation and later in combination with a lognormal asset process (as required in most stochastic volatility applications). As we shall see, such path generation can, under many relevant parameter settings, be surprisingly challenging. Indeed, despite the popularity and the longevity of the square-root diffusion—the first uses in finance date back several decades—it is only in the last few years that a satisfactory palette of Monte Carlo algorithms has been established.

# **Problem Definition and Key Theoretical** Results

Let  $x(t)$  be a scalar random variable satisfying a stochastic differential equation (SDE) of the meanreverting square-root type, that is

$$dx(t) = \kappa (\theta - x(t)) dt + \epsilon \sqrt{x(t)} dW(t),$$
  
$$x(0) = x_0$$
 (1)

where  $\kappa, \theta, \epsilon$  are positive constants and  $W(t)$  is a Brownian motion in a given probability measure. Applications of equation  $(1)$  in finance include the seminal CIR (Cox-Ingersoll-Ross) model for interest rates (see Cox-Ingersoll-Ross (CIR) Model) and the Heston stochastic volatility model (see Heston Model). In practical usage of such models (e.g., to price options), we are often faced with the problem of generating Monte Carlo paths of  $x$  on some discrete timeline. To devise a simulation scheme, it suffices to contemplate the more fundamental question of how to generate, for an arbitrary increment  $\Delta$ , a random sample of  $x(t + \Delta)$  given  $x(t)$ ; repeated application of the resulting one-period scheme produces a full path of  $x$  on an arbitrary set of discrete dates.

To aid in the construction of simulation algorithms, let us quickly review a few well-known theoretical results for equation (1).

**Proposition 1** Let  $F(z; \nu, \lambda)$  be the cumulative distribution function for the noncentral chi-square dis $t$ ribution with  $v$  degrees of freedom and noncentrality *parameter*  $\lambda$ *:* 

$$F(z;\nu,\lambda) = e^{-\lambda/2} \sum_{j=0}^{\infty} \frac{(\lambda/2)^j}{j! 2^{\nu/2+j} \Gamma(\nu/2+j)}$$
$$\times \int_0^z y^{\nu/2+j-1} e^{-x/2} dy \tag{2}$$

For the process  $(1)$  define

$$d = 4\kappa\theta/\epsilon^{2};$$
  
$$n(t,T) = \frac{4\kappa e^{-\kappa(T-t)}}{\epsilon^{2} \left(1 - e^{-\kappa(T-t)}\right)}, \ T > t \tag{3}$$

Let  $T > t$ . Conditional on  $x(t)$ ,  $x(T)$  is distributed as  $e^{-\kappa(T-t)}/n(t,T)$  times a noncentral chi-square distri- $\text{bution with } d \text{ degrees of freedom and noncentrality}$ parameter  $x(t)n(t, T)$ . That is,

$$\Pr\left(x(T) < x | x(t)\right)$$
  
=  $F\left(\frac{x \cdot n(t,T)}{e^{-\kappa(T-t)}}; d, x(t) \cdot n(t,T)\right)$  (4)

From the known properties of the noncentral chisquare distribution, the following corollary easily follows.

**Corollary 1** For  $T > t$ ,  $x(T)$  has the following first two conditional moments:

$$E(x(T)|x(t)) = \theta + (x(t) - \theta)e^{-\kappa(T-t)}$$
  

$$Var(x(T)|x(t)) = \frac{x(t)\epsilon^2 e^{-\kappa(T-t)}}{\kappa}$$
  

$$\times \left(1 - e^{-\kappa(T-t)}\right) + \frac{\theta \epsilon^2}{2\kappa} \left(1 - e^{-\kappa(T-t)}\right)^2 \quad (5)$$

**Proposition 2** Assume that  $x(0) > 0$ . If  $2\kappa\theta \ge \epsilon^2$ , then the process for x can never reach zero. If  $2\kappa\theta$  <  $\epsilon^2$ , the origin is accessible and strongly reflecting.

The condition  $2\kappa\theta \geq \epsilon^2$  in Proposition 2 is often known as the *Feller condition* (see [12]) for equation  $(1)$ . When equation  $(1)$  is used as a model for interest rates or credit spreads, market-implied model parameters are typically such that the Feller condition is satisfied. However, when equation (1) represent a stochastic variance process (as in the section Stochastic Volatility Simulation), the Feller condition rarely holds. As it turns out, a violation of the Feller condition may increase the difficulty of Monte Carlo path generation considerably.

## **Simulation Schemes**

#### Exact Simulation

According to Proposition 1, the distribution of  $x(t + \Delta)$  given  $x(t)$  is known in closed form. Generation of a random sample of  $x(t + \Delta)$  given  $x(t)$ can therefore be done entirely bias-free by sampling from a noncentral chi-square distribution. Using the fact that a noncentral chi-square distribution can be seen as a regular chi-square distribution with Poissondistributed degrees of freedom (see  $[9]$ ), the following algorithm can be used.

- 1. Draw a Poisson random variable  $N$ , with mean  $\frac{1}{2}x(t)n(t,t+\Delta).$
- 2. Given  $N$ , draw a regular chi-square random variable  $\chi_v^2$ , with  $v = d + 2N$  degrees of freedom.<br>3. Set  $x(t + \Delta) = \chi_v^2 \cdot \exp(-\kappa \Delta) / n(t, t + \Delta)$ .

Steps 1 and 3 of this algorithm are straightforward, but Step 2 is somewhat involved. In practice, generation of chi-squared variables would most often use one of several available techniques for the gamma distribution, a special case of which is the chi-square distribution. A standard algorithm for the generation of gamma variates of acceptance-rejection type is the Cheng-Feast algorithm [5], and a number of others are listed in [9], though direct generation by the aid of the inverse cumulative distribution function [6] is also a practically viable option.

We should note that if  $d > 1$ , it may be numerically advantageous to use a different algorithm, based on the convenient relation

$$\chi_d^{\prime 2}(\lambda) \stackrel{d}{=} \left(Z + \sqrt{\lambda}\right)^2 + \chi_{d-1}^2 \ , \quad d > 1 \quad (6)$$

where  $\stackrel{d}{=}$  denotes equality in distribution,  $\chi_d^2(\lambda)$  is a noncentral chi-square variable with  $d$  degrees of freedom and noncentrality parameter  $\lambda$ , and Z is an ordinary  $\mathcal{N}(0, 1)$  Gaussian variable. We trust that the reader can complete the details on application of equation (6) in a simulation algorithm for  $x(t + \Delta)$ .

One might think that the existence of an exact simulation scheme for  $x(t + \Delta)$  would settle once and for all the question of how to generate paths of the square-root process. In practice, however, several complications may arise with the application of the algorithm mentioned earlier. Indeed, the scheme is quite complex compared with many standard SDE discretization schemes and may not fit smoothly into existing software architecture for SDE simulation routines. Also, computational speed may be an issue, and the application of acceptance-rejection sampling will potentially cause a "scrambling effect" when process parameters are perturbed, resulting in poor sensitivity computations. While caching techniques can be designed to overcome some of these issues. storage, look-up, and interpolation of such a cache pose their own challenges. Further, the basic scheme above provides no explicit link between the paths of the Brownian motion  $W(t)$  and that of  $x(t)$ , complicating applications in which, say, multiple correlated Brownian motions need to be advanced through time.

In light of the discussion earlier, it seems reasonable to also investigate the application of simpler simulation algorithms. These will typically exhibit a bias for finite values of  $\Delta$ , but convenience and speed may more than compensate for this, especially if the bias is small and easy to control by reduction of stepsize. We proceed to discuss several classes of such schemes.

## Biased Taylor-type Schemes

**Euler Schemes.** Going forward, let us use  $\hat{x}$  to denote a discrete-time (biased) approximation to  $x$ . A classical approach to constructing simulation schemes for SDEs involves the application of Itô-Taylor expansions, suitably truncated. See **Monte Carlo** Simulation for Stochastic Differential Equations, Stochastic Differential Equations: Scenario Simulation, and Stochastic Taylor Expansions for details.

The simplest of such schemes is the *Euler scheme*, a direct application of which would write

$$\hat{x}(t + \Delta) = \hat{x}(t) + \kappa(\theta - \hat{x}(t))\Delta \n+ \epsilon \sqrt{\hat{x}(t)} Z\sqrt{\Delta} \n$$
(7)

where Z is  $\mathcal{N}(0, 1)$  Gaussian variable. One immediate (and fatal) problem with equation  $(7)$  is that the discrete process for  $x$  can become negative with nonzero probability, making computation of  $\sqrt{\hat{x}(t)}$ impossible and causing the time-stepping scheme to fail. To get around this problem, several remedies have been proposed in the literature, starting with the suggestion in [13] that one simply replaces  $\sqrt{\hat{x}(t)}$  in equation (7) with  $\sqrt{\left|\hat{x}(t)\right|}$ . Lord *et al.*, [14] review a number of such "fixes", concluding that the following works best:

$$\hat{x}(t+\Delta) = \hat{x}(t) + \kappa(\theta - \hat{x}(t)^{+})\Delta$$
$$+ \epsilon \sqrt{\hat{x}(t)^{+}} Z\sqrt{\Delta} \tag{8}$$

where we use the notation  $x^+ = \max(x, 0)$ . In [14] this scheme is denoted "full truncation"; its main characteristic is that the process for  $\hat{x}$  is allowed to go below zero, at which point the process for  $x$  becomes deterministic with an upward drift of  $\kappa\theta$ .

**Higher-order Schemes.** The scheme (8) has firstorder weak convergence, in the sense that expectations of functions of  $x$  will approach their true values as  $\mathcal{O}(\Delta)$ . To improve convergence, it is tempting to apply a *Milstein scheme*, the most basic of which is

$$\hat{x}(t+\Delta) = \hat{x}(t) + \kappa(\theta - \hat{x}(t))\Delta$$
$$+ \epsilon \sqrt{\hat{x}(t)} Z\sqrt{\Delta} + \frac{1}{4} \epsilon^2 \Delta \left(Z^2 - 1\right) \tag{9}$$

As was the case for equation  $(7)$ , this scheme has a positive probability of generating negative values of  $\hat{x}$  and therefore cannot be used without suitable modifications. Kahl and Jäckel [11] list several other Milstein-type schemes, some of which allow for a certain degree of control over the likelihood of generating negative values. One particularly appealing variation is the *implicit Milstein scheme*, defined as

$$\hat{x}(t+\Delta) = (1+\kappa\Delta)^{-1} \cdot \left(\hat{x}(t) + \kappa\theta\Delta\right)$$
$$+\epsilon\sqrt{\hat{x}(t)} Z\sqrt{\Delta} + \frac{1}{4}\epsilon^2\Delta(Z^2 - 1)\right) \tag{10}$$

It is easy to verify that this discretization scheme results in strictly positive paths for the  $x$  process if  $4\kappa\theta > \epsilon^2$ . For cases where this bound does not hold, it will be necessary to modify equation (10) to prevent problems with the computation of  $\sqrt{\hat{x}(t)}$ . For instance, whenever  $\hat{x}(t)$  drops below zero, we could use equation  $(8)$  rather than equation  $(10)$ .

Under certain sufficient regularity conditions, Milstein schemes have second-order weak convergence. Owing to the presence of a square root in equation (1), these sufficient conditions are violated here, and one should not expect equation  $(10)$  to have second-order convergence for all parameter values, even the ones that satisfy  $4\kappa\theta > \epsilon^2$ . Numerical tests of Milstein schemes for square-root processes can be found in [9] and [11]; overall these schemes perform fairly well in certain parameter regimes, but are typically less robust than the Euler scheme.

## Moment-matching Schemes

Lognormal Approximation. The simulation schemes introduced in the section Biased Taylor-type Schemes all suffer to various degrees from an inability to keep the path of  $x$  nonnegative throughout. One, rather obvious, way around this is to draw  $\hat{x}(t + \Delta)$ from a user-selected probability distribution that (i) is reasonably close to the true distribution of  $x(t + \Delta)$ and (ii) is certain not to produce negative values. To ensure that (i) is satisfied, it is natural to select the parameters of the chosen distribution to match one or more of the true moments for  $x(t + \Delta)$ , conditional upon  $x(t) = \hat{x}(t)$ . For instance, if we assume that the true distribution of  $x(t + \Delta)$  is well approximated by a lognormal distribution with parameters  $\mu$  and  $\sigma$ , we write (see  $[2]$ )

$$\hat{x}(t+\Delta) = e^{\mu+\sigma Z} \tag{11}$$

where Z is a Gaussian random variable, and  $\mu$ ,  $\sigma$  are chosen to satisfy

$$e^{\mu + \frac{1}{2}\sigma^2} = E\left(x(t+\Delta)|x(t) = \hat{x}(t)\right)$$

$$e^{2\left(\mu + \frac{1}{2}\sigma^2\right)}\left(e^{\sigma^2} - 1\right) = \text{Var}\left(x(t+\Delta)|x(t) = \hat{x}(t)\right)$$
(13)

The results in Corollary 1 can be used to compute the right-hand sides of this system of equations, which can then easily be solved analytically for *µ* and *σ*.

As is the case for many other schemes, equation (11) works best if the Feller condition is satisfied. If not, the lower tail of the lognormal distribution is often too thin to capture the true distribution shape of *x(t* ˆ + *)*—see Figure 1.

**Truncated Gaussian.** Figure 1 demonstrates that the density of *x(t* ˆ + *)* may sometimes be nearly singular at the origin. To accommodate this, one could contemplate inserting an actual singularity through outright truncation at the origin of a distribution that may otherwise go negative. Using a Gaussian distribution for this, say, one could write

$$\hat{x}(t+\Delta) = (\mu + \sigma Z)^{+} \tag{14}$$

where *µ* and *σ* are determined by moment-matching, along the same lines as in the section Lognormal Approximation. While this moment-matching exercise cannot be done in an entirely analytical fashion, a number of caching tricks outlined in [3] can be used to make the determination of *µ* and *σ* essentially instantaneous. As documented in [3], the scheme (14) is robust and generally has attractive convergence properties when applied to standard option pricing problems. Being fundamentally Gaussian when *x(t)* ˆ is far from the origin, equation (14) is somewhat similar to the Euler scheme (8), although the performance

![](_page_3_Figure_6.jpeg)

**Figure 1** Cumulative distribution function for *x(T )* given *x(*0*)*, with *T* = 0*.*1. Model parameters were *x(*0*)* = *θ* = 4%, *κ* = 50%, and = 100%. The lognormal and Gaussian distributions in the graph were parameterized by matching mean and variances to the exact distribution of *x(T )*

of equation (14) is typically better than equation (8). Unlike equation (8), the truncated Gaussian scheme (14) also ensures, by construction, that negative values of *x(t* ˆ + *)* cannot be attained.

**Quadratic-exponential.** We finish our discussion of biased schemes for equation (1) with a more elaborate moment-matched scheme, based on a combination of a squared Gaussian and an exponential distribution. In this scheme, for large values of *x(t)* ˆ , we write

$$\hat{x}(t+\Delta) = a\,(b+Z)^2\tag{15}$$

where *Z* is a standard Gaussian random variable, and *a* and *b* are certain constants, to be determined by moment-matching. These constants *a* and *b* depend on the time step and *x(t)* ˆ , as well as the parameters in the SDE for *x.* While based on the well-established asymptotics for the noncentral chi-square distribution (see [3]), formula (15) does not work well for low values of *x(t)* ˆ —in fact, the moment-matching exercise fails to work—so we supplement it with a scheme to be used when *x(t)* ˆ is small. Andersen [3] shows that a good choice is to approximate the density of *x(t* ˆ + *)* with

$$\Pr\left(\hat{x}(t+\Delta) \in [x, x+dx]\right)$$
  
 
$$\approx \left(p\delta(x) + \beta(1-p)e^{-\beta x}\right) dx \ , \quad x \ge 0 \tag{16}$$

where *δ* is a Dirac delta-function, and *p* and *β* are nonnegative constants to be determined. As in the scheme in the section Truncated Gaussian, we have a probability mass at the origin, but now the strength of this mass *(p)* is explicitly specified, rather than implied from other parameters. The mass at the origin is supplemented with an exponential tail. It can be verified that if *p* ∈ [0*,* 1] and *β* ≥ 0, then equation (16) constitutes a valid density function.

Assuming that we have determined *a* and *b*, Monte Carlo sampling from equation (15) is trivial. To draw samples in accordance with equation (16), we can generate a cumulative distribution function

$$\Psi(x) = \Pr\left(\hat{x}(t+\Delta) \le x\right) \\
= p + (1-p)\left(1 - e^{-\beta x}\right), \quad x \ge 0 \quad (17)$$

the inverse of which is readily computable, allowing for efficient generation of random draws by the inverse distribution method.

What remains is the determination of the constants *a*, *b*, *p*, and *β*, as well as a rule for when to switch from equation  $(15)$  to sampling from equation (17). The first problem is easily settled by moment-matching techniques.

**Proposition 3** Let  $m \stackrel{\Delta}{=} E(x(t + \Delta)|x(t) = \hat{x}(t))$ and  $s^2 \stackrel{\Delta}{=} \text{Var}\left(x(t+\Delta)|x(t) = \hat{x}(t)\right)$  and set  $\psi =$  $s^2/m^2$ . Provided that  $\psi \leq 2$ , set

$$b^{2} = 2\psi^{-1} - 1 + \sqrt{2\psi^{-1}}\sqrt{2\psi^{-1} - 1} \ge 0 \quad (18)$$

and

$$a = \frac{m}{1+b^2} \tag{19}$$

Let  $\hat{x}(t + \Delta)$  be as defined in equation (15); then  $\mathrm{E}\left(\hat{x}(t+\Delta)\right) = m \text{ and } \mathrm{Var}\left(\hat{x}(t+\Delta)\right) = s^2.$ 

**Proposition 4** Let m, s, and  $\psi$  be as defined in *Proposition 3. Assume that*  $\psi \ge 1$  *and set* 

$$p = \frac{\psi - 1}{\psi + 1} \in [0, 1) \tag{20}$$

and

$$\beta = \frac{1-p}{m} = \frac{2}{m(\psi+1)} > 0 \tag{21}$$

Let  $\hat{x}(t + \Delta)$  be sampled from equation (17); then  $\mathrm{E}\left(\hat{x}(t+\Delta)\right) = m \text{ and } \mathrm{Var}\left(\hat{x}(t+\Delta)\right) = s^2.$ 

The terms m, s,  $\psi$  defined in the two propositions above are explicitly computable from the result in Corollary 1. For any  $\psi_c$  in [1, 2], a valid switching *rule* is to use equation (15) if  $\psi \leq \psi_c$  and to sample equation (17) otherwise. The exact choice for  $\psi_c$  is noncritical;  $\psi_c = 1.5$  is a good choice.

The quadratic-exponential (QE) scheme outlined above is typically the most accurate of the biased schemes introduced in this article. Indeed, in most practical applications, the bias introduced by the scheme is statistically undetectable at the levels of Monte Carlo noise acceptable in practical applications; see [3] for numerical tests under a range of challenging conditions. Variations on the QE scheme without an explicit singularity in zero can also be found in [3].

## **Stochastic Volatility Simulation**

As mentioned earlier, square-root processes are commonly used to model stochastic movements in the volatility of some financial asset. A popular example of such an application is the *Heston model* [10], defined by a vector SDE of the form<sup>a</sup>

$$dY(t) = Y(t)\sqrt{x(t)} \, dW_Y(t) \tag{22}$$

$$dx(t) = \kappa \left(\theta - x(t)\right) dt + \epsilon \sqrt{x(t)} dW(t) \quad (23)$$

 $dW_Y(t) \cdot dW(t) = \rho dt, \quad \rho \in [-1, 1].$  For with numerical work, it is useful to recognize that the process for  $Y(t)$  is often relatively close to geometric Brownian motion, making it sensible to work with logarithms of  $Y(t)$ , rather than  $Y(t)$  itself. An application of Itô's Lemma shows that equations  $(22)$ – $(23)$ are equivalent to

$$d\ln Y(t) = -\frac{1}{2}x(t) dt + \sqrt{x(t)} dW_Y(t)$$
 (24)

$$dx(t) = \kappa \left(\theta - x(t)\right) dt + \epsilon \sqrt{x(t)} dW(t) \tag{25}$$

We proceed to consider the joint simulation of equations  $(24)$ – $(25)$ .

#### Broadie-Kaya Scheme

As demonstrated in [4], it is possible to simulate equations  $(24)$ – $(25)$  bias-free. To show this, first integrate the SDE for  $x(t)$  and rearrange.

$$\int_{t}^{t+\Delta} \sqrt{x(u)} \, \mathrm{d}W(u)$$
  
=  $\epsilon^{-1} \left( x(t+\Delta) - x(t) - \kappa\theta\Delta + \kappa \int_{t}^{t+\Delta} x(u) \, \mathrm{d}u \right)$   
(26)

Performing a Cholesky decomposition we can also write

$$d\ln Y(t) = -\frac{1}{2}x(t) dt + \rho\sqrt{x(u)} dW(u) + \sqrt{1 - \rho^2}\sqrt{x(u)} dW^*(u)$$
 (27)

where  $W^*$  is a Brownian motion independent of W. An integration yields

$$\ln Y(t+\Delta) = \ln Y(t) + \frac{\rho}{\epsilon} \left( x(t+\Delta) - x(t) - \kappa \theta \Delta \right)$$
$$+ \left( \frac{\kappa \rho}{\epsilon} - \frac{1}{2} \right) \int_{t}^{t+\Delta} x(u) \, \mathrm{d}u$$
$$+ \sqrt{1-\rho^2} \int_{t}^{t+\Delta} \sqrt{x(u)} \, \mathrm{d}W^*(u) \tag{28}$$

where we have used equation (26). Conditional on  $x(t+\Delta)$  and  $\int_{t}^{t+\Delta} x(u) \, \mathrm{d}u$ , it is clear that the distribution of  $\ln Y(t + \Delta)$  is Gaussian with easily computable moments. After first sampling  $x(t + \Delta)$  from the noncentral chi-square distribution (as described in the section Exact Simulation), one then performs the following steps:

- 1. Conditional on  $x(t + \Delta)$  (and  $x(t)$ ) draw a sample of  $I = \int_{t}^{t+\Delta} x(u) \, \mathrm{d}u$ .
- 2. Conditional on  $x(t + \Delta)$  and I, use equation (28) to draw a sample of  $\ln Y(t + \Delta)$  from a Gaussian distribution.

While execution of the second step is straightforward, the first one is decidedly not, as the conditional distribution of the integral  $I$  is not known in closed form. In [4], the authors instead derive a characteristic function, which they numerically Fourier-invert to generate the cumulative distribution function for I, given  $x(t + \Delta)$  and  $x(t)$ . Numerical inversion of this distribution function over a uniform random variable finally allows for generation of a sample of  $I$ . The total algorithm requires great care in numerical discretization to prevent introduction of noticeable biases and is further complicated by the fact that the characteristic function for  $I$  contains two modified Bessel functions.

The Broadie-Kaya algorithm is bias-free by construction, but its complexity and lack of speed is problematic in some applications. At the cost of introducing a (small) bias, [15] improves computational efficiency by introducing certain approximations to the characteristic function of time-integrated variance, enabling efficient caching techniques.

### Other Schemes

Taylor-type Schemes. In their examination of "fixed" Euler schemes, Lord et al. [14] suggest simulation of the Heston model by combining equation (8) with the following scheme for  $\ln Y$ :

$$\ln \hat{Y}(t+\Delta) = \ln \hat{Y}(t) - \frac{1}{2}\hat{x}(t)^{+}\Delta$$
$$+ \sqrt{\hat{x}(t)^{+}}Z_{Y}\sqrt{\Delta} \qquad (29)$$

where  $Z_Y$  is a Gaussian  $\mathcal{N}(0, 1)$  draw, correlated to Z in equation (8) with correlation coefficient  $\rho$ . For the periods where  $\hat{x}$  drops below zero in equation (8), the process for  $\hat{Y}$  comes to a standstill.

Kahl and Jäckel [11] consider several alternative schemes for  $Y$ , the most prominent being the "IJK" scheme, defined as

$$\ln \hat{Y}(t+\Delta) = \ln \hat{Y}(t)$$
$$-\frac{\Delta}{4} \left(\hat{x}(t+\Delta) + \hat{x}(t)\right) + \rho \sqrt{\hat{x}(t)} Z \sqrt{\Delta}$$
$$+\frac{1}{2} \left(\sqrt{\hat{x}(t+\Delta)} + \sqrt{\hat{x}(t)}\right) \left(Z_Y \sqrt{\Delta} - \rho Z \sqrt{\Delta}\right)$$
$$+\frac{1}{4} \epsilon \rho \Delta \left(Z^2 - 1\right) \tag{30}$$

Here,  $\hat{x}(t + \Delta)$  and  $\hat{x}(t)$  are meant to be simulated by the implicit Milstein scheme  $(5)$ ; again the correlation between the Gaussian samples  $Z_{\gamma}$  and Z is  $\rho$ .

**Simplified Broadie–Kaya.** We recall from the discussion earlier that the complicated part of the Broadie-Kaya algorithm was the computation of  $\int_{t}^{t+\Delta} x(u) \, \mathrm{d}u$ , conditional on  $x(t)$  and  $x(t+\Delta)$ . Andersen [3] suggests a naive, but effective, approximation based on the idea that

$$\int_{t}^{t+\Delta} x(u) \, \mathrm{d}u \approx \Delta \left[ \gamma_1 x(t) + \gamma_2 x(t+\Delta) \right] \quad (31)$$

for certain constants  $\gamma_1$  and  $\gamma_2$ . The constants  $\gamma_1$ and  $\gamma_2$  can be found by moment-matching techniques (using results from [8], p. 16), but [3] presents evidence that it will often be sufficient to use either an Euler-like setting  $(\gamma_1 = 1, \gamma_2 = 0)$  or a central discretization  $(\gamma_1 = \gamma_2 = \frac{1}{2})$ . In any case, equation  $(30)$  combined with equation  $(27)$  gives rise to a scheme for  $Y$ -simulation that can be combined with any basic algorithm that can produce  $\hat{x}(t)$  and  $\hat{x}(t + \Delta)$ . Andersen [3] provides numerical results for the case where  $\hat{x}(t)$  and  $\hat{x}(t + \Delta)$  are simulated by the algorithms in the sections Truncated Gaussian and Quadratic-exponential; the results are excellent, particularly when the QE algorithm in the section Quadratic-exponential is used to sample  $x$ .

Martingale Correction. Finally, let us note that some of the schemes outlined above (including equation (29) and the one in the section Simplified Broadie-Kaya) generally do not lead to martingalebehavior of  $\hat{Y}$ ; that is,  $E(\hat{Y}(t+\Delta)) \neq E(\hat{Y}(t))$ . For the cases where the error *e* = E*(Y (t* ˆ + *))* − E*(Y (t))* ˆ is analytically computable, it is, however, straightforward to remove the bias by simply adding −*e* to the sample value for *Y (t* ˆ + *)*. Andersen [3] gives several examples of this idea.

# **Further Reading**

In this article, we restricted ourselves to the presentation of relatively simple methods, which in the two-dimensional Heston model setting only require two variates per time step. Such schemes are often the most convenient in actual trading systems and for implementations that rely on Wiener processes built from low discrepancy numbers. More complicated high-order Taylor schemes, which often require extra variates, are described in [13]. The efficacy of such methods are, however, unproven in the specific setting of the Heston model.

In recent work, Alfonsi [1] constructs a secondorder scheme for the CIR process, using a switching idea similar to that of the QE scheme. For the Heston process, Alfonsi develops a "second-order scheme candidate" involving three variates per time step; the numerical performance of the scheme compares favorably with Euler-type schemes.

# **End Notes**

a*.* We assume that *Y* is a martingale in the chosen measure; adding a drift is straightforward.

# **References**

- [1] Alfonsi, A. (2008). *A Second-Order Discretization Scheme for the CIR Process: Application to the Heston Model*, Working Paper, Institut fur Mathematik, TU, ¨ Berlin.
- [2] Andersen, L. & Brotherton-Ratcliffe, R. (2005). Extended Libor market models with stochastic volatility, *Journal of Computational Finance* **9**(1), 1–40.
- [3] Andersen, L. (2008). Simple and efficient simulation of the Heston stochastic volatility model, *Journal of Computational Finance* **11**(3), 1–42.

- [4] Broadie, M. & Kaya, O. (2006). Exact simulation of ¨ stochastic volatility and other affine jump diffusion processes, *Operations Research* **54**(2), 217–231.
- [5] Cheng, R. & Feast, G. (1980). Gamma variate generators with increased shape parameter range, *Communications of the ACM* **23**(7), 389–394.
- [6] DiDonato, A.R. & Morris, A.H. (1987). Incomplete gamma function ratios and their inverse, *ACM TOMS* **13**, 318–319.
- [7] Duffie, D., Pan, J. & Singleton, K. (2000). Transform analysis and asset pricing for affine jump diffusions, *Econometrica* **68**, 1343–1376.
- [8] Dufresne, D. (2001). *The Integrated Square-Root Process*, Working Paper, University of Montreal.
- [9] Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*, Springer Verlag, New York.
- [10] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**(2), 327–343.
- [11] Kahl, C. & Jackel, P. (2006). Fast strong approximation ¨ Monte Carlo schemes for stochastic volatility models, *Journal of Quantitative Finance* **6**(6), 513–536.
- [12] Karlin, S. & Taylor, H. (1981). *A Second Course in Stochastic Processes*, Academic Press.
- [13] Kloeden, P. & Platen, E. (1999). *Numerical Solution of Stochastic Differential Equations*, 3rd Edition, Springer Verlag, New York.
- [14] Lord, R., Koekkoek, R. & van Dijk, D. (2006). *A Comparison of Biased Simulation Schemes for Stochastic Volatility Models*, Working Paper, Tinbergen Institute, Amsterdam.
- [15] Smith, R. (2007). An almost exact simulation method for the Heston model, *Journal of Computational Finance* **11**(1), 115–125.

# **Related Articles**

**Affine Models**; **Cox–Ingersoll–Ross (CIR) Model**; **Heston Model**; **Monte Carlo Simulation for Stochastic Differential Equations**; **Stochastic Differential Equations: Scenario Simulation**; **Stochastic Taylor Expansions**.

LEIF B.G. ANDERSEN, PETER JACKEL ¨ & CHRISTIAN KAHL
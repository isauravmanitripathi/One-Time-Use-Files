# **Barndorff-Nielsen and** Shephard (BNS) Models

Stochastic volatility models based on non-Gaussian Ornstein-Uhlenbeck (OU)-type processes were introduced in [3]. The motivation was to construct a mathematically tractable model that provides an adequate description of price fluctuations on various timescales. The main idea is to model the volatility with a non-Gaussian OU process: solution of a linear Stochastic differential equation (SDE) with Lévy increments. The non-Gaussian increments allow to build a process that is positive and linear, meaning that many computations are very simple.

# Non-Gaussian Ornstein-Uhlenbeck-type Processes

The OU-type process (see [8, 11, 12] for original introduction or [2, 4, 10] for a more modern treatment) is defined as the solution of the stochastic differential equation

$$\mathbf{d}y_t = -\lambda y_t + \mathbf{d}Z_t \tag{1}$$

where  $Z$  is a Lévy process. It can be explicitly written as

$$y_t = y_0 e^{-\lambda t} + \int_0^t e^{-\lambda(t-s)} dZ_s$$
 (2)

At any time t, the distribution of  $y_t$  is infinitely divisible. If the characteristic triplet of Z is  $(A, \nu, \gamma)$ , the characteristics of  $y_t$  are given by

$$A_t^y = \frac{A}{2\lambda} \{ 1 - e^{-2\lambda t} \}$$
  

$$\gamma_t^y = \frac{\gamma}{\lambda} \{ 1 - e^{-\lambda t} \} + y_0 e^{-\lambda t}$$
  

$$\nu_t^y = \int_1^{e^{\lambda t}} \nu(\xi B) \frac{\mathrm{d}\xi}{\lambda \xi} \quad \forall B \in \mathcal{B}(\mathbb{R}) \tag{3}$$

and the characteristic function of  $y_t$  is

$$E[e^{iuy_t}] = \exp\left(iuy_0e^{-\lambda t} + \int_0^t \psi(ue^{\lambda(s-t)})\,ds\right) \tag{4}$$

with  $\psi(u) = \ln E[e^{iuZ_1}]$ . Under the integrability condition  $\int_{|x|>1} \ln |x| \nu(\mathrm{d}x) < \infty$ , the process  $(y_t)$  has a stationary distribution with characteristics

$$A^{y} = \frac{A}{2\lambda}, \quad \gamma^{y} = \frac{\gamma}{\lambda}, \quad \nu^{y}(B)$$
$$= \int_{1}^{\infty} \nu(\xi B) \frac{\mathrm{d}\xi}{\lambda \xi}, \quad \forall B \in \mathcal{B}(\mathbb{R}) \tag{5}$$

In the stationary case, an OU-type process has an exponential (short memory) autocorrelation structure:

$$Cov(y_t, y_{t+s}) = e^{-\lambda s} \text{Var } y_t \tag{6}$$

To obtain more interesting correlation structures, one can add up several OU-type processes [1]: if  $y$  and  $\tilde{y}$  are independent stationary OU-type processes with parameters  $\lambda$  and  $\tilde{\lambda}$  then

$$\text{Cov}(y_t + \tilde{y}_t, y_{t+s} + \tilde{y}_{t+s}) = e^{-\lambda s} \text{Var } y_t$$
$$+ e^{-\tilde{\lambda}s} \text{Var } \tilde{y}_t \quad (7)$$

The price to be paid is an increased model dimension: the two-dimensional process  $(y, \tilde{y})$  is Markov but the sum  $y + \tilde{y}$  is not. Superpositions of OUtype processes can also be used to construct finitedimensional approximations to non-Markov (e.g., long memory) processes.

#### **Positive OU-type processes**

Positive OU-type processes can be used as linear models for stationary financial time series such as volatility (discussed below) or commodity prices (see [6]). An OU-type process is positive if the driving Lévy process  $Z$  is a positive Lévy process, also known as a *subordinator*. In this case, the trajectory consists of a series of positive jumps with exponential decay between them like in Figure 1.

#### **Model Specification and Examples**

The "econometric" (as opposed to risk-neutral) version of the Barndorff-Neilsen and Shephard (BNS) stochastic volatility model has the form

$$S_t = S_0 \exp(X_t)$$
  

$$dX_t = \left(\mu + \beta \sigma_t^2\right) dt + \sigma_t dW_t + \rho dZ_t \rho \le 0$$
  

$$d\sigma_t^2 = -\lambda \sigma_t^2 dt + dZ_t \quad \sigma_0^2 > 0$$
(8)

![](_page_1_Figure_1.jpeg)

Figure 1 Sample trajectory of a positive OU-type process

The log stock price is a stochastic volatility process with downward jumps  $(Z \text{ has only positive jumps})$ and the volatility is a positive OU-type process. Introducing  $Z$  into the equation for the log price with a negative coefficient accounts for the *leverage effect*: volatility jumps up when price jumps down.

Nicolato and Venardos [9] have shown that model (8) is arbitrage-free, that is, one can always find an equivalent martingale measure. Under a martingale measure, the model takes the form

$$S_t = S_0 \exp(X_t)$$
  
$$dX_t = \left(r - l(\rho) - \frac{1}{2}\sigma_t^2\right) dt + \sigma_t dW_t$$
  
$$+ \rho dZ_t$$
  
$$d\sigma_t^2 = -\lambda \sigma_t^2 dt + dZ_t, \quad \sigma_0^2 > 0 \tag{9}$$

where r is the interest rate and  $l(u) := \ln E[e^{uZ_1}]$ .

As an example of a concrete specification, suppose that the stationary distribution  $\mu$  of the squared volatility process  $\sigma_t^2$  is the gamma distribution with density  $\mu(x) = \alpha^{c}/\Gamma(c)x^{c-1}e^{-\alpha x}1_{x>0}$  (this is the same as the stationary distribution of the volatility in Heston's stochastic volatility model). In this case,  $(Z_t)$  has zero drift and a Lévy measure with density  $v(x) = \alpha \lambda c e^{-\alpha x}$ , that is, it is a compound Poisson process with exponential jump size distribution. The Laplace exponent of Z is  $l(u) = \lambda c u/\alpha - u$ .

## **Option Pricing and Hedging**

The BNS models are a subclass of affine processes (see Affine Models) [7]: there is an explicit expression for the characteristic function of log stock price  $X$ . Under the risk-neutral probability,

$$\begin{split} \phi_t(u) &= E[e^{\mathrm{i}uX_t}] \\ &= \exp\left\{\mathrm{i}u(r-l(\rho))t - \mathrm{i}\sigma_0^2\frac{u^2 + \mathrm{i}u}{2}\varepsilon(\lambda, t) \\ &+ \int_0^t l\Big(\mathrm{i}\rho u - \frac{u^2 + \mathrm{i}u}{2}\varepsilon(\lambda, t-s)\Big)\,\mathrm{d}s\right\} \end{split} \tag{10}$$

with  $\varepsilon(\lambda, t) := 1 - e^{-\lambda t}/t$ . This means that if the risk-neutral parameters are known, European options can be priced by Fourier inversion (see **Exponential Lévy Models**). The expected integrated variance is

$$E\left[\int_{0}^{t} \sigma_{s}^{2} \, \mathrm{d}s\right] = \sigma_{0}^{2} \frac{1 - \mathrm{e}^{-\lambda t}}{\lambda} + E[Z_{1}] \frac{\mathrm{e}^{-\lambda t} - 1 + \lambda t}{\lambda^{2}} \quad (11)$$

leading to a simple explicit formula for the fair rate of a variance swap.

The market being generally incomplete, there exist many risk-neutral probabilities and the prices of contingent claims are not unique. The solution is to select the risk-neutral probability implied by the market, calibrating the model parameters to a set of quoted option prices. Nicolato and Venardos [9] carry out the calibration exercise by the usual technique of nonlinear least squares:

$$\min_{\theta} \sum_{i=1}^{N} (C_i^M - C^{\theta}(T_i, K_i))^2 \tag{12}$$

where N is the total number of observations,  $C_i^M$  is the observed price of the option with strike  $K_i$  and time to maturity  $T_i$ , and  $C^{\theta}(T_i, K_i)$  is the price of this option evaluated in a model with parameter vector  $\theta$ . This method appears to work well in [9] but in other situations two problems may arise:

Lack of flexibility: in BNS models, the same parameter  $\rho$  determines the size of jumps in the price process (and hence the short-maturity skew or asymmetry of the implied volatility smile) and the correlation between the price process and the volatility (the long-dated skew). For this reason, the model may be difficult to calibrate in markets with pronounced skew changes from short to long maturities such as FX markets.

Lack of stability: since the calibration functional  $(12)$  is not convex and the number of model parameters may be large, the calibration algorithm may be caught in a local minimum, which leads to instabilities in the calibration procedure. Usual remedies for this problem include the use of global minimization algorithms such as simulated annealing or adding a convex penalty term to the functional  $(12)$  to make the problem well posed.

The minimal variance hedging in BNS models is discussed in [5]. Let the option price at time  $t$ be given by  $C(t, S_t, \sigma_t^2)$  (this can be computed by Fourier transform). The hedging strategy minimizing the variance of the residual hedging error under the risk-neutral probability is then given by

$$\begin{split} \phi_t &= \left[ \sigma_{t-}^2 \frac{\partial C}{\partial S} + \frac{1}{S_{t-}} \int \nu(\,\mathrm{d}z) (\mathrm{e}^{\rho z} - 1) \right. \\ & \times \left[ C(t, \, S_{t-} \mathrm{e}^{\rho z}, \, \sigma_{t-}^2 + z) - C(t, \, S_{t-}, \, \sigma_{t-}^2) \right] \\ & \times \left[ \sigma_{t-}^2 + \int (\mathrm{e}^{\rho z} - 1)^2 \nu(\,\mathrm{d}z) \right]^{-1} \end{split} \tag{13}$$

When there are no jumps in the stock price ( $\rho = 0$ ), the optimal hedging strategy is just delta-hedging:  $\phi_t = \partial C/\partial S$ ; even though there are jumps in the option price, they cannot be hedged using stock only, because the stock does not jump.

#### References

- Barndorff-Nielsen, O.E. (2001). Superposition of [1] Ornstein-Uhlenbeck type processes, Theory of Probability and Its Applications 45, 175-194.
- [2] Barndorff-Nielsen, O.E., Jensen, J.L. & Sørensen, M. (1998). Some stationary processes in discrete and continuous time, Advances in Applied Probability 30, 989-1007.

- Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-[3] Gaussian Ornstein-Uhlenbeck based models and some of their uses in financial econometrics, Journal of the Royal Statistical Society: Series B 63, 167-241.
- Cont, R. & Tankov, P. (2004). Financial Modelling with [4] Jump Processes, Chapman & Hall/CRC Press.
- [5] Cont, R., Tankov, P. & Voltchkova, E. (2007). Hedging with options in models with jumps, in Stochastic Analysis and Applications: The Abel Symposium 2005 in Honor of Kiyosi Ito, F.E. Benth, G. Di Nunno, T. Lindstrom, B. Øksendal & T. Zhang, eds, Springer, pp. 197-218.
- Deng, S.-J. & Jiang, W. (2005). Lévy process-driven [6] mean-reverting electricity price model: the marginal distribution analysis, Decision Support Systems 40,  $483 - 494$
- [7] Duffie, D., Filipovic, D. & Schachermayer, W. (2003). Affine processes and applications in finance, Annals of Applied Probability 13, 984-1053.
- [8] Jurek, Z.J. & Vervaat, W. (1983). An integral representation for self-decomposable Banach space valued random variables, Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 62(2), 247-262.
- [9] Nicolato, E. & Venardos, E. (2003). Option pricing in stochastic volatility models of Ornstein-Uhlenbeck type. *Mathematical Finance* **13**, 445–466.
- [10] Sato, K. (1999). *Lévy Processes and Infinitely Divisible* Distributions, Cambridge University Press, Cambridge.
- [11] Sato K. & Yamazato M. (1983). Stationary processes of Ornstein-Uhlenbeck type, in *Probability Theory and* Mathematical Statistics, Fourth USSR-Japan Symposium, K. Itô & V. Prokhorov, eds, Lecture Notes in Mathematics, Vol. 1021, Springer, Berlin.
- [12] Wolfe, S.J. (1982). On a continuous analogue of the stochastic difference equation  $x_n = \rho x_{n-1} + b_n$ , Stochastic Processes and Applications 12(3), 301–312.

### **Related Articles**

Exponential Lévy Models; Lévy Processes; Ornstein–Uhlenbeck Processes.

PETER TANKOV
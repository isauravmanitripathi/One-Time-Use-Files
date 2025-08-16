# Ornstein-Uhlenbeck Processes

There are several reasons why Ornstein-Uhlenbeck processes are of practical interest in financial stochastic modeling. These continuous-time stochastic processes offer the possibility of capturing important distributional deviations from Gaussianity and for flexible modeling of dependence structures, while retaining analytic tractability.

An *Ornstein-Uhlenbeck* (OU) process is defined as the solution  $X_t$  of a Langevin-type stochastic differential equation (SDE)  $dX_t = -\lambda X_t dt + dZ_t$ where  $\lambda > 0$  and  $Z_t$  is a Lévy process (see Lévy **Processes**). The process is named after L. S. Ornstein and G. E. Uhlenbeck who, in 1930, considered the classical Langevin equation when  $Z$  is a Brownian motion, and hence  $X_t$  is a Gaussian process. Historical notes, references, and details are found in [6, 7] while modeling aspects are found in  $[1]$ . At the time of writing, new extensions and applications of OU processes are thriving, many of them motivated by financial modeling.

#### The Gaussian OU Process

Let  $\{B_t : t \ge 0\}$  be a standard Brownian motion,  $\sigma$  a positive constant, and  $x_0$  a real constant. The classical OU process

$$X_t = e^{-\lambda t} x_0 + \sigma \int_0^t e^{-\lambda(t-s)} dB_s, \quad t \ge 0 \qquad (1)$$

is the solution of the classical Langevin equation  $dX_t = -\lambda X_t dt + \sigma dB_t$ ,  $X_0 = x_0$ . It was originally proposed as a model for the velocity of a Brownian motion and it is the continuous-time analog of the discrete-time autoregressive process  $AR(1)$ . In mathematical finance, OU is used for modeling of the dynamics of interest rates and volatilities of asset prices. The process  $X_t$  is a Gaussian process with (almost surely) continuous sample paths, mean function  $E(X_t) = x_0 \sigma e^{-\lambda t}$ , and covariance

$$\operatorname{Cov}(X_{t}, X_{s}) = \frac{\sigma^{2}}{2\lambda} \left( e^{-\lambda|t-s|} - e^{-\lambda(t+s)} \right) \quad (2)$$

For  $t = s$ , we obtain  $\text{var}(X_t) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda t})$ .<br>Let *N* be a zero-mean Gaussian random variable with variance  $\frac{\sigma^2}{2\lambda}$ , independent of the Brownian motion  $\{B_t : t \ge 0\}$ . The process  $X_t = \sigma e^{-\lambda t} \int_0^t e^{\lambda s} dB_s + N$ is a stationary Gaussian process with  $\text{Cov}(X_t, X_s) =$  $\frac{\sigma^2}{2\lambda}e^{-\lambda|t-s|}$ . Moreover,  $X_t$  is a Markov process with stationary transition probability

$$P_t(x, B) = \frac{\sqrt{\lambda}}{\sigma\sqrt{\pi(1 - e^{-2\lambda t})}}$$
$$\times \int_B \exp\left\{-\frac{\lambda}{\sigma^2} \frac{(y - xe^{-\lambda t})^2}{1 - e^{-2\lambda t}}\right\} dy$$
(3)

#### Non-Gaussian OU Processes

Let  $\{Z_t : t \ge 0\}$  be a Lévy process (see Lévy Processes). A solution of the Langevin-type SDE  $dX_t =$  $-\lambda X_t dt + dZ_t$  is a stochastic process  $\{X_t : t \ge 0\}$ with right-continuous and left-limit paths satisfying the equation

$$X_t = X_0 - \lambda \int_0^t X_s \mathrm{d}s + Z_s, \quad t \ge 0 \qquad (4)$$

When  $X_0$  is independent of  $\{Z_t : t \ge 0\}$ , the unique (almost surely) solution is the OU process

$$X_t = e^{-\lambda t} X_0 + \int_0^t e^{-\lambda(t-s)} dZ_s, \quad t \ge 0 \quad (5)$$

We call  $Z_t$  the background driving Lévy process (BDLP). Of special relevance in financial modeling is the case when  $Z_t$  is a nonnegative increasing Lévy process (a subordinator) and  $X_0$  is nonnegative. The corresponding OU process is positive, moves up entirely by jumps, and then tails off exponentially. Hence it can be used as a variance process.

Every OU process is a time-homogeneous Markov process starting from  $X_0$  and its transition probability  $P_t(x, dy)$  is infinitely divisible (see Infinite Divisibility) with characteristic function (see **Filtering**)

$$\int_{\mathbb{R}} e^{iuy} P_t(x, dy) = \exp\left[ixue^{-\lambda t} + \int_0^t \Psi(e^{-\lambda s}u)ds\right]$$
(6)

where  $\Psi$  is the *characteristic exponent* of the Lévy process  $Z_t$  given by the Lévy-Khintchine representation

$$\Psi(u) = iau - \frac{1}{2}u^2\sigma^2\n$$

$$\n+ \int_{\mathbb{R}} (e^{iux} - 1 - iux1_{|x| \le 1})\Pi(dx), \quad u \in \mathbb{R}\n$$
(7)

where  $\sigma^2 \ge 0$ ,  $a \in \mathbb{R}$ , and  $\Pi$ , the Lévy measure, is a positive measure on  $\mathbb{R}$  with  $\Pi(\{0\}) = 0$ and  $\int_{\mathbb{R}} \min(1, |x|^2) \Pi(dx) < \infty$ . For each  $t > 0$ , the probability distribution of  $Z_t$  has characteristic function  $\varphi_t(u) = E[e^{iuX_t}] = \exp(t\Psi(u))$ . When the Lévy measure is zero,  $Z_t$  is a Brownian motion with variance  $\sigma^2$  and drift a.

## The Integrated OU Process

A non-Gaussian OU process  $X_t$  has the same jump times of  $Z_t$ , as one sees from equation (4). However,  $X_t$  and  $Z_t$  cobreak in the sense that a linear combination of the two does not jump. We see this by considering the continuous integrated OU process  $I_t^X =$  $\int_0^t X_s ds$ , which has two alternative representations

$$I_t^X = \lambda^{-1} \{ X_0 - X_t + Z_t \} = \lambda^{-1} (1 - e^{-\lambda t}) X_0$$
$$+ \lambda^{-1} \int_0^t \left\{ 1 - e^{-\lambda (t-s)} \right\} dZ_s \tag{8}$$

In the Gaussian case, the process  $I_t^X$  is interpreted as the displacement of the Brownian particle. In financial applications,  $I_t^X$  is used to model integrated variance  $[1]$ .

## **Stationary Distribution and the Stationary OU Process**

An OU process has an asymptotic distribution  $\mu$ when  $t \to \infty$  if it does not have too many big jumps. This is achieved if  $Z_1$  is  $\text{ID}_{\text{log}}$ :  $\int_{|x|>2} \ln |x| \Pi(dx)$  $< \infty$ , where  $\Pi$  is the Lévy measure of  $Z_1$ . In this case,  $\mu$  does not depend on  $X_0$  and we call  $\mu$  the stationary distribution of  $X_t$ . Moreover,  $\mu$  is a selfdecomposable (SD) distribution (and hence infinitely divisible): for any  $\theta \in (0, 1)$ , there is a random variable  $\varepsilon_{\theta}$  independent of X such that  $X \stackrel{d}{=} \theta X + \varepsilon_{\theta}$ . Conversely, for every SD distribution  $\mu$  there exists a Lévy process  $Z_t$  with  $Z_1$  being ID<sub>log</sub> and such that  $\mu$  is the stationary distribution of the OU process driven by  $Z_t$ .

The strictly stationary OU process is defined as

$$X_{t} = e^{-\lambda t} \int_{-\infty}^{t} e^{\lambda s} dZ_{s}, \quad t \in \mathbb{R}$$
 (9)

where  $\{Z_t : t \in \mathbb{R}\}$  is a Lévy process constructed as follows: let  $\{Z_t^1 : t \ge 0\}$  be a Lévy process with characteristic exponent  $\Psi_1$  and let  $\{Z_t^2 : t \ge 0\}$  be a Lévy process with characteristic exponent  $\Psi_2(u) =$  $\Psi_1(-u)$  and independent of  $Z^1$ . Then  $Z_t = Z_t^1$  for  $t \ge 0$  and  $Z_t = \overline{Z}_{-t}^2$  for  $t < 0$ . In this case, the law of  $X_t$  is SD and conversely, for any SD law  $\mu$  there exists a BDLP  $Z_t$  such that equation (9) determines a stationary OU process with distribution  $\mu$ . As a result, taking  $X_0 = \int_{-\infty}^0 e^{\lambda s} dZ_s$ , we can always consider (5) as a strictly stationary OU process with a prescribed SD distribution  $\mu$ . It is an important example of a continuous-time moving average process.

#### Generalizations

The monographs  $[6, 7]$  contain a detailed study of multivariate OU process, while matrix extensions are considered in [2]. Another extension is the  $generalized \ OU \ process$ , which has arisen in several financial applications  $[4, 8]$ . It is defined as

$$X_t = e^{-\xi_t} X_0 + e^{-\xi_t} \int_0^t e^{-\xi_s -} d\eta_s, \quad t \ge 0 \quad (10)$$

where  $\{(\xi_t, \eta_t) : t \ge 0\}$  is a bivariate Lévy process, independent of  $X_0$ . This process is a homogeneous Markov process starting from  $X_0$ , and, in general, the existence of the stationary solution depends on the convergence of integrals of exponentials of Lévy processes. For example, when  $\xi$  and  $\eta$  are independent, and if  $\xi_t \to \infty$  and  $V_{\infty} = \int_0^{\infty} e^{-\xi_s} d\eta_s$ is defined and finite, then the law of  $V_{\infty}$  is the unique stationary solution of  $X_t$ . In the dependent case, the generalized OU process admits a stationary solution that does not degenerate to a constant process if and only if  $V_{\infty} = \lim_{t \to \infty} \int_0^t e^{-\xi_s} dL_s$ exists and is finite almost surely and does not

degenerate to constant random variable, and where  $L_t$  is the accompanying Lévy process  $L_t = \eta_t +$  $\sum_{0 < s \le t} (e^{-\Delta \xi_s} - 1) \Delta \eta_s - t \mathbf{E}(B_1^{\xi}, B_1^{\eta}), \text{ where } \Delta \xi_s =$  $\xi_s - \xi_{s-}$ , with  $B_1^{\xi}, B_1^{\eta}$  the Gaussian parts of  $\xi$  and  $\eta$ respectively  $[3, 5]$ .

## References

- [1] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-Gaussian Ornstein-Uhlenbeck-based models and some of their uses in financial economics (with discussion), The Journal of the Royal Statistical Society B 63, 167–241.
- [2] Barndorff-Nielsen, O.E. & Stelzer, R. (2007). Positivedefinite matrix processes of finite variation, Probability and Mathematical Statistics 27, 3-43.
- [3] Carmona, P., Petit, F. & Yor, M. (2001). Exponential functionals of Lévy processes, in Lévy Processes. Theory and Applications, O.E. Barndorff-Nielsen, T. Mikosch & S.I. Resnick, eds, Birkhäuser, pp. 41-55.
- [4] Klüppelberg, C., Linder, A. & Maller, R. (2006). Continuous time volatility modelling: COGARCH versus Ornstein-Uhlenbeck models, in The Shiryaev Festschrift: From Stochastic Calculus to Mathematical Finance,

Y. Kabanov, R. Lipster & J. Stovanov, eds. Springer, рр. 392-419.

- [5] Linder, A. & Maller, R. (2005). Lévy processes and the stationarity of generalised Ornstein-Uhlenbeck processes, Stochastic Processes and Their Applications 115, 1701-1722.
- [6] Rocha-Arteaga, A. & Sato, K. (2003). Topics in Infinitely Divisible Distributions and Lévy Processes, Aportaciones Matemáticas Investigación, Mexican Mathematical Society, 17.
- [7] Sato, K. (1999). Lévy Processes and Infinitely Divisible Distributions, Cambridge University Press, Cambridge.
- Yor, M. (2001). Exponential Functionals of Brownian [8] Motion and Related Processes, Springer, New York.

## **Related Articles**

Infinite Divisibility; Lévy Processes; Stochastic Integrals.

Víctor Pérez-Abreu
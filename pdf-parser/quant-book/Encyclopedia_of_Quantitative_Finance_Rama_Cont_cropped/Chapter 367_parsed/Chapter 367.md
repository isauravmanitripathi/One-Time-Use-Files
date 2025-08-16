# **Autoregressive Moving** Average (ARMA) Processes

Autoregressive moving average (ARMA) processes  $\{Y_t, t = 0, \pm 1, \ldots\}$  have played a key role as stationary models for time series observed at regularly spaced times. They constitute a very convenient parametric family, capable of exhibiting a broad range of dependence structures and marginal distributions. Well-established prediction, model-selection, and estimation techniques are also available and the asymptotic properties of the customary estimators are well understood. Continuous-time ARMA (denoted CARMA) processes play an analogous role in continuous time. Although continuous-time data is very rarely available, it is often the case that observations of a time series at discrete times can be fruitfully regarded as sampled values of an underlying continuous-time process. The continuous-time framework is very convenient for the modeling of highfrequency data and for dealing with irregularly spaced discrete-time data. Many of the problems of mathematical finance are formulated most conveniently in a continuous time setting, and in constructing more complex continuous-time models for financial data, CARMA processes also play a role. Although ARMA and CARMA processes with infinite second moments can be defined (see  $[3]$  and  $[7]$ ) we restrict our attention here to second-order processes, for which these moments are finite.

#### **ARMA Processes**

The process  $\{Y_n, n = 0, \pm 1, \ldots\}$  is said to be an  $ARMA(p, q)$  process with (real-valued) parameters  $\{\phi_1,\ldots,\phi_p;\theta_1,\ldots,\theta_q;\sigma\}$  if it is a stationary solution of the equations

$$Y_n - \phi_1 Y_{n-1} - \dots - \phi_p Y_{n-p}$$
  
=  $\sigma (Z_n + \theta_1 Z_{n-1} + \dots + \theta_q Z_{n-q})$  (1)

where  $\sigma > 0$ ,  $\phi_p \neq 0$ ,  $\theta_q \neq 0$ ,  $\{Z_n\}$  is standard white noise, i.e., a sequence of uncorrelated random variables with mean 0 and variance 1 (written  $\{Z_n\}$  ~  $\text{WN}(0, 1)$ ) and the polynomials  $\phi(z) := (1 - \phi_1 z -$ 

 $\cdots - \phi_{p}z^{p}$  and  $\theta(z) := (1 + \theta_{1}z + \cdots + \theta_{q}z^{q})$  have no common zeros. Stationarity here means  $EY_t$  is independent of t and  $E(Y_{t+h}Y_t)$  is independent of t for all  $h$ . It can be shown (see [5]) that there is a unique stationary solution of equation (1) for  $\{Y_n\}$  in terms of the white noise sequence  $\{Z_n\}$  if and only if  $\phi(z)$  is nonzero for all complex z such that  $|z| = 1$ . The solution is

$$Y_n = \sum_{j = -\infty}^{\infty} \sigma \psi_j Z_{n-j} \tag{2}$$

where  $\psi(z) := \sum_{j=-\infty}^{\infty} \psi_j z^j$  is the Laurent expansion of  $\theta(z)/\phi(z)$ , valid in an annulus of the form  $|z-1| < \delta$ . If, in addition, the reciprocals  $\xi_1, \ldots, \xi_n$ of the zeros of the polynomial  $\phi(z)$  satisfy

$$|\xi_r| < 1, \quad r = 1, \dots, p$$
 (3)

then  $\psi_j = 0$  for  $j < 0$  and  $\{Y_n\}$  is said to be a *causal function of*  $\{Z_n\}$ . Since, from a second-order point of view, i.e., taking into account the first- and second-order moments of  $\{Y_n\}$  only, every noncausal  $ARMA(p, q)$  process can be written as a causal function of a different standard white noise process, attention is usually restricted to processes defined by equation  $(1)$  with condition  $(3)$  satisfied. We can then write

$$Y_n = \sum_{j = -\infty}^n g_{n-j} Z_j \tag{4}$$

 $\psi(z) := \sum_{j=0}^{\infty} \psi_j z^j = \theta(z) / \phi(z), \quad |z| \le 1,$ where and

$$g_j = \sigma \psi_j, \ \ j = 0, 1, 2, \dots$$
 (5)

The sequence  $\{g_i\}$  is called the *kernel* or *absolutely* summable linear filter relating the ARMA process  $\{Y_n\}$  to  $\{Z_n\}$ . In all that follows, we shall assume causality so that the representation (4) holds with  $g_i$ given by equation  $(5)$ .

If we suppose, in addition, that the sequence  $\{Z_t\}$ is an independent and identically distributed (iid) sequence, then  $\{Y_n\}$  is said to be a *strict* ARMA process. In this case,  $\{Y_n\}$  is a strictly stationary process, i.e., for each positive integer  $n$  and for each  $(t_1, \ldots, t_n)$ , the joint distribution of  $(Y_{t_1+h}, \ldots, Y_{t_n+h})$ is independent of  $h$ .

The ARMA process defined by equation  $(1)$  has an equivalent and illuminating state-space represen*tation*, specified by the equations,

$$Y_n = \sigma \boldsymbol{\theta}' \mathbf{X}_n \tag{6}$$

and

$$\mathbf{X}_{n+1} - \Phi \mathbf{X}_n = \mathbf{e} Z_{n+1} \tag{7}$$

where

$$\Phi = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ \phi_{r} & \phi_{r-1} & \phi_{r-2} & \cdots & \phi_{1} \end{bmatrix},\n$$

$$\n\mathbf{e} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}, \quad \boldsymbol{\theta} = \begin{bmatrix} \theta_{r-1} \\ \theta_{r-2} \\ \vdots \\ \theta_{1} \\ \theta_{0} \end{bmatrix}$$

 $r := \max(p, q + 1), \ \theta_0 := 1, \ \theta_j := 0 \ \text{for} \ j > q \ \text{and}$  $\phi_j := 0$  for  $j > p$ . The causality condition (3) implies that the eigenvalues of the matrix  $\Phi$  are all less than 1 in absolute value so that the state-vector  $\mathbf{X}_t$  has the representation,

$$\mathbf{X}_n = \sum_{j = -\infty}^n \Phi^{n-j} \mathbf{e} \ Z_j \tag{8}$$

Equations  $(6)$  and  $(8)$  show that the kernel sequence  $\{g_i\}$  in the representation (4) can also be written as

$$g_j = \sigma \boldsymbol{\theta}' \Phi^j \ \mathbf{e}, \ \ j = 0, 1, 2, \dots \tag{9}$$

From equations (4) and (9) we easily find that  $EY_n =$  $0$  and

$$\gamma_Y(h) := \text{Cov}(Y_{t+h}, Y_t) = \sigma^2 \boldsymbol{\theta}' \ \Phi^{|h|} \Xi \ \boldsymbol{\theta} \qquad (10)$$

where  $\Xi = E[\mathbf{X}_t \mathbf{X}_t'] = \sum_{j=0}^{\infty} \Phi^j \mathbf{e} \mathbf{e}' \Phi^{j}$ . The ARMA process, as we have defined it, has mean 0. We can, of course, easily extend the definition by saying that  $\{U_n\}$  is an ARMA process with mean  $\mu$  if  $\{U_n - \mu\}$ is a zero-mean ARMA process.

**Remark 1** In the case when  $p > q$  and the reciprocals,  $\xi_1, \ldots, \xi_p$ , of the zeros of the polynomial  $\phi(z)$ are distinct, it follows from equations (4) and (9) and the spectral representation of the matrix  $\Phi$ , that  $\{Y_n\}$  has a *canonical representation* as a linear combination of (possibly complex-valued)  $ARMA(1,0)$ processes,  $\{Y_{r,n}\}\.$  Thus

$$Y_n = \sum_{r=1}^p \beta_r Y_{r,n} \tag{11}$$

where  $Y_{r,n} = \sum_{j=-\infty}^{n} \xi^{n-j} Z_j$  and  $\beta_r = -\sigma \xi_r \theta(\xi_r^{-1})/$  $\phi'(\xi_r^{-1})$ . Notice that the driving white noise sequence is the same for each of the component processes  $\{Y_{r,n}\}\$ , so they are not independent. Corresponding to the canonical decomposition  $(11)$ , there is an analogous representation of the autocovariance function, namely,

$$\gamma_Y(h) = \sum_{j=1}^p \gamma_j \xi_j^{|h|},\tag{12}$$

where  $\gamma_j = -\sigma^2 \xi_j \theta(\xi_j) \theta(\xi_j^{-1})/[\phi(\xi_j)\phi'(\xi_j^{-1})]$ .

Remark 2 Parallel to the time domain representation (4) of  $\{Y_n\}$ , there is a *spectral* or *frequency domain* representation,

$$Y_n = \int_{-\pi}^{\pi} \sigma \frac{\theta(e^{-i\omega})}{\phi(e^{-i\omega})} e^{i\omega n} \, \mathrm{d}Z(\omega) \tag{13}$$

where  $\{Z(\omega), -\pi \leq \omega \leq \pi\}$  is an orthogonal increment process with mean 0 and  $E|dZ(\omega)|^2 = d\omega/$  $(2\pi)$ , and the autocovariance function has the corresponding spectral representation  $\gamma_Y(h) = \int_{-\pi}^{\pi} f(\omega)$  $e^{ih\omega} d\omega$ , where the spectral density function f is given by

$$f(\omega) = \frac{\sigma^2}{2\pi} \left| \frac{\theta(\mathbf{e}^{-i\omega})}{\phi(\mathbf{e}^{-i\omega})} \right|^2, \ \omega \in [-\pi, \pi] \tag{14}$$

**Remark 3** So far we have considered only secondorder properties of  $\{Y_n\}$ . If we make the stronger assumption that the driving white noise sequence is iid with log characteristic function, log  $E \exp(i\omega Z_n)$  $=\xi(\omega)$ , and if  $t_1,\ldots,t_n$  are integers such that  $t_1 <$  $t_2 < \cdots < t_n$  and  $\omega_1, \ldots, \omega_n \in \mathbb{R}$ , then we can use the representation  $(4)$  to derive the log of the joint characteristic function,

$$\log E \exp(i \sum_{r=1}^{n} \omega_r Y_{t_r})$$
  
= 
$$\sum_{k=0}^{n-1} \sum_{j=t_{n-k-1}+1}^{t_{n-k}} \xi \left( \sum_{r=0}^{k} \omega_{n-r} g_{t_{n-r}-j} \right) \quad (15)$$

where  $t_0 := -\infty$ .

2

#### **CARMA Processes**

A natural analog, in continuous time, of the stochastic difference equation (1) is the stochastic differential equation,

$$a(D)Y(t) = \sigma b(D)DL(t) \tag{16}$$

where  $\sigma$  is a strictly positive scale parameter, D denotes differentiation with respect to t,  $a(z) := z^p +$  $a_1z^{p-1} + \ldots + a_p, \ b(z) := b_0 + b_1z + \ldots + b_{p-1}$  $z^{p-1}$ , and the coefficients  $b_j$  satisfy  $b_q = 1$  and  $b_j =$ 0 for  $q < j < p$ . To avoid trivial and easily eliminated complications, we shall assume that  $a(z)$  and  $b(z)$  have no common factors.

The continuous-time analogs of the driving noise terms  $Z_n$  in equation (1) are the increments of the process  $L$ . We shall assume that  $L$  is a Lévy process on  $(-\infty, \infty)$ , i.e., a process with homogeneous independent increments, continuous in probability, with cadlag sample-paths and  $L(0) = 0$ . We shall also restrict attention to second-order Lévy processes, i.e., those satisfying the condition  $E(L(1)^2) < \infty$ , and suppose, without further loss of generality, that  $\text{Var}L(1) = 1$  and  $EL(t) = \mu t$  for some  $\mu \in \mathbb{R}$ . The increments of  $L$  on disjoint intervals of equal length are then iid random variables with finite variance and some infinitely divisible distribution which could, for example, be Gaussian, gamma, compound Poisson, inverse Gaussian, or one of many other possibilities.

Since the derivatives on the right of equation  $(16)$ do not exist in the usual sense, we write the equation in state-space form (cf. equations  $(6)$  and  $(7)$ ),

$$Y(t) = \sigma \mathbf{b}' \mathbf{X}(t) \tag{17}$$

and

$$d\mathbf{X}(t) - \mathbf{A}\mathbf{X}(t) dt = \mathbf{e} dL(t) \tag{18}$$

where

$$\mathbf{A} = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -a_p & -a_{p-1} & -a_{p-2} & \cdots & -a_1 \end{bmatrix},$$
$$\mathbf{e} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} b_0 \\ b_1 \\ \vdots \\ b_{p-2} \\ b_{p-1} \end{bmatrix}$$

with solution satisfying

$$\mathbf{X}(t) = \mathbf{e}^{A(t-s)} \mathbf{X}(s)$$
$$+ \int_{s}^{t} \mathbf{e}^{A(t-u)} \mathbf{e} \ dL(u), \text{ for all } t > s \quad (19)$$

In the Gaussian case  $L$  is Brownian motion, equation  $(18)$  is interpreted as an Ito equation and the integral in equation  $(19)$  is an Ito integral. In the general case, the integral in equation  $(19)$  is defined as in [12].

If we restrict attention to causal solutions, i.e., if we make the assumption that  $\mathbf{X}(s)$  is independent of  $\{L(t) - L(s), t > s\}$  for every s, then necessary and sufficient conditions for the existence of a strictly stationary process  $\mathbf{X}$  satisfying equation (19) (see [6] are

$$\mathcal{R}e(\lambda_r) < 0, \quad r = 1, \dots, p \tag{20}$$

and, under these conditions, the stationary solution must satisfy

$$\mathbf{X}(t) \text{ is distributed as } \int_0^\infty e^{Au} \mathbf{e} \, dL(u) \text{ for all } t \tag{21}$$

where  $\lambda_1, \ldots, \lambda_p$  are the eigenvalues of A (which are also the zeros of the autoregressive polynomial  $a(z)$ ). Condition (21) specifies the stationary marginal distribution of  $\mathbf{X}(t)$  and condition (20) is the continuous-time analog of the causality condition (3).

If we assume that the conditions  $(20)$  and  $(21)$ hold, and let  $s \to -\infty$  in equation (19) we find that

$$\mathbf{X}(t) = \int_{-\infty}^{t} \mathbf{e}^{A(t-u)} \mathbf{e} \, \mathrm{d}L(u) \tag{22}$$

Conversely, if  $\mathbf{X}(t)$  is defined by equation (22) then  $\mathbf{X}$  is a strictly stationary causal process satisfying equation (19). Consequently,  $\{X(t)\}\$  as defined in equation  $(22)$  is the unique, strictly stationary causal function of  $L$  satisfying equation (19).

We now define the strictly stationary causal CARMA process by equation (17) with  $X$  given by equation  $(22)$ . Thus,

$$Y(t) = \int_{-\infty}^{t} \sigma \mathbf{b}' e^{A(t-u)} \mathbf{e} \, \mathrm{d}L(u) \tag{23}$$

This is the continuous-time analog of equation  $(4)$ with the discrete-time kernel,  $\{g_j = \sigma \boldsymbol{\theta}' \Phi^j \mathbf{e}, j =$  $0, 1, 2, \ldots$ , replaced by the continuous-time kernel,

$$g(t) = \sigma \mathbf{b}' e^{At} \mathbf{e}, \ t > 0 \tag{24}$$

From equation (23), we find that  $EY(t) = \sigma \mu b_0/a_p$ (where  $\mu = EL(1)$ ) and

$$\gamma_Y(h) := \text{Cov}[Y(t+h), Y(t)] = \sigma^2 \mathbf{b}' e^{A|h|} \Sigma \mathbf{b} \quad (25)$$

where  $\Sigma = E[\mathbf{X}(t)\mathbf{X}(t)'] = \int_0^\infty e^{Ay} \mathbf{e} \mathbf{e}' e^{A'y} \, \mathrm{d}y.$ 

**Remark 4** If the zeros,  $\lambda_1, \ldots, \lambda_p$ , of the polynomial  $a(z)$  are distinct, it follows from equation (23) and the spectral representation of the matrix  $A$  that  $\{Y_n\}$  has a *canonical representation* as a linear combination of (possibly complex-valued)  $\text{CARMA}(1,0)$ processes,  $\{Y_r(t)\}\$ . Thus,

$$Y(t) = \sum_{r=1}^{p} \beta_r Y_r(t) \tag{26}$$

where  $Y_r(t) = \int_{-\infty}^t e^{\lambda_r(t-u)} dL(u)$  and  $\beta_r = \sigma b(\lambda_r) /$  $a'(\lambda_r)$ . Notice that the driving process L is the same for each of the component processes  $\{Y_r(t)\}\$ , so they are not independent. Corresponding to the canonical decomposition  $(26)$ , there is an analogous representation of the autocovariance function, namely,

$$\gamma(h) = \sum_{r=1}^{p} \gamma_r e^{\lambda_r |h|} \tag{27}$$

where  $\gamma_r = \sigma^2 b(\lambda_r) b(-\lambda_r) / [a(-\lambda_r) a'(\lambda_r)].$ 

**Remark 5** The mean-corrected process  $\{Y^*(t) =$  $Y(t) - \sigma \mu b_0/a_n$  has a spectral representation

$$Y^*(t) = \int_{-\infty}^{\infty} \sigma \frac{b(i\omega)}{a(i\omega)} e^{i\omega t} \, \mathrm{d}Z(\omega) \tag{28}$$

where  $\{Z(\omega), -\infty < \omega < \infty\}$  is an orthogonal increment process with mean 0 and  $E|dZ(\omega)|^2 = d\omega/$  $(2\pi)$ , and the autocovariance function of Y (and of  $Y^*$ ) has the corresponding spectral representation  $\gamma_Y(h) = \int_{-\infty}^{\infty} f(\omega) e^{ih\omega} d\omega$ , where the spectral density function  $f$  is given by

$$f(\omega) = \frac{\sigma^2}{2\pi} \left| \frac{b(i\omega)}{a(i\omega)} \right|^2, \ \omega \in (-\infty, \infty) \tag{29}$$

Gaussian processes with such rational spectral densities were discussed extensively in [9].

**Remark 6** If  $\log E \exp(i\omega L(1)) = \xi(\omega)$ , and if  $t_1, \ldots, t_n$  satisfy  $t_1 < t_2 < \cdots < t_n$  and  $\omega_1, \ldots, \omega_n \in$  $\mathbf{R}$ , then from the representation (23),

$$\log E \exp(i \sum_{r=1}^{n} \omega_r Y(t_r))$$
  
= 
$$\sum_{k=0}^{n-1} \int_{t_{n-k-1}}^{t_{n-k}} \xi \left( \sum_{r=0}^{k} \omega_{n-r} g(t_{n-r} - u) \right) du \ (30)$$

where  $t_0 := -\infty$ .

#### **Prediction and Inference**

From observations at discrete times,  $t_1 < t_2 < \cdots <$  $t_{k-1}$ , of either an ARMA or CARMA process  $\{Y(t)\}$ with specified parameter values, various techniques are available for computing the minimum meansquared error linear predictor,

$$\hat{Y}(t_k) = \alpha_{k,0} + \alpha_{k,1}Y(t_{k-1}) + \cdots + \alpha_{k,k-1}Y(t_1)$$
(31)

of  $Y(t_k)$ ,  $t_k > t_{k-1}$ , and its mean-squared error,  $v_k =$  $E(Y(t_k) - \hat{Y}(t_k))^2$ . For details see, for example [5] and [11]. If we assume that the series is Gaussian, we can write the joint density of  $(Y(t_1), \ldots, Y(t_n))$ at  $(y(t_1),..., y(t_n))$  as

$$g(y((t_1),...,y(t_n))) = \prod_{k=1}^n \frac{1}{\sqrt{v_k}} f\left(\frac{y(t_k) - m(t_k)}{\sqrt{v_k}}\right)$$
(32)

where  $f$  is the standard normal density function,  $m(t_k) = \alpha_{k,0} + \alpha_{k,1}y(t_{k-1}) + \cdots + \alpha_{k,k-1}y(t_1)$  $k > 1$ ,  $m_1 = EY(t)$  and  $v_1 = \text{Var}(Y(t))$ . For given values of  $p$  and  $q$ , maximum Gaussian likelihood (MGL) estimators of the parameters are obtained by maximizing  $g$  with respect to the process parameters. This is a nonlinear maximization problem, and requires the use of efficient numerical techniques. Many other estimation procedures are available, with varying asymptotic efficiencies, but it is known that under rather mild conditions and even when the process  $\{Y(t)\}\$ is not in fact Gaussian, MGL estimators have good asymptotic properties. Model selection, i.e., choice of *p* and *q*, is usually made by minimization of an information criterion, well-known examples being the AIC, AICC, and BIC. See [5] and [10] for details.

## **Some Extensions and Applications**

One of the features frequently observed in financial and geophysical time series is the very slow rate of decay with increasing lag of the sample autocorrelation function. In order to model this phenomenon, *fractionally integrated* ARMA and CARMA processes were introduced. These have the property that the autocorrelation function decreases asymptotically at a hyperbolic rate, rather than at the exponential rate of decay for both ARMA and CARMA processes. For information on fractionally integrated processes see [2, 6, 8].

Nonlinear generalizations of ARMA and CARMA processes, in particular threshold models (see [14]), have also found a wide variety of applications.

In mathematical finance, the CARMA(1,0) (or stationary Ornstein–Uhlenbeck) process, driven by a nondecreasing Levy process, has been used to rep- ´ resent stochastic volatility in the stochastic volatility model of Barndorff-Nielsen and Shephard [1]. Higher order CARMA models for stochastic volatility have also been used to allow for more complex autocorrelation functions (see [4] and [13]). In the COGARCH models of (see Further Reading), the volatility process is a nonlinear self-exciting CARMA process and for COGARCH models in which the volatility process has finite variance, the volatility has the autocorrelation function of a CARMA process, a property analogous to the corresponding result for the volatility of a GARCH process, which, if the volatility has finite variance, has the autocorrelation function of an ARMA process.

## **Acknowledgments**

The author gratefully acknowledges support of this work by the National Science Foundation under Grant, DMS-0744058.

## **References**

- [1] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-Gaussian ornstein—Uhlenbeck based models and some of their uses in financial economics (with discussion), *Journal of the Royal Statistical Society, Series B* **63**, 167–241.
- [2] Beran, J. (1994). *Statistics for Long-Memory Processes*, Chapman & Hall, New York.
- [3] Brockwell, P.J. (2001). Levy-driven CARMA processes, ´ *Annals of the Institute of Statistical Mathematics* **53**, 113–124.
- [4] Brockwell, P.J. (2004). Representations of continuoustime ARMA processes, *Journal of Applied Probability* **41A**, 375–382.
- [5] Brockwell, P.J. & Davis, R.A. (1991). *Time Series: Theory and Methods*, 2nd Edition, Springer, New York.
- [6] Brockwell, P.J. & Marquardt, T. (2005). Fractionally integrated continuous-time ARMA processes, *Statistica Sinica* **15**, 477–494.
- [7] Cline, D.B.H. & Brockwell, P.J. (1985). Linear prediction of ARMA processes with infinite variance, *Stochastic Processes and their Applications* **19**, 281–296.
- [8] Comte, F. & Renault, E. (1996). Long memory continuous time models, *Journal of Econometrics* **73**, 101–149.
- [9] Doob, J.L. (1944). The elementary Gaussian processes, *Annals of the Mathematics and Statistics* **25**, 229–282.
- [10] Hannan, E.J. (1973). The asymptotic theory of linear time series models, *Journal of Applied Probability* **10**, 130–145.
- [11] Jones, R.H. (1985). Time series analysis with unequally spaced data, in *Time Series in the Time Domain*, *Handbook of Statistics*, E.J. Hannan, P.R. Krishnaiah & M.M. Rao, eds, North Holland, Amsterdam, Vol. 5, pp. 157–178.
- [12] Protter, P.E. (2004). *Stochastic Integration and Differential Equations*, 2nd Edition, Springer, New York.
- [13] Todorov, V. & Tauchen, G. (2006). Simulation methods for Levy-driven CARMA sto ´ chastic volatility models, *Journal of Business and Economic Statistics* **24**, 455–469.
- [14] Tong, H. (1990). *Non-linear Time Series : A Dynamical System Approach*, Clarendon Press, Oxford.

## **Further Reading**

- Brockwell, P.J., Chadraa, E. & Lindner, A. (2006). Continuoustime GARCH processes, *Annals of Applied Probability* **16**, 790–826.
- Kluppelberg, C., Lindner, A. & Maller, R. (2004). A continuous ¨ time GARCH process driven by a Levy process: stationarity ´ and second order behaviour, *Journal of Applied Probability* **41**, 601–622.

PETER J. BROCKWELL
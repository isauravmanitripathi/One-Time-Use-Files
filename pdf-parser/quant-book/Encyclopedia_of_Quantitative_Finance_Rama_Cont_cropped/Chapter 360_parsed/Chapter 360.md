# **Simulation-based** Estimation

Simulation-based estimation methods were first used in microeconometric models involving qualitative or limited dependent endogenous variables and, possibly, lagged endogenous variables (see, in particular, [13, 14]) and in macroeconometric models [11, 12]. In this literature, the role of simulations was to approximate likelihood functions or moments which are not computable exactly, and the origin of the computational problem was often the occurrence of large-size integrals when passing from characteristics of the latent model to those of the observable model.

In financial econometrics, the computational problem comes from the simultaneous presence of dynamics and latent variables. Such a situation may imply, for instance, a likelihood function defined as a multivariate integral the size of which is astronomical. Let us look more precisely at the genesis of the problem.

Many financial econometric models can be written in the form

$$\begin{cases}\n y_t = r_{1t}(\underline{y_{t-1}}, \underline{y_t^*}, \varepsilon_{1t}; \theta) \\
y_t^* = r_{2t}(\underline{y_{t-1}}, \underline{y_{t-1}^*}, \varepsilon_{2t}; \theta)t = 1, \dots, T\n\end{cases} \tag{1}$$

where  $y_t$  is an observable endogenous vector,  $y_t^*$  is an unobservable endogenous vector,  $\theta$  is an unknown vector,  $\varepsilon_{1t}$  and  $\varepsilon_{2t}$  are independent unobservable error white noises (the distributions of which can be assumed to be known without loss of generality),  $y_t$ is a notation for  $(y_t, y_{t-1}, \ldots)$ .

From system (1) it is, in general, easy to derive the conditional probability density function (pdf):

$$f(y_t/\underline{y_{t-1}}, \underline{y_t^*}; \theta)$$
  
and 
$$f(y_t^*/\underline{y_{t-1}}, \underline{y_{t-1}^*}; \theta)$$

and, therefore, the joint pdf:

$$f(\underline{y_T}, \underline{y_T^*}; \theta) = \prod_{t=1}^{T} f(y_t / \underline{y_{t-1}}, \underline{y_t^*}, \theta)$$
$$f(y_t^* / \underline{y_{t-1}}, \underline{y_{t-1}^*}, \theta) \qquad (2)$$

However since  $y_T^*$  is unobserved the likelihood function is

$$l_T(\underline{y_T};\theta) = \int f(\underline{y_T}, \underline{y_T^*}; \theta) d\underline{y_T^*} \tag{3}$$

Even if  $y_T^*$  is scalar, we are facing an integral of size  $T$ , to which the standard numerical methods cannot be applied. For instance, in the simplest case where each  $y_t^*$  can take only two values the previous integral is a sum of  $2^T$  terms. If  $T = 100$ , which is very small in finance, we have  $2^{100}$  terms. So standard numerical procedures are of no use. Note, however, that recursive algorithms are available in some special cases (the Kalman filter in the linear case and the Kitagawa-Hamilton in the case where  $y_{t}^{*}$  takes a finite number of values and appears in the model with a fixed number of lags).

# **Examples of Models of Type Governed by** Equations (1)

1. Stochastic volatility models

$$y_t = \exp(y_t^*) \varepsilon_{1t} \tag{4}$$

$$y_t^* = \theta_1 + \theta_2 y_{t-1}^* + \varepsilon_{2t} \tag{5}$$

$$\varepsilon_{1t} \sim N(0, 1), \varepsilon_{2t} \sim N(0, \theta_3) \tag{6}$$

Factor ARCH model

$$y_t = \theta_1 y_t^* + \varepsilon_{1t}, \quad y_t$$
: multivariate  
 $(\theta_{11} = 1)$  (7)

$$y_t^* = (\theta_2 + \theta_3 y_{t-1}^{*2})^{1/2} \varepsilon_{2t}$$
 (8)

$$\varepsilon_{1t} \sim N(0, \Sigma(\theta_4)) \tag{9}$$

$$\varepsilon_{2t} \sim N(0, 1) \tag{10}$$

where  $y_t$  is a vector and  $y_t^*$  a univariate latent ARCH driving the whole dynamics.

Diffusion process observed at discrete dates 3. If we observe the diffusion,

$$d\tilde{y}_t = a(\tilde{y}_t, \theta) + \sigma(\tilde{y}_t, \theta) dW_t \qquad (11)$$

(where  $W_t$  is a standard Brownian motion) at  $t =$  $1, \ldots, T$ , we can consider the Euler approximation corresponding to time unit  $\frac{1}{n}$  (*n* is an integer chosen by the econometrician to have a good approximation):

$$\tilde{y}_{\tau} = \tilde{y}_{\tau - \frac{1}{n}} + \frac{1}{n} a(\tilde{y}_{\tau - \frac{1}{n}}, \theta) + \frac{1}{\sqrt{n}} \sigma(\tilde{y}_{\tau - \frac{1}{n}}, \theta) \varepsilon_{\tau}$$
(12)

where  $\tau$  takes the values  $\frac{k}{n}$ ,  $k = 1, 2, \ldots$  and the sequence  $\varepsilon_{\tau}$  is a standard Gaussian white noise. The  $\tilde{y}_{\tau}$  are observed only if  $\tau$  is an integer. Renaming  $\tilde{y}_{\tau} = y_{k}^{*}, \varepsilon_{\tau} = \varepsilon_{1k}$ , we have

$$y_{k}^{*} = y_{k-1}^{*} + \frac{1}{n}a(y_{k-1}^{*}, \theta) + \frac{1}{\sqrt{n}}$$
$$\times \sigma(y_{k-1}^{*}, \theta)\varepsilon_{1k}$$
(13)

$$y_k = y_k^*$$
, if *k* multiple of *n*  
= 0, otherwise (by convention) (14)

which is of type (1) ( $k$  replacing  $t$ ).

#### **Simulation Methods**

The econometric methods described below are based on different simulation methods, which can be partitioned into three categories.

The first category is made of *unconditional sim*ulations obtained in the following way. Drawing a sequence  $(\tilde{\varepsilon}_{1t}^s, \tilde{\varepsilon}_{2t}^s, t = 1, \ldots, T)$  in the known distribution of  $(\varepsilon_{1t}, \varepsilon_{2t})$ , choosing initial values for  $y_t$  and  $y_t^*$ , and using equation (1), we can, for any value of  $\theta$ , compute simulated paths  $\{y_t^s(\theta), y_t^{*s}(\theta), t =$  $1, \ldots, T$ . These simulations are unconditional in the sense that they do not depend on the observed values  $y_1, \ldots, y_T.$ 

The second category is made of *sequentially con*ditional simulations. Using formulas (2) and (3) we see that if, for a given value of  $\theta$ , we draw sequentially  $y_t^{*s}$ , = 1, ..., T in  $f(y_t^*/y_{t-1}, y_{t-1}^*; \theta)$ , where  $y_{t-1}$  are the observed values, we get an *unbiased simulator* of the likelihood function  $f(y_T; \theta)$ , namely,  $\n\Pi_{t=1}^{T} f(y_{t}/y_{t-1}, y_{t}^{*s}, \theta),\n$  since

$$l(\underline{y_T};\theta) = E\prod_{t=1}^{T} f(y_t/\underline{y_{t-1}}, \underline{y_t}^{*s}, \theta) \qquad (15)$$

the expectation being taken with respect to the probability with pdf

 $\n\Pi_{t=1}^{T} f(y_{t}^{*s} / y_{t-1}, y_{t-1}^{*s}; \theta)\n$ . Therefore,  $f(y_{T}; \theta)$  is the limit when  $S$  goes to infinity of

$$\frac{1}{S} \sum_{s=1}^{S} f(y_t^{*s} / \underline{y_{t-1}}, \underline{y_{t-1}^{*s}}; \theta) \tag{16}$$

However, in practice, this convergence is often very slow and must be improved by importance sampling methods  $[1, 4]$ .

In the third category, we have the globally conditional simulations. The aim is to simulate in the global conditional distribution with pdf  $f(y_T^*/y_T, \theta)$ , for a given  $\theta$ . Note that the previous sequential drawing does not provide such a global drawing; a sequential procedure giving such a drawing should be based on the sequence of pdfs  $f(y_t^*/y_T, y_{t-1}^*;\theta)$  $(y_T \text{ replacing } y_{t-1}), \text{ but this is not feasible since}$  $\overline{f(y_t^*/y_T, y_{t-1}^*; \theta)}$  is not computable. More generally, the problem seems to have s no solution since

$$f(\underline{y_T^*}/\underline{y_T};\theta) = \frac{f(\underline{y_T},\underline{y_T^*};\theta)}{f(\underline{y_T};\theta)}\tag{17}$$

and the denominator is not computable. The key remark to solve the problem is that this denominator is constant, for given  $(y_T, \theta)$ , and therefore we can use simulation techniques that only require us to know the pdf up to a multiplicative constant. The more important techniques satisfying these conditions are Monte Carlo Matkov chain (MCMC) techniques like the Hastings–Metropolis algorithm.

In a first method, the likelihood function, which is not easily computable, is replaced by another objective function, the optimization of which gives consistent asymptotically normal estimators. Examples of such a method are the indirect inference (II) method [9], briefly described below, and the method of simulated moments [5], which is a particular case of the II method.

The second kind of methods is based on an approximation of the maximum likelihood estimator. For instance, the simulated likelihood ratio method  $[2]$  is based on the identity

$$\frac{l(\underline{y_T}, \theta)}{l(\underline{y_T}; \bar{\theta})} = E_{\bar{\theta}} \left[ \frac{l(\underline{y_T}, \underline{y_T^*}; \theta)}{l(\underline{y_T}, \underline{y_T^*}; \bar{\theta})} / \underline{y_T} \right] \tag{18}$$

for any given  $\bar{\theta}$ . Therefore a globally conditional simulation  $y_T^{*s}$  in  $f(y_T^*/y_T;\theta)$  provides the unbiased simulator  $\frac{l(y_T, y_T^{*s}; \theta)}{l(y_T, y_T^{*s}; \theta)}$  of  $\frac{l(y_T; \theta)}{l(y_T; \theta)}$  and the ratio can be consistently approximated by an empirical mean of such unbiased simulations. Another example is the simulated expectation maximization (EM) method [15]. The EM algorithm is based on the maximization in  $\theta$  at iteration *m* of  $E_{\theta^{(m)}}[\log f(y_T, y_T^*, \theta)/y_T]$ ; this conditional expectation is, in general,  $\overline{\text{not}}$  computable but, again, can be approximated using globally conditional simulations.

The third approach is the Bayesian approach. Given a prior distribution of  $\theta$ , with pdf  $\pi(\theta)$ , the Bayesian approach is based on the posterior pdf  $\pi(\theta/y_T)$ . Since

$$\pi(\theta/\underline{y_T}) = \frac{f(\theta, \underline{y_T})}{f(\underline{y_T})} = \frac{f(\underline{y_T}; \theta)\pi(\theta)}{f(\underline{y_T})} \tag{19}$$

the computation of  $\pi(\theta/y_T)$  seems impossible and, moreover, a simulation in this pdf seems also impossible since it is not even known up to a multiplicative constant

The key idea here is to consider the joint posterior pdf of  $\theta$  and  $y_T^*$  given  $y_T$ , which is

$$f(\theta, \underline{y_T^*}/\underline{y_T}) = \frac{f(\underline{y_T}, \underline{y_T^*}; \theta)\pi(\theta)}{f(y_T)} \tag{20}$$

The numerator of equation  $(20)$  is now computable and therefore, simulations in this joint distribution can be made, giving approximations of not only  $\pi(\theta/y_T)$ but also of the *smoothing* distribution  $f(y_T^*/y_T)$ . See [3].

#### **Indirect Inference**

Let us consider an auxiliary criterion  $Q_T(y_T, \beta)$ , where  $\beta$  is an auxiliary parameter. We assume that, when T goes to infinity,  $Q_T(y_T, \beta)$  converges to a deterministic function  $Q_{\infty}(\theta_0, \beta)$ , and we denote by  $b(\theta)$  the function obtained by  $b(\theta)$  =  $\arg \max_{\beta} Q_{\infty}(\theta, \beta)$ . The function  $b(.)$  is called a *binding function* and is assumed to be injective. The II estimators are obtained in the following way:

First step Compute .

$$\hat{\beta}_T = \arg\max_{\beta} Q_T(\underline{y}_T, \beta) \tag{21}$$

Second step Compute 4

$$\hat{\theta}_{ST}(\Omega) = \arg\min_{\theta} [\hat{\beta}_T - \hat{\beta}_{ST}(\theta)]' \Omega[\hat{\beta}_T - \hat{\beta}_{ST}(\theta)] \tag{22}$$

where

$$\hat{\beta}_{ST} = \arg\max_{\beta} \sum_{s=1}^{S} Q_T[\underline{y_T^s}(\theta), \beta] \qquad (23)$$

 $y_T^s(\theta)$  being an unconditional simulated path corresponding the value  $\theta$  of the parameter of interest and  $\Omega$  a symmetric positive definite matrix.

Two asymptotic equivalent versions of  $\hat{\theta}_{ST}(\Omega)$  are obtained if in equation (21)  $\hat{\beta}_{ST}(\theta)$  is replaced either by

$$\frac{1}{S} \sum_{s=1}^{S} \beta_T^S(\theta) \tag{24}$$

with  $\beta_T^S(\theta) = \arg \max_{\beta} Q_T[y_T^s(\theta), \beta]$  or by

$$\tilde{\beta}_{ST}(\theta) = \arg\max_{\beta} Q_{ST}[y_{ST}^{s}(\theta), \beta] \qquad (25)$$

Note, however, that the latter equivalence requires that

$$\frac{\partial Q_T}{\partial \beta}(\underline{y_T}, \beta) = \sum_{t=1}^T \frac{\partial Q_1(y_t; \beta)}{\partial \beta} \tag{26}$$

Finally we also obtain a class of estimators  $\hat{\theta}_{ST}(\Sigma)$ , which is globally asymptotically equivalent to the class  $\hat{\theta}_{ST}(\Omega)$  [6] by

$$\hat{\hat{\theta}}_{ST}(\Sigma) = \arg\min_{\theta} \left( \sum_{s=1}^{S} \frac{\partial Q_{T}[\underline{y_{T}^{s}}(\theta), \hat{\beta}_{T}]}{\partial \beta'} \right)$$
$$\Sigma \left( \sum_{s=1}^{S} \frac{\partial Q_{T}[\underline{y_{T}^{s}}(\theta), \hat{\beta}_{T}]}{\partial \beta} \right) (27)$$

A clear advantage of these methods is that the basic model has only been used through the path simulations *y<sup>s</sup> <sup>T</sup> (θ )*. Therefore the only requirement made on the model is the possibility of performing these path simulations, which is generally satisfied.

When *S* is fixed and *T* goes to infinity the II estimators are consistent and asymptotically normal. The asymptotic variance–covariance matrix depends on  and this matrix can be optimally chosen. Note, however, that, if *θ* and *β* have the same size,  does not matter asymptotically. Specification tests can be based on the optimal values of equation (21) for the optimal matrix , and the classical asymptotic significance tests (score test, Wald test, or a test based on the optimal values of the criteria providing the estimators) are also available.

The general ideas of the II can also be used in other domains: corrections for second-order bias [10], notions of indirect information and indirect identification [8, 9], and encompassing [7].

An important issue of the II methodology is the choice of *QT* and natural candidates are loglikelihood functions of approximations of the model retained or approximations of the log-likelihood function of this model.

## **References**

- [1] Billio, M. & Monfort, A. (1998). Switching state space models likelihood function, filtering and smoothing, *Journal of Statistical Planning and Inference* **68**(1), 64–103.
- [2] Billio, M., Monfort, A. & Robert, C. (1997). *The Simulated Likelihood Ratio Method*. CREST Discussion paper no. 9821.
- [3] Billio, M., Monfort, A. & Robert, C. (1999). Bayesian methods for switching ARMA models, *Journal of Econometrics* **93**, 229–255.
- [4] Danielsson, J. & Richard, J.F. (1995). Accelerated Gaussian importance sampler with application to dynamic latent variable model, in *Econometric Inference using Simulation Techniques*, H. Van Dijk, A. Monfort & B.W. Brown, eds, John Wiley & Sons.

- [5] Duffie, D. & Singleton, K. (1993). Simulated moments estimation of Markov models of asset prices, *Econometrica* **61**, 929–952.
- [6] Gallant, A.R. & Tauchen, G. (1996). Which moments to match? *Econometric Theory* **12**, 657–668.
- [7] Gourieroux, C. & Monfort, A. (1995). Testing encom- ´ passing, and simulating dynamic econometric models, *Econometric Theory* **11**, 195–228.
- [8] Gourieroux, C. & Monfort, A. (1996). ´ *Simulation Based Econometric Methods*, Oxford University Press.
- [9] Gourieroux, C., Monfort, A. & Renault, E. (1993). ´ Indirect inference, *Journal of Applied Econometrics* **8**, 85–118.
- [10] Gourieroux, C., Renault, E. & Touzi, N. (1999). Cali- ´ bration by simulation for small sample bias correction, in *Simulation Based Inference in Econometrics, Methods and Applications*, R. Mariano, T. Schuermann & M. Weeks, eds, Cambridge University Press.
- [11] Laroque, G. & Salanie, B. (1989). Estimation of mul- ´ timarket fixed-price models: an application of pseudomaximum likelihood methods, *Econometrica* **57**, 831–860.
- [12] Laroque, G. & Salanie, B. (1995). Simulation-based esti- ´ mation of models with lagged latent variables, in *Econometric Inference Using Simulation Techniques*, H. Van Dijk, A. Monfort, B.W. Brown, eds, John Wiley & Sons.
- [13] Lerman, S. & Manski, C. (1981). On the use of simulated frequencies to approximate choice probabilities, in *Structural Analysis of Discrete Data with Econometric Applications*, C. Manski & D. McFadden, eds, MIT Press, Cambridge, MA, pp. 305–319.
- [14] McFadden, D. (1989). A method of simulated moments for estimation of discrete response model without numerical integration, *Econometrica* **57**, 995–1026.
- [15] Shephard, N. (1995). Fitting nonlinear time series with applications to stochastic variance model, in *Econometric Inference Using Simulation Techniques*, H.A. Van Dijk, B.W. Monfort & B.W. Brown, eds, John Wiley & Sons.

## **Related Articles**

**Generalized Method of Moments (GMM)**; **Monte Carlo Simulation**.

ALAIN MONFORT
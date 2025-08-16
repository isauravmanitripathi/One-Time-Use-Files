# Variance Reduction

Classical convergence results for the Monte Carlo method show that the ratio  $\sigma/\sqrt{n}$  governs its accuracy, *n* being the number of drawings and  $\sigma$  the variance of the random variable of which we compute the expectation. Variance reduction techniques consist in modifying the classical Monte Carlo method to reduce the order of magnitude of the simulation error. The basic idea behind variance reduction techniques consists in rewriting the quantity to be computed as the expectation of a random variable that has a smaller variance.

In other words, if the quantity to be computed is the expectation  $E[X]$  of a real square integrable random variable  $X$ , variance reduction methods aim at finding an alternative representation  $\mathbf{E}(X) = \mathbf{E}(Y) +$  $C$ , using another square integrable random variable Y such that  $\text{Var}(Y) < \text{Var}(X)$ , C being a computable constant.

The most widely used variance reduction methods are "importance sampling" and "control variate" methods. As such, distinct sections are devoted to them. We also describe other classical variance reduction methods: antithetic variables, stratified sampling. and conditioning. For each method, we give simple examples related to option pricing.

## **Control Variates**

Let  $X$  be a real-valued random variable and assume that we want to compute its expectation using a Monte Carlo method. In this method we use  $Y$ , another square integrable random variable, called the *control variate*, to write  $E(X)$  as

$$\mathbf{E}(X) = \mathbf{E}(X - Y) + \mathbf{E}(Y) \tag{1}$$

When  $\mathbf{E}(Y)$  can be computed using an explicit formula and  $\text{Var}(X - Y)$  is smaller than  $\text{Var}(X)$ , we can use a Monte Carlo method to estimate  $\mathbf{E}(X - Y)$ , and add the known value of  $E(Y)$ . Note that a variance reduction can be obtained only if  $X$  and  $Y$  are *not* independent. In fact, the more dependent are  $X$  and  $Y$  or the nearer is  $Y$  to  $X$ , the better the control variate performs.

Let us illustrate this principle by simple financial examples.

# Using Call-put Arbitrage Formula for Variance Reduction

In a financial context, the price of the underlying assets is usually a good source for control variate as under a risk neutral probability the expected value of the actualized price remains constant with time.

This idea is used when taking into account the call-put arbitrage relation. Let  $S_t$  be the price at time  $t$  of an asset, and denote by  $C$  the price of the European call option

$$C = \mathbf{E} \left( e^{-rT} \left( S_T - K \right)_+ \right) \tag{2}$$

and by  $P$  the price of the European put option

$$P = \mathbf{E} \left( e^{-rT} \left( K - S_T \right)_+ \right) \tag{3}$$

There exists a relation between the price of the put and the call, which does not depend on the models for the price of the asset, namely, the "call-put arbitrage formula":

$$C - P = \mathbf{E} \left( e^{-rT} \left( S_T - K \right) \right) = S_0 - K e^{-rT} \tag{4}$$

This arbitrage formula, which remains true whatever the model, can be used to replace the computation of a call option price by a put option price.

**Remark 1** For the Black–Scholes model explicit formulas for the variance of the put and the call options can be obtained. Often, the variance of the put option is smaller than the variance of the call option. Note that this is not always true but since the payoff of the put is bounded, whereas the payoff of the call is not, this is certainly true when volatility is large enough.

**Remark 2** Observe that call–put relations can also be obtained for Asian options or index options.

For Asian options, set  $\bar{S}_T = 1/T \int_0^{\infty} S_s \, ds$ . We have

$$\mathbf{E}\left(\left(\bar{S}_{T}-K\right)_{+}\right)-\mathbf{E}\left(\left(K-\bar{S}_{T}\right)_{+}\right)$$
$$=\mathbf{E}\left(\bar{S}_{T}\right)-K\tag{5}$$

and, in the Black-Scholes model,

$$\mathbf{E}(\bar{S}_T) = \frac{1}{T} \int_0^T \mathbf{E}(S_s) \, \mathrm{d}s$$
$$= \frac{1}{T} \int_0^T S_0 \, \mathrm{e}^{rs} \, \mathrm{d}s = S_0 \frac{\mathrm{e}^{rT} - 1}{rT} \qquad (6)$$

## The Kemna and Vorst Method for Asian Options

A variance reduction method based on the control variate is proposed in [11] for computing the value of a fixed-strike Asian option. The price of an average (or Asian) put option with fixed strike is

$$\mathbf{E}\left(\mathrm{e}^{-rT}\left(K-\frac{1}{T}\int_{0}^{T}S_{s}\,\mathrm{d}s\right)_{+}\right)\tag{7}$$

where  $(S_t, t \ge 0)$  is the Black–Scholes model

$$S_t = x \exp\left(\left(r - \frac{\sigma^2}{2}\right)t + \sigma W_t\right) \tag{8}$$

If  $\sigma$  and r are small enough, an expansion of the exponential function suggest that  $1/T \int_0^T S_s \, ds$  can be approximated by  $\exp\left(1/T\int_0^T \log(S_s) \, ds\right)$ . This heuristic argument suggests to use  $Y$ , where

$$Y = e^{-rT} \left( K - \exp(Z) \right)_+ \tag{9}$$

and  $Z = 1/T \int_0^T \log(S_s) ds$ , as a control variate. As the random variable  $Z$  is Gaussian, we can explicitly compute  $\mathbf{E}(Y)$  using the (Black-Scholestype) formula

$$\mathbf{E}\left(\left(K - \mathbf{e}^{Z}\right)_{+}\right) = KN(-d)$$
$$-\mathbf{e}^{\mathbf{E}(Z) + \frac{1}{2}\text{Var}(Z)}N\left(-d - \sqrt{\text{Var}(Z)}\right) \quad (10)$$

where  $d = (\mathbf{E}(Z) - \log(K))/\sqrt{\text{Var}(Z)}$ .

To have a working algorithm, it remains to sample

$$e^{-rT}\left(K-\frac{1}{T}\int_0^T S_s \,ds\right)_+ - Y \qquad (11)$$

This method can be very efficient when  $\sigma \approx 0.3$  by year,  $r \approx 0.1$  by year and  $T \approx 1$  year. Of course, for larger values of  $\sigma$  and r, the gain obtained with this control variate is less significant but this method still remains useful.

## **Index Options**

A very similar idea can be used for pricing index options. Assume that  $S_t$  is given by the multidimensional Black–Scholes model. Let  $\sigma$  be a  $p \times d$  matrix and  $W^1, \ldots, W^d$  be d independent Brownian motions. Denote by  $(S_t, t > 0)$  the solution of

$$\begin{cases}\ndS_t^1 = S_t^1 (r dt + [\sigma dW_t]_1), S_0^1 = x_1 \\
\dots \\
dS_t^p = S_t^p (r dt + [\sigma dW_t]_p) S_0^p = x_p\n\end{cases} \n$$
(12)

where  $[\sigma \, dW_t]_i = \sum_{j=1}^d \sigma_{ij} \, dW_t^j$ . Note that this equation can be solved to get, for  $i = 1, \ldots, p$ ,

$$S_T^i = x_i \, \mathrm{e}^{\left(r - 1/2 \sum_{j=1}^d \sigma_{ij}^2\right)T + \sum_{j=1}^d \sigma_{ij} W_T^j} \qquad (13)$$

Moreover, denote by  $I_t$  the value of an index  $I_t =$  $\sum_{i=1}^{p} a_i S_t^i$ , where  $a_1, \ldots, a_p$  is a given set of positive numbers such that  $\sum_{i=1}^{p} a_i = 1$ . Suppose that we want to compute the price of a European index put option with payoff at time T given by  $(K - I_T)_+$ .

Consider  $I_T/m$  where  $m = a_1x_1 + \cdots + a_dx_d$ . Because  $I_0/m = 1$ , an expansion of the exponential function suggests approximation of  $I_T/m$  by  $Y_T/m$ , where  $Y_T$  is the lognormal random variable

$$Y_T = m e^{\sum_{i=1}^p a_i x_i / m \left( \left\{ r - \frac{1}{2} \sum_{j=1}^d \sigma_{ij}^2 \right\} T + \sum_{j=1}^d \sigma_{ij} W_T^j \right)}$$
(14)

As we can explicitly compute  $\mathbf{E}\left[(K-Y_T)_+\right]$  using a Black-Scholes formula, this suggests to use the control variate  $Z = (K - Y_T)_+$  and to sample  $(K - I_T)_+ - (K - Y_T)_+$ . We refer to Figure 1 to see the improvement in variance obtained when using this control variate in a multidimensional Black-Scholes model.

#### A Random Volatility Model

Consider the pricing of an option in a Black–Scholes model with stochastic volatility. The price  $(S_t, t \ge 0)$ is the solution of the stochastic differential equation

$$dS_t = S_t (r dt + \sigma(Y_t) dW_t), \quad S(0) = x \quad (15)$$

where  $\sigma$  is a bounded function and  $Y_t$  is the solution of another stochastic differential equation

$$dY_t = b(Y_t) dt + c(Y_t) dW'_t, \quad Y_0 = y \quad (16)$$

where  $(W_t, t \ge 0)$  and  $(W'_t, t \ge 0)$  are two, not necessarily independent, Brownian motions. We want to

![](_page_2_Figure_1.jpeg)

**Figure 1** At the money index call option : with and without control variate,  $d = 10$ ,  $\sigma = 0.3/\sqrt{\text{year}}$  for each asset, every covariance equal to 0.5,  $T = 1$ 

compute the price of a European option with payoff  $f(S_T)$  at time T given by

$$\mathbf{E}\left(\mathbf{e}^{-rT}f(S_T)\right) \tag{17}$$

If the volatility of the volatility (i.e.,  $c(Y_t)$ ) is not too large or if  $Y_t$  has an invariant law (as for the Orstein–Uhlenbeck process) with mean  $\sigma_0$ , we can expect  $\sigma_0$  to be an acceptable approximation of  $\sigma_t$ .

This suggests the use of the control variate  $e^{-rT} f(\bar{S}_T)$ , where  $\bar{S}_T$  is the solution of a Black-Scholes equation:

$$d\bar{S}_t = \bar{S}_t \left( r \, dt + \sigma_0 \, dW_t \right), \quad S(0) = x \quad (18)$$

For standard payoff  $f$ ,  $\mathbf{E}\left(\mathrm{e}^{-rT}f(\bar{S}_T)\right)$  can be obtained using a Black-Scholes-type formula; hence, it remains to sample

$$e^{-rT}f(S_T) - e^{-rT}f(\bar{S}_T) \tag{19}$$

and to check on simulations, using the standard estimate for the variance, that this procedure actually reduces the variance.

#### Using the Hedge as a Control Variate

In most standard financial models, a hedging strategy is available. This hedge can be used as a hint to construct a control variate.

Let  $(S_t, t \ge 0)$  be the price of the asset. Assume that the price of the option at time  $t$  can be expressed as  $C(t, S_t)$  (this fact is satisfied for any Markovian model). When an explicit approximation  $\bar{C}(t,x)$  of  $C(t, x)$  is known, we can use the control variate

$$Y = \sum_{k=1}^{N} \frac{\partial \bar{C}}{\partial x} (t_k, S_{t_k})$$
$$\times \left( (S_{t_{k+1}} - S_{t_k}) - \mathbf{E} \left( S_{t_{k+1}} - S_{t_k} \right) \right) \quad (20)$$

Note that  $\mathbf{E}(Y) = 0$  by construction and so no correction is needed. If  $\bar{C}$  is close to C and if N is large enough, a large reduction in the variance can be obtained.

#### Optimizing a Set of Control Variates

Assume that  $Y = (Y^1, \ldots, Y^n)$  is a given set of control variates with 0 expectation (or more generally having a known expectation) and finite variance. It is quite easy to optimize the control variate among all linear combinations of the coordinate of  $Y$ .

Let us denote by  $\lambda$  an  $\mathbf{R}^n$  vector. As for every  $\lambda$ 

$$\mathbf{E}(X) = \mathbf{E}(X - \langle \lambda, Y \rangle) \tag{21}$$

we can use  $\langle \lambda, Y \rangle$  as a control variate and it is natural to choose  $\lambda$  to be the minimizer of the variance Var  $(X - \langle \lambda, Y \rangle)$ . A simple computation shows that this minimizer is given by

$$\lambda^* = \Gamma_Y^{-1} \text{Cov}(X, Y) \tag{22}$$

when  $\Gamma_Y$ , the covariance matrix of the vector Y, is invertible and where  $\text{Cov}(X, Y) = (\text{Cov}(X, Y_i)),$  $1 \le i \le n$ ). Note that the optimizing  $\lambda^*$  can be estimated using independent samples of the law of  $(X, Y), ((X_1, Y_1), \ldots, (X_n, Y_n))$  and the standard estimators of the variances and the covariances of the random variables. This leads to a convergent estimator  $\hat{\lambda}_n := \hat{\lambda}_n(X_1, Y_1, \ldots, X_n, Y_n)$  of  $\lambda^*$ .

Using  $\hat{\lambda}_n$  with an independent sample  $((X'_1, Y'_1),$  $\ldots$ ,  $(X'_n, Y'_n)$  leads to a convergent and *unbiased* estimator

$$E_n^1 = \frac{1}{n} \sum_{i=1}^n X'_i - \langle \hat{\lambda}_n, Y'_n \rangle \tag{23}$$

whereas using the same drawings leads to a convergent but *biased* estimator

$$E_n^2 = \frac{1}{n} \sum_{i=1}^n X_i - \langle \hat{\lambda}_n, Y_n \rangle \tag{24}$$

The bias of the second estimator is negligible, at least for large samples as it can be shown that the two estimators follow the same central limit theorem:

$$\sqrt{n}\left(E_n^i - \mathbf{E}(X)\right) \to \mathcal{N}\big(0, (\sigma^*)^2\big) \tag{25}$$

for  $i = 1$  or 2 and where  $(\sigma^*)^2$  is the best available variance

$$(\sigma^*)^2 = \min_{\lambda \in \mathbf{R}^d} \text{Var}(X - \langle \lambda, Y \rangle) \tag{26}$$

See [5, 12] for details and proofs on this technique known as *adaptive control variates*.

#### Perfect Control Variates for Diffusion Models

An interesting result is that perfect (zero-variance) control variates exist for diffusion models. Although the argumentation is mainly theoretical, it can give hints for implementation.

We want to compute  $\mathbf{E}(Z)$  where  $Z = \psi(X_s, 0 \le$  $s \leq T$ ) and  $(X_s, s \geq 0)$  is the solution of

$$dX_t = b(X_t) dt + \sigma(X_t) dW_t, \quad X(0) = x \quad (27)$$

We assume that  $(X_t, t \ge 0)$  is  $\mathbf{R}^n$  valued and  $(W_t, t \ge 0)$ 0) is an  $\mathbf{R}^d$ -valued Brownian motion.

The *predictable representation theorem* shows that we are often able (at least theoretically) to cancel the variance using a stochastic integral as a control variate.

**Theorem 1** (Predictable Representation Theorem). Let Z be a random variable such that  $\mathbf{E}(Z^2)$  <  $+\infty$ . Assume that Z is measurable with respect to  $\sigma(W_s, s < T)$ . Then there exists a stochastic process  $(H_t, t \leq T)$  adapted to the Brownian filtration, such that  $\mathbf{E}\left(\int_0^T H_s^2 \, \mathrm{d}s\right) < +\infty$  and

$$Z = \mathbf{E}(Z) + \int_0^T H_s \, \mathrm{d}W_s \tag{28}$$

For a proof we refer to  $[10, 15]$ .

**Remark 3** Note that  $Z$  needs to be measurable with respect to the  $\sigma$ -field generated by the Brownian motion.

The theorem shows that, in principle, we are able to cancel the variance of  $Z$  using a stochastic integral as a control variate. Nevertheless, the explicit computation of  $(H_s, s \leq T)$  is much more complicated than the one of  $\mathbf{E}(Z)$ ! The reader is referred to [14] for formulas for  $H_s$  involving Malliavin derivatives and conditional expectations. In financial applications, empirical methods are often used instead.

When the price of the underlying asset is described by a Markovian model  $X_t$ , the process  $(H_t, t \leq T)$ can be written as  $H_t = v(t, X_t)$ , v being a function of  $t$  and  $x$  often related to the hedge in the context of financial models.

**Theorem 2** Let b and  $\sigma$  be two Lipschitz continuous functions. Let  $(X_t, t \ge 0)$  be the unique solution of

$$dX_t = b(X_t) dt + \sigma(X_t) dW_t, \quad X_0 = x \quad (29)$$

Denote by  $A$  the infinitesimal generator of this diffusion

$$Af(x) = \frac{1}{2} \sum_{i,j=1}^{n} a_{ij}(x) \frac{\partial^2 f}{\partial x_i \partial x_j}(x)$$
$$+ \sum_{j=1}^{n} b_j(x) \frac{\partial f}{\partial x_j}(x) \tag{30}$$

where  $a_{ij}(x) = \sum_{k=1}^{p} \sigma_{ik}(x) \sigma_{jk}(x)$ .

Assume that there exists a  $C^{1,2}([0,T] \times \mathbf{R}^d)$  function, with bounded derivatives in  $x$ , as solution to the problem

$$\begin{cases}\n\begin{aligned}\n\text{For } (t, x) &\in [0, T] \times \mathbf{R}^n, \\
\left(\frac{\partial u}{\partial t} + Au\right)(t, x) &= 0, \\
u(T, x) &= g(x), \quad x \in \mathbf{R}^n\n\end{aligned}\n\end{cases} \tag{31}$$

Then if  $Z = g(X_T)$  and  $Y = \int_{0}^{T} \frac{\partial u}{\partial x}(s, X_{s}) \sigma(s, X_{s}) \, \mathrm{d}W_{s}$  $(32)$ 

we have

$$\mathbf{E}(Z) = Z - Y \tag{33}$$

The random variable  $Y$  is, thus, a perfect control variate for  $Z$ .

**Proof** Using Itôs formula, we obtain

$$\begin{split} \mathrm{d}u(t,\,X_t) &= \left(\frac{\partial u}{\partial t} + Au\right)(t,\,X_t)\,\mathrm{d}t \\ &+ \frac{\partial u}{\partial x}(t,\,X_t)\sigma(s,\,X_s)\,\mathrm{d}W_t \end{split} \tag{34}$$

Now, integrate between 0 and  $T$  and take the expectation of both sides of the equality. Using the facts that  $u$  is a solution of equation (31) and that the stochastic integral is a martingale, we get

$$u(0, x) = Z - Y = \mathbf{E}(Z) \tag{35}$$

**Remark 4** Theorem 2 shows that we only need to look for  $H_t$  as a function of t and  $X_t$  when X is a diffusion process. However, the explicit formula involves partial derivatives with respect to  $x$  and it is numerically difficult to take advantage of it.

In a practical situation, we can use the following heuristic procedure. Assume that we know an approximation  $\bar{u}$  for u. The previous theorem suggests to use

$$Y = \int_0^T \frac{\partial \bar{u}}{\partial x}(t, X_t) \sigma(s, X_s) \, \mathrm{d}W_t \tag{36}$$

as a control variate. Note that for every function  $\bar{u}$  (even a bad approximation of u), we obtain an unbiased estimator for  $\mathbf{E}(Z)$  by setting  $Z' = Z - Y$ . For a reasonable choice of  $\bar{u}$ , we can expect an improvement of the variance of the estimator. Indeed, set

$$\bar{Z} := g(X_T) - \int_0^T \frac{\partial \bar{u}}{\partial x}(t, X_t) \sigma(X_t) \, \mathrm{d}W_t \quad (37)$$

 $\bar{Z}$  is an unbiased estimator of  $\mathbf{E}(g(X_T))$  and

$$\mathbf{E}\left(|\bar{Z} - \mathbf{E}g(X_T)|^2\right)$$
  
= 
$$\mathbf{E}\left(\int_0^T \left|\left(\frac{\partial u}{\partial x} - \frac{\partial \bar{u}}{\partial x}\right)(t, X_t)\right|^2 \sigma(t, X_t)^2 \,\mathrm{d}t\right)$$
(38)

This variance can be expected to be small if  $\partial \bar{u}/\partial x$ is a good approximation of  $\partial u/\partial x$ .

# **Importance Sampling**

Importance sampling methods proceed by *changing the law* of the samples. Assume that  $X$  takes its values in  $\mathbf{R}^d$ ,  $\phi$  is a bounded function from  $\mathbf{R}^d$  to  $\mathbf{R}$ , and we want to compute  $\mathbf{E}(\phi(X))$ . The aim is to find a new random variable  $Y$  following a different law and a function *i* such that  $\mathbf{E}(\phi(X)) = \mathbf{E}(i(Y)\phi(Y)).$ The function  $i$ , the *importance function*, is needed to maintain the equality of the expectations for every function  $f$ . Obviously, this method is interesting in a Monte Carlo method only if  $\text{Var}(i(Y)\phi(Y))$  is smaller than  $\text{Var}(\phi(X))$ .

Consider  $X$  as an  $\mathbf{R}^d$ -valued random variable following a law with density  $f(x)$  for which we want to compute  $\mathbf{E}(\phi(X))$ 

$$\mathbf{E}(\phi(X)) = \int_{\mathbf{R}^d} \phi(x) f(x) \, \mathrm{d}x \tag{39}$$

If  $\tilde{f}$  is any density on  $\mathbf{R}^d$  such that  $\tilde{f}(x) > 0$  and  $\int_{\mathbf{R}^d} \tilde{f}(x) dx = 1$ , clearly one can rewrite  $\mathbf{E}(\phi(X))$  as

$$\mathbf{E}(\phi(X)) = \int_{\mathbf{R}^d} \frac{\phi(x)f(x)}{\tilde{f}(x)} \tilde{f}(x) dx$$
$$= \mathbf{E}\left(\frac{\phi(Y)f(Y)}{\tilde{f}(Y)}\right) \tag{40}$$

where Y is a random variable with density law  $\tilde{f}(x)$ under **P**. Hence,  $\mathbf{E}(\phi(X))$  can be approximated by an alternative estimator

$$\frac{1}{n}\left(\frac{\phi(Y_1)f(Y_1)}{\tilde{f}(Y_1)}+\cdots+\frac{\phi(Y_n)f(Y_n)}{\tilde{f}(Y_n)}\right) \quad (41)$$

where  $(Y_1, \ldots, Y_n)$  are independent copies of Y. Denoting  $Z = \phi(Y) f(Y) / \tilde{f}(Y)$ , this estimator will have a smaller asymptotic variance than the standard one if  $\text{Var}(Z) < \text{Var}(\phi(X))$ . Note that the variance of  $Z$  is given by

$$\operatorname{Var}(Z) = \int_{\mathbf{R}} \frac{g^2(x)f^2(x)}{\tilde{f}(x)} \, \mathrm{d}x - \mathbf{E}(\phi(X))^2 \tag{42}$$

An easy computation shows that when  $\phi(x) > 0$ , for every  $x \in \mathbf{R}^d$ , the choice of  $\tilde{f}(x) = \phi(x) f(x) /$  $\mathbf{E}(\phi(X))$  leads to a zero-variance estimator as  $Var(Z) = 0$ . Of course, this result can seldom be used in practice as it relies on the exact knowledge of  $\mathbf{E}(\phi(X))$ , which is exactly what we need to compute. Nevertheless, it can lead to a useful heuristic approach : choose for  $\tilde{f}(x)$  a good approximation of  $|\phi(x)f(x)|$  such that  $\tilde{f}(x)/\int_{\mathbf{R}} \tilde{f}(x) dx$  can be sampled easily.

## An Elementary Gaussian Example

In finance, importance sampling is especially useful when computing multidimensional Gaussian expectations as all computations and simulations are completely explicit.

Let  $G$  be a Gaussian random variable with mean zero and unit variance. We want to compute  $\mathbf{E}(\phi(G))$ , for a function  $\phi$ . We choose for the new sampling law, its shifted valued  $\tilde{G} = G + m$ , m being a real constant to be determined later; hence,

$$\mathbf{E}\left(\phi(G)\right) = \mathbf{E}\left(\phi(\tilde{G})\frac{f(\tilde{G})}{\tilde{f}(\tilde{G})}\right) \tag{43}$$

where f is the density of the law of G and  $\tilde{f}$  the density of the law of  $\tilde{G}$ . Easy computation leads to

$$\mathbf{E}\left(\phi(G)\right) = \mathbf{E}\left(\phi(\tilde{G})\,\mathrm{e}^{-m\tilde{G} + (m^2/2)}\right)$$
$$= \mathbf{E}\left(\phi(G+m)\,\mathrm{e}^{-mG - (m^2/2)}\right) \quad (44)$$

As a simple example of the use of equation (44), assume that we want to compute a European call option in the Black–Scholes model;  $\phi$  is then given by

$$\phi(G) = \left(\lambda e^{\sigma G} - K\right)_{\perp} \tag{45}$$

where  $\lambda$ ,  $\sigma$ , and K are positive constants. When  $\lambda \ll K$ ,  $\mathbf{P}(\lambda e^{\sigma G} > K)$  is very small and the option will, very unlikely, be exercised. This fact leads to a very large relative error when using a standard Monte Carlo method. To increase to exercise probability, we can use equality  $(44)$  to obtain

$$\mathbf{E}\left(\left(\lambda e^{\sigma G} - K\right)_+\right)$$
  
= 
$$\mathbf{E}\left(\left(\lambda e^{\sigma(G+m)} - K\right)_+ e^{-mG - (m^2/2)}\right) \tag{46}$$

and choose  $m = m_0$  with  $\lambda e^{\sigma m_0} = K$ , since

$$\mathbf{P}\left(\lambda \,\mathrm{e}^{\sigma(G+m_0)} > K\right) = \frac{1}{2} \tag{47}$$

This choice of  $m$  is certainly not optimal; however, it drastically improves the efficiency of the Monte Carlo method when  $\lambda \ll K$ . See Figure 2 for an illustration of the improvement, which can be obtained using this idea.

![](_page_5_Figure_15.jpeg)

**Figure 2** Call options: use of importance sampling for deep out-of-the-money call option  $\sigma = 0.3/\sqrt{\text{year}}$ ,  $S_0 = 70$ ,  $K = 100$ 

#### A Multidimensional Gaussian Case: Index Options

The previous method can easily be extended to multidimensional Gaussian cases. Let us start by motivating this in the context of index option pricing. Denote by  $(S_t, t > 0)$  a multidimensional Black-Scholes model solution of equation (13)

$$S_T^i = S_0^i \exp\left(\left(r - \frac{1}{2} \sum_{j=1}^d \sigma_{ij}^2\right) T + \sum_{j=1}^d \sigma_{ij} W_T^j\right) \tag{48}$$

Moreover, denote  $I_t$  by the value of an index  $I_t =$  $\sum_{i=1}^{n} a_i S_t^i$ , where  $a_1, \ldots, a_n$  is a given set of positive numbers such that  $\sum_{i=1}^{n} a_i = 1$ . Suppose that we want to compute the price of a European call or put option with payoff at time T given by  $f(I_T)$ . Obviously, there exists a function  $\phi$  such that

$$f(I_T) = \phi(G_1, \dots, G_d) \tag{49}$$

where  $G_i = W_T^j / \sqrt{T}$ . The price of this option can be rewritten as  $\mathbf{E}(\phi(G))$ , where  $G = (G_1, \ldots, G_d)$  is a  $d$ -dimensional Gaussian vector with unit covariance matrix.

As in the one-dimensional case, it is easy (by a change of variable) to prove that if  $m =$  $(m_1,\ldots,m_d)$ , then

$$\mathbf{E}(\phi(G)) = \mathbf{E}\left(\phi(G+m) \,\mathrm{e}^{-mG - (|m|^2/2)}\right) \tag{50}$$

where  $m.G = \sum_{i=1}^{d} m_i G_i$  and  $|m|^2 = \sum_{i=1}^{d} m_i^2$ . In view of equation (50), the second moment  $V(m)$  of the random variable  $X_m = \phi(G+m) e^{-m \cdot G - |m|^2/2}$  is

$$V(m) = \mathbf{E} \left( \phi^2 (G+m) e^{-2mG - |m|^2} \right)$$
  
=  $\mathbf{E} \left( \phi^2 (G) e^{-mG + |m|^2/2} \right)$  (51)

The choice of a minimizing  $m$  (or an approximation) is more difficult than in one dimension. From the previous formula, it follows that  $V(m)$  is a strictly convex function, a property from which we can derive useful approximation methods for a minimizer of  $V(m)$ . The reader is referred to [6] for an almost optimal way to choose the parameter  $m$  or to [1, 2] for a use of stochastic algorithms to get convergent approximation of the  $m$  minimizing the variance  $V(m)$ .

# The Girsanov Theorem and Path-dependent Options

We can extend further these techniques to pathdependent options, using the Girsanov theorem. Let  $(S_t, t > 0)$  be the solution of

$$dS_t = S_t (r dt + \sigma dW_t), S_0 = x \qquad (52)$$

where  $(W_t, t > 0)$  is a Brownian motion under a probability  $P$ . We want to compute the price of a path-dependent option with payoff given by

$$\phi(S_t, t \le T) = \psi(W_t, t \le T) \tag{53}$$

Common examples of such a situation are

- Asian options whose payoff is given by  $f(S_T, \int_0^T S_s \, ds)$  and
- Maximum options whose payoff is given by  $f(S_T, \max_{s < T} S_s)$ .

We start by considering the Brownian case that is a straightforward extension of the technique used in the preceding paragraph. For every real number  $\lambda$ , define the process  $(W_t^{\lambda}, t \leq T)$  as

$$W_t^{\lambda} := W_t + \lambda t \tag{54}$$

According to the Girsanov theorem,  $(W_t^{\lambda}, t < T)$  is a Brownian motion under the probability law  $\mathbf{P}^{\lambda}$ defined by

$$\mathbf{P}^{\lambda}(A) = \mathbf{E}(L_T^{\lambda} \mathbf{1}_A), \quad A \in \mathcal{F}_T \tag{55}$$

where  $L_T^{\lambda} = e^{-\lambda W_T - \lambda^2 T/2}$ . Denote by  $\mathbf{E}^{\lambda}$  the expectation under this new probability  $\mathbf{P}^{\lambda}$ . For every bounded function  $\psi$  we have

$$\mathbf{E}\left(\psi(W_t, t \le T)\right) = \mathbf{E}^{\lambda}\left(\psi(W_t^{\lambda}, t \le T)\right)$$
$$= \mathbf{E}\left(L_T^{\lambda}\psi(W_t^{\lambda}, t \le T)\right) \quad (56)$$

and thus

$$\mathbf{E} \left( \psi(W_t, t \le T) \right)$$
  
= 
$$\mathbf{E} \left( e^{-\lambda W_T - (\lambda^2 T/2)} \psi(W_t + \lambda t, t \le T) \right) \quad (57)$$

For example, if we want to compute the price of a fixed-strike Asian option  $P$  given by

$$\mathbf{E}\left(\mathrm{e}^{-rt}\left(\frac{1}{T}\int_{0}^{T}x\mathrm{e}^{\left(r-(\sigma^{2}/2)\right)s+\sigma W_{s}}\,\mathrm{d}s-K\right)\right) \quad (58)$$

we can use the previous equality to obtain

$$P = \mathbf{E} \left( e^{-rt - \lambda W_T - \lambda^2 T/2} \left( \frac{1}{T} \int_0^T x e^{(r - \sigma^2/2)s + \sigma(W_s + \lambda s)} ds - K \right)_+ \right)$$
(59)

This representation can be used for deep out-of-the money options (that is to say,  $x \ll K$ ). Then  $\lambda$  can be chosen such that

$$\frac{x}{T} \int_0^T e^{(r-\sigma^2/2)s + \sigma\lambda s} ds = K \tag{60}$$

in order to increase the exercise probability.

### Importance Sampling for the Poisson Process

Similar results can also be obtained for Poisson processes and can be useful to construct variance reduction methods for financial models with jumps.

Let  $(N_s^{\lambda}, s \ge 0)$  be a Poisson process with intensity  $\lambda$ . Denote by

$$L_T^{\mu \to \lambda} = e^{T(\mu - \lambda)} \left(\frac{\lambda}{\mu}\right)^{N_T^{\mu}} \tag{61}$$

We have for every bounded functional  $f$ 

$$\mathbf{E}\left(f(N_s^{\lambda}, s \le T)\right) = \mathbf{E}\left(L_T^{\mu \to \lambda} f(N_s^{\mu}, s \le T)\right) \tag{62}$$

See  $[4]$  for a proof and extensions. Note that the variance is given by  $V(\lambda) = \mathbf{E}(X_{\mu}^{2}) - \mathbf{E}(X_{\mu})^{2}$  where  $X_{\mu} = L_T^{\mu \to \lambda} f(N_s^{\mu}, s \leq T)$  and

$$\mathbf{E}(X_{\mu}^{2}) = \mathbf{E}\left(\mathbf{e}^{T(\mu-\lambda)}\left(\frac{\lambda}{\mu}\right)^{N_{T}^{\lambda}}\right)$$
$$\times f^{2}(N_{t}^{\lambda}, 0 \leq t \leq T)\right) \tag{63}$$

From this formula, a convexity property in  $\mu$  can be derived and optimization algorithms deduced from the Euler equation associated with the variance minimization problem.

This methodology can be useful for jump models in finance (e.g., the Merton model) by mixing a change of law on the underlying Brownian motion and on Poisson process.

Importance Sampling for Diffusion Processes

Following [14], we now present a result which proves that variance can be canceled using importance sampling for a diffusion process. The reader is also refered to [13] for the necessary background on simulation of diffusion processes.

**Proposition 1** Let  $Z$  be a random variable such that  $Z = \psi(W_s, 0 \le s \le T)$ ,  $\mathbf{E}(Z^2) < +\infty$  and  $\mathbf{P}(Z \ge \epsilon) = 1$ , for an  $\epsilon > 0$ .

Then, there exists an adapted process  $(h_t, 0 <$  $t < T$ ), such that, if

$$L_T = \exp\left(-\int_0^T h_s \, \mathrm{d}W_s - \frac{1}{2} \int_0^T |h_s|^2 \, \mathrm{d}s\right) \tag{64}$$

 $\mathbf{E}(L_T) = 1$ , then we can define a probability  $\tilde{\mathbf{P}}$  by

$$\mathbf{P}(A) = \mathbf{E} \left( L_T \mathbf{1}_A \right) \tag{65}$$

Under this probability  $\tilde{\mathbf{P}}$ 

$$\tilde{\mathbf{E}}\left(L_T^{-1}Z\right) = \mathbf{E}(Z) \text{ and } \tilde{\text{Var}}\left(L_T^{-1}Z\right) = 0 \quad (66)$$

**Remark 5** Under  $\tilde{\mathbf{P}}$ , the random variable  $L_T^{-1}Z$  has zero variance, and thus is almost surely constant. So if we are able to sample  $L_T^{-1}Z$  under  $\tilde{\mathbf{P}}$ , we obtain a zero-variance estimator for  $\mathbf{E}(Z)$ .

Of course, an effective computation of  $h_t$  is almost always impossible. However, heuristic approximation methods can also be derived. We refer to  $[14]$  for an overview of some of these methods.

**Proof** The representation theorem for Brownian martingales proves the existence of a process  $(H_t, t \leq$ T) such that, for  $t \leq T$ 

$$\mathbf{E}\left(Z|\mathcal{F}_{t}\right) = \mathbf{E}\left(Z\right) + \int_{0}^{t} H_{s} \, \mathrm{d}W_{s} \tag{67}$$

Let  $\phi_t = \mathbf{E} (Z|\mathcal{F}_t) / \mathbf{E} (Z)$ . Equality (67) becomes

$$\phi_t = 1 + \int_0^t \frac{H_s}{\mathbf{E}(Z)} \, \mathrm{d}W_s = 1 - \int_0^t \phi_s h_s \, \mathrm{d}W_s \quad (68)$$

This is a linear equation for  $\phi$ , which can be solved to obtain

$$\phi_T = \exp\left(-\int_0^T h_s \, \mathrm{d}W_s - \frac{1}{2} \int_0^T |h_s|^2 \, \mathrm{d}s\right)$$
  
=  $L_T$  (69)

However, as Z is an  $\mathcal{F}_T$ -measurable random variable,  $L_T = \phi_T = Z/\mathbf{E}(Z)$ . Thus,  $\mathbf{E}(L_T) = 1$  and  $L_T^{-1}Z =$  $\mathbf{E}(Z)$  almost surely under **P** and  $\tilde{\mathbf{P}}$ .

The previous theorem can be used in a simulation context for diffusion processes. Let  $(X_t, t > 0)$  be the unique solution of

$$dX_t = b(X_t) dt + \sigma(X_t) dW_t,$$
  
 
$$X(0) = x$$
 (70)

where b and  $\sigma$  are Lipschitz functions and  $(W_t, t \geq$ 0) is a Brownian motion. If  $(h_t, t \ge 0)$  is a process such that  $\mathbf{E}(L_T) = 1$ , then X is also a solution of

$$\begin{cases}\ndX_t = (b(X_t) - \sigma(X_t)h_t) dt + \sigma(X_t) d\tilde{W}_t \\
X(0) = x\n\end{cases} \tag{71}$$

where  $(\tilde{W}_t = W_t + \int_0^t h_s \, ds, 0 \le t \le T)$  is a Brownian motion under the probability  $\tilde{\mathbf{P}}$ . Hence, we can, in principle, sample the process  $X$  under the new probability  $\tilde{\mathbf{P}}$ . This is easy when  $h_t$  can be written as  $v(t, X_t)$ , v being a function of t and x. Indeed, in this case,  $X$  satisfies the stochastic differential equation

$$dX_t = \tilde{b}(t, X_t) dt + \sigma(X_t) d\tilde{W}_t, \quad X(0) = x \quad (72)$$

with  $\tilde{b}(t,x) = b(x) - \sigma(x)v(t,x)$ . Since  $\tilde{W}$  is a Brownian motion under  $\tilde{\mathbf{P}}$ , we can simulate X under  $\hat{\mathbf{P}}$  using a standard discretization scheme for this stochastic differential equation.

Now we give a more explicit formula for  $h_t$  when the random variable is given by

$$Z = e^{-\int_0^T r(X_s) \, ds} f(X_T) \tag{73}$$

when  $f$  and  $r$  are bounded positive functions and  $(X_t, t \ge 0)$  is the  $\mathbf{R}^d$ -diffusion process solution of equation (70). Note that such a  $Z$  has a form suitable for the computation of option or zero-coupon prices.

Assume that there exists a  $C^{1,2}([0,T]\times \mathbf{R}^d)$  solution to

$$\begin{cases}\n u(T,x) = f(x) & \text{for } x \in \mathbf{R}^n \\
 \left(\frac{\partial u}{\partial t} + Au - ru\right)(t,x) = 0 \\
 & \text{for } (t,x) \in [0,T] \times \mathbf{R}^n\n\end{cases} \tag{74}$$

where  $A$  is the infinitesimal generator of the diffusion  $(X_t, t \ge 0)$  given by equation (30). Then

$$e^{-\int_0^t r(X_s) ds} u(t, X_t) = u(0, x)$$
  
+ 
$$\int_0^t e^{-\int_0^s r(X_u) du} \frac{\partial u}{\partial x}(s, X_s) \sigma(X_s) dW_s \quad (75)$$

Assuming that the stochastic integral is a martingale, we have

$$\mathbf{E}\left(\mathrm{e}^{-\int_{0}^{T}r(X_{s})\,\mathrm{d}s}f(X_{T})|\mathcal{F}_{t}\right)$$
$$=\mathbf{E}\left(\mathrm{e}^{-\int_{0}^{T}r(X_{s})\,\mathrm{d}s}u(T,X_{T})|\mathcal{F}_{t}\right)$$
$$=\mathrm{e}^{-\int_{0}^{t}r(X_{s})\,\mathrm{d}s}u(t,X_{t})\tag{76}$$

Thus, we have  $Z = \mathbf{E}(Z) + \int_0^T H_t \, dW_t$  with

$$H_t = e^{-\int_0^t r(X_s) ds} \frac{\partial u}{\partial x}(t, X_t) \sigma(X_t)$$

and

$$\mathbf{E}\left(\mathbf{e}^{-\int_{0}^{T}r(X_{s})\,\mathrm{d}s}f(X_{T})|\mathcal{F}_{t}\right)$$
$$=\mathbf{e}^{-\int_{0}^{t}r(X_{s})\,\mathrm{d}s}u(t,X_{t})\tag{77}$$

Therefore, using the proof of Proposition 1, we can see that the process  $h_t$  defined by

$$h_{t} = -\frac{e^{-\int_{0}^{t} r(X_{s}) ds} \frac{\partial u}{\partial x}(t, X_{t}) \sigma(X_{t})}{e^{-\int_{0}^{t} r(X_{s}) ds} u(t, X_{t})}$$
$$= -\frac{\frac{\partial u}{\partial x}(t, X_{t}) \sigma(X_{t})}{u(t, X_{t})} \tag{78}$$

allows to cancel the variance of the Monte Carlo method.

**Remark 6** Note that, as  $h_t$  is a function of  $t$  and  $X_t$ , simulation is always possible in principle.

In practical terms, when we know (even rough) approximations  $\bar{u}(t,x)$  of  $u(t,x)$ , it is natural to try to reduce the variance by substituting  $\bar{u}$  for  $u$  in the previous formula. The reader is referred to [17] to see how large deviation theory can give a good approximation  $\bar{u}$  and lead to effective variance reductions.

# **Antithetic Variables**

Antithetic variables are widely used in Monte Carlo simulations because of generality and ease of implementation. Note, though, that it seldom leads to significant effects on the variance and, if not used with care, it can even lead to an increase of the variance.

First, let us consider a simple example,  $I =$  $\mathbf{E}(g(U))$  where U is uniformly distributed on the interval [0, 1]. As  $1-U$  has the same law as U

$$I = \mathbf{E}\left(\frac{1}{2}(g(U) + g(1-U))\right) \tag{79}$$

Therefore, one can draw  $2n$  independent random variables  $U_1, \ldots, U_{2n}$  following a uniform law on  $[0, 1]$ , and approximate *I* either by using

$$I_{2n}^{0} = \frac{1}{2n} \left( g(U_1) + g(U_2) \right.$$
  
$$+ \cdots + g(U_{2n-1}) + g(U_{2n}) \left. \right)$$

or

$$I_{2n} = \frac{1}{2n} \left( g(U_1) + g(1 - U_1) \right.$$
  
$$\left. + \dots + g(U_n) + g(1 - U_n) \right) \tag{80}$$

We can now compare the variances of  $I_{2n}$  and  $I_{2n}^0$ Observe that, in doing this, we assume that most of the numerical work relies on the evaluation of  $g$  and the time devoted to the simulation of the random variables is negligible; this is often a realistic assumption.

The variance of the two estimators are given, respectively, by

$$\operatorname{Var}(I_{2n}^{0}) = \frac{1}{2n} \operatorname{Var}(g(U_{1}))$$
  
$$\operatorname{Var}(I_{2n}) = \frac{1}{2n} \left( \operatorname{Var}(g(U_{1}) + \operatorname{Cov}(g(U_{1}), g(1-U_{1})) \right)$$
(81)

Obviously,  $\text{Var}(I_{2n}) \leq \text{Var}(I_{2n}^0)$  if and only if Cov  $(g(U_1), g(1-U_1)) \le 0$ . When g is either an increasing or a decreasing function, this can be shown to be true and thus the Monte Carlo method using antithetic variables  $(I_{2n})$  is better than the standard one  $(I_{2n}^{0}).$ 

This simple idea can be greatly generalized. If  $X$ is a random variable taking values in  $\mathbf{R}^d$  (or even an infinite dimension space) and if T operates on  $\mathbf{R}^d$  in

such a way that the law of  $X$  is preserved by  $T$ , we can construct a generalized antithetic method based on the equality

$$\mathbf{E}(g(X)) = 1/2\mathbf{E}\left(g(X) + g(T(X))\right) \tag{82}$$

In other words, if  $(X_1, \ldots, X_{2n})$  are sampled along the law of  $X$ , we can consider the estimator

$$I_{2n} = \frac{1}{2n} \left( g(X_1) + g(T(X_1)) \right. \\ \left. + \dots + g(X_n) + g(T(X_n)) \right) \tag{83}$$

and compare it to

$$I_{2n}^{0} = \frac{1}{2n} \left( g(X_1) + g(X_2) \right)$$
  
+ \dots + g(X\_{2n-1}) + g(X\_{2n}) (84)

The same computations as before prove that the estimator  $I_{2n}$  is better than the crude one  $I_{2n}^0$  if and only if  $\text{Cov}(g(X), g(T(X))) \leq 0$ .

## A Generic Example

Let T be the transformation from  $\mathbf{R}^d$  to  $\mathbf{R}^d$  defined by

$$(u^1, \dots, u^d) \to (1 - u^1, \dots, 1 - u^d)$$
 (85)

Obviously, if  $U = (U^1, \ldots, U^d)$  is a vector of independent random variables, then the law of  $T(U)$ is identical to the law of  $U$ . Hence, we can construct an antithetic estimator  $I_{2n}$ . It can be shown that this estimator improves upon the standard one when  $f(u_1, \ldots, u_d)$  is monotonic in each of its coordinates.

## A Toy Financial Example

Let  $G$  be a standard Gaussian random variable. Clearly, the law of  $-G$  and  $G$  are identical and we can consider the transformation  $T(x) = -x$  to construct an antithetic method.

A very simple illustration is given by the call option in the Black-Scholes model where the payoff can be written as

$$\mathbf{E}\left(\left(\lambda\,\mathrm{e}^{\sigma G}-K\right)_{+}\right)\tag{86}$$

 $\lambda$ ,  $\sigma$ , and K being positive real numbers. As this payoff is increasing as a function of  $G$ , the antithetic estimator

$$I_{2n} = \frac{1}{2n} \left( g(G_1) + g(-G_1) \right.$$
  
$$\left. + \dots + g(G_n) + g(-G_n) \right) \tag{87}$$

with  $g(x) = (\lambda e^{\sigma x} - K)_+$ , certainly reduces the variance.

This example can be easily extended to the (more useful) multidimensional Gaussian case, when  $G =$  $(G^1,\ldots,G^d)$  are independent standard Gaussian random variables.

#### Antithetic Variables for Path-dependent Options

The antithetic variables method can also be applied to path-dependent options. For this, consider a pathdependent payoff  $\psi$  ( $S_s$ ,  $s \leq T$ ), where ( $S_t$ ,  $t \geq 0$ ) follows the Black-Scholes model

$$S_t = x \exp\left((r - 1/2\sigma^2)t + \sigma W_t\right) \qquad (88)$$

 $(W_t, t \ge 0)$  is a Brownian motion, r and  $\sigma$  positive real numbers. As the law of  $(-W_t, t \ge 0)$  is identical to the law of  $(W_t, t \ge 0)$ 

$$\mathbf{E}\left(\psi\left(x\mathrm{e}^{(r-1/2\sigma^{2})s+\sigma W_{s}},s\leq T\right)\right)$$
$$=\mathbf{E}\left(\psi\left(x\mathrm{e}^{(r-(1/2)\sigma^{2})s-\sigma W_{s}},s\leq T\right)\right) \tag{89}$$

An antithetic method can be constructed using this equality.

## **Stratified Sampling**

Stratified sampling aims at decomposing the computation of an expectation into specific subsets (called strata). Suppose we want to compute  $I = \mathbf{E}(g(X)),$ where X is an  $\mathbf{R}^d$ -valued random variable and g a bounded measurable function from  $\mathbf{R}^d$  to  $\mathbf{R}$ .

Let  $(D_i, 1 \le i \le m)$  be a partition of  $\mathbf{R}^d$ . I can be expressed as

$$I = \sum_{i=1}^{m} \mathbf{E}(g(X)|X \in D_i)\mathbf{P}(X \in D_i) \qquad (90)$$

where

$$\mathbf{E}(g(X)|X \in D_i) = \frac{\mathbf{E}(\mathbf{1}_{\{X \in D_i\}}g(X))}{\mathbf{P}(X \in D_i)} \qquad (91)$$

Note that  $\mathbf{E}(g(X)|X \in D_i)$  can be interpreted as  $\mathbf{E}(g(X^{i}))$ , where  $X^{i}$  is a random variable whose law is the law of X conditioned to belong to  $D_i$ . When X has a density given by  $f(x)$ , this conditional law also has a density given by

$$\frac{1}{\int_{D_i} f(y) \, \mathrm{d}y} \mathbf{1}_{\{x \in D_i\}} f(x) \, \mathrm{d}x$$

When we further assume that the numbers  $p_i =$  $\mathbf{P}(X \in D_i)$  can be explicitly computed, one can use a Monte Carlo method to approximate each conditional expectation  $I_i = \mathbf{E}(g(X)|X \in D_i)$  by

$$\tilde{I}_{i} = \frac{1}{n_{i}} \left( g(X_{1}^{i}) + \dots + g(X_{n_{i}}^{i}) \right) \tag{92}$$

where  $(X_1^i, \ldots, X_{n_i}^i)$  are independent copies of  $X^i$ . An estimator  $\tilde{I}$  of  $I$  is then given by

$$\tilde{I} = \sum_{i=1}^{m} p_i \tilde{I}_i \tag{93}$$

Of course, the samples used to compute  $\tilde{I}_i$  are supposed to be independent and so the variance of  $\tilde{I}$  is  $\sum_{i=1}^{m} p_i^2(\sigma_i^2/n_i)$ , where  $\sigma_i^2$  be the variance of  $g(X^i)$ .

By fixing the total number of simulations  $\sum_{i=1}^{m}$  $n_i = n$  and minimizing the above variance, we obtain an optimal allocation of points in the strata

$$n_{i} = n \frac{p_{i}\sigma_{i}}{\sum_{i=1}^{m} p_{i}\sigma_{i}} \tag{94}$$

For these values of  $n_i$ , the variance of  $\tilde{I}$ , given in this case by  $1/n \left(\sum_{i=1}^{m} p_i \sigma_i\right)^2$ , is always smaller than the one obtained without stratification.

**Remark 7** The optimal stratification involves the  $\sigma_i$ s which are almost never explicitly known. So one needs to estimate these  $\sigma_i$ s by some preliminary Monte Carlo simulations.

Moreover, let us underline that a bad repartition of  $n_i$  may *increase* the variance of the estimator.

A common way to circumvent these difficulties is to choose a proportional repartition:  $n_i =$  $np_i$ . The corresponding variance  $1/n \sum_{i=1}^m p_i \sigma_i^2$ , is still smaller than the original one, but not optimal. This choice is often made especially when the probabilities  $p_i$  are explicit.

For more considerations on the choice of the  $n_i$ and for hints on suitable choices of the sets  $D_i$ , see [3].

#### A Toy Financial Example

In the standard Black-Scholes, model the price of a call option is given by

$$\mathbf{E}\left(\left(\lambda e^{\sigma G} - K\right)_{+}\right) \tag{95}$$

It is natural to use the following strata for  $G: \{G < d\}$ or  $\{G > d\}$ , where  $d = \log(K/\lambda)/\sigma$ . Of course the variance of the stratum  $G < d$  is equal to 0. So, in the optimal allocation, we have to simulate only one point in this stratum: all other points have to be drawn in the stratum  $G \ge d$ . This can be done by using the (numerical) inverse of the cumulative distribution function of a Gaussian random variable.

### Index Options

A European call or put index option in the multidimensional Black-Scholes model can be expressed as  $\mathbf{E}(h(G))$ , for  $G = (G_1, \ldots, G_n)$  a vector of independent standard Gaussian random variables and for some complicated but explicit function h from  $\mathbf{R}^n$ to R.

Now, choose a vector  $u \in \mathbf{R}^n$  such that  $|u| = 1$  (so  $\langle u, G \rangle = \sum_{i=1}^{n} u_i G_i$  is also a standard Gaussian random variable) and a partition  $(B_i, 1 \le i \le n)$  of  $\mathbf{R}$  such that

$$\mathbf{P}(< u, G > \in B_i) = \mathbf{P}(G_1 \in B_i) = 1/n$$
 (96)

This can be done by setting  $B_i = N^{-1}((i-1)/n)$ ,  $N^{-1}(i/n)$ , where N is the cumulative distribution function of a standard Gaussian random variable and  $N^{-1}$  is its inverse. Then define the  $\mathbf{R}^{n}$ -strata by  $D_i = \{u \in \mathbf{R}^n, \langle u, x \rangle \in B_i\}.$ 

In order to implement a stratification method based on these strata, we need first to sample the Gaussian random variable  $\langle u, G \rangle$  given that  $\langle u, G \rangle$  belongs to  $B_i$ , then to sample the vector G when knowing already the value  $\langle u, G \rangle$ .

The first point is easy since, if  $U$  is uniformly distributed on [0, 1], then the law of  $N^{-1}((i - 1/N) +$  $(U/N)$  is precisely the law of a standard Gaussian random variable conditioned to be in  $B_i$ .

To solve the second point, observe that  $G - \langle$  $u, G > u$  is a Gaussian vector independent of

 $\langle u, G \rangle$ . So if Y is a copy of the vector G,  $G = \langle u, G \rangle u + G - \langle u, G \rangle u$  and  $\langle u, G \rangle$  $u + Y - \langle u, Y \rangle$  have the same distribution. This leads to a very simple simulation method for  $G$  given  $\langle u, G \rangle = \lambda$  and to an effective way to implement the suggested stratification method.

Note that this method can be made efficient by choosing a good vector  $u$ . An almost optimal way to choose the vector  $u$  can be found in [6].

## Conditioning

This method uses the well-known fact that conditioning reduces the variance. Indeed, for any square integrable random variable  $Z$ , we have

$$\mathbf{E}(Z) = \mathbf{E}(\mathbf{E}(Z|\mathcal{B}))\tag{97}$$

where  $\mathcal{B}$  is any  $\sigma$ -algebra defined on the same probability space as  $Z$ . When, in addition,  $Z$  is square integrable, the conditional expectation is an  $L^2$  projection so

$$\mathbf{E}\left(\mathbf{E}(Z|\mathcal{B})^2\right) \le \mathbf{E}(Z^2) \tag{98}$$

and thus  $\text{Var}(\mathbf{E}(Z|\mathcal{B})) < \text{Var}(Z)$ .

When  $Y$  is a random variable defined on the same probability space as X and  $\mathcal{B} = \sigma(Y)$ , it is well known that  $\mathbf{E}(Z|\sigma(Y))$  can be written as

$$\mathbf{E}(Z|Y) := \mathbf{E}(Z|\sigma(Y)) = \phi(Y) \tag{99}$$

for some measurable function  $\phi$  and the practical efficiency of simulating  $\phi(Y)$  instead of Z heavily relies on getting an explicit formula for the function  $\phi$ . This can be achieved when  $Z = f(X, Y)$ , where  $X$  and  $Y$  are independent random variables. In this case, we have

$$\mathbf{E}(f(X,Y)|Y) = \phi(Y) \tag{100}$$

where  $\phi(y) = \mathbf{E}(f(X, y)).$ 

## A Basic Example

Suppose that we want to compute  $\mathbf{P}(X \leq Y)$ , where  $X$  and  $Y$  are independent random variables. This occurs in finance, in a slightly more complex setting, when computing the hedge of an exchange option (or the price of a digital exchange option). We have

$$\mathbf{P}\left(X\leq Y\right) = \mathbf{E}\left(F(Y)\right) \tag{101}$$

where  $F(x) = \mathbf{P}(X \le x)$  is the distribution function of  $X$ . This can be used to obtain a variance reduction which can be significant, especially when the probability  $\mathbf{P}(X < Y)$  is small.

# A Financial Example: A Stochastic Volatility Model

Let  $(W_t, t > 0)$  be a Brownian motion and r be a real number. Assume that  $(S_t, t > 0)$  follows a Black-Scholes model with stochastic volatility, which is solution of

$$dS_t = S_t (r dt + \sigma_t dW_t), \quad S_0 = x \quad (102)$$

where  $(\sigma_t, t \ge 0)$  is a given continuous stochastic process independent of the Brownian motion  $(W_t, t \ge$ 0). We want to compute the option price

$$\mathbf{E}\left(\mathbf{e}^{-rT}f(S_T)\right) \tag{103}$$

where  $f$  is a bounded measurable function. Clearly  $S_T$  can be expressed as

$$S_T = x \exp\left(rT - \frac{1}{2} \int_0^T \sigma_t^2 dt + \int_0^T \sigma_t dW_t^1\right)$$
(104)

As the processes  $(\sigma_t, t \ge 0)$  and  $(W_t, t \ge 0)$  are independent,  $\left(\int_0^T \sigma_t^2 dt, \int_0^T \sigma_t dW_t\right)$  has the same law as

$$\left(\int_0^T \sigma_t^2 \, \mathrm{d}t, \sqrt{\frac{1}{T} \int_0^T \sigma_t^2 \, \mathrm{d}t} \times W_T\right) \quad (105)$$

Conditioning with respect to the process  $(\sigma_t, 0 \le t \le t)$  $T$ ), we obtain

$$\begin{aligned} \mathbf{E} \left( e^{-rT} f(S_T) \right) \\ &= \mathbf{E} \left( \mathbf{E} \left[ e^{-rT} f(S_T) | \sigma_t, 0 \le t \le T \right] \right) \\ &= \mathbf{E} \left( \psi(\sigma_t, 0 \le t \le T) \right) \end{aligned} \tag{106}$$

where, for a fixed volatility path  $(v_t, 0 \le t \le T)$ ,

$$\begin{split} \phi(v_t, 0 &\le t \le T) \\ &= \mathbf{E} \left( e^{-rT} f\left(x e^{rT - \int_0^T v_t^2/2 \, \mathrm{d}t + W_T \sqrt{1/T \int_0^T v_t^2 \, \mathrm{d}t}} \right) \right) \\ &= \phi\left(\sqrt{\frac{1}{T} \int_0^T v_t^2 \, \mathrm{d}t} \right) \end{split} \tag{107}$$

 $\phi(\sigma)$  being the price of the option in the standard Black–Scholes model with volatility  $\sigma$ , that is

$$\phi(\sigma) = \mathbf{E}\left(\mathrm{e}^{-rT}f\left(x\mathrm{e}^{\left(r-(\sigma^2/2)\right)T+\sigma W_T}\right)\right) \qquad (108)$$

Hence, we only need to sample  $\int_0^T \sigma_t^2 dt$  in order to use a Monte Carlo method using the random variable  $\psi(\sigma_t, 0 < t < T).$ 

## Additional References

For complements, we refer the reader to classical books devoted to Monte Carlo methods ([7, 9, 16, 18]). For a more specific discussion of Monte Carlo methods in finance see  $[5, 8]$ .

## References

- Arouna, B. (2003/2004). Robbins-Monro algorithms and  $[1]$ variance reduction in finance, The Journal of Computational Finance 7(2), 35-61.
- [2] Arouna, B. (2004). Adaptative Monte-Carlo method, a variance reduction technique, Monte Carlo Methods Application  $10(1)$ , 1–24.
- [3] Cochran, W.G. (1977). Sampling Techniques, Series in Probabilities and Mathematical Statistics, Wiley.
- Cont, R. & Tankov, P. (2004). Financial Modelling with [4] Jump Processes, CRC Financial Mathematics Series, Chapman & Hall.
- [5] Glasserman, P. (2004). Monte-Carlo methods in financial engineering, Applications of Mathematics (New York), Stochastic Modelling and Applied Probability, Springer-Verlag, New York, Vol. 53.
- Glasserman, P., Heidelberger, P. & Shahabuddin, P. [6] (1999). Asymptotically optimal importance sampling and stratification for pricing path dependent options, Mathematical Finance  $9(2)$ , 117–152.
- Hammersley, J. & Handscomb, D. (1979). Monte-Carlo [7] *Methods*, Chapman & Hall, London.
- [8] Jäkel, P. (2002). Monte-Carlo Methods in Finance, Wiley.
- Kalos, M.H. & Whitlock, P.A. (1986). Monte Carlo [9] Methods, John Wiley & Sons.
- [10] Karatzas, I. & Shreve, S.E. (1991). *Brownian Motion* and Stochastic Calculus, 2nd Edition, Springer-Verlag, New York.
- [11] Kemna, A.G.Z. & Vorst, A.C.F. (1990). A pricing method for options based on average asset values, Journal of Banking Finance 14, 113-129.
- [12] Kim, S. & Anderson, S.G. (2004). Winter Simulation Conference, Proceedings of the 36th conference on Winter simulation, Washington, D.C.
- [13] Kloeden, P.E. & Platen, E. (1999). *Numerical Solution* of Stochastic Differential Equations, Applications of

*Mathematics (New York)*, 3rd Edition, Springer-Verlag, Berlin, Vol. 23.

- [14] Newton, N.J. (1994). Variance reduction for simulated diffusions, *SIAM Journal on Applied Mathematics* **54**(6), 1780–1805.
- [15] Revuz, D. & Yor, M. (1991). *Continuous Martingales and Brownian Motion*, Springer-Verlag, Berlin.
- [16] Ripley, B.D. (1987). *Stochastic Simulation*, Wiley.
- [17] Fournie, E., Lasry, J.M. & Touzi, N. (1997). Monte ´ Carlo methods for stochastic volatility models, in *Numerical methods in finance*, Publ. Newton Inst., Rogers, L.C.G. *et al.*, ed., Cambridge University Press, Cambridge 146–164.
- [18] Rubinstein, R.Y. (1981). *Simulation and the Monte-Carlo Method*, *Series in Probabilities and Mathematical Statistics*, Wiley.

**Related Articles**

**Monte Carlo Greeks**; **Monte Carlo Simulation for Stochastic Differential Equations**; **Option Pricing: General Principles**; **Rare-event Simulation**; **Simulation of Square-root Processes**.

BERNARD LAPEYRE
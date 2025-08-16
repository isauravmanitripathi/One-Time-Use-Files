# **Econometrics of Diffusion** Models

Many models in finance take the form of stochastic differential equations, where the variable of interest  $X_t$  is a vector of asset prices, interest rates, and so on, with dynamics of the form

$$dX_t = \mu(X_t; \theta)dt + \sigma(X_t; \theta)dW_t \tag{1}$$

where  $W_t$  is an *m*-dimensional standard Brownian motion. In a typical parametric situation, the functions  $\mu$  and  $\sigma$  are known, but not the parameter vector  $\theta$ , which is to be estimated. In the base case, the data are discrete observations on the process  $X_t$  sampled at dates  $\Delta$ ,  $2\Delta$ , ...,  $n\Delta$ , on a time interval [0, T] with  $T = n\Delta$  and  $\Delta$  fixed. The case where  $\Delta$  is either deterministic and time varying or random (as long as independent from  $X$ ) introduces no further fundamental difficulties. This article focuses exclusively on the case where  $\Delta$  need not be small, that is, exclude the vast array of methods specifically designed only for high-frequency data.

A number of methods are available to estimate  $\theta$ . First maximum-likelihood estimation is discussed, followed by nonlikelihood alternatives.

### Maximum-likelihood Estimation

Well-established principles from statistics indicate that in this context maximum-likelihood estimation of  $\theta$  is the method of choice. One should write down as a function of  $\theta$  the probability of collecting the observations we have actually obtained, and pick the value of  $\theta$  that maximizes this function, known as the likelihood function. In other words, the resulting estimator of  $\theta$  is the one that makes it most likely that the model would have produced the data we obtained.

Furthermore, the form of the likelihood function is particularly simple due to the Markovian nature of the model (1). The probability of observing the data  $\{X_0, X_{\Delta}, \ldots, X_{n\Delta}\}$ , given that the parameter vector is  $\theta$ , is

$$\mathbb{P}(X_{n\Delta}, X_{(n-1)\Delta}, \dots, X_0; \theta)$$
  
= 
$$\mathbb{P}(X_{n\Delta} | X_{(n-1)\Delta}, \dots, X_0; \theta)$$

$$\times \mathbb{P}(X_{(n-1)\Delta}, \dots, X_0; \theta)\n$$

$$\n= \mathbb{P}(X_{n\Delta}|X_{(n-1)\Delta}; \theta)\n$$

$$\n\times \mathbb{P}(X_{(n-1)\Delta}, \dots, X_0; \theta)\n$$

$$\n= \mathbb{P}(X_{n\Delta}|X_{(n-1)\Delta}; \theta) \times \dots\n$$

$$\n\times \mathbb{P}(X_{\Delta}|X_0; \theta) \mathbb{P}(X_0; \theta) \tag{2}$$

where the first equality is simply Bayes' rule and the second is a consequence of Markov property. Repeating the process for each successive observation yields the third equality. The objective is then to maximize over values of  $\theta$ , this function or equivalently its log

$$\ell_N(\theta) \equiv \sum_{i=1}^n l_X(X_{i\Delta}|X_{(i-1)\Delta}, \Delta; \theta) \qquad (3)$$

where  $l_X(x|x_0, \Delta; \theta) = \ln p_X(x|x_0, \Delta; \theta)$  and  $p_X(x|x_0, \Delta; \theta)$  $(x|x_0, \Delta; \theta)$  is the transition density of the process, or the probability that X will go from  $x_0$  to x in the amount of time  $\Delta$ , when the parameter vector is  $\theta$ .

All this is indeed exceedingly simple, except for one not so minor detail: with few exceptions, we do not know in closed form the expression of the transition density  $p_X$  corresponding to a given model (1)! In finance, the exceptions are the well-known models of Black and Scholes [10] (the geometric Brownian motion  $dX_t = \beta X_t dt +$  $\sigma X_t dW_t$ ), Vasicek [37] (the Ornstein–Uhlenbeck process  $dX_t = \beta(\alpha - X_t)dt + \sigma dW_t$  and Cox *et al.* [18] (Feller's square-root process  $dX_t = \beta(\alpha - \beta)$  $(X_t)dt + \sigma X_t^{1/2}dW_t$ ) which rely on these existing closed-form expressions. The fact that these models have closed-form derivative prices is, of course, not by coincidence, since a derivative price is the expected value of its payoff under the density  $p_X$ corresponding to the risk-neutral version of the model. So knowledge of the density in closed form and closed-form option prices is closely related.

In many cases that are relevant in finance, however, the transition function is unknown: see, for example, the models used in [16]  $(dX_t = \beta(\alpha (X_t)dt + \sigma X_t dW_t$ , [31]  $(dX_t = (\alpha X_t^{-(1-\delta)} + \beta)dt +$  $\sigma X_t^{\delta/2} dW_t$ ), [17]; the more general version of Chan *et al.* [11]  $(dX_t = \beta(\alpha - X_t)dt + \sigma X_t^{\gamma}dW_t)$ , [14]  $(\mathrm{d}X_t = (\alpha_0 + \alpha_1 X_t + \alpha_2 X_t^2)\mathrm{d}t + (\sigma_0 + \sigma_1 X_t) \mathrm{d}W_t);$ the affine class of models in [20] and [19] ( $dX_t =$  $\beta(\alpha - X_t)dt + \sqrt{\sigma_0 + \sigma_1 X_t}dW_t$ ; and the nonlinear mean reversion model in [1]  $(dX_t = (\alpha_0 + \alpha_1 X_t + \alpha_1 X_t)$  $\alpha_2 X_t^2 + \alpha_{-1}/X_t) dt + (\beta_0 + \beta_1 X_t + \beta_2 X_t^{\beta_3}) dW_t).$ 

A method to construct accurate approximations in closed form to the unknown transition density  $p_X(x|x_0, \Delta; \theta)$  for an arbitrary diffusion model (1) is described later.

## **Constructing the Likelihood Function**

The construction of the function  $l_X$  to be used in equation (3) follows [2] (examples and application to interest rate data), [3] (univariate theory), and [4] (multivariate theory). The method proceeds by constructing a closed-form expansion to approximate the transition density  $p_X$ , or equivalently  $l_X$ directly. While the description below may seem involved, in practice these calculations can be implemented in software such as *Mathematica*. Alternative methods would involve solving numerically a partial differential equation, or employing simulations, neither one delivering a closed-form approximation to  $l_{\rm X}$ . The closed-form method has been shown to be substantially more accurate and faster in practical implementations than the alternatives [28, 29].

#### Reducibilty

Whenever possible, it is advisable to start with a change of variable. A diffusion  $X$  is *reducible* if and only if there exists a one-to-one transformation of the diffusion  $X$  into a diffusion  $Y$  whose diffusion matrix  $\sigma_Y$  is the identity matrix. That is, there exists an invertible function  $\gamma(x;\theta)$  such that  $Y_t \equiv \gamma(X_t;\theta)$ satisfies the stochastic differential equation:

$$dY_t = \mu_Y(Y_t; \theta)dt + dW_t \tag{4}$$

Every univariate diffusion is reducible, through the simple transformation  $Y_t = \int^{X_t} du/\sigma(u;\theta)$ . However, not every multivariate diffusion is reducible (a necessary and sufficient condition for reducibility is given in [4]). Whenever a diffusion is reducible, an expansion can be computed for the transition density  $p_X$  of X by first computing it for the density  $p_Y$  of  $Y$  and then transforming  $Y$  back into  $X$ .

The idea is, in fact, to make two successive transformations  $X \mapsto Y \mapsto Z$  such that Z is sufficiently close to a Normal random variable, then construct a sequence for  $p_Z$  around a Normal and revert the transformation  $Z \mapsto Y \mapsto X$ . This will yield an expansion for  $p_X$  around a deformed Normal, unless

the volatility function  $\sigma$  is constant (independent of  $X_t$ ).

When a diffusion is not reducible, the situation is more involved (see the section The Irreducible Case). The expansion for  $l_Y$  is of the form

$$l_{Y}^{(K)}(y|y_{0}, \Delta; \theta) = -\frac{m}{2}\ln(2\pi\Delta) + \frac{C_{Y}^{(-1)}(y|y_{0};\theta)}{\Delta} + \sum_{k=0}^{K} C_{Y}^{(k)}(y|y_{0};\theta) \frac{\Delta^{k}}{k!}$$
(5)

The coefficients of the expansion are given explicitly by

$$C_Y^{(-1)}(y|y_0;\theta) = -\frac{1}{2} \sum_{i=1}^m (y_i - y_{0i})^2 \qquad (6)$$
  
$$C_Y^{(0)}(y|y_0;\theta) = \sum_{i=1}^m (y_i - y_{0i}) \int_0^1 \mu_{Yi} \times (y_0 + u(y - y_0); \theta) du \qquad (7)$$

and, for  $k \ge 1$ ,

$$C_Y^{(k)}(y|y_0;\theta) = k \int_0^1 G_Y^{(k)}(y_0 + u(y-y_0)|y_0;\theta)u^{k-1} du \quad (8)$$

where  $G_Y^{(k)}(y|y_0;\theta)$  is given explicitly as a function of  $\mu_{Yi}$  and  $C_Y^{(j-1)}$ ,  $j = 1, \ldots, k$ .

Given an expansion for the density  $p_Y$  of Y, an expansion for the density  $p_X$  of  $X$  can be obtained by a direct application of the Jacobian formula:

$$l_X^{(K)}(x|x_0,\Delta;\theta) = -\frac{m}{2}\ln(2\pi\Delta) - D_v(x;\theta)$$
$$+\frac{C_Y^{(-1)}(\gamma(x;\theta)|\gamma(x_0;\theta);\theta)}{\Delta}$$
$$+\sum_{k=0}^K C_Y^{(k)}(\gamma(x;\theta)|$$
$$\times \gamma(x_0;\theta);\theta)\frac{\Delta^k}{k!} \tag{9}$$

from  $l_Y^{(K)}$  given in equation (5), using the coefficients  $C_{\nu}^{(k)}, k = -1, 0, \ldots, K$  given above, and where

$$D_{v}(x;\theta) \equiv \frac{1}{2} \ln(\text{Det}[v(x;\theta)]) \tag{10}$$

with  $v(x;\theta) \equiv \sigma(x;\theta)\sigma^{\mathrm{T}}(x;\theta)$ .

# The Irreducible Case

In the irreducible case, no such  $Y$  exists and the expansion of the log likelihood  $l_X$  has the form

$$l_{X}^{(K)}(x|x_{0}, \Delta; \theta) = -\frac{m}{2}\ln(2\pi\Delta) - D_{v}(x;\theta) + \frac{C_{X}^{(-1)}(x|x_{0};\theta)}{\Delta} + \sum_{k=0}^{K} \times C_{X}^{(k)}(x|x_{0};\theta)\frac{\Delta^{k}}{k!}$$
(11)

The approach is to calculate a Taylor series in  $(x - x_0)$  of each coefficient  $C_X^{(k)}$ , at order  $j_k$  in  $(x - x_0)$ . Such an expansion will be denoted by  $C_{\mathbf{x}}^{(j_k,k)}$  at order  $j_k = 2(K-k)$ , for  $k = -1, 0, \ldots, K$ .

The resulting expansion will then be

$$\tilde{l}_{X}^{(K)}(x|x_{0},\Delta;\theta) = -\frac{m}{2}\ln(2\pi\Delta) - D_{v}(x;\theta) + \frac{C_{X}^{(j_{-1},-1)}(x|x_{0};\theta)}{\Delta} + \sum_{k=0}^{K} \times C_{X}^{(j_{k},k)}(x|x_{0};\theta)\frac{\Delta^{k}}{k!}$$
(12)

Such a Taylor expansion was unnecessary in the reducible case: the expressions given above provide the explicit expressions of the coefficients  $C_{V}^{(k)}$  and then in equation  $(9)$  we have the corresponding ones for  $C_{X}^{(k)}$ . However, even for an irreducible diffusion. it is still possible to compute the coefficients  $C_{\mathbf{x}}^{(j_k,k)}$ explicitly.

For each  $k = -1, 0, \ldots, K$ , the coefficient  $C_{\mathbf{v}}^{(k)}$  $(x|x_0;\theta)$  in equation (12) solves an equation of the form

$$f_X^{(k-1)}(x|x_0;\theta) = C_X^{(k)}(x|x_0;\theta) - \sum_{i=1}^m \sum_{j=1}^m \times v_{ij}(x;\theta) \frac{\partial C_X^{(-1)}(x|x_0;\theta)}{\partial x_i} \times \frac{\partial C_X^{(k)}(x|x_0;\theta)}{\partial x_j} - G_X^{(k)}(x|x_0;\theta)$$
$$= 0 \tag{13}$$

Each function  $G_X^{(k)}$ ,  $k = 0, 1, ..., K$ , involves only<br>the coefficients  $C_X^{(h)}$  for  $h = -1, ..., k - 1$ , so this

system of equation can be utilized to solve recursively for each coefficient at a time. Specifically, the equation  $f_X^{(-2)} = 0$  determines  $C_X^{(-1)}$ , given  $C_X^{(-1)}$ ,  $G_X^{(0)}$  becomes known and the equation  $f_X^{(-1)} = 0$ determines  $C_X^{(0)}$ , given  $C_X^{(-1)}$  and  $\hat{C}_X^{(0)}$ ,  $G_X^{(1)}$  becomes known and the equation  $f_X^{(0)} = 0$  then determines  $C_X^{(1)}$ , and so on. It turns out that this results in a system of linear equations in the coefficients of the polynomials  $C_X^{(j_k,k)}$ , so each one of these equations can be solved explicitly in the form of the Taylor expansion  $C_X^{(j_k,k)}$  of the coefficient  $C_X^{(k)}$ , at order  $j_k$ in  $(x - x_0)$ .

# **Applications: Stochastic Volatility and Term Structure Models**

In a stochastic volatility model, the asset price process  $S_t$  follows

$$dS_t = (r - \delta)S_t dt + \sigma_1(X_t; \theta)dW_t^Q \qquad (14)$$

where r is the riskfree rate,  $\delta$  is the dividend yield paid by the asset (both taken to be constant only for simplicity),  $\sigma_1$  denotes the first row of the matrix  $\sigma$ , and O denotes the equivalent martingale measure [25]. The volatility state variables  $V_t$  then follow a stochastic differential equation (SDE) on their own. For example, in the [26] model,  $m = 2$  and  $q = 1$ :

$$\begin{split} \mathrm{d}X_{t} &= \mathrm{d}\left[\begin{array}{c} S_{t} \\ V_{t} \end{array}\right] = \left[\begin{array}{c} (r-\delta)S_{t} \\ \kappa(\gamma-V_{t}) \end{array}\right] \mathrm{d}t \\ &+ \left[\begin{array}{cc} \sqrt{(1-\rho^{2})V_{t}}S_{t} & \rho\sqrt{V_{t}}S_{t} \\ 0 & \sigma\sqrt{V_{t}} \end{array}\right] \\ &\times \mathrm{d}\left[\begin{array}{c} W_{1}^{\mathcal{Q}}(t) \\ W_{2}^{\mathcal{Q}}(t) \end{array}\right] \end{split} \tag{15}$$

The model is completed by the specification of a vector of market prices of risk for the different sources of risk ( $W_1$  and  $W_2$  here), such as

$$\Lambda(X_t;\theta) = \left[\lambda_1 \sqrt{(1-\rho^2)V_t}, \ \lambda_2 \sqrt{V_t}\right]' \qquad (16)$$

which characterizes the change of measure from  $Q$ back to the physical probability measure  $P$ .

Likelihood inference for this and other stochastic volatility models is discussed in [7]. Given a time series of observations of both the asset price,  $S_t$ , and a vector of option prices (which, for simplicity, we take to be call options)  $C_t$ , the time series of  $V_t$  can then be inferred from the observed  $C_t$ . If  $V_t$  is multidimensional, sufficiently many options are required with varying strike prices and maturities to allow extraction of the current value of  $V_t$  from the observed stock and call prices. Otherwise, only a single option is needed. For reasons of statistical efficiency, we seek to determine the joint likelihood function of the observed data, as opposed to, for example, conditional or unconditional moments. We employ the closed-form approximation technique described above, which yields in closed form the joint likelihood function of  $[S_t; V_t]'$ . From there, the joint likelihood function of the observations on  $G_t = [S_t; C_t]' = f(X_t; \theta)$  is obtained simply by multiplying the likelihood of  $X_t = [S_t; V_t]'$  by the Jacobian term  $J_t$ :

$$\ln p_G(g|g_0, \Delta; \theta) = -\ln J_t(g|g_0, \Delta; \theta)$$
$$+ l_X(f^{-1}(g; \theta)|f^{-1}$$
$$\times (g_0; \theta); \Delta, \theta) \tag{17}$$

with  $l_X$  obtained as described above.

Another example of practical interest in finance consists of term structure models. A multivariate term structure model specifies that the instantaneous riskless rate  $r_t$  is a deterministic function of an  $m$ dimensional vector of state variables,  $X_t$ :

$$r_t = r(X_t; \theta) \tag{18}$$

An affine yield model is any model where the short rate  $(18)$  is an affine function of the state vector and the risk-neutral dynamics  $(1)$  are affine:

$$dX_t = (\tilde{A} + \tilde{B}X_t)dt + \Sigma \sqrt{S(X_t; \alpha, \beta)}dW_t^{\mathcal{Q}} \quad (19)$$

where  $\tilde{A}$  is an *m*-element column vector,  $\tilde{B}$  and  $\Sigma$  are  $m \times m$  matrices, and  $S(X_t; \alpha, \beta)$  is the diagonal matrix with elements  $S_{ii} = \alpha_i + X'_i \beta_i$ , with each  $\alpha_i$  a scalar and each  $\beta_i$  an  $m \times 1$  vector,  $1 \le i \le m$  [19].

It can then be shown that, in affine models, bond prices have the exponential affine form  $\exp(-\gamma_0(\tau;\theta) - \gamma(\tau;\theta)'x)$ , where  $\tau = T - t$  is the bond's time to maturity. Aït-Sahalia and Kimmel [6] consider likelihood inference for affine term structure models on the basis of observations on the bond yields. For other implementations of the method in various contexts and with various datasets [8, 13, 21, 32, 36]. Methods to do small sample bias corrections, relevant in particular for the speed of mean reversion parameter when near a unit root, are provided by Phillips and Yu [33] and Tang and Chen [35].

## **Nonlikelihood Methods**

Because of the Cramer-Rao lower bound, maximumlikelihood estimation will, at least asymptotically, be efficient and should therefore be the method of choice for estimating  $\theta$  given that we now have available closed-form, numerically tractable, likelihood expansions. There are, however, a number of alternative methods available to estimate the parameter vector. This discussion will again not include methods appropriate only when the sampling interval  $\Delta$  tends to  $0$ .

The method of moments is generally not available with standard moments such as the mean, variance, and so on. Hansen and Scheinkman [24] provide moment functions in the form of expectations of the infinitesimal generator that are applied to test functions, while Bibby and Sørensen [9] and Kessler and Sørensen [30] consider other constructions of moment functions.

A different type of moment functions is obtained by simulation. The moment function is the expected value, under the model whose parameters one wishes to estimate, of the score function from an auxiliary model. The idea is that the auxiliary model should be easier to estimate; in particular, the parameters of the auxiliary model appearing in the moment function are replaced by their quasi-maximum likelihood estimates. The parameters of the model of interest are then estimated by minimizing a generalized method of moments (GMM)-like criterion. This method has the advantage of being applicable to a wide class of models. On the other hand, the estimates are obtained by simulations that are computationally intensive and they require the selection of an arbitrary auxiliary model, so the parameter estimates for the model of interest will vary based on both the set of simulations and the choice of auxiliary model. Related implementations of this idea are due to Smith [34], Gouriéroux et al. [23], and Gallant and Tauchen [22].

Nonparametric methods are appropriate when the drift and diffusion functions in equation  $(1)$  are specified as  $\mu(x)$  and  $\sigma(x)$  instead of being dependent upon a finite-dimensional vector of parameters  $\theta$ . They are particularly useful for the purpose of testing whether a given parametric model for  $\mu(x;\theta)$  and  $\sigma(x;\theta)$  is appropriate, by comparing the parametric and nonparametric estimates of the corresponding densities.

Let  $\pi_X(\cdot,\theta)$  denote the marginal density implied by the parametric model and  $p_X(\cdot|\cdot,\cdot,\theta)$  the transition density. Under regularity assumptions,  $(\mu(\cdot, \theta))$ ,  $\sigma^2(\cdot,\theta)$ ) will uniquely characterize the marginal and transition densities over discrete time intervals. For example, the Ornstein-Uhlenbeck process  $dX_t =$  $\beta(\alpha - X_t)dt + \gamma dW_t$  generates Gaussian marginal and transitional densities. The square-root process  $dX_t = \beta(\alpha - X_t)dt + \gamma X_t^{1/2}dW_t$  yields a Gamma marginal and noncentral chi-squared transitional densities.

More generally, any parametrization of  $\mu$  and  $\sigma^2$ corresponds to a parametrization of the marginal and transitional densities. While the direct estimation of  $\mu$  and  $\sigma^2$  with discrete data is problematic, the estimation of the densities explicitly takes into account the discreteness of the data. The basic idea in [1] is to use the mapping between the drift and diffusion, on the one hand, and the marginal and transitional densities, on the other, to test the model's specification using densities at the observed discrete frequency  $(\pi_X, p_X)$  instead of the infinitesimal characteristics of the process  $(\mu, \sigma^2)$ .

Aït-Sahalia *et al.* [5] develop an alternative specification test for the transition density of the process, based on a direct comparison of the nonparametric estimate of the transition density to the assumed parametric transition function. What makes this new direct testing approach possible is the subsequent development, described above, of closed-form expansions for  $p_X(x|x_0, \Delta, \theta)$ , which, as already noted, is rarely known in closed form. A complementary approach to this is the one proposed by Hong and Li [27], who use the fact that under the null hypothesis, the random variables  $\{P_X(X_{i\Delta}|X_{(i-1)\Delta}, \Delta, \theta)\}$  are a sequence of independent and identically distributed (i.i.d.) uniform random variables [12, 15]. Using for  $P_X$  the closed-form approximations described above, they detect the departure from the null hypothesis by comparing the kernel-estimated bivariate density of  $\{(Z_i, Z_{i+\Delta})\}$  with that of the uniform distribution on the unit square, where  $Z_i =$  $P(X_{i\Delta}|X_{(i-1)\Delta}, \Delta, \theta).$ 

## Acknowledgments

Financial support from the NSF under grants DMS-0532370 and SES-0850533 is gratefully acknowledged.

## References

- [1] Aït-Sahalia, Y. (1996). Testing continuous-time models of the spot interest rate, Review of Financial Studies 9, 385-426.
- Aït-Sahalia, Y. (1999). Transition densities for interest [2] rate and other nonlinear diffusions, Journal of Finance 54. 1361-1395.
- [3] Aït-Sahalia, Y. (2002). Maximum-likelihood estimation of discretely-sampled diffusions: a closed-form approximation approach, *Econometrica* **70**, 223-262.
- [4] Aït-Sahalia, Y. (2008). Closed-form likelihood expansions for multivariate diffusions, Annals of Statistics 36, 906-937.
- [5] Aït-Sahalia, Y., Fan, J. & Peng, H. (2009). Nonparametric transition-based tests for jump-diffusions, Journal of the American Statistical Association forthcoming.
- Aït-Sahalia, Y. & Kimmel, R. (2002). Estimating Affine [6] Multifactor Term Structure Models Using Closed-Form Likelihood Expansions. Technical Reports, Princeton University.
- Aït-Sahalia, Y. & Kimmel, R. (2007). Maximum likeli-[7] hood estimation of stochastic volatility models, Journal of Financial Economics 83, 413-452.
- Bakshi, G., Ju, N. & Ou-Yang, H. (2006). Estimation [8] of continuous-time models with an application to equity volatility dynamics, Journal of Financial Economics 82,  $227 - 249.$
- [9] Bibby, B.M. & Sørensen, M.S. (1995). Estimation functions for discretely observed diffusion processes, Bernoulli 1. 17-39.
- [10] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, Journal of Political Economy 81, 637–654.
- [11] Chan, K.C., Karolyi, G.A., Longstaff, F.A. & Sanders, A.B. (1992). An empirical comparison of alternative models of the short-term interest rate, Journal of Finance 48, 1209-1227.
- [12] Chen, S.X., Jiti Gao, J. & Tang, C. (2008). A test for model specification of diffusion processes, Annals of Statistics 36, 167-198.
- [13] Cheridito, P., Filipović, D. & Kimmel, R.L. (2007). Market price of risk specifications for affine models: theory and evidence, Journal of Financial Economics 83, 123-170.
- [14] Constantinides, G.M. (1992). A theory of the nominal term structure of interest rates, Review of Financial Studies 5, 531-552.
- [15] Corradi, V. & Swanson, N.R. (2005). A bootstrap specification test for diffusion processes, Journal of Econometrics 124, 117-148.

- [16] Courtadon, G. (1982). The pricing of options on default free bonds, *Journal of Financial and Quantitative Analysis* **17**, 75–100.
- [17] Cox, J.C. (1975). The constant elasticity of variance option pricing model, *The Journal of Portfolio Management* 15–17, Special issue published in 1996.
- [18] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–408.
- [19] Dai, Q. & Singleton, K.J. (2000). Specification analysis of affine term structure models, *Journal of Finance* **55**, 1943–1978.
- [20] Duffie, D. & Kan, R. (1996). A yield-factor model of interest rates, *Mathematical Finance* **6**, 379–406.
- [21] Egorov, A.V., Li, H. & Ng, D. (2008). A tale of two yield curves: modeling the joint term structure of dollar and euro interest rates, *Journal of Econometrics* forthcoming.
- [22] Gallant, A.R. & Tauchen, G.T. (1996). Which moments to match? *Econometric Theory* **12**, 657–681.
- [23] Gourieroux, C., Monfort, A. & Renault, E. (1993). ´ Indirect inference, *Journal of Applied Econometrics* **8**, S85–S118.
- [24] Hansen, L.P. & Scheinkman, J.A. (1995). Back to the future: generating moment implications for continuoustime Markov processes, *Econometrica* **63**, 767–804.
- [25] Harrison, M. & Kreps, D. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **20**, 381–408.
- [26] Heston, S. (1993). A closed-form solution for options with stochastic volatility with applications to bonds and currency options, *Review of Financial Studies* **6**, 327–343.
- [27] Hong, Y. & Li, H. (2005). Nonparametric specification testing for continuous-time models with applications to term structure of interest rates, *Review of Financial Studies* **18**, 37–84.
- [28] Hurn, A., Jeisman, J. & Lindsay, K. (2007). Seeing the wood for the trees: a critical evaluation of methods to estimate the parameters of stochastic differential equations, *Journal of Financial Econometrics* **5**, 390–455.

- [29] Jensen, B. & Poulsen, R. (2002). Transition densities of diffusion processes: numerical comparison of approximation techniques, *Journal of Derivatives* **9**, 1–15.
- [30] Kessler, M. & Sørensen, M. (1999). Estimating equations based on eigenfunctions for a discretely observed diffusion, *Bernoulli* **5**, 299–314.
- [31] Marsh, T. & Rosenfeld, E. (1982). Stochastic processes for interest rates and equilibrium bond prices, *Journal of Finance* **38**, 635–646.
- [32] Mosburger, G. & Schneider, P. (2005). *Modelling International Bond Markets with Affine Term Structure Models*. Technical Reports, Vienna University of Economics and Business Administration.
- [33] Phillips, P.C. & Yu, J. (2009). Maximum likelihood and Gaussian estimation of continuous time models in finance, in *Handbook of Financial Time Series*, T. Andersen, R. Davis, J.-P. Kreib & T. Mikosch, eds, Springer, New York.
- [34] Smith, A.A. (1993). Estimating nonlinear time series models using simulated vector autoregressions, *Journal of Applied Econometrics* **8**, S63–S84.
- [35] Tang, C.Y. & Chen, S.X. (2009). Parameter estimation and bias correction for diffusion processes, *Journal of Econometrics* forthcoming.
- [36] Thompson, S. (2008). Identifying term structure volatility from the LIBOR-swap curve, *Review of Financial Studies* **21**, 819–854.
- [37] Vasicek, O. (1977). An equilibrium characterization of the term structure, *Journal of Financial Economics* **5**, 177–188.

# **Related Articles**

**Markov Processes**; **Stochastic Volatility Models**.

YACINE A¨IT-SAHALIA
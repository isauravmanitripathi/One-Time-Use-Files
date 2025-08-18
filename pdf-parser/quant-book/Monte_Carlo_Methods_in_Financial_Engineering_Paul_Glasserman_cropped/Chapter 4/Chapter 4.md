This chapter develops methods for increasing the efficiency of Monte Carlo simulation by reducing the variance of simulation estimates. These methods draw on two broad strategies for reducing variance: taking advantage of tractable features of a model to adjust or correct simulation outputs, and reducing the variability in simulation inputs. We discuss control variates, antithetic variates, stratified sampling, Latin hypercube sampling, moment matching methods, and importance sampling, and we illustrate these methods through examples. Two themes run through this chapter:

- o The greatest gains in efficiency from variance reduction techniques result from exploiting specific features of a problem, rather than from generic applications of generic methods.
- o Reducing simulation error is often at odds with convenient estimation of the simulation error itself; in order to supplement a reduced-variance estimator with a valid confidence interval, we sometimes need to sacrifice some of the potential variance reduction.

The second point applies, in particular, to methods that introduce dependence across replications in the course of reducing variance.

## 4.1 Control Variates

## 4.1.1 Method and Examples

The method of control variates is among the most effective and broadly applicable techniques for improving the efficiency of Monte Carlo simulation. It exploits information about the errors in estimates of known quantities to reduce the error in an estimate of an unknown quantity.

To describe the method, we let  $Y_1, \ldots, Y_n$  be outputs from n replications of a simulation. For example,  $Y_i$  could be the discounted payoff of a derivative security on the *i*th simulated path. Suppose that the  $Y_i$  are independent and

identically distributed and that our objective is to estimate  $E[Y_i]$ . The usual estimator is the sample mean  $\bar{Y} = (Y_1 + \cdots + Y_n)/n$ . This estimator is unbiased and converges with probability 1 as  $n \to \infty$ .

Suppose, now, that on each replication we calculate another output  $X_i$ along with  $Y_i$ . Suppose that the pairs  $(X_i, Y_i), i = 1, \ldots, n$ , are i.i.d. and that the expectation  $E[X]$  of the  $X_i$  is known. (We use  $(X, Y)$  to denote a generic pair of random variables with the same distribution as each  $(X_i, Y_i)$ .) Then for any fixed  $b$  we can calculate

$$Y_i(b) = Y_i - b(X_i - \mathsf{E}[X])$$

from the  $i$ th replication and then compute the sample mean

$$\bar{Y}(b) = \bar{Y} - b(\bar{X} - \mathsf{E}[X]) = \frac{1}{n} \sum_{i=1}^{n} (Y_i - b(X_i - \mathsf{E}[X])).$$
 (4.1)

This is a control variate estimator; the observed error  $\bar{X} - \mathsf{E}[X]$  serves as a control in estimating  $E[Y]$ .

As an estimator of  $E[Y]$ , the control variate estimator (4.1) is unbiased because

$$\mathsf{E}[\bar{Y}(b)] = \mathsf{E}\left[\bar{Y} - b(\bar{X} - \mathsf{E}[X])\right] = \mathsf{E}[\bar{Y}] = \mathsf{E}[Y]$$

and it is consistent because, with probability  $1$ ,

$$\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} Y_i(b) = \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} (Y_i - b(X_i - \mathsf{E}[X]))$$
  
=  $\mathsf{E}[Y - b(X - \mathsf{E}[X])]$   
=  $\mathsf{E}[Y].$ 

Each  $Y_i(b)$  has variance

$$\begin{aligned} \mathsf{Var}[Y_i(b)] &= \mathsf{Var}\left[Y_i - b(X_i - \mathsf{E}[X])\right] \\ &= \sigma_Y^2 - 2b\sigma_X\sigma_Y\rho_{XY} + b^2\sigma_X^2 \equiv \sigma^2(b), \end{aligned} \tag{4.2}$$

where  $\sigma_X^2 = \text{Var}[X]$ ,  $\sigma_Y^2 = \text{Var}[Y]$ , and  $\rho_{XY}$  is the correlation between X and Y. The control variate estimator  $\bar{Y}(b)$  has variance  $\sigma^2(b)/n$  and the ordinary sample mean  $\bar{Y}$  (which corresponds to  $b=0$ ) has variance  $\sigma_Y^2/n$ . Hence, the control variate estimator has smaller variance than the standard estimator if  $b^2 \sigma_X < 2b \sigma_Y \rho_{XY}$ .

The optimal coefficient  $b^*$  minimizes the variance (4.2) and is given by

$$b^* = \frac{\sigma_Y}{\sigma_X} \rho_{XY} = \frac{\text{Cov}[X, Y]}{\text{Var}[X]}.$$
(4.3)

Substituting this value in  $(4.2)$  and simplifying, we find that the ratio of the variance of the optimally controlled estimator to that of the uncontrolled estimator is

 $4.1$  Control Variates 187

$$\frac{\mathsf{Var}[\bar{Y} - b^*(\bar{X} - \mathsf{E}[X])]}{\mathsf{Var}[\bar{Y}]} = 1 - \rho_{XY}^2. \tag{4.4}$$

A few observations follow from this expression:

- $\circ$  With the optimal coefficient  $b^*$ , the effectiveness of a control variate, as measured by the variance reduction ratio  $(4.4)$ , is determined by the strength of the correlation between the quantity of interest Y and the control X. The sign of the correlation is irrelevant because it is absorbed in  $b^*$ .
- o If the computational effort per replication is roughly the same with and without a control variate, then  $(4.4)$  measures the computational speed-up resulting from the use of a control. More precisely, the number of replications of the  $Y_i$  required to achieve the same variance as n replications of the control variate estimator is  $n/(1-\rho_{XY}^2)$ .
- $\circ$  The variance reduction factor  $1/(1-\rho_{XY}^2)$  increases very sharply as  $|\rho_{XY}|$ approaches 1 and, accordingly, it drops off quickly as  $|\rho_{XY}|$  decreases away from 1. For example, whereas a correlation of  $0.95$  produces a ten-fold speedup, a correlation of 0.90 yields only a five-fold speed-up; at  $|\rho_{XY}| = 0.70$ the speed-up drops to about a factor of two. This suggests that a rather high degree of correlation is needed for a control variate to yield substantial benefits.

These remarks and equation (4.4) apply if the optimal coefficient  $b^*$  is known. In practice, if  $E[Y]$  is unknown it is unlikely that  $\sigma_Y$  or  $\rho_{XY}$  would be known. However, we may still get most of the benefit of a control variate using an estimate of  $b^*$ . For example, replacing the population parameters in  $(4.3)$  with their sample counterparts yields the estimate

$$\hat{b}_n = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^n (X_i - \bar{X})^2}.$$
(4.5)

Dividing numerator and denominator by  $n$  and applying the strong law of large numbers shows that  $\hat{b}_n \to b^*$  with probability 1. This suggests using the estimator  $Y(b_n)$ , the sample mean of  $Y_i(b_n) = Y_i - b_n(X_i - \mathsf{E}[X])$ ,  $i =$  $1,\ldots,n$ . Replacing  $b^*$  with  $b_n$  introduces some bias; we return to this point in Section  $4.1.3$ .

The expression in  $(4.5)$  is the slope of the least-squares regression line through the points  $(X_i, Y_i)$ ,  $i = 1, \ldots, n$ . The link between control variates and regression is useful in the statistical analysis of control variate estimators and also permits a graphical interpretation of the method. Figure 4.1 shows a hypothetical scatter plot of simulation outputs  $(X_i, Y_i)$  and the estimated regression line for these points, which passes through the point  $(\bar{X}, \bar{Y})$ . In the figure,  $\bar{X} < \mathsf{E}[X]$ , indicating that the *n* replications have underestimated  $\mathsf{E}[X]$ . If the  $X_i$  and  $Y_i$  are positively correlated, this suggests that the simulation estimate  $\bar{Y}$  likely underestimates  $\mathsf{E}[Y]$ . This further suggests that we should adjust the estimator upward. The regression line determines the magnitude of the adjustment; in particular,  $\bar{Y}(\hat{b}_n)$  is the value fitted by the regression line at the point  $\mathsf{E}[X]$ .

![](_page_3_Figure_1.jpeg)

Fig. 4.1. Regression interpretation of control variate method. The regression line through the points  $(X_i, Y_i)$  has slope  $b_n$  and passes through  $(\bar{X}, \bar{Y})$ . The control variate estimator  $\bar{Y}(\hat{b}_n)$  is the value fitted by the line at  $\mathsf{E}[X]$ . In the figure, the sample mean  $\bar{X}$  underestimates  $\mathsf{E}[X]$  and  $\bar{Y}$  is adjusted upward accordingly.

## Examples

To make the method of control variates more tangible, we now illustrate it with several examples.

**Example 4.1.1** Underlying assets. In derivative pricing simulations, underlying assets provide a virtually universal source of control variates. We know from Section  $1.2.1$  that the absence of arbitrage is essentially equivalent to the requirement that appropriately discounted asset prices be martingales. Any martingale with a known initial value provides a potential control variate precisely because its expectation at any future time is its initial value. To be concrete, suppose we are working in the risk-neutral measure and suppose the interest rate is a constant r. If  $S(t)$  is an asset price, then  $\exp(-rt)S(t)$  is a martingale and  $E[\exp(-rT)S(T)] = S(0)$ . Suppose we are pricing an option on S with discounted payoff Y, some function of  $\{S(t), 0 \le t \le T\}$ . From independent replications  $S_i$ ,  $i = 1, \ldots, n$ , each a path of S over  $[0, T]$ , we can form the control variate estimator

$$\frac{1}{n}\sum_{i=1}^{n}(Y_i-b[S_i(T)-e^{rT}S(0)]),$$

or the corresponding estimator with b replaced by  $\hat{b}_n$ . If  $Y = e^{-rT}(S(T)-K)^+$ , so that we are pricing a standard call option, the correlation between  $Y$  and  $S(T)$  and thus the effectiveness of the control variate depends on the strike K. At  $K = 0$  we would have perfect correlation; for an option that is deep out-of-the-money (i.e., with large  $K$ ), the correlation could be quite low. This

188

is illustrated in Table 4.1 for the case of  $S \sim \text{GBM}(r, \sigma^2)$  with parameters  $r = 5\%, \sigma = 30\%, S(0) = 50, \text{ and } T = 0.25.$  This example shows that the effectiveness of a control variate can vary widely with the parameters of a problem.  $\Box$ 

٠.

| $\begin{array}{c cccc} K & 40 & 45 & 50 & 55 & 60 & 65 & 70 \\ \hat{\rho} & 0.995 & 0.968 & 0.895 & 0.768 & 0.604 & 0.433 & 0.286 \\ \hat{\rho}^2 & 0.99 & 0.94 & 0.80 & 0.59 & 0.36 & 0.19 & 0.08 \end{array}$ |  |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|

**Table 4.1.** Estimated correlation  $\hat{\rho}$  between  $S(T)$  and  $(S(T) - K)^+$  for various values of K, with  $S(0) = 50$ ,  $\sigma = 30\%$ ,  $r = 5\%$ , and  $T = 0.25$ . The third row measures the fraction of variance in the call option payoff eliminated by using the underlying asset as a control variate.

**Example 4.1.2** Tractable options. Simulation is sometimes used to price complex options in a model in which simpler options can be priced in closed form. For example, even under Black-Scholes assumptions, some pathdependent options require simulation for pricing even though formulas are available for simpler options. A tractable option can sometimes provide a more effective control than the underlying asset.

A particularly effective example of this idea was suggested by Kemna and Vorst [209] for the pricing of Asian options. Accurate pricing of an option on the arithmetic average

$$\bar{S}_A = \frac{1}{n} \sum_{i=1}^n S(t_i)$$

requires simulation, even if  $S$  is geometric Brownian motion. In contrast, calls and puts on the geometric average

$$\bar{S}_G = \left(\prod_{i=1}^n S(t_i)\right)^{1/n}$$

can be priced in closed form, as explained in Section  $3.2.2$ . Thus, options on  $S_G$  can be used as control variates in pricing options on  $\bar{S}_A$ .

Figure 4.2 shows scatter plots of simulated values of  $(\bar{S}_A - K)^+$  against the terminal value of the underlying asset  $S(T)$ , a standard call payoff  $(S(T)-K)^{+}$ , and the geometric call payoff  $(\bar{S}_{G}-K)^{+}$ . The figures are based on  $K = 50$  and thirteen equally spaced averaging dates; all other parameters are as in Example  $4.1.1$ . The leftmost panel shows that the weak correlation between  $\bar{S}_A$  and  $S(T)$  is further weakened by applying the call option payoff to  $\bar{S}_A$ , which projects negative values of  $\bar{S}_A - K$  to zero; the resulting correlation is approximately  $0.79$ . The middle panel shows the effect of applying the call option pavoff to  $S(T)$  as well: in this case the correlation increases

to approximately  $0.85$ . The rightmost panel illustrates the extremely strong relation between the payoffs on the arithmetic and geometric average call options. The correlation in this case is greater then  $0.99$ . A similar comparison is made in Broadie and Glasserman [67].  $\Box$ 

![](_page_5_Figure_2.jpeg)

Fig. 4.2. Scatter plots of payoff of call option on arithmetic average against the underlying asset, the payoff of a standard call, and the payoff of a call on the geometric average.

**Example 4.1.3** Bond prices. In a model with stochastic interest rates, bond prices often provide a convenient source of control variates. As emphasized in Sections  $3.3-3.4$  and Sections  $3.6-3.7$ , an important consideration in implementing an interest rate simulation is ensuring that the simulation correctly prices bonds. While this is primarily important for consistent pricing, as a byproduct it makes bonds available as control variates. Bonds may be viewed as the underlying assets of an interest rate model, so in a sense this example is a special case of Example  $4.1.1$ .

In a model of the short rate  $r(t)$ , a bond maturing at time T has initial price

 $4.1$  Control Variates 191

$$B(0,T) = \mathsf{E}\left[\exp\left(-\int_0^T r(u) \, du\right)\right],$$

the expectation taken with respect to the risk-neutral measure. Since we may assume that  $B(0,T)$  is known, the quantity inside the expectation provides a potential control variate. But even if  $r$  is simulated without discretization error at dates  $t_1, \ldots, t_n = T$ , the difference

$$\exp\left(-\frac{1}{n}\sum_{i=1}^{n}r(t_{i})\right)-B(0,T)$$

will not ordinarily have mean 0 because of the error in approximating the integral. Using this difference in a control variate estimator could therefore introduce some bias, though the bias can be made as small as necessary by taking a sufficiently fine partition of  $[0,T]$ . In our discussion of the Vasicek model in Section 3.3, we detailed the exact joint simulation of  $r(t_i)$  and its time integral

$$Y(t_i) = \int_0^{t_i} r(u) \, du.$$

This provides a bias-free control variate because

$$\mathsf{E}\left[\exp(-Y(T))\right] = B(0,T).$$

Similar considerations apply to the forward rate models of Sections 3.6 and 3.7. In our discussion of the Heath-Jarrow-Morton framework, we devoted considerable attention to deriving the appropriate discrete drift condition. Using this drift in a simulation produces unbiased bond price estimates and thus makes bonds available as control variates. In our discussion of LIBOR market models, we noted that discretizing the system of SDEs for the LIBOR rates  $L_n$  would not produce unbiased bond estimates; in contrast, the methods in Section 3.7 based on discretizing deflated bonds or their differences do produce unbiased estimates and thus allow the use of bonds as control variates.

Comparison of this discussion with the one in Section  $3.7.3$  should make clear that the question of whether or not asset prices can be used as control variates is closely related to the question of whether a simulated model is  $\text{arbitrage-free.} \quad \Box$ 

**Example 4.1.4** Tractable dynamics. The examples discussed thus far are all based on using one set of prices in a model as control variates for some other price in the same model. Another strategy for developing effective control variates uses prices in a simpler model. We give two illustrations of this idea.

Consider, first, the pricing of an option on an asset whose dynamics are modeled by

$$\frac{dS(t)}{S(t)} = r \, dt + \sigma(t) \, dW(t),$$

where  $\sigma(t)$  may be function of  $S(t)$  or may be stochastic and described by a second SDE. We might simulate S at dates  $t_1, \ldots, t_n$  using an approximation of the form

$$S(t_{i+1}) = S(t_i) \exp\left( [r - \frac{1}{2}\sigma(t_i)^2](t_{i+1} - t_i) + \sigma(t_i)\sqrt{t_{i+1} - t_i}Z_{i+1} \right),$$

where the  $Z_i$  are independent  $N(0,1)$  variables. In a stochastic volatility model, a second recursion would determine the evolution of  $\sigma(t_i)$ . Suppose the option we want to price would be tractable if the underlying asset were geometric Brownian motion. Then along with  $S$  we could simulate

$$\tilde{S}(t_{i+1}) = \tilde{S}(t_i) \exp\left( [r - \frac{1}{2}\tilde{\sigma}^2](t_{i+1} - t_i) + \tilde{\sigma}\sqrt{t_{i+1} - t_i}Z_{i+1} \right)$$

for some constant  $\tilde{\sigma}$ , the same sequence  $Z_i$ , and with initial condition  $S(0)$  $S(0)$ . If, for example, the option is a standard call with strike K and expiration  $t_n$ , we could form a controlled estimator using independent replications of

$$(S(t_n)-K)^+ - b\left((\tilde{S}(t_n)-K)^+ - \mathsf{E}\left[(\tilde{S}(t_n)-K)^+\right]\right)$$

Except for a discount factor, the expectation on the right is given by the Black-Scholes formula. For effective variance reduction, the constant  $\tilde{\sigma}$  should be chosen close to a typical value of  $\sigma$ .

As a second illustration of this idea, recall that the dynamics of forward LIBOR under the spot measure in Section  $3.7$  are given by

$$\frac{dL_n(t)}{L_n(t)} = \sum_{j=\eta(t)}^n \frac{\sigma_j(t)^\top \sigma_n(t) \delta_j L_j(t)}{1 + \delta_j L_j(t)} dt + \sigma_n(t)^\top dW(t), \quad n = 1, \dots, M. \tag{4.6}$$

Suppose the  $\sigma_n$  are deterministic functions of time. Along with the forward LIBOR rates, we could simulate auxiliary processes

$$\frac{dS_n(t)}{S_n(t)} = \sigma_n^\top(t) \, dW(t), \quad n = 1, \dots, M. \tag{4.7}$$

These form a multivariate geometric Brownian motion and lend themselves to tractable pricing and thus to control variates. Alternatively, we could use

$$\frac{d\tilde{L}_n(t)}{\tilde{L}_n(t)} = \sum_{j=\eta(t)}^n \frac{\sigma_j(t)^\top \sigma_n(t) \delta_j L_j(0)}{1 + \delta_j L_j(0)} dt + \sigma_n(t)^\top dW(t). \tag{4.8}$$

Notice that the drift in this expression is a function of the constants  $L_j(0)$ rather than the stochastic processes  $L_j(t)$  appearing in the drift in (4.6). Hence,  $L_n$  is also a geometric Brownian motion though with time-varying drift. Even if an option on the  $S_n$  or  $L_n$  cannot be valued in closed form, if it can be valued quickly using a numerical procedure it may yield an effective control variate.

The evolution of  $L_n$ ,  $S_n$ , and  $L_n$  is illustrated in Figure 4.3. This example initializes all rates at 6%, takes  $\delta_i \equiv 0.5$  (corresponding to semi-annual rates), and assumes a stationary specification of the volatility functions in which  $\sigma_n(t) \equiv \sigma(n-\eta(t)+1)$  with  $\sigma$  increasing linearly from 0.15 to 0.25. The figure plots the evolution of  $L_{40}$ ,  $S_{40}$ , and  $L_{40}$  using a log-Euler approximation of the type in (3.120). The figure indicates that  $L_{40}$  tracks  $L_{40}$  quite closely and that even  $S_{40}$  is highly correlated with  $L_{40}$ .

![](_page_8_Figure_2.jpeg)

Fig. 4.3. A sample path of  $L_{40}$  using the true dynamics in (4.6), the geometric Brownian motion approximation  $L_{40}$  with time-varying drift, and the driftless geometric Brownian motion  $S_{40}$ .

It should be noted that simulating an auxiliary process as suggested here may substantially increase the time required per replication — perhaps even doubling it. As with any variance reduction technique, the benefit must be weighed against the additional computing time required, using the principles in Section 1.1.3.  $\Box$ 

**Example 4.1.5** Hedges as controls. There is a close link between the selection of control variates and the selection of hedging instruments. If  $Y$  is a discounted payoff and we are estimating  $E[Y]$ , then any instrument that serves as an effective hedge for  $Y$  also serves as an effective control variate if it can be easily priced. Indeed, the calculation of the optimal coefficient  $b^*$  is identical to the calculation of the optimal hedge ratio in minimum-variance hedging (see, e.g., Section 2.9 of Hull  $[189]$ ).

Whereas a static hedge (a fixed position in another asset) may provide significant variance reduction, a dynamic hedge can, in principle, remove all

 $variance$  — at least under the assumptions of a complete market and continuous trading as discussed in Section  $1.2.1$ . Using the notation of Section  $1.2.1$ , let  $V(t)$  denote the value at time t of a price process that can be replicated through a self-financing trading strategy applied to a set of underlying assets  $S_j, j = 1, \ldots, d$ . As in Section 1.2.1, under appropriate conditions we have

$$V(T) = V(0) + \int_0^T \sum_{j=1}^d \frac{\partial V(t)}{\partial S_j} \, dS_j(t).$$

In other words,  $V$  is replicated through a delta-hedging strategy that holds  $\partial V/\partial S_j$  shares of asset  $S_j$  at each instant. This suggests that  $V(T)$  should be highly correlated with

$$\sum_{i=1}^{m} \sum_{j=1}^{d} \frac{\partial V(t_{i-1})}{\partial S_j} [S_j(t_i) - S_j(t_{i-1})]$$
(4.9)

where  $0 = t_0 < t_1 < \cdots < t_m \equiv T$ ; this is a discrete-time approximation to the dynamic hedging strategy. Of course, in practice if  $V(t)$  is unknown then its derivatives are likely to be unknown. One may still obtain an effective control variate by using a rough approximation to the  $\partial V/\partial S_i$ ; for example, one might calculate these deltas as though the underlying asset prices followed geometric Brownian motions, even if their actual dynamics are more complex. See Clewlow and Carverhill  $[87]$  for examples of this.

Using an expression like  $(4.9)$  as a control variate is somewhat similar to using all the increments  $S_j(t_i) - S_j(t_{i-1})$  as controls or, more conveniently, the increments of the discounted asset prices since these have mean zero. The main difference is that the coefficients  $\partial V/\partial S_i$  in (4.9) will not in general be constants but will depend on the  $S_j$  themselves. We may therefore interpret (4.9) as using the  $S_j(t_i) - S_j(t_{i-1})$  as nonlinear control variates. We discuss nonlinear controls more generally in Section 4.1.4.  $\Box$ 

**Example 4.1.6** Primitive controls. In the examples above, we have stressed the use of special features of derivative pricing models in identifying potential control variates. Indeed, significant variance reduction is usually achieved only by taking advantage of special properties of a model. It is nevertheless worth mentioning that many generic (and thus typically not very effective) control variates are almost always available in a simulation. For example, most of the models discussed in Chapter 3 are simulated from a sequence  $Z_1, Z_2, \ldots$ of independent standard normal random variables. We know that  $\mathsf{E}[Z_i] = 0$ and  $\text{Var}[Z_i] = 1$ , so the sample mean and sample variance of the  $Z_i$  are available control variates. At a still more primitive level, most simulations start from a sequence  $U_1, U_2, \ldots$  of independent Unif[0,1] random variables. Sample moments of the  $U_i$  can also be used as controls.  $\Box$ 

Later in this chapter we discuss other techniques for reducing variance. In a sense, all of these can be viewed as strategies for selecting control variates.

For suppose we want to estimate  $E[Y]$  and in addition to the usual sample mean  $\bar{Y}$  we have available an alternative unbiased estimator Y. The difference  $(\bar{Y}-\bar{Y})$  has (known) expectation zero and can thus be used to form a control variate estimate of the form

$$\bar{Y} - b(\bar{Y} - \tilde{Y}).$$

The special cases  $b = 0$  and  $b = 1$  correspond to using just one of the two estimators; by optimizing b, we obtain a combined estimator that has lower variance than either of the two.

## Output Analysis

In analyzing variance reduction techniques, along with the effectiveness of a technique it is important to consider how the technique affects the statistical interpretation of simulation outputs. So long as we deal with unbiased, independent replications, computing confidence intervals for expectations is a simple matter, as noted in Section 1.1 and explained in Appendix A. But we will see that some variance reduction techniques complicate interval estimation by introducing dependence across replications. This issue arises with control variates if we use the estimated coefficient  $b_n$  in (4.5). It turns out that in the case of control variates the dependence can be ignored in large samples; a more careful consideration of small-sample issues will be given in Section  $4.1.3$ .

For any fixed b, the control variate estimator  $\bar{Y}(b)$  in (4.1) is the sample mean of independent replications  $Y_i(b), i = 1, \ldots, n$ . Accordingly, an asymptotically valid  $1 - \delta$  confidence interval for  $\mathsf{E}[Y]$  is provided by

$$\bar{Y}(b) \pm z_{\delta/2} \frac{\sigma(b)}{\sqrt{n}},\tag{4.10}$$

where  $z_{\delta/2}$  is the  $1-\delta/2$  quantile from the normal distribution  $(\Phi(z_{\delta/2}) =$  $(1 - \delta/2)$  and  $\sigma(b)$  is the standard deviation per replication, as in (4.2).

In practice,  $\sigma(b)$  is typically unknown but can be estimated using the sample standard deviation

$$s(b) = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (Y_i(b) - \bar{Y}(b))^2}.$$

The confidence interval (4.10) remains asymptotically valid if we replace  $\sigma(b)$ with  $s(b)$ , as a consequence of the limit in distribution

$$\frac{Y(b) - \mathsf{E}[Y]}{\sigma(b)/\sqrt{n}} \Rightarrow N(0,1)$$

and the fact that  $s(b)/\sigma(b) \to 1$ ; see Appendix A.2. If we use the estimated coefficient  $\hat{b}_n$  in (4.5), then the estimator

$$\bar{Y}(\hat{b}_n) = \frac{1}{n} \sum_{i=1}^n (Y_i - \hat{b}_n(X_i - \mathsf{E}[X]))$$

is not quite of the form  $\bar{Y}(b)$  because we have replaced the constant b with the random quantity  $\hat{b}_n$ . Nevertheless, because  $\hat{b}_n \to b^*$ , we have

$$\sqrt{n}(\bar{Y}(\hat{b}_n) - \bar{Y}(b^*)) = (\hat{b}_n - b^*) \cdot \sqrt{n}(\bar{X} - \mathsf{E}[X]) \Rightarrow 0 \cdot N(0, \sigma_X^2) = 0,$$

so  $\bar{Y}(\hat{b}_n)$  satisfies the same central limit theorem as  $\bar{Y}(b^*)$ . This means that  $\bar{Y}(\hat{b}_n)$  is asymptotically as precise as  $\bar{Y}(b^*)$ . Moreover, the central limit theorem applies in the form

$$\frac{\bar{Y}(\hat{b}_n) - \mathsf{E}[Y]}{s(\hat{b}_n) / \sqrt{n}} \Rightarrow N(0, 1),$$

with  $s(\hat{b}_n)$  the sample standard deviation of the  $Y_i(\hat{b}_n)$ ,  $i = 1, \ldots, n$ , because  $s(\hat{b}_n)/\sigma(b^*) \to 1$ . In particular, the confidence interval (4.10) remains asymptotically valid if we replace  $\bar{Y}(b)$  and  $\sigma(b)$  with  $\bar{Y}(\hat{b}_n)$  and  $s(\hat{b}_n)$ , and confidence intervals estimated using  $\hat{b}_n$  are asymptotically no wider than confidence intervals estimated using the optimal coefficient  $b^*$ .

We may summarize this discussion as follows. It is a simple matter to estimate asymptotically valid confidence intervals for control variate estimators. Moreover, for large  $n$ , we get all the benefit of the optimal coefficient  $b^*$  by using the estimate  $b_n$ . However, for finite n, there may still be costs to using an estimated rather than a fixed coefficient; we return to this point in Section  $4.1.3$ .

## 4.1.2 Multiple Controls

We now generalize the method of control variates to the case of multiple controls. Examples  $4.1.1-4.1.6$  provide ample motivation for considering this extension.

- $\circ$  If  $e^{-rt}S(t)$  is a martingale, then  $e^{-rt_1}S(t_1), \ldots, e^{-rt_d}S(t_d)$  all have expectation  $S(0)$  and thus provide d controls on each path.
- $\circ$  If the simulation involves d underlying assets, the terminal values of all assets may provide control variates.
- o Rather than use a single option as a control variate, we may want to use options with multiple strikes and maturities.
- $\circ$  In an interest rate simulation, we may choose to use d bonds of different maturities as controls.

Suppose, then, that each replication  $i$  of a simulation produces outputs  $Y_i$  and  $X_i = (X_i^{(1)}, \ldots, X_i^{(d)})^{\top}$  and suppose the vector of expectations  $\mathsf{E}[X]$  is known. We assume that the pairs  $(X_i, Y_i), i = 1, \ldots, n$ , are i.i.d. with covariance matrix

 $4.1$  Control Variates 197

$$\begin{pmatrix} \Sigma_X & \Sigma_{XY} \\ \Sigma_{XY}^\top & \sigma_Y^2 \end{pmatrix} . \tag{4.11}$$

Here,  $\Sigma_X$  is  $d \times d$ ,  $\Sigma_{XY}$  is  $d \times 1$ , and, as before the scalar  $\sigma_Y^2$  is the variance of the  $Y_i$ . We assume that  $\Sigma_X$  is nonsingular; otherwise, some  $X^{(k)}$  is a linear combination of the other  $X^{(j)}$ s and may be removed from the set of controls.

Let  $\bar{X}$  denote the vector of sample means of the controls. For fixed  $b \in \mathbb{R}^d$ , the control variate estimator  $\bar{Y}(b)$  is

$$\bar{Y}(b) = \bar{Y} - b^{\top}(\bar{X} - \mathsf{E}[X]).$$

Its variance per replication is

$$\mathsf{Var}[Y_i - b^\top (X_i - \mathsf{E}[X])] = \sigma_Y^2 - 2b^\top \Sigma_{XY} + b^\top \Sigma_{XX} b. \tag{4.12}$$

This is minimized at

$$b^* = \Sigma_X^{-1} \Sigma_{XY}.\tag{4.13}$$

As in the case of a single control variate, this is also the slope (more precisely, the vector of coefficients) in a regression of Y against  $X$ .

As is customary in regression analysis, define

$$R^2 = \Sigma_{XY}^\top \Sigma_X^{-1} \Sigma_{XY} / \sigma_Y^2; \tag{4.14}$$

this generalizes the squared correlation coefficient between scalar  $X$  and  $Y$  and measures the strength of the linear relation between the two. Substituting  $b^*$ into the expression for the variance per replication and simplifying, we find that the minimal variance (that is, the variance of  $Y_i(b^*)$ ) is

$$\sigma_Y^2 - \Sigma_{XY}^\top \Sigma_X^{-1} \Sigma_{XY} = (1 - R^2) \sigma_Y^2. \tag{4.15}$$

Thus,  $R^2$  measures the fraction of the variance of Y that is removed in optimally using  $X$  as a control.

In practice, the optimal vector of coefficients  $b^*$  is unknown but may be estimated. The standard estimator replaces  $\Sigma_X$  and  $\Sigma_{XY}$  in (4.13) with their sample counterparts to get

$$\hat{b}_n = S_X^{-1} S_{XY}, \tag{4.16}$$

where  $S_X$  is the  $d \times d$  matrix with  $jk$  entry

$$\frac{1}{n-1} \left( \sum_{i=1}^{n} X_i^{(j)} X_i^{(k)} - n \bar{X}^{(j)} \bar{X}^{(k)} \right) \tag{4.17}$$

and  $S_{XY}$  is the *d*-vector with *j*th entry

$$\frac{1}{n-1}\left(\sum_{i=1}^n X_i^{(j)}Y_i - n\bar{X}^{(j)}\bar{Y}\right).$$

 $\mathbb{Q}^{\mathbb{Z}}_{\mathbb{Z}}$ 

The number of controls  $d$  is ordinarily not very large so size is not an obstacle in inverting  $S_X$ , but if linear combinations of some of the controls are highly correlated this matrix may be nearly singular. This should be considered in choosing multiple controls.

A simple estimate of the variance of  $\bar{Y}(\hat{b}_n)$  is provided by  $s_n/\sqrt{n}$  where  $s_n$  is the sample standard deviation of the adjusted replications

$$Y_i(\hat{b}_n) = Y_i - \hat{b}_n^\top (X_i - \mathsf{E}[X]).$$

The estimator  $s_n$  ignores the fact that  $b_n$  is itself estimated from the replications, but it is nevertheless a consistent estimator of  $\sigma_Y(b^*)$ , the optimal standard deviation in (4.15). An asymptotically valid  $1-\delta$  confidence interval is thus provided by

$$\bar{Y}(\hat{b}_n) \pm z_{\delta/2} \frac{s_n}{\sqrt{n}}.\tag{4.18}$$

The connection between control variates and regression analysis suggests an alternative way of forming confidence intervals; under additional assumptions about the joint distribution of the  $(X_i, Y_i)$  the alternative is preferable, especially if  $n$  is not very large. We return to this point in Section 4.1.3.

### Variance Decomposition

In looking for effective control variates, it is useful to understand what part of the variance of an ordinary estimator is removed through the use of controls. We now address this point.

Let  $(X, Y)$  be any random vector with Y scalar and X d-dimensional. Let  $(X,Y)$  have the partitioned covariance matrix in (4.11). For any b, we can write

$$Y = \mathsf{E}[Y] + b^{\top}(X - \mathsf{E}[X]) + \epsilon,$$

simply by defining  $\epsilon$  so that equality holds. If  $b = b^* = \Sigma_X^{-1} \Sigma_{XY}$ , then in fact  $\epsilon$  is uncorrelated with X; i.e.,  $Y - b^{*\top}(X - \mathsf{E}[X])$  is uncorrelated with X so

$$\mathsf{Var}[Y] = \mathsf{Var}[b^{*\top}X] + \mathsf{Var}[\epsilon] = \mathsf{Var}[b^{*\top}X] + \mathsf{Var}[Y - b^{*\top}X].$$

In this decomposition, the part of  $\text{Var}[Y]$  eliminated by using X as a control is  $\mathsf{Var}[b^{*\top}X]$  and the remaining variance is  $\mathsf{Var}[\epsilon]$ .

The optimal vector  $b^*$  makes  $b^{*\top}(X - \mathsf{E}[X])$  the projection of  $Y - \mathsf{E}[Y]$ onto  $X - \mathsf{E}[X]$ ; the residual  $\epsilon$  may be interpreted as the part of  $Y - \mathsf{E}[Y]$ orthogonal to  $X - \mathsf{E}[X]$ , orthogonal here meaning uncorrelated. The smaller this orthogonal component (as measured by its variance), the greater the variance reduction achieved by using  $X$  as a control for  $Y$ . If, in particular, Y is a linear combination of the components of X, then using X as a control eliminates all variance. Of course, in this case  $E[Y]$  is a linear combination of the (known) components of  $\mathsf{E}[X]$ , so simulation would be unnecessary.

Consider, again, the examples with which we opened this section. If we use multiple path values  $S(t_i)$  of an underlying asset as control variates, we eliminate all variance in estimating the expected value of any instrument whose payoff is a linear combination of the  $S(t_i)$ . (In particular, each  $\mathsf{E}[S(t_i)]$ is trivially estimated without error if we use  $S(t_i)$  as a control.) The variance that remains in estimating an expected payoff while using the  $S(t_i)$  as controls is attributable to the part of the payoff that is uncorrelated with the  $S(t_i)$ . Similarly, if we use bond prices as control variates in pricing an interest rate derivative, the remaining variance is due to the part of the derivative's payoff that is uncorrelated with any linear combination of bond prices.

## Control Variates and Weighted Monte Carlo

In introducing the idea of a control variate in Section  $4.1.1$ , we explained that the observed error in estimating a known quantity could be used to adjust an estimator of an unknown quantity. But the technique has an alternative interpretation as a method for assigning weights to replications. This alternative perspective is sometimes useful, particularly in relating control variates to other methods.

For simplicity, we start with the case of a single control; thus,  $Y_i$  and  $X_i$ are scalars and the pairs  $(X_i, Y_i)$  are i.i.d. The control variate estimator with estimated optimal coefficient  $\hat{b}_n$  is  $\bar{Y}(\hat{b}_n) = \bar{Y} - \hat{b}_n(\bar{X} - \mathsf{E}[X]).$  As in (4.5), the estimated coefficient is given by

$$\hat{b}_n = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^n (X_i - \bar{X})^2}.$$

By substituting this expression into  $\bar{Y}(\hat{b}_n)$  and simplifying, we arrive at

$$\bar{Y}(\hat{b}_n) = \sum_{i=1}^n \left(\frac{1}{n} + \frac{(\bar{X} - X_i)(\bar{X} - \mathsf{E}[X])}{\sum_{i=1}^n (X_i - \bar{X})^2}\right) Y_i \equiv \sum_{i=1}^n w_i Y_i. \tag{4.19}$$

In other words, the control variate estimator is a weighted average of the replications  $Y_1, \ldots, Y_n$ . The weights  $w_i$  are completely determined by the observations  $X_1, \ldots, X_n$  of the control.

A similar representation applies with multiple controls. Using the estimated vector of coefficients in (4.16), the sample covariance matrix  $S_X$  in  $(4.17)$  and simplifying, we get

$$\bar{Y}(\hat{b}_n) = \sum_{i=1}^n \left(\frac{1}{n} + \frac{1}{n-1}(\bar{X} - X_i)^\top S_X^{-1}(\bar{X} - \mathsf{E}[X])\right) Y_i, \tag{4.20}$$

which is again a weighted average of the  $Y_i$ . Here, as before,  $X_i$  denotes the vector of controls  $(X_i^{(1)}, \ldots, X_i^{(d)})^{\top}$  from the *i*th replication, and  $\bar{X}$  and  $\mathsf{E}[X]$ 

The representation in  $(4.20)$  is a special case of a general feature of regression — namely, that a fitted value of Y is a weighted average of the observed values of the  $Y_i$  with weights determined by the  $X_i$ . One consequence of this representation is that if we want to estimate multiple quantities (e.g., prices of various derivative securities) from the same set of simulated paths using the same control variates, the weights can be calculated just once and then applied to all the outputs. Hesterberg and Nelson  $[178]$  also show that  $(4.20)$ is useful in applying control variates to quantile estimation. They indicate that although it is possible for some of the weights in  $(4.19)$  and  $(4.20)$  to be negative, the probability of negative weights is small in a sense they make precise.

### 4.1.3 Small-Sample Issues

In our discussion (following  $(4.10)$ ) of output analysis with the method of control variates, we noted that because  $\hat{b}_n$  converges to  $b^*$ , we obtain an asymptotically valid confidence interval if we ignore the randomness of  $\hat{b}_n$ and the dependence it introduces among  $Y_i(\hat{b}_n)$ ,  $i = 1, \ldots, n$ . Moreover, we noted that as  $n \to \infty$ , the variance reduction achieved using  $\hat{b}_n$  approaches the variance reduction that would be achieved if the optimal  $b^*$  were known.

In this section, we supplement these large-sample properties with a discussion of statistical issues that arise in analyzing control variate estimators based on a finite number of samples. We note that stronger distributional assumptions on the simulation output lead to confidence intervals valid for all  $n$ . Moreover, it becomes possible to quantify the loss in efficiency due to estimating  $b^*$ . This offers some guidance in deciding how many control variates to use in a simulation. This discussion is based on results of Lavenberg, Moeller, and Welch  $[221]$  and Nelson  $[277]$ .

For any fixed b, the control variate estimator  $Y(b)$  is unbiased. But using  $b_n$ , we have

$$\operatorname{Bias}(\bar{Y}(\hat{b}_n)) = \mathsf{E}[\bar{Y}(\hat{b}_n)] - \mathsf{E}[Y] = -\mathsf{E}[\hat{b}_n^\top(\bar{X} - \mathsf{E}[X])],$$

which need not be zero because  $\hat{b}_n$  and  $\bar{X}$  are not independent. A simple way to eliminate bias is to use  $n_1$  replications to compute an estimate  $\hat{b}_{n_1}$  and to then apply this coefficient with the remaining  $n - n_1$  replications of  $(X_i, Y_i)$ . This makes the coefficient estimate independent of  $\bar{X}$  and thus makes  $\mathsf{E}[\hat{b}_{n_1}^\top \bar{X}]$  $\mathsf{E}[\hat{b}_{n_1}^\top] \mathsf{E}[\bar{X}]$ . In practice, the bias produced by estimating  $b^*$  is usually small so the cost of estimating coefficients through separate replications is unattractive. Indeed, the bias is typically  $O(1/n)$ , whereas the standard error is  $O(1/\sqrt{n})$ .

Lavenberg, Moeller, and Welch [221] and Nelson [277] note that even if  $\hat{b}_n$  is estimated from the same replications used to compute  $\bar{Y}$  and  $\bar{X}$ , the control variate estimator is unbiased if the regression of  $Y$  on  $X$  is linear. More precisely, if

 $\mathsf{E}[Y|X] = c_0 + c_1 X^{(1)} + \dots + c_d X^{(d)} \quad \text{for some constants } c_0, c_1, \dots, c_d, \tag{4.21}$ 

then  $\mathsf{E}[\bar{Y}(\hat{b}_n)] = \mathsf{E}[Y]$ .

Å,

Under the additional assumption that  $\text{Var}[Y|X]$  does not depend on X, Nelson [277] notes that an *unbiased* estimator of the variance of  $\bar{Y}(\hat{b}_n)$ ,  $n > 1$  $d-1$ , is provided by

$$\hat{s}_n^2 = \left(\frac{1}{n-d-1} \sum_{i=1}^n [Y_i - \bar{Y}(\hat{b}_n) - \hat{b}_n^\top (X_i - \mathsf{E}[X])]^2\right)$$
$$\times \left(\frac{1}{n} + \frac{1}{n-1} (\bar{X} - \mathsf{E}[X])^\top S_X^{-1} (\bar{X} - \mathsf{E}[X])\right).$$

The first factor in this expression is the sample variance of the regression residuals, the denominator  $n-d-1$  reflecting the loss of  $d+1$  degrees of freedom in estimating the regression coefficients in  $(4.21)$ . The second factor inflates the variance estimate when  $\bar{X}$  is far from  $\mathsf{E}[X]$ .

As in Lavenberg et al.  $[221]$  and Nelson  $[277]$ , we now add a final assumption that  $(X, Y)$  has a multivariate normal distribution, from which two important consequences follow. The first is that this provides an exact confidence interval for  $E[Y]$  for all n: the interval

$$\bar{Y}(\hat{b}_n) \pm t_{n-d-1,\delta/2}\hat{s}_n \tag{4.22}$$

covers  $\mathsf{E}[Y]$  with probability  $1-\delta$ , where  $t_{n-d-1,\delta/2}$  denotes the  $1-\delta/2$ quantile of the t distribution with  $n-d-1$  degrees of freedom. This confidence interval may have better coverage than the crude interval  $(4.18)$ , even if the assumptions on which it is based do not hold exactly.

A second important conclusion that holds under the added assumption of normality is an exact expression for the variance of  $Y(b_n)$ . With d controls and  $n > d + 2$  replications,

$$\mathsf{Var}[\bar{Y}(\hat{b}_n)] = \frac{n-2}{n-d-2}(1-R^2)\frac{\sigma_Y^2}{n}.$$
 (4.23)

Here, as before,  $\sigma_Y^2 = \text{Var}[Y]$  is the variance per replication without controls and  $R^2$  is the squared multiple correlation coefficient defined in (4.14). As noted in (4.15),  $(1 - R^2)\sigma_V^2$  is the variance per replication of the control variate estimator with known optimal coefficient. We may thus write  $(4.23)$  $as$ 

$$\mathsf{Var}[\bar{Y}(\hat{b}_n)] = \frac{n-2}{n-d-2} \mathsf{Var}[\bar{Y}(b^*)]. \tag{4.24}$$

In light of this relation, Lavenberg et al. [221] call  $(n-2)/(n-d-2)$  the loss factor measuring the loss in efficiency due to using the estimate  $\hat{b}_n$  rather than the exact value  $b^*$ .

Both  $(4.22)$  and  $(4.24)$  penalize the use of too many controls — more precisely, they penalize the use of control variates that do not provide a sufficiently large reduction in variance. In  $(4.99)$ , a larger directly in a loss of

degrees of freedom, a larger multiplier  $t_{n-d-1,\delta/2}$ , and thus a wider confidence interval unless the increase in d is offset by a sufficient decrease in  $\hat{s}_n$ . In (4.24), a larger  $d$  results in a larger loss factor and thus a greater efficiency cost from using estimated coefficients. In both cases, the cost from using more controls is eventually overwhelmed by increasing the sample size  $n$ ; what constitutes a reasonable number of control variates thus depends in part on the intended number of replications.

The validity of the confidence interval  $(4.22)$  and the loss factor in  $(4.24)$ depends on the distributional assumptions on  $(X, Y)$  introduced above leading up to  $(4.22)$ ; in particular, these results depend on the assumed normality of  $(X, Y)$ . (Loh [239] provides extensions to more general distributions but these seem difficult to use in practice.) In pricing applications,  $Y$  would often be the discounted payoff of an option contract and thus highly skewed and distinctly non-normal. In this case, application of  $(4.22)$  and  $(4.24)$  lacks theoretical support.

Nelson [277] analyzes the use of various remedies for control variate estimators when the distributional assumptions facilitating their statistical analysis fail to hold. Among the methods he examines is *batching*. This method groups the replications  $(X_i, Y_i), i = 1, \ldots, n$ , into k disjoint batches of  $n/k$  replications each. It then calculates sample means of the  $(X_i, Y_i)$  within each batch and applies the usual control variate procedure to the  $k$  sample means of the  $k$  batches. The appeal of this method lies in the fact that the batch means should be more nearly normally distributed than the original  $(X_i, Y_i)$ . The cost of batching lies in the loss of degrees of freedom: it reduces the effective sample size from  $n$  to  $k$ . Based on a combination of theoretical and experimental results, Nelson  $[277]$  recommends forming 30 to 60 batches if up to five controls are used. With a substantially larger number of controls, the cost of replacing the number of replications n with  $k = 30{\text -}60$  in (4.22) and (4.24) would be more significant; this would argue in favor of using a larger number of smaller batches.

Another strategy for potentially improving the performance of control variate estimators replaces the estimated covariance matrix  $S_X$  with its true value  $\Sigma_X$  in estimating  $b^*$ . This is feasible if  $\Sigma_X$  is known, which would be the case in at least some of the examples introduced in Section  $4.1.1$ . Nelson [277] and Bauer, Venkatraman, and Wilson [40] analyze this alternative; perhaps surprisingly, they find that it generally produces estimators inferior to the usual method based on  $b_n$ .

## 4.1.4 Nonlinear Controls

Our discussion of control variates has thus far focused exclusively on *linear* controls, meaning estimators of the form

$$\bar{Y} - b^{\top}(\bar{X} - \mathsf{E}[X]),\tag{4.25}$$

with the vector  $b$  either known or estimated. There are, however, other ways one might use the discrepancy between  $\bar{X}$  and  $\mathsf{E}[X]$  to try to improve the estimator  $\bar{Y}$  in estimating  $\mathsf{E}[Y]$ . For example, in the case of scalar X, the estimator

$$\bar{Y}\frac{\mathsf{E}[X]}{\bar{X}}$$

adjusts  $\bar{Y}$  upward if  $0 < \bar{X} < \mathsf{E}[X]$ , downward if  $0 < \mathsf{E}[X] < \bar{X}$ , and thus may be attractive if  $X_i$  and  $Y_i$  are positively correlated. Similarly, the estimator  $\bar{Y}\bar{X}/\mathsf{E}[X]$  may have merit if the  $X_i$  and  $Y_i$  are negatively correlated. Other estimators of this type include

$$\bar{Y} \exp\left(\bar{X} - \mathsf{E}[X]\right)$$
 and  $\bar{Y}^{(X/\mathsf{E}[X])}$ .

In each case, the convergence of  $\bar{X}$  to  $\mathsf{E}[X]$  ensures that the adjustment to  $\overline{Y}$  vanishes as the sample size increases, just as in (4.25). But for any finite number of replications, the variance of the adjusted estimator could be larger or smaller than that of  $\bar{Y}$ .

These are examples of *nonlinear* control variate estimators. They are all special cases of estimators of the form  $h(\bar{X}, \bar{Y})$  for functions h satisfying

$$h(\mathsf{E}[X], y) = y$$
 for all y.

The difference between the controlled estimator  $h(\bar{X}, \bar{Y})$  and  $\bar{Y}$  thus depends on the deviation of  $\bar{X}$  from  $\mathsf{E}[X]$ .

Although the introduction of nonlinear controls would appear to substantially enlarge the class of candidate estimators, it turns out that in large samples, a nonlinear control variate estimator based on a smooth  $h$  is equivalent to an ordinary linear control variate estimator. This was demonstrated in Glynn and Whitt [159], who note a related observation in Cheng and Feast [84]. We present the analysis leading to this conclusion and then discuss its implications.

## Delta Method

The main tool for the large-sample analysis of nonlinear control variate estimators is the *delta method*. This is a result providing a central limit theorem for functions of sample means. To state it generally, we let  $\xi_i$ ,  $i = 1, 2, \ldots$  be i.i.d. random vectors in  $\mathbb{R}^k$  with mean vector  $\mu$  and covariance matrix  $\Sigma$ . The sample mean  $\bar{\xi}$  of  $\xi_1,\ldots,\xi_n$  satisfies the central limit theorem

$$\sqrt{n}[\bar{\xi} - \mu] \Rightarrow N(0, \Sigma).$$

Now let  $h: \mathbb{R}^k \to \mathbb{R}$  be continuously differentiable in a neighborhood of  $\mu$  and suppose the partial derivatives of h at  $\mu$  are not all zero. For sufficiently large  $n$ , a Taylor approximation gives

$$h(\xi) = h(\mu) + \nabla h(\zeta_n)[\xi - \mu],$$

with  $\nabla h$  the gradient of h (a row vector) and  $\zeta_n$  a point on the line segment joining  $\mu$  and  $\bar{\xi}$ . As  $n \to \infty$ ,  $\bar{\xi} \to \mu$  and thus  $\zeta_n \to \mu$  as well; continuity of the gradient implies  $\nabla h(\zeta_n) \to \nabla h(\mu)$ . Thus, for large n, the error  $h(\bar{\xi}) - h(\mu)$ is approximately the inner product of the constant vector  $\nabla h(\mu)$  and the asymptotically normal vector  $\bar{\xi} - \mu$ , and is itself asymptotically normal. More precisely,

$$\sqrt{n}[h(\bar{\xi}) - h(\mu)] \Rightarrow N(0, \nabla h(\mu) \Sigma \nabla h(\mu)^{\top}). \tag{4.26}$$

See also Section 3.3 of Serfling  $[326]$ , for example.

For the application to nonlinear controls, we replace  $\xi_i$  with  $(X_i, Y_i)$ ,  $\mu$ with  $(\mathsf{E}[X], \mathsf{E}[Y])$ , and  $\Sigma$  with

$$\Sigma = \begin{pmatrix} \Sigma_X & \Sigma_{XY} \\ \Sigma_{XY}^\top & \sigma_Y^2 \end{pmatrix},$$

the covariance matrix in  $(4.11)$ . From the delta method, we know that the nonlinear control variate estimator is asymptotically normal with

$$\sqrt{n}[h(\bar{X}, \bar{Y}) - \mathsf{E}[Y]] \Rightarrow N(0, \sigma_h^2),$$

(recall that  $h(\mathsf{E}[X], \mathsf{E}[Y]) = \mathsf{E}[Y]$ ) and

$$\sigma_h^2 = \left(\frac{\partial h}{\partial y}\right)^2 \sigma_Y^2 + 2\left(\frac{\partial h}{\partial y}\right) \nabla_x h \Sigma_{XY} + \nabla_x h \Sigma_X \nabla_x h^\top,$$

with  $\nabla_x h$  denoting the gradient of h with respect to the elements of X and with all derivatives evaluated at  $(\mathsf{E}[X], \mathsf{E}[Y])$ . Because  $h(\mathsf{E}[X], \cdot)$  is the identity, the partial derivative of  $h$  with respect to its last argument equals 1 at  $(\mathsf{E}[X], \mathsf{E}[Y]),$  so

$$\sigma_h^2 = \sigma_Y^2 + 2\nabla_x h \Sigma_{XY} + \nabla_x h \Sigma_X \nabla_x h^\top.$$

But this is precisely the variance of

$$Y_i - b^\top (X_i - \mathsf{E}[X])$$

with  $b = -\nabla_x h(\mathsf{E}[X], \mathsf{E}[Y])$ ; see (4.12). Thus, the distribution of the nonlinear control variate estimator using  $\bar{X}$  is asymptotically the same as the distribution of an ordinary linear control variate estimator using  $\bar{X}$  and a specific vector of coefficients b. In particular, the limiting variance parameter  $\sigma_h^2$  can be no smaller than the optimal variance that would be derived from using the optimal vector  $b^*$ .

A negative reading of this result leads to the conclusion that nonlinear controls add nothing beyond what can be achieved using linear controls. A somewhat more positive and more accurate interpretation would be that whatever advantages a nonlinear control variate estimator may have must be limited to small samples. "Small" may well include all relevant sample sizes in specific applications. The delta method tells us that asymptotically only the linear part of h matters, but if h is highly nonlinear a very large sample may be required for this asymptotic conclusion to be relevant. For fixed  $n$ , each of the examples with which we opened this section may perform rather differently from a linear control.

It should also be noted that in the linear control variate estimator to which any nonlinear control variate estimator is ultimately equivalent, the coefficient b is implicitly determined by the function h. In particular, using a nonlinear control does not entail estimating this coefficient. In some cases, a nonlinear control may be effective because  $-\nabla_x h$  is close to optimal but need not be  $estimated.$ 

## 4.2 Antithetic Variates

The method of *antithetic variates* attempts to reduce variance by introducing negative dependence between pairs of replications. The method can take various forms; the most broadly applicable is based on the observation that if U is uniformly distributed over [0, 1], then  $1-U$  is too. Hence, if we generate a path using as inputs  $U_1, \ldots, U_n$ , we can generate a second path using  $1-U_1,\ldots,1-U_n$  without changing the law of the simulated process. The variables  $U_i$  and  $1-U_i$  form an antithetic pair in the sense that a large value of one is accompanied by a small value of the other. This suggests that an unusually large or small output computed from the first path may be balanced by the value computed from the antithetic path, resulting in a reduction in variance.

These observations extend to other distributions through the inverse transform method:  $F^{-1}(U)$  and  $F^{-1}(1-U)$  both have distribution F but are antithetic to each other because  $F^{-1}$  is monotone. For a distribution symmetric about the origin,  $F^{-1}(1-u)$  and  $F^{-1}(u)$  have the same magnitudes but opposite signs. In particular, in a simulation driven by independent standard normal random variables, antithetic variates can be implemented by pairing a sequence  $Z_1, Z_2, \ldots$  of i.i.d.  $N(0, 1)$  variables with the sequence  $-Z_1, -Z_2, \ldots$ of i.i.d.  $N(0,1)$  variables, whether or not they are sampled through the inverse transform method. If the  $Z_i$  are used to simulate the increments of a Brownian path, then the  $-Z_i$  simulate the increments of the reflection of the path about the origin. This again suggests that running a pair of simulations using the original path and then its reflection may result in lower variance.

To analyze this approach more precisely, suppose our objective is to estimate an expectation  $\mathsf{E}[Y]$  and that using some implementation of antithetic sampling produces a sequence of pairs of observations  $(Y_1, Y_1), (Y_2, Y_2), \ldots,$  $(Y_n, Y_n)$ . The key features of the antithetic variates method are the following:

 $\circ$  the pairs  $(Y_1, \tilde{Y}_1), (Y_2, \tilde{Y}_2), \ldots, (Y_n, \tilde{Y}_n)$  are i.i.d.;

 $\circ$  for each *i*,  $Y_i$  and  $\tilde{Y}_i$  have the same distribution, though ordinarily they are not independent.

We use  $Y$  generically to indicate a random variable with the common distribution of the  $Y_i$  and  $Y_i$ .

The antithetic variates estimator is simply the average of all  $2n$  observations,

$$\hat{Y}_{\rm AV} = \frac{1}{2n} \left( \sum_{i=1}^{n} Y_i + \sum_{i=1}^{n} \tilde{Y}_i \right) = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{Y_i + \tilde{Y}_i}{2} \right). \tag{4.27}$$

The rightmost representation in (4.27) makes it evident that  $\hat{Y}_{AV}$  is the sample mean of the  $n$  independent observations

$$\left(\frac{Y_1+\tilde{Y}_1}{2}\right), \left(\frac{Y_2+\tilde{Y}_2}{2}\right), \dots, \left(\frac{Y_n+\tilde{Y}_n}{2}\right). \tag{4.28}$$

The central limit theorem therefore applies and gives

$$\frac{\hat{Y}_{\rm AV} - \mathsf{E}[Y]}{\sigma_{\rm AV}/\sqrt{n}} \Rightarrow N(0,1)$$

with

$$\sigma_{\rm AV}^2 = \mathsf{Var}\left[\frac{Y_i + \tilde{Y}_i}{2}\right].$$

As usual, this limit in distribution continues to hold if we replace  $\sigma_{AV}$  with  $s_{\text{AV}}$ , the sample standard deviation of the *n* values in (4.28). This provides asymptotic justification for a  $1-\delta$  confidence interval of the form

$$\hat{Y}_{\rm AV} \pm z_{\delta/2} \frac{s_{\rm AV}}{\sqrt{n}},$$

where  $1 - \Phi(z_{\delta/2}) = \delta/2$ .

Under what conditions is an antithetic variates estimator to be preferred to an ordinary Monte Carlo estimator based on independent replications? To make this comparison, we assume that the computational effort required to generate a pair  $(Y_i, Y_i)$  is approximately twice the effort required to generate  $Y_i$ . In other words, we ignore any potential computational savings from, for example, flipping the signs of previously generated  $Z_1, Z_2, \ldots$  rather than generating new normal variables. This is appropriate if the computational cost of generating these inputs is a small fraction of the total cost of simulating  $Y_i$ . Under this assumption, the effort required to compute  $\hat{Y}_{AV}$  is approximately that required to compute the sample mean of  $2n$  independent replications, and it is therefore meaningful to compare the variances of these two estimators. Using antithetics reduces variance if

$$\mathsf{Var}\left[\hat{Y}_{\mathrm{AV}}\right] < \mathsf{Var}\left[\frac{1}{2n}\sum_{i=1}^{2n}Y_i\right];$$

i.e., if

4.2 Antithetic Variates 207

$$\mathsf{Var}\left[Y_i + \tilde{Y}_i\right] < 2\mathsf{Var}[Y_i].$$

The variance on the left can be written as

$$\begin{split} \mathsf{Var}\left[Y_i + \tilde{Y}_i\right] &= \mathsf{Var}[Y_i] + \mathsf{Var}[\tilde{Y}_i] + 2\mathsf{Cov}[Y_i, \tilde{Y}_i] \\ &= 2\mathsf{Var}[Y_i] + 2\mathsf{Cov}[Y_i, \tilde{Y}_i], \end{split}$$

using the fact that  $Y_i$  and  $\tilde{Y}_i$  have the same variance if they have the same distribution. Thus, the condition for antithetic sampling to reduce variance becomes

$$\mathsf{Cov}\left[Y_i, \tilde{Y}_i\right] < 0. \tag{4.29}$$

Put succinctly, this condition requires that negative dependence in the inputs (whether U and  $1-U$  or Z and  $-Z$ ) produce negative correlation between the outputs of paired replications. A simple sufficient condition ensuring this is monotonicity of the mapping from inputs to outputs defined by a simulation algorithm. To state this precisely and to give a general formulation, suppose the inputs to a simulation are independent random variables  $X_1,\ldots,X_m$ . Suppose that Y is an increasing function of these inputs and Y is a decreasing function of the inputs; then

$$\mathsf{E}[Y\bar{Y}] \le \mathsf{E}[Y]\mathsf{E}[\bar{Y}].$$

This is a special case of more general properties of *associated* random variables, in the sense of Esary, Proschan, and Walkup [113]. Observe that if  $Y = f(U_1, \ldots, U_d)$  or  $Y = f(Z_1, \ldots, Z_d)$  for some increasing function f, then  $\tilde{Y} = f(1-U_1,\ldots,1-U_d) \text{ and } \tilde{Y} = f(-Z_1,\ldots,-Z_d) \text{ are decreasing functions}$ of  $(U_1,\ldots,U_d)$  and  $(Z_1,\ldots,Z_d)$ , respectively. The requirement that the simulation map inputs to outputs monotonically is rarely satisfied exactly, but provides some qualitative insight into the scope of the method.

The antithetic pairs  $(U, 1-U)$  with  $U \sim \text{Unif}[0,1]$  and  $(Z, -Z)$  with  $Z \sim$  $N(0,1)$  share an additional relevant property: in each case, the average of the paired values is the population mean, because

$$\frac{U + (1 - U)}{2} = 1/2 \quad \text{and} \quad \frac{Z + (-Z)}{2} = 0$$

It follows that if the output Y is a linear function of inputs  $(U_1,\ldots,U_d)$  or  $(Z_1,\ldots,Z_d)$ , then antithetic sampling results in a zero-variance estimator. Of course, in the linear case simulation would be unnecessary, but this observation suggests that antithetic variates will be very effective if the mapping from inputs to outputs is close to linear.

## Variance Decomposition

Antithetic variates eliminate the variance due to the *antisymmetric* part of an integrand, in a sense we now develop. For simplicity, we restrict attention to

/

the case of standard normal inputs, but our observations apply equally well to any other distribution symmetric about the origin and apply with minor modifications to uniformly distributed inputs.

Suppose, then, that  $Y = f(Z)$  with  $Z = (Z_1, \ldots, Z_d) \sim N(0, I)$ . Define the symmetric and antisymmetric parts of  $f$ , respectively, by

$$f_0(z) = \frac{f(z) + f(-z)}{2}$$
 and  $f_1(z) = \frac{f(z) - f(-z)}{2}$ .

Clearly,  $f = f_0 + f_1$ ; moreover, this gives an orthogonal decomposition of f in the sense that  $f_0(Z)$  and  $f_1(Z)$  are uncorrelated:

$$\begin{split} \mathsf{E}[f_0(Z)f_1(Z)] &= \frac{1}{4}\mathsf{E}[f^2(Z) - f^2(-Z)] \\ &= 0 \\ &= \mathsf{E}[f_0(Z)]\mathsf{E}[f_1(Z)]. \end{split}$$

It follows that

$$\operatorname{Var}[f(Z)] = \operatorname{Var}[f_0(Z)] + \operatorname{Var}[f_1(Z)]. \tag{4.30}$$

The first term on the right is the variance of an estimate of  $E[f(Z)]$  based on an antithetic pair  $(Z, -Z)$ . Thus, antithetic sampling eliminates all variance if f is antisymmetric  $(f = f_1)$  and it eliminates no variance if f is symmetric  $(f = f_0).$ 

Fox  $[127]$  advocates the use of antithetic sampling as the first step of a more elaborate framework, in order to eliminate the variance due to the linear (or, more generally, the antisymmetric) part of  $f$ .

## Systematic Sampling

Antithetic sampling pairs a standard normal vector  $Z = (Z_1, \ldots, Z_d)$  with its reflection  $-Z = (-Z_1, \ldots, -Z_d)$ , but it is natural to consider other vectors formed by changing the signs of the components of  $Z$ . Generalizing still further leads us to consider transformations  $T: \mathbb{R}^d \to \mathbb{R}^d$  (such as multiplication by an orthogonal matrix) with the property that  $TZ \sim N(0, I)$  whenever  $Z \sim N(0, I)$ . This property implies that the iterated transformations  $T^2 Z$ ,  $T^3Z, \ldots$  will also have standard normal distributions. Suppose that  $T^k$  is the identity for some k. The usual antithetic transformation has  $k = 2$ , but by considering other rotations and reflections of  $\mathbb{R}^d$ , it is easy to construct examples with larger values of  $k$ .

Define

$$f_0(z) = \frac{1}{k} \sum_{i=1}^k f(T^i Z)$$
 and  $f_1(z) = f(z) - f_0(z)$ .

We clearly have  $\mathsf{E}[f_0(Z)] = \mathsf{E}[f(Z)].$  The estimator  $f_0(Z)$  generalizes the antithetic variates estimator; in the survey sampling literature, methods of this

type are called *systematic* sampling because after the initial random drawing of Z, the  $k-1$  subsequent points are obtained through deterministic transformations of  $Z$ .

The representation  $f(Z) = f_0(Z) + f_1(Z)$  again gives an orthogonal decomposition. To see this, first observe that

$$\begin{split} \mathsf{E}[f_0(Z)^2] &= \frac{1}{k} \sum_{i=1}^k \mathsf{E}\left[f(T^i Z) \cdot \frac{1}{k} \sum_{j=1}^k f(T^j T^i Z)\right] \\ &= \frac{1}{k} \sum_{i=1}^k \mathsf{E}\left[f(T^i Z) \cdot f_0(T^i Z)\right] \\ &= \mathsf{E}[f(Z) f_0(Z)], \end{split}$$

 $SO$ 

$$\mathsf{E}[f_0(Z)f_1(Z)] = \mathsf{E}[f_0(Z)(f(Z) - f_0(Z))] = 0.$$

Thus, (4.30) continues to hold under the new definitions of  $f_0$  and  $f_1$ . Assuming the  $f(T^i Z)$ ,  $i = 1, \ldots, k$ , require approximately equal computing times, the estimator  $f_0(Z)$  beats ordinary Monte Carlo if

$$\mathsf{Var}[f_0(Z)] < \frac{1}{k} \mathsf{Var}[f(Z)].$$

The steps leading to  $(4.29)$  generalize to the requirement

$$\sum_{j=1}^{k-1} \mathsf{Cov}[f(Z), f(T^j Z)] < 0.$$

This condition is usually at least as difficult to satisfy as the simple version  $(4.29)$  for ordinary antithetic sampling.

For a more general formulation of antithetic sampling and for historical remarks, see Hammersley and Handscomb  $[169]$ . Boyle  $[52]$  is an early application in finance. Other work on antithetic variates includes Fishman and Huang  $[122]$  and Rubinstein, Samorodnitsky, and Shaked  $[312]$ .

## 4.3 Stratified Sampling

## 4.3.1 Method and Examples

Stratified sampling refers broadly to any sampling mechanism that constrains the fraction of observations drawn from specific subsets (or  $strata$ ) of the sample space. Suppose, more specifically, that our goal is to estimate  $E[Y]$ with Y real-valued, and let  $A_1, \ldots, A_K$  be disjoint subsets of the real line for which  $P(Y \in \bigcup_i A_i) = 1$ . Then

$$\mathsf{E}[Y] = \sum_{i=1}^{K} P(Y \in A_i) \mathsf{E}[Y|Y \in A_i] = \sum_{i=1}^{K} p_i \mathsf{E}[Y|Y \in A_i] \tag{4.31}$$

with  $p_i = P(Y \in A_i)$ . In random sampling, we generate independent  $Y_1,\ldots,Y_n$  having the same distribution as Y. The fraction of these samples falling in  $A_i$  will not in general equal  $p_i$ , though it would approach  $p_i$  as the sample size  $n$  increased. In stratified sampling, we decide in advance what fraction of the samples should be drawn from each stratum  $A_i$ ; each observation drawn from  $A_i$  is constrained to have the distribution of Y conditional on  $Y \in A_i$ .

The simplest case is proportional sampling, in which we ensure that the fraction of observations drawn from stratum  $A_i$  matches the theoretical probability  $p_i = P(Y \in A_i)$ . If the total sample size is n, this entails generating  $n_i = np_i$  samples from  $A_i$ . (To simplify the discussion, we ignore rounding and assume  $np_i$  is an integer instead of writing  $\lfloor np_i \rfloor$ .) For each  $i = 1, \ldots, K$ , let  $Y_{ij}, j = 1, \ldots, n_i$  be independent draws from the conditional distribution of Y given  $Y \in A_i$ . An unbiased estimator of  $E[Y|Y \in A_i]$  is provided by the sample mean  $(Y_{i1} + \cdots + Y_{in_i})/n_i$  of observations from the *i*th stratum. It follows from (4.31) that an unbiased estimator of  $E[Y]$  is provided by

$$\hat{Y} = \sum_{i=1}^{K} p_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} Y_{ij} = \frac{1}{n} \sum_{i=1}^{K} \sum_{j=1}^{n_i} Y_{ij}.$$
 (4.32)

This estimator should be contrasted with the usual sample mean  $\bar{Y} = (Y_1 +$  $\cdots + Y_n/n$  of a random sample of size n. Compared with  $\bar{Y}$ , the stratified estimator  $\hat{Y}$  eliminates sampling variability across strata without affecting sampling variability within strata.

We generalize this formulation in two simple but important ways. First, we allow the strata to be defined in terms of a second variable  $X$ . This *stratification variable* could take values in an arbitrary set; to be concrete we assume it is  $\Re^d$ -valued and thus take the strata  $A_i$  to be disjoint subsets of  $\Re^d$  with  $P(X \in \bigcup_i A_i) = 1$ . The representation (4.31) generalizes to

$$\mathsf{E}[Y] = \sum_{i=1}^{K} P(X \in A_i) \mathsf{E}[Y | X \in A_i] = \sum_{i=1}^{K} p_i \mathsf{E}[Y | X \in A_i], \tag{4.33}$$

where now  $p_i = P(X \in A_i)$ . In some applications, Y is a function of X (for example,  $X$  may be a discrete path of asset prices and  $Y$  the discounted payoff of a derivative security), but more generally they may be dependent without either completely determining the other. To use  $(4.33)$  for stratified sampling, we need to generate pairs  $(X_{ij}, Y_{ij}), j = 1, \ldots, n_i$ , having the conditional distribution of  $(X, Y)$  given  $X \in A_i$ .

As a second extension of the method, we allow the stratum allocations  $n_1,\ldots,n_K$  to be arbitrary (while summing to n) rather than proportional to

 $p_1,\ldots,p_K$ . In this case, the first representation in (4.32) remains valid but the second does not. If we let  $q_i = n_i/n$  be the fraction of observations drawn from stratum  $i, i = 1, \ldots, K$ , we can write

$$\hat{Y} = \sum_{i=1}^{K} p_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} Y_{ij} = \frac{1}{n} \sum_{i=1}^{K} \frac{p_i}{q_i} \sum_{j=1}^{n_i} Y_{ij}.$$
(4.34)

By minimizing the variance of this estimator over the  $q_i$ , we can find an allocation rule that is at least as effective as a proportional allocation. We return to this point later in this section.

From this introduction it should be clear that the use of stratified sampling involves consideration of two issues:

- $\circ$  choosing the stratification variable X, the strata  $A_1, \ldots, A_K$ , and the allo- $\text{cation } n_1, \ldots, n_K;$
- generating samples from the distribution of  $(X, Y)$  conditional on  $X \in A_i$ .

In addressing the first issue we will see that stratified sampling is most effective when the variability of  $Y$  within each stratum is small. Solutions to the second issue are best illustrated through examples.

**Example 4.3.1** Stratifying uniforms. Perhaps the simplest application of stratified sampling stratifies the uniformly distributed random variables that drive a simulation. Partition the unit interval  $(0,1)$  into the n strata

$$A_1 = \left(0, \frac{1}{n}\right], \ A_2 = \left(\frac{1}{n}, \frac{2}{n}\right], \ \ldots, \ A_n = \left(\frac{n-1}{n}, 1\right).$$

Each of these intervals has probability  $1/n$  under the uniform distribution, so in a proportional allocation we should draw one sample from each stratum. (The sample size  $n$  and the number of strata  $K$  are equal in this example.) Let  $U_1,\ldots,U_n$  be independent and uniformly distributed between 0 and 1 and let

$$V_i = \frac{i-1}{n} + \frac{U_i}{n}, \quad i = 1, \dots, n. \tag{4.35}$$

Each  $V_i$  is uniformly distributed between  $(i-1)/n$  and  $i/n$ , which is to say that  $V_i$  has the conditional distribution of U given  $U \in A_i$  for  $U \sim \text{Unif}[0,1]$ . Thus,  $V_1, \ldots, V_n$  constitute a stratified sample from the uniform distribution. (In working with the unit interval and the subintervals  $A_i$ , we are clearly free to define these to be open or closed on the left or right; in each setting, we adopt whatever convention is most convenient.)

Suppose  $Y = f(U)$  so that  $\mathsf{E}[Y]$  is simply the integral of f over the unit interval. Then the stratified estimator

$$\hat{Y} = \frac{1}{n} \sum_{i=1}^{n} f(V_i)$$

is similar to the deterministic midpoint integration rule

$$\frac{1}{n} \sum_{i=1}^{n} f\left(\frac{2i-1}{2n}\right)$$

based on the value of f at the midpoints of the  $A_i$ . A feature of the randomization in the stratified estimator is that it makes  $\hat{Y}$  unbiased.

This example easily generalizes to partitions of  $(0,1)$  into intervals of unequal lengths. If  $A_i = (a_i, b_i]$ , then the conditional distribution of U given  $U \in A_i$  is uniform between  $a_i$  and  $b_i$ ; we can sample from this conditional distribution by setting  $V = a_i + U(b_i - a_i)$ .  $\Box$ 

**Example 4.3.2** Stratifying nonuniform distributions. Let  $F$  be a cumulative distribution function on the real line and let

$$F^{-1}(u) = \inf\{x : F(x) \le u\}$$

denote its inverse as defined in Section 2.2.1. Given probabilities  $p_1, \ldots, p_K$ summing to 1, define  $a_0 = -\infty$ ,

$$a_1 = F^{-1}(p_1), \ a_2 = F^{-1}(p_1 + p_2), \ \ldots, \ a_K = F^{-1}(p_1 + \cdots + p_K) = F^{-1}(1).$$

 $\text{Define strata}$ 

$$A_1 = (a_0, a_1], A_2 = (a_1, a_2], \ldots, A_K = (a_{K-1}, a_K]$$

or with  $A_K = (a_{K-1}, a_K)$  if  $a_K = \infty$ . By construction, each stratum  $A_i$  has probability  $p_i$  under  $F$ ; for if  $Y$  has distribution  $F$ , then

$$P(Y \in A_i) = F(a_i) - F(a_{i-1}) = p_i.$$

Thus, defining strata for  $F$  with specified probabilities is straightforward, provided one can find the quantiles  $a_i$ . Figure 4.4 displays ten equiprobable  $(p_i = 1/K)$  strata for the standard normal distribution.

To use the sets  $A_1, \ldots, A_K$  for stratified sampling, we need to be able to generate samples of Y conditional on  $Y \in A_i$ . As demonstrated in Example 2.2.5, this is easy using the inverse transform method. If  $U \sim \text{Unif}[0,1]$ , then

$$V = a_{i-1} + U(a_i - a_{i-1})$$

is uniformly distributed between  $a_{i-1}$  and  $a_i$  and then  $F^{-1}(V)$  has the distribution of Y conditional on  $Y \in A_i$ .

Figure 4.5 illustrates the difference between stratified and random sampling from the standard normal distribution. The left panel is a histogram of 500 observations, five from each of 100 equiprobable strata; the right panel is a histogram of 500 independent draws from the normal distribution. Stratification clearly produces a better approximation to the underlying distribution.

![](_page_28_Figure_1.jpeg)

Fig. 4.4. A partition of the real line into ten intervals of equal probability under the standard normal distribution. The area under the normal density over each interval is  $1/10$ .

How might we use stratified samples from the normal distribution in simulating paths of a stochastic process? It would not be legitimate to use one value from each of 100 strata to generate 100 steps of a single Brownian path: the increments of Brownian motion are independent but the stratified values are not, and ignoring this dependence would produce nonsensical results. In contrast, we could validly use the stratified values to generate the first increment of 100 replications of a single Brownian path (or the terminal values of the paths, as explained in Section  $4.3.2$ ). In short, in using stratified sampling or any other variance reduction technique, we are free to introduce dependence *across* replications but not *within* replications.  $\Box$ 

![](_page_28_Figure_4.jpeg)

Fig. 4.5. Comparison of stratified sample (left) and random sample (right). The stratified sample uses 100 equiprobable strata with five samples from each stratum; the random sample consists of 500 independent draws from the normal distribution. Both histograms use  $25$  bins.

**Example 4.3.3** Stratification through acceptance-rejection. A crude but almost universally applicable method for generating samples conditional on a stratum generates unconditional samples and keeps those that fall in the target set. This is the method described in Example 2.2.8 for conditional sampling, and may be viewed as a form of acceptance-rejection in which the acceptance probability is always  $0$  or  $1$ .

To describe this in more detail, we use the notation of  $(4.33)$ . Our goal is to generate samples of the pair  $(X,Y)$  using strata  $A_1,\ldots,A_K$  for X, with  $n_i$  samples to be generated conditional on  $X \in A_i, i = 1, \ldots, K$ . Given a mechanism for generating unconditional samples from the distribution of  $(X,Y)$ , we can repeatedly generate such samples until we have produced  $n_i$ samples with  $X \in A_i$  for each  $i = 1, \ldots, K$ ; any extra samples generated from a stratum are simply rejected.

The efficiency of this method depends on the computational cost of generating pairs  $(X,Y)$  and determining the stratum in which X falls. It also depends on the stratum probabilities: if  $P(X \in A_i)$  is small, a large number of candidates may be required to produce  $n_i$  samples from  $A_i$ . These computational costs must be balanced against the reduction in variance achieved through stratification. Glasserman, Heidelberger, and Shahabuddin [143] analyze the overhead from rejected samples in this method based on a Poisson approximation to the arrival of samples from each stratum.  $\Box$ 

**Example 4.3.4** Stratifying the unit hypercube. The methods described in  $Ex$ amples  $4.3.1$  and  $4.3.2$  extend, in principle, to multiple dimensions. Using the inverse transform method, a vector  $(X_1, \ldots, X_d)$  of independent random variables can be represented as  $(F_1^{-1}(U_1), \ldots, F_d^{-1}(U_d))$  with  $F_i$  the distribution of  $X_i$  and  $U_1, \ldots, U_d$  independent and uniform over  $[0, 1)$ . In this sense, it suffices to consider the uniform distribution over the  $d$ -dimensional hypercube  $[0,1)^d$ . (In the case of dependent  $X_1,\ldots,X_d$ , replace  $F_i$  with the conditional distribution of  $X_i$  given  $X_1, \ldots, X_{i-1}$ .) In stratifying the unit hypercube with respect to the uniform distribution, it is convenient to take the strata to be products of intervals because the probability of such a set is easily calculated and because it is easy to sample uniformly from such a set by applying a transformation like  $(4.35)$  to each coordinate.

Suppose, for example, that we stratify the  $j$ th coordinate of the hypercube into  $K_j$  intervals of equal length. Each stratum of the hypercube has the form

$$\prod_{j=1}^d \left[\frac{i_j-1}{K_j}, \frac{i_j}{K_j}\right), \quad i_j \in \{1, \ldots, K_j\}$$

and has probability  $1/(K_1 \cdots K_d)$ . To generate a vector V uniformly distributed over this set, generate  $U_1, \ldots, U_d$  independently from Unif[0,1) and define the  $j$ th coordinate of  $V$  to be

$$V_j = \frac{i_j - 1 + U_j}{K_i}, \quad j = 1, \dots, d. \tag{4.36}$$

In this example, the total number of strata is  $K_1 \cdots K_d$ . Generating at least one point from each stratum therefore requires a sample size at least this large. Unless the  $K_i$  are quite small (in which case stratification may provide little benefit), this is likely to be prohibitive for  $d$  larger than 5, say. In Section 4.4 and Chapter 5, we will see methods related to stratified sampling that are better suited to higher dimensions.  $\Box$ 

## Output Analysis

We now turn to the problem of interval estimation for  $\mu \stackrel{\triangle}{=} \mathsf{E}[Y]$  using stratified sampling. As in (4.33), let  $A_1, \ldots, A_K$  denote strata for a stratification variable X and let  $Y_{ij}$  have the distribution of Y conditional on  $X \in A_i$ . For  $i = 1, \ldots, K$ , let

$$\mu_i = \mathsf{E}[Y_{ij}] = \mathsf{E}[Y|X \in A_i] \tag{4.37}$$

$$\sigma_i^2 = \text{Var}[Y_{ij}] = \text{Var}[Y|X \in A_i]. \tag{4.38}$$

Let  $p_i = P(X \in A_i), i = 1, \ldots, K$ , denote the stratum probabilities; we require these to be strictly positive and to sum to 1. Fix an allocation  $n_1, \ldots, n_K$ with all  $n_i \geq 1$  and  $n_1 + \cdots + n_K = n$ . Let  $q_i = n_i/n$  denote the fraction of samples allocated to the  $i$ th stratum. For any such allocation the estimator  $Y$  in (4.33) is unbiased because

$$\mathsf{E}[\hat{Y}] = \sum_{i=1}^K p_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} \mathsf{E}[Y_{ij}] = \sum_{i=1}^K p_i \mu_i = \mu.$$

The variance of  $\hat{Y}$  is given by

$$\mathsf{Var}[\hat{Y}] = \sum_{i=1}^K p_i^2 \mathsf{Var}\left[\frac{1}{n_i} \sum_{j=1}^{n_i} Y_{ij}\right] = \sum_{i=1}^K p_i^2 \frac{\sigma_i^2}{n_i} = \frac{\sigma^2(q)}{n},$$

with

$$\sigma^2(q) = \sum_{i=1}^K \frac{p_i^2}{q_i} \sigma_i^2.$$
 (4.39)

For each stratum  $A_i$ , the samples  $Y_{i1}, Y_{i2}, \ldots$  are i.i.d. with mean  $\mu_i$  and variance  $\sigma_i^2$  and thus satisfy

$$\frac{1}{\sqrt{\lfloor nq_i \rfloor}} \sum_{j=1}^{\lfloor nq_i \rfloor} (Y_{ij} - \mu_i) \Rightarrow N(0, \sigma_j^2)$$

as  $n \to \infty$  with  $q_1, \ldots, q_K$  fixed. The centered and scaled estimator  $\sqrt{n}(\hat{Y} - \mu)$  $\text{can be written as}$ 

- Martin States - Alberta

$$\sqrt{n}(\hat{Y} - \mu) = \sqrt{n} \sum_{i=1}^{K} p_i \left( \frac{1}{\lfloor nq_i \rfloor} \sum_{j=1}^{\lfloor nq_i \rfloor} (Y_{ij} - \mu_i) \right)$$
$$\approx \sum_{i=1}^{K} \frac{p_i}{\sqrt{q_i}} \left( \frac{1}{\sqrt{\lfloor nq_i \rfloor}} \sum_{j=1}^{\lfloor nq_i \rfloor} (Y_{ij} - \mu_i) \right),$$

the approximation holding in the sense that the ratio of the two expressions approaches 1 as  $n \to \infty$ . This shows that  $\sqrt{n}(\hat{Y} - \mu)$  is asymptotically a linear combination (with coefficients  $p_i/\sqrt{q_i}$ ) of independent normal random variables (with mean 0 and variances  $\sigma_i^2$ ). It follows that

$$\sqrt{n}(\hat{Y} - \mu) \Rightarrow N(0, \sigma^2(q))$$

with  $\sigma^2(q)$  as defined in (4.39). This limit holds as the sample size n increases with the number of strata  $K$  held fixed.

A consequence of this central limit theorem for  $\hat{Y}$  is the asymptotic validity of

$$\hat{Y} \pm z_{\delta/2} \frac{\sigma(q)}{\sqrt{n}} \tag{4.40}$$

as a  $1 - \delta$  confidence interval for  $\mu$ , with  $z_{\delta/2} = \Phi^{-1}(1 - \delta/2)$ . In practice,  $\sigma^2(q)$  is typically unknown but can be consistently estimated using

$$s^{2}(q) = \sum_{i=1}^{K} \frac{p_{i}^{2}}{q_{i}} s_{i}^{2},$$

where  $s_i^2$  is the sample standard deviation of  $Y_{i1}, \ldots, Y_{in_i}$ .

Alternatively, one can estimate  $\sigma^2(q)$  through independent replications of  $\hat{Y}$ . More precisely, suppose the sample size n can be expressed as  $mk$  with m and k integers and  $m \geq 2$ . Suppose  $k_i = q_i k$  is an integer for all  $i = 1, \ldots, K$ and note that  $n_i = mk_i$ . Then  $\hat{Y}$  is the average of m independent stratified estimators  $\hat{Y}_1, \ldots, \hat{Y}_m$ , each of which allocates a fraction  $q_i$  of observations to stratum *i* and has a total sample size of *k*. Each  $\hat{Y}_j$  thus has variance  $\sigma^2(q)/k$ ; because  $\hat{Y}$  is the average of the  $\hat{Y}_1,\ldots,\hat{Y}_m$ , an asymptotically (as  $m\to\infty$ ) valid confidence interval for  $\mu$  is provided by

$$\hat{Y} \pm z_{\delta/2} \frac{\sigma(q)/\sqrt{k}}{\sqrt{m}}.\tag{4.41}$$

This reduces to (4.40), but  $\sigma(q)/\sqrt{k}$  can now be consistently estimated using the sample standard deviation of  $\hat{Y}_1, \ldots, \hat{Y}_m$ . This is usually more convenient than estimating all the stratum variances  $\sigma_i^2$ ,  $i = 1, \ldots, K$ .

In this formulation, each  $\hat{Y}_j$  may be thought of as a batch with sample size k and the original estimator  $\hat{Y}$  as the sample mean of m independent batches. Given a total sample size  $n$ , is it preferable to have at least m observations from each stratum, as in this setting, or to increase the number of strata so that only one observation is drawn from each? A larger  $m$  should improve our estimate of  $\sigma(q)$  and the accuracy of the normal approximation implicit in the confidence intervals above. However, we will see below (cf.  $(4.46)$ ) that taking finer strata reduces variance. Thus, as is often the case, we face a tradeoff between reducing variance and accurately measuring variance.

## Optimal Allocation

In the case of a proportional allocation of samples to strata,  $q_i = p_i$  and the variance parameter  $\sigma^2(q)$  simplifies to

$$\sum_{i=1}^{K} \frac{p_i^2}{q_i} \sigma_i^2 = \sum_{i=1}^{K} p_i \sigma_i^2.$$
 (4.42)

To compare this to the variance without stratification, observe that

$$\mathsf{E}[Y^2] = \sum_{i=1}^K p_i \mathsf{E}[Y^2 | X \in A_i] = \sum_{i=1}^K p_i (\sigma_i^2 + \mu_i^2),$$

so using  $\mu = \sum_{i=1}^{K} p_i \mu_i$  we get

$$\text{Var}[Y] = \mathsf{E}[Y^2] - \mu^2 = \sum_{i=1}^K p_i \sigma_i^2 + \sum_{i=1}^K p_i \mu_i^2 - \left(\sum_{i=1}^K p_i \mu_i\right)^2. \tag{4.43}$$

By Jensen's inequality,

$$\sum_{i=1}^K p_i \mu_i^2 \ge \left(\sum_{i=1}^K p_i \mu_i\right)^2$$

with strict inequality unless all  $\mu_i$  are equal. Thus, comparing (4.42) and  $(4.43)$ , we conclude that stratified sampling with a proportional allocation can only decrease variance.

Optimizing the allocation can produce further variance reduction. Minimizing  $\sigma^2(q)$  subject to the constraint that  $(q_1,\ldots,q_K)$  be a probability vector yields the optimal allocation

$$q_i^* = \frac{p_i \sigma_i}{\sum_{\ell=1}^K p_\ell \sigma_\ell}, \quad i = 1, \dots, K.$$

In other words, the optimal allocation for each stratum is proportional to the product of the stratum probability and the stratum standard deviation. The optimal variance is thus

$$\sigma^{2}(q^{*}) = \sum_{i=1}^{K} \frac{p_{i}^{2}}{q_{i}^{*}} \sigma_{i}^{2} = \left(\sum_{i=1}^{K} p_{i} \sigma_{i}\right)^{2}.$$

Comparison with  $(4.42)$  indicates that the additional reduction in variance from optimizing the allocation is greatest when the stratum standard deviations vary widely.

In practice, the  $\sigma_i$  are rarely known so the optimal fractions  $q_i^*$  are not directly applicable. Nevertheless, it is often practical to use pilot runs to get estimates of the  $\sigma_i$  and thus of the  $q_i^*$ . The estimated optimal fractions can then be used to allocate samples to strata in a second (typically larger) set of runs.

In taking the optimal allocation to be the one that minimizes variance, we are implicitly assuming that the computational effort required to generate samples is the same across strata. But this assumption is not always appropriate. For example, in sampling from strata through acceptance-rejection as described in Example 4.3.3, the expected time required to sample from  $A_i$  is proportional to  $1/p_i$ . A more complete analysis should therefore account for differences in computational costs across strata.

Suppose, then, that  $\tau_i$  denotes the expected computing time required to sample  $(X,Y)$  conditional on  $X \in A_i$  and let s denote the total computing budget. Let  $Y(s)$  denote the stratified estimator produced with a budget s, assuming the fraction of samples allocated to stratum i is  $q_i$ . (This is asymptotically equivalent to assuming the fraction of the computational budget allocated to stratum i is proportional to  $q_i \tau_i$ .) Arguing much as in Section 1.1.3, we find that

$$\sqrt{s}[\hat{Y}(s) - \mu] \Rightarrow N\left(0, \sigma^2(q, \tau)\right),$$

with

$$\sigma^2(q,\tau) = \left(\sum_{i=1}^K \frac{p_i^2 \sigma_i^2}{q_i}\right) \left(\sum_{i=1}^K q_i \tau_i\right).$$

By minimizing this work-normalized variance parameter we find that the optimal allocation is

$$q_i^* = \frac{p_i \sigma_i / \sqrt{\tau_i}}{\sum_{\ell=1}^K p_\ell \sigma_\ell / \sqrt{\tau_\ell}},$$

which now accounts for differences in computational costs across strata. Like the  $\sigma_i$ , the  $\tau_i$  can be estimated through pilot runs.

## Variance Decomposition

The preceding discussion considers the allocation of samples to given strata. In order to consider the question of how strata should be selected in the first place, we now examine what part of the variance of  $Y$  is removed through stratification of  $X$ .

As before, let  $A_1, \ldots, A_K$  be strata for X. Let  $\eta \equiv \eta(X) \in \{1, \ldots, K\}$ denote the index of the stratum containing X, so that  $X \in A_n$ . We can  $always write$ 

$$Y = \mathsf{E}[Y|\eta] + \epsilon \tag{4.44}$$

simply by defining the residual  $\epsilon$  so that equality holds. It is immediate that  $\mathsf{E}[\epsilon|\eta] = 0$  and that  $\epsilon$  is uncorrelated with  $\mathsf{E}[Y|\eta]$  because

$$\mathsf{E}[\epsilon\left(\mathsf{E}[Y|\eta] - \mathsf{E}[Y]\right)] = 0,$$

as can be seen by first conditioning on  $\eta$ . Because (4.44) decomposes Y into the sum of uncorrelated terms, we have

$$\mathsf{Var}[Y] = \mathsf{Var}[\mathsf{E}[Y|\eta]] + \mathsf{Var}[\epsilon].$$

We will see that stratified sampling with proportional allocation eliminates the first term on the right, leaving only the variance of the residual term and thus guaranteeing a variance reduction.

The residual variance is  $E[\epsilon^2]$  because  $E[\epsilon] = 0$ . Also,

$$\mathsf{E}[\epsilon^2|\eta] = \mathsf{E}\left[ (Y - \mathsf{E}[Y|\eta])^2|\eta \right] = \mathsf{Var}[Y|\eta].$$

We thus arrive at the familiar decomposition

2.

$$\mathsf{Var}[Y] = \mathsf{Var}[\mathsf{E}[Y|\eta]] + \mathsf{E}\left[\mathsf{Var}[Y|\eta]\right].\tag{4.45}$$

The conditional expectation of Y given  $\eta = i$  is  $\mu_i$ , and the probability that  $\eta = i$  is  $p_i$ . The first term on the right side of (4.45) is thus

$$\mathsf{Var}[\mathsf{E}[Y|\eta]] = \sum_{i=1}^K p_i \mu_i^2 - \left(\sum_{i=1}^K p_i \mu_i\right)^2.$$

Comparing this with  $(4.43)$ , we conclude from  $(4.44)$  and  $(4.45)$  that

$$\mathsf{Var}[\epsilon] = \mathsf{E}\left[\mathsf{Var}[Y|\eta]\right] = \sum_{i=1}^{K} p_i \sigma_i^2,$$

which is precisely the variance parameter in  $(4.42)$  for stratified sampling with proportional allocation. This confirms that the variance parameter of the stratified estimator is the variance of the residual of  $Y$  after conditioning on  $\eta$ .

Consider now the effect of alternative choices of strata. The total variance  $\text{Var}[Y]$  in (4.45) is constant, so making the residual variance small is equivalent to making  $\mathsf{Var}[\mathsf{E}[Y|\eta]]$  large — i.e., to making  $\mathsf{Var}[\mu_{\eta}]$  large. This indicates that we should try to choose strata to achieve a high degree of variability across the stratum means  $\mu_1, \ldots, \mu_K$  and low variability within each stratum. Indeed,

from  $(4.45)$  we find that stratification eliminates inter-stratum variability, leaving only intra-stratum variability.

Another consequence of  $(4.45)$  is that further stratification results in further variance reduction. More precisely, suppose the partition  $\{A_1,\ldots,A_{\tilde{K}}\}$ refines the partition  $\{A_1,\ldots,A_K\}$ , in the sense that the stratum index  $\tilde{\eta}$  of the new partition completely determines  $\eta$ . Then  $\mathsf{E}[Y|\eta] = \mathsf{E}[\mathsf{E}[Y|\tilde{\eta}]|\eta]$  and Jensen's inequality yields

$$\mathsf{Var}[\mathsf{E}[Y|\eta]] \le \mathsf{Var}[\mathsf{E}[Y|\tilde{\eta}]],\tag{4.46}$$

from which it follows that the residual variance from the refined strata cannot exceed the residual variance from the original strata.

The decomposition  $(4.44)$  invites a comparison between stratified sampling and control variates. Consider the case of real-valued  $X$ . Using the method of Example 4.3.2, we can in principle stratify  $X$  using an arbitrarily large number of equiprobable intervals. As we refine the stratification, it is reasonable to expect that  $\mathsf{E}[Y|\eta]$  will approach  $\mathsf{E}[Y|X]$ . (For a specific result of this type see Lemma 4.1 of Glasserman, Heidelberger, and Shahabuddin [139].) The  $\text{decomposition (4.44) becomes}$ 

$$Y = \mathsf{E}[Y|X] + \epsilon = g(X) + \epsilon,$$

with  $q(x) = \mathsf{E}[Y|X=x]$ . If q is linear, then the variance removed through (infinitely fine) stratification of  $X$  is precisely the same as the variance that would be removed using  $X$  as a control variate. But in the general case, using  $X$  as a control variate would remove only the variance associated with the linear part of g near  $E[X]$ ; see the discussion in Section 4.1.4. In contrast, infinitely fine stratification of X removes all the variance of  $g(X)$  leaving only the variance of the residual  $\epsilon$ . In this sense, using X as a stratification variable is more effective than using it as a control variate. However, it should also be noted that using X as a control requires knowledge only of  $E[X]$  and not the full distribution of  $X$ ; moreover, it is often easier to use  $X$  as a control than to generate samples from the conditional law of  $(X,Y)$  given the stratum containing  $X$ .

## 4.3.2 Applications

This section illustrates the application of stratified sampling in settings somewhat more complex than those in Examples  $4.3.1-4.3.4$ . As noted in Exam- $\text{ple } 4.3.4$ , fully stratifying a random vector becomes infeasible in high dimensions. We therefore focus primarily on methods that stratify a scalar projection in a multidimensional setting. This can be effective in valuing a derivative security if its discounted payoff is highly variable along the selected projection.

## Terminal Stratification

In the pricing of options, the most important feature of the path of an underlying asset is often its value at the option expiration; much of the variability in the option's payoff can potentially be eliminated by stratifying the terminal value. As a step in this direction, we detail the stratification of Brownian motion along its terminal value. In the special case of an asset described by geometric Brownian motion with constant volatility, this is equivalent to stratifying the terminal value of the asset price itself.

Suppose, then, that we need to generate a discrete Brownian path  $W(t_1)$ ,  $\ldots$ ,  $W(t_m)$  and that we want to stratify the terminal value  $W(t_m)$ . We can accomplish this through a variant of the Brownian bridge construction of Brownian motion presented in Section 3.1. Using the inverse transform method as in Example 4.3.2 we can stratify  $W(t_m)$ , and then conditional on each value of  $W(t_m)$  we can generate the intermediate values  $W(t_1), \ldots, W(t_{m-1})$ .

Consider, in particular, the case of  $K$  equiprobable strata and a proportional allocation. Let  $U_1,\ldots,U_K$  be independent Unif[0,1] random variables  $\text{and set}$ 

$$V_i = \frac{i-1}{K} + \frac{U_i}{K}, \quad i = 1, \dots, K.$$

Then  $\Phi^{-1}(V_1), \ldots, \Phi^{-1}(V_K)$  form a stratified sample from the standard normal distribution and  $\sqrt{t_m}\Phi^{-1}(V_1), \ldots, \sqrt{t_m}\Phi^{-1}(V_m)$  form a stratified sample from  $N(0,t_m)$ , the distribution of  $W(t_m)$ . To fill in the path leading to each  $W(t_m)$ , we recall from Section 3.1 that the conditional distribution of  $W(t_j)$ given  $W(t_{i-1})$  and  $W(t_m)$  is

$$N\left(\frac{t_m-t_j}{t_m-t_{j-1}}W(t_{j-1})+\frac{t_j-t_{j-1}}{t_m-t_{j-1}}W(t_m),\frac{(t_m-t_j)(t_j-t_{j-1})}{t_m-t_{j-1}}\right),\,$$

with  $t_0 = 0$  and  $W(0) = 0$ .

The following algorithm implements this idea to generate  $K$  Brownian paths stratified along  $W(t_m)$ :

$$\begin{array}{l} \text{for } i = 1, \dots, K \\ \text{generate } U \sim \text{Unif}[0,1] \\ V \leftarrow (i-1+U)/K \\ W(t_m) \leftarrow \sqrt{t_m} \Phi^{-1}(V) \\ \text{for } j = 1, \dots, m-1 \\ \text{ generate } Z \sim N(0,1) \\ W(t_j) \leftarrow \frac{t_m - t_j}{t_m - t_{j-1}} W(t_{j-1}) + \frac{t_j - t_{j-1}}{t_m - t_{j-1}} W(t_m) + \sqrt{\frac{(t_m - t_j)(t_j - t_{j-1})}{t_m - t_{j-1}}} Z \end{array}$$

Figure 4.6 illustrates the construction. Of the  $K = 10$  paths generated by this algorithm, exactly one terminates in each of the  $K = 10$  strata defined for  $W(t_m)$ , here with  $t_m = 1$ .

If the underlying asset price  $S(t)$  is modeled by geometric Brownian motion, then driving the simulation of  $S$  with these Brownian paths stratifies the terminal asset price  $S(t_m)$ ; this is a consequence of the fact that  $S(t_m)$  is a monotone transformation of  $W(t_m)$ . In valuing an option on S, rather than constructing equiprobable strata over all possible terminal values, we may combine all values of  $S(t_m)$  that result in zero payoff into a single stratum

![](_page_37_Figure_1.jpeg)

Fig. 4.6. Simulation of  $K$  Brownian paths using terminal stratification. One path reaches each of the  $K$  strata. The strata are equiprobable under the distribution of  $W(1)$ .

and create a finer stratification of terminal values that potentially produce a nonzero payoff. (The payoff will not be completely determined by  $S(t_m)$  if it is path-dependent.)

As an example of how a similar construction can be used in a more complex example, consider the dynamics of a forward LIBOR rate  $L_n$  as in (4.6). Consider a single-factor model (so that  $W$  is a scalar Brownian motion) with deterministic but time-varying volatility  $\sigma_n \equiv \sigma$ . Without the drift term in  $(4.6)$ , the terminal value  $L_n(t_m)$  would be determined by

$$\int_0^{t_m} \sigma(u) \, dW(u)$$

rather than  $W(t_m)$ , so we may prefer to stratify this integral instead. If  $\sigma$  is constant over each interval  $[t_i, t_{i+1})$ , this integral simplifies to

$$W(t_m)\sigma(t_{m-1}) + \sum_{i=1}^{m-1} W(t_i)[\sigma(t_{i-1}) - \sigma(t_i)]. \tag{4.47}$$

Similarly, for some path-dependent options one may want to stratify the av- $\text{erage}$ 

$$\frac{1}{m} \sum_{i=1}^{m} W(t_i). \tag{4.48}$$

In both cases, the stratification variable is a linear combination of the  $W(t_i)$ and is thus a special case of the general problem treated next.

## Stratifying a Linear Projection

Generating  $(W(t_1), \ldots, W(t_m))$  stratified along  $W(t_m)$  or (4.47) or (4.48) are all special cases of the problem of generating a multivariate normal random vector stratified along some projection. We now turn to this general formulation of the problem.

Suppose, then, that  $\xi \sim N(\mu, \Sigma)$  in  $\Re^d$  and that we want to generate  $\xi$  with  $X \equiv v^{\top} \xi$  stratified for some fixed vector  $v \in \mathbb{R}^d$ . Suppose the  $d \times d$  matrix  $\Sigma$ has full rank. We may take  $\mu$  to be the zero vector because stratifying  $v^{\top}\xi$  is equivalent to stratifying  $v^{\top}(\xi-\mu)$  since  $v^{\top}\mu$  is a constant. Also, stratifying X is equivalent to stratifying any multiple of X; by scaling v if necessary, we may therefore assume that  $v^{\top} \Sigma v = 1$ . Thus,

$$X = v^{\top} \xi \sim N(0, v^{\top} \Sigma v) = N(0, 1),$$

so we know how to stratify  $X$  using the method in Example 4.3.1.

The next step is to generate  $\xi$  conditional on the value of X. First observe that  $\xi$  and X are jointly normal with

$$\begin{pmatrix} \xi \\ X \end{pmatrix} \sim N \left( 0, \begin{pmatrix} \Sigma & \Sigma v \\ v^\top \Sigma & v^\top \Sigma v \end{pmatrix} \right).$$

Using the Conditioning Formula  $(2.25)$ , we find that

$$(\xi|X=x) \sim N\left(\frac{\Sigma v}{v^{\top}\Sigma v}x, \Sigma - \frac{\Sigma vv^{\top}\Sigma}{v^{\top}\Sigma v}\right) = N\left(\Sigma vx, \Sigma - \Sigma vv^{\top}\Sigma\right).$$

Observe that the conditional covariance matrix does not depend on  $x$ ; this is important because it means that only a single factorization is required for the conditional sampling. Let A be any matrix for which  $AA^{\top} = \Sigma$  (such as the one found by Cholesky factorization) and observe that

$$\begin{aligned} (A - \Sigma vv^\top A)(A - \Sigma vv^\top A)^\top \\ &= AA^\top - AA^\top vv^\top \Sigma - \Sigma vv^\top AA^\top + \Sigma vv^\top \Sigma vv^\top \Sigma \\ &= \Sigma - \Sigma vv^\top \Sigma, \end{aligned}$$

again using the fact that  $v^{\top} \Sigma v = 1$ . Thus, we can use the matrix  $A - \Sigma v v^{\top} A$ to sample from the conditional distribution of  $\xi$  given X.

The following algorithm generates K samples from  $N(0,\Sigma)$  stratified along the direction determined by  $v$ :

$$\begin{array}{l} \text{for } i = 1, \dots, K \\ \text{generate } U \sim \text{Unif}[0,1] \\ V \leftarrow (i-1+U)/K \\ X \leftarrow \Phi^{-1}(V) \\ \text{ generate } Z \sim N(0, I) \text{ in } \Re^d \\ \xi \leftarrow \Sigma v X + (A - \Sigma vv^\top A) Z \end{array}$$

By construction, of the  $K$  values of  $X$  generated by this algorithm, exactly one will fall in each of  $K$  equiprobable strata for the standard normal distribution. But observe that under this construction,

$$v^{\top}\xi = v^{\top}\Sigma vX + v^{\top}(A - \Sigma vv^{\top}A)Z = X.$$

Thus, of the K values of  $\xi$  generated, exactly one has a projection  $v^{\top}\xi$  falling into each of  $K$  equiprobable strata. In this sense, the algorithm generates samples from  $N(0,\Sigma)$  stratified along the direction determined by v.

To apply this method to generate a Brownian path with the integral in  $(4.47)$  stratified, take  $\Sigma$  to be the covariance matrix of the Brownian path  $(\Sigma_{ij} = \min(t_i, t_j), \text{ as in (3.6)})$  and

$$v \propto (\sigma(0) - \sigma(1), \sigma(1) - \sigma(2), \ldots, \sigma(m-2) - \sigma(m-1), \sigma(m-1))^{\top},$$

normalized so that  $v^{\top} \Sigma v = 1$ . To generate the path with its average (4.48) stratified, take  $v$  to be the vector with all entries equal to the square root of the sum of the entries of  $\Sigma$ . Yet another strategy for choosing stratification directions is to use the principal components of  $\Sigma$  (cf. Section 2.3.3).

Further simplification is possible in stratifying a sample from the *standard* multivariate normal distribution  $N(0, I)$ . In this case, the construction above becomes

$$\xi = vX + (I - vv^{\top})Z, \quad X \sim N(0,1), \quad Z \sim N(0,I),$$

with v now normalized so that  $v^{\top}v = 1$ . Since  $X = v^{\top}\xi$ , by stratifying X we stratify the projection of  $\xi$  onto v. The special feature of this setting is that the matrix-vector product  $(I - vv^\top)Z$  can be evaluated as  $Z - v(v^\top Z)$ , which requires  $O(d)$  operations rather than  $O(d^2)$ .

This construction extends easily to allow stratification along multiple directions simultaneously. Let B denote a  $d \times m$  matrix,  $m < d$ , whose columns represent the stratification directions. Suppose  $B$  has been normalized so that  $B^{\top} \Sigma B = I$ . If  $\Sigma$  itself is the identity matrix, this says that the m columns of B form a set of orthonormal vectors in  $\mathbb{R}^d$ . Where we previously stratified the scalar projection  $X = v^{\top} \xi$ , we now stratify the *m*-vector  $X = B^{\top} \xi$ , noting that  $X \sim N(0, I)$ . For this, we first stratify the *m*-dimensional hypercube as in Example 4.3.4 and then set  $X_{j} = \Phi^{-1}(V_{j}), j = 1, ..., m$ , with  $(V_{1}, ..., V_{m})$ sampled from a stratum of the hypercube as in  $(4.36)$ . This samples X from the  $m$ -dimensional standard normal distribution with each of its components stratified. We then set

$$\xi = \Sigma BX + (A - \Sigma BB^{\top} A)Z, \quad Z \sim N(0, I),$$

for any  $d \times d$  matrix A satisfying  $AA^{\top} = \Sigma$ . The projection  $B^{\top}\xi$  of  $\xi$  onto the columns of  $B$  returns  $X$  and is stratified by construction.

To illustrate this method, we apply it to the LIBOR market model discussed in Section  $3.7$ , using the notation and terminology of that section. We

use accrual intervals of length  $\delta = 1/2$  and set all forward rates initially equal to  $6\%$ . We consider a single-factor model (i.e., one driven by a scalar Brownian motion) with a piecewise constant stationary volatility, meaning that  $\sigma_n(t)$ depends on n and t only through  $n - \eta(t)$ , the number of maturity dates remaining until  $T_n$ . We consider a model in which volatility decreases linearly from  $0.20$  to  $0.10$  over a 20-year horizon, and a model in which all forward rate volatilities are  $0.15$ .

Our simulation uses a time increment equal to  $\delta$ , throughout which volatilities are constant. We therefore write

$$\int_0^{T_n} \sigma_n(t) dW(t) = \sqrt{\delta} \sum_{i=1}^n \sigma_n(T_{i-1}) Z_i, \qquad (4.49)$$

with  $Z_1, Z_2, \ldots$  independent  $N(0,1)$  variables. This suggests using the vector  $(\sigma_n(0), \sigma_n(T_1), \ldots, \sigma_n(T_{n-1}))$  as the stratification direction in sampling  $(Z_1,\ldots,Z_n)$  from the standard normal distribution in  $\Re^n$ .

Table 4.2 reports estimated variance reduction ratios for pricing various options in this model. Each entry in the table gives an estimate of the ratio of the variance using ordinary Monte Carlo to the variance using a stratified sample of equal size. The results are based on 40 strata (or simply 40 independent samples for ordinary Monte Carlo); the estimated ratios are based  $1000$ replications, each replication using a sample size of 40. The 1000 replications merely serve to make the ratio estimates reliable; the ratios themselves should be interpreted as the variance reduction achieved by using 40 strata.

The results shown are for a caplet with a maturity of 20 years, a caplet with a maturity of 5 years, bonds with maturities  $20.5$  and  $5.5$  years, and a swaption maturing in 5 years to enter into a 5-year, fixed-for-floating interest rate swap. The options are all at-the-money. The results are based on simulation in the spot measure using the log-Euler scheme in  $(3.120)$ , except for the last row which applies to the forward measure for maturity  $20.5$ . In each case, the stratification direction is based on the relevant portion of the volatility vector  $-$  forty components for a 20-year simulation, ten components for a 5-year simulation. (Discounting a payment to be received at  $T_{n+1}$  requires simulating to  $T_n$ .)

The results in the table indicate that the variance reduction achieved varies widely but can be quite substantial. With notable exceptions, we generally see greater variance reduction at shorter maturities, at least in part because of the discount factor (see, e.g.,  $(3.109)$ ). The stratification direction we use is tailored to a particular rate  $L_n$  (through (4.49)), but not necessarily to the discount factor. The discount factor becomes a constant under the forward measure and, accordingly, we see a greater variance reduction in this case, at the same maturity. Surprisingly, we find the greatest improvement in the case of the swaption, even though the stratification direction is not specifically tailored to the swap rate.

|                  | $\text{Linear}$ | $\text{Constant}$ |
|------------------|-----------------|-------------------|
|                  | volatility      | volatility        |
| Spot Measure     |                 |                   |
| Caplet, $T = 20$ | 2               |                   |
| Caplet, $T=5$    | 26              | 50                |
| Swaption, $T=5$  | 38              | 79                |
| Bond, $T = 20.5$ | 12              | 4                 |
| Bond, $T = 5.5$  | 5               | 4                 |
| Forward Measure  |                 |                   |
| Caplet, $T = 20$ |                 |                   |

**Table 4.2.** Variance reduction factors using one-dimensional stratified sampling in a single-factor LIBOR market model. The stratification direction is determined by the vector of volatilities. The results are based on 1000 replications of samples (stratified or independent) of size 40. For each instrument, the value of  $T$  indicates the maturity.

## Optimal Directions

In estimating  $\mathsf{E}[f(\xi)]$  with  $\xi \sim N(\mu, \Sigma)$  and f a function from  $\Re^d$  to  $\Re$ , it would be convenient to know the stratification direction v for which stratifying  $v^{\top}\xi$ would produce the greatest reduction in variance. Finding this optimal  $v$  is rarely possible; we give a few examples for which the optimal direction is available explicitly.

With no essential loss of generality, we restrict attention to the case of  $\mathsf{E}[f(Z)]$  with  $Z \sim N(0, I)$ . From the variance decomposition (4.45) and the surrounding discussion, we know that the residual variance after stratifying a linear combination  $v^{\top}Z$  is  $\mathsf{E}[\mathsf{Var}[f(Z)|\eta]]$ , where  $\eta$  is the (random) index of the stratum containing  $v^{\top}Z$ . If we use equiprobable strata and let the number of strata grow (with each new set of strata refining the previous set), this residual variance converges to  $\mathsf{E}[\mathsf{Var}[f(Z)|v^{\top}Z]]$  (cf. Lemma 4.1 of [139]). We will therefore compare alternative choices of  $v$  through this limiting value.

In the linear case  $f(z) = b^{\top}z$ , it is evident that the optimal direction is  $v = b$ . Next, let  $f(z) = z^{\dagger} A z$  for some  $d \times d$  matrix A. We may assume that A is symmetric and thus that it has real eigenvalues  $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_d$  and associated orthonormal eigenvectors  $v_1, \ldots, v_d$ . Minimizing  $\mathsf{E}[\mathsf{Var}[f(Z)|v^\top Z]]$ over vectors  $v$  for which  $v^{\top}v = 1$  is equivalent to maximizing  $\text{Var}[\mathsf{E}[f(Z)|v^{\top}Z]]$ over the same set because the two terms sum to  $\text{Var}[f(Z)]$  for any v. In the quadratic case, some matrix algebra shows that  $v^{\top}v = 1$  implies

$$\mathsf{Var}[\mathsf{E}[Z^{\top}AZ|v^{\top}Z]] = (v^{\top}Av)^2.$$

This is maximized by  $v_1$  if  $\lambda_1^2 \geq \lambda_d^2$  and by  $v_d$  if  $\lambda_d^2 \geq \lambda_1^2$ . In other words, the optimal stratification direction is an eigenvector of  $A$  associated with an eigenvalue of largest absolute value. The effect of optimal stratification is to reduce variance from  $\sum_i \lambda_i^2$  to  $\sum_i \lambda_i^2 - \max_i \lambda_i^2$ .

As a final case, let  $f(z) = \exp(\frac{1}{2}z^{\top}Az)$ . For  $f(Z)$  to have finite second moment, we now require that  $\lambda_1 < 1/2$ . Theorem 4.1 of [139] shows that the optimal stratification direction in this case is an eigenvector  $v_{j^*}$  where  $j^*$  $satisfies$ 

$$\left(\frac{\lambda_{j^*}}{1-\lambda_{j^*}}\right)^2 = \max_{i=1,\ldots,d} \left(\frac{\lambda_i}{1-\lambda_i}\right)^2. \tag{4.50}$$

As in the previous case, this criterion will always select either  $\lambda_1$  or  $\lambda_d$ , but it will not necessarily select the one with largest absolute value.

Simulation is unnecessary for evaluation of  $E[f(Z)]$  in each of these examples. Nevertheless, a linear, quadratic, or exponential-quadratic function may be useful as an approximation to a more general  $f$  and thus as a guide in selecting stratification directions. Fox  $[127]$  uses quadratic approximations for related purposes in implementing quasi-Monte Carlo methods. Glasserman, Heidelberger, and Shahabuddin [139] use an exponential-quadratic approximation for stratified sampling in option pricing; in their application,  $A$  is the Hessian of the logarithm of an option's discounted payoff. We discuss this method in Section  $4.6.2$ .

## Radial Stratification

The symmetry of the standard multivariate normal distribution makes it possible to draw samples from this distribution with stratified norm. For  $Z \sim N(0, I)$  in  $\Re^d$ , let

$$X = Z_1^2 + \dots + Z_d^2,$$

so that  $\sqrt{X} = \|Z\|$  is the radius of the sphere on which Z falls. The distribution of X is chi-square with d degrees of freedom (abbreviated  $\chi^2_d$ ) and is given explicitly in  $(3.71)$ . Section 3.4.2 discusses efficient methods for sampling from  $\chi^2_d$ , but for stratification it is more convenient to use the inverse transform method as explained in Example  $4.3.2$ . There is no closed-form expression for the inverse of the  $\chi^2_d$  distribution, but the inverse can be evaluated numerically and methods for doing this are available in many statistical software libraries (see, e.g., the survey in Section 18.5 of [201]). Hence, by generating a stratified sample from Unif[0,1] and then applying the inverse of the  $\chi^2_d$  distribution, we can generate stratified values of  $X$ .

The next step is to sample  $Z$  conditional on the value of the stratification variable  $X$ . Because of the symmetry of the normal distribution, given  $X$  the vector Z is uniformly distributed on the sphere of radius  $\sqrt{X}$ . This is the basis of the Box-Muller method (cf. Section 2.3) in dimension 2 but it holds for all dimensions d. To sample uniformly from the sphere of radius  $R = \sqrt{X}$  in  $\Re^d$ , we can extend the Box-Muller construction as follows: sample  $U_1, \ldots, U_{d-1}$ independently from  $\text{Unif}[0,1]$  and set

$$Z_1 = R \cos(2\pi U_1)$$
  
$$Z_2 = R \sin(2\pi U_1) \cos(2\pi U_2)$$

::  
::  

$$Z_{d-1} = R \sin(2\pi U_1) \sin(2\pi U_2) \cdots \sin(2\pi U_{d-2}) \cos(2\pi U_{d-1})$$
  
 $Z_d = R \sin(2\pi U_1) \sin(2\pi U_2) \cdots \sin(2\pi U_{d-2}) \sin(2\pi U_{d-1}).$ 

Alternatively, given a method for generating standard normal random variables we can avoid the evaluation of sines and cosines. If  $\xi_1, \ldots, \xi_d$  are independent  $N(0,1)$  random variables and  $\xi = (\xi_1,\ldots,\xi_d)^\top$ , then  $\xi/\|\xi\|$  is uniformly distributed over the unit sphere and

$$Z = R \frac{\xi}{\|\xi\|}$$

is uniformly distributed over the sphere of radius of  $R$ .

It should be noted that neither of these constructions extends easily to stratified sampling from  $N(0,\Sigma)$  for general  $\Sigma$ . If  $\zeta \sim N(0,\Sigma)$  and  $X = \zeta \Sigma^{-1} \zeta$ , then  $X \sim \chi^2_d$  and we can stratify  $X$  just as before; moreover, given  $X$ ,  $\zeta$  is uniformly distributed over the ellipsoid

$$\mathcal{H}_X = \{ x \in \mathbb{R}^d : x^\top \Sigma^{-1} x = X \}.$$

The difficulty lies in sampling uniformly from the ellipsoid. Extending the Box-Muller construction entails replacing the sines and cosines with elliptic functions. The second construction does not appear to generalize at all: if  $\xi \sim N(0, \Sigma)$ , the vector  $\sqrt{X}\xi/\sqrt{\xi^{\top}\Sigma^{-1}\xi}$  lies on the ellipsoid  $\mathcal{H}_X$  but is not uniformly distributed over the ellipsoid.

The construction does, however, generalize beyond the standard normal to the class of *spherically contoured* distributions. The random vector  $Y$  is said to have a spherically contoured distribution if its conditional distribution given  $||Y||$  is uniform over the sphere of radius  $||Y||$ ; see Fang, Kotz, and Ng [114]. To stratify Y along its radius, we must therefore stratify  $X = \|Y\|$ , which will not be  $\chi^2_d$  except in the normal case. Given X, we can sample Y uniformly from the sphere of radius  $||X||$  using either of the methods described above for the normal distribution.

Radial stratification is proposed and applied in  $[142]$  as a method for reducing variance in estimating the risk in a portfolio of options for which losses result from large moves of the underlying assets in any direction.

## Stratifying a Poisson Process

In this example, we generate a Poisson process on  $[0,T]$  with the total number of jumps in this interval stratified. Let  $\lambda$  denote the arrival rate for the Poisson process and N the number of jumps in  $[0,T]$ . Then N is a Poisson random variable with distribution

$$P(N = k) = e^{-\lambda T} \frac{(\lambda T)^k}{k!}, \quad k = 0, 1, 2, \dots.$$

We can sample from this distribution using the inverse transform method, as in Figure 3.9, and thus generate a stratified sample of values as in Example 4.3.2.

For each value of  $N$  in the stratified sample, we need to generate the arrival times of the jumps in  $[0,T]$  conditional on the number of jumps N. For this we use a standard property of the Poisson process: given  $N = k$ , the arrival times of the jumps have the joint distribution of the order statistics of k independent random variables uniformly distributed over  $[0, T]$ . Thus, we may start from Unif[0,1] random variables  $U_1,\ldots,U_k$ , multiply them by T to make them uniform over  $[0,T]$ , and then sort them in ascending order to obtain the arrival times.

An alternative to sorting, detailed in Fox  $[127]$ , samples directly from the joint distribution of the order statistics. Let  $V_1, \ldots, V_k$  and  $U_1, \ldots, U_k$  denote independent  $\text{Unif}[0,1]$  random variables. Then

$$V_1^{1/k} V_2^{1/(k-1)} \cdots V_k, \quad \ldots, \quad V_1^{1/k} V_2^{1/(k-1)}, \quad V_1^{1/k}$$
 (4.51)

have the joint distribution of the ascending order statistics of  $U_1, \ldots, U_k$ . For example,

$$P(\max(U_1,\ldots,U_k) \le x) = P(U_1 \le x) \cdots P(U_k \le x) = x^k, \quad x \in [0,1],$$

and the last term in  $(4.51)$  simply samples from this distribution by applying its inverse to  $V_1$ . An induction argument verifies correctness of the remaining terms in  $(4.51)$ . The products in  $(4.51)$  can be evaluated recursively from right to left. (To reduce round-off error, Fox [127] recommends recursively summing the logarithms of the  $V_i^{1/(k-i+1)}$  and then exponentiating.) The *i*th arrival time,  $i = 1, \ldots, k$ , can then be generated as

$$\tau_i = TV_1^{1/k} V_2^{1/(k-1)} \cdots V_{k-i+1}^{1/i}; \qquad (4.52)$$

i.e., by rescaling from  $[0, 1]$  to  $[0, T]$ . Because the terms in  $(4.51)$  are generated from right to left, Fox  $[127]$  instead sets

$$\tau_i = T \cdot (1 - V_1^{1/k} V_2^{1/(k-1)} \cdots V_i^{1/(k-i+1)});$$

this has the same distribution as  $(4.52)$  and allows generation of the arrival times in a single pass. (Subtracting the values in  $(4.51)$  from 1 maps the *i*th largest value to the *i*th smallest.)

This method of stratification extends, in principle, to inhomogeneous Poisson processes. The number of arrivals in  $[0, T]$  continues to be a Poisson random variable in this case. Conditional on the number of arrivals, the times of the arrivals continue to be distributed as order statistics, but now of random variables with a density proportional to the arrival rate  $\lambda(t), t \in [0, T]$ , rather than a uniform density.

## Terminal Stratification in a Binomial Lattice

A binomial lattice provides a discrete-time, discrete-space approximation to the evolution of a diffusion process. Each node in the lattice (see Figure  $4.7$ ) is associated with a level of the underlying asset (or rate)  $S$ ; over a single time step, the movement of the asset is restricted to two successor nodes, usually corresponding to a move up and a move down. By varying the spacing of the nodes and the transition probabilities, it is possible to vary the conditional mean and variance of the change in the underlying asset over a single time step, and thus to approximate virtually any diffusion processes.

![](_page_45_Figure_3.jpeg)

**Fig. 4.7.** A four-step binomial lattice. Each node has an associated value  $S$  of the underlying asset. Each node has two successor nodes, corresponding to a move up and a move down.

Binomial lattices are widely used for numerical option pricing. A typical algorithm proceeds by backward induction: an option contract determines the payoffs at the terminal nodes (which correspond to the option expiration); the option value at any other node is determined by discounting the values at its two successor nodes.

Consider, for example, the pricing of a put with strike  $K$ . Each terminal node corresponds to some level  $S$  of the underlying asset at expiration and thus to an option value  $(K-S)^+$ . A generic node in the lattice has an "up" successor node and a "down" successor node; suppose the option values  $V_u$ and  $V_d$ , respectively, at the two successor nodes have already been calculated. If the probability of a move up is  $p$ , and if the discount factor over a single step is  $1/(1+R)$ , then the value at the current node is

$$V = \frac{1}{1+R} \left( pV_u + (1-p)V_d \right).$$

In pricing an *American* put, the backward induction rule is

$$V = \max\left(\frac{1}{1+R}\left(pV_u + (1-p)V_d\right), K-S\right).$$

Binomial option pricing is ordinarily a deterministic calculation, but it can be combined with Monte Carlo. Some path-dependent options, for example, are more easily valued through simulation than through backward induction. In some cases, there are advantages to sampling paths through the binomial lattice rather than sampling paths of a diffusion. For example, in an interest rate lattice, it is possible to compute bond prices at every node. The availability of these bond prices can be useful in pricing path-dependent options on, e.g., bonds or swaps through simulation.

An ordinary simulation through a binomial lattice starts at the root node and generates moves up or down using the appropriate probabilities for each node. As a further illustration of stratified sampling, we show how to simulate paths through a binomial lattice with the terminal value stratified.

Consider, first, the case of a binomial lattice for which the probability of an up move has the same value  $p$  at all nodes. In this case, the total number of up moves  $N$  through an  $m$ -step lattice has the binomial distribution

$$P(N = k) = {m \choose k} p^k (1-p)^{m-k}, \quad k = 0, 1, \dots, m.$$

Samples from this distribution can be generated using the inverse transform method for discrete distributions, as in Example 2.2.4, much as in the case of the Poisson distribution in Figure 3.9. As explained in Example 4.3.2, it is a simple matter to generate stratified samples from a distribution using the inverse transform method. Thus, we have a mechanism for stratifying the total number of up moves through the lattice. Since the terminal node is determined by the difference  $N - (m - N) = 2N - m$  between the number of up and down moves, stratifying  $N$  is equivalent to stratifying the terminal node.

The next step is to sample a path through the lattice *conditional* on the terminal node — equivalently, conditional on the number of up moves  $N$ . The key observation for this procedure is that, given  $N$ , all paths through the lattice with N up moves (hence  $m - N$  down moves) are equally likely. Generating a path conditional on  $N$  is simply a matter of randomly distributing  $N$  "ups" among m moves. At each step, the probability of a move up is the ratio of the number of remaining up moves to the number of remaining steps. The following algorithm implements this idea:

 $k \leftarrow N$  (total number of up moves to be made) for  $i = 0, ..., m - 1$ if  $k = 0$  move down if  $k \geq m - i$  move up if  $0 < k < m - i$ 

```
generate U \sim \text{Unif}[0,1]if (m-i)U < kk \leftarrow k - 1move up
else move down
```

The variable k records the number of remaining up moves and  $m-i$  is the number of remaining steps. The condition  $(m-i)U < k$  is satisfied with probability  $k/(m-i)$ . This is the ratio of the number of remaining up moves to the number of remaining steps, and is thus the conditional probability of an up move on the next step. Repeating this algorithm for each of the stratified values of  $N$  produces a set of paths through the lattice with stratified terminal node.

This method extends to lattices in which the probability of an up move varies from node to node, though this extension requires substantial additional computing. The first step is to compute the distribution of the terminal node, which is no longer binomial. The probability of reaching a node can be calculated using the lattice itself: this probability is the "price" (without discounting) of a security that pays 1 in that node and 0 everywhere else. Through forward induction, the probabilities of all terminal nodes can be found in  $O(m^2)$  operations. Once these are computed, it becomes possible to use the discrete inverse transform method to generate stratified samples from the terminal distribution.

The next step is to simulate paths through the lattice conditional on a terminal node. For this, let  $p$  denote the unconditional probability of an up move at the current node. Let  $h_u$  denote the unconditional probability of reaching the given terminal node from the up successor of the current node; let  $h_d$  denote the corresponding probability from the down successor. Then the *conditional* probability of an up move at the current node (given the terminal node) is  $ph_u/(ph_u+(1-p)h_d)$  and the conditional probability of a down move is  $(1-p)h_d/(ph_u+(1-p)h_d)$ . Once the  $h_u$  and  $h_d$  have been calculated at every node, it is therefore a simple matter to simulate paths conditional on a given terminal node by applying these conditional probabilities at each step. Implementing this requires calculation of  $O(m)$  conditional probabilities at every node, corresponding to the  $O(m)$  terminal nodes. These can be calculated with a total effort of  $O(m^3)$  using backward induction.

## 4.3.3 Poststratification

As should be evident from our discussion thus far, implementation of stratified sampling requires knowledge of stratum probabilities and a mechanism for conditional sampling from strata. Some of the examples discussed in Sec- $\text{tion } 4.3.2 \text{ suggest that conditional sampling may be difficult even when com$ puting stratum probabilities is not. *Poststratification* combines knowledge of stratum probabilities with ordinary independent sampling to reduce variance,

at least asymptotically. It can therefore provide an attractive alternative to genuine stratification when conditional sampling is costly.

As before, suppose our objective is to estimate  $E[Y]$ . We have a mechanism for generating independent replications  $(X_1, Y_1), \ldots, (X_n, Y_n)$  of the pair  $(X,Y)$ ; moreover, we know the probabilities  $p_i = P(X \in A_i)$  for strata  $A_1,\ldots,A_K$ . As usual, we require that these be positive and sum to 1. For  $i = 1, \ldots, K$ , let

$$N_i = \sum_{j=1}^n \mathbf{1}\{X_j \in A_i\}$$

denote the number of samples that fall in stratum  $i$  and note that this is now a random variable. Let

$$S_i = \sum_{j=1}^n \mathbf{1}\{X_j \in A_i\} Y_j$$

denote the sum of those  $Y_j$  for which  $X_i$  falls in stratum *i*, for  $i = 1, \ldots, K$ .

The usual sample mean  $\bar{Y} = (Y_1 + \cdots + Y_n)/n$  can be written as

$$\bar{Y} = \frac{S_1 + \dots + S_K}{n} = \sum_{i=1}^K \frac{N_i}{n} \cdot \frac{S_i}{N_i},$$

at least if all  $N_i$  are nonzero. By the strong law of large numbers,  $N_i/n \to p_i$ and  $S_i/N_i \to \mu_i$ , with probability 1, where  $\mu_i = \mathsf{E}[Y|X \in A_i]$  denotes the stratum mean, as in  $(4.37)$ . Poststratification replaces the random fraction  $N_i/n$  with its expectation  $p_i$  to produce the estimator

$$\hat{Y} = \sum_{i=1}^{K} p_i \frac{S_i}{N_i}.$$
(4.53)

Whereas the sample mean  $\bar{Y}$  assigns weight  $1/n$  to every observation, the poststratified estimator weights values falling in stratum i by the ratio  $p_i/N_i$ . Thus, values from undersampled strata  $(N_i < np_i)$  get more weight and values from oversampled strata  $(N_i > np_i)$  get less weight. To cover the possibility that none of the *n* replications falls in the *i*th stratum, we replace  $S_i/N_i$  with zero in (4.53) if  $N_i = 0$ .

It is immediate from the almost sure convergence of  $S_i/N_i$  to  $\mu_i$  that the poststratified estimator  $\hat{Y}$  is a consistent estimator of  $\mathsf{E}[Y]$ . Less clear are its merits relative to the ordinary sample mean or a genuinely stratified estimator. We will see that, asymptotically as the sample size grows, poststratification is as effective as stratified sampling in reducing variance. To establish this result, we first consider properties of ratio estimators more generally.

## Ratio Estimators

We digress briefly to derive a central limit theorem for ratio estimators. For this discussion, let  $(R_i, Q_i)$ ,  $i = 1, 2, \ldots$ , be independent and identically distributed pairs of random variables with

$$\mathsf{E}[R_i] = \mu_R, \ \mathsf{E}[Q_i] = \mu_Q, \ \mathsf{Var}[R_i] = \sigma_R^2, \ \mathsf{Var}[Q_i] = \sigma_Q^2, \ \mathsf{Cov}[R_i, Q_i] = \sigma_{RQ},$$

and  $\mu_Q \neq 0$ . The sample means of the first *n* values are

$$\bar{R} = \frac{1}{n} \sum_{i=1}^{n} R_i, \quad \bar{Q} = \frac{1}{n} \sum_{i=1}^{n} Q_i.$$

By the strong law of large numbers, the ratio  $\bar{R}/\bar{Q}$  converges with probability 1 to  $\mu_R/\mu_Q$ .

By applying the delta method introduced in Section 4.1.4 to the function  $h(x,y) = x/y$ , we obtain a central limit theorem of the form

$$\sqrt{n}\left(\frac{\bar{R}}{\bar{Q}} - \frac{\mu_R}{\mu_Q}\right) \Rightarrow N(0, \sigma^2)$$

for the ratio estimator. The variance parameter  $\sigma^2$  is given by the general expression in  $(4.26)$  for the delta method and simplifies in this case to

$$\sigma^2 = \frac{\mu_R^2}{\mu_Q^4} \sigma_R^2 - \frac{2\mu_R}{\mu_Q^3} \sigma_{RQ} + \frac{\sigma_R^2}{\mu_Q^2} = \frac{\text{Var}[R - \frac{\mu_R}{\mu_Q}Q]}{\mu_Q^2}.$$
 (4.54)

This parameter is consistently estimated by

$$s^{2} = \sum_{i=1}^{n} \left( R_{i} - \bar{R}Q_{i}/\bar{Q} \right)^{2} / n(\bar{Q})^{2},$$

from which we obtain an asymptotically valid  $1 - \delta$  confidence interval

$$\frac{\bar{R}}{\bar{Q}} \pm z_{\delta/2} \frac{s}{\sqrt{n}},$$

with  $z_{\delta/2} = -\Phi^{-1}(\delta/2)$ .

For fixed n,  $\bar{R}/\bar{Q}$  is a biased estimator of  $\mu_R/\mu_Q$ . The bias has the form

$$\mathsf{E}\left[\frac{\bar{R}}{\bar{Q}} - \frac{\mu_R}{\mu_Q}\right] = \frac{(\mu_R \sigma_Q^2/\mu_Q^3) - (\sigma_{RQ}/\mu_Q^2)}{n} + O(1/n^2);$$

see, e.g., Fishman  $[121]$ , p.109. Subtracting an estimate of the leading term can reduce the bias to  $O(1/n^2)$ .

## Poststratification: Asymptotic Variance

We now apply this analysis of ratio estimators to derive a central limit theorem for the poststratified estimator  $\hat{Y}$ , which is a linear combination of ratio estimators. A straightforward extension of the result for a single ratio gives

$$\sqrt{n}\left(\frac{S_1}{N_1}-\mu_1,\ldots,\frac{S_K}{N_K}-\mu_K\right)\Rightarrow N(0,\Sigma),$$

with the limiting matrix  $\Sigma$  again determined by the delta method. For the diagonal entries of  $\Sigma$ , (4.54) gives

$$\Sigma_{ii} = \frac{\text{Var}[Y\mathbf{1}\{X \in A_i\} - \mu_i \mathbf{1}\{X \in A_i\}]}{p_i^2} = \frac{\sigma_i^2}{p_i},$$

with  $\sigma_i^2$  the stratum variance defined in (4.38). A similar calculation for  $j \neq i$ gives

$$\Sigma_{ij} = \frac{\text{Cov}[(Y - \mu_i)\mathbf{1}\{X \in A_i\}, (Y - \mu_j)\mathbf{1}\{X \in A_j\}]}{p_i p_j} = 0$$

because  $A_i$  and  $A_j$  are disjoint.

The poststratified estimator satisfies

$$\hat{Y} - \mu = \sum_{i=1}^{K} p_i \left( \frac{S_i}{N_i} - \mu_i \right)$$

and therefore

$$\sqrt{n}[\hat{Y} - \mu] \Rightarrow N(0, \sigma^2)$$

with

$$\sigma^2 = \sum_{i,j=1}^K p_i \Sigma_{ij} p_j = \sum_{i=1}^K p_i \sigma_i^2.$$

This is precisely the asymptotic variance for the stratified estimator based on proportional allocation of samples to strata; see  $(4.42)$ . It can be estimated consistently by replacing each  $\sigma_i^2$  with the sample variance of the observations falling in the  $i$ th stratum.

From this result we see that in the large-sample limit, we can extract all the variance reduction of stratified sampling without having to sample conditionally from the strata by instead weighting each observation according to its stratum. How large the sample needs to be for the two methods to give similar results depends in part on the number of strata and their probabilities. There is no simple way to determine at what sample size this limit becomes relevant without experimentation. But stratified sampling is generally preferable and poststratification is best viewed as an alternative for settings in which conditional sampling from the strata is difficult.

## 4.4 Latin Hypercube Sampling

Latin hypercube sampling is an extension of stratification for sampling in multiple dimensions. Recall from the discussion in Example 4.3.4 that stratified sampling in high dimensions is possible in principle but often infeasible in practice. The difficulty is apparent even in the simple case of sampling from the d-dimensional hypercube  $[0,1)^d$ . Partitioning each coordinate into K strata produces  $K^d$  strata for the hypercube, thus requiring a sample size of at least  $K^d$  to ensure that each stratum is sampled. For even moderately large d, this may be prohibitive unless  $K$  is small, in which case stratification provides little benefit. For this reason, in Section  $4.3.2$  we focused on methods for stratifying a small number of important directions in multidimensional problems.

Latin hypercube sampling treats all coordinates equally and avoids the exponential growth in sample size resulting from full stratification by stratifying only the one-dimensional marginals of a multidimensional joint distribution. The method, introduced by McKay, Conover, and Beckman [259] and further analyzed in Stein  $[337]$ , is most easily described in the case of sampling from the uniform distribution over the unit hypercube. Fix a dimension  $d$  and a sample size K. For each coordinate  $i = 1, \ldots, d$ , independently generate a stratified sample  $V_i^{(1)}, \ldots, V_i^{(K)}$  from the unit interval using K equiprobable strata; each  $V_i^{(j)}$  is uniformly distributed over  $[(j-1)/K, j/K)$ . If we arrange the  $d$  stratified samples in columns.

$$V_{1}^{(1)} \quad V_{2}^{(1)} \quad \cdots \quad V_{d}^{(1)}$$
$$V_{1}^{(2)} \quad V_{2}^{(2)} \quad \cdots \quad V_{d}^{(2)}$$
$$\vdots \qquad \vdots \qquad \vdots$$
$$V_{1}^{(K)} \quad V_{2}^{(K)} \quad \cdots \quad V_{d}^{(K)}$$

then each row gives the coordinates of a point in  $[0,1)^d$ . The first row identifies a point in  $[0, 1/K)^d$ , the second a point in  $[1/K, 2/K)^d$ , and so on, corresponding to  $K$  points falling in subcubes along the diagonal of the unit hypercube. Now randomly permute the entries in each column of the array. More precisely, let  $\pi_1, \ldots, \pi_d$  be permutations of  $\{1, \ldots, K\}$ , drawn independently from the distribution that makes all  $K!$  such permutations equally likely. Let  $\pi_i(i)$  denote the value to which  $i$  is mapped by the *j*th permutation. The rows of the  $array$ 

$$V_{1}^{\pi_{1}(1)} \quad V_{2}^{\pi_{2}(1)} \quad \cdots \quad V_{d}^{\pi_{d}(1)}$$
  

$$V_{1}^{\pi_{1}(2)} \quad V_{2}^{\pi_{2}(2)} \quad \cdots \quad V_{d}^{\pi_{d}(2)}$$
  

$$\vdots \qquad \vdots \qquad \vdots$$
  

$$V_{1}^{\pi_{1}(K)} \quad V_{2}^{\pi_{2}(K)} \quad \cdots \quad V_{d}^{\pi_{d}(K)}$$
  

$$(4.55)$$

continue to identify points in  $[0,1)^d$ , but they are no longer restricted to the diagonal. Indeed, each row is a point *uniformly distributed* over the unit

hypercube. The K points determined by the K rows are not independent: if we project the  $K$  points onto their *i*th coordinates, the resulting set of values  $\{V_i^{\pi_i(1)}, \ldots, V_i^{\pi_i(K)}\}$  is the same as the set  $\{V_i^{(1)}, \ldots, V_i^{(K)}\}$ , and thus forms a stratified sample from the unit interval.

The "marginal" stratification property of Latin hypercube sampling is illustrated in Figure 4.8. The figure shows a sample of size  $K = 8$  in dimension  $d = 2$ . Projecting the points onto either of their two coordinates shows that exactly one point falls in each of the eight bins into which each axis is partitioned. Stratified sampling would require drawing a point from each square and thus a sample size of  $64$ .

![](_page_52_Figure_3.jpeg)

Fig. 4.8. A Latin hypercube sample of size  $K = 8$  in dimension  $d = 2$ .

To generate a Latin hypercube sample of size K in dimension d, let  $U_i^{(j)}$ be independent Unif[0,1) random variables for  $i = 1, \ldots, d$  and  $j = 1, \ldots, K$ . Let  $\pi_1, \ldots, \pi_d$  be independent random permutations of  $\{1, \ldots, K\}$  and set

$$V_i^{(j)} = \frac{\pi_i(j) - 1 + U_i^{(j)}}{K}, \quad i = 1, \dots, d, \quad j = 1, \dots, K. \tag{4.56}$$

The sample consists of the  $K$  points  $(V_1^{(j)}, \ldots, V_d^{(j)}), j = 1, \ldots, K$ . To generate a random permutation, first sample uniformly from  $\{1,\ldots,K\}$ , then sample uniformly from the remaining values, and continue until only one value remains. In (4.56) we may choose one of the permutations  $(\pi_d, \text{ say})$  to be the identity,  $\pi_d(i) \equiv i$  without affecting the joint distribution of the sample.

Using the inverse transform method, this construction easily extends to nonuniform distributions. For example, to generate a Latin hypercube sample of size K from  $N(0, I)$  in  $\mathbb{R}^d$ , set

$$Z_i^{(j)} = \Phi^{-1}(V_i^{(j)}), \quad i = 1, \dots, d, \quad j = 1, \dots, K$$

with  $\Phi$  the cumulative normal and  $V_i^{(j)}$  as in (4.56). The sample consists of  $\text{the vectors}$ 

$$Z^{(j)} = (Z_1^{(j)}, \dots, Z_d^{(j)}), \quad j = 1, \dots, K; \tag{4.57}$$

in  $\Re^d$ . Projecting these K points onto any axis produces a stratified sample of size  $K$  from the standard univariate normal distribution. Even if the inverse transform is inconvenient or if the marginals have different distributions, the construction in  $(4.55)$  continues to apply, provided we have some mechanism for stratifying the marginals: generate a stratified sample from each marginal using  $K$  equiprobable strata for each, then randomly permute these d stratified samples.

This construction does rely crucially on the assumption of independent marginals, and transforming variables to introduce dependence can affect the partial stratification properties of Latin hypercube samples in complicated ways. This is evident in the case of a multivariate normal distribution  $N(0, \Sigma)$ . To sample from  $N(0, \Sigma)$ , we set  $X = AZ$  with  $Z \sim N(0, I)$  and  $AA^{\top} = \Sigma$ . Replacing independently generated Zs with the Latin hypercube sample  $(4.57)$ produces points  $X^{(j)} = AZ^{(j)}, j = 1, \ldots, K$ ; but the marginals of the  $X^{(j)}$ so constructed will not in general be stratified. Rather, the marginals of the  $A^{-1}X^{(j)}$  are stratified.

**Example 4.4.1** Brownian paths. As a specific illustration, consider the simulation of Brownian paths at times  $0 = t_0 < t_1 \cdots < t_d$ . As in (4.57), let  $Z^{(1)}, \ldots, Z^{(K)}$  denote a Latin hypercube sample from  $N(0, I)$  in d dimensions. From these K points in  $\Re^d$ , we generate K discrete Brownian paths  $W^{(1)}, \ldots, W^{(K)}$  by setting

$$W^{(j)}(t_n) = \sum_{i=1}^n \sqrt{t_i - t_{i-1}} Z_i^{(j)}, \quad n = 1, \dots, d.$$

If we fix a time  $t_n$ ,  $n \geq 2$ , and examine the K values  $W^{(1)}(t_n), \ldots, W^{(K)}(t_n)$ , these will not form a stratified sample from  $N(0, t_n)$ . It is rather the increments of the Brownian paths that would be stratified.

These K Brownian paths could be used to generate K paths of a process driven by a single Brownian motion. It would not be appropriate to use the  $K$  Brownian paths to generate a single path of a process driven by a  $K$ -dimensional Brownian motion. Latin hypercube sampling introduces dependence between elements of the sample, whereas the coordinates of a  $K$ dimensional (standard) Brownian motion are independent. Using  $(W^{(1)}, \ldots,$  $W^{(K)}$  in place of a K-dimensional Brownian motion would thus change the law of the simulated process and could introduce severe bias. In contrast, the *marginal* law of each  $W^{(j)}$  coincides with that of a scalar Brownian motion. Put succinctly, in implementing a variance reduction technique we are free to introduce dependence *across* paths but not *within* paths.  $\Box$ 

**Example 4.4.2** Paths through a lattice. To provide a rather different example, we apply Latin hypercube sampling to the problem of simulating paths through a binomial lattice. (See Figure 4.7 and the surrounding discussion for background.) Consider an *m*-step lattice with fixed probabilities p and  $1-p$ . The "marginals" in this example correspond to the  $m$  time steps, so the dimension d equals m, and the sample size K is the number of paths. We encode a move up as a 1 and a move down as a 0. For each  $i = 1, \ldots, m$  we generate a stratified sample of 1s and 0s: we "generate"  $|pK|$  1s and  $|K - pK|$  0s, and if  $pK$  is not an integer, the Kth value in the sample is 1 with probability p and 0 with probability  $1 - p$ . For example, with  $d = 4$ ,  $K = 8$ , and  $p = 0.52$ , we might get

|              | $1\ 1\ 1\ 1$ |  |
|--------------|--------------|--|
|              | $1\ 1\ 1\ 1$ |  |
|              | $1\ 1\ 1\ 1$ |  |
|              | $1\ 1\ 1\ 1$ |  |
|              |              |  |
| $0\ 0\ 0\ 0$ |              |  |
|              | $0\ 0\ 0\ 0$ |  |
|              | $0\ 0\ 0\ 0$ |  |

the columns corresponding to the  $d = 4$  stratified samples. Applying a random permutation to each column produces, e.g.,

> $0\ 1\ 0\ 1$  $0\ 0\ 1\ 1$  $1\ 1\ 0\ 1$ 1110  $0\ 1\ 0\ 0$  $1011$  $0\ 0\ 1\ 0$ 1100

Each row now encodes a path through the lattice. For example, the last row corresponds to two consecutive moves up followed by two consecutive moves down. Notice that, for each time step  $i$ , the fraction of paths on which the *ith* step is a move up is very nearly  $p$ . This is the property enforced by Latin hypercube sampling.

One could take this construction a step further to enforce the (nearly) correct fraction of up moves at each *node* rather than just at each time step. For simplicity, suppose  $Kp^d$  is an integer. To the root node, assign  $Kp$  1s and  $K(1-p)$  0s. To the node reached from the root by taking  $\ell$  steps up and k steps down,  $\ell + k < d$ , assign  $Kp^{\ell+1}(1-p)^k$  ones and  $Kp^{\ell}(1-p)^{k+1}$  zeros. Randomly and independently permute the ones and zeros at all nodes. The result encodes  $K$  paths through the lattice with the fraction of up moves out of every node exactly equal to  $p$ .

Mintz  $[269]$  develops a simple way to implement essentially the same idea. His implementation eliminates the need to precompute and permute the outcomes at all nodes. Instead, it assigns to each node a counter that keeps track

of the number of paths that have left that node by moving up. For example, consider again a node reached from the root by taking  $\ell$  steps up and k steps down,  $\ell + k < d$ . Let K be the total number of paths to be generated and again suppose for simplicity that  $Kp^d$  is an integer. The number of paths reaching the designated node is

$$K_{\ell k} = K p^{\ell} (1 - p)^k,$$

so the counter at that node counts from zero to  $pK_{\ell k}$ , the number of paths that exit that node by moving up. If a path reaches the node and finds the counter at i, it moves down with probability  $i/pK_{\ell k}$  and moves up with the complementary probability. If it moves up, the counter is incremented to  $i+1$ .  $\Box$ 

## Variance Reduction and Variance Decomposition

We now state some properties of Latin hypercube sampling that shed light on its effectiveness. These properties are most easily stated in the context of sampling from  $[0,1)^d$ . Thus, suppose our goal is to estimate

$$\alpha_f = \int_{[0,1)^d} f(u) \, du$$

for some square-integrable  $f:[0,1)^d \to \mathbb{R}$ . The standard Monte Carlo estimator of this integral can be written as

$$\bar{\alpha}_f = \frac{1}{K} \sum_{j=0}^{K-1} f(U_{jd+1}, U_{jd+2}, \dots, U_{jd+d})$$

with  $U_1, U_2, \ldots$  independent uniforms. The variance of this estimator is  $\sigma^2/K$ with  $\sigma^2 = \text{Var}[f(U_1,\ldots,U_d)]$ . For  $V^{(1)},\ldots,V^{(K)}$  as in (4.56), define the esti- $\text{mator}$ 

$$\hat{\alpha}_f = \frac{1}{K} \sum_{j=1}^K f(V^{(j)}).$$

McKay et al.  $[259]$  show that

$$\text{Var}[\hat{\alpha}_f] = \frac{\sigma^2}{K} + \frac{K-1}{K} \text{Cov}[f(V^{(1)}), f(V^{(2)})],$$

which could be larger or smaller than the variance of the standard estimator  $\bar{\alpha}_f$ , depending on the covariance between distinct points in the Latin hypercube sample. By construction,  $V^{(j)}$  and  $V^{(k)}$  avoid each other — for example, their *i*th coordinates cannot fall in the same bin if  $j \neq k$  — which suggests that the covariance will often be negative. This holds, in particular, if  $f$  is monotone in each coordinate, as shown by McKay et al. [259]. Proposition 3 of Owen [288] shows that for any (square-integrable) f and any  $K > 2$ ,

4.4 Latin Hypercube Sampling  $241$ 

$$\operatorname{Var}[\hat{\alpha}_f] \leq \frac{\sigma^2}{K-1},$$

so the variance produced by a Latin hypercube sample of size  $K$  is no larger than the variance produced by an i.i.d. sample of size  $K-1$ .

Stein [337] shows that as  $K \to \infty$ , Latin hypercube sampling eliminates the variance due to the *additive* part of  $f$ , in a sense we now explain. For each  $i = 1, \ldots, d$ , let

$$f_i(u) = \mathsf{E}[f(U_1,\ldots,U_{i-1},u,U_i,\ldots,U_d)],$$

for  $u \in [0,1)$ . Observe that each  $f_i(U)$ ,  $U \sim \text{Unif}[0,1)$  has expectation  $\alpha_f$ . The function

$$f_{\text{add}}(u_1, \dots, u_d) = \sum_{i=1}^d f_i(u_i) - (d-1)\alpha_f$$

also has expectation  $\alpha_f$  and is the best additive approximation to f in the sense that

$$\int_{[0,1)^d} \left( f(u_1, \dots, u_d) - f_{\text{add}}(u_1, \dots, u_d) \right)^2 du_1 \cdots du_d$$
  
$$\leq \int_{[0,1)^d} \left( f(u_1, \dots, u_d) - \sum_{i=1}^d h_i(u_i) \right)^2 du_1 \cdots du_d$$

for any univariate functions  $h_1, \ldots, h_d$ . Moreover, the residual

$$\epsilon = f(U_1, \ldots, U_d) - f_{\text{add}}(U_1, \ldots, U_d)$$

is uncorrelated with  $f(U_1, \ldots, U_d)$  and this allows us to decompose the variance  $\sigma^2$  of  $f(U_1, \ldots, U_d)$  as  $\sigma^2 = \sigma_{\text{add}}^2 + \sigma_{\epsilon}^2$  with  $\sigma_{\text{add}}^2$  the variance of  $f_{\text{add}}(U_1, \ldots, U_d)$  and  $\sigma_{\epsilon}^2$  the variance o

$$\text{Var}[\hat{\alpha}_f] = \frac{\sigma_\epsilon^2}{K} + o(1/K). \tag{4.58}$$

Up to terms of order  $1/K$ , Latin hypercube sampling eliminates  $\sigma_{\text{add}}^2$  — the variance due to the additive part of  $f$  — from the simulation variance. This further indicates that Latin hypercube sampling is most effective with integrands that nearly separate into a sum of one-dimensional functions.

## Output Analysis

Under various additional conditions on  $f$ , Loh [238], Owen [285], and Stein [337] establish a central limit theorem for  $\hat{Y}$  of the form

$$\sqrt{K}[\hat{\alpha}_f - \alpha_f] \Rightarrow N(0, \sigma_\epsilon^2),$$

which in principle provides the basis for a large-sample confidence interval for  $\alpha_f$  based on Latin hypercube sampling. In practice,  $\sigma^2_{\epsilon}$  is neither known nor easily estimated, making this approach difficult to apply.

A simpler approach to interval estimation generates i.i.d. estimators  $\hat{\alpha}_f(1), \ldots, \hat{\alpha}_f(n)$ , each based on a Latin hypercube sample of size K. An asymptotically (as  $n \to \infty$ ) valid  $1 - \delta$  confidence interval for  $\alpha_f$  is provided by

$$\left(\frac{1}{n}\sum_{i=1}^{n}\hat{\alpha}_{f}(i)\right) \pm z_{\delta/2}\frac{\hat{s}}{\sqrt{n}},$$

with  $\hat{s}$  the sample standard deviation of  $\hat{\alpha}_f(1), \ldots, \hat{\alpha}_f(n)$ .

The only cost to this approach lies in foregoing the possibly greater variance reduction from generating a single Latin hypercube sample of size  $nK$ rather than n independent samples of size K. Stein [337] states that this loss is small if  $K/d$  is large.

A  $K \times K$  array is called a Latin square if each of the symbols  $1, \ldots, K$ appears exactly once in each row and column. This helps explain the name "Latin hypercube sampling." Latin squares are used in the design of experiments, along with the more general concept of an *orthogonal array*. Owen  $[286]$  extends Stein's  $[337]$  approach to analyze the variance of Monte Carlo estimates based on randomized orthogonal arrays. This method generalizes Latin hypercube sampling by stratifying low-dimensional (but not just onedimensional) marginal distributions.

## Numerical Illustration

We conclude this section with a numerical example. We apply Latin hypercube sampling to the pricing of two types of path-dependent options  $-$  an Asian option and a barrier option. The Asian option is a call on the arithmetic average of the underlying asset over a finite set of dates; the barrier option is a down-and-out call with a discretely monitored barrier. The underlying asset is  $\text{GBM}(r, \sigma^2)$  with  $r = 5\%, \sigma = 0.30$ , and an initial value of 50. The barrier is fixed at  $40$ . The option maturity is one year in all cases. We report results for  $8$  and  $32$  equally spaced monitoring dates; the number of dates is the dimension of the problem. With  $d$  monitoring dates, we may view each discounted option payoff as a function of a standard normal random vector in  $\Re^d$  and apply Latin hypercube sampling to generate these vectors.

Table  $4.3$  reports estimated variance reduction factors. Each entry in the table is an estimate of the ratio of the variance using independent sampling to the variance using a Latin hypercube sample of the same size. Thus, larger ratios indicate greater variance reduction. The sample sizes displayed are  $50$ ,  $200$ , and  $800$ . The ratios are estimated based on  $1000$  replications of samples of the indicated sizes.

The most salient feature of the results in Table  $4.3$  is the effect of varying the strike: in all cases, the variance ratio increases as the strike decreases. This

is to be expected because at lower strikes the options are more nearly linear. The variance ratios are nearly the same in dimensions  $8$  and  $32$  and show little dependence on the sample size. We know that the variance of independent replications (the numerators in these ratios) are inversely proportional to the sample sizes. Because the ratios are roughly constant across sample sizes, we may conclude that the variance using Latin hypercube sampling is nearly inversely proportional to the sample size. This suggests that (at least in these examples) the asymptotic result in  $(4.58)$  is relevant for sample sizes as small as  $K = 50$ .

|                  |                 | $8 \text{ steps}$ |     |     | $32 \text{ steps}$ |     |     |
|------------------|-----------------|-------------------|-----|-----|--------------------|-----|-----|
|                  | $\text{Strike}$ | 50                | 200 | 800 | 50                 | 200 | 800 |
| $\text{Asian}$   | 45              | 7.5               | 8.6 | 8.8 | 7.1                | 7.6 | 8.2 |
| Option           | 50              | 3.9               | 4.4 | 4.6 | 3.7                | 3.6 | 4.0 |
|                  | 55              | 2.4               | 2.6 | 2.8 | 2.3                | 2.1 | 2.5 |
| $\text{Barrier}$ | 45              | 4.1               | 4.1 | 4.3 | 3.8                | 3.7 | 3.9 |
| Option           | 50              | 3.2               | 3.2 | 3.4 | 3.0                | 2.9 | 3.1 |
|                  | 55              | 2.5               | 2.6 | 2.7 | 2.4                | 2.2 | 2.4 |

**Table 4.3.** Variance reduction factors using Latin hypercube sampling for two pathdependent options. Results are displayed for dimensions (number of monitoring dates) 8 and 32 using samples of size 50, 200, and 800. Each entry in the table is estimated from 1000 replications, each replication consisting of 50, 200, or 800 paths.

The improvements reported in Table 4.3 are mostly modest. Similar variance ratios could be obtained by using the underlying asset as a control variate; for the Asian option, far greater variance reduction could be obtained by using a geometric average control variate as described in Example  $4.1.2$ . One potential advantage of Latin hypercube sampling is that it lends itself to the use of a single set of paths to price many different types of options. The marginal stratification feature of Latin hypercube sampling is beneficial in pricing many different options, whereas control variates are ideally tailored to a specific application.

## 4.5 Matching Underlying Assets

÷.

This section discusses a set of loosely related techniques with the common objective of ensuring that certain sample means produced in a simulation exactly coincide with their population values (i.e., with the values that would be attained in the limit of infinitely many replications). Although these techniques could be used in almost any application of Monte Carlo, they take on special significance in financial engineering where matching sample and population means will often translate to ensuring exact finite-sample pricing of

underlying assets. The goal of derivatives pricing is to determine the value of a derivative security *relative* to its underlying assets. One could therefore argue that correct pricing of these underlying assets is a prerequisite for accurate valuation of derivatives.

The methods we discuss are closely related to control variates, which should not be surprising since we noted (in Example  $4.1.1$ ) that underlying assets often provide convenient controls. There is also a link with stratified sampling: stratification with proportional allocation ensures that the sample means of the stratum indicator functions coincide with their population means. We develop two types of methods: *moment matching* based on transformations of simulated paths, and methods that weight (but do not transform) paths in order to match moments. When compared with control variates or with each other, these methods may produce rather different small-sample properties while becoming equivalent as the number of samples grows. This makes it difficult to compare estimators on theoretical grounds.

## 4.5.1 Moment Matching Through Path Adjustments

The idea of transforming paths to match moments is most easily introduced in the setting of a single underlying asset  $S(t)$  simulated under a risk-neutral measure in a model with constant interest rate  $r$ . If the asset pays no dividends, we know that  $E[S(t)] = e^{rt}S(0)$ . Suppose we simulate n independent copies  $S_1, \ldots, S_n$  of the process and define the sample mean process

$$\bar{S}(t) = \frac{1}{n} \sum_{i=1}^{n} S_i(t).$$

For finite n, the sample mean will not in general coincide with  $E[S(t)]$ ; the simulation could be said to misprice the underlying asset in the sense that

$$e^{-rt}\bar{S}(t) \neq S(0),\tag{4.59}$$

the right side being the current price of the asset and the left side its simulation estimate.

A possible remedy is to transform the simulated paths by setting

$$\tilde{S}_{i}(t) = S_{i}(t) \frac{\mathsf{E}[S(t)]}{\bar{S}(t)}, \quad i = 1, \dots, n,$$
(4.60)

 $\text{or}$ 

$$\bar{S}_i(t) = S_i(t) + \mathsf{E}[S(t)] - \bar{S}(t), \quad i = 1, \dots, n,$$
(4.61)

and then using the  $\tilde{S}_i$  rather than the  $S_i$  to price derivatives. Using either the multiplicative adjustment  $(4.60)$  or the additive adjustment  $(4.61)$  ensures that the sample mean of  $\tilde{S}_1(t), \ldots, \tilde{S}_n(t)$  exactly equals  $\mathsf{E}[S(t)].$ 

These and related transformations are proposed and tested in Barraquand [37], Boyle et al. [53], and Duan and Simonato [96]. Duan and Simonato call

 $(4.60)$  empirical martingale simulation; Boyle et al. use the name moment *matching*. In other application domains, Hall [164] analyzes a related cen*tering* technique for bootstrap simulation and Gentle [136] refers briefly to constrained sampling. In many settings, making numerical adjustments to samples seems unnatural — some discrepancy between the sample and population mean is to be expected, after all. In the financial context, the error in  $(4.59)$  could be viewed as exposing the user to arbitrage through mispricing and this might justify attempts to remove the error completely.

A further consequence of matching the sample and population mean of the underlying asset is a finite-sample form of *put-call parity*. The algebraic identity

$$(a - b)^{+} - (b - a)^{+} = a - b$$

implies the constraint

Шe,

$$e^{-rT}\mathsf{E}[(S(T)-K)^{+}] - e^{-rT}\mathsf{E}[(K-S(T))^{+}] = S(0) - e^{-rT}K$$

on the values of a call, a put, and the underlying asset. Any adjustment that equates the sample mean of  $\tilde{S}_1(T), \ldots, \tilde{S}_n(T)$  to  $\mathsf{E}[S(T)]$  ensures that

$$e^{-rT}\frac{1}{n}\sum_{i=1}^{n}(\tilde{S}_{i}(T)-K)^{+}-e^{-rT}\frac{1}{n}\sum_{i=1}^{n}(K-\tilde{S}_{i}(T))^{+}=S(0)-e^{-rT}K.$$

This, too, may be viewed as a type of finite-sample no-arbitrage condition.

Of  $(4.60)$  and  $(4.61)$ , the multiplicative adjustment  $(4.60)$  seems preferable on the grounds that it preserves positivity whereas the additive adjustment  $(4.61)$  can make some  $\tilde{S}_i$  negative even if  $S_1(t), \ldots, S_n(t), \mathsf{E}[S(t)]$  are all positive. However, we get  $\mathsf{E}[\tilde{S}_i(t)] = \mathsf{E}[S(t)]$  using (4.61) but not with (4.60). Indeed,  $(4.61)$  even preserves the martingale property in the sense that

$$\mathsf{E}[e^{-r(T-t)}\tilde{S}_i(T)|\tilde{S}_i(u), 0 \le u \le t] = \tilde{S}_i(t).$$

Both (4.60) and (4.61) change the law of the simulated process  $(S_i(t)$  and  $S_i(t)$ will not in general have the same distribution) and thus typically introduce some bias in estimates computed from the adjusted paths. This bias vanishes as the sample size n increases and is typically  $O(1/n)$ .

## Large-Sample Properties

There is some similarity between the transformations in  $(4.60)$  and  $(4.61)$  and the nonlinear control variates discussed in Section 4.1.4. The current setting does not quite fit the formulation in Section 4.1.4 because the adjustments here affect individual observations and not just their means.

To extend the analysis in Section 4.1.4, we formulate the problem as one of estimating  $\mathsf{E}[h_1(X)]$  with X taking values in  $\Re^d$  and  $h_1$  mapping  $\Re^d$  into  $\Re.$  For example, we might have  $X = S(T)$  and  $h_1(x) = e^{-rT}(x-K)^+$  in the

case of pricing a standard call option. The moment matching estimator has  $\text{the form}$ 

$$\frac{1}{n}\sum_{i=1}^{n}h(X_i,\bar{X})$$

with  $X_1,\ldots,X_n$  i.i.d. and  $\bar{X}$  their sample mean. The function h is required to satisfy  $h(x,\mu_X) = h_1(x)$  with  $\mu_X = \mathsf{E}[X]$ . It is easy to see that an estimator of the form

$$e^{-rT}\frac{1}{n}\sum_{i=1}^{n}(\tilde{S}_{i}(T)-K)^{+},$$

with  $\tilde{S}_i$  as in (4.60) or (4.61), fits in this framework. Notice, also, that by including in the vector  $X$  powers of other components of  $X$ , we make this formulation sufficiently general to include matching higher-order moments as well as the mean.

Suppose now that  $h(X_i, \cdot)$  is almost surely continuously differentiable in a neighborhood of  $\mu_X$ . Then

$$\frac{1}{n}\sum_{i=1}^{n}h(X_i,\bar{X}) \approx \frac{1}{n}\sum_{i=1}^{n}h_1(X_i) + \frac{1}{n}\sum_{i=1}^{n}\nabla_{\mu}h(X_i,\mu_X)[\bar{X} - \mu_X],\qquad(4.62)$$

with  $\nabla_{\mu}h$  denoting the gradient of h with respect to its second argument. Because  $\bar{X} \to \mu_X$ , this approximation becomes increasingly accurate as n increases. This suggests that, asymptotically in  $n$ , the moment matching estimator is equivalent to a control variate estimator with control  $\bar{X}$  and  $\text{coefficient vector}$ 

$$b_n^{\top} = \frac{1}{n} \sum_{i=1}^n \nabla_{\mu} h(X_i, \mu_X) \to \mathsf{E} \left[ \nabla_{\mu} h(X, \mu_X) \right]. \tag{4.63}$$

Some specific results in this direction are established in Duan, Gauthier, and Simonato [97] and Hall [164]. However, even under conditions that make this argument rigorous, the moment matching estimator may perform either better or worse in small samples than the approximating control variate estimator.

The dependence among the observations  $h(X_i, \bar{X}), i = 1, \ldots, n$ , introduced through use of a common sample mean  $\bar{X}$  complicates output analysis. One approach proceeds as though the approximation in  $(4.62)$  held exactly and estimates a confidence interval the way one would with a linear control variate (cf. Sections 4.1.1 and 4.1.3). An alternative is to generate  $k$  independent batches, each of size  $m$ , and to apply moment matching separately to each batch of  $m$  paths. A confidence interval can then be formed from the sample mean and sample standard deviation of the  $k$  means computed from the  $k$ batches. As with stratified sampling or Latin hypercube sampling, the cost of batching lies in foregoing potentially greater variance reduction by applying the method to all  $km$  paths.

## Examples

 $\mathbb{C}^{\mathbb{Z}}$ 

F

We turn now to some more specific examples of moment matching transformations.

**Example 4.5.1** Brownian motion and geometric Brownian motion. In the case of a standard one-dimensional Brownian motion  $W$ , the additive transformation

$$\tilde{W}_i(t) = W_i(t) - \bar{W}(t)$$

seems the most natural way to match the sample and population means there is no reason to try to avoid negative values of  $W_i$ , and the mean of a normal distribution is a location parameter. The transformation

$$\tilde{W}_i(t) = \frac{W_i(t) - \bar{W}(t)}{s(t)/\sqrt{t}},\tag{4.64}$$

with  $s(t)$  the sample standard deviation of  $W_1(t), \ldots, W_n(t)$ , matches both first and second moments. But for this it seems preferable to scale the increments of the Brownian motion: with

$$W_i(t_k) = \sum_{j=1}^{k} \sqrt{t_j - t_{j-1}} Z_{ij}$$

and  $\{Z_{ij}\}$  independent  $N(0,1)$  random variables, set

$$\bar{Z}_j = \frac{1}{n} \sum_{i=1}^n Z_{ij}, \quad s_j^2 = \frac{1}{n-1} \sum_{i=1}^n \left( Z_{ij} - \bar{Z}_j \right)^2$$

and

$$\tilde{W}_i(t_k) = \sum_{j=1}^k \sqrt{t_j - t_{j-1}} \frac{Z_{ij} - \bar{Z}_j}{s_j}.$$

This transformation preserves the independence of increments whereas  $(4.64)$  $\text{does not.}$ 

For geometric Brownian motion  $S \sim \text{GBM}(r, \sigma^2)$ , the multiplicative transformation  $(4.60)$  is more natural. It reduces to

$$\tilde{S}_i(t) = S(0)e^{rT} \frac{ne^{\sigma W_i(t)}}{\sum_{j=1}^n e^{\sigma W_j(t)}}.$$

This transformation does not lend itself as easily to matching higher moments.

As a simple illustration, we apply these transformations to the pricing of a call option under Black-Scholes assumptions and compare results in Figure 4.9. An ordinary simulation generates replications of the terminal asset price using

$$S_i(T) = S(0) \exp\left((r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}Z_i\right), \quad i = 1, \dots, n.$$

Method Z1 replaces each  $Z_i$  with  $Z_i - \bar{Z}$  and method Z2 uses  $(Z_i - \bar{Z})/s$ , with  $\bar{Z}$  the sample mean and s the sample standard deviation of  $Z_1,\ldots,Z_n$ . Methods SM and SA use the multiplicative and additive adjustments  $(4.60)$ and (4.61). Method CV uses  $\bar{S}$  as a control variate with the optimal coefficient estimated as in  $(4.5)$ .

Figure 4.9 compares estimates of the absolute bias and standard error for these methods in small samples of size  $n = 16, 64, 256$ , and 1024. The model parameters are  $S(0) = K = 50, r = 5\%, \sigma = 0.30$ , and the option expiration is  $T = 1$ . The results are based on 5000 replications of each sample size. The graphs in Figure 4.9 are on log-log scales; the slopes in the top panel are consistent with a  $O(1/n)$  bias for each method and those in the bottom panel are consistent with  $O(1/\sqrt{n})$  standard errors. Also, the biases are about an order of magnitude smaller than the standard errors.

In this example, the control variate estimator has the highest bias  $-$  recall that bias in this method results from estimation of the optimal coefficient though the bias is quite small at  $n = 1024$ . Interestingly, the standard errors for the CV and SM methods are virtually indistinguishable. This suggests that the implicit coefficient  $(4.63)$  in the linear approximation to the multiplicative adjustment coincides with the optimal coefficient. The CV and SM methods achieve somewhat smaller standard errors than SA and Z1, which may be considered suboptimal control variate estimators. The lowest variance is attained by  $Z2$ , but because this method adjusts both a sample mean and a sample variance, it should be compared with a control variate estimator using two controls. (Compared with ordinary simulation, the Z2 reduces variance by a factor of about 40; the other methods reduce variance by factors ranging from about  $3 \text{ to } 7.$ 

These results suggest that moment matching estimators are indeed closely related to control variate estimators. They can sometimes serve as an indirect way of implementing a control, potentially providing much of the variance reduction while reducing small-sample bias. Though we observe this in Figure 4.9, there is of course no guarantee that the same would hold in other examples.  $\Box$ 

**Example 4.5.2** Short rate models. We consider, next, finite-sample adjustments to short rate processes with the objective of matching bond prices. We begin with an idealized setting of continuous-time simulation of a short rate process  $r(t)$  under the risk-neutral measure. From independent replications  $r_1,\ldots,r_n$  of the process, suppose we can compute estimated bond prices

$$\bar{B}(0,T) = \frac{1}{n} \sum_{i=1}^{n} \exp\left(-\int_{0}^{T} r_i(t) dt\right). \tag{4.65}$$

From these we define empirical forward rates

![](_page_64_Figure_1.jpeg)

Fig. 4.9. Bias (top) and standard error (bottom) versus sample size in pricing a standard call option under Black-Scholes assumptions. The graphs compare moment matching based on the mean of  $Z_i$  (Z1), the mean and standard deviation of  $Z_i$  (Z2), multiplicative (SM) and additive (SA) adjustments based on  $\bar{S}$ , and an estimator using  $\bar{S}$  as linear control variate (CV).

$$\hat{f}(0,T) = -\frac{\partial}{\partial T} \log \bar{B}(0,T). \tag{4.66}$$

The model bond prices and forward rates are

$$B(0,T) = \mathsf{E}\left[\exp\left(-\int_0^T r(t) \, dt\right)\right]$$

and

ŵ,

$$f(0,T) = -\frac{\partial}{\partial T} \log B(0,T).$$

The adjustment

$$\tilde{r}_i(t) = r_i(t) + f(0, t) - \tilde{f}(0, t)$$

 $results in$ 

$$\frac{1}{n}\sum_{i=1}^{n}\exp\left(-\int_{0}^{T}\tilde{r}_{i}(t)\,dt\right) = B(0,T);$$

i.e., in exact pricing of bonds in finite samples.

Suppose, now, that we can simulate  $r$  exactly but only at discrete dates  $0 = t_0, t_1, \ldots, t_m$ , and our bond price estimates from n replications are given  $\text{bv}$ 

$$\bar{B}(0,t_m) = \frac{1}{n} \sum_{i=1}^n \exp\left(-\sum_{j=0}^{m-1} r_i(t_j)[t_{j+1}-t_j]\right).$$

The yield adjustment

$$\tilde{r}_i(t_j) = r_i(t_j) + \frac{\log \bar{B}(0, t_{j+1}) - \log \bar{B}(0, t_j)}{t_{j+1} - t_j} - \frac{\log B(0, t_{j+1}) - \log B(0, t_j)}{t_{j+1} - t_j}$$

results in

$$\frac{1}{n}\sum_{i=1}^{n}\exp\left(-\sum_{j=0}^{m-1}\tilde{r}_{i}(t_{j})[t_{j+1}-t_{j}]\right)=B(0,t_{m}).$$

In this case, the adjustment corrects for discretization error as well as sampling variability.  $\Box$ 

**Example 4.5.3**  $HJM$  framework. Consider a continuous-time HJM model of the evolution of the forward curve  $f(t,T)$ , as in Section 3.6, and suppose we can simulate independent replications  $f_1, \ldots, f_n$  of the paths of the curve. Because  $f(t, t)$  is the short rate at time t, the previous example suggests the adjustment  $\tilde{f}_i(t,t) = f_i(t,t) + f(0,t) - \hat{f}(0,t)$  with  $\hat{f}$  as in (4.66) and  $\bar{B}(0,T)$ as in (4.65) but with  $r_i(t)$  replaced by  $f_i(t,t)$ . But the HJM setting provides additional flexibility to match additional moments by adjusting other rates  $f(t,u)$ .

We know that for any  $0 < t < T$ ,

$$\mathsf{E}\left[\exp\left(-\int_0^t f(u,u)\,du - \int_t^T f(t,u)\,du\right)\right] = B(0,T);$$

this follows from the fact that discounted bond prices are martingales and is nearly the defining property of the HJM framework. We choose  $f$  to enforce the finite-sample analog of this property, namely

$$\frac{1}{n}\sum_{i=1}^{n}\exp\left(-\int_{0}^{t}\tilde{f}_{i}(u,u)\,du-\int_{t}^{T}\tilde{f}_{i}(t,u)\,du\right)=B(0,T).$$

#### 4.5 Matching Underlying Assets 251

This is accomplished by setting

$$\tilde{f}_i(t,T) = f_i(t,T) + f(0,T) - \frac{\sum_{i=1}^n f_i(t,T)H_i(t,T)}{\sum_{i=1}^n H_i(t,T)},$$

with

$$H_i(t,T) = \exp\left(-\int_0^t f_i(u,u) \, du - \int_t^T f_i(t,u) \, du\right)$$

In practice, one would simulate on a discrete grid of times and maturities as explained in Section  $3.6.2$  and this necessitates some modification. However, using the discretization in Section  $3.6.2$ , the discrete discounted bond prices are martingales and thus lend themselves to a similar adjustment.  $\Box$ 

**Example 4.5.4** Normal random vectors. For i.i.d. normal random vectors, centering by the sample mean is equivalent to sampling *conditional* on the sample mean equaling the population mean. To see this, let  $X_1,\ldots,X_n$  be independent  $N(\mu, \Sigma)$  random vectors. The adjusted vectors

$$\tilde{X}_i = X_i - \bar{X} + \mu$$

have mean  $\mu$ ; moreover, they are jointly normal with

$$\begin{pmatrix}\n\tilde{X}_{1} \\
\vdots \\
\tilde{X}_{n}\n\end{pmatrix} \sim N \left( \begin{pmatrix}\n\mu \\
\vdots \\
\mu\n\end{pmatrix}, \begin{pmatrix}\n(n-1)\Sigma/n & -\Sigma/n & \dots & -\Sigma/n \\
-\Sigma/n & (n-1)\Sigma/n & \vdots \\
\vdots & \ddots & -\Sigma/n \\
-\Sigma/n & -\Sigma/n & (n-1)\Sigma/n\n\end{pmatrix} \right),$$

as can be verified using the Linear Transformation Property  $(2.23)$ . But this is also the joint distribution of  $X_1,\ldots,X_n$  given  $\bar{X}=\mu$ , as can be verified using the Conditioning Formula  $(2.25)$ .  $\Box$ 

## 4.5.2 Weighted Monte Carlo

An alternative approach to matching underlying prices in finite samples assigns weights to the paths instead of shifting them. The weights are chosen to equate weighted averages over the paths to the corresponding population means.

Consider, again, the setting surrounding  $(4.59)$  with which we introduced the idea of moment matching. Suppose we want to price an option on the underlying asset  $S(t)$ ; we note that the simulation misprices the underlying asset in finite samples in the sense that the sample mean  $\bar{S}(t)$  deviates from  $e^{rt}S(0)$ . Rather than change the simulated values  $S_1(t),\ldots,S_n(t)$ , we may choose weights  $w_1, \ldots, w_n$  satisfying

$$\sum^{n} w_i S_i(t) = e^{rt} S(0),$$

and then use these same weights in estimating the expected payoff of an option. For example, this yields the estimate

$$e^{-rt} \sum_{i=1}^{n} w_i (S_i(t) - K)^+$$

for the price of a call struck at  $K$ .

The method can be formulated more generically as follows. Suppose we want to estimate  $\mathsf{E}[Y]$  and we know the mean vector  $\mu_X = \mathsf{E}[X]$  for some random  $d$ -vector  $X$ . For example,  $X$  might record the prices of underlying assets at future dates, powers of those prices, or the discounted payoffs of tractable options. Suppose we know how to simulate i.i.d. replications  $(X_i, Y_i)$ ,  $i = 1, \ldots, n$ , of the pair  $(X, Y)$ . In order to match the known mean  $\mu_X$  in finite samples, we choose weights  $w_1, \ldots, w_n$  satisfying

$$\sum_{i=1}^{n} w_i X_i = \mu_X \tag{4.67}$$

and then use

$$\sum_{i=1}^{n} w_i Y_i \tag{4.68}$$

to estimate  $E[Y]$ . We may also want to require that the weights sum to 1:

$$\sum_{i=1}^{n} w_i = 1. \tag{4.69}$$

We can include this in (4.67) by taking one of the components of the  $X_i$  to be identically equal to  $1$ .

The number of constraints  $d$  is typically much smaller than the number of replications n, so  $(4.67)$  does not determine the weights. We choose a particular set of weights by selecting an objective function  $H: \mathbb{R}^d \to \mathbb{R}$  and solving the constrained optimization problem

$$\min H(w_1, \dots, w_n) \quad \text{subject to (4.67).} \tag{4.70}$$

Because the replications are i.i.d., it is natural to restrict attention to functions H that are convex and symmetric in  $w_1, \ldots, w_n$ ; the criterion in (4.70) then penalizes deviations from uniformity in the weights.

An approach of this type was proposed by Avellaneda et al.  $[26, 27]$ , but more as a mechanism for model correction than variance reduction. In their setting, the constraint (4.67) uses a vector  $\mu_o$  (to be interpreted as market prices) different from  $\mu_X$  (the model prices). The weights thus serve to calibrate an imperfect model to the observed market prices of actively traded instruments in order to more accurately price a less liquid instrument. Broadie,

Glasserman, and Ha  $[68]$  use a related technique for pricing American options; we return to this in Chapter 8. It should be evident from the discussion leading to  $(4.68)$  and  $(4.70)$  that there is a close connection between this approach and using  $X$  as a control variate; we make the connection explicit in Example  $4.5.6$ . First we treat the objective considered by Avellaneda et al.  $[26, 27].$ 

**Example 4.5.5** Maximum entropy weights. A particularly interesting and in some respects convenient objective  $H$  is the (negative) entropy function

$$H(w_1,\ldots,w_n) = \sum_{i=1}^n w_i \log w_i,$$

which we take to be  $+\infty$  if any  $w_i$  is negative. (By convention,  $0 \cdot \log 0 = 0$ .) Using this objective will always produce positive weights, provided there is a positive feasible solution to  $(4.67)$ . Such a solution exists whenever the convex hull of the points  $X_1,\ldots,X_n$  contains  $\mu_X$ , and this almost surely occurs for sufficiently large  $n$ .

We can solve for the optimal weights by first forming the Lagrangian

$$\sum_{i=1}^{n} w_i \log w_i - \nu \sum_{i=1}^{n} w_i - \lambda^{\top} \sum_{i=1}^{n} w_i X_i.$$

Here,  $\nu$  is a scalar and  $\lambda$  is a d-vector. For this objective it turns out to be convenient to separate the constraint on the weight sum, as we have here. Setting the derivative with respect to  $w_i$  equal to zero and solving for  $w_i$ yields

$$w_i = e^{\nu - 1} \exp(\lambda^\top X_i).$$

Constraining the weights to sum to unity yields

$$w_i = \frac{\exp(\lambda^\top X_i)}{\sum_{j=1}^n \exp(\lambda^\top X_j)}.\tag{4.71}$$

The vector  $\lambda$  is then determined by the condition

$$\frac{\sum_{i=1}^{n} e^{\lambda^{\top} X_i} X_i}{\sum_{i=1}^{n} e^{\lambda^{\top} X_i}} = \mu_X,$$

which can be solved numerically.

Viewed as a probability distribution on  $\{X_1,\ldots,X_n\}$ , the  $(w_1,\ldots,w_n)$ in  $(4.71)$  corresponds to an *exponential change of measure* applied to the uniform distribution  $(1/n, \ldots, 1/n)$ , in a sense to be further developed in Section 4.6. The solution in  $(4.71)$  may be viewed as the minimal adjustment to the uniform distribution needed to satisfy the constraints  $(4.67)$ – $(4.69)$ .  $\Box$ 

**Example 4.5.6** Least-squares weights. The simplest objective to consider in  $(4.70)$  is the quadratic

$$H(w_1,\ldots,w_n) = \frac{1}{2}w^{\top}w,$$

with w the vector of weights  $(w_1,\ldots,w_n)^\top$ . We will show that the estimator  $w^{\top}Y = \sum w_i Y_i$  produced by these weights is identical to the control variate estimator  $\bar{Y}(b_n)$  defined by (4.16).

Define an  $n \times (d+1)$  matrix A whose *i*th row is  $(1, X_i^{\top} - \mu_X^{\top})$ . (Here we assume that  $X_1, \ldots, X_n$  do not contain an entry identically equal to 1.) Constraints (4.67)-(4.69) can be expressed as  $w^{\top}A = (1, 0)$ , where **0** is a row vector of  $d$  zeros. The Lagrangian becomes

$$\frac{1}{2}w^{\top}w + w^{\top}A\lambda$$

with  $\lambda \in \Re^d$ . The first-order conditions are  $w = -A\lambda$ . From the constraint  $\text{we get}$ 

$$(1, \mathbf{0}) = w^{\top} A = -\lambda^{\top} A^{\top} A \Rightarrow -\lambda^{\top} = (1, \mathbf{0})(A^{\top} A)^{-1}$$
$$\Rightarrow w^{\top} = (1, \mathbf{0})(A^{\top} A)^{-1} A^{\top},$$

assuming the matrix  $A$  has full rank. The weighted Monte Carlo estimator of the expectation of the  $Y_i$  is thus

$$w^{\top}Y = (1, \mathbf{0})(A^{\top}A)^{-1}A^{\top}Y, \quad Y = (Y_1, \dots, Y_n)^{\top}.$$
 (4.72)

The control variate estimator is the first entry of the vector  $\beta \in \Re^{d+1}$  that  $\text{solves}$ 

$$\min_{\beta} \frac{1}{2} (Y - A\beta)^{\top} (Y - A\beta);$$

i.e., it is the value fitted at  $(1, \mu_X)$  in a regression of the  $Y_i$  against the rows of A. From the first-order conditions  $(Y - A\beta)^{\top} A = 0$ , we find that the optimal  $\beta$  is  $(A^{\top}A)^{-1}A^{\top}Y$ . The control variate estimator is therefore

$$(1, \mathbf{0})\beta = (1, \mathbf{0})(A^{\top}A)^{-1}A^{\top}Y,$$

which coincides with  $(4.72)$ . When written out explicitly, the weights in  $(4.72)$ take precisely the form displayed in  $(4.20)$ , where we first noted the interpretation of a control variate estimator as a weighted Monte Carlo estimator.  $\Box$ 

This link between the general strategy in  $(4.68)$  and  $(4.70)$  for constructing "moment-matched" estimators and the more familiar method of control variates suggests that  $(4.68)$  provides at best a small refinement of the control variate estimator. As the sample size  $n$  increases, the refinement typically vanishes and using knowledge of  $\mu_X$  as a constraint in (4.67) becomes equivalent to using it in a control variate estimator. A precise result to this effect is proved in Glasserman and Yu  $[147]$ . This argues in favor of using control variate estimators rather than  $(4.68)$ , because they are easier to implement and because more is known about their sampling properties.

## 4.6 Importance Sampling

## 4.6.1 Principles and First Examples

*Importance sampling* attempts to reduce variance by changing the probability measure from which paths are generated. Changing measures is a standard tool in financial mathematics; we encountered it in our discussion of pricing principles in Section  $1.2.2$  and several places in Chapter 3 in the guise of changing numeraire. Appendix B.4 reviews some of the underlying mathematical theory. When we switch from, say, the objective probability measure to the risk-neutral measure, our goal is usually to obtain a more convenient representation of an expected value. In importance sampling, we change measures to try to give more weight to "important" outcomes thereby increasing sampling efficiency.

To make this idea concrete, consider the problem of estimating

$$\alpha = \mathsf{E}[h(X)] = \int h(x)f(x) \, dx$$

where X is a random element of  $\Re^d$  with probability density f, and h is a function from  $\mathbb{R}^d$  to  $\mathbb{R}$ . The ordinary Monte Carlo estimator is

$$\hat{\alpha} = \hat{\alpha}(n) = \frac{1}{n} \sum_{i=1}^{n} h(X_i)$$

with  $X_1,\ldots,X_n$  independent draws from f. Let g be any other probability density on  $\Re^d$  satisfying

$$f(x) > 0 \Rightarrow g(x) > 0 \tag{4.73}$$

for all  $x \in \mathbb{R}^d$ . Then we can alternatively represent  $\alpha$  as

$$\alpha = \int h(x) \frac{f(x)}{g(x)} g(x) \, dx.$$

This integral can be interpreted as an expectation with respect to the density  $g$ ; we may therefore write

$$\alpha = \tilde{\mathsf{E}}\left[h(X)\frac{f(X)}{g(X)}\right],\tag{4.74}$$

 $\hat{\mathsf{E}}$  here indicating that the expectation is taken with X distributed according to g. If  $X_1, \ldots, X_n$  are now independent draws from g, the importance sampling estimator associated with  $q$  is

$$\hat{\alpha}_g = \hat{\alpha}_g(n) = \frac{1}{n} \sum_{i=1}^n h(X_i) \frac{f(X_i)}{g(X_i)}.$$
(4.75)

The weight  $f(X_i)/g(X_i)$  is the likelihood ratio or Radon-Nikodym derivative evaluated at  $X_i$ .

It follows from (4.74) that  $\tilde{\mathsf{E}}[\hat{\alpha}_g] = \alpha$  and thus that  $\hat{\alpha}_g$  is an unbiased estimator of  $\alpha$ . To compare variances with and without importance sampling it therefore suffices to compare second moments. With importance sampling, we have

$$\tilde{\mathsf{E}}\left[\left(h(X)\frac{f(X)}{g(X)}\right)^2\right] = \mathsf{E}\left[h(X)^2\frac{f(X)}{g(X)}\right]$$

This could be larger or smaller than the second moment  $\mathsf{E}[h(X)^2]$  without importance sampling; indeed, depending on the choice of  $q$  it might even be *infinitely* larger or smaller. Successful importance sampling lies in the art of selecting an effective importance sampling density  $q$ .

Consider the special case in which h is nonnegative. The product  $h(x)f(x)$ is then also nonnegative and may be normalized to a probability density. Suppose  $q$  is this density. Then

$$g(x) \propto h(x)f(x), \tag{4.76}$$

and  $h(X_i)f(X_i)/g(X_i)$  equals the constant of proportionality in (4.76) regardless of the value of  $X_i$ ; thus, the importance sampling estimator  $\hat{\alpha}_g$  in (4.75) provides a *zero-variance* estimator in this case. Of course, this is useless in practice: to normalize  $h \cdot f$  we need to divide it by its integral, which is  $\alpha$ ; the zero-variance estimator is just  $\alpha$  itself.

Nevertheless, this optimal choice of  $q$  does provide some useful guidance: in designing an effective importance sampling strategy, we should try to sample in proportion to the product of h and f. In option pricing applications, h is typically a discounted payoff and  $f$  is the risk-neutral density of a discrete path of underlying assets. In this case, the "importance" of a path is measured by the product of its discounted payoff and its probability density.

If  $h$  is the indicator function of a set, then the optimal importance sampling density is the original density conditioned on the set. In more detail, suppose  $h(x) = \mathbf{1}\{x \in A\}$  for some  $A \subset \Re^d$ . Then  $\alpha = P(X \in A)$  and the zero-variance importance sampling density  $h(x)f(x)/\alpha$  is precisely the conditional density of X given  $X \in A$  (assuming  $\alpha > 0$ ). Thus, in applying importance sampling to estimate a probability, we should look for an importance sampling density that approximates the conditional density. This means choosing  $g$  to make the event  $\{X \in A\}$  more likely, especially if A is a rare set under f.

## Likelihood Ratios

In our discussion thus far we have assumed, for simplicity, that X is  $\Re^d$ -valued, but the ideas extend to  $X$  taking values in more general sets. Also, we have assumed that X has a density  $f$ , but the same observations apply if  $f$  is a probability mass function (or, more generally, a density with respect to some reference measure on  $\mathbb{R}^d$ , possibly different from Lehesgue measure)

For option pricing applications, it is natural to think of  $X$  as a discrete path of underlying assets. The density of a path (if one exists) is ordinarily not specified directly, but rather built from more primitive elements. Consider, for example, a discrete path  $S(t_i)$ ,  $i = 0, 1, \ldots, m$ , of underlying assets or state variables, and suppose that this process is Markov. Suppose the conditional distribution of  $S(t_i)$  given  $S(t_{i-1}) = x$  has density  $f_i(x, \cdot)$ . Consider a change of measure under which the transition densities  $f_i$  are replaced with transition densities  $q_i$ . The likelihood ratio for this change of measure is

$$\prod_{i=1}^{m} \frac{f_i(S(t_{i-1}), S(t_i))}{g_i(S(t_{i-1}), S(t_i))}.$$

More precisely, if  $E$  denotes expectation under the original measure and  $\tilde{E}$ denotes expectation under the new measure, then

$$\mathsf{E}[h(S(t_1),\ldots,S(t_m))] = \tilde{\mathsf{E}}\left[h(S(t_1),\ldots,S(t_m))\prod_{i=1}^m \frac{f_i(S(t_{i-1}),S(t_i))}{g_i(S(t_{i-1}),S(t_i))}\right],\tag{4.77}$$

for all functions  $h$  for which the expectation on the left exists and is finite.

Here we have implicitly assumed that  $S(t_0)$  is a constant. More generally, we could allow it to have density  $f_0$  under the original measure and density  $g_0$  under the new measure. This would result in an additional factor of  $f_0(S(t_0))/g(S(t_0))$  in the likelihood ratio.

We often simulate a path  $S(t_0), \ldots, S(t_m)$  through a recursion of the form

$$S(t_{i+1}) = G(S(t_i), X_{i+1}), \tag{4.78}$$

driven by i.i.d. random vectors  $X_1, X_2, \ldots, X_m$ . Many of the examples considered in Chapter 3 can be put in this form. The  $X_i$  will often be normally distributed, but for now let us simply assume they have common density  $f$ . If we apply a change of measure that preserves the independence of the  $X_i$  but changes their common density to  $q$ , then the corresponding likelihood ratio is

$$\prod_{i=1}^{m} \frac{f(X_i)}{g(X_i)}$$

This means that

$$\mathsf{E}[h(S(t_1), \dots, S(t_m))] = \tilde{\mathsf{E}}\left[h(S(t_1), \dots, S(t_m)) \prod_{i=1}^m \frac{f(X_i)}{g(X_i)}\right],\tag{4.79}$$

where, again,  $E$  and  $E$  denote expectation under the original and new measures, respectively, and the expectation on the left is assumed finite. Equation  $(4.79)$  relies on the fact that  $S(t_1), \ldots, S(t_m)$  are functions of  $X_1, \ldots, X_m$ .

### Random Horizon

Identities (4.77) and (4.79) extend from a fixed number of steps m to a random number of steps, provided the random horizon is a stopping time. We demonstrate this in the case of i.i.d. inputs, as in (4.79). For each  $n = 1, 2, \ldots$ let  $h_n$  be a function of n arguments and suppose we want to estimate

$$\mathsf{E}[h_N(S(t_1),\ldots,S(t_N))],\tag{4.80}$$

with N a random variable taking values in  $\{1, 2, \ldots\}$ . For example, in the case of a barrier option with barrier  $b$ , we might define  $N$  to be the index of the smallest  $t_i$  for which  $S(t_i) > b$ , taking  $N = m$  if all  $S(t_0), \ldots, S(t_m)$  lie below the barrier. We could then express the discounted payoff of an up-and-out put as  $h_N(S(t_1), \ldots, S(t_N))$  with

$$h_n(S(t_1),\ldots,S(t_n)) = \begin{cases} e^{-rt_m}(K-S(t_m))^+, \ n=m; \\ 0, \qquad \qquad n=0,1,\ldots,m-1. \end{cases}$$

The option price then has the form  $(4.80)$ .

Suppose that  $(4.78)$  holds and, as before, E denotes expectation when the  $X_i$  are i.i.d. with density f and  $\hat{\mathsf{E}}$  denotes expectation when they are i.i.d. with density g. For concreteness, suppose that  $S(t_0)$  is fixed under both measures. Let N be a stopping time for the sequence  $X_1, X_2, \ldots$ ; for example, N could be a stopping time for  $S(t_1), S(t_2), \ldots$  as in the barrier option example. Then

$$\mathsf{E}[h_N(S(t_1),\ldots,S(t_N))\mathbf{1}\{N<\infty\}]$$
  
=  $\tilde{\mathsf{E}}\left[h_N(S(t_1),\ldots,S(t_N))\prod_{i=1}^N\frac{f(X_i)}{g(X_i)}\mathbf{1}\{N<\infty\}\right],$ 

provided the expectation on the left is finite. This identity (sometimes called Wald's identity or the fundamental identity of sequential analysis  $-$  see, e.g., Asmussen  $[20]$ ) is established as follows:

$$\begin{split} &\mathsf{E}[h_N(S(t_1), \dots, S(t_N)) \mathbf{1}\{N < \infty\}] \\ &= \sum_{n=1}^{\infty} \mathsf{E}[h_n(S(t_1), \dots, S(t_n)) \mathbf{1}\{N = n\}] \\ &= \sum_{n=1}^{\infty} \tilde{\mathsf{E}} \left[ h_n(S(t_1), \dots, S(t_n)) \mathbf{1}\{N = n\} \prod_{i=1}^{n} \frac{f(X_i)}{g(X_i)} \right] \\ &= \tilde{\mathsf{E}} \left[ h_N(S(t_1), \dots, S(t_N)) \prod_{i=1}^{N} \frac{f(X_i)}{g(X_i)} \mathbf{1}\{N < \infty\} \right]. \end{split} \tag{4.81}$$

The second equality uses the stopping time property: because  $N$  is a stopping time the event  $\{N = n\}$  is determined by  $X_1, \ldots, X_n$  and this allows us to apply  $(4.79)$  to each term in the infinite sum. It is entirely possible for the event  $\{N < \infty\}$  to have probability 1 under one of the measures but not the other; we will see an example of this in Example  $4.6.3$ .

## Long Horizon

We continue to consider two probability measures under which random vectors  $X_1, X_2, \ldots$  are i.i.d., P giving the  $X_i$  density  $f, \tilde{P}$  giving them density  $g$ .

It should be noted that even if  $f$  and  $g$  are mutually absolutely continuous, the probability measures  $P$  and  $\tilde{P}$  will not be. Rather, absolute continuity holds for the restrictions of these measures to events defined by a finite initial segment of the infinite sequence. For  $A \subseteq \mathbb{R}^d$ , the event

$$\left\{\lim_{m\to\infty}\frac{1}{m}\sum_{i=1}^{m}\mathbf{1}\{X_{i}\in A\}=\int_{A}f(x)\,dx\right\}$$

has probability 1 under  $P$ ; but some such event must have probability 0 under  $\hat{P}$  unless f and g are equal almost everywhere. In short, the strong law of large numbers forces  $P$  and  $\hat{P}$  to disagree about which events have probability 0.

This collapse of absolute continuity in the limit is reflected in the somewhat pathological behavior of the likelihood ratio as the number of terms grows, through an argument from Glynn and Iglehart [157]. Suppose that

$$\tilde{\mathsf{E}}\left[|\log(f(X_1)/g(X_1))|\right] < \infty;$$

then the strong law of large numbers implies that

$$\frac{1}{m} \sum_{i=1}^{m} \log(f(X_i)/g(X_i)) \to \tilde{\mathsf{E}}\left[\log(f(X_1)/g(X_1))\right] \equiv c \tag{4.82}$$

with probability 1 under  $\tilde{P}$ . By Jensen's inequality,

$$c \leq \log \tilde{\mathsf{E}}[f(X_1)/g(X_1)] = \log \int \frac{f(x)}{g(x)} g(x) dx = 0,$$

with strict inequality unless  $\tilde{P}(f(X_1) = g(X_1)) = 1$  because log is strictly concave. But if  $c < 0$ , (4.82) implies

$$\sum_{i=1}^{m} \log(f(X_i)/g(X_i)) \to -\infty;$$

exponentiating, we find that

$$\prod_{i=1}^{m} \frac{f(X_i)}{g(X_i)} \to 0$$

with  $\tilde{P}$ -probability 1. Thus, the likelihood ratio converges to 0 though its expectation equals 1 for all  $m$ . This indicates that the likelihood ratio becomes highly skewed, taking increasingly large values with small but non-negligible probability. This in turn can result in a large increase in variance if the change of measure is not chosen carefully.

## Output Analysis

An importance sampling estimator does not introduce dependence between replications and is just an average of i.i.d. replications. We can therefore supplement an importance sampling estimator with a large-sample confidence interval in the usual way by calculating the sample standard deviation across replications and using it in  $(A.6)$ . Because likelihood ratios are often highly skewed, the sample standard deviation will often underestimate the true standard deviation, and a very large sample size may be required for confidence intervals based on the central limit theorem to provide reasonable coverage. These features should be kept in mind in comparing importance sampling estimators based on estimates of their standard errors.

## Examples

**Example 4.6.1** Normal distribution: change of mean. Let  $f$  be the univariate standard normal density and g the univariate normal density with mean  $\mu$  and variance 1. Then simple algebra shows that

$$\prod_{i=1}^{m} \frac{f(Z_i)}{g(Z_i)} = \exp\left(-\mu \sum_{i=1}^{m} Z_i + \frac{m}{2}\mu^2\right).$$

A bit more generally, if we let  $g_i$  have mean  $\mu_i$ , then

$$\prod_{i=1}^{m} \frac{f(Z_i)}{g_i(Z_i)} = \exp\left(-\sum_{i=1}^{m} \mu_i Z_i + \frac{1}{2} \sum_{i=1}^{m} \mu_i^2\right). \tag{4.83}$$

If we simulate Brownian motion on a grid  $0 = t_0 < t_1 < \cdots < t_m$  by setting

$$W(t_n) = \sum_{i=1}^{n} \sqrt{t_i - t_{i-1}} Z_i,$$

then  $(4.83)$  is the likelihood ratio for a change of measure that adds mean  $\mu_i \sqrt{t_i - t_{i-1}}$  to the Brownian increment over  $[t_{i-1}, t_i]$ .  $\Box$ 

**Example 4.6.2** Exponential change of measure. The previous example is a special case of a more general class of convenient measure transformations. For a cumulative distribution function  $F$  on  $\Re$ , define

$$\psi(\theta) = \log \int_{-\infty}^{\infty} e^{\theta x} \, dF(x).$$

This is the *cumulant generating function* of  $F$ , the logarithm of the moment generating function of F. Let  $\Theta = \{\theta : \psi(\theta) < \infty\}$  and suppose that  $\Theta$  is nonempty. For each  $\theta \in \Theta$ , set

4.6 Importance Sampling 261

$$F_{\theta}(x) = \int_{-\infty}^{x} e^{\theta u - \psi(\theta)} dF(u);$$

each  $F_{\theta}$  is a probability distribution, and  $\{F_{\theta}, \theta \in \Theta\}$  form an *exponential family* of distributions. The transformation from F to  $F_{\theta}$  is called exponential tilting, exponential twisting, or simply an exponential change of measure. If F has a density f, then  $F_{\theta}$  has density

$$f_{\theta}(x) = e^{\theta x - \psi(\theta)} f(x).$$

Suppose that  $X_1, \ldots, X_n$  are initially i.i.d. with distribution  $F = F_0$  and that we apply a change of measure under which they become i.i.d. with distribution  $F_{\theta}$ . The likelihood ratio for this transformation is

$$\prod_{i=1}^{n} \frac{dF_0(X_i)}{dF_\theta(X_i)} = \exp\left(-\theta \sum_{i=1}^{n} X_i + n\psi(\theta)\right). \tag{4.84}$$

The standard normal distribution has  $\psi(\theta) = \theta^2/2$ , from which we see that this indeed generalizes Example 4.6.1. A key feature of exponential twisting is that the likelihood ratio — which is in principle a function of all  $X_1,\ldots,X_n$ — reduces to a function of the sum of the  $X_i$ . In statistical terminology, the sum of the  $X_i$  is a *sufficient statistic* for  $\theta$ .

The cumulant generating function  $\psi$  records important information about the distributions  $F_{\theta}$ . For example,  $\psi'(\theta)$  is the mean of  $F_{\theta}$ . To see this, let  $\mathsf{E}_{\theta}$ denote expectation with respect to  $F_{\theta}$  and note that  $\psi(\theta) = \log \mathsf{E}_0[\exp(\theta X)].$ Differentiation yields

$$\psi'(\theta) = \frac{\mathsf{E}_0[Xe^{\theta X}]}{\mathsf{E}_0[e^{\theta X}]} = \mathsf{E}_0[Xe^{\theta X - \psi(\theta)}] = \mathsf{E}_{\theta}[X].$$

A similar calculation shows that  $\psi''(\theta)$  is the variance of  $F_{\theta}$ . The function  $\psi$ passes through the origin; Hölder's inequality shows that it is convex, so that  $\psi''(\theta)$  is indeed positive. For further theoretical background on exponential families see, e.g., Barndorff-Nielson [35].

We conclude with some examples of exponential families. The normal distributions  $N(\theta, \theta \sigma^2)$  form an exponential family in  $\theta$  for all  $\sigma > 0$ . The gamma densities

$$\frac{1}{\Gamma(a)\theta^a}x^{a-1}e^{-x/\theta}, \quad x \ge 0,$$

form an exponential family in  $\theta$  for each value of the shape parameter  $a > 0$ . With  $a = 1$ , this is the family of exponential distributions with mean  $\theta$ . The Poisson distributions

$$e^{-\lambda} \frac{\lambda^k}{k!}, \quad k = 0, 1, \dots,$$

form an exponential family in  $\theta = \log \lambda$ . The binomial distributions

$$\frac{n!}{k!(n-k)!}p^k(1-p)^{n-k}, \quad k = 0, 1, \dots, n,$$

form an exponential family in  $\theta = \log(p/(1-p))$ .  $\Box$ 

**Example 4.6.3** Ruin probabilities. A classic application of importance sampling arises in estimating ruin probabilities in the theory of insurance risk. Consider an insurance firm earning premiums at a constant rate  $p$  per unit of time and paying claims that arrive at the jumps of a Poisson process with rate  $\lambda$ . Letting  $N(t)$  denote the number of claims arriving in [0, t] and  $Y_i$  the size of the *i*th claim,  $i = 1, 2, \ldots$ , the net payout of the firm over  $[0, t]$  is given by

$$\sum_{i=1}^{N(t)} Y_i - pt.$$

Suppose the firm has a reserve of  $x$ ; then ruin occurs if the net payout ever exceeds  $x$ . We assume the claims are i.i.d. and independent of the Poisson process. We further assume that  $\lambda \mathsf{E}[Y_i] < p$ , meaning that premiums flow in at a faster rate than claims are paid out; this ensures that the probability of eventual ruin is less than  $1$ .

If ruin ever occurs, it must occur at the arrival of a claim. It therefore suffices to consider the discrete-time process embedded at the jumps of the Poisson process. Let  $\xi_1, \xi_2, \ldots$  be the interarrival times of the Poisson process; these are independent and exponentially distributed with mean  $1/\lambda$ . The net payout between the  $(n-1)$ th and nth claims (including the latter but not the former) is  $X_n = Y_n - p\xi_n$ . The net payout up to the *n*th claim is given by the random walk  $S_n = X_1 + \cdots + X_n$ . Ruin occurs at

$$\tau_x = \inf\{n \ge 0 : S_n > x\},\$$

with the understanding that  $\tau_x = \infty$  if  $S_n$  never exceeds x. The probability of eventual ruin is  $P(\tau_x < \infty)$ . Figure 4.10 illustrates the notation for this  $\text{example.}$ 

The particular form of the increments  $X_n$  is not essential to the problem so we generalize the setting. We assume that  $X_1, X_2, \ldots$  are i.i.d. with  $0 <$  $P(X_i > 0) < 1$  and  $\mathsf{E}[X_i] < 0$ , but we drop the specific form  $Y_n - p\xi_n$ . We add the assumption that the cumulant generating function  $\psi_X$  of the  $X_i$  (cf. Example  $4.6.2$ ) is finite in a neighborhood of the origin. This holds in the original model if the cumulant generating function  $\psi_Y$  of the claim sizes  $Y_i$  is finite in a neighborhood of the origin.

For any point  $\theta$  in the domain of  $\psi_X$ , consider the exponential change of measure with parameter  $\theta$  and let  $\mathsf{E}_{\theta}$  denote expectation under this measure. Because  $\tau_x$  is a stopping time, we may apply (4.81) to write the ruin probability  $P(\tau_x < \infty)$  as an  $\mathsf{E}_{\theta}$ -expectation. Because we have applied an exponential change of measure, the likelihood ratio simplifies as in  $(4.84)$ ; thus, the ruin probability becomes

![](_page_78_Figure_1.jpeg)

**Fig. 4.10.** Illustration of claim sizes  $Y_i$ , interarrival times  $\xi_i$ , and the random walk  $S_n$ . Ruin occurs at the arrival of the  $\tau$ th claim.

$$P(\tau_x < \infty) = \mathsf{E}_{\theta} \left[ e^{-\theta S_{\tau_x} + \psi_X(\theta)\tau_x} \mathbf{1}_{\{\tau_x < \infty\}} \right]. \tag{4.85}$$

If  $0 < \psi'_X(\theta) < \infty$  (which entails  $\theta > 0$  because  $\psi(0) = 0$  and  $\psi'(0) = 0$  $\mathsf{E}[X_n] < 0$ , then the random walk has positive drift  $\mathsf{E}_{\theta}[X_n] = \psi'_X(\theta)$  under the twisted measure, and this implies  $P_{\theta}(\tau_x < \infty) = 1$ . We may therefore omit the indicator inside the expectation on the right. It also follows that we may obtain an unbiased estimator of the ruin probability by simulating the random walk under  $P_{\theta}$  until  $\tau_x$  and returning the estimator  $\exp(-\theta S_{\tau_x} + \psi_X(\theta)\tau_x)$ . This would not be feasible under the original measure because of the positive probability that  $\tau_x = \infty$ .

Among all  $\theta$  for which  $\psi'_X(\theta) > 0$ , one is particularly effective for simulation and indeed optimal in an asymptotic sense. Suppose there is a  $\theta > 0$  at which  $\psi_X(\theta) > 0$ . There must then be a  $\theta_* > 0$  at which  $\psi_X(\theta_*) = 0$ ; convexity of  $\psi_X$  implies uniqueness of  $\theta^*$  and positivity of  $\psi'_X(\theta_*)$ , as is evident from Figure 4.11. In the insurance risk model with  $X_n = Y_n - p\xi_n$ ,  $\theta_*$  is the unique positive solution to

$$\psi_Y(\theta) + \log\left(\frac{\lambda}{\lambda + p\theta}\right) = 0$$

where  $\psi_Y$  is the cumulant generating function for the claim-size distribution.

With the parameter  $\theta_*, (4.85)$  becomes

$$P(\tau_x < \infty) = \mathsf{E}_{\theta_*} \left[ e^{-\theta_* S_{\tau_x}} \right] = e^{-\theta_* x} \mathsf{E}_{\theta_*} \left[ e^{-\theta_* (S_{\tau_x} - x)} \right].$$

Because the overshoot  $S_{\tau_x} - x$  is nonnegative, this implies the simple bound  $P(\tau_x < \infty) \leq e^{-\theta_x x}$  on the ruin probability. Under modest additional regularity conditions (for example, if the  $X_n$  have a density),  $\mathsf{E}_{\theta_*}\left[e^{-\theta_*(S_{\tau_x}-x)}\right]$ converges to a constant c as  $x \to \infty$ , providing the classical approximation

í٦.

![](_page_79_Figure_1.jpeg)

**Fig. 4.11.** Graph of a cumulant generating function  $\psi_X$ . The curve passes through the origin and has negative slope there because  $\psi'_X(0) = \mathsf{E}[X] < 0$ . At the positive root  $\theta_*$ , the slope is positive.

$$P(\tau_x < \infty) \sim ce^{-\theta_* x},$$

meaning that the ratio of the two sides converges to 1 as  $x \to \infty$ . Further details and some of the history of this approximation are discussed in Asmussen  $[20]$  and in references given there.

From the perspective of simulation, the significance of  $\theta_*$  lies in the variance reduction achieved by the associated importance sampling estimator. The unbiased estimator  $\exp(-\theta_* S_{\tau_x})$ , sampled under  $P_{\theta_*}$ , has second moment

$$\mathsf{E}_{\theta_*}\left[e^{-2\theta_*S_{\tau_x}}\right] \le e^{-2\theta_*x}.$$

By Jensen's inequality, the second moment of any unbiased estimator must be at least as large as the square of the ruin probability, and we have seen that this probability is  $O(e^{-\theta_{*}x})$ . In this sense, the second moment of the importance sampling estimator based on  $\theta_*$  is asymptotically optimal as  $x \to \infty$ .

This strategy for developing effective and even asymptotically optimal importance sampling estimators originated in Siegmund's  $[331]$  application in sequential analysis. It has been substantially generalized, particularly for queueing and reliability applications, as surveyed in Heidelberger [175].  $\Box$ 

**Example 4.6.4** A knock-in option. As a further illustration of importance sampling through an exponential change of measure, we apply the method to a down-and-in barrier option. This example is from Boyle et al. [53]. The option is a digital knock-in option with payoff

$$\mathbf{1}\{S(T) > K\} \cdot \mathbf{1}\{\min_{1 \le k \le m} S(t_k) < H\},\$$

with  $0 < t_1 < \cdots < t_m = T$ , S the underlying asset, K the strike, and H the barrier. If H is much smaller than  $S(0)$ , most naths of an ordinary simulation will result in a payoff of zero; importance sampling can potentially make knock-ins less rare.

Suppose the underlying asset is modeled through a process of the form

$$S(t_n) = S(0) \exp(L_n), \quad L_n = \sum_{i=1}^n X_i,$$

with  $X_1, X_2, \ldots$  i.i.d. and  $L_0 = 0$ . This includes geometric Brownian motion but many other models as well; see Section 3.5. The option payoff is then

$$\mathbf{1}\{L_m > c, \tau < m\}$$

where  $c = \log(K/S(0))$ ,  $\tau$  is the first time the random walk  $L_n$  drops below  $-b$ , and  $-b = \log(H/S(0))$ . If b or c is large, the probability of a payoff is small. To increase the probability of a payoff, we need to drive  $L_n$  down toward  $-b$  and then up toward c.

Suppose the  $X_i$  have cumulant generating function  $\psi$  and consider importance sampling estimators of the following form: exponentially twist the distribution of the  $X_i$  by some  $\theta_-$  (with drift  $\psi'(\theta_-) < 0$ ) until the barrier is crossed, then twist the remaining  $X_{\tau+1},\ldots,X_m$  by some  $\theta_+$  (with drift  $\psi'(\theta_+) > 0$  to drive the process up toward the strike. On the event  $\{\tau < m\}$ , the likelihood ratio for this change of measure is (using  $(4.81)$  and  $(4.84)$ )

$$\exp\left(-\theta_{-}L_{\tau} + \psi(\theta_{-})\tau\right) \cdot \exp\left(-\theta_{+}[L_{m} - L_{\tau}] + \psi(\theta_{+})[m - \tau]\right)$$
  
= 
$$\exp\left((\theta_{+} - \theta_{-})L_{\tau} - \theta_{+}L_{m} + (\psi(\theta_{-}) - \psi(\theta_{+}))\tau + m\psi(\theta_{+})\right).$$

The importance sampling estimator is the product of this likelihood ratio and the discounted payoff.

We now apply a heuristic argument to select the parameters  $\theta_-, \theta_+$ . We expect most of the variability in the estimator to result from the barrier crossing time  $\tau$ , because for large b and c we expect  $L_{\tau} \approx -b$  and  $L_m \approx c$ on the event  $\{\tau < m, L_m > c\}$ . (In other words, the undershoot below  $-b$ and the overshoot above c should be small.) If we choose  $\theta_-, \theta_+$  to satisfy  $\psi(\theta_{-}) = \psi(\theta_{+}),$  the likelihood ratio simplifies to

$$\exp\left((\theta_+ - \theta_-)L_\tau - \theta_+ L_m + m\psi(\theta_+)\right),\,$$

and we thus eliminate explicit dependence on  $\tau$ .

To complete the selection of the parameters  $\theta_{\pm}$ , we impose the condition that traveling in a straight-line path from 0 to  $-b$  at rate  $|\psi'(\theta_{-})|$  and then from  $-b$  to c at rate  $\psi'(\theta_+)$ , the process should reach c at time m; i.e.,

$$\frac{-b}{\psi'(\theta_-)} + \frac{c+b}{\psi'(\theta_+)} = m.$$

These conditions uniquely determine  $\theta_{\pm}$ , at least if the domain of  $\psi$  is sufficiontly large This is illustrated in Figure 4.12

![](_page_81_Figure_0.jpeg)

![](_page_81_Figure_1.jpeg)

Fig. 4.12. Illustration of importance sampling strategy for a knock-in option. Twisting parameters  $\theta_{\pm}$  are chosen so that (a)  $\psi(\theta_{-}) = \psi(\theta_{+})$  and (b) straight-line path with slopes  $\psi'(\theta_-)$  and  $\psi'(\theta_+)$  reaches  $-b$  and then  $c$  in  $m$  steps.

In the case of geometric Brownian motion  $\text{GBM}(\mu, \sigma^2)$  with equally spaced time points  $t_n = nh$ , we have

$$X_n \sim N((\mu - \frac{1}{2}\sigma^2)h, \sigma^2 h),$$

and the cumulant generating function is

$$\psi(\theta) = (\mu - \frac{1}{2}\sigma^2)h\theta + \frac{1}{2}\sigma^2 h\theta^2$$

Because this function is quadratic in  $\theta$ , it is symmetric about its minimum and the condition  $\psi(\theta_-) = \psi(\theta_+)$  implies that  $\psi'(\theta_-) = -\psi'(\theta_+)$ . Thus, under our proposed change of measure, the random walk moves at a constant speed of  $|\psi'(\theta_{\pm})|$ . To traverse the path down to the barrier and up to the strike in m  $\text{steps, we must have}$ 

$$|\psi'(\theta_{\pm})| = \frac{2b+c}{m}.$$

We can now solve for the twisting parameters to get

$$\theta_{\pm} = \left(\frac{1}{2} - \frac{\mu}{\sigma^2}\right) \pm \frac{2b + c}{m\sigma^2 h}.$$

The term in parentheses on the right is the point at which the quadratic  $\psi$  is minimized. The twisting parameters  $\theta_{\pm}$  are symmetric about this point.

Table 4.4 reports variance ratios based on this method. The underlying asset  $S(t)$  is  $\text{GBM}(r,\sigma^2)$  with  $r=5\%$ ,  $\sigma=0.15$ , and initial value  $S(0)=95$ . We consider an option paying  $10,000$  if not knocked out, hence having price  $10,000 \cdot e^{-rT} P(\tau < m, S(T) > K)$ . As above, m is the number of steps and  $T \equiv t_m$  is the option maturity. The last column of the table gives the estimated ratio of the variance per replication using ordinary Monte Carlo to the variance using importance sampling. It is thus a measure of the speedup produced by importance sampling. The estimates in the table are based

on  $100,000$  replications for each case. The results suggest that the variance ratio depends primarily on the rarity of the payoff, and not otherwise on the maturity. The variance reduction can be dramatic for extremely rare payoffs.

An entirely different application of importance sampling to barrier options is developed in Glasserman and Staum [146]. In that method, at each step along a simulated path, the value of an underlying asset is sampled conditional on not crossing a knock-out barrier so that all paths survive to maturity. The one-step conditional distributions define the change of measure in this approach.  $\Box$ 

|                                 |  |                           | $H$ $K$ Price Variance Ratio |
|---------------------------------|--|---------------------------|------------------------------|
| $T = 0.25, m = 50$ 94 96 3017.6 |  |                           | 2                            |
|                                 |  | 90 96 426.6               | 10                           |
|                                 |  | 85 96 5.6                 | 477                          |
|                                 |  | 90 106 13.2               | 177                          |
| $T = 1, m = 50$ 90 106 664.8    |  |                           | 6                            |
|                                 |  | $85 \quad 96 \quad 452.0$ | 9                            |
| $T = 0.25, m = 100 85 96 6.6$   |  |                           | 405                          |
|                                 |  | 90 106 15.8               | 180                          |

**Table 4.4.** Variance reduction using importance sampling in pricing a knock-in barrier option with barrier  $H$  and strike  $K$ .

## 4.6.2 Path-Dependent Options

 $\sim 10$ 

We turn now to a more ambitious application of importance sampling with the aim of reducing variance in pricing path-dependent options. We consider models of underlying assets driven by Brownian motion (or simply by normal random vectors after discretization) and change the drift of the Brownian motion to drive the underlying assets into "important" regions, with "importance" determined by the payoff of the option. We identify a specific change of drift through an optimization problem.

The method described in this section is from Glasserman, Heidelberger, and Shahabuddin (henceforth abbreviated GHS) [139], and that reference contains a more extensive theoretical development than we provide here. This method restricts itself to deterministic changes of drift over discrete time steps. It is theoretically possible to eliminate all variance through a stochastic change of drift in continuous time, essentially by taking the option being priced as the numeraire asset and applying the change of measure associated with this change of numeraire. This however requires knowing the price of the option in advance and is not literally feasible, though it potentially provides a basis for approximations. Related ideas are developed in Chapter 16 of Kloeden and Platen [211], Newton [278, 279], and Schoenmakers and Heemink [210]

We restrict ourselves to simulations on a discrete time grid  $0 = t_0 < t_1 <$  $\cdots < t_m = T$ . We assume the only source of randomness in the simulated model is a  $d$ -dimensional Brownian motion. The increment of the Brownian motion from  $t_{i-1}$  to  $t_i$  is simulated as  $\sqrt{t_i - t_{i-1}} Z_i$ , where  $Z_1, Z_2, \ldots, Z_m$  are independent d-dimensional standard normal random vectors. Denote by  $Z$  the concatenation of the  $Z_i$  into a single vector of length  $n \equiv md$ . Each outcome of  $Z$  determines a path of underlying assets or state variables, and each such path determines the discounted payoff of an option. If we let  $G$  denote the composition of these mappings, then  $G(Z)$  is the discounted payoff derived from Z. Our task is to estimate  $E[G(Z)]$ , the expectation taken with Z having the  $n$ -dimensional standard normal distribution.

An example will help fix ideas. Consider a single underlying asset modeled as geometric Brownian motion  $\text{GBM}(r, \sigma^2)$  and simulated using

$$S(t_i) = S(t_{i-1}) \exp\left( [r - \frac{1}{2}\sigma^2](t_i - t_{i-1}) + \sigma\sqrt{t_i - t_{i-1}}Z_i \right), \quad i = 1, \dots, m.$$
(4.86)

Consider an Asian call option on the arithmetic average S of the  $S(t_i)$ . We may view the payoff of the option as a function of the  $Z_i$  and thus write

$$G(Z) = G(Z_1, \dots, Z_m) = e^{-rT} [\bar{S} - K]^+.$$

Pricing the option means evaluating  $E[G(Z)]$ , the expectation taken with  $Z \sim$  $N(0,I).$ 

## Change of Drift: Linearization

Through importance sampling we can change the distribution of  $Z$  and still obtain an unbiased estimator of  $E[G(Z)]$ , provided we weight each outcome by the appropriate likelihood ratio. We restrict ourselves to changes of distribution that change the mean of Z from 0 to some other vector  $\mu$ . Let  $P_{\mu}$ and  $\mathsf{E}_{\mu}$  denote probability and expectation when  $Z \sim N(\mu, I)$ . From the form of the likelihood ratio given in Example 4.6.1 for normal random vectors, we find that

$$\mathsf{E}[G(Z)] = \mathsf{E}_{\mu} \left[ G(Z) e^{-\mu^{\top} Z + \frac{1}{2}\mu^{\top} \mu} \right]$$

for any  $\mu \in \mathbb{R}^n$ . We may thus simulate as follows:

for replications 
$$i = 1, \ldots, N$$
  
generate  $Z^{(i)} \sim N(\mu, I)$   
 $Y^{(i)} \leftarrow G(Z^{(i)}) \exp\left(-\mu^{\top} Z^{(i)} + \frac{1}{2} \mu^{\top} \mu\right)$   
return  $(Y^{(1)} + \cdots + Y^{(N)})/N$ .

This estimator is unbiased for any choice of  $\mu$ ; we would like to choose a  $\mu$ that produces a low-variance estimator.

If  $G$  takes only nonnegative values (as is typical of discounted option payoffs), we may write  $G(z) = \exp(F(z))$ , with the convention that  $F(z) = -\infty$ 

if  $G(z) = 0$ . Also, note that taking an expectation over Z under  $P_{\mu}$  is equivalent to replacing Z with  $\mu + Z$  and taking the expectation under the original measure. (In the algorithm above, this simply means that we can sample from  $N(\mu, I)$  by sampling from  $N(0, I)$  and adding  $\mu$ .) Thus,

 $\ddot{\phantom{a}}$ 

$$\begin{split} \mathsf{E}[G(Z)] &= \mathsf{E}\left[e^{F(Z)}\right] = \mathsf{E}_{\mu} \left[e^{F(Z)} e^{-\mu^{\top} Z + \frac{1}{2}\mu^{\top} \mu}\right] \\ &= \mathsf{E}\left[e^{F(\mu+Z)} e^{-\mu^{\top} (\mu+Z) + \frac{1}{2}\mu^{\top} \mu}\right] \\ &= \mathsf{E}\left[e^{F(\mu+Z)} e^{-\mu^{\top} Z - \frac{1}{2}\mu^{\top} \mu}\right]. \end{split} \tag{4.87}$$

For any  $\mu$ , the expression inside the expectation in (4.87) is an unbiased estimator with Z having distribution  $N(0, I)$ . To motivate a particular choice of  $\mu$ , we now expand F to first order to approximate the estimator as

$$e^{F(\mu+Z)}e^{-\mu^{\top}Z-\frac{1}{2}\mu^{\top}\mu} \approx e^{F(\mu)+\nabla F(\mu)Z}e^{-\mu^{\top}Z-\frac{1}{2}\mu^{\top}\mu},\tag{4.88}$$

with  $\nabla F(\mu)$  the gradient of F at  $\mu$ . If we can choose  $\mu$  to satisfy the fixed-point condition

$$\nabla F(\mu) = \mu^{\top}, \tag{4.89}$$

then the expression on the right side of  $(4.88)$  collapses to a constant with no dependence on Z. Thus, applying importance sampling with  $\mu$  satisfying  $(4.89)$  would produce a zero-variance estimator if  $(4.88)$  held exactly, and it should produce a low-variance estimator if  $(4.88)$  holds only approximately.

## Change of Drift: Normal Approximation and Optimal Path

We now present an alternative argument leading to an essentially equivalent choice of  $\mu$ . Recall from the discussion surrounding (4.76) that the optimal importance sampling density is the normalized product of the integrand and the original density. For the problem at hand, this means that the optimal density is proportional to

$$e^{F(z) - \frac{1}{2}z^{\top}z},$$

because  $\exp(F(z))$  is the integrand and  $\exp(-z^{\top}z/2)$  is proportional to the standard normal density. Normalizing this function by its integral produces a probability density but not, in general, a normal density. Because we have restricted ourselves to changes of mean, we may try to select  $\mu$  so that  $N(\mu, I)$ approximates the optimal distribution. One way to do this is to choose  $\mu$  to be the mode of the optimal density; i.e., choose  $\mu$  to solve

$$\max_{z} F(z) - \frac{1}{2} z^{\top} z. \tag{4.90}$$

The first-order condition for the optimum is  $\nabla F(z) = z^{\top}$ , which coincides with  $(4.89)$ . If, for example, the objective in  $(4.90)$  is strictly concave, and if the first-order condition has a solution, this solution is the unique optimum.

We may interpret the solution  $z_*$  to (4.90) as an optimal path. Each  $z \in \Re^n$ may be interpreted as a path because each determines a discrete Brownian path and thus a path of underlying assets. The solution to  $(4.90)$  is the most "important" path if we measure importance by the product of payoff  $\exp(F(z))$  and probability density  $\exp(-z^{\top}z/2)/(2\pi)^{n/2}$ . In choosing  $\mu = z_{*}$ , we are therefore choosing the new drift to push the process along the optimal path.

 $\text{GHS}$  [139] give conditions under which this approach to importance sampling has an asymptotic optimality property. This property is based on introducing a parameter  $\epsilon$  and analyzing the second moment of the estimator as  $\epsilon$ approaches zero. From a practical perspective, a small  $\epsilon$  should be interpreted as a nearly linear  $F$ .

## Asian Option

We illustrate the selection and application of the optimal change of drift in the case of the Asian call defined above, following the discussion in GHS [139]. Solving (4.90) is equivalent to maximizing  $G(z) \exp(-z^{\top} z/2)$  with G the discounted payoff of the Asian option. The discount factor  $e^{-rT}$  is a constant in this example, so for the purpose of optimization we may ignore it and redefine  $G(z)$  to be  $[\bar{S}-K]^+$ . Also, in maximizing it clearly suffices to consider points z at which  $\bar{S} > K$  and thus at which G is differentiable.

For the first-order conditions, we differentiate

$$[\bar{S} - K]e^{-z^{\top}z/2}$$

 $to get$ 

$$\frac{\partial \bar{S}}{\partial z_j} - [\bar{S} - K] z_j = 0.$$

Using  $(4.86)$ , we find that

$$\frac{\partial \bar{S}}{\partial z_j} = \frac{1}{m} \sum_{i=j}^m \frac{\partial S(t_i)}{\partial z_j} = \frac{1}{m} \sum_{i=j}^m \sigma \sqrt{t_i - t_{i-1}} S(t_i).$$

The first-order conditions thus become

$$z_j = \frac{\sum_{i=j}^{m} \sigma \sqrt{t_i - t_{i-1}} S(t_i)}{mG(z)}$$

Now we specialize to the case of an equally spaced time grid with  $t_i - t_{i-1} \equiv$  $h.$  This yields

4.6 Importance Sampling 271

$$z_1 = \frac{\sigma\sqrt{h}(G(z) + K)}{G(z)}, \quad z_{j+1} = z_j - \frac{\sigma\sqrt{h}S(t_j)}{mG(z)}, \quad j = 1, \dots, m-1. \tag{4.91}$$

Given the value of  $G(z)$ , (4.91) and (4.86) determine z. Indeed, if  $y \equiv G(z)$ , we could apply (4.91) to calculate  $z_1$  from y, then (4.86) to calculate  $S(t_1)$ , then  $(4.91)$  to calculate  $z_2$ , and so on. Through this iteration, each value of y determines a  $z(y)$  and path  $S(t_i, y)$ ,  $i = 1, \ldots, m$ . Solving the first-order conditions reduces to finding the y for which the payoff at  $S(t_1, y), \ldots, S(t_m, y)$ is indeed  $y$ ; that is, it reduces to finding the root of the equation

$$\frac{1}{m} \sum_{j=1}^{m} S(t_j, y) - K - y = 0.$$

 $\text{GHS}$  [139] report that numerical examples suggest that this equation has a unique root. This root can be found very quickly through a one-dimensional search. Once the root  $y_*$  is found, the optimization problem is solved by  $z_{*} = z(y_{*})$ . To simulate, we then set  $\mu = z_{*}$  and apply importance sampling with mean  $\mu$ .

## Combined Importance Sampling and Stratification

In GHS  $[139]$ , further (and in some cases enormous) variance reduction is achieved by combining importance sampling with stratification of a linear projection of Z. Recall from Section 4.3.2 that sampling Z so that  $v^{\top}Z$  is stratified for some  $v \in \Re^n$  is easy to implement. The change of mean does not affect this. Indeed, we may sample from  $N(\mu, I)$  by sampling from  $N(0, I)$ and then adding  $\mu$ ; we can apply stratified sampling to  $N(0, I)$  before adding  $\mu$ .

Two strategies for selecting the stratification direction  $v$  are considered in GHS [139]. One simply sets  $v = \mu$  on the grounds that  $\mu$  is an important path and thus a potentially important direction for stratification. The other strategy expands  $(4.88)$  to get

$$e^{F(\mu+Z)}e^{-\mu^{\top}Z-\frac{1}{2}\mu^{\top}\mu} \approx e^{F(\mu)+\nabla F(\mu)Z+\frac{1}{2}Z^{\top}H(\mu)Z}e^{-\mu^{\top}Z-\frac{1}{2}\mu^{\top}\mu},$$

with  $H(\mu)$  the Hessian matrix of F at  $\mu$ . Importance sampling with  $\mu^{\top}$  =  $\nabla F(\mu)$  eliminates the linear term in the exponent, and this suggests that the stratification should be tailored to the quadratic term.

In Section  $4.3.2$ , we noted that the optimal stratification direction for estimating an expression of the form  $E[\exp(\frac{1}{2}Z^{\top}AZ)]$  with A symmetric is an eigenvector of  $A$ . The optimal eigenvector is determined by the eigenvalues of A through the criterion in  $(4.50)$ . This suggests that we should stratify along the optimal eigenvector of the Hessian of F at  $\mu$ . This entails numerical calculation of the Hessian and its eigenvectors.

Table  $4.5$  shows results from GHS [139]. The table shows variance ratios (i.e., variance reduction factors) using importance sampling and two combinations of importance sampling with stratified sampling, using the two strategies just described for selecting a stratification direction. All results use  $S(0) = 50$ .  $r = 0.05$ , and  $T = 1$  and are estimated from one million paths for each case. The results show that importance sampling by itself can produce noteworthy variance reduction (especially for out-of-the-money options) and that the combined impact with stratification can be astounding. The combination reduces variance by factors in the thousands.

|   |                        |    |                      | $\text{Importance}$ | IS $\&$        | IS $\&$            |
|---|------------------------|----|----------------------|---------------------|----------------|--------------------|
| n | $\sigma$               |    | $K$ Price            | Sampling            | Strat. $(\mu)$ | Strat. $(v_{j^*})$ |
|   |                        |    | $16\ 0.10\ 45\ 6.05$ | 11                  | 1,097          | 1,246              |
|   |                        | 50 | 1.92                 | 7                   | 4,559          | 5,710              |
|   |                        |    | $55\;\;0.20$         | 21                  | 15,520         | 17,026             |
|   |                        |    | $16\ 0.30\ 45\ 7.15$ | 8                   | 1,011          | 1,664              |
|   |                        | 50 | 4.17                 | 9                   | 1,304          | 1,899              |
|   |                        |    | $55 \ 2.21$          | 12                  | 1,746          | 2,296              |
|   | $64\ 0.10\ 45\ \ 6.00$ |    |                      | 11                  | 967            | 1,022              |
|   |                        |    | $50 \text{ } 1.85$   | 7                   | 4,637          | 5,665              |
|   |                        | 55 | 0.17                 | 23                  | 16,051         | 17,841             |
|   | $64\ 0.30\ 45\ 7.02$   |    |                      | 8                   | 1,016          | 1,694              |
|   |                        | 50 | 4.02                 | 9                   | 1,319          | 1,971              |
|   |                        |    | $55 \ 2.08$          | 12                  | 1,767          | 2,402              |

**Table 4.5.** Estimated variance reduction ratios for Asian options using importance sampling and combinations of importance sampling with stratified sampling, stratifying along the optimal  $\mu$  or the optimal eigenvector  $v_{j^*}$ . Stratified results use 100  $strata.$ 

The results in Table 4.5 may seem to suggest that stratification has a greater impact than importance sampling, and one may question the value of importance sampling in this example. But the effectiveness of stratification is indeed enhanced by the change in mean, which results in more paths producing positive payoffs. The positive-part operator  $[\cdot]^+$  applied to  $\bar{S}-K$  diminishes the effectiveness of stratified sampling, because it tends to produce many  $\text{strata with a constant (zero) payoff} \longrightarrow \text{stratifying a region of constant payoff is}$ useless. By shifting the mean of  $Z$ , we implicitly move more of the distribution of the stratification variable  $v^{\top}Z$  (and thus more strata) into the region where the payoff varies. In this particular example, the region defined by  $\bar{S} > K$  is reasonably easy to characterize and could be incorporated into the selection of strata; however, this is not the case in more complex examples.

A further notable feature of Table  $4.5$  is that the variance ratios are quite similar whether we stratify along  $\mu$  or along the optimal eigenvector  $v_{*}$ . In fact, GHS [139] find that the vectors  $\mu$  and  $v_*$  nearly coincide, once normalized to have the same length. They find similar patterns in other examples. This phenomenon can occur when  $G$  is well approximated by a nonlinear function of a linear combination of  $z_1, \ldots, z_m$ . For suppose  $G(z) \approx g(v^{\top}z)$ ; then, the gradient of G is nearly proportional to  $v^{\top}$  and so  $\mu$  will be nearly proportional to  $v$ . Moreover, the Hessian of  $G$  will be nearly proportional to the rank-1 matrix  $vv^{\top}$ , whose only nonzero eigenvectors are multiples of v. Thus, in this setting, the optimal mean is proportional to the optimal eigenvector.

## Application in the Heath-Jarrow-Morton Framework

GHS [140] apply the combination of importance sampling and stratified sampling in the Heath-Jarrow-Morton framework. The complexity of this setting necessitates some approximations in the calculation of the optimal path and eigenvector to make the method computationally feasible. We comment on these briefly.

We consider a three-factor model (so  $d = 3$ ) discretized in time and maturity as detailed in Section 3.6.2. The discretization interval is a quarter of a year and we consider maturities up to 20 years, so  $m = 80$  and the vector Z of random inputs has dimension  $n = md = 240$ . The factor loadings for each of the three factors are as displayed in Figure 4.13, where they are plotted against time to maturity.

![](_page_88_Figure_5.jpeg)

Fig. 4.13. Factor loadings in three-factor HJM model used to illustrate importance sampling.

As in Section 3.6.2, we use  $\hat{f}(t_i, t_j)$  to denote the forward rate at time  $t_i$ for the interval  $[t_j, t_{j+1}]$ . We use an equally spaced time grid so  $t_i = ih$  with  $h$  a quarter of a year. The initial forward curve is

$$\hat{f}(0, t_j) = \log(150 + 12j)/100, \quad j = 0, 1, \dots, 80,$$

which increases gradually, approximately from  $5\%$  to  $7\%$ .

Among the examples considered in GHS [140] is the pricing of an interest rate caplet maturing in  $T = t_m$  years with a strike of K. The caplet pays

$$\max\left(0, (e^{\hat{f}(t_m, t_m)h} - 1) - Kh)\right)$$

at  $t_{m+1}$ . For a maturity of  $T=5$  years,  $m=20$  and the optimal drift  $\mu$  is a vector of dimension  $md = 60$ . We encode this vector in the following way: the first 20 components give the drift as a function of time for the first factor (i.e., the first component of the underlying three-dimensional Brownian motion); the next 20 components give the drift for the second factor; and the last  $20$ components give the drift for the third factor.

With this convention, the left panel of Figure 4.14 displays the optimal drift found through numerical solution of the optimization problem  $(4.90)$ , with  $\exp(F(z))$  the discounted caplet payoff determined by the input vector  $z$ . This optimal path gives a positive drift to the first and third factors and a negative drift to the second; all three drifts approach zero toward the end of the 20 steps (the caplet maturity).

The right panel of Figure 4.14 shows the net effect on the short rate of this change of drift. (Recall from Section 3.6.2 that the short rate at  $t_i$  is simply  $\hat{f}(t_i, t_i)$ .) If each of the three factors were to follow the mean paths in the left panel of Figure 4.14, the short rate would follow the dashed line in the right panel of the figure. This should be compared with the initial forward curve, displayed as the solid line: without a change of drift, the central path of the short rate would roughly follow this forward curve. Thus, the net effect of the change of drift in the underlying factors is to push the short rate higher. This is to be expected because the caplet payoff increases with the short rate. But it is not obvious that the "optimal" way to push the short rate has the factors follow the paths in the left panel of Figure 4.14.

![](_page_89_Figure_7.jpeg)

Fig. 4.14. Left panel shows optimal drift for factors in pricing a five-year caplet struck at 7%. Right panel compares path of short rate produced by optimal drift with the initial forward curve.

### 4.6 Importance Sampling 275

Table 4.6 compares the efficacy of four variance reduction techniques in pricing caplets: antithetic variates, importance sampling using the optimal drift, and two combinations of importance sampling with stratified sampling using either the optimal drift  $\mu$  or the optimal eigenvector  $v_{i^*}$  for the stratification direction. Calculation of the optimal eigenvector requires numerical calculation of the Hessian. The table (from [140]) displays estimated variance ratios based on 50,000 paths per method. The last two columns are based on 100 strata. The table indicates that importance sampling is most effective for deep out-of-the-money caplets, precisely where antithetics become least effective. Both strategies for stratification produce substantial additional variance reduction in these examples.

|     |              |                 |              | IS $&$         | IS $\&$            |
|-----|--------------|-----------------|--------------|----------------|--------------------|
| T   |              | $K$ Antithetics | $\text{IS}$  | Strat. $(\mu)$ | Strat. $(v_{j^*})$ |
| 2.5 | 0.04         | 8               | 8            | 246            | 248                |
|     | 0.07         |                 | 16           | 510            | 444                |
|     | 0.10         |                 | 173          | 3067           | 2861               |
| 5.0 | 0.04         | 4               | 8            | 188            | 211                |
|     | 0.07         | 1               | 11           | 241            | 292                |
|     | 0.10         |                 | 27           | 475            | 512                |
|     | $10.0\ 0.04$ | 4               | $\mathbf{7}$ | 52             | 141                |
|     | 0.07         | 1               | 8            | 70             | 185                |
|     | 0.10         |                 | 12           | 110            | 244                |
|     | $15.0\ 0.04$ | 4               | 5            | 15             | 67                 |
|     | 0.07         | 2               | 6            | 22             | 112                |
|     | 0.10         |                 | 8            | 31             | 158                |

**Table 4.6.** Estimated variance ratios for caplets in three-factor HJM model.

Further numerical results for other interest rate derivatives are reported in GHS  $[140]$ . As in Table 4.6, the greatest variance reduction typically occurs for out-of-the-money options. The combination of importance sampling with stratification is less effective for options with discontinuous payoffs; a specific example of this in  $[140]$  is a "flex cap," in which only a subset of the caplets in a cap make payments even if all expire in-the-money.

In a complex, high-dimensional setting like an HJM model, the computational overhead involved in finding the optimal path or the optimal eigenvector can become substantial. These are fixed costs, in the sense that these calculations need only be done once for each pricing problem rather than once for each path simulated. In theory, as the number of paths increases (which is to say as the required precision becomes high), any fixed cost eventually becomes negligible, but this may not be relevant for practical sample sizes.

 $\text{GHS}$  [140] develop approximations to reduce the computational overhead in the optimization and eigenvector calculations. These approximations are

based on assuming that the optimal drift (or optimal eigenvector) are piecewise linear between a relatively small number of nodes. This reduces the dimension of the problem. Consider, for example, the computation of a  $120$ dimensional optimal drift consisting of three 40-dimensional segments. Making a piecewise linear approximation to each segment based on four nodes per segment reduces the problem to one of optimizing over the 12 nodes rather than all 120 components of the vector. Figure 4.15 illustrates the results of this approach in finding both the optimal drift and the optimal eigenvector for a ten-year caplet with a  $7\%$  strike. These calculations are explained in detail in GHS [140]. The figure suggests that the approach is quite effective. Simulation results reported in [140] based on using these approximations confirm the viability of the approach.

![](_page_91_Figure_2.jpeg)

**Fig. 4.15.** Optimal drift (left) and eigenvector (right) calculated using a piecewise linear approximation with three or four nodes per segment.

## 4.7 Concluding Remarks

It is easier to survey the topic of variance reduction than to answer the question that brings a reader to such a survey: "Which technique should I use?" There is rarely a simple answer to this question. The most effective applications of variance reduction techniques take advantage of an understanding of the problem at hand. The choice of technique should depend on the available information and on the time available to tailor a general technique to a particular problem. An understanding of the strengths and weaknesses of alternative methods and familiarity with examples of effective applications are useful in choosing a technique.

Figure  $4.16$  provides a rough comparison of several techniques discussed in this chapter. The figure positions the methods according to their complexity and shows a range of typical effectiveness for each. We have not given the

axes units or scales, nor have we defined what they mean or what counts as typical; the figure should clearly not be taken literally or too seriously. We include it to highlight some differences among the methods in the types of implementations and applications discussed in this chapter.

![](_page_92_Figure_2.jpeg)

Fig. 4.16. Schematic comparison of some variance reduction techniques

The effectiveness of a method is the efficiency improvement it brings in the sense discussed in Section 1.1.3. Effectiveness below the horizontal axis in the figure is detrimental — worse than not using any variance reduction technique. In the complexity of a method we include the level of effort and detailed knowledge required for implementation. We now explain the positions of the methods in the figure:

- o Antithetic sampling requires no specific information about a simulated model and is trivial to implement. It rarely provides much variance reduction. It can be detrimental (as explained in Section  $4.2$ ), but such cases are not common.
- o Control variates and methods for matching underlying assets (including path adjustments and weighted Monte Carlo) give similar results. Of these methods, control variates are usually the easiest to implement and the best understood. Finding a good control requires knowing something about the simulated model — but not too much. A control variate implemented with an optimal coefficient is guaranteed not to increase variance. When the optimal coefficient is estimated rather than known, it is theoretically possible for a control variate to be detrimental at very small sample sizes, but this is not a practical limitation of the method.
- o We have positioned stratified sampling at a higher level of complexity because we have in mind examples like those in Section  $4.3.2$  where the stratification variable is tailored to the model. In contrast, stratifying a uniform

distribution (as in Example  $4.3.1$ ) is trivial but not very effective by itself. Using a variable for stratification requires knowing its distribution whereas using it as a control only requires knowing its mean. Stratified sampling is similar to using the distribution (more precisely, the stratum probabilities) as controls and is thus more powerful than using just the mean. With a proportional allocation, stratified sampling never increases variance; using any other allocation may be viewed as a form of importance sampling.

- We have omitted Latin hypercube sampling from the figure. As a generalization of stratified sampling, it should lie upwards and to the right of that method. But a generic application of Latin hypercube sampling (in which the marginals simply correspond to the uniform random variables used to drive a simulation) is often both easier to implement and less effective than a carefully designed one-dimensional stratification. A problem for which a generic application of Latin hypercube sampling is effective, is also a good candidate for the quasi-Monte Carlo methods discussed in Chapter 5.
- As emphasized in the figure, importance sampling is the most delicate of the methods discussed in this chapter. It has the capacity to exploit detailed knowledge about a model (often in the form of asymptotic approximations) to produce orders of magnitude variance reduction. But if the importance sampling distribution is not chosen carefully, this method can also increase variance. Indeed, it can even produce infinite variance.

There are counterexamples to nearly any general statement one could make comparing variance reduction techniques and one could argue against any of the comparisons implied by Figure 4.16. Nevertheless, we believe these comparisons to be indicative of what one finds in applying variance reduction techniques to the types of models and problems that arise in financial engineering.

We close this section with some further references to the literature on variance reduction. Glynn and Iglehart  $[156]$  survey the application of variance reduction techniques in queueing simulations and discuss some techniques not covered in this chapter. Schmeiser, Taaffe, and Wang [318] analyze biased control variates with coefficients chosen to minimize root mean square error; this is relevant to, e.g., Example  $4.1.3$  and to settings in which the mean of a control variate is approximated using a binomial lattice. The conditional sampling methods of Cheng  $[81, 82]$  are relevant to the methods discussed in Sections 4.3.2 and 4.5.1. Hesterberg [177] and Owen and Zhou [292] propose defensive forms of importance sampling that mix an aggressive change of distribution with a more conservative one to bound the worst-case variance. Dupuis and Wang  $[108]$  show that a dynamic exponential change of measure — in which the twisting parameter is recomputed at each step  $$ can outperform a static twist. An adaptive importance sampling method for Markov chains is shown in Kollman et al.  $[214]$  to converge exponentially fast. An importance sampling method for stochastic volatility models is developed

in Fournié, Lasry, and Touzi [125]. Schoenmakers and Heemink [319] apply importance sampling for derivatives pricing through an approximating PDE.

Shahabuddin  $[327]$  uses rare-transition asymptotics to develop an impor- $\text{tance sampling procedure for reliability systems; see Heidelberger [175] and}$ Shahabuddin [328] for more on this application area. Asmussen and Binswanger [22], Asmussen, Binswanger, and Højgaard [23], and Juneja and Shahabuddin [206] address difficulties in applying importance sampling to heavytailed distributions; see also Section 9.3.

Avramidis and Wilson [30] and Hesterberg and Nelson [178] analyze variance reduction techniques for quantile estimation. We return to this topic in Chapter  $9.$ 

Among the techniques not discussed in this chapter is *conditional Monte Carlo*, also called Rao-Blackwellization. This method replaces an estimator by its conditional expectation. As  $\text{M}$  and  $\text{B}$  inswanger [22] give a particularly effective application of this idea to an insurance problem; Fox and Glynn [129] combine it with other techniques to estimate infinite horizon discounted costs; Boyle et al.  $[53]$  give some applications in option pricing.
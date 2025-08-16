# **Generalized Method of Moments (GMM)**

The generalized method of moments (GMM) provides a computationally convenient method of obtaining consistent and asymptotically normally distributed estimators of the parameters of statistical models. The method has been applied in many areas of economics but has arguably been most frequently applied in finance. In fact, it was in empirical finance that the power of the method was first illustrated: for while Hansen [7] introduced GMM and presented its fundamental statistical theory, Hansen and Hodrick [9] and Hansen and Singleton [10] showed the potential of the GMM approach to estimation through their empirical analyses of, respectively, foreign exchange markets and asset pricing. This article briefly describes the GMM framework for estimation and inference in the case where time-series data are used. The reader is referred to [6] for a comprehensive treatment of GMM that presents both a rigorous statistical analysis of the method and empirical illustrations in finance. For applications of GMM to panel data, see [15].

The popularity of GMM can be understood by comparing the requirements for the method to those for maximum likelihood (ML). While ML is the best available estimator within the paradigm of classical statistics, its optimality stems from its basis on the joint probability distribution of the data. However, in many scenarios of interest in finance, this dependence on the probability distribution can become a weakness for two main reasons. First, in some models, the joint probability distribution is only implicitly specified and is not available in a convenient closed form with the result that ML is computationally infeasible, for example, in stochastic volatility models [11]. Secondly, in other cases, the underlying theoretical model places restrictions on the distribution of the data but does not completely specify its form, with the result that ML is infeasible unless the researcher imposes an arbitrary assumption about the distribution. The latter is an unattractive strategy because if the assumed distribution is incorrect, then the optimality of ML is lost, and the resulting estimator may even be inconsistent; for example, in nonlinear Euler equation models [10]. In contrast, GMM estimation is based on population moment conditions. It turns out that in many cases where the financial-theoretic model does not specify the complete distribution, it does specify population moment conditions. Therefore, in these settings, GMM can be preferred to ML because it offers a way to estimate the parameters solely on the basis of information deduced from the underlying financial model.

The cornerstone of GMM estimation is the population moment condition:

#### **Definition 1 Population Moment Condition.**

*Let θ*<sup>0</sup> *be a vector of unknown parameters that are to be estimated,* **v***<sup>t</sup> be a vector of random variables, and* **f***(.) a vector of functions. Then a population moment condition takes the form*

$$E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}_0)] = 0 \tag{1}$$

*for all t.*

To illustrate the types of population moment conditions that can arise in finance models, we consider the specific examples in the seminal papers [9] and [10].

**Example 1** The efficiency of foreign exchange markets

Consider the following regression model for the relationship between the forward and spot exchange rates:

$$s_{t+k} = \beta_{0,1} + \beta_{0,2} f_{t,k} + u_t \tag{2}$$

where *ft,k* is the log of the *k*− period forward exchange rate at time *t*, *st*<sup>+</sup>*<sup>k</sup>* is the log of the spot exchange rate in period *t* + *k*, *β*0*,*<sup>1</sup> and *β*0*,*<sup>2</sup> are unknown parameters, and *ut* is an error term. Hansen and Hodrick [9] demonstrate that under the simple efficient-markets hypothesis, the following population moment condition holds

$$E[f_{t,k}(s_{t+k} - \beta_{0,1} - \beta_{0,2}f_{t,k})] = 0 \qquad (3)$$

where *(β*0*,*1*, β*0*,*2*)* = *(*0*,* 1*)*.

**Example 2** The consumption-based asset-pricing model

The consumption-based asset-pricing model involves a representative agent who makes investment and consumption decisions at time *t* to maximize his/her discounted lifetime utility subject to a budget constraint. Assuming that the agent's utility function is of the constant relative risk aversion form and that the only asset available as a possible investment yields a pay-off in the following period, Hansen and Singleton  $[10]$  show that the model implies the following population moment condition:

$$E\left[\mathbf{z}_{t}\left\{\delta_{0}\left(\frac{c_{t+1}}{c_{t}}\right)^{\gamma_{0}-1}\left(\frac{g_{t+1}}{p_{t}}\right)-1\right\}\right]=0\qquad(4)$$

where  $c_t$  is consumption in period t,  $g_{t+1}$  is the gain (cash flow) on the asset in period  $t + 1$ ,  $p_t$  is the price of the asset in period t,  $\mathbf{z}_t$  is a vector of variables in the agent's information set at time  $t$ , and the unknown parameters  $1 - \gamma_0$  and  $\delta_0$  are, respectively, the agent's coefficient of relative risk aversion and discount factor.

The population moment condition states that  $E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta})]$  equals zero when evaluated at  $\boldsymbol{\theta}_0$ . For the GMM estimation to be successful, this must be a unique property of  $\theta_0$ , that is,  $E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta})]$  is not equal to zero when evaluated at any other value of  $\theta$ . If the latter holds, then  $\theta_0$  is said to be *identified* by  $E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}_0)] = 0$ . A first-order condition for identification (often referred to as a local *condition*) is that  $rank\{G(\theta_0)\} = p$ , where  $G(\theta) =$  $E[\partial \mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta})/\partial \boldsymbol{\theta}']$ , and this plays a crucial role in standard asymptotic distribution theory for GMM. By definition, the moment condition involves  $q$  pieces of information about  $p$  unknowns; therefore identification can only hold if  $q \geq p$ . For reasons that emerge below, it is convenient to split this scenario into two parts:  $q = p$ , in which case  $\theta_0$  is said to be *just identified*, and  $q > p$ , in which case  $\theta_0$  is said to be *overidentified*.

Let  $\mathbf{g}_T(\boldsymbol{\theta})$  be the analogous sample moment to  $E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta})]$ , that is,  $\mathbf{g}_T(\boldsymbol{\theta}) = T^{-1} \sum_{t=1}^T \mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta})$  where  $T$  is the sample size. The GMM estimator is then as follows.

## **Definition 2 Generalized Method of Moments** Estimator.

The generalized method of moments estimator based on equation (1) is the value of  $\boldsymbol{\theta}$  that minimizes

$$Q_T(\boldsymbol{\theta}) = \mathbf{g}_T(\boldsymbol{\theta})' \mathbf{W}_T \mathbf{g}_T(\boldsymbol{\theta}) \tag{5}$$

where  $\mathbf{W}_T$  is known as the weighting matrix and is restricted to be a positive semidefinite matrix that converges in probability to  $\mathbf{W}$ , some positive definite matrix of constants.

The restrictions on the weighting matrix are required to ensure that  $O_T(\theta)$  is a meaningful measure of the distance the sample moment is from zero at different values of  $\theta$ . The choice of weighting matrix is discussed further below.

The first-order conditions for this minimization are

$$\mathbf{G}_T(\hat{\boldsymbol{\theta}}_T)'\mathbf{W}_T\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T) = 0 \tag{6}$$

where  $\mathbf{G}_T(\boldsymbol{\theta}) = T^{-1} \sum_{t=1}^T \partial \mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}) / \partial \boldsymbol{\theta}'$ . The structure of these conditions reveals some interesting insights into GMM estimation. Since  $G_T(\theta)$  is  $q \times p$ , it follows that equation (6) involves calculating  $\hat{\boldsymbol{\theta}}_T$  as the value of  $\boldsymbol{\theta}$  that sets the *p* linear combinations of  $\mathbf{g}_T(.)$  to zero. Therefore, if  $p = q$  (and  $\mathbf{G}_T(\hat{\boldsymbol{\theta}}_T)'\mathbf{W}_T$  is nonsingular), then  $\hat{\boldsymbol{\theta}}_T$  satisfies the analogous sample moment condition to equation (1),  $\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T) = 0$ , and is, thus, the method of moments estimator based on the original moment condition. However, if  $q > p$ , then the first-order conditions are not equivalent to solving the sample moment condition. Instead,  $\hat{\theta}_T$  is equivalent to the method of moments estimator based on

$$\mathbf{G}(\boldsymbol{\theta}_0)' \mathbf{W} E[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}_0)] = 0 \tag{7}$$

Although equation  $(1)$  implies equation  $(7)$ , the reverse does not hold because  $q > p$ ; therefore, in this case, the estimation is actually based on only part of the original information. As a result, if  $q > p$ , then GMM can be viewed as decomposing the original moment condition into two parts, the *identify*ing restrictions, which contain the information actually used in the estimation, and the *overidentifying* restrictions, which represent a remainder. Furthermore, GMM estimation produces two fundamental statistics each of which is associated with a particular component: the estimator  $\hat{\theta}_T$  is a function of the information in the identifying restrictions, and the estimated sample moment,  $\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T)$ , is a function of the information in the overidentifying restrictions. While unused in estimation, the overidentifying restrictions play a crucial role in inference about the validity of the model as discussed below.

To establish the consistency and asymptotic normality of the GMM estimator, it is necessary to place restrictions on  $\mathbf{v}_t$  and  $\mathbf{f}(.)$ . In the standard asymptotic framework (see [7]), it is assumed that  $\mathbf{v}_t$  is stationary and ergodic,  $\mathbf{f}(.)$  is continuous and differentiable and that its derivative is continuous in  $\theta$ . Various expectations of  $\mathbf{f}(.)$  and its derivative must also exist. These conditions permit the applications of laws of large numbers and central limit theorems to the requisite sample averages. Chief among the restrictions on expectations of  $\mathbf{f}()$  are that the population moment condition is valid and identifies  $\theta_0$ . Under the above conditions, it can be shown that the  $\hat{\boldsymbol{\theta}}_T \stackrel{p}{\rightarrow} \boldsymbol{\theta}_0$  and

$$T^{1/2}(\hat{\boldsymbol{\theta}}_T - \boldsymbol{\theta}_0) \stackrel{d}{\to} N(0, V) \tag{8}$$

where

$$V = [\mathbf{G}(\boldsymbol{\theta}_0)' \mathbf{W} \mathbf{G}(\boldsymbol{\theta}_0)]^{-1} \mathbf{G}(\boldsymbol{\theta}_0)' \mathbf{W} \mathbf{S}(\boldsymbol{\theta}_0) \mathbf{W} \mathbf{G}(\boldsymbol{\theta}_0)$$
$$\times [\mathbf{G}(\boldsymbol{\theta}_0)' \mathbf{W} \mathbf{G}(\boldsymbol{\theta}_0)]^{-1}$$

and  $\mathbf{S}(\boldsymbol{\theta}) = \lim_{T \to \infty} Var[T^{1/2}\mathbf{g}_T(\boldsymbol{\theta})].$ 

At this point, we return to the issue of the choice of weighting matrix. In the discussion of the firstorder conditions above, it is noted that if  $p = q$ , then the GMM estimator can be found by solving  $\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T)$ . As a result, the estimator does not depend on  $\mathbf{W}_T$ . The asymptotic properties must also be invariant to  $\mathbf{W}_T$  and it can be shown that  $\mathbf{V}$  reduces to  $\{\mathbf{G}(\boldsymbol{\theta}_0)'\mathbf{S}(\boldsymbol{\theta}_0)^{-1}\mathbf{G}(\boldsymbol{\theta}_0)\}^{-1}$  in this case. However, if  $q > p$ , then the first-order conditions depend on  $\mathbf{W}_T$ and therefore so does  $\hat{\theta}_T$ , in general. This dependence is unattractive because it raises the possibility that subsequent inferences can be affected by the choice of weighting matrix. However, in terms of asymptotic properties, the choice of weighting matrix only manifests itself in  $V$ , the asymptotic variance of the estimator. Since this is the case, it is natural to choose  $\mathbf{W}_T$  such that  $\mathbf{V}$  is minimized in a matrix sense. Hansen [7] shows that this can be achieved by setting  $\mathbf{W}_T = \hat{\mathbf{S}}_T^{-1}$  where  $\hat{\mathbf{S}}_T$  is a consistent estimator of  $S(\theta_0)$ . The resulting asymptotic variance is  $\mathbf{V} = \mathbf{V}^0 = \{ \mathbf{G}(\boldsymbol{\theta}_0)' S(\boldsymbol{\theta}_0)^{-1} \mathbf{G}(\boldsymbol{\theta}_0) \}^{-1}; \text{Chamberlain [4]}$ shows  $\mathbf{V}^0$  is a semiparametric efficiency bound for estimation of  $\theta_0$  based on equation (1).

In practical terms, two issues arise in the implementation of GMM with this choice of weighting matrix: (i) how to construct  $\hat{\mathbf{S}}_T$  so that it is a consistent estimator of  $S(\theta_0)$ ; (ii) how to handle the dependence of  $\hat{\mathbf{S}}_T$  on  $\hat{\boldsymbol{\theta}}_T$ . We treat each in turn.

#### (i) Estimation of $S(\theta_0)$ .

Under stationarity and ergodicity and certain other technical restrictions, it can be shown that  $S(\theta_0)$  =  $\Gamma_0(\boldsymbol{\theta}_0) + \sum_{i=1}^{\infty} \{ \Gamma_i(\boldsymbol{\theta}_0) + \Gamma_i(\boldsymbol{\theta}_0)' \}$  where  $\Gamma_i(\boldsymbol{\theta}_0) =$  $\text{Cov}[\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}_0), \mathbf{f}(\mathbf{v}_{t-i}, \boldsymbol{\theta}_0)]$  is known as the *i*-lag autocovariance matrix of  $\mathbf{f}(\mathbf{v}_t, \boldsymbol{\theta}_0)$  [2]. In some cases, the structure of the model implies  $\Gamma_i(\theta_0) = 0$  for all  $i > k$ for some  $k$ , and this simplifies the estimation problem ([6], Section 3.5). In the absence of such a restriction  $\mathbf{a}$ on the autocovariance matrices, the long-run variance can be estimated by a member of the class of *heteroscedasticity autocorrelation covariance (HAC)* estimators defined by

$$\hat{\mathbf{S}}_{\text{HAC}} = \hat{\mathbf{\Gamma}}_0 + \sum_{i=1}^{T-1} \omega(i; b_T) (\hat{\mathbf{\Gamma}}_i + \hat{\mathbf{\Gamma}}'_i) \qquad (9)$$

where  $\hat{\mathbf{\Gamma}}_j = T^{-1} \sum_{t=j+1}^T \hat{\mathbf{f}}_t \hat{\mathbf{f}}_{t-j}^v, \ \hat{\mathbf{f}}_t = \mathbf{f}(v_t, \hat{\boldsymbol{\theta}}_T), \ \omega(.)$ is known as the *kernel*, and  $b_T$  is known as the bandwidth. The kernel and bandwidth must satisfy certain restrictions to ensure  $\hat{\mathbf{S}}_{\text{HAC}}$  is both consistent and positive semidefinite. As an illustration, Newey and West [13] propose the use of the kernel  $\omega(i, b_T) = \{1 - i/(b_T + 1)\}\mathcal{I}\{i \leq b_T\}$  where  $\mathcal{I}\{i \leq t_T\}$  $b_T$  is an indicator variable that takes the value 1 if  $i < b_T$  and 0, otherwise. This choice is an example of a truncated kernel estimator because the number of included autocovariances is determined by  $b_T$ . For consistency, we require  $b_T \rightarrow$  $\infty$  with  $T \to \infty$  but  $b_T = o(T^{1/2})$ . Various choices of kernel have been proposed and their properties analyzed: while theoretical rankings are possible, the evidence suggests that the choice of  $b_T$ is a far more important determinant of finite sample performance. Andrews [2] and Newey and West [14] propose data-based methods for the selection of  $b_T$ . See ([6], Section 3.5) for further discussion.

#### (ii) Dependence of $\hat{S}_T$ on $\hat{\theta}_T$ .

As is apparent from the above discussion, the calculation of a consistent estimator for  $S(\theta_0)$  requires knowledge of a (consistent) estimator of  $\theta_0$ . Therefore, to calculate a GMM estimator that attains the efficiency bound, a multistep procedure is used. In the first step, GMM is performed with an arbitrary weighting matrix; this preliminary estimator is then used in the calculation of  $\hat{\mathbf{S}}_T$ . In the second step, GMM estimation is performed with  $\mathbf{W}_T = \hat{\mathbf{S}}_T^{-1}$ . For obvious reasons, the resulting estimator is commonly referred to as the two-step GMM estimator. Instead of stopping after just two steps, the procedure can be continued so that on the  $i$ th step the GMM estimation is performed using  $\mathbf{W}_T = \hat{\mathbf{S}}_T^{-1}$ , where  $\hat{\mathbf{S}}_T$  is based on the estimator from the  $(i-1)$ 

th step. This yields the so-called iterated GMM estimator.

While two steps are sufficient to attain the efficiency bound, simulation evidence suggests that there are often considerable gains to iteration in the sense of improvements in the quality of asymptotic theory as an approximation to finite sample behavior ([6], Chapter 6). Notwithstanding these improvements, there is evidence that the quality of the asymptotic approximation may be poor in some circumstances of interest and this motivated the development of alternative methods for attaining the efficiency bound. One such method is the *continuous-updating gener*alized method of moments (CUGMM) estimator proposed by Hansen et al. [8]. The CUGMM estimator is the value of  $\boldsymbol{\theta}$  that minimizes  $\mathbf{g}_T(\boldsymbol{\theta})'\mathbf{S}_T(\boldsymbol{\theta})^{-1}\mathbf{g}_T(\boldsymbol{\theta})$ where  $S_T(\theta)$  is a (matrix) function of  $\theta$  such that  $\mathbf{S}_T(\boldsymbol{\theta}) \stackrel{p}{\rightarrow} \mathbf{S}(\boldsymbol{\theta})$  uniformly in  $\boldsymbol{\theta}$ . While the CUGMM estimator has the same limiting distribution as the iterated GMM estimator, Newey and Smith [12] and Anatolyev [1] demonstrate analytically that the continuous-updating estimator can be expected to exhibit lower finite sample bias than its two-step counterpart; see also [3].

The foregoing results are predicated on the assumption that equation (1) represents valid information about  $\theta_0$ , and, in this sense, that the model is correctly specified. In practice, it is desirable to assess whether the data appear consistent with the restriction implied by the population moment condition. As noted above, if  $p = q$ , then the first-order conditions force  $\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T) = 0$  irrespective of whether equation (1) holds, and so the latter cannot be tested directly using the estimated sample moment,  $\mathbf{g}_T(\hat{\boldsymbol{\theta}}_T)$ . However, if  $q > p$ , then  $\mathbf{g}_T(\boldsymbol{\theta}_T) \neq 0$  because GMM estimation only imposes the identifying restrictions and ignores the overidentifying restrictions. The latter represent  $q - p$ restrictions which are true if equation (1) is itself true. To motivate the most commonly applied test statistic, it is useful to recall two aspects of our discussion above: (i) the GMM minimand measures the distance of  $\mathbf{g}_T(\boldsymbol{\theta})$  from zero; and (ii) the estimated sample moment contains information about overidentifying restrictions. Combining (i) and (ii), it can be shown that GMM minimand evaluated at  $\hat{\theta}_T$  is a measure of how far the sample is from satisfying the overidentifying restrictions. This leads to the overidentifying restrictions test

statistic,

$$J_T = T \mathbf{g}_T (\hat{\boldsymbol{\theta}}_T)' \hat{\mathbf{S}}_T^{-1} \mathbf{g}_T (\hat{\boldsymbol{\theta}}_T) \tag{10}$$

which converges to a  $\chi_{q-p}^2$  distribution under the null hypothesis that equation (1) holds. Notice that  $J_T$  is conveniently calculated as the sample size times the two-step (or iterated) GMM minimand evaluated at the associated estimator. The overidentifying restrictions test is the standard model diagnostic within the GMM framework. Nevertheless,  $J_T$  does not have power against all alternatives of interest: Ghysels and Hall [5] show that  $J_T$  has no (local) power against parameter variation and so it is prudent to complement the overidentifying restrictions test with tests of structural stability ([6], Section 5.4).

As noted above, there is evidence that in some cases of interest, the aforementioned (standard) asymptotic theory can provide a poor approximation to the finite sample performance of the GMM estimator and its associated inference techniques. This has prompted researchers to develop ways of ameliorating these deficiencies. The proposed methods fall into three basic categories: (i) methods for *moment selection*, which are designed to determine the "best" set of moments to use with a view to then basing inference on the standard asymptotic theory described above; (ii) resampling methods such as the *bootstrap* that are valid under similar assumptions to the standard theory but aim to provide more accurate approximations to finite sample behavior; and (iii) alternative asymptotic theories that are based on different assumptions to the standard framework and are designed to provide more accurate approximations in certain scenarios of interest, such as weak identifi*cation.* For further discussion of  $(i)$ – $(iii)$ , see  $(6]$ , Chapters 6, 7, and 8).

### References

- [1] Anatolyev, S. (2005). GMM, GEL, Serial correlation, and asymptotic bias, *Econometrica* **73**, 983–1002.
- [2] Andrews, D. (1991). Heteroscedasticity and autocorrelation consistent covariance matrix estimation, Econometrica 59, 817-858.
- Antoine, B., Bonnal, H. & Renault, E. (2007). On the [3] efficient use of the informational content of estimating equations: implied probabilities and Euclidean Empirical Likelihood, Journal of Econometrics 138, 461-487.
- [4] Chamberlain, G. (1987). Asymptotic efficiency in estimation with conditional moment restrictions, Journal of Econometrics 34, 305-334.

- [5] Ghysels, E. & Hall, A. (1990). Are consumption based intertemporal asset pricing models structural? *Journal of Econometrics* **45**, 121–139.
- [6] Hall, A. (2005). *Generalized Method of Moments*, Oxford University Press, Oxford, UK.
- [7] Hansen, L. (1982). Large sample properties of Generalized Method of Moments estimators, *Econometrica* **50**, 1029–1054.
- [8] Hansen, L., Heaton, J. & Yaron, A. (1996). Finite sample properties of some alternative GMM estimators obtained from financial market data, *Journal of Business and Economic Statistics* **14**, 262–280.
- [9] Hansen, L. & Hodrick, R. (1980). Forward exchange rates as optimal predictors of future spot rates, *Journal of Political Economy* **87**, 829–853.
- [10] Hansen, L. & Singleton, K. (1982). Generalized instrumental variables estimation of nonlinear rational expectations models, *Econometrica* **50**, 1269–1286.

- [11] Melino, A. & Turnbull, S. (1990). Pricing foreign currency options with stochastic volatility, *Journal of Econometrics* **45**, 239–266.
- [12] Newey, W. & Smith, R. (2004). Higher order properties of GMM and generalized empirical likelihood estimators, *Econometrica* **72**, 219–255.
- [13] Newey, W. & West, K. (1987). A simple positive semi–definite heteroscedasticity and autocorrelation consistent covariance matrix, *Econometrica* **55**, 703–708.
- [14] Newey, W. & West, K. (1994). Automatic lag selection in covariance matrix estimation, *Review of Economic Studies* **61**, 631–653.
- [15] Wooldridge, J. (2002). *Econometric Analysis of Cross Section and Panel Data*, MIT Press, Cambridge, MA.

ALASTAIR R. HALL
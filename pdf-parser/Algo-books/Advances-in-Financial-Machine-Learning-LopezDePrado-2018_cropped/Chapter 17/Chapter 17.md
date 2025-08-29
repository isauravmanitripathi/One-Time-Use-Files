School Press.

- 18. Ledoit, O. and M. Wolf (2003): "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection." *Journal of Empirical Finance* , Vol. 10, No. 5, pp. 603–621.
- 19. Raffinot, T. (2017): "Hierarchical clustering based asset allocation." *Journal of Portfolio Management* , forthcoming.
- 20. Rokach, L. and O. Maimon (2005): "Clustering methods," in Rokach, L. and O. Maimon, eds., *Data Mining and Knowledge Discovery Handbook* . Springer, pp. 321–352.

## **Notes**

1 A short version of this chapter appeared in the *Journal of Portfolio Management,* Vo1. 42, No. 4, pp. 59–69, Summer of 2016.

- 2 For additional metrics see:
  - [http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.p](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html) dist.html
  - http://docs.scipy.org/doc/scipy-[0.16.0/reference/generated/scipy.cluster.hierarchy.linkage.html](http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.cluster.hierarchy.linkage.html)

# **PART 4**

# **Useful Financial Features**

- 1. [Chapter 17 Structural Breaks](#page-0-0)
- 2. Chapter 18 Entropy Features
- 3. Chapter 19 Microstructural Features

# <span id="page-0-0"></span>**CHAPTER 17**

# **Structural Breaks**

## **17.1 Motivation**

In developing an ML-based investment strategy, we typically wish to bet when there is a confluence of factors whose predicted outcome offers a favorable risk-adjusted return. Structural breaks, like the transition from one market regime to another, is one example of such a confluence that is of particular interest. For instance, a mean-reverting pattern may give way to a momentum pattern. As this transition takes place, most market participants are caught off guard, and they will make costly mistakes. This sort of errors is the basis for many profitable strategies, because the actors on the losing side will typically become aware of their mistake once it is too late. Before they accept their losses, they will act irrationally, try to hold the position, and hope for a comeback. Sometimes they will even increase a losing position, in desperation. Eventually they will be forced to stop loss or stop out. Structural breaks offer some of the best risk/rewards. In this chapter, we will review some methods that measure the likelihood of structural breaks, so that informative features can be built upon them.

# **17.2 Types of Structural Break Tests**

We can classify structural break tests in two general categories:

- **CUSUM tests:** These test whether the cumulative forecasting errors significantly deviate from white noise.
- **Explosiveness tests:** Beyond deviation from white noise, these test whether the process exhibits exponential growth or collapse, as this is inconsistent with a random walk or stationary process, and it is unsustainable in the long run.
  - **Right-tail unit-root tests:** These tests evaluate the presence of exponential growth or collapse, while assuming an autoregressive specification.
  - **Sub/super-martingale tests:** These tests evaluate the presence of exponential growth or collapse under a variety of functional forms.

## **17.3 CUSUM Tests**

In Chapter 2 we introduced the CUSUM filter, which we applied in the context of event-based sampling of bars. The idea was to sample a bar whenever some variable, like cumulative prediction errors, exceeded a predefined threshold. This concept can be further extended to test for structural breaks.

### **17.3.1 Brown-Durbin-Evans CUSUM Test on Recursive Residuals**

This test was proposed by Brown, Durbin and Evans [1975]. Let us assume that at every observation *t* = 1, …, *T* , we count with an array of features *x <sup>t</sup>* predictive of a value *y <sup>t</sup>* . Matrix *X <sup>t</sup>* is composed of the time series of features *t* ≤ *T* , { *x <sup>i</sup>* } *<sup>i</sup>* <sup>=</sup> 1, …, *<sup>t</sup>* . These authors propose that we compute recursive least squares (RLS) estimates of β, based on the specification

$$y_t = \boldsymbol{\beta}_t' \boldsymbol{x}_t + \boldsymbol{\varepsilon}_t$$

which is fit on subsamples ([1, *k* + 1], [1, *k* + 2], …, [1, *T* ]), giving *T* − *k* least squares estimates . We can compute the standardized 1-step ahead recursive residuals as

$$\hat{\omega}_t = \frac{y_t - \hat{\beta}'_{t-1} x_t}{\sqrt{f_t}}$$
$$f_t = \hat{\sigma}_{\varepsilon}^2 \Big[ 1 + x'_t \big( X'_t X_t \big)^{-1} x_t$$

The CUSUM statistic is defined as

$$S_{t} = \sum_{j=k+1}^{t} \frac{\hat{\omega}_{j}}{\hat{\sigma}_{\omega}}$$
$$\hat{\sigma}_{\omega}^{2} = \frac{1}{T-k} \sum_{t=k}^{T} (\hat{\omega}_{t} - \mathbf{E}[\hat{\omega}_{t}])^{2}$$

Under the null hypothesis that β is some constant value, *H <sup>0</sup>* : β *<sup>t</sup>* = β, then *S <sup>t</sup>* ∼ *N* [0, *t* − *k* − 1]. One caveat of this procedure is that the starting point is chosen arbitrarily, and results may be inconsistent due to that.

## **17.3.2 Chu-Stinchcombe-White CUSUM Test on Levels**

This test follows Homm and Breitung [2012]. It simplifies the previous method by dropping { *x <sup>t</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* , and assuming that *H <sup>0</sup>* : β *<sup>t</sup>* = 0, that is, we forecast

no change (E *<sup>t</sup>* <sup>−</sup> <sup>1</sup> [Δ *y <sup>t</sup>* ] = 0). This will allow us to work directly with *y <sup>t</sup>* levels, hence reducing the computational burden. We compute the standardized departure of log-price *y <sup>t</sup>* relative to the log-price at *y <sup>n</sup>* , *t* > *n* , as

$$S_{n,t} = (y_t - y_n) \left(\hat{\sigma}_t \sqrt{t - n}\right)^{-1}$$
$$\hat{\sigma}_t^2 = (t - 1)^{-1} \sum_{i=2}^t (\Delta y_i)^2$$

Under the null hypothesis *H <sup>0</sup>* : β *<sup>t</sup>* = 0, then *S <sup>n</sup> , <sup>t</sup>* ∼ *N* [0, 1]. The timedependent critical value for the *one-sided test* is

$$c_{\alpha}[n,t] = \sqrt{b_{\alpha} + \log[t-n]}$$

These authors derived via Monte Carlo that *b 0.05* = 4.6. One disadvantage of this method is that the reference level *y <sup>n</sup>* is set somewhat arbitrarily. To overcome this pitfall, we could estimate *S <sup>n</sup> , <sup>t</sup>* on a series of backward-shifting windows *n* ∈ [1, *t* ], and pick .

## **17.4 Explosiveness Tests**

Explosiveness tests can be generally divided between those that test for one bubble and those that test for multiple bubbles. In this context, bubbles are not limited to price rallies, but they also include sell-offs. Tests that allow for multiple bubbles are more robust in the sense that a cycle of bubble-burstbubble will make the series appear to be stationary to single-bubble tests. Maddala and Kim [1998], and Breitung [2014] offer good overviews of the literature.

## **17.4.1 Chow-Type Dickey-Fuller Test**

A family of explosiveness tests was inspired by the work of Gregory Chow, starting with Chow [1960]. Consider the first order autoregressive process

$$y_t = \rho y_{t-1} + \varepsilon_t$$

where  $\epsilon_t$  is white noise. The null hypothesis is that  $y_t$  follows a random walk,  $H_0$ :  $\rho = 1$ , and the alternative hypothesis is that  $y_t$  starts as a random walk but changes at time  $\tau^* T$ , where  $\tau^* \in (0, 1)$ , into an explosive process:

$$H_1: y_t = \begin{cases} y_{t-1} + \varepsilon_t \text{ for } t = 1, \dots, \tau^* T \\ \rho y_{t-1} + \varepsilon_t \text{ for } t = \tau^* T + 1, \dots, T, \text{ with } \rho > 1 \end{cases}$$

At time  $T$  we can test for a switch (from random walk to explosive process) having taken place at time  $\tau^*$  *T* (break date). In order to test this hypothesis, we fit the following specification,

$$\Delta y_t = \delta y_{t-1} D_t[\tau^*] + \varepsilon_t$$

where  $D_t[\tau^*]$  is a dummy variable that takes zero value if  $t < \tau^* T$ , and takes the value one if  $t \ge \tau^* T$ . Then, the null hypothesis  $H_0$ :  $\delta = 0$  is tested against the (one-sided) alternative  $H_1$ :  $\delta > 1$ :

$$DFC_{\tau^*} = \frac{\hat{\delta}}{\hat{\sigma}_{\delta}}$$

The main drawback of this method is that  $\tau^*$  is unknown. To address this issue, Andrews [1993] proposed a new test where all possible  $\tau^*$  are tried, within some interval  $\tau^* \in [\tau_0, 1 - \tau_0]$ . As Breitung [2014] explains, we should leave out some of the possible  $\tau^*$  at the beginning and end of the sample, to ensure that either regime is fitted with enough observations (there must be enough zeros and enough ones in  $D_{t}[\tau^{*}]$ ). The test statistic for an unknown  $\tau^{*}$  is the maximum of all  $T(1 - 2\tau_0)$  values of  $DFC_{\tau^*}$ .

$$SDFC = \sup_{\tau^* \in [\tau_0, 1 - \tau_0]} \{DFC_{\tau^*}\}\$$

Another drawback of Chow's approach is that it assumes that there is only one break date  $\tau^* T$ , and that the bubble runs up to the end of the sample (there is no switch back to a random walk). For situations where three or more regimes (random walk  $\rightarrow$  bubble  $\rightarrow$  random walk ...) exist, we need to discuss the Supremum Augmented Dickey-Fuler (SADF) test.

### **17.4.2 Supremum Augmented Dickey-Fuller**

In the words of Phillips, Wu and Yu [2011], "standard unit root and cointegration tests are inappropriate tools for detecting bubble behavior because they cannot effectively distinguish between a stationary process and a periodically collapsing bubble model. Patterns of periodically collapsing bubbles in the data look more like data generated from a unit root or stationary autoregression than a potentially explosive process." To address this flaw, these authors propose fitting the regression specification

$$\Delta y_t = \alpha + \beta y_{t-1} + \sum_{l=1}^{L} \gamma_l \Delta y_{t-l} + \varepsilon_t$$

where we test for  $H_0: \beta \le 0$ ,  $H_1: \beta > 0$ . Inspired by Andrews [1993], Phillips and Yu [2011] and Phillips, Wu and Yu [2011] proposed the Supremum Augmented Dickey-Fuller test (SADF). SADF fits the above regression at each end point  $t$  with backwards expanding start points, then computes

$$SADF_{t} = \sup_{t_{0} \in [1, t-\tau]} \{ADF_{t_{0},t}\} = \sup_{t_{0} \in [1, t-\tau]} \left\{\frac{\hat{\beta}_{t_{0},t}}{\hat{\sigma}_{\beta_{t_{0},t}}}\right\}$$

where  $\hat{\beta}_{t_0,t}$  is estimated on a sample that starts at  $t_0$  and ends at  $t$ , τ is the minimum sample length used in the analysis,  $t_0$  is the left bound of the backwards expanding window, and  $t = \tau$ , ...,  $T$ . For the estimation of *SADF*<sub>t</sub>, the right side of the window is fixed at  $t$ . The standard ADF test is a special case of *SADF*<sub> $t$ </sub>, where  $\tau = t - 1$ .

There are two critical differences between  $SADF_t$  and  $SDFC$ : First,  $SADF_t$  is computed at each  $t \in [\tau, T]$ , whereas SDFC is computed only at *T*. Second, instead of introducing a dummy variable, SADF recursively expands the beginning of the sample ( $t_0 \in [1, t - \tau]$ ). By trying all combinations of a nested double loop on  $(t_0, t)$ , SADF does not assume a known number of regime switches or break dates. Figure 17.1 displays the series of E-mini S&P 500 futures prices after applying the ETF trick (Chapter 2, Section 2.4.1), as well as the SADF derived from that price series. The SADF line spikes when prices exhibit a bubble-like behavior, and returns to low levels when the bubble bursts. In the following sections, we will discuss some enhancements to Phillips' original SADF method.

![](_page_6_Figure_1.jpeg)

![](_page_6_Figure_2.jpeg)

## *17.4.2.1 Raw vs. Log Prices*

It is common to find in the literature studies that carry out structural break tests on raw prices. In this section we will explore why log prices should be preferred, particularly when working with long time series involving bubbles and bursts.

For raw prices { *y <sup>t</sup>* }, if ADF's null hypotesis is rejected, it means that prices are stationary, with finite variance. The implication is that returns are not time invariant, for returns' volatility must decrease as prices rise and increase as prices fall in order to keep the price variance constant. When we run ADF on raw prices, we assume that returns' variance is not invariant to price levels. If returns variance happens to be invariant to price levels, the model will be structurally heteroscedastic.

In contrast, if we work with log prices, the ADF specification will state that

 $\Delta \log[y_t] \propto \log[y_{t-1}]$ 

Let us make a change of variable,  $x_t = ky_t$ . Now,  $\log[x_t] = \log[k] + \log[y_t]$ , and the ADF specification will state that

$$\Delta \log[x_t] \propto \log[x_{t-1}] \propto \log[y_{t-1}]$$

Under this alternative specification based on log prices, price levels condition returns' mean, not returns' volatility. The difference may not matter in practice for small samples, where  $k \approx 1$ , but SADF runs regressions across decades and bubbles produce levels that are significantly different between regimes ( $k \neq 1$ ).

#### **17.4.2.2 Computational Complexity**

The algorithm runs in  $\mathcal{O}(n^2)$ , as the number of ADF tests that SADF requires for a total sample length *T* is

$$\sum_{t=\tau}^{T} t - \tau + 1 = \frac{1}{2}(T - \tau + 2)(T - \tau + 1) = \begin{pmatrix} T - \tau + 2 \\ 2 \end{pmatrix}$$

<span id="page-7-1"></span>Consider a matrix representation of the ADF specification, where  $X \in \mathbb{R}^{T \times N}$ and  $y \in \mathbb{R}^{T \times 1}$ . Solving a single ADF regression involves the floating point operations (FLOPs) listed in **Table 17.1**.

#### <span id="page-7-0"></span>**Table 17.1 FLOPs per ADF Estimate**

| <b>Matrix Operation</b> | FLOPs             |
|-------------------------|-------------------|
| $o_1 = X'y$             | $(2T - 1)N$       |
| $o_2 = X'X$             | $(2T-1)N^2$       |
| $o_3 = o^{-1}$          | $N^3 + N^2 + N$   |
| $o_4 = o_3 o_1$         | $2N^2-N$          |
| $o_5 = y - Xo_4$        | $ T + (2N - 1)T $ |
| $o_6 = o_5 o_5$         | $2T - 1$          |
|                         | $2 + N^2$         |

| $o_7 = o_3 o_6 \frac{\ }{T}$ |  |
|------------------------------|--|
| $o_4[0,0]$                   |  |
| $O_8$<br>$\sqrt{o_7[0,0]}$   |  |

This gives a total of  $f(N, T) = N^3 + N^2(2T + 3) + N(4T - 1) + 2T + 2$ FLOPs per ADF estimate. A single SADF update requires  $g(N, T, \tau) = \sum_{t=\tau}^{T} f(N, t) + T - \tau$  FLOPs ( $T - \tau$  operations to find the maximum ADF stat), and the estimation of a full SADF series requires  $\sum_{t=\tau}^{T} g(N, T, \tau)$ .

Consider a dollar bar series on E-mini S&P 500 futures. For  $(T, N)$  = (356631, 3), an ADF estimate requires 11,412,245 FLOPs, and a SADF update requires 2,034,979,648,799 operations (roughly 2.035 TFLOPs). A full SADF time series requires 241,910,974,617,448,672 operations (roughly 242 PFLOPs). This number will increase quickly, as the  $T$  continues to grow. And this estimate excludes notoriously expensive operations like alignment, preprocessing of data, I/O jobs, etc. Needless to say, this algorithm's double loop requires a large number of operations. An HPC cluster running an efficiently parallelized implementation of the algorithm may be needed to estimate the SADF series within a reasonable amount of time. Chapter 20 will present some parallelization strategies useful in these situations.

#### 17.4.2.3 Conditions for Exponential Behavior

Consider the zero-lag specification on log prices,  $\Delta \log[y_t] = \alpha + \beta \log[y_{t-1}]$ +  $\epsilon_t$ . This can be rewritten as  $\log[\tilde{y}_t] = (1 + \beta)\log[\tilde{y}_{t-1}] + \epsilon_t$ , where  $\log[\tilde{y}_t] = \log[y_t] + \frac{\alpha}{\beta}$ . Rolling back *t* discrete steps, we obtain  $\mathrm{E}[\log[\tilde{y}_t]] = (1+\beta)^t \log[\tilde{y}_0], \text{ or } \mathrm{E}[\log[y_t]] = -\frac{\alpha}{\beta} + (1+\beta)^t (\log[y_0] + \frac{\alpha}{\beta}). \text{ The}$ index *t* can be reset at a given time, to project the future trajectory of  $y_0 \rightarrow y_t$ after the next  $t$  steps. This reveals the conditions that characterize the three states for this dynamic system:

- Steady:  $\beta < 0 \Rightarrow \lim_{t \to \infty} \mathrm{E}[\log[y_t]] = -\frac{\alpha}{\beta}.$ <br>
  The disequilibrium is  $\log[y_t] (-\frac{\alpha}{\beta}) = \log[\tilde{y}_t].$ 
  - Then  $\frac{\mathrm{E}[\log[\bar{y}_t]]}{\log[\bar{y}_0]} = (1+\beta)^t = \frac{1}{2}$  at  $t = -\frac{\log[2]}{\log[1+\beta]}$  (half-life).
- Unit-root:  $\beta = 0$ , where the system is non-stationary, and behaves as a martingale.

• Explosive:  $\beta > 0$ , where  $\lim_{t \to \infty} \mathbb{E}[\log[y_t]] = \begin{cases} -\infty, & \text{if } \log [y_0] < \frac{\alpha}{\beta} \\ +\infty, & \text{if } \log [y_0] > \frac{\alpha}{\alpha} \end{cases}$ .

### 17.4.2.4 Quantile ADF

SADF takes the supremum of a series on t-values,

 $SADF_t = \sup_{t_0 \in [1, t-\tau]} \{ADF_{t_0, t}\}\.$  Selecting the extreme value introduces some robustness problems, where SADF estimates could vary significantly depending on the sampling frequency and the specific timestamps of the samples. A more robust estimator of ADF extrema would be the following: First, let  $s_t = \{ADF_{t_0,t}\}_{t_0 \in [0,t_1-\tau]}$ . Second, we define  $Q_{t,q} = Q[s_t, q]$  the  $q$ quantile of  $s_t$ , as a measure of centrality of high ADF values, where  $q \in [0,$ 1]. Third, we define  $\dot{Q}_{t,q,v} = Q_{t,q+v} - Q_{t,q-v}$ , with  $0 < v \le \min\{q, 1-q\}$ , as a measure of dispersion of high ADF values. For example, we could set  $q = 0.95$ and  $v = 0.025$ . Note that SADF is merely a particular case of QADF, where  $SADF_t = Q_{t,1}$  and  $\dot{Q}_{t,q,v}$  is not defined because  $q = 1$ .

## 17.4.2.5 Conditional ADF

Alternatively, we can address concerns on SADF robustness by computing conditional moments. Let  $f \, [ \, x \, ]$  be the probability distribution function of  $s_t = \{ADF_{t_0,t}\}_{t_0 \in [1,t_1-\tau]}$ , with  $x \in s_t$ . Then, we define  $C_{t,q} = K^{-1} \int_{Qt,q}^{\infty} xf[t]$  $x$  ]  $dx$  as a measure of centrality of high ADF values, and  $\dot{C}_{t,q} = \sqrt{K^{-1} \int_{Q_{t,q}}^{\infty} (x - C_{t,q})^2 f[x] dx}$  as a measure of dispersion of high ADF values, with regularization constant  $K = \int_{Q_{ta}}^{\infty} f[x] dx$ . For example, we could use  $q = 0.95$ .

By construction,  $C_{t,q} \leq SADF_t$ . A scatter plot of  $SADF_t$  against  $C_{t,q}$  shows that lower boundary, as an ascending line with approximately unit gradient (see <u>Figure 17.2</u>). When SADF grows beyond  $-1.5$ , we can appreciate some horizontal trajectories, consistent with a sudden widening of the right fat tail in  $s_t$ . In other words,  $(SADF_t - C_{t,a})/\dot{C}_{t,a}$  can reach significantly large values even if  $C_{t,q}$  is relatively small, because *SADF*<sub>t</sub> is sensitive to outliers.

![](_page_10_Figure_0.jpeg)

**Figure 17.2** SADF (x-axis) vs CADF (y-axis)

Figure 17.3 (a) plots for the E-mini S&P 500 futures prices over time. Figure 17.3 (b) is the scatter-plot of against *SADF <sup>t</sup>* , computed on the E-mini S&P 500 futures prices. It shows evidence that outliers in *s<sup>t</sup>* bias *SADF <sup>t</sup>* upwards.

![](_page_11_Figure_0.jpeg)

**Figure 17.3** (a) over time (b) (y-axis) as a function of *SADF <sup>t</sup>* (x-axis)

#### *17.4.2.6 Implementation of SADF*

This section presents an implementation of the SADF algorithm. The purpose of this code is not to estimate SADF quickly, but to clarify the steps involved in its estimation. Snippet 17.1 lists SADF's inner loop. That is the part that estimates , which is the backshifting component of the

algorithm. The outer loop (not shown here) repeats this calculation for an advancing *t* , { *SADF <sup>t</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* . The arguments are:

- logP : a pandas series containing log-prices
- minSL : the minimum sample length (τ), used by the final regression
- constant : the regression's time trend component
  - 'nc' : no time trend, only a constant
  - 'ct' : a constant plus a linear time trend
  - 'ctt' : a constant plus a second-degree polynomial time trend
- lags : the number of lags used in the ADF specification

## **SNIPPET 17.1 SADF'S INNER LOOP**

Snippet 17.2 lists function getXY , which prepares the numpy objects needed to conduct the recursive tests.

## **SNIPPET 17.2 PREPARING THE DATASETS**

Snippet 17.3 lists function lagDF , which applies to a dataframe the lags specified in its argument lags .

## **SNIPPET 17.3 APPLY LAGS TO DATAFRAME**

Finally, Snippet 17.4 lists function getBetas , which carries out the actual regressions.

## **SNIPPET 17.4 FITTING THE ADF SPECIFICATION**

```
def getBetas(y,x):
   xy = np.dot(x.T,y)xx = np.dot(x.T,x)xxinv = np.linalg.inv(xx)bMean=np.dot(xxinv,xy)
   err=y - np.dot(x, bMean)bVar = np.dot(err.T,err)/(x.shape[0] - x.shape[1]) * xxinvreturn bMean, bVar
```

## **17.4.3 Sub- and Super-Martingale Tests**

In this section we will introduce explosiveness tests that do not rely on the standard ADF specification. Consider a process that is either a sub- or supermartingale. Given some observations  $\{y_t\}$ , we would like to test for the existence of an explosive time trend,  $H_0: \beta = 0, H_1: \beta \neq 0$ , under alternative specifications:

• Polynomial trend (SM-Poly1):

$$y_t = \alpha + \gamma t + \beta t^2 + \varepsilon_t$$

• Polynomial trend (SM-Poly2):

$$\log[y_t] = \alpha + \gamma t + \beta t^2 + \varepsilon_t$$

• Exponential trend (SM-Exp):

$$y_t = \alpha e^{\beta t} + \varepsilon_t \Rightarrow \log[y_t] = \log[\alpha] + \beta t + \xi_t$$

• Power trend (SM-Power):

$$y_t = \alpha t^{\beta} + \varepsilon_t \Rightarrow \log[y_t] = \log[\alpha] + \beta \log[t] + \xi_t$$

Similar to SADF, we fit any of these specifications to each end point  $t = \tau$ , ...,  $T$ , with backwards expanding start points, then compute

$$SMT_{t} = \sup_{t_{0} \in [1, t-\tau]} \left\{ \frac{\left| \hat{\beta}_{t_{0}, t} \right|}{\hat{\sigma}_{\beta_{t_{0}, t}}} \right\}$$

The reason for the absolute value is that we are equally interested in explosive growth and collapse. In the simple regression case (Greene [2008], p. 48), the variance of β is , hence . The same result is generalizable to the multivariate linear regression case (Greene [2008], pp. 51– 52). The of a weak long-run bubble may be smaller than the of a strong short-run bubble, hence biasing the method towards long-run bubbles. To correct for this bias, we can penalize large sample lengths by determining the coefficient φ ∈ [0, 1] that yields best explosiveness signals.

$$SMT_{t} = \sup_{t_{0} \in [1, t-\tau]} \left\{ \frac{\left| \hat{\beta}_{t_{0}, t} \right|}{\hat{\sigma}_{\beta_{t_{0}, t}} (t - t_{0})^{\varphi}} \right\}$$

For instance, when φ = 0.5, we compensate for the lower associated with longer sample lengths, in the simple regression case. For φ → 0, *SMT <sup>t</sup>* will exhibit longer trends, as that compensation wanes and long-run bubbles mask short-run bubbles. For φ → 1, *SMT <sup>t</sup>* becomes noisier, because more short-run bubbles are selected over long-run bubbles. Consequently, this is a natural way to adjust the explosiveness signal, so that it filters opportunities targeting a particular holding period. The features used by the ML algorithm may include *SMT <sup>t</sup>* estimated from a wide range of φ values.

## **Exercises**

- 1. On a dollar bar series on E-mini S&P 500 futures,
  - 1. Apply the Brown-Durbin-Evans method. Does it recognize the dotcom bubble?
  - 2. Apply the Chu-Stinchcombe-White method. Does it find a bubble in 2007–2008?
- 2. On a dollar bar series on E-mini S&P 500 futures,

- 1. Compute the *SDFC* (Chow-type) explosiveness test. What break date does this method select? Is this what you expected?
- 2. Compute and plot the SADF values for this series. Do you observe extreme spikes around the dot-com bubble and before the Great Recession? Did the bursts also cause spikes?
- 3. Following on exercise 2,
  - 1. Determine the periods where the series exhibited
    - 1. Steady conditions
    - 2. Unit-Root conditions
    - 3. Explosive conditions
  - 2. Compute QADF.
  - 3. Compute CADF.
- 4. On a dollar bar series on E-mini S&P 500 futures,
  - 1. Compute SMT for SM-Poly1 and SM-Poly 2, where φ = 1. What is their correlation?
  - 2. Compute SMT for SM-Exp, where φ = 1 and φ = 0.5. What is their correlation?
  - 3. Compute SMT for SM-Power, where φ = 1 and φ = 0.5. What is their correlation?
- 5. If you compute the reciprocal of each price, the series { *y <sup>−</sup> <sup>1</sup> t* } turns bubbles into bursts and bursts into bubbles.
  - 1. Is this transformation needed, to identify bursts?
  - 2. What methods in this chapter can identify bursts without requiring this transformation?

## **References**

- 1. Andrews, D. (1993): "Tests for parameter instability and structural change with unknown change point." *Econometrics* , Vol. 61, No. 4 (July), pp. 821–856.
- 2. Breitung, J. and R. Kruse (2013): "When Bubbles Burst: Econometric Tests Based on Structural Breaks." *Statistical Papers* , Vol. 54, pp. 911– 930.
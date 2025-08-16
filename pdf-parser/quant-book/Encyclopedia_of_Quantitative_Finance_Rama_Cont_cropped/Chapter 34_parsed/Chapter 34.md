# **Heavy Tails**

The three most cited stylized properties attributed to log-returns of financial assets or stocks are (i) a kurtosis much larger than 3, the kurtosis of a normal distribution; (ii) serial dependence without correlation; and (iii) volatility clustering. Any realistic and useful model for log-returns must account for all three of these characteristics. In this article, the focus is on the large kurtosis property, which is indicative of heavy tails in the returns. Although this stylized fact may not draw the same level of attention as the other two, it can have a serious impact on modeling and inference questions related to financial time series. One such application is the estimation of the Value at Risk, which is an important entity in the finance industry. For example, financial institutions would like to estimate large quantiles of the absolute returns, that is, the level at which the probability that an absolute return exceeds this value is small such as 0.01 or less. The estimation of these large quantities is extremely sensitive to the shape assumed for the tail of the marginal distribution. A light-tailed assumption for the tails can severely underestimate the actual quantiles of the marginal distribution. In addition to Value at Risk, heavy tails can impact the estimation of key measures of dependencies in financial time series. This includes the sample autocorrelation of the time series and of functions of the time series such as absolute values and squares. Standard central limit theory for mixing sequences generally directly applies to the sample autocorrelation functions (ACFs) of a financial time series and its squares, provided the fourth and eight moments, respectively, are finite. If these moments are infinite, as well may be the case for financial time series, then the asymptotic behavior of the sample ACFs is often nonstandard. As it turns out, GARCH processes and stochastic volatility (SV) processes, which are the primary modeling engines for financial returns, exhibit heavy tails in the marginal distribution. We focus on heavy tails and how the concept of regular variation plays a vital role in both these processes.

It is often a misconception to associate heavytailed distributions with a very large variance. Rather, the term is used to describe data that exhibit bursts of outlying observations. These outlying observations could be orders of magnitude larger than the median of the observations. In the early 1960s, Mandelbrot (*see* **Mandelbrot, Benoit**) [31], Mandelbrot and Taylor [32], and Fama [21] realized that the marginal distribution of returns appeared to be heavy tailed. To cope with heavy tails, they considered non-Gaussian stable distributions for the marginals. Since this class of distributions has infinite variance, it was a slightly controversial approach. On the other hand, for many financial time series, there is evidence that the marginal distribution may have a finite variance but an infinite fourth moment. Figure 1 contains two financial time series that exhibit heavy tails. Figure 1(a) consists of the daily pound/US dollar exchange rate from October 1, 1981 to June 28, 1985, while Figure 1(b) displays the log-returns of the daily closing price of Merck stock from January 2, 2003 through April 28, 2006. One can certainly detect the occasional bursts of outlying observations in both series that are representative of heavy tails. As described in the second section (see Figure 3c and d), there is statistical evidence that the tail behavior of the marginal distribution is heavy with possibly infinite fourth moments.

Regular variation is a natural and often used concept to describe and model heavy-tailed phenomena. Many processes that are designed to model financial time series, such as the GARCH and heavytailed SV processes, have the property that all finitedimensional distributions are regularly varying. For such processes, one can apply standard results from extreme value theory for establishing limiting behavior of the extremes of the process, the sample ACF of the process and its squares, and a host of other statistics. The regular variation condition and its properties are described in the second section. In the third section, some of the main results on regular variation for GARCH and SV processes, respectively, are described. The fourth section describes some of the applications of the regular variation conditions mentioned in the third section, with emphasis on extreme values, point processes, and sample autocorrelations.

## **Regular Variation**

Multivariate regular variation plays an indispensable role in extreme value theory and often serves as the starting point for modeling multivariate extremes. In some respect, one can regard a random vector that is regularly varying as the heavy-tailed analog

![](_page_1_Figure_1.jpeg)

Figure 1 Log-returns for US/pound exchange rate, October 1, 1981 to June 28, 1985 (a) and log-returns for closing price of Merck stock, January 2, 2003 to April 28, 2006 (b)

of a Gaussian random vector. Unlike a Gaussian random vector, which is characterized by the mean vector and all pairwise covariances, a regular varying random vector in  $d$  dimensions is characterized by two components, an index  $\alpha > 0$  and a random vector  $\boldsymbol{\Theta}$  with values in  $\mathbb{S}^{d-1}$ , where  $\mathbb{S}^{d-1}$  denotes the unit sphere in  $\mathbb{R}^d$  with respect to the norm  $|\cdot|$ . The random vector  $\mathbf{X}$  is said to be *regularly varying* with index  $-\alpha$  if for all  $t > 0$ ,

$$\frac{P(|\mathbf{X}| > tu, \mathbf{X}/|\mathbf{X}| \in \cdot)}{P(|\mathbf{X}| > u)} \stackrel{v}{\to} t^{-\alpha} P(\mathbf{\Theta} \in \cdot)$$
  
as  $u \to \infty$  (1)

The symbol  $\stackrel{v}{\rightarrow}$  stands for vague convergence on  $\mathbb{S}^{d-1}$ ; vague convergence of measures is treated in detail in [27]. See [24, 36, 37] for background on multivariate regular variation. In this context, the convergence in equation (1) holds for all continuity sets  $A \in \mathcal{B}(\mathbb{S}^{d-1})$  of  $\Theta$ . In particular, equation (1) implies that the modulus of the random vector  $|X|$  is regularly varying, that is,

$$\lim_{u \to \infty} \frac{P(|\mathbf{X}| > t \, u)}{P(|\mathbf{X}| > u)} = t^{-\alpha} \tag{2}$$

Hence, roughly speaking, from the defining equation  $(1)$ , the modulus and angular parts of the random vector,  $|X|$  and  $X/|X|$ , are *independent* in the limit,

that is,

$$P(|\mathbf{X}/|\mathbf{X}| \in A||\mathbf{X}| > u) \to P(\mathbf{\Theta} \in A)$$
  
as  $u \to \infty$  (3)

The distribution of  $\Theta$  is often called the *spectral measure* of the regularly varying random vector. The modulus has power-law-like tails in the sense that

$$P(|\mathbf{X}| > x) = L(x)x^{-\alpha} \tag{4}$$

where  $L(x)$  is a slowly varying function, that is, for any  $t > 0$ ,  $L(tx)/L(x) \to 1$  as  $x \to \infty$ . This property implies that the rth moments of  $|X|$  are infinite for  $r > \alpha$  and finite for  $r < \alpha$ .

There is a second characterization of regular variation that is often useful in applications. Replacing u in equation (1) by the sequence  $a_n > 0$  satisfying,  $nP(|\mathbf{X}| > a_n) \rightarrow 1$  (i.e., we may take  $a_n$  to be the  $1 - n^{-1}$  quantile of  $|\mathbf{X}|$ ), we obtain

$$nP(|\mathbf{X}| > t \, a_n \, , \, \mathbf{X}/|\mathbf{X}| \in \cdot \, ) \xrightarrow{v} t^{-\alpha} P(\mathbf{\Theta} \in \cdot \, )$$
  
as  $n \to \infty$  (5)

As expected, the multivariate regular variation condition collapses to the standard condition in the one-dimensional case  $d = 1$ . In this case,  $\mathbb{S}^0 =$  $\{-1, 1\}$ , so that the random variable X is regular varying if and only if  $|X|$  is regularly varying

$$\lim_{u \to \infty} \frac{P(|X| > t u)}{P(|X| > u)} = t^{-\alpha} \tag{6}$$

and the tail balancing condition,

$$\lim_{u \to \infty} \frac{P(X > u)}{P(|X| > u)} = p \quad \text{and}$$
  
$$\lim_{u \to \infty} \frac{P(X < -u)}{P(|X| > u)} = q \tag{7}$$

holds, where  $p$  and  $q$  are nonnegative constants with  $p + q = 1$ . The Pareto distribution, *t*-distribution, and nonnormal stable distributions are all examples of one-dimensional distributions that are regularly varying.

**Example 1** (Independent components). Suppose that  $\mathbf{X} = (X_1, X_2)'$  consists of two independent and identically distributed (i.i.d.) components, where  $X_1$ is regularly varying random variable. The scatter plot of 10 000 replicates of these pairs, where  $X_1$  has a  $t$ -distribution with 3 degrees of freedom, is displayed in Figure 2(a). The  $t$ -distribution is regularly varying, with index  $\alpha$  being equal to the degrees of freedom. In this case, the spectral measure is a discrete distribution, which places equal mass at the intersection of the unit circle and the coordinate axes. That is,

$$P\left(\Theta = \frac{\pi k}{2}\right) = \frac{1}{4} \quad \text{for } k = -1, 0, 1, 2$$
 (8)

The scatter plot in Figure 2 reflects the form of the spectral distribution. The points that are far from the origin occur only near the coordinate axes. The interpretation is that the probability that both components of the random vector are large at the same time is quite small.

Example 2 (Totally Dependent Components). In contrast to the independent case of Example 1, suppose that both components of the vector are identical, that is,  $\mathbf{X} = (X, X)$ , with X regularly varying in one dimension. Independent replicates of this random vector would just produce points lying on a  $45^{\circ}$  line through the origin. Here, it is easy to see that the vector is regularly varying with spectral measure given by

$$P\left(\Theta = \frac{\pi}{4}\right) = p \quad \text{and} \quad P\left(\Theta = \frac{-\pi}{4}\right) = q \quad (9)$$

**Example 3** (AR(1) Process). Let  $\{X_t\}$  be the AR(1) process defined by the recursion:

$$X_t = 0.9X_{t-1} + Z_t \tag{10}$$

![](_page_2_Figure_14.jpeg)

**Figure 2** Scatter plot of 10 000 pairs of observations with i.i.d. components having a  $t$ -distribution with 3 degrees of freedom (a) and 10 000 observations of  $(X_t, X_{t+1})$  from an AR(1) process (b)

where  $\{Z_t\}$  is an i.i.d. sequence of random variables that have a symmetric stable distribution with exponent 1.8. This stable distribution is regularly varying with index  $\alpha = 1.8$ . Since  $X_t = \sum_{i=0}^{\infty} 0.9^i Z_{t-i}$  is a linear process, it follows [14, 15] that  $X_t$  is also symmetric and regularly varying with index 1.8. In fact,  $X_t$  has a symmetric stable distribution with exponent 1.8 and scale parameter  $(1 - 0.9^{1.8})^{-1/1.8}$ . The scatter plot of consecutive observations  $(X_t, X_{t+1})$  based on 10 000 observations generated from an AR(1) process is displayed in Figure  $2(b)$ . It can be shown that all finite-dimensional distributions of this time series are regularly varying. The spectral distribution of the vector consisting of two consecutive observations  $\mathbf{X} = (X_t, X_{t+1})$  is given by

$$P(\Theta = \pm \arctan(0.9)) = 0.9898$$
 and  
 $P(\Theta = \pm \pi/2) = 0.0102$  (11)

As seen in Figure 2, one can see that most of the points in the scatter plot, especially those far from the origin, cluster tightly around the line through the origin with slope 0.9. This corresponds to the large mass at  $arctan(0.9)$  of the distribution of  $\Theta$ . One can also detect a smattering of extreme points clustered around the vertical axis.

#### *Estimation of* $\alpha$

A great deal of attention in the extreme value theory community has been devoted to the estimation of  $\alpha$ in the regular variation condition (1). The generic Hill estimate is often a good starting point for this task. There are more sophisticated versions of Hill estimates, see [23] for a nice treatment of Hill estimators, but for illustration we stick with the standard version. For observations  $X_1, \ldots, X_n$  from a nonnegative-valued time series, let  $X_{n:1} > \cdots > X_{n:n}$ be the corresponding descending order statistics. If the data were in fact i.i.d. from a Pareto distribution, then the maximum likelihood estimator of  $\alpha^{-1}$  based on the largest  $m + 1$  order statistics is

$$\hat{\alpha}^{-1} = \frac{1}{m} \sum_{j=1}^{m} \left( \ln X_{n:j} - \ln X_{n:m+1} \right) \tag{12}$$

Different values of m produce an array of  $\alpha$ estimates. The typical operating procedure is to plot the estimate of  $\alpha$  versus *m* and choose a value of  $m$  where the plot appears horizontal for an extended segment. See [7, 37] for other procedures for selecting  $m$ . There is the typical bias *versus* variance trade-off, with larger  $m$  producing smaller variance but larger bias. Figure 3 contains graphs of the Hill estimate of  $\alpha$  as a function of *m* for the two simulated series in Figure 2 and the exchange rate and log-return data of Figure 1. In all cases, one can see a range of m for which the graph of  $\hat{\alpha}$  is relatively flat. Using this segment as an estimate of  $\alpha$ , we would estimate the index as approximately 3 for the two simulated series, approximately 3 for the exchange rate data, and around 3.5 for the stock price data. (The value of  $\alpha$  for the two simulated series is indeed 3.) Also displayed on the plots are  $95\%$ confidence intervals for  $\alpha$ , assuming the data are i.i.d. As suggested by these plots, the return data appear to have quite heavy tails.

#### *Estimation of the Spectral Distribution*

Using property (3), a naive estimate of the distribution of  $\Theta$  is based on the angular components  $\mathbf{X}_{t}/|\mathbf{X}_{t}|$  in the sample. One simply uses the empirical distribution of these angular pieces for which the modulus  $|X_t|$  exceeds some large threshold. More details can be found in [37]. For the scatter plots in Figure 2, we produced in Figure 4 kernel density estimates of the spectral density function for the random variable  $\Theta$  on  $(-\pi, \pi]$ . One can see in the graph of the i.i.d. data, the large spikes at values of  $\theta = -\pi, -\pi/2, 0, \pi/2, \pi$  corresponding to the coordinate axes (the values at  $-\pi$  and  $\pi$  should be grouped together). On the other hand for the  $AR(1)$  process, the density estimate puts large mass at  $\theta = \arctan(0.9)$  and  $\theta = \arctan(0.9) - \pi$  corresponding to the line with slope 0.9 in the first and third quadrants, respectively. Since there are only a few points on the vertical axis, the density estimate does not register much mass at 0 and  $\pi$ .

## Regular Variation for GARCH and SV Processes

### GARCH Processes

The autoregressive conditional heterscedastic (ARCH) process developed by Engle [19] and its generalized version, GARCH, developed by Engle

![](_page_4_Figure_1.jpeg)

Figure 3 Hill plots for tail index: (a) i.i.d. data in Figure 2; (b) AR(1) process in Figure 2; (c) log-returns for US/pound exchange rate; and (d) log-returns for Merck stock, January 2, 2003 to April 28, 2006

and Bollerslev [20] are perhaps the most popular models for financial time series (see GARCH Models). Although there are many variations of the GARCH process, we focus on the traditional version. We say that  $\{X_t\}$  is a GARCH $(p, q)$  process if it is a strictly stationary solution of the equations:

$$X_{t} = \sigma_{t} Z_{t}$$
  

$$\sigma_{t}^{2} = \alpha_{0} + \sum_{i=1}^{p} \alpha_{i} X_{t-i}^{2}$$
  

$$+ \sum_{j=1}^{q} \beta_{j} \sigma_{t-j}^{2}, \quad t \in \mathbb{Z}$$
(13)

where the *noise* or *innovations* sequence  $(Z_t)_{t \in \mathbb{Z}}$  is an i.i.d. sequence with mean zero and unit variance. It is usually assumed that all coefficients  $\alpha_i$  and  $\beta_i$  are nonnegative, with  $\alpha_0 > 0$ . For identification purposes, the variance of the noise is assumed to be 1 since otherwise its standard deviation can be absorbed into  $\sigma_t$ .  $(\sigma_t)$  is referred to as the *volatility* sequence of the GARCH process.

The parameters are typically chosen to ensure that a causal and strictly stationary solution to the equations (13) exists. This means that  $X_t$  has a representation as a measurable function of the past and present noise values  $Z_s$ ,  $s \le t$ . The necessary and sufficient conditions for the existence and uniqueness of a stationary ergodic solution to equation  $(13)$  are

![](_page_5_Figure_1.jpeg)

Figure 4 The estimation of the spectral density function for i.i.d. components (a) and for the  $AR(1)$  process (b) from Figure 2

given in [35] for the  $GARCH(1, 1)$  case and for the general GARCH $(p, q)$  case in [4]; see [30] for a summary of the key properties of a GARCH process. In some cases, one only assumes weak stationarity, in which case the conditions on the parameters reduce substantially. A GARCH process is weakly stationary if and only if

$$\alpha_0 > 0 \quad \text{and} \quad \sum_{j=1}^p \alpha_j + \sum_{j=1}^q \beta_j < 1 \tag{14}$$

To derive properties of the tail of the finitedimensional distributions of a GARCH process, including the marginal distribution, it is convenient to embed the squares  $X_t^2$  and  $\sigma_t^2$  in a stochastic recurrence equation (SRE). This embedding can be used to derive other key properties of the process beyond the finite-dimensional distributions. For example, conditions for stationarity and  $\beta$ -mixing can be established from the properties of SREs and general theory of Markov chains. Here, we focus on the tail behavior.

One builds an SRE by including the volatility process in the state vector. An SRE takes the form

$$\mathbf{Y}_t = \mathbf{A}_t \mathbf{Y}_{t-1} + \mathbf{B}_t \tag{15}$$

where  $\mathbf{Y}_t$  is an *m*-dimensional random vector,  $\mathbf{A}_t$ is an  $m \times m$  random matrix, **B**<sub>t</sub> is a random vector, and  $\{(\mathbf{A}_t, \mathbf{B}_t)\}$  is an i.i.d. sequence. Under suitable conditions on the coefficient matrices and error matrices, one can derive various properties about the Markov chain  $\mathbf{Y}_t$ . For example, iteration of equation (15) yields a unique stationary and causal solution:

$$\mathbf{Y}_{t} = \mathbf{B}_{t} + \sum_{i=1}^{\infty} \mathbf{A}_{t} \cdots \mathbf{A}_{t-i+1} \mathbf{B}_{t-i} , \quad t \in \mathbb{Z} \tag{16}$$

To ensure almost surely (a.s.) convergence of the infinite series in equation  $(16)$ , and hence the existence of a unique a strictly stationary solution to equation  $(15)$ , it is assumed that the *top Lyapunov exponent* given by

$$\gamma = \inf_{n \ge 1} n^{-1} E \log \|\mathbf{A}_n \cdots \mathbf{A}_1\| \tag{17}$$

is negative, where  $\|\cdot\|$  is the operator norm corresponding to a given norm in  $\mathbb{R}^m$ .

Now, the GARCH process, at least its squares, can be embedded into an SRE by choosing

 $(18)$ 

$$\mathbf{Y}_{t} = \begin{pmatrix} \sigma_{t+1}^{2} \\ \vdots \\ \sigma_{t-q+2}^{2} \\ X_{t}^{2} \\ \vdots \\ X_{t-p+1}^{2} \end{pmatrix}, \quad \mathbf{A}_{t} = \begin{pmatrix} \alpha_{1}Z_{t}^{2} + \beta_{1} & \beta_{2} & \cdots & \beta_{q-1} & \beta_{q} & \alpha_{2} & \alpha_{3} & \cdots & \alpha_{p} \\ 1 & 0 & \cdots & 0 & 0 & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 & 0 & 0 & 0 & \cdots & 0 \\ Z_{t}^{2} & 0 & \cdots & 0 & 0 & 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & 1 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & 0 & \cdots & 1 & 0 \end{pmatrix}$$
$$\mathbf{B}_{t} = (\alpha_{0}, 0, \ldots, 0)'$$

where, as required,  $\{(\mathbf{A}_t, \mathbf{B}_t)\}\$  is an i.i.d. sequence. The top row in the SRE for the GARCH specification follows directly from the definition of the squared volatility process  $\sigma_{t+1}^2$  and the property that  $X_t =$  $\sigma_t Z_t$ .

In general, the top Lyapunov coefficient  $\gamma$  for the GARCH SRE cannot be calculated explicitly. However, a sufficient condition for  $\gamma < 0$  is given as

$$\sum_{i=1}^{p} \alpha_i + \sum_{j=1}^{q} \beta_j < 1 \tag{19}$$

see p. 122 [4]. It turns out that this condition is also necessary and sufficient for the existence of a weakly stationary solution to the GARCH recursions. The solution will also be strictly stationary in this case.

It has been noted that for many financial time series, the  $GARCH(1,1)$  often provides an adequate model or is at least a good starter model. This is one of the few models where the Lyapunov coefficient can be computed explicitly. In this case, the SRE equation essentially collapses to the one-dimensional SRE given as

$$\sigma_{t+1}^2 = \alpha_0 + (\alpha_1 Z_t^2 + \beta_1) \sigma_t^2 = A_t \sigma_t^2 + \alpha_0 \tag{20}$$

where  $A_t = \alpha_1 Z_t^2 + \beta_1$ . The elements in the second row in the vector and matrix components of equation  $(18)$  play no role in this case. Hence,

$$\gamma = n^{-1} E \log \left( A_n \cdots A_1 \right) = E \log A_1$$
$$= E \log \left( \alpha_1 Z^2 + \beta_1 \right) \tag{21}$$

The conditions [35],  $E \log(\alpha_1 Z^2 + \beta_1) < 0$  and  $\alpha_0 > 0$ , are necessary and sufficient for the existence of a stationary causal nondegenerate solution to the  $GARCH(1,1)$  equations.

Once the squares and volatility sequence,  $X_t^2$  and  $\sigma_t^2$ , respectively, are embedded in an SRE, then one can apply classical theory for SREs as developed by Kesten [28], (see also [22]), and extended by Basrak et al. [2], to establish regular variation of the tails of  $X_t^2$  and  $\sigma_t^2$ . The following result by Basrak *et al.* [1] summarizes the key results applied to a GARCH process.

**Theorem 1** Consider the process  $(Y_t)$  in equation (18) obtained from embedding a stationary GARCH process into the SRE  $(18)$ . Assume that Z has a positive density on  $\mathbb{R}$  such that  $E(|Z|^h) < \infty$ for  $h < h_0$  and  $E(|Z|^{h_0}) = \infty$  for some  $h_0 \in (0, \infty]$ . Then with  $\mathbf{Y} = \mathbf{Y}_1$ , there exist  $\alpha > 0$ , a constant  $c > 0$ 0. and a random vector  $\boldsymbol{\Theta}$  on the unit sphere  $\mathbb{S}^{p+q-2}$ such that

$$x^{\alpha/2}P(|\mathbf{Y}| > x) \to c \quad \text{as } x \to \infty \tag{22}$$

and for every  $t > 0$ 

$$\frac{P(|\mathbf{Y}| > tx, \mathbf{Y}/|\mathbf{Y}| \in \cdot)}{P(|\mathbf{Y}| > x)} \xrightarrow{w} t^{-\alpha/2} P(\mathbf{\Theta} \in \cdot)$$
  
as  $x \to \infty$  (23)

where  $\stackrel{w}{\rightarrow}$  denotes weak convergence on the Borel  $\sigma$ -(i) field of  $\mathbb{S}^{p+q-2}$  a

It follows that the components of the vector of  $\mathbf{Y}$ are also regularly varying so that

$$P(|X_1| > x) \sim c_1 x^{-\alpha} \quad \text{and}$$
  
 
$$P(\sigma_1 > x) \sim c_2 x^{-\alpha} \tag{24}$$

for some positive constants  $c_1$  and  $c_2$ . A straightforward application of Breiman's lemma [6], (cf. [13], Section 4), allows us to remove the absolute values in  $X_1$  to obtain

$$P(X_1 > x) = P(\sigma_1 Z_1^+ > x)$$
  

$$\sim E((Z_1^+)^{\alpha}) P(\sigma_1 > x) \quad (25)$$
  

$$P(X_1 \leq -x) = P(-\sigma_1 Z_1^- \leq -x)$$
  

$$\sim E((Z_1^-)^{\alpha}) P(\sigma_1 > x) \quad (26)$$

where  $Z_1^{\pm}$  are the respective positive and negative parts of  $Z_1$ . With the exception of simple models such as the  $GARCH(1,1)$ , there is no explicit formula for the index  $\alpha$  of regular variation of the marginal distribution. In principle,  $\alpha$  could be estimated from the data using a Hill style estimator, but an enormous sample size would be required in order to obtain a precise estimate of the index.

In the GARCH(1,1) case,  $\alpha$  is found by solving the following equation:

$$E[(\alpha_1 Z^2 + \beta_1)^{\alpha/2}] = 1 \tag{27}$$

This equation can be solved for  $\alpha$  by numerical and/or simulation methods for fixed values of  $\alpha_1$  and  $\beta_1$  from the stationarity region of a GARCH(1,1) process and assuming a concrete density for Z. (See [12] for a table of values of  $\alpha$  for various choices of  $\alpha_1$  and  $\beta_1$ .) Note that in the case of an integrated GARCH (IGARCH) process where  $\alpha_1 + \beta_1 = 1$ , then we have  $\alpha = 2$ . This holds regardless of the distribution of  $Z_1$ , provided it has a finite variance. Since the marginal distribution of an IGARCH process has Pareto-like tails with index 2, the variance is infinite.

While equations  $(25)$  and  $(26)$  describe only the regular variation of the marginal distribution, it is also true that the finite-dimensional distributions are regularly varying. To see this in the  $GARCH(1,1)$ case, we note that the volatility process is given as

$$\sigma_{t+1}^2 = (\alpha_1 Z_t^2 + \beta_1)\sigma_t^2 + \beta_0 \tag{28}$$

so that

$$(\sigma_1^2, \dots, \sigma_m^2) = (1, \alpha_1 Z_1^2 + \beta_1, (\alpha_1 Z_2^2 + \beta_1) \times (\alpha_1 Z_1^2 + \beta_1), \dots, \alpha_1 Z_{m-1}^2 + \beta_1) \dots \times (\alpha_1 Z_1^2 + \beta_1) \sigma_1^2 + \mathbf{R}_m$$
  
=  $\mathbf{D}_m \sigma_1^2 + \mathbf{R}_m$  (29)

where  $\mathbf{R}_m$  has tails that are lighter than those for  $\sigma_1^2$ . Now since  $\mathbf{D}_m = (D_1, \ldots, D_m)$  is independent of  $\sigma_1^2$ and has a  $\alpha/2 + \delta$  moment for some  $\delta > 0$ , it follows by a generalization of Breiman's lemma [1] that

$$\mathbf{U}_m := (X_1^2, \dots, X_m^2) = \mathbf{F}_m \sigma_1^2 + \mathbf{R}_m \tag{30}$$

where  $\mathbf{F}_m = (Z_1^2 D_1, \ldots, Z_m^2 D_m)$  is regularly varying with

$$\lim_{x \to \infty} \frac{P(|\mathbf{U}_m| > x, \mathbf{U}_m/|\mathbf{U}_m| \in A)}{P(|\mathbf{U}_m| > x)}$$

$$= \lim_{x \to \infty} \frac{P(|\mathbf{F}_m|\sigma_1^2 > x, \mathbf{F}_m/|\mathbf{F}_m| \in A)}{P(|\mathbf{F}_m|\sigma_1^2 > x)}$$

$$= \frac{E\left(|\mathbf{F}_m|^{\alpha/2}I_A(\mathbf{F}_m/|\mathbf{F}_m|)\right)}{E|\mathbf{F}_m|^{\alpha/2}} \tag{31}$$

It follows that the finite-dimensional distributions of a GARCH process are regularly varying.

## Stochastic Volatility Processes

The SV process also starts with the multiplicative  $model(13)$ 

$$X_t = \sigma_t Z_t \tag{32}$$

with  $(Z_t)$  being an i.i.d. sequence of random variables. If  $\text{var}(Z_t) < \infty$ , then it is conventional to assume that  $Z_t$  has mean 0 and variance 1. Unlike the GARCH process, the volatility process  $(\sigma_t)$  for SV processes is assumed to be independent of the sequence  $(Z_t)$ . Often, one assumes that  $\log \sigma_t^2$  is a linear Gaussian process given by

$$\log \sigma_t^2 = Y_t = \mu + \sum_{j=0}^{\infty} \psi_j \eta_{t-j} \tag{33}$$

where  $(\psi_i)$  is a sequence of square summable coefficients and  $(\eta_t)$  is a sequence of i.i.d. N(0,  $\sigma^2$ ) random variables independent of  $(Z_t)$ . If  $\text{var}(Z_t)$  is

finite and equal to 1, then the SV process  $X_t =$  $\sigma_t Z_t = \exp^{Y_t/2} Z_t$  is white noise with mean 0 and variance  $\exp{\{\mu + \sigma^2 \sum_{j=0}^{\infty} \psi_j^2/2\}}$ . One advantage of such processes is that one can explicitly compute the autocovariance function (ACVF) of any power of  $X_t$ and its absolute values. For example, the ACVF of the squares of  $(X_t)$  is, for  $h > 0$ , given as

$$\begin{split} \gamma_{|X|^2}(h) &= E(\exp\{Y_0 + Y_h\}) - (E\exp\{Y_0\})^2 \\ &= \exp\left\{2\mu + \sigma^2 \sum_{i=0}^{\infty} \psi_i^2\right\} \\ &\times \left[\exp\left\{\sigma^2 \sum_{i=0}^{\infty} \psi_i \psi_{i+h}\right\} - 1\right] \\ &= e^{2\mu} e^{\gamma_Y(0)} \Big[e^{\gamma_Y(h)} - 1\Big] \end{split} \tag{34}$$

Note that as  $h \to \infty$ ,

$$\gamma_{|X|^2}(h) \sim e^{2\mu} e^{\gamma_Y(0)} \left[ e^{\gamma_Y(h)} - 1 \right] \sim e^{2\mu} e^{\gamma_Y(0)} \gamma_Y(h)$$
(35)

so that the ACVF of the SV for the squares converges to zero at the same rate as the log-volatility process.

If  $Z_t$  has a Gaussian distribution, then the tail of  $X_t$  remains light although a bit heavier than a Gaussian [3]. This is in contrast to the GARCH case where an i.i.d. Gaussian input leads to heavytailed marginals of the process. On the other hand, for SV processes, if the  $Z_t$  have heavy tails, for example, if  $Z_t$  has a *t*-distribution, then Davis and Mikosch [10] show that  $X_t$  is regularly varying. Furthermore, in this case, any finite collection of  $X_t$ 's has the same limiting joint tail behavior as an i.i.d. sequence with regularly varying marginals. Specifically, the two random vectors,  $(X_1, \ldots, X_k)'$ and  $(E|\sigma_1|^{\alpha})^{1/\alpha}(Z_1,\ldots,Z_k)'$  have the same joint tail behavior.

### **Limit Theory GARCH and SV Processes**

#### Convergence of Maxima

If  $(X_t)$  is a stationary sequence of random variables with common distribution function  $F$ , then often one can directly relate the limiting distribution of the maxima,  $M_n = \max\{X_1, \ldots, X_n\}$  to F. Assuming

that  $X_1$  is regularly varying with index  $-\alpha$  and choosing the sequence  $(a_n)$  such that  $n(1 - F(a_n)) \rightarrow 1$ , then

$$F^{n}(a_{n}x) \to G(x) = \begin{cases} 0, & x \le 0 \\ e^{-x^{-\alpha}}, & x > 0 \end{cases}$$
(36)

This relation is equivalent to convergence in distribution of the maxima of the associated independent sequence  $(\hat{X}_t)$  (i.e., the sequence  $(\hat{X}_t)$  is i.i.d. with common distribution function  $F$ ) normalized by  $a_n$ to the Fréchet distribution G. Specifically, if  $\hat{M}_n =$  $\max\{\hat{X}_1,\ldots,\hat{X}_n\}$ , then

$$P(a_n^{-1}M_n \le x) \to G(x) \tag{37}$$

Under mild mixing conditions on the sequence  $(X_t)$  $[29]$ , we have

$$P(a_n^{-1}M_n \le x) \to H(x) \tag{38}$$

with  $H$  a nondegenerate distribution function if and only if

$$H(x) = G^{\theta}(x) \tag{39}$$

for some  $\theta \in (0, 1]$ . The parameter  $\theta$  is called the *extremal index* and can be viewed as a sample size adjustment for the maxima of the dependent sequence due to clustering of the extremes. The case  $\theta = 1$  corresponds to no clustering, in which case the limiting behavior of  $M_n$  and  $\hat{M}_n$  are identical. In case  $\theta < 1$ ,  $M_n$  behaves asymptotically like the maximum of  $n\theta$  independent observations. The reciprocal of the extremal index  $1/\theta$  of a stationary sequence  $(X_t)$  also has the interpretation as the expected size of clusters of high-level exceedances in the sequence.

There are various sufficient conditions for ensuring that  $\theta = 1$ . Perhaps the most common anticlustering condition is  $D'$  [28], which has the following form:

$$\limsup_{n \to \infty} n \sum_{t=2}^{[n/k]} P(X_1 > a_n x, X_t > a_n x) = O(1/k)$$
(40)

as  $k \to \infty$ . Hence, if the stationary process  $(X_t)$ satisfies a mixing condition and  $D'$ , then

$$P(a_n^{-1}M_n \le x) \to G(x) \tag{41}$$

Returning to the GARCH setting, we assume that the conditions of Theorem 1 are satisfied. Then we know that  $P(|X| > x) \sim c_1 x^{-\alpha}$  for some  $\alpha, c_1 > 0$ , and we can even specify the value of  $\alpha$  in the  $GARCH(1, 1)$  case by solving equation (27). Now choosing  $a_n = n^{1/\alpha} c_1^{1/\alpha}$ , we have  $nP(|X_1| > a_n) \rightarrow$ 1 and defining  $M_n = \max\{|X_1|, \ldots, |X_n|\}$ , we obtain

$$P(a_n^{-1}M_n \le x) \to \exp\{-\theta_1 x^{-\alpha}\}\tag{42}$$

where the extremal index  $\theta_1$  is strictly less than 1. Explicit formulae for the extremal index of a general GARCH process are hard to come by. In some special cases, such as the ARCH $(1)$  and the GARCH $(1,1)$ , there are more explicit expressions. For example, in the GARCH(1,1) case, the extremal index  $\theta_1$  for the maxima of the absolute values of the GARCH process is given by Mikosch and Stărică [34]

$$\theta_{1} = \frac{\lim_{k \to \infty} E\left( |Z_{1}|^{\alpha} - \max_{j=2,\dots,k+1} \left| Z_{j}^{2} \prod_{i=2}^{j} A_{i} \right|^{\alpha/2} \right)_{+}}{E|Z_{1}|^{\alpha}}\n$$
(43)

The above expression can be evaluated by Monte-Carlo simulation, see, for example, [25] for the ARCH(1) case with standard normal noise  $Z_t$ ; see [18], Section 8.1, where one can also find some advice as to how the extremal index of a stationary sequence can be estimated from data.

The situation is markedly different for SV processes. For the SV process with either light- or heavy-tailed noise, one can show that  $D'$  is satisfied and hence the extremal index is always 1 (see  $[3]$ for the light-tailed case and [10] for the heavy-tailed case). Hence, although both GARCH and SV models exhibit stochastic clustering, only the GARCH process displays extremal clustering.

### Convergence of Point Processes

The theory of point processes plays a central role in extreme value theory and in combination with regular variation can be a powerful tool for establishing limiting behavior of other statistics beyond extreme order statistics. As in the previous section, suppose that  $(\hat{X}_t)$  is an i.i.d. sequence of nonnegative random variables with common distribution  $F$  that has regularly varying tails with index  $-\alpha$ . Choosing the sequence  $a_n$  satisfying  $n(1 - F(a_n)) \rightarrow 1$ , we have

$$nP(\hat{X}_1 > a_n x) \to x^{-\alpha} \tag{44}$$

as  $n \to \infty$ . Now equation (44) can be strengthened to the statement

$$n P(a_n^{-1}\hat{X}_1 \in B) \to \nu(B) \tag{45}$$

for all suitably chosen Borel sets  $B$ , where the measure  $\nu$  is defined by its value on intervals of the form  $(a, b]$  with  $a > 0$  as

$$\nu(a,b] = a^{-\alpha} - b^{-\alpha} \tag{46}$$

The convergence in equation  $(46)$  can be connected with the convergence in the distribution of a sequence of point processes. For a bounded Borel set B in  $E =$  $[0,\infty] \setminus \{0\}$ , define the sequence of point processes  $(\hat{N}_n)$  by

$$\hat{N}_n(B) = \#\left\{ a_n^{-1} \hat{X}_j \in B \ , \ j = 1, 2, \dots, n \right\} \tag{47}$$

If B is the interval  $(a, b]$  with  $0 < a < b \leq \infty$ , then since the  $\hat{X}_i$  are i.i.d.,  $\hat{N}_n(B)$  has a binomial distribution with number of trials  $n$  and probability of success

$$p_n = P(a_n^{-1}\hat{X}_1 \in (a, b]) \tag{48}$$

It then follows from equation (46) that  $\hat{N}_n(B)$  converges in distribution to a Poisson random variable  $N(B)$  with mean  $\nu(B)$ . In fact, we have the stronger point process convergence:

$$\hat{N}_n \stackrel{d}{\to} N \tag{49}$$

where  $N$  is a Poisson process on  $E$  with mean measure  $v(dx)$  and  $\stackrel{d}{\rightarrow}$  denotes convergence in distribution of point processes. For our purposes,  $\stackrel{d}{\rightarrow}$  for point processes means that for any collection of *bounded*<sup>b</sup> Borel sets  $B_1, \ldots, B_k$  for which  $P(N(\partial B_i) > 0) =$  $0, j = 1, ..., k$ , we have

$$(\hat{N}_n(B_1), \dots, \hat{N}_n(B_k)) \xrightarrow{d} (N(B_1), \dots, N(B_k))$$
(50)

on  $\mathbb{R}^k$  [18, 29, 36].

As an application of equation (49), define  $\hat{M}_{n,k}$  to be the *k*th largest among  $\hat{X}_1, \ldots, \hat{X}_n$ . For  $y \leq x$ , the event  $\{a_n^{-1}\hat{M}_n \le x, a_n^{-1}\hat{M}_{n,k} \le y\} = \{\hat{N}_n(x,\infty) = 0,$  $\hat{N}_n(y, x] < k-1$  and hence

$$P(a_n^{-1}\hat{M}_n \le x, a_n^{-1}\hat{M}_{n,k} \le y)$$
  
=  $P(\hat{N}_n(x,\infty) = 0, \hat{N}_n(y,x] \le k-1)$   
 $\rightarrow P(N(x,\infty) = 0, N(y,x] \le k-1)$   
=  $e^{-x^{-\alpha}} \sum_{j=0}^{k-1} (y^{-\alpha} - x^{-\alpha})^j / j!$  (51)

As a second application of the limiting Poisson convergence in equation (49), the limiting Poisson process  $\hat{N}$  has points located at  $\Gamma_k^{-1/\alpha}$ , where  $\Gamma_k =$  $E_1 + \cdots + E_k$  is the sum of k i.i.d. unit exponentially distributed random variables. Then if  $\alpha < 1$ , the result is more complicated; if  $\alpha > 1$ , we obtain the convergence of partial sums:

$$a_n^{-1} \sum_{t=1}^n \hat{X}_t \stackrel{d}{\to} \sum_{j=0}^\infty \Gamma_j^{-1/\alpha} \tag{52}$$

In other words, the sum of the points of the point process  $N_n$  converges in distribution to the sum of points in the limiting Poisson process.

For a stationary time series  $(X_t)$  with heavy tails that satisfy a suitable mixing condition, such as strong mixing, and the anticlustering condition  $D'$ , then the convergence in equation (49) remains valid, as well as the limit in equation (52), at least for positive random variables. For example, this is the case for SV processes. If the condition  $D'$  is replaced by the assumption that all finite-dimensional random variables are regularly varying, then there is a point convergence result for  $N_n$  corresponding to  $(X_t)$ . However, the limit point process in this case is more difficult to describe. Essentially, the point process has anchors located at the Poisson points  $\Gamma_i^{-1/\alpha}$ . At each of these anchor locations, there is an independent cluster of points that can be described by the distribution of the angular measures in the regular variation condition [8, 9]. These conditions can then be applied to functions of the data, such as lagged products, to establish the convergence in distribution of the sample autocovariance function. This is the subject of the following section.

# The Behavior of the Sample Autocovariance and Autocorrelation Functions

The ACF is one of the principal tools used in classical time series modeling. For a stationary Gaussian process, the dependence structure of the process is completely determined by the ACF. The ACF also conveys important dependence information for linear process. To some extent, the dependence governed by a linear filter can be fully recovered from the ACF. For the time series consisting of financial returns, the data are uncorrelated, so the value of the ACF is substantially diminished. Nevertheless, the ACF of other functions of the process such as the squares and absolute values can still convey useful information about the nature of the nonlinearity in the time series. For example, slow decay of the ACF of the squares is consistent with the volatility clustering present in the data. For a stationary time series  $(X_t)$ , the ACVF and ACF are defined as

$$\gamma_X(h) = \text{cov}(X_0, X_h) \quad \text{and}$$
$$\rho_X(h) = \text{corr}(X_0, X_h) = \frac{\gamma_X(h)}{\gamma_X(0)}, \quad h \ge 0 \tag{53}$$

respectively. Now for observations  $X_1, \ldots, X_n$  from the stationary time series, the ACVF and ACF are estimated by their sample counterparts, namely, by

$$\hat{\gamma}_X(h) = \frac{1}{n} \sum_{t=1}^{n-h} (X_t - \overline{X}_n) \left( X_{t+h} - \overline{X}_n \right) \quad (54)$$

and

$$\hat{\rho}_X(h) = \frac{\hat{\gamma}_X(h)}{\hat{\gamma}_X(0)} = \frac{\sum_{t=1}^{n-h} (X_t - \overline{X}_n)(X_{t+h} - \overline{X}_n)}{\sum_{t=1}^{n} (X_t - \overline{X}_n)^2} \tag{55}$$

where  $\overline{X}_n = n^{-1} \sum_{t=1}^n X_t$  is the sample mean.

Even though the sample ACVF is an average of random variables, its asymptotic behavior is determined by the extremes values, at least in the case of heavy-tailed data. Regular variation and point process theory are the two ingredients that play a key role in deriving limit theory for the sample ACVF and ACF. In particular, one applies the point process techniques alluded to in the previous section to the

stationary process consisting of products  $(X_t X_{t+h})$ . The first such results were established by Davis and Resnick  $[14-16]$  in a linear process setting. Extensions by Davis and Hsing [8] and Davis and Mikosch [9] allowed one to consider more general time series models beyond those linear. The main idea is to consider a point process  $N_n$  based on products of the form  $X_t X_{t+h}/a_n^2$ . After establishing convergence of this point process, in many cases one can apply the continuous mapping theorem to show that the sum of the points that comprise  $N_n$  converges in distribution to the sum of the points that make up the limiting point process. Although the basic idea for establishing these results is rather straightforward, the details are slightly complex. These ideas have been applied to the case of GARCH processes in [1] and to SV processes in [10], which are summarized below.

### The GARCH Case

The scaling in the limiting distribution for the sample ACF depends on the index of regular variation  $\alpha$ specified in Theorem 1. We summarize the results for the various cases of  $\alpha$ .

- 1. If  $\alpha \in (0, 2)$ , then  $\hat{\rho}_X(h)$  and  $\hat{\rho}_{|X|}(h)$  have nondegenerate limit distributions. The same statement holds for  $\hat{\rho}_{X^2}(h)$  when  $\alpha \in (0, 4)$ .
- 2. If  $\alpha \in (2, 4)$ , then both  $\hat{\rho}_X(h)$ ,  $\hat{\rho}_{|X|}(h)$  converge in probability to their deterministic counterparts  $\rho_X(h)$ ,  $\rho_{|X|}(h)$ , respectively, at the rate  $n^{1-2/\alpha}$ and the limit distribution is a complex function of non-Gaussian stable random variables.
- 3. If  $\alpha \in (4, 8)$ , then

$$n^{1-4/(2\alpha)}(\hat{\rho}_{X^2}(h) - \rho_{X^2}(h)) \xrightarrow{d} S_{\alpha/2}(h) \quad (56)$$

where the random variable  $S_{\alpha/2}(h)$  is a function of infinite variance stable random variables.

4. If  $\alpha > 4$ , then the one can apply standard central limit theorems for stationary mixing sequences to establish a limiting normal distribution [17, 26]. In particular,  $(\hat{\rho}_X(h))$  and  $(\hat{\rho}_{|X|}(h))$  have Gaussian limits at  $\sqrt{n}$ -rates. The corresponding result holds for  $(X_t^2)$  when  $\alpha > 8$ .

These results show that the limit theory for the sample ACF of a GARCH process is rather complicated when the tails are heavy. In fact, there is considerable empirical evidence based on extreme

value statistics as described in the second section, indicating that log-return series might not have a finite fourth or fifth moment<sup>c</sup> and then the limit results above would show that the usual confidence bands for the sample ACF based on the central limit theorem and the corresponding  $\sqrt{n}$ -rates are far too optimistic in this case.

## **The Stochastic Volatility Case**

For a more direct comparison with the GARCH process, we choose a distribution for the noise process that matches the power law tail of the GARCH with index  $\alpha$ . Then

$$\left(\frac{n}{\ln n}\right)^{1/\alpha} \hat{\rho}_X(h)$$
 and  $\left(\frac{n}{\ln n}\right)^{1/(2\alpha)} \hat{\rho}_{X^2}(h)$  (57)

converge in distribution for  $\alpha \in (0, 2)$  and  $\alpha \in (0, 4)$ , respectively. This illustrates the excellent large sample behavior of the sample ACF for SV models even if  $\rho_X$  and  $\rho_{X^2}$  are not defined [11, 13]. Thus, even if  $\text{var}(Z_t) = \infty$  or  $EZ_t^4 = \infty$ , the estimates  $\hat{\rho}_X(h)$ and  $\hat{\rho}_{X^2}(h)$ , respectively, converge to zero at a rapid rate. This is in marked contrast with the situation for GARCH processes, where under similar conditions on the marginal distribution, the respective sample ACFs converge in distribution to random variables without any scaling.

## **End Notes**

<sup>a.</sup>Basrak *et al.* [1] proved this result under the condition that  $\alpha/2$  is not an even integer. Boman and Lindskog [5] removed this condition.

<sup>b.</sup>Here bounded means bounded away from zero.

<sup>c.</sup>See, for example, [18], Chapter 6, and [33].

## References

- [1] Basrak, B., Davis, R.A. & Mikosch, T. (2002). Regular variation of GARCH processes. Stochastic Processes and Their Applications 99, 95–116.
- Basrak, B., Davis, R.A. & Mikosch, T. (2002). A [2] characterization of multivariate regular variation, The Annals of Applied Probability 12, 908-920.
- [3] Breidt, F.J. & Davis, R.A. (1998). Extremes of stochastic volatility models, The Annals of Applied Probability 8, 664-675.
- [4] Bougerol, P. & Picard, N. (1992). Stationarity of GARCH processes and of some nonnegative time series, Journal of Econometrics 52, 115-127.
The capital asset pricing model (CAPM) is a major breakthrough in applying theoretical principles from modern portfolio theory in a real market environment. It is still in use, although in the meantime a more sophisticated model, the arbitrage pricing theory (APT), has become available. Even though both models look like close relatives, their underlying assumptions are very different. Indeed, the APT operates under such general conditions that it is able to generate a whole family of market models.

#### 7.1 **Empirical Problems with MPT**

We have seen in the last chapter, how everything falls into place in modern portfolio theory. How can there possibly be problems, severe enough to disqualify it for practical application? The answer has to do with the statistical properties of the quantities required by the MPT. It was implicitly assumed that the expectation vector  $|\mu\rangle$  and the covariance matrix  $\Sigma$  of a random vector of returns  $|R\rangle$  is known. This assumption, as innocent as it looks, is the source of all the problems. In reality these quantities have to be estimated. So let's assume, you have recorded a time series of returns  $|r_1\rangle, \ldots, |r_T\rangle$ . How would you estimate  $|\mu\rangle$  and  $\Sigma$ ? The simplest possibility is to use the maximum-likelihood estimators

$$|\hat{\mu}\rangle = \frac{1}{T} \sum_{t=1}^{T} |r_{t}\rangle \quad \text{and} \quad \hat{\Sigma} = \frac{1}{T} \sum_{t=1}^{T} |r_{t}\rangle\langle r_{t}| - |\hat{\mu}\rangle\langle\hat{\mu}|, \tag{7.1}$$

where  $|\cdot\rangle\langle\cdot|$  is the outer product, defined by

$$|a\rangle\langle a| = \begin{pmatrix} a_1a_1 & a_1a_2 & \dots & a_1a_N \\ a_2a_1 & a_2a_2 & \dots & a_2a_N \\ \vdots & \vdots & \ddots & \vdots \\ a_Na_1 & a_Na_2 & \dots & a_Na_N \end{pmatrix}.$$
 (7.2)

For  $\hat{\Sigma}$  to be positive definite, there have to be at least  $T = N$  linearly independent observations  $|r_{t}\rangle$ . You might think now that does not sound too bad altogether. But remember that MPT was tailored for middle- or long-term horizons, where returns can be safely assumed normally distributed. And now think for example only of those stocks contained within the S&P 500 index. If the return horizon is one year, we need at least 500 years of data, to get an admissible estimate for the covariance matrix  $\Sigma$ .

Another way to see the estimation problem of MPT is to count the number of free parameters to be estimated. There are N estimates for the expected returns  $\mu_n$ , for  $n =$  $1, \ldots, N$ . The covariance matrix has N rows and N columns, but not all entries  $\sigma_{mn}$  are free parameters. Because  $\Sigma$  is symmetric, only the upper  $(n \ge m)$  or lower  $(n \le m)$  triangle is unrestricted. Altogether there are  $\frac{N(N+1)}{2}$  free parameters contained in  $\Sigma$ . The total number of free parameters  $\beta$  to be estimated in the MPT-world with N assets is

$$#\beta = \frac{N(N+3)}{2}.\tag{7.3}$$

**Ouick calculation 7.1** Confirm the total number of free parameters.

In the case of the  $S\&P$  500 index, we are dealing with a total of 125750 free parameters. You see the problem. On the other hand, as we will see, the CAPM characterizes the entire market by only  $N$  beta-factors. Furthermore, the data requirements are dramatically reduced and well inside empirical range.

## The Capital Asset Pricing Model (CAPM)

Let's start our discussion with some properties of the capital market line (CML). The slope of the CML is obviously

$$m = \frac{\mu_{\rm MP} - r}{\sigma_{\rm MP}},\tag{7.4}$$

as illustrated in Figure 7.1 left. Because all efficient portfolios are located on the capital market line, we can write an equation, relating the expected return of an arbitrary efficient portfolio  $P$  to its risk, expressed in terms of its standard deviation,

$$\mu_P = r + m\sigma_P = r + \frac{\mu_{\text{MP}} - r}{\sigma_{\text{MP}}} \sigma_p. \tag{7.5}$$

![](_page_1_Figure_10.jpeg)

Fig. 7.1 Slope of the capital market line (left) and market portfolio mixed with stock (right)

The slope *m* is called the market price of risk, because it indicates with how much extra expected return the agent has to be compensated for taking one additional unit of risk, measured in  $\sigma$ -units.

Now let's build a portfolio  $P$  by taking an arbitrary stock  $S$ , and mixing it with the market portfolio MP. What is the expected return and the standard deviation of this portfolio? A straightforward calculation yields

$$\mu_P = w_S \mu_S + (1 - w_S) \mu_{\text{MP}}$$
  

$$\sigma_P = \sqrt{w_S^2 \sigma_S^2 + 2w_S (1 - w_S) \sigma_{S,\text{MP}} + (1 - w_S)^2 \sigma_{\text{MP}}^2},$$
(7.6)

where the shorthand notation  $\sigma_{S,MP} = \text{Cov}[R_S, R_{MP}]$  was used. For reasons that become clear shortly, we also need the derivative of (7.6) with respect to  $w_S$ ,

$$\frac{\partial \mu_P}{\partial w_S} = \mu_S - \mu_{\text{MP}}\n$$

$$\n\frac{\partial \sigma_P}{\partial w_S} = \frac{w_S \sigma_S^2 + (1 - 2w_S)\sigma_{S,\text{MP}} - (1 - w_S)\sigma_{\text{MP}}^2}{\sigma_P}.\n$$
(7.7)

Now it is crucial to realize that for the weight  $w<sub>S</sub> = 0$  the portfolio P is nothing else than the market portfolio and furthermore, the slope of  $\mu_P$  at  $w_S = 0$  is m,

$$\left. \frac{d\mu_P}{d\sigma_P} \right|_{w_S = 0} = m,\tag{7.8}$$

see also Figure 7.1 right. If the moments of  $R_S$  and  $R_{\text{MP}}$  are fixed, we have  $d\mu_P = \frac{\partial \mu_P}{\partial w_S} dw_S$ and  $d\sigma_P = \frac{\partial \sigma_P}{\partial w_S} dw_S$ . Now, everything falls into place and we have

$$m = \frac{\partial \mu_P / \partial w_S}{\partial \sigma_P / \partial w_S} \bigg|_{w_S = 0},\tag{7.9}$$

or a little bit more detailed using  $(7.7)$ 

$$\frac{\mu_{\rm MP} - r}{\sigma_{\rm MP}} = \frac{\mu_S - \mu_{\rm MP}}{\sigma_{S,\rm MP} - \sigma_{\rm MP}^2} \cdot \sqrt{\sigma_{\rm MP}^2}.$$
(7.10)

**Quick calculation 7.2** Verify the last equation for  $w_S = 0$ .

Rearranging terms in  $(7.10)$ , one obtains

$$\mu_S = (\mu_{\rm MP} - r) \left( \frac{\sigma_{S,\rm MP}}{\sigma_{\rm MP}^2} - 1 \right) + \mu_{\rm MP}. \tag{7.11}$$

Renaming the ratio  $\frac{\sigma_{\text{S,MP}}}{\sigma_{\text{MP}}^2} = \beta_S$  and expanding the associated bracket, yields the CAPM equation

$$\mu_S = r + \beta_S(\mu_{\rm MP} - r) \tag{7.12}$$

![](_page_3_Figure_1.jpeg)

**Fig. 7.2** Mean-beta-diagram with market portfolio and security market line (SML)

of Sharpe (1964), Lintner (1965), and Mossin (1966). Let's first calculate a few special βs to get a feeling for the new model. For example let's investigate the β for the risk-free security

$$\beta_0 = \frac{\sigma_{0,\text{MP}}}{\sigma_{\text{MP}}^2} = \frac{\rho_{0,\text{MP}} \sigma_0 \sigma_{\text{MP}}}{\sigma_{\text{MP}}^2} = 0, \tag{7.13}$$

where we used that σ<sup>0</sup> = 0. Next, let's calculate the β of the market portfolio itself,

$$\beta_{\rm MP} = \frac{\sigma_{\rm MP,MP}}{\sigma_{\rm MP}^2} = \frac{\sigma_{\rm MP}^2}{\sigma_{\rm MP}^2} = 1. \tag{7.14}$$

We have from (7.12) that µ*<sup>S</sup>* as a function of β*<sup>S</sup>* is a line with µ-intercept *r* and slope µMP − *r*. We can thus draw a µ-β-diagram as in Figure 7.2. The straight line, connecting *r* and MP, is called the security market line (SML). It maps the available securities along their respective β-risk, relative to the market portfolio. To understand the last statement completely, we have to investigate the connection between the beta-factors and the so-called market risk.

The capital asset pricing model (7.12) is a statement about the expectation value of the random return of security *S*. We certainly expect it to occur on average over many realized returns of this security, but we do not expect it to be a precise prediction of the next realization. Instead we can explicitly include a random error, to obtain the more realistic model

$$R_S = R_0 + \beta_S (R_{\rm MP} - R_0) + \epsilon_S, \tag{7.15}$$

with *E* [ ϵ*S* ] = 0 and Var[ ϵ*S* ] =σ 2 ϵ .

**Quick calculation 7.3** Check that the expectation of (7.15) is the CAPM-equation.

It is further assumed that the individual random error ϵ*<sup>S</sup>* is not correlated with *R*MP. We can now calculate the variance of *RS*,

$$\text{Var}[R_S] = \beta_S^2 \sigma_{\text{MP}}^2 + \sigma_{\epsilon}^2. \tag{7.16}$$

Obviously, there are two sources of risk, contributing to the overall variability of  $R_{S_1}$ the market or systematic risk, represented by  $\beta_{\rm S}^2 \sigma_{\rm MP}^2$ , and a specific or idiosyncratic risk  $\sigma_{\epsilon}^2$ , exclusively related to the security S. Note that only the systematic risk is compensated in terms of extra expected return in the CAPM  $(7.12)$ . Idiosyncratic risk is not accounted for.

To see the implication for a portfolio, we have to understand first how the beta of a portfolio is calculated. Recall that the return of the portfolio  $P$  is

$$R_P = \sum_{n=1}^{N} w_n R_n,\tag{7.17}$$

where  $R_n$  is the random return of security  $S_n$ , and all weights add up to one. The betafactor is universally defined as the covariance of the respective random return with the return of the market portfolio, divided by the variance of the market portfolio. Using that the covariance is linear in both of its arguments, one obtains

$$\beta_P = \frac{\text{Cov}[R_P, R_{\text{MP}}]}{\text{Var}[R_{\text{MP}}]} = \sum_{n=1}^N w_n \frac{\text{Cov}[R_n, R_{\text{MP}}]}{\text{Var}[R_{\text{MP}}]} = \sum_{n=1}^N w_n \beta_n. \tag{7.18}$$

That is, the beta of a portfolio is the weighted sum of all security-betas in the portfolio.

**Quick calculation 7.4** Verify that covariances are linear in each argument.

This is a very convenient result and it enables us to finally conclude the discussion of diversification.

We earlier conducted a calculation that suggested that the risk in large portfolios in the limit may be diversified away completely. At that point we had no access to the concepts of systematic and idiosyncratic risk. Now let's finally finish the discussion in the same framework. We earlier assumed that there are  $N$  securities with identical expectation value and variance. This translates into every security having the same beta-factor  $\beta$  and identical idiosyncratic variance  $\sigma_{\epsilon}^2$ . As before, choosing equal weights  $w_n = \frac{1}{N}$ , the expected return of the portfolio is given by the CAPM-equation

$$E[R_P] = r + \sum_{n=1}^{N} \frac{1}{N} \beta \cdot (\mu_{\text{MP}} - r) = r + \beta (\mu_{\text{MP}} - r). \tag{7.19}$$

There is no surprise, that the portfolio has the same expected return as each particular security. But now let's calculate the variance of the portfolio

$$\operatorname{Var}[R_P] = \beta^2 \sigma_{\text{MP}}^2 + \frac{1}{N^2} \sum_{n=1}^N \sigma_{\epsilon}^2 = \beta^2 \sigma_{\text{MP}}^2 + \frac{\sigma_{\epsilon}^2}{N}.$$
 (7.20)

In the limit  $N \rightarrow \infty$  the idiosyncratic risk is diversified away, whereas the systematic risk is non-diversifiable. This is the reason why systematic risk is compensated by expected return but idiosyncratic risk is not. In a manner of speaking, the market expects every

agent to only participate in terms of already optimally diversified portfolios. Agents holding single securities or small portfolios are not fully compensated for the risk they take. That is why everyone you hear of making a fortune by trading a small collection of risky securities was probably a good deal more lucky than other market participants. Of course you rarely hear of the poor dogs losing every dollar with a similar strategy.

# **Estimating Betas from Market Data**

One of the greatest victories of the CAPM is the dramatically reduced hunger for empirical data. We have seen that modern portfolio theory requires a huge amount of data to estimate the covariance matrix of all traded securities. In other words, MPT tries to establish mutual relations between all asset returns. The CAPM does so only between the securities and the market portfolio. The trick is to identify an index like the  $\&P$  500 or the DAX as proxy for the respective market portfolio. In this setup, linear regression is the vehicle to generate estimates for the beta-factors. Linear regression is the working horse of statistics and econometrics. It is based on the linear model

$$Y = \alpha + \beta X + \epsilon,\tag{7.21}$$

where Y is called the response variable, X is the regressor, and  $\epsilon$  is a random error with known distribution, usually assumed *Gaussian*. The parameters  $\alpha$  and  $\beta$  are the ones to be estimated from the data. Regression analysis requires some technical conditions like stationarity and homogeneity of errors, which are usually satisfied in the context of long-term returns. So we do not bother with any of these at this point. Instead we ask the question: How is regression analysis used to produce estimates for  $\alpha$  and  $\beta$ ?

Assume, you have an observation series of the response variable  $v_t$ , and also of the regression variable  $x_t$  for  $t = 1, \ldots, T$ . Indexing by t suggests that we have time series data, but regression analysis also applies to cross-sectional data. We can organize these observations in vector/matrix form

$$|y\rangle = X|\beta\rangle + |\epsilon\rangle,\tag{7.22}$$

where

$$|y\rangle = \begin{pmatrix} y_1 \\ \vdots \\ y_T \end{pmatrix}, \quad X = \begin{pmatrix} 1 & x_1 \\ \vdots & \vdots \\ 1 & x_T \end{pmatrix}, \quad |\beta\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad |\epsilon\rangle = \begin{pmatrix} \epsilon_1 \\ \vdots \\ \epsilon_T \end{pmatrix}. \tag{7.23}$$

**Quick calculation 7.5** Verify that  $(7.22)$  and  $(7.23)$  reproduce the linear model  $(7.21)$ for every  $t = 1, \ldots, T$ .

The notation is a bit ambiguous here, because in  $(7.22)$  X represents a data matrix, whereas in  $(7.21)$  X is a random regression variable, but it is difficult to argue with tradition. We certainly do not expect the real data to obey an exact linear relationship,

which would mean ϵ*<sup>t</sup>* = 0 for all *t* = 1, . . . ,*T*. Instead we are interested in the best possible linear fit in the least-squares sense. That is, we have to minimize the total square error

$$\sum_{t=1}^{T} \epsilon_t^2 = \langle \epsilon | \epsilon \rangle = (\langle y | - \langle \beta | X' \rangle (|y \rangle - X | \beta \rangle). \tag{7.24}$$

There are two important things to note here: The total square error constitutes a functional *F* = ⟨ϵ|ϵ⟩ to be minimized with respect to ⟨β|, and the optimization problem is a convex one. Thus, the necessary and sufficient condition for a minimum is

$$\frac{\delta F}{\delta \langle \beta |} = -2X'(|y\rangle - X|\beta\rangle) \stackrel{!}{=} |0\rangle. \tag{7.25}$$

The −*X* ′ term is due to the chain rule of differentiation.

**Quick calculation 7.6** Confirm the functional derivative.

Rearranging (7.25) yields

$$X'X|\hat{\beta}\rangle = X'|y\rangle,\tag{7.26}$$

where we have adopted the common hat-notation for an estimator in statistics. Assuming that *X* ′*X* is invertible, we can multiply both sides with (*X* ′*X*) −1 from the left to obtain the desired least-squares estimator

$$|\hat{\beta}\rangle = (X'X)^{-1}X'|y\rangle. \tag{7.27}$$

Inverting *X* ′*X* is usually not a problem. The necessary condition is that *X* contains at least as many linearly independent observations as there are parameters to be estimated. In most situations there are many more observations than parameters. Under fairly mild conditions, the least-squares estimator is the best linear unbiased estimator available, and it is easy to compute. We can now state an estimated version of the linear model (7.21)

$$\hat{Y} = \hat{\alpha} + \hat{\beta}X + \epsilon,\tag{7.28}$$

where *Y*ˆ is the best possible model for *Y* we can find.

To apply least-squares estimation in the context of the CAPM, in order to estimate the beta-factor of a particular security *S*, set

$$y_t = r_{S,t} - r$$
 and  $x_t = r_{\text{MP},t} - r$ , (7.29)

where the realized values of the respective returns are again indicated by small letters. If the CAPM is right, the estimator αˆ should be minute. In portfolio management, this estimator is called Jensen's alpha. We will discuss it in more detail in the next chapter.

![](_page_7_Figure_1.jpeg)

**Fig. 7.3** Regression of monthly excess returns of S&P 500 (*x*MP) on Microsoft (*yS*) from 1993 to 2013

Instead, let's state the resulting linear relationship between the excess returns of security *S* and the market portfolio explicitly,

$$\hat{r}_S - r = \hat{\alpha}_S + \hat{\beta}_S(r_{\rm MP} - r). \tag{7.30}$$

Let's look at a neat example.

**Example 7.1**

The regression relationship (7.30) was estimated for monthly return data of the Microsoft stock between 1993 and 2013. The S&P 500 index was used as proxy for the market portfolio, and the risk-free rate of return over one month was assumed *r* = 0.25%, which means a 3% annual interest rate.

Results

The resulting estimates for the parameters α*<sup>S</sup>* and β*<sup>S</sup>* are

$$\hat{\alpha}_S = 8.37 \cdot 10^{-3}$$
 and  $\hat{\beta}_S = 1.31$ .

The data points (*x<sup>t</sup>* , *yt*) and the resulting regression line are shown in Figure 7.3. As expected, the estimate for α*<sup>S</sup>* is small, even though monthly periods are probably not long enough to remove all short-term artifacts in the return series. The estimate of β*<sup>S</sup>* indicates that the systematic risk, inherent in the Microsoft stock, is higher than the risk of the market portfolio.

........................................................................................................................

Now that we have a regression relation at hand, we have immediate access to all consequences of the CAPM. But how do we use it to make predictions about returns of specific securities or portfolios? Assume we have used the information F*<sup>T</sup>* to estimate the beta-factor of security *S*. We can take our advanced stochastic model (7.15) on

page 123, replace  $\beta_S$  by the estimate  $\hat{\beta}_S$ , and take conditional expectations on both sides to obtain the prediction formula

$$E[R_{S,T+1}|\mathcal{F}_T] = r + \hat{\beta}_S(\mu_{\text{MP}} - r). \tag{7.31}$$

This equation needs some explanation. First of all, the expectation value of the random error vanishes conditionally and unconditionally,  $E[\epsilon_{T+1}] = 0$ . We have further implicitly assumed that we can learn nothing about the expected market portfolio return  $R_{\text{MP},T+1}$  from the information  $\mathcal{F}_T$ , and thus  $E[R_{\text{MP},T+1}|\mathcal{F}_T] = E[R_{\text{MP},T+1}] = \mu_{\text{MP}}$ . This is always true, if returns are indeed independent and identically distributed, as we usually assume. Of course we do not know  $\mu_{\text{MP}}$  either, so we have to estimate it from the available return data or use some economically motivated guess. The estimate  $\hat{\beta}_S$  is known at time  $T$ , and is hence treated like a constant.

Equation  $(7.31)$  looks different from the original CAPM equation  $(7.12)$  on page 122. To show the connection between them we have to use the law of iterated expectations

$$E[E[R_{S,T+1}|\mathcal{F}_T]]=E[R_{S,T+1}]=\mu_S,\t(7.32)$$

and the fact that the estimate  $\hat{\beta}_S$  is unbiased, which means  $E[\hat{\beta}_S] = \beta_S$ . The unconditional expectation is with respect to the information  $\mathcal{F}_0$ . Thus, the law of iterated expectations says that at time  $t = 0$ , the expected future prediction you may make at any later time  $t = T$ , has to equal the prediction you can make today, at time  $t = 0$ . This is because from today's point of view, you have to predict the available information at time T as well, and so you expect the predicted prediction to be consistent with your current prediction. Taking unconditional expectations on both sides of  $(7.31)$  yields

$$\mu_S = r + \beta_S(\mu_{\rm MP} - r). \tag{7.33}$$

We can thus conclude that in some way the CAPM is the expectation of  $(7.31)$ . This insight has a powerful dark side. We have to accept that the conditional expectation  $E[R_{ST+1}|\mathcal{F}_T]$ , as well as the estimator  $\hat{\beta}_S$  are random variables, with their own distributions. We have already implicitly made this assumption in claiming that  $\hat{\beta}_S$  is an unbiased estimator.

#### **Quick calculation 7.7** Can you see why?

To understand these subtleties thoroughly, we have to consider by no means trivial statistical issues. But for assessing the consequences of the CAPM, if it comes in touch with real data, this is both necessary and rewarding.

## 7.4

# **Statistical Issues of Regression Analysis and Inference**

In order to assess the quality of a prediction based on observation data, it is worthwhile to take a closer look at some statistical properties of estimators and regression analysis. Many inferential conclusions are extremely subtle and it is easy to lose track of the substantial concepts. To avoid confusion this section provides information about relevant topics in structured blocks. We start with some diagnostic tools, then move on to the properties of the relevant estimators, and finally discuss the consequences of estimated beta-factors in the CAPM.

#### 7.4.1 **Coefficient of Determination**

It seems like a good starting point to ask how accurate the linear fit, provided by regression analysis, actually is. If the regressor provides no information about the response variable, then the whole CAPM is nothing more than an interesting theoretical exercise. The influence of the regressor is usually assessed by the coefficient of determination  $R^2$ . It indicates the proportion of variability of the response variable that is explained by the linear regression. That was the easy part. Understanding how it is constructed is the difficult one. Again assume that we have a vector of observations of both the response variable and the regressor. The arithmetic mean of the response variable is

$$\bar{y} = \frac{1}{T} \sum_{t=1}^{T} y_t = \frac{1}{T} \langle 1 | y \rangle. \tag{7.34}$$

To turn  $|v\rangle$  into a vector of deviations from its mean, we can write

$$|y\rangle - \bar{y}|1\rangle = |y\rangle - \frac{1}{T}|1\rangle\langle 1|y\rangle = M_0|y\rangle, \tag{7.35}$$

where the centering matrix  $M_0$ , defined by

$$M_0 = I - \frac{1}{T} |1\rangle\langle 1|,\tag{7.36}$$

turns the observations into deviations from the mean. The matrix  $M_0$  has two useful, and more or less obvious properties. It is symmetric,  $M_0 = M'_0$ , and it is idempotent, which means that  $M_0^2 = M_0$  (see for example Greene, 2003, sect. A.2.8). We will use it shortly to construct sums of squares.

If the regression parameters are estimated via least-squares, we can write the following decomposition

$$|y\rangle = |\hat{y}\rangle + |e\rangle,\tag{7.37}$$

#### 129

with  $|\hat{v}\rangle = X|\hat{\beta}\rangle$  and the vector of residuals  $|e\rangle = |v\rangle - |\hat{v}\rangle$ . The residuals are estimates for the realizations of the random error. Note one important fact: By the first order condition of the least-squares estimator  $(7.25)$ , we have

$$X'(|y\rangle - X|\hat{\beta}\rangle) = X'|e\rangle = |0\rangle. \tag{7.38}$$

But the first row of X' entirely consists of ones and thus, we have  $\langle 1|e \rangle = 0$ , the residuals sum to zero, and  $M_0|e\rangle = |e\rangle$ . Now multiply (7.37) with the centering matrix to obtain deviations from the mean

$$M_0|y\rangle = M_0 X|\hat{\beta}\rangle + |e\rangle. \tag{7.39}$$

To obtain the sums of squares, simply square both sides, and use that  $M_0$  is symmetric and idempotent, which means  $M'_0M_0 = M_0$ ,

$$\langle y|M_0|y\rangle = \langle \hat{\beta}|X'M_0X|\hat{\beta}\rangle + \langle e|e\rangle. \tag{7.40}$$

The cross-terms on the right hand side vanish, because  $\langle \hat{\beta} | X' M_0 | e \rangle = 0$ .

**Ouick calculation 7.8** Verify the last statement.

The relationship  $(7.40)$  is often written in a somewhat less formal way as

$$SST = SSE + SSR, \tag{7.41}$$

where SST stands for "sum of squares total," SSE for "sum of squares explained," and SSR for "sum of squares residual." The coefficient of determination is defined as the ratio of the sum of squares explained and the sum of squares total,

$$R^{2} = \frac{\text{SSE}}{\text{SST}} = 1 - \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\langle e|e\rangle}{\langle y|M_{0}|y\rangle}.$$
(7.42)

In Example 7.1 we conducted a linear regression of the  $S\&P$  500 returns on the Microsoft stock returns. Calculating the coefficient of determination in this example yields  $R^2 = 35\%$ . This means that 35% of the variability of the returns of Microsoft is explained by the changes in the returns of the index. On the other hand,  $65\%$  of the total variability is due to idiosyncratic random fluctuations. We now begin to see, why it is not easy to test the predictions of the CAPM empirically.

#### 7.4.2 Confidence Intervals

As mentioned before, parameter estimates are themselves random variables, because they are functions of a particular realization of other random variables. We will only consider unbiased estimators that generate at least asymptotically normally distributed estimates. We can then ask the question: What is the probability that the true parameter  $\beta$ , which we do not know, is covered by the symmetric interval  $\hat{\beta} \pm z_k \sigma_{\beta}$ , for arbitrary  $z_k$ ? This is an easy question, because for a normally distributed random variable, we have

$$P\left(-z_{1-\frac{\gamma}{2}} \leq \frac{\hat{\beta} - \beta}{\sigma_{\beta}} \leq z_{1-\frac{\gamma}{2}}\right) = 1 - \gamma,\tag{7.43}$$

where  $z_k = \Phi^{-1}(k)$  is the quantile function of the standard normal distribution. Now we can conclude that the random interval  $\hat{\beta} \pm z_{1-\hat{z}} \sigma_{\beta}$  covers the true unknown parameter with probability  $1 - \gamma$ . This probability is also called confidence level and is most frequently chosen to be  $1 - \gamma = 95\%$ . The corresponding standard normal quantile is  $z_{0.975} = 1.96$ , and the critical values of the resulting confidence interval  $[c_l, c_u]$  are  $c_{u/l} = \hat{\beta} \pm 1.96 \sigma_{\beta}$ .

Now let's look at the least-squares estimator  $|\hat{\beta}\rangle$ . First let's check that it is unbiased and normally distributed. From the definition of  $|\hat{\beta}\rangle$ , we have

$$\begin{aligned} \hat{\beta} \rangle &= (X'X)^{-1}X'|y\rangle = (X'X)^{-1}X'(X|\beta\rangle + |\epsilon\rangle) \\ &= |\beta\rangle + (X'X)^{-1}X'|\epsilon\rangle. \end{aligned} \tag{7.44}$$

Define the  $\sigma$ -algebra  $\mathcal{R}_T$ , generated by the historical observations of the regression variable  $x_t$  for  $t = 1, \ldots, T$ . Then it is easy to see that conditional on  $\mathcal{R}_T$ , the estimator  $|\hat{\beta}\rangle$ is an affine transformation of  $|\epsilon\rangle$ . If the random vector of errors is normally distributed, then  $|\hat{\beta}\rangle$  is normal, too.<sup>1</sup> Furthermore, because  $|\epsilon\rangle$  is assumed uncorrelated with the data, we can even take unconditional expectations to obtain

$$E[|\hat{\beta}\rangle] = |\beta\rangle. \tag{7.45}$$

Because the variance of  $|\hat{\beta}\rangle$  depends on the history of the regression variable, we have to condition on  $\mathcal{R}_T$  to obtain

$$\operatorname{Var}[\hat{\beta}\rangle|\mathcal{R}_{T}] = (X'X)^{-1}X'\operatorname{Var}[\epsilon]X(X'X)^{-1}.$$
(7.46)

But we have assumed the random errors uncorrelated with everything else, especially with themselves, and so  $\text{Var}[\epsilon] = \sigma^2 I$ . Plugging this into (7.46), one obtains

$$\text{Var}[\hat{\beta}|\mathcal{R}_T] = \sigma_\epsilon^2 (X'X)^{-1}.$$
 (7.47)

The only problem with (7.47) is that we do not know  $\sigma_{\epsilon}^2$ . We have to estimate it from the data, too. An unbiased estimator is

$$\hat{\sigma}_{\epsilon}^{2} = \frac{1}{T - 2} \sum_{t=1}^{T} e_{t}^{2} = \frac{1}{T - 2} \langle e | e \rangle. \tag{7.48}$$

To understand the factor  $\frac{1}{T-2}$ , realize that there would be no residual, if we had only two observations. Because there are two parameters, the least-squares fit would be exact in this case. Only if we have three or more linearly independent observations, is the fit not exact. Therefore, there are really only  $T-2$  free equations. The number 2 is called the degrees of freedom. The same thing happens if we estimate a sample variance. Because we have to estimate the mean first, we lose one equation and the correction factor is  $\frac{1}{T-1}$ .

<sup>&</sup>lt;sup>1</sup> Even if  $|\epsilon\rangle$  is not normally distributed,  $|\hat{\beta}\rangle$  is still asymptotically normal under fairly mild conditions, see Greene (2003, chap. 5).

In a general multiple regression framework with  $Q$  parameters, like in the arbitrage pricing theory (APT), the correction factor will be  $\frac{1}{T-Q}$ .

The conditional covariance matrix of the least-squares estimate in Example 7.1 is

$$\text{Var}[|\hat{\beta}_S\rangle|\mathcal{R}_T] = 10^{-3} \cdot \begin{pmatrix} 0.026 & -0.046 \\ -0.046 & 13.453 \end{pmatrix}.$$
 (7.49)

From this, we can construct confidence intervals for the particular estimates  $\hat{\alpha}_S$  and  $\hat{\beta}_S$ by using the diagonal entries in (7.49). But because we have used an estimate of  $\sigma_{e}^{2}$ , the distribution of  $|\hat{\beta}_S\rangle$ , conditional on the regression data, is no longer *Gaussian*. Luckily, it is still asymptotically normal, so that we can use the standard normal quantile  $z_{1-\frac{\gamma}{2}}$ , if T is large enough.<sup>2</sup> We have used 20 years of monthly data in Example 7.1, so there should be no problem. On a confidence level of  $1 - \gamma = 95\%$ , one obtains

$$\hat{\alpha}_S: c_{u/l} = 8.37 \cdot 10^{-3} \pm 9.99 \cdot 10^{-3} \quad \text{and} \quad \hat{\beta}_S: c_{u/l} = 1.31 \pm 0.23.$$
 (7.50)

At a 95% confidence level, the interval around  $\hat{\alpha}_S$  covers the parameter value  $\alpha_S = 0$ , as predicted by the CAPM. That is a reassuring result. At the same confidence level, we can conclude that the Microsoft stock is indeed riskier than the market portfolio, because  $\beta_S = 1$  is outside the confidence interval. The second statement is a lot stronger than the first one, because the statistical error is only  $\gamma = 5\%$ . In the first case, we do not know the error, all we can say is that it is less than or equal to  $1 - \gamma = 95\%$ .

#### 7.4.3 Confidence Bands

There are two quantities, for which we can compute confidence bands, in order to assess the situation. The first one is the regression line

$$\hat{y}(x) = \hat{\alpha} + \hat{\beta}x = \begin{pmatrix} 1 & x \end{pmatrix} |\hat{\beta}\rangle, \tag{7.51}$$

which is also the expectation value of  $\hat{Y}$ , conditional on the realization  $X = x$  of the regression variable.

**Quick calculation 7.9** Check that by reviewing (7.28) on page 126.

The second quantity of interest is the conditional random variable  $\hat{Y}(x) = \hat{y}(x) + \epsilon$  itself.

Conditional on the history of the regression variable, the variance of the estimated parameter vector  $|\hat{\beta}\rangle$  according to (7.47) is  $\sigma_{\epsilon}^2(X'X)^{-1}$ . Thus, we can compute the conditional variance of the estimated regression line as a function of  $x$ ,

$$\operatorname{Var}[\hat{y}(x)|\mathcal{R}_T] = \sigma_{\epsilon}^2 \left(1 \ x\right) (X'X)^{-1} \begin{pmatrix} 1 \\ x \end{pmatrix}.$$
 (7.52)

<sup>&</sup>lt;sup>2</sup> The exact distribution is Student's *t*-distribution, with  $T-2$  degrees of freedom. For  $T>30$ , this one virtually coincides with the normal distribution.

![](_page_13_Figure_1.jpeg)

**Fig. 7.4** 95%-confidence bands for regression line and conditional estimate of the response variable in the Microsoft/S&P 500 Example 7.1

If we take the square root of (7.52), we can compute a confidence interval around *y*ˆ(*x*). This is indicated in Figure 7.4 as the narrow gray shaded area between the 95% critical boundary functions, for the data of Example 7.1. Of course, the variance of ϵ had to be estimated again by σˆ 2 ϵ , and thus, the distribution of *y*ˆ*S*(*x*MP) for any given *x*MP is only approximately normal. But in our large sample, we do not have to worry about that. You can see nicely that for *x*MP = 0, the confidence area covers *y<sup>S</sup>* = 0, confirming the CAPM's prediction, as already discussed at the end of the last section on confidence intervals.

Computing the variance of *Y*ˆ (*x*) = *y*ˆ(*x*) + ϵ is now an easy task. Because ϵ is uncorrelated with everything else, there are no covariance terms and thus, one obtains

$$\operatorname{Var}[\hat{Y}(x)|\mathcal{R}_T] = \operatorname{Var}[\hat{y}(x)|\mathcal{R}_T] + \sigma_{\epsilon}^2. \tag{7.53}$$

That is, the variance of the estimate *y*ˆ(*x*) is simply augmented by σ 2 ϵ , to account for the uncertainty introduced by the random error ϵ. Taking the square root of (7.53), a confidence band for *Y*ˆ (*x*), conditional on the regression variable taking the value *X* = *x*, can be computed. The respective band for the data of Example 7.1 is indicated in Figure 7.4 as the area between the two dashed curves. Those curves are the critical boundaries for a confidence level of 95%. This band is considerably broader than the one for the regression line. That is because in Example 7.1, the idiosyncratic error contributed roughly two thirds of the overall variability of the response variable. Therefore, the variance (7.53) is dominated by the σ 2 ϵ term, which of course again had to be replaced by the appropriate estimate.

## **7.4.4 Predictions of the CAPM**

We have already computed the expected return of an arbitrary security *S* in the next period, (7.31) on page 128, conditional on the information available today, F*T*.

![](_page_14_Figure_1.jpeg)

Fig. 7.5 95%-confidence interval for predicted stock return (dashed) and 95%-confidence band for the conditional expected return (shaded area) in the Microsoft/S&P 500 Example 7.1

Now let's assess this prediction. We can easily calculate the conditional variance of  $R_{\leq T+1}$ .

$$\operatorname{Var}[R_{S,T+1}|\mathcal{F}_T] = \hat{\beta}_S^2 \sigma_{\text{MP}}^2 + \sigma_{\epsilon}^2. \tag{7.54}$$

So by taking the square root, we can compute a confidence interval of the CAPMprediction. Of course, the variances  $\sigma_{\text{MP}}^2$  and  $\sigma_{\epsilon}^2$  are not known and have to be estimated. That renders the conditional return estimator again only asymptotically normal. If we compute all this for the monthly Microsoft/S&P 500 data of Example 7.1, we obtain on the 95% confidence level

$$c_{u/l} = 0.7\% \pm 19\%. \tag{7.55}$$

The confidence interval is indicated in Figure 7.5 by the dashed boundaries. That is a tremendously large interval compared to the small expected return. More generally, the problem is said to be subject to a very low signal to noise ratio. In this situation it is a difficult task to make useful statements about the small quantity that is subject to such large noisy fluctuations. This is one source of the problems encountered in trying to verify the CAPM empirically. As it stands today, more than 50 years later, there are still no conclusive statistical results to support acceptance or rejection of the model.

The strength of the CAPM, however, lies in its conditional nature. If we assume for the moment that we can prematurely observe or, more realistically, reliably predict  $R_{\text{MP},T+1}$ , then we can compute the distribution of  $R_{S,T+1}$  with respect to the larger information  $\mathcal{F}_X$ , generated by additionally conditioning on the market portfolio return. In this case the conditional moments are

$$E[R_{S,T+1}|\mathcal{F}_X] = r + \hat{\beta}_S(r_{\text{MP},T+1} - r) \quad \text{and} \quad \text{Var}[R_{S,T+1}|\mathcal{F}_X] = \sigma_\epsilon^2. \tag{7.56}$$

This is incredibly useful in stress-testing, when the return *r*MP,*T*+<sup>1</sup> is set to some catastrophic level, in order to see what kind of stock or portfolio return is to be expected in such a scenario.

For Example 7.1, the respective 95%-confidence band is indicated as the shaded area in Figure 7.5. This band has still a width of roughly 30.7%, because the dominant contribution to the overall variability of *RS*,*T*+<sup>1</sup> comes from the idiosyncratic variance σ 2 ϵ . But more importantly, the fact that the regression line is tilted means that we can learn something from observing, or better yet adequately predicting the market portfolio return. Once realizing this fact, we can hope to find better models, explaining a larger proportion of the variance of the response variable, to narrow down the interval in which the next stock return is expected. The framework for constructing such models is introduced in the subsequent section.

## **7.5 The Arbitrage Pricing Theory (APT)**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • The arbitrage pricing theory (APT) of Ross (1976) and Roll and Ross (1980) looks much like a simple extension of the CAPM. It is in fact a kind of multi-factor version

$$\mu_S = r + \sum_{q=1}^{Q} \lambda_{S,q} (\mu_{F_q} - r). \tag{7.57}$$

It is even used in the same way as the CAPM, but it is based on an entirely different set of assumptions. The different theoretical foundation is what makes the APT an extremely powerful instrument. The CAPM can be understood as one possible version of the arbitrage pricing theory, and thus, much of the criticism associated with some restrictive assumptions, is wiped out in one stroke. But, as we shall see, despite its similarity with the CAPM, the APT is a completely different beast.

The natural starting point is the classical linear factor analytic model of statistics

$$R_S - \mu_S = \sum_{q=1}^{Q} \lambda_{S,q} F_q + \epsilon_S, \qquad (7.58)$$

where the factors *F<sup>q</sup>* are independent random variables with zero mean and covariance Cov[*Fp*, *Fq*] = δ*pq*. The error term ϵ*<sup>S</sup>* is again assumed uncorrelated with everything else. The coefficients λ*S*,*<sup>q</sup>* are traditionally called factor loadings, but they play the same role as multiple regression coefficients. The purpose of the linear factor model is to give the variability of *R<sup>S</sup>* more structure, or in other words, to explain a greater proportion of the variability of the random return of security *S*, by considering *Q* latent factors. As it turns out, this model has to be modified to allow for an asymptotically arbitrage free security market. But for the moment we will pretend that (7.58) was true until we can see, which restrictions have to be altered. Assume we have a large security market, with

![](_page_16_Figure_1.jpeg)

**Fig. 7.6 3D** Orthogonal projection of the vector  $|a_0\rangle$  into the  $a_1$ - $a_2$ -plane

 $n = 1, \dots, N$  securities. The factor analytic model of this market can be written most efficiently as

$$|R\rangle = |\mu\rangle + \Lambda |F\rangle + |\epsilon\rangle, \tag{7.59}$$

with

$$|R\rangle = \begin{pmatrix} R_{1} \\ \vdots \\ R_{N} \end{pmatrix}, \quad |\mu\rangle = \begin{pmatrix} \mu_{1} \\ \vdots \\ \mu_{N} \end{pmatrix}, \quad \Lambda = \begin{pmatrix} \lambda_{1,1} & \dots & \lambda_{1,Q} \\ \vdots & \ddots & \vdots \\ \lambda_{N,1} & \dots & \lambda_{N,Q} \end{pmatrix}, \quad |F\rangle = \begin{pmatrix} F_{1} \\ \vdots \\ F_{Q} \end{pmatrix}, \quad |\epsilon\rangle = \begin{pmatrix} \epsilon_{1} \\ \vdots \\ \epsilon_{N} \end{pmatrix}. \tag{7.60}$$

We will leave it that way for now and turn to a special portfolio that we can assemble in such a market, the so-called projection portfolio.

We have already discussed the *Riesz*-representation theorem, which is of great importance in the theory of vector spaces. There is another very important theorem, called the projection theorem. Take a look at Figure 7.6. There is a plane, call it the  $a_1$ - $a_2$ plane, spanned by the vectors  $|a_1\rangle$  and  $|a_2\rangle$ , and another vector  $|a_0\rangle$ , not situated in the  $a_1$ - $a_2$ -plane. But we can always project the vector  $|a_0\rangle$  into that plane. Unfortunately, there are infinitely many perfectly valid projections from which we can choose. We are interested in one particular projection, the so-called orthogonal projection, indicated by the small square in Figure 7.6. Let's call the vector obtained by this particular projection  $|\hat{a}_0\rangle$ . Clearly,  $|\hat{a}_0\rangle$  can be represented as a linear combination of the form

$$|\hat{a}_0\rangle = \beta_1 |a_1\rangle + \beta_2 |a_2\rangle = \sum_{q=1}^2 \beta_q |a_q\rangle, \tag{7.61}$$

because by definition, the projection of  $|a_0\rangle$  lives in the  $a_1$ - $a_2$ -plane. Actually, we can formulate this fact more generally as

$$|\hat{a}_0\rangle = \sum_{q=1}^{Q} \beta_q |a_q\rangle = A|\beta\rangle, \tag{7.62}$$

with

$$A = \begin{bmatrix} |a_1\rangle \dots |a_Q\rangle \end{bmatrix} \quad \text{and} \quad |\beta\rangle = \begin{pmatrix} \beta_1 \\ \vdots \\ \beta_Q \end{pmatrix}. \tag{7.63}$$

As we can already understand geometrically,  $|\hat{a}_0\rangle$  is the orthogonal projection of  $|a_0\rangle$ into the  $a_1$ -...- $a_0$ -hyperplane, if the distance, or equivalently the squared distance, between the tip of  $|a_0\rangle$  and the tip of  $|\hat{a}_0\rangle$  becomes minimal. This distance is called  $\epsilon$  in Figure 7.6. Actually,  $\epsilon$  is the length of the vector  $|\epsilon\rangle = |a_0\rangle - A|\beta\rangle$ . That means, we are facing the problem of choosing a vector  $\beta$ , to minimize the squared length

$$\langle \epsilon | \epsilon \rangle = (\langle a_0 | - \langle \beta | A' \rangle) (|a_0 \rangle - A | \beta \rangle). \tag{7.64}$$

But we already solved this least-squares problem in  $(7.27)$  on page 126, and we found

$$|\hat{\beta}\rangle = (A'A)^{-1}A'|a_0\rangle. \tag{7.65}$$

Thus, we can conclude that the orthogonal projection is obtained by choosing the linear combination

$$|\hat{a}_0\rangle = A|\hat{\beta}\rangle = A(A'A)^{-1}A'|a_0\rangle = B|a_0\rangle, \tag{7.66}$$

where  $B = A(A'A)^{-1}A'$  is called the orthogonal projection matrix, or the projector for short. The projector has some special properties, which are easy to prove. For example, it is symmetric,  $B' = B$ , and it is idempotent,  $B^2 = B$ .

**Quick calculation 7.10** Show that  $B$  is symmetric and idempotent.

Returning to our initial setup of the factor analytic model  $(7.59)$ , the first step is to assemble a projection portfolio  $|\theta\rangle$ , such that  $|\mu\rangle = |\hat{\mu}\rangle + |\theta\rangle$  holds; see Figure 7.7. Using

![](_page_17_Figure_12.jpeg)

**Fig. 7.7 BD** Projection portfolio  $|\theta\rangle$  orthogonal to  $|\lambda_1\rangle, \ldots, |\lambda_O\rangle$  and  $|1\rangle$ 

the projector  $B$ , this portfolio is

$$|\theta\rangle = (I - B)|\mu\rangle,\tag{7.67}$$

where again  $B = A(A'A)^{-1}A'$ , and

$$A = \begin{bmatrix} |1\rangle & |\lambda_1\rangle & \dots & |\lambda_Q\rangle \end{bmatrix} = \begin{bmatrix} |1\rangle & \Lambda \end{bmatrix}.$$
 (7.68)

Observe that the form  $\langle \theta |$  is orthogonal to every vector in A, and of course to  $|\hat{\mu}\rangle$ ; see again Figure 7.7. In particular we have

$$\langle \theta | \mu \rangle = \langle \theta | \theta \rangle + \langle \theta | \hat{\mu} \rangle = \langle \theta | \theta \rangle. \tag{7.69}$$

**Quick calculation 7.11** Prove the second equality in  $(7.69)$  by using that B is idempotent.

Now suppose, we have an arbitrarily scaled version of the projection portfolio,  $\alpha|\theta\rangle$ , with  $\alpha > 0$ . Combining this scaled portfolio with our factor analytic model for the return process,  $R_P = \alpha \langle \theta | R \rangle$ , we obtain

$$R_{P} = \alpha \langle \theta | \mu \rangle + \alpha \langle \theta | \Lambda | F \rangle + \alpha \langle \theta | \epsilon \rangle$$
  
=  $\alpha \langle \theta | \theta \rangle + \alpha \langle \theta | \epsilon \rangle.$  (7.70)

With this equation for the returns of the scaled projection portfolio we are now ready to conduct an asymptotic analysis in the limit of very large markets. Following Shiryaev  $(1999, \text{sect. } 2d)$ , we set the scale factor to

$$\alpha = \langle \theta | \theta \rangle^{-\frac{2}{3}}.\tag{7.71}$$

For large portfolios,  $N \rightarrow \infty$ , we obtain the expected return

$$E[R_P] = \langle \theta | \theta \rangle^{\frac{1}{3}} = \sqrt[3]{\sum_{n=1}^{N} \theta_n^2 \xrightarrow[N \to \infty]{N \to \infty}} \infty.$$
(7.72)

That is good news; as long as we are able to form portfolios that are sufficiently large, there is obviously no limit to the expected return we can hope for. But we surely expect that there is a catch somewhere. So let's check what the variance of our scaled projection portfolio is:

$$\operatorname{Var}[R_{P}] = \alpha^{2} \langle \theta | \Sigma_{\epsilon} | \theta \rangle = \langle \theta | \theta \rangle^{-\frac{4}{3}} \sum_{n=1}^{N} \theta_{n}^{2} \sigma_{\epsilon_{n}}^{2}, \tag{7.73}$$

where  $\Sigma_{\epsilon}$  is the diagonal matrix of variances of the idiosyncratic errors. We do not know the magnitude of the variance of each individual error, but we can bound it from above by taking the largest one

$$\operatorname{Var}[R_{P}] \leq \frac{1}{\sqrt[3]{\sum_{n=1}^{N} \theta_{n}^{2}}} \max_{n} (\sigma_{\epsilon_{n}}^{2}) \xrightarrow{N \to \infty} 0.$$
(7.74)

This is an amazing result, because in the limit  $N \rightarrow \infty$ , we seem to realize an infinite return almost surely. What would this magical portfolio cost? We can assume without

loss of generality that we start with normalized prices for all securities,  $s_n = 1$  for  $n = 1, \dots, N$ . In this case, the price of the projection portfolio is

$$\langle s|\theta\rangle = \langle 1|\theta\rangle = 0,\tag{7.75}$$

because the portfolio  $|\theta\rangle$  is orthogonal to the form (1). The scaling factor does not change anything. To summarize the situation, we have constructed a portfolio that does not cost anything, but in the limit  $N \rightarrow \infty$  generates infinite returns almost surely. Such a constellation is called an asymptotic arbitrage opportunity (Kabanov and Kramkov, 1998). Clearly, we would expect an efficient market not to support such arbitrage opportunities. But where did things go wrong? If we recap our steps, we have to conclude that the only possible way out is to require that

$$\lim_{N \to \infty} \langle \theta | \theta \rangle = \lim_{N \to \infty} \sum_{n=1}^{N} \theta_n^2 < \infty. \tag{7.76}$$

But what are the implications of this requirement? First, recall the definition of the projection portfolio and the orthogonal projection matrix,

$$|\theta\rangle = (I - B)|\mu\rangle = |\mu\rangle - A|\hat{\beta}\rangle,\tag{7.77}$$

where  $|\hat{\beta}\rangle = (A'A)^{-1}A'|\mu\rangle$ . Now let's decompose the linear combination  $A|\hat{\beta}\rangle$ ,

$$|\theta\rangle = |\mu\rangle - \hat{\beta}_0 |1\rangle - \sum_{q=1}^{Q} \hat{\beta}_q |\lambda_q\rangle. \tag{7.78}$$

Finally, let's rewrite condition  $(7.76)$  in another form

$$\lim_{N \to \infty} \sum_{n=1}^{N} \theta_n^2 = \lim_{N \to \infty} \sum_{n=1}^{N} \left( \mu_n - \hat{\beta}_0 - \sum_{q=1}^{Q} \hat{\beta}_q \lambda_{n,q} \right)^2 < \infty. \tag{7.79}$$

For  $(7.79)$  to be true, the square bracket has to be zero for most values of *n*. Put another way, the square bracket is only allowed to be different from zero for a finite number of securities. Because in the limit  $N \rightarrow \infty$ , a finite number of particular securities does not make any difference, the consequence of requirement  $(7.79)$  is

$$\mu_n = \hat{\beta}_0 + \sum_{q=1}^{Q} \hat{\beta}_q \lambda_{n,q}, \qquad (7.80)$$

for almost all  $n \leq N$ . All that remains to do is to identify the  $\hat{\beta}$ -coefficients. Suppose, we are looking at a risk-free security  $B_0$ . In this case the latent factors do not influence the expected return. In other words, the loadings vanish,  $\lambda_{0,q} = 0$  for  $q = 1, \ldots, Q$ , and  $\mu_0 =$  $\hat{\beta}_0$ . This immediately identifies  $\hat{\beta}_0$  with the risk-free interest rate r, and (7.80) becomes

$$\mu_n = r + \sum_{q=1}^{Q} \hat{\beta}_q \lambda_{n,q}.$$
(7.81)

Now let's see what happens, if we look at a particular factor  $F<sub>n</sub>$ . In this case, we have  $\lambda_{F_{p},q} = \delta_{pq}$ , and  $\mu_{F_{p}} = r + \hat{\beta}_{p}$ , because the loading for the *p*-th factor is of course one, and all other loadings vanish. But from this we can conclude that  $\hat{\beta}_q = \mu_{F_q} - r$  for all  $q = 1, \ldots, Q$ . Thus, Equation (7.81) becomes

$$\mu_n = r + \sum_{q=1}^{Q} \lambda_{n,q} (\mu_{F_q} - r). \tag{7.82}$$

This relation has to hold for almost all securities  $n \leq N$ , in particular for the arbitrary security S, in which case we have recovered the APT-equation  $(7.57)$  on page 135.

What does our analysis tell us about the factor analytic model from which we departed initially? We have to modify this model in two respects. The obvious modification is to discard the overall expectation vector  $|\mu\rangle$  and instead to allow for factor specific expectations  $\mu_{F_a} \neq 0$ . This is an immediately evident consequence of the structure of  $(7.82)$ . The second modification is not quite so obvious. Recall that the form  $\langle \theta |$ , associated with the projection portfolio (7.67), is orthogonal to every loading vector  $|\lambda_q\rangle$ , for  $q = 1, \ldots, Q$ . Therefore, all results remain unchanged if we allow for oblique factors, which means that the factors  $F_q$  may have mutual correlation structure. But that is pretty much everything the APT tells us about the latent factors. It does neither provide information about what they are, nor how many of them to include. Nevertheless, working with the APT is no more difficult than working with the CAPM, which is why the APT is very popular with practitioners.

# Comparing CAPM and APT

Using CAPM and APT makes them appear like close relatives. Analyzing their foundations reveals fundamental differences. But let's first look at the similarities in their application. We have seen that the  $\beta$ -coefficient of a risky security in the framework of the CAPM can be estimated by linear regression. The  $\lambda$ s in the APT can be estimated by multiple linear regression

$$|y\rangle = X|\lambda\rangle + |\epsilon\rangle,\tag{7.83}$$

. . . . . . . . . . . . . . . . . . . .

where

$$|y\rangle = \begin{pmatrix} y_1 \\ \vdots \\ y_T \end{pmatrix}, \quad X = \begin{pmatrix} 1 & x_{1,1} & \dots & x_{Q,1} \\ \vdots & \vdots & & \vdots \\ 1 & x_{1,T} & \dots & x_{Q,T} \end{pmatrix}, \quad |\lambda\rangle = \begin{pmatrix} \lambda_0 \\ \vdots \\ \lambda_Q \end{pmatrix}, \quad |\epsilon\rangle = \begin{pmatrix} \epsilon_1 \\ \vdots \\ \epsilon_T \end{pmatrix}. \tag{7.84}$$

If we identify the realized values of the response variable and the regressors, as we did before, with

$$y_t = r_{S,t} - r$$
 and  $x_{q,t} = f_{q,t} - r,$  (7.85)

then we obtain the estimate of the coefficient vector  $|\lambda\rangle$  by least-squares,

 $|\hat{\lambda}\rangle = (X'X)^{-1}X'|_{V}\rangle.$  $(7.86)$ 

7.6

As in case of the CAPM, we certainly expect the estimate λˆ <sup>0</sup> to be approximately zero, if the APT is correct. Everything we said about the statistical properties still remains valid. From (7.86) we can only tell the difference, because we called the coefficients of the APT λ and not β. This is a very close resemblance.

What about the differences? The CAPM was derived, departing from modern portfolio theory. The framework included multivariate normal and independently distributed returns, the same risk-free interest rate for borrowing and lending, and equilibrium prices of assets. All of these features have been the subject of harsh criticism in the past, although empirical results do not support rejection of the CAPM. The APT on the other hand is based only on the assumption that in very large markets there should not be any arbitrage opportunities. The absence of arbitrage is an extremely general requirement. Realize that in the presence of arbitrage opportunities, there cannot be an equilibrium, because agents would trade in strategies to exploit them, until price adjustments remove these opportunities. But the absence of arbitrage does not require an equilibrium. The bottom line is that APT operates under extremely mild and barely criticizable conditions. On the other hand, its implications only apply to large portfolios and markets. In small markets, APT can be violated quite seriously. The theoretical implications are also far more general than those of the CAPM. The APT merely provides the shape of the relation between latent factors and the security returns. It says neither what they are, nor how many of them are needed. The fact that the CAPM is reproduced as one particular manifestation of the APT, clearly strengthens the theoretical rationale of the CAPM.

## **7.7 Further Reading**

The classical references for the capital asset pricing model (CAPM) are Sharpe (1964), Lintner (1965), and Mossin (1966). For an excellent review including all technical assumptions, see Gatfaoui (2010). For a non-technical discussion of the CAPM see Estrada (2005, chap. 6 & 7). The former source also discusses the three-factor extension of Fama and French (1993, 1996). The original sources for the arbitrage pricing theory (APT) are Ross (1976), and Roll and Ross (1980). A compressed discussion of the concepts involved can be found in Shiryaev (1999, sect. 2d). A very careful and accessible treatment of this subject is Huberman (1982), and also Ingersoll (1987, chap. 7). Statistical and econometrical issues of regression analysis and parameter estimation are treated thoroughly in Greene (2003). For the factor analytic model see Mardia et al. (2003, chap. 8 & 9).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

## **7.8 Problems**

- • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •
- **7.1** Practitioners often assume that the true yearly β of a security decays towards βMP = 1 with time. A simple model for such a mean reversion process is

$$\hat{\beta}_{k+1} = \frac{1}{3}\hat{\beta}_k + \frac{2}{3},$$

where  $\hat{\beta}_k = E[\beta_{t+k}|\mathcal{F}_t]$ . Show that  $\hat{\beta}_k$  is given by

$$\hat{\beta}_k = 1 + \left(\frac{1}{3}\right)^k (\hat{\beta}_0 - 1).$$

**7.2** Prove that the half life of the difference  $\hat{\beta}_0 - \beta_{\text{MP}}$  in Problem 7.1 is

$$k = \frac{\log 2}{\log 3} \approx 0.63$$

years.

7.3 Look at the general mean reversion structure

$$\hat{\beta}_{k+1} = \lambda \hat{\beta}_k + (1 - \lambda),$$

where  $0 \le \lambda \le 1$  is an arbitrary coefficient. How is  $\lambda$  to be chosen if the intrinsic period is one month, to maintain the term structure of the yearly period model?

7.4 For an arbitrary random variable Y and a  $\sigma$ -algebra  $\mathcal{F}_4$ , generated by observing some event  $A$ , the variance decomposition

$$\text{Var}[Y] = \text{Var}[E[Y|\mathcal{F}_A]] + E[\text{Var}[Y|\mathcal{F}_A]]$$

holds. Show that the unconditional variance of the least-squares estimator  $|\hat{\beta}\rangle$  is

$$\text{Var}[\hat{\beta}] = \sigma_{\epsilon}^2 E[(X'X)^{-1}],$$

where  $X$  is the usual data matrix, containing a column of ones and the regressors  $X_t$ , for  $t = 1, ..., T$ .

7.5 The original three-factor portfolio model of Fama and French (1993, 1996) is formulated in the form

$$R_P = R_0 + \beta_1 (R_{\rm MP} - R_0) + \beta_2 \text{SMB}_P + \beta_3 \text{HML}_P + \epsilon_P,$$

where SMB indicates the market capitalization spread ("small minus big"), and HML is the spread in the book-to-market ratio ("high minus low"). Show that this model is empirically indistinguishable from a three-factor APT-model, if the restriction

$$\alpha = \lambda_0 - r(\lambda_2 + \lambda_3)$$

holds, and  $\beta_q = \lambda_q$  for  $q = 1, 2, 3$ .

7.6 Show that the modified factor model

$$|R\rangle = R_0 \left| |1\rangle \right| - \Lambda \left| |1\rangle + \Lambda |F\rangle + |\epsilon\rangle,$$

with  $E[F_q] = \mu_{F_q}$ ,  $\text{Cov}[F_p, F_q] = \sigma_{pq}$ ,  $\text{Cov}[F_q, \epsilon_n] = 0$ ,  $E[\epsilon_n] = 0$ , and  $\text{Cov}[\epsilon_m, \epsilon_n] = 0$  $\delta_{mn}\sigma_n^2$ , generates the correct APT-equation (7.57).
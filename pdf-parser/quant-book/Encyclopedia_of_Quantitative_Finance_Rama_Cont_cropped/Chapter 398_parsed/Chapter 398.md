# **Credibility Theory**

Credibility originates from the insurance industry and its basic idea goes back as far as the year 1918, when Whitney [20] was confronted with the problem of estimating risk premiums in workmen compensation. For the premium of an individual contract  $i$ , he suggested taking a weighted mean

$$\widehat{\mu_i} = \alpha \overline{X}_i + (1 - \alpha) \overline{X} \tag{1}$$

where  $\overline{X}_i$  is the observed average claim amount per volume unit for the individual contract *i* and  $\overline{X}$ is the corresponding overall mean of the insurance portfolio. The expression *credibility* was originally used for the weight  $\alpha$  in equation (1), which is a measure of reliability attached to the individual claims experience.

Since then, *credibility theory* has become an established discipline of insurance mathematics. Though mainly encountered in insurance applications, it also has the potential to be a powerful tool in the wider field of finance, where applications are found in credit risk (see Credit Risk) and in operational risk (see Operational Risk) assessments.

Credibility theory deals with the fundamental concepts of *individual risk* and *collective* or *individual* claims experience and a priori knowledge. The aim is to assess the individual risks. There are two sources of information on an individual risk: observations of the individual risk on the one hand, and a priori knowledge, gained from other similar risks in the portfolio (the collective) or from an expert opinion (personal belief), on the other.

Credibility theory can be described as follows:

- It answers the question of how one should combine the information out of the two sources to get a "best" estimate of the individual risk.
- It is the mathematical tool to describe heterogeneous collectives.
- It belongs mathematically to the area of Bayesian statistics.

A concise description of credibility theory and its development seen from the perspective of its essential mathematical structure can be found in [17]. References [5, 8] are some recent textbooks on credibility.

## **Credibility Estimators**

In a simple set-up, the underlying paradigm is the "two-urn" model. The individual risk is characterized by its risk characteristic  $\vartheta$ , which is drawn from the first urn describing the risk structure within the collective. Hence  $\vartheta$  is a realization of a random variable  $\Theta$ . Given  $\Theta = \vartheta$ , the claims are drawn from the second urn with distribution  $F_{\vartheta}$ . The risk premium becomes a random variable  $\mu(\Theta)$ , which has to be estimated from the observed data  $X$ . The objective is to find an estimator  $\mu(\Theta)$ , which minimizes the quadratic loss or mean squared error (mse)

$$\mathrm{mse}\left(\widehat{\mu\left(\Theta\right)}\right) = E\left[\widehat{\mu\left(\Theta\right)} - \mu\left(\Theta\right)\right)^{2}\right] \qquad (2)$$

The "two-urn" model formulates the problem in the language of Bayesian statistics. Essentially, this had already been done in the 1940s by Bailey [1], but it became well known only in the late 1960s, when it was set out clearly by Bühlmann in [2, 3].

The estimator minimizing equation  $(2)$  is the Baves estimator

$$\mu\left(\Theta\right)^{\text{Bayes}} = E\left[\mu\left(\Theta\right)|\mathbf{X}\right] \tag{3}$$

In many models, it is a linear function of the observations. This is, in particular, the case for the one-parametric exponential family with its natural conjugate prior [13]. A famous example is the Poisson–Gamma model, where  $\Theta$  is Gamma distributed and where the observations, the claim numbers, are Poisson distributed with parameter  $\Theta$ . This model was the actuarial basis for the construction of bonus-malus systems in third-party motor liability. The case where the Bayes estimator is a linear function of the observations is referred to as exact *credibility*. As an example, we consider the situation where we want to design a bonus-malus scheme for fleets of cars. We assume that the *a priori* expected number of claims within a given period (e.g.,  $1 \text{ year}$ ) for a specific fleet *i* is equal to  $v_i$ , which is known and can be calculated on the basis of objective tariff variables. On the other hand, we know that things like driver education might have considerable influence and that the true expected number of claims for that particular fleet is  $\mu(\Theta_i) = \Theta_i \nu_i$ , where  $\Theta_i$ is an unknown risk quality factor for that particular fleet with  $E[\Theta_i] = 1$ . We assume that we know from portfolio experience of different fleets that the standard deviation of  $\Theta_i$  is equal to  $\tau$ . Now we have observed a number of  $N_i$  claims in the given period for fleet  $i$ . On the basis of the Poisson–Gamma model we then obtain the following bonus-malus factor by which the base premium is multiplied to obtain the experience-rated premium:

$$\widehat{\Theta_i} = 1 + \alpha_i \left( \frac{N_i}{\nu_i} - 1 \right), \text{ where } \alpha_i = \frac{\nu_i}{\nu_i + \tau^{-2}}$$
(4)

For instance, if  $v_i = 20$ ,  $N_i = 15$ , and  $\tau = 20\%$ , then there results a bonus-malus factor of 89%.

In general, the Bayes estimator cannot be expressed in closed analytical form. Moreover, one has to specify the family  $\{F_{\vartheta}\}\$  of distributions as well as the structure distribution  $U$ , which are both mostly not known in practice.

The basic idea behind credibility is to *restrict* the class of allowable estimator functions to those which are *linear* in the components of the observation vector **X.** Credibility estimators are therefore linear Bayes estimators, minimizing the mse within the class of linear estimators.

The so-called normal equations play a central role, that is,  $\mu(\Theta)^{\text{cred}}$  is the credibility estimator of  $\mu(\Theta)$ based on  $\mathbf{X}^T = (X_1, \dots X_n)$  if and only if it satisfies the normal equations

$$E\left[\mu\left(\Theta\right)^{\text{cred}} - \mu(\Theta)\right] = 0, \tag{5}$$
  

$$\text{Cov}\left[\mu\left(\Theta\right)^{\text{cred}}, X_{j}\right] = \text{Cov}\left[\mu(\Theta), X_{j}\right]$$
  

$$\text{for } j = 1, 2, \dots, n \tag{6}$$

Hence the credibility estimator only depends on first and second moments and not on the whole underlying distributions.

The only mathematical structure in the most general credibility set-up is the fact that one wants to estimate a random variable  $\mu(\Theta)$  based on a random vector  $\mathbf{X}^T$ . Neither  $\mu(\Theta)$  nor the components of  $\mathbf{X}^T$ are further specified, that is, the observations  $X_i$  can also be functions of some other original observations.

Credibility is most elegantly understood by looking at the space  $\mathcal{L}^2$  of square integrable random variables.  $\mathcal{L}^2$  together with the inner product  $\langle X, Y \rangle := E[XY]$  is a Hilbert space. The corresponding norm of an X in  $\mathcal{L}^2$  is  $||X|| = \sqrt{\langle X, X \rangle}$ .

The advantage of looking at credibility in this way is that we can apply our intuitive understanding of the properties of linear vector spaces to the credibility problem. The mse of an estimator  $\widehat{\mu(\Theta)}$  becomes  $\|\widehat{\mu(\Theta)} - \mu(\Theta)\|^2$  and the credibility estimator is the point in the subspace  $L(\mathbf{X}, 1) :=$  $\left\{\widehat{\mu(\Theta)}:\widehat{\mu(\Theta)}=a_0+\sum_{i=1}^n a_iX_i,\quad a_0,a_1,\ldots\in\mathbb{R}\right\}$ closest to  $\mu(\Theta)$ . Hence  $\mu(\Theta)^{\text{cred}}$  is the orthogonal projection of  $\mu(\Theta)$  on  $L(\mathbf{X}, 1)$ , and the normal equations  $(5)$  and  $(6)$  follow from the orthogonality property. For a historical perspective of the Hilbert space approach in the context of credibility, we refer to [9].

#### The Bühlmann–Straub Model

The Bühlmann-Straub (BS) [7] model is the best known credibility model that is widely used in practice. It extends the simple Bühlmann model [2] by allowing for observations with associated weights, which are very often encountered in practice such as when considering claim averages, claim frequencies, loss ratios, and so on.

The risks are embedded in a collective of similar risks numbered  $i = 1, 2, \ldots, I$ , each of which is characterized by its own  $\Theta_i$  and has observations  $\{X_{ij}: j = 1, 2, \ldots, n_i\}$  with associated weights  $w_{ij}$ . The BS model assumes that, conditionally on  $\Theta_i$ , the random variables  $\{X_{ij}: j = 1, 2, \ldots, n_i\}$  are independent with

$$E\left[X_{ij} \left|\Theta_i\right.\right] = \mu\left(\Theta_i\right) \tag{7}$$

$$\operatorname{Var}\left[X_{ij} \mid \Theta_i\right] = \frac{\sigma^2(\Theta_i)}{w_{ij}} \tag{8}$$

that the pairs  $(\Theta_1, \mathbf{X}_1)$ ,  $(\Theta_2, \mathbf{X}_2)$ , ... are independent and that  $\Theta_1, \Theta_2, \ldots$  are independent and identically distributed (i.i.d.).

A heterogeneous portfolio is modeled in this manner. The risks in the portfolio are different: they have different risk profiles  $\Theta_i$ . But the risks in the portfolio also have something in common: *a priori*, they cannot be recognized as being different, which results from the fact that the risk profiles  $\Theta_i$  are i.i.d.

The credibility estimator turns out to be a weighted mean

$$\mu(\Theta_i)^{\text{cred}} = \alpha_i \overline{X}_i + (1 - \alpha_i) \,\mu \tag{9}$$

where

$$\overline{X}_{i} = \sum_{j} \frac{w_{ij}}{w_{i\bullet}} X_{ij}, \ w_{i\bullet} = \sum_{j} w_{ij}, \ \alpha_{i} = \frac{w_{i\bullet}}{w_{i\bullet} + \frac{\sigma^{2}}{\tau^{2}}}$$
(10)

and where  $\mu$ ,  $\sigma^2$ , and  $\tau^2$  are the so-called structural parameters

$$\mu = E\left[\mu\left(\Theta_{i}\right)\right], \ \sigma^{2} = E\left[\sigma^{2}(\Theta_{i})\right],$$
  
$$\tau^{2} = \text{Var}\left[\mu\left(\Theta_{i}\right)\right] \tag{11}$$

The mse is

$$\operatorname{mse}(\mu(\Theta_i)^{\operatorname{cred}}) = (1 - \alpha_i) \tau^2 = \alpha_i \frac{\sigma^2}{w_{i\bullet}} \qquad (12)$$

The credibility estimator  $(9)$  has a natural interpretation. The expected value  $\mu$  over the whole collective is the best estimator based only on the *a priori* knowledge and ignoring the individual observations, whereas  $\overline{X}_i$  is the best linear estimator when looking only at the individual observations and ignoring the  $a$ priori knowledge (optimally compressed data, linear sufficient statistics). The credibility estimator takes both sources of information into account and is a weighted mean of the two components with weights inversely proportional to the mse. This general intuitive principle is also valid in the more general models.

The assumption that the risks in the portfolio are  $a$ *priori* equal is rather strong and often not fulfilled in practice. Often, there are known *a priori* differences between risks, that is, instead of equation (7) we have  $E[X_{ij}|\Theta_i] = a_i \mu(\Theta_i)$  with known constants  $a_i$ . However, by a linear transformation one can transform the problem to the BS model and still apply it.

The credibility estimator  $(9)$  does not depend on the observations of the other risks in the portfolio. However, the structural parameters are usually not known, in practice, and have to be estimated from the data of the collective. For the overall mean  $\mu$ , one can restrict the class of estimators further by allowing only linear estimators without a constant term. The best estimator out of this class is named the *homogeneous credibility estimator*,  $\mu(\Theta_i)_{\text{hom}}^{\text{cred}}$ , and contains a built-in estimator for  $\mu$ . In the BS model it is obtained by replacing  $\mu$  in equation (9) by

$$\widehat{\mu} = \sum_{i} \frac{\alpha_{i}}{\alpha_{\bullet}} \overline{X}_{i}, \text{ where } \alpha_{\bullet} = \sum_{i} \alpha_{i} \qquad (13)$$

When replacing the structural parameters in equation (9) by their estimated values, one arrives at the empirical credibility estimator. It can be shown [16] that under rather general conditions, the empirical credibility estimator converges in probability to the credibility estimator if the size of collateral data increases.

### **Hierarchical Credibility**

Hierarchical credibility is an extension of the BS model in the sense that it generalizes the "twourn" model to a "many-urn model". In such models, the risk characteristics of the individual risks are drawn from a collective urn whose risk characteristics are drawn from a further parent urn and so on. Such hierarchies appear naturally in many situations. For instance, in insurance pricing, one often encounters the situation that individual risks are classified according to their "tariff positions", tariff positions are grouped together into "subgroups", subgroups into "groups", groups into "main groups", which together make the total of a line of business. A hierarchical model has the advantage of leading to a well-founded, properly balanced distribution of the burden of claims, in particular, of large claims, among the individual risks.

The concept of hierarchical credibility was introduced by Jewell [14] and Taylor [19]. It is best understood when looking at credibility estimators as orthogonal projections on linear subspaces, which, as shown in [6], leads to a recursive calculation of the credibility estimators. First, a linear sufficient statistics is calculated bottom up, and then the credibility estimators are calculated top down, where the estimators on the different levels have the same structure as the ones in the BS model.

#### **Multidimensional Credibility**

The essence of *multidimensional credibility* is that one wants to estimate a real-valued vector  $\mu(\Theta)$  =  $(\mu_1(\Theta), \ldots, \mu_p(\Theta))^T$  as, for instance, the claims load for "normal claims" and "big claims", "claim frequency" and "claim size", the claims load in different layers, and so on. The point is that one estimates the components of  $\mu(\Theta)$  simultaneously on the basis of the same observation vector  $\mathbf{X}$ . For instance, when estimating the claims load for big claims, one also looks at the observed claims load for normal claims, and *vice versa*.

Multidimensional credibility was introduced by Jewell [12]. A convenient way is to consider an abstract setup, where  $X$  has the same dimension as  $\mu\left(\Theta\right)$  with  $E\left[\mathbf{X}\left|\Theta\right.\right] = \mu\left(\Theta\right)$  and  $\text{Cov}(\mathbf{X}, \mathbf{X}^{T}\left|\Theta\right.\right) =$  $\Sigma(\Theta)$ . This vector **X** may be obtained by data compression from the raw data. The structure of the credibility estimator inherits its form from the simple model and becomes

$$\boldsymbol{\mu}(\Theta)^{\text{cred}} = A\,\mathbf{X} + (I - A)\,\boldsymbol{\mu} \tag{14}$$

where

$$A = T \left(T + S\right)^{-1} \tag{15}$$

is the credibility matrix,  $I$  is the identity matrix, and

$$\boldsymbol{\mu} = E\left[\boldsymbol{\mu}\left(\Theta\right)\right], \ S = E\left[\boldsymbol{\Sigma}\left(\Theta\right)\right],$$
  
$$T = \text{Cov}\left[\boldsymbol{\mu}\left(\Theta\right), \boldsymbol{\mu}\left(\Theta\right)^{T}\right]$$
 (16)

are the structural parameters.

Mostly, one is not primarily interested in the individual components of the vector  $\mu(\Theta)$ , but rather in a linear combination

$$\mu(\Theta) := \sum_{k=1}^{p} a_k \mu_k(\Theta) = \mathbf{a}^T \boldsymbol{\mu}(\Theta) \qquad (17)$$

For the mse of  $\mu$  ( $\Theta$ ) one obtains

$$\text{mse}(\mu(\Theta)) = \mathbf{a}^T V_2 \mathbf{a} \tag{18}$$

where

$$V_2 = (I - A) T = A S \t\t(19)$$

is the *mse matrix*.

The optimal data compression to reduce the raw data to a vector  $\mathbf{X}$  of the same dimension as  $\mu(\Theta)$  is discussed in [5] and can be expressed as an orthogonal projection on a translated subspace

$$\mathbf{B} = \text{Pro} \left( \boldsymbol{\mu}(\Theta) \middle| L_e^{\text{ind}} \left( \mathbf{X} \right) \right) \tag{20}$$

where

$$L_e^{\text{ind}}(\mathbf{X}) = \left\{ \widehat{\boldsymbol{\mu}(\Theta)} \colon \widehat{\mu_k(\Theta)} = \sum_j a_j^{(k)} X_j \right\}$$
  
for  $k = 1, \dots, p; E\left[ \widehat{\boldsymbol{\mu}(\Theta)} \middle| \Theta \right] = \boldsymbol{\mu}(\Theta) \right\}$  (21)

#### Credibility in the Regression Case

The credibility regression model was introduced by Hachemeister [11] and motivated by the problem of forecasting average claim amounts for bodily injury claims in third-party auto liability for various states in the United States. In contrast to classical statistics, the regression parameters are assumed to be a random vector  $\beta(\Theta)$ , that is, it is assumed that

$$E\left[\mathbf{X}|\Theta\right] = Y \boldsymbol{\beta}(\Theta) \tag{22}$$

$$\operatorname{Cov}\left(\mathbf{X}, \mathbf{X}^{T} \middle| \Theta\right) = \Sigma\left(\Theta\right) \tag{23}$$

where  $\mathbf{X}$  is the observation vector of a particular risk, Y is the corresponding design matrix and  $\beta$  ( $\Theta$ ) the regression vector. The credibility estimator of  $\beta$  ( $\Theta$ ) is most elegantly found by making use of the multidimensional credibility result. The optimal data compression is

$$\mathbf{B} = \left(Y^T S^{-1} Y\right)^{-1} Y^T S^{-1} \mathbf{X} \tag{24}$$

and by applying equation  $(14)$  one obtains

$$\boldsymbol{\beta}(\Theta)^{\text{cred}} = A \, \mathbf{B} + (I - A) \, \boldsymbol{\beta} \tag{25}$$

where

$$A = T \left( T + \left( Y^T S^{-1} Y \right)^{-1} \right)^{-1}$$
  
$$\boldsymbol{\beta} = E \left[ \boldsymbol{\beta} \left( \Theta \right) \right], \quad S = E \left[ \Sigma \left( \Theta \right) \right],$$
  
$$T = \text{Cov} \left[ \boldsymbol{\beta} \left( \Theta \right), \boldsymbol{\beta} \left( \Theta \right)^T \right]$$
 (26)

In many practical situations,

$$\Sigma\left(\Theta\right) = \sigma^{2}(\Theta)W^{-1} \tag{27}$$

where  $W$  is a diagonal matrix with known weights  $w_i$  down the diagonal. Then

$$\mathbf{B} = \left(Y^T W Y\right)^{-1} Y^T W \mathbf{X} \tag{28}$$
$$A = T \left(T + \sigma^2 \left(Y^T W Y\right)^{-1}\right)^{-1},$$
$$\text{where } \sigma^2 = E \left[\sigma^2(\Theta)\right] \tag{29}$$

When Hachemeister applied the theory to his data on bodily injury (a case of simple regression), he obtained some "rather strange" results for some of the states. The solution is found in [4]: one should work with an orthogonal design matrix. In the simple linear regression case, this means that one should choose the barycenter not at the origin but rather at the center of gravity of time. Then the credibility estimators for the two regression components "barycenter" and "slope" split into two one-dimensional credibility formulas of the same type as in the BS-model.

### **Evolutionary Credibility Models**

Evolutionary credibility models are characterized by the fact that the risk parameters vary stochastically in time. Such models are closely tied to recursive credibility formulae often referred to as recursive credibility.

References  $[10, 18]$  are some of the early actuarial papers devoted to *evolutionary or recursive credibil*ity. A well-known recursive procedure developed in an engineering context is the Kalman Filter [15] (see also Filtering).

In the one-dimensional evolutionary credibility *model*, a specific risk with observation vector  $\mathbf{X}$ is again characterized by its individual risk profile. However, this risk profile is itself a stochastic process, that is, a sequence of random variables

$$\mathbf{\Theta} = \left\{ \Theta_1, \Theta_2, \dots, \Theta_j, \dots \right\} \tag{30}$$

The components  $\Theta_i$  are to be understood as the risk profile in year  $j$  and it is assumed that

$$E[X_j|\mathbf{\Theta}] = E[X_j|\Theta_j] = \mu(\Theta_j) \quad (31)$$

$$\operatorname{Var}\left[X_{j}|\mathbf{\Theta}\right] = \operatorname{Var}\left[X_{j}|\Theta_{j}\right] = \frac{\sigma^{2}\left(\Theta_{j}\right)}{w_{j}} \quad (32)$$

where  $X_j$  is the observation in year j,  $w_j$  an appropriate weight and  $E\left[\sigma^2\left(\Theta_i\right)\right] = \sigma^2$ . The aim is to find for each year  $n$  the credibility estimator of  $\mu$  ( $\Theta_n$ ) based on the observations  $\{X_1, \ldots, X_{n-1}\}$ .

It is useful to split up the step from  $\mu \left(\Theta_n\right)^{\text{cred}}$  to  $\mu \left(\Theta_{n+1}\right)^{\text{cred}}$  into two steps:

#### 1. Updating

Improve the estimation of  $\mu(\Theta_n)$  on the basis of the newest information  $X_n$ .

#### 2. Parameter movement

Change the estimation owing to the switch of the parameter from  $\mu$  ( $\Theta_n$ ) to  $\mu(\Theta_{n+1})$ .

In this connection, it is suitable to introduce the terminology and notation from state space models:

$$\mu_{n|n-1} := \text{Pro} \left( \mu \left( \Theta_n \right) | L \left( 1, X_1, \dots, X_{n-1} \right) \right),$$
  

$$\mu_{n|n} := \text{Pro} \left( \mu \left( \Theta_n \right) | L \left( 1, X_1, \dots, X_{n-1}, X_n \right) \right),$$
  

$$q_{n|n} := E \left[ \left( \mu_{n|n} - \mu \left( \Theta_n \right) \right)^2 \right],$$
  

$$q_{n|n-1} := E \left[ \left( \mu_{n|n-1} - \mu \left( \Theta_n \right) \right)^2 \right]$$
  
(33)

Here  $\mu_{n|n-1}$  is just another notation for  $\mu$  ( $\Theta_n$ )<sup>cred</sup>, which is the credibility estimator of  $\mu(\Theta_n)$  based on the observations  $X_1, \ldots, X_{n-1}$ , whereas  $\mu_{n|n}$ is the updated estimator of  $\mu(\Theta_n)$  based on the observations  $X_1, \ldots, X_{n-1}, X_n$ .

If the observations in different years are, on the average, conditionally uncorrelated, and if the process  $\mu\left(\Theta\right)$  has orthogonal increments, that is, if

$$E\left[\text{Cov}\left(X_{k}, X_{j} \middle| \boldsymbol{\Theta}\right)\right] = 0 \tag{34}$$
  

$$\text{Pro}\left(\mu\left(\Theta_{n+1}\right) \middle| L\left(1, \mu\left(\Theta_{1}\right), \dots, \mu\left(\Theta_{n}\right)\right)\right)$$
  

$$= \mu\left(\Theta_{n}\right) \quad \text{for } n \ge 1 \tag{35}$$

then the credibility estimators can be calculated by the following recursive procedure ("Kalman filter notation"):

#### 1. Anchoring (Period 1)

$$\mu_{1|0} = E \left[ \mu \left( \Theta_1 \right) \right] \quad \text{and}\n$$

$$\nq_{1|0} = E \left[ \left( \mu_{1|0} - \mu \left( \Theta_1 \right) \right)^2 \right] \tag{36}$$

#### 2. Recursion $(n \ge 1)$

(a) Updating

$$\mu_{n|n} = \alpha_n X_n + (1 - \alpha_n) \mu_{n|n-1} \quad (37)$$
  
where  $\alpha_n = \frac{q_{n|n-1}}{q_{n|n-1} + \frac{\sigma^2}{w_n}},$   
 $q_{n|n} = (1 - \alpha_n) q_{n|n-1} \quad (38)$ 

(b) Change from  $\mu$  ( $\Theta_n$ ) to  $\mu$  ( $\Theta_{n+1}$ ) (parameter movement)

$$\mu_{n+1|n} = \mu_{n|n} \tag{39}$$

$$q_{n+1|n} = q_{n|n} + \delta_{n+1}^2 \tag{40}$$

where *δ*<sup>2</sup> *<sup>n</sup>*+<sup>1</sup> = Var[*µ(n*<sup>+</sup>1*)* − *µ(n)*].

The collection of models can be enlarged by allowing linear transformation on the right-hand side of equation *(*35*)* and adjusting equations *(*39*)* and *(*40*)* accordingly.

The evolutionary model sketched here can easily be extended to the *evolutionary regression credibility model.* By an appropriate choice of the components of *β (n)*, the evolutionary regression model allows the modeling of a large number of evolutionary phenomena. In particular, one can model in this way all situations where the process *µ j* : *j* = 1*,* 2*,...* is an autoregressive moving average (ARMA) process (*see* **Autoregressive Moving Average (ARMA) Processes**). Analogously, one can extend the idea to the multidimensional case and consider the *evolutionary multidimensional credibility model*. It allows to model situations where the individual risk over time depends both on specific individual factors as well as on global factors affecting all risks in the collective simultaneously (see [5] for further details). Such models might, besides insurance, also be suitable for applications in finance.

## **References**

- [1] Bailey, A.L. (1950). Credibility procedures, Laplace's generalization of Bayes' Rule, and the combination of collateral knowledge with observed data, *Proceedings of the Casualty Actuarial Society* **37**, 7–23.
- [2] Buhlmann, H. (1967). Experience rating and credibility, ¨ *ASTIN Bulletin* **4**, 199–207.
- [3] Buhlmann, H. (1969). Experience rating and credibility, ¨ *ASTIN Bulletin* **5**, 157–165.
- [4] Buhlmann, H. & Gisler, A. (1997). Credibility in the ¨ regression case revisited, *ASTIN Bulletin* **27**, 83–98.
- [5] Buhlmann, H. & Gisler, A. (2005). ¨ *A Course in Credibility Theory and its Applications*, Universitext, Springer, Berlin.
- [6] Buhlmann, H. & Jewell, W.S. (1987). Hierarchical ¨ credibility revisited, *Bulletin of the Swiss Association of Actuaries* **87**, 35–54.

- [7] Buhlmann, H. & Straub, E. (1970). Glaubw ¨ urdigkeit ¨ fur Schadens ¨ atze, ¨ *Bulletin of the Swiss Association of Actuaries* **76**, 111–133.
- [8] Dannenburg, D.R., Kaas, R. & Goovaerts, M.J. (1996). *Practical Actuarial Credibility Models*, Institute of Actuarial Science and Econometrics, Amsterdam.
- [9] De Vylder, F. (1976). Geometrical credibility, *Scandinavian Actuarial Journal* **76**, 121–149.
- [10] Gerber, H.U. & Jones, D.A. (1975). Credibility formulas of the updating type, *Transaction of the Society of Actuaries* **27**, 39–52.
- [11] Hachemeister, C.A. (1975). Credibility for regression models with application to trend, in *Credibility: Theory and Applications*, P.M. Kahn, ed., Academic Press, New York, pp. 129–163.
- [12] Jewell, W.S. (1973). *Multidimensional Credibility*, Report ORC Berkeley, Operations Research Center, Berkeley.
- [13] Jewell, W.S. (1974). Credibility means are exact Bayesian for simple exponential families, *ASTIN Bulletin* **8**, 77–90.
- [14] Jewell, W.S. (1975). The use of collateral data in credibility theory: a hierarchical model, *Giornale dell'Instituto Italiano degli Attuari* **38**, 1–16.
- [15] Kalmann, R.E. (1960). A new approach to linear filtering and prediction problems, *Transactions of ASME-Journal of Basic Engineering* **82**, 35–45.
- [16] Norberg, R. (1980). Empirical Bayes credibility, *Scandinavian Actuarial Journal* **38**, 177–194.
- [17] Norberg, R. (2004). Credibility theory, in *Encyclopedia of Actuarial Science*, J.L. Teugels & B. Sundt, eds, Wiley, Chichester, UK, pp. 398–406.
- [18] Sundt, B. (1981). Recursive credibility estimation, *Scandinavian Actuarial Journal* 3–22.
- [19] Taylor, G.C. (1979). Credibility analysis of a general hierarchical model, *Scandinavian Actuarial Journal* 1–12.
- [20] Whitney, A.W. (1918). The theory of experience rating, *Proceedings of the Casualty Actuarial Society* **4**, 274–292.

## **Related Articles**

#### **Credit Rating**; **Credit Scoring**.

ALOIS GISLER
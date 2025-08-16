# **Copulas: Estimation**

Copulas are a tool for modeling and capturing the dependence of two or more random variables (rv's). In the work of Sklar [22], the term *copula* was used for the first time; it is derived from the Latin word *copulare*, which means to connect or to join. Similarly, Hoeffding had already studied distributions under "arbitrary changes of scale" in the 1940s; see [7].

The main purpose of a copula is to disentangle the dependence structure of a random vector from its marginals. A  $d$ -dimensional copula is defined as a function  $C : [0, 1]^d \rightarrow [0, 1]$ , which is a cumulative distribution function (cdf) with uniform<sup>a</sup> marginals. On one hand, this leads to the following properties:

- 1.  $C(u_1, \ldots, u_d)$  is increasing in each component  $u_i, i \in \{1, \ldots, d\}.$
- 2.  $C(1, \ldots, 1, u_i, 1, \ldots, 1) = u_i$  for all  $1 \le i \le d$ .
- 3. For  $a_i < b_i$ ,  $1 < i < d$ , C satisfies the rectangle inequality

$$\sum_{i_1=1}^2\cdots\sum_{i_d=1}^2(-1)^{i_1+\ldots+i_d}C(u_{1,i_1},\ldots,u_{d,i_d})\geq 0,$$

where  $u_{j,1} = a_j$  and  $u_{j,2} = b_j$ .

On the other hand, every function satisfying  $(1)$ – $(3)$ is a copula. Furthermore,  $C(1, u_1, \ldots, u_{d-1})$  is again a copula and so are all  $k$ -dimensional marginals with  $2 < k < d$ .

The construction of multivariate copulas is difficult. There is a rich literature on uni- and bivariate distributions but many of these families do not have obvious multivariate generalizations.<sup>b</sup> Similarly, it is not at all straightforward to generalize a two-dimensional copula to higher dimensions. For example, consider the construction of threedimensional copulas. A possible attempt is to try  $C_1(C_2(u_1, u_2), u_3)$  where  $C_1, C_2$  are bivariate copulas. However, already for  $C_1 = C_2 = \max\{u_1 + u_2 1, 0$ } (the countermonotonicity copula, introduced in the section *Important Copulas*) this procedure fails. See [18, Section 3.4] for further details. Also Chapter 4 in [11] gives an overview of construction of multivariate copulas with different concepts. In particular, it discusses the construction of a  $d$ -dimensional copula given the set of  $d(d-1)/2$  bivariate margins.

The class of Archimedean copulas (see also the section Archimedean Copulas) is an important class for which the construction of multivariate copulas can be performed quite generally. A common example of a three-dimensional Archimedean copula is given by the following exchangeable Archimedean copula:

$$C(u_1, u_2, u_3) = \phi^{-1}(\phi(u_1) + \phi(u_2) + \phi(u_3)) \quad (1)$$

with appropriate generator  $\phi$ . However, for appropriate  $\phi_1, \phi_2$ ,

$$\phi_1^{-1}(\phi_2 \circ \phi_1^{-1}(\phi_1(u_1) + \phi_1(u_2)) + \phi_2(u_3)) \quad (2)$$

also gives a three-dimensional copula (see [14], Section 5.4.3). It is of course possible that  $\phi_1$  and  $\phi_2$  are generators of different types of Archimedean copulas.

The key to the separation of marginals and dependence structure is the *quantile transformation*. Let U be a standard uniform rv and  $F^{-1}(y) :=$  $\inf \{x : F(x) \ge y\}$  be the generalized inverse of F. Then

$$P\left(F^{-1}(U) \le x\right) = F(x) \tag{3}$$

This result is frequently used for simulation: the generation of uniform rv's is readily implemented in typical software packages and if we are able to compute  $F^{-1}$ , we can sample from F using equation  $(1)$ .

On the contrary, the probability transformation is used to compute copulas implied from distributions, see the following section Copulas derived from Distributions. Consider  $X$  having a continuous distribution function  $F_2$ , then  $F(X)$  is standard uniform.<sup>c</sup>

#### Sklar's Theorem

It is not surprising that every distribution function inherently embodies a copula function. On the other hand, any copula entangled with some marginal distributions in the right way leads to a proper multivariate distribution function. This is the important contribution of Sklar's theorem [22]. Ran  $F$  denotes the range of  $F$ .

**Theorem** Consider a  $d$ -dimensional  $cdf$   $F$  with marginals  $F_1, \ldots, F_d$ . There exists a copula C such that

$$F(x_1, ..., x_d) = C(F_1(x_1), ..., F_d(x_d)) \quad (4)$$

for all  $x_i$  in  $[-\infty, \infty]$ ,  $i = 1, \ldots, d$ . If  $F_i$  is continuous for all  $i = 1, ..., d$  then C is unique; otherwise, *C* is uniquely determined only on Ran  $F_1 \times \ldots \times$ Ran  $F_d$ . On the other hand, consider a copula C and univariate cdf's  $F_1, \ldots, F_d$ . Then F as defined in equation  $(4)$  is a multivariate cdf with marginals  $F_1, \ldots, F_d.$ 

It is important to note that for discrete distributions, copulas are not as natural as they are for continuous distributions; compare [8].

In the following, we therefore concentrate on continuous  $F_i$ ,  $i = 1, \ldots, d$ . It is interesting to examine the consequences of representation  $(2)$  for the copula itself. Using that  $F^{\circ}F^{-1}(y) = y$  for any continuous  $\text{CDF } F$ , we obtain

$$C(\mathbf{u}) = F\left(F_1^{-1}(u_1), \dots, F_d^{-1}(u_d)\right) \tag{5}$$

While relation (4) is usually the starting point for simulations that are based on a given copula and given marginals, relation (5) rather proves to be the theoretical tool to obtain the copula from any multivariate distribution function. This equation also allows to extract a copula directly from a multivariate distribution function.

## **Invariance Under Transformations**

An important property of a copula is that it is invariant under strictly increasing transformations: for strictly increasing functions  $T_i : \mathbb{R} \to \mathbb{R}, i =$  $1, \ldots, d$  the rv's  $X_1, \ldots, X_d$  and  $T_1(X_1), \ldots, T_d(X_d)$ have the same copula.

## **Bounds of Copulas**

Hoeffding and Fréchet independently derived that a copula always lies in between certain bounds; compare Figure 1. This is because of the existence of some extreme cases of dependency, co- and countermonotonicity. The so-called *Fréchet-Hoeffding bounds* are given by

$$\max\left\{\sum_{i=1}^{d} u_i + 1 - d, 0\right\} \le C(\mathbf{u}) \le \min\left\{u_1, \dots, u_d\right\}$$
(6)

which holds for any copula  $C$ . Although a comonotonic copula exists in any dimension  $d$ , there is no countermonotonicity copula in the case of dimensions  $\text{greater than two.}^{\text{d}}$ 

![](_page_1_Figure_12.jpeg)

**Figure 1** According to the Fréchet–Hoeffding bounds, every copula has to lie inside of the pyramid shown in the graph. The surface given by the bottom and back side of the pyramid (the lower bound) is the countermonotonicity copula  $C(u, v) = \max\{u + v - 1, 0\}$ , while the front side (the upper bound) is the comonotonicity copula,  $C(u, v) = \min(u, v)$ 

## Important Copulas

First, the *independence copula* is given by

$$\prod_{i=1}^{d} u_i \tag{7}$$

Random variables are independent if and only if their copula is the independence copula.

The comonotononicity copula or the Fréchet-*Hoeffding upper bound* is given by

$$\min\left\{u_1,\ldots,u_d\right\} \tag{8}$$

Random variables  $X_1, \ldots, X_d$  are called *comono*tonic, if their copula is as in equation (8). This is equivalent to  $(X_1,\ldots,X_d)$  having the same distribution as  $(T_1(Z), \ldots, T_d(Z))$  with some rv Z and strictly increasing functions  $T_1, \ldots, T_d$ . Therefore, comonotonicity refers to perfect dependence in the sense where all rv's are, in an increasing and deterministic way, depending on  $Z$ .

The other case of perfect dependence is given by countermonotonicity. The *countermonotonicity cop*ula reads

$$\max\left\{u_1 + u_2 - 1, 0\right\} \tag{9}$$

Two rv's with this copula are called *countermonotonic*. This is equivalent to  $(X_1, X_2)$  having the same distribution as  $(T_1(Z), T_2(Z))$  for some rv Z and  $T_1$  being increasing and  $T_2$  being decreasing or vice versa. However, the Fréchet-Hoeffding lower bound as given in equation (6) is *not* a copula for  $d > 2$ ; see [14], Example 5.21.

#### Copulas Derived from Distributions

The probability transformation<sup>e</sup> allows to obtain the copula inherent in multivariate distributions: for a multivariate cdf  $F$  with continuous marginals  $F_i$ , the inherent copula is given by

$$C(\mathbf{u}) = F\left(F_1^{-1}(u_1), \dots, F_d^{-1}(u_d)\right) \qquad (10)$$

For example, for a multivariate normal distribution, the implied copula is called Gaussian copula. For a d-dimensional rv X, the correlation matrix<sup>f</sup>  $\Gamma$  is obtained from the covariance matrix by scaling each component to variance 1. Therefore,  $\Gamma$  is given by the entries  $\text{Corr}(X_i, X_j)$ ,  $1 \leq i, j \leq d$  (see Correlation

**Risk**). For such a *correlation matrix*  $\Gamma$  the Gaussian copula is given by

$$\Phi_{\Gamma}(\Phi^{-1}(u_1), \dots, \Phi^{-1}(u_d)) \tag{11}$$

In a similar fashion, one obtains the *t*-copula or the Student copula

$$t_{\nu,\Gamma}(t_{\nu}^{-1}(u_1)\ldots,t_{\nu}^{-1}(u_d))\tag{12}$$

where **Γ** is the correlation matrix,  $t_{\nu}$  is the cdf of the one dimensional  $t_{\nu}$  distribution, and  $t_{\nu}$  is the cdf of the multivariate  $t_{\nu,\Gamma}$  distribution. The mixing nature of the  $t$ -distribution leads to a dramatically different behavior in the tails, which is an important property in applications. See the section *Tail Dependence*.

#### Archimedean Copulas

An important class of analytically tractable copulas are the Archimedean copulas. For the bivariate case, consider a continuous and strictly decreasing function  $\phi : [0, 1] \longrightarrow [0, \infty]$  with  $\phi(1) = 0$ , called the *generator*. Then  $C(u_1, u_2)$  given by

$$\begin{cases} \phi^{-1}(\phi(u_1) + \phi(u_2)) & \text{if } \phi(u_1) + \phi(u_2) \le \phi(0) \\ 0 & \text{otherwise} \end{cases}$$
(13)

is a copula if and only if  $\phi$  is convex; see [18], Theorem 4.1.4. If  $\phi(0) = \infty$  the generator is said to be *strict* and  $C(u_1, u_2) = \phi^{-1}(\phi(u_1) + \phi(u_2)).$ 

For the multivariate case, there are different possibilities of generalization. A relatively special case is when the copula is of the form

$$\phi^{-1}(\phi(u_1) + \ldots + \phi(u_d)) \tag{14}$$

These are the so-called exchangeable Archimedean copulas and  $[15]$  give a complete characterization of such  $\phi$  leading to a copula of the form (7). One may also consider asymmetric specifications of multivariate Archimedean copulas; see [14] Section 5.4.2 and 5.4.3. We present some examples of Archimedean copulas in bivariate case: from the generator  $(-\ln u)^{\theta}$ one obtains the bivariate Gumbel copula or Gumbel-Hougaard copula as follows:

$$\exp\left(-\left[(-\ln u_1)^{\theta} + (-\ln u_2)^{\theta}\right]^{\frac{1}{\theta}}\right) \tag{15}$$

where  $\theta \in [1, \infty)$ . For  $\theta = 1$  it coincides with the independence copula, and for  $\theta \rightarrow \infty$ , it converges to the comonotonicity copula. The Gumbel copula has tail dependence in the upper right corner.

The *Clayton copula* is given by<sup>g</sup>

$$\left(\max\left\{u_1^{-\theta} + u_2^{-\theta} - 1, 0\right\}\right)^{-\frac{1}{\theta}} \tag{16}$$

where  $\theta \in [-1, \infty) \setminus \{0\}$ . For  $\theta \to 0$  it converges to the independence copula, and for  $\theta \to \infty$  to the comonotonicity copula. For  $\theta = -1$  we obtain the Fréchet-Hoeffding lower bound. The generator  $\theta^{-1}(u^{-\theta}-1)$  of the Clayton copula is strict only if  $\theta > 0$ . In this case

$$C_{\theta}^{Cl}(u_1, u_2) = \left(u_1^{-\theta} + u_2^{-\theta} - 1\right)^{-\frac{1}{\theta}} \qquad (17)$$

The generator  $\ln(e^{-\theta}-1) - \ln(e^{-\theta u}-1)$  leads to the Frank copula given by

$$-\frac{1}{\theta} \ln \left( 1 + \frac{(e^{-\theta u_1} - 1) \cdot (e^{-\theta u_2} - 1)}{e^{-\theta} - 1} \right) \tag{18}$$

for  $\theta \in \mathbb{R} \setminus \{0\}$ .

The *generalized Clayton copula* is obtained from the generator  $\theta^{-\delta}(u^{-\theta}-1)^{\delta}$ :

$$\left( \left[ (u_1^{-\theta} - 1)^{\delta} + (u_2^{-\theta} - 1)^{\delta} \right]^{\frac{1}{\delta}} + 1 \right)^{-\frac{1}{\theta}} \tag{19}$$

with  $\theta > 0$  and  $\delta \ge 1$ . Note that for  $\delta = 1$  the standard Clayton copula is to attained; compare [18], Example 4.19.

Further examples of Archimedean copulas may be found in [18], and in particular one may consider Table 4.1 therein as well as Sections  $4.5$  and  $4.6$ (Table 1).

Table 1 List of some copulas. For the Gumbel, Clayton, Frank and the Marshall-Olkin copula, only the bivariate versions are stated. References to the multivariate versions are given in the text. Further copulas may be found in [18], Table 4.1 (p. 94) and Sections 4.5 as well as 4.6

| Name                                                           | Copula                                                                                                                                                                   | Paramter range                  |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| Independence or product copula                                 | $\n\Pi(\mathbf{u}) = \prod u_i\n$                                                                                                                                        |                                 |
| Comonotonicity copula or<br>Fréchet–Hoeffding upper bound      | $M(\mathbf{u}) = \min\left\{u_1, \ldots, u_d\right\}$                                                                                                                    |                                 |
| Countermonotonicity copula or<br>Fréchet–Hoeffding lower bound | $W(u_1, u_2) = \max \{u_1 + u_2 - 1, 0\}$                                                                                                                                |                                 |
| Gaussian copula <sup>(a)</sup>                                 | $C_{\mathbf{F}}^{Ga}(\mathbf{u}) = \Phi_{\mathbf{F}}(\Phi^{-1}(u_1), \ldots, \Phi^{-1}(u_d))$                                                                            |                                 |
| $t$ - or Student copula <sup>(a)</sup>                         | $C_{v,\Gamma}^{t}(\mathbf{u}) = t_{v,\Gamma}(t_{v}^{-1}(u_{1}), \ldots, t_{v}^{-1}(u_{d}))$                                                                              |                                 |
| Gumbel copula or<br>Gumbel–Hougaard copula                     | $C_{\theta}^{Gu}(u_1, u_2) = \exp\left(-\left[(-\ln u_1)^{\theta} + (-\ln u_2)^{\theta}\right]^{\frac{1}{\theta}}\right)$                                                | $\theta \in [1, \infty)$        |
| Clayton copula $^{(b)}$                                        | $C_{\theta}^{Cl}(u_1, u_2) = (\max\{u_1^{-\theta} + u_2^{-\theta} - 1, 0\})^{-\frac{1}{\theta}}$                                                                         | $\theta \in [-1, \infty)$       |
| Generalized Clayton <sup>(b)</sup> copula                      | $C_{\theta,\delta}^{Cl}(u_1,u_2) = \left( \left[ (u_1^{-\theta} - 1)^{\delta} + (u_2^{-\theta} - 1)^{\delta} \right]^{\frac{1}{\delta}} + 1 \right)^{-\frac{1}{\theta}}$ | $\theta \ge 0, \delta \ge 1$    |
| $\text{Frank copula}^{(b)}$                                    | $C_{\theta}^{Fr}(u_1, u_2) = -\frac{1}{\theta} \ln \left( 1 + \frac{(e^{-\theta u_1} - 1) \cdot (e^{-\theta u_2} - 1)}{e^{-\theta} - 1} \right)$                         | $\theta \in \mathbb{R}$         |
| Marshall–Olkin copula or<br>generalized Cuadras-Augé copula    | $C_{\alpha_1,\alpha_2}(u_1,u_2) = \min \left\{ u_2 \cdot u_1^{1-\alpha_1}, u_1 \cdot u_2^{1-\alpha_2} \right\}$                                                          | $\alpha_1, \alpha_2 \in [0, 1]$ |

<sup>&</sup>lt;sup>(a)</sup>Here  $\Gamma$  is a correlation matrix, that is, a covariance matrix where each variance is scaled to 1

<sup>&</sup>lt;sup>(b)</sup> For the (generalized) Clayton and the Frank copula, the case  $\theta = 0$  is given as the limit for  $\theta \to 0$ , which leads to the independence copula in both cases

### The Marshall-Olkin Copula

The *Marshall–Olkin copula* is a copula with singular component. For intuition, consider two components that are subject to certain shocks that lead to failure of either one or both the components. The shocks occur at times that are assumed to be independent and exponentially distributed. Denote the realized shock times by  $Z_1, Z_2$  and  $Z_{12}$ . Then we obtain for the probability that the two components live longer than  $x_1$  and  $x_2$ , respectively,

$$P(Z_1 > x_1)P(Z_2 > x_2)P(Z_{12} > \max\{x_1, x_2\})$$
(20)

This extends to the multivariate case in a straightforward way; compare [4] and [18]. The related copula equals

$$\min\left\{u_2 \cdot u_1^{1-\alpha_1}, u_1 \cdot u_2^{1-\alpha_2}\right\} \tag{21}$$

with  $\alpha_i \in [0, 1]$ . A similar family is given by the Cuadras-Augé copulas

$$\min \{u_1, u_2\} \cdot (\max \{u_1, u_2\})^{\alpha} \tag{22}$$

 $\alpha \in [0, 1]$ ; see [3].

## **Measures of Dependence**

Measures of dependence summarize the dependence structures of rv's. There are three important concepts: linear correlation, rank correlation, and tail dependence. A further concept of dependence is association; see [6, 17].

#### Linear Correlation

Linear correlation is a well-studied concept. It is a dependence measure, which is useful only for elliptical distributions (see Multivariate Distribu**tions**). This is because elliptical distributions are fully described by mean vector, covariance matrix, and a characteristic generator function. As mean and variances are determined by the marginal distributions, the copulas of elliptical distributions depend only on the covariance matrix and the generator function. Linear correlation, therefore, has a distinguished role in this class, which it does not have in other multivariate models.

#### Rank Correlation

Rank correlations describe the dependence structure of the ranks, that is, the dependence structure of the considered ry's when transformed to uniform marginals using the probability transformation. Most importantly, this implies a direct representation in terms of the underlying copula; compare equation  $(5)$ . We consider Kendall's tau and Spearman's rho, which also play an important role in nonparametric statistics.

For rv's  $\mathbf{X} = X_1, \ldots, X_d$  with marginals  $F_i, i =$  $1, \ldots, d$ , *Spearman's rho* is defined by

$$\rho_S(\mathbf{X}) := \text{Corr}\left(F_1(X_1), \dots, F_d(X_d)\right) \tag{23}$$

Corr is the correlation matrix whose entries are given by  $\text{Corr}(F_i(X_i), F_i(X_i)).$ 

Consider an independent copy  $\tilde{\mathbf{X}}$  of  $\mathbf{X}$ . Then *Kendall's tau* is defined by

$$\rho_{\tau}(\mathbf{X}) := \text{Cov}\left[\text{sign}\left(\mathbf{X} - \tilde{\mathbf{X}}\right)\right] \tag{24}$$

For  $d = 2$ .

$$\rho_{\tau}(X_1, X_2) = P\left( (X_1 - \tilde{X}_1) \cdot (X_2 - \tilde{X}_2) > 0 \right)$$
$$-P\left( (X_1 - \tilde{X}_1) \cdot (X_2 - \tilde{X}_2) < 0 \right)$$
(25)

which explains this measure of dependency.

Both measures have values in  $[-1, 1]$ ; they are 0 for independent variables (while there might also be nonindependent rv's with zero rank correlation) and they equal  $1 (-1)$  for the comonotonic (countermonotonic) case. Moreover, they can directly be derived from the copula of  $X$ ; see [14], Proposition 5.29. For example,

$$\rho_S(X_1, X_2) = 12 \int_0^1 \int_0^1 \left( C(u_1, u_2) - u_1 u_2 \right) \, \mathrm{d}u_1 \, \mathrm{d}u_2 \tag{26}$$

In the case of a bivariate Gaussian copula one obtains<sup>h</sup>  $\rho_S(X_1, X_2) = \frac{6}{\pi} \arcsin \frac{\rho}{2}$  and a similar expression for  $\rho_{\tau}$ .

For other examples and certain bounds that interrelate those two measures, we refer the reader to [18], Sections  $5.1.1-5.1.3$ . For multivariate extensions see, for example, [21] and [23].

#### Tail Dependence

We distinguish between *upper* and *lower* tail dependence. Consider two rv's  $X_1$  and  $X_2$  with marginals  $F_1, F_2$  and copula C. Upper tail dependence means intuitively that with large values of  $X_1$  also large values of  $X_2$  are expected. More precisely, the *coefficient* of upper tail dependence is defined by

$$\lambda_u := \lim_{q \nearrow 1} P\left(X_2 > F_2^{-1}(q) \middle| X_1 > F_1^{-1}(q)\right) \tag{27}$$

provided the limit exists and  $\lambda_u \in [0, 1]$ . The *coeffi*cient of lower tail dependence is

$$\lambda_{l} := \lim_{q \searrow 0} P\left(X_{2} \leq F_{2}^{-1}(q) \middle| X_{1} \leq F_{1}^{-1}(q)\right) \quad (28)$$

If  $\lambda_u > 0$ ,  $X_1$  and  $X_2$  are called *upper tail dependent*, while for  $\lambda_u = 0$  they are asymptotically independent in the upper tail; this applies analogously for  $\lambda_l$ . For continuous cdf's, Bayes' rule gives

$$\lambda_l = \lim_{q \searrow 0} \frac{C(q, q)}{q} \tag{29}$$

and

$$\lambda_u = 2 + \lim_{q \searrow 0} \frac{C(1-q, 1-q) - 1}{q} \tag{30}$$

A Gaussian copula has no tail dependence if the correlation is not equal to 1 or  $-1$ . For the bivariate *t*-distribution

$$\lambda_l = \lambda_u = 2t_{\nu+1} \left( -\sqrt{\frac{(\nu+1)(1-\rho)}{1+\rho}} \right) \tag{31}$$

provided  $\rho > -1$ . Note that even for zero correlation this copula shows tail dependence.

Tail dependence is a key quantity for joint quantile exceedances; see Example 5.34 in [14]: a multivariate Gaussian distribution will give a much smaller probability to the event that all returns from a portfolio are below the 1% quantiles of their respective distributions than a multivariate  $t$ -distribution. This is because of the difference in the tail dependence.

#### Association

A relatively stronger concept than correlation is the so-called association introduced in [6]. If  $Cov(X, Y) > 0$ , then one would consider X and Y as somehow associated. If, moreover,  $Cov(f(X))$ ,  $g(Y) \ge 0$  for all pairs of nondecreasing functions  $f, g$ , they would be considered more strongly associated. If  $Cov(f(X, Y), g(X, Y)) > 0$  for all pairs of functions  $f, g$  which are nondecreasing in each argument, an even stronger dependence holds. Random variables  $X_1, \ldots, X_d =: \mathbf{X}$  are called *associated* if  $\text{Cov}(f(\mathbf{X}), g(\mathbf{X})) \ge 0$  for all  $f, g$  that are nondecreasing and the covariance exists. Examples of associated rv's include independent rv's, positively correlated normal variables, and also the generalized exponential distribution turning up in the Marshall-Olkin copula.

### Sampling from Copulas

Consider given marginals  $F_1, \ldots, F_d$  and a given copula C. The first step is to simulate  $(U_1, \ldots, U_d)$ with uniform marginals and copula  $C$ . By equation (3), the vector  $(F_1^{-1}(U_1), \ldots, F_d^{-1}(U_d))$  has copula  $C$  and the desired marginals.

If the copula is inherited from a multivariate distribution, the task reduces to simulating this multivariate distribution, for example, Gaussian or  $t$ -distribution.

If the copula is Archimedean, this task is more demanding and we refer the reader to [14], Algorithm 5.48 for details.

#### Conclusion

On one hand, copulas are a very general tool to describe dependence structures and have been successfully applied in many cases. However, the immense generality is also a drawback in many applications and also the static characteristic of this measure of dependence has been criticized; see the referenced literature. Obviously, the application of copulas has been a great success to a number of fields, and they are a frequently used concept especially in finance. They serve as an excellent tool for calibrating dependence structures or stress testing portfolios or other products in finance and insurance as they allow to interpolate between extreme cases of dependence.

# **Literature**

The literature on copulas is growing fast. The vital article on copulas **Copulas in Insurance** by P. Embrechts gives an excellent overview of the literature and applications. An introduction to copulas that extends this note in many ways may be found in [20]. For a detailed exposition of copulas with different applications in view, we refer the reader to [4, 14, 19]. Reference [2] gives additional examples and [13] analyzes extreme financial risks. Estimation of copulas is discussed in [14], Section 5.5, [1] and [10]. For an in-depth study of copulas consider [11, 18]. Interesting remarks of the history and the development of copulas may be found in [7]. For more details on Marshall–Olkin copulas, in particular the multivariate ones, see [4, 18]. In the modeling of Levy ´ processes (*see* **Levy Processes ´** ) one considers dependency of jumps where the measure is no longer a probability measure. This leads to the development of so-called Levy copulas; compare [12] and ´ **Levy ´ Copulas**. The pitfalls mentioned with linear correlation are discussed in detail in [5] or [14 Chapter 5.2.1]. For a discussion on the general difficulties in the application of copulas, we refer the reader to [9, 16].

## **End Notes**

a*.* Although standard, it is not necessary to consider uniform marginals (*see* **Copulas in Insurance**).

b*.* One example is the exponential distributions whose multivariate extension leads to the Marshall–Olkin copula, introduced in the following paragraph.

c*.* See, for example [14], Proposition 5.2.

d*.* See [14], Example 5.21, for a counterexample.

e*.* For a rv *X* with continuous cdf *F*, the rv *F (X)* is standard uniform, see Section 1.

f*.* See **Correlation Risk**.

g*.* For generating the Clayton copula, it would be sufficient to use *(u*<sup>−</sup>*<sup>θ</sup>* − 1*)* instead of *θ*<sup>−</sup><sup>1</sup>*(u*<sup>−</sup>*<sup>θ</sup>* − 1*)* as generator. However, for *θ <* 0, this function is increasing and the above result would not be applicable.

h*.* Compare [14], Theorem 5.36. *ρS* and *ρτ* for elliptic distributions are also covered.

## **Acknowledgments**

The author thanks F. Durante and R. Frey for helpful comments.

## **References**

- [1] Charpentier, A., Fermanian, J.-D. & Scaillet, O. (2007). The estimation of copulas: from theory to practice, in *Copulas: From Theory to Applications in Finance*, J. Rank, ed, Risk Books, pp. 35–60.
- [2] Cherubini, U., Luciano, E. & Vecchiato, W. (2004). *Copula Methods in Finance*, Wiley, Chichester.
- [3] Cuadras, C.M. & Augee, J. (1981). A continuous general ´ multivariate distribution and its properties, *Communications in Statistics: Theory and Methods* **10**, 339–353.
- [4] Embrechts, P. Lindskog, F. & McNeil, A.J. (2003). Modeling dependence with copulas and applications to risk management, in *Handbook of Heavy Tailed Distributions in Finance*, S.T. Rachev, ed, Elsevier, pp. 331–385.
- [5] Embrechts, P., McNeil, A.J. & Straumann, D. (2001). Correlation and dependency in risk management: properties and pitfalls, in *Risk Management: Value at Risk and Beyond*, M. Dempster & H.K. Moffatt, eds, Cambridge University Press, pp. 176–223.
- [6] Esary, J.D., Proschan, F. & Walkup, D.W. (1967). Association of random variables, with applications, *Annals of Mathematical Statistics* **28**, 1466–1474.
- [7] Fisher, N.I. (1995). Copulas, in *Encyclopedia of Statistical Sciences*, S. Kotz, C. Read, N. Balakrishnan, & B. Vidakovic, eds, Wiley, pp. 159–163.
- [8] Genest, C. & Neslehov ˇ a, J. (2007). A primer on copulas ´ for count data, *Astin Bulletin* **37**, 475–515.
- [9] Genest, C. & Remillard, B. (2006). Diskussion of "cop- ´ ulas: tales and facts", by Thomas Mikosch, *Extremes* **9**, 27–36.
- [10] Genest, C., Remillard, B. & Beaudoin, D. (2007). ´ Goodness-of-fit tests for copulas: A review and a power study, *Insurance: Mathematics and Economics* in press, http://dx.doi.org/10.1016/j.insmatheco.2007.10.005.
- [11] Joe, H. (1997). *Multivariate Models and Dependence Concepts*, Chapman & Hall, London.
- [12] Kallsen, J. & Tankov, P. (2006). Characterization of dependence of multidimensional Levy processes using ´ Levy copulas, ´ *Journal of Multivariate Analysis* **97**, 1551–1572.
- [13] Malevergne, Y. & Sornette, D. (2006). *Extreme Financial Risks*, Springer Verlag, Berlin.
- [14] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management: Concepts, Techniques and Tools*, Princeton University Press.
- [15] McNeil, A.J. & Neslehov ˇ a, J. (2008). Multivariate ´ Archimedean copulas, *d*-monotone functions and *l*1 norm symmetric distributions, *Annals of Statistics*, forthcoming.
- [16] Mikosch, T. (2006). Copulas: tales and facts, *Extremes* **9**, 3–20.
- [17] Muller, A. & Stoyan, D. (2002). ¨ *Comparison Methods for Stochastic Models and Risk*, John Wiley & Sons, New York.

## **8 Copulas: Estimation**

- [18] Nelsen, R.B. (1999). *An Introduction to Copulas*, *Lecture Notes in Statistics*, Springer Verlag, Berlin, Vol. 139.
- [19] Rank, J. (ed) (2007). *Copulas: from Theory to Applications in Finance*, Risk Books.
- [21] Schmidt, T. (2007). Coping with copulas, in *Copulas: From Theory to Applications in Finance*, J. Rank, ed, Risk Books, pp. 1–31.
- [20] Schmidt, F. & Schmidt, R. (2007). Multivariate conditional versions of Spearmans' rho, *Journal of Multivariate Analysis* **98**, 1123–1140.
- [22] Sklar, A. (1959). Fonctions de repartition ´ a` *n* dimensions e leurs marges, *Publications de l'Institut de Statistique de l'Univiversit´e de Paris* **8**, 229–231.

[23] Taylor, M.D. (2007). Multivariate measures of concordance, *Annals of the Institute of Statistical Mechanics* **59**, 789–806.

## **Related Articles**

**Copulas in Econometrics**; **Copulas in Insurance**; **Correlation Risk**; **Levy Copulas ´** ; **Operational Risk**; **Risk Exposures**.

THORSTEN SCHMIDT
# **Multivariate Distributions**

Financial risk models, whether for market or credit risks, are inherently multivariate. For instance, the value change of a portfolio of traded instruments over a fixed time horizon depends on a random vector of risk-factor changes or returns; similarly, the loss incurred by a credit portfolio depends on a random vector of losses for the individual counterparties in the portfolio. In this article, we review some multivariate distributions (models for the distribution of random vectors) that are particularly useful for financial data. Our discussion is based mainly on Chapter 3 of [5]; the closely related issue of copulas and dependence measurement is discussed in Copulas: Estimation.

### **Random Vectors and Their Distributions**

In this section, we briefly review some key notions from multivariate statistics.

### Joint and Marginal Distributions

Consider a general  $d$ -dimensional random vector (think of risk-factor changes or log-returns)  $X =$  $(X_1,\ldots,X_d)'$ . The dependence between the components of  $\mathbf{X}$  is completely described by the *joint*  $distribution$  (df)

$$F_{\mathbf{X}}(\mathbf{x}) = F_{\mathbf{X}}(x_1, \dots, x_d) = P\left(\mathbf{X} \le \mathbf{x}\right)$$
$$= P\left(X_1 \le x_1, \dots, X_d \le x_d\right) \tag{1}$$

The *marginal* distribution function of  $X_i$ , written as  $F_{X_i}$  or often simply as  $F_i$ , is the df of that risk factor considered individually and is easily calculated from the joint df via

$$F_i(x_i) = P(X_i \le x_i)$$
  
=  $F(\infty, \dots, \infty, x_i, \infty, \dots, \infty)$  (2)

where the last expression is understood as the limit, as the respective arguments tend to the upper boundaries of the support of the distribution. If the marginal df  $F_i(x)$  is absolutely continuous, then we refer to its derivative  $f_i(x)$  as the *marginal density* of  $X_i$ . The

df of a random vector  $\mathbf{X}$  is said to be *absolutely* continuous if

$$F(x_1,\ldots,x_d)$$
  
=  $\int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_d} f(u_1,\ldots,u_d) \, \mathrm{d}u_1 \ldots \, \mathrm{d}u_d$  (3)

for some nonnegative function  $f$  integrating to one, known as the *joint density* of  $\mathbf{X}$ .

#### Conditional Distributions and Independence

If we have a multivariate model for risks in the form of a joint df or density, we can make conditional probability statements about the probability that certain components take certain values given that other components take other values. More precisely, partition **X** into  $(\mathbf{X}'_1, \mathbf{X}'_2)'$ , where  $\mathbf{X}_1 = (X_1, \ldots, X_k)'$ and  $\mathbf{X}_2 = (X_{k+1}, \ldots, X_d)'$ . Assume that **X** is absolutely continuous with density  $f$  and denote by  $f_{\mathbf{X}_1}(\mathbf{x}_1) = \int f(\mathbf{x}_1, \mathbf{x}_2) \, \mathrm{d}\mathbf{x}_2$  the density of  $\mathbf{x}_1$ . Then the conditional distribution of  $\mathbf{X}_2$  given  $\mathbf{X}_1 = \mathbf{x}_1$  has density

$$f_{\mathbf{X}_2|\mathbf{X}_1}(\mathbf{x}_2 \mid \mathbf{x}_1) = \frac{f(\mathbf{x}_1, \mathbf{x}_2)}{f_{\mathbf{X}_1}(\mathbf{x}_1)} \tag{4}$$

The components of  $X$  are called *mutually independent*, if and only if  $F(\mathbf{x}) = \prod_{i=1}^{d} F_i(x_i)$  for all  $\mathbf{x} \in \mathbb{R}^d$ or, in the case where **X** possesses a density,  $f(\mathbf{x}) =$  $\prod_{i=1}^d f_i(x_i).$ 

### Moments and Characteristic Function

The *mean vector* of  $\mathbf{X}$ , when it exists, is given by  $E(\mathbf{X}) := (E(X_1), \dots, E(X_d))'$ ; the *covariance matrix*, when it exists, is the matrix  $\Sigma = \text{cov}(\mathbf{X})$ with  $(i, j)$ th element given by  $\sigma_{ij} = \text{cov}(X_i, X_j) =$  $E(X_iX_j) - E(X_i)E(X_j)$ , the ordinary pairwise covariance between  $X_i$  and  $X_j$ . The diagonal elements  $\sigma_{11}, \ldots, \sigma_{dd}$  are the variances of the components of  $X$ . Mean vectors and covariance matrices are extremely, easily manipulated under linear operations on the vector **X**. For any matrix  $B \in \mathbb{R}^{k \times d}$  and vector  $\mathbf{b} \in \mathbb{R}^k$ , we have

$$E(B\mathbf{X} + \mathbf{b}) = BE(\mathbf{X}) + \mathbf{b} \tag{5}$$

$$cov(B\mathbf{X} + \mathbf{b}) = B \, cov(\mathbf{X})B' \tag{6}$$

Covariance matrices are symmetric and positive semidefinite. In case that  $\Sigma$  is positive definite  $(\mathbf{a}'\Sigma\mathbf{a}>0 \text{ for any } \mathbf{a}\in\mathbb{R}^d\setminus\{0\}), \text{ we can use the well-}$ known Cholesky factorization  $\Sigma = AA'$  for a lower triangular matrix  $A$  with positive diagonal elements known as the *Cholesky factor*; this decomposition is very useful for simulation purposes.

An important tool for studying multivariate distributions is the *characteristic function* of a random vector (or its distribution), given by

$$\phi_{\mathbf{X}}(\mathbf{t}) = E\left(\mathbf{e}^{it'\mathbf{X}}\right), \quad \mathbf{t} \in \mathbb{R}^d \tag{7}$$

### The Multivariate Normal Distribution

The multivariate normal distribution is central to much of classical multivariate analysis and provided the starting point for attempts to model market risk via the variance-covariance method (see Market **Risk** or Chapter 2 of  $[5]$ ); moreover, it is an important building block for constructing more refined distributions.

#### Definition and Basic Properties

A random vector  $\mathbf{X} = (X_1, \dots, X_d)'$  has a *multivari*ate normal or Gaussian distribution if

$$\mathbf{X} \stackrel{\text{d}}{=} \boldsymbol{\mu} + A\mathbf{Z} \tag{8}$$

where  $\mathbf{Z} = (Z_1, \ldots, Z_k)'$  is a vector of independent and identically distributed (iid) univariate standard normal random variables (rvs) (mean zero and variance one), and  $A \in \mathbb{R}^{d \times k}$  and  $\boldsymbol{\mu} \in \mathbb{R}^{d}$  are the matrix and vector of constants, respectively. It is easy to verify, using equations  $(5)$  and  $(6)$ , that the mean vector of this distribution is  $E(\mathbf{X}) = \boldsymbol{\mu}$  and the covariance matrix is  $cov(\mathbf{X}) = \Sigma$ , where  $\Sigma = AA'$  is a positive semidefinite matrix. Moreover, using the fact that the characteristic function of a standard univariate normal variate Z is  $\phi_Z(t) = \exp(-t^2/2)$ , the characteristic function of  $\mathbf{X}$  may be calculated to be

$$\phi_{\mathbf{X}}(\mathbf{t}) = E\left(\mathbf{e}^{i\mathbf{t}'\mathbf{X}}\right) = \exp\left(i\mathbf{t}'\boldsymbol{\mu} - \frac{1}{2}\mathbf{t}'\boldsymbol{\Sigma}\mathbf{t}\right), \quad \mathbf{t} \in \mathbb{R}^d$$
(9)

Clearly, the distribution is characterized by its mean vector and covariance matrix, and hence a standard notation is  $\mathbf{X} \sim N_d(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ . Note that the components of **X** are mutually independent if and only if  $\Sigma$  is diagonal. For example,  $\mathbf{X} \sim N_d(\mathbf{0}, I_d)$  if and only if  $X_1, \ldots, X_d$  are iid  $N(0, 1)$ , the standard univariate normal distribution.

We concentrate on the *nonsingular case* of the multivariate normal when rank $(A) = d \leq k$ . In this case, the covariance matrix  $\Sigma$  has full rank d and is therefore invertible (nonsingular) and positive definite. Moreover,  $\mathbf{X}$  has an absolutely continuous distribution function with joint density given by

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{\frac{d}{2}} |\Sigma|^{\frac{1}{2}}} \times \exp\left\{-\frac{(\mathbf{x} - \boldsymbol{\mu})' \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu})}{2}\right\}, \quad \mathbf{x} \in \mathbb{R}^d$$
(10)

where  $|\Sigma|$  denotes the determinant of  $\Sigma$ . In the singular case, the support of the distribution of  $X$ is a strict subspace of  $\mathbb{R}^d$  and a joint density does not exist. The form of the density clearly shows that points with equal density lie on ellipsoids determined by equations of the form  $(\mathbf{x} - \boldsymbol{\mu})' \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu}) = c$ , for constants  $c > 0$ .

In order to generate a realization  $\mathbf{X} \sim N_d(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with  $\Sigma$  positive definite, one would proceed as follows:

- 1. Perform a Cholesky decomposition  $\Sigma = AA'$  of the covariance matrix  $\Sigma$  (see, e.g., [6]).
- 2. Generate a vector  $\mathbf{Z} = (Z_1, \ldots, Z_d)'$  of independent standard normal variates and set  $X =$  $\mu + AZ$ .

We now summarize further useful properties of the multivariate normal that underline the attractiveness of this distribution for computational work in risk management. Linear combinations of multivariate normal random vectors are multivariate normal; if  $\mathbf{X} \sim N_d(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ , we have for any  $B \in \mathbb{R}^{k \times d}$  and  $\mathbf{b} \in$  $\mathbb{R}^k$  that

$$B\mathbf{X} + \mathbf{b} \sim N_k(B\boldsymbol{\mu} + b, B\Sigma B') \tag{11}$$

As a special case, if  $\mathbf{a} \in \mathbb{R}^d$ , then  $\mathbf{a}'\mathbf{X} \sim N(\mathbf{a}'\boldsymbol{\mu})$ ,  $\mathbf{a}'\Sigma\mathbf{a}$ ), and this fact is used routinely in the variance-covariance approach to risk management. Similarly, marginal distributions of a multivariate normal random vector are univariate normal.

Assuming  $\Sigma$  is positive definite, the *conditional* distributions of  $X_2$  given  $X_1$  and of  $X_1$  given  $X_2$ may also be shown to be multivariate normal. For example,  $\mathbf{X}_2 \mid \mathbf{X}_1 = \mathbf{x}_1 \sim N_{d-k}(\boldsymbol{\mu}_{2.1}, \boldsymbol{\Sigma}_{22.1})$  where

$$\boldsymbol{\mu}_{2.1} = \boldsymbol{\mu}_2 + \Sigma_{21} \Sigma_{11}^{-1} (\mathbf{x}_1 - \boldsymbol{\mu}_1)$$
 and  
 $\Sigma_{22.1} = \Sigma_{22} - \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}$  (12)

are the conditional mean vector and covariance matrix.

## Multivariate Normal Distributions as Model for Asset Returns

There are numerous empirical tests of the suitability of the multivariate normal distribution as a model for log-returns (risk-factor changes) for financial data. These tests involve both testing the hypothesis that marginal log-returns are normal (univariate tests) and tests for multivariate normality; details and further references can, for instance, be found in Section  $3.1.4 \text{ of } [3]$ . Broadly speaking, the outcome of these tests points to three main defects of the multivariate normal distribution (at least for data over a shorter time horizon such as daily or even monthly data):

- 1. The tails of its univariate marginal distributions are too thin; they do not assign enough weight to *extreme* events.
- The joint tails of the distribution do not assign 2. enough weight to *joint extreme* outcomes.
- The distribution has a strong form of symmetry 3. known as *elliptical symmetry*.

In the next section, we look at models that address some of these defects

# Variance Mixtures and Elliptical Distributions

### Normal Mixture Distributions

The random vector  $\mathbf{X}$  is said to have a *multivariate* normal variance mixture distribution if

$$\mathbf{X} \stackrel{\text{d}}{=} \boldsymbol{\mu} + \sqrt{W} A \mathbf{Z} \quad \text{where} \tag{13}$$

 $\mathbf{Z} \sim N_k(\mathbf{0}, I_k); A \in \mathbb{R}^{d \times k}$  and  $\boldsymbol{\mu} \in \mathbb{R}^d$  are a matrix, respectively, a vector of constants; and where  $W \ge 0$  is a nonnegative, scalar-valued rv, which is independent of  $\mathbf{Z}$ . Such distributions are known as variance mixtures, since  $\mathbf{X} \mid W = w \sim N_d(\mu, w\Sigma)$ where  $\Sigma = AA'$ . The distribution of **X** can be considered as a composite distribution, constructed by taking a set of multivariate normal distributions with the same mean vector and with the same covariance matrix up to a multiplicative constant  $w$ ; the mixture distribution—which is generally not a normal distribution—is then constructed by drawing randomly from this set of component multivariate normals according to a set of "weights" determined by the distribution of  $W$ .

Provided  $W$  has a finite expectation, we may easily calculate that  $E(\mathbf{X}) = \boldsymbol{\mu}$  and that  $cov(\mathbf{X}) =$  $E(W) \Sigma$ . Note that normal variance mixtures provide nice examples of models where a lack of correlation does not necessarily imply independence of the components of  $\mathbf{X}$ ; indeed, it can be shown that two uncorrelated rvs  $(X_1, X_2)$  having a normal mixture distribution with  $E(W) < \infty$  are independent, if and only if  $W$  is almost surely constant, that is, if  $(X_1, X_2)$  are bivariate normally distributed.

The characteristic function of a multivariate normal variance mixture is given by

$$\phi_{\mathbf{X}}(\mathbf{t}) = \exp\left(i\mathbf{t}'\boldsymbol{\mu}\right)\widehat{H}\left(\mathbf{t}'\boldsymbol{\Sigma}\mathbf{t}/2\right) \tag{14}$$

where  $\widehat{H}(\theta) = \int_0^\infty e^{-\theta v} \, \mathrm{d}H(v)$  is the Laplace-Stieltjes transform of the df  $H$  of  $W$ . We use the notation  $\mathbf{X} \sim M_d(\boldsymbol{\mu}, \boldsymbol{\Sigma}, \hat{H})$  for normal variance mixtures. Assuming that  $\Sigma$  is positive definite and that the distribution of  $W$  places no point mass at zero, the density of  $\mathbf{X} \sim M_d(\boldsymbol{\mu}, \Sigma, \widehat{H})$  becomes

$$f(\mathbf{x}) = \int \frac{w^{-\frac{d}{2}}}{(2\pi)^{\frac{d}{2}} |\Sigma|^{\frac{1}{2}}} \times \exp\left\{-\frac{(\mathbf{x} - \boldsymbol{\mu})'\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})}{2w}\right\} dH(w) \tag{15}$$

Note that all such densities depend on  $\mathbf{x}$  only through the quadratic form  $(\mathbf{x} - \boldsymbol{\mu})' \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu}).$ 

The most important example is provided by the *multivariate t-distribution*. Here, we take  $W$  in equation  $(13)$  to be a rv with an inverse gamma distribution  $W \sim \text{Ig}(\nu/2, \nu/2)$  (which is equivalent to saying that  $\nu/W \sim \chi^2_{\nu}$ ). The notation for this distribution is  $\mathbf{X} \sim t_d(\nu, \boldsymbol{\mu}, \boldsymbol{\Sigma})$ . Since  $E(W) = \nu/(\nu - 2)$ , we have  $\text{cov}(\mathbf{X}) = \frac{\nu}{\nu - 2} \boldsymbol{\Sigma}$  and the covariance matrix of this distribution is only defined if  $\nu > 2$ . Using equation  $(15)$ , the density can be calculated to be

$$f(\mathbf{x}) = \frac{\Gamma\left(\frac{\nu+d}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)(\pi\nu)^{\frac{d}{2}}|\Sigma|^{\frac{1}{2}}} \times \left(1 + \frac{(\mathbf{x} - \boldsymbol{\mu})'\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})}{\nu}\right)^{-\frac{\nu+d}{2}} \tag{16}$$

The multivariate  $t$  has heavier marginal tails than the normal distribution and a more pronounced tendency to generate simultaneous extreme outcomes (*see also* Copulas: Estimation).

Normal variance mixture distributions are easy to work with under linear operations; if  $\mathbf{X} \sim M_d(\boldsymbol{\mu})$ ,  $\Sigma, \widehat{H}$  and  $\mathbf{Y} = B\mathbf{X} + \mathbf{b}$  where  $B \in \mathbb{R}^{k \times d}$  and  $\mathbf{b} \in$  $\mathbb{R}^k$ , then  $\mathbf{Y} \sim M_k(B\boldsymbol{\mu} + \mathbf{b}, B\Sigma B', \widehat{H})$ . Thus, linear transformations of  $X$  remain in the subclass of mixture distributions specified by  $\widehat{H}$  or, equivalently, by the mixing variable W of which  $\widehat{H}$  is the Laplace-Stieltjes transform. For example, if  $X$  has a multivariate *t* distribution with  $\nu$  degrees of freedom, then so does any linear transformation of  $X$ .

### *Normal Mean–variance Mixture Distributions*

The definition  $(13)$  can be generalized to allow for skewed distributions:  $\mathbf{X}$  is said to have a multivariate normal mean-variance mixture distribution if

$$\mathbf{X} \stackrel{\text{d}}{=} \boldsymbol{\mu} + W\boldsymbol{\gamma} + \sqrt{W}A\mathbf{Z} \tag{17}$$

For instance, if we assume  $W \sim N^-(\lambda, \chi, \psi)$  (a generalized inverse Gaussian distribution), we obtain the class of (multivariate) generalized hyperbolic distributions (see Generalized Hyperbolic Models). These distributions have important applications in finance and risk management; in particular, they are infinitely divisible and therefore directly connected to Lévy processes (see Lévy Processes). Note that mean-variance mixture distributions are, in general, skewed; in particular, the density is no longer constant on ellipsoids. We refer to Section  $3.2.4$  of [5] for further information and further references about this class.

#### Spherical and Elliptical Distributions

Many important distribution have densities that are constant on ellipsoids and thus belong to the class of elliptical distributions; this class has some theoretical properties that makes it attractive as a model for the joint distribution of risk factors. Elliptical distributions are defined as affine transformations of *spherical* random vectors. A random vector  $\mathbf{X} =$  $(X_1,\ldots,X_d)'$  has a spherical distribution, if, for every orthogonal map  $U \in \mathbb{R}^{d \times d}$  (i.e., maps satisfying  $UU' = U'U = I$ ), one has  $UX \stackrel{\text{d}}{=} X$ . Spherical random vectors are thus distributionally invariant under rotations. It can be shown that  $X$  is spherical if and only if one of the following properties hold:

1. There exists a function  $\psi$  of a scalar variable, called *characteristic generator*, such that, for all  $\mathbf{t} \in \mathbb{R}^d$ .

$$\phi_{\mathbf{X}}(\mathbf{t}) = E\left(\mathbf{e}^{i\mathbf{t}^{\prime}\mathbf{X}}\right) = \psi\left(\mathbf{t}^{2}_{1} + \dots + t^{2}_{d}\right)$$
(18)

2. For every  $\mathbf{a} \in \mathbb{R}^d$ , one has  $\mathbf{a}'\mathbf{X} \stackrel{\text{d}}{=} ||\mathbf{a}||X_1$ , where  $||\mathbf{a}||^2 = \mathbf{a}'\mathbf{a} = a_1^2 + \dots + a_d^2.$  $\mathbf{X}$  has an *elliptical distribution* if

$$\mathbf{X} \stackrel{\text{d}}{=} \boldsymbol{\mu} + A\mathbf{Y} \tag{19}$$

where **Y** is spherical and  $A \in \mathbb{R}^{d \times k}$  and  $\boldsymbol{\mu} \in \mathbb{R}^{d}$ are a matrix and vector of constants, respectively. The characteristic function can be written as  $\phi_{\mathbf{X}}(\mathbf{t}) =$  $e^{it'\mu}\psi(t'\Sigma t)$ , where  $\psi(\cdot)$  is the characteristic generator of  $\mathbf{Y}$  introduced in equation (18). Examples include the multivariate normal distribution and, more generally, the multivariate variance mixture distributions (13). Elliptical distributions share many properties with the multivariate normal distribution: affine transformations of elliptical random vectors and, in particular, marginal distributions remain elliptical with the same generator  $\psi$ ; if we condition on one or several components of an elliptical random vector, the ensuing conditional distribution is elliptical, albeit, in general, with a different generator.

An important property of elliptical distributions for risk management purposes is the fact that Value at Risk (VaR) (see Value-at-Risk) is a coherent risk *measure* (see **Convex Risk Measures**) if restricted to the set of all linear combinations of the components of some elliptical random vector.

## **Notes and Further References**

Much of the material from the sections "Random Vectors and Their Distributions" and "The Multivariate Normal Distribution" can be found in greater detail in standard texts on multivariate statistical analysis such as [4, 7]. There are countless possible tests of univariate normality and a good starting point is the entry on *Departures from Normality, Tests for* in volume 2 of the Encyclopedia of Statistics [3]; the latter source also contains tests for multivariate normality.

A comprehensive reference for the spherical and elliptical distributions (including a special treatment of symmetric variance mixture models) is given by Fang *et al.* [2]. A useful reference on the multivariate generalized hyperbolic distribution is Blæsild [1].

## **References**

[1] Blæsild, P. (1981). The two-dimensional hyperbolic distribution and related distributions, with an application to Johannsen's bean data, *Biometrika* **68**(1), 251–263.

- [2] Fang, K.-T., Kotz, S. & Ng, K.-W. (1987). *Symmetric Multivariate and Related Distributions*, Chapman & Hall, London.
- [3] Kotz, S., Johnson, N. & Read, C. (eds) (1985). *Encyclopedia of Statistical Sciences*, Wiley, New York.
- [4] Mardia, K., Kent, J. & Bibby, J. (1979). *Multivariate Analysis*, Academic Press, London.
- [5] McNeil, A., Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management: Concepts, Techniques and Tools*, Princeton University Press, Princeton.
- [6] Press, W., Teukolsky, S., Vetterling, W. & Flannery, B. (1992). *Numerical Recipes in C*, Cambridge University Press, Cambridge.
- [7] Seber, G. (1984). *Multivariate Observations*, Wiley, New York.

## **Related Articles**

**Copulas: Estimation**; **Copulas in Econometrics**; **Correlation Risk**.

RUDIGER ¨ FREY
# **Random Matrix Theory**

Random matrix theory is the study of matrices with random entries. It has been applied in quantitative finance for the estimation of large covariance matrices which are of interest in portfolio optimization (see Modern Portfolio Theory; Risk-Return Analysis). This estimation problem is linked to understanding the properties of *large-dimensional random* matrices.

If daily returns on  $n$  days for  $p$  different assets are represented as an  $n \times p$  matrix X, the sample covariance matrix  $\widehat{\Sigma}$  is defined as

$$\widehat{\Sigma} = \frac{1}{n-1}(X - \bar{X})'(X - \bar{X}) \tag{1}$$

where X' is the transpose of X and  $\bar{X}$  is a  $(n \times p)$ matrix of means, that is, its  $k$ th column has constant value equal to the mean of the  $k$ th column of  $X$ . These matrices are important in practice because they are used to estimate from the data the (unknown) population covariance  $\Sigma$ , when the rows of X,  $\{X_i\}_{i=1}^n$ are assumed to be independent identically distributed (i.i.d.) *p*-dimensional vectors with covariance  $\Sigma$ . When that is the case,  $\widehat{\Sigma}$  is an unbiased estimator of  $\Sigma$ , that is,  $\mathbf{E}(\widehat{\Sigma}) = \Sigma$ .

In the Markowitz portfolio optimization problem (see Risk-Return Analysis), optimal weights for different assets are allocated according to a formula involving the covariance  $\Sigma$  of the assets. Since  $\Sigma$  is unknown, it is necessary to estimate it, and the sample covariance matrix is often used as an estimator. Note that for large portfolios,  $p$  will be quite large, of order 100 for instance. Also, if looking at daily returns, the number of days, n, used to compute  $\widehat{\Sigma}$  is often chosen not to exceed a year or two of trading, and is also therefore of order a few 100s (roughly 250 to 500). Hence, in financial practice, it will often be the case that both  $p$  and  $n$  are "large".

This is in contrast to the classical theory (see  $[1]$ ), which is concerned with asymptotics where  $p$  is held fixed and  $n$  goes to infinity. In this setting of "small  $p$ , large  $n$ ", the sample covariance matrix is known to be a good estimator of the population covariance. For instance, the sample eigenvalues can be shown to be close to the population eigenvalues, and similarly for corresponding eigenspaces. Practically, it means that using the sample covariance matrix in the solution of a Markowitz portfolio optimization problem with a few assets will work "well", if we observe the assets for a long enough time.

The "large  $p$ , large  $n$ " situation is very different and is the one that is studied in random matrix theory. Roughly speaking, what happens in that situation is that, under "reasonable" assumptions detailed later. the eigenvalues of  $\widehat{\Sigma}$  become inconsistent estimators of the eigenvalues of  $\Sigma$ . Similarly, problems develop with eigenvectors.

The first result in this area was obtained by Marčenko-Pastur [21]. A subcase of the result shown there can, for instance, be interpreted as saying that if the entries of X are i.i.d  $\mathcal{N}(0, 1)$ , the histogram of eigenvalues of  $\widehat{\Sigma}$  is asymptotically *nonrandom* (though the matrix itself is random) and moreover its shape can be described. The limiting density of eigenvalues is, if  $p/n \rightarrow r \in (0, 1)$ ,

$$f_r(x) = \frac{1}{2\pi r} \frac{\sqrt{(b-x)(x-a)}}{x} 1_{a \le x \le b} \qquad (2)$$

In the above equation,  $b = (1 + \sqrt{r})^2$  and  $a = (1 \sqrt{r}$ <sup>2</sup>. The probability distribution with corresponding density is often called the *Marčenko-Pastur* law. It is illustrated in Figure 1. (If  $r > 1$ , there is also a point mass of mass  $(1 - 1/r)$  at 0.)

Several general facts about eigenvalues of random matrices can be observed in Figure 1. First, the sample eigenvalues are more dispersed than the population eigenvalues. Second, the extreme eigenvalues exhibit bias: instead of converging to the population (or "true") extreme eigenvalues, which in the case above are concentrated at 1, the largest (respectively, smallest) sample eigenvalue is asymptotically at least as large as  $b = (1 + \sqrt{r})^2$  (respectively, as small as  $a = (1 - \sqrt{r})^2$ ). Under certain moment conditions on the entries of  $X$ , it can actually be shown that the extreme eigenvalues of  $\widehat{\Sigma}$  converge to b and a. We now turn to a more precise presentation of the results we have hinted at.

## **Eigenvalues of Sample Covariance** Matrices

Two types of results are available for eigenvalues of sample covariance matrices: results dealing with the behavior of the "bulk" of eigenvalues and "edge" results, which deal with extreme (maximal or minimal) eigenvalues.

![](_page_1_Figure_1.jpeg)

**Figure 1** Density of Marčenko-Pastur law and histogram of eigenvalues. Here the histogram of eigenvalues of  $X'X/n$  is plotted, for  $p = 200$ ,  $n = 500$ . The entries of X are i.i.d  $\mathcal{N}(0, 1)$ . Since  $\Sigma = \text{id}$ , the "true" (or population) eigenvalues are all equal to 1, illustrating the fact that the sample covariance matrix is not a good estimator of the population covariance when  $r \neq 0$ . The curve is the theoretical prediction obtained from the Marčenko–Pastur law

"Bulk" results deal with the empirical distribution of the eigenvalues and study the convergence properties of this (random) probability measure. If  $l_1 \ge l_2 \ge \ldots \ge l_p$  denote the decreasingly ordered eigenvalues of the  $p \times p$  matrix  $\hat{\Sigma}$ , we call  $F_p$  the spectral distribution of  $\Sigma$ ; by definition, we have

$$dF_p(x) = \frac{1}{p} \sum_{i=1}^p \delta_{l_i} dx \tag{3}$$

Here  $\delta_x$  denotes a Dirac mass (of mass 1) at x. Note that  $F_p$  is a probability measure. Also,  $F_p([x, \infty))$ is the proportion of eigenvalues of  $\widehat{\Sigma}$  that are larger than  $x$ .

To study  $F_p$  in random matrix theory, it is common to use the Stieltjes transform of a distribution. By definition, the Stieltjes transform of a distribution  $G$  is a complex-valued function of one complex variable with strictly positive imaginary part, defined  $\text{as}$ 

$$m_G(z) = \int \frac{\mathrm{d}G(x)}{x - z} \,, \text{ for } z \in \mathbb{C}^+$$
$$= \{ z \in \mathbb{C} \text{ with } \text{Im}[z] > 0 \} \tag{4}$$

We note that  $m_G$  maps  $\mathbb{C}^+$  into  $\mathbb{C}^+$ . The importance of Stieltjes transforms in this context comes from the fact that if  $F_p$  is a sequence of probability distributions and  $m_{F_n}(z)$  converges, for all z in  $\mathbb{C}^+$  to  $m_F(z)$ , where  $m_F(z)$  is in  $\mathbb{C}^+$ , and  $\lim_{y\to\infty} y m_F(iy) = -1$ , then  $F_p$  converges weakly to  $F$  (and therefore  $F$  is a probability distribution). For a thorough introduction to the connection between convergence of Stieltjes transforms and convergence of probability distributions, we refer the reader to [15].

An important result concerning eigenvalues of sample covariance matrices is the following result shown in [26], which generalizes results in [21] and  $[29]$ . We note that the functional equation we are about to state was found first in  $[21]$  and is sometimes called the Marčenko-Pastur equation.

**Theorem 1** (Silverstein [26]) Let Y be an  $n \times p$ matrix with i.i.d entries, denoted  $Y_{i,j}$ . Suppose that  $Y_{i,j}$  has two moments, that is,  $\mathbf{E}\left(Y_{i,j}^{2}\right) < \infty$ , and variance 1. Let  $\Sigma_{p}$  be the population covariance matrix. In particular,  $\Sigma_p$  is positive semidefinite. Suppose the spectral distribution of  $\Sigma_p$ ,  $H_p$ , has

a limit,  $H$ , in the sense of weak convergence of distributions.

Let the data matrix be represented by  $X = Y \Sigma_p^{1/2}$ . Call  $F_p$  the spectral distribution of  $X'X/n$  and  $m_p$ the Stieltjes transform of  $F_p$ . Call  $v_p(z) = -(1$  $p/n)/z + p/nm_p(z)$ . ( $v_p$  is the Stieltjes transform of the spectral distribution of the matrix  $XX'/p$ .)

When  $p/n \rightarrow r \neq 0$ ,  $F_p$  converges weakly almost surely (a.s.) to a deterministic (probability) distribution F. Moreover,  $\forall z \in \mathbb{C}^+, v_n(z) \rightarrow v(z)$  a.s., and

$$-\frac{1}{v(z)} = z - r \int \frac{\lambda dH(\lambda)}{1 + \lambda v(z)} \tag{5}$$

It can be shown that there is a unique solution to the previous equation which is a Stieltjes transform.

Some comments are in order here. First, equation (5) relates the properties of the limit of the empirical spectral distribution ("encoded" by its Stielties transform in  $v$ ) to those of the limiting population spectral distribution represented by  $H$ . Also, because finite rank perturbation of matrices does not affect limiting spectral distributions (see, for instance, [2]), the same result applies to the limiting spectral distribution of  $(X - \bar{X})'(X - \bar{X})/n$ , the sample covariance matrix used in practice. In other respects, the Marčenko-Pastur law can be obtained fairly simply from equation  $(5)$ , as explained in [21] for instance. Finally, robustness properties (and lack thereof) of this functional equation have recently been investigated in [8], highlighting, in particular, geometric limitations for the data, implicitly implied by the model used in Theorem 1.

#### Properties of Extreme Eigenvalues

Limiting spectral distribution properties do not in general imply anything about properties of extreme eigenvalues, beside the fact that extreme eigenvalues need to be at the edge (or outside) of the support of the limiting spectral distribution. However, properties of these extreme eigenvalues are important in statistics, in particular for techniques such as principal component analysis ( $PCA$ ; see [22]).

Results about extreme eigenvalues are available. An important one is for instance, when  $\Sigma_p = \text{Id}_p$ ; then the largest eigenvalue of  $X'X/n$  converges to  $(1+\sqrt{r})^2$ . The result was first obtained in [14], and under weaker assumptions in [30]. We cite the latter result.

**Theorem 2** (*Yin et al. [30]*) Suppose X is an  $n \times p$ data matrix, with i.i.d entries. Suppose that  $\mathbf{E}(X_{i,j}) =$  $0, \mathbf{E}\left(X_{i,j}^{2}\right) = 1 \text{ and } \mathbf{E}\left(X_{i,j}^{4}\right) < \infty. \text{ Suppose } p/n \to r \in (0, \infty), \text{ as } n \to \infty. \text{ Then, we have, if } l_{1}(X'X/n)$ denotes the largest eigenvalue of  $X'X/n$ ,

$$l_1\left(\frac{X'X}{n}\right) \to (1+\sqrt{r})^2 \tag{6}$$

As explained in  $[25]$ , the existence of the fourth moment is necessary for this result to hold. Similar convergence results exist concerning the smallest eigenvalue of  $\widehat{\Sigma}$  (see [3] and [2, p. 635]).

More recent theoretical work concerns fluctuation behavior of the largest eigenvalues of sample covariance matrices. Following mathematical breakthroughs in the 1990s (see [27]), it has become possible to describe the limiting distribution of  $l_1(X'X/n)$ . In particular, the papers [9, 13, 17, 18], show the following:

**Theorem 3** Suppose X is an  $n \times p$  matrix with i.i.d  $\mathcal{N}(0, 1)$  entries. Suppose n and p tend to infinity. Then

$$n^{2/3} \frac{l_1(X'X/n) - (1 + \sqrt{p/n})^2}{(1 + \sqrt{p/n})(1 + \sqrt{n/p})^{1/3}} \Longrightarrow \text{TW}_1 \quad (7)$$

The most important part of the result (the case  $p/n$ having a finite nonzero limit) is shown in [18]. In the previous theorem,  $TW_1$  is a Tracy-Widom distribution. Its density is known explicitly (see  $[28]$ and  $[18]$ ).

In all the previous examples,  $\Sigma_p = \text{Id}_p$ . The case of general  $\Sigma$  is starting to be understood, too, and is more relevant to techniques such as PCA. The situation where  $\Sigma$  has a few isolated "large" eigenvalues and all the other eigenvalues are equal is now reasonably well understood (see [5, 23]). In this case, the empirical largest eigenvalue is biased and the bias can be computed explicitly. The corresponding sample eigenvector does not converge to the population eigenvector associated with the isolated eigenvalue. The situation where  $\Sigma$  is truly general is more complicated. A formula for the limit of the largest eigenvalue in certain class of population covariance matrices is given in [12], along with a notion of isolation of eigenvalues. Let us finally note that as described in [4] in a slightly different context (and partially generalized in  $[5]$ ), if the population largest eigenvalue is not isolated (or large) enough, the largest empirical eigenvalue will asymptotically not be affected by its existence. In other words, in this situation, the existence of an isolated population eigenvalue is not detected by looking at the empirical largest eigenvalue, something that is potentially problematic in PCA.

## **Estimation of Covariance Matrices**

Because of the increased availability of larger dimensional datasets, and in part because of recent results in random matrix theory indicating that in high dimensions (i.e.,  $p$  large and of the same order of magnitude as  $n$ ) the sample covariance matrix is not a good estimator (or proxy) for the population covariance, there has been quite a bit of activity recently in statistics to try to come up with better estimators of population covariance.

The classic paper  $[16]$  (see also  $[1, Section 7.8]$ ) has shown that one could improve estimation of  $\Sigma$ (i.e., decrease the expected squared error of the corresponding estimator) by using linear combinations of  $\hat{\Sigma}$  and any positive semidefinite matrices. These methods are often called *shrinkage* methods in statistics. More recently, Ledoit and Wolf [20] showed they could improve estimation of  $\Sigma$  by shrinking  $\widehat{\Sigma}$  toward the identity. Their method amounts to adding a certain quantity to all eigenvalues of  $\widehat{\Sigma}$  and keeping the same eigenvectors to get a new estimator of  $\Sigma$ ,  $\hat{\Sigma}$ . Finally, the paper [19], in the context of Markowitz portfolio optimization, proposed to use random matrix results to also shrink the eigenvalues of  $\widehat{\Sigma}$ , this time in a nonlinear fashion; after noting the similarity between part of the histogram of eigenvalues of a sample correlation matrix computed from financial data and the density of the Marčenko-Pastur law, the authors of [19] proposed to leave unchanged the eigenvalues falling outside the Marčenko-Pastur-looking part of the histogram, and to change those falling within it to a common value. They showed that this method improved on their dataset the predictive performance of the efficient frontier they obtained when solving the Markowitz optimization problem with  $\Sigma$  replaced by their estimate.

Other nonlinear methods for nonlinear shrinking of eigenvalues using random matrix theory have been proposed (see [11, 24]). Improved estimation of covariance matrices is at the moment an active topic of research in statistics [6, 7, 10], and while it is not obvious that the results obtained there are immediately applicable in the financial context, some of the insights found in these papers might prove helpful in the future.

### References

- Anderson, T.W. (2003). An Introduction to Multivariate  $[1]$ Statistical Analysis, Wiley Series in Probability and Statistics, 3rd Edition, Wiley-Interscience, John Wiley & Sons, Hoboken, NJ.
- [2] Bai, Z.D. (1999). Methodologies in spectral analysis of large-dimensional random matrices, a review, Statistica Sinica  $9(3)$ ,  $611-677$ . With comments by G. J. Rodgers and Jack W. Silverstein; and a rejoinder by the author.
- Bai, Z.D. & Yin, Y.Q. (1993). Limit of the smallest [3] eigenvalue of a large-dimensional sample covariance matrix, Annals of Probability 21(3), 1275-1294.
- [4] Baik, J., Ben Arous, G. & Péché, S. (2005). Phase transition of the largest eigenvalue for non-null complex sample covariance matrices, Annals of Probability 33(5), 1643-1697.
- [5] Baik, J. & Silverstein, J. (2006). Eigenvalues of large sample covariance matrices of spiked population models, Journal of Multivariate Analysis 97(6), 1382-1408.
- [6] Bickel, P.J. & Levina, E. (2007). Covariance Regularization by Thresholding, Technical Report 744, Department of Statistics, UC Berkeley.
- [7] Bickel, P.J. & Levina, E. (2008). Regularized estimation of large covariance matrices, The Annals of Statistics 36(1), 199-227.
- [8] El Karoui, N. Concentration of measure and spectra of random matrices: with applications to correlation matrices, elliptical distributions and beyond, *The Annals* of Applied Probability To Appear.
- [9] El Karoui, N. (2003). On the largest eigenvalue of Wishart matrices with identity covariance when  $n$ ,  $p$  and  $p/n \rightarrow \infty$ . arXiv:math.ST/0309355, September 2003.
- [10] El Karoui, N. (2008). Operator norm consistent estimation of large dimensional sparse covariance matrices, The Annals of Statistics 36(6), 2717-2756.
- [11] El Karoui, N. (2008). Spectrum estimation for large dimensional covariance matrices using random matrix theory, The Annals of Statistics 36(6), 2757–2790.
- [12] El Karoui, N. (2007). Tracy-Widom limit for the largest eigenvalue of a large class of complex sample covariance matrices, The Annals of Probability 35(2), 663-714.
- [13] Forrester, P.J. (1993). The spectrum edge of random matrix ensembles, *Nuclear Physics B* **402**(3), 709–728.
- [14] Geman, S. (1980). A limit theorem for the norm of random matrices, Annals of Probability  $\mathbf{8}(2)$ , 252–261.
- [15] Geronimo, J.S. & Hill, T.P. (2003). Necessary and sufficient condition that the limit of Stieltjes transforms is a Stieltjes transform, *Journal of Approximation Theory* 121(1), 54-60.

- [16] Haff, L.R. (1980). Empirical Bayes estimation of the multivariate normal covariance matrix, *Annals of Statistics* **8**(3), 586–597.
- [17] Johansson, K. (2000). Shape fluctuations and random matrices, *Communications in Mathematical Physics* **209**(2), 437–476.
- [18] Johnstone, I. (2001). On the distribution of the largest eigenvalue in principal component analysis, *Annals of Statistics* **29**(2), 295–327.
- [19] Laloux, L., Cizeau, P., Bouchaud, J.-P. & Potters, M. (1999). Noise dressing of financial correlation matrices, *Physical Review Letters* **83**(7), 1467–1470.
- [20] Ledoit, O. & Wolf, M. (2004). A well-conditioned estimator for large-dimensional covariance matrices, *Journal of Multivariate Analysis* **88**(2), 365–411.
- [21] Marcenko, V.A. & Pastur, L.A. (1967). Distribution ˇ of eigenvalues in certain sets of random matrices, *Mathematics of the USSR-Sbornik* **72**(114), 507–536.
- [22] Mardia, K.V., Kent, J.T. & Bibby, J.M. (1979). *Multivariate Analysis*, *Probability and Mathematical Statistics: A Series of Monographs and Textbooks*, Academic Press [Harcourt Brace Jovanovich Publishers], London.
- [23] Paul, D. (2007). Asymptotics of sample eigenstructure for a large dimensional spiked covariance model, *Statistica Sinica* **17**(4), 1617–1642.

- [24] Rao, N.R., Mingo, J., Speicher, R. & Edelman, A. (2008). Statistical Eigen-Inference from Large Wishart Matrices, *The Annals of Statistics* **36**(6), 2850–2885.
- [25] Silverstein, J.W. (1989). On the weak limit of the largest eigenvalue of a large-dimensional sample covariance matrix, *Journal of Multivariate Analysis* **30**(2), 307–311.
- [26] Silverstein, J.W. (1995). Strong convergence of the empirical distribution of eigenvalues of largedimensional random matrices, *Journal of Multivariate Analysis* **55**(2), 331–339.
- [27] Tracy, C. & Widom, H. (1994). Level-spacing distribution and the Airy kernel, *Communications in Mathematical Physics* **159**, 151–174.
- [28] Tracy, C. & Widom, H. (1996). On orthogonal and symplectic matrix ensembles, *Communications in Mathematical Physics* **177**, 727–754.
- [29] Wachter, K.W. (1978). The strong limits of random matrix spectra for sample matrices of independent elements, *Annals of Probability* **6**(1), 1–18.
- [30] Yin, Y.Q., Bai, Z.D. & Krishnaiah, P.R. (1988). On the limit of the largest eigenvalue of the largedimensional sample covariance matrix, *Probability Theory and Related Fields* **78**(4), 509–521.

NOUREDDINE EL KAROUI
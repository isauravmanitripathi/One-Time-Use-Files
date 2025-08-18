This chapter develops methods for simulating paths of a variety of stochastic processes important in financial engineering. The emphasis in this chapter is on methods for *exact* simulation of continuous-time processes at a discrete set of dates. The methods are exact in the sense that the joint distribution of the simulated values coincides with the joint distribution of the continuoustime process on the simulation time grid. Exact methods rely on special features of a model and are generally available only for models that offer some tractability. More complex models must ordinarily be simulated through, e.g., discretization of stochastic differential equations, as discussed in Chapter 6.

The examples covered in this chapter are arranged roughly in increasing order of complexity. We begin with methods for simulating Brownian motion in one dimension or multiple dimensions and extend these to geometric Brownian motion. We then consider Gaussian interest rate models. Our first real break from Gaussian processes comes in Section 3.4, where we treat square-root diffusions. Section 3.5 considers processes with jumps as models of asset prices. Sections 3.6 and 3.7 treat substantially more complex models than the rest of the chapter; these are interest rate models that describe the term structure through a curve or vector of forward rates. Exact simulation of these models is generally infeasible; we have included them here because of their importance in financial engineering and because they illustrate some of the complexities of the use of simulation for derivatives pricing.

# 3.1 Brownian Motion

# 3.1.1 One Dimension

By a *standard* one-dimensional Brownian motion on  $[0, T]$ , we a mean a stochastic process  $\{W(t), 0 \le t \le T\}$  with the following properties:

$$\text{(i)} \quad W(0) = 0;$$

- 80 3 Generating Sample Paths
- the mapping  $t \mapsto W(t)$  is, with probability 1, a continuous function on (ii)  $[0,T]$
- (iii) the increments  $\{W(t_1) W(t_0), W(t_2) W(t_1), \ldots, W(t_k) W(t_{k-1})\}$ are independent for any  $k$  and any  $0 \le t_0 < t_1 < \cdots < t_k \le T$ ;
- (iv)  $W(t) W(s) \sim N(0, t s)$  for any  $0 \le s < t \le T$ .

In (iv) it would suffice to require that  $W(t) - W(s)$  have mean 0 and variance  $t-s$ ; that its distribution is in fact normal follows from the continuity of sample paths in (ii) and the independent increments property (iii). We include the condition of normality in (iv) because it is central to our discussion. A consequence of  $(i)$  and  $(iv)$  is that

$$W(t) \sim N(0, t), \tag{3.1}$$

for  $0 < t \leq T$ .

For constants  $\mu$  and  $\sigma > 0$ , we call a process  $X(t)$  a Brownian motion with drift  $\mu$  and diffusion coefficient  $\sigma^2$  (abbreviated  $X \sim \text{BM}(\mu, \sigma^2)$ ) if

$$\frac{X(t) - \mu t}{\sigma}$$

is a standard Brownian motion. Thus, we may construct  $X$  from a standard Brownian motion  $W$  by setting

$$X(t) = \mu t + \sigma W(t).$$

It follows that  $X(t) \sim N(\mu t, \sigma^2 t)$ . Moreover, X solves the stochastic differen- $\text{tial equation (SDE)}$ 

$$dX(t) = \mu \, dt + \sigma \, dW(t).$$

The assumption that  $X(0) = 0$  is a natural normalization, but we may construct a Brownian motion with parameters  $\mu$  and  $\sigma^2$  and initial value x by simply adding x to each  $X(t)$ .

For deterministic but time-varying  $\mu(t)$  and  $\sigma(t) > 0$ , we may define a Brownian motion with drift  $\mu$  and diffusion coefficient  $\sigma^2$  through the SDE

$$dX(t) = \mu(t) dt + \sigma(t) dW(t)$$

i.e., through

$$X(t) = X(0) + \int_0^t \mu(s) \, ds + \int_0^t \sigma(s) \, dW(s),$$

with  $X(0)$  an arbitrary constant. The process X has continuous sample paths and independent increments. Each increment  $X(t) - X(s)$  is normally distribited with mean

$$\mathsf{E}[X(t) - X(s)] = \int_s^t \mu(u) \, du$$

 $\mathbf{L}$ nd variance

$$\operatorname{Var}[X(t) - X(s)] = \operatorname{Var}\left[\int_s^t \sigma(u) \, dW(u)\right] = \int_s^t \sigma^2(u) \, du.$$

# Random Walk Construction

In discussing the simulation of Brownian motion, we mostly focus on simulating values  $(W(t_1), \ldots, W(t_n))$  or  $(X(t_1), \ldots, X(t_n))$  at a fixed set of points  $0 < t_1 < \cdots < t_n$ . Because Brownian motion has independent normally distributed increments, simulating the  $W(t_i)$  or  $X(t_i)$  from their increments is straightforward. Let  $Z_1, \ldots, Z_n$  be independent standard normal random variables, generated using any of the methods in Section  $2.3.2$ , for example. For a standard Brownian motion set  $t_0 = 0$  and  $W(0) = 0$ . Subsequent values can be generated as follows:

$$W(t_{i+1}) = W(t_i) + \sqrt{t_{i+1} - t_i} Z_{i+1}, \quad i = 0, \dots, n-1.$$

$$(3.2)$$

For  $X \sim \text{BM}(\mu, \sigma^2)$  with constant  $\mu$  and  $\sigma$  and given  $X(0)$ , set

$$X(t_{i+1}) = X(t_i) + \mu(t_{i+1} - t_i) + \sigma \sqrt{t_{i+1} - t_i} Z_{i+1}, \quad i = 0, \dots, n-1. \tag{3.3}$$

With time-dependent coefficients, the recursion becomes

$$X(t_{i+1}) = X(t_i) + \int_{t_i}^{t_{i+1}} \mu(s) \, ds + \sqrt{\int_{t_i}^{t_{i+1}} \sigma^2(u) \, du} Z_{i+1}, \quad i = 0, \dots, n-1.$$
(3.4)

The methods in  $(3.2)$ – $(3.4)$  are *exact* in the sense that the joint distribution of the simulated values  $(W(t_1), \ldots, W(t_n))$  or  $(X(t_1), \ldots, X(t_n))$  coincides with the joint distribution of the corresponding Brownian motion at  $t_1,\ldots,t_n$ . Of course, this says nothing about what happens between the  $t_i$ . One may extend the simulated values to other time points through, e.g., piecewise linear interpolation; but no deterministic interpolation method will give the extended vector the correct joint distribution. The methods in  $(3.2)$ – $(3.4)$ are exact at the time points  $t_1, \ldots, t_n$  but subject to discretization error, compared to a true Brownian motion, if deterministically interpolated to other time points. Replacing  $(3.4)$  with the Euler approximation

$$X(t_{i+1}) = X(t_i) + \mu(t_i)(t_{i+1} - t_i) + \sigma(t_i)\sqrt{t_{i+1} - t_i}Z_{i+1}, \quad i = 0, \ldots, n-1,$$

will in general introduce discretization error even at  $t_1,\ldots,t_n$ , because the increments will no longer have exactly the right mean and variance. We return to the topic of discretization error in Chapter 6.

The vector  $(W(t_1), \ldots, W(t_n))$  is a linear transformation of the vector of increments  $(W(t_1), W(t_2) - W(t_1), \ldots, W(t_n) - W(t_{n-1}))$ . Since these increments are independent and normally distributed, it follows from the Linear Transformation Property (2.23) that  $(W(t_1), \ldots, W(t_n))$  has a multivariate normal distribution. Simulating  $(W(t_1), \ldots, W(t_n))$  is thus a special case of the general problem, treated in Section 2.3.3, of generating multivariate normal vectors. While the random walk construction suffices for most applications, it is interesting and sometimes useful to consider alternative sampling methods.

To apply any of the methods considered in Section 2.3.3, we first need to find the mean vector and covariance matrix of  $(W(t_1), \ldots, W(t_n))$ . For a standard Brownian motion, we know from (3.1) that  $E[W(t_i)] = 0$ , so the mean vector is identically 0. For the covariance matrix, consider first any  $0 < s < t < T$ ; using the independence of the increments we find that

$$\begin{aligned} \mathsf{Cov}[W(s), W(t)] &= \mathsf{Cov}[W(s), W(s) + (W(t) - W(s))] \\ &= \mathsf{Cov}[W(s), W(s)] + \mathsf{Cov}[W(s), W(t) - W(s)] \\ &= s + 0 = s. \end{aligned} \tag{3.5}$$

Letting C denote the covariance matrix of  $(W(t_1), \ldots, W(t_n))$ , we thus have

$$C_{ij} = \min(t_i, t_j). \tag{3.6}$$

# Cholesky Factorization

Having noted that the vector  $(W(t_1), \ldots, W(t_n))$  has the distribution  $N(0, C)$ , with  $C$  as in (3.6), we may simulate this vector as  $AZ$ , where  $Z = (Z_1, \ldots, Z_n)^\top$  $\sim N(0, I)$  and A satisfies  $AA^{\top} = C$ . The Cholesky method discussed in Section 2.3.3 takes A to be lower triangular. For C in  $(3.6)$ , the Cholesky factor s given by

$$A = \begin{pmatrix} \sqrt{t_1} & 0 & \cdots & 0\\ \sqrt{t_1} & \sqrt{t_2 - t_1} & \cdots & 0\\ \vdots & \vdots & \ddots & \vdots\\ \sqrt{t_1} & \sqrt{t_2 - t_1} & \cdots & \sqrt{t_n - t_{n-1}} \end{pmatrix},$$

is can be verified through calculation of  $AA^{\top}$ . In this case, generating  $W(t_1), \ldots, W(t_n)$  as AZ is simply a matrix-vector representation of the ecursion in  $(3.2)$ . Put differently, the random walk construction  $(3.2)$  may be iewed as an efficient implementation of the product  $AZ$ . Even exploiting the ower triangularity of A, evaluation of AZ is an  $O(n^2)$  operation; the random ralk construction reduces this to  $O(n)$  by implicitly exploiting the fact that he nonzero entries of each column of  $A$  are identical.

For a BM $(\mu, \sigma^2)$  process X, the mean vector of  $(X(t_1), \ldots, X(t_n))$  has th component  $\mu t_i$  and the covariance matrix is  $\sigma^2 C$ . The Cholesky factor  $\sigma A$  and we once again find that the Cholesky method coincides with the  $\text{increment recursion } (3.3).$ 

# rownian Bridge Construction

he recursion (3.2) generates the vector  $(W(t_1), \ldots, W(t_n))$  from left to right. le may however generate the  $W(t_i)$  in any order we choose, provided that ; each step we sample from the correct conditional distribution given the lues already generated. For example, we may first generate the final value  $V(t_n)$ , then sample  $W(t_{\lfloor n/2 \rfloor})$  conditional on the value of  $W(t_n)$ , and proceed

by progressively filling in intermediate values. This flexibility can be useful in implementing variance reduction techniques and low-discrepancy methods. It follows from the Conditioning Formula  $(2.24)$  that the conditional distribution needed at each step is itself normal and this makes conditional sampling feasible.

Conditioning a Brownian motion on its endpoints produces a *Brownian bridge.* Once we determine  $W(t_n)$ , filling in intermediate values amounts to simulating a Brownian bridge from  $0 = W(0)$  to  $W(t_n)$ . If we next sample  $W(t_{\lfloor n/2 \rfloor})$ , then filling in values between times  $t_{\lfloor n/2 \rfloor}$  and  $t_n$  amounts to simulating a Brownian bridge from  $W(t_{\mid n/2 \mid})$  to  $W(t_n)$ . This approach is thus referred to as a Brownian bridge construction.

As a first step in developing this construction, suppose  $0 < u < s < t$ and consider the problem of generating  $W(s)$  conditional on  $W(u) = x$  and  $W(t) = y$ . We use the Conditioning Formula (2.24) to find the conditional distribution of  $W(s)$ . We know from (3.5) that the unconditional distribution is given by

$$\begin{pmatrix} W(u) \\ W(s) \\ W(t) \end{pmatrix} \sim N \left( 0, \begin{pmatrix} u & u & u \\ u & s & s \\ u & s & t \end{pmatrix} \right).$$

The Conditioning Formula  $(2.24)$  gives the distribution of the second component of a partitioned vector conditional on a value of the first component. We want to apply this formula to find the distribution of  $W(s)$  conditional on the value of  $(W(u), W(t))$ . We therefore first permute the entries of the vector to  $\text{get}$ 

$$\begin{pmatrix} W(s) \\ W(u) \\ W(t) \end{pmatrix} \sim N \left( 0, \begin{pmatrix} s \ u \ s \\ u \ u \ u \\ s \ u \ t \end{pmatrix} \right)$$

We now find from the Conditioning Formula that, given  $(W(u) = x, W(t) =$  $y$ ,  $W(s)$  is normally distributed with mean

$$\mathsf{E}[W(s)|W(u) = x, W(t) = y] = 0 - (u \ s) \begin{pmatrix} u \ u \\ u \ t \end{pmatrix}^{-1} \begin{pmatrix} x \\ y \end{pmatrix} = \frac{(t-s)x + (s-u)y}{(t-u)}, \tag{3.7}$$

and variance

$$s - \left(u\ s\right) \begin{pmatrix} u\ u \\ u\ t \end{pmatrix}^{-1} \begin{pmatrix} u \\ s \end{pmatrix} = \frac{(s-u)(t-s)}{(t-u)},\tag{3.8}$$

 $\text{since}$ 

$$\begin{pmatrix} u \ u \ t \end{pmatrix}^{-1} = \frac{1}{t-u} \begin{pmatrix} t/u \ -1 \ 1 \end{pmatrix}.$$

In particular, the conditional mean  $(3.7)$  is obtained by linearly interpolating between  $(u, x)$  and  $(t, y)$ .

Suppose, more generally, that the values  $W(s_1) = x_1, W(s_2) = x_2, \ldots,$  $W(s_k) = x_k$  of the Brownian path have been determined at the times  $s_1 <$  $s_2 < \cdots < s_k$  and that we wish to sample  $W(s)$  conditional on these values. Suppose that  $s_i < s < s_{i+1}$ . Then

$$(W(s)|W(s_j) = x_j, j = 1, \ldots, k) = (W(s)|W(s_i) = x_i, W(s_{i+1}) = x_{i+1}),$$

in the sense that the two conditional distributions are the same. This can again be derived from the Conditioning Formula  $(2.24)$  but is more immediate from the Markov property of Brownian motion (a consequence of the independent increments property): given  $W(s_i)$ ,  $W(s)$  is independent of all  $W(t)$  with  $t < s_i$ , and given  $W(s_{i+1})$  it is independent of all  $W(t)$  with  $t > s_{i+1}$ . Thus, conditioning on all  $W(s_i)$  is equivalent to conditioning on the values of the Brownian path at the two times  $s_i$  and  $s_{i+1}$  closest to s. Combining these observations with  $(3.7)$  and  $(3.8)$ , we find that

$$(W(s)|W(s_1) = x_1, W(s_2) = x_2, \dots, W(s_k) = x_k) = N\left(\frac{(s_{i+1} - s)x_i + (s - s_i)x_{i+1}}{(s_{i+1} - s_i)}, \frac{(s_{i+1} - s)(s - s_i)}{(s_{i+1} - s_i)}\right).$$

This is illustrated in Figure 3.1. The conditional mean of  $W(s)$  lies on the ine segment connecting  $(s_i, x_i)$  and  $(s_{i+1}, x_{i+1})$ ; the actual value of  $W(s)$  is ormally distributed about this mean with a variance that depends on  $(s-s_i)$ nd  $(s_{i+1}-s)$ . To sample from this conditional distribution, we may set

$$W(s) = \frac{(s_{i+1} - s)x_i + (s - s_i)x_{i+1}}{(s_{i+1} - s_i)} + \sqrt{\frac{(s_{i+1} - s)(s - s_i)}{(s_{i+1} - s_i)}}Z,$$

 $\text{ith } Z \sim N(0,1) \text{ independent of all } W(s_1), \ldots, W(s_k).$ 

By repeatedly using these observations, we may indeed sample the comonents of the vector  $(W(t_1), \ldots, W(t_n))$  in any order. In particular, we may art by sampling  $W(t_n)$  from  $N(0, t_n)$  and proceed by conditionally sampling termediate values, at each step conditioning on the two closest time points ready sampled (possibly including  $W(0) = 0$ ).

If n is a power of 2, the construction can be arranged so that each  $W(t_i)$ ,  $< n$ , is generated conditional on the values  $W(t_{\ell})$  and  $W(t_r)$  with the operty that i is midway between  $\ell$  and r. Figure 3.2 details this case. If, for ample,  $n = 16$ , the algorithm starts by sampling  $W(t_{16})$ ; the first loop over samples  $W(t_8)$ ; the second samples  $W(t_4)$  and  $W(t_{12})$ ; the third samples  $(t_2)$ ,  $W(t_6)$ ,  $W(t_{10})$ , and  $W(t_{14})$ ; and the final loop fills in all  $W(t_i)$  with  $\text{Id } i$ . If n is not a power of 2, the algorithm could still be applied to a subset  $2^m < n$  of the  $t_i$ , with the remaining points filled in at the end.

Our discussion of the Brownian bridge construction (and Figure 3.2 in rticular) has considered only the case of a standard Brownian motion. How ould the construction be modified for a Brownian motion with drift  $\mu$ ? Only

![](_page_6_Figure_1.jpeg)

**Fig. 3.1.** Brownian bridge construction of Brownian path. Conditional on  $W(s_i)$  $x_i$  and  $W(s_{i+1}) = x_{i+1}$ , the value at s is normally distributed. The conditional mean is obtained by linear interpolation between  $x_i$  and  $x_{i+1}$ ; the conditional variance is obtained from  $(3.8)$ .

```
Input:
                      Time indices (t_1, \ldots, t_{2^m})Path (w_1, \ldots, w_{2^m}) with distribution of (W(t_1), \ldots, W(t_{2^m}))Output:Generate (Z_1,\ldots,Z_{2^m}) \sim N(0,I)\begin{array}{l} h \leftarrow 2^m, \quad j_{\text{max}} \leftarrow 1 \\ w_h \leftarrow \sqrt{t_h} Z_h \end{array}t_0 \leftarrow 0, w_0 \leftarrow 0for k = 1, \ldots, mi_{\min} \leftarrow h/2, \quad i \leftarrow i_{\min}\ell \leftarrow 0, \quad r \leftarrow hfor j = 1, \ldots, j_{\text{max}}a \leftarrow \left( (t_r - t_i) w_\ell + (t_i - t_\ell) w_r \right) / (t_r - t_\ell)<br>b \leftarrow \sqrt{(t_i - t_\ell) (t_r - t_i) / (t_r - t_\ell)}w_i \leftarrow a + bZ_ii \leftarrow i + h; \quad \ell \leftarrow \ell + h, \quad r \leftarrow r + h\text{end}j_{\text{max}} \leftarrow 2 * j_{\text{max}};h \leftarrow i_{\min};end
     return (w_1, \ldots, w_{2^m})
```

Fig. 3.2. Implementation of Brownian bridge construction when the number of time indices is a power of 2. The conditional standard deviations assigned to  $b$  could be precomputed and stored in an array  $(b_1,\ldots,b_{2^m})$  if multiple paths are to be generated. The interpolation weights used in calculating the conditional mean  $a$ could also be precomputed.

the first step — sampling of the rightmost point — would change. Instead of sampling  $W(t_m)$  from  $N(0,t_m)$ , we would sample it from  $N(\mu t_m, t_m)$ . The conditional distribution of  $W(t_1), \ldots, W(t_{n-1})$  given  $W(t_m)$  is the same for all values of  $\mu$ . Put slightly differently, a Brownian bridge constructed from a Brownian motion with drift has the same law as one constructed from a standard Brownian motion. (For any finite set of points  $t_1, \ldots, t_{n-1}$  this can be established from the Conditioning Formula  $(2.24)$ .) Hence, to include a drift  $\mu$  in the algorithm of Figure 3.2, it suffices to change just the third line, adding  $\mu t_h$  to  $w_h$ . For a Brownian motion with diffusion coefficient  $\sigma^2$ , the conditional mean  $(3.7)$  is unchanged but the conditional variance  $(3.8)$ is multiplied by  $\sigma^2$ . This could be implemented in Figure 3.2 by multiplying each b by  $\sigma$  (and setting  $w_h \leftarrow \mu t_h + \sigma \sqrt{t_h} Z_h$  in the third line); alternatively, the final vector  $(w_1, \ldots, w_{2^m})$  could simply be multiplied by  $\sigma$ .

Why use a Brownian bridge construction? The algorithm in Figure 3.2 has no computational advantage over the simple random walk recursion  $(3.2)$ . Nor loes the output of the algorithm have any statistical feature not shared by the output of  $(3.2)$ ; indeed, the Brownian bridge construction is valid precisely because the distribution of the  $(W(t_1), \ldots, W(t_m))$  it produces coincides with that resulting from  $(3.2)$ . The potential advantage of the Brownian bridge construction arises when it is used with certain variance reduction techniques and low-discrepancy methods. We will return to this point in Section 4.3 and Thapter 5. Briefly, the Brownian bridge construction gives us greater control wer the coarse structure of the simulated Brownian path. For example, it ises a single normal random variable to determine the endpoint of a path, which may be the most important feature of the path; in contrast, the endoint obtained from  $(3.2)$  is the combined result of n independent normal andom variables. The standard recursion  $(3.2)$  proceeds by evolving the path orward through time; in contrast, the Brownian bridge construction proceeds  $y$  adding increasingly fine detail to the path at each step, as illustrated in igure 3.3. This can be useful in focusing variance reduction techniques on important" features of Brownian paths.

### 'rincipal Components Construction

s just noted, under the Brownian bridge construction a single normal random riable (say  $Z_1$ ) determines the endpoint of the path; conditional on the idpoint, a second normal random variable (say  $Z_2$ ) determines the midpoint the path, and so on. Thus, under this construction, much of the ultimate ape of the Brownian path is determined (or *explained*) by the values of just ie first few  $Z_i$ . Is there a construction under which even more of the path determined by the first few  $Z_i$ ? Is there a construction that maximizes the riability of the path explained by  $Z_1, \ldots, Z_k$  for all  $k = 1, \ldots, n$ ?

This optimality objective is achieved for any normal random vector by the incipal components construction discussed in Section  $2.3.3$ . We now discuss 3 application to a discrete Brownian path  $W(t_1), \ldots, W(t_n)$ . It is useful to

![](_page_8_Figure_1.jpeg)

Fig. 3.3. Brownian bridge construction after 1, 2, 4, and 8 points have been sampled. Each step refines the previous path.

visualize the construction in vector form as

ŕ,

$$\begin{pmatrix} W(t_1) \\ W(t_2) \\ \vdots \\ W(t_n) \end{pmatrix} = \begin{pmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{n1} \end{pmatrix} Z_1 + \begin{pmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{n2} \end{pmatrix} Z_2 + \dots + \begin{pmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{nn} \end{pmatrix} Z_n. \tag{3.9}$$

Let  $a_i = (a_{1i}, \ldots, a_{ni})^\top$  and let A be the  $n \times n$  matrix with columns  $a_1,\ldots,a_n$ . We know from Section 2.3.3 that this is a valid construction of the discrete Brownian path if  $AA^{\top}$  is the covariance matrix C of W =  $(W(t_1),\ldots,W(t_n))^\top$ , given in (3.6). We also know from the discussion of principal components in Section 2.3.3 that the approximation error

$$\mathsf{E}\left[\|W - \sum_{i=1}^{k} a_i Z_i\|^2\right] \qquad (\|x\|^2 = x^{\top} x)$$

from using just the first k terms in (3.9) is minimized for all  $k = 1, \ldots, n$ by using principal components. Specifically,  $a_i = \sqrt{\lambda_i} v_i$ ,  $i = 1, \ldots, n$ , where  $\lambda_1 > \lambda_2 > \cdots > \lambda_n > 0$  are the eigenvalues of C and the  $v_i$  are eigenvectors,

$$Cv_i = \lambda_i v_i, \quad i = 1, \dots, n,$$

normalized to have length  $||v_i|| = 1$ .

Consider, for example, a 32-step discrete Brownian path with equal time increments  $t_{i+1} - t_i = 1/32$ . The corresponding covariance matrix has entries

 $\mathcal{I}_{ij} = \min(i,j)/32, i,j = 1,\ldots,32.$  The magnitudes of the eigenvalues of this natrix drop off rapidly — the five largest are  $13.380, 1.489, 0.538, 0.276,$  and ).168. The variability explained by  $Z_1, \ldots, Z_k$  (in the sense of (2.34)) is 81%,  $10\%, 93\%, 95\%, \text{ and } 96\%, \text{ for } k = 1, \ldots, 5; \text{ it exceeds } 99\% \text{ at } k = 16. \text{ This}$  $\text{indicates that although full construction of the 32-step path requires 32 normal}$ andom variables, most of the variability of the path can be determined using ar fewer  $Z_i$ .

Figure 3.4 plots the normalized eigenvectors  $v_1, v_2, v_3$ , and  $v_4$  associated  $\text{with the four largest eigenvalues. (Each of these is a vector with 32 entries; }$ hey are plotted against the  $j\Delta t$ ,  $j = 1, \ldots, 32$ , with  $\Delta t = 1/32$ .) The  $v_i$ ppear to be nearly sinusoidal, with frequencies that increase with  $i$ . Indeed, kesson and Lehoczky [8] show that for an  $n$ -step path with equal spacing  $_{i+1}-t_i=\Delta t,$ 

$$v_i(j) = \frac{2}{\sqrt{2n+1}} \sin\left(\frac{2i-1}{2n+1}j\pi\right), \quad j = 1, \dots, n,$$

nd

$$\lambda_i = \frac{\Delta t}{4} \sin^{-2} \left( \frac{2i-1}{2n+1} \frac{\pi}{2} \right),$$

 $\mathbf{r}$   $i = 1, \ldots, n$ . To contrast this with the Brownian bridge construction in igure 3.3, note that in the principal components construction the  $v_i$  are ultiplied by  $\sqrt{\lambda_i}Z_i$  and then summed; thus, the discrete Brownian path ay be viewed as a random linear combination of the vectors  $v_i$ , with random efficients  $\sqrt{\lambda_i}Z_i$ . The coefficient on  $v_i$  has variance  $\lambda_i$  and we have seen that le  $\lambda_i$  drop off quickly. Thus, the first few  $v_i$  (and  $\sqrt{\lambda_i}Z_i$ ) determine most of e shape of the Brownian path and the later  $v_i$  add high-frequency detail to e path. As in the Brownian bridge construction, these features can be useful implementing variance reduction techniques by making it possible to focus the most important  $Z_i$ . We return to this point in Sections 4.3.2 and 5.5.2.

Although the principal components construction is optimal with respect explained variability, it has two drawbacks compared to the random walk d Brownian bridge constructions. The first is that it requires  $O(n^2)$  operions to construct  $W(t_1), \ldots, W(t_n)$  from  $Z_1, \ldots, Z_n$ , whereas the previous nstructions require  $O(n)$  operations. The second (potential) drawback is at with principal components none of the  $W(t_i)$  is fully determined until  $Z_1,\ldots,Z_n$  have been processed — i.e., until all terms in (3.9) have been mmed. In contrast, using either the random walk or Brownian bridge conuction, exactly k of the  $W(t_1), \ldots, W(t_n)$  are fixed by the first k normal adom variables, for all  $k = 1, \ldots, n$ .

We conclude this discussion of the principal components construction with rief digression into simulation of a continuous path  $\{W(t), 0 \le t \le 1\}$ . In discrete case, the eigenvalue-eigenvector condition  $Cv = \lambda v$  is (recall (3.6))

$$\sum_{j} \min(t_i, t_j) v(j) = \lambda v(i).$$

![](_page_10_Figure_1.jpeg)

Fig. 3.4. First four eigenvectors of the covariance matrix of a 32-step Brownian path, ordered according to the magnitude of the corresponding eigenvalue.

In the continuous limit, the analogous property for an eigenfunction  $\psi$  on  $[0, 1]$  is

$$\int_0^1 \min(s, t) \psi(s) \, ds = \lambda \psi(t).$$

The solutions to this equation and the corresponding eigenvalues are

$$\psi_i(t) = \sqrt{2} \sin\left(\frac{(2i+1)\pi t}{2}\right), \quad \lambda_i = \left(\frac{2}{(2i+1)\pi}\right)^2, \quad i = 0, 1, 2, \dots$$

Note in particular that the  $\psi_i$  are periodic with increasing frequencies and that the  $\lambda_i$  decrease with *i*. The *Karhounen-Loève expansion* of Brownian motion is

$$W(t) = \sum_{i=0}^{\infty} \sqrt{\lambda_i} \psi_i(t) Z_i, \quad 0 \le t \le 1,$$
(3.10)

with  $Z_0, Z_1, \ldots$  independent  $N(0, 1)$  random variables; see, e.g., Adler [5]. This infinite series is an exact representation of the continuous Brownian path. It may be viewed as a continuous counterpart to  $(3.9)$ . By taking just the first  $k$  terms in this series, we arrive at an approximation to the continuous path  $\{W(t), 0 \le t \le 1\}$  that is optimal (among all approximations that use just  $k$  standard normals) in the sense of explained variability. This approximation does not however yield the exact joint distribution for any subset  $\{W(t_1), \ldots, W(t_n)\}\$  except the trivial case  $\{W(0)\}.$ 

The Brownian bridge construction also admits a continuous counterpart through a series expansion using *Schauder functions* in place of the  $\sqrt{\lambda_i}\psi_i$ 

in  $(3.10)$ . Lévy [233, pp.17–20] used the limit of the Brownian bridge construction to construct Brownian motion; the formulation as a series expansion is discussed in Section 1.2 of McKean  $[260]$ . Truncating the series after  $2^m$  terms produces the piecewise linear interpolation of a discrete Brownian bridge construction of  $W(0), W(2^{-m}), \ldots, W(1)$ . See Acworth et al. [4] for further discussion with applications to Monte Carlo.

# 3.1.2 Multiple Dimensions

We call a process  $W(t) = (W_1(t), \ldots, W_d(t))^\top$ ,  $0 < t < T$ , a standard Brownian motion on  $\Re^d$  if it has  $W(0) = 0$ , continuous sample paths, independent increments, and

$$W(t) - W(s) \sim N(0, (t-s)I),$$

for all  $0 \le s \le t \le T$ , with I the  $d \times d$  identity matrix. It follows that each of the coordinate processes  $W_i(t), i = 1, \ldots, d$ , is a standard one-dimensional Brownian motion and that  $W_i$  and  $W_j$  are independent for  $i \neq j$ .

Suppose  $\mu$  is a vector in  $\Re^d$  and  $\Sigma$  is a  $d \times d$  matrix, positive definite or semidefinite. We call a process X a Brownian motion with drift  $\mu$  and covariance  $\Sigma$  (abbreviated  $X \sim \text{BM}(\mu, \Sigma)$ ) if X has continuous sample paths and independent increments with

$$X(t) - X(s) \sim N((t-s)\mu, (t-s)\Sigma).$$

The initial value  $X(0)$  is an arbitrary constant assumed to be 0 unless otherwise specified. If B is a  $d \times k$  matrix satisfying  $BB^{\top} = \Sigma$  and if W is a standard Brownian motion on  $\mathbb{R}^k$ , then the process defined by

$$X(t) = \mu t + BW(t) \tag{3.11}$$

is a  $\text{BM}(\mu,\Sigma)$ . In particular, the law of X depends on B only through  $BB^{\top}$ .

The process in  $(3.11)$  solves the SDE

$$dX(t) = \mu \, dt + B \, dW(t).$$

We may extend the definition of a multidimensional Brownian motion to deterministic, time-varying  $\mu(t)$  and  $\Sigma(t)$  through the solution to

$$dX(t) = \mu(t) dt + B(t) dW(t),$$

where  $B(t)B^{\top}(t) = \Sigma(t)$ . This process has continuous sample paths, independent increments, and

$$X(t) - X(s) \sim N\left(\int_s^t \mu(u) \, du, \int_s^t \Sigma(u) \, du\right).$$

A calculation similar to the one leading to (3.5) shows that if  $X \sim$  $\text{3M}(\mu, \Sigma)$ , then

$$\operatorname{Cov}[X_i(s), X_j(t)] = \min(s, t) \Sigma_{ij}.$$
(3.12)

In particular, given a set of times  $0 < t_1 < t_2 < \cdots < t_n$ , we can easily find the covariance matrix of

$$(X_1(t_1), \ldots, X_d(t_1), X_1(t_2), \ldots, X_d(t_2), \ldots, X_1(t_n), \ldots, X_d(t_n)) \qquad (3.13)$$

along with its mean and reduce the problem of generating a discrete path of  $X$  to one of sampling this *nd*-dimensional normal vector. While there could be cases in which this is advantageous, it will usually be more convenient to use the fact that this  $nd$ -vector is the concatenation of  $d$ -vectors representing the state of the process at  $n$  distinct times.

### Random Walk Construction

Let  $Z_1, Z_2, \ldots$  be independent  $N(0, I)$  random vectors in  $\mathbb{R}^d$ . We can construct a standard d-dimensional Brownian motion at times  $0 = t_0 < t_1 < \cdots < t_n$ by setting  $W(0) = 0$  and

$$W(t_{i+1}) = W(t_i) + \sqrt{t_{i+1} - t_i} Z_{i+1}, \quad i = 0, \dots, n-1.$$

$$(3.14)$$

This is equivalent to applying the one-dimensional random walk construction  $(3.2)$  separately to each coordinate of  $W$ .

To simulate  $X \sim \text{BM}(\mu, \Sigma)$ , we first find a matrix B for which  $BB^{\top} = \Sigma$ (see Section 2.3.3). If B is  $d \times k$ , let  $Z_1, Z_2, \ldots$  be independent standard normal random vectors in  $\mathbb{R}^k$ . Set  $X(0) = 0$  and

$$X(t_{i+1}) = X(t_i) + \mu(t_{i+1} - t_i) + \sqrt{t_{i+1} - t_i} BZ_i, \quad i = 0, \dots, n-1. \quad (3.15)$$

Thus, simulation of  $\mathrm{BM}(\mu,\Sigma)$  is straightforward once  $\Sigma$  has been factored. For the case of time-dependent coefficients, we may set

$$X(t_{i+1}) = X(t_i) + \int_{t_i}^{t_{i+1}} \mu(s) \, ds + B(t_i, t_{i+1}) Z_i, \quad i = 0, \dots, n-1,$$

with

$$B(t_i, t_{i+1})B(t_i, t_{i+1})^{\top} = \int_{t_i}^{t_{i+1}} \Sigma(u) \, du,$$

thus requiring  $n$  factorizations.

# Brownian Bridge Construction

Application of a Brownian bridge construction to a standard  $d$ -dimensional Brownian motion is straightforward: we may simply apply independent onedimensional constructions to each of the coordinates. To include a drift vector (i.e., for BM( $\mu, I$ ) process), it suffices to add  $\mu_i t_n$  to  $W_i(t_n)$  at the first step

of the construction of the *i*th coordinate, as explained in Section 3.1.1. The rest of the construction is unaffected.

To construct  $X \sim \text{BM}(\mu, \Sigma)$ , we may use the fact that X can be represented as  $X(t) = \mu t + BW(t)$  with B a  $d \times k$  matrix,  $k < d$ , satisfy- $\text{ing } BB^{\top} = \Sigma$ , and W a standard k-dimensional Brownian motion. We may then apply a Brownian bridge construction to  $W(t_1), \ldots, W(t_n)$  and recover  $X(t_1), \ldots, X(t_n)$  through a linear transformation.

### Principal Components Construction

As with the Brownian bridge construction, one could apply a one-dimensional principal components construction to each coordinate of a multidimensional Brownian motion. Through a linear transformation this then extends to the construction of  $\mathrm{BM}(\mu,\Sigma)$ . However, the optimality of principal components is lost in this reduction; to recover it, we must work directly with the covariance matrix of  $(3.13)$ .

It follows from  $(3.12)$  that the covariance matrix of  $(3.13)$  can be represented as  $(C \otimes \Sigma)$ , where  $\otimes$  denotes the Kronecker product producing

$$(C \otimes \Sigma) = \begin{pmatrix} C_{11}\Sigma & C_{12}\Sigma & \cdots & C_{1n}\Sigma \\ C_{21}\Sigma & C_{22}\Sigma & \cdots & C_{2n}\Sigma \\ \vdots & \vdots & \ddots & \vdots \\ C_{n1}\Sigma & C_{n2}\Sigma & \cdots & C_{nn}\Sigma \end{pmatrix}.$$

If C has eigenvectors  $v_1,\ldots,v_n$  and eigenvalues  $\lambda_1 \geq \cdots \geq \lambda_n$ , and if  $\Sigma$ has eigenvectors  $w_1,\ldots,w_d$  and eigenvalues  $\eta_1 \geq \cdots \geq \eta_d$ , then  $(C \otimes \Sigma)$ has eigenvectors  $(v_i \otimes w_j)$  and eigenvalues  $\lambda_i \eta_j$ ,  $i = 1, \dots, n, j = 1, \times, d$ . This special structure of the covariance matrix of  $(3.12)$  makes it possible to reduce the computational effort required to find all eigenvalues and eigenvectors from the  $O((nd)^3)$  typically required for an  $(nd \times nd)$  matrix to  $O(n^3 + d^3)$ .

If we rank the products of eigenvalues as

$$(\lambda_i \eta_j)_{(1)} \geq (\lambda_i \eta_j)_{(2)} \geq \cdots (\lambda_i \eta_j)_{(nd)},$$

hen for any  $k = 1, \ldots, n$ ,

$$\frac{\sum_{r=1}^k (\lambda_i \eta_j)_{(r)}}{\sum_{r=1}^{nd} (\lambda_i \eta_j)_{(r)}} \le \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^n \lambda_i}.$$

n other words, the variability explained by the first  $k$  factors is always smaller or a  $d$ -dimensional Brownian motion than it would be for a scalar Brownin motion over the same time points. This is to be expected since the  $d$ imensional process has greater total variability.

# 3.2 Geometric Brownian Motion

50  $\mathcal{L}_{\mathcal{L}}$ 

> A stochastic process  $S(t)$  is a *geometric Brownian motion* if  $\log S(t)$  is a Brownian motion with initial value  $\log S(0)$ ; in other words, a geometric Brownian motion is simply an exponentiated Brownian motion. Accordingly, all methods for simulating Brownian motion become methods for simulating geometric Brownian motion through exponentiation. This section therefore focuses more on modeling than on algorithmic issues.

> Geometric Brownian motion is the most fundamental model of the value of a financial asset. In his pioneering thesis of 1900, Louis Bachelier developed a model of stock prices that in retrospect we describe as ordinary Brownian motion, though the mathematics of Brownian motion had not yet been developed. The use of geometric Brownian motion as a model in finance is due primarily to work of Paul Samuelson in the 1960s. Whereas ordinary Brownian motion can take negative values — an undesirable feature in a model of the price of a stock or any other limited liability asset — geometric Brownian motion is always positive because the exponential function takes only positive values. More fundamentally, for geometric Brownian motion the *percentage*  $\text{changes}$

$$\frac{S(t_2) - S(t_1)}{S(t_1)}, \frac{S(t_3) - S(t_2)}{S(t_2)}, \dots, \frac{S(t_n) - S(t_{n-1})}{S(t_{n-1})}$$
(3.16)

are independent for  $t_1 < t_2 < \cdots < t_n$ , rather than the absolute changes  $S(t_{i+1}) - S(t_i)$ . These properties explain the centrality of geometric rather than ordinary Brownian motion in modeling asset prices.

### 3.2.1 Basic Properties

Suppose  $W$  is a standard Brownian motion and  $X$  satisfies

$$dX(t) = \mu \, dt + \sigma \, dW(t),$$

so that  $X \sim \text{BM}(\mu, \sigma^2)$ . If we set  $S(t) = S(0) \exp(X(t)) \equiv f(X(t))$ , then an application of Itô's formula shows that

$$dS(t) = f'(X(t)) dX(t) + \frac{1}{2}\sigma^2 f''(X(t)) dt$$
  
=  $S(0) \exp(X(t))[\mu dt + \sigma dW(t)] + \frac{1}{2}\sigma^2 S(0) \exp(X(t)) dt$   
=  $S(t)(\mu + \frac{1}{2}\sigma^2) dt + S(t)\sigma dW(t).$  (3.17)

In contrast, a geometric Brownian motion process is often specified through an SDE of the form

$$\frac{dS(t)}{S(t)} = \mu \, dt + \sigma \, dW(t), \tag{3.18}$$

an expression suggesting a Brownian model of the "instantaneous returns"  $dS(t)/S(t)$ . Comparison of (3.17) and (3.18) indicates that the models are

inconsistent and reveals an ambiguity in the role of " $\mu$ ." In (3.17),  $\mu$  is the drift of the Brownian motion we exponentiated to define  $S(t)$  — the drift of  $\log S(t)$ . In (3.18),  $S(t)$  has drift  $\mu S(t)$  and (3.18) implies

$$d\log S(t) = (\mu - \frac{1}{2}\sigma^2) dt + \sigma dW(t), \qquad (3.19)$$

as can be verified through Itô's formula or comparison with  $(3.17)$ .

We will use the notation  $S \sim \text{GBM}(\mu, \sigma^2)$  to indicate that S is a process of the type in (3.18). We will refer to  $\mu$  in (3.18) as the *drift parameter* though it is not the drift of either  $S(t)$  or  $\log S(t)$ . We refer to  $\sigma$  in (3.18) as the volatility parameter of  $S(t)$ ; the diffusion coefficient of  $S(t)$  is  $\sigma^2 S^2(t)$ .

From (3.19) we see that if  $S \sim \text{GBM}(\mu, \sigma^2)$  and if S has initial value  $S(0)$ ,  $\text{then}$ 

$$S(t) = S(0) \exp\left( [\mu - \frac{1}{2}\sigma^2]t + \sigma W(t) \right). \tag{3.20}$$

A bit more generally, if  $u < t$  then

$$S(t) = S(u) \exp\left( [\mu - \frac{1}{2}\sigma^2](t - u) + \sigma(W(t) - W(u)) \right), \tag{3.21}$$

from which the claimed independence of the returns in  $(3.16)$  becomes evident. Moreover, since the increments of  $W$  are independent and normally distributed, this provides a simple recursive procedure for simulating values of S at  $0 = t_0 < t_1 < \cdots < t_n$ :

$$S(t_{i+1}) = S(t_i) \exp\left( \left[ \mu - \frac{1}{2} \sigma^2 \right] (t_{i+1} - t_i) + \sigma \sqrt{t_{i+1} - t_i} Z_{i+1} \right), \quad (3.22)$$
  
$$i = 0, 1, \dots, n-1,$$

with  $Z_1, Z_2, \ldots, Z_n$  independent standard normals. In fact, (3.22) is equivalent to exponentiating both sides of (3.3) with  $\mu$  replaced by  $\mu - \frac{1}{2}\sigma^2$ . This method is *exact* in the sense that the  $(S(t_1), \ldots, S(t_n))$  it produces has the joint distribution of the process  $S \sim \text{GBM}(\mu, \sigma^2)$  at  $t_1, \ldots, t_n$  — the method involves no discretization error. Time-dependent parameters can be incorporated by exponentiating both sides of  $(3.4)$ .

### Lognormal Distribution

From (3.20) we see that if  $S \sim \text{GBM}(\mu, \sigma^2)$ , then the marginal distribution of  $S(t)$  is that of the exponential of a normal random variable, which is called ι lognormal distribution. We write  $Y \sim LN(\mu, \sigma^2)$  if the random variable Y as the distribution of  $\exp(\mu + \sigma Z)$ ,  $Z \sim N(0,1)$ . This distribution is thus given by

$$P(Y \le y) = P(Z \le [\log(y) - \mu]/\sigma)$$
  
=  $\Phi\left(\frac{\log(y) - \mu}{\sigma}\right)$ 

nd its density by

3.2 Geometric Brownian Motion 95

$$\frac{1}{y\sigma}\phi\left(\frac{\log(y)-\mu}{\sigma}\right). \tag{3.23}$$

Moments of a lognormal random variable can be calculated using the basic identity

$$\mathsf{E}[e^{aZ}] = e^{\frac{1}{2}a^2}$$

for the moment generating function of a standard normal. From this it follows that  $Y \sim LN(\mu, \sigma^2)$  has

$$\mathsf{E}[Y] = e^{\mu + \frac{1}{2}\sigma^2}, \quad \mathsf{Var}[Y] = e^{2\mu + \sigma^2} \left( e^{\sigma^2} - 1 \right);$$

in particular, the notation  $Y \sim LN(\mu, \sigma^2)$  does not imply that  $\mu$  and  $\sigma^2$  are the mean and variance of  $Y$ . From

$$P(Y \le e^{\mu}) = P(Z \le 0) = \frac{1}{2}$$

we see that  $e^{\mu}$  is the median of Y. The mean of Y is thus larger than the median, reflecting the positive skew of the lognormal distribution.

Applying these observations to (3.20), we find that if  $S \sim \text{GBM}(\mu, \sigma^2)$ then  $(S(t)/S(0)) \sim LN([\mu - \frac{1}{2}\sigma^2]t, \sigma^2 t)$  and

$$\mathsf{E}[S(t)] = e^{\mu t} S(0), \quad \mathsf{Var}[S(t)] = e^{2\mu t} S^2(0) \left( e^{\sigma^2 t} - 1 \right).$$

In fact, we have

й,

$$\mathsf{E}[S(t)|S(\tau), 0 \le \tau \le u] = \mathsf{E}[S(t)|S(u)] = e^{\mu(t-u)}S(u), \quad u < t, \tag{3.24}$$

and an analogous expression for the conditional variance. The first equality in  $(3.24)$  is the Markov property (which follows from the fact that S is a oneto-one transformation of a Brownian motion, itself a Markov process) and the second follows from  $(3.21)$ .

Equation (3.24) indicates that  $\mu$  acts as an average growth rate for S, a sort of average continuously compounded rate of return. Along a single sample path of  $S$  the picture is different. For a standard Brownian motion  $W$ , we have  $t^{-1}W(t) \to 0$  with probability 1. For  $S \sim \text{GBM}(\mu, \sigma^2)$ , we therefore find that

$$\frac{1}{t}\log S(t) \to \mu - \frac{1}{2}\sigma^2,$$

Ģ.

with probability 1, so  $\mu - \frac{1}{2}\sigma^2$  serves as the growth rate along each path. If this expression is positive,  $S(t) \to \infty$  as  $t \to \infty$ ; if it is negative, then  $S(t) \to 0$ . In a model with  $\mu > 0 > \mu - \frac{1}{2}\sigma^2$ , we find from (3.24) that  $\mathsf{E}[S(t)]$  grows exponentially although  $S(t)$  converges to 0. This seemingly pathological behavior is explained by the increasing skew in the distribution of  $S(t)$ : although  $S(t) \rightarrow 0$ , rare but very large values of  $S(t)$  are sufficiently likely to produce an increasing mean.

# 3.2.2 Path-Dependent Options

Our interest in simulating paths of geometric Brownian motion lies primarily in pricing options, particularly those whose payoffs depend on the path of an underlying asset S and not simply its value  $S(T)$  at a fixed exercise date T. Through the principles of option pricing developed in Chapter 1, the price of an option may be represented as an expected discounted payoff. This price is estimated through simulation by generating paths of the underlying asset, evaluating the discounted payoff on each path, and averaging over paths.

## Risk-Neutral Dynamics

The one subtlety in this framework is the probability measure with respect to which the expectation is taken and the nearly equivalent question of how the payoff should be discounted. This bears on how the paths of the underlying asset ought to be generated and more specifically in the case of geometric Brownian motion, how the drift parameter  $\mu$  should be chosen.

We start by assuming the existence of a constant continuously compounded interest rate  $r$  for riskless borrowing and lending. A dollar invested at this rate at time  $0$  grows to a value of

$$\beta(t) = e^{rt}$$

at time t. Similarly, a contract paying one dollar at a future time  $t$  (a zerocoupon bond) has a value at time 0 of  $e^{-rt}$ . In pricing under the risk-neutral measure, we discount a payoff to be received at time  $t$  back to time 0 by dividing by  $\beta(t)$ ; i.e.,  $\beta$  is the numeraire asset.

Suppose the asset  $S$  pays no dividends; then, under the risk-neutral measure, the discounted price process  $S(t)/\beta(t)$  is a martingale:

$$\frac{S(u)}{\beta(u)} = \mathsf{E}\left[\frac{S(t)}{\beta(t)}|\{S(\tau), 0 \le \tau \le u\}\right].\tag{3.25}$$

Comparison with  $(3.24)$  shows that if S is a geometric Brownian motion under the risk-neutral measure, then it must have  $\mu = r$ ; i.e.,

$$\frac{dS(t)}{S(t)} = r dt + \sigma dW(t). \tag{3.26}$$

As discussed in Section 1.2.2, this equation helps explain the name "riskneutral." In a world of risk-neutral investors, all assets would have the same  $\text{average rate of return}$  — investors would not demand a higher rate of return for holding risky assets. In a risk-neutral world, the drift parameter for  $S(t)$ would therefore equal the risk-free rate  $r$ .

In the case of an asset that pays dividends, we know from Section  $1.2.2$  that the martingale property  $(3.25)$  continues to hold but with S replaced by the sum of  $S$ , any dividends paid by  $S$ , and any interest earned from investing the

dividends at the risk-free rate r. Thus, let  $D(t)$  be the value of any dividends paid over  $[0, t]$  and interest earned on those dividends. Suppose the asset pays a continuous dividend yield of  $\delta$ , meaning that it pays dividends at rate  $\delta S(t)$ at time  $t$ . Then  $D$  grows at rate

$$\frac{dD(t)}{dt} = \delta S(t) + rD(t),$$

the first term on the right reflecting the influx of new dividends and the second term reflecting interest earned on dividends already accumulated. If  $S \sim \text{GBM}(\mu, \sigma^2)$ , then the drift in  $(S(t) + D(t))$  is

$$\mu S(t) + \delta S(t) + rD(t).$$

The martingale property (3.25), now applied to the combined process  $(S(t) +$  $D(t)$ , requires that this drift equal  $r(S(t) + D(t))$ . We must therefore have  $\mu + \delta = r$ ; i.e.,  $\mu = r - \delta$ . The net effect of a dividend yield is to reduce the growth rate by  $\delta$ .

We discuss some specific settings in which this formulation is commonly  $used:$ 

- o Equity Indices. In pricing index options, the level of the index is often modeled as geometric Brownian motion. An index is not an asset and it does not pay dividends, but the individual stocks that make up an index may pay dividends and this affects the level of the index. Because an index may contain many stocks paying a wide range of dividends on different dates, the combined effect is often approximated by a continuous dividend vield  $\delta$ .
- Exchange Rates. In pricing currency options, the relevant underlying variable is an exchange rate. We may think of an exchange rate  $S$  (quoted as the number of units of domestic currency per unit of foreign currency) as the price of the foreign currency. A unit of foreign currency earns interest at some risk-free rate  $r_f$ , and this interest may be viewed as a dividend stream. Thus, in modeling an exchange rate using geometric Brownian motion, we  $\text{set } \mu = r - r_f.$
- o Commodities. A physical commodity like gold or oil may in some cases behave like an asset that pays *negative* dividends because of the cost of storing the commodity. This is easily accommodated in the setting above by taking  $\delta < 0$ . There may, however, be some value in holding a physical commodity; for example, a party storing oil implicitly holds an option to sell or consume the oil in case of a shortage. This type of benefit is sometimes  $\text{approximated through a hypothetical }convenience \text{ yield that accrues from}$ physical storage. The net dividend yield in this case is the difference between the convenience yield and the cost rate for storage.
- o Futures Contracts. A futures contract commits the holder to buying an underlying asset or commodity at a fixed price at a fixed date in the future. The *futures price* is the price specified in a futures contract at which both

the buyer and the seller would willingly enter into the contract without either party paying the other. A futures price is thus not the price of an asset but rather a price agreed upon for a transaction in the future.

Let  $S(t)$  denote the price of the underlying asset (the spot price) and let  $F(t,T)$  denote the futures prices at time t for a contract to be settled at a fixed time T in the future. Entering into a futures contract at time t to buy the underlying asset at time  $T > t$  is equivalent to committing to exchange a known amount  $F(t,T)$  for an uncertain amount  $S(T)$ . For this contract to have zero value at the inception time  $t$  entails

$$0 = e^{-r(T-t)} \mathsf{E}[(S(T) - F(t,T))|\mathcal{F}_t],\tag{3.27}$$

where  $\mathcal{F}_t$  is the history of market prices up to time t. At  $t = T$  the spot and futures prices must agree, so  $S(T) = F(T,T)$  and we may rewrite this  $condition as$ 

$$F(t,T) = \mathsf{E}[F(T,T)|\mathcal{F}_t].$$

Thus, the futures price is a martingale (in its first argument) under the risk-neutral measure. It follows that if we choose to model a futures price (for fixed maturity  $T$ ) using geometric Brownian motion, we should set its drift parameter to zero:

$$\frac{dF(t,T)}{F(t,T)} = \sigma \, dW(t).$$

Comparison of  $(3.27)$  and  $(3.25)$  reveals that

$$F(t,T) = e^{(r-\delta)(T-t)}S(t),$$

with  $\delta$  the net dividend yield for S. If either process is a geometric Brownian motion under the risk-neutral measure then the other is as well and they have the same volatility  $\sigma$ .

This discussion blurs the distinction between futures and forward contracts. The argument leading to  $(3.27)$  applies more specifically to a forward price because a forward contract involves no intermediate cashflows. The holder of a futures contract typically makes or receives payments each day through a margin account; the discussion above ignores these cashflows. In a world with deterministic interest rates, futures and forward prices must be equal to preclude arbitrage so the conclusion in  $(3.27)$  is valid for both. With stochastic interest rates, it turns out that futures prices continue to be martingales under the risk-neutral measure but forward prices do not. The theoretical relation between futures and forward prices is investigated in  $\text{Cox, Ingersoll, and Ross [90]}; \text{ it is also discussed in many texts on derivative}$ securities (e.g., Hull  $[189]$ ).

# Path-Dependent Payoffs

We turn now to some examples of path-dependent payoffs frequently encountered in option pricing. We focus primarily on cases in which the payoff depends on the values  $S(t_1), \ldots, S(t_n)$  at a fixed set of dates  $t_1, \ldots, t_n$ ; for these it is usually possible to produce an unbiased simulation estimate of the option price. An option payoff could in principle depend on the complete path  $\{S(t), 0 \le t \le T\}$  over an interval  $[0, T]$ ; pricing such an option by simulation will often entail some discretization bias. In the examples that follow, we distinguish between discrete and continuous monitoring of the underlying  $\text{asset.}$ 

◦ Asian option: discrete monitoring. An Asian option is an option on a time average of the underlying asset. Asian calls and puts have payoffs  $(\bar{S}-K)^+$ and  $(K - \bar{S})^+$  respectively, where the strike price K is a constant and

$$\bar{S} = \frac{1}{n} \sum_{i=1}^{n} S(t_i) \tag{3.28}$$

is the average price of the underlying asset over the discrete set of monitoring dates  $t_1,\ldots,t_n$ . Other examples have payoffs  $(S(T)-\bar{S})^+$  and  $(\bar{S}-S(T))^+$ . There are no exact formulas for the prices of these options, largely because the distribution of  $\bar{S}$  is intractable.

◦ Asian option: continuous monitoring. The continuous counterparts of the discrete Asian options replace the discrete average above with the continuous average

$$\bar{S} = \frac{1}{t-u} \int_u^t S(\tau) \, d\tau$$

over an interval  $[u, t]$ . Though more difficult to simulate, some instances of continuous-average Asian options allow pricing through the transform analysis of Geman and Yor  $[135]$  and the eigenfunction expansion of Linet- $\text{sky } [237].$ 

 $\circ$  Geometric average option. Replacing the arithmetic average  $\bar{S}$  in (3.28) with

$$\left(\prod_{i=1}^{n} S(t_i)\right)^{1/n}$$

produces an option on the geometric average of the underlying asset price. Such options are seldom if ever found in practice, but they are useful as test cases for computational procedures and as a basis for approximating ordinary Asian options. They are mathematically convenient to work with because the geometric average of (jointly) lognormal random variables is itself lognormal. From (3.20) we find (with  $\mu$  replaced by r) that

$$\left(\prod_{i=1}^{n} S(t_i)\right)^{1/n} = S(0) \exp\left([r - \frac{1}{2}\sigma^2] \frac{1}{n} \sum_{i=1}^{n} t_i + \frac{\sigma}{n} \sum_{i=1}^{n} W(t_i)\right).$$

$$\sum_{i=1}^{n} W(t_i) \sim N\left(0, \sum_{i=1}^{n} (2i-1)t_{n+1-i}\right).$$

It follows that the geometric average of  $S(t_1), \ldots, S(t_n)$  has the same distribution as the value at time T of a process  $\text{GBM}(r-\delta,\bar{\sigma}^2)$  with

$$T = \frac{1}{n} \sum_{i=1}^{n} t_i, \quad \bar{\sigma}^2 = \frac{\sigma^2}{n^2 T} \sum_{i=1}^{n} (2i-1)t_{n+1-i}, \quad \delta = \frac{1}{2}\sigma^2 - \frac{1}{2}\bar{\sigma}^2.$$

An option on the geometric average may thus be valued using the Black-Scholes formula  $(1.44)$  for an asset paying a continuous dividend yield. The expression

$$\exp\left(\int_u^t \log S(\tau) \, d\tau\right)$$

is a continuously monitored version of the geometric average and is also lognormally distributed. Options on a continuous geometric average can similarly be priced in closed form.

o Barrier options. A typical example of a barrier option is one that gets "knocked out" if the underlying asset crosses a prespecified level. For instance, a *down-and-out call* with barrier b, strike  $K$ , and expiration  $T$  has payoff

$$\mathbf{1}\{\tau(b) > T\}(S(T) - K)^+,$$

where

$$\tau(b) = \inf\{t_i : S(t_i) < b\}$$

is the first time in  $\{t_1,\ldots,t_n\}$  the price of the underlying asset drops below b (understood to be  $\infty$  if  $S(t_i) > b$  for all i) and  $\mathbf{1} \{ \}$  denotes the indicator of the event in braces. A down-and-in call has payoff  $\mathbf{1}_{\{\tau(b) \leq T\}}(S(T)-K)^+$ : it gets "knocked in" only when the underlying asset crosses the barrier. Upand-out and up-and-in calls and puts are defined analogously. Some knockout options pay a rebate if the underlying asset crosses the barrier, with the rebate possibly paid either at the time of the barrier crossing or at the expiration of the option.

These examples of discretely monitored barrier options are easily priced by simulation through sampling of  $S(t_1), \ldots, S(t_n), S(T)$ . A continuously monitored barrier option is knocked in or out the instant the underlying asset crosses the barrier; in other words, it replaces  $\tau(b)$  as defined above with

$$\tilde{\tau}(b) = \inf\{t \ge 0 : S(t) \le b\}.$$

Both discretely monitored and continuously monitored barrier options are found in practice. Many continuously monitored barrier options can be priced in closed form; Merton [261] provides what is probably the first such formula and many other cases can be found in, e.g., Briys et al. [62]. Discretely monitored barrier options generally do not admit pricing formulas and hence require computational procedures.

o Lookback options. Like barrier options, lookback options depend on extremal values of the underlying asset price. Lookback puts and calls expiring at  $t_n$ have payoffs

$$(\max_{i=1,\dots,n} S(t_i) - S(t_n))$$
 and  $(S(t_n) - \min_{i=1,\dots,n} S(t_i))$ 

respectively. A lookback call, for example, may be viewed as the profit from buying at the lowest price over  $t_1, \ldots, t_n$  and selling at the final price  $S(t_n)$ . Continuously monitored versions of these options are defined by taking the maximum or minimum over an interval rather than a finite set of points.

### Incorporating a Term Structure

Thus far, we have assumed that the risk-free interest rate  $r$  is constant. This implies that the time-t price of a zero-coupon bond maturing (and paying 1) at time  $T > t$  is

$$B(t,T) = e^{-r(T-t)}.$$
(3.29)

Suppose however that at time 0 we observe a collection of bond prices  $B(0,T)$ , indexed by maturity T, incompatible with  $(3.29)$ . To price an option on an underlying asset price  $S$  consistent with the observed term structure of bond prices, we can introduce a deterministic but time-varying risk-free rate  $r(u)$ by setting

$$r(u) = -\frac{\partial}{\partial T} \log B(0, T) \Big|_{T=u}$$

Clearly, then,

$$B(0,T) = \exp\left(-\int_0^T r(u) \, du\right).$$

With a deterministic, time-varying risk-free rate  $r(u)$ , the dynamics of an asset price  $S(t)$  under the risk-neutral measure (assuming no dividends) are described by the  $SDE$ 

$$\frac{dS(t)}{S(t)} = r(t) dt + \sigma dW(t)$$

 $\text{with solution}$ 

$$S(t) = S(0) \exp\left(\int_0^t r(u) \, du - \frac{1}{2}\sigma^2 t + \sigma W(t)\right).$$

This process can be simulated over  $0 = t_0 < t_1 < \cdots < t_n$  by setting

a commente pambre i anno

$$S(t_{i+1}) = S(t_i) \exp\left(\int_{t_i}^{t_{i+1}} r(u) \, du - \frac{1}{2} \sigma^2(t_{i+1} - t_i) + \sigma \sqrt{t_{i+1} - t_i} Z_{i+1}\right),$$

with  $Z_1, \ldots, Z_n$  independent  $N(0, 1)$  random variables.

If in fact we are interested only in values of  $S(t)$  at  $t_1, \ldots, t_n$ , the simulation can be simplified, making it unnecessary to introduce a short rate  $r(u)$  at all. If we observe bond prices  $B(0,t_1),\ldots,B(0,t_n)$  (either directly or through interpolation from other observed prices), then since

$$\frac{B(0, t_i)}{B(0, t_{i+1})} = \exp\left(\int_{t_i}^{t_{i+1}} r(u) \, du\right),\,$$

we may simulate  $S(t)$  using

$$S(t_{i+1}) = S(t_i) \frac{B(0, t_i)}{B(0, t_{i+1})} \exp\left(-\frac{1}{2}\sigma^2(t_{i+1} - t_i) + \sigma\sqrt{t_{i+1} - t_i}Z_{i+1}\right). \tag{3.30}$$

# Simulating Off a Forward Curve

For some types of underlying assets, particularly commodities, we may observe not just a spot price  $S(0)$  but also a collection of forward prices  $F(0,T)$ . Here,  $F(0,T)$  denotes the price specified in a contract at time 0 to be paid at time T for the underlying asset. Under the risk-neutral measure,  $F(0,T) = \mathsf{E}[S(T)]$ ; in particular, the forward prices reflect the risk-free interest rate and any dividend yield (positive or negative) on the underlying asset. In pricing options, we clearly want to simulate price paths of the underlying asset consistent with the forward prices observed in the market.

The equality  $F(0,T) = \mathsf{E}[S(T)]$  implies

$$S(T) = F(0,T) \exp\left(-\frac{1}{2}\sigma^2 T + \sigma W(T)\right)$$

Given forward prices  $F(0, t_1), \ldots, F(0, t_n)$ , we can simulate using

$$S(t_{i+1}) = S(t_i) \frac{F(0, t_{i+1})}{F(0, t_i)} \exp\left(-\frac{1}{2}\sigma^2(t_{i+1} - t_i) + \sigma\sqrt{t_{i+1} - t_i}Z_{i+1}\right).$$

This generalizes (3.30) because in the absence of dividends we have  $F(0,T) =$  $S(0)/B(0,T)$ . Alternatively, we may define  $M(0) = 1$ ,

$$M(t_{i+1}) = M(t_i) \exp\left(-\frac{1}{2}\sigma^2(t_{i+1}-t_i) + \sigma\sqrt{t_{i+1}-t_i}Z_{i+1}\right), \ \ i = 0,\ldots,n-1,$$

and set  $S(t_i) = F(0, t_i)M(t_i), i = 1, \ldots, n.$ 

### Deterministic Volatility Functions

Although geometric Brownian motion remains an important benchmark, it has been widely observed across many markets that option prices are incompatible with a GBM model for the underlying asset. This has fueled research into alternative specifications of the dynamics of asset prices.

Consider a market in which several options with various strikes and maturities are traded simultaneously on the same underlying asset. Suppose the market is sufficiently liquid that we may effectively observe prices of the options without error. If the assumptions underlying the Black-Scholes formula held exactly, all of these option prices would result from using the same volatility parameter  $\sigma$  in the formula. In practice, one usually finds that this implied volatility actually varies with strike and maturity. It is therefore natural to seek a minimal modification of the Black-Scholes model capable of reproducing market prices.

Consider the extreme case in which we observe the prices  $C(K,T)$  of call options on a single underlying asset for a continuum of strikes  $K$  and maturities T. Dupire [107] shows that, subject only to smoothness conditions on C as a function of K and T, it is possible to find a function  $\sigma(S,t)$  such that the model  $\sim$ 

$$\frac{dS(t)}{S(t)} = r dt + \sigma(S(t), t) dW(t)$$

reproduces the given option prices, in the sense that

$$e^{-rT}\mathsf{E}[(S(T)-K)^{+}] = C(K,T)$$

for all  $K$  and  $T$ . This is sometimes called a *deterministic volatility function* to emphasize that it extends geometric Brownian motion by allowing  $\sigma$  to be a deterministic function of the current level of the underlying asset. This feature is important because it ensures that options can still be hedged through a position in the underlying asset, which would not be the case in a stochastic volatility model.

In practice, we observe only a finite set of option prices and this leaves a great deal of flexibility in specifying  $\sigma(S,t)$  while reproducing market prices. We may, for example, impose smoothness constraints on the choice of volatility function. This function will typically be the result of a numerical optimization procedure and may never be given explicitly.

Once  $\sigma(S,t)$  has been chosen to match a set of actively traded options, simulation may still be necessary to compute the prices of less liquid pathdependent options. In general, there is no exact simulation procedure for these models and it is necessary to use an Euler scheme of the form

$$S(t_{i+1}) = S(t_i) \left( 1 + r(t_{i+1} - t_i) + \sigma(S(t_i), t_i) \sqrt{t_{i+1} - t_i} Z_{i+1} \right),$$

with  $Z_1, Z_2, \ldots$  independent standard normals, or

$$S(t_{i+1}) =$$
  
$$S(t_i) \exp\left( [r - \frac{1}{2}\sigma^2(S(t_i), t_i)](t_{i+1} - t_i) + \sigma(S(t_i), t_i)\sqrt{t_{i+1} - t_i}Z_{i+1} \right),$$

which is equivalent to an Euler scheme for  $\log S(t)$ .

o Generating Bample Faths  $\mathbf{1} \mathbf{0} \mathbf{1}$ 

### 3.2.3 Multiple Dimensions

A multidimensional geometric Brownian motion can be specified through a system of SDEs of the form

$$\frac{dS_i(t)}{S_i(t)} = \mu_i \, dt + \sigma_i \, dX_i(t), \quad i = 1, \dots, d,\tag{3.31}$$

where each  $X_i$  is a standard one-dimensional Brownian motion and  $X_i(t)$ and  $X_i(t)$  have correlation  $\rho_{ij}$ . If we define a  $d \times d$  matrix  $\Sigma$  by setting  $\Sigma_{ij} = \sigma_i \sigma_j \rho_{ij}$ , then  $(\sigma_1 X_1, \ldots, \sigma_d X_d) \sim \text{BM}(0, \Sigma)$ . In this case we abbreviate the process  $S = (S_1, \ldots, S_d)$  as  $\text{GBM}(\mu, \Sigma)$  with  $\mu = (\mu_1, \ldots, \mu_d)$ . In a convenient abuse of terminology, we refer to  $\mu$  as the drift vector of S, to  $\Sigma$  as its covariance matrix and to the matrix with entries  $\rho_{ij}$  as its correlation matrix; the actual drift vector is  $(\mu_1 S_1(t), \ldots, \mu_d S_d(t))$  and the covariances are given by

$$\text{Cov}[S_i(t), S_j(t)] = S_i(0)S_j(0)e^{(\mu_i + \mu_j)t} \left( e^{\rho_{ij}\sigma_i\sigma_j} - 1 \right).$$

This follows from the representation

$$S_i(t) = S_i(0)e^{(\mu_i - \frac{1}{2}\sigma_i^2)t + \sigma_i X_i(t)}, \quad i = 1, \dots, d$$

Recall that a Brownian motion  $\text{BM}(0,\Sigma)$  can be represented as  $AW(t)$ with W a standard Brownian motion  $\text{BM}(0, I)$  and A any matrix for which  $AA^{\top} = \Sigma$ . We may apply this to  $(\sigma_1 X_1, \ldots, \sigma_d X_d)$  and rewrite (3.31) as

$$\frac{dS_i(t)}{S_i(t)} = \mu_i \, dt + a_i \, dW(t), \quad i = 1, \dots, d,\tag{3.32}$$

with  $a_i$  the *i*th row of A. A bit more explicitly, this is

$$\frac{dS_i(t)}{S_i(t)} = \mu_i \, dt + \sum_{j=1}^d A_{ij} \, dW_j(t), \quad i = 1, \dots, d.$$

This representation leads to a simple algorithm for simulating  $\text{GBM}(\mu, \Sigma)$ at times  $0 = t_0 < t_1 < \cdots < t_n$ :

$$S_i(t_{k+1}) = S_i(t_k)e^{(\mu_i - \frac{1}{2}\sigma_i^2)(t_{k+1} - t_k) + \sqrt{t_{k+1} - t_k} \sum_{j=1}^d A_{ij} Z_{k+1,j}}, \quad i = 1, \dots, d,$$
(3.33)

 $k = 0, \ldots, n-1$ , where  $Z_k = (Z_{k1}, \ldots, Z_{kd}) \sim N(0, I)$  and  $Z_1, Z_2, \ldots, Z_n$ are independent. As usual, choosing A to be the Cholesky factor of  $\Sigma$  can reduce the number of multiplications and additions required at each step. Notice that  $(3.33)$  is essentially equivalent to exponentiating both sides of the ecursion (3.15); indeed, all methods for simulating  $\text{BM}(\mu, \Sigma)$  provide methods or simulating  $\text{GBM}(\mu, \Sigma)$  (after replacement of  $\mu_i$  by  $\mu_i - \frac{1}{2}\sigma_i^2$ ).

The discussion of the choice of the drift parameter  $\mu$  in Section 3.2.2 applies qually well to each  $\mu_i$  in pricing options on multiple underlying assets. Often,

 $\mu_i = r - \delta_i$  where r is the risk-free interest rate and  $\delta_i$  is the dividend yield on the *i*th asset  $S_i$ .

We list a few examples of option payoffs depending on multiple assets:

 $\circ$  Spread option. A call option on the spread between two assets  $S_1$ ,  $S_2$  has payoff

$$([S_1(T) - S_2(T)] - K)^+$$

with  $K$  a strike price. For example, *crack spread* options traded on the New York Mercantile Exchange are options on the spread between heating oil and crude oil futures.

o Basket option. A basket option is an option on a portfolio of underlying assets and has a payoff of, e.g.,

$$([c_1S_1(T) + c_2S_2(T) + \cdots + c_dS_d(T)] - K)^+$$

Typical examples would be options on a portfolio of related assets  $-$  bank stocks or Asian currencies, for instance.

○ *Outperformance option.* These are options on the maximum or minimum of multiple assets and have payoffs of, e.g., the form

$$(\max\{c_1S_1(T), c_2S_2(T), \cdots, c_dS_d(T)\} - K)^+.$$

 $\circ$  Barrier options. A two-asset barrier option may have a payoff of the form

$$\mathbf{1}\{\min_{i=1,\ldots,n} S_2(t_i) < b\}(K - S_1(T))^+;$$

This is a down-and-in put on  $S_1$  that knocks in when  $S_2$  drops below a barrier at  $b$ . Many variations on this basic structure are possible. In this example, one may think of  $S_1$  as an individual stock and  $S_2$  as the level of an equity index: the put on the stock is knocked in only if the market drops.

 $\circ$  Quantos. Quantos are options sensitive both to a stock price and an exchange rate. For example, consider an option to buy a stock denominated in a foreign currency with the strike price fixed in the foreign currency but the payoff of the option to be made in the domestic currency. Let  $S_1$  denote the stock price and  $S_2$  the exchange rate, expressed as the quantity of domestic currency required per unit of foreign currency. Then the payoff of the option in the domestic currency is given by

$$S_2(T)(S_1(T) - K)^{+}. \t\t(3.34)$$

The payoff

έ.

$$\left(S_1(T) - \frac{K}{S_2(T)}\right)^+$$

corresponds to a quanto in which the level of the strike is fixed in the domestic currency and the payoff of the option is made in the foreign currency.

# Change of Numeraire

The pricing of an option on two or more underlying assets can sometimes be transformed to a problem with one less underlying asset (and thus to a lower-dimensional problem) by choosing one of the assets to be the numeraire. Consider, for example, an option to exchange a basket of assets for another asset with payoff

$$\left(\sum_{i=1}^{d-1} c_i S_i(T) - c_d S_d(T)\right)^+,$$

for some constants  $c_i$ . The price of the option is given by

$$e^{-rT} \mathsf{E} \left[ \left( \sum_{i=1}^{d-1} c_i S_i(T) - c_d S_d(T) \right)^+ \right], \tag{3.35}$$

the expectation taken under the risk-neutral measure. Recall that this is the measure associated with the numeraire asset  $\beta(t) = e^{rt}$  and is characterized by the property that the processes  $S_i(t)/\beta(t)$ ,  $i = 1, \ldots, d$ , are martingales under this measure.

As explained in Section 1.2.3, choosing a different asset as numeraire  $$ say  $S_d$  — means switching to a probability measure under which the processes  $S_i(t)/S_d(t), i = 1, \ldots, d-1, \text{ and } \beta(t)/S_d(t)$  are martingales. More precisely, if we let  $P_{\beta}$  denote the risk-neutral measure, the new measure  $P_{S_d}$  is defined by the likelihood ratio process (cf. Appendix  $B.4$ )

$$\left(\frac{dP_{S_d}}{dP_{\beta}}\right)_t = \frac{S_d(t)}{\beta(t)} \frac{\beta(0)}{S_d(0)}.\n$$
(3.36)

Through this change of measure, the option price  $(3.35)$  can be expressed  $\text{as}$ 

$$\begin{split} e^{-rT} \mathsf{E}_{S_d} \left[ \left( \sum_{i=1}^{d-1} c_i S_i(T) - c_d S_d(T) \right)^+ \left( \frac{dP_\beta}{dP_{S_d}} \right)_T \right] \\ &= e^{-rT} \mathsf{E}_{S_d} \left[ \left( \sum_{i=1}^{d-1} c_i S_i(T) - c_d S_d(T) \right)^+ \left( \frac{\beta(T) S_d(0)}{S_d(T) \beta(0)} \right) \right] \\ &= S_d(0) \mathsf{E}_{S_d} \left[ \left( \sum_{i=1}^{d-1} c_i \frac{S_i(T)}{S_d(T)} - c_d \right)^+ \right], \end{split}$$

with  $\mathsf{E}_{S_d}$  denoting expectation under  $P_{S_d}$ . From this representation it becomes clear that only the  $d-1$  ratios  $S_i(T)/S_d(T)$  (and the constant  $S_d(0)$ ) are needed to price this option under the new measure. We thus need to determine the dynamics of these ratios under the new measure.

Using  $(3.32)$  and  $(3.36)$ , we find that

9

$$\left(\frac{dP_{S_d}}{dP_{\beta}}\right)_t = \exp\left(-\frac{1}{2}\sigma_d^2 + a_d W(t)\right).$$

 $Girsanov's Theorem$  (see Appendix B.4) now implies that the process

$$W^d(t) = W(t) - a_d^\top t$$

is a standard Brownian motion under  $P_{S_d}$ . Thus, the effect of changing numeraire is to add a drift  $a^{\top}$  to W. The ratio  $S_i(t)/S_d(t)$  is given by

$$\begin{split} \frac{S_i(t)}{S_d(t)} &= \frac{S_i(0)}{S_d(0)} \exp\left(-\frac{1}{2}\sigma_i^2 t + \frac{1}{2}\sigma_d^2 t + (a_i - a_d)W(t)\right) \\ &= \frac{S_i(0)}{S_d(0)} \exp\left(-\frac{1}{2}\sigma_i^2 t + \frac{1}{2}\sigma_d^2 t + (a_i - a_d)(W^d(t) + a_d^\top)\right) \\ &= \frac{S_i(0)}{S_d(0)} \exp\left(-\frac{1}{2}(a_i - a_d)(a_i - a_d)^\top + (a_i - a_d)W^d(t)\right), \end{split}$$

using the identities  $a_j a_j^{\top} = \sigma_j^2$ ,  $j = 1, \ldots, d$ , from the definition of the  $a_j$  in (3.32). Under  $P_{S_d}$ , the scalar process  $(a_i - a_d)W^d(t)$  is a Brownian motion with drift 0 and diffusion coefficient  $(a_i - a_d)(a_i - a_d)^{\top}$ . This verifies that the ratios  $S_i/S_d$  are martingales under  $P_{S_d}$  and also that  $(S_1/S_d,\ldots,S_{d-1}/S_d)$ remains a multivariate geometric Brownian motion under the new measure. It is thus possible to price the option by simulating just this  $(d-1)$ -dimensional process of ratios rather than the original  $d$ -dimensional process of asset prices.

This device would not have been effective in the example above if the payoff in  $(3.35)$  had instead been

$$\left(\sum_{i=1}^{d} c_i S_i(T) - K\right)^+$$

with K a constant. In this case, dividing through by  $S_d(T)$  would have produced a term  $K/S_d(T)$  and would thus have required simulating this ratio as well as  $S_i/S_d$ ,  $i = 1, \ldots, d-1$ . What, then, is the scope of this method? If the payoff of an option is given by  $g(S_1(T), \ldots, S_d(T))$ , then the property we need is that  $g$  be homogeneous of degree 1, meaning that

$$g(\alpha x_1,\ldots,\alpha x_d)=\alpha g(x_1,\ldots,x_d)$$

for all scalars  $\alpha$  and all  $x_1, \ldots, x_d$ . For in this case we have

$$\frac{g(S_1(T),\ldots,S_d(T))}{S_d(T)} = g(S_1(T)/S_d(T),\ldots,S_{d-1}(T)/S_d(T),1)$$

and taking one of the underlying assets as numeraire does indeed reduce by one the relevant number of underlying stochastic variables. See Jamshidian  $[197]$  for a more general development of this observation.

Concreasing Nample 1 aulis

# 3.3 Gaussian Short Rate Models

This section and the next develop methods for simulating some simple but important stochastic interest rate models. These models posit the dynamics of an instantaneous continuously compounded short rate  $r(t)$ . An investment in a money market account earning interest at rate  $r(u)$  at time u grows from  $\text{a value of 1 at time 0 to a value of}$ 

$$\beta(t) = \exp\left(\int_0^t r(u) \, du\right)$$

at time  $t$ . Though this is now a stochastic quantity, it remains the numeraire for risk-neutral pricing. The price at time 0 of a derivative security that pays X at time T is the expectation of  $X/\beta(T)$ , i.e.,

$$\mathsf{E}\left[\exp\left(-\int_0^T r(u)\,du\right)X\right],\tag{3.37}$$

the expectation taken with respect to the risk-neutral measure. In particular, the time-0 price of a bond paying 1 at  $T$  is given by

$$B(0,T) = \mathsf{E}\left[\exp\left(-\int_0^T r(u) \, du\right)\right].\tag{3.38}$$

We focus primarily on the dynamics of the short rate under the risk-neutral measure.

The Gaussian models treated in this section offer a high degree of tractability. Many simple instruments can be priced in closed form in these models or using deterministic numerical methods. Some extensions of the basic models and some pricing applications do, however, require simulation for the calculation of expressions of the form  $(3.37)$ . The tractability of the models offers opportunities for increasing the accuracy of simulation.

# 3.3.1 Basic Models and Simulation

The classical model of Vasicek  $[352]$  describes the short rate through an Ornstein-Uhlenbeck process (cf. Karatzas and Shreve [207], p.358)

$$dr(t) = \alpha(b - r(t)) dt + \sigma dW(t). \tag{3.39}$$

Here, W is a standard Brownian motion and  $\alpha$ , b, and  $\sigma$  are positive constants. Notice that the drift in (3.39) is positive if  $r(t) < b$  and negative if  $r(t) > b$ ; thus,  $r(t)$  is pulled toward level b, a property generally referred to as mean *reversion.* We may interpret b as a long-run interest rate level and  $\alpha$  as the speed at which  $r(t)$  is pulled toward b. The mean-reverting form of the drift is

an essential feature of the Ornstein-Uhlenbeck process and thus of the Vasicek  $model.$ 

The continuous-time Ho-Lee model [185] has

$$dr(t) = g(t) dt + \sigma dW(t) \tag{3.40}$$

with  $g$  a deterministic function of time. Both (3.39) and (3.40) define Gaussian processes, meaning that the joint distribution of  $r(t_1), \ldots, r(t_n)$  is multivariate normal for any  $t_1, \ldots, t_n$ . Both define Markov processes and are special cases of the general Gaussian Markov process specified by

$$dr(t) = [g(t) + h(t)r(t)] dt + \sigma(t) dW(t), \qquad (3.41)$$

with g, h, and  $\sigma$  all deterministic functions of time. Natural extensions of  $(3.39)$  and  $(3.40)$  thus allow  $\sigma$ , b, and  $\alpha$  to vary with time. Modeling with the Vasicek model when  $b$  in particular is time-varying is discussed in Hull and White [190].

The SDE  $(3.41)$  has solution

$$r(t) = e^{H(t)}r(0) + \int_0^t e^{H(t) - H(s)}g(s) \, ds + \int_0^t e^{H(t) - H(s)}\sigma(s) \, dW(s),$$

with

$$H(t) = \int_0^t h(s) \, ds,$$

as can be verified through an application of Itô's formula. Because this produces a Gaussian process, simulation of  $r(t_1), \ldots, r(t_n)$  is a special case of the general problem of sampling from a multivariate normal distribution, treated in Section 2.3. But it is a sufficiently interesting special case to merit consideration. To balance tractability with generality, we will focus on the Vasicek model (3.39) with time-varying  $b$  and on the Ho-Lee model (3.40). Similar ideas apply to the general case  $(3.41)$ .

# Simulation

For the Vasicek model with time-varying  $b$ , the general solution above specializes to

$$r(t) = e^{-\alpha t} r(0) + \alpha \int_0^t e^{-\alpha(t-s)} b(s) \, ds + \sigma \int_0^t e^{-\alpha(t-s)} \, dW(s). \tag{3.42}$$

Similarly, for any  $0 < u < t$ ,

$$r(t) = e^{-\alpha(t-u)}r(u) + \alpha \int_u^t e^{-\alpha(t-s)}b(s) ds + \sigma \int_u^t e^{-\alpha(t-s)} dW(s).$$

From this it follows that, given  $r(u)$ , the value  $r(t)$  is normally distributed with mean

$$e^{-\alpha(t-u)}r(u) + \mu(u,t), \quad \mu(u,t) \equiv \alpha \int_u^t e^{-\alpha(t-s)}b(s) \, ds \tag{3.43}$$

and variance

. 1

$$\sigma_r^2(u,t) \equiv \sigma^2 \int_u^t e^{-2\alpha(t-s)} ds = \frac{\sigma^2}{2\alpha} \left(1 - e^{-2\alpha(t-u)}\right). \tag{3.44}$$

To simulate r at times  $0 = t_0 < t_1 < \cdots < t_n$ , we may therefore set

$$r(t_{i+1}) = e^{-\alpha(t_{i+1} - t_i)} r(t_i) + \mu(t_i, t_{i+1}) + \sigma_r(t_i, t_{i+1}) Z_{i+1}, \qquad (3.45)$$

with  $Z_1, \ldots, Z_n$  independent draws from  $N(0, 1)$ .

This algorithm is an exact simulation in the sense that the distribution of the  $r(t_1), \ldots, r(t_n)$  it produces is precisely that of the Vasicek process at times  $t_1,\ldots,t_n$  for the same value of  $r(0)$ . In contrast, the slightly simpler  $Euler$  scheme

$$r(t_{i+1}) = r(t_i) + \alpha(b(t_i) - r(t_i))(t_{i+1} - t_i) + \sigma\sqrt{t_{i+1} - t_i}Z_{i+1}$$

entails some discretization error. Exact simulation of the Ho-Lee process  $(3.40)$ is a special case of the method in  $(3.4)$  for simulating a Brownian motion with time-varying drift.

In the special case that  $b(t) \equiv b$ , the algorithm in (3.45) simplifies to

$$r(t_{i+1}) = e^{-\alpha(t_{i+1}-t_i)}r(t_i) + b(1 - e^{-\alpha(t_{i+1}-t_i)}) + \sigma\sqrt{\frac{1}{2\alpha}\left(1 - e^{-2\alpha(t_{i+1}-t_i)}\right)}Z_{i+1}.$$
(3.46)

The Euler scheme is then equivalent to making the approximation  $e^x \approx 1 + x$ for the exponentials in this recursion.

Evaluation of the integral defining  $\mu(t_i, t_{i+1})$  and required in (3.45) may seem burdensome. The effort involved in evaluating this integral clearly depends on the form of the function  $b(t)$  so it is worth discussing how this function is likely to be specified in practice. Typically, the flexibility to make  $b$  vary with time is used to make the dynamics of the short rate consistent with an observed term structure of bond prices. The same is true of the function  $g$  in the Ho-Lee model (3.40). We return to this point in Section 3.3.2, where we discuss bond prices in Gaussian models.

# Stationary Version

Suppose  $b(t) \equiv b$  and  $\alpha > 0$ . Then from (3.43) we see that

$$\mathsf{E}[r(t)] = e^{-\alpha t} r(0) + (1 - e^{-\alpha t})b \to b \quad \text{as } t \to \infty,$$

so the process  $r(t)$  has a limiting mean. It also has a limiting variance given  $(via (3.44))$  by

3.3 Gaussian Short Rate Models 111

$$\lim_{t \to \infty} \text{Var}[r(t)] = \lim_{t \to \infty} \frac{\sigma^2}{2\alpha} \left( 1 - e^{-2\alpha t} \right) = \frac{\sigma^2}{2\alpha}$$

In fact,  $r(t)$  converges in distribution to a normal distribution with this mean and variance, in the sense that for any  $x \in \Re$ 

$$P(r(t) \le x) \to \Phi\left(\frac{x-b}{\sigma/\sqrt{2\alpha}}\right),$$

with  $\Phi$  the standard normal distribution. The fact that  $r(t)$  has a limiting distribution is a reflection of the stabilizing effect of mean reversion in the drift and contrasts with the long-run behavior of, for example, geometric Brownian motion.

The limiting distribution of  $r(t)$  is also a stationary distribution in the sense that if  $r(0)$  is given this distribution then every  $r(t)$ ,  $t > 0$ , has this distribution as well. Because  $(3.46)$  provides an exact discretization of the process, the  $N(b, \sigma^2/2\alpha)$  distribution is also stationary for the discretized process. To simulate a stationary version of the process, it therefore suffices to draw  $r(0)$  from this normal distribution and then proceed as in (3.46).

# 3.3.2 Bond Prices

As already noted, time-dependent drift parameters are typically used to make a short rate model consistent with an observed set of bond prices. Implementation of the simulation algorithm  $(3.45)$  is thus linked to the *calibration* of the model through the choice of the function  $b(t)$ . The same applies to the function  $g(t)$  in the Ho-Lee model and as this case is slightly simpler we consider it first.

Our starting point is the bond-pricing formula (3.38). The integral of  $r(u)$ from 0 to T appearing in that formula is normally distributed because  $r(u)$ is a Gaussian process. It follows that the bond price is the expectation of the exponential of a normal random variable. For a normal random variable  $X \sim N(m, v^2)$ , we have  $E[\exp(X)] = \exp(m + (v^2/2))$ , so

$$\mathsf{E}\left[\exp\left(-\int_0^T r(t)\,dt\right)\right] = \exp\left(-\mathsf{E}\left[\int_0^T r(t)\,dt\right] + \tfrac{1}{2}\mathsf{Var}\left[\int_0^T r(t)\,dt\right]\right). \tag{3.47}$$

To find the price of the bond we therefore need to find the mean and variance of the integral of the short rate.

In the Ho-Lee model, the short rate is given by

$$r(t) = r(0) + \int_0^t g(s) ds + \sigma W(t)$$

and its integral by

$$\int_0^T r(u) \, du = r(0)T + \int_0^T \int_0^u g(s) \, ds \, du + \sigma \int_0^T W(u) \, du.$$

This integral has mean

$$r(0)T + \int_0^T \int_0^u g(s) \, ds \, du$$

and variance

$$\begin{split} \operatorname{Var}\left[\sigma \int_{0}^{T} W(u) \, du\right] &= 2\sigma^{2} \int_{0}^{T} \int_{0}^{t} \operatorname{Cov}[W(u), W(t)] \, du \, dt \\ &= 2\sigma^{2} \int_{0}^{T} \int_{0}^{t} u \, du \, dt \\ &= \frac{1}{3}\sigma^{2} T^{3}. \end{split} \tag{3.48}$$

Substituting these expressions in  $(3.47)$ , we get

$$B(0,T) = \mathsf{E}\left[\exp\left(-\int_0^T r(u) \, du\right)\right]$$
  
=  $\exp\left(-r(0)T - \int_0^T \int_0^u g(s) \, ds \, du + \frac{\sigma^2 T^3}{6}\right).$ 

If we are given a set of bond prices  $B(0,T)$  at time 0, our objective is to choose the function  $q$  so that this equation holds.

To carry this out we can write

$$B(0,T) = \exp\left(-\int_0^T f(0,t) \, dt\right),\,$$

with  $f(0,t)$  the instantaneous forward rate for time t as of time 0 (cf. Appendix C). The initial forward curve  $f(0,T)$  captures the same information as the initial bond prices. Equating the two expressions for  $B(0,T)$  and taking logarithms, we find that

$$r(0)T + \int_0^T \int_0^u g(s) \, ds \, du - \frac{\sigma^2 T^3}{6} = \int_0^T f(0, t) \, dt.$$

Differentiating twice with respect to the maturity argument  $T$ , we find that

$$g(t) = \left. \frac{\partial}{\partial T} f(0, T) \right|_{T=t} + \sigma^2 t. \tag{3.49}$$

Thus, bond prices produced by the Ho-Lee model will match a given set of bond prices  $B(0,T)$  if the function g is tied to the initial forward curve  $f(0,T)$ in this way; i.e., if we specify

3.3 Gaussian Short Rate Models 113

$$dr(t) = \left(\left.\frac{\partial}{\partial T}f(0,T)\right|_{T=t} + \sigma^2 t\right)dt + \sigma dW(t). \tag{3.50}$$

A generic simulation of the Ho-Lee model with drift function  $g$  can be written as

$$r(t_{i+1}) = r(t_i) + \int_{t_i}^{t_{i+1}} g(s) \, ds + \sigma \sqrt{t_{i+1} - t_i} Z_{i+1},$$

with  $Z_1, Z_2, \ldots$  independent  $N(0,1)$  random variables. With  $g$  chosen as in  $(3.49)$ , this simplifies to

$$r(t_{i+1}) = r(t_i) + [f(0, t_{i+1}) - f(0, t_i)] + \frac{\sigma^2}{2} [t_{i+1}^2 - t_i^2] + \sigma \sqrt{t_{i+1} - t_i} Z_{i+1}.$$

Thus, no integration of the drift function  $q$  is necessary; to put it another way, whatever integration is necessary must already have been dealt with in choosing the forward curve  $f(0,t)$  to match a set of bond prices.

The situation is even simpler if we require that our simulated short rate be consistent only with bonds maturing at the simulation times  $t_1, \ldots, t_n$ . To satisfy this requirement we can weaken  $(3.49)$  to the condition that

$$\int_{t_i}^{t_{i+1}} g(s) \, ds = f(0, t_{i+1}) - f(0, t_i) + \frac{\sigma^2}{2} [t_{i+1}^2 - t_i^2].$$

Except for this constraint, the choice of  $g$  is immaterial — we could take it to be continuous and piecewise linear, for example. In fact, we never even need to specify g because only its integral over the intervals  $(t_i, t_{i+1})$  influence the values of  $r$  on the time grid  $t_1, \ldots, t_n$ .

# Bonds in the Vasicek Model

٠

A similar if less explicit solution applies to the Vasicek model. The integral of the short rate is again normally distributed; we need to find the mean and variance of this integral to find the price of a bond using  $(3.47)$ . Using  $(3.42)$ , for the mean we get

$$\mathsf{E}\left[\int_0^T r(t) \, dt\right] = \int_0^T \mathsf{E}[r(t)] \, dt$$
$$= \frac{1}{\alpha} (1 - e^{-\alpha T}) r(0) + \alpha \int_0^T \int_0^t e^{-\alpha(t-s)} b(s) \, ds \, dt. \tag{3.51}$$

For the variance we have

$$\operatorname{Var}\left[\int_{0}^{T} r(t) dt\right] = 2 \int_{0}^{T} \int_{0}^{t} \operatorname{Cov}[r(t), r(u)] du dt. \tag{3.52}$$

Community Namble Fallis

From (3.42) we get, for  $u \leq t$ ,

$$\begin{split} \mathsf{Cov}[r(t), r(u)] &= \sigma^2 \int_0^u e^{-\alpha(t-s)} e^{-\alpha(u-s)} \, ds \\ &= \frac{\sigma^2}{2\alpha} \left( e^{\alpha(u-t)} - e^{-\alpha(u+t)} \right). \end{split} \tag{3.53}$$

Integrating two more times as required for  $(3.52)$  gives

$$\operatorname{Var}\left[\int_{0}^{T} r(t) dt\right] = \frac{\sigma^{2}}{\alpha^{2}} \left[T + \frac{1}{2\alpha} \left(1 - e^{-2\alpha T}\right) + \frac{2}{\alpha} \left(e^{-\alpha T} - 1\right)\right]. \tag{3.54}$$

By combining  $(3.51)$  and  $(3.54)$  as in  $(3.47)$ , we arrive at an expression for the bond price  $B(0,T)$ .

Observe that (3.54) does not depend on  $r(0)$  and (3.51) is a linear transformation of  $r(0)$ . If we set

$$A(t,T) = \frac{1}{\alpha} \left( 1 - e^{-\alpha(T-t)} \right)$$

and

$$\begin{split} C(t,T) &= -\alpha \int_t^T \int_t^u e^{-\alpha(u-s)} b(s) \, ds \, du \\ &+ \frac{\sigma^2}{2\alpha^2} \left[ (T-t) + \frac{1}{2\alpha} \left( 1 - e^{-2\alpha(T-t)} \right) + \frac{2}{\alpha} \left( e^{-\alpha(T-t)} - 1 \right) \right], \end{split}$$

then substituting  $(3.51)$  and  $(3.54)$  in  $(3.47)$  produces

$$B(0,T) = \exp(-A(0,T)r(0) + C(0,T)).$$

In fact, the same calculations show that

$$B(t,T) = \exp(-A(t,T)r(t) + C(t,T)). \tag{3.55}$$

In particular,  $\log B(t,T)$  is a linear transformation of  $r(t)$ . This feature has been generalized by Brown and Schaefer [71] and Duffie and Kan [101] to what is generally referred to as the *affine class* of interest rate models.

As in our discussion of the Ho-Lee model, the function  $b(s)$  can be chosen to match a set of prices  $B(0,T)$  indexed by T. If we are concerned only with matching a finite set of bond prices  $B(0, t_1), \ldots, B(0, t_n)$ , then only the values of the integrals

$$\int_{t_i}^{t_{i+1}} e^{-\alpha(t_{i+1}-s)} b(s) \, ds$$

need to be specified. These are precisely the terms  $\mu(t_i, t_{i+1})$  needed in the simulation algorithm  $(3.45)$ . Thus, these integrals are by-products of fitting the model to a term structure and not additional computations required solely for the simulation.

# Joint Simulation with the Discount Factor

Most applications that call for simulation of a short rate process  $r(t)$  also require values of the discount factor

$$\frac{1}{\beta(t)} = \exp\left(-\int_0^t r(u) \, du\right)$$

or, equivalently, of

$$Y(t) = \int_0^t r(u) \, du.$$

Given values  $r(0), r(t_1), \ldots, r(t_n)$  of the short rate, one can of course generate approximate values of  $Y(t_i)$  using

$$\sum_{j=1}^{i} r(t_{j-1})[t_j - t_{j-1}], \quad t_0 = 0,$$

or some other approximation to the time integral. But in a Gaussian model, the pair  $(r(t), Y(t))$  are jointly Gaussian and it is often possible to simulate paths of the pair without discretization error. To carry this out we simply need to find the means, variances, and covariance of the increments of  $r(t)$ and  $Y(t)$ .

We have already determined (see (3.45)) that, given  $r(t_i)$ ,

$$r(t_{i+1}) \sim N\left(e^{-\alpha(t_{i+1}-t_i)}r(t_i) + \mu(t_i, t_{i+1}), \sigma_r^2(t_i, t_{i+1})\right).$$

From the same calculations used in (3.51) and (3.54), we find that, given  $r(t_i)$ and  $Y(t_i)$ ,

$$Y(t_{i+1}) \sim N(Y(t_i) + \mu_Y(t_i, t_{i+1}), \sigma_Y^2(t_i, t_{i+1})),$$

with

$$\mu_Y(t_i, t_{i+1}) = \frac{1}{\alpha} \left( 1 - e^{-\alpha(t_{i+1} - t_i)} \right) r(t_i) + \alpha \int_{t_i}^{t_{i+1}} \int_{t_i}^u e^{-\alpha(u - s)} b(s) \, ds \, du$$

 $\text{and}$ 

$$\sigma_Y^2(t_i, t_{i+1}) = \frac{\sigma^2}{\alpha^2} \left( (t_{i+1} - t_i) + \frac{1}{2\alpha} \left( 1 - e^{-2\alpha(t_{i+1} - t_i)} \right) + \frac{2}{\alpha} \left( e^{-\alpha(t_{i+1} - t_i)} - 1 \right) \right).$$

It only remains to determine the conditional covariance between  $r(t_{i+1})$ and  $Y(t_{i+1})$  given  $(r(t_i), Y(t_i))$ . For this we proceed as follows:

3

$$\begin{split} \operatorname{Cov}\left[r(t),Y(t)\right] &= \int_0^t \operatorname{Cov}\left[r(t),r(u)\right] du \\ &= \frac{\sigma^2}{2\alpha} \int_0^t e^{\alpha(u-t)} - e^{-\alpha(u+t)} \, du \\ &= \frac{\sigma^2}{2\alpha^2} \left[1 + e^{-2\alpha t} - 2e^{-\alpha t}\right]. \end{split}$$

The required covariance is thus given by

$$\sigma_{rY}(t_i, t_{i+1}) = \frac{\sigma^2}{2\alpha} \left[ 1 + e^{-2\alpha(t_{i+1} - t_i)} - 2e^{-\alpha(t_{i+1} - t_i)} \right].$$

The corresponding correlation is

$$\rho_{rY}(t_i, t_{i+1}) = \frac{\sigma_{rY}(t_i, t_{i+1})}{\sigma_r(t_i, t_{i+1})\sigma_Y(t_i, t_{i+1})}$$

With this notation, the pair  $(r, Y)$  can be simulated at times  $t_1, \ldots, t_n$  without discretization error using the following algorithm:

$$r(t_{i+1}) = e^{-\alpha(t_{i+1}-t_i)}r(t_i) + \mu(t_i, t_{i+1}) + \sigma_r(t_i, t_{i+1})Z_1(i+1)$$
  

$$Y(t_{i+1}) = Y(t_i) + \mu_Y(t_i, t_{i+1}) + \sigma_Y(t_i, t_{i+1})[\rho_{rY}(t_i, t_{i+1})Z_1(i+1) + \sqrt{1 - \rho_{rY}^2(t_i, t_{i+1})}Z_2(i+1)],$$

where  $(Z_1(i), Z_2(i))$ ,  $i = 1, \ldots, n$ , are independent standard bivariate normal random vectors.

# Change of Numeraire

Thus far, we have considered the dynamics of the short rate  $r(t)$  only under the risk-neutral measure. Recall that the numeraire asset associated with the risk-neutral measure is  $\beta(t) = \exp(\int_0^t r(u) \, du)$  and the defining feature of this probability measure is that it makes the discounted bond prices  $B(t,T)/\beta(t)$ martingales. In fact, the dynamics of the bond prices under the Gaussian models we have considered are of the form (for fixed  $T$ )

$$\frac{dB(t,T)}{B(t,T)} = r(t) dt - A(t,T)\sigma dW(t) \tag{3.56}$$

with  $A(t,T)$  deterministic; this follows from (3.55). The solution of this equation is

$$B(t,T) = B(0,T) \exp\left(\int_0^t [r(u) - \frac{1}{2}\sigma^2 A^2(u,T)] \, du - \sigma \int_0^t A(u,T) \, dW(u)\right),$$

from which it is evident that

3.3 Gaussian Short Rate Models 117

$$\frac{B(t,T)}{\beta(t)} = B(0,T) \exp\left(-\frac{1}{2}\sigma^2 \int_0^t A^2(u,T) \, du - \sigma \int_0^t A(u,T) \, dW(u)\right) \tag{3.57}$$

is an exponential martingale.

As discussed in Section 1.2.3, the *forward measure* for any date  $T_F$  is the measure associated with taking the  $T_F$ -maturity bond  $B(t,T_F)$  as numeraire asset. The defining feature of the forward measure is that it makes the ratios  $B(t,T)/B(t,T_F)$  martingales for  $T < T_F$ . It is defined by the likelihood ratio process

$$\left(\frac{dP_{T_F}}{dP_{\beta}}\right)_t = \frac{B(t,T_F)\beta(0)}{\beta(t)B(0,T_F)},$$

and this is given in (3.57) up to a factor of  $1/B(0,T_F)$ . From Girsanov's Theorem, it follows that the process  $W^{T_F}$  defined by

$$dW^{T_F}(t) = dW(t) + \sigma A(t, T_F) dt$$

is a standard Brownian motion under  $P_{T_E}$ . Accordingly, the dynamics of the Vasicek model become

$$dr(t) = \alpha(b(t) - r(t)) dt + \sigma dW(t)$$
  
=  $\alpha(b(t) - r(t)) dt + \sigma (dW^{T_F}(t) - \sigma A(t, T_F) dt)$   
=  $\alpha(b(t) - \sigma^2 A(t, T_F) - r(t)) dt + \sigma dW^{T_F}(t).$  (3.58)

Thus, under the forward measure, the short rate process remains a Vasicek process but the reversion level  $b(t)$  becomes  $b(t) - \sigma^2 A(t, T_F)$ .

The process in (3.58) can be simulated using (3.45) with  $b(t)$  replaced by  $b(t) - \sigma^2 A(t, T_F)$ . In particular, we simulate  $W^{T_F}$  the way we would simulate any other standard Brownian motion. The simulation algorithm does not "know" that it is simulating a Brownian motion under the forward measure rather than under the risk-neutral measure.

Suppose we want to price a derivative security making a payoff of  $g(r(T_F))$ at time  $T_F$ . Under the risk-neutral measure, we would price the security by computing

$$\mathsf{E}\left[e^{-\int_0^{T_F} r(u) \, du} g(r(T_F))\right].$$

In fact, g could be a function of the path of  $r(t)$  rather than just its terminal value. Switching to the forward measure, this becomes

$$\begin{split} &\mathsf{E}_{T_F} \left[ e^{-\int_0^{T_F} r(u) \, du} g(r(T_F)) \left( \frac{dP_\beta}{dP_{T_F}} \right)_{T_F} \right] \\ &= \mathsf{E}_{T_F} \left[ e^{-\int_0^{T_F} r(u) \, du} g(r(T_F)) \left( \frac{\beta(T_F) B(0, T_F)}{B(T_F, T_F) \beta(0)} \right) \right] \\ &= B(0, T_F) \mathsf{E}_{T_F} \left[ g(r(T_F)) \right], \end{split}$$

where  $E_{T_F}$  denotes expectation under the forward measure. Thus, we may price the derivative security by simulating  $r(t)$  under the forward measure  $P_{T_F}$ , estimating the expectation of  $g(r(T_F))$  and multiplying by  $B(0,T_F)$ . Notice that discounting in this case is deterministic — we do not need to simulate a discount factor. This apparent simplification results from inclusion of the additional term  $-\sigma^2 A(t,T_F)$  in the drift of  $r(t)$ .

A consequence of working under the forward measure is that the simulation prices the bond maturing at  $T_F$  exactly: pricing this bond corresponds to taking  $q(r(T_F)) \equiv 1$ . Again, this apparent simplification is really a consequence of the form of the drift of  $r(t)$  under the forward measure.

### 3.3.3 Multifactor Models

A general class of Gaussian Markov processes in  $\mathbb{R}^d$  have the form

$$dX(t) = C(b - X(t)) dt + D dW(t)$$
(3.59)

where C and D are  $d \times d$  matrices, b and  $X(t)$  are in  $\Re^d$ , W is a standard d-dimensional Brownian motion, and  $X(0)$  is Gaussian or constant. Such a process remains Gaussian and Markovian if the coefficients  $C, b,$  and  $D$  are made time-varying but deterministic. The solution of  $(3.59)$  is

$$X(t) = e^{-Ct}X(0) + \int_0^t e^{-C(t-s)}b \, ds + \int_0^t e^{-C(t-s)}D \, dW(s),$$

from which it is possible to define an exact time-discretization similar to  $(3.45)$ .

A model of the short rate process can be specified by setting  $r(t) = a^{\top}X(t)$ with  $a \in \mathbb{R}^d$  (or with a deterministically time-varying). The elements of  $X(t)$ are then interpreted as "factors" driving the evolution of the short rate. Because each  $X(t)$  is normally distributed,  $r(t)$  is normally distributed. However,  $r(t)$  is not in general a Markov process: to make the future evolution of r independent of the past, we need to condition on the full state information  $X(t)$ and not merely  $r(t)$ .

Recall from  $(3.55)$  that in the Vasicek model (with constant or time-varying coefficients), bond prices are exponentials of affine functions of the short rate. A similar representation applies if the short rate has the form  $r(t) = a^{\top}X(t)$ and  $X(t)$  is as in (3.59); in particular, we have

$$B(t,T) = \exp(-A(t,T)^\top X(t) + C(t,T))$$

for some  $\Re^d$ -valued function  $A(t,T)$  and some scalar function  $C(t,T)$ . In the single-factor setting, differentiating  $(3.55)$  and then simplifying leads to

$$\frac{dB(t,T)}{B(t,T)} = r(t) dt - A(t,T)\sigma dW(t),$$

with  $\sigma$  the diffusion parameter of  $r(t)$ . The instantaneous correlation between the returns on bonds with maturities  $T_1$  and  $T_2$  is therefore

3.3 Gaussian Short Rate Models  $119$ 

$$\frac{A(t,T_1)\sigma \cdot A(t,T_2)\sigma}{\sqrt{A^2(t,T_1)\sigma^2}\sqrt{A^2(t,T_2)\sigma^2}} = 1.$$

In other words, all bonds are instantaneously perfectly correlated. In the multifactor setting, the bond price dynamics are given by

$$\frac{dB(t,T)}{B(t,T)} = r(t) dt - A(t,T)^{\top} D dW(t).$$

The instantaneous correlation for maturities  $T_1$  and  $T_2$  is

$$\frac{A(t,T_1)^\top D D^\top A(t,T_2)}{\|A(t,T_1)^\top D\| \|A(t,T_2)^\top D\|},$$

which can certainly take values other than 1. The flexibility to capture less than perfect instantaneous correlation between bond returns is the primary motivation for considering multifactor models.

Returning to the general formulation in  $(3.59)$ , suppose that C can be diagonalized in the sense that  $VCV^{-1} = \Lambda$  for some matrix V and diagonal matrix  $\Lambda$  with diagonal entries  $\lambda_1, \ldots, \lambda_d$ . Suppose further that C is nonsingular and define  $Y(t) = VX(t)$ . Then

$$\begin{aligned} dY(t) &= V \, dX(t) \\ &= V[C(b - X(t) \, dt + D \, dW(t)] \\ &= (VCb - \Lambda Y(t)) \, dt + VD \, dW(t) \\ &= \Lambda(\Lambda^{-1}VCb - Y(t)) \, dt + VD \, dW(t) \\ &= \Lambda(Vb - Y(t)) \, dt + VD \, dW(t) \\ &= \Lambda(\tilde{b} - Y(t)) \, dt + d\tilde{W}(t) \end{aligned}$$

with  $\tilde{W}$  a BM $(0, \Sigma)$  process,  $\Sigma = VDD^{\top}V^{\top}$ . It follows that the components of  $(Y_1, \ldots, Y_d)$  satisfy

$$dY_j(t) = \lambda_j(\tilde{b}_j - Y_j(t)) dt + d\tilde{W}_j(t), \quad j = 1, \dots, d.$$
 (3.60)

In particular, each  $Y_i$  is itself a Markov process. The  $Y_i$  remain coupled, however, through the correlation across the components of  $\tilde{W}$ . They can be simulated as in  $(3.46)$  by setting

$$Y_j(t_{i+1}) =$$
  
$$e^{\lambda_j(t_{i+1}-t_i)}Y_j(t_i) + (e^{\lambda_j(t_{i+1}-t_i)}-1)\tilde{b}_j + \sqrt{\frac{1}{2\lambda_j} \left(1 - e^{-2\lambda_j(t_{i+1}-t_i)}\right)}\xi_j(i+1),$$

where  $\xi(1), \xi(2), \ldots$  are independent  $N(0, \Sigma)$  random vectors,  $\xi(i) = (\xi_1(i), \xi(2), \ldots$  $\ldots, \xi_d(i)$ ). Thus, when C is nonsingular and diagonalizable, simulation of  $(3.59)$  can be reduced to a system of scalar simulations.

 $\mathbb{C}^{\mathbb{Z}}$ 

wanter I autio

As noted by Andersen and Andreasen [14], a similar reduction is possible even if  $C$  is not diagonalizable, but at the expense of making all coefficients time-dependent. If  $V(t)$  is a deterministic  $d \times d$  matrix-valued function of time and we set  $Y(t) = V(t)X(t)$ , then

$$\begin{aligned} dY(t) &= \dot{V}(t)X(t) \, dt + V(t)dX(t) \\ &= [\dot{V}(t)X(t) + V(t)C(b - X(t))] \, dt + V(t)D \, dW(t), \end{aligned}$$

where  $V(t)$  denotes the time derivative of  $V(t)$ . If we choose  $V(t) = \exp([C I|t$ ), then

$$\dot{V}(t) = V(t)C - V(t)$$

and thus

$$dY(t) = [V(t)Cb - V(t)X(t)]dt + V(t)D\,dW(t)$$
  
= ( $\tilde{b}(t) - Y(t)dt + \tilde{D}(t)dW(t),$  (3.61)

with  $\tilde{b}(t) = V(t)Cb$  and  $\tilde{D}(t) = V(t)D$ . Notice that the drift of each component  $Y_i(t)$  depends only on that  $Y_i(t)$ . This transformation therefore decouples the drifts of the components of the state vector, making each  $Y_i$  a Markov process, though the components remain linked through the diffusion term. We can recover the original state vector by setting  $X(t) = V(t)^{-1}Y(t)$ because  $V(t)$  is always invertible. The seemingly special form of the dynamics in  $(3.61)$  is thus no less general than the dynamics in  $(3.59)$  with time-varying coefficients.

# 3.4 Square-Root Diffusions

Feller [118] studied a class of processes that includes the square-root diffusion

$$dr(t) = \alpha(b - r(t)) dt + \sigma \sqrt{r(t)} dW(t), \qquad (3.62)$$

with  $W$  a standard one-dimensional Brownian motion. We consider the case in which  $\alpha$  and b are positive. If  $r(0) > 0$ , then  $r(t)$  will never be negative; if  $2\alpha b \geq \sigma^2$ , then  $r(t)$  remains strictly positive for all t, almost surely.

This process was proposed by  $\text{Cox}$ , Ingersoll, and Ross [91] as a model of the short rate, generally referred to as the CIR model. They developed a general equilibrium framework in which if the change in production opportunities is assumed to follow a process of this form, then the short rate does as well. As with the Vasicek model, the form of the drift in  $(3.62)$  suggests that  $r(t)$  is pulled towards b at a speed controlled by  $\alpha$ . In contrast to the Vasicek model, in the CIR model the diffusion term  $\sigma\sqrt{r(t)}$  decreases to zero as  $r(t)$ approaches the origin and this prevents  $r(t)$  from taking negative values. This eature of  $(3.62)$  is attractive in modeling interest rates.

All of the coefficients in  $(3.62)$  could in principle be made time-dependent. In practice, it can be particularly useful to replace the constant  $b$  with a function of time and thus consider

$$dr(t) = \alpha(b(t) - r(t)) dt + \sigma \sqrt{r(t)} dW(t). \tag{3.63}$$

As with the Vasicek model, this extension is frequently used to make the bond price function

$$T \mapsto \mathsf{E}\left[\exp\left(-\int_0^T r(u)\,du\right)\right]$$

match a set of observed bond prices  $B(0,T)$ .

Although we stress the application of  $(3.63)$  to interest rate modeling, it should be noted that this process has other financial applications. For example, Heston  $[179]$  proposed a stochastic volatility model in which the price of an asset  $S(t)$  is governed by

$$\frac{dS(t)}{S(t)} = \mu \, dt + \sqrt{V(t)} \, dW_1(t) \tag{3.64}$$

$$dV(t) = \alpha(b - V(t)) dt + \sigma \sqrt{V(t)} dW_2(t), \qquad (3.65)$$

where  $(W_1, W_2)$  is a two-dimensional Brownian motion. Thus, in Heston's model, the squared volatility  $V(t)$  follows a square-root diffusion. In addition, the process in  $(3.63)$  is sometimes used to model a stochastic intensity for a jump process in, for example, modeling default.

A simple Euler discretization of (3.62) suggests simulating  $r(t)$  at times  $t_1,\ldots,t_n$  by setting

$$r(t_{i+1}) = r(t_i) + \alpha(b - r(t_i))[t_{i+1} - t_i] + \sigma\sqrt{r(t_i)^+} \sqrt{t_{i+1} - t_i} Z_{i+1}, \quad (3.66)$$

with  $Z_1,\ldots,Z_n$  independent  $N(0,1)$  random variables. Notice that we have taken the positive part of  $r(t_i)$  inside the square root; some modification of this form is necessary because the values of  $r(t_i)$  produced by Euler discretization may become negative. We will see, however, that this issue can be avoided (along with any other discretization error) by sampling from the exact transition law of the process.

### 3.4.1 Transition Density

The SDE  $(3.62)$  is not explicitly solvable the way those considered in Sections  $3.2$  and  $3.3$  are; nevertheless, the transition density for the process is known. Based on results of Feller  $[118]$ , Cox et al. [91] noted that the distribution of  $r(t)$  given  $r(u)$  for some  $u < t$  is, up to a scale factor, a noncentral chi-square distribution. This property can be used to simulate the process  $(3.62)$ . We follow the approach suggested by Scott [324].

A noncentral chi-square random variable  $\chi_{\nu}^{\prime 2}(\lambda)$  with  $\nu$  degrees of freedom and noncentrality parameter  $\lambda$  has distribution

$$P(\chi_{\nu}^{\prime 2}(\lambda) \le y) = F_{\chi_{\nu}^{\prime 2}(\lambda)}(y)$$
  
$$\equiv e^{-\lambda/2} \sum_{j=0}^{\infty} \frac{(\frac{1}{2}\lambda)^j / j!}{2^{(\nu/2)+j} \Gamma(\frac{\nu}{2}+j)} \int_0^y z^{(\nu/2)+j-1} e^{-z/2} dz, \quad (3.67)$$

for  $y > 0$ . The transition law of  $r(t)$  in (3.62) can be expressed as

$$r(t) = \frac{\sigma^2 (1 - e^{-\alpha(t-u)})}{4\alpha} \chi_d^{\prime 2} \left(\frac{4\alpha e^{-\alpha(t-u)}}{\sigma^2 (1 - e^{-\alpha(t-u)})} r(u)\right), \quad t > u,\tag{3.68}$$

where

$$d = \frac{4b\alpha}{\sigma^2}.\tag{3.69}$$

This says that, given  $r(u)$ ,  $r(t)$  is distributed as  $\sigma^2(1-e^{-\alpha(t-u)})/(4\alpha)$  times a noncentral chi-square random variable with  $d$  degrees of freedom and noncentrality parameter

$$\lambda = \frac{4\alpha e^{-\alpha(t-u)}}{\sigma^2 (1 - e^{-\alpha(t-u)})} r(u); \tag{3.70}$$

equivalently,

$$P(r(t) \le y|r(u)) = F_{\chi_d^{\prime 2}(\lambda)} \left(\frac{4\alpha y}{\sigma^2 (1 - e^{-\alpha(t-u)})}\right),$$

with d as in (3.69),  $\lambda$  as in (3.70), and  $F_{\chi^{\prime 2}_{d}(\lambda)}$  as in (3.67). Thus, we can simulate the process  $(3.62)$  exactly on a discrete time grid provided we can sample from the noncentral chi-square distribution.

Like the Vasicek model, the square-root diffusion  $(3.62)$  has a limiting stationary distribution. If we let  $t \to \infty$  in (3.68), we find that  $r(t)$  converges in distribution to  $\sigma^2/4\alpha$  times a noncentral chi-square random variable with  $d$  degrees of freedom and noncentrality parameter 0 (making it an ordinary chi-square random variable). This is a stationary distribution in the sense that if  $r(0)$  is drawn from this distribution, then  $r(t)$  has the same distribution for all  $t$ .

# Chi-Square and Noncentral Chi-Square

If  $\nu$  is a positive integer and  $Z_1,\ldots,Z_{\nu}$  are independent  $N(0,1)$  random variables, then the distribution of

$$Z_1^2 + Z_2^2 + \dots + Z_\nu^2$$

is called the chi-square distribution with  $\nu$  degrees of freedom. The symbol  $\chi^2_{\nu}$ denotes a random variable with this distribution; the prime in  $\chi^{\prime 2}_{\nu}(\lambda)$  emphasizes that this symbol refers to the noncentral case. The chi-square distribution is given by

3.4 Square-Root Diffusions 123

$$P(\chi_{\nu}^{2} \leq y) = \frac{1}{2^{\nu/2} \Gamma(\nu/2)} \int_{0}^{y} e^{-z/2} z^{(\nu/2)-1} dz, \tag{3.71}$$

where  $\Gamma(\cdot)$  denotes the gamma function and  $\Gamma(n) = (n-1)!$  if n is a positive integer. This expression defines a valid probability distribution for all  $\nu > 0$ and thus extends the definition of  $\chi^2_{\nu}$  to non-integer  $\nu$ .

For integer  $\nu$  and constants  $a_1, \ldots, a_{\nu}$ , the distribution of

$$\sum_{i=1}^{\nu} (Z_i + a_i)^2 \tag{3.72}$$

is noncentral chi-square with  $\nu$  degrees of freedom and noncentrality parameter  $\lambda = \sum_{i=1}^{\nu} a_i^2$ . This representation explains the term "noncentral." The distribution in (3.67) extends the definition to non-integer  $\nu$ .

It follows from the representation in (3.72) that if  $\nu > 1$  is an integer, then

$$\chi_{\nu}^{\prime 2}(\lambda) = \chi_{1}^{\prime 2}(\lambda) + \chi_{\nu-1}^{2},$$

meaning that the two sides have the same distribution when the random variables on the right are independent of each other. As discussed in Johnson et al. [202, p.436], this representation is valid even for non-integer  $\nu > 1$ . Thus, to generate  $\chi_{\nu}^{\prime 2}(\lambda)$ ,  $\nu > 1$ , it suffices to generate  $\chi_{\nu-1}^2$  and an independent  $N(0,1)$  random variable Z and to set

$$\chi_{\nu}^{\prime 2}(\lambda) = (Z + \sqrt{\lambda})^2 + \chi_{\nu-1}^2. \tag{3.73}$$

This reduces sampling of a noncentral chi-square to sampling of an ordinary chi-square (and an independent normal) when  $\nu > 1$ .

For any  $\nu > 0$ , (3.67) indicates that a noncentral chi-square random variable can be represented as an ordinary chi-square random variable with a random degrees-of-freedom parameter. In more detail, if  $N$  is a Poisson random variable with mean  $\lambda/2$ , then

$$P(N = j) = e^{-\lambda/2} \frac{(\lambda/2)^j}{j!}, \quad j = 0, 1, 2, \dots.$$

Consider now a random variable  $\chi^2_{\nu+2N}$  with N having this Poisson distribution. Conditional on  $N = j$ , the random variable has an ordinary chi-square distribution with  $\nu + 2j$  degrees of freedom:

$$P(\chi_{\nu+2N}^2 \le y|N=j) = \frac{1}{2^{(\nu/2)+j}\Gamma((\nu/2)+j)} \int_0^y e^{-z/2} z^{(\nu/2)+j-1} \, dz.$$

The unconditional distribution is thus given by

$$\sum_{j=0}^{\infty} P(N=j) P(\chi_{\nu+2N}^2 \le y | N=j) = \sum_{j=0}^{\infty} e^{-\lambda/2} \frac{(\lambda/2)^j}{j!} P(\chi_{\nu+2j}^2 \le y),$$

which is precisely the noncentral chi-square distribution in  $(3.67)$ . We may therefore sample  $\chi_{\nu}^{\prime 2}(\lambda)$  by first generating a Poisson random variable N and then, conditional on N, sampling a chi-square random variable with  $\nu + 2N$ degrees of freedom. This reduces sampling of a noncentral chi-square to sampling of an ordinary chi-square and a Poisson random variable. We discuss methods for sampling from these distributions below. Figure 3.5 summarizes their use in simulating the square-root diffusion  $(3.62)$ .

```
Simulation of dr(t) = \alpha(b - r(t)) dt + \sigma \sqrt{r(t)} dW(t)on time grid 0 = t_0 < t_1 < \cdots < t_n with d = 4b\alpha/\sigma^2Case 1: d > 1for i = 0, ..., n - 1c \leftarrow \sigma^2 (1 - e^{-\alpha(t_{i+1} - t_i)})/(4\alpha)\lambda \leftarrow r(t_i)(e^{-\alpha(t_{i+1}-t_i)})/cgenerate Z \sim N(0, 1)generate X \sim \chi^2_{d-1}r(t_{i+1}) \leftarrow c[(Z + \sqrt{\lambda})^2 + X]end
    Case 2: d \leq 1for i = 0, ..., n - 1c \leftarrow \sigma^2 (1 - e^{-\alpha (t_{i+1} - t_i)}) / (4\alpha)\lambda \leftarrow r(t_i)(e^{-\alpha(t_{i+1}-t_i)})/cgenerate N \sim \text{Poisson}(\lambda/2)generate X \sim \chi^2_{d+2N}r(t_{i+1}) \leftarrow cXend
```

**Fig. 3.5.** Simulation of square-root diffusion  $(3.62)$  by sampling from the transition density.

Figure 3.6 compares the exact distribution of  $r(t)$  with the distribution produced by the Euler discretization  $(3.66)$  after a single time step. The comparison is based on  $\alpha = 0.2$ ,  $\sigma = 0.1$ ,  $b = 5\%$ , and  $r(0) = 4\%$ ; the left panel takes  $t = 0.25$  and the right panel takes  $t = 1$ . These values for the model parameters are sensible for an interest rate model if time is measured in years, so the values of  $t$  should be interpreted as a quarter of a year and a full year, respectively. The figures suggest that the Euler discretization produces too many values close to or below  $0$  and a mode to the right of the true mode. The effect if particularly pronounced over the rather large time step  $t=1$ .

![](_page_46_Figure_1.jpeg)

Fig. 3.6. Comparison of exact distribution (solid) and one-step Euler approximation (dashed) for a square-root diffusion with  $\alpha = 0.2$ ,  $\sigma = 0.1$ ,  $b = 5\%$ , and  $r(0) = 4\%$ . The left panel compares distributions at  $t = 0.25$ , the right panel at  $t = 1$ .

# 3.4.2 Sampling Gamma and Poisson

The discussion leading to Figure 3.5 reduces the problem of simulating the square-root diffusion  $(3.62)$  to one of sampling from a chi-square distribution and possibly also the normal and Poisson distributions. We discussed sampling from the normal distribution in Section  $2.3$ ; we now consider methods for sampling from the chi-square and Poisson distributions.

### Gamma Distribution

The gamma distribution with shape parameter a and scale parameter  $\beta$  has density

$$f(y) = f_{a,\beta}(y) = \frac{1}{\Gamma(a)\beta^a} y^{a-1} e^{-y/\beta}, \quad y \ge 0.$$
 (3.74)

It has mean  $a\beta$  and variance  $a\beta^2$ . Comparison with (3.71) reveals that the chi-square distribution is the special case of scale parameter  $\beta = 2$  and shape parameter  $a = \nu/2$ . We therefore consider the more general problem of generating samples from gamma distributions.

Methods for sampling from the gamma distribution typically distinguish the cases  $a \leq 1$  and  $a > 1$ . For the application to the square-root diffusion  $(3.62)$ , the shape parameter a is given by  $d/2$  with d as in (3.69). At least in the case of an interest rate model,  $d$  would typically be larger than 2 so the case  $a > 1$  is most relevant. We include the case  $a \leq 1$  for completeness and other potential applications. There is no loss of generality in fixing the scale parameter  $\beta$  at 1: if X has the gamma distribution with parameters  $(a, 1)$ , then  $\beta X$  has the gamma distribution with parameters  $(a, \beta)$ .

Cheng and Feast  $[83]$  develop a method based on a general approach to random variate generation known as the ratio-of-uniforms method. The ratioof-uniforms method is closely related to the acceptance-rejection method disaround in Section 222 It evaluate the following property Suppose  $f$  is a

nonnegative, integrable function on  $[0,\infty)$ ; if  $(X,Y)$  is uniformly distributed over the set  $A = \{(x, y) : x \leq \sqrt{f(y/x)}\}$ , then the density of  $Y/X$  is proportional to f. (See p.180 of Fishman [121] or p.59 of Gentle [136].) Suppose A is contained in a bounded rectangle. Then to sample uniformly from  $A$ , we can repeatedly sample pairs  $(X, Y)$  uniformly over the rectangle and keep the first one that satisfies  $X \leq \sqrt{f(Y/X)}$ . The ratio-of-uniforms method delivers  $Y/X$  as a sample from the density proportional to f.

To sample from the gamma density with  $a > 1$ , define

$$A = \left\{ (x, y) : 0 \le x \le \sqrt{[(y/x)^{a-1}e^{-y/x}]} \right\}.$$

This set is contained in the rectangle  $[0, \bar{x}] \times [0, \bar{y}]$  with  $\bar{x} = [(a-1)/e]^{(a-1)/2}$ and  $\bar{y} = [(a+1)/e]^{(a+1)/2}$ . Sampling uniformly over this rectangle, the expected number of samples needed until one lands in  $A$  is given by the ratio of the area of A to that of the rectangle. As shown in Fishman [121], this ratio is  $O(\sqrt{a})$ , so the time required to generate a sample using this method grows with the shape parameter. Cheng and Feast [83] and Fishman [121] develop modifications of this basic approach that accelerate sampling. In Figure 3.7, which is Fishman's Algorithm GKM1, the first acceptance test is a fast check that reduces the number of logarithmic evaluations. When many samples are to be generated using the same shape parameter (as would be the case in the application to the square-root diffusion), the constants in the setup step in Figure 3.8 should be computed just once and then passed as arguments to the sampling routine. For large values of the shape parameter  $a$ , Algorithm  $\text{GKM2}$  in Fishman [121] is faster than the method in Figure 3.7.

> Setup:  $\bar{a} \leftarrow a - 1, b \leftarrow (a - (1/(6a)))/\bar{a}, m \leftarrow 2/\bar{a}, d \leftarrow m + 2$ repeat generate  $U_1, U_2 \sim \text{Unif}[0,1]$  $V \leftarrow bU_2/U_1$ if  $mU_1 - d + V + (1/V) \le 0$ , accept elseif  $m \log U_1 - \log V + V - 1 \leq 0$ , accept until accept return  $Z \leftarrow \bar{a}V$

Fig. 3.7. Algorithm GKM1 from Fishman [121], based on Cheng and Feast [83], for sampling from the gamma distribution with parameters  $(a, 1), a > 1$ .

Ahrens and Dieter [6] provide a fast acceptance-rejection algorithm for the case  $a \leq 1$ . Their method generates candidates by sampling from distributions concentrated on [0,1] and  $(1,\infty)$  with appropriate probabilities. In more detail, let  $p = e/(a + e)$  ( $e = \exp(1)$ ) and define

3.4 Square-Root Diffusions 127

$$g(z) = \begin{cases} paz^{a-1}, & 0 \le z \le 1\\ (1-p)e^{-z+1}, & z > 1. \end{cases}$$

This is a probability density; it is a mixture of the densities  $az^{a-1}$  on [0, 1] and  $e^{-z+1}$  on  $(1,\infty)$ , with weights p and  $(1-p)$ , respectively. We can sample from  $q$  by sampling from each of these densities with the corresponding probabilities. Each of these two densities is easily sampled using the inverse transform method: for the density  $az^{a-1}$  on [0, 1] we can use  $U^{1/a}$ ,  $U \sim \text{Unif}[0,1]$ ; for the density  $e^{-z+1}$  on  $(1,\infty)$  we can use  $1-\log(U)$ . Samples from g are suitable candidates for acceptance-rejection because the ratio  $f_{a,1}(z)/g(z)$  with  $f_{a,1}$  a  $\text{gamma density as in (3.74)}$  is bounded. Inspection of this ratio indicates that a candidate Z in [0,1] is accepted with probability  $e^{-Z}$  and a candidate in  $(1,\infty)$  is accepted with probability  $Z^{a-1}$ . A global bound on the ratio is given bv

$$f_{a,1}(z)/g(z) \le \frac{a+e}{ae\Gamma(a)} \le 1.39;$$

recall from Section  $2.2.2$  that the upper bound on this ratio determines the expected number of candidates generated per accepted sample.

Figure 3.8 displays the method of Ahrens and Dieter  $[6]$ . The figure is based on Algorithm  $GS^*$  in Fishman [121] but it makes the acceptance tests more explicit, if perhaps slightly slower. Notice that if the condition  $Y \leq 1$  fails to hold, then Y is uniformly distributed over [1, b]; this means that  $(b-Y)/a$ has the distribution of  $U/e, U \sim \text{Unif}[0,1]$  and thus  $-\log((b-Y)/a)$  has the distribution of  $1 - \log(U)$ .

```
Setup: b \leftarrow (a + e)/erepeat
    generate U_1, U_2 \sim \text{Unif}[0,1]; Y \leftarrow bU_1if Y \leq 1Z \leftarrow Y^{1/a}if U_2 < \exp(-Z), accept
    otherwise Z \leftarrow -\log((b-Y)/a)if U_2 < Z^{a-1}, accept
\text{until accept}return Z
```

Fig. 3.8. Ahrens-Dieter method for sampling from the gamma distribution with parameters  $(a, 1), a \leq 1.$ 

# Poisson Distribution

The Poisson distribution with mean  $\theta > 0$  is given by

$$P(N=k) = e^{-\theta} \frac{\theta^k}{k!}, \quad k = 0, 1, 2, \dots$$
 (3.75)

We abbreviate this by writing  $N \sim \text{Poisson}(\theta)$ . This is the distribution of the number of events in  $[0, 1]$  when the times between consecutive events are independent and exponentially distributed with mean  $1/\theta$ . Thus, a simple method for generating Poisson samples is to generate exponential random variables  $X_i = -\log(U_i)/\theta$  from independent uniforms  $U_i$  and then take N to be the largest integer for which  $X_1 + \cdots + X_N \leq 1$ . This method is rather slow, especially if  $\theta$  is large. In the intended application in Figure 3.5, the mean of the Poisson random variable  $-$  equal to half the noncentrality parameter in the transition density of the square-root diffusion — could be quite large for plausible parameter values.

An alternative is to use the inverse transform method. For discrete distributions, this amounts to a sequential search for the smallest  $n$  at which  $F(n) \leq U$ , where F denotes the cumulative distribution function and U is Unif[0,1]. In the case of a Poisson distribution,  $F(n)$  is calculated as  $P(N = 0) + \cdots + P(N = n)$ ; rather than calculate each term in this sum using (3.75), we can use the relation  $P(N = k + 1) = P(N = k)\theta/(k + 1)$ . Figure 3.9 illustrates the method.

```
p \leftarrow \exp(-\theta), \, F \leftarrow pN \leftarrow 0generate U \sim \text{Unif}[0,1]while U > FN \leftarrow N + 1p \leftarrow p\theta/NF \leftarrow F + preturn N
```

**Fig. 3.9.** Inverse transform method for sampling from Poisson( $\theta$ ), the Poisson distribution with mean  $\theta$ .

# 3.4.3 Bond Prices

Cox, Ingersoll, and Ross  $[91]$  derived an expression for the price of a bond

$$B(t,T) = \mathsf{E}\left[\exp\left(-\int_t^T r(u) \, du\right) | r(t) \right]$$

when the short rate evolves according to  $(3.62)$ . The bond price has the exponential affine form

$$B(t,T) = e^{-A(t,T)r(t) + C(t,T)}$$

as in a Gaussian short rate model, but with

$$A(t,T) = \frac{2(e^{\gamma(T-t)}-1)}{(\gamma+\alpha)(e^{\gamma(T-t)}-1)+2\gamma}$$

and

$$C(t,T) = \frac{2\alpha b}{\sigma^2} \log \left( \frac{2\gamma e^{(\alpha+\gamma)(T-t)/2}}{(\gamma+\alpha)(e^{\gamma(T-t)}-1)+2\gamma} \right),\,$$

and  $\gamma = \sqrt{\alpha^2 + 2\sigma^2}$ .

This expression for the bond price is a special case of a more general result, given as Proposition  $6.2.5$  in Lamberton and Lapevre [218]. This result gives the bivariate Laplace transform of the short rate and its integral: for nonnegative  $\lambda, \theta$ ,

$$\mathsf{E}\left[\exp\left(-\lambda r(T) - \theta \int_t^T r(u) \, du\right) | r(t)\right] = \exp(-\alpha b\psi_1(T-t) - r(t)\psi_2(T-t)) \tag{3.76}$$

with

$$\psi_1(s) = -\frac{2}{\sigma^2} \log \left( \frac{2\gamma(\theta)e^{(\alpha+\gamma(\theta))s/2}}{\sigma^2 \lambda(e^{\gamma(\theta)s}-1) + \gamma(\theta) - \alpha + e^{\gamma(\theta)s}(\gamma(\theta) + \alpha)} \right),$$

and

$$\psi_2(s) = \frac{\lambda(\gamma(\theta) + \alpha + e^{\gamma(\theta)s}(\gamma(\theta) - \alpha)) + 2\theta(e^{\gamma(\theta)s} - 1)}{\sigma^2\lambda(e^{\gamma(\theta)s} - 1) + \gamma(\theta) - \alpha + e^{\gamma(\theta)s}(\gamma(\theta) + \alpha)}$$

and  $\gamma(\theta) = \sqrt{\alpha^2 + 2\sigma^2\theta}$ . The bond pricing formula is the special case  $\lambda = 0$ ,  $\theta = 1.$ 

The bivariate Laplace transform in  $(3.76)$  characterizes the joint distribution of the short rate and its integral. This makes it possible, at least in principle, to sample from the joint distribution of  $(r(t_{i+1}), Y(t_{i+1}))$  given  $(r(t_i), Y(t_i))$  with

$$Y(t) = \int_0^t r(u) \, du$$

As explained in Section 3.3.2, this would allow exact simulation of the short rate and the discount factor on a discrete time grid. In the Gaussian setting, the joint distribution of  $r(t)$  and  $Y(t)$  is normal and therefore easy to sample; in contrast, the joint distribution determined by  $(3.76)$  is not explicitly available. Scott [324] derives the Laplace transform of the conditional distribution of  $Y(t_{i+1}) - Y(t_i)$  given  $r(t_i)$  and  $r(t_{i+1})$ , and explains how to use numerical transform inversion to sample from the conditional distribution. Through this method, he is able to simulate  $(r(t_i), Y(t_i))$  without discretization error.

# Time-Dependent Coefficients

As noted earlier, the parameter  $b$  is often replaced with a deterministic function of time  $b(t)$  in order to calibrate the model to an initial term structure, resulting in the dynamics specified in  $(3.63)$ . In this more general setting, a result of the form in (3.76) continues to hold but with functions  $\psi_1$  and  $\psi_2$  depending on both t and T rather than merely on  $T-t$ . Moreover, these functions will not in general be available in closed form, but are instead characterized by a system of ordinary differential equations. By solving these differential equations numerically, it then becomes possible to compute bond prices. Indeed, bond prices continue to have the exponential affine form, though the functions  $A(t,T)$  and  $C(t,T)$  in the exponent are no longer available explicitly but are also determined through ordinary differential equations (see Duffie, Pan, Singleton [105] and Jamshidian [195]). This makes it possible to use a numerical procedure to choose the function  $b(t)$  to match an initial set of bond prices  $B(0,T).$ 

Once the constant  $b$  is replaced with a function of time, the transition density of the short rate process ceases to admit the relatively tractable form discussed in Section 3.4.1. One can of course simulate using an Euler scheme of the form

$$r(t_{i+1}) = r(t_i) + \alpha(b(t_i) - r(t_i))[t_{i+1} - t_i] + \sigma\sqrt{r(t_i)^+} \sqrt{t_{i+1} - t_i} Z_{i+1},$$

with independent  $Z_i \sim N(0,1)$ . However, it seems preferable (at least from a distributional perspective) to replace this normal approximation to the transition law with a noncentral chi-square approximation. For example, if we  $\text{let}$ 

$$\bar{b}(t_i) = \frac{1}{t_{i+1} - t_i} \int_{t_i}^{t_{i+1}} b(s) \, ds$$

denote the average level of  $b(t)$  over  $[t_i, t_{i+1}]$  (assumed positive), then (3.68) suggests simulating by setting

$$r(t_{i+1}) = \frac{\sigma^2 (1 - e^{-\alpha(t_{i+1} - t_i)})}{4\alpha} \chi_d^{\prime 2} \left(\frac{4\alpha e^{-\alpha(t_{i+1} - t_i)}}{\sigma^2 (1 - e^{-\alpha(t_{i+1} - t_i)})} r(t_i)\right), \qquad (3.77)$$

with  $d = 4\bar{b}\alpha/\sigma^2$ . We can sample from the indicated noncentral chi-square distribution using the methods discussed in Section 3.4.1. However, it must be stressed that whereas  $(3.68)$  is an exact representation in the case of constant coefficients,  $(3.77)$  is only an approximate procedure. If it suffices to choose the function  $b(t)$  to match only bonds maturing at the simulation grid dates  $t_1,\ldots,t_n$ , then it may be possible to choose b to be constant over each interval  $[t_i, t_{i+1}],$  in which case (3.77) becomes exact.

Jamshidian [195] shows that if  $\alpha$ , b, and  $\sigma$  are all deterministic functions of time, the transition density of  $r(t)$  can be represented through a noncentral chi-square distribution provided  $\alpha(t)b(t)/\sigma^2(t)$  is independent of t. From  $(3.69)$  we see that this is equivalent to requiring that the degrees-of-freedom

parameter  $d = 4b\alpha/\sigma^2$  be constant. However, in this setting, the other parameters of the transition density are not given explicitly but rather as solutions to ordinary differential equations.

# Change of Numeraire

Recall from Sections 1.2.3 and 3.3.2 that the forward measure for any date  $T_F$ is the measure associated with taking as numeraire asset the bond  $B(t,T_F)$ maturing at  $T_F$ . We saw in Section 3.3.2 that if the short rate follows an Ornstein-Uhlenbeck process under the risk-neutral measure, then it continues to follow an OU process under a forward measure. An analogous property holds if the short rate follows a square-root diffusion.

Most of the development leading to  $(3.58)$  results from the exponential affine formula for bond prices and thus extends to the square-root model. In this setting, the bond price dynamics become

$$\frac{dB(t,T)}{B(t,T)} = r(t) dt - A(t,T)\sigma\sqrt{r(t)} dW(t);$$

in particular, the coefficient  $\sigma\sqrt{r(t)}$  replaces the  $\sigma$  of the Gaussian case. Proceeding as in  $(3.56)$ – $(3.58)$  but with this substitution, we observe that Girsanov's Theorem implies that the process  $W^{T_F}$  defined by

$$dW^{T_F}(t) = dW(t) + \sigma\sqrt{r(t)}A(t,T_F) dt$$

is a standard Brownian motion under the forward measure  $P_{T_F}$ . The dynamics of the short rate thus become

$$\begin{split} dr(t) &= \alpha(b(t) - r(t)) \, dt + \sigma \sqrt{r(t)} \, dW(t) \\ &= \alpha(b(t) - r(t)) \, dt + \sigma \sqrt{r(t)} [dW^{T_F}(t) - \sigma \sqrt{r(t)} A(t, T_F) dt] \\ &= \alpha(b(t) - (1 + \sigma^2 A(t, T_F)) r(t)] \, dt + \sigma \sqrt{r(t)} \, dW^{T_F}(t). \end{split}$$

This can be written as

$$dr(t) = \alpha(1 + \sigma^2 A(t, T_F)) \left(\frac{b(t)}{1 + \sigma^2 A(t, T_F)} - r(t)\right) dt + \sigma \sqrt{r(t)} dW^{T_F}(t),$$

which shows that under the forward measure the short rate is again a squareroot diffusion but one in which both the level to which the process reverts and the speed with which it reverts are functions of time. The pricing of derivative securities through simulation in the forward measure works the same way here as in the Vasicek model.

# 3.4.4 Extensions

In this section we consider further properties and extensions of the square-root diffusion. We discuss multifactor models, a connection with squared Gaussian processes, and a connection with CEV (constant elasticity of variance) models.

### Multifactor Models

The simplest multifactor extension of the CIR interest rate model defines independent processes

$$dX_i(t) = \alpha_i(b_i - X_i(t)) dt + \sigma_i \sqrt{X_i(t)} dW_i(t), \quad i = 1, \ldots, d,$$

and takes the short rate to be  $r(t) = X_1(t) + \cdots + X_d(t)$ . Much as in the discussion of Section 3.3.3, this extension allows imperfect instantaneous correlation among bonds of different maturities. Each  $X_i$  can be simulated using the method developed in the previous sections for a single-factor model.

It is possible to consider more general models in which the underlying processes  $X_1, \ldots, X_d$  are correlated. However, once one goes beyond the case of independent square-root factors, it seems more natural to move directly to the full generality of the affine models characterized by Duffie and Kan [101]. This class of models has a fair amount of tractability and computationally attractive features, but we will not consider it further here.

### Squared Gaussian Models

We next point out a connection between the (single-factor) square-root diffusion and a Gaussian model of the type considered in Section 3.3. This connection is of intrinsic interest, it sheds further light on the simulation procedure of Section 3.4.1, and it suggests a wider class of interest rate models. The link between the CIR model and squared Gaussian models is noted in Rogers  $[307]$ ; related connections are developed in depth by Revuz and Yor  $[306]$  in their discussion of Bessel processes.

Let  $X_1(t), \ldots, X_d(t)$  be independent Ornstein-Uhlenbeck processes of the  $\text{form}$ 

$$dX_i(t) = -\frac{\alpha}{2}X_i(t) dt + \frac{\sigma}{2} dW_i(t), \quad i = 1, \ldots, d,$$

for some constants  $\alpha$ ,  $\sigma$ , and independent Brownian motions  $W_1, \ldots, W_d$ . Let  $Y(t) = X_1^2(t) + \cdots + X_d^2(t)$ ; then Itô's formula gives

$$\begin{split} dY(t) &= \sum_{i=1}^d (2X_i(t) \, dX_i(t) + \frac{\sigma^2}{4} \, dt) \\ &= \sum_{i=1}^d (-\alpha X_i^2(t) + \frac{\sigma^2}{4}) \, dt + \sigma \sum_{i=1}^d X_i(t) \, dW_i(t) \\ &= \alpha \left(\frac{\sigma^2 d}{4\alpha} - Y(t)\right) \, dt + \sigma \sum_{i=1}^d X_i(t) \, dW_i(t). \end{split}$$

If we now define

$$d\tilde{W}(t) = \sum_{i=1}^{d} \frac{X_i(t)}{\sqrt{Y(t)}} \, dW_i(t),$$

then  $\tilde{W}(t)$  is a standard Brownian motion because the vector  $(X_1(t),\ldots,$  $(X_d(t))/\sqrt{Y(t)}$  multiplying  $(dW_1(t),\ldots,dW_d(t))^\top$  has norm 1 for all t. Hence,

$$dY(t) = \alpha \left(\frac{\sigma^2 d}{4\alpha} - Y(t)\right) dt + \sigma \sqrt{Y(t)} d\tilde{W}(t),$$

which has the form of (3.62) with  $b = \sigma^2 d/4\alpha$ .

Starting from  $(3.62)$  and reversing these steps, we find that we can construct a square-root diffusion as a sum of squared independent Ornstein-Uhlenbeck processes provided  $d = 4b\alpha/\sigma^2$  is an integer. Observe that this is precisely the degrees-of-freedom parameter in  $(3.69)$ . In short, a square-root diffusion with an integer degrees-of-freedom parameter is a sum of squared Gaussian processes.

We can use this construction from Gaussian processes to simulate  $r(t)$  in (3.62) if *d* is an integer. Writing  $r(t_{i+1})$  as  $\sum_{j=1}^{d} X_j^2(t_{i+1})$  and using (3.45) for the one-step evolution of the  $X_j$ , we arrive at

$$r(t_{i+1}) = \sum_{j=1}^{d} \left( e^{-\frac{1}{2}\alpha(t_{i+1}-t_i)} \sqrt{r(t_i)/d} + \frac{\sigma}{2} \sqrt{\frac{1}{\alpha}(1 - e^{-\alpha(t_{i+1}-t_i)})} Z_{i+1}^{(j)} \right)^2,$$

where  $(Z_i^{(1)}, \ldots, Z_i^{(d)})$  are standard normal *d*-vectors, independent for different values of  $i$ . Comparison with  $(3.72)$  reveals that the expression on the right is a scalar multiple of a noncentral chi-square random variable, so this construction is really just a special case of the method in Section  $3.4.1$ . It sheds some light on the appearance of the noncentral chi-square distribution in the law of  $r(t)$ .

This construction also points to another strategy for constructing interest rate models: rather than restricting ourselves to a sum of independent, identical squared OU processes, we can consider other quadratic functions of multivariate Gaussian processes. This idea has been developed in Beaglehole and Tenney  $[42]$  and Jamshidian  $[196]$ . The resulting models are closely related to the affine family.

## $\text{CEV Process}$

We conclude this section with a digression away from interest rate models to consider a class of asset price processes closely related to the square-root diffusion.

Among the important alternatives to the lognormal model for an asset price considered in Section 3.2 is the constant elasticity of variance  $(CEV)$ process (see Cox and Ross [89], Schroder [322] and references there)

$$dS(t) = \mu S(t) dt + \sigma S(t)^{\beta/2} dW(t). \qquad (3.78)$$

This includes geometric Brownian motion as the special case  $\beta = 2$ ; some empirical studies have found that  $\beta < 2$  gives a better fit to stock price data. If we write the model as

$$\frac{dS(t)}{S(t)} = \mu \, dt + \sigma S(t)^{(\beta - 2)/2} \, dW(t),$$

we see that the instantaneous volatility  $\sigma S(t)^{(\beta-2)/2}$  depends on the current level of the asset, and  $\beta < 2$  implies a negative relation between the price level and volatility.

If we set  $X(t) = S(t)^{2-\beta}$  and apply Itô's formula, we find that

$$dX(t) = \left[\frac{\sigma^2}{2}(2-\beta)(1-\beta) + \mu(2-\beta)X(t)\right]dt + \sigma(2-\beta)\sqrt{X(t)}\,dW(t),$$

revealing that  $X(t)$  is a square-root diffusion. For  $\mu > 0$  and  $1 < \beta < 2$ , we can use the method of the Section 3.4.1 to simulate  $X(t)$  on a discrete time grid and then invert the transformation from S to X to get  $S(t) = X(t)^{1/(2-\beta)}$ . The case  $\beta < 1$  presents special complications because of the behavior of S near 0; simulation of this case is investigated in Andersen and Andreasen [13].

# $3.5 \text{ Processes with Jumps}$

Although the vast majority of models used in derivatives pricing assume that the underlying assets have continuous sample paths, many studies have found evidence of the importance of jumps in prices and have advocated the inclusion of jumps in pricing models. Compared with a normal distribution, the logarithm of a price process with jumps is often *leptokurtotic*, meaning that it has a high peak and heavy tails, features typical of market data. In this section we discuss a few relatively simple models with jumps, highlighting issues that affect the implementation of Monte Carlo.

# 3.5.1 A Jump-Diffusion Model

Merton [263] introduced and analyzed one of the first models with both jump and diffusion terms for the pricing of derivative securities. Merton applied this model to options on stocks and interpreted the jumps as idiosyncratic shocks affecting an individual company but not the market as a whole. Similar models have subsequently been applied to indices, exchange rates, commodity prices, and interest rates.

Merton's jump-diffusion model can be specified through the SDE

$$\frac{dS(t)}{S(t-)} = \mu \, dt + \sigma \, dW(t) + dJ(t) \tag{3.79}$$

where  $\mu$  and  $\sigma$  are constants, W is a standard one-dimensional Brownian motion, and  $J$  is a process independent of  $W$  with piecewise constant sample paths. In particular,  $J$  is given by

٦

 $3.5$  Processes with Jumps  $135$ 

$$J(t) = \sum_{j=1}^{N(t)} (Y_j - 1)$$
 (3.80)

where  $Y_1, Y_2, \ldots$  are random variables and  $N(t)$  is a *counting process*. This means that there are random arrival times

$$0 < \tau_1 < \tau_2 < \cdots$$

and

$$N(t) = \sup\{n : \tau_n \le t\}$$

counts the number of arrivals in [0, t]. The symbol  $dJ(t)$  in (3.79) stands for the jump in J at time t. The size of this jump is  $Y_j - 1$  if  $t = \tau_j$  and 0 if t does not coincide with any of the  $\tau_i$ .

In the presence of jumps, a symbol like  $S(t)$  is potentially ambiguous: if it is possible for S to jump at t, we need to specify whether  $S(t)$  means the value of  $S$  just before or just after the jump. We follow the usual convention of assuming that our processes are continuous from the right, so

$$S(t) = \lim_{u \downarrow t} S(u)$$

includes the effect of any jump at  $t$ . To specify the value just before a potential jump we write  $S(t-)$ , which is the limit

$$S(t-) = \lim_{u \uparrow t} S(u)$$

from the left.

If we write  $(3.79)$  as

$$dS(t) = \mu S(t-) \, dt + \sigma S(t-) \, dW(t) + S(t-) \, dJ(t),$$

we see that the increment  $dS(t)$  in S at t depends on the value of S just before a potential jump at  $t$  and not on the value just after the jump. This is as it should be. The jump in S at time t is  $S(t) - S(t-)$ . This is 0 unless J jumps at t, which is to say unless  $t = \tau_j$  for some j. The jump in S at  $\tau_j$  is

$$S(\tau_j) - S(\tau_j -) = S(\tau_j -)[J(\tau_j) - J(\tau_j -)] = S(\tau_j -)(Y_j - 1)$$

hence

$$S(\tau_j) = S(\tau_j -)Y_j.$$

This reveals that the  $Y_j$  are the ratios of the asset price before and after a jump — the jumps are multiplicative. This also explains why we wrote  $Y_j - 1$ rather than simply  $Y_j$  in (3.80).

By restricting the  $Y_j$  to be positive random variables, we ensure that  $S(t)$ can never become negative. In this case, we see that

$$\log S(\tau_j) = \log S(\tau_j -) + \log Y_j,$$

so the jumps are additive in the logarithm of the price. Additive jumps are a natural extension of Brownian motion and multiplicative jumps (as in  $(3.79)$ ) provide a more natural extension of geometric Brownian motion; see the discussion at the beginning of Section 3.2. The solution of  $(3.79)$  is given by

$$S(t) = S(0)e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W(t)} \prod_{j=1}^{N(t)} Y_j,$$
(3.81)

which evidently generalizes the corresponding solution for geometric Brownian motion.

Thus far, we have not imposed any distributional assumptions on the jump process  $J(t)$ . We now consider the simplest model — the one studied by Merton [263] — which takes  $N(t)$  to be a Poisson process with rate  $\lambda$ . This makes the interarrival times  $\tau_{j+1} - \tau_j$  independent with a common exponential distribution.

$$P(\tau_{j+1} - \tau_j \le t) = 1 - e^{-\lambda t}, \quad t \ge 0.$$

We further assume that the  $Y_j$  are i.i.d. and independent of N (as well as W). Under these assumptions,  $J$  is called a *compound Poisson process*.

As noted by Merton [263], the model is particularly tractable when the  $Y_i$ are lognormally distributed, because a product of lognormal random variables is itself lognormal. In more detail, if  $Y_j \sim LN(a,b^2)$  (so that  $\log Y_j \sim N(a,b^2)$ ) then for any fixed  $n$ ,

$$\prod_{j=1}^{n} Y_j \sim LN(an, b^2 n).$$

It follows that, conditional on  $N(t) = n$ ,  $S(t)$  has the distribution of

$$S(0)e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W(t)} \prod_{j=1}^n Y_j \sim S(0) \cdot LN((\mu - \frac{1}{2}\sigma^2)t, \sigma^2t) \cdot LN(an, b^2n)$$
  
=  $LN(\log S(0) + (\mu - \frac{1}{2}\sigma^2)t + an, \sigma^2t + b^2n),$ 

using the independence of the  $Y_i$  and W. If we let  $F_{n,t}$  denote this lognormal distribution (cf. Section 3.2.1) and recall that  $N(t)$  has a Poisson distribution with mean  $\lambda t$ , then from the Poisson probabilities (3.75) we find that the unconditional distribution of  $S(t)$  is

$$P(S(t) \le x) = \sum_{n=0}^{\infty} e^{-\lambda t} \frac{(\lambda t)^n}{n!} F_{n,t}(x),$$

a Poisson mixture of lognormal distributions. Merton  $|263|$  used this property to express the price of an option on  $S$  as an infinite series, each term of which is the product of a Poisson probability and a Black-Scholes formula.

Recall that in the absence of jumps the drift  $\mu$  in (3.79) would be the risk-free rate, assuming the asset pays no dividends and assuming the model represents the dynamics under the risk-neutral measure. Suppose, for simplicity, that the risk-free rate is a constant  $r$ ; then the drift is determined by the condition that  $S(t)e^{-rt}$  be a martingale. Merton [263] extends this principle to his jump-diffusion model under the assumption that jumps are specific to a single stock and can be diversified away; that is, by assuming that the market does not compensate investors for bearing the risk of jumps. We briefly describe how this assumption determines the drift parameter  $\mu$  in (3.79).

A standard property of the Poisson process is that  $N(t) - \lambda t$  is a martingale. A generalization of this property is that

$$\sum_{i=1}^{N(t)} h(Y_j) - \lambda \mathsf{E}[h(Y)]t$$

is a martingale for i.i.d.  $Y, Y_1, Y_2$  and any function h for which  $E[h(Y)]$  is finite. Accordingly, the process

$$J(t) - \lambda m t$$

is a martingale if  $m = \mathsf{E}[Y_i] - 1$ . The choice of drift parameter in (3.79) that makes  $S(t)e^{-rt}$  a martingale is therefore  $\mu = r - \lambda m$ . In this case, if we rewrite  $(3.79)$  as

$$\frac{dS(t)}{S(t-)} = r dt + \sigma dW(t) + [dJ(t) - \lambda m dt],$$

the last two terms on the right are martingales and the net growth rate in  $S(t)$  is indeed r.

With this notation and with  $\log Y_i \sim N(a, b^2)$ , Merton's [263] option pricing formula becomes

$$e^{-rT}\mathsf{E}[(S(T)-K)^{+}] = \sum_{n=0}^{\infty} e^{-\lambda t} \frac{(\lambda t)^{n}}{n!} e^{-rT}\mathsf{E}[(S(T)-K)^{+}|N(T)=n]$$
$$= \sum_{n=0}^{\infty} e^{-\lambda' t} \frac{(\lambda' t)^{n}}{n!} \mathrm{BS}(S(0), \sigma_{n}, T, r_{n}, K),$$

where  $\lambda' = \lambda(1+m)$ ,  $\sigma_n^2 = \sigma^2 + b^2n/T$ ,  $r_n = r - \lambda m + n\log(1+m)/T$ , and  $BS(\cdot)$  denotes the Black-Scholes call option formula (1.4).

# Simulating at Fixed Dates

We consider two approaches to simulating the jump-diffusion model  $(3.79)$ , each of which is an instance of a more general strategy for simulating a broader class of jump-diffusion models. In the first method, we simulate the process at a fixed set of dates  $0 = t_0 < t_1 < \cdots < t_n$  without explicitly distinguishing

 $\mathcal{L}_{\mathcal{L}}$ 

the effects of the jump and diffusion terms. In the second method, we simulate the jump times  $\tau_1, \tau_2, \ldots$  explicitly.

We continue to assume that N is a Poisson process, that  $Y_1, Y_2, \ldots$  are i.i.d., and that N, W, and  $\{Y_1, Y_2, \ldots\}$  are mutually independent. We do not assume the  $Y_j$  are lognormally distributed, though that will constitute an interesting special case.

To simulate  $S(t)$  at time  $t_1, \ldots, t_n$ , we generalize (3.81) to

$$S(t_{i+1}) = S(t_i)e^{(\mu - \frac{1}{2}\sigma^2)(t_{i+1} - t_i) + \sigma[W(t_{i+1}) - W(t_i)]} \prod_{j=N(t_i)+1}^{N(t_{i+1})} Y_j,$$

with the usual convention that the product over j is equal to 1 if  $N(t_{i+1}) =$  $N(t_i)$ . We can simulate directly from this representation or else set  $X(t)$  $\log S(t)$  and

$$X(t_{i+1}) = X(t_i) + (\mu - \frac{1}{2}\sigma^2)(t_{i+1} - t_i) + \sigma[W(t_{i+1}) - W(t_i)] + \sum_{j=N(t_i)+1}^{N(t_{i+1})} \log Y_j;$$
(3.82)

this recursion replaces products with sums and is preferable, at least if sampling  $\log Y_i$  is no slower than sampling  $Y_i$ . We can exponentiate simulated values of the  $X(t_i)$  to produce samples of the  $S(t_i)$ .

A general method for simulating (3.82) from  $t_i$  to  $t_{i+1}$  consists of the following steps:

- 1. generate  $Z \sim N(0,1)$
- 2. generate  $N \sim \text{Poisson}(\lambda(t_{i+1}-t_i))$  (see Figure 3.9); if  $N=0$ , set  $M=0$ and go to Step  $4$
- 3. generate  $\log Y_1, \ldots, \log Y_N$  from their common distribution and set  $M =$  $\log Y_1 + \ldots + \log Y_N$

 $4. \text{ set}$ 

$$X(t_{i+1}) = X(t_i) + \left(\mu - \frac{1}{2}\sigma^2\right)(t_{i+1} - t_i) + \sigma\sqrt{t_{i+1} - t_i}Z + M$$

This method relies on two properties of the Poisson process: the increment  $N(t_{i+1}) - N(t_i)$  has a Poisson distribution with mean  $\lambda(t_{i+1} - t_i)$ , and it is independent of increments of N over  $[0, t_i]$ .

Under further assumptions on the distribution of the  $Y_i$ , this method can sometimes be simplified. If the  $Y_j$  have the lognormal distribution  $LN(a, b^2)$ , then  $\log Y_i \sim N(a, b^2)$  and

$$\sum_{j=1}^{n} \log Y_j \sim N(an, b^2 n) = an + b\sqrt{n}N(0, 1).$$

In this case, we may therefore replace Step  $3$  with the following:

3'. generate  $Z_2 \sim N(0,1)$ ; set  $M = aN + b\sqrt{N}Z_2$ 

If the  $\log Y_i$  have a gamma distribution with shape parameter a and scale parameter  $\beta$  (see (3.74)), then

$$\log Y_1 + \log Y_2 + \dots + \log Y_n$$

has the gamma distribution with shape parameter  $an$  and scale parameter  $\beta$ . Consequently, in Step 3 above we may sample M directly from a gamma distribution, conditional on the value of  $N$ .

Kou [215] proposes and analyzes a model in which  $|\log Y_i|$  has a gamma distribution (in fact exponential) and the sign of  $\log Y_j$  is positive with probability q, negative with probability  $1-q$ . In this case, conditional on the Poisson random variable N taking the value n, the number of  $\log Y_j$  with positive sign has a binomial distribution with parameters  $n$  and  $q$ . Step 3 can therefore be replaced with the following:

 $3a''$ . generate  $K \sim \text{Binomial}(N,q)$  $3b''$ . generate  $R_1 \sim \text{Gamma}(Ka,\beta)$  and  $R_2 \sim \text{Gamma}((N-K)a,\beta)$  and set  $M = R_1 - R_2$ 

In  $3b''$ , interpret a gamma random variable with shape parameter zero as the constant 0 in case  $K = 0$  or  $K = N$ . In 3a'', conditional on  $N = n$ , the binomial distribution of  $K$  is given by

$$P(K=k) = \frac{n!}{k!(n-k)!}q^k(1-q)^{n-k}, \quad k = 0, 1, \dots, n.$$

Samples from this distribution can be generated using essentially the same method used for the Poisson distribution in Figure 3.9 by changing just the first and sixth lines of that algorithm. In the first line, replace the mass at the origin  $\exp(-\theta)$  for the Poisson distribution with the corresponding value  $(1 - \theta)$  $q)^n$  for the binomial distribution. Observe that the ratio  $P(K = k)/P(K = k)$  $(k-1)$  is given by  $q(n+1-k)/k(1-q)$ , so the sixth line of the algorithm becomes  $p \leftarrow pq(n+1-N)/N(1-q)$  (where N now refers to the binomial random variable produced by the algorithm).

### Simulating Jump Times

Simulation methods based on (3.82) produce values  $S(t_i) = \exp(X(t_i)),$  $i = 1, \ldots, n$ , with the exact joint distribution of the target process (3.79) at dates  $t_1, \ldots, t_n$ . Notice, however, that this approach does not identify the times at which  $S(t)$  jumps; rather, it generates the total number of jumps in each interval  $(t_i, t_{i+1}]$ , using the fact that the number of jumps has a Poisson distribution.

An alternative approach to simulating  $(3.79)$  simulates the jump times  $\tau_1, \tau_2, \ldots$  explicitly. From one jump time to the next,  $S(t)$  evolves like an

 $\mathcal{N}_{\mathcal{L}}$ 

ordinary geometric Brownian motion because we have assumed that  $W$  and  $J$  in (3.79) are independent of each other. It follows that, conditional on the times  $\tau_1, \tau_2, \ldots$  of the jumps,

$$S(\tau_{j+1}-) = S(\tau_j)e^{(\mu - \frac{1}{2}\sigma^2)(\tau_{j+1}-\tau_j) + \sigma[W(\tau_{j+1})-W(\tau_j)]}$$

and

$$S(\tau_{j+1}) = S(\tau_{j+1} -)Y_{j+1}.$$

Taking logarithms and combining these steps, we get

$$X(\tau_{j+1}) = X(\tau_j) + (\mu - \frac{1}{2}\sigma^2)(\tau_{j+1} - \tau_j) + \sigma[W(\tau_{j+1}) - W(\tau_j)] + \log Y_{j+1}.$$

A general scheme for simulating one step of this recursion now takes the following form:

- 1. generate  $R_{j+1}$  from the exponential distribution with mean  $1/\lambda$
- 2. generate  $Z_{i+1} \sim N(0,1)$
- 3. generate  $\log Y_{j+1}$
- 4. set  $\tau_{j+1} = \tau_j + R_{j+1}$  and

$$X(\tau_{j+1}) = X(\tau_j) + (\mu - \frac{1}{2}\sigma^2)R_{j+1} + \sigma\sqrt{R_{j+1}}Z_{j+1} + \log Y_{j+1}.$$

Recall from Section 2.2.1 that the exponential random variable  $R_{i+1}$  can be generated by setting  $R_{j+1} = -\log(U)/\lambda$  with  $U \sim \text{Unif}[0,1]$ .

The two approaches to simulating  $S(t)$  can be combined. For example, suppose we fix a date  $t$  in advance that we would like to include among the simulated dates. Suppose it happens that  $\tau_j < t < \tau_{j+1}$  (i.e.,  $N(t) = N(t-)$  $j$ ). Then

$$S(t) = S(\tau_j) e^{(\mu - \frac{1}{2}\sigma^2)(t - \tau_j) + \sigma[W(t) - W(\tau_j)]}$$

and

$$S(\tau_{j+1}) = S(t)e^{(\mu - \frac{1}{2}\sigma^2)(\tau_{j+1} - t) + \sigma[W(\tau_{j+1}) - W(t)]}Y_{j+1}$$

Both approaches to simulating the basic jump-diffusion process  $(3.79)$  simulating the number of jumps in fixed subintervals and simulating the times at which jumps occur  $-$  can be useful at least as approximations in simulating more general jump-diffusion models. Exact simulation becomes difficult when the times of the jumps and the evolution of the process between jumps are no longer independent of each other.

# Inhomogeneous Poisson Process

A simple extension of the jump-diffusion model  $(3.79)$  replaces the constant jump intensity  $\lambda$  of the Poisson process with a deterministic (nonnegative) function of time  $\lambda(t)$ . This means that

$$P(N(t+h) - N(t) = 1|N(t)) = \lambda(t)h + o(h)$$

and  $N(t)$  is called an *inhomogeneous* Poisson process. Like an ordinary Poisson process it has independent increments and these increments are Poisson distributed, but increments over different intervals of equal length can have different means. In particular, the number of jumps in an interval  $(t_i, t_{i+1}]$ has a Poisson distribution with mean  $\Lambda(t_{i+1}) - \Lambda(t_i)$ , where

$$\Lambda(t) = \int_0^t \lambda(u) \, du.$$

Provided this function can be evaluated, simulation based on  $(3.82)$  generalizes easily to the inhomogeneous case: where we previously sampled from the Poisson distribution with mean  $\lambda(t_{i+1}-t_i)$ , we now sample from the Poisson distribution with mean  $\Lambda(t_{i+1}) - \Lambda(t_i)$ .

It is also possible to simulate the interarrival times of the jumps. The key property is

$$P(\tau_{j+1}-\tau_j\leq t|\tau_1,\ldots,\tau_j)=1-\exp(-[\Lambda(\tau_j+t)-\Lambda(\tau_j)]),\quad t\geq 0,$$

provided  $\Lambda(\infty) = \infty$ . We can (at least in principle) sample from this distribution using the inverse transform method discussed in Section 2.2.1. Given  $\tau_i$ , let

$$X = \inf \left\{ t \ge 0 : 1 - \exp\left(-\int_{\tau_j}^t \lambda(u) \, du\right) = U \right\}, \quad U \sim \text{Unif}[0,1]$$

then X has the required interarrival time distribution and we may set  $\tau_{j+1}$  $\tau_j + X$ . This is equivalent to setting

$$X = \inf \left\{ t \ge 0 : \int_{\tau_j}^t \lambda(u) \, du = \xi \right\} \tag{3.83}$$

where  $\xi$  is exponentially distributed with mean 1. We may therefore interpret the time between jumps as the time required to consume an exponential random variable if it is consumed at rate  $\lambda(u)$  at time u.

If the time-varying intensity  $\lambda(t)$  is bounded by a constant  $\lambda$ , the jumps of the inhomogeneous Poisson process can be generated by  $thinning$  an ordinary Poisson process  $\bar{N}$  with rate  $\bar{\lambda}$ , as in Lewis and Shedler [235]. In this procedure, the jump times of  $\bar{N}$  become *potential* jump times of  $N$ ; a potential jump at time t is accepted as an actual jump with probability  $\lambda(t)/\bar{\lambda}$ . A bit more explicitly, we have the following steps:

- 1. generate jump times  $\bar{\tau}_j$  of N (the interarrival times  $\bar{\tau}_{j+1} \bar{\tau}_j$  are independent and exponentially distributed with mean  $1/\lambda$ )
- 2. for each j generate  $U_j \sim \text{Unif}[0,1]$ ; if  $U_j\bar{\lambda} < \lambda(\bar{\tau}_j)$  then accept  $\bar{\tau}_j$  as a jump time of  $N$ .

Figure  $3.10$  illustrates this construction.

![](_page_63_Figure_0.jpeg)

![](_page_63_Figure_1.jpeg)

**Fig. 3.10.** Construction of an inhomogeneous Poisson process from an ordinary  $\mathbf{F}$ Poisson process by thinning. The horizontal coordinates of the open circles are the jump times of a Poisson process with rate  $\lambda$ ; each circle is raised to a height uniformly distributed between 0 and  $\bar{\lambda}$ . Circles below the curve  $\lambda(t)$  are accepted as jumps of the inhomogeneous Poisson process. The times of the accepted jumps are indicated by the filled circles.

# 3.5.2 Pure-Jump Processes

If  $S(t)$  is the jump-diffusion process in (3.79) with  $J(t)$  a compound Poisson process, then  $X(t) = \log S(t)$  is a process with independent increments. This is evident from  $(3.82)$  and the fact that both W and J have independent increments. Geometric Brownian motion also has the property that its logarithm has independent increments. It is therefore natural to ask what other potentially fruitful models of asset prices might arise from the representation

$$S(t) = S(0) \exp(X(t)) \tag{3.84}$$

with  $X$  having independent increments. Notice that we have adopted the normalization  $X(0) = 0$ .

The process X is a  $Lévy$  process if it has stationary, independent increments and satisfies the technical requirement that  $X(t)$  converges in distribution to  $X(s)$  as  $t \rightarrow s$ . Stationarity of the increments means that  $X(t+s)-X(s)$  has the distribution of  $X(t)$ . Every Lévy process can be represented as the sum of a deterministic drift, a Brownian motion, and a pure-jump process independent of the Brownian motion (see, e.g., Chapter 4 of Sato  $[317]$ ). If the number of jumps in every finite interval is almost surely finite, then the pure-jump component is a compound Poisson process. Hence, in constructing processes of the form  $(3.84)$  with X a Lévy process, the only way to move beyond the jump-diffusion process  $(3.79)$  is to consider processes with an infinite number of jumps in finite intervals. We will in fact focus on pure-jump processes of this type — that is,  $Lévy$  processes with no Brownian component. Several processes of this type have been proposed as models of asset prices, and we consider some of these examples. A more extensive discussion of the simulation of Lévy process can be found in Asmussen [21].

It should be evident that in considering processes with an infinite number of jumps in finite intervals, only the first of the two approaches developed in Section  $3.5.1$  is viable: we may be able to simulate the increments of such a process, but we cannot hope to simulate from one jump to the next. To simulate a pure-jump Lévy process we should therefore consider the distribution of its increments over a fixed time grid.

A random variable  $Y$  (more precisely, its distribution) is said to be in*finitely divisible* if for each  $n = 2, 3, \ldots$ , there are i.i.d. random variables  $Y_1^{(n)}, \ldots, Y_n^{(n)}$  such that  $Y_1^{(n)} + \cdots + Y_n^{(n)}$  has the distribution of Y. If X is a Lévy process  $(X(0) = 0)$ , then

$$X(t) = X(t/n) + [X(2t/n) - X(t/n)] + \dots + [X(t) - X((n-1)t/n)]$$

decomposes  $X(t)$  as the sum of n i.i.d. random variables and shows that  $X(t)$ has an infinitely divisible distribution. Conversely, for each infinitely divisible distribution there is a Lévy process for which  $X(1)$  has that distribution. Simulating a Lévy process on a fixed time grid is thus equivalent to sampling from infinitely divisible distributions.

A Lévy process with nondecreasing sample paths is called a *subordinator*. A large class of  $Lévy$  processes (sometimes called processes of type G) can be represented as  $W(G(t))$  with W Brownian motion and G a subordinator independent of  $W$ . Several of the examples we consider belong to this class.

# Gamma Processes

If  $Y_1,\ldots,Y_n$  are independent with distribution  $\text{Gamma}(a/n,\beta)$ , then  $Y_1$  +  $\cdots + Y_n$  has distribution Gamma $(a, \beta)$ ; thus, gamma distributions are infinitely divisible. For each choice of the parameters a and  $\beta$  there is a Lévy process (called a *gamma process*) such that  $X(1)$  has distribution Gamma $(a, \beta)$ . We can simulate this process on a time grid  $t_1, \ldots, t_n$  by sampling the increments

$$X(t_{i+1}) - X(t_i) \sim \text{Gamma}(a \cdot (t_{i+1} - t_i), \beta)$$

independently, using the methods of Sections  $3.4.2$ .

A gamma random variable takes only positive values so a gamma process is nondecreasing. This makes it unsuitable as a model of (the logarithm of) a risky asset price. Madan and Seneta [243] propose a model based on  $(3.84)$  and  $X(t) = U(t) - D(t)$ , with U and D independent gamma processes representing the up and down moves of  $X$ . They call this the *variance gamma process*. Increments of  $X$  can be simulated through the increments of  $U$  and  $D$ .

If  $U(1)$  and  $D(1)$  have the same shape and scale parameters, then X admits an alternative representation as  $W(G(t))$  where W is a standard Brownian motion and G is a gamma process. In other words, X can be viewed as the result of applying a random time-change to an ordinary Brownian motion: the deterministic time argument t has been replaced by the random time  $G(t)$ ,

which becomes the conditional variance of  $W(G(t))$  given  $G(t)$ . This explains the name "variance gamma."

Madan et al. [242] consider the more general case  $W(G(t))$  where W now has drift parameter  $\mu$  and variance parameter  $\sigma^2$ . They restrict the shape parameter of  $G(1)$  to be the reciprocal of its scale parameter  $\beta$  (so that  $E[G(t)] = t$  and show that this more general variance gamma process can still be represented as the difference  $U(t) - D(t)$  of two independent gamma processes. The shape and scale parameters of  $U(1)$  and  $D(1)$  should be chosen to satisfy  $a_U = a_D = 1/\beta$  and

$$\beta_U \beta_D = \frac{\sigma^2 \beta}{2}, \quad \beta_U - \beta_D = \mu \beta.$$

The general variance gamma process can therefore still be simulated as the difference between two independent gamma processes. Alternatively, we can use the representation  $X(t) = W(G(t))$  for simulation. Conditional on the increment  $G(t_{i+1})-G(t_i)$ , the increment  $W(G(t_{i+1}))-W(G(t_i))$  has a normal distribution with mean  $\mu[G(t_{i+1})-G(t_i)]$  and variance  $\sigma^2[G(t_{i+1})-G(t_i)]$ . Hence, we can simulate  $X$  as follows:

- 1. generate  $Y \sim \text{Gamma}((t_{i+1} t_i)/\beta, \beta)$  (this is the increment in G)
- 2. generate  $Z \sim N(0,1)$
- 3. set  $X(t_{i+1}) = X(t_i) + \mu Y + \sigma \sqrt{Y} Z$ .

The relative merits of this method and simulation through the difference of  $U$ and  $D$  depend on the implementation details of the methods used for sampling from the gamma and normal distributions.

Figure 3.11 compares two variance gamma densities with a normal density; all three have mean  $0$  and standard deviation  $0.4$ . The figure illustrates the much higher kurtosis that can be achieved within the variance gamma family. Although the examples in the figure are symmetric, positive and negative skewness can be introduced through the parameter  $\mu$ .

### Normal Inverse Gaussian Processes

This class of processes, described in Barndorff-Nielsen [36], has some similarities to the variance gamma model. It is a Lévy process whose increments have a normal inverse Gaussian distribution; it can also be represented through a random time-change of Brownian motion.

The inverse Gaussian distribution with parameters  $\delta, \gamma > 0$  has density

$$f_{IG}(x) = \frac{\delta e^{\delta \gamma}}{\sqrt{2\pi}} x^{-3/2} \exp\left(-\frac{1}{2}(\delta^2 x^{-1} + \gamma^2 x)\right), \quad x > 0.$$
 (3.85)

This is the density of the first passage time to level  $\delta$  of a Brownian motion with drift  $\gamma$ . It has mean  $\delta/\gamma$  and variance  $\delta/\gamma^3$ . The inverse Gaussian distribution is infinitely divisible: if  $X_1$  and  $X_2$  are independent and have this density

![](_page_66_Figure_1.jpeg)

**Fig. 3.11.** Examples of variance gamma densities. The most peaked curve has  $\mu = 0$ ,  $\sigma = 0.4$ , and  $\beta = 1$  (and is in fact a double exponential density). The next most peaked curve has  $\mu = 0$ ,  $\sigma = 0.4$ , and  $\beta = 0.5$ . The dashed line is the normal density with mean  $0$  and standard deviation  $0.4$ .

with parameters  $(\delta_1, \gamma)$  and  $(\delta_2, \gamma)$ , then it is clear from the first passage time interpretation that  $X_1 + X_2$  has this density with parameters  $(\delta_1 + \delta_2, \gamma)$ . It follows that there is a Lévy process  $Y(t)$  for which  $Y(1)$  has density (3.85).

The *normal* inverse Gaussian distribution  $NIG(\alpha, \beta, \mu, \delta)$  with parameters  $\alpha, \beta, \mu, \delta$  can be described as the distribution of

$$\mu + \beta Y(1) + \sqrt{Y(1)}Z, \quad Z \sim N(0, 1),\n$$
(3.86)

with  $Y(1)$  having density (3.85),  $\alpha = \sqrt{\beta^2 + \gamma^2}$ , and Z independent of  $Y(1)$ . The mean and variance of this distribution are

$$\mu + \frac{\delta \beta}{\alpha \sqrt{1 - (\beta/\alpha)^2}} \quad \text{ and } \quad \frac{\delta}{\alpha (1 - (\beta/\alpha)^2)^{3/2}},$$

respectively. The density is given in Barndorff-Nielsen [36] in terms of a modified Bessel function. Three examples are graphed in Figure  $3.12$ ; these illustrate the possibility of positive and negative skew and high kurtosis within this family of distributions.

Independent normal inverse Gaussian random variables add in the following way:

$$NIG(\alpha, \beta, \mu_1, \delta_1) + NIG(\alpha, \beta, \mu_2, \delta_2) = NIG(\alpha, \beta, \mu_1 + \mu_2, \delta_1 + \delta_2).$$

In particular, these distributions are infinitely divisible. Barndorff-Nielsen [36] studies Lévy processes with NIG increments. Such a process  $X(t)$  can be represented as  $W(Y(t))$  with  $Y(t)$  the Lévy process defined from (3.85) and W a Brownian motion with drift  $\beta$ , unit variance, and initial value  $W(0) = \mu$ . At  $t = 1$ , this representation reduces to (3.86).

![](_page_67_Figure_1.jpeg)

Fig. 3.12. Examples of normal inverse Gaussian densities. The parameters  $(\alpha, \beta, \mu, \delta)$  are as follows:  $(1, -0.75, 2, 1)$  for A,  $(1, 0, 0, 1)$  for B, and  $(1, 2, -0.75, 1)$ for C. The dashed line is the standard normal density and is included for comparison with case  $B$ , which also has mean 0 and standard deviation 1.

Eberlein  $[109]$  discusses the use of the NIG Lévy processes (in fact, a more general family called *generalized hyperbolic* Lévy processes) in modeling log returns. Barndorff-Nielsen [36] proposes several mechanisms for constructing models of price processes using NIG Lévy processes as a building block.

As with the variance gamma process of Madan and Seneta [243], there are in principle two strategies for simulating  $X$  on a discrete time grid. We can simulate the increments by sampling from the NIG distribution directly or we can use the representation as a time-changed Brownian motion (as in  $(3.86)$ ). However, direct sampling from the NIG distribution does not appear to be particularly convenient, so we consider only the second of these two  $alternatives.$ 

To simulate  $X(t)$  as  $W(Y(t))$  we need to be able to generate the increments of  $Y$  by sampling from the (ordinary) inverse Gaussian distribution. An interesting method for doing this was developed by Michael, Schucany, and Haas [264]. Their method uses the fact that if Y has the density in  $(3.85)$ ,  $\text{then}$ 

$$\frac{(\gamma Y - \delta)^2}{Y} \sim \chi_1^2;$$

we may therefore sample Y by first generating  $V \sim \chi^2_1$ . Given a value of V, the resulting equation for  $Y$  has two roots,

$$y_1 = \frac{\delta}{\gamma} + \frac{V}{2\gamma^2} - \frac{1}{2\delta\gamma}\sqrt{4\delta^3 V/\gamma + \delta^2 V^2/\gamma}$$

 $\text{and}$ 

$$y_2 = \delta^2/\gamma^2 y_1.$$

Michael et al. [264] show that the smaller root  $y_1$  should be chosen with probability  $\delta/(\delta + \gamma y_1)$  and the larger root  $y_2$  with the complementary probability. Figure 3.13 illustrates the implementation of the method. The  $\chi^2_1$  random variable required for this algorithm can be generated as either a  $\text{Gamma}(1/2, 2)$ or as the square of a standard normal.

$$\begin{aligned} &\text{Setup: } a \leftarrow 1/\gamma, \, b \leftarrow a * \delta, \, b \leftarrow b * b \\ &\text{generate } V \sim \chi_1^2 \\ &\xi \leftarrow a * V \\ &Y \leftarrow a * (\delta + (\xi/2) + \sqrt{\xi * (\delta + (\xi/4))} \\ &p \leftarrow \delta/(\delta + \gamma * Y) \\ &\text{generate } U \sim \text{Unif}[0,1] \\ &\text{if } U > p \text{ then } Y \leftarrow b/Y \\ &\text{return } Y \end{aligned}$$

**Fig. 3.13.** Algorithm for sampling from the inverse Gaussian distribution  $(3.85)$ , based on Michael et al.  $[264]$ .

To simulate an increment of the NIG process  $X(t) = W(Y(t))$  from  $t_i$  to  $t_{i+1}$ , we use the algorithm in Figure 3.13 to generate a sample Y from the inverse Gaussian distribution with parameters  $\delta(t_{i+1}-t_i)$  and  $\gamma$ ; we then set

$$X(t_{i+1}) = X(t_i) + \beta Y + \sqrt{YZ}$$

with  $Z \sim N(0,1)$ . (Recall that  $\beta$  is the drift of W in the NIG parameterization.)

Despite the evident similarity between this construction and the one used for the variance gamma process, a result of Asmussen and Rosiński [25] points to an important distinction between the two processes: the cumulative effect of small jumps can be well-approximated by Brownian motion in a NIG process but not in a variance gamma process. Loosely speaking, even the small jumps of the variance gamma process are too large or too infrequent to look like Brownian motion. Asmussen and Rosiński [25] discuss the use and applicability of a Brownian approximation to small jumps in simulating Lévy processes.

### Stable Paretian Processes

A distribution is called *stable* if for each  $n \geq 2$  there are constants  $a_n > 0$  and  $b_n$  such that

$$X_1 + X_2 + \dots + X_n =_{\mathrm{d}} a_n X + b_n,$$

where  $X, X_1, \ldots, X_n$  are independent random variables with that distribution. (The symbol "=<sub>d</sub>" indicates equality in distribution.) If  $b_n = 0$  for all n, the distribution is  $strictly$  stable. The best known example is the standard normal distribution for which

$$X_1 + X_2 + \dots + X_n =_{\rm d} n^{1/2} X.$$

In fact,  $a_n$  must be of the form  $n^{1/\alpha}$  for some  $0 < \alpha \leq 2$  called the *index* of the stable distribution. This is Theorem VI.1.1 of Feller [119]; for broader coverage of the topic see Samorodnitsky and Tagqu [316].

Stable random variables are infinitely divisible and thus define Lévy processes. Like the other examples in this section, these Lévy processes have no Brownian component (except in the case of Brownian motion itself) and are thus pure-jump processes. They can often be constructed by applying a random time change to an ordinary Brownian motion, the time change itself having stable increments.

Only the normal distribution has stable index  $\alpha = 2$ . Non-normal stable distributions (those with  $\alpha < 2$ ) are often called *stable Paretian*. These are heavy-tailed distributions: if X has stable index  $\alpha < 2$ , then  $\mathsf{E}[|X|^p]$  is infinite for  $p > \alpha$ . In particular, all stable Paretian distributions have infinite variance and those with  $\alpha \leq 1$  have  $\mathsf{E}[|X|] = \infty$ . Mandelbrot [246] proposed using stable Paretian distributions to model the high peaks and heavy tails (relative to the normal distribution) of market returns. Infinite variance suggests that the tails of these distributions may be *too* heavy for market data, but see Rachev and Mittnik  $[302]$  for a comprehensive account of applications in finance.

Stable random variables have probability densities but these are rarely available explicitly; stable distributions are usually described through their characteristic functions. The density is known for the normal case  $\alpha = 2$ ; the Cauchy (or  $t_1$ ) distribution, corresponding to  $\alpha = 1$  and density

$$f(x) = \frac{1}{\pi} \frac{1}{1+x^2}, \quad -\infty < x < \infty;$$

and the case  $\alpha = 1/2$  with density

$$f(x) = \frac{1}{\sqrt{2\pi}} x^{-3/2} \exp(-1/(2x)), \quad x > 0.$$

This last example may be viewed as a limiting case of the inverse Gaussian distribution with  $\gamma = 0$ . Through a first passage time interpretation (see Feller [119], Example VI.2(f)), the Cauchy distribution may be viewed as a limiting case of the NIG distribution  $\alpha = \beta = \mu = 0$ . Both densities given above can be generalized by introducing scale and location parameters (as in  $[316]$ , p.10). This follows from the simple observation that if  $X$  has a stable distribution then so does  $\mu + \sigma X$ , for any constants  $\mu, \sigma$ .

As noted in Example  $2.1.2$ , samples from the Cauchy distribution can be generated using the inverse transform method. If  $Z \sim N(0,1)$  then  $1/Z^2$  has

the stable density above with  $\alpha = 1/2$ , so this case is also straightforward. Perhaps surprisingly, it is also fairly easy to sample from other stable distributions even though their densities are unknown. An important tool in sampling from stable distributions is the following representation: if  $V$  is uniformly distributed over  $[-\pi/2, \pi/2]$  and W is exponentially distributed with mean 1, then

$$\frac{\sin(\alpha V)}{(\cos(V))^{1/\alpha}} \left(\frac{\cos((1-\alpha)V)}{W}\right)^{(1-\alpha)/\alpha}$$

has a symmetric α-stable distribution; see p.42 of Samorodnitsky and Tagqu [316] for a proof. As noted there, this reduces to the Box-Muller method (see Section 2.3.2) when  $\alpha = 2$ . Chambers, Mallows, and Stuck [79] develop simulation procedures based on this representation and additional transformations. Samorodnitsky and Taqqu [316], pp.46-49, provide computer code for sampling from an arbitrary stable distribution, based on Chambers et al. [79].

Feller [119], p.336, notes that the Lévy process generated by a symmetric stable distribution can be constructed through a random time change of Brownian motion. This also follows from the observation in Samorodnitsky and Taqqu  $[316]$ , p.21, that a symmetric stable random variable can be generated as the product of a normal random variable and a positive stable random variable, a construction similar to  $(3.86)$ .

# 3.6 Forward Rate Models: Continuous Rates

The distinguishing feature of the models considered in this section and the next is that they explicitly describe the evolution of the full term structure of interest rates. This contrasts with the approach in Sections  $3.3$  and  $3.4$  based on modeling the dynamics of just the short rate  $r(t)$ . In a setting like the Vasicek model or the Cox-Ingersoll-Ross model, the current value of the short rate determines the current value of all other term structure quantities forward rates, bond prices, etc. In these models, the state of the world is completely summarized by the value of the short rate. In multifactor extensions, like those described in Section 3.3.3, the state of the world is summarized by the current values of a finite number (usually small) of underlying factors; from the values of these factors all term structure quantities are determined, at least in principle.

In the framework developed by Heath, Jarrow, and Morton  $[174]$  (HJM), the state of the world is described by the full term structure and not necessarily by a finite number of rates or factors. The key contribution of HJM lies in identifying the restriction imposed by the absence of arbitrage on the evolution of the term structure.

At any point in time the term structure of interest rates can be described in various equivalent ways — through the prices or yields of zero-coupon

bonds or par bonds, through forward rates, and through swap rates, to name just a few examples. The HJM framework models the evolution of the term structure through the dynamics of the forward rate curve. It could be argued that forward rates provide the most primitive description of the term structure (and thus the appropriate starting point for a model) because bond prices and vields reflect averages of forward rates across maturities, but it seems difficult to press this point too far.

From the perspective of simulation, this section represents a departure from the previous topics of this chapter. Thus far, we have focused on models that can be simulated exactly, at least at a finite set of dates. In the generality of the HJM setting, some discretization error is usually inevitable. HJM simulation might therefore be viewed more properly as a topic for Chapter 6; we include it here because of its importance and because of special simulation issues it raises.

### 3.6.1 The HJM Framework

The HJM framework describes the dynamics of the forward rate curve  $\{f(t,T), 0 \leq t \leq T \leq T^*\}$  for some ultimate maturity  $T^*$  (e.g., 20 or 30 years from today). Think of this as a curve in the maturity argument  $T$  for each value of the time argument  $t$ ; the length of the curve shrinks as time advances because  $t \leq T \leq T^*$ . Recall that the forward rate  $f(t,T)$  represents the instantaneous continuously compounded rate contracted at time  $t$  for riskless borrowing or lending at time  $T \geq t$ . This is made precise by the relation

$$B(t,T) = \exp\left(-\int_t^T f(t,u) \, du\right)$$

between bond prices and forward rates, which implies

$$f(t,T) = -\frac{\partial}{\partial T} \log B(t,T). \tag{3.87}$$

The short rate is  $r(t) = f(t, t)$ . Figure 3.14 illustrates this notation and the evolution of the forward curve.

In the HJM setting, the evolution of the forward curve is modeled through an SDE of the form

$$df(t,T) = \mu(t,T) dt + \sigma(t,T)^\top dW(t). \tag{3.88}$$

In this equation and throughout, the differential  $df$  is with respect to time t and not maturity T. The process  $W$  is a standard d-dimensional Brownian motion;  $d$  is the number of *factors*, usually equal to 1, 2, or 3. Thus, while the forward rate curve is in principle an infinite-dimensional object, it is driven by a low-dimensional Brownian motion. The coefficients  $\mu$  and  $\sigma$  in (3.88) (scalar and  $\Re^d$ -valued, respectively) could be stochastic or could depend on current

![](_page_72_Figure_1.jpeg)

**Fig. 3.14.** Evolution of forward curve. At time 0, the forward curve  $f(0, \cdot)$  is defined for maturities in  $[0, T^*]$  and the short rate is  $r(0) = f(0, 0)$ . At  $t > 0$ , the forward curve  $f(t,\cdot)$  is defined for maturities in  $[t,T^*]$  and the short rate is  $r(t) = f(t,t)$ .

and past levels of forward rates. We restrict attention to the case in which  $\mu$ and  $\sigma$  are deterministic functions of t,  $T \geq t$ , and the current forward curve  $\{f(t,u), t \leq u \leq T^*\}$ . Subject to technical conditions, this makes the evolution of the curve Markovian. We could make this more explicit by writing, e.g.,  $\sigma(f, t, T)$ , but to lighten notation we omit the argument f. See Heath, Jarrow, and Morton [174] for the precise conditions needed for  $(3.88)$ .

We interpret  $(3.88)$  as modeling the evolution of forward rates under the risk-neutral measure (meaning, more precisely, that  $W$  is a standard Brownian motion under that measure). We know that the absence of arbitrage imposes a condition on the risk-neutral dynamics of asset prices: the price of a (dividendfree) asset must be a martingale when divided by the numeraire

$$\beta(t) = \exp\left(\int_0^t r(u) \, du\right).$$

Forward rates are not, however, asset prices, so it is not immediately clear what restriction the absence of arbitrage imposes on the dynamics in  $(3.88)$ . To find this restriction we must start from the dynamics of asset prices, in particular bonds. Our account is informal; see Heath, Jarrow, and Morton  $[174]$  for a rigorous development.

To make the discounted bond prices  $B(t,T)/\beta(t)$  positive martingales, we posit dynamics of the form

$$\frac{dB(t,T)}{B(t,T)} = r(t) dt + \nu(t,T)^{\top} dW(t), \quad 0 \le t \le T \le T^*.$$
(3.89)

The bond volatilities  $\nu(t,T)$  may be functions of current bond prices (equivalently of current forward rates since  $(3.87)$  makes a one-to-one correspondence

between the two). Through  $(3.87)$ , the dynamics in  $(3.89)$  constrain the evolution of forward rates. By Itô's formula,

$$d\log B(t,T) = [r(t) - \frac{1}{2}\nu(t,T)^{\top}\nu(t,T)]\,dt + \nu(t,T)^{\top}dW(t)$$

If we now differentiate with respect to  $T$  and then interchange the order of differentiation with respect to  $t$  and  $T$ , from (3.87) we get

$$\begin{split} df(t,T) &= -\frac{\partial}{\partial T} d\log B(t,T) \\ &= -\frac{\partial}{\partial T} [r(t) - \frac{1}{2}\nu(t,T)^\top \nu(t,T)] \, dt - \frac{\partial}{\partial T} \nu(t,T)^\top dW(t). \end{split}$$

Comparing this with  $(3.88)$ , we find that we must have

$$\sigma(t,T) = -\frac{\partial}{\partial T}\nu(t,T)$$

and

$$\mu(t,T) = -\frac{\partial}{\partial T} [r(t) - \frac{1}{2}\nu(t,T)^{\top}\nu(t,T)] = \left(\frac{\partial}{\partial T}\nu(t,T)\right)^{\top}\nu(t,T).$$

To eliminate  $\nu(t,T)$  entirely, notice that

$$\nu(t,T) = -\int_t^T \sigma(t,u) \, du + \text{constant}.$$

But because  $B(t,T)$  becomes identically 1 as t approaches T (i.e., as the bond matures), we must have  $\nu(T,T) = 0$  and thus the constant in this equation is 0. We can therefore rewrite the expression for  $\mu$  as

$$\mu(t,T) = \sigma(t,T)^{\top} \int_{t}^{T} \sigma(t,u) \, du; \tag{3.90}$$

this is the risk-neutral drift imposed by the absence of arbitrage. Substituting in  $(3.88)$ , we get

$$df(t,T) = \left(\sigma(t,T)^{\top} \int_{t}^{T} \sigma(t,u) \, du\right) \, dt + \sigma(t,T)^{\top} \, dW(t). \tag{3.91}$$

This equation characterizes the arbitrage-free dynamics of the forward curve under the risk-neutral measure; it is the centerpiece of the HJM framework.

Using a subscript  $j = 1, \ldots, d$  to indicate vector components, we can write  $(3.91)$  as

$$df(t,T) = \sum_{j=1}^{d} \left( \sigma_j(t,T) \int_t^T \sigma_j(t,u) \, du \right) \, dt + \sum_{j=1}^{d} \sigma_j(t,T) \, dW_j(t). \tag{3.92}$$

This makes it evident that each factor contributes a term to the drift and that the combined drift is the sum of the contributions of the individual factors.

In (3.91), the drift is determined once  $\sigma$  is specified. This contrasts with the  $\text{dynamics of the short rate models in Sections 3.3 and 3.4 where parameters}$ of the drift could be specified independent of the diffusion coefficient without introducing arbitrage. Indeed, choosing parameters of the drift is essential in calibrating short rate models to an observed set of bond prices. In contrast, an HJM model is automatically calibrated to an initial set of bond prices  $B(0,T)$  if the initial forward curve  $f(0,T)$  is simply chosen consistent with these bond prices through  $(3.87)$ . Put slightly differently, calibrating an HJM model to an observed set of bond prices is a matter of choosing an appropriate initial condition rather than choosing a parameter of the model dynamics. The effort in calibrating an HJM model lies in choosing  $\sigma$  to match market prices of interest rate *derivatives* in addition to matching bond prices.

We illustrate the HJM framework with some simple examples.

**Example 3.6.1** Constant  $\sigma$ . Consider a single-factor  $(d = 1)$  model in which  $\sigma(t,T) \equiv \sigma$  for some constant  $\sigma$ . The interpretation of such a model is that each increment  $dW(t)$  moves all points on the forward curve  $\{f(t,u), t \leq u \leq t\}$  $T^*$  by an equal amount  $\sigma dW(t)$ ; the diffusion term thus introduces only parallel shifts in the forward curve. But a model in which the forward curve makes only parallel shifts admits arbitrage opportunities: one can construct a costless portfolio of bonds that will have positive value under every parallel shift. From (3.90) we find that an HJM model with constant  $\sigma$  has drift

$$\mu(t,T) = \sigma \int_t^T \sigma \, du = \sigma^2(T-t).$$

In particular, the drift will vary (slightly, because  $\sigma^2$  is small) across maturities, keeping the forward curve from making exactly parallel movements. This small adjustment to the dynamics of the forward curve is just enough to keep the model arbitrage-free. In this case, we can solve  $(3.91)$  to find

$$f(t,T) = f(0,T) + \int_0^t \sigma^2(T-u) \, du + \sigma W(t)$$
  
=  $f(0,T) + \frac{1}{2}\sigma^2[T^2 - (T-t)^2] + \sigma W(t).$ 

In essentially any model, the identity  $r(t) = f(t, t)$  implies

$$dr(t) = df(t,T)\Big|_{T=t} + \left.\frac{\partial}{\partial T}f(t,T)\right|_{T=t} dt.$$

In the case of constant  $\sigma$ , we can write this explicitly as

$$dr(t) = \sigma \, dW(t) + \left( \left. \frac{\partial}{\partial T} f(0, T) \right|_{T-t} + \sigma^2 t \right) \, dt.$$

Comparing this with (3.50), we find that an HJM model with constant  $\sigma$ coincides with a Ho-Lee model with calibrated drift.  $\Box$ 

**Example 3.6.2** Exponential  $\sigma$ . Another convenient parameterization takes  $\sigma(t,T) = \sigma \exp(-\alpha(T-t))$  for some constants  $\sigma,\alpha > 0$ . In this case, the diffusion term  $\sigma(t,T) dW(t)$  moves forward rates for short maturities more than forward rates for long maturities. The drift is given by

$$\mu(t,T) = \sigma^2 e^{-\alpha(T-t)} \int_t^T e^{-\alpha(T-u)} du = \frac{\sigma^2}{\alpha} \left( e^{-2\alpha(T-t)} - e^{-\alpha(T-t)} \right).$$

An argument similar to the one used in Example  $3.6.1$  shows that the short rate in this case is described by the Vasicek model with time-varying drift parameters.

This example and the one that precedes it may be misleading. It would be incorrect to assume that the short rate process in an HJM setting will always have a convenient description. Indeed, such examples are exceptional.  $\Box$ 

**Example 3.6.3** Proportional  $\sigma$ . It is tempting to consider a specification of the form  $\sigma(t,T) = \tilde{\sigma}(t,T)f(t,T)$  for some deterministic  $\tilde{\sigma}$  depending only on t and T. This would make  $\tilde{\sigma}(t,T)$  the volatility of the forward rate  $f(t,T)$ and would suggest that the distribution of  $f(t,T)$  is approximately lognormal. However, Heath et al. [174] note that this choice of  $\sigma$  is inadmissible: it produces forward rates that grow to infinity in finite time with positive probability. The difficulty, speaking loosely, is that if  $\sigma$  is proportional to the level of rates, then the drift is proportional to the rates *squared*. This violates the linear growth condition ordinarily required for the existence and uniqueness of solutions to SDEs (see Appendix  $B.2$ ). Market conventions often presuppose the existence of a (proportional) volatility for forward rates, so the failure of this example could be viewed as a shortcoming of the HJM framework. We will see in Section 3.7 that the difficulty can be avoided by working with simple rather than continuously compounded forward rates.  $\Box$ 

### Forward Measure

Although the HJM framework is usually applied under the risk-neutral measure, only a minor modification is necessary to work in a forward measure. Fix a maturity  $T_F$  and recall that the forward measure associated with  $T_F$  corresponds to taking the bond  $B(t,T_F)$  as numeraire asset. The forward measure  $P_{T_F}$  can be defined relative to the risk-neutral measure  $P_{\beta}$  through

$$\left(\frac{dP_{T_F}}{dP_{\beta}}\right)_t = \frac{B(t, T_F)\beta(0)}{\beta(t)B(0, T_F)}.$$

From the bond dynamics in  $(3.89)$ , we find that this ratio is given by

$$\exp\left(-\frac{1}{2}\int_0^t \nu(u,T_F)^\top \nu(u,T_F) \, du + \int_0^t \nu(u,T_F)^\top \, dW(u)\right).$$

By the Girsanov Theorem, the process  $W^{T_F}$  defined by

$$dW^{T_F}(t) = -\nu(t, T_F)^\top dt + dW(t)$$

is therefore a standard Brownian motion under  $P_{T_F}$ . Recalling that  $\nu(t,T)$  is the integral of  $-\sigma(t,u)$  from  $u=t$  to  $u=T$ , we find that the forward rate  $\text{dynamics } (3.91) \text{ become}$ 

$$\begin{split} df(t,T) &= -\sigma(t,T)^{\top} \nu(t,T) \, dt + \sigma(t,T)^{\top} [\nu(t,T_F)^{\top} \, dt + dW^{T_F}(t)] \\ &= -\sigma(t,T)^{\top} [\nu(t,T) - \nu(t,T_F)] \, dt + \sigma(t,T)^{\top} \, dW^{T_F}(t) \\ &= -\sigma(t,T)^{\top} \left( \int_T^{T_F} \sigma(t,u) \, du \right) \, dt + \sigma(t,T)^{\top} \, dW^{T_F}(t), \quad (3.93) \end{split}$$

for  $t \leq T \leq T_F$ . Thus, the HJM dynamics under the forward measure are similar to the dynamics under the risk-neutral measure, but where we previously integrated  $\sigma(t, u)$  from t to T, we now integrate  $-\sigma(t, u)$  from T to  $T_F$ . Notice that  $f(t,T_F)$  is a martingale under  $P_{T_F}$ , though none of the forward rates is a martingale under the risk-neutral measure.

### 3.6.2 The Discrete Drift

Except under very special choices of  $\sigma$ , exact simulation of (3.91) is infeasible. Simulation of the general HJM forward rate dynamics requires introducing a discrete approximation. In fact, each of the two arguments of  $f(t,T)$  requires discretization. For the first argument, fix a time grid  $0 = t_0 < t_1 < \cdots < t_1 < t_1 < \cdots < t_1 < t_1 < \cdots < t_1 < t_1 < t_1 < \cdots < t_1 < t_1 < t_1 < t_1 < t_1 < t_1 < t_1 < t_1 < t_1 < t_1$  $t_M$ . Even at a fixed time  $t_i$ , it is generally not possible to represent the full forward curve  $f(t_i,T), t_i \leq T \leq T^*$ , so instead we fix a grid of maturities and approximate the forward curve by its value for just these maturities. In principle, the time grid and the maturity grid could be different; however, assuming that the two sets of dates are the same greatly simplifies notation with little loss of generality.

We use hats to distinguish discretized variables from their exact continuoustime counterparts. Thus,  $\hat{f}(t_i, t_j)$  denotes the discretized forward rate for maturity  $t_j$  as of time  $t_i$ ,  $j \geq i$ , and  $\hat{B}(t_i, t_j)$  denotes the corresponding bond price,

$$\hat{B}(t_i, t_j) = \exp\left(-\sum_{\ell=i}^{j-1} \hat{f}(t_i, t_\ell)[t_{\ell+1} - t_\ell]\right). \tag{3.94}$$

To avoid introducing any more discretization error than necessary, we would like the initial values of the discretized bonds  $B(0, t_i)$  to coincide with the exact values  $B(0, t_j)$  for all maturities  $t_j$  on the discrete grid. Comparing  $(3.94)$  with the equation that precedes  $(3.87)$ , we see that this holds if

$$\sum_{\ell=0}^{j-1} \hat{f}(0, t_{\ell}) [t_{\ell+1} - t_{\ell}] = \int_0^{t_j} f(0, u) \, du;$$

i.e., if

$$\hat{f}(0, t_{\ell}) = \frac{1}{t_{\ell+1} - t_{\ell}} \int_{t_{\ell}}^{t_{\ell+1}} f(0, u) \, du,\tag{3.95}$$

for all  $\ell = 0, 1, \ldots, M-1$ . This indicates that we should initialize each  $\hat{f}(0, t_{\ell})$ to the *average* level of the forward curve  $f(0,T)$  over the interval  $[t_{\ell}, t_{\ell+1}]$ rather than, for example, initializing it to the value  $f(0, t_{\ell})$  at the left endpoint of this interval. The discretization  $(3.95)$  is illustrated in Figure 3.15.

![](_page_77_Figure_4.jpeg)

Fig. 3.15. Discretization of initial forward curve. Each discretized forward rate is the average of the underlying forward curve over the discretization interval.

Once the initial curve has been specified, a generic simulation of a singlefactor model evolves like this: for  $i = 1, \ldots, M$ ,

$$\hat{f}(t_i, t_j) = \hat{f}(t_{i-1}, t_j) + \n\hat{\mu}(t_{i-1}, t_j)[t_i - t_{i-1}] + \hat{\sigma}(t_{i-1}, t_j)\sqrt{t_i - t_{i-1}}Z_i, \ j = i, \dots, M, \quad (3.96)$$

where  $Z_1,\ldots,Z_M$  are independent  $N(0,1)$  random variables and  $\hat{\mu}$  and  $\hat{\sigma}$ denote discrete counterparts of the continuous-time coefficients in  $(3.91)$ . We allow  $\hat{\sigma}$  to depend on the current vector  $\hat{f}$  as well as on time and maturity, though to lighten notation we do not include  $\hat{f}$  as an explicit argument of  $\hat{\sigma}$ .

In practice,  $\hat{\sigma}$  would typically be specified through a calibration procedure designed to make the simulated model consistent with market prices of actively traded derivative securities. (We discuss calibration of a closely related class of models in Section 3.7.4.) In fact, the continuous-time limit  $\sigma(t,T)$  may never be specified explicitly because only the discrete version  $\hat{\sigma}$  is used in the simulation. But the situation for the drift is different. Recall that in deriving  $(3.91)$  we chose the drift to make the model arbitrage-free; more precisely, we chose it to make the discounted bond prices martingales. There are many

ways one might consider choosing the discrete drift  $\hat{\mu}$  in (3.96) to approximate the continuous-time limit  $(3.90)$ . From the many possible approximations, we choose the one that preserves the martingale property for the discounted bond prices.

Recalling that  $f(s,s)$  is the short rate at time s, we can express the continuous-time condition as the requirement that

$$B(t,T)\exp\left(-\int_0^t f(s,s)\,ds\right)$$

be a martingale in  $t$  for each  $T$ . Similarly, in the discretized model we would like

$$\hat{B}(t_i, t_j) \exp\left(-\sum_{k=0}^{i-1} \hat{f}(t_k, t_k)[t_{k+1} - t_k]\right)$$

to be a martingale in *i* for each *j*. Our objective is to find a  $\hat{\mu}$  for which this holds. For simplicity, we start by assuming a single-factor model.

The martingale condition can be expressed as

$$\mathsf{E}\left[\hat{B}(t_i, t_j)e^{-\sum_{k=0}^{i-1}\hat{f}(t_k, t_k)[t_{k+1}-t_k]}|Z_1, \dots, Z_{i-1}\right]$$
$$=\hat{B}(t_{i-1}, t_j)e^{-\sum_{k=0}^{i-2}\hat{f}(t_k, t_k)[t_{k+1}-t_k]}.$$

Using  $(3.94)$  and canceling terms that appear on both sides, this reduces to

$$\mathsf{E}\left[e^{-\sum_{\ell=i}^{j-1}\hat{f}(t_i,t_\ell)[t_{\ell+1}-t_\ell]}|Z_1,\ldots,Z_{i-1}\right] = e^{-\sum_{\ell=i}^{j-1}\hat{f}(t_{i-1},t_\ell)[t_{\ell+1}-t_\ell]}.$$

Now we introduce  $\hat{\mu}$ : on the left side of this equation we substitute for each  $\hat{f}(t_i, t_\ell)$  according to (3.96). This yields the condition

$$\mathsf{E}\left[e^{-\sum_{\ell=i}^{j-1} \left(\hat{f}(t_{i-1},t_{\ell}) + \hat{\mu}(t_{i-1},t_{\ell})[t_i - t_{i-1}] + \hat{\sigma}(t_{i-1},t_{\ell})\sqrt{t_i - t_{i-1}}Z_i\right)[t_{\ell+1} - t_{\ell}]} | Z_1,\ldots,Z_{i-1}\right]$$
$$= e^{-\sum_{\ell=i}^{j-1} \hat{f}(t_{i-1},t_{\ell})[t_{\ell+1} - t_{\ell}]}.$$

Canceling terms that appear on both sides and rearranging the remaining terms brings this into the form

$$\mathsf{E}\left[e^{-\sum_{\ell=i}^{j-1}\hat{\sigma}(t_{i-1},t_{\ell})\sqrt{t_{i}-t_{i-1}}[t_{\ell+1}-t_{\ell}]Z_{i}}|Z_{1},\ldots,Z_{i-1}\right]$$
$$=e^{\sum_{\ell=i}^{j-1}\hat{\mu}(t_{i-1},t_{\ell})[t_{i}-t_{i-1}][t_{\ell+1}-t_{\ell}]}.$$

The conditional expectation on the left evaluates to

$$e^{\frac{1}{2}\left(\sum_{\ell=i}^{j-1}\hat{\sigma}(t_{i-1},t_{\ell})[t_{\ell+1}-t_{\ell}]\right)^{2}[t_{i}-t_{i-1}]},$$

so equality holds if

 $\mathcal{L}_{\mathcal{L}}$ 

$$\frac{1}{2} \left( \sum_{\ell=i}^{j-1} \hat{\sigma}(t_{i-1}, t_{\ell}) [t_{\ell+1} - t_{\ell}] \right)^2 = \sum_{\ell=i}^{j-1} \hat{\mu}(t_{i-1}, t_{\ell}) [t_{\ell+1} - t_{\ell}];$$

i.e., if

$$\hat{\mu}(t_{i-1}, t_j)[t_{j+1} - t_j] = \frac{1}{2} \left( \sum_{\ell=i}^j \hat{\sigma}(t_{i-1}, t_\ell)[t_{\ell+1} - t_\ell] \right)^2 - \frac{1}{2} \left( \sum_{\ell=i}^{j-1} \hat{\sigma}(t_{i-1}, t_\ell)[t_{\ell+1} - t_\ell] \right)^2. (3.97)$$

This is the discrete version of the HJM drift; it ensures that the discretized discounted bond prices are martingales.

To see the connection between this expression and the continuous-time drift (3.90), consider the case of an equally spaced grid,  $t_i = ih$  for some increment  $h > 0$ . Fix a date t and maturity T and let  $i, j \to \infty$  and  $h \to 0$ in such a way that  $jh = T$  and  $ih = t$ ; each of the sums in (3.97) is then approximated by an integral. Dividing both sides of (3.97) by  $t_{j+1} - t_j = h$ , we find that for small  $h$  the discrete drift is approximately

$$\frac{1}{2h}\left[\left(\int_t^T \sigma(t,u)\,du\right)^2 - \left(\int_t^{T-h} \sigma(t,u)\,du\right)^2\right] \approx \frac{1}{2}\frac{\partial}{\partial T}\left(\int_t^T \sigma(t,u)\,du\right)^2,$$

 $\text{which is}$ 

$$\sigma(t,T)\int_t^T \sigma(t,u)\,du.$$

This suggests that the discrete drift in  $(3.97)$  is indeed consistent with the continuous-time limit in  $(3.90)$ .

In the derivation leading to  $(3.97)$  we assumed a single-factor model. A similar result holds with d factors. Let  $\hat{\sigma}_k$  denote the kth entry of the d-vector  $\hat{\sigma}$  and

$$\hat{\mu}_k(t_{i-1},t_j)[t_{j+1}-t_j] = \frac{1}{2} \left( \sum_{\ell=i}^j \hat{\sigma}_k(t_{i-1},t_\ell)[t_{\ell+1}-t_\ell] \right)^2 - \frac{1}{2} \left( \sum_{\ell=i}^{j-1} \hat{\sigma}_k(t_{i-1},t_\ell)[t_{\ell+1}-t_\ell] \right)^2,$$

for  $k = 1, \ldots, d$ . The combined drift is given by the sum

$$\hat{\mu}(t_{i-1}, t_j) = \sum_{k=1}^d \hat{\mu}_k(t_{i-1}, t_j).$$

A generic multifactor simulation takes the form

$$\hat{f}(t_i, t_j) = \hat{f}(t_{i-1}, t_j) + \hat{\mu}(t_{i-1}, t_j)[t_i - t_{i-1}] \\
+ \sum_{k=1}^{d} \hat{\sigma}_k(t_{i-1}, t_j) \sqrt{t_i - t_{i-1}} Z_{ik}, \quad j = i, \dots, M, \n$$
(3.98)

where the  $Z_i = (Z_{i1}, \ldots, Z_{id}), i = 1, \ldots, M$ , are independent  $N(0, I)$  random  $vectors.$ 

We derived  $(3.97)$  by starting from the principle that the discretized discounted bond prices should be martingales. But what are the practical implications of using some other approximation to the continuous drift instead of this one? To appreciate the consequences, consider the following experiment. Imagine simulating paths of  $\hat{f}$  as in (3.96) or (3.98). From a path of  $\hat{f}$  we may  $\text{extract a path}$ 

$$\hat{r}(t_0) = \hat{f}(t_0, t_0), \quad \hat{r}(t_1) = \hat{f}(t_1, t_1), \quad \dots \quad \hat{r}(t_M) = \hat{f}(t_M, t_M),$$

of the discretized short rate  $\hat{r}$ . From this we can calculate a discount factor

$$\hat{D}(t_j) = \exp\left(-\sum_{i=0}^{j-1} \hat{r}(t_i)[t_{i+1} - t_i]\right) \tag{3.99}$$

for each maturity  $t_j$ . Imagine repeating this over *n* independent paths and let  $\hat{D}^{(1)}(t_i), \ldots, \hat{D}^{(n)}(t_i)$  denote discount factors calculated over these n paths. A consequence of the strong law of large numbers, the martingale property, and the initialization in  $(3.95)$  is that, almost surely,

$$\frac{1}{n}\sum_{i=1}^{n}\hat{D}^{(i)}(t_{j}) \to \mathsf{E}[\hat{D}(t_{j})] = \hat{B}(0,t_{j}) = B(0,t_{j}).$$

This means that if we simulate using  $(3.97)$  and then use the simulation to price a bond, the simulation price converges to the value to which the model was ostensibly calibrated. With some other choice of discrete drift, the simulation price would in general converge to something that differs from  $B(0, t_i)$ , even if only slightly. Thus, the martingale condition is not simply a theoretical  $\text{feature}$  — it is a prerequisite for internal consistency of the simulated model. Indeed, failure of this condition can create the illusion of arbitrage opportunities. If  $E[D^{(1)}(t_j)] \neq B(0,t_j)$ , the simulation would be telling us that the market has mispriced the bond.

The errors (or apparent arbitrage opportunities) that may arise from using a different approximation to the continuous-time drift may admittedly be quite small. But given that we have a simple way of avoiding such errors and given that the form of the drift is the central feature of the HJM framework, we may as well restrict ourselves to  $(3.97)$ . This form of the discrete drift appears to be in widespread use in the industry; it is explicit in Andersen  $[11]$ .

### Forward Measure

 $\mathbb{K}$ 

Through an argument similar to the one leading to  $(3.97)$ , we can find the appropriate form of the discrete drift under the forward measure. In continuous

time, the forward measure for maturity  $T_F$  is characterized by the requirement that  $B(t,T)/B(t,T_F)$  be a martingale, because the bond maturing at  $T_F$  is the numeraire asset associated with this measure. In the discrete approximation, if we take  $t_M = T_F$ , then we require that  $\hat{B}(t_i, t_i)/\hat{B}(t_i, t_M)$  be a martingale in  $i$  for each  $j$ . This ratio is given by

$$\frac{\hat{B}(t_i, t_j)}{\hat{B}(t_i, t_M)} = \exp\left(\sum_{\ell=j}^{M-1} \hat{f}(t_i, t_\ell)[t_{\ell+1} - t_\ell]\right).$$

The martingale condition leads to a discrete drift  $\hat{\mu}$  with

$$\hat{\mu}(t_{i-1}, t_j)[t_{j+1} - t_j] = \frac{1}{2} \left( \sum_{\ell=j+1}^{M-1} \hat{\sigma}(t_{i-1}, t_\ell)[t_{\ell+1} - t_\ell] \right)^2 - \frac{1}{2} \left( \sum_{\ell=j}^{M-1} \hat{\sigma}(t_{i-1}, t_\ell)[t_{\ell+1} - t_\ell] \right)^2. \tag{3.100}$$

The relation between this and the risk-neutral discrete drift  $(3.97)$  is, not surprisingly, similar to the relation between their continuous-time counterparts in  $(3.91)$  and  $(3.93)$ .

### 3.6.3 Implementation

Once we have identified the discrete form of the drift, the main consideration in implementing an HJM simulation is keeping track of indices. The notation  $f(t_i, t_i)$  is convenient in describing the discretized model — the first argument shows the current time, the second argument shows the maturity to which this forward rate applies. But in implementing the simulation we are not interested in keeping track of an  $M \times M$  matrix of rates as the notation  $f(t_i, t_i)$  might suggest. At each time step, we need only the vector of current rates. To implement an HJM simulation we need to adopt some conventions regarding the indexing of this vector.

Recall that our time and maturity grid consists of a set of dates  $0 =$  $t_0 < t_1 < \cdots < t_M$ . If we identify  $t_M$  with the ultimate maturity  $T^*$  in the continuous-time model, then  $t_M$  is the maturity of the longest-maturity bond represented in the model. In light of  $(3.94)$ , this means that the last forward rate relevant to the model applies to the interval  $[t_{M-1}, t_M]$ ; this is the forward rate with maturity argument  $t_{M-1}$ . Thus, our initial vector of forward rates consists of the M components  $f(0,0), f(0,t_1), \ldots, f(0,t_{M-1}),$ which is consistent with the initialization  $(3.95)$ . At the start of the simulation we will represent this vector as  $(f_1,\ldots,f_M)$ . Thus, our first convention is to use  $1$  rather than  $0$  as the lowest index value.

As the simulation evolves, the number of relevant rates decreases. At time  $t_i$ , only the rates  $f(t_i, t_i), \ldots, f(t_i, t_{M-1})$  are meaningful. We need to specify how these  $M-i$  rates should be indexed, given that initially we had a vector

of M rates: we can either pad the initial portion of the vector with irrelevant data or we can shorten the length of the vector. We choose the latter and represent the  $M-i$  rates remaining at  $t_i$  as the vector  $(f_1,\ldots,f_{M-i})$ . Thus, our second convention is to index forward rates by relative maturity rather than absolute maturity. At time  $t_i$ ,  $f_i$  refers to the forward rate  $f(t_i, t_{i+j-1})$ . Under this convention  $f_1$  always refers to the current level of the short rate because  $\hat{r}(t_i) = \hat{f}(t_i, t_i)$ .

Similar considerations apply to  $\hat{\mu}(t_i, t_j)$  and  $\hat{\sigma}_k(t_i, t_j)$ ,  $k = 1, \ldots, d$ , and we adopt similar conventions for the variables representing these terms. For values of  $\hat{\mu}$  we use variables  $m_i$  and for values of  $\hat{\sigma}_k$  we use variables  $s_i(k)$ ; in both cases the subscript indicates a relative maturity and in the case of  $s_i(k)$  the argument  $k = 1, \ldots, d$  refers the factor index in a d-factor model. We design the indexing so that the simulation step from  $t_{i-1}$  to  $t_i$  indicated in  $(3.98)$  becomes

$$f_j \leftarrow f_{j+1} + m_j [t_i - t_{i-1}] + \sum_{k=1}^d s_j(k) \sqrt{t_i - t_{i-1}} Z_{ik}, \quad j = 1, \dots, M - i.$$

Thus, in advancing from  $t_{i-1}$  to  $t_i$  we want

Ť.

$$m_j = \hat{\mu}(t_{i-1}, t_{i+j-1}), \quad s_j(k) = \hat{\sigma}_k(t_{i-1}, t_{i+j-1}). \tag{3.101}$$

In particular, recall that  $\hat{\sigma}$  may depend on the current vector of forward rates; as implied by (3.101), the values of all  $s_i(k)$  should be determined before the forward rates are updated.

To avoid repeated calculation of the intervals between dates  $t_i$ , we introduce the notation

$$h_i = t_i - t_{i-1}, \quad , i = 1, \ldots, M.$$

These values do not change in the course of a simulation so we use the vector  $(h_1,\ldots,h_M)$  to represent these same values at all steps of the simulation.

We now proceed to detail the steps in an HJM simulation. We separate the algorithm into two parts, one calculating the discrete drift parameter at a fixed time step, the other looping over time steps and updating the forward  $\text{curve at each step. Figure 3.16 illustrates the calculation of}$ 

$$\hat{\mu}_k(t_{i-1}, t_j) = \frac{1}{2h_j} \left[ \sum_{\ell=i}^d \left( \sum_{\ell=i}^j \hat{\sigma}_k(t_{i-1}, t_\ell) h_{\ell+1} \right)^2 - \sum_{k=1}^d \left( \sum_{\ell=i}^{j-1} \hat{\sigma}_k(t_{i-1}, t_\ell) h_{\ell+1} \right)^2 \right]$$

in a way that avoids duplicate computation. In the notation of the algorithm, this drift parameter is evaluated as

$$\frac{1}{2(t_{j+1}-t_j)}[B_{\text{next}}-B_{\text{prev}}],$$

and each  $A_{\text{next}}(k)$  records a quantity of the form

$$\sum_{\ell=i}^j \hat{\sigma}_k(t_{i-1},t_\ell) h_{\ell+1}.$$

$$\begin{aligned} \text{Inputs: } s_j(k), \ j = 1, \dots, M - i, \ k = 1, \dots, d \text{ as in (3.101)} \\ \text{and } h_1, \dots, h_M \ (h_\ell = t_\ell - t_{\ell-1}) \end{aligned}$$
  
$$\begin{aligned} \text{Inputs: } s_j(k), \ j = 1, \dots, M - i, \ k = 1, \dots, d \text{ as in (3.101)} \\ \text{for } j = 1, \dots, M - i \end{aligned}$$
  
$$\begin{aligned} A_{\text{prev}}(k) &\leftarrow 0, \ k = 1, \dots, d \\ \text{for } k = 1, \dots, d \\ A_{\text{next}}(k) &\leftarrow A_{\text{prev}}(k) + s_j(k) * h_{i+j} \\ B_{\text{next}} &\leftarrow B_{\text{next}} + A_{\text{next}}(k) * A_{\text{next}}(k) \\ A_{\text{prev}}(k) &\leftarrow A_{\text{next}}(k) \end{aligned}$$
  
$$\begin{aligned} A_{\text{prev}}(k) &\leftarrow A_{\text{next}}(k) \\ \text{end} \\ \begin{aligned} m_j &\leftarrow (B_{\text{next}} - B_{\text{prev}})/(2h_{i+j}) \\ B_{\text{prev}} &\leftarrow B_{\text{next}} \end{aligned}$$
  
end  
$$\begin{aligned} \text{return } m_1, \dots, m_{M-i}. \end{aligned}$$

**Fig. 3.16.** Calculation of discrete drift parameters  $m_i = \hat{\mu}(t_{i-1}, t_{i+i-1})$  needed to simulate transition from  $t_{i-1}$  to  $t_i$ .

Figure  $3.17$  shows an algorithm for a single replication in an HJM simulation; the steps in the figure would naturally be repeated over many independent replications. This algorithm calls the one in Figure 3.16 to calculate the discrete drift for all remaining maturities at each time step. The two algorithms could obviously be combined, but keeping them separate should help clarify the various steps. In addition, it helps stress the point that in propagating the forward curve from  $t_{i-1}$  to  $t_i$ , we first evaluate the  $s_i(k)$  and  $m_i$ using the forward rates at step  $i-1$  and then update the rates to get their values at step  $i$ .

To make this point a bit more concrete, suppose we specified a single-factor model with  $\hat{\sigma}(t_i, t_j) = \tilde{\sigma}(i, j) \hat{f}(t_i, t_j)$  for some fixed values  $\tilde{\sigma}(i, j)$ . This makes each  $\hat{\sigma}(t_i, t_j)$  proportional to the corresponding forward rate. We noted in Ex- $\text{ample 3.6.3 that this type of diffusion term is inadmissible in the continuous-}$ time limit, but it can be (and often is) used in practice so long as the increments  $h_i$  are kept bounded away from zero. In this model it should be clear that in updating  $\hat{f}(t_{i-1}, t_j)$  to  $\hat{f}(t_i, t_j)$  we need to evaluate  $\tilde{\sigma}(i-1, j)\hat{f}(t_{i-1}, t_j)$ before we update the forward rate.

Since an HJM simulation is typically used to value interest rate derivatives, we have included in Figure  $3.17$  a few additional generic steps illustrating how

Inputs: initial curve  $(f_1, \ldots, f_M)$  and intervals  $(h_1, \ldots, h_M)$  $D \leftarrow 1, P \leftarrow 0, C \leftarrow 0.$ for  $i = 1, \ldots, M - 1$  $D \leftarrow D * \exp(-f_1 * h_i)$ evaluate  $s_j(k), j = 1, ..., M - i, k = 1, ..., d$ (recall that  $s_i(k) = \hat{\sigma}_k(t_{i-1}, t_{i+j-1})$ ) evaluate  $m_1, \ldots, m_{M-i}$  using Figure 3.16 generate  $Z_1, \ldots, Z_d \sim N(0, 1)$ for  $j = 1, \ldots, M - i$  $S \leftarrow 0$ for  $k = 1, \ldots, d$   $S \leftarrow S + s_j(k) \ast Z_k$  $f_j \leftarrow f_{j+1} + m_j * h_i + S * \sqrt{h_i}$ end  $P \leftarrow \text{cashflow at } t_i \text{ (depending on instrument)}$  $C \leftarrow C + D * P$  $\text{end}$ return  $C$ .

**Fig. 3.17.** Algorithm to simulate evolution of forward curve over  $t_0, t_1, \ldots, t_{M-1}$ and calculate cumulative discounted cashflows from an interest rate derivative.

a path of the forward curve is used both to compute and to discount the payoff of a derivative. The details of a particular instrument are subsumed in the placeholder "cashflow at  $t_i$ ." This cashflow is discounted through multiplication by  $D$ , which is easily seen to contain the simulated value of the discount factor  $D(t_i)$  as defined in (3.99). (When D is updated in Figure 3.17, before the forward rates are updated,  $f_1$  records the short rate for the interval  $[t_{i-1}, t_i]$ .) To make the pricing application more explicit, we consider a few  $\text{examples.}$ 

**Example 3.6.4** Bonds. There is no reason to use an HJM simulation to price bonds — if properly implemented, the simulation will simply return prices that could have been computed from the initial forward curve. Nevertheless, we consider this example to help fix ideas. We discussed the pricing of a zerocoupon bond following (3.99); in Figure 3.17 this corresponds to setting  $P \leftarrow 1$ at the maturity of the bond and  $P \leftarrow 0$  at all other dates. For a coupon paying bond with a face value of 100 and a coupon of c, we would set  $P \leftarrow c$  at the coupon dates and  $P \leftarrow 100 + c$  at maturity. This assumes, of course, that the coupon dates are among the  $t_1, \ldots, t_M$ .  $\Box$ 

**Example 3.6.5** Caps. A caplet is an interest rate derivative providing protection against an increase in an interest rate for a single period; a  $cap$  is a portfolio of caplets covering multiple periods. A caplet functions almost like a call option on the short rate, which would have a payoff of the form

 $(r(T)-K)^{+}$  for some strike K and maturity T. In practice, a caplet differs from this in some small but important ways. (For further background, see Appendix  $C.$ )

In contrast to the instantaneous short rate  $r(t)$ , the underlying rate in a caplet typically applies over an interval and is based on discrete compounding. For simplicity, suppose the interval is of the form  $[t_i, t_{i+1}]$ . At  $t_i$ , the continuously compounded rate for this interval is  $\hat{f}(t_i, t_i)$ ; the corresponding discretely compounded rate  $\hat{F}$  satisfies

$$\frac{1}{1+\hat{F}(t_i)[t_{i+1}-t_i]} = e^{-\hat{f}(t_i,t_i)[t_{i+1}-t_i]};$$

i.e.,

$$\hat{F}(t_i) = \frac{1}{t_{i+1} - t_i} \left( e^{\hat{f}(t_i, t_i)[t_{i+1} - t_i]} - 1 \right).$$

The payoff of the caplet would then be  $(\hat{F}(t_i) - K)^+$  (or a constant multiple of this). Moreover, this payment is ordinarily made at the end of the interval,  $t_{i+1}$ . To discount it properly we should therefore simulate to  $t_i$  and set

$$P \leftarrow \frac{1}{1 + \hat{F}(t_i)[t_{i+1} - t_i]} (\hat{F}(t_i) - K)^+; \tag{3.102}$$

in the notation of Figure  $3.17$ , this is

$$P \leftarrow e^{-f_1 h_{i+1}} \left(\frac{1}{h_{i+1}} \left(e^{f_1 h_{i+1}} - 1\right) - K\right)^+.$$

Similar ideas apply if the caplet covers an interval longer than a single simulation interval. Suppose the caplet applies to an interval  $[t_i, t_{i+n}]$ . Then  $(3.102)$  still applies at  $t_i$ , but with  $t_{i+1}$  replaced by  $t_{i+n}$  and  $F(t_i)$  redefined to be

$$\hat{F}(t_i) = \frac{1}{t_{n+i} - t_i} \left( \exp\left( \sum_{\ell=0}^{n-1} \hat{f}(t_i, t_{i+\ell}) [t_{i+\ell+1} - t_{i+\ell}] \right) - 1 \right).$$

In the case of a cap consisting of caplets for, say, the periods  $[t_{i_1}, t_{i_2}], [t_{i_2}, t_{i_3}],$  $\ldots$ ,  $[t_{i_k}, t_{i_{k+1}}]$ , for some  $i_1 < i_2 < \cdots < i_{k+1}$ , this calculation would be repeated and a cashflow recorded at each  $t_{i_j}, j = 1, \ldots, k$ .  $\Box$ 

**Example 3.6.6** Swaptions. Consider, next, an option to swap fixed-rate payments for floating-rate payments. (See Appendix  $C$  for background on swaps and swaptions.) Suppose the underlying swap begins at  $t_{j_0}$  with payments to be exchanged at dates  $t_{j_1}, \ldots, t_{j_n}$ . If we denote the fixed rate in the swap by R, then the fixed-rate payment at  $t_{j_k}$  is  $100R[t_{j_k}-t_{j_{k-1}}]$ , assuming a principal or *notional* amount of 100. As explained in Section C.2 of Appendix C, the value of the swap at  $t_{j_0}$  is

3.7 Forward Rate Models: Simple Rates 165

$$\hat{V}(t_{j_0}) = 100 \left( R \sum_{\ell=1}^n \hat{B}(t_{j_0}, t_{j_\ell}) [t_{j_\ell} - t_{j_{\ell-1}}] + \hat{B}(t_{j_0}, t_{j_n}) - 1 \right).$$

The bond prices  $\hat{B}(t_{j_0},t_{j_\ell})$  can be computed from the forward rates at  $t_{j_0}$ using  $(3.94)$ .

The holder of an option to enter this swap will exercise the option if  $\hat{V}(t_{j_0}) > 0$  and let it expire otherwise. (For simplicity, we are assuming that the option expires at  $t_{j_0}$  though similar calculations apply for an option to enter into a *forward* swap, in which case the option expiration date would be prior to  $t_{j_0}$ .) Thus, we may view the swaption as having a payoff of  $\max\{0,\hat{V}(t_{j_0})\}$  at  $t_{j_0}$ . In a simulation, we would therefore simulate the forward curve to the option expiration date  $t_{j_0}$ ; at that date, calculate the prices of the bonds  $\hat{B}(t_{i_0}, t_{i_\ell})$  maturing at the payment dates of the swaps; from the bond prices calculate the value of the swap  $\hat{V}(t_{j_0})$  and thus the swaption payoff max $\{0, \hat{V}(t_{j_0})\}$ ; record this as the cashflow P in the algorithm of Figure 3.17 and discount it as in the algorithm.

This example illustrates a general feature of the HJM framework that contrasts with models based on the short rate as in Sections 3.3 and 3.4. Consider valuing a 5-year option on a 20-year swap. This instrument involves maturities as long as 25 years, so valuing it in a model of the short rate could involve simulating paths over a 25-year horizon. In the HJM framework, if the initial forward curve extends for 25 years, then we need to simulate only for 5 years; at the expiration of the option, the remaining forward rates contain all the information necessary to value the underlying swap. Thus, although the HJM setting involves updating many more variables at each time step, it may also require far fewer time steps.  $\Box$ 

# 3.7 Forward Rate Models: Simple Rates

The models considered in this section are closely related to the HJM framework of the previous section in that they describe the arbitrage-free dynamics of the term structure of interest rates through the evolution of forward rates. But the models we turn to now are based on *simple* rather than continuously compounded forward rates. This seemingly minor shift in focus has surprisingly far-reaching practical and theoretical implications. This modeling approach has developed primarily through the work of Miltersen, Sandmann, and Sondermann [268], Brace, Gatarek, and Musiela [56], Musiela and Rutkowski  $|274|$ , and Jamshidian  $|197|$ ; it has gained rapid acceptance in the financial industry and stimulated a growing stream of research into what are often called LIBOR market models.

# 3.7.1 LIBOR Market Model Dynamics

The basic object of study in the HJM framework is the forward rate curve  $\{f(t,T), t \leq T \leq T^*\}$ . But the instantaneous, continuously compounded forward rates  $f(t,T)$  might well be considered mathematical idealizations they are not directly observable in the marketplace. Most market interest rates are based on simple compounding over intervals of, e.g., three months or six months. Even the instantaneous short rate  $r(t)$  treated in the models of Sections 3.3 and 3.4 is a bit of a mathematical fiction because short-term rates used for pricing are typically based on periods of one to three months. The term "market model" is often used to describe an approach to interest rate modeling based on observable market rates, and this entails a departure from instantaneous rates.

Among the most important benchmark interest rates are the London Inter-Bank Offered Rates or LIBOR. LIBOR is calculated daily through an average of rates offered by banks in London. Separate rates are quoted for different maturities (e.g., three months and six months) and different currencies. Thus, each day new values are calculated for three-month Yen LIBOR, six-month US dollar LIBOR, and so on.

LIBOR rates are based on *simple* interest. If  $L$  denotes the rate for an accrual period of length  $\delta$  (think of  $\delta$  as 1/4 or 1/2 for three months and six months respectively, with time measured in years), then the interest earned on one unit of currency over the accrual period is  $\delta L$ . For example, if threemonth LIBOR is  $6\%$ , the interest earned at the end of three months on a principal of 100 is  $0.25 \cdot 0.06 \cdot 100 = 1.50$ .

A forward LIBOR rate works similarly. Fix  $\delta$  and consider a maturity T. The forward rate  $L(0,T)$  is the rate set at time 0 for the interval  $[T, T + \delta]$ . If we enter into a contract at time 0 to borrow 1 at time  $T$  and repay it with interest at time  $T + \delta$ , the interest due will be  $\delta L(0,T)$ . As shown in Appendix C (specifically equation  $(C.5)$ ), a simple replication argument leads to the following identity between forward LIBOR rates and bond prices:

$$L(0,T) = \frac{B(0,T) - B(0,T+\delta)}{\delta B(0,T+\delta)}.$$
(3.103)

This further implies the relation

$$L(0,T) = \frac{1}{\delta} \left( \exp\left(\int_T^{T+\delta} f(0,u) \, du\right) - 1\right) \tag{3.104}$$

between continuous and simple forwards, though it is not necessary to introduce the continuous rates to build a model based on simple rates.

It should be noted that, as is customary in this literature, we treat the forward LIBOR rates as though they were risk-free rates. LIBOR rates are based on quotes by banks which could potentially default and this risk is presumably reflected in the rates. US Treasury bonds, in contrast, are generally considered to have a negligible chance of default. The argument leading to  $(3.103)$  may not hold exactly if the bonds on one side and the forward rate on the other reflect different levels of creditworthiness. We will not, however, attempt to take account of these considerations.

Although  $(3.103)$  and  $(3.104)$  apply in principle to a continuum of maturities  $T$ , we consider a class of models in which a finite set of maturities or  $tenor$  dates

$$0 = T_0 < T_1 < \cdots < T_M < T_{M+1}$$

are fixed in advance. As argued in Jamshidian [197], many derivative securities tied to LIBOR and swap rates are sensitive only to a finite set of maturities and it should not be necessary to introduce a continuum to price and hedge these securities. Let

$$\delta_i = T_{i+1} - T_i, \quad i = 0, \dots, M,$$

denote the lengths of the intervals between tenor dates. Often, these would all be equal to a nominally fixed interval of a quarter or half year; but even in this case, day-count conventions would produce slightly different values for the fractions  $\delta_i$ .

For each date  $T_n$  we let  $B_n(t)$  denote the time-t price of a bond maturing at  $T_n$ ,  $0 \le t \le T_n$ . In our usual notation this would be  $B(t,T_n)$ , but writing  $B_n(t)$  and restricting n to  $\{1, 2, \ldots, M+1\}$  emphasizes that we are working with a finite set of bonds. Similarly, we write  $L_n(t)$  for the forward rate as of time t for the accrual period  $[T_n, T_{n+1}]$ ; see Figure 3.18. This is given in terms of the bond prices by

$$L_n(t) = \frac{B_n(t) - B_{n+1}(t)}{\delta_n B_{n+1}(t)}, \quad 0 \le t \le T_n, \quad n = 0, 1, \dots, M. \tag{3.105}$$

After  $T_n$ , the forward rate  $L_n$  becomes meaningless; it sometimes simplifies notation to extend the definition of  $L_n(t)$  beyond  $T_n$  by setting  $L_n(t)$  =  $L_n(T_n)$  for all  $t \geq T_n$ .

From  $(3.105)$  we know that bond prices determine the forward rates. At a tenor date  $T_i$ , the relation can be inverted to produce

$$B_n(T_i) = \prod_{j=i}^{n-1} \frac{1}{1 + \delta_j L_j(T_i)}, \quad n = i+1, \dots, M+1.$$
 (3.106)

However, at an arbitrary date  $t$ , the forward LIBOR rates do not determine the bond prices because they do not determine the discount factor for intervals shorter than the accrual periods. Suppose for example that  $T_i < t < T_{i+1}$  and we want to find the price  $B_n(t)$  for some  $n > i + 1$ . The factor

$$\prod_{j=i+1}^{n-1} \frac{1}{1+\delta_j L_j(t)}$$

![](_page_89_Figure_0.jpeg)

![](_page_89_Figure_1.jpeg)

**Fig. 3.18.** Evolution of vector of forward rates. Each  $L_n(t)$  is the forward rate for the interval  $[T_n, T_{n+1}]$  as of time  $t \leq T_n$ .

discounts the bond's payment at  $T_n$  back to time  $T_{i+1}$ , but the LIBOR rates do not specify the discount factor from  $T_{i+1}$  to t.

Define a function  $\eta: [0, T_{M+1}) \to \{1, \ldots, M+1\}$  by taking  $\eta(t)$  to be the unique integer satisfying

$$T_{\eta(t)-1} \le t < T_{\eta(t)};$$

thus,  $\eta(t)$  gives the index of the next tenor date at time t. With this notation, we have

$$B_n(t) = B_{\eta(t)}(t) \prod_{j=\eta(t)}^{n-1} \frac{1}{1 + \delta_j L_j(t)}, \quad 0 \le t < T_n; \tag{3.107}$$

the factor  $B_{\eta(t)}(t)$  (the current price of the shortest maturity bond) is the missing piece required to express the bond prices in terms of the forward  $LIBOR$  rates.

# Spot Measure

We seek a model in which the evolution of the forward LIBOR rates is described by a system of SDEs of the form

$$\frac{dL_n(t)}{L_n(t)} = \mu_n(t) \, dt + \sigma_n(t)^\top \, dW(t), \quad 0 \le t \le T_n, \quad n = 1, \dots, M, \quad (3.108)$$

with W a d-dimensional standard Brownian motion. The coefficients  $\mu_n$  and  $\sigma_n$  may depend on the current vector of rates  $(L_1(t),\ldots,L_M(t))$  as well as the

current time t. Notice that in (3.108)  $\sigma_n$  is the (proportional) volatility because we have divided by  $L_n$  on the left, whereas in the HJM setting (3.91) we took  $\sigma(t,T)$  to be the absolute level of volatility. At this point, the distinction is purely one of notation rather than scope because we allow  $\sigma_n(t)$  to depend on the current level of rates.

9

Recall that in the HJM setting we derived the form of the drift of the forward rates from the absence of arbitrage. More specifically, we derived the drift from the condition that bond prices be martingales when divided by the numeraire asset. The numeraire we used is the usual one associated with the risk-neutral measure,  $\beta(t) = \exp(\int_0^t r(u) \, du)$ . But introducing a short-rate process  $r(t)$  would undermine our objective of developing a model based on the simple (and thus more realistic) rates  $L_n(t)$ . We therefore avoid the usual risk-neutral measure and instead use a numeraire asset better suited to the tenor dates  $T_i$ .

A simply compounded counterpart of  $\beta(t)$  works as follows. Start with 1 unit of account at time 0 and buy  $1/B_1(0)$  bonds maturing at  $T_1$ . At time  $T_1$ , reinvest the funds in bonds maturing at time  $T_2$  and proceed this way, at each  $T_i$  putting all funds in bonds maturing at time  $T_{i+1}$ . This trading strategy earns (simple) interest at rate  $L_i(T_i)$  over each interval  $[T_i, T_{i+1}]$ , just as in the continuously compounded case a savings account earns interest at rate  $r(t)$  at time t. The initial investment of 1 at time 0 grows to a value of

$$B^*(t) = B_{\eta(t)}(t) \prod_{j=0}^{\eta(t)-1} [1 + \delta_j L_j(T_j)]$$

at time t. Following Jamshidian [197], we take this as numeraire asset and call the associated measure the *spot measure*.

Suppose, then, that  $(3.108)$  holds under the spot measure, meaning that W is a standard Brownian motion under that measure. The absence of arbitrage restricts the dynamics of the forward LIBOR rates through the condition that bond prices be martingales when *deflated* by the numeraire asset. (We use the term "deflated" rather than "discounted" to emphasize that we are dividing by the numeraire asset and not discounting at a continuously compounded rate.) From (3.107) and the expression for  $B^*$ , we find that the deflated bond price  $D_n(t) = B_n(t)/B^*(t)$  is given by

$$D_n(t) = \left(\prod_{j=0}^{\eta(t)-1} \frac{1}{1+\delta_j L_j(T_j)}\right) \prod_{j=\eta(t)}^{n-1} \frac{1}{1+\delta_j L_j(t)}, \quad 0 \le t \le T_n. \tag{3.109}$$

Notice that the spot measure numeraire  $B^*$  cancels the factor  $B_{\eta(t)}(t)$  used in  $(3.107)$  to discount between tenor dates. We are thus left in  $(3.109)$  with an expression defined purely in terms of the LIBOR rates. This would not have been the case had we divided by the risk-neutral numeraire asset  $\beta(t)$ .

We require that the deflated bond prices  $D_n$  be positive martingales and proceed to derive the restrictions this imposes on the LIBOR dynam-

ics  $(3.108)$ . If the deflated bonds are indeed positive martingales, we may write

$$\frac{dD_{n+1}(t)}{D_{n+1}(t)} = \nu_{n+1}(t)^{\top} dW(t), \quad n = 1, \dots, M,$$

for some  $\Re^d$ -valued processes  $\nu_{n+1}$  which may depend on the current level of  $(D_2, \ldots, D_{M+1})$  (equivalently, of  $(L_1, \ldots, L_M)$ ). By Itô's formula,

$$d\log D_{n+1}(t) = -\frac{1}{2} \|\nu_{n+1}(t)\| \, dt + \nu_{n+1}^\top(t) \, dW(t).$$

We may therefore express  $\nu_{n+1}$  by finding the coefficient of  $dW$  in

$$d \log D_{n+1}(t) = -\sum_{j=\eta(t)}^{n} d \log(1 + \delta_j L_j(t));$$

notice that the first factor in (3.109) is constant between maturities  $T_i$ . Applying Itô's formula and  $(3.108)$ , we find that

$$\nu_{n+1}(t) = -\sum_{j=\eta(t)}^{n} \frac{\delta_j L_j(t)}{1 + \delta_j L_j(t)} \sigma_j(t). \tag{3.110}$$

We now proceed by induction to find the  $\mu_n$  in (3.108). Setting  $D_1(t) \equiv$  $B_1(0)$ , we make  $D_1$  constant and hence a martingale without restrictions on any of the LIBOR rates. Suppose now that  $\mu_1, \ldots, \mu_{n-1}$  have been chosen consistent with the martingale condition on  $D_n$ . From the identity  $D_n(t)$  =  $D_{n+1}(1+\delta_n L_n(t)),$  we find that  $\delta_n L_n(t)D_{n+1}(t) = D_n(t) - D_{n+1}(t),$  so  $D_{n+1}(t)$ is a martingale if and only if  $L_n D_{n+1}$  is a martingale. Applying Itô's formula,  $we get$ 

$$\begin{split} d(L_n D_{n+1}) \\ &= D_{n+1} \, dL_n + L_n \, dD_{n+1} + L_n D_{n+1} \nu_{n+1}^\top \sigma_n \, dt \\ &= \left( D_{n+1} \mu_n L_n + L_n D_{n+1} \nu_{n+1}^\top \sigma_n \right) \, dt + L_n D_{n+1} \sigma_n^\top \, dW + L_n \, dD_{n+1}. \end{split}$$

(We have suppressed the time argument to lighten the notation.) To be consistent with the martingale restriction on  $D_{n+1}$  and  $L_n D_{n+1}$ , the dt coefficient must be zero, and thus

$$\mu_n = -\sigma_n^\top \nu_{n+1};$$

notice the similarity to the HJM drift  $(3.90)$ . Combining this with  $(3.110)$ , we arrive at

$$\mu_n(t) = \sum_{j=\eta(t)}^n \frac{\delta_j L_j(t)\sigma_n(t)^\top \sigma_j(t)}{1 + \delta_j L_j(t)} \tag{3.111}$$

as the required drift parameter in  $(3.108)$ , so

$$\frac{dL_n(t)}{L_n(t)} = \sum_{j=\eta(t)}^n \frac{\delta_j L_j(t)\sigma_n(t)^\top \sigma_j(t)}{1+\delta_j L_j(t)} dt + \sigma_n(t)^\top dW(t), \quad 0 \le t \le T_n, \tag{3.112}$$

 $n = 1, \ldots, M$ , describes the arbitrage-free dynamics of forward LIBOR rates under the spot measure. This formulation is from Jamshidian [197], which should be consulted for a rigorous and more general development.

### Forward Measure

As in Musiela and Rutkowski [274], we may alternatively formulate a LIBOR market model under the forward measure  $P_{M+1}$  for maturity  $T_{M+1}$  and take the bond  $B_{M+1}$  as numeraire asset. In this case, we redefine the deflated bond prices to be the ratios  $D_n(t) = B_n(t)/B_{M+1}(t)$ , which simplify to

$$D_n(t) = \prod_{j=n+1}^{M} (1 + \delta_j L_j(t)). \tag{3.113}$$

Notice that the numeraire asset has once again canceled the factor  $B_{n(t)}(t)$ , leaving an expression that depends solely on the forward LIBOR rates.

We could derive the dynamics of the forward LIBOR rates under the forward measure through the Girsanov Theorem and  $(3.112)$ , much as we did in the HJM setting to arrive at  $(3.93)$ . Alternatively, we could start from the requirement that the  $D_n$  in (3.113) be martingales and proceed by induction (backwards from  $n = M$ ) to derive restrictions on the evolution of the  $L_n$ . Either way, we find that the arbitrage-free dynamics of the  $L_n$ ,  $n = 1, \ldots, M$ , under the forward measure  $P_{M+1}$  are given by

$$\frac{dL_n(t)}{L_n(t)} = -\sum_{j=n+1}^{M} \frac{\delta_j L_j(t)\sigma_n(t)^{\top} \sigma_j(t)}{1 + \delta_j L_j(t)} dt + \sigma_n(t)^{\top} dW^{M+1}(t), \quad 0 \le t \le T_n,$$
(3.114)

with  $W^{M+1}$  a standard d-dimensional Brownian motion under  $P_{M+1}$ . The relation between the drift in  $(3.114)$  and the drift in  $(3.112)$  is analogous to the relation between the risk-neutral and forward-measure drifts in the HJM setting; compare  $(3.90)$  and  $(3.93)$ .

If we take  $n = M$  in (3.114), we find that

$$\frac{dL_M(t)}{L_M(t)} = \sigma_M(t)^\top dW^{M+1}(t),$$

so that, subject only to regularity conditions on its volatility,  $L_M$  is a martingale under the forward measure for maturity  $T_{M+1}$ . Moreover, if  $\sigma_M$  is deterministic then  $L_M(t)$  has lognormal distribution  $LN(-\bar{\sigma}_M^2(t)/2, \bar{\sigma}_M^2(t))$ with

$$\bar{\sigma}_M(t) = \sqrt{\frac{1}{t} \int_0^t \|\sigma_M(u)\|^2 \, du}.$$
 (3.115)

In fact, the choice of M is arbitrary: each  $L_n$  is a martingale (lognormal if  $\sigma_n$ is deterministic) under the forward measure  $P_{n+1}$  associated with  $T_{n+1}$ .

These observations raise the question of whether we may in fact take the coefficients  $\sigma_n$  to be deterministic in (3.112) and (3.114). Recall from Exam- $\text{ple } 3.6.3 \text{ that this choice (deterministic proportional volatility)} \text{ is inadmissible}$ in the HJM setting, essentially because it makes the HJM drift quadratic in the current level of rates. To see what happens with simple compounding, rewrite  $(3.112)$  as

$$dL_n(t) = \sum_{j=\eta(t)}^n \frac{\delta_j L_j(t) L_n(t) \sigma_n(t)^\top \sigma_j(t)}{1 + \delta_j L_j(t)} dt + L_n(t) \sigma_n(t)^\top dW(t) \quad (3.116)$$

and consider the case of deterministic  $\sigma_i$ . The numerators in the drift are quadratic in the forward LIBOR rates, but they are stabilized by the terms  $1 + \delta_i L_i(t)$  in the denominators; indeed, because  $L_i(t) \geq 0$  implies

$$\left| \frac{\delta_j L_j(t)}{1 + \delta_j L_j(t)} \right| \le 1,$$

the drift is linearly bounded in  $L_n(t)$ , making deterministic  $\sigma_i$  admissible. This feature is lost in the limit as the compounding period  $\delta_i$  decreases to zero. Thus, the distinction between continuous and simple forward rates turns out to have important mathematical as well as practical implications.

# 3.7.2 Pricing Derivatives

We have noted two important features of LIBOR market models: they are based on observable market rates, and (in contrast to the HJM framework) they admit deterministic volatilities  $\sigma_i$ . A third important and closely related feature arises in the pricing of interest rate caps.

Recall from Example  $3.6.5$  (or Appendix C.2) that a cap is a collection of caplets and that each caplet may be viewed as a call option on a simple forward rate. Consider, then, a caplet for the accrual period  $[T_n, T_{n+1}]$ . The underlying rate is  $L_n$  and the value  $L_n(T_n)$  is fixed at  $T_n$ . With a strike of K, the caplet's payoff is  $\delta_n(L_n(T_n)-K)^+$ ; think of the caplet as refunding the amount by which interest paid at rate  $L_n(T_n)$  exceeds interest paid at rate K. This payoff is made at  $T_{n+1}$ .

Let  $C_n(t)$  denote the price of this caplet at time t; we know the terminal value  $C_n(T_{n+1}) = \delta_n(L_n(T_n) - K)^+$  and we want to find the initial value  $C_n(0)$ . Under the spot measure, the deflated price  $C_n(t)/B^*(t)$  must be a martingale, so

$$C_n(0) = B^*(0) \mathsf{E}^* \left[ \frac{\delta_n (L_n(T_n) - K)^+}{B^*(T_{n+1})} \right],$$

where we have written  $E^*$  for expectation under the spot measure. Through  $B^*(T_{n+1}),$  this expectation involves the joint distribution of  $L_1(T_1), \ldots,$  $L_n(T_n)$ , making its value difficult to discern. In contrast, under the forward

measure  $P_{n+1}$  associated with maturity  $T_{n+1}$ , the martingale property applies to  $C_n(t)/B_{n+1}(t)$ . We may therefore also write

$$C_n(0) = B_{n+1}(0) \mathsf{E}_{n+1} \left[ \frac{\delta_n (L_n(T_n) - K)^+}{B_{n+1}(T_{n+1})} \right],$$

with  $\mathsf{E}_{n+1}$  denoting expectation under  $P_{n+1}$ . Conveniently,  $B_{n+1}(T_{n+1}) \equiv 1$ , so this expectation depends only on the marginal distribution of  $L_n(T_n)$ . If we take  $\sigma_n$  to be deterministic, then  $L_n(T_n)$  has the lognormal distribution  $LN(-\bar{\sigma}_n^2(T_n)/2, \bar{\sigma}_n^2(T_n))$ , using the notation in (3.115). In this case, the caplet price is given by the *Black formula* (after Black  $[49]$ ),

$$C_n(0) = \mathrm{BC}(L_n(0), \bar{\sigma}_n(T_n), T_n, K, \delta_n B_{n+1}(0)),$$

with

$$\begin{aligned} &\text{BC}(F,\sigma,T,K,b) = \\ &b\left(F\Phi\left(\frac{\log(F/K) + \sigma^2 T/2}{\sigma\sqrt{T}}\right) - K\Phi\left(\frac{\log(F/K) - \sigma^2 T/2}{\sigma\sqrt{T}}\right)\right) \end{aligned} \tag{3.117}$$

and  $\Phi$  the cumulative normal distribution. Thus, under the assumption of deterministic volatilities, caplets are priced in closed form by the Black formula.

This formula is frequently used in the reverse direction. Given the market price of a caplet, one can solve for the "implied volatility" that makes the formula match the market price. This is useful in calibrating a model to market data, a point we return to in Section  $3.7.4$ .

Consider, more generally, a derivative security making a payoff of  $g(L(T_n))$ at  $T_k$ , with  $L(T_n) = (L_1(T_1), \ldots, L_{n-1}(T_{n-1}), L_n(T_n), \ldots, L_M(T_n))$  and  $k \geq$  $n$ . The price of the derivative at time 0 is given by

$$\mathsf{E}^* \left[ \frac{g(L(T_n))}{B^*(T_k)} \right]$$

(using the fact that  $B^*(0) = 1$ ), and also by

$$B_m(0)\mathsf{E}_m\left[\frac{g(L(T_n))}{B_m(T_k)}\right]$$

for every  $m \geq k$ . Which measure and numeraire are most convenient depends on the payoff function  $q$ . However, in most cases, the expectation cannot be evaluated explicitly and simulation is required.

As a further illustration, we consider the pricing of a swaption as described in Example  $3.6.6$  and Appendix C.2. Suppose the underlying swap begins at  $T_n$  with fixed- and floating-rate payments exchanged at  $T_{n+1}, \ldots, T_{M+1}$ . From equation (C.7) in Appendix C, we find that the forward swap rate at time  $t$ is given by

$$S_n(t) = \frac{B_n(t) - B_{M+1}(t)}{\sum_{j=n+1}^{M+1} \delta_j B_j(t)}.$$
(3.118)

Using (3.107) and noting that  $B_{\eta(t)}(t)$  cancels from the numerator and denominator, this swap rate can be expressed purely in terms of forward LIBOR rates.

Consider, now, an option expiring at time  $T_k \leq T_n$  to enter into the swap over  $[T_n, T_{M+1}]$  with fixed rate T. The value of the option at expiration can be expressed as (cf. equation  $(C.11)$ )

$$\sum_{j=n+1}^{M+1} \delta_j B_j(T_k) (R - S_n(T_k))^+.$$

This can be written as a function  $g(L(T_k))$  of the LIBOR rates. The price at time zero can therefore be expressed as an expectation using the general  $\text{expressions above.}$ 

By applying Itô's formula to the swap rate  $(3.118)$ , it is not difficult to conclude that if the forward LIBOR rates have deterministic volatilities, then the forward swap rate cannot also have a deterministic volatility. In particular, then, the forward swap rate cannot be geometric Brownian motion under any equivalent measure. Brace et al. [56] nevertheless use a lognormal approximation to the swap rate to develop a method for pricing swaptions; their approximation appears to give excellent results. An alternative approach has been developed by Jamshidian [197]. He develops a model in which the term structure is described through a vector  $(S_0(t),\ldots,S_M(t))$  of forward swap rates. He shows that one may choose the volatilities of the forward swap rates to be deterministic, and that in this case swaption prices are given by a variant of the Black formula. However, in this model, the LIBOR rates cannot also have deterministic volatilities, so caplets are no longer priced by the Black formula. One must therefore choose between the two pricing formulas.

### 3.7.3 Simulation

Pricing derivative securities in LIBOR market models typically requires simulation. As in the HJM setting, exact simulation is generally infeasible and some discretization error is inevitable. Because the models of this section deal with a finite set of maturities from the outset, we need only discretize the time argument, whereas in the HJM setting both time and maturity required discretization.

We fix a time grid  $0 = t_0 < t_1 < \cdots < t_m < t_{m+1}$  over which to simulate. It is sensible to include the tenor dates  $T_1, \ldots, T_{M+1}$  among the simulation dates. In practice, one would often even take  $t_i = T_i$  so that the simulation evolves directly from one tenor date to the next. We do not impose any restrictions on the volatilities  $\sigma_n$ , though the deterministic case is the most widely used. The only other specific case that has received much attention takes  $\sigma_n(t)$  to be the product of a deterministic function of time and a function of  $L_n(t)$  as proposed in Andersen and Andreasen [13]. For example, one may take  $\sigma_n(t)$ proportional to a power of  $L_n(t)$ , resulting in a CEV-type of volatility. In either

this extension or in the case of deterministic volatilities, it often suffices to restrict the dependence on time to piecewise constant functions that change values only at the  $T_i$ . We return to this point in Section 3.7.4.

Simulation of forward LIBOR rates is a special case of the general problem of simulating a system of SDEs. One could apply an Euler scheme or a higher-order method of the type discussed in Chapter 6. However, even if we restrict ourselves to Euler schemes (as we do here), there are countless alternatives. We have many choices of variables to discretize and many choices of probability measure under which to simulate. Several strategies are compared both theoretically and numerically in Glasserman and Zhao [151], and the discussion here draws on that investigation.

The most immediate application of the Euler scheme under the spot measure discretizes the SDE  $(3.116)$ , producing

$$\hat{L}_n(t_{i+1}) = \hat{L}_n(t_i) + \mu_n(\hat{L}(t_i), t_i)\hat{L}_n(t_i)[t_{i+1} - t_i] \n+ \hat{L}_n(t_i)\sqrt{t_{i+1} - t_i}\sigma_n(t_i)^\top Z_{i+1} \n$$
(3.119)

with

$$\mu_n(\hat{L}(t_i), t_i) = \sum_{j=\eta(t_i)}^n \frac{\delta_j \hat{L}_j(t_i) \sigma_n(t_i)^\top \sigma_j(t_i)}{1 + \delta_j \hat{L}_j(t_i)}$$

and  $Z_1, Z_2, \ldots$  independent  $N(0, I)$  random vectors in  $\mathbb{R}^d$ . Here, as in Section 3.6.2, we use hats to identify discretized variables. We assume that we are given an initial set of bond prices  $B_1(0), \ldots, B_{M+1}(0)$  and initialize the simulation by setting

$$\hat{L}_n(0) = \frac{B_n(0) - B_{n+1}(0)}{\delta_n B_{n+1}(0)}, \quad n = 1, \dots, M,$$

in accordance with  $(3.105)$ .

An alternative to  $(3.119)$  approximates the LIBOR rates under the spot measure using

$$\hat{L}_n(t_{i+1}) = \hat{L}_n(t_i) \times \exp\left(\left[\mu_n(\hat{L}(t_i), t_i) - \frac{1}{2} \|\sigma_n(t_i)\|^2\right] [t_{i+1} - t_i] + \sqrt{t_{i+1} - t_i} \sigma_n(t_i)^\top Z_{i+1}\right).$$
(3.120)

This is equivalent to applying an Euler scheme to  $\log L_n$ ; it may also be viewed as approximating  $L_n$  by geometric Brownian motion over  $[t_i, t_{i+1}],$  with drift and volatility parameters fixed at  $t_i$ . This method seems particularly attractive in the case of deterministic  $\sigma_n$ , since then  $L_n$  is close to lognormal. A further property of  $(3.120)$  is that it keeps all  $L_n$  positive, whereas  $(3.119)$  can produce negative rates.

For both of these algorithms it is important to note that our definition of  $\eta$  makes  $\eta$  right-continuous. For the original continuous-time processes we

could just as well have taken  $\eta$  to be left-continuous, but the distinction is important in the discrete approximation. If  $t_i = T_k$ , then  $\eta(t_i) = k+1$  and the sum in each  $\mu_n(\hat{L}(t_i), t_i)$  starts at  $k+1$ . Had we taken  $\eta$  to be left-continuous, we would have  $\eta(T_i) = k$  and thus an additional term in each  $\mu_n$ . It seems intuitively more natural to omit this term as time advances beyond  $T_k$  since  $L_k$  ceases to be meaningful after  $T_k$ . Glasserman and Zhao [151] and Sidenius [330] both find that omitting it (i.e., taking  $\eta$  right-continuous) results in smaller discretization error.

Both  $(3.119)$  and  $(3.120)$  have obvious counterparts for simulation under the forward measure  $P_{M+1}$ . The only modification necessary is to replace  $\mu_n(\hat{L}(t_i), t_i)$  with

$$\mu_n(\hat{L}(t_i), t_i) = -\sum_{j=n+1}^M \frac{\delta_j \hat{L}_j(t_i) \sigma_n(t_i)^\top \sigma_j(t_i)}{1 + \delta_j \hat{L}_j(t_i)}.$$

Notice that  $\mu_M \equiv 0$ . It follows that if the  $\sigma_M$  is deterministic and constant between the  $t_i$  (for example, constant between tenor dates), then the log Euler scheme (3.120) with  $\mu_M = 0$  simulates  $L_M$  without discretization error under the forward measure  $P_{M+1}$ . None of the  $L_n$  is simulated without discretization error under the spot measure, but we will see that the spot measure is nevertheless generally preferable for simulation.

### Martingale Discretization

In our discussion of simulation in the HJM setting, we devoted substantial attention to the issue of choosing the discrete drift to keep the model arbitragefree even after discretization. It is therefore natural to examine whether an analogous choice of drift can be made in the LIBOR rate dynamics. In the HJM setting, we derived the discrete drift from the condition that the discretized discounted bond prices must be martingales. In the LIBOR market model, the corresponding requirement is that

$$\hat{D}_n(t_i) = \prod_{j=0}^{n-1} \frac{1}{1 + \delta_j \hat{L}_j(t_i \wedge T_j)}$$
(3.121)

be a martingale (in i) for each n under the spot measure; see (3.109). Under the forward measure, the martingale condition applies to

$$\hat{D}_n(t_i) = \prod_{j=n}^{M} \left( 1 + \delta_j \hat{L}_j(t_i) \right); \tag{3.122}$$

see  $(3.113)$ .

Consider the spot measure first. We would like, as a special case of  $(3.121)$ , for  $1/(1 + \delta_1 \hat{L}_1)$  to be a martingale. Using the Euler scheme (3.119), this requires

3.7 Forward Rate Models: Simple Rates 177

$$\mathsf{E}\left[\frac{1}{1+\delta_1(\hat{L}_1(0)[1+\mu_1t_1+\sqrt{t_1}\sigma_1^\top Z_1)]}\right] = \frac{1}{1+\delta_1\hat{L}_1(0)},$$

the expectation taken with respect to  $Z_1 \sim N(0, I)$ . However, because the denominator inside the expectation has a normal distribution, the expectation is infinite no matter how we choose  $\mu_1$ . There is no discrete drift that preserves the martingale property. If, instead, we use the method in  $(3.120)$ , the condition becomes

$$\mathsf{E}\left[\frac{1}{1+\delta_1(\hat{L}_1(0)\exp([\mu_1-\|\sigma_1\|^2/2]t_1+\sqrt{t_1}\sigma_1^\top Z_1))}\right] = \frac{1}{1+\delta_1\hat{L}_1(0)}$$

In this case, there is a value of  $\mu_1$  for which this equation holds, but there is no explicit expression for it. The root of the difficulty lies in evaluating an  $\text{expression of the form}$ 

$$\mathsf{E}\left[\frac{1}{1+\exp(a+bZ)}\right], \quad Z \sim N(0,1),$$

which is effectively intractable. In the HJM setting, calculation of the discrete drift relies on evaluating far more convenient expressions of the form  $E[\exp(a +$  $bZ$ ]; see the steps leading to (3.97).

Under the forward measure, it is feasible to choose  $\mu_1$  so that  $D_2$  in (3.122) is a martingale using an Euler scheme for either  $L_1$  or  $\log L_1$ . However, this quickly becomes cumbersome for  $D_n$  with larger values of n. As a practical matter, it does not seem feasible under any of these methods to adjust the drift to make the deflated bond prices martingales. A consequence of this is that if we price bonds in the simulation by averaging replications of  $(3.121)$ or (3.122), the simulation price will not converge to the corresponding  $B_n(0)$ as the number of replications increases.

An alternative strategy is to discretize and simulate the deflated bond prices themselves, rather than the forward LIBOR rates. For example, under the spot measure, the deflated bond prices satisfy

$$\frac{dD_{n+1}(t)}{D_{n+1}(t)} = -\sum_{j=\eta(t)}^{n} \left(\frac{\delta_j L_j(t)}{1+\delta_j L_j(t)}\right) \sigma_j^{\top}(t) dW(t)$$
$$= \sum_{j=\eta(t)}^{n} \left(\frac{D_{j+1}(t)}{D_j(t)} - 1\right) \sigma_j^{\top}(t) dW(t). \tag{3.123}$$

An Euler scheme for  $\log D_{n+1}$  therefore evolves according to

$$D_{n+1}(t_{i+1}) =$$
  
$$\hat{D}_{n+1}(t_i) \exp\left(-\frac{1}{2} \|\hat{\nu}_{n+1}(t_i)\|^2 [t_{i+1} - t_i] + \sqrt{t_{i+1} - t_i} \hat{\nu}_{n+1}(t_i)^\top Z_{i+1}\right) \tag{3.124}$$

with

 $\sim$ 

$$\hat{\nu}_{n+1}(t_i) = \sum_{j=\eta(t_i)}^n \left(\frac{\hat{D}_{j+1}(t_i)}{\hat{D}_j(t_i)} - 1\right) \sigma_j(t_i). \tag{3.125}$$

In either case, the discretized deflated bond prices are automatically martingales; in  $(3.124)$  they are positive martingales and in this sense the discretization is arbitrage-free. From the simulated  $D_n(t_i)$  we can then define the discretized forward LIBOR rates by setting

$$\hat{L}_n(t_i) = \frac{1}{\delta_n} \left( \frac{\hat{D}_n(t_i) - \hat{D}_{n+1}(t_i)}{\hat{D}_{n+1}(t_i)} \right),$$

for  $n = 1, \ldots, M$ . Any other term structure variables (e.g., swap rates) required in the simulation can then be defined from the  $L_n$ .

Glasserman and Zhao  $[151]$  recommend replacing

$$\left(\frac{\hat{D}_{j+1}(t_i)}{\hat{D}_j(t_i)} - 1\right) \quad \text{with} \quad \min\left\{ \left(\frac{\hat{D}_{j+1}(t_i)}{\hat{D}_j(t_i)}\right)^+ - 1, 0\right\}.\tag{3.126}$$

This modification has no effect in the continuous-time limit because  $0 \leq$  $D_{j+1}(t) \leq D_j(t)$  (if  $L_j(t) \geq 0$ ). But in the discretized process the ratio  $\ddot{D}_{j+1}/\ddot{D}_j$  could potentially exceed 1.

Under the forward measure  $P_{M+1}$ , the deflated bond prices (3.113) satisfy

$$\frac{dD_{n+1}(t)}{D_{n+1}(t)} = \sum_{j=n+1}^{M} \frac{\delta_j L_j(t)}{1 + \delta_j L_j(t)} \sigma_j(t)^{\top} dW^{M+1}(t)$$
$$= \sum_{j=n+1}^{M} \left(1 - \frac{D_{j+1}(t)}{D_j(t)}\right) \sigma_j^{\top}(t) dW^{M+1}(t). \tag{3.127}$$

We can again apply an Euler discretization to the logarithm of these variables to get  $(3.124)$ , except that now

$$\hat{\nu}_{n+1}(t_i) = \sum_{j=n+1}^{M} \left(1 - \frac{\hat{D}_{j+1}(t_i)}{\hat{D}_j(t_i)}\right) \sigma_j(t_i),$$

possibly modified as in  $(3.126)$ .

Glasserman and Zhao  $[151]$  consider several other choices of variables for discretization, including (under the spot measure) the normalized differences

$$V_n(t) = \frac{D_n(t) - D_{n+1}(t)}{B_1(0)}, \quad n = 1, \dots, M;$$

these are martingales because the deflated bond prices are martingales. They satisfy

$$\frac{dV_n}{V_n} = \left[ \left( \frac{V_n + V_{n-1} + \dots + V_1 - 1}{V_{n-1} + \dots + V_1 - 1} \right) \sigma_n^{\top} + \sum_{j=\eta}^{n-1} \left( \frac{V_j}{V_{j-1} + \dots + V_1 - 1} \right) \sigma_j^{\top} \right] dW,$$

with the convention  $\sigma_{M+1} \equiv 0$ . Forward rates are recovered using

$$\delta_n L_n(t) = \frac{V_n(t)}{V_{n+1}(t) + \dots + V_{M+1}(t)}$$

Similarly, the variables

 $\mathbb{C}$ 

$$\delta_n X_n(t) = \delta_n L_n(t) \prod_{j=n+1}^M (1 + \delta_j L_j(t))$$

are differences of deflated bond prices under the forward measure  $P_{M+1}$  and thus martingales under that measure. The  $X_n$  satisfy

$$\frac{dX_n}{X_n} = \left(\sigma_n^\top + \sum_{j=n+1}^M \frac{\delta_j X_j \sigma_j^\top}{1 + \delta_j X_j + \dots + \delta_M X_M}\right) \, dW^{M+1}.$$

Forward rates are recovered using

$$L_n = \frac{X_n}{1 + \delta_{n+1}X_{n+1} + \dots + \delta_M X_M}$$

Euler discretizations of  $\log V_n$  and  $\log X_n$  preserve the martingale property and thus keep the discretized model arbitrage-free.

### Pricing Derivatives

The pricing of a derivative security in a simulation proceeds as follows. Using any of the methods considered above, we simulate paths of the discretized variables  $\hat{L}_1,\ldots,\hat{L}_M$ . Suppose we want to price a derivative with a payoff of  $g(L(T_n))$  at time  $T_n$ . Under the spot measure, we simulate to time  $T_n$  and then calculate the deflated payoff

$$g(\hat{L}(T_n)) \cdot \prod_{j=0}^{n-1} \frac{1}{1 + \delta_j \hat{L}_j(T_j)}.$$

Averaging over independent replications produces an estimate of the derivative's price at time 0. If we simulate under the forward measure, the estimate consists of independent replications of

$$g(\hat{L}(T_n)) \cdot B_{M+1}(0) \prod_{j=1}^{n-1} (1 + \delta_j \hat{L}_j(T_j)).$$

Glasserman and Zhao [151] compare various simulation methods based, in part, on their discretization error in pricing caplets. For the case of a caplet over  $[T_{n-1}, T_n]$ , take  $g(x) = \delta_{n-1}(x - K)^+$  in the expressions above. If the  $\sigma_i$ are deterministic, the caplet price is given by the Black formula, as explained in Section 3.7.2. However, because of the discretization error, the simulation price will not in general converge exactly to the Black price as the number of replications increase. The bias in pricing caplets serves as a convenient indication of the magnitude of the discretization error.

Figure 3.19, reproduced from Glasserman and Zhao [151], graphs biases in caplet pricing as a function of caplet maturity for various simulation methods. The horizontal line through the center of each panel corresponds to zero bias. The error bars around each curve have halfwidths of one standard error, indicating that the apparent biases are statistically significant. Details of the parameters used for these experiments are reported in Glasserman and Zhao  $[151]$  along with several other examples.

These and other experiments suggest the following observations. The smallest biases are achieved by simulating the differences of deflated bond prices (the  $V_n$  in the spot measure and the  $X_n$  in the forward measure) using an Euler scheme for the logarithms of these variables. (See Glasserman and Zhao [151] for an explanation of the modified  $V_n$  method.) An Euler scheme for  $\log D_n$  is nearly indistinguishable from an Euler scheme for  $L_n$ . Under the forward measure  $P_{M+1}$ , the final caplet is priced without discretization error by the Euler schemes for  $\log X_n$  and  $\log L_n$ ; these share the feature that they make the discretized rate  $L_M$  lognormal.

The graphs in Figure 3.19 compare discretization biases but say nothing about the relative variances of the methods. Glasserman and Zhao  $[151]$ find that simulating under the spot measure usually results in smaller variance than simulating under the forward measure, especially at high levels of volatility. An explanation for this is suggested by the expressions  $(3.109)$  and  $(3.113)$  for the deflated bond prices under the two measures; whereas  $(3.109)$ always lies between 0 and 1,  $(3.113)$  can take arbitrarily large values. This affects derivatives pricing through the discounting of payoffs.

### 3.7.4 Volatility Structure and Calibration

In our discussion of LIBOR market models we have taken the volatility factors  $\sigma_n(t)$  as inputs without indicating how they might be specified. In practice, these coefficients are chosen to calibrate a model to market prices of actively traded derivatives, especially caps and swaptions. (The model is automatically calibrated to bond prices through the relations  $(3.105)$  and  $(3.106)$ .) Once the model has been calibrated to the market, it can be used to price less liquid

![](_page_102_Figure_1.jpeg)

Ą,

 $\mathbb{R}^n$ 

Fig. 3.19. Comparison of biases in caplet pricing for various simulation methods. Top panel uses spot measure; method A is an Euler scheme for  $L_n$  and methods B-E are Euler schemes for log variables. Bottom panel uses the forward measure  $P_{M+1}$ ; method A is an Euler scheme for  $L_n$  and methods B-D are Euler schemes for  $\log$  variables.

instruments for which market prices may not be readily available. Accurate and efficient calibration is a major topic in its own right and we can only touch on the key issues. For a more extensive treatment, see James and Webber [194] and Rebonato [303]. Similar considerations apply in both the HJM framework and in LIBOR market models; we discuss calibration in the LIBOR setting because it is somewhat simpler. Indeed, convenience in calibration is one of the main advantages of this class of models.

The variables  $\sigma_n(t)$  are the primary determinants of both the level of volatility in forward rates and the correlations between forward rate. It is often useful to distinguish these two aspects and we will consider the overall

level of volatility first. Suppose we are given the market price of a caplet for the interval  $[T_n, T_{n+1}]$  and from this price we calculate an implied volatility  $v_n$  by inverting the Black formula (3.117). (We can assume that the other parameters of the formula are known.) If we choose  $\sigma_n$  to be any deterministic  $\mathbb{R}^d$ -valued function satisfying

$$\frac{1}{T_n} \int_0^{T_n} \|\sigma_n(t)\|^2 \, dt = v_n^2,$$

then we know from the discussion in Section 3.7.2 that the model is calibrated to the market price of this caplet, because the model's caplet price is given by the Black formula with implied volatility equal to the square root of the expression on the left. By imposing this constraint on all of the  $\sigma_i$ , we ensure that the model is calibrated to all caplet prices. (As a practical matter, it may be necessary to infer the prices of individual caplets from the prices of caps, which are portfolios of caplets. For simplicity, we assume caplet prices are available.)

Because LIBOR market models do not specify interest rates over accrual periods shorter than the intervals  $[T_i, T_{i+1}],$  it is natural and customary to restrict attention to functions  $\sigma_n(t)$  that are constant between tenor dates. We take each  $\sigma_n$  to be right-continuous and thus denote by  $\sigma_n(T_i)$  its value over the interval  $[T_i, T_{i+1})$ . Suppose, for a moment, that the model is driven by a scalar Brownian motion, so  $d = 1$  and each  $\sigma_n$  is scalar valued. In this case, it is convenient to think of the volatility structure as specifed through a lower-triangular matrix of the following form:

$$\begin{pmatrix}\n\sigma_1(T_0) \\
\sigma_2(T_0) & \sigma_2(T_1) \\
\vdots & \vdots & \ddots \\
\sigma_M(T_0) & \sigma_M(T_1) & \cdots & \sigma_M(T_{M-1})\n\end{pmatrix}.$$

The upper half of the matrix is empty (or irrelevant) because each  $L_n(t)$  ceases to be meaningful for  $t > T_n$ . In this setting, we have

$$\int_0^{T_n} \sigma_n^2(t) dt = \sigma_n^2(T_0)\delta_0 + \sigma_n^2(T_1)\delta_1 + \cdots + \sigma_n^2(T_{n-1})\delta_{n-1},$$

so caplet prices impose a constraint on the sums of squares along each row of the matrix.

The volatility structure is *stationary* if  $\sigma_n(t)$  depends on n and t only through the difference  $T_n - t$ . For a stationary, single-factor, piecewise constant volatility structure, the matrix above takes the form

$$\begin{pmatrix}\n\sigma(1) & & & \\
\sigma(2) & \sigma(1) & & \\
\vdots & \vdots & \ddots & \\
\sigma(M) \ \sigma(M-1) \ \cdots \ \sigma(1)\n\end{pmatrix}$$

for some values  $\sigma(1), \ldots, \sigma(M)$ . (Think of  $\sigma(i)$  as the volatility of a forward rate  $i$  periods away from maturity.) In this case, the number of variables just equals the number of caplet maturities to which the model may be calibrated. Calibrating to additional instruments requires introducing nonstationarity or additional factors.

 $\sim$ 

In a multifactor model (i.e.,  $d \geq 2$ ) we can think of replacing the entries  $\sigma_n(T_i)$  in the volatility matrix with the norms  $\|\sigma_n(T_i)\|$ , since the  $\sigma_n(T_i)$  are now vectors. With piecewise constant values, this gives

$$\int_0^{T_n} \|\sigma_n(t)\|^2 dt = \|\sigma_n(T_0)\|^2 \delta_0 + \|\sigma_n(T_1)\|^2 \delta_1 + \dots + \|\sigma_n(T_{n-1})\|^2 \delta_{n-1},$$

so caplet implied volatilities continue to constrain the sums of squares along each row. This also indicates that taking  $d \geq 2$  does not provide additional flexibility in matching these implied volatilities.

The potential value of a multifactor model lies in capturing correlations between forward rates of different maturities. For example, from the Euler approximation in  $(3.120)$ , we see that over a short time interval the correlation between the increments of  $\log L_j(t)$  and  $\log L_k(t)$  is approximately

$$\frac{\sigma_k(t)^\top \sigma_j(t)}{\|\sigma_k(t)\| \, \|\sigma_j(t)\|}$$

These correlations are often chosen to match market prices of swaptions (which, unlike caps, are sensitive to rate correlations) or to match historical correlations.

In the stationary case, we can visualize the volatility factors by graphing them as functions of time to maturity. This can be useful in interpreting the correlations they induce. Figure 3.20 illustrates three hypothetical factors in a model with  $M = 15$ . Because the volatility is assumed stationary, we may write  $\sigma_n(T_i) = \sigma(n-i)$  for some vectors  $\sigma(1), \ldots, \sigma(M)$ . In a three-factor model, each  $\sigma(i)$  has three components. The three curves in Figure 3.20 are graphs of the three components as functions of time to maturity. If we fix a time to maturity on the horizontal axis, the total volatility at that point is given by the sums of squares of the three components; the inner products of these three-dimensional vectors at different times determine the correlations between the forward rates.

Notice that the first factor in Figure 3.20 has the same sign for all maturities; regardless of the sign of the increment of the driving Brownian motion, this factor moves all forward rates in the same direction and functions approximately as a parallel shift. The second factor has values of opposite signs at short and long maturities and will thus have the effect of tilting the forward curve (up if the increment in the second component of the driving Brownian motion is positive and down if it is negative). The third factor bends the forward curve by moving intermediate maturities in the opposite direction of long and short maturities, the direction depending on the sign of the increment of the third component of the driving Brownian motion.

3 Generating Sample Paths 184

![](_page_105_Figure_1.jpeg)

Fig.  $3.20$ . Hypothetical volatility factors.

The hypothetical factors in Figure 3.20 are the first three principal components of the matrix

$$0.12^2 \exp((-0.8\sqrt{|i-j|})), \quad i,j=1,\ldots,15.$$

More precisely, they are the first three eigenvectors of this matrix as ranked by their eigenvalues, scaled to have length equal to their eigenvalues. It is common in practice to use the principal components of either the covariance matrix or the correlation matrix of changes in forward rates in choosing a factor structure. Principal components analysis typically produces the qualitative features of the hypothetical example in Figure  $3.20$ ; see, e.g., the examples in James and Webber  $[194]$  or Rebonato  $[304]$ .

An important feature of LIBOR market models is that a good deal of calibration can be accomplished through closed form expressions or effective approximations for the prices of caps and swaptions. This makes calibration fast. In the absence of formulas or approximations, calibration is an iterative procedure requiring repeated simulation at various parameter values until the model price matches the market. Because each simulation can be quite time consuming, calibration through simulation can be onerous.
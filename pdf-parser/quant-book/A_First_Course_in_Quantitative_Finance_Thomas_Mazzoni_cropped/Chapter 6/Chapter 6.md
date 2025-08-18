✖

# **6 Modern Portfolio Theory**

Modern portfolio theory (MPT) is mainly due to Harry Markowitz (1952, 1959), who received the Nobel Prize in Economics 1990 for his pioneering work. What is remarkable about MPT is that it is conceptually easy to grasp, because it is deeply embedded in the *Gauss*ian world of distributions, but at the same time it reveals completely general and important principles, like the consequences of diversification. Those principles remain true, even in highly sophisticated market models like APT.

# **6.1 The Gaussian Framework**

It may sound strange to call the work of Markowitz "modern" portfolio theory nowadays, since it is more than 60 years old. Nevertheless, because of its fundamental nature it deserves at least the attribute "classical." We will keep on calling it modern portfolio theory (MPT), where the letter M could interchangeably stand for Markowitz. MPT is concerned with the analysis of returns of risky assets over intermediate- and long-term horizons. It focuses on the first two moments of the return distribution, the mean µ and the variance σ 2 . It is worthwhile to demonstrate that both the long-term nature of returns and the limiting moment condition, each by itself, leads inevitably to a *Gauss*ian framework.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

As for the term structure, it is always possible, to decompose a long-term return into a sum of short-term returns. If the short-term is not too short, returns can be assumed independent or at least uncorrelated, and thus, due to the central limit theorem, large sums of them tend to be normally distributed. That sounds almost too good to be true, so let's see how it actually works. Assume that we partition a given time interval into *N* smaller subintervals. Let these subintervals be such that we can assume the short-term returns *R<sup>n</sup>* independent and identically distributed with say *E* [ *R<sup>n</sup>* ] = 0 and Var[ *R<sup>n</sup>* ] = 1 *N* for *n* = 1, . . . , *N*. We can always do an affine transformation on *R<sup>n</sup>* to obtain these conditions, so there is no harm done. Now let's ask, how the sum

$$R = \sum_{n=1}^{N} R_n \tag{6.1}$$

is distributed? We know that the characteristic function φ(*u*) of *R* has to be the product of all characteristic functions of *Rn*, which are all the same, because all short-term returns are identically distributed. Therefore, we have

$$\varphi(u) = \varphi_n^N(u). \tag{6.2}$$

So what is the characteristic function φ*n*(*u*) of *Rn*? Recall the definition (2.34) on page 21 of the characteristic function

$$\varphi_n(u) = E[e^{iuR_n}] = E\left[1 + iuR_n + \frac{1}{2}i^2u^2R_n^2 + \cdots\right] \\
\approx 1 - \frac{1}{2}u^2\frac{1}{N},\n$$
(6.3)

where we simply *Taylor*-expanded the complex exponential and neglected terms of higher order than O ( *N*<sup>−</sup><sup>1</sup> ) , because we want *N* to grow large.

**Quick calculation 6.1** Can you see why *E* [ *R* 2 *n* ] = Var[ *R<sup>n</sup>* ] ?

In the limit *N* → ∞ we obtain

$$\lim_{N \to \infty} \varphi(u) = \lim_{N \to \infty} \left( 1 - \frac{\frac{1}{2}u^2}{N} \right)^N = e^{-\frac{1}{2}u^2},\tag{6.4}$$

which is immediately identified as the characteristic function of a standard normal random variable. We have used the very restrictive assumption of independent returns, to prove the central limit theorem in a simple way. It indeed holds for merely uncorrelated returns, too (see Billingsley, 1995, theorem 35.11).

If we accept the central limit argument, then focusing on the mean and variance is absolutely justified, because the normal distribution is completely determined by its first two moments. If we however reject it, there is another chain of arguments, also leading to a *Gauss*ian framework. This one is a little more subtle. Suppose you have no idea, what the utility function of a representative agent looks like. So use quadratic utility as a local approximation. The *von Neumann–Morgenstern*-functional then becomes

$$U[R] = E[-(\eta - R)^{2}] = -E[\eta^{2} - 2\eta R + R^{2}]$$
  
=  $-\eta^{2} + 2\eta\mu - \sigma^{2} - \mu^{2}$   
=  $-(\eta - \mu)^{2} - \sigma^{2}$ . (6.5)

The bliss point η is a parameter of the quadratic utility function and carries no information about the return distribution. The only relevant parameters left are µ and σ 2 , the mean and the variance. That was the easy part. Now that we are stuck with the first two moments, we have to show that the best guess we can make about the unknown probability distribution of *R* is a *Gauss*ian. To do this, we need a concept from information theory, the entropy functional

$$S[X] = -\int f(x) \log f(x) dx,$$
(6.6)

where *f*(*x*) is the unknown probability density function, yet to be determined. For a discussion on information and entropy see Bernardo and Smith (2000, sect. 2.7). Roughly speaking, entropy is a measure for the absence of information. What we are looking for is a probability distribution, incorporating solely the existence of a finite expectation

value and a finite variance, and nothing more. In other words, we are looking for the maximum entropy distribution, given a finite mean and variance.

Our formal starting point is the vector space of real random variables with finite first and second moments, *L* 2 (Ω,F ,*P*). The *L* stands for "Lebesgue" here, not for a linear functional. But first we have to explain what it means, to differentiate a functional with respect to a specific coefficient of a vector, or with respect to a function at a specific point, respectively. Let's first take a look at the more intuitive case of R *<sup>N</sup>*. The functional derivative with respect to a vector |*a*⟩ is a form,

$$\frac{\delta L}{\delta |a\rangle} = \langle \delta L|. \tag{6.7}$$

If we want to differentiate with respect to a specific component, say *am*, we have to use the chain rule

$$\frac{\partial L}{\partial a_m} = \langle \eth L | \partial_m a \rangle,\tag{6.8}$$

where we have used the shorthand notation |∂*ma*⟩ for the vector with components <sup>∂</sup>*a<sup>n</sup>* ∂*a<sup>m</sup>* . Obviously, <sup>∂</sup>*a<sup>n</sup>* ∂*a<sup>m</sup>* = δ*nm* and hence |∂*ma*⟩ = |*em*⟩. We then obtain

$$\frac{\partial L}{\partial a_m} = \langle \delta L | e_m \rangle = \sum_{n=1}^N \delta L_n \delta_{nm} = \delta L_m. \tag{6.9}$$

Now let's look at the function space *L* 2 . The function *f*(*x*) can be thought of as an infinite collection of numbers, namely function values, one for each possible value of *x*. To push this analogy a little bit further, imagine |*f*⟩ as a column vector with infinitely many components. We want to differentiate a functional with respect to one of them, say *f*(*y*). We have then in complete analogy

$$\frac{\partial L}{\partial f(y)} = \langle \delta L | e(y) \rangle = \int \delta L(x) \delta(x - y) dx = \delta L(y), \tag{6.10}$$

where Dirac's delta function δ(*x* − *y*) is the continuous analogue of the *Kronecker*-delta δ*nm* (3.18) on page 36. Let's not worry too much about the delta function at this point, we will come back to it later. In fact, the last equality in (6.10) gives a correct definition. Let's see how this works in a simple example.

**Example 6.1**

Consider the vector space *L* 2 (Ω,F ,*P*) of real random variables with finite variance. Assume you know that realizations of the random variable *X* can only occur in the interval [*a*, *b*]. What is the maximum entropy distribution of *X*?

### Solution

To find the desired distribution, we have to maximize the entropy functional under the normalization constraint,

$$\max_{f(y)} S[X] \quad \text{subject to} \quad \int_{a}^{b} f(x) dx = 1.$$

This is done using Lagrange's method. The computation of the first order condition with respect to  $f(y)$  is given here in full detail

$$\begin{split} \frac{\partial \mathcal{L}}{\partial f(y)} &= -\int_{a}^{b} \frac{\delta(f(x)\log f(x))}{\delta f(x)} \cdot \delta(x-y) dx - \lambda \int_{a}^{b} \frac{\delta f(x)}{\delta f(x)} \cdot \delta(x-y) dx \\ &= -\int_{a}^{b} (\log f(x) + 1)\delta(x-y) dx - \lambda \int_{a}^{b} \delta(x-y) dx \\ &= -\log f(y) - 1 - \lambda \stackrel{!}{=} 0, \end{split}$$

where  $\mathcal{L}$  is the *Lagrange*-function. The  $\delta$ -notation has been used a bit sloppily here, to indicate that the derivative is with respect to the entire function  $f(x)$ . After trivial algebraic manipulations one obtains

$$f(y) = e^{-(1+\lambda)} = c$$

where  $c$  is a constant, not yet determined. We have now to consider the normalization condition, reproduced by the second first order condition with respect to  $\lambda$ 

$$\int_{a}^{b} f(y) dy = \int_{a}^{b} c dy = cy \Big|_{a}^{b} = c(b-a) \stackrel{!}{=} 1,$$

from which we immediately conclude that  $c = \frac{1}{b-a}$ . Thus, X is uniformly distributed in the interval  $[a, b]$ , with density function

$$f(y) = \frac{1}{b-a}.$$

This is a very intuitive result, because there was no more initial information than the possible range of realizations. Don't worry about the variable name  $\gamma$  here, it is only a label. We could as well rename it back to  $x$ , to clean up the notation.

Now let's return to the original question. What is the maximum entropy distribution, given the first two moments are defined? Except for the normalization constraint, we have two additional constraints in the optimization problem,

$$\int_{-\infty}^{\infty} x f(x) dx = \mu \quad \text{and} \quad \int_{-\infty}^{\infty} x^2 f(x) dx = \sigma^2 + \mu^2. \tag{6.11}$$

**Quick calculation 6.2** Confirm that the second constraint is equivalent to  $Var[X] = \sigma^2$ .

Collecting all terms in a *Lagrange*-function as in Example 6.1, we obtain the first order condition

$$\frac{\partial \mathcal{L}}{\partial f(y)} = -\log f(y) - (1 + \lambda_0) - \lambda_1 y - \lambda_2 y^2 = 0. \tag{6.12}$$

**Quick calculation 6.3** Verify this first order condition.

Rearranging terms and exponentiating both sides of the equation yields

$$f(y) = ce^{-(\lambda_1 y + \lambda_2 y^2)} \quad \text{with} \quad c = e^{-(1 + \lambda_0)}.$$
 (6.13)

To determine the unknown constant *c*, we have to use the normalization constraint. But now we run into a problem. There is no way to integrate the exponential with our usual tricks like substitution or integration by parts. The good news is, it can be done by squaring the integral and changing coordinates. The solution of this so-called *Gauss*ian integral is

$$\int_{-\infty}^{\infty} e^{-(\lambda_1 y + \lambda_2 y^2)} dy = \sqrt{\frac{\pi}{\lambda_2}} \exp\left(\frac{\lambda_1^2}{4\lambda_2}\right) = \frac{1}{c} \quad \text{for} \quad \lambda_2 > 0,$$
 (6.14)

see Gradshteyn and Ryzhik (2007, p. 337). We are on the right track. Using this result, we obtain

$$f(y) = \sqrt{\frac{\lambda_2}{\pi}} \exp\left(-\frac{\lambda_1^2}{4\lambda_2} - \lambda_1 y - \lambda_2 y^2\right) = \sqrt{\frac{\lambda_2}{\pi}} \exp\left(-\lambda_2 \left(y + \frac{\lambda_1}{2\lambda_2}\right)^2\right). \tag{6.15}$$

Now it is time for an educated guess. We will assume certain expressions for the remaining *Lagrange*-multipliers and check afterwards that they satisfy the constraints. Take

$$\lambda_1 = -\frac{\mu}{\sigma^2} \quad \text{and} \quad \lambda_2 = \frac{1}{2\sigma^2}.\n$$
(6.16)

We can already see that the requirement λ<sup>2</sup> > 0 from the solution of the *Gauss*ian integral (6.14) is satisfied. From (6.15) we get

$$f(y) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(y-\mu)^2}{2\sigma^2}},$$
(6.17)

the normal probability density function. It is immediately clear that the remaining moment constraints are satisfied and we are done.

The normal distribution assumption in modern portfolio theory is by no means a matter of convenience, but has a strong theoretical rationale. We are lucky, because the normal distribution has very pleasant properties, allowing many analytical results. Leaving this path, there are very few results to be obtained without approximations or numerical computations.

# **6.2 Mean-Variance Analysis**

In the *Markowitz*-world, portfolios are entirely described by their expected returns and variances. A given portfolio is said to dominate another one, if its µ-σ-configuration results in a higher level of utility for every possible risk-averse agent. But what are the

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

general characteristics of a curve of constant utility? If we are not allowed to specify a particular utility function beforehand, we can *Taylor*-expand the expected utility functional

$$U[R] = E[u(R)] = u(\mu) + u'(\mu)E[(R - \mu)] + \frac{1}{2}u''(\mu)E[(R - \mu)^{2}] + \cdots$$
  

$$\approx u(\mu) + \frac{1}{2}u''(\mu)\sigma^{2}.$$
(6.18)

If we multiply and divide the second order expansion term by *u* ′ (µ), we can write (6.18) in a more transparent way

$$U[R] \approx u(\mu) - \frac{1}{2}u'(\mu) \text{ARA}(\mu)\sigma^2 \approx u(\mu) - u'(\mu)\pi, \tag{6.19}$$

where π is the risk premium, see (4.20) on page 67. We did a lot of approximating here, but we always kept second order terms, because risk aversion is encoded in the second derivative of an agent's utility function. Therefore, we can be sure that we did not lose any characteristic features. The risk premium π is guaranteed to be an increasing function of σ 2 , with π = 0 for σ <sup>2</sup> = 0, as long as the agent is risk averse.

**Quick calculation 6.4** Verify that the risk premium for CARA-utility is π ≈ 1 2 ασ<sup>2</sup> .

We now have enough information to sketch the generic shape of the utility functional; see Figure 6.1. As you can see, the projections of all curves of constant utility *U* onto the µ-σ-plane are convex. This projection is illustrated in Figure 6.2 and it is called a µ-σ-diagram.

**Quick calculation 6.5** What does the curve of constant utility for a risk-neutral agent look like in the µ-σ-diagram? It is not a diagonal line!

![](_page_5_Figure_9.jpeg)

**Fig. 6.1** 3D Mean-variance analysis – Approximation of a generic utility functional

![](_page_6_Figure_1.jpeg)

**Fig. 6.2** Mean-variance analysis – µ-σ-diagram with curve of constant utility and several securities

The degree of convexity depends on the individual utility function, but since *u* is strictly concave for any risk-averse agent, the curves *U* = const. have to remain strictly convex. This allows for a fundamental statement about securities or portfolios of securities according to their positions in the µ-σ-diagram. The concept is called µ-σ-dominance or sometimes stochastic dominance of zeroth order. A security *A* is said to dominate a security *B*, if one of the following three conditions hold:

1. 
$$\mu_A > \mu_B$$
 and  $\sigma_A = \sigma_B$ ,  
2.  $\mu_A = \mu_B$  and  $\sigma_A < \sigma_B$ ,  
3.  $\mu_A > \mu_B$  and  $\sigma_A < \sigma_B$ .  
(6.20)

There are three securities indicated in the µ-σ-diagram in Figure 6.2. We can say a lot about their dominance relationships. Security *A* dominates security *B* because the first condition in (6.20) holds. Security *A* also dominates *C*, because of condition two. But securities *B* and *C* have no dominance relationship. Note that *A* also dominates every hypothetical portfolio of securities, situated on the line connecting *B* and *C*, because of condition three. You might expect that those hypothetical portfolios are linear combinations of *B* and *C*, but this is not true in general. We will see why in a moment. First let's explain what it means to add securities in a little more detail.

Assume the price of a portfolio *P* of securities *S*1, . . . , *SN*, say at time *t* = 0, is

$$p_0 = \langle s_0 | \theta \rangle = \sum_{n=1}^{N} s_{0n} \theta_n. \tag{6.21}$$

Then the return of portfolio *P* between *t* = 0 and *t* = 1 can be written as

$$r_{P} = \frac{p_{1} - p_{0}}{p_{0}} = \frac{1}{p_{0}} \sum_{n=1}^{N} (s_{1n} - s_{0n}) \cdot \theta_{n} = \sum_{n=1}^{N} \frac{s_{1n} - s_{0n}}{s_{0n}} \cdot \frac{s_{0n}\theta_{n}}{\langle s_{0}|\theta\rangle}$$
  
$$= \sum_{n=1}^{N} r_{n}w_{n} = \langle r|w\rangle,$$
 (6.22)

with ⟨1|*w*⟩ = 1, and *w<sup>n</sup>* is the fraction of the total portfolio value at *t* = 0, that is due to the position in *Sn*. We have assumed in (6.22) that security prices at *t* = 0 and at *t* = 1 are known and thus, returns are deterministic. We indicated this fact by using

small letters. Generally, returns are random variables or more precisely, multivariate normally distributed random variables in MPT. A multivariate normally distributed vector (or form) of random variables  $\langle R|$  is completely determined by its expectation vector (form)

$$\langle \mu | = \left( \mu_1 \ \mu_2 \ \dots \ \mu_N \right), \tag{6.23}$$

and its covariance matrix

$$\Sigma = \begin{pmatrix}\n\sigma_1^2 & \sigma_{12} & \dots & \sigma_{1N} \\
\sigma_{12} & \sigma_2^2 & \dots & \sigma_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{1N} & \sigma_{2N} & \dots & \sigma_N^2\n\end{pmatrix},\n$$
(6.24)

where  $\sigma_n^2 = \text{Var}[R_n]$  and  $\sigma_{nm} = \sigma_{mn} = \text{Cov}[R_n, R_m]$ . If we now form a portfolio  $P = \langle S | \theta \rangle$ , then the expectation value and variance of its return is given by

$$\mu_P = \langle \mu | w \rangle \quad \text{and} \quad \sigma_P^2 = \langle w | \Sigma | w \rangle. \tag{6.25}$$

Can you see how efficient vector notation is here? Now let's focus on a portfolio composed of only two risky securities, A and B. We call the portfolio weights w and  $1 - w$ and require for the moment that  $0 \le w \le 1$ , which means no short selling is permitted. We get for the expectation value and variance of the portfolio

$$\mu_P = w\mu_A + (1 - w)\mu_B$$
  

$$\sigma_P^2 = w^2 \sigma_A^2 + 2w(1 - w)\rho_{AB}\sigma_A\sigma_B + (1 - w)^2 \sigma_B^2,$$
(6.26)

where we have used that  $\text{Cov}[X, Y] = \rho_{XY} \sqrt{\text{Var}[X] \text{Var}[Y]}$ , see (2.33) on page 20, and  $-1 \leq \rho_{XY} \leq 1$  is the correlation coefficient.

### **Quick calculation 6.6** Confirm $(6.26)$ by using $(6.25)$ .

We are interested in the location of the possible portfolios in the  $\mu$ - $\sigma$ -diagram for different values of  $\rho_{AB}$ . The three natural choices  $\rho_{AB} = 1$ ,  $\rho_{AB} = 0$ , and  $\rho_{AB} = -1$  are illustrated in Figure 6.3 left and it is worthwhile to elaborate on them a bit further.

## Perfect correlation:

For  $\rho_{AB} = 1$  securities A and B are also called perfectly correlated. In this case we see from  $(6.26)$  that the standard deviation of the portfolio becomes

$$\sigma_P = \sqrt{(w\sigma_A + (1-w)\sigma_B)^2} = w\sigma_A + (1-w)\sigma_B, \tag{6.27}$$

where we have used the binomial theorem. In this case the resulting portfolio is indeed located on the line, connecting A and B in the  $\mu$ - $\sigma$ -diagram, because  $\mu_P$  as well as  $\sigma_P$ are linear combinations of the corresponding quantities of  $A$  and  $B$ .

![](_page_8_Figure_1.jpeg)

**Fig. 6.3** Portfolio of two risky assets with different correlation (left) and minimum variance portfolio (right)

#### **Zero correlation:**

If ρ*AB* = 0, securities *A* and *B* are called uncorrelated. The standard deviation of the portfolio is

$$\sigma_P = \sqrt{w^2 \sigma_A^2 + (1 - w)^2 \sigma_B^2}.$$
 (6.28)

In this case, one can find portfolios with smaller standard deviation than either of the original securities. This is the first glimpse of the very important concept of diversification. It can be shown in a rather tedious computation that all possible combinations of *A* and *B* lie on a hyperbola in the µ-σ-diagram.

### **Perfect anti-correlation:**

The securities *A* and *B* are said to be anti-correlated or perfectly negative correlated, if ρ*AB* = −1. This case is special in that it creates a portfolio with no risk. In other words, the return of such a portfolio would be the (shadow) risk-free rate. In a real world scenario it is highly unlikely to find two perfectly negative correlated securities. Nevertheless, let's compute the weights of the risk-free portfolio. The necessary condition is that the standard deviation vanishes,

$$\sigma_P = w\sigma_A - (1 - w)\sigma_B \stackrel{!}{=} 0. \tag{6.29}$$

This problem is easily solved and one obtains

$$w^* = \frac{\sigma_B}{\sigma_A + \sigma_B}.\tag{6.30}$$

**Quick calculation 6.7** Verify this result.

Generally, most of the time the correlation of assets is weakly positive, but even a correlation of ρ = 0.5 turns out to be beneficial if we want to reduce the risk of a portfolio. The situation is sketched schematically in Figure 6.3 right. Assume you start with 100% of security *B* in your portfolio and you want to reduce risk. As you increase the proportion of security *A*, your standard deviation will decrease, and also your expected

return. Nothing comes without a price. You will finally get to a point, where the standard deviation cannot be reduced any further. This portfolio is called the minimum variance portfolio (MVP). Note that on your way down from  $B$  to MVP, all portfolios you constructed were not dominated by any other portfolio. This is why the upper branch of the curve is called the efficient frontier. If you increase the proportion of A beyond the MVP, your standard deviation will increase again, but the expected return continues to decrease. All portfolios on the lower branch are dominated by portfolios on the upper branch with smaller or identical standard deviation. Therefore, you would not want to hold one of these lower branch portfolios.

# The Minimum Variance Portfolio

Let's first consider the familiar situation of two risky assets, A and B, before proceeding to the general case. First realize that the minimum variance portfolio (MVP) is of course at the same time the portfolio with the smallest standard deviation, because variance is the square of the standard deviation. If  $\rho_{AB}$  is not known beforehand, we have

$$\sigma_P^2 = w^2 \sigma_A^2 + 2w(1 - w)\rho_{AB}\sigma_A\sigma_B + (1 - w)^2 \sigma_B^2.$$
 (6.31)

This is what we have to minimize, without constraints. Additionally, we will no longer require  $0 \le w \le 1$ , which means short selling is permitted from here on. As a matter of convenience, we will actually minimize  $\frac{1}{2}\sigma_p^2$ ; you will see why in a moment. The necessary first order condition for a minimum is

$$\frac{1}{2}\frac{d\sigma_P^2}{dw} = w\sigma_A^2 + (1-w)\rho_{AB}\sigma_A\sigma_B - w\rho_{AB}\sigma_A\sigma_B - (1-w)\sigma_B^2 = 0.$$
 (6.32)

There it is, no additional factors of 2. Because we allowed short selling, the hyperbola of possible portfolio configurations extends to infinity in the  $\sigma$ -direction, but has only one minimum. So the first order condition is sufficient. Solving  $(6.32)$  yields

$$w_{\text{MVP}} = \frac{\sigma_B^2 - \rho_{AB}\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho_{AB}\sigma_A\sigma_B}.$$
(6.33)

**Quick calculation 6.8** Confirm this result.

That was a neat calculation. But in passing to larger portfolios, we have first to examine what we are up against. Which portfolio combinations are possible if there are N assets? And what does the efficient frontier look like?

You can see most easily what is going on for  $N > 2$  risky securities graphically. Figure 6.4 left shows the situation for  $N=4$  assets. You may for example assemble two portfolios, one containing only  $A$  and  $B$ , and the other containing only  $C$  and  $D.$  Of course you are also allowed to mix these two portfolios, and there is a continuum of such mixtures. You could have just as well assembled different portfolios, say

# 6.3

![](_page_10_Figure_1.jpeg)

**Fig. 6.4** Possible portfolio combinations for *N* > 2 risky assets

from *A* and *C*, and from *B* and *D*, and mixed those. If you exhaust all possibilities for assembling and mixing portfolios, you obtain a new curve of variance efficient portfolio combinations, including all assets. An even more tedious calculation shows that this curve is a hyperbola, too. In fact this property carries over to the case of arbitrary *N*, where we will see much easier why this is the case. So the situation in the *N*-security world is conceptually no more difficult than for two securities; see Figure 6.4 right. The only difference is that not every admissible portfolio with a fixed expected return has the smallest possible variance, but only those portfolios located on the variance efficient hyperbola.

To find the minimum variance portfolio in a *N*-security world, we have to solve the constrained optimization problem

$$\min_{\langle w|} \frac{1}{2} \langle w|\Sigma|w\rangle \quad \text{subject to} \quad \langle 1|w\rangle = 1. \tag{6.34}$$

**Quick calculation 6.9** Write the *Lagrange*-function for this optimization problem.

We obtain two first order conditions, which are sufficient, because we are still looking for a minimum in a hyperbola that extends to infinity in the σ-direction. The first condition is

$$\frac{\delta \mathcal{L}}{\delta \langle w|} = \Sigma |w\rangle - \lambda |1\rangle \stackrel{!}{=} |0\rangle, \tag{6.35}$$

from which we immediately obtain

$$|w^*\rangle = \lambda \Sigma^{-1} |1\rangle. \tag{6.36}$$

The second first order condition reproduces the normalization constraint

$$\frac{\partial \mathcal{L}}{\partial \lambda} = 1 - \langle 1 | w \rangle \stackrel{!}{=} 0. \tag{6.37}$$

Using this condition with (6.36), one obtains

$$1 = \langle 1 | w^* \rangle = \lambda \langle 1 | \Sigma^{-1} | 1 \rangle. \tag{6.38}$$

Note that ⟨1|Σ −1 |1⟩ is a scalar and we have a solution for λ,

$$\lambda = \frac{1}{\langle 1|\Sigma^{-1}|1\rangle}.\tag{6.39}$$

Putting (6.36) and (6.39) together, the solution to the optimization problem is

$$|w_{\text{MVP}}\rangle = \frac{\Sigma^{-1}|1\rangle}{\langle 1|\Sigma^{-1}|1\rangle}.$$
(6.40)

⟩

Obviously, the *Lagrange*-multiplier is only a normalizing factor, which is perfectly sensible considering the nature of the constraint. Let's look at an example:

## **Example 6.2**

Consider the situation with *N* = 2 securities. What is the vector of portfolio weights|*w* ∗ of the minimum variance portfolio?

#### Solution

For *N* = 2 we have

$$\Sigma = \begin{pmatrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{pmatrix} \quad \Rightarrow \quad \Sigma^{-1} = \frac{1}{\det \Sigma} \begin{pmatrix} \sigma_2^2 & -\rho \sigma_1 \sigma_2 \\ -\rho \sigma_1 \sigma_2 & \sigma_1^2 \end{pmatrix},$$

and further

$$\Sigma^{-1}|1\rangle = \frac{1}{\det \Sigma} \begin{pmatrix} \sigma_2^2 - \rho \sigma_1 \sigma_2 \\ \sigma_1^2 - \rho \sigma_1 \sigma_2 \end{pmatrix} \quad \text{and} \quad \langle 1|\Sigma^{-1}|1\rangle = \frac{1}{\det \Sigma} (\sigma_1^2 + \sigma_2^2 - 2\rho \sigma_1 \sigma_2).$$

We thus obtain the MVP-weights

$$w_1^* = \frac{\sigma_2^2 - \rho \sigma_1 \sigma_2}{\sigma_1^2 + \sigma_2^2 - 2\rho \sigma_1 \sigma_2} \quad \text{and} \quad w_2^* = \frac{\sigma_1^2 - \rho \sigma_1 \sigma_2}{\sigma_1^2 + \sigma_2^2 - 2\rho \sigma_1 \sigma_2},$$

which is exactly our earlier result (6.33). ........................................................................................................................

**Quick calculation 6.10** Show that the variance of the MVP is given by σ 2 MVP = 1 ⟨1|Σ−<sup>1</sup> |1⟩ .

# **6.4 Variance Efficient Portfolios**

A portfolio with expected return µ*<sup>P</sup>* is called variance efficient, if there is no other portfolio with the same expected return, but smaller variance. Note that variance efficient portfolios are not necessarily µ-σ-dominant.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

**Quick calculation 6.11** Can you see why?

To find the weights of an arbitrary variance efficient portfolio, we have to impose an additional constraint. To be a little more precise, we have to minimize the variance under the condition that the expected return is  $\mu_P$  and of course that all weights sum to one. The proper *Lagrange*-function has the form

$$\mathcal{L} = \frac{1}{2} \langle w | \Sigma | w \rangle + \lambda_1 (\mu_P - \langle \mu | w \rangle) + \lambda_2 (1 - \langle 1 | w \rangle). \tag{6.41}$$

From the first order conditions, which are still sufficient, we can extract the required vector of portfolio weights

$$|w^*\rangle = \lambda_1 \Sigma^{-1} |\mu\rangle + \lambda_2 \Sigma^{-1} |1\rangle. \tag{6.42}$$

Quick calculation 6.12 Verify this result by deriving the respective first order condition.

From the constraints, we get another pair of first order conditions that is needed in order to solve for the *Lagrange*-multipliers. The result is a system of two linear equations

$$\langle \mu | w^* \rangle = \mu_p = \lambda_1 \underbrace{\langle \mu | \Sigma^{-1} | \mu \rangle}_{b} + \lambda_2 \underbrace{\langle \mu | \Sigma^{-1} | 1 \rangle}_{c}$$
  
$$\langle 1 | w^* \rangle = 1 = \lambda_1 \underbrace{\langle 1 | \Sigma^{-1} | \mu \rangle}_{b} + \lambda_2 \underbrace{\langle 1 | \Sigma^{-1} | 1 \rangle}_{c},$$
  
(6.43)

which can be written more efficiently as

$$\begin{pmatrix} \mu_P \\ 1 \end{pmatrix} = \begin{pmatrix} a & b \\ b & c \end{pmatrix} \begin{pmatrix} \lambda_1 \\ \lambda_2 \end{pmatrix}.\n$$
(6.44)

Solving this vector equation is not difficult and one obtains the *Lagrange*-multipliers

$$\lambda_1 = \frac{c\mu_P - b}{ac - b^2} \quad \text{and} \quad \lambda_2 = \frac{a - b\mu_P}{ac - b^2}.$$
 (6.45)

**Quick calculation 6.13** Verify this result.

Plugging  $(6.45)$  into  $(6.42)$  yields

$$|w_P\rangle = \Sigma^{-1} \frac{(c\mu_P - b)|\mu\rangle + (a - b\mu_P)|1\rangle}{ac - b^2},\tag{6.46}$$

with

$$a = \langle \mu | \Sigma^{-1} | \mu \rangle, \quad b = \langle \mu | \Sigma^{-1} | 1 \rangle, \quad \text{and} \quad c = \langle 1 | \Sigma^{-1} | 1 \rangle. \tag{6.47}$$

Note one very important point: The expected portfolio return µ*<sup>P</sup>* goes linear into (6.46). That means, if we know two portfolios on the hyperbola of variance efficient portfolios, then we can construct other variance efficient portfolios from them. This fact is summarized in the following theorem:

**Theorem 6.1 (Two-fund separation)** *Let* µ<sup>1</sup> *and* µ<sup>2</sup> *be the expected returns of two variance efficient portfolios with weights* |*w*1⟩ *and* |*w*2⟩. *The portfolio P with expected return* µ*<sup>P</sup>* = λµ<sup>1</sup> + (1 − λ)µ<sup>2</sup> *for* λ ∈ R *is also variance efficient, if its weights are given by*

$$|w_P\rangle = \lambda |w_1\rangle + (1-\lambda)|w_2\rangle.$$

**Quick calculation 6.14** Prove the theorem by plugging µ*<sup>P</sup>* = λµ<sup>1</sup> + (1 − λ)µ<sup>2</sup> into (6.46).

What Theorem 6.1 means is that we do not have to solve a constrained optimization problem for every point on the variance efficient frontier. We only have to do it twice. With two solutions, we can reconstruct the entire curve. And remember, the MVP was already one solution.

In the present problem we know the expected return of the portfolio, because we fixed µ*<sup>P</sup>* in the constraint. But how large is its variance? According to our formula, we must have

$$\sigma_P^2 = \langle w_P | \Sigma | w_P \rangle = \frac{c\mu_P^2 - 2b\mu_P + a}{ac - b^2}.$$
(6.48)

It is an instructive exercise to verify (6.48), but it is not necessarily a quick calculation. However, we can finally see why the variance efficient portfolios are indeed located on a hyperbola. The general equation for a hyperbola in the µ-σ-space is

$$\frac{\sigma^2}{\alpha^2} - \frac{(\mu - \gamma)^2}{\beta^2} = 1. \tag{6.49}$$

Comparing (6.48) and (6.49), we see that we only have to complete the square, rearrange terms, and make the correct identifications for α, β, and γ. Thus, everything we claimed so far regarding sufficiency of first order conditions, was well justified.

# **6.5 Optimal Portfolios and Diversification**

Until now, we have not chosen a particular portfolio maximizing an agent's utility functional of any kind. All we have done is to narrow down the possible candidates. What we have found so far is that an optimal portfolio has to lie on the efficient frontier, which is the upper branch of the hyperbola of variance efficient portfolios. But that is very good news, because the efficient frontier is a concave function of σ and we know that for any risk-averse agent, curves of constant utility have to be convex. This immediately implies that we find our optimal portfolio in the point where one particular

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

![](_page_14_Figure_1.jpeg)

Fig. 6.5 Utility maximizing portfolio for risk-averse agent

utility curve is tangential to the efficient frontier; see Figure 6.5. All we have to do now is to make the *von Neumann–Morgenstern*-utility functional concrete. In MPT, risk is due to the variance of returns. Thus, it is a common assumption that the risk premium is proportional to the variance. Under this assumption the following equality holds

$$E[R] = E[u(R)] + \pi = U[R] + \frac{\alpha}{2} \text{Var}[R], \qquad (6.50)$$

where  $\frac{\alpha}{2}$  is an agent specific constant of proportionality. We have thus in our  $\mu$ - $\sigma$ -world a one parameter family of utility functionals

$$U_{\alpha}[R] = \mu - \frac{\alpha}{2}\sigma^2, \tag{6.51}$$

characterizing the risk aversion of an individual agent by the magnitude of  $\alpha$ . To find an optimal portfolio for an agent with given risk aversion  $\alpha$ , we have to solve the following optimization problem

$$\max_{|w\rangle} U_{\alpha}[R_{P}] \quad \text{subject to} \quad \langle 1|w\rangle = 1. \tag{6.52}$$

That does not look too bad. The first order condition for a maximum with respect to  $\langle w|$  is

$$\frac{\delta \mathcal{L}}{\delta \langle w|} = |\mu\rangle - \alpha \Sigma |w\rangle - \lambda |1\rangle \stackrel{!}{=} |0\rangle, \tag{6.53}$$

from which we obtain

$$|w^*\rangle = \Sigma^{-1} \frac{|\mu\rangle - \lambda |1\rangle}{\alpha}.$$
 (6.54)

Using the normalization constraint, we get an equation for the *Lagrange*-multiplier

$$1 = \langle 1 | w^* \rangle = \frac{b - \lambda c}{\alpha},\tag{6.55}$$

where we adopted the shorthand notation  $b = \langle 1|\Sigma^{-1}|\mu\rangle$  and  $c = \langle 1|\Sigma^{-1}|1\rangle$  from (6.47). Solving for  $\lambda$  yields

$$\lambda = \frac{b - \alpha}{c}.\tag{6.56}$$

Plugging this result into  $(6.54)$  yields the desired weights

$$w_{\alpha}\rangle = \Sigma^{-1}\left(\frac{1}{\alpha}|\mu\rangle + \frac{1}{c}\left(1 - \frac{b}{\alpha}\right)|1\rangle\right),\tag{6.57}$$

with

$$b = \langle 1|\Sigma^{-1}|\mu\rangle \quad \text{and} \quad c = \langle 1|\Sigma^{-1}|1\rangle. \tag{6.58}$$

**Ouick calculation 6.15** Verify Equation (6.57).

Up to this point, we have not discussed the effects of diversification in much detail. In fact, we will not be able to understand it thoroughly, until we can distinguish systematic and idiosyncratic risk. But for the moment we can build some intuition, to understand why every optimal portfolio has to be an optimally diversified portfolio. Let's do some calculations in the simplest possible setup. Assume there are  $N$  securities, each one of them with expected return  $E[R_n] = \mu$  and variance  $\text{Var}[R_n] = \sigma^2$ , and all returns are uncorrelated. In this framework, all securities are located at the same point in the  $\mu$ - $\sigma$ -diagram. You might now argue that in this case it is pointless to build a portfolio, because all securities have identical expected returns and variances. Let's take a somewhat closer look at this argument. All securities have the same  $\mu$  and  $\sigma^2$ , true, but they are not identical. To see what that means, assemble a simple portfolio, where the weights are all the same,  $w_n = \frac{1}{N}$ . This portfolio has expected return

$$E[R_P] = \sum_{n=1}^{N} \frac{1}{N} E[R_n] = \frac{1}{N} \sum_{n=1}^{N} \mu = \mu.$$
 (6.59)

That is not a big surprise. But look what happens to the variance of the portfolio

$$\text{Var}[R_P] = \sum_{n=1}^{N} \frac{1}{N^2} \text{Var}[R_n] = \frac{1}{N^2} \sum_{n=1}^{N} \sigma^2 = \frac{\sigma^2}{N}.$$
 (6.60)

This portfolio clearly dominates every single security, because its standard deviation is reduced by a factor of  $\frac{1}{\sqrt{N}}$ . Now you might argue that if this is correct, then the variance of a portfolio has to tend to zero for large enough  $N$ . Unfortunately, this is not the case, but for the moment the discussion of that issue has to be postponed.

6.6

# **Tobin's Separation Theorem and the Market Portfolio**

In our current framework, every agent with risk aversion  $\alpha$  has her own optimal portfolio with individual composition of securities. This view changed dramatically as Tobin (1958) brought a new player into the game, the risk-free return  $R_0$ . Note, that the riskfree rate of return is not a random variable, at least not for now. The uppercase letter notation is only to keep things consistent and to interpret it as the return of the riskless

![](_page_16_Figure_1.jpeg)

**Fig. 6.6** Capital market line and market portfolio (left) with optimal portfolio (right)

zeroth security *B*0, with *E* [ *R*<sup>0</sup> ] = *r* and Var[ *R*<sup>0</sup> ] = 0. Why does this additional security shake things up that violently? Let's see what Tobin's separation principle claims:

**Theorem 6.2 (Tobin's separation theorem)** *If agents are allowed to borrow or lend at a risk-free rate r*, *then the optimal portfolio for every risk-averse agent is a particular linear combination of the risk-free security B*<sup>0</sup> *and the so-called market portfolio (MP), whereas the composition of the market portfolio is the same for every agent.*

Let's see if we can first understand this graphically. In Figure 6.6 the market portfolio (MP) is indicated as the tangential point of the efficient frontier and a straight line with µ-intercept *r*. This straight line, connecting *r* and MP, is called the capital market line (CML). Why has this to be the right picture? Remember that the curves of constant utility are convex. Therefore, the steeper the slope of the capital market line, the higher the utility level an agent can achieve. But the capital market line has to intersect the efficient frontier at least at one point, to provide a linear combination with a variance efficient portfolio. The only possible conclusion is that the capital market line has to be tangent to the efficient frontier. Because of this, the market portfolio is also called the tangential portfolio. It is now also obvious, why every agent bases her investment decision on the same portfolio, because the market portfolio is the only remaining efficient portfolio of risky assets. All other variance efficient portfolios are dominated by portfolios on the capital market line. The agent's individual risk aversion merely determines the mixing point on that line.

Having straightened things out, it is time to compute the weights of the market portfolio. This is a surprisingly simple task, not at all requiring constrained optimization. The key observation is that the market portfolio weights do not change relative to one another, because the composition of the market portfolio stays the same for all agents. Let's proceed in two steps. First, locate an arbitrary portfolio on the capital market line, and second, shift this portfolio by setting the weight *w*<sup>0</sup> of the risk-free bond *B*<sup>0</sup> to zero. First things first. Because we are looking for an arbitrary portfolio on the capital market line, we can choose an arbitrary risk aversion parameter α. So let's choose α = 1 for convenience. The corresponding utility functional is

$$U_1[R_P] = w_0 r + \langle \mu | w \rangle - \frac{1}{2} \langle w | \Sigma | w \rangle. \tag{6.61}$$

The clever trick is now to circumvent the normalization constraint by realizing that

$$w_0 = 1 - \langle 1 | w \rangle \tag{6.62}$$

has to hold. Using this relation, the normalization is built into the optimization problem just as in the case of two securities, where we have used *w* and 1 − *w* for the weights. One obtains the first order condition

$$\frac{\delta U_1}{\delta \langle w|} = -r|1\rangle + |\mu\rangle - \Sigma|w\rangle \stackrel{!}{=} |0\rangle,\tag{6.63}$$

which is solved by

$$|w^*\rangle = \Sigma^{-1}(|\mu\rangle - r|1\rangle). \tag{6.64}$$

Here comes the second step. For *w*<sup>0</sup> = 0 it follows from (6.62) that ⟨1|*w* ∗ ⟩ = 1 has to hold. But the weights are unchanged relative to one another, they are merely scaled. Thus, the market portfolio weights have to be given by

$$|w_{\text{MP}}\rangle = \frac{\Sigma^{-1}(|\mu\rangle - r|1\rangle)}{\langle 1|\Sigma^{-1}(|\mu\rangle - r|1\rangle)}.$$
(6.65)

We are not finished yet. Now that we know the location of the market portfolio on the efficient frontier, we can compute the agent's optimal portfolio. Tobin's separation theorem states that the desired portfolio is a linear combination of *B*<sup>0</sup> and the market portfolio. Thus, the portfolio return has to be

$$R_P = (1 - \lambda)R_0 + \lambda R_{\rm MP},\tag{6.66}$$

for λ ≥ 0. It is an easy exercise to compute the expected return of this portfolio,

$$\mu_P = (1 - \lambda)r + \lambda\mu_{\text{MP}}.\tag{6.67}$$

As for the variance, recall that Cov[*X*, *Y*] = ρ*XY*σ*X*σ*<sup>Y</sup>* and Var[ *R*<sup>0</sup> ] = 0. The calculation is then straightforward,

$$\sigma_P^2 = (1 - \lambda)^2 \sigma_0^2 + 2(1 - \lambda)\lambda \rho_{0,\text{MP}} \sigma_0 \sigma_{\text{MP}} + \lambda^2 \sigma_{\text{MP}}^2 = \lambda^2 \sigma_{\text{MP}}^2.$$
(6.68)

Now using the simplified *von Neumann–Morgenstern*-utility functional

$$U_{\alpha}[R_P] = (1 - \lambda)r + \lambda\mu_{\rm MP} - \frac{\alpha}{2}\lambda^2\sigma_{\rm MP}^2, \tag{6.69}$$

the unconstrained maximization is with respect to λ only.

**Quick calculation 6.16** Write the first order condition for this problem.

Using our standard optimization routine one obtains the solution

$$\lambda_{\alpha} = \frac{1}{\alpha} \frac{\mu_{\text{MP}} - r}{\sigma_{\text{MP}}^2}.$$
(6.70)

Equation (6.70) makes perfect sense. The larger the risk aversion  $\alpha$ , the smaller the proportion of the market portfolio the agent is willing to hold. The same is true for the variance  $\sigma_{\rm MD}^2$ , which is a measure for the risk involved. If the excess return  $\mu_{\rm MP} - r$ grows larger, the agent is willing to hold a larger proportion of the market portfolio.

There is an extra bonus that goes along with the calculation of the market portfolio. Since it is very easy to compute the minimum variance portfolio, we can give a parametrized version of the efficient frontier in terms of the respective portfolio weights

$$\begin{split} |w_{\gamma}\rangle &= (1-\gamma)|w_{\text{MVP}}\rangle + \gamma|w_{\text{MP}}\rangle \\ &= \Sigma^{-1} \left( (1-\gamma)\frac{|1\rangle}{c} + \gamma\frac{|\mu\rangle - r|1\rangle}{b - rc} \right), \end{split} \tag{6.71}$$

for  $\gamma \geq 0$ , with

 $b = \langle 1 | \Sigma^{-1} | \mu \rangle$  and  $c = \langle 1 | \Sigma^{-1} | 1 \rangle$ .  $(6.72)$ 

In deriving this result, the two-fund separation theorem on page 113 was used.

Tobin's separation theorem provides a mechanism to decouple the portfolio selection problem from the investment decision problem. The market portfolio is always the same for every agent. Only the proportions held in the risky portfolio and the risk-free security differ between agents. This makes life a lot easier for financial advisors. They do not have to assemble individual portfolios for all their clients, but can rely on only one market portfolio. Usually a proxy, like the S&P 500 for example, is used instead of a genuine market portfolio, because such a portfolio would have to incorporate all assets, even non tradable ones, which is of course impossible.

# **Further Reading**

6.7

A very instructive source is the classical book by Markowitz (1959), and also the original work of Tobin (1958). A non-technical introduction is Estrada (2005). A concise review is provided in Hens and Rieger (2010, chap. 3). For a compressed technical treatment see Janssen et al. (2009, chap. 17). A detailed and carefully written exposition of the whole subject is Elton et al.  $(2010)$ . For the impact of real market imperfections, like short-selling restrictions for example, see Kan and Smith (2008). A very refreshing discussion of the scientific legacy of modern portfolio theory is Fabozzi et al. (2002).

# **6.8 Problems**

**6.1** Think of a world without the opportunity of risk-free borrowing or lending. You can only hold money, which means saving is permitted, or invest in a portfolio of risky assets. Show that in this world the market portfolio is given by

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$|w_{\mathrm{MP}}\rangle = \frac{\Sigma^{-1}|\mu\rangle}{\langle 1|\Sigma^{-1}|\mu\rangle}$$

.

- **6.2** Which expected return would an agent in the world of Problem 6.1 require to hold the market portfolio, if her risk aversion is α = 1?
- **6.3** Assume there are different risk-free rates for borrowing and lending, and *R b* 0 > *R l* 0 . Sketch the capital market curve graphically and explain what happens to the tangential portfolio.
- **6.4** For a random variable *X* ∼ *N*(µ, σ<sup>2</sup> ), the probability of realizing a value *x* outside the range µ ± 2σ is roughly 5%. What proportion of the market portfolio should an agent hold, if she is willing to accept a nominal loss with no more than 2.5% probability? Assume that there is a riskless security and the risk-free rate of return is *r*.
- **6.5** Assume there are two security funds, one based on corporate bonds *B*, and the other on stocks *S*, with µ*<sup>B</sup>* < µ*S*, σ*<sup>B</sup>* < σ*S*, and ρ*BS* = 0. Construct a market portfolio out of these two funds, assuming a risk-free rate of return *r*, and compute the weights *w* ∗ *B* and *w* ∗ *S* .
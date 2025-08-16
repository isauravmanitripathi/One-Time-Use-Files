# **Accumulated Claims**

For measuring operational risk (see Operational Risk) or the risk of an insurance contract or an insurance portfolio, one has to find "good" models for the losses of the contract. These models need to be simple in order to be able to get desired answers but complicated enough to reflect the "real" situation. To achieve this goal, there are two different approaches: one approach is to model the number of claims and the individual claim sizes and the other is to model the distribution of the accumulated claim sizes directly. We consider the first approach in the second section and the second approach in the third section. In the fourth section, we discuss numerical methods to calculate the distribution function.

#### **Compound Models**

The most natural way to model the accumulated claims distribution is the distribution of a random sum

$$S = \sum_{k=1}^{N} Y_k \tag{1}$$

where  $N \in \{0, 1, \ldots\}$  is the (random) number of claims and  $Y_k$  is the (random) size of the kth claim. Here, we make the convention  $\sum_{k=1}^{0} Y_k = 0$ . In a portfolio where claims do not occur simultaneously, one can assume that N and  $\{Y_k\}$  are independent and that  $\{Y_k\}$  are independent and identically distributed (i.i.d.). If claims occur simultaneously—as, for instance, claims caused by natural catastrophes—one has to consider  $Y_k$  as the accumulated claim from an event. The distribution of  $S$  is then called a *compound distribution* (see **Ruin Theory**; Insurance Risk Models).

One often needs some characteristics of the distribution of S. By conditioning on  $N$ , one finds

$$\mathbb{E}[S] = \mathbb{E}[N]\mathbb{E}[Y] \tag{2}$$

$$Var[S] = Var[N]E[Y]^{2} + Var[Y]E[N]$$
(3)

$$\mathbb{E}[\mathbf{e}^{rS}] = \mathbb{E}[\exp\{N \log \mathbb{E}[\mathbf{e}^{rY}]\}] \tag{4}$$

We see that the characteristics can be easily calculated from the corresponding quantities for  $N$  and  $Y$ .

Let  $p_k = \mathbb{P}[N = k]$ . Popular models for N are the binomial distribution  $p_k = \binom{n}{k} q^k (1-q)^{n-k}$ ,  $n \in \mathbb{N}, q \in (0, 1)$ ; the Poisson distribution  $p_k = e^{-\lambda} \lambda^k / k!$ ,  $\lambda > 0$ ; the negative binomial distribution  $p_k = \binom{\alpha + k - 1}{k} q^{\alpha} (1 - q)^k, \ \alpha > 0, \ q \in (0, 1);$ and the logistic distribution  $p_k = -q^{n+1}/[(n+1)]$  $\log(1-q)$ ,  $q \in (0, 1)$ .

The Poisson distribution appears as a limit. Suppose that there are  $m$  independent individual contracts where a claim occurs with probability  $q^{(j)}$ . The average number of claims is approximately  $\lambda =$  $\sum_{j=1}^{m} q^{(j)}$ . If now  $m \to \infty$  such that  $\lambda$  remains constant and  $\sum_{j=1}^{m} (q^{(j)})^2 \rightarrow 0$ , then the number of claims converges to a Poisson distribution with parameter  $\lambda$ .

The compound Poisson model has a few more nice properties. Suppose that there are *m* portfolios  $S^{(j)}$ modeled as compound Poisson with parameter  $\lambda^{(j)}$ and the distribution  $G^{(j)}(y)$  of the increments. Then  $S = \sum_{i=1}^{m} S^{(i)}$  has a compound Poisson distribution with parameter  $\lambda = \sum_{j=1}^{m} \lambda^{(j)}$  and distribution of the increments

$$G(y) = \sum_{j=1}^{m} \lambda^{-1} \lambda^{(j)} G^{(j)}(y) \tag{5}$$

Conversely, if  $S$  has a compound Poisson distribution and  $B^{(j)}$  are sets such that  $B^{(i)} \cap B^{(j)} = \emptyset$  for  $i \neq j$ *j*, then  $S^{(j)} = \sum_{k=1}^{N} Y_k \mathbb{I}_{Y_k \in B^{(j)}}$  are independent and compound Poisson distributed with parameter  $\lambda^{(j)} =$  $\lambda \mathbb{P}[Y \in B^{(j)}]$  and  $Y_k^{(j)}$  has the distribution  $\mathbb{P}[Y \in \cdot \mid$  $Y \in B^{(j)}$ 

Easy treatable models are also mixed Poisson models, where  $\Lambda > 0$  is a random variable, and N conditioned on  $\Lambda$  has a Poisson distribution with parameter  $\Lambda$ . One finds that

$$\mathbb{E}[N] = \mathbb{E}[\Lambda] \tag{6}$$

$$Var[N] = Var[\Lambda] + \mathbb{E}[\Lambda] \tag{7}$$

$$\mathbb{E}[\mathbf{e}^{rN}] = \mathbb{E}[\exp{\Lambda(\mathbf{e}^r - 1)}] \tag{8}$$

For example, if  $\Lambda$  follows a gamma distribution, which means that  $\Lambda$  has the density  $\beta^{\gamma} x^{\gamma-1} e^{-\beta x} \mathbb{I}_{x>0} / \Gamma(\gamma)$ , then N has a negative binomial distribution with  $\alpha = \gamma$  and  $q = \beta/(\beta + 1)$ .

![](_page_1_Figure_1.jpeg)

**Figure 1** Densities of  $S$  (solid line), its normal approximation (dotted line), and its translated gamma approximation (dashed line)

Further risk models and details can be found in  $[1, 3, 4, 7, 9]$ . Applications to operational risk are described in  $[2, 5, 6]$ .

#### Approximations

The calculation of the distribution of a compound sum is in general not possible. It involves  $n$ -fold convolutions, that is,  $n$ -fold integrals, which numerically is a problem. One, therefore, has to use approximations to the aggregate claims distribution. Let us denote by  $\mu_k = \mathbb{E}[S^k]$  the moments of S, by  $\sigma^2 =$  $\mu_2 - \mu_1^2$  the variance, and by  $\beta = \mathbb{E}[(S - \mu)^3] \sigma^{-3/2}$ the coefficient of skewness.

The *normal approximation* is the normal distribution with the same mean and variance as  $S$ . This approximation usually does not fit well because it does not take care of the skewness.

An approximation that usually works well is the translated gamma approximation. Let  $\gamma = 4\beta^{-2}$ ,  $\alpha =$  $2/(\beta\sigma)$ , and  $k = \mu - \gamma/\alpha$ . Let Z be a gammadistributed random variable with parameters  $\nu$  and  $\alpha$ . Then  $Z + k$  has the same first three moments as S. That three moments are matched is also a reason for the good fit.

As an example we consider a compound Poisson distribution with  $\lambda = 20$  and Pareto-distributed claim sizes with mean 1 and variance 2, that is,

 $\mathbb{P}[Y > y] = (3/(3 + y))^4$ . Figure 1 shows the densities of the exact distribution and its normal and translated gamma approximations. Both approximations do not fit well close to the mean value 20, but for risk management this region is not very interesting. We can see that in the right tail the normal approximation underestimates the true density considerably, whereas the fit in the tail of the translated gamma approximation is quite good.

Further possibilities for approximations are Edgeworth expansions, saddle point approximations, or the normal power approximation,  $[3, 4, 7, 9]$ .

### **Panjer Recursion**

Suppose that  $Y_i > 0$  takes values in N. Then also S takes values in  $\mathbb{N}$ . If we denote by  $f_k =$  $\mathbb{P}[Y=k]$  and  $f_k^{*n} = \mathbb{P}[Y_1 + \cdots + Y_n = k]$ , then  $g_k = \mathbb{P}[S = k]$  can be calculated by  $g_0 = p_0$  and  $g_n = \sum_{k=1}^n p_k f_n^{*k}$ . The convolutions are obtained recursively:  $f_k^{*(n+1)} = \sum_{\ell=1}^{k-1} f_\ell^{*n} f_{k-\ell}$ , where  $f_\ell^{*1} = f_\ell$ . The problem is that numerous calculations have to be executed, which makes the procedure slow.

A faster procedure can be found if for  $r \ge 1$ 

$$p_r = \left(a + \frac{b}{r}\right) p_{r-1} \tag{9}$$

for some constants *a, b*. It turns out that the distribution of *N* must be binomial (*a <* 0, −*b/a* ∈ ), Poisson (*a* = 0, *b >* 0), or negative binomial (*a* ∈ *(*0*,* 1*)*, *a* + *b >* 0). In these cases, we have *g*<sup>0</sup> = *p*<sup>0</sup> and recursively

$$g_r = \sum_{k=1}^r \left( a + \frac{bk}{r} \right) f_k g_{r-k} \tag{10}$$

The method is fast and is also stable for the compound Poisson and the compound negative binomial distributions. This method goes back to Panjer [8].

Generalizations of formula (10) are treated for the case where *f*<sup>0</sup> *>* 0 or the case where the recursion (9) holds for *r* ≥  *>* 1 [4, 10–12].

# **References**

- [1] Asmussen, S. (2000). *Ruin Probabilities*, World Scientific, Singapore.
- [2] Cruz, M.G. (2002). *Modeling, Measuring and Hedging Operational Risk*, Wiley, New York.
- [3] Daykin, C.D., Pentikainen, T. & Pesonen, M. (1994). ¨ *Practical Risk Theory for Actuaries*, Chapman & Hall, London.
- [4] Dickson, D.C.M. (2005). *Insurance Risk and Ruin*, Cambridge University Press, Cambridge.
- [5] Embrechts, P., Kaufmann, R. & Samorodnitsky, G. (2004). Ruin theory revisited, stochastic models for operational risk, in *Risk Management for Central Bank Foreign Reserves*, C. Bernadell, P. Cardon, J. Coche,

F.X. Diebold, S. Manganelli, eds, European Central Bank, Frankfurt A.M., pp. 243–261.

- [6] Frachot, A., Moudoulaud, O. & Roncalli, T. (2004). Loss distribution approach in practice, in M. Ong, ed., *The Basel Handbook: A Guide for Financial Practitioners*, Risk Books, London.
- [7] Gerber, H.U. (1979). *An Introduction to Mathematical Risk Theory*, Huebner Foundation Monographs, Philadelphia.
- [8] Panjer, H.H. (1981). Recursive evaluation of a family of compound distributions, *ASTIN Bulletin* **12**, 22–26.
- [9] Rolski, T., Schmidli, H., Schmidt, V. & Teugels, J.L. (1999). *Stochastic Processes for Insurance and Finance*, Wiley, Chichester.
- [10] Schroter, K.J. (1991). On a family of counting distribu- ¨ tions and recursions for related compound distributions, *Scandinavian Actuarial Journal* 161–175.
- [11] Sundt, B. (1992). On some extensions of Panjer's class of counting distributions, *ASTIN Bulletin* **22**, 61–80.
- [12] Sundt, B. & Jewell, W.S. (1981). Further results on recursive evaluation of compound distributions, *ASTIN Bulletin* **12**, 27–39.

# **Related Articles**

**Cramer–Lundberg Estimates ´** ; **Heavy Tails in Insurance**; **Insurance Risk Models**; **Operational Risk**; **Poisson Process**; **Ruin Theory**.

HANSPETER SCHMIDLI
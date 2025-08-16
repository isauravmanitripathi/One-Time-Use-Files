## Cramér's Theorem

Let  $X, X_1, X_2, \ldots$  be independent and identically distributed (i.i.d.) random variables with partial sums  $S_n = \sum_{k=1}^n X_k$  and empirical means  $\hat{S}_n = n^{-1} S_n$  for  $n = 1, 2, \dots$  Assuming a finite mean  $\mu = E[X]$ , by the law of large numbers, it holds for every  $x > \mu$ that

$$\lim_{n \to \infty} P\left(\hat{S}_n > x\right) = 0\tag{1}$$

Cramér's theorem refines this result by identifying an exact exponential decay rate of the small probability in equation (1). Note that the central limit theorem cannot, in general, capture this subtle decay rate because the central limit theorem focuses on averagesized fluctuations while the rare event  $(\hat{S}_n > x)$  is mainly determined by large values of the random variables  $X_1, \ldots, X_n$ .

Study of the probability of such a rare event has important applications in insurance and finance. For example, in insurance context, we may understand the random variables  $X_1, \ldots, X_n$  as respective claim amounts of  $n$  policy holders during a time period or of a single policy holder during  $n$ time periods. The event  $(\hat{S}_n > x)$  with  $x \ge \mu + \delta$ , where  $\delta > 0$  is interpreted as the safety loading, describes a critical situation that the insurance company loses money. To make sure that the probability of this rare event is sufficiently small, we need to determine what value of  $\delta$  is appropriate. A good approximation for the probability  $P(\hat{S}_n > x)$ enables us to get a simple yet powerful solution to this problem.

Let us take another example from financial risk management. Denote by  $Q_{\alpha}[S_n]$  and  $CTE_{\alpha}[S_n]$ , respectively, the quantile (value at risk) and conditional tail expectation of the sum  $S_n$  of  $n$  risk variables, where  $\alpha \in (0, 1)$  represents the confidence level, usually chosen to be close to 1 (see Value-at-Risk and Expected Shortfall). By definition,

$$Q_{\alpha} [S_n] = \inf \{ y : P(S_n > y) \le 1 - \alpha \} \tag{2}$$

and

$$\text{CTE}_{\alpha} \left[ S_n \right] = E \left[ S_n | S_n > Q_{\alpha} \left[ S_n \right] \right]$$
$$= Q_{\alpha} \left[ S_n \right] + \frac{\int_{Q_{\alpha} \left[ S_n \right]}^{\infty} P \left( S_n > y \right) \mathrm{d}y}{P \left( S_n > Q_{\alpha} \left[ S_n \right] \right)} \tag{3}$$

Hence, an efficient approximation for the probability in equation (1) is desired for calculation of both  $Q_{\alpha} [S_n]$  and  $CTE_{\alpha} [S_n]$ .

Define the cumulant generating function of  $X$  as

$$\Lambda(\lambda) = \ln E\left[e^{\lambda X}\right], \qquad \lambda \in \mathbb{R} \tag{4}$$

Note that  $\Lambda(0) = 0$  and  $-\infty < \Lambda(\lambda) < \infty$  for all  $\lambda \in \mathbb{R}.$  Further define the Fenchel–Legendre transform of  $\Lambda(\cdot)$  as

$$\Lambda^*(x) = \sup_{\lambda \in \mathbb{R}} \left\{ \lambda x - \Lambda(\lambda) \right\}, \qquad x \in \mathbb{R} \tag{5}$$

It can be shown that both  $\Lambda(\cdot)$  and  $\Lambda^*(\cdot)$  are convex (but not necessarily strictly convex) functions on  $\mathbb{R}$  and that  $\Lambda^*(\cdot)$  is lower semicontinuous (i.e.,  $\Lambda^*(\cdot)$  takes values in  $[0,\infty]$  and is such that, for every  $y \in [0, \infty)$ , the level set  $\{x : \Lambda^*(x) \le y\}$  is closed).

The following are some concrete and easily verifiable examples for  $\Lambda^*(\cdot)$  (see, e.g., page 35 of [3]):

- 1. If  $X$  follows a Poisson distribution with mean  $\theta > 0$  then  $\Lambda^*(x) = \theta - x + x \ln \frac{x}{\theta}$  for  $x \ge 0$ and  $\Lambda^*(x) = \infty$  otherwise.
- 2. If  $X$  follows a Bernoulli distribution with success probability  $p \in (0, 1)$  then  $\Lambda^*(x) = x \ln \frac{x}{p} +$  $(1-x)\ln\frac{1-x}{1-p} \text{ for } x \in [0,1] \text{ and } \Lambda^*(x) = \infty$ otherwise.
- 3. If  $X$  follows an exponential distribution with mean  $1/\theta$  then  $\Lambda^*(x) = \theta x - 1 - \ln(\theta x)$  for  $x > 0$  and  $\Lambda^*(x) = \infty$  otherwise.
- 4. If X follows a normal distribution with mean  $\mu$ and variance  $\sigma^2$  then  $\Lambda^*(x) = \frac{(x-\mu)^2}{2\sigma^2}$ .

For a Borel set  $\Gamma$ , denote by  $\Gamma$  and  $\overline{\Gamma}$  its interior and closure, respectively. Throughout, inf  $\oslash = \infty$ , by convention.

Cramér's Theorem For every Borel set  $\Gamma$  with nonempty interior.

$$\begin{split} -\inf_{x \in \dot{\Gamma}} \Lambda^*(x) &\leq \liminf_{n \to \infty} \frac{1}{n} \ln P\left(\hat{S}_n \in \Gamma\right) \\ &\leq \limsup_{n \to \infty} \frac{1}{n} \ln P\left(\hat{S}_n \in \Gamma\right) \\ &\leq -\inf_{x \in \bar{\Gamma}} \Lambda^*(x) \end{split} \tag{6}$$

A sequence of probability measures,  $\{P_n\}$ , is said to satisfy the large deviation principle (see Large **Deviations**) with a rate function  $I(\cdot)$  if, for every Borel set  $\Gamma$ .

$$-\inf_{x\in\dot{\Gamma}}I(x) \leq \liminf_{n\to\infty}\frac{1}{n}\ln P_n\left(\Gamma\right)$$
  
$$\leq \limsup_{n\to\infty}\frac{1}{n}\ln P_n\left(\Gamma\right) \leq -\inf_{x\in\bar{\Gamma}}I(x)$$
  
(7)

Thus, Cramér's theorem shows that the probability laws of the empirical means  $\hat{S}_n$  satisfy the large deviation principle with rate function  $\Lambda^*(\cdot)$  (see Large Deviations).

Note that Cramér's theorem does not require  $\Lambda(\lambda) < \infty$  for all  $\lambda \in \mathbb{R}$ . It is applicable even when the mean of X does not exist. For  $\mu \in \Gamma$ , Cramér's theorem does not contribute because both sides of equation (6) turn out to be zero. If  $\inf_{x \in \mathring{\Gamma}} \Lambda^*(x) =$  $\inf_{x\in\bar{\Gamma}} \Lambda^*(x)$ , as is often the case in applications, then

$$\lim_{n \to \infty} \frac{1}{n} \ln P\left(\hat{S}_n \in \Gamma\right) = -\inf_{x \in \Gamma} \Lambda^*(x) \qquad (8)$$

or, equivalently,

$$P\left(\hat{S}_n \in \Gamma\right) = \exp\left\{-n\left(\inf_{x \in \Gamma} \Lambda^*(x) + o(1)\right)\right\} \tag{9}$$

where  $o(1)$  tends to 0 as  $n \to \infty$ . It can be shown that, for every real number  $y$ ,

$$\lim_{n \to \infty} \frac{1}{n} \ln P\left(\hat{S}_n \ge y\right) = -\inf_{x \ge y} \Lambda^*(x) \tag{10}$$

see, for example, Corollary 2.2.19 of [3].

The first statement of Cramér's theorem for distributions possessing densities was given by Cramér [2], who applied it to model the insurance business (see Cramér-Lundberg Estimates). This is the first rigorous result concerning large deviations and is viewed as the historical starting point of large deviation theory. An extension to general distributions was done by Chernoff [1]. Cramér's theorem is also often cited as the Cramér-Chernoff theorem in the literature of large deviation theory.

Various versions of Cramér's theorem have been included in many monographs in large deviation theory. This most general version of Cramér's theorem is due to [3]. Textbook treatments of Cramér's theorem can be found in  $[6, 16]$ , and  $[10]$ , among others.

A similar result for the empirical means of i.i.d. random vectors in  $\mathbb{R}^d$  has been established. A further extension to dependent, not necessarily identically distributed, random vectors in  $\mathbb{R}^d$  leads to the Gärtner-Ellis theorem.

## Large Deviations Without Cramér's Condition

Note that if  $\Lambda(\lambda) = \infty$  for all  $\lambda \neq 0$ , then  $\Lambda^*(x) = 0$ for all  $x \in \mathbb{R}$  and consequently equation (7) gives a trivial approximation

$$\lim_{n \to \infty} \frac{1}{n} \ln P\left(\hat{S}_n \in \Gamma\right) = 0 \tag{11}$$

Similarly, if  $\Lambda(\lambda) = \infty$  for all  $\lambda > 0$ , then  $\Lambda^*(x) = 0$ for all  $x > \mu$  and, in this case, Cramér's theorem leads to equation (11) with  $\Gamma = [\mu, \infty)$ , while if  $\Lambda(\lambda) = \infty$  for all  $\lambda < 0$  then  $\Lambda^*(x) = 0$  for all  $x < 0$  $\mu$  and in this case Cramér's theorem leads to equation (11) with  $\Gamma = (-\infty, \mu]$ . To avoid such trivialities, it is necessary to assume  $\Lambda(\lambda) < \infty$  in a neighborhood of  $\lambda = 0$ , which is usually referred to as *Cramér's* condition.

Study of large deviations for heavy-tailed random variables for which Cramér's condition is violated forms another important part of large deviation theory. The concept of subexponentiality plays a central role during the study in this direction. By definition, the common distribution of i.i.d. random variables  $X$ ,  $X_1, X_2, \ldots$  is said to be subexponential (on the right)

if the relation

$$\lim_{x \to \infty} \frac{P\left(\sum_{k=1}^{n} X_{k}^{+} > x\right)}{P\left(X^{+} > x\right)} = n \tag{12}$$

holds for some (or, equivalently, for all)  $n = 2, 3, \ldots$ where  $X^+ = \max\{X, 0\}$  (see Heavy Tails in Insurance). We remark that many popular distributions such as Pareto, lognormal, and heavy-tailed Weibull distributions are subexponential; see, for example, [5]. The very definition of subexponentiality opens a natural way to establish

$$\lim_{n \to \infty} \sup_{x \ge x_n} \left| \frac{P(S_n > x)}{nP(X > x)} - 1 \right| = 0 \tag{13}$$

for appropriate constants  $x_n$  serving as a threshold. The uniform asymptotic relation  $(13)$  is at the core of the mainstream study of large deviations in the presence of heavy tails. We usually say that results like equation  $(13)$  give precise asymptotics for large deviations while results like equations  $(6)$  and  $(10)$ give rough asymptotics for large deviations.

Pioneering works in the study of precise large deviations include  $[12, 13]$  and  $[7-9]$ . Overviews are available in [14] and [11], the latter of which contains a table summarizing choices of the threshold sequence  $\{x_n\}$  in equation (13) for most subexponential distributions. Some recent developments of precise large deviations can be found in  $[15]$  and  $[4]$ , among others.

## References

- [1] Chernoff, H. (1952). A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations, Annals of Mathematical Statistics 23, 493-507.
- [2] Cramér, H. (1938). Sur un nouveau théorème-limite de la théorie des probabilités, Actualités Scientifiques et Industrielles. 736, 5-23.

- Dembo, A. & Zeitouni, O. (1998). Large Deviations [3] Techniques and Applications, 2nd Edition, Springer-Verlag, New York.
- Denisov, D., Dieker, A.B. & Shneer, V. (2008). Large [4] deviations for random walks under subexponentiality: the big-jump domain, The Annals of Probability 36, 1946-1991
- [5] Embrechts, P., Klüppelberg, C. & Mikosch, T. (1997). Modelling Extremal Events for Insurance and Finance, Springer-Verlag, Berlin.
- Gulinsky, O.V. & Veretennikov, A.Y. (1993). Large [6] Deviations for Discrete-time Processes with Averaging, VSP, Utrecht.
- [7] Heyde, C.C. (1967). A contribution to the theory of large deviations for sums of independent random variables. Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 7, 303-308.
- Heyde, C.C. (1967). On large deviation problems for [8] sums of random variables which are not attracted to the normal law, Annals of Mathematical Statistics 38, 1575-1578.
- Heyde, C.C. (1968). On large deviation probabilities [9] in the case of attraction to a non-normal stable law, Sankhyā Series A 30, 253-258.
- [10] Klenke, A. (2008). *Probability Theory—A Comprehen*sive Course, Springer-Verlag London, Ltd., London.
- [11] Mikosch, T. & Nagaev, A.V. (1998). Large deviations of heavy-tailed sums with applications in insurance, Extremes 1, 81-110.
- [12] Nagaev, A.V. (1969). Integral limit theorems with regard to large deviations when Cramér's condition is not satisfied, *Theory of Probability and its Applications* **14**,  $51 - 64.$
- [13] Nagaev, A.V. (1969). Integral limit theorems with regard to large deviations when Cramér's condition is not satisfied, Theory of Probability and its Applications 14, 193-208.
- $[14]$ Nagaev, S.V. (1979). Large deviations of sums of independent random variables, Annals of Probability 7,  $745 - 789$
- [15] Tang, Q. (2006). Insensitivity to negative dependence of the asymptotic behavior of precise large deviations, Electronic Journal of Probability 11, 107-120.
- [16] Varadhan, S.R.S. (1984). Large Deviations and Applications, SIAM, Philadelphia, PA.

**QIHE TANG**
# **Wiener–Hopf Decomposition**

A fundamental part of the theory of random walks and Levy processes is a set of conclusions, which, ´ in modern times, are loosely referred to as *the Wiener–Hopf factorization*. Historically, the identities around which the Wiener–Hopf factorization is centered are the culmination of a number of works that include [2–4, 6–8, 14–17], and many others; although the analytical roots of the so-called Wiener–Hopf method go much further back than these probabilistic references; see, for example, [9, 13]. The importance of the Wiener–Hopf factorization for either a random walk or a Levy process is that ´ it characterizes the range of the running maximum of the process as well as the times at which new maxima are attained. We deal with the Wiener–Hopf factorization for random walks before moving to the case of Levy processes. The discussion very closely follows ´ the ideas of [6, 7]. Indeed, for the case of random walks, we shall not deter from providing proofs as their penetrating and yet elementary nature reveals a simple path decomposition that is arguably more fundamental than the Wiener–Hopf factorization itself. The Wiener–Hopf factorization for Levy processes is ´ essentially a technical variant of the case for random walks and we only state it without proof.

# **Random Walks and Infinite Divisibility**

Suppose that {*ξi* : *i* = 1*,* 2*,...*} are a sequence of valued independent and identically distributed (i.i.d.) random variables defined on the common probability space *(-,* F*, -)* with common distribution function *F*. Let

$$S_0 = 0 \text{ and } S_n = \sum_{i=1}^n \xi_i$$
 (1)

The process *S* = {*Sn* : *n* ≥ 0} is called a (*real valued*) random walk. For convenience, we make a number of assumptions on *F*. First,

$$\min\{F(0,\infty), F(-\infty,0)\} > 0 \tag{2}$$

meaning that the random walk may experience both positive and negative jumps, and second, *F* has no atoms. In the prevailing analysis, we repeatedly refer to general and specific classes of infinitely divisible random variables (*see* **Infinite Divisibility**). An *<sup>d</sup>* valued random variable *X* is infinitely divisible if for each *n* = 1*,* 2*,* 3*,...*

$$X \stackrel{d}{=} X_{(1,n)} + \dots + X_{(n,n)} \tag{3}$$

where {*X(i,n)* : *i* = 1*,...,n*} are i.i.d. distributed and the equality is in the distribution. In other words, if *µ* is the characteristic function of *X*, then for each *n* = 1*,* 2*,* 3*,...* we have *µ* = *(µn)n*, where *µn* is the the characteristic function of some *<sup>d</sup>* -valued random variable.

In general, if *X* is any *<sup>d</sup>* -valued random variable that is also infinitely divisible, then for each *θ* ∈ *<sup>d</sup>* , *E(*e*iθ*·*X)* = e<sup>−</sup>*(θ )* where

$$\Psi(\theta) = ia \cdot \theta + \frac{1}{2} \mathcal{Q}(\theta) \n+ \int_{\mathbb{R}^d} \left( 1 - e^{i\theta \cdot x} + i\theta \cdot x \mathbf{1}_{(|x| < 1)} \right) \Pi(\mathrm{d}x) \tag{4}$$

where *a* ∈ *<sup>d</sup>* , *Q* is a positive semidefinite quadratic form on *<sup>d</sup>* and is a measure supported in *<sup>d</sup>* \{0} such that

$$\int_{\mathbb{R}^d} 1 \wedge |x|^2 \Pi(\mathrm{d}x) < \infty \tag{5}$$

Here, |·| is Euclidean distance and, for *a, b* ∈ *<sup>d</sup>* , *a* · *b* is the usual Euclidean inner product.

A special example of an infinitely divisible distribution is the geometric distribution. The symbol *<sup>p</sup>* always denotes a geometric distribution with parameter *p* ∈ *(*0*,* 1*)* defined on *(-,* F*, -)*. In particular,

$$P(\Gamma_p = k) = pq^k, \quad k = 0, 1, 2, \dots$$
 (6)

where *q* = 1 − *p*. The geometric distribution has the following properties that are worth recalling for the forthcoming discussion. First,

$$P(\Gamma_p \ge k) = q^k \tag{7}$$

and, second, the lack-of-memory property:

$$P(\Gamma_p \ge n + m | \Gamma_p \ge m) = P(\Gamma_p \ge n),$$
  
$$n, m = 0, 1, 2, \dots$$
 (8)

A more general class of infinitely divisible distributions than the latter, which will shortly be of use, are those that may be expressed as the distribution of a random walk sampled at an independent and geometrically distributed time;  $S_{\Gamma_p} = \sum_{i=1}^{\Gamma_p} \xi_i$ . (Note, we interpret  $\sum_{i=1}^{0}$  as the empty sum). To justify the previous claim, a straightforward computation shows that for each  $n = 1, 2, 3, \ldots$ 

$$\mathbb{E}\left(\mathbf{e}^{i\theta S_{\Gamma_p}}\right) = \left(\left(\frac{p}{1 - q\,\mathbb{E}\left(\mathbf{e}^{i\theta \xi_1}\right)}\right)^{\frac{1}{n}}\right)^n$$
$$= \mathbb{E}\left(\mathbf{e}^{i\theta S_{\mathbf{A}_{1/n,p}}}\right)^n\tag{9}$$

where  $\Lambda_{1/n,p}$  is a negative binomial random variable with parameters  $1/n$  and  $p$ , which is independent of S. The latter has distribution mass function

$$\mathbb{P}(\mathbf{\Lambda}_{1/n,p}=k) = \frac{1}{k!} \frac{\Gamma(k+1/n)}{\Gamma(1/n)} p^{1/n} q^k \qquad (10)$$

for  $k = 0, 1, 2, \ldots$ 

## **Wiener–Hopf Factorization for Random** Walks

We now turn our attention to the Wiener-Hopf factorization. Fix  $0 < p < 1$  and define

$$G = \inf \left\{ k = 0, 1, \dots, \mathbf{\Gamma}_p : S_k = \max_{j = 0, 1, \dots, \mathbf{\Gamma}_p} S_j \right\}$$
(11)

where  $\Gamma_p$  is a geometrically distributed random variable with parameter  $p$ , which is independent of the random walk  $S$ , that is,  $G$  is the first visit of  $S$ to its maximum over the time period  $\{0, 1, \ldots, \Gamma_p\}$ . Now define

$$N = \inf\{n > 0 : S_n > 0\} \tag{12}$$

In other words, the first visit of S to  $(0, \infty)$  after  $time 0.$ 

Theorem 1 (Wiener-Hopf Factorization for Ran**dom Walks**) Assume all of the notation and conventions above.

 $(G, S_G)$  is independent of  $(\Gamma_p - G, S_{\Gamma_p} - S_G)$ (i) and both pairs are infinitely divisible.

(ii) For  $0 < s < 1$  and  $\theta \in \mathbb{R}$ 

$$E\left(s^{G}e^{i\theta S_{G}}\right)$$
  
=  $\exp\left\{-\int_{(0,\infty)}\sum_{n=1}^{\infty}\left(1-s^{n}e^{i\theta x}\right)q^{n}\frac{1}{n}F^{*n}(\mathrm{d}x)\right\}$  (13)

(iii) For 
$$0 < s \le 1$$
 and  $\theta \in \mathbb{R}$ 

$$E\left(s^{N}e^{i\theta S_{N}}\right)$$
  
= 1 - exp $\left\{-\int_{(0,\infty)}\sum_{n=1}^{\infty}s^{n}e^{i\theta x}\frac{1}{n}F^{*n}(\mathrm{d}x)\right\}$  (14)

Note that the third part of the Wiener-Hopf factorization characterizes what is known as the ladder height process of the random walk S. The latter is the bivariate random walk  $(T, H) := \{(T_n, H_n) : n =$  $0, 1, 2, \ldots$ } where  $(T_0, H_0) = (0, 0)$ , and otherwise for  $n = 1, 2, 3, \ldots$ 

$$T_n = \begin{cases} \min\left\{k \ge 1 : S_{T_{n-1}+k} > H_{n-1}\right\} & \text{if } T_{n-1} < \infty \\ \infty & \text{if } T_{n-1} = \infty \end{cases}$$

and

$$H_n = \begin{cases} S_{T_n} & \text{if } T_n < \infty \\ \infty & \text{if } T_n = \infty \end{cases} \tag{15}$$

That is to say, the process  $(T, H)$ , until becoming infinite in value, represents the times and positions of the running maxima of  $S$ , the so-called ladder times and ladder heights. It is not difficult to see that  $T_n$ is a stopping time for each  $n = 0, 1, 2, \ldots$  and hence thanks to the i.i.d. increments of  $S$ , the increments of  $(T, H)$  are i.i.d. with the same law as the pair  $(N, S_N).$ 

**Proof** (i) The path of the random walk may be broken into  $v \in \{0, 1, 2, \ldots\}$  finite (or completed) excursions from the maximum followed by an additional excursion, which straddles the random time  $\Gamma_{p}$ . Here, we understand the use of the word straddle to mean that if  $\ell$  is the index of the left end point of the straddling excursion then  $\ell \leq \Gamma_p$ . By the strong Markov property for random walks and lack of memory, the completed excursions must have the same law, namely, that of a random walk sampled on the time points  $\{1, 2, \ldots, N\}$  conditioned on the

event that  $\{N \leq \Gamma_p\}$  and hence  $\nu$  is geometrically distributed with parameter  $1 - P(N \leq \Gamma_p)$ . Mathematically, we express

$$(G, S_G) = \sum_{i=1}^{\nu} \left( N^{(i)}, H^{(i)} \right) \tag{16}$$

where the pairs  $\{(N^{(i)}, H^{(i)}): i = 1, 2, ...\}$  are independent having the same distribution as  $(N, S_N)$ conditioned on  $\{N \leq \Gamma_p\}$ . Note also that G is the sum of the lengths of the latter conditioned excursions and  $S_G$  is the sum of the respective increment of the terminal value over the initial value of each excursion. In other words,  $(G, S_G)$  is the componentwise sum of  $\nu$  independent copies of  $(N, S_N)$  (with  $(G, S_G) = (0, 0)$  if  $v = 0$ ). Infinite divisibility follows as a consequence of the fact that  $(G, S_G)$  is a geometric sum of i.i.d. random variables. The independence of  $(G, S_G)$  and  $(\Gamma_p - G, S_{\Gamma_p} - S_G)$  is immediate from the decomposition described above.

Feller's classic duality lemma (cf [3]) for random walks says that for any  $n = 0, 1, 2, \ldots$  (which may later be randomized with an independent geometric distribution), the independence and common distribution of increments implies that  $\{S_{n-k} - S_n :$  $k = 0, 1, \ldots, n$  has the same law as  $\{-S_k : k =$  $0, 1, \ldots, n$ . In the current context, the duality lemma also implies that the pair  $(\Gamma_p - G, S_{\Gamma_p} - S_G)$  is equal in distribution to  $(D, S_D)$  where

$$D := \sup \left\{ k = 0, 1, \dots, \mathbf{\Gamma}_p : S_k = \min_{j = 0, 1, \dots, \mathbf{\Gamma}_p} S_j \right\}$$
(17)

(ii) Note that, as a geometric sum of i.i.d. random variables, the pair  $(\Gamma_p, S_{\Gamma_p})$  is infinitely divisible for  $s \in (0, 1)$  and  $\theta \in \mathbb{R}$ , let  $q = 1 - p$  and also that, on one hand,

$$E(s^{\Gamma_{p}}e^{i\theta S_{\Gamma_{p}}}) = E\left(E\left(se^{i\theta S_{1}}\right)^{\Gamma_{p}}\right)$$
$$= \sum_{k\geq 0} p\left(qsE\left(e^{i\theta S_{1}}\right)\right)^{k}$$
$$= \frac{p}{1 - qsE\left(e^{i\theta S_{1}}\right)}$$
(18)

and, on the other hand, with the help of Fubini's Theorem,

$$\exp\left\{-\int_{\mathbb{R}}\sum_{n=1}^{\infty}\left(1-s^{n}e^{i\theta x}\right)q^{n}\frac{1}{n}F^{*n}(\mathrm{d}x)\right\}$$
$$=\exp\left\{-\sum_{n=1}^{\infty}\left(1-s^{n}E\left(\mathrm{e}^{i\theta S_{n}}\right)\right)q^{n}\frac{1}{n}\right\}$$
$$=\exp\left\{-\sum_{n=1}^{\infty}\left(1-s^{n}E\left(\mathrm{e}^{i\theta S_{1}}\right)^{n}\right)q^{n}\frac{1}{n}\right\}$$
$$=\exp\left\{\log(1-q)-\log\left(1-sqE\left(\mathrm{e}^{i\theta S_{1}}\right)\right)\right\}$$
$$=\frac{p}{1-qsE(\mathrm{e}^{i\theta S_{1}})}\tag{19}$$

where, in the last equality, we have applied the Mercator–Newton series expansion of the logarithm. Comparing the conclusions of the last two series of equalities, the required expression for  $E(s^{\Gamma_p}e^{i\theta S_{\Gamma_p}})$ follows. The Lévy measure mentioned in equation  $(4)$  is thus identifiable as

$$\Pi(\mathrm{d}y,\,\mathrm{d}x) = \sum_{n=1}^{\infty} \delta_{\{n\}}(\mathrm{d}y) F^{*n}(\mathrm{d}x) \frac{1}{n} q^n \qquad (20)$$

for  $(y, x) \in \mathbb{R}^2$ .

We know that  $(\Gamma_p, S_{\Gamma_p})$  may be written as the independent sum of  $(G, S_G)$  and  $(\Gamma_p - G, S_{\Gamma_p} S_G$ ), where both are infinitely divisible. Further, the former has Lévy measure supported on  $\{1, 2, \ldots\} \times$  $(0,\infty)$  and the latter has Lévy measure supported on  $\{1, 2, \ldots\} \times (-\infty, 0)$ . In addition,  $E(s^{\overline{G}}e^{i\theta S_G})$ extends to the upper half of the complex plane in  $\theta$  (and is continuous on the real axis) and  $E\left(s^{\Gamma_p-G}e^{i\theta(S_{\Gamma_p}-S_G)}\right)$  extends to the lower half of the complex plane in  $\acute{\theta}$  (and is continuous on the real axis).<sup> $a$ </sup> Taking account of equation (4), this forces the factorization of the expression for  $E(s^{\Gamma_p}e^{i\theta S_{\Gamma_p}})$ in such a way that

$$E(s^{G}e^{i\theta S_{G}}) = e^{-\int_{(0,\infty)} \sum_{n=1}^{\infty} (1-s^{n}e^{i\theta x})q^{n}F^{*n}(\mathrm{d}x)/n}$$
(21)

(iii) Note that the path decomposition given in part (i) shows that

$$E\left(s^{G}e^{i\theta S_{G}}\right) = E\left(s^{\sum_{i=1}^{\nu}N^{(i)}}e^{i\theta\sum_{i=1}^{\nu}H^{(i)}}\right) \qquad (22)$$

where the pairs  $\{(N^{(i)}, H^{(i)}): i = 1, 2, ...\}$  are independent having the same distribution as  $(N, S_N)$  conditioned on  $\{N < \Gamma_n\}$ . Hence, we have

$$\begin{split} &E\left(s^{G}\mathbf{e}^{i\theta S_{G}}\right) \\ &= \sum_{k\geq 0} P(N>\Gamma_{p})P(N\leq\Gamma_{p})^{k} \\ &\times E\left(s^{\sum_{i=1}^{k}N^{(i)}}\mathbf{e}^{i\theta\sum_{i=1}^{k}H^{(i)}}\right) \\ &= \sum_{k\geq 0} P(N>\Gamma_{p})P(N\leq\Gamma_{p})^{k}E\left(s^{N}\mathbf{e}^{i\theta S_{N}}|N\leq\Gamma_{p}\right)^{k} \\ &= \sum_{k\geq 0} P(N>\Gamma_{p})E\left(s^{N}\mathbf{e}^{i\theta S_{N}}\mathbf{1}_{\{N\leq\Gamma_{p}\}}\right)^{k} \\ &= \sum_{k\geq 0} P(N>\Gamma_{p})E\left((qs)^{N}\mathbf{e}^{i\theta S_{N}}\right)^{k} \\ &= \frac{P(N>\Gamma_{p})}{1-E\left((qs)^{N}\mathbf{e}^{i\theta S_{N}}\right)} \end{split} \tag{23}$$

Note that in the fourth equality we use the fact that  $P(\Gamma_p \ge n) = q^n$ .

The required equality to be proved follows by setting  $s = 0$  in equation (21) to recover

$$P(N > \Gamma_p) = \exp\left\{-\int_{(0,\infty)} \sum_{n=1}^{\infty} \frac{q^n}{n} F^{*n}(\mathrm{d}x)\right\}$$
(24)

and then plugging this back into the right-hand side of equation (23) and rearranging.

#### Lévy Processes and Infinite Divisibility

A (one-dimensional) stochastic process  $X = \{X_t :$  $t \ge 0$ } is called a *Lévy process* (see **Lévy Processes**) on some probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  if

- X has paths that are  $\mathbb{P}$ -almost surely right 1. continuous with left limits;
- 2. given  $0 \le s \le t < \infty$ ,  $X_t X_s$  is independent of  $\{X_u : u < s\};$
- 3. given  $0 \le s \le t < \infty$ ,  $X_t X_s$  is equal in distribution to  $X_{t-s}$ ; and

$$\mathbb{P}(X_0 = 0) = 1\tag{25}$$

It is easy to deduce that if  $X$  is a Lévy process, then for each  $t > 0$  the random variable  $X_t$  is infinitely divisible. Indeed, one may also show via a straightforward computation that

$$\mathbb{E}\left(\mathrm{e}^{i\theta X_{t}}\right) = \mathrm{e}^{-\Psi(\theta)t} \text{ for all } \theta \in \mathbb{R}, \quad t \ge 0 \quad (26)$$

where, in its most general form,  $\Psi$  takes the form given in equation (4). Conversely, it can also be shown that given a Lévy–Khintchine exponent (4) of an infinitely divisible random variable, there exists a Lévy process that satisfies equation (26). In the special case that the Lévy-Khintchine exponent  $\Psi$ belongs to that of a positive-valued infinitely divisible distribution, it follows that the increments of the associated Lévy process must be positive and hence its paths are necessarily monotone increasing. In full generality, a Lévy process may be naively thought of as the independent sum of a linear Brownian motion plus an independent process with discontinuities in its path, which, in turn, may be seen as the limit (in an appropriate sense) of the partial sums of a sequence of compound Poisson processes with drift. The book by Bertoin [1] gives a comprehensive account of the above details.

The definition of a Lévy process suggests that it may be thought of as a continuous-time analog of a random walk. Let us introduce the exponential random variable with parameter  $p$ , denoted by  $\mathbf{e}_p$ , which henceforth is assumed to be independent of all other random quantities under discussion and defined on the same probability space. Like the geometric distribution, the exponential distribution also has a lack-of-memory property in the sense that for all  $0 \le s, t < \infty$  we have  $\mathbb{P}(\mathbf{e}_p > t + s | \mathbf{e}_p > t) =$  $\mathbb{P}(\mathbf{e}_p > s) = e^{-ps}$ . Moreover,  $\mathbf{e}_p$ , and, more generally,  $X_{e_n}$ , is infinitely divisible. Indeed, straightforward computations show that for each  $n = 1, 2, 3, \ldots$ 

$$\mathbb{E}(\mathrm{e}^{i\theta X_{\mathbf{e}_p}}) = \left(\left(\frac{p}{p+\Psi(\theta)}\right)^{\frac{1}{n}}\right)^n = \mathbb{E}\left(\mathrm{e}^{i\theta X_{\gamma_{1/n,p}}}\right)^n\tag{27}$$

where  $\gamma_{1/n,p}$  is a gamma distribution with parameters  $1/n$  and p, which is independent of X. The latter has distribution

$$\mathbb{P}(\gamma_{1/n,p} \in \mathrm{d}x) = \frac{p^{1/n}}{\Gamma(1/n)} x^{-1+1/n} \mathrm{e}^{-\mathrm{p}x} \, \mathrm{d}x \qquad (28)$$

for  $x > 0$ .

# Wiener-Hopf Factorization for Lévy Processes

The Wiener-Hopf factorization for a one-dimensional Lévy processes is slightly more technical than for random walks but, in principle, appeals to essentially the same ideas that have been exhibited in the above exposition of the Wiener-Hopf factorization for random walks. In this section, therefore, we give only a statement of the Wiener-Hopf factorization. The reader who is interested in the full technical details is directed primarily to the article by Greenwood and Pitman [6] for a natural and insightful probabilistic presentation (in the author's opinion). Alternative accounts based on the aforementioned article can be found in the books by Bertoin [1] and Kyprianou [12], and derivation of the Wiener–Hopf factorization for Lévy processes from the Wiener-Hopf factorization for random walks can be found in  $[18]$ .

Before proceeding to the statement of the Wiener-Hopf factorization, we first need to introduce the ladder process associated with any Lévy process  $X$ . Here, we encounter more subtleties than for the random walk. Consider the range of the times and positions at which the process  $X$  attains new maxima. That is to say, the random set  $\{(t, \overline{X}_t) : \overline{X}_t = X_t\}$ where  $\overline{X}_t = \sup_{s \leq t} X_s$  is the running maximum. It turns out that this range is equal in law to the range of a killed bivariate subordinator  $(\tau, H) = \{(\tau_t, H_t) :$  $t < \zeta$ , where the killing time  $\zeta$  is an independent and exponentially distributed random variable with some rate  $\lambda \geq 0$ . In the case that  $\lim_{t \uparrow \infty} X_t = \infty$ , there should be no killing in the process  $(\tau, H)$  and hence  $\lambda = 0$  and we interpret  $\mathbb{P}(\zeta = \infty) = 1$ . Note that we may readily define the Laplace exponent of the killed process  $(\tau, H)$  by

$$\mathbb{E}(\mathrm{e}^{-\alpha\tau_{t}-\beta H_{t}}\mathbf{1}_{(t<\zeta)}) = \mathrm{e}^{-\kappa(\alpha,\beta)t} \tag{29}$$

for all  $\alpha, \beta \ge 0$  where, necessarily,  $\kappa(\alpha, \beta) = \lambda +$  $\phi(\alpha, \beta)$  is the rate of  $\zeta$ , and  $\phi$  is the bivariate Laplace exponent of the unkilled process  $\{(\tau_t, H_t) : t \ge 0\}.$ Analogous to the role played by joint probability generating and characteristic exponent of the pair  $(N, S_N)$  in Theorem 1 (iii), the quantity  $\kappa(\alpha, \beta)$  also is prominent in the Wiener-Hopf factorization for Lévy processes, which we state below. To do so, we give one final definition. For each  $t > 0$ , let

$$\overline{G}_{\mathbf{e}_p} = \sup\{s < \mathbf{e}_p : X_s = \overline{X}_s\} \tag{30}$$

Theorem 2 (The Wiener-Hopf Factorization for **Lévy Processes)** Suppose that  $X$  is any Lévy process other than a compound Poisson process. As usual, denote by  $\mathbf{e}_p$  an independent and exponentially distributed random variable.

(i) The pairs

$$(\overline{G}_{\mathbf{e}_p}, \overline{X}_{\mathbf{e}_p})$$
 and  $(\mathbf{e}_p - \overline{G}_{\mathbf{e}_p}, \overline{X}_{\mathbf{e}_p} - X_{\mathbf{e}_p})$  (31)

are independent and infinitely divisible. (ii) *For*  $\alpha, \beta \ge 0$ 

$$\mathbb{E}\left(\mathrm{e}^{-\alpha\overline{G}_{\mathbf{e}_{p}}-\beta\overline{X}_{\mathbf{e}_{p}}}\right) = \frac{\kappa(p,0)}{\kappa(p+\alpha,\beta)}\qquad(32)$$

(iii) The Laplace exponent  $\kappa(\alpha, \beta)$  may be identified in terms of the law of  $X$  in the following way,

$$\kappa(\alpha,\beta) = k \exp\left(\int_0^\infty \int_0^\infty \left(e^{-t} - e^{-\alpha t - \beta x}\right) \times \mathbb{P}(X_t \in dx) \frac{dt}{t}\right)$$
(33)

where  $\alpha, \beta \ge 0$  and k is a dimensionless strictly positive constant.

# The First Passage Problem and **Mathematical Finance**

There are many applications of the Wiener-Hopf factorization in applied probability, and mathematical finance is no exception in this respect. One of the most prolific links is the relationship between the information contained in the Wiener-Hopf factorization and the distributions of the first passage times

$$\tau_x^+ := \inf\{t > 0 : X_t > x\} \text{ and}$$
  
 $\tau_x^- := \inf\{t > 0 : X_t < x\}$  (34)

together with the overshoots  $X_{\tau^+} - x$  and  $x - X_{\tau^-}$ , where  $x \in \mathbb{R}$ . In turn, this is helpful for the pricing of certain types of exotic options.

For example, in a simple market model for which there is one risky asset modeled by an exponential Lévy process and one riskless asset with a fixed rate of return, say  $r > 0$ , the value of a perpetual American put, or indeed a perpetual down-and-in put, boils down to the computation of the following quantity:

$$v_{y}(x) := \mathbb{E}\left(\mathrm{e}^{-r\tau_{y}^{-}}\left(K - \mathrm{e}^{X_{\tau_{y}^{-}}}\right)^{+} | X_{0} = x\right) \quad (35)$$

where  $y \in \mathbb{R}$  and  $z^+ = \max\{0, z\}$  and the expectation is taken with respect to an appropriate risk-neutral measure that keeps  $X$  in the class of Lévy processes (e.g., the measure that occurs as a result of the Escher transform). To see the connection with the Wiener-Hopf factorization consider the following lemma and its corollary:

**Lemma 1** For all  $\alpha > 0$ ,  $\beta > 0$  and  $x > 0$  we have

$$\mathbb{E}\left(\mathrm{e}^{-\alpha\tau_{x}^{+}-\beta X_{\tau_{x}^{+}}}\mathbf{1}_{(\tau_{x}^{+}<\infty)}\right) = \frac{\mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\mathbf{1}_{\left(\overline{X}_{\mathbf{e}_{\alpha}}>x\right)}\right)}{\mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\right)}\tag{36}$$

**Proof** First, assume that  $\alpha$ ,  $\beta$ ,  $x > 0$  and note that

$$\begin{split} &\mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\mathbf{1}_{\left(\overline{X}_{\mathbf{e}_{\alpha}}>x\right)}\right) \\ &= \mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\mathbf{1}_{\left(\tau_{x}^{+}<\mathbf{e}_{\alpha}\right)}\right) \\ &= \mathbb{E}\left(\mathbf{1}_{\left(\tau_{x}^{+}<\mathbf{e}_{\alpha}\right)}\mathrm{e}^{-\beta X_{\tau_{x}^{+}}}\mathbb{E}\left(\mathrm{e}^{-\beta\left(\overline{X}_{\mathbf{e}_{\alpha}}-X_{\tau_{x}^{+}}\right)}\middle|\mathcal{F}_{\tau_{x}^{+}}\right)\right) \tag{37} \end{split}$$

Now, conditionally on  $\underline{\mathcal{F}}_{\tau_x^+}$  and on the event  $\tau_x^+ < \mathbf{e}_{\alpha}$ , the random variables  $\overline{X}_{\mathbf{e}_{\alpha}}-X_{\tau_{x}^{+}}$  and  $\overline{X}_{\mathbf{e}_{\alpha}}$  have the same distribution, thanks to the lack-of-memory property of  $\mathbf{e}_{\alpha}$  and the strong Markov property. Hence, we have the factorization

$$\mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\mathbf{1}_{\left(\overline{X}_{\mathbf{e}_{\alpha}}>x\right)}\right) = \mathbb{E}\left(\mathrm{e}^{-\alpha\tau_{x}^{+}-\beta X_{\tau_{x}^{+}}}\right)\mathbb{E}\left(\mathrm{e}^{-\beta\overline{X}_{\mathbf{e}_{\alpha}}}\right)$$
(38)

The case that  $\beta$  or x is equal to zero can be achieved by taking limits on both sides of the above equality.

By replacing X by  $-X$  in Lemma 1, we get the following analogous result for first passage into the negative half line.

**Corollary 1** *For all*  $\alpha, \beta \ge 0$  *and*  $x \ge 0$ *, we have* 

$$\mathbb{E}\left(\mathrm{e}^{-\alpha\tau_{-x}^{-}+\beta X_{\tau_{-x}^{-}}}\mathbf{1}_{(\tau_{-x}^{-}<\infty)}\right) = \frac{\mathbb{E}\left(\mathrm{e}^{\beta \underline{X}_{\mathbf{e}_{\alpha}}}\mathbf{1}_{(-\underline{X}_{\mathbf{e}_{\alpha}}>x)}\right)}{\mathbb{E}\left(\mathrm{e}^{\beta \underline{X}_{\mathbf{e}_{\alpha}}}\right)}\tag{39}$$

In that case, we may develop the expression in equation  $(35)$  by using Corollary 1 to obtain

$$v_{y}(x) = \frac{\mathbb{E}\left(\left(K\mathbb{E}\left[e^{\underline{X}_{e_{r}}}\right] - e^{x + \underline{X}_{e_{r}}}\right)\mathbf{1}_{\left(-\underline{X}_{e_{r}} > x - y\right)}\right)}{\mathbb{E}\left(e^{\underline{X}_{e_{r}}}\right)}$$
(40)

where  $\underline{X}_{t} = \inf_{s < t} X_{s}$  is the running infimum. Ultimately, further development of the expression on the right-hand side above requires knowledge of the distribution of  $X_{\bullet}$ . This is information, which, in principle, can be extracted from the Wiener-Hopf factorization.

We conclude by mentioning the articles  $[5, 10]$ and [11] in which the Wiener-Hopf factorization is used for the pricing of barrier options (see Lookback Options).

#### **End Notes**

<sup>a.</sup>It is this part of the proof that makes the connection with the general analytic technique of the Wiener-Hopf method of factorizing operators. This also explains the origin of the terminology Weiner-Hopf factorization for what is otherwise a path, and consequently distributional, decomposition.

## References

- [1] Bertoin, J. (1996). Lévy Processes, Cambridge University Press.
- [2] Borovkov, A.A. (1976). Stochastic Processes in Oueueing Theory, Springer-Verlag.
- [3] Feller, W. (1971). An Introduction to Probability Theory and its Applications, 2nd Edition, Wiley, Vol. II.
- Fristedt, B.E. (1974). Sample functions of stochastic pro-[4] cesses with stationary independent increments, Advances in Probability 3, 241-396.
- [5] Fusai, G., Abrahams, I.D. & Sgarra, C. (2006). An exact analytical solution for discrete barrier options, Finance and Stochastics  $10$ , 1–26.
- Greenwood, P.E. & Pitman, J.W. (1979). Fluctua-[6] tion identities for Lévy processes and splitting at

the maximum, *Advances in Applied Probability* **12**, 839–902.

- [7] Greenwood, P.E. & Pitman, J.W. (1980). Fluctuation identities for random walk by path decomposition at the maximum. Abstracts of the Ninth Conference on Stochastic Processes and Their Applications, Evanston, Illinois, 6–10 August 1979, *Advances in Applied Probability* **12**, 291–293.
- [8] Gusak, D.V. & Korolyuk, V.S. (1969). On the joint distribution of a process with stationary independent increments and its maximum. *Theory of Probability* **14**, 400–409.
- [9] Hopf, E. (1934). *Mathematical Problems of Radiative Equilibrium*. Cambridge tracts, No. 31.
- [10] Jeannin, M. & Pistorius, M.R. (2007). *A Transform Approach to Calculate Prices and Greeks of Barrier Options Driven by a Class of L´evy*. Available at arXiv: http://arxiv.org/abs/0812.3128.
- [11] Kudryavtsev, O. & Levendorski, S.Z. (2007). *Fast and Accurate Pricing of Barrier Options Under Levy Processes*. Available at SSRN: http://ssrn.com/abstract= 1040061.
- [12] Kyprianou, A.E. (2006). *Introductory Lectures on Fluctuations of L´evy Processes with Applications*, Springer.
- [13] Payley, R. & Wiener, N. (1934). *Fourier Transforms in the Complex Domain*, American Mathematical Society. Colloquium Publications, New York, Vol. 19.

- [14] Percheskii, E.A. & Rogozin, B.A. (1969). On the joint distribution of random variables associated with fluctuations of a process with independent increments, *Theory of Probability and its Applications* **14**, 410–423.
- [15] Spitzer, E. (1956). A combinatorial lemma and its application to probability theory, *Transactions of the American Mathematical Society* **82**, 323–339.
- [16] Spitzer, E. (1957). The Wiener-Hopf equation whose kernel is a probability density, *Duke Mathematical Journal* **24**, 327–343.
- [17] Spitzer, E. (1964). *Principles of Random Walk*, Van Nostrand.
- [18] Sato, K.-I. (1999). *L´evy Processes and Infinitely Divisible Distributions*, Cambridge University Press.

# **Related Articles**

**Fractional Brownian Motion**; **Infinite Divisibility**; **Levy Processes ´** ; **Lookback Options**.

ANDREAS E. KYPRIANOU
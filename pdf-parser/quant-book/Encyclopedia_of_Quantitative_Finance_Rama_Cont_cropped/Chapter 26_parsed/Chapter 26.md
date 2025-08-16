# **Infinite Divisibility**

We say that a random variable  $X$  has an infinitely divisible (ID) distribution (in short  $X$  is ID) if for all the integers  $n > 1$  there exist *n* independent identically distributed (i.i.d) random variables  $X_1,\ldots,X_n$ , such that  $X_1+\cdots+X_n\stackrel{d}{=}X$ , where  $\stackrel{d}{=}$ is equality in distribution. Alternatively,  $X$  (or its distribution  $\mu$ ) is ID if for all  $n \ge 1$ ,  $\mu$  is the *nth* convolution  $\mu_n * \cdots * \mu_n$ , where  $\mu_n$  is a probability distribution.

There are several advantages in using infinitely divisible distributions and processes in financial modeling. First, they offer wide possibilities for modeling alternatives to the Gaussian and stable distributions, while maintaining a link with the central limit theorem and a rich probabilistic structure. Second, they are closely linked to Lévy processes: for each ID distribution  $\mu$  there is a Lévy process (see Lévy Processes)  $\{X_t : t \ge 0\}$  with  $X_1$  having distribution  $\mu$ . Third, every stationary distribution of an Ornstein-Uhlenbeck process (see Ornstein-Uhlenbeck Processes) belongs to the class  $L$  of ID distributions, which are self-decomposable (SD). We say that a random variable  $X$  is SD if it has the linear autoregressive property: for any  $\theta \in (0, 1)$ , there is a random variable  $\varepsilon_{\theta}$  independent of X such that  $X \stackrel{d}{=} \theta X + \varepsilon_{\theta}$ .

The concept of infinite divisibility in probability was introduced in 1929 by de Fenneti. Its theory was established in the 1930s by Khintchine, Kolmogorov, and Lévy. Motivated by applications arising in different fields, from the 1960s on there was a renewed interest in the subject, in particular, among many other topics, in the study of concrete examples and subclasses of ID distributions. Historical notes and references are found in  $[3, 6, 8, 9]$ .

## Link with the Central Limit Theorem

The class of ID distributions is characterized as the class of possible limit laws for triangular arrays of the form  $X_{n,1} + \cdots + X_{n,k_n} - a_n$ , where  $k_n > 0$  is an increasing sequence,  $X_{n,1}, \ldots, X_{n,k_n}$  are independent random variable for every  $n \ge 1$ ,  $a_n$ are normalized constants, and  $\{X_{n,j}\}$  is *infinitesimal*:  $\lim_{n\to\infty} \max_{1\leq j\leq k_n} P(|X_{n,j}| > \epsilon) = 0$ , for each  $\epsilon > 0$ . On the other hand, the class L of SD distributions is characterized as the class of possible limit laws for normalized sequences of the form  $(X_1 + \cdots + X_n - a_n)/b_n$ , where  $X_1, X_2, \ldots$  are independent random variables and  $a_n$  and  $b_n > 0$ are sequences of numbers with  $\lim_{n\to\infty} b_n = \infty$  and  $\lim_{n\to\infty} b_{n+1}/b_n = 1.$ 

## Lévy-Khintchine Representation

In terms of characteristic functions (see Filtering), a random variable X is ID if  $\varphi(u) = E[e^{iuX}]$  is represented by  $\varphi = (\varphi_n)^n$ , where  $\varphi_n$  is the characteristic function of a probability distribution for every  $n > 1$ . We define the *characteristic exponent* or cumulant function of X by  $\Psi(u) = \log \varphi(u)$ . The Lévy-Khintchine representation establishes that a distribution function  $\mu$  is ID if and only if its characteristic exponent is represented by

$$\Psi(u) = iau - \frac{1}{2}u^2\sigma^2\n$$

$$\n+ \int_{\mathbb{R}} \left( e^{iux} - 1 - iux1_{|x| \le 1} \right) \Pi(dx), \quad u \in \mathbb{R}\n$$
(1)

where  $\sigma^2 \ge 0$ , *a* ∈ ℝ and Π is a positive measure on  $\mathbb{R}$  with no atom at zero and  $\int_{\mathbb{R}} \min(1, |x|^2) \Pi(dx) <$  $\infty$ . The triplet  $(a, \sigma^2, \Pi)$  is unique and is called the generating triplet of  $\mu$ , while  $\Pi$  is its Lévy *measure.* When  $\pi$  is zero, we have the Gaussian distribution. We speak of the purely non-Gaussian case when  $\sigma^2 = 0$ . When  $\Pi(dx) = h(x)dx$  is absolutely continuous, we call the nonnegative function  $h$  the Lévy density of  $\Pi$ . Distributions in the class  $L$  are also characterized by having Lévy densities of the form  $h(x) = |x|^{-1} g(x)$ , where g is nondecreasing in  $x < 0$  and nonincreasing in  $x > 0.$ 

A nonnegative ID random variable is characterized by a special form of its Lévy-Khintchine representation: it is purely non-Gaussian,  $\Pi(-\infty, 0) = 0$ ,  $\int_{|x|<1} |x| \Pi(\mathrm{d}x) < \infty$ , and

$$\Psi(u) = ia_0u + \int_{\mathbb{R}_+} \left( e^{iux} - 1 \right) \Pi(dx) \qquad (2)$$

where  $a_0 \ge 0$  is called the *drift*. The associated Lévy process  $\{X_t : t \ge 0\}$  is called a *subordinator*. It is a

nonnegative increasing process having characteristic exponent (2). Subordinators are useful models for random time evolutions.

Several properties of an ID random variable  $X$ are related to corresponding properties of its Lévy measure  $\Pi$ . For example, the *k*th moment  $E |X|^k$  is finite if and only if  $\int_{|x|>1} |x|^k \Pi(dx)$  is finite. Likewise, for the ID<sub>log</sub> condition:  $\int_{|x|>2} \ln |x| \Pi(dx) < \infty$ if and only if  $\int_{|x|>2} \ln |x| \mu(dx) < \infty$ .

The monograph [8] has a detailed study of multivariate ID distributions and their associated Lévy processes.

### **Classical Examples and Criteria**

The Poisson distribution with mean  $\lambda > 0$  is ID with Lévy measure  $\Pi(B) = \lambda 1_{\{1\}}(B)$ , but is not SD. A compound Poisson distribution is the law of  $X = \sum_{i=1}^{N} Y_i$ , where  $N, Y_1, Y_2, \ldots$  are independent random variables,  $N$  having Poisson distribution with mean  $\lambda$  and the  $Y_i$ 's have the same distribution G, with  $G(\{0\}) = 0$ . Any compound Poisson distribution is ID with Lévy measure  $\Pi(B) = \lambda G(B)$ . This distribution is a building block for all other ID laws, since every ID distribution is the limit of a sequence of compound Poisson distributions.

An important example of an SD law is the gamma distribution with shape parameter  $\alpha > 0$  and scale parameter  $\beta > 0$ . It has Lévy density  $h(x) =$  $\alpha x^{-1}e^{-\beta x}$ ,  $x > 0$ . The  $\alpha$ -stable distribution, with  $0 < \alpha < 2$  and purely non Gaussian, is also SD. Its Lévy density is  $h(x) = c_1 x^{-1-\alpha} dx$  on  $(0, \infty)$  and  $h(\mathrm{d}x) = c_2 |x|^{-1-\alpha}$  on  $(-\infty, 0)$ , with  $c_1 \ge 0, c_2 \ge 0$ and  $c_1 + c_2 > 0$ .

There is no explicit characterization of infinite divisibility in terms of densities or distributions. However, there are some sufficient or necessary conditions to test for infinite divisibility. A nonnegative random variable with density  $f$  is ID in any of the following cases: (i)  $\log f$  is convex, (ii) f is completely monotone, or (iii)  $f$  is hyperbolically completely monotone [9]. If  $X$  is symmetric around zero, it is ID if it has a density that is completely monotone on  $(0, \infty)$ . For a non-Gaussian ID distribution F, its tail behavior is  $-\log(1 + F(-x) - F(x)) = O(x \log x)$ , when  $x \to \infty$ . Hence, no bounded random variable is ID and if a density has a decay of the type  $c_1 \exp(-c_2 x^2)$  with some  $c_1, c_2$  positive and if it is not Gaussian, then  $F$  is not ID. An important property of SD distributions is that they always have densities that are unimodal.

Infinite divisibility is preserved under some mixtures of distributions. One has the surprising fact that any mixture of the exponential distribution is ID:  $X \stackrel{d}{=} YV$  is ID whenever V has exponential distribution and  $Y$  is an arbitrary nonnegative random variable independent of  $V$ . The monograph [9] has a detailed study of ID mixtures.

### **Stochastic Integral Representations**

Several classes of ID distributions are characterized by stochastic integrals (see Stochastic Integrals) of a nonrandom function with respect to a Lévy process [2]. The classical example is the class  $L$ that is also characterized as all the laws of  $X \stackrel{d}{=}$  $\int_0^\infty e^{-t} \mathrm{d}Z_t$ , where  $Z_t$  is a Levy process having Lévy measure  $\Pi_Z$  with the ID<sub>log</sub> condition. More generally, the stochastic integral  $\int_0^1 \log t^{-1} dZ_t$  is well defined for every Lévy process  $Z_t$ . Denote by  $B(\mathbb{R})$ the class of all the distributions of these stochastic integrals. The class  $B(\mathbb{R})$  coincides with those ID laws with completely monotone Lévy density. It is also characterized as the smallest class that contains all mixtures of exponential distributions and is closed under convolution, convergence, and reflection. It is sometimes called the Bondenson-Goldie-Steutel class of distributions. Multivariate extensions are presented in [2].

## **Generalized Gamma Convolutions**

The class of generalized gamma convolutions (GGCs) is the smallest class of probability distributions on  $\mathbb{R}_+$  that contains all gamma distributions and is closed under convolution and convergence in distribution [6]. These laws are in the class  $L$  and have Lévy density of the form  $h(x) = x^{-1}g(x), x > 0,$ with g a completely monotone function on  $(0, \infty)$ . Most of the classical distributions on  $\mathbb{R}_+$  are GGC: gamma, lognormal, positive  $\alpha$ -stable, Pareto, Student  $t$ -distribution, Gumbel, and  $F$ -distribution. Of special applicability in financial modeling is the family of generalized inverse Gaussian distributions [4, 7].

A distribution  $\mu$  with characteristic exponent  $\Psi$ is GGC if and only if there exists a positive Radon measure U on  $(0, \infty)$  such that

$$\Psi(u) = ia_0u - \int_0^\infty \log\left(1 + \frac{iu}{s}\right)U(\mathrm{d}s) \qquad (3)$$

with  $\int_0^1 |\log x| U(\mathrm{d}x) < \infty$  and  $\int_1^\infty U(\mathrm{d}x)/x < \infty$ . The measure  $U_{\mu}$  is called the *Thorin measure* of  $\mu$ . So, the triplet of  $\mu$  is  $(a_0, 0, \nu_\mu)$  where the Lévy measure is concentrated on  $(0,\infty)$  and such that  $v_{\mu}(\mathrm{d}x) = \mathrm{d}x/x \int_{0}^{\infty} \mathrm{e}^{-xs} U_{\mu}(\mathrm{d}s)$ . Moreover, any GGC is the law of a Wiener-gamma integral  $\int_0^\infty h(u) \mathrm{d}\gamma_u$ , where  $(\gamma_t; t \ge 0)$  is the standard gamma process with Lévy measure  $v(dx) = e^{-x}(dx/x)$  and h is a Borel function  $h: \mathbb{R}_+ \to \mathbb{R}_+$  with  $\int_0^\infty \log(1 + h(t)) dt < \infty$ . The function *h* is called the *Thorin function* of  $\mu$  and is obtained as follows. Let  $F_U(x) = \int_0^x U(dy)$ for  $x \ge 0$  and let  $F_U^{-1}(s)$  be the right continuous inverse of  $F_{II}^{-1}(s)$  in the sense of composition of functions, that is  $F_U^{-1}(s) = \inf\{t > 0; F_U(t) \ge s\}$  for  $s \ge 0$ . Then,  $h(s) = 1/F_U^{-1}(s)$  for  $s \ge 0$ . For the positive  $\alpha$ -stable distributions,  $0 < \alpha < 1$ ,  $h(s) =$  $\{s\theta\Gamma(\alpha+1)\}^{-1/\alpha}$  for a  $\theta>0$ .

For distributions on  $\mathbb{R}$ , Thorin also introduced the class  $T(\mathbb{R})$  of extended generalized gamma convolutions as the smallest class that contains the GGC and is closed under convolution, convergence in distribution, and reflection. These distributions are in the class  $L$  and are characterized by the alternative representation of their characteristic exponents

$$\Psi(u) = iua - \frac{1}{2}u^2\sigma^2\n$$

$$\n-\int_{\mathbb{R}_+} \left[ \ln\left(1 - \frac{iu}{x}\right) + \frac{iux}{1+x^2} \right] U(\mathrm{d}x) \quad (4)$$

where  $a \in \mathbb{R}$ ,  $\sigma^2 \ge 0$  and  $U : \mathbb{R}_+ \to \mathbb{R}_+$  is a nondecreasing function with  $U(0) = 0$ ,  $\int_0^1 |\ln(x)| U(dx) <$  $\infty$  and  $\int_{1}^{\infty} x^{-2} U(\mathrm{d}x) < \infty$ . Several examples of Thorin distributions are given in [6, 9]. Any member of this class is the law of a stochastic integral  $\int_0^\infty g^*(t) dZ_t$ , where  $Z_t$  is a Lévy process with  $Z_1$  satisfying the ID<sub>log</sub> condition and  $g^*$  is the inverse of the incomplete gamma function  $g(t) =$  $\int_{t}^{\infty} u^{-1} e^{-u} du$  [2].

## Type G Distributions

A random variable X is of type G if  $X \stackrel{d}{=} \sqrt{V}N$ , where  $N$  and  $V$  are independent random variables with  $V$  being nonnegative ID and  $N$  having the standard normal distribution. Any type  $G$  distribution is ID and it is interpreted as the law of a random time changed Brownian motion  $B_V$ , where  $\{B_t : t \ge 0\}$  is a Brownian motion independent of V. When we know the Lévy measure  $\rho$  of V, we can compute the Lévy density of X as  $h(x) =$  $(2\pi)^{-1/2} \int_{\mathbb{R}_+} s^{-1/2} e^{-\frac{1}{2s}x^2} \rho(\mathrm{d}s)$  as well as its characteristic exponent

$$\Psi_X(u) = \int_{\mathbb{R}_+} \left( e^{-(1/2)u^2 s} - 1 \right) \rho(ds) \tag{5}$$

Many classical distributions are of type  $G$  and SD: the gamma variance distribution, where  $V$  has a gamma distribution; the Student  $t$ , where  $V$  has the distribution of the reciprocal chi-square distribution and the symmetric  $\alpha$ -stable distributions,  $0 < \alpha < 2$ ; here V is a positive  $\alpha/2$ -stable random variable, including the Cauchy distribution case  $\alpha = 1$ . Of special relevance in financial modeling are the normal inverse Gaussian, with  $V$  following the inverse Gaussian law [1], and the zero-mean symmetric generalized hyperbolic distributions, where  $V$  has the generalized inverse Gaussian law [5, 7]; all their moments are finite and they can accommodate heavy tails.

### **Tempered Stable Distributions**

Tempered stable distributions (see **Tempered Stable Process**) are useful in mathematical finance as an attractive alternative to stable distributions, since they can have moments and heavy tails at the same time. Their corresponding Lévy and Ornstein-Uhlenbeck processes combines both the stable and Gaussian trends. An ID distribution on  $\mathbb{R}$  is *tempered stable* if it is purely non-Gaussian and if its Lévy measure is of the form

$$\Pi(B) = \int_{\mathbb{R}} \int_0^\infty 1_B(sx)s^{-1-\alpha}g(s)ds\tau(dx) \qquad (6)$$

where  $0 < \alpha < 2$ , g is a completely monotone function on  $(0,\infty)$  and  $\tau$  is a finite Borel measure on  $\mathbb R$ such that  $\tau$  has no atom at zero and  $\int_{\mathbb{R}} |x|^{\alpha} \tau(dx) <$  $\infty$ . These distributions are in class L and constitute a proper subclass of the class of Thorin distributions  $T(\mathbb{R})$ .

# **References**

- [1] Barndorff-Nielsen, O.E. (1998). Processes of normal inverse Gaussian type, *Finance and Stochastics* **2**, 41–68.
- [2] Barndorff-Nielsen, O.E., Maejima, M. & Sato, K. (2006). Some classes of multivariate infinitely divisible distributions admitting stochastic integral representations, *Bernoulli* **12**, 1–33.
- [3] Barndorff-Nielsen, O.E., Mikosch, T. & Resnick, S. (eds) (2001). *L´evy Processes—Theory and Applications*, Birkhauser, Boston. ¨
- [4] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-Gaussian Ornstein–Uhlenbeck-based models and some of their uses in financial economics (with Discussion), *Journal of the Royal Statistical Society Series B* **63**, 167–241.
- [5] Bibby, B.M. & Sorensen, M. (2003). Hyperbolic distributions in finance, in *Handbook of Heavy Tailed Distributions in Finance*, S.T. Rachev, ed, Elsevier, Amsterdam.
- [6] Bondesson, L. (1992). *Generalized Gamma Convolutions and Related Classes of Distributions and Densities*, *Lecture Notes in Statistics*, Springer, Berlin, Vol. 76.
- [7] Eberlein, E. & Hammerstein, E.V. (2004). Generalized hyperbolic and inverse Gaussian distributions: limiting cases and approximation of processes, in *Seminar*

*on Stochastic Analysis, Random Fields and Applications IV*, *Progress in Probability*, R.C. Dalang, M. Dozzi & F. Russo, eds, Birkhauser, Vol. 58, pp. 221–264. ¨

- [8] Sato, K. (1999). *L´evy Processes and Infinitely Divisible Distributions*, Cambridge University Press, Cambridge.
- [9] Steutel, F.W. & Van Harn, K. (2003). *Infinite Divisibility of Probability Distributions on the Real Line*, Marcel-Dekker, New York.

# **Further Reading**

- James, L.F., Roynette, B. & Yor, M. (2008). Generalized gamma convolutions, Dirichlet means, Thorin measures, with explicit examples, *Probability Surveys* **8**, 346–415.
- Rosinski, J. (2007). Tempering stable processes, *Stochastic Processes and Their Applications* **117**, 677–707.

# **Related Articles**

**Exponential Levy Models ´** ; **Heavy Tails**; **Levy ´ Processes**; **Ornstein–Uhlenbeck Processes**; **Tempered Stable Process**; **Time-changed Levy Process ´** .

V´ICTOR PEREZ ´ -ABREU
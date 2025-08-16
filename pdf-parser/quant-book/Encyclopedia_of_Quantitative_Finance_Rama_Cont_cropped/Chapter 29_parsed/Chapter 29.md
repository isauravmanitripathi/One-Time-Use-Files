# Lévy Processes

A Lévy process is a continuous-time stochastic process with independent and stationary increments. Lévy processes may be thought of as the continuoustime analogs of random walks. Mathematically, a Lévy process can be defined as follows.

**Definition 1** An  $\mathbb{R}^d$ -valued stochastic process  $X =$  $\{X_t : t \ge 0\}$  defined on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ is said to be a Lévy process if it possesses the following properties:

- 1. The paths of X are  $\mathbb{P}$  almost surely right continuous with left limits.
- $\mathbb{P}(X_0=0)=1.$ 2.
- 3. For  $0 \le s \le t$ ,  $X_t X_s$  is equal in distribution to  $X_{t-s}$ .
- 4. For  $0 \le s \le t$ ,  $X_t X_s$  is independent of  $\{X_u :$  $u < s$ .

Historically, Lévy processes have always played a central role in the study of stochastic processes with some of the earliest work dating back to the early 1900s. The reason for this is that, mathematically, they represent an extremely robust class of processes, which exhibit many of the interesting phenomena that appear in, for example, the theories of stochastic and potential analysis. Moreover, this in turn, together with their elementary definition, has made Lévy processes an extremely attractive class of processes for modeling in a wide variety of physical, biological, engineering, and economical scenarios. Indeed, the first appearance of particular examples of Lévy processes can be found in the foundational works of Bachelier [1, 2], concerning the use of Brownian motion, within the context of financial mathematics, and Lundberg [9], concerning the use of Poisson processes within the context of insurance mathematics.

The term Lévy process honors the work of the French mathematician Paul Lévy who, although not alone in his contribution, played an instrumental role in bringing together an understanding and characterization of processes with stationary and independent increments. In earlier literature, Lévy processes have been dealt with under various names. In the 1940s, Lévy himself referred to them as a subclass of processus additifs (additive processes), that is, processes

with independent increments. For the most part, however, research literature through the 1960s and 1970s refers to Lévy processes simply as processes with stationary and independent increments. One sees a change in language through the 1980s and by the 1990s the use of the term *Lévy process* had become standard.

Judging by the volume of published mathematical research articles, the theory of Lévy processes can be said to have experienced a steady flow of interest from the time of the foundational works, for example, of Lévy [8], Kolmogorov [7], Khintchine [6], and Itô [5]. However, it was arguably in the 1990s that a surge of interest in this field of research occurred, drastically accelerating the breadth and depth of understanding and application of the theory of Lévy processes. While there are many who made prolific contributions during this period, as well as thereafter, the general progression of this field of mathematics was enormously encouraged by the monographs of Bertoin [3] and Sato [10]. It was also the growing research momentum in the field of financial and insurance mathematics that stimulated a great deal of the interest in Lévy processes in recent times, thus entwining the modern theory of Lévy processes ever more with its historical roots.

#### Lévy Processes and Infinite Divisibility

The properties of stationary and independent increments imply that a Lévy process is a Markov process. One may show in addition that Lévy processes are strong Markov processes. From Definition 1 alone it is otherwise difficult to understand the richness of the class of Lévy processes. To get a better impression in this respect, it is necessary to introduce the notion of an infinitely divisible distribution. Generally, an  $\mathbb{R}^d$ -valued random variable  $\Theta$  has an infinitely divisible distribution if for each  $n = 1, 2, \ldots$  there exists a sequence of i.i.d. random variables  $\Theta_{1,n}, \ldots, \Theta_{n,n}$ such that

$$\Theta \stackrel{d}{=} \Theta_{1,n} + \dots + \Theta_{n,n} \tag{1}$$

where  $\stackrel{d}{=}$  is equality in distribution. Alternatively, this relation can be expressed in terms of characteristic exponents. That is to say, if  $\Theta$  has characteristic exponent  $\Psi(u) := -\log \mathbb{E}(e^{iu \cdot \Theta})$ , then  $\Theta$  is infinitely divisible if and only if for all  $n \ge 1$  there exists a characteristic exponent of a probability distribution, say  $\Psi_n$ , such that  $\Psi(u) = n \Psi_n(u)$  for all  $u \in \mathbb{R}^d$ .

It turns out that  $\Theta$  has an infinitely divisible distribution if and only if there exists a triple  $(a, \Sigma, \Pi)$ , where  $a \in \mathbb{R}^d$ ,  $\Sigma$  is a  $d \times d$  matrix whose eigenvalues are all nonnegative, and  $\Pi$  is a measure concentrated on  $\mathbb{R}^d \setminus \{0\}$  satisfying  $\int_{\mathbb{R}^d} (1 \wedge |x|^2) \Pi(dx) <$  $\infty$ , such that

$$\Psi(u) = \mathrm{i}a \cdot u + \frac{1}{2}u \cdot \Sigma u\n$$

$$\n+ \int_{\mathbb{R}^d} \left(1 - \mathrm{e}^{\mathrm{i}u \cdot x} + \mathrm{i}u \cdot x \mathbf{1}_{(|x| < 1)}\right) \Pi(\mathrm{d}x) \quad (2)$$

for every  $\theta \in \mathbb{R}^d$ . Here, we use the notation  $u \cdot x$ for the Euclidian inner product and  $|x|$  for Euclidian distance. The measure  $\Pi$  is called the *Lévy* (*char*acteristic) measure and it is unique. The identity in equation (2) is known as the Lévy-Khintchine formula.

The link between a Lévy processes and infinitely divisible distributions becomes clear when one notes that for each  $t > 0$  and any  $n = 1, 2, \ldots$ ,

$$X_t = X_{t/n} + (X_{2t/n} - X_{t/n}) + \dots + (X_t - X_{(n-1)t/n})$$
(3)

As a result of the fact that  $X$  has stationary independent Increments, it follows that  $X_t$  is infinitely divisible.

It can be deduced from the above observation that any Lévy process has the property that for all  $t \geq 0$ 

$$\mathbb{E}\left(\mathrm{e}^{\mathrm{i}u\cdot X_{t}}\right) = \mathrm{e}^{-t\Psi(u)}\tag{4}$$

where  $\Psi(\theta) := \Psi_1(\theta)$  is the characteristic exponent of  $X_1$ , which has an infinitely divisible distribution. The converse of this statement is also true, thus constituting the Lévy-Khintchine formula for Lévy processes.

Theorem 1 (Lévy-Khintchine formula for Lévy **processes).**  $a \in \mathbb{R}^d$ ,  $\Sigma$  is a  $d \times d$  matrix whose eigenvalues are all nonnegative, and  $\Pi$  is a measure concentrated on  $\mathbb{R}^d \setminus \{0\}$  satisfying  $\int_{\mathbb{R}^d} (1 \wedge |x|^2) \Pi$  $(dx) < \infty$ . Then there exists a Lévy process having characteristic exponent

$$\Psi(u) = \mathrm{i}a \cdot u + \frac{1}{2}u \cdot \Sigma u\n$$

$$\n+ \int_{\mathbb{R}^d} \left( 1 - \mathrm{e}^{\mathrm{i}u \cdot x} + \mathrm{i}u \cdot x \mathbf{1}_{(|x| < 1)} \right) \Pi(\mathrm{d}x) \quad (5)$$

Two fundamental examples of Lévy processes, which are shown in the next section to form the "building blocks" of all the other Lévy processes, are Brownian motion and compound Poisson processes. A Brownian motion is the Lévy process associated with the characteristic exponent

$$\Psi(u) = \frac{1}{2}u \cdot \Sigma u \tag{6}$$

and therefore has increments over time periods of length  $t$ , which are Gaussian distributed with covariance matrix  $\Sigma t$ . It can be shown that, up to the addition of a linear drift, Brownian motions are the only Lévy processes that have continuous paths.

A compound Poisson process is the Lévy process associated with the characteristic exponent:

$$\Psi(u) = \int_{\mathbb{R}^d} \left(1 - e^{iu \cdot x}\right) \lambda F(dx) \tag{7}$$

where  $\lambda > 0$  and F is a probability distribution. Such processes may be described pathwise by the piecewise linear process:

$$\sum_{i=1}^{N_t} \xi_i, \quad t \ge 0 \tag{8}$$

where  $\{\xi_i : i \ge 1\}$  are a sequence of i.i.d. random variables with common distribution F, and  $\{N_t : t \geq 0\}$ 0} is a Poisson process with rate  $\lambda$ ; the latter is the process with initial value zero and with unit increments whose interarrival times are independent and exponentially distributed with parameter  $\lambda$ .

It is a straightforward exercise to show that the sum of any finite number of independent Lévy processes is also a Lévy process. Under some circumstances, one may show that a countably infinite sum of Lévy processes also converges in an appropriate sense to a Lévy process. This idea forms the basis of the Lévy-Itô decomposition, discussed in the next section, where, as alluded to above, the Lévy processes that are summed together are either a Brownian motion with drift or a compound Poisson process with drift.

## The Lévy-Itô Decomposition

Hidden in the Lévy-Khintchine formula is a representation of the path of a given Lévy process. Every Lévy process may always be written as the independent sum of up to a countably infinite number of other Lévy processes, at most one of which will be a linear Brownian motion and the remaining processes will be compound Poisson processes with drift.

Let  $\Psi$  be the characteristic exponent of some infinitely divisible distribution with associated triple  $(a, \Sigma, \Pi)$ . The necessary assumption that  $\int_{\mathbb{R}^d} (1 \wedge$  $|x|^2 \Pi(dx) < \infty$  implies that  $\Pi(A) < \infty$  for all Borel A such that 0 is in the interior of  $A^c$  and, in particular, that  $\Pi(\{x : |x| \ge 1\}) \in [0, \infty)$ . With this in mind, it is not difficult to see that, after some simple reorganization, for  $u \in \mathbb{R}^d$ , the Lévy–Khintchine formula can be written in the form

$$\Psi(\theta) = \left\{ iu \cdot a + \frac{1}{2}u \cdot \Sigma u \right\} \\
+ \left\{ \lambda_0 \int_{|x| \ge 1} \left( 1 - e^{iu \cdot x} \right) F_0(dx) \right\} \\
+ \sum_{n \ge 1} \left\{ \lambda_n \int_{2^{-n} \le |x| < 2^{-(n-1)}} \left( 1 - e^{iu \cdot x} \right) F_n(dx) \right\} \\
+ i\lambda_n u \cdot \left( \int_{2^{-n} \le |x| < 2^{-(n-1)}} x F_n(dx) \right) \right\} \quad (9)$$

where  $\lambda_0 = \Pi(\{x : |x| \ge 1\}), F_0(\mathrm{d}x) = \Pi(\mathrm{d}x)/\lambda_0,$ and for  $n = 1, 2, 3, \ldots, \lambda_n = \Pi(\{x : 2^{-n} \le |x| <$  $2^{-(n-1)}$ ) and  $F_n(\mathrm{d}x) = \Pi(\mathrm{d}x)/\lambda_n$  (with the understanding that the *n*th integral is absent if  $\lambda_n = 0$ ). This decomposition suggests that the Lévy process  $X = \{X_t : t \ge 0\}$  associated with  $\Psi$  may be written as the independent sum:

$$X_t = Y_t + X_t^{(0)} + \lim_{k \uparrow \infty} \sum_{n=1}^k X_t^{(n)}, \ t \ge 0 \tag{10}$$

where

$$Y_t = B_t^{\Sigma} - at, \ t \ge 0 \tag{11}$$

with  $\{B_t^{\Sigma}: t \ge 0\}$  a *d*-dimensional Brownian motion with covariance matrix  $\Sigma$ ,

$$X_t^{(0)} = \sum_{i=1}^{N_t^{(0)}} \xi_i^{(0)}, \ t \ge 0 \tag{12}$$

with  $\{N_t^{(0)}: t \ge 0\}$  as a Poisson process with rate  $\lambda_0$  and  $\{\xi_i^{(0)}: i \ge 1\}$  are independent and identically

distributed with common distribution  $F_0(\mathrm{d}x)$  concentrated on  $\{x : |x| \ge 1\}$  and for  $n = 1, 2, 3, ...$ 

$$X_t^{(n)} = \sum_{i=1}^{N_t^{(n)}} \xi_i^{(n)} - \lambda_n t \int_{2^{-n} \le |x| < 2^{-(n-1)}} x F_n(\mathrm{d}x), \ t \ge 0$$
(13)

with  $\{N_t^{(n)}: t \ge 0\}$  as a Poisson process with rate  $\lambda_n$  and  $\{\xi_i^{(n)}: i \geq 1\}$  are independent and identically distributed with common distribution  $F_n(dx)$  concentrated on  $\{x : 2^{-n} \le |x| < 2^{-(n-1)}\}$ . The limit in equation  $(10)$  needs to be understood in the appropriate context, however.

It is a straightforward exercise to deduce that  $X^{(n)}$ is a square integrable martingale on account of the fact that it is a centered compound Poisson process together with the fact that  $x^2$  is integrable in the neighborhood of the origin against the measure  $\Pi$ . It is not difficult to see that  $\sum_{n=1}^{k} X^{(n)}$  is also a square integrable martingale. The convergence of  $\sum_{n=1}^{k} X_{\cdot}^{(n)}$ as  $k \uparrow \infty$  can happen in one of the two ways. The two quantities

$$\lim_{k \uparrow \infty} \sum_{n=1}^{k} \sum_{i=1}^{N_i^{(n)}} |\xi_i^{(n)}| \text{ and}$$
$$\lim_{k \uparrow \infty} \sum_{n=1}^{k} \int_{2^{-n} \le |x| < 2^{-(n-1)}} |x| \lambda_n F_n(\mathrm{d}x) \quad (14)$$

are either simultaneously finite or infinite (for all  $t > 0$ ), where the random limit is understood in the almost sure sense. When both are finite, that is to say, when  $\int_{|x|<1} |x|\Pi(dx) < \infty$ , then  $\sum_{n=1}^{\infty} X^{(n)}$  is well defined as the difference of a stochastic processes with jumps and a linear drift. Conversely when  $\int_{|x|<1} |x|\Pi(\mathrm{d}x) = \infty$ , it can be shown that, thanks to the assumption,  $\int_{|x|<1} |x|^2 \Pi(dx) < \infty$ ,  $\sum_{n=1}^k X^{(n)}$  converges uniformly over finite time horizons in the  $L^2$  norm as  $k \uparrow \infty$ . In that case, the two exploding limits in equation  $(14)$  compensate one another in the right way for their difference to converge in the prescribed sense.

Either way, the properties of stationary and independent increments and almost surely right continuous paths with left limits that belong to  $\sum_{n=1}^{k} X^{(n)}_{\cdot}$  as a finite sum of Lévy processes are also inherited by the limiting process as  $k \uparrow \infty$ . It is also the case that the limiting Lévy process is also a square integrable martingale just as the elements of the approximating sequence are.

## **Path Variation**

Consider any function  $f:[0,\infty)\to\mathbb{R}^d$ . Given any partition  $\mathcal{P} = \{a = t_0 < t_2 < \cdots < t_n = b\}$  of the bounded interval  $[a, b]$ , define the variation of  $f$  over  $[a, b]$  with partition  $\mathcal{P}$  by

$$V_{\mathcal{P}}(f, [a, b]) = \sum_{i=1}^{n} |f(t_i) - f(t_{i-1})| \tag{15}$$

The function  $f$  is said to be of bounded variation over  $[a, b]$  if

$$V(f, [a, b]) := \sup_{\mathcal{P}} V_{\mathcal{P}}(f, [a, b]) < \infty \tag{16}$$

where the supremum is taken over all partitions of  $[a, b]$ . Moreover,  $f$  is said to be of *bounded variation* if the above inequality is valid for all bounded intervals [a, b]. If  $V(f, [a, b]) = \infty$  for all bounded intervals  $[a, b]$ , then f is said to be of *unbounded* variation.

For any given stochastic process  $X = \{X_t : t \geq 0\}$ 0}, we may adopt these notions in the almost sure sense. So, for example, the statement " $X$  is a process of bounded variation" (or "has paths of bounded variation") simply means that as a random mapping,  $X:[0,\infty)\to\mathbb{R}^d$  is of bounded variation almost surely.

In the case that  $X$  is a Lévy process, the Lévy–Itô decomposition also gives the opportunity to establish a precise characterization of the path variation of a Lévy process. Since any Lévy process may be written as the independent sum as in equation  $(10)$ and any  $d$ -dimension Brownian motion is known to have paths of unbounded variation, it follows that any Lévy process for which  $\Sigma \neq 0$  has unbounded variation. In the case that  $\Sigma = 0$ , since the paths of the component  $X^{(0)}$  in equation (10) are independent and clearly of bounded variation (they are piecewise linear), the path variation of  $X$  is characterized by the way in which the component  $\sum_{n=1}^{k} X_t^{(n)}$  converges. In the case that

$$\int_{|x|<1} |x|\Pi(\,\mathrm{d}x)<\infty\tag{17}$$

the Lévy process  $X$  will thus be of bounded variation and otherwise, when the above integral is infinite, the paths are of unbounded variation.

In the case that  $d = 1$ , as an extreme case of a Lévy process with bounded variation, it is possible that the process  $X$  has nondecreasing paths, in which case it is called a *subordinator*. As is apparent from the Lévy-Itô decomposition (9), this will necessarily occur when  $\Pi(-\infty, 0) = 0$ ,

$$\int_{(0,1)} x \Pi(\mathrm{d}x) < \infty \tag{18}$$

and  $\Sigma = 0$ . In that case, reconsidering the decomposition  $(10)$ , one may identify

$$X_{t} = \left(-a - \int_{(0,1)} x \Pi(\mathrm{d}x)\right)t + \lim_{k \uparrow \infty} \sum_{n=1}^{k} \sum_{i=1}^{N_{t}^{(n)}} \xi_{i}^{(n)}$$
(19)

On account of the assumption  $\Pi(-\infty, 0) = 0$ , all the jumps  $\xi_i^{(n)}$  are nonnegative. Hence, it is also a necessary condition that

$$-a - \int_{(0,1)} x \Pi(\mathrm{d}x) \ge 0 \tag{20}$$

for  $X$  to have nondecreasing paths. These necessary conditions are also sufficient.

#### Lévy Processes as Semimartingales

Recall that a semimartingale with respect to a given filtration  $\mathbb{F} := \{ \mathcal{F}_t : t > 0 \}$  is defined as the sum of an F-local martingale and an F-adapted process of bounded variation. The importance of semimartingales is that they form a natural class of stochastic processes with respect to which one may construct a stochastic integral and thereafter perform calculus. Moreover, the theory of stochastic calculus plays a significant role in mathematical finance as it can be used as a key ingredient in justifying the pricing and hedging of derivatives in markets where risky assets are modeled as positive semimartingales.

A popular choice of model for risky assets in recent years has been the exponential of a Lévy process (see Exponential Lévy Models). Lévy processes have also been used as building blocks in more complex stochastic models for prices, such as stochastic

volatility models with jumps (see Barndorff-Nielsen and Shephard (BNS) Models) and time-changed Lévy models (see **Time-changed Lévy Process**). The monograph of Cont and Tankov [4] gives an extensive exposition on these types of models. Thanks to Itô's formula for semimartingales, the exponential of a Lévy process is a semimartingale when it can be shown that a Lévy process is a semimartingale. However, reconsidering equation (10) and recalling that  $B^{\Sigma}$  and  $\lim_{k\uparrow\infty}\sum_{n=1}^{k}X^{(n)}$  are martingales and that  $X^{(0)} - a \cdot$  is an adapted process with bounded variation paths, it follows immediately that any Lévy process is a semimartingale.

# References

- Bachelier, L. (1900). Théorie de la spéculation, Annales [1] Scientifiques de lÉcole Normale Supérieure 17, 21–86.
- Bachelier, L. (1901). Théorie mathematique du jeu, [2] Annales Scientifiques de lÉcole Normale Supérieure 18, 143-210.
- [3] Bertoin, J. (1996). Lévy Processes, Cambridge University Press, Cambridge.
- Cont, R. & Tankov, P. (2004). Financial Modelling [4] with Jump Processes, Financial Mathematics Series, Chapman & Hall/CRC.
- Itô, K. (1942). On stochastic processes. I. (Infinitely [5] divisible laws of probability), Japanese Journal of Mathematics 18,  $261-301$ .

- Khintchine, A. (1937). A new derivation of one formula [6] by Levy P., Bulletin of Moscow State University  $I(1)$ ,  $1 - 5$
- Kolmogorov, N.A. (1932). Sulla forma generale di un [7] processo stocastico omogeneo (un problema di B. de Finetti), Atti Reale Accademia Nazionale dei Lincei Rend 15, 805-808.
- [8] Lévy, P. (1934). Sur les intégrales dont les éléments sont des variables aléatoires indépendantes, Annali della Scuola Normale Superiore di Pisa 3-4, 217-218, 337-366.
- [9] Lundberg, F. (1903). Approximerad framställning av sannolikhetsfunktionen, Återförsäkring av kollektivrisker, Akademisk Afhandling Almqvist och Wiksell, Uppsala.
- Sato, K. (1999). Lévy Processes and Infinitely Divisible  $[10]$ Distributions, Cambridge University Press, Cambridge.

#### **Related Articles**

Generalized Hyperbolic Models; Infinite Divisibility; Jump Processes; Lévy Copulas; Normal Inverse Gaussian Model: Poisson Process: Stochastic Exponential; Tempered Stable Process; Timechanged Lévy Process; Variance-gamma Model.

ANDREAS E. KYPRIANOU
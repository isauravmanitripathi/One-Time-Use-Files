# Martingales

The word *martingale* originated from Middle French. It means a device for steadying a horse's head or checking its upward movement. In eighteenthcentury France, *martingale* also referred to a class of betting strategies in which a player increases the stake usually by doubling each time a bet is lost. The word "martingale", which appeared in the official dictionary of the Academy in 1762 (in the sense of a strategy) means "a strategy that consists in betting all that you have lost". See [7] for more about the origin of martingales. The simplest version of the martingale betting strategies was designed to beat a fair game in which the gambler wins his stake if a coin comes up heads and loses it if the coin comes up tails. The strategy had the gambler keep doubling his bet until the first head eventually occurs. At this point, the gambler stops the game and recovers all previous losses, besides winning a profit equal to the original stake. Logically, if a gambler is able to follow this "doubling strategy" (in French, it is still referred to as la martingale), he would win sooner or later. But in reality, the exponential growth of the bets would bankrupt the gambler quickly. It is Doob's optional stopping theorem (the cornerstone of martingale theory) that shows the impossibility of successful betting strategies.

In probability theory, a *martingale* is a stochastic process (a collection of random variables) such that the conditional expectation of an observation at some future time  $t$ , given all the observations up to some earlier time  $s < t$ , is equal to the observation at that earlier time  $s$ . The name "martingale" was introduced by Jean Ville  $(1910-1989)$  as a synonym of "gambling system" in his book on "collectif" in the Borel collection, 1938. However, the concept of martingale was created and investigated as early as in 1934 by Paul Pierre Lévy (1886–1971), and a lot of the original development of the theory was done by Joseph Leo Doob (1910-2004). At present, the martingale theory is one of the central themes of modern probability. It plays a very important role in the study of stochastic processes. In practice, a martingale is a model of a fair game. In financial markets, a fair game means that there is no arbitrage. Mathematical finance builds the bridge that connects no-arbitrage arguments and martingale theory. The fundamental theorem (principle) of asset pricing states, roughly

speaking, that a mathematical model for stochastic asset prices  $X$  is free of arbitrage if and only if  $X$ is a martingale under an equivalent probability measure. The fair price of a *contingent claim* associated with those assets  $X$  is the expectation of its payoff under the martingale equivalent measure (risk neutral measure).

Martingale theory is a vast field of study, and this article only gives an introduction to the theory and describes its use in finance. For a complete description, readers should consult texts such as [4, 13] and [6].

#### **Discrete-time Martingales**

A (finite or infinite) sequence of random variables  $X = \{X_n | n = 0, 1, 2, \ldots\}$  on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  is called a discrete-time *martingale* (respectively, *submartingale*, *supermartingale*) if for all  $n = 0.1.$ 

2, ...,  $\mathbb{E}[|X_n|] < \infty$  and

$$\mathbb{E}\Big[X_{n+1}\Big|X_0, X_1, \dots, X_n\Big] = X_n$$
  
(respectively  $\ge X_n, \le X_n$ ) (1)

By the tower property of conditional expectations, equation  $(1)$  is equivalent to

$$\mathbb{E}\Big[X_n \Big| X_0, X_1, \dots, X_k\Big] = X_k$$
  
(respectively  $\ge X_k, \le X_k$ ), for any  $k \le n$  (2)

Obviously, X is a submartingale if and only if  $-X$ is a supermartingale. Every martingale is also a submartingale and a supermartingale; conversely, any stochastic process that is both a submartingale and a supermartingale is a martingale. The expectation  $\mathbb{E}[X_n]$  of a martingale X at time n, is a constant for all  $n$ . This is one of the reasons that in a fair game, the asset of a player is supposed to be a martingale. For a supermartingale X,  $\mathbb{E}[X_n]$ is a nonincreasing function of  $n$ , whereas for a submartingale  $X$ ,  $\mathbb{E}[X_n]$  is a nondecreasing function of  $n$ . Here is a mnemonic for remembering which is which: "Life is a supermartingale; as time advances, expectation decreases." The conditional expectation of  $X_n$  in equation (2) should be evaluated on the basis of *all* information available up to time  $k$ , which can be summarized by a  $\sigma$ -algebra  $\mathcal{F}_k$ ,

$$\mathcal{F}_k = \{\text{all events occurring at times} \}$$
  
 
$$i = 0, 1, 2, \dots, k\}$$
(3)

A sequence of increasing  $\sigma$ -algebras  $\{\mathcal{F}_n | n = 0, 1,$ 2,...}, that is,  $\mathcal{F}_k \subseteq \mathcal{F}_n \subseteq \mathcal{F}$  for  $k \leq n$ , is called a *filtration*, denoted by  $\mathbb{F}$ . When  $\mathcal{F}_n$  is the smallest  $\sigma$ -algebra containing all the information of X up to time *n*,  $\mathcal{F}_n$  is called the  $\sigma$ -algebra generated by  $X_0, X_1, \ldots, X_n$ , denoted by  $\sigma\{X_0, X_1, \ldots, X_n\}$ , and  $\mathbb{F}$  is called the *natural filtration* of X. For another sequence of random variables  $\{Y_k | k = 0, 1, \ldots\}$ , let  $\mathcal{F}_k = \sigma\{Y_0, Y_1, \dots, Y_k\}, \text{ then } \mathbb{E}[X_n | Y_0, Y_1, \dots, Y_k] =$  $\mathbb{E}[X_n|\mathcal{F}_k].$ 

A sequence of random variables  $X = \{X_n | n =$  $[0, 1, 2, \ldots]$  on the filtered probability space  $(\Omega, \mathcal{F}, \mathcal{F})$  $\mathbb{F}, \mathbb{P}$ ) is said to be *adapted* if  $X_n$  is  $\mathcal{F}_n$ -measurable for each *n*, which means that given  $\mathcal{F}_n$ , there is no randomness in  $X_n$ . An adapted X is called a discrete-time martingale (respectively submartingale, *supermartingale*) with respect to the filtration  $\mathbb{F}$ , if for each n,  $\mathbb{E}[|X_n|] < \infty$ , and

$$\mathbb{E}[X_n|\mathcal{F}_k] = X_k \quad \text{(respectively } \ge X_k, \quad \le X_k),$$
  
for any  $k < n$  (4)

**Example 1** (Closed Martingales). Let  $Z$  be a random variable with  $\mathbb{E}|Z| < \infty$ , then for any filtration  $\mathbb{F} = (\mathcal{F}_n), X_n = \mathbb{E}[Z|\mathcal{F}_n]$  is a martingale (also called a *martingale closed by*  $Z$ ). Conversely, for any martingale  $X$  on a finite probability space, there exists a random variable Z such that  $X_n = \mathbb{E}[Z|\mathcal{F}_n]$ .

Example 2 (Partial Sums of i.i.d. Random Vari**ables**). Let  $Z_1, Z_2, \ldots$  be a sequence of independent, identically distributed (i.i.d.) random variables such that  $\mathbb{E}[Z_n] = \mu$ , and  $\mathbb{E}[Z_n^2] = \sigma^2 < \infty$ , and that the moment generating function  $\phi(\theta) = \mathbb{E}[\theta^{Z_1}]$ exists for some  $\theta > 0$ . Let  $S_n$  be the partial sum,  $S_n = Z_1 + \cdots + Z_n$ , also called a *random walk*. Let  $\mathcal{F}_n = \sigma\{Z_1,\ldots,Z_n\}$ . Then

$$S_n - n\mu, \quad (S_n - n\mu)^2 - n\sigma^2, \quad \frac{\theta^{S_n}}{[\phi(\theta)]^n} \qquad (5)$$

are all martingales. If  $\mathbb{P}(Z_k = +1) = p$ ,  $\mathbb{P}(Z_k =$  $-1$  =  $q = 1 - p$ , then  $S_n$  is called a *simple* random

walk and  $(q/p)^{S_n}$  is a martingale since  $\phi(p/q) = 1$ ; in particular, when  $p = q = 1/2$ ,  $S_n$  is called a simple symmetric random walk. If  $Z_k$  has the Bernoulli distribution,  $\mathbb{P}(Z_k = +1) = p$ ,  $\mathbb{P}(Z_k =$  $0 = q = 1 - p$ , then  $S_n$  has the binomial distribution  $(n, p)$ , and  $(q/p)^{2S_n-n}$  is a martingale since  $\phi([q/p]^2) = q/p.$ 

Example 3 (Polya's Urn). An urn initially contains  $r$  red and  $b$  blue marbles. One is chosen randomly. Then it is put back together with another one of the same color. Let  $X_n$  be the number of red marbles in the urn after  $n$  iterations of this procedure, and let  $Y_n = X_n/(n + r + b)$ . Then the sequence  $Y_n$ is a martingale.

**Example 4** (A Convex Function of Martingales). By Jensen's inequality, a convex function of a martingale is a submartingale. Similarly, a convex and nondecreasing function of a submartingale is also submartingale. Examples of convex functions are  $\max(x-k,0)$  for constant k,  $|x|^p$  for  $p\geq 1$  and  $e^{\theta x}$ for constant  $\theta$ .

**Example 5** (Martingale Transforms). Let  $X$  be a martingale with respect to the filtration  $\mathbb{F}$  and  $H$  be a *predictable process* with respect to  $\mathbb{F}$ , that is,  $H_n$ is  $\mathcal{F}_{n-1}$ -measurable for  $n \geq 1$ , where  $\mathcal{F}_0 = \{\emptyset, \Omega\}$ . A martingale transform of  $X$  by  $H$  is defined by

$$\left(H \cdot X\right)_n = H_0 X_0 + \sum_{i=1}^n H_i (X_i - X_{i-1}) \quad (6)$$

where the expression  $H \cdot X$  is the discrete analog of the stochastic integral  $\int H \, dX$ . If  $\mathbb{E}|(H \cdot X)_n| < \infty$ for  $n > 1$ , then  $(H \cdot X)_n$  is a martingale with respect to  $\mathbb{F}$ . The interpretation is that in a fair game X, if we choose our bet at each stage on the basis of the prior history, that is, the bet  $H_n$  for the *n*th gamble only depends on  $\{X_0, X_1, \ldots, X_{n-1}\}$ , then the game will continue to be fair. If  $X_n$  is the asset price at time *n* and  $H_n$  is the number of shares of the assets held by the investor during the time period from time  $n$ until time  $n + 1$ , more precisely, for the time interval  $[n, n + 1)$ , then  $(H \cdot X)_n$  is the total gain (or loss) up to time  $n$  (the value of the portfolio at time  $n$  with the trading strategy  $H$ ).

A random variable  $T$  taking values in  $\{0, 1, 2,$  $\ldots; \infty$  is a *stopping time T* with respect to a filtration  $\mathbb{F} = \{ \mathcal{F}_n \mid n = 0, 1, 2, \ldots \}$ , if for each *n*, the event  $\{T = n\}$  is  $\mathcal{F}_n$ -measurable, or equivalently, the event  $\{T \le n\}$  is  $\mathcal{F}_n$ -measurable. If S and T are stopping times, then  $S + T$ ,  $S \vee T = \max(S, T)$ , and  $S \wedge T = \min(S, T)$  are all stopping times. Particularly,  $T \wedge n$  is a bounded stopping time for any fixed time *n*.  $X_n^T =: X_{T \wedge n}$  is said to be the *process* **X** stopped at  $\ddot{T}$ , since on the event  $\{\omega | T(\omega) = k\}$ ,  $X_n^T = X_k$  for  $n = k, k + 1, \ldots$ 

# Doob's Optional Stopping Theorem

Let  $X$  be a martingale and  $T$  be a bounded stopping time with respect to the same filtration  $\mathbb{F}$ , then  $\mathbb{E}[X_T] = \mathbb{E}[X_0]$ . Conversely, for an adapted process X, if  $\mathbb{E}[|X_T|] < \infty$  and  $\mathbb{E}[X_T] = \mathbb{E}[X_0]$  hold for all bounded stopping time  $T$ , then  $X$  is a martingale. This theorem says roughly that stopping a martingale at a stopping time  $T$  does not alter its expectation, provided that the decision when to stop is based only on information available up to time  $T$ . The theorem also shows that a martingale stopped at a stopping time is still a martingale, and there is no way to be sure to win in a fair game if the stopping time is bounded.

#### **Continuous-time Martingales**

A continuous-time stochastic process  $X$  on filtered probability space  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  is a collection of random variables  $X = \{X_t : 0 < t < \infty\}$ , where  $X_t$ is a random variable observed at time t, and the filtration  $\mathbb{F} = \{ \mathcal{F}_t : 0 \le t \le \infty \}$ , which is a family of increasing  $\sigma$ -algebras,  $\mathcal{F}_s \subseteq \mathcal{F}_t \subseteq \mathcal{F}$  for  $s \leq t$ . A process *X* is said to be *adapted* if  $X_t$  is  $\mathcal{F}_t$  measurable for each  $t$ . A random variable  $T$  taking values in  $[0, \infty]$  is called a *stopping time*, if the event  $\{T \le t\}$ is  $\mathcal{F}_t$  measurable for each t. The stopping time  $\sigma$ *algebra*  $\mathcal{F}_T$  is defined to be  $\mathcal{F}_T = \{A \in \mathcal{F} \mid A \cap \{T \leq T\}$  $t \in \mathcal{F}_t$ , all  $t \ge 0$ , which represents the information up to the stopping time  $T$ .

A real-valued, adapted process  $X$  is called a continuous-time *martingale* (respectively *supermartingale*, *submartingale*) with respect to the filtration  $\mathbb{F}$  if

1.  $\mathbb{E}[|X_t|] < \infty$ , for  $t > 0$ (7)

2. 
$$\mathbb{E}[X_t|\mathcal{F}_s] = X_s \text{ (respectively } \leq X_s, \geq X_s),$$

a.s. for any 
$$0 \le s \le t$$
 (8)

Continuous-time martingales have the same properties as discrete-time martingales. For example, Doob's optional stopping theorem says that for a martingale  $X_t$  with right continuous paths, which is closed in  $\mathbf{L}^1$  by a random variable  $X_{\infty}$ , we have

$$\mathbb{E}[X_T|\mathcal{F}_S] = X_S \quad \text{a.s. for any two stopping times} 0 < S < T \tag{9}$$

The most important continuous-time martingale is Brownian motion, which was named for the Scottish botanist Robert Brown, who, in 1827, observed ceaseless and irregular movement of pollen grains suspended in water. It was studied by Albert Einstein in 1905 at the level of modern physics. Its mathematical model was first rigorously constructed in 1923 by Norbert Wiener. Brownian motion is also called a Wiener process. The Wiener process gave rise to the study of continuous-time martingales, and has been an example that helps mathematicians to understand stochastic calculus and diffusion processes.

It was Louis Bachelier (1870-1946), now recognized as the founder of mathematical finance (see [9]), who first, in 1900, used Brownian motion  $B$  to model short-term stock prices  $S_t$  at a time t in financial markets, that is,  $S_t = S_0 + \sigma B_t$ , where  $\sigma > 0$  is a constant. Now we can see that if Brownian motion B is defined on  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ , then the price process S is a martingale under the probability measure  $\mathbb{P}$ .

In 1965, the American economist Paul Samuelson rediscovered Bachelier's ideas and proposed the geometric Brownian motion  $S_0 \exp\{(\mu - (\sigma^2/2))t +$  $\sigma B_t$  as a model for long-term stock prices  $S_t$ . That is,  $S_t$  follows the stochastic differential equation (SDE):  $dS_t = \mu S_t dt + \sigma S_t dB_t$ . From this simple structure, we get the famous Black-Scholes option price formulas for European calls and puts. This SDE is now called the Black-Scholes equation (model). Contrary to Bachelier's setting, the price process  $S$  is not a martingale under  $\mathbb{P}$ . However, by Girsanov's theorem, there is a unique probability measure  $\mathbb{Q}$ , which is equivalent to  $\mathbb{P}$ , such that the discounted stock price  $e^{-rt}S_t$  is a martingale under  $\mathbb{Q}$  for  $0 \le t \le T$ , where r is the riskless rate of interest, and  $T > 0$  is a fixed constant.

The reality is not as simple as the above linear SDE. A simple generalization is  $dS_t = \mu(t, S_t) dt +$  $\sigma(t, S_t)$  dB<sub>t</sub>. If one believes that risky asset prices have jumps, an appropriate model might be

$$dS_t = \mu(t, S_t) dt + \sigma(t, S_t) dB_t + J(t, S_t) dN_t$$
(10)

where N is a Poisson process with intensity  $\lambda$ ,  $J(t, S_t)$  refers to the jump size, and N indicates when the jumps occur. Since  $N$  is a counting (pure jump) process with independent and stationary increments, both  $N_t - \lambda t$  and  $(N_t - \lambda t)^2 - \lambda t$  are martingales. For a more general model, we could replace  $N$  by a Lévy process that includes the Brownian motion and Poisson process as special cases.

Under these general mathematical models, it becomes hard to turn the fundamental principle of asset pricing into a precise mathematical theorem: the absence of arbitrage possibilities for a stochastic process S, a *semimartingale* defined on  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ , is equivalent to the existence of an equivalent measure  $\mathbb{Q}$ , under which S is a *local martingale*, sometimes, a sigma martingale. See [2] or [3].

# **Local Martingales and Finite Variation** Processes

There are two types of processes with only jump discontinuities. A process is said to be càdlàg if it almost surely (a.s.) has sample paths that are right continuous, with left limits. A process is said to be *càglàd* if it almost surely has sample paths that are left continuous, with right limits. The words càdlàg and càglàd are acronyms from the French for *continu* à droite, limites à gauche, and continu à gauche, *limites à droite*, respectively. Let

 $\mathbb{D}$  = the space of adapted processes

with càdlàg paths

 $\mathbb{L}$  = the space of adapted processes

with càglàd paths 
$$(11)$$

An adapted, càdlàg process  $A$  is called a *finite variation* (FV) process if sup  $\sum_{i=1}^{N} |A_{t_i} - A_{t_{i-1}}|$  is bounded almost surely for each constant  $t > 0$ , where the supremum is taken over the set of all partitions  $0 = t_0 \le t_1 \le \cdots \le t_N = t$ . An FV process is a difference of two increasing processes. Although the Brownian motion  $B$  has continuous paths, it has paths of *infinite variation* on  $[0, t]$ , which prevents us from defining the stochastic integral  $\int H \, dB$  as a Riemann-Stieltjes integral, path by path.

An adapted, càdlàg process  $M$  is called a *local martingale* with respect to a filtration  $\mathbb{F}$  if there exists a sequence of increasing stopping time  $T_n$ with  $\lim_{n\to\infty} T_n = \infty$  almost surely, such that for each  $n$ ,  $M_{t \wedge T_n}$  is a martingale. A similar concept is that a function is *locally bounded*: for example,  $1/t$  is not bounded over  $(0, 1]$ , but it is bounded on the interval  $[1/n, 1]$  for any integer n. A process moving very rapidly though with continuous paths, or jumping unboundedly and frequently, might not be a martingale. However, we could modify it to be a martingale by stopping it properly, that is, it is a martingale up to a stopping time, but may not be a martingale for all time.

The class of local martingales includes martingales as special cases. For example, if for every  $t >$ 0,  $\mathbb{E}\{\sup_{s\leq t}|M_{s}|\}<\infty$ , then *M* is a martingale; if for all  $t > 0$ ,  $\mathbb{E}\{[M, M]_t\} < \infty$ , then M is a martingale, and  $\mathbb{E}\{M_t^2\} = \mathbb{E}\{[M, M]_t\}$ . Conversely, if M is a martingale with  $\mathbb{E}\{M_t^2\} < \infty$  for all  $t > 0$ , then  $\mathbb{E}\{[M, M]_t\} < \infty$  for all  $t > 0$ . For the definition of quadratic variation  $[M, M]_t$ , see equation (14) in the next section.

Not all local martingales are martingales. Here is a typical *example* of a local martingale, but not a martingale. Lots of continuous-time martingales, supermartingales, and submartingales can be constructed from Brownian motion, since it has independent and stationary increments and it can be approximated by a random walk. For example, let  $B$  be a standard Brownian motion in  $\mathbb{R}^3$  with  $B_0 = x \neq 0$ . Let  $u(y) = ||y||^{-1}$ , be a *superharmonic* function on  $\mathbb{R}^3$ .  $M_t = u(B_t)$  is a positive supermartingale. Since  $\lim_{t\to\infty}\sqrt{t}\ \mathbb{E}\{M_t\}=\sqrt{\pi}$  and  $\mathbb{E}\{M_0\}=u(x), M$  does not have constant expectations and it cannot be a martingale.  $M$  is known as the inverse Bessel Process. For each n, we define a stopping time  $T_n =$  $\inf\{t>0: \|B_t\| < 1/n\}$ . Since the function u is har*monic* outside of the ball of radius  $1/n$  centered at the origin, the process  $\{M_{t \wedge T_n} : t \ge 0\}$  is a martingale for each  $n$ . Therefore,  $M$  is a local martingale.

# Semimartingales and Stochastic Integrals

Today stocks and bonds are traded globally almost 24 hours a day, and online trading happens every second. When trading takes place almost continuously, it is simpler to use a continuous-time stochastic processes to model the price  $X$ . The value of the portfolio at time  $t$  with the continuous-time trading strategy  $H$  becomes the limit of sums as shown in the martingale transform  $(H \cdot X)_n$  in equation (6), that is, the stochastic integral  $\int_0^t H_s \, dX_s$ . Stochastic calculus is more complicated than regular calculus because  $X$ can have paths of infinite variation, especially when  $X$  has unbounded jumps, for example, when  $X$  is Brownian motion, a continuous-time martingale, or a local martingale. For stochastic integration theory, see **Stochastic Integrals** or consult [8, 11] and [12], and other texts.

Let  $0 = T_1 \leq \cdots \leq T_{n+1} < \infty$  be a sequence of stopping times and  $H_i \in \mathcal{F}_{T_i}$  with  $|H_i| < \infty$ . A process  $H$  with a representation

$$H_{t} = H_{0}\mathbf{1}_{\{0\}}(t) + \sum_{i=1}^{n} H_{i}\mathbf{1}_{(T_{i}, T_{i+1})}(t)$$
(12)

is called a *simple predictable process*. A collection of simple predictable processes is denoted by  $S$ . For a process  $X \in \mathbb{D}$  and  $H \in \mathbb{S}$  having the representation  $(12)$ , we define a linear mapping as the martingale transforms in equation (6) in the discretetime case

$$(H \cdot X)_t = H_0 X_0 + \sum_{i=1}^n H_i (X_{t \wedge T_{i+1}} - X_{t \wedge T_i}) \quad (13)$$

If for any  $H \in \mathbf{S}$  and each  $t \geq 0$ , the sequence of random variables  $(H^n \cdot X)_t$  converges to  $(H \cdot$  $(X)_t$  in probability, whenever  $H^n \in \mathbf{S}$  converges to  $H$  uniformly, then  $X$  is called a *semimartingale*. For example, an FV process, a local martingale with continuous paths, and a Lévy process are all semimartingales.

Since the space **S** is dense in  $\mathbb{L}$ , for any  $H \in \mathbb{L}$ , there exists  $H_n \in \mathbf{S}$  such that  $H_n$  converges to  $H$ . For a semimartingale X and a process  $H \in \mathbb{L}$ , the *stochastic integral*  $\int H \, dX$ , also denoted by  $(H \cdot X)$ , is defined by  $\lim_{n\to\infty}(H^n\cdot X)$ . For any  $H\in\mathbb{L},\ H\cdot X$ is a semimartingale, it is an FV process if  $X$  is, and it is a local martingale if X is. But  $H \cdot X$  may not be a martingale even if  $X$  is.  $H \cdot X$  is a martingale if X is a local martingale and  $\mathbb{E}\{\int_0^t H_s^2 d[X,X]_s\} < \infty$ for each  $t > 0$ .

For a semimartingale  $X$ , its *quadratic variation*  $[X, X]$  is defined by

$$[X, X]_t = X_t^2 - 2 \int_0^t X_{s-} \, \mathrm{d} X_s \tag{14}$$

where  $X_{s-}$  denotes the left limit at s. Let  $[X, X]^c$ denote the path-by-path continuous part of  $[X, X]$ , and  $\Delta X_s = X_s - X_{s-}$  be the jump of X at s, then  $[X, X]_t = [X, X]_t^c + \sum_{0 \le s \le t} (\Delta X_s)^2$ . For an FV process  $X$ ,  $[X, X]_t = \sum_{0 \le s \le t} (\bar{\Delta}X_s)^2$ . In particular, if  $X$  is an FV process with continuous paths, then  $[X, X]_t = X_0^2$  for all  $t \ge 0$ . For a continuous local martingale X, then  $X^2 - [X, X]_t$  is a continuous local martingale. Moreover, if  $[X, X]_t = X_0^2$  for all t, then  $X_t = X_0$  for all t; in other words, if an FV process is also a continuous local martingale, then it is a constant process.

# Lévy's Characterization of Brownian Motion

A process  $X$  is a standard Brownian motion if and only if it is a continuous local martingale with  $[X, X]_t = t.$ 

The theory of stochastic integration for integrands in  $\mathbb{L}$  is sufficient to establish Itô's formula, the Girsanov-Meyer theorem, and to study SDEs. For example, the *stochastic exponential* of a semimartingale  $X$ with  $X_0 = 0$ , written  $\mathcal{E}(X)$ , is the unique semimartingale Z that is a solution of the linear SDE:  $Z_t =$  $1 + \int_0^t Z_{s-} dX_s$ . When X is a continuous local martingale, so is  $\mathcal{E}(X)_t = \exp\{X_t - \frac{1}{2}[X,X]_t\}$ . Furthermore, if *Kazamaki's Criterion* sup<sub>T</sub>  $\mathbb{E}\{\exp(\frac{1}{2}X_T)\}\$  $\infty$  holds, where the supremum is taken over all bounded stopping times, or if *Novikov's Criterion*  $\mathbb{E}\{\exp(\frac{1}{2}[X,X]_{\infty})\} < \infty$  holds (stronger but easier to check in practice), then  $\mathcal{E}(X)$  is a martingale. See [10] for more on these conditions. When  $X$  is Brownian motion,  $\mathcal{E}(X) = \exp\{X_t - \frac{1}{2}t\}$  is referred to as geometric Brownian motion.

The space of integrands  $\mathbb{L}$  is not general enough to have *local times* and martingale representation theory, which is essential for hedging in finance. On the basis of the *Bichteler–Dellacherie theorem*,  $X$  is a semimartingale if and only if  $X = M + A$ , where M is a local martingale and  $A$  is an FV process, we can extend the stochastic integration from  $\mathbb{L}$  to the space  $\mathcal{P}$  of predictable processes, which are measurable with respect to  $\sigma\{H: H \in \mathbb{L}\}$ . For a semimartingale  $X$ , if a predictable  $H$  is  $X$  integrable, that is, we can define the stochastic integral  $H \cdot X$ , then we write  $H \in L(X)$  (see chapter 4 of [8]). If  $H \in \mathcal{P}$ is locally bounded then  $H \in L(X)$  and  $H \cdot X$  is a local martingale if X is. However, if  $H \in \mathcal{P}$  is not locally bounded or  $H \notin \mathbb{L}$ , then  $H \cdot X$  may not be a local martingale even if X is an  $L^2$  martingale. For such an example due to M. Émery, see pp 152 of [5] or pp 176 of [8]. If  $X$  is a local martingale and  $H \in L(X)$ , then  $H \cdot X$  is a sigma martingale.

### **Sigma Martingales**

The concept of a sigma martingale was introduced by Chou [1] and further analyzed by Émery [5]. It has seen a revival in popularity owing to Delbaen and Schachermayer [2]; see [8] for a more detailed treatment. Sigma martingales relate to martingales analogously as sigma-finite measures relate to finite measures. A sigma martingale, which may not be a local martingale, has the essential features of a martingale.

A semimartingale  $X$  is called a *sigma martingale* if there exists a martingale  $M$  and a nonnegative  $H \in \mathcal{P}$  such that  $X = H \cdot M$ , or, equivalently, if there exists a nonnegative  $H \in \mathcal{P}$  such that  $H \cdot X$  is a martingale.

A local martingale is a sigma martingale, but a sigma martingale with large jumps might fail to be a local martingale. If  $X$  is a sigma martingale and if either  $\sup_{s \le t} |X_s|$  or  $\sup_{s \le t} |\Delta X_s|$  is *locally integrable* (for example,  $X$  has continuous paths or bounded jumps), then  $X$  is a local martingale. If  $X$  is a sigma martingale and  $H \in L(X)$ , then  $H \cdot X$  is always a sigma martingale.

The concept of a sigma martingale is new in the context of mathematical finance. It was introduced to deal with possibly unbounded jumps of the asset price process  $X$ . When we consider the process  $X$  with jumps, it is often convenient to assume the jumps to be unbounded, for example, the Lévy processes and the family of ARCH, GARCH processes. If the conditional distribution of jumps is Gaussian, then the process is not locally bounded. In that case, the concept of a sigma martingale is unavoidable. On the other hand, if we are only interested in how to price and hedge some contingent claims, not the underlying assets  $X$ , then it might not be necessary to require the asset price  $X$  to be a (local) martingale

and it suffices to require  $H \cdot X$  to be a martingale for some  $H$ , that is,  $X$  is a sigma martingale. Moreover, nonnegative sigma martingales are local martingales, so in particular for stock prices, we do need to consider sigma martingales.

Finally, we cite two fundamental theorems of asset *pricing* from chapters 8 and 14 of [3] to see why we need sigma martingales in mathematical finance.

**Theorem 1** Let the discounted price process S be *a locally bounded semimartingale defined on*  $(\Omega,$  $\mathcal{F}, \mathbb{F}, \mathbb{P})$ . Then there exists a probability measure  $\mathbb{Q}$ (equivalent to  $\mathbb{P}$ ) under which S is a local martingale, if and only if  $S$  satisfies the condition of no free lunch with vanishing risk (NFLVR).

Here the concept of NFLVR is a mild strengthening of the concept of no arbitrage, which is introduced by Delbaen and Schachermayer in [2].

**Theorem 2** If we assume that  $S$  is a nonlocally bounded semimartingale, then we have a general theorem by replacing the term "local martingale" by the term "sigma martingale" in Theorem 1 above. However if  $S \ge 0$ , then "local martingale" suffices, because sigma martingales bounded below are a priori local martingales.

## Conclusion

A local martingale is a martingale up to a sequence of stopping times that goes to  $\infty$ , while a sigma martingale is a countable sum (a mixture) of martingales.

#### References

- $[1]$ Chou, C.S. (1977). Caractérisation d'une classe de semimartingales, Séminaire de Probabilit és XIII, LNM, Vol. 721, Springer, pp. 250-252.
- [2] Delbaen, F. & Schachermayer, W. (1998). The Fundamental Theorem of Asset Pricing for Unbounded Stochastic Processes, Mathematicsche Annalen, Vol. 312, Springer, pp. 215-250.
- Delbaen, F. & Schachermayer, W. (2006). The Mathe-[3] matics of Arbitrage, Springer Finance Series, Springer-Verlag, New York.
- [4] Dellacherie, C. & Meyer, P.A. (1982). Probabilities and Potential, Vol. 29 of North-Holland Mathematics Studies, North-Holland, Amsterdam.
- [5] Émery, M. (1980). Compensation de processus à variation finie non localement int'egrales., Séminaire de Probabilités XIV, LNM, Vol. 784, Springer, pp. 152-160.
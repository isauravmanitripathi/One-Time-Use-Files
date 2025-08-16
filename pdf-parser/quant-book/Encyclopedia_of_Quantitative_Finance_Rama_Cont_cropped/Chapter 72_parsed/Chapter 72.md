# **Equivalent Martingale** Measures

The usual setting of mathematical finance is provided by a *d*-dimensional stochastic process  $S = (S_t)_{0 \le t \le T}$ based on and adapted to a filtered probability space  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{0 \le t \le T}, \mathbb{P}).$  This process S models the price evolution of  $d$  risky stocks, which is random.

To alleviate notation, we assume from the very beginning that these prices are denoted in discounted terms: fix a traded asset, the "bond", as numéraire and express stock prices  $S$  in units of this bond. This simple and classical technique allows us to dispense with discount factors in the formulae below (compare Section 2.1 in [6] for more details).

A central topic in mathematical finance is to decide whether there is a probability measure  $Q$ , equivalent to  $\mathbb{P}$ , such that S is a martingale under  $Q$ . This is the theme of the fundamental theorem of asset pricing (see Fundamental Theorem of Asset Pricing). Once we know that there exist equivalent martingale measures, they can be used to determine risk-neutral prices of derivative securities by taking expectations under these measures (see **Risk-neutral Pricing**), and to replicate, respectively, sub- or superreplicate, the derivative.

In fact, we were less precise in the previous paragraph (as is usual in this context) by requiring that  $S$  is a *martingale*. It turns out that some technical care is needed here, involving the notions of *local martingales* and, more generally, of *sigma*martingales. This article deals precisely with these technical variants of the concept of a martingale.

We start by giving precise definitions.

**Definition 1** An  $\mathbb{R}^d$ -valued stochastic process  $(S_t)_{0 \le t \le T}$  based on and adapted to  $(\Omega, \mathcal{F},$  $(\mathcal{F}_t)_{0 \le t \le T}$ ,  $\mathbb{P}$ ) is called a

(i) martingale if

$$\mathbb{E}[S_t|\mathcal{F}_u] = S_u, \quad 0 \le u \le t \le T \qquad (1)$$

(ii) local martingale if there exists a sequence  $(\tau_n)_{n=1}^{\infty}$  of  $[0,T] \cup \{+\infty\}$ -valued stopping times, increasing a.s. to  $\infty$ , such that the stopped processes  $S_t^{\tau_n}$  are all martingales, where

$$S_t^{\tau_n} = S_{t \wedge \tau_n}, \quad 0 \le t \le T \tag{2}$$

(iii) sigma-martingale if there is an  $\mathbb{R}^d$ -valued martingale  $M = (M_t)_{0 \le t \le T}$  and a predictable *M*-integrable  $\mathbb{R}_+$ -valued process  $\varphi$  such that  $S = \varphi \cdot M.$ 

The process  $\varphi \cdot M$  is defined as the stochastic integral in the sense of semimartingales. The-by now well understood—underlying theory was developed notably by the school of P.A. Meyer in Strasbourg  $[10-12]$ :

$$(\varphi \cdot M)_t = \int_0^t \varphi_u \, \mathrm{d}M_u, \quad 0 \le t \le T \qquad (3)$$

It is not obvious, but true, that a local martingale is a sigma-martingale, so that (i)  $\Rightarrow$  (ii)  $\Rightarrow$  (iii) holds true above, while the reverse implications fail to hold true as we discuss later.

Why is it necessary to introduce these generalizations of the concept of a martingale? Let us start with a familiar example of a martingale, namely, geometric Brownian motion

$$M_t = \exp\left[W_t - \frac{t}{2}\right], \quad t \ge 0 \tag{4}$$

where the process  $(W_t)_{t>0}$  is a standard Brownian motion.

Clearly,  $(M_t)_{t\geq 0}$  is a martingale (with reference to its natural filtration) when t ranges in  $[0, \infty[$ . But what happens if we include  $t = \infty$  into the time set? It is straightforward to verify that

$$M_{\infty} := \lim_{t \to \infty} M_t \tag{5}$$

exists a.s. and equals

$$M_{\infty} = 0 \tag{6}$$

Hence we may well define the continuous process  $(M_t)_{0 \le t \le \infty}$ ; this process is not a martingale any more as

$$1 = M_0 > \mathbb{E}[M_\infty] = 0 \tag{7}$$

In this example, the breakdown of the martingale property happens at  $t = \infty$ . However, it is purely formal to shift this problem to any other point  $T \in ]0, \infty[$ , for example,  $T = 1$ . Indeed, letting

$$\tilde{M}_t = M_{\tan\left(\frac{t\pi}{2}\right)}, \quad 0 \le t < 1\n$$

$$\n\tilde{M}_1 = M_\infty = 0 \tag{8}$$

we find a process  $(\tilde{M}_t)_{0 \le t \le 1}$ , having a.s. continuous paths, which fails to be a martingale. However, it is intuitively clear that "locally", that is, before t assumes the value 1, the process  $(\tilde{M}_t)_{0 \le t \le 1}$  is "something like a martingale". The good way to formalize this intuition is to find a "localizing" sequence of stopping times as in (ii) above. The canonical choice<sup>a</sup> is

$$\tau_n = \inf\{t \in [0, 1] : |\tilde{M}_t| \ge n\} \tag{9}$$

which is a  $[0, 1] \cup \{\infty\}$ -valued stopping time, if we define the infimum over the empty set to be equal to  $\infty$ . It is straightforward to verify that  $(\tau_n)_{n=1}^{\infty}$  satisfies the requirements of (ii) above.

In the above example it holds true that  $(\tilde{M}_t)_{0 \le t \le 1}$ is a martingale, that is, when  $t$  ranges in [0, 1]. In other words, the problem only arises at  $t = 1$ . However, there is a more subtle phenomenon in this context, where the problem not only appears at one single value of  $t$ , but also for all  $t$ .

The canonical example for this phenomenon is the inverse of the three-dimensional Bessel process $^{\rm b}$  $(R_t)_{0 \le t \le 1}$ . It may be defined by  $R_0 = 1$  and

$$dR_t = R_t^2 dW_t, \quad 0 \le t \le 1 \tag{10}$$

It turns out that equation  $(10)$  well defines a stochastic process with continuous paths, which is a local martingale (define  $(\tau_n)_{n=1}^{\infty}$  as in equation (9)). However, the function

$$t \to \mathbb{E}[R_t], \quad 0 \le t \le 1 \tag{11}$$

is *strictly decreasing* on the entire interval  $[0, 1]$ . Intuitively speaking, this may be interpreted as  $(R_t)_{0 \le t \le 1}$ "losing mass in continuous time". We leave it to the reader to develop his or her own intuition for this remarkable phenomenon. In any case, this example should convince the reader that the concept of *local martingales*, involving "localizing" sequences of stopping times, is a useful and natural notion.

To underline this claim even further, think of a diffusion process  $(X_t)_{0 \le t \le 1}$  satisfying the equation

$$dX_t = \sigma(X_t, t) dW_t + \mu(X_t, t) dt, \quad 0 \le t \le 1$$
(12)

A typical argument used, for example, in the derivation of the Black-Scholes partial differential equation (PDE) (compare Complete Markets or [Vol. II] [13]), goes as follows: for the drift term  $\mu(X_t, t)$  we have  $\mu(X_t, t) \equiv 0$  if and only if  $(X_t)_{0 \le t \le 1}$  is a martingale. This is a very useful argument. However, this argument is not quite complete, as a glance at equation  $(10)$  reveals where we only obtain a local martingale. The correct statement is the process  $X$  is a *local martingale* if and only if  $\mu(X_t, t) = 0$ , a.s. with respect to  $d\mathbb{P} \otimes d\lambda$ .

#### **Local Martingales in Finance**

As a concrete example of a local martingale modeling a price process we consider  $\tilde{S} = (\tilde{S}_t)_{0 \le t \le T} =$  $(\tilde{M}_t)_{0 \le t \le 1}$ , the time-changed geometric Brownian motion defined in equation (8). We consider  $\hat{S}$  to be defined on  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{0 \le t \le T}, \mathbb{P})$ , where the filtration  $(\mathcal{F}_t)_{0 \le t \le T}$  is generated by  $\tilde{S}$  and  $\mathcal{F} = \mathcal{F}_T$ . We conclude that  $Q = \mathbb{P}$  is the unique probability measure Q on  $\mathcal{F}$ , which is equivalent to  $\mathbb{P}$  and such that  $\tilde{S}$  is a local martingale under  $Q$ . This quickly follows from the fact that  $Q = \mathbb{P}$  is the unique probability measure on  $\mathcal{F}$ , equivalent to  $\mathbb{P}$ , such that the Brownian motion  $W = (W_t)_{0 \le t < \infty}$  in equation (4) is a martingale under  $O$ .

The question arises whether  $\hat{S}$  defines a sound, that is, arbitrage-free model of a financial market. At first glance, things seem suspicious; after all,  $(S_t)_{0 \le t \le T}$ , is a ridiculous stock; it starts at  $\tilde{S}_0 = 1$  and ends a.s. at  $S_T = 0$ . Hence buying a stock S and holding it up to time  $T = 1$  is a very "silly investment". M. Harrison and St. Pliska [8] called such an investment a *suicide* strategy. But it is not forbidden to be silly.

A much more appealing investment strategy would be to go short in the stock at time 0, and to hold this short position up to time  $T$ , as this strategy yields a.s. a gain of one Euro. However, unfortunately, this is forbidden. To understand why this is the case, let us recall from Fundamental Theorem of Asset Pricing the definition of *admissibility*: a trading strategy  $H =$  $(H_t)_{0 \le t \le T}$  for a (general semimartingale) stock price process  $S$  is defined as a predictable strategy, which is S-integrable. By definition, the stochastic integral

$$(H \cdot S)_t = \int_0^t (H_u, \mathrm{d}S_u), \quad 0 \le t \le T \qquad (13)$$

then is well defined. We call  $H$  *admissible*, if there is a constant  $C > 0$  such that a.s.

$$(H \cdot S)_t \ge -C, \quad 0 \le t \le T \tag{14}$$

The finite credit line  $C$  rules out doubling strategies and similar schemes that capitalize on taking higher and higher risks. A typical representative of such a "kind of doubling strategy" is the strategy of going short in the stock  $(S_t)_{0 \le t \le T}$ , which corresponds to taking  $H_t \equiv -1$ , for  $0 \le t \le T$ .

We now shall convince ourselves that local martingales yield sound, arbitrage-free models of financial markets. It turns out that it does not matter whether we start with a true martingale  $S = (S_t)_{0 \le t \le T}$  or with a local martingale  $S$ , if we are only interested in the *admissible stochastic integrals*  $H \cdot S$ . Indeed, it was shown by J.P. Ansel and C. Stricker [1, Corr. 3.5] that, given a local martingale  $S$  and an admissible integrand H, the stochastic integral  $H \cdot S$  is a local martingale and therefore (using once more the fact that  $H \cdot S$  is bounded from below) a supermartingale. In particular, the process  $H \cdot S$  cannot increase in expectation; but it may very well decrease in expectation as, for example, the process  $\tilde{S}$  above.

The following characterization of local martingales (see [4, Prop. 2.5] for more on this issue) is useful in this context.

**Proposition 1** For an  $\mathbb{R}^d$ -valued semimartingale S the following are equivalent.

- $(i)$  S is a local martingale.
- (ii)  $S = \varphi \cdot M$ , where M is an  $\mathbb{R}^d$ -valued martingale, and  $\varphi$  is an  $\mathbb{R}_+$ -valued, M-integrable, predictable, increasing process.

From this proposition and the trivial formula<sup>c</sup>

$$H \cdot M = \frac{H}{\varphi} \cdot (\varphi \cdot M) = \frac{H}{\varphi} \cdot S \tag{15}$$

which holds true for every  $\mathbb{R}^d$ -valued, predictable, *M*-integrable process  $H = (H_t)_{0 \le t \le T}$  we deduce that the family of processes, which are stochastic integrals on the local martingale  $S$  coincides with the family of processes, which are stochastic processes on the martingale  $M$ . Also note that  $H$  is admissible for  $M$ if and only if  $\frac{H}{\omega}$  is admissible for S.

The bottom line of formula  $(15)$  is that *there is* no difference between the stock price process S and  $M$  in *Proposition 1* if we are only interested in the *admissible stochastic integrals* on these processes: these two families of stochastic integrals coincide.

## **Sigma-martingales**

For continuous stock price processes  $S$  or, more generally, for locally bounded processes  $S$ , the concept of *local martingales* is sufficiently general to characterize those models that satisfy the condition of no free lunch with vanishing risk (see **Fundamental** Theorem of Asset Pricing).

However, if we pass to processes  $S$  that are not locally bounded any more, we still need one more step of generalization. The key concept for doing so was introduced by C. Chou [2] and M. Émery [7] under the name of "semimartingale de la classe  $(\sum_{m})$ ". In [4], F. Delbaen and this author took the liberty of calling these processes sigma-martingales S. The reason for this is that their relation to martingales is analogous to the relation between sigmafinite measures and finite measures, as seen from Definition 1 above. Also note the (only) difference between Definition 1 (iii) of a sigma-martingale, and the characterization of a local martingale as given in Proposition 1: in the latter the predictable,  $\mathbb{R}_+$ -valued process  $\varphi$  is supposed to be *increasing* while there is no such restriction in the former one.

Here is the illuminating example, due to M. Émery [7] (compare [4, Ex. 2.2]), of the archetypical sigmamartingale, which fails to be a local martingale.

**Example 1** We start with an exponentially distributed random variable  $\tau$  and an independent Bernoulli random variable  $\varepsilon$ , that is,  $\mathbb{P}[\varepsilon = 1] =$  $\mathbb{P}[\varepsilon=-1]=\frac{1}{2}$ . These random variables are based on some probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ .

Define the process  $M = (M_t)_{t>0}$  by

$$M_t = \begin{cases} 0, & \text{for} \quad 0 \le t \le \tau \\ \varepsilon, & \text{for} \quad \tau \le t \end{cases} \tag{16}$$

The verbal description goes like this: the process *M* remains at zero until time  $\tau$ ; then a coin is flipped, independently of  $\tau$ , and the process *M* continues at the level  $+1$  or  $-1$ , according to the result of this coin flip.

Denoting by  $(\mathcal{F}_t)_{t\geq 0}$  the filtration generated by  $(M_t)_{t>0}$ , it is rather obvious that  $(M_t)_{t>0}$  is a martin*gale* in this filtration  $(\mathcal{F}_t)_{t>0}$ . To keep in line with the above notation, we only consider the finite-horizon process  $(M_t)_{0 \le t \le T}$ , but the example could as well be presented for the infinite horizon.

Let  $\varphi = (\varphi_t)_{0 \le t \le 1}$  be the *deterministic process* 

$$\varphi_t = t^{-1}, \quad 0 \le t \le 1 \tag{17}$$

and define the stochastic integral  $S = \varphi \cdot M$ , for which we get

$$S_{t} = \begin{cases} 0, & \text{for } 0 \le t \le \tau \\ \tau^{-1}\varepsilon, & \text{for } \tau \le t \end{cases}$$
(18)

The process  $S = (S_t)_{0 \le t \le 1}$  is a well-defined stochastic integral (in the pointwise Stieltjes sense). The verbal description of  $S$  goes as follows: again  $S$ remains at 0 until time  $\tau$  and then, depending on the sign of  $\varepsilon$ , it jumps to  $+\tau^{-1}$  or  $-\tau^{-1}$ .

Is the process  $S$  a martingale? Morally speaking, one might think yes, as it has the same odds of jumping up or down.<sup>d</sup> But this intuition goes wrong: indeed, the notion of martingale is based on some (conditional) expectations to be zero. When we do the calculations in the present example we end up with expressions of the form  $\infty - \infty$ , which creates a problem. Indeed, we have

$$\mathbb{E}[|S_t|] = \infty, \quad \text{for } 0 \le t \le 1 \tag{19}$$

as is easily seen from  $\int_0^t u^{-1} du = \infty$ , for  $t > 0$ . In fact, it is not hard to show [7] that, for every  $(\mathcal{F}_t)_{0 \le t \le 1}$ —stopping time  $\sigma : \Omega \to [0, 1]$ , such that  $\mathbb{P}[\sigma > 0] > 0$ , we have

$$\mathbb{E}[|S_{\sigma}|] = \infty \tag{20}$$

It follows that  $S$  even fails to be a local martingale. But, of course,  $S$  is a sigma-martingale by its very construction.

The message of the above example is that the notion of sigma-martingale is tailor-made to save the intuition that—from a "moral point of view"—the above process  $S$  is "something like a martingale".

Let us turn from moral considerations to finance again: the question arises as to whether a process  $S = (S_t)_{0 \le t \le T}$ , which is a sigma-martingale under some measure  $Q$  equivalent to  $\mathbb{P}$ , well defines a sound, that is, arbitrage-free, model of a financial market. The answer is analogous to the case of a local martingale, namely, a resounding yes. If  $S =$  $\varphi \cdot M$ , for some  $\mathbb{R}_+$ -valued predictable process  $\varphi$ , then again the "trivial formula"  $(15)$  above holds true. Hence again the families of *admissible stochastic integrals* on the processes S and M coincide. If these are the only relevant objects—as is the case for the classical approach to no-arbitrage theory as proposed by M. Harrison and S. Pliska [8]—the processes  $S$  and  $M$  work equally well. In particular, the Ansel-Stricker Theorem carries over to sigmamartingales (see [4, Th. 5.5] for a somewhat stronger version of this result).

It is not hard to show that a locally bounded process, which is a sigma-martingale, is already a local martingale [4, Prop. 2.5 and 2.6]. Émery's example shows that this is not the case any more if we drop the local boundedness assumption. From a financial point of view, however, the question of interest arises in a slightly different version. Is there an example of a process  $S = (S_t)_{0 \le t \le T}$ , which is a sigma-martingale, say under  $\mathbb{P}$ , but such that it *fails to* be a local martingale under any probability measure  $Q$  equivalent to  $\mathbb{P}$ ?

Émery's original example does not provide a counterexample to this question; in this example, it is not hard to pass from  $\mathbb{P}$  to  $Q$  such that S even becomes a  $O$ -martingale. However, in [4, Ex. 2.3] a variant of Émery's example has been constructed, which is a process S taking values in  $\mathbb{R}^2$ answering the above question negatively. It seems worth mentioning that—to the best of the author's knowledge-it is unknown whether there also is a counterexample of a process  $S$ , taking values only in  $\mathbb{R}$ , to this question.

#### **Separating Measures**

We have seen in the preceding sections that, for a process  $S = (S_t)_{0 \le t \le T}$  which is a sigma-martingale under some probability measure  $Q$  and for each admissible integrand  $H$ , we have the inequality

$$\mathbb{E}_{O}[(H \cdot S)_{T}] \le 0 \tag{21}$$

Indeed, the theorem of Ansel-Stricker [1, Corr.  $3.5$ ] and its extension to sigma-martingales [4, Th. 5.5] imply that  $H \cdot S$  is a local martingale and, using again the boundedness from below, the process  $H \cdot S$  is a supermartingale.

The notion of a separating measure introduced by Y. Kabanov in  $[9]$ , takes this inequality  $(21)$  as defining property. To formalize this idea, we assume that S is an  $\mathbb{R}^d$ -valued semimartingale on some filtered probability space  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{0 \le t \le T}, \mathbb{P})$ . We say that a measure  $Q$ , equivalent to  $\mathbb{P}$ , is a *separating measure* for  $S$  if, for all admissible, predictable S-integrable integrands  $H$ , inequality (21) holds true.

If  $S$  is bounded, then it is straightforward to verify that the validity of inequality (21), for all admissible  $H$ , is tantamount to  $S$  being a martingale. It follows that, if  $S$  is locally bounded, then the validity of inequality (21), for all admissible  $H$ , is tantamount to  $S$  being a local martingale. Hence, we do not find anything new by using the notion of *separating measure* in the context of locally bounded semimartingales  $S$ . However, for semimartingales  $S$ that are not locally bounded, we do find something new; as observed above, if  $S$  is a sigma-martingale under  $Q$  then inequality (21) holds true, for all admissible  $H$ . But the converse does not hold true. The difference is illustrated by the subsequent easy one-period example. To stay in line with the present notation, we write it as an example in continuous time.

**Example 2** Let *X* be an  $\mathbb{R}$ -valued random variable, defined on some probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ , which is unbounded from above and from below. For example, we may choose  $X$  to be normally distributed.

The process  $S = (S_t)_{0 \le t \le 1}$  is defined as

$$S_t = \begin{cases} 0 & 0 \le t < 1 \\ X & t = 1 \end{cases} \tag{22}$$

Defining  $(\mathcal{F}_t)_{0 \le t \le 1}$  as the filtration generated by  $S = (S_t)_{0 \le t \le 1}$ , we find that the only  $(\mathcal{F}_t)_{0 \le t \le 1}$ predictable processes are the *constant processes*  $H =$  $(H_t)_{0 \le t \le 1}$ . Among those, the only S-admissible predictable process is  $H = 0$ . Indeed, if  $H = \text{const} \neq 0$ , the process  $H \cdot S$  is not bounded from below in the sense of inequality  $(14)$ .

The condition (21) therefore is trivially satisfied, for *each* probability measure Q equivalent to  $\mathbb{P}$ . On the other hand,  $S$  is a martingale (or, equivalently, a local or a sigma-martingale) under  $O$  if

$$\mathbb{E}_{\mathcal{Q}}[X] = \mathbb{E}_{\mathcal{Q}}[S_1] = 0 \tag{23}$$

Hence we see that, in this easy example, the class of separating measures  $Q$  is strictly bigger than the class of probability measures  $Q$ , equivalent to  $\mathbb{P}$ , under which  $S$  is a sigma-martingale.

Where does the nomenclature "separating measure" come from? This concept arises naturally as an intermediary step in the proof of **Fundamental The**orem of Asset Pricing (compare [9] for a careful analysis of the arguments in  $[3]$  and  $[4]$  and, in particular, for the introduction of the name "separating measure").

In the context of this theorem, after surmounting some difficulties, an application of the Hahn-Banach theorem plus an exhaustion argument due to J. Yan ([15], compare also [14]) provides a  $\sigma^*$ -continuous, linear functional  $F: L^{\infty}(\Omega, \mathcal{F}, \mathbb{P}) \to \mathbb{R}$  which *stric* $t \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n$ 

$$(H \cdot S)_T = \int_0^T (H_t, \mathrm{d}S_t) \tag{24}$$

where  $H$  runs through the admissible integrands, from  $L^{\infty}_{+}(\Omega, \mathcal{F}, \mathbb{P}) \setminus \{0\}$ , that is, the positive orthant with the origin 0 deleted. Normalizing the functional F by  $F(\zeta) = 1$ , this translates into the fact that F is of the form

$$F(g) = \mathbb{E}_{\mathcal{Q}}[g], \quad g \in L^{\infty}(\Omega, \mathcal{F}, \mathbb{P}) \tag{25}$$

where  $Q$  is a *separating measure*.

If the process  $S$  is bounded (respectively, locally bounded), it immediately follows that  $S$  is a martingale (respectively, a local martingale) under this separating measure  $Q$ , which concludes the proof of the fundamental theorem of asset pricing (see [3]).

If, however,  $S$  fails to be locally bounded, then we cannot conclude that  $S$  is "some kind of martingale" under the separating measure  $Q$ , as is illustrated by Example 2 above. Some further work is needed—which was carried out in  $[4]$ —to pass from the separating measure  $Q$  to a probability measure  $\tilde{Q}$ , which is equivalent to  $\mathbb{P}$  and under which S is a sigma-martingale measure. It turns out that, in the setting of the fundamental theorem of asset pricing [4], the latter set is dense with reference to  $\|\cdot\|_1$  in the set of separating measures for S. In particular, this set is nonempty, provided we have found a separating measure. This argument concludes the proof of the fundamental theorem of asset pricing also in the case of a general,  $\mathbb{R}^d$ -valued semimartingale  $S$ .

#### **End Notes**

<sup>a</sup>.For *continuous* local martingales  $(M_t)_{t\geq 0}$  starting at  $M_0 = 0$  the choice of stopping times *via* equation (9) always works, that is, gives a sequence  $(\tau_n)_{n=1}^{\infty}$  satisfying the requirements of (ii) above. In the case of càdlàg local martingales this is not true any more and one may give examples of local martingales where equation (9) does not define a sequence of localizing stopping times.

<sup>b.</sup>The name is derived from the following fact: let  $(B_t)_{0 \le t \le 1} = (B_t^1, B_t^2, B_t^3)_{0 \le t \le 1}$  be an  $\mathbb{R}^3$ -valued standard Brownian motion starting at  $B_0 = (B_0^1, B_0^2, B_0^3) = (1, 0, 0).$ Let  $R_t = \|B_t\|^{-1}$  where  $\|.\|$  denotes Euclidean norm on  $\mathbb{R}^3$ . Then  $(R_t)_{0 \le t \le 1}$  satisfies equation (10), where  $(W_t)_{0 \le t \le 1}$  is a one-dimensional Brownian motion adapted to the filtration generated by the three-dimensional Brownian  $(B_t)_{0 \le t \le 1}$ . We refer to  $[11]$  for a beautiful presentation of the theory of Bessel processes (compare also [5]).

<sup>c</sup>.It is easy to verify that in Proposition 1 (as well as in Definition 1 (iii)), we may assume without loss of generality that  $\varphi$  takes its values in  $]0, \infty[$  (or, equivalently, in  $[1, \infty[$ ). See [4, Prop. 2.5] for details.

<sup>d.</sup>A precise statement is that the processes  $S$  and  $-S$  have the same law, which obviously is the case.

<sup>e</sup>. To be precise, we have to consider the random variables  $(H \cdot S)_T \wedge C$ , where C runs through  $\mathbb{R}_+$ , to make sure that these random variables are in  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ .

### References

- Ansel, J.P. & Stricker, C. (1994). Couverture des actifs [1] contingents et prix maximum, Annales de l'Institut Henri Poincaré - Probabilités et Statistiques 30, 303-315.
- [2] Chou, C.S. (1977/78). Caractérisation d'une classe de semimartingales, in Séminaire de Probabilités XIII, Springer Lecture Notes in Mathematics, Springer, Vol. 721, pp. 250-252.
- [3] Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing, Mathematische Annalen 300, 463-520.
- Delbaen, F. & Schachermayer, W. (1998). The funda-[4] mental theorem of asset pricing for unbounded stochastic processes, Mathematische Annalen 312, 215-250.
- [5] Delbaen, F. & Schachermayer, W. (1995). Arbitrage possibilities in Bessel processes and their relations to local martingales, *Probability Theory and Related Fields* 102, 357-366.
- Delbaen, F. & Schachermayer, W. (2006). The Math-[6] ematics of Arbitrage, Springer Finance, p. 371. ISBN: 3-540-21992-7.
- Émery, M. (1980). Compensation de processus à varia-[7] tion finie non localement intégrables, in Séminaire de Probabilités XIV, J. Azema & M. Yor, eds, Springer Lecture Notes in Mathematics, Springer, Vol. 784, рр. 152-160.

- Harrison, J.M. & Pliska, S.R. (1981). Martingales and [8] stochastic integrals in the theory of continuous trading, Stochastic Processes and their Applications 11,  $215 - 260.$
- Kabanov, Y.M. (1997). On the FTAP of Kreps-Delbaen-[9] Schachermayer (English), in Statistics and Control of Stochastic Processes, Y.M. Kabanov, B.L. Rozovskii & A.N. Shiryaev, eds, The Liptser Festschrift. Papers from the Steklov Seminar held in Moscow, Russia, 1995–1996, World Scientific, Singapore, pp.  $191 - 203$ .
- [10] Protter, P. (1990). Stochastic integration and differential equations. A new approach, in Applications of Mathematics, (2nd edition, 2003, corrected third printing: 2005) Springer-Verlag, Berlin, Heidelberg, New York, Vol. 21.
- $[111]$ Revuz, D. & Yor, M. (1991). Continuous martingales and Brownian motion, in Grundlehren der Mathematischen Wissenschaften, 3rd edition, 1999, corrected third printing: 2005, Springer, Vol. 293.
- [12] Rogers, L.C.G. & Williams, D. (2000). Diffusions, Markov Processes and Martingales, Cambridge University Press, Vol. I and II.
- [13] Shreve, S. (2004). Stochastic calculus for finance, Springer Finance I, II, 208, 550.
- Stricker, Ch. (1990). Arbitrage et Lois de martingale, [14] Annales de l'Institut Henri Poincaré - Probabilites et Statistiques 26, 451-460.
- [15] Yan, J.A. (1980). Caractérisation d' une classe d'ensembles convexes de  $L^1$  ou  $H^1$ , in *Séminaire de* Probabilités XIV, J. Azema & M. Yor, eds, Springer Lecture Notes in Mathematics, Springer, Vol. 784, pp.  $220 - 222.$

# **Related Articles**

Arbitrage Strategy; Complete Markets; Free Lunch; Fundamental Theorem of Asset Pricing; Martingales; Minimal Entropy Martingale Measure; Minimal Martingale Measure; Riskneutral Pricing; Second Fundamental Theorem of Asset Pricing.

WALTER SCHACHERMAYER
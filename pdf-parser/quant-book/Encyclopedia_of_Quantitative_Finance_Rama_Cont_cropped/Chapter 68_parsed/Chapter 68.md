## **Fundamental Theorem of Asset Pricing**

Consider a financial market modeled by a price process *S* on an underlying probability space *(,* F*, )*. The *fundamental theorem of asset pricing*, which is one of the pillars supporting the modern theory of Mathematical Finance, states that the following two statements are *essentially* equivalent:

- 1. *S* does not allow for arbitrage (NA).
- 2. There exists a probability measure *Q* on the underlying probability space *(,* F*, )*, which is equivalent to and under which the process is a martingale.

We have formulated this theorem in vague terms, which will be made precise in the sequel: we formulate versions of this theorem that use precise definitions and avoid the use of the word *essentially*.

The story of this theorem started—like most of modern Mathematical Finance—with the work of Black (*see* **Black, Fischer**), Scholes [3], and Merton (*see* **Merton, Robert C.**) [25]. These authors consider a model *S* = *(St)*0≤*t*≤*<sup>T</sup>* of geometric Brownian motion proposed by Samuelson (*see* **Samuelson, Paul A.**) [30], which is widely known today as the Black–Scholes model. Presumably every reader of this article is familiar with the well-known technique to price options in this framework (*see* **Risk-neutral Pricing**): one changes the underlying measure to an equivalent measure *Q* under which the discounted stock price process is a martingale. Subsequently, one prices options (and other derivatives) by simply taking expectations with respect to this "risk neutral" or "martingale" measure *Q*.

In fact, this technique was *not* the novel feature of [3, 25]. It was used by actuaries for some centuries and it was also used by Bachelier [2] in 1900 who considered Brownian motion (which, of course, is a martingale) as a model *S* = *(St)*0≤*t*≤*<sup>T</sup>* of a stock price process. In fact, the prices obtained by Bachelier (*see* **Bachelier, Louis (1870–1946)**) by this method were—at least for the empirical data considered by Bachelier himself —very close to those derived from the celebrated Black–Merton–Scholes formula ([34]).

The decisive *novel feature* of the Black–Merton– Scholes approach was the argument that links this pricing technique with the notion of arbitrage: the payoff function of an option can be precisely *replicated* by trading dynamically in the underlying stock. This idea, which is credited in footnote 3 of [3] to Merton, opened a completely new perspective on how to deal with options, as it linked the pricing issue with the idea of hedging, that is, dynamically trading in the underlying asset.

The technique of replicating an option is completely absent in Bachelier's early work; apparently, the idea of "spanning" a market by forming linear combinations of primitive assets first appears in the Economics literature in the classic paper by Arrow (*see* **Arrow, Kenneth**) [1]. The mathematically delightful situation, that the market is complete in the sense that all derivatives can be replicated, occurs in the Black–Scholes model as well as in Bachelier's original model of Brownian motion (*see* **Second Fundamental Theorem of Asset Pricing**). Another example of a model in continuous time sharing this property is the compensated Poisson process, as observed by Cox and Ross (*see* **Ross, Stephen**) [4]. Roughly speaking, these are the only models in continuous time sharing this seducingly beautiful "martingale representation property" (see [16, 39] for a precise statement on the uniqueness of these families of models).

Appealing as it might be, the consideration of "complete markets" as above is somewhat dangerous from an economic point of view: the precise replicability of options, which is a sound mathematical theorem in the framework of the above models, may lead to the illusion that this is also true in economic reality. However, these models are far from matching reality in a one-to-one manner. Rather they only highlight important aspects of reality and therefore should not be considered as ubiquitously appropriate.

For many purposes, it is of crucial importance to put oneself into a more general modeling framework.

When the merits as well as the limitations of the Black–Merton–Scholes approach unfolded in the late 1970s, the investigations on the fundamental theorem of asset pricing started. As Harrison and Pliska formulate it in their classic paper [15]: "it was a desire to better understand their formula which originally motivated our study, *...* ".

The challenge was to obtain a deeper insight into the relation of the following two aspects: on one hand, the methodology of pricing by taking expectations with respect to a properly chosen "risk neutral" or "martingale" measure  $Q$ ; on the other hand, the methodology of pricing by "no arbitrage" considerations. Why, after all, do these two seemingly unrelated approaches yield identical results in the Black-Merton-Scholes approach? Maybe even more importantly: how far can this phenomenon be extended to more involved models?

To the best of the author's knowledge, the first person to take up these questions in a systematic way was Ross (see **Ross, Stephen**) [29]; see also [4, 27, 28]. He chose the following setting to formalize the situation: fix a topological, ordered vector space  $(X, \tau)$ , modeling the possible cash flows (e.g., the payoff function of an option) at a fixed time horizon T. A good choice is, for example,  $X = L^p(\Omega, \mathcal{F}, \mathbb{P}),$ where  $1 \leq p \leq \infty$  and  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{0 \leq t \leq T}, \mathbb{P})$  is the underlying filtered probability space. The set of marketed assets  $M$  is a subspace of  $X$ .

In the context of a stock price process  $S =$  $(S_t)_{0 \le t \le T}$  as above, one might think of *M* as all the outcomes of an initial investment  $x \in \mathbb{R}$  plus the result of subsequent trading according to a predictable trading strategy  $H = (H_t)_{0 \le t \le T}$ . This yields (in discounted terms) an element

$$m = x + \int_0^T H_t \mathrm{d}S_t \tag{1}$$

in the set  $M$  of marketed claims. It is natural to price the above claim m by setting  $\pi(m) = x$ , as this is the net investment necessary to finance the above claim  $m$ .

For notational convenience, we shall assume in the sequel that  $S$  is a one-dimensional process. It is straightforward to generalize to the case of  $d$  risky assets by assuming that S is  $\mathbb{R}^d$ -valued and replacing the above integral by

$$m = x + \int_0^T \sum_{i=1}^d H_t^i \mathrm{d}S_t^i \tag{2}$$

Some words of warning about the stochastic integral (1) seem necessary. The precise admissibility conditions, which should be imposed on the stochastic integral (1), in order to make sense both mathematically as well as economically, are a subtle issue. Much of the early literature on the fundamental theorem of asset pricing struggled exactly with this question. An excellent reference is [14]. Ross [29] circumvented this problem by deliberately leaving this issue aside and simply starting with the modeling assumption that the subset  $M \subseteq X$  as well as a pricing operator  $\pi : M \to \mathbb{R}$  are given.

Let us now formalize the notion of arbitrage. In the above setting, we say that the **no arbitrage** assumption is satisfied if, for  $m \in M$ , satisfying  $m > 0$ ,  $\mathbb{P}$ -a.s. and  $\mathbb{P}[m > 0] > 0$ , we have  $\pi(m) > 0$ 0. In prose, this means that it is not possible to find a claim  $m \in M$ , which bears no risk (as  $m > 0$ ,  $\mathbb{P}$ -a.s.), yields some gain with strictly positive probability (as  $\mathbb{P}[m>0]>0$ , and such that its price  $\pi(m)$  is less than or equal to zero.

The question that now arises is whether it is possible to extend  $\pi: M \to \mathbb{R}$  to a nonnegative, continuous linear functional  $\pi^*: X \to \mathbb{R}$ .

What does this have to do with the issue of martingale measures? This theme was developed in detail by Harrison and Kreps [14]. Suppose that  $X = L^p(\Omega, \mathcal{F}, \mathbb{P})$  for some  $1 \le p < \infty$ , that the price process  $S = (S_t)_{0 \le t \le T}$  satisfies  $S_t \in X$ , for each  $0 \le t \le T$ , and that *M* contains (at least) the "simple integrals" on the process  $S = (S_t)_{0 \le t \le T}$  of the form

$$m = x + \sum_{i=1}^{n} H_i (S_{t_i} - S_{t_{i-1}})$$
(3)

Here  $x \in \mathbb{R}$ ,  $0 = t_0 < t_1 < \ldots < t_n = T$  and  $(H_i)_{i=1}^n$  is a (say) bounded process which is pre*dictable*, that is,  $H_i$  is  $\mathcal{F}_{t_{i-1}}$ -measurable. The sums in equation (3) are the Riemann sums corresponding to the stochastic integrals (1). The Riemann sums (3) have a clear-cut economic interpretation [14]. In equation  $(3)$  we do not have to bother about subtle convergence issues as only finite sums are involved in the definition. It is therefore a traditional (minimal) requirement that the Riemann sums of the form (3) are in the space  $M$  of marketed claims; naturally, the price of a claim  $m$  of the form (3) should be defined as  $\pi(m) = x$ .

Now suppose that the functional  $\pi$ , which is defined for the claims of the form  $(3)$  can be extended to a continuous, nonnegative functional  $\pi^*$  defined on  $X = L^p(\Omega, \mathcal{F}, \mathbb{P}).$  If such an extension  $\pi^*$  exists, it is induced by some function  $g \in L^q(\Omega, \mathcal{F}, \mathbb{P})$ , where  $\frac{1}{p} + \frac{1}{q} = 1$ . The nonnegativity of  $\pi^*$  is tantamount to  $g \ge 0$ ,  $\mathbb{P}$ -a.s., and the fact that  $\pi^*(1) = 1$  shows that  $g$  is the density of a probability measure  $Q$  with Radon–Nikodym derivative  $\frac{dQ}{dP} = g$ .

If we can find such an extension  $\pi^*$  of  $\pi$ , we thus find a probability measure O on  $(\Omega, \mathcal{F}, \mathbb{P})$  for which

$$\pi^* \left( \sum_{i=1}^n H_i \left( S_{t_i} - S_{t_{i-1}} \right) \right) = \mathbb{E}_{\mathcal{Q}} \left[ \sum_{i=1}^n H_i (S_{t_i} - S_{t_{i-1}}) \right]$$
(4)

for every bounded predictable process  $H = (H_i)_{i=1}^n$ as above, which is tantamount to  $(S_t)_{0 \le t \le T}$  being a martingale (see [Th. 2] [14], or [Lemma 2.2.6] [11]).

To sum up, in the case  $1 \le p < \infty$ , finding a continuous, nonnegative extension  $\pi^*: L^p(\Omega, \mathcal{F}, \mathbb{P}) \to$  $\mathbb{R}$  of  $\pi$  amounts to finding a  $\mathbb{P}$ -absolutely continuous measure  $Q$  with  $\frac{dQ}{dP} \in L^q$  and such that  $(S_t)_{0 \le t \le T}$  is a martingale under  $Q$ .

At this stage, it becomes clear that in order to find such an extension  $\pi^*$  of  $\pi$ , the Hahn-Banach theorem should come into play in some form, for example, in one of the versions of the separating hyperplane theorem.

In order to be able to do so, Ross assumes ([p. 472] [29]) that "...we will endow  $X$  with a strong enough topology to insure that the positive orthant  $\{x \in X | x > 0\}$  is an open set, ...". In practice, the only infinite-dimensional ordered topological vector space  $X$ , such that the positive orthant has nonempty interior, is  $X = L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ , endowed with the topology induced by  $\|.\|_{\infty}$ .

Hence the two important cases, applying to Ross' hypothesis, are when either the probability space  $\Omega$ is finite, so that  $X = L^p(\Omega, \mathcal{F}, \mathbb{P})$  simply is finite dimensional and its topology does not depend on  $1 \leq p \leq \infty$ , or if  $(\Omega, \mathcal{F}, \mathbb{P})$  is infinite and  $X =$  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$  equipped with the norm  $\|.\|_{\infty}$ .

After these preparations we can identify the two convex sets to be separated: let  $A = \{m \in M :$  $\pi(m) < 0$  and B be the interior of the positive cone of  $X$ . Now make the easy, but crucial, observation: these sets are disjoint if and only if the no-arbitrage condition is satisfied. As one always can separate an open convex set from a disjoint convex set, we find a functional  $\tilde{\pi}$ , which is strictly positive on B, while  $\tilde{\pi}$  takes nonpositive values on A. By normalizing  $\tilde{\pi}$ , that is, letting  $\pi^* = \tilde{\pi}(1)^{-1}\tilde{\pi}$  we have thus found the desired extension.

In summary, the first precise version of the fundamental theorem of asset pricing is established in [29], the proof relying on the Hahn–Banach theorem. There are, however, serious limitations: in the case of infinite  $(\Omega, \mathcal{F}, \mathbb{P})$ , the present result only applies to  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$  endowed with the norm topology. In this case, the continuous linear functional  $\pi^*$  only is in  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})^*$  and not necessarily in  $L^1(\Omega, \mathcal{F}, \mathbb{P})$ ; in other words, we cannot be sure that  $\pi^*$  is induced by a probability measure  $Q$ , as it may happen that  $\pi^* \in L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})^*$  also has a singular part.

Another drawback, which already appears in the case of finite-dimensional  $\Omega$  (in which case  $\pi^*$ certainly is induced by some  $Q$  with  $\frac{dQ}{dP} = g \in L^1(\Omega, \mathcal{F}, P)$  is the following: we cannot be sure that the function  $g$  is strictly positive  $\mathbb{P}$ -a.s. or, in other words, that  $Q$  is equivalent to  $\mathbb{P}$ .

After this early work by Ross, a major advance in the theory was achieved between 1979 and 1981 by three seminal papers [14, 15, 24] by Harrison, Kreps, and Pliska. In particular, [14] is a landmark in the field. It uses a similar setting as [29], namely, an ordered topological vector space  $(X, \tau)$  and a linear functional  $\pi: M \to \mathbb{R}$ , where M is a linear subspace of  $X$ . Again the question is whether there exists an extension of  $\pi$  to a linear, continuous, strictly positive  $\pi^*: X \to \mathbb{R}$ . This question is related in [14] to the issue of whether  $(M, \pi)$  is viable as a model of economic equilibrium. Under proper assumptions on the convexity and continuity of the preferences of agents, this is shown to be equivalent to the extension discussed above.

The paper [14] also analyzes the case when  $\Omega$  is finite. Of course, only processes  $S = (S_t)_{t=0}^T$  indexed by finite, discrete time  $\{0, 1, \ldots, T\}$  make sense in this case. For this easier setting, the following precise theorem was stated and proved in the subsequent paper [15] by Harrison and Pliska:

**Theorem 1** ([Th. 2. 7.] [15]): suppose the stochastic process  $S = (S_t)_{t=0}^T$  is based on a finite, filtered, probability space  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t=0}^T, \mathbb{P})$ . The market model contains no-arbitrage possibilities if and only if there is an equivalent martingale measure for S.

The proof again relies on a (finite-dimensional version) of the Hahn-Banach theorem plus an extra argument making sure to find a measure  $Q$ , which is *equivalent to*  $\mathbb{P}$ . Harrison and Pliska thus have achieved a precise version of the above meta-theorem in terms of equivalent martingale measures, which does not use the word "essentially". Actually, the theme of the Harrison-Pliska theorem goes back much further, to the work of Shimony [35] and Kemeny [22] on symbolic logic in the tradition of Carnap, de Finetti, and Ramsey. These authors showed that, in a setting with only finitely many states of the world, a family of possible bets does not allow (by taking linear combinations) for making a riskless profit (i.e., one certainly does not lose but wins with strictly positive probability), if and only if there is a probability measure  $O$  on these finitely many states. which prices the possible bets by taking conditional  $O$ -expectations.

The restriction to finite  $\Omega$  is very severe in applications: the flavor of the theory, building on Black-Scholes-Merton, is precisely the concept of continuous time. Of course, this involves infinite probability spaces  $(\Omega, \mathcal{F}, \mathbb{P})$ .

Many interesting questions were formulated in the papers  $[14, 15]$  hinting on the difficulties to prove a version of the fundamental theorem of asset pricing beyond the setting of finite probability spaces.

A major breakthrough in this direction was achieved by Kreps [24]: as above, let  $M \subseteq X$  and a linear functional  $\pi: M \to \mathbb{R}$  be given. The typical choice for X will now be  $X = L^p(\Omega, \mathcal{F}, \mathbb{P})$ , for  $1 \leq p \leq \infty$ , equipped with the topology  $\tau$  of convergence in norm, or, if  $X = L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ , equipped with the Mackey topology  $\tau$  induced by  $L^1(\Omega, \mathcal{F}, \mathbb{P})$ . This setting will make sure that a continuous linear functional on  $(X, \tau)$  will be induced by a measure Q, which is absolutely continuous with respect to  $\mathbb{P}$ .

The no-arbitrage assumption means that  $M_0 :=$  $\{m \in M : \pi(m) = 0\}$  intersects the positive orthant  $X_{+}$  of X only in  $\{0\}$ . In order to obtain an extension of  $\pi$  to a continuous, linear functional  $\pi^*: X \to \mathbb{R}$  we have to find an element in  $(X, \tau)^*$ , which separates the convex set  $M_0$  from the disjoint convex set  $X_{+}\{0\}$ , that is, the positive orthant of X with 0 deleted.

Easy examples show that, in general, this is not possible. In fact, this is not much of a surprise (if  $X$  is infinite-dimensional) as we know that some topological condition is needed for the Hahn-Banach theorem to work.

It is always possible to separate a *closed* convex set from a disjoint *compact* convex set by a continuous linear functional. In fact, one may even get strict separation in this case. It is this version of the Hahn–Banach theorem that Kreps eventually applies.

But how? After all, neither  $M_0$  nor  $X_{+}{0}$  are closed in  $(X, \tau)$ , let alone compact.

Here is the ingenious construction of Kreps: define

$$A = \overline{M_0 - X_+} \tag{5}$$

where the bar denotes the closure with respect to the topology  $\tau$ . We shall require that A still satisfies

$$A \cap X_+ = \{0\} \tag{6}$$

This property is baptized as "*no free lunch*" by Kreps:

**Definition 1** [24]: The financial market defined by  $(X, \tau)$ , M, and  $\pi$  admits a free lunch if there are nets  $(m_{\alpha})_{\alpha\in I}\in M_0$  and  $(h_{\alpha})_{\alpha\in I}\in X_+$  such that

$$\lim_{\alpha \in I} \ (m_{\alpha} - h_{\alpha}) = x \tag{7}$$

for some  $x \in X_+\setminus\{0\}$ .

It is easy to verify that the negation of the above definition is tantamount to the validity of equation  $(6)$ .

The economic interpretation of the "no free lunch" condition is a sharpening of the "no-arbitrage condition". If the latter is violated, we can simply find an element  $x \in X_+\{0\}$ , which also lies in  $M_0$ . If the former fails, we cannot quite guarantee this, but we can find  $x \in X_+\{0\}$ , which can be approximated in the  $\tau$ -topology by elements of the form  $m_{\alpha} - h_{\alpha}$ . The passage from  $m_{\alpha}$  to  $m_{\alpha} - h_{\alpha}$  means that agents are allowed to "throw away money", that is, to abandon a positive element  $h_{\alpha} \in X_{+}$ . This combination of the "free disposal" assumption with the possibility of passing to limits is crucial in Kreps' approach  $(5)$ as well as in most of the subsequent literature. It was shown in [Ex. 3.3] [32]; ([33]) that the (seemingly ridiculous) "free disposal" assumption cannot be dropped.

Definition  $(5)$  is tailor-made for the application of Hahn-Banach. If the no free lunch condition (6) is satisfied, we may, for any  $h \in X_+$ , separate the  $\tau$ -closed, convex set A from the one-point set  $\{h\}$ by an element  $\pi_h \in (X, \tau)^*$ . As  $0 \in A$ , we may assume that  $\pi_h|_A \leq 0$  while  $\pi_h(h) > 0$ . We thus have obtained a nonnegative (as  $-X_{+} \subseteq A$ ), continuous linear functional  $\pi_h$ , which is strictly positive on a given  $h \in X_+$ . Supposing that  $X_+$  is  $\tau$ -separable (which is the case in the above setting of  $L^p$ -spaces if  $(\Omega, \mathcal{F}, \mathbb{P})$  is countably generated), fix a dense sequence  $(h_n)_{n=1}^{\infty}$  and find strictly positive scalars  $\mu_n > 0$  such that  $\pi^* = \sum_{n=1}^{\infty} \mu_n \pi_{h_n}$  converges to a probability measure in  $(X, \tau)^* = L^q(\Omega, \mathcal{F}, \mathbb{P})$ , where  $\frac{1}{p} + \frac{1}{q} = 1$ . This yields the desired extension  $\pi^*$  of  $\pi$  which is *strictly positive* on  $X_+\{0\}$ .

We still have to specify the choice of  $(M_0, \pi)$ . The most basic choice is to take for given  $S = (S_t)_{0 \le t \le T}$ the space generated by the "simple integrands" (3) as proposed in [14]. We thus may deduce from Kreps' arguments in [24] the following version of the fundamental theorem of asset pricing.

**Theorem 2** Let  $(\Omega, \mathcal{F}, \mathbb{P})$  be countably generated and  $X = L^p(\Omega, \mathcal{F}, \mathbb{P})$  endowed with the norm topol- $\log \tau$ , if  $1 \le p < \infty$ , or the Mackey topology induced by  $L^1(\Omega, \mathcal{F}, \mathbb{P})$ , if  $p = \infty$ .

Let  $S = (S_t)_{0 \le t \le T}$  be a stochastic process taking values in X. Define  $M_0 \subseteq X$  to consist of the simple stochastic integrals  $\sum_{i=1}^{n} H_i(S_{t_i} - S_{t_{i-1}})$  as in equa $tion(3)$ 

Then the "no free lunch" condition (5) is satisfied if and only if there is a probability measure Q with  $\frac{dQ}{d\mathbb{P}} \in$  $L^q(\Omega, \mathcal{F}, \mathbb{P}), \text{ where } \frac{1}{p} + \frac{1}{q} = 1, \text{ such that } (S_t)_{0 \le t \le T} \text{ is }$ a O-martingale.

This remarkable theorem of Kreps sets new standards. For the first time, we have a mathematically precise statement of our meta-theorem applying to a general class of models in continuous time. There are still some limitations, however.

When applying the theorem to the case  $1 \le p <$  $\infty$ , we find the requirement  $\frac{\mathrm{d}\varrho}{\mathrm{d}\mathbb{P}}\in L^q(\Omega,\mathcal{F},\mathbb{P})$  for some  $q > 1$ , which is not very pleasant. After all, we want to know what exactly corresponds (in terms of some no-arbitrage condition) to the existence of an equivalent martingale measure  $Q$ . The *q*-moment condition is unnatural in most applications. In particular, it is not invariant under equivalent changes of measures as is done often in the applications.

The most interesting case of the above theorem is  $p = \infty$ . However, in this case, the requirement  $S_t \in X = L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$  is unduly strong for most applications. In addition, for  $p = \infty$ , we run into the subtleties of the Mackey topology  $\tau$  (or the weak-star topology, which does not make much of a difference) on  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ . We shall discuss this issue below.

The "heroic period" of the development of the fundamental theorem of asset pricing marked by Ross [29], Harrison-Kreps [14], Harrison-Pliska [15], and Kreps [24], put the issue on safe mathematical grounds and brought some spectacular results. However, it still left many questions open; quite a number of them were explicitly stated as open problems in these papers.

Subsequently a rather extensive literature developed, answering these problems and opening new perspectives. We cannot give a full account on all of this literature and refer, for example, to the monograph [11] for more extensive information. We can give an outline.

As regards the situation for  $1 < p < \infty$  in Kreps' theorem, this issue was further developed by Duffie and Huang [12] and, in particular, by Stricker [36]. This author related the no free lunch condition of Kreps to a theorem by Yan [37] obtained in the context of the Bichteler-Dellacherie theorem on the characterization of semimartingales. Using Yan's theorem, Stricker gave a different proof of Kreps' theorem, which does not need the assumption that  $(\Omega, \mathcal{F}, \mathbb{P})$  is countably generated.

A beautiful extension of the Harrison–Pliska theorem was obtained in 1990 by Dalang, Morton, and Willinger [5]. They showed that, for an  $\mathbb{R}^d$ -valued process  $(S_t)_{t=0}^T$  in finite discrete time, the no-arbitrage condition is indeed equivalent to the existence of an equivalent martingale measure. The proof is surprisingly tricky, at least for the case  $d > 2$ . It is based on the measurable selection theorem (the suggestion to use this theorem is acknowledged to Delbaen). Different proofs of the Dalang-Morton-Willinger theorem have been given in [17, 20, 21, 26, 31].

An important question left unanswered by Kreps was whether one can, in general, replace the use of nets  $(m_{\alpha} - h_{\alpha})_{\alpha \in I}$ , indexed by  $\alpha$  ranging in a general ordered set *I*, simply by sequences  $(m_n - h_n)_{n=1}^{\infty}$ . In the context of continuous processes,  $S = (S_t)_{0 \le t \le T}$ , a positive answer was given by Delbaen in [6], if one is willing to make the harmless modification to replace the deterministic times  $0 = t_0 \le t_1 \le \ldots \le t_n = T$  in equation (3) by *stopping times*  $0 = \tau_0 \leq \tau_1 \leq \ldots \leq$  $\tau_n = T$ . A second case, where the answer to this question is positive, are processes  $S = (S_t)_{t=0}^{\infty}$  in infinite, discrete time as shown in  $[32]$ .

The Banach-Steinhaus theorem implies that, for a sequence  $(m_n - h_n)_{n=1}^{\infty}$  converging in  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ with respect to the weak-star (or Mackey) topology, the norms  $(||m_n - h_n||_{\infty})_{n=1}^{\infty}$  remain bounded ("uniform boundedness principle"). Therefore, it follows that in the above two cases of continuous processes  $S = (S_t)_{0 \le t \le T}$  or processes  $(S_t)_{t=0}^{\infty}$  in infinite, discrete time, the "no free lunch" condition of Kreps can be equivalently replaced by the "no free lunch

with bounded risk" condition introduced in [32]: in equation  $(7)$  above, we additionally impose that  $(|m_{\alpha}-h_{\alpha}|_{\infty})_{\alpha\in I}$  remains bounded. In this case, we have that there is a constant  $M > 0$  such that  $m_{\alpha} \geq -M$ ,  $\mathbb{P}$ -a.s. for each  $\alpha \in I$ , which explains the wording "bounded risk".

However, in the context of general semimartingale models  $S = (S_t)_{0 \le t \le T}$ , a counter-example was given by Delbaen and the author in ( $[Ex. 7.8]$  [7]) showing that the "no free lunch with bounded risk" condition does not imply the existence of an equivalent martingale measure. Hence, in a general setting and by only using simple integrals, there is no possibility of getting any more precise information on the free lunch condition than the one provided by Kreps' theorem.

At this stage it became clear that, in order to obtain sharper results, one has to go beyond the framework of simple integrals (3) and rather use general stochastic integrals (1). After all, the simple integrals are only a technical gimmick, analogous to step functions in measure theory. In virtually all the applications, for example, the replication strategy of an option in the Black-Scholes model, one uses general integrals of the form  $(1)$ .

General integrands pose a number of questions to be settled. First of all, the integral (1) has to be mathematically well defined. The theory of stochastic calculus starting with K. Itô, and developed in particular by the Strasbourg school of probability around Meyer, provides very precise information on this issue: there is a good integration theory for a given stochastic process  $S = (S_t)_{0 \le t \le T}$  if and only if S is a semimartingale (theorem of Bichteler-Dellacherie).

Hence, mathematical arguments lead to the model assumption that  $S$  has to be a semimartingale. However, what about an economic justification of this assumption? Fortunately, the economic reasoning hints in the same direction. It was shown by Delbaen and the author that, for a locally bounded stochastic process  $S = (S_t)_{0 \le t \le T}$ , a very weak form of Kreps' "no free lunch" condition involving simple integrands  $(3)$ , implies already that S is a semimartingale (see [Theorem 7.2] [7], for a precise statement).

Hence, it is natural to assume that the model  $S = (S_t)_{0 \le t \le T}$  of stock prices is a semimartingale so that the stochastic integral (3) makes sense mathematically, for all S-integrable, predictable processes  $H = (H_t)_{0 \le t \le T}$ . As pointed out, [14, 15] impose, in addition, an admissibility condition to rule out doubling strategies and similar schemes.

**Definition 2** ([Def. 2.7] [7]): An S-integrable predictable process  $H = (H_t)_{0 \le t \le T}$  is called admissible if there is a constant  $M > 0$  such that

$$\int_0^t H_u \mathrm{d}S_u \ge -M, \quad a.s., \ for \ 0 \le t \le T \qquad (8)$$

The economic interpretation is that the economic agent, trading according to the strategy, has to respect a finite credit line  $M$ .

Let us now sketch the approach of [7]. Define

$$K = \left\{ \int_0^T H_t \mathrm{d}S_t : H \text{ admissible} \right\} \tag{9}$$

which is a set of (equivalence classes of) random variables. Note that by equation (6) the elements  $f \in K$  are uniformly bounded from below, that is,  $f \ge -M$  for some  $M \ge 0$ . On the other hand, there is no reason why the positive part  $f_{+}$  should obey any boundedness or integrability assumption.

As a next step, we "allow agents to throw away money" similarly as in Kreps' work [24]. Define

$$C = \left\{ g \in L^{\infty}(\Omega, \mathcal{F}, \mathbb{P}) : g \le f \text{ for some } f \in K \right\}$$
$$= \left[ K - L_{+}^{0}(\Omega, \mathcal{F}, \mathbb{P}) \right] \cap L^{\infty}(\Omega, \mathcal{F}, \mathbb{P}) \tag{10}$$

where  $L^0_{+}(\Omega, \mathcal{F}, \mathbb{P})$  denotes the set of nonnegative measurable functions.

By construction,  $C$  consists of bounded random variables, so that we can use the functional analytic duality theory between  $L^{\infty}$  and  $L^{1}$ . The difference of the subsequent definition to Kreps' approach is that it pertains to the norm topology  $\|.\|_{\infty}$  rather than to the Mackey topology on  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ .

**Definition 3** ([2.8] [11]): A locally bounded semimartingale  $S = (S_t)_{0 \le t \le T}$  satisfies the no free lunch with vanishing risk condition if

$$\bar{C} \cap L^{\infty}_{+}(\Omega, \mathcal{F}, \mathbb{P}) = \{0\} \tag{11}$$

where  $\bar{C}$  denotes the  $\|.\|_{\infty}$ -closure of C.

Here is the translation of equation  $(11)$  into prose: the process  $S$  fails the above condition if there is a function  $g \in L^{\infty}_{+}(\Omega, \mathcal{F}, \mathbb{P})$  with  $\mathbb{P}[g > 0] > 0$  and a sequence  $(f^n)_{n=1}^{\infty}$  of the form

$$f^{n} = \int_{0}^{T} H_{t}^{n} \mathrm{d}S_{t} \tag{12}$$

where  $H^n$  are admissible integrands, such that

$$f_n \ge g - \frac{1}{n} \qquad a.s. \tag{13}$$

Hence the condition of no free lunch with vanishing risk is intermediate between the (stronger) no free lunch condition of Kreps and the (weaker) no-arbitrage condition. The latter would require that there is a nonnegative function  $g$  with  $\mathbb{P}[g > 0] > 0$ , which is of the form

$$g = \int_0^T H_t \mathrm{d}S_t \tag{14}$$

for an admissible integrand  $H$ . Condition (13) does not quite guarantee this, but something — at least from an economic point of view — very close: we can *uniformly* approximate from below such a  $g$  by the outcomes  $f_n$  of admissible trading strategies.

The main result of Delbaen and the author [7] reads as follows.

**Theorem 3** ([Corr. 1.2][7]): Let  $S = (S_t)_{0 \le t \le T}$  be a locally bounded real-valued semimartingale.

There is a probability measure O on  $(\Omega, \mathcal{F})$ , which is equivalent to  $\mathbb{P}$  and under which S is a local martingale if and only if  $S$  satisfies the condition of no free lunch with vanishing risk.

This is a mathematically precise theorem, which, in my opinion, is quite close to the vague "metatheorem" at the beginning of this article. The difference to the intuitive "no arbitrage" idea is that the agent has to be willing to sacrifice (at most) the quantity  $\frac{1}{n}$  in equation (13), where we may interpret  $\frac{1}{n}$  as, say, 1 cent.

The proof of the above theorem is rather long and technical and a more detailed discussion goes beyond the scope of this article. To the best of the author's knowledge, no essential simplification of this proof has been achieved so far ([19]).

Mathematically speaking, the statement of the theorem looks very suspicious at first glance: after all, the no free lunch with vanishing risk condition pertains to the *norm topology* of  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ . Hence it seems that, when applying the Hahn-Banach theorem, one can only obtain a linear functional in  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})^*$ , which is not necessarily of the form  $\frac{\mathrm{d} \varrho}{\mathrm{d} \mathbb{P}} \in L^1(\Omega, \mathcal{F}, \mathbb{P})$ , as we have seen in Ross' work [29].

The reason why the above theorem, nevertheless, is true is a little miracle: it turns out ([Th. 4.2] [7]) that, under the assumption of no free lunch with vanishing risk, the set  $C$  defined in equation (10) is *automatically* weak-star closed in  $L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ . This pleasant fact is not only a crucial step in the proof of the above theorem; maybe even more importantly, it also found other applications. For example, to find general existence results in the theory of utility optimization (see **Expected Utility Maximization: Duality Methods**) it is of crucial importance to have a closedness property of the set over which one optimizes: for these applications, the above result is very useful [23].

Without going into the details of the proof, the importance of certain elements in the set  $K$  is pointed out. The admissibility rules out the use of doubling strategies. The opposite of such a strategy can be called a *suicide strategy*. It is the mathematical equivalent of making a bet at the roulette, leaving it as well as all gains on the table as long as one keeps winning, and wait until one loses for the first time. Such strategies, although admissible, do not reflect economic efficiency. More precisely, we define the following.

**Definition 4** An admissible outcome  $\int_0^T H_t \mathrm{d}S_t$ is called maximal if there is no other admissible<br>strategy  $H'$  such that  $\int_0^T H'_t dS_t \geq \int_0^T H_t dS_t$  with  $\mathbb{P}[\int_0^T H_t' \mathrm{d}S_t > \int_0^T H_t \mathrm{d}S_t] > 0$ 

In the proof of Theorem 6, these elements play a crucial role and the heart of the proof consists in showing that every element in  $K$  is dominated by a maximal element. However, besides their mathematical relevance, they also have a clear economic interpretation. There is no use in implementing a strategy that is not maximal as one can do better. Nonmaximal elements can also be seen as bubbles [18].

In Theorem 6, we only assert that  $S$  is a *local* martingale under  $O$ . In fact, this technical concept cannot be avoided in this setting. Indeed, fix an S-integrable, predictable, admissible process  $H =$  $(H_t)_{0 \le t \le T}$  as well as a bounded, predictable, strictly positive process  $(k_t)_{0 \le t \le T}$ . The subsequent identity holds true trivially.

$$\int_0^t H_u \mathrm{d}S_u = \int_0^t \frac{H_u}{k_u} \mathrm{d}\tilde{S}_u, \quad 0 \le t \le T \tag{15}$$

where

$$\tilde{S}_u = \int_0^u k_v \mathrm{d}S_v, \quad 0 \le u \le T \tag{16}$$

The message of equations  $(15)$  and  $(16)$  is that the class of processes obtained by taking admissible stochastic integrals on S or  $\tilde{S}$  simply coincide. An easy interpretation of this rather trivial fact is that the possible investment opportunities do not depend on whether stock prices are denoted in euros or in cents (this corresponds to taking  $k_t \equiv 100$  above).

However, it may very well happen that  $\tilde{S}$  is a martingale while  $S$  only is a local martingale. In fact, the concept of local martingales may even be *characterized* in these terms ([Proposition 2.5] [10]): a semimartingale  $S$  is a local martingale if and only if there is a strictly positive, decreasing, predictable process k such that  $\tilde{S}$  defined in equation (16) is a martingale.

Again we want to emphasize the role of the maximal elements. It turns out ([8, 11]) that if  $\int_0^T H_t dS_t$  is maximal, *if and only if* there is an equivalent local martingale measure Q such that the process  $\int_0^t H_u dS_u$ is a martingale and not just a local martingale under  $Q$ . One can show ([9, 11]) that for a given sequence of maximal elements  $\int_0^T H_t^n dS_t$ , one can find one and the same equivalent local martingale measure  $Q$  such that all the processes  $\int_0^t H_u^n dS_u$  are Q-martingales. Another useful and related characterization ([8, 11]) is that if a process  $V_t = x + \int_0^t H_u dS_u$  defines a maximal element  $\int_0^T H_u dS_u$  and remains strictly positive, the whole financial market can be rewritten in terms of  $V$  as a new numéraire without losing the noarbitrage properties. The change of numéraire and the use of the maximal elements allows to introduce a numéraire invariant concept of admissibility, see [9] for details. An important result in this article is that the sum of maximal elements is again a maximal element.

Theorem 6 above still contains one severe limitation of generality, namely, the local boundedness assumption on  $S$ . As long as we only deal with con- $\n *tinuous processes S, this requirement is, of course,* \n$ satisfied. However, if one also considers processes with jumps, in most applications it is natural to drop the local boundedness assumption.

The case of general semimartingales  $S$  (without any boundedness assumption) was analyzed in [10]. Things become a little trickier as the concept of local martingales has to be weakened even further: we refer to **Equivalent Martingale Measures** for a discussion of the concept of sigma-martingales. This concept allows to formulate a result pertaining to a perfectly general setting.

**Theorem 4** ([Corr. 1.2][7]): Let  $S = (S_t)_{0 \le t \le T}$  be an  $\mathbb{R}^d$ -valued semimartingale.

*There is a probability measure Q on*  $(\Omega, \mathcal{F})$ *, which* is equivalent to  $\mathbb{P}$  and under which S is a sigmamartingale if and only if  $S$  satisfies the condition of no free lunch with vanishing risk with respect to admissible strategies.

One may still ask whether it is possible to formulate a version of the fundamental theorem, which does not rely on the concepts of local or sigma-, but rather on "true" martingales.

This was achieved by Yan [38] by applying a clever change of numéraire technique, (see Change of Numeraire also [Section 5] [13]): let us suppose that  $(S_t)_{0 \le t \le T}$  is a *positive* semimartingale, which is natural if we model, for example, prices of shares (while the previous setting of not necessarily positive price processes also allows for the modeling of forwards, futures etc.).

Let us weaken the admissibility condition (8) above, by calling a predictable, S-integrable process allowable if

$$\int_0^t H_u \mathrm{d}S_u \ge -M(1+S_t) \quad a.s., \text{ for } 0 \le t \le T$$
(17)

The economic idea underlying this notion is well known and allows for the following interpretation: an agent holding  $M$  units of stock and bond may, in addition, trade in  $S$  according to the trading strategy  $H$  satisfying equation (17); the agent will then remain liquid during  $[0, T]$ .

By taking  $S + 1$  as new numéraire and replacing admissible by allowable trading strategies, Yan obtains the following theorem.

**Theorem 5** ([Theorem 3.2] [38]) Suppose that  $S$  is a positive semimartingale.

*There is a probability measure*  $Q$  *on*  $(\Omega, \mathcal{F})$ *, which* is equivalent to  $\mathbb{P}$  and under which S is a martingale if and only if  $S$  satisfies the condition of no free lunch with vanishing risk with respect to allowable trading strategies.
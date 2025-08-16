# Filtrations

The notion of *filtration*, introduced by Doob, has become a fundamental feature of the theory of stochastic processes. Most basic objects, such as martingales, semimartingales, stopping times, or Markov processes, involve the notion of filtration.

**Definition 1** Let  $(\Omega, \mathcal{F}, \mathbb{P})$  be a probability space. A filtration  $\mathbb{F}$ , on  $(\Omega, \mathcal{F}, \mathbb{P})$ , is an increasing family  $(\mathcal{F}_t)_{t>0}$  of sub- $\sigma$ -algebras of  $\mathcal{F}$ . In other words, for each t,  $\mathcal{F}_t$  is a  $\sigma$ -algebra included in  $\mathcal{F}$  and if  $s \leq t$ ,  $\mathcal{F}_s \subset \mathcal{F}_t$ . A probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  endowed with a filtration  $\mathbb{F}$  is called a filtered probability space.

We now give a definition that is very closely related to that of a filtration.

**Definition 2** A stochastic process  $(X_t)_{t>0}$  on  $(\Omega,$  $(\mathcal{F}, \mathbb{P})$  is adapted to the filtration  $(\mathcal{F}_t)$  if, for each  $t > 0$ ,  $X_t$  is  $\mathcal{F}_t$ -measurable.

A stochastic process  $X$  is always adapted to its *natural filtration*  $\mathbb{F}^X$ , where for each  $t \ge 0$ ,  $\mathcal{F}_t^X = \sigma(X_s, s \leq t)$  (the last notation means that  $\mathcal{F}_t$ is the smallest  $\sigma$ -algebra with respect to which all the variables  $(X_s, s \leq t)$  are measurable).  $\mathbb{F}^X$  is, hence, the smallest filtration to which  $X$  is adapted.

The parameter  $t$  is often thought of as time, and the  $\sigma$ -algebra  $\mathcal{F}_t$  represents the set of information available at time  $t$ , that is, events that have occurred up to time t. Thus, the filtration  $\mathbb{F}$  represents the evolution of the information or knowledge of the world with time. If  $X$  is an adapted process, then  $X_t$ , its value at time t, depends only on the evolution of the universe prior to  $t$ .

**Definition 3** Let  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  be a filtered probability space.

- 1. The filtration  $\mathbb{F}$  is said to be complete if  $(\Omega, \mathcal{F}, \mathbb{P})$ is complete and if  $\mathcal{F}_0$  contains all the  $\mathbb{P}$ -null sets.
- 2. The filtration  $\mathbb{F}$  is said to satisfy the usual hypotheses if it is complete and right continuous, that is, for all  $t \geq 0$ ,  $\mathcal{F}_t = \mathcal{F}_{t+}$ , where

$$\mathcal{F}_{t+} = \bigcap_{u>t} \mathcal{F}_u \tag{1}$$

Some fundamental theorems, such as the Début theorem, require the usual hypotheses. Hence naturally, very often in the literature on the theory of stochastic processes and mathematical finance, the underlying filtered probability spaces are assumed to satisfy the usual hypotheses. This assumption is not very restrictive for the following reasons:

- 1. Any filtration can easily be made complete and right continuous; indeed, given a filtered probability space  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ , we first complete the probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ , and then we add all the  $\mathbb{P}$ -null sets to every  $\mathcal{F}_{t+}, t \geq 0$ . The new filtration thus obtained satisfies the usual hypotheses and is called the *usual augmentation* of  $\mathbb{F}$ ;
- 2. Moreover, in most classical and encountered cases, the filtration  $\mathbb{F}$  is right continuous. Indeed, this is the case when, for instance,  $\mathbb{F}$  is the natural filtration of a Brownian motion, a Lévy process, a Feller process, or a Hunt process [8, 9].

# **Enlargements of Filtrations**

For more precise and detailed references, the reader can consult the books  $[4-6, 8]$  or the survey article [7].

## Generalities

Let  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  be a filtered probability space satisfying the usual hypotheses. Let  $\mathbb{G}$  be another filtration satisfying the usual hypotheses and such that  $\mathcal{F}_t \subset \mathcal{G}_t$ for every  $t \ge 0$ . One natural question is, how are the F-semimartingales modified when considered as stochastic processes in the larger filtration  $\mathbb{G}$ ? Given the importance of semimartingales and martingales (in particular, in mathematical finance where they are used to model prices), it seems natural to characterize situations where the semimartingale or martingale properties are preserved.

**Definition 4** We shall say that the pair of filtrations  $(\mathbb{F}, \mathbb{G})$  satisfies the  $(H')$  hypothesis if every  $\mathbb{F}$ -semimartingale is a  $\mathbb{G}$ -semimartingale.

**Remark 1** In fact, using a classical decomposition of semimartingales due to Jacod and Mémin, it is enough to check that every  $\mathbb{F}$ -bounded martingale is a G-semimartingale.

**Definition 5** *We shall say that the pair of filtrations*  $(\mathbb{F}, \mathbb{G})$  satisfies the  $(H)$  hypothesis if every  $\mathbb{F}$ -local martingale is a G-local martingale.

The theory of enlargements of filtrations, developed in the late 1970s, provides answers to questions such as those mentioned earlier. Currently, this theory has been widely used in mathematical finance, especially in insider trading models and in models of default risk. The insider trading models are usually based on the so-called *initial enlargements of filtra*tions, whereas the models of default risk fit well in the framework of the *progressive enlargements of filtrations.* More precisely, given a filtered probability space  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ , there are essentially two ways of enlarging filtrations:

- initial enlargements, for which  $\mathcal{G}_t = \mathcal{F}_t \setminus \mathcal{H}$  for every  $t > 0$ , that is, the new information  $\mathcal{H}$  is brought in at the origin of time and
- progressive enlargements, for which  $\mathcal{G}_t = \mathcal{F}_t \setminus \mathcal{H}_t$ for every  $t > 0$ , that is, the new information is brought in progressively as the time  $t$  increases.

Before presenting the basic theorems on enlargements of filtrations, we state a useful theorem due to Stricker.

**Theorem 1** (Stricker [10]). Let  $\mathbb{F}$  and  $\mathbb{G}$  be two filtrations as above, such that for all  $t \geq 0$ ,  $\mathcal{F}_t \subset \mathcal{G}_t$ . If  $(X_t)$  is a  $G$ -semimartingale that is  $\mathbb{F}$ -adapted, then it is also an  $\mathbb{F}$ -semimartingale.

#### Initial Enlargements of Filtrations

The most important theorem on initial enlargements of filtrations is due to Jacod and deals with the special case where the initial information brought in at the origin of time consists of the  $\sigma$ -algebra generated by a random variable. More precisely, let  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ be a filtered probability space satisfying the usual assumptions. Let Z be an  $\mathcal{F}$  measurable random variable. Define

$$\mathcal{G}_{t} = \bigcap_{\varepsilon > 0} \left( \mathcal{F}_{t+\varepsilon} \bigvee \sigma \left\{ Z \right\} \right), \quad t \ge 0 \tag{2}$$

In financial models, the filtration  $\mathbb{F}$  represents the public information in a financial market and the random variable  $Z$  stands for the additional (anticipating) information of an insider.

The conditional laws of Z given  $\mathcal{F}_t$ , for  $t \geq 0$ , play a crucial role in initial enlargements.

**Theorem 2** (Jacod's criterion). Let Z be an  $\mathcal{F}$  measurable random variable and let  $O_t(\omega, dx)$  denote the regular conditional distribution of Z given  $\mathcal{F}_t$ ,  $t \geq 0$ . Suppose that for each  $t \ge 0$ , there exists a positive  $\sigma$ -finite measure  $\eta_t$  (dx) (on  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ ) such that

$$Q_t(\omega, dx) \ll \eta_t(dx)$$
 almost surely (3)

Then every  $\mathbb{F}$ -semimartingale is a  $\mathbb{G}$ -semimartingale.

**Remark 2** In fact, this theorem still holds for random variables with values in a standard Borel space. Moreover, the existence of the  $\sigma$ -finite measure  $\eta_t$  (dx) is equivalent to the existence of one positive  $\sigma$ -finite measure  $\eta$  (dx) such that  $Q_t(\omega, dx) \ll$  $\eta$  (dx) and in this case  $\eta$  can be taken to be the distribution of  $Z$ .

Now we give classical corollaries of Jacod's theorem.

**Corollary 1** Let Z be independent of  $\mathcal{F}_{\infty}$ . Then, every  $\mathbb{F}$ -semimartingale is a  $\mathbb{G}$ -semimartingale.

**Corollary 2** Let  $Z$  be a random variable taking on only a countable number of values. Then every  $\mathbb{F}$ semimartingale is a  $G$ -semimartingale.

In some cases, it is possible to obtain an explicit decomposition of an F-local martingale as a Gsemimartingale [4–8]. For example, if  $Z = B_{t_0}$ , for some fixed time  $t_0 > 0$  and a Brownian Motion *B*, it can be shown that Jacod's criterion holds for  $t < t_0$ and that every  $\mathbb{F}$ -local martingale is a semimartingale for  $0 \le t < t_0$ , but not necessarily including  $t_0$ . Indeed in this case, there are  $F$ -local martingales that are not  $\mathbb{G}$ -semimartingales. Moreover, B is a G-semimartingale, which decomposes as

$$B_t = B_0 + \widetilde{B}_t + \int_0^{t \wedge t_0} \mathrm{d}s \frac{B_{t_0} - B_s}{t_0 - s} \tag{4}$$

where  $(\widetilde{B}_t)$  is a G Brownian Motion.

Remark 3 There are cases where Jacod's criterion does not hold but where other methods apply [4, 6, 7].

#### Progressive Enlargements of Filtrations

Let  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  be a filtered probability space satisfying the usual hypotheses, and  $\rho: (\Omega, \mathcal{F}) \to$  $(\mathbb{R}_+, \mathcal{B}(\mathbb{R}_+))$  be a random time. We enlarge the initial filtration  $\mathbb{F}$  with the process  $(\rho \wedge t)_{t>0}$ , so that the new enlarged filtration  $\mathbb{F}^{\rho}$  is the smallest filtration (satisfying the usual assumptions) containing F and making  $\rho$  a stopping time (i.e., for all  $t \ge 0$ ,  $\mathcal{F}_t^o = \mathcal{K}_{t+}^o$ , where  $\mathcal{K}_t^o = \mathcal{F}_t \bigvee \sigma \ (\rho \wedge t)$ ). One may interpret  $\rho$  as the instant of default of an issuer; the given filtration  $\mathbb{F}$  can be thought of as the filtration of default-free prices, for which  $\rho$  is not a stopping time. Then, the filtration  $\mathbb{F}^{\rho}$  is the defaultable market filtration used for the pricing of defaultable assets.

A few processes play a crucial role in our discussion:

the  $\mathbb{F}$ -supermartingale

$$Z_t^{\rho} = \mathbb{P}\left[\rho > t \mid \mathcal{F}_t\right] \tag{5}$$

chosen to be càdlàg, associated to  $\rho$  by Azéma [1];

- $\bullet$  the  $\mathbb{F}$ -dual optional projection of the process  $\mathbf{1}_{\{\rho < t\}}$ , denoted by  $A_t^{\rho}$  (see [7, 8] for a definition of dual optional projections); and
- the càdlàg martingale

$$\mu_t^{\rho} = \mathbb{E}\left[A_{\infty}^{\rho} \mid \mathcal{F}_t\right] = A_t^{\rho} + Z_t^{\rho} \tag{6}$$

**Theorem 3** Every  $\mathbb{F}$ -local martingale  $(M_t)$ , stopped at  $\rho$ , is an  $\mathbb{F}^{\rho}$ -semimartingale, with canonical *decomposition:* 

$$M_{t \wedge \rho} = \widetilde{M}_{t} + \int_{0}^{t \wedge \rho} \frac{\mathrm{d} \langle M, \mu^{\rho} \rangle_{s}}{Z_{s-}^{\rho}} \tag{7}$$

where  $(\widetilde{M}_t)$  is an  $\mathbb{F}^{\rho}$ -local martingale.

The most interesting case in the theory of progressive enlargements of filtrations is when  $\rho$  is an *honest time* or equivalently the end of an  $\mathbb{F}$  optional set  $\Gamma$ , that is,

$$\rho = \sup \{ t : (t, \omega) \in \Gamma \} \tag{8}$$

Indeed, in this case, the pair of filtrations  $(\mathbb{F}, \mathbb{F}^{\rho})$ satisfies the  $(H')$  hypothesis: every  $\mathbb{F}$ -local martingale  $(M_t)$  is an  $\mathbb{F}^{\rho}$ -semimartingale, with canonical decomposition:

$$M_{t} = \widetilde{M}_{t} + \int_{0}^{t \wedge \rho} \frac{\mathrm{d}\langle M, \mu^{\rho} \rangle_{s}}{Z_{s-}^{\rho}} - \int_{\rho}^{t} \mathbf{1}_{\{\rho \le t\}} \frac{\mathrm{d}\langle M, \mu^{\rho} \rangle_{s}}{1 - Z_{s-}^{\rho}} \tag{9}$$

The next decomposition formulas are used for pricing in default models:

## Proposition 1

1. Let  $\xi \in L^1$ . Then a càdlàg version of the martingale  $\xi_t = \mathbb{E}\left[\xi|\mathcal{F}_t^{\rho}\right]$ , on the set  $\{t < \rho\}$ , is given by:

$$\xi_t \mathbf{1}_{t < \rho} = \frac{1}{Z_t^{\rho}} \mathbf{1}_{t < \rho} \mathbb{E} \left[ \xi \mathbf{1}_{t < \rho} | \mathcal{F}_t \right] \tag{10}$$

2. Let  $\xi \in L^1$  and let  $\rho$  be an honest time. Then a càdlàg version of the martingale  $\xi_t = \mathbb{E}\left[\xi|\mathcal{F}_t^o\right]$  is given as

$$\xi_{t} = \frac{1}{Z_{t}^{\rho}} \mathbb{E} \left[ \xi \mathbf{1}_{t < \rho} | \mathcal{F}_{t} \right] \mathbf{1}_{t < \rho} + \frac{1}{1 - Z_{t}^{\rho}} \mathbb{E} \left[ \xi \mathbf{1}_{t \ge \rho} | \mathcal{F}_{t} \right] \mathbf{1}_{t \ge \rho} \tag{11}$$

## $The (H) Hypothesis$

The  $(H)$  hypothesis, in contrast to the  $(H')$  hypothesis, is sometimes presented as a no-abitrage condition in default models. Let  $(\Omega, \mathcal{F}, \mathbb{P})$  be a probability space satisfying the usual assumptions. Let  $\mathbb{F}$  and  $\mathbb{G}$ be two subfiltrations of  $\mathcal{F}$ , with

$$\mathcal{F}_t \subset \mathcal{G}_t \tag{12}$$

Brémaud and Yor [2] have proven the following characterization of the  $(H)$  hypothesis:

**Theorem 4** The following are equivalent:

1. Every  $\mathbb{F}$ -martingale is a  $\mathbb{G}$ -martingale. 2. For all  $t \ge 0$ , the sigma fields  $\mathcal{G}_t$  and  $\mathcal{F}_{\infty}$  are independent conditionally on  $\mathcal{F}_t$ .

**Remark 4** We also say that  $\mathbb{F}$  is *immersed* in  $\mathbb{G}$ .

In the framework of the progressive enlargement of some filtration  $\mathbb{F}$  with a random time  $\rho$ , the  $(H)$  hypothesis is equivalent to one of the following hypothesis  $[3]$ :

- 1.  $\forall t$ , the  $\sigma$ -algebras  $\mathcal{F}_{\infty}$  and  $\mathcal{F}_{t}^{\rho}$  are conditionally independent given  $\mathcal{F}_t$ .
- For all bounded  $\mathcal{F}_{\infty}$  measurable random vari-2. ables **F** and all bounded  $\mathcal{F}_t^{\rho}$  measurable random variables  $\mathbf{G}_t$ , we have

$$\mathbb{E}\left[\mathbf{F}\mathbf{G}_{t} \mid \mathcal{F}_{t}\right] = \mathbb{E}\left[\mathbf{F} \mid \mathcal{F}_{t}\right] \mathbb{E}\left[\mathbf{G}_{t} \mid \mathcal{F}_{t}\right] \quad (13)$$

3. For all bounded  $\mathcal{F}_t^{\rho}$  measurable random variables  $\mathbf{G}_t$ :

$$\mathbb{E}\left[\mathbf{G}_{t} \mid \mathcal{F}_{\infty}\right] = \mathbb{E}\left[\mathbf{G}_{t} \mid \mathcal{F}_{t}\right] \tag{14}$$

4. For all bounded  $\mathcal{F}_{\infty}$  measurable random vari- $\text{ables } \mathbf{F}.$ 

$$\mathbb{E}\left[\mathbf{F} \mid \mathcal{F}_t^o\right] = \mathbb{E}\left[\mathbf{F} \mid \mathcal{F}_t\right] \tag{15}$$

5. For all  $s \leq t$ ,

$$\mathbb{P}\left[\rho \le s \mid \mathcal{F}_t\right] = \mathbb{P}\left[\rho \le s \mid \mathcal{F}_\infty\right] \tag{16}$$

In view of applications to financial mathematics, a natural question is, how is the  $(H)$  hypothesis affected when we make an equivalent change of probability measure?

**Proposition 2** Let  $\mathbb{Q}$  be a probability measure that is equivalent to  $\mathbb{P}$  (on  $\mathcal{F}$ ). Then, every  $(\mathbb{F}, \mathbb{Q})$ semimartingale is a  $(\mathbb{G}, \mathbb{Q})$ -semimartingale.

Now, define

$$\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\Big|_{\mathcal{F}_t} = R_t, \quad \frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\Big|_{\mathcal{G}_t} = R'_t \tag{17}$$

If  $Y = \frac{d\mathbb{Q}}{d\mathbb{P}}$ , then the hypothesis  $(H)$  holds under  $\mathbb{Q}$  if and only if

$$\forall X \ge 0, \quad X \in \mathcal{F}_{\infty}, \quad \frac{\mathbb{E}_{\mathbf{P}}[XY|\mathcal{G}_t]}{R'_t} = \frac{\mathbb{E}_{\mathbf{P}}[XY|\mathcal{F}_t]}{R_t} \tag{18}$$

In particular, when  $\frac{d\mathbb{Q}}{d\mathbb{P}}$  is  $\mathcal{F}_{\infty}$  measurable,  $R_t = R'_t$  and the hypothesis  $(H)$  holds under  $\mathbb{Q}$ . A decomposition formula is given below.

**Theorem 5** If  $(X_t)$  is a  $(\mathbb{F}, \mathbb{Q})$ -local martingale, then the stochastic process

$$I_X(t) = X_t + \int_0^t \frac{R'_{s-}}{R'_s}$$

$$\times \left(\frac{1}{R_{s-}}\,\mathrm{d}[X,\,R]_{s} - \frac{1}{R_{s-}'}\,\mathrm{d}[X,\,R']_{s}\right) \tag{19}$$

is a  $(\mathbb{G}, \mathbb{Q})$ -local martingale.

## References

- Azéma, J. (1972). Quelques applications de la théorie [1] générale des processus I, Inventiones Mathematicae 18, 293-336.
- Brémaud, P. & Yor, M. (1978). Changes of filtration [2] and of probability measures, Zeitschrift fur Wahrscheinlichkeitstheorie und Verwandte Gebiete **45**. 269–295.
- Elliott, R.J., Jeanblanc, M. & Yor, M. (2000). On models [3] of default risk, Mathematical Finance 10, 179-196.
- [4] Jeulin, T. (1980). Semi-martingales et Grossissements d'une Filtration, Lecture Notes in Mathematics, Springer, Vol. 833.
- Jeulin, T. & Yor, M. (eds) (1985). Grossissements de [5] Filtrations: Exemples et Applications, Lecture Notes in Mathematics, Springer, Vol. 1118.
- Mansuy, R. & Yor, M. (2006). Random Times and [6] (Enlargement of Filtrations) in a Brownian Setting, Lecture Notes in Mathematics, Springer, Vol. 1873.
- [7] Nikeghbali, A. (2006). An essay on the general theory of stochastic processes, *Probability Surveys* 3, 345–412.
- [8] Protter, P.E. (2005). Stochastic Integration and Differential Equations, 2nd Edition, version 2.1, Springer.
- [9] Revuz, D. & Yor, M. (1999). Continuous Martingales and Brownian Motion, 3rd Edition, Springer.
- $[10]$ Stricker, C. (1977). Quasi-martingales, martingales locales, semimartingales et filtration naturelle, Zeitschrift fur Wahrscheinlichkeitstheorie und Verwandte Gebiete 39, 55-63.

# **Further Reading**

Jacod, J. (1985). Grossissement initial, hypothèse (H'), et théorème de Girsanov, in Grossissements de Filtrations: Exemples et Applications, T. Jeulin & M. Yor, eds, Springer, рр. 15-35.

# **Related Articles**

Compensators; Equivalence of Probability Measures; Martingale Representation Theorem; Martingales; Poisson Process; Semimartingale.

DELIA COCULESCU & ASHKAN NIKEGHBALI
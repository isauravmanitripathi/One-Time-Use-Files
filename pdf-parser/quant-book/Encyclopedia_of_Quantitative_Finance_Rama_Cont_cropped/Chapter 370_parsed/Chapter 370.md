# **Time Change**

The mathematical concept of time-changing continuous-time stochastic processes has first been studied in [11, 17, 18, 23, 24, 29, 39] and has later been introduced to the finance literature in [14]. Today, it can be regarded as one of the standard tools for building financial models (see also [22, 32]).

Let  $X = (X_t)_{t \ge 0}$  denote a stochastic process, sometimes referred to as the base process, and let  $T = (T_s)_{s>0}$  denote a nonnegative, nondecreasing stochastic process not necessarily independent of  $X$ . The *time-changed process* is then defined as  $Y = (Y_s)_{s>0}$ , where

$$Y_s = X_{T_s} \tag{1}$$

The process  $X$  is said to evolve in *operational time*. The process  $T$  is referred to as a *time change*, stochastic clock, chronometer, or business time. It reflects the varying *speed* of  $Y$ .

This article is structured as follows. First we link the use of time-changed stochastic processes to the construction of univariate stochastic volatility models in finance. Then we focus on the choice of an appropriate base process and, next, on popular examples for the time change. Finally, we briefly discuss the potential and the limitations of the methodology of time-changing stochastic processes to construct multivariate models in finance.

#### **Stochastic Volatility Models**

The use of time-changed stochastic processes in finance is closely linked to the concept of stochastic volatility models for asset prices. Numerous empirical studies have revealed the fact that asset price volatility tends to be time varying and tends to show clustering effects. The concept of stochastic volatility (*see* **Volatility**) in continuous-time asset price models on a filtered probability space  $(\Omega, \mathcal{A}, (\mathcal{F}_t)_{t>0}, \mathbb{P})$  can basically be introduced by two methods.

One of the methods is to use time-changed stochastic processes as in equation  $(1)$ , where natural assumptions are that  $X = (X_t)_{t \ge 0}$  is an  $\mathcal{F}_t$ semimartingale and  $(T_s)_{s>0}$  is an increasing family of  $\mathcal{F}_t$ -stopping times. The base process X is often assumed to possess some homogeneity properties,

whereas a nonlinear time change can induce deviations from homogeneity.

The other method is to use stochastic integrals (see **Stochastic Integrals**) of the form

$$Y_t = \int_0^t \sigma_{r-} \, \mathrm{d}X_r \tag{2}$$

where  $\sigma = (\sigma_t)_{t>0}$  is a nonnegative  $\mathcal{F}_t$ -predictable stochastic volatility process and  $X = (X_t, t \ge 0)$  is an  $\mathcal{F}_t$ -semimartingale. Often, X is assumed to possess some homogeneity properties so that nonconstant  $\sigma$  can induce deviations from homogeneity.

Under certain conditions, the models  $(1)$  and  $(2)$ lead to equivalent models. However, in general, this is not true, and we highlight in the following text some of the main differences between these two modeling approaches.

#### **Time-changed Lévy Processes**

In the finance literature, the main focus is on timechanged Brownian motion or, more generally, on time-changed Lévy processes (see Lévy Processes; Time-changed Lévy Process), since these processes possess natural homogeneity properties of stationary and independent increments (returns).

Time-changed Brownian motion has first been used as a model for (logarithmic) asset prices by Clark [14]. He investigated the case where  $X = B =$  $(B_t)_{t>0}$  is a standard Brownian motion and where T is an independent continuous-time change. Clearly, in such a setting, the time-changed process  $Y_s = B_{T_s}$ has a mixed normal distribution, that is,  $Y_s|T_s \sim$  $N(0, T<sub>s</sub>)$ , and is a continuous local martingale. The power of such models and those with the assumptions of independence and/or continuity relaxed is expressed in the following key results.

**Theorem 1** (*Dubins–Schwarz*). [18, 34, 35] Every continuous local martingale  $M = (M_s)_{s \ge 0}$  can be written as a time-changed Brownian motion  $(B_{[M]_s})_{s>0}$ , where  $[M] = ([M]_s)_{s\geq 0}$  is the (continuous) quadratic variation of M.

Also  $M_t = \int_0^t \sigma_{r-} \mathrm{d}W_r$  for  $X = W = (W_t)_{t \ge 0}$ Brownian motion and  $\sigma = (\sigma_t)_{t>0}$  independent nonnegative with càdlàg sample paths is a continuous local martingale with quadratic variation  $[M]_t =$ 

 $\left[\int_0^{\cdot} \sigma_{r-} \mathrm{d}W_r\right]_t = \int_0^t \sigma_r^2 \mathrm{d}r$ , which is often referred to as integrated variance.

Corollary 1 In the context of the Dubins-Schwarz theorem, for the local martingale  $M_s = \int_0^s \sigma_{r-} dW_r =$  $B_{[M]_s}$  independence of W and  $\sigma$  is equivalent to independence of B and  $T = [M]$ .

Therefore, the models  $(1)$  and  $(2)$  are equivalent if X is a Brownian motion and  $T_s = \int_0^s \sigma_r^2 dr$ is an absolutely continuous time change. Regarding Clark's independence assumption, we note that independence of  $\sigma$  and X is also equivalent in models (1) and (2); however, this excludes the leverage effect, that is, the usually negative correlation between asset returns and volatility.

Fundamentally, these results are due to the scaling property of Brownian motion  $X$ , which translates spatial scaling  $\sigma X_t$  or model (2) into temporal scaling  $X_{\sigma^2 t}$  or model (1). Also, if Brownian motion is replaced by an  $\alpha$ -stable Lévy process and  $T_t =$  $\int_0^{\iota} \sigma_s^{\alpha} ds$ , the two models (1) and (2) are basically equivalent [25, 26]. No other Lévy process has such a scaling property, and indeed, the models (1) and (2) will be different. If we relate higher volatility to higher market activity, then model (1) suggests that markets move at a higher speed, and model (2) suggests that the volumes traded are higher.

Theorem 2 (Monroe [33]). Every (càdlàg) semimartingale  $Z = (Z_s)_{s \ge 0}$  can be written as a timechanged Brownian motion  $(B_{T_s})_{s\geq 0}$  for a (càdlàg) *family of stopping times*  $(T_s)_{s\geq 0}$  *on a suitably extended* probability space.

In the light of the fundamental theorem of asset pricing (see Fundamental Theorem of Asset Pri**cing**), this means that every arbitrage-free model can be viewed as time-changed Brownian motion. However, this result is of limited use for the construction of simple and natural parametric models.

In the finance literature, we find many asset price models where the base process is chosen to be a Lévy process other than Brownian motion (see, e.g., [12, 13]). Here, we refer to **Time-changed Lévy Process** for a detailed treatment of this class of models.

We also mention Lamperti's representations [27, 28] of continuous-state branching processes and of self-similar Markov processes as time-changed Lévy processes very much in the spirit of the

Dubins-Schwarz Theorem. Salminen and Yor [36] use Lamperti's time change to study Dufresne's functional [20] that arises in the computation of discounted values in certain models of continuously payable perpetuities in actuarial science.

#### **Choice of Time Change**

There are different methods for choosing a time change that is suitable for financial models. Two classes of such processes are particularly popular: subordinators and absolutely continuous time changes [1].

In the finance literature, the terms time change and *subordinator* are sometimes used synonymously. However, in probability theory, the term subordinator describes a particular class of stochastic processes (as defined below) and does not include all time changes.

#### Subordinators

Subordinators are nondecreasing Lévy processes [10, 15, 37] and hence possess stationary and independent increments. They are pure jump processes of possibly infinite activity plus a deterministic linear drift. Clearly, they have no Brownian component and are of finite variation. Important examples include simple Poisson processes, increasing compound Poisson processes, gamma processes, and (tempered) stable subordinators. Note that many popular models in finance are based on time-changed Brownian motion where the time change is chosen to be a subordinator. For example, the variance gamma process [30, 31] can be represented as Brownian motion time-changed by a gamma process, the normal tempered stable process (including the normal inverse gaussian process [2, 3]) can be written as a Brownian motion timechanged by a tempered stable subordinator. Brownian motion, time-changed by an independent subordinator, yields a Lévy process always.

#### Absolutely Continuous Time Changes

Another important class of time changes is given by the class of absolutely continuous time changes of the form  $T_s = \int_0^s \tau_u du$ , for a positive and integrable process  $\tau = (\tau_s)_{s \ge 0}$ . Note that in such a setting T is always continuous, but  $\tau$  can exhibit jumps. The process  $\tau$  is often called *instantaneous* (business)

*activity rate*. Such models have been studied in the context when *X* is a Levy process by Carr ´ *et al.* [12] and [13] among others. The advantage of this model class is that it leads to affine models that are highly analytically tractable (see, e.g., [19, 25]), whereas stochastic integrals with respect to Levy ´ processes are in general not affine. Popular examples for the instantaneous activity rate are given by the Cox– Ingersoll–Ross process and the non-Gaussian Ornstein–Uhlenbeck process [7, 8, 16].

# **Multivariate Setting**

Time-changed stochastic processes are also used in the finance literature to construct multivariate models. Usually, the base process *X* is then assumed to be multivariate (e.g., a multivariate Brownian motion) and the time-change process *T* is still assumed to be univariate ([15, 21] and the references therein). The advantage of such a modeling framework is the fact that such processes are highly analytically tractable and easy to simulate from. However, the range of dependence between the univariate components in such a multivariate model is rather limited (and, in particular, does not even include complete independence). Furthermore, such a model does not allow for an arbitrary choice of univariate models for the components [15]. The mathematical properties of multivariate processes *X* time-changed by a multivariate vector of time changes *T* have recently been studied in [5], but this has so far not been considered as a standard tool for constructing multivariate models in finance. So far, it has been much more common to use multivariate extensions of a stochastic integral (2) to construct multivariate stochastic volatility models, than to use time-changed processes. Finally, note that the concept of subordinators can also be generalized to matrix subordinators [4, 6] and their applicability in financial models is subject to ongoing research (see, e.g., [9, 38] for some first references).

# **Acknowledgments**

We would like to thank Marc Yor and Ole Barndorff-Nielsen for suggesting relevant references. The first author acknowledges financial support by the Center for Research in Econometric Analysis of Time Series, CREATES, funded by the Danish National Research Foundation.

# **References**

- [1] Ane, T. & Geman, H. (2000). Order flow, transaction ´ clock, and normality of asset returns, *The Journal of Finance* **55**(5), 2259–2284.
- [2] Barndorff-Nielsen, O.E. (1997). Normal inverse gaussian distributions and stochastic volatility modelling, *Scandinavian Journal of Statistics* **24**, 1–13.
- [3] Barndorff-Nielsen, O.E. (1998). Processes of normal inverse Gaussian type, *Finance and Stochastics* **2**, 41–68.
- [4] Barndorff-Nielsen, O.E., Maejima, M. & Sato, K.-I. (2006). Some classes of multivariate infinitely divisible distributions admitting stochastic integral representation, *Bernoulli* **12**, 1–33.
- [5] Barndorff-Nielsen, O.E., Pedersen, J. & Sato, K.-I. (2001). Multivariate subordination, selfdecomposability and stability, *Advances in Applied Probability* **33**, 160–187.
- [6] Barndorff-Nielsen, O.E. & Perez-Abreu, V. (2008). ´ Matrix subordinators and related upsilon transformations, *Theory of Probability and its Applications* **52**(1), 1–23.
- [7] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non– Gaussian Ornstein–Uhlenbeck–based models and some of their uses in financial economics (with discussion), *Journal of the Royal Statistical Society, Series B-Statistical Methodology* **63**, 167–241.
- [8] Barndorff-Nielsen, O.E. & Shephard, N. (2002). Econometric analysis of realised volatility and its use in estimating stochastic volatility models, *Journal of the Royal Statistical Society. Series B* **B 64**, 253–280.
- [9] Barndorff-Nielsen, O.E. & Stelzer, R. (2007). Positive–definite matrix processes of finite variation, *Probability and Mathematical Statistics* **27**(1), 3–43.
- [10] Bertoin, J. (1996). *L´evy Processes*, Cambridge University Press, Cambridge.
- [11] Bochner, S. (1949). Diffusion equation and stochastic processes, *Proceedings of the National Academy of Sciences of the United States of America* **85**, 369–370.
- [12] Carr, P., Geman, H., Madan, D.B. & Yor, M. (2003). Stochastic volatility for Levy processes, ´ *Mathematical Finance* **13**(3), 345–382.
- [13] Carr, P. & Wu, L. (2004). Time–changed Levy pro- ´ cesses and option pricing, *Journal of Financial Economics* **71**, 113–141.
- [14] Clark, P.K. (1973). A subordinated stochastic process model with fixed variance for speculative prices, *Econometrica* **41**, 135–156.
- [15] Cont, R. & Tankov, P. (2004). *Financial Modelling With Jump Processes*, *Financial Mathematics Series*, Chapman & Hall, Boca Raton, Florida.
- [16] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). An intertemporal general equilibrium model of asset prices, *Econometrica* **53**, 363–384.
- [17] Doeblin, W. (2000). Sur l'equation de Kolmogoroff, ´ *Les Comptes Rendus de l'Acad´emie des Sciences* **I**(331),

1031–1187. Pli cachete d´ epos ´ e le 26 f ´ evrier 1940, ouvert ´ le 18 mai 2000.

- [18] Dubins, L. & Schwarz, G. (1965). On continuous martingales, *Proceedings of the National Academy of Sciences of the United States of America* **53**(5), 913–916.
- [19] Duffie, D., Filipovic, D. & Schachermayer, W. (2003). Affine processes and applications in finance, *Annals of Applied Probability* **13**, 984–1053.
- [20] Dufresne, D. (1990). The distribution of a perpetuity, with applications to risk theory and pension funding, *Scandinavian Actuarial Journal* **1990**, 39–79.
- [21] Eberlein, E. (2001). Application of generalized hyperbolic Levy motion to finance, in ´ *L´evy Processes: Theory and Applications*, O.E. Barndorff-Nielsen, T. Mikosch & S. Resnick, eds, Birkhauser, Basel, pp. 319–337. ¨
- [22] Geman, H. (2005). From measure changes to time changes in asset pricing, *Journal of Banking and Finance* **29**, 2701–2722.
- [23] Hunt, G. (1957). Markov processes and potentials I, II and III, *Illinois Journal of Mathematics* **1**, 44–93; 316–396; (1958). **2**, 151–213.
- [24] Ito, K. & McKean, H.P. (1965). ˆ *Diffusion Processes and Their Sample Paths*, Springer–Verlag, Berlin.
- [25] Kallsen, J. (2006). A didactic note on affine stochastic volatility models, in *From Stochastic Calculus to Mathematical Finance*, Y. Kabanov, R. Liptser & J. Stoyanov, eds, Springer–Verlag, Berlin, pp. 343–368.
- [26] Kallsen, J. & Shiryaev, A. (2002). Time change representation of stochastic integrals, *Theory of Probability and its Applications* **46**, 522–528.
- [27] Lamperti, J. (1967). Continuous–state branching processes, *Bulletin of The American Mathematical Society* **73**, 382–386.
- [28] Lamperti, J. (1972). *Semi–Stable Markov Processes. I*, *Probability Theory and Related Fields*, Springer–Verlag, Vol. 22, pp. 205–225.
- [29] Levy, P. (1948). ´ *Processus Stochastiques Et Mouvement Brownien*, Gauthier–Villars, Paris.
- [30] Madan, D., Carr, P. & Chang, E. (1998). The variance gamma process and option pricing, *European Finance Review* **2**, 79–105.
- [31] Madan, D.B. & Seneta, E. (1990). The VG model for share market returns, *Journal of Business* **63**, 511–524.
- [32] McKean, H. (2002). Scale and clock, in *Mathematical Finance—Bachelier Congress 2000*, *Springer Finance*,

H. Geman, D. Madan, S. Pliska & T. Vorst, eds, Springer-Verlag, Berlin.

- [33] Monroe, I. (1978). Processes that can be embedded in Brownian motion, *The Annals of Probability* **6**(1), 42–56.
- [34] Protter, P.E. (2004). *Stochastic Integration and Differential Equations*, 2nd Edition, Springer, London.
- [35] Revuz, D. & Yor, M. (2001). *Continuous Martingales and Brownian Motion*, 3rd Edition, Springer, Berlin.
- [36] Salminen, P. & Yor, M. (2005). Perpetual integral functionals as hitting and occupation times, *Electronic Journal of Probability* **10**, 371–419.
- [37] Sato, K. (1999). *L´evy processes and Infinitely Divisible Distributions*, Cambridge University Press, Cambridge.
- [38] Stelzer, R.J. (2007). *Multivariate Continuous time stochastic volatility models driven by a L´evy process*, Dissertation, Technische Universitat M¨ unchen, M ¨ unchen. Urn: ¨ http://d-nb.info/986220337.
- [39] Volkonski, V. (1958). Random time changes in strong Markov processes, *Theory of Probability and its Applications* **3**, 310–326.

# **Further Reading**

- Fu, M., Jarrow, R., Yen, J.-Y. & Elliott, R. (eds) (2007). *Advances in Mathematical Finance*, *Applied and Numerical Harmonic Analysis*, Birkhauser, Boston. ¨
- Jeanblanc, M., Yor, M. & Chesney, M. (2009). *Mathematical Methods for Financial Markets*, *Springer Finance*, Springer-Verlag, Berlin.

# **Related Articles**

**Jump Processes**; **Levy Processes ´** ; **Martingales**; **Normal Inverse Gaussian Model**; **Realized Volatility and Multipower Variation**; **Stochastic Integrals**; **Time-changed Levy Process ´** ; **Variancegamma Model**; **Volatility**.

ALMUT E.D. VERAART & MATTHIAS WINKEL
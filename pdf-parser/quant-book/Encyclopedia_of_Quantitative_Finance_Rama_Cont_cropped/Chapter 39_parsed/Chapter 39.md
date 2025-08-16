# **Equivalence of Probability Measures**

In finance it is often important to consider different probability measures. The statistical measure, commonly denoted by *P*, is supposed to (ideally) reflect the real-world dynamics of financial assets. A risk-neutral measure (*see* **Equivalent Martingale Measures**), often denoted by *Q*, is the measure of choice for the valuation of derivative securities. Prices of traded assets are supposed to be (local) *Q*-martingales, and hence their dynamics (as seen under *Q*) typically differs from their actual behavior (as modeled under *P*). How far can the dynamics with respect to these two measures be away in terms of qualitative behavior? We would not expect that events that do not occur in the real world, in the sense that they have *P*-probability zero, like a stock price exploding to infinity, would have positive *Q*probability in the risk-neutral world. This discussion leads to the notion of absolute continuity.

**Definition 1** *Let P, Q be two probability measures defined on a measurable space (,* F*). We say that Q is absolutely continuous with respect to P, denoted by Q P, if all P-zero sets are also Q-zero sets. If Q P and P Q we say that P and Q are equivalent, denoted by P* ∼ *Q. In other words, two equivalent measures have the same zero sets.*

Let *Q P*. By the Radon–Nikodym theorem there exists a *density Z* = d*Q/*d*P* so that for *f* ∈ *L*<sup>1</sup> *(Q)* we can calculate its expectation with respect to *Q* by

$$E_{\mathcal{Q}}[f] = E_{\mathcal{P}}[Zf] \tag{1}$$

Note that if *Q* is absolutely continuous, but not equivalent to *P*, then we have *P (Z* = 0*) >* 0.

We now look at a dynamic picture, and assume that we also have a filtration *(*F*t)*0≤*t*≤*<sup>T</sup>* at our disposal where *T* is some fixed finite time horizon. For *t* ≤ *T* let

$$Z_t = E_P \left[ Z | \mathcal{F}_t \right] \tag{2}$$

We call the martingale *Z* = *(Zt)* the *density process* of *Q*. The *Bayes formula* tells us how to calculate conditional expectations with respect to *Q* in terms of *P*. Let 0 ≤ *s* ≤ *t* ≤ *T* and *f* be F*t*-measurable and in *L*<sup>1</sup> *(Q)*. We then have

$$Z_{s}E_{Q}\left[f|\mathcal{F}_{s}\right] = E_{P}\left[Z_{t}f|\mathcal{F}_{s}\right] \tag{3}$$

As consequence of Bayes' formula, we get that if *M* is a *Q*-martingale then *ZM* is a *P*-martingale and *vice versa*. Hence, we can turn any *Q*-martingale into a *P*-martingale by just multiplying it with the density process. It follows that the martingale property is *not* invariant under equivalent measure changes.

There are, however, a couple of important objects like stochastic integrals and quadratic variations which do remain invariant under equivalent measure changes although they depend, by their definition, *a priori* on some probability measure. Let us illustrate this in case of the quadratic variation of a semimartingale *S*. This is defined to be the limit in *P*-probability of the sum of the squared *S*-increments over a time grid, for vanishing mesh size. It is elementary that convergence in *P*-probability implies convergence in *Q*-probability if *Q P*, and thus convergence in *P*-probability is equivalent to the convergence in *Q*-probability when *P* and *Q* are equivalent. This implies, for example, that quadratic variations remain the same under a change to an equivalent probability measure.

The compensator or angle bracket process, however, is *not* invariant with respect to equivalent measure changes. It is defined (for reasonable processes *S*) as the process *S* one has to subtract from the quadratic variation process [*S*] to turn it into a local martingale. But, as we have seen, the martingale property typically gets lost by switching the measure. As an example, consider a Poisson process *N* with intensity *λ*. We have [*N*] = *N*, so the compensator equals *λt*. As we shall see below, the effect of an equivalent measure change is that the intensity changes as well, to *µ*, say, so the compensator under the new measure would be *µt*.

# **Girsanov's Theorem**

As we have discussed above, the martingale property is not preserved under measure changes. Fortunately, it turns out that at least the semimartingale property is preserved. Moreover, it is possible to state the precise semimartingale decomposition under the new measure *Q*. This result is known in the literature as the *Girsanov's theorem*, although it was rather Cameron and Martin who proved a first version of it in a Wiener space setting. Later on it was extended in various levels of generality by Girsanov, Meyer, and Lenglart, among many others.

Let us first give some examples. They are all the consequences of the general formulation of Girsanov's theorem to be given below.

1. Let B be a P-Brownian motion,  $\mu \in \mathbb{R}$ , and define an equivalent measure  $Q$  by the stochastic exponential

$$\frac{\mathrm{d}Q}{\mathrm{d}P} = \mathcal{E}(-\mu B)_T = \exp\left(-\mu B_T - \frac{1}{2}\mu^2 T\right) \tag{4}$$

Then  $\widehat{B} = B + \mu t$  is a Q-Brownian motion (up to time  $T$ ). Alternatively stated, the semimartingale decomposition of B under O is  $B = \widehat{B}$  - $\mu t$ . Hence the effect of the measure change is to add a drift term to the Brownian motion.

2. Let  $N_t - \lambda t$  be a compensated Poisson process on an interval [0, T] with P-intensity  $\lambda > 0$ , and let  $\kappa > 0$ . Define an equivalent measure  $Q$  by

$$\frac{\mathrm{d}Q}{\mathrm{d}P} = \mathrm{e}^{-\kappa\lambda T} \prod_{0 < s \le T} (1 + \kappa \Delta N_s)$$
$$= \mathrm{e}^{-\kappa\lambda T} (1 + \kappa)^{N_T}$$
$$= \exp\left(N_T \ln\left(1 + \kappa\right) - \kappa\lambda T\right) \qquad (5)$$

Then N is a Poisson process on  $[0, T]$  under Q with intensity  $(1 + \kappa) \lambda$ . The process  $N_t - (1 + \kappa) \lambda t$ is a compensated Poisson process under  $Q$  and thus a O-martingale. Hence the effect of the measure change is to change the intensity of the Poisson process, or in other words, to add a drift term to the compensated Poisson process.

One of the most important applications of measure changes in mathematical finance is to find martingale measures for the price process  $S$  of some risky asset.

**Definition 2** A martingale measure for  $S$  is a probability measure  $Q$  such that  $S$  is a  $Q$ -local martingale.

Let us now state a general form of Girsanov's theorem. It is not the most general setting, though, since we will assume that  $Q$  is equivalent to  $P$ which suffices for most applications in finance. This is due to the fact that one would often choose  $Q$ 

to be a martingale measure for the price process, and then equivalence is a necessary condition to exclude arbitrage opportunities [1]. There is, however, also a result which covers the case where  $O$  is only absolutely continuous, but not equivalent to  $P$ , and which has been proven by Lenglart [2].

Theorem 1 (Girsanov's Theorem: Standard **Version).** Let  $P \sim Q$ , with density process given by

$$Z_t = E\left[\left.\frac{\mathrm{d}Q}{\mathrm{d}P}\right|\mathcal{F}_t\right] \tag{6}$$

If S is a semimartingale under  $P$  with decomposition  $S = M + A$  (here M is a local martingale, and A a process of locally finite variation), then  $S$  is a semimartingale under  $Q$  as well and has decomposition

$$S = \left(M - \int \frac{1}{Z} d[Z, M]\right) + \left(A + \int \frac{1}{Z} d[Z, M]\right) \tag{7}$$

In particular,  $M - \int \frac{1}{Z} d[Z, M]$  is a local Qmartingale.

In situations where the process  $S$  may exhibit jumps, it is often more convenient to apply a version of Girsanov which uses the angle bracket instead of the quadratic covariation.

Theorem 2 (Girsanov's Theorem: Predictable **Version).** Let  $P \sim Q$ , with density process as above, and  $S = M + A$  be a P-semimartingale. Given that  $\langle Z, M \rangle$  exists (with respect to P), then the decomposition of  $S$  under  $Q$  is

$$S = \left( M - \int \frac{1}{Z_{-}} d\langle Z, M \rangle \right) + \left( A + \int \frac{1}{Z_{-}} d\langle Z, M \rangle \right) \tag{8}$$

### Here $Z_{-}$ denotes the left-continuous version of Z.

Whereas the standard version of Girsanov's theorem always works, we need an integrability condition (existence of  $\langle Z, M \rangle$ ) for the predictable version.

However, in case  $S = M + A$  for a local martingale  $M$  and a finite variation process  $A$ , it is rarely the case in a discontinuous framework that  $dA \ll d[M]$ , whereas it is quite natural in financial applications that  $dA \ll d \langle M \rangle$  (see below).

In mathematical finance, these results are often applied to find a martingale measure for the price process S. Consider, for example, the Bachelier model where  $S = B + \mu t$  is a Brownian motion plus drift. If we now take as above the measure change as given by a density process  $Z_t = \exp\left(-\mu B_t - \frac{1}{2}\mu^2 t\right)$ , then we have (since  $dZ = -\mu Z dB$ )

$$A + \int \frac{1}{Z} d[Z, M] = \mu t + \int \frac{1}{Z} d\left[-\mu \int Z dB, B\right]$$
$$= \mu t + \int \frac{1}{Z} d\left(-\mu \int Z dt\right)$$
$$= 0 \tag{9}$$

According to Girsanov's theorem (here the standard version coincides with the predictable one since  $S$  is continuous), the price process  $S$  is therefore a  $Q$ -local martingale (and, in fact, a Brownian motion according to Lévy's characterization), and hence  $Q$ is a martingale measure for  $S$ .

More generally, Girsanov's theorem implies an important structural result for the price process  $S$ in an arbitrage-free market. As has been mentioned above, it is essentially true that some no-arbitrage property implies the existence of an equivalent martingale measure Q for  $S = M + A$ , with density process  $Z$ . Therefore, we must have by the predictable version (8), given that  $\langle Z, M \rangle$  exists, that

$$A = -\int \frac{1}{Z_{-}} \mathrm{d} \left\langle Z, M \right\rangle \tag{10}$$

to get that  $S$  is a local  $Q$ -martingale. As it follows from the so-called Kunita-Watanabe inequality that

$$d\langle Z,M\rangle \ll d\langle M\rangle \tag{11}$$

(here  $\langle Z, M \rangle$  respectively  $\langle M \rangle$  are interpreted as the associated measures on the nonnegative real line), we conclude that

$$\mathrm{d}A \ll \mathrm{d}\left\langle M\right\rangle \tag{12}$$

and hence there exists some predictable process  $\lambda$ such that

$$S = M + \int \lambda \, \mathrm{d} \langle M \rangle \tag{13}$$

For example, in the Bachelier model  $S = B + \mu t$ we have that  $\langle B \rangle_t = t$ , and hence  $\lambda$  equals the constant  $\mu$ .

The predictable version of Girsanov's theorem can now be applied to remove the drift  $\int \lambda d \langle M \rangle$  as follows: we define a probability measure  $Q$  via

$$\frac{\mathrm{d}Q}{\mathrm{d}P} = \mathcal{E}\bigg(-\int \lambda \,\mathrm{d}M\bigg)_T \tag{14}$$

where  $\mathcal{E}$  denotes the Doléans-Dade stochastic exponential, assuming that  $\mathcal{E}(-\int \lambda \mathrm{d}M)$  is a martingale. The corresponding density process  $Z$ therefore satisfies the stochastic differential equation

$$dZ = -Z_{-}\lambda \, dM \tag{15}$$

It follows that

$$\langle Z, M \rangle = \left\langle -\int Z_{-\lambda} \, \mathrm{d}M, M \right\rangle = -\int Z_{-\lambda} \mathrm{d} \, \langle M \rangle \tag{16}$$

and

$$S = M + \int \lambda d \langle M \rangle = M - \int \frac{1}{Z_{-}} d \langle Z, M \rangle \quad (17)$$

is by the (predictable version) of the Girsanov theorem a local  $Q$ -martingale: the drift has been removed by the measure change.

This representation of  $S$  has an important consequence for the structure of martingale measures, provided the so-called *structure condition* holds:

$$\int_0^T \lambda_s^2 \mathrm{d} \, \langle M \rangle_s < \infty \qquad P-\text{a.s.} \tag{18}$$

In that case, the remarkable conclusion we can draw from  $(13)$  is that the existence of an equivalent martingale measure for  $S$  implies that  $S$  is a special semimartingale, for example, its finite variation part is predictable and therefore the semimartingale decomposition (13) is unique. Moreover, the following result holds.

**Proposition 1** Let  $Q$  be an equivalent martingale measure for S, and the structure condition (18) hold. Then the density process  $Z$  of  $Q$  with respect to  $P$  is given by the stochastic exponential

$$Z = \mathcal{E}\bigg(-\int \lambda \,\mathrm{d}M + L\bigg) \tag{19}$$

*for some process L such that L as well as* [*M,L*] *are local P-martingales. The converse statement is true as well, assuming that all involved processes are locally bounded: if Q is a probability measure whose density process can be written like in equation (19) with L as above, then Q is a martingale measure for S.*

This result is fundamental in incomplete markets (*see* **Complete Markets**), where there are many equivalent martingale measures for the price process *S*. Indeed, any choice of *L* as in the statement of the proposition gives one particular pricing measure.

In applications in finance, the density process *Z* can also be interpreted in terms of a **change of numeraire**.

# **References**

- [1] Delbaen, F. & Schachermayer, W. (2006). *The Mathematics of Arbitrage*, Springer, Berlin.
- [2] Protter, P.E. (2005). *Stochastic Integration and Differential Equations*, 2nd Edition, Version 2.1, Springer, Heidelberg.

# **Related Articles**

**Change of Numeraire**; **Equivalent Martingale Measures**; **Semimartingale**; **Stochastic Exponential**; **Stochastic Integrals**.

THORSTEN RHEINLANDER ¨
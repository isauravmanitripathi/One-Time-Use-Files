## **Stochastic Exponential**

Let X be a semimartingale with  $X_0 = 0$ . Then there exists a unique semimartingale  $Z$  that satisfies the equation

$$Z_t = 1 + \int_0^t Z_{s-} \, \mathrm{d}X_s \tag{1}$$

It is called the *stochastic exponential* of  $X$  and is denoted by  $\mathcal{E}(X)$ . Sometimes the stochastic exponential is also called the *Doléans exponential*, after the French mathematician Catherine Doléans-Dade, Note that  $Z_{-}$  denotes the left-limit process, so that the integrand in the stochastic integral is predictable.

We first give some examples as follows:

1. If  $B$  is a Brownian motion, then an application of Itô's formula reveals that

$$\mathcal{E}(B)_t = \exp\left(B_t - \frac{1}{2}t\right) \tag{2}$$

2. Likewise, the stochastic exponential for a compensated Poisson process  $N - \lambda t$  is given as

$$\mathcal{E}(N - \lambda t)_t = \exp\left(-\frac{1}{2}\lambda t\right) \times 2^{N_t}$$
$$= \exp\left(\ln(2)N_t - \frac{1}{2}\lambda t\right) \quad (3)$$

3. The classical Samuelson model for the evolution of stock prices is also given as a stochastic exponential. The price process  $S$  is modeled here as the solution of the stochastic differential eauation

$$\frac{\mathrm{d}S_t}{S_t} = \sigma \,\mathrm{d}B_t + \mu \,\mathrm{d}t \tag{4}$$

Here, we consider the constant trend coefficient  $\mu$ , the volatility  $\sigma$ , and a Brownian motion B. The solution to this equation is

$$S_{t} = \mathcal{E}(\sigma B_{t} + \mu t)$$
  
=  $\exp\left(\sigma B_{t} + \left(\mu - \frac{1}{2}\sigma^{2}\right)t\right)$  (5)

For a general semimartingale  $X$  as above, the expression for the stochastic exponential is

$$Z_{t} = \exp\left(X_{t} - \frac{1}{2} \left[X\right]_{t}\right) \prod_{0 < s \le t} (1 + \Delta X_{s})$$
$$\times \exp\left(-\Delta X_{s} + \frac{1}{2} \left(\Delta X_{s}\right)^{2}\right) \tag{6}$$

where the possibly infinite product converges. Here  $[X]$  denotes the *quadratic variation* process of X.

In case  $X$  is a local martingale vanishing at zero with  $\Delta X > -1$ , then  $\mathcal{E}(X)$  is a strictly positive local martingale. This property renders the stochastic exponential very useful as a model for asset prices in case the price process is directly modeled under a martingale measure, that is, in the risk neutral world. However, considering some Lévy-process  $X$ , many authors prefer to model the price process as  $exp(X)$ rather than  $\mathcal{E}(X)$  since this form is better suited for applying Laplace transform methods. In fact, the two representations are equivalent because starting with a model of the form  $exp(X)$ , one can always find a Lévy-process  $\widehat{X}$  such that  $\exp(X) = \mathcal{E}(\widehat{X})$ and vice versa (in case the stochastic exponential is positive). The detailed calculations involving characteristic triplets can be found in Goll and Kallsen [3].

Finally, for any two semimartingales  $X, Y$  we have the formula

$$\mathcal{E}(X)\,\mathcal{E}(Y) = \mathcal{E}(X+Y+[X,Y])\tag{7}$$

which generalizes the multiplicative property of the usual exponential function.

## **Martingale Property**

The most crucial issue from the point of mathematical finance is that, given  $X$  is a local martingale, the stochastic exponential  $\mathcal{E}(X)$  may fail to be a martingale. Let us give an illustration of this phenomenon.

We assume that the price process of a risky asset evolves as the stochastic exponential  $Z_t =$  $\exp\left(B_t - \frac{1}{2}t\right)$  where *B* is a standard Brownian motion starting in zero. Since one-dimensional Brownian motion is almost-surely recurrent, and therefore gets negative for arbitrarily large times, zero must be an accumulation point of  $Z$ . As  $Z$  can be written as a stochastic integral of  $B$ , it is a local martingale, and hence a supermartingale by Fatou's lemma because it is bounded from below. We conclude by the supermartingale convergence theorem that  $Z$  converges (necessarily to zero). This shows that

$$\lim_{t \to \infty} Z_t = 0 \qquad P - \text{a.s} \tag{8}$$

Holding one stock of the asset with price process  $Z$  therefore amounts to following a suicide strategy, since one starts with an initial capital of one and ends up with no money at all at time infinity. The mathematical explanation for this phenomenon is that  $Z$  is not a martingale on the closed interval  $[0,\infty]$ , or equivalently, the family  $\{Z_t, t \in \mathbb{R}_+\}$  is not uniformly integrable.

What is more, one of the main applications of stochastic exponentials is that they are intricately related to measure changes since they qualify as candidates for density processes (see Girsanov's theorem). Let us fix a filtered probability space  $(\Omega, \mathcal{F}_{\infty}, (\mathcal{F}_{t}), P)$ . In case the stochastic exponential is positive, we may define a new measure  $Q$  on  $\mathcal{F}_{\infty}$  via

$$\frac{\mathrm{d}Q}{\mathrm{d}P} = Z_{\infty} \tag{9}$$

If Z is a uniformly integrable martingale, then  $Q$ is a probability measure since  $E[Z_{\infty}] = Z_0 = 1$ . On the other hand, if  $Z$  is a strict local martingale, hence a strict supermartingale, then we get  $Q(\Omega) =$  $E[Z_{\infty}] < 1$ . It is therefore of paramount interest to have criteria at hand for stochastic exponentials to be true martingales. We first focus on the continuous case.

Theorem 1 (Kazamaki's Criterion). Let  $M$  be a continuous local martingale. Suppose

$$\sup_{T} E\left[\exp\left(\frac{1}{2}M_{T}\right)\right] < \infty \tag{10}$$

where the supremum is taken over all bounded stopping times T. Then  $\mathcal{E}(M)$  is a uniformly integrable *martingale.* 

A slightly weaker result, which, however, is often easier to apply, is given by the following criterion.

Theorem 2 (Novikov's Criterion). Let  $M$  be a continuous local martingale. Suppose

$$E\left[\exp\left(\frac{1}{2}\left[M\right]_{\infty}\right)\right] < \infty \tag{11}$$

Then  $\mathcal{E}(M)$ uniformly is  $a$ integrable martingale.

Nevertheless, these results are still not applicable in many practically important situations, for example, if one wants to construct martingale measures in stochastic volatility models driven by Brownian motions. In that case, the following result taken from Liptser and Shiryaev [8] often turns out to be useful.

**Theorem 3** Let T be a finite time horizon,  $\vartheta$  a predictable process with

$$P\left(\int_0^T \vartheta_s^2 \, \mathrm{d}s < \infty\right) = 1 \tag{12}$$

and  $B$  a Brownian motion. Provided that there is  $\varepsilon > 0$  such that

$$\sup_{0 \le t \le T} E\left[\exp\left(\varepsilon \vartheta_t^2\right)\right] < \infty \qquad P - \text{a.s.} \tag{13}$$

then the stochastic exponential  $\mathcal{E}(\int \vartheta dB)$  is a martingale on  $[0, T]$ .

Let us now turn to the discontinuous case. A generalization of Novikov's criterion has been obtained by Lepingle and Mémin [7] where more results in this direction can be found.

**Theorem 4** Let  $M$  be a locally bounded local P-martingale with  $\Delta M > -1$ . If

$$E\left[\exp\left(\frac{1}{2}\left[M^{\rm c}\right]_{\infty}\right)\prod_{t}\left(1+\Delta M_{t}\right)\right]$$
$$\times\exp\left(-\frac{\Delta M_{t}}{1+\Delta M_{t}}\right)\right]<\infty\qquad(14)$$

then  $\mathcal{E}(M)$  is a uniformly integrable martingale. Here  $M^c$  denotes the continuous local martingale part of  $M$ .

The situation is particularly transparent for Lévy processes; see Cont and Tankov [1].

**Theorem 5** If  $M$  is both a Lévy process and a local martingale, then its stochastic exponential  $\mathcal{E}(M)$ (given that it is positive) is already a martingale.

Alternative conditions for ensuring that stochastic exponentials are martingales in case of Brownian motion driven stochastic volatility models have been provided in Hobson [4] as well as in Wong and Heyde [9]. Moreover, Kallsen and Shiryaev [6] give results generalizing and complementing the criterions in Lepingle and Memin [7]. In case of local ´ martingales of stochastic exponential form E*(X)*, where *X* denotes one component of a multivariate affine process, Kallsen and Muhle-Garbe [5] give sufficient conditions for *M* to be a true martingale. Finally, there are important links between stochastic exponentials of *BMO*-martingales, reverse Holder ¨ inequalities, and weighted norm inequalities (i.e., inequalities generalizing martingale inequalities to certain semimartingales); compare Doleans-Dade and ´ Meyer [2].

## **References**

- [1] Cont, R. & Tankov P. (2003). *Financial Modelling with Jump Processes*, Chapman & Hall/CRC Press, Boca Raton.
- [2] Doleans-Dade, C. & Meyer, P.A. (1979). In ´ egalit ´ es de ´ normes avec poids, *S´eminaire de Probabilit´es de Strasbourg* **13**, 313–331.

- [3] Goll, T. & Kallsen, J. (2000). Optimal portfolio with logarithmic utility, *Stochastic Processes and their Applications* **89**, 91–98.
- [4] Hobson, D. (2004). Stochastic volatility models, correlation and the *q*-optimal measure, *Mathematical Finance* **14**, 537–556.
- [5] Kallsen, J. & Muhle-Garbe, J. (2007). *Exponentially Affine Martingales and Affine Measure Changes*, preprint, TU Munchen. ¨
- [6] Kallsen, J. & Shiryaev, A.N. (2002). The cumulant process and Esschers's change of measure, *Finance and Stochastics* **6**, 397–428.
- [7] Lepingle, D. & Memin, J. (1978). Sur l'int ´ egrabilit ´ e´ uniforme des martingales exponentielles, *Zeitschrift f¨ur Wahrscheinlichkeitstheorie und verwandte Gebiete* **42**, 175–203.
- [8] Liptser, R. & Shiryaev, A.N. (1977). *Statistics of Random Processes I*, Springer, Berlin.
- [9] Wong, B. & Heyde, C.C. (2004). On the martingale property of stochastic exponentials, *Journal of Probability and its Applications* **41**, 654–664.

THORSTEN RHEINLANDER ¨
## **Minimal Entropy Martingale Measure**

Consider a stochastic process  $S = (S_t)_{t \ge 0}$  on a probability space  $(\Omega, \mathcal{F}, P)$  and adapted to a filtration  $\mathbb{F} = (\mathcal{F}_t)_{t \ge 0}$ . Each  $S_t$  takes values in  $\mathbb{R}^d$  and models the discounted prices at time  $t$  of  $d$  basic assets traded in a financial market. An equivalent local martingale measure (ELMM) for S, possibly on  $[0, T]$ for a time horizon  $T < \infty$ , is a probability measure  $Q$  equivalent to the original (historical, real-world) measure P (on  $\mathcal{F}_T$ , if there is a T) such that S is a local Q-martingale (on  $[0, T]$ , respectively); see **Equivalent Martingale Measures.** If  $S$  is a nonnegative  $P$ -semimartingale, the fundamental theorem of asset pricing says that the existence of an ELMM  $Q$ for  $S$  is equivalent to the absence-of-arbitrage condition (NFLVR) that  $S$  admits no free lunch with vanishing risk; see Fundamental Theorem of Asset Pricing.

**Definition 1** *Fix a time horizon T* <  $\infty$ *. An ELMM*  $Q^{E}$  for S on [0, T] is called minimal entropy martingale measure (MEMM) if  $O^E$  minimizes the relative entropy  $H(O|P)$  over all ELMMs O for S on [0, T].

Recall that the *relative entropy* is defined as

$$H(Q|P) := \begin{cases} E_P \left[ \frac{\mathrm{d}Q}{\mathrm{d}P} \log \frac{\mathrm{d}Q}{\mathrm{d}P} \right] & \text{if } Q \ll P \\ +\infty & \text{otherwise} \end{cases} \quad (1)$$

This is an example of the general concept of an  $f$ divergence of the form

$$D_{f}(Q|P) := \begin{cases} E_{P} \left[ f\left(\frac{\mathrm{d}Q}{\mathrm{d}P}\right) \right] & \text{if } Q \ll P \\ +\infty & \text{otherwise} \end{cases} \quad (2)$$

where f is a convex function on  $[0, \infty)$ ; see [26, 49], or [22] for a number of examples. The minimizer  $Q^{*,f}$  of  $D_f(\cdot|P)$  is then called *f*-optimal *ELMM*.

In many situations arising in mathematical finance, f-optimal ELMMs come up via duality from expected utility maximization problems; see **Expected Utility Maximization: Duality Methods;** Expected Utility Maximization. One starts with a utility function  $U$  (see **Utility Function**) and obtains  $f$  (up to an affine function) as the convex conjugate of  $U$ , that is,

$$f(y) - \alpha y - \beta = \sup_{x} (U(x) - xy) \tag{3}$$

Finding  $Q^{*,f}$  is then the dual to the primal problem of maximizing the expected utility

$$\vartheta \mapsto E\left[U\left(x_0 + \int_0^T \vartheta_r \, \mathrm{d}S_r\right)\right] \tag{4}$$

from terminal wealth over allowed investment strategies  $\vartheta$ . Moreover, under suitable conditions, the solutions  $Q^{*,f}$  and  $\vartheta^{*,U}$  are related by

$$\frac{\mathrm{d}Q^{*,f}}{\mathrm{d}P} = \text{const.} \ U' \left( x_0 + \int_0^T \vartheta_r^{*,U} \, \mathrm{d}S_r \right) \quad (5)$$

More details can, for instance, be found in [26, 41, 46, 67, 68]. Relative entropy comes up with  $f_E(y) =$  $y \log y$  when one starts with the exponential utility functions  $U_{\alpha}(x) = -e^{-\alpha x}$  with risk aversion  $\alpha > 0$ . The duality in this special case has been studied in detail in [8, 18, 40].

Since  $f_E$  is strictly convex, the minimal entropy martingale measure is always unique. If  $S$  is locally bounded, the MEMM (on  $[0, T]$ ) exists if and only if there is at least one ELMM  $O$  for  $S$  on  $[0, T]$ with  $H(Q|P) < \infty$  [21]. For general unbounded S, the MEMM need not exist; [21] contains a counterexample, and [1] shows how the duality above will then fail. In [21], it is also shown that the MEMM is automatically equivalent to  $P$ , even if it is defined as the minimizer of  $H(Q|P)$  over all P-absolutely continuous local martingale measures for S on  $[0, T]$ , provided that there exists some ELMM  $Q$  for  $S$  on [0, T] with  $H(Q|P) < \infty$ . Moreover, the density of  $Q^E$  with respect to P on  $\mathcal{F}_T$  has a very specific form; it is given by

$$\left. \frac{\mathrm{d}Q^{E}}{\mathrm{d}P} \right|_{\mathcal{F}_{T}} = Z_{T}^{E} = Z_{0} \exp \left( \int_{0}^{T} \vartheta_{r}^{E} \, \mathrm{d}S_{r} \right) \quad (6)$$

for some constant  $Z_0 > 0$  and some predictable Sintegrable process  $\vartheta^E$ . This has been proved in [21] for models in finite discrete time and in [26, 28] in general; see also [23] for an application to finding optimal strategies in a Lévy process setting. Note,

however, that representation  $(2)$  holds only at the time horizon,  $T$ ; the density process

$$Z_{t}^{E} = \frac{\mathrm{d}Q^{E}}{\mathrm{d}P}\bigg|_{\mathcal{F}_{t}} = E_{P}\left[Z_{T}^{E}\,\big|\,\mathcal{F}_{t}\right], \quad 0 \leq t \leq T \quad (7)$$

is usually quite difficult to find. We remark that the above results on both the equivalence to  $P$  and the structure of the  $f_E$ -optimal  $Q^E$  have versions for more general  $f$ -divergences [26]. (Essentially, equation  $(2)$  is relation  $(1)$  in the case of exponential utility, but it can also be proved directly without using general duality.)

The history of the minimal entropy martingale measure  $Q^E$  is not straightforward to trace. A general definition and an authoritative exposition are given by Frittelli [21]. However, the idea of the so-called minimax measures to link martingale measures via duality to utility maximization already appears, for instance, in  $[30, 31, 41]$ ; see also  $[8]$ . Other early contributors include Miyahara [53], who used the term "canonical martingale measure", and Stutzer [70]; some more historical comments and references are contained in [71]. Even before, in [20], it was shown that the property defining the MEMM is satisfied by the so-called minimal martingale measure if  $S$  is continuous and the so-called mean-variance trade-off of  $S$  has constant expectation over all ELMMs for  $S$ ; see also Minimal Martingale Measure. The most prominent example for this occurs when  $S$  is a Markovian diffusion [53].

After the initial foundations, work on the MEMM has mainly concentrated on three major areas. The first aims to determine or describe the MEMM and, in particular, its density process  $Z^E$  more explicitly in specific models. This has been done, among others, for the following:

- stochastic volatility models: see [9, 10, 35, 62, 63], and compare also Volatility; Barndorff-Nielsen and Shephard (BNS) Models;
- jump-diffusions [54]; and
- Lévy processes (see Lévy Processes), both in general and in special settings: see [36] for an overview and  $[42, 43]$  for some examples. In particular, many studies have considered exponential Lévy models (see Exponential Lévy **Models**) where  $S = S_0 \mathcal{E}(L)$  and L is a Lévy process under  $P$ . There, the existence of the MEMM  $Q^E$  reduces to an analytical condition on the Lévy triplet of L. Moreover,  $Q^E$  is then

given by an Esscher transform (see Esscher **Transform**) and  $L$  is again a Lévy process under  $Q^{E}$ ; see, for instance, [13, 19, 24, 39].

For continuous semimartingales  $S$ , an alternative approach is to characterize  $Z^E$  via semimartingale backward equations or backward stochastic differential equations [50, 52]. The results in [56, 57] use a mixture of the above ideas in a specific class of models.

The second major area is concerned with convergence questions. Several authors have proved, in several settings and with various techniques, that the minimal entropy martingale measure  $Q^E$  is the limit, as  $p \searrow 1$ , of the so-called *p*-optimal martingale measures obtained by minimizing the  $f$ -divergence associated to the function  $f(y) = y^p$ . This line of research was initiated in [27, 28], and later contributions include [39, 52, 65]. In [45, 60], this convergence is combined with the general duality  $(1)$ from utility maximization in order to obtain convergence results for optimal wealths and strategies as well.

The third, and by far the most important area of research on the MEMM, is centered on its link to the exponential utility maximization problem; see  $[8, 18]$ for a detailed exposition of this issue. More specifically, the MEMM is very useful when one studies the valuation of contingent claims by (exponential) *utility* indifference valuation; see Utility Indifference Val**uation.** To explain this, we fix an initial capital  $x_0$ and a random payoff  $H$  due at time  $T$ . The maximal expected utility one can obtain by trading in  $S$  via some strategy  $\vartheta$ , if one starts with  $x_0$  and has to pay out  $H$  in  $T$ , is

$$\sup_{\vartheta} E\left[U\left(x_0 + \int_0^T \vartheta_r \, \mathrm{d}S_r - H\right)\right] =: u(x_0; -H) \tag{8}$$

and the *utility indifference value*  $x_H$  is then implicitly defined by

$$u(x_0 + x_H; -H) = u(x_0; 0) \tag{9}$$

Hence,  $x_H$  represents the monetary compensation required for selling  $H$  if one wants to achieve utility indifference at the optimal investment behavior. If  $U = U_{\alpha}$  is exponential, its multiplicative structure

makes the analysis of the utility indifference value  $x_H$ tractable, in remarkable contrast to all other classical utility functions. Moreover,  $u(x_0; -H)$  as well as  $x_H$ and the optimal strategy  $\vartheta^*_H$  can be described with the help of a minimal entropy martingale measure (defined here with respect to a new,  $H$ -dependent reference measure  $P_H$  instead of  $P$ ). This topic has first been studied in [4, 58, 59, 64]; later work has examined intertemporally dynamic extensions [5, 51], descriptions via backward stochastic differential equations (BSDEs) in specific models [6, 51], extensions to more general payoff structures [38, 47, 48, 61], and so on [29, 37, 69].

Apart from the above, there are a number of other areas where the minimal entropy martingale measure has come up; these include the following:

- option price comparisons [7, 11, 32-34, 55]; e
- generalizations or connections to other optimal ELMMs [2, 14, 15, 66]); see also Minimal **Martingale Measure** and [20];
- utility maximization with a random time horizon  $\bullet$ [12]:
- good deal bounds [44]; see also Good-deal Bounds: and
- a calibration game [25].

There are also many papers that simply choose the MEMM as pricing measure for option pricing applications; especially in papers from the actuarial literature, this approach is often motivated by the connections between the MEMM and the Esscher transformation. Finally, we mention that the idea of looking for a martingale measure subject to a constraint on relative entropy also naturally comes up in calibration problems; see, for instance, [3, 16, 17] and **Model Calibration**.

## References

- Acciaio, B. (2005). Absolutely continuous optimal mar-[1] tingale measures, Statistics and Decisions 23.  $81 - 100.$
- Arai, T. (2001). The relations between minimal martin-[2] gale measure and minimal entropy martingale measure, Asia-Pacific Financial Markets 8, 137–177.
- [3] Avellaneda, M. (1998). Minimum-relative-entropy calibration of asset pricing models, International Journal of Theoretical and Applied Finance 1, 447–472.
- [4] Becherer, D. (2003). Rational hedging and valuation of integrated risks under constant absolute risk

aversion. Insurance: Mathematics and Economics 33.  $1 - 28.$ 

- Becherer, D. (2004). Utility-indifference hedging and [5] valuation via reaction-diffusion systems, Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 460, 27-51.
- [6] Becherer, D. (2006). Bounded solutions to backward SDEs with jumps for utility optimization and indifference hedging, Annals of Applied Probability 16, 2027-2054.
- Bellamy, N. (2001). Wealth optimization in an incom-[7] plete market driven by a jump-diffusion process, Journal of Mathematical Economics 35, 259-287.
- [8] Bellini, F. & Frittelli, M. (2002). On the existence of minimax martingale measures, Mathematical Finance 12.  $1-21$ .
- [9] Benth, F.E. & Karlsen, K.H. (2005). A PDE representation of the density of the minimal entropy martingale measure in stochastic volatility markets, Stochastics 77,  $109 - 137.$
- [10] Benth, F.E. & Meyer-Brandis, T. (2005). The density process of the minimal entropy martingale measure in a stochastic volatility model with jumps, Finance and Stochastics 9, 563-575.
- [11] Bergenthum, J. & Rüschendorf, L. (2007). Convex ordering criteria for Lévy processes, Advances in Data Analysis and Classification 1, 143-173.
- [12] Blanchet-Scalliet, C., El Karoui, N. & Martellini, L. (2005). Dynamic asset pricing theory with uncertain time-horizon, Journal of Economic Dynamics and Control 29, 1737-1764.
- [13] Chan, T. (1999). Pricing contingent claims on stocks driven by Lévy processes, Annals of Applied Probability 9, 504-528.
- [14] Choulli, T. & Stricker, C. (2005). Minimal entropy-Hellinger martingale measure in incomplete markets, Mathematical Finance 15, 465-490.
- [15] Choulli, T. & Stricker, C. (2006). More on minimal entropy-Hellinger martingale measure, Mathematical Finance 16, 1-19.
- [16] Cont, R. & Tankov, P. (2004). Nonparametric calibration of jump-diffusion option pricing models, Journal of Computational Finance 7,  $1-49$ .
- [17] Cont, R. & Tankov, P. (2006). Retrieving Lévy processes from option prices: regularization of an ill-posed inverse problem, SIAM Journal on Control and Optimization 45,  $1 - 25.$
- [18] Delbaen, F., Grandits, P., Rheinländer, T., Samperi, D., Schweizer, M. & Stricker, C. (2002). Exponential hedging and entropic penalties, Mathematical Finance 12,  $99 - 123$ .
- [19] Esche, F. & Schweizer, M. (2005). Minimal entropy preserves the Lévy property: how and why, Stochastic Processes and their Applications 115, 299-327.
- [20] Föllmer, H. & Schweizer, M. (1991). Hedging of contingent claims under incomplete information, in M.H.A. Davis & R.J. Elliott, eds, Applied Stochastic Analysis,
## **Minimal Martingale** Measure

Let  $S = (S_t)$  be a stochastic process on a filtered probability space  $(\Omega, \mathcal{F}, (\mathcal{F}_t), P)$  that models the discounted prices of primary traded assets in a financial market. An equivalent local martingale measure (ELMM) for S is a probability measure  $Q$  equivalent to the original (historical) measure  $P$  such that  $S$ is a local  $Q$ -martingale (see **Equivalent Martingale Measures**). If  $S$  is a nonnegative  $P$ -semimartingale, the fundamental theorem of asset pricing says that an ELMM  $Q$  for  $S$  exists if and only if  $S$  satisfies the no-arbitrage condition (NFLVR), that is, admits no free lunch with vanishing risk (see **Fundamental** Theorem of Asset Pricing). By Girsanov's theorem,  $S$  is then under  $P$  a semimartingale with a decomposition  $S = S_0 + M + A$  into a local *P*-martingale  $M$  and an adapted process  $A$  of finite variation. If S is special under  $P$ , then A can be chosen predictable and the resulting canonical decomposition of  $S$  is unique. We say that  $S$  satisfies the structure condition (SC) if  $M$  is locally  $P$ -square-integrable and A has the form  $A = \int d\langle M \rangle \lambda$  for a predictable process  $\lambda$  such that the increasing process  $\int \lambda' d\langle M \rangle \lambda$ is finite-valued. In an Itô process model where S is given by a stochastic differential equation  $dS_t =$  $S_t((\mu_t - r_t) dt + \sigma_t dW_t)$ , the latter process is given by  $\int \left( (\mu_t - r_t) / \sigma_t \right)^2 dt$ , the integrated squared instantaneous Sharpe ratio of  $S$  (see **Sharpe Ratio**).

Definition 1 Suppose S satisfies (SC). An ELMM  $\widehat{P}$  for S with P-square-integrable density  $d\widehat{P}/dP$  is called minimal martingale measure  $(MMM)$  (for S) if  $\widehat{P} = P$  on  $\mathcal{F}_0$  and if every local P-martingale L that is locally P-square integrable and strongly Porthogonal to M is also a local  $\widehat{P}$ -martingale. We call  $\widehat{P}$  orthogonality preserving if L is also strongly  $\widehat{P}$ -orthogonal to S.

The basic idea for the MMM first appeared in [46] in a more specific model, where it was used as an auxiliary technical tool in the context of local risk-minimization (see also Hedging for an overview of key ideas on hedging and Mean-Variance Hedging for an alternative quadratic approach). More precisely, the so-called

locally risk-minimizing strategy for a given contingent claim  $H$  was obtained there (under some specific assumptions) as the integrand from the classical Galtchouk-Kunita-Watanabe decomposition of H under  $\widehat{P}$ . However, the introduction of  $\widehat{P}$  in [46] and also in [47] was still somewhat *ad hoc*. The above definition was given in [18] where the main results presented here can also be found. In particular,  $[18]$  showed that for continuous S, the  $Galtchouk-Kunita-Watanabe$  decomposition of  $H$ under the MMM  $\widehat{P}$  provides (under very mild integrability conditions) the so-called Föllmer-Schweizer decomposition of  $H$  under the original measure  $P$ , and this in turn immediately gives the locally riskminimizing strategy for  $H$ . We emphasize that this is no longer true, in general, if  $S$  has jumps. The MMM subsequently found various other applications and uses and has become fairly popular, especially in models with continuous price processes.

Suppose now  $S$  satisfies (SC). For every ELMM Q for S with  $dQ/dP \in L^2(P)$ , the density process then takes the form

$$Z^{\mathcal{Q}} := \frac{\mathrm{d}\mathcal{Q}}{\mathrm{d}P}\bigg|_{\mathit{I\!F}} = Z_0^{\mathcal{Q}} \mathcal{E}\bigg(-\int \lambda \,\mathrm{d}M + L^{\mathcal{Q}}\bigg) \qquad (1)$$

with some locally  $P$ -square-integrable local  $P$ martingale  $L^Q$ . If the MMM  $\widehat{P}$  exists, then it has  $\widehat{Z}_0 = 1$  and  $L^{\widehat{P}} \equiv 0$ , and its density process is thus given by the stochastic exponential (see Stochastic **Exponential**)

$$\widehat{Z} = \mathcal{E}\left(-\int \lambda \, \mathrm{d}M\right)$$
$$= \exp\left(-\int \lambda \, \mathrm{d}M - \frac{1}{2} \int \lambda' \, \mathrm{d}[M] \,\lambda\right)$$
$$\times \prod (1 - \lambda' \Delta M) \exp\left(\lambda' \Delta M + \frac{1}{2} (\lambda' \Delta M)^2\right) \tag{2}$$

The advantage of this explicit representation is that it allows to determine the MMM  $\widehat{P}$  and its density process  $\widehat{Z}$  directly from the ingredients *M* and  $\lambda$  of the canonical decomposition of  $S$ . Conversely, one can start with the above expression for  $\widehat{Z}$  to define a candidate for the density process of the MMM. This gives existence of the MMM under the following conditions:

- 1.  $\widehat{Z}$  is strictly positive; this happens if and only if  $\lambda' \Delta M < 1$ , that is, all the jumps of  $\int \lambda \, dM$  are strictly below 1.
- The local *P*-martingale  $\widehat{Z}$  is a true *P*-martingale. 2.
- 3.  $\overline{Z}$  is *P*-square-integrable.

Condition 1 automatically holds (on any finite time interval) if S, hence also  $M$ , is continuous; it typically fails in models where  $S$  has jumps. Conditions 2 and 3 can fail even if 1 holds and even if there exists some ELMM for  $S$  with  $P$ -square-integrable density; see [45] or [15] for a counterexample.

The above explicit formula for  $\widehat{Z}$  shows that  $\widehat{P}$  is minimal in the sense that its density process contains the smallest number of symbols among all ELMMs  $Q$ . More seriously, the original idea was that  $\widehat{P}$  should turn S into a (local) martingale while having a minimal impact on the overall martingale structure of our setting. This is captured and made precise by the definition. If  $S$  is continuous, one can show that  $\widehat{P}$  is even orthogonality preserving; see [18] for this, and note that this usually fails if  $S$  has iumps.

To some extent, the naming of the "minimal" martingale measure is misleading since  $\widehat{P}$  was not originally defined as the minimizer of a particular functional on ELMMs. However, if  $S$  is continuous, Föllmer and Schweizer [18] have proved that  $\hat{P}$ minimizes

$$Q \mapsto H(Q|P) - E_Q \left[ \int_0^\infty \lambda'_u \, \mathrm{d}\langle M \rangle_u \lambda u \right] \qquad (3)$$

over all ELMMs  $Q$  for  $S$ ; see also [49]. Moreover, Schweizer [50] has shown that if  $S$  is continuous, then  $\widehat{P}$  minimizes the reverse relative entropy  $H(P|Q)$  over all ELMMs Q for S; this no longer holds if  $S$  has jumps. Under more restrictive assumptions, other minimality properties for  $\widehat{P}$  have been obtained by several authors. However, a general result under the sole assumption (SC) is not available so far.

There is a large amount of literature related to the MMM. In fact, a Google Scholar search for "minimal martingale measure" (enclosed in quotation marks) produced in April 2008 a list of well over 400 hits. As a first category, this contains papers where the MMM is studied *per se* or used as in the original approach of local risk-minimization. In terms of topics, the following areas of related work can be found in that category:

- Properties, characterization results, and general-. izations for the MMM:  $[1, 4, 9-11, 14, 19, 33,$ 36, 37, 49, 51];
- Convergence results for option prices (computed under the MMM): [25, 32, 42, 44];
- Applications to hedging: [7, 39, 47, 48] (see also Hedging).
- Uses for option pricing:  $[8, 13, 55]$ , to name only a very a few; comparison results for option prices are given in [22, 24, 34] (see also Riskneutral Pricing).
- Problems and counterexamples: [15, 16, 43, 45, 521.
- Equilibrium justifications for using the MMM: [26, 40].

A second category of papers contains those where the MMM has (sometimes unexpectedly) come up in connection with various other problems and topics in mathematical finance. Examples include the following:

- Classical utility maximization and utility indifference valuation [3, 20, 21, 23, 35, 41, 53, 54]: the MMM here often appears because the special structure of a given model implies that  $\widehat{P}$  has a particular optimality property (see also **Expected Utility Maximiza**tion; Expected Utility Maximization: Duality Methods; Utility Indifference Valuation; and Minimal Entropy Martingale Measure).
- The numeraire portfolio and growth-optimal investment  $[2, 12]$ : this is related to the minimization of the reverse relative entropy  $H(P|\cdot)$ over ELMMs (see also **Kelly Problem**).
- The concept of value preservation  $[28-30]$ : here the link seems to come up because value preservation is, like local risk-minimization, a local optimality criterion.
- Good deal bounds in incomplete markets [5, 6]: the MMM naturally shows up here because good deal bounds are formulated via instantaneous quadratic restrictions on the pricing kernel (ELMM) to be chosen (see also Good-deal Bounds; Sharpe Ratio; Market Price of Risk).
- Local utility maximization [27]; again, the link here is due to the local nature of the criterion that is used.
- Risk-sensitive control [17, 31, 38]; this is an . area where the connection to the MMM seems

not yet well understood. See also **Risk-sensitive Asset Management**.

## **References**

- [1] Arai, T. (2001). The relations between minimal martingale measure and minimal entropy martingale measure, *Asia-Pacific Financial Markets* **8**, 137–177.
- [2] Becherer, D. (2001). The numeraire portfolio for unbounded semimartingales, *Finance and Stochastics* **5**, 327–341.
- [3] Berrier, F., Rogers, L.C.G. & Tehranchi, M. (2008). *A Characterization of Forward Utility Functions*, *preprint*, http://www.statslab.cam.ac.uk/∼mike/forward -utilities.pdf.
- [4] Biagini, F. & Pratelli, M. (1999). Local risk minimization and numeraire, *Journal of Applied Probability* **36**, 1126–1139.
- [5] Bjork, T. & Slinko, I. (2006). Towards a general ¨ theory of good-deal bounds, *The Review of Finance* **10**, 221–260.
- [6] Cern ˇ y, A. (2003). Generalised Sharpe ratios and asset ´ pricing in incomplete markets, *European Finance Review* **7**, 191–233.
- [7] Cern ˇ y, A. & Kallsen, J. (2007). On the structure of ´ general mean-variance hedging strategies, *The Annals of Probability* **35**, 1479–1531.
- [8] Chan, T. (1999). Pricing contingent claims on stocks driven by Levy processes, ´ *The Annals of Applied Probability* **9**, 504–528.
- [9] Choulli, T. & Stricker, C. (2005). Minimal entropy-Hellinger martingale measure in incomplete markets, *Mathematical Finance* **15**, 465–490.
- [10] Choulli, T. & Stricker, C. (2006). More on minimal entropy-Hellinger martingale measure, *Mathematical Finance* **16**, 1–19.
- [11] Choulli, T., Stricker, C. & Li, J. (2007). Minimal Hellinger martingale measures of order *q*, *Finance and Stochastics* **11**, 399–427.
- [12] Christensen, M.M. & Larsen, K. (2007). No arbitrage and the growth optimal portfolio, *Stochastic Analysis and Applications* **25**, 255–280.
- [13] Colwell, D.B. & Elliott, R.J. (1993). Discontinuous asset prices and non-attainable contingent claims, *Mathematical Finance* **3**, 295–308.
- [14] Delbaen, F., Grandits, P., Rheinlander, T., Samperi, D., ¨ Schweizer, M. & Stricker, C. (2002). Exponential hedging and entropic penalties, *Mathematical Finance* **12**, 99–123.
- [15] Delbaen, F. & Schachermayer, W. (1998). A simple counterexample to several problems in the theory of asset pricing, *Mathematical Finance* **8**, 1–11.
- [16] Elliott, R.J. & Madan, D.B. (1998). A discrete time equivalent martingale measure, *Mathematical Finance* **8**, 127–152.

- [17] Fleming, W.H. & Sheu, S.J. (2002). Risk-sensitive control and an optimal investment model II, *The Annals of Applied Probability* **12**, 730–767.
- [18] Follmer, H. & Schweizer, M. (1991). Hedging of con- ¨ tingent claims under incomplete information, in *Applied Stochastic Analysis*, *Stochastics Monographs*, M.H.A. Davis & R.J. Elliott eds, Gordon and Breach, London, Vol. 5, pp. 389–414.
- [19] Grandits, P. (2000). On martingale measures for stochastic processes with independent increments, *Theory of Probability and its Applications* **44**, 39–50.
- [20] Grasselli, M. (2007). Indifference pricing and hedging for volatility derivatives, *Applied Mathematical Finance* **14**, 303–317.
- [21] Henderson, V. (2002). Valuation of claims on nontraded assets using utility maximization, *Mathematical Finance* **12**, 351–373.
- [22] Henderson, V. (2005). Analytical comparisons of option prices in stochastic volatility models, *Mathematical Finance* **15**, 49–59.
- [23] Henderson, V. & Hobson, D.G. (2002). Real options with constant relative risk aversion, *Journal of Economic Dynamics and Control* **27**, 329–355.
- [24] Henderson, V. & Hobson, D.G. (2003). Coupling and option price comparisons in a jump-diffusion model, *Stochastics and Stochastics Reports* **75**, 79–101.
- [25] Hong, D. & Wee, I.S. (2003). Convergence of jumpdiffusion models to the Black-Scholes model, *Stochastic Analysis and Applications* **21**, 141–160.
- [26] Jouini, E. & Napp, C. (1999). *Continuous Time Equilibrium Pricing of Nonredundant Assets*, *Leonard N. Stern School Finance Department Working Paper 99-008* , New York University, http://w4.stern.nyu.edu/finance/ research.cfm?doc id=1216, http://www.stern.nyu.edu/ fin/workpapers/papers99/wpa99008.pdf.
- [27] Kallsen, J. (2002). Utility-based derivative pricing in incomplete markets, in *Mathematical Finance— Bachelier Congress 2000*, H. Geman, D. Madan, S.R. Pliska & T. Vorst, eds, Springer-Verlag, Berlin, Heidelberg, New York, pp. 313–338.
- [28] Korn, R. (1998). Value preserving portfolio strategies and the minimal martingale measure, *Mathematical Methods of Operations Research* **47**, 169–179.
- [29] Korn, R. (2000). Value preserving strategies and a general framework for local approaches to optimal portfolios, *Mathematical Finance* **10**, 227–241.
- [30] Korn, R. & Schal, M. (1999). On value preserving ¨ and growth optimal portfolios, *Mathematical Methods of Operations Research* **50**, 189–218.
- [31] Kuroda, K. & Nagai, H. (2002). Risk-sensitive portfolio optimization on infinite time horizon, *Stochastics and Stochastics Reports* **73**, 309–331.
- [32] Lesne, J.-P., Prigent, J.-L. & Scaillet, O. (2000). Convergence of discrete time option pricing models under stochastic interest rates, *Finance and Stochastics* **4**, 81–93.
- [33] Mania, M. & Tevzadze, R. (2003). A unified characterization of *q*-optimal and minimal entropy martingale
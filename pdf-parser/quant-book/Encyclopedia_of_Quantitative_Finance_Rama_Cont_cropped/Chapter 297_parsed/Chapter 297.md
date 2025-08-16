## **Mean–Variance Hedging**

In a nutshell, *mean-variance hedging (MVH)* is the problem of approximating, with minimal meansquared error, a given payoff by the final value of a self-financing trading strategy in a financial market. Mean-variance portfolio selection (MVPS), on the other hand, consists of finding a self-financing strategy whose final value has maximal mean and minimal variance.

More precisely, let  $S = (S_t)_{0 \le t \le T}$  be an  $(\mathbb{R}^d)$ valued) stochastic process on a filtered probability space  $(\Omega, \mathcal{F}, \mathit{I\!F}, P)$  and think of  $S_t$  as discounted time  $t$  prices of  $d$  underlying risky assets. Assume S is a semimartingale and denote by  $\Theta$  a class of  $(I\!R^d\text{-valued})$  predictable S-integrable processes  $\vartheta =$  $(\vartheta_t)_{0 \le t \le T}$  satisfying suitable technical conditions. Together with an initial capital  $x$ , each  $\vartheta$  describes, *via* its time *t* holdings  $\vartheta_t$  in *S*, a self-financing strategy whose *value* at time  $t$  is given by the stochastic integral (*see* **Stochastic Integrals**)

$$V_t(x,\vartheta) = x + \int_0^t \vartheta_u \, \mathrm{d}S_u =: x + G_t(\vartheta) \qquad (1)$$

Mean-variance portfolio selection, for some risk aversion parameter  $\gamma > 0$ , then amounts to

$$\begin{array}{ll}\text{maximize } E[V_T(x,\vartheta)] - \gamma \text{Var}[V_T(x,\vartheta)]\\ \text{over all } \vartheta \in \Theta \end{array} \tag{2}$$

and MVH, for a final time  $T$  payoff given by a square-integrable  $\mathcal{F}_T$ -measurable random variable  $H$ , amounts to (see **Hedging**)

minimize 
$$E[|V_T(x,\vartheta) - H|^2]$$
  
over all  $\vartheta \in \Theta$  (3)

By writing the objective of equation (2) as  $m(\vartheta)$  –  $\gamma E\left[|V_T(x,\vartheta)-m(\vartheta)|^2\right]$  and adding the constraint  $m(\vartheta) := E[V_T(x, \vartheta)] = m$ , we can solve problem  $(2)$  by first solving problem  $(3)$  for a constant payoff  $H \equiv m$  and then optimizing over m. So we first focus on mean-variance hedging.

**Remark 1** A Google Scholar search quickly reveals that the literature on "mean-variance hedging" and "mean-variance portfolio selection" is vast; it cannot be properly surveyed here. Hence we have chosen

references partly for historical interest, partly for novelty, and partly for other subjective reasons. Any omissions may be blamed on this and lack of space.

In mathematical terms, MVH as in equation  $(3)$  is simply the problem of finding the best approximation in  $L^2 = L^2(P)$  of H by an element of  $\mathcal{G} := G_T(\Theta)$ . Existence (for arbitrary  $H$ ) is thus tantamount to closedness of  $\mathcal{G}$  in  $L^2$ , which depends on the precise choice of  $\Theta$ ; results in that direction can be found in [15, 16, 18, 24, 44, 50]. Since the optimal approximand is given by the projection in  $L^2$  of  $H$  onto  $\mathcal{G}$ , MVH (without constraints on strategies) has the pleasant feature that its solution is linear as a function of  $H$ . The main challenge, however, is to find more explicit descriptions of the optimal strategy  $\tilde{\vartheta}^{H}$ , that is, the minimizer for problem (3). The key difficulty there stems from the fact that S is, in general, a  $P$ -semimartingale, but not a  $P$ martingale.

**Remark 2** If S is a  $P$ -martingale, MVH of  $H$  is solved by projecting the *P*-martingale  $V^H$  associated with  $H$  onto the stable subspace of all stochastic integrals of  $S$ , and the optimal strategy is the integrand in the Galtchouk-Kunita-Watanabe decomposition of  $V^H$  with respect to S under P. This is also the (first component of the) strategy which is *risk-minimizing* for  $H$  in the sense of [22]; see also [11]. However, in this mathematically classical case, MVH is of minor interest for finance since a martingale stock price process has zero excess return.

Historically, mean-variance portfolio selection is much older than mean-variance hedging. It is traditionally credited to Harry Markowitz (1952), although closely related work by Bruno de Finetti (1940) has been discovered recently; [2] provides an overview (see Markowitz, Harry; Modern Portfolio Theory). For the static one-period case where  $G_T(\vartheta) =$  $\vartheta^{\text{tr}}(S_T-S_0)$  and  $\vartheta$  is a nonrandom vector, [40, 41] contain a general formulation and [43] an explicit solution (see also Risk-Return Analysis). A multiperiod treatment, whether in discrete or in continuous time, is considerably more delicate; this was already noticed in  $[45]$  and is explained more carefully a bit later.

Mean-variance hedging in the general formulation (3) seems to have been introduced only around 1990. It first appeared in a specific framework in [49], which generalizes a particular example from [21], and was subsequently extended to very general settings; see [47, 55] for surveys of the literature up to around 2000. Most of these papers use martingale techniques, and an important quantity in that context is the variance-optimal martin*gale measure*  $\tilde{P}$ , obtained as the solution to the dual problem of minimizing over all (signed) local martingale measures Q for S the  $L^2(P)$ -norm of the density  $dO/dP$  (see **Equivalent Martingale** Measures). It turns out [53] that if one modifies problem  $(3)$  to

minimize 
$$E\left[|V_T(x,\vartheta) - H|^2\right]$$
  
over all  $x \in \mathbb{R}$  and  $\vartheta \in \Theta$  (4)

the optimal initial capital is given by  $\tilde{x} = E_{\tilde{p}}[H]$ , and  $\tilde{P}$  also plays a key role in finding the optimal strategy  $\tilde{\vartheta}^{H}$ . If S is continuous, then  $\tilde{P}$  is equivalent to  $P$  (see **Equivalence of Probability Measures**) so that its density process  $Z^{\tilde{P}}$  is strictly positive [19]. This can then be exploited to give a more explicit description of  $\tilde{\vartheta}^H$ , either *via* an elegant change of numeraire ([24], see also Change of Numeraire), or via a change of measure and a recursive formula  $[48]$ ; see also  $[1]$  for an overview of partial extensions to discontinuous settings. For general discontinuous  $S$ , [15] have shown that the optimal strategy can be found in the same way as the locally risk-minimizing strategy [55] provided one first makes a change from  $P$  to a new (their so-called opportunity-neutral) probability measure  $P^*$ .

One common feature of all the above results is that they require for a more explicit description of  $\tilde{\vartheta}^H$  the density process  $(Z^{\tilde{P}} \text{ or } Z^{P^*})$  of some measure, and that this process is very difficult to find in general. Things become much simpler under the (frequently made but restrictive) assumption that  $S$  has a deterministic mean-variance trade-off (also called *nonstochastic opportunity set*), because  $\tilde{P}$  then coincides with the minimal martingale measure  $\widehat{P}$  (see **Minimal Martingale Measure**), which can always be written down directly from the semimartingale decomposition of  $S$ ; see [52]. The process  $S$  typically has a deterministic mean-variance trade-off if it has independent returns or is a Lévy process (see Lévy **Processes**); this explains why MVH can be used so easily in such settings.

The original MVH problem  $(3)$  is a static problem in the sense that one tries at time  $0$  to find an optimal strategy for the entire interval  $[0, T]$ . For an intertemporally dynamic formulation, one would at any time  $t$ 

minimize 
$$E\left[|V_T(x,\vartheta) - H|^2\big|\mathcal{F}_t\right]$$
  
over all  $\vartheta \in \Theta_t(\psi)$  (5)

where  $\Theta_t(\psi)$  denotes all strategies  $\vartheta \in \Theta$  that agree up to time t with a given  $\psi \in \Theta$ . In view of equation (1), one recognizes in equation (5) a linear-quadratic stochastic control (LQSC) problem, and this point of view allows to exploit additional theory (see Stochastic Control) and to obtain, in some situations, more explicit results about the optimal strategy as well. The idea to tackle MVH via LQ control techniques and backward stochastic differential equations (BSDEs; see Backward Stochastic Differential Equations) seems to originate with M. Kohlmann and X. Y. Zhou. Together with various coauthors, they developed this approach through several papers in an Itô diffusion setting for S; references [29, 31, 37, 60, 61] provide an overview. A key contribution was made a little earlier in [36] in a discrete-time model by embedding the MVPS problem into a class of auxiliary LQSC problems. Extensions beyond the Brownian setting are given in [10, 38, 39] among others; approaches in discrete time can be found in  $[14, 25]$ or [51].

As already stated, MVH is very popular and has been used and studied in many examples and contexts. A few of these are mentioned below:

- stochastic volatility models ( $[5, 34]$ ; see also Stochastic Volatility Models);
- insurance and ALM applications [17, 20, 57];
- weather derivatives or electricity loads ( $[12,$ 46]; see also Weather Derivatives; Commodity Risk);
- uncertain horizon models [42];  $\bullet$
- insider trading [6, 13, 30];
- robustness and model uncertainty ([23, 58]; see . also Robust Portfolio Optimization);
- default risk and credit derivatives ([4, 8, 28]; see also Section 10, "Credit Derivatives", of this encyclopedia).

Perhaps the main difference between meanvariance hedging and mean-variance portfolio selection is that MVPS is not consistent over time, in the following sense. If, in analogy to equation (5), we consider for each  $t$  the problem to

$$\begin{aligned} \text{maximize } E[V_T(x,\vartheta)|\mathcal{F}_t] \\ &- \gamma \text{Var}[V_T(x,\vartheta)|\mathcal{F}_t] \text{ over } \vartheta \end{aligned} \tag{6}$$

this is no longer a standard stochastic control problem because of the variance term. In particular, the crucial dynamic programming property fails: if  $\vartheta^*$  solves problem (2) on  $[0, T]$  and we consider problem (6) where we optimize over all  $\vartheta \in \Theta_t(\vartheta^*)$ , that is, strategies  $\vartheta$  that agree with  $\vartheta^*$  up to time t, the solution of this conditional problem over  $[t, T]$ will differ from  $\vartheta^*$ , in general. This makes things surprisingly difficult and explains why MVPS in a general multiperiod setting has still not been solved in a satisfactorily explicit manner.

From the purely geometric structure of the problem, one can derive by elementary arguments the optimal final value

$$G_T(\vartheta^*) = \frac{1}{2\gamma} \bigg( \alpha - \frac{\mathrm{d}\tilde{P}}{\mathrm{d}P} \bigg) \tag{7}$$

with  $\alpha = E \left[ \left( d\tilde{P} / dP \right)^2 \right]$ ; this can be seen from [53, 54] or also found in [59]. However, (7) mainly shows that finding the optimal strategy  $\vartheta^*$  is inextricably linked to a precise knowledge of the variance-optimal martingale measure  $\tilde{P}$ , which is very difficult to obtain in general. For the case of a *deterministic mean-variance trade-off* (nonstochastic opportunity *set*), we have already seen that  $\tilde{P}$  equals the minimal martingale measure  $\widehat{P}$  so that equation (7) readily gives the solution to the MVPS problem (2) in explicit form. This includes for instance the results obtained by Li and Ng [36] in finite discrete time or by Zhou and Li [61] who used BSDE techniques in continuous time. Other work in various settings includes [7, 35, 56].

One major area of recent developments in MVPS is the inclusion of constraints (for instance, [9, 26, 27, 32, 33]). Another challenging open problem is to find a time-consistent formulation  $(3]$  provides a first attempt).

## References

 $[1]$ Arai, T. (2005). Some remarks on mean-variance hedging for discontinuous asset price processes, International *Journal of Theoretical and Applied Finance* **8**, 425–443.

- Barone, L. (2008). Bruno de Finetti and the case of the [2] critical line's last segment, Insurance: Mathematics and Economics 42, 359-377.
- Basak, S. & Chabakauri, G. (2008). Dynamic mean-[3] variance asset allocation, London Business School, available at SSRN: http://ssrn.com/abstract=965926. forthcoming in Review of Financial Studies.
- Biagini, F. & Cretarola, A. (2007). Quadratic hedging [4] methods for defaultable claims, Applied Mathematics and Optimization 56, 425-443.
- Biagini, F., Guasoni, P. & Pratelli, M. (2000). Mean-[5] variance hedging for stochastic volatility models, Mathematical Finance  $10, 109-123$ .
- Biagini, F. & Oksendal, B. (2006). Minimal variance [6] hedging for insider trading, International Journal of Theoretical and Applied Finance 9, 1351–1375.
- [7] Bick, A. (2004). The mathematics of the portfolio frontier: a geometry-based approach, Quarterly Review of Economics and Finance 44, 337-361.
- Bielecki, T.R., Jeanblanc, M. & Rutkowski, M. (2004). [8] Hedging of defaultable claims, in Paris-Princeton Lecture Notes on Mathematical Finance, Lecture Notes in Mathematics, Springer, Vol. 1847, pp. 1-132.
- [9] Bielecki, T.R., Jin, H., Pliska, S.R. & Zhou, X.Y. (2005). Continuous-time mean-variance portfolio selection with bankruptcy prohibition, *Mathematical Finance* 15. 213-244.
- [10] Bobrovnytska, O. & Schweizer, M. (2004). Meanvariance hedging and stochastic control: beyond the Brownian setting, IEEE Transactions on Automatic Control 49. 396-408.
- [11] Bouleau, N. & Lamberton, D. (1989). Residual risks and hedging strategies in Markovian markets, Stochastic Processes and their Applications 33, 131-150.
- [12] Brockett, P.L., Wang, M., Yang, C. & Zou, H. (2006). Portfolio effects and valuation of weather derivatives, Financial Review 41/1, 55-76.
- [13] Campi, L. (2005). Some results on quadratic hedging with insider trading, Stochastics 77, 327-348.
- [14] Černý, A. (2004). Dynamic programming and meanvariance hedging in discrete time, Applied Mathematical Finance 11, 1-25.
- [15] Černý, A. & Kallsen, J. (2007). On the structure of general mean-variance hedging strategies, Annals of Probability 35, 1479-1531.
- [16] Choulli, T., Krawczyk, L. & Stricker, C. (1998).  $\mathcal{E}$ -martingales and their applications in mathematical finance, Annals of Probability 26, 853-876.
- [17] Dahl, M. & Møller, T. (2006). Valuation and hedging of life insurance liabilities with systematic mortality risk, Insurance: Mathematics and Economics 39, 193-217.
- [18] Delbaen, F., Monat, P., Schachermayer, W., Schweizer, M. & Stricker, C. (1997). Weighted norm inequalities and hedging in incomplete markets, Finance and Stochastics 1, 181–227.
- [19] Delbaen, F. & Schachermayer, W. (1996). The varianceoptimal martingale measure for continuous processes,

*Bernoulli* **2**, 81–105. Amendments and corrections (1996). *Bernoulli* **2**, 379–380.

- [20] Delong, L. & Gerrard, R. (2007). Mean-variance portfolio selection for a non-life insurance company, *Mathematical Methods of Operations Research* **66**, 339–367.
- [21] Duffie, D. & Richardson, H.R. (1991). Mean-variance hedging in continuous time, *Annals of Applied Probability* **1**, 1–15.
- [22] Follmer, H. & Sondermann, D. (1986). Hedging of ¨ non-redundant contingent claims, in *Contributions to Mathematical Economics*, W. Hildenbrand & A. Mas-Colell, eds, North-Holland, pp. 205–223.
- [23] Goldfarb, D. & Iyengar, G. (2003). Robust portfolio selection problems, *Mathematics of Operations Research* **28**, 1–38.
- [24] Gourieroux, C., Laurent, J.P. & Pham, H. (1998). Mean- ´ variance hedging and numeraire, ´ *Mathematical Finance* **8**, 179–200.
- [25] Gugushvili, S. (2003). Dynamic programming and mean-variance hedging in discrete time, *Georgian Mathematical Journal* **10**, 237–246.
- [26] Hu, Y. & Zhou, X.Y. (2006). Constrained stochastic LQ control with random coefficients, and application to portfolio selection, *SIAM Journal on Control and Optimization* **44**, 444–466.
- [27] Jin, H. & Zhou, X.Y. (2007). Continuous-time Markowitz's problems in an incomplete market, with no-shorting portfolios, in *Stochastic Analysis and Applications. Proceedings of the Second Abel Symposium, Oslo, 2005*, F.E. Benth, G. Di Nunno, T. Lindstrøm, B. O*/* ksendal & T. Zhang eds, Springer, pp. 125–151.
- [28] Kohlmann, M. (2007). The mean-variance hedging of a defaultable option with partial information, *Stochastic Analysis and Applications* **25**, 869–893.
- [29] Kohlmann, M. & Tang, S. (2002). Global adapted solution of one-dimensional backward stochastic Riccati equations, with application to the mean-variance hedging, *Stochastic Processes and their Applications* **97**, 255–288.
- [30] Kohlmann, M., Xiong, D. & Ye, Z. (2007). Change of filtrations and mean-variance hedging, *Stochastics* **79**, 539–562.
- [31] Kohlmann, M. & Zhou, X.Y. (2000). Relationship between backward stochastic differential equations and stochastic controls: a linear-quadratic approach, *SIAM Journal on Control and Optimization* **38**, 1392–1407.
- [32] Korn, R. & Trautmann, S. (1995). Continuous-time portfolio optimization under terminal wealth constraints, *Mathematical Methods of Operations Research* **42**, 69–92.
- [33] Labbe, C. & Heunis, A.J. (2007). Convex duality ´ in constrained mean-variance portfolio optimization, *Advances in Applied Probability* **39**, 77–104.
- [34] Laurent, J.P. & Pham, H. (1999). Dynamic programming and mean-variance hedging, *Finance and Stochastics* **3**, 83–110.

- [35] Leippold, M., Trojani, F. & Vanini, P. (2004). A geometric approach to multiperiod mean variance optimization of assets and liabilities, *Journal of Economic Dynamics and Control* **28**, 1079–1113.
- [36] Li, D. & Ng, W.-L. (2000). Optimal dynamic portfolio selection: Multi-period mean-variance formulation, *Mathematical Finance* **10**, 387–406.
- [37] Lim, A.E.B. (2004). Quadratic hedging and meanvariance portfolio selection with random parameters in an incomplete market, *Mathematics of Operations Research* **29**, 132–161.
- [38] Lim, A.E.B. (2006). Mean-variance hedging when there are jumps, *SIAM Journal on Control and Optimization* **44**, 1893–1922.
- [39] Mania, M. & Tevzadze, R. (2003). Backward stochastic PDE and imperfect hedging, *International Journal of Theoretical and Applied Finance* **6**, 663–692.
- [40] Markowitz, H.M. (1952). Portfolio selection, *Journal of Finance* **7**, 77–91.
- [41] Markowitz, H.M., Lacey, R., Plymen, J., Dempster, M.A.H. & Tompkins, R.G. (1994). The general meanvariance portfolio selection problem [and discussion], *Philosophical Transactions: Physical Sciences and Engineering, Mathematical Models in Finance* **347**(1684), 543–549.
- [42] Martellini, L. & Urosevi ˆ c, B. (2006). Static mean- ´ variance analysis with uncertain time horizon, *Management Science* **52**, 955–964.
- [43] Merton, R.C. (1972). An analytic derivation of the efficient portfolio frontier, *Journal of Financial and Quantitative Analysis* **7**, 1851–1872.
- [44] Monat, P. & Stricker, C. (1995). Follmer-Schweizer ¨ decomposition and mean-variance hedging of general claims, *Annals of Probability* **23**, 605–628.
- [45] Mossin, J. (1968). Optimal multiperiod portfolio policies, *Journal of Business* **41**, 215.
- [46] Nas¨ akk ¨ al¨ a, E. & Keppo, J. (2005). Electricity load pat- ¨ tern hedging with static forward strategies, *Managerial Finance* **31/6**, 116–137.
- [47] Pham, H. (2000). On quadratic hedging in continuous time, *Mathematical Methods of Operations Research* **51**, 315–339.
- [48] Rheinlander, T. & Schweizer, M. (1997). On L ¨ 2 projections on a space of stochastic integrals, *Annals of Probability* **25**, 1810–1831.
- [49] Schweizer, M. (1992). Mean-variance hedging for general claims, *Annals of Applied Probability* **2**, 171–179.
- [50] Schweizer, M. (1994). Approximating random variables by stochastic integrals, *Annals of Probability* **22**, 1536–1575.
- [51] Schweizer, M. (1995). Variance-optimal hedging in discrete time, *Mathematics of Operations Research* **20**, 1–32.
- [52] Schweizer, M. (1995). On the minimal martingale measure and the Follmer-Schweizer decomposition, ¨ *Stochastic Analysis and Applications* **13**, 573–599.

- [53] Schweizer, M. (1996). Approximation pricing and the variance-optimal martingale measure, *Annals of Probability* **24**, 206–236.
- [54] Schweizer, M. (2001). From actuarial to financial valuation principles, *Insurance: Mathematics and Economics* **28**, 31–47.
- [55] Schweizer, M. (2001). A guided tour through quadratic hedging approaches, in *Option Pricing, Interest Rates and Risk Management*, E. Jouini, J. Cvitanic & M. ´ Musiela, eds, Cambridge University Press, pp. 538–574.
- [56] Steinbach, M.C. (2001). Markowitz revisited: meanvariance models in financial portfolio analysis, *SIAM Review* **43**, 31–85.
- [57] Thomson, R.J. (2005). The pricing of liabilities in an incomplete market using dynamic mean-variance hedging, *Insurance: Mathematics and Economics* **36**, 441–455.
- [58] Toronjadze, T. (2001). Optimal mean-variance robust hedging under asset price model misspecification, *Georgian Mathematical Journal* **8**, 189–199.

- [59] Xia, J. & Yan, J.A. (2006). Markowitz's portfolio optimization in an incomplete market, *Mathematical Finance* **16**, 203–216.
- [60] Zhou, X.Y. (2003). Markowitz's world in continuous time, and beyond, in *Stochastic Modeling and Optimization: With Applications in Queues, Finance, and Supply Chains*, D.D. Yao, H. Zhang & D.Y. Zhou, eds, Springer, pp. 279–309.
- [61] Zhou, X.Y. & Li, D. (2000). Continuous-time meanvariance portfolio selection: a stochastic LQ framework, *Applied Mathematics and Optimization* **42**, 19–33.

## **Related Articles**

**Expected Utility Maximization**; **Hedging**; **Minimal Martingale Measure**; **Risk–Return Analysis**; **Stochastic Integrals**.

MARTIN SCHWEIZER
# Hedging

In a complete market (see **Complete Markets**) derivative securities are redundant in the sense that they can be replicated by the gains from trading via a self-financing admissible strategy in the underlying asset. This replicating strategy is then called the *hedging strategy* for the claim.

More formally, we fix some filtered probability space  $(\Omega, \mathcal{A}, (\mathcal{F}_t), P)$ . The (discounted) price process of a risky asset is modeled by an  $(\mathcal{F}_t)$ -adapted semimartingale S. A claim B is an  $\mathcal{F}_T$ -measurable random variable, where  $T$  is the maturity of the claim.  $B$  is *attainable* if there exists a constant  $c$  and an admissible strategy  $\vartheta$  such that

$$B = c + \int_0^T \vartheta_t \, \mathrm{d}S_t \tag{1}$$

The quintuple  $(\Omega, \mathcal{A}, (\mathcal{F}_t), P, S)$  models a financial market. A market is *complete* if all bounded claims are attainable. Finally, a market that is not complete is called *incomplete*.

In case there exists an equivalent martingale measure (see Equivalent Martingale Measures) Q for  $S$  in a complete market, it must be unique according to some version of the second fundamental theorem of asset pricing (see Second Fundamental Theorem of Asset Pricing). Moreover, S has the predictable representation property (PRP) (see **Martingale Representation Theorem**) with respect to (w.r.t.)  $(Q, (\mathcal{F}_t))$ , meaning that every  $(Q, (\mathcal{F}_t))$ martingale can be written as a sum of its initial value and a stochastic integral w.r.t. S. These facts can be used to show existence of an optimal hedging strategy as follows: we consider for each bounded claim  $B$  the associated  $Q$ -martingale  $V$  given by

$$V_t = E_O \left[ B \, | \, \mathcal{F}_t \right], \qquad t \le T \tag{2}$$

By the PRP, there exists an admissible strategy  $\vartheta$ such that

$$V_t = V_0 + \int_0^t \vartheta_u \, \mathrm{d}S_u, \qquad t \le T \tag{3}$$

In particular, for  $t = T$ , we get

$$B = E_{\mathcal{Q}}[B] + \int_{0}^{T} \vartheta_{t} \, \mathrm{d}S_{t} \tag{4}$$

To calculate  $\vartheta$ , note that we can express  $\vartheta$  as the (symbolic) differential of angle bracket processes  $(w.r.t. Q),$ 

$$\vartheta_t = \frac{\mathrm{d}\left\langle V, S \right\rangle_t}{\mathrm{d}\left\langle S \right\rangle_t} \tag{5}$$

which then in turn can often be evaluated by assuming more specific structures for the price process  $S$ and the claim  $B$ .

### **Ouadratic Risk Minimization**

In incomplete markets, one can in general not hedge a claim perfectly, and hence, there will always be some remaining risk which can be minimized according to various criteria. The Föllmer-Sondermann (FS) [5] approach consists in an orthogonal projection in  $L^2(Q)$  of a square-integrable claim B onto the subspace spanned by the constants and stochastic integrals w.r.t. the price process  $S$  (which we assume to be locally square-integrable). Here,  $Q$  is some martingale measure for  $S$  that has been obtained either *via* calibration or according to some optimality criterion.

More precisely, given a claim  $B \in L^2(Q, \mathcal{F}_T)$ , we want to minimize

$$E_{Q}\left[\left(B-c-\int_{0}^{T}\vartheta_{t}\,\mathrm{d}S_{t}\right)^{2}\right] \qquad \qquad (6)$$

over all constants c and all  $\vartheta \in L^2(S)$ , that is, predictable processes  $\vartheta$ , such that  $E_Q \left[ \int_0^T \vartheta_t^2 \, \mathrm{d} \left[ S \right]_T \right]$  $< \infty$ . Hence, the goal is to project B onto the linear space

$$K = \left\{ c + \int_0^T \vartheta_t \, \mathrm{d}S_t : \ c \in \mathbb{R}, \vartheta \in L^2(S) \right\} \subset L^2(Q) \tag{7}$$

For  $\vartheta$  as above we also denote

$$K_0 = \left\{ \int_0^T \vartheta_t \, \mathrm{d}S_t : \vartheta \in L^2(S) \right\} \subset L^2(Q) \qquad (8)$$

By its very construction, the stochastic integral yields an isometry (here, we understand  $[S]$  as the measure on  $[0, T]$  which is associated with the increasing process  $[S]$ 

$$K_0 \cong L^2 \left( \Omega \times [0, T], Q \otimes [S] \right) \tag{9}$$

$$\int_0^T \vartheta_t \, \mathrm{d}S_t \longleftrightarrow \vartheta \tag{10}$$

since we have

$$E_{\mathcal{Q}}\left[\left(\int_{0}^{T} \vartheta_{t} \, \mathrm{d}S_{t}\right)^{2}\right] = E_{\mathcal{Q}}\left[\int_{0}^{T} \vartheta_{t}^{2} \, \mathrm{d}\left[S\right]_{T}\right] \tag{11}$$

Hence,  $K_0$  is isometrically isomorphic to an  $L^2$ space and therefore closed. Therefore, we can apply the theorem about the orthogonal projection in the Hilbert spaces to get a decomposition

$$B = c^B + \int_0^T \vartheta_t^B \, \mathrm{d}S_t + L_T \tag{12}$$

where  $L_T$  is orthogonal to each element of  $K$ ; in particular,  $E_0[L_T] = 0$  since  $1 \in K$ . It follows that we have  $c^{\widetilde{B}} = E_O[B]$ , and  $\vartheta^B$  is called the FS optimal hedging strategy. As processes,  $L_t :=$  $E[L_T|\mathcal{F}_t]$  and S are strongly orthogonal in the sense that LS is a Q-martingale or equivalently,  $\langle L, S \rangle =$ 0, where the predictable covariation  $\langle ., . \rangle$  here, refers to the measure  $Q$ . This implies

$$\int \vartheta^B \, \mathrm{d}\langle V, \, S \rangle = \langle S, \, S \rangle \tag{13}$$

where  $V_t := E_O[B|\mathcal{F}_t]$  denotes the martingale generated by  $B$ . Moreover, a simple calculation yields

$$E_{\mathcal{Q}}[L_T^2] = E_{\mathcal{Q}} \bigg[ \langle V, V \rangle_T - \int_0^T (\vartheta_t^B)^2 \langle S, S \rangle_t \bigg] \tag{14}$$

Equation  $(13)$  is sometimes written as

$$\vartheta^{B} = \frac{\mathrm{d}\langle V,\,S\rangle}{\mathrm{d}\langle S,\,S\rangle} \tag{15}$$

We call

$$V = c^B + \int \vartheta^B \, \mathrm{d}S + L \tag{16}$$

the Galtchouk-Kunita-Watanabe (GKW) decomposition of  $B$  or rather  $V$  relative to  $S$ .

In some models, one can compute the optimal (risk-minimizing) hedging strategy by solving a partial integro-differential equation [1] or by a generalized Clark-Ocone formula from Malliavin calculus [2].

#### **Utility-indifference Hedging**

Let  $u$  be some utility function defined on the whole real line. If there exists a number  $\pi$  satisfying

$$\sup_{\vartheta} E\left[u\left(x + \int_{0}^{T} \vartheta_{t} \, \mathrm{d}S_{t}\right)\right]$$
$$= \sup_{\vartheta} E\left[u\left(x + \int_{0}^{T} \vartheta_{t} \, \mathrm{d}S_{t} + \pi - B\right)\right] (17)$$

then it is called *utility-indifference price* of the claim  $B$ . It is the threshold where the investor is indifferent whether just to maximize expected utility from a pure investment into the stock with the price process  $S$  or to sell in addition a claim  $B$  and collect a premium  $\pi$  for this.

The optimal strategies  $\vartheta$  on both sides of equation  $(17)$  typically differ. The difference

$$\theta := \phi^B - \phi^0 \tag{18}$$

of the optimizers on the right- and the left-hand side respectively can be interpreted as a *utility-based* hedging strategy. It corresponds to the adjustment of the investor's portfolio made in order to account for the option.

Let us consider exponential utility

$$u(x) = 1 - \exp(-\alpha x) \tag{19}$$

where  $\alpha > 0$ . If  $\theta^{\alpha}$  denotes the exponential utilitybased hedging strategy corresponding to selling  $\alpha$ units of the claim  $B$ , then it turns out that under quite general conditions the associated normalized gains  $\frac{1}{\alpha} \int_0^T \theta_t^{\alpha} dS_t$  converge in  $L^2(Q^0)$ ,  $Q^0$  being the minimal entropy martingale measure, to  $\int_0^T \vartheta_t^B dS_t$ .<br>Here,  $\vartheta^B$  is the integrand coming from the GKW decomposition (12) w.r.t.  $Q^0$ ; see [6] and the references contained therein.

#### **Further Approaches to Hedging**

Ideally, one would like to find a hedging strategy that always allows one to superreplicate the claim  $B.$  Finding such a strategy is related to the optional decomposition theorem for supermartingales which are bounded from below. However, it turns out that pursuing such a *superhedging strategy* is too expensive in the sense that the corresponding price typically equals the highest price consistent with noarbitrage pricing, that is, it amounts to sup*<sup>Q</sup> EQ* [*B*], where the supremum is taken over all the equivalent martingale measures *Q*.

Therefore, it has been proposed by Follmer and ¨ Leukert [3] to maximize the probability of a successful hedge given a certain amount of initial capital, a concept that they call *quantile hedging*. However, with this approach there is no protection for the worst case scenarios other than portfolio diversification, and technically, it might be difficult to implement this since it corresponds to hedging a knock-out option. The same authors [4], moreover, considered *efficient hedges* which minimize the expected shortfall weighted by some loss function. In this way, the investor may interpolate between the extremes of no hedge and a superhedge, depending on the accepted level of shortfall risk.

## **References**

[1] Cont R., Tankov P. & Voltchkova E. (2007). Hedging with options in presence of jumps, in *Stochastic Analysis and Applications: The Abel Symposium 2005 in honor of Kiyosi Ito*, F.E. Benth, G. Di Nunno, T. Lindstrom, B. ksendal & T. Zhang, eds, Springer, pp. 197–218.

- [2] Di Nunno, G. (2002). Stochastic integral representation, stochastic derivatives and minimal variance hedging, *Stochastics and Stochastics Reports* **73**, 181–198.
- [3] Follmer, H. & Leukert, P. (1999). Quantile hedging, ¨ *Finance and Stochastics* **3**, 251–273.
- [4] Follmer, H. & Leukert, P. (2000). Efficient hedging: cost ¨ versus shortfall risk, *Finance and Stochastics* **4**, 117–146.
- [5] Follmer, H. & Sondermann, D. (1986). Hedging of non- ¨ redundant contingent claims. Contributions to mathematical economics, in *Honor of G. Debreu*, W. Hildenbrand & A. Mas-Colell, eds, Elsevier Science Publications, North-Holland, pp. 205–223.
- [6] Kallsen, J. & Rheinlander, T. (2008). ¨ *Asymptotic Utilitybased Pricing and Hedging for Exponential Utility*. Preprint.

## **Related Articles**

**Complete Markets**; **Delta Hedging**; **Equivalent Martingale Measures**; **Mean–Variance Hedging**; **Option Pricing: General Principles**; **Second Fundamental Theorem of Asset Pricing**; **Stochastic Integrals**; **Superhedging**; **Uncertain Volatility Model**; **Utility Indifference Valuation**.

THORSTEN RHEINLANDER ¨
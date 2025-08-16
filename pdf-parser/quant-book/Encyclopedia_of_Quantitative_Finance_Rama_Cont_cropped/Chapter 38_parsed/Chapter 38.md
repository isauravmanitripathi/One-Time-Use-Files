# **Stochastic Integrals**

If  $H_t$  represents the number of shares of a certain asset held by an investor and  $X_t$  denotes the price of the asset, the gain on  $[0, t]$  from the trading strategy  $H$  is often represented as

$$\int_0^t H_t \, \mathrm{d}X_t \tag{1}$$

Here, our goal is to give a precise meaning to such "stochastic integrals", where  $H$  and  $X$  are stochastic processes verifying appropriate assumptions.

Looking at the time-series data for price evolution of, say, a stock, one realizes that placing smoothness assumptions, such as differentiability, on the paths of  $X$  would be unrealistic. Consequently, this puts us in a situation where the theory of ordinary integration is no longer sufficient for our purposes. In what follows, we construct the stochastic integral  $\int H \, dX$ for a class of integrands and integrators that are as large as possible while satisfying certain conditions. The stochastic processes that we use are defined on a complete probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ . We always assume that all the processes are jointly measurable, that is, for any process  $(Y_t)_{0 \le t < \infty}$  the map  $(t, \omega) \mapsto$  $Y_t(\omega)$  is measurable with respect to  $\mathcal{B}(\mathbb{R}_+) \times \mathcal{F}$ , where  $\mathcal{B}(\mathbb{R}_+)$  is the Borel σ-algebra on [0, ∞). In addition, we are given a *filtration*  $(\mathcal{F}_t)_{0 \le t \le \infty}$  (see Filtrations), which models the accumulation of our information over time. The filtration  $(\mathcal{F}_t)_{0 \le t \le \infty}$  is usually denoted by  $\mathbb{F}$  for convenience. We say that a jointly measurable process,  $Y$ , is *adapted* (or  $\mathbb{F}$ *adapted* if we need to specify the filtration) if  $Y_t \in \mathcal{F}_t$ for all  $t, 0 \le t < \infty$ . We assume that the following hypotheses hold true.

### Assumption 1 The filtered complete probability space $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$ satisfies the usual hypotheses (see **Filtrations**)

Although the above hypotheses are restrictive, they are satisfied in many situations. The natural filtration of a Lévy process, in particular a Brownian motion, satisfies the usual hypotheses once completed. The same is true for the natural filtration of any counting process or "reasonable" strong Markov process (see, e.g., [7] for a more detailed discussion of the usual hypotheses and their consequences).

Having fixed the stochastic base on which all the processes are defined, let us go back to our primary task of defining the integral  $\int H \, dX$ . If X is a process of finite variation, the theory is that of Lebesgue-Stieltjes integration.

**Definition 1** A stochastic process  $X$  is said to be càdlàg (for continu à droite, limites à gauche from French) if it a.s. has sample paths that are right con*tinuous on*  $[0, \infty)$  *with left limits on*  $(0, \infty)$ *. Similarly,* a stochastic process  $X$  is said to be càglàd (for continu à gauche, limites à droite) if it a.s. has sample paths that are left continuous on  $(0,\infty)$  with right limits on  $[0, \infty)$ . We denote the space of adapted, càdlàg (respectively, càglàd) processes by  $\mathbb{D}$  (respec*tively*,  $\mathbb{L}$ ).

**Definition 2** Let  $X$  be a càdlàg process. For a given  $\omega \in \Omega$ , the variation of the path  $X(\omega)$  on the compact interval  $[a, b]$  is defined as

$$\sup_{\pi \in P} \sum_{t_i \in \pi} \left| X_{t_{i+1}}(\omega) - X_{t_i}(\omega) \right| \tag{2}$$

where  $P$  is the set of all finite partitions of  $[a, b]$ .  $X$ is said to be a finite variation  $(FV)$  process if X is  $\dot{c}$ àdlàg and almost all paths of  $X$  have finite variation on each compact interval of  $[0, \infty)$ .

If X is an FV process, for fixed  $\omega$ , it induces a signed measure on  $\mathbb{R}_+$  and thus we can define a jointly measurable integral  $\int_0^t H_s(\omega) \, dX_s(\omega)$  for any bounded and jointly measurable  $H$ . In other words, the integral  $\int H \, dX$  can be defined path by path as a Lebesgue-Stieltjes integral, if  $H$  is a jointly measurable process such that  $\int_0^t H_s(\omega) \, dX_s(\omega)$  exists and is finite for all  $t > 0$ , a.s.

Unfortunately, the set of FV processes is not rich enough if one wants to give a rigorous meaning to  $\int H \, dX$  using only Stieltjes integration. When we replace  $X$  with, say, a Brownian motion, the theory of Stieltjes integration fails to work since the Brownian motion is known to have paths of infinite variation in every compact interval of  $\mathbb{R}_+$ . Therefore, one needs to develop a concept of integration with respect to a class of processes that is large enough to cover processes such as the Brownian motion or the more general Lévy processes, which find frequent applications in different fields.

To find the weakest conditions on  $X$  so that  $\int H \, dX$  is well defined, we start with the simplest possible form for the integrand  $H$  and work gradually to extend the stochastic integral to more complex integrands by imposing conditions on  $X$  but making sure that these conditions are as minimal as possible at the same time.

The simplest integrand one can think of is of the following form:

$$H_{t}(\omega) = \mathbf{1}_{(S(\omega), T(\omega)]}(t)$$
  
$$:= \begin{cases} 1 & \text{if } S(\omega) < t \leq T(\omega) \\ 0 & \text{otherwise} \end{cases}$$
(3)

where  $S$  and  $T$  are stopping times (see **Filtrations**) with respect to  $\mathbb{F}$ . In financial terms, this corresponds to a buy-and-hold strategy, whereby one unit of the asset is bought at, possibly random, time  $S$  and sold at time  $T$ . If  $X$  is the stochastic process representing the price of the asset, the net profit of such a trading strategy after time T is equal to  $X_T - X_S$ . This leads us to define  $\int H \, dX$  as

$$\int_0^t H_s \, \mathrm{d}X_s = X_{t \wedge T} - X_{t \wedge S} \tag{4}$$

where  $t \wedge T := \min\{t, T\}$  for all  $t, 0 \le t < \infty$ , and stopping times  $T$ . Clearly, the process  $H$  in equation  $(3)$  has paths that are left continuous and possess right limits. We could similarly have defined  $\int H \, dX$  for H of the form, say,  $\mathbf{1}_{[S,T)}$ . However, there is a good reason for insisting on paths that are continuous from the left on  $(0, \infty)$  as we see in Example 1. Let us denote  $\int_0^t H_s \, \mathrm{d}X_s$  by  $(H \cdot X)_t$ .

**Theorem 1** Let  $H$  be of the form (3) and  $M$  be a martingale (see **Martingales**). Then  $H \cdot M$  is a martingale.

Later, we will see that the above theorem holds for a more general class of integrands so that the stochastic integrals preserve the martingale property. The following example shows why the left continuity for  $H$  is a reasonable restriction from a financial perspective.

**Example 1** Let  $N$  be a Poisson process with intensity  $\lambda$  and define X by  $X_t = \lambda t - N_t$ . It is well known that  $X$  is a martingale. Suppose that there exists a traded asset with a price process given by  $X$ . Under normal circumstances, one should not be able to make arbitrage profits by trading in this

asset since its price does not change over time on average. Indeed, if H is of the form (3), then  $H \cdot X$ is a martingale with expected value zero so that the traders earn zero profit on average, as expected. Now consider another strategy  $H = \mathbf{1}_{[0,T_1)}$ , where  $T_1$  is the time of the first jump of N. Since X is an FV process,  $H \cdot X$  is well defined as a Stieltjes integral and is given by  $(H \cdot X)_t = \lambda(t \wedge T_1) > 0$ , a.s., being the value of the portfolio at time  $t$ . Thus, this trading strategy immediately accumulates arbitrage profits. A moment of reflection reveals that such a trading strategy is not feasible under usual circumstances since it requires the knowledge of the time of a market crash, time  $T_1$  in this case, before it happens. If we use  $H = \mathbf{1}_{[0,T_1]}$  instead, this problem disappears.

Naturally, one will want the stochastic integral to be linear. Given a linear integral operator, we can define  $H \cdot X$  for integrands that are linear combinations of processes of the form  $(3)$ .

**Definition 3** A process  $H$  is said to be simple predictable if  $H$  has a representation

$$H_{t} = H_{0}\mathbf{1}_{\{0\}}(t) + \sum_{i=1}^{n} H_{i}\mathbf{1}_{(T_{i},T_{i+1}]}(t) \qquad (5)$$

where  $0 = T_1 \leq \cdots \leq T_{n+1} < \infty$  is a finite sequence of stopping times,  $H_0 \in \mathcal{F}_0$ ,  $H_i \in \mathcal{F}_{T_i}$ ,  $1 \leq i \leq n$  with  $|H_i| < \infty$ , a.s.,  $0 \le i \le n$ . The collection of simple predictable processes is denoted by  $S$ .

Let  $\mathbf{L}^0$  be the space of finite-valued random variables endowed with the topology of convergence in probability. Define the linear mapping  $I_X : \mathbf{S} \mapsto$  $\mathbf{L}^0$  as

$$I_X(H) = (H \cdot X)_{\infty}$$
  
$$:= H_0 X_0 + \sum_{i=1}^n H_i (X_{T_{i+1}} - X_{T_i}) \qquad (6)$$

where  $H$  has the representation given in equation (5). Note that this definition does not depend on the particular choice of representation for  $H$ .

Another property that the operator  $I_X$  must have is that it should satisfy some version of the bounded convergence theorem. This will inevitably place some restrictions on the stochastic process  $X$ . Thus, to have a large enough class of integrators, we choose a reasonably weak version. A particularly weak version of the bounded convergence theorem is that the *uniform* convergence of  $H^n$  to H in S implies the convergence of  $I_X(H^n)$  to  $I_X(H)$  only in probability. Let  $S_u$  be the space S topologized by uniform convergence and recall that for a process  $X$  and a stopping time T, the notation  $X^T$  denotes the process  $(X_{t\wedge T})_{t>0}.$ 

**Definition 4** A process  $X$  is a total semimartingale if *X* is càdlàg, adapted and  $I_X : \mathbf{S}_u \mapsto \mathbf{L}^0$  is continuous.  $X$  is a semimartingale (see **Semimartingale**) if, for each  $t \in [0, \infty)$ ,  $X^t$  is a total semimartingale.

This continuity property of  $I_X$  allows us to extend the definition of stochastic integrals to a class of integrands that is larger than  $S$  when the integrator is a semimartingale.

It follows from the definition of a semimartingale that semimartingales form a vector space. One can also show that all square integrable martingales and all adapted FV processes are semimartingales (see Semimartingale). Therefore, the sum of a square integrable martingale and an adapted FV process would also be a semimartingale. The converse of this statement is also "essentially" true. The precise statement is the following theorem.

Theorem 2 (Bichteler–Dellacherie Theorem). Let  $X$  be a semimartingale. Then there exist processes M, A, with  $M_0 = A_0 = 0$  such that

$$X_t = X_0 + M_t + A_t \tag{7}$$

where  $M$  is a local martingale and  $A$  is an adapted FV process.

Here, we emphasize that this decomposition is not necessarily unique. Indeed, suppose that  $X$  has the decomposition  $X = X_0 + M + A$  and the space  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  supports a Poisson process N with intensity  $\lambda$ . Then  $Y_t = N_t - \lambda t$  will define a martingale, which is also an FV process. Therefore,  $X$  can also be written as  $X = X_0 + (M + Y) + (A - Y)$ . The reason for the nonuniqueness is the existence of martingales that are of finite variation. However, if X has a decomposition  $X = X_0 + M + A$ , where  $M$  is a local martingale and  $A$  is *predictable*<sup>a</sup> and FV with  $M_0 = A_0 = 0$ , then such a decomposition is unique since all predictable local martingales that are of finite variation have to be constant.

Arguably, Brownian motion is the most well known of all semimartingales. In the following section, we develop stochastic integration with respect to a Brownian motion.

# $L^2$ Theory of Stochastic Integration with **Respect to Brownian Motion**

We assume that there exists a Brownian motion,  $B$ , on  $(\Omega, \mathcal{F}, \mathbb{F}, \mathbb{P})$  with  $B_0 = 0$ , and that  $\mathcal{F}_0$  only contains the  $(\mathcal{F}, \mathbb{P})$ -null sets. First, we define the notion of predictability, which is the key concept in defining the stochastic integral.

**Definition 5** The predictable  $\sigma$ -algebra  $\mathcal{P}$  on  $[0,\infty)\times\Omega$  is defined to be the smallest  $\sigma$ -algebra on  $[0,\infty) \times \Omega$  with respect to which every adapted càglàd process is measurable. A process is said to be predictable if it is a  $P$ -measurable map from  $[0,\infty)\times\Omega$  to  $\mathbb{R}$ .

Clearly,  $S \subset \mathcal{P}$ . Actually, there is more to this as is shown by the next theorem.

**Theorem 3** Let  $bS$  be the set of elements of  $S$ that are bounded a.s. Then,  $\mathcal{P} = \sigma(\mathbf{bS})$ , that is,  $\mathcal{P}$  is  $generated by the processes in **bS**.$ 

By linearity of the stochastic integral and Theorem 1 and using the fact that Brownian motion has increments independent from the past with a certain Gaussian distribution, we have the following.

**Theorem 4** Let  $H \in \mathbf{bS}$  and define  $(H \cdot B)_t = (H \cdot B)_t$  $(B^t)_{\infty}$ , that is,  $(H \cdot B)_t$  is the stochastic integral of H with respect to  $B^t$ . Then  $H \cdot B$  is a martingale and

$$\mathbb{E}\left[ (H \cdot B)_t^2 \right] = \int_0^t \mathbb{E}[H_s^2] \, \mathrm{d}s \tag{8}$$

In the following, we construct the stochastic integral with respect to Brownian motion for a subset of predictable processes. To keep the exposition simple, we restrict our attention to a finite interval  $[0, T]$ , where  $T$  is arbitrary but deterministic. Define

$$\mathcal{L}^{2}(B^{T}) := \left\{ H \in \mathcal{P} : \int_{0}^{T} \mathbb{E}[H_{s}^{2}] \, \mathrm{d}s < \infty \right\} \quad (9)$$

which is a Hilbert space. Note that  $\mathbf{bS} \subset \mathcal{L}^2(B^T)$ . Letting  $L^2(\mathcal{F}_T)$  denote the space of square integrable  $\mathcal{F}_T$ -measurable random variables, Theorem 4 now implies the map

$$I_{B^T} : \mathbf{bS} \mapsto \mathcal{L}^2(\mathcal{F}_T) \tag{10}$$

defined by

$$I_{B^T}(H) = (H \cdot B)_T \tag{11}$$

is an isometry. Consequently, we can extend the definition of the stochastic integral uniquely to the closure of **bS** in  $\mathcal{L}^2(B^T)$ . An application of monotone class theorem along with Theorem 3 yields that the closure is the whole  $\mathcal{L}^2(B^T)$ .

**Theorem 5** Let  $H \in \mathcal{L}^2(B^T)$ . Then the Itô integral  $(H \cdot B)_T$  of H with respect to  $B^T$  is the image of H under the extension of the isometry  $I_{B^T}$  to the whole of  $\mathcal{L}^2(B^T)$ . In particular,

$$\mathbb{E}\left[ (H \cdot B)_T^2 \right] = \int_0^T \mathbb{E}[H_s^2] \, \mathrm{d}s \tag{12}$$

Moreover, the process Y defined by  $Y_t = (H \cdot B)_{t \wedge T}$ is a square integrable martingale.

The property (12) is often called the *Itô isometry*.

## **Stochastic Integration with Respect to General Semimartingales**

In the previous section, we developed the stochastic integration for Brownian motion over the interval  $[0, T]$ . We need to mention here that the method employed works not only for Brownian motion but also for any martingale  $M$  that is square integrable over  $[0, T]$ , the latter case requiring some extra effort mainly for establishing the existence of the so-called *quadratic variation* process associated with  $M$ . This would, in turn, allow us to extend the definition of the stochastic integral with respect to  $X$  of the form  $X = M + A$ , where M is a square integrable martingale and  $A$  is a process of finite variation on compacts by defining, under some conditions on  $H$ ,

$$H \cdot X = H \cdot M + H \cdot A \tag{13}$$

where  $H \cdot A$  can be computed as a path-by-path Lebesgue-Stieltjes integral. In this section, we establish the stochastic integral with respect to a general semimartingale. The idea would be similar to the construction of the stochastic integral with respect to Brownian motion. We show that the integral operator is a continuous mapping from the set of simple predictable process into an appropriate space so that we can extend the set of possible integrands to the closure of  $S$  in a certain topology.

**Definition 6** A sequence of processes  $(H^n)_{n>1}$  converges to a process  $H$  uniformly on compacts in probability (UCP) if, for each  $t > 0$ ,  $\sup_{0 \le s \le t} |H_s^n - H_s|$ converges to 0 in probability.

The following result is not surprising and one can refer to, for example,  $[7]$  for a proof.

**Theorem 6** The space  $S$  is dense in  $\mathbb{L}$  under the *UCP topology.* 

The following mapping is key to defining the stochastic integral with respect to a general semimartingale.

**Definition 7** For  $H \in \mathbf{S}$  and  $X$  being a càdlàg process, define the linear mapping  $J_X : \mathbf{S} \mapsto \mathbb{D}$  by

$$J_X(H) = H_0 X_0 + \int_{i=1}^n H_i(X^{T_{i+1}} - X^{T_i}) \qquad (14)$$

where  $H$  has the representation as in equation (5).

Note the difference between  $J_X$  and  $I_X$ .  $I_X$  maps processes into random variables, whereas  $J_X$  maps processes into processes.

**Definition 8** For  $H \in \mathbf{S}$  and X being an adapted càdlàg process, we call  $J_X(H)$  the stochastic integral of H with respect to  $X$ .

Observe that  $J_X(H)_t = I_{X^t}(H)$ . This property, combined with the definition of a semimartingale, yields the following continuity property for  $J_X$ .

**Theorem 7** Let X be a semimartingale and  $\mathbf{S}_{\text{UCP}}$ (respectively  $\mathbb{D}_{\text{UCP}}$ ) denote the space **S** (respectively,  $\mathbb{D}$ ) endowed with the UCP topology. Then the map- $\text{ping } J_X : \mathbf{S}_{\text{UCP}} \mapsto \mathbb{D}_{\text{UCP}} \text{ is continuous.}$ 

Using Theorem 6, we can now extend the integration operator  $J_X$  from **S** to  $\mathbb{L}$  by continuity, since  $\mathbb{D}_{\text{UCP}}$  is a complete metric space<sup>b</sup>.

**Definition 9** Let  $X$  be a semimartingale. The continuous linear mapping  $J_X : \mathbb{L}_{\text{UCP}} \mapsto \mathbb{D}_{\text{UCP}}$  obtained as the extension of  $J_X: \mathbf{S}_{\text{UCP}} \mapsto \mathbb{D}_{\text{UCP}}$  is called the stochastic integral.

Note that, in contrast to the  $L^2$  theory utilized in the previous section, we do not need to impose any integrability conditions on either  $X$  or  $H$  to establish the existence of the stochastic integral  $H \cdot X$  as long as H remains in  $\mathbb{L}$ . The above continuity property of the stochastic integrals moreover allows us to approximate the  $H \cdot X$  using the Riemann sums.

**Definition 10** Let  $\sigma$  denote a finite sequence of finite stopping times:

$$0 = T_0 \le T_1 \le \dots \le T_k < \infty. \tag{15}$$

The sequence of  $\sigma$  is called a random partition. A sequence of random partitions  $\sigma_n$ 

$$\sigma_n: 0 = T_0^n \le T_1^n \le \dots \le T_{k_n}^n \tag{16}$$

is said to tend to identity if

1.  $\lim_{n\to\infty} \sup_j T_j^n = \infty$ , a.s. and<br>2.  $\sup_j |T_{j+1}^n - T_j^n|$  converges to 0 a.s.

Let Y be a process and  $\sigma$  be a random partition. Define the process

$$Y^{\sigma} := Y_0 \mathbf{1}_{\{0\}} + \sum_j Y_{T_j} \mathbf{1}_{(T_j, T_{j+1}]} \tag{17}$$

Consequently, if Y is in  $\mathbb{D}$  or  $\mathbb{L}$ 

$$Y^{\sigma} \cdot X = Y_0 X_0 + \sum_j Y_{T_j} \left( X^{T_{j+1}} - X^{T_j} \right) \tag{18}$$

for any semimartingale  $X$ .

**Theorem 8** Let  $X$  be a semimartingale and let  $\int_{0+}^{t} H_s \, \mathrm{d}X_s \text{ denote } (H \cdot X)_t - H_0 X_0 \text{ for any } H \in \mathbb{L}.$ If  $Y$  is a process in  $\mathbb D$  or in  $\mathbb L$ , and  $(\sigma_n)$  is a sequence of random partitions tending to identity, then the process  $\left(\int_{0+}^{t} Y^{\sigma_n}_{s} dX_{s}\right)_{t\geq 0}$  converges to the stochastic integral  $(Y_{-}) \cdot X$  in  $\overset{\sim}{UCP}$ , where  $Y_{-}$  is the process defined as  $(Y_{-})_s = \lim_{r \to s, r \lt s} Y_r$ , for  $s > 0$ , and  $(Y_{-})_{0} = 0$ .

**Example 2** As an application of the above theorem, we calculate  $\int_0^t B_s \, dB_s$ , where B is a standard Brownian motion with  $B_0 = 0$ . Let  $(\sigma_n)$  be a sequence of random partitions of the form  $(16)$  tending to identity and let  $B^n = B^{\sigma_n}$ . Note that

$$\begin{split} \int_{0}^{t} B_{s}^{n} \, \mathrm{d}B_{s} &= \sum_{\substack{t_{j} \in \sigma_{n} \\ t_{j} < t}} B_{t_{j}} (B_{t \wedge t_{j+1}} - B_{t_{j}}) \\ &= \sum_{\substack{t_{j} \in \sigma_{n} \\ t_{j} < t}} \frac{1}{2} (B_{t \wedge t_{j+1}} + B_{t_{j}}) (B_{t \wedge t_{j+1}} - B_{t_{j}}) \\ &- \sum_{\substack{t_{j} \in \sigma_{n} \\ t_{j} < t}} \frac{1}{2} (B_{t \wedge t_{j+1}} - B_{t_{j}})^{2} \\ &= \frac{1}{2} B_{(t \wedge T_{k_{n}}^{n})}^{2} - \frac{1}{2} \sum_{\substack{t_{j} \in \sigma_{n} \\ t_{j} < t}} (B_{t_{j+1}} - B_{t_{j}})^{2} \tag{19} \end{split}$$

As *n* tends to  $\infty$ , the sum<sup>c</sup> in equation (19) is known to converge to t. Obviously,  $B_{T_{t}^{n} \wedge t}^{2}$  tends to  $B_t^2$  since  $\sigma_n$  tends to identity. Thus, we conclude via Theorem 8 that

$$\int_0^t B_s \, \mathrm{d}B_s = \frac{1}{2} B_t^2 - \frac{t}{2} \tag{20}$$

since *B* is continuous with  $B_0 = 0$ . Thus, the integration rules for a stochastic integral are quite different from those for an ordinary integral. Indeed, if  $A$ were a continuous process of finite variation with  $A_0 = 0$ , then the Riemann–Stieltjes integral of  $A \cdot A$ will yield the following formula:

$$\int_{0}^{t} A_{s} \, \mathrm{d}A_{s} = \frac{1}{2} A_{t}^{2} \tag{21}$$

As in the case of Brownian motion, stochastic integration with respect to a semimartingale preserves the martingale property.

**Theorem 9** Let  $H \in \mathbb{L}$  such that  $\lim_{t \downarrow 0} |H_t| < \infty$ and  $X$  be a local martingale (see **Martingales**). Then  $H \cdot X$  is also a local martingale.

Next, we would like to weaken the restriction that an integrand must be in  $\mathbb{L}$ . If we want the stochastic integral to still preserve the martingale property with this extended class of integrands, we inevitably need to restrict our attention to predictable processes. To see this, consider the process  $H = \mathbf{1}_{[0,T_1)}$  in Example 1. This process is not predictable since the jump times of a Poisson process are not predictable stopping times. As we have shown in Example 1, the integral of  $H$  with respect to a particular martingale is not a martingale.

Before we allow more general predictable integrands in a stochastic integral, we need to develop the notion of *quadratic variation* of a semimartingale. This is discussed in the following section.

#### **Properties of Stochastic Integrals**

In this section, H denotes an element of  $\mathbb{L}$  and X denotes a semimartingale. For a process  $Y \in \mathbb{D}$ , we define  $\Delta Y_t = Y_t - Y_{t-}$ , the jump at t. Recall that two process  $Y$  and  $Z$  are said to be *indistinguishable* if  $\mathbb{P}\{\omega: Y_t(\omega) = Z_t(\omega), \ \forall t\} = 1.$ 

**Theorem 10** Let T be a stopping time. Then  $(H \cdot$  $(X)^{T} = H\mathbf{1}_{[0,T]} \cdot X = H \cdot (X^{T}).$ 

**Theorem 11** The jump process  $(\Delta (H \cdot X)_t)_{t>0}$  is *indistinguishable from*  $(H_t \Delta X_t)_{t \ge 0}$ .

In finance theory, one often needs to work under the so-called *risk-neutral* measure rather than the empirical or objective measure  $\mathbb{P}$ . Recall that definitions of a semimartingale and its stochastic integral are given in spaces topologized by convergence in probability. Thus, one may wonder whether the value of a stochastic integral remains unchanged under an equivalent change of measure. The following theorem shows that this is indeed the case. Let  $\mathbb{Q}$  be another probability measure on  $(\Omega, \mathcal{F})$  and let  $H_{\mathbb{Q}} \cdot X$  denote the stochastic integral of  $H$  with respect to  $X$  computed under  $\mathbb{Q}$ .

**Theorem 12** Let  $\mathbb{Q} \ll \mathbb{P}$ . Then,  $H_{\mathbb{Q}} \cdot X$  is indistin*guishable from*  $H_{\mathbb{P}} \cdot X$ .

**Theorem 13** Let  $\mathbb{G} = (\mathcal{G}_t)_{t \ge 0}$  be another filtration such that H is in both  $L(\mathbb{G})$  and  $L(\mathbb{F})$ , and such that X is also a  $\mathbb{G}$ -semimartingale. Then  $H_{\mathbb{G}} \cdot X$  is indistinguishable from  $H_{\mathbb{F}} \cdot X$ .

The following theorem shows the stochastic integral is an extension of the Lebesgue-Stieltjes integral.

**Theorem 14** If X is an FV process, then  $H \cdot X$ is indistinguishable from the Lebesgue-Stieltjes integral, computed path by path. Consequently,  $H \cdot X$  is an FV process.

**Theorem 15** The stochastic integral is associative. That is,  $H \cdot X$  is also a semimartingale and if  $G \in \mathbb{L}$ 

$$G \cdot (H \cdot X) = (GH) \cdot X \tag{22}$$

**Definition 11** *The quadratic variation process of*  $X$ *,* denoted by  $[X, X] = ([X, X]_t)_{t>0}$ , is defined as

$$[X, X] = X^2 - 2X_{-} \cdot X \tag{23}$$

Recall that  $X_{0-} = 0$ . Let Y be another semimartingale. The quadratic covariation of  $X$  and  $Y$ , denoted by  $[X, Y]$ , is defined as

$$[X, Y] = XY - Y_{-} \cdot X - X_{-} \cdot Y \tag{24}$$

Since  $X_{-}$  (and  $Y_{-}$ ) belongs to  $\mathbb{L}$ , we can use Theorem 8 to deduce the following.

**Theorem 16** Let  $Y$  be a semimartingale. The quadratic covariation  $[X, Y]$  of  $X$  and  $Y$  is an adapted càdlàg process that satisfies the following:

- 1.  $[X, Y]_0 = X_0Y_0$  and  $\Delta[X, Y] = \Delta X \Delta Y$ .
- 2. If  $(\sigma_n)$  is a sequence of partitions tending to identity, then

$$X_0 Y_0 + \sum_{j} (X^{T_{j+1}^n} - X^{T_j^n})$$
$$\times (Y^{T_{j+1}^n} - Y^{T_j^n}) \to [X, Y] \qquad (25)$$

with convergence in UCP, where  $\sigma_n$  is of the form  $(16).$ 

3. If T is any stopping time, then  $[X^T, Y] =$  $[X, Y^T] = [X, Y]^T.$ Moreover,  $[X, X]$  is increasing.

Since  $[X, X]$  is increasing and càdlàg by definition, we immediately deduce that  $[X, X]$  is of finite variation. Moreover, the following polarization identity

$$[X,Y] = \frac{1}{2}([X+Y,X+Y] - [X,X] - [Y,Y])$$
(26)

reveals that  $[X, Y]$  is the difference of two increasing processes; therefore,  $[X, Y]$  is an FV process as well. This, in turn, implies  $XY$  is also a semimartingale and yields the *integration by parts* formula:

$$X_t Y_t = (X_- \cdot Y)_t + (Y_- \cdot X)_t + [X, Y]_t \qquad (27)$$

When  $X$  and  $Y$  are FV processes, the classical integration by parts formula reads as follows:

$$X_t Y_t = X_0 Y_0 + (X_- \cdot Y)_t + (Y_- \cdot X)_t + \sum_{0 < s \le t} \Delta X_s \Delta Y_s \qquad (28)$$

Therefore, if  $X$  or  $Y$  is a continuous processes of finite variation, then  $[X, Y] = X_0Y_0$ . In particular, if  $X$  is a continuous FV process, then its quadratic variation is equal to  $X_0^2$ .

**Theorem 17** Let  $X$  and  $Y$  be two semimartingales, and let  $H$  and  $K$  be two measurable processes. Then one has a.s.

$$\begin{split} & \int_{0}^{\infty} |H_{s}| |K_{s}| \mid \mathrm{d}[X,Y]_{s} | \\ & \leq \left( \int_{0}^{\infty} H_{s}^{2} \mathrm{d}[X,X]_{s} \right)^{\frac{1}{2}} \left( \int_{0}^{\infty} K_{s}^{2} \mathrm{d}[Y,Y]_{s} \right)^{\frac{1}{2}} \text{ (29)} \end{split}$$

The above inequality is called *Kunita-Watanabe* inequality. An immediate consequence of this inequality is that if  $X$  or  $Y$  has zero quadratic variation, then  $[X, Y] = 0$ . The following theorem follows from the definition of quadratic variation and Theorem 9.

**Theorem 18** Let  $X$  be a local martingale. Then,  $X^2 - [X, X]$  is a local martingale. Moreover,  $[X, X]$ is the unique adapted càdlàg and FV process A such that  $X^2 - A$  is a local martingale and  $\Delta A = (\Delta X)^2$ with  $A_0 = X_0^2$ .

Note that the uniqueness in the above theorem is lost if we do not impose  $\Delta A = (\Delta X)^2$ . Roughly speaking, the above theorem infers  $\mathbb{E}(X_t^2) = \mathbb{E}([X, X]_t)$ when  $X$  is a martingale. The following theorem formalizes this intuition.

**Corollary 1** Let  $X$  be a local martingale. Then,  $X$ is a martingale with  $\mathbb{E}(X_t^2) < \infty$ , for all  $t \geq 0$ , if and only if  $\mathbb{E}([X,X]_t) < \infty$ , for all  $t > 0$ . If  $\mathbb{E}([X,X]_t) <$  $\infty$ , then  $\mathbb{E}(X_t^2) = \mathbb{E}([X,X]_t)$ .

The following corollary to Theorem 18 is of fundamental importance in the theory of martingales.

**Corollary 2** Let  $X$  be a continuous local martingale, and  $S < T < \infty$  be stopping times. If X has paths of finite variation on the stochastic interval  $(S, T)$ ,

then  $X$  is constant on  $[S, T]$ . Moreover, if  $[X, X]$  is *constant on*  $[S, T] \cap [0, \infty)$ *, then X is also constant* there.

The following result is quite handy when it comes to the calculation of the quadratic covariation of two stochastic integrals.

**Theorem 19** Let Y be a semimartingale and  $K \in \mathbb{L}$ . Then

$$[H \cdot X, K \cdot Y]_t = \int_0^t H_s K_s \, d[X, Y]_s \qquad (30)$$

In the following section, we define the stochastic integral for predictable integrals. However, we already have all the results to present the celebrated  $It\hat{o}'s$ formula.

**Theorem 20** (Itô's Formula). Let X be a semimartingale and  $f$  be a  $C^2$  real function. Then  $f(X)$ is again a semimartingale and the following formula holds:

$$f(X_{t}) - f(X_{0}) = \int_{0+}^{t} f'(X_{s-}) \, dX_{s}$$
  
+  $\frac{1}{2} \int_{0+}^{t} f''(X_{s-}) \, d[X, X]_{s}$   
+  $\sum_{0 < s \le t} \left\{ f(X_{s}) - f(X_{s-}) - f'(X_{s-}) \Delta X_{s} - \frac{1}{2} f''(X_{s-}) (\Delta X_{s})^{2} \right\}$  (31)

# **Stochastic Integration for Predictable** Integrands

In this section, we weaken the hypothesis that  $H \in \mathbb{L}$ in order for  $H \cdot X$  to be well defined for a semimartingale  $X$ . As explained earlier, we restrict our attention to predictable processes since we want the stochastic integral to preserve the martingale property. We will not be able to show the existence of stochastic integral  $H \cdot X$  for all  $H \in \mathcal{P}$  but, as in the section  $L^2$  Theory of Stochastic Integration with Respect to Brownian Motion, we give a meaning to  $H \cdot X$  for the appropriately integrable processes in  $\mathcal{P}$ . First, we assume that  $X$  is a special semimartingale, that is, there exist processes  $M$  and  $A$  such that  $M$  is a local martingale and  $A$  is predictable and of finite variation with  $M_0 = A_0 = 0$  and  $X = X_0 + M + A$ . This decomposition of a special semimartingale is unique and called the *canonical decomposition*. Without loss of generality, let us assume that  $X_0 = 0$ .

**Definition 12** Let  $X$  be a special semimartingale with the canonical decomposition  $X = M + A$ . The  $\mathcal{H}^2$  norm of X is defined as

$$\parallel X \parallel_{\mathcal{H}^{2}} := \parallel [M, M]_{\infty}^{1/2} \parallel_{L^{2}} + \parallel \int_{0}^{\infty} \mid \mathrm{d}A_{s} \mid \parallel_{L^{2}}$$
(32)

The space of  $\mathcal{H}^2$  semimartingales consists of special semimartingales with finite  $\mathcal{H}^2$  norm. We write  $X \in$  $\mathcal{H}^2$  to indicate that X belongs to the space of  $\mathcal{H}^2$ semimartingales.

One can show that the space of  $\mathcal{H}^2$  semimartingales is a Banach space, which is the key property to extend the definition of stochastic integrals for a more general class of integrands. Let  $\mathbf{b} \mathbb{L}$  denote the space of bounded adapted processes with càglàd paths and  $\mathbf{b}\mathcal{P}$  denote the space of bounded predictable processes.

**Definition 13** Let  $X \in \mathcal{H}^2$  with the canonical decomposition  $X = N + A$  and let  $H, J \in \mathbf{b}\mathcal{P}$ . We define the metric  $d_X(H, J)$  as

$$d_X(H, J) := \left\| \left( \int_0^\infty (H_s - J_s)^2 \, \mathrm{d}[M, M]_s \right)^{1/2} \right\|_{L^2} + \left\| \int_0^\infty |H_s - J_s|| \, \mathrm{d}A_s| \right\|_{L^2} \tag{33}$$

From the monotone class theorem, we obtain the following.

**Theorem 21** For  $X \in \mathcal{H}^2$ , the space **b**L is dense in **b** $\mathcal{P}$  under  $d_{\mathcal{X}}(\cdot,\cdot)$ .

It is straightforward to show that if  $H \in \mathbf{b} \mathbb{L}$  and  $X \in$  $\mathcal{H}^2$ , then  $H \cdot X \in \mathcal{H}^2$ . The following is an immediate consequence of the definition of  $d_X(\cdot, \cdot)$ .

**Theorem 22** Let  $X \in \mathcal{H}^2$  and  $(H^n) \subset \mathbf{b} \mathbb{L}$  such that  $(H^n)$  is Cauchy under  $d_X(\cdot, \cdot)$ . Then,  $(H^n \cdot X)$  is Cauchy in  $\mathcal{H}^2$ .

Moreover, it is easy to show that if  $(H^n) \subset \mathbf{b} \mathbb{L}$  and  $(J^n) \subset \mathbf{b} \mathbb{L}$  converge to the same limit under  $d_X(\cdot, \cdot)$ , then  $(H^n \cdot X)$  and  $(J^n \cdot X)$  converge to the same limit in  $\mathcal{H}^2$ . Thus, we can now define the stochastic integral  $H \cdot X$  for any  $H \in \mathbf{b}\mathcal{P}$ .

**Definition 14** Let  $X \in \mathcal{H}^2$  and  $H \in \mathbf{b}\mathcal{P}$ . Let  $(H^n) \subset$ **b**L *such that*  $\lim_{n\to\infty} d_X(H^n, H) = 0$ . *The stochastic* integral  $H \cdot X$  is the unique semimartingale  $Y \in \mathcal{H}^2$ such that  $\lim_{n\to\infty} H^n \cdot X = Y$  in  $\mathcal{H}^2$ .

Note that if  $B$  is a standard Brownian motion,  $B$ is not in  $\mathcal{H}^2$  but  $B^T \in \mathcal{H}^2$  for any deterministic and finite T. Therefore, for any  $H \in \mathbf{b}\mathcal{P}$ ,  $H \cdot B^T$  is well defined. Moreover,  $H \in \mathbf{b}\mathcal{P}$  implies  $H \in \mathcal{L}^2(B^T)$ where  $\mathcal{L}^2(B^T)$  is the space defined in the section  $L^2$  Theory of Stochastic Integration with Respect to Brownian Motion. One can easily check that the stochastic integral  $H \cdot B^T$  defined by Definition 14 is indistinguishable from the stochastic integral  $H \cdot B^T$ defined in the section  $L^2$  Theory of Stochastic Integration with Respect to Brownian Motion. Clearly,  $\mathbf{b}\mathcal{P}$  is strictly contained in  $\mathcal{L}^2(B^T)$ , and we know from the section  $L^2$  Theory of Stochastic Integration with Respect to Brownian Motion that it is possible to define the stochastic integral with respect to  $B^T$ for any process in  $\mathcal{L}^2(B^T)$ . Thus, it is natural to ask whether we can extend the stochastic integral given by Definition 14 to integrands that satisfy a certain square integrability condition.

**Definition 15** Let  $X \in \mathcal{H}^2$  with the canonical decomposition  $X = M + A$ . We say that  $H \in \mathcal{P}$  is  $(\mathcal{H}^2, X)$  integrable if

$$\mathbb{E}\left(\int_{0}^{\infty}H_{s}^{2}\mathrm{d}[M,M]_{s}\right) + \mathbb{E}\left(\left\{\int_{0}^{\infty}|H_{s}||\mathrm{d}A_{s}|\right\}^{2}\right) < \infty \qquad (34)$$

It can be shown that if  $H \in \mathcal{P}$  is  $(\mathcal{H}^2, X)$  integrable,  $(H^n \cdot X)$  is a Cauchy sequence in  $\mathcal{H}^2$  where  $H^n =$  $H\mathbf{1}_{\{|H| \le n\}}$  is in **b** $\mathcal{P}$ , which means that we can define the stochastic integral for such  $H$ .

**Definition 16** Let  $X \in \mathcal{H}^2$  and let  $H \in \mathcal{P}$  be  $(\mathcal{H}^2, X)$ integrable. The stochastic integral  $H \cdot X$  is defined to be the  $\lim_{n\to\infty} H^n \cdot X$ , with convergence in  $\mathcal{H}^2$ , where  $H^n = H\mathbf{1}_{\{|H| < n\}}.$ 

In the case  $X = B^T$ ,  $M = B^T$ , and  $A = 0$ ; therefore, H being  $(\mathcal{H}^2, X)$  integrable is equivalent to the condition

$$\int_0^I \mathbb{E}(H_s^2) \, \mathrm{d}s < \infty \tag{35}$$

which gives exactly the elements of  $\mathcal{L}^2(B^T)$ .

So far, we have been able to define the stochastic integral with predictable integrands only for semimartingales in  $\mathcal{H}^2$ . This seems to be a major restriction. However, as the following theorem shows, it is not. Recall that for a stopping time T,  $X^{T-}$  =  $X\mathbf{1}_{[0,T)} + X_{T-}\mathbf{1}_{[T,\infty]}.$ 

**Theorem 23** Let X be a semimartingale,  $X_0 =$ 0. Then X is prelocally in  $\mathcal{H}^2$ . That is, there exists a nondecreasing sequence of stopping times  $(T^n)$ ,  $\lim_{n\to\infty} T^n = \infty$  a.s., such that  $X^{T^n -} \in \mathcal{H}^2$ , for each  $n \geq 1$ .

**Definition 17** Let  $X$  be a semimartingale and  $H \in \mathcal{P}$ . The stochastic integral  $H \cdot X$  is said to exist if there exists a sequence of stopping times  $(T^n)$  increasing to  $\infty$  a.s. such that  $X^{T^{n-}} \in \mathcal{H}^2$ , for each  $n \ge 1$ , and such that  $H$  is  $(\mathcal{H}^2, X^{T^n-})$  integrable for each  $n \geq 1$ . In this case, we write  $H \in L(X)$  and define the stochastic integral as

$$H \cdot X = H \cdot (X^{T^{n}}), \qquad on \ [0, T^{n}) \tag{36}$$

for each n.

A particular case when  $H \cdot X$  is well defined is when  $H$  is locally bounded.

**Theorem 24** Let *X* be a semimartingale and  $H \in \mathcal{P}$ be locally bounded. Then,  $H \in L(X)$ .

We also have the martingale preservation property.

**Theorem 25** Let  $M$  be a local martingale and  $H \in \mathcal{P}$  be locally bounded. Then,  $H \cdot M$  is a local martingale.

The general result that  $M$  a local martingale and  $H \in L(M)$  implies that  $H \cdot M$  is a local martingale is not true. The following example is due to Emery and can be taken as a starting point for a study of *sigma*martingales (see Equivalent Martingale Measures).

**Example 3** Let  $T$  be an exponential random variable with parameter 1 and let  $U$  be an independent random variable with  $\mathbb{P}(U=1) = \mathbb{P}(U=-1) =$  $1/2$ , and set  $X = U\mathbf{1}_{[T,\infty)}$ . Then, X is a martingale in its own filtration. Let *H* be defined as  $H_t = \frac{1}{t} \mathbf{1}_{\{t>0\}}$ .  $H$  is a deterministic predictable integral. Note that  $H$  is not locally bounded, being only continuous on  $(0, \infty)$ .  $H \cdot X$  exists as a Lebesgue-Stieltjes integral since X has paths of finite variation. However,  $H \cdot X$ is not a local martingale since, for any stopping time S with  $P(S > 0) > 0$ ,  $\mathbb{E}(|(H \cdot X)_S|) = \infty$ .

When  $M$  is a continuous local martingale, the theory becomes nicer.

**Theorem 26** Let  $M$  be a continuous local martingale and let  $H \in \mathcal{P}$  be such that  $\int_0^t H_s^2 d[M, M]_s <$  $\infty$ , for each  $t \geq 0$ . Then  $H \in L(M)$  and  $H \cdot M$  is a continuous local martingale.

The question may arise as to whether the properties of stochastic integral stated for left-continuous integrands in the section Properties of Stochastic Integrals continue to hold when we allow predictable integrands. The answer is positive except for Theorems 13 and 14. Still, if  $X$  is a semimartingale with paths of finite variation on compacts and if  $H \in L(X)$  is such that the Stieltjes integral  $\int_0^t |H_s| |dX_s|$  exists a.s. for each  $t \ge 0$ , then the stochastic integral  $H \cdot X$  agrees with the Stieltjes integral computed path by path. However,  $H \cdot X$  is not necessarily an FV process. See [7, Exercise 45] in Chapter IV] of [7] for a counterexample. The analogous result for Theorem 13 is the following, which is particularly useful when one needs to study asymmetric information in financial markets where some traders possess extra information compared to others.

**Theorem 27** Let  $\mathbb{G}$  be another filtration satisfying the usual hypotheses and suppose that  $\mathcal{F}_t \subset \mathcal{G}_t$ , each  $t > 0$ , and that X remains a semimartingale with respect to  $\mathbb{G}$ . Let H be locally bounded and predictable for  $\mathbb{F}$ . Then H is locally bounded and predictable for  $\mathbb{G}$ , the stochastic integral  $H_{\mathbb{G}} \cdot X$  exists and is equal to  $H_{\mathbb{F}} \cdot X$ .

It is important to have  $H$  locally bounded in the above theorem; see [4] for a counterexample in the context of enlargement of filtrations.

We end this section with the *dominated conver*gence theorem for stochastic integrals.

**Theorem 28** Let  $X$  be a semimartingale and  $(H^n) \subset \mathcal{P}$  be a sequence converging a.s. to a limit  $H \in \mathcal{P}$ . If there exists a process  $G \in L(X)$  such that  $|H^n| \leq G$ , for all n, then  $H^n \in L(X)$  for all  $n, H \in$  $L(X)$  and  $(H^n \cdot X)$  converges to  $H \cdot X$  in UCP.

### **Concluding Remarks**

In this article, we used the approach of Protter [7] to define the semimartingale as a good integrator and construct its stochastic integral. Another approach that is closely related is given by Chou *et al.* [1], who developed the stochastic integration for general predictable integrands with respect to a semimartingale in a space endowed with the semimartingale topology. Historically, the stochastic integral was first proposed for Brownian motion by Itô [3], then for continuous martingales, then for square integrable martingales, and finally for càdlàg processes that can be written as the sum of a locally square integrable local martingale and an FV process by J.L. Doob, H. Kunita, S. Watanabe, P. Courrège, P.A. Meyer, and others. Later in 1970, Doléans-Dade and Meyer [2] showed that the local square integrability condition could be relaxed, which led to the traditional definition of a semimartingale as a sum of a local martingale and an FV process. A different theory of stochastic integration, the *Itô-belated integral*, was developed by McShane [5]. It imposed different restrictions on the integrators and the integrands and used a theory of "gauges" and appeared to be very different from the approach here. It turns out, however, that when the integral  $\int H dX$  made sense both as a stochastic integral in the sense developed here and as an Itô-belated integral, they were indistinguishable. See [6] for a comparison of these two integrals. Another related stochastic integral is called the Fisk-Stratonovich (FS) integral that was developed by Fisk and Stratonovich independently. The FS integral obeys the integration by parts formula for FV

processes when at least one of the integrand or the integrator is continuous.

### **End Notes**

<sup>a.</sup> See Definition 5 for the definition of a predictable process. <sup>b.</sup>For a proof of the fact that  $\mathbb{D}_{\text{UCP}}$  is metrizable and complete under that metric, see [7].

<sup>c.</sup>This sum converges to the *quadratic variation* of  $B$  over the interval  $[0, t]$  as we see in Theorem 16.

#### References

- [1] Chou, C.S., Meyer, P.A. & Stricker, C. (1980). Sur les intégrales stochastiques de processus prévisibles non bornés, Séminaire de Probabilités, XIV. Lecture Notes in Mathematics, 784, Springer, Berlin, pp. 128-139.
- [2] Doléans-Dade, C. & Meyer, P.-A. (1970). Intégrales stochastiques par rapport aux martingales locales, Séminaire de Probabilités, IV. Lecture Notes in Mathematics, 124, Springer, Berlin, pp. 77-107.
- [3] Itô, K. (1944). Stochastic integral, Proceedings of the Imperial Academy of Tokyo 20, 519-524.
- [4] Jeulin, T. (1980). Semi-martingales et Grossissement d'une Filtration, Lecture Notes in Mathematics, Springer, Berlin, Vol. 833.
- [5] McShane, E.J. (1974). *Stochastic Calculus and Stochastic* Models, Probability and Mathematical Statistics, Academic Press, New York, Vol. 25.
- [6] Protter, P. (1979). A comparison of stochastic integrals, The Annals of Probability 7(2), 276–289.
- [7] Protter, P. (2005). Stochastic Integration and Differential *Equations*, 2nd Edition, Version 2.1, Springer, Berlin.

### **Related Articles**

Arbitrage Strategy; Complete Markets; Equivalent Martingale Measures: Filtrations: Itô's Formula; Martingale Representation Theorem; Semimartingale.

Umut Cetin
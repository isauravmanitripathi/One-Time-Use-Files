# **Early Exercise Options: Upper Bounds**

#### **Setup and Basic Results**

We work, as usual, on a filtered probability space and consider a contingent claim with *early exercise* rights, that is, the right to accelerate payment on the claim at will. Let the claim in question be characterized by an adapted, nonnegative payout process  $U(t)$ , payable to the option holder at a stopping time (or *exercise policy*)  $\tau < T$ , chosen by the holder. If early exercise can take place at any time in some interval, we say that the derivative security is an American option; if exercise can only take place on a discrete set of dates, we say that it is a *Bermudan option*.

Let the allowed set of exercise dates larger than or equal to t be denoted  $\mathcal{D}(t)$ , and suppose that we are given at time 0 a particular exercise policy  $\tau$  taking values in  $\mathcal{D}(0)$ , as well as a pricing numeraire N inducing a unique martingale measure  $Q^N$ . Let  $C^{\tau}(0)$ be the time  $0$  value of a derivative security that pays  $U(\tau)$ . Under technical conditions on  $U(t)$ , we can write the value of the derivative security as

$$C^{\tau}(0) = \mathbf{E}^{N} \left( \frac{U(\tau)}{N(\tau)} \right) \tag{1}$$

where  $E^{N}(\cdot)$  denotes expectation in measure  $Q^{N}$  and where we have assumed, with no loss of generality, that  $N(0) = 1$ . Let  $T(t)$  be the time t set of (future) stopping times taking value in  $\mathcal{D}(t)$ . In the absence of arbitrage, the time 0 value  $C(0)$  of a security with early exercise into  $U$  is then given by the *optimal* stopping problem

$$C(0) = \sup_{\tau \in \mathcal{T}(0)} C^{\tau}(0) = \sup_{\tau \in \mathcal{T}(0)} \mathcal{E}^{N}\left(\frac{U(\tau)}{N(\tau)}\right) \tag{2}$$

reflecting the fact that a rational investor would choose an exercise policy to optimize the value of his/her claim.

With  $E_t^N(\cdot)$  denoting expectation conditional on the information (i.e., the filtration) at time  $t$ , we can extend equation  $(2)$  to future times t

$$C(t) = N(t) \sup_{\tau \in \mathcal{I}(t)} \mathcal{E}_t^N \left(\frac{U(\tau)}{N(\tau)}\right) \tag{3}$$

where  $\sup_{\tau} \mathbf{E}_{t}^{N} \left(U(\tau)/N(\tau)\right)$  is known as the *Snell* envelope of  $U/N$  under  $O^N$ . Here  $C(t)$  must be interpreted as the value of the option with early exercise, *conditional* on exercise not having taken place before time *t*. To make this explicit, let  $\tau^*$  ∈  $T(0)$  be the optimal exercise policy, as seen from time 0. We can then write, for  $0 < t \leq T$ ,

$$C(0) = \mathbf{E}^{N} \left( \mathbf{1}_{\{\tau^* \ge t\}} C(t) / N(t) \right)$$
  
+ 
$$\mathbf{E}^{N} \left( \mathbf{1}_{\{\tau^* < t\}} U(\tau^*) / N(\tau^*) \right) \tag{4}$$

where we break the time 0 value into two components: one from the time  $t$  value of the option, should it not have been exercised before time  $t$ , and other from the right to exercise on  $[0, t]$ . As we can always elect —possibly suboptimally —to never exercise on  $[0, t]$ , from equation (4) we see that

$$C(0) \ge \mathcal{E}^N \left( C(t) / N(t) \right) \tag{5}$$

which establishes that  $C(t)/N(t)$  is a *supermartingale* under  $O^N$ . This result also follows directly from known properties of the Snell envelope; see [13].

In numerical implementations, it is most relevant to consider the discrete-time (i.e., Bermudan) case and assume that  $\mathcal{D}(0) = \{T_1, T_2, \ldots, T_B\},\$ where  $T_1 > 0$  and  $T_B = T$ . For  $t \in (T_i, T_{i+1})$ , define  $H_i$  as the time t value of the Bermudan option when exercise is restricted to the dates  $\mathcal{D}(T_{i+1}) =$  $\{T_{i+1}, T_{i+2}, \ldots, T_B\}$ ; that is,

$$H_i(t) = N(t) \mathcal{E}_t^N \left( C(T_{i+1}) / N(T_{i+1}) \right),$$
  

$$i = 1, \dots, B - 1$$
 (6)

At time  $T_i$ ,  $H_i(T_i)$  can be interpreted as the *holding* value of the Bermudan option, that is, the value of the Bermudan option if not exercised at time  $T_i$ . If an optimal exercise policy is followed, clearly we must have at time  $T_i$ 

$$C(T_i) = \max (U(T_i), H_i(T_i)), \quad i = 1, \dots, B$$
 (7)

such that

$$H_i(t) = N(t) \mathbf{E}_t^N \left( \max \left( U(T_{i+1}), H_{i+1}(T_{i+1}) \right) \right),$$
  

$$i = 1, \dots, B - 1 \tag{8}$$

Starting with the terminal condition  $H_B(T) = 0$ , equation (8) defines an backward iteration in time for the value  $C(0) = H_0(0)$ .

## **Option Pricing Bounds**

In a setting where  $U(t)$  is a function of a lowdimensional diffusion process, the iteration (8) can often be solved numerically by partial differential equations (PDE) or lattice methods, for example, the finite difference method (see Finite Difference Methods for Early Exercise Options). In many cases of practical interest, however, these methods either do not apply or are computationally infeasible. In such situations, we may be interested in at least bounding the value of an option with early exercise rights. Providing a *lower bound* is straightforward: postulate an exercise policy  $\tau$  and compute the price  $C^{\tau}(0)$  by direct methods, for example, the Monte Carlo method. From equation (2), this clearly provides a lower bound

$$C^{\tau}(0) \le C(0) \tag{9}$$

The closer the postulated exercise policy  $\tau$  is to the optimal exercise policy  $\tau^*$ , the tighter this bound will be. Two common strategies for approximation of  $\tau^*$ in a Monte Carlo setting are discussed in Bermudan Options and Exercise Boundary Optimization **Methods**, the first based on regression estimates of holding values  $H$  in equation (8) and the second on optimization of parametric rules for the exercise strategy.

To produce an *upper bound*, we can rely on duality results established in [9, 14]. To present these results here, let  $\mathcal{K}$  denote the space of adapted martingales  $\pi$ for which  $\sup_{\tau \in [0,T]} \mathbb{E}^N |\pi(\tau)| < \infty$ . For a martingale  $\pi \in \mathcal{K}$ , we then write

$$C(0) = \sup_{\tau \in \mathcal{T}(0)} \mathcal{E}^{N} \left( \frac{U(\tau)}{N(\tau)} \right)$$
  
$$= \sup_{\tau \in \mathcal{T}(0)} \mathcal{E}^{N} \left( \frac{U(\tau)}{N(\tau)} + \pi(\tau) - \pi(\tau) \right)$$
  
$$= \pi(0) + \sup_{\tau \in \mathcal{T}(0)} \mathcal{E}^{N} \left( \frac{U(\tau)}{N(\tau)} - \pi(\tau) \right) \tag{10}$$

In the second equality, we have relied on the *optional* sampling theorem to tell us that the martingale property is satisfied up to a bounded random stopping time, that is, that  $E^N(\pi(\tau)) = \pi(0)$ . See [12] for details. We now turn the above result into an upper bound by forming a pathwise maximum at all possible future exercise dates  $\mathcal{D}(0)$ :

$$C(0) = \pi(0) + \sup_{\tau \in \mathcal{T}(0)} \mathbf{E}^{N} \left( \frac{U(\tau)}{N(\tau)} - \pi(\tau) \right)$$
  
$$\leq \pi(0) + \mathbf{E}^{N} \left( \max_{t \in \mathcal{D}(0)} \left( \frac{U(t)}{N(t)} - \pi(t) \right) \right) \tag{11}$$

With equations  $(9)$  and  $(11)$  we have, as desired, established upper and lower bounds for values of options with early exercise rights. Let us consider how to make these bounds tight. As mentioned earlier, to tighten the lower bound we need to pick exercise strategies close to the optimal one. Tightening the upper bound is a bit more involved and requires usage of the Doob-Meyer decomposition (see **Doob–Meyer Decomposition**), which can be used here to show that

$$C(t)/N(t) = M(t) - A(t) \tag{12}$$

where  $M(t)$  is a martingale and  $A(0)$  an increasing, predictable process with  $A(0) = 0$  (such that  $C(0) =$  $M(0)$ ). Given equation (12), consider taking  $\pi(t)$  =  $M(t)$  in equation (11), to get

$$C(0) \leq C(0) + \mathcal{E}^{N} \left( \max_{t \in \mathcal{D}(0)} \frac{U(t)}{N(t)} - M(t) \right)$$
  
=  $C(0) + \mathcal{E}^{N} \left( \max_{t \in \mathcal{D}(0)} \frac{U(t)}{N(t)} - \frac{C(t)}{N(t)} - A(t) \right)$   
\$\leq C(0). \qquad (13)\$

The last inequality follows from the fact that  $C(t)$  >  $U(t)$  and  $A(t) > 0$ . As  $M(0) = C(0)$ , it follows that the quantity

$$M(0) + \mathbf{E}^N \left( \max_{t \in \mathcal{D}(0)} \frac{U(t)}{N(t)} - M(t) \right),$$
  
$$M(t) = \frac{C(t)}{N(t)} + A(t) \tag{14}$$

is bounded by  $C(0)$  from both above and below, that is, it must equal  $C(0)$ . We have thereby arrived at a *dual* formulation of the option price

$$C(0) = \inf_{\pi \in \mathcal{K}} \left( \pi(0) + \mathbf{E}^N \left( \max_{t \in \mathcal{D}(0)} \frac{U(t)}{N(t)} - \pi(t) \right) \right)$$
(15)

and have demonstrated that the infimum is attained when the martingale  $\pi$  is set equal to the martingale component  $M$  of the deflated price process  $C(t)/N(t)$ .

## **Monte Carlo Upper Bound Methods**

Let us consider how we can use the upper bound results  $(11)$  and  $(15)$  in an actual Monte Carlo application. According to equation (11), to generate an upper bound for the true option price, it evidently suffices to simply pick *any* martingale process adapted to the filtration we work in, and then compute the expectation (11) by Monte Carlo methods. For instance, if the filtration is generated by a vectorvalued Brownian motion  $W(t)$ , we can always set

$$\pi(t) = \int_0^t \sigma(t)^\top \, \mathrm{d}W(t) \tag{16}$$

for some adapted vector-process  $\sigma(t)$  satisfying the usual conditions required for the stochastic integral to be a proper martingale. Clearly, however, if  $\sigma(t)$ is chosen arbitrarily, the resulting upper bound is likely to be very loose, and probably not very useful. While equation (15) is of little immediate practical use (since we do not know the process  $C(t)/N(t)$ ), it does suggest that for a chosen martingale  $\pi(t)$  in equation  $(11)$  to produce a tight upper bound, it needs to be "close" to  $M(t)$ .

Several strategies have been proposed for constructing a good martingale  $\pi(t)$ . When working on a simple model set up on simple payouts, sometimes one can make inspired guesses for what  $\pi(t)$  should be. For instance, in a one-dimensional Black-Scholes model, Rogers [14] shows that using the numerairedeflated European put option price (which is analytically known) as a guess for  $\pi(t)$  generates good bounds for a Bermudan put option price. This approach, however, does not easily generalize to settings with more complicated dynamics and/or more complicated exercise payouts.

#### The Andersen-Broadie Algorithm

A general strategy for generating upper bounds is proposed in [1], which can start from any approximation to the optimal exercise strategy, perhaps generated from either of the methods in Bermudan Options or Exercise Boundary Optimization Methods. Using a straightforward "simulationwithin-a-simulation" approach, the authors construct an estimate to the value process  $C^{\tau}(t)$  and use its estimated martingale component as  $\pi(t)$  in equation (11). Specifically, working on a discrete timeline, they set

$$\pi(T_{i+1}) - \pi(T_i) = \frac{C^{\tau}(T_{i+1})}{N(T_{i+1})} - \mathcal{E}_{T_i}^N \left(\frac{C^{\tau}(T_{i+1})}{N(T_{i+1})}\right)$$
$$= \mathcal{E}_{T_{i+1}}^N \left(\frac{U(\tau)}{N(\tau)}\right) - \mathcal{E}_{T_i}^N \left(\frac{U(\tau)}{N(\tau)} | \tau \ge T_{i+1}\right) \tag{17}$$

where nested simulations are used to estimate both expectations on the right-hand side of the equation.<sup>a</sup> The resulting Monte Carlo estimate of the upper bound is shown to be biased high always, with the bias being a decreasing function in the number of inner simulation trials. As suggested by equation  $(15)$ , the upper bound produced by the algorithm in  $[1]$  strongly depends on the quality of the exercise strategy: the better the strategy, the tighter the bound.

The need for nested simulations makes the algorithm in [1] expensive: if  $M$  is the number of outer simulations and  $K$  the number of inner simulations. an option with  $B$  exercise opportunities will involve a worst case workload proportional to

$$M \cdot K \cdot B^2 \tag{18}$$

For comparison, a lower bound simulation has a workload proportional to  $M \cdot B$ , plus whatever work is required to estimate the exercise rule in a presimulation. In many cases the inner simulations can be stopped quickly (due to early exercise); thus, in practice the dependence on  $B$  in equation (18) is often less than quadratic and sometimes close to linear. In addition, in [3] it is shown—along with other ideas for efficiency improvements—that inner simulations are not needed on dates where it is suboptimal to exercise the option, which can lead to considerable time savings, especially for out-of-the-money options. Finally,  $K$  can often be set to a number much smaller than  $M$  without significantly affecting the quality of the upper bound, and even very small values of  $K$  (e.g.,  $50-100$  or less) may yield informative results. With the computational improvements suggested in [3], upper bound computations on a range of different option payouts take on the order of  $1-10$  CPU minutes compared with  $0.1-2$  CPU minutes for the lower

bound. Of course, the CPU times depend on the speed of the processor, but it is safe to say that relatively tight confidence intervals for most option types can be obtained in times measured in minutes, not in hours as is commonly believed.

The strategy in  $[1]$  is generic, in that it can handle virtually any type of multidimensional process dynamics and security payouts. Despite the computational drawbacks, the use of nested simulation guarantees that the choice of  $\pi$  induces an upper bound estimate that is biased high. Importantly, this key property is *not* shared by many alternative estimators, such as regression, of the expectations in equation  $(17)$ . One exception is discussed in [8] where a special martingale-preserving regression approach is introduced. This algorithm, however, requires strong conditions on regression basis functions that may be hard to check in practice.

#### The Belomestny–Bender–Schoenmakers Algorithm

In the special case where dynamics are driven only by Brownian motions, the usual martingale representation theorems show that the optimal strategy  $\pi^*(t)$ must be an Ito integral, that is, of the form in equation (16). Starting again from a postulated exercise strategy, Belomestny *et al.*  $[2]$  use this observation to construct a regression on a set of basis functions to uncover an estimate for the function  $\sigma(t)$ . By applying regression techniques this way—rather than to directly compute expectations of  $U(\tau)/N(\tau)$ —the authors are able to construct a true martingale process  $\pi(t)$ , which can be turned into a valid upper bound through equation (11). The resulting nonnested simulation algorithm requires careful implementation to yield stable results, in part, because the optimal integrand  $\sigma(t)$  can be expected to be considerably less regular than  $\pi^*(t)$  itself; this, in turn, requires additional thought in the selection of appropriate basis functions for the regression. One possibility advocated in [2] is to include, whenever available, exact or approximate expressions for the diffusion term in dynamics of several still-alive European options underlying the Bermudan option. This strategy is akin to that of  $[14]$ , and its feasibility depends on the pricing problem at hand. In cases where it does apply, the authors of [2] demonstrate that their method gives good results, with the upper bound often being nearly as tight as that of the nested algorithm in [1]. They also show how to use their technique to develop a variance-reduced version of the algorithm in [1].

#### **Confidence Intervals and Practical Usage**

Assume that we have estimated an exercise strategy using either of the approaches in Bermudan Options or Exercise Boundary Optimization Methods. Suppose that the Monte Carlo estimate for the lower bound price is  $\hat{C}_{lo}(0)$  with a sample standard deviation of  $\hat{s}_{lo}$  based on  $M_{lo}$  Monte Carlo trials. Using, say, the algorithm in [1], we also estimate an upper bound  $\hat{C}_{hi}(0)$  with a sample standard deviation  $\hat{s}_{hi}$  computed from  $M_{hi}$  (outer) simulation trials. With  $z_x$  denoting the xth percentile of a standard Gaussian distribution, asymptotically a  $100(1 - \alpha)\%$ confidence interval for the true price  $C(0)$  must be  $\text{tighter}^{\text{b}}$  than

$$\left[\hat{C}_{lo}(0) - z_{1-\alpha/2} \frac{\hat{s}_{lo}}{\sqrt{M_{lo}}}; \hat{C}_{hi}(0) - z_{1-\alpha/2} \frac{\hat{s}_{hi}}{\sqrt{M_{hi}}}\right] \tag{19}$$

Most often, upper bound simulation algorithms can be expected to be both more involved and/or more expensive than lower bound simulation methods. In many cases, the role of the upper bound simulation algorithm will therefore be to test whether postulated lower bound exercise strategies are tight or not. Specifically, starting from some guess for the exercise strategy, we can produce confidence intervals using equation (19) to test whether the lower bound estimate is of good quality, in which case the confidence interval can be made tight by using large values of  $M_{lo}$  and  $M_{hi}$  (as well as the number of inner simulation trials). In case the lower bound estimator is deemed unsatisfactory, we can iteratively refine it, by altering the choice of basis functions, say, until the confidence interval is tight. Importantly, such tests can often be done at a high level, covering entire classes of payouts and/or models. Once an exercise strategy has been validated for a particular product or model, day-to-day pricing of Bermudan securities can be done by the lower bound method, with only occasional runs of the upper bound method needed (e.g., if market conditions change markedly). If upper bound methods are predominantly used in this manner, the fact that they may sometimes be computationally intensive<sup>c</sup> becomes less punitive.

#### **Extensions and Related Work**

The results  $(11)$  and  $(15)$  are sometimes known as additive duality results. Jamshidian [10] has introduced alternative *multiplicative* results. A comparative study of additive and multiplicative duality was undertaken in [7], with the authors concluding that the additive duality results are preferable in applications.

Earlier methods for producing lower and upper bounds were proposed in [5, 6]. Both methods [5, 6] have the significant feature of producing automatically convergent bounds. However, [5] is only practical when the number of exercise dates is a small finite number (e.g., less than five). The method proposed in [6] does not suffer this drawback, but is more challenging to implement and is substantially slower than most lower bounds methods.

Finally, let us note that computation of upper bounds by Monte Carlo simulation theoretically extends to option sensitivities (Greeks), as demonstrated in [11] where duality is applied to the likelihood ratio method (see [4]). As the proposed algorithm is very computationally intensive, the practical value of this result remains to be seen.

#### **End Notes**

<sup>a</sup> In cases where  $U(t)$  is not known in closed form as may be the case for complicated callable securities (see Bermudan Swaptions and Callable Libor Exotics)nested simulation can also be used to establish estimates for  $U(t)$ .

<sup>b</sup>. The confidence interval is conservative because of the low bias in  $\hat{C}_{l_0}(0)$  (i.e.,  $E^N(\hat{C}_{l_0}) \leq C(0)$ ) and the high bias in  $\hat{C}_{hi}(0)$  which originates in part from the nature of the upper bound, and in part from the earlier mentioned additional high bias introduced by the inner simulations.

<sup>c</sup>.Note, though, that in testing the viability of a class of exercise rules through an upper bound simulation, it is often acceptable to work with a reduced set of exercise opportunities—for example change a quarterly exercise schedule to an annual one—in order to save computation time (see equation  $(18)$ ).

## References

[1] Andersen, L. & Broadie, M. (2004). A primal-dual simulation algorithm for pricing multi-dimensional American options, *Management Science* **50**, 1222–1234.

- Belomestny, D., Bender, C. & Schoenmakers, J. (2009). [2] True upper bounds for Bermudan products via nonnested Monte Carlo, Mathematical Finance, 19(1), 53-71.
- [3] Broadie, M. & Cao, M. (2008). Improved lower and upper bound algorithms for pricing American options by simulation, *Quantitative Finance* **8**, 845-861.
- [4] Broadie, M. & Glasserman, P. (1996). Estimating security price derivatives using simulation, Management Science 42, 269-285.
- [5] Broadie, M. & Glasserman, P. (1997). Pricing American-style securities using simulation, Journal of Economic Dynamics and Control 21, 1323-1352.
- [6] Broadie, M. & Glasserman, P. (2004). A stochastic mesh method for pricing high-dimensional American options, *Journal of Computational Finance* **7**, 35–72.
- [7] Chen, N. & Glasserman, P. (2007). Additive and multiplicative duals for American option pricing, Finance and Stochastics 11, 153-179.
- [8] Glasserman, P. & Yu, B. (2005). Pricing American options by simulation: regression now or regression later? in Monte Carlo and Quasi-Monte Carlo Methods, H. Niederreiter, ed, Springer Verlag.
- Haugh, M. & Kogan, L. (2004). Pricing American [9] options: a duality approach, Operations Research 52,  $258 - 270.$
- [10] Jamshidian, F. (2006). The duality of optimal exercise and domineering claims: a Doob-Meyer decomposition approach to the Snell envelope, Stochastics: an International Journal of Probability and Stochastics Processes 79. 27-60.
- [11] Kaniel, R., Tompaidis, S. & Zemlianov, A. (2008). Efficient computation of hedging parameters for discretely exercisable options, Operations Research 56, 811-826.
- [12] Karatzas, I. & Shreve, S. (1991). Brownian Motion and Stochastic Calculus, 2nd Edition, Springer Verlag.
- [13] Lamberton, D. & Lapeyre, B. (2007). Introduction to Stochastic Calculus Applied to Finance, 2nd Edition, CRC Press.
- $[14]$ Rogers, L.C.G. (2001). Monte Carlo valuation of American options, *Mathematical Finance* **12**, 271–286.

# **Related Articles**

American Options; Bermudan Options; Bermudan Swaptions and Callable Libor Exotics; Doob-Meyer Decomposition; Exercise Boundary **Optimization Methods; Finite Difference Methods** for Early Exercise Options.

LEIF B.G. ANDERSEN & MARK BROADIE
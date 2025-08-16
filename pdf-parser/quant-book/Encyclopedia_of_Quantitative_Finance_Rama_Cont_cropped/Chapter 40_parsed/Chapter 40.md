# **Skorokhod Embedding**

Analysis of a random evolution focuses initially on the behavior at a fixed deterministic, or random, time. The process and time horizon are known and we investigate the marginal law of the process. If we reverse this point of view, we face the embedding problem. We fix a probability distribution and a (wellunderstood) stochastic process and we try to design a random time such that the process at this time behaves according to the specified distribution. In other words, we know what we want to see and we ask when to look for it.

This Skorokhod embedding problem (SEP) or the Skorokhod stopping problem, first formulated and solved by A.V. Skorokhod in 1961 (English translation in 1965  $[20]$ ), is thus the problem of representing a given distribution  $\mu$  as the distribution of a given stochastic process (such as a Brownian motion) at some stopping time. It has stimulated research in probability theory for over 40 years now—the problem has been changed, generalized, or specialized in various ways. We discuss some key results in the domain, along with the applications in quantitative finance, namely to the computation of robust marketconsistent prices and hedges of exotic derivatives.

### The Skorokhod Embedding Problem

The *SEP* problem can be stated as follows:

Given a stochastic process  $(X_t : t \ge 0)$  and a probability measure  $\mu$ , find a minimal stopping time  $\tau$  such that  $X_{\tau}$  has the law  $\mu: X_{\tau} \sim \mu$ .

At first, there seems to be a trivial solution to the SEP when  $X_t = B_t$  is a Brownian motion. Write  $\Phi$ and  $F_{\mu}$  for the cumulative distribution function of the standard normal distribution and of  $\mu$ , respectively. Then  $F_{\mu}^{-1}(\Phi(B_1))$  has law  $\mu$  and hence the stopping time  $\tau = \inf\{t \ge 2 : B_t = F_{\mu}^{-1}(\Phi(B_1))\}$  satisfies  $B_{\tau} \sim \mu$ . However, this solution is intuitively "too large", in particular  $\mathbb{E}\tau = \infty$ . A meaningful solution needs to be "small". To express this, Skorokhod [20] imposed  $\mathbb{E}\tau < \infty$  and solved the problem explicitly for any centered target measure with finite variance. To avoid the restriction on the set of target measures, in general, one requires  $\tau$  to be *minimal*. Minimality of  $\tau$  signifies that if a stopping time  $\rho$  satisfies  $\rho \leq \tau$  and  $X_{\rho} \sim X_{\tau}$  then  $\rho = \tau$ . When  $\mathbb{E}B_{\tau} = 0$ , minimality of  $\tau$  is equivalent to  $(B_{t \wedge \tau} : t \ge 0)$  being a uniformly integrable martingale (see  $[6, 12]$ ) and, in consequence, when  $\mathbb{E}B_{\tau}^2 < \infty$ , it is further equivalent to  $\mathbb{E}\tau < \infty$ . Note that we can have many, in fact, infinitely many, minimal stopping times all of which embed the same distribution  $\mu$ .

We want  $\tau$  to be "small" to enable us to iterate the embedding procedure. In this way, Skorokhod [20] represented a random walk as a Brownian motion stopped at an increasing sequence of stopping times and deduced properties of the random walk from the well-understood behavior of Brownian motion. As a simple example, one can use the representation to deduce the central limit theorem from the strong law of large numbers (cf. [14, Sec. 11.2]). The ideas of embedding processes into Brownian motion were extended and finally led to the celebrated work of Monroe [13], who proved that any semimartingale is a time-changed Brownian motion.

The SEP, as stated above, does not necessarily have a solution—existence of a solution depends greatly on X and  $\mu$ . This can be seen already for realvalued diffusions [6]. However, for Brownian motion on  $\mathbb{R}$ , or any continuous local martingale  $(X_t)$  with  $\langle X \rangle_{\infty} = \infty$  a.s., there is always a solution to the SEP and there are numerous explicit constructions (typically, for the case of centered  $\mu$ ), of which we give two examples below (cf.  $[14]$ ).

### Explicit Solutions

Skorokhod [20] and Dubins [8] solved the SEP for Brownian motion and arbitrary centered<sup>a</sup> probability measure  $\mu$ . However, the search for new solutions continued and was, to a large extent, motivated by the properties of the stopping times. Researchers sought simple explicit solutions that would have additional optimal properties. Several solutions were obtained using stopping times of the form

$$\tau = \inf\{t : (A_t, B_t) \in \Gamma\}, \quad \Gamma = \Gamma(\mu) \subset \mathbb{R}^2 \quad (1)$$

which is a first hitting time for the Markov process  $(A_t, B_t)$ , where  $(A_t)$  is some auxiliary increasing process. We now give two examples.

Consider  $A_t = t$  and let  $\tau_R$  be the resulting stopping time in (1). Root [17] proved that for any centered  $\mu$  there is a *barrier*  $\Gamma = \Gamma(\mu)$  such that  $B_{\tau} \sim \mu$ , where a *barrier* is a set in  $\mathbb{R}_+ \times \mathbb{R}$ (time-space) such that if a point is in  $\Gamma$ , then all points to the right of it are also in  $\Gamma$  (see Figure 1).

![](_page_1_Figure_1.jpeg)

**Figure 1** The barrier  $\Gamma$  and Root stopping time  $\tau_R$ embedding a uniform law

Later Rost (cf. [14]) proved an analogous result replacing  $\Gamma(\mu)$  with a reversed barrier  $\tilde{\Gamma} = \tilde{\Gamma}(\mu)$ , which is a set in time-space such that if a point is in  $\Gamma$ , then all the points to the left of it are also in  $\Gamma$ . We denote  $\tilde{\tau}_R$  the first hitting of  $\tilde{\Gamma}(\mu)$ . Rost (cf. [14, 19]) proved that for any other solution  $\tau$  to the SEP and any positive convex function  $f$ , we have

$$\mathbb{E}f(\tau_R) \le \mathbb{E}f(\tau) \le \mathbb{E}f(\tilde{\tau}_R) \tag{2}$$

In financial terms, as we will see, this implies bounds on the prices of volatility derivatives. Given a measure  $\mu$ , the barrier  $\Gamma$  and the reversed barrier  $\Gamma$ are not known explicitly. However, using techniques of partial differential equations, they can be computed numerically together with the bounds in equation  $(2)$ (see [9]).

Consider now  $A_t = \overline{B}_t = \sup_{u \le t} B_u$  in equation (1). Azéma and Yor [1] proved that, for a probability measure  $\mu$  satisfying  $\int x\mu(dx) = B_0$ , the stopping time

$$\tau_{AY} = \inf\{t : \Psi_{\mu}(B_t) \le B_t\},\$$
  
where 
$$\Psi_{\mu}(x) = \frac{1}{\mu([x,\infty))} \int_{[x,\infty)} u\mu(\mathrm{d}u) \quad (3)$$

is minimal and  $B_{\tau_{AY}} \sim \mu$ . The Azéma–Yor stopping time is also optimal as it stochastically maximizes the maximum:  $\mathbb{P}(\overline{B}_{\tau} \geq \alpha) \leq \mathbb{P}(\overline{B}_{\tau_{AY}} \geq \alpha)$ , for all  $\alpha \geq 0$ and any minimal  $\tau$  with  $B_{\tau} \sim B_{\tau_{AV}}$ . Later, Perkins [16] developed a stopping time  $\tau_P$ , which, in turn, stochastically minimizes the maximum. As we will

see, these two solutions induce upper and lower bounds on the price of a one-touch option.

# Applications

## Robust Price Bounds

In the standard approach to pricing and hedging, one postulates a model for the underlying, calibrates it to the market prices of liquidly traded vanilla options (see **Call Options**), and then uses the model to derive prices and associated hedges for exotic over-thecounter products (such as Barrier Options; Lookback Options; Foreign Exchange Options). Prices and hedges will be correct only if the model describes the real world perfectly, which is not very likely. The SEP-driven approach uses the market data to deduce bounds on the prices consistent with *no-arbitrage* and the associated super-replicating strategies (see **Superhedging**), which are robust to model misspecification.

Assume absence of arbitrage (see Fundamental Theorem of Asset Pricing) and work under a risk-neutral measure (see Risk-neutral Pricing) so that the forward price process (see Forwards and **Futures**)  $(S_t : t < T)$  is a martingale. Equivalently, under a simplifying assumption of zero interest rates,  $S_t$  is simply the stock price process. We are interested in pricing an exotic option with payoff given by a path-dependent functional  $F(S)_T$ . Our main example considered below is a *one-touch* option struck at  $\alpha$ that pays 1 if the stock price reaches  $\alpha$  before maturity T:  $O^{\alpha}(S)_T = \mathbf{1}_{\overline{S}_T > \alpha}$ , where  $\overline{S}_T = \sup_{t < T} S_t$ . It follows from Monroe's theorem that  $S_t = B_{\rho_t}$ , for a Brownian motion  $(B_t)$  with  $B_0 = S_0$  and some increasing sequence of stopping times  $\rho_t : t \leq T$ (possibly relative to an enlarged filtration). We make no other assumptions about the dynamics of the underlying. Instead, we propose to investigate the restrictions induced by the market data.

Suppose, first, that we know the market prices of calls and puts (see **Call Options**) for all strikes at one maturity  $T$ . This is equivalent to knowing the distribution  $\mu$  of  $S_T$  (cf. [3]). Thus, we can see the stopping time  $\rho = \rho_T$  as a solution to the SEP for  $\mu$ . Conversely, given a solution  $\tau$  to the SEP for  $\mu$ , the process  $\tilde{S}_t = B_{\tau \wedge \frac{t}{T-t}}$  is a model for the stockprice process consistent with the observed prices of calls and puts at maturity  $T$ . In this way, we obtain

a correspondence that allows us to identify market models with solutions to the SEP and vice versa. In consequence, to estimate the fair price of the exotic option  $\mathbb{E} F(S)_T$ , it suffices to bound  $\mathbb{E} F(B)_T$ among all solutions  $\tau$  to the SEP. More precisely, if  $F(S)_T = F(B)_{\rho_T}$  a.s., then we have

$$\inf_{\tau: B_{\tau} \sim \mu} \mathbb{E} F(B)_{\tau} \le \mathbb{E} F(S)_{T} \le \sup_{\tau: B_{\tau} \sim \mu} \mathbb{E} F(B)_{\tau} \quad (4)$$

where all stopping times  $\tau$  are minimal. Consider, for example, a volatility derivative<sup>b</sup> paying  $F(S)_T =$  $f(\langle S \rangle_T)$ , for some positive convex function f, and suppose that the underlying  $(S_t)$  is continuous. Then, by Dubins-Schwarz theorem, we can take the time change  $\rho_t = \langle S \rangle_t$  so that  $f(\langle S \rangle_T) = f(\rho_T) =$  $F(B)_{\rho_T}$ . Using inequality (2), inequality (4) becomes

$$\mathbb{E}f(\tau_R) \le \mathbb{E}f(\langle S \rangle_T) \le \mathbb{E}f(\tilde{\tau}_R) \tag{5}$$

where  $B_{\tau_R} \sim S_T \sim B_{\tilde{\tau}_R}$  (cf. [9]).

When  $(S_t)$  has jumps typically one of the bounds in inequality (4) remains true and the other degenerates. In the example of a one-touch option, one sees that  $O^{\alpha}(S)_T \leq O^{\alpha}(B)_{\rho_T}$  and the fair price is always bounded above by  $\sup_{\tau} \{ \mathbb{P}(\overline{B}_{\tau} \geq \alpha) : B_{\tau} \sim$  $\mu$ . Furthermore, the supremum is attained by the Azéma-Yor construction discussed above. The best lower bound on the price in the presence of jumps is the obvious bound  $\mu([\alpha, \infty))$ . In consequence, the price of a one-touch option  $\mathbb{E} O^{\alpha}(S)_T = \mathbb{P}(\overline{S}_T \geq \alpha)$ is bounded by

$$\mu([\alpha,\infty)) \leq \mathbb{P}(\overline{S}_T \geq \alpha) \leq \mathbb{P}(\overline{B}_{\tau_{AY}} \geq \alpha)$$
$$= \mu([\Psi_{\mu}^{-1}(\alpha))) \tag{6}$$

and the lower bound can be improved to  $\mathbb{P}(\overline{B}_{\tau_P} \geq \alpha)$ under the hypothesis that  $(S_t)$  is continuous, where  $\tau_P$  is Perkins' stopping time (see [5] for detailed discussion and numerical examples). Selling a onetouch option for a lower price then the upper bound in equation (6) necessarily involves some risk. If additional modeling assumptions are made, then a lower price can be justified, but this new price is not necessarily robust to model misspecification.

The above analysis can be extended if we know more market data. For example, knowing prices of puts and calls at some earlier expiry  $T_1 < T$  would lead to solving the SEP, constrained by embedding an intermediate law  $\mu_1$  before  $\mu$ . This was achieved by Brown et al. [4] who gave an explicit construction

of an embedding that maximizes the maximum. As we have seen, in financial terms, this amounts to obtaining the least upper bound on the price of a one-touch option.

In practice, we do not observe the prices of calls and puts for all strikes but only for a finite family of strikes. As a result, the terminal law of  $S_T$  is not specified entirely and one needs to optimize among possible terminal laws (cf. [5, 10]). In general, different sets of market prices lead to embedding problems with different constraints. The resulting problems can be complex. In particular, to our best knowledge, there are no known optimal solutions to the SEP with multiple intermediate law constraints.

# Robust Hedging

Once we know the price-range for an option, we want to understand model-free super-replicating strategies (see **Superhedging**). In general, to achieve this, we need to develop a pathwise approach to the SEP. Following  $[5]$ , we treat the example of a one-touch option. We develop a super-replicating portfolio with the initial wealth equal to the upper bound displayed in equation  $(6)$ .

The key observation lies in the following simple inequality:

$$\mathbf{1}_{\overline{S}_T \ge \alpha} \le \frac{(S_T - K)^+}{\alpha - K} + \frac{S_{\varsigma \wedge T} - S_T}{\alpha - K} \mathbf{1}_{\overline{S}_T \ge \alpha} \tag{7}$$

where  $\alpha > S_0$ ,  $K$  and  $\varsigma = \inf\{t : S_t \ge \alpha\}$ . Taking expectations yields  $\mathbb{P}(\overline{S}_T \geq \alpha) \leq C(K)/(\alpha - K)$ , where  $C(K)$  denotes the price of a European call with strike K and maturity T. Taking the optimal  $K =$  $K^*$  such that  $C(K^*) = (\alpha - K^*)|C'(K^*)|$  we find  $\mathbb{P}(\overline{S}_T \geq \alpha) \leq |C'(K^*)| = \mathbb{P}(S_T \geq K^*)$ . On the other hand, using  $|C'(K)| = \mu([K, \infty))$ , where  $\mu \sim S_T$ , we have

$$C(K) = \int_{K}^{\infty} (u - K)\mu(du) = |C'(K)| \Big(\Psi_{\mu}(K) - K\Big)$$
(8)

The equation for  $K^*$  implies readily that  $K^* =$  $\Psi_{\mu}^{-1}(\alpha)$  and the bound we have derived coincides with equation  $(6)$ .

Inequality (7) encodes the super-replicating strategy. The first term of the right-hand side means we buy  $1/(\alpha - K^*)$  calls with strike  $K^*$ . The second term is a simple dynamic trading: if the price reaches level  $\alpha$ , we sell  $1/(\alpha - K^*)$  forwards on the stock. At the cost of  $C_1 = C(K^*)/(\alpha - K^*)$  we are then guaranteed to super-replicate the one-touch regardless of the dynamics of the underlying. In consequence, selling the one-touch for  $C_2 > C_1$  would be an arbitrage opportunity as we would make a riskless profit of  $C_2 - C_1$ . Finally, note that our derivation of the superhedge is pathwise and makes no assumptions about the existence (or uniqueness) of the pricing measure.

#### Other Resources

The arguments for robust pricing and hedging of lookback (see **Lookback Options**) and barrier (see **Barrier Options**) options can be found in the pioneering work of Hobson [10] and in [5]. Dupire [9] investigated volatility derivatives using the SEP.  $\text{Cox } et \text{ al.}$  [7] designed pathwise inequalities to derive price range and robust super-replicating strategies for derivatives paying a convex function of the local time (see Local Times; Corridor Variance Swap). The idea of *no-arbitrage* bounds on the prices goes back to Merton [11] (see Arbitrage Bounds). This was refined in *no-good deals* (see **Good-deal Bounds**) pricing, where one postulates that markets not only exclude arbitrage opportunities but also any *highly* desirable investments. No-good deals pricing yields tighter bounds on the prices but requires an arbitrary choice of utility function.

We refer to [14] for an extended survey of the SEP, including its history and overview of its applications. We have not discussed here the SEP for processes other than Brownian motion. Rost [18] investigated the problem for a general Markov process and has a necessary and sufficient condition on the target measure  $\mu$  for existence of an embedding. Bertoin and Le Jan [2] then developed an explicit solution, in a broad class of Markov processes, which was based on additive functionals. More recently, the approach of Vallois  $[21]$  was extended to provide explicit solutions for classes of discontinuous processes including Azéma's martingale [15].

### Acknowledgments

This research was supported by a Marie Curie Intra-European Fellowship at Imperial College London within the 6th European Community Framework Programme.

# **End Notes**

<sup>a.</sup> When modeling the stock price process, implicitly we shift both B and  $\mu$  by a constant  $S_0$ .

<sup>b.</sup>Here, written on the realized quadratic variation of the stock itself and not the log process.

# References

- Azéma, J. & Yor, M. (1979). Une solution simple au  $[1]$ problème de Skorokhod, in *Séminaire de Probabilités*. XIII, Lecture Notes in Mathematics, Springer, Berlin, Vol. 721, pp. 90-115.
- Bertoin, J. & Le Jan, Y. (1992). Representation of [2] measures by balayage from a regular recurrent point. Annals of Probability 20(1), 538-548.
- [3] Breeden, D.T. & Litzenberger, R.H. (1978). Prices of state-contingent claims implicit in option prices, The Journal of Business 51(4), 621-651.
- Brown, H., Hobson, D. & Rogers, L.C.G. (2001). The [4] maximum maximum of a martingale constrained by an intermediate law, Probability Theory and Related Fields 119(4), 558-578.
- Brown, H., Hobson, D. & Rogers, L.C.G. (2001). Robust [5] hedging of barrier options, *Mathematical Finance*  $11(3)$ ,  $285 - 314.$
- Cox, A. & Hobson, D. (2006). Skorokhod embeddings, [6] minimality and non-centered target distributions, Probability Theory and Related Fields 135(3), 395-414.
- Cox, A., Hobson, D. & Obłój, J. (2008). Pathwise [7] inequalities for local time: applications to Skorokhod embeddings and optimal stopping, Annals of Applied Probability 18(5), 1870-1896.
- [8] Dubins, L.E. (1968). On a theorem of Skorohod, The Annals of Mathematical Statistics 39, 2094-2097.
- [9] Dupire, B. (2005). Arbitrage Bounds for Volatility Derivatives as a Free Boundary Problem, http://www. math.kth.se/pde\_finance/presentations/Bruno.pdf.
- [10] Hobson, D. (1998). Robust hedging of the lookback option, Finance and Stochastics 2, 329-347.
- [11] Merton, R.C. (1973). Theory of rational option pricing, Bell Journal of Economics and Management Science 4,  $141 - 183.$
- [12] Monroe, I. (1972). On embedding right continuous martingales in Brownian motion, The Annals of Mathematical Statistics 43, 1293-1311.
- [13] Monroe, I. (1978). Processes that can be embedded in Brownian motion, The Annals of Probability  $6(1)$ ,  $42 - 56.$
- [14] Obłój, J. (2004). The Skorokhod embedding problem and its offspring, *Probability Surveys* 1, 321–392.
- [15] Obłój, J. (2007). An explicit solution to the Skorokhod embedding problem for functionals of excursions of Markov processes, Stochastic Process and their Application. 117(4), 409-431.
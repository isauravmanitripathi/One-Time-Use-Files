# **Uncertain Volatility Model**

## **Black–Scholes and Realized Volatility**

What happens when a trader uses the Black–Scholes ((BS) in the sequel) formula to dynamically hedge a call option at a given constant volatility while the realized volatility is not constant?

It is not difficult to show that the answer is the following: if the realized volatility is lower than the managing volatility, the corresponding profit and loss (P&L) will be nonnegative. Indeed, a simple, yet, clever application of Ito's formula shows us that ˆ the instantaneous P&L of being short a delta-hedged option reads

$$P \& L_t = \frac{1}{2} \Gamma S_t^2 \left[ \sigma_t^2 dt - \left( \frac{dS_t}{S_t} \right)^2 \right] \qquad (1)$$

where is the gamma of the option (the second derivative with respect to the underlying, which is positive for a call option), and *σt* the spot volatility, for example, the volatility at which the option was sold and d*St St* 2 represents the realized variance over the period [*t,t* + d*t*]. Note that this holds without any assumption on the realized volatility, which will certainly turn out to be nonconstant. This result is fundamental in practice: it allows traders to work with neither exact knowledge of the behavior of the volatility nor a more complex toolbox than the plain BS formula; an upper bound of the realized volatility is enough to grant a profit (conversely, a lower bound for option buyers). This way of handling the realized volatility with the BS formula is of historical importance in the option market. El Karoui, Jeanblanc, and Shreve have formalized it masterfully in [5].

# **Superhedging and the Uncertain Volatility Model (UVM)**

## *The UVM Framework*

Assume that you perform the previous strategy. You are certainly not alone in the market, and you wish you have the lowest possible selling price compatible with your risk aversion. In practice, on the derivatives desk (this is a big difference with the insurance world where the risk is distributed among a large enough number of buyers), the risk aversion is total, meaning that your managing policy will aim at yielding a nonnegative P&L whatever the realized path. This approach is what is called the superhedging strategy (or superstrategy) approach to derivative pricing. Of course, the larger the set of the underlying scenarios (or paths) for which you want to have the superhedging property (*see* **Superhedging**), the higher the initial selling price. The first set that comes to mind is the set of paths associated with an unknown volatility, say between two boundary values *σ*min and *σ*max. In other words, we look for the cheapest price at which we can sell and manage an option without any assumption on the volatility except that it lies in the [*σ*min*, σ*max] range. This framework is the uncertain volatility model (UVM) introduced by Avellaneda *et al.* [2].

If you take a call option (or more generally a European option with convex payoff), the BS price at volatility *σ*max is a good candidate. Indeed, it yields a superhedging strategy by result (1). And should the realized volatility be constantly *σ*max, then your P&L will be 0. It is easy to conclude from this that the BS *σ*max price is the UVM selling price for an option with a convex payoff.

Now very often traders use strategies (butterflies, callspreads, etc.) which are not convex any longer. It is not at all easy to find a superstrategy in such cases. There is one exception; if you hedge at the selling time and do not rebalance your hedge before maturity, the cheapest price associated to such a strategy will be the value at the initial underlying value of the concave envelope of the payoff function. It is easy to see that this value corresponds to the total uncertainty case, or to the [0*,*∞] case in the UVM model. For a call option it will be the value of the underlying.

## *Black–Scholes–Barenblatt Equation*

There come into play the seminal work [2] and independently [7]: Going back to equation (1), we are looking for a model with the property that the managing volatility is *σ*min when the gamma is nonnegative, and *σ*max in the converse situation. Should such a model exist, it will yield an optimal solution to the superhedging problem.

An easy way to approximate the optimal solution is to consider a tree (a trinomial tree, for instance) where the dependence upon the volatility lies in the node probabilities and not in the tree grid. In the classical backward pricing scheme one can then choose the managing volatility according to the local convexity (since it is a trinomial tree, each node has three offshoot and so a convexity information) of the immediately forward price. Of course, it is not the convexity of the current price since we are calculating it, but the related error of replacing the current convexity by the forward one will certainly go to zero when the time step goes to zero.

The related continuous-time object is the Black-Scholes partial differential equation (PDE) where the second-order term is replaced by the following nonlinear one

$$\frac{1}{2}S_t^2\left(\sigma_{\max}^2\Gamma^+-\sigma_{\min}^2\Gamma^-\right)$$

where, as usual,  $x^+$  and  $x^-$  denote the positive and negative parts. This PDE has been named Black-Scholes-Barenblatt since it looks like the Barenblatt PDE occurring in porosity theory. More precisely, in case of no arbitrage, assume that the stock price dynamics satisfy  $dS_t = S_t (r dt + \sigma_t dW_t)$ , where  $W_t$  is a standard Brownian motion and r is the risk-free interest rate. This is valid under the class  $\mathcal{P}$  of all the probability measures such that  $\sigma_{\min} \leq$  $\sigma_t \leq \sigma_{\text{max}}$ . Let  $\Pi_t$  denote the value of a derivative at time t written on  $S_t$  with maturity T and final payoff  $\Phi(S_T)$ ; then at any time  $0 < t < T$ , we must have  $W^-(t, S_t) \leq \Pi_t \leq W^+(t, S_t)$  where

$$W^{-}(t, S_{t}) = \inf_{P \in \mathcal{P}} \mathbb{E}_{t}^{P} \left[ e^{-r(T-t)} \Phi(S_{T}) \right]$$
  
$$W^{+}(t, S_{t}) = \sup_{P \in \mathcal{P}} \mathbb{E}_{t}^{P} \left[ e^{-r(T-t)} \Phi(S_{T}) \right] \qquad (2)$$

The two bounds satisfy the following nonlinear PDE, called the *Black–Scholes–Barenblatt equation* (which reduces to the classical BS one in the case  $\sigma_{\min} = \sigma_t = \sigma_{\max}$ ):

$$\frac{\partial W^{\pm}}{\partial t} + r \left( \frac{\partial W^{\pm}}{\partial S} S - W^{\pm} \right) + \frac{1}{2} \Sigma \left( \frac{\partial^2 W^{\pm}}{\partial S^2} \right) S^2 \frac{\partial^2 W^{\pm}}{\partial S^2} = 0 \qquad (3)$$

with the terminal condition

$$W^{\pm}(S,T) = \Phi(S_T) \tag{4}$$

where

$$\Sigma \left( \frac{\partial^2 W^+}{\partial S^2} \right) = \begin{cases} \sigma_{\text{max}}^2 & \text{if } \frac{\partial^2 W^+}{\partial S^2} \ge 0\\ \sigma_{\text{min}}^2 & \text{if } \frac{\partial^2 W^+}{\partial S^2} < 0 \end{cases} \tag{5}$$

and

$$\Sigma \left( \frac{\partial^2 W^-}{\partial S^2} \right) = \begin{cases} \sigma_{\text{max}}^2 & \text{if } \frac{\partial^2 W^-}{\partial S^2} \le 0\\ \sigma_{\text{min}}^2 & \text{if } \frac{\partial^2 W^-}{\partial S^2} > 0 \end{cases} \tag{6}$$

Observe that in case  $\Phi$  is convex, the BS price at volatility  $\sigma_{\text{max}}$  is convex for any time t, so that it solves the Black-Scholes-Barenblatt equation. Conversely, if  $\Phi$  is concave, so is its BS price at volatility  $\sigma_{\text{max}}$  for any time *t*, which yields the unique solution to the Black-Scholes-Barenblatt equation.

#### Superstrategies and Stochastic Control

Note that this PDE is also a classical Hamilton-Jacobi-Bellman equation occurring in stochastic control theory. Indeed a related object of interest is the supremum of the risk-neutral prices over all the dynamics of volatility that satisfy the range property:

$$\sup_{P\in\mathcal{P}}\mathbb{E}^P f$$

where  $\mathcal{P}$  is the set of risk-neutral probabilities, each of which corresponds to a volatility process with value at each time in  $[\sigma_{\min}, \sigma_{\max}]$ . In fact, such an object is not that easy to define in the classical probabilistic modeling framework, since two different volatility processes will typically yield mutually singular probability measures on the set of possible paths. A convenient framework is the stochastic control framework. In such a framework, the managing volatility being interpreted as a control, one tries to optimize a given expectation—the riskneutral price in this case. It turns out that stochastic optimal control will yield the optimal superstrategy price.

Nevertheless, the connection between the superstrategy problem and stochastic control is not that obvious, and these need to be spelled out carefully in this respect. Recall that the stochastic control problem is the maximization of an expectation over a set of processes, whereas the superstrategy problem is the almost sure domination of the option payoff at maturity by a hedging strategy.

Note that even in the UVM case, there are still plenty of open questions. In fact, a neat formulation of the superhedging problem is not a piece of cake. The issue is avoided in [2], handled partially in [7], and more formally in [8], where the model uncertainty is specified as a set of martingale probabilities on the canonical space, and also in [6]. Once this is done, a natural theoretical problem, given such a "model set", is to find out a formula for the cheapest superhedging price. The supremum of the risk-neutral prices over all the probabilities of the set will in general be strictly smaller than the cheapest price, even if they match in the UVM setting. The precise property of the "model set" that makes this equality remains to be clarified. Some partial results in this direction, with progresses towards a general theorem, are available in [4], where the case of path-dependent payoffs in the UVM framework is also solved.

#### Lagrangian UVM

In practice, the UVM approach is easy to implement for standard options by using the tree scheme described above, for example. It can be extended in the same way for path-dependent options. Nevertheless, when the price pops up, the usual reaction of the trader or risk officer is that the price is too high, especially too high to explain the observed market price.

The fact that the price is high is a direct consequence of the total aversion approach in the superstrategy formulation, and also of the fact that the price corresponds to the worst-case scenario where the gamma changes signs exactly when the volatility switches regimes. This is a highly unlikely situation. To lower the price and fit in the traditional setting where one wants to fit the observed market price of liquid European calls and puts (so-called vanillas), Avellaneda, Levy, and Paras propose a constrained extension of the UVM model where the price of the complex products of the trader is handled within the UVM framework with the additional constraint of fitting the vanilla prices. By duality, this reduces to computing the UVM price for a portfolio parameterized by a Lagrangian multiplier and then minimizing the dual value function over the Lagrangian parameter. Mathematically speaking, let us consider an asset  $S_t$  and a payoff  $\Phi(S_T)$ . *m* European options with

payoffs  $F_1(S_{T_1}), \ldots, F_m(S_{T_m})$  with maybe different strikes and maturities are available for hedging; let  $f_1,\ldots,f_m$  be their respective market prices at the time of the valuation  $t \leq \min(T, T_1, \ldots, T_m)$ . Consider now an agent who buys quantities  $\lambda_1, \ldots, \lambda_m$ of each option. His total cost of hedging then reads

$$\Pi(t, S_t, \lambda_1, \dots, \lambda_m)\n$$

$$\n= \sup_{P \in \mathcal{P}} \left\{ e^{-r(T-t)} \Phi(S_T) - \sum_{i=1}^m \lambda_i e^{-r(T_i-t)} F_i(S_{T_i}) \right\}\n$$

$$\n+ \sum_{i=1}^m \lambda_i f_i \tag{7}$$

where the supremum (sup) is calculated within the UVM framework as presented above, and we must specify a range  $\Lambda_i^+ \leq \lambda_i \leq \Lambda_i^-$  ( $\Lambda_i^{\pm}$  represent the quantities available on the market). The optimal hedge is then defined as the solution to the problem

$$\Pi^*(t, S_t) = \inf_{\lambda_1, \dots, \lambda_m} \Pi(t, S_t, \lambda_1, \dots, \lambda_m) \quad (8)$$

In fact, the first-order conditions read  $\frac{\partial \Pi}{\partial \lambda_i} = \sum_{i=1}^{m} f_i - \mathbb{E}^{P^*} \left( e^{-r(T_i - t)} F_i \left( S_{T_i} \right) \right) = 0$ , where  $P^*$  realizes the sup above. These conditions exactly fit the model to observed market prices. The convexity of  $\Pi(t, S_t, \lambda_1,$  $\ldots, \lambda_m$ ) with respect to  $\lambda_i$  ensures that if a minimum exists, then it is unique.

This approach is very attractive from a theoretical point of view, but it is much harder to implement. The consistency of observed vanilla prices is a crucial step that is rarely met in practice. Even if numerous robust algorithms exist to handle the dual problem, their implementation is quite tricky. In fact, this constrained formulation implies a calibration property of the model, and the design of a stable and robust calibration algorithm is one of the greatest challenges in the field of financial derivatives.

#### The Curse of Nonlinearity

Another issue for a practitioner is the inherent nonlinearity of the UVM formulation. Most traditional models like BS, Heston, or Lévy-based models are linear models. The fact that an option price should depend on the whole portfolio of the trader is a nobrainer for risk officers, but this nonlinearity is a challenge for the modularity and the flexibility of pricing systems. This is very often a no-go feature in practice.

The complexity of evaluating a portfolio in the UVM framework is real, as studied thoroughly by Avellaneda and Buff in [1]. Following [1], let us consider a portfolio with  $n$  options with payoffs  $f_1, \ldots, f_n$  and maturities  $t_1, \ldots, t_n$ . The computational problem becomes tricky when the portfolio consists of barrier options. Indeed, this means that, at any time step, the portfolio we are trying to value might be different (in case the stock price has reached the barrier of any option) from the one at the previous time step. Because of the nonlinearity, a PDE specific to this portfolio has to be solved in this case. Avellaneda and Buff [1] addressed this very issue: a naive implementation would require solving the  $2^n - 1$  nonlinear PDEs, each representing a subportfolio. They provide an algorithm to build the minimal number  $N_n$  of subportfolios (i.e., of nonlinear PDEs to solve) and show the following:

- If the initial portfolio consists of barrier (single or double) and vanilla options, then  $N_n \leq \frac{n(n+1)}{2}$
- If the initial portfolio only consists of single barrier options ( $n_u$  up-and-out ones and  $n_d$  =  $n - n_u$  down-and-out ones), then  $N_n = n_d +$  $n_u + n_d n_u$ . This assumes that all the barriers are different. If some are identical, then the number of required computations decreases.

Numerically speaking, the finite-difference pricing is done on a lattice, matching almost exactly all the barriers. Nevertheless in [3], an optimal construction of the lattice to solve the PDEs is provided.

## References

- [1] Avellaneda, M. & Buff, R. (1999). Combinatorial implications of nonlinear uncertain volatility models: the case of barrier options, Applied Mathematical Finance 1,  $1 - 18$
- [2] Avellaneda, M., Levy, A. & Paras, A. (1995). Pricing and hedging derivative securities in markets with uncertain volatilities, Applied Mathematical Finance 2, 73-88.
- [3] Avellaneda, M. & Paras, A. (1996). Managing the volatility risk of portfolios of derivative securities: the Lagrangian uncertain volatility model, Applied Mathematical Finance 3, 21-52.
- [4] Denis, L. & Martini, C. (2006). A theoretical framework for the pricing of contingent claims in the presence of model uncertainty, Annals of Applied Probability 16(2),  $827 - 852$
- [5] El Karoui, N., Jeanblanc, M. & Shreve, S. (1998). Robustness of the Black and Scholes formula, Mathematical Finance 8(2), 92-126.
- [6] Frey, R. (2000). Superreplication in stochastic volatility models and optimal stopping, Finance and Stochastics  $4(2), 161-187.$
- [7] Lyons, T.J. (1995). Uncertain volatility and the risk-free synthesis of derivatives, Applied Mathematical Finance 2, 117-133.
- [8] Martini, C. (1997). Superreplications and stochastic control, IIIrd Italian Conference on Mathematical Finance, Trento.

# **Related Articles**

Black-Scholes Formula; Models; Stochastic Control.

CLAUDE MARTINI & ANTOINE JACQUIER
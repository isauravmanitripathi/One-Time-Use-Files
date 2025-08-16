# **Static Hedging**

Liquid traded put and call options can be used as hedge instruments for over-the-counter traded products. Barrier options are the most common exotic options, and, for these contracts, static hedging works out particularly well. In the Black–Scholes model there are simple methods (conceptually straightforward and/or closed form) for constructing replicating portfolios that do not require dynamic trading; they are set up at initiation of the barrier option, and liquidated at either knockout or expiry. They are, thus, static hedges. Inspired by Allen and Padovani [1], we describe how to find static hedges for barrier options in the Black–Scholes model in a way that encompasses both Derman's [6] intuitive calendar-spread algorithm and Carr's [4] strike-spread hedges stemming from put–call symmetry.

## **Construction of Static Hedges**

Unless we explicitly say otherwise, we consider a Black–Scholes model throughout this article. This means that the interest rate is constant, and all options are written on some underlying asset *S* that follows a geometric Brownian motion. A zero-rebate, knockout barrier option is a contract that pays off as a plain vanilla option if *S* stays within a specified barrier for the whole life of the barrier option, but becomes worthless if the barrier is hit or crossed (*see also* **Barrier Options**). Recurrent examples are the downand-out call and the up-and-out call The value of a still-alive barrier option is of the form *F (St,t)*, where the function *F* solves the Black–Scholes partial differential equation with 0 as boundary condition along the barrier (*see* **Finite Difference Methods for Barrier Options**). This is illustrated in Figure 1, which is useful to keep in mind when the method for constructing static hedges is described in the following.

#### *Construction of Static Hedges*

A portfolio of puts and calls that (approximately) replicates the barrier option can be found as the solution to a linear system of equations, and constructing it does not require knowledge/implementation of barrier option valuation formulas. The idea is to match the barrier option's value at expiry and along the barrier.

To illustrate, consider a down-and-out call with strike *K*, expiry *T*, and barrier *B*. (An up-and-out call is treated similarly, except strike-above-the-barrier calls are used as hedge instruments.) Let *Put*, *Call* (spot, time | strike, expiry) denote put and call values.

Suppose that we have specified a grid of time points 0 = *t*<sup>0</sup> *< t*<sup>1</sup> *<...<tn* = *T* , and *n* pairs of put with strikes *Kj* ≤ *B* and expiries *Tj* ≤ *T* . Find the solution *α* to

$$A\alpha + u = 0 \tag{1}$$

where *A* is an *n* × *n* matrix with entries *Ai,j* = *P ut (B, ti*|*Kj , Tj )* and *u* is an *n*-vector with entries *Call(B, ti*|*K, T )*. A portfolio with the *(K, T )*-call and *αj* in the *(Kj , Tj )*-put then matches the barrier option's zero value at the *ti*-points along the barrier, and its expiry payoff above the barrier. So the barrier option is—to a good approximation when the match points, the *ti*'s, are close —replicated buying this portfolio at time 0 and selling it either when the barrier option is knocked out (because sample paths are continuous, this can only happen if the barrier is actually hit) or when it expires. In other words, this represents a static hedge. There is freedom of choice regarding strikes and expiries of the hedge instruments. Derman [6] suggests calendarspread hedging with strikes along the barrier,that is, using *Tj* = *tj*<sup>−</sup><sup>1</sup> and *Kj* = *B*. This makes the *A*matrix triangular so that we can solve for *αj* 's in one easy-to-explain backward-working pass. Another choice—closely related to Carr's work [4]—is to use strike spreads, that is, *Tj* = *T* for all *j* and *Kj* 's that are different and below the barrier.

**Example 1.** Table 1 gives a numerical comparison of the performance of different hedge portfolios for three-month barrier options; a typical lifetime of a barrier option in foreign exchange markets. Looking at the results in Table 1 for the down-and-out call, we see the appeal of using options as hedge instruments; very few options are needed in the static hedges to achieve a hedge quality that is several orders of magnitude better than usual dynamic *-*-hedging. The numbers for the up-and-out call demonstrate one problem that static hedging does not immediately solve: the up-and-out call is a *reverse* or *live-out* option meaning that the underlying call is in the money when the barrier option knocks out. This

![](_page_1_Figure_1.jpeg)

**Figure 1** The PDEs for (a) down-and-out and (b) up-and-out call options

Table 1 Performance of dynamic and static hedge strategies in the Black-Scholes with 15% volatility and zero interest rate and dividends. The columns show the initial price of the hedge portfolio and the standard deviation of the benchmarked discounted hedge error, that is, the value of hedge portfolio at liquidation minus barrier option payoff relative to the initial value of the barrier option. All static hedges use three options besides the  $(K, T)$ -call. The time points for value matching, the  $t_i$ s, and the expiries for the calendar spreads are from the list (0, 1/12, 2/12, 3/12). The strike spreads use calls with strikes (110,112,114) for the up-and-out case, and puts with strikes ( $90.25_{=B^2/K}$ ,  $88.25$ ,  $86.25$ ) for the down-and out case. The  $\Delta$ -hedge is adjusted daily and all portfolios are continuously monitored

| Hedge method                                                            | Barrier option type                             |                        |                                                |                        |
|-------------------------------------------------------------------------|-------------------------------------------------|------------------------|------------------------------------------------|------------------------|
|                                                                         | Down-and-out call<br>$K = 100, T = 1/4, B = 95$ |                        | Up-and-out call<br>$K = 100, T = 1/4, B = 110$ |                        |
|                                                                         | Cost                                            | Standard deviation (%) | Cost                                           | Standard deviation (%) |
| Dynamic; $\Delta$<br>Static; strike spreads<br>Static; calendar spreads | 2.6964<br>2.6964<br>2.6704                      | 1.0                    | 1.0358<br>1.0674<br>1.3468                     | 81<br>19<br>94         |

discontinuity creates a large gap risk, and hedge quality deteriorates. To alleviate this, a number of regularization techniques have been suggested, for instance [10] using singular value decomposition when solving equation  $(1)$ .

### Beyond Black-Scholes Dynamics

Constructing static hedges by solving linear equations like equation (1) goes well beyond the Black–Scholes model. For constant elasticity of variance (asset volatility  $\sigma S_t^{\gamma-1}$ ) and local volatility (asset volatility of the form  $\sigma(S_t, t)$  models, the system carries over verbatim; the entries of the A-matrix are just calculated with a different formula/method. For jumpdiffusion models [2], one needs to extend the grid of match points to space points beyond the barrier, and for stochastic volatility models [8], an extra

dimension is needed to match different volatility levels at knockout. By using both strike and calendar spreads, asymptotically perfect static hedges can be found in these two cases. It should be stressed that the static hedges are model and parameter dependent, but experimental and empirical evidence  $[7, 9]$  suggests a high degree of robustness to model risk.

### **Put–Call Symmetry and Static Hedges**

In a number of papers  $[3-5]$ , Peter Carr and coauthors have derived put-call symmetries and shown how they can be used to create static hedges for barrier options. In its basic form [4] [page 1167], the put-call symmetry states that in the zero-dividend, zero-interest rate Black-Scholes model, we have

$$Call(S_t, t|K, T) = (K/S_t) \times Put(S_t, t|S_t^2/K, T)$$

for all 
$$S_t$$
,  $t$ ,  $K$ , and  $T$  (2)

So a down-and-out call is replicated by buying one strike-*K* call, selling *K/B* puts with strike *B*<sup>2</sup>*/K*, liquidating this position the first time that *St* = *B* , and if that does not happen, holding it until the options expire. More general symmetry relations enable one to find static hedges for such contracts as up-andout calls, barrier options with rebates, lookback options, and double barrier options ([11] is a survey). Those static hedges will typically involve a continuum of plain vanilla options. Put–call symmetries also exist in models with nonzero interest rates and dividends, and more general dynamics than geometric Brownian motion (see [5]). Note that the strikespread approach from the previous section finds the symmetry-based static hedges without explicit knowledge of closed-form results, and that the perfect replication of the down-and-out call in Table 1—where the strike-*B*<sup>2</sup>*/K* put is included as a hedge instrument—demonstrates the basic put–call symmetry.

## **References**

- [1] Allen, S. & Padovani, O. (2002). Risk management using quasi-static hedging, *Economic Notes* **31**, 277–336.
- [2] Andersen, L., Andreasen, J. & Eliezer, D. (2002). Static replication of barrier options: some general results, *Journal of Computational Finance* **5**, 1–25.

- [3] Bowie, J. & Carr, P. (1994). Static simplicity, *Risk Magazine* **7**(8), 44–50.
- [4] Carr, P., Ellis, K. & Gupta, V. (1998). Static hedging of exotic options, *Journal of Finance* **53**, 1165–1190.
- [5] Carr, P. & Lee, R. (2008). Put-call symmetry: extensions and applications, *Mathematical Finance* forthcoming.
- [6] Derman, E., Ergener, D. & Kani, I. (1995). Static options replication, *Journal of Derivatives* **2**, 78–95.
- [7] Engelmann, B., Fengler, M., Nalholm, M. & Schwendner, P. (2007). Static versus dynamic hedges: an empirical comparison for barrier options, *Review of Derivatives Research* **9**, 239–264.
- [8] Fink, J. (2003). An examination of the effectiveness of static hedging in the presence of stochastic volatility, *Journal of Futures Markets* **23**, 859–890.
- [9] Nalholm, M. & Poulsen, R. (2006). Static hedging and model risk for barrier options, *Journal of Futures Markets* **26**, 449–463.
- [10] Nalholm, M. & Poulsen, R. (2006). Static hedging of barrier options under general asset dynamics: unification and application, *Journal of Derivatives* **13**, 46–60.
- [11] Poulsen, R. (2006). Barrier options and their static hedges: simple derivations and extensions, *Quantitative Finance* **6**, 327–335.

## **Related Articles**

**Barrier Options**; **Finite Difference Methods for Barrier Options**; **Hedging**; **Put–Call Parity**;

ROLF POULSEN
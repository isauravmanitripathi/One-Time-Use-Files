# **Arbitrage Bounds**

A key question in option pricing concerns how to incorporate information about the prices of existing, liquidly traded options into the prices of exotic options. In the classical **Black–Scholes model**, where there is only one parameter to choose, this question becomes: what do existing prices tell us about the volatility? Since the Black–Scholes model lacks the flexibility to capture all the market information, a wide variety of pricing models have been proposed. Rather than specifying a model and pricing with respect to this model, an alternative approach is to construct model-free *arbitrage* bounds on the price of exotic options. Arbitrage bounds are constraints on the price of an option, due to the absence of **arbitrage strategies**. These strategies are typically derived from relationships between the payoff of an option, and the payoff of a simple trading strategy constructed from other related derivatives—for example, the strategy might be a buy-and-hold strategy. If such a simple trading strategy can be shown to be worth at least as much as the corresponding option at maturity in every possible outcome, then the initial cost of the trading strategy must be more than the cost of the option, or else there exists a simple arbitrage. An important feature of these bounds is that they are often valid for a very wide class of models.

## **Arbitrage Bounds for Call Prices**

Perhaps the earliest and simplest example of arbitrage bounds are the following inequalities, which are described in the seminal paper [29]:

$$\max \{0, S_0 - B(T)K\} \le C(K, T) \le S_0 \tag{1}$$

where *C(K, T )* is the time-0 price of a *European call* option on the asset *(St)t*<sup>≥</sup><sup>0</sup> with strike *K* and maturity *T* , and *B(T )* is the time-0 price of a bond that is worth \$1 at time *T* . These bounds can be derived from the following simple arbitrages:

1. Suppose *C(K, T ) > S*0. Then we can construct an arbitrage by selling the call option and buying the asset. We receive an initial positive cash flow, while at maturity the option is worth *(ST* − *K)*+, which is less than *ST* , the value of the asset we hold.

2. Suppose *C(K, T ) < S*<sup>0</sup> − *B(T )K*. Then we can construct an arbitrage by buying the call option with strike *K*, selling short the asset, and buying *K* units of the bond that pays \$1 at time *T* . At time 0, we receive the cash amount

$$S_0 - B(T)K - C(K,T) \tag{2}$$

which, by assumption, is strictly positive. At maturity, writing *x*<sup>+</sup> = max{*x,* 0}, we hold a portfolio whose value is

$$(S_T - K)_+ - (S_T - K) \tag{3}$$

which is positive.

3. Finally, it is clear that the call option must have a positive value (i.e., *C(T , K)* ≥ 0), but this can also be considered a consequence of the arbitrage strategy of "buying" the derivative (for a negative price), and hence receiving positive cash flows both initially and at maturity.

There are some key features of the above example that are repeated in other similar applications. Note, first of all, that the inequalities make no modeling assumptions—the final value of the arbitrage portfolios will be larger/smaller than the call option for any final value of the asset, so these bounds are truly independent of any model for the underlying asset. Secondly, the bounds are the best we can do in the following sense: it can be shown that there are arbitrage-free models for the asset price under which the bounds are tight. For example, if the interest rates are deterministic, and the asset price satisfies *St* = *S*0*B(t)*, then the lower bounds hold for all strikes, and there is no arbitrage in the market. Alternatively, the upper and lower bounds can be shown to be the Black–Scholes price of an option in the limit as *σ* → ∞ and *σ* → 0, respectively.

In practice, these bounds are far too wide for most practical purposes, although they can be useful as a check that a pricing algorithm is producing sensible numerical results. Part of the reason for this wide range of values concerns the relatively small amount of information that is being used in deriving the bound. In general, one would expect to have some information about the behavior of the market. A natural place to look for further information is in the market prices of other vanilla options: in model-specific pricing, this information is commonly used for calibration of the model. However, the information contained in these prices can also be used to provide arbitrage bounds on the prices of other exotic derivatives through the formulation of appropriate portfolios.

### Breeden–Litzenberger Formula

One of the initial works to consider the pricing implications of vanilla options on exotic options is [6]. Here, the authors suppose that the value of calls at all strikes and a given maturity are known, and observe that

$$p(x) = \frac{1}{B(T)} \frac{\partial^2 C(K,T)}{\partial K^2} \bigg|_{K=x} \tag{4}$$

can be thought of as the density of a random variable. The value at time-0 of an option whose payoff is only  $\mathbf{v}$ a function of the terminal value of the asset,  $f(S_T)$ , can then be shown to be

$$B(T) \int f(x) p(x) \, \mathrm{d}x \tag{5}$$

or, intuitively, the discounted expectation under the density implied by the call prices. We can see this by noting that (at least for twice-differentiable functions  $f$ ), we have

$$f(S) = f(0) + Sf'(0) + \int_0^\infty f''(K)(S - K)_+ \, \mathrm{d}K \tag{6}$$

and therefore may replicate the contract  $f(S)$  exactly by holding  $f(0)$  in cash, buying  $f'(0)$  units of the asset, and "holding" a continuous portfolio of calls consisting of  $f''(K) dK$  units of call options with strikes in  $[K, K + dK]$ . Since this portfolio replicates the exotic option exactly, by an arbitrage argument, the prices must agree. The price of the portfolio of calls can be shown to be equation (5). In practice, some discrete approximation of such a portfolio is necessary, and this is generally possible provided the calls trade at a suitably large range of strikes.

One of the interesting consequences of this result is that we have a representation for the price of the exotic option as a discounted expectation. A key result in modern mathematical finance is the fundamental theorem of asset pricing, which allows us to deduce from the assumption of no arbitrage

that the price of an option may be written as a discounted expectation under a suitable probability measure. However, an assumption of the fundamental theorem of asset pricing is that there is a (known) model for the underlying asset. In the situation we wish to consider, there is no such measure. It is therefore not immediate that we can say anything about any probabilistic structure that might help us. One of the interesting consequences of this result is that it does provide some information about the underlying probabilistic structure: namely, that the call prices "imply" a risk-neutral distribution for the asset price. and that there are arbitrage relationships that ensure that any other option whose payoff depends only on the final value of the asset also has the price implied by this probability measure.

#### **Arbitrage Bounds for Exotic Options**

A general approach that is implied by the above examples is the following: suppose we know the prices of (and can trade in) a set of "vanilla" derivatives. Consider also an exotic option, for example, a **barrier option**. Without making any (strong) assumptions about a model for the underlying asset, what does arbitrage imply about the price of the barrier option? Through a suitable set of trades in the underlying and vanilla options, we should be able to construct portfolios and self-financing trading strategies that either dominate, or are dominated by, the payoff of the exotic option. If we can find a portfolio that dominates the exotic option, then the initial cost of this portfolio (which is known) must be at least as much as the price of the exotic option, or else there will be an arbitrage from buying the portfolio and selling the exotic option. The price of this portfolio therefore provides an upper bound on the price of the option. In a similar manner, we may also find a lower bound for the price of the option by looking for portfolios and trading strategies in the underlying and vanilla options that result in a terminal value that is always dominated by the exotic option. Note that we are, in general, interested in the least upper bound and also the greatest lower bound that can be attained, since these will give the tightest possible bounds.

We have been vague about two concepts here: first, we said that we would not want to make any "strong" assumptions about the model of the underlying asset. The exact assumptions that different examples make about the underlying models vary from case to case, but typically we might assume, perhaps, that the underlying asset price is continuous (or at least, that it continuously crosses a barrier), or that the price process satisfies some symmetry assumption. Secondly, we have not specified what types of trading strategies we wish to consider: this is because, in part, this depends heavily on the assumptions on the price process—for example, trading strategies that involve a trade when the asset first crosses a barrier often assume that the underlying crosses the barrier continuously; the assumption on the symmetry of the asset price results in identities connecting the prices of call and put options. However, the important point to note here is that we work typically in a class of price processes that are too large to be able to hedge dynamically in any meaningful way, so that continuously rebalancing the portfolio is not an option. Two important classes of strategies are static strategies, which involve purchasing an initial portfolio of the underlying and vanilla options, and holding this to maturity (see Static Hedging), and *semistatic* strategies, which involve a fixed position in the options, and some trading in the underlying asset, often at hitting times of certain levels or sets.

### **Consistency of Vanilla Options**

Since we are looking for arbitrage in the market when we add an exotic option, it is important that the initial prices of the vanilla options do include an arbitrage. In the case of equity markets, where the underlying vanilla options are call options, written on a given set of strikes and maturities, this is a question that has been studied by a number of authors [9, 11, 13, 15, 18]. The fundamental conclusion that may be arrived at from all these works is the following: the prices of calls are arbitrage free if and only if there exists a model under which the prices agree with the discounted expectation under the model. Moreover, the existence of the model has a relatively straightforward characterization in terms of the properties of the call prices, so that for a given set of call prices, the conditions may be checked with relative ease. Moreover, some practical concerns can be included in the models: [15] allows the inclusion of default of the asset, while [18] also allows for the inclusion of dividends.

Of course, not all markets fit naturally into this framework, and so other settings should also be considered, as, for example, in [27], where arbitrage bounds for fixed income markets are considered.

#### **Barrier Options**

One of the simplest classes of options that can be considered are the various types of barrier options. and one of the simplest of these options is the one*touch* barrier option: this is an option that pays \$1 at maturity if the barrier is breached during the lifetime of the contract, and expires worthless if the barrier is not hit before maturity. Suppose that the price process is continuous, and suppose further that the riskless interest rate is zero. Then [7] provides an upper bound on the price of the option,  $OT(R, T)$ , where R is the level of the barrier,  $R > S_0$ , and T is the maturity of the option. The bound that is derived in  $[7]$  is

$$OT(R,T) \le \inf_{x \le R} \frac{C(x,T)}{R-x} \tag{7}$$

The bound can be most clearly seen by noting the corresponding arbitrage strategy: suppose that the bound does not hold, then we can find an  $x$  for which

$$OT(R,T) > \frac{C(x,T)}{R-x} \tag{8}$$

We sell the one-touch option, and buy  $\frac{1}{R-x}$  units<br>of the call with strike x and maturity T. If the barrier at  $R$  is not hit, the one-touch option expires worthless, and our call option may have positive value. Alternatively, suppose that at some time, the barrier is hit. At this time, we enter into a forward contract on the asset. Specifically, we sell  $\frac{1}{R-x}$  units of a forward struck at  $R$ . Since the current value of the asset is  $R$ , and we have assumed that the interest rates are zero, we may enter into such a contract for free. At maturity, the value of our position in the forward will be  $\frac{R-Sr}{R-x}$ , and the total value of our position in the call and the forward is

$$\frac{1}{R-x}(S_T - x)_+ + \frac{R - S_T}{R-x} = \frac{1}{R-x}$$
$$\times \left[ (S_T - x) + (x - S_T)_+ + (R - S_T) \right]$$
$$= -1 + \frac{(x - S_T)_+}{R-x} \tag{9}$$

where we write *x*<sup>+</sup> = max {*x,* 0}. Since the value of the portfolio is now greater than the value of the one-touch option, we have an arbitrage.

It can also be shown that the bound here is the best that can be attained: specifically, it can be shown that there exists a model under which there is equality in the identity (7). By considering the form of the hedge, we can also say something about the extremal model. For equality to be there in equation (7), we must always have equality between the payoff of the one-touch option, and the value of the hedging portfolio. The case where the barrier is not hit requires that

$$0 = \frac{(S_T - x)_+}{R - x} \tag{10}$$

or, equivalently, that *ST* is always below *x*. The case where the barrier is struck requires that

$$1 = 1 + \frac{(x - S_T)_+}{R - x} \tag{11}$$

or that *ST* is always above *x*. In other words, in the extremal model, the paths that hit the barrier will, at maturity, finish above the minimizing value of *x*, while those that do not hit the barrier will always end up below *x*.

A similar approach allows us to find a lower bound. In this case, the hedging portfolio consists of a digital call struck at the barrier, so that the payoff of this option is simply \$1 if the asset ends up above the barrier, and put options are struck at the barrier, at some *y<R*. Note that the digital call can, in theory at least, be arbitrarily closely approximated by buying a suitably large number of calls just below the strike, and selling the same number of calls at the strike, so that we can deduce the price of the digital call from the prices of the vanilla call options. The prices of the puts can be deduced from **put–call parity**. In a manner similar to the above, we can find the "best" bound by finding the value of *y* that corresponds to the most expensive portfolio. Again, the bound is tight, in the sense that there exists a model under which we attain equality. We can also describe the behavior in this model: the paths that hit the barrier will end up either below *y* or above *R*. Those that do not hit the barrier will finish between *y* and *R*.

Using extensions of these ideas, similar bounds can be found for other common barrier options, for example, down-and-in calls. Full details can be found in [7].

There are a number of observations that we can make about the solution to the above problem, and which extend more generally. First, the extension to nonzero interest rates is nontrivial—one of the assumptions that was made in constructing the trading strategy was that, when the barrier is struck, we would be able to enter into a forward contract with a strike at the barrier. If there are nonzero interest rates, we will not be able to enter into such a contract at no cost. Consequently, these results are only generally valid in cases where there is zero cost of carry, for example, where the underlying is a forward price, in foreign exchange markets where both currencies have the same interest rate, or commodities where the interest rate is the same as the convenience yield. Secondly, recall that the only assumption we made on the paths was continuity. This assumption is key to knowing that we can sell forward as we hit the barrier. In fact, the upper bound will still hold if the path is not continuous, provided we sell forward the first time that we go above the barrier, at which point, we can enter into a forward contract that is at least as good for our purposes. Note, however, that under the model for which the bound is tight, we must cross the barrier continuously. The same is not true of the lower bound, which fails if the asset price does not cross the barrier continuously. If the path is not assumed continuous, a new bound can be derived, which corresponds to the asset jumping immediately to its final value. The third aspect to note about these constructions is that there is a natural extension to the case where calls are available at finitely many strikes. Consider the upper bound on the one-touch option, and suppose that calls trade at a finite set of strikes *K*1*, K*2*,...,Kn*. Rather than taking the infimum over *x* where *x<R*, to get an upper bound, we can take the minimum over the strikes at which calls are available

$$OT(R,T) \le \min_{i:K_i < R} \frac{C(K_i,T)}{R-K_i} \tag{12}$$

The previous arguments can be applied directly to show that this is an upper bound. It can also be shown that there is a model that fits with the call prices, and under which this bound is attained, so the resulting bounds are the best possible. Details of this extension can be found in [7].

#### **Put–Call Symmetry**

An alternative approach to the pricing of barrier options using the above techniques is to introduce the concept of "put-call symmetry". Following [5], we say that put-call symmetry holds if the value of a call struck at  $K > S_t$ , and a put struck at  $H < S_t$ , satisfy

$$C(K)K^{-1/2} = P(H)H^{-1/2}$$
(13)

where the current asset price  $S_0$  is the geometric mean of H and K:  $(KH)^{1/2} = S_0$ . While this is a more general concept, in the context of a **local volatility model**, this assumption can be interpreted in terms of a symmetry condition on the volatility:  $\sigma(S_t, t) =$  $\sigma(S_0^2/S_t, t)$ . In particular, this is an assumption that is satisfied whenever the volatility is a deterministic function of time. Alternatively, if we graph the **implied volatility** smile against  $log(K/S_t)$ , the smile should be symmetric. Note that, as above, we still require either the interest rate to be zero, or, for example, to be working with a forward price.

Under the assumption that put-call symmetry holds at all future times, we can construct replicating portfolios for many types of barrier options. Consider the case of a down-and-in call (see Barrier Options), with a barrier at R and strike K, so  $R < S_0$ . Then we may hedge the option simply by purchasing initially  $K/R$  puts at H, where  $H = R^2/K$ . If the asset never reaches the barrier, both the down-and-in call and the put expire worthless, so we consider the behavior at the barrier. When the asset is at the barrier, put-call symmetry implies

$$C(K) = \frac{K}{R}P(H) \tag{14}$$

and so we may sell the puts and buy a call with strike  $K$ . Thus this portfolio exactly replicates the down-and-in call.

The results described above were initially introduced in [5], where, in addition to considering knockin and knockout calls, and the one-touch option above, the authors also included the **lookback** option by expressing it as a portfolio of suitable down-andin options. Further developments can be found in [10], which considers the replication of more general options in this framework, and [12], which extends to double knockout calls, rolldown calls, and ratchet calls. Further extensions to these ideas, where the volatility is assumed to be a known function of the underlying and time, can be found in [2]. A different approach to static hedging is given in [20].

## Arbitrage Bounds via Skorokhod Embeddings

As shown by Dupire [21], if prices of calls at all strikes *and* all maturities are known, there is a unique diffusion model, the local volatility model, which matches those call prices. If we drop the diffusion assumption, we are led to follow the line of reasoning from [6]. One of the conclusions from this work is that knowing the call prices at all strikes at a fixed future maturity implies the law of the asset price under the risk-neutral measure at this fixed future date. Further, as a consequence of the assumption of no arbitrage, we believe that under the riskneutral measure, the discounted asset price should be a martingale. In this manner, we should be able to restrict the class of possible (discounted, risk-neutral) price processes to the class of martingales that have a given terminal distribution. If we now also wish to infer information about the price of an exotic option, we can ask the question: what is the largest/smallest price implied by the martingale price processes in this class? Moreover, we might hope to find an arbitrage if the option trades outside this range.

One of the simplest examples to consider is the one-touch option above: under the risk-neutral measure, the price of the call is the discounted probability that the price process goes above the barrier before the expiry date. By restricting ourselves to the class of martingales with a given terminal law, we should be able to deduce some information about the possible values of this probability, and thus of the price of the option. The key to using this approach efficiently is to find a suitable representation of the set of martingales with the given terminal distribution.

A classical result from probability theory, the Dambis-Dubins-Schwartz Theorem, states that any continuous martingale may be written as the time change of a Brownian motion (see, for example, [33, Chapter V]), and this is essentially true if the martingale is only right continuous [30]. Hence, if the discounted asset price is a martingale, one would expect it to be a time change of a Brownian motion—that is, we would expect to be able to write

$$B(t)S_t = W_{\tau(t)} \tag{15}$$

where *Wt* is a Brownian motion, *τ (t)* is increasing in *t* and is a stopping time for all *t*. As a consequence, any martingale price process should be a time change of a Brownian motion. If, in addition, we know that the law of *ST* under the risk-neutral measure is implied by the call prices, we also know that *Wτ (T )* has a given law. Finally, suppose that the time change is continuous (as it will be if the price process is continuous), then many of the properties in which we are interested remain unaffected by the exact form of the time change. For example, consider the probability of whether the discounted asset price goes above a barrier *R* before time *T* . This is the same as the probability that the Brownian motion *Wt* with *Wτ (t)* = *B(t)St* goes above the barrier before time *τ (T )*. Moreover, consider two time changes *τ (t)* and *τ (t)* ˜ , such that we always have *τ (T )* = ˜*τ (T )*. Then the probability of whether the barrier has been breached will be the same for the price processes corresponding to the time change *τ* and the time change *τ*˜. Consequently, if we are concerned with such path properties of the underlying price process, when we look in the Brownian setting, we need only differentiate between different final stopping times *τ (T )*, and not different time changes.

The argument then goes as follows: suppose we know call prices at all strikes at time *T* . From this information, we may deduce the law of the discounted asset price *B(T )ST* , which we assume to be a time change of a Brownian motion, and whose value at some stopping time *τ* therefore has the same law. Since the time change in the intermediate time is assumed to be continuous, and its exact form will not impact the quantities of interest, we get a one-toone correspondence between possible price processes and the class of stopping times of a Brownian motion that have a given law. This line of reasoning is of interest, since the problem of finding a stopping time with a given terminal law has a long history in the probabilistic literature, where it is known as the **Skorokhod embedding problem**. In particular, given a distribution *µ*, we say that a stopping time *τ* is a (Skorokhod) embedding of *µ*, if *Wτ* has law *µ*. The recent survey paper [31] contains a comprehensive survey of the probabilistic literature on the Skorokhod embedding problem.

Getting back to the one-touch option, we see that the upper bound will correspond to the stopping time that maximizes the probability of being larger than the barrier within the class of embeddings, and the minimum will correspond to stopping time that minimizes the probability within this class. The construction of arbitrage bounds for the price of the option is therefore equivalent to the identification of extremal Skorokhod embeddings for the law implied by the call prices at maturity, as seen in [7]. The construction that attains this maximum is due to Azema and Yor [3], while the construction that attains the minimum is due to Perkins [32], and it can be shown that these embeddings do indeed have the behavior that was hypothesized previously: for the upper bound, those paths that hit the barrier remain above the level *x* derived in the bound, while in the lower bound, those paths that hit the barrier all either finish above the barrier, or stop below *y*.

The Skorokhod embedding approach was initially explored in [23]. In this work, it is shown that the upper bound on the price of a lookback option can be computed in terms of the available call prices. Moreover, Hobson [23] has constructed a trading strategy that will result in an arbitrage should the lookback option trade above the given bound. In this case, the strategy involves constructing an initial portfolio of calls (purchased at the specified prices) and then selling these calls appropriately as the price process sets new maxima. The price at which the calls can be sold will be at least the intrinsic value of the call, and it can be shown that the profit from selling off the calls appropriately will be at least the payoff from the lookback option. A simple lower bound is also derived, but without assuming any continuity. For discontinuous asset prices, the lower bound is attained by the price process that jumps immediately to its final value. In terms of the corresponding Skorokhod embeddings, the upper bound has close connections with the embedding due to Azema and Yor [3]; this can be shown to maximize the law of the maximum over the class of embeddings. Further, it can be shown that if we use the price process that corresponds to the stopping time constructed in [3], then the trading strategy dominating the lookback option actually attains equality demonstrating that the upper bound is the best possible. This connection between an extremal Skorokhod embedding and a corresponding bound on the price of a connected exotic option has been exploited a number of times: in [8], these techniques are used to generalize the above results to the case where the call prices at an intermediate time are also known; in [24] the embedding due to Perkins [32] is generalized to provide a lower bound on the price of a forward start digital option, under the assumption that the price process is continuous; in [16] the embedding of Vallois [35] is used to provide an upper bound on products related to corridor variance options.

A related development of these ideas is considered in [28], wherein the problem of fitting martingales to marginal distributions specified at all maturities is presented, and some solutions corresponding to the different Skorokhod embedding approaches, the local volatility models of Dupire [21], and processes with independent increments are discussed.

## **Advantages and Disadvantages**

From a theoretical point of view, the results described above provide a clear, satisfactory picture: for a relatively large class of options, a range of modelfree prices, or even exact prices, can be established. Where there is a range of prices, the upper and lower bounds can usually be shown to be tight, and trading strategies produced that result in arbitrages, should the bounds be violated.

However, the results have often been produced under strong restrictions on the mechanics of the market—typically, the cost of carry has been assumed to be zero, and factors such as transaction costs have been ignored. To some extent, these factors can be added into the bounds, although this is at the expense of wider bounds. Moreover, the bounds that result from the model-free techniques have a tendency to be rather wide. Figure 1 illustrates the resulting bounds for the one-touch option, comparing the upper and lower bounds described earlier, with the actual price derived from a Black–Scholes model. The range of the bounds is, for interesting values, of the order of 5% of the final payoff above the Black–Scholes price, and as much as 15% below the Black–Scholes price. These ranges are of much too high an order to be helpful for pricing purposes.

How else might these techniques be of use in practice? One important feature is the tendency to produce simple hedging portfolios. These allow a trader to cover a position in a derivative with a portfolio that needs little or no ongoing management, and through which they have a guaranteed lower bound on any possible hedging error. Several authors, for example, [22, 34], have produced comparisons between static or semistatic and dynamic

![](_page_6_Figure_7.jpeg)

**Figure 1** Upper and lower model-free bounds on the price of a one-touch option, as a function of the strike, compared with the Black–Scholes price. The interest rate is 0, the asset price is \$90, and *σ* = 15%

hedging. In [34], there is no clear outperformance by either strategy, but in some circumstances the static or semistatic hedging strategy outperforms the dynamic strategy. In [22], the authors consider barrier options, and find that some static hedging strategies for barrier options appear to outperform dynamic strategies. Another useful observation is that by identifying the extremal models, one can identify the key model properties that influence the price of the option: for example, in finding bounds for the onetouch barrier, the extremal models were identified as those models that either hit the barrier and stay close, or those models that hit the barrier and end up far away. Knowledge of these extremes might help in deciding where the real price might lie in relation to the arbitrage bounds, or how prices of the option might react to large structural changes to the market. Finally, arbitrage bounds can also be considered as a special case of the **good-deal bounds** of [14]. Good-deal bounds provide a range of prices, outside of which there exists a trading strategy whose payoff may be considered a "good deal", which is not necessarily an arbitrage, but is sufficiently close to one to be very desirable for an investor.

## **Additional Resources**

There are a number of papers [17, 25, 26] that consider deriving bounds on the price of **basket options**, where the payoff of the option depends on the value of a weighted sum of a number of assets, and where calls are traded on each of the underlying assets. There are also connections to [1], where bounds on the prices of **Asian options** are derived.

Another class of options where similar hedging techniques have been considered are installment options [19], which are options similar to a European call, but where the holder pays for the option in a set number of installments, and has the option to stop paying the installments at any point before maturity, thereby losing the final payoff for the contract.

A common complication that arises in constructing many of the bounds and their respective hedging portfolios is that there can be some nontrivial optimization problems, typically, large linear programming problems [4, 17, 25].

## **References**

- [1] Albrecher, H., Mayer, P.A. & Schoutens, W. (2008). General lower bounds for arithmetic Asian option prices, *Applied Mathematical Finance* **15**(2), 123–149.
- [2] Andersen, L.B.G., Andreasen, J. & Eliezer, D. (2002). Static replication of barrier options: some general results, *Journal of Computational Finance* **5**(4), 1–25.
- [3] Azema, J. & Yor, M. (1979). Une solution simple au ´ probleme de Skorokhod, in ` *S´eminaire de Probabilit´es, XIII (Univ. Strasbourg, Strasbourg, 1977/78)*, *Lecture Notes in Mathematics*, Springer, Berlin, Vol. 721, pp. 90–115.
- [4] Bertsimas, D. & Popescu, I. (2002). On the relation between option and stock prices: a convex optimization approach, *Operations Research* **50**(2), 358–374.
- [5] Bowie, J. & Carr, P. (1994). Static simplicity, *Risk* **7**(8), 45–49.
- [6] Breeden, D.T. & Litzenberger, R.H. (1978). Prices of state-contingent claims implicit in option prices, *Journal of Business* **51**(4), 621–651.
- [7] Brown, H., Hobson, D. & Rogers, L.C.G. (2001a). Robust hedging of barrier options, *Mathematical Finance* **11**(3), 285–314.
- [8] Brown, H., Hobson, D. & Rogers, L.C.G. (2001b). The maximum maximum of a martingale constrained by an intermediate law, *Probability Theory and Related Fields* **119**(4), 558–578.
- [9] Buehler, H. (2006). Expensive martingales, *Quantitative Finance* **6**(3), 207–218.
- [10] Carr, P. & Chou, A. (1997). Breaking barriers, *Risk* **10**(9), 139–145.
- [11] Carr, P. & Madan, D.B. (2005). A note on sufficient conditions for no arbitrage, *Finance Research Letters* **2**, 125–130.

- [12] Carr, P., Ellis, K. & Gupta, V. (1998). Static hedging of exotic options, *Journal of Finance* **53**(3), 1165–1190.
- [13] Carr, P., Geman, H., Madan, D.B. & Yor, M. (2003). Stochastic volatility for Levy processes, ´ *Mathematical Finance* **13**(3), 345–382.
- [14] Cerny, A. & Hodges, S.D. (1999). *The theory of gooddeal pricing in financial markets*, *FORC preprint, No. 98/90*.
- [15] Cousot, L. (2007). Conditions on option prices for absence of arbitrage and exact calibration, *Journal of Banking and Finance* **31**, 3377–3397.
- [16] Cox, A.M.G., Hobson, D.G. & Obloj, J. (2008). Pathwise inequalities for local time: applications to Skorokhod embeddings and optimal stopping, *Annals of Applied Probability* **18**(5), 1870–1896.
- [17] d'Aspremont, A. & El Ghaoui, L. (2006). Static arbitrage bounds on basket option prices, *Mathematical Programming* **106**(3), Series A, 467–489.
- [18] Davis, M.H.A. & Hobson, D.G. (2007). The range of traded option prices, *Mathematical Finance* **17**(1), 1–14.
- [19] Davis, M.H.A., Schachermayer, W. & Tompkins, R.G., (2001). Installment options and static hedging, in *Mathematical Finance* (Konstanz, 2000), Trends in Mathematics, Birkhauser, Basel, pp. 131–139. ¨
- [20] Derman, E., Ergener, D. & Kani, I. (1995). Static options replication, *Journal of Derivatives* **2**, 78–95.
- [21] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 32–39.
- [22] Engelmann, B., Fengler, M.R., Nalholm, M. & Schwender, P. (2006). Static versus dynamic hedges: an empirical comparison for barrier options, *Review of Derivatives Research* **9**(3), 239–264.
- [23] Hobson, D.G. (1998). Robust hedging of the lookback option, *Finance and Stochastics* **2**(4), 329–347.
- [24] Hobson, D.G. & Pedersen, J.L. (2002). The minimum maximum of a continuous martingale with given initial and terminal laws, *Annals of Probability* **30**(2), 978–999.
- [25] Hobson, D., Laurence, P. & Wang, T. (2005a). Staticarbitrage upper bounds for the prices of basket options, *Quantitative Finance* **5**(4), 329–342.
- [26] Hobson, D., Laurence, P. & Wang, T. (2005b). Staticarbitrage optimal subreplicating strategies for basket options, *Insurance, Mathematics & Economics* **37**(3), 553–572.
- [27] Jaschke, S.R. (1997). Arbitrage bounds for the term structure of interest rates, *Finance and Stochastics* **2**(1), 29–40.
- [28] Madan, D.B. & Yor, M. (2002). Making Markov martingales meet marginals: with explicit constructions, *Bernoulli* **8**(4), 509–536.
- [29] Merton, R.C. (1973). Theory of rational option pricing, *The Bell Journal of Economics and Management Science* **4**(1), 141–183.
- [30] Monroe, I. (1972). On embedding right continuous martingales in Brownian motion, *Annals of Mathematical Statistics* **43**, 1293–1311.

- [31] Obłoj, J. (2004). The Skorokhod embedding problem ´ and its offspring, *Probability Surveys* **1**, 321–390, electronic.
- [32] Perkins, E. (1986). The Cereteli-Davis solution to the *H*1-embedding problem and an optimal embedding in Brownian motion, in *Seminar on Stochastic Processes, 1985* (Gainesville, Fla., 1985), Progress in Probabity and Statistics, Birkhauser Boston, Boston, Vol. 12, ¨ pp. 172–223.
- [33] Revuz, D. & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], 3rd Edition, Springer-Verlag, Berlin, Vol. 293.

- [34] Tompkins, R. (1997). Static versus dynamic hedging of exotic options: an evaluation of hedge performance via simulation, *Netexposure* **1**, 1–28.
- [35] Vallois, P. (1983). Le probleme de Skorokhod sur ` **R**: une approche avec le temps local, in *Seminar on Probability, XVII*, Lecture Notes in Mathematics, Springer, Berlin, Vol. 986, pp. 227–239.

## **Related Articles**

**Arbitrage Strategy**; **Barrier Options**; **Dupire Equation**; **Good-deal Bounds**; **Hedging**; **Model Calibration**; **Skorokhod Embedding**; **Static Hedging**.

ALEXANDER COX
# **Pricing Kernels**

Pricing kernels or stochastic discount factors (SDFs) (see Stochastic Discount Factors) are used to represent valuation operators in dynamic stochastic economies. A kernel is a commonly used mathematical term for representing an operator. The term stochastic discount factor (SDF) extends concepts from economics and finance to include adjustments for risk. As we will see, there is a close connection between the two terms. The terms *pricing kernel* and SDF are often used interchangeably.

After deriving convenient representations for prices, we provide several examples of stochastic discount factors and discuss econometric methods for estimating and testing asset pricing models that restrict stochastic discount factors.

# **Representing Prices**

We follow Ross [49] and Harrison and Kreps [34] by exploring the implications of no arbitrage in frictionless markets to obtain convenient representations of pricing operators. We build these operators as mappings that assign prices that trade in competitive markets to payoffs on portfolios of assets. The payoffs specify how much a numeraire good is provided in alternative states of the world. To write these operators, we invoke the *law of one price*, which stipulates that any two assets with the same payoff must necessarily have the same price. This law is typically implied by but is weaker than the *principle* of no arbitrage (see Fundamental Theorem of Asset **Pricing**). Formally, the principle of no arbitrage stipulates that nonnegative payoffs that are positive with positive (conditional) probability command a strictly positive price. To see why the principle implies the law of one price, suppose that there is such a nonnegative portfolio payoff and call this portfolio  $a$ . If two portfolios, say  $b$  and  $c$  have the same payoff but the price of portfolio  $b$  is less than that of portfolio  $c$ , then an arbitrage opportunity exists. This can be seen by taking a long position on portfolio  $b$ , a short position on portfolio  $c$ , and using the proceeds to purchase portfolio  $a$ . This newly constructed portfolio has zero price but a positive payoff, violating the principle of no arbitrage.

Given that we can assign prices to payoffs, let  $\pi_{t,t+1}$  be the date t valuation operator for payoffs (consumption claims) at date  $t + 1$ . This operator assigns prices or values to portfolio payoffs  $p_{t+1}$  in a space  $P_{t+1}$  suitably restricted. We extend Debreu's  $[17]$  notion of a valuation functional to a valuation operator to allow for portfolio prices to depend on date t information. With this in mind, let  $\mathcal{F}_t$  be the sigma algebra used to depict the information available to all investors at date  $t$ . We use a representation of  $\pi_{t,t+1}$  of the following form:

$$\pi_{t,t+1}(p_{t+1}) = E(s_{t+1}p_{t+1}|\mathcal{F}_t) \tag{1}$$

for some positive random variable  $s_{t+1}$  with probability one and any admissible payoff  $p_{t+1} \in P_{t+1}$  on a portfolio of assets.

**Definition 1** The positive random variable  $s_{t+1}$  is the pricing kernel of the valuation operator  $\pi_{t,t+1}$ , provided that representation  $(1)$  is valid.

If a kernel representation exists, the valuation operator  $\pi_{t,t+1}$  necessarily satisfies the principle of no arbitrage.

How does one construct a representation of this type? There are alternative ways to achieve this. First, suppose that (i)  $P_{t+1}$  consists of all random variables that are  $\mathcal{F}_{t+1}$  measurable and have finite conditional (on  $\mathcal{F}_t$ ) second moments, (ii)  $\pi_{t,t+1}$  is linear conditioned on  $\mathcal{F}_t$ , (iii)  $\pi_{t,t+1}$  also satisfies a conditional continuity restriction, and (iv) the principle of no arbitrage is satisfied. The existence of a kernel  $s_{t+1}$ follows from a conditional version of the Riesz representation theorem [30]. Second, suppose that (i)  $P_{t+1}$  consists of all bounded random variables that are  $\mathcal{F}_{t+1}$  measurable, (ii)  $\pi_{t,t+1}$  is linear conditioned on  $\mathcal{F}_t$ , (iii)  $E(\pi_{t,t+1})$  induces an absolutely continuous measure on  $\mathcal{F}_{t+1}$ , and (iv) the principle of no arbitrage is satisfied. We can apply the Radon-Nikodym theorem to justify the existence of a kernel. In both these cases, security markets are *complete* in that payoffs of any indicator function for events in  $\mathcal{F}_{t+1}$  are included in the domain of the operator.<sup>a</sup> Kernels can be constructed for other mathematical restrictions on asset payoffs and prices as well.

As featured by Harrison and Kreps [34] and Hansen and Richard [30], suppose that  $P_t$  is not so richly specified. Under the (conditional) Hilbert space formulation and appropriate restrictions on  $P_t$ , we may still apply a (conditional) version of the Riesz

representation theorem to represent

$$\pi_{t,t+1}(p_{t+1}) = E(q_{t+1}p_{t+1}|\mathcal{F}_t) \tag{2}$$

for some  $q_{t+1} \in P_{t+1}$  and all  $p_{t+1} \in P_{t+1}$ . Even if the principle of no arbitrage is satisfied, there is no guarantee that the resulting  $q_{t+1}$  is positive with probability 1, however. Provided, however, that we can extend  $P_{t+1}$  to a larger space that includes indicator functions for events in  $\mathcal{F}_{t+1}$  while preserving the principle of no arbitrage, when there exists a pricing kernel  $s_{t+1}$  for  $\pi_{t,t+1}$ . However, the pricing kernel may not be unique.

## **Stochastic Discounting**

The random variable  $s_{t+1}$  is also called the *one-period* stochastic discount factor. Its multiperiod counterpart is as follows.

**Definition 2** The stochastic discount process  $\{S_{t+1} :$  $t = 1, 2, \ldots$  is

$$S_{t+1} = \prod_{j=1}^{t+1} s_j \tag{3}$$

where  $s_i$  is the pricing kernel used to represent the valuation operator between dates  $j-1$  and  $j$ .

Thus, the  $t+1$  period SDF compounds the corresponding one-period SDFs. The compounding is justified by the law of iterated values when trading is allowed at intermediate dates. As a consequence,

$$\pi_{0,t+1}(p_{t+1}) = E\left(S_{t+1}p_{t+1}|\mathcal{F}_0\right) \tag{4}$$

gives the date zero price of a security that pays  $p_{t+1}$ in the numeraire at date  $t + 1$ . An SDF discounts the future in a manner that depends on future outcomes. This outcome dependence is included in order to make adjustments for risk. However, such adjustments are unnecessary for a discount bond because such a bond has a payoff that is equal to one independent of the state realized at date  $t+1$ . The price of a date  $t + 1$  discount bond is obtained from formula (4) by letting  $p_{t+1} = 1$  and hence is given by  $E\left[S_{t+1}|\mathcal{F}_0\right]$ .

More generally, the date  $\tau$  price of  $p_{t+1}$  is given  $as$ 

$$\pi_{\tau,t+1}(p_{t+1}) = E\left[\left(\frac{S_{t+1}}{S_{\tau}}\right)p_{t+1}|\mathcal{F}_{\tau}\right] \qquad (5)$$

for  $\tau \leq t$ . Thus, the ratio  $\frac{S_{t+1}}{S_{\tau}}$  is the pricing kernel for the valuation operator  $\pi_{\tau,t+1}$ .

## **Risk-neutral Probabilities**

Given a one-period pricing kernel, we build the socalled *risk-neutral probability measure* recursively as follows. First, rewrite the one-period pricing operator as

$$\pi_{t,t+1}(p_{t+1}) = E(s_{t+1}|\mathcal{F}_t) \tilde{E}(p_{t+1}|\mathcal{F}_t) \quad (6)$$

where

$$\tilde{E}\left(p_{t+1}|\mathcal{F}_{t}\right) = E\left(\left[\frac{s_{t+1}}{E\left(s_{t+1}|\mathcal{F}_{t}\right)}\right]p_{t+1}|\mathcal{F}_{t}\right) \quad (7)$$

Thus, one-period pricing is conveniently summarized by a one-period discount factor for a riskless payoff,  $E(s_{t+1}|\mathcal{F}_t)$ , and a change of the conditional probability measure implied by the conditional expectation operator  $\tilde{E}(\cdot|\mathcal{F}_t)$ . Risk adjustments are now absorbed into the change of probability measure.

Using this construction repeatedly, we decompose the date  $t + 1$  component of the SDF process:

$$S_{t+1} = \bar{S}_{t+1} M_{t+1} \tag{8}$$

where

$$\bar{S}_{t+1} = \left[ \prod_{j=1}^{t+1} E\left(s_j | \mathcal{F}_{j-1}\right) \right] \tag{9}$$

is the discount factor constructed from the sequence of one-period riskless discount factors and

$$M_{t+1} = \prod_{j=1}^{t+1} \frac{s_j}{E\left(s_j | \mathcal{F}_{j-1}\right)} = \frac{S_{t+1}}{\bar{S}_{t+1}} \qquad (10)$$

is the positive martingale adapted to  $\{\mathcal{F}_t : t =$  $0, 1, \ldots$  with expectation unity. For each date t,  $M_t$ can be used to assign  $\tilde{\cdot}$  probabilities to events in  $\mathcal{F}_t$ . Since  $E(M_{t+1}|\mathcal{F}_t) = M_t$ , the date  $t+1$  assignment of probabilities to events in  $\mathcal{F}_{t+1}$  is compatible with the date *t* assignment to events in  $\mathcal{F}_t \subset \mathcal{F}_{t+1}$ . This follows from the law of iterated expectations. In effect, the law of iterated expectations enforces the law of iterated values.

Applying factorization  $(8)$ , we have an alternative way to represent  $\pi_{\tau,t+1}$ :

$$\pi_{\tau,t+1}(p_{t+1}) = \tilde{E}\left[\bar{S}_{t+1}p_{t+1}|\mathcal{F}_t\right] \tag{11}$$

Pricing is reduced to riskless discounting and a distorted (risk-neutral) conditional expectation. The insight provided in [34, 49] is that dynamic asset pricing in the absence of arbitrage is captured by the existence of a positive (with probability one) martingale that can be used to represent prices in conjunction with a sequence of one-period riskless discount factors. Moreover, it justifies an arguably mild modification of the "efficient market hypothesis" that states that discounted prices should behave as martingales with the appropriate cash-flow adjustment. While Rubinstein [50] and Lucas [42] had clearly shown that efficiency should not preclude risk compensation, the notion of equivalent martingale measures reconciles the points of view under greater generality. The martingale property and associated "risk-neutral pricing" are recovered for some distortion of the historical probability measure that encapsulates risk compensation. This distortion preserves "equivalence" (the two probability measures agree about which events in  $\mathcal{F}_t$  are assigned probability zero measure for each finite  $t$ ) by ensuring the existence of a strictly positive SDF.

The concept of equivalent martingale measure (for each  $t$ ) has been tremendously influential in derivative asset pricing. The existence of such a measure allows risk-neutral pricing of all contingent claims that are attainable because their payoff can be perfectly duplicated by self-financing strategies. Basic results from probability theory are directly exploitable in characterizing asset pricing in an arbitrage-free environment. More details can be found in Econometrics of Option Pricing.

Although we have developed this discussion for a discrete-time environment, there are wellknown continuous-time extensions. In the case of continuous-time Brownian motion information structures, the change of measure has a particularly simple structure. In accordance to the Girsanov theorem, the Brownian motion under the original probability measure becomes a Brownian motion with drift under the risk-neutral measure. These drifts absorb the adjustments for exposure to Brownian motion risk.

# **Investors' Preferences**

Economic models show how exposure to risk is priced and what determines riskless rates of interest. As featured by Ross [49], the risk exposure that

is priced is the risk that cannot be diversified by averaging through the construction of portfolios of traded securities. Typical examples include macroeconomic shocks. Empirical macroeconomics seeks to identify macroeconomic shocks to quantify responses of macroeconomic aggregates to those shocks. Asset pricing models assign prices to exposure of cash flows to the identified shocks. The risk prices are encoded in SDF processes and hence are implicit in the risk-neutral probability measures used in financial engineering.

SDFs implied by specific economic models often reflect investor preferences. Subjective rates of discount and intertemporal elasticities appear in formulas for risk-free interest rates, and investors' aversion to risk appears in formulas for the prices assigned to alternative risk exposures. Sometimes the reflection of investor preferences is direct and sometimes it is altered by the presence of market frictions. In what follows, we illustrate briefly some of the SDFs that have been derived in the literature.

# Power Utility

When there are no market frictions and markets are complete, investors' preferences can be subsumed into a utility function of a representative agent. In what follows, suppose that the representative investor has discounted time-separable utility with a constant elasticity of substitution (CES)  $1/\rho$ :

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left(\frac{C_{t+1}}{C_t}\right)^{-\rho} \tag{12}$$

This is the SDF for the power utility specification of the model of Rubinstein [50] and Lucas [42].<sup>b</sup>

#### Recursive Utility

Following Epstein and Zin [18], Kreps and Porteus [41] and Weil [53], preferences are specified recursively using continuation values for hypothetical consumption processes. Using a double CES recursion, the resulting SDF is

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left(\frac{C_{t+1}}{C_t}\right)^{-\rho} \left[\frac{U_{t+1}}{\mathsf{R}_t(U_{t+1})}\right]^{\rho-\gamma} \quad (13)$$

where  $\gamma > 0$ ,  $\rho > 0$ ,  $U_t$  is the continuation value associated with current and future consumption, and

$$\mathsf{R}_{t}(U_{t+1}) \doteq \left( E\left[ \left( U_{t+1} \right)^{1-\gamma} | \mathcal{F}_{t} \right] \right)^{1/(1-\gamma)} \tag{14}$$

is the risk-adjusted continuation value. The parameter  $\rho$  continues to govern the elasticity of substitution, whereas the parameter  $\gamma$  alters the risk preferences. See [25, 31, 52] for a discussion of the use of continuation values in representing the SDF and see [11, 25] for discussions of empirical implications. When  $\rho = 1$ , the recursive utility model coincides with a model in which investors have a concern about robustness as in [6].

The recursive utility model is just one of a variety of ways of altering investors' preferences. For instance, Constantinides [15] and Heaton [36] explore implications of introducing intertemporal complementarities in the form of "habit persistence".

#### Consumption Externalities and Reference Utility

Abel [1], Campbell and Cochrane [12] and Menzly et al. [45] develop asset pricing implications of models in which there are consumption externalities in models with stochastic consumption growth. These externalities can depend on a social stock of past consumptions. The implied one-period SDF in these models has the following form:

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left(\frac{C_{t+1}}{C_t}\right)^{-\rho} \frac{\phi(H_t)}{\phi(H_0)} \qquad (15)$$

The social stock of consumption is built as a possibly nonlinear function of current and past social consumption or innovations to social consumption. The construction of this stock differs across the various specifications. The process  $\{H_t : t = 0, 1, \ldots\}$  is the ratio of the consumption to the social stock and  $\phi$  is an appropriately specified function of this ratio. In a related approach, Garcia et al. [21] consider investors' preferences in consumption as being evaluated relative to a reference level that is determined externally. The SDF is

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left(\frac{C_{t+1}}{C_t}\right)^{-\rho} \left(\frac{H_t}{H_0}\right)^{\eta} \tag{16}$$

where the process  $\{H_t : t = 0, 1, \ldots\}$  is the ratio of the consumption to the reference level. In effect, the social externality in these models induces a preference shock or wedge to the SDF specification, which explicitly depends on the equilibrium aggregate consumption process. Finally, Bakshi and Chen [8] develop implications for a model in which relative wealth enters the utility function of investors.

## Incomplete Markets

Suppose that individuals face private shocks that they cannot insure against but that they can write complete contracts over aggregate shocks. Let  $\mathcal{F}_{t+1}$ denote the date  $t + 1$  sigma algebra generated by aggregate shocks available up until date  $t + 1$ . This conditioning information set determines the type of risk exposure that can be traded as of date  $t + 1$ . Under this partial risk sharing and power utility, the SDF for pricing aggregate uncertainty is

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left( \frac{E\left[ (C_{t+1}^j)^{-\rho} | \mathcal{F}_{t+1} \right]}{E\left[ (C_t^j)^{-\rho} | \mathcal{F}_t \right]} \right)$$
$$= \exp(-\delta) \left( \frac{C_{t+1}^a}{C_t^a} \right)^{-\rho}$$
$$\times \left( \frac{E\left[ (C_{t+1}^j/C_{t+1}^a)^{-\rho} | \mathcal{F}_{t+1} \right]}{E\left[ (C_t^j/C_t^a)^{-\rho} | \mathcal{F}_t \right]} \right) \quad (17)$$

In this example and those that follow,  $C_{t+1}^j$  is consumption for individual j and  $C_{t+1}^a$  is aggregate consumption. Characterization (17) of the SDF displays the pricing implications of limited risk sharing in security markets. It is satisfied, for instance, in the model of Constantinides and Duffie [16].

#### Private Information

Suppose that individuals have private information about labor productivity that is conditionally independent, given aggregate information, leisure enters preferences in a manner that is additively separable and consumption allocations are Pareto optimal given the private information. As shown by Kocherlakota and Pistaferri [40], the SDF follows from the "inverse Euler equation" of  $[40, 47]$ ,

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left( \frac{E\left[ (C_t^j)^{\rho} | \mathcal{F}_t \right]}{E\left[ (C_{t+1}^j)^{\rho} | \mathcal{F}_{t+1} \right]} \right)$$
$$= \exp(-\delta) \left( \frac{C_{t+1}^a}{C_t^a} \right)^{-\rho}$$
$$\times \left( \frac{E\left[ (C_t^j / C_t^a)^{\rho} | \mathcal{F}_t \right]}{E\left[ (C_{t+1}^j / C_{t+1}^a)^{\rho} | \mathcal{F}_{t+1} \right]} \right) \quad (18)$$

where  $\mathcal{F}_t$  is generated by the public information. As emphasized by Rogerson [47], this is a model with a form of "savings constraints". While the stochastic discount factor for the incomplete information model is expressed in terms of the  $(-\rho)^{\text{th}}$  moments of the cross-sectional distributions of consumption in adjacent time periods Kocherlakota and Pistaferri [40] show that in the private information model it is the  $\rho$ th moments of these same distributions.

#### Solvency Constraints

Luttmer [43], He and Modest [35], and Cochrane and Hansen [14] study asset pricing implications in models with limits imposed on the state contingent debt that is allowed. Alvarez and Jermann [4] motivate such constraints by appealing to limited commitment as in [38, 39]. When investors default, they are punished by excluding participation in asset markets in the future. Chien and Lustig [13] explore the consequences of alternative (out of equilibrium) punishments. Following [43], the SDF in the presence of solvency constraints and power utility is

$$\frac{S_{t+1}}{S_t} = \exp(-\delta) \left( \min_j \frac{C_{t+1}^j}{C_t^j} \right)^{-\rho} \tag{19}$$

and in particular,

$$\frac{S_{t+1}}{S_t} \ge \exp(-\delta) \left(\frac{C_{t+1}^a}{C_t^a}\right)^{-\rho} \tag{20}$$

Thus, the consumer with the smallest realized growth rate in consumption has a zero Lagrange multiplier on his or her solvency constraint, and hence the intertemporal marginal rate of substitution for this person is equal to the SDF. For the other consumers, the binding constraint prevents them shifting consumption from the future to the current period.

# Long-term Risk

The SDF process assigns prices to risk exposures at alternative investment horizons. To study pricing over these horizons, Alvarez and Jermann [5], Hansen and Scheinkman [32], and Hansen [24] use a Markov structure and apply factorizations of the following form:

$$S_{t+1} = \exp(-\eta t)M_{t+1}\frac{f(X_0)}{\hat{f}(X_{t+1})}$$
(21)

where  $\{M_t : t = 0, 1, \ldots\}$  is a multiplicative martin*gale*,  $\eta$  is a positive number,  $\{X_t : t = 0, 1, \ldots\}$  is an underlying Markov process, and  $\hat{f}$  is a positive function of the Markov state. The martingale is used as a convenient change of probability, one that is distinct from the "risk-neutral" measure described previously. Using this change of measure, asset prices can be depicted as

$$\pi_{0,t+1} (p_{t+1}) = \exp \left[ -\eta(t+1) \right] \times \hat{E} \left[ \frac{p_{t+1}}{\hat{f}(X_{t+1})} | X_0 \right] \hat{f}(X_0) \tag{22}$$

where  $\hat{\cdot}$  is the conditional expectation that is built with the martingale  $\{M_t : t \ge 0\}$  in (21). The additional discounting is now constant and simple expectations can now be computed by exploiting the Markov structure. Hansen and Scheinkman [32] give necessary and sufficient conditions for the martingale in factorization  $(21)$  to imply a change of probability measure with stable stochastic dynamics.<sup>c</sup> While Alvarez and Jermann  $[5]$  use this factorization to investigate the long-term links between the bond market and the macroeconomy, Hansen and Scheinkman [32] and Hansen [24] extend this factorization to study the valuation of cash flows that grow stochastically over time. As argued by Hansen and Scheinkman [32] and Hansen [24], these more general factorizations are valuable for the study of risk-return trade-offs for long investment horizons.

As argued by Bansal and Lehmann [9], many alterations to the power utility model in the section Power Utility can be represented as

$$\frac{S_{t+1}^*}{S_t^*} = \left(\frac{S_{t+1}}{S_t}\right) \left[\frac{f(X_{t+1})}{f(X_t)}\right] \tag{23}$$

for a positive function  $f$ . Transient components in asset pricing models are included to produce shortterm alterations in asset prices and are expressed as the ratio of a function of the Markov state in adjacent dates. As shown by Bansal and Lehmann [9], this representation arises in models with habit persistence, or as shown in [24] the same is true for a limiting version of the recursive utility model. Combining equation  $(23)$  with equation  $(21)$  gives

$$S_{t+1}^* = \exp(-\eta)M_{t+1} \frac{f^*(X_0)}{f^*(X_{t+1})}$$
(24)

where  $f^* = \hat{f}/f$ .

# **Inferring Stochastic Discount Factors** from Data

Typically a finite number of asset payoffs are used in econometric practice. In addition, the information used in an econometric investigation may be less than that used by investors. With this in mind, let  $Y_{t+1}$  denote an *n*-dimensional vector of asset payoffs observed by the econometrician such that

$$E\left(|Y_{t+1}|^2|\mathcal{G}_t\right) < \infty \tag{25}$$

with  $E\left(Y_{t+1}Y_{t+1}'|\mathcal{G}_t\right)$  nonsingular with probability 1 and  $\mathcal{G}_t \subset \mathcal{F}_t$ . Let  $Q_t$  denote the corresponding price vector that is measurable with respect to  $\mathcal{G}_t$ , implying that

$$E\left(s_{t+1}Y_{t+1}|\mathcal{G}_{t}\right) = Q_{t} \tag{26}$$

where  $s_{t+1} = S_{t+1}/S_t$ . We may construct a counterpart to a (one-period) SDF by forming

$$p_{t+1}^{*} = Y_{t+1}' \left[ E \left( Y_{t+1} Y_{t+1}' | \mathcal{G}_t \right) \right]^{-1} Q_t \tag{27}$$

Note that

$$E\left(p_{t+1}^*Y_{t+1}\middle|\mathcal{G}_t\right) = Q_t \tag{28}$$

suggesting that we could just replace  $s_{t+1}$  in equation (26) with  $p_{t+1}^*$ . We refer to  $p_{t+1}^*$  as a *counterpart* to an SDF because we have not restricted  $p_{t+1}^*$  to be positive.

This construction is a special case of the representation of the prices implied by a conditional version of the Riesz representation theorem [30]. Since  $p_{t+1}^*$ is not guaranteed to be positive, if we used it to assign prices to derivative claims (nonlinear functions of  $Y_{t+1}$ ), we might induce arbitrage opportunities. Nevertheless, provided that  $s_{t+1}$  has a finite conditional second moment,

$$E\left[ \left( s_{t+1} - p_{t+1}^* \right) Y_{t+1} | \mathcal{G}_t \right] = 0 \tag{29}$$

This orthogonality indicates that  $p_{t+1}^*$  is the conditional least-squares projection of  $s_{t+1}$  onto  $Y_{t+1}$ . Although a limited set of asset price data will not reveal  $s_{t+1}$ , the data can provide information about the date  $t + 1$  kernel for pricing over a unit time interval.

Suppose that  $Y_{t+1}$  contains a conditionally riskless payoff. Then

$$E\left(s_{t+1}|\mathcal{G}_t\right) = E\left(p_{t+1}^*|\mathcal{G}_t\right) \tag{30}$$

By a standard least-squares argument, the conditional volatility of  $s_{t+1}$  must be at least as large as the conditional volatility of  $p_{t+1}^*$ . There are a variety of other restrictions that can be derived. For instance, see [9, 28, 51].<sup>d</sup>

This construction has a direct extension to the case in which a complete set of contracts can be written over the derivative claims. Let  $H_{t+1}$  be the set of all payoffs that have finite second moments conditioned on  $\mathcal{G}_t$  and are of the form  $h_{t+1} = \phi(Y_{t+1})$ for some Borel measurable function  $\phi$ . Then, we may obtain a kernel representation for pricing claims with payoffs in  $H_{t+1}$  by applying the Riesz representation theorem:

$$\pi_t(h_{t+1}) = E\left(h_{t+1}^* h_{t+1} | \mathcal{G}_t\right) \tag{31}$$

for some  $h_{t+1}^*$  in  $H_{t+1}$ . Then

$$E\left[\left(s_{t+1} - h_{t+1}^*\right)h_{t+1} | \mathcal{G}_t\right) = 0 \tag{32}$$

which shows that the conditional least-squares projection of  $s_{t+1}$  onto  $H_{t+1}$  is  $h_{t+1}^*$ . In this case,  $h_{t+1}^*$  will be positive. Thus, this richer collection of observed tradable assets implies a more refined characterization of  $s_{t+1}$  including the possibility that  $s_{t+1} = h_{t+1}^*$ , provided  $H_{t+1}$  coincides with the full collection of oneperiod payoffs that could be traded by investors. The estimation procedures of  $[3, 48]$  can be interpreted as estimating  $h_{t+1}^*$  projected on the return information.

## **Linear Asset Pricing Models**

The long history of linear beta pricing can be fruitfully revisited within the SDF framework. Suppose that

$$Q_t = E\left[ (\lambda_t \cdot z_{t+1} + \alpha_t) Y_{t+1} | \mathcal{G}_t \right] \tag{33}$$

for some vector  $\lambda_t$  and some scalar  $\alpha_t$  that are  $\mathcal{G}_t$ measurable. Then

$$E\left[Y_{t+1}|\mathcal{G}_t\right] = \alpha_t^* \mathcal{Q}_t + \lambda_t^* \cdot \text{cov}(Y_{t+1}, z_{t+1}|\mathcal{G}_t) \quad (34)$$

where

$$\alpha_t^* = \frac{1}{\alpha_t + \lambda_t \cdot E(z_{t+1}|\mathcal{G}_t)}$$
  
$$\lambda_t^* = -\lambda_t \alpha_t^*$$
 (35)

which produces the familiar result that risk compensation expressed in terms of the conditional mean discrepancy:  $E[Y_{t+1}|\mathcal{G}_t] - \alpha_t^*Q_t$  depends on the conditional covariances with the factors. When the entries of  $z_{t+1}$  are standardized to a have conditional variances equal to unity, the entries of  $\lambda_t^*$  become the conditional regression coefficients, the "betas" of the asset payoffs onto the alternative observable factors. When  $z_{t+1}$  is the scalar market return, this specification gives the familiar CAPM from empirical finance. When  $z_{t+1}$  is augmented to include the payoff on a portfolio designed to capture risk associated with size (market capitalization) and the payoff on a portfolio designed to capture risk associated with book to market equity, this linear specification gives a conditional version of the [19] three-factor model designed to explain cross-sectional differences in expected returns (see Factor Models).

If the factors are among the asset payoffs and a conditional (on  $\mathcal{G}_t$ ) riskless payoff is included in  $Y_{t+1}$ , then

$$p_{t+1}^* = \lambda_t \cdot z_{t+1} + \alpha_t \tag{36}$$

and thus  $\lambda_t \cdot z_{t+1} + \alpha_t$  is the conditional least-squares regression of  $s_{t+1}$  onto  $Y_{t+1}$ .

For estimation and inference, consider the special case in which  $\mathcal{G}_t$  is degenerate and the vector  $Y_{t+1}$  consists of excess returns  $(Q_t$  is a vector of zeros). Suppose that the data generation process for  $\{(z_{t+1}, Y_{t+1})\}$  is independent and identically distributed (i.i.d.) and multivariate normal. Then  $\alpha_t$  and  $\lambda_t$  are time invariant. The coefficient vectors can be efficiently estimated by maximum likelihood and the pricing restrictions tested by likelihood ratio statistics [22]. As MacKinlay and Richardson [44] point out, it is important to relax the i.i.d. normal assumption in many applications. In contrast with the parametric maximum likelihood approach, generalized method of moments (GMM) provides an econometric framework that allows conditional heteroskedasticity and temporal dependence [23]. Moreover, the GMM approach offers the important advantage to provide a unified framework for the testing of conditional linear beta pricing models. See [37] for an extensive discussion of the application of GMM to linear factor models. We will have more to say about estimation when  $\mathcal{G}_t$  is not degenerate in our subsequent discussion.

Suppose that the conditional linear pricing model is misspecified. Hansen and Jagannathan [29] show that choosing  $(\lambda_t, \alpha_t)$  to minimize the maximum pricing error of payoffs with  $E(|p_{t+1}|^2|\mathcal{G}_t) = 1$  is equivalent to solving the least-squares problem:<sup>e</sup>

$$\min_{\lambda_{t}, \alpha_{t}, v_{t+1}, E((v_{t+1})^{2}|\mathcal{G}_{t}) < \infty} E\left[ \left( \lambda_{t} \cdot z_{t+1} + \alpha_{t} - v_{t+1} \right)^{2} | \mathcal{G}_{t} \right]$$
  
subject to  $Q_{t} = E\left( v_{t+1} Y_{t+1} | \mathcal{G}_{t} \right)$  (37)

This latter problem finds a random variable  $v_{t+1}$ that is close to  $\lambda_t \cdot z_{t+1} + \alpha_t$ , allowing for departures from pricing formula (33) where  $v_{t+1}$  is required to represent prices correctly. For a fixed  $(\lambda_t, \alpha_t)$ , the "concentrated" objective is

$$\begin{aligned} \left[ E[\lambda_t \cdot z_{t+1} + \alpha_t) Y_{t+1} | \mathcal{G}_t] - Q_t \right]' \\ \times \left[ E\left( Y_{t+1} Y_{t+1}' | \mathcal{G}_t \right) \right]^{-1} \\ \times \left[ E[\lambda_t \cdot z_{t+1} + \alpha_t) Y_{t+1} | \mathcal{G}_t] - Q_t \right] \end{aligned} \tag{38}$$

which is a quadratic form of the vector of pricing error. The random vector  $(\lambda_t, \alpha_t)$  is chosen to minimize this pricing error. In the case of a correct specification, this minimization results in a zero objective; otherwise, it provides a measure of model misspecification.

## **Estimating Parametric Models**

In examples of SDFs like those given in the section Investors' Preferences, there are typically unknown parameters to estimate. This parametric structure often permits the identification of the SDF even with limited data on security market payoffs and prices. To explore this approach, we introduce a parameter  $\theta$  that governs say investors' preferences. It is worth noting that inference about  $\theta$  is a semiparametric statistical problem since we avoid the specification of the law of motion of asset payoffs and prices along with the determinants of SDFs. In what follows, we sketch the main statistical issues in the following simplified context.

Suppose that  $s_{t+1} = \phi_{t+1}(\theta_o)$  is a parameterized model of an SDF that satisfies

$$E\left[\phi_{t+1}(\theta_o)Y_{t+1}|\mathcal{G}_t\right] - Q_t = 0\tag{39}$$

where  $\phi_{t+1}$  can depend on observed data but the parameter vector  $\theta_o$  is unknown. This conditional

moment restriction implies a corresponding unconditional moment condition:

$$E\left[\phi_{t+1}(\theta_o)Y_{t+1} - Q_t\right] = 0\tag{40}$$

As emphasized by Hansen and Richard [30], conditioning information can be brought in through the back door by scaling payoffs and their corresponding prices by random variables that are  $\mathcal{G}_t$  measurable. Hansen and Singleton [33] describe how to use the unconditional moment condition to construct a GMM estimator of the parameter vector  $\theta_{o}$  with properties characterized by Hansen [23] (see also Generalized Method of Moments (GMM)).

As an alternative, the parameterized family of models might be misspecified. Then the approach of [29] described previously could be used, whereby an estimator of  $\theta_{o}$  is obtained by minimizing

$$\left[\frac{1}{N}\sum_{t=1}^{N}\phi_{t+1}(\theta)Y_{t+1} - Q_{t}\right] \left[\frac{1}{N}\sum_{t=1}^{N}Y_{t+1}Y_{t+1}'\right]^{-1} \times \left[\frac{1}{N}\sum_{t=1}^{N}\phi_{t+1}(\theta)Y_{t+1} - Q_{t}\right] \tag{41}$$

with respect to  $\theta$ . This differs from a GMM formulation because the weighting matrix in the quadratic form does not depend on the SDF, but only on the second moment matrix of the payoff vector  $Y_{t+1}$ . This approach suffers from a loss of statistical efficiency in estimation when the model is correctly specified, but it facilitates comparisons across models because the choice of an SDF does not alter how the overall magnitude of the pricing errors is measured.

As in [26, 29], the analysis can be modified to incorporate the restriction that pricing errors should also be small for payoffs on derivative claims. This can be formalized by computing the time series approximation to the least-squares distance between a candidate, but perhaps misspecified, SDF from the family of strictly positive random variables  $z_{t+1}$  that solve the pricing restriction:

$$E(z_{t+1}Y_{t+1} - Q_t) = 0 \t\t(42)$$

See [25] for more discussion of these alternative approaches for estimation.

So far we have described econometric methods that reduce conditional moment restrictions  $(33)$  and  $(40)$ 

to their unconditional counterparts. From a statistical perspective, it is more challenging to work with the original conditional moment restriction. Along this vein, Ai and Chen [2] and Antoine et al. [7] develop nonparametric methods to estimate conditional moment restrictions used to represent pricing restrictions. In particular, Antoine *et al.* [7] develop a conditional counterpart to the continuously updated GMM estimator introduced by Hansen *et al.* [27] in which the weighting matrix in GMM objective explicitly depends on the unknown parameter to be estimated.<sup>f</sup> These same methods can be adapted to explicitly take account of conditioning information while allowing for misspecification as in [29].

# Acknowledgment

Jarda Borovicka provided suggestions that were very helpful for this article.

## **End Notes**

<sup>a.</sup> See [46] for a dynamic extension using this approach.

<sup>b.</sup>See [10] for a continuous-time counterpart.

<sup>c.</sup> Although Hansen and Scheinkman [32] use a continuoustime formulation, discrete-time counterparts to their analysis are straightforward to obtain.

d. These authors do not explicitly use conditioning information. In contrast, Gallant et al. [20] estimate conditional moment restrictions using a flexible parameterization for the dynamic evolution of the data.

e. Hansen and Jagannathan [29] abstract from conditioning information, but what follows is a straightforward extension.

<sup>f</sup>. The continuously updated estimator is also closely related to the "minimum entropy" and "empirical likelihood" approaches (see Entropy-based Estimation).

# References

- Abel, A.B. (1990). Asset prices under habit formation [1] and catching up with the Joneses, American Economic Review 80(2), 38-42.
- Ai, C. & Chen, X. (2003). Efficient estimation of [2] models with conditional moment restrictions containing unknown functions, *Econometrica* **71**(6), 1795–1843.
- [3] Ait-Sahalia, Y. & Lo, A.W. (1998). Nonparametric estimation of state-price densities implicit in financial asset prices, Journal of Finance 53(2), 499-547.
- [4] Alvarez, F. & Jermann, U.J. (2000). Efficiency, equilibrium, and asset pricing with risk of default, Econometrica 68(4), 775-798.

- [5] Alvarez, F. & Jermann, U.J. (2005). Using asset prices to measure the persistence of the marginal utility of wealth, *Econometrica* **73**(6), 1977–2016.
- [6] Anderson, E.W., Hansen, L.P. & Sargent, T.J. (2003). A quartet of semigroups for model specification, robustness, prices of risk, and model detection, *Journal of the European Economic Association* **1**, 69–123.
- [7] Antoine, B., Bonnal, H. & Renault, E. (2007). On the efficient use of the informational content of estimating equations: implied probabilities and euclidean empirical likelihood, *Journal of Econometrics* **138**(2), 461–487.
- [8] Bakshi, G.S. & Chen, Z. (1996). The spirit of capitalism and stock-market prices, *American Economic Review* **86**(1), 133–157.
- [9] Bansal, R. & Lehmann, B.N. (1997). Growth-optimal portfolio restrictions on asset pricing models, *Macroeconomic Dynamics* **1**(2), 333–354.
- [10] Breeden, D.T. (1979). An intertemporal asset pricing model with stochastic consumption and investment opportunities, *Journal of Financial Economics* **7**(3), 265–296.
- [11] Campbell, J.Y. (2003). Consumption-based asset pricing, in G.M. Constantinides, M. Harris & R.M. Stulz, eds, *Handbook of the Economics of Finance*, Elsevier, Chapter 13, Vol. 1, pp. 803–887.
- [12] Campbell, J.Y. & Cochrane, J.H. (1999). By force of habit, *Journal of Political Economy* **107**(2), 205–251.
- [13] Chien, Y.L. & Lustig, H.N. (2008). The market price of aggregate risk and the wealth distribution, forthcoming in the *Review of Financial Studies*.
- [14] Cochrane, J.H. & Hansen, L.P. (1992). Asset pricing explorations for macroeconomics, *NBER Macroeconomics Annual* **7**, 115–165.
- [15] Constantinides, G.M. (1990). Habit formation: a resolution of the equity premium puzzle, *Journal of Political Economy* **98**(3), 519–543.
- [16] Constantinides, G.M. & Duffie, D. (1996). Asset pricing with heterogeneous consumers, *Journal of Political Economy* **104**(2), 219–240.
- [17] Debreu, G. (1954). Valuation equilibrium and Pareto optimum, *Proceedings of the National Academy of Sciences* **40**(7), 588–592.
- [18] Epstein, L. & Zin, S. (1989). Substitution, risk aversion and the temporal behavior of consumption and asset returns: A theoretical framework, *Econometrica* **57**(4), 937–969.
- [19] Fama, E.F. & French, K.R. (1992). The cross-section of expected stock returns, *Journal of Finance* **47**, 427–465.
- [20] Gallant, A.R., Hansen, L.P. & Tauchen, G. (1990). Using conditional moments of asset payoffs to infer the volatility of intertemporal marginal rates of substitution, *Journal of Econometrics* **45**(1–2), 141–179.
- [21] Garcia, R., Renault, E. & Semenov, A. (2006). Disentangling risk aversion and intertemporal substitution through a reference utility level, *Finance Research Letters* **3**, 181–193.

- [22] Gibbons, M.R., Ross, S.A. & Shanken, J. (1989). A test of the efficiency of a given portfolio, *Econometrica* **57**(5), 1121–1152.
- [23] Hansen, L.P. (1982). Large sample properties of generalized method of moments estimators, *Econometrica* **50**(4), 1029–1054.
- [24] Hansen, L.P. (2008). Modeling the long run: valuation in dynamic stochastic economies, *Fisher-Schultz Lecture at the 2006 Meetings of the Econometric Society*, Vienna, Austria, 2006.
- [25] Hansen, L.P., Heaton, J. Lee, J. & Roussanov, N. (2007). *Handbook of Econometrics*, Intertemporal substitution and risk aversion, in J.J. Heckman & E.E. Leamer, eds, Handbook of Econometrics, Elsevier, Chapter 61, Vol. 6.
- [26] Hansen, L.P., Heaton, J. & Luttmer, E.G.J. (1995). Econometric evaluation of asset pricing models, *Review of Financial Studies* **8**(2), 237–274.
- [27] Hansen, L.P., Heaton, J. & Yaron, A. (1996). Finitesample properties of some alternative gmm estimators, *Journal of Business and Economic Statistics* **14**(3), 262–280.
- [28] Hansen, L.P. & Jagannathan, R. (1991). Implications of security market data for models of dynamic economies, *Journal of Political Economy* **99**(2), 225–262.
- [29] Hansen, L.P. & Jagannathan, R. (1997). Assessing specification errors in stochastic discount factor models, *Journal of Finance* **52**(2), 557–590.
- [30] Hansen, L.P. & Richard, S.F. (1987). The role of conditioning information in deducing testable restrictions implied by dynamic asset pricing models, *Econometrica* **50**(3), 587–614.
- [31] Hansen, L.P., Sargent, T.J. & Tallarini, T.D. Jr. (1999). Robust permanent income and pricing, *The Review of Economic Studies* **66**(4), 873–907.
- [32] Hansen, L.P. & Scheinkman, J.A. (2009). Long-term risk: an operator approach, *Econometrica* **77**(1), 177–234.
- [33] Hansen, L.P. & Singleton, K.J. (1982). Generalized instrumental variables estimation of nonlinear rational expectations models, *Econometrica* **50**(5), 1269–1286.
- [34] Harrison, J.M. & Kreps, D.M. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **20**, 381–408.
- [35] He, H. & Modest, D.M. (1995). Market frictions and consumption-based asset pricing, *Journal of Political Economy* **103**(1), 94–117.
- [36] Heaton, J. (1995). An empirical investigation of asset pricing with temporally dependent preference specifications, *Econometrica* **63**(3), 681–717.
- [37] Jagannathan, R., Soulakis, G. & Wang, Z. (2009). The analysis of the cross section of security returns, in forthcoming in the *Handbook of Financial Econometrics*, Y. Ait-Sahalia & L.P. Hansen, Elsevier.
- [38] Kehoe, T.J. & Levine, D.K. (1993). Debt-constrained asset markets, *Review of Economic Studies* **60**(4), 865–888.

- [39] Kocherlakota, N.R. (1996). Implications of efficient risk sharing without commitment, *Review of Economic Studies* **63**(4), 595–609.
- [40] Kocherlakota, N. & Pistaferri, L. (2009). Asset pricing implications of Pareto optimality with private information, *Journal of Political Economy* **117**(3), 555–590.
- [41] Kreps, D.M. & Porteus, E.L. (1978). Temporal resolution of uncertainty and dynamic choice, *Econometrica* **46**(1), 185–200.
- [42] Lucas, R.E. (1978). Asset prices in an exchange economy, *Econometrica* **46**(6), 1429–1445.
- [43] Luttmer, E.G.J. (1996). Asset pricing in economies with frictions, *Econometrica* **64**(6), 1439–1467.
- [44] MacKinlay, A.C. & Richardson, M.P. (1991). Using generalized method of moments to test mean-variance efficiency, *Journal of Finance* **46**, 511–527.
- [45] Menzly, L., Santos, T. & Veronesi, P. (2004). Understanding predictability, *Journal of Political Economy* **112**(1), 1–47.
- [46] Rogers, L.C.G. (1998). The origins of risk-neutral pricing and the Black-Scholes formula, in *Risk Management and Analysis*, C.O. Alexander, ed., Wiley, New York, Chapter 2, pp. 81–94.
- [47] Rogerson, W.P. (1985). The first-order approach to principal-agent problems, *Econometrica* **53**(6), 1357–1367.

- [48] Rosenberg, J.V. & Engle, R.F. (2002). Empirical pricing kernels, *Journal of Financial Economics* **64**(3), 341–372.
- [49] Ross, S.A. (1976). The arbitrage theory of capital asset pricing, *Journal of Economic Theory* **13**, 341–360.
- [50] Rubinstein, M. (1976). The valuation of uncertain income streams and the valuation of options, *Bell Journal* **7**, 407–425.
- [51] Snow, K. (1991). Diagnosing asset pricing using the distribution of asset returns, *Journal of Finance* **46**(3), 955–983.
- [52] Tallarini, T.D. (2000). Risk-sensitive real business cycles, *Journal of Monetary Economics* **45**(3), 507–532.
- [53] Weil, P. (1990). Nonexpected utility in macroeconomics, *The Quarterly Journal of Economics* **105**(1), 29–42.

# **Related Articles**

**Arrow–Debreu Prices**; **Complete Markets**; **Fixed Mix Strategy**; **Fundamental Theorem of Asset Pricing**; **Stochastic Discount Factors**.

LARS PETER HANSEN & ERIC RENAULT
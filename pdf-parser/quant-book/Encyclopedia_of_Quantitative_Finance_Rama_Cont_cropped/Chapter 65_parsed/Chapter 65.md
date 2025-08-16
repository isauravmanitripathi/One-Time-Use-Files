# **Real Options**

Real options theory is about decision making and value creation in an uncertain world. It owes its success to its ability to reconcile frequently observed investment behaviors that are seemingly inconsistent with rational choices at the firm level. For instance, Dixit [15] uses real options to explain why firms undertake investments only if they expect a yield in excess of a required hurdle rate, thus violating the Marshallian theory of long- and short-run equilibria.a*,*<sup>b</sup> This is because, relative to a setting in which there is no uncertainty, unforeseeable future payouts discourage commitment to a project unless the expected profitability of the project is sufficiently high. The real options methodology allows to identify and value risky investments and, under certain conditions, to even take advantage of uncertainty. Indeed, as we shall see, this valuation approach insures investments against possible adverse outcomes while retaining upside potential.c

## **Definition of a Real Option**

A real option gives its holder the right, but not the obligation, to take an action (e.g., deferring, expanding, contracting, or abandoning) for a specified price, called the *exercise*—or *strike*—*price*, on or before some specified future date. We can identify at least six factors that affect the value of a real option: the value of the underlying risky asset (i.e., the project, investment, or acquisition); the exercise price; the volatility of the value of the underlying asset; the time to expiration of the option; the interest rate; and the dividend rate of the underlying asset (i.e., the cash outflows or inflows over the life of the option). If the value of the underlying project, its standard deviation, or the time to expiration increase, so too does the value of the option. The value of the (call) option also increases if the risk-free rate of interest goes up. Lost dividends decrease the value of the option.d A higher exercise price reduces (augments) the value of a call (put) option.e

The quantitative origins of real options derive from the seminal work of Black and Scholes [2] and Merton [32] on financial options pricing (*see* **Black–Scholes Formula**). These roots are evident in the assumptions that trading and decision making take place in continuous time and that the underlying sources of uncertainty follow Brownian motions. Even though these assumptions may be unsuitable in some corporate contexts, they permit to derive precise theoretical solutions, thereby proving to be essential.f*,*<sup>g</sup> The focus of this earlier literature has been on valuing individual real options: the option to expand a project, for instance, is an American call option (*see* **American Options**). So is a deferral option that gives a firm the right to delay the start of a project. The option to abandon a project, or to scale back by selling a fraction of it for a fixed price, is formally an American put (*see* **American Options**). Real-world projects, however, are often more complex in that they involve a collection of real options, whose values may interact. The recent development in financial options interdependencies has enabled a smoother transition from a theoretical stage to an application stage.h Margrabe's [29] valuation of an option to exchange one risky asset for another (*see* **Margrabe Formula**) finds immediate application in the modeling of switching options, which allow a firm to switch between two modes of operation. Geske [19] values options on options—called *compound options* —which may be applied to growth opportunities that become available only if earlier investments are undertaken. Phased investments belong to this category. Thus, almost paradoxically, in this relatively new field of research, the mathematically most complex models, which apply sophisticated contingent claims analysis techniques, entail a great wealth of factual applications.i Moreover, numerous studies show that real options represent a sizable fraction of a firm's value; both Kester [25] and Pindyck [35], for instance, estimate that the value of a firm's growth options is more than half its market value of equity if demand volatility exceeds 20%. For this reason, the theory of real options has gained significant importance among management practitioners whose choices determine the success or failure of their enterprises. Amram and Kulatilaka [1] collect several case studies to show practitioner audiences how real options can improve capital investment planning and results. In particular, they list three real options characteristics that are of great use to managers: (i) options payoffs are contingent on the manager's decisions; (ii) options valuations are aligned with financial market valuations; and (iii) options thinking can be used to design and manage strategic investments proactively. The real options paradigm, however, is only the last stage in the evolution of valuation models. The traditional approach to valuing investment projects, which owes its origins to John Hicks and Irving Fisher, is based on net present value. This technique involves discounting expected net cash flows from a project at a discount rate that reflects the risk of those cash flows, called the *risk-adjusted* discount rate. Brennan and Trigeorgis [8] characterize this first-phase models as *static*, or *mechanistic*. The second-phase models are *controllable* cash-flow models, in which projects can be managed actively in response to the resolution of exogenous uncertainties. Since they ignore strategic investment, both first- and second-phase models often lead to suboptimal decisions. *Dynamic, gametheoretic* options models assume that projects can be managed actively, instead.j These models take into account not only the resolution of exogenous uncertainties but also the actions of outside parties. For this reason, an area of immense importance within game-theoretic options models concerns market competition and strategy.

Strategic firm interactions are isomorphic to a portfolio of real options.k Furthermore, the payouts of a project (as well as its value) can be seen as the outcome of a game among the inside agent, outside agents, and nature. Dixit [14] and Williams [40] were the first to consider real options within an equilibrium context. Smit and Ankum [37], among others, study competitive reactions within a game-theoretic framework under different market structures. In the same line of research is Grenadier's [21] analysis of a perfectly competitive real-estate market with stochastic demand and time to build.l

## **Solution of the Basic Model**

Besides particular cases, all investment expenditures have two important characteristics. First, they are at least partly irreversible, and second, they can be delayed so that the firm has the opportunity to wait for new information to arrive before committing any resources.

The most basic continuous-time model of irreversible investment was originally developed by McDonald and Siegel [31]. In their problem, a firm must decide when to invest in a single risky project, denoted by *V* , with a fixed known cost *I* . The project is assumed to follow a geometric Brownian motion with expected return and volatility indicated by *µ* and *σ*, respectively. The project's payout rate equals *δ*. Formally, the process can be written as

$$\frac{\mathrm{d}V}{V} = (\mu - \delta) \,\mathrm{d}t + \sigma \,\mathrm{d}z \tag{1}$$

where d*z* is the increment of a Wiener process and *(*d*z)*<sup>2</sup> = d*t*. <sup>m</sup>*,*<sup>n</sup> In addition, denote the value of the firm's investment opportunity (its option to invest) by *F (V )*. It can be shown that the optimal rule is to invest at the date *τ* <sup>∗</sup> when the project's value first exceeds a certain optimal threshold *V* <sup>∗</sup>. This rule maximizes

$$F(V) = \max_{\tau} E[(V_{\tau} - I)e^{-\mu\tau}], \quad V_0 = V \qquad (2)$$

over all possible stopping times *τ* , where *E* is the expectation operator. Prior to undertaking the project the only return to holding the investment option is its capital appreciation, so that

$$\mu F(V) dt = E[dF(V)] \tag{3}$$

Expanding d*F (V )* using Ito's lemma yields ˆ

$$dF(V) = F'(V) dV + \frac{1}{2}F''(V)(dV)^2 \tag{4}$$

where primes indicate derivatives. Lastly, substituting equation (1) in (4) and taking expectations on both sides gives

$$\frac{1}{2}\sigma^2 V^2 F''(V) + (\mu - \delta) V F'(V) - \mu F(V) = 0$$
(5)

Equation (5) must be solved simultaneously for the project value *F (V )* and the optimal investment threshold *V* <sup>∗</sup>, subject to three boundary conditions:

$$F(0) = 0 \tag{6}$$

$$F(V^*) = V^* - I \tag{7}$$

$$F'(V^*) = 1\tag{8}$$

Equation (6) is equivalent to stating that the investment option is worthless when the project's outcome is null. Equations (7) and (8) indicate the payoff and marginal value associated with the optimum. To derive *V* <sup>∗</sup>, we must guess a functional form that satisfies equation (5) and verify if it works. In particular, if we take  $F(V) = AV^{\beta}$ , then

$$V^* = \frac{\beta I}{\beta - 1} \tag{9}$$

and

$$\beta = \frac{1}{2} - \frac{\mu - \delta}{\sigma^2} + \sqrt{\left(\frac{\mu - \delta}{\sigma^2} - \frac{1}{2}\right)^2 + \frac{2\mu}{\sigma^2}} \quad (10)$$

The optimal rule is to invest when the value of the project exceeds the cost by a factor  $\frac{\beta}{\beta-1} > 1$ .<br>This result is in contrast with net present value, which prescribes to invest as long as the value of the project exceeds the cost  $(V^* = I)$ . However, since the latter rule does not account for uncertainty and irreversibility, it is incorrect and it leads to suboptimal decisions.

Furthermore, as it is apparent from the solution, the higher the risk of the project, measured by  $\sigma$ , the larger are the value of the option and the opportunity cost of investing. Increasing values of the growth rate,  $\mu$ , also cause  $F(V)$  and  $V^*$  to be higher. On the other hand, larger expected payout rates,  $\delta$ , lower both  $F(V)$  and  $V^*$  as holding the option becomes more expensive.

Dixit and Pindyck [16] show how the optimal investment rule can be found by using both dynamic programming (as it is done above) and contingent claims analysis.<sup>o</sup>

Contingent claims methods require one important assumption: stochastic changes in the value of the project must be *spanned* by existing assets in the economy (see Complete Markets). Specifically, capital markets must be sufficiently *complete* so that one could find an asset, or construct a dynamic portfolio of assets, the price of which is perfectly correlated with the value of the project (see Risk**neutral Pricing**). $^{p,q}$  This assumption allows properly taking into account all the flexibility (options) that the project might have and using all the information contained in market prices (e.g., futures prices) when such prices exist.<sup>r</sup> If the sources of uncertainty in a project are not traded assets (examples of which are product demand uncertainty, geological uncertainty, technological uncertainty, cost uncertainty, etc.), an equilibrium model of asset prices can be used to value the contingent claim.<sup>s</sup>

### **Numerical Methods in Real Options**

In practice, most real option problems must be solved using numerical methods. Until recently, these methods were so complex that only few companies found it practical to use them when formulating operating strategies. However, advances in both computational power and understanding of the techniques over the last 20 years have made it feasible to apply real options thinking to strategic decision making. Numerical solutions give not only the value of the project but also the optimal strategy for exercising the options.<sup>t</sup> The simplest real option problems involving one or two state variables can be more conveniently solved using binomial or trinomial trees in one or two dimensions (see Finite Element Methods).<sup>u</sup> When a problem involves more state variables, perhaps path dependent, the more practical solution is to use Monte Carlo simulation methods (see Monte **Carlo Simulation**). $^{v,w}$  In order to do so, we use the assumption that properly anticipated prices (or cash flows) fluctuate randomly. Regardless of the pattern of cash flows that a project is expected to have, the changes in its present value will follow a random walk. This theorem, attributable to Paul Samuelson, allows us to combine any number of uncertainties by using Monte Carlo techniques, and to produce an estimate of the present value of a project conditional on the set of random variables drawn from their underlying distributions. More generally, there are two types of numerical techniques for option valuation: (i) those that approximate the underlying stochastic processes directly and (ii) those approximating the resulting partial differential equation. The first category includes lattice approaches and Monte Carlo simulations. Examples of the second category include numerical integration (see **Quadrature Methods**); and the implicit/explicit finite difference schemes (see Finite Difference Methods for Barrier Options; Finite Difference Methods for Early **Exercise Options**) used by Brennan [6], Brennan and Schwartz [7], and Majd and Pindyck [28], among others.

#### Conclusions

The application of option concepts to value real assets has been an important growth area in the theory and practice of finance. The insights and techniques derived from option pricing have proven capable of quantifying the managerial operating flexibility and strategic interactions thus far ignored by conventional net present value and other quantitative approaches. This flexibility represents a substantial part of the value of many projects and neglecting it can undervalue investments and induce a misallocation of resources. By explicitly incorporating management flexibility into the analysis, real options have provided the tools for properly valuing corporate resources and capital budgeting.

## **End Notes**

a*.* Marshall's [30] analysis states that if price exceeds longrun average cost, then existing firms expand and new ones enter a business.

b*.* Symmetrically, firms often do not exit a business for lengthy periods, even after the price falls substantially below long-run average cost. This phenomenon is dubbed *hysteresis*.

c*.* Amram and Kulatilaka [1], Brennan and Trigeorgis [8], Copeland and Antikarov [10], Dixit and Pindyck [16], Grenadier [21], Schwartz and Trigeorgis [36], and Smit and Trigeorgis [38] represent core reference volumes on real investment decisions under uncertainty. The survey article by Boyer *et al.* [4] is a noteworthy collection of all most notable contributions to the literature on strategic investment games, from the pioneering works of Gilbert and Harris [20] and Fudenberg and Tirole [18] to more recent contributions.

d*.* For a thorough examination of the variables driving real options' analysis, the reader is referred to [10], Chapter 1. e*.* An interesting example on the effect of an option's exercise price on its value is presented by Moel and Tufano [33]. They study the bidding for rights to explore and develop a copper mine in Peru. A peculiar aspect of the transaction is the nature of the bidding rules that bidders were required to follow by the Peruvian government. Each bid was required to specify the minimum amount that the bidder would spend on developing the property if they decided to go ahead after exploration. This is equivalent to allowing the bidders to specify the exercise price of their development option. This structure gave rise to incentives that affected the amount that firms would offer, thus inducing successful bidders to make uneconomic investments.

f*.* Boyarchenko and Levendorskii [3] relax these assumptions and show how to analyze firm decisions in discrete time.

g*.* Cox, Ross, and Rubinstein's [12] binomial approach enables a more simplified valuation of options in discrete time.

h*.* Detemple [13] provides a complete treatment of American-style derivatives pricing. He analyzes in detail both plain and exotic contingent claims and presents recent results on the numerical computation of optimal exercise boundaries, hedging prices, and hedging portfolios.

i*.* Flexible manufacturing, natural resource investments, land development, leasing, large-scale energy projects, research and development, and foreign investment are all examples of real options cases.

j*.* Trigeorgis and Mason [39] remark that option valuation can be seen as a special version of decision tree analysis. Decision scientists propose the use of decision tree analysis [34] to capture the value of operating flexibility associated with many projects.

k*.* Luerhman [27] explains how a business strategy compares to a series of options more than to a single option. *De facto*, executing a strategy almost always involves making a sequence of decisions: some actions are taken immediately, while others are deliberately deferred.

l*.* The time-to-build and continuous-time features of Grenadier's [21] model translate into an infinite state space. Despite this, he is able to determine the optimal construction rules by engineering an artificial economy with a finite state space in which the equilibrium strategy is identical to that of the true economy.

m*.* According to equation (1), the current project value is known but its future values are uncertain.

n*.* Chapters 3 and 4 in [16] provide a thorough overview of the mathematical tools necessary to study investment decision using a continuous-time approach.

o*.* Although equivalent, the two methodologies are conceptually rather different: while the former lies on the option's value satisfying the Bellman equation, the latter is founded on the construction of a risk-free portfolio formed by a long position in the firm's option and a short position in units of the firm's project. Chapter 5 in [16] presents a detailed explanation, along with a guided derivation, of the optimal rule obtained on adopting each technique.

p*.* Duffie [17] gives great emphasis to the implications of complete markets for asset pricing under uncertainty.

q*.* Harrison and Kreps [22], Harrison and Pliska [23], and others have shown that, in complete markets, the absence of arbitrage implies the existence of a probability distribution such that securities are priced on the basis of their discounted (at the risk-free rate) expected cash flows, where expectation is determined under the *riskneutral probability measure*. If all risks can be hedged, this probability is unique. The critical advantage of working in the risk-neutral environment is that it is a convenient environment for option pricing.

r*.* The reader is referred to [36] for a more rigorous discussion on the application of contingent claims analysis to determine a project's optimal operating policy.

s*.* See [11] for the derivation of a fundamental partial differential equation that must be satisfied by the value of all contingent claims on the value of state variables that are not traded assets.

t*.* Broadie and Detemple [9] conduct a careful evaluation of the many methods for computing American option prices.

u*.* Boyle [5] shows how lattice frameworks can be extended to handle two state variables.

v*.* In the last few years, methods have been developed, which allow using simulations for solving American-style options. For example, Longstaff and Schwartz [26] developed a least-squares Monte Carlo approach to compare the value of immediate exercise with the conditional expected value from continuation.

w*.* Hull and White [24] suggest a control variate technique to improve computational efficiency when a similar derivative asset with an analytic solution is available.

## **References**

- [1] Amram, M. & Kulatilaka, N. (1999). *Real Options: Managing Strategic Investment in an Uncertain World*, Harvard Business School Press, Boston, MA.
- [2] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *The Journal of Political Economy* **18**(3), 637–654.
- [3] Boyarchenko, S. & Levendorskii, S. (2000). Entry and exit strategies under Non-Gaussian distributions, in *Project Flexibility, Agency, and Competition*, M. Brennan & L. Trigeorgis, eds, Oxford University Press, Inc., New York, NY, pp. 71–84.
- [4] Boyer, R., Gravelle, E. & Lasserre, P. (2004). *Real Options and Strategic Competition: A Survey*. Working Paper.
- [5] Boyle, P. (1988). A lattice framework for option pricing with two state variables, *The Journal of Financial and Quantitative Analysis* **23**(1), 1–12.
- [6] Brennan, M. (1979). The pricing of contingent claims in discrete time models, *The Journal of Finance* **34**(1), 53–68.
- [7] Brennan, M. & Schwartz, E. (2001). Finite differences methods and jump processes arising in the pricing of contingent claims: a synthesis, in *Real Options and Investment Under Uncertainty: Classical Readings and Recent Contributions*, E. Schwartz & L. Trigeorgis, eds, The MIT Press, Cambridge, MA, pp. 559–570.
- [8] Brennan, M. & Trigeorgis, L. (2000). *Project Flexibility, Agency, and Competition*, Oxford University Press, Inc., New York, NY.
- [9] Broadie, M. & Detemple, J. (1996). American option valuation: new bounds, approximations, and a comparison of existing methods, *The Review of Financial Studies* **9**(4), 1211–1250.
- [10] Copeland, T. & Antikarov, V. (2001). *Real Options: A Practitioner's Guide*, W.W. Norton & Company, New York.
- [11] Cox, J., Ingersoll, J. & Ross, S. (1985). An intertemporal general equilibrium model of asset prices, *Econometrica* **53**(2), 363–384.

- [12] Cox, J., Ross, S. & Rubinstein, M. (1979). Option pricing: a simplified approach, *The Journal of Financial Economics* **7**(3), 229–263.
- [13] Detemple, J. (2005). *American-Style Derivatives: Valuation and Computation*, Chapman & Hall/CRC.
- [14] Dixit, A. (1989). Entry and exit decisions under uncertainty, *The Journal of Political Economy* **97**(3), 620–638.
- [15] Dixit, A. (1992). Investment and hysteresis, *The Journal of Economic Perspectives* **6**(1), 107–132.
- [16] Dixit, A. & Pindyck, R. (1994). *Investment Under Uncertainty*, Princeton University Press, Princeton, NJ.
- [17] Duffie, D. (1996). *Dynamic Asset Pricing Theory*, Princeton University Press, Princeton, NJ.
- [18] Fudenberg, D. & Tirole, J. (1985). Preemption and rent equalization in the adoption of new technology, *The Review of Economic Studies* **52**(3), 383–401.
- [19] Geske, R. (1979). A note on analytical valuation formula for unprotected American call options on stocks with known dividends, *The Journal of Financial Economics* **7**, 375–380.
- [20] Gilbert, R. & Harris, R. (1984). Competition with lumpy investment, *RAND Journal of Economics* **15**(2), 197–212.
- [21] Grenadier, S. (2000). Strategic options and product market competition, in *Project Flexibility, Agency, and Competition*, M. Brennan, & L. Trigeorgis, eds, Oxford University Press, Inc., New York, NY, pp. 275–296.
- [22] Harrison, M. & Kreps, D. (1979). Martingales and arbitrage in multiperiod securities markets, *The Journal of Economic Theory* **20**(3), 381–408.
- [23] Harrison, J. & Pliska, S. (1981). Martingales and stochastic integrals in the theory of continuous trading, *Stochastic Processes and Their Applications* **11**, 215–260.
- [24] Hull, J. & White, A. (1988). The use of control variate technique in option pricing, *The Journal of Financial and Quantitative Analysis* **23**(3), 237–251.
- [25] Kester, W. (2001). Today's options for tomorrow's growth, in *Real Options and Investment Under Uncertainty: Classical Readings and Recent Contributions*, E. Schwartz & L. Trigeorgis, eds, The MIT Press, Cambridge, MA, pp. 33–46.
- [26] Longstaff, F. & Schwartz, E. (2001). Valuing American options by simulations: a simple least-squares approach, *The Review of Financial Studies* **14**(1), 113–147.
- [27] Luehrman, T. (2001). Strategy as a portfolio of real options, in *Real Options and Investment Under Uncertainty: Classical Readings and Recent Contributions*, E. Schwartz & L. Trigeorgis, eds, The MIT Press, Cambridge, MA, pp. 385–404.
- [28] Majd, S. & Pindyck, R. (1987). Time to build, option value, and investment decisions, *The Journal of Financial Economics* **18**(1), 7–27.
- [29] Margrabe, W. (1978). The value of an option to exchange one asset for another, *The Journal of Finance* **33**(1), 177–186.
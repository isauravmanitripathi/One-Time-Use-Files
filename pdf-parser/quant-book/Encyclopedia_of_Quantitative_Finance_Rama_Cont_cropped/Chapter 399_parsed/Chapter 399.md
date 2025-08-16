# **Life Insurance**

Finance and life insurance have a lot in common. Life insurance contracts specify an exchange of streams of payments between the insurance company and the contract holder. These payment streams may cover the lifetime of the contract holder. Therefore, time valuation of money is crucial for any measurement of payments due in the past as well as in the future. Life insurance companies never keep their money idle, and accumulation and distribution of capital gains are always a part of the insurance business. With respect to the future, appropriate discounting of contractual obligations improves the estimates of liabilities.

The subject matter of life insurance draws on a wide set of mathematical disciplines including probability theory, stochastic processes, statistics, economics, and mathematical finance. However, in addition, less positivistic areas such as accounting and law, in general, and insurance accounting, contractual law, and regulatory law, in particular, often play important roles when theory meets practice. The broad title covers a survey of the mathematics of life insurance rather than life insurance in general.

At the end of the day, life insurance is a betting game on life history events such as death, survival, and disability. Betting in this context is very different from betting on horses or football since the benefit is paid conditional on a life history event that has already caused financial distress of the betting party: one buys a coverage against death to protect one's dependants—typically spouse and children—financially against the loss of future income upon death; one buys life annuities to protect oneself financially against living long by stretching out capital holdings until an uncertain time of death; and one buys a coverage against disability to protect oneself and one's dependants financially against the loss of income upon disability. In this respect, insurance and pension saving are betting games that hedge the personal financial position against financially adverse events. However, this explains why the society encourages its members to play this betting game (partly in contrast to other betting games) under slightly regulated conditions: it has a stabilizing effect on the financial position of individuals and families and thereby on the society as a whole.

The insurance companies and pension funds are the counterparts of this betting game. This exposition deals, first of all, with the technical toolbox they use in order to provide relevant, fair, and reliable bets. However, it also deals with the enlargement of the toolbox caused by the integration of mathematical finance as a part of life insurance mathematics. New paradigms lead to new answers to what the terms relevant, fair, and reliable mean at all. However, the enlightenment is not one way: some of the classical tools of life insurance are relevant to modern finance and we provide an example.

The section Modeling of Payment Streams presents the classical modeling framework for life history risk and the payment streams linked to it, first in the so-called survival model and second in a multistate model. The section Valuation of Payment Streams deals with the valuation of and fairness criteria for these payment streams. First, we evaluate on the basis of classical actuarial assumptions and then discuss how the financial market helps to relax some of these assumptions. Finally, we exemplify by credit risk modeling and valuation, how methods of classical life insurance can also contribute to a structured view on modern financial topics. The section Design of Payment Streams formalizes the so-called participation feature in typical practical arrangements that add a dimension to the risk sharing taking place in an insurance contract. We distinguish between the classical with-profit construction, where design and decision is primarily a matter for the insurance company, and the more modern unit-link, where design and decision, to a larger extent, is a matter for the policy holder. Finally, in the section Management of Payment Streams, we focus on these decision processes. Optimal decision making on both sides of the balance scheme is the essence of asset-liability management (ALM). We conclude by relating these decision processes to those in the classical investment–consumption problem of personal finance.

## **Modeling of Payment Streams**

#### *The Survival Model Payment Streams*

The payments of an insurance contract can be formalized by a payment process *B*, where *B (t)* represents the accumulated payments from the insurance company to the policy holder until time *t*. The payments are then the increments *(*d*B (t))t*<sup>≥</sup><sup>0</sup> and we have that

$$B(t) = \int_{0-}^{t} \mathrm{d}B(s) \tag{1}$$

where, by definition,  $\int_0^t = \int_{(0,t]}$  and  $\int_{0-}^t = \int_{[0,t]}$ .<br>Thus, payments going from the insurance company to the policy holder (benefits) appear in  $B$ as positive increments, whereas payments going from the policy holder to the insurance company (premiums/contributions) appear in  $B$  as negative increments. In the formation of  $B$ , we have assumed that there are no payments before inception of the contract at time 0, that is,  $B(0-) = 0$ . We specify the payments in a continuous-time framework. We denote by  $T$  the time of death of a policy holder. To formalize the connection between payments and the life history of the insured, we introduce the indicator process  $I(t)$ . This process indicates whether the insured is alive in the sense that  $I(t) = 1$  if the insured is alive at time t and  $I(t) = 0$  if the insured is dead at time t. The process  $Z(t) = 1 - I(t)$  indicates whether the insured is dead, which is illustrated in Figure 1.

We also introduce a counting process  $(N(t))_{t>0}$ , counting the number of deaths of the insured (equals 0 or 1) over [0, t]. Note that  $N = Z = 1 - I$ . Finally, we introduce the notation  $(\varepsilon^{u}(t))_{t>0}$  for the deterministic indicator process, indicating that  $t$  exceeds u, that is,  $\varepsilon^{u}(t) = 1 \, [t > u]$ . Fixing a time horizon  $n$  for the insurance contract and introducing a retirement time  $m < n$ , most insurance payment processes in a survival model are given by a payment process  $B$  in the following form:

$$\begin{aligned} \mathsf{d}B\left(t\right) &= \Delta B^{0}(t)\mathsf{d}\varepsilon^{0}(t) + b^{0}(t)I(t)\mathsf{d}t + b^{01}(t) \\ &\quad \times \mathsf{d}N(t) + \Delta B^{0}(t)I(t)\mathsf{d}\varepsilon^{m}(t), \quad t \leq n \end{aligned} \tag{2}$$

Here,  $\Delta B^{0}$  (0) is a possible single premium (negative) triggered at time 0,  $b^0(t)$  is an annuity benefit rate (positive) or a level premium rate (negative) at time  $t$ , both conditional on survival by multiplication of I,  $b^{01}(t)$  is a death benefit triggered upon death before time *n*, and  $\Delta B^{0}(m)$  is a pension sum benefit triggered at time  $m$  upon survival to time  $m$ . In Table 1, we specify the elements in some standard forms of benefit and premium payment processes.

To have an idea about the future prospects of  $B$ , we need to specify the distribution of  $T$ . We form the

![](_page_1_Figure_6.jpeg)

Figure 1 Survival model

survival function  $\overline{F}$ , the lifetime distribution function  $F$ , and the death density, respectively,

$$F(t) = P(T > t) = P(I(t) = 1)$$
  

$$F(t) = P(T \le t) = P(I(t) = 0) = 1 - \overline{F}(t)$$
  

$$f(t) = \frac{d}{dt}F(t)$$
(3)

The distribution of  $T$  is typically parameterized by the hazard rate conventionally denoted by  $\mu$  (Greek  $m$  for mortality rate) and defined as the death rate conditional on survival,

$$\mu(t) dt = P(t \le T < t + dt | T > t)$$
$$= \frac{f(t) dt}{\overline{F}(t)} = -\frac{\overline{F}'(t) dt}{\overline{F}(t)} \tag{4}$$

This forms a differential equation for  $\overline{F}$  with initial condition  $\overline{F}(0) = 1$ . Its solution  $\overline{F}$  and the resulting  $F$  and  $f$  are given as

$$\overline{F}(t) = e^{-\int_0^t \mu(s)ds}, \quad F(t) = 1 - e^{-\int_0^t \mu(s)ds},$$
  
$$f(t) = e^{-\int_0^t \mu(s)ds} \mu(t) \tag{5}$$

thereby forming the elementary distribution characteristics in terms of the mortality rate. One of the advantages from representing these characteristics in terms of the mortality rate is that the corresponding quantities conditional on survival until a given age, say x, have the same structure with  $\mu(t)$  replaced by  $\mu$  (x + t), for example,

$$P(T > x + t | T > x) = e^{-\int_0^t \mu(x+s)ds} \qquad (6)$$

This is useful when the insurance company sells a contract to an  $x$ -year old and takes into account the fact that he/she survived so far. There are many candidates for the mortality rate that can take any form as long as  $\mu(t) > 0$  and it integrates to infinity over  $[0, \infty)$ . The Gompertz–Makeham mortality rate

$$\mu\left(t\right) = \alpha + \beta e^{\gamma t} \tag{7}$$

allows for a nonage-dependent effect  $\alpha$  (death from accident) and an exponential age-dependent effect (death from deterioration of health over time). This is classic due to its good fit to data relative to its low number of parameters. In the Danish mortality law

|                                 | B0 (0)<br> | b0 (t)                                           | b01 (t)   | B0 (m)<br> |
|---------------------------------|------------|--------------------------------------------------|-----------|------------|
| Benefits                        |            |                                                  |           |            |
| Pure endowment                  | 0          | 0                                                | 0         | 1          |
| Term insurance                  | 0          | 0                                                | 1 [t ≤ m] | 0          |
| Endowment insurance             | 0          | 0                                                | 1 [t ≤ m] | 1          |
| Temporary life annuity          | 0          | 1 [t ≤ n]                                        |           |            |
| Deferred temporary life annuity | 0          | 1 [m <t n]<="" td="" ≤=""><td></td><td></td></t> |           |            |
| Premiums                        |            |                                                  |           |            |
| Single premium                  | −1         |                                                  |           |            |
| Level premium                   |            | −1 [t ≤ m]                                       |           |            |

G82 for Danish males, the parameters are *α* = 5 × 10<sup>−</sup><sup>4</sup>*, β* = 7*.*5858 × 10<sup>−</sup><sup>5</sup>*,* and *γ* = log *(*1*.*09144*).*

#### *The Multistate Model Payment Streams*

Although the payment process in equation (2) formalizes a number of standard forms of benefits and premium payment processes, there is a number of contracts that are not covered. An example is a contract where the level premium is not paid during periods of disability, that is, the level premium is contingent on the state of health. Such so-called premium waiver conditions and different types of disability annuities can be covered by extending the survival model with a third state, "disabled" (Figure 2).

Another example is a widow's/widower's pension where the two spouses in a married couple are insured such that, for example, an annuity rate is payable in the time period where one spouse survives another. Insurances on two lives can be covered by combining two survival models (Figure 3). It is now easy to

![](_page_2_Figure_7.jpeg)

**Figure 2** Disability model

![](_page_2_Figure_9.jpeg)

**Figure 3** Dependent lives model

imagine a combination of Figures 2 and 3 into a dependent lives model with disability.

In general, we let *Z* be a process moving around in a finite number of states numbered from 0 to *J* . For such a process, we introduce two vectors of processes: the indicator process *I <sup>j</sup>* , *j* ∈ {0*,...,J* } indicates sojourn in state *j* and the counting process *N<sup>j</sup>* , *j* ∈ {0*,...,J* } counts the number of jumps into state *j* . Note that, in contrast to the survival model, the counting processes are in general not necessarily equal to 0 or 1: for example, in a disability model, the policy holder can move back and forth between "disabled" and "active". Formally,

$$I^{j}(t) = 1 [Z(t) = j]$$
  
$$N^{j}(t) = \#\{s \le t : Z(s-) \ne j, Z(s) = j\}$$
(8)

We can now formalize a set of general payment processes driven by a multistate model (by convention, *Z (*0*)* = 0),

$$\begin{split} \mathrm{d}B\left(t\right) &= \Delta B^{0}\left(t\right) \mathrm{d}\varepsilon^{0}\left(t\right) + \sum_{j} I^{j}\left(t\right) b^{j}\left(t\right) \mathrm{d}t \\ &+ \sum_{k} \sum_{j:j\neq k} I^{j}\left(t\right) b^{jk}\left(t\right) \mathrm{d}N^{k}\left(t\right) \\ &+ \sum_{j} I^{j}\left(t\right) \Delta B^{j}\left(t\right) \mathrm{d}\varepsilon^{m}\left(t\right), t \leq n \end{split} \tag{9}$$

Here, *-B*<sup>0</sup> *(*0*)* is a possible single premium (negative) triggered at time 0, *b<sup>j</sup> (t)* is a payment rate (positive or negative) at time *t* conditional on sojourn in state *j* , *-B<sup>j</sup> (t)* is a lump sum payment at time *t* conditional on sojourn in state *j* , and *bjk (t)* is an insurance sum triggered and paid upon a transition from state *j* to state *k*. Note that, for example, in the disability model,  $N^2$  counts the number of deaths no matter from which state the death occurs; but by the specification of *j* in  $b^{j2}$  and multiplication by  $I^{j}(t-)$  the death sum is allowed to depend on this information.

To have an idea about the future prospects of  $B$ , we need to specify the distribution of  $Z$ . The traditional approach is to assume the existence of deterministic piecewise continuous functions  $\mu^{jk}(t)$ such that the distribution of  $N^k$  is characterized by its intensity  $\mu^{Z(t-k)}(t)$ . This means that the probability of experiencing a transition into state  $k$ over  $[t, t + dt)$  is proportional to the time interval dt with proportionality factor  $\mu^{Z(t-k)}(t)$ . We allow this to depend on  $Z(t-)$  such that, for example, in the disability model we can have a mortality intensity that depends on whether the policy holder is active or disabled. Given that these intensities exist,  $Z$  is a time-inhomogeneous multistate Markov process.

In more general models, one loosens up the Markov assumption (see Markov Processes) and works with, for example, semi-Markov models where the transition intensity into a given state does not only depend on where the policy holder is but also depends on how much time he/she has spent there. This is relevant in the disability model, where the mortality rate from the state "disabled" at a given age may depend on the duration of disability. Even if one sticks to a Markov model for  $Z$ , the duration of sojourn may still be needed as a state process to formalize, for example, the annuity payments depending on the duration. The main example is the so-called qualification period that has to be spent as disabled before the disability annuity starts. Note carefully the difference between taking duration as a part of the probability model and taking it as a part of the state process formalizing the payment process. In the following section, we give more examples of relaxation of the Markov property of  $Z$ .

#### **Valuation of Payment Streams**

#### Classical Valuation Based on Three Assumptions

We assume that the payments are currently deposited on (or withdrawn from) an account that bears interest at rate  $r(t)$  at time  $t$ . We can now arrive at the present value at time  $t$  of a payment process by adding up the values of all elements in the payment process. We get the present value at time  $t$  of the payment process  $B$ :

$$\int_{0-}^{n} e^{-\int_{t}^{s} r(\tau)d\tau} dB(s) \qquad (10)$$

The value at time 0 of a payment process  $B$  is the net loss at time  $0$  that the insurance company faces by initiation of the contract. If the processes describing the policy holder's life history and the interest rate were known at time 0, this net loss could be calculated at time 0. To avoid losses (and gains), one should ideally balance the elements in the payment process such that the net loss is 0:

$$\int_{0-}^{n} e^{-\int_{0}^{t} r(s) ds} dB(t) = 0 \qquad (11)$$

However, the processes for the policy holder's life history and the interest rate are not known at time 0. We consider these processes as stochastic processes defined on a filtered (see **Filtrations**) probability space  $(\Omega, \mathcal{F}, \{\mathcal{F}(t)\}_{t\geq 0}, P)$  such that the present value at time 0 becomes a stochastic variable and its outcome is revealed over time. The question is how one should balance the elements of the insurance contract in that situation.

A particular situation arises if we work under the following condition.

#### Condition 1

- The insurance company issues (or can issue) 1. contracts to a "large" number  $\nu$  of individuals with identically distributed payment processes  $\left(B^{i}\right)_{i=1,\ldots,\nu}$
- For all  $i, j, i \neq j$ ,  $B^i$  is independent of  $B^j$ . 2.
- The interest rate is deterministic. 3

Then the law of large numbers applies and provides that the average gain from a contract converges toward the expected gain from a single contract (skipping the  $i$  then) as the number of contracts tends to infinity, that is,

$$\frac{1}{\nu} \sum_{i=1}^{\nu} \int_{0-}^{n} e^{-\int_{0}^{t} r(s) ds} dB^{i}(t)$$
$$\stackrel{P}{\to} E\left[\int_{0-}^{n} e^{-\int_{0}^{t} r(s) ds} dB(t)\right] \tag{12}$$

To avoid *systematic* gains (and losses), one should, therefore, balance the elements in the payment process such that the expected net gain is equal to 0,

$$E\left[\int_{0-}^{n} e^{-\int_{0}^{t} r(\tau)d\tau} \mathrm{d}B\left(t\right)\right] = 0\tag{13}$$

This balance equation formalizes the *principle* of equivalence that is fundamental in classical life insurance mathematics.

If one of the three assumptions fails, the classical principle of equivalence fails as a balancing tool for the elements in the payment process: if the insurance company cannot issue a large number of contracts, it makes no sense to draw conclusions from the law of large numbers; if  $B^i$  and  $B^j$  are dependent for  $i \neq j$ , the law of large numbers does not apply; and if the interest rate is not deterministic, we cannot deduce independence between present values from independence between payment processes. It should be mentioned, however, that Condition 1 can be weakened such that it holds only in a certain asymptotic sense.

Actually, the insurance company is interested in the valuation of the future payments not only at time 0 but also at any point in time  $t$  during the term of contract. This is required to inform the policy holder about the financial status of his/her contract and to inform the financial market and the regulators about the financial status of the insurance company. To estimate the present value of future payments at time  $t$ ,  $\int_{t}^{n} e^{-\int_{t}^{s} r(\tau)d\tau} dB(s)$ , the insurance company naturally takes into account all information it possesses at that point in time. If we work under Condition 1 and in the multistate Markov model, we can argue, by the law of large numbers, for the valuation formula:

$$E\left[\int_{t}^{n} e^{-\int_{t}^{s} r(\tau)d\tau} dB(s) \middle| Z(t) \right] = \sum_{j} I^{j}(t) V^{j}(t)$$
(14)

where

$$V^{j}(t) = E\left[\int_{t}^{n} e^{-\int_{t}^{s} r(\tau)d\tau} dB(s) \middle| Z(t) = j\right] (15)$$

These so-called statewise reserves are fundamental quantities in classical life insurance mathematics. They are characterized by a system of ordinary differential equations and presented in [6] as an inevitable tool for life insurance mathematicians. Substituting the payment process  $(9)$  into the reserve for state  $j$ , we get the differential equation (see Markov Processes):

$$\frac{\mathrm{d}}{\mathrm{d}t}V^{j}(t) = r(t)V^{j}(t) - b^{j}(t) - \sum_{k:k\neq j} \mu^{jk}(t) \left(b^{jk}(t) + V^{k}(t) - V^{j}(t)\right)$$
(16)

which holds outside  $\{0, m, n\}$ . Inside  $\{0, m, n\}$ , the conditions are

$$V^{j}(n) = 0$$
  
$$V^{j}(m-) = \Delta B^{j}(m) + V^{j}(m)$$
  
$$V^{j}(0-) = \Delta B^{j}(0) + V^{j}(0)$$
 (17)

Note that, by taking the process  $Z$  to start in state 0 by convention, we can formulate the equivalence principle in terms of the statewise reserve:

$$V^{0}(0-) = \Delta B^{0}(0) + V^{0}(0) = 0 \qquad (18)$$

The special case of the differential equation  $(16)$ that holds for the survival model was discovered by Thiele in 1875. In addition, generalized versions like, for example, equation (16) are spoken of as Thiele's differential equation. Interestingly, Thiele was actually also the first to model the Brownian motion mathematically in connection with his study of time series [5, 19]. Classical valuation formulas of classical life insurance products can be found in the textbook [4]. See also [13] for an account of different notions of reserves.

**Example 1** Let us calculate the equivalence level premium for an endowment insurance sold to an  $x$ -year old based on the assumptions above. Plugging in the elementary endowment insurance benefits and a level premium rate  $\pi$  (Greek p for premium), the equivalence principle reads

$$E\left[\int_{0-}^{m} e^{-\int_{0}^{t} r(s)ds} \left(-\pi I(t)dt + dN(t)\right) + I(t) d\varepsilon^{m}(t)\right]$$
  
$$= E\left[\int_{0-}^{m} e^{-\int_{0}^{t} r(s)ds} \left(-\pi I(t)dt + dN(t)\right) + e^{-\int_{0}^{m} r(s)ds} I(m)\right] = 0 \qquad (19)$$

where expectation is actually conditional expectation given that the policy holder is  $x$  years old, that is,  $T > x$ . This forms one equation (the principle of equivalence) with one unknown  $(\pi)$  and its solution is called the equivalence premium. By plugging in the characteristics of the lifetime distribution in equation  $(5)$  and collecting terms, we get

with the terminal condition given by definition,

$$V^0(m-) = 1 \tag{24}$$

and the initial condition as a result of inserting the equivalence premium calculated above,

$$V^0(0) = 0 \tag{25}$$

$$\int_{0-}^{m} e^{-\int_{0}^{t} (r(s) + \mu(x+s))ds} \left(-\pi + \mu(x+t)\right) dt + e^{-\int_{0}^{m} (r(s) + \mu(x+s))ds} = 0$$

$$\Rightarrow \frac{\int_{0-}^{m} e^{-\int_{0}^{t} (r(s) + \mu(x+s))ds} \mu(x+t) dt + e^{-\int_{0}^{m} (r(s) + \mu(x+s))ds}}{\int_{0-}^{m} e^{-\int_{0}^{t} (r(s) + \mu(x+s))ds} dt} = \pi \tag{20}$$

Actuaries have developed a shorthand notation for expected present values of standard payment streams. An actuary could write the premium formula above in code:

$$\pi = \frac{A_{x\overline{m}}}{a_{x\overline{m}}} = \frac{A_{x\overline{m}}^{1} + {}_{m}E_{x}}{a_{x\overline{m}}}$$
(21)

The reserve to set up at time  $t$  given that the policy holder is alive is then given by

$$V^{0}(t) = E\left[\int_{t}^{m} e^{-\int_{t}^{s} r(\tau)d\tau} \left(-\pi I\left(s\right)ds + dN\left(s\right)\right) + e^{-\int_{t}^{m} r(s)ds} I\left(m\right) \middle| I\left(t\right) = 1\right]$$
$$= \int_{t}^{m} e^{-\int_{t}^{s} (r(\tau) + \mu(x+\tau))d\tau} \left(-\pi + \mu\left(x+s\right)\right)ds + e^{-\int_{t}^{m} (r(s) + \mu(x+s))ds} \tag{22}$$

It is easy to verify that this reserve actually fulfills the special case of the Thiele differential equation,

$$\frac{\mathrm{d}}{\mathrm{d}t}V^{0}(t) = r(t)V^{0}(t) + \pi - \mu(t)(1 - V^{0}(t))$$
(23)

## Can the Financial Market Relax the Three Assumptions?

In this subsection, we discuss how mathematical finance can help us relax parts of Condition 1 and the valuation principles and formulas that follow from such a relaxation.

### The "Large Number" Assumption

This is inevitable for the law of large numbers to apply and we mention just, in passing, some of its counterparts in finance. In capital asset pricing model (CAPM; see Capital Asset Pricing Model) the hypothesis is that only systematic risk (aka systemic risk, market risk (see Market Risk), and nondiversifiable risk and is the risk that hits large numbers of assets in the market or the whole economy) has a price, in terms of expected return, while there is no price for taking unsystematic risk (aka idiosyncratic risk and diversifiable risk and is the risk that hits only one or a small number of assets in the market). The motivation is that unsystematic risk can be avoided without loss of expected return by choosing a sufficiently diversified portfolio. In arbitrage pricing theory (APT; see Arbitrage Pricing Theory), the CAPM is connected to arbitrage pricing by introducing the notion of asymptotic arbitrage. The conclusion is that to avoid asymptotic arbitrage (excess return for taking risk that can be cleared away by diversification), the price of unsystematic risk cannot be systematically positive, but one cannot say much about the price of unsystematic risk in a particular asset.

In insurance terms, the explanation is as follows: to avoid systematic gains (and losses), the price for taking unsystematic risk must be zero, leading to the equivalence principle under the objective measure. An asymptotic arbitrage argument would give access to a positive price for taking on insurance risk from particular policy holders as long as this does not happen systematically across the policy holders in a large portfolio. However, competition among insurance companies and/or regulation will typically prevent that particular policy holders pay premiums that are larger than their expected benefits.

#### The Independence Assumption

This can be relaxed to some extent with some help from financial market considerations and actions. This is convenient since the independence assumption is difficult to justify in practice. The help from financial market considerations and actions depends on the source of dependence. Here, we distinguish between two different sources both coming from insufficiency in the model presented in the section Modeling of Payment Streams: first, in practice, the payment coefficients  $b^j(t)$ ,  $b^{jk}(t)$ , and  $\Delta B^j(t)$  are typically not only dependent on the policy holder state but also on the financial performance of some investment fund or index. Second, in practice, the Markov assumption is violated by uncertainties in demographic trends and movements coming from sociological, medicinal, and economic developments.

First, the payment coefficients are supposed to protect buying power upon insurance events rather than nominal values. Therefore, the contracts typically contain participation features in the sense that the policy holder participates in the capital gains of some investment fund. The participation is either directly spelled out in the contract (unit-linked life insurance) or indirectly enforced by the legislative environment in which the contract is underwritten (with-profit life insurance). Additionally, the payments may be linked to the policy holder's salary or some salary index. We take a closer look at these participation features in the section Design of Payment Streams.

Such participation features affect the valuation since they create dependence between payment processes. To the extent that the dependence is created by financial market risk, a natural idea is to adopt other valuation techniques available for that part of the risk, for example, no arbitrage pricing. A example is to let the payment coefficients be contingent claims formalized as functions of an asset price. Consider, for example, the endowment insurance studied in Example 1, with the modification that a function f of the asset price at time m,  $S(m)$ , is paid out as benefit conditional on survival to time  $m$ . Formally  $\Delta B^{0}(m) = f(S(m))$ , and the (unknown) present value at time 0 of the payment process is

$$\int_{0-}^{m} e^{-\int_{0}^{t} r(s)ds} \left(-\pi I(t) dt + dN(t)\right)$$
$$+ e^{-\int_{0}^{m} r(\tau) d\tau} I(m) f(S(m)) \tag{26}$$

What is the financial value of this present value and what is the equivalence premium? Questions of this type were first approached with financial methods in  $[2]$  and since then by several other financial economists and insurance mathematicians [1]. To formalize the standard answer, we introduce two filtrations (see **Filtrations**) and corresponding measures generated by insurance risk and financial risk, respectively. Formally,  $\mathcal{F}^Z(t) = \sigma(Z(s), 0 \le s \le t)$ and  $\mathcal{F}^S(t) = \sigma(S(s), 0 < s < t)$  such that  $(\Omega^Z, \mathcal{F}^Z)$  $P^{Z}$ ) and  $(\Omega^{S}, \mathcal{F}^{S}, P^{S})$  form two filtered probability spaces from which we can construct the filtered product probability space ( $\Omega^Z \times \Omega^S$ ,  $\mathcal{F}^Z \otimes \mathcal{F}^S$ ,  $P^Z \otimes P^S$ ). The standard answer to the valuation problem above is then to take a product measure combining the objective measure  $P^Z$  with respect to insurance risk in  $Z$  and some martingale measure (see **Equivalent Martingale Measures**)  $Q^S$  with respect to financial risk in  $S$ , that is,

$$E^{P^{Z} \otimes Q^{S}} \left[ \int_{0-}^{m} e^{-\int_{0}^{t} r(s) ds} \left( -\pi I(t) dt + dN(t) \right) \right.$$
  
$$\left. + e^{-\int_{0}^{m} r(\tau) d\tau} I(m) f(S(m)) \right]$$
  
$$= \int_{0-}^{m} e^{-\int_{0}^{t} (r(s) + \mu(x+s)) ds} \left( -\pi + \mu(x+t) \right) dt$$
  
$$\left. + e^{-\int_{0}^{m} (r(s) + \mu(x+s)) ds} E^{Q^{S}} \left[ f(S(m)) \right] \right]$$
(27)

If the martingale measure is unique, so is the financial value of the payment process and the equivalence premium is obtained as in Example 1

by equating the financial value to zero and isolating  $\pi$ . It is a delicate issue to argue for equation (27) to be the "correct" value. It is clear that one somehow uses the diversification argument for the insurance risk and the no arbitrage argument for the financial risk. However, to make this precise, it takes arguments from incomplete markets pricing typically based on quadratic hedging or no asymptotic arbitrage approaches. Optimal investment is also an issue since, in general, no investment strategy hedges (see **Hedging**) the payment process for any outcome of the stochastic lifetime. In fact, parts of the development of quadratic hedging approaches (see [17] and references therein) are directly inspired by insurance applications in general and to life insurance payment processes in particular,  $[10, 11, 16]$ .

The statewise reserves introduced above generalize to reserves for more general future payments. In the case of a Markov model for  $S$ , these are characterized by deterministic differential equations that generalize Thiele's differential equation (16) [18].

Second, the transition intensities in the process  $Z$  move not only over age but also over calendar time in the sense that a mortality intensity for an  $x$ -year old is not necessarily the same in two different calendar years. If these movements are stochastic, this also creates dependence between policy holders and, thereby, between the payment processes written on their lives, and the Markov property of  $Z$  is lost. This is clear since the prospects of an insured's life not only depends on his/her state of health but also on the historical demographic development that is common for all insured.

There are different approaches to the modeling of, for example, mortality intensities. These are typically either sociobiologically flavored or financially flavored. By sociobiological flavor we mean that the starting point for the modeling is the biological, medicinal, and sociological sources of uncertainties. If, say, the future invention of a particular vaccine is expected to have a significant impact on the mortality intensity, then one should try to predict the finding of such a vaccine. By financial flavor we mean that the main source of inspiration is modeling of the short rate of interest. The benefits of such an inspiration are clear when comparing the survival probability  $e^{-\int_0^t \mu(s)ds}$  with a discount factor  $e^{-\int_0^t r(s)ds}$ . If we assume some kind of affine mortality intensity model, we achieve particularly simple expressions for, for example, the expected survival probability,

$$E\left[e^{-\int_0^t \mu(s) \mathrm{d}s}\right] \tag{28}$$

Such particularly simple expressions are appealing but suffer from mainly two disadvantages: it is difficult to motivate by sociobiological arguments that Vasicek or CIR (see Cox-Ingersoll-Ross (CIR) **Model**) model behavior should be present in mortality rates, and it is difficult to generalize the modeling advantages from the survival model to a multistate model.

The main challenge in stochastic modeling of the mortality intensity is the financial valuation of the demographic risk in a given model. Demographic risk is clearly nondiversifiable since the same mortality intensity hits a whole population or portfolio of insured. Is it priced by the financial market then? From the beginning of the millennium, there have been a few attempts by participants in the financial market to form a market for mortality derivatives. The idea is to involve the rest of the financial market, in addition to insurers and reinsurers, in taking part in mortality risk. The motivation for the investors is diversification since mortality intensities are not perfectly correlated with classical financial market risk. There are a lot of delicate questions concerning institutional and contractual design of products in such a market in addition to the modeling issues mentioned above. These questions are not so far answered sufficiently well by neither the market nor the academicians working in the field and, therefore, such a market is not flying yet. The prices in such a possible market place would give hints concerning the valuation of a survival probability, for example, under which probability measure (martingale measure) the expectation in equation  $(28)$  should be taken in order to form a market price. However, so far, the market is not sufficiently rich of assets and liquid to be really informative. See  $[3]$  for a review of the challenges of mortality risk.

#### The Deterministic Interest Rate Assumption

If this is not fulfilled we cannot, in the first place, say anything certain about the value at time  $t$  of one unit paid at time  $u > t$ . However, if there exists a sufficiently rich market of risk-free bonds, then we can say something: if at time  $t$  we have access to a risk-free zero-coupon bond (see **Bond**) maturing at time  $u$ , then the value of that bond, denoted by  $P(t, u)$ , is the only value of the payment of one unit at time  $u$  that prevents arbitrage. From bond market theory, it is known that the zero-coupon price can be represented as the conditional expected value of the stochastic discount factor under an equivalent martingale measure  $O^r$  derived from the price processes of the bond market. The question is, how can we use the bond market to update the valuation formula

$$E\left[\int_{0-}^{n} e^{-\int_{0}^{t} r(s)ds} dB(t)\right] \tag{29}$$

Here, the independence between payment processes does not carry over to the independence of present values in the following form:

$$\int_{0-}^{n} e^{-\int_{0}^{t} r(s)ds} dB(t) \qquad (30)$$

since it is the same interest rate process that hits all policies. Again, we can take a product measure, now combining the objective measure  $P^Z$  with respect to insurance risk in  $Z$  and some martingale measure  $O^r$  with respect to financial risk in r, and form the expectation

$$E^{P^{Z}\otimes Q^{r}}\left[\int_{0-}^{n}\mathrm{e}^{-\int_{0}^{t}r(s)\mathrm{d}s}\mathrm{d}B\left(t\right)\right]\tag{31}$$

If the payments are in nominal terms, that is, independent of market risk including interest rate risk, this formula reduces to

$$E^{P^{Z}}\left[\int_{0-}^{n}P\left(0,t\right)\mathrm{d}B\left(t\right)\right]\tag{32}$$

Again, the considerations apply: we cannot motivate equation  $(32)$  by either diversification or the no arbitrage principle but must rely on a combination of the two, introducing, for example, quadratic hedging in incomplete markets pricing and/or no asymptotic arbitrage arguments. No bond portfolio hedges the payment processes for all outcomes of  $Z$ , so the bond portfolio must reflect some optimization criterion.

### *What Can Finance Learn from Life Insurance:* An Example

After a section about "what finance has done for life insurance", we partly balance out things by a remark on "what life insurance has done for finance." Taking Figure 1 to represent the life history of a corporate rather than that of a human being, we have a simple credit risk model and in equation (2) a formalization of simple single-name credit risk derivatives. The default hazard rate  $\mu$  is, however, usually then modeled as a stochastic process, depending on some underlying macroeconomic variables or processes creating cross-corporate dependence similar to the dependence between life histories of policy holders. Following this idea and replacing in Figure (3) the husband by Corporate A and his wife by Corporate B, we have a simple two-name model. In the payment  $process (9)$ , we have formalized simple two-corporate credit risk derivatives. This model can from there be generalized to an arbitrary number of corporates. The cost of an exploding number of states and intensities as the number of corporates increases can be dealt by using appropriate cross-corporate homogeneity assumptions.

Figure (3) illustrates three sources of dependence playing distinct roles in the dependence modeling and in the calculation of expected values. One type of dependence between the two corporates exists, as mentioned in the previous paragraph, even if  $\mu^{02} =$  $\mu^{13}$  and  $\mu^{01} = \mu^{23}$ , but these intensities are functions of the same underlying economic processes. Then the corporates are dependent by being part of the same economy (or in the human life model by the two spouses being part of the same generation). Stronger dependence is present if, in addition,  $\mu^{02} \neq \mu^{13}$ and/or  $\mu^{01} \neq \mu^{23}$ . The so-called positive contagion, for example,  $\mu^{13} > \mu^{02}$ , appears if, for example, there is some kind of contractual relation between the corporates (or in the human life model if, upon the death of his spouse, the widower tends to die from loneliness and isolation). The so-called negative contagion, for example,  $\mu^{23} < \mu^{01}$ , appears if, for example, the two corporates are competing and the surviving corporate wins market shares after the default of the other (or in the human life model if, upon the death of her spouse, the widow finds a young lover and lives out her second youth). Even stronger dependence is present if we, in addition, allow for a transition from state 0 to state 3. The so-called joint default appears if the corporates are so closely connected, for example, through some mother-daughter relationship, that one credit risk event draws down both corporates simultaneously (or in the human life model, if both spouses in

the married couple are sitting in the same lethally crashing car.)

Note that here the dependence is introduced in a dynamic way such that one clearly sees what is going on. The valuation of payment processes and fairness principles studied in this section carry over directly to dynamic valuation of involved multicorporate credit risk derivatives. Furthermore, nondiversifiable risk is probably less of a problem here, since much of the macroeconomic risk driving default intensities are actually priced by the market, for example, interest rate risk. The dynamic atomic modeling has some advantages over the usual copula approach to dependence modeling that aggregates static effects by the cost of opaqueness [7].

### **Design of Payment Streams**

#### With-profit Life Insurance

On the one hand, the policy holder is interested in protecting buying power upon insurance events rather than nominal values. On the other hand, the insurance company is not necessarily interested in taking on nondiversifiable risk. Thus, the parties have delicate interests in sharing this risk, and this risk sharing takes many different institutional and contractual forms. In the traditional method for risk sharing, the payments finally paid are a consequence of the contract and the institutional management within certain regulatory constraints. The idea is, in the first place, to charge nominal premiums that are sufficiently high to cover nominal benefits under all possible outcomes of the economic-demographic environment. The surplus created by such a prudent payment stream belongs to the policy holder and should be redistributed as dividend payments to policy holders. The investment strategy and the redistribution are chosen at the discretion of the insurance company within a set of regulatory requirements.

The traditional way of forming the prudent nominal payment stream is to put up a set of artificial assumptions on the transition intensities  $\mu^{jk*}$  and the interest rate  $r^*$ , thereby forming the so-called technical basis, representing some kind of worstcase scenario. Now the nominal payment stream  $B$  is settled in accordance with the equivalence principle under these artificial assumptions, that is, fulfilling

$$E^* \left[ \int_{0-}^n e^{-\int_0^t r^*(\tau) d\tau} dB(t) \right] = 0 \tag{33}$$

where  $E^*$  denotes expectation with respect to the measure under which the transition intensities are given by  $\mu^{jk*}$ . Under the technical basis, the independence assumption is fulfilled by construction, since the payments are nominal and all transitions intensities are deterministic such that  $Z$  is Markov under the technical measure. In addition, under the technical basis, the deterministic interest rate assumption is fulfilled by construction. Thus, since Condition 1 is fulfilled, the expectation on the left-hand side of equation (33) expresses a financial value, however, under the technical assumptions.

The surplus is created when capital gains different from  $r^*$  are realized and real transitions different from the ones expected through  $\mu^{jk*}$  are experienced. This surplus is redistributed as dividend payments. We introduce a dividend payment process  $D$  with a structure similar to the one presented for  $B$  in equation (9). However, here we emphasize that the dividend payment process is not adapted to the filtration  $\mathcal{F}^Z$  generated by Z, as is B in this case, but adapted to a larger filtration  $\mathcal{F}^Z \vee \mathcal{F}^Y$ , where  $\mathcal{F}^Y$ is generated by realized capital gains and realized intensities. Now, what can we require from such a dividend payment process for the policy to be fair?

The classical approach is first to note that if the capital gains process and the transition intensities were known up to time  $n$ , this would be as working under Condition 1, and we could put up the usual equivalence principle. This observation inspires to an equivalence formula where the equivalence is required given the economic-demographic development, that is,

$$E\left[\int_{0-}^{n} \frac{1}{G\left(t\right)} \mathrm{d}\left(B+D\right)\left(t\right) \middle| \mathcal{F}^{Y}\left(n\right)\right] = 0 \qquad (34)$$

where  $G$  is the portfolio value corresponding to a self-financing investment strategy chosen by the insurance company. This means that all economicdemographic risk coming from the payment process  $B$  is returned to the policy holder through the payment process  $D$ . One can view this approach as careful risk management by design of the contract. This approach is discussed in  $[14]$ .

The modern approach, inspired from mathematical finance, is actually to allow for an exchange of economic-demographic risk as long as this risk is priced in accordance with the market. This gives rise to a substantial relaxation of equation (34) into

$$E^{P^{Z} \otimes Q^{Y}} \left[ \int_{0-}^{n} e^{-\int_{0}^{t} r(s)} d(B+D)(t) \right] = 0 \quad (35)$$

This method does not necessarily return all economic-demographic risk to the policy holders but leaves parts of it at the insurer who is, in return, appropriately paid for this risk through the valuation measure  $Q^Y$ . There are, however, two main challenges in replacing equation  $(34)$  by equation  $(35)$ : first, there is no (sufficiently rich and liquid) market to make the  $Q^Y$  measure unique with respect to demographic risk. Second, in the classical approach (34), all the risk management has been taken care of by the design of the contract. Introducing equation (35), risk management also means optimal decision making during the terms of the contract, for example, through optimal investment in incomplete markets. This approach is taken in many publications in the area, see the textbook  $[11]$  and references therein

The insurance companies decide on the dividend process and the investment strategy to which it is adapted within certain constraints given by the contractual, institutional, and regulatory environment. There are, however, substantial regional and institutional differences in how this decision is constrained and made around the world. In addition, given the payment process  $D$ , there are differences in how this payment process materializes into payments experienced by the policy holders. In other words, these dividends are not necessarily paid out in cash. More often they are kept within in the insurance company but assigned to the policy holder who will then, in return, receive the so-called bonus payments in connection with either future premium payments and/or benefit payments in the payment process  $B$ . Here, we describe two of the more important arrangements. The first arrangement is important due to its major role in the UK/US tradition in the past, but during these decades it is partly superseded by the second arrangement that has a long tradition in the continental Europe.

In pension funding, the contract is part of an employment contract: the employer pays the premiums and the employee receives the benefits. The benefits are typically not nominal but rather linked to the policy holder's salary or some salary index. In general, prudent technical assumptions give rise to a positive and increasing dividend payment stream that is experienced by the employer as a current or future discount in the premium level. However, if at all, one is not so concerned about prudence because a negative surplus can be filled by paying out negative dividends in terms of increasing current or future premiums paid by the employer. This arrangement splits the financial-demographic risk between the insurance company (pension fund) and the employer, whereas the employee goes free (apart from salary risk). This class of arrangements is called *defined ben*- $\text{efits } (DBs)$  since the benefits are determined initially (possibly in terms of the salary), whereas the future premiums are unknown to the employer and will go up or down, respectively, when a negative or positive surplus is returned.

In with-profit life insurance, the contract is either a private contract or part of an employment contract. The employee or the employer pays the premium and the employee receives the benefits. Here, in contrast, the premiums are nominal or linked to some salary index. Sufficiently prudent technical assumptions give rise to a positive and increasing dividend payment stream that is experienced by the employee as a current or future bonus benefit level. One is here, in contrast, indeed concerned about prudence because a negative surplus can typically not be returned to the policy holder who is contractually protected from decreasing benefits: these are considered as binding minimum guarantees. The financial-demographic risk is shared between the policy holder who receives unknown benefits and the insurance company who bears the risk that the surplus becomes negative, whereas the employer goes free. This class of arrangements is called *defined*  $contributions$  (DCs) since the contributions (premiums) are determined initially (possibly in terms of the salary), whereas the future benefits are unknown to the employee (but often constrained downward by minimum guarantees).

It is clear that understanding the mathematics of finance in general and no arbitrage valuation in particular has played a crucial role in replacing the fairness constraint  $(34)$  by the fairness constraint  $(35)$ . This replacement has given the involved parties, that is, policy holders typically represented by regulators, investors, and insurance companies, access to measuring and appropriately evaluating the exchanged risk. Note, however, that part of this risk is neither diversifiable nor hedgeable and therefore there is still some ambiguity left in the fairness criterion (35), which is not present in equation  $(34)$ . Also note that valuation is closely connected to existence of efficient hedging strategies—strategies that may be difficult to follow for leading insurance companies and pension funds due to regulatory restrictions and, more importantly, from a real economic point of view—these funds are often large investors in the sense that their actions in the market have adverse feedback effects in market prices.

#### Unit-linked Life Insurance

Unit-linked life insurance has partly replaced the traditional contracts described above, in particular in the private market. The idea comes from the US market and is making up an increasing part of the private market also in Europe with considerable regional differences, though. The idea is to formalize the adaptation to the economic-demographic environment explicitly in the contract in such a way that the investment strategy can be chosen at the discretion of the policy holder rather than the insurance company.

In pure unit-link insurance, that is, without any form of guarantee, all risks from the investment are eventually returned to the policy holder in one way or another. Then we can naturally take the counterpart to the equivalence criterion  $(34)$  and require equivalence of the payment process  $B$ ,

$$E\left[\int_{0-}^{n} \frac{1}{G\left(t\right)} \mathrm{d}B\left(t\right) \middle| \mathcal{F}^{Y}\left(n\right)\right] = 0 \qquad (36)$$

where  $G$  is the portfolio value corresponding to a selffinancing investment strategy chosen partly by the policy holder. By multiplication of  $G(n)$ , which is  $\mathcal{F}^{Y}(n)$ -measurable, and splitting up the integral, one sees that this is equivalent to the following settlement of the final lump sum payment:

$$E\left[\Delta B^{Z(n)}\left(n\right)\middle|\mathcal{F}^{Y}\left(n\right)\right]$$
  
=  $-E\left[\int_{0-}^{n-}\frac{G\left(n\right)}{G\left(t\right)}\mathrm{d}B\left(t\right)\middle|\mathcal{F}^{Y}\left(n\right)\right]$  (37)

This relation restricts the terminal lump sum to finally make up for all movements on capital gains and transition intensities in the past. For this relation to hold, it is sufficient to formalize the payment process by

$$\mathrm{d}B\left(t\right) = G\left(t\right)\mathrm{d}B^*\left(t\right) \tag{38}$$

where  $B^*(t)$  is a nominal payment process fulfilling the relation

$$E\left[\int_{0-}^{n} \mathrm{d}B^{*}\left(t\right)\right] = 0\tag{39}$$

In pure unit-link insurance, the (risk-minimizing) investment strategy implemented by the insurance company coincides essentially with the investment strategy stipulated in the contract.

Such an insurance contract is not provided in practice due to legislative constraints and the policy holder's demand for specification of guaranteed levels of premiums and benefits, typically nominal, that protect the policy holder from large capital losses. Such features introduce a genuine sharing of risk between the policy holder and the insurance company, and the criterion  $(36)$  is too tight. We can relax equation  $(36)$  by introducing the counterpart to equation (35) and require that the payment process  $B$ fulfills

$$E^{P^{Z}\otimes Q^{Y}}\left[\int_{0-}^{n}e^{-\int_{0}^{t}r(s)}dB\left(t\right)\right]=0\qquad(40)$$

For example, let us say that the terminal lump sum payment given in equation  $(37)$  is floored off at some guarantee level  $K$ . This guarantee must be compensated, for example, by specifying that only a proportion  $a$  of the sum is paid out if it is larger than  $K$ , that is,

$$E\left[\Delta B^{Z(n)}\left(n\right)\middle|\mathcal{F}^{Y}\left(n\right)\right]$$
  
=  $\max\left(-aE\left[\int_{0-}^{n-}\frac{G\left(n\right)}{G\left(t\right)}\mathrm{d}B\left(t\right)\middle|\mathcal{F}^{Y}\left(n\right)\right],K\right)$   
(41)

Looking closer at this, the terminal payment is some kind of delicate Asian option on  $G$ . Now, financial mathematics helps us in calculating fair pairs of  $a$  and  $K$  such that equation (40) is fulfilled. Such pairs will depend on the riskiness in the portfolio underlying G. The pair  $(1, -\infty)$  is one example, corresponding to equation (37), that does not depend on the investment portfolio, though. In such more advanced types of unit-link insurance, the (riskminimizing) investment strategy implemented by the insurance company does not essentially coincide with the investment strategy chosen by the policy holder but contains some investment in or hedging of the embedded derivatives

In the section Design of Payment Streams, we set the framework for the design of the payment streams. Furthermore, we discussed fairness constraints. Within the fairness constraints, there are a series of decisions to be made by the insurance company and/or the policy holder. In this section, we focus on these decisions. In with-profit life insurance and pension funding, there are two decision processes of paramount interest: the investment decisions underlying  $G$  and the dividend payment stream  $D$ .

We form the surplus  $X$  at time  $t$  as the assets at time  $t$  minus the liabilities at time  $t$  with respect to the contract or portfolio of contracts in focus. The assets are the payments to the insurance company (premiums less benefits) in the past accumulated with capital gains. The liabilities are some measure of the future obligations in the payment process  $B$ , here denoted by  $V(t)$ . Thus,

$$X(t) = -\int_{0-}^{t} \frac{G(t)}{G(s)} \mathrm{d}(B+D)(s) - V(t) \quad (42)$$

From our analysis in the section Valuation of Payment Streams, we have several candidates for the liabilities to be plugged in: the classical liability is the technical reserve

$$E^* \left[ \left. \int_t^n e^{-\int_t^s r^*(\tau) d\tau} dB\left(s\right) \right| Z\left(t\right) \right] \tag{43}$$

which is the present value of future payments under the same artificial assumptions as the ones used in the equivalence principle. This ensures that, by the equivalence principle, the surplus prior to inception is equal to 0, that is,  $X(0-) = 0$ . A more realistic estimate of the future obligations is a market consistent valuation along the lines of equation (32) of the future payments conditional on all information up to time *t*:

$$E^{P^{Z}}\left[\left.\int_{t}^{n}P\left(t,s\right)\mathrm{d}B\left(s\right)\right|Z\left(t\right)\right]\tag{44}$$

Anyway, the surplus will evolve according to the investment and dividend decisions made in the past. In fact, the surplus can be considered as the policy holder's extra wealth, in excess of  $V$ , which is managed by the insurance company. Since the investment strategy can be parameterized as an investment strategy for the surplus itself, this investment-dividend problem is a delicate version of the classical investment-consumption problem known from finance. It is certainly a nonstandard version due to a series of particularities (related to financial topics mentioned in brackets): (i) the decision maker and the consumer do not coincide since the dividends go to the policy holder while the investment-dividend decisions are made by the insurance company (principal agent problem); (ii) usually, the dividends are not paid out as cash but transferred to a future payment stream (habit formation); (iii) obligations are nonhedgeable due to diversifiable death risk and nondiversifiable mortality risk (nonhedgeable income process); (iv) there are regional solvency constraints on the surplus-varying in strictness and underlying valuation principles (intermediate constraints on wealth); (v) there are regional constraints on investment and surplus redistribution strategies (intermediate constraints on investment and consumption); (vi) usually, the surplus is accounted for on (sub)portfolio level rather than individual level and the portfolio members have possibly inhomogeneous attitudes to risk; and (vii) short-fall risk due to nonhedgeable obligations or aggressive investment decisions is borne by the equity holders who should be appropriately paid for it.

The list of particularities is all parts of the subject matter of ALM, which is essential in modern mathematics of life insurance and its merger with parts of mathematical finance, including incomplete market valuation, liability-driven investments, constrained asset allocation, and strategic asset allocation. These areas of finance have gained momentum from their applications in life insurance and versions of these problems stemming from practical problems in the insurance market continue to challenge asset managers both on the theoretical and the practical side.

With the prevalence of unit-link insurance comes the importance for the policy holders to make good investment decisions and for the insurance companies to advise them in doing so. At first glance, this is a classical personal finance problem of optimal investment of pension savings, with or without uncertain lifetime. However, the appearance of genuine insurance elements in the contract, that is, financial protection against life history events, brings to the surface a more delicate process of decision making. This includes the financial protection bought throughout life in terms of insurance payments: given the financial situation at time *t*, what is the best death sum, disability sum/annuity, and unemployment sum/annuity to buy? Optimal decisions are naturally influenced by the market price of risk and risk aversion of the policy holder, as is the investment decision in classical personal finance. However, the market price of risk is not necessarily easy to deduct from a market offering contracts with nonexplicit participation features and constraints in a heavily regulated environment. And should risk aversion with respect to life history risk be parameterized in the same way as risk aversion with respect to financial risk?

Clearly, the formulation of the optimization problem is much more involved in the area of personal finance and insurance than in the area of pure personal finance. Ambiguity in the way the optimization problem should be formulated at all and the opaque insurance market in which the decisions are to be taken contribute to a complication of the subject matter. However, it also turns out facilitating in some respects to introduce access to the insurance market: it is by now well-accepted that human wealth, that is, the financial value of future labor earnings, is an important asset in personal decision making. This explains partly the rationale of life cycle investment saying that younger people should hold a larger proportion of their financial assets in risky investments than should older people. However, uncertainties in future earnings in general and the risk of loosing the human wealth in an insurance event— for example, disability or unemployment—make the human wealth difficult to assess. The introduction of an insurance market and insurance decisions has a completing effect on the market that makes the assessment of human wealth less ambiguous.

In the literature, the approach to personal finance and insurance go in two distinct directions: one direction is inspired from ruin considerations and formulates the optimization problem in terms of the probability of life time ruin in the sense of ever living below some defined level of poverty [9]. Another direction is inspired from personal finance and formulates the optimization problem in terms of expected utility of future consumption across life history events and uncertain lifetimes. This direction was initiated in [15] and recent contributions are [8, 12].

# **References**

- [1] Aase, K.K. & Persson, S.-A. (1994). Pricing of unitlinked life insurance policies, *Scandinavian Actuarial Journal* **1994**, 26–52.
- [2] Brennan, M.J. & Schwartz, E.S. (1976). The pricing of equity-linked life insurance policies with an asset value guarantee, *Journal of Financial Economics* **3**, 195–213.
- [3] Cairns, A.J.G., Blake, D. & Dowd, K. (2008). Modelling and management of mortality risk: a review, *Scandinavian Actuarial Journal* **2008**(2–3), 79–113.
- [4] Gerber, H.U. (1995). *Life Insurance Mathematics*, 2nd edition, Springer-Verlag.
- [5] Hald, A. (1981). T. N. Thiele's contributions to statistics, *International Statistic Review* **49**, 1–20.
- [6] Hoem, J.M. (1969). Markov chain models in life insurance, *Bl¨atter der Deutschen Gesellschaft f¨ur Versicherungsmathematik* **9**, 91–107.
- [7] Kraft, H. & Steffensen, M. (2007). Bankruptcy, counterparty risk, and contagion, *Review of Finance* **11**, 209–252.
- [8] Kraft, H. & Steffensen, M. (2008). Optimal consumption and insurance: a continuous-time Markov chain approach, to appear in *ASTIN Bulletin* **28**(1), 231–257.
- [9] Milevsky, M., Moore, K. & Young, V. (2006). Asset allocation and annuity-purchase strategies to minimize the probability of ruin, *Mathematical Finance* **16**(4), 647–671.
- [10] Møller, T. (2001). Risk-minimizing hedging strategies for insurance payment processes, *Finance and Stochastics* **5**(4), 419–446.
- [11] Møller, T. & Steffensen, M. (2007). *Market-Valuation Methods in Life and Pension Insurance*, Cambridge University Press.
- [12] Nielsen, P.H. & Steffensen, M. (2008). Optimal investment and life insurance strategies under minimum and maximum constraints, to appear in *Insurance: Mathematics and Economics*.
- [13] Norberg, R. (1991). Reserves in life and pension insurance, *Scandinavian Actuarial Journal* 3–24.
- [14] Norberg, R. (1999). A theory of bonus in life insurance, *Finance and Stochastics* **3**(4), 373–390.
- [15] Richard, S.F. (1975). Optimal consumption, portfolio and life insurance rules for an uncertain lived individual in a continuous time model, *Journal of Financial Economics* **2**, 187–203.
- [16] Schweizer, M. (2001). From actuarial to financial valuation principles, *Insurance: Mathematics and Economics* **28**, 31–47.
- [17] Schweizer, M. (2001). A guided tour through quadratic hedging approaches, in *Option Pricing, Interest Rates and Risk Management*. E. Jouini, J. Cvitanic & M. Musiela, eds, Cambridge University Press.

- [18] Steffensen, M. (2000). A no arbitrage approach to Thiele's differential equation, *Insurance: Mathematics and Economics* **27**, 201–214.
- [19] Thiele, T.N. (1880). *Sur la Compensation de Quelques Erreurs Quasisystematiques par la Methodes de Moindres Carres*, Reitzel, Copenhagen.

## **Related Articles**

**Credit Risk**; **Hedging**; **Market Risk**; **Risk-neutral Pricing**.

MOGENS STEFFENSEN
## Jarrow-Lando-Turnbull Model

The credit-risk model of Jarrow, Lando, and Turnbull is based on a Markov chain with finite state space, modeled in discrete or continuous time. Economically, it relies on the appealing interpretation of using different rating classes, which are represented by the states of the Markov chain. Presumably, it is the first credit-risk model that incorporates rating information into the valuation of defaultable bonds and credit derivatives. An advantage of modeling the credit-rating process is that the resulting bond prices explicitly depend on the issuer's initial rating and possible rating transitions in the future. Moreover, the model allows to price derivatives whose payoffs depend on the credit rating of some reference bond, an application that is not straightforward in intensitybased models or structural-default models.

Technically, the model is formulated on a filtered probability space with a money-market account  $B = \{B(t)\}_{0 \le t \le T}$  as numéraire. The state space of the underlying Markov chain is denoted by  $S =$  $\{1,\ldots,K\}$ , where state K represents default. The other states are identified with rating classes that are ordered according to increasing default risk, that is, state 1 represents the best rating. Transition probabilities from one state to another are specified via a probability matrix  $\boldsymbol{Q}$  in discrete time and using a generator matrix  $\Lambda$  in continuous time. Multiple defaults are excluded by making the default state absorbing, which corresponds to specific choices of the last rows of  $\boldsymbol{O}$  and  $\boldsymbol{\Lambda}$ , respectively. The original model achieves a high level of tractability by imposing the following assumptions: existence of a unique equivalent martingale measure, independence of risk-free interest rates and credit migrations under the martingale measure, and a constant recovery  $R$  paid at the maturity of the defaulted bonds. It is further suggested in  $[8]$  that historical transition probabilities could be adjusted by some deterministic, time-dependent, proportional risk premium to derive the required transition matrix  $\tilde{\boldsymbol{Q}}$ or generator matrix  $\hat{\Lambda}$  under the martingale measure. Then,  $T$ -year survival probabilities are expressed in terms of this martingale measure, under which defaultable bonds, futures, and derivatives on risky bonds are priced by computing their expected discounted payoff. To be more precise, let us briefly

describe the discrete-time case. Denoting the matrix of risk premiums at time t by the  $K \times K$ -dimensional diagonal matrix  $\mathbf{\Pi}(t) = \text{diag}(\pi_1(t), \dots, \pi_{K-1}(t), 1),$ it is assumed that

$$\tilde{\boldsymbol{Q}}(t,t+1) - \boldsymbol{I} = \boldsymbol{\Pi}(t)(\boldsymbol{Q} - \boldsymbol{I}) \tag{1}$$

where  $I$  denotes the  $K$ -dimensional identity matrix and with assumptions ensuring that  $\tilde{O}(t, t+1)$  is a probability matrix with absorbing state  $K$ . It is well known that the  $n$ -step transition matrix at time  $t$  under the martingale measure is given by

$$\tilde{\mathcal{Q}}(t,t+n) = \prod_{i=0}^{n-1} \tilde{\mathcal{Q}}(t+i,t+i+1), \quad \forall n \in \mathbb{N}$$
(2)

Let  $\tau$  denote the random default time and  $C(T)$  the random payoff at time  $T$  of a credit-risky claim. Then the value  $C(t)$  at time t of this contingent claim is given by

$$C(t) = B(t) \cdot \tilde{\mathbb{E}}_t[C(T)/B(T)] \tag{3}$$

with  $\tilde{\mathbb{E}}_t$  denoting the conditional expectation, with respect to the information at time  $t$  under the martingale measure. Under these assumptions, the price  $P(t, T)$  of a default-free zero-coupon bond at time t, maturing at time  $T$ , is given by

$$P(t,T) = B(t) \cdot \mathbb{E}_t[1/B(T)] \tag{4}$$

The corresponding price  $P_i^d(t,T)$  of a defaultable zero-coupon bond rated  $i$  at time  $t$  is given by

$$P_i^d(t,T) = P(t,T) \cdot \left(R + (1-R) \cdot \tilde{Q}_t^i(\tau > T)\right)$$
(5)

with  $\tilde{Q}_t(\tau > T) = (\tilde{Q}_t^1(\tau > T), \dots, \tilde{Q}_t^{K-1}(\tau > T), 0)$ denoting the time  $T$  survival probabilities for firms in the different rating classes at time  $t$  under the martingale measure. These survival probabilities are given by

$$\tilde{Q}_{t}^{i}(\tau > T) = 1 - \tilde{q}_{i,K}(t,T), \quad i = 1,\ldots,K \quad (6)$$

where  $\tilde{q}_{i,K}(t,T)$  denotes the respective element of  $Q(t, T)$ . Further applications of the model include the construction of hedging strategies against rating changes and the pricing of options on risky debt.

Most results derived in the discrete model find their analog in the continuous version of the model. More complicated in a continuous framework is the derivation of martingale probabilities, specified by the generator matrix ˜ . For the construction of this matrix, [8] presents an implicit calibration method that starts with a historical estimation of . On the basis of the paradigm of choosing ˜ *close* to the historical , a proportional risk premium is introduced, which is calibrated to observed bond prices.

The original references of the presented methodology are [9] and [8], and an excellent textbook summary is Chapter 12 of [4]. An introduction to Markov chains is given in [1] and [3]. Estimation procedures of the historical intensity matrix are studied in [10] and [7]. Considering generalizations of the model, let us mention [5] for stochastic recovery rates, [2, 12], and [13], for transition probabilities explained by state variables, and [11] for a different risk premium. Finally, a multifirm extension using a stochastic time change is presented in [6].

## **References**

- [1] Anderson, W.J. (1991). *Continuous-Time Markov Chains. An Applications-Oriented Approach*, Springer Verlag, New York.
- [2] Arvanitis, A., Gregory, J. & Laurent, J.-P. (1999). Building models for credit spreads, *The Journal of Derivatives* **6**(3), 27–43.
- [3] Behrends, E. (2000). *Introduction to Markov Chains*, Vieweg Verlag, Braunschweig/Wiesbaden.
- [4] Bielecki, T.R. & Rutkowski, M. (2002). *Credit Risk: Modeling, Valuation and Hedging*, Springer Verlag, Berlin.

- [5] Das, S.R. & Tufano, P. (1996). Pricing credit-sensitive debt when interest rates, credit ratings and credit spreads are stochastic, *The Journal of Financial Engineering* **5**(2), 161–198.
- [6] Hurd, T.R. & Kuznetsov, A. (2007). Affine Markov chain model of multifirm credit migration, *The Journal of Credit Risk* **3**(1), 3–29.
- [7] Israel, R.B., Rosenthal, J.S. & Wei, J.Z. (2001). Finding generators for Markov chains via empirical transition matrices, with applications to credit risk, *The Journal of Mathematical Finance* **11**(2), 245–265.
- [8] Jarrow, R.A., Lando, D. & Turnbull, S.M. (1997). A Markov model for the term structure of credit risk spreads, *The Review of Financial Studies* **10**(2), 481–523.
- [9] Jarrow, R.A. & Turnbull, S.M. (1995). Pricing derivatives on financial securities subject to credit risk, *The Journal of Finance* **50**(1), 53–85.
- [10] Kavvathas, D. (2001). Estimating credit rating transition probabilities for corporate bonds, *AFA 2001 New Orleans Meetings*, New Orleans.
- [11] Kijima, M. & Komoribayashi, K. (1998). A Markov chain model for valuing credit risk derivatives, *The Journal of Derivatives* **6**(1), 97–108.
- [12] Thomas, L.C., Allen, D.E. & Morkel-Kingsbury, N. (2002). A hidden Markov chain model for the term structure of bond credit risk spreads, *International Review of Financial Analysis* **11**(3), 311–329.
- [13] Wei, J.Z. (2003). A multi-factor, credit migration model for sovereign and corporate debts, *The Journal of International Money and Finance* **22**(5), 709–735.

## **Related Articles**

**Credit Default Swaps**; **Duffie–Singleton Model**; **Hazard Rate**; **Multiname Reduced Form Models**.

RUDI ZAGST & MATTHIAS A. SCHERER
# **Second Fundamental Theorem of Asset Pricing**

The second fundamental theorem of asset pricing concerns the mathematical characterization of the economic concept of market completeness for liquid and frictionless markets with an arbitrary number of assets. The theorem establishes the mathematical necessary and sufficient conditions in order to guarantee that every contingent claim on the market can be duplicated with a portfolio of primitive assets. For finite asset economies, completeness (i.e., perfect replication of every claim on the market by admissible self-financing strategies) is equivalent to uniqueness of the equivalent martingale measure. This result can be extended to market models with an infinite number of assets by defining completeness in terms of approximate replication of claims by attainable ones. Hence several definitions of completeness are possible, and in the sequel we will present and discuss them extensively.

### **Finite Number of Assets**

The *second fundamental theorem* appeared in [9] under the assumption that the interest rate is zero and that the agent employs only simple trading strategies to address the following issue, raised in the economic literature [1, 20, 22]: given a financial market, which contingent claims are "spanned" by a given set of market securities?

In the seminal paper [7], it was already observed that in the idealized Black-Scholes market the cash flow of an option can be duplicated by managing a portfolio containing only stock and bond. A natural question is then as follows: for which contingent claim does this result hold in more general markets? When does it hold for all contingent claims on the market?

For markets with a finite number of asset prices, the answer to this problem was provided for the first time in  $[10, 11]$ . Here we follow the notation of  $[11]$ in order to state the *second fundamental theorem*.

Let  $T < \infty$  be a fixed time horizon; consider a probability space  $(\Omega, \mathcal{F}, P)$  endowed with a filtration  $(\mathcal{F}_t)_{t\in[0,T]}$  satisfying the usual conditions and such that  $\mathcal{F}_0$  contains only  $\Omega$  and the null sets of  $P$ 

and with  $\mathcal{F}_T = \mathcal{F}$ . Let  $S = (S_t^0, \ldots, S_t^d)_{t \in [0,T]}$  be a  $(d + 1)$ -dimensional strictly positive semimartingale, whose components  $S^0, \ldots, S^d$  are right continuous with left limits. Moreover, we assume that  $S_0^0 = 1$ . Here, the stochastic process  $S_t^k$  represents the value at time  $t$  of the  $k$ th security on the market. The discounted price process  $Z = (Z_t^1, \ldots, Z_t^d)_{t \in [0,T]}$  is then defined by setting  $Z^k = S^k / S^0$ , for  $k = 1, \ldots, d$ . Let  $\mathbb{P}$  be the set of probability measures  $Q$  on  $(\Omega, \mathcal{F})$  that are equivalent to P and such that Z is a (vector) martingale under O. We assume that  $\mathbb{P}$ is not empty, that is, that the market is arbitrage free (see Fundamental Theorem of Asset Pri**cing**). We fix an element  $P^*$  in  $\mathbb{P}$  and denote by  $E^*$  the expectation under  $P^*$ . Let  $L(Z)$  denote the set of all vector-valued, predictable processes  $H =$  $(H_t^1,\ldots,H_t^d)_{t\in[0,T]}$  that are *integrable* with respect to the semimartingale Z. For further details on  $L(Z)$ , we refer to Remark 1 below.

**Definition 1** A stochastic process  $\phi \in L(Z)$  is said to be an admissible self-financing strategy if

- (i) the discounted value process  $V^*(\phi) := \sum_{k=1}^d \phi^k Z^k$  is almost surely nonnegative;<br>(ii)  $V^*(\phi)$  satisfies the self-financing condition

$$V_t^*(\phi) = V_0^*(H) + \int_0^t \sum_{k=1}^d \phi_s^k \, \mathrm{d}Z_s^k, \ t \in [0, T]; \tag{1}$$

(iii)  $V^*(\phi)$  is a martingale under  $P^*$ .

Condition  $(iii)$  is introduced here to rule out "certain foolish strategies that throw out money" [11], that is, for no-arbitrage reasons. Note also that in the preceding definition only the last condition may depend on the choice of the reference measure  $P^*$ .

A contingent claim  $X$  with maturity  $T$  is then represented by a nonnegative ( $\mathcal{F}_T$ -measurable) random variable. Such a claim is said to be *attainable* if there exists an admissible trading strategy  $\phi$  such that  $V_T^*(\phi) = X/S_T^0$ . The model is said to be *complete* if every claim<sup>a</sup> is attainable.

**Theorem 1** (The second fundamental theorem of asset pricing, [11]). Let  $\mathbb{P} \neq \emptyset$ . Then the following statements are equivalent:

(i) The model is complete under  $P^*$ .

(ii) Every  $P^*$ -martingale M can be represented in the form

$$M_{t} = M_{0} + \int_{0}^{t} \sum_{k=1}^{d} H_{s}^{k} dZ_{s}^{k}, \ t \in [0, T] \quad (2)$$

*for some*  $H \in L(Z)$  *(predictable representation* property).

(iii)  $\mathbb{P}$  is a singleton, that is, there exists a unique equivalent martingale measure for  $Z$ .

The proof of this theorem relies on some results of [12, 14], Chapter XI, relating the representation property  $(1)$  to a condition involving a certain set of probability measures.

**Remark 1** In Theorem 1 the definition of the space  $L(Z)$  is crucial, as shown by a counterexample in [19]. From reference [16] we obtain that  $L(Z)$ must be the largest class of integrands over which multidimensional integrals with respect to  $Z$  can be defined, as done implicitly in [11]. Hence by Theorem 4.6 of [12] we have that  $L(Z)$  is the space of the vector-valued, predictable processes  $H = (H_t^1, \ldots, H_t^d)_{t \in [0,T]}$  such that

$$\int_{0}^{t} \sum_{i,j=1}^{d} H_{s}^{i} H_{s}^{j} d[Z^{i}, Z^{j}]_{s}, \ t \in [0, T]$$
 (3)

is locally integrable.

Completeness can be easily characterized in some particular cases, as shown by the following examples.

**Example 1** Consider a market with a finite number of assets in discrete time  $\{0, \ldots, T\}$  and let  $\mathcal{P}_t$  be the partition of  $\Omega$  underlying  $\mathcal{F}_t$ . For each cell A of  $\mathcal{P}_t$ ,  $t \in \{0, \ldots, T-1\}$ , we define as *splitting index of A* the number  $K_t(A)$  of cells of  $\mathcal{P}_{t+1}$  that are contained in  $A$ . Then completeness can be characterized as follows.

**Proposition 1** (Proposition 2.12 of [10]). Let  $\mathbb{P} \neq \emptyset$ and suppose that the securities are not redundant.<sup>b</sup> Then the model is complete if and only if  $K_t(A) =$  $d+1$  for all  $A \in \mathcal{P}_t$  and  $t = 0, \ldots, T-1$ .

Hence completeness is a matter of dimension. Corollary  $4.2$  of [23] shows that if the market is complete, then the splitting index  $K_t(A)$  is determined by the price process  $S$  only, that is, for every  $t = 0, \ldots, T$  and each  $A \in \mathcal{P}_t$ , we have  $K_t(A) =$  $\dim(\text{span}\{S_{t+1}(\omega) : \omega \in A\})$ . Hence it is sufficient to check if the rank of the matrix with columns formed by the vectors  $S_{t+1}(\omega)$ ,  $\omega \in A$ , equals the splitting index  $K_t(A)$  of A. By using this geometric property of the sample paths of the price process, an algorithm is then provided in [23] to check if finite securities markets in discrete time are complete.

**Example 2** In the case when security prices follow Itô processes on a multidimensional Brownian filtration, completeness of the market can be characterized in terms of the volatility matrix of the underlying asset prices, as shown in [3, 16, 18]. Consider a market with  $d$  risky assets given by Itô processes of the form

$$S_t^i = S_0^i \exp\left[\int_0^t \alpha_s^i \, \mathrm{d}s - 1/2 \sum_{j=1}^n \int_0^t (\sigma_s^{ij})^2 \, \mathrm{d}s + \sum_{j=1}^n \int_0^t \sigma_s^{ij} \, \mathrm{d}W_s^j \right], \ t \in [0, T]$$
(4)

 $i = 1, \ldots, d$ , on the probability space  $(\Omega, \mathcal{F}, P)$ endowed with the (augmented) natural filtration  $(\mathcal{F}_t)_{t \in [0,T]}$  generated by the *n*-dimensional Brownian motion  $W = (W_t^1, \ldots, W_t^n)_{t \in [0,T]}$  with  $\mathcal{F}_T = \mathcal{F}$ . Here  $S^0$  can be assumed constantly equal to 1 for the sake of simplicity. For  $t \in [0, T]$  we denote by  $\Sigma_t(\omega)$  the (random) volatility matrix, whose entries are given by

$$[\Sigma_t(\omega)]_{ij} = \sigma_t^{ij}(\omega), \quad i = 1, \dots, d, \quad j = 1, \dots, n$$
(5)

If for all  $i = 1, \ldots, d$ ,  $S_0^i$  is a positive constant,  $(\alpha_t^l)_{t \in [0,T]}$  an adapted stochastic process with

$$\int_0^T |\alpha_s^i| \, \mathrm{d}s < \infty, \ \text{a.s.} \tag{6}$$

and  $(\sigma_t^{ij})_{t \in [0,T]}$  are adapted stochastic processes with

$$\int_0^T (\sigma_s^{ij})^2 \, \mathrm{d}s < \infty, \text{ a.s.} \tag{7}$$

for  $j = 1, \ldots, n$ , then the following characterization of market completeness holds.

**Theorem 2** (Theorem 4 of [3], Theorem 2.2 and 3.2 of [16]). Let  $\mathbb{P} \neq \emptyset$ . Then the market is complete if and only if  $P(\text{rank}(\Sigma_t) = d \text{ for almost all } t \in$  $[0, T] = 1.$ 

For further references, see also Theorem 4.1 of [18]. Since there are  $n$  sources of randomness represented by the Brownian motions, it is natural to expect that  $n$  sufficiently independent asset prices are needed for completeness. Clearly, if  $d < n$  the market cannot be complete.

Example 3 If price processes are discontinuous but with a finite number of jump sizes, then we obtain again a characterization of completeness in terms of the volatility matrix, as shown by the following theorem attributed to Bättig [3]. We set again  $S^0 = 1$  and consider price processes driven by a multivariate point process<sup>c</sup>  $\mu$  with compensator  $v(\mathrm{d}t, \mathrm{d}x) = K_t(\mathrm{d}x) \mathrm{d}t$  such that

$$S_t^i = S_0^i \varepsilon (R^i)_t, \ t \in [0, T], \ i = 1, \dots, d \quad (8)$$

with

$$R_t^i = \int_0^t \alpha_s^i \, \mathrm{d}s + \int_{[0,t] \times E} \sigma^i(u,x) (\mu(\, \mathrm{d}u, \, \mathrm{d}x) - \nu(\, \mathrm{d}u, \, \mathrm{d}x)), \ \ t \in [0,T], \ \ i = 1,\dots,d,$$

where the  $\sigma^{i}(t, x)$ s are bounded  $d\mu \otimes dP$  a.e.,  $\mathcal{E}$  is the Doléans exponential (for the definition, we refer to Theorem I.4.61 of [13]), and  $E \subset \mathbb{R}$ . Note that here  $\sigma^i$ ,  $\mu$ , and  $\nu$  may depend on  $\omega$ , but for the sake of simplicity we do not indicate this dependence. In this context, asset prices may have jumps that can be thought of as the result of possible shocks that may trigger the market. If the cardinality  $|E|$  of E is finite, we denote again by  $\Sigma_t$  the volatility matrix, whose row vectors are given by  $(\sigma^i(t,x))_{x\in E}, i=1,\ldots,d.$ 

**Theorem 3** (Theorem 5 of [3]). Let  $\mathbb{P} \neq \emptyset$ ,  $|E| <$  $\infty$  and  $K_t(\{x\}) > 0$  for every  $x \in E$ . Then the market is complete if and only if  $P(\text{rank}(\Sigma_t) =$  $|E|$  for almost all  $t \in [0, T] = 1$ .

Furthermore, in the case of a finite number of jumps that may trigger the economy, the characterization of market completeness is similar to the Itô price process case, that is, one needs  $|E|$  sufficiently independent processes for completeness in presence of the  $|E|$  sources of randomness, given by the  $|E|$  different possible shocks.

We have seen that the key to completeness is the predictable representation property. Hence, a natural question concerns the kind of martingales for which the predictable representation property is satisfied. For the continuous case, we have that the predictable representation property holds for diffusion processes that are martingales and have either Lipschitz coefficients [24] or a nondegenerate diffusion matrix and continuous coefficients [14]. The only one-dimensional martingales with stationary and independent increments that satisfy the predictable representation property are the Wiener and the Poisson martingales [25]. Hence the representation property holds for finite Lévy measures, but it fails for infinite Lévy measures. In the next section, we discuss the *second fundamental theorem* in the case of infinite dimensional financial markets.

#### Infinite Number of Assets

Many applications of hedging involve dynamic trading in principle in infinitely many securities, for example, in pricing of interest rate derivatives by using pure discount bonds or in the use of the term and strike structure of European put and call options to hedge exotic derivatives, when asset prices are driven by Lévy measures. Hence it is natural to develop infinite dimensional market models to address this kind of issues. The problem now is to establish if the second fundamental theorem still holds, and if the market is endowed with an infinite number of assets.

By defining a complete market via the density of a vector space, the second fundamental theorem is in [8] proved to hold true for (infinitely many) continuous and bounded asset price processes, if all the martingales with respect to the reference filtration  $\mathcal{F}_t$  are continuous ([8], Theorem 6.7). In the case of a general filtration, Theorem  $6.5$  of [8] states that completeness is equivalent for  $P^*$  to be an extreme point of  $\mathbb{P}$ , that is, a weaker version of the *second* fundamental theorem holds.

The hypothesis of continuity cannot be dropped and in the presence of jumps (discontinuities) and infinitely many assets, a counterexample to the sec*ond fundamental theorem* is provided in [2], where an economy with infinitely many assets is constructed, in which the market is complete; yet, there exists an infinity of equivalent martingale measures. Since the formulation of this counterexample, many papers have studied the problem of extending the result of the second fundamental theorem to markets with infinitely many assets. Since many definitions of completeness are possible, the solution to the counterexample of  $[2]$  relies on the choice of the definition of completeness that is adopted. A first answer to this problem was provided in 1997 by Björk et al. [5, 6], where Theorem 6.11 shows that in the presence of infinitely many assets and a continuum of jump sizes, the uniqueness of the equivalent martingale measure is equivalent to the market being *approximately complete*, that is, every bounded contingent claim can be approached in  $L^2(Q)$  for some  $Q \in \mathbb{P}$  by a sequence of hedgeable claims.

In 1999, a number of papers appeared [3, 4,  $15, 17$  at the same time, where new definitions of market completeness were proposed in order to maintain the second fundamental theorem, even in complex economies. The equivalence between market completeness and uniqueness of the pricing measure is maintained by introducing a notion of market completeness that is independent both of the notion of no arbitrage and of a chosen equivalent martingale measure. In finite-dimensional markets, the definition of market completeness is given in terms of replicating value processes in economies without arbitrage possibilities and with respect to a given equivalent martingale measure. However, the issue of completeness is about the ability to replicate certain cash flows, and not about how these cash flows are valued or whether these values are arbitrage free. From this perspective, the appropriate measure to address the issue of completeness is the statistical probability measure  $P$ , and not an equivalent martingale measure that may also not exist. In reference [17], this new approach was also motivated by the empirical asset pricing literature. Moreover, an example in [3] shows an economy where the existence of an equivalent martingale measure precludes the possibility of market completeness. Hence in references  $[3, 4, 15,$ 17], the concept of exact (almost everywhere) replication of a contingent claim *via* an admissible portfolio is substituted by the notion of approximation of a contingent claim. The main outlines of this approach are the following.

Let  $M$  denote the space of the *P*-absolutely continuous signed measures on  $\mathcal{F}_T$ . Then  $Q \in \mathbb{M}$  can be interpreted as a market agent's personal way of assigning values to claims, that is, the set M represents the possible contingent claims valuation measures held by traders. An agent using the valuation measure  $Q \in \mathbb{M}$  assigns to a contingent claim H the value  $\int H dQ$ . The fact that M is given by the Pabsolutely continuous signed measures on  $\mathcal{F}_T$  has two particular meanings: first that all traders agree on null events, and second, that there can be strictly positive random variables with negative personal value. For a given trader, represented by  $Q \in M$ , two contingent claims  $H_1$  and  $H_2$  are approximately equal if

$$\left| \int (H_1 - H_2) \, \mathrm{d}Q \right| < \epsilon \text{ for small } \epsilon > 0 \qquad (10)$$

Denote the space of all bounded contingent claims by  $C$ . The finite intersections of the sets of the form  $B(H_1,\epsilon) = \left\{ H_2 \in \mathcal{C} \mid \left| \int (H_1 - H_2) \, \mathrm{d}Q \right| < \epsilon \right\}, \ \ H_1 \in$  $\mathcal{C}$ , and  $\epsilon > 0$ , give a basis for a topology  $\tau^{\mathcal{Q}}$  on  $\mathcal{C}$ . We endow  $\mathcal{C}$  with the coarsest topology  $\tau$  finer than all of the  $\tau^Q$ ,  $Q \in \mathbb{M}$ . This topology is now agent independent, that is, two claims are approximately equal if all the agents believe that their values are close. The topology  $\tau$  is usually referred as the *weak*<sup>\*</sup> topology on  $\mathcal{C}$  [21].

An agent is then allowed to trade in a finite number of assets via self-financing, bounded, stopping time simple strategies that yield a bounded payoff at  $T$ . As in the previous section, a (bounded) claim is said to be attainable if it can be replicated by one of such strategies. In this setting, the market is said to be *quasicomplete* if any contingent claim  $H \in \mathcal{C}$ can be approximated by attainable claims in the weak\* topology induced by  $\mathbb{M}$  on  $\mathcal{C}$ . Since the weak\* topology as well as the trading strategies are agent measure independent, the same is true for this notion of completeness. Consider now the space  $\mathbb{P}_{\pm}$  of the  $P$ -absolutely continuous signed martingale measures. Then the following generalized version of the *second* fundamental theorem holds.

**Theorem 4** (The second fundamental theorem of asset pricing, Theorem 2 of [3], Theorem 1 of [4], Theorem 5 of [17]). Let  $\mathbb{P}_{\pm} \neq \emptyset$ . Then there exists a unique P-absolutely continuous signed martingale measure if and only if the market is quasicomplete.

The proof of this theorem relies on the theory of linear operators between locally convex topological vector spaces.

Since the market is endowed with an infinite number of assets, in principle, trading in infinitely many assets may be possible. To take this possibility into account, in  $[5, 6, 15, 17]$  portfolios consisting of infinitely many assets are allowed by considering measure-valued strategies. The result of Theorem 4 still holds in the case of market models where measure-valued strategies are allowed as shown in Theorem 6.11 of [5] and Theorem 2.1 of [15].

This approach resolves the paradox of the counterexample of  $[2]$ , since the economy considered in [2] is incomplete under this new definition of market completeness. Moreover, if  $\mathbb{P} \neq \emptyset$  and the number of assets is finite or the asset prices are given by continuous processes, then Theorem 5 of  $[4]$  shows that the market model is quasicomplete if and only if it is complete.

## **End Notes**

<sup>a.</sup> We say that a contingent claim is integrable if  $E^*[X/S_T^0]$  <  $\infty$ . By Definition 1, it follows that an attainable contingent claim is necessarily integrable. Hence we can restate the definition of market completeness as follows. The model is said to be *complete* if every integrable claim is attainable.

<sup>b.</sup>The price process is said to contain a redundancy if  $P(\alpha \cdot S_{t+1} = 0|A) = 1$  for some nontrivial vector  $\alpha$ , some  $t < T$ , and some  $A \in \mathcal{P}_t$ .

<sup>c.</sup>Let  $E$  be a Blackwell space. An  $E$ -multivariate point process is an integer-valued random measure on  $[0, T] \times$  $E$  with  $\mu([0, t] \times E) < \infty$  for every  $\omega, t \in [0, T]$  (see Definition III.1.23 of [13]).

## References

- [1] Arrow, K. (1964). The role of securities in the optimal allocation of risk-bearing, Review of Economics Studies 31, 91-96.
- [2] Artzner, P. & Heath, D. (1995). Approximate completeness with multiple martingale measures, Mathematical *Finance* **5**,  $1-11$ .
- Bättig, R. (1999). Completeness of securities mar-[3] ket models-an operator point of view, The Annals of Applied Probability 9, 529-566.
- Bättig, R. & Jarrow, R.A. (1999). The second funda-[4] mental theorem of asset pricing: a new approach, The Review of Financial Studies 12, 1219-1235.

- Biörk, T., Di Masi, G., Kabanov, Y. & Runggaldier, W. [5] (1997). Towards a general theory of bond markets, Finance and Stochastics 1, 141-174.
- Björk, T.G., Kabanov, Y. & Runggaldier, W. (1997). [6] Bond market structure in the presence of marked point processes. Mathematical Finance 7, 211-223.
- [7] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, Journal of Political Economy 81, 637-659.
- Delbaen, F. (1992). Representing martingale measures [8] when asset prices are continuous and bounded. Mathematical Finance 2, 107-130.
- Harrison, J.M. & Kreps, D.M. (1979). Martingales and [9] arbitrage in multiperiod securities markets. Journal of Economic Theory 20, 381-408.
- [10] Harrison, J.M. & Pliska, S.R. (1981). Martingales and stochastic integrals in the theory of continuous trading, Stochastic Processes and Their Applications 11, 215-260.
- [11] Harrison, J.M. & Pliska, S.R. (1983). A stochastic calculus model of continuous trading: complete markets. Stochastic Processes and Their Applications 15,  $313 - 316$
- [12] Jacod, J. (1979). Calcul Stochastique et Problèmes des Martingales, Lectures Notes in Mathematics, No. 714, Springer-Verlag, Berlin, Heidelberg, New York.
- [13] Jacod, J. & Shiryaev, A.N. (1987). Limit Theorems for Stochastic Processes, Springer-Verlag, Berlin, Heidelberg, New York.
- [14] Jacod, J. & Yor, M. (1977). Etude des solutions extrémales et représentation intégrales des solutions pour certains problèmes des martingales, Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete 38,  $83 - 125$
- [15] Jarrow, R.A., Jin, X. & Madan, D.B. (1999). The second fundamental theorem of asset pricing, Mathematical Finance 9, 255-273.
- [16] Jarrow, R.A. & Madan, D.B. (1991). A characterization of complete security markets on a Brownian filtration, Mathematical Finance 1, 31-43.
- [17] Jarrow, R.A. & Madan, D.B. (1999). Hedging contingent claims on semimartingales, Finance and Stochastics 3, 111-134.
- [18] Londono, J.A. (2004). State tameness: a new approach for credit constrains, Electronic Communications in Probability  $9, 1-13.$
- [19] Müller, S.M. (1989). On complete securities markets and the martingale property of securities, *Economics Letters* 31. 37-41.
- [20] Ross, S. (1976). The arbitrage theory of capital asset pricing, Journal of Economic Theory 13, 341-360.
- [21] Rudin, W. (1991). Functional Analysis, 2nd Edition, MacGraw-Hill, New York.
- Stiglitz, J. (1972). On the optimality of the stock [22] market allocation of investment, Quarterly Journal of Economics 86, 25-60.
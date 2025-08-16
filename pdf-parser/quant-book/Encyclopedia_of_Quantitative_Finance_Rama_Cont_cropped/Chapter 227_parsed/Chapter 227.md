# **Forward and Swap** Measures

Forward and swap measures are instances of general numeraire measures and are useful in interest-rate modeling and derivatives valuation. They take a zero-coupon bond and an annuity as the numeraire, respectively. Accordingly, the forward price of any asset and the instantaneous and Libor forward rates are martingales under the forward measure. Likewise, the forward swap rate is a martingale under the swap measure.

Assuming deterministic forward Libor or swap rate volatility leads to industry-standard Black-Scholes type pricing formulae for caplets and swaptions, respectively. The forward measure has other interesting applications in option pricing and in the Libor market model.

The forward measure was implicit in Merton's [7] extension of the Black-Scholes model to stochastic interest rates. Early development and application of the concept appeared in [4] and [2]. The swap measure was discussed heuristically in [8] and formalized in [5]. Forward and swap measures are instances of the change of numeraire, as described heuristically in [6] and formalized in [3].

#### **Numeraire Measures**

We take as given a stochastic basis  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t>0}, \mathbb{P})$ and a family  $(A^i)_{i \in I}$  of semimartingales. Each  $A^i$  is viewed as the observable price process of a traded zero-dividend asset. We assume that this family is arbitrage free in that there exists a positive semimartingale  $S = (S_t)$  such that  $S_- > 0$ ,  $S_0 = 1$ , and  $SA^{i}$  is a martingale for every  $i \in I$ . Such a process  $S$  is called a *state price density* (or sometimes a state price deflator, cf. Duffie [1]), and we fix one such process.(In a complete market, it is unique.)

For our purposes here, we define an *asset* as a semimartingale  $C$  such that there exist a finite subset  $J \subset I$  and bounded predictable processes  $\delta^j$ satisfying  $C = \sum_{j \in J} \delta^j A^j$  and  $dC = \sum_{j \in J} \delta^j dA^j$ . As such, an asset is the price process of a dynamic self-financing portfolio, for example, a (static) linear combination of  $A^i$ . The  $\delta^j$  are called the *deltas* or the *hedge ratios*.

It can be shown that  $SC$  is a martingale for any asset C. This implies the law of one price: if two assets have almost surely the same prices at some time  $T$ , then they will have identical prices at all times  $t < T$ .

Let  $N$  be a *numeraire*, that is, a positive asset. For each  $T > 0$  define the measure  $\mathbb{P}^{\bar{N},T}$  on  $\mathcal{F}_T$  via its Radon-Nikodym derivative by

$$\frac{\mathrm{d}\mathbb{P}^{N,T}}{\mathrm{d}\mathbb{P}} = \frac{S_T N_T}{N_0} \tag{1}$$

This is an equivalent probability measure and is called the associated *equivalent martingale measure* or numeraire measure. Since  $SN$  is a martingale, for any  $s < T$ , the restriction of  $\mathbb{P}^{N,T}$  to  $\mathcal{F}_s$  equals  $\mathbb{P}^{N,s}$ . (In an incomplete market,  $\mathbb{P}^{N,T}$  depends on the choice of  $S$ .)

By an easy and well-known consequence of the Bayes' rule, given a process  $C$ , the process  $SC$  is a  $\mathbb{P}$ -martingale on [0, T] if and only if  $C/N$  is a  $\mathbb{P}^{N,T}$ martingale on  $[0, T]$ . In particular, this holds for all assets C, yielding for  $t < T$  the pricing formula,

$$C_t = N_t \mathbb{E}^{\mathbb{P}^{N,T}} \left[ \frac{C_T}{N_T} \mid \mathcal{F}_t \right] \tag{2}$$

A useful technique is the *change of numeraire*. Suppose *B* is another numeraire and *M* is a  $\mathbb{P}^{N,T}$ martingale. Note that both  $F := N/B$  and  $MF$  are  $\mathbb{P}^{B,T}$ -martingales. Hence, using Itô's product rule,  $\int F_{-}dM + [M, F]$  is a  $\mathbb{P}^{B,T}$ -local martingale. (Here,  $[M, F]$  denotes the quadratic covariation of  $M$  and F.) Thus, dividing by  $F_{-}$ , so is  $M + \int d[M, F]/F_{-}$ . In particular, if F is continuous, then the  $\mathbb{P}^{B,T}$ -drift of M equals  $-d[M, \log F]$ .

## The Forward Measure

For a fixed maturity  $T$ , let us assume there exists an asset  $P^T$  such that  $P_T^T = 1$ . Such an asset, called the T-maturity zero-coupon bond, is necessarily positive and unique on  $[0, T]$  by the law of one price. Its associated numeraire measure on  $\mathcal{F}_T$  is called the *T*-forward measure and denoted  $\mathbb{P}^T$ . Its expectation operator is denoted  $\mathbb{E}^T$ . Since  $P_T^T = 1$ , by equation  $(1)$ 

$$\frac{\mathrm{d}\mathbb{P}^T}{\mathrm{d}\mathbb{P}} = \frac{S_T}{P_0^T} \tag{3}$$

By equation (2), the *T*-forward price  $C/P^T$  of any asset C is a  $\mathbb{P}^T$ -martingale on [0, T] and

$$C_t = P_t^T \mathbb{E}^T [C_T \mid \mathcal{F}_t] \tag{4}$$

The price of a European thus equals the discounted expected value of its payoff.

Another important property is that *forward interest* rates are martingales under the forward measure. The simple (or Libor) *T*-forward rate  $L^{T,\varepsilon}$  of length  $\varepsilon > 0$ is defined by

$$L_t^{T,\varepsilon} := \frac{P_t^{T-\varepsilon} - P_t^T}{\varepsilon P_t^T} \tag{5}$$

Assuming that  $P^{T-\varepsilon}$  is an asset,  $P^{T-\varepsilon}/P^{T}$ , and with it.  $L^{T,\varepsilon}$  is a  $\mathbb{P}^T$ -martingale.

As  $\varepsilon$  approaches zero,  $L_t^{T,\varepsilon}$  approaches the instantaneous forward rate  $f_t^T$  defined by

$$f_t^T := -\frac{\partial \log(P_t^T)}{\partial T} \tag{6}$$

As such, in the limit, the instantaneous forward rate process  $f^T$  is also a  $\mathbb{P}^T$ -martingale.

### **Option Pricing and Hedging**

Consider a  $T$ -expiry option on an asset  $A$  (e.g. a stock or a bond) with time T-payoff  $g(A_T)$ , where  $g(x)$ is a Borel function of linear growth. For example,  $g(x) = \max(x - K, 0)$  for a call option struck at K. We wish to construct an asset C satisfying  $C_T =$  $g(A_T)$ . From equation (4), we know that the only possible candidate is  $C = P^T F$ , where

$$F_t := \mathbb{E}^T[g(A_T) \,|\, \mathcal{F}_t] \tag{7}$$

This works if we assume the process  $X := A/P^{T}$  is continuous and  $F_t = f(t, X_t)$  for some  $C^{1,2}$  function  $f(t, x)$ . The desired deltas (hedge ratios) are then simply given by

$$\delta_t^A := \frac{\partial f}{\partial x}(X_t, t), \quad \delta^P := F - \delta^A X \qquad (8)$$

Indeed,  $C := P^T F = \delta^A A + \delta^P P^T$  obviously. Moreover, since both X and F are  $\mathbb{P}^T$ -martingales, Itô's formula implies  $dF = \delta^A dX$ . An application of Itô's product rule known as the *numeraire-invariance theorem* cf. [1]), then shows that  $dC = \delta^A dA + \delta^P dP^T$ .

The above Markovian assumption that  $F_t =$  $f(t, X_t)$  for some function  $f(t, x)$  is generally satisfied when  $X$  is a positive diffusion, specifically when  $d[X]_t = X_t^2 \sigma^2(t, X_t) dt$  for some positive continuous bounded function  $\sigma(t, x)$ . (Here [X] denotes the quadratic variation of  $X$ .) This is equivalent to  $dX_t = X_t \sigma(t, X_t) dW_t$  for some  $\mathbb{P}^T$ -Brownian motion W. In this case,  $f(t, x)$  is basically obtained as  $\mathbb{E}^T[g(X_T) | X_t = x]$ . By Itô's formula,  $f(t, x)$ satisfies

$$\frac{\partial f}{\partial t} + \frac{1}{2}x^2\sigma^2(t,x)\frac{\partial^2 f}{\partial x^2} = 0 \qquad (f(x,T) = g(x))$$
(9)

## **Closed-form Solutions**

The classical case assumes as in  $[7]$  that the forward price volatility  $\sigma(t, X_t)$  is deterministic, that is, independent of X. Then X is a  $\mathbb{P}^T$  log-Gaussian martingale, and hence conditioned on time t,  $X_T =$  $A_T$  is  $\mathbb{P}^T$ -lognormally distributed with mean  $X_t$  and log-variance  $\int_{t}^{T} \sigma^{2}(s) ds$ . As such, for, say, a call option with payoff function  $g(x) = \max(x - K, 0)$ , equation  $(7)$  readily yields

$$C(t) = K P_t^T \mathbf{C}_{\mathbf{BS}} \left( \frac{A_t}{P_t^T K}, \int_t^T \sigma^2(t) \, \mathrm{d}t \right) \tag{10}$$

where, denoting the standard normal distribution function by  $N(\cdot)$ ,

$$C_{\text{BS}}(x,v) := xN \left( \frac{\log(x)}{\sqrt{v}} + \frac{\sqrt{v}}{2} \right)$$
$$- N \left( \frac{\log(x)}{\sqrt{v}} - \frac{\sqrt{v}}{2} \right) \quad (11)$$

Specific examples are the Vasicek or more general Gaussian interest-rate models (see Gaussian Interest-Rate Models) where the deterministic (forward) zero-coupon bond price volatilities are determined endogenously in terms of mean reversion and other model parameters. For zero-coupon bond options, equation (7) can be computed in the  $Cox$ -Ingersoll-Ross model (see Cox-Ingersoll-Ross (CIR) Model) and the quadratic Gaussian model (see Quadratic Gaussian Models) in terms of the noncentral chi-squared distribution function. This is derived by showing that the spot interest rate  $r_T :=$  $f_T^T$  is noncentral chi-squared distributed under the forward measure  $\mathbb{P}^T$  (e.g., [4]).

## **Cap Pricing**

A cap is a portfolio of consecutive caplets, and a caplet of maturity T, length  $\varepsilon$ , and strike rate K is an option with payoff  $\varepsilon \max(L_{T-\varepsilon}^{T,\varepsilon}-K,0)$  at time T. A caplet is actually equivalent to a zero-coupon bond put option, so a bond option model as in the previous section is applicable. However, more directly, by the pricing formula given by equation  $(4)$  the caplet price  $C_t$  is given by

$$C_{t} = \varepsilon P_{t}^{T} \mathbb{E}^{T} [\max(L_{T-\varepsilon}^{T,\varepsilon} - K, 0) | \mathcal{F}_{t}]$$
 (12)

By the section The Forward Measure, the forward Libor process  $L^{T,\varepsilon}$  is a martingale under the forward measure  $\mathbb{P}^T$ . Hence, if its volatility  $\sigma(t)$  is deterministic, it is log-Gaussian and we get, as in, the section Closed-form Solutions,

$$C_{t} = \varepsilon K P_{t}^{T} \mathbf{C}_{\mathbf{BS}} \left( \frac{L_{t}^{T,\varepsilon}}{K}, \int_{t}^{T} \sigma^{2}(t) \, \mathrm{d}t \right) \tag{13}$$

## The Forward Measure by Changing the **Risk-neutral Measure**

Let  $r_t := f_t^t$  denote the spot interest rate. One often starts with the "money market" asset  $\exp(\int_0^{\cdot} r_t dt)$ as the numeraire and uses its equivalent martingale measure, often called the risk-neutral measure and denoted by  $\mathbb{Q}$ . Accordingly,  $\exp(-\int_0^t r_t dt)C$  is a  $\mathbb{Q}$ martingale for any asset  $C$ . One can then change the numeraire to the T-maturity bond  $P^T$  and obtain the  $T$ -forward measure  $\mathbb{P}^T$  by the formula

$$\frac{d\mathbb{P}^T}{d\mathbb{Q}} = \frac{1}{P_0^T} \exp\left(-\int_0^T r_t \, \mathrm{d}t\right) \tag{14}$$

Since the forward rate process  $f^T$  is a  $\mathbb{P}^T$ martingale, it follows from the section Numeraire Measures that when  $P^T$  is continuous, the  $\mathbb{Q}$ -drift of  $f^T$  equals  $-\mathrm{d}[\log P^T, f^T]$ .

## Libor Market Model SDE in the Forward Measure

Consider a sequence of dates  $0 < T_1 \cdots < T_{n+1}$ , for example, equidistant semiannually. Given "daycount fractions"  $\varepsilon_i \approx T_{i+1} - T_i$ , the forward Libor rates  $L_t^i$ 

are defined as in the section The Forward Measure by

$$\varepsilon_i L_t^i = \frac{P_t^{I_i}}{P_t^{T_{i+1}}} - 1 \qquad (t \le T_i, \ i = 1, \dots, n) \tag{15}$$

Evidently,  $L^i$  is a  $\mathbb{P}^{T_{i+1}}$ -martingale on [0,  $T_i$ ].

In some applications such as valuation by Monte Carlo simulation, it is necessary to determine the dynamics of all the forward Libor processes  $L^i$  under the same measure. One appropriate measure is the spot-Libor measure, a simple-compounding analog of the risk-neutral measure that takes as numeraire a "rolling zero-coupon bond" (cf. [5]). Another convenient measure is the terminal measure, that is, the  $T_{n+1}$ -forward measure  $\mathbb{P}^{T_{n+1}}$ . Let  $W^1, \ldots, W^n$  be  $\mathbb{P}^{T_{n+1}}$ -Brownian motions with correlations  $\rho^{ij}$ , that is,  $d[W^i, W^j]_t = \rho^{ij}_t dt$ . Assume

$$\mathrm{d}L_t^i = \mu_t^i \,\mathrm{d}t + \sigma_t^i \,\mathrm{d}W_t^i \tag{16}$$

for some predictable processes  $\mu^i$  and  $\sigma^i$ . For example, in the deterministic-volatility Libor market model,  $\sigma_t^i = \sigma_i(t) L_t^i$  for some deterministic functions  $\sigma_i(t)$ . Since  $L^i$  is a  $\mathbb{P}^{T_{i+1}}$ -martingale, it follows from the section Numeraire Measures that  $\mu^i dt =$  $-\mathrm{d}[L^i,\log F]$ , where

$$F := \frac{P^{T_{i+1}}}{P^{T_{n+1}}} = \prod_{j=i+1}^{n} (1 + \varepsilon_j L^j) \tag{17}$$

Therefore, the drift of the forward Libor rate in the terminal measure is given by

$$\mu^{i} dt = -\sum_{j=i+1}^{n} \frac{\varepsilon_{j} d[L^{i}, L^{j}]}{1 + \varepsilon_{j} L^{j}}$$
$$= -\sum_{j=i+1}^{n} \frac{\varepsilon_{j} \sigma^{i} \sigma^{j} \rho^{ij}}{1 + \varepsilon_{j} L^{j}} dt \qquad (18)$$

#### **The Swap Measure**

Let  $T_i$  and  $\varepsilon_i$  be as in the previous section. For each  $1 \leq i \leq j$ , the swap measure  $\mathbb{P}^{ij}$  is defined on  $\mathcal{F}_{T_{i+1}}$ as the equivalent martingale measure associated with the annuity numeraire

$$A^{ij} := \varepsilon_i P^{T_{i+1}} + \dots + \varepsilon_{j-1} P^{T_j} \tag{19}$$

The forward swap rate  $S_t^{ij}$  with start date  $T_i$  and end date  $T_i$  is defined for  $t \leq T_i$  by

$$S_t^{ij} := \frac{P_t^{T_i} - P_t^{T_j}}{A_t^{ij}} \tag{20}$$

It follows from the section Numeraire Measures that  $S^{ij}$  is a martingale under the swap measure  $\mathbb{P}^{ij}$ .

The main application of the swap measure is to European swaptions, that is, options to enter an interest-rate swap at a fixed strike rate. Specifically, a payer swaption with start date  $T_i$ , end date  $T_i$ , expiration  $T \leq T_i$  and strike rate K has the payoff  $C_T$  at time T given by

$$C_T = A_T^{ij} \max(S_T^{ij} - K, 0) \tag{21}$$

(When  $j = i + 1$ , a payer swaption is just a caplet). Arguments similar to those in the section Option Pricing and Hedging show that the swaption is replicable under general diffusion assumptions, for example, when  $S^{ij}$  has deterministic volatility or, more generally, when it is a diffusion process under the swap measure  $\mathbb{P}^{ij}$ . The swaption price process C is then uniquely characterized by  $C/A^{ij}$  being a  $\mathbb{P}^{ij}$ martingale, implying by equation  $(21)$  that

$$C_t = A_t^{ij} \mathbb{E}^{\mathbb{P}^{ij}} [\max(S_T^{ij} - K, 0) \mid \mathcal{F}_t] \qquad (22)$$

When  $S^{ij}$  has a deterministic volatility  $\sigma_{ij}(t)$  (i.e.,  $d[S^{ij}]_t = \sigma_{ii}^2(t)(S_t^{ij})^2 dt$ , this yields

$$C_t = K A_t^{ij} C_{\text{BS}} \left( \frac{S_t^{ij}}{K}, \int_t^T \sigma_{ij}^2(t) \, \text{d}t \right) \tag{23}$$

The market uses this formula to quote swaptions, namely a constant volatility  $\sigma_{ij}$  is quoted from which one computes the swaption price by equation  $(23)$ . Receiver swaptions are treated similarly.

The valuation of Bermudan options is more complex. Here, the swaption can be exercised at any time  $T_i, \ldots, T_{i-1}$ . One approach, known as the coterminal swap market model, assumes that the forward swap rates  $S^{ij}, \ldots, S^{j-1,j}$  all have deterministic volatilities. According to equation (23), the model is then automatically calibrated to all the European swaptions with start dates  $T_i, \ldots, T_{i-1}$  and the same end date  $T_i$ , thus ruling out obvious arbitrage opportunities.

Constructs similar to the swap measure have been applied to credit default swaptions.

#### References

- Duffie, D. (2001). Dynamic Asset Pricing Theory, 3rd [1] Edition, Princeton University Press.
- [2] Geman, H. (1989). The Importance of the Forward Neutral Probability in a Stochastic Approach of Interest Rates, ESSEC working paper.
- [3] Geman, H., El-Karoui, N. & Rochet, J.C. (1995). Change of numeraire, change of probability measure, and option pricing, Journal of Applied Probability 32, 443-458.
- [4] Jamshidian, F. (1987). Pricing of Contingent Claims in the One-Factor Term Structure Model, working paper, appeared in Vasicek and Beyond, Risk Publications,  $(1996).$
- [5] Jamshidian, F. (1997). Libor and swap market model and measures. Finance and Stochastics 1, 293-330.
- Margrabe, W. (1978). The value of an option to exchange [6] one asset for another, Journal of Finance 33, 177-186.
- [7] Merton, R. (1973). Theory of rational option pricing, *Bell* Journal of Economics  $4(1)$ ,  $141-183$ .
- [8] Neuberger, A. (1990). Pricing Swap Options Using the Forward Swap Market, IFA Preprint.

### **Related Articles**

Caps and Floors; Change of Numeraire; Exchange Options: Itô's Formula: LIBOR Market Model; LIBOR Rate; Martingales; Term Structure Models; Swap Market Models.

FARSHID JAMSHIDIAN
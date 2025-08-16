# **Weighted Variance Swap**

Let the underlying process *Y* be a semimartingale taking values in an interval *I* . Let *ϕ* : *I* → be a difference of convex functions, and let *X* := *ϕ(Y )*. A typical application takes *Y* to be a positive price process and *ϕ(y)* = log *y* for *y* ∈ *I* = *(*0*,*∞*)*.

Then (the floating leg of) a forward-starting *weighted variance swap* or *generalized variance swap* on *ϕ(Y )* (shortened to "on *Y* " if the *ϕ* is understood), with *weight* process *wt* , forward-start time *θ*, and expiry *T* , is defined to pay, at a fixed time *T*pay ≥ *T >θ* ≥ 0,

$$\int_{\theta}^{T} w_t \, \mathrm{d}[X]_t \tag{1}$$

where [·] denotes quadratic variation. In the case that *θ* = 0, the trade date, we have a spot-starting weighted variance swap. The basic cases of weights take the form *wt* = *w(Yt)*, for a measurable function *w* : *I* → [0*,*∞*)*, such as the following.

- 1. The weight *w(y)* = 1 defines a *variance swap* (*see* **Variance Swap**).
- 2. The weight *w(y)* = 11*y*∈*C*, the indicator function of some interval *C*, defines a *corridor variance swap* (*see* **Corridor Variance Swap**) with corridor *C*. For example, a corridor of the form *C* = *(*0*,H)* produces a *down* variance swap.
- 3. The weight *w(y)* = *y/Y*<sup>0</sup> defines a *gamma swap* (*see* **Gamma Swap**).

## **Model-free Replication and Valuation**

Assuming a deterministic interest rate *rt* , let *Zt* be the time-*t* price of a bond that pays 1 at time *T*pay. Assume that *Y* is the continuous price process of a share that pays continuously a deterministic proportional dividend *qt* . Let

$$Z_{t} = \exp\left(-\int_{t}^{T_{\text{pay}}} r_{u} \, \mathrm{d}u\right) \quad \text{and}$$
$$Q_{t} := \exp\left(\int_{0}^{t} q_{u} \, \mathrm{d}u\right) \tag{2}$$

so the share price with reinvested dividends is *YtQt* . Then the payoff

$$\int_{\theta}^{T} w(Y_t) \, \mathrm{d}[X]_t \tag{3}$$

admits a model-independent replication strategy, which holds European options statically and trades the underlying shares dynamically. Indeed, let *λ* : *I* → be a difference of convex functions, let *λy* denote its left-hand derivative, and assume that its second derivative in the distributional sense has a signed density, denoted *λyy* , which satisfies for all *y* ∈ *I*

$$\lambda_{yy}(y) = 2\varphi_y^2(y)w(y) \tag{4}$$

where *ϕy* denotes the left-hand derivative of *ϕ*. Then

$$\begin{split} \int_{\theta}^{T} w(Y_{t}) \, \mathrm{d}[X]_{t} \\ &= \lambda(Y_{T}) - \lambda(Y_{\theta}) - \int_{\theta}^{T} \lambda_{y}(Y_{t}) \, \mathrm{d}Y_{t} \qquad (5) \\ &= \lambda(Y_{T}) - \lambda(Y_{\theta}) + \int_{\theta}^{T} (q_{t} - r_{t}) \lambda_{y}(Y_{t}) Y_{t} \, \mathrm{d}t \\ &- \int_{\theta}^{T} \lambda_{y}(Y_{t}) \frac{Z_{t}}{Q_{t}} \, \mathrm{d}(Y_{t} Q_{t}/Z_{t}) \qquad (6) \end{split}$$

where equation (5) is by a proposition in [2] that slightly extends [1], and equation (6) is by Ito's rule. So the following self-financing strategy replicates (and hence prices) the payoff (3). Hold statically a claim that pays at time *T*pay

$$\lambda(Y_T) - \lambda(Y_\theta) + \int_\theta^T (q_\tau - r_\tau) \lambda_y(Y_\tau) Y_\tau \, \mathrm{d}\tau \quad (7\text{a})$$

and trade shares dynamically, holding at each time *t* ∈ *(θ , T )*

$$-\lambda_{y}(Y_{t})Z_{t} \quad \text{shares} \tag{7b}$$

and a bond position that finances the shares and accumulates the trading gains or losses. Hence, the payoff (3) has time-0 value equal to that of the replicating claim (7a), which is synthesizable from Europeans with expiries in [*θ,T* ]. Indeed, for a put/call separator *κ* (such as *κ* = *Y*0), if *λ(κ)* = *λy (κ)* = 0, then each *λ* claim decomposes into puts/calls at all strikes *K*, with quantities 2*ϕ*<sup>2</sup> *<sup>y</sup> (K)w(K)* d*K*:

$$\lambda(y) = \int_{I} 2\varphi_{y}^{2}(K)w(K)\text{Van}(y, K) \, \mathrm{d}K \qquad (8)$$

where Van*(y, K)*:= *(K* − *y)*<sup>+</sup>11*K<κ*+*(y* − *K)*<sup>+</sup>11*K>κ* denotes the vanilla put or call payoff. For put/call decompositions of general European payoffs, see [1].

## **Futures-dependent Weights**

In equation (3), the weight is a function of spot *Yt* . The alternative payoff specification

$$\int_{\theta}^{T} w(Y_{t}Q_{t}/Z_{t}) \, \mathrm{d}[X]_{t} \tag{9}$$

makes *wt* a function of the *futures* price (a constant times *YtQt /Zt*).

In the case *ϕ* = log, we have [*X*] = [log *Y* ] = [log*(YQ/Z)*]; hence

$$\begin{split} \int_{\theta}^{T} w \big( Y_{t} Q_{t} / Z_{t} \big) \, \mathrm{d}[X]_{t} \\ &= \lambda \Big( \frac{Y_{T} Q_{T}}{Z_{T}} \Big) - \lambda \Big( \frac{Y_{\theta} Q_{\theta}}{Z_{\theta}} \Big) \\ &- \int_{\theta}^{T} \lambda_{y} (Y_{t} Q_{t} / Z_{t}) \, \mathrm{d}(Y_{t} Q_{t} / Z_{t}) \end{split}$$

for *λ* satisfying equation (4). So the alternative payoff (9) admits replication as follows: hold statically a claim that pays at time *T*pay

$$\lambda(Y_T Q_T / Z_T) - \lambda(Y_\theta Q_\theta / Z_\theta) \tag{10a}$$

and trade shares dynamically, holding at each time *t* ∈ *(θ , T )*

$$-\lambda_{y}(Y_{t}Q_{t}/Z_{t})Q_{t} \quad \text{shares} \qquad (10b)$$

and a bond position that finances the shares and accumulates the trading gains or losses. Thus, the payoffs (9) and (10a) have equal values at time 0.

In special cases (such as *w* = 1 or *r* = *q* = 0), the spot-dependent (3) and futures-dependent (9) weight specifications are equivalent. In general, the spotdependent weighting is harder to replicate, as it requires a continuum of expiries in equation (7a), unlike equation (10a). The spot-dependent weighting is, however, the more common specification and is assumed in remainder of this article.

## **Examples**

Returning to the previously specified examples of weights *w(Yt)*, we express the replication payoff *λ* in a compact formula, and also expanded in terms of vanilla payoffs according to equation (8). We take *ϕ(y)* = log *y* unless otherwise stated.

• *Variance swap*: Equation (4) has solution

$$\lambda(y) = -2 \log(y/\kappa) + 2y/\kappa - 2$$
$$= \int_0^\infty \frac{2}{K^2} \text{Van}(y, K) \, \text{d}K \qquad (11)$$

• *Arithmetic variance swap*: For *ϕ(y)* = *y*, equation (4) has solution

$$\lambda(y) = (y - \kappa)^2 = \int_0^\infty 2 \operatorname{Van}(y, K) \, dK \quad (12)$$

• *Corridor variance swap*: Equation (4) has solution

$$\lambda(y) = \int_{K \in C} \frac{2}{K^2} \operatorname{Van}(y, K) \, \mathrm{d}K \tag{13}$$

• *Gamma swap*: Equation (4) has solution

$$\lambda(y) = \frac{2}{Y_0} \Big[ y \log(y/\kappa) - y + \kappa \Big]$$
$$= \int_0^\infty \frac{2}{Y_0 K} \text{Van}(y, K) \, \mathrm{d}K \qquad (14)$$

In all cases, the strategy (7) replicates the desired contract. In the case of a variance swap, the strategy (10) also replicates it, because *w(Y )* = 1 = *w(YQ/Z)*.

## **Discrete Dividends**

Assume that at the fixed times *tm* where *θ* = *t*<sup>0</sup> *< t*<sup>1</sup> *<* ··· *< tM* = *T* , the share price jumps to *Ytm* = *Ytm*<sup>−</sup> − *δm(Ytm*−*)*, where each discrete dividend is given by a function *δm* of prejump price. In this case, the dividend-adjusted weighted variance swap can be defined to pay at time *T*pay

$$\sum_{m=1}^{M} \int_{t_{m-1}+}^{t_{m}-} w(Y_t) \, \mathrm{d}[X]_t \tag{15}$$

If the function  $y \mapsto y - \delta_m(y)$  has an inverse  $f_m: I \to I$ , and if Y is still continuous on each  $[t_{m-1}, t_m)$ , then each term in equation (15) can be constructed via equation (7), together with the relation  $\lambda(Y_{t_{m-}}) = \lambda(f_m(Y_{t_m}))$ . Specifically, the *m*th term admits replication by holding statically a claim that pays at time  $T_{\text{pay}}$ 

$$\lambda(f_m(Y_{t_m})) - \lambda(Y_{t_{m-1}})$$
  
+ 
$$\int_{t_{m-1}}^{t_m} (q_\tau - r_\tau) \lambda_y(Y_\tau) Y_\tau \ d\tau \qquad (16)$$

and holding dynamically  $-\lambda_{\nu}(Y_t)Z_t$  shares, at each time  $t \in (t_{m-1}, t_m)$ .

#### **Contract Specifications in Practice**

In practice, weighted variance swap transactions are forward settled; no payment occurs at time 0, and at time  $T_{\text{pay}}$  the party long the swap receives the total payment

$$Notional \times (Floating - Fixed) \tag{17}$$

where "fixed" (also known as the strike), expressed in units of annualized variance, is the price contracted at time 0 for time- $T_{\text{pay}}$  delivery of "floating", an annualized discretization of equation (15) that monitors  $Y$ , typically daily, for  $N$  periods. In the usual case of  $\varphi = \log$ , this results in a specification

 $Floating := Annualization$ 

$$\times \sum_{n=1}^{N} w(Y_n) \left( \log \frac{Y_n + D_n}{Y_{n-1}} \right)^2 \quad (18)$$

where  $D_n$  denotes the discrete dividend payment, if any, of the  $n$ th period. Both here and in the theoretical form (15), no adjustment is made for any dividends deemed to be continuous (for example, index variance contracts typically do not adjust for index dividends; see [3]).

In some contracts—for example, single-stock (down-)variance—the risk to the variance seller that  $Y$  crashes is limited by imposing a cap on the payoff. Hence,

$$Notional \times \Big( \min(Floating, Cap \times Fixed) - Fixed \Big)$$
(19)

replaces equation (17), where "Cap" is an agreed constant, such as the square of  $2.5$ .

## References

- [1] Carr, P. & Madan, D. (1998). Towards a theory of volatility trading, in Volatility, R. Jarrow, ed, Risk Publications, рр. 417-427.
- [2] Carr, P. & Lee, R. (2009). *Hedging Variance Options on* Continuous Semimartingales, Forthcoming in Finance and Stochastics.
- [3] Overhaus, M., Bermúdez, A., Buehler, H., Ferraris, A., Jordinson, C. & Lamnouar, A. (2007). Equity Hybrid Derivatives, John Wiley & Sons.

#### **Related Articles**

Corridor Variance Swap; Gamma Swap; Variance Swap.

ROGER LEE
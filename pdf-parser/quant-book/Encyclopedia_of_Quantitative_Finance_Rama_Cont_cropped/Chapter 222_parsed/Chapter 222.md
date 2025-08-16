# **Trigger Swaps**

We discuss two classes of exotic interest rate derivatives: trigger swaps and targeted accrual redemption notes (TARNs). Subsequently, we outline possible valuation methodologies and assess the impact on the quality of risk estimates.

A trigger swap features an underlying swap. Cash flows of this underlying swap only start to be exchanged from the moment that a certain trigger condition is met. An example trigger condition is that some trigger index should be within a prespecified range. These are barrier type options, *see* **Barrier Options**.

The above-described trigger swap is of *knock-in* type, as opposed to a *knock-out* feature with which a swap is cancelled when the trigger index ends up in a prespecified range. There is a simple relation between an underlying swap and its knock-in and knock-out variants:

value of swap = value of knock-in swap

+ value of knock-out swap

The above relation shows that the ability to value knock-out swaps also yields the ability to value knock-in swaps. Hence in the remainder of the article, we restrict the discussion to knock-out swaps.

A TARN is a trigger swap where the trigger index is the cumulative sum of structured coupons paid, typically of knock-out type. In this case, the barrier is referred to as a *lifetime cap*.

Example term sheets of a knock-in swap and a TARN are displayed in Tables 1 and 2, respectively. Both term sheets feature structured coupons that are exchanged for IBOR plus spread—this is more or less the general rule. There are several variations often applied to the basic TARN design:

- 1. The form in Table 2 is referred to as *partial final coupon* in order to exactly attain the lifetime cap.
- 2. The latter is in contrast to a *full-final coupon* where an excess over the lifetime cap is allowed.
- 3. If the sum of coupons is below target at maturity, then a *lifetime floor* dictates that a make up coupon be paid to attain the target.

#### *Valuation*

We focus the discussion primarily on valuation methods, such as a Markovian grid or Monte Carlo simulation. The presentation is more or less independent of model choice, unless explicitly mentioned otherwise.

It is well known that simulation-based risk estimates for derivatives with discontinuous payoff are less efficient than for those with continuous payoff. In contrast, a Markovian grid naturally provides high-quality risk estimates, as the backward induction expectation operator has a smoothing effect—as long as interpolation is dealt with properly. Knock-out features can be easily valued on a grid as the value of a knock-out swap is simply 0 for those state nodes for which the trigger index is within the knock-out range. Path-dependent aspects such as the cumulative coupon trigger index of TARNs may be incorporated by adding a dimension to the Markovian grid that keeps track of the cumulative coupon.

Although a Markovian grid has excellent credentials, the alternative of simulation may also successfully be applied. Its drawback—as mentioned above—lies in less than efficient estimates of risk sensitivities. The remainder of the article outlines four techniques to improve risk estimates for trigger swaps in a simulation framework: (i) large shifts, (ii) importance sampling (IS), (iii) conditioning, and (iv) smoothing.

All of the described methods may also be found in the article overview paper of Piterbarg (2004, [1]).

#### *Large Shift Sizes*

Ordinary simulation, without further enhancements, remains a viable technique of obtaining risk estimates. In the general case, risk sensitivities are calculated *via* finite differences, for which we must specify a shift size. For continuous payoffs, it is more efficient to use "smaller" shift sizes (say of the order 10<sup>−</sup>8). However, for discontinuous payoffs, this is not the case as small shift sizes mostly ignore the risk component due to the digital option embedded in the knock-out structure. With discontinuous payoffs, it is more efficient to use somewhat larger shift sizes, say of the order of 1 basis point.

### *Importance Sampling (IS)*

IS is typically used to reduce the variance of the simulation estimate. (For an overview of variance

| Product  | CMS spread knock-out                |
|----------|-------------------------------------|
| Currency | CCY                                 |
| Maturity | $X$ years                           |
| Receive  | Float funding plus margin           |
| Pay      | $Y \times$ (CCY CMS10-CMS2)         |
|          | Annually, floor at $0\%$            |
|          | If on any day the spread            |
|          | CCY CMS10-CMS2 $\geq$ B% then from  |
|          | the next coupon period onwards a    |
|          | fixed rate of $Z\%$ knocks in until |
|          | maturity of the trade               |
|          |                                     |

| Table 1 | Example knock-in swap |  |  |
|---------|-----------------------|--|--|
|---------|-----------------------|--|--|

| Example TARN<br>Table 2 |  |
|-------------------------|--|
|-------------------------|--|

| Product  | Guaranteed inverse floater swap       |
|----------|---------------------------------------|
| Currency | CCY                                   |
| Maturity | $X$ years                             |
| Receive  | Float funding plus margin             |
| Pay      | $Y - Z \times$ CCY 6M IBOR in arrears |
|          | Semi-annually, floor at $0\%$         |
|          | If on any day the sum of              |
|          | structured coupons $\geq B\%$         |
|          | then pay $B\%$ -[sum of coupons]      |
|          | and the trade cancels thereafter      |

reduction techniques, see Variance Reduction.) For knock-outs; however, the simulation value estimate is usually of desirable quality. It is, however, a side effect of IS that we are interested in. With IS, we sample conditional on knocking out or in. Realizations of these conditional samples then need to be multiplied by the likelihood ratio, which is a measure for the probability of the conditional event. These likelihood ratios smoothen the valuation and cause the discontinuity to disappear. Hence, we obtain efficient risk. See Glasserman and Staum [2].

#### Conditioning

Conditioning is specifically geared toward TARNs. With TARNs, each cash flow is contingent on a sum of index rates being within range. We focus on the valuation of one TARN cash flow, since we may value the whole TARN if we can value all cash flows. We halt the simulation when the penultimate index rate is determined. Subsequently, the remaining cash flow is a digital option with underlying rate the final index rate that determines whether or not we obtain the TARN cash flow. This digital option may be valued analytically with a Black-type formulathe latter provides smoothing, from which we obtain more efficient risk estimates.

#### Smoothing

For knock-outs, we observe a trigger index  $x$ . If the trigger is outside of the survival range  $[L, U]$ , then the trade knocks out. We assume  $L \leq U$ . We consider the survival ratio  $A_i$  for each cash flow *i*. The survival ratio  $A_i$  is either 0 or 1. It evolves from cash flow to cash flow as follows:

$$A_{i+1} = A_i \times \left(1 - R_i^{\text{KO}}\right) \tag{1}$$

The quantity  $R_i^{\text{KO}}$  is the knock-out ratio. For the remainder of the presentation, we omit the cash flow index *i* for convenience. The knock-out ratio  $R^{\text{KO}}$  is either  $0$  or  $1$ , and is given by:

 $\sim$ 

$$R^{\text{KO}} = 1\{x < L\} + 1\{x > U\} \tag{2}$$

A smoothed version of the function in equation  $(2)$ is easily devised. An example is given in Figure 1. The smoothed function may be parameterized. For "small" parameters, the smoothed version is hardly distinguishable from the original discontinuous function. The use of "large" parameters leads to an intolerable bias in the derivative value. Experience and testing may provide guidance in selecting a parameter that bares acceptable bias yet sufficiently improves risk sensitivity estimates.

We test smoothing for a trade such as given in Table 1. We use  $10^{-6}$ bps ("small") shift for smooth and 0.5 bps ("large") for nonsmooth. The terminology

![](_page_1_Figure_16.jpeg)

**Figure 1** Knock-out ratio *versus* trigger index  $x$ , with lower and upper knock-out barriers  $L$  and  $U$ . Discontinuous, according to contract (full line) and smoothed (dotted line)

| Table 3 |  | P&L prediction results |  |
|---------|--|------------------------|--|
|---------|--|------------------------|--|

| −10 bps                            | −1 bps                           | 0 bps                                           | 1 bps                           | 10 bps                           |
|------------------------------------|----------------------------------|-------------------------------------------------|---------------------------------|----------------------------------|
|                                    |                                  |                                                 |                                 |                                  |
| 1 005 251<br>−1266<br>−1597<br>331 | 994 113<br>−1519<br>−2042<br>523 | 992 594                                         | 990 804<br>−1790<br>−1871<br>82 | 981 537<br>−1106<br>−1772<br>667 |
|                                    |                                  |                                                 |                                 |                                  |
| 1 002 928<br>−1227<br>−1226<br>−1  | 991 884<br>−1228<br>−1228<br>0   | 990 656                                         | 989 429<br>−1227<br>−1227<br>0  | 978 420<br>−1224<br>−1223<br>−1  |
|                                    |                                  | Nonsmooth, large shifts<br>Smooth, small shifts |                                 |                                  |

"Pred" means predicted P&L. Market data and other data used for this test may be obtained from the author upon request

is as follows: NPV, trade value. P&L, realized profit and loss per basis point up-shift. Predicted P&L: the average of the delta at two points: at the associated shift size and for the unperturbed case. Gap: predictability gap, P&L − Predicted P&L. The results are displayed in Table 3.

## **References**

- [1] Piterbarg, V.V. (2004). TARNs: models, valuation, risk sensitivities, *Wilmott* **14**, 62–71.
- [2] Glasserman, P. & Staum, J. (2001). Conditioning on onestep survival for barrier option simulations, *Operations Research* **49**, 923–937.

RAOUL PIETERSZ
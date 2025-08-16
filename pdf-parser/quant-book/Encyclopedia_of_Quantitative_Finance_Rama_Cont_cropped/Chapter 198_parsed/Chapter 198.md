# **Intensity-based Credit Risk Models**

**Reduced-form credit risk models** have become standard tools for pricing credit derivatives and for providing a link between credit spreads and default probabilities. In structural models, following the Merton approach [1, 12], default is defined by a firm value hitting a certain barrier. In such an approach, the concept of credit spread is rather abstract since it is not modeled explicitly and therefore is not directly accessible and may also have dynamics that are not completely pleasing. Reduced-form models, however, concentrate on modeling the hazard rate or intensity of default, which is directly linked to the credit spread process. In contrast to a structural approach, the event of default in a reduced-form model comes about as a sudden unanticipated event (although the likelihood of this event may have been changing).

## **Deterministic Hazard Rates**

## *Risk-neutral Default Probability*

The basic idea around pricing default sensitive products is that of considering a risky zero-coupon bond of unit notional and maturity *T* . We write the payoff at maturity as

$$C(T,T) = \begin{cases} 1 & \text{default} \\ \delta & \text{no default} \end{cases} \tag{1}$$

where *δ* is an assumed recovery fraction paid immediately in the event of default. The price of a risky cash flow due at time *T* is then

$$C(t,T) = [S(t,T) + [1 - S(t,T)]\delta]B(t,T) \quad (2)$$

with *B(t, T )* denoting the risk-free discount factor for time *T* as seen from time *t*, *S(t, T )* is the risk-neutral survival (no default) probability (*see* **Hazard Rate**) in the interval [*t,T* ] or, equivalently, 1 − *S(t, T )* is the risk-neutral default probability. This style of approach was developed by Jarrow and Turnbull [8, 9].

## *Pricing a Credit Default Swap (CDS)*

A credit default swap (CDS) (*see* **Credit Default Swaps**) has become a benchmark product for trading credit risk and hence we base most of our analysis around CDS pricing. Standard assumptions used in pricing CDS include deterministic default probabilities, interest rates, and recovery values (or at least independence between these three quantities). In a CDS contract, the protection buyer will typically pay a fixed periodic premium, *X*CDS, to the protection seller until the maturity date or the default (credit event) time (*T* ). The present value of these premiums at time *t* can be written as

$$V_{\text{premium}}(t, T) = \sum_{i=1}^{m} S(t, t_i) B(t, t_i) \Delta_{i-1,i} X_{\text{CDS}} \quad (3)$$

where *m* is the number of premium payments and *<sup>i</sup>*−1*,i* represents the day count fraction.

The protection seller in a CDS contract will undertake in the event of a default to compensate the buyer for the loss of notional less some recovery value, *δ*. The value of the default component obtained by integrating over all possible default times is given by

$$V_{\text{default}}(t, T) = (1 - \delta) \int_{t}^{T} B(t, u) \, \mathrm{d}S(t, u) \qquad (4)$$

Note that due to the required negative slope of *S(t, u)*, this term will be negative; hence, the sum of equations (3) and (4) defines the value of a CDS from a protection provider's point of view.

## *Defining the Hazard Rate*

In pricing a CDS, the main issue is to define *S(t, u)* for all relevant times in the future, *t* ≤ *u* ≤ *T* . If we consider default to be a Poisson process driven by a constant intensity of default, then the survival probability is

$$S(t, u) = \exp[-h(u - t)] \tag{5}$$

where *h* is the intensity of default, often described as the hazard rate. We can interpret *h* as a forward instantaneous default probability; the probability of default in a small period d*t* conditional on no prior default is *h* d*t*. Default is a sudden unanticipated event (although it may, of course, have been partly anticipated due to a high value of *h*).

## *Link from Hazard Rate to Credit Spread*

If we assume that CDS premiums are paid continuously,a then the value of the premium payments can be written as

$$V_{\text{premium}}(t, T) \approx X_{\text{CDS}} \int_{t}^{T} B(t, u) S(t, u) \, \text{d}u \qquad (6)$$

Under the assumption of a constant hazard rate of default, we can write d*S(t, u)* = −*hS(t, u)* d*u* and the default payment leg becomes

$$V_{\text{default}}(t, T) = -(1 - \delta)h \int_{t}^{T} B(t, u)S(t, u) \, \mathrm{d}u \quad (7)$$

The CDS spread will be such that the total value of these components is zero. Hence from *V*premium*(t, T )* + *V*default*(t, T )* = 0 we have the simple relationship

$$h \approx \frac{X_{\text{CDS}}}{(1-\delta)}\tag{8}$$

The above close relationship between the hazard rate and CDS premium (credit spread) is important in that the underlying variable in our model is directly linked to credit spreads observed in the market. This is a key advantage over structural models whose underlying variables are rather abstract and hard to observe.

## *Simple Formulas*

Suppose we define the risk-free discount factors *via* a constant continuously compounded interest rate *B(t, u)* = exp[−*r(u* − *t)*]. We then have closed-form expressions for quantities such as

$$V_{\text{premium}}(t, T) / X_{\text{CDS}}$$
  

$$\approx \int_{t}^{T} \exp[-(r+h)(u-t)] du$$
  

$$= \frac{1 - \exp[-(r+h)(T-t)]}{r+h}$$
 (9)

The above expression and equation (8) allow a quick calculation for the value of a CDS, or equivalently a risky annuity or DV01 for a particular credit.

## *Incorporating Term Structure*

For a nonconstant intensity of default, the survival probability is given by

$$S(t, u) = \exp\left[-\int_{t}^{u} h(x) \, \mathrm{d}x\right] \tag{10}$$

To allow for a term structure of credit (e.g., CDS premia at different maturities) and indeed a term structure of interest rates, we must choose some functional form for *h*. Such an approach is the credit equivalent of yield curve stripping, although due to the illiquidity of credit spreads much less refined, and was first suggested by Li [10]. The single-name CDS market is mainly based around 5-year instruments and other maturities will be rather illiquid. A standard approach is to choose a piecewise constant representation of the hazard rate to coincide with the maturity dates of the individual CDS quotes.

## **Extensions**

## *Bonds and Basis Issues*

Within a reduced-form framework, bonds can be priced in a similar way to CDS:

$$V_{\text{bond}}(t, T) = \sum_{i=1}^{m} S(t, t_i) B(t, t_i) \Delta_{i-1, i} X_{\text{bond}}$$
$$+ S(t, T) B(t, T) - \delta \int_{t}^{T} B(t, u) \, \mathrm{d}S(t, u) \tag{11}$$

The first term above is similar to the default payment on a CDS but the assumption here is that the bond will be worth a fraction *δ* in default. The second and third terms represent the coupon and principal payments on the bond, respectively. It is therefore possible to price bonds *via* the CDS market (or *vice versa*) and indeed to calibrate a credit curve *via* bonds of different maturities from the same issuer. However, the treatment of bonds and CDS within the same modeling framework must be done with caution. Components such as funding, the CDS delivery option, delivery squeezes, and counterparty risk mean that CDS and bonds of the same issuer will trade with a basis representing nonequal riskneutral default probabilities. In the context of the formulas, the components creating such a basis would represent different recovery values as well as discount factors when pricing CDS and bonds of the same issuer.

## *Stochastic Default Intensity*

The deterministic reduced-form approach can be extended to accommodate stochastic hazard rates and leads to the following expression for survival probabilities:-

$$S(t, u) = E^{\mathcal{Q}} \left[ \exp \left[ - \int_{t}^{u} h(x) \, \mathrm{d}x \right] \right] \tag{12}$$

This has led to various specifications for modeling a hazard rate process with parallels with interest-rate models for modeling products sensitive to credit spread volatility with examples to be found in [4, 5, 11]. Jarrow *et al.* [7] (*see* **Jarrow–Lando–Turnbull Model**) have extended such an approach to have a Markovian structure to model credit migration or discrete changes in credit quality that would lead to jump in the credit spread. Furthermore, credit hybrid models with hazard rates correlated to other market variables, such as interest rates, have been introduced. For example, see [13].

## *Portfolio Approaches*

The first attempts at modeling portfolio credit products, such as basket default swaps and CDOs, involved multidimensional hazard rate models. However, it was soon realized that introducing the level of default correlation required to price such products realistically was far from trivial. This point is easily understood by considering that two perfectly correlated hazard rates will not produce perfectly correlated default events and more complex dynamics are required such as those considered by Duffie [3]. Most portfolio credit models have instead followed structural approaches (commonly referred to as *copula models* with the so-called Gaussian copula model becoming the market standard for pricing CDOs; *see* **Gaussian Copula Model**) for reasons of simplicity. Schonbucher and Schubert [14] have shown how to combine intensity and copula models. More recently, the search for more sophisticated portfolio credit risk modeling approaches is largely based around reduced-form models as in [2] and [6] (*see* **Multiname Reduced Form Models**).

## **Conclusions**

We have outlined the specification and usage of reduced-form models for modeling a default process and described the link between the underlying in such a model and market observed credit spreads. We have described the application of such models to vanilla credit derivative structures such as CDS and also more sophisticated structures such as credit spread options, credit hybrid instrument, and portfolio credit products.

## **End Notes**

a*.* CDS premiums are typically paid quarterly in arrears but an accrued premium is paid in the event of default to compensate the protection seller for the period for which a premium has been paid. Hence the continuous premium assumption is only a mild approximation.

## **References**

- [1] Black, F. & Cox, J. (1976). Valuing corporate securities: some effects of bond indenture provisions, *Journal of Finance* **31**, 351–367.
- [2] Chapovsky, D., Rennie, A. & Tavares, P. (2006). *Stochastic Intensity Modelling for Structured Credit Exotics*, working paper, Merrill Lynch.
- [3] Duffie, D. (1998). *First-to-Default Valuation*, Institut de Finance, University of Paris, Dauphine, and Graduate School of Business, Stanford University.
- [4] Duffie, D. (1999). Credit swap valuation, *Financial Analysts Journal* January/February, 73–87.
- [5] Duffie, D. & Singleton, K. (1999). Modeling term structures of defaultable bonds, *Review of Financial Studies* **12**(4), 687–720.
- [6] Inglis, S. & Lipton, A. (2007). Factor models for credit correlation, *Risk Magazine* **20**, 110–115.
- [7] Jarrow, R.A., Lando, D. & Turnbull, S.M. (1997). A Markov model for the term structure of credit spreads, *Review of Financial Studies* **10**, 481–523.
- [8] Jarrow, R.A. & Turnbull, S.M. (1992). Credit risk: drawing the analogy, *Risk Magazine* **5**(9), 63–70.
- [9] Jarrow, R.A. & Turnbull, S.M. (1995). Pricing derivatives with credit risk, *Journal of Finance* **50**, 53–85.

- [10] Li, D.X. (1998). *Constructing a Credit Curve, Credit Risk* , A RISK Special report (November 1998), pp. 40–44.
- [11] Longstaff, F. & Schwartz, E. (1995). Valuing risky debt: a new approach, *Journal of Finance* **50**, 789–820.
- [12] Merton, R.C. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [13] Schonbucher, P.A. (2002/3). Tree implementation of a credit spread model for credit derivatives, *Journal of Computational Finance* **6**(2), 1–38.
- [14] Schonbucher, P. & Schubert, D. (2001). *Copula Dependant Default Risk in Intensity Models*, working paper, Bonn University.

**Related Articles**

**Credit Default Swaps**; **Duffie–Singleton Model**; **Hazard Rate**; **Multiname Reduced Form Models**; **Nested Simulation**; **Reduced Form Credit Risk Models**.

JON GREGORY
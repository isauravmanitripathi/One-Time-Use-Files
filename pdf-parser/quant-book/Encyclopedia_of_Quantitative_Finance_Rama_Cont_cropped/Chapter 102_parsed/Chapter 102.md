## Margrabe Formula

An exchange option gives its owner the right, but not the obligation, to exchange  $b$  units of one asset for  $a$  units of another asset at a specific point in time, that is, it is a claim that pays off  $(aS_1(T)$  $bS_2(T)^+$  at time T.

Outperformance option or Margrabe option are alternative names for the same payoff.

Let us assume that the interest rate is constant  $(r)$  and that the underlying assets follow correlated ( $dW_1 dW_2 = \rho dt$ ) geometric Brownian motions under the risk-neutral measure.

$$dS_i = \mu_i S_i dt + \sigma_i S_i dW_i \quad \text{for } i = 1, 2 \quad (1)$$

Note that allowing  $\mu_i$ 's that are different from r enables us to use resulting valuation formula for the exchange option directly in cases with nontrivial carrying costs on the underlying. This could be for futures (where the drift rate is 0), currencies (where the drift rate is the difference between domestic and foreign interest rates, see Foreign Exchange **Options**), stocks with dividends (where the drift rate is  $r$  less the dividend yield), or nontraded quantities with convenience yields.

The value of the exchange option at time  $t$  is

$$\pi^{EO}(t) = EO(T - t, aS_1(t), bS_2(t)) \tag{2}$$

where the function EO is given by

$$EO(\tau, S_1, S_2) = S_1 e^{(\mu_1 - r)\tau} \mathcal{N}(d_+) - S_2 e^{(\mu_2 - r)\tau} \mathcal{N}(d_-)$$
(3)

with

$$d_{\pm} = \frac{\ln(S_1/S_2) + (\mu_1 - \mu_2 \pm \sigma^2/2)\tau}{\sigma\sqrt{\tau}} \qquad (4)$$

where  $\sigma = \sqrt{\sigma_1^2 + \sigma_2^2 - 2\sigma_1\sigma_2\rho}$ ,  $\mathcal{N}$  denotes the standard normal distribution function and  $\tau = T - t$ . The formula was derived independently by Margrabe [12] and Fisher [6], but despite the two papers being published side by side in the Journal of Finance, the formula commonly bears only the former author's name. The result is most easily proven by using a change of numeraire (see Change of Numeraire), writing

$$\pi^{\text{EO}}(t) = S_2(t) \mathbf{E}_t^{\mathcal{Q}^{S_2}} ((aS_1(T)/S_2(T) - b)^+) \quad (5)$$

noting that  $S_1/S_2$  follows a geometric Brownian motion, and reusing the Black-Scholes calculation for the mean of a truncated lognormal variable.

If the underlying asset prices are multiplied by a positive factor, then the exchange option's value changes by that same factor. This means that we can use Euler's homogeneous function theorem to read off the partial derivatives of the option value with respect to the underlying assets (the deltas) directly from the Margrabe formula (see [15] for more such tricks), specifically

$$\frac{\text{dEO}}{\text{d}S_1} = \text{e}^{(\mu_1 - r)\tau} \mathcal{N}(\text{d}_+)$$
(6)

and similarly for  $S_2$ . If the S assets are traded, then a portfolio with these holdings (scaled by  $a$  and  $b$ ) that is made self-financing with the risk-free asset replicates the exchange option, and the Margrabe formula gives *the only* no-arbitrage price.

If the underlying assets do not pay dividends during the life of the exchange option (so that the risk-neutral drift rates are  $\mu_1 = \mu_2 = r$ ), then early exercise is never optimal, and the Margrabe formula holds for American options too. With nontrivial carrying costs, this is not true, but as noted by [2], a change of numeraire reduces the dimensionality of the problem so that standard one-dimensional methods for American option pricing can be used.

The Margrabe formula is still valid with stochastic interest rates, provided the factors that drive interest rates are independent of those driving the S assets.

Exchange options are most common in overthe-counter foreign exchange markets, but exchange features are embedded in many other financial contexts; mergers and acquisitions (see [12]) and indexed executive stock options (see  $[9]$ ) to give just two examples.

## Variations and Extensions

Some variations of exchange options can be valued in closed form. In [10], a formula for a so-called traffic light option that pays

$$(S_1(T) - K_1)^+(S_2(T) - K_2)^+ \tag{7}$$

is derived, and [4] gives a formula for the value of a compound exchange option, that is, a contract that pays

$$(\pi^{\text{EO}}(T_C) - S_2(T_C))^+ \text{ at time } T_C < T \qquad (8)$$

Both formulas involve the bivariate normal distribution function, and in the case of the compound exchange option a nonlinear but well-behaved equation that must be solved numerically.

For knock-in and knockout exchange options whose barriers are expressed in terms of the ratio of the two underlying assets, [7] show that the reflection-principle-based closed-form solutions (see [14]) from the Black-Scholes model carry over; this means that barrier option values can be expressed solely through the EO-function evaluated at appropriate points.

However, there are not always easy answers; in the simple case of a spread option

$$(S_1(T) - S_2(T) - K)^+ \tag{9}$$

there is no commonly accepted closed-form solution. The reason for this is that a sum of lognormal variables is not lognormal. More generally, many financial valuation problems can be cast as follows: calculate the expected value of

$$\left(\sum_{i=1}^{n} \alpha_{i,n} X_{i,n} - K\right)^{+} \tag{10}$$

where the  $X_{i,n}$ 's are lognormally distributed. One can use generic techniques such as direct integration, numerical solution of partial differential equations, or Monte Carlo simulation, but there is an extensive literature on other approximation methods. These include

- moment approximation, where the moments of  $\sum_{i=1}^{n} \alpha_{i,n} X_{i,n}$  are calculated, the variable then treated as lognormal, and the option priced by a Black-Scholes-like formula; an application to Asian options is given in  $[11]$ .
- integration by Fourier transform techniques, which extends beyond lognormal models and works well if *n* is not too large (say  $2-4$ ); an application to spread options is given in  $[1]$ .
- limiting results for  $n \to \infty$  as obtained in [5] and [13]; the relation to the reciprocal gamma

distribution has been used for Asian and basket options.

- changing to Gaussian processes as suggested in [3]; this may be suitable for commodity markets where spread contracts are popular, and it allows for the inclusion of mean reversion.
- if the  $a_{i,n}X_{i,n}$ 's depend monotonically on a common random variable, then Jamshidian's approach from  $[8]$  can be used to decompose an option on a portfolio into a portfolio of simpler options. This is used to value options on coupon-bearing bonds in one-factor interest-rate models.

## References

- Alexander, C. & Scourse, A. (2004). Bivariate normal [1] mixture spread option valuation, Quantitative Finance 4, 637-648.
- Bjerksund, P. & Stensland, G. (1993). American [2] exchange options and a put-call transformation: a note, Journal of Business, Finance and Accounting 20, 761-764.
- Carmona, R. & Durrleman, V. (2003). Pricing and [3] hedging spread options, SIAM Review 45, 627-685.
- Carr, P. (1988). The valuation of sequential exchange [4] opportunities, Journal of Finance 43, 1235-1256.
- Dufresne, D. (2004). The log-normal approximation in [5] financial and other computations, Advances in Applied Probability 36, 747-773.
- Fischer, S. (1978). Call option pricing when the exercise [6] price is uncertain, and the valuation of index bonds, Journal of Finance, 33, 169-176.
- [7] Haug, E.G. & Haug, J. (2002). Knock-in/out Margrabe, Wilmott Magazine 1, 38-41.
- Jamshidian, F. (1989). An exact bond option formula, [8] Journal of Finance 44, 205-209.
- Johnson, S.A. & Tian, Y.S. (2001). Indexed execu-[9] tive stock options, Journal of Financial Economics 57, 35-64.
- [10] Jørgensen, P.L. (2007). Traffic light options, Journal of Banking and Finance 31, 3698-3719.
- [11] Levy, E. (1992). Pricing European average rate currency options, Journal of International Money and Finance  $11(5), 474-491.$
- [12] Margrabe, W. (1978). The value of an option to exchange one asset for another, Journal of Finance 33, 177-186.
- [13] Milevsky, M.A. & Posner, S.E. (1998). Asian options, the sum of lognormals, and the reciprocal gamma distribution, Journal of Financial and Quantitative Analysis 33, 409-422.

- [14] Poulsen, R. (2006). Barrier options and their static hedges: simple derivations and extensions, *Quantitative Finance* **6**, 327–335.
- [15] Reiss, O. & Wystup, U. (2001). Efficient computation of options price sensitivities using homogeneity and other tricks, *Journal of Derivatives* **9**, 41–53.

**Related Articles**

**Black–Scholes Formula**; **Change of Numeraire**; **Exchange Options**; **Foreign Exchange Options**.

ROLF POULSEN
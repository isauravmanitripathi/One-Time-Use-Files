# **Local Volatility Model**

The most important input for pricing equity derivatives comes from vanilla call and put options on an equity index or a single stock. The market convention for these options follows the classic Black-Scholes-Merton (BSM) model [3, 15]: the price of each option can be represented by a single number called the *implied volatility*, which is the unknown volatility parameter required in the BSM model to reproduce the price. The implied volatilities for different maturities and strikes are often significantly different, and they collectively form the implied volatility surface of the underlying. A fundamental modeling problem is to explain the implied volatility surface accurately using logical assumptions. Many interesting applications follow directly from the solution to this problem. The impact from different parts of the implied volatility surface on a product can be assessed, leading to a deeper understanding of the product, its risks, and the associated hedging strategy. Moreover, different derivatives products, including those not available from the market, may be priced and analyzed under assumptions consistent with the vanilla options.

This article discusses the local volatility surface approach for analyzing equity implied volatility surfaces and examines a common framework in which different modeling assumptions can be incorporated. Local volatility models were first developed by Dupire [11], Derman and Kani [9], and Rubinstein [19] in the last decade and have since become one of the most popular approaches in equity derivatives quantitative research [1, 2, 7, 8, 10, 13, 16, 18]. We present the model from a practitioner's perspective, discussing calibration techniques with extension to dividends and interest rate modeling, with emphasis on the ease of application to real-world problems.

#### **Basic Model**

The basic local volatility model is an extension of BSM to the case where the diffusion volatility becomes a deterministic function of time and the spot price. In the absence of dividends, the stock dynamics can be represented by the following stochastic differential equation:

$$\frac{\mathrm{d}S_t}{S_t} = g_t \,\mathrm{d}t + \sigma(t, S_t) \,\mathrm{d}W_t \tag{1}$$

where  $S_t$  is the stock price at time  $t, g_t = r_t - b_t$  is the known growth rate of the stock ( $r_t$  is the interest rate and  $b_t$  is the effective stock borrowing cost) at  $t, \sigma(t, S)$  is the local volatility function for given time  $t$  and stock price  $S$ , and  $W_t$  is a Brownian motion representing the uncertainty in the stock price. Dynamics (1) can also be viewed as the effective representation of a general stochastic volatility model where  $\sigma^2(t, S)$  is the expectation of the instantaneous diffusion coefficient conditioning on  $S_t = S$  [13, 17]. If we use  $C(t, S; T, K) = \mathbf{E}[\max(S_T - K, 0)]$  $S_t = S$  to represent the undiscounted price for a European call option with maturity  $T$  and strike  $K$ when the stock price at time  $t \leq T$  is S, then equation (1) leads to the well-known Dupire equation for  $C$ :

$$\frac{\partial C}{\partial T} = \frac{\sigma^2(T, K)K^2}{2} \frac{\partial^2 C}{\partial K^2} + g_T \left( C - K \frac{\partial C}{\partial K} \right) \tag{2}$$

Equation  $(2)$  gives the relationship between the call option price  $C$  and the local volatility function  $\sigma(t, S)$ . In theory, if arbitrary-free prices of  $C(T, K)$ were known for arbitrary T and  $K, \sigma(t, S)$  could be recovered by inverting equation  $(2)$  with differentials of  $C$ . In practice, the market option prices are only directly available on a few maturities and strikes. Schemes for interpolating and extrapolating implied volatilities are often adopted in practice to arrive at a smooth function  $C(T, K)$ . Such schemes, however, typically lack explicit controls on the various derivatives terms in equation (2), and the local volatility directly inverted from equation  $(2)$  can exhibit strange shapes and sometimes attain nonphysical values for reasonable implied volatility input.

Instead of assuming the implied volatilities perfectly known for all maturities and strikes and inverting equation (2), one can model the local volatility function  $\sigma(t, S)$  directly as a parametric function. Solving the forward partial differential equation (2) numerically with the initial conditions

$$C(t, S, T = t, K) = \max(S - K, 0) \tag{3}$$

yields call option prices for all maturity  $T$ s and strike  $K_{\rm s}$ , from which the implied volatility surface can be derived. The parameters of the local volatility function can then be determined by matching the implied volatility surface generated from the model to that from the market. With a careful design of the local volatility function, this so-called *calibration* process can be implemented very efficiently for practical use. This methodology has the advantage that the knowledge of a perfect implied volatility surface is not required and the model is arbitrage free by construction. In addition, a great amount of analytical flexibility is available, which allows tailor-made designs of different models for specific purposes.

## **Volatility Surface Design and Calibration**

The key to the success of a volatility model lies in an understanding of how the implied volatility surface is used in practice. Empirically, option traders often refer to the implied volatility surface and its shape deformation with intuitive descriptions such as *level, slope*, and *curvature*, effectively approximating the shape as simple quadratic functions. In addition, for strikes away from the at-the-money (ATM) region, sometimes the ability to modify the out-of-the-money (OTM) surface independent from the central shape is desired, which traders intuitively speak of as changing the *put wing* or the *call wing*. Thus there exist several degrees of freedom on the volatility surface that a good model should be able to accommodate, and we can design the local volatility function so that each mode is captured by a distinct parameter.

To facilitate comparison across different modeling techniques, we standardize the model specification in terms of the BSM implied volatilities on a small number of strikes per maturity, typically three or five. For example, volatilities on three strikes in the ATM region can be used to provide a precise definition of the traders' level, slope, and curvature parameters. Similarly, fixing volatilities at one downside strike and one upside strike in the OTM region allows the model to agree on a five-parameter specification of level, slope, curvature, put wing, and call wing. These calibration strikes on each maturity are chosen to cover the range of practical interest, usually one to two standard deviations of diffusion at the stock's typical volatility. In the absence of fine structures such as sharp jumps in the underlying, we expect that one standard deviation in the strike range provides a natural length scale over which the stock price distribution varies smoothly. Thus the implied volatility should have a very smooth shape over the range thus defined, and matching the implied volatilities at the calibration strikes should produce a very good match for all the implied volatilities between them.

The preceding discussions give a straightforward strategy for building the local volatility model—we specify a small number of strikes, and tune the local volatility function with the same number of parameters as the number of strikes for each maturity in a bootstrapping process. The local volatility parameters are then solved through a root-finding routine so that the implied volatilities at the specified strikes on each maturity are reproduced. As each local volatility parameter is designed to capture a distinct aspect of the surface shape, the root-finding system is well behaved and converges quickly to the solution in practice. More importantly, such a process allows a much smaller numerical noise compared to a typical optimization process, giving rise to much more stable calibration results. This is essential in ensuring robust Greeks and scenario outputs from the model.

## **Discrete Dividend Models**

Dividend modeling is an important problem in equity derivatives. It can be shown [15] that with nonzero dividends, the original BSM model only works when the payment amount is proportional to the stock price immediately before the ex-dividend date (exdate), through incorporating the dividend yields in *gt* of equation (1). However, many market participants tend to view future dividends as absolute cash amounts, and this is especially true after trading in index dividend swaps becomes liquid. Existing literature [4, 5, 12, 14] suggests even in the case of a constant volatility, cash dividend equity models (also known as *discrete dividend models*) are much less tractable than proportional dividend ones. Recently, Overhaus *et al.* [16] proposed a theory to ship future cash dividends from the stock price to arrive at a *pure* stock process, on which one can apply the Dupire equation. This theory calls for the changes in future dividends to have a global impact, especially for maturities *before* their ex-dates, a feature that certain traders find somewhat counterintuitive.

Nontrivial dividend specifications can be naturally introduced in the framework here. We note that between ex-dates, equations (1) and (2) continue to hold without modification. Across an ex-date  $T_i$ , a simple model for the stock price is

$$S_{T_i^+} = (1 - Y_i) S_{T_i^-} - D_i \tag{4}$$

where  $Y_i$  and  $D_i$  are respectively the dividend yield and cash dividend amount for the ex-date  $T_i$ . This is the mixed-dividend model, which includes proportional and cash dividend models as special cases.  $Y_i$ and  $D_i$  can be determined from a *nominal* dividend schedule specifying the ex-dates and the dividend payment amount, as well as a mixing schedule specifying the portion of dividends that should remain as cash, the rest being converted into proportional yield. Typically, cash dividends can be specified for the first few years to reflect the certainty on expected dividends, gradually switching to all proportional in the long term. Theoretically, equation (4) has the disadvantage of allowing negative exdividend stock prices. In practice, if the mixing ratio is switched to all proportional after a few years, this does not pose a serious problem. According to dividend model (4), the forward equation across the ex-date becomes

$$C(T_i^+, K) = (1 - Y_i) C\left(T_i^-, \frac{K + D_i}{1 - Y_i}\right) \tag{5}$$

and can be implemented in the same way as standard jump conditions. With equation  $(5)$  incorporated, the calibration strategy in the section Volatility Surface Design and Calibration can be applied in exactly the same way. We note that it is straightforward to extend the local volatility model here to handle more interesting dividend models, in which the dividend amount can be made a function of the spot immediately before the ex-date. As long as such a function becomes small enough when the stock price goes to zero, the issue of negative ex-dividend stock prices can be theoretically eliminated.

#### **Stochastic Interest Rate Models**

Local volatility models can be extended to cases where stochastic interest rate needs to be considered [16]. The interest rate can be modeled through classic short-rate models, and the equity process is then specified as a diffusion with stochastic growth rate. Following Brigo and Mercurio [6], we have

$$\frac{\mathrm{d}S_t}{S_t} = (r_t - b_t) \,\mathrm{d}t + \sigma(t, S_t) \,\mathrm{d}W_t \quad (6a)$$

$$r_t = u_t + y_t \tag{6b}$$

$$dy_t = \alpha(\phi - y_t) dt + \sigma_t y_t^{\beta} dB_t \qquad (6c)$$

$$\mathrm{d}W_t \,\mathrm{d}B_t = \rho \,\mathrm{d}t \tag{6d}$$

where  $u_t$  is a function of time describing the deterministic part of the interest rate,  $y_t$  is a diffusion process modeling the stochastic part of the interest rate, and  $B_t$  is a Brownian motion describing the interest rate uncertainty, correlated with  $W_t$  with coefficient  $\rho$ . In equation (6c),  $\alpha$ ,  $\beta$ ,  $\phi$ , and  $\sigma_t$  are parameters describing the short-rate process. For example, when  $\phi = 0$  and  $\beta = 0$ , equation (6c) is equivalent to the Hull–White model. With nonzero  $\phi$  and  $\beta = \frac{1}{2}$ , the shifted Cox-Ingersoll-Ross (CIR++) model is obtained. Both models admit closed form pricing formula for zero-coupon bonds, interest rate caps, and swaptions, which can be used for calibration to interest rate derivatives market observables. For a given short-rate model and its parameters, the local volatility function  $\sigma(t, S)$  needs to be recovered from equity derivatives market information. This can be achieved by considering the transition density for the joint evolution of the stock price  $S_t$  and short rate  $r_t$  under stochastic discount factor, that is,

$$p(t, S, y; T, K, Y)$$
  
=  $\mathbf{E} \bigg[ \exp \bigg( -\int_{t}^{T} r_{\tau} \, d\tau \bigg) \times \delta(S_{T} - K) \delta(y_{T} - Y) \bigg| S_{t} = S, y_{t} = y \bigg]$ (7)

The Fokker–Planck equation for such a quantity can be written down as

$$\begin{split} \frac{\partial p}{\partial T} &= \frac{\partial^2 (K^2 \sigma^2 (T, K) p)}{2 \partial K^2} + \frac{\sigma_T^2}{2} \frac{\partial^2 (Y^{2\beta} p)}{2 \partial Y^2} \\ &+ \rho \sigma_T \frac{\partial^2 (K \sigma (T, K) Y^{\beta} p)}{\partial K \partial Y} \\ &- (u_T + Y - b_T) \frac{\partial (K p)}{\partial K} \\ &- \alpha \phi \frac{\partial p}{\partial Y} + \alpha \frac{\partial (Y p)}{\partial Y} - (u_T + Y) p \end{split} \tag{8}$$

By solving equation (8) subject to vanishing boundary conditions on  $K$  and  $Y$  as well as delta-function initial condition at  $T = t$ , one can recover the European option prices as

$$C(t, S_t; T, K) = \int_0^\infty \mathrm{d}S \max(S - K, 0)$$
$$\times \int_{-\infty}^\infty p(t, S_t, y_0; T, S, Y) \, \mathrm{d}Y \quad (9)$$

and hence derive the implied volatility surface from the hybrid model (6). The strategy discussed in the section Volatility Surface Design and Calibration can once again be invoked. In practice, since the two-factor model takes significantly more time in calculation than the basic model, it is very effective to use the basic model solution as a starting point for the hybrid calibration.

![](_page_3_Figure_4.jpeg)

Figure 1 The implied and local volatility surface on the S&P 500 Index in November 2007. (a) The implied volatility as a function of time to maturity and strike price (expressed as a percentage of spot price). (b) The local volatility surface calibrated under the basic model. (c) Changes in the local volatility surface when cash dividends are assumed for the first five years, gradually transitioning to proportional dividends in 10 years. (d) Changes in the local volatility surface where the interest rate is assumed to follow the Hull-White model calibrated to ATM caps with correlation  $\rho = 30\%$ . In both (c) and (d) the new local volatility is smaller than in (b)

## **Examples**

We use data from the S&P 500 index market as examples to illustrate the preceding discussions. Figure 1(a) and (b) shows a typical implied volatility surface and the calibrated local volatility surface under the basic model, that is, with proportional dividend and deterministic interest rate assumptions. The implied volatility surface is given by option traders. Normally it is retrieved from data in both the listed and OTC options market, interpolated, and extrapolated with trader-specified functions. The local volatility surface is built by simply calibrating to five strikes on each marked maturity, with the Libor-Swap curve and the full index dividend schedule. Excellent calibration quality can be obtained: the option price differences computed using the input implied volatility surface and the calibrated local volatility surface are less than one basis point of the spot price for most liquid strikes and below 10 basis points across all strikes and maturities. This accuracy is sufficient for most practical purposes.

Figure 1(c) and (d) displays the changes in the local volatility surface when we include effects of cash dividends or stochastic interest rate into the model. We have assumed the Hull–White model for the interest rate in these calculations. The dividend and interest rate specifications are seen to have a significant impact on the local volatility surface and hence can be important in derivatives pricing. Cash

![](_page_4_Figure_5.jpeg)

**Figure 2** Impact of discrete dividends and stochastic interest rate on derivative pricing. (a) Changes to the fair strike of the variance swaps with different dividend assumptions. (b) Changes to the fair strike of the variance swaps under stochastic interest rate with different correlation. The labels indicate the maturity of the variance swaps. (c) Changes to the *PV* of the lookback options with different dividend assumption. (d) Changes to the *PV* of the lookback options under stochastic interest rate with different correlation. The numbers in (c) and (d) are in units of vega of Table 2

dividends introduce additional deterministic, nonproportional jump structures in the equity dynamics, and to maintain the same implied volatility surface the local volatility needs to become smaller. This effect depends on the dividend size relative to future spot prices, and thus become more pronounced for smaller strikes and longer maturities, producing a skewed shape in the difference. On the other hand, stochastic interest rate introduces volatility in discount bond prices and with positive correlation also reduces the equity local volatility. This effect does not depend on spot levels explicitly and is instead related to the volatility ratio between the interest rate and the equity and their correlation. Since the interest rate usually has a small volatility compared to the equity, to the leading order the effect of stochastic rates can sometimes be approximated by a parallel shift on the local volatility surface.

We can apply these local volatility models to price exotic derivatives not directly available from the vanilla market. One example is variance swaps, which are popular OTC products offered to capitalize on the discrepancy between implied and realized volatility. Another example is lookback options, which provide payoffs on the maximum/minimum index prices over a set of observation dates and can be appealing hedges to insurance companies who have sold policies with similar exposure. Tables 1 and 2 display the pricing results for these structures using the basic model.

Figure 2 shows the pricing impact on these structures when the effects of cash dividends and stochastic interest rates are considered. As the payout for the variance swap is directly linked to the equity's average local volatility, the pricing is strongly affected by the assumption of cash dividends and stochastic

<table>

 **Table 1** Pricing of variance swaps with the basic model

| Maturity (years) | Fair strike (%) |  |
|------------------|-----------------|--|
|                  |                 |  |
|                  | 27.59           |  |
| 2                | 28.18           |  |
| 3                | 28.42           |  |
|                  | 29.14           |  |
| 5                | 30.00           |  |
|                  |                 |  |

The payoff for strike K at maturity is  $\frac{252}{N} \sum_{i=0}^{N-1} (\ln \frac{S_{i+1}}{S_i})^2$  $K^2$ , where  $S_i$  is the index closing price on the *i*th business day from the current date  $(i = N \text{ corresponds to the maturity})$ . The fair strike is the value  $K$  such that the contract costs nothing to enter

**Table 2** Pricing of five-year lookback options with the basic model

| Option type                                                                                | Payout formula PV (%) Vega (%) |      |
|--------------------------------------------------------------------------------------------|--------------------------------|------|
| Call on maximum $\max_{i=0}^{5} \left(\frac{S_i}{S_0}\right) - \frac{S_5}{S_0}$ 25.29 1.17 |                                |      |
| Put on minimum $1 - \min_{i=0}^{5} \left(\frac{S_i}{S_0}\right)$ 22.35                     |                                | 0.85 |

 $S_i(i = 0, 1, \ldots, 5)$  is the index price at annual observation dates on year  $i$  from the current date. The PV is the calculated present value according to the payout formula at maturity. The Vega is the change in PV when a parallel shift of  $1\%$  is applied to the implied volatility surface

interest rate. For lookback options, one needs to look at the joint distribution among equity prices across different observation dates. Cash dividends generally reduce the local volatility and hence decrease the correlation between the equity prices at different dates, leading to lower lookback prices. With stochastic interest rate, the effect of modified equity diffusion volatility can either reinforce (e.g., call on maximum) or partly cancel (e.g., put on minimum) the effect of stochastic discounting.

The numerical impact of different modeling assumptions can be comparable to a full percentage difference in volatility. Hence, it may be important to take these into account when accurate and competitive pricing of exotic equity derivatives is required. An extensive and detailed discussion of the impact of stochastic interest rate on popular hybrid products can be found in  $[16]$ .

### References

- Andersen, L. & Brotherton-Ratcliffe, R. (1997). The [1] equity option volatility smile: an implicit finitedifference approach, Journal of Computational Finance 1.  $5-38$ .
- [2] Berestycki, H., Busca, J. & Florent, I. (2002). Asymptotics and calibrations of local volatility models, Quantitative Finance 2, 61-69.
- Black, F. & Scholes, M. (1973). The pricing of options [3] and corporate liabilities, Journal of Political Economy 81, 631-659.
- [4] Bos, M. & Vandermark, S. (2002). Finessing fixed dividends, Risk Magazine 15(9), 157-158.
- [5] Bos, R., Gairat, A. & Shepeleva, S. (2003). Dealing with discrete dividends, Risk Magazine 16(1), 109-112.
- [6] Brigo, D. & Mercurio, F. (2006). Interest Rate Models-Theory and Practice with Smile, Inflation and Credit, 2nd Edition, Springer Finance.

- [7] Brown, G. & Randall, C. (1999). If the skew fits, *Risk Magazine* **12**(4), 62–65.
- [8] Coleman, T.F., Li, Y. & Verma, A. (1999). Reconstructing the unknown volatility function, *Journal of Computational Finance* **2**, 77–102.
- [9] Derman, E. & Kani, I. (1994). Riding on a smile, *Risk Magazine* **7**(2), 32–39.
- [10] Dumas, B., Fleming, J. & Whaley, R.E. (1998). Implied volatility functions: empirical tests, *Journal of Finance* **53**, 2059–2106.
- [11] Dupire, B. (1994). Pricing with a smile, *Risk Magazine* **7**(1), 18–20.
- [12] Frishling, F. (2002). A discrete question, *Risk Magazine* **15**(1), 115–116.
- [13] Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*, Wiley, Hoboken, New Jersy.
- [14] Haug, E., Haug, J. & Lewis, A. (2003). Back to basics: a new approach to the discrete dividend problem, *Wilmott Magazine* **5**, 37–47.
- [15] Merton, R.C. (1973). Theory of rational option pricing, *The Bell Journal of Economics and Management Science* **4**, 141–183.

- [16] Overhaus, M., Bermudez, A., Buehler, H., Ferraris, A., ´ Jordinson, C. & Lamnouar, A. (2007). *Equity Hybrid Derivatives*, Wiley, Hoboken, New Jersy.
- [17] Piterbarg, V. (2007). Markovian projection method for volatility calibration, *Risk Magazine* **20**(4), 84–89.
- [18] Rebonato, R. (2004). *Volatility and Correlation*, 2nd Edition, Wiley, Chichester, West Sussex.
- [19] Rubinstein, M. (1994). Implied binomial trees, *Journal of Finance* **69**, 771–818.

## **Related Articles**

**Corridor Variance Swap**; **Dividend Modeling**; **Dupire Equation**; **Lookback Options**; **Model Calibration**; **Optimization Methods**; **Stochastic Volatility Interest Rate Models**; **Tikhonov Regularization**; **Variance Swap**; **Yield Curve Construction**.

CHIYAN LUO & XINMING LIU
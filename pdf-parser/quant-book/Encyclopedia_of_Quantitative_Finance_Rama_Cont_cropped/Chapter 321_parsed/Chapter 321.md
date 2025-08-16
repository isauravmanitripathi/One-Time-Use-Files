# **Commodity Forward Curve Modeling**

## **Commodity Futures and Forward Prices**

For several centuries, commodity forward markets have been the main place of commodity trading, as they allow producers and consumers to manage commodity price risk without going into actual delivery of a commodity. Forward contracts are traded over-the-counter between two parties and the grade of commodity, delivery point, exact amount, and exact delivery date are specified at the time of writing the contract. In this respect, they are different from *futures contracts*, which are standardized in terms of the grade, amount, delivery date, and location. Commodities are traded on exchanges such as the London Metal Exchange (LME), Chicago Board of Trade (CBOT), Chicago Mercantile Exchange (CME), InterContinental Exchange (ICE), and New York Mercantile Exchange (NYMEX). These futures markets provide the most reliable and liquid commodity futures prices. For example, most of the trading activity in oil markets takes place in futures and forward contracts, where the volume of trades is almost 10 times higher than in the spot market.

Throughout the article, we denote the commodity futures or forward price on day *t* for maturity date *T* by *F (t, T )* and the spot price (i.e., the price for the immediate delivery) on day *t* by *S(t)*. The forward curve prevailing on day *t* is the collection of futures prices {*F (t, T )*}*<sup>T</sup>* for all traded maturities *T* = 1*,* 2*,...,N*. It has been known for some time that, in absence of credit risk, forward and futures prices are equal under nonstochastic interest rates [5]. In commodity markets, interest rate risk plays a secondary role compared to the commodity spot price risk, so we use the terms "futures price" and "forward price" interchangeably.

Forward curves are of paramount importance in commodity markets, for several reasons. They provide information about the views of market participants, anticipated price trends, and expectations about future supply and demand. Futures prices observed in liquid futures markets provide price discovery and are essential for daily marking to market existing portfolio positions as well as for risk management activities such as Value-at-Risk calculations. Forward commodity prices influence storage, production, and other strategic decisions in related industries. Finally, futures contracts provide the way of calibrating derivatives pricing models under the risk-neutral probability measure.

The spot price of a commodity is often considered as the most important factor driving the whole forward curve [6, 13]. The influence of the spot price becomes greater as the futures contract approaches maturity, culminating in the following convergence property: on maturity date, the futures price must coincide with the spot price

$$F(T,T) = S(T) \tag{1}$$

This property follows from the absence of arbitrage and the possible occurrence of physical delivery of a commodity at the maturity of the futures contract. However, there are markets where the spot price is rather opaque or unreliable (or completely nonexistent, as it is the case, for instance, in electricity markets). In such cases, the convergence property does not necessarily hold or does not take place smoothly as the maturity approaches. These considerations, among others, may question the suitability of the spot price as the main driving factor of the forward curve.

Crude oil (and some metals) forward curves have traditionally been in one of the two states: backwardation, when the futures prices for short maturities are more expensive than those maturing later, or contango, which is the opposite situation. Figure 1 shows the NYMEX crude oil forward curve on February 21, 2008, when the market was in backwardation, and Figure 2 shows a contango forward curve observed on February 28, 2007.

Whether the market is in backwardation or in contango depends on the current price as well as inventory levels, transportation and storage costs, supply of storage, supply and demand equilibria, strategic and political issues, and many other factors. The shape of the commodity forward curve is closely related to the notion of the so-called *convenience yield*, that is, the benefit of holding a physical commodity over a futures contract. Backwardated forward curves arise when the benefit of holding a physical commodity (i.e., the convenience yield) is high and the interest rates and storage costs (representing together the "cost of carry") are relatively low. This happens, for instance, when there is a general perception of

![](_page_1_Figure_1.jpeg)

**Figure 1** NYMEX crude oil forward curve, February 21, 2008

![](_page_1_Figure_3.jpeg)

**Figure 2** NYMEX crude oil forward curve, February 28, 2007

low availability of a commodity and instability of its supply. More generally, the shape of the forward curve summarizes perceptions of market participants about the current state and future developments of the global commodity market.

For seasonal commodities, such as natural gas, electricity, or agricultural commodities, futures prices are largely governed by seasonal demand (as it is the case for energy) or supply (for agricultural commodities). For those commodities, transportation or storage capabilities are limited, so the excess demand or supply shortage cannot be absorbed by transporting a commodity from a different part of the world with excess supply, or storing at times of plentiful supply and using it whenever necessary.

![](_page_1_Figure_7.jpeg)

**Figure 3** UK Natural Gas forward curve, March 7, 2007

This results in a high seasonal premium on futures contracts maturing during periods of high demand (such as winter, in the case of natural gas) or low supply (such as before harvest, for agricultural commodities). This is illustrated in Figure 3, where a forward curve for natural gas in the United Kingdom is shown. Futures maturing in the winter (the time of high demand for gas in the United Kingdom) are clearly at a premium compared to those maturing in summer.

The dynamic modeling of the forward curve (i.e., the description of its random movements over time) and the understanding of the main fundamental factors behind its evolution has been a subject of extensive research, both by practitioners and academics. A proper model of the dynamics of the forward curve is an essential input in most derivative pricing models, scenario simulation, and risk management applications. A successful forward curve model should be able to match current observed forward curves, generate realistic forward curves containing empirically observed features, and should ideally be able to extrapolate the forward curve beyond the longest observed maturity. Moreover, it should be easily and quickly calibrated to the market data. However, just as in case of the Treasuries yield curves, commodity forward curve modeling is a challenging task, owing to the inherent multidimensionality of the problem and a nontrivial dependence structure across maturities. In contrast to interest rates, features such as seasonality may further complicate the modeling process.

# **Forward Curve Models**

Forward curve modeling approaches for commodities can be loosely classified into three main categories. The first one is a martingale-based approach, which models the dynamics of futures prices directly under the risk-adjusted probability measure  $Q$ , making use of the fact that futures prices are martingales under such a measure. One or possibly several risk factors driving the risk-neutral dynamics of the entire forward curve are usually assumed (resulting in the so-called *one-factor* or *multifactor models*).

Multifactor models such as those described in [4] are similar to the celebrated Heath–Jarrow–Morton (HJM) approach for modeling the yield curve [7], in that they directly model futures prices under the risk-neutral probability measure.<sup>a</sup> So the following representation is often considered:

$$\frac{\mathrm{d}F(t,T)}{F(t,T)} = \sum_{i=1}^{n} \sigma_i(t,T) \,\mathrm{d}W_i(t) \tag{2}$$

where *n* is the number of risk factors,  $W_i(t)$ ,  $i =$  $1, \ldots, n$  are Brownian motions (possibly correlated) representing sources of uncertainty and  $\sigma_i(t, T)$  are volatilities associated with the risk factors (possibly varying deterministically in time and maturity). The statistical technique of *principal component analysis* is often used to derive the risk factors, in which case they are assumed to be uncorrelated. Such an approach focuses on the martingale property of  $(F(t,T))_{t\leq T}$  under Q, which is useful for derivatives pricing. However, it is less suited for trading strategies involving spot and forward positions (the most common ones in a trading environment), as it says nothing about the actual evolution of the forward curves and hence cannot be calibrated to historical futures market data. The risk factors can be rather arbitrary and do not always have a clear meaning.<sup>b</sup> Alternatively, more interpretable fundamental stochastic factors can be taken. For example, a popular choice is to take the short-term and longterm price components (e.g., [10, 14]), which together determine the commodity's spot price:

$$S(t) = s(t) + X(t) + L(t)$$
(3)

where  $X(t)$  and  $L(t)$  are respectively the short- and long-term price components and  $s(t)$  is a possible (deterministic) seasonal component of the spot price. Then the futures prices are obtained using the relationship

$$F(t,T) = E_{\mathcal{Q}}(S(T)|\mathcal{F}_t) \tag{4}$$

where  $Q$  is the risk-adjusted probability measure and  $\mathcal{F}_t$  is the information available up to date t. To evaluate the expression (4), the dynamics of the fundamental factors (such as  $X(t)$  and  $L(t)$ ) under the risk-adjusted probability measure  $Q$  should be specified. Usually, such dynamics include the market prices of risk (the spot price risk and convenience yield risk), which make these models rather hard to calibrate, as market prices of risk are not observable. Another problem with such models is that the forward curves derived from equation (4) usually do not match observed forward curves.

Another approach to the commodity forward curve modeling is a static arbitrage-based one, making use of the cash-and-carry arguments and describing the no-arbitrage relationship between the spot and futures prices. This approach is based on the no-arbitrage assumption and implies that the futures price of a commodity must be equal to the cost of acquiring the physical commodity and carrying it until the maturity of the futures . Physical commodities, unlike financial assets, cannot be stored costlessly; so for them, the cost of carry is largely determined by the accumulated storage costs (and the interest lost on the investment into a commodity). However, these arguments would imply that commodity forward curves should always be in contango, that is, futures prices for longer maturities should always be higher than those for shorter maturities and the spot price. In practice, this is rarely the case; for example, historically, the crude oil futures market has been in backwardation approximately 75% of the time. To cope with this observation, the notion of *convenience yield* was introduced by Kaldor [8] and Working [15]. It is defined as the premium received by the owner of the physical commodity and not accruing to the holder of a futures contract written on it. This concept leads to the famous cost-of-carry relationship:

$$F(t,T) = S(t)e^{[r(t)+c(t)-\tilde{y}(t)](T-t)}$$
(5)

where  $r(t)$  is the riskless interest rate on the date t,  $c(t)$  is the storage cost (per unit of time and per dollar worth of commodity), and  $\tilde{y}(t)$  the convenience yield, all continuously compounded. Often, the convenience yield is defined net of storage costs:  $y(t) = \tilde{y}(t)$  -

 $c(t)$ , in which case the cost-of-carry relationship becomes

$$F(t,T) = S(t)e^{[r(t)-y(t)](T-t)}$$
(6)

In its early versions, the cost-of-carry relationship (6) included a constant or deterministic (but timevarying) convenience yield, such as in [3]. The next step was to define the convenience yield as a function of the spot price. More realistic versions of equation  $(6)$  (e.g., those in  $[6, 9]$ ) included the convenience yield as a stochastic process. Some authors stressed a time-spread optionality embedded in the convenience yield (discussed in, e.g., [12]). To emphasize this option-like feature of the convenience yield, it should be considered as a function of maturity  $T$  (or time to maturity  $T - t$ ), as well as time t:  $y = y(t, T)$ , as suggested in [2]. This representation is particularly useful in the case of seasonal commodities.

Obtaining a dynamic model for the forward prices from the cost-of-carry relationship (6) goes as follows. The spot price  $S(t)$  and the convenience yield  $y(t)$  are considered as the main fundamental stochastic factors driving the forward curve's evolution. A stochastic model is assumed for the joint dynamics of  $S(t)$  and  $y(t)$  (e.g., correlated geometric Brownian motions or mean-reverting diffusions) and then the corresponding dynamics for the futures prices is obtained by substituting the expressions for  $S(t)$  and  $y(t)$  into the cost-of-carry relationship (6). Sometimes, the interest rate can be added as another fundamental factor, as in [11]. The cost-of-carry relationship (6) holds under any probability measure, so for the purposes of derivatives pricing, the riskneutral dynamics of futures prices can be obtained from the risk-neutral dynamics of the fundamental factors.

#### The Seasonal Forward Curve Models

Seasonal forward curves are often observed in energy and agricultural markets. One attempt to model these has been made by Sorensen [14] and Lucia and Schwartz [10] who consider a deterministic seasonal component of the spot price, which subsequently enters the expression for the forward prices. However, seasonality in forward prices obtained in this way does not match the empirically observed seasonal patterns present in a forward curve, especially the observation that the forward price's seasonality is a function of the contract *maturity*  $T$  and not so much of the current date  $t$ .

Forward prices of seasonal energy commodities such as natural gas and electricity are influenced by seasonal demand due to heating or air-conditioning; agricultural commodities are influenced by seasonal supply (harvest). These constraints result in positive seasonal premia attached to futures maturing in calendar months of high demand or low supply. The seasonal cost-of-carry model by Borovkova and Geman [2] incorporates such a seasonal premium within the framework of statistical arbitrage-like relationship.

Assume that the forward curve contains liquid maturities up to one year  $(12 \text{ months})$  or an integer number of years. The first fundamental factor of the seasonal cost-of-carry model is defined as the geometric average of the observed forward prices at  $date\ t$ :

$$\bar{F}(t) = \sqrt[N]{\prod_{T=1}^{N} F(t,T)} \tag{7}$$

where  $N$  is the most distant maturity. The average level of the forward curve  $\bar{F}(t)$  is a robust quantity and a good indicator of the overall state of the forward market (more so than the volatile spot price). Note that, if  $N = 12 \times k$   $(k = 1, 2, \ldots)$ , then  $F(t)$ is a nonseasonal quantity, unlike a possibly seasonal spot price. Furthermore, the commodity spot price can be unreliable or even unavailable, so it is often not a good candidate to be the main fundamental factor driving the forward curve.

The seasonal premia  $s(M)$ ,  $(M = 1, \ldots, 12)$ , less associated with calendar months, are defined as the average premia, expressed in per cent, in futures expiring in the calendar month  $M$  with respect to the *day-t* average forward price  $\overline{F}(t)$ . It is assumed to be deterministic and  $\sum_{M=1}^{12} s(M) = 0$ .

The seasonal cost-of-carry model describes the relationship between the prevailing forward price  $\overline{F}(t)$  and the futures price  $F(t, T)$ :

$$F(t,T) = \bar{F}(t)e^{[s(T)-\gamma(t,T-t)(T-t)]} \tag{8}$$

where the quantity  $\gamma(t, T - t)$ , defined by the relationship above, is called the *stochastic premium* at date  $t$  (as opposed to the deterministic seasonal premium  $s(T)$ ), associated with the time to maturity  $T-t$ . Denoting  $\tau = T-t$ , the stochastic premium becomes  $\gamma(t,\tau) = \gamma(t,T-t)$ , which emphasizes that *γ* is associated with the time to maturity *τ* rather than the maturity date *T* .

Therefore, futures maturing in a particular calendar month can be either at a premium or a discount relative to the average level of the forward curve. This is a periodic, that is, seasonal effect, which is associated with periods of high demand or low supply. The seasonal premium is the nonstochastic quantity *s(M)*, which can be consistently estimated from the historical data. The quantity *γ (t, τ )*, on the other hand, is a stochastic process in *t*, indexed by the time to maturity *τ* , and summarizes all deviations of the actual observed futures prices from the anticipated futures prices given by *F (t)* ¯ e*s(T )*. It is called the *stochastic cost of carry*, or *stochastic premium devoid of seasonal premium*, for time to maturity *τ* . Factors influencing the function *γ* are, for example, levels of stocks, political news and events, or unusual weather conditions.

The seasonal cost-of-carry model (8) is related to the traditional cost-of-carry models such as the one in [3], but with the traditional convenience yield replaced by the stochastic premium *γ (t, τ )*. This stochastic premium can be seen as the "relative convenience yield" (with respect to its average across all maturities), net of the scaled seasonal premium:

$$y(t,T) - \frac{1}{N} \sum_{M=1}^{N} y(t,M) = \gamma(t,\tau) - \frac{s(T)}{\tau} \quad (9)$$

where *y(t, T )* is the traditional convenience yield.

The convergence property of the futures price to the spot price (1) provides the following expression for the spot price within the seasonal cost-of-carry model:

$$S(t) = \bar{F}(t)e^{s(t)}$$
 (10)

hence, if the spot price is not available in a particular market, the above relationship can be used to define a valuable proxy for the spot price.

The stochastic premium can be represented by a mean-reverting process, where the parameters of the process (such as the mean-reversion speed, level, and volatility) may differ per time to maturity *τ* . The entire term structure of *γ (t, τ )* can be driven by the same Brownian motion *W (t)*; more sources of uncertainty can be easily incorporated. The average forward price *F (t)* ¯ can be modeled by any appropriate diffusion or jump-diffusion process, uncorrelated to the term structure of {*γ (t, τ )*}*<sup>τ</sup>* .

The seasonal premium and other model parameters can be estimated from the set of historical futures prices by the ordinary least squares method or a Kalman filter methodology. Figure 4 shows the estimated seasonal premia for UK natural gas, electricity, and heating oil futures. Our estimates are based on historical data sets of ICE futures prices from 2001 to 2008.

As expected, futures expiring in winter are at a premium with respect to the average price level, and summer futures at a discount. December gas futures are on average at a 28% premium and December electricity futures are at 15% premium. The seasonal premium for heating oil is generally smaller, and is at most 3%, which reflects a wider availability of storage and transportation for heating oil.

For longer forward curves (such as the one depicted in Figure 3), a significant slope (defining an overall backwardation or contango state) can be

![](_page_4_Figure_14.jpeg)

**Figure 4** Natural gas, electricity, and heating oil seasonal premia. (a) Seasonal component, natural gas futures. (b) Seasonal forward premium, electricity futures. (c) Gasoil seasonal component

detected. In such cases, instead of defining the  $\bar{F}(t)$  as the day- $t$  level of the forward curve, we can approximate the overall shape of the log-forward curve on day  $t$  by a straight line fitted to all available forward log prices:

$$X_{\tau}(t) = X_0(t) + \alpha(t)\tau \tag{11}$$

where the parameters  $\alpha(t)$  (slope) and  $X_0(t)$  (intercept) are estimated on each day  $t$  by the ordinary least squares method. Note that equation  $(11)$  defines an affine function of the time to maturity. If the slope  $\alpha(t)$  on day t is negative, then the forward curve is in overall backwardation, such as in Figure 3, where the seasonal premium is still clearly present. The positive  $\alpha(t)$  defines the contango forward curve shape. If  $\alpha(t)$  is not significantly different from zero, then we are in the situation of the initial seasonal cost-ofcarry model, with the parameter  $\bar{F}_0(t) = e^{X_0(t)}$  being exactly the geometric average of the forward curve  $F(t)$ .

The seasonal premia  $s(M)$   $(M = 1, \ldots, 12)$  are defined, as before, by the average premia in futures expiring in the calendar month  $M$ , but now with respect to the day- $t$  overall shape of the forward curve, given by the exponent of equation  $(11)$ . The generalized seasonal cost-of-carry model is given by

$$F(t,T) = \bar{F}_0(t)e^{\alpha(t)\tau + s(T) - \gamma(t,\tau)\tau}, \quad \tau = T - t$$
(12)

where  $\gamma(t,\tau)$  is again the stochastic forward premium, defined by the relationship  $(12)$  above. This is a three-factor model. The slope  $\alpha(t)$ , the intercept  $X_0(t)$ , and the stochastic premium  $\gamma(t,\tau)$  are the three fundamental factors. The factors  $X_0(t)$  and  $\alpha(t)$  have a well-known interpretation, closely related to the principal component analysis of the forward curve. They reflect the *level and slope* of the forward curve on date  $t$  and contain most of the forward curve's variability. The remaining stochastic variation of the forward curve, in particular its curvature, is summarized in the stochastic forward premia  $\gamma(t,\tau)$ . All three fundamental factors are pairwise uncorrelated.

The dynamics of the factor  $X_0(t)$  can be a process mean reverting to a constant or an increasing level, or a geometric Brownian motion. Jumps can be incorporated into  $X_0(t)$  as well. The slope  $\alpha(t)$  and the stochastic premium  $\gamma(t,\tau)$  can be modeled as (uncorrelated) mean-reverting processes.

Specifying the factors' dynamics leads to the corresponding forward price dynamics via the relationship  $(12)$ , which holds under any probability measure (statistical or risk neutral). Risk management applications, scenario simulations, and portfolio strategies involving spot and forward positions can be devised using the representation under the statistical probability measure. For purposes of derivatives pricing, the risk-neutral dynamics is of interest. Specifying such dynamics for the three fundamental factors implies the risk-neutral dynamics and distributions for the futures prices. With these in hand, derivatives such as futures options or calendar spread options can be easily valued by a Black-Scholes-like approach or by Monte Carlo simulations. Recall that, under the risk-neutral measure  $Q$ , futures prices are martingales, that is, their drift is identically zero. This results in a restriction on the model parameters under  $O$ , similar to the HJM condition [7] on Treasury forward rates, or the conditions obtained by Amin *et al.*  $[1]$ .

## Conclusions

Building a well-functioning model for commodity forward curves is a challenging task owing to particular features of commodity markets and an inherent multidimensionality of the problem. Applications of commodity forward curve models include the generation of realistic forward curves for risk management and scenario simulations. Moreover, an appropriate model can be used for extending the observed forward curves beyond the most distant liquid maturity, a necessary task in the valuation of physical assets such as gas storage facilities or refineries. The formulation of the fundamental factors' risk-neutral dynamics provides a unifying framework for pricing derivatives, such as calendar spread options, that depend on the entire forward curve.

### **End Notes**

<sup>a.</sup> As a futures contract does not require an initial investment, under  $Q$  its price remains constant on average and there is no drift term representing the average growth on the investment.

b*.* If these risk factors are obtained by the principal component analysis, they are usually interpreted as changes in the level, slope, and curvature of the forward curve.

## **References**

- [1] Amin, K., Ng, V. and Pirrong, C. (2004). *Arbitrage-Free Valuation of Energy Derivatives In: Managing Energy Price Risk*, The New Challenges and Solution. Third Edition Ed. Vincent Kaminski, Risk Books.
- [2] Borovkova, S. & Geman, H. (2006). Seasonal and stochastic effects in commodity forward curves, *Review of Derivatives Research* **9**, 167–186.
- [3] Brennan, M.J. & Schwartz, E.S. (1985). Evaluating natural resource investments, *Journal of Business* **58**(2), 135–157.
- [4] Clewlow, L. & Strickland, C. (2000). *Energy Derivatives: Pricing and Risk Management*, Lacima Publications, London, UK.
- [5] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–407.
- [6] Gibson, R. & Schwartz, E.S. (1990). Stochastic convenience yield and the pricing of oil contingent claims, *Journal of Finance* **45**(3), 959–976.
- [7] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims evaluation, *Econometrica* **60**(1), 77–105.
- [8] Kaldor, N. (1939). Speculation and economic stability, *Review of Economic Studies* **7**, 1–27.
- [9] Litzenberger, R.H. & Rabinowitz, N. (1995). Backwardation in oil futures markets: theory and empirical evidence, *Journal of Finance* **50**(5), 1517–1545.

- [10] Lucia, J. & Schwartz, E.S. (2002). Electricity prices and power derivatives: evidence from the nordic power exchange, *Review of Derivatives Research* **5**(1), 5–50.
- [11] Miltersen, K.R. & Schwartz, E.S. (1998). Pricing of options on commodity futures with stochastic term structures of convenience yield and interest rates, *Journal of Financial and Quantitative Analysis* **33**(3), 33–59.
- [12] Routledge, B.R., Seppi, D.J. & Spatt, C.S. (2000). Equilibrium forward curves for commodities, *Journal of Finance* **55**(3), 1297–1338.
- [13] Schwartz, E.S. (1997). The stochastic behaviour of commodity prices: implications for valuation and hedging, *Journal of Finance* **53**(3), 923–973.
- [14] Sorensen, C. (2002). Modeling seasonality in agricultural commodity futures, *Journal of Futures Markets* **22**(5), 393–426.
- [15] Working, H. (1948). The theory of price of storage, *Journal of Farm Economics* **30**, 1–28.

## **Further Reading**

- Gabillon, J. (1994). Analyzing the forward curve, in *Managing Energy Price Risk*, Risk Publications.
- Geman, H. (2005). *Commodities and Commodity Derivatives*, Wiley Finance.

## **Related Articles**

#### **Commodity Price Models**; **Electricity Forward Contracts**; **Forwards and Futures**.

SVETLANA BOROVKOVA
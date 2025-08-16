## **Commodity Price Models**

Arbitrage models of commodity prices are relative pricing devices. They allow market operators to evaluate commodity-linked securities in terms of *quoted* commodity prices or indices. Spark and crack spread options, multicommodity basket options, swing contracts, and collateralized commodity obligations are just a few examples of financial securities that can be priced (and thus hedged) using commodity models [17]. Moreover, the valuation of certain real assets may benefit from the use of these models. That is the case of long-term investments in natural resources, which can be interpreted as real (*vs*. financial) options written on the value of the corresponding commodity price(s) [37].

Models differ in the *primitives* from which prices of more complex positions can be derived and in the way the stochastic dynamics of these building blocks is described. As a consequence, model selection mainly depends on the level of development characterizing the market under consideration. For instance, oil markets are rather mature; they provide traders with a large quantity of reliable quotes for futures as well as vanilla options; these prices may thus be considered as model primitives. On the contrary, several electricity markets quote spot prices only, which then constitute candidate primitives for valuation purposes.

We begin by deriving the most important commodity valuation formula based on arbitrage considerations; then, we consider four major classes of commodity price models, each one gathering models sharing a common set of primitives; finally, we address a number of modeling issues underlying the design of risk management systems for commodity portfolios.

*Net convenience revenue* is defined as the sum of all benefits (e.g., saved costs of shortage, consumption value, and other side cash flows) minus the sum of all costs (e.g., storage expenses and replacement costs for perishable goods) stemming from physically holding a storable commodity over a period of time [8]. For the purpose of pricing forward contracts, which represent the simplest class of commodity derivatives, net convenience revenue must be computed net of the risk-free rate of interest on the currency of denomination representing the purely financial cost of funding the operation. This computation results in a quantity referred to as *cost of carry*. The underlying argument goes as follows.

Current time is denoted by *t*. We consider a forward contract delivering a single unit of a commodity at a future time *T >t* for a price *x(t)*. Although this price is determined at current time *t*, it represents a cash flow occurring at time *T* . It is assumed that holding the asset over the time interval [*t,T* ] leads to an overall benefit *B* and bears a total cost *C*, both quantities expressed in units of currency available at time *T* . A short forward position at time *t* leads to a time *T* pay off equal to *x (t)* −*S (T )*. At a first glance, one may think of hedging this cash flow by borrowing the present value of delivery price *x (t)* and then buying the underlying asset at current price *S (t)*. However, this strategy generates the required cash flow *S (T )* −*x (t) plus* an additional amount given by the net convenience revenue resulting from the asset holding. We then have to modify our trading strategy in a way to offset the resulting net convenience revenue. This can be done by borrowing funds equal to the present value of *B* − *C*. Table 1 illustrates the resulting *replicating strategy*, which is commonly referred to as *cash-and-carry*. *Vf* denotes the forward contract value and *PT (t)* is the discount factor representing the time *t* value of 1 unit of currency of denomination available at time *T* .

The net cash flow *Vπ (T )* resulting from this trading strategy at delivery is zero. Barring arbitrage opportunities, the time *t* value *Vπ (t)* of the resulting position must vanish as well. This fact leads to a formula for the commodity *forward (fair) value Vf* :

$$V_{\pi}(t) = 0 \Leftrightarrow V_{f}(t)$$
  
=  $S(t) - [x(t) + B - C] \times P_{T}(t)$  (1)

The corresponding time *t forward price fT (t)* is defined as the unique delivery price *x (t)* negotiated at time *t* and making the value *Vf* of the forward contract equal to zero at the same time:

$$f_T(t) = x(t) : V_f(t) = 0 \tag{2}$$

Solving this equation with respect to the unknown delivery price *x (t)* leads to a formula for the arbitrage-free forward price:

$$f_T(t) = \frac{S(t)}{P_T(t)} - (B - C)$$
 (3)

|                 | Position value at $t$                                            | Value at $T$     |
|-----------------|------------------------------------------------------------------|------------------|
| 1 short forward | $-V_{f}(t)$                                                      | $-S(T) + x(t)$   |
| Borrowing \$    | $-[x(t)+B]P_T(t)$                                                | $-x(t)-B$        |
| Lending $$$     | $+C \times P_T(t)$                                               | $+C$             |
| 1 long asset    | $+S(t)$                                                          | $+S(T)+B-C$      |
| Portfolio $\pi$ | $V_{\pi}(t) = -V_{f}(t) - [x(t) + B - C] \times P_{T}(t) + S(t)$ | $V_{\pi}(T) = 0$ |

<table>

 **Table 1** Replicating strategy for a commodity forward contract

If side benefits and costs quote in terms of continuously compounded rates of appreciation  $\beta$  and depreciation  $\chi$  respectively, then we may write the spot-forward parity (3) in the continuously compounded multiplicative form:

$$f_T(t) = \frac{S(t)}{P_T(t)} e^{-(\beta - \chi)[T - t]} \tag{4}$$

The difference  $c := \beta - \chi$  defines the notion of average spot convenience yield per time unit. If  $r$  denotes the continuously compounded risk-free interest yield prevailing on average over the forward contract lifetime, then  $f_T(t) = S(t) e^{[r-(\beta-\chi)][T-t]}$ and the factor  $r - (\beta - \chi)$  represents the yield quoted average cost of carry per time unit.

Spot-forward parities (3) and (4) result from arbitrage considerations under the assumption that:

- 1. a spot price is quoted;
- 2. forward delivery occurs at a single fixed point in time;
- 3. the underlying asset is storable.

In contrast to hypothesis 1, some markets (e.g., oil) do not quote prices for spot delivery. In this case, we may either identify spot with the shortest maturity forward, or simply avoid considering spot prices and focus on forward curve models, whereby forward prices are model primitives and the spot is a derived quantity. As opposed to assumption 2, a few markets (e.g., electricity and shipping freight) quote forwards for delivery over a whole time period. A possible way out consists in finding implied forward prices compatible to the existing market quotes [28]. As far as assumption 3 is concerned, some commodities (e.g., electricity) cannot be stored. This fact prevents traders from performing a cash-and-carry strategy in the way described earlier, which may lead to denying the validity of the spot-forward parity. However, asset storability is not actually required to derive this relationship. One simply need be able to enter a commitment whereby the asset is delivered on the future date  $T$  at the standing spot price  $S(T)$ . This is the case, for instance, of a trader owning the right to handle a production unit with available capacity on the date of delivery.

If any process between interest rate and convenience yield is stochastic, one has to rely on the general arbitrage pricing formula. This formula states that the fair value of a financial security is the risk-neutral expected value of the sum of all discounted future cash flows going to the holder. In a diffusion model setting, risk neutrality operatively translates into a price drift  $\mu_{S}^{*}(t)$  that can equivalently be written either as an instantaneous cost of carry  $r(t) - c(t)$ or as the historical price drift  $\mu_S(t)$  plus the product between price volatility  $\sigma_{S}(t)$  and a *market price of risk* process  $\lambda(t)$ . This latter can be estimated using methods proposed by Benth *et al.* [4] and Kolos and Ronn [29], among others.

In the case of a forward contract issued at time  $t$ and maturing at a future time  $T > t$ , the fair value at time  $s: t \leq s \leq T$  reads as follows:

$$V_f(s) = \mathbb{E}_s^{\mathbb{P}^*} \left( e^{-\int_s^T r(u) \, du} \left( S \left( T \right) - x \left( t \right) \right) \right) \tag{5}$$

where  $\mathbb{P}^*$  denotes the risk-neutral probability, and  $r = (r(u), t \le u)$  is the interest rate process. Substituting this quantity into the zero-value condition  $(2)$ and solving for the delivery price leads to a *general* spot-forward parity:

$$f_T(t) = \frac{\mathbb{E}_t^{\mathbb{P}^*} \left( e^{-\int_t^T r(s) \, \mathrm{d}s} S(T) \right)}{P_T(t)} \tag{6}$$

We note that the underlying convenience revenue implicitly appears via the risk-neutral drift of spot price dynamics, that is,  $\mu_{S}^{*}(t) = r(t) - c(t)$ . We refer to  $c(t)$  as the instantaneous spot convenience  $yield$  associated to commodity S. A more explicit expression is derived in  $[25]$  under the assumption

of a deterministic covariance between spot price and the exponentially integrated convenience yield processes.

Gibson and Schwartz [21] propose a model where commodity prices evolve through a continuous diffusion process driven by two factors: one factor is idiosyncratic to spot price returns; the other affects price evolution through the instantaneous convenience yield process. The resulting *-*<sup>∗</sup>-dynamics read as follows:

$$dS(t) = [r - c(t)]S(t) dt + \sigma_S S(t) dW_S(t) \quad (7)$$

$$dc(t) = \kappa [\alpha^* - c(t)] dt + \sigma_c dW_c(t)$$
 (8)

where *σS* (respectively, *σc*) represents the spot price return (respectively, instantaneous convenience yield) volatility coefficient *κ* denotes the mean reversion frequency of convenience yield; *α*<sup>∗</sup> = *α* + *σcλκ*<sup>−</sup><sup>1</sup> (respectively, *α*) indicates the risk-neutral (respectively, historical) long-term convenience yield level; and the two *-*<sup>∗</sup>-Brownian motions *WS* and *Wc* are assumed to be correlated with a coefficient *ρ*. These dynamics are assumed to start at initial values *S (t*0*)* and *c (t*0*)*. The model represents a prototype for the *spot-convenience yield model* class (SC models). Bjerksund (1991, unpublished manuscript) and Jamshidian and Fein [26] show that forward prices in this model are exponentially affine functions of the pair *(*ln *S (t), c (t))*. This feature is shared by most SC models, a fact leading Bjork and Land ¨ en´ [6] to pursue a systematic study of affine models for commodity prices in the general setting of jumpdiffusions (*see* **Affine Models** for details on affine models in the context of interest rates). SC models have been extensively studied in a number of papers, such as [10, 16, 30, 33, 37, 38], among others. Extensions to jump-diffusions can be found in [12] and [22].

SC models are intuitive in terms of economic interpretation and deliver analytically tractable expressions. However, they experience all consequences stemming from the highly reduced observability of their primitives. First, commodity markets do not quote instantaneous convenience yields. Consequently, filtering techniques (e.g., Kalman) are required to estimate the corresponding process. However, these procedures may deliver an unstable assessment of model parameters, a fact that can undermine the significance of hedging prescriptions resulting from a fitted model. Second, fitting quoted forward curves or term structures of volatility and correlation requires the use of calibration procedures whose effectiveness and numerical stability must be evaluated case by case. Once more, the attention of the modeler is drawn on the nature of the primitives involved in the modeling process. These considerations led a few authors to propose the *forward model* class (FD models) as a viable alternative to SC models.

Jamshidian [24] directly assigns *futures* price *FT (t)* dynamics under the risk-neutral probability *-*<sup>∗</sup> as

$$\frac{\mathrm{d}F_T(t)}{F_T(t)} = \Sigma_T(t) \,\mathrm{d}\mathbf{W}(t) \tag{9}$$

where the initial condition *(FT (t*0*), T* ≥ *t*0*)* is represented by the currently quoted forward price curve and **W** is an *n*-dimensional standard Brownian motion. As theory requires, these processes are all *-*<sup>∗</sup>-martingales, that is, they exhibit no drift [14]. If interest rates are deterministic, model *(*9*)* can be used to describe forward price dynamics as well. This is particularly important in view of the observation that interest rate volatility is usually dominated by commodity price volatility and thus the time value of money can assumed to be nonrandom in this kind of model [37]. Any particular instance of this class results from assigning a value to each of the following three quantities:

- 1. a futures/forward curve quoted at time *t*0;
- 2. a number *n* of statistically independent driving factors;
- 3. a volatility structure *( T (t), t*<sup>0</sup> ≤ *t* ≤ *T )*.

FD models have been studied by Cortazar and Schwartz [11] and Audet *et al.* [2], among others. In particular, Andersen [1] illustrates a number of alternative modeling frameworks and examines their performance in option calibration.

The main benefit from using FD models is that primitives are observable quantities, possibly up to a deterministic transformation of market price data. Moreover, FD models are very intuitive and flexible from a trader's perspective. For instance, they easily allow the user to identify noise terms with a number of forward curve deformations resulting from a statistical analysis of historical market moves. As a result, one obtains a picture of the number of significant noise driving terms as well as the way they impact on the various sections of the forward curve (see [39], among others).

However, spot dynamics implied by FD models *via* the self-explaining assignment  $S(t) := F_t(t)$ need not be Markovian processes. Jamshidian [24] first derives conditions on the volatility structure, ensuring that the resulting spot price dynamics is Markovian. Unfortunately, this and subsequent results pursued within one-factor Heath-Jarrow-Morton interest rate setting cannot be applied to SC models that involve two-factor Markovian processes. Using the Chevette's technique developed for multidimensional HJM interest rates models, Andersen [1] disentangles abstract Markovian factors underlying forward price dynamics. Alternatively, Roncoroni and Id Brik [36] pursue a systematic study on the direct correspondence between SC models and FD models.

A third class of models has been proposed by Miltersen and Schwartz [32]. These authors consider the notion of *instantaneous* forward convenience yield  $c_T(t)$  as implicitly defined through:

$$F_T(t) = S(t) e^{\int_t^T c_s(t) ds}$$
 (10)

for all  $T \geq t$ . It can be shown that the process  $c_t(t)$  is actually the instantaneous convenience yield defined as the formal "instantaneous dividend rate" process  $c(t)$  entering the risk-neutral drift in expression (7). More precisely, Bjork and Landen [6] show that

$$c_{T}(t) = \mathbb{E}_{t}^{\mathbb{P}^{*}}(c(T)) + \frac{\operatorname{Cov}_{t}^{\mathbb{P}^{*}}\left(\mathrm{e}^{-\int_{t}^{T}r(u)\,\mathrm{d}u}S(T),c(T)\right)}{\mathbb{E}_{t}^{\mathbb{P}^{*}}\left(\mathrm{e}^{-\int_{t}^{T}r(u)\,\mathrm{d}u}S(T)\right)}$$
(11)

from which we deduce that  $c_t(t) = c(t)$ .

Although formula (10) defines  $c_T(t)$  in terms of forward and spot prices, for modeling purposes it is actually used the other way around: processes  $S$  and  $c_T$  are defined as primitives for a set of maturities  $T$ ; then forward prices are derived using expression (10) and drift restrictions are calculated on the  $c_T$ dynamics. This methodology defines the forward convenience yield model class (FC models). An interesting application of this setting is represented by the calibration procedure developed in [31].

Compared to both SC and FD models, this setting has the advantage of clearly exhibiting the contribution of spot price and convenience revenue to the formation of a forward price. FC models suffer from similar drawbacks as those affecting SC models: spot prices may be unavailable in the market under consideration; also, (instantaneous forward) convenience yields are rather difficult to imply from market quotes. In particular, differentiating a term structure of forward prices resulting from fitting observed market quotes may generate a curve exhibiting pronounced spikes because of the instability of the differential operator.

A final modeling framework is perhaps the simplest and most popular one. The idea is to focus on the fine properties of a particular class of commodity spot prices without assuming any stochastic structure about the underlying convenience yield dynamics. This restrictive assumption is partly offset by the flexibility introduced upon selecting an appropriate spot price process for modeling and pricing purposes. Spot models for energy price dynamics include  $[1, 3, 7, 9,$ 13, 15, 18, 20, 23, 27, 34, 35], among others. Eydeland and Wolyniec [17] and Fusai and Roncoroni [19] report a large number of examples and references about one-factor commodity price models.

At the time of writing, there seems to be no general consensus on a benchmark setting for pricing commodity-linked derivatives. As a consequence of the arguments illustrated here, we may suggest for the modeler to focus on primitives, structural elements, and driving noise terms.

- 1. Primitives. They should be selected within the set of market quantities for which reliable data are available. In our view, these may involve an appropriate combination of spot, forward, and swap prices or indices according to considerations of representativeness and liquidity. For instance, a market model for electricity or shipping freight indices may build on average prices as introduced in [5], while the general Markovian FD models framework may provide a model generator more suitable for gas and oil markets.
- 2. *Structural elements*. A proper form for price drift, volatility, and jump components, if any, should be identified using statistical analysis of historical data and then fitted to observed prices. One may perform a nonparametric estimation of

these characteristics and then define an appropriate family of functions reproducing the features displayed by the estimated graphs. Besides representativeness, structural elements ought to be selected in such a way that the resulting model is stable under statistical estimation, a property that goes with the reliability of all valuation assessments and hedging prescriptions stemming from using the model in practice.

3. *Driving noise terms*. Number and nature of underlying noise terms should be assessed on the basis of historical price analysis (e.g., examination of the trajectorial properties of price paths, principal components analysis) and jump filtering. For instance, a strong deviation of market price returns measured over short-timelagged data should be interpreted as a sign that prices experience shocks of jump nature. Also, slowly decreasing eigenvalues of the historical covariance matrix of forward price returns are an indication of the significance of asynchronous movements affecting forward curve dynamics.

## **References**

- [1] Andersen, L. (2008). *Markov Models for Commodity Futures: Theory and Practice*, Working Paper, Banc of America Securities.
- [2] Audet, N., Heiskanen, P., Keppo, J. & Vehvilainen, I. (2002). Modelling of electricity forward curve dynamics, in *Modelling Prices in Competitive Electricity Markets*, D.W. Bunn, ed, John Wiley & Sons, pp. 251–265.
- [3] Barlow, M.T. (2002). A diffusion model for electricity prices, *Mathematical Finance* **12**, 287–298.
- [4] Benth, F.E., Cartea, A. & Kiesel, R. (2008). Pricing forward contracts in power markets by the certainty equivalence principle: explaining the sign of the market risk premium, *Journal of Banking and Finance* **32**(10), 2006–2021.
- [5] Benth, F.E. & Koekebakker, S. (2008). Stochastic modeling of financial electricity contracts, *Energy Economics* **30**(3), 1116–1157.
- [6] Bjork, T. & Land ¨ en, C. (2001). On the term struc- ´ ture of futures and forward prices, in *Mathematical Finance–Bachelier Congress 2000*, H. Geman, D. Madan, S.R. Pliska & T. Vorst, eds, Springer Verlag, Berlin, Heidelberg, New York.
- [7] Black, F. (1976). The pricing of commodity contracts, *Journal of Financial Economics* **3**, 167–179.
- [8] Brennan, M. (1991). The price of convenience and the valuation of commodity contingent claims, in *Stochastic Models and Option Values*, D. Lund & B. Oksendal, eds, Elsevier Science.

- [9] Cartea, A. & Figueroa, M.G. (2005). Pricing in electricity markets: a mean reverting jump diffusion model with seasonality, *Applied Mathematical Finance* **12**(4), 313–335.
- [10] Casassus, J. & Collin-Dufresne, P. (2005). Stochastic convenience yield implied from commodity futures and interest rates, *Journal of Finance* **60**, 2283–2331.
- [11] Cortazar, G. & Schwartz, E.S. (1994). The valuation of commodity contingent claims, *Journal of Derivatives* **1**, 27–39.
- [12] Crosby, J. (2008). A multi-factor jump-diffusion model for commodities, *Quantitative Finance* **8**, 181–200.
- [13] De Jong, C. (2006). The nature of power spikes: A regime-switch approach, *Studies in Nonlinear Dynamics and Econometrics*, **10**(3) Article 3.
- [14] Duffie, D. (2001). *Dynamic Asset Pricing Theory*, Princeton University Press.
- [15] Escribano, A., Pena, J.I. & Villaplana, P. (2002). ˜ *Modeling Electricity Prices: International Evidence*, Working Paper 02–27(8), Universidad Carlos III, Madrid.
- [16] Eydeland, A. & Geman, H. (1998). Pricing power derivatives, *Risk* September.
- [17] Eydeland, A. & Wolyniec, K. (2003). *Energy and Power Risk Management: New Developments in Modeling, Pricing and Hedging*, John Wiley & Sons.
- [18] Fusai, G., Marena, M. & Roncoroni, A. (2008). Analytical pricing of discretely monitored Asian-style options: theory and application to commodity markets, *Journal of Banking and Finance* **32**(10), 2033–2045.
- [19] Fusai, G. & Roncoroni, A. (2008). *Implementing Models in Quantitative Finance: Methods and Cases*, Springer Finance.
- [20] Geman, H. & Roncoroni, A. (2006). Understanding the fine structure of electricity prices, *Journal of Business* **79**, 1225–1262.
- [21] Gibson, R. & Schwartz, E.S. (1990). Stochastic convenience yield and the pricing of oil contingent claims, *Journal of Finance* **45**(3), 959–976.
- [22] Hilliard, J.E. & Reiss, J. (1998). Valuation of commodity futures and options under stochastic convenience yields, interest rates, and jump diffusion in the spot, *Journal of Financial and Quantitative Analysis* **33**(1), 61–86.
- [23] Huisman, R. & Mahieu, R. (2003). Regime jumps in electricity prices, *Energy Economics* **25**, 425–434.
- [24] Jamshidian, F. (1992). Commodity option valuation in the Gaussian futures term structure model, *Review of Futures Markets* **10**, 61–86.
- [25] Jamshidian, F. (1993). Option and futures evaluation with deterministic volatilities, *Mathematical Finance* **3**(2), 149–159.
- [26] Jamshidian, F. & Fein, M. (1990). *Closed-Form Solutions for Oil Futures and European Options in the Gibson-Schwartz Model: A Comment*, Working Paper, Financial Strategies Group, Merrill Lynch Capital Markets, New York.
- [27] Jarrow, R.A. (1987). The pricing of commodity options with stochastic interest rates, *Advances in Futures and Options Research* **2**, 19–45.

- [28] Koekebakker, S. & Os Adland, R. (2004). Modelling forward freight rate dynamics—empirical evidence from time charter rates, *Maritime Policy and Management* **31**(4), 319–335.
- [29] Kolos, S.P. & Ronn, E.I. (2008). Estimating the commodity market price of risk for energy prices, *Energy Economics* **30**, 621–641.
- [30] Korn, O. (2005). Drift matters: an analysis of commodity derivatives, *Journal of Futures Markets* **25**, 211–241.
- [31] Miltersen, K. (2003). Commodity price modelling that matches current observables, *Quantitative Finance* **3**, 51–58.
- [32] Miltersen, K. & Schwartz, E.S. (1998). Pricing of options on commodity futures with stochastic term structures of convenience yield and interest rates, *Journal of Financial and Quantitative Analysis* **33**, 33–59.
- [33] Nielsen, M.J. & Schwartz, E.S. (2004). Theory of storage and the pricing of commodity claims, *Review of Derivatives Research* **7**, 5–24.
- [34] Ribeiro, D. & Hodges, S. (2005). A contangoconstrained model for storable commodity prices, *Journal of Futures Markets* **25**(11), 1025–1044.
- [35] Roncoroni, A. (2002). *Essays in quantitative finance: modelling and calibration in interest rate and electricity markets*, Ph.D. Dissertation, Universite Paris IX ´ Dauphine, France.

- [36] Roncoroni, A. & Id Brik, R. (2008). *On The Relationship Between Commodity Forward Models and Spot-Convenience Yield Model*, Working Paper, ESSEC Business School.
- [37] Schwartz, E.S. (1997). The stochastic behavior of commodity prices: implications for valuation and hedging, *Journal of Finance* **52**(3), 923–973.
- [38] Schwartz, E.S. & Smith, J. (2000). Short-term variations and long-term dynamics in commodity prices, *Management Science* **46**, 893–911.
- [39] Tolmasky, C. & Hindanov, D. (2002). Principal components analysis for correlated curves and seasonal commodities: the case of the petroleum, *Journal of Futures Markets* **22**(11), 1019–1035.

## **Related Articles**

**Commodity Forward Curve Modeling**; **Electricity Forward Contracts**; **Forwards and Futures**; **Heath–Jarrow–Morton Approach**.

ANDREA RONCORONI
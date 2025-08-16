# **Electricity Markets**

Since the early 1990s, an increasing number of countries worldwide have liberalized their electricity power sectors. Contrary to the situation that prevailed earlier, when power sectors were not open to competition and prices were set by regulators according to the cost of generation, transmission, and distribution, electricity prices are now determined by an equilibrium of supply and demand, which introduces a substantial price risk with volatilities much higher than those of equity prices. A big share of the total electricity in liberalized power markets is traded over the counter through bilateral agreements. There exists a rich variety of exotic options traded in this market. On the other hand, similar to how the end of the Bretton Woods system in 1973 caused the appearance of currency exchanges, the deregulation of electricity markets has led to the creation of organized electricity exchanges, where electricity is quoted almost as any other commodity (see Table 1 for a list of the major European electricity exchanges).

Although commonly referred to as *commodity*, electricity is in many ways different from the more classical commodities like oil, coal, metals, and agriculture. One substantial difference is that electricity has very limited storage possibilities. To a certain degree, producers may store electricity indirectly in water reservoirs (for hydro-based electricity production) or *via* gas, oil, or coal (for thermal electricity production). However, the consumer of electricity cannot buy for storage. This implies that electricity is not a tradable asset (in the sense that one can buy the asset and sell it later on), and usual hedging arguments to price futures/forwards and other derivatives cannot be applied. Other effects of the lack of storability are strong seasonal and very volatile price behavior. Also, because electricity is only useful when sourced continuously in time, all power contracts concern the delivery of electricity over a *period* of time and not at a fixed point in time. In this sense, electricity markets share more similarities with temperature and also natural gas markets than with the more classical commodity markets. Like electricity, both temperature and natural gas exhibit restricted storage possibilities (storage is impossible for temperature and rather costly for gas), and the corresponding traded contracts are of *flow-over-a-period* type.

Contracts traded on electricity exchanges can typically be divided into two categories: contracts with physical delivery and financially settled contracts. In the following, we shortly sketch the organization of the Scandinavian exchange Nord Pool, but the situation is similar at most other electricity exchanges.

Contracts with physical delivery include actual consumption or production of electricity as part of contract fulfillment. The market for physical delivery is supervised by a so-called transmission system operator (TSO) who balances supply and demand, and market participants are those with proper facilities for production or consumption. Further, contracts with physical delivery are organized in two different submarkets: the *real-time* and the *day-ahead* markets, known as the *two-settlement system*. On the day-ahead market, hourly power contracts for the next day's 24 h (midnight to midnight) are traded. Each day at noon, the day-ahead market is closed for bids and prices for each hour the next day are derived. Electricity prices on the day-ahead market are referred to as *spot prices* as they are reference prices for the financially settled futures/forward contracts. The real-time market, on the other hand, is organized for short-term upward or downward regulation and bids may be posted or changed close to operational time. In both the day-ahead and the real-time market, prices are derived in auctions. The TSO lists bids for each hour according to the price, the so-called *merit order*, and prices are derived by balancing supply and demand.

Financial power contracts are settled financially against a reference price. The market for financial electricity contracts does not require central coordination but can be considered as side bets on the physical system. In contrast to the physical market, a big share of the market players are speculators. The predominantly traded financial contracts are futures/forward type contracts written on the (weighted) average of the hourly spot price (day-ahead market) over a specific *delivery period*. At Nord Pool, there exist daily and weekly contracts of futures type with margin accounts, and monthly, quarterly, and yearly contracts of forward type. Besides futures/forwards contracts, Nord Pool's financial market also organizes trade in European call and put options written on futures/forwards, however, in much smaller volumes.

The substantial electricity price risk introduced by the liberalization of electricity markets requires a precise statistical modeling for risk management,

| Country           | Starting date | Name                                                       |
|-------------------|---------------|------------------------------------------------------------|
| England and Wales | 1990          | Electricity pool                                           |
|                   | 2001          | UK Power Exchange (UKPX)                                   |
| Scandinavia       | 1993          | Nord Pool (Norway only)                                    |
|                   | From 1996     | Sweden, Denmark, Finland consecutively joined<br>Nord Pool |
| Spain             | 1998          | OMEL                                                       |
| Netherlands       | 1999          | Amsterdam Power Exchange (APX)                             |
| Germany           | 2000          | Leipzig Power Exchange (LPX)                               |
|                   | 2001          | European Power Exchange (EEX)                              |
| Poland            | 2000          | Polish Power Exchange                                      |
| France            | 2001          | Powernext                                                  |
| Italy             | 2004          | Gestore Mercato Elettrico (GME)                            |

**Table 1** Major European electricity exchanges

pricing, and asset evaluation purposes. Over recent years, a number of models have been proposed, which basically can be separated in two categories. Models in the first category aim at directly modeling the dynamics of the complete electricity futures curve and, to this end, techniques known from interest rate modeling have been transferred to electricity futures curve modeling (see e.g., [4, 5, 16, 17], and the book [6] with references therein). One of the main problems with this approach is that electricity futures curves seem to have far more complex dynamics than interest rate curves. It seems hardly possible to model the complete futures curve including the spot price in the short end with a reasonable number of factors.

Models in the second category aim at modeling the dynamics of the spot price of electricity. In this framework, the main difficulty when it comes to futures/forwards and other derivatives pricing is the nonstorability of electricity, which makes the market highly incomplete. The cost-of-carry relationship between spot and forward prices breaks down, and a pricing measure (equivalently, market price of risk) has to be identified. Also, since forwardlooking information on a nonstorable asset is not reflected by actual price behavior of this asset, one has to be cautious about the market information modeling [7].

In the following text, we consider reduced-form electricity spot price models, which are members of the second category. In particular, in the section Stylized Feature of Electricity Spot Prices we present the stylized features of electricity spot prices to take into account when specifying a model, before we give a review of reduced-form spot models existing in the literature in the section Reduced-form Electricity Spot Price Models.

# **Stylized Feature of Electricity Spot Prices**

In Figure 1, a section of the daily Nord Pool spot price is shown, which behaves very nicely in the sense that it illustrates well the qualitative characteristics to take into account when specifying a spot price model. In [23], a systematic statistical analysis is performed on spot data from seven electricity exchanges (two American and five European) and the following list of five stylized features common to all data sets has been identified.

## • **Seasonality**

Electricity spot prices reveal seasonal behavior in yearly, weekly, and daily cycles. However, the seasonality has little effect on the overall variability of the price data.

## • **Stationarity**

Similar to other commodities, electricity prices tend to exhibit stationary behavior. They are mean reverting to a trend which, however, may exhibit slow stochastic variations (see Figure 2).

## • **Multiscale autocorrelation**

The observed autocorrelation structure of most European price series is described quite precisely with a weighted sum of exponentials:

$$\sum_{i=1}^{n} w_i \,\mathrm{e}^{-h\lambda_i} \tag{1}$$

where the number *n* of factors needed for a good description is 2 or 3, and the weights *wi* add

![](_page_2_Figure_1.jpeg)

**Figure 1** Daily spot price at Nord Pool spanning the period April 1, 1997–July 14, 2000

![](_page_2_Figure_3.jpeg)

**Figure 2** UKPX time series (after the seasonality has been removed) and its 6-month moving average

up to 1 (see Figure 3). We mention that the two American and also the Nord Pool price series exhibit a quite different, almost nonstationary, autocorrelation structure, which might be due to different market organization.

• **Spikes**

All data sets of electricity spot prices show impressive spikes, that is, violent upward jumps followed by rapid return to about the same level. The intensity of spike occurrence can vary over time. This fundamental property of electricity prices is due to the nonstorability of this commodity, and any relevant spot price model must take this feature into account. In [19, 23], it is ascertained that appropriate modeling of spike risk requires a Pareto-like distribution with polynomial tail.

## • **Non-Gaussianity**

The examination of daily spot prices reveals a highly non-Gaussian distribution, which tends to be slightly positively skewed and strongly leptokurtic. This high excess kurtosis is explained by the presence of the low-probability largeamplitude spikes.

![](_page_3_Figure_1.jpeg)

**Figure 3** Fitting the autocorrelation function with a sum of two exponentials.  $(a-c)$  APX, EEX, UKPX

# **Reduced-form Electricity Spot Price** Models

We conclude this article by presenting some spot price models existing in the literature. For this, we restrict to an overview as given in [23] of *reduced*form models in continuous time, but we mention that there is a variety of different spot model types like hybrid models or econometric time series models (see, e.g., [20, 21, 24] or the text books [9, 12, 13, 26] with references therein).

#### Structural Models

Structural or equilibrium models as proposed in [1, 18] derive prices by balancing supply and demand. The (very inelastic) demand for electricity is described by a stochastic process

$$D_t = \overline{D_t} + X_t \tag{2}$$

$$dX_t = (\mu - \lambda X_t) dt + \sigma dW_t \tag{3}$$

where  $\overline{D_t}$  describes the seasonal component and  $X_t$ corresponds to the stationary stochastic part. The price is obtained by matching the demand level with a deterministic supply function. In particular, the supply function must be nonlinear and strongly increasing in the right end to account for exploding cost of electricity generation (price spikes) in times of sudden rise in demand. Barlow [1] proposes

$$P_t = \left(\frac{a_0 - D_t}{b_0}\right)^{1/\alpha} \tag{4}$$

for some  $\alpha > 0$ , while Kanamura and Ohashi [18] suggest a "hockey stick" profile

$$P_t = (a_1 + b_1 D_t) 1_{D_t \le D_0}$$
  
+  $(a_1 + b_1 D_t) 1_{D_t > D_0}$  (5)

Further, we mention in this category market equilibrium models as derived in  $[8, 15]$ .

#### Markov Models

Geman and Roncoroni [14] model the electricity logprice as a one-factor Markov jump diffusion.

$$dP_t = \theta(\mu_t - P_t) dt + \sigma dW_t + h(t) dJ_t \quad (6)$$

The spikes are introduced by making the jump direction and intensity level-dependent: if the price is high, the jump intensity is high and downward jumps are more likely, whereas if the price is low, jumps are rare and upward-directed.

#### Regime-switching Models

In the one-factor Markov specification of Geman and Roncoroni [14], the "spike regime" is distinguished from the "base regime" by a deterministic threshold on the price process: if the price is higher than a given value, the process is in the "spike regime"; otherwise it is in the "base regime". This threshold value may be difficult to calibrate and it is not very realistic to suppose that it is determined in advance. Regimeswitching models as in [27] alleviate this problem by introducing a two-state unobservable Markov chain, which determines the transition from "base regime" to "spike regime" with greater volatility and faster mean reversion

$$dP_t = \theta^1(\mu_t - P_t) + \sigma^1 dW_t \quad \text{(base regime)} \quad (7)$$
  
$$dP_t = \theta^2(\mu_t - P_t) + \sigma^2 dW_t \quad \text{(spike regime)} \quad (8)$$

#### Multifactor Ornstein-Uhlenbeck Models

Multifactor Ornstein-Uhlenbeck models describe the deseasonalized logarithmic spot price (geometric models), alternatively the deseasonalized spot

![](_page_4_Figure_1.jpeg)

**Figure 4** Comparison of the real EEX series (b) and the simulated series with estimated parameters (a)

price (arithmetic models), as a sum of independent Levy-driven Ornstein–Uhlenbeck components: ´

$$X(t) = \sum_{i=1}^{n} Y_i(t)$$
  

$$dY_i(t) = -\lambda_i Y_i(t) dt + dL_i(t), \quad Y_i(0) = y_i$$
  
(10)

where processes *Li(t)* are independent, possibly time inhomogeneous Levy processes. For example, ´ in the case of a two-factor model, the first factor corresponds to the stochastic base signal with a slow rate of mean reversion *λ*1, and the second factor represents the spikes and has a high rate of mean reversion *λ*2. The earliest model in this family proposed in the literature is a Gaussian one-factor model in [25]. Subsequently, several authors have proposed various improvements [2, 3, 11, 22]. We also mention here the model in [10], which is a mixture of a structural and a multifactor model.

Multifactor Ornstein–Uhlenbeck models are capable of capturing all the stylized features presented in the previous section and to precisely describe daily spot price dynamics. In particular, the arithmetic model proposed in [3] can reproduce the multiscale autocorrelation structure of European spot prices, and, at the same time, it is mathematically very tractable. However, due to their non-Markovianity, in case of several factors, estimation of multifactor models is not obvious. In [19, 23], we develop statistical estimation procedures based on separation of the data into a spike and a base component. In [23], this procedure is based on methods from nonparametric statistics, while we use tools from extreme value theory in [19]. Figure 4 shows a simulation of a twofactor model as a result of an estimation on EEX data in [19].

# **References**

- [1] Barlow, M.T. (2002). A diffusion model for electricity prices, *Mathematical Finance* **12**, 287–298.
- [2] Barlow, M.T., Gusev, Y. & Manpo, L. (2004). Calibration of multifactor models in electricity markets, *International Journal of Theoretical and Applied Finance* **7**, 101–120.
- [3] Benth, F.E., Kallsen, J. & Meyer-Brandis, T. (2007). A non-Gaussian Ornstein-Uhlenbeck process for electricity spot price modeling and derivatives pricing, *Applied Mathematical Finance* **14**(2), 153–169.
- [4] Benth, F. & Koekebakker, S. (2008). Stochastic modeling of financial electricity contracts, *Energy Economics* **30**(3), 1116–1157.
- [5] Benth, F.E., Koekebakker, S. & Ollmar, F. (2008). Extracting and applying smooth forward curves from average-based commodity contracts with seasonal variation, *Journal of Derivatives* Fall, 52–66.

# **6 Electricity Markets**

- [6] Benth, F., Koekebakker, S. & Saltyte-Benth, J. (2008). Stochastic modeling of electricity and related markets, in *Advanced Series on Statistical Science and Applied Probability*, O.E. Barndorff-Nielsen, ed., World Scientific, Vol. 11.
- [7] Benth, F. & Meyer-Brandis, T. (2009). The information premium in electricity markets, *Journal of Energy Markets* **2**(3), accepted.
- [8] Bessembinder, H. & Lemmon, M. (2002). Equilibrium pricing and optimal hedging in electricity forward markets, *Journal of Finance* **57**, 1347–1382.
- [9] Burger, M., Graeber, B. & Schindlmayr, G. (2007). *Managing Energy Risk*, John Wiley & Sons, Chichester.
- [10] Burger, M., Klar, B., Muller, A. & Schindlmayer, G. (2004). A spot market model for pricing derivatives in electricity markets, *Quantitative Finance* **4**, 109–122.
- [11] Deng, S.-J. & Jiang, W. (2005). Levy process-driven ´ mean-reverting electricity price model: the marginal distribution analysis, *Decision Support Systems* **40**, 483–494.
- [12] Eydeland, A. & Wolyniec, K. (2003). *Energy and Power Risk Management*, John Wiley & Sons, Chichester.
- [13] Geman, H. (2005). *Commodities and Commodity Derivatives*, Wiley-Finance, John Wiley & Sons, Chichester.
- [14] Geman, H. & Roncoroni, A. (2006). Understanding the fine structure of electricity prices, *Journal of Business* **79**, 1225–1261.
- [15] Hinz, J. (2003). Modeling day ahead prices, *Applied Mathematical Finance* **10**(2), 149–161.
- [16] Hinz, J., von Grafenstein, L., Verschuere, M. & Wilhelm, M. (2005). Pricing electricity risk by interest rate methods, *Quantitative Finance* **5**(1), 49–60.
- [17] Hinz, J. & Wilhelm, M. (2006). Pricing flowcommodity derivatives using fixed income market techniques, *International Journal of Theoretical and Applied Finance* **9**(8), 1299–1321.
- [18] Kanamura, T. & Ohashi, K. (2007). A structural model for electricity prices with spikes: measurement of spike risk and optimal policies for hydropower plant operation, *Energy Economics* **29**(5), 1010–1032.
- [19] Kluppelberg, C., Meyer-Brandis, T. & Schmidt, A. ¨ (2008). Electricity spot price modelling with a view

towards extreme spike risk, *Quantitative Finance* accepted.

- [20] Knittel, C. & Roberts, M. (2001). *An Empirical Examination of Deregulated Electricity Prices*. POWER WP-087, University of California Energy Institute.
- [21] Leon, A. & Rubia, A. (2004). Testing for weekly seasonal unit roots in the Spanish power pool, in *Modelling Prices in Competitive Electricity Markets*, D.W. Bunn, ed., Wiley Series in Financial Economics, Wiley, pp. 177–189.
- [22] Lucia, J. & Schwartz, E.S. (2002). Electricity prices and power derivatives: evidence from the Nordic Power Exchange, *Review of Derivatives Research* **5**(1), 5–50.
- [23] Meyer-Brandis, T. & Tankov, P. (2008). Multi-factor jump-diffusion models of electricity prices, *IJTAF* **11**(5), 503–528.
- [24] Misiorek, A., Trueck, S. & Weron, R. (2006). Point and interval forecasting of spot electricity prices: Linear vs. non-linear time series models, *Studies in Nonlinear Dynamics and Econometrics* **10**(3), Article 2.
- [25] Schwartz, E.S. (1997). The stochastic behavior of commodity prices: implications for valuation and hedging, *Journal of Finance* **52**(3), 923–973.
- [26] Weron, R. (2006). *Modeling and Forecasting Electricity Loads and Prices – A Statistical Approach*, John Wiley & Sons, Chichester.
- [27] Weron, R. (2009). Heavy-tails and regime-switching in electricity prices, *Mathematical Methods of Operations Research* **69**(3), 457–473.

# **Related Articles**

**Commodity Forward Curve Modeling**; **Commodity Price Models**; **Electricity Forward Contracts**; **Stylized Properties of Asset Returns**; **Swing Options**.

THILO MEYER-BRANDIS
# **Electricity Forward** Contracts

In quantitative modeling of the electricity market, a fundamental question is to establish the link between spot and forward prices. The classical theory of arbitrage, including storage and convenience yield, does not easily carry over to electricity because of a single complicating fact: the nonstorability of the commodity. In this article, we discuss the spotforward relation for electricity in view of the classical theory.

## Forward Pricing by No Arbitrage

Let us recall how to derive forward prices using noarbitrage arguments. Denote by  $S(t)$  the spot price of an asset at time  $t > 0$ , and consider a forward contract with delivery at time  $T \ge t$ . To prevent arbitrage opportunities, the forward price  $f(t, T)$  at time t must be

$$f(t,T) = S(t) \exp(r(T-t)) \tag{1}$$

with  $r > 0$  being the risk-free interest rate. If this is not the case, we can exploit a buy-and-hold strategy to obtain arbitrage. For example, if  $f(t, T) >$  $S(t) \exp(r(T-t))$ , finance a purchase of the spot contract with borrowing money and go short the forward. At delivery, hand over the spot, pay the debt with continuously compounding interest  $r$ , and receive the forward price. This entails in a sure win  $f(t, T) - S(t) \exp(r(T - t))$ . Obviously, if the forward price is less than  $S(t) \exp(r(T-t))$ , the strategy above is reversed. A fundamental assumption in this trading scheme is the storability of the spot.

If  $S(t)$  is a semimartingale process on a filtered probability space  $(\Omega, (\mathcal{F}_t), \mathcal{F}, P)$ , there exists risk *neutral probabilities*  $Q$  such that the discounted spot price is a  $Q$ -martingale. The forward price can be represented alternatively as a conditional expectation with respect to  $Q$ , that is,

$$f(t,T) = \mathbb{E}_{Q} \left[ S(T) \, | \, \mathcal{F}_{t} \right] \tag{2}$$

where  $\mathcal{F}_t$  is the given information filtration in the market. We remark in passing that, in general, we have many pricing measures  $Q$  for a semimartingale process, but because of the buy-and-hold strategy we get a unique forward price.

The risk premium is defined as the difference between the forward price and the predicted spot price at delivery, that is,

$$P(t,T) \stackrel{\Delta}{=} f(t,T) - \mathbb{E}\left[S(T) \,|\, \mathcal{F}_t\right] \tag{3}$$

Letting  $S(t)$  be a geometric Brownian motion,

$$dS(t) = \mu S(t) dt + \sigma S(t) dB(t) \tag{4}$$

we easily find that

$$P(t,T) = S(t) \left( e^{r(T-t)} - e^{\mu(T-t)} \right) \tag{5}$$

which is negative in "normal" markets since the expected return  $\mu$  is naturally bigger than the riskfree interest rate, Hence, the forward price is below the expected spot, which is referred to as the forward market being in normal backwardation. In economical terms, this is explained as the producers wanting to secure their future income and hence creating a hedging pressure in the market. The opposite situation, when the risk premium is positive, is referred to as the forward market being *contango*.

One can easily imagine frictions in the market preventing the feasability of the buy-and-hold strategy. Typically, in commodity markets, costs related to storage and transportation are incurred. The price for storage leads to a modification of the forward price. One also talks of a convenience vield in commodity markets, understanding a discount in the forward price due to the *convenience* to own the underlying spot. In effect, these modifications lead to a forward price

$$f(t,T) = S(t) \exp((r-\delta)(T-t)) \tag{6}$$

where  $\delta$  is a factor accounting for storage, convenience yield, transportation, and so on.

The forward price can still be expressed in terms of a conditional expectation as in equation (2), but now we use pricing measures  $Q$ , which do not necessarily turn the discounted spot dynamics into a  $Q$ -martingale. Hence, by a specific choice of  $Q$  one may represent equation  $(6)$  as in equation  $(2)$ . Considering the specific case of a geometric Brownian motion again, equation (6) is obtained by using the Girsanov transformation to introduce a measure  $Q$ under which

$$dW(t) = \frac{\mu - (r - \delta)}{\sigma} dt + dB(t) \tag{7}$$

is a Brownian motion. Note that this change of measure does not turn the discounted spot price into a Q-martingale. However, more importantly, normal backwardation is no longer the immediate implication, since the sign of the risk premium

$$P(t,T) = S(t) \left( e^{(r-\delta)(T-t)} - e^{\mu(T-t)} \right) \tag{8}$$

is determined by the relation between r,  $\delta$ , and  $\mu$ which is not *a priori* clear. Thus, we may have a market either in contango or in backwardation; however, we cannot have both in the sense that the sign of the risk premium changes with time to maturity of the contracts.

#### The Case of Electricity

In real electricity markets, the forward and futures contracts<sup>a</sup> deliver the power over a period rather than at a specific future time point. Thus, a long position entered at time  $t$  in an electricity forward delivering over the period  $[\tau_1, \tau_2], t \leq \tau_1$  gives a profit/loss

$$\int_{\tau_1}^{\tau_2} S(T) \, \mathrm{d}T - (\tau_2 - \tau_1) F(t, \tau_1, \tau_2) \tag{9}$$

with  $F(t, \tau_1, \tau_2)$  being the forward price denoted in a currency per megawatt hour.<sup>b</sup> The question is what  $F(t, \tau_1, \tau_2)$  should be.

Electricity is a nonstorable commodity by physical nature. Once purchased, we must use it, and any buyand-hold strategy is not feasible. One cannot talk of any storage costs for electricity and nor of any convenience yield. This means that there is no natural connection as in equation (6). However, based on equation (2) we can *define* the electricity forward price as

$$F(t, \tau_1, \tau_2) = \mathbb{E}_{\mathcal{Q}} \left[ \frac{1}{\tau_2 - \tau_1} \int_{\tau_1}^{\tau_2} S(T) \, \mathrm{d}T \, | \, \mathcal{F}_t \right] \tag{10}$$

Interchanging expectation and  $dT$ -integration, we get

$$F(t, \tau_1, \tau_2) = \frac{1}{\tau_2 - \tau_1} \int_{\tau_1}^{\tau_2} f(t, T) \, \mathrm{d}T \tag{11}$$

indicating that an electricity forward corresponds to the average of forward contracts delivering at each time point  $t$  in the settlement period.

In order to make equation  $(10)$  or  $(11)$  operational, one must specify a spot price dynamics and a pricing

measure Q. Since  $S(t)$  is nonstorable, it cannot be used for any hedging purposes, and in this respect functions only like an index for the forward price. We can therefore choose any stochastic dynamics we like for the spot, even going beyond the semimartingale framework as is usually required in mathematical finance. The pricing measure  $O$  is a priori any equivalent probability measure. In practice, however, we want to choose a  $O$  such that we know the dynamics of  $S$  under this measure to be able to calculate the conditional expectation. A valid choice is  $Q = P$ ; however, this would imply a zero-risk premium, which is hardly a realistic situation.

Empirical investigations in electricity markets show that one may have a change of sign in the risk premium. Thus, it may not be the case that the market is either in normal backwardation or in contango. In fact, one has observed a positive premium in the short end of the forward market, whereas contracts with maturity in the longer end have a negative premium. The latter is consistent with producers creating a hedging pressure since they want to lock in their production. However, the positive premium in the short end has been explained by the consumers' wish to hedge the spike risk inherent in spot prices. Thus, in order to hedge the risk of paying a high spot price, the consumers are willing to pay a premium. See [7] for more on this. Bessembinder and Lemmon [5] develop an equilibrium model for the electricity market with consumers and producers. On the basis of a discrete-time equilibrium model for the spot prices, the authors show that the risk premium in the forward market depends on both price variation and right skewedness of prices. Longstaff and Wang [8] found empirical evidence for these propositions in the Pennsylvania, New Jersey, and Maryland (PJM) market.

We observe that, by definition,  $F(t, \tau_1, \tau_2)$  is a  $Q$ -martingale. This is in accordance with the noarbitrage theory that states that all forward contracts must be martingales under the pricing measure. Observe that when t approaches start of delivery  $\tau_1$ , we do not, in general, have that  $F(t, \tau_1, \tau_2)$  converges to the spot price. This is rather natural since the forward contract depends on the spot over a period of delivery, and not only at a fixed time of delivery. On the other hand, this is a distinct feature for electricity markets, which is not observed in most other commodity markets. An immediate effect of this is that one does not expect the same degree of sensitivity to spot price variations in electricity forwards as for other commodities.

The range of spot models that allow for explicit electricity forward prices is rather limited. Much of the literature on commodites focuses on meanreverting spot price models, and the exponential Ornstein–Uhlenbeck process (*see* **Ornstein–Uhlenbeck Processes**)

$$S(t) = S(0) \exp(X(t)) \tag{12}$$

where

$$dX(t) = \alpha(\theta - X(t)) dt + \sigma dB(t) \qquad (13)$$

is the classical example; see [9]. This model has been generalized to allow for jumps modeling spikes (see [6] for the threshold model by Geman and Roncoroni). However, even though one can derive explicit expressions for the forward prices *f (t, T )*, it seems to be very hard to obtain the same for electricity forwards (see [4] for examples). On the other hand, arithmetic models as suggested in [2] seem to be appropriate for this.

The problem of choosing the right pricing measure *Q* can be approached from several different angles. The most common is by means of introducing a parameterized class of pricing measures *Q*, that is, pricing measures that depend on one or more parameters. These parameters will appear in the forward prices, and thus one may estimate them by calibration to observed forward prices. The relation between *<sup>P</sup>* and the estimated pricing measure *<sup>Q</sup>* would give us a statistical estimate on the risk premium in the market.

Benth *et al.* [1] propose to model the formation of forward prices from spot by using the certainty equivalence principle. Two representative agents, a consumer and a producer, decide whether to trade in the spot or forward market, based on where prices are more preferable. The certainty equivalence principle leads to forward pricing bounds within which the settled forward prices must lie. Introducing the market power as an explanatory variable, forward prices can be expressed in terms of the spot. Moreover, the risk premium is stochastic, and a positive premium in the short end of the forward curve is explicitly linked to the spikes in the spot, a feature which is in line with [7]. One may derive the risk neutral pricing measure for option pricing purposes. Empirical support for this approach has been found in an analysis of spot and forward price data observed at the German electricity exchange EEX.

An alternative approach promoted in [3] is to use the *Heath–Jarrow–Morton* (HJM, *see* **Heath– Jarrow–Morton Approach**) idea from *interestrate modeling* to electricity forwards. This entails modeling the price dynamics *t* → *F (t, τ*1*, τ*2*)* for arbitrary delivery periods [*τ*1*, τ*2]. In fact, the application of HJM in electricity is not straightforward. At Nord Pool, say, the market trades in contracts with overlapping delivery periods, leading to certain price relations that must be met to avoid arbitrage possibilities. Benth and Koekebakker [3] show that this leads to rather strong restrictions on the feasible models; for instance, geometric Brownian motion with timedependent volatility is ruled out. Furthermore, the connection to the underlying spot price is lost since there is no convergence of electricity forwards to the spot when time to delivery goes to zero. We refer to [3] and the monograph [4] for more discussion on these issues and empirical studies of data from Nord Pool where a market model (*LIBOR model*, *see* **LIBOR Market Model**) approach is taken.

## **End Notes**

a*.* We assume constant interest rate *r* and make no distinction between a forward and a futures contract.

b*.* At Nord Pool, the settlement is with respect to the hourly spot price over the delivery period. This would entail a summation over the spot prices at the discrete hours. However, we choose to work with the slightly more notational convenient integration.

## **References**

- [1] Benth, F.E., Cartea, A. & Kiesel, R. (2008). Pricing forward contracts in power markets by the certainty equivalence principle: explaining the sign of the market risk premium. *Journal of Banking Finance* **32**(10), 2006–2021.
- [2] Benth, F.E., Kallsen, J. & Meyer-Brandis, T. (2007). A non-Gaussian Ornstein-Uhlenbeck process for electricity spot price modeling and derivatives pricing, *Applied Mathematical Finance* **14**(2), 153–169.
- [3] Benth, F.E. & Koekebakker, S. (2008). Stochastic modeling of financial electricity contracts, *Energy Economics* **30**(3), 1116–1157.
- [4] Benth, F.E., Saltyt ˇ e Benth, J. & Koekebakker, S. (2008). ˙ *Stochastic Modelling of Electricity and Related Markets*, World Scientific.

## **4 Electricity Forward Contracts**

- [5] Bessembinder, H. & Lemmon, M. (2002). Equilibrium pricing and optimal hedging in electricity forward markets, *Journal of Finance* **57**, 1347–1382.
- [6] Geman, H. & Roncoroni, A. (2006). Understanding the fine structure of electricity prices, *Journal of Business* **79**(3), 1225–1261.
- [7] Geman, H. & Vasicek, O. (2001). Forwards and futures on non-storable commodities: the case of electricity, *Risk* **August**, 12–27.
- [8] Longstaff, F.A. & Wang, A.W. (2004). Electricity forward prices: a high-frequency empirical analysis, *Journal of Finance* **59**(4), 1877–1900.
- [9] Lucia, J. & Schwartz, E.S. (2002). Electricity prices and power derivatives: evidence from the Nordic Power Exchange, *Review of Derivatives Research* **5**(1), 5–50.

## **Related Articles**

**Commodity Forward Curve Modeling**; **Commodity Price Models**; **Forwards and Futures**.

FRED E. BENTH
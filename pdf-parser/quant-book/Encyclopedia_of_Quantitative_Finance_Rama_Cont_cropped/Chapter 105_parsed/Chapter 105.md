# **Foreign Exchange Basket** Options

Quite often, corporate and institutional currency managers are faced with an exposure in more than one currency. Generally, these exposures would be hedged using individual strategies for each currency. These strategies are composed of spot transactions, forwards, and, in many cases, options on a single currency. Nevertheless, there are instruments that include several currencies, and these can be used to build a multicurrency strategy that is almost always cheaper than the portfolio of the individual strategies. As a leading example, we explain basket options in detail.<sup>a</sup>

#### **Basket Options**

Basket options are derivatives based on a common base currency, say EUR and several other risky currencies. The option is actually written on the basket of risky currencies. Basket options are European options paying the difference between the basket value and the strike, if positive, for a basket call, or the difference between strike and basket value, if positive, for a basket put, respectively, at maturity. The risky currencies have different weights in the basket to reflect the details of the exposure.

For example, a basket call on two currencies USD and JPY pays off

$$\max\left(a_1\frac{S_1(T)}{S_1(0)} + a_2\frac{S_2(T)}{S_2(0)} - K; 0\right) \tag{1}$$

at maturity T, where  $S_1(t)$  denotes the exchange rate of EUR/USD and  $S_2(t)$  denotes the exchange rate of EUR/JPY at time t,  $a_i$  the corresponding weights, and  $K$  the strike.

A basket option protects against a drop in both currencies at the same time. Individual options on each currency cover some cases, which are not protected by a basket option (shaded triangular areas in Figure 1) and that is why they cost more than a basket.

The ellipsoids connect the points that are reached with the same probability assuming that the forward prices are at the center.

#### **Pricing Basket Options**

Basket options should be priced in a consistent way with plain vanilla options. Hence the basic model assumption is a lognormal process for the individual correlated basket components. A decomposition into uncorrelated components of the exchange rate processes

$$dS_i = \mu_i S_i dt + S_i \sum_{j=1}^N \Omega_{ij} dW_j \qquad (2)$$

is the basis for pricing. Here  $\mu_i$  denotes the difference between the foreign and the domestic interest rate of the *i*th currency pair and  $dW_i$  the *j*th component of independent Brownian increments. The covariance matrix is given by  $C_{ij} = (\Omega \Omega^{\text{T}})_{ij} = \rho_{ij} \sigma_i \sigma_j$ . Here  $\sigma_i$ denotes the volatility of the *i*th currency pair and  $\rho_{ij}$ the correlation coefficients.

#### Exact Method

Starting with the uncorrelated components, the pricing problem is reduced to the  $N$ -dimensional integration of the payoff. This method is accurate but rather slow for more than two or three basket components.

#### A Simple Approximation

A simple approximation method assumes that the basket spot itself is a lognormal process with drift  $\mu$  and volatility  $\sigma$  driven by a Wiener Process  $W(t)$ :

$$dS(t) = S(t)[\mu \, dt + \sigma \, dW(t)] \tag{3}$$

with solution

$$S(T) = S(t)e^{\sigma W(T-t) + (\mu - 1/2\sigma^2)(T-t)}$$
(4)

given we know the spot  $S(t)$  at time t. It is a fact that the sum of lognormal processes is not lognormal itself, but as a crude approximation, it is certainly a quick method that is easy to implement. To price the basket call, the drift and the volatility of the basket spot need to be determined. This is done by matching the first and second moment of the basket spot with the first and second moment of the lognormal model for the basket spot. The moments of lognormal spot are

$$E(S(T)) = S(t)e^{\mu(T-t)}$$
  
$$E(S(T)^{2}) = S(t)^{2}e^{(2\mu+\sigma^{2})(T-t)}$$
 (5)

![](_page_1_Figure_1.jpeg)

Figure 1 Basket-payoff and contour lines for probabilities

We solve these equations for the drift and volatility:

$$\mu = \frac{1}{T - t} \ln\left(\frac{E(S(T))}{S(t)}\right)$$
$$\sigma = \sqrt{\frac{1}{T - t} \ln\left(\frac{E(S(T)^{2})}{E(S(T))^{2}}\right)} \tag{6}$$

In these formulae we now use the moments for the basket spot:

$$\begin{split} \mathbf{E}(S(T)) &= \sum_{i=1}^{N} \alpha_i S_i(t) \mathbf{e}^{\mu_i(T-t)} \\ \mathbf{E}(S(T)^2) &= \sum_{i,j=1}^{N} \alpha_i \alpha_j S_i(t) S_j(t) \\ &\quad \times \mathbf{e}^{\left(\mu_i + \mu_j + \sum_{k=1}^{N} \Omega_{ki} \Omega_{jk}\right)(T-t)} \end{split} \tag{7}$$

The pricing formula is the well-known Black-Scholes-Merton formula for plain vanilla call options:

$$\begin{aligned} \upsilon(0) &= \mathsf{e}^{-r_d T} \left( F \mathbf{N}(d_+) - K \mathbf{N}(d_-) \right) \\ F &= S(0) \mathsf{e}^{\mu T} \\ d_{\pm} &= \frac{1}{\sigma \sqrt{T}} \left( \ln \left( \frac{F}{K} \right) \pm \frac{1}{2} \sigma^2 T \right) \end{aligned} \tag{8}$$

Here  $N$  denotes the cumulative normal distribution function and  $r_d$  the domestic interest rate.

#### A More Accurate and Equally Fast Approximation

The previous approach can be taken one step further by introducing one more term in the Itô-Taylor expansion of the basket spot, which results in

$$\begin{split} \upsilon(0) &= \mathsf{e}^{-r_d T} \left( F \mathbf{N}(d_1) - K \mathbf{N}(d_2) \right) \\ F &= \frac{S(0)}{\sqrt{\eta}} \mathsf{e}^{\left(\mu - \lambda/2 + (\lambda \sigma^2/2(\eta))\right) T} \\ d_2 &= \frac{\sigma - \sqrt{\sigma^2 + \lambda \left( (1 + (\lambda/\eta)) \sigma^2 T - 2\ln(F\sqrt{\eta}/K) \right)}}{\sqrt{T} \lambda} \\ d_1 &= \sqrt{\eta} d_2 + \frac{\sigma \sqrt{T}}{\sqrt{\eta}} \end{split} \tag{9}$$

where  $\eta = 1 - \lambda T$ 

The new parameter  $\lambda$  is determined by matching the third moment of the basket spot and the model spot. For details, see [1].

Most remarkably, this major improvement in the accuracy only requires a marginal additional computation effort.

# **Correlation Risk**

Correlation coefficients between market instruments are usually not obtained easily. Either historical data analysis or implied calibrations need to be done. However, in the foreign exchange (FX) market, the cross instrument is traded as well. For instance, in the example above, USD/JPY spot and options are traded, and the correlation can be determined from this contract. In fact, denoting the volatilities as in the tetrahedron (Figure 2), we obtain formulae for the correlation coefficients in terms of known market implied volatilities:

$$\rho_{12} = \frac{\sigma_3^2 - \sigma_1^2 - \sigma_2^2}{2\sigma_1\sigma_2}$$
$$\rho_{34} = \frac{\sigma_1^2 + \sigma_6^2 - \sigma_2^2 - \sigma_5^2}{2\sigma_3\sigma_4} \tag{10}$$

![](_page_1_Figure_20.jpeg)

Figure 2 Currency tetrahedron including cross contracts

| Table 1                           |       |
|-----------------------------------|-------|
| GBP/USD                           | 8.9%  |
| USD/JPY                           | 10.1% |
| GBP/JPY                           | 9.8%  |
| EUR/USD                           | 10.5% |
| EUR/GBP                           | 7.5%  |
| EUR/JPY                           | 10.0% |
| FX implied volatilities for three |       |

month at-the-money vanilla options as of November 23, 2001. *Source*: Reuters

This method also allows hedging correlation risk by trading FX implied volatility. For details see [1].

# **Practical Example**

To find out how much one can save using a basket option, we take EUR as a base currency and consider a basket of three currencies USD, GBP, and JPY. For the volatilities, we take the values in Table 1.

The resulting correlation coefficients are given in Table 2.

The amount of option premium one can save using a basket call rather than three individual call options is illustrated in Table 3.

The amount of premium saved essentially depends on the correlation of the currency pairs (Figure 3). In Figure 3, we take the parameters of the previous scenario, but restrict ourselves to the currencies USD and JPY.

# **Upper Bound by Vanilla Options**

It is actually clear that the price of the two vanilla options in the previous example is an upper bound of the basket option price. It seems intuitively clear that for a correlation of 100% the price is the same.

| Table 3            |        |               |        |
|--------------------|--------|---------------|--------|
| Base currency      | EUR    | Interest rate | 4.0%   |
| Nominal in EUR     | 39 007 | Strike K      | 1      |
| Currencies         | USD    | JPY           | GBP    |
| Nominals           | 29%    | 30%           | 41%    |
| 1/spot             | 1.1429 | 0.00919       | 1.6091 |
| Spot               | 0.8750 | 108.81        | 0.6215 |
| Strikes (in EUR)   | 1.1432 | 0.00927       | 1.5985 |
| Volatilities       | 10.5%  | 10.0%         | 7.5%   |
| Interest rates     | 4.0%   | 0.5%          | 7.0%   |
| BS-values (in EUR) | 235    | 227           | 233    |
| Basket value       | 563    |               |        |
| Sum of individuals | 695    |               |        |
|                    |        |               |        |

Comparison of a basket call with three currencies for a maturity of three months *versus* the cost of three individual call options

![](_page_2_Figure_13.jpeg)

**Figure 3** Premium of basket option versus premium of option strategy depending on the correlation

Surprisingly, this is just the case if a specific relation between the strike of the individual options and their volatilities is satisfied. The basket strike has to satisfy

$$K = a_1 \frac{K_1}{S_1(0)} + a_2 \frac{K_2}{S_2(0)}$$
 (11)

|         | GBP/USD (%) | USD/JPY (%) | GBP/JPY (%) | EUR/USD (%) | EUR/GBP (%) | EUR/JPY (%) |
|---------|-------------|-------------|-------------|-------------|-------------|-------------|
| GBP/USD | 100         | −47         | 42          | 71          | −19         | 27          |
| USD/JPY | −47         | 100         | 60          | −53         | −18         | 45          |
| GBP/JPY | 42          | 60          | 100         | 10          | −36         | 71          |
| EUR/USD | 71          | −53         | 10          | 100         | 55          | 52          |
| EUR/GBP | −19         | −18         | −36         | 55          | 100         | 40          |
| EUR/JPY | 27          | 45          | 71          | 52          | 40          | 100         |

**Table 2**

FX implied three-month correlation coefficients as of Nov 23, 2001

which leads to the natural choice

$$K_i = K \frac{S_i(0)}{a_1 + a_2} \tag{12}$$

Each strike *Ki* satisfies the above constraint by choosing

$$K_i = S_i(0)e^{(\mu_i + 1/2\sigma_i^2)T + \chi \sigma_i \sqrt{T}}$$
(13)

for some arbitrary, but common *χ* for all basket components.

# **Smile Adjustment**

For the pricing method, described there is no smile considered. Given the volatility smile for vanilla options, *σ*i*(K, T )*, with the same maturity as the basket option, the implied density *P* for each currency pair in the basket can be derived from vanilla prices *V* .

$$P(K,T) = e^{rT} \partial_{KK} V(K,\sigma_i(K,T)) \tag{14}$$

A mapping *ϕ(w)* can be derived that maps the Gaussian random numbers to smile-adjusted random numbers for each currency pair. The implicit construction solves the problem for the probability of the mapped Brownian to be the same as the smile-implied probability.

Using Monte Carlo simulation to price vanilla options using the mapping, it can be shown that in the limit, the derived prices are perfectly in line with the smile. The formula for the Monte Carlo simulation for a realization of a Brownian *w* is given by

$$S_i(0, w) = S_i(0)e^{(\mu_i + 1/2\sigma_i^2)T + \varphi(w)\sigma_i\sqrt{T}}$$
(15)

To price the basket option using the smile in Monte Carlo, a sequence of independent random numbers is used. These random numbers are correlated using the square-root matrix as above and these are fed into the individual mappings, hence generating the simulated spot at the basket maturity. Evaluating the payoff and averaging will generate a smile-adjusted price (see Table 4). Black–Scholes prices and smile-adjusted prices are shown next to each other for a direct comparison.

# **Conclusion**

Many corporate portfolios are exposed to multicurrency risk. One way to turn this fact into an advantage

| Table 4 |  |
|---------|--|
|         |  |

| Base currency              | EUR    |        |       |
|----------------------------|--------|--------|-------|
| Nominal in EUR             | 39 007 |        |       |
| Currencies                 | USD    | JPY    | GBP   |
| Nominals                   | 29%    | 30%    | 41%   |
| RR 25d                     | −0.25% | −4.30% | 1.10% |
| Fly 25d                    | 0.30%  | 0.17%  | 0.25% |
| BS-values (in EUR)         | 235    | 227    | 233   |
| Smile values (in EUR)      | 233    | 168    | 278   |
| Basket smile value         | 554    |        |       |
| Sum of individuals (smile) | 680    |        |       |
| Basket value               | 563    |        |       |
| Sum of individuals         | 695    |        |       |
|                            |        |        |       |

is to use multicurrency hedge instruments. We have shown that basket options are convenient instruments protecting against exchange rates of most of the basket components changing in the *same* direction. A rather unlikely market move of half of the currencies' exchange rates in *opposite* directions is not protected by basket options, but when taking this residual risk into account, the hedging cost is reduced substantially. The smile impact on the basket value can be calculated rather easily without referring to a specific model, because the product is path-independent.

# **End Notes**

a*.* This article is an extension of "Hakala, J. & Wystup, U. (2002) *Making the most out of Multiple Currency Exposure: Protection with Basket Options*, *The Euromoney Foreign Exchange and Treasury Management Handbook 2002* , Adrian Hornbrook."

# **References**

[1] Hakala, J. & Wystup, U. (2001). *Foreign Exchange Risk*, Risk Publications, London.

# **Further Reading**

Wystup, U. (2006). *FX Options and Structured Products*, Wiley.

# **Related Articles**

#### **Basket Options**.

JURGEN ¨ HAKALA & UWE WYSTUP
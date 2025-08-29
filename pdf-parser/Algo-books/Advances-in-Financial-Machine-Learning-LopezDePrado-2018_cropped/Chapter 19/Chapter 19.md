- 1. Easley, D., R. Engle, M. O'Hara, and L. Wu (2008): "Time-varying arrival rates of informed and uninformed traders." *Journal of Financial Econometrics* , Vol. 6, No. 2, pp. 171–207.
- 2. Easley, D., M. López de Prado, and M. O'Hara (2011): "The microstructure of the flash crash." *Journal of Portfolio Management* , Vol. 37, No. 2, pp. 118–128.
- 3. Easley, D., M. López de Prado, and M. O'Hara (2012c): "Optimal execution horizon." *Mathematical Finance* , Vol. 25, No. 3, pp. 640–672.
- 4. Gnedenko, B. and I. Yelnik (2016): "Minimum entropy as a measure of effective dimensionality." Working paper. Available at <https://ssrn.com/abstract=2767549.>

### **Note**

1 Alternatively, we could have worked with a vector of holdings, should the covariance matrix had been computed on price changes.

# **CHAPTER 19**

# **Microstructural Features**

### **19.1 Motivation**

Market microstructure studies "the process and outcomes of exchanging assets under explicit trading rules" (O'Hara [1995]). Microstructural datasets include primary information about the auctioning process, like order cancellations, double auction book, queues, partial fills, aggressor side, corrections, replacements, etc. The main source is Financial Information eXchange (FIX) messages, which can be purchased from exchanges. The level of detail contained in FIX messages provides researchers with the ability to understand how market participants conceal and reveal their intentions. That makes microstructural data one of the most important ingredients for building predictive ML features.

### **19.2 Review of the Literature**

The depth and complexity of market microstructure theories has evolved over time, as a function of the amount and variety of the data available. The first

generation of models used solely price information. The two foundational results from those early days are trade classification models (like the tick rule) and the Roll [1984] model. The second generation of models came after volume datasets started to become available, and researchers shifted their attention to study the impact that volume has on prices. Two examples for this generation of models are Kyle [1985] and Amihud [2002].

The third generation of models came after 1996, when Maureen O'Hara, David Easley, and others published their "probability of informed trading" (PIN) theory (Easley et al. [1996]). This constituted a major breakthrough, because PIN explained the bid-ask spread as the consequence of a sequential strategic decision between liquidity providers (market makers) and position takers (informed traders). Essentially, it illustrated that market makers were sellers of the option to be adversely selected by informed traders, and the bid-ask spread is the premium they charge for that option. Easley et al. [2012a, 2012b] explain how to estimate VPIN, a high-frequency estimate of PIN under volume-based sampling.

These are the main theoretical frameworks used by the microstructural literature. O'Hara [1995] and Hasbrouck [2007] offer a good compendium of low-frequency microstructural models. Easley et al. [2013] present a modern treatment of high-frequency microstructural models.

### **19.3 First Generation: Price Sequences**

The first generation of microstructural models concerned themselves with estimating the bid-ask spread and volatility as proxies for illiquidity. They did so with limited data and without imposing a strategic or sequential structure to the trading process.

## **19.3.1 The Tick Rule**

In a double auction book, quotes are placed for selling a security at various price levels (offers) or for buying a security at various price levels (bids). Offer prices always exceed bid prices, because otherwise there would be an instant match. A trade occurs whenever a buyer matches an offer, or a seller matches a bid. Every trade has a buyer and a seller, but only one side initiates the trade.

The tick rule is an algorithm used to determine a trade's aggressor side. A buyinitiated trade is labeled "1", and a sell-initiated trade is labeled "-1", according to this logic:

$$b_t = \begin{cases} 1 & \text{if } \Delta p_t > 0\\ -1 & \text{if } \Delta p_t < 0\\ b_{t-1} & \text{if } \Delta p_t = 0 \end{cases}$$

where *p <sup>t</sup>* is the price of the trade indexed by *t* = 1, …, *T* , and *b <sup>0</sup>* is arbitrarily set to 1. A number of studies have determined that the tick rule achieves high classification accuracy, despite its relative simplicity (Aitken and Frino [1996]). Competing classification methods include Lee and Ready [1991] and Easley et al. [2016].

Transformations of the { *b <sup>t</sup>* } series can result in informative features. Such transformations include: (1) Kalman Filters on its future expected value, E *<sup>t</sup>* [ *b <sup>t</sup> + 1* ]; (2) structural breaks on such predictions (Chapter 17), (3) entropy of the { *b <sup>t</sup>* } sequence (Chapter 18); (4) t-values from Wald-Wolfowitz's tests of runs on { *b <sup>t</sup>* }; (5) fractional differentiation of the cumulative { *b <sup>t</sup>* } series, (Chapter 5); etc.

#### 19.3.2 The Roll Model

Roll [1984] was one of the first models to propose an explanation for the effective bid-ask spread at which a security trades. This is useful in that bid-ask spreads are a function of liquidity, hence Roll's model can be seen as an early attempt to measure the liquidity of a security. Consider a mid-price series  $\{m_t\}$ }, where prices follow a Random Walk with no drift,

$$m_t = m_{t-1} + u_t$$

hence price changes  $\Delta m_t = m_t - m_{t-1}$  are independently and identically drawn from a Normal distribution

$$\Delta m_t \sim N \left[0, \sigma_u^2\right]$$

These assumptions are, of course, against all empirical observations, which suggest that financial time series have a drift, they are heteroscedastic, exhibit serial dependency, and their returns distribution is non-Normal. But with a proper sampling procedure, as we saw in Chapter 2, these assumptions may not be too unrealistic. The observed prices,  $\{p_t\}$ , are the result of sequential trading against the bid-ask spread:

$$p_t = m_t + b_t c$$

where *c* is half the bid-ask spread, and  $b_t \in \{-1, 1\}$  is the aggressor side. The Roll model assumes that buys and sells are equally likely,<br> $P[b_t = 1] = P[b_t = -1] = \frac{1}{2}$ , serially independent,  $E[b_t b_{t-1}] = 0$ , and independent from the noise,  $E[b_t u_t] = 0$ . Given these assumptions, Roll derives the values of *c* and  $\sigma^2_u$  as follows:

$$\sigma^{2} \left[ \Delta p_{t} \right] = \mathbb{E} \left[ \left( \Delta p_{t} \right)^{2} \right] - \left( \mathbb{E} \left[ \left( \Delta p_{t} \right) \right] \right)^{2} = 2c^{2} + \sigma_{u}^{2}$$
$$\sigma \left[ \Delta p_{t}, \Delta p_{t-1} \right] = -c^{2}$$

resulting in  $c = \sqrt{\max\{0, -\sigma[\Delta p_t, \Delta p_{t-1}]\}}$  and  $\sigma_u^2 = \sigma^2[\Delta p_t] + 2\sigma[\Delta p_t, \Delta p_t]$  $_{t-1}$ ]. In conclusion, the bid-ask spread is a function of the serial covariance of price changes, and the true (unobserved) price's noise, excluding

microstructural noise, is a function of the observed noise and the serial covariance of price changes.

The reader may question the need for Roll's model nowadays, when datasets include bid-ask prices at multiple book levels. One reason the Roll model is still in use, despite its limitations, is that it offers a relatively direct way to determine the *effective* bid-ask spread of securities that are either rarely traded, or where the published quotes are not representative of the levels at which market makers' are willing to provide liquidity (e.g., corporate, municipal, and agency bonds). Using Roll's estimates, we can derive informative features regarding the market's liquidity conditions.

### **19.3.3 High-Low Volatility Estimator**

Beckers [1983] shows that volatility estimators based on high-low prices are more accurate than the standard estimators of volatility based on closing prices. Parkinson [1980] derives that, for continuously observed prices following a geometric Brownian motion,

$$\begin{split} &\mathrm{E}\left[\frac{1}{T}\sum_{t=1}^{T}\left(\log\left[\frac{H_{t}}{L_{t}}\right]\right)^{2}\right] = k_{1}\sigma_{HL}^{2} \\ &\mathrm{E}\left[\frac{1}{T}\sum_{t=1}^{T}\left(\log\left[\frac{H_{t}}{L_{t}}\right]\right)\right] = k_{2}\sigma_{HL} \end{split}$$

where *k <sup>1</sup>* = 4log[2], , *H <sup>t</sup>* is the high price for bar *t* , and *L <sup>t</sup>* is the low price for bar *t.* Then the volatility feature σ *HL* can be robustly estimated based on observed high-low prices.

#### **19.3.4 Corwin and Schultz**

Building on the work of Beckers [1983], Corwin and Schultz [2012] introduce a bid-ask spread estimator from high and low prices. The estimator is based on two principles: First, high prices are almost always matched against the offer, and low prices are almost always matched against the bid. The ratio of high-tolow prices reflects fundamental volatility as well as the bid-ask spread. Second, the component of the high-to-low price ratio that is due to volatility increases proportionately with the time elapsed between two observations.

Corwin and Schultz show that the spread, as a percentage of price, can be estimated as

$$S_t = \frac{2(e^{\alpha_t} - 1)}{1 + e^{\alpha_t}}$$

where

$$\alpha_t = \frac{\sqrt{2\beta_t} - \sqrt{\beta_t}}{3 - 2\sqrt{2}} - \sqrt{\frac{\gamma_t}{3 - 2\sqrt{2}}}$$
$$\beta_t = \mathbb{E}\left[\sum_{j=0}^1 \left[\log\left(\frac{H_{t-j}}{L_{t-j}}\right)\right]^2\right]$$
$$\gamma_t = \left[\log\left(\frac{H_{t-1,t}}{L_{t-1,t}}\right)\right]^2$$

and *H <sup>t</sup> <sup>−</sup> 1, <sup>t</sup>* is the high price over 2 bars ( *t* − 1 and *t* ), whereas *L <sup>t</sup> <sup>−</sup> 1, <sup>t</sup>* is the low price over 2 bars ( *t* − 1 and *t* ). Because α *<sup>t</sup>* < 0⇒ *S <sup>t</sup>* < 0, the authors recommend setting negative alphas to 0 (see Corwin and Schultz [2012], p. 727). Snippet 19.1 implements this algorithm. The corwinSchultz function receives two arguments, a series dataframe with columns ( High , Low ), and an integer value sl that defines the sample length used to estimate β *<sup>t</sup>* .

#### **SNIPPET 19.1 IMPLEMENTATION OF THE CORWIN-SCHULTZ ALGORITHM**

```
<pre>def getBeta(series,sl):</pre>
    hl=series[['High','Low']].values
    hl = np.log(hl[:, 0]/hl[:, 1]) **2hl=pd.Series(hl,index=series.index)
    beta=pd.stats.moments.rolling sum(hl,window=2)
    <pre>beta=pd.stats.moments.rolling mean(beta,window=sl)</pre>
    return beta.dropna()
\#<pre>def getGamma(series):</pre>
    h2=pd.stats.moments.rolling max(series['High'],window=2)
    12=pd.stats.moments.rolling min(series['Low'],window=2)
    qamma = np.log(h2.values/12.values) **2\text{gamma} = \text{pd}.\text{Series}(\text{gamma}, \text{index} = \text{h2}.\text{index})return gamma.dropna()
#—
<pre>def getAlpha(beta,gamma):</pre>
    den = 3 - 2 \times 2 \times 5\alpha = (2^{**}.5-1) * (\beta * 0.5) / denalpha = (gamma/den) **.5alpha<0]=0 # set negative alphas to 0 (see p.727 of paper)
    return alpha.dropna()
#-
<pre>def corwinSchultz(series,sl=1):</pre>
    # Note: S<0
    beta = qetBeta (series, sl)
```

```
gamma=getGamma(series)
```

```
alpha=getAlpha(beta,gamma)
```

```
spread=2*(np.exp(alpha)-1)/(1+np.exp(alpha))
```

```
startTime=pd.Series(series.index[0:spread.shape[0]],index=spread.index)
spread=pd.concat([spread,startTime],axis=1)
```

```
spread.columns=['Spread','Start Time'] # 1st loc used to compute beta
return spread
```

Note that volatility does not appear in the final Corwin-Schultz equations. The reason is that volatility has been replaced by its high/low estimator. As a byproduct of this model, we can derive the Becker-Parkinson volatility as shown in Snippet 19.2.

#### **SNIPPET 19.2 ESTIMATING VOLATILITY FOR HIGH-LOW PRICES**

This procedure is particularly helpful in the corporate bond market, where there is no centralized order book, and trades occur through bids wanted in competition (BWIC). The resulting feature, bid-ask spread *S* , can be estimated recursively over a rolling window, and values can be smoothed using a Kalman filter.

# **19.4 Second Generation: Strategic Trade Models**

Second generation microstructural models focus on understanding and measuring illiquidity. Illiquidity is an important informative feature in financial ML models, because it is a risk that has an associated premium. These models have a stronger theoretical foundation than first-generation models, in that they explain trading as the strategic interaction between informed and uninformed traders. In doing so, they pay attention to signed volume and order flow imbalance.

Most of these features are estimated through regressions. In practice, I have observed that the t-values associated with these microstructural estimates are more informative than the (mean) estimates themselves. Although the literature does not mention this observation, there is a good argument for preferring features based on t-values over features based on mean values: t-values are rescaled by the standard deviation of the estimation error, which incorporates another dimension of information absent in mean estimates.

## 19.4.1 Kyle's Lambda

Kyle [1985] introduced the following strategic trade model. Consider a risky asset with terminal value  $v \sim N[p_0, \Sigma_0]$ , as well as two traders:

- A noise trader who trades a quantity  $u = N[0, \sigma^2]$ , independent of v.
- An informed trader who knows  $v$  and demands a quantity  $x$ , through a market order.

The market maker observes the total order flow  $y = x + u$ , and sets a price *p* accordingly. In this model, market makers cannot distinguish between orders from noise traders and informed traders. They adjust prices as a function of the order flow imbalance, as that may indicate the presence of an informed trader. Hence, there is a positive relationship between price change and order flow imbalance, which is called market impact.

The informed trader conjectures that the market maker has a linear price adjustment function,  $p = \lambda y + \mu$ , where  $\lambda$  is an inverse measure of liquidity. The informed trader's profits are  $\pi = (v - p)x$ , which are maximized at  $x = \frac{v-\mu}{2\lambda}$ , with second order condition  $\lambda > 0$ .

Conversely, the market maker conjectures that the informed trader's demand is a linear function of  $v: x = \alpha + \beta v$ , which implies  $\alpha = -\frac{\mu}{2\lambda}$  and  $\beta = \frac{1}{2\lambda}$ . Note that lower liquidity means higher  $\lambda$ , which means lower demand from the informed trader.

Kyle argues that the market maker must find an equilibrium between profit maximization and market efficiency, and that under the above linear functions, the only possible solution occurs when

$$\mu = p_0$$

$$\alpha = p_0 \sqrt{\frac{\sigma_u^2}{\Sigma_0}}$$

$$\lambda = \frac{1}{2} \sqrt{\frac{\Sigma_0}{\sigma_u^2}}$$
$$\beta = \sqrt{\frac{\sigma_u^2}{\Sigma_0}}$$

Finally, the informed trader's expected profit can be rewritten as

$$\mathrm{E}\left[\pi\right] = \frac{\left(v - p_{0}\right)^{2}}{2} \sqrt{\frac{\sigma_{u}^{2}}{\Sigma_{0}}} = \frac{1}{4\lambda} \left(v - p_{0}\right)^{2}$$

The implication is that the informed trader has three sources of profit:

- The security's mispricing.
- The variance of the noise trader's net order flow. The higher the noise, the easier the informed trader can conceal his intentions.
- The reciprocal of the terminal security's variance. The lower the volatility, the easier to monetize the mispricing.

In Kyle's model, the variable λ captures price impact. Illiquidity increases with uncertainty about *v* and decreases with the amount of noise. As a feature, it can be estimated by fitting the regression

$$\Delta p_t = \lambda \left( b_t V_t \right) + \varepsilon_t$$

where { *p <sup>t</sup>* } is the time series of prices, { *b <sup>t</sup>* } is the time series of aggressor flags, { *V <sup>t</sup>* } is the time series of traded volumes, and hence { *b <sup>t</sup> V <sup>t</sup>* } is the time series of signed volume or net order flow. Figure 19.1 plots the histogram of Kyle's lambdas estimated on the E-mini S&P 500 futures series.

![](_page_10_Figure_0.jpeg)

![](_page_10_Figure_1.jpeg)

#### **19.4.2 Amihud's Lambda**

Amihud [2002] studies the positive relationship between absolute returns and illiquidity. In particular, he computes the daily price response associated with one dollar of trading volume, and argues its value is a proxy of price impact. One possible implementation of this idea is

$$\left|\Delta\text{log}\left[\tilde{p}_{\tau}\right]\right| = \lambda \sum_{t \in B_{\tau}} \left(p_t V_t\right) + \varepsilon_{\tau}$$

where *B <sup>τ</sup>* is the set of trades included in bar τ, is the closing price of bar τ, and *p <sup>t</sup> V <sup>t</sup>* is the dollar volume involved in trade *t* ∈ *B <sup>τ</sup>* . Despite its apparent simplicity, Hasbrouck [2009] found that daily Amihud's lambda estimates exhibit a high rank correlation to intraday estimates of effective spread. Figure 19.2 plots the histogram of Amihud's lambdas estimated on the E-mini S&P 500 futures series.

![](_page_11_Figure_0.jpeg)

![](_page_11_Figure_1.jpeg)

#### **19.4.3 Hasbrouck's Lambda**

Hasbrouck [2009] follows up on Kyle's and Amihud's ideas, and applies them to estimating the price impact coefficient based on trade-and-quote (TAQ) data. He uses a Gibbs sampler to produce a Bayesian estimation of the regression specification

$$\log\left[\tilde{p}_{i,\tau}\right] - \log\left[\tilde{p}_{i,\tau-1}\right] = \lambda_i \sum_{t \in B_{i,\tau}} \left(b_{i,t} \sqrt{p_{i,t} V_{i,t}}\right) + \epsilon_{i,\tau}$$

where *B <sup>i</sup> , <sup>τ</sup>* is the set of trades included in bar τ for security *i* , with *i* = 1, …, *I* , is the closing price of bar τ for security *i* , *b <sup>i</sup> , <sup>t</sup>* ∈ { − 1, 1} indicates whether trade *t* ∈ *B <sup>i</sup> , <sup>τ</sup>* was buy-initiated or sell-initiated; and *p <sup>i</sup> , <sup>t</sup> V <sup>i</sup> , <sup>t</sup>* is the dollar volume involved in trade *t* ∈ *B <sup>i</sup> , <sup>τ</sup>* . We can then estimate λ *<sup>i</sup>* for every security *i* , and use it as a feature that approximates the effective cost of trading (market impact).

<span id="page-12-1"></span>Consistent with most of the literature, Hasbrouck recommends 5-minute timebars for sampling ticks. However, for the reasons discussed in Chapter 2, better results can be achieved through stochastic sampling methods that are synchronized with market activity. [Figure 19.3](#page-12-0) plots the histogram of Hasbrouck's lambdas estimated on the E-mini S&P 500 futures series.

![](_page_12_Figure_1.jpeg)

<span id="page-12-0"></span>**[Figure 19.3](#page-12-1)** Hasbrouck's lambdas estimated on E-mini S&P 500 futures

### **19.5 Third Generation: Sequential Trade Models**

As we have seen in the previous section, strategic trade models feature a single informed trader who can trade at multiple times. In this section we will discuss an alternative kind of model, where randomly selected traders arrive at the market sequentially and independently.

Since their appearance, sequential trade models have become very popular among market makers. One reason is, they incorporate the sources of uncertainty faced by liquidity providers, namely the probability that an informational event has taken place, the probability that such event is negative, the arrival rate of noise traders, and the arrival rate of informed traders. With those variables, market makers must update quotes dynamically, and manage their inventories.

#### **19.5.1 Probability of Information-based Trading**

Easley et al. [1996] use trade data to determine the probability of informationbased trading (PIN) of individual securities. This microstructure model views trading as a game between market makers and position takers that is repeated over multiple trading periods.

Denote a security's price as *S* , with present value *S <sup>0</sup>* . However, once a certain amount of new information has been incorporated into the price, *S* will be either *S <sup>B</sup>* (bad news) or *S <sup>G</sup>* (good news). There is a probability α that new information will arrive within the timeframe of the analysis, a probability δ that the news will be bad, and a probability (1 − δ) that the news will be good. These authors prove that the expected value of the security's price can then be computed at time *t* as

$$\mathbf{E}\left[S_{t}\right]=\left(1-\alpha_{t}\right)S_{0}+\alpha_{t}\left[\delta_{t}S_{B}+\left(1-\delta_{t}\right)S_{G}\right]$$

Following a Poisson distribution, informed traders arrive at a rate μ, and uninformed traders arrive at a rate ε. Then, in order to avoid losses from informed traders, market makers reach breakeven at a bid level *B <sup>t</sup>* ,

$$\mathbf{E}\left[B_{t}\right] = \mathbf{E}\left[S_{t}\right] - \frac{\mu\alpha_{t}\delta_{t}}{\varepsilon + \mu\alpha_{t}\delta_{t}}\left(\mathbf{E}\left[S_{t}\right] - S_{B}\right)$$

and the breakeven ask level *A <sup>t</sup>* at time *t* must be,

$$\mathrm{E}\left[A_{t}\right] = \mathrm{E}\left[S_{t}\right] + \frac{\mu\alpha_{t}\left(1-\delta_{t}\right)}{\varepsilon + \mu\alpha_{t}\left(1-\delta_{t}\right)}\left(S_{G} - \mathrm{E}\left[S_{t}\right]\right)$$

It follows that the breakeven bid-ask spread is determined as

$$\mathbf{E}\left[A_{t}-B_{t}\right] = \frac{\mu\alpha_{t}\left(1-\delta_{t}\right)}{\varepsilon+\mu\alpha_{t}\left(1-\delta_{t}\right)}\left(S_{G}-\mathbf{E}\left[S_{t}\right]\right) + \frac{\mu\alpha_{t}\delta_{t}}{\varepsilon+\mu\alpha_{t}\delta_{t}}\left(\mathbf{E}\left[S_{t}\right]-S_{B}\right)$$

For the standard case when , we obtain

$$\delta_t = \frac{1}{2} \Rightarrow \mathbf{E} \left[ A_t - B_t \right] = \frac{\alpha_t \mu}{\alpha_t \mu + 2\varepsilon} \left( S_G - S_B \right)$$

This equation tells us that the critical factor that determines the price range at which market makers provide liquidity is

$$PIN_t = \frac{\alpha_t \mu}{\alpha_t \mu + 2\varepsilon}$$

The subscript *t* indicates that the probabilities α and δ are estimated at that point in time. The authors apply a Bayesian updating process to incorporate information after each trade arrives to the market.

In order to determine the value *PIN <sup>t</sup>* , we must estimate four non-observable parameters, namely {α, δ, μ, ε}. A maximum-likelihood approach is to fit a mixture of three Poisson distributions,

$$\begin{split} \mathbf{P}[V^B, V^S] &= (1 - \alpha) \mathbf{P}[V^B, \varepsilon] \mathbf{P}[V^S, \varepsilon] \\ &+ \alpha (\delta \mathbf{P}[V^B, \varepsilon] \mathbf{P}[V^S, \mu + \varepsilon] + (1 - \delta) \mathbf{P}[V^B, \mu + \varepsilon] \mathbf{P}[V^S, \varepsilon]) \end{split}$$

where *V B* is the volume traded against the ask (buy-initiated trades), and *V S* is the volume traded against the bid (sell-initiated trades).

#### **19.5.2 Volume-Synchronized Probability of Informed Trading**

Easley et al. [2008] proved that

$$\begin{split} \mathrm{E}\left[V^B - V^S\right] &= (1-\alpha)(\varepsilon - \varepsilon) + \alpha\left(1-\delta\right)(\varepsilon - (\mu+\varepsilon)) + \alpha\delta\left(\mu+\varepsilon-\varepsilon\right) \\ &= \alpha\mu\left(1-2\delta\right) \end{split}$$

and in particular, for a sufficiently large μ,

$$\mathrm{E}[|V^B - V^S|] \approx \alpha \mu$$

Easley et al. [2011] proposed a high-frequency estimate of PIN, which they named volume-synchronized probability of informed trading (VPIN). This

procedure adopts a *volume clock* , which synchronizes the data sampling with market activity, as captured by volume (see Chapter 2). We can then estimate

$$\frac{1}{n} \sum_{\tau=1}^{n} \left| V_{\tau}^{B} - V_{\tau}^{S} \right| \approx \alpha \mu$$

where *V B τ* is the sum of volumes from buy-initiated trades within volume bar τ, *V S τ* is the sum of volumes from sell-initiated trades within volume bar τ, and *n* is the number of bars used to produce this estimate. Because all volume bars are of the same size, *V* , we know that by construction

$$\frac{1}{n}\sum_{\tau=1}^{n}\left(V_{\tau}^{B}+V_{\tau}^{S}\right)=V=\alpha\mu+2\varepsilon$$

Hence, PIN can be estimated in high-frequency as

$$VPIN_{\tau} = \frac{\sum_{\tau=1}^{n} |V_{\tau}^{B} - V_{\tau}^{S}|}{\sum_{\tau=1}^{n} (V_{\tau}^{B} + V_{\tau}^{S})} = \frac{\sum_{\tau=1}^{n} |V_{\tau}^{B} - V_{\tau}^{S}|}{nV}$$

For additional details and case studies of VPIN, see Easley et al. [2013]. Using linear regressions, Andersen and Bondarenko [2013] concluded that VPIN is not a good predictor of volatility. However, a number of studies have found that VPIN indeed has predictive power: Abad and Yague [2012], Bethel et al. [2012], Cheung et al. [2015], Kim et al. [2014], Song et al. [2014], Van Ness et al. [2017], and Wei et al. [2013], to cite a few. In any case, linear regression is a technique that was already known to 18th-century mathematicians (Stigler [1981]), and economists should not be surprised when it fails to recognize complex non-linear patterns in 21st-century financial markets.

#### **19.6 Additional Features from Microstructural Datasets**

The features we have studied in Sections 19.3 to 19.5 were suggested by market microstructure theory. In addition, we should consider alternative features that, although not suggested by the theory, we suspect carry important information about the way market participants operate, and their future intentions. In doing so, we will harness the power of ML algorithms, which can learn how to use these features without being specifically directed by theory.

## **19.6.1 Distibution of Order Sizes**

Easley et al. [2016] study the frequency of trades per trade size, and find that trades with round sizes are abnormally frequent. For example, the frequency rates quickly decay as a function of trade size, with the exception of round trade sizes {5, 10, 20, 25, 50, 100, 200, …}. These authors attribute this phenomenon to so-called "mouse" or "GUI" traders, that is, human traders who send orders by clicking buttons on a GUI (Graphical User Interface). In the case of the E-mini S&P 500, for example, size 10 is 2.9 times more frequent than size 9; size 50 is 10.9 times more likely than size 49; size 100 is 16.8 times more frequent than size 99; size 200 is 27.2 times more likely than size 199; size 250 is 32.5 times more frequent than size 249; size 500 is 57.1 times more frequent than size 499. Such patterns are not typical of "silicon traders," who usually are programmed to randomize trades to disguise their footprint in markets.

A useful feature may be to determine the normal frequency of round-sized trades, and monitor deviations from that expected value. The ML algorithm could, for example, determine if a larger-than-usual proportion of round-sized trades is associated with trends, as human traders tend to bet with a fundamental view, belief, or conviction. Conversely, a lower-than-usual proportion of round-sized trades may increase the likelihood that prices will move sideways, as silicon traders do not typically hold long-term views.

## **19.6.2 Cancellation Rates, Limit Orders, Market Orders**

Eisler et al. [2012] study the impact of market orders, limit orders, and quote cancellations. These authors find that small stocks respond differently than large stocks to these events. They conclude that measuring these magnitudes is relevant to model the dynamics of the bid-ask spread.

Easley et al. [2012] also argue that large quote cancellation rates may be indicative of low liquidity, as participants are publishing quotes that do not intend to get filled. They discuss four categories of predatory algorithms:

**Quote stuffers:** They engage in "latency arbitrage." Their strategy involves overwhelming an exchange with messages, with the sole intention of slowing down competing algorithms, which are forced to parse messages that only the originators know can be ignored.

- **Quote danglers:** This strategy sends quotes that force a squeezed trader to chase a price against her interests. O'Hara [2011] presents evidence of their disruptive activities.
- **Liquidity squeezers:** When a distressed large investor is forced to unwind her position, predatory algorithms trade in the same direction, draining as much liquidity as possible. As a result, prices overshoot and they make a profit (Carlin et al. [2007]).
- **Pack hunters:** Predators hunting independently become aware of one another's activities, and form a pack in order to maximize the chances of triggering a cascading effect (Donefer [2010], Fabozzi et al. [2011], Jarrow and Protter [2011]). NANEX [2011] shows what appears to be pack hunters forcing a stop loss. Although their individual actions are too small to raise the regulator's suspicion, their collective action may be market-manipulative. When that is the case, it is very hard to prove their collusion, since they coordinate in a decentralized, spontaneous manner.

These predatory algorithms utilize quote cancellations and various order types in an attempt to adversely select market makers. They leave different signatures in the trading record, and measuring the rates of quote cancellation, limit orders, and market orders can be the basis for useful features, informative of their intentions.

# **19.6.3 Time-Weighted Average Price Execution Algorithms**

Easley et al. [2012] demonstrate how to recognize the presence of execution algorithms that target a particular time-weighted average price (TWAP). A TWAP algorithm is an algorithm that slices a large order into small ones, which are submitted at regular time intervals, in an attempt to achieve a pre-defined time-weighted average price. These authors take a sample of E-mini S&P 500 futures trades between November 7, 2010, and November 7, 2011. They divide the day into 24 hours, and for every hour, they add the volume traded at each second, irrespective of the minute. Then they plot these aggregate volumes as a surface where the x-axis is assigned to volume per second, the y-axis is assigned to hour of the day, and the z-axis is assigned to the aggregate volume. This analysis allows us to see the distribution of volume within each minute as the day passes, and search for low-frequency traders executing their massive orders on a chronological time-space. The largest concentrations of volume within a minute tend to occur during the first few seconds, for almost every hour of the day. This is particularly true at 00:00–01:00 GMT (around the open

of Asian markets), 05:00–09:00 GMT (around the open of U.K. and European equities), 13:00–15:00 GMT (around the open of U.S. equities), and 20:00– 21:00 GMT (around the close of U.S. equities).

A useful ML feature may be to evaluate the order imbalance at the beginning of every minute, and determine whether there is a persistent component. This can then be used to front-run large institutional investors, while the larger portion of their TWAP order is still pending.

# **19.6.4 Options Markets**

Muravyev et al. [2013] use microstructural information from U.S. stocks and options to study events where the two markets disagree. They characterize such disagreement by deriving the underlying bid-ask range implied by the put-call parity quotes and comparing it to the actual bid-ask range of the stock. They conclude that disagreements tend to be resolved in favor of stock quotes, meaning that option *quotes* do not contain economically significant information. At the same time, they do find that option *trades* contain information not included in the stock price. These findings will not come as a surprise to portfolio managers used to trade relatively illiquid products, including stock options. Quotes can remain irrational for prolonged periods of time, even as sparse prices are informative.

Cremers and Weinbaum [2010] find that stocks with relatively expensive calls (stocks with both a high volatility spread and a high change in the volatility spread) outperform stocks with relatively expensive puts (stocks with both a low volatility spread and a low change in the volatility spread) by 50 basis points per week. This degree of predictability is larger when option liquidity is high and stock liquidity is low.

In line with these observations, useful features can be extracted from computing the put-call implied stock price, derived from option trades. Futures prices only represent mean or expected future values. But option prices allow us to derive the entire distribution of outcomes being priced. An ML algorithm can search for patterns across the Greek letters quoted at various strikes and expiration dates.

# **19.6.5 Serial Correlation of Signed Order Flow**

Toth et al. [2011] study the signed order flow of London Stock Exchange stocks, and find that order signs are positively autocorrelated for many days. They attribute this observation to two candidate explanations: Herding and order splitting. They conclude that on timescales of less than a few hours, the persistence of order flow is overwhelmingly due to splitting rather than herding.

Given that market microstructure theory attributes the persistency of order flow imbalance to the presence of informed traders, it makes sense to measure the strength of such persistency through the serial correlation of the signed volumes. Such a feature would be complementary to the features we studied in Section 19.5.

## **19.7 What Is Microstructural Information?**

Let me conclude this chapter by addressing what I consider to be a major flaw in the market microstructure literature. Most articles and books on this subject study asymmetric information, and how strategic agents utilize it to profit from market makers. But how is information exactly defined in the context of trading? Unfortunately, there is no widely accepted definition of information in a microstructural sense, and the literature uses this concept in a surprisingly loose, rather informal way (López de Prado [2017]). This section proposes a proper definition of information, founded on signal processing, that can be applied to microstructural studies.

Consider a features matrix *X* = { *X <sup>t</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* that contains information typically used by market makers to determine whether they should provide liquidity at a particular level, or cancel their passive quotes. For example, the columns could be all of the features discussed in this chapter, like VPIN, Kyle's lambda, cancellation rates, etc. Matrix *X* has one row for each decision point. For example, a market maker may reconsider the decision to either provide liquidity or pull out of the market every time 10,000 contracts are traded, or whenever there is a significant change in prices (recall sampling methods in Chapter 2), etc. First, we derive an array *y* = { *y <sup>t</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* that assigns a label 1 to an observation that resulted in a market-making profit, and labels as 0 an observation that resulted in a market-making loss (see Chapter 3 for labeling methods). Second, we fit a classifier on the training set ( *X* , *y* ). Third, as new out-of-sample observations arrive τ > *T* , we use the fit classifier to predict the label . Fourth, we derive the cross-entropy loss of these

predictions, *L <sup>τ</sup>* , as described in Chapter 9, Section 9.4. Fifth, we fit a kernel density estimator (KDE) on the array of negative cross-entropy losses, { − *L <sup>t</sup>* } *t* = *T* + 1, …, τ , to derive its cumulative distribution function, *F.* Sixth, we estimate the microstructural information at time *t* as φ <sup>τ</sup> = *F* [ − *L <sup>τ</sup>* ], where φ <sup>τ</sup> ∈ (0, 1).

This microstructural information can be understood as the complexity faced by market makers' decision models. Under normal market conditions, market makers produce *informed forecasts* with low cross-entropy loss, and are able to profit from providing liquidity to position takers. However, in the presence of (asymmetrically) informed traders, market makers produce *uninformed forecasts* , as measured by high cross-entropy loss, and they are adversely selected. In other words, microstructural information can only be defined and measured relative to the predictive power of market makers. The implication is that {φ <sup>τ</sup> } should become an important feature in your financial ML toolkit.

Consider the events of the flash crash of May 6, 2010. Market makers wrongly predicted that their passive quotes sitting on the bid could be filled and sold back at a higher level. The crash was not caused by a single inaccurate prediction, but by the accumulation of thousands of prediction errors (Easley et al. [2011]). If market makers had monitored the rising cross-entropy loss of their predictions, they would have recognized the presence of informed traders and the dangerously rising probability of adverse selection. That would have allowed them to widen the bid-ask spread to levels that would have stopped the order flow imbalance, as sellers would no longer have been willing to sell at those discounts. Instead, market makers kept providing liquidity to sellers at exceedingly generous levels, until eventually they were forced to stop-out, triggering a liquidity crisis that shocked markets, regulators, and academics for months and years.

#### **Exercises**

- 1. From a time series of E-mini S&P 500 futures tick data,
  - 1. Apply the tick rule to derive the series of trade signs.
  - 2. Compare to the aggressor's side, as provided by the CME (FIX tag 5797). What is the accuracy of the tick rule?
  - 3. Select the cases where FIX tag 5797 disagrees with the tick rule.
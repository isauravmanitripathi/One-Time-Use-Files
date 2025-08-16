# **Risk Premia**

Risk premia are the expected excess returns that compensate investors for taking on aggregate risk. The first section of this article defines risk premia analytically. The second section surveys empirical evidence on equity, bond, and currency excess returns. The third section reviews the models that explain these risk premia.

# **Theoretical Definition**

Risk premia are derived analytically from Euler equations that link returns to stochastic discount factors (SDFs). These Euler equations can be derived under three different assumptions: complete markets. the law of one price, or the existence of investors' preferences. These three assumptions are reviewed here, followed by the analytical definition of risk premia.

#### *Euler Equations*

Utility-based Asset Pricing. Assume that the investor derives some utility  $u$  from consumption  $C$ now and in the next period. This setup can be easily generalized to many periods. Let us find the price  $P_t$ at time t of a payoff  $X_{t+1}$  at time  $t + 1$ . Let Q be the original consumption level in the absence of any asset purchase and let  $\xi$  be the amount of the asset the investor chooses to buy. The constant subjective discount factor is  $\beta$ . The maximization problem of this investor is

$$\text{Max}_{\xi} \quad u(C_t) + E_t[\beta u(C_{t+1})]$$

subject to:  $C_t = Q_t - P_t \xi$ ,

$$C_{t+1} = Q_{t+1} + X_{t+1}\xi \tag{1}$$

Substituting the constraints into the objective and setting the derivative with respect to  $\xi$  to zero yields

$$P_t u'(C_t) = E_t[\beta u'(C_{t+1})X_{t+1}] \tag{2}$$

where  $P_t u'(C_t)$  is the loss in utility if the investor buys another unit of the asset, and  $E_t[\beta u'(C_{t+1})X_{t+1}]$ is the expected and discounted increase in utility he/she obtains from the extra payoff  $X_{t+1}$ . The

investor continues to buy or sell the asset until the marginal loss equals the marginal gain. The Euler equation is thus

$$P_{t} = E_{t} \left[ \beta \frac{u'(C_{t+1})}{u'(C_{t})} X_{t+1} \right] = E_{t} [M_{t+1} X_{t+1}] \quad (3)$$

where the SDF  $M_{t+1}$  is defined as  $M_{t+1} \equiv \beta u'$  $(C_{t+1})/u'(C_t).$ 

Complete Markets. Let us now abstract from utilities and assume that markets are *complete*. There are  $S$  states of nature tomorrow, and  $s$  denotes an individual state. A contingent claim is a security that pays one dollar (or one unit of the consumption good) in one state  $s$  only tomorrow. The price today of this contingent claim is  $P_c(s)$ . In complete markets, investors can buy any contingent claim (or synthesize all contingent claims). Let  $X$  be the payoff space and  $X(s) \in X$  denote an asset's payoff in state of nature s. Let  $\pi(s)$  be the probability that state s occurs. Then the price of this asset is

$$P(X) = \sum_{s=1}^{S} P_c(s)X(s) = \sum_{s=1}^{S} \pi(s) \frac{P_c(s)}{\pi(s)} X(s) \quad (4)$$

We define  $M$  as the ratio of the contingent claim's price to the corresponding state's probability  $M(s) \equiv$  $P_c(s)/\pi(s)$  to obtain the Euler equation in complete markets:

$$P(X) = \sum_{s=1}^{S} \pi(s)M(s)X(s) = E(MX) \qquad (5)$$

Law of One Price and the Absence of Arbitrage. Finally, assume now that markets are *incomplete* and that we simply observe a set of prices  $P$  and payoffs  $X$ . Under a minimal set of assumptions, some discount factor exists that represents the observed prices by the same equation  $P = E(MX)$ . These assumptions are defined below:

**Definition 1** *Free portfolio formation:*  $X_1, X_2 \in$  $\underline{X} \Rightarrow aX_1 + bX_2 \in \underline{X}$  for any real a and b.

**Definition 2** Law of one price:  $P(aX_1 + bX_2) =$  $aP(X_1) + bP(X_2)$ .

Note that free portfolio formation rules out short sales constraints, bid/ask spreads, leverage limitations, and so on. The law of one price says that investors cannot make instantaneous profits by repackaging portfolios. These assumptions lead to the following theorem:

**Theorem 1** *Given free portfolio formation and the* law of one price, there exists a unique payoff  $X^{\star} \in X$ such that  $P(X) = E(X^*X)$  for all  $X \in X$ .

As a result, there exists an SDF  $M$  such that  $P(X) = E(MX)$ . Note that the existence of a discount factor implies the law of one price  $E[M(X +$  $Y$ ] =  $E[MX] + E[MY]$ . The theorem reverses this logic. Cochrane [7] offers a geometric and an arithmetic proof. With a stronger assumption, the absence of arbitrage, the SDF is strictly positive and thus represents some-potentially unknown-preferences. Let us first review the definition of the absence of arbitrage and then turn to this new theorem.

**Definition 3** Absence of arbitrage: A payoff space  $\underline{X}$  and pricing function  $P(X)$  leave no arbitrage  $\textit{opportunities if every payoff } X \textit{ that is always nonneg-}$ *ative* ( $X \ge 0$  *almost surely) and strictly positive* ( $X >$ 0) with some positive probability has some strictly *positive price*  $P(X) > 0$ .

In other words, no arbitrage says that one cannot get for free a portfolio that might pay off positively but will certainly never cost one anything. This assumption leads to the next theorem:

**Theorem 2** No arbitrage and the law of one price imply the existence of a strictly positive discount factor  $M > 0$  such that  $P = E(MX)$ ,  $\forall X \in \underline{X}$ .

We have seen three ways to derive the Euler equation that links any asset's price to the SDF. Before we exploit the Euler equation to define risk premia, note that only aggregate risk matters for asset prices.

Aggregate and Idiosyncratic Risk. Only the component of payoffs that is correlated with the SDF shows up in the asset's price. Idiosyncratic risk, uncorrelated with the SDF, generates no premium. To see this, let us project  $X$  on  $M$  and decompose the payoff as follows:

$$X = \text{proj}(X|M) + \varepsilon \tag{6}$$

Projecting  $X$  on  $M$  is like regressing  $X$  on  $M$  without a constant:

$$\text{proj}(X|M) = \frac{E(MX)}{E(M^2)}M\tag{7}$$

The residuals  $\varepsilon$  are orthogonal to the right-hand side variable M:  $E(M\varepsilon) = 0$ , which means that the price of  $\varepsilon$  is zero. The price of the projection of X on M is the price of  $X$ :

$$P(proj(X|M)) = E\left(M\frac{E(MX)}{E(M^2)}M\right) = E(MX)$$
(8)

Payoffs and Returns. We have reviewed three frameworks that lead to the Euler equation. This equation defines the asset price  $P$  for any asset. For stocks, the payoff  $X_{t+1}$  is the price next period  $P_{t+1}$ and the dividend  $D_{t+1}$ . For a one-period bond, the payoff is 1: one buys a bond at price  $P_t$  and receive 1 dollar next period. Alternatively, we can write the Euler equation in terms of returns. For stocks, returns are payoffs divided by prices:  $R_{t+1} = X_{t+1}/P_{t+1}$ . For bonds, one pays 1 dollar today and receives  $R_{t+1}$ dollars tomorrow. In any case, the Euler equation in terms of returns is thus

$$E_t[M_{t+1}R_{t+1}] = 1 \tag{9}$$

The Euler equation naturally applies to a risk-free asset. If one pays 1 dollar today and receives  $R_t^f$ dollars tomorrow for sure, the risk-free rate  $R_t^f$ satisfies

$$R_t^f = 1/E_t[M_{t+1}] \t\t(10)$$

## Expected Excess Returns

Definition of Risk Premia. Applying the definition of the covariance to the Euler equation (9) for the asset return  $R^i$  leads to  $E_t(M_{t+1})E_t(R_{t+1}^i)$  +  $\text{cov}_{t}[M_{t+1}, R_{t+1}^{i}] = 1.$  Using the definition of the risk-free rate in equation  $(10)$ , we obtain

$$E_t(R_{t+1}^i) - R_t^f = -R_t^f cov_t[M_{t+1}, R_{t+1}^i] \qquad (11)$$

The left-hand side of equation (11) defines the expected excess return. The right-hand side of equation (11) defines the risk premium. When the asset return  $R^i$  is negatively correlated to the SDF, the investor expects a positive excess return on asset  $i$ . All assets have an expected return equal to the risk-free rate, plus a risk adjustment that is positive or negative.

To gain some intuition on the definition above. let us consider the case of preference-based SDFs. Assume that utility increases, and marginal utility decreases with consumption; this is the consumptioncapital asset pricing model (consumption-CAPM). Here, the SDF—also known as *intertemporal margi*nal rate of substitution—is the ratio of marginal utility of consumption tomorrow divided by the marginal utility of consumption today. Substituting the SDF into equation  $(11)$ , we obtain

$$E_t(R_{t+1}^i) - R_t^f = -R_t^f \frac{\text{Cov}_t[\beta u'(C_{t+1}), R_{t+1}^i]}{u'(C_t)}$$
(12)

Marginal utility  $u'(C)$  declines as consumption C rises. Thus, an asset's expected excess return is positive if its return covaries positively with consumption. The reason for this is can be explained as follows. Our assumption on the investors' utility function implies that investors dislike uncertainty about consumption. An asset whose return covaries positively with consumption pays off well when the investor is already feeling wealthy and it pays off badly when he/she is already feeling poor. Thus, such an asset will make the investor's consumption stream more volatile. As a result, assets whose returns covary positively with consumption make consumption more volatile, and so must promise higher expected returns to induce investors to hold them.

Beta-representation and Market Price of Risk. We can rewrite the right-hand side of equation  $(11)$  as

$$\underbrace{\left(-\frac{\text{Cov}_{t}[M_{t+1}, R_{t+1}^{i}]}{\text{Var}_{t}[M_{t+1}]}\right)}_{\beta_{i,M}} \underbrace{\left(\frac{\text{Var}_{t}[M_{t+1}]}{E_{t}[M_{t+1}]}\right)}_{\lambda_{M}} \tag{13}$$

 $E(R_{t+1}^i) - R_t^f = \beta_{i,M} \lambda_M$  is then a beta-representation of the Euler equation. Note that  $\lambda_M$  is independent of the asset *i*. It is called the *market price of risk*.  $\beta_{i,M}$ is the quantity of risk. The expected excess return on asset  $i$  is equal to the quantity of risk of this asset times the price of risk.

Euler Equation with Log Returns and Log SDF. To interpret risk premia, it is often easier to rewrite the previous results in terms of the log SDF  $m_{t+1}$  and log return  $r_{t+1}^i$ . Assuming that SDF and returns are  $lognormal$ , equation (9) leads to

$$E_t(m_{t+1}) + E_t(r_{t+1}^i) + \frac{1}{2} \text{Var}_t(m_{t+1})$$
  
+ 
$$\frac{1}{2} \text{Var}_t(r_{t+1}^i) + \text{Cov}_t(m_{t+1}, r_{t+1}^i) = 0 \qquad (14)$$

where lowercase letters denote logs. The same equation holds for the risk-free rate  $r_t^f$ . Let  $\tilde{r}_{t+1}^{e,i}$  be the excess return corrected for the Jensen term:  $\tilde{r}_{t+1}^{e,i} = r_{t+1}^i - r_t^f + \frac{1}{2} \text{Var}_t(r_{t+1}^i)$ . Then, the expected log excess return is equal to

$$E_t(\tilde{r}_{t+1}^{e,i}) = -\text{Cov}_t(m_{t+1}, \tilde{r}_{t+1}^{e,i}) \tag{15}$$

For the consumption-CAPM, the utility each period is  $u(C) = C^{1-\gamma}/(1-\gamma)$ . The log SDF depends only on consumption growth and is equal to  $m_{t+1} = \log \beta - \gamma g - \gamma (\Delta c_{t+1} - g)$ , where g is the average consumption growth. In this case, the expected excess return is equal to

$$E_t(\tilde{r}_{t+1}^{e,i}) = \gamma \operatorname{Cov}_t(\Delta c_{t+1} - g, \tilde{r}_{t+1}^{e,i}) \qquad (16)$$

Again, assets whose returns covary positively with consumption must promise positive expected returns to induce investors to hold them.

## **Empirical Evidence**

Now the empirical stylized facts on risk premia are discussed. A large literature shows that, in many asset markets, expected excess returns are sizable and timevarying. The equity, bond, and currency markets are considered (see Predictability of Asset Prices).

#### Stock Markets

Evidence of large risk premia abound on equity markets. The size of the average excess return on the stock market is actually puzzling from a consumption-based asset pricing perspective; it constitutes the equity premium puzzle. Moreover, expected equity returns appear time-varying.

**Equity Premium Puzzle.** To understand the equity premium puzzle, let us first define the Sharpe ratio.

**Definition 4** The Sharpe ratio SR measures how much return the investor receives per unit of volatility:

$$SR = \frac{E(R^i) - R^f}{\sigma(R^i)}\tag{17}$$

where  $\sigma(R^i)$  denotes the standard deviation of the return  $R^i$ .

Over the period 1927–2006 in the United States, real excess returns on the New York Stock Exchange (NYSE) stock index have averaged 8%, with a standard deviation of 20%, and thus the Sharpe ratio has been about  $0.4$ . Starting from equation (11) and using the fact that correlations are below unity, the Sharpe ratio is linked to the first and second moments of SDFs:

$$\left| \frac{E(R^{i}) - R^{f}}{\sigma(R^{i})} \right| \leq \left| \frac{\sigma(M)}{E(M)} \right| \tag{18}$$

Now, recall the consumption-CAPM and assume that consumption is lognormal. Then, the right-hand side is approximately

$$\frac{\sigma(M)}{E(M)} = \sqrt{e^{\gamma^2 \sigma_{\Delta c}^2} - 1} \approx \gamma \sigma_{\Delta c} \tag{19}$$

Aggregate nondurable and services consumption growth has a mean of 2% and a standard deviation of 1%, implying a risk-aversion coefficient of 40! If we take into account the low correlation between consumption growth rates and market returns, the implied risk aversion is even higher. This is the equity premium puzzle of Mehra and Prescott [16]. Such a high risk-aversion coefficient implies implausibly high risk-free rates. This is the risk-free rate puzzle of Weil [19]. The abovementioned evidence is based on *realized* excess returns. Yet similar results are obtained with expected excess returns, which turn out to be large and time-varying.

Time-varying Expected Excess Returns. The Campbell and Shiller [5] decomposition of stock returns frames the evidence on stock market predictability. To see this, start from  $1 = R_{t+1}^{-1}R_{t+1} =$  $R_{t+1}^{-1}(P_{t+1}+D_{t+1})/P_t$ , and multiply both sides by the price-dividend ratio  $P_t/D_t$  to obtain

$$\frac{P_t}{D_t} = R_{t+1}^{-1} \left( 1 + \frac{P_{t+1}}{D_{t+1}} \right) \frac{D_{t+1}}{D_t} \tag{20}$$

Taking logs leads to

$$p_t - d_t = -r_{t+1} + \Delta d_{t+1} + \log(1 + e^{p_{t+1} - d_{t+1}})$$
(21)

A first-order Taylor approximation of the last term around the mean price-dividend ratio  $P/D$  gives

$$p_t - d_t = -r_{t+1} + \Delta d_{t+1} + k + \rho (p_{t+1} - d_{t+1})$$
(22)

where  $k = \log(1 + P/D)$  and  $\rho = (P/D)/(1 + P/D)$  $P/D$ ). Iterating forward and assuming that  $\lim_{i\to\infty} \rho^j(p_{t+i}-d_{t+i})=0$ , one obtains

$$p_t - d_t = \text{Constant} + \sum_{j=1}^{\infty} \rho^{j-1} (\Delta d_{t+j} - r_{t+j}) \tag{23}$$

This equation holds *ex-post*, and thus also *ex-ante*:

$$p_t - d_t = \text{Constant} + E_t \sum_{j=1}^{\infty} \rho^{j-1} (\Delta d_{t+j} - r_{t+j})$$
(24)

Now multiply both sides by  $p_t - d_t - E(p_t - d_t)$ . Then the variance of the log price-dividend ratio is

$$\operatorname{cov}\left(p_{t}-d_{t},\sum_{j=1}^{\infty}\rho^{j-1}\Delta d_{t+j}\right)$$
$$-\operatorname{cov}\left(p_{t}-d_{t},\sum_{j=1}^{\infty}\rho^{j-1}r_{t+j}\right) \qquad (25)$$

The fact that the price-dividend ratio varies means that either dividend growth rates or returns must be forecastable. The question is: which one is forecastable? Long-horizon regressions show little predictability in dividend growth rates and some predictability in returns and excess returns (Table 1).

We have seen that the aggregate stock market offers evidence of sizable and time-varying risk premia. Many subsets of the market offer comparable results. For example, Fama and French [12] sort stocks along different dimensions (e.g., their market size, book-to-market ratios, or past returns), build the corresponding portfolios and obtain large cross sections of returns. Buying the stocks in the last portfolio and selling the ones in the first portfolio lead to large and predictable excess returns, and thus evidence of equity risk premia.

| Horizon<br>h | Excess returns |      |       | Dividend growth |      |       |
|--------------|----------------|------|-------|-----------------|------|-------|
|              | $\alpha$       | s.e. | $R^2$ | $\alpha$        | s.e. | $R^2$ |
|              | 3.77           | 1.38 | 0.07  | $-0.11$         | 1.00 | 0.00  |
| 2            | 7.46           | 2.36 | 0.12  | $-0.76$         | 0.86 | 0.01  |
| 3            | 12.07          | 3.70 | 0.18  | 0.12            | 0.98 | 0.00  |
| 4            | 17.62          | 5.27 | 0.24  | 0.41            | 1.26 | 0.00  |
| 5            | 22.01          | 5.66 | 0.29  | 0.03            | 0.89 | 0.00  |

**Table 1** Long-horizon stock market predictability tests

This table reports slope coefficients  $\alpha$ , standard errors s.e. and  $R^2$  from in-sample predictability tests. In the left panel, the univariate regressions are  $R_{t,t+h}^e = C + \alpha D_t/P_t + \varepsilon_{t+h}$ , where  $R_{t,t+h}^e$  denotes the *h*-year ahead stock market excess return and  $D_t/P_t$  the dividend-price ratio. In the right panel, the regressions are  $D_{t+h}/D_t = C + \alpha D_t/P_t + \epsilon_{t+h}$ , where  $D_{t+h}/D_t$  denotes the *h*-year ahead dividend growth rate. The sample relates to the period 1927–2006. Data are annual

### **Bond Markets**

Equivalent results are obtained on bond markets, where expected excess returns exist and are timevarying. These results contradict the usual "expectation hypothesis of the term structure". It is reviewed, followed by the empirical evidence on bond excess returns (*see Expectations Hypothesis*).

The expectation hypothesis can be defined in three equivalent ways:

The yield  $y_t^n$  of a bond with maturity *n* is equal to the average of the expected yields of future one-year bonds, up to a constant risk premium:

$$y_t^n = \frac{1}{n} E_t(y_t^1 + y_{t+1}^1 + \dots + y_{t+n-1}^1) \qquad (26)$$

The forward rate equals the expected future spot rate, up to a constant risk premium:

$$f_t^{n \to n+1} = E_t(y_{t+n}^1) \tag{27}$$

The expected holding-period return (defined as the return on buying a bond of a given maturity  $n$  and selling it in the next period) is the same for any maturity  $n$ , up to a constant risk premium:

$$E_t(hpr_{t+1}^n) = y_t^1, \forall n \tag{28}$$

where  $hpr_{t+1}^n = p_{t+1}^{n-1} - p_t^n$  denotes the log holding-period return and  $p_t^n$  the log price of a bond of maturity  $n^a$ 

Following Campbell and Shiller [6], the expectation hypothesis is often tested with the following

**Table 2** Expectation hypothesis tests

| $n=2$   | $n=3$   | $n=4$   | $n=5$   |
|---------|---------|---------|---------|
| $-0.88$ | $-1.46$ | $-1.62$ | $-1.70$ |
| [0.47]  | [0.48]  | [0.53]  | [0.61]  |

This table reports slope coefficients  $\beta_n$  and associated standard errors from the following univariate regressions:  $y_{t+1}^{n-1} - y_t^n =$  $\alpha + \beta_n \left( \frac{y_t^n - y_t^1}{n-1} \right) + \epsilon_{t+1}$ , where  $y_t^n$  denotes the *n*-year bond yield. The sample relates to the period 1952-2006. Data are annual

equation:

$$y_{t+1}^{n-1} - y_t^n = \alpha + \beta_n \left( \frac{y_t^n - y_t^1}{n-1} \right) + \epsilon_{t+1} \qquad (29)$$

The expectation hypothesis implies that  $\beta_n = 1$ . In the data, the slope coefficient  $\beta_n$  is significantly below 1, often negative, and decreasing with the horizon  $n$  (Table 2). The rejection of the expectation hypothesis implies that bond markets offer timevarying, expected excess returns.

#### Currency Markets

Risk premia are also prevalent on currency markets. Currency excess returns correspond to the following investment strategy: borrowing in the domestic currency, exchanging this amount for some foreign currency, lending abroad, and converting back the earnings into the domestic currency. According to the standard uncovered interest rate parity (UIP) condition, the expected change in exchange rate should be equal to the interest rate differential between foreign and domestic risk-free bonds. In this case, expected currency excess returns should be zero. However, the UIP condition is clearly rejected in the data. In a simple regression of exchange rate changes on interest rate differentials, UIP predicts a slope coefficient of 1. Instead, empirical work following Hansen and Hodrick [13] and Fama [11] consistently reveals a regression coefficient that is smaller than 1 and very often negative. The international economics literature refers to these negative UIP slope coefficients as the UIP puzzle or forward premium anomaly. Negative slope coefficients mean that currencies with higher than average interest rates actually tend to appreciate. Investors in foreign one-period discount bonds thus earn the interest rate spread, which is known at the time of their investment, plus the bonus from the appreciation of the currency during the holding period. As a result, the failure of the UIP condition implies positive predictable excess returns when investing in high interest rate currencies and negative excess returns for investing in low interest rate currencies. Lustig and Verdelhan [15] build portfolios of currency excess returns by sorting currencies on their interest rate differentials with the United States. They obtain a large cross section of currency excess returns and show that these excess returns compensate the US investor for bearing US aggregate macroeconomic risk because high interest rate currencies tend to depreciate in bad times. As a result, currency excess returns are also evidence of risk premia.

To summarize this section, equity, bond, and currency markets offer predictable excess returns, and are thus characterized by risk premia. Now the potential theoretical explanations of these risk premia are discussed.

# **Theoretical Interpretations**

As observed above, the consumption-CAPM (also known as *power utility*) can replicate average equity excess returns only with implausibly high risk-aversion coefficients. Moreover, if consumption growth shocks are close to independent and identically distributed (i.i.d.)—as they are in the data—this model does not explain time variations in expected excess returns. A large literature seeks to address these shortcomings and offers different interpretations of the observed risk premia. Now the three most

successful classes of models in this literature, namely, habit preferences, long-run risk, and disaster risk, are reviewed.

## *Habit Preferences*

Habit preferences assume that the agent does not care about the absolute level of his/her consumption, but cares about its relative level compared to a habit level that can be interpreted as a subsistence level, past consumption, or the neighbors' consumption. Hence, preferences over habits *H* are defined using ratios or differences (*C/H* or *C* − *H*), where *H* depends on past consumption: *Ht* = *f (Ct*<sup>−</sup>1*, Ct*<sup>−</sup>2*, . . .)*. Major examples of habit preferences are found in Abel [1], Campbell and Cochrane [4], Constantinides [8] and Sundaresan [18]. Preferences defined using differences between consumption and habit (e.g., *u(C)* = *(C* − *H )*<sup>−</sup>*<sup>γ</sup>* ) imply time-varying risk-aversion coefficient if the percentage gap between consumption and habit changes through time:

$$\gamma_t = -\frac{CU_{CC}}{U_C} = \frac{\gamma H_t}{C_t - H_t} \tag{30}$$

Campbell and Cochrane [4] propose a model along these lines. In their model, the habit level is slow moving; in bad times, consumption falls close to the habit level, and the investor is very risk averse. This model offers a new interpretation to risk premia: investors fear bad returns and wealth loss because they tend to happen in recessions, when consumption falls relative to its recent past. These preferences generate many interesting asset pricing features: pro-cyclical variations of stock prices, long-horizon predictability, countercyclical variation of stock market volatility, countercyclicality of the Sharpe ratio, and the short- and long-run equity premium.

## *Long-run Risk*

The long-run risk literature works off the class of preferences due to Epstein and Zin [9, 10] and Kreps and Porteus [14]. These preferences impute a concern for the timing of the resolution of uncertainty to agents, and the risk-aversion coefficient is no longer the inverse of the intertemporal elasticity of substitution as it is with the consumption-CAPM (*see* **Recursive Preferences**). Building on these preferences, Bansal and Yaron [2] propose a model where the consumption and dividend growth processes contain a low-frequency component and are heteroscedastic. These two features capture time-varying growth rates and time-varying economic uncertainty. Because this low-frequency component is persistent, a high value today signals high expected consumption growth in the future. If the intertemporal elasticity of substitution is above 1, then, in response to higher expected growth, agents buy more assets, and the price to consumption ratio rises: the intertemporal substitution effect dominates the wealth effect. In this case, asset prices are high in good times and low in bad times; thus, investors require risk premia. In this model, agents have preference for early resolution of uncertainty, which increases the risk compensation for long-run growth and uncertainty risks.

#### Disaster Risk

In the disaster risk literature, the agent is characterized by the usual constant relative risk-aversion preferences. Rietz [17] assumes that in each period a small-probability disaster may occur, and in this case, consumption and dividends drop sharply. Barro [3] calibrates disaster probabilities from the twentieth-century global history and shows that they are consistent with the high equity premium, low riskfree rate, and volatile stock returns. In this model, risk premia exist because investors fear rare economic disasters.

# Conclusion

Under a minimal set of assumptions, any return satisfies a simple Euler equation. This equation implies that expected returns in excess of the risk-free rate, that is, risk premia, exist because returns comove with aggregate factors that matter for the investor. Empirical evidence from the equity, bond, and currency markets points to large and time-varying predictable excess returns. A recent literature tries to replicate and interpret these risk premia as compensations for recession, long-run, or disaster risks.

## Acknowledgments

I owe a great part of my knowledge on risk premia to John Cochrane and to his book on "Asset Pricing", which has inspired large parts of this article.

# **End Notes**

<sup>a.</sup>Recall that the yield  $y_t^n$  of an *n*-year bond is a fraction of the log price  $p_t^n$  of the bond:  $y_t^n = -\frac{1}{n} p_t^n$ .

# References

- Abel, A.B. (1990). Asset prices under habit formation [1] and catching up with the Joneses, American Economic Review 80(2), 38-42.
- Bansal, R. & Yaron, A. (2004). Risks for the long run: a [2] potential resolution of asset prizing puzzles, The Journal of Finance 59, 1481–1509.
- [3] Barro, R. (2006). Rare disasters and asset markets in the twentieth century, *Quarterly Journal of Economics* 121, 823-866.
- Campbell, J.Y. & Cochrane, J.H. (1999). By force of [4] habit: a consumption-based explanation of aggregate stock market behavior, Journal of Political Economy 107(2), 205-251.
- Campbell, J.Y. & Shiller, R.J. (1988). The dividend-[5] price ratio and expectations of future dividends and discount factors, Review of Financial Studies 1, 195-228.
- Campbell, J.Y. & Shiller, R.J. (1991). Yield spreads and [6] interest rates: a bird's eye view, Review of Economic Studies 58, 495-514.
- Cochrane, J.H. (2001). Asset Pricing. Princeton Univer-[7] sity Press, Princeton, NJ.
- Constantinides, G.M. (1990). Habit formation: a reso-[8] lution of the equity premium puzzle, The Journal of Political Economy 98, 519-543.
- Epstein, L.G. & Zin, S. (1989). Substitution, risk aver-[9] sion and the temporal behavior of consumption and asset returns: a theoretical framework, *Econometrica* 57, 937-969.
- [10] Epstein, L.G. & Zin, S. (1991). Substitution, risk aversion and the temporal behavior of consumption and asset returns, Journal of Political Economy 99(6),  $263 - 286$
- [11] Fama, E. (1984). Forward and spot exchange rates, Journal of Monetary Economics 14, 319-338.
- [12] Fama, E.F. & French, K.R. (1992). The cross-section of expected stock returns, Journal of Finance 47(2), 427-465.
- [13] Hansen, L.P. & Hodrick, R.J. (1980). Forward exchange rates as optimal predictors of future spot rates: an econometric analysis, Journal of Political Economy 88(5),  $829 - 853.$
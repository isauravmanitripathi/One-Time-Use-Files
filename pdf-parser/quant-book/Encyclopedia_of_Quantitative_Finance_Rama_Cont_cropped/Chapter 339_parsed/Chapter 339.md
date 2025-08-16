# **Kyle Model**

The Kyle model [13] provides a tractable framework in which liquidity and the informativeness of prices can be measured. It played a key role in the proliferation of research papers on heterogeneous information that occurred in the past two decades.<sup>a</sup> The model formalizes the explanation of liquidity given by Treynor  $[6]$ —reprinted as  $[14]$ —who observes that "the liquidity of a market ... is inversely related to the average rate of flow of new information ... and directly related to the volume of liquidity-motivated transactions." These relationships are captured in "Kyle's lambda".

The Kyle model describes the price of a single risky asset over a time period  $[0, 1]$ . A risk-free asset is used as the numeraire, so the risk-free rate is zero. In the original model, there is a single trader with private information. An announcement is made at date 1 that reveals the information of this trader, and he/she is able to liquidate his/her position at date 1 at the revealed value. The "liquidity-motivated transactions" described by Bagehot [6] are modeled as random trades (by "liquidity traders" or "noise traders") that are independent of the asset value. The trades of the informed and liquidity traders are "batched" and submitted to risk-neutral competitive market makers.<sup>b</sup> The market makers trade on their own accounts to clear the market, and because of competition and risk neutrality, the clearing price is the expected value of the asset, conditional on the information in the order flow.

An important feature of the Kyle model is the strategic behavior of the informed trader, that is, he/she considers the impact his/her orders have on the market price. This assumption avoids the "schizophrenia" of traders who believe they have no impact on market prices yet understand that prices reflect their private information, which, as Hellwig [10] notes, prevails in some competitive rational expectations models.

#### Single-period Kyle Model

In the single-period model, trading occurs only at date 0. Before trading, the single informed trader observes a normally distributed random variable  $\tilde{v}$ with mean  $\bar{v}$  and variance  $\sigma_v^2$ . The informed trader

chooses an order  $\tilde{x}$  depending on  $\tilde{v}$ . Noise traders submit an order  $\tilde{z}$  that is independent of  $\tilde{v}$  and normally distributed with mean 0 and variance  $\sigma_{z}^{2}$ . Market makers observe  $\tilde{y} \equiv \tilde{x} + \tilde{z}$  and set the price equal to  $\tilde{p} = E[\tilde{v}|\tilde{y}]$ . At date 1, the value  $\tilde{v}$  is revealed to the market, and the asset can be traded in arbitrarily large quantities at the price  $\tilde{v}$ . Thus, the informed trader's profit is  $\tilde{x}(\tilde{v}-\tilde{p})$ , and his/her objective is to maximize the expected profit.

There is a unique "linear equilibrium". Linearity means that  $\tilde{p} = \mu + \lambda \tilde{y}$  and  $\tilde{x} = \alpha + \beta \tilde{v}$ , for constants  $\mu$ ,  $\lambda$ ,  $\alpha$ , and  $\beta$ . Equilibrium means the following:

- (A) Given  $\alpha$  and  $\beta$ , pricing satisfies Bayes' rule, that is,  $\mu + \lambda \tilde{y} = E[\tilde{v}|\tilde{y}].$
- $(B)$ Given  $\mu$  and  $\lambda$ , the insider's strategy is optimal, that is,

$$\alpha + \beta \tilde{v} = \operatorname{argmax}_{x} E[x(\tilde{v} - \mu - \lambda(x + \tilde{z}))|\tilde{v}]$$
(1)

Note that optimality in  $(B)$  is among all possible demands x, including nonlinear functions of  $\tilde{v}$ . Linearity implies that  $\tilde{v}$  and  $\tilde{v}$  are jointly normal, so  $\lambda = \text{cov}(\tilde{v}, \tilde{v})/\text{var}(\tilde{v})$ . Using this fact and solving the optimization problem in (B), it is straightforward to calculate that the unique linear equilibrium is given by  $\mu = \bar{v}$ ,  $\alpha = -\beta \bar{v}$ ,  $\beta = \sigma_z/\sigma_v$ , and  $\lambda = \sigma_v/(2\sigma_z)$ . The unconditional expected profit of the informed trader is  $\sigma_v \sigma_z/2$ .

Kyle [13] defines the reciprocal of  $\lambda$  as the "depth" of the market. It measures the number of shares that can be traded, causing only a unit change in the price. The formula for  $1/\lambda$  encapsulates Bagehot's intuition: the depth of the market is proportional to the amount of noise trading as measured by  $\sigma_z$  and inversely proportional to the amount of private information as measured by  $\sigma_v$ .

#### **Dynamic Kyle Model**

A trader who recognizes that his/her trades impact the market price will typically want to execute a trade in small pieces, walking up or down the market supply curve. The single-period model gives the informed trader only one opportunity to trade, which is an unnatural constraint. Relaxing this constraint enables one to examine how the dynamic optimization of the informed trader affects the evolution of liquidity over time. The general conclusion is that the informed trader spreads his/her trades over time in a manner that has the effect of smoothing liquidity intertemporally. We return to this issue in the final paragraph.

Kyle [13] analyzes a discrete-time  $N$ -period version of the model, assuming that the noise trades in each period are independent normally distributed variables with variance  $\sigma_z^2 \Delta t$ , where  $\Delta t = 1/N$  is the length of each period. The variance of cumulative noise trades during the period [0, 1] is again  $\sigma_z^2$ . Kyle shows that the equilibria converge to the equilibrium of a continuous-time model in which the noise trades arrive as a Brownian motion with volatility  $\sigma_z$ .

The continuous-time model affords the informed trader the maximum flexibility in timing his/her trades. In the original continuous-time model, the single informed trader observes the normally distributed variable  $\tilde{v}$  at date 0, and the asset trades at  $\tilde{v}$  at date 1, as in the single-period model. The asset is traded continuously during  $[0, 1]$ . The number of shares Z held by noise traders is assumed to be a Brownian motion, independent of  $\tilde{v}$ , having volatility  $\sigma_z$ . Again, the variance of cumulative noise trades during  $[0, 1]$ is  $\sigma_z^2$ . At each date t, the informed trader chooses a number of shares  $X_t$  to hold. This choice depends on  $\tilde{v}$  and the history of Z through date  $t$ .<sup>c</sup> Market makers observe  $Y \equiv X + Z$  and set the price  $P_t$  to be the expected value of  $\tilde{v}$ , conditional on the information in  $Y$  through date  $t$ .

The principal conclusions of the continuous-time model are as follows:

- 1. The price change at each instant is  $dP_t = \lambda dY_t$ , where  $\lambda = \sigma_v/\sigma_z$ . Thus, market depth is constant over time, and the depth of the market is only half of what it is when the informed trader is constrained to trade only once.
- The price process is a Brownian motion with 2. volatility  $\sigma_v$ . Constancy of the volatility means that information is incorporated into the price at a constant rate. The volatility does not depend on the level of noise trading  $\sigma_z$ .
- 3. All of the private information is incorporated into the price before the announcement date (the price converges to  $\tilde{v}$  by date 1).
- 4. The expected profit of the informed trader is  $\sigma_v \sigma_z$ . Thus, the insider's expected profit is twice

what it is when he/she is constrained to trade only once. This implies that the expected losses of noise traders are also twice what they are in the single-period model.

5. The equilibrium informed trades are of order  $dt$ . This reflects the fact that the desired trades of a patient anonymous trader are optimally executed in small pieces.

To analyze the informed trader's optimization problem in this model, one must start with some guess about how  $P$  depends on  $Y$ . Two possible approaches are as follows: (i) conjecture  $P_t = H(t, Y_t)$  for some function *H* and (ii) conjecture  $dP_t = \mu_t dt + \lambda_t dY_t$ for nonrandom  $\mu$  and  $\lambda$ . Either approach is feasible for the basic model. In some generalizations of the model, the first conjecture works, and in others the second works.<sup>d</sup> Taking approach (ii), one can analyze the Hamilton-Jacobi-Bellman equation for the informed trader, using the price as the state variable, to deduce that  $\mu$  must be zero and  $\lambda$  must be constant for the informed trader to have an optimum. When this is true, any continuous finite-variation strategy for the informed trader is optimal, provided the price is pushed to  $\tilde{v}$  by the announcement date.

To deduce the value of  $\lambda$ , one can use the Kalman-Bucy filtering equation (see **Filtering**). Alternatively, in the basic model, one can reason as follows: because the price is always the conditional expectation of  $\tilde{v}$ , it is a martingale, given market makers' information. Because  $dP = \lambda dY$ , Y must also be a martingale relative to market makers' information. Given that  $dX$  is of order  $dt$ , it follows that the volatility of  $Y$  is the volatility of  $Z$ . Thus,  $Y$  is actually a Brownian motion with volatility  $\sigma_z$ , relative to the market makers' information. In particular,  $Y_1$  is normally distributed with mean zero and variance  $\sigma_z^2$ . Given that  $\tilde{v} = P_0 + \lambda Y_1$ , it follows that  $P_0 = \bar{v}$  and  $\lambda = \sigma_v/\sigma_z.$ 

The informational advantage of the informed trader in this model can be summarized as follows. The price process appears to be a Brownian motion to market makers and the rest of the market. However, the informed trader knows its date 1 value  $\tilde{v}$ . Thus, to the informed trader, the price process is a Brownian bridge. The informed trader's equilibrium trading strategy is precisely the drift of a Brownian bridge:

$$\mathrm{d}X_t = \frac{\sigma_z}{\sigma_v} \left(\frac{\tilde{v} - P_t}{1 - t}\right) \mathrm{d}t \tag{2}$$

For general (i.e., nonnormal) continuous distributions of the asset value, the result of constant depth generalizes to *λ* being a martingale, given market makers' information. For example, if the asset value is lognormally distributed, then the equilibrium price process is a geometric Brownian motion: d*P* = *λ(P )* d*Y* = *φP* d*Y* for constant *φ* [2]. This martingale property is robust to time-varying liquidity trading and a flow of information to the informed trader [5] but not to risk aversion [7, 12] or to the presence of multiple informed traders [4, 8, 11].

## **Acknowledgments**

We are grateful to Pete Kyle for helpful comments.

## **End Notes**

a*.* The paper of Kyle [13] was the seventh most widely cited finance paper during the 1990s, according to Arnold *et al.* [1].

b*.* The assumption that orders are batched is unimportant if liquidity trades are small and arrive frequently. This is established by Back and Baruch [3], who analyze a discrete-trade/Poisson model, which can be interpreted as a Glosten–Milgrom [9] model with explicit optimization by the informed trader. They show that the equilibria of the Glosten–Milgrom model converge to the equilibrium of a continuous-time Kyle model as the arrival rate of liquidity trades converges to infinity and the size of individual liquidity trades converges to zero.

c*.* The informed trader can implicitly observe *Z* by observing the price and backing out the influence of *X* on the price. d*.* A third approach is useful in the case of an informed trader with CARA utility: take *Pt* = *H (t, Ut)* where d*Ut* = *κt* d*Yt* for some function *H* and a nonrandom *κ* [7].

## **References**

[1] Arnold, T., Butler, A.W., Crack, T.F. & Altintig, A. (2003). Impact: what influences finance research? *Journal of Business* **76**, 343–361.

- [2] Back, K. (1992). Insider trading in continuous time, *Review of Financial Studies* **5**, 387–409.
- [3] Back, K. & Baruch, S. (2004). Information in securities markets: Kyle Meets Glosten and Milgrom, *Econometrica* **72**, 433–465.
- [4] Back, K., Cao, C.H. & Willard, G.A. (2000). Imperfect competition among informed traders, *Journal of Finance* **55**, 2117–2155.
- [5] Back, K. & Pedersen, H. (1998). Long-lived information and intraday patterns, *Journal of Financial Markets* **1**, 385–402.
- [6] Bagehot, W. (1971). The only game in town, *Financial Analysts' Journal* **22**, 12–14. (pseud.).
- [7] Baruch, S. (2002). Insider trading and risk aversion, *Journal of Financial Markets* **5**, 451–464.
- [8] Foster, F.D. & Viswanathan, S. (1996). Strategic trading when agents forecast the forecasts of others, *Journal of Finance* **51**, 1437–1478.
- [9] Glosten, L.R. & Milgrom, P.R. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders, *Journal of Financial Economics* **14**, 71–100.
- [10] Hellwig, M.F. (1980). On the aggregation of information in competitive markets, *Journal of Economic Theory* **22**, 477–498.
- [11] Holden, C.W. & Subrahmanyam, A. (1992). Long-lived private information and imperfect competition, *Journal of Finance* **47**, 247–270.
- [12] Holden, C.W. & Subrahmanyam, A. (1994). Risk aversion, imperfect competition, and long-lived information, *Economics Letters* **44**, 181–190.
- [13] Kyle, A.S. (1985). Continuous auctions and insider trading, *Econometrica* **53**, 1315–1336.
- [14] Treynor, J. (1995). The only game in town, *Financial Analysts' Journal* **51**, 81–83.

## **Related Articles**

**Adverse Selection**; **Filtering**; **Glosten–Milgrom Models**; **Liquidity**; **Liquidity Premium**; **Market Transparency**.

KERRY BACK & SHMUEL BARUCH
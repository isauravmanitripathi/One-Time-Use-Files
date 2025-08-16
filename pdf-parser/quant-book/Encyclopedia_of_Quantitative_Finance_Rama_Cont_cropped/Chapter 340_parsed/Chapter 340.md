# **Probability of Informed** Trading

The extent of private information in markets is a critical determinant in the price formation process. By modeling the trading process and the market maker's learning process, we can use trade data to make inferences about this private information, or more precisely, about the probability of informed trading (PIN). The extent of private information affects bid and ask prices and, hence, the available liquidity in an asset. Perhaps more importantly, the effect of PIN transcends pure market microstructure issues, as evidence suggests that PIN affects the required rate of return on stocks.

### The PIN Model

In a series of papers, Easley et al. model a market in which a competitive market maker trades a risky asset with informed and uninformed traders  $[4-8]$ . As a simple example, consider the sequential trade tree diagram shown in Figure 1. Trade occurs over  $t = 1, \ldots, T$  discrete trading days and, within each trading day, trade occurs in continuous time. Information events occur between trading days with probability  $\alpha$ . When an information event occurs, it is either bad news, with probability  $\delta$ , or good news with probability,  $1 - \delta$ . Good news at date t is that the asset is worth  $\bar{V}_t$ , and bad news is that it is worth  $V_t$ .

During any trading day, orders arrive at the market according to Poisson processes. The market maker sets prices to buy or sell throughout the day, and then executes orders as they arrive. Traders informed of bad news sell and those informed of good news buy. Orders from the informed traders follow a Poisson process, with daily arrival rate  $\mu$ . Uninformed traders trade for liquidity reasons. Buy and sell orders from uninformed traders arrive at the market according to independent Poisson processes, with daily arrival rates  $\varepsilon_b$  for buy orders and  $\varepsilon_s$  for sell orders. If an order arrives at some time, the market maker observes the trade (either a buy or a sale), and he/she uses this information to update his/her beliefs. New prices are set, trades evolve, and the price process moves in response to the market maker's changing beliefs.

We can use the model parameters to compute the probability that the opening trade on a day is information based, PIN, as

$$\text{PIN} = \frac{\alpha \mu}{\alpha \mu + \varepsilon_b + \varepsilon_s} \tag{1}$$

where  $\alpha \mu + \varepsilon_b + \varepsilon_s$  is the arrival rate for all orders and  $\alpha\mu$  is the arrival rate for information-based orders. Thus, the ratio is the fraction of orders that arise from informed traders or the probability that the opening trade is information based.

The model is quite flexible and allows for extensions with greater complexity in the trading and information processes. Easley et al. [3], for instance, present a dynamic extension with time variation in the traders' arrival rates.

#### **Estimating the PIN Model**

Suppose that we now view this problem from the perspective of an econometrician. If we, like the market maker, can observe the sequence of trades, we can use this to estimate the structural model via maximum likelihood. That is, we can determine the probability of information-based trading in a given stock.

The first step in the estimation is to note that the total number of buys and sells per day is a sufficient statistic for the trade data. This occurs because of the assumption that arrivals follow independent Poisson processes. The likelihood function induced by this model for the total number of buys and sells on a single trading day is

$$\mathcal{L}((B, S)|\theta) = \alpha (1 - \delta) e^{-(\mu + \varepsilon_b + \varepsilon_s)} \frac{(\mu + \varepsilon_b)^B (\varepsilon_s)^S}{B!S!}$$
$$+ \alpha \delta e^{-(\mu + \varepsilon_b + \varepsilon_s)} \frac{(\mu + \varepsilon_s)^S (\varepsilon_b)^B}{B!S!}$$
$$+ (1 - \alpha) e^{-(\varepsilon_b + \varepsilon_s)} \frac{(\varepsilon_b)^B (\varepsilon_s)^S}{B!S!} \quad (2)$$

where  $(B, S)$  is the total number of buys and sells for the day and  $\theta = (\mu, \epsilon_b, \epsilon_s, \alpha, \delta)$  is the parameter vector. This likelihood function is a mixture of three Poisson probabilities, weighted by the probability of having a "good news day"  $\alpha(1-\delta)$ , a "bad news day"  $\alpha\delta$ , and a "no news day"  $(1 - \alpha)$ .

The model assumes that each day the arrivals of an information event and trades, conditional on information events, are drawn from identical and independent distributions. Thus, the likelihood function for  $T$  days is a product of the above likelihood over days. The log likelihood function, after dropping a constant term and rearranging, can be written as

$$\begin{split} &\mathcal{L}((B_t, S_t)_{t=1}^T | \theta) \\ &= \sum_{t=1}^T \left[ -\varepsilon_b - \varepsilon_s + M_t (\ln x_b + \ln x_s) \right. \\ &\quad + B_t \ln(\mu + \varepsilon_b) + S_t \ln(\mu + \varepsilon_s)] \\ &\quad + \sum_{t=1}^T \ln \left[ \alpha (1 - \delta) \mathrm{e}^{-\mu} x_s^{S_t - M_t} x_b^{-M_t} \right. \\ &\quad + \alpha \delta \mathrm{e}^{-\mu} x_b^{B_t - M_T} x_s^{-M_t} + (1 - \alpha) x_s^{S_t - M_t} x_b^{B_t - M_t} \right] \end{split} \tag{3}$$

where  $M_t = \min(B_t, S_t) + \max(B_t, S_t)/2$ ,  $x_s = \frac{\varepsilon_s}{\mu + \varepsilon_s}$ , and  $x_b = \frac{\varepsilon_b}{\mu + \varepsilon_b}$ . The factoring of  $x_b^{M_t}$  and  $x_{s}^{M_{t}}$  increases the computing efficiency and reduces the truncation error. This is particularly important for stocks with a large number of buys and sells as it avoids computation of small fractions (arrival rates) taken to large powers (numbers of trades).

The likelihood function (3) depends upon the number of buys and sells per day. In the United States, the most widely available high-frequency data sets do not contain information about the underlying orders, only the resulting transactions. Therefore, researchers rely on algorithms such as the Lee and Ready [10] algorithm, which mainly uses trade placement relative to the current bid and ask quotes to determine trade direction.

Easley et al. [4] obtain yearly PIN estimates for all New York Stock Exchange (NYSE)-listed stocks. They find that PIN is on average 0.19 across stocks and its cross-sectional standard deviation is 0.057. That is, for an average stock, 19% of trades are motivated by private information.

# Applications

The estimates of the model's structural parameters can be used to construct the theoretical opening bid and ask prices. As is standard in microstructure models, the market maker sets trading prices such that his/her expected losses to informed traders just offset his/her expected gains from trading with uninformed traders. This balancing of gains and losses gives rise to the bid-ask spread. The opening spread is easiest to interpret if we express it explicitly in terms of PIN. In the case where the uninformed are equally likely to

![](_page_1_Figure_8.jpeg)

**Figure 1** Tree diagram of the trading process.  $\alpha$  is the probability of an information event,  $\delta$  is the probability of a low signal,  $\mu$  is the rate of informed trade arrival,  $\varepsilon_b$  is the arrival rate of uninformed buy orders, and  $\varepsilon_s$  is the arrival rate of uninformed sell orders. Nodes to the left-hand side of the dotted line occur once per day

buy and sell  $(\varepsilon_b = \varepsilon_s = \varepsilon)$  and news is equally likely to be good or bad ( $\delta = 0.5$ ), the percentage opening spread is

$$\frac{\Sigma}{V_t^*} = \text{PIN}\frac{(V_t - V_t)}{V_t^*} \tag{4}$$

where  $\Sigma$  is the spread, ask minus bid price, and  $V_t^*$  is the unconditional expected value of the asset given by  $V_t^* = \delta \bar{V}_t + (1 - \delta) \bar{V}_t$ . The opening spread is therefore directly related to the probability of informed trading. Note that if PIN equals zero, because of the absence of either new information ( $\alpha = 0$ ) or traders informed of it ( $\mu = 0$ ), the spread is also zero. This reflects the fact that only asymmetric information affects spreads when market makers are risk neutral. Neither the estimated measure of informationbased trading nor the predicted spread is related to market maker inventory because these factors do not enter into the model. Instead, these estimates represent a pure measure of the risk of private information.

Indeed, Easley et al. [8] and [4] find a strong relationship between PIN and the opening bid-ask spreads, consistent with the predictions of the model. In addition, PIN is negatively related crosssectionally to variables such as firm size and the level trading activity and positively related to the level of insider and institutional holdings [1].

Informational asymmetry has implications for a firm's cost of capital. An increase in PIN represents a risk not only to the market maker but also to the uninformed investors who cannot adjust their portfolios to take the private information into account. Therefore, uninformed investors would need to be compensated to invest in high PIN stocks. Easley and O'Hara [9] formalize this notion in a rational expectations model and show that more private information and less public information lead to higher expected returns. Easley et al. [4] find that a difference in PIN of 10 percentage points (about 2 standard deviations) between two stocks leads to a difference in expected returns of 2.5% per year.

The PIN variable also represents a straightforward control or interaction variable for researchers interested in the impact of a third variable on, say, stock prices. As an example, Duarte *et al.* [2] find that the effect of regulation fair disclosure on a firms' cost of capital is negative related to PIN, which is consistent with the notion that high PIN firms benefit more from decreases in the informational asymmetry resulting from increased disclosure.

## References

- Aslan, H., Easley, D., Hvidkjaer, S. & O'Hara, M. [1] (2007). Firm Characteristics and Informed Trading: Implications for Asset Pricing. Working paper, University of Houston, Cornell University and INSEAD.
- Duarte, J., Han, X., Harford, J. & Young, L. (2008). [2] Information asymmetry, information dissemination and the effect of regulation FD on the cost of capital, Journal of Financial Economics 87, 24-44.
- [3] Easley, D., Engle, R., O'Hara, M. & Wu, L. (2008). Time-varying arrival rates of informed and uninformed trades, Journal of Financial Econometrics 6(2), 171-207.
- [4] Easley, D., Hvidkjaer, S. & O'Hara, M. (2002). Is information risk a determinant of asset returns? Journal of Finance 57, 2185-2221.
- [5] Easley, D., Kiefer, N.M. & O'Hara, M. (1996). Creamskimming or profit-sharing? The curios role of purchased order flow, Journal of Finance 51, 811-833.
- Easley, D., Kiefer, N.M. & O'Hara, M. (1997). The [6] information content of the trading process, Journal of Empirical Finance 4, 159-186.
- [7] Easley, D., Kiefer, N.M. & O'Hara, M. (1997). One day in the life of a very common stock, Review of Financial Studies 10, 805-835.
- Easley, D., Kiefer, N.M., O'Hara, M. & Paperman, J.B. [8] (1996). Liquidity, information, and infrequently traded stocks, Journal of Finance 51, 1405-1436.
- [9] Easley, D. & O'Hara, M. (2004). Information and the cost of capital, Journal of Finance 59(4), 1553-1583.
- Lee, C.M.C. & Ready, M.J. (1991). Inferring trade [10] direction from intraday data, Journal of Finance 46, 733-746.

Soeren Hvidkjaer
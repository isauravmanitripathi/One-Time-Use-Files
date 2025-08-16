# **Fixed Mix Strategy**

There are a number of advantages of adopting multiperiod models over the traditional single-period, static models in portfolio managements [12]. One of the more important benefits, among others, is the improved performance on portfolio investments *via* the fixed mix rule  $[3-5]$ . The buy-and-hold rule, which represents single-period models, does not rebalance the portfolio at any intermediate juncture; hence, the weight on each component might change as asset prices fluctuate in different proportions. In contrast, when a portfolio is constructed based on the fixed mix rule, it is rebalanced at every time point so that component weights remain the same as the initial state. To keep the weights unchanged, investors should sell assets whose prices have gone up and buy ones whose prices have dropped. Therefore, in some sense, the fixed mix rule is analogous to the "buy low/sell high" strategy. Possibly because of such an analogy, there seems to be a widely spread misconception regarding the fixed mix strategy and its benefits—it requires mean-reverting processes for assets. Of course, because of its nature, it is not difficult to see that it would be helpful to have such processes to achieve better performance. However, the truth is that mean reversion is *not* necessary for the fixed mix to accomplish superior performance.

#### **Theoretical Background**

We first recall performance of the buy-and-hold strategy. Suppose that there are  $n$  stocks whose mean return is  $r \in \mathbf{R}^n$  and covariance matrix  $\Sigma \in$  $\mathbf{R}^{n \times n}$ . Assuming that normality,  $r^{\text{BH}}$  the average buyand-hold portfolio return with weight  $w \in \mathbf{R}^n$ , is normally distributed with mean  $w^T r$  and variance  $\sigma_n^2 = w^T \Sigma w$ . That is,

$$r^{\text{BH}} \sim \mathbf{N}(w^T r, \sigma_p^2) \equiv \mathbf{N}(w^T r, w^T \Sigma w) \tag{1}$$

Next, let us consider a fixed mix portfolio constructed from the same stocks with the same weight  $(w)$ as the previous buy-and-hold portfolio. Since it is rebalanced at every intermediate juncture, it is required to model stock prices as processes. Thus, we model them as an  $n$ -dimensional geometric Brownian motion whose return distribution for a unit time

length would be the same as the previous case. Then, the price process of stock  $i$  can be written as the following SDE:

$$\frac{\mathrm{d}S_i^i}{S_i^i} = \left(r_i + \frac{\sigma_i^2}{2}\right)\mathrm{d}t + \mathrm{d}B_t^i\tag{2}$$

where  $\sigma_i^2$  is the *i*th diagonal term of  $\Sigma$  (hence, variance of stock  $i$ ) and for the Cholesky factorization of  $\Sigma$ , L and the standard *n*-dimensional Wiener process  $(W_t^1 - W_t^n)^T$ ,

$$d(B_t^1 - B_t^n)^T = Ld(W_t^1 - W_t^n)^T$$
 (3)

Since the fixed mix portfolio is rebalanced at each time point to the initial weight  $(w)$ , its instantaneous growth rate is the same as the weighted sum of instantaneous growth rates of the stocks at any given juncture. Therefore, the SDE for the portfolio wealth can be written as

$$\frac{\mathrm{d}P_t^{\mathrm{FM}}}{P_t^{\mathrm{FM}}} = \sum_{i=1}^n w_i \frac{\mathrm{d}S_t^i}{S_t^i} = \sum_{i=1}^n w_i \left\{ \left( r_i + \frac{\sigma_i^2}{2} \right) \mathrm{d}t + \mathrm{d}B_t^i \right\} \tag{4}$$

With simple algebra, one can show that, for the standard one-dimensional Wiener process  $W_t$ ,

$$\frac{\mathrm{d}P_t^{\mathrm{FM}}}{P_t^{\mathrm{FM}}} = \left(w^T r + \frac{1}{2} \sum_{i=1}^n w_i \sigma_i^2\right) \mathrm{d}t + \sigma_p^2 \mathrm{d}W_t \quad (5)$$

Hence, the return of the fixed mix portfolio for a unit time length can be given as

$$r^{\text{FM}} \sim N\left(w^T r + \frac{1}{2} \sum_{i=1}^n w_i \sigma_i^2 - \frac{1}{2} \sigma_p^2, \quad \sigma_p^2\right)$$
$$\equiv N\left(w^T r + \frac{1}{2} \sum_{i=1}^n w_i \sigma_i^2 - \frac{1}{2} w^T \Sigma w, w^T \Sigma w\right)$$
(6)

Therefore, returns of both buy-and-hold  $(r^{\dagger} \text{BH})$  and fixed mix  $(r^{\dagger}FM)$  are normally distributed with the same variance  $(\sigma_p^2)$ , whereas the mean of the latter contains extra terms  $(\sum_{i=1}^{n} w_i \sigma_i^2 - \sigma_p^2/2)$ . These extra terms, which are often referred to as *rebalanc*ing gains or volatility pumping, represent the value of having an option to constantly rebalance the portfolio to initial weights.

To observe its effects more closely, let us consider the following simple example: suppose that we have  $n$  stocks where the expected return and the volatility of each are r and  $\sigma$ , and the correlation is given as  $\rho$ . Assuming the portfolio is equally weighted, the amount of the rebalancing gain

$$RG = \frac{1}{2} \left\{ \sum_{i=1}^{n} \frac{1}{n} \sigma^2 - \left(\frac{1}{n} - \frac{1}{n}\right) \Sigma \left(\frac{1}{n} - \frac{1}{n}\right)^T \right\}$$
$$= \frac{(n-1)\sigma^2 (1-\rho)}{2n} \tag{7}$$

Now it is evident that the fixed mix strategy has benefit over the static buy-and-hold rule, even without *mean-reversion*; the rebalancing gain is always positive, except the case that all stock returns are perfectly correlated, in which it becomes 0. Note that the rebalancing gain is an increasing function of the number of stocks (n) and the volatility ( $\sigma$ ) and is a decreasing function of the correlation  $(\rho)$ . See Figure 1 for the illustrations of simulation results for the effects of  $\sigma$  and  $\rho$  to rebalancing gains. Therefore, with the wisdom from the portfolio theory, one can see that volatile stocks should *not* be penalized when a portfolio is constructed with the fixed mix rule, as long as their correlations to other stocks are low and they possess reasonable expected returns; they can serve as good sources of rebalancing gains. The portfolio risks can be effectively reduced via dynamic diversification. For more complete discussion, see  $[3-5,$ 10, 15].

![](_page_1_Figure_4.jpeg)

**Figure 1** Effects of volatility  $(\sigma)$  and correlation  $(\rho)$  to rebalancing gains  $(n = 5)$ 

## **Practical Examples**

Under certain conditions, the fixed mix rule has been proved to be optimal in multiperiod settings. Early on, Mossin [7] showed that it is the optimal strategy when an investor maximizes the expected power utility of her terminal wealth, assuming IID asset returns and no intermediate consumption. Samuleson [17] analyzed the problem in more generalized settings: using an additive intertemporal power utility function of consumption over time, he proved that it is still optimal to adopt the fixed mix rule when the investor is allowed to consume at intermediate junctures. Merton [6] also concluded the same in the continuous time setting model.

Indeed, there are many practical applications that are successfully taking advantage of rebalancing gains by employing fixed mix rules. Among others [9, 14, 16], one of good examples is the S&P 500 equalweighted index (S&P EWI) by Rydex Investments (Figure 2) [8]. Unlike traditional cap-weighted  $S\&P$ 500 index, it applies the fixed mix rule to the same stocks as S&P 500, rebalancing them every six month to maintain the equally weighted portfolio. During 1994-2005, S&P Equal Weighted Index earned 2% excess return with mere 0.6% extra volatility over S&P 500. This added profit is partially due to superior performance of small/mid-sized stocks and also can be accounted for by rebalancing gains.

Implementations of the fixed mix rule could also lead to successful leverage. Figure 3 illustrates levered portfolios of buy-and-hold and fixed

![](_page_1_Figure_10.jpeg)

Figure 2 Log prices of S&P 500 and S&P EWI during July 2003 to December 2006

![](_page_2_Figure_1.jpeg)

**Figure 3** Efficient frontiers of levered buy-and-hold and fixed mix portfolios: (a) mix of traditional and alternative assets (1994–2005) and (b) mix of momentum strategies of five regions (1980–2006)

mix portfolios constructed in two different domains. Figure 3(a) compares efficient frontiers of buy-andhold and fixed mix portfolios, which are constructed with six traditional assets (S&P 500, EAFE, Lehman long-term bond index, Strips, NAREIT, and Goldman Sachs commodity index) and four alternative assets (hedge fund index, managed futures index, Tremont long-short equity index, and currency index) [11]. Both are equally weighted and levered up to 100% *via* t-bill rate. Although the buy-and-hold portfolio is not rebalanced, monthly rebalancing rule is adopted for the fixed mix for the entire sample period (1994–2005). In addition, Figure 3(b) depicts results from portfolios of industry-level momentum strategies across international stock markets for 27 year sample period (1980–2006) [10]. Momentum strategies are constructed in five nonoverlapping regions (US, EU, Europe except EU, Japan, and Asia except Japan) and aggregated into equally weighted portfolios with leverage up to 100%. Similar to the previous case, the fixed mix portfolio is rebalanced monthly. In both the cases, the efficient frontiers from the fixed mix dominate ones from the buy-and-hold.

## **Implementation Issues**

The fixed mix rule is now becoming a norm in various financial domains. For instance, it is now commonplace for large pension plans, such as TIAA-CREF, to automatically rebalance client-selected portfolios back to client-selected weights, at the client's requests. Given the circumstances, it is imperative to address issues regarding practical implementations. First, since the best sources of rebalancing gains are volatile financial instruments with low intracorrelations, it is crucial to find a set of relatively independent assets. However, the task is very unlikely to be perfectly achieved in the real world. Second, even such a set exists at certain time point, correlations could change over time. For instance, it is well known that stock indices across international markets become highly correlated upon serious market distress. In addition, one should consider transaction costs such as capital gain taxes upon deciding the rebalancing intervals. Although frequent rebalancing could lead to investment performance close to the theoretical values, it may deteriorate performance due to transaction costs. Careful analysis on this tradeoff is required. Good references regarding practical implementations of the fixed mix rules include [1, 2, 13, 18].

## **References**

- [1] Davis, M.H.A. & Norman, A.R. (1990). Portfolio selection with transaction costs, *Mathematics of Operations Research* **15**, 676–713.
- [2] Dumas, B. & Luciano, E. (1991). An exact solution to a dynamic portfolio choice problem under transaction costs, *Journal of Finance* **46**, 577–595.
- [3] Fernholz, R. (2002). *Stochastic Portfolio Theory*, Springer-Verlag, New York.
- [4] Fernholz, R. & Shay, B. (1982). Stochastic portfolio theory and stock market equilibrium, *Journal of Finance* **37**, 615–624.
- [5] Luenberger, D. (1997). *Investment Science*; Oxford University Press, New York.

- [6] Merton, R.C. (1969). Lifetime portfolio selection under uncertainty: the continuous-time case, *Review of Economics Statistics* **51**, 247–257.
- [7] Mossin, J. (1968). Optimal multi-period portfolio policies, *Journal of Business* **41**, 215–229.
- [8] Mulvey, J.M. (2005). *Essential Portfolio Theory*, A Rydex Investment White Paper (also Princeton University Report), 14–17.
- [9] Mulvey, J.M., Gould, G. & Morgan, C. (2000). An asset and liability management system for Towers Perrin-Tillinghast, *Interfaces* **30**, 96–114.
- [10] Mulvey, J.M. & Kim, W.C. (2007). *Constructing a Portfolio of Industry-level Momentum Strategies Across Global Equity Markets*, Princeton University Report.
- [11] Mulvey, J.M. & Kim, W.C. (2007). The role of alternative assets in portfolio construction, *Encyclopedia of Quantitative Risk Assessment*, John Wiley & Sons, to be published.
- [12] Mulvey, J.M., Pauling, B. & Madey, R.E. (2003). Advantages of multi-period portfolio models, *Journal of Portfolio Management* **29**, 35–45.
- [13] Mulvey, J.M. & Simsek, K.D. (2002). Rebalancing strategies for long-term investors. *Computational Methods in Decision-Making, Economics and Finance: Optimization Models*, E.J. Kontoghiorghes, B. Rustem & S. Siokos, eds, Kluwer, pp. 15–33.
- [14] Mulvey, J.M. & Thorlacius, A.E. (1998). The Towers Perrin global capital market scenario generation system: CAP Link, in *World Wide Asset and Liability Modeling*, W. Ziemba & J. Mulvey, eds, Cambridge University Press, Cambridge, pp. 286–312.

- [15] Mulvey, J.M., Ural, C. & Zhang, Z. (2007). hbox-Improving performance for long-term investors: wide diversification, leverage, and overlay strategies, *Quantitative Finance* **7**, 175–187.
- [16] Perold, A.F. & Sharpe, W.F. (1998). Dynamic strategies for asset allocation, *Financial Analysts Journal* **44**, 16–27.
- [17] Samuelson, P.A. (1969). Lifetime portfolio selection by dynamic stochastic programming, *Review of Economics Statistics* **51**, 239–246.
- [18] Shreve, S.E. & Soner, H.M. (1991). Optimal investment and consumption with two bonds and transaction costs, *Mathematical Finance* **1**, 53–84.

## **Further Reading**

Mulvey, J.M., Kaul, S.S.N. & Simsek, K.D. (2004). Evaluating a trend-following commodity index for multi-period asset allocation, *Journal of Alternative Investments* **7**, 54–69.

## **Related Articles**

**Diversification**; **Expected Utility Maximization**; **Mutual Funds**; **Transaction Costs**.

JOHN M. MULVEY & WOO CHANG KIM
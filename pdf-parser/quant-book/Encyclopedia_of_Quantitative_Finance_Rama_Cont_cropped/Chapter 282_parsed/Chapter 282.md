# **Sharpe Ratio**

The Sharpe ratio (SR) is a popular measure of portfolio performance that was introduced as the reward-to-variability ratio in [6]. For a given set of returns during an evaluation period, portfolio *p*'s *ex post* SR is

$$SR_p = \frac{\overline{R}_p - \overline{R}_f}{s_p} \tag{1}$$

where *Rp* and *sp* denote, respectively, the historical average and standard deviation of *p*'s returns; *Rf* denotes the average risk-free return.a A portfolio's SR is typically compared to a market index *m*'s SR:

$$SR_m = \frac{\overline{R}_m - \overline{R}_f}{s_m} \tag{2}$$

Figure 1 shows that *SR<sup>p</sup>* represents the slope of a line originating at the average risk-free rate and extending to point *p* where the portfolio is located. Similarly, *SR<sup>m</sup>* represents the slope of a line extending to point *m* where the index is located. This line is a proxy for the *ex post* capital market line (CML) in [5]. Portfolio *p* has had superior performance relative to *m* since *SR<sup>p</sup> > SRm*, resulting in it plotting above the CML; if it had plotted below, then *SR<sup>p</sup> < SR<sup>m</sup>* and it would have had inferior performance.

![](_page_0_Figure_6.jpeg)

**Figure 1** Evaluating the performance of portfolio *p* with the Sharpe ratio

The SR can also be used to make portfolio construction decisions as in [7]. For a given holding period, portfolio *p*'s *ex ante* SR is

$$\frac{\mathrm{E}[R_p] - R_f}{\sigma[R_p]} \tag{3}$$

where *E*[*Rp*] and *σ*[*Rp*] denote, respectively, the expected value and standard deviation of *p*'s future return, and *Rf* denotes the risk-free return. In frictionless markets with a risk-free security, the tangency portfolio in [10] has the highest SR (in absolute value). Optimal portfolios of investors using mean–variance analysis consist of combinations of the risk-free security and the tangency portfolio, which is the market portfolio in [5].

The SR has limitations. First, it assumes that either (i) investors' objective functions are defined solely over the first two moments of portfolio return distributions or (ii) such distributions are characterized by only these moments. Second, proper use of the SR requires knowledge of investors' investment horizons. Levy [4] shows that a bias emerges when using it with a horizon that is different from that of investors. Cvitanic´ *et al.* [2] find that maximizing the short-term *ex ante* SR is suboptimal for long-term investors. Third, the SR can be manipulated by using derivatives. Ingersoll *et al.* [3] define and characterize a manipulation-proof performance measure. Their measure resembles the average value of a power utility function defined over portfolio returns.

## **End Notes**

a*.* For other reward-to-risk ratios of portfolio performance that use VaR and beta instead of standard deviation as risk measures in the denominator of equation (1), see references [1] and [11], respectively. Also see references [8] and [9].

## **References**

- [1] Alexander, G.J. & Baptista, A.M. (2003). Portfolio performance evaluation using Value-at-Risk, *Journal of Portfolio Management* **29**, 93–102.
- [2] Cvitanic, J., Lazrak, A. & Wang, T. (2008). Implications ´ of the Sharpe ratio as a performance measure in multiperiod settings, *Journal of Economic Dynamics and Control* **32**, 1622–1649.
- [3] Ingersoll, J., Spiegel, M., Goetzmann, W. & Welch, I. (2007). Portfolio performance manipulation and manipulation-proof performance measures, *Review of Financial Studies* **20**, 1503–1546.

- [4] Levy, H. (1972). Portfolio performance and the investment horizon, *Management Science* **18**, B645–B653.
- [5] Sharpe, W.F. (1964). Capital asset prices: a theory of market equilibrium under conditions of risk, *Journal of Finance* **19**, 425–442.
- [6] Sharpe, W.F. (1966). Mutual fund performance, *Journal of Business* **39**, 119–138.
- [7] Sharpe, W.F. (1975). The Sharpe ratio, *Journal of Portfolio Management* **21**, 49–58.
- [8] Sortino, F., van der Meer, R. & Plantinga, A. (1999). The Dutch triangle, *Journal of Portfolio Management* **26**, 50–58.
- [9] Stutzer, M. (2000). A portfolio performance index, *Financial Analysts Journal* **56**, 52–61.

- [10] Tobin, J. (1958). Liquidity preference as behavior towards risk, *Review of Economic Studies* **25**, 65–86.
- [11] Treynor, J. (1965). How to rate management of investment funds, *Harvard Business Review* **43**, 63–75.

## **Related Articles**

#### **Capital Asset Pricing Model**; **Performance Measures**; **Sharpe, William F**.

GORDON J. ALEXANDER & ALEXANDRE M. BAPTISTA
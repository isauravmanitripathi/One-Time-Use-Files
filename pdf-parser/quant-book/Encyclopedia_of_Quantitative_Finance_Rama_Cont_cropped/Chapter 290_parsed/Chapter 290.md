# **Kelly Problem**

Consider a financial market with  $K$  assets whose prices  $P_i(t), i = 1, \ldots, K$  are stochastic, dynamic processes, and a risk-free asset whose price is  $P_0(t)$ . The vector of prices at time  $t$  is

$$\mathbf{P}(t) = (P_0(t), P_1(t), \dots, P_K(t))' \tag{1}$$

If the prices are given at points in time  $t_1$  and  $t_2$ , with  $t_1 < t_2$ , then the rate of return over that time on a unit of capital invested in asset  $i$  is

$$R_i(t_1, t_2) = \frac{P_i(t_2)}{P_i(t_1)} = 1 + r_i(t_1, t_2), i = 0, \dots K$$
(2)

When there are dividends  $D_i$  accrued in the time interval, then the return is  $R_i(t_1, t_2) = (P_i(t_2) +$  $D_i(t_2-t_1)/P_i(t_1)$ .

Suppose an investor has  $w_t$  units of capital at time  $t$ , and that capital is fully invested in the assets, with the proportions invested in each asset given by  $x_i(t), i = 0, \dots K$ , where  $\sum_{i=0}^{K} x_i(t) = 1$ . Then an investment or trading strategy at time  $t$  is the vector process

$$\mathbf{X}(t) = (x_0(t), x_1(t), \dots, x_K(t))'$$
 (3)

Given the investments  $w_{t_1}X(t_1)$  at time  $t_1$ , the accumulated capital at time  $t_2$  is

$$W(t_2) = w_{t_1} R'(t_1, t_2) X(t_1) = w_{t_1} \sum_{i=0}^{K} R_i(t_1, t_2) x_i(t_1)$$
(4)

The trajectory of returns between time  $t_1$  and time  $t_2$  depends on the asset, and is typically nonlinear. So changing the investment strategy at points in time between  $t_1$  and  $t_2$  will possibly improve capital accumulation. If trades could be timed to correspond to highs and lows in prices, then greater capital would be accumulated. To consider the effect of changes in strategy, partition the time interval into  $n$  segments, with  $d = \frac{t_2 - t_1}{n}$ , so that the accumulated capital is monitored, and the investment strategy is possibly revised at times  $t_1, t_1 + d, \ldots, t_1 + nd = t_2$ . Then

wealth at time  $t_2$  is

$$W_n(t_2) = w_{t_1} \prod_{i=0}^{n-1} R'(t_1 + id, t_1 + (i+1)d)$$
$$\times X(t_1 + id) \qquad (5)$$

Alternatively, wealth is

$$W_n(t_2) = w_{t_1} \left( \exp\left[\frac{1}{n} \sum_{i=0}^{n-1} \ln(R'(t_1 + id, t_1 + id, t_1)) + (i+1)dX(t_1 + id) \right] \right)^n$$
 (6)

The exponential form highlights the growth rate with the strategy  $\mathbf{X} = (X(t_1), \dots, X(t_1 + (n-1)d)),$ 

$$G_n(X) = \frac{1}{n} \sum_{i=0}^{n-1} \ln(R'(t_1 + id, t_1 + (i+1)d))$$
$$\times X(t_1 + id)$$
(7)

As the partitioning of the interval gets finer, so that  $d \rightarrow 0$ , then monitoring and trading are continuous. If d is fixed and the random variables  $V_i = \ln(R'(t_1 +$  $id, t_1 + (i + 1)d)X(t_1 + id), i = 0, \ldots, n - 1$  are independent and identically distributed (i.i.d.) with mean  $\mu_d$  and variance  $\sigma_d^2$ , then  $S_n(t_2) = (1/(\sigma_d \sqrt{n}))$  $\sum (V_i - \mu_d)$  converges as *n* increases (i.e, as  $t_2$ increases) to a standard normal variable. The simplest continuous time process with normally distributed accumulations is the Brownian motion model. In the continuous case, therefore, it is usually assumed that the instantaneous returns  $dP_i(t)/P_i(t)$  are approximated by Brownian motion.

If the distribution of accumulated capital (wealth) at the horizon is the criterion for deciding on an investment strategy, then the rate of growth of capital becomes the determining factor when the horizon is distant. For fixed d and i.i.d  $V_i$ , the growth rate converges to the mean growth rate as  $n$  increases, so considering the average growth rate between  $t_1$  and  $t_2$ , for strategy  $\mathbf{X} = (X(t_1), \ldots, X(t_1 + (n-1)d)),$ 

$$E[G_n(X)] = \frac{1}{n} \sum_{i=0}^{n-1} E[\ln(R'(t_1 + id, t_1 + (i+1)d) \times X(t_1 + id))]$$
(8)

| Feature      | Property                                                                                                                                                                                                                            | Reference                                           |  |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--|
|              | Maximizes the asymptotic rate of growth                                                                                                                                                                                             | Algeot and Cover [1] and Brieman [3]                |  |
|              | Maximizes median log wealth                                                                                                                                                                                                         | Ethier $[5]$                                        |  |
| Good         | Minimizes expected time to asymptotically large<br>goals                                                                                                                                                                            | Algeot and Cover [1], Brieman [3] and<br>Browne [4] |  |
|              | Never risks ruin                                                                                                                                                                                                                    | Hakansson and Miller [8]                            |  |
|              | Kelly is the unique evolutionary strategy                                                                                                                                                                                           | Hens and Schenk-Hoppe [9]                           |  |
|              | It takes a long time to outperform other strategies<br>with high probability                                                                                                                                                        | Aucamp [2]; Browne [4] and Thorp [13]               |  |
| $\text{Bad}$ | The total amount invested swamps the gains                                                                                                                                                                                          | Ethier and Tavare [6]; Griffin [7]                  |  |
|              | The average return converges to half the return from<br>optimal expected wealth                                                                                                                                                     | Ethier and Tavare [6]; Griffin [7]                  |  |
|              | Kelly strategy does not optimize the expected<br>nonlogarithmic utility of wealth. Example:<br>Bernoulli trials with $1/2 < p < 1$ , and $u(w) = w$ .<br>Then $x = 1$ maximizes $u(w)$ , but $x = 2p - 1$<br>maximizes $E[\ln(w)].$ | Samuelson [11]; Thorp [12]                          |  |

**Table 1** Some good and bad properties of the optimal capital growth strategy

where  $E$  denotes the expected value.

The case usually discussed is the one in which the incremental returns are serially independent. So the maximization of  $E[G_n(X)]$  is

$$\max \left\{ E[\ln(R'(t_1+id,t_1+(i+1)d)X(t_1+id))] \right\}$$
(9)

separately for each  $i$ . If the distribution of the returns is the same for each  $i$ , a fixed strategy holds over time.

The strategy that solves equation  $(9)$  subject to the normalization constraint is called the Kelly or *optimal capital growth strategy*. This strategy is the unique evolutionary stable strategy, in the sense that it asymptotically overwhelms other portfolio rules that may be used within the population of investors with the accumulated wealth criterion. Strategies that survive in the long run must converge to the optimal growth strategy [9]. In the case of a stationary returns distribution, the Kelly or log optimal portfolio is  $X^{*'} = (x_0^*, \tilde{X}^{*'})$ , where  $x_0^* = 1 - \sum_{i=1}^K x_i^*$ . This Kelly strategy is a *fixed mix*. In other words, the fraction of wealth invested in assets is determined by  $X^*$ , but rebalancing is required to maintain the fractions as wealth varies.

The optimal growth/Kelly strategy has been studied extensively. A list of some of its properties is given in Table 1.

A variation on the Kelly strategy is the fractional Kelly strategy defined as  $\tilde{X}_f = f\tilde{X}^*, f \ge 0$ . The fractional Kelly strategy has the same distribution of wealth across risky assets as the Kelly, but varies the fraction of wealth invested in those risky assets. Table 2 gives an example of the gain in security and the loss in return from a half-Kelly strategy. The results are from a simulation [15] assuming initial wealth of \$1000 and 700 decision points for investing in five possible assets, each with expected return of 1.14.

Observe that the Kelly strategy has enormous returns most of the time, but it is possible to make  $700$  independent bets, all with a  $14\%$  advantage at differing odds, and lose 98% of one's fortune. So the Kelly strategy, which is used by many great investors (see  $[14]$ ) is risky in the short term because the absolute Arrow-Pratt risk aversion index is almost zero; it is also risky in the long term and must be used with care.

<table>

 **Table 2** Performance of Kelly and half-Kelly strategies

| Final wealth statistic           | Kelly<br>18 | Half-Kelly<br>145 |
|----------------------------------|-------------|-------------------|
| Minimum                          |             |                   |
| Maximum                          | 483 883     | 111 770           |
| Mean                             | 48 135      | 13 069            |
| Median                           | 17 269      | 8043              |
| Probability of exceeding 500     | 0.916       | 0.990             |
| Probability of exceeding 1000    | 0.870       | 0.945             |
| Probability of exceeding 10 000  | 0.598       | 0.480             |
| Probability of exceeding 50 000  | 0.302       | 0.03              |
| Probability of exceeding 100 000 | 0.166       | 0.001             |

## **References**

- [1] Algeot, P. & Cover, T.M. (1988). Asymptotic optimality and asymptotic equipartition properties of log-optimum investment, *Annals of Probability* **16**, 876–898.
- [2] Aucamp, D. (1993). On the extensive number of plays to achieve superior performance with the geometric mean strategy, *Management Science* **39**, 1163–1172.
- [3] Brieman, L. (1961). Investment policies for expanding business optimal in a long-run sense, *Naval Research Logistics Quarterly* **7**, 647–651.
- [4] Browne, S. (1998). The return on investment from proportional portfolio strategies, *Advances in Applied Probability* **30**, 216–238.
- [5] Ethier, S.N. (2004). The Kelly system maximizes median fortune, *Journal of Applied Probability* **41**, 1230–1236.
- [6] Ethier, S.N. & Tavare, S. (1983). The proportional bettor's return on investment, *Journal of Applied Probability* **20**, 563–573.
- [7] Griffin, P. (1985). Different measures of win rates for optimal proportional betting, *Management Science* **30**, 1540–1547.
- [8] Hakansson, N. & Miller, B. (1975). Compound-return mean-variance efficient portfolios never risk ruin, *Management Science* **22**, 391–400.
- [9] Hens, T. & Schenk-Hoppe, K. (2005). Evolutionary stability of portfolio rules in incomplete markets, *Journal of Mathematical Economics* **41**, 43–66.
- [10] Kelly, J. (1956). A new interpretation of information rate, *Bell System Technology Journal* **35**, 917–926.
- [11] Samuelson, P.A. (1971). The fallacy of maximizing the geometric mean in long sequences of investing or gambling, *Proceedings of National Academy of Science* **68**, 2493–2496.
- [12] Thorp, E.O. (1971). Portfolio choice and the Kelly criterion, in *Proceedings of the Business and Economics Section of the American Statistical Association*, pp. 215–224.

- [13] Thorp, E.O. (2006). The Kelly criterion in blackjack, sports betting, and the stock market, in *Handbook of Asset and Liability Management*, *Theory and Methods*, S.A. Zenios & W.T. Ziemba, eds, North-Holland, Vol. 1, pp. 406–427.
- [14] Ziemba, W.T. (2005). The symmetric downside-risk Sharpe ratio and the evaluation of great investors and speculators, *Journal of Portfolio Management* Fall, 108–122.
- [15] Ziemba, W.T. & Hausch, D.B. (1986). *Betting at the Racetrack*, Dr. Z Investments, Inc., San Luis Obupo, CA.

## **Further Reading**

- Bell, R.M. & Cover, T.M. (1980). Competitive optimality of logarithmic investment, *Mathematics of Operations Research* **5**, 161–166.
- MacLean, L.C., Ziemba, W.T. & Blazenko, G. (1992). Growth versus security in dynamic investment analysis, *Management Science* **38**, 1562–1585.
- Rotando, L.M. & Thorp, E.O. (1992). The Kelly criterion and the stock market, *American Mathematical Monthly*, December, 922–931.
- Stutzer, M. (2003). Portfolio choice with endogenous utility: a large deviations approach, *Journal of Econometrics* **116**, 365–386.

## **Related Articles**

#### **Expected Utility Maximization**; **Fixed Mix Strategy**; **Sharpe Ratio**.

#### LEONARD C. MACLEAN & WILLIAM T. ZIEMBA
![](_page_0_Picture_0.jpeg)

 $\bullet$  he portfolio management process allocates trading capital among the best available trading strategies. These allocation decisions are made with a two-pronged goal in mind:

- 1. Maximize returns on total capital deployed in the trading operation.
- 2. Minimize the overall risk.

High-frequency portfolio management tasks can range from instantaneous decisions to allocate capital among individual trading strategies to weekly or monthly portfolio rebalancing among groups of trading strategies. The groups of trading strategies can be formed on the basis of the methodology deployed (e.g., event arbitrage), common underlying instruments (e.g., equity strategies), trading frequency (e.g., one hour), or other common strategy factors. One investment consultant estimates that most successful funds run close to 25 trading strategies at any given time; fewer strategies provide insufficient risk diversification, and managing a greater number of strategies becomes unwieldy. Each strategy can, in turn, simultaneously trade anywhere from one to several thousands of financial securities.

This chapter reviews modern academic and practitioner approaches to high-frequency portfolio optimization. As usual, effective management begins with careful measurement of underlying performance; distributions of returns of strategies composing the overall portfolio are the key inputs into the portfolio optimization. This chapter discusses the theoretical underpinnings of portfolio optimization once the distributions of returns of the underlying strategies have been estimated. It begins with a review of classical portfolio theory and proceeds to consider the latest applications in portfolio management.

### **ANALYTICAL FOUNDATIONS OF PORTFOLIO OPTIMIZATION**

#### **Graphical Representation of the Portfolio Optimization Problem**

The dominant focus of any portfolio management exercise is minimizing risks while maximizing returns. The discipline of portfolio optimization originated from the seminal work of Markowitz (1952). The two dimensions of a portfolio that he reviewed are the average return and risk of the individual securities that compose the portfolio and of the portfolio as a whole. Optimization is conducted by constructing an "efficient frontier," a set of optimal risk-return portfolio combinations for the various instruments under consideration. In the absence of leveraging opportunities (opportunities to borrow and increase the total capital available as well as opportunities to lend to facilitate leverage of others), the efficient frontier is constructed as follows:

**1.** For every possible combination of security allocations, the risk and return are plotted on a two-dimensional chart, as shown in Figure 14.1. Due to the quadratic nature of the risk function, the resulting chart takes the form of a hyperbola.

![](_page_1_Figure_6.jpeg)

**FIGURE 14.1** Graphical representation of the risk-return optimization constructed in the absence of leveraging opportunities. The bold line indicates the efficient frontier.

- **2.** The points with the highest level of return for every given level of risk are selected as the efficient frontier. The same result is obtained if the frontier is selected as the set of points with the lowest level of risk for every given level of return. The bold segment highlights the efficient frontier.
- **3.** An individual investor then selects a portfolio on the efficient frontier that corresponds to the investor's risk appetite.

In the presence of leveraging, the efficient frontier shifts dramatically upward to a straight line between the lending rate, approximated to be risk free for the purposes of high-level analysis, and the "market" portfolio, which is a portfolio lying on a line tangent to the efficient frontier of Figure 14.2. Figure 14.2 shows the resulting efficient frontier.

An interpretation of the efficient frontier in the presence of the leverage rate *RF* proceeds as follows. If an investor can lend a portion of his wealth at the rate *RF* to high-grade borrowers, he can reduce the risk of his overall portfolio by reducing his risk exposure. The lending investor then ends up on the bold line between *RF* and the market portfolio point (σ *<sup>M</sup>*, *RM*). The investor incurs two advantages by lending compared with selecting a portfolio from the efficient set with no lending as represented in Figure 14.1:

**1.** The investor may be able to attain lower risk than ever possible in the no-lending situation.

![](_page_2_Figure_6.jpeg)

**FIGURE 14.2** Graphical representation of the risk-return optimization constructed in the presence of leveraging opportunities. All leveraging is assumed to be conducted at the risk-free rate *RF*. The bold line indicates the efficient frontier. The point (σ *<sup>M</sup>*, *RM*) corresponds to the "market portfolio" for the given *RF* and the portfolio set.

**2.** With lending capabilities, the investor's return gets scaled linearly to his scaling of risk. In the no-lending situation, the investor's return decreases faster than the investor's decrease in risk.

Similarly, an investor who decides to borrow to increase the capital of his portfolio ends up on the efficient frontier but to the right of the market portfolio. The borrowing investor, too, enjoys the return, which increases linearly with risk and is above the no-borrowing opportunity set.

#### **Core Portfolio Optimization Framework**

Analytical estimation of the efficient frontier requires an understanding of the returns delivered by the strategies making up the portfolio. The return of each strategy *i* is measured as a simple average return over the time period *t* ∈ [1,..., *T*],

$$\overline{R}_{i} = \frac{1}{T} \sum_{t=1}^{T} R_{it} \tag{14.1}$$

where *Rit* is the return of strategy *i* in time period *t*, *t* ∈ [1,..., *T*]. The annualized risk of each strategy *i*, σ*<sup>i</sup>* <sup>2</sup> is often measured as a variance *Vi*, a square of the standard deviation:

$$V_i = \frac{1}{T - 1} \sum_{t=1}^{T} (R_{it} - \overline{R}_i)^2$$
(14.2)

Note that in computation of the average return, *Ri*, the sum of returns is divided by the total number of returns, *T*, whereas in computation of the risk in equation (14.2), the sum of squared deviations from the mean is divided by *T* − 1 instead. The *T* − 1 factor reflects the number of "degrees of freedom" used in the computation of *Vi*. Every statistical equation counts every independent variable (a raw number) as a degree of freedom; at the same time, every estimate used in the statistical equation reduces the number of degrees of freedom by 1. Thus, in the estimation of *Ri*, the number of independent variables is *T*, while in the estimation of *Vi*, the number of independent variables is reduced by 1 since the equation (14.2) uses *Ri*, an estimate itself.

The sample frequency of time period *t* should match the frequency intended for the analysis. In developing high-frequency trading frameworks, it may be desirable to make all the inferences from returns at very high intra-day frequencies—for example, a minute or a second. For investor relations purposes, daily or even monthly frequency of returns is often sufficient.

If the portfolio comprises  $I$  strategies, each represented by a proportion  $x_i$  within the portfolio, and each with the average annualized return of  $\overline{R}_i$  and risk of  $V_i$ , the total risk and return of the portfolio can be determined as follows:

$$E[R_p] = \sum_{i=1}^{I} x_i E[R_i]$$
(14.3)

$$V[R_p] = \sum_{i=1}^{I} \sum_{j=1}^{i} x_i x_j \operatorname{cov}[R_i, R_j]$$
(14.4)

where  $x_i$  is the proportion of the portfolio capital allocated to the strategy *i* at any given time,  $E[R_p]$  and  $E[R_i]$  represent respective average annualized returns of the combined portfolio and of the individual strategy  $i$ , and  $\text{cov}[R_i, R_j]$  is the covariance between returns of strategy i and returns of strategy  $j$ :

$$\text{cov}[R_i, R_j] = \rho_{ij} V_i^{0.5} V_j^{0.5} = E[R_i] E[R_j] - E[R_i R_j]$$
(14.5)

Additionally, the optimal portfolio should satisfy the following constraint: the sum of all allocations  $x_i$  in the portfolio should add up to 100 percent of the portfolio:

$$\sum_{i=1}^{I} x_i = 1 \tag{14.6}$$

Note that the formulation  $(14.6)$  allows portfolio weights of individual securities  $\{x_i\}$  to be all real numbers, both positive and negative. Positive numbers denote long positions, while negative numbers denote short positions.

The basic portfolio optimization problem is then specified as follows:

$$\min V[R_p], \text{ s.t. } E[R_p] \ge \mu, \sum_{i=1}^{I} x_i = 1 \tag{14.7}$$

where  $\mu$  is the minimal acceptable average return.

For a trading operation with the coefficient of risk aversion of λ, the mean-variance optimization framework becomes the one shown in equation (14.8):

$$\max \sum_{t=1}^{T} \left( E[R_{p,t}] - \lambda V[R_{p,t}] \right), \ \sum_{i=1}^{I} x_i = 1 \tag{14.8}$$

The value of the objective function of equation (14.8) resulting from the optimization can be interpreted as "value added" to the particular investor with risk aversion of λ. The risk aversion parameter λ is taken to be about 0.5 for very risk-averse investors, 0 for risk-neutral investors, and negative for risk-loving investors.

Furthermore, when the trading operation is tasked with outperforming a particular benchmark, µ, the optimization problem is reformulated as follows:

$$\max \sum_{t=1}^{T} \left( E[R_{p,t}] - \lambda V[R_{p,t}] \right), \text{ s.t. } \sum_{t=1}^{T} E[R_{p,t}] \ge \mu, \sum_{i=1}^{I} x_i = 1 \qquad (14.9)$$

#### **Portfolio Optimization in the Presence of Transaction Costs**

The portfolio optimization model considered in the previous section did not account for transaction costs. Transaction costs, analyzed in detail in Chapter 19, decrease returns and distort the portfolio risk profile; depending on the transaction costs' correlation with the portfolio returns, transaction costs may increase overall portfolio risk. This section addresses the portfolio optimization solution in the presence of transaction costs.

The trading cost minimization problem can be specified as follows:

$$\min_{\substack{s.t. V[TC] \le K}} E[TC] \tag{14.10}$$

where *E*[*TC*] is the average of observed trading costs, *V*[*TC*] is the variance of observed trading costs, and *K* is the parameter that specifies the maximum trading cost variance. Changing the parameter *K* allows us to trace out the "efficient trading frontier," a collection of minimum trading costs for each level of dispersion of trading costs.

Alternatively, given the risk-aversion coefficient λ of the investor or portfolio manager, the target trading cost strategy can be determined from the following optimization:

$$\min E[TC] + \lambda V[TC] \tag{14.11}$$

Both the efficient trading frontier and the target trading cost scenario can be used as benchmarks to compare execution performance of individual traders and executing broker-dealers. However, the cost optimization by itself does not answer the question of portfolio optimization in the presence of trading costs.

Engle and Ferstenberg (2007) further propose an integrative framework for portfolio and execution risk decisions. Using  $x_{it}$  to denote the proportion of the total portfolio value allocated to the security  $i$  at the end of period t,  $p_{it}$  to denote the price of security i at the end of period t, and  $c_t$  to denote the cash holdings in the portfolio at the end of period t, Engle and Ferstenberg (2007) specify the portfolio value at the end of period t as follows:

$$y_t = \sum_{i=1}^{I} x_{it} p_{it} + c_t \qquad (14.12)$$

If the portfolio rebalancing happens at the end of each period, the oneperiod change in the portfolio value from time  $t$  to time  $t + 1$  is then

$$\Delta y_{t+1} = y_{t+1} - y_t = \sum_{i=1}^{I} x_{i,t} (p_{i,t+1} - p_{it}) + \sum_{i=1}^{I} (x_{i,t+1} - x_{it}) p_{i,t+1} + (c_{t+1} - c_t)$$
$$= \sum_{i=1}^{I} x_{i,t} \Delta p_{i,t+1} + \sum_{i=1}^{I} \Delta x_{i,t+1} p_{i,t+1} + \Delta c_{t+1} \tag{14.13}$$

If the cash position bears no interest and there are no dividends, the change in the cash position is strictly due to changes in portfolio composition executed at time t at transaction prices  $\tilde{p}_{it}$  for each security i:

$$\Delta c_{i,t+1} = -\sum_{i=1}^{I} \Delta x_{i,t+1} \tilde{p}_{i,t+1} \tag{14.14}$$

The negative sign on the right-hand side of equation  $(14.14)$  reflects the fact that the increase in the holding position of security *i*,  $\Delta x_{it}$  results in a decrease of cash available in the portfolio. Combining equations  $(14.13)$  and  $(14.14)$  produces the following specification for the changes in the portfolio at time  $t$ :

$$\Delta y_{t+1} = \sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} + \sum_{i=1}^{I} \Delta x_{i,t+1} (p_{i,t+1} - \tilde{p}_{i,t+1}) = \sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} - T C_{t+1}$$
(14.15)

where  $\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1}$  is the change in portfolio value due to the active portfolio management and  $\sum_{i=1}^{I} \Delta x_{i,t+1}(p_{i,t+1} - \tilde{p}_{i,t+1})$  is due to trading costs.

Specifically,  $\sum_{i=1}^{I} \Delta x_{i,t+1}(p_{i,t+1} - \tilde{p}_{i,t+1})$  would equal 0 if all the trades were executed at their target prices,  $p_{i,t+1}$ .

The combined portfolio optimization problem in the presence of risk aversion  $\lambda$ , max  $E[\Delta y_{t+1}] - \lambda V[\Delta y_{t+1}]$ , can then be rewritten as follows for each period  $t+1$ :

$$\max E\left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} - T C_{t+1}\right] - \lambda V \left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} - T C_{t+1}\right] \quad (14.16)$$

where  $TC_t = \sum_{i=1}^I \Delta x_{it}(p_{it} - \tilde{p}_{it}), \ \Delta x_{it}$  is the one-period change in portfolio weight of security *i*,  $p_{it}$  is the target execution price for trading of security i at the end of period t, and  $\tilde{p}_{it}$  is the realized execution price for security  $i$  at the end of period  $t$ .

In addition, the interaction between transaction costs and portfolio allocations can be captured as follows:

$$V\left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} - T C_{t+1}\right] = V\left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1}\right]$$
$$+ V\left[T C_{t+1}\right] - 2 \operatorname{cov}\left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1}, T C_{t+1}\right] \tag{14.17}$$

The resulting Sharpe ratio of the portfolio can be ex-ante computed as follows:

Sharpe ratio 
$$= \frac{E\left[\sum_{i=1}^{I} x_{i} \Delta p_{i} - TC\right] - R^{f}}{\sqrt{T} \sqrt{V\left[\sum_{i=1}^{I} x_{it} \Delta p_{i,t+1} - TC_{t+1}\right]}}$$
(14.18)

#### Portfolio Diversification with Asymmetric Correlations

The portfolio optimization frameworks discussed previously assume that the correlations between trading strategies behave comparably in rising and falling markets. Ang and Chen  $(2002)$ , however, show that this does not have to be the case; the authors document that correlation of equity returns often increases in falling markets, likely distorting correlations of trading strategies used in trading portfolios. Explicit modeling of time-varying correlations of portfolio strategies may refine portfolio estimation and generate more consistent results.

One way to model correlations is to follow the methodology developed by Ang and Chen (2002). The authors' methodology is based on examining the distribution of correlations of returns: if correlations behave normally, they are symmetrical; the correlations accompanying extreme negative returns are equal to the correlations accompanying extreme positive returns. Any asymmetry in correlations of extreme returns should be incorporated in portfolio management solutions.

#### **Dealing with Estimation Errors in Portfolio Optimization**

All portfolio optimization exercises involve estimates of average returns, return variances, and correlations. The classic Markowitz (1952) methodology takes the estimated parameters as true distributional values and ignores the estimation error. Frankfurter, Phillips, and Seagle (1971); Dickenson (1979); and Best and Grauer (1991), among others, point out that the estimation errors distort the portfolio selection process and result in poor out-of-sample performance of the complete portfolio.

A common way to overcome estimation errors is to learn from them. A mechanism known as the Bayesian approach proposes that the system learns from its own estimation mistakes by comparing its realized performance with its forecasts. The portfolio optimization system then corrects its future estimates based on its own learnings. In a purely systematic environment, the self-correction process happens without any human intervention. The Bayesian self-correction mechanism is often referred to as a "genetic algorithm."

In the Bayesian approach, the average return estimate of a particular security is considered to be a random variable and is viewed probabilistically in the context of previously obtained information, or priors. All expectations are subsequently developed with respect to the distribution obtained for the estimate. Multiple priors, potentially representing multiple investors or analysts, increase the accuracy of the distribution for the estimate.

Under the Bayesian specification, all mean and variance-covariance estimates are associated with a confidence interval that measures the accuracy of the forecast. An accurate forecast has a tight confidence interval, while the inaccurate forecast has a wide confidence interval. After the accuracy of the previous forecast has been determined, the portfolio weight of a security is scaled depending on the width of the confidence intervals of these securities. The wider the confidence intervals for parameter estimates, the smaller the portfolio weight for that security. When the confidence intervals approach 0, the weights are similar to those of the classic mean-variance optimization.

The traditional Bayesian approach, applied to mean-variance optimization by Jorion  $(1986)$ , works as follows: both mean and variance estimates computed on a contemporary data sample are adjusted by lessons gleaned from historical (prior) observations.

The dispersion of the distributions of the true mean and variance of the distributions shrink as more observations are collected and analyzed with time. If  $R_{n,t}$  is the portfolio return following the mean-variance optimization of equation (14.7) from time  $t-1$  to time t, and  $\hat{E}[R_{i,t}]$  is the average return estimate for security *i*,  $\hat{E}[R_{i,t}] = \frac{1}{t} \sum_{\tau=1}^{t} R_{i,\tau}$ , the "Bayes-Stein shrinkage estimators" for expected return and variance of an individual security  $i$  to be used in the mean-variance optimization for the next period  $t+1$ , are computed as follows:

$$\begin{aligned} E[R_{i,t+1}]_{BS} &= (1 - \phi_{i,BS})\hat{E}[R_{i,t}] + \phi_{i,BS}R_{p,t} \\ V[R_{i,t+1}]_{BS} &= V[R_{i,t}]\left[1 + \frac{1}{t+\nu}\right] + \frac{\nu}{t(t+1+\nu)}V[R_{i,t}] \end{aligned}$$

where  $v$  is the precision of the mean estimates:  $v = \frac{(N-2)}{t} \frac{V[R_{i,t}]}{(R_{p,t} - \hat{E}[R_{i,t}])^2}$ ,  $N$  is the number of observations in the sample at time t, and  $\phi_{BS}$  is the shrinkage factor for the mean:  $\phi_{BS} = \frac{v}{t+v}$ . The case of zero precision  $(v=0)$  corresponds to completely diffuse estimates.

Some investors feel particularly strongly about the accuracy of a forecast and would prefer to exclude systems generating inaccurate or ambiguous forecasts from their trading tool belt. Garlappi, Uppal, and Wang  $(2007)$ propose a Bayesian portfolio allocation methodology for such investors. An ambiguity-averse investor may be one who relies on multiple information sources and prefers to trade a particular financial security only when those information sources are in agreement about the future movement of that security. This ambiguity aversion is different from risk aversion. Risk aversion measures the investor's tolerance for variance in returns measured after the trades have been executed, or ex-post, whereas ambiguity aversion measures the investor's tolerance for dispersion in the trade outcome forecasts before any trades have been executed, or ex-ante.

To specify the ambiguity aversion, Garlappi, Uppal, and Wang (2007) add the following constraint to the standard mean-variance optimization:  $f(E[R], \hat{E}[R], V[R]) \leq \varepsilon$ , where f is the uncertainty about forecasts of expected returns, and  $\varepsilon$  is the investor's maximum tolerance for such uncertainty:

$$f(E[R], \hat{E}[R], V[R]) = \frac{(E[R] - \hat{E}[R])^2}{V[R]/T} \tag{14.19}$$

where  $T$  is the number of observations in the sample.

The optimization problem of equation (14.7) over a one-period horizon and multiple assets now becomes:

$$\max(E[R] - \lambda V[R]), \text{ s.t. } \sum_{i=1}^{I} x_i = 1, \ E[R] \ge \mu, \ f(E[R], \hat{E}[R], V[R]) \le \varepsilon$$
(14.20)

Garlappi, Uppal, and Wang (2007) show that the optimization of equation (14.20) can be rewritten as follows:

$$\max(E[R] - \lambda V[R] - \sqrt{\xi V[R]}), \text{ s.t. } \sum_{i=1}^{I} x_i = 1 \tag{14.21}$$

where ξ specifies the multi-asset aversion to ambiguity:

$$(\hat{E}[R] - E[R])'V[R](\hat{E}[R] - E[R]) \le \xi \tag{14.22}$$

The methodology presented here documents analytical approaches to portfolio optimization. The following sections discuss practical approaches to the estimation of portfolio optimization problems defined previously as well as to other aspects of effective portfolio management in high-frequency trading operations.

### **EFFECTIVE PORTFOLIO MANAGEMENT PRACTICES**

Effective practical portfolio management involves making the following key decisions:

- **1.** How much leverage is appropriate within the portfolio?
- **2.** What proportion of the portfolio should be invested into which trading strategy?

This section presents best-practices answers for each of these questions.

## **How Much Leverage Is Appropriate within the Portfolio?**

Two methodologies, option-based portfolio insurance (OBPI) and constant proportion portfolio insurance (CPPI), address the leverage component of the portfolio optimization process. Both methodologies require that a substantial proportion of the portfolio at any time be left in cash or invested in risk-free bonds. Each methodology determines exactly what proportion of the portfolio should be left in cash and what proportion should be levered and then invested into risky securities. The OBPI method is static in nature, while the CPPI allocation changes with changes in the market value of the overall portfolio.

- **1.** The OBPI methodology suggests that only a fixed proportion of the portfolio (e.g., *X* percent, *X* < 100 percent) be invested in risky instruments. The technique was first developed by Leland and Rubenstein (1976), who introduced the concept as options-based insurance. In Leland and Rubenstein (1976), the portfolio is structured to preserve (100 − *X*) percent of the original portfolio capital, while allowing the portfolio to benefit from the potential upside of the *X* percent of the portfolio invested in risky securities, such as options. Such portfolios are now commonly securitized and marketed as "structured products." The proportion of the portfolio *X* can be determined through the costbenefit analysis of option and bond prices versus expected probabilities of option payouts or, in high-frequency trading cases, the selling price of the option.
- **2.** CPPI is another popular portfolio allocation strategy that calls for dynamic adjustment of portfolio breakdown into cash and risky securities, unlike OBPI, in which the breakdown is static. Black and Jones (1987) and Perold and Sharpe (1988) created CPPI as an extension of OBPI that morphed into an automated method widely used by industry practitioners today.

CPPI works in accordance with the following steps:

- **1.** Management sets the absolute worst-case maximum drawdown, a floor for the market value of the portfolio. If the market value of the portfolio reaches the floor, the portfolio is fully liquidated into cash. Suppose that the maximum allowable drawdown is *L percent*.
- **2.** The "cushion" is the difference between the market value of the portfolio and the floor. A proportion of the cushion is levered and invested in risky securities. The exact proportion of the cushion invested in the risky instruments is determined by a "multiplier," *M*, set by management. Common multipliers range from 3 to 6.
- **3.** The risk capital allocated to the risky securities then becomes *M* × *Cushion*. As an illustration, suppose that the total capital allocated to a particular portfolio is \$100 million, with 10 percent being the absolute

maximum drawdown. The value of the cushion at this point is \$10 million. If the multiplier is set to 5 (*M* = 5), the maximum actively invested at-risk capital can be \$50 million. However, this \$50 million can be levered. Black and Jones (1987) and Perold and Sharpe (1988) assumed that the leverage ratio on the cushion stays constant during the whole life of the portfolio, leading to the "constant" term in CPPI. Modern CPPI strategies allow for dynamic leverage strategies that scale leverage down in adverse market conditions.

The CPPI allocation ensures that the portfolio always has enough cash to mitigate portfolio risks and to safeguard the investment principal. The portfolio is periodically rebalanced to reflect the current market value of the portfolio. The higher the market value of the portfolio, the more of its proportion is allocated to risky assets. Conversely, the lower the market value of the portfolio, the higher the proportion of the portfolio that is held in cash or in nearly risk-free fixed-income securities.

#### **What Proportion of the Portfolio Should Be Invested into Which Trading Strategy?**

After the performance of individual securities and trading strategies has been assessed and the best performers identified, the composition of the master portfolio is determined from the best-performing strategies. This step of the process is known as asset allocation and involves determining the relative weights of strategies within the master portfolio.

The easiest approach to portfolio optimization is to create an equally weighted portfolio of the best-performing strategies. Although the equally weighted framework diversifies the risk of the overall portfolio, it may not diversify the risk as well as a thorough portfolio optimization process. As the number of securities in the portfolio increases, however, determining the optimal weights for each security becomes increasingly complex and time-consuming—a real challenge in the high-frequency environment.

Several classes of algorithms have been proposed to simplify and speed up setting the optimal portfolio weights. Optimization algorithms fall into three classes:

**1.** The simultaneous equations framework is the algorithm that directly follows the Markowitz (1952) specification. It has been shown to be inefficient for optimization if the portfolio exceeds 10 strategies, and it may produce highly erroneous forecasts when 20 or more assets are involved. The forecast errors are due to the estimation errors that occur when the average returns and variances are computed. The Bayesian error-correction framework, discussed previously in this chapter, alleviates some of the input estimation errors. Still, in addition to the issues of forecast errors, the estimation time of this algorithm grows exponentially with the number of trading strategies involved, making this method hardly suitable for high-frequency trading of many assets.

- **2.** Nonlinear programming is a class of optimizers popular in commercial software. The nonlinear algorithms employ a variety of techniques with the objective of maximizing or minimizing the target portfolio optimization function given specified parameters such as portfolio allocation weights. Some of these algorithms employ a gradient technique whereby they analyze the slope of the objective function at any given point and select the fastest increasing or decreasing path to the target maximum or minimum, respectively. The nonlinear programming algorithms are equally sensitive to the estimation errors of the input means and variances of the returns. Most often, the algorithms are too computationally complex to be feasible in the high-frequency environments. A recent example of a nonlinear optimizer is provided by Steuer, Qi, and Hirschberger (2006).
- **3.** The critical line–optimizing algorithm was developed by Markowitz (1959) to facilitate the computation of his own portfolio theory. The algorithm is fast and comparatively easy to implement. Instead of providing point weights for each individual security considered in the portfolio allocation, the critical line optimizer delivers a set of portfolios on the efficient frontier, a drawback that has precluded many commercial companies from adapting this method. A recent algorithm by Markowitz and Todd (2000) addresses some of the issues. According to Niedermayer and Niedermayer (2007), the Markowitz and Todd (2000) algorithm outperforms the algorithm designed by Steuer, Qi, and Hirschberger (2006) by a factor of 10,000 for at least 2,000 assets considered simultaneously.

The existing algorithms, whatever the complexity and accuracy of their portfolio allocation outputs, may not be perfectly suited to the high-frequency trading environment. First, in environments where a delay of 1 second can result in a million-dollar loss, the optimization algorithms in their current form still consume too much time and system power. Second, these algorithms ignore the liquidity considerations pertinent to the contemporary trading settings; most of the transactions occur in blocks or "clips" of a prespecified size. Trades of larger-than-normal sizes as well as trades of smaller blocks incur higher transaction costs that in the high-frequency environment can put a serious strain on the system's profitability.

A simple high-frequency alternative to the complex optimization solutions is a discrete pair-wise (DPW) optimization developed by Aldridge (2009c). The DPW algorithm is a fast compromise between the equally weighted portfolio setting and a full-fledged optimization machine that outputs portfolio weights in discrete clips of the prespecified sizes. No fractional weights are allowed. The algorithm works as follows:

- **1.** Candidates for selection into the overall portfolio are ranked using Sharpe ratios and sorted from the highest Sharpe ratio to the lowest. This step of the estimation utilizes the fact that the Sharpe ratio itself is a measure of where each individual strategy lies on the efficient frontier.
- **2.** An even number of strategies with the highest Sharpe ratios are selected for inclusion into the portfolio. Half of the selected strategies should have historically positive correlations with the market, and half should have historically negative correlations with the market.
- **3.** After the universe of financial instruments is selected on the basis of the Sharpe ratio characteristics, all selected strategies are ranked according to their current liquidity. The current liquidity can be measured as the number of quotes or trades that have been recorded over the past 10 minutes of trading activity, for example.
- **4.** After all the strategies have been ranked on the basis of their liquidity, the pairs are formed through the following process: the two strategies within each pair have opposite historical correlation with the market. Thus, strategies historically positively correlated with the market are matched with strategies historically negatively correlated with the market. Furthermore, the matching should occur according to the strategy liquidity rank. The most liquid strategy positively correlated with the market should be matched with the most liquid strategy negatively correlated with the market, and so on until the least liquid strategy positively correlated with the market is matched with the least liquid strategy negatively correlated with the market. The liquidity-based matching ensures that the high-frequency dynamic captured by correlation is due to idiosyncratic movements of the strategy rather than the illiquidity conditions of one strategy.
- **5.** Next, for each pair of strategies, the high-frequency volatility of a portfolio of just the two strategies is computed for discrete position sizes in either strategy. For example, in foreign exchange, where a standard transactional clip is \$20 million, the discrete position sizes considered for the pair-wise optimization may be −\$60 million, −\$40 million, −\$20 million, 0, \$20 million, \$40 million, and \$60 million, where the minus sign indicates the short position. Once the volatility for the various portfolio combinations is selected within each pair of strategies, the positions with the lowest portfolio volatility are selected.

**6.** The resulting pair portfolios are subsequently executed given the maximum allowable allocation constraints for each strategy. The maximum long and short allocation is predetermined and constrained as follows: the cumulative gross position in each strategy cannot exceed a certain size, and the cumulative net position cannot exceed another, separately set, limit that is smaller than the aggregate of the gross limits for all strategies. The smaller net position clause ensures a degree of market neutrality.

The DWP algorithm is particularly well suited to high-frequency environments because it has the following properties:

- The DPW algorithm avoids the brunt of the impact of input estimation errors by reducing the number of strategies in each portfolio allocation decision.
- The negative historical correlation of input securities ensures that within each pair of matched strategies, the minimum variance will result in long positions in both strategies most of the time. Long positions in the strategies are shown to historically produce the highest returns per unit of risk, as is determined during the Sharpe ratio ranking phase. The times that the system results in short positions for one or more strategy are likely due to idiosyncratic market events.
- The algorithm is very fast in comparison with other portfolio optimization algorithms. The speed of the algorithm comes from the following "savings" in computational time:
  - If the total number of strategies selected in the Sharpe ratio ranking phase is 2*K*, the DPW algorithm computes only *K* correlations. Most other portfolio optimization algorithms compute correlation among every pair of strategies among the 2*K* securities, requiring 2*K*(*K* − 1) correlation computations instead.
  - The grid search employed in seeking the optimal portfolio size for each strategy within each portfolio pair optimizes only between two strategies, or in two dimensions. A standard algorithm requires a 2*K*-dimensional optimization.
  - Finally, the grid search allows only a few discrete portfolio weight values. In the main example presented here, there are seven allowable portfolio weights: −\$60 MM; −\$40 MM; −\$20 MM; 0; \$20 MM; \$40 MM; and \$60 MM. This limits the number of iterations and resulting computations from, potentially, infinity, to 72 = 49.

Alexander (1999) notes that correlation and volatility are not sufficient to ensure long-term portfolio stability; both correlation and volatility are typically computed using short-term returns, which only partially reflect dynamics in prices and necessitate frequent portfolio rebalancing. Instead, Alexander (1999) suggests that in portfolio optimization more attention should be paid to cointegration of constituent strategies. Auxiliary securities, such as options and futures, can be added into the portfolio mix based on cointegration analysis to further strengthen the risk-return characteristics of the trading operation. The cointegration-enhanced portfolios can work particularly well in trading operations that are tasked with outperforming specific financial benchmarks.

# **CONCLUSION**

Competent portfolio management enhances the performance of highfrequency strategies. Ultra-fast execution of portfolio optimization decisions is difficult to achieve but is critical in high-frequency settings.
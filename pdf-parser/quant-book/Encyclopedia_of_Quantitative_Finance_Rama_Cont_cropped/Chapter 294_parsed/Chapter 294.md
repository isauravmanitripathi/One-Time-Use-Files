## Robust Portfolio Optimization

Portfolio selection is the problem of allocating capital over a number of available assets in order to maximize the "return" on the investment while minimizing the "risk". Although the benefits of diversification in reducing risk have been appreciated since the inception of financial markets, Markowitz [25, 26] formulated the first mathematical model for portfolio selection. In the Markowitz portfolio selection model, the "return" on a portfolio is measured by the expected value of the random portfolio return, and the associated "risk" is quantified by the variance of the portfolio return. Markowitz showed that, given either an upper bound on the risk that the investor is willing to take or a lower bound on the return the investor is willing to accept, the optimal portfolio can be obtained by solving a convex quadratic programming problem. This mean-variance model has had a profound impact on the economic modeling of financial markets and the pricing of assets—the capital asset pricing model (CAPM) developed primarily by Sharpe [30], Lintner [22], and Mossin [28] was an immediate logical consequence of the Markowitz theory. In 1990, Sharpe and Markowitz shared the Nobel Memorial Prize in Economic Sciences for their work on portfolio allocation and asset pricing.

In spite of the theoretical success of the mean-vari ance model, practitioners have shied away from this model. The following quote from Michaud [27] summarizes the problem: "Although Markowitz efficiency is a convenient and useful theoretical framework for portfolio optimality, in practice it is an error prone procedure that often results in *error-maximized* and investment-irrelevant portfolios." This behavior is a reflection of the fact that solutions of optimization problems are often very sensitive to perturbations in the parameters of the problem; since the estimates of the market parameters are subject to statistical errors, the results of the subsequent optimization are not very reliable. Various aspects of this phenomenon have been extensively studied in the literature on portfolio selection. Chopra and Ziemba [8] study the cashequivalent loss from the use of estimated parameters instead of the true parameters. Broadie [5] investigates the influence of errors on the efficient frontier and Chopra [7] investigates the turnover in the composition of the optimal portfolio as a function of the estimation error (see also Part II of [31] for a summary of this research). Several studies have shown that imposing constraints on the portfolio weights in a mean-variance optimization problem leads to better out-of-sample performance [15, 16]. Practitioners have always imposed no short-sale constraints and/or bounds for each security to improve diversity. It is suggested that constraining portfolio weights may reduce volatility, increase realized efficiency, and decrease downside risk or shortfall probability. Jagannathan and Ma [19] provide theoretical justification for these observations. Michaud [27] suggests resampling the mean returns  $\mu$  and the covariance matrix  $\Sigma$  of the assets from a confidence region around a nominal set of parameters, and then aggregating the portfolios obtained by solving a Markowitz problem for each sample. Recently, scenario-based stochastic programming models have also been proposed for handling the uncertainty in parameters (see Part V of [31] for a survey of this research). Neither of the above two scenario based approaches provide any hard guarantees on the portfolio performance, and both become very inefficient as the number of assets grows.

Robust optimization is a deterministic optimization framework in which one explicitly models the parameter uncertainty, and the optimization problems are solved assuming worst-case behavior of these perturbations. This robust optimization framework was introduced in [3] for linear programming and in [2] for general convex programming [4]. There is also a parallel literature on robust formulations of optimization problems originating from robust control [10, 12] and  $[11]$ .

In order to clearly understand the main ideas underlying the robust portfolio selection approach, consider the following very simple model. Suppose the true (unknown) covariance matrix  $\Sigma$  and the true (unknown) mean return vector  $\boldsymbol{\mu}$  are known to lie in uncertainty sets

$$S_m = \left\{ \boldsymbol{\mu} : (\boldsymbol{\mu} - \boldsymbol{\mu}_0)^{\mathrm{T}} \boldsymbol{\Sigma}_0^{-1} (\boldsymbol{\mu} - \boldsymbol{\mu}_0) \leq \beta_1^2 \right\} \quad (1)$$

and

$$S_v = \{ \mathbf{\Sigma} : \|\mathbf{\Sigma} - \mathbf{\Sigma}_0\|_F \le \beta_2 \} \tag{2}$$

where  $\|\mathbf{A}\|_{F} = \text{Tr}(\mathbf{A}^T \mathbf{A})$ . The confidence regions associated with maximum likelihood estimates of the parameters  $(\mu, \Sigma)$  have precisely the ellipsoidal structure described above and these confidence regions may be used as the uncertainty sets. The robust portfolio selection problem corresponding to the uncertainty sets  $S_m$  and  $S_v$  is given by

$$\max_{\{\boldsymbol{\phi}: \mathbf{1}^{\mathrm{T}} \boldsymbol{\phi} = 1\}} \min_{\{\boldsymbol{\mu} \in S_m, \boldsymbol{\Sigma} \in S_v\}} \left\{ \boldsymbol{\mu}^{\mathrm{T}} \boldsymbol{\phi} - \tau \boldsymbol{\phi}^{\mathrm{T}} \boldsymbol{\Sigma} \boldsymbol{\phi} \right\} \qquad (3)$$

that is, the utility of holding a portfolio  $\boldsymbol{\phi}$  is the worstcase utility when the parameters are allowed to vary in their uncertainty sets. Thus, robust optimization implicitly assumes Knightian uncertainty, that is, the market parameters are assumed to be ambiguous.

For fixed  $\boldsymbol{\phi}$ , the solution of the inner minimization problem

$$\begin{aligned} \min_{\{\boldsymbol{\mu}\in S_m, \boldsymbol{\Sigma}\in S_v\}} \left\{ \boldsymbol{\mu}^{\mathrm{T}}\boldsymbol{\phi} - \tau\boldsymbol{\phi}^{\mathrm{T}}\boldsymbol{\Sigma}\boldsymbol{\phi} \right\} \\ = \boldsymbol{\mu}_0^{\mathrm{T}}\boldsymbol{\phi} - \beta_1\sqrt{\boldsymbol{\phi}^{\mathrm{T}}\boldsymbol{\Sigma}_0\boldsymbol{\phi}} - \tau\left(\boldsymbol{\phi}^{\mathrm{T}}(\boldsymbol{\Sigma}_0 + \beta_2\mathbf{I})\boldsymbol{\phi}\right) \end{aligned} \tag{4}$$

Thus, the robust portfolio selection problem is equivalent to

$$\max_{\{\boldsymbol{\phi}: \mathbf{1}^{\mathrm{T}} \boldsymbol{\phi} = 1\}} \left\{ \boldsymbol{\mu}_0^{\mathrm{T}} \boldsymbol{\phi} - \beta_1 \sqrt{\boldsymbol{\phi}^{\mathrm{T}} \boldsymbol{\Sigma}_0 \boldsymbol{\phi}} - \tau \left( \boldsymbol{\phi}^{\mathrm{T}} (\boldsymbol{\Sigma}_0 + \beta_2 \mathbf{I}) \boldsymbol{\phi} \right) \right\}$$
(5)

The objective function of this optimization problem can be reinterpreted in the following manner. The optimal portfolio  $\boldsymbol{\phi}^*$  is the optimal solution of the classical mean-variance optimization problem with

1. a perturbed mean vector:

$$\mu = \hat{\boldsymbol{\mu}} - \left(\frac{\beta_1}{\sqrt{(\boldsymbol{\phi}^*)^{\mathrm{T}}\boldsymbol{\Sigma}_0\boldsymbol{\phi}^*}}\right)\boldsymbol{\Sigma}_0\boldsymbol{\phi}^* \qquad (6)$$

that is, each component of the mean vector is adjusted to reduce the return on the portfolio  $\boldsymbol{\phi}^*$ , and

2. a perturbed covariance matrix

$$\mathbf{\Sigma} = \mathbf{\Sigma}_0 + \beta_2 \mathbf{I} \tag{7}$$

that is, the volatility of each of the assets is increased by an amount  $\beta_2$ .

Thus, the robust portfolio selection problem can be interpreted as a modification of the classical mean-variance optimization problem where the parameter values are dynamically adjusted to account for the uncertainty.

The optimization problem  $(5)$  can be reformulated as a second-order cone program (SOCP) (see [23] or [29] for details). This fact has important theoretical and practical implications. Since the computational complexity of an SOCP is comparable to that of a convex quadratic program, it follows that robust active portfolio selection is able to provide protection against parameter fluctuations at very moderate computational cost. Moreover, a number of commercial solvers such as MOSEK, CPLEX, and Frontline System (supplier of EXCEL SOLVER) provide the capability for solving SOCPs in a numerically robust manner.

The simple model described in the preceding text does not scale as the number of assets grows. At the very minimum, the data required to calculate the maximum likelihood estimate  $\Sigma_0$  grows as  $\mathcal{O}(n^2)$ , where  $n$  is the number of assets. Goldfarb and Iyengar [17] work with a robust factor model wherein the single period return  $\boldsymbol{r}$  is assumed to be a random variable given by

$$\boldsymbol{r} = \boldsymbol{\mu} + \boldsymbol{V}^{\mathrm{T}} \boldsymbol{f} + \boldsymbol{\varepsilon} \tag{8}$$

where  $\boldsymbol{\mu} \in \mathbf{R}^n$  is the vector of mean returns,  $f \sim$  $\mathcal{N}(\mathbf{0}, \mathbf{F}) \in \mathbf{R}^m$  is the vector of returns of the factors that drive the market,  $V \in \mathbf{R}^{m \times n}$  is the matrix of factor loadings of the *n* assets, and  $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{D})$  is the vector of residual returns. For a detailed discussion of appropriate uncertainty sets for the parameters  $\mu$ ,  $V, F$ , and  $D$  and methods used to parameterize these sets from data, see Section 6 in [17].

Halldórsson and Tütüncü [18] show that if the uncertain mean return vector  $\mu$  and the uncertain covariance matrix  $\Sigma$  of the asset returns  $r$  belong to the component-wise uncertainty sets  $S_m = \{\boldsymbol{\mu} : \boldsymbol{\mu}^{\tilde{L}} \leq$  $\boldsymbol{\mu} \leq \boldsymbol{\mu}^{U}$  and  $S_{v} = \{\boldsymbol{\Sigma} : \boldsymbol{\Sigma} \succeq 0, \boldsymbol{\Sigma}^{L} \leq \boldsymbol{\Sigma} \leq \boldsymbol{\Sigma}^{U}\},$ respectively, the robust problem reduces to a nonlinear saddle-point problem that involves semidefinite constraints. Here  $\mathbf{A} \succeq 0$  (respectively  $\succ 0$ ) denotes that the matrix  $\mathbf{A}$  is symmetric and positive semidefinite (respectively definite). This approach has several shortcomings when applied to practical problems—the model is not a factor model (in applied work, factor models are popular because of the econometric relevance of the factors), no procedure is provided for specifying the extreme values  $(\boldsymbol{\mu}^L, \boldsymbol{\mu}^U)$ , and  $(\mathbf{\Sigma}^L, \mathbf{\Sigma}^U)$  defining the uncertainty structure and,

moreover, the solution algorithm, although polynomial, is not practicable when the number of assets is large. A multiperiod robust model, where the uncertainty sets are finite sets, was proposed in [1].

Recently, Delage and Ye [9] have proposed a distributionally robust model for portfolio selection. They assume that the distribution  $f$  of the random return  $\xi$  is uncertain and is assumed to belong to uncertainty sets of the form:

$$\mathcal{D}_{1}(\mathcal{S}, \boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}_{0}, \boldsymbol{\gamma}_{1}, \boldsymbol{\gamma}_{2}) = \begin{cases} \mathbb{P}_{f}(\boldsymbol{\xi} \in \mathcal{S}) = 1\\ f: \quad (\mathbb{E}_{f}[\boldsymbol{\xi}] - \boldsymbol{\mu}_{0})' \boldsymbol{\Sigma}_{0}^{-1} (\mathbb{E}_{f}[\boldsymbol{\xi}] - \boldsymbol{\mu}_{0}) \leq \boldsymbol{\gamma}_{1} \\ \mathbb{E}_{f}[(\boldsymbol{\xi} - \boldsymbol{\mu}_{0})(\boldsymbol{\xi} - \boldsymbol{\mu}_{0})'] \leq \boldsymbol{\gamma}_{2} \boldsymbol{\Sigma}_{0} \end{cases}$$
(9)

Notice that the uncertainty set for the covariance matrix  $\mathbb{E}_{f}[(\boldsymbol{\xi}-\boldsymbol{\mu}_{0})(\boldsymbol{\xi}-\boldsymbol{\mu}_{0})']$  has an *upper* bound and the uncertainty set for the mean vector  $\mathbb{E}_f[\boldsymbol{\xi}]$ is centered around the nominal covariance matrix  $\Sigma_0$ instead of the true covariance matrix. Delage and Ye consider robust portfolio selection problems of the form

$$\max_{\boldsymbol{\phi}\in\boldsymbol{\Phi}}\ \min_{f\in\mathcal{D}_1}\mathbb{E}_f[u(\boldsymbol{\phi},\boldsymbol{\xi})] \tag{10}$$

where  $u(\boldsymbol{\phi}, \boldsymbol{\xi})$  is a piece-wise linear concave utility function of the form  $u(\boldsymbol{\phi}, \boldsymbol{\xi}) = \min_{k} \{a_{k} \boldsymbol{\xi}' \boldsymbol{\phi} + b_{k}\}.$ Fix  $\phi \in \Phi$ . Then convex duality implies that the inner optimization problem  $\min_{f \in \mathcal{D}_1} \mathbb{E}_f[u(\boldsymbol{\phi}, \boldsymbol{\xi})]$  is equivalent to

$$\begin{aligned} \max \quad & r - t, \\ \text{s. t.} \quad & r \le a_k \boldsymbol{\xi}' \boldsymbol{\phi} + b_k + \boldsymbol{\xi}' \mathbf{Q} \boldsymbol{\xi} + \boldsymbol{\xi}' \mathbf{q} \quad \forall k, \ \forall \boldsymbol{\xi} \in \mathcal{S} \\ & t \ge (\gamma_2 \boldsymbol{\Sigma}_0 + \boldsymbol{\mu}_0 \boldsymbol{\mu}_0') \bullet \mathbf{Q} + \boldsymbol{\mu}_0' \mathbf{q} \\ & + \sqrt{\gamma_1} \|\boldsymbol{\Sigma}_0^{\frac{1}{2}} (\mathbf{q} + 2\mathbf{Q}\boldsymbol{\mu}_0) \| \\ & \mathbf{Q} \succeq \mathbf{0} \end{aligned} \tag{11}$$

where  $\mathbf{A} \bullet \mathbf{B} = \text{Tr}(\mathbf{AB})$  denotes the Frobenius inner product of matrices. Note that equation (11) is a semiinfinite optimization problem since the first constraint has to hold for all  $\xi \in S$ . Moreover, it is a semidefinite program, and is, therefore, a much harder problem compared to SOCPs or convex quadratic programs. Using results from convex optimization theory, Delage and Yu show that an  $\epsilon$ -approximate

solution in  $\mathcal{O}\left(n^{6.5}\log\left(\frac{1}{\epsilon}\right)\right)$  iterations. This complexity is prohibitive for a portfolio selection problem of any reasonable size; however, it does provide a new perspective, namely, uncertainty sets for random returns. Lim et al. have studied a minimax regret formulation for portfolio selection in continuous time [21].

The robust optimization methodology has also been extended to *active* portfolio management problems where the goal is to beat a given benchmark by using information that is not broadly available in the market. Since errors in estimating the returns of assets are expected to have serious consequences for an active strategy, robust models are likely to result in portfolios with significantly superior performance. Erdoğan et al. [14] show how the basic robust portfolio selection model extends to robust active portfolio management. Since active portfolio strategies tend to execute many trades, properly modeling and managing trading costs are essential for the success of any practical active portfolio management model [20, 24]. Erdoğan et al. [14] show that a very large class of piecewise convex trading cost functions can be incorporated into an active portfolio selection problem in a tractable manner. Ceria and Stubbs [6] show how to impose a variety of side constraints on the exceptional return  $\alpha$  and still recast the portfolio selection problem as an SOCP. Erdogan et al. [13] show how to incorporate analysts' views about  $\alpha$ and nonparametric loss functions into robust active portfolio management.

## References

- Ben-Tal, A., Margalit, T. & Nemirovski, A. (2000). [1] Robust modeling of multi-stage portfolio problems, in High Performance Optimization, Kluwer Academic Publishers, Dordrecht, pp. 303-328.
- [2] Ben-Tal, A. & Nemirovski, A. (1998). Robust convex optimization, Mathematics of Operations Research 23(4), 769-805.
- Ben-Tal, A. & Nemirovski, A. (1999). Robust solutions [3] of uncertain linear programs, Operations Research Letters  $25(1)$ , 1–13.
- [4] Ben-Tal, A. & Nemirovski, A. (2001). Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA.
- [5] Broadie, M. (1993). Computing efficient frontiers using estimated parameters, Annals of Operations Research 45,  $21 - 58.$

## **4 Robust Portfolio Optimization**

- [6] Ceria, S. & Stubbs, R.A. (2006). Incorporating estimation errors into portfolio selection: robust portfolio construction, *Journal of Asset Management* **7**, 109–127.
- [7] Chopra, V.K. (1993). Improving optimization, *Journal of Investing* **2**, (Fall), 51–59.
- [8] Chopra, V.K. & Ziemba, W.T. (1993). The effect of errors in means, variances and covariances on optimal portfolio choice, *Journal of Portfolio Management* **19**, (Winter), 6–11.
- [9] Delage, E. & Ye, Y. Distributionally robust optimization under moment uncertainty with applications to datadriven problem, Under review in *Operations Research*.
- [10] El Ghaoui, L. & Lebret, H. (1997). Robust solutions to least-squares problems with uncertain data, *SIAM Journal on Matrix Analysis and Applications* **18**(4), 1035–1064.
- [11] El Ghaoui, L. & Niculescu, N. (eds) (1999). *Recent Advances on LMI Methods in Control*, SIAM.
- [12] El Ghaoui, L., Oustry, F. & Lebret, H. (1998). Robust solutions to uncertain semidefinite programs, *SIAM Journal on Optimization* **9**(1), 33–52.
- [13] Erdogan, E., Goldfarb, D. & Iyengar, G. (2006). ˘ *Robust Active Portfolio Management*, Technical Report TR-2004-11, Computational Optimization Research Center (CORC), IEOR Department, Columbia University, Avaliable at http://www.corc.ieor.columbia.edu/reports/ techreports/tr-2004-11.pdf
- [14] Erdogan, E., Goldfarb, D. & Iyengar, G. (2008). Robust ˘ active portfolio management, *Journal of Computational Finance* **11**(4), 71–98.
- [15] Frost, P.A. & Savarino, J.E. (1986). An empirical Bayes approach to efficient portfolio selection, *Journal of Financial and Quantitative Analysis* **21**, 293–305.
- [16] Frost, P.A. & Savarino, J.E. (1988). For better performance: constrain portfolio weights, *Journal of Portfolio Management* **15**, 29–34.
- [17] Goldfarb, D. & Iyengar, G. (2003). Robust portfolio selection problems, *Mathematics of Operations Research* **28**(1), 1–38.
- [18] Halldorsson, B.V. & T ´ ut¨ unc ¨ u, R.H. (2000). ¨ *An Interiorpoint Method for a Class of Saddle Point Problems*. Technical report, Carnegie Mellon University, April 2000.

- [19] Jagannathan, R. & Ma, T. (2003). Risk reduction in large portfolios: why imposing the wrong constraints helps, *Journal of Finance* **58**, 1651–1683.
- [20] Kissell, R. & Glantz, M. (2003). *Optimal Trading Strategies: Quantitative Approaches for Managing Market Impact and Trading Risk*, AMACOM.
- [21] Lim, A.E.B., Shanthikumar, J.G. & Watewai, T. Robust asset allocation with benchmarked objectives, Under review in *Mathematical Finance*.
- [22] Lintner, J. (1965). Valuation of risky assets and the selection of risky investments in stock portfolios and capital budgets, *Review of Economics and Statistics* **47**, 13–37.
- [23] Lobo, M.S., Vandenberghe, L., Boyd, S. & Lebret, H. (1998). Applications of second-order cone programming, *Linear Algebra and its Applications* **284**(1–3), 193–228.
- [24] Loeb, T.F. (1983). Trading cost: the critical link between investment information and results, *Financial Analysts Journal*, 39–44.
- [25] Markowitz, H.M. (1952). Portfolio selection, *Journal of Finance* **7**, 77–91.
- [26] Markowitz, H.M. (1959). *Portfolio Selection*, Wiley, New York.
- [27] Michaud, R.O. (1998). *Efficient Asset Management: A Practical Guide to Stock Portfolio Optimization and Asset Allocation*, Harward Business School Press, Boston.
- [28] Mossin, J. (1966). Equilibrium in capital asset markets, *Econometrica* **34**(4), 768–783.
- [29] Nesterov, Y. & Nemirovski, A. (1993). *Interior-point polynomial algorithms in convex programming*, SIAM, Philadelphia.
- [30] Sharpe, W. (1964). Capital asset prices: a theory of market equilibrium under conditions of risk, *Journal of Finance* **19**(3), 425–442.
- [31] Ziemba, W.T. & Mulvey, J.M. (eds) (1998). *Worldwide Asset and Liability Modeling*, Cambridge University Press, Cambridge, UK.

## GARUD IYENGAR
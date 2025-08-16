# **Risk–Return Analysis**

# **Mean–Variance Analysis**

While the idea of trade-off curves goes back to, Pareto, the notion of a trade-off curve (later dubbed *efficient frontier*) in finance was introduced by Markowitz [15] in 1952. Markowitz proposed expected return and variance as both a hypothesis about how investors act and as a rule for guiding action in fact. By 1959 [18], he had given up the notion of mean and variance as a hypothesis but continued to propose them as criteria for action.

Tobin [32] said that the use of mean and variance as criteria assumed either a quadratic utility function or a Gaussian probability distribution. This view is sometimes ascribed to Markowitz, but he never justified the use of mean and variance in this way. His views evolved considerably from 1952 to 1959 [15] and [18]. Consequently, his early views [15] should be ignored. In his book published in 1959, Markowitz [18] accepts the views of Von Neumann and Morgenstern [33] when probability distributions are known, and Leonard J. Savage [29] when probabilities are not known. The former asserts that one should maximize expected utility, whereas the latter asserts that when probabilities are not known one should maximize expected utility using probability beliefs when objective probabilities are not known.

A utility function *U (R)* is any function of return *R*. If the function is concave, that is,

$$U(aX + (1 - a)Y) \ge aU(X) + (1 - a)U(Y) \quad (1)$$

for *a* ∈ [0*,* 1] then an investor prefers certainty to random returns. If

$$U(aX + (1 - a)Y) \le aU(X) + (1 - a)U(Y) \quad (2)$$

then the investor prefers gambling to certainty. An intermediate case is when the utility function is linear. In this case, the gambler is neither risk averse as in equation (1) nor risk seeking as in equation (2). Rather, the investor acts to maximize expected return.

Markowitz [18] seeks to serve the cautious investor whose utility function satisfies equation (1). In this respect, Markowitz, assumes a different shape of utility function in [15] from the one in [16]. In the latter, he assumes a utility function that is convex in some places and concave in others. This was proposed as a hypothesis about human action consistent with gambling and insurance. It builds upon and, the author believes, improves upon [7].

# **Critical Line Algorithm**

The critical line algorithm (CLA) is presented in [17] and again in Appendix A of [18]. The latter shows that the algorithm works even if the matrix of covariances, required by the problem, is singular. This is important since the problem may include short as well as long positions (treated as separate "investments" to represent real-world constraints on the selection of the portfolio when short-sales are permitted), or covariances based on historical returns when there are more securities than observations. In either case, a singular covariance matrix will result.

The CLA makes use of the fact that, in portfolio space, the set of efficient portfolios is piecewise linear. In mean–variance space it is piecewise parabolic; in mean–standard deviation space it is piecewise linear or hyperbolic (see [19] or [22], Chapter 7). The CLA generates, one after the other, all the linear pieces of the portfolio-space set without groping or iterating for the right answer. In this manner, CLA generates the entire mean–variance efficient set almost as quickly as the best methods for finding a single point in this set.

The CLA uses the George Dantzig simplex algorithm [6] of linear programming to determine the first critical line. The portfolio selection constraint may be bounded or unbounded. In the latter case, the first critical line is a ray that proceeds without bounds in the direction of increasing expected return. Again, see [22, Chapter 8], Chapter 9 of [22] discusses the degenerate case in which variables go to zero simultaneously.

# **Mean–Variance Approximations to Expected Utility**

Markowitz [18] accepts the justifications of Von Neumann and Morgenstern [33], and Leonard J. Savage [29] for expected utility using personal probabilities when objective probabilities are not known. He conjectures that a suitably chosen point from the efficient frontier will approximately maximize expected utility for the kinds of utility functions that are commonly proposed for cautious investors, and for the kinds of probability distributions that are found in practice. Levy and Markowitz [14] expand on this notion considerably. Specifically, Levy and Markowitz show that for such probability distributions and utility functions there is typically a correlation between the actual expected utility and the mean–variance approximation in excess of 0.99. Levy and Markowitz also show that the Pratt [27] and Arrow [1] objections to quadratic utility do not apply to the kind of approximations used by them, or to those in [18]. Specifically, Pratt and Arrow assume that the investor has one fixed-forever utility function and, as her or his wealth changes, the investor moves up and down this utility function. Under this assumption, if the investor becomes wealthy enough, quadratic utility no longer increases with wealth. This is clearly absurd. The Levy and Markowitz [14] and the Markowitz [18] approximations are based on Taylor expansions about current wealth, or expected end-of-period wealth.

# **Models of Covariance**

If covariances are computed from historical returns with more securities than there are observations, for example, 5000 securities and 60 months of observations, then the covariance matrix will be singular. A preferable alternative is to use a linear model of covariance where the return on the *i*th security is assumed to obey the following relationship:

$$r_i = \alpha_i + \Sigma \beta_{ik} f_k + u_i \tag{3}$$

where *ui* are independent of each other and the *fk*. The *fk* may be either factors or scenarios or some of each. These ideas are carried out in, for example [28, 30], and [20, 21].

# **Semivariance**

In [18, Chapter 9], Markowitz defines two forms of semivariance, namely, about expected value *E* or about some fixed number *a*:

$$S_E = E(\min(r, E)^2) \tag{4}$$

$$S_a = E(\min(r, a)^2) \tag{5}$$

In [18], Markowitz says that some form of semivariance seems preferable to mean–variance analysis, but computation is a problem. At present, this computational problem has disappeared. In [18, Chapter 9], he presents a variant of CLA, which traces out the mean–semivariance frontier. Sortino [31] champions the use of semivariance. Mean–variance analysis has been dubbed *modern portfolio theory* (*MPT*). Sortino refers to risk– return analysis with semivariance as *postmodern portfolio theory*.

The chief argument in favor of semivariance, as opposed to variance, is that the investor is not concerned with upside deviations; she or he is concerned only with downside deviations. Arguments in favor of mean–variance rather than semivariance are as follows: variance requires only the covariance matrix as input rather than historical returns, or synthetic history generated randomly; and, the mean–variance approximations of expected utility do so well when probability distributions are not spread out "too much".

# **Other Measures of Risk**

Konno [11] recommends absolute deviation as a criterion for risk in a risk– return trade-off analysis. An advantage of these criteria is that the frontier may be traced out using linear programming.

In [18, Chapter 13], Markowitz objects to these criteria because the function that they imply as the approximation to the utility function does not seem plausible. A similar, but even stronger, objection is raised there to the use of probability of loss as the measure of risk.

# **Time**

In [18, Chapters 11 and 13], Markowitz notes that mean–variance analysis is a single-period analysis, but that does not mean that it is useless in a manyperiod world. Bellman [2] shows that the optimum strategy for a many-period or infinite-period game consists of maximizing a sequence of single-period utility functions where the utility function is the "derived" utility for the game. If assets are perfectly liquid, the end-of-period derived utility function depends only on end-of-period wealth, and if the Levy–Markowitz approximations to expected utility are good enough, then one may use mean–variance

or

for a many-period game. If the end-of-period utility function depends on other state variables, and the utility function may be adequately approximated by a quadratic, then the action should depend on mean and variance, and covariance with the other state variables.

If assets are not perfectly liquid, then state variables include the holding of each asset. This results in the problem referred to as the *curse of dimensionality*. Markowitz and van Dijk [19] propose a heuristic for solving this problem. This heuristic approximates the unknown derived utility function by a quadratic in the various state variables. Kritzman [12] report as follows:

Our tests reveal that the quadratic heuristic provides solutions that are remarkably close to the dynamic programming solutions for those cases in which dynamic programming is feasible and far superior to solutions based on standard industry heuristics. In the case of five assets, in fact, it performs better than dynamic programming due to approximations required to implement the dynamic programming algorithm. Moreover, unlike the dynamic programming solution, the quadratic heuristic is scalable to as many as several hundred assets.

# **Estimation of Parameters**

Covariance matrices are sometimes estimated from historical returns and sometimes from factor or scenario models such as the one-factor model of Sharpe [30], the many-factor model of Rosenberg [28], or the scenario models of Markowitz and Perold [20, 21].

Expected returns are estimated in a great variety of ways. It is unlikely that anyone would suggest that the expected returns of individual stocks be estimated from the historical average returns. The Ibbotson [9] series are frequently used to estimate expected returns for asset classes. Black and Litterman [3, 4] propose a very interesting Bayesian approach to the estimation of expected returns. Richard Michaud [25] proposes to use estimates for asset classes based on what he refers to as a *resampled frontier*. Markowitz and Usmen [23] test the resampled frontier idea against a diffuse Bayesian approach. By and large, they find that the Michaud approach outperformed the diffuse Bayesian approach. However, Markowitz and Usmen noted that had they increased the variance estimated by the Bayesian they would have done approximately as well as the Michaud approach. Somehow, Michaud's patented process, which averages repeated drawings of frontiers generated from a Gaussian distribution with historical covariances, seems to essentially replicate a supercautious Bayesian.

Additional methods for estimating expected return are based on statistical methods for "disentangling" various anomalies [10], or estimates based on factors that [8] might use. See [13, 26], and [5]. The latter paper is based on results obtained by back-testing many alternate hypotheses concerning how to achieve excess returns. When many estimation methods are tested, the expected future return for the best of the lot (assuming that nature will sample from the same population as before) should not be estimated as if this were the only procedure tested (see [24]).

# **References**

- [1] Arrow, K. (1971). *Aspects of the Theory of Risk Bearing*, Markham Publishing Company, Chicago, IL.
- [2] Bellman, R.E. (1957). *Dynamic Programming*, Princeton University Press, Princeton, NJ.
- [3] Black, F. & Litterman, R. (1991). Asset allocation: combining investor views with market equilibrium, *Journal of Fixed Income* **1**(2), 7–18.
- [4] Black, F. & Litterman, R. (1992). Global portfolio optimization, *Financial Analysts Journal* **48**(5), 28–43.
- [5] Bloch, M., Guerard, J., Markowitz, H., Todd, P. & Xu, G. (1993). A comparison of some aspects of the U.S. and Japanese equity markets, *Japan and the World Economy* **5**, 3–26.
- [6] Dantzig, G.B. (1954). *Notes on Linear Programming: Parts VIII, IX, X—Upper Bounds, Secondary Constraints, and Block Triangularity in Linear Programming*, The RAND Corporation, Research Memorandum RM-1367, October 4, 1954. Published in Econometrica, Vol. 23, No. 2, April 1955, pp. 174–183.
- [7] Friedman, M. & Savage, L.P. (1948). The utility analysis of choices involving risk, *Journal of Political Economy,* **56**, 279–304.
- [8] Graham, B. & Dodd, D.L. (1940). *Security Analysis*, 2nd Edition, McGraw-Hill, New York.
- [9] Ibbotson R.G. (2009). *Market Results for Stock, Bonds, Bills, and Inflation 1926–2008*. Classic Yearbook, Morningstar, Inc, Chicago, IL.
- [10] Jacobs, B.I. & Levy, K.N. (1988). Disentangling equity return regularities: new insights and investment opportunities, *Financial Analysts Journal* **44**(3), 18–44.
- [11] Konno, H. & Yamazaki, H. (1991). Mean-absolute deviation portfolio optimization model and its applications to Tokyo stock market, *Management Science* **37**(5), 519–531.
- [12] Kritzman, M., Myrgren, S. & Page, S. (2007). *Portfolio Rebalancing: A Test of the Markowitz-van Dijk Heuristic*, Pending Publication.

- [13] Lakonishok, J., Shleifer, A. & Vishny, R.W. (1994). Contrarian investment, extrapolation and risk, *Journal of Finance* **49**(5), 1541–1578.
- [14] Levy, H. & Markowitz, H.M. (1979). Approximating expected utility by a function of mean and variance, *American Economic Review* **69**(3), 308–317.
- [15] Markowitz, H.M. (1952). Portfolio selection, *The Journal of Finance* **7**(1), 77–91.
- [16] Markowitz, H.M. (1952). The utility of wealth, *The Journal of Political Economy* **2**, 152–158.
- [17] Markowitz, H.M. (1956). The optimization of a quadratic function subject to linear constraints, *Naval Research Logistics Quarterly* **3**, 111–133.
- [18] Markowitz, H.M. (1959, 1991). *Portfolio Selection: Efficient Diversification of Investments*, 2nd Edition, Wiley, Yale University Press, Basil Blackwell.
- [19] Markowitz, H.M. & van Dijk, E. (2003). Single-period mean–variance analysis in a changing world, *Financial Analysts Journal* **59**(2), 30–44.
- [20] Markowitz, H.M. & Perold, A.F. (1981). Portfolio analysis with factors and scenarios, *The Journal of Finance* **36**(14), 871–877.
- [21] Markowitz, H.M. & Perold, A.F. (1981). Sparsity and piecewise linearity in large portfolio optimization problems, in *Sparse Matrices and Their Uses*, I.S. Duff ed, Academic Press, pp. 89–108.
- [22] Markowitz, H.M. & Todd, P. (2000). *Mean-Variance Analysis in Portfolio Choice and Capital Markets*, Frank J. Fabozzi Associates, New Hope, PA. (revised reissue of Markowitz (1987) with chapter by Peter Todd).
- [23] Markowitz, H.M. & Usmen, N. (2003). Resampled frontiers versus diffuse Bayes: an experiment, *Journal of Investment Management* **1**(4), 9–25.
- [24] Markowitz, H.M. & Xu, G.L. (1994). Date mining corrections, *The Journal of Portfolio Management* **21**, 60–69.
- [25] Michaud, R.O. (1989). The Markowitz optimization enigma: is optimized optimal? *Financial Analysts Journal* **45**(1), 31–42.

- [26] Ohlson, J.A. (1979). Risk, return, security-valuation and the stochastic behavior of accounting numbers, *Journal of Financial and Quantitative Analysis* **14**(2), 317–336.
- [27] Pratt, J.W. (1964). Risk aversion in the small and in the large, *Econometrica* **32**, 122–136.
- [28] Rosenberg, B. (1974). Extra-market components of covariance in security returns, *Journal of Financial and Quantitative Analysis* **9**(2), 263–273.
- [29] Savage, L.J. (1954). *The Foundations of Statistics*, 2nd Revised Edition, John Wiley & Sons, Dover, New York.
- [30] Sharpe, W.F. (1963). A simplified model for portfolio analysis, *Management Science* **9**(2), 277–293.
- [31] Sortino, F. & Satchell, S. (2001). *Managing Downside Risk in Financial Markets: Theory, Practice and Implementation*, Butterworth-Heinemann, Burlington, MA.
- [32] Tobin, J. (1958). Liquidity preference as behavior towards risk, *Review of Economic Studies* **25**(1), 65–86.
- [33] Von Neumann, J. & Morgenstern, O. (1944, 1953). *Theory of Games and Economic Behavior*, 3rd Edition, Princeton University Press.

# **Further Reading**

Ibbotson, R.G. & Sinquefield, R.A. (2007). *Stocks, Bonds, Bills and Inflation Yearbook*, Morningstar, New York.

# **Related Articles**

**Behavioral Portfolio Selection**; **Black–Litterman Approach**; **Diversification**; **Expected Utility Maximization**; **Markowitz, Harry**; **Mean–Variance Hedging**.

HARRY M. MARKOWITZ
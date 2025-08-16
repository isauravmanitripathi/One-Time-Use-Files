# **Optimization Methods**

No area of computational mathematics plays a greater role in the support of financial decision making and strategy development than numerical optimization. The full gamut of optimization methodologies are applied to this end—linear and quadratic, nonlinear and global, stochastic and deterministic, discrete and continuous—and applications propagate throughout the front office, back office, analysis, and trading operations. The use of optimization is deep, pervasive, and growing.

We organize our presentation in three "levels". The top level in our presentation is the management of portfolios based on quadratic programming, the second level is stochastic programming for portfolio optimization, and the lowest (but perhaps the most important) level is model calibration (*see* **Model Calibration**).

While some of the methodological issues that arise are specific to the different levels, there are three dominant themes that cut across all levels: speed, robustness, and quality of solution. Speed often dominates thinking in financial circles since rapid informed decision making (sometimes, "automatic") can translate into capital gains (conversely, lack of sufficient speed can lead to losses). Nevertheless, a "wrong" answer computed at record speed is not of much value (and could be quite disastrous). A solution can be wrong in several ways. For example, if the computed solution is not robust, then the resultant strategy may be a very poor strategy under slight tweaking of the parameters defining the problem. This is a serious practical problem because problem parameters are almost always determined in an approximate manner (i.e., they are not known exactly). Other solution quality issues can arise. For example, some optimization problems are too hard to solve in reasonable time and so approximation schemes must be used. But how good is the approximate solution?

As we discuss some of the optimization challenges that arise under the organizing levels mentioned above, we make particular note of these three unifying numerical concerns.

## **Portfolio Management: Quadratic Programming**

The most famous optimization application in finance is the mean–variance portfolio optimization problem, first introduced by Markowitz [19]; *see also* **Risk–Return Analysis**. The question that is addressed by "mean–variance portfolio optimization" is both easy to understand and practical: how should one distribute, across a given set of financial instruments, a finite investment in order to balance (according to the investors preference) risk and expected return? In its pure form, this question can be formulated as a positive definite quadratic programming problem.

Let *µ* ∈ *<sup>n</sup>* be a vector of expected returns for *n* assets, and an *n*-by-*n* matrix *Q* be the covariance matrix of asset returns. Assume that the vector *x* ∈ *<sup>n</sup>* denotes the percentage of asset holdings. Then the mean-variance portfolio optimization problem can be formulated as

$$\min_{x} \quad -\mu^{T} x + \lambda x^{T} Q x$$
  
subject to 
$$\sum_{i=1}^{n} x_{i} = 1 \quad (1)$$

where *λ* ≥ 0 is a risk aversion parameter. Additional (linear) constraints can be imposed, for example, no short selling constraints correspond to *x* ≥ 0. There are many good algorithms, and codes (e.g., MOSEK and LOQO [24]) to solve positive definite quadratic programming problems, but the situation becomes more complex (and more interesting) as financial (and numerical) concerns are introduced.

One complication arises in the equity setting: portfolios held in many firms can be quite large—in several thousands—and typically have a dense matrix *Q*; nevertheless, there is serious need to determine a solution rapidly. Moreover, because many of the subsets of instruments in the portfolio behave in a highly correlated way the matrix *Q* can be illconditioned. This means numerical algorithms can have a hard time computing accurate answers, and small changes in the input data can lead to very different proposed strategies and portfolios. One approach to address these difficulties is to use a factor model. However, algorithm implementation needs to exploit this special structure of the covariance matrix for optimal computational efficiency.

Another complication is the need to use additional terms, for example, to capture transaction costs (*see* **Transaction Costs**). These additional terms yield a more realistic model; however, they may also change the objective function into a more nonlinear function. This apparent small change has a big impact—general nonlinear codes (even with linear constraints) are more complex and have fewer "guarantees" relative to quadratic objective functions.

Recently, there has been considerable attention paid to the fact that the objective function in equation (1) is just an approximation to reality. Estimation of expected returns is notoriously difficult; the expected return parameter may be closer to wishful thinking than reality. Specifically, return *µ* and covariance matrix *Q* are supposed to represent the return and risk going forward in time but are typically, in fact, the return and risk going backward. The question is, how well does our chosen portfolio (i.e., the optimization solution based on these estimated parameters) perform as reality rolls forward under real conditions? Unfortunately, the answer is that it may not do very well at all; see for example, [5, 6].

There is now considerable attention being paid to this very practical concern, generally under the label "robust optimization"; see for example, [14, 15, 23], and **Robust Portfolio Optimization**. The goal of robust optimization is to guarantee the best performance in the worse case. Since the support for an uncertain parameter may be infinite, a robust portfolio is typically determined by considering optimal performance in the worst case within some uncertainty sets for model parameters. For example, the min–max robust formulation for equation (1) can be expressed as

$$\min_{x} \quad \max_{\mu \in \mathcal{S}_{\mu}, Q \in \mathcal{S}_{Q}} -\mu^{T} x + \lambda x^{T} Q x$$
  
subject to 
$$\sum_{i=1}^{n} x_{i} = 1 \qquad (2)$$

where S*<sup>µ</sup>* and S*<sup>Q</sup>* are uncertainty sets for the expected return *µ* and covariance matrix *Q*, respectively. The uncertainty sets are often either intervals or ellipsoids (typically corresponding to some confidence intervals). Efficient computational methods for conic optimization and semidefinite programming can be used to solve some of these robust optimization problems; see, for example, [11].

There is need for still more research here though since much of the work to date takes an unduly conservative—and expensive—point of view: given a range to capture the possibility values of the parameters, solve the problem in the worst case. This solution provides protection but is certainly on the extreme risk-averse side. Recently, a conditional Value-at-Risk (CVaR) robust formulation is considered in [25] to address uncertainty in the parameters for mean–variance portfolio optimization.

## **CVaR Minimization and Optimal Executions: Stochastic Programming**

Optimal financial decisions often need to be made using uncertain parameters which describe the optimization problems. This view leads to stochastic programming problems.

Even in a single-period portfolio optimization framework, if instrument values (e.g., options) depend nonlinearly on the risk factors, a different risk measure, instead of standard deviation, for example, Value-at-Risk (VaR) (*see* **Value-at-Risk**) or CVaR (*see* **Expected Shortfall**), needs to be used. Both these measures quantify near-worst case losses and both present interesting optimization challenges.

VaR is essentially a quantile of a loss distribution. For a confidence level *β*, for example, 95%, the VaR of a portfolio is the loss in the portfolio's market value over a specified time horizon that is exceeded with probability 1 − *β*. When VaR is used as a risk measure, the portfolio optimization problem is, in general, a nonconvex programming problem. Computing a global minimizer remains a computationally challenging task.

An alternative risk measure to VaR is CVaR. When the distribution of the portfolio loss is continuous, for a given time horizon and a confidence level *β*, CVaR is the conditional expectation of the loss exceeding VaR. In contrast to VaR, CVaR provides additional information on the magnitude of the excess loss. It has been shown that CVaR is a coherent risk measure; see for example, [3, 21]. In addition, minimizing CVaR typically leads to a portfolio with a small VaR.

Assume that *L(x)* is the random variable denoting loss of a portfolio *x* ∈ *<sup>n</sup>* within a given time horizon. If *x* is a vector of instrument holdings and *δV* is (random) change in the instrument values, then *L(x)* = −*x<sup>T</sup> (δV )*. For a given confidence level, CVaR is given by

$$\text{CVaR}_{\beta}(L(x))$$
  
= 
$$\min_{\alpha} \left(\alpha + (1 - \beta)^{-1} \mathbf{E}((L(x) - \alpha)^{+})\right) \tag{3}$$

where  $(L(x) - \alpha)^{+} = \max(L(x) - \alpha, 0)$  and  $\mathbf{E}(\cdot)$ denotes the expectation of a random variable. When the loss distribution is continuous, the above relation follows directly from the optimality condition [22]. Unlike VaR, the CVaR portfolio optimization problem.

$$\min_{x,\alpha} \quad \left(\alpha + (1-\beta)^{-1} \mathbf{E}((L(x)-\alpha)^{+})\right) \tag{4}$$

is a convex optimization problem [22].

Assume that  $\{(\delta V)_i\}_{i=1}^m$  are independent samples of the change in the instrument values over the given horizon. Then the following is a scenario CVaR optimization problem, which approximates the above continuous CVaR optimization problem:

$$\min_{(x,\alpha)} \left( \alpha + \frac{1}{m(1-\beta)} \sum_{i=1}^{m} \left[ -(\delta V)_{i}^{T} x - \alpha \right]^{+} \right) \quad (5)$$

This piecewise linear optimization problem has an equivalent linear programming formulation, which can be solved using standard linear programming methods. The resulting linear program has  $O(m + n)$ variables and  $O(m+n)$  constraints, where m is the number of Monte Carlo samples and  $n$  is the number of instruments. Note that any additional linear constraints can easily be included. Although this linear programming problem can be solved using standard linear programming software, a smoothing technique is proposed in [1]; this smoothing method is shown to be significantly more computationally efficient when the number of instruments and scenarios become large.

Frequently, portfolio optimal decision problem is also a multistage dynamic programming problem. Recently, there has been much interest in the optimal execution of a portfolio of large trades under the market impact consideration; see, for example, [2, 4, 13].

The optimal execution problem can be formulated as a continuous time stochastic control problem. We illustrate the problem here in the discrete setting. Suppose that a financial institution wants to sell a large number of shares  $\bar{S} \in \mathbb{R}^m$  in *m* assets by trading at  $t_0 = 0 < t_1 < \cdots < t_N = T$ , where  $t_{i+1} - t_i =$  $\tau = \frac{T}{N}$  and  $T > 0$  is the time horizon. Let the trades between  $t_{k-1}$  and  $t_k$  be denoted by vectors  $n_k$ ,  $k =$  $1, 2, \cdots, N$ .

Let us assume that, at time  $t_k$ ,  $k = 0, 1, \dots, N$ , the vector  $P_k$  are the prices per share of assets that are publicly available in the market and  $\tilde{P}_k$  are the execution prices of one unit of the assets. The execution cost (see **Execution Costs**) of the trades is often defined as  $P_0^T \bar{S} - \sum_{k=1}^N n_k^T \tilde{P}_k$ . Owing to uncertainties in price movements and in realized prices, this implementation cost is a random variable. Hence, the mean-variance formulation of the execution cost problem with a risk-aversion parameter  $\lambda > 0$  is

$$\begin{aligned} \min_{n_1, n_2, \dots, n_N} \quad & \mathbf{E} \left( P_0^T \bar{S} - \sum_{k=1}^N n_k^T \tilde{P}_k \right) + \\ & \lambda \cdot \mathbf{Var} \left( P_0^T \bar{S} - \sum_{k=1}^N n_k^T \tilde{P}_k \right) \\ \text{s.t.} \quad & \sum_{k=1}^N n_k = \bar{S} \\ & n_k \ge 0, \quad k = 1, 2, \dots, N \end{aligned} \tag{6}$$

where  $\mathbf{E}(\cdot)$  and  $\mathbf{Var}(\cdot)$  denote the expectation and the variance of a random variable, respectively.

The complexity level of equation (6) depends on assumptions on the price dynamics and the impact functions. In [2], the price vector  $P_k$  is assumed to follow the dynamics:

$$P_k = P_{k-1} + \tau^{1/2} \Sigma \xi_k - \tau g\left(\frac{n_k}{\tau}\right) \tag{7}$$

where  $\xi_{l}^{T} \in \mathbb{R}^{l}$  represents an *l*-vector of independent standard normals, and  $\Sigma$  is an  $m \times l$  volatility matrix of the asset prices. The *m*-vector function  $g(.)$ measures the permanent price impact (see **Price Impact**), which is, in general, relatively small. The execution prices are given by

$$\tilde{P}_k = P_{k-1} - h\left(\frac{n_k}{\tau}\right) \tag{8}$$

where the *m*-vector nonlinear function  $h(.)$  describes the temporary price impact.

Even in this simple price dynamic and market impact models, there are many interesting and important issues for the optimal execution problem. Price impact functions represent the *expected* price depression caused by trading assets at a unit rate. Estimating both temporary and permanent impact functions can incur large estimation errors. The sensitivity of the optimal execution strategy to the estimation error in the impact matrices has recently been studied in [20]. In addition, if the price dynamics and impact functions depend on additional state variables as considered in [4], solving a portfolio execution problem with many assets is computationally challenging, especially when no short selling constraints are imposed.

## **Nonlinear Programming**

One of the most active roles optimization plays in finance is the calibration of models (see Model Cali**bration**) yield curve construction (see Yield Curve **Construction**) and statistical estimation problems (see Generalized Method of Moments (GMM); Entropy-based Estimation; Simulation-based Estimation). Mathematical models are used to represent the behavior of financial instruments, and portfolios of such instruments, and such models almost always require parameters to be estimated. These parameters can be scalars, vectors, matrices, tensors, lines, curves, and surfaces. The estimation processes can lead to linear, nonlinear, convex, and nonconvex optimization problems (see examples in **Model Cali**bration).

The usual situation leads to a data-fitting problem: given a model with unknown parameters, and given some real data (say, market prices), determine the "best" value for the parameters. An important class of such problems is the option model calibration problem in which one determines a model so that model values best fit market prices. Such problems are known as *inverse* problems and there is a significant literature on the creation and solution of inverse problems in engineering.

To illustrate, assume that a family of models are described by the model parameters  $x$  in a feasible set  $\Omega$ . The feasible set constraints (such as nonnegativity, upper-bound constraints) can be used to impose certain conditions on the model parameters. Calibration problems determine the best fit to the market option prices; the best fitting parameters can be determined by solving the following nonlinear least-squares problem:

$$\min_{x \in \Omega} \frac{1}{2} \sum_{j=1}^{m} \left( V_0(K_j, T_j; x) - V_0^{\text{mkt}}(K_j, T_j) \right)^2 \quad (9)$$

where  $V_0^{\text{mkt}}(K_i, T_i)$  denote today's market prices for standard options with strike  $K_i$  and expiry  $T_i$ ,  $j = 1, \cdots, m$ , and  $\{V_0(K_i, T_i; x), j = 1, \cdots, m\}$ denote today's model values corresponding to model parameters  $x$ .

Let  $F(x): \mathbb{R}^n \to \mathbb{R}^m$  denote the residual vector

$$F(x) \stackrel{\text{def}}{=} \begin{bmatrix} V_0(K_1, T_1; x) - V_0^{\text{mkt}}(K_1, T_1) \\ \vdots \\ V_0(K_m, T_m; x) - V_0^{\text{mkt}}(K_m, T_m) \end{bmatrix} \tag{10}$$

The calibration problem is a *nonlinear least*squares problem

$$\min_{x \in \Omega} \quad \frac{1}{2} \|F(x)\|_2^2$$

There are a host of numerical challenges and issues that arise in the calibration setting but we only mention a few of them here. The foremost, without a doubt, is the reliability of the data (and the volume of data to be used). Data reliability can lead to preprocessing steps such as filtering, and, in some cases, choosing an optimization formulation that is relatively insensitive to data errors (e.g., least-squares minimization is much more sensitive to (erroneous) outliers than absolute-value minimization).

Avoiding overfitting is also a major issue. In order for a model to calibrate some market information, for example, market option prices, one needs to consider a family of sufficiently complex models. For example, it is well known that the classical Black-Scholes model is inadequate to calibrate equity option prices and more complex models such as local volatility function models (see Local Volatility Model), jump models (see Exponential Lévy Models), and stochastic volatility models (see **Heston Model**) have been proposed. When a family of complex models such as local volatility function models are considered, it is crucial to avoid overfitting data; see for example, [8]. Even when a family of models are described by a few model parameters, the question of whether there exists sufficient information to robustly determine model parameters still remains; see, for example, jump model calibration problems [10, 18]. *See also* **Tikhonov Regularization** for additionaldiscussion on regularization techniques.

In addition, option model calibration problems face computational challenges. The problem is often nonconvex and it is possible for this calibration optimization problem to have multiple local minimizers; see for example, [17]. Also note that each initial model value *V*0*(Kj , Tj* ; *x)* is a complex nonlinear function of the model parameters *x*. The Levenberg–Marquardt method or Gauss–Newton method can be used to solve the nonlinear least-squares problem; see, for example, [12]. If the calibration problem has additional bound constraints, an interior point trust region method [7] can be applied. Genetic algorithms have also been used for the calibration problem; see, for example, [17]. Optimization software for this nonlinear least-squares problem requires repeated evaluation of each initial model value *V*0*(Kj , Tj* ; *x)*, which is typically done through numerical computation methods for partial differential equations or using Monte Carlo simulations. A good initial guess for the model parameters can also be crucial in ensuring success in obtaining a solution. We note that automatic differentiation may also be a useful computational tool in accurately computing the Jacobian matrices ∇*F*, which are often required by an optimization software. For more information on automatic differentiation, see, for example, [9, 16].

#### **References**

- [1] Alexander, S., Coleman, T.F. & Li, Y. (2004). Derivative portfolio hedging based on CVaR, in *New Risk Measures in Investment and Regulation*, Szego, G., ed., Wiley, pp. 339–363.
- [2] Almgren, R. & Chriss, N. (2000/2001). Optimal execution of portfolio transactions, *Journal of Risk* **3**, 3.
- [3] Artzner, P., Delbaen, F., Eber, J.M. & Heath, D. (1999). Coherent measures of risk, *Mathematical Finance* **9**, 203–228.
- [4] Bertsimas, D. & Lo, A.W. (1998). Optimal execution costs, *Journal of Financial Markets* **1**, 1–50.
- [5] Best, M.J. & Grauer, R.R. (1991). On the sensitivity of mean-variance-efficient portfolios to changes in asset means: some analytical and computational results, *The Review of Financial Studies* **4**, 315–342.

- [6] Broadie, M. (1993). Computing efficient frontiers using estimated parameters, *Annals of Operations Research* **45**, 21–58.
- [7] Coleman, T.F. & Li, Y. (1996). An interior, trust region approach for nonlinear minimization subject to bounds, *SIAM Journal on Optimization* **6**(2), 418–445.
- [8] Coleman, T.F., Li, Y. & Verma, A. (1999). Reconstructing the unknown local volatility function, *The Journal of Computational Finance* **2**(3), 77–102.
- [9] Coleman, T.F. & Verma, A. (2000). ADMIT-1: automatic differentiation and matlab interface toolbox, *ACM Transactions on Mathematical Software* **26**, 150–175.
- [10] Cont, R. & Tankov, P. (2004). Nonparametric calibration of jump-diffusion option pricing models, *The Journal of Computational Finance* **7**(3), 1–49.
- [11] Cornuejols, G. & Tut¨ unc ¨ u, R.H. (2007). ¨ *Optimization methods in finance*, Cambridge.
- [12] Dennis, J.E. & Schnabel, R.B. (1983). *Numerical Methods for Unconstrained Optimization and Nonlinear Equations*. Prentice-Hall Series in Computational Mathematics, Prentice-Hall.
- [13] Engle, R. & Ferstenberg, R. (2006). *Execution Risk* . Technical report, National Bureau of Economic Research, Cambridge, MA.
- [14] Garlappi, L., Uppal, R. & Wang, T. (2007). Portfolio selection with parameter and model uncertainty: A multi-prior approach, *Review of Financial Studies* **20**, 41–81.
- [15] Goldfarb, D. & Iyengar, G. (2003). Robust portfolio selection problems, *Mathematics of Operations Research* **28**(1), 1–38.
- [16] Griewank, A. & Corliss, G. (eds) (1991). *Automatic Differentiation of Algorithm: Theory, Implementation and Applications*. SIAM Proceedings Series, SIAM.
- [17] Hamida, S.B. & Cont, R. (2005). Recovering volatility from option prices by evolutionary optimization, *Journal of Computational Finance* **8**, 1–34.
- [18] He, C., Kennedy, J.S., Coleman, T.F., Forsyth, P.A., Li, Y. & Vetzal, K. (2006). Calibration and hedging under jump diffusion, *Review of Derivative Research* **9**, 1–35.
- [19] Markowitz, H.M. (1959). *Portfolio Selection: Efficient Diversification of Investments*, John Wiley, New York.
- [20] Moazeni, S., Coleman, T.F. & Li, Y. (2007). *Optimal Portfolio Execution Strategies and Sensitivity to Priceimpact Parameters' Perturbations*. Technical report, David R. Cheriton School of Computer Science, University of Waterloo, Waterloo, Ontario, Canada.
- [21] Pflug, G.Ch. (2000). Some remarks on the value-at-risk and the conditional value-at-risk, in *Probabilistic Constrained Optimization: Methodology and Applications*, S. Uryasev, ed., Kluwer Academic Publishers.
- [22] Rockafellar, R.T. & Uryasev, S. (2000). Optimization of conditional value-at-risk, *Journal of Risk* **2**(3), 21–41.
- [23] Tut¨ unc ¨ u, R.H. & Koenig, M. (2004). Robust asset ¨ allocation, *Annals of Operations Research* **132**(1), 157–187.

#### **6 Optimization Methods**

- [24] Vanderbei, R.J. (1999). LOQO: an interior-point method code for quadratic programming, *Optimization Codes and Software* **11**, 451–484.
- [25] Zhu, L., Coleman, T.F. & Li, Y. (2007). *Min-max Robust and CVaR Robust Mean-variance Portfolios*. Technical report, David R. School of Computer Science, University of Waterloo, Waterloo, Canada.

**Related Articles**

**Model Calibration**; **Risk–Return Analysis**; **Stochastic Control**; **Tikhonov Regularization**.

THOMAS F. COLEMAN & YUYING LI
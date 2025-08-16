# Black–Litterman Approach

The approach by Black and Litterman (BL) [2] blends a reference market distribution with subjective views on the market and yields allocations that smoothly reflect those views.

We present the original BL model and we review the related literature. A longer version of this article with all the proofs and more details is available at  $www.symmys.com > Research > Working Papers.$ 

#### The Original Model

Here we follow [4], see also [5, 12] and [13].

#### The Market Model

We consider a market of  $N$  securities or asset classes. whose returns are normally distributed:

$$\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \tag{1}$$

The covariance  $\Sigma$  is estimated by exponential smoothing of the past return realizations. Since  $\mu$ cannot be known with certainty, BL model it as a normal random variable

$$\boldsymbol{\mu} \sim \mathcal{N}(\boldsymbol{\pi}, \boldsymbol{\tau} \boldsymbol{\Sigma}) \tag{2}$$

where  $\pi$  represents the best guess for  $\mu$  and  $\tau \Sigma$  the uncertainty on this guess.

To set  $\pi$ , BL invoke an equilibrium argument. Assuming there is no estimation error, that is,  $\tau \equiv 0$ in equation  $(2)$ , the reference model  $(1)$  becomes

$$\mathbf{X} \sim \mathcal{N}(\boldsymbol{\pi}, \boldsymbol{\Sigma}) \tag{3}$$

Assume that, consistent with this normal market, all investors maximize a mean-variance trade-off and that the optimization is unconstrained:

$$\mathbf{w}_{\lambda} \equiv \operatorname*{argmax}_{\mathbf{w}} \left\{ \mathbf{w}' \boldsymbol{\pi} - \lambda \mathbf{w}' \boldsymbol{\Sigma} \mathbf{w} \right\} \tag{4}$$

The solution of this optimization problem yields the relationship between the equilibrium portfolio  $\widetilde{\mathbf{w}}$ , which stems from an average risk-aversion level  $\overline{\lambda}$ and the reference expected returns:

$$\boldsymbol{\pi} \equiv 2\overline{\lambda}\boldsymbol{\Sigma}\widetilde{\mathbf{w}} \tag{5}$$

Therefore,  $\pi$  can be set in terms of  $\widetilde{\mathbf{w}}$ , where BL set exogenously  $\overline{\lambda} \approx 1.2$ . Giacometti *et al.* [3] generalize this argument to stable-distributed markets. Notice that historical information does not play a direct role in the determination of  $\pi$ : this is an instance of the shrinkage approach to estimation risk, see more details in the extended online version of this article.

To calibrate the overall uncertainty level  $\tau$  in equation (2), we can compare this specification with the dispersion of the sample mean in a market where returns are distributed as in equation  $(3)$ independently across time: this implies  $\tau \approx 1/T$ . Satchell and Scowcroft [12] propose an ingenious model where  $\tau$  is stochastic, but extra parameters need to be calibrated. In practice, a tailor-made calibration that spans the interval  $(0, 1)$  is called for in most applications, see also the discussion in [13].

To illustrate, we consider the oversimplified case of an international stock fund that invests in the following six stock market national indexes: Italy, Spain, Switzerland, Canada, United States, and Germany. The covariance matrix of daily returns on the above classes  $\Sigma$  is estimated as follows in terms of the (annualized) volatilities  $\sigma \approx (21\%, 24\%, 24\%, 24\%, 24\%, 24\%, 24\%, 24\%, 24$ 25%, 29%, 31%) and the correlation matrix

| $\mathbf{C} \approx$ |  |     | 54% 62% 25% 41% 59%<br>1 69% 29% 36% 83% |  |
|----------------------|--|-----|------------------------------------------|--|
|                      |  | 15% | 46% 65%<br>47% 39%                       |  |
|                      |  |     |                                          |  |
|                      |  |     | 38%                                      |  |
|                      |  |     |                                          |  |

To determine the prior expectation  $\pi$ , we start from the market-weighted portfolio  $\widetilde{\mathbf{w}} \approx (4\%, 4\%, 4\%, 4\%, 4\%, 4\%, 4\%, 4\%, 4\%, 4\%,$ 5%, 8%, 71%, 8%)' and obtain from equation (5) the annualized expected returns  $\pi \approx (6\%, 7\%, 9\%, 8\%,$ 17%, 10%)'. Finally, we set  $\tau \approx 0.4$  in equation (2).

#### The Views

BL consider views on expectations. In the normal market (1), this corresponds to statements on the parameter  $\mu$ . Furthermore, BL focus on linear views: K views are represented by a  $K \times N$  "pick" matrix **P**, whose generic  $k$ th row determines the relative weight of each expected return in the respective view. To associate uncertainty with the views, BL use a normal model:

$$\mathbf{P}\boldsymbol{\mu} \sim \mathcal{N}(\mathbf{v}, \boldsymbol{\Omega}) \tag{7}$$

where the metaparameters **v** and quantify views and uncertainty thereof, respectively.

If the user has only qualitative views, it is convenient to set the entries of **v** in terms of the volatility induced by the market:

$$v_k \equiv (\mathbf{P}\boldsymbol{\pi})_k + \eta_k \sqrt{(\mathbf{P}\boldsymbol{\Sigma}\mathbf{P}')_{k,k}}, \quad k = 1, \dots, K$$
 (8)

where *ηk* ∈ {−*β,* −*α,* +*α,* +*β*} defines "very bearish", "bearish", "bullish", and "very bullish" views, respectively. Typical choices for these parameters are *α* ≡ 1 and *β* ≡ 2. Also, it is convenient to set as in [6]

$$\mathbf{\Omega} \equiv \frac{1}{c} \mathbf{P} \mathbf{\Sigma} \mathbf{P}' \tag{9}$$

where the scatter structure of uncertainty is inherited from the market volatilities and correlations and *c* represents an overall level of confidence in the views.

To continue with our example, the manager might assess two views: the Spanish index will rise by 12% on an annualized basis, and the spread United States–Germany will experience a negative annualized change of 10%. Therefore, the pick matrix reads

$$\mathbf{P} \equiv \begin{pmatrix} 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & -1 \end{pmatrix} \tag{10}$$

and the annualized views vector becomes **v** ≡ *(*12%*,* −10%*)* . We set the uncertainty in the views to be of the same order of magnitude as that of the market, that is, *c* ≡ 1 in equation *(*9*)*.

#### *The Posterior*

With the above inputs, we can apply Bayes' rule to compute the posterior market model:

$$\mathbf{X}|\mathbf{v};\mathbf{\Omega}\sim\mathcal{N}(\boldsymbol{\mu}_{BL},\boldsymbol{\Sigma}_{BL})\tag{11}$$

where

$$\mu_{BL} = \pi + \tau \Sigma \mathbf{P}' (\tau \mathbf{P} \Sigma \mathbf{P}' + \mathbf{\Omega})^{-1} (\mathbf{v} - \mathbf{P} \pi) \quad (12)$$

$$\mathbf{\Sigma}_{BL} = (1+\tau)\mathbf{\Sigma} - \tau^2 \mathbf{\Sigma} \mathbf{P}' (\tau \mathbf{P} \mathbf{\Sigma} \mathbf{P}' + \mathbf{\Omega})^{-1} \mathbf{P} \mathbf{\Sigma} \tag{13}$$

See the proof in the extended online version of this article.

The normal posterior distribution *(*11*)* represents the modification of the reference model *(*3*)* that incorporates the views *(*7*)*.

#### *The Allocation*

With the posterior distribution, it is now possible to set and solve a mean–variance optimization, possibly under a set of linear constraints, such as boundaries on securities/asset classes, or a budget constraint. This quadratic programming problem can be easily solved numerically. The ensuing efficient frontier represents a gentle twist to equilibrium that reflects the views without extreme corner solutions.

In our example, we assume the standard long-only and budget constraints, that is, **w** ≥ **0** and **w 1** ≡ 1. In Figure 1, we plot the efficient frontier from the reference model *(*3*)* and from the posterior model *(*11*)*. Consistently with the views, the exposure to the Spanish market increases for lower risk values; the exposure to Germany increases across all levels of risk aversion; and the exposure to the US market decreases.

## **Related Literature**

The BL posterior distribution *(*11*)* presents two puzzles. On one extreme, when the views are uninformative, that is, → **∞** in equation *(*7*)*, one would expect the posterior to equal the reference model (3). On the other extreme, when the confidence in the views **v** is full, that is, → **0**, one would expect the posterior to yield scenario analysis: the user inputs deterministic scenarios **v** ≡ *(v*1*,...,vK)* for the factor combinations, resulting in a conditional distribution

$$\mathbf{X}|\mathbf{v} \sim \mathcal{N}(\boldsymbol{\mu}|\mathbf{v}, \boldsymbol{\Sigma}|\mathbf{v}) \tag{14}$$

where

$$\mu|\mathbf{v} \equiv \boldsymbol{\pi} + \boldsymbol{\Sigma} \mathbf{P}' (\mathbf{P} \boldsymbol{\Sigma} \mathbf{P}')^{-1} (\mathbf{v} - \mathbf{P} \boldsymbol{\pi}) \qquad (15)$$

$$\mathbf{\Sigma}|\mathbf{v} \equiv \mathbf{\Sigma} - \mathbf{\Sigma} \mathbf{P}' (\mathbf{P} \mathbf{\Sigma} \mathbf{P}')^{-1} \mathbf{P} \mathbf{\Sigma} \tag{16}$$

see, for example, [9].

The BL model does not satisfy the above two limit conditions. However, this issue can be fixed as in [6], by rephrasing the model in terms of views on the market **X**, instead of the parameter *µ*. As we show in the extended online version of this article, the posterior then reads

$$\mathbf{X}|\mathbf{v}; \mathbf{\Omega} \sim \mathcal{N}(\boldsymbol{\mu}_{\mathrm{BL}}, \boldsymbol{\Sigma}_{\mathrm{BL}}) \tag{17}$$

![](_page_2_Figure_1.jpeg)

**Figure 1** BL: efficient frontier twisted according to the views

where

$$\mu_{BL} \equiv \boldsymbol{\pi} + \boldsymbol{\Sigma} \mathbf{P}' (\mathbf{P} \boldsymbol{\Sigma} \mathbf{P}' + \boldsymbol{\Omega})^{-1} (\mathbf{v} - \mathbf{P} \boldsymbol{\pi}) \qquad (18)$$

$$\mathbf{\Sigma}_{BL} \equiv \mathbf{\Sigma} - \mathbf{\Sigma} \mathbf{P}' (\mathbf{P} \mathbf{\Sigma} \mathbf{P}' + \mathbf{\Omega})^{-1} \mathbf{P} \mathbf{\Sigma} \tag{19}$$

These formulas are very similar to their counterparts *(*12*)*–*(*13*)* in the original BL model. However, the parameter *τ* in equation *(*2*)* is no longer present and the two limit conditions are now satisfied.

Therefore, scenario analysis processes views on market expectations with infinite confidence and the BL model overlays uncertainty to the views by means of Bayesian formulas. Qian and Gorman [11] use a conditional/marginal factorization to input views on volatilities and correlations in addition to expectations. Pezier [10] processes full and partial views on expectations and covariances by least discrimination. Almgren and Chriss [1] provide a framework to express ranking, "lax" views on expectations.

The posterior formulas *(*12*)*–*(*13*)*, their modified versions *(*18*)*–*(*19*)*, as well as the formulas in the above literature can be applied to any *normal* distribution, not necessarily the equilibrium *(*5*)*. Accordingly, Meucci [7] applies the above approaches to fully generic risk factors that map nonlinearly into the final P&L, instead of securities returns.

To further extend all the above approaches to nonnormal markets, as well as fully general nonlinear views from possibly multiple users, Meucci [8] uses entropy minimization and opinion pooling: since no costly repricing is ever necessary, this technique covers even the most complex derivatives.

## **Acknowledgments**

The author gratefully acknowledges the very helpful feedback from Bob Litterman, Ninghui Liu, and Jay Walters.

## **References**

- [1] Almgren, R. & Chriss, N. (2006). Optimal Portfolios from Ordering Information, *Journal of Risk* **9**, 1–47.
- [2] Black, F. & Litterman, R. (1990). Asset allocation: combining investor views with market equilibrium, *Goldman Sachs Fixed Income Research* September.
- [3] Giacometti, M., Bertocchi, I., Rachev, T.S. & Fabozzi, F. (2007). Stable distributions in the Black-Litterman approach to asset allocation, *Quantitative Finance* **7**, 423–433.
- [4] He, G. & Litterman, R. (2002). *The Intuition Behind Black-Litterman Model Portfolios*. ssrn.com.
- [5] Idzorek, T.M. (2004). *A Step-by-Step Guide to the Black-Litterman Model*, Zephyr Associates Publications.
- [6] Meucci, A. (2005). *Risk and Asset Allocation*, Springer.
- [7] Meucci, A. (2009). Enhancing the Black-Litterman and Related Approaches: Views and Stress-Test on Risk Factors, *Journal of Asset Management* **10**(2), 89–96.
- [8] Meucci, A. (2008). Fully flexible views: theory and practice, *Risk* **21**, 97–102. Available at symmys.com *>* Reasearch *>* Working Papers.

- [9] Mina, J. & Xiao, J.Y. (2001). *Return to RiskMetrics: The Evolution of a Standard*, Risk Metrics Publications.
- [10] Pezier, J. (2007). *Global Portfolio Optimization Revisited: A Least Discrimination Alternative to Black-Litterman*. ICMA Centre Discussion Papers in Finance.
- [11] Qian, E. & Gorman, S. (2001). Conditional distribution in portfolio theory, *Financial Analyst Journal* **57**, 44–51.
- [12] Satchell, S. & Scowcroft, A. (2000). A demystification of the Black-Litterman model: managing quantitative and traditional construction, *Journal of Asset Management* **1**, 138–150.
- [13] Walters, J. (2008). *The Black-Litterman Model: A Detailed Exploration*. blacklitterman.org.

## **Related Articles**

#### **Capital Asset Pricing Model**; **Risk–Return Analysis**.

ATTILIO MEUCCI
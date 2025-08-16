# Diversification

Diversification involves spreading investments among various assets in order to improve portfolio performance in some manner. Mathematical analysis of portfolio diversification was introduced in 1952 by Markowitz [6] with his concept of mean/variance portfolio efficiency. A portfolio was called *efficient* if, among all portfolios of the same assets, the portfolio had minimum variance for a given expected rate of return. Hence, in the setting of expected portfolio return and variance, portfolio diversification served to control the risk of a portfolio. In 1982, Fernholz and Shay [3] showed that if the expected compound growth rate of a portfolio is considered rather than the expected rate of return, then portfolio diversification can increase the expected growth rate as well as control risk.

### **Mean/Variance Portfolio Diversification**

Suppose that a portfolio **P** holds *n* assets  $X_1, \ldots, X_n$ , and let  $p_1, \ldots, p_n$  be the weights, or proportions of each corresponding asset in the portfolio. In this case, the weights need not be all positive, but they must add up to 1,  $p_1 + \cdots + p_n = 1$ . A negative value of  $p_i$  indicates a short sale of  $\mathbf{X}_i$ .

Suppose that  $\alpha_i$  is the expected rate of return of  $\mathbf{X}_i$  and that  $\sigma_{ij}$  is the covariance of return between  $\mathbf{X}_i$  and  $\mathbf{X}_j$ , with the variance of return of  $\mathbf{X}_i$  written as  $\sigma_i^2 = \sigma_{ii}$ . With this notation, the expected rate of return of  $\mathbf{P}$  is given by

$$\alpha_P = \sum_{i=1}^n p_i \alpha_i \tag{1}$$

and the variance of  $\mathbf{P}$  is

$$\sigma_P^2 = \sum_{i,j=1}^n p_i p_j \sigma_{ij} \tag{2}$$

In mean/variance theory [6, 7], a portfolio is optimally diversified if the portfolio variance  $\sigma_p^2$  is minimal under the constraints

$$p_1 + \dots + p_n = 1 \quad \text{and} \quad \alpha_P \ge A \tag{3}$$

where  $A$  is a given constant. For a *long-only* portfolio, the additional constraints  $p_1 \ge 0, \ldots, p_n \ge 0$  are imposed.

In mean/variance theory, there is no specific measure of portfolio diversification, but it is understood that diversification can reduce the portfolio variance without lowering the expected return of the portfolio. Portfolios with minimum variance for a given value of portfolio return are called *efficient* portfolios, and we say that efficient portfolios lie on the efficient frontier in mean/variance space.

### **Diversification and Expected Growth Rate**

The expected rate of return of a financial asset is more precisely called the expected *arithmetic* rate of return of the asset. Another measure of portfolio performance is the expected *logarithmic* rate of return of an asset, and this logarithmic rate is frequently called the expected (compound) growth rate of the asset. It was shown in  $[1, 3]$  that the expected growth rate of a financial asset is a better indicator of longterm performance than the expected return, and, for this reason, it is likely to be preferable for multiperiod performance analysis (see [4]). The relation between the expected rate of return  $\alpha$  of an asset and its expected growth rate  $\gamma$  is

$$\alpha = \gamma + \frac{1}{2}\sigma^2 \tag{4}$$

where  $\sigma^2$  is the variance of the asset. Equation (4) is an application of Itô's rule for stochastic integration [5]; the relation is exact for continuous-time analysis and approximate for multiperiod discretetime analysis (see [1]).

For the portfolio **P**, the portfolio variance  $\sigma_P^2$  is the same whether it is measured with regard to the portfolio return or the portfolio growth rate. However, the relationship between the portfolio growth rate and the growth rates of the individual assets is more complicated than the corresponding relationship for arithmetic returns given by equation (1). If the assets  $\mathbf{X}_1, \ldots, \mathbf{X}_n$  have growth rates  $\gamma_1, \ldots, \gamma_n$ , then the growth rate of  $\mathbf{P}$  is given by

$$\gamma_P = \sum_{i=1}^n p_i \gamma_i + \gamma_P^* \tag{5}$$

where

$$\gamma_P^* = \frac{1}{2} \left( \sum_{i=1}^n p_i \sigma_i^2 - \sum_{i,j=1}^n p_i p_j \sigma_{ij} \right) \tag{6}$$

is called the *excess growth rate* of **P** (see  $[1-3]$ ). From equation  $(2)$ , we see that the excess growth rate is half the difference of the weighted average of the variances of the assets in the portfolio minus the variance of the portfolio itself. We see from equations  $(5)$  and  $(6)$  that diversification affects both the variance and the expected growth rate of the portfolio.

# **Excess Growth and the Efficacy** of Diversification

The excess growth rate  $\gamma_p^*$  of the portfolio **P** can be used as a measure of the *efficacy* of diversification of the portfolio. The more effective the diversification, the greater the difference between the average variance of the assets and the portfolio variance, and the greater the contribution to the portfolio growth rate.

Equation (6) remains valid if the covariances  $\sigma_{ij}$ are replaced by covariances measured relative to some *numeraire* asset (see [1]), so in this sense the excess growth rate is *numeraire invariant*. Suppose  $\mathbf{Z}$  is a financial asset; then the covariance of  $\mathbf{X}_i$  and  $\mathbf{X}_{i}$  relative to  $\mathbf{Z}$  is given by

$$\sigma_{ij/Z} = \sigma_{ij} - \sigma_{iZ} - \sigma_{jZ} + \sigma_Z^2 \tag{7}$$

where  $\sigma_{iZ}$  is the covariance of  $\mathbf{X}_i$  with  $\mathbf{Z}$ ,  $\sigma_{jZ}$  is the covariance of  $\mathbf{X}_j$  with  $\mathbf{Z}$ , and  $\sigma_Z^2$  is the variance of  $\mathbf{Z}$ . With the notation  $\sigma_{i/Z}^2 = \sigma_{ii/Z}$ , equation (6) becomes

$$\gamma_P^* = \frac{1}{2} \left( \sum_{i=1}^n p_i \sigma_{i/Z}^2 - \sum_{i,j=1}^n p_i p_j \sigma_{ij/Z} \right) \tag{8}$$

In particular, if the asset  $\mathbf{Z}$  is the portfolio  $\mathbf{P}$  itself, then the variance of  $\mathbf{P}$  relative to itself vanishes:

$$\sum_{i,j=1}^{n} p_i p_j \sigma_{ij/P} = \sigma_{P/P}^2 = 0 \tag{9}$$

so we have simply

$$\gamma_P^* = \frac{1}{2} \sum_{i=1}^n p_i \sigma_{i/P}^2 \tag{10}$$

If **P** is a long-only portfolio, then all the terms  $p_i \sigma_{i/P}^2$ are nonnegative, and it follows from equation  $(10)$ that  $\gamma_{P}^{*}$  is also nonnegative. Hence, for such a portfolio, diversification will not decrease the portfolio growth rate, and is likely to increase it.

# The Efficacy of Diversification in the US **Stock Market**

Here, we shall consider an example of the excess growth rate as a measure of efficacy of diversification. Figure 1 shows the smoothed, annualized excess growth rate for the US stock market over most of the twentieth century. The data used to construct Figure 1 come from the monthly stock database of the Center for Research in Securities Prices (CRSP) at the University of Chicago. The stocks included in this market are those traded on the New York Stock Exchange (NYSE), the American Stock Exchange (AMEX), and the NASDAQ Stock Market, with adjustments made for real estate investment trusts (REITs), closed-end funds, and American depository receipts (ADRs). Until 1962, the data included only NYSE stocks, after July 1962 AMEX stocks were included, and at the beginning of 1973 NASDAQ stocks were included. The number of stocks in this market varies from a few hundred in 1927 to about 7500 after 1999.

We see in Figure 1 that the excess growth rate of the market has varied considerably over time, from an estimated minimum excess growth rate

![](_page_1_Figure_18.jpeg)

Figure 1 Efficacy of diversification of the US stock market, as measured by the market excess growth rate, 1927-2005

of about 1% a year in the 1950s to a maximum of about 16% a year near 2000. The volatility of the stocks has a significant effect on the efficacy of diversification, with higher excess growth rates appearing in the bubble years of the 1930s, the 1970s, and around 2000, even though during these periods there was concentration of capital into the larger stocks. In contrast, the excess growth rate increased only modestly with the increase in the number of stocks in the market from under 1000 in the early years to over 5000 in the later years. Hence, in the absence of higher volatility, the addition of new assets did not significantly increase the efficacy of diversification over the observed period.

#### [2] Fernholz, R. & Karatzas, I. (2008). Stochastic portfolio theory: an overview, in *Mathematical Modelling and Numerical Methods in Finance*, A. Bensoussan, Q. Zhang & P. Ciarlet, eds, Elsevier, Amsterdam.

- [3] Fernholz, R. & Shay, B. (1982). Stochastic portfolio theory and stock market equilibrium, *Journal of Finance* **37**, 615–624.
- [4] Hughson, E., Stutzer, M. & Yung, C. (2006). The misuse of expected returns, *Financial Analysts Journal* **62**, 88–96.
- [5] Ito, K. (1951). On stochastic differential equations, ˆ *Memoirs of the American Mathematical Society* **4**, 1–51.
- [6] Markowitz, H. (1952). Portfolio selection, *Journal of Finance* **7**, 77–91.
- [7] Markowitz, H. (1959). *Portfolio Selection*, John Wiley & Sons, New York.

ROBERT FERNHOLZ

## **References**

[1] Fernholz, R. (2002). *Stochastic Portfolio Theory*, Springer-Verlag, New York.
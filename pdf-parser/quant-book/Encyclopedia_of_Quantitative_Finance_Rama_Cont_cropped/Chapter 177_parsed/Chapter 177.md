# **Credit Portfolio** Simulation<sup>a</sup>

## **Portfolio Modeling**

In risk management, quantitative techniques are mainly used for measuring the risk in a portfolio of assets rather than computing the prices of individual securities. The quantification of portfolio risk is traditionally split into separate calculations for market and credit risk, which are performed in different types of portfolio models. This article focuses on credit risk, more precisely on simulation techniques in structural credit portfolio models. We refer to [4] for a comprehensive exposition of Monte Carlo (MC) methods in quantitative finance including applications in market risk models.

In a typical bank, risk capital for credit risk far outweighs capital requirements for any other risk class. Key drivers of credit risk are concentrations in a bank's credit portfolio. Depending on their formulation, credit portfolio models can be divided into reduced-form models and structural (or firm-value) models (see Reduced Form Credit Risk Models; Structural Default Risk Models). The progenitor of all structural models is the model of Merton [13], which links the default of a firm to the relationship between its assets and the liabilities that it faces at the end of a given time period  $[0, T]$ . More precisely, in a structural credit portfolio model, the  $i$ th counterparty defaults if its ability-to-pay variable  $A_i$  falls below a default threshold  $D_i$ : the default event at time T is defined as  $\{A_i \leq D_i\} \subseteq \Omega$ , where  $A_i$  is a real-valued random variable on the probability space  $(\Omega, \mathcal{A}, \mathbb{P})$ and  $D_i \in \mathbb{R}$ . The portfolio loss variable is defined by

$$L := \sum_{i=1}^{n} l_i \cdot \mathbf{1}_{\{A_i \le D_i\}} \tag{1}$$

where *n* denotes the number of counterparties and  $l_i$  is the loss-at-default of the  $i$ th counterparty. To reflect risk concentrations, each  $A_i$  is decomposed into a sum of systematic factors  $X_1, \ldots, X_m$ , which are often identified with geographic regions or industries, and an idiosyncratic (or firm-specific) factor  $Z_i$ , that

is  $A_i$  has the representation

$$A_i = \sqrt{R_i^2} \sum_{j=1}^m w_{ij} X_j + \sqrt{1 - R_i^2} Z_i \qquad (2)$$

The idiosyncratic factors are independent of each other as well as independent of the systematic factors. It is usually assumed that the factors follow a multivariate Gaussian distribution. We refer to this class of models as *Gaussian multifactor models*.<sup>b</sup> The impact of the risk factors on  $A_i$  is determined by  $R_i^2 \in [0, 1]$  and the factor weights  $w_{ii} \in \mathbb{R}$ .

To quantify portfolio risk, measures of risk are applied to the portfolio loss distribution  $(1)$ . The most widely used risk measures in banking are Value-at-Risk and expected shortfall: Value-at-Risk Va $R_{\alpha}(L)$ of L at level  $\alpha \in (0, 1)$  is simply an  $\alpha$ -quantile of L, whereas expected shortfall of L at level  $\alpha$  is defined by

$$\mathrm{ES}_{\alpha}(L) := (1-\alpha)^{-1} \int_{\alpha}^{1} \mathrm{VaR}_{u}(L) \mathrm{d}u$$

For most practical applications, the average of all losses above the  $\alpha$ -quantile is a good approximation of  $\text{ES}_{\alpha}(L)$ : for  $c := \text{VaR}_{\alpha}(L)$  we have

$$\mathrm{ES}_{\alpha}(L) \approx \mathrm{E}(L|L>c) = (1-\alpha)^{-1} \int L \cdot \mathbf{1}_{\{L>c\}} \, \mathrm{d}\mathbb{P}$$
(3)

This approximation is an exact equality unless the distribution of  $L$  has an atom at  $c$ , a situation that very rarely arises in practice.

#### **Simulation Techniques**

Since the portfolio loss distribution  $(1)$  does not have analytic form, the actual calculation and allocation of portfolio risk is a challenging problem. Saddlepoint techniques have been successfully applied to certain types of portfolios; see, for example, [10] or see Saddlepoint Approximation. The most flexible approach, however, is based on MC simulation of the portfolio loss distribution. The following are the main steps in generating one MC sample:

1. calculation of a sample  $(x_1, \ldots, x_m)$  of the correlated systematic factors and a sample  $(z_1, \ldots, z_n)$ of the independent idiosyncratic factors;

- 2. calculation of the corresponding values  $(a_1, \ldots, a_n)$  $a_n$ ) of the ability-to-pay variables using equation  $(2);$
- 3. calculation of the set of defaulted counterparties defined by  $Def := \{i \in \{1, \ldots, n\} \mid a_i < D_i\};$
- 4. calculation of the portfolio loss: the sum  $\sum_{i \in Def} l_i$  is a sample of the portfolio loss distribution

The MC scenarios of the portfolio loss distribution are used as input for the calculation of risk measures. As an example, we compute expected shortfall with respect to the  $\alpha = 99.9\%$  quantile based on  $k = 100\,000$  MC samples  $s_1 \ge s_2 \ge \ldots \ge s_k$  of the portfolio loss L. Then  $ES_{\alpha}(L)$  becomes

$$(1-\alpha)^{-1} \int L \cdot \mathbf{1}_{\{L>c\}} \, \mathrm{d}\mathbb{P} \approx \sum_{i=1}^{100} s_i/100 \qquad (4)$$

Since  $ES_{\alpha}(L)$  is calculated as the average of 100 samples only, the MC estimate is subject to large statistical fluctuations and is numerically unstable. This is even truer for expected shortfall contributions of individual transactions. A significantly higher number of samples has to be computed, which makes straightforward MC simulation impracticable for large credit portfolios.

Different techniques have been developed that reduce the variance of MC simulations and—as a consequence—the number of samples required for stable results. We refer to [4] for a general introduction to variance reduction techniques including control variates, antithetic variables, stratified sampling, moment matching, and importance sampling. Recent research  $[3, 5-9, 12, 14]$  has shown that importance sampling is particularly efficient for stabilizing MC simulation in Gaussian multifactor models. Importance sampling attempts to reduce variance by changing the probability measure used for generating MC samples. In the above setting, the integral in equation  $(3)$  is replaced by the equivalent integral on the right-hand side of the equation

$$\int L \cdot \mathbf{1}_{\{L>c\}} \, \mathrm{d}\mathbb{P} = \int L \cdot \mathbf{1}_{\{L>c\}} \cdot f \, \mathrm{d}\bar{\mathbb{P}} \qquad (5)$$

where  $\mathbb{P}$  is absolutely continuous with respect to the probability measure  $\bar{\mathbb{P}}$  and has (Radon–Nikodym) density  $f$ . This change of measure results in the MC estimate

$$\mathrm{ES}_{\alpha}(L)_{k,\bar{\mathbb{P}}} := \frac{1}{k} \sum_{i=1}^{k} L_{\bar{\mathbb{P}}}(i) \cdot \mathbf{1}_{\{L_{\bar{\mathbb{P}}}(i) > c\}} \cdot f(i) \qquad (6)$$

where  $L_{\bar{p}}(i)$  is a realization of the portfolio loss L under the probability measure  $\bar{\mathbb{P}}$  and  $f(i)$  is the corresponding value of the density function. The objective is to choose the probability measure  $\bar{\mathbb{P}}$  in such a way that the variance of the MC estimate for the integral (5) is minimal under  $\bar{\mathbb{P}}$ . A general formula for the optimal importance sampling measure  $\bar{\mathbb{P}}$  is given in [15], which transforms equation (6) into a zerovariance estimator. However, since the construction requires knowledge of the integral (3) itself, the optimal measure cannot be used in the actual calculation. Nevertheless, it provides guidance on the design of an effective importance sampling strategy. Another technique for measure transformation, called *exponential tilting*, applies exponential families of distributions, which are specified by cumulant generating functions [1, 4]. As a general rule, detailed knowledge about the model (often in the form of asymptotic approximations) is indispensable for the construction of importance sampling algorithms. It is precisely this feature of importance sampling that makes the practical application more difficult but, on the other hand, increases the effectiveness of the methodology.

Importance sampling in Gaussian multifactor models utilizes the conditional independence of ability-to-pay variables by splitting the simulation of the portfolio loss distribution into two steps (compare to [11] in the more general context of mixture models). In a first step, importance sampling is used to simulate the systematic factors, and then the independence of the ability-to-pay variables conditional on systematic scenarios is exploited, for example, by another application of importance sampling or by limit theorems  $[7, 8]$ .

A natural importance sampling measure  $\bar{\mathbb{P}}$  for the systematic factors is a negative shift, that is, the systematic factors have a negative mean under  $\mathbb{P}$ , which enforces a higher number of defaults and therefore increases the stability of the MC estimate. For calculating the shift, Glasserman and Li [7] minimize an upper bound on the second moment of the importance sampling estimator of the tail probability. Furthermore, they show that the corresponding importance sampling scheme is asymptotically optimal. The approach in  $[8, 9]$  utilizes the infinite granularity approximation of the portfolio loss distribution (compare to [16]). More precisely, the original portfolio  $P$  is approximated by a homogeneous and infinitely granular portfolio  $\bar{P}$ . The loss distribution of  $\overline{P}$  can be specified by a Gaussian one-factor model. The calculation of the shift of the systematic factors is now done in two steps: in the first step, the optimal mean is calculated in the one-factor setting and then the scalar mean is lifted to a mean vector for the systematic factors in the original multifactor model. Other importance sampling techniques [3, 6] are based on the Robbins-Monro stochastic approximation method or use large deviation analysis to calculate multiple mean shifts.

The efficiency of the proposed variance reduction schemes heavily depends on the portfolio characteristics. For example, the technique proposed in [8, 9] is tailored to large and well-diversified portfolios. For those portfolios the analytic loss distribution of the infinitely granular portfolio provides an excellent fit, which typically reduces the variance—and therefore the number of required MC scenarios-by a factor of more than 100. Smaller portfolios with low dependence on systematic factors, on the other hand, are dominated by idiosyncratic risk, which increases the relative importance of variance reduction techniques on idiosyncratic factors [7, 8], for example, importance sampling based on exponential tilting.

### **End Notes**

<sup>a.</sup>The views expressed in this article are those of the author and do not necessarily reflect the position of Deutsche Bank AG.

<sup>b.</sup>A survey on credit portfolio modeling can be found in [2, 11].

#### References

- Barndorff-Nielsen, O. (1978). Information and Exponen-[1] tial Families, Wiley.
- [2] Bluhm, C., Overbeck, L. & Wagner, C. (2002). An Introduction to Credit Risk Modeling, CRC Press/Chapman & Hall.

- Egloff, D., Leippold, M., Jöhri, S. & Dalbert, C. [3] (2005). Optimal Importance Sampling for Credit Portfolios with Stochastic Approximations. Working paper, Zürcher Kantonalbank, Zurich.
- Glasserman, P. (2004). Monte Carlo Methods in Finan-[4] cial Engineering, Springer.
- [5] Glasserman, P. (2005). Measuring marginal risk contributions in credit portfolios, Journal of Computational Finance 9. 1-41.
- Glasserman, P., Kang, W. & Shahabuddin, P. (2007). [6] Fast Simulation of Multifactor Portfolio Credit Risk. Working paper, Columbia University, New York.
- Glasserman, P. & Li, J. (2005). Importance sam-[7] pling for portfolio credit risk, Management Science 51, 1643-1656.
- Kalkbrener, M., Kennedy, A. & Popp, M. (2007). [8] Efficient calculation of expected shortfall contributions in large credit portfolios, Journal of Computational Finance 11, 45-77.
- Kalkbrener, M., Lotter, H. & Overbeck, L. (2004). [9] Sensible and efficient capital allocation for credit portfolios, Risk 17(1), S19-S24.
- [10] Martin, R., Thompson, K. & Browne, C. (2001). Taking to the saddle, Risk 14(6), 91-94.
- [11] McNeil, A.J., Frey, R. & Embrechts, P. (2005). *Quan*titative Risk Management: Concepts, Techniques, and Tools, Princeton University Press.
- [12] Merino, S. & Nyfeler, M. (2004). Applying importance sampling for estimating coherent credit risk contributions, *Quantitative Finance* 4, 199-207.
- [13] Merton, R. (1974). On the pricing of corporate debt: the risk structure of interest rates, Journal of Finance 29, 449-470.
- [14] Morokoff, W.J. (2004). An importance sampling method for portfolios of credit risky assets, Proceedings of the 2004 Winter Simulation Conference, IEEE Press, pp. 1668-1676.
- [15] Rubinstein, R.Y. (1981). Simulation and the Monte Carlo Method, Wiley.
- [16] Vasicek, O. (2002). Loan portfolio value, *Risk* **15**(12),  $160 - 162.$

## **Related Articles**

Large Pool Approximations; Monte Carlo Simulation; Structural Default Risk Models; Saddlepoint Approximation; Variance Reduction.

MICHAEL KALKBRENER
## **Economic Capital** Allocation

In a bank, risk is usually quantified in terms of risk capital (or economic capital). The reason for the close connection between risk and capital is the fact that the main purpose of the bank's capital is to provide protection against extreme losses, that is, capital invested in safe and liquid assets should ensure solvency of the bank even in adverse economic scenarios. Hence, the capital requirements of a bank are determined by its risk profile. The actual calculation is based on risk measures like Value-at-Risk (VaR) or expected shortfall; see [12] or **Convex Risk Measures** for an exposition of the theory of risk measures.

Techniques for measuring risk are not only required for capital management but are also prerequisites for profitability analysis and portfolio optimization. The development of the theoretical relationship between risk and expected return is built on two economic theories: portfolio theory and capital market theory [18, 19, 25]. Portfolio theory deals with the selection of portfolios that maximize the expected returns consistent with individually acceptable levels of risk, whereas capital market theory focuses on the relationship between security returns and risk. These theories also provide a natural framework for measuring profitability. The profitability analysis is commonly carried out by expressing the risk-return relationship as simple rational functions of risk and return components. The two basic variants of these so-called risk adjusted ratios are known as *RORAC* or *RAROC*, respectively; see  $[20]$  for details.

Portfolio optimization and the profitability analysis of individual business units, portfolios, and transactions require the quantification of risk at the respective levels of the bank's hierarchy. In line with portfolio theory, the main objective of this analysis is to measure the contribution of each unit to the total risk of the bank and to allocate risk capital accordingly. For a mathematical formalization of the allocation problem, we assume that a risk measure  $\rho$  has been fixed and that X is a portfolio that consists of subportfolios  $X_1, \ldots, X_m$ . The objective is to distribute the risk capital  $k := \rho(X)$  of the portfolio  $X = X_1 + \cdots + X_m$  to its subportfolios, that is, to

compute risk contributions  $k_1, \ldots, k_m$  of  $X_1, \ldots, X_m$ with  $k = k_1 + \cdots + k_m$ .

In recent years, theoretical and practical aspects of different allocation schemes have been analyzed in several articles; see for instance  $[5-8, 11, 14, 22, 23,$ 26–28]. An allocation scheme proposed by several authors is the allocation by the gradient or Euler principle: the capital allocated to the subportfolio  $X_i$  of  $X$  is the derivative of the associated risk measure  $\rho$  at X in the direction of  $X_i$  (see formula (9) for a precise formalization). In the following, we review a simple axiomatization of capital allocation proposed in [15]. The main axioms are the property that the entire risk capital of a portfolio is allocated to its subportfolios and a diversification property that is closely linked to the subadditivity of the underlying risk measure. It turns out that in this framework the Euler principle is an immediate consequence of the proposed axioms.

## **Axioms for Capital Allocation**

Let  $(\Omega, \mathcal{A}, \mathbb{P})$  be a probability space,  $L^0$  the space of all equivalence classes of real-valued random variables on  $\Omega$  and V a subspace of the vector space  $L^0$ , which represents portfolios. More precisely, we will identify each portfolio  $X$  with its loss function, that is, X is an element of V and  $X(\omega)$  specifies the loss of X at a future date in state  $\omega \in \Omega$ . We assume that a function  $\rho: V \to \mathbb{R}$  has been defined. For each  $X \in V$ ,  $\rho(X)$  specifies the risk capital associated with portfolio  $X$ . At this point, we do not require that the risk measure  $\rho$  has specific properties.

The axiomatization in  $[15]$  is based on the assumption that the capital allocated to subportfolio  $X_i$  only depends on  $X_i$  and  $X$  but not on the decomposition of the remainder  $X - X_i = \sum_{i \neq i} X_j$  of the portfolio. Hence, a capital allocation can be considered as a function  $\Lambda$  from  $V \times V$  to  $\mathbb{R}$ . Its interpretation is that  $\Lambda(X, Y)$  represents the capital allocated to the portfolio  $X$  considered as a subportfolio of portfolio  $Y$ .

Definition 1 (Axiomatization of Capital Allocation). A function  $\Lambda: V \times V \to \mathbb{R}$  is called a capital *allocation with associated risk measure*  $\rho$  *if it satisfies* the condition  $\Lambda(X, X) = \rho(X)$  for all  $X \in V$ , that is, if the capital allocated to  $X$  (considered as standalone portfolio) is the risk capital  $\rho(X)$  of X. The following requirements for  $\Lambda$  are proposed. The capital allocation  $\Lambda$  is called

$$\begin{array}{ll}\n\text{linear :} & \forall a, b \in \mathbb{R}, X, Y, Z \in V \tag{1} \\
\Lambda(aX + bY, Z) = a\Lambda(X, Z) + b\Lambda(Y, Z) & \forall X, Y \in V \tag{2} \\
\text{diversifying :} & \forall X, Y \in V \tag{2} \\
\Lambda(X, Y) \leq \Lambda(X, X) & \forall X \in V \tag{3} \\
\text{continuous at } Y \in V : & \forall X \in V \tag{3} \\
\lim_{s \to 0} \Lambda(X, Y + \epsilon X) = \Lambda(X, Y) & \forall X \in V \tag{3}\n\end{array}$$

The first two axioms ensure that the risk capital of the portfolio equals the sum of the (contributory) risk capital of its subportfolios and that the capital allocated to a subportfolio  $X$  never exceeds the risk capital of  $X$  considered as a stand-alone portfolio. If  $\Lambda$  is continuous at  $Y \in V$ , then small changes to the portfolio  $Y$  only have a limited effect on the risk capital of its subportfolios. We refer to [7, 8] for alternative axiomatizations based on game-theoretic concepts.

The above axiom system provides a close link between risk measures and capital allocation rules. First, given a capital allocation  $\Lambda$  the corresponding risk measure  $\rho$  is obviously given by the values of  $\Lambda$  on the diagonal, that is,  $\rho(X) = \Lambda(X, X)$ . Conversely, assume that a risk measure  $\rho$  is

$$\begin{array}{l} \textit{positively homogeneous:} \\ \rho(aX) = a\rho(X) \\ \textit{subadditive:} \\ \rho(X+Y) \leq \rho(X) + \rho(Y) \end{array}$$

Then, the corresponding capital allocation  $\Lambda_{\rho}$  can be constructed as follows: let  $V^*$  be the set of real linear functionals on  $V$  and for a given risk measure  $\rho$  consider the subset

$$H_{\rho} := \{ h \in V^* \mid h(X) \le \rho(X) \text{ for all } X \in V \} \quad (6)$$

It is an easy consequence of the Hahn-Banach theorem (see, for instance, Theorem II.3.10 in [10]) that for a positively homogeneous and subadditive risk measure  $\rho$ 

$$\rho(X) = \max\{h(X) \mid h \in H_{\rho}\}\tag{7}$$

for all  $X \in V$ . Hence, for every  $Y \in V$  there exists an  $h_{\nu}^{\rho} \in H_{\rho}$  with  $h_{\nu}^{\rho}(Y) = \rho(Y)$ . This allows to define

a capital allocation  $\Lambda_{\rho}$  by

$$\Lambda_{\rho}(X,Y) := h^{\rho}_{Y}(X) \tag{8}$$

The set  $H_{\rho}$  can be interpreted as a collection of (generalized) scenarios: the capital allocated to a subportfolio  $X$  of portfolio  $Y$  is simply the loss of  $X$ under scenario  $h_{\rm v}^{\rho}$ .

The following theorem (Theorem  $4.2$  in [15]) states the equivalence between positively homogeneous, subadditive (but not necessarily coherent) risk measures and linear, diversifying capital allocations.

**Theorem 1** (Existence of Capital Allocations). Let  $\rho: V \to \mathbb{R}.$ 

$$\forall a \ge 0, \ X \in V \tag{4}$$

$$\forall X, Y \in V \tag{5}$$

- 1. If there exists a linear, diversifying capital allocation  $\Lambda$  with associated risk measure  $\rho$ , then  $\rho$ is positively homogeneous and subadditive.
- 2. If  $\rho$  is positively homogeneous and subadditive, then  $\Lambda_{\rho}$  is a linear, diversifying capital allocation with associated risk measure  $\rho$ .

If a linear, diversifying capital allocation  $\Lambda$  is moreover continuous at a portfolio  $Y \in V$ , then it is uniquely determined by the directional derivative of its associated risk measure, as the next theorem (Theorem 4.3 in  $[15]$ ) shows.

**Theorem 2** (Uniqueness of Capital Allocations). Let  $\rho$  be a positively homogeneous and subadditive risk measure and  $Y \in V$ . Then the following three conditions are equivalent:

- 1.  $\Lambda_{o}$  is continuous at Y, that is, for all  $X \in V$  $\lim_{\epsilon \to 0} \Lambda_{\rho}(X, Y + \epsilon X) = \Lambda_{\rho}(X, Y).$
- 2. The directional derivative

$$\lim_{\epsilon \to 0} \frac{\rho(Y + \epsilon X) - \rho(Y)}{\epsilon} \tag{9}$$

exists for every  $X \in V$ .

3. There exists a unique  $h \in H_{\rho}$  with  $h(Y) = \rho(Y)$ .

If these conditions are satisfied then  $\Lambda_{\rho}(X,Y)$  equals the directional derivative (9) for all  $X \in V$ , that is,  $\Lambda_{\rho}$  is given by the Euler principle.

If the equivalent conditions in Theorem 2 are not satisfied for  $Y \in V$ , then the two-sided directional derivative (9) does not exist for all  $X$  and the capital allocation  $\Lambda_{\rho}(., Y)$  is not uniquely defined. In a recent article, Cherny and Orlov [6] propose two different solutions to this problem: either the replacement of the two-sided directional derivative by a one-sided directional derivative or a modification of the axiomatization in Definition 1 obtained by adjusting the continuity axiom and adding law invariance. They show that for a spectral risk measure  $[1, 27]$ , (see also Spectral Measures of Risk), there exists a unique capital allocation satisfying the proposed axiom system. Capital allocations for spectral risk measures are also investigated in [23]. An axiomatic characterization of capital allocations of coherent risk measures  $[3]$  is given in  $[16]$ .

The Euler principle is an allocation scheme that has been proposed by several authors; see [28] for an overview. Tasche [26] argues that allocation based on the Euler principle provides the right signals for performance measurement. Another justification for the Euler principle is given by Denault [8] using the framework of cooperative game theory. He shows that the Euler principle is the only fair allocation principle for a differentiable coherent risk measure. The existence of the directional derivative (9) is analyzed in several articles, for example, in [4, 11, 13, 27]. Alternative allocation techniques have been explored in the actuarial sciences; see, for example, [9, 21]. A comparison of different combinations of risk measures and allocation methods can be found in [29].

## **Capital Allocation for Specific Risk Measures**

In classical portfolio theory, risk is measured by standard deviations [19]. More precisely, let  $c$  be a nonnegative real number and define the risk measure  $\rho_c^{\text{Std}}$  and the capital allocation  $\Lambda_c^{\text{Std}}$  by

$$\rho_c^{\text{Std}}(X) := c \cdot \text{Std}(X) + \text{E}(X) \tag{10}\n$$

$$\n\Lambda_c^{\text{Std}}(X, Y)\n$$

$$\n\begin{aligned}\n\colon=& \begin{cases}\nc \cdot \text{Cov}(X, Y) / \text{Std}(Y) + E(X) & \text{if } \text{Std}(Y) > 0, \\
E(X) & \text{if } \text{Std}(Y) = 0\n\end{cases} \tag{11}\n\end{aligned}$$

The risk measure  $\rho_c^{\text{Std}}$  is positively homogeneous and subadditive but not coherent for  $c > 0$ . The covariance allocation  $\Lambda_c^{\rm Std}$  is linear and diversifying.<br>It is derived from the risk measure  $\rho_c^{\rm Std}$  using the construction principle (8). If  $\text{Std}(Y) > 0$  then  $\Lambda_c^{\text{Std}}$  is continuous at  $Y$  and equals the directional derivative (9) by Theorem 2.

The current standard in the finance industry is to define the risk capital in terms of a quantile of the loss distribution (see Value-at-Risk): the Value-at-Risk  $\text{VaR}_{\alpha}(X)$  of the portfolio X at a specified confidence level  $\alpha \in (0, 1)$  is defined by

$$\text{VaR}_{\alpha}(X) := \inf\{l \in \mathbb{R} \mid \mathbb{P}(X \le l) \ge \alpha\} \tag{12}$$

VaR has an intuitive economic interpretation, that is, it specifies the capital needed to absorb losses with probability  $\alpha$ , and has even achieved the high status of being written in industry regulations. However, VaR also has an obvious limitation as a risk measure: in general, it is not subadditive if applied to portfolios with nonelliptic distributions. Theorem 1 implies that in the general case there do not exist linear, diversifying capital allocations for VaR. However, under regularity conditions (see, for example, [26]), the directional derivative (9) exists for  $\text{VaR}_{\alpha}$ and equals

$$E(X|Y = VaR_{\alpha}(Y)) \tag{13}$$

The most prominent coherent risk measure is expected shortfall (see, for instance, [2, 24], **Expected Shortfall**) given by

$$\mathrm{ES}_{\alpha}(X) = \frac{1}{1-\alpha} \int_{\alpha}^{1} \mathrm{VaR}_{u}(X) \, \mathrm{d}u \qquad (14)$$

Instead of fixing a quantile at a particular confidence level  $\alpha$ , expected shortfall averages VaR across the entire tail specified by  $\alpha$ . Coherence implies that expected shortfall is positively homogeneous and subadditive. Hence, application of equation (8) yields

$$\Lambda_{\alpha}^{\mathrm{ES}}(X,Y) := \left(\int X \cdot \mathbf{1}_{\{Y > \mathrm{VaR}_{\alpha}(Y)\}} \, \mathrm{d}\mathbb{P} \right.$$
  
$$+ \beta_{Y} \int X \cdot \mathbf{1}_{\{Y = \mathrm{VaR}_{\alpha}(Y)\}} \, \mathrm{d}\mathbb{P} \right) / (1-\alpha), \quad \text{with}$$
  
$$\beta_{Y} := \frac{\mathbb{P}(Y \le \mathrm{VaR}_{\alpha}(Y)) - \alpha}{\mathbb{P}(Y = \mathrm{VaR}_{\alpha}(Y))}$$
  
if  $\mathbb{P}(Y = \mathrm{VaR}_{\alpha}(Y)) > 0$  (15)

which is a linear, diversifying capital allocation with respect to  $ES_{\alpha}$ . If

$$\mathbb{P}(Y > \text{VaR}_{\alpha}(Y)) = 1 - \alpha$$
  
or 
$$\mathbb{P}(Y \ge \text{VaR}_{\alpha}(Y)) = 1 - \alpha \qquad (16)$$

then  $\Lambda_{\alpha}^{\text{ES}}$  is continuous at Y and equals the directional derivative (9). In particular, equation (16) holds if  $\mathbb{P}(Y = \text{VaR}_{\alpha}(Y)) = 0$ ; in that case,  $\Lambda_{\alpha}^{\text{ES}}(X, Y)$  takes the particularly intuitive form

$$\Lambda_{\alpha}^{\text{ES}}(X,Y) = E(X \mid Y > \text{VaR}_{\alpha}(Y)) \tag{17}$$

The impact of capital allocation techniques on portfolio management has been analyzed in a case study in [17], which compares expected shortfall allocation and covariance allocation in large credit portfolios.

## References

- Acerbi, C. (2004). Coherent representation of subjective [1] risk-aversion, in Risk Measures for the 21st Century, G. Szego, ed, Wiley, Chichester.
- Acerbi, C. & Tasche, D. (2002). On the coherence of [2] expected shortfall, Journal of Banking and Finance 26,  $1487 - 1503$ .
- Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D. (1999). [3] Coherent measures of risk, *Mathematical Finance* 9(3), 203-228.
- Carlier, G. (2008). Differentiability properties of rank-[4] linear utilities, Journal of Mathematical Economics 44(1), 15–23.
- Cherny, A.S. (2007). Pricing with coherent risk, Proba-[5] bility Theory and Its Applications  $52(3)$ ,  $506-540$ .

- Cherny, A.S. & Orloy, D.V. (2007). On Two Approaches [6] to Coherent Risk Contribution, Preprint, Moscow State University.
- Delbaen, F. (2000). Coherent Risk Measures. Lecture [7] notes, Scuola Normale Superiore di Pisa.
- [8] Denault, M. (2001). Coherent allocation of risk capital, Journal of Risk  $4(1)$ , 1-34.
- Dhaene, J., Goovaerts, M. & Kaas, R. (2003). Economic [9] capital allocation derived from risk measures. American Actuarial Journal 7(2), 44-59.
- [10] Dunford, N. & Schwartz, J. (1958). Linear Operators-Part I: General Theory, Interscience Publishers, New York.
- [11] Fischer, T. (2003). Risk capital allocation by coherent risk measures based on one-sided moments, Insurance: Mathematics and Economics  $32(1)$ ,  $135-146$ .
- $[12]$ Föllmer, H. & Schied, A. (2004). Stochastic Finance-An Introduction in Discrete Time, 2nd Edition, Walter de Gruvter. Berlin.
- [13] Gourieroux, C., Laurent, J.-P. & Scaillet, O. (2000). Sensitivity analysis of values at risk, Journal of Empirical Finance 7, 225-245.
- [14] Hallerbach, W. (2003). Decomposing portfolio valueat-risk: a general analysis, *Journal of Risk*  $5(2)$ ,  $1-18$ .
- [15] Kalkbrener, M. (2005). An axiomatic approach to capital allocation, Mathematical Finance 15(3), 425-437.
- Kalkbrener, M. (2007). An Axiomatic Characteriza-[16] tion of Capital Allocations of Coherent Risk Measures, Preprint, Deutsche Bank, Frankfurt.
- Kalkbrener, M., Lotter, H. & Overbeck, L. (2004). Sen-[17] sible and efficient capital allocation for credit portfolios, Risk 17(1), S19-S24.
- [18] Lintner, J. (1965). Security prices, risk and maximal gains from diversification, Journal of Finance 20(4), 587-615.
- [19] Markowitz, H. (1952). Portfolio selection, Journal of Finance 7, 77-91.
- [20] Matten, C. (2000). Managing Bank Capital: Capital Allocation and Performance Measurement, 2nd Edition, Wiley, New York.
- [21] Myers, S.C. & Read, J.A. (2001). Capital allocation for insurance companies, Journal of Risk and Insurance 68(4), 545-580.
- [22] Overbeck, L. (2000). Allocation of economic capital in loan portfolios, in Proceedings Measuring Risk in Complex Stochastic Systems, Lecture Notes in Statistics, Vol. 147, W. Hardle & G. Stahl, eds, Springer, Berlin, 1999.
- Overbeck, L. (2004). Spectral capital allocation, in [23] Economic Capital, A Practitioner Guide, A. Dev, ed, Risk Books, London.
- Rockafellar, R.T. & Uryasev, S. (2002). Conditional [24] value-at-risk for general loss distributions, Journal of Banking and Finance 26, 1443-1471.
- Sharpe, W. (1964). Capital asset prices: a theory of [25] market equilibrium under conditions of risk, Journal of Finance  $19(3)$ , 425–442.

- [26] Tasche, D. (1999). *Risk Contributions and Performance Measurement*, Preprint, Munich University of Technology.
- [27] Tasche, D. (2002). Expected shortfall and beyond, *Journal of Banking and Finance* **26**(7), 1519–1533.
- [28] Tasche, D. (2007). *Euler Allocation: Theory and Practice*, Preprint, Fitch Ratings, London.
- [29] Urban, M., Dittrich, J., Kluppelberg, C. & St ¨ olting, R. ¨ (2004). Allocation of risk capital to insurance portfolios, *Bl¨atter der DGVFM* **26**, 389–406.

**Related Articles**

**Convex Risk Measures**; **Economic Capital**; **Riskadjusted Return on Capital (RAROC)**; **Value-at-Risk**.

MICHAEL KALKBRENER
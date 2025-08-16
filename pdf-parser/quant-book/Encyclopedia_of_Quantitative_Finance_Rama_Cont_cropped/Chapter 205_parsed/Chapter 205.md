# **Local Correlation Model**

The local correlation model is a credit portfolio loss model that generalizes the Gaussian copula model (see Gaussian Copula Model) and allows to account for the base correlation smile (see **Base** Correlation).

The local correlation model is essentially similar to an exotic copula model; its originality lies mainly in its economic interpretation. The model consists of a slight modification in the analytical specification of the Gaussian copula (see Gaussian Copula Model):

$$A_i = \sqrt{\rho(X)}X + \sqrt{1 - \rho(X)}\varepsilon_i \tag{1}$$

Each reference entity in the portfolio is represented by its asset value  $A_i$ , driven by a specific factor  $\varepsilon_i$ , and an economic factor X, common to all names in the economy. In the Gaussian framework, the correlation parameter  $\rho$  is constant and therefore  $A_i$  is Gaussian. On the contrary, in the local correlation model,  $\rho(X)$  is a function of the economy factor, making assets non-Gaussian. As a result,  $\rho(X)$  is not a measure of the actual asset correlation in the traditional sense. In the local correlation model, default correlation does not depend on the average spread of the portfolio, its dispersion, rating, or industrial sectors, but rather on the global state of the economy. In other words, the local correlation function is universal and can be used regardless of the composition of the reference portfolio. We can, therefore, calibrate our local correlation function to standard Collateralized Debt Obligation (CDO) tranches and use it to price bespoke CDOs. The model's applications are discussed later.

## Large Pool Framework

Conditional on a state of the economy, the local correlation model behaves just like any other Gaussian copula model. The conditional cumulative loss is given as

$$L(K|X) = P\left[ (1 - RR) \times \frac{1}{n} \sum_{i=1}^{n} 1_{\{A_i \le G_i^{-1}(p_i)\}} \le K|X \right]$$
(2)

In equation (2),  $RR$  is a fixed recovery rate assumption,  $n$  is the number of obligors in the portfolio,  $A_i$  is the *i*th asset value as defined in the previous section,  $p_i$  is the probability of default for the *i*th obligor, and  $G_i$  is  $A_i$ 's cumulative distribution function.  $P$  is the risk-neutral probability. In an infinitely diversified portfolio, asset distributions and default probabilities do not depend on the obligor, and equa- $\text{tion (2) becomes}$ 

$$L(K|X) = P\left[1_{\{A \le G^{-1}(p)\}} \le \frac{K}{1 - RR} | X = x\right]$$
  
=  $1_{\left\{N\left(\frac{G^{-1}(p) + x\sqrt{\rho(x)}}{\sqrt{1 - \rho(x)}}\right) \le \frac{K}{1 - RR}\right\}}$  (3)

Finally, equation  $(3)$  yields the expression for unconditional cumulative loss:

$$L(K) = P\left[N\left(\frac{G^{-1}(p) + X\sqrt{\rho(X)}}{\sqrt{1 - \rho(X)}}\right) \le \frac{K}{1 - RR}\right] \tag{4}$$

Assuming that cumulative loss distribution  $L$ and asset distribution  $G$  are known, we can use equation  $(4)$  to obtain the local correlation function.

#### Implied Loss Distribution

Let us first derive an expression for cumulative loss distribution. The only information we have about a portfolio's cumulative loss comes from CDO market quotes. For example, five single-tranche CDOs are quoted based on the iTraxx Main portfolio—the European credit benchmark—and the CDX IG portfolio—the US credit benchmark. These prices form the "base correlation skew"-five constant correlations obtained using the Gaussian copula framework (see Gaussian Copula Model; Base Correlation). We write the naïve cumulative loss obtained using constant base correlations as  $L(K, \rho_K^{\text{Base}})$ . The naïve cumulative loss coincides with the actual cumulative loss  $L(K)$  on the five market points.  $L(K)$  can then be continuously interpolated using the following formula:

$$L(K) = L(K, \rho_K^{\text{Base}}) + \frac{\partial L}{\partial K}(K, \rho_K^{\text{Base}})$$
$$\times \int_0^K \frac{\partial L}{\partial \rho}(k, \rho_K^{\text{Base}}) \, \mathrm{d}k \tag{5}$$

 $\mathbf{1}$ 

# Results and Interpretation

One last assumption is made before we derive the final result: we need to assume that the asset distribution G is a Gaussian distribution, that is,  $G \equiv N$ . We drop this assumption later on. Equations (4) and (5) can finally be combined to obtain an analytical expression for local correlation  $\rho(X)$ .

Let us now discuss the economic interpretation of equation (4). We define the idiosyncratic threshold as

$$\tilde{\varepsilon}(X) = \frac{G^{-1}(p) + X\sqrt{\rho(X)}}{\sqrt{1 - \rho(X)}}\tag{6}$$

Equation  $(4)$  can be rewritten according to the following equation:

$$L(K) = N(x_K), \quad x_K = \tilde{\varepsilon}^{-1} \left( N^{-1} \left( \frac{K}{1 - RR} \right) \right)$$
(7)

This means that for each level of loss  $K$  in the portfolio, there is an equivalent<sup>a</sup> state of the economy  $x_K$ . Thus, for every state of the economy, there is a single corresponding loss level for any diversified portfolio. We can, therefore, interpret the local correlation  $\rho(X)$  in a given state of the economy as the equivalent constant correlation to be used for a tiny tranche of size  $dK$ , centered at strike  $K = L^{-1} \cdot N(X).$ 

The results so far are summarized as follows. The large pool assumption allows us to relate the local correlation function to the cumulative loss distribution. Furthermore, assuming that assets are normally distributed, we can generate a mapping of each state of the economy into a loss level for any given portfolio. The local correlation can, therefore, be interpreted as the correlation of a tiny tranche centered at the corresponding loss level in a given state of the economy.

### Relaxing the Gaussian Assumption

We made two crucial assumptions in the previous sections: we assumed that the portfolio could be considered infinitely diversified—the large pool assumption-and we also assumed that despite the local correlation specification (1), assets could be considered to be Gaussian

If we drop the Gaussian assumption, the law of assets becomes

$$G_i^{\rho}(z) = P[A_i \le z]$$
  
= 
$$\int N\left(\frac{z + x\sqrt{\rho(x)}}{\sqrt{1 - \rho(x)}}\right)\varphi(x) dx \qquad (8)$$

Equations  $(2)$  and  $(8)$  can be used simultaneously to solve both the local correlation function  $\rho(x)$ and asset distribution  $G$  at the same time, through a fixed-point algorithm. We initialize the algorithm by setting  $G \equiv N$  and solve equation (2) to get the corresponding  $\rho(x)$  function. The result is substituted into equation (8), which yields a new version of  $G$ . We iterate this process until the local correlation function is stable.

#### Relaxing the Large Pool Assumption

We now relax the large pool assumption. Considering equation (2), individual default probabilities are now used in their general form:

$$g_{i|X} = N\left(\frac{G^{-1}(p_i) + X\sqrt{\rho(X)}}{\sqrt{1 - \rho(X)}}\right) \tag{9}$$

Assuming that the function  $\rho(X)$  is known, we can compute the loss distribution  $L(K)$  via equation (2), using Andersen's combinatory algorithm as presented in [2]. We, therefore, need to provide the model with a functional form for local correlation such as a parametric representation. In  $[1]$  (see **Ran**dom Factor Loading Model (for Portfolio Credit)), Andersen et al. use a piecewise constant correlation function in their random factor loading model. Continuous functions such as piecewise linear functions or cubic splines can also be used. Such a parameterization suggests that the model needs to be calibrated to market prices through high-dimension optimization. Such an optimization is beyond the scope of this article.

#### Application to Exotic CDO Valuation

The problem of mapping the correlation of bespoke portfolios against standard ones has been a hot topic ever since standard CDO tranches started to trade. The question is, "How do we obtain the Gaussian correlation assumption to use with a nonstandard portfolio and nonstandard subordination from standard CDO quotes?" Amongst other authors, Turc and Very [4] have described several ways of choosing the right equivalent correlation for nonstandard CDO pricing [3]. The probability-matching approach turns out to be the most consistent technique. It suggests using the index correlation corresponding to an equivalent strike in probabilistic terms. In other words, the index strike and bespoke strike are equivalent if they have the same probability of being reached. In the local correlation model, remember that the function *ρ(X)* is considered as a universal constant, independent of the portfolio. Thus, equation (7) yields

$$L_{\text{index}}(K_{\text{index}}) = N(X) = L_{\text{bespoke}}(K_{\text{bespoke}}) \quad (10)$$

Equation (10) shows that the local correlation model is equivalent to the probability-matching approach. It is, therefore, consistent with one of the most popular market practices for bespoke CDO pricing.

# **Acknowledgments**

We would like to acknowledge the contribution of Philippe Very, of Natixis, for the development of the local correlation model.

# **End Notes**

a*.* Equivalence in terms of probability.

# **References**

- [1] Andersen, L. & Sidenius, J. (2004). *Extensions to the Gaussian Copula: Random Recovery and Random Factor Loadings*.
- [2] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *Risk* November, 67–72.
- [3] Jeffery, C. (2006). Credit model meltdown, *Risk Magazine* **19**(11), 21–25.
- [4] Turc, J. & Very, P. (2008). Pricing CDOs with a smile: the local correlation model, in *Frontiers in Quantitative Finance: Volatility and Credit Risk Modeling*, R. Cont, ed., Wiley, Chapter 9.

# **Further Reading**

Burtschell, X., Gregory, J. & Laurent, J.-P. (2005, 2008). *A Comparative Analysis of CDO Pricing Models*.

# **Related Articles**

**Base Correlation**; **CDO Tranches: Impact on Economic Capital**; **Collateralized Debt Obligations (CDO)**; **Gaussian Copula Model**; **Modeling Correlation of Structured Instruments in a Portfolio Setting**; **Random Factor Loading Model (for Portfolio Credit)**.

JULIEN TURC & BENJAMIN HERZOG
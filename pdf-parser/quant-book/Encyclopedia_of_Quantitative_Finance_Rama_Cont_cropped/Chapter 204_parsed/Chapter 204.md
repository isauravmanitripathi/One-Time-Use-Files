# **Random Factor Loading Model (for Portfolio** $\text{Credit}$

Consider a portfolio of  $N$  risky assets, all assumed (for simplicity) to generate a \$1 loss at the time of default. Let  $\tau_i$  denote the random default time for asset *i*, such that the total portfolio loss  $L(T)$  on the horizon  $[0, T]$  is

$$L(T) = \sum_{i=1}^{N} 1_{\tau_i \le T}$$
 (1)

From credit default swap (CDS) or bond markets, we can normally extract risk-neutral survival probabilities

$$Q_i(T) = \Pr(\tau_i > T), \quad i = 1, ..., N$$
 (2)

for all  $T$ ; this information locks risk-neutral expected portfolio losses at

$$E(L(T)) = \sum_{i=1}^{N} E(1_{\tau_i \le T}) = \sum_{i=1}^{N} (1 - Q_i(T)) \quad (3)$$

To be able to construct the entire distribution of  $L(T)$ —and not just its first moment—we need additional information about the default codependencies among the  $N$  assets.

The default codependence model that we consider here is in the class of *factor models*, in the sense that codependence is induced solely by a scalar<sup>a</sup> random variable  $Z$ —the so-called *systematic factor*—that affects all assets through a factor "loading" function. Conditional on Z, all N default times  $\tau_i$  are assumed to be independent of each other.

In practice, specification of factor loading is done using conditional survival time distributions  $q_i: \mathbb{R}_+ \times \mathbb{R} \to [0, 1],$  defined by

$$q_i(t, z) \equiv \Pr(\tau_i > t | Z = z)$$
  

$$i = 1, \dots, N, \quad t \ge 0$$
(4)

Complete prescription of a factor model requires specification of (i) all  $N$  functions  $q_i$  and (ii) the probability distribution of the systematic factor  $Z$ . As should be obvious, the  $q_i$ 's cannot be prescribed

arbitrarily, as they are subject to strong consistency and regularity conditions. For instance, we know from basic probability

$$\Pr\left(\tau_{i} > T\right) = \int q_{i}(T, z) \Pr\left(Z \in \mathrm{d}z\right) = Q_{i}(T) \quad (5)$$

which, for any given distribution of  $Z$ , provides an important constraint on  $q_i$ . Other regularity conditions—including those associated with the fact that  $L$ must be never decreasing in  $T$ —are reviewed in [1].

We emphasize the importance of the assumption of conditional independence, which allows for the application of efficient numerical methods to construct the (discrete) distribution of  $L(T)$  in equation (1). Andersen *et al.* [4] give one such algorithm and discuss in detail its application in price and sensitivity computations for collateralized debt obligations (CDOs).

## **Random Factor Loading Models**

A standard recipe for specifying the functions  $q_i$ 's in a financially meaningful way is to assume that Pr  $(\tau_i > T) = \Pr(X_i > H_i(T))$  for a deterministic default barrier  $H_i(T)$  and a *default driver*  $X_i$  of the form

$$X_i = \beta_i Z + e_i, \quad i = 1, \dots, N$$
 (6)

where  $\beta_i$  is a firm-specific constant, Z is a one-dimensional systematic factor, and  $e_i$  is a residual variable idiosyncratic to firm *i* and independent of Z and  $e_i$ ,  $j \neq i$ . As Z is often loosely considered a proxy for the state of the "market", equation (6) has some qualitative similarity with the CAPM setup, with  $X_i$ loosely representing the asset returns on firm  $i$ . The Gaussian copula model falls in the class of equation (6) as do many Levy-type copula models.

The RFL (random factor loading) class starts from equation (6), but alters the dependence of  $X_i$ on  $Z$  from strictly linear to a generic functional relationship. Specifically, one writes

$$X_i = A_i(Z) + e_i, \quad i = 1, \dots, N$$
 (7)

where  $A_i$  is a possibly firm-specific deterministic function. For reasons of tractability, it is most common to assume that Z and  $e_i$  are Gaussian, and to (arbitrarily) normalize such that  $E(X_i) = 0$ . In this case, one has

$$X_i = A_i(Z) + \epsilon_i + m_i, \quad i = 1, ..., N$$
 (8)

where Z and all residuals  $\epsilon_i$  are independent standard Gaussian variables (i.e., distributed as  $\mathcal{N}(0, 1)$ ), and the constant  $m_i$  is set to  $m_i = -E(A_i(Z))$ . Going forward, equation (8) shall be our working definition of a one-factor RFL model.

By moving away from strictly linear "loading" on the systematic variable, RFL models can incorporate a number of empirical observations about default codependence dynamics. Most importantly, we have the ability to increase the loading for low values of  $Z (= a "bad" market outcome)$  as a way of modeling the well-established fact that equity price correlations tend to increase in a market downturn. This, in turn, tends to fatten the upper tail of the distribution of  $L(T)$ , an effect that is consistent with the market for synthetic CDOs.

### **Some Analytical Results**

For simplicity, let us now drop<sup>b</sup> the subscript  $i$  on  $A_i$  and  $m_i$ . For completely arbitrary specifications of  $A(z)$ , there is obviously no hope that the distribution of  $X_i$  in equation (8) has a closed-form representation. If  $A(z)$  is taken to be piecewise linear, however, such a result exists, as shown in [3]. To list it, let us define thresholds  $\theta_0 < \theta_1 < \dots \theta_{K-1}$  and then write

$$A(z) = (\alpha_0 z + \beta_0) \mathbb{1}_{z \le \theta_0} + \sum_{k=1}^{K-1} (\alpha_k z + \beta_k) \mathbb{1}_{z \in (\theta_{k-1}, \theta_k]} + (\alpha_K z + \beta_K) \mathbb{1}_{z > \theta_{K-1}}$$
(9)

where the slopes  $\{\alpha_k\}_{k=0}^K$  and intercepts  $\{\beta_k\}_{k=0}^K$  are given constants. Let  $\Phi(x)$  be the Gaussian conditional default functions (CDFs), and let  $\Phi_2(x, y; \rho)$ be the bivariate Gaussian CDF at the correlation level  $\rho$ . Define, for  $k = 1, \ldots, K - 1$ ,

$$\psi(k,x) = \Phi_2\left(\frac{x - \beta_k - m}{\sqrt{1 + \alpha_k^2}}, \theta_k; \frac{\alpha_k}{\sqrt{1 + \alpha_k^2}}\right)$$
$$- \Phi_2\left(\frac{x - \beta_k - m}{\sqrt{1 + \alpha_k^2}}, \theta_{k-1}; \frac{\alpha_k}{\sqrt{1 + \alpha_k^2}}\right)$$
(10)

and

$$\psi(0,x) = \Phi_2\left(\frac{x - m - \beta_0}{\sqrt{1 + \alpha_0^2}}, \theta_0; \frac{\alpha_0}{\sqrt{1 + \alpha_0^2}}\right) \quad (11)\n$$

$$\n\psi(K,x) = \Phi_2\left(\frac{x - m - \beta_K}{\sqrt{1 + \alpha_K^2}}, -\theta_{K-1}; \frac{-\alpha_K}{\sqrt{1 + \alpha_K^2}}\right) \quad (12)$$

Then

$$\Pr\left(X_i \le x\right) = \sum_{k=0}^{K} \psi(k, x) \tag{13}$$

We can use equation  $(13)$  to ensure that the model is in calibration with market-observed default probabilities, by insisting that the default barrier function  $H_i(T)$  is set (by numerical root search) such that

$$\sum_{k=0}^{K} \psi(k, H_i(T)) = 1 - Q_i(T), \quad i = 1, \dots, N$$
(14)

We also notice that (with  $\varphi$  being the Gaussian density)

$$E(X_i) = m - \alpha_0 \varphi(\theta_0) \theta_0 + \beta_0 \Phi(\theta_0)$$
  
+ 
$$\sum_{k=1}^{K-1} \alpha_k \left( \varphi(\theta_{k-1}) - \varphi(\theta_k) \right)$$
  
+ 
$$\sum_{k=1}^{K-1} \beta_k \left( \Phi(\theta_k) - \Phi(\theta_{k-1}) \right)$$
  
+ 
$$\alpha_K \varphi(\theta_{K-1}) + \beta_K \Phi \left( -\theta_{K-1} \right)$$
  
(15)

which can be used to set *m* such that  $E(X_i) = 0$ .

## **CDO Calibration**

The free parameters of the RFL model are those involved in setting the function  $A(z)$ . Assuming that  $A$  is piecewise linear on  $K$  different intervals, we evidently have a total of  $3K + 2$  parameters in the model: *K* interval break-points *θ*0*, θ*1*,...,θK*−1; *K* + 1 slopes *α*0*,...,αK*; and *K* + 1 intercepts *β*0*,...,βK* . In general, this number of parameters is too high, so to avoid overfitting one normally locks some of these parameters manually and calibrates the rest against observed CDO prices. A few common parameter strategies are listed below.

#### **Classic RFL**

In this approach, which was developed in [3], we set all *K* + 1 intercepts (*βk )* to zero, leaving 2*K* + 1 free parameters for the calibration. In typical applications, sufficient calibration accuracy is often reached with *K* = 2 break-points, for a total of five free calibration parameters. We note that when intercepts are forced to zero, the function *A* is of the form

$$A(z) = a(z) \cdot z \tag{16}$$

where *a* is piecewise flat. Comparison with equation (6) shows that, loosely, the function <sup>√</sup>*a(z)* can be interpreted as a "random correlation" function. Consistent with earlier discussion, the calibrated *a(z)* will always be decreasing in *z*, that is, when the economy variable *Z* is low (= bad economy) correlations increase, and *vice versa*.

#### **Discrete RFL**

In this style, we set all *K* + 1 slopes to zero, yielding

$$A(z) = b(z) \tag{17}$$

where *b* is piecewise flat at levels *b*0*, b*1*,...,bK*. Evidently then, the distribution of *A(Z)* is here simply a discrete distribution<sup>c</sup> taking on *K* + 1 different values with *K* + 1 different probabilities. As the RFL model is normalized to work with the term *A(Z)* − *E (A(Z))*, we can add an arbitrary constant to the function *b(z)* without altering the model; equivalently, we are free to lock one of the *bk* values to a fixed constant (e.g., zero) without losing any generality. As a consequence, the effective number of parameters here is 2*K*.

#### **Fixed-slope RFL**

Our setup here is similar to that in discrete RFL, but now we allow for a nonzero constant slope *α* to be used for all line segments: *αk* = *α*, *k* = 0*,...,K*. We include this parameter in the set of free parameters to be optimized on, so now the problem dimension is 2*K* + 1.

# **Comments and Extensions**

Unlike a number of other factor models, the RFL model extends the basic Gaussian copula model by altering the CDF *qi*, rather than the density of the systematic factor *Z*. On the other hand, we can rewrite the RFL model as

$$X_i = Y + \epsilon_i, \quad Y = A(Z) + m \tag{18}$$

So, if we elect to treat the variable *Y* , rather than *Z*, as our systematic factor, the RFL model can, in fact, also be interpreted as extending the Gaussian copula model through a change of systematic factor density. Indeed, by a suitable choice of *A*, *all* factor models with Gaussian residuals can be cast as an RFL model of the type in equation (8). Andersen and Piterbarg [2] discuss this in more detail, using the models in [5, 6, 8] as examples.

In [1], the RFL model is extended to allow for Poisson- or mixture-style jumps in both residuals and in the systematic factor; the model in [7] is a special case of such a jump-extended RFL model. Andersen [1] also discusses methods to introduce a dynamic element into RFL and other factor models, by letting the density of *Z* depend on time.

# **End Notes**

a*.* Extensions to vector-valued *Z* is straightforward; see, for example, [3].

b*.* To keep free parameters at a manageable level, it is, in fact, common to use a single *A* for an entire portfolio. Firmspecific *A* functions may, however, be of use when mixing portfolios or as part of a bespoke mapping rule.

c*.* So rather than optimizing on the *θk* parameters, we can work directly with the discrete probabilities *(θk )* − *(θk*<sup>−</sup>1*)*.

# **References**

- [1] Andersen, L. (2006/2007). Portfolio losses in factor models: term structures and intertemporal loss dependence, *Journal of Credit Risk* **2**(4), 3–31.
- [2] Andersen, L. & Piterbarg, V.L. (2008). *The Definitive Guide to CDOs – Market, Application, Valuation, and Hedging*, Risk Books.
- [3] Andersen, L. & Sidenius, J. (2004/2005). Extensions of the Gaussian Copula: random recovery and random factor loadings, *Journal of Credit Risk* **1**(1), 29–70.
- [4] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *Risk* **16**, 67–72.

- [5] Guegan, D. & Houdain, J. (2005). *Collateralized Debt Obligations Pricing and Factor Models: A New Methodology Using Normal Inverse Gaussian Distributions*. Working Paper.
- [6] Inglis, S. & Lipton, A. (2007). *Factor Models for Credit Correlation*. Working Paper, Merrill Lynch.
- [7] Willeman, S. (2005). *Fitting the CDO Correlation Skew: A Tractable Structural Jump Model*. Working Paper, Aarhus Business School.
- [8] Xu, G. (2006). *Extending Gaussian Copula with Jumps to match Correlation Smile*. Working Paper, Wachovia Securities, defaultrisk.com.

# **Related Articles**

**Base Correlation**; **Collateralized Debt Obligations (CDO)**; **Copulas: Estimation**; **Credit Portfolio Simulation**; **Default Barrier Models**; **Gaussian Copula Model**; **Local Correlation Model**; **Multiname Reduced Form Models**.

LEIF B.G. ANDERSEN
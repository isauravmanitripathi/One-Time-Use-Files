# **Weighted Monte Carlo**

Weighted Monte Carlo (WMC) is the name given to an algorithm used to build and calibrate asset-pricing models for financial derivatives. The algorithm combines two fixtures of the toolbox of quantitative modeling. One is Monte Carlo simulation to generate "paths" for rates and market prices on which derivatives are written [7, 9]. The other is the maximum entropy (ME) criterion, used to calculate a posteriori statistical weights for the paths. ME is one of the main tools in science for calculating a posteri*ori* probabilities in the presence of known constraints associated with the probability measure (see [8] for classical econometric applications of ME).

The essence of the method is as follows [3]: let  $X_t(\omega)$ ,  $0 < t < T$ ,  $\omega \in \Omega$  represent a model for the evolution of market variables or factors of interest. One of the most common applications is the case when  $X_t$  is a multivariate diffusion or jump diffusion process, for example,

$$dX_{\alpha t} = \sum_{j} \sigma_{\alpha j} dW_{jt} + \mu_{\alpha} dt,$$
  
$$1 \le \alpha \le n, \quad 1 \le j \le m \tag{1}$$

This process represents an *a priori* model for the joint forward evolution of the market. The parameters of the model,  $\sigma$ ,  $\mu$  typically correspond to econometrically estimated factors and expected returns. We note that, since the model is used for pricing derivatives. some of the parameters can also be implied from the prices of at-the-money options and forward prices. In the language of financial economics, the measure induced by  $X_t$  is either the "physical measure" or a hybrid of the physical measure and a risk-neutral measure with respect to select observable forwards and implied volatilities.

A Monte Carlo simulation of the ensemble with  $N$ paths is generated numerically, where the paths are denoted by  $\omega_k$ , that is, they can be viewed as a sampling of the probability space  $\Omega$ . The WMC algorithm calibrates the Monte Carlo model so that it fits the current market prices of  $M$  benchmarks or reference European-style derivatives, with discounted payoffs  $g_1(\omega), g_2(\omega), \ldots, g_N(\omega)$  and prices  $c_1, c_2, \ldots, c_M$ . We denote the discounted payoffs along the simulated

paths by

$$G_{ik} = g_i(\omega_k), \ i = 1, \ldots, M, \ k = 1, \ldots, N \ (2)$$

WMC associates a probability  $p_k, k = 1, \dots N$  to each path, in such a way that the pricing equations

$$c_i = \sum_{k=1}^{N} G_{ik} p_k \tag{3}$$

or  $c = Gp$  in vector notation, hold for all indices i. Clearly, equation (3) states that the model reprices correctly the  $M$  reference instruments. In general, we assume that the number of simulation paths is much larger than the number of benchmarks (options, forwards), which is what happens in practical situations. The choice of the probabilities is done by applying the criterion of ME, that is, by maximizing

$$H(p_1, \ldots, p_N) = -\sum_{k=1}^{N} p_k \log p_k \qquad (4)$$

subject to the  $M$  constraints in equation (3). A least-squares version of the algorithm least squares weighted Monte Carlo (LSWMC) proposes to solve the problem

$$\min_{\mathbf{p}} \left\{ \sum_{i=1}^{M} \left( \sum_{k=1}^{N} G_{ik} p_{k} - c_{i} \right)^{2} - 2\epsilon H(\mathbf{p}) \right\} \qquad (5)$$

Here,  $\epsilon > 0$  is a tolerance parameter that must be adjusted by the user. If  $\epsilon \ll 1$ , LSWMC corresponds to the classical WMC. For finite, relatively small, values of  $\epsilon$  the algorithm returns, an approximate solution of equation (3). In practice, the implementation  $(5)$  is recommended, since a solution will exist for arbitrary data  $\{G_{ik}, c_i\}$ .

#### **Dual Formulation**

The WMC (LSWMC) algorithm is usually solved in its *dual form*. Define the partition function

$$Z(\lambda_1,\ldots,\lambda_M) = \sum_{k=1}^N e^{\sum_{i=1}^M \lambda_i G_{ik}} \qquad (6)$$

where  $\lambda_1, \ldots, \lambda_M$  are Lagrange multipliers. The dual problem is

$$\min_{\lambda} \left\{ \log Z(\lambda) - \sum_{i=1}^{M} c_i \lambda_i + \frac{\epsilon}{2} \sum_{i=1}^{M} \lambda_i^2 \right\} \quad (7)$$

The advantage of solving the dual problem is that the number of variables is  $M$ , hence much less than the number of simulated paths. It is well known that the latter problem is convex in  $\lambda$  and always admits a solution if  $\epsilon > 0$ . Furthermore, the probabilities are given explicitly in terms of the multipliers, which solve the dual problem, namely,

$$p_k = \frac{1}{Z} e^{\sum_{i=1}^{M} \lambda_i G_{ik}} \ k = 1, 2, \dots, N \tag{8}$$

In practical implementations, the dual problem can be solved with a gradient-based convex optimization routine such as L-BFGS.

## **Connection with Kullback-Leibler Relative Entropy**

We can view WMC as an algorithm that minimizes, in a discrete setting, the relative entropy, or Kullback-Leibler distance between the prior probability measure induced by the paths (3) (call it  $P_0$ ) and the posterior measure induced by the probability vector  $p$  (call it  $P$ ), in the sense that it provides a solution of

$$\min_{P} \left\{ 2\epsilon D(P||P_0) + \sum_{i=1}^{M} \left[ \mathbb{E}^P(g_i(\omega)) - c_i \right]^2 \right\} \tag{9}$$

with

$$D(P||P_0) = \mathbf{E}^P \left( \log \frac{\mathrm{d}P}{\mathrm{d}P_0} \right) \tag{10}$$

where  $\frac{dP}{dP_0}$  is the Radon-Nikodym derivative of  $P$  with respect to  $P_0$ . The latter interpretation, however, should be taken with a grain of salt since the implementation is always done in the discrete setting, ensuring that the relative entropy between two measures defined on the paths of the MC simulation is always well defined (unlike in the continuous limit, where absolute continuity in Wiener space is often a stringent condition).

#### **Connection with Utility Maximization**

It can be shown, *via* an analysis of the dual problem, that the WMC algorithm gives a pricing measure, which corresponds to optimal investment by a representative investor in the reference instruments when this investor has an exponential utility [6].

#### Main Known Applications

Some of the most well-known applications of this method have been in the context of multiasset equity derivatives. In this case, the *a priori* measure corresponds to a multidimensional diffusion for stock prices, generated using a factor model (or model for the correlation matrix). The *a posteriori* measure is generated by calibrating to traded options on several underlying assets. For instance, the underlying stocks can be the components of the Nasdaq 100 index and the reference instruments all listed options on the underlying stocks. In the latter case, some care must be taken with the fact that listed options are American-style, but this difficulty can be overcome by generating prices of European options using the implied volatilities of the traded options. This yields a calibrated multiasset pricer for derivatives defined on the components of the Nasdaq 100. As a general rule, it is recommended to calibrate to forward prices (zero-strike calls) in addition to options, to ensure put-call parity in the *a posteriori* measure. The value  $\epsilon = 0.25$  seems to give results that are within the bid-ask spread of listed options contracts [1, 2].

Another application of WMC is to the calibration of volatility surfaces for foreign-exchange (FX) options, to obtain a volatility surface that matches forward prices, at-the-money options, strangles, and risk-reversals on all available maturities. Owing to the nature of quotes in FX, the recommended value for the tolerance parameter should be of the order of  $10^{-4}$  in this case [1, 2].

Applications of WMC have been also proposed in the context of credit derivatives, most notably for calibrating so-called top-down models [5].

#### Dispersion Trading

Dispersion trading corresponds to buying and selling index options and hedging with options on the component stocks. WMC gives a method for obtaining a model price for index options based on a model,

which incorporates a view of the correlation between stocks (expressed in the *a priori* probability for  $X_t$ ) and is calibrated to all the options on the components of the index. Comparing the model price (or implied volatility) with the implied volatility of index options quoted in the market provides a rational setting for comparing the prices of index options with the prices of options on the components of the index. One of the important features of WMC is that it allows the user to incorporate views on the volatility skew/smile of the components in the valuation process  $[1, 2]$ .

#### Connection to Control Variates

The WMC framework can be generalized to any concave function  $H(\mathbf{p})$ . Avellaneda and Gamba [4] suggest, as one practical approach,

$$H(\mathbf{p}) = -\sum_{k=1}^{N} \Psi(p_k) \tag{11}$$

with  $\Psi(\cdot)$  being any convex function. Obvious choices are

$$\Psi^{(\mathbf{Q})}(p) = \left(p - \frac{1}{N}\right)^2 \quad \text{(Quadratic)} \tag{12}$$

$$\Psi^{(S)}(p) = p \log p \qquad \text{(Shannon)} \qquad (13)$$

The problem of minimization of  $-H(\mathbf{p})$  subject to the constraints (probability normalization and calibration)

$$1 = \boldsymbol{p}^\top \boldsymbol{n} \quad \text{and} \quad \boldsymbol{c} = G \boldsymbol{p} \tag{14}$$

with the diagonal vector  $\mathbf{n} := (1, \cdots, 1)^{\top} \in \mathbb{R}^{N}$  (to simplify summation notation), leads to the Lagrange function

$$\mathcal{L}(\boldsymbol{p}, \boldsymbol{\lambda}, \boldsymbol{\mu}) = -H(\boldsymbol{p}) - \boldsymbol{\lambda}^{\top} (G \boldsymbol{p} - \boldsymbol{c}) - \boldsymbol{\mu} \left( \boldsymbol{p}^{\top} \boldsymbol{n} - 1 \right)$$
(15)

Assuming the existence of an extremum, solving

$$\nabla_{\! \boldsymbol{p}} \mathcal{L}(\boldsymbol{p}, \boldsymbol{\lambda}, \boldsymbol{\mu}) = 0 \n\tag{16}$$

gives

$$p_k = \psi^{-1}(\boldsymbol{\lambda}^\top G \boldsymbol{e}_k + \mu) \tag{17}$$

with  $\psi(p) = \frac{\mathrm{d}\Psi(p)}{\mathrm{d}p}$  and  $e_k$  being the unit vector along the *k*-th axis in  $\mathbb{R}^N$ . For the specific choices (12) and  $(13)$ , this means

$$p_k^{(\mathbf{Q})} = \frac{1}{N} + \frac{1}{2} \boldsymbol{\lambda}^\top G \left( \boldsymbol{e}_k - \frac{1}{N} \boldsymbol{n} \right)$$
 (Quadratic) (18)

$$p_k^{(S)} = \frac{e^{\lambda^\top G e_k}}{Z(\lambda)} \quad \text{(Shannon)} \tag{19}$$

with  $Z(\lambda) = \sum_{k=1}^{N} e^{\lambda^{\top} G e_k}$ , where we have eliminated  $\mu$  using the probability normalization condition 1 =  $\boldsymbol{p}^\top \boldsymbol{n}$ . Substituting equation (18) and, respectively, equation  $(19)$ , back into equation  $(15)$  leads to the Lagrange dual functions

$$\hat{\mathcal{L}}^{(\mathbf{Q})}(\boldsymbol{\lambda}) = \boldsymbol{\lambda}^{\top} \left( \boldsymbol{c} - G \frac{\boldsymbol{n}}{N} \right) \n+ \frac{N}{2} \boldsymbol{\lambda}^{\top} G \left( \frac{\boldsymbol{n} \boldsymbol{n}^{\top}}{N^{2}} - \frac{1}{N} \right) G^{\top} \boldsymbol{\lambda} \qquad (20)$$

$$\hat{\mathcal{L}}^{(S)}(\lambda) = \lambda^{\top} c - \log Z(\lambda) \tag{21}$$

The dual formulation of the original problem is to find

$$\arg\max_{\lambda} \hat{\mathcal{L}}(\lambda) \tag{22}$$

For the quadratic case, this is guaranteed to have at least one solution given by the linear system

$$\frac{N}{2}G\left(\frac{1}{N} - \frac{\boldsymbol{n}\boldsymbol{n}^{\top}}{N^{2}}\right)G^{\top}\boldsymbol{\lambda}^{(\mathbf{Q})} = \boldsymbol{c} - G\frac{\boldsymbol{n}}{N} \qquad (23)$$

Note that

$$G\left(\frac{1}{N} - \frac{n\boldsymbol{n}^{\top}}{N^{2}}\right)G^{\top} = \langle \boldsymbol{g}\boldsymbol{g}^{\top}\rangle_{N}^{P_{0}} - \langle \boldsymbol{g}\rangle_{N}^{P_{0}}\langle \boldsymbol{g}\rangle_{N}^{P_{0}\top} (24)$$
$$= \langle \boldsymbol{g}, \boldsymbol{g}\rangle_{N}^{P_{0}} \tag{25}$$

where  $\langle \cdot \rangle_N^{P_0}$  stands for the Monte Carlo estimator of the expectation under the original measure  $P_0$  computed as the plain average over the  $N$  simulated paths, and  $\langle \cdot, \cdot \rangle_N^{P_0}$  for the according covariance (defined such that  $\langle \boldsymbol{a}, \boldsymbol{b} \rangle = \langle \boldsymbol{b}, \boldsymbol{a} \rangle^{\top}$ ). In other words,

$$\boldsymbol{\lambda}^{(\mathrm{Q})} = \frac{2}{N} \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P_0^{-1}} \cdot \left( \boldsymbol{c} - \langle \boldsymbol{g} \rangle_N^{P_0} \right) \tag{26}$$

and

$$\boldsymbol{p}^{(\mathrm{Q})} = \frac{\boldsymbol{n}}{N} + \left(\frac{\boldsymbol{n}}{N} - \frac{\boldsymbol{n}\boldsymbol{n}^{\top}}{N^{2}}\right)G^{\top}$$
$$\cdot \left\langle \boldsymbol{g}, \boldsymbol{g} \right\rangle_{N}^{P_{0}^{-1}} \cdot \left(\boldsymbol{c} - \left\langle \boldsymbol{g} \right\rangle_{N}^{P_{0}}\right) \tag{27}$$

Note that the inverse of the autocovariance matrix of the calibration instruments is to be understood in a Moore-Penrose sense to safeguard against the singular case.

When using these probabilities for the valuation of a payoff v, with  $v_k := v(\omega_k)$ , we arrive at

$$\begin{split} \langle v \rangle_N^{P^{(\mathbf{Q})}} &= \boldsymbol{v}^\top \boldsymbol{p}^{(\mathbf{Q})} \\ &= \langle v \rangle_N^{P_0} + \langle v, \boldsymbol{g} \rangle_N^{P_0} \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P_0^{-1}} \end{split} \tag{28}$$

$$\cdot \left( \boldsymbol{c} - \langle \boldsymbol{g} \rangle_N^{P_0} \right) \tag{29}$$

which is identical to the classic control variate rule [7, 9].

For  $\mathcal{L}^{(S)}(\lambda)$ , a second-order expansion in  $\lambda$  around zero gives

$$\hat{\mathcal{L}}^{(\mathrm{S})} = -\log N + \boldsymbol{\lambda}^{\top} \left( \boldsymbol{c} - \langle \boldsymbol{g} \rangle_N^{P_0} \right) \n- \frac{1}{2} \boldsymbol{\lambda}^{\top} \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P_0} \boldsymbol{\lambda} + \mathcal{O}(\boldsymbol{\lambda}^3)$$
(30)

and hence we obtain the analytical initial guess

$$\boldsymbol{\lambda}^{(\mathrm{S}),1} := \frac{N}{2} \boldsymbol{\lambda}^{(\mathrm{Q})} \tag{31}$$

for any iterative procedure to solve (22). A simple algorithm can be based on a second-order expansion of  $\hat{\mathcal{L}}^{(S)}(\lambda)$  around the previous iteration's estimate for  $\lambda^{(S)}$ . This gives

$$\boldsymbol{\lambda}^{(\mathrm{S}),i+1} = \boldsymbol{\lambda}^{(\mathrm{S}),i} + \left(G\boldsymbol{\Pi}^{(\mathrm{S}),i}G^{\top} - G\boldsymbol{p}^{(\mathrm{S}),i}\boldsymbol{p}^{(\mathrm{S}),i^{\top}}G^{\top}\right)^{-1} \times (\boldsymbol{c} - G\boldsymbol{p}^{(\mathrm{S}),i}) \tag{32}$$

with

$$\Pi^{(\mathcal{S}),i} := \text{diag}\left(p_1^{(\mathcal{S}),i}, \cdots, p_N^{(\mathcal{S}),i}\right) \in \mathbb{R}^{N \times N} \tag{33}$$

and

$$p_k^{(\mathbf{S}),i} = p_k^{(\mathbf{S})}(\boldsymbol{\lambda}^{(\mathbf{S}),i}) \tag{34}$$

as defined in equation (19). Interestingly, the term

 $G\mathbf{p}^{(\mathrm{S}),i}$ 

in equation  $(32)$  is the vector of expectations for the  $M$  calibration instruments under the (numerical) measure  $P^{(S),i}$  defined by the numerically computed vector of probabilities  $\boldsymbol{p}^{(S),i}$ , and

$$\left(G\Pi^{(\mathrm{S}),i}G^{\top} - G\boldsymbol{p}^{(\mathrm{S}),i}\boldsymbol{p}^{(\mathrm{S}),i}^{\top}G^{\top}\right) \qquad (35)$$

is the associated (numerical) covariance matrix of the calibration instruments. The simple algorithm is thus, in a formal notation, to start with  $\lambda^{(S),0} = 0$  (in all entries of the vector), to compute

$$\boldsymbol{p}^{(\mathrm{S}),i} = \boldsymbol{p}^{(\mathrm{S})} \left( \boldsymbol{\lambda}^{(\mathrm{S}),i} \right) \tag{36}$$

using equation  $(19)$ , to proceed to

$$\boldsymbol{\lambda}^{(\mathrm{S}),i+1} = \boldsymbol{\lambda}^{(\mathrm{S}),i} + \langle \boldsymbol{g}, \boldsymbol{g} \rangle_{N}^{P^{(\mathrm{S}),i}}$$
$$\cdot \left( \boldsymbol{c} - \langle \boldsymbol{g} \rangle_{N}^{P^{(\mathrm{S}),i}} \right) \tag{37}$$

and to  $\boldsymbol{p}^{(S),i+1}$ , and so on.

It is, in general, possible that a solution to equation (22) may not exist for  $\hat{\mathcal{L}}^{(S)}$  if the model's initial calibration implies prices for the calibration instruments that are too far away from  $c$ . When this happens, any iterative procedure will experience that  $\hat{\mathcal{L}}^{(S)}(\lambda)$  grows at an ever decreasing rate in some direction in  $\mathbb{R}^M$ , and, eventually, the solver will terminate when it hits an internal minimum-progress criterion. A numerical approximation for  $\lambda^{(S)}$  computed in this way will represent an ME best-possible fit, and is still usable in a vein similar to that obtained by the least squares approach mentioned in the beginning. An inexpensive warning indication for this situation is given when any of the  $p_k^{(Q)}$  are negative. Note that this then also signals that the classic control variate method implicitly uses a (numerical) measure that is not equivalent to the original model's measure, which in turn may result in arbitrageable prices.

#### Hedge Ratios

The fact that the fine tuning of the pricing measure  $P$ is achieved by varying the probabilities of the paths such that hedge instruments are correctly repriced allows for the calculation of hedge ratios without recalibration of the original model, and without resimulation. This can be seen as follows. We seek to compute the sensitivity of  $\langle v \rangle_N^P$  with respect to the calibration prices c. Since the probability vector  $p(\lambda)$ is computed as an analytical function of the Lagrange multipliers, which in turn are computed numerically from  $c$ , we have

$$\nabla_{\!c} \langle v \rangle_N^P = \nabla_{\!c} (\boldsymbol{p}^\top \boldsymbol{v}) = J \cdot \nabla_{\!a} \boldsymbol{p}^\top \boldsymbol{v} \tag{38}$$

with the elements of the Jacobian matrix  $J$  given by

$$J_{lm} = \partial_{c_l} \lambda_m \tag{39}$$

Given any  $\Psi$ , which, together with the calibration constraints, ultimately defines our desired pricing measure  $P$ , we can combine equation (17) and the probability normalization condition  $1 = \mathbf{p}^\top \mathbf{n}$  to arrive at

$$\nabla_{\!c} \langle v \rangle_N^P = s^{P_{\rm H}} \cdot J \cdot \langle \boldsymbol{g}, v \rangle_N^{P_{\rm H}} \tag{40}$$

where we have defined the hedge measure  $P_{\rm H}$  in terms of the (numerical) probabilities  $\boldsymbol{p}^{P_{\rm H}}$  whose elements are given by

$$s^{P_{\rm H}} := \sum_{k=1}^{N} 1/\psi'\left(p_{k}^{P}\right) \quad \text{with}$$
$$p_{k}^{P_{\rm H}} := \frac{1/\psi'\left(p_{k}^{P}\right)}{s^{P_{\rm H}}} \tag{41}$$

What remains to be calculated is the Jacobian  $J$ . This can be done in one of three ways, depending on the choice of  $\Psi$ :

1. Analytically (explicitly). For instance, for  $\Psi^{(Q)}$ , we obtain  $s^{P_{\rm H}^{(Q)}} = 1$ ,  $p_k^{P_{\rm H}^{(Q)}} = \frac{1}{N}$ ,  $P_{\rm H}^{(Q)} = P_0$ , and therefore

$$\nabla_{\!\!c} \langle v \rangle_N^{P^{(Q)}} = \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P_0^{-1}} \cdot \langle \boldsymbol{g}, v \rangle_N^{P_0} \tag{42}$$

- 2. Numerically. If  $\lambda^P$  is computed by an iterative procedure that starts with no information other than the simulated paths and  $c$  itself as indicated in equation (32), the chain rule propagation can be derived and implemented as part of the iterative procedure. This approach may have to be chosen if no solution to equation  $(22)$ exists. An alternative would be to precalibrate the original model better such that a Monte Carlo weighting scheme can be found that reprices the calibration instruments exactly.
- 3. Analytically (implicitly). As long as a solution to equation  $(22)$  exists, that is, as long as the WMC scheme reprices the calibration instruments correctly, we can use the fact that  $\nabla_{\!c} \langle g \rangle_N^P$  must be the  $M \times M$  identity matrix. This gives the generic result

$$\nabla_{\!\!c} \langle v \rangle_N^P = \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P_{\rm H} - 1} \cdot \langle \boldsymbol{g}, v \rangle_N^{P_{\rm H}} \qquad (43)$$

which means that for any  $P_0$  and  $P$ , that is,  $\Psi$ , that permit perfect repricing of the hedges (calibration instruments) under  $P$ , the hedge ratios for any payoff  $v$  can be seen as a regression of the covariances between  $v$  and the hedge instruments against the autocovariances of the hedge instruments under the calibration-adjusted measure  $P_{\rm H}$ .

It is worth mentioning that for  $\Psi^{(S)}(p) = p \log p$ , we obtain  $s^{P_{\rm H}^{(\rm S)}} = 1, \ p_k^{P_{\rm H}^{(\rm S)}} = p_k^{P_{\rm H}^{(\rm S)}}, \ P_{\rm H}^{(\rm S)} = P^{(\rm S)}, \text{ and}$ 

$$\nabla_{\!\!c} \langle v \rangle_N^{P^{(\mathrm{S})}} = \langle \boldsymbol{g}, \boldsymbol{g} \rangle_N^{P^{(\mathrm{S})}-1} \cdot \langle \boldsymbol{g}, v \rangle_N^{P^{(\mathrm{S})}} \tag{44}$$

In other words, the calibration-adjusted measure is the same as the pricing measure. This is a special property of the Shannon entropy pricing measure  $p(S)$ 

As a final note on hedge ratio calculations with WMC, it should be noted that unlike most of the other sensitivity calculation schemes used with Monte Carlo methods, the above shown analysis results directly in *hedge ratios*, bypassing the otherwise common intermediate stage of *model parameter sen*sitivities, which require remapping to hedge ratios for tradable instruments. This feature greatly reduces the noise often observed on risk figures that are computed by numerically fitting model parameters to market observable prices since the noise-compounding effects of recalibration and numerical calculation of sensitivities of hedge instrument prices to model parameters are avoided.

### References

- [1] Avellaneda, M. (2002). Empirical Aspects of Dispersion Trading in the US Equities Markets. Powerpoint presentation, Courant Institute of Mathematical Sciences, New York University, November 2002. www.math.nyu.edu/ faculty/avellane/ParisFirstTalkSlides.pdf
- [2] Avellaneda, M. (2002). Weighted-Monte Carlo Methods for Equity Derivatives: Theory and Practice, Powerpoint presentation, Courant Institute of Mathematical Sciences, New York University, November 2002. www.math.nyu. edu/faculty/avellane/ParisTalk2.pdf
- Avellaneda, M., Buff, R., Friedman, C., Grandchamp, N., [3] Kruk, L. & Newman, J. (2001). Weighted Monte Carlo: a new approach for calibrating asset-pricing models, International Journal of Theoretical and Applied Finance,  $4(1), 91-119.$
- [4] Avellaneda, M. & Gamba, R. (2000). Conquering the Greeks in Monte Carlo: efficient calculation of the market

sensitivities and Hedge-Ratios of financial assets by direct numerical simulation, *Mathematical Finance–Bachelier Congress 2000* , Monte Carlo, pp. 93–109, 2000/2002. www.math.nyu.edu/faculty/avellane/ConqueringThe Greeks.pdf

- [5] Cont, R. & Minca, A. (2008). *Recovering Portfolio Default Intensities Implied by CDO Quotes*, Financial engineering report no. 2008-01, Columbia University Center for Financial Engineering, ssrn.com/ abstract=1104855.
- [6] Delbaen, F., Grandits, P., Rheinlander, T., Samperi, D., Schweizer, M. & Stricker, C. (2002). Exponential hedging

and entropic penalties, *Mathematical Finance* **12**, 99–123, ssrn.com/abstract=312802.

- [7] Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*, Springer.
- [8] Golan, A., Judge, G. & Miller, D. (1996). *Maximum Entropy Econometrics*, John Wiley & Sons.
- [9] Jackel, P. (2002). ¨ *Monte Carlo Methods in Finance*, John Wiley & Sons.

MARCO AVELLANEDA & PETER JACKEL ¨
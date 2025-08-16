# **Model Calibration**

The fundamental theorem of asset pricing (see Fun**damental Theorem of Asset Pricing**) shows that, in an arbitrage-free market, market prices can be represented as (conditional) expectations with respect to a martingale measure  $\mathbb{O}$ : a probability measure  $\mathbb{O}$ on the set  $\Omega$  of possible trajectories  $(S_t)_{t \in [0,T]}$  of the underlying asset such that the asset price  $S_t/N_t$  discounted by the numeraire  $N_t$  is a martingale. The value  $V_t(H_T)$  of a (discounted) terminal payoff  $H_T$ at  $T$  is then given by

$$V_t(H_T) = E^{\mathbb{Q}}[B(t,T)H_T|\mathcal{F}_t] \tag{1}$$

where  $B(t, T) = N_t/N_T$  is the discount factor. For example, the value under the pricing rule  $\mathbb{Q}$  of a call option with strike  $K$  and maturity  $T$  is given by  $E^{\mathbb{Q}}[B(t,T)(S_T-K)^{+}|\mathcal{F}_t]$ . However, this result does not say how to construct the pricing measure  $\mathbb{Q}$ . Given that data sets of option prices have become increasingly available, a common approach for selecting a pricing model  $\mathbb{Q}$  is to choose, given a set of liquidly traded derivatives with (discounted) terminal payoffs  $(H^i)_{i \in I}$  and market prices  $(C_i)_{i \in I}$ , a pricing measure  $\mathbb{Q}$  compatible with the observed market prices:

**Problem 1** [Calibration Problem] Given market prices  $(C_i)_{i \in I}$  (say at date  $t = 0$ ) for a set of options with discounted terminal payoffs  $(H_i)_{i \in I}$ , construct a probability measure  $\mathbb{Q}$  on  $\Omega$  such that

the (discounted) asset price  $(S_t)_{t \in [0,T]}$  is a martingale under  $\mathbb{Q}$ 

$$T \ge t \ge u \ge 0 \Rightarrow E^{\mathbb{Q}}[S_t|\mathcal{F}_u] = S_u \quad (2)$$

the pricing rule implied by  $\mathbb{Q}$  is consistent with market prices

$$\forall i \in I, \quad E^{\mathbb{Q}}[H_i] = C_i \tag{3}$$

where, for ease of notation, we have set discount factors to 1 (prices are discounted) and  $E[.]$  denotes the conditional expectation given initial information  $\mathcal{F}_0$ . Thus, a pricing rule  $\mathbb{Q}$  is said to be calibrated to the benchmark instruments  $H_i$  if the value of these instruments, computed in the model, correspond to their market prices  $C_i$ .

Option prices being evaluated as expectations, this inverse problem can also be interpreted as a (generalized) moment problem for the law  $\mathbb{Q}$  of riskneutral process given a finite number of option prices, it is typically an *ill-posed* problem and can have many solutions. However, the number of observed options can be large ( $\simeq 100 - 200$  for index options) and finding even a single solution is not obvious and requires efficient numerical algorithms.

In the Black-Scholes model (see Black-Scholes Formula), calibration amounts to picking the volatility parameter to be equal to the implied volatility of a traded option. However, if more than one option is traded, the Black-Scholes model cannot be calibrated to market prices, since in most options markets implied volatility varies across strikes and maturities; this is the *volatility smile* phenomenon. Therefore, to solve the calibration problem, we need more flexible models, some examples of which are given here.

**Example 1** [Diffusion Model (*see* **Local Volatility Model**)] If an asset price is modeled as a diffusion process

$$dS_t = S_t[\mu \, dt + \sigma(t, S_t) \, dW_t] \tag{4}$$

parameterized by a local volatility function

$$\sigma : (t, S) \to \sigma(t, S) \tag{5}$$

then the values of call options can be computed by solving the Dupire equation (see Implied Volatility Surface)

$$\frac{\partial C_0}{\partial T} + Kr \frac{\partial C_0}{\partial K} - \frac{K^2 \sigma^2(T, K)}{2} \frac{\partial^2 C_0}{\partial K^2} = 0$$
  
$$\forall K \ge 0, \quad C_0(T = 0, K) = (S - K)^+ \tag{6}$$

The corresponding inverse problem is to find a (smooth) volatility function  $\sigma : [0, T] \times \mathbb{R}_+ \to \mathbb{R}_+$ such that  $C^{\sigma}(T_i, K_i) = C^*(T_i, K_i)$  where  $C^{\sigma}$  is the solution of equation (6) and  $C^*(T_i, K_i)$  are the market prices of call options.

**Example 2** In an exponential-Lévy model  $S_t =$  $\exp X_t$ , where  $X_t$  is a Lévy process (see **Exponential Lévy Models**) with diffusion coefficient  $\sigma > 0$  and Lévy measure v, call prices  $C^{\sigma,v}(t_0, S_0; T_i, K_i)$  are easily computed using Fourier-based methods (see

Fourier Methods in Options Pricing). The calibration problem is to find  $\sigma$ ,  $\nu$  such that

$$\forall i \in I, \ C^{\sigma,v}(t_0, S_0; T_i, K_i) = C^*(T_i, K_i) \tag{7}$$

This is an example of a nonlinear inverse problem where the parameter lies in a space of measures.

Example 3 In the LIBOR market model, a set of  $N$  interest rates (LIBOR rates) is modeled as a diffusion process  $L_t = (L_t^i)_{i=1..N}$  with constant covariance matrix  $\Sigma =^t \sigma.\sigma \in Sym^+(n \times n)$ :

$$\mathrm{d}L_t^i = \mu_t^i \,\mathrm{d}t + L_t^i \sigma_i \,\mathrm{d}W_t^j \tag{8}$$

This model can then be used to analytically price caps, floors, and swaptions (using a lognormal approximation), whose prices depend on the entries of the covariance matrix  $\Sigma$ . The calibration problem is to find a symmetric semidefinite positive matrix  $\Sigma \in Sym^+(n \times n)$  such that the model prices  $C^{\Sigma}$ match market prices

$$\forall i \in I, \ C^{\Sigma}(T_i, K_i) = C^*(T_i, K_i) \tag{9}$$

This problem can be recast as a semi-definite programming problem [2].

Other examples include the construction of yield curves from bond prices (see **Bond Options**) calibration of term structure models (see Term Structure **Models**) to bond prices, recovering the distribution of volatility from option prices [28] calibration to American options in diffusion models [1] and recovery of portfolio default rates from market quotes of credit derivatives [16, 18].

These problems are typically ill-posed in the sense that, either solutions may not exist (model class is too narrow to reproduce observations) or solutions are not unique (if data is finite or sparse). In practice, existence of a solution is restored by formulating the problem as an optimization problem

$$\inf_{\theta \in E} F(C^{\theta} - C) \tag{10}$$

where  $E$  is the parameter space and  $F$  is a loss function applied to the discrepancy  $C^{\theta} - C$  between market prices and model prices. An algorithm is then used to retrieve *one* solution and the main issue is the *stability* of this reconstructed solution as a function of inputs (market prices).

## **Inversion formulas**

In the theoretical situation where prices of European options are available for all strikes and maturities, the calibration problem can sometimes be explicitly solved using an inversion formula.

For the diffusion model in Example 1, the Dupire formula [25] (see **Dupire Equation**):

$$\sigma(T,K) = \sqrt{\frac{\frac{\partial C_0}{\partial T} + Kr\frac{\partial C_0}{\partial K}}{\frac{K^2}{2}\frac{\partial^2 C_0}{\partial K^2}}}$$
(11)

allows to invert the volatility function from call option prices. Similar formulas can be obtained in credit derivative pricing models, for inverting portfolio default rates from collateralized debt obligation (CDO) tranche spreads [16] and pure jump models with state-dependent jump intensity ("local Levy" model) [12]. No such inversion formula is available in the case of American options (see American **Options**). The Dupire formula (11) has been widely used by practitioners for recovering the local volatility function from call/put option prices by interpolating in strike and maturity and applying equation (11). However, since equation (11) involves differentiating the inputs, it suffers from instability and sensitivity to small changes in inputs, as shown in Figure 1. This instability deters one from using inversion formulas such as equation  $(6)$  even in the rare cases where they exist.

#### **Least-squares Formulation**

i

Typically, if the model is misspecified, the observed option prices may not lie within the range of prices attainable by the model. Also, option prices are defined up to a bid-ask spread: a model may generate prices compatible with the market but may not exactly fit the mid-market prices for any given  $\theta \in E$ . For these reasons, one often reformulates calibration as a least-squares problem

$$\inf_{\in E} J_0(\theta), \ J_0(\theta) = \sum_{i=1}^{I} w_i |C_i(\theta) - C_i|^2 \ (12)$$

where  $C_i$  are mid-market quotes and  $w_i > 0$  are a set of weights, often chosen inversely proportional to the (squared) bid-ask spread of  $C_i$ .

![](_page_2_Figure_1.jpeg)

**Figure 1** Extreme sensitivity of Dupire formula to noise in the data. Two examples of call price function (left) and their corresponding local volatilities (right). The prices differ through IID noise ∼ *UNIF(*0*,* 0*.*001*)*, representing a bid–ask spread

In most models, the call prices are computed numerically *via* Fourier transform (*see* **Fourier Methods in Options Pricing**) or by solving a partial differential equation (PDE) (*see* **Partial Differential Equations**). However, in many situations (short or long maturity, small vol–vol, etc.) approximation formulae for implied volatilities *(Ti, Ki)* of call options are available [5, 10, 11, 30] in terms of model parameters (*see* **Implied Volatility in Stochastic Volatility Models**; **Implied Volatility: Volvol Expansion**; **Implied Volatility: Long Maturity Behavior**; **SABR Model**). In these situations, parameters are calibrated by a least-squares fit to the approximate formula:

$$\inf_{\theta \in E} \sum_{i=1}^{I} w_i |\Sigma(T_i, K_i; \theta) - \Sigma^*(T_i, K_i)|^2 \qquad (13)$$

An example is the SABR model (*see* **SABR Model**), whose popularity is almost entirely due to its ease of calibration using the Hagan formula [30].

In most cases, option prices *Ci(θ )* depend continuously on *θ* and *E* is a subset of a finite dimensional space (i.e., there are a finite number of bounded parameters), so the least-squares formulation always admits a solution. However, the solution of equation (12) need not be unique: *J*<sup>0</sup> may, in fact, have several *global* minima, when the observed option prices do not uniquely identify the model. Figures 2 and 3 show examples of the function *J*<sup>0</sup> for some popular parametric option pricing models, computed using a data set of DAX index options prices on May 11, 2001. The pricing error in the Heston stochastic volatility model (*see* **Heston Model**), shown in figure as a function of the "volatility of volatility" and the mean reversion rate, displays a line of local minima. The pricing error for the variance gamma model (*see* **Variance-gamma Model**) in Figure 3 displays a nonconvex profile, with two distinct minima in the range

![](_page_3_Figure_1.jpeg)

Pricing error in heston model: SP500 options data, 2000.

 $\textbf{Figure 2} \quad \text{Error surface for the Heston stochastic volatility model, DAX options}$ 

![](_page_3_Figure_4.jpeg)

Figure 3 Error surface for variance gamma (pure jump) model, DAX options

of observed values. These examples show that, even if the number of observations (option prices) is much higher than the number of parameters, this does not imply identifiability of parameters.

Regularization methods can be used to overcome this problem [27]. A common method is to have a convex penalty term  $R$ , called the *regularization*  term, to the pricing error and solve the auxiliary problem:

$$\inf_{\theta \in E} J_{\alpha}(\theta) \tag{14}$$

where

$$J_{\alpha}(\theta) = J_0(\theta) + \alpha R(\theta) \tag{15}$$

The functional (16) consists of two parts: the regularization term *αR(θ )* which is convex in its argument and the quadratic pricing error which measures the precision of calibration. The coefficient *α*, called *regularization parameter*, defines the relative importance of the two terms: it characterizes the tradeoff between prior knowledge and the information contained in option prices. *Jα(.)* is usually minimized by gradient-based methods, where the crux of the algorithm is an efficient computation of the gradient ∇*θJ* .

When parameter is a function (such as the local volatility function), the regularization term is often chosen to be a smoothness (e.g., Sobolev) norm. This method, called *Tikhonov regularization* (*see* **Tikhonov Regularization**) has been applied to diffusion models [1, 2, 13, 23, 26] and to exponential-Levy ´ models [19].

Another popular choice of regularization term is the relative entropy (*see* **Entropy-based Estimation**) *R(θ )* = *H (<sup>θ</sup>* |*)* with respect to a prior probability measure . In continuous-time models, relative entropy can be used as regularization criterion only if the prior possesses a nonempty class of equivalent martingale measures, that is, it corresponds to an incomplete market model (*see* **Complete Markets**). From a calibration perspective, market incompleteness (i.e., the nonuniqueness of equivalent martingale measure) is therefore an *advantage*: it allows to conciliate compatibility with option prices and equivalence with respect to a reference probability measure. Examples are provided by jump processes (*see* **Jump Processes**; **Exponential Levy Models ´** ) or reducedform credit risk models (*see* **Reduced Form Credit Risk Models**): one can modify the jump size distribution (Levy measure) or the default intensity while ´ preserving equivalence (*see* **Equivalence of Probability Measures**) of measures [18, 20]. For Levy ´ processes (*see* **Exponential Levy Models ´** ), the relative entropy term *H (ν)* is computable in terms of the Levy measure ´ *ν* [21]. The calibration problem then takes the following form:

**Problem 2** *Given a prior L´evy process with law* <sup>0</sup> *and characteristics (σ*0*, ν*0*), find a L´evy measure ν which minimizes*

$$J_{\alpha}(\nu) = \alpha H(\nu) + \sum_{i=1}^{N} w_i (C_0^{\nu}(T_i, K_i) - C_0(T_i, K_i))^2$$
(16)

This regularized formulation has the advantage that its solution exhibits continuous dependence on market prices and with respect to the choice of the prior model [21, 22].

Simpler regularization methods can be used in settings where prices are computed using analytical transform methods. Belomestny & Reiss [8] propose a spectral regularization method for calibrating exponential-Levy models. Aspremont [3] formulates ´ the calibration of LIBOR market models (Example 3) as semidefinite programming problems under constraints.

Different regularization terms select *different* solutions: Tikhonov regularization approximates the leastsquares solution with smallest norm [27] while entropy-based regularization selects the minimumentropy least-squares solution [22].

## **Entropy Minimization Under Calibration Constraints**

An alternative approach to regularization is to select a pricing model by minimizing the relative entropy (*see* **Entropy-based Estimation**) of the probability measure with respect to a prior, under calibration constraints

$$\inf_{\mathbb{Q}\sim\mathbb{P}} H(\mathbb{Q}|\mathbb{P}) \quad \text{under} \quad C_i = E^{\mathbb{Q}}[H_i] \quad \text{for } i \in I$$
(17)

Relative entropy being strictly convex, any solution of equation (17) is unique and can be computed in a stable manner using Lagrange multiplier (dual) methods [24] (*see* **Convex Duality**).

Application of these ideas to a set of scenarios leads to the *weighted Monte Carlo algorithm* (*see* **Weighted Monte Carlo**) [6]: one first simulates *N* sample paths *N* = {*ω*1*, ..ωN* } from a *prior* model and then solves the above problem (AV) using as prior the uniform distribution on *N* . The idea is to weight the paths in order to verify the calibration constraints. The weights *(<sup>N</sup> (ωi), i* = 1*..N )* are constructed by minimizing relative entropy under calibration constraints

$$\inf_{\mathbb{Q}_{N}\in\mathcal{P}(\Omega_{N})}\sum_{i=1}^{N}\mathbb{Q}_{N}(\omega_{i})\ln\frac{\mathbb{Q}_{N}(\omega_{i})}{\mathbb{P}_{N}(\omega_{i})}\text{ under}$$

$$\sum_{i=1}^{N} \mathbb{Q}_{N}(\omega_{i}) G_{j}(\omega_{i}) = C_{j}$$
(18)

This constrained optimization problem is solved by duality  $[6, 24]$ : the dual has an explicit solution, in the form of a Gibbs-Boltzmann measure [4, 6] (see **Entropy-based Estimation**). A (discounted) payoff X is then priced using the same set of simulated paths via

$$E^{\mathbb{Q}_{N}}[X] = \sum_{i=1}^{N} \mathbb{Q}_{N}(\omega_{i})X(\omega_{i})$$
$$= \frac{1}{N} \sum_{i=1}^{N} \frac{\mathbb{Q}_{N}(\omega_{i})}{\mathbb{P}_{N}(\omega_{i})}X(\omega_{i}) \qquad (19)$$

The benchmark payoffs (calibration instruments) play the role of *biased* control variates, leading to variance reduction [29]:

$$E^{\mathbb{Q}_N}[X] = E^{\mathbb{Q}_N} \left[ X - \sum_{i=1}^I \alpha_i H_i \right] + \sum_{i=1}^I \alpha_i C_i \quad (20)$$

This method yields as a by-product, a static hedge portfolio  $\alpha_i^*$ , which minimizes the variance in equation (20) [3, 6, 17].

A drawback is that the martingale property is lost in this process since it would correspond to an infinite number of constraints. As a result, derivative prices computed with the weighted Monte Carlo algorithm may fail to verify arbitrage relations across maturities (e.g. calendar spread relations), especially when applied to forward-starting contracts.

These arbitrage constraints can be restored by representing  $\mathbb{Q}$  as a random mixture of martingales the law of random mixture being chosen via relative entropy minimization under calibration constraints [17]. This results in an arbitrage-free version of the weighted Monte Carlo approach, which is applied to recovering covariance matrices implied by index options in  $[15]$ .

## **Stochastic Control Methods**

In certain continuous-time models, the relative entropy minimization approach can be mapped, via a duality argument, into a stochastic control problem, which can then be solved using dynamic programming techniques. Consider a Markovian model where the state variable  $S_t$  (asset price, interest rate,..) follows a stochastic differential equation

$$dX_{t} = \mu_{\theta}(t) dt + \sigma_{\theta}(t, S_{t}) dW_{t}$$
$$+ \int \gamma_{\theta}(t, X_{t-}) \mu(dt dz) \qquad (21)$$

where W is a Wiener process and  $\mu$  a compensated Poisson random measure with intensity  $\nu_{\theta}(dz)\lambda_{\theta}(t) dt$ . The coefficients of the model are parameterized by some parameter  $\theta \in E$ ; in a nonparametric setting,  $\theta$  is just the coefficient itself and  $E$  is a functional space. Denote the law of the solution by  $\mathbb{Q}^{\theta}$ . Consider now the case where the calibration criterion  $J(.)$  can be expressed as an expected value  $J(\theta) = E^{\theta} \left[ \int_0^T \phi(X_t) dt \right]$  with a strictly convex function  $\phi(.)$ . A classical approach to solve the calibration problem

$$\inf_{\theta \in E} J(\theta), \quad \text{under} \quad E^{\theta}[H_i] = C_i \tag{22}$$

is to introduce the Lagrangian functional

$$\mathcal{L}(\theta,\lambda) = J(\theta) - \sum_{i \in I} \lambda_i (E^{\theta}[H_i] - C_i)$$
$$= E^{\theta} \left[ \int_0^T \phi(X_t) \, \mathrm{d}t - \sum_{i \in I} \lambda_i (H_i - C_i) \right]$$
(23)

where  $\lambda_i$  is the Lagrange multiplier associated to the calibration constraint for payoff  $H_i$ . The *dual* problem associated to the constrained minimization problem  $(22)$  is given by

$$\inf_{\theta \in E} \mathcal{L}(\theta, \lambda) = \inf_{\theta \in E} E^{\theta} \int_{0}^{T} \phi(X_{t}) dt$$
$$- \sum_{i \in I} \lambda_{i}(H_{i} - C_{i})$$
$$\Phi$$
 (24)

It can be viewed as a *stochastic control problem* (see Stochastic Control) with running cost  $\phi(t, X_t)$ and *terminal cost*  $\Phi$ .

This original formulation of the calibration problem was first presented by Avellaneda et al. [7] in the context of diffusion model with unknown volatility

$$dS_t = S_t \sigma(t, S_t) dW_t \tag{25}$$

The calibration criterion in  $[7]$  was chosen to be

$$J(\sigma) = E^{\sigma} \left[ \int_0^T dt \ \eta(\sigma^2(t, X_t^{\sigma})) \right] \qquad (26)$$

where  $\eta$  is a strictly convex function. Duality between  $(22)$  and  $(24)$  is not obvious in this case since the Lagrangian is not convex with respect to its argument [31]. The stochastic control approach can also be applied in the context of model calibration by relative entropy minimization for classes of models where absolute continuity is preserved under a change of parameters, such as models with jumps. Cont and Minca [18] use this approach for retrieving the default rate in a portfolio from CDO tranche spreads indexed on the portfolio.

#### **Stochastic Algorithms**

Objective functions used in calibration (with the exception of entropy-based methods) are typically nonconvex, event after regularization, leading to multiple minima and lack of convergence in gradientbased methods. Stochastic algorithms known as evolutionary algorithms, which contain simulated annealing as a special case, have been widely used for global nonconvex optimization are natural candidate for solving such problems [9].

Suppose, for instance, we want to minimize the pricing error

$$J_0(\theta) = \sum_{i=1}^{I} w_i |C_i^{\theta} - C_i|, \quad \theta \in E \qquad (27)$$

where  $C_i^{\theta}$  are model prices and  $C_i$  are observed (transaction or mid-market) prices for the benchmark options. Now define the *a priori* error level  $\delta$  as

$$\delta = \sum_{i=1}^{I} w_i |C_i^{\text{bid}} - C_i^{\text{ask}}| \tag{28}$$

Given the uncertainty on option values due to bid-ask spreads, one cannot meaningfully distinguish a "perfect" fit  $J_0(\theta) = 0$  from any other fit with  $J_0(\theta) \leq \delta$ . Therefore, all parameter values in the level set  $G_{\delta} = \{ \theta \in E, J_0(\theta) \leq \delta \}$  correspond to

models that are compatible with the market data  $(C_i^{\text{bid}}, C_i^{\text{ask}})_{i=1..I}$ . An evolutionary algorithm simulates an inhomogeneous Markov chain  $(X_n)_{n>1}$  in  $E^N$  which undergoes mutation-selection cycles [9] designed such that as the number of iterations  $n$ grows, the components  $(\theta_1^N, ..., \theta_n^N)$  of  $X_n$  converge to the  $G_{\delta}$ , yielding a population of points  $(\theta_k)$  which converges to a sample of model parameters compatible with the market data  $(C_i^{\text{bid}}, C_i^{\text{ask}})_{i=1..I}$  in the sense that  $J_0(\theta_k) \leq \delta$ . We thus obtain a population of N model parameters calibrated to market data, which can be different especially if the initial problem has multiple solutions.

Figure 4 shows a sample of local volatility functions obtained using this approach [9]. These examples illustrate that precise reconstruction of local volatility from call option prices is at best illusory; the parameter uncertainty is too important to be ignored, especially for short maturities where it does not affect the prices very much; short-term volatility hovers anywhere between 15% and 30%. These observations cast a doubt on the volatility content of very short-term options in terms of volatility and questions whether one can solely rely on short maturity asymptotics (*see SABR Model*) in model calibration.

#### **Parameter Uncertainty**

Model calibration is usually the first step in a procedure whose ultimate purpose is the pricing and hedging of (exotic) options. Once the model parameter  $\theta$  is calibrated to market prices, it is used to compute a model-dependent quantity  $f(\theta)$ —price of an exotic option or a hedge ratio—using a numerical procedure. Given the ill-posedness of the calibration problem and the resulting uncertainty on the solution  $\theta$ , one question is the impact of this uncertainty on such model-dependent quantities. This aspect is often neglected in practice and many users of pricing models view the calibrated parameter as fixed, equating calibration with a curve-fitting exercise.

Particle methods yield, as a by-product, a way to analyze model uncertainty. While calibration algorithms based on deterministic optimization yield a point estimate for model parameters, particle methods yield a *population*  $Q = \{Q_{\theta_1}, ..., Q_{\theta_k}\}$  of pricing models, all of which price the benchmark options with equivalent precision  $E^{\mathbb{Q}}(H_i) \in [C_i^{\text{bid}}, C_i^{\text{ask}}]$ . The

![](_page_7_Figure_1.jpeg)

Confidence intervals for local volatility : DAX options.

**Figure 4** A sample of local volatility surfaces calibrated to DAX options

heterogeneity of this population reflects the uncertainty in model parameters, which are left undetermined by the benchmark options. This idea can be exploited to produce a quantitative measure of model uncertainty compatible with observed market prices of benchmark instruments [14], by considering the interval of prices

$$\left[\inf_{\mathbb{Q}\in\mathcal{Q}}E^{\mathbb{Q}}[X],\sup_{\mathbb{Q}\in\mathcal{Q}}E^{\mathbb{Q}}[X]\right] \tag{29}$$

for a payoff *X* in the various calibrated models. Another approach is to calibrate several different models to the same data and compare the value of the exotic option across models [14, 32]. Model uncertainty in derivative pricing is further discussed in [14].

## **Relation with Pricing and Hedging**

Calibrating a model to market prices simply ensures that model prices of benchmark instruments reflect current "mark-to-market" values. It also ensures that the cost of a static hedge (*see* **Static Hedging**) using these benchmark instruments is correctly reflected in model prices: if a payoff *H* can be statically hedged with a portfolio containing *αi* units of benchmark instrument *Hi*,

$$H = \alpha_0 + \sum_{i \in I} \alpha_i H_i \tag{30}$$

the cost *α*<sup>0</sup> + *αiCi* of setting up the hedge is automatically equal to the model price *E*[*H*].

Calibration does not entail that prices, hedge ratios, or risk parameters generated by the model are "correct" in any sense. This requires a correct model specification with realistic dynamics for risk factors. Indeed, many different models may calibrate the same prices of, say, a set of call options but lead to very different prices of hedge ratios for exotics [14, 32]. For example, any equity volatility smile can be reproduced by a one-factor diffusion model (see Example 1) *via* an appropriate specification of the local volatility surface, but there is ample evidence that volatility itself should be modeled as a risk factor (*see* **Stochastic Volatility Models**) and a one-factor diffusion may lead to an underestimation of volatility risk and unrealistic dynamics [30].

However, a model that is *not calibrated* to market prices of liquidly traded derivatives is typically not easy to use. For example, even if a payoff can be statically hedged with traded derivatives using an initial capital *V*0, the model price will not be equal to *V*0. Thus, model prices will, in general, be inconsistent with hedging costs if the model is not calibrated. Thus, calibration seems a necessary but not sufficient condition for choosing a model for pricing and hedging.

## **References**

- [1] Achdou, Y. (2005). An inverse problem for a parabolic variational inequality arising in volatility calibration with American options, *SIAM Journal on Control and Optimization* **43**, 1583–1615.
- [2] Achdou, Y. & Pironneau, O. (2002). Volatility smile by multilevel least square, *International Journal of Theoretical and Applied Finance* **5**(2), 619–643.
- [3] d'Aspremont, A. (2005). Risk-management methods for the Libor market model using semidefinite programming, *Journal of Computational Finance* **8**(4), 77–99.
- [4] Avellaneda, M. (1998). The minimum-entropy algorithm and related methods for calibrating asset-pricing models, *Proceedings of the International Congress of Mathematicians*, Documenta Mathematica, Berlin, Vol. III, pp. 545–563.
- [5] Avellaneda, M., Boyer-Olson, D., Busca, J. & Friz, P. (2002). Reconstructing the smile, *Risk Magazine* October.
- [6] Avellaneda, M., Buff, R., Friedman, C., Grandchamp, N., Kruk, L. & Newman, J. (2001). Weighted Monte Carlo: a new technique for calibrating asset-pricing models, *International Journal of Theoretical and Applied Finance* **4**, 91–119.
- [7] Avellaneda, M., Friedman, C., Holmes, R. & Samperi, D. (1997). Calibrating volatility surfaces via relative entropy minimization, *Applied Mathematical Finance* **4**, 37–64.
- [8] Belomestny, D. & Reiss, M. (2006). Spectral calibration of exponential Levy Models, ´ *Finance and Stochastics* **10**(4), 449–474.
- [9] Ben Hamida, S. & Cont, R. (2004). Recovering volatility from option prices by evolutionary optimization, *Journal of Computational Finance* **8**(3), 43–76.
- [10] Berestycki, H., Busca, J. & Florent, I. (2004). Computing the implied volatility in stochastic volatility models, *Communications on Pure and Applied Mathematics* **57**(10), 1352–1373.
- [11] Bouchouev, I., Isakov, V. & Valdivia, N. (2002). Recovering a volatility coefficient by linearization, *Quantitative Finance* **2**, 257–263.
- [12] Carr P., Geman H., Madan D.B. & Yor M. (2004). From local volatility to local Levy models, ´ *Quantitative Finance* **4**(5), 581–588.
- [13] Coleman, T., Li, Y. & Verma, A. (1999). Reconstructing the unknown volatility function, *Journal of Computational Finance* **2**(3), 77–102.

- [14] Cont, R. (2006). Model uncertainty and its impact on the pricing of derivative instruments, *Mathematical Finance* **16**(3), 519–547.
- [15] Cont, R. & Deguest, R. (2009). *What do index options imply about the dependence among stock returns?* Columbia University Financial Engineering Report 2009- 06,www.ssrn.com.
- [16] Cont, R., Deguest, R. & Kan, Y.H. (2009). *Default Intensities Implied by CDO Spreads: Inversion Formula and Model Calibration*. Columbia University Financial Engineering Report 2009-04, www.ssrn.com.
- [17] Cont, R. & Leonard, Ch. (2008). ´ *A Probabilistic Approach to Inverse Problems in Option Pricing*. Working Paper.
- [18] Cont, R. & Minca, A. (2008). *Recovering Portfolio Default Intensities Implied by CDO Tranches*. Financial Engineering Report 2008-01, Columbia University.
- [19] Cont, R. & Rouis, M. (2006). *Recovering L´evy Processes from Option Prices by Tikhonov Regularization*. Working Paper.
- [20] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman and Hall/CRC Press, Boca Raton.
- [21] Cont, R. & Tankov, P. (2004). Nonparametric calibration of jump-diffusion option pricing models, *Journal of Computational Finance* **7**(3), 1–49.
- [22] Cont, R. & Tankov, P. (2005). Recovering Levy pro- ´ cesses from option prices: regularization of an ill-posed inverse problem, *SIAM Journal on Control and Optimization* **45**(1), 1–25.
- [23] Crepey, S. (2003). Calibration of the local volatility in ´ a trinomial tree using Tikhonov regularization, *Inverse Problems* **19**, 91–127.
- [24] Csiszar, I. (1975). I-divergence geometry of probability ´ distributions and minimization problems, *The Annals of Probability* **3**, 146–158.
- [25] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- [26] Engl, H. & Egger, H. (2005). Tikhonov regularization applied to the inverse problem of option pricing: convergence analysis and rates, *Inverse Problems* **21**, 1027–1045.
- [27] Engl, H.W., Hanke, M. & Neubauer, A. (1996). *Regularization of Inverse Problems*, Mathematics and its Applications, Kluwer Academic Publishers, Dordrecht, The Netherlands, Vol. 375.
- [28] Friz, P. & Gatheral, J. (2005). *Valuing Volatility Derivatives as an Inverse Problem, Quantitative Finance*, December 2005.
- [29] Glasserman, P. & Yu, B. (2005). Large sample properties of weighted Monte Carlo estimators, *Operations Research* **53**(2), 298–312.
- [30] Hagan, P., Kumar, D., Lesniewski, A.S. & Woodward, D.E. Managing smile risk, *Wilmott Magazine* September, 84–108.
- [31] Samperi, D. (2002). Calibrating a diffusion model with uncertain volatility, *Mathematical Finance* **12**, 71–87.

[32] Schoutens, W., Simons, E. & Tistaert, J. (2004). A perfect calibration! Now what? *Wilmott Magazine* March.

## **Further Reading**

- Biagini, S. & Cont, R. (2006). Model-free representation of pricing rules as conditional expectations, in *Stochastic Processes and Applications to Mathematical Finance*, J. Akahori, S. Ogawa and S. Watanabe, eds, World Scientific, Singapore, pp. 53–66.
- Harrison, J.M. & Pliska, S.R. (1981). Martingales and stochastic integrals in the theory of continuous trading, *Stochastic Processes and their Applications* **11**, 215–260.

## **Related Articles**

**Black–Scholes Formula**; **Convex Duality**; **Dupire Equation**; **Entropy-based Estimation**; **Exponential Levy Models ´** ; **Implied Volatility in Stochastic Volatility Models**; **Implied Volatility: Large Strike Asymptotics**; **Jump Processes**; **Local Volatility Model**; **Markov Functional Models**; **SABR Model**; **Stochastic Volatility Models**; **Weighted Monte Carlo**; **Yield Curve Construction**.

RAMA CONT
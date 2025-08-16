# **Realized Volatility** Options

Let the underlying process  $Y$  be a positive semimartingale, and let  $X_t := \log(Y_t/Y_0)$ .

Define realized variance to be  $[X]$ , where  $[\cdot]$ denotes the quadratic variation (but see the section "Contract Specifications in Practice").

Define a *realized variance option* on  $Y$  with variance strike  $O$  and expiry  $T$  to pay

$$([X]_T - Q)^+$$
 for a realized variance call

 $(Q - [X]_T)^+$  for a realized variance put

and define a realized volatility option on  $Y$  with volatility strike  $Q^{1/2}$  and expiry T to pay

$$([X]_T^{1/2} - Q^{1/2})^+$$
 for a realized volatility call  
 $(Q^{1/2} - [X]_T^{1/2})^+$  for a realized volatility put

In some places, we restrict attention to puts. Call prices follow by put-call parity: for realized variance options, a long-call short-put combination pays  $[X]_T - Q$ , equal to a Q-strike variance swap, and for realized volatility options, a long-call short-put combination pays  $[X]_T^{1/2} - Q^{1/2}$ , equal to a  $Q^{1/2}$ -strike volatility swap.

Unlike variance swaps (see Variance Swap; Weighted Variance Swap), which admit exact model-free (assuming only continuity of  $Y$ ) hedging and pricing in terms of Europeans, variance, and volatility options have a range of values, consistent with the given prices of Europeans. With no further assumptions, there exist sub/superreplication strategies and lower/upper pricing bounds (in the section "Pricing Bounds by Model-free Use of Europeans"). Under an independence condition, there exist exact pricing formulas in terms of Europeans (in the section "Pricing by Use of Europeans, Under an Independence Condition"). Under specific models, there exist exact pricing formulas in terms of model parameters (in the section "Pricing by Modeling the Underlying Process").

Unless otherwise noted, all prices are denominated in units of a  $T$ -maturity discount bond. The results apply to dollar-denominated prices, provided that

interest rates vary deterministically, because if  $Y'$  is a dollar-denominated share price and  $Y$  is that share's bond-denominated price, then  $\log Y - \log Y'$  has finite variation; hence,  $[\log Y] = [\log Y']$ .

Expectations  $\mathbb{E}$  will be with respect to martingale measure  $\mathbb{P}$ .

## **Transform Analysis**

Some of the methods surveyed here (in the sections "Pricing by Modeling the Underlying Process" and "Pricing via Transform") will price variance/volatility options by integrating prices of payoffs of the form  $e^{z[X]_T}$ . Transform analysis relates the former to the latter, by the following pricing formulas, proved in [5].

Assume that the continuous payoff function  $h$ :  $\mathbb{R} \to \mathbb{R}$  satisfies

$$\int_{-\infty}^{\infty} e^{-\alpha q} h(q) \, \mathrm{d}q < \infty \tag{1}$$

for some  $\alpha \in \mathbb{R}$ . For all  $z \in \alpha + \mathbb{R}i := \{z \in \mathbb{C} :$  $\text{Re } z = \alpha$ , define the bilateral Laplace transform

$$H(z) := \int_{-\infty}^{\infty} e^{-zq} h(q) \, dq \tag{2}$$

If  $|H|$  is integrable along  $\alpha + \mathbb{R}i$  for some  $\alpha < 0$ , then by Bromwich and Fubini, the  $h([X]_T)$  payoff has price

$$\mathbb{E}h([X]_T) = \frac{1}{2\pi i} \int_{\alpha - \infty i}^{\alpha + \infty i} H(z) \mathbb{E}e^{z[X]_T} dz \qquad (3)$$

For a *variance put*, let  $h(q) = (Q - q)^+$ . Then for all  $\alpha$  < 0, formula (3) holds with

$$H(z) = \frac{\mathrm{e}^{-Qz}}{z^2} \tag{4}$$

For a *volatility put*, let  $h(q) = \left(\sqrt{Q} - \sqrt{q^+}\right)^+$ . Then for all  $\alpha < 0$ , formula (3) holds with

$$H(z) = -\frac{\sqrt{\pi} \operatorname{Erf}(\sqrt{zQ})}{2z^{3/2}} \tag{5}$$

To price variance and volatility calls by put-call parity, we have the variance swap value

$$\mathbb{E}[X]_T = \frac{\partial}{\partial z}\bigg|_{z=0} \mathbb{E} e^{z[X]_T} \tag{6}$$

and the volatility swap value

$$\mathbb{E}[X]_T^{1/2} = \frac{1}{2\sqrt{\pi}} \int_0^\infty \frac{1 - \mathbb{E} e^{-z[X]_T}}{z^{3/2}} \, \mathrm{d}z \qquad (7)$$

if  $\mathbb{E}e^{z[X]_T}$  is analytic in a neighborhood of  $z=0$ .

## Pricing by Modeling the Underlying Process

Under Heston and under Lévy models, we give formulas for the transform  $\mathbb{E}e^{z[X]_T}$ , where  $\text{Re } z < 0$ . Hence, formula (3) prices the variance put and volatility put, using equations  $(4)$  and  $(5)$ , respectively.

#### Example: Heston Dynamics

Under the Heston model for instantaneous variance (see Heston Model),

$$dV_t = (a - \kappa V_t) dt + \beta \sqrt{V_t} dW_t \qquad (8)$$

and the transform of  $[X]_T = \int_0^T V_t \, dt$  is

$$\mathbb{E}e^{z[X]_T} = e^{A(z) + B(z)V_0} \tag{9}$$

where

$$A(z) := \frac{a}{\beta^2} \bigg[ (\kappa - \gamma)T$$
$$- 2\log\left(1 + \frac{\kappa - \gamma}{2\gamma}(1 - e^{-\gamma T})\right) \bigg] \quad (10)$$
$$B(z) := \frac{2z(e^{\gamma T} - 1)}{2\gamma + (\gamma + \kappa)(e^{\gamma T} - 1)},$$
$$\gamma := \sqrt{\kappa^2 - 2\beta^2 z} \quad (11)$$

by [6]. Other affine models also have explicit formulas for  $\mathbb{E}e^{z[x]_T}$ .

#### Example: Lévy Dynamics

If  $X$  is a Lévy process (see Lévy Processes) with Gaussian variance  $\sigma^2$  and Lévy measure v, then [X] has transform

$$\mathbb{E}e^{z[X]_T} = \exp\left(T\frac{\sigma^2 z^2}{2} + T\int_{\mathbb{R}} \left(e^{zx^2} - 1\right)\nu(dx)\right) \tag{12}$$

For variance option pricing under pure-jump processes with independent increments, but without assuming stationary increments, see [2].

# Pricing by Use of Europeans, Under an **Independence Condition**

In this section, let  $Y$  be a share price that follows general stochastic volatility dynamics

$$\mathrm{d}Y_t = \sigma_t Y_t \ \mathrm{d}W_t \tag{13}$$

where  $\sigma$  and the Brownian motion *W* are independent. Although all three subsections use this assumption, the schemes in the sections "Pricing via Transform" and "Pricing and Hedging via Uniform or  $L^2$  Payoff Approximation" are immunized, to first order, against violations of the independence condition.

#### Pricing via Transform

The transform of  $[X]_T = \int_0^T \sigma_t^2 dt$  satisfies [5]

$$\mathbb{E}e^{z[X]_{t}} = \mathbb{E}\bigg(\theta_{+}(Y_{T}/Y_{0})^{1/2+\sqrt{(1/4)+2z}} + \theta_{-}(Y_{T}/Y_{0})^{1/2-\sqrt{(1/4)+2z}}\bigg) \tag{14}$$

provided that the expectations are finite. Here,  $\theta_{\pm}$  :=  $(1 \mp 1/\sqrt{1+8z})/2$ . The right-hand side (RHS) of equation (14) is in principle observable from  $T$ expiry Europeans, which allows variance/volatility put option pricing by the formulas  $(3-5)$ . In this context, equation (6) can be replaced by the logcontract value  $-2\mathbb{E}X_T$ , and equation (7) can be replaced by the synthetic volatility swap value (see Volatility Swaps).

Moreover, source  $[5]$  shows that equation  $(14)$ still holds approximately in the presence of correlation between  $\sigma$  and W, in the sense that the RHS is constructed to have zero sensitivity to first-order correlation effects.

# Pricing and Hedging via Uniform or $L^2$ Payoff Approximation

For continuous payoffs,  $h: [0, \infty) \to \mathbb{R}$  with finite limit at  $\infty$ , such as the variance put or volatility put, consider an *n*th-order approximation to  $h(q)$ 

$$A_n(q) := a_{n,n} e^{-cnq} + a_{n,n-1} e^{-c(n-1)q} + \dots + a_{n,0}$$
(15)

where  $c > 0$  is an arbitrary constant.

To choose A by uniform approximation,  $a_{n,k}$ may be determined as the coefficients of the  $n$ th Bernstein polynomial approximation to the function  $x \mapsto h(-(1/c) \log x)$  on [0, 1].

Then source  $[5]$  shows that

$$\mathbb{E}h([X]_T)$$
  
=  $\lim_{n \to \infty} \mathbb{E} \sum_{k=0}^n a_{n,k} \bigg( \theta_+ (Y_T/Y_0)^{1/2 + \sqrt{1/4 - 2ck}}$   
+  $\theta_- (Y_T/Y_0)^{1/2 - \sqrt{1/4 - 2ck}} \bigg)$  (16)

where  $\theta_{\pm} := (1 \mp 1/\sqrt{1-8ck})/2$ . The RHS of equation (16) is, in principle, observable from  $T$ -expiry Europeans and is moreover designed to have zero sensitivity to first-order correlation effects.

Alternatively, to choose A by  $L^2$  approximation, the  $a_{n,k}$  may be determined by  $L^2(\mu)$  projection of *h* onto span $\{1, e^{-cq}, \ldots, e^{-cnq}\}$ , where the "prior"  $\mu$ is a finite measure on  $[0, \infty)$ . In practice,  $a_{n,k}$  may be computed by weighted least squares regression of  $h(q)$  on the regressors  $\{q \mapsto e^{-ckq} : k = 0, \ldots, n\}$ , with weights given by  $\mu$ . Then source [5] shows that equation (16) still holds, regardless of the choice of the prior  $\mu$ , provided that  $dP/d\mu$  exists in  $L^2(\mu)$ , where *P* denotes the  $\mathbb{P}$ -distribution of  $[X]_T$ .

For *hedging* purposes, the summation in the RHS of equation (16) provides a European-style payoff that, in conjunction with share trading, replicates the volatility payoff  $h([X]_T)$  to arbitrary accuracy.

#### Pricing via Variance Distribution Inference

Given the prices  $\mathbf{c} \in \mathbb{R}^{N \times 1}$  of vanilla options at strikes  $K_1, \ldots, K_N$ , a scheme in [8] discretizes into  $\{v_1,\ldots,v_J\}$  the possible values of  $[X]_T$ , and proposes to infer the discretized variance distribution  $\mathbf{p} \in$  $\mathbb{R}^{J\times 1}$  where  $p_i := \mathbb{P}([X]_T = v_i)$ , by solving approximately for  $\mathbf{p}$  in

$$\mathbf{Bp} = \mathbf{c} \tag{17}$$

where  $\mathbf{B} \in \mathbb{R}^{N \times J}$  is given by  $B_{ni} := C^{BS}(K_n, v_i),$ the Black-Scholes formula for strike  $K_n$  and squared unannualized volatility  $v_i$ . The approximate solution is chosen to minimize  $\|\mathbf{B}\mathbf{p} - \mathbf{c}\|^2$  plus a convex penalty term. The contact paying  $h([X]_T)$  is then priced as  $\sum p_i h(v_i)$ .

## **Pricing by Use of Variance or Volatility** Swaps

With sufficient liquidity, variance and/or volatility swap quotes can be taken as inputs. For example, an approximation in [8] prices variance options by fitting a lognormal variance distribution to variance and volatility swaps of the same expiry. An approximation in [4] prices and hedges variance and volatility options by fitting a displaced lognormal, to variance and volatility swaps.

The variance curve models in  $[1]$  apply a different approach to using variance swaps; they take as inputs the variance swap quotes at multiple expiries, and they model the dynamics of the term structure of forward variance. Applications include pricing and hedging of realized variance options.

# **Pricing Bounds by Model-free Use of** Europeans

In this section, consider variance options on, more generally, any continuous share price  $Y$ .

Given European options of the same expiry  $T$ , there exist model-free sub/superreplication strategies, and hence lower/upper pricing bounds, for the variance options. Here *model-free* means that, aside from continuity and positivity, we make *no* assumptions on  $Y$ .

#### Subreplication and Lower Bounds

The following subreplication strategy is due to  $[7]$ : this exposition also draws from  $[3]$ .

Let  $\lambda : (0, \infty) \to \mathbb{R}$  be convex, let  $\lambda_{\nu}$  denote its left-hand derivative, and assume that its second derivative in the distributional sense has a density, denoted  $\lambda_{yy}$ , which satisfies for all  $y \in \mathbb{R}_+$ 

$$\lambda_{yy}(y) \le 2/y^2 \tag{18}$$

Define for  $y > 0$  and  $v > 0$ 

$$BS(y, v; \lambda) := \int_{-\infty}^{\infty} \lambda(ye^{z}) \frac{1}{\sqrt{2\pi v}} e^{-(z+v/2)^{2}/(2v)} \,\mathrm{d}z \tag{19}$$

and define  $BS(y, 0; \lambda) := \lambda(y)$ , and let  $BS_y$  denote its y-derivative. Let  $\tau_Q := \inf\{t \ge 0 : [X]_t \ge Q\}.$ Then the following trading strategy subreplicates the variance call payoff: hold statically a claim that pays at time  $T$ 

$$\lambda(Y_T) - BS(Y_0, Q; \lambda) \tag{20}$$

and trade shares dynamically, holding at each time  $t \in (0, T)$ 

$$-BS_{y}(Y_{t}, Q - [X]_{t}; \lambda) \qquad \text{shares if } t \leq \tau_{Q}$$
$$-\lambda_{y}(Y_{t}) \qquad \text{shares if } t > \tau_{Q} \quad (21)$$

and a bond position that finances the shares and accumulates the trading gains or losses. Therefore, the time-0 value of the contract paying  $(20)$  provides a lower bound on the variance call value.

The lower bound from equation  $(20)$  is optimized by  $\lambda$  consisting of  $2/K^2$  dK out-of-the-money vanilla payoffs at all K where  $I_0(K, T)$ , the squared unannualized Black–Scholes implied volatility, exceeds  $Q$ :

$$\lambda(y) = \int_{\{K: I_0(K,T) > Q\}} \frac{2}{K^2} \text{van}_K(y) \, \mathrm{d}K \qquad (22)$$

See [3] for generalization to forward-starting variance options.

#### Superreplication and Upper Bounds

The following superreplication strategy is due to [3]. Choose any  $b_d \in (0, Y_0]$  and  $b_u \in [Y_0, \infty)$ . Let

$$\begin{split} BP(y,q) \\ &:= \int_{-\infty - \alpha i}^{\infty - \alpha i} \left[ \sqrt{y/b_u} \sinh \left( \log (b_d/y) f(z) \right) \right. \\ &\left. - \sqrt{y/b_d} \sinh \left( \log (b_u/y) f(z) \right) \right] \\ &\left. \left. \left[ 2\pi z^2 e^{i(Q-q)z} \sinh \left( \log (b_u/b_d) f(z) \right) \right] \mathrm{d}z \right. \end{split} \tag{23}$$

where  $f(z) := \sqrt{1/4 - 2iz}$  and where  $\alpha > 0$  is arbitrary. For  $y > 0$  and  $b_d \neq b_u$ , define

$$L(y; b_{d}, b_{u})$$
  
:= -2 log(y/b<sub>u</sub>) + 2  $\frac{\log(b_{u}/b_{d})}{b_{u} - b_{d}}(y - b_{u})$  (24)

and define  $L(y; Y_0, Y_0) := -2\log(y/Y_0) + 2y/Y_0 - 2$ . Let

$$L^*(y) := \begin{cases} L(y) & \text{if } y \notin (b_d, b_u) \\ -BP(y, 0) & \text{if } y \in (b_d, b_u) \end{cases} \tag{25}$$

Let  $BP_y$  and  $L_y$  denote the y-derivatives, and let  $\tau_b := \inf\{t \ge 0: \ Y_t \notin (b_d, b_u)\}.$ 

Then, the following strategy superreplicates the variance call payoff  $([X]_T - Q)^+$ . Hold statically a claim that pays at time  $T$ 

$$L^*(Y_T) - L^*(Y_0) \t\t(26)$$

and trade shares dynamically, holding at each time at each time  $t \in (0, T)$ 

$$BP_{y}(Y_{t}, [X]_{t} - [X]_{0}) \quad \text{shares if } 0 \le t \le \tau_{b}$$
$$-L_{y}(Y_{t}) \quad \text{shares if } t > \tau_{b} \tag{27}$$

and a bond position that finances the shares and accumulates the trading gains or losses.

Therefore, the time-0 value of the contract paying  $(26)$  provides an upper bound on the variance call value. Given  $T$ -expiry European options data, the upper bound from equation (26) may be optimized over all choices of  $(b_d, b_u)$ .

#### Connection to the Skorokhod Problem

Whereas the sections "Subreplication and Lower Bounds" and "Superreplication and Upper Bounds" presented explicit hedging strategies, which imply pricing bounds, this section presents (a logarithmic version of) the result in [7], which showed that stopping-time analysis also implies pricing bounds.

Denote by  $\nu$  the  $\mathbb{P}$ -distribution of  $Y_T$ , which is revealed by the prices of  $T$ -expiry options on  $Y$ .

Suppose that  $\tilde{Y}$  is a continuous  $\mathcal{F}$ -martingale with  $\tilde{Y}_T \sim \nu$ , and  $[\tilde{X}]_T$  has finite expectation, where  $\tilde{X} :=$  $\log \tilde{Y}$ . Then Dambis–Dubins–Schwartz implies that  $\tilde{Y}_t = G_{[\tilde{X}]_t}$ , where G is a driftless unit-volatility geometric  $\mathcal{G}$ -Brownian motion (on an enlarged probability space if needed) with  $G_0 = Y_0$ , and  $[\tilde{X}]_t$ are  $\mathcal{G}$ -stopping times, where  $\mathcal{G}_s := \mathcal{F}_{\inf\{t: [\tilde{X}]_t > s\}}$ . Thus  $G_{[\tilde{X}]_T} \sim \nu$ ; and hence  $[\tilde{X}]_T$  solves a Skorokhod problem (see Skorokhod Embedding): it is a finiteexpectation stopping time that embeds the distribution  $\nu$  in G. Conversely, if some finite-expectation  $\tau$  embeds  $\nu$  in a driftless unit-volatility geometric Brownian motion G, then  $\tilde{Y}_t := G_{\tau \wedge (t/(T-t))}$  defines a continuous martingale with  $\tilde{Y}_T \sim \nu$  and  $[\log \tilde{Y}]_T = \tau$ .

Therefore, distributions of stopping times solving the Skorokhod problem are identical to distributions of realized variance consistent with the given price distribution  $\nu$ . Skorokhod solutions that have optimality properties, therefore, imply bounds on prices of variance/volatility options. In particular, *Root's* solution is known [9] to minimize the expectations of convex functions of the stopping time; the minimized expectation is, in that sense, a sharp lower bound on the price of a variance option (see also **Skorokhod** Embedding).

#### **Contract Specifications in Practice**

In practice, the realized variance in the payoff specification is defined by replacing quadratic variation  $[X]_T$  with an annualized discretization that monitors  $Y$ , typically daily, for  $N$  periods, resulting in a specification

Annualization 
$$\times \sum_{n=1}^{N} \left( \log \frac{Y_n}{Y_{n-1}} \right)^2$$
 (28)

If the contract adjusts for dividends (as typical for single-stock dividends but not index dividends) then the term inside the parentheses becomes  $\log((Y_n +$  $D_n)/Y_{n-1}$ , where  $D_n$  denotes the discrete dividend payment, if any, of the  $n$ th period.

## References

- [1] Buehler, H. (2006). Consistent variance curve models, Finance and Stochastics  $10(2)$ , 178–203.
- [2] Carr, P., Geman, H., Madan, D. & Yor, M. (2005). Pricing options on realized variance, Finance and Stochastics  $9(4), 453-475.$
- [3] Carr, P. & Lee, R. Hedging variance options on continuous semimartingales, Finance and Stochastics, forthcoming.
- [4] Carr, P. & Lee, R. (2007). Realized volatility and variance: options via swaps, Risk  $20(5)$ , 76-83.
- [5] Carr, P. & Lee, R. (2008). Robust Replication of Volatility Derivatives, Bloomberg LP and University of Chicago.
- [6] Cox, J., Ingersoll, J. & Ross, S. (1985). A theory of the term structure of interest rates, *Econometrica* 53(2), 385-407.
- [7] Dupire, B. (2005). Volatility Derivatives Modeling, Bloomberg LP.
- [8] Friz, P. & Gatheral, J. (2005). Valuation of volatility derivatives as an inverse problem, Quantitative Finance 5(6), 531–542.
- [9] Rost, H. (1976). Skorokhod stopping times of minimal variance, Séminaire de Probabilités (Strasbourg), Springer-Verlag, Vol. 10, pp. 194-208.

# **Related Articles**

Exponential Lévy Models; Heston Model; Lévy Processes; Skorokhod Embedding; Variance Swap; Volatility Swaps; Volatility Index Options; Weighted Variance Swap.

ROGER LEE
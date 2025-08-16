# **Backward Stochastic Differential Equations: Numerical Methods**

Nonlinear backward stochastic differential equations (BSDEs) were introduced in 1990 by Pardoux and Peng [34]. The interest in BSDEs comes form their connections with partial differential equations (PDEs) [14, 38]; stochastic control (see Stochastic Control); and mathematical finance (see [16, 17], among others). In particular, as shown in [15], BSDEs are a useful tool in the pricing and hedging of European options. In a complete market, the price process  $Y$ of  $\xi$  is a solution of a BSDE. BSDEs are also useful in quadratic hedging problems in incomplete markets (see Mean-Variance Hedging).

The result that there exist unique BSDE equations under the assumption that the generator is locally Lipschitz can be found in [19]. A similar result was obtained in the case when the coefficient is continuous with linear growth [24]. The same authors, Lepeltier and San Martín [23], generalized these results under the assumption that the coefficients have a superlinear quadratic growth. Other extensions of existence and uniqueness of BSDE are dealt with in [20, 25, 30]. Stability of solutions for BSDE have been studied, for example, in [1], where the authors analyze stability under disturbances in the filtration. In [6], the authors show the existence and uniqueness of the solution and the link with integral-PDEs (see Partial Integro-differential Equations (PIDEs)). An existence theorem for BSDEs with jumps is presented in [25, 36]. The authors state a theorem for Lipschitz generators proved by fixed point techniques [37].

Since BSDE solutions are explicit in only a few cases, it is natural to search for numerical methods approximating the unique solution of such equations and to know the associated type of convergence. Some methods of approximation have been developed.

A four-step algorithm is proposed in [27] to solve equations of forward-backward type, relating the type of approximation to PDEs theory. On the other hand, in [3], a method of random discretization in time is used where the convergence of the method for the solution  $(Y, Z)$  needs regularity

assumptions only, but for simulation studies multiple approximations are needed. See also [10, 13, 28] for forward-backward systems of SDE (FBSDE) solutions, [18] for a regression-based Monte Carlo method, [39] for approximating solutions of BSDEs, and [35] for Monte Carlo valuation of American Options.

On the other hand, in [2, 9, 11, 26] the authors replace Brownian motion by simple random walks in order to define numerical approximations for BSDEs. This technique simplifies the computation of conditional expectations involved at each time step.

A quantization (see **Quantization Methods**) technique was suggested in  $[4, 5]$  for the resolution of reflected backward stochastic differential equations (RBSDEs) when the generator  $f$  does not depend on the control variable  $z$ . This method is based on the approximation of continuous time processes on a finite grid, and requires a further estimation of the transition probabilities on the grid.

In [8], the authors propose a discrete-time approximation for approximations of RBSDEs. The  $L^p$  norm of the error is shown to be of the order of the time step. On the other hand, a numerical approximation for a class of RBSDEs based on numerical approximations for BSDE and approximations given in [29], can be found in [31, 33].

Recently, work on numerical schemes for jumps is given in  $[22]$  and is based on the approximation for the Brownian motion and a Poisson process by two simple random walks. Finally, for decoupled FBSDEs with jumps a numerical scheme is proposed in [7].

Let  $\Omega = \mathcal{C}([0, 1], \mathbb{R}^d)$  and consider the canonical Wiener space  $(\Omega, \mathcal{F}, \mathbb{P}, \mathcal{F}_t)$ , in which  $B_t(\omega) = \omega(t)$ is a standard  $d$ -dimensional Brownian motion. We consider the following BSDE:

$$Y_t = \xi + \int_t^T f(s, Y_s, Z_s) \mathrm{d}s - \int_t^T Z_s \mathrm{d}B_s \qquad (1)$$

where  $\xi$  is a  $\mathcal{F}_T$ -measurable square integrable random variable and  $f$  is Lipschitz continuous in the space variable with Lipschitz constant  $L$ . The solution of equation (1) is a pair of adapted processes  $(Y, Z)$ , which satisfies the equation.

## **Numerical Methods for BSDEs**

One approach for a numerical scheme for solving BSDEs is based upon a discretization of the equation (1) by replacing  $B$  with a simple random walk. To be more precise, let us consider the symmetric random walk  $W^n$ :

$$W_t^n := \frac{1}{\sqrt{n}} \sum_{k=0}^{c_n(t)} \zeta_k^n, \quad 0 \le t \le T \tag{2}$$

where  $\{\zeta_k^n\}_{1 \le k \le n}$  is an i.i.d. Bernoulli symmetric sequence. We define  $\mathcal{G}_k^n := \sigma(\zeta_1^n, \ldots, \zeta_k^n)$ . Throughout this section  $c_n(t) = [nt]/n$ , and  $\xi^n$  denotes a square integrable random variable, measurable w.r.t.  $\mathcal{G}_n^n$  that should converge to  $\xi$ . We assume that  $W^n$ and  $B$  are defined in the same probability space.

In [26], the authors consider the case when the generator depends only on the variable  $Y$ , which makes the analysis simpler. In this situation, the BSDE  $(1)$  is given by

$$Y_t = \xi + \int_t^T f(Y_s) \mathrm{d}s - \int_t^T Z_s \mathrm{d}B_s \qquad (3)$$

whose solution is given by

$$Y_{t} = \mathbb{E}\left(\xi + \int_{t}^{T} f(Y_{s}) \mathrm{d}s \Big| \mathcal{F}_{t}\right) \tag{4}$$

which can be discretized in time with step-size  $h =$  $T/n$  by solving a discrete BSDE given by

$$Y_{t_i}^n = \xi^n + \frac{1}{n} \sum_{j=i}^n f(Y_{t_j}^n) - \sum_{j=i}^{n-1} Z_{t_j}^n \triangle W_{t_{j+1}}^n \qquad (5)$$

This equation has a unique solution  $(Y_t^n, Z_t^n)$  since the martingale  $W^n$  has the predictable representation property. It can be checked that solving this equation is equivalent to finding a solution to the following implicit iteration problem:

$$Y_{t_i}^n = \mathbb{E}\left\{Y_{t_{i+1}}^n + \frac{1}{n}f(Y_{t_i}^n)\Big|\mathcal{G}_i^n\right\} \tag{6}$$

which, due to the adaptedness condition, is equivalent to

$$Y_{t_i}^n - \frac{1}{n} f(Y_{t_i}^n) = \mathbb{E}\left\{Y_{t_{i+1}}^n \middle| \mathcal{G}_i^n\right\} \tag{7}$$

Furthermore, once  $Y_{t_{i+1}}^n$  is determined,  $Y_{t_i}^n$  is solved  $via$  equation (7) by a fixed point technique:

$$\begin{cases}\nX^0 = \mathbb{E}\left\{Y_{t_{i+1}} \middle| \mathcal{G}_i^n\right\} \\
X^1 = X^0 + \frac{1}{n} f(X^k)\n\end{cases} \tag{8}$$

It is standard to show that if  $f$  is uniformly Lipschitz in the spatial variable  $x$  with Lipschitz constant  $L$  (we also assume that  $f$  is bounded by  $R$ ), then the iterations of this procedure will converge to the true solution of equation (7) at a geometric rate  $L/n$ . Therefore, in the case where *n* is large enough, one iteration would already give us the error estimate:  $|Y_{t_i}^n - X^1| \leq \frac{LR}{n^2}$ , producing a good approximate solution of equation (7). Consequently, the explicit numerical scheme is given by

$$\begin{cases}\n\hat{Y}_{T}^{n} = \xi^{n}; \hat{Z}_{T}^{n} = 0 \\
X_{t_{i}}^{n} = \mathbb{E} \left\{ \hat{Y}_{t_{i+1}} \middle| \mathcal{G}_{i}^{n} \right\} \\
\hat{Y}_{t_{i}}^{n} = X_{t_{i}}^{n} + \frac{1}{n} f(X_{t_{i}}^{n}) \\
\hat{Z}_{t_{i}}^{n} = \mathbb{E} \left\{ \left[ \hat{Y}_{t_{i+1}} + \frac{1}{n} f(\hat{Y}_{t_{i}}^{n}) - \hat{Y}_{t_{i}}^{n} \right] (\triangle W_{t_{i+1}}^{n})^{-1} \middle| \mathcal{G}_{i}^{n} \right\} \n\end{cases} \n$$
(9)

The convergence of  $\hat{Y}^n$  to Y is proved in the sense of the Skorohod topology in [9, 26]. In [11], the convergence of the sequence  $Y^n$  is established using the tool of convergence of filtrations. See also [3] for the case where  $f$  depends on both variables  $y$  and  $z$ .

## **Application to European Options**

In the Black-Scholes model (see Black-Scholes Formula)

$$dS_t = \mu S_t dt + \sigma S_t dB_t \tag{10}$$

which is the continuous version of

$$\frac{S_{t+\Delta t} - S_t}{S_t} \approx \mu \Delta t + \sigma \Delta B_t \tag{11}$$

where the relative return has linear growth plus a random perturbation.  $\sigma$  is called the *volatility* and it is a measure of uncertainty. In this particular case,  $S$ has an explicit solution given by the Doleans-Dade exponential

$$S_t = S_0 e^{(\mu - \frac{1}{2}\sigma^2 t) + \sigma B_t}$$
(12)

We assume the existence of a riskless asset whose evolution is given by  $\beta_t = \beta_0 e^{rt}$ , where r is a constant interest rate. Then  $\beta$  satisfies the ODE:

$$\beta_t = \beta_0 + r \int_0^t \beta_s \, \mathrm{d}s \tag{13}$$

A portfolio is a pair of adapted processes  $(a_t, b_t)$ that represent the amount of investment in both assets at time  $t$  (both can be positive or negative). The wealth process is then given by

$$Y_t = a_t S_t + b_t \beta_t \tag{14}$$

We assume  $Y$  is self-financing:

$$dY_t = a_t dS_t + b_t d\beta_t \tag{15}$$

A call option gives the holder the right to buy an agreed quantity of a particular commodity  $S$  at a certain time (the expiration date,  $T$ ) for a certain price (the strike price  $K$ ). The holder has to pay a fee (called a premium  $q$ ) for this right. If the option can be exercised only at  $T$ , the option is called *European*. If it can be exercised at any time before  $T$ , it is called *American.* The main question is, what is the right price for an option? Mathematically,  $q$  is determined by the existence of a replication strategy with the initial value  $q$  and final value  $(S_T - K)^+$ ; that is, find  $(a_t, b_t)$  such that

$$Y_t = a_t S_t + b_t \beta_t \quad Y_T = (S_T - K)^+ \quad Y_0 = q \quad (16)$$

We look for a solution to this problem of the form  $Y_t = w(t, S_t)$  with  $w(T, x) = (x - K)^+$ . Using Itô's formula, we get

$$Y_{t} = Y_{0} + \int_{0}^{t} \frac{\partial w}{\partial x} dS_{s} + \int_{0}^{t} \frac{\partial^{2} w}{\partial x^{2}} d[S, S]_{s}$$
  
+ 
$$\int_{0}^{t} \frac{\partial w}{\partial t} ds = Y_{0} + \int_{0}^{t} \frac{\partial w}{\partial x} \{ \mu S_{s} ds + \sigma S_{s} dB_{s} \}$$
  
+ 
$$\int_{0}^{t} \frac{1}{2} \frac{\partial^{2} w}{\partial x^{2}} \sigma^{2} S_{s}^{2} ds$$
  
+ 
$$\int_{0}^{t} \frac{\partial w}{\partial t} ds = Y_{0} + \int_{0}^{t} \frac{\partial w}{\partial x} \sigma S_{s} dB_{s}$$
  
+ 
$$\int_{0}^{t} \left( \frac{1}{2} \frac{\partial^{2} w}{\partial x^{2}} \sigma^{2} S_{s}^{2} + \mu S_{s} \frac{\partial w}{\partial x} + \frac{\partial w}{\partial t} \right) ds \quad (17)$$

Using the self-financing property, we obtain

$$Y_t = Y_0 + \int_0^t a_s \mathrm{d}S_s + \int_0^t b_s \mathrm{d}\beta_s = Y_0 + \int_0^t a_s \left\{ \mu S_s \, \mathrm{d}s \right\}$$
$$+ \sigma S_s \mathrm{d}B_s \right\} + \int_0^t b_s \mathrm{d}\beta_s = Y_0 + \int_0^t a_s \sigma S_s \, \mathrm{d}B_s$$

$$+\int_{0}^{t}\left(rb_{s}\beta_{s}+a_{s}\mu S_{s}\right)\mathrm{d}s\tag{18}$$

Using the uniqueness in the predictable representation property for Brownian motion (see **Martingale Representation Theorem**), we obtain that

$$a_{s}\sigma S_{s} = \sigma S_{s}\frac{\partial w}{\partial x}$$
  
$$rb_{s}\beta_{s} + a_{s}\mu S_{s} = \frac{1}{2}\sigma^{2}S_{s}^{2}\frac{\partial^{2}w}{\partial x^{2}} + \mu S_{s}\frac{\partial w}{\partial x} + \frac{\partial w}{\partial t}$$
  
$$a_{s} = \frac{\partial w}{\partial x}(s, S_{s})$$
  
$$b_{s} = \frac{Y_{s} - a_{s}S_{s}}{\beta_{s}}$$
 (19)

Since  $r \frac{(Y_s - a_s S_s)}{\beta_s} \beta_s + a_s \mu S_s = \frac{1}{2} \sigma^2 S_s^2 \frac{\partial^2 w}{\partial x^2} + \mu S_s \frac{\partial w}{\partial x} + \frac{\partial w}{\partial t}$ , the equation for  $w$  is

$$r\frac{\partial w}{\partial t} + \frac{1}{2}\sigma^2 x^2 \frac{\partial^2 w}{\partial x^2} = -rx\frac{\partial w}{\partial x} + rw$$
$$w(T, x) = (x - K)^+ \tag{20}$$

The solution of this PDE is related to a BSDE, which we deduce now. Let us start again from the self-financing assumption

$$(S_{T} - K)^{+} = Y_{T} = Y_{t} + \int_{t}^{T} \frac{\partial w}{\partial x} dS_{s}$$
  
+ 
$$\int_{t}^{T} r \left( Y_{s} - S_{s} \frac{\partial w}{\partial x} \right) ds = Y_{t}$$
  
+ 
$$\int_{t}^{T} \sigma S_{s} \frac{\partial w}{\partial x} dB_{s}$$
  
+ 
$$\int_{t}^{T} \left( rY_{s} + (\mu - r)S_{s} \frac{\partial w}{\partial x} \right) ds$$
  
(21)

from which we deduce

$$Y_t = \xi + \int_t^T (\alpha Z_s - rY_s) \mathrm{d}s - \int_t^T Z_s \mathrm{d}B_s \qquad (22)$$

with  $\alpha = \frac{r-\mu}{\sigma}$ ,  $\xi = (S_0 e^{(\mu-\frac{1}{2}\sigma^2T)+\sigma B_T} - K)^+$ , and  $Z_s = \sigma S_s \frac{\partial w}{\partial r}$ . In this case, we have an explicit solution for  $w$  given by

$$Y_0 = S_0 \Phi(g(T, S_0)) - K e^{-rT} \Phi(h(T, S_0))$$
(23)

$$w(t,x) = x\Phi(g(T-t,x))$$
$$-Ke^{-r(T-t)}\Phi(h(T-t,x)) \tag{24}$$

where  $g(t, x) = \frac{\ln(x/K) + (r+1/2\sigma^2)t}{\sigma\sqrt{t}}, h(t, x) = g(t, x) \sigma\sqrt{t}$  and  $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{\frac{-y^2}{2}} dy$  is the standard normal distribution. In general, for example, when  $\sigma$  may depend on time and  $(S_t)$ , we obtain a BSDE for  $(Y_t)$  coupled with a forward equation for  $(S_t)$ , that can be solved numerically.

## **Numerical Methods for RBSDEs**

In this section, we are interested in the numerical approximation of BSDEs with reflection (in short, RBSDEs). We present here the case of one lower barrier, which we assume is an Itô process (a sum of a Brownian martingale and a continuous finite variation process).

$$Y_{t} = \xi + \int_{t}^{T} f(s, Y_{s}, Z_{s}) \mathrm{d}s$$
$$- \int_{t}^{T} Z_{s} \mathrm{d}B_{s} + K_{T} - K_{t} \quad 0 \le t \le T \qquad (25)$$

$$Y_t \ge L_t, \quad 0 \le t \le T, \quad \text{and} \quad \int_0^T \left(Y_t - L_t\right) \mathrm{d}K_t = 0 \tag{26}$$

where, as before,  $f$  is the generator,  $\xi$  is the terminal condition, and  $L = (L_t)$  is the reflecting barrier. Under the Lipschitz assumption of  $f$  (see  $[14]$  and for generalizations see  $[12, 21, 32]$ ) there is a unique solution  $(Y, Z, K)$  of adapted processes, with the condition that  $K$  is increasing and minimal in the sense that it is supported at the times  $Y$  touches the boundary.

The numerical scheme for RBSDEs that we present here is based on a penalization of equation (26) [14] coupled with a use of the standard Euler scheme. The penalization equation is given by

$$Y_t^{\varepsilon} = \xi + \int_t^1 f(s, Y_s^{\varepsilon}, Z_s^{\varepsilon}) \mathrm{d}s$$
$$- \int_t^1 Z_s^{\varepsilon} \mathrm{d}B_s + \frac{1}{\varepsilon} \int_t^1 (L_s - Y_s^{\varepsilon})^+ \mathrm{d}s \tag{27}$$

In this framework, we define

$$K_t^{\varepsilon} := \frac{1}{\varepsilon} \int_0^t (L_s - Y_s^{\varepsilon})^+ \mathrm{d}s, \quad 0 \le t \le 1 \qquad (28)$$

where  $\varepsilon$  is the penalization parameter. In order to have an explicit iteration, we include an extra Picard iteration, and the numerical procedure is then

$$Y_{t_{i}}^{\varepsilon,p+1,n} = Y_{t_{i+1}}^{\varepsilon,p+1,n} + \frac{1}{n}f(t_{i}, Y_{t_{i}}^{\varepsilon,p,n}, Z_{t_{i}}^{\varepsilon,p,n}) + \frac{1}{n\varepsilon}(L_{t_{i}} - Y_{t_{i}}^{\varepsilon,p,n})^{+} - \frac{1}{\sqrt{n}}Z_{t_{i}}^{\varepsilon,p+1,n}\zeta_{i+1}$$
(29)

$$K_{t_{i+1}}^{\varepsilon, p+1, n} - K_{t_i}^{\varepsilon, p+1, n} := \frac{1}{n\varepsilon} \left( S - \ddot{Y}_{t_i}^{\varepsilon, p+1, n} \right)$$
  
for  $i \in \{n-1, \dots, 0\}$  (30)

**Theorem 1** Under the assumptions

- **A1.**  $f$  is Lipschitz continuous and bounded;
- **A2.** L is assumed to be an Itô process;

**A3.** 
$$\lim_{n \to +\infty} \mathbb{E} \left[ \sup_{s \in [0,T]} \left| \mathbb{E}[\xi | \mathcal{F}_s] - \mathbb{E}[\xi^n | \mathcal{G}_{c_n(s)}^n] \right| \right] = 0$$

٦

the triplet  $(\xi^n, Y^{\varepsilon,p,n}, Z^{\varepsilon,p,n}, K^{\varepsilon,p,n})$  converges in the Skorohod topology toward the solution  $(\xi, Y, Z, K)$ of the RBSDE (26) (the order is first  $p \rightarrow \infty$ , then  $n \to \infty$  and finally  $\varepsilon \to 0$ ).

## A Procedure Based on Ma and Zhang's Method

We now introduce a numerical scheme based on a suggestion given in [29]. The new ingredient is to use a standard BSDE with no reflection and then

impose in the final condition of every step of the discretization that the solution must be above the barrier. Schematically we have

- $\bullet \quad Y_1^n := \xi^n$
- for  $i=n, n-1, \ldots 1$  let  $\left(\tilde{Y}^n, Z^n\right)$  be the solution of the BSDE:

$$\tilde{Y}_{t_{i+1}}^n = Y_{t_i}^n + \frac{1}{n} f(s, \tilde{Y}_s^n, Z_s^n) - Z_s^n (W_{t_{i+1}}^n - W_{t_i}^n)$$
(31)

 $\bullet \quad \text{define } Y^n_{t_{i+1}} = \tilde{Y}^n_{t_{i+1}} \vee L_{t_{i+1}}$ 

• let 
$$K_0^n = 0$$
 and define  $K_{t_i}^n := \sum_{j=1}^l (Y_{t_{j-1}}^n - \tilde{Y}_{t_{j-1}}^n)$ 

Clearly  $K^n$  is predictable and we have

$$Y_{t_{i-1}}^{n} = Y_{t_{i}}^{n} + \int_{t_{i-1}}^{t_{i}} f\left(s, \tilde{Y}_{s}^{n}, Z_{s}^{n}\right) ds$$
$$- \int_{t_{i-1}}^{t_{i}} Z_{s}^{n} dW_{s}^{n} + K_{t_{i}}^{n} - K_{t_{i-1}}^{n} \qquad (32)$$

**Theorem 2** Under the assumptions A1, A2 of Theorem 1 and

$$\lim_{n \to +\infty} \mathbb{E} \left[ \sup_{s \in [0,T]} \left| \mathbb{E}[\xi | \mathcal{F}_s] - \mathbb{E}[\xi^n | \mathcal{G}_{c_n(s)}^n] \right| \right]^2 = 0 \tag{33}$$

![](_page_4_Figure_11.jpeg)

**Figure 1** Binomial tree for six time steps,  $r = 0.06$ ,  $\sigma = 0.4$ , and  $T = 0.5$ 

we have

$$\lim_{n \to \infty} \mathit{I\!E} \left[ \sup_{0 \le i \le n} \left| Y_{t_i} - Y_{t_i}^n \right|^2 + \int_0^1 \left| Z_t - Z_t^n \right|^2 \mathrm{d}t \right] = 0 \tag{34}$$

#### Application to American Options

An American option (see **American Options**) is one that can be exercised at any time between the purchase date and the expiration date  $T$ , which we assume is nonrandom and for the sake of simplicity we take  $T = 1$ . This situation is more general than the European-style option, which can only be exercised on the date of expiration. Since an American option provides an investor with a greater degree of flexibility, the premium for this option should be higher than the premium for a European-style option.

We consider a financial market described by a filtered probability space  $(\Omega, \mathcal{F}, \mathcal{F}_{0 \le t \le T}, \mathbb{P})$ . As above, we consider the following adapted processes: the price of the risk asset  $S = (S_t)_{0 \le t \le T}$  and the wealth process  $Y = (Y_t)_{0 \le t \le T}$ . We assume that the rate interest r is constant. The aim is to obtain  $Y_0$ , the value of the American Option.

We assume that there exists a risk-neutral measure (see Equivalent Martingale Measures) allowing one to compute prices of all contingent claims as the expected value of their discounted cash flows. The equation that describes the evolution of  $Y$  is given by a linear reflected BSDE coupled with the forward equation for  $S$ .

$$Y_t = (K - S_1)^+ - \int_t^1 (rY_s + (\mu - r)Z_s) \, \mathrm{d}s$$

$$+ K_1 - K_t - \int_t Z_s \mathrm{d}B_s \tag{35}$$

$$S_t = S_0 + \int_0^t \mu S_s \mathrm{d}s + \int_0^t \sigma S_s \mathrm{d}B_s \tag{36}$$

The increasing process  $K$  keeps the process  $Y$ above the barrier  $L_t = (S_t - K)^+$  (for a call option) in a minimal way, that is,  $Y_t \ge L_t$ ,  $dK_t \ge 0$ , and

$$\int_0^1 (Y_t - L_t) \mathrm{d}K_t = 0 \tag{37}$$

**Table 1** Numerical scheme for an American option with 18 steps,  $K = 100$ ,  $r = 0.06$ ,  $\sigma = 0.4$ , and  $T = 0.5$ , and different values of  $S_0$ 

| n           | $S_0 = 80$ | $S_0 = 100$ | $S_0 = 120$ |
|-------------|------------|-------------|-------------|
|             | 20         | 11.2773     | 4.1187      |
| 2           | 22.1952    | 10.0171     | 3.8841      |
| 3           | 21.8707    | 10.7979     | 3.1489      |
| 4           | 22.8245    | 10.1496     | 3.9042      |
|             |            |             |             |
| 15          | 22.6775    | 10.8116     | 3.7119      |
| 16          | 22.6068    | 10.6171     | 3.6070      |
| 17          | 22.7144    | 10.7798     | 3.6811      |
| 18          | 22.6271    | 10.6125     | 3.6364      |
| Real values | 21.6059    | 9.9458      | 4.0611      |

The exercise random time is given by the following stopping time  $\tau = \inf\{t : Y_t - L_t < 0\}$  that represents the exit time from the market for the investor. As usual, we take  $\tau = 1$  if Y never touches the boundary L. At  $\tau$  the investor will buy the stock if  $\tau < 1$ , otherwise he/she does not exercise the option. In this problem, we are interested in finding  $Y_t$ ,  $Z_t$ , and  $\tau$ .

In Table 1 and Figure 1, we summarize the results of a simulation for the American option.

#### Acknowledgments

Jaime San Martín's research is supported by Nucleus Millennium Information and Randomness P04-069-F and BASAL project. Soledad Torres' research is supported by PBCT-ACT 13 Stochastic Analysis Laboratory, Chile.

## References

- Antonelli, F. (1996). Stability of backward stochastic [1] differential equations, Stochastic Processes and Their Applications  $62(1)$ , 103–114.
- Antonelli, F. & Kohatsu-Higa, A. (2000). Filtration [2] stability of backward SDE's, Stochastic Analysis and *Applications*  $18(1)$ , 11–37.
- Bally, V. (1997). Approximation Scheme for Solutions [3] of BSDE. Backward Stochastic Differential Equations. (Paris, 1995-1996), Pitman Research Notes Mathematics Series, Longman, Harlow, Vol. 364, pp. 177-191.
- [4] Bally, V. & Pagès, G. (2003). A quantization algorithm for solving multi-dimensional discrete-time optimal stopping problems, *Bernoulli* **9**(6), 1003–1049.
- [5] Bally, V., Pagès, G. & Printems, J. (2001). A Stochastic Quantization Method for Nonlinear Problems. Monte
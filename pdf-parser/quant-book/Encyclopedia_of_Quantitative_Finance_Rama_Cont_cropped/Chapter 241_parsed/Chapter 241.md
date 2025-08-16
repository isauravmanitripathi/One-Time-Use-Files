# **Partial Differential Equations**

In their seminal 1973 article [3], Black and Scholes derived a partial differential equation (PDE) for the call option price by considering a portfolio containing the option and the underlying asset and using absence of arbitrage arguments. Later, in the 1980s, Harrison, Kreps, and Pliska [10, 11] pioneered the use of stochastic calculus in mathematical finance and introduced martingale methods for option pricing in continuous time. This article is an overview of various contexts in finance where PDEs arise, in particular, for option pricing, portfolio optimization, and calibration. The PDE approach of Black-Scholes and the martingale method are related through the Feynman-Kac formula (see Markov Processes).

First, we recall the basic derivation of the Black-Scholes PDE and then present the PDEs for various exotic options and, in particular, American options. A paragraph is devoted to Hamilton-Jacobi-Bellman (HJB) equations, which are nonlinear PDEs arising from stochastic control and portfolio optimization. Finally, we discuss some PDEs associated with calibration problems. Computational aspects are treated in companion entries (see **Finite** Difference Methods for Barrier Options; Finite Difference Methods for Early Exercise Options; Finite Element Methods).

## The Black-Scholes PDE

We recall the original arguments in the derivation of the Black-Scholes PDE for option pricing [3, 14]. In the Black-Scholes model, we consider a market with a risk-free bond of constant interest rate  $r$ , and a stock with a price process  $S$  evolving according to a geometric Brownian motion:

$$dS_t = bS_t dt + \sigma S_t dW_t \tag{1}$$

where the drift rate b and the volatility  $\sigma > 0$  are assumed to be constant and  $W$  is a standard Brownian motion. We now consider a European call option, characterized by its payoff  $(S_T - K)_+$  at the maturity  $T$ , and with strike  $K$ . We denote by  $V$  the value of the call option:  $V = V(t, S_t)$  is a function of the spot price of the underlying asset  $S_t$  at time t. At the expiry date of the option, we have  $V(T, S_T) = (S_T - K)_+$ , and for  $t < T$ , by assuming that the function V is smooth, we get by Itô's formula

$$\begin{split} \mathrm{d}V &= \frac{\partial V}{\partial t} \,\mathrm{d}t + \frac{\partial V}{\partial S} \,\mathrm{d}S + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \,\mathrm{d}t \\ &= \left(\frac{\partial V}{\partial t} + bS \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) \,\mathrm{d}t \\ &+ \sigma S \frac{\partial V}{\partial S} \,\mathrm{d}W \end{split} \tag{2}$$

Now consider a portfolio consisting of the option and a short position  $\Delta$  in the asset: the portfolio value is then equal to  $\Pi = V - \Delta S$ , and its self-financed dynamics is given by

$$\begin{split} \mathrm{d}\Pi &= \mathrm{d}V - \Delta \,\mathrm{d}S \\ &= \left(\frac{\partial V}{\partial t} + bS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \Delta bS\right) \,\mathrm{d}t \\ &+ \sigma S \left(\frac{\partial V}{\partial S} - \Delta\right) \,\mathrm{d}W \end{split} \tag{3}$$

The random component in the evolution of the portfolio  $\Pi$  may be eliminated by choosing

$$\Delta = \frac{\partial V}{\partial S} \tag{4}$$

This results in a portfolio with deterministic increment:

$$d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt \tag{5}$$

Now, by arbitrage-free arguments, the rate of return of the riskless portfolio  $\Pi$  must be equal to the interest rate  $r$  of the bond, that is,

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r\,\Pi\tag{6}$$

and recalling that  $\Pi = V - (\partial V/\partial S)S$ , this leads to the *Black–Scholes partial differential equation*:

$$rV - \frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = 0 \qquad (7)$$

This PDE together with the terminal condition  $V(T, S) = (S - K)_{+}$  is a linear parabolic Cauchy

problem, whose solution is analytically known, and this is the celebrated Black-Scholes formula. Moreover, this formula can also be computed as an expectation:

$$V(t, S) = \mathbb{E}^{\mathbb{Q}} \left[ e^{-r(T-t)} (S_T - K)_+ \middle| S_t = S \right] \quad (8)$$

where  $\mathbb{E}^{\mathbb{Q}}$  denotes the expectation under which the drift rate  $b$  in equation (1) is replaced by the interest rate r.  $\mathbb{Q}$  is called *risk-neutral probability*.

## **Linear PDEs for European Options**

The derivation presented in the previous paragraph is prototypical. Besides the absence of arbitrage argument, the key points for the derivation of the PDE satisfied by the option price is the Markov property of the stochastic processes describing the market factors. The relation with risk-neutral probability is achieved through the Feynman-Kac formula (see Markov **Processes**). In its basic (multidimensional) version, the Feynman-Kac representation is formulated as follows: let us consider the stochastic differential equation on  $\mathbb{R}^n$ 

$$dX_s = b(X_s) ds + \sigma(X_s) dW_s \tag{9}$$

where  $b$  and  $\sigma$  are measurable functions valued, respectively, on  $\mathbb{R}^n$  and  $\mathbb{R}^{n \times d}$ , and W is a  $n$ -dimensional Brownian motion. Consider the Cauchy problem

$$rv - \frac{\partial v}{\partial t} - b(x)D_x v - \frac{1}{2}\text{tr}(\sigma\sigma'(t,x)D_x^2 v) = 0$$
  
on  $[0,T) \times \mathbb{R}^n$  (10)

$$v(T, x) = g(x) \quad \text{on } \mathbb{R}^n \tag{11}$$

Here,  $D_x v$  is the gradient,  $D_x^2 v$  is the Hessian matrix of v, with respect to the x variable,  $\sigma'$  is the transpose of  $\sigma$ , and tr denotes the trace of a matrix. Then, the solution to this Cauchy problem may be represented as

$$v(t,x) = \mathbb{E}\left[e^{-\int_t^T r(u, X_u^{t,x}) \mathrm{d}s} g(X_T^{t,x})\right] \tag{12}$$

where  $X_s^{t,x}$  is the solution to equation (9) starting from x at  $s = t$ . The Feynman-Kac formula is a

probabilistic interpretation of the integral representation of the solution using the *Green's function*, which is in this case the density of the underlying asset. The Black-Scholes price is a particular case with r constant,  $b(t, x) = rx$ ,  $\sigma(t, x) = \sigma x$ , and  $g(x) =$  $(x - K)_{\perp}$ . More generally, the interest rate r and the volatility  $\sigma$  may depend on time and spot price.

In the general case, we do not have analytical expression for  $v$ , and we have to resort to numerical methods for option pricing. The probabilistic representation  $(12)$  is the basis for Monte Carlo methods in option pricing while deterministic numerical methods (finite differences and finite elements) are based on the PDE (11).

## Barrier Options

The payoff of these options depends on the fact that the underlying asset crossed or not, some given barriers during the time interval  $[0, T]$  (see **Barrier Options**). For example, a down-and-out call option has a payoff  $(S_T - K)_+ 1_{\inf_{t \in [0,T]} S_t > L}$ . Its price  $v(t, x)$ at time t for a spot price  $S_t = x$ , satisfies the boundary value problem:

$$rv - \frac{\partial v}{\partial t} - rx \frac{\partial v}{\partial x} - \frac{1}{2} \sigma^2 x^2 \frac{\partial^2 v}{\partial x^2} = 0,$$
  

$$(t, x) \in [0, T) \times (L, \infty)$$
  

$$v(t, L) = 0$$
  

$$v(T, x) = (x - K)_+$$
  
(13)

## Lookback Options

The payoff of these options involve the maximum or minimum of the underlying asset (see **Lookback Options**). For instance, the floating strike lookback put option pays at maturity  $M_T - S_T$  where  $M_t =$  $\sup_{0 \le t \le T} S_t$ . The pair  $(S_t, M_t)$  is a Markov process, and the price at time  $t$  of this lookback option is equal to  $v(t, S_t, M_t)$  where the function v is defined for  $t \in [0, T], (S, M) \in \{(S, M) \in \mathbb{R}^2 : 0 <$  $S \leq M$ , and satisfies the Neumann problem:

$$rv - \frac{\partial v}{\partial t} - rS\frac{\partial v}{\partial S} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 v}{\partial S^2} = 0$$
$$\frac{\partial v}{\partial M}(t, M, M) = 0$$
$$v(T, S, M) = M - S \qquad (14)$$

## Asian Options

These options involve the average of the risky asset (see Asian Options). For example, the payoff of an Asian call option is  $(A_T - K)_+$  where  $A_t =$  $\frac{1}{t} \int_0^t S_u \, \mathrm{d}u$ . The pair  $(S_t, A_t)$  is a Markov process, and the price at time  $t$  of this Asian option is equal to  $v(t, S_t, A_t)$  where the function v is defined for  $t \in [0, T], (S, A) \in \mathbb{R}^2_+,$  and satisfies the Cauchy problem (see, e.g., [16]):

$$rv - \frac{\partial v}{\partial t} - rS\frac{\partial v}{\partial S} - \frac{1}{t}(S - A)\frac{\partial v}{\partial A}$$
$$-\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 v}{\partial S^2} = 0$$
$$v(T, S, A) = (A - K)_+ \tag{15}$$

# **American Options and Free Boundary** Problems

With respect to European options presented so far, American options give the holder the right to exercise his/her right at any time up to maturity (see American Options). For an American put option of payoff  $(K - S_t)_+, 0 \le t \le T$ , its price at time t and for a spot stock price  $S_t = x$  is given by

$$v(t,x) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}} \left[ e^{-r(\tau - t)} (K - S_{\tau})_{+} \middle| S_{t} = x \right]$$
(16)

where  $\mathcal{T}_{t,T}$  denotes the set of stopping times valued in  $[t, T]$ . In terms of PDE, and within the Black-Scholes framework, this leads via the dynamic programming principle (see  $[7]$ ) to a variational inequality:

$$\min \left[ rv - \frac{\partial v}{\partial t} - rx \frac{\partial v}{\partial x} - \frac{1}{2} \sigma^2 x^2 \frac{\partial^2 v}{\partial x^2}, \right.$$
$$\left. v(t, x) - (K - x)_+ \right] = 0 \tag{17}$$

together with the terminal condition:  $v(T, x) = (K (x)_{+}$ . This variational inequality maybe written equivalently as

$$rv - \frac{\partial v}{\partial t} - rx\frac{\partial v}{\partial x} - \frac{1}{2}\sigma^2 x^2 \frac{\partial^2 v}{\partial x^2} \ge 0 \tag{18}$$

which corresponds to the supermartingale property of the discounted price process  $e^{-rt}v(t, S_t)$ 

$$v(t,x) \ge (K - x)_{+} \tag{19}$$

which results directly from the fact that by exercising his/her right immediately, one receives the option payoff, and

$$rv - \frac{\partial v}{\partial t} - rx \frac{\partial v}{\partial x} - \frac{1}{2}\sigma^2 x^2 \frac{\partial^2 v}{\partial x^2} = 0,$$
  
for  $(t, x) \in \mathcal{C} = \{v(t, x) > (K - x)_+\}$  (20)

which means that as long as we are in the continuation region  $C$ , that is, the value of the American option price is strictly greater than its payoff, the holder does not exercise his/her right early. The formulation  $(18-20)$  is also called a *free-boundary problem*, and in the case of the American put, there is an increasing function  $x^*(t)$ , the free-boundary or critical price, which is smaller than  $K$ , and such that  $C = \{(t, x) : x > x^*(t)\}$ . This free boundary is an unknown part of the PDE and separates the continuation region from the exercise region where the option is exercised, that is,  $v(t, x) = (K - x)_{+}$ . The above conditions do not determine the unknown free boundary  $x^*(t)$ . An additional condition is required, which is the continuous differentiability of the option price across the boundary  $x^*(t)$ :

$$v(t, x^*(t)) = K - x^*(t), \quad \frac{\partial v}{\partial x}(t, x^*(t)) = -1$$
(21)

This general property is known in optimal stopping theory as the *smooth fit principle*. However, the American option price  $v$  is not  $C^2$ , and the nonlinear PDE (17) should be interpreted in a weak sense by means of distributions (see [2] or [12]), or in the viscosity sense (see [5]). Notice that the main difference between PDE for American options and European options is the nonlinearity of the equation in the former case. This makes the theory and the numerical implementation more difficult than for the European options.

#### **Stochastic Control and Bellman Equations**

Stochastic control problems arise in continuous-time portfolio management. This may be formulated in a roughly general framework as follows: we consider a controlled diffusion process in the form

$$dX_s = b(X_s, \alpha_s) ds + \sigma(X_s, \alpha_s) dW_s, \quad \text{in } \mathbb{R}^n$$
(22)

where  $W$  is a  $d$ -dimensional Brownian motion on some filtered probability space  $(\Omega, \mathcal{F}, \mathbb{F} = (\mathcal{F}_t), \mathbb{P}),$ and  $\alpha = (\alpha_t)$  is an adapted process valued in a Borel set  $A \subset \mathbb{R}^m$ , the so-called control process, which influences the dynamics of the state process  $X$  through the drift coefficient  $b$  and the diffusion coefficient  $\sigma$ . A stochastic control problem (in a finite horizon) consists of maximizing over the control processes a functional objective in the form

$$\mathbb{E}\left[\int_{0}^{\mathrm{T}}f(X_{t},\alpha_{t})\,\mathrm{d}t + g(X_{T})\right] \tag{23}$$

where  $f$  and  $g$  are real-valued measurable functions. The method used to solve this problem, and initiated by Richard Bellman in the 1950s, is to introduce the value function  $v(t, x)$ , that is the maximum of the objective when starting from state  $x$  at time  $t$ , and to apply the dynamic programming principle (DPP). The DPP formally states that if a control is optimal from time  $t$  until  $T$ , then it is also optimal from time  $t + h$  until T for any  $t + h > t$ . Mathematically, the DPP relates the value functions at two different dates t and  $t + h$ , and by studying the behavior of the value functions when  $h$  tends to zero, one obtains a PDE satisfied by  $v$ , the so-called Hamilton-Jacobi-Bellman equation:

$$-\frac{\partial v}{\partial t} - \sup_{a \in A} \left[ b(x,a) D_x v + \frac{1}{2} \text{tr}(\sigma \sigma'(x,a) D_x^2 v) + f(x,a) \right] = 0, \quad \text{on } [0,T) \times \mathbb{R}^n \tag{24}$$

together with the terminal condition  $v(T, x) = g(x)$ . Here, and in the sequel, the prime symbol "" is

for the transpose. The most famous application of Bellman equation in finance is the portfolio selection of Merton [13]. In this problem, an investor can choose to invest at any time between a riskless bond of interest rate  $r$  or a stock with Black-Scholes dynamics of rate of return  $\beta$  and volatility  $\nu$ . By denoting  $\alpha_t$ , the proportion of wealth  $X_t$  invested in the stock, this corresponds to a controlled wealth process X in equation (22) with  $b(x, a) = ax(\beta - r) +$ rx and  $\sigma(x, a) = ax\gamma$ . The objective of the investor is to maximize his/her expected utility from terminal wealth, which corresponds to a functional objective of the form (23) with  $f = 0$ , and g an increasing, concave function. A usual choice of utility function is  $g(x) = x^p$ , with  $0 < p < 1$ , in which case, there is an explicit solution to the corresponding HJB equation  $(24)$ . Moreover, the optimal control attaining the argument maximum in equation  $(24)$  is a constant equal to  $b - r/(1-p)\gamma^2$ . In the general case, there is no explicit solution to the HJB equation. Moreover, the solution is not smooth  $C^2$  and one proves actually that the value function is characterized as the unique weak solution to the HJB equation in the viscosity sense. We refer to the books [9] and [15] for an overview of stochastic control and viscosity solutions in finance.

Related nonlinear PDEs also arise in the uncertain volatility model, where one computes the cost of (super)hedging an option when the volatility is only known to be inside a band (*see Uncertain Volatility* Model).

## **Diffusion Models and the Dupire PDE**

It is well known that the constant coefficient Black– Scholes model is not consistent with empirical observations in the markets. Indeed, given a call option with quoted price  $C_M$  on the market, one may associate the so-called *implied volatility*, that is, the volatility  $\sigma_{\text{imp}}$  such that the price given by the Black-Scholes formula coincides with  $C_M$ . If the Black-Scholes model was sharp, then the implied volatility would not depend on the strike and maturity of the option. However, it is often observed that the implied volatility is far from constant and is actually a convex function of the strike price, a phenomenon known as the volatility smile. Several extensions of the Black-Scholes model have been proposed in the literature. We focus here on local volatility models (see Local Volatility Model) where the volatility is a function  $\sigma(t, S_t)$  of time and the spot price. In this model, the price  $C(t, S_t)$  of a call option of strike K and maturity  $T$  satisfies the PDE:

$$rC - \frac{\partial C}{\partial t} - rS\frac{\partial C}{\partial S} - \frac{1}{2}\sigma^{2}(t, S)S^{2}\frac{\partial^{2} C}{\partial S^{2}} = 0,$$
  
$$(t, S) \in [0, T) \times (0, \infty)$$
  
$$C(T, S) = (S - K)_{+}$$
  
(25)

The calibration problem in this local volatility model consists of finding a function  $\sigma(t, S)$ , which reproduces the observed call option prices on the market for all strikes and maturities. In other words, we want to determine  $\sigma(t, S)$  in such a way that the prices computed, for example, with the above PDE coincide with the observed prices. The solution to this problem has been provided by Dupire [6]. By fixing the date  $t$  and the spot price  $S$ , and by denoting  $C(t, S, T, K)$  the call option price with strike K and maturity  $T > t$ , Dupire showed that it satisfies the forward (with initial condition) parabolic PDE:

$$\frac{\partial C}{\partial T} + rK \frac{\partial C}{\partial K} - \frac{1}{2}\sigma^2(T, K)K^2 \frac{\partial^2 C}{\partial K^2} = 0,$$
  
$$(T, K) \in [t, \infty) \times \mathbb{R}_+$$
 (26)

$$C(t, S, t, K) = (S - K)_{+}$$
(27)

This PDE may be obtained by at least two methods. The first one is based on Itô-Tanaka formula on the risk-neutral expectation representation of the call option price, while the second one is derived by PDE arguments based on the Fokker-Planck equation for the diffusion process  $(S_t)$  (see, e.g., [1]). The PDE (26) can be used, in principle, to compute the local volatility function from the call options prices observed at various strikes  $K$  and maturities  $T$ :

$$\sigma^{2}(T,K) = 2\frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{K^{2}\frac{\partial^{2}C}{\partial K^{2}}}$$
(28)

This is known as Dupire's formula (see Dupire Equation). Notice that equation (28) cannot be used directly since only a finite number of options are quoted on the market. We refer to [1] or [4] for a more advanced discussion of such PDEs.

# **Semilinear PDEs**

We have presented so far three types of PDE in finance: linear PDEs arising from European options and Feynman-Kac formulas, variational inequalities arising from American options and optimal stopping, and nonlinear HJB arising from stochastic control problems. Semilinear PDEs the form

$$-\frac{\partial v}{\partial t} - b(x)D_x v - \frac{1}{2}\text{tr}(\sigma\sigma'(x)D_x^2 v)$$
$$-f(x, v, D_x v'\sigma) = 0, \quad (t, x) \in [0, T) \times \mathbb{R}^n$$
$$v(T, x) = g(x), \quad x \in \mathbb{R}^n \tag{29}$$

Such PDEs arise, for instance, in finance in option pricing with large investor models or in indifference pricing (see **Expected Utility Maximization**). Backward stochastic differential equations [8] provide probabilistic approaches for solving such PDEs arising in finance (see Backward Stochastic Differential Equations).

## References

- [1] Achdou, Y. & Pironneau, O. (2005). Computational Methods for Option Pricing, Frontiers in Applied Mathematics. SIAM.
- [2] Bensoussan, A. & Lions, J.L. (1982). Applications of Variational Inequalities in Stochastic Control, North Holland, Amsterdam.
- [3] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, Journal of Political Economy, 81, 637-654.
- [4] Cont, R. & BenHamida, S. (2005). Recovering volatility from option prices by evolutionary optimization, Journal of Computational Finance  $\mathbf{8}(3)$ , 1–34.
- [5] Crandall, M., Ishii, H. & Lions, P.L. (1992). User's guide to viscosity solutions of second order partial differential equations, Bulletin of the American Mathematical Society 27, 1-167.
- Dupire, B. (1994). Pricing with a smile, Risk 7, 18-20. [6]
- El Karoui, N. (1981). Les aspects probabilistes du [7] contrôle stochastique, Lecture Notes in Mathematics 876, 73-238.
- [8] El Karoui, N., Peng, S. & Quenez, M.C. (1997). Backward stochastic differential equations in finance, Mathematical Finance,  $7, 1-71$ .
- [9] Fleming, W. & Soner, M. (1993). Controlled Markov Processes and Viscosity Solutions, Springer Verlag.
- [10] Harrison, M. & Kreps, D. (1979). Martingales and arbitrage in multiperiod securities markets, Journal of Economic Theory, 20, 381-408.

# **6 Partial Differential Equations**

- [11] Harrison, M. & Pliska, S. (1981). Martingales and Stochastic integrals in the theory of continuous trading, *Stochastic Processes and Applications*, **11**, 215–260.
- [12] Jaillet, P., Lamberton, D. & Lapeyre, B. (1990). Variational inequalities and the pricing of American options, *Acta Applicandae Mathematicae* **21**, 263–289.
- [13] Merton, R. (1973). Optimum consumption and portfolio rules in a continuous-time model, *Journal of Economic Theory* **3**, 373–413.
- [14] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science*, **4**(1), 141–183.
- [15] Pham, H. (2007). *Optimisation et contrˆole stochastique appliqu´es `a la finance*, Springer Verlag.
- [16] Rogers, C. & Shi, Z. (1995). The value of an Asian option, *Journal of Applied Probability*, **32**, 1077–1088.

HUYENˆ PHAM
# Cramér-Lundberg Estimates

Cramér-Lundberg estimates and bounds are used to estimate ruin probabilities of the surplus in an insurance risk model. The studies of insurance risk models can be dated back to 1909, when F. Lundberg presented his paper "On the theory of risk" at the Sixth International Congress of Actuaries (see [14]). In the paper, a shifted compound Poisson process was used to model the surplus of an insurance company. The model was further investigated by H. Cramér (see [2]). Because of the pioneering work of Lundberg and Cramér on the shifted compound Poisson model, the shifted compound Poisson model is often referred to as the Cramér-Lundberg risk model/process or the classical compound Poisson risk model these days. For a comprehensive coverage of insurance risk models, see Ruin Theory and **Insurance Risk Models.** 

In the Cramér-Lundberg risk model, the number of claims from an insurance portfolio of an insurance company follows a Poisson process  $N(t)$ (see **Poisson Process**) with intensity  $\lambda$ , the successive claim amounts  $X_n$ ,  $n = 1, 2, \ldots$ , are positive, independent, and identically distributed random variables with common distribution function  $P(x), x > 0$ , and they are assumed to be independent of the number of claims process  $N(t)$ . The aggregate claims from the insurance portfolio up to time t are thus given by  $S(t) = \sum_{n=1}^{N(t)} X_n$ ; this is a compound Poisson process with mean  $E\{S(t)\}=$  $\lambda t E(X)$  and variance  $Var\{S(t)\} = \lambda t E(X^2)$ , where  $X$  is a generic copy of  $X_n$ 's (see Accumulated Claims). Suppose that the company has initial surplus  $u > 0$  and receives premiums continuously at annual rate  $c$ . The company's surplus process is written as  $U(t) = u + ct - S(t)$ . In order to ensure that the premium incomes cover the insurance claims over time, it is generally assumed that  $c > \lambda E(X)$ . Let  $\theta = [c - E \{S(1)\}]/E \{S(1)\}$ . Then c may be written as  $c = (1 + \theta)\lambda E(X)$ . Thus,  $\theta$  is the risk premium for the expected claim of one monetary unit per unit time and is called the *relative security loading*.

Several quantities associated with the surplus process are of central interest. Among them are the first time that the surplus becomes negative or the company is insolvent  $T = \inf\{t; U(t) < 0\}$  and the probability that the ruin event occurs  $\psi(u) =$  $Pr\{T < \infty\}$ . Thanks to the independent increments property of the Poisson process, it can be shown that the probability of ruin  $\psi(u)$  satisfies the defective renewal equation

$$\psi(u) = \frac{1}{1+\theta} \int_0^u \psi(u-x) \, dP_e(x)$$
$$+ \frac{1}{1+\theta} [1 - P_e(u)] \tag{1}$$

where  $P_e(x)$  is the equilibrium distribution of  $P(x)$ and is given by

$$P_e(x) = \frac{\int_0^x [1 - P(y)] \, dy}{E(X)} \tag{2}$$

As the probability of ruin is the solution of the defective renewal equation (1), methods in renewal theory apply. The negative solution  $-\kappa$ , when it exists, of the following equation

$$\int_0^\infty e^{-zx} dP_e(x) = 1 + \theta \tag{3}$$

or its equivalent form

$$cz + \lambda \tilde{p}(z) - \lambda = 0 \tag{4}$$

where  $\tilde{p}(z)$  is the Laplace-Stieltjes transform of  $P(x)$ , plays a key role in the analysis of time-ofruin related quantities of the risk model. Equation (3) or (4) is referred to as the Cramér-Lundberg equation or condition, and  $\kappa$  the Lundberg adjustment coefficient. It is straightforward to show that the function  $e^{\kappa u}\psi(u)$  satisfies a proper renewal equation and thus the key renewal theorem applies. As a result, one has the Cramér-Lundberg estimate or approximation of ruin probabilities

$$\psi(u) \sim \frac{\theta E(X)}{E\left\{X e^{\kappa X}\right\} - (1+\theta)E(X)} e^{-\kappa u}, \text{ as } u \to \infty$$
(5)

Moreover, a simple exponential upper bound, called the *Lundberg Bound* or *Lundberg inequality*, is obtainable:

$$\psi(u) \le e^{-\kappa u}, \ u \ge 0 \tag{6}$$

The results  $(5)$  and  $(6)$  are two of the most celebrated results in ruin theory (*see Ruin Theory*).

#### **Expected Discounted Penalty Function**

Two other important quantities related to the time of ruin are the surplus immediately before ruin  $U(T-)$ and the deficit at ruin  $|U(T)|$ , where  $T-$  is the left limit of  $T$ . In the seminal paper [7], Gerber and Shiu introduced the expected discounted penalty function (see Gerber-Shiu Function) to provide a unified treatment of the time of ruin T, the surplus  $U(T-)$ and the deficit  $|U(T)|$ . The function is defined as

 $\Psi(u)$  $= E \left[ e^{-\delta T} w(U(T-), |U(T)|) \right] I(T < \infty) |U(0) = u$ (7)

where  $w(x, y)$  is the penalty for a surplus amount of  $x$  immediately before ruin and a deficit amount of  $y$  at ruin, and  $\delta$  is interpreted as either a force of interest or a Laplace transform variable. The probability of ruin  $\psi(u)$ , the joint distribution of  $U(T-)$  and  $|U(T)|$ , and more, are the special cases of the expected discounted penalty function. There have been many papers analyzing the expected discounted penalty function for various insurance risk models. It has been shown that the expected discounted penalty function  $\Psi(u)$  satisfies a defective renewal equation. As a result, a Cramér–Lundberg estimate for the expected discounted penalty function  $\Psi(u)$  is obtainable.

#### **Distributional Generalizations**

It is easy to verify that the solution of the defective renewal equation  $(1)$  is the (right) tail of a compound geometric distribution. Hence, the results for the probability of ruin may also apply to compound geometric distributions. If  $G(x)$  is the distribution function of a compound geometric distribution with geometric parameter  $\phi$  and the secondary distribution  $F_Y(x)$ , one has the Cramér–Lundberg estimate

$$1 - G(x) \sim Ce^{-\kappa x}, \ x \to \infty \tag{8}$$

with

$$C = \frac{1 - \phi}{\kappa \phi E \left\{ Y e^{\kappa Y} \right\}} \tag{9}$$

and the Lundberg inequality

$$1 - G(x) \le e^{-\kappa x}, \ x \ge 0 \tag{10}$$

where  $\kappa$  is the Lundberg adjustment coefficient when the equilibrium  $P_e(x)$  is replaced by  $F_Y(x)$ . Further generalizations include the refinements and generalizations of the exponential bound to new worse than used (NWU) bounds and distributional generalizations of the Cramér-Lundberg estimate and the Lundberg inequality to other compound distributions. See [4, 10] and [17], and references therein.

### **Further Extensions**

The Cramér–Lundberg risk model has been extended in several ways. Dufresne and Gerber [3] added a Brownian motion to the Cramér-Lundberg risk model:

$$U(t) = u + ct - S(t) + \sigma W(t) \tag{11}$$

where  $\{W(t)\}\$  is the standard Brownian motion. The additional diffusion term may be interpreted as the future uncertainty of the aggregate claims, the future uncertainty of the premium incomes, or the fluctuation of the investment of the surplus. In this situation, the expected discounted penalty function  $\Phi(u)$  satisfies the defective renewal equations. Thus, a Cramér–Lundberg estimate similar to equation (4) exists for  $\Phi(u)$  and the result can be found in [15].

The model (11) is a special case of Lévy processes (see Lévy Processes). A number of papers discuss the probability of ruin for this class of surplus processes. See [9, 11] and [18]. More recently, the expected discounted penalty function for general Lévy processes has been investigated in [5]. Generally, the results for Lévy surplus processes are very similar to those for the model  $(11)$ .

Another extension is to replace the Poisson process by a renewal process. The resulting risk model is often called the Sparre Andersen model as it was first investigated by Sparre Andersen [1]. In this case, the expected discounted penalty function defined by equation  $(7)$  still satisfies a defective renewal equation. The defective renewal equation structure implies that Lundberg estimates and bounds hold in this more general situation. For further discussion of these issues, see **Ruin Theory** [8, 12, 16], and references therein

# **Financial Applications**

The expected discounted penalty function can be used to price American perpetual options. Assume that the price of a risky asset follows a jumpdiffusion process under a risk-neutral probability measure: *A(t)* = *A(*0*)*exp{*ct* + *σW (t)* − *S(t)*}*, t* ≥ 0 where the components in this model are the same as those in equation (11) except that the choice of *c* is such that the present value process of *A(t)* is a martingale (*see* **Ito's Formula ˆ** ). Consider an American perpetual put option with time-*t* payoff max {*K* − *A(t),* 0}*,* where *K* is the strike price. The optimal exercise boundary is constant owing to the stationary and independent increment property of the process. Let *ϕ* be the constant and the time of exercise thus is

$$T = \inf\left\{t : A(t) < \varphi\right\} \tag{12}$$

If we define the initial surplus *u* = ln[*A(*0*)/ϕ*] and the penalty function *w(x, y)* = max *K* − *ϕ*e<sup>−</sup>*<sup>y</sup> ,* 0 , the exercise time *T* in equation (12) is the time of ruin for the model (11) and the price of the American perpetual put option is the same as the expected discounted penalty function for the model (11). See [6] for details. Further applications include the pricing of perpetual catastrophe equity put options. A catastrophe equity put option is an option contract that allows an insurer to issue a fixed number of convertible preferred shares at a predetermined price to the option writer, when the accumulated catastrophic loss amount of the insurer or a loss index exceeds a prespecified level. For details, see [13].

# **References**

- [1] Andersen, E.S. (1957). On the collective theory of risk in the case of contagion between claims, *Transactions XVth International Congress of Actuaries* **2**, 219–229.
- [2] Cramer, H. (1930). ´ *On the Mathematical Theory of Risk*, Skandia Jubilee Volume, Stockholm.
- [3] Dufresne, F. & Gerber, H. (1991). Risk theory for the compound Poisson process that is perturbed by diffusion, *Insurance: Mathematics and Economics* **12**, 9–22.
- [4] Embrechts, P., Maejima, M. & Teugels, J. (1985). Asymptotic behaviour of compound distributions, *ASTIN Bulletin* **15**, 45–48.
- [5] Garrido, J. & Morales, M. (2006). On the expected discounted penalty function for the Levy risk processes, *North American Actuarial Journal* **10**(4), 196–216.

- [6] Gerber, H. & Landry, B. (1998). On the discounted penalty at ruin in a jump-diffusion and the perpetual put option, *Insurance: Mathematics and Economics* **22**, 263–276.
- [7] Gerber, H. & Shiu, E.S.W. (1998). On the time value of ruin, *North American Actuarial Journal* **2**(1), 48–72, Discussions, 72–78.
- [8] Gerber, H.U. & Shiu, E.S.W. (2005). The time value of ruin in a Sparre Andersen model, *North American Actuarial Journal* **9**(2), 49–84.
- [9] Huzak, M., Perman, M., Sikic, H. & Vondracek, Z. (2004). Ruin probabilities and decompositions for general perturbed risk processes, *Annals of Applied Probability* **14**, 1378–1397.
- [10] Kalashnikov, V. (1997). *Geometric Sums: Bounds for Rare Events with Applications*, Kluwer Academic Publishers, Dordrecht.
- [11] Kluppelberg, C., Kyprianou, A.E. & Maller, R.A. ¨ (2004). Ruin probabilities and overshoots for general Levy insurance risk processes, *Annals of Applied Probability* **14**, 1766–1801.
- [12] Li, S. & Garrido, J. (2004). On ruin for the Erlang(n) risk process, *Insurance: Mathematics and Economics* **34**, 391–408.
- [13] Lin, X.S. & Wang, T. (2009). Pricing perpetual American catastrophe put options: a penalty function approach, *Insurance: Mathematics and Economics*, **44**, 287–295.
- [14] Lundberg, F. (1909). Uber die theorie der ruckversic- ¨ herung, *Transactions of VI International Congress of Actuaries* **1**, 877–948.
- [15] Tsai, C.C.-L. & Willmot, G.E. (2002). A generalized defective renewal equation for the surplus process perturbed by diffusion, *Insurance: Mathematics and Economics* **30**, 51–66.
- [16] Willmot, G.E. (2007). On the discounted penalty function in the renewal risk model with general interclaim times, *Insurance: Mathematics and Economics* **41**, 17–31.
- [17] Willmot, G.E. & Lin, X.S. (2001). *Lundberg Approximations for Compound Distributions with Insurance Applications*, Lecture Notes in Statistics 156, Springer-Verlag, New York.
- [18] Yang, H.L. & Zhang, L. (2001). Spectrally negative Levy ´ processes with applications in risk theory, *Advances in Applied Probability* **33**, 281–291.

# **Related Articles**

**American Options**; **Cramer's Theorem ´** ; **Insurance Derivatives**; **Insurance Risk Models**; **Levy ´ Processes**; **Large Deviations**; **Ruin Theory**.

X. SHELDON LIN
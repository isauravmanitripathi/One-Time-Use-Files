# Gerber-Shiu Function

Risk theory studies insurance risk models that describe the uncertainty associated with the claims recorded by an insurance company for the losses incurred by its policy holders. From premium and investment income, insurers set aside funds (surplus) to cover such losses. Ruin theory studies the fluctuations of these surplus processes. Classical problems include ruin (low) and dividend (high) barrier hitting times (see  $[5]$ ).

In the last decade, the expected discounted penalty function, proposed by Gerber and Shiu, has unified the treatment of the joint distribution of the time to ruin, the surplus just prior to ruin, and the deficit at ruin. This article centers on this expected discounted penalty function, commonly called the Gerber-Shiu  $(G-S)$  function in the actuarial literature.

The G-S function is somewhat akin to an expected discounted payoff function for financial instruments. A brief description of its general features is given here, together with references that discuss details, generalizations, and applications to insurance and finance.

# Introduction

Risk theory models describe the uncertainty associated with the claims recorded by an insurance company. The aggregate claims up to time  $t$ ,

$$S(t) = X_1 + \dots + X_{N(t)} = \sum_{i=1}^{N(t)} X_i, \quad t \ge 0 \quad (1)$$

(with  $S(t) = 0$  if  $N(t) = 0$ ) forms a random process of interest in Insurance Risk Model. It combines the two sources of uncertainty about the portfolio—the claim frequency and severity. The collection  $\{S(t)\}_{t\geq 0}$  is called the *aggregate claims process*, see [9, Chapters 6, 9].

Another important insurance process is the accumulated surplus at  $t$ :

$$U(t) = u + ct - S(t) = u + ct - \sum_{i=1}^{N(t)} X_i, \quad t > 0$$
(2)

where  $U(0) = u \ge 0$  is the initial surplus at time 0. Here  $c$  denotes the aggregate premium amount charged per unit time by the company to its portfolio policy holders, and  $S(t)$  is given by equation (1).

# **Ruin Theory**

 $\Phi_{\bullet}(u)$ 

The central focus of classical **Ruin Theory** is the time of ruin

$$T = \inf\{t > 0; U(t) < 0\} \tag{3}$$

when the surplus falls below zero for the first time. Depending on the aggregate claims model  $S(t)$ , if  $c > \mathbb{E}[S(1)]$ , the time of ruin T may be a defective random variable, with  $\Psi(u) = \mathbb{P}\{T < \infty\} < 1$ . This  $\Psi(u)$  is called the *probability of ultimate ruin*, whereas the (possibly defective) distribution function of  $T$ ,  $\Psi(u;t) = \mathbb{P}\{T < t\}$ , is called the *finite-time* ruin probability [1].

The expected discounted penalty function, introduced by Gerber and Shiu in [6], captures the joint distribution of three random variables related to ruin; the time of ruin  $T$ , the surplus immediately prior to ruin  $U(T^{-})$ , a **Solvency** early warning, and the severity of the deficit at ruin  $|U(T)|$ , a recovery test measure. Also called the Gerber-Shiu  $(G-S)$ *function*, the expected discounted penalty function is defined as

$$= \mathbb{E}\left[e^{-\delta T}w\left(U(T^-),|U(T)|\right)I(T<\infty)\Big|U(0)=u\right]$$
(4)

where  $\delta$  is the discount rate and w is a known penalty function, representing the cost to the insurer, at the time of ruin, of a surplus  $U(T^{-})$  prior to ruin and of a deficit  $|U(T)|$  at ruin. The indicator function  $I(T < \infty)$  applies the penalty only if ruin occurs.

Table 1 lists some interesting special choices of the penalty function  $w$ .

The  $G-S$  function was first derived in [6] for the classical Poisson risk model, in which  $S(t)$  in equation (1) is a compound Poisson  $(\lambda; F_X)$  process. Gerber and Shiu show that  $\Phi_{\delta}$  satisfies a defective renewal equation

$$\Phi_{\delta}(u) = \frac{\lambda}{c} \int_{0}^{u} \Phi_{\delta}(u-x) \int_{x}^{\infty} e^{-\rho(y-x)} dF_{X}(y) dx$$
$$+ \frac{\lambda}{c} e^{\rho u} \int_{u}^{\infty} e^{-\rho x} \int_{x}^{\infty} w(x, y-x) dF_{X}(y) dx$$
(5)

| δ            | w(x, y)                  | Special case of the $G-S$<br>function $\Phi_{\delta}(u)$    |
|--------------|--------------------------|-------------------------------------------------------------|
| $\delta > 0$ | $e^{-tx - sy}$           | Trivariate Laplace transform<br>of T, $U(T^-)$ and $ U(T) $ |
| $\delta > 0$ | 1                        | the Laplace transform of $T$                                |
| $\delta = 0$ | $x^m y^n$                | Joint moments of $U(T^-)$ and<br> U(T)                      |
| $\delta = 0$ | $I(x + y < z)$           | (defective) distribution of<br>ruin-causing claim at $z$    |
| $\delta = 0$ | $I(x \leq z, y \leq z')$ | joint distribution of $U(T^-)$<br>and $ U(T) $ at $(z, z')$ |
| $\delta = 0$ |                          | The probability of ultimate<br>ruin $\Psi(u)$               |

**Table 1** G-S function  $\Phi_{\delta}(u)$  for different penalty functions  $w$ 

where  $\rho$  is the unique nonnegative solution of Lundberg's equation

$$\lambda + \delta - c\rho = \lambda \hat{F}_X(\rho) \tag{6}$$

and  $\hat{F}_X(s) = \int_0^\infty e^{-sx} dF_X(x)$  is the Laplace–Stieltjes transform of  $F_X$ .

The solution of equation  $(5)$  can be expressed as an infinite series of convolutions  $\Phi_{\delta}(u) = h *$  $\sum_{k}^{\infty} g^{*k}(u)$ , for given auxiliary functions g and  $h$ . This result extends to more general risk processes, including the Sparre Andersen (compound renewal) model [10], discounting of claims [2, 3], Lévy risk processes [4], or the Markov-modulated risk model [11].

# **Applications to Finance**

The G-S function has been used also to analyze some financial instruments, such as several types of perpetual American options [7, 8]. As pointed out in these references, the pricing of perpetual options is related to the valuation of equity indexed annuities (EIA), hence the  $G-S$  function can help in analyzing the financial guarantee embedded in an EIA.

Current research work on G-S functions and extensions to financial instruments includes the valuation of contingent claims and the study of the optimal stopping time to exercise an option.

#### References

- [1] Asmussen, S. (2000). Ruin Probabilities, World Scientific, Singapore.
- [2] Cai, J. & Dickson, D.C.M. (2002). On the expected discounted penalty function at ruin of a surplus process with interest, Insurance Mathematics and Economics 30,  $389 - 404$
- [3] Cai, J., Feng, R. & Willmot, G.E. (2007). The compound Poisson surplus model with interest and liquid reserves: analysis of the Gerber-Shiu discounted penalty function, Methodology and Computing in Applied Probability in press.
- [4] Garrido, J. & Morales, M. (2006). On the expected discounted penalty function for Levy risk processes, North American Actuarial Journal 10(4), 196-218.
- [5] Gerber, H.U. (1979). An Introduction to Mathematical Risk Theory, S.S. Huebner Foundation for Insurance, University of Pennsylvania.
- Gerber, H.U. & Shiu, E.S.W. (1998). On the time value [6] of ruin, North American Actuarial Journal 2(1), 48-78.
- Gerber, H.U. & Shiu, E.S.W. (1998). Pricing perpetual [7] options for jump processes, North American Actuarial Journal  $2(3)$ ,  $101-112$ .
- [8] Gerber, H.U. & Shiu, E.S.W. (2003). Pricing perpetual fund protection with withdrawal option, North American Actuarial Journal  $7(2)$ , 1–33.
- [9] Klugman, S.A., Panjer, H.H. & Willmot, G.E. (2008). Loss Models: From Data to Decisions, 3rd Edition, John Wiley & Sons, New York.
- [10] Li, S. & Garrido, J. (2005). On a general class of renewal risk process: analysis of the Gerber-Shiu function, Advances in Applied Probability 37, 836-8856.
- $[11]$ Lu, Y. & Tsai, C.C.L. (2007). The expected discounted penalty at ruin for a Markov-modulated risk process perturbed by diffusion, North American Actuarial Journal 11(2), 136-152.

ALEJANDRO BALBAS & JOSE GARRIDO
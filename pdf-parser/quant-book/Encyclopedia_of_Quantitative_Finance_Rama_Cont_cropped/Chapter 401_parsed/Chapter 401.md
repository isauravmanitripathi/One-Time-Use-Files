# **Esscher Transform**

The *Esscher transform* has a long and remarkable history in actuarial science. Its origin can be traced back to the seminal work of a Swedish actuary, Esscher [7], whose motivation was to develop a flexible and convenient way to approximate the probability distribution of the aggregate claims of an insurance portfolio (*see* **Accumulated Claims**), an important problem in the classical risk theory. Buhlmann [1, 2] developed the Esscher premium ¨ calculation principle and showed that it is a particular case of an economic premium principle. Nowadays, the Esscher transform has applications in option valuation, asset allocation, and risk management, the so-called three pillars in quantitative finance.

Suppose *F (x)* represents the probability distribution function of a nonnegative random variable *X* and *θ* denotes a real constant so that the moment generating function of *X* exists; that is,

$$M_X(\theta) := E[e^{\theta X}] < \infty \tag{1}$$

The Esscher transform *F (x, θ )* is defined as

$$F(x,\theta) := \frac{\int_0^x e^{\theta y} dF(y)}{M_X(\theta)}$$
 (2)

Here, *F (x, θ )* is well defined since *MX(θ ) <* ∞. *MX(θ )* is a normalization constant to make *F (x, θ )* a probability distribution function.

The main idea of the Esscher transform is to define a new probability distribution function for *X* by adjusting the original distribution *F (x)* of *X* using an exponential factor e*θy* . In particular, for each given parameter *θ*, we associate it with a transformed probability distribution function *F (x, θ )* of *X*.

In this article, we focus on the applications of the Esscher transform in quantitative finance. For an excellent survey of the applications of the Esscher transform in actuarial science, see [14]. Here, we discuss the applications of the Esscher transform to option valuation and asset allocation (*see* **Merton Problem**). For the applications of the Esscher transform to risk management, see [12].

## **Application to Option Pricing**

The pioneering work of Gerber and Shiu [8] used the Esscher transform for option valuation. Let {*X(t)*; *t* ≥ 0} denote a stochastic process with stationary and independent increments and *X(*0*)* = 0. Assume that the force of interest or the risk-free interest rate *r* is a positive constant. For each *t* ≥ 0, the random variable *X(t)* has an infinitely divisible distribution. Let *S(t)* denote the price of a nondividend-paying risky asset at time *t*. Assume that

$$S(t) = S(0)e^{X(t)}, \quad t \ge 0$$

Here, *X(t)* represents the continuously compounded return from the non-dividend-paying risky asset over the time horizon [0*, t*].

Let *F (x, t)* denote the probability distribution function of *X(t)*. Suppose *MX(z, t)* represents the moment generating function of *X(t)*; that is, *MX(z, t)* := *E*[e*zX(t)*]. The Esscher transform of the process {*X(t)*; *t* ≥ 0} is also a process with stationary and independent increments. The probability distribution function of *X(t)* defined by the Esscher transform with parameter *θ* is

$$F(x,t;\theta) := \frac{\int_0^x e^{\theta y} dF(y,t)}{M_X(\theta,t)}$$
(3)

The moment generating function of *X(t)* evaluated under the probability distribution function *F (x, t*; *θ )* defined by the Esscher transform with parameter *θ* is

$$M_X(z,t;\theta) = \frac{M_X(\theta+z,t)}{M_X(\theta,t)}$$
(4)

By the fundamental theorem of asset pricing (*see* **Fundamental Theorem of Asset Pricing**) (see [10, 11]), to guarantee the absence of arbitrage (*see* **Arbitrage Strategy**) options should be priced by taking the expected discounted payoffs with respect to an equivalent measure under which the discounted stock price process {e<sup>−</sup>*rtS(t)*; *t* ≥ 0} is a martingale (*see* **Equivalent Martingale Measures**). Such a change of measure can be achieved using the Esscher transform in the following way. First, we look for a risk-neutral Esscher parameter *θ* <sup>∗</sup> such that

$$1 = e^{-rt} E^*[e^{X(t)}]$$
 (5)

where  $E^*[\cdot]$  represents expectation taken with respect to the probability distribution function  $F(x, t; \theta^*)$ . Equivalently,  $\theta^*$  is the unique solution of the following equation (see  $[8]$ ):

$$r = \ln[M_X(1, 1; \theta^*)] \tag{6}$$

Now, we consider a European-style option (see **Options: Basic Definitions**) with payoff  $V(T)$  at maturity  $T$ . Then, the price of the option is

$$V(0) = E^*[e^{-rT}V(T)] \tag{7}$$

The Esscher transform provides a flexible and convenient way to price options under different parametric specifications of the return process of the underlying risky asset. It is also a convenient tool for option valuation under an incomplete market, in which there is more than one equivalent martingale measure and not every contingent claim can be hedged (see **Hedg**ing) perfectly. However, an important question arises. How does one justify an option price obtained from the Esscher transform in an incomplete market? Gerber and Shiu [8] showed that an option price arising from the Esscher transform can be obtained by solving a utility maximization problem of an economic agent with power utility. Bühlmann et al. [3, 4] provided justification for the use of the Esscher transform for asset pricing under general dynamics of the underlying risky assets. The novelty of the work of Gerber and Shiu is to highlight the interplay between actuarial and financial pricing, which is coined as an important research agenda in modern actuarial science (see [3]). Since the work of Gerber and Shiu [8], there has been much work on further exploring the use of the Esscher transform for option pricing.

Bühlmann et al. [3] introduced the conditional Esscher transform to price options under general semimartingales (*see* **Martingales**). Bühlmann *et al.* [4] adopted the Esscher transform in a discrete financial model and investigated the no-arbitrage theory of asset pricing. Chan [5] employed the Esscher transform to price options in a continuous-time financial model driven by Lévy processes (see **Exponential** Lévy Models). Yao [15] specified a forward-riskadjusted measure and developed a consistent framework for pricing options on equities, interest rates and foreign exchange rates. Siu et al. [13] introduced the use of the Esscher transform for pricing options under a class of GARCH models with innovations having a general and flexible distribution. Elliott et al. [6] considered the option pricing problem when the price dynamics of the underlying risky asset are governed by a Markov regime-switching model.

#### **Asset Allocation**

The Esscher transform can also be used to provide an elegant solution to the asset allocation problem [9]. Here, we outline the key results from Gerber and Shiu [9] under a complete securities market with a single primitive risky asset. Let  $\{X(t); t > 0\}$  denote a Wiener process with "real-world" expected rate of return  $\mu$  and diffusion coefficient  $\sigma$ ; that is, for each  $t > 0, X(t)$  follows a normal distribution with mean  $\mu t$  and variance  $\sigma^2 t$ . Define a price kernel of the securities market by the Esscher transform as below:

$$\Lambda := \frac{e^{\theta^* X(T)}}{E[e^{\theta^* X(T)}]} \tag{8}$$

where, in this case, the risk-neutral Esscher parameter  $\theta^*$  is given by

$$\theta^* = \frac{r - \sigma^2/2 - \mu}{\sigma^2} \tag{9}$$

Let  $\beta := \theta^* \mu + (\theta^* \sigma)^2 / 2$ . Then,

$$\Lambda = e^{\theta^* X(T) - \beta T} \tag{10}$$

Suppose  $Y$  denotes a random payment in the securities market at time  $T$ . Then, the price of the random payment at time 0 is  $E[\Lambda Y]$ . Consider an investor with initial wealth  $w$  and decision horizon  $T$  who buys the random payment  $Y$ . Then, the terminal wealth of the investor at time  $T$  is

$$W(T) = w e^{rT} + Y - E[\Lambda Y] \tag{11}$$

This implies that

$$E[\Lambda W(T)] = w e^{rT} \tag{12}$$

Now, we suppose that the investor has a risk-averse utility function (*see* **Utility Function**)  $u(x)$  such that  $u'(x) > 0$  and  $u''(x) < 0$ . The goal of the investor is to determine the terminal wealth  $W(T)$ , which maximizes the expectation  $E[u(W(T))]$  subject to the budget constraint imposed by equation (12).

Gerber and Shiu showed that the necessary and sufficient condition for optimality is

$$u'(W(T)) = E[u'(W(T))] \Lambda \tag{13}$$

The necessary condition can be shown by a standard tool in actuarial science, namely, the variational argument (see [9]). The sufficient condition for optimality can be shown by exploiting the concavity of the utility function.

Let  $m := E[u'(W(T))]$ . Suppose I is an inverse of the marginal utility function  $u'$ . Since  $u'' < 0$ , I exists. Then, the optimal terminal wealth is

$$W(T) = I(m\Lambda) \tag{14}$$

By equations  $(12)$  and  $(14)$ ,

$$E[\Lambda I(m\Lambda)] = w e^{rT} \tag{15}$$

Consider an exponential utility function as follows:

$$u(x) = -\frac{e^{-\alpha x}}{\alpha}, \quad x \in (-\infty, \infty) \tag{16}$$

where  $\alpha > 0$  and  $1/\alpha$  is the constant level of risk tolerance.

In this case, the optimal terminal wealth is given by

$$W(T) = w e^{rT} + \frac{\theta^* [(r - \sigma^2/2)T - X(T)]}{\alpha} \quad (17)$$

Under the assumption of a frictionless and complete market, Gerber and Shiu [9] determined an optimal dynamic strategy by replicating a contingent claim related to the optimal terminal wealth  $W(T)$ . In particular, for the exponential utility function, Gerber and Shiu [9] obtained the following optimal amount invested in the risky asset at time  $t \in [0, T]$  using the dynamic delta hedging argument:

$$\rho(t) = \left(\frac{\mu - r + \sigma^2/2}{\alpha \sigma^2}\right) e^{-r(T-t)} \tag{18}$$

### References

- [1] Bühlmann, H. (1980). An economic premium principle, ASTIN Bulletin 11, 52-60.
- Bühlmann, H. (1984). The general economic premium, [2] ASTIN Bulletin 14, 13-21.
- [3] Bühlmann, H., Delbaen, F., Embrechts, P. & Shiryaev, A.N. (1996). No-arbitrage, change of measures and conditional Esscher transforms, CWI Quarterly 9, 291-317.

- Bühlmann, H., Delbaen, F., Embrechts, P. & Shirvaev, [4] A.N. (1998). On Esscher transforms in discrete finance models, ASTIN Bulletin 28, 171-186.
- Chan, T. (1999). Pricing contingent claims on stocks [5] driven by Lévy processes, Annals of Applied Probability 9, 503-528.
- [6] Elliott, R.J., Chan, L.L. & Siu, T.K. (2005). Option pricing and Esscher transform under regime switching, Annals of Finance 1(4), 423-432.
- [7] Esscher, F. (1932). On the probability function in the collective theory of risk, Skandinavisk Aktuarietidskrift 15, 175-195.
- [8] Gerber, H.U. & Shiu, E.S.W. (1994). Option pricing by Esscher transforms (with discussions), Transactions of the Society of Actuaries 46, 99-191.
- Gerber, H.U. & Shiu, E.S.W. (2000). Investing for retire-[9] ment: optimal capital growth and dynamic asset allocation, North American Actuarial Journal 4(2), 42-62.
- [10] Harrison, J.M. & Pliska, S.R. (1981). Martingales and stochastic integrals in the theory of continuous trading, Stochastic Processes and Their Applications 11,  $215 - 280.$
- [11] Harrison, J.M. & Pliska, S.R. (1983). A stochastic calculus model of continuous trading: complete markets, Stochastic Processes and their Applications 15, 313-316.
- [12] Siu, T.K., Tong, H. & Yang, H. (2001). Bayesian risk measures for derivatives via random Esscher transform, *North American Actuarial Journal* **5**(3), 78–91.
- [13] Siu, T.K., Tong, H. & Yang, H. (2004). On pricing derivatives under GARCH models: a dynamic Gerber-Shiu approach, North American Actuarial Journal 8(3),  $17 - 31$
- [14] Yang, H. (2004). The Esscher transform, in *Encyclopedia* of Actuarial Science, J. Teugels & B. Sundt, eds, John Wiley & Sons, New York, Vol. 2, pp. 617-621.
- [15] Yao, Y. (2001). State price density, Esscher transforms, and pricing options on stocks, bonds, and foreign exchange rates, North American Actuarial Journal 5, 104-117.

#### **Related Articles**

**Equivalence of Probability Measures; Equivalent** Martingale Measures; Exponential Lévy Models

TAK KUEN SIU
# **Exchange Options**

# **Definition and Examples**

A European exchange option is a contract that gives the buyer the right to exchange two (possibly dividend-paying) assets *A* and *B* at a fixed expiration time *T* , say, to receive *A* and deliver (or pay) *B*; thus, the option payoff is

$$(A_T - B_T)^+ := \max(A_T - B_T, 0) \tag{1}$$

(American and Bermudan exchange options are complicated by early optimal exercise and not discussed here.) An ordinary (European) call or put on an asset struck at *K* can be viewed, as in [9], as an option to exchange the asset with the *T* -maturity zero-coupon bond of principal *K*. More generally, a call or put on an *s*-maturity forward contract (*s* ≥ *T* ) on a zero-dividend asset is equivalent to an option to exchange the asset at time *T* with an *s*-maturity zero-coupon bond. Options to exchange two stocks or commodities provide good hypothetical examples but are not prevalent in the market place.

Exchange options are related to spread options with time-*T* payoffs of the form *(X* − *Y )*<sup>+</sup>, given two prescribed time-*T* observables *X* and *Y* . A common structure is a CMS spread option, with *X* and *Y* , say, the 20-year and the 2-year spot swap rates at time *T* . A spread option can be viewed as an exchange option when there exist (or can be replicated) two zero-dividend assets *A* and *B* such that *AT* = *X* and *BT* = *Y* . In the CMS case, *A* and *B* can be taken as the coupon cash flows of two CMS bonds or swaps. In practice, exchange options on dividend-paying assets are reduced to the zero-dividend case in a similar way.

Interest-rate swaptions, including caplets and floorlets as one-period special cases, can be viewed both as ordinary call or put options struck at par on coupon bonds and more directly as options to exchange the fixed and floating cash flow legs of a swap. The latter is the standard as it imposes the classical assumption of a lognormal ratio *AT /BT* on the forward swap rate (a swap-curve concept) rather than on the forward coupon bond price.

An exchange option is related to its reverse by parity: *(Y* − *X)*<sup>+</sup> = *(X* − *Y )*<sup>+</sup> + *Y* − *X.* (Hence, an American option to exchange two fixed zero-dividend assets is not exercised early.)

# **Pricing and Hedging Approaches**

The exchange option is a special case of a *pathindependent* contingent claim with payoff being a *homogeneous function* of the underlying asset prices at expiration. It is governed by the same general theory (*see* **Option Pricing: General Principles**). One makes sure that the underlying assets are arbitrage free, which implies that there are no free lunches in a strong sense. If the payoff can be attained by a sufficiently regular self-financing trading strategy (SFTS) (e.g., a bounded number of shares or "deltas"), then the law of one price holds and the option price at each time is defined as the value of the self-financing portfolio. Otherwise, arbitrage-free pricing is not unique. We do not discuss this case, but only mention that one approach then chooses a linear pricing kernel (e.g., the minimal measure) among the many then available and another is nonlinear based on expected utility maximization.

Payoff replication by an SFTS is a question of predictable representation. As the payoff in this case is a path-independent function of the underliers, it seems natural that the option price as well as deltas be functions of time and the underliers at that time. This has been the traditional Markovian approach, beginning with Black and Scholes [1] and immediate extension by Merton [9] (*see* **Black–Scholes Formula**). Their simple choice of a geometric Brownian motion for the underlying asset in [1] and more generally of a deterministic-volatility forward price process in [9] meant that the underlying SDE and the associated PDE had constant coefficients (in log-state). Ito's formula was applied to construct a ˆ riskless hedge, with the deltas (hedge ratios) simply given by partial derivatives of the unique solution to the PDE.

Black and Scholes constructed an SFTS for a call option struck at *K* by dynamically rebalancing long positions on the underlying asset *A* financed by shorting the riskless money market asset *B*<sup>∗</sup> = *(*e*rt)*, post an initial investment equal to the option price. Merton's extension to stochastic interest rate *r* treated the call as an option *C* to exchange the asset *A* with the *T* -maturity zero-coupon bond *B* of principal *K*. The Black–Scholes model corresponded to a deterministic bond price  $B_t = e^{-r(T-t)}K$ , but now, in general,  $B$  had infinite variation. The former's simplicity was nonetheless recaptured by exploiting the homogeneous symmetry of the option payoff to reduce dimensionality by  $1$ —in effect, a projective transformation that hedged the forward option contract  $F := C/B$  with trades in the forward asset  $X :=$  $A/B$ . The relevant volatility was accordingly the forward price volatility. An SFTS in the two assets and Itô's formula led to a PDE for the homogeneous option price function  $C(t, A, B)$  and an equivalent PDE for the forward option price function  $F(t, X)$ .

Margrabe [8] extended the theory in [9] to an option to exchange any two correlated assets assuming constant volatilities (see Margrabe Formula). He observed akin to [9] that the self-financing equation with  $\partial C/\partial A$  and  $\partial C/\partial B$  as deltas is, by Itô's formula, equivalent to  $C(t, A, B)$  satisfying a PDE with no first-order terms in  $A, B$ . Choosing  $C$  as the homogenized Black-Scholes function, it followed by Euler's formula for homogeneous functions that  $\partial C/\partial A$  and  $\partial C/\partial B$  in fact formed an SFTS. The result demonstrated that (in this case) the exchange option is replicated by dynamically going long in  $A$ and short in  $B$ , with no trades in any other asset. (This fails in general, e.g., a bond exchange option in a  $k \ge 3$  factor non-Gaussian short-rate model.) "*Taking* asset two as numéraire," Margrabe [8] also presented (acknowledging Stephen Ross) a key financial invariance argument as a heuristic alternative to the PDE algebraic proof of [9], reducing to a call on  $A/B$ struck at 1 in the Black-Scholes model with zero interest rate.

Martingale theory leads to a conceptual as well as computationally practical representation of solutions to the PDEs that describe option prices as a conditional expectation of terminal payoff. Harrison and Kreps [5] and Harrison and Pliska [6] developed, in related papers, an equivalent martingale measure framework that not only made this fruitful representation of the option price available but also laid a more general and probabilistic formulation of the notion of a dynamic hedge, or its mirror image, a replicating SFTS (see Risk-neutral Pricing). Their arbitrage-free semimartingale approach does permit path dependency, yet accommodates Markovian SDE/PDE models even better. They took the money market asset  $B^*$  as a tradable entering any hedge, giving it a general stochastic form  $B_{r}^{*} = e^{\int_{0}^{t} r_{s} ds}$  for discounting payoffs before expectation. In concert with Black-Scholes but in contrast to Merton and Margrabe, the finite variation asset  $B^*$ was their exclusive choice of numéraire.

With the advent of the forward measure sometime later (see Forward and Swap Measures), it was evident that Merton's choice of an infinite variation zero-coupon bond  $B$  as the financing hedge instrument fitted equivalent martingale measure theory perfectly well, and it led to quicker derivations of concrete pricing formulae than  $B^*$ , as discounting is conveniently performed outside the expectation [4, 7]. Another useful numéraire was the one by Neuberger [10] to price interest-rate swaptions. Viewed as an option to exchange the fixed and floating swap cash flows, the assets' ratio  $A/B$  represents the forward swap rate here. The assumption in [10] that the ratio has deterministic volatility yielded a model that has since served as industry standard to quote swaption-implied volatilities (see Swap Mar**ket Models**). Here, it is noteworthy that the ratio  $A/B$ has deterministic volatility but  $A$  and  $B$  themselves decidedly do not. In time, El-Karoui et al. [4] showed that one can basically change numéraire to any asset  $B$  and associate with it an equivalent measure under which  $A/B$  is a martingale for every other asset A (see Change of Numeraire).

Today, option pricing and hedging theory has advanced farther and in many directions. Especially relevant to our discussion of exchange options is the principle of numéraire invariance and arbitrage-free modeling. For in-depth studies of these and related topics, we refer the reader to  $[3]$  and  $[2]$ , among other excellent books. Our approach is to concentrate on the modeling in "projective coordinate"  $X := A/B$ , and impose for the most part conditions that are invariant under the transformation  $X \mapsto 1/X$ .

# The Deterministic-volatility and **Exponential-Poisson Models**

The option to exchange two assets with a *deterministic volatility*  $\sigma(t)$  of the asset price ratio  $X = A/B$  is celebrated as the simplest nontrivial example in option pricing theory. Its classical Black-Scholes/Merton option price function and explicit representation of the "deltas" ("hedge ratios") illustrate the principles that underline options in many assets with arbitrary homogeneous payoffs and more general dynamics. There is another concrete albeit less known example with simple jumps in  $X$  involving the Poisson rather than the normal distribution. The pattern is similar, with the main difference being that the deltas are the partial differences rather than the partial derivatives of the option price function.

We fix, throughout, a stochastic basis  $(\Omega, (\mathcal{F}_t), \mathcal{F}_t)$  $\mathbb{P}$ ) with time horizon  $t \in [0, T]$ ,  $T > 0$ . In this section, we fix two *zero-dividend* assets with price processes  $A = (A_t)$  and  $B = (B_t)$ .

#### The Exchange Option Price Process

When  $A$  and  $B$  are semimartingales, we call a pair  $(\delta^A, \delta^B)$  of (locally) bounded predictable processes a (locally) *bounded SFTS* (see, more generally, the section Self-financing Trading Strategies) if  $C =$  $C_0 + \int \delta^A \mathrm{d}A + \int \delta^B \mathrm{d}B$ , where

$$C = \delta^A A + \delta^B B \tag{2}$$

Clearly, C is then a semimartingale,  $\Delta C =$  $\delta^A \Delta A + \delta^B \Delta B$ , and hence  $C_- = \delta^A A_- + \delta^B B_-$ .

The differential form of the self-financing equation is often handy:

$$dC = \delta^A dA + \delta^B dB \tag{3}$$

SFTSs form a linear space. If there exists a unique *bounded* SFTS  $(\delta^A, \delta^B)$  such that

$$C_T = (A_T - B_T)^+ \tag{4}$$

then it is justified to call  $C$  the exchange option price *process* and  $\delta^A$  and  $\delta^B$  the *deltas*.

Assume now that the semimartingales  $A$  and  $B$ are positive and have positive left limits.

The numéraire invariance principle (see the section Numéraire Invariance and more comprehensively the section The Invariance Principle) states that if  $(\delta^A, \delta^B)$  is a locally bounded SFTS, then  $C = \delta^A A + \delta^B B$  satisfies  $d\left(\frac{C}{B}\right) = \delta^A d\left(\frac{A}{B}\right)$  (similarly by symmetry with A as numéraire). This is useful for uniqueness. Numéraire invariance also states the converse: if  $C$  is a semimartingale and  $\delta^A$  a locally bounded predictable process such that  $d\left(\frac{C}{B}\right) = \delta^A d\left(\frac{A}{B}\right)$ , then  $(\delta^A, \delta^B)$  is an SFTS and equations (2) and (3) hold, where  $\delta^B = \frac{C_-}{R} - \delta^A \frac{A_-}{R}$ .

This reduces existence to finding an  $F_0$  and  $\delta^A$  such that

$$\left(\frac{A_T}{B_T} - 1\right)^+ = F_0 + \int_0^T \delta_t^A \mathrm{d}\left(\frac{A_t}{B_t}\right) \qquad (5)$$

The exchange option price process is then the semimartingale  $C = B\left(F_0 + \int \delta^A d\left(\frac{A}{B}\right)\right)$ .<br>Numéraire invariance in effect reduces general

option pricing and hedging to a market where one of the asset price processes equals 1 identically. The remaining task is to find the above "projective" predictable representation of the ratio payoff against the ratio process.

#### Deterministic-volatility Exchange Option Model

Let  $\sigma(t) > 0$  be a continuous positive function. Define the *Black–Scholes/Merton* projective option price function

$$f(t,x) := x\delta_A(t,x) + \delta_B(t,x) \tag{6}$$

for  $t \leq T$ ,  $x > 0$ , where  $\delta_A(T, x) := 1_{x > 1}$ ,  $\delta_B$  $(T, x) := -1_{x>1}$ , and for  $t < T$ ,

$$\delta_A(t,x) := N\left(\frac{\log x}{\sqrt{\nu_t}} + \frac{\sqrt{\nu_t}}{2}\right),$$
  
$$\delta_B(t,x) := -N\left(\frac{\log x}{\sqrt{\nu_t}} - \frac{\sqrt{\nu_t}}{2}\right) \tag{7}$$

where  $v_t := \int_t^T \sigma^2(s) ds$  and  $N(\cdot)$  is the normal distribution function. The function  $f(t, x)$  is continuous, and on  $t < T$  is  $C^1$  in t and analytic in x. In addition,  $-1 \leq \delta_B \leq 0 \leq \delta_A \leq 1$ , and

$$f(T,x) = (x-1)^{+}, \quad \frac{\partial f}{\partial x}(t,x) = \delta_A(t,x) \quad (8)$$

As is well known and seen in the sections Deterministic-volatility Model Uniqueness and Projective Continuous SDE SFTS, the function  $f(t, x)$ is the unique  $C^{1,2}$  (on  $t < T$ ) solution with bounded partial derivative  $\frac{\partial f}{\partial x}(t, x)$  subject to  $f(T, x) = (x 1)^+$  of the PDE

$$\frac{\partial f}{\partial t}(t,x) + \frac{1}{2}\sigma^2(t)x^2\frac{\partial^2 f}{\partial x^2}(t,x) = 0\tag{9}$$

Assume now  $A = BX$  for some positive continuous semimartingale  $X > 0$  satisfying

$$d[\log X]_t = \sigma^2(t)dt, \quad (A = BX) \quad (10)$$

Under this assumption, one traditionally defines the exchange option price process  $C$  by

$$C := BF, \quad F = (F_t), \quad F_t := f(t, X_t)$$
 (11)

Clearly,  $C_T = (A_T - B_T)^+$ . The definition is justified using the continuous semimartingales

$$\delta_t^A := \delta_A(t, X_t) = \frac{\partial f}{\partial x}(t, X_t),$$
  
$$\delta_t^B := \delta_B(t, X_t) = F_t - \delta_t^A X_t \tag{12}$$

Clearly,  $C = \delta^A A + \delta^B B$ , and the deltas are bounded:  $0 \le \delta^A \le 1$  and  $-1 \le \delta^B \le 0$ . Since  $f(t, x)$  satisfies the PDE (9) (as directly verified) and  $\frac{\partial f}{\partial x}(t, X_t) = \delta_t^A$ , by Itô's formula, the continuous semimartingale  $F := (f(t, X_t))$  satisfies the predictable representation

$$dF = \delta^A dX \tag{13}$$

If, at this stage, we assume that  $B$  is a semimartingale, then  $A$  and  $C$  are semimartingales too, and by the invariance principle discussed next,  $dC =$  $\delta^A dA + \delta^B dB$  and  $(\delta^A, \delta^B)$  is a bounded SFTS.

#### Numéraire Invariance

Let X and F be two semimartingales and  $\delta^A$  be a locally bounded predictable process such that  $dF = \delta^A dX$ . Set  $\delta^B = F - \delta^A X$ . Clearly  $\delta^B = F_- - \delta^A X$ .  $\delta^A X_-$  since  $\Delta F = \delta^A \Delta X$ . Let B be any semimartingale. Set  $A = BX$ ,  $C = BF$ . Clearly  $C = \delta^A A +$  $\delta^B B$ . We claim  $dC = \delta^A dA + \delta^B dB$ , so  $(\delta^A, \delta^B)$  is an SFTS.

Indeed, this follows by applying Itô's product rule to BF, then substituting  $dF = \delta^A dX$  and  $F_{-} =$  $\delta^B + \delta^A X_-\,$ , followed by Itô's product rule on BX:

$$dC = d(BF) = B_{-}dF + F_{-}dB + d[B, F]$$
  
=  $B_{-}\delta^{A}dX + (\delta^{B} + \delta^{A}X_{-})dB + \delta^{A}d[B, X]$   
=  $\delta^{A}d(BX) + \delta^{B}dB = \delta^{A}dA + \delta^{B}dB$  (14)

Conversely, if  $A$  and  $B$  are semimartingales with  $B, B_{-} > 0$  and  $(\delta^{A}, \delta^{B})$  is an SFTS, then

 $d\left(\frac{C}{B}\right) = \delta^A d\left(\frac{A}{B}\right)$ , where  $C = \delta^A A + \delta^B B$ . (See the section The Invariance Principle for a more lucid treatment.)

#### Exponential-Poisson Exchange Option Model

Assume that the two zero-dividend asset price processes A and B satisfy  $A = BX$ , where X is a semimartingale satisfying

$$X_t = X_0 e^{\beta P_t - (e^{\beta} - 1)\lambda t} \tag{15}$$

for some constants  $\beta \neq 0$ ,  $\lambda > 0$  and semimartingale P such that  $[P] = P$  and  $P_0 = 0$  (Thus,  $P_t =$  $\sum_{s\leq t} 1_{\Delta P_s\neq 0}$ ). Define the projective option price function  $f(t, x)$ ,  $x > 0$  by

$$f(t,x) := \sum_{n=0}^{\infty} (x e^{\beta n - (e^{\beta} - 1)\lambda(T - t)} - 1)^{+}$$
$$\times \frac{\lambda^{n}}{n!} (T - t)^{n} e^{-\lambda(T - t)} \tag{16}$$

and exchange option price process by

$$C := BF, \quad F = (F_t), \quad F_t := f(t, X_t)$$
 (17)

Clearly  $f(T, x) = (x - 1)^{+}$  and  $C_{T} = (A_{T} - B_{T})^{+}$ . One has the predictable representation

$$dF = \delta^A dX \tag{18}$$

as shown shortly, where

$$\delta_t^A := \delta_A(t, X_{t-}), \quad \delta_A(t, x) := \frac{f(t, e^{\beta}x) - f(t, x)}{(e^{\beta} - 1)x}$$
(19)

Thus by numéraire invariance,  $(\delta^A, \delta^B)$  is an SFTS if  $A$  and  $B$  are semimartingales, where

$$\delta^B := F - \delta^A X = F_- - \delta^A X_- \tag{20}$$

Moreover, it is bounded. Indeed, since  $|(e^{\beta}y 1)^+ - (y - 1)^+ \le |e^{\beta} - 1|y \text{ for any } y > 0,$ 

$$0 \le \delta_A(t, x) \le \sum_{n=0}^{\infty} e^{\beta n - (e^{\beta} - 1)\lambda(T - t)}$$
$$\times \frac{\lambda^n}{n!} (T - t)^n e^{-\lambda(T - t)} = 1 \tag{21}$$

Hence,  $0 \le \delta^A \le 1$ . Similarly,  $-1 \le \delta^B \le 0$ .

We note that  $f(t, x)$  is not  $C^1$  in x (though convex, absolutely continuous, and piecewise analytic in  $x$ ). We also caution that this model is arbitrage free only when  $\mathbb{P}\{P_t = n\} > 0$  for all  $t > 0$  and  $n \in \mathbb{N}$ , for example, when  $P$  is a Poisson process under an equivalent measure.

## Derivation of the Predictable Representation

To show  $dF = \delta^A dX$  (equation (18)), we first note that  $[P]^c = 0$  since  $[P] = P$ ; hence,  $(\Delta P)^2 = \Delta P$ and  $P_t = [P]_t = \sum_{s \le t} \Delta P_s$ . If  $v(p), p \in \mathbb{R}$ , is any function, then clearly  $V = (v(P_t))$  is a semimartingale and we have

$$\begin{aligned} \Delta V_t &= v(P_t) - v(P_{t-}) = (v(P_t) - v(P_{t-})) \Delta P_t \\ &= (v(P_{t-} + 1) - v(P_{t-})) \Delta P_t \end{aligned} \tag{22}$$

Hence, as  $V$  is clearly the sum of its jumps,

$$V_t - v(0) = \sum_{s \le t} \Delta V_s$$
  
=  $\sum_{s \le t} (v(P_{s-} + 1) - v(P_{s-})) \Delta P_s$   
=  $\int_0^t (v(P_{s-} + 1) - v(P_{s-})) dP_s$  (23)

Likewise,  $(u(t, P_t))$  is a semimartingale for any  $C^1$  in t function  $u(t, p), p \in \mathbb{R}$ , and one has

$$du(t, P_t) = \frac{\partial u}{\partial t}(t, P_{t_-})dt + (u(t, P_{t_-} + 1) - u(t, P_{t_-}))dP_t$$
 (24)

Now, define the function

$$x(t, p) := X_0 e^{\beta p - (e^{\beta} - 1)\lambda t} \quad (p \in \mathbb{R})$$
 (25)

Clearly  $X_t = x(t, P_t)$ . Applying equation (24) to the function  $x(t, p)$  and using that

$$\frac{\partial x}{\partial t}(t, p) = -x(t, p)(e^{\beta} - 1)\lambda,$$
  
$$x(t, p+1) - x(t, p) = x(t, p)(e^{\beta} - 1) \qquad (26)$$

(or alternatively applying Itô's formula to  $x(t, P_t)$ and simplifying) yields

$$dX_t = X_{t-}(e^{\beta} - 1)d(P_t - \lambda t) \tag{27}$$

Next, define the function of  $t < T$  and  $p \in \mathbb{R}$ ,

$$u(t, p) := f(t, x(t, p))$$
  
= 
$$\sum_{n=0}^{\infty} (X_0 e^{\beta(p+n) - (e^{\beta} - 1)\lambda T} - 1)^+$$
$$\times \frac{\lambda^n}{n!} (T - t)^n e^{-\lambda (T - t)} \qquad (28)$$

Clearly,  $u(t, P_t) = F_t$ . One readily verifies that  $u(t, p)$  satisfies the equation

$$\frac{\partial u}{\partial t}(t, p) + \lambda(u(t, p+1) - u(t, p)) = 0 \qquad (29)$$

Hence by equation  $(24)$  we have,

$$dF_t = (u(t, P_{t_-} + 1) - u(t, P_{t_-}))d(P_t - \lambda t) \quad (30)$$

Combining this with equation  $(27)$  and the fact that clearly

$$u(t, p+1) - u(t, p) = f(t, e^{\beta}x(t, p)) - f(t, x(t, p)) \quad (31)$$

we conclude that, as desired,

$$dF_t = \frac{f(t, e^{\beta} X_{t-}) - f(t, X_{t-})}{(e^{\beta} - 1)X_{t-}} dX_t \tag{32}$$

#### The Homogeneous Option Price Function

There is an alternative derivation of the self-financing equation  $dC = \delta^A dA + \delta^B dB$  much along that in [9] and [8] that does not employ numéraire invariance. It is related to a family of two-dimensional PDEs satisfied by the Merton/Margrabe homogeneous option *price function*  $c(t, a, b)$  below.

Let  $f(t, x)$ ,  $x > 0$ , be any  $C^{1,2}$  function, for example, as in equation (6). Define the homogenized function

$$c(t, a, b) := bf\left(t, \frac{a}{b}\right) \quad (a, b > 0) \tag{33}$$

Then  $c(t, a, b)$  is homogeneous of degree 1 in  $(a, b)$ , and hence by Euler's formula

$$c(t,a,b) = \frac{\partial c}{\partial a}(t,a,b)a + \frac{\partial c}{\partial b}(t,a,b)b \qquad (34)$$

A laborious repeated application of the chain rule on equation  $(33)$  gives

$$a^{2} \frac{\partial^{2} c}{\partial a^{2}}(t, a, b) = b^{2} \frac{\partial^{2} c}{\partial b^{2}}(t, a, b)$$
$$= -ab \frac{\partial^{2} c}{\partial a \partial b}(t, a, b)$$
$$= bx^{2} \frac{\partial^{2} f}{\partial x^{2}}(t, x), \quad x := \frac{a}{b} \quad (35)$$

Let  $\sigma(t)$ ,  $\sigma_A(t, a, b)$ ,  $\sigma_B(t, a, b)$ ,  $\sigma_{AB}(t, a, b)$  be any functions  $(a, b > 0)$  such that

$$\sigma^{2}(t) = \sigma_{A}^{2}(t, a, b) + \sigma_{B}^{2}(t, a, b) - 2\sigma_{AB}(t, a, b)$$
(36)

Using equations (35), (36), and  $\frac{\partial c}{\partial t}(t, a, b) =$  $b\frac{\partial f}{\partial t}\left(t,\frac{a}{b}\right)$ , we see that  $c(t,a,b)$  satisfies the PDE

$$\frac{\partial c}{\partial t} + \frac{1}{2}\sigma_A^2(t, a, b)a^2 \frac{\partial^2 c}{\partial a^2} + \frac{1}{2}\sigma_B^2(t, a, b)b^2 \frac{\partial^2 c}{\partial b^2}$$
$$+ \sigma_{AB}(t, a, b)ab \frac{\partial^2 c}{\partial a\partial b} = 0 \tag{37}$$

if and only if  $f(t,x)$  satisfies the PDE (9):  $\frac{\partial f}{\partial t}$  +  $\frac{1}{2}\sigma^2(t)x^2\frac{\partial^2 f}{\partial x^2} = 0.$ <br>The PDE (9) was utilized in [1] and [9] (but not

in [8]), and Merton [9] stated its equivalence to the PDE (37) (assuming  $\sigma_A$ , etc., depend only on t). As noted in [9] and expounded in [8], if  $d[\log A]_t =$  $\sigma_A^2(t)dt$ , d[log B]<sub>t</sub> =  $\sigma_B^2(t)dt$  and d[log A, log B]<sub>t</sub> =  $\sigma_{AB}(t)dt$ , then Itô's formula and equation (37) imply at once  $\mathrm{d}c(t, A_t, B_t) = \delta_t^A \mathrm{d}A_t + \delta_t^B \mathrm{d}B_t$ , with  $\delta^A$  and  $\delta^B$  as in equation (40), and thus  $(\delta^A, \delta^B)$  is an SFTS with price process  $c(t, A, B)$  by Euler's formula (34).

Let us expand on this (see also the sections Self-financing Trading Strategies and Homogeneous Continuous Markovian SFTS). Let  $\sigma(t)$  > 0 be a continuous function, and  $f(t, x)$  be the Black–Scholes/Merton function (6). Set  $c(t, a, b) :=$  $bf(t, a/b)$ . Clearly,

$$\frac{\partial c}{\partial a}(t, a, b) = \frac{\partial f}{\partial x}\left(t, \frac{a}{b}\right) = \delta_A\left(t, \frac{a}{b}\right) \tag{38}$$

This combined with Euler's formula (34) and the definition (6)  $f := \delta_A x + \delta_B$  give

$$\frac{\partial c}{\partial b}(t, a, b) = \delta_B\left(t, \frac{a}{b}\right) \tag{39}$$

Assume that  $A$  and  $B$  are positive semimartingales with positive left limits and  $X := A/B$  has deterministic volatility  $\sigma(t)$ :  $d[X]_t = X_t^2 \sigma^2(t) dt$ . Using equation (12), the deltas are conveniently the sensitivities of the homogeneous Merton/Margrabe function:

$$\delta_t^A = \frac{\partial c}{\partial a}(t, A_t, B_t), \quad \delta_t^B = \frac{\partial c}{\partial b}(t, A_t, B_t) \quad (40)$$

Since *X* is continuous, we also have  $\delta_t^A = \frac{\partial C}{\partial a}(t, A_{t-}, B_{t-})$  and similarly  $\delta_t^B$ . The section Deterministic-Volatility Exchange Option Model yields  $dC = \delta^A dA + \delta^B dB$  with  $C_t = B_t f(t, X_t) =$  $c(t, A_t, B_t)$ . Therefore, by equation (40) and Itô's formula,

$$\frac{\partial c}{\partial t}dt + \frac{1}{2}\frac{\partial^2 c}{\partial a^2}d[A]_t^c + \frac{1}{2}\frac{\partial^2 c}{\partial b^2}d[B]_t^c + \frac{\partial^2 c}{\partial a\partial b}d[A, B]_t^c = 0 \tag{41}$$

where the partial derivatives are evaluated at  $(t, A_{t-}, B_{t-})$  and  $[\cdot]^c$  is the bracket continuous part. (The jump term in Itô's formula vanishes as it equals  $\sum_{s < t} (\Delta C_s - \delta_s^A \Delta A_s - \delta_s^B \Delta B_s) = 0.$ 

Returning to the approach of Merton [9], assume now that  $d[\log A]_t = \sigma_A^2(t, A_t, B_t) dt$  for some function  $\sigma_A$  and similarly d[log B] =  $\sigma_B^2 dt$  and  $d[\log A, \log B] = \sigma_{AB} dt$ . Then equation (36) holds using  $\log X = \log A - \log B$ . Since  $f(t, x)$  satisfies the PDE (9), the PDE (37) follows as before by the chain rule. However, equation (37) implies equation (41), which by Itô's formula in turn implies the selffinancing equation  $dC = \delta^A dA + \delta^B dB$  with  $\delta^A$  and  $\delta^B$  given by equation (40).

#### Change of Numéraire

The solution  $c(t, a, b)$  to the PDE (37) subject to  $c(T, a, b) = (a - b)^{+}$  can be expressed in a form  $\mathbb{E}(X - Y)^{+}$  for some random variables X and  $Y > 0$ with means  $a$  and  $b$ . Expectations of this form often become more tractable by a change of measure as in [4]. Define the equivalent probability measure  $\mathbb{Q}$  by  $\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} := \frac{Y}{\mathbb{F}\mathbf{V}}.$  Clearly,

$$\mathbb{E}^{\mathbb{Q}}\left(\frac{X}{Y}\right) = \frac{\mathbb{E}(X)}{\mathbb{E}(Y)} \quad \left(\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} := \frac{Y}{\mathbb{E}(Y)}\right) \tag{42}$$

Replacing X by  $(X - Y)^+$  in equation (42) and using the homogeneity to factor out  $Y$ , we get

$$\mathbb{E}\left(X-Y\right)^{+} = \mathbb{E}(Y)\mathbb{E}^{\mathbb{Q}}\left(\frac{X}{Y}-1\right)^{+} \tag{43}$$

If  $X/Y$  is  $\mathbb{Q}$ -lognormally distributed then equation  $(43)$  together with equation  $(42)$  readily yields

$$\mathbb{E}(X - Y)^{+} = \mathbb{E}(X)N\left(\frac{\log(\mathbb{E}X/\mathbb{E}Y)}{\sqrt{\nu^{\mathbb{Q}}}} + \frac{\sqrt{\nu^{\mathbb{Q}}}}{2}\right) - \mathbb{E}(Y)N\left(\frac{\log(\mathbb{E}X/\mathbb{E}Y)}{\sqrt{\nu^{\mathbb{Q}}}} - \frac{\sqrt{\nu^{\mathbb{Q}}}}{2}\right)$$
(44)

where  $\nu^{\mathbb{Q}} := \text{var}^{\mathbb{Q}}[\log(X/Y)]$ . When X and Y are bivariately lognormally distributed, it is not difficult to show that  $X/Y$  is lognormally distributed in both  $\mathbb{P}$  and  $\mathbb{Q}$  with the same log-variance  $\nu^{\mathbb{Q}} = \nu :=$  $\text{var}[\log(X/Y)].$  Then  $\nu^{\mathbb{Q}}$  can be replaced with  $\nu$  in equation (44). This occurs when the functions  $\sigma_A$ ,  $\sigma_B$ and  $\sigma_{AB}$  in equation (37) are independent of *a* and *b*, as in  $[8, 9]$ .

#### Uniqueness

Assume that  $A$  and  $B$  are positive semimartingales with positive left limits such that  $X := A/B$ is square-integrable martingale under an equivalent probability measure  $\mathbb{Q}$  and  $d\langle X\rangle_t^{\mathbb{Q}} = X_t^2 \sigma_t^2 dt$  for some nowhere zero process  $\sigma$ , where  $\langle X \rangle^{\mathbb{Q}}$  is the  $\mathbb{Q}$ -compensator of  $[X]$ . (Of course,  $\langle X \rangle^{\mathbb{Q}} = [X]$  if X is continuous.) Let  $(\delta^A, \delta^B)$  be an SFTS and set  $C := \delta^A A + \delta^B B$ . We claim that  $\delta^A = \delta^B = 0$  if  $C_T = 0$  and  $\delta^A$  is bounded.

Indeed, set  $F := C/B$ . By numéraire invariance,  $dF = \delta^A dX$ . Hence, F is a Q-square-integrable martingale since X is and  $\delta^A$  is bounded. Thus,  $F = 0$  since  $F_T = C_T/B_T = 0$ . Hence,  $0 = d\langle F \rangle^{\mathbb{Q}} =$  $(\delta^A)^2 X_{-}^2 \sigma^2 dt$ . However,  $X_{-}^2 \sigma^2 > 0$ . Thus,  $\delta^A = 0$ and  $\delta^B = F - \delta^A X = 0.$ 

In general, since  $F := C/B$  is a  $\mathbb{Q}$ -martingale, we have the following pricing formula:

$$C_t = B_t \mathbb{E}^{\mathbb{Q}}[C_T/B_T \mid \mathcal{F}_t] \tag{45}$$

#### Deterministic-volatility Model Uniqueness

Assume that  $A$  and  $B$  are positive semimartingales with positive left limits and  $X := A/B$  is an Itô process following

$$\frac{\mathrm{d}X_t}{X_t} = \mu_t \mathrm{d}t + \sigma_t \mathrm{d}Z_t, \quad \left(X := \frac{A}{B}\right) \tag{46}$$

where Z is a Brownian motion and  $\mu$  and  $\sigma >$ 0 are predictable processes with  $\sigma$  bounded and  $\mathbb{E}\big[e^{1/2\int_0^T(\mu_t/\sigma_t)^2\mathrm{d}t}\big] < \infty. \text{ Let } (\delta^A, \delta^B) \text{ be an SFTS}$ with  $\delta^A$  bounded. Set  $C := \delta^A A + \delta^B B$ . We claim that  $\delta^A = \delta^B = 0$  if  $C_T = 0$ . Indeed, the process

$$M := \mathcal{E}\left(-\int \frac{\mu}{\sigma} \mathrm{d}Z\right) = \mathrm{e}^{-\int \frac{\mu}{\sigma} \mathrm{d}Z - \frac{1}{2} \int \left(\frac{\mu}{\sigma}\right)^2 \mathrm{d}t} \tag{47}$$

is then a positive martingale with  $M_0 = 1$ . Define the equivalent probability measure  $\mathbb{Q}$  by  $d\mathbb{Q} = M_T d\mathbb{P}$ . The process  $W := Z + \int \frac{\mu}{\sigma} dt$  is a Q-Brownian motion because  $[W]_t = t$  and W is  $\mathbb{Q}$ -local martingale as  $MW$  is a local martingale using Itô's product rule:

$$\begin{aligned} \mathsf{d}(MW) - W \mathsf{d}M &= M \mathsf{d}W + \mathsf{d}[W, M] \\ &= M \left( \mathsf{d}Z + \frac{\mu}{\sigma} \mathsf{d}t \right) - M \frac{\mu}{\sigma} \mathsf{d}[Z] \\ &= M \mathsf{d}Z \end{aligned} \tag{48}$$

Moreover,  $dX = X \sigma dW$  by equation (46). Therefore, X is a  $\mathbb{Q}$ -square integrable martingale since  $\sigma$ is bounded. The claim, thus, follows by the section Uniqueness.

Assume now that  $\sigma_t$  is *deterministic*. The results of the section Deterministic-Volatility Exchange Option Model hold since  $d[\log X] = \sigma_t^2 dt$ . However, we can now derive them more conceptually. Indeed, both conditioned on  $\mathcal{F}_t$  and unconditionally,  $X_T/X_t$  is  $\mathbb{Q}$ lognormally distributed with mean 1 and log-variance  $\int_t^T \sigma_s^2 \text{d}s$  since  $X_T = X_t e^{\int_t^T \sigma_s \text{d}W_s - 1/2 \int_t^T \sigma_s^2 \text{d}s}$ . Hence, bv equation  $(45)$ .

$$f(t, X_t) = \mathbb{E}^{\mathbb{Q}}[(X_T - 1)^+ | \mathcal{F}_t] \quad \text{where}$$
$$f(t, x) := \mathbb{E}^{\mathbb{Q}}\left(x\frac{X_T}{X_t} - 1\right)^+ \tag{49}$$

which function readily equals the Black-Scholes/ Merton option price function (6). Thus,  $F :=$  $(f(t, X_t))$  is a  $\mathbb{Q}$ -martingale. Therefore, Itô's formula implies that  $f(t, x)$  satisfies the PDE (9) and d $F = \delta^A$ d $X$  where  $\delta^A := \frac{\partial f}{\partial x}(t, X_t)$ . Numéraire invariance now yields that the pair  $(\delta^A, \delta^B) := F \delta^A X$ ) is an SFTS. Clearly,  $C_T = (A_T - B_T)^+$  where  $C := \delta^A A + \delta^B B = BF.$ 

### Exponential-Poisson Model Uniqueness

Let  $\beta \neq 0$  be a constant and  $\kappa$  and  $\lambda$  be positive continuous adapted processes such that  $\lambda$  is bounded and  $\mathbb{E} e^{\int_0^T \left(\frac{\lambda_t}{\kappa_t} - 1\right)^2 \kappa_t dt} < \infty. \text{ Let } P \text{ be semimartingale sat-}$ isfying  $[P] = P$  with  $P_0 = 0$  and compensator  $\int \kappa dt$ . Assume that  $A$  and  $B$  are positive semimartingales with positive left limits and  $X := \frac{A}{B}$  satisfies

$$dX_t = X_{t-}(e^{\beta} - 1)(dP_t - \lambda_t dt) \tag{50}$$

Using  $de^{\beta P} = (e^{\beta} - 1)e^{\beta P} dP$  or as in the section Derivation of the Predictable Representation, this is equivalent to the integrated form

$$X_t = X_0 e^{\beta P_t - (e^{\beta} - 1) \int_0^t \lambda_s \mathrm{d}s} \tag{51}$$

Let  $(\delta^A, \delta^B)$  be an SFTS with  $\delta^A$  bounded. Set  $C := \delta^A A + \delta^B B$ . We claim that  $\delta^A = \delta^B =$  $0 \text{ if } C_T = 0. \quad \text{Indeed, } \quad \mathbb{E} \left\langle \int \left( \frac{\lambda}{K} - 1 \right)^{(\mathrm{d}P - \kappa \, \mathrm{d}t)} \right\rangle_T = \mathbb{E}$  $e^{\int_0^T \left(\frac{\lambda_t}{\kappa_t} - 1\right)^2 \kappa_t dt} < \infty$ , so the positive local martingale

$$M := \mathcal{E}\left(\int \left(\frac{\lambda}{\kappa} - 1\right) (\mathrm{d}P - \kappa \mathrm{d}t) \right)$$
  
=  $\mathrm{e}^{-\int (\lambda - \kappa) \mathrm{d}t} \prod_{s \leq \cdot} \left(1 + \left(\frac{\lambda_s}{\kappa_s} - 1\right) \Delta P_s\right)$  (52)

is a martingale. Define the equivalent probability measure  $\mathbb{Q}$  by  $\mathrm{d}\mathbb{Q} = M_T \mathrm{d}\mathbb{P}$ . Then  $N := P - \int \lambda \mathrm{d}t$ is a  $\mathbb{Q}$ -local martingale as *MN* is a local martingale by Itô's product rule:

$$\begin{aligned} \mathrm{d}(MN) - N_{-}\mathrm{d}M &= M_{-}\mathrm{d}N + \mathrm{d}[M,N] \\ &= M_{-}(dP - \lambda \mathrm{d}t) \\ &+ M_{-} \left(\frac{\lambda}{\kappa} - 1\right) \mathrm{d}P \\ &= M_{-} \frac{\lambda}{\kappa} (\mathrm{d}P - \kappa \mathrm{d}t) \end{aligned} \tag{53}$$

Therefore, by equation (50), X is a  $\mathbb{Q}$ -squareintegrable martingale (in fact, in  $\mathcal{H}^p(\mathbb{Q})$  for all  $p > 0$ ) since  $\lambda$  is bounded. Thus, by the section Uniqueness,  $\delta^A = \delta^B = 0$  if  $C_T = 0$ , as claimed.

Assume now that  $\lambda$  is a positive constant. By equation  $(51)$  we have a special case of the exponential-Poisson model. Further,  $P$  is a  $\mathbb{Q}$ -Poisson process with intensity  $\lambda$  since  $[P] = P$ . We now have uniqueness, but additionally, the previous results follow more conceptually as follows.

Conditioned on  $\mathcal{F}_t$ ,  $P_T - P_t$  is Q-Poisson distributed with mean  $\lambda(T-t)$ . Its unconditional  $\mathbb{Q}$ distribution is identical. Thus, the  $\mathcal{F}_t$ - conditional and the unconditional  $\mathbb{Q}$ -distribution of  $X_T/X_t$  are identical and are exponentially Poisson distributed with mean 1. Hence, by equation  $(45)$ ,

$$f(t, X_t) = \mathbb{E}^{\mathbb{Q}}[(X_T - 1)^+ | \mathcal{F}_t] \quad \text{where}$$
  
$$f(t, x) := \mathbb{E}^{\mathbb{Q}}\left(x\frac{X_T}{X_t} - 1\right)^+$$
(54)

which function readily equals that defined in equation (16). Thus,  $F := (f(t, X_t))$  is a  $\mathbb{Q}$ -martingale. Using this and equation  $(24)$ , one shows that  $F$  satisfies equation (32) and with it that the pair  $(\delta^A, \delta^B)$  as defined in equation  $(19)$ , equation  $(20)$  is a bounded SFTS for the exchange option.

## Extension to Dividends

Consider two assets with positive price processes  $\hat{A}$ and  $\hat{B}$  and continuous dividend yields  $y_t^A$  and  $y_t^B$ . When there exist traded or replicable zero-dividend assets A and B such that  $A_T = \hat{A}_T$  and  $B_T = \hat{B}_T$  (if not, there is little hope of replication), it is natural to define the price process of the option to exchange  $\hat{A}$ and  $\hat{B}$  to be that of the option to exchange A and B. If  $y^A$  and  $y^B$  are deterministic, then consistent with the treatment of dividends in [9],  $A$  (and similarly  $B$ ) is simply given by

$$A_t := a\tilde{A}_t = e^{-\int_t^T y_s^A ds} \hat{A}_t,$$
  
$$\tilde{A}_t := e^{\int_0^t y_s^A ds} \hat{A}_t, \quad a := e^{-\int_0^T y_t^A dt}$$
(55)

Note  $A/B$  is a semimartingale if and only if  $\hat{A}/\hat{B}$ is, in which case  $\lceil \log A/B \rceil = \lceil \log \hat{A}/\hat{B} \rceil$ .

In general,  $\tilde{A}_t$  is the price of the zero-dividend asset that initially buys one share of  $\hat{A}$  and thereon continually reinvests all dividends in  $\hat{A}$  itself. What is required is that the four zero-dividend assets  $A$ ,  $\tilde{A}$ . B, and  $\tilde{B}$  be arbitrage free in relation to one another (see the section Arbitrage-free Semimartingales and Uniqueness).

For instance, say  $\hat{A}$  and  $\hat{B}$  are the yen/dollar and yen/Euro exchange rates viewed as yen-denominated dividend assets. Then  $A$  is the yen-value of the US  $T$ maturity zero-coupon bond and  $\tilde{A}$  is the yen-value of the US money market asset. This exchange option is equivalent to a Euro-denominated call struck at 1 on the Euro/dollar exchange rate  $\hat{A}/\hat{B}$ . The ratio  $A/B$ is the *forward* Euro/dollar exchange rate. If it has deterministic volatility, we are as in a setting of [7], which yields the same pricing formula as that from the section Deterministic-volatility Exchange Option Model.

# **Pricing and Hedging Options with Homogeneous Payoffs**

We took some shortcuts to quickly present the main results for two of the simplest and among the most interesting examples. A better understanding of the principles at work requires generalization to contingent claims  $C$  on many assets with price processes  $A = (A^1, \cdots, A^m) > 0$ and a path-independent payoff  $C_T = h(A_T)$  given as a homogeneous function  $h(a)$ ,  $a \in \mathbb{R}^m_+$ , of the asset prices  $A_T$  at expiration time T. Combined with an underlying SDE and the resulting PDE, such a Markovian setting utilizes the invariance principle and equivalent martingale measures to derive unique pricing and construct an SFTS that replicates the given payoff  $h(A_T)$  in general. The construction is explicit in the multivariate extensions of the deterministic-volatility and exponential-Poisson models.

The homogeneity of the payoff function  $h(a)$ implies  $h(A_T) = A_T^m g(X_T)$  where  $g(x) := h(x, 1)$ ,  $x \in \mathbb{R}^n_+, \quad n := m-1, \quad \text{and} \quad X := \left(\frac{A^1}{A^m}, \cdots, \frac{A^n}{A^m}\right).$ Once a predictable representation  $F = F_0 + \delta'$ .  $X$ ,  $F_T = g(X_T)$  is found, then by numéraire invariance  $\delta := (\delta', \delta^m)$  will be an SFTS with payoff  $h(A_T)$ , where  $\delta^m := F_- - \sum_{i=1}^n \delta^i X_- =$  $F - \sum_{i=1}^{n} \delta^{i} X$ . Uniqueness of pricing requires boundedness of partial derivatives (or differences) of  $h(a)$  (or  $g(x)$ ) and that A be arbitrage free, meaning  $X$  is a martingale under an equivalent measure. Arbitrage freedom holds "generically" when the matrix ( $(X^i, X^j)$ ) is nonsingular, basically a "noredundant-asset" condition. Then the SFTS is also unique.

Libor and swap derivatives are among contingent claims with homogeneous payoffs.

## Self-financing Trading Strategies

By an SFTS we mean a pair  $(\delta, A)$  of an mdimensional semimartingale  $A = (A^1, \ldots, A^m)$  and an A-integrable predictable vector process  $\delta =$  $(\delta^1,\ldots,\delta^m)$  such that (with  $\delta\cdot A$  denoting the *m*dimensional stochastic integral)

$$\sum_{i=1}^{m} \delta^{i} A^{i} = \sum_{i=1}^{m} \delta^{i}_{0} A^{i}_{0} + \delta \cdot A \tag{56}$$

We then say  $\delta$  is an SFTS for A. This is equivalent to saying that the SFTS *price process* 

$$C := \sum_{i=1}^{m} \delta^{i} A^{i} \tag{57}$$

satisfies  $C = C_0 + \delta \cdot A$ . Clearly, C is then a semimartingale,  $\Delta C = \sum_i \delta^i \Delta A_i$ , and hence

$$C_{-} = \sum_{i=1}^{m} \delta^{i} A_{-}^{i} \tag{58}$$

If  $\delta^i$  are bounded (say by b) and  $A^i$  are martingales, then the SFTS price process  $C$  is a martingale because  $C$  is then a local martingale that is dominated by a martingale  $M$ :

$$|C_{t}| \leq b \sum_{i} |A_{t}^{i}| = b \sum_{i} |\mathbb{E}[A_{T}^{i} | \mathcal{F}_{t}]|$$
  
$$\leq b \sum_{i} \mathbb{E}[|A_{T}^{i}| | \mathcal{F}_{t}] =: M_{t}$$
  
(59)

As suggested by the case of a locally bounded  $\delta$ , we often use the differential form

$$dC = \sum_{i=1}^{m} \delta^{i} dA^{i} \tag{60}$$

of the equation  $C = C_0 + \delta \cdot A$  as a convenient symbolic equivalent in calculations. One interprets  $A^{i}$  as prices of *m* zero-dividend assets and  $\delta^{i}$  as the number of shares invested in them at time  $t$ . Then  $C_t$ indicates the resultant self-financing portfolio price by equation  $(57)$ , and equation  $(60)$  is the selffinancing equation, implying that the change  $dC$ in the portfolio price is only due to the changes  $dA^{i}$  in the asset prices with no financing from outside.

Assume for the remainder of this subsection as a way of motivation that A is continuous and  $C_t =$  $c(t, A_t)$  for some  $C^{1,2}$  function  $c(t, a)$ .<sup>a</sup> Then by equation (60) and Itô's formula, we have

$$\frac{\partial c}{\partial t}(t, A_t) dt + \frac{1}{2} \sum_{i,j=1}^{m} \frac{\partial^2 c}{\partial a_i \partial a_j}(t, A_t) d[A^i, A^j]_t$$
$$= \sum_{i=1}^{m} \left(\delta^i_t - \frac{\partial c}{\partial a_i}(t, A_t)\right) dA^i_t \quad (61)$$

In particular, if  $\delta_t^i = \frac{\partial c}{\partial a_i}(t, A_t)$  for all *i* then  $c(t, A_t) = \sum_i \frac{\partial c}{\partial a_t}(t, A_t) A_t^i$  by equation (57) and

$$\frac{\partial c}{\partial t}(t, A_t)dt + \frac{1}{2} \sum_{i,j=1}^{m} \frac{\partial^2 c}{\partial a_i \partial a_j}(t, A_t) d[A^i, A^j]_t = 0$$
(62)

In general,  $\sum_{i,j} \left( \delta^i - \frac{\partial c}{\partial a_i} \right) \left( \delta^j - \frac{\partial c}{\partial a_j} \right) d[A^i,$  $A^{j}$  = 0 since the (left) right-hand side of equation

(61) has finite variation. Thus, if  $[A^i]$  are absolutely continuous and the  $m \times m$  matrix  $(d/dt[A^i, A^j])$ is nonsingular, then  $\delta^i_t = \partial c/\partial a_i(t, A_t)$ , so equation (62) holds and  $c(t, A_t) = \sum_i \partial c / \partial a_i(t, A_t) A_t^i$ . If further the support of  $A_t$  is a cone, it follows  $c(t, a)$  is homogeneous of degree 1 in a on that cone.

Assume that  $M^{i} := e^{-\int r dt} A^{i}$  are local martingales under an equivalent measure for some locally bounded predictable process r. Then  $dA^{i} = rA^{i}dt +$  $e^{\int r dt} dM^{i}$ ; thus, by equations (61) and (57)

$$\frac{\partial c}{\partial t}(t, A_t) dt + \frac{1}{2} \sum_{i,j=1}^{m} \frac{\partial^2 c}{\partial a_i \partial a_j}(t, A_t) d[A^i, A^j]_t$$
$$= r_t \left( C_t - \sum_{i=1}^{m} \frac{\partial c}{\partial a_i}(t, A_t) A_t^i \right) dt \tag{63}$$

Hence, if  $c(t, a)$  is homogeneous (in a), then by Euler's formula equation (62) holds (yet  $\delta^i$  may differ from  $\partial c/\partial a_i(t, A_t)$  if there are redundancies, for then a regular replicating SFTS is not unique).

Given a homogeneous payoff function  $h(a)$ , the section Homogeneous Continuous Markovian SFTS constructs under suitable assumptions a homogeneous solution  $c(t, a)$  to equation (62) with  $c(T, a) =$  $h(a)$ . Clearly then, by Euler and Itô formulae,  $(\partial c/\partial a_i(t, A_t))$  is an SFTS for A (as observed in [9] and highlighted in [8], see the section The Homogeneous Option Price Function). To this end, we first factor out the homogeneous symmetry of  $h(a)$ next.

#### The Invariance Principle

Let  $(\delta, A)$  be an SFTS and S a (scalar) semimartingale such that  $\delta$  is  $SA := (SA^1, \cdots, SA^m)$ -integrable. Then  $(\delta, SA)$  is an SFTS. Consequently,

$$d(SC) = \sum_{i=1}^{m} \delta^{i} d(SA^{i}) \tag{64}$$

where  $C := \sum_i \delta^i A^i = C_0 + \delta \cdot A$ , that is,  $SC =$  $S_0C_0 + \delta \cdot (SA)$ . Indeed, by Itô's product rule, then substituting for  $dC$  and  $C_{-}$  and regrouping, followed by Itô's product rule again,

$$d(SC) = S_{-}dC + C_{-}dS + d[S, C]$$
  
=  $S_{-}\sum_{i=1}^{m} \delta^{i} dA^{i} + \sum_{i=1}^{m} \delta^{i} A^{i}_{-} dS + \sum_{i=1}^{m} \delta^{i} d[S, A^{i}]$   
=  $\sum_{i=1}^{m} \delta^{i} (S_{-}dA^{i} + A^{i}_{-}dS + d[S, A^{i}])$   
=  $\sum_{i=1}^{m} \delta^{i} d(SA^{i})$  (65)

Interpreting  $S$  as an exchange rate, this result [3, 4, 8], called *numéraire invariance*, means that the self-financing property is independent of the base currency. (To the best of our knowledge, the term was coined in the 1992 edition of  $[3]$ , where a similar proof is given.)

If S,  $S_{-} > 0$ , then applied to the semimartingale  $1/S$  we see that  $\delta$  is an SFTS for A if and only if it is one for SA. Thus, if equation (57) holds, then equations  $(60)$  and  $(64)$  are equivalent.

Assume now that  $A^m$ ,  $A^m_- > 0$  and  $m \ge 2$ . Define the  $n := m - 1$  dimensional semimartingale

$$X := \left(\frac{A^{1}}{A^{m}}, \dots, \frac{A^{n}}{A^{m}}\right), \quad n := m - 1 \tag{66}$$

Taking  $S = 1/A^m$ , it follows that  $\delta$  is an SFTS for A if and only if it is an SFTS for  $A/A^m = (X, 1)$ , that is, if and only if  $F := C/A^m$  satisfies  $F = F_0 +$  $\delta' \cdot X$  where  $\delta' := (\delta^1, \dots, \delta^n)$ . Clearly in this case,  $F = \sum_{i=1}^n \delta^i X^i + \delta^m$  and  $F_- = \sum_{i=1}^n \delta^i X_-^i + \delta^m$  as  $\Delta F = \dot{\delta}' \cdot \Delta X$ . Thus,

$$\delta^{m} = F - \sum_{i=1}^{n} \delta^{i} X^{i} = F_{-} - \sum_{i=1}^{n} \delta^{i} X_{-}^{i}, \ \left( F := \frac{C}{A^{m}} \right)$$
(67)

(When  $m = 1$ , a similar argument shows that  $\delta$ must be a constant, as intuitively obvious.)

Conversely, suppose that  $\delta'$  is an X-integrable process and F is a process such that  $F = F_0 + \delta' \cdot X$ . Define  $\delta^m$  by either of the above formulas—the other then holds as before. Obviously then  $\delta = (\delta', \delta^m)$  is an SFTS for  $(X, 1)$  with price process F. Hence by

numéraire invariance,  $\delta$  is an SFTS for A with price process  $C = A^m F$ , provided  $\delta$  is A-integrable.

Thus, numéraire invariance shows that in order to find an SFTS with a given time-T payoff  $C_T$  it is sufficient to find processes  $\delta'$  and F such that  $F = F_0 + \delta' \cdot X$  and  $F_T = C_T / A_T^m$ .

Since  $\delta^m = F - \sum_{i=1}^n \delta^i X^i$ , the *m*th delta  $\delta^m$  is like F determined by  $\delta'$  and  $F_0$ . As such, one interprets the  $m$ -th asset as the "numéraire asset" chosen to finance an otherwise arbitrary trading strategy  $\delta'$ in the other assets, post an initial investment of  $C_0 = A_0^m F_0.$ 

We often use the differential form  $dF = \sum_{i=1}^{n} \delta^{i}$  $\mathrm{d}X^i$  of the equation  $F = F_0 + \delta' \cdot X$ .

### Arbitrage-free Semimartingales and Uniqueness

We call a semimartingale  $A = (A^1, \dots, A^m), m > 2,$ *arbitrage free* if there exists a positive semimartingale S with  $S_{-} > 0$  such that  $SA^{i}$  are martingales for all  $i$ . Such a process S is called a *state price density* or *deflator* for A. The *law of one price* (with bounded deltas) justifies the terminology:

If A is arbitrage free and  $\delta$  is a bounded SFTS for A, then SC is a martingale where  $C := \sum_{i=1}^{m} \delta^{i} A^{i}$ ; consequently,  $C = 0$  if  $C_T = 0$ .

Indeed, by numéraire invariance  $\delta$  is then an SFTS for  $SA$  with price process  $SC$ . Hence by the section Self-financing Trading Strategies, SC is a martingale, implying  $SC = 0$  if  $C_T = 0$ , and with it  $C = 0$ , as claimed.

A simple and well-known argument yields that if  $A^m, A^m > 0$ , then A is arbitrage free if and only if there exists an equivalent probability measure  $\mathbb{Q}$  such that X is a  $\mathbb{Q}$ -martingale, where  $X :=$  $\left(\frac{A^1}{A^m}, \cdots \frac{A^n}{A^m}\right)$ ,  $n := m - 1$ .<sup>b</sup> Numéraire invariance then implies that  $C/A^m$  is a  $\mathbb{Q}$ -martingale for the price process  $C := \sum_i \delta^i A^i$  of any bounded SFTS  $\delta$ , and hence

$$C_t = A_t^m \mathbb{E}^{\mathbb{Q}} \left[ \frac{C_T}{A_T^m} \, | \, \mathcal{F}_t \right] \tag{68}$$

Indeed, by numéraire invariance,  $\delta$  is an SFTS for  $A/A^m$  with price process  $C/A^m$ . Hence,  $C/A^m$  is a Q-martingale by the section Self-Financing Trading Strategies since  $A/A^m$  is a  $\mathbb{Q}$ -martingale and  $\delta$  is bounded.

Suppose that  $X$  is a  $\mathbb{Q}$ -square-integrable martingale and  $\delta^i$  are bounded for  $i \leq n$ . Then  $F := C/A^m$  is a  $\mathbb{Q}$ -square-integrable martingale since  $dF = \sum_{i=1}^{n} \delta^{i} dX^{i}$  by numéraire invariance.<br>Moreover,  $d\langle F \rangle^{\mathbb{Q}} = \sum_{ij=1}^{n} \delta^{i} \delta^{j} d\langle X^{i}, X^{j} \rangle^{\mathbb{Q}}$ . Thus, *if*  $(X^i)^{\mathbb{Q}}$  are absolutely continuous and the  $n \times n$  matrix  $(\mathrm{d}/\mathrm{d}t\langle X^i,X^j\rangle^{\mathbb{Q}})$  is nonsingular, then given any random variable  $R$ , there exists at most one SFTS  $\delta$  for A such that  $\sum_{i=1}^{m} \delta^{i}_{T} A^{i}_{T} = R$  and  $\delta^{i}$  are bounded for  $i < n$ .

## Projective Continuous Markovian SFTS

Let  $X = (X^1, \dots, X^n)$  be a continuous vector martingale. In this, subsection  $x \in \mathbb{R}^n_+$  if  $X > 0$  (the main case of interest); otherwise,  $x \in \mathbb{R}^n$ . Let  $g(x)$  be a Borel function of linear growth (so  $\mathbb{E}|g(X_T)| < \infty$ ), and  $f(t, x)$  be a continuous function,  $C^{1,2}$  on  $t < T$ . Set  $m := n + 1$  and define the  $C^1$  functions

$$\delta_i(t,x) := \frac{\partial f}{\partial x_i}(t,x), \ i \le n,$$
  
$$\delta_m(t,x) := f(t,x) - \sum_{i=1}^n \delta_i(t,x)x_i \qquad (69)$$

and the continuous vector process

$$\delta = (\delta^1, \dots, \delta^m), \quad \delta^i_t := \delta_i(t, X_t) \tag{70}$$

First suppose that

$$f(t, X_t) = \mathbb{E}[g(X_T) | \mathcal{F}_t]$$
(71)

Then the process  $F := (f(t, X_t))$  is a martingale, and since  $X^i$  are also martingales, Itô's formula yields

$$dF_t = \sum_{i=1}^n \frac{\partial f}{\partial x_i}(t, X_t) dX_t^i, \qquad (72)$$

and

$$\frac{\partial f}{\partial t}(t, X_t) \mathrm{d}t + \frac{1}{2} \sum_{i, j=1}^n \frac{\partial^2 f}{\partial x_i \partial x_j}(t, X_t) \mathrm{d}[X^i, X^j]_t = 0 \tag{73}$$

Clearly,  $F_T = g(X_T)$  and equation (72) imply  $\delta$  is an SFTS for  $(X, 1)$  with price process F.

Conversely, suppose that  $f(t, x)$  satisfies equation (73) or equivalently, by Itô's formula, equation (72). By equation (72),  $\delta$  is an SFTS for  $(X, 1)$  with price process  $F := f(t, X_t)$ . Thus by the section Self-financing Trading Strategies, if  $\delta_i(t, x)$ are bounded then  $F$  is a martingale and if further  $f(T, x) = g(x)$  then equation (71) holds. Moreover, as in the section Arbitrage-free Semimartingales and Uniqueness,  $\delta$  given by equation (70) is then the

*unique* bounded SFTS for  $(X, 1)$  with payoff  $g(X_T)$ , provided  $d[X^i, X^j] = X^i X^j \sigma^{ij} dt$  for some nonsingular matrix process  $(\sigma_t^{ij})$ .

## Example: Projective Deterministic Volatility

Let  $X = (X^1, \ldots, X^n) > 0$  be a continuous *n*dimensional martingale such that

$$d[X^i, X^j]_t = X^i_t X^j_t \sigma_{ij}(t) dt \tag{74}$$

for some  $n^2$  deterministic continuous functions  $\sigma_{ii}(t)$ . So,  $d[\log X^i, \log X^j]_t = \sigma_{ii}(t)dt$ . Conditioned on  $\mathcal{F}_t$ and unconditionally,  $X_T/X_t$  is then *multivariately* lognormally distributed, with mean  $(1, \dots, 1)$  and log-covariance matrix  $(\int_t^T \sigma_{ij}(s) ds)$ . Let  $P(t, T, z)$ denote its distribution function. Let  $g(x)$  be a Borel function of linear growth. Define the function

$$f(t,x) := \mathbb{E}\left[g\left(x_1\frac{X_T^1}{X_t^1},\ldots,x_n\frac{X_T^n}{X_t^n}\right)\right] \tag{75}$$

Obviously,  $f(T, x) = g(x)$ . Clearly,  $f(t, x)$  can also be represented in two other ways as

í

$$f(t,x) = \int_{\mathbb{R}^n_+} g(x_1 z_1, \dots, x_n z_n) P(t, T, dz)$$
$$= \mathbb{E}\left[g\left(x_1 \frac{X_T^1}{X_t^1}, \dots, x_n \frac{X_T^n}{X_t^n}\right) \mid \mathcal{F}_t\right] \tag{76}$$

Equation (71) holds by the second equality, and  $f(t, x)$  is  $C^1$  in t and smooth (even analytic) in x on  $t < T$  as seen by changing variable in the integral to  $y^i = x^i z^i$  and differentiating under the integral sign in the first equality. Therefore by equation  $(73)$ ,  $f(t, x)$  satisfies the PDE

$$\frac{\partial f}{\partial t} + \frac{1}{2} \sum_{i,j=1}^{n} \sigma_{ij}(t) x_i x_j \frac{\partial^2 f}{\partial x_i \partial x_j} = 0 \qquad (77)$$

on the support of X, equation (72) holds, and  $\delta$  is an SFTS for  $(X, 1)$  with price process  $F := (f(t, X_t)),$  a martingale by equation (71). If  $g(x)$  is dx-absolutely continuous with bounded partial derivatives  $\frac{\partial g}{\partial x_i}$ (as  $L^1$  functions), then  $g(x)$  has linear growth,  $\mathbb{E}|g(X_T)|^p < \infty$  for  $p > 0$ , and

$$\frac{\partial f}{\partial x_i}(t,x) = \mathbb{E}\left[\frac{X_T^i}{X_t^i}\frac{\partial g}{\partial x_i}\left(x_1\frac{X_T^1}{X_t^1},\dots,x_n\frac{X_T^n}{X_t^n}\right)\right] \tag{78}$$

Thus,  $\delta_i(t, x) = \frac{\partial f}{\partial x_i}(t, x)$  are bounded. If  $g(x)$  –  $\sum \frac{\partial g}{\partial x_i} x_i$  is bounded, then so is  $\delta_m(t, x)$  as

$$\delta_m(t,x) = \mathbb{E}\left[g\left(x\frac{X_T}{X_t}\right) - \sum_{i=1}^n \frac{\partial g}{\partial x_i} \left(x\frac{X_T}{X_t}\right) \frac{X_T^i}{X_t^i}\right] \tag{79}$$

It further follows that if  $f(t, x)$  is any  $C^{1,2}$ function with bounded partials  $\frac{\partial f}{\partial x_i}(t, x)$  satisfying  $f(T, x) = 0$  for all  $x$  and the PDE (77), then  $F :=$  $(f(t, X_t)) = 0$ . Indeed, equation (72) then holds by PDE (77) and Itô's formula, implying  $F$  is a squareintegrable martingale. Thus  $F = 0$  since  $F_T = 0$ . As such,  $f(t, x) = 0$  identically if the support of  $X_t$ equals  $\mathbb{R}^n_+$  for every t. This is so if the matrix  $(\sigma_{ii}(t))$ is nonsingular at least near 0, and it is "generically" so even when the matrix has rank 1 but is time dependent.

#### Projective Continuous SDE SFTS

Continuous Markovian positive martingales  $X =$  $(X^1,\cdots,X^n)$  often arise as solutions to an SDE system of the form

$$\mathrm{d}X_t^i = X_t^i \sum_{j=1}^k \varphi_{ij}(t, X_t) \mathrm{d}W_t^j \tag{80}$$

where  $W^1, \cdots, W^k$  are independent Brownian motions and  $\varphi_{ij}(t, x)$ ,  $x \in \mathbb{R}^n_+$ , are continuous bounded functions. As is well known, for each  $s \leq T$  and  $x \in \mathbb{R}^n_+$ , there is a unique continuous semimartingale  $X^{s,x} = (X^{s,x}_t)$  on  $[s,T]$  with  $X^{s,x}_s =$ x satisfying this SDE; moreover,  $X^{s,x}$  is a positive square-integrable martingale (in fact in all  $\mathcal{H}^p$ ) since  $\varphi_{ij}(t, x)$  are bounded. Fixing an  $X_0 \in \mathbb{R}^n_+$ , the solution on  $[0, T]$  starting at  $X_0$  at time 0 is denoted as  $X = X^{0, X_0}$ . The Markov property holds: for any Borel function  $g(x)$  of linear growth,

$$\mathbb{E}[g(X_T) | \mathcal{F}_t] = f(t, X_t) \quad \text{where}$$
$$f(t, x) := \mathbb{E} g(X_T^{t, x}) \tag{81}$$

Clearly  $f(T, x) = g(x)$ . (Intuitively,  $f(t, x) =$  $\mathbb{E}[g(X_T) | X_t = x].$ 

Thus if we assume that  $\varphi_{ij}(t, x)$  are sufficiently regular so that  $f(t, x)$  is  $C^{1,2}$  on  $t < T$  for every

bounded (hence of linear growth) Borel function  $g(x)$ , then the assumptions of the section Projective Continuous Markovian SFTS are satisfied and the conclusions hold. In particular, equation (72) then holds, and since

$$d[X^{i}, X^{j}] = X^{i}X^{j}\sigma_{ij}(t, X)dt \text{ where}$$
  

$$\sigma_{ij}(t, x) := \sum_{l=1}^{k} \varphi_{il}(t, x)\varphi_{jl}(t, x) \qquad (82)$$

it follows from equation  $(73)$  that, at least on the support of X,  $f(t, x)$  satisfies the PDE

$$\frac{\partial f}{\partial t}(t,x) + \frac{1}{2} \sum_{i,j=1}^{n} x_i x_j \sigma_{ij}(t,x) \frac{\partial^2 f}{\partial x_i \partial x_j}(t,x) = 0$$
(83)

In the deterministic-volatility case, the functions  $\varphi_{ij}$  and hence  $\sigma_{ij}$  are independent of x and simply  $X_T^{i,x} = xX_T/X_t$ , explaining why in this special case  $f(t, x)$  is also given by equation (73).

In general, if  $g(x)$  is absolutely continuous with bounded derivatives and the probability transition function of  $X$  is sufficiently regular, one shows, as in the deterministic volatility case, that the  $x$ -partial derivatives of  $f$  (the deltas) are bounded and thereby concludes uniqueness.

If  $\sigma_{ii}(t, x)$  are homogeneous of degree 0 in x, then (assumed) uniqueness and symmetry of PDE (73) under dilation in x imply that  $f(t, x)$  is homogeneous of degree 1 in x if  $g(x)$  is so. By Euler's formula then  $\delta_m(t,x) = 0$  in equation (69), implying  $(\delta^1,\cdots,\delta^n)$ is an SFTS for  $X$ .

#### Homogeneous Continuous Markovian SFTS

Let  $A = (A^1, \dots, A^m)$  be a semimartingale with  $A, A_{-} > 0$  such that  $X^{i} := A^{i}/A^{m}$  are Itô processes following

$$dX_t^i = X_t^i \sum_{j=1}^k \varphi_t^{ij} (dZ_t^j + \phi^j dt)$$
  
(*i* = 1, ..., *n* := *m* - 1) (84)

where  $Z^j$  are independent Brownian motions and  $\phi^j$ ,  $\varphi^{ij}$  are locally bounded predictable processes with  $\varphi^{ij}$  bounded and  $\mathbb{E} e^{1/2 \sum_j \int_0^T (\phi_t^j)^2 dt} < \infty$ . Define the martingale

$$M := \mathcal{E}\left(-\sum_{j=1}^{k} \int \phi^{j} \mathrm{d}Z^{j}\right)$$
$$= \mathrm{e}^{-\sum_{j=1}^{k} \left(\int \phi^{j} \mathrm{d}Z^{j} + \frac{1}{2} \int (\phi^{i})^{2} \mathrm{d}t\right)} \tag{85}$$

and the measure  $\mathbb{Q}$  by  $d\mathbb{Q} = M_T d\mathbb{P}$ . Then  $W^i :=$  $Z^{i} + \int \phi^{i} dt$  are Q-Brownian motions and are Qindependent since  $[W^k, W^l] = 0$  for  $k \neq l$ . Hence,  $X^i$  are  $\mathbb{Q}$ -square-integrable martingales as  $dX^i =$  $X^i \sum_{j=1}^k \varphi^{ij} \mathrm{d}W^j$  and  $\varphi^{ij}$  are bounded. Thus, A is arbitrage free.

Now let  $h(a)$ ,  $a \in \mathbb{R}^m_+ > 0$ , be a homogeneous function of linear growth. Define  $g(x) := h(x, 1)$ ,  $x \in \mathbb{R}^n_+$ . Assume further that  $\varphi_t^{ij} = \varphi_{ij}(t, X_t)$  for some continuous bounded functions  $\varphi_{ij}(t, x)$ . Then equation (80) holds, and hence the section Projective Continuous SDE SFTS applied under measure  $\mathbb{Q}$  shows that X is  $\mathbb{Q}$ -Markovian in that  $\mathbb{E}^{\mathbb{Q}}[g(X_T) | \mathcal{F}_t] := f(t, X_t)$  where  $f(t, x) =$  $\mathbb{E}^{\mathbb{Q}}g(X^{t,x}_T)$ , as in equation (81). Thus, by the section Projective Continuous SDE SFTS, equations (72) and (73) hold and  $\delta$  as defined in equation (70) is an SFTS for  $(X, 1)$ . Therefore by numéraire invariance,  $\delta$  is an SFTS for A with price process  $C = A^m F$ . The homogeneity of  $h(a)$  further implies  $C_T = A_T^m g(X_T) = h(A_T).$ 

We have thus constructed an SFTS with the given *payoff*  $h(A_T)$ . As in the section Example: Projective Deterministic Volatility or Projective Continuous SDE SFTS, we ensure its boundedness by requiring the x-partial derivatives of  $g(x)$  or equivalently *a*-partial derivatives of  $h(a)$  (as  $L^1_{loc}$  functions) be bounded and thereby get unique pricing. For (very) low dimensions  $n$ , the PDE (83) is suitable for numerical valuation in the absence of a closed-form solution.

Although the option price process and the deltas are already found, let us also consider the homogeneous option price function referred to in the section Self-financing Trading Strategies, and now naturally defined by

$$c(t,a) := a_m f\left(t, \frac{a^1}{a^m}, \dots, \frac{a^n}{a^m}\right) \tag{86}$$

Then  $C_t = c(t, A_t)$ . Agreeably,  $\delta_t^i = \frac{\partial c}{\partial a_i}(t, A_t)$ by equation (69). (For  $i = m$  use Euler's formula for  $c(t, a)$ .) By the continuity of X and equation (69),  $\delta_t^i = \frac{\partial c}{\partial a_i}(t, A_{t-})$  too. Therefore by Itô's formula,

$$\frac{\partial c}{\partial t}(t, A_{t-})dt + \frac{1}{2} \sum_{i,j=1}^{m} \frac{\partial^{2} c}{\partial a_{i} \partial a_{j}}(t, A_{t-}) d[A^{i}, A^{j}]_{t}^{c} = 0$$
(87)

(The term for the sum of jumps in Itô's formula vanishes since  $\Delta C = \sum \delta^i \Delta A^i$ .) This yields the PDE  $\frac{\partial c}{\partial t} + \frac{1}{2} \sum_{i,j} a_i a_j \sigma_{ij}^A(t,a) \frac{\partial^2 c}{\partial a_i \partial a_j} = 0 \text{ for the special}$ case  $d[A^i, A^j]_t = A^i_t A^j_t \sigma^A_{ii}(t, A_t) dt$  for some functions  $\sigma_{ij}^{A}(t, a)$ . The quotient-space PDE (83) is more fundamental for it holds in general (even when  $A$  is discontinuous) and has one lower dimension. Change of variable  $L^{i} = \frac{X^{i}}{X^{i+1}} - 1$   $(i < n), L^{n} = X^{n} - 1,$ transforms equation  $(83)$  to the Libor market model PDE.

### Multivariate Poisson Predictable Representation

Let  $P = (P^1, \dots, P^k)$  be a vector of independent Poisson processes  $P^i$  with intensities  $\lambda_i > 0$ . For any  $C^1$  in t function  $u(t, p)$ ,  $p \in \mathbb{R}^k$ , the process  $u(t, P) = (u(t, P_t))$  is a finite activity semimartingale, and using  $[P^i, P^j] = 0$ , one has  $\Delta u(t, P) =$  $\sum_i \Delta_i u(t, P_-) \Delta P^i$ , where

$$\Delta_i u(t, p) := u(t, p_1, \dots, p_i + 1, \dots, p_n) - u(t, p)$$
(88)

denotes the *i*th forward partial difference of  $u(t, p)$ in  $p$ . This in turn readily implies

$$\mathrm{d}u(t,\,P) = \frac{\partial u}{\partial t}(t,\,P_{-})\mathrm{d}t + \sum_{i=1}^{k} \Delta_{i}u(t,\,P_{-})\mathrm{d}P^{i} \tag{89}$$

Let  $v(p)$ ,  $p \in \mathbb{R}^k$  be a function of exponential linear growth. Define the function

$$u(t,p) := \sum_{q_1,\dots,q_k=0}^{\infty} v(p+q)$$
$$\times \prod_{i=1}^{k} \frac{\lambda_i^{q_i}}{q_i!} (T-t)^{q_i} e^{-\lambda_i (T-t)} \quad (p \in \mathbb{R}^k)$$
(90)

Clearly,  $u(T, p) = v(p)$ . Since the unconditional distribution of  $P_{T-t}$  is Poisson and is the same as the distribution of  $P_T - P_t$  conditioned on  $\mathcal{F}_t$ , we have

$$u(t, p) = \mathbb{E}[v(p + P_T - P_t)]$$
  
= 
$$\mathbb{E}[v(p + P_T - P_t) | \mathcal{F}_t]$$
 (91)

Hence,  $u(t, P_t) = \mathbb{E}[v(P_T) | \mathcal{F}_t].$  (Intuitively,  $u(t, p) = \mathbb{E}[v(P_T) | P_t = p].$  Thus, the process

$$F = (F_t), \quad F_t := u(t, P_t) = \mathbb{E}[v(P_T) \mid \mathcal{F}_t] \quad (92)$$

is a martingale. But so are  $P^j - \lambda_i t$ . Therefore in view of equation  $(89)$ , it follows that

$$dF = \sum_{i=1}^{k} \Delta_i u(t, P_-) d(P^i - \lambda_i t) \qquad (93)$$

and  $u(t, p)$  satisfies the equation

$$\frac{\partial u}{\partial t}(t, P_{t-}) + \sum_{i=1}^{k} \lambda_i \Delta_i u(t, P_{t-}) = 0 \qquad (94)$$

Since  $F_T = v(P_T)$  and  $F_0 = u(0, 0)$ , combining equations (90) and (93) yields the following representation:

$$v(P_T) = \sum_{q_1,\dots,q_k=0}^{\infty} v(q_1,\dots,q_k) \prod_{i=1}^{k} \frac{\lambda_i^{q_i}}{q_i!} T^{q_i} e^{-\lambda_i T}$$
$$+ \sum_{i=1}^{k} \int_0^T \Delta_i u(t,P_{t-}) \mathrm{d}(P_t^i - \lambda_i t) \quad (95)$$

#### Projective Exponential-Poisson SFTS

Let  $P = (P^1, \dots, P^k)$  be a vector of independent Poisson processes  $P^j$  with intensities  $\lambda_j > 0$ . Let  $X_0 \in \mathbb{R}^n_+, n \geq k$ , and  $\beta = (\beta_{ij})$  be an  $n \times k$  matrix such that the  $n \times k$  matrix  $(e^{\beta_{ij}} - 1)$  has full rank. Then the processes  $X^i := (x_i(t, P_t)), i = 1, \dots, n$ , are square-integrable martingales (in fact in all  $\mathcal{H}^p$ ), where

$$x_i(t, p) := X_0^i \exp\left(\sum_{j=1}^k (\beta_{ij} p_j - (\mathrm{e}^{\beta_{ij}} - 1)\lambda_j t)\right)$$
$$(p \in \mathbb{R}^k) \tag{96}$$

Since

$$\frac{\partial x_i}{\partial t}(t, p) = -x_i(t, p) \sum_{j=1}^k (e^{\beta_{ij}} - 1)\lambda_j,$$
  
$$\Delta_j x_i(t, p) = x_i(t, p)(e^{\beta_{ij}} - 1) \tag{97}$$

it follows from equation (89) (or easily also from Itô's formula) that

$$dX^{i} = X^{i}_{-} \sum_{j=1}^{k} (e^{\beta_{ij}} - 1)$$
$$\times d(P^{j} - \lambda_{j}t) \quad (X^{i}_{t} := x_{i}(t, P_{t})) \tag{98}$$

Let  $\alpha = (\alpha_{ij})$  be any  $n \times k$  matrix such that  $\sum_{i} (e^{\beta_{il}} - 1)\alpha_{ij} = \delta_{jl}$ , all  $1 \leq j, l \leq k$ . Then

$$d(P^j - \lambda_j t) = \sum_{i=1}^n \alpha_{ij} \frac{dX^i}{X^i_-}$$
(99)

Now let  $g(x)$ ,  $x \in \mathbb{R}^n_+$ , be a function of linear growth; define the function

$$v(p) := g(x_1(T, p), \dots, x_n(T, p)), \quad (p \in \mathbb{R}^n)$$
(100)

and the function  $u(t, p)$  by equation (90). By the section Multivariate Possion Predictable Representation,  $F := (u(t, P_t))$  is a martingale with  $F_T = v(P_T) = g(X_T)$  and is represented as equation  $(93)$ . Substituting equation  $(99)$  into equation  $(93)$ yields

$$dF = \sum_{i=1}^{n} \delta^{i} dX^{i} \tag{101}$$

where

$$\delta_t^i := \frac{1}{X_{t-}^i} \sum_{j=1}^k \alpha_{ij} \Delta_j u(t, P_{t-}) \qquad (102)$$

Thus,  $\delta = (\delta^1, \dots, \delta^m)$  is an SFTS for  $(X, 1)$ where  $m := n + 1$  and  $\delta^m := F - \sum_{i=1}^n \delta^i X^i$ .

It is more desirable to express  $\delta$  in terms of X. One has  $u(t, p) = f(t, x(t, p))$ , where

$$f(t,x) := \mathbb{E}\left[g\left(x\frac{X_T}{X_t}\right)\right] = \mathbb{E}\left[g\left(x\frac{X_T}{X_t}\right) \mid \mathcal{F}_t\right]$$
  
$$= \sum_{q_1,\cdots,q_n=0}^{\infty} g\left(x_1 e^{\sum_{j=1}^n (\beta_{1j}q_j - (e^{\beta_{1j}} - 1)\lambda_j(T-t))}, \ldots, x_n e^{\sum_{j=1}^n (\beta_{nj}q_j - (e^{\beta_{nj}} - 1)\lambda_j(T-t))}\right) \prod_{i=1}^n \frac{\lambda_i^{q_i}}{q_i!} (T-t)^{q_i} e^{-\lambda_i(T-t)}$$
  
(103)

The equalities follow from the definition of  $v(p)$ above and of  $u(t, p)$  in equation (90) together with the two formulae following it.<sup>c</sup> We clearly have  $f(T, x) = g(x)$  and

$$F_t := u(t, P_t) = f(t, X_t) = \mathbb{E}[g(X_T) | \mathcal{F}_t] \quad (104)$$

Since  $u(t, p) = f(t, x(t, p))$ , the deltas in equation (102) are given by partial differences of  $f(t, x)$ as

$$\delta_t^i = \delta_i(t, X_{t-}) \quad \text{where}$$
  
$$\delta_i(t, x) := \frac{1}{x_i} \sum_{j=1}^k \alpha_{ij} (f(t, e^{\beta_{1j}} x_1, \dots, e^{\beta_{nj}} x_n) - f(t, x)) \tag{105}$$

We have unique pricing since  $(X, 1)$  is arbitrage free (as  $X^i$  are martingales). Specifically, if  $\hat{\delta}$  is another SFTS for  $(X, 1)$  with payoff  $\hat{F}_T = g(X_T)$ , then  $\hat{F} := \sum_{i=1}^{n} \hat{\delta}^{i} X^{i} + \hat{\delta}^{m} = F$  provided that either all  $\hat{\delta}^i$ ,  $i \leq n$  are bounded or all  $\hat{\delta}^i - \delta^i$ ,  $i \leq n$  are bounded.

Indeed, then  $\hat{F} = \hat{F}_0 + \hat{\delta}' \cdot X$  is a martingale, since  $X$  is square integrable (in the second case, also use that F is a martingale). Hence,  $\hat{F} = F$  as  $\hat{F}_T = F_T$ .

Moreover, if  $k = n$  we have unique hedging, that is,  $\hat{\delta} = \delta$  for any bounded SFTS  $\hat{\delta}$  for  $(X, 1)$  with *payoff*  $\hat{F}_T = g(X_T)$ . Indeed,  $\hat{F} = F$ , as before; thus, setting  $\theta^i := \hat{\delta}^i - \delta^i$  gives

$$0 = \mathrm{d}\langle \hat{F} - F \rangle = \sum_{i,j=1}^{n} \theta^{i} \theta^{j} \mathrm{d}\langle X^{i}, X^{j} \rangle$$
$$= \sum_{i,j=1}^{n} \theta^{i} \theta^{j} X_{-}^{i} X_{-}^{j} \sum_{l=1}^{n} (\mathrm{e}^{\beta_{il}} - 1)(\mathrm{e}^{\beta_{jl}} - 1)\lambda_{l} \mathrm{d}t \tag{106}$$

the last equality following from equation (98). However, the  $n \times n$  matrix  $\left(\sum_{l=1}^{n} (e^{\beta_{il}} - 1) (e^{\beta_{jl}} - 1)\right)$  $(1)\lambda_l^n_{i,i=1}$  is nonsingular. Therefore,  $\theta^i = 0$ , that is,  $\hat{\delta}^i = \delta^i$  for  $i \leq n$ , implying  $\hat{\delta}^m = \delta^m$  too as  $\hat{F} = F$ .

One shows, as in the section Exponential-Poisson Exchange Option Model, that the processes  $\delta^i$  are bounded if  $\gamma_i(x)$  are bounded, where

$$\gamma_i(x) := \frac{1}{x_i} \sum_{j=1}^k \alpha_{ij} (g(e^{\beta_{1j}} x_1, \dots, e^{\beta_{nj}} x_n) - g(x)),$$
  
$$\gamma_m(x) := g(x) - \sum_{i=1}^n \gamma_i(x) x_i$$
 (107)

#### Homogeneous Exponential-Poisson SFTS

Let  $A > 0$  be an *m*-dimensional semimartingale with  $A_{-} > 0$  and set  $X := (A^{i}/A^{m})_{i=1}^{n}, n := m-1$ , as before. Assume that

$$dX_t^i = X_{t-}^i \sum_{j=1}^k (e^{\beta_{ij}} - 1)(dP_t^j - \lambda_t^j dt) \qquad (108)$$

where  $1 \leq k \leq n$ ,  $\beta_{ij}$  are constants with the  $n \times$ k matrix  $(e^{\beta_{ij}}-1)$  of full rank,  $\lambda^j>0$  are bounded predictable processes, and  $P^{j}$  are semimartingales with  $[P^j, P^l] = 0$  for  $j \neq l$  such that  $[P^j] = P^j$ ,  $P_0^j = 0$ , and  $P^j - \int \kappa^j dt$  are local martingales for some locally bounded predictable processes  $\kappa^j > 0$ . Assume further that  $\mathbb{E} \exp\left(\sum_{j=1}^k \int_0^T \left(\frac{\lambda_t^j}{\kappa_t^j} - 1\right)^2 \kappa_t^j \mathrm{d}t\right) < \infty.$ 

Owing to the above growth condition, the positive local martingale

$$M := \mathcal{E}\left(\sum_{j=1}^{k} \int \left(\frac{\lambda^{j}}{\kappa^{j}} - 1\right) (\mathrm{d}P^{j} - \kappa^{j} \mathrm{d}t)\right)$$
$$= \mathrm{e}^{-\sum_{j=1}^{k} \int (\lambda^{j} - \kappa^{j}) \mathrm{d}t} \prod_{s \leq \cdot} (1 + \sum_{j=1}^{n} \left(\frac{\lambda_{s}^{j}}{\kappa_{s}^{j}} - 1\right) \Delta P_{s}^{j}) \tag{109}$$

is a martingale. Define the measure  $\mathbb{Q}$  by  $d\mathbb{Q} =$  $M_T d\mathbb{P}$ . As in the section Exponential-Poisson Model Uniqueness,  $\int \lambda^j dt$  are the  $\mathbb{Q}$ -compensator of  $P^j$ . This, equation (108), and boundedness of  $\lambda^j$  imply that  $X^i$  are  $\mathbb{Q}$ -square integrable martingales. Thus, A is arbitrage free. As before, the SDE  $(108)$  integrates to

$$X_t^i = X_0^i e^{\sum_{j=1}^k \beta_{ij} P_t^j - (e^{\beta_{ij}} - 1) \int_0^t \lambda_s^j ds}$$
(110)

Now assume  $\lambda^j$  are constant. Then  $P^j$  are  $\mathbb{Q}$ -Poisson processes with intensities  $\lambda^j$  and are independent since  $[P^j, P^l] = 0, j \neq l$ . Let  $h(a), a \in$  $\mathbb{R}^m_+$ , be a homogeneous function of linear growth. Define  $g(x) := h(x, 1), x \in \mathbb{R}^n_+$ . The section Projective Exponential-Poisson SFTS applied under  $\mathbb{Q}$ implies that  $\delta$  given by equation (105) (with  $\delta^m =$  $F - \sum_{i=1}^{n} \delta^{i} X^{i}$  is an SFTS for  $(X, 1)$  with price process  $F = (f(t, X_t))$  satisfying  $F_T = g(X_T)$ , where  $f(t, x)$  is defined explicitly by equation (103), or equivalently,  $f(t,x) = \mathbb{E}^{\mathbb{Q}} g(xX_T/X_t)$ . Therefore, by numéraire invariance,  $\delta$  is an SFTS for A with price process  $C := A^m F$  satisfying  $C_T =$  $A^m g(X_T) = h(A_T)$  by homogeneity.

Assume finally that the payoff function  $h(a)$  is such that the functions  $\gamma_i(x)$  defined in equation (107) are bounded (e.g.,  $h(a) = \max(a^1, \dots, a^m)$ ). By the section Projective Exponential-Poisson SFTS, if  $k = n$ , then  $\delta$  is the unique bounded SFTS for A with payoff  $C_T = h(A_T)$ . In general, since A is arbitrage free,  $\hat{C} = C$  for any other bounded SFTS  $\hat{\delta}$  for A with payoff  $\hat{C}_T = h(A_T)$ , where  $\hat{C} :=$  $\sum_i \hat{\delta}^i A^i$ .

## **End Notes**

<sup>a</sup>. Clearly, then the restriction of (any such)  $c(t, a)$  to the support of A is unique, and if  $\hat{c}(t, a)$  is any function that equals  $c(t, a)$  on the support of A, then  $C_t = \hat{c}(t, A_t)$  too. If the support of  $A_t$  is a proper surface, for example, if  $m = 2$  and  $A^2$  is deterministic as in the Black-Scholes model or  $A_t^2 = a_2(t, A_t^1)$  as in Markovian short-rate models, then obviously there exist infinitely many nonhomogeneous functions  $\hat{c}(t, a)$  such that  $C_t = \hat{c}(t, A_t)$ . (Such a homogeneous function also exists under some assumptions as in the section Homogeneous Continuous Markovian SFTS.)

<sup>b.</sup>Indeed, first assume that  $A$  is arbitrage free and let  $S$ be a state price density. The martingale  $M := \frac{S A^m}{\mathbb{E}[S_0 A_0^m]}$ clearly satisfies  $\mathbb{E} M_T = 1$ . Hence, the equivalent measure  $\mathbb{Q}$  defined by  $d\mathbb{Q} = M_T d\mathbb{P}$  is a probability measure. Since  $MX^i = \frac{SA^i}{\mathbb{E}[S_0A_0^m]}$  is a martingale,  $X^i$  is a  $\mathbb{Q}$ martingale by Bayes' rule. Conversely, assume that  $X^i$  are  $\mathbb{Q}$ -martingales for some  $\mathbb{Q}$ . Define  $M_t := \mathbb{E}\left[\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\mid \mathcal{F}_t\right] >$ 0. Then (the right continuous version of)  $\stackrel{\text{L}}{M} = (M_t)$  is a martingale (so  $M_{-} > 0$ ). By Bayes' rule  $MX^{i}$  are martingales since  $X^i$  are  $\mathbb{Q}$ -martingales. Set  $S := M/A^m$ . Then  $S, S_{-} > 0$  and  $SA^{i} = MX^{i}$ . Thus S is a deflator, as desired. Further, since  $SC$  is a martingale for any bounded SFTS  $\delta$ , by the Bayes' rule  $SC/M = C/A^m$  is a  $\mathbb{O}$ -martingale.

<sup>c</sup>. The projective option price function  $f(t, x) :=$  $\mathbb{E}\left[g\left(x\frac{X_T}{X_t}\right)\right]$ , also encountered for the log-Gaussian case in equation (75), satisfies  $f(t, X_t) = \mathbb{E}[g(X_T) | \mathcal{F}_t]$  in general when  $X$  is the exponential of any  $n$ -dimensional process of independent increments (inhomogeneous Lévy *process*), but we no longer have hedging in general.

#### References

- Black, F. & Scholes, M. (1973). The pricing of options [1] and corporate liabilities, Journal of Political Economics 81. 637-659.
- [2] Delbaen, F. & Schachermayer, W. (2006). The Mathematics of Arbitrage, Springer.
- Duffie, D. (2001). Dynamic Asset Pricing Theory, 3rd [3] Edition, Princeton University Press.
- [4] El-Karoui, N., Geman, H. & Rochet, J.C. (1995). Change of numeraire, change of probability measure, and option pricing, Journal of Applied Probability 32,  $443 - 458$
- Harrison, M.J. & Kreps, D.M. (1979). Martingales and [5] arbitrage in multiperiod securities markets, Journal of Economic Theory 20, 381-408.
- Harrison, M.J. & Pliska, S. (1981). Martingales and [6] stochastic integrals in the theory of continuous trading, Stochastic Processes and their Applications 11, 215-260.
- [7] Jamshidian, F. (1993). Options and futures evaluation with deterministic volatilities, Mathematical Finance  $3(2), 149-159.$
- [8] Margrabe, W. (1978). The value of an option to exchange one asset for another, Journal of Finance 33,  $177 - 186.$

- [9] Merton, R. (1973). Theory of rational option pricing, *Bell Journal of Economics* **4**(1), 141–183.
- [10] Neuberger, A. (1990). *Pricing Swap Options Using the Forward Swap Market*, IFA Preprint.

# **Related Articles**

**Arbitrage Strategy**; **Caps and Floors**; **CMS Spread Products**; **Equivalent Martingale Measures**; **For-** **eign Exchange Options**; **Forward–Backward Stochastic Differential Equations (SDEs)**; **Hedging**; **Ito's Formula ˆ** ; **Markov Processes**; **Martingales**; **Poisson Process**.

FARSHID JAMSHIDIAN
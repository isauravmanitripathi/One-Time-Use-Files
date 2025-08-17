# **Black–Scholes Formula**

"If options are correctly priced in the market, it should not be possible to make sure profits by creating portfolios of long and short positions in options and their underlying stocks. Using this principle, a theoretical valuation formula for options is derived." These sentences, from the abstract of the great paper [2] by Fischer Black and Myron Scholes, encapsulate the basic idea that—with the asset price model they employ—insisting on absence of **arbitrage** is enough to obtain a unique value for a call option on the asset. The resulting formula, equation (6) below, is the most famous formula in financial economics. and, in fact, that whole subject splits decisively into the pre-Black-Scholes and post-Black-Scholes eras.

This article aims to give a self-contained derivation of the formula, some discussion of the hedge parameters, and some extensions of the formula, and to indicate why a formula based on a stylized mathematical model, which is known not to be a particularly accurate representation of real asset prices, has nevertheless proved so effective in the world of option trading. The section The Model and Formula formulates the model and states and proves the formula. As is well known, the formula can equally well be stated in the form of a partial differential equation (PDE); this is equation  $(9)$  below. The next section discusses the PDE aspects of Black-Scholes. The section Hedge Parameters summarizes information about the option 'greeks', while the sections The Black 'Forward' Option Formula and A Universal Black Formula introduce what is actually a more useful form of Black-Scholes, usually known as the Black formula. Finally, the section Implied Volatility and Market Trading discusses the applications of the formula in market trading. We define the *implied volatility* and demonstrate a "robustness" property of Black-Scholes, which implies that effective hedging can be achieved even if the "true" price process is substantially different from Black and Scholes' stylized model.

### The Model and Formula

Let  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in \mathbb{R}^+}, \mathbb{P})$  be a **probability space** with a given filtration  $(\mathcal{F}_t)$  representing the flow of information in the market. Traded asset prices are  $\mathcal{F}_t$ -adapted stochastic processes on  $(\Omega, \mathcal{F}, \mathbb{P})$ . We assume that the market is *frictionless*; assets may be held in arbitrary amount, positive and negative, the interest rate for borrowing and lending is the same, and there are no transaction costs (i.e., the  $bid-ask$  spread is 0). While there may be many traded assets in the market, we fix attention on two of them. First, there is a "risky" asset whose price process  $(S_t, t \in \mathbb{R}^+)$  is assumed to satisfy the **stochastic dif**ferential equation (SDE)

$$dS_t = \mu S_t dt + \sigma S_t dw_t \tag{1}$$

with given *drift*  $\mu$  and *volatility*  $\sigma$ . Here  $(w_t, t \in \mathbb{R}^+)$ is an  $(\mathcal{F}_t)$ -Brownian motion. Equation (1) has a unique solution: if  $S_t$  satisfies equation (1), then by the Itô formula

$$d \log S_t = \left(\mu - \frac{1}{2}\sigma^2\right) dt + \sigma dw_t \tag{2}$$

so that  $S_t$  satisfies equation (1) if and only if

$$S_t = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma w_t\right) \tag{3}$$

Asset  $S_t$  is assumed to have a constant dividend yield  $q$ , that is, the holder receives a dividend payment  $qS_t$  dt in the time interval [t, t + dt]. Secondly, there is a riskless asset paying interest at a fixed continuously compounding rate  $r$ . The exact form of this asset is unimportant—it could be a moneymarket account in which  $1$  deposited at time *s* grows to  $e^{r(t-s)}$  at time t, or it could be a zero-coupon bond maturing with a value of  $1$  at some time  $T$ , so that its value at  $t \leq T$  is

$$B_t = \exp(-r(T - t)) \tag{4}$$

This grows, as required, at rate  $r$ :

$$\mathrm{d}B_t = r\,B_t\,\mathrm{d}t\tag{5}$$

Note that equation  $(5)$  does not depend on the final maturity  $T$  (the same growth rate is obtained from any zero-coupon bond) and the choice of  $T$  is a matter of convenience.

A European call option on  $S_t$  is a contract, entered at time  $0$  and specified by two parameters  $(K, T)$ , which gives the holder the right, but not the obligation, to purchase 1 unit of the risky asset at price K at time  $T > 0$ . (In the frictionless market setting, an option to buy  $N$  units of stock is equivalent to  $N$  options on a single unit, so we do not need to include quantity as a parameter.) If  $S_T \leq K$  the option is worthless and will not be exercised. If  $S_T > K$  the holder can exercise his option, buying the asset at price  $K$ , and then immediately selling it at the prevailing market price  $S_T$ , realizing a profit of  $S_T$  – K. Thus, the exercise value of the option is  $[S_T K^+ = \max(S_T - K, 0)$ . Similarly, the exercise value of a *European put option*, conferring on the holder the right to *sell* at a fixed price K, is  $[K - S_T]^+$ . In either case, the exercise value is nonnegative and, in the above model, is strictly positive with positive probability, so the option buyer should pay the writer a premium to acquire it. Black and Scholes [2] showed that there is a unique arbitrage-free value for this premium.

#### Theorem 1

1. In the above model, the unique arbitrage-free value at time  $t < T$  when  $S_t = S$  of the call  $option \nmatrix at \ntime T with \n~~strike~~ K is$ 

$$C(t, S) = e^{-q(T-t)} SN(d_1) - e^{-r(T-t)} KN(d_2)$$
(6)

where  $N(\cdot)$  denotes the cumulative standard normal distribution function

$$N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{1}{2}y^2} dy \tag{7}$$

and

$$d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T - t)}{\sigma\sqrt{T - t}}$$
$$d_2 = d_1 - \sigma\sqrt{T - t} \tag{8}$$

2. The function  $C(t, S)$  may be characterized as the unique  $C^{1,2}$  solution<sup>a</sup> of the Black–Scholes PDE

$$\frac{\partial C}{\partial t} + rS\frac{\partial C}{\partial S} + \frac{1}{2}\sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} - rC = 0 \qquad (9)$$

solved backward in time with the terminal boundary condition

$$C(T, S) = [S - K]^{+} \tag{10}$$

3. The value of the put option with exercise time  $T$ and strike  $K$  is

$$P(t, S) = e^{-r(T-t)} K N(-d_2)$$
$$- e^{-q(T-t)} SN(-d_1) \qquad (11)$$

To prove the theorem, we are going to show that the call option value can be replicated by a dynamic trading strategy investing in the asset  $S_t$  and in the zero-coupon bond  $B_t = e^{-r(T-t)}$ . A trading strategy is specified by an initial capital  $x$  and a pair of adapted processes  $\alpha_t$ ,  $\beta_t$  representing the number of units of  $S, B$  respectively held at time  $t$ ; the portfolio value at time t is then  $X_t = \alpha_t S_t + \beta_t B_t$ , and by definition  $x = \alpha_0 S_0 + \beta_0 B_0$ . The trading strategy  $(x, \alpha, \beta)$  is admissible if

(i) 
$$\int_0^T \alpha_t^2 S_t^2 dt < \infty \text{ a.s.}$$
  
(ii) 
$$\int_0^T |\beta_t| dt < \infty \text{ a.s.}$$

(iii) There exists a constant  $L \ge 0$  such that  $X_t \geq -L$  for all t, a.s.

The *gain from trade* in  $[s, t]$  is

$$\int_s^t \alpha_u \, \mathrm{d}S_u + \int_s^t \beta_u \, \mathrm{d}B_u + \int_s^t q \alpha_u S_u \, \mathrm{d}u$$

where the first integral is an Itô stochastic integral. This is the sum of the accumulated capital gains/losses in the two assets plus the total dividend received. The trading strategy is *self-financing* if

$$\alpha_t S_t + \beta_t B_t - \alpha_s S_s - \beta_s B_s$$
  
=  $\int_s^t \alpha_u \, \mathrm{d}S_u + \int_s^t q \alpha_u S_u \, \mathrm{d}u + \int_s^t \beta_u \, \mathrm{d}B_u \quad (13)$ 

implying that the change in value over any interval in portfolio value is entirely due to gains from trade (the accumulated increments in the value of the assets in the portfolio plus the total dividend received).

We can always create self-financing strategies by fixing  $\alpha$ , the investment in the risky asset, and investing all residual wealth in the bond. Indeed, the value of the risky asset holding at time  $t$  is  $\alpha_t S_t$ , so if the total portfolio value is  $X_t$  we take

 $\beta_t = (X_t - \alpha_t S_t)/B_t$ . The portfolio value process is then defined implicitly as the solution of the SDE

$$\begin{aligned} \mathrm{d}X_t &= \alpha_t \,\mathrm{d}S_t + q\alpha_t S_t \,\mathrm{d}t + \beta_t \,\mathrm{d}B_t \\ &= \alpha_t \,\mathrm{d}S_t + q\alpha_t S_t \,\mathrm{d}t + (X_t - \alpha_t S_t)r \,\mathrm{d}t \\ &= rX_t \,\mathrm{d}t + \alpha_t S_t \sigma(\theta \,\mathrm{d}t + \mathrm{d}w_t) \end{aligned} \tag{14}$$

where  $\theta = (\mu - r + q)/\sigma$ . This strategy is always self-financing since  $X_t$  is, by definition, the gains from trade process, while the value is  $\alpha S + \beta B = X$ .

**Proof of Theorem** (1) The key step is to put the "wealth equation"  $(14)$  into a more convenient form by **change** of **measure**. Define a measure  $\mathbb{Q}$ , the so-called *risk-neutral measure* on  $(\Omega, \mathcal{F}_T)$  by the Radon-Nikodým derivative

$$\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} = \exp\left(-\theta w_T - \frac{1}{2}\theta^2 T\right) \tag{15}$$

(The right-hand side has expectation 1, since  $w_T \sim$  $N(0, T)$ .) Expectation with respect to  $\mathbb{Q}$  will be denoted  $\mathbb{E}_{\mathbb{Q}}$ . By the Girsanov theorem,  $\check{w} = w_t + \theta t$ is a  $\mathbb{Q}$ -Brownian motion, so that from equation (1) the SDE satisfied by  $S_t$  under  $\mathbb{Q}$  is

$$dS_t = (r - q)S_t dt + \sigma S_t d\check{w}_t \tag{16}$$

so that for  $t < T$ 

$$S_T = S_t \exp\left(\left(r - q - \frac{1}{2}\sigma^2\right)(T - t) + \sigma(\check{w}_T - \check{w}_t)\right)$$
(17)

Applying the Itô formula and equation (14) we find that, with  $\tilde{X}_t = e^{-rt} X_t$  and  $\tilde{S}_t = e^{-rt} S_t$ 

$$\mathrm{d}\tilde{X}_t = \alpha_t \tilde{S}_t \sigma \, \mathrm{d}\check{w}_t \tag{18}$$

Thus  $e^{-rt}X_t$  is a  $\mathbb{Q}$ -local martingale under condition (12)(i). Let  $h(S) = [S - K]^+$  and suppose there exists a replicating strategy, that is, a strategy  $(x, \alpha, \beta)$  with value process  $X_t$  constructed as in equation (14) such that  $X_T = h(S_T)$  a.s. Suppose also that  $\alpha_t$  satisfies the stronger condition

$$\mathbb{E}_{\mathbb{Q}} \int_0^T \alpha_t^2 S_t^2 \, \mathrm{d}t < \infty \tag{19}$$

Then  $\tilde{X}_t$  is a  $\mathbb{Q}$ -martingale, and hence for  $t < T$ 

$$X_t = e^{-r(T-t)} \mathbb{E}_{\mathbb{Q}}[h(S_T)|\mathcal{F}_t]$$
(20)

and in particular

$$x = e^{-rT} \mathbb{E}_{\mathbb{Q}}[h(S_T)] \tag{21}$$

Now  $S_t$  is a **Markov process**, so the conditional expectation in equation (20) is a function of  $S_t$ , and indeed we see from equation (17) that  $S_T$  is a function of  $S_t$  and the increment  $(\check{w}_T - \check{w}_t)$ , which is independent of  $\mathcal{F}_t$ . Writing  $(\check{w}_T - \check{w}_t) = Z\sqrt{T-t}$ where  $Z \sim N(0, 1)$ , the expectation is simply a one-dimensional integral with respect to the normal distribution. Hence,  $X_t = C(t, S_t)$  where

$$C(t, S) = \frac{\mathrm{e}^{-r(T-t)}}{\sqrt{2\pi}} \int_{-\infty}^{\infty} h(S \exp((r-q-\sigma^2/2) \times (T-t) - \sigma x \sqrt{T-t})) \mathrm{e}^{-1/2x^2} \mathrm{d}x \tag{22}$$

Straightforward calculations show that this integral is equal to the closed-form expression in equation (6).

The argument so far shows that if there is a replicating strategy, the initial capital required must be  $x = C(0, S_0)$  where C is defined by equation (22). It remains to identify the strategy  $(x, \alpha, \beta)$  and to show that it is admissible. Let us temporarily take for  $\alpha$  granted the assertions of part (2) of the theorem; these will be proved in Theorem 3 below, where we also show that  $(\partial C/\partial S)(t, S) = e^{-q(T-t)}N(d_1)$ , so that in particular  $0 < \partial C/\partial S < 1$ .

The replicating strategy is  $\mathcal{A} = (x, \alpha, \beta)$  defined by

$$x = C(0, S_0), \quad \alpha_t = \frac{\partial C}{\partial S}(t, S_t)$$
$$\beta_t = \frac{1}{rB_t} \left( \frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} - qS_t \frac{\partial C}{\partial S} \right) \tag{23}$$

Indeed, using the PDE (9) we find that  $X_t = \alpha_t S_t +$  $\beta_t B_t = C(t, S_t)$ , so that A is replicating and also  $X_t \ge 0$ , so that condition (12)(iii) is satisfied. From equation  $(17)$ 

$$S_t^2 = S_0^2 \exp((2r - 2q - \sigma^2)t + 2\sigma \check{w}_t) \qquad (24)$$

so that  $\mathbb{E}_{\mathbb{Q}}[S_t^2] = \exp((2r - 2q + \sigma^2)t)$ . Since  $|e^{-r(T-t)}\partial C/\partial S| < 1$ , this shows that  $\mathbb{E}_{\mathbb{Q}}\int_{0}^{T}\alpha_{t}^{2}S_{t}^{2}$  $dt < \infty$ , that is, condition (19) is satisfied. Since  $\beta_t$ is, almost surely (a. s.), a continuous function of  $t$  it satisfies equation (12)(ii). Thus  $\mathcal{A}$  is admissible. The gain from trade in an interval  $[s, t]$  is

$$\begin{split} &\int_{s}^{t} \alpha_{u} \, \mathrm{d}S_{u} + \int_{s}^{t} q \alpha_{u} S_{u} \, \mathrm{d}u + \int_{s}^{t} \beta_{u} \, \mathrm{d}B_{u} \\ &= \int_{s}^{t} \frac{\partial C}{\partial S} \, \mathrm{d}S + \int_{s}^{t} \left( \frac{\partial C}{\partial t} + \frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} C}{\partial S^{2}} \right) \, \mathrm{d}u \\ &= \int_{s}^{t} \, \mathrm{d}C \\ &= C(t, S_{t}) - C(s, S_{s}) \end{split} \tag{25}$$

(We obtain the first equality from the definition of  $\alpha$ ,  $\beta$ , and it turns out to be just the Itô formula applied to the function  $C$ .) This confirms the self-financing property and completes the proof.

Finally, part (3) of the theorem follows from the model-free **put-call parity** relation  $C - P =$  $e^{-q(T-t)}S - e^{-r(\bar{T}-t)}K$  and symmetry of the normal distribution:  $N(-x) = 1 - N(x)$ .

The replicating strategy derived above is known as **delta hedging**: the number of units of the risky asset held in the portfolio is equal to the Black-Scholes delta,  $\Delta = \partial C / \partial S$ .

So far, we have concentrated entirely on the hedging of call options. We conclude this section by showing that, with the class of trading strategies we have defined, there are no arbitrage opportunities in the Black-Scholes model.

**Theorem 2** There is no admissible trading strategy in a single asset and the zero-coupon bond that generates an arbitrage opportunity, in the Black–Scholes model.

**Proof** Suppose  $X_t$  is the portfolio value process corresponding to an admissible trading strategy  $(x, \alpha, \beta)$ . There is an arbitrage opportunity if  $x = 0$ and, for some t,  $X_t \ge 0$  a.s. and  $\mathbb{P}[X_t > 0] > 0$ , or equivalently  $\mathbb{E}[X_t] > 0$ . This is the  $\mathbb{P}$ -expectation, but  $\mathbb{E}[X_t] > 0 \Leftrightarrow \mathbb{E}_{\mathbb{Q}}[\tilde{X}_t] > 0$  since  $\mathbb{P}$  and  $\mathbb{Q}$  are equivalent measures and  $e^{-rt} > 0$ . From equation (18),  $\tilde{X}_t$  is a  $\mathbb{Q}$ -local martingale which, by the definition of admissibility, is bounded below by a constant  $-L$ . It follows that  $\tilde{X}_t$  is a **supermartingale**, so if  $x = 0$ , then  $\mathbb{E}_{\mathbb{Q}}[\tilde{X}_t] \leq 0$  for any t. So no arbitrage can arise from the strategy  $(0, \alpha, \beta)$ .  $\Box$ 

# The Black-Scholes Partial Differential Equation

#### Theorem 3

- 1. The Black-Scholes PDE (9) with boundary condition (10) has a unique  $C^{1,2}$  solution, given by equation (6).
- 2. The Black-Scholes "delta",  $\Delta(t, S)$ , is given by

$$\Delta(t, S) = \frac{\partial}{\partial S} C(t, S) = e^{-q(T-t)} N(d_1) \quad (26)$$

**Proof** It can—with some pain—be directly checked that  $C(t, S)$  defined by equation (6) does satisfy the Black-Scholes PDE (9), (10), and a further calculation (not quite as simple as it appears) gives the formula (26) for the Black-Scholes delta. It is, however, enlightening to take the original route of Black and Scholes and relate the equation (9) to a simpler equation, the *heat equation*. Note from the explicit expression  $(17)$  for the price process under the risk-neutral measure that, given the starting point  $S_t$ , there is a one-to-one relation between  $S_T$  and the Brownian increment  $\check{w}_T - \check{w}_t$ . We can therefore always express things interchangeably in "S coordinates" or in " $\check{w}$  coordinates". In fact, we already made use of this in deriving the integral price expression  $(22)$ . Here we proceed as follows.

For fixed parameters  $S_0, r, q, \sigma$ , define the functions  $\phi: \mathbb{R}^+ \times \mathbb{R} \to \mathbb{R}^+$  and  $u: [0, T] \times \mathbb{R} \to \mathbb{R}^+$  by

$$\phi(t,x) = S_0 \exp\left(\left(r - q - \frac{1}{2}\sigma^2\right)t + \sigma x\right) \tag{27}$$

and

$$u(t,x) = C(t,\phi(t,x)) \tag{28}$$

Note that the inverse function  $\psi(t,s) = \phi^{-1}(t,s)$ (i.e., the solution for x of the equation  $s = \phi(t, x)$ ) is

$$\psi(t,s) = \frac{1}{\sigma} \left( \log \left( \frac{s}{S_0} \right) - \left( r - q - \frac{1}{2} \sigma^2 \right) t \right) \tag{29}$$

A direct calculation shows that  $C$  satisfies equation  $(9)$  if and only if u satisfies the heat equation

$$\frac{\partial u}{\partial t} + \frac{1}{2} \frac{\partial^2 u}{\partial x^2} - r u = 0 \tag{30}$$

If  $W_t$  is Brownian motion on some probability space and u is a  $C^{1,2}$  function, then an application of the Itô formula shows that

$$\mathbf{d}(\mathbf{e}^{-rt}u(t,W_t)) = \mathbf{e}^{-rt} \left(\frac{\partial u}{\partial t} + \frac{1}{2}\frac{\partial^2 u}{\partial x^2} - ru\right) \mathbf{d}t$$
$$+ \mathbf{e}^{-rt} \frac{\partial u}{\partial x} \mathbf{d}W_t \tag{31}$$

If  $u$  satisfies equation (30) with boundary condition  $u(T, x) = g(x)$  and

$$\mathbb{E}\int_{0}^{T}\left(\frac{\partial u}{\partial x}(t, W_{t})\right)^{2} \mathrm{d}t < \infty \tag{32}$$

then the process  $t \mapsto e^{-rt}u(t, W_t)$  is a martingale so that, with  $\mathbb{E}_{t,x}$  denoting the conditional expectation given  $W_t = x$ ,

$$\begin{aligned} \mathbf{e}^{-rt}u(t,x) &= \mathbb{E}_{t,x}[\mathbf{e}^{-rT}u(T,W_T)] \\ &= \mathbb{E}_{t,x}[\mathbf{e}^{-rT}g(W_T)] \end{aligned} \tag{33}$$

Since  $W_T \sim N(x, T - t)$ , this shows that *u* is given bv

$$u(t,x) = \frac{e^{-r(T-t)}}{\sqrt{2\pi(T-t)}} \int_{-\infty}^{\infty} g(y) e^{-\frac{(y-x)^2}{2(T-t)}} dy \quad (34)$$

A sufficient condition for equation  $(32)$  is

$$\frac{1}{\sqrt{2\pi T}}\int_{-\infty}^{\infty}g^2(y)e^{-y^2/2T}\,dy<\infty\qquad(35)$$

In our case, the boundary condition is  $g(x) =$  $[\phi(t,x)-K]^+ < \phi(t,x)$  and this condition is easily checked. Hence, equation  $(30)$  with this boundary condition has unique  $\hat{C}^{1,2}$  solution (34), implying that the inverse function  $C(t, S) = u(t, \psi(t, S))$  given by equation (22) is the unique  $C^{1,2}$ , solution of equation  $(9)$  as claimed.  $\Box$ 

## **Hedge Parameters**

Bringing in all the parameters, the Black-Scholes formula (6) is a six-parameter function  $C(t, S) =$  $\mathcal{C}(\tau, S, K, r, q, \sigma)$ , where  $\tau = T - t$  is the time to maturity. For risk-management purposes, it is important to know the sensitivities of the option value to changes in the parameters. The conventional hedge parameters or "greeks" are given in Table 1. There are slight notational problems in that "vega" is not the name of a Greek letter (here we have used uppercase upsilon, but this is not necessarily a conventional choice) and upper-case rho coincides with Latin P, so this parameter is usually written  $\rho$ , risking confusion with correlation parameters. The expressions in the right-hand column are readily obtained from the sensitivity parameters (42) and (43) of the "universal" Black Formula introduced below.

Delta is, of course, the Black–Scholes hedge ratio. Gamma measures the convexity of  $C$  and is at its maximum when the option is close to being at the money. Since gamma is the rate of change of delta, frequent rebalancing of the hedge portfolio will be required in areas of high gamma. Theta is defined as  $-\partial \mathcal{C}/\partial \tau$  and is generally negative (as can be seen from the table, it is always negative for a call option on an asset with no dividends). It represents the "time decay" in the option value as the maturity time is reduced, that is, real time advances. As regards rho, it is not immediately obvious, without doing the calculation, what its sign will be: on one hand, increasing  $r$  increases the forward price, pushing a call option further into the money, while on the other hand increased  $r$  implies heavier discounting, reducing option value. As can be seen from the table,

| Table 1 |  |  |  |  | Black–Scholes risk parameters |
|---------|--|--|--|--|-------------------------------|
|---------|--|--|--|--|-------------------------------|

| Delta |   | $\frac{\partial \mathcal{C}}{\partial S}$      | $e^{-q\tau}N(d_1)$                                                                                                       |
|-------|---|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Gamma |   | $\frac{\partial^2 \mathcal{C}}{\partial S^2}$  | $\frac{\mathrm{e}^{-q\tau}N'(\mathrm{d}_1)}{S\sigma\sqrt{\tau}}$                                                         |
| Theta | Θ | $\frac{\partial \mathcal{C}}{\partial \tau}$   | $\frac{e^{-q\tau}SN'(\mathbf{d}_1)\sigma}{2\sqrt{\tau}} + q\,e^{-q\tau}SN(\mathbf{d}_1) - r\,Ke^{-r\tau}N(\mathbf{d}_2)$ |
| Rho   | Ρ | $\frac{\partial \mathcal{C}}{\partial r}$      | $K\tau e^{-r\tau}N(d_2)$                                                                                                 |
| Vega  | Υ | $\frac{\partial \mathcal{C}}{\partial \sigma}$ | $e^{-q\tau} S \sqrt{\tau} N'(d_1)$                                                                                       |

the first effect wins: rho is always positive. Vega is in some ways the most important parameter, since a key risk in managing books of traded options is "vega risk", and in Black–Scholes this is completely "outside the model". Bringing it back inside the model is the subject of **stochastic volatility**.

An extensive discussion of the risk parameters and their uses can be found in Hull [6].

#### The Black "Forward" Option Formula

The six-parameter representation  $C(\tau, S, K, r, q, \sigma)$ is not the best parameterization of Black-Scholes. For the asset  $S_t$  with dividend yield  $q$ , the forward *price* at time t for delivery at time T is  $F(t, T) =$  $S_t e^{(r-q)(T-t)}$  (this is a model-free result, not related to the Black-Scholes model). We can trivially reexpress the price formula  $(6)$  as

$$C(t, S_t) = B(t, T)(F(t, T)N(d_1) - KN(d_2)) \quad (36)$$

with

$$d_1 = \frac{\log(F(t,T)/K) + \frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}}$$
  
$$d_2 = d_1 - \sigma\sqrt{T-t}$$
 (37)

where  $B(t, T) = e^{-r(T-t)}$  is the zero-coupon bond value or "discount factor" from  $T$  to  $t$ . There is, however, far more to this than just a change of notation. First, the continuously compounding rate  $r$  is not market data. The market data at time  $t$  is the set of discount factors  $B(t, t')$  for  $t' > t$ . We see from equation (36) that " $r$ " plays two distinct roles in Black-Scholes: it appears in the computation of the forward price  $F$  and the discount factor  $B$ . But both of these are more fundamental than  $r$  itself and are, in fact, market data which, as equation (36) shows, can be used directly. A further advantage is that the exact mechanism of dividend payment is not important, as long as there is an unambiguously defined forward price.

Formula (36) is known as the Black formula and is the most useful version of Black-Scholes, being widely applied in connection with FX (foreign exchange) and interest-rate options as well as dividend-paying equities. Fundamentally, it relates to a price model in which the price is expressed in the risk-neutral measure as  $S_t = F(0, t)M_t$  where  $M_t$  is the exponential martingale

$$M_t = \exp\left(\sigma \, \dot{w}_t - \frac{1}{2} \sigma^2 t\right) \tag{38}$$

which is equivalent to equation  $(17)$ . This model accords with the general fact that, in a world of deterministic interest rates, the forward price is the expected price in the risk-neutral measure, that is, the ratio  $S_t/F(0, t)$  is a positive martingale with expectation 1. The exponential martingale  $(38)$  is the simplest continuous-path process with these properties.

# A Universal Black Formula

The parameterization of Black-Scholes can be further compressed as follows. First, note that  $\sigma$  and  $\tau = (T - t)$  do not appear separately, but only in the combination  $a = \sigma \sqrt{T - t}$ , where  $a^2$  is sometimes known as the *operational time*. Next, define the "moneyness" m as  $m(t,T) = K/F(t,T)$ , and define

$$d(a,m) = \frac{a}{2} - \frac{\log m}{a} \tag{39}$$

(so that  $d_1 = d(\sigma\sqrt{T-t}, K/F(t, T))$ ). Then the Black formula (36) becomes

$$C = BF \ f(a, m) \tag{40}$$

where

$$f(a,m) = N(d(a,m)) - mN(d(a,m) - a) \quad (41)$$

Now  $BF$  is the price of a zero-strike call, or equivalently the price to be paid at time  $t$  for delivery of the asset at time T. Formula (40) says that the price of the  $K$ -strike call is the (model-free) price of the zero-strike call modified by a factor  $f$  that depends only on the moneyness and operational time. We call  $f$  the *universal Black–Scholes function*, and a graph of it is shown in Figure 1. With  $N' = dN/dx$  and  $d = d(a, m)$  we find that  $mN'(d - a) = N'(d)$  and hence obtain the following very simple expressions for the first-order derivatives:

$$\frac{\partial f}{\partial a}(a,m) = N'(d) \tag{42}$$

$$\frac{\partial f}{\partial m}(a,m) = -N(d-a) \tag{43}$$

In particular,  $\partial f/\partial a > 0$  and  $\partial f/\partial m < 0$  for all  $a, m$ .

![](_page_6_Figure_1.jpeg)

Figure 1 The universal Black–Scholes function

This minimal parameterization of Black-Scholes is used in studies of stochastic volatility; see, for example, **Gatheral** [5].

#### **Implied Volatility and Market Trading**

So far, our discussion has been entirely within the Black-Scholes model. What happens if we attempt to use Black-Scholes delta hedging in real market trading? This question has been considered by several authors, including El Karoui et al. [3] and Fouque et al. [4], though neither of these discusses the effect of jumps in the price process.

In the universal price formula  $(40)$ , the parameters  $B, F, m$  are market data, so we can regard the formula as a mapping  $a \mapsto p = BFf(a,m)$  from a to price  $p \in [B(F - K]^+, BF)$ . In a traded options market,  $p$  is market data (but must lie in the stated interval, else there is a static arbitrage opportunity). In view of equation (42),  $f(a, m)$  is strictly increasing in a and hence there is a unique value  $a = \hat{a}(p)$  such that  $p = BFf(\hat{a}(p), m)$ . The implied volatility is  $\hat{\sigma}(p) =$  $\hat{a}(p)/\sqrt{T-t}$ . If the underlying price process  $S_t$ actually were geometric Brownian motion (1), then  $\hat{\sigma}$  would be the same, and equal to the volatility  $\sigma$ , for call options of all strikes and maturities. Of course, this is never the case in practice—see  $[5]$  for

a discussion. Here, we restrict ourselves to examining what happens if we naïvely apply the Black-Scholes delta-hedge when in reality the underlying process is *not* geometric Brownian motion, taking  $q = 0$  for simplicity. Specifically, we assume that the "true" price model, under measure  $\mathbb{P}$ , is

$$S_t = S_0 + \int_0^t \eta_t S_{t-} \mathrm{d}t + \int_0^t \kappa_t S_{t-} \mathrm{d}W_t$$
$$+ \int_{[0,t] \times \mathbb{R}} S_{t-} v_t(z) \mu(\mathrm{d}t, \mathrm{d}z) \tag{44}$$

where  $\mu$  is a finite-activity *Poisson random measure*, so that there is a finite measure  $\nu$  on  $\mathbb{R}$  such that  $\mu([0, t] \times A) - \nu(A)t \equiv (\mu - \pi)([0, t] \times A)$  is a martingale for each  $A \in \mathcal{B}(\mathbb{R})$ .  $\eta, \kappa, \nu$  are predictable processes. Assume that  $\eta$ ,  $\kappa$  and  $\nu$  are such that the solution to the SDE (44) is well defined and, moreover, that  $v_t(z) > -1$  so  $S_t > 0$  almost surely. This is a very general model including path-dependent coefficients, stochastic volatility, and jumps. Readers unfamiliar with jump-diffusion models can set  $\mu = \nu = \pi = 0$  below, and refer to the last paragraph of this section for comments on the effect of jumps.

Consider the scenario of selling at time  $0$  a European call option at implied volatility  $\hat{\sigma}$ , that is, for the price  $p = \mathcal{C}(T, S_0, K, r, \hat{\sigma})$  and then following a Black-Scholes delta-hedging trading strategy based on constant volatility  $\hat{\sigma}$  until the option expires at time T. As usual, we shall denote  $C(t, s) =$  $\mathcal{C}(T-t, s, K, r, \hat{\sigma})$ , so that the hedge portfolio, with value process  $X_t$ , is constructed by holding  $\alpha_t :=$  $\partial_S C(t, S_{t-})$  units of the risky asset S, and the remainder  $\beta_t := \frac{1}{B_t}(X_{t-} - \alpha_t S_{t-})$  units in the riskless asset  $B$  (a unit notional zero-coupon bond). This portfolio, initially funded by the option sale (so  $X_0 =$  $p$ ), defines a self-financing trading strategy. Hence, the portfolio value process  $X$  satisfies the SDE

$$X_{t} = p + \int_{0}^{t} \partial_{S}C(u, S_{u-})\eta_{u}S_{u-}du$$
  
+ 
$$\int_{0}^{t} \partial_{S}C(u, S_{u-})\kappa_{u}S_{u-}dW_{u}$$
  
+ 
$$\int_{[0,t]\times\mathbb{R}} \partial_{S}C(u, S_{u-})S_{u-}v_{u}(z)\mu(\mathrm{d}u, \mathrm{d}z)$$
  
+ 
$$\int_{0}^{t} (X_{u} - \partial_{S}C(u, S_{u-})S_{u})r\mathrm{d}u \qquad (45)$$

Now define  $Y_t = C(t, S_t)$ , so that, in particular,  $Y_0 =$  $p$ . Applying the Itô formula (Lemma 4.4.6 of [1]) gives

$$Y_{t} = p + \int_{0}^{t} \partial_{t} C(u, S_{u-}) du$$
  
+ 
$$\int_{0}^{t} \partial_{s} C(u, S_{u-}) \eta_{u} S_{u-} du$$
  
+ 
$$\int_{0}^{t} \partial_{s} C(u, S_{u-}) \kappa_{u} S_{u-} du$$
  
+ 
$$\frac{1}{2} \int_{0}^{t} \partial_{sS}^{2} C(u, S_{u-}) \kappa_{u}^{2} S_{u-}^{2} du$$
  
+ 
$$\int_{[0,t] \times \mathbb{R}} \left( C(u, S_{u-}(1+v_{u}(z))) - C(u, S_{u-}) \right) \mu(dt, dz) \tag{46}$$

Thus the 'hedging error' process defined by  $Z_t :=$  $X_t - Y_t$  satisfies the SDE

$$Z_{t} = \int_{0}^{t} rX_{u} du - \int_{0}^{t} \left( rS_{u-}\partial_{S}C(u, S_{u-}) \right) du$$
  
+  $\partial_{t}C(u, S_{u-}) + \frac{1}{2}\kappa_{u}^{2}S_{u-}^{2}\partial_{SS}^{2}C(u, S_{u-})\right) du$   
-  $\int_{[0,t]\times\mathbb{R}} \left( C(u, S_{u-}(1+v_{u}(z))) - C(u, S_{u-}) \right)$   
-  $\partial_{S}C(u, S_{u-})S_{u-}v_{u}(z) \mu(du, dz)$   
=  $\int_{0}^{t} rZ_{u} du + \frac{1}{2} \int_{0}^{t} \Gamma(u, S_{u-})S_{u-}^{2}(\hat{\sigma}^{2} - \kappa_{u}^{2}) du$   
-  $\int_{[0,t]\times\mathbb{R}} \left( C(u, S_{u-}(1+v_{u}(z))) \right)$   
-  $C(u, S_{u-}) - \partial_{S}C(u, S_{u-})S_{u-}v_{u}(z) \mu(du, dz)$   
(47)

where  $\Gamma(t, S_t) = \partial_{SS}^2 C(t, S_t)$ , and the last equality follows from the Black-Scholes PDE. Therefore, the final difference between the hedging strategy and the required option payout is given by

$$Z_T = X_T - [S_T - K]^+$$
  
=  $\frac{1}{2} \int_0^T e^{r(T-t)} S_{t-}^2 \Gamma(t, S_{t-}) (\hat{\sigma}^2 - \kappa_t^2) dt$ 

$$- \int_{[0,T]\times\mathbb{R}} \mathrm{e}^{r(T-t)} \bigg( \int_0^1 \int_0^{\epsilon} \Gamma(t, S_{t-}(1+\epsilon' v_t(z))) \times v_t^2(z) S_{u-}^2 \mathrm{d}\epsilon' \mathrm{d}\epsilon \bigg) \pi(\mathrm{d}t, \mathrm{d}z) - M_T \tag{48}$$

where  $M_T$  is the terminal value of the martingale

$$M_{t} = \int_{[0,T]\times\mathbb{R}} \mathrm{e}^{r(T-t)} \bigg( \int_{0}^{1} \int_{0}^{\epsilon} \Gamma(t, S_{t-}(1+\epsilon' v_{t}(z))) \times v_{t}^{2}(z) S_{u-}^{2} \mathrm{d}\epsilon' \mathrm{d}\epsilon \bigg) (\mu - \pi) (\mathrm{d}t, \mathrm{d}z) \tag{49}$$

Equation  $(48)$  is a key formula, as it shows that successful hedging is quite possible even under significant model error. Without some "robustness" property of this kind, it is hard to imagine that the derivatives industry could exist at all, since hedging under realistic conditions would be impossible.

Consider first the case  $\mu \equiv 0$ , where  $S_t$  has continuous sample paths and the last two terms in equation (48) vanish. Then, successful hedging depends entirely on the relationship between the implied volatility  $\hat{\sigma}$  and the true "local volatility"  $\kappa_t$ . Note from Table 1 that  $\Gamma_t > 0$ . If we, as option writers, are lucky and  $\hat{\sigma}^2 \geq \beta_t^2$  a.s. for all t, then the hedging strategy makes a profit with probability  $1$  even though the true price model is substantially different from the assumed model as in equation (1). On the other hand, if we underestimate the volatility, we will consistently make a loss. The magnitude of the profit or loss depends on the option convexity  $\Gamma$ . If  $\Gamma$  is small, then hedging error is small even if the volatility has been grossly misestimated.

For the option writer, jumps in either direction are unambiguously bad news. Since  $C$  is convex,  $\Delta C > (\partial C/\partial S)\Delta S$ , so the last term in equation  $(47)$  is monotone decreasing: the hedge profit takes a hit every time there is a jump, either upward or downward, in the underlying price. However, there is some recourse: in equation (48),  $M_T$  has expectation  $0$  while the penultimate term is negative. By increasing  $\hat{\sigma}$  we increase  $\mathbb{E}[Z_T]$ , so we could arrive at a situation where  $\mathbb{E}[Z_T] > 0$ , although in this case there is no possibility of with probability  $l$  profit because of the martingale term. All of this reinforces the trader's intuition that one can offset additional hedge costs by charging more upfront (i.e.,

increasing *σ*ˆ ) and hedging at the higher level of implied volatility.

# **End Notes**

a*.* A two-parameter function is *C*<sup>1</sup>*,*<sup>2</sup> if it is once (twice) continuously differentiable in the first (second) argument.

# **References**

[1] Applebaum, D. (2004). *L´evy Processes and Stochastic Calculus*, Cambridge University Press.

- [2] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [3] El Karoui, N., Jeanblanc-Picque, M. & Shreve, S.E. ´ (1998). Robustness of the Black and Scholes formula, *Mathematical Finance* **8**, 93–126.
- [4] Fouque, J.-P., Papanicolaou, G. & Sircar, K.R. (2000). *Derivatives in Financial Markets with Stochastic Volatility*, Cambridge University Press.
- [5] Gatheral, J. (2006). *The Volatility Surface*, Wiley.
- [6] Hull, J.C. 2005. *Options, Futures and Other Derivatives*, 6th Edition, Prentice Hall.

MARK H.A. DAVIS
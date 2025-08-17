# **American Options**

An American option is a contract between the seller and the buyer. It is characterized by a nonnegative random function of time  $Z$  and a maturity. The option can be exercised at any time  $t$  between the initial date and the maturity. If the buyer exercises the option at time  $t$ , he/she receives the amount of money  $Z(t)$  at time t. The buyer may exercise the option only once before the maturity. The price of an American option is always greater than or equal to the price of the corresponding European option (see **Black–Scholes Formula**). Indeed, the buyer of an American option gets more rights than the one who holds a European option, as he/she may exercise the option at any time before the maturity. This is the right of early exercise, and the difference between the American and European options prices is called the early exercise premium. The basic American options are American call and put options (see Call Options): they allow the buyer to sell or buy a financial asset at a price  $K$  (the strike price) and before a date (maturity) agreed before. The function  $Z$  associated to the call (respectively put) option is then  $Z(t) = (S_t - K)^+$  (respectively  $Z(t) = (K - S_t)^{+}$ , where  $S_t$  is the value at time t of the underlying financial asset.

The study of American options began in 1965 with McKean [41] who considered the pricing problem as an optimal stopping problem and reduced it to a free boundary problem. The option value is then computable if one knows the free boundary called the optimal exercise boundary. In 1976, Van Moerbecke [48] exhibited some properties of this boundary. The formalization of the American option pricing problem as an optimal stopping problem was done in the two pioneering works of Benssoussan and Karatzas [5, 32].

They have proved that, under no arbitrage and completeness assumptions (see Complete Markets), the value process of an American option is the Snell envelope of the pay-off process, that is, the smallest supermartingale greater than the pay-off process. From previous works on these processes [23], we can derive some properties of the value process. Especially, we obtain characterization of optimal exercise times. In the section American Option and Snell Envelope, we present the main results and some numerical methods based on this characterization of the option value process.

We can adopt a complementary point of view to study an American option. If we specify the evolution model for the underlying assets of the option, we could characterize the option value as the solution of a variational inequality. This method, introduced by Benssoussan and Lions [6], was applied to American options by Jaillet *et al.* [31]. We present this variational approach in the section Analytic Properties of American Options. We conclude this survey by giving results on exercise regions. In particular, we recall a formula linking the European and the American option prices known as the early exercise premium formula (see the section Exercise Region).

## **American Option and Snell Envelope**

To price and hedge an American option, we have to choose a model for the financial market. We consider a filtered probability space  $(\Omega, \mathbb{F} = (\mathcal{F}_t)_{0 \le t \le T}, \mathbb{P}),$ where T is the maturity of our investment,  $\mathcal{F}_t$  the information available at time t, and  $\mathbb{P}$  the historical probability. We assume that the market is composed of  $d + 1$  assets:  $S^0$ ,  $S^1$ , ...,  $S^d$ .  $S^0$  is a deterministic process representing the time value of money. The others are risky assets such that  $S_t^i$  is the value of asset  $i$  at time  $t$ . In this section, we assume that the market does not offer arbitrage opportunities and is complete (see Complete Markets). Harisson and Pliska [28] observed that the no arbitrage assumption is equivalent to the existence of a probability measure equivalent to the historical one under which the discounted asset price processes are martingales. In a complete market, such a probability measure is unique and called the risk-neutral probability measure (see Risk-neutral Pricing). We will denote it by  $\mathbb{P}^*$ .

# American Option Pricing

We present the problems linked to the American option study. The first one is the option pricing. An American option is characterized by an adapted and nonnegative process  $(Z_t)_{t>0}$ , which represents the option pay-off if its owner exercises it at time  $t$ . We generally define  $Z$  as a function of one or several underlying assets. For instance, for a call option with strike price K, we have  $Z_t = (S_t - K)^+$ 

or for a put option on the minimum of two assets, we have  $Z_t = (K - \min(S_t^1, S_t^2))^+$ . There also exist options, called *Amerasian options*, where the pay-off depends on the whole path of the assets, for instance,  $Z_t = \left(K - \frac{1}{t} \int_0^t S_u \, \mathrm{d}u\right)^\top.$ 

Using arbitrage arguments, Benssoussan and Karatzas [5, 32] have shown that the discounted American option value at time  $t$  is the Snell envelope of the discounted pay-off process [19, 43]. For the definition and general properties on the Snell envelope, we refer to [23] for continuous time and to [44] for discrete time. We can then assert that the price at time  $t$  of an American option with pay-off process  $Z$  and maturity  $T$  is

$$P_{t} = \text{esssup}_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}_{\mathbb{P}^{*}} \left[ \frac{S_{t}^{0}}{S_{\tau}^{0}} Z_{\tau} \mid \mathcal{F}_{t} \right] \tag{1}$$

where  $\mathcal{T}_{t,T}$  is the set of  $\mathbb{F}$ -stopping times with values in  $[t, T]$ .

The second problem appearing in the option theory consists in determining a hedging strategy for the option seller (see **Hedging**). The solution follows directly from the Snell envelope properties. Indeed, if  $X$  is a process, we will denote the discounted process by  $\tilde{X} = \frac{X}{\varsigma_0}$  and we have the following result ([35, Corollary 10.2.4]).

**Proposition 1** The process  $(\tilde{P}_t)_{0 \le t \le T}$  is the smallest right-continuous super martingale that dominates  $(Z_t)_{0 \le t \le T}.$ 

As  $(\tilde{P}_t)_{0 \le t \le T}$  is a super martingale, it admits a Doob decomposition (see Doob-Meyer Decom**position**). There exist a unique right-continuous martingale  $(M_t)_{0 \le t \le T}$  and a unique nondecreasing, continuous, adapted process  $(A_t)_{0 \le t \le T}$  such that  $A_0 = 0$  and  $\tilde{P}_t = M_t - A_t$  for all  $t \in [0, T]$ . This decomposition of  $P$  is very useful to determine a surreplication strategy for an American option (see **Superhedging**). A strategy is defined as a predictable process  $(\phi_t)_{0 \le t \le T}$  such that the value, at time *t*, of the portfolio associated with this strategy is  $V_t(\phi) =$  $\sum_{i=0}^{d} \phi_t^i S_t^i$ . In a complete market, each contingent claim is replicable; then there exists a self-financing strategy  $\phi$  such that  $V_T(\phi) = S_T^0 M_T$ . As  $\tilde{V}(\phi)$  is a martingale under the risk-neutral probability, we get  $\tilde{V}_t(\phi) = M_t$  for all  $t \in [0, T]$ . In conclusion, we have constructed a self-financing strategy such that

$$\forall t \in [0, T], \quad V_t(\phi) = P_t + S_t^0 A_t \ge P_t \quad (2)$$

This is a surreplication strategy for American options. Moreover, for this strategy, the initial wealth for hedging the option is minimum because we have  $V_0(\phi) = P_0.$ 

The third problem arising in the American option theory is linked to early exercise opportunity. Contrary to European options, for the American option holder, knowing the arbitrage price of his/her option is not enough. He/she has to know when it is optimal for him/her to exercise the option. The tool to study this problem is the optimal stopping theory.

#### *Optimal Exercise*

We recall some useful results of the optimal stopping theory and apply them to the American put option in the famous Black-Scholes model. These results are proved in [23] in a larger setting and their financial applications have been developed in [35]. An optimal stopping time for an American option holder is a stopping time that maximizes his/her gain. Consequently, a stopping time  $\nu$  is optimal if we have

$$\mathbb{E}_{\mathbb{P}^*}[\tilde{Z}_{\nu}] = \text{esssup}_{\tau \in \mathcal{T}_0 \, \tau} \mathbb{E}_{\mathbb{P}^*}[\tilde{Z}_{\tau} \mid \mathcal{F}_t] \tag{3}$$

We have a characterization of optimal stopping times, thanks to the following theorem.

**Theorem 1** Let  $\tau^* \in \mathcal{T}_{0,T}$ .  $\tau^*$  is an optimal stopping time if and only if  $P_{\tau^*} = Z_{\tau^*}$  and the process  $(\tilde{P}_{t \wedge \tau^*})_{0 \le t \le T}$  is a martingale.

It follows from this result that the stopping time

$$\tau^* = \inf\{t \ge 0: \ P_t = Z_t\} \wedge T \tag{4}$$

is an optimal stopping time and, obviously, it is the smallest one. We can easily determine the largest optimal stopping time by using the Doob decomposition of super martingale. We introduce the following stopping time:

$$\nu^* = \inf\{t \ge 0: A_t > 0\} \wedge T \tag{5}$$

and it is easy to see that  $v^*$  is the largest optimal stopping time.

We then apply these results to an American put option in Black-Scholes framework (see Black-Scholes Formula). We assume that the underlying asset  $S$  of the option is solution, under the risk-neutral probability, to the following equation:

$$dS_t = S_t (r dt + \sigma dW_t)$$
 (6)

with  $r, \sigma > 0$  and W a standard Brownian motion.

From the Markov property of  $S$ , we can deduce that the option price at time t is  $P(t, S_t)$ , where

$$P(t,x) = \sup_{\tau \in \mathcal{T}_{0,T-t}} \mathbb{E}_{\mathbb{P}^*}[\mathrm{e}^{-r\tau} (K - S_{\tau})^+ | S_0 = x] \tag{7}$$

It is easy to see that  $t \to P(t,x)$  is nonincreasing for all  $x \in [0, +\infty)$ . Moreover, for  $t \in [0, T]$ , the function  $x \to P(t, x)$  is convex [24, 29, 30]. From the convexity of  $P$ , we deduce that there exists a unique optimal stopping time:  $\tau^* = \inf\{t > 0 :$  $P(t, S_t) = (K - S_t)^{+} \wedge T$ . We introduce the socalled critical price or free boundary  $s(t) = \inf\{x \in$  $[0, +\infty)$ :  $P(t, x) > (K - x)^{+}$  and can write that

$$\tau^* = \inf\{t \ge 0 : S_t \le s(t)\} \wedge T$$
$$= \inf\{t \ge 0 : W_t \le \alpha(t)\} \wedge T$$
$$\text{with } \alpha(t) = \frac{1}{\sigma} \left( \ln \left( \frac{s(t)}{S_0} \right) - \left( r - \frac{\sigma^2}{2} \right) t \right) (8)$$

Hence,  $\tau^*$  is the reaching time of  $\alpha$  by a Brownian motion. If  $\alpha$  was known, we could compute  $\tau^*$ and then  $P$ . However, the only way to get the law of  $\tau^*$  explicitly is to reduce the dimension by considering options with infinite maturity (also known as *perpetual options*). In this case, we have the following result ( $[37,$  Proposition 4.5]).

Proposition 2 The value function of an American perpetual put option is

$$P^{\infty}(x) = \sup_{\tau \in \mathcal{T}_{0+\infty}} \mathbb{E}_{\mathbb{P}^*} [e^{-r\tau} (K - S_{\tau})^+ \times \zeta_{\tau < +\infty} | S_0 = x]$$
(9)

and is given by

$$P^{\infty}(x) = \begin{cases} K - x & \text{if } x \le s^* \\ (K - s^*) \left(\frac{s^*}{x}\right)^{\gamma} & \text{if } x > s^* \end{cases}$$
  
where  $\gamma = \frac{2r}{\sigma^2}$  and  $s^* = \frac{K\gamma}{1+\gamma}$  (10)

is the critical price.

Another technique to reduce the dimension of the problem is the randomization of the maturity applied in  $[9, 13]$ , but only approximations of the option price can be obtained in this way. In the following section, we present methods to approximate  $P$  based on the discretization of the problem.

#### Approximation of the American Option Value

To approximate  $P_t$ , it is natural to restrict the set of exercise dates to a finite one. We then introduce a subdivision  $S = \{t_1, \ldots, t_n\}$  of the interval [0, T] and assume that the option owner can exercise only at a date in S. Such options are called *Bermuda options* and their price at time  $t$  is given by

$$P_t^n = \text{esssup}_{\tau \in \mathcal{T}_{t}^n} \mathbb{E}[S_t^0 \tilde{Z}_{\tau} \mid \mathcal{F}_t] \tag{11}$$

where  $T_{t,T}^n$  is the set of  $\mathbb{F}$ -stopping times with values in  $S \cap [t, T]$ . We obviously have  $\lim_{n \to +\infty} P^n = P$ and some estimates of the error have been given in [1, 15]. For perpetual put options, Dupuis and Wang [21] have obtained a first-order expansion of the error on the value function and on the critical prices. In the case of finite maturity, this problem is still open; we just know that the error is proportional to  $\frac{1}{n}$  for<br>the value function and to  $\frac{1}{\sqrt{n}}$  for the critical prices [18].

We have to determine  $P_{t_i}^n$  for all  $i \in \{1, \ldots, n\}$ . For this, we use the so-called dynamic programming equation:

$$\begin{cases} P_{T}^{n} = Z_{T} \\ P_{t_{i}}^{n} = \max\left(Z_{t_{i}}, \mathbb{E}_{\mathbb{P}^{*}}\left[\frac{S_{t_{i}}^{0}}{S_{t_{i+1}}^{0}} P_{t_{i+1}}^{n} \mid \mathcal{F}_{t_{i}}\right]\right) \end{cases}$$
(12)

This equation is easy to understand with financial arguments. At maturity of the option, it is obvious that the option price  $P_T^n$  is equal to the pay-off  $Z_T$ . At time  $t_i < T$ , the option holder has two choices: he/she exercises and then earns  $Z_{t_i}$ ; else he/she keeps the option and then would have the option value at time  $n + 1$ ,  $P_{t_{i+1}}^n$ . Hence, using the no arbitrage assumption, one can prove that at time  $t_i$  the option seller should receive

$$\max\left(Z_{t_{i}}, \ \mathbb{E}_{\mathbb{P}^{*}}\left[\frac{S_{t_{i}}^{0}}{S_{t_{i+1}}^{0}}P_{t_{i+1}}^{n} \mid \mathcal{F}_{t_{i}}\right]\right) \qquad (13)$$

Computing the Bermuda option price consists now in calculating the expectations in the dynamic programming equation. On the one hand, Monte Carlo techniques have been applied to solve this problem (see Monte Carlo Simulation for Stochastic Differential Equations; Bermudan Options and  $[11]$ ). More precisely, we can quote some regression methods based on projections on Hilbert space base  $[40, 47]$ , quantization algorithms proposed in  $[1, 2]$ , and some Monte Carlo methods based on Malliavin calculus [3, 8]. On the other hand, we can use a discrete approximation of the underlying assets process. A widely used model is the Cox, Ross, and Rubinstein model (see **Binomial Tree**). We introduce a family of independent and identically distributed Bernouilli variables  $(U_n)_{1 \le n \le N}$  with values in  $\{b, h\}$ , where  $-1 < b < h$ . We then consider only two assets  $S^0$  and S whose respective initial values are 1 and  $S_0$ such that

$$S_n^0 = (1+r)^n$$
 and  $S_n = S_{n-1}(1+U_n)$   
 $\forall n \in \{1, ..., N\}$  (14)

where  $r > 0$  is the constant interest rate of the market. From the no arbitrage assumption, it follows that  $b < r < h$  and that, under the risk-neutral probability  $\mathbb{P}^*$ , we have  $p := \mathbb{P}^*(U_1 = h) = \frac{r-b}{h-b}$ . Hence, using the Markov property of *S*, we can price an American option on S. For instance, for a call option with exercise price K, we get  $P_n = F(n, S_n)$ , where F is the solution to the following equation:

$$F(N, x) = (K - x)^{+}$$
  

$$F(n, x) = \max \left\{ K - x, \frac{1}{1+r} \times (pF(n+1, x(1+h))) + (1-p)F(n+1, x(1+b))) \right\}$$
(15)

The convergence of binomial approximations was first studied in a general setting in [34]. The rate of convergence is difficult to get, but some estimates are given in [36, 38].

In conclusion, for some simple models, one can numerically solve the option pricing problem. However, only the time variable is discretized. Analytical methods have been developed and provide a better understanding of the links between time and space variables. In particular, we can characterize the option value as a solution to a variational inequality and get an approximation of its solution, thanks to finite difference methods. This characterization has many consequences from the theoretical point of view and on practical aspects.

#### **Analytic Properties of American Options**

In this section, we assume that the assets prices process follows a model called local volatility model (see **Local Volatility Model**). This model is complete and takes into account the smile of volatility observed when one calibrates the Black-Scholes model (see Model Calibration; Implied Volatility Surface and  $[20]$ ). We suppose that the assets prices process is solution to the following stochastic differential equation:

$$dS_t^i = S_t^i \left( b_i \left( t, S_t \right) dt + \sum_{j=1}^d \sigma_{i,j} \left( t, S_t \right) dW_t^j \right) \tag{16}$$

where W is a standard Brownian motion on  $\mathbb{R}^d$ , b a function mapping  $[0, T] \times [0, +\infty)^d$  into  $\mathbb{R}^d$ , and  $\sigma$  a function mapping  $[0,T] \times [0,+\infty)^d$  into  $\mathbb{R}^{d \times d}$ . Moreover, we assume that  $b$  is bounded and Lipschitz continuous, that  $\sigma$  is Lipschitz continuous in the space variable, and that there exists  $\alpha \ge 1/2$  and  $\sigma_H$ such that  $\forall x \in [0, +\infty), (t, s) \in [0, T]^2, \mid \sigma(t, x) \sigma(s,x) \leq \sigma_H |t-s|^{\alpha}$ . Moreover, to ensure the completeness of the market and the nondegeneracy of the partial differential equation satisfied by European option price functions, we assume that there exist  $m > 0$  and  $M > 0$  such that

$$\forall (t, x, \xi) \in [0, T] \times [0, +\infty)^d \times \mathbb{R}^d,$$
  
$$m^2 \|\xi\|^2 \le \xi^* \sigma^* \sigma(t, x) \xi \le M^2 \|\xi\|^2 \qquad (17)$$

From the Markov property of the process  $S$ , at time  $t$ , the price of an American option with maturity T and pay-off process  $(f(S_t))_{0 \le t \le T}$  is  $P(t, S_t)$ , where

$$P(t,x) = \sup_{\tau \in \mathcal{I}_{t,T}} \mathbb{E}\left[e^{-r(\tau-t)}f(S_{\tau}) \mid S_t = x\right] \quad (18)$$

## The Value Function

To compute the option price, we now have to study the option value function  $P$ . From its definition, we can derive immediate properties:

 $\bullet \quad \forall x \in [0, +\infty)^d, \ P(T, x) = f(x)$ 

- $\forall (t, x) \in [0, T] \times [0, +\infty)^d, P(t, x) \ge f(x)$ .
- If the coefficients  $\sigma$  and b do not depend on time, we can write

$$P(t,x) = \sup_{\tau \in \mathcal{T}_{0,T-t}} \mathbb{E}\left[e^{-r\tau}f(S_{\tau}) \mid S_0 = x\right] \quad (19)$$

then the function  $t \to P(t,x)$  is nonincreasing on  $[0, T].$ 

Up to imposing some assumptions on the regularity of the pay-off function, we can derive some important continuity properties of  $P$ . In this section, we assume that  $f$  is nonnegative and continuous on  $[0, +\infty)$  such that

$$\exists (M, n) \in [0, +\infty) \times \mathbb{N}, \ \forall x \in [0, +\infty)^d,$$
$$|f(x)| + \sum_{i=1}^d \left| \frac{\partial f}{\partial x_i}(x) \right| \le M(1 + |x|^n) \quad (20)$$

These assumptions are generally satisfied by the pay-off functions appearing in finance, especially by the pay-off functions of put and call options. In this setting, we have the following result [31].

**Proposition 3** There exists a constant  $C > 0$  such that

$$\forall t \in [0, T], \ \forall (x, y) \in [0, +\infty)^{2d},$$
$$| P(t, x) - P(t, y) | \le C | x - y | \tag{21}$$

$$\forall x \in [0, +\infty)^{a}, \ \forall (t, s) \in [0, T]^{2},$$
$$\mid P(t, x) - P(s, y) \mid \leq C \left| (T - t)^{\frac{1}{2}} - (T - s)^{\frac{1}{2}} \right| \tag{22}$$

As a consequence of this result, we can assert that the first-order derivatives of  $P$  in the sense of distributions are locally bounded on the open set  $(0, T) \times (0, +\infty)^d$ . This plays a crucial role in the characterization of  $P$  as a solution to a variational inequality.

#### Variational Inequality

In a more general setting, Benssoussan and Lions [6] have studied existence and uniqueness of solutions of variational inequalities and linked these solutions to those of optimal stopping problems. Applying this method to the American option problem, Jaillet *et al.* have proved that the value function  $P$  can be characterized as the unique solution, in the sense of distribution, of the following variational inequality [31]:

$$\begin{cases}\n\mathcal{D}P \le 0, & f \le P, \quad (P - f)\mathcal{D}P = 0 \quad \text{a.e.} \\
P(x,T) = f(x) \quad \text{on} \quad [0, +\infty)\n\end{cases}\n$$
(23)

where we set

$$\mathcal{D}h(t,x) = \frac{\partial h}{\partial t} + \frac{1}{2} \sum_{i,j=1}^{d} (\sigma \sigma^*)_{i,j}(t,x) x_i x_j \frac{\partial^2 h}{\partial x_i x_j}$$
$$+ \sum_{i=1}^{d} b_i(t,x) x_i \frac{\partial h}{\partial x_i} - rh \qquad (24)$$

This inequality directly derives from the properties of the Snell envelope. Indeed, the condition  $\mathcal{D}P \leq 0$ is the analytic translation of the super martingale property of  $\tilde{P}$ ,  $f \leq P$  corresponds to  $Z \leq P$ , and the fact that one of this two inequalities has to be an equality follows from the martingale property of  $(P_{t \wedge \tau^*})_{0 \le t \le T}.$ 

From the variational inequality, we can use numerical methods, such as finite difference methods, to compute the option price (see Finite Difference Methods for Early Exercise Options and [31]). From a theoretical point of view, we can deduce some analytic properties of  $P$ . If we add the condition that second-order derivatives of the pay-off function are bounded from below, we have the following result.

## **Proposition 4** Regularity of $P$

- 1. Smooth fit property: For  $t \in [0, T)$ , the function  $x \rightarrow P(t,x)$  is continuously differentiable and its first derivatives are uniformly bounded on  $[0, T] \times [0, +\infty)^d$ .
- There exists a constant  $C > 0$  such that for all 2.  $(t, x) \in [0, T) \times [0, +\infty)^d$ , we have

$$\left| \frac{\partial P}{\partial t}(t,x) \right| + |D^2 P(t,x)| \le \frac{C}{(T-t)^{\frac{1}{2}}} \tag{25}$$

where  $D^2P$  is the Hessian matrix of P.

The *smooth fit property* has equally been established with probabilistic arguments, using the early exercise premium formula presented in the section Exercise Region [30, 43]. In connection with free boundary problems, some analytic methods have been developed in [26] from which we can deduce the continuity of  $\frac{\partial P}{\partial t}$  on  $[0, T) \times [0, +\infty)^d$ .<br>Thanks to the variational inequality, we can estab-

lish the so-called robustness of Black-Scholes formula [24]. The two main results obtained are the following.

**Proposition 5** We assume that  $d = 1$ . If the pay-off function is convex, then the value function  $P$  is equally *convex. Moreover, if there exist*  $\sigma_1$ ,  $\sigma_2 > 0$  *such that*  $\sigma_1 \leq \sigma \leq \sigma_2$ , then we have

$$P^{\sigma_1} < P < P^{\sigma_2} \tag{26}$$

where  $P^{\sigma_i}$  is the value function of the American option on an underlying asset with volatility  $\sigma_i$ .

The propagation of convexity has been proved with probabilistic arguments in [29] and can be extended to the case  $d > 1$ . The robustness of Black-Scholes formula is equally useful from a practical point of view because it allows to construct surreplication and subreplication strategies using a constant volatility.

When there is only one risky asset modeled as a geometric Brownian motion, the analytic properties presented in this section can be used to transform, thanks to Green's theorem, the variational inequality in an integral equation (see Integral Equation **Methods for Free Boundaries**). This point of view has been adopted to provide new numerical methods  $[16]$  to get theoretical results such as the convexity of the critical price for the put option  $[22]$  or its behavior near maturity [16, 25].

## Integro-differential Equation

The integro-differential approach can be extended to the American option on jump diffusions (see Partial Integro-differential Equations (PIDEs)). In 1976, Merton (see Merton, Robert C. and [42]) introduced a model including some discontinuities in the assets value process. He considered a risky asset whose value process is solution to the following equation:

$$dS_t = S_{t^-} \left( \mu dt + \sigma dW_t + d \left( \sum_{i=1}^{N_t} U_i \right) \right) \qquad (27)$$

where  $\mu \in \mathbb{R}, \ \sigma > 0, \ W$  is a standard Brownian motion, N is a Poisson process with intensity  $\lambda >$ 0, and the  $U_i$  are independent and identically distributed variables with values in  $(-1, +\infty)$  such that  $\mathbb{E}[U_i^2] < +\infty.$ 

This model is not complete but up to a change of probability measure, we can suppose that  $\mu =$  $r - \lambda \mathbb{E}[U_1]$ , where  $r > 0$  is the constant interest rate of the market. Hence,  $\tilde{S}$  is a martingale with respect to the filtration generated by *W*, *N*, and  $(U_i \zeta_{i \leq N_t})_{0 \leq t \leq T}$ . The option price is then determined as the initial wealth of a replication portfolio, which minimizes the quadratic risk. Merton obtained closed formulas to calculate the European options price. In this model, Zhang [50] extended the variational inequality approach to evaluate the American options price and he got a characterization of the value function as solution to the following integro-differential equation:

$$\begin{cases}\n\mathcal{D}P + \mathcal{I}P \le 0, & f \le P, \\
(\mathcal{D}P + \mathcal{I}P)(P - f) = 0 \quad \text{a.e.} \\
P(x, T) = f(x) \quad \text{on} \quad [0, +\infty)\n\end{cases} \tag{28}$$

with

$$\mathcal{D}h(t,x) = \frac{\partial h}{\partial t} + \frac{\sigma^2 x^2}{2} \frac{\partial^2 h}{\partial x^2} + \mu x \frac{\partial h}{\partial x} - rh$$
  
$$\mathcal{I}h(t,x) = \lambda \int \left( h(t,x+z) - h(t,x) \right) \nu(dz) \tag{29}$$

where  $\nu$  is the law of  $\ln(1+U_1)$ . Zhang used this equation to derive numerical schemes for approximating  $P$ . However, he could not obtain a description of the optimal exercise strategies. This was studied by Pham [46] who obtained a pricing decomposition formula and some properties of the exercise boundary.

In conclusion, analytic properties of the American option value function have been used to build numerical methods of pricing and to get some theoretical properties. Although the variational point of view is better for understanding the discretization of American options, it is less explicit than the probabilistic methods. We can remark that a specific region of  $[0,T] \times [0,+\infty)^d$  appears in these two approaches: the so-called exercise region

$$\mathcal{E} = \{(t, x) \in [0, T) \times [0, +\infty)^d : P(t, x) = f(x)\}$$
(30)

If we knew  $\mathcal{E}$ , on the one hand, we would be able to determine the law of optimal stopping times and, on the other hand, the option pricing problem would be reduced to solving a partial differential equation in the complementary set of  $\mathcal{E}$ . In the following section, we recall some results on exercise regions and in particular we give a price decomposition, known as the early exercise premium formula, which involves the exercise region.

## **Exercise Region**

#### Description

In the section Optimal Exercise, we have already presented a brief description of the exercise region of an American put option on a single underlying following the Black-Scholes model. These results are still true in the local volatility model introduced in the section Analytic Properties of American Options. Hence, for a put option with maturity  $T$  and strike price  $K$ , we have

$$\mathcal{E} = \{(t, x) \in [0, T) \times [0, +\infty); x \le s(t)\}$$
 with

$$s(t) = \inf\{x \in [0, +\infty) : P(t, x) = f(x)\}\tag{31}$$

Using the integral equation satisfied by  $P$  in the Black-Scholes model, we can apply general results proved in [27] for free boundary problems and assert that  $s$  is continuously differentiable on  $[0, T)$ . It has been shown that this is still true in the local volatility model using some blow-up techniques and monotonicity formulas [7, 12]. Moreover, Kim [33] proved that  $\lim_{t\to T} s(t) = \min(K, \frac{rK}{s})$  if S is solution to  $dS_t = S_t((r - \delta)dt + \sigma(t, S_t)dW_t)$ . We will see that the behavior of  $s$  near maturity has been extensively studied.

The description of exercise region for options on several assets is more interesting because in high dimension numerical methods are less efficient and it helps to have a better understanding of these products. Broadie and Detemple were the first to investigate this problem [10]. They give precise descriptions of the exercise region shapes for the most traded options on several assets. Their results were completed by Villeneuve [49]. In particular, he gives a characterization of the nonemptiness of the exercise region. We just quote here the main results concerning a call option on the maximum on two

assets but the same kinds of results exist for many others options.

We denote by  $\mathcal{E}_t$  the temporal section of the exercise region. For a call option on the maximum of two assets,  $S^1$  and  $S^2$   $\mathcal{E}_t$  can be decomposed in two regions:  $\mathcal{E}_t^1 = \mathcal{E}_t \cap \{(x_1, x_2) \in [0, +\infty)^2 : x_2 \leq$  $x_1$ } and  $\mathcal{E}_t^2 = \mathcal{E}_t \cap \{(x_1, x_2) \in [0, +\infty)^2 : x_1 \le x_2\}.$ These two regions are convex and can be rewritten as follows:

$$\mathcal{E}_t^1 = \{ (x_1, x_2) \in [0, +\infty)^2 : s_1(t, x_2) \le x_1 \} \text{ and}$$
  
$$\mathcal{E}_t^2 = \{ (x_1, x_2) \in [0, +\infty)^2 : s_2(t, x_1) \le x_2 \} \quad (32)$$

where  $s_1$  and  $s_2$  are the respective continuous boundaries of  $\mathcal{E}_1(t)$  and  $\mathcal{E}_2(t)$ .

To compute these boundaries, we can use the early exercise premium formula given in the following section.

#### Early Exercise Premium Formula

About the same time, many authors have exhibited a decomposition formula for the American option price  $[14, 30, 43]$ . This formula is very enlightening from a financial point of view because it consists in writing that  $P_t = P_t^e + a_t$  where  $P_t^e$  is the corresponding European option price and  $a$  is a nonnegative function of time corresponding to the premium the option buyer has to pay to get the right of early exercise. If the exercise region is known, a closed formula allows us to compute this premium. We recall this formula for a put option on a dividend-paying asset following the Black-Scholes model:

$$P(t,x) = P^{e}(t,x) + \int_{t}^{T} \mathbb{E}_{\mathbb{P}^{*}}[e^{-r(u-t)}(\delta S_{u} - rK) \times \zeta_{\{S_{u} \geq s(u)\}} | S_{t} = x] du$$
(33)

where  $\delta > 0$  is the dividend rate and  $P^{e}(t, x) =$  $\mathbb{E}_{\mathbb{P}^*}[e^{-r(T-t)}(K-S_T)^+|S_t=x]$ . This formula is equally interesting from a theoretical point of view as it leads to an integral equation for the critical price:

$$K - s(t) = P^{e}(t, s(t)) + \int_{t}^{T} \mathbb{E}_{\mathbb{P}^{*}}[\mathrm{e}^{-ru} \left(\delta S_{u} - rK\right)$$
$$\times \zeta_{\{S_{u} \ge s(u)\}} | S_{t} = s(t)] \, \mathrm{d}u \tag{34}$$

This formula has been extended in [10] to American options on several assets. For the call on the maximum on two assets, we get

$$P(t,x) = P^{e}(t,x) + \int_{t}^{T} \mathbb{E}_{\mathbb{P}^{s}}[e^{-r(u-t)}(\delta_{1}S_{u}^{1} - rK) \times \zeta_{\{S_{u}^{1} \geq s_{1}(u,S_{u}^{2})\}} | S_{t} = x] du$$
$$+ \int_{t}^{T} \mathbb{E}_{\mathbb{P}^{s}}[e^{-r(u-t)}(\delta_{2}S_{u}^{2} - rK) \times \zeta_{\{S_{u}^{2} \geq s_{2}(u,S_{u}^{1})\}} | S_{t} = x] du \qquad (35)$$

Once again an integral equation could be derived for  $(s_1, s_2)$ .

We can also use this formula and the integral equation satisfied by the free boundary to study the behavior of the exercise region for short maturity. This is a crucial point for numerical methods. Indeed, we have seen that both the value function and the free boundary present irregularities near maturity, which implies instability in numerical methods.

## Behavior Near Maturity

The behavior of the exercise region near maturity has been extensively studied when there is only one underlying asset. In his pioneering work, Van Moerbecke conjectured a parabolic behavior for the boundary near maturity [48]. However, when the asset does not distribute dividends, it has been shown that there is an extra logarithmic factor [4]. Lamberton and Villeneuve have then proved that, in the Black-Scholes model, the free boundary has a parabolic behavior if its limit is a point of regularity for the pay-off function, else a logarithmic factor appears [39]. This result has been extended to local volatility model in [17]. In a recent paper [16], new approximations are provided for the location of the free boundary by using integral equation satisfied by  $P$  and  $s$ . However, this technique cannot be extended to the case of options on several assets. When there are several underlying assets, the behavior of the exercise boundary near maturity has been studied by Nyström [45], who has proved that the convergence rate, when time to maturity goes to  $0$ , is faster than parabolic.

# References

- Bally, V. & Pagès, G. (2003). Error analysis of the [1] quantization algorithm for obstacle problems, Stochastic Processes and their Applications 106, 1-40.
- Bally, V., Pagès, G. & Printems, J. (2005). A quantiza-[2] tion method for pricing and hedging multi-dimensional American style options, Mathematical Finance 15,  $119 - 168.$
- [3] Bally, V., Caramellino, L. & Zanette, A. (2005). Pricing American options by Monte Carlo methods using a Malliavin Calculus approach, Monte Carlo Methods and Applications 11, 97-133.
- Barles, G., Burdeau, J., Romano, M. & Sansoen, N. [4] (1995). Critical stock price near expiration, Mathematical finance 5, 77-95.
- [5] Benssoussan, A. (1984). On the theory of option pricing, Acta Applicandae Mathematicae 2, 139–158.
- [6] Benssoussan, A. & Lions, J.L. (1982). Applications of Variational Inequalities in Stochastic Control, North-Holland.
- [7] Blanchet, A. (2006). On the regularity of the free boundary in the parabolic obstacle problem. Application to American options, Nonlinear Analysis 65(7), 1362-1378.
- Bouchard, B., Ekeland, I. & Touzi, N. (2004). On the [8] Malliavin approach to Monte-Carlo approximation of conditional expectations, *Finance and Stochastics* **8**(1),  $45 - 71.$
- Bouchard, B., El Karoui, N. & Touzi, N. (2005). [9] Maturity randomisation for stochastic control problems, Annals of Applied Probability 15(4), 2575-2605.
- [10] Broadie, M. & Detemple, J.B. (1997). The valuation of American options on multiple assets, Mathematical Finance 7, 241-286.
- [11] Broadie, M. & Glasserman, P. (1997). Pricing Americanstyle securities using simulation, Journal of Economic Dynamics and Control 21, 1323-1352.
- [12] Caffarelli, L., Petrosyan, A. & Shahgholian, H. (2004). Regularity of a free boundary in parabolic potential theory, Journal of the American Mathematical Society 17(4), 827-869.
- [13] Carr, P. (1998). Randomization and the American Put, The Review of Financial Studies 11, 597-626.
- [14] Carr, P., Jarrow, R. & Myneni, R. (1992). Alternative characterization of American put options, Mathematical Finance 2, 87-106.
- [15] Carverhill, A.P. & Webber, N. (1990). *American options:* theory and numerical analysis, in Options: Recent Advances in Theory and Practice, S. Hodges, ed, Manchester University Press.
- [16] Chadam, J. & Chen, X. (2007). Analytical and numerical approximations for the early exercise boundary for American put options, to appear in *Dynamics of Contin*uous, Discrete and Impulsive Systems 10, 649-657.
- [17] Chevalier, E. (2005). Critical price near maturity for an American option on a dividend-paying stock in
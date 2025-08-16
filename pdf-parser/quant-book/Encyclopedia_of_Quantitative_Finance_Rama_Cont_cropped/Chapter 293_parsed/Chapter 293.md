## **Risk-sensitive Asset** Management

In risk-sensitive asset management, maximization of the criterion

$$J(v_0;T) = \frac{1}{\gamma} \log E[e^{\gamma \log V_T}] = \frac{1}{\gamma} \log E[V_T^{\gamma}] \quad (1)$$

for  $\gamma < 1, \neq 0$  is considered, where  $V_T$  is the total wealth an investor possesses, defined by  $V_T =$  $\sum_i N_T^i S_T^i$  with  $N_T^i$  the number of shares invested into *i*th security  $S_T^i$  at time T and  $v_0$  the initial wealth. It is equivalent to expected power utility maximization with the criterion  $\frac{1}{\nu}E[V_T^{\gamma}]$ . Looking at asymptotics as  $\gamma \to 0$ ,

$$\frac{1}{\gamma} \log E[e^{\gamma \log V_T}] \sim E[\log V_T]$$
$$+ \gamma \operatorname{Var}[\log V_T] + O(\gamma^2) \tag{2}$$

we see that maximizing the criterion amounts asymptotically to maximizing expected log utility while minimizing its variance if  $\gamma < 0$ . In that sense,  $\gamma < 0$ means risk averse. On the other hand,  $\gamma > 0$  means risk seeking since it comes to maximizing log utility as well as its variance.

The infinite time horizon problem of maximizing

$$\overline{\lim}_{T \to \infty} \frac{1}{T} J(v_0, x; T) = \overline{\lim}_{T \to \infty} \frac{1}{\gamma T} \log E[e^{\gamma \log V_T}]$$
(3)

is often considered in an incomplete market model, where security prices are defined by

$$dS^{0}(t) = r(X_{t})S^{0}(t) dt$$
(4)

$$dS^{i}(t) = S^{i}(t) \left\{ \alpha^{i}(X_{t}) dt + \sum_{k=1}^{n+m} \sigma_{k}^{i}(X_{t}) dW_{t}^{k} \right\} \quad (5)$$

 $i = 1, \ldots m$ , with an  $(n + m)$ -dimensional Brownian motion process  $W_t = (W_t^1, W_t^2, ..., W_t^{n+m})$  defined on a filtered probability space  $(\Omega, \mathcal{F}, P; \mathcal{F}_t)$ . Its volatilities  $\sigma$ , instantaneous mean returns  $\alpha$ , and interest rate  $r$ , are affected by economic factors

 $(X_t^1,\ldots,X_t^n)$  defined as the solution of the stochastic differential equation

$$dX_t = \beta(X_t) dt + \lambda(X_t) dW_t, \quad X(0) = x \in R^n$$
(6)

Introducing portfolio proportion  $h_t^i$  invested into *i*th security defined by  $h^{i}(t) = \frac{N^{i}(t)S^{i}(t)}{V(t)}$  for each  $i =$  $0, \ldots, m$  and setting  $h(t) = (h^1(t), h^2(t), \ldots, h^m(t)),$ the total wealth  $V_t$  turns out to satisfy

$$\frac{\mathrm{d}V(t)}{V(t)} = \{r(X_t) + h(t)^* \hat{\alpha}(X_t)\} \mathrm{d}t$$
$$+ h(t)^* \sigma(X_t) W_t \tag{7}$$

under the self-financing condition, where  $\hat{\alpha}(x)$  =  $\alpha(x) - r(x)$ **1**. In these maximization problems, the portfolio proportion  $h_t$  is considered an investment strategy and assumed to be  $\mathcal{G}^{S,X}_t := \sigma(S(u), X(u),$  $u \leq t$ ) progressively measurable in the case of full information. The problem is often considered under partial information where  $h_t$  is assumed to be  $\mathcal{G}_t^S$  :=  $\sigma(S(u), u \leq t)$  measurable. Here we discuss the case of full information and the set of admissible strategies  $\mathcal{A}(T)$  (or  $\mathcal{A}$ ) is determined as the totality of  $\mathcal{G}^{S,X}_t$  progressively measurable investment strategies satisfying some suitably defined integrability conditions.

If  $\gamma < 0$ , introducing the value function

$$\hat{v}(t,x) = \inf_{h \in \mathcal{A}(T-t)} \log E[e^{\gamma \log V_{T-t}(h)}] \qquad (8)$$

we see that

1

$$\sup_{h} J(v_0, x; T) = \frac{1}{\gamma} \hat{v}(0, x) \tag{9}$$

Under the change of measure,

$$P^{h}(A) = E\left[e^{\gamma \int_{0}^{T} h_{s}^{*}\sigma(X_{s})dW_{s} - \frac{\gamma^{2}}{2} \int_{0}^{T} h_{s}^{*}\sigma\sigma^{*}(X_{s})h_{s}ds} : A\right]$$
(10)

the value function is expressed as

$$\hat{v}(t,x) = \gamma \log v_0 + \inf_{h \in \mathcal{A}(T)} \log E^h \left[ e^{\gamma \int_0^{T-t} \eta(X_s, h_s) \mathrm{d}s} \right]$$
(11)

with the initial wealth  $v_0$ , where

$$\eta(x,h) = h^*\hat{\alpha}(x) - \frac{1-\gamma}{2}h^*\sigma\sigma^*(x)h + r(x) \tag{12}$$

By using the Brownian motion  $W_t^h := W_t \gamma \int_0^t \sigma^*(X_s) h_s \, ds$  under the new probability measure  $P^h$  the dynamics of economic factor  $X_t$  is written as

$$dX_{t} = \left\{ \beta(X_{t}) + \gamma \lambda \sigma^{*}(X_{t}) h_{t} \right\} dt + \lambda(X_{t}) dW_{t}^{h}$$
(13)

Thus the Hamilton–Jacobi–Bellman  $(H-J-B)$  equation for the value function is deduced as

$$\begin{cases} \frac{\partial v}{\partial t} + \frac{1}{2} \text{tr}[\lambda \lambda^* D^2 v] + \frac{1}{2} (Dv)^* \lambda \lambda^* Dv \\ + \inf_h \{ [\beta + \gamma \lambda \sigma^* h]^* Dv + \gamma \eta(x, h) \} = 0 \\ v(T, x) = \gamma \log v_0 \end{cases}$$
(14)

which can be rewritten as

$$\begin{cases} \frac{\partial v}{\partial t} + \frac{1}{2} \text{tr}[\lambda \lambda^* D^2 v] + \beta_\gamma^* D v \\ + \frac{1}{2} (D v)^* \lambda N_\gamma^{-1} \lambda^* D v - U_\gamma = 0 \\ v(t, x) = \gamma \log v_0 = 0 \end{cases}$$
(15)

where

$$\beta_{\gamma} = \beta + \frac{\gamma}{1 - \gamma} \lambda \sigma^* (\sigma \sigma^*)^{-1} \hat{\alpha} \tag{16}$$

$$N_{\gamma}^{-1} = I + \frac{\gamma}{1-\gamma} \sigma^* (\sigma \sigma^*)^{-1} \sigma \tag{17}$$

$$U = \frac{\gamma}{\gamma} \hat{\sigma}^* (\sigma \sigma^*)^{-1} \hat{\sigma} + r(r) \tag{18}$$

$$U_{\gamma} = -\frac{r}{2(1-\gamma)}\hat{\alpha}^*(\sigma\sigma^*)^{-1}\hat{\alpha} + r(x) \quad (18)$$

Under suitable conditions the H-J-B equation (15) has a solution with sufficient regularity [1, 13]. Moreover, if the condition

$$\hat{\alpha}^*(\sigma\sigma^*)^{-1}\hat{\alpha}\to\infty, \ |x|\to\infty \tag{19}$$

is assumed, then the solution such that  $v(t,x) \rightarrow$  $-\infty$ ,  $\forall t < T$ , as $|x| \to \infty$  is unique and the identification

$$v(0, x; T) \equiv v(0, x) = \hat{v}(0, x) \equiv \inf_{h \in \mathcal{A}(T)} J^0(v, x; h; T)$$
(20)

can be verified.

The value for the problem on infinite time horizon is defined as

$$\hat{\chi}(\gamma) = \inf_{h \in \mathcal{A}} \underline{\chi}(h; \gamma) \tag{21}$$

$$\underline{\chi}(h;\gamma) = \underline{\lim}_{T \to \infty} \frac{1}{T} \log E[V_T(h)^{\gamma}] \qquad (22)$$

by suitably setting the set  $\mathcal{A}$  of admissible strategies. The corresponding  $H-J-B$  equation of ergodic type for the problem is considered

$$\begin{split} \chi(\gamma) &= \frac{1}{2} \text{tr}[\lambda \lambda^* D^2 w] + \frac{1}{2} (Dw)^* \lambda \lambda^* Dv \\ &+ \inf_h \left\{ [\beta + \gamma \lambda \sigma^* h]^* Dw + \gamma \eta(x, h) \right\}, \\ &= \frac{1}{2} \text{tr}[\lambda \lambda^* D^2 w] + \beta^*_{\gamma} Dw \\ &+ \frac{1}{2} (Dw)^* \lambda N_{\gamma}^{-1} \lambda^* Dw - U_{\gamma} \end{split} \tag{23}$$

However, even if we set as  $\mathcal{A} = \{h_{\cdot}|_{[0,T]} \in \mathcal{A}(T), \forall T\}$ identification of  $\hat{\chi}(\gamma)$  with the solution  $\chi(\gamma)$  to the  $H-J-B$  equation (23) cannot be shown in general. Indeed, even in the case of a linear Gaussian model (see below), such identification cannot be seen always to hold [5, 11, 13]. Instead, we introduce the asymptotic value

$$\tilde{\chi}(\gamma) = \lim_{T \to \infty} \frac{1}{T} v(0, x; T) \tag{24}$$

Then, a general discussion is possible for linear Gaussian models. Since the verification  $v(0, x) =$  $\hat{v}(0,x)$  holds in general for the problem on a finite time horizon, in the case of linear Gaussian models,

$$\lim_{T \to \infty} \frac{1}{T} \inf_{h \in \mathcal{A}} J^{0}(v, x; h; T) = \tilde{\chi}(\gamma) \qquad (25)$$

is verified. Assume that  $r(x) = r$ ,  $\alpha(x) = Ax +$  $a, \ \sigma(x) = \Sigma, \ \beta(x) = Bx + b, \ \lambda(x) = \Lambda, \ \text{where}$ A, B,  $\Sigma$ ,  $\Lambda$  are constant matrices, a, b are constant vectors and  $r$  is a constant. Then, the solution to equation  $(15)$  has an explicit expression as  $v(t, x) = \frac{1}{2}x^*P(t)x + q(t)^*x + k(t)$ , where  $P(t)$  is a nonpositive definite solution to the Riccati equation

$$\dot{P}(t) + P(t)\Lambda N^{-1}\Lambda^* P(t) + K_1^* P(t)$$
$$+ P(t)K_1 - C^* C = 0, \quad P(T) = 0 \quad (26)$$

and  $q(t)$ ,  $K(t)$  are respectively solutions to

$$\dot{q}(t) + (K_1 + \Lambda N^{-1} \Lambda P(t))^* q(t) + P(t)b$$
$$+ \frac{\gamma}{1 - \gamma} (A^* + P(t) \Lambda \Sigma^*)$$
$$\times (\Sigma \Sigma^*)^{-1} \hat{a} = 0, \quad q(T) = 0 \qquad (27)$$

and

$$\dot{k}(t) + \frac{1}{2} \text{tr}[\Lambda \Lambda^* P(t)] + \frac{1}{2} q(t)^* \Lambda \Lambda^* q(t)$$
$$+ \frac{\gamma}{2(1-\gamma)} (\hat{a} + \Sigma \Lambda^* q(t))^* (\Sigma \Sigma^*)^{-1}$$
$$\times (\hat{a} + \Sigma \Lambda^* q(t)) = 0 \tag{28}$$

$$k(T) = \gamma \log v_0 \tag{29}$$

where

$$K_1 := B + \frac{\gamma}{1 - \gamma} \Lambda \Sigma^* (\Sigma \Sigma^*)^{-1} A \qquad (30)$$

$$C := \sqrt{-\frac{\gamma}{1-\gamma}} \Sigma^* (\Sigma \Sigma^*)^{-1} A \tag{31}$$

$$N^{-1} := I + \frac{\gamma}{1-\gamma} \Sigma^* (\Sigma \Sigma^*)^{-1} \Sigma \tag{32}$$

If  $G := B - \Lambda \Sigma (\Sigma \Sigma^*)^{-1} A$  is stable, then  $P(t) =$  $P(t;T), q(t) = q(t;T)$  converge as  $T \to \infty$  respectively to  $\overline{P}$ ,  $\overline{q}$ , which are respectively solutions to

$$K_1^* \overline{P} + \overline{P} K_1 + \overline{P} \Lambda N^{-1} \Lambda^* \overline{P} - C^* C = 0 \quad (33)$$
$$(K_1 + \Lambda N^{-1} \Lambda^* \overline{P})^* \overline{q} + \overline{P} b$$
$$+ \frac{\gamma}{1 - \gamma} (A^* + \overline{P} \Lambda \Sigma^*) (\Sigma \Sigma^*)^{-1} \hat{a} = 0 \quad (34)$$

and  $-\dot{k}(t) = -\dot{k}(t;T)$  converges to  $\chi(\gamma)$  determined by

$$\chi(\gamma) = \frac{1}{2} \text{tr}[\Lambda \Lambda^* \overline{P}] + \frac{1}{2} \overline{q}^* \Lambda \Lambda^* \overline{q} \\
+ \frac{\gamma}{2(1-\gamma)} (\hat{a} + \Sigma \Lambda^* \overline{q})^* (\Sigma \Sigma^*)^{-1} \\
\times (\hat{a} + \Sigma \Lambda^* \overline{q}) \tag{35}$$

The nonpositive definite solutions to equations  $(33)$ and (34) are unique and  $(K_1 + \Lambda N^{-1} \Lambda^* \overline{P})$  is stable under the present assumptions. Thus  $\frac{1}{T}v(0;x;T)$ 

converges to  $\tilde{\chi}(\gamma) = \chi(\gamma)$  and  $(\chi(\gamma), w)$  defined by  $w(x) = \frac{1}{2}x^*\overline{P}x + \overline{q}^*x$  turns out to be a solution to equation  $(23)$ . If, furthermore,

$$\overline{P}\Lambda\Sigma^*(\Sigma\Sigma^*)^{-1}\Sigma\Lambda^*\overline{P} < A^*(\Sigma\Sigma^*)^{-1}A \qquad (36)$$

holds, then one can show that  $\chi(\gamma) = \hat{\chi}(\gamma)$  [11, 13]. The infimum in equation (23) is attained by  $\hat{h}(x) =$  $\frac{1}{1-\nu}(\sigma\sigma^*)^{-1}(\hat{\alpha}+\sigma\lambda^*Dw)(x)$  and in the linear Gaussian model  $\hat{h}(x) = \frac{1}{1-\nu} (\Sigma \Sigma^*)^{-1} [\hat{a} + \Sigma \Lambda^* \overline{q} + (A +$  $\Sigma \Lambda^* \overline{P} x$ . Thus, under condition (37) optimal strategy for  $\hat{\chi}(\gamma)$  is defined as  $\hat{h}_t = \hat{h}(X_t), t < \infty$ <br>[11]. Decomposing as  $\hat{h}_t = \frac{1}{1-\gamma}\hat{h}_t^1 + \frac{1}{1-\gamma}\hat{h}_t^2 := \frac{1}{1-\gamma}$ <br> $(\Sigma\Sigma^*)^{-1}[\hat{a} + AX_t] + \frac{1}{1-\gamma}(\Sigma\Sigma^*)^{-1}[\Sigma\Lambda^*\overline{q} + \Sigma\Lambda^*]$  $\overline{P}X_t$ ], Davis-Lleo [4] regard this decomposition as

a generalization of Merton's mutual funds theorem (see **Merton Problem**). Here  $\hat{h}_t^1$  is a log utility portfolio (Kelly portfolio, see below and in Kelly Problem).

When  $0 < \gamma < 1$  maximizing the criterion

$$\check{\chi}(h;\gamma) = \overline{\lim_{T \to \infty}} \frac{1}{T} \log E[V_T(h))^{\gamma}] \tag{37}$$

is considered. As a generic structure it can be seen that there exists  $\gamma^f$  such that  $\check{\chi}(\gamma) = \sup_h \check{\chi}(h;\gamma)$ diverges for  $\gamma^f < \gamma < 1$ . However, it is only in onedimensional linear Gaussian models that one can find the infimum of such  $\gamma^f$  explicitly [6].

The problems under bench-marked setting can be considered similarly ( $cf$  [2, 4]).

Noting that

$$\frac{1}{T} \log V_T(h) = \frac{-1}{2T} \int_0^T \left\{ h_t - \rho^{-1} \hat{\alpha}(X_t) \right\}^* \times \rho \left\{ h_t - \rho^{-1} \hat{\alpha}(X_t) \right\} dt \n+ \frac{1}{2T} \int_0^T \left\{ r(X_t) + \hat{\alpha}^* \rho^{-1} \hat{\alpha}(X_t) \right\} dt \n+ \frac{1}{T} \int_0^T h_t^* \sigma(X_t) dW_t \tag{38}$$

where  $\rho = \sigma \sigma^*, h_t^K := (\sigma \sigma^*)^{-1} \hat{\alpha}(X_t)$  turns out to maximize pathwise the growth rate of  $V_T(h)$  on the long run and it is called Kelly portfolio (logutility portfolio) [10] or numéraire portfolio. This is a control problem at the level of the law of large numbers.

The problem of maximizing the criterion

$$\overline{J}(\kappa, h) = \overline{\lim_{T \to \infty}} \frac{1}{T} \log P(\log V_T(h) \ge \kappa T) \quad (39)$$

is a kind of large deviation control problem and it is considered as the dual to risk-sensitive asset management in the risk-seeking case  $0 < \nu < 1$  [7, 9, 17, 18, 20]. On the other hand, the problem of minimizing the criterion

$$\underline{J}(\kappa, h) = \underline{\lim}_{T \to \infty} \frac{1}{T} \log P(\log V_T(h) \leq \kappa T) \quad (40)$$

is also a kind of large deviation control problem and it is considered as the dual to risk-sensitive asset management in the risk-averse case  $\gamma < 0$  [3, 8, 15, 20]. Studies of these problems are still in progress.

Choosing as admissible strategies the set of all  $\mathcal{G}^S_t := \sigma(S(u), \ u \leq t)$  progressively measurable processes satisfying some integrability conditions, the problems under partial information are considered as well [7, 12, 14-16, 19].

## References

- Bensoussan, A., Frehse, J. & Nagai, H. (1998). Some [1] results on risk-sensitive control with full information, Applied Mathematics and Optimization 37, 1–41.
- [2] Browne, S. (1999). Beating a moving target : optimal portfolio strategies for outperforming a stochastic benchmark, Finance and Stochastics 3, 275-294.
- [3] Browne, S. (1999). The risk and rewards of minimizing shortfall probability, Journal of Portfolio Management 25(4), 76–85.
- Davis, M. & Lleo, S. (2008). Risk-sensitive bench-[4] marked asset management, Quantitative Finance 8,  $415 - 426.$
- Fleming, W.H. & Sheu, S.J. (1999). Optimal long term [5] growth rate of expected utility of wealth, Annals of Applied Probability 9(3), 871-903.
- Fleming, W.H. & Sheu, S.J. (2002). Risk-sensitive [6] control and an optimal investment model. II, Annals of Appliede Probability 12(2), 730-767.
- Hata, H. & Iida, Y. (2006). A risk-sensitive stochastic [7] control approach to an optimal investment problem with partial information, Finance and Stochastics 10, 395-426.
- Hata, H., Nagai, H. & Sheu, S.J. Asymptotics of the [8] probability minimizing a "down-side" risk, to appear in Annals of Applied Probability.
- Hata, H. & Sekine, J. (2005). Solving long term optimal [9] investment problems with Cox-Ingersoll-Ross interest rates, Advances in Mathematical Economics 8, 231-255.

- [10] Kelly, J. (1956). A new interpretation of information rate, Bell System Technical Journal 35, 917-926.
- $[11]$ Kuroda, K. & Nagai, H. (2002). Risk sensitive portfolio optimization infinite time horizon, Stochastics and Stochastics Reports 73, 309-331.
- Nagai, H. (1999). Risk-sensitive dynamic asset manage-[12] ment with partial information, in Stochastics in Finite and Infinite Dimensions, a volume in honor of G. Kallianpur, J. Xiong ed, Birkhäuser, pp. 321-340.
- [13] Nagai, H. (2003). Optimal strategies for risk-sensitive portfolio optimization problems for general factor models, SIAM Journal of Control and Optimization 41, 1779-1800.
- [14] Nagai, H. (2004). Risk-sensitive portfolio optimization with full and partial information, Stochastic Analysis and Related Topics, Advanced Studies in Pure Mathematics 41, 257-278.
- [15] Nagai, H. Asymptotics of the probability minimizing a "down-side" risk under partial information, Preprint.
- Nagai, H. & Peng, S. (2002). Risk-sensitive dynamic [16] portfolio optimization with partial informationon infinite time horizon, Annals of Applied Probability 12(1), 173-195.
- [17] Pham, H. (2003). A large deviations approach to optimal long term investment, Finance and Stochastics 7,  $169 - 195$
- [18] Pham, H. (2003). A risk-sensitive control dual approach to a large deviations control problem, Systems and Control Letters 49, 295-309.
- [19] Rishel, R. (1999). Optimal portfolio management with partial observation and power utility function, Stochastic Analysis, Control, Optimization and Applications, a volume in honor of W.H. Fleming. 605-620.
- [20] Stutzer, M. (2003). Portfolio choice with endogeneous utility: a large deviations approach, Journal of Econometrics 116, 365-386.

## **Further Reading**

- Bielecki, T.R. & Pliska, S.R. (1999). Risk sensitive dynamic asset management, Applied Mathematics and Optimization 39. 337-360.
- Merton, R.C. (1990). Continuous Time Finance, Blackwell, Malden.

## **Related Articles**

**Expected Utility Maximization: Duality Methods;** Expected Utility Maximization; Kelly Problem; Merton Problem; Stochastic Control.

HIDEO NAGAI
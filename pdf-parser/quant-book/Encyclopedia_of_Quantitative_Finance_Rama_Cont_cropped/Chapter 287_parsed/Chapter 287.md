# **Stochastic Control**

The theory of stochastic optimal control concerns the control of a dynamical system in the presence of random noises so as to optimize a certain performance criterion. The early development of stochastic optimal control theory began in the period between the late 1950s and early 1960s. The earlier stage of the development focused on the quadratic performance criterion. Around the same period, the classic work of Bellman [1] first introduced one of the main approaches in stochastic optimal control theory, namely, the dynamic programming principle. The dynamic programming approach plays a significant role in modern finance, in particular, continuous-time finance. The key idea of the dynamic programming principle is to consider a family of stochastic optimal control problems with different starting times and states and to relate the problems through the Hamilton–Jacobi–Bellman (HJB) equation. An HJB equation is a nonlinear second-order partial differential equation (*see* **Partial Differential Equations**) that describes the local behavior of the performance criterion evaluated at the optimal control. For detailed discussion of the dynamic programming approach, we refer to [11, 12, 21].

Together with the HJB approach, the stochastic maximum principle provides the second main approach to stochastic control. The key idea of the stochastic maximum principle is to derive a set of necessary conditions satisfied by any optimal control. The stochastic maximum principle basically states that any optimal control must satisfy forward–backward stochastic differential equations (SDEs), called the *optimality system*, and a maximum condition of a functional, called the *Hamiltonian*. The novelty of the stochastic maximum principle is to make the stochastic optimal control problem, which is infinite dimensional, more tractable. It leads to explicit solutions for the optimal controls in some cases. References [2] and [21] provided excellent discussions on the stochastic maximum principle.

Merton [16, 17] pioneered the study of an optimal consumption–investment problem in a continuoustime economy. He first explored the state of the art of the stochastic optimal control theory to develop an elegant (closed-form) solution to the problem (*see* **Merton Problem**). The stochastic control approach adopted by Merton uses the HJB equation. Another approach is the martingale approach, which uses the martingale method for risk-neutral valuation of options to provide an elegant solution to the optimal consumption–investment problem. The martingale approach was pioneered by the important contributions of Cox and Huang [4] and Karatzas *et al.* [13]. It was then extended by a number of authors, (see, e.g., [14]).

Each of the three main approaches in stochastic optimal control has its own merits. For example, dynamic programming works well in the case when (i) the state processes and optimal controls are Markov (*see* **Markov Processes**), (ii) the state processes have deterministic coefficients, and (iii) state constraints are absent. The stochastic maximum principle can deal with the situations when the state processes have random coefficients and state constraints are present. The martingale approach is applicable when one considers a general state process, for example, when the state process is not Markov. It works well when the market is complete though there are some works that consider the case when the market is incomplete (see [14]). The martingale approach is suitable for the situations when there are nonnegative constraints on consumption and wealth. It is difficult to say which one is uniformly better or more general than the other two. However, the three approaches are related to each other in some way. For example, the relationship between the dynamic programming approach and the stochastic maximum principle can be established by relating the solutions of the forward–backward SDEs associated with the stochastic maximum principle to those of the HJB equation from the dynamic programming ([21], Chapter 5). The relationship between the martingale approach and the stochastic maximum principle stems from two facts. Firstly, the solutions of the adjoint equations can be related to the density process for the change of measures in the martingale approach. Secondly, the first-order condition of the constrained maximization problem in the martingale approach is related to that of the first-order condition of the Hamiltonian in the stochastic maximum principle [3]. It is interesting to note that the three approaches end up with the same result of the optimal consumption–investment problem in some cases.

We discuss three methods, namely, the martingale method, the HJB Method, and the stochastic maximum principle to solve the optimal consumption–investment problem. Here, we focus on the case of a power utility function. For general cases, refer to  $[10, 14]$ .

#### The Martingale Approach

The development here is based on the contributions of Karaztazs, Lehoczky, Sethi, Shreve, and Xu [13]. Here, we just present some main results and highlight some key steps. For a more comprehensive discussion, we refer to [10; Chapter 10].

We consider a popular model for a financial market consisting of one risk-free asset and  $n$  risky assets. These assets are tradable over a finite time horizon  $[0, T^*]$ , where  $T^* < \infty$ . Fix a complete probability space  $(\Omega, \mathcal{F}, \mathcal{P})$ , where  $\mathcal{P}$  is a real-world probability measure.

The dynamics of the risk-free asset or bond,  $B$ , and the risky assets  $S_1, S_2, \ldots, S_n$ , under  $\mathcal{P}$ , are governed by

$$dB(t) = r(t)B(t) dt$$
,  $B(0) = 1$  (1)

$$\mathrm{d}S_i(t) = S_i(t) \left( \mu_i(t) \,\mathrm{d}t + \sum_{j=1}^n \sigma_{ij}(t) \,\mathrm{d}W_j(t) \right) \tag{2}$$

$$S_i(0) = s_i$$
,  $i = 1, 2, ..., n$  (3)

Here  $W(t) := (W_1(t), W_2(t), \ldots, W_n(t))^T$  is an  $n$ -dimensional Brownian motion defined on  $(\Omega, \mathcal{F}, \mathcal{P})$ , where  $y^T$  is the transpose of a vector y. Write  $\{\mathcal{F}(t)\}\$  for the right-continuous and complete filtration generated by  $\{W(t)\}\$ . For a treatment of SDEs, see [8].

The market interest rate  $r(t)$ , the vector of appreciation rates  $\mu(t) := (\mu_1(t), \mu_2(t), \dots, \mu_n(t))^T$ , and the volatility matrix  $\sigma(t) := [\sigma_{ij}(t)]_{i,j=1,2,...,n}$  of the risky assets are supposed to be measurable,  $\{\mathcal{F}(t)\}$ adapted, and bounded processes. The market is complete.

Let  $a(t) := \sigma(t)\sigma^{T}(t)$ . Suppose there is an  $\epsilon > 0$ such that

$$\xi^T a(t)\xi \ge \epsilon |\xi|^2, \quad \forall \xi \in \mathbb{R}^n, \quad (t, \omega) \in [0, T^*] \times \Omega,$$

where  $|\cdot|$  denotes the Euclidean norm in  $\mathbb{R}^n$ .

Then, the inverses of  $\sigma$  and  $\sigma^T$  exist and are bounded, and the market is complete. The filtration  $\{\mathcal{F}(t)\}\$ is equivalent to the  $\mathcal{P}$ -completion of the filtration generated by the price process  $\{S(t)\}.$ 

We define the market price of risk by

$$\theta(t) := \sigma^{-1}(t)(\mu(t) - r(t)\mathbf{1})\tag{4}$$

where  $\mathbf{1} := (1, 1, \dots, 1)^T \in \mathbb{R}^n$ ;  $\theta$  is bounded and  $\{\mathcal{F}(t)\}$ -progressively measurable.

Now, we introduce an exponential process:

$$\Lambda(t) := \exp\left(-\int_0^t \theta^T(s) \, \mathrm{d}W(s) - \frac{1}{2} \int_0^t |\theta^T(s)|^2 \mathrm{d}s\right) \tag{5}$$

Define a new probability measure  $\mathcal{P}^{\theta} \sim \mathcal{P}$  on  $\mathcal{F}(T^*)$ by setting

$$\frac{\mathrm{d}\mathcal{P}^{\theta}}{\mathrm{d}P} := \Lambda(T^*) \tag{6}$$

By Girsanov's theorem,

$$W^{\theta}(t) := W(t) + \int_0^t \theta(s) \, \mathrm{d}s \tag{7}$$

is an  $n$ -dimensional standard Brownian motion under  $\mathcal{P}^{\theta}$ .

Also, under  $\mathcal{P}^{\theta}$ ,

$$\mathrm{d}S_i(t) = S_i(t) \left( r(t) \,\mathrm{d}t + \sum_{j=1}^n \sigma_{ij}(t) \,\mathrm{d}W_j^{\theta}(t) \right) \tag{8}$$

Here  $\mathcal{P}^{\theta}$  is called the *risk-neutral* or *equivalent martingale measure.* 

Consider a power utility as below:

$$U(c) = \frac{c^{\gamma}}{\gamma} \ , \quad 0 < \gamma < 1 \tag{9}$$

where  $\gamma$  represents the risk-aversion parameter. The relative degree of risk aversion is  $1 - \gamma$ , which indicates how risk averse the investor is. The higher  $1 - \gamma$  is, the more risk averse the investor is.

Let  $U'$  denote the first derivative of  $U(c)$  with respect to c. Write  $I(\cdot)$  for the inverse of  $U'(\cdot)$ . Then, for any  $y \in (0, \infty)$ ,

$$I(y) = y^{1/(\gamma - 1)} \tag{10}$$

Consider a measurable  $\mathbb{R}^n$ -valued,  $\{\mathcal{F}(t)\}$ -adapted process  $\pi := (\pi_1, \pi_2, \dots, \pi_n)^T$  and a consumption

process  $\{c(t)\}\$ as a nonnegative, measurable,  $\{\mathcal{F}(t)\}\$ adapted process such that

$$\int_0^{T^*} (c(t) + |\pi(t)|^2) dt < \infty, \quad \mathcal{P} \text{ a.s.} \quad (11)$$

Here  $\pi_i(t)S_i(t)$  represents the amount invested in the *i*th risky asset, for  $i = 1, 2, \ldots, n$ . So,  $\pi$  is called a portfolio process or a trading strategy. Note that the adapted condition of  $(\pi, c)$  implies that the investor cannot anticipate the future. One financial implication is that "insider trading" is not allowed.

We assume that  $\pi$  is self-financing. A trading strategy is said to be self-financing if the changes in the value of the wealth result entirely from net gains or losses from the investments in the risk-free asset and the risky assets. In other words, there is no net inflow or outflow of funds. Let  $\{V(t)\}$  denote the wealth process of the investor, where  $V(t) := \sum_{i=1}^{n} \pi_i(t) S_i(t) + \left(1 - \sum_{i=1}^{n} \pi_i(t)\right) B(t) - \int_0^t c(s) \, ds.$  Then, under  $\mathcal{P}$ , the evolution of  $\{V(t)\}\$ is governed by

$$dV(t) = \sum_{i=1}^{n} \pi_i(t) dS_i(t) + \left(1 - \sum_{i=1}^{n} \pi_i(t)\right) dB(t) - c(t) dt \qquad (12)$$

Let  $\beta(t) := B^{-1}(t) = \exp\left(-\int_0^t r(u) \, \mathrm{d}u\right)$ . Then, under  $\mathcal{P}^{\theta}$ , the evolution of the discounted wealth process  $\{\beta(t)V(t)\}\$ is governed by

$$\beta(t)V(t) = v - \int_0^t \beta(s)c(s) \, \mathrm{d}s$$
$$+ \int_0^t \beta(s)\pi^T(s)\sigma(s) \, \mathrm{d}W^\theta(t) \quad (13)$$

where  $v = V(0)$  represents the initial wealth of the investor

Let  $\mathcal{A}(v)$  denote the class of control processes  $(\pi, c)$ , for the initial wealth v, with wealth process satisfying equation  $(13)$  and that the wealth process  $\{V(t)\}\$ is nonnegative at all times in  $[0, T^*]$ .

It can be shown that for any  $(\pi, c) \in \mathcal{A}(v)$ ,

$$E^{\theta} \left[ \int_0^{T^*} \beta(t) c(t) \, \mathrm{d}t \right] \le v \tag{14}$$

The utility maximization problem is to select  $(\pi, c) \in \mathcal{A}(v)$  so as to maximize the expected discounted utility see Expected Utility Maximization, **Expected Utility Maximization: Duality Methods** from consumption over  $[0, T^*]$ :

$$J(v,\pi,c) := E\left[\int_0^{T^*} \frac{(c(t))^{\gamma}}{\gamma} dt\right] \qquad (15)$$

Note that the utility only depends on the consumption level. So, in order to maximize the utility from consumption, we should increase the consumption level up to a certain bound. In other words, we only consider the consumption processes  $c$  such that  $E^{\theta} \left[ \int_{0}^{T^*} \beta(t) c(t) dt \right] = v$ . The utility maximization problem is to solve the following maximization problem:

$$J(v, \hat{\pi}, \hat{c}) = \sup_{(\pi, c) \in \mathcal{A}(v)} J(v, \pi, c) \tag{16}$$

subject to the budget constraint

$$E\left[\int_{0}^{T^{*}} \Lambda(t)\beta(t)c(t) dt\right] = v \qquad (17)$$

To solve the problem, we need to find the optimal portfolio process  $\hat{\pi}$ , the optimal consumption process  $\hat{c}$ , and the value function defined by  $\Phi(v) :=$  $J(v, \hat{\pi}, \hat{c}).$ 

Let  $\lambda$  denote the Lagrange multiplier of the constrained maximization problem (3). Then, the first-order conditions of the maximization problem imply that the optimal consumption rate  $c^*(t)$  satisfy

$$c^*(t) = (\lambda \Lambda(t)\beta(t))^{1/(\gamma - 1)}$$
(18)

$$E\left[\int_{0}^{T^{*}} \Lambda(t)\beta(t)c^{*}(t) dt\right] = v \qquad (19)$$

So, the optimal consumption process is

$$c^*(t) = (\lambda \Lambda(t)\beta(t))^{1/(\gamma - 1)}, \quad \forall t \in [0, T^*] \quad (20)$$

with the Lagrange multiplier  $\lambda$  determined by

$$\lambda = \left(\frac{v}{E\left[\int_0^{T^*} \left(\Lambda(t)\beta(t)\right)^{\gamma/(\gamma-1)} \mathrm{d}t\right]}\right)^{\gamma-1} \tag{21}$$

Since the market is complete, the optimal wealth process  $\{V^*(t)\}\$ is given by

$$V^*(t) = E^{\theta} \left[ \int_0^{T^*} c^*(s) \beta(s) \, \mathrm{d}s |\mathcal{F}(t) \right]$$
  
= 
$$\frac{1}{\Lambda(t)} E \left[ \int_0^{T^*} \Lambda(s) c^*(s) \beta(s) \, \mathrm{d}s |\mathcal{F}(t) \right]$$
(22)

## The HJB Method

In this section, we illustrate the use of the dynamic programming approach, also called the *HJB* method, to solve the optimal consumption-investment problem described in the section The Martingale Approach. We consider the asset price dynamics in the section The Martingale Approach with timedependent coefficients replaced by constant coefficients. We impose the same assumptions and notation for control policies, utility function, and probability measures as those in the section The Martingale Approach, unless otherwise stated.

We consider the same problem as that in the last section on the interval  $[t, T^*]$  instead of  $[0, T^*]$ . For any  $t \in [0, T^*]$ , we consider admissible policies  $(\pi, c) \in \mathcal{A}(t, v)$  for which the wealth process  $\{V(t)\}\$ satisfies

$$e^{-ru}V(u)$$
  
=  $ve^{-rt} - \int_{t}^{u} e^{-rs}c(s) ds$   
+  $\int_{t}^{u} e^{-rs}\pi^{T}(s)\sigma dW^{\theta}(s) \qquad \forall u \in [t, T^{*}]$  (23)

Here we require that the wealth process  $\{V(t)\}\$ is nonnegative at all times in  $[0, T^*]$ .

The value function, which is an indirect utility see **Expected Utility Maximization, Expected Utility** Maximization: Duality Methods function, is defined by

$$\Phi(t,v) := \sup_{(\pi,c)\in\mathcal{A}(t,v)} E\left[\int_t^{T^*} \frac{(c(s))^\gamma}{\gamma} \, \mathrm{d}s|\mathcal{F}(t)\right] \tag{24}$$

Let  $\Phi_t$ ,  $\Phi_v$ , and  $\Phi_{vv}$  denote the derivative of  $\Phi$  with respect to *t*, the first and second derivatives of  $\Phi$  with respect to  $v$  respectively. Then, the value function satisfies the following HJB equation:

$$0 = \Phi_t + \sup_{\pi \in \mathbb{R}^n, c \in [0, \infty)} \left[ \frac{1}{2} |\pi^T \sigma|^2 \Phi_{vv} + [(rv - c) + \pi^T (\mu - r\mathbf{1})] \Phi_v + \frac{c^{\gamma}}{\gamma} \right]$$
(25)

with the boundary and terminal conditions

$$\Phi(t,0+) = 0, \quad \forall t \in [0,T^*] \tag{26}$$

$$\Phi(T^*, v) = 0, \quad \forall v \in (0, \infty) \tag{27}$$

With the power utility, the solution of the HJB equation is

$$\Phi(t,v) = \frac{(g(t))^{1-\gamma}}{\gamma} v^{\gamma} \tag{28}$$

where

$$g(t) = \frac{1}{K} (1 - e^{-K(T-t)})$$
 (29)

with

$$K = -\frac{\gamma}{1-\gamma} \left(r + \frac{|\theta|^2}{2(1-\gamma)}\right) \tag{30}$$

$$\theta = \sigma^{-1}(\mu - r\mathbf{1})\tag{31}$$

In this case, the optimal consumption and portfolio processes are, respectively, given by

$$c^*(t,v) = \frac{v}{g(t)}\tag{32}$$

and

$$\pi^*(t,v) = (\sigma^T)^{-1} \left(\frac{v}{1-\gamma}\right) \theta \tag{33}$$

The HJB method for the optimal consumption-investment problem is discussed in different monographs, such as [6, 15, 18, 19], and others. These monographs focus on discussing the verification theorem for the HJB solution to the problem. Loosely speaking, if a bounded, continuous, and smooth enough function satisfies the HJB equation with associated boundary conditions, the function is identical to the value function. The verification theorem also provides a sufficient condition for an optimal control. For detailed discussion on the verification theorem, we refer to [18] for the diffusion case and [19] for the jump-diffusion case.

One fundamental result behind the HJB method is called the *principle of optimality*. Informally speaking, the principle of optimality states that if you do not know the optimal expected reward at the current time  $t$ , but have knowledge of how well you can achieve at some later time, say  $t + h$ , you can evaluate the expected reward associated with the policy of adopting the control u during  $(t, t + h)$ , acting optimally from  $t + h$  onward and minimizing over the set of controls. Indeed, the HJB equation for a stochastic control problem follows "in principle" from the principle of optimality for dynamic programming. By the principle of optimality and Itô's differentiation rule, it can be shown that the value function of a stochastic optimal control problem satisfies the HJB equation if the value function satisfies certain differentiability or smoothness conditions see Monotone Schemes. However, the principle of optimality and its derivation are often overlooked in some recent literature on the stochastic optimal control theory and its financial applications, but they are certainly important. Some fundamental contributions to these aspects were due to Davis and Varaiya [5] and Elliott [7], (see also [8]). In these works, the martingale method was used to deduce the principle of optimality.

### The Stochastic Maximum Principle

Firstly, we suppose that the state  $X(t) := X^{(u)}(t)$  of a controlled diffusion in  $\mathbb{R}^n$  is

$$dX(t) = b(t, X(t), u(t)) dt$$
  
+  $\sigma(t, X(t), u(t)) dW(t)$  (34)

where the coefficients b and  $\sigma$  satisfy some regularity conditions.

Here, the control  $u$  enters both the drift coefficient b and the diffusion coefficient  $\sigma$ . We assume that (i) the control  $u(t) := u(t, \omega)$  takes value in  $U \subset \mathbb{R}^k$ , for some positive integer k; (ii) u is  $\{\mathcal{F}(t)\}$ -progressively measurable and right continuous with left-hand limit (RCLL); and (iii) the controlled diffusion has a unique solution  $\{X^{(u)}(t)\}\$ . These controls are called

*admissible* and we write  $\mathcal{U}$  for the set of admissible controls.

We consider the same performance criterion as the one in the principle of optimality in the section The HJB Method and impose the same set of assumptions for the performance criterion as those in that section.

Let  $H: [0, T^*] \times \mathbb{R}^n \times U \times \mathbb{R}^n \times \mathcal{L}(\mathbb{R}^n, \mathbb{R}^n) \to$  $\Re$  denote the Hamiltonian given by

$$H(t, X, u, p, q)$$
  
:=  $g(t, X, u) + b^{T}(t, X, u)p + tr(\sigma^{T}(t, X, u)q)$   
(35)

where  $tr(M)$  represents the trace of a square matrix  $M$ ; we suppose that  $H$  is differentiable in  $X$ .

The adjoint equation corresponding to  $u$  and  $X^{(u)}$ for the unknown processes  $\{p(t)\}\$  and  $\{q(t)\}\$  is given by the following backward stochastic differential equation:

$$\begin{aligned} \mathrm{d}p(t) &= -\nabla H(t, X(t), u(t), p(t), q^T(t)) \,\mathrm{d}t \\ &+ q^T(t) \,\mathrm{d}W(t) \end{aligned} \tag{36}$$

$$p(T^*) = \nabla h(X(T^*)) \tag{37}$$

where  $\nabla G$  is the gradient of a function G with respect to  $X$ .  $h$  is a concave function of  $X$ .

Then, we present a sufficient maximum principle in the following proposition.

**Proposition 1** Let  $u^* \in \mathcal{U}$  and the corresponding controlled state process be  $X^* := X^{(u^*)}$ . Suppose there exists a solution  $(p^*(t), q^*(t))$  of the corresponding adjoint equation,  $(36)$  and  $(37)$  satisfying

$$E\left[\int_0^{T^*} q^*(t)(q^*(t))^T \mathrm{d}t\right] < \infty \tag{38}$$

Suppose, further, that

1. *for each*  $t \in [0, T^*]$ ,

$$H(t, X^*(t), u^*(t), p^*(t), q^*(t))$$
  
= 
$$\sup_{u \in U} H(t, X^*(t), u, p^*(t), q^*(t)) \quad (39)$$

2.  $h(X)$  is a concave function of  $X$ ,

*3. for each*  $t \in [0, T^*]$ *,* 

$$H^*(X) := \max_{u \in U} H(t, X, u, p^*(t), q^*(t)) \quad (40)$$

exists and is a concave function of  $X$ . Then,  $u^*$  is an optimal control.

For the necessary condition of the stochastic maximum principle, we refer to  $[2, 3, 7-9, 20]$ .

Now, we illustrate the application of the stochastic maximum principle to the optimal consumption-investment problem presented. Here, we just present some heuristic arguments. For detailed discussions and proofs, we refer to The Martingale Approach [3]. We assume the same asset price dynamics and adopt the same notation as those in the section. As in that section, the market is complete here, so the market price of risk is uniquely determined. We consider the following utility maximization problem for both consumption and terminal wealth:

$$J_1(v) := \sup_{(\pi,c)\in\mathcal{A}(v)} E\left[\int_0^{T^*} \frac{(c(t))^{\gamma_1}}{\gamma_1} \mathrm{d}t + \frac{(V(T^*))^{\gamma_2}}{\gamma_2}\right] \tag{41}$$

In this case, the Hamiltonian is

$$H(t, V, (\pi, c), p, q)$$

$$= \frac{c^{\gamma_1}}{\gamma_1} + p \left[ r(t)V - c + \pi^T (\mu(t) - r(t)\mathbf{1}) \right]$$

$$+ q^T \sigma^T (t)\pi \tag{42}$$

and the adjoint equation has the following form:

$$dp(t) = -r(t)p(t) dt + qT(t) dW(t) \quad (43)$$

$$p(T) = (V^*(T))^{\gamma_2 - 1} \tag{44}$$

Define an exponential process  $\{Z_{\bar{\theta}}(t)\}$  by

$$Z_{\bar{\theta}}(t) := \exp\left(-\int_0^t \bar{\theta}^T(s) \, \mathrm{d}W(s) - \frac{1}{2} \int_0^t |\bar{\theta}(s)|^2 \mathrm{d}s\right) \tag{45}$$

where  $\{\bar{\theta}(t)\}\$  is a measurable,  $\{\mathcal{F}(t)\}\$ -adapted process, which is uniformly bounded in  $(t, \omega) \in [0, T^*] \times$ Ω. Write  $\xi_{\bar{\theta}}(t) := \beta(t) Z_{\bar{\theta}}(t)$ , for each  $t \in [0, T^*]$ .

It can be shown that an adapted solution to the adjoint equation  $(42)$  and  $(43)$  is given by the processes

$$p(t) = p(0)\xi_{\bar{\theta}}(t), \quad q(t) = -p(0)\xi_{\bar{\theta}}(t)\theta(t) \quad (46)$$

From the first-order conditions of maximizing the Hamiltonian  $(5)$ , one obtains

$$c^*(t) = (p(0)\xi_{\bar{\theta}}(t))^{1/(\gamma_1 - 1)}$$
(47)

$$\bar{\theta}(t) = \sigma^{-1}(\mu(t) - r(t)\mathbf{1}) = \theta(t) \qquad (48)$$

To simplify the notation, write  $\xi(t) := \xi_{\bar{\theta}}(t)$ , for each  $t \in [0, T^*]$ . Define a function  $\mathcal{X} : (0, \infty) \to$  $(0, \infty)$  by

$$\mathcal{X}(y)$$

$$:=E\left[\int_{0}^{T^{*}}\xi(s)(y\xi(s))^{\frac{1}{\gamma_{1}-1}}\mathrm{d}s+\xi(T^{*})(y\xi(T^{*}))^{\frac{1}{\gamma_{2}-1}}\right]$$
(49)

Since  $\mathcal{X}$  is strictly decreasing and surjective, its inverse  $\mathcal{Y} := \mathcal{X}^{-1} : (0, \infty) \to (0, \infty)$  exists and is strictly decreasing. We then conjecture that the optimal controls  $(\pi^*, c^*)$  satisfy

$$E\left[\int_0^{T^*} \xi(s)c^*(s) \, \mathrm{d}s + \xi(T^*)V^*(T^*)\right] = v \tag{50}$$

Under this conjecture,  $p(0) = \mathcal{Y}(v)$ .

By the martingale representation theorem, there exists a progressively measurable process  $\eta$ :  $[0, T^*] \times \Omega \to \mathbb{R}^n \text{ with } \int_0^{T^*} |\eta(s)|^2 \mathrm{d}s < \infty, \ \mathcal{P} \text{ a.s.}$ such that

$$E\left[\int_{0}^{T^{*}} \xi(s)(\mathcal{Y}(v)\xi(s))^{\frac{1}{\gamma_{1}-1}} \mathrm{d}s$$
  
+ 
$$\xi(T^{*})(\mathcal{Y}(v)\xi(T^{*}))^{\frac{1}{\gamma_{2}-1}} |\mathcal{F}(t)\right]$$
  
= 
$$v + \int_{0}^{t} \eta^{T}(s) \, \mathrm{d}W(s) \tag{51}$$

Then, it can be shown that

$$\pi^*(t) = \sigma^{-1}(t) \left[ \frac{\eta(t)}{\xi(t)} + V^*(t)\theta(t) \right] \qquad (52)$$

$$c^*(t) = (\mathcal{Y}(v)\xi(t))^{\frac{1}{\gamma_1 - 1}}$$
(53)

where the optimal wealth process {*V* <sup>∗</sup>*(t)*} is given by

$$V^*(t) = \frac{1}{\xi(t)} E\left[\int_t^{T^*} \xi(s) (\mathcal{Y}(v)\xi(s))^{\frac{1}{\gamma_1 - 1}} ds + \xi(T^*)(\mathcal{Y}(v)\xi(T^*))^{\frac{1}{\gamma_2 - 1}} |\mathcal{F}(t)\right]$$
(54)

## **References**

- [1] Bellman, R.S. (1957). *Dynamic Programming*, Princeton University Press, Princeton.
- [2] Bensoussan, A. (1981). *Lectures on Stochastic Control*, Lecture Notes in Mathematics, 972, Springer-Verlag, Berlin, pp. 1–62.
- [3] Cadenillas, A. & Karatzas, I. (1995). The stochastic maximum principle for linear, convex optimal control with random coefficients, *SIAM Journal of Control and Optimization* **33**(2), 590–624.
- [4] Cox, J.C. & Huang, C.-F. (1989). Optimal consumption and portfolio policies when asset prices follow a diffusion process, *Journal of Economic Theory* **49**, 33–83.
- [5] Davis, M.H.A. & Varaiya, P.P. (1973). Dynamic programming conditions for partially observable stochastic systems, *SIAM Journal on Control and Optimization* **11**, 226–261.
- [6] Duffie, D. (1996). *Dynamic Asset Pricing Theory*, 2nd Edition, Princeton University Press, Princeton.
- [7] Elliott, R.J. (1977). The optimal control of a stochastic system, *SIAM Journal on Control and Optimization* **15**(5), 756–778.
- [8] Elliott, R.J. (1982). *Stochastic Calculus and Applications*, Springer, Berlin, Heidelberg, New York.
- [9] Elliott, R.J. & Kohlmann, M. (1994). The second order minimum principle and adjoint process, *Stochastics and Stochastics Reports* **46**, 25–39.
- [10] Elliott, R.J. & Kopp, P.E. (2005). *Mathematics of Financial Markets*, Springer, Berlin, Heidelberg, New York.

- [11] Fleming, W.H. & Rishel, R.W. (1975). *Deterministic and Stochastic Optimal Control*, Springer, Berlin, Heidelberg, New York.
- [12] Fleming, W.H. & Soner, H.M. (1993). *Controlled Markov Processes and Viscosity Solutions*, Springer, Berlin, Heidelberg, New York.
- [13] Karatzas, I., Lehoczky, J.P. & Shreve, S.E. (1987). Optimal portfolio and consumption decisions for a "small investor" on a finite horizon, *SIAM Journal of Control and Optimization* **25**, 1557–1586.
- [14] Karatzas, I. & Shreve, S.E. (1998). *Methods of Mathematical Finance*, Springer, Berlin, Heidelberg, New York.
- [15] Korn, R. (1997). *Optimal Portfolios: Stochastic Models for Optimal Investment and Risk Management in Continuous Time*, World Scientific, Singapore.
- [16] Merton, R.C. (1969). Lifetime portfolio selection under uncertainty: the continuous-time model, *Review of Economics and Statistics* **51**, 247–257.
- [17] Merton, R.C. (1971). Optimal consumption and portfolio rules in a continuous time model, *Journal of Economic Theory* **3**, 373–413.
- [18] Øksendal, B. (2003). *Stochastic Differential Equations: An Introduction with Applications*, 6th Edition, Springer, Berlin, Heidelberg, New York.
- [19] Øksendal, B. & Sulem, A. (2004). *Applied Stochastic Control of Jump Diffusions*, Springer, Berlin, Heidelberg, New York.
- [20] Peng, S. (1990). A general stochastic maximum principle for optimal control problems, *SIAM Journal of Control and Optimization* **28**, 966–979.
- [21] Yong, J. & Zhou, X.Y. (1999). *Stochastic Control*, Springer, Berlin, Heidelberg, New York.

## **Related Articles**

**Expected Utility Maximization**; **Expected Utility Maximization: Duality Methods**; **Markov Processes**; **Merton Problem**; **Monotone Schemes**; **Partial Differential Equations**.

ROBERT J. ELLIOTT & TAK KUEN SIU
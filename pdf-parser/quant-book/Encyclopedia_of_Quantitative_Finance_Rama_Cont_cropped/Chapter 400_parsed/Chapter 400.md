# **Stochastic Control in** Insurance

# **Classification of Models**

The stochastic control problem in insurance can be classified according to the type of models used to describe the *surplus* or the *risk* process (see Insurance Risk Models), the particular controls that are allowed, and the nature of the objective function.

## Modeling of the Surplus

In the classical Cramér-Lundberg model, the risk process is modeled by a compound Poisson process

$$R(t) = R(0) + pt - \sum_{0}^{A(t)} U_i \tag{1}$$

where  $A(t)$  is the Poisson process of the incoming claims, whose intensity  $\beta$  without loss of generality can be set to 1, the i.i.d. sequence  $U_i$  represents the sizes of the successive claims and  $p$  is the premium rate with  $p = (1 + \eta)EU$ , with  $\eta$  being the *relative* safety loading. If one considers a sequence of such models with  $R^n(0) = xn^{1/2}$  and  $\eta^n = \mu n^{-1/2}$ , then  $R^n(nt)n^{-1/2}$  converges weakly to a Brownian motion with drift  $\mu$  and diffusion coefficient  $\sigma = [EU^2]^{1/2}$ .

# Reinsurance

The risk control in either of such models is done by way of reinsurance (see Reinsurance). This is a contract that the *cedent* (the original insurance company) makes with the reinsurance company so that the reinsurance company pays a part or all of each of the incoming claims in exchange for the portion of the premiums coming to the cedent. The cedent makes a decision on the *retention level*  $a$ , and the size of each claim is reduced from  $U_i$  to  $U_i^a$ , while the premium rate is simultaneously reduced from p to  $p^a$ ; the precise meaning of this is different for different types of the reinsurances involved. The following are the most common types of reinsurances considered in the literature:

- Proportional reinsurance.  $U^a = aU$ ,  $0 \le a \le 1$ . .
- Excess-of-loss reinsurance.  $U^a = U \wedge a$ ,  $0 \le$  $a < \infty$ .

• *XL*-reinsurance.  $U^a = U \wedge M + (U - M - L)^+$ . Here  $a = (M, L)$  is described by two parameters  $0 < L, M < \infty$ , with M being called the retention level and  $L$  being called the *limit*.

When the type of the reinsurance is fixed, the premium rate  $p^a$  depends on the premium calculation principle:

- Expected value principle.  $p^a = p (1 + \eta_1)E(U)$  $\bullet$  $-U^{a}$ ), where  $\eta_{1}$  is the safety loading of the reinsurer.
  - *Cheap reinsurance.*  $\eta_1 = \eta$ . In this case,  $p^a = (1 + \eta)E(U^a).$
  - Noncheap reinsurance.  $\eta_1 > \eta$ .

Variance principle.  $\bullet$ 

$$p^{a} = p - [E(U - U^{a}) + p_{1} \text{var}(U - U^{a})]$$

Given the reinsurance scheme, once the level  $a$  is chosen, the dynamics of the surplus process  $R^{a}(t)$ will be governed by equation (1) with  $U$  replaced by  $U^a$  and p replaced by  $p^a$ . If one makes a diffusion approximation then the limiting process will be a linear diffusion with drift  $\mu^a$  and diffusion coefficient  $\sigma^a$ , while  $\sigma^a = E[(U^a)^2]^{1/2}$  is the same as before. Further,  $\mu^a$  is equal to the difference between the premium rate per unit time and the expected losses per unit time.

- proportional reinsurance.  $\mu^a = a\mu$ , Cheap  $\sigma^a = a\sigma.$
- Noncheap proportional reinsurance.  $\mu^a = \mu$   $(1-a)\lambda$ ,  $\sigma^a = a\sigma$ ,  $\lambda > \mu$ .
- Excess-of-loss reinsurance.  $\mu^a = \int_0^a (1 F(x)) dx$ ,  $\sigma^a = \left[ \int_0^a 2x(1 F(x)) dx \right]^{1/2}$ .

In stochastic control models, the reinsurance is dynamically controlled, that is,  $a = a(t)$ , where  $a(t)$ is a process adapted to the information filtration. Other controls used in the insurance optimization models are given below.

## Dividend Control

In the problems where the objective is to maximize the present value of the dividends, the latter is controlled. The corresponding control is described by an increasing functional  $L(t)$  which is the cumulative amount of dividends paid out up to time  $t$ . From the definition, it follows that  $L(t)$  is an increasing right-continuous process with  $L(0-) = 0$ . As with any control functional, it should be adapted to the information filtration, and in addition we require that for any t (deterministic or random)  $L(t) - L(t-) <$  $R(t)$ , where  $R(t)$  is the value of the surplus at time t.

## Investment Control

In case the models allow the surplus to be invested in the financial market we have a third control  $b(t)$ representing the amount invested in the risky asset at time  $t$  (for simplicity, we consider here only the Black-Scholes financial market (see Black-Scholes **Formula**) with one risky asset; the generalization to multiple assets and other markets is obvious).

## Model Formulation and the Hamilton-Jacobi-Bellman Equation

Any stochastic control model starts with a probability space  $(\Omega, \mathcal{F}, P)$  endowed with a filtration (see **Filtrations**)  $\mathcal{F}_t$ ,  $t \ge 0$  and a process  $\sum_{i=1}^{A(t)} U_i$  (in the case of Cramér-Lundberg modeling) or a standard Brownian motion  $w(t)$  adapted to  $\mathcal{F}_t$ . A control  $\pi$  consists of a triple  $(a(\cdot), b(\cdot), L(\cdot))$  of functionals adapted to the information filtration  $\mathcal{F}_t$ . If it satisfies the previously mentioned restrictions, then the control is admissible. Once the control  $\pi$  is chosen, then in the case of the Cramér-Lundberg model the dynamics of the controlled surplus process becomes

$$dR(t) = p^{a(t)} dt - dN^{a(t)}(t)$$
  
+ b(t) dS<sub>1</sub>(t)/S<sub>1</sub>(t) + (R(t)  
- b(t)) dS<sub>0</sub>(t)/S<sub>0</sub>(t) - dL(t) (2)

$$R(0) = x \tag{3}$$

Here,  $dN^{a}(t)(t) = U^{a(t)}1_{A(t)-A(t-)=1}$ . In the case of the diffusion approximation, the surplus is governed by

$$dX(t) = \mu^{a(t)} dt + \sigma^{a(t)} dw(t)$$
  
+ b(t) dS<sub>1</sub>(t)/S<sub>1</sub>(t) + (X(t)  
- b(t)) dS<sub>0</sub>(t)/S<sub>0</sub>(t) - dL(t) (4)

$$X(0) = x \tag{5}$$

with  $S_0(t)$  and  $S_1(t)$  being the price process for riskfree and risky asset, respectively.

#### Objectives

We describe below the two most popular objectives that are studied in the optimization models in insurance.

- Ruin probability minimization. In this case, the third control related to dividends payouts is not present and  $\pi = (a(\cdot), b(\cdot))$ . The stopping time  $\tau$ , which is the hitting time of  $(-\infty, 0)$ by the surplus process (that is the first time when the surplus process becomes negative) is called the ruin time (see **Ruin Theory**). With each control  $\pi$ , a performance index  $J_{\rm x}(\pi) = P(\tau <$  $\infty$ ) is defined, where x stands for the initial surplus. The objective is to find the *value function*  $V(x) = \inf_{\pi} J_x(\pi)$  and the associated *optimal control*  $\pi^*$ , such that  $V(x) = J_x(\pi^*)$ .
- *Dividend optimization*. The performance index in this case is related to the expected cumulative present value of the total dividend payouts until the time of bankruptcy. If there is no setup cost each time the dividend payments are initiated and the payments can be paid in a continuous manner, then  $J_x(\pi) = E\left[\int_0^{\tau} e^{-ct} dL(t)\right]$ , where c is the discount rate. The value function and the optimal control are defined as  $V(x) = \sup_{\pi} J_{x}(\pi)$ and  $J_x(\pi^*) = V(x)$ .

In the models with a setup cost,  $L(t) = \sum_{0}^{\infty} \xi_{i}$  $1_{\zeta_i \leq t}$  where  $\zeta_i$  is an increasing sequence of stopping times, corresponding to the times when the dividends are paid out and  $\xi_i$  is a positive  $\mathcal{F}_{\zeta}$ -measurable random variable representing the amount of dividends paid out at the times  $\zeta_i$ . In this case,  $J_x(\pi) = E\left[\sum_{i=1}^{\infty} e^{-c\zeta_i} g(\xi_i)\right]$ , where  $g(y)$  is a function showing the amount of dividends that reaches shareholders, if  $\nu$  of the surplus is used for the dividend distribution, for example,  $g(x) = x - K.$ 

## Optimality Equations and the Optimal Control

For any fixed pair  $a, b$ , let  $R^{a,b}$  or  $X^{a,b}$  be the process defined by equation (2) or (4), respectively, with  $a(t) \equiv a, b(t) \equiv b$  and  $L(t) \equiv 0$ , and let  $\mathcal{L}^{a,b}$  be the infinitesimal generator of this process. Then dynamic programming shows that if  $V(x)$  is a  $C^2$  function, then in the case of ruin probability minimization it satisfies the Hamilton–Jacobi–Bellman equation:

$$\min_{a,b} \mathcal{L}^{a,b} V(x) = 0 \tag{6}$$

In diffusion models, equation (6) is a fully nonlinear second-order differential equation, while in the Cramer–Lundberg case it is a second order integro- ´ differential equation. One of the boundary conditions for equation (6) is *V (*∞*)* = 0, and the second boundary condition is at the point 0. For the diffusion case, it is *V (*0*)* = 1, while in the Cramer–Lundberg case ´ it is *γV(*0*)* + *δV (*0*)* = 0, with *γ* and *δ* determined from the exogenous parameters of the problem. The argmin *(A*<sup>∗</sup>*(x), B*<sup>∗</sup>*(x))* of the left-hand side of equation (6) provides the *optimal feedback control functions*, which when substituted into equation (2) or (4) as *(A*<sup>∗</sup>*(R(t)), B*<sup>∗</sup>*(R(t)))* or as *(A*<sup>∗</sup>*(X(t)), B*<sup>∗</sup>*(X(t)))* in the place of *a(t)* and *b(t)* results in the stochastic differential equation whose solution yields the optimal surplus process and the optimal control as a function of time.

For the dividend optimization problem, the Hamilton–Jacobi–Bellman equation for the value function takes on the form

$$\max[\max_{a,b} \mathcal{L}^{a,b} V(x) - cV(x), \mathcal{M}V(x)] = 0 \quad (7)$$

The operator M, in the case of continuous dividend payments, is the first-order differential operator 1 − *V (x)*, while in the case of discrete payments it is of a quasi-variational form max*y<x* [*V (x)* − *V (y)* + *(x* − *y)* − *K*]. The boundary conditions at ∞ are of a polynomial growth type. The boundary condition at 0 for the Cramer–Lundberg model is similar to the ´ ruin minimization case, and for the diffusion model it is *V (*0*)* = 0. The optimal feedback risk and investment control functions are determined the same way as before, while the smallest point where the solution satisfies M*V (x)* = 0 determines the level which the surplus under the optimal control should never exceed and reaching which triggers the dividends payments.

# **Bibliographical Remarks**

A discrete time model of ruin probability minimization in which reinsurance and investment are present was considered in [16]. Ruin probability minimization in the Cramer–Lundberg case was studied [9–11]. For diffusion models, this problem was treated in [15, 17, 18, 20].

One of the first dividend maximization problems in the framework of the classical risk process was considered in [4] and [7]. There, the optimality of the barrier strategy was stated. A dividend distribution model with the reinsurance control was studied in [3].

Dividend optimization in diffusion models with continuous dividend payouts was considered in [1, 2, 12–14]. An analysis of the model in which a setup cost leads to discrete optimal dividend payouts is done in [5].

Problems of optimal control of a pension fund were studied in [6] and [8]. The monograph [19] is a good source of the methods and techniques used in application of stochastic control in insurance. It also provides a comprehensive list of the literature.

# **References**

- [1] Asmussen, S., Højgaard, B. & Taksar, M. (1999). Optimal risk control and dividend distribution policies. Example of Excess-of-Loss reinsurance, *Finance and Stochastics* **4**, 299–324.
- [2] Asmussen, S. & Taksar, M. (1997). Controlled diffusion models for optimal dividend pay-out, *Insurance: Mathematics and Economics* **20**, 1–15.
- [3] Azcue, P. & Muler, N. (2005). Optimal reinsurance and dividend distribution policies in Cramer-Lundberg model, *Mathematical Finance* **15**, 261–308.
- [4] Buhlmann, H. (1970). ¨ *Mathematical Methods in Risk Theory*, Springer, New York.
- [5] Cadenillas, A., Choulli, T., Taksar, M. & Zhang, L. (2006). Classical and impulse stochastic control for the optimization of the dividend and risk policies of an insurance firm, *Mathematical Finance* **16**, 181–202.
- [6] Cairns, A. (2000). Some notes on the dynamic and optimal control of stochastic pension fund models in continuous time, *ASTIN Bulletin* **30**, 19–55.
- [7] Gerber, H. (1969). Entscheidungsskriterien fur den ¨ zusammengesetzten poisson-prozess, *Mitteilungen der Vereinigung Schweizerischer Versicherungsmathe matiker* **69**, 185–228.
- [8] Gerber, H. & Shiu, E. (2000). Investing for retirement: optimal capital growth and dynamic asset allocation, *North American Actuarial Journal* **4**, 42–62.
- [9] Hipp, C. & Plum, M. (2000). Optimal investment for insurers, *Insurance: Mathematics and Economics* **27**, 215–228.
- [10] Hipp, C. & Plum, M. (2003). Optimal investment for investors with state dependent income, and for insurers, *Finance and Stochastics* **27**, 215–228.
- [11] Hipp, C. & Vogt, M. (2003). Optimal dynamic XLreinsurance, *ASTIN Bulletin*, **33**, 193–207.
- [12] Højgaard, B. & Taksar, M. (1998). Optimal proportional reinsurance policies for diffusion models, *Scandinavian Actuarial Journal* **2**, 166–168.

# **4 Stochastic Control in Insurance**

- [13] Højgaard, B. & Taksar, M. (1998). Optimal proportional reinsurance policies for diffusion models with transaction costs, *Insurance: Mathematics and Economics* **22**, 41–51.
- [14] Højgaard, B. & Taksar, M. (1999). Controlling risk exposure and dividend pay-out schemes: insurance company example, *Mathematical Finance* **2**, 153–182.
- [15] Luo, S., Taksar, M. & Tsoi, A. (2008). On reinsurance and investment for large insurance portfolios, *Insurance: Mathematics and Economics* **42**, 434–444.
- [16] Schal, M. (2004). On discrete time dynamic program- ¨ ming in insurance: exponential utility and minimization of the ruin probability, *Scandinavian Actuarial Journal* **3**, 189–210.

- [17] Schmidli, H. (2002). On minimizing the ruin probability by investment and reinsurance, *The Annals of Applied Probability* **12**, 890–907.
- [18] Schmidli, H. (2004). Asymptotics of ruin probabilities for risk processes under optimal reinsurance policies, *QUESTA* **46**, 149–157.
- [19] Schmidli, H. (2008). *Stochastic Control in Insurance*, Springer-Verlag, London.
- [20] Taksar, M. & Markussen, C. (2003). Optimal dynamic reinsurance policies for large insurance portfolios, *Finance and Stochastics* **7**, 97–121.

## MICHAEL TAKSAR
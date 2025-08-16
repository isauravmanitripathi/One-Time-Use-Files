# **Merton Problem**

How does an individual decide on where to invest his wealth and how much of it to use during his lifetime? This is a basic question that needs to be answered in order to understand and predict individual economic behavior and also in order to derive the aggregate demands for securities that, together with their supply schedules, determine their prices in equilibrium.

In two path-breaking papers, Merton [21, 22] has formulated and derived the individual's optimal consumption-investment behavior in a continuoustime framework that allows the introduction of a useful structure that can be appropriately molded to model different interesting situations and to yield concrete results. This formulation has come to be known as the *Merton problem*.

## Formulation of the Merton Problem

Let  $P(t) = (P_0(t), \ldots, P_n(t)), 0 \le t \le T$ , denote the prices at time t of  $n + 1$  limited liability assets paying no dividends and traded continuously in a perfect market. The price dynamics of  $P(t)$  is assumed to follow a correlated vector Ito process whose  $i$ th component obeys the general stochastic differential equation

$$\frac{\mathrm{d}P_i}{P_i} = \alpha_i(P, t) \,\mathrm{d}t + \sigma_i(P, t) \,\mathrm{d}z_i \tag{1}$$

For  $i, j = 0, \ldots, n$ , the  $dz_i$ s are correlated Wiener processes satisfying  $dz_i dz_j = \rho_{ij}(P, t) dt$  for given real functions  $\rho_{ij}(\cdot,\cdot)$ ;  $dz_i dt = 0$ ; the expectations  $E(dz_i)$  equal zero; and denote  $\sigma_{ij}(\cdot, \cdot) := \sigma_i \sigma_i \rho_{ij}$ .

At time 0, the individual is endowed with an initial number of units of wealth  $W_0$  and he then selects a complete plan of consumption and investment spanning his lifetime  $[0, T]$  so as to maximize his expected utility of consumption and the bequest he will leave at time  $T$ .

Formally, at any future time  $t$  in  $(0, T]$ , based on the history of the prices, his previous consumption, and previous investment choices, the individual plans to consume at a rate  $c(t)$  and trade so as to hold his remaining wealth  $W(t)$  in a portfolio that is invested in  $N_i(t)$  shares of asset *i*. The consumption and investment choices are said to be the individual's controls.

The individual plans to control his consumption and investment so as to

$$\max E_0 \left[ \int_0^T u(c(t), t) \, \mathrm{d}t + B(W(T)) \right] \tag{2}$$

subject to his wealth constraint

$$W(0) = W_0, W(t) = \sum_{i=0}^{n} N_i(t) P(t), \quad 0 \le t \le T$$
(3)

where  $u$  is the individual's instantaneous utility, and  $B(\cdot)$  is the bequest function.

## **Solution by Dynamic Programming**

To solve the Merton problem by dynamic programming, the wealth constraint (3) is needed in differential form. Taking the total stochastic differential in equation (3), noting that both the number of shares and their prices are Ito processes, results in

$$dW(t) = \sum_{i=0}^{n} N_i(t) dP_i(t) + \sum_{i=0}^{n} dN_i(t) dP_i(t)$$
$$+ \sum_{i=0}^{n} dN_i(t) P_i(t) \qquad (4)$$

Clearly, the first term on the right-hand side (RHS) of equation (4) is associated with the capital gains to the portfolio over the interval  $dt$ resulting from the change in the asset prices. Equally clearly, the third term on the RHS of that equation is associated with the inflow of wealth from external sources that is used to buy additional shares for the portfolio (negative inflow would mean outflow, as when shares are sold to finance consumption.). It is not clear, though, how to associate the middle term on the RHS-with the capital gain or with the cash inflow to the portfolio.

Taking care that choices made at any given time do not anticipate the future, Merton [22] shows that the middle term on the RHS of equation (4), along with the third term, comprise together the total inflow of funds to the portfolio. Therefore, in the absence of other income, the incremental inflow to the portfolio at time  $t$  in this problem is given by  $-c(t) dt = \sum_{i=0}^{n} dN_i(t) dP_i(t)$ 

 $+\sum_{i=0}^{n} dN_i(t)P_i(t)$ , and equation (4) becomes the Merton self-financing condition

$$dW(t) = \sum_{i=0}^{n} N_i(t) dP_i(t) - c(t) dt$$
 (5)

It is remarkable that a special case of Merton's self-financing condition in equation  $(5)$  is equivalent to the Black-Scholes partial differential equation (PDE), which is prominent in derivative pricing.<sup>a</sup>

It is convenient to express the Merton selffinancing condition, equation (4), in terms of portfolio weights,  $w_i(t) := N_i(t)P_i(t)/W(t)$ , which would serve as the portfolio controls from now on instead of the number of shares. Substituting the weights and the asset returns from equation  $(1)$  in equation  $(5)$  yields the differential wealth dynamics,

$$dW(t) = \left(-c + W \sum_{i=0}^{n} w_i \alpha_i\right) dt$$
$$+ W \sum_{i=0}^{n} w_i \sigma_i dz_i, \text{ with } \sum_{i=0}^{n} w_i = 1$$
(6)

which the individual obeys when solving for the consumption and investment controls in the expected utility maximization problem (2).

Since the utility functional in equation  $(2)$  is time-additive, the Merton problem can be solved by dynamic programming. To that end, define the value function (also called the indirect utility of  $wealth)$  by

$$J(W(t), t) := \max_{c(\tau), \{w_i(\tau)\}, t \le \tau \le T}$$
$$E_t \left[ \int_t^T u(c(\tau), \tau) \, \mathrm{d}\tau + B(W(T)) \right] \qquad (7)$$

subject to the wealth dynamics in equation  $(6)$ , and where  $E_t$  denotes the expectation operator given the information at time  $t$ , that is, the knowledge at time  $t$  of the prices, wealth, and consumption rate that determine the conditional probabilities of the future prices.

Then, 
$$J(W(t), t) = \max_{c(\tau), \{w_i(\tau)\}, t \le \tau \le T}$$

$$E_{t} \bigg[ \int_{t}^{t+\Delta t} \bigg[ u(c(\tau), \tau) \, \mathrm{d}\tau$$
  
+ 
$$\int_{t+\Delta t}^{T} u(c(\tau), \tau) \, \mathrm{d}\tau + B(W(T)) \bigg]$$
  
= 
$$\max_{c(\tau), \{w_{t}(\tau)\}, t \leq \tau \leq t+\Delta t} E_{t} \bigg\{ \int_{t}^{t+\Delta t} u(c(\tau), \tau) \, \mathrm{d}\tau$$
  
+ 
$$\max_{c(\tau), \{w_{t}(\tau)\}, t+\Delta t \leq \tau \leq T} E_{t+\Delta t} \bigg[ \int_{t+\Delta t}^{T} u(c(\tau), \tau) \, \mathrm{d}\tau$$
  
+ 
$$B(W(T)) \bigg] \bigg\}$$

(the law of iterated expectations was used above:  $E_t E_{t+\Delta t}[\ ] = E_t[\ ])$ 

$$= \max_{c(\tau), \{w_{l}(\tau)\}, t \leq \tau \leq t + \Delta t} E_{t} \bigg\{ \int_{t}^{t + \Delta t} u(c(\tau), \tau) \, \mathrm{d}\tau$$
$$+ J(W(t + \Delta t), t + \Delta t) \bigg\}$$
$$= \max_{c(t), \{w_{l}(t)\}} E_{t}[u(c(t), t) \Delta t + o(\Delta t)$$
$$+ J(W(t), t) + \Delta J]$$
$$= J(W(t), t) + \max_{c(t), \{w_{l}(t)\}} \{u(c(t), t) \Delta t + o(\Delta t)$$
$$+ E_{t}[\Delta J] \} \tag{8}$$

where  $o(x)$  means a quantity that tends to zero faster than does  $x$ .

By Ito's lemma and by the wealth equation  $(5)$ ,

$$E_{t}[\Delta J] = E_{t} \bigg[ J_{t} \Delta t + J_{W} \Delta W + \frac{1}{2} J_{\text{WW}} (\Delta W)^{2}$$
  
+  $o(\Delta t) \bigg] = J_{t} \Delta t + J_{\text{W}} \bigg( -c + W \sum_{i=0}^{n} w_{i} \alpha_{i} \bigg) \Delta t$   
+  $\frac{1}{2} J_{\text{WW}} W^{2} \bigg( \sum_{i=0}^{n} \sum_{j=0}^{n} w_{i} w_{j} \sigma_{ij} \bigg) \Delta t + o(\Delta t)$   
(9)

Substituting the last expression in equation  $(8)$ , subtracting  $J(W(t), t)$  from both sides, dividing by  $\Delta t$ , and taking the limit  $\Delta t \rightarrow 0$ , yields

$$0 = \max_{c(t), \{w_i(t)\}_0^n} \left\{ u(c(t), t) + J_t \right\}$$

$$+ J_{W} \bigg( -c + W \sum_{i=0}^{n} w_{i} \alpha_{i} \bigg) + \frac{1}{2} J_{WW} W^{2}$$
$$\times \bigg( \sum_{i=0}^{n} \sum_{j=0}^{n} w_{i} w_{j} \sigma_{ij} \bigg) \bigg\}$$
$$\text{subject to } \sum_{i=0}^{n} w_{i} = 1 \tag{10}$$

Equation (10) is the Hamilton-Jacobi-Bellman (HJB) equation for the Merton problem.

#### A Solved Example

The HJB equation yields a nonlinear partial differential equation in the unknown function of two variables  $J(W, t)$  with the end condition  $J(W, T) =$  $B(W(T))$ , the utility from bequest. A solution example is illustrated next for the case with one riskless asset yielding a constant rate of return  $\alpha_0 = r$  and with  $n$  risky assets following correlated geometric Brownian motions, that is,  $\alpha_i$ ,  $\sigma_i$ , and  $\sigma_{ii}$  are all constants, and  $\sigma_{0i} = \sigma_{i0} = 0$ , for  $i, j = 0, \ldots, n$ .

Substituting  $w_0 = 1 - \sum_{i=1}^n w_i$  and  $\sum_{i=0}^n w_i \alpha_i =$  $r + \sum_{i=1}^{n} w_i (\alpha_i - r)$  in the HJB equation  $(10)$  yields

$$0 = \max_{c(t), \{w_i(t)\}_1^n} G(c(t), w_1(t), \dots, w_n(t)), \qquad (11)$$

where  $G(c, w_1, \dots, w_n) := u(c, t) + J_t + J_W$  $\begin{bmatrix} -c & + & rW & + & W\sum_{i=1}^n w_i(\alpha_i - r) \end{bmatrix} + (1/2)$  $J_{\rm WW}W^2\left(\sum_{i=1}^n\sum_{j=1}^n w_i w_j \sigma_{ij}\right)$  is a real function of  $n+1$  free real variables, and the maximization problem exhibits no constraints.

To locate the point  $(c^*, w_1^*, \ldots, w_n^*)$  that maximizes G, requires the  $n + 1$  first-order conditions,

$$\frac{\partial G}{\partial c} = 0 = \frac{\partial u}{\partial c}(c, t) - J_w \tag{12}$$
$$\frac{\partial G}{\partial w_i} = 0 = J_w(\alpha_i - r) + J_{\rm WW}W \sum_{j=1}^n w_j \sigma_{ij},$$
$$(i = 1, \dots, n) \tag{13}$$

If for every time t,  $u(c, t)$  is strictly concave and twice continuously differentiable in  $c$ , then equation (12) can be inverted to yield  $c^* = f(J_W, t)$ . The system of linear equations (13) can be solved for the weights on the risky assets  $w_i^*$  as functions of  $J_W$ ,  $J_{\text{WW}}$ , and W. Then these  $(c^*, w_1^*, \ldots, w_n^*)$  are substituted back in equation  $(11)$  to yield

$$0 = G(c^*, w_1^*, \dots, w_n^*) \tag{14}$$

which then becomes a nonlinear partial differential equation of the second order in the unknown function  $J(W, t)$  with the end condition  $J(W, T) =$  $B(W(T)).$ 

Merton [21] demonstrates closed-form solutions to equation  $(14)$  for some special cases. For example, assume that the instantaneous utility of consumption is the isoelastic,  $u(c, t) = \exp(-\rho t)c^{\gamma}/\gamma$ ; utility from bequest is 0; there are two available assets, one is risk-free returning at a rate  $r$  and the other risky, following a Geometric Brownian motion with a constant drift,  $\alpha$ , and a constant variance per unit time,  $\sigma^2$ . Then the optimal weight that the portfolio puts on the risky asset is the constant  $w^*(t) = (\alpha - r)/[(1 - \alpha - r)]$  $(\gamma)\sigma^2$ ,  $0 \le t \le T$ , and the optimal consumption rate is given by  $c^*(t) = W(t)a/[(1 - \exp(-a(T - t))],$  $0 \le t \le T$ , where  $W(t)$  is the value of the portfolio at time  $t$ , and where

$$a := \frac{\gamma}{1-\gamma} \left[ \frac{\rho}{\gamma} - r - \frac{1}{2} \left( \frac{\alpha-r}{\sigma} \right)^2 \frac{1}{1-\gamma} \right] \quad (15)$$

Generally, however, equation  $(14)$  must be solved numerically.

## The Merton Problem with State-dependent **Price Process Parameters**

Merton [23] extends his problem to include parameters of the price processes that depend on a state variable  $x$  which itself follows an Ito process, that is,

$$\frac{\mathrm{d}P_i}{P_i} = \alpha_i(x, t) \,\mathrm{d}t + \sigma_i(x, t) \,\mathrm{d}z_i,$$
  
(0 \le t \le T, i = 0, \ldots, n) (16)

$$dx = a(x, t) dt + s(x, t) dz$$
 (17)

where the  $dz_i$  and dz are correlated Wiener processes satisfying  $dz_i dz_i = \rho_{ij}(x, t) dt$ ;  $dz_i dz = \rho_{ix} dt$ ;  $dz_i dt = dz dt = 0$ ,  $E(dz_i) = 0$ ;  $(i, j = 0, ..., n)$ . Denote  $\boldsymbol{\alpha} := (\alpha_1, \ldots, \alpha_n), \quad \mathbf{r} := (r, \ldots, r), \quad \boldsymbol{\sigma}_x :=$  $(\rho_{1x}\sigma_1s,\ldots,\rho_{nx}\sigma_ns)$ , and  $\sigma$  denote by the matrix with  $\sigma_{ij} := \sigma_i \sigma_i \rho_{ij}$  in the *ij* place.

Defining the indirect utility  $J(W, x, t)$  as before, but recognizing that it now depends also on the state variable, and following the same derivation as before with the obvious modifications, Merton [23] shows that in the presence of a riskless asset returning at the constant rate  $r$ , the optimal investment plan described by the control vector process of weights on the risky assets in the portfolio that maximizes lifetime utility of consumption is given by

$$\mathbf{w}_{t}^{*} = \left(-\frac{J_{W}}{WJ_{\text{WW}}}\right)\boldsymbol{\sigma}^{-1}(\boldsymbol{\alpha} - \mathbf{r}) + \left(-\frac{J_{\text{xW}}}{WJ_{\text{WW}}}\right)\boldsymbol{\sigma}^{-1}\boldsymbol{\sigma}_{\text{x}}$$
$$=: D\mathbf{d} + H\mathbf{h}, \quad 0 \le t \le T \tag{18}$$

The scalars  $D$  and  $H$  are agent specific, but the vectors  $\mathbf{d}$  and  $\mathbf{h}$  are not. It follows that every investor behaves as if the risky part of his portfolio is split between two mutual funds holding total portfolios with weights that are proportional to  $\mathbf{d}$ and  $\mathbf{h}$ , respectively; then there is also the part that is invested in the risk-free asset. The result is a three-fund separation theorem. Merton [23] shows that while the first risky mutual fund is used to diversify, that is, to obtain the largest expected return for a given amount of risk borne, the second risky mutual fund is used to hedge unfavorable shifts in the state variable  $x$ , in the sense that if an increase in  $x$  diminishes planned consumption, then the investor compensates himself by shifting wealth to the asset with returns that increase with  $x$ .

The Merton problem was first formulated and solved using stochastic control in  $[21, 22]$ . It provides the basis for the intertemporal capital asset pricing model in  $[23]$ . Extensions of the problem include  $[19]$ , 20, 26]. In references  $[3, 4, 12-15]$ , the problem is treated in incomplete markets and under other market constraints. Transaction costs are introduced into the Merton problem in  $[1, 5, 11, 29]$ . The problem is extended to incomplete information settings in  $[6, 8,$ 27]; to settings with habit formation utilities in [7,  $17, 28$ ; and to settings with recursive utilities in [2, 10]. Textbooks that provide a detailed treatment of the Merton problem include [9, 16, 25].

#### **End Notes**

<sup>a.</sup>Specifically, suppose the portfolio comprises two assets, one risky and one riskless, and that there are no inflows to or outflows from the portfolio, that is,  $c(t) = 0$  for all t. Then, if only Markov controls of the portfolio are considered, namely, number of units of the two assets that depend only on time and the concurrent price, it follows that the value of the portfolio which then obviously depends only on time and the concurrent price of the risky asset, can be shown to necessarily satisfy the Black-Scholes PDE. Moreover, the number of shares of the risky asset in the portfolio is equal to the partial derivative of the said portfolio value function with respect to the price of the risky asset (see [18, 24]). The converse is also true.

### References

- $[1]$ Akian, M., Menaldi, J.-L. & Sulem, A. (1996). On an investment-consumption model with transaction costs, SIAM Journal on Control and Optimization 34, 329-364.
- Bergman, Y.Z. (1985). Time preference and capital asset [2] pricing models, Journal of Financial Economics 14,  $145 - 159.$
- Brennan, M., Schwartz, E. & Lagnado, R. (1997). Strate-[3] gic asset allocation, Journal of Economic Dynamics and Control 21, 1377-1403.
- Cvitanic, J. & Karatzas, I. (1996). Hedging and port-[4] folio optimization under transaction costs: a martingale approach, Mathematical Finance 6, 133-165.
- Davis, M. & Norman, A. (1990). Portfolio selection with [5] transaction costs. Mathematics of Operations Research 15, 676–713.
- [6] Detemple, J. (1986). Asset pricing in a production economy with incomplete information, Journal of Finance 41, 383-391.
- Detemple, J. & Zapatero, F. (1992). Optimal [7] consumption-portfolio policies with habit formation, Mathematical Finance 2, 251-274.
- Dotan, M. & Feldman, D. (1986). Equilibrium interest [8] rates and multiperiod bonds in a partially observable economy, Journal of Finance 41, 369-382.
- [9] Duffie, D. (2001). Dynamic Asset Pricing Theory, Princeton University Press, Princeton.
- [10] Duffie, D. & Epstein, L. (1992). Asset pricing with stochastic differential utility, Review of Financial Studies 5, 411–436.
- [11] Duffie, D. & Sun, T.S. (1990). Transactions costs and portfolio choice in a discrete-continuous time setting, Journal of Economic Dynamics and Control 14, 35-51.
- [12] Dybvig, P. (1995). Duesenberry's ratcheting of consumption: optimal dynamic consumption and investment given intolerance for any decline in standard of living, Review of Economic Studies 62, 287-313.
- [13] Fleming, A. & Zariphopoulou, T. (1991). An optimal Investment-consumption model with borrowing constraints, Mathematics of Operations Research 16, 802-822.
- [14] He, H. & Pagès, H. (1993). Labor income, borrowing constraints, and equilibrium asset prices, Economic Theory 3, 663–696.

- [15] Hindy, A. (1995). Viable prices in financial markets with solvency constraints, *Journal of Mathematical Economics* **24**, 105–136.
- [16] Ingersoll, J. (1987). *Theory of Financial Decision Making*, Rowman and Littlefield, Totowa.
- [17] Ingersoll, J. (1992). Optimal consumption and portfolio rules with intertemporally dependent utility of consumption, *Journal of Economic Dynamics and Control* **16**, 681–712.
- [18] Jarrow, R.A. & Rudd, A. (1983). *Option Pricing*, Irwin, 100–105.
- [19] Karatzas, I., Lehoczky, J., Sethi, S. & Shreve, S. (1986). Explicit solution of a general consumption-investment problem, *Mathematics of Operations Research* **11** , 261–264.
- [20] Lehoczky, J., Sethi, S. & Shreve, S. (1983). Optimal consumption and investment policies allowing consumption constraints and bankruptcy, *Mathematics of Operations Research* **8**, 613–636.
- [21] Merton, R.C. (1969). Lifetime portfolio selection under uncertainty—continuous-time case, *Review of Economics and Statistics* **51**, 247–257.
- [22] Merton, R.C. (1971). Optimum consumption and portfolio rules in a continuous-time model, *Journal of Economic Theory* **3**, 373–413.
- [23] Merton, R.C. (1973). Intertemporal capital asset pricing model, *Econometrica* **41**, 867–887.
- [24] Merton, R.C. (1977). On the pricing of contingent claims and the Modigliani–Miller theorem, *Journal of Financial Economics* **5**, 241–250.
- [25] Merton, R.C. (1990). *Continuous-Time Finance*, Basil Blackwell.
- [26] Richard, S. (1975). Optimal consumption, portfolio, and life insurance rules for an uncertain lived individual in a continuous time model, *Journal of Financial Economics* **2**, 187–203.
- [27] Schweizer, M. (1994). Risk-minimizing hedging strategies under restricted information, *Mathematical Finance* **4**, 327–342.
- [28] Sundaresan, S. (1989). Intertemporally dependent preferences in the theories of consumption, portfolio choices and equilibrium asset pricing, *Review of Financial Studies* **2**, 73–89.
- [29] Vayanos, D. (1998). Transaction costs and asset pricing: a dynamic equilibrium model, *Review of Financial Studies* **11**, 1–58.

YAACOV Z. BERGMAN
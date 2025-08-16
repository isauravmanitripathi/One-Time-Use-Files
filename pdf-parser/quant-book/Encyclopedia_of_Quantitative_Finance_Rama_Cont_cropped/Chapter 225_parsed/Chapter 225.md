# **Stochastic Volatility Interest Rate Models**

Stochastic volatility has been widely used to model implied volatility smiles for European caps and swaptions. We discuss models of the yield curve that incorporate stochastic volatility, defined as randomness in the volatility of the bond prices that is not spanned by movements in the yield curve. We argue that it is difficult to specify short rate models that exhibit unspanned stochastic volatility and that a more natural choice for construction of stochastic volatility models is the Heath, Jarrow, and Morton (HJM) or Libor Market Model framework. We then consider the specification of stochastic volatility interest rate models and survey some of the stochastic volatility models found in the literature.

## **"Unspanned" Stochastic Volatility**

S*tochastic volatility* interest-rate models are models that prescribe moves in the volatility of rates that cannot directly be inferred from the shape or the level of the yield curve. Let *P (t, T )* be the time *t* price of a zero-coupon bond maturing at time *T* and let the time *t* continuously compounded forward rate for deposit over the interval [*T,T* + *dT* ] be given by

$$f(t,T) = -\frac{\partial \ln P(t,T)}{\partial T}, t \le T \tag{1}$$

Assume that interest rates evolve continuously. As shown by Heath *et al.* [9], absence of arbitrage implies that the forward rates have to evolve according to (*see* **Heath–Jarrow–Morton Approach** for the HJM model)

$$df(t,T) = \sigma(t,T) \cdot \left(\int_t^T \sigma(t,s) \, ds\right) dt$$
  
+  $\sigma(t,T) \cdot dW(t)$  (2)

where *W* is a vector Brownian motion under the risk-neutral measure, and {*σ (t, T )*}*t*≤*<sup>T</sup>* some family of vector processes.

A "true" stochastic volatility model has the property that there exists some stochastic process *z* and at least one maturity *U*, so that

$$\frac{\partial \sigma(t, U)}{\partial z(t)} \neq 0 \tag{3a}$$

*and*

$$\frac{\partial f(t,T)}{\partial z(t)} = 0 \tag{3b}$$

for all *T* .

In other words, "true" or "unspanned" stochastic volatility is when there is uncertainty in the volatility of the rates, which cannot be fully hedged by taking positions in bonds. There is considerable empirical evidence of unspanned stochastic volatility in interest rates and interest rate options markets (see, e.g., Casassus *et al.* [5]).

It is very difficult to specify a traditional shortrate model that can be categorized as a true stochastic volatility model. This is so because stochastic shortrate volatility will tend to show up as a second factor that the bond prices will depend on. Consider, for example, the model by Fong and Vasicek [7]:

$$dr(t) = \kappa(\theta - r(t)) dt + \sqrt{v(t)} dW_1(t)$$
  

$$dv(t) = \beta(\alpha - v(t)) dt + \varepsilon \sqrt{v(t)} dW_2(t) \quad (4)$$
  

$$dW_1(t) \cdot dW_2(t) = \rho dt$$

where *κ, θ , β, α, ε, ρ* are constants, and *W*<sup>1</sup> and *W*<sup>2</sup> Brownian motions under the risk-neutral measure. In this model, we have

$$P(t,T) = E_t \left[ e^{-\int_t^T r(u) du} \right]$$
  
=  $E \left[ e^{-\int_t^T r(u) du} |r(t), v(t) \right]$  (5)  
 $\equiv P(t,T; r(t), v(t))$ 

So the bond price becomes a function of two stochastic variables. Hence, we can invert the system and infer the level of both the short rate and the short rate volatility from any two points on the yield curve. Thus, the model is not a true stochastic volatility model. This is also the case for the Longstaff and Schwartz [13] model and other early attempts to produce stochastic volatility yield curve model.

In fact, it is also the case for attempts to formulate a stochastic volatility yield curve model in the context of the Markov functional approach by Hunt *et al.* [12] (*see* **Markov Functional Models** for the Markov functional models).

So, as observed by Andreasen *et al.* [4], the most straightforward way of formulating a stochastic volatility yield curve model is to directly use the HJM approach, or equivalently the Libor market model approach, and directly specify the stochastic nature of the bond or forward rate volatility structure (see LIBOR Market Model for the Libor market model). In the HJM modeling approach, we see that it is easy to specify a volatility structure satisfying equation (3a,b). We could, for example, set  $\sigma(t, T)$  =  $c \cdot \sqrt{z(t)}$  for some constant c and some Markov process  $z$ .

Intuitively, if the volatility is nondeterministic, then the minimal number of state variables in a HJM model is two, so with the addition of stochastic volatility the number of state variables in a "true" stochastic volatility HJM model is at least three. In fact, Dufresne and Goldstein [6] provide a partial differential equation (PDE)-based argument to justify that the minimal number of state variables for a "true" stochastic volatility interest rate model is three.

#### **Model Specifications**

In the following, we present some examples of stochastic volatility interest-rate models. A Libor market model is based on a discrete time grid  $0 =$  $t_0 < t_1 < \dots$  Let

$$L_k(t) = \frac{1}{t_{k+1} - t_k} \left( \frac{P(t, t_k)}{P(t, t_{k+1})} - 1 \right) \tag{6}$$

be the forward Libor rate over the period  $[t_k, t_{k+1}]$ . Under absence of arbitrage, we have

$$\mathrm{d}L_{k}(t) = \vartheta_{k}(t) \cdot \sum_{j=i+1}^{k} \frac{\delta_{j} \vartheta_{j}(t)}{1 + \delta_{j} L_{j}(t)} \,\mathrm{d}t$$
$$+ \vartheta_{k}(t) \cdot \mathrm{d}\widetilde{W}(t), t_{i-1} \le t < t_{i} \qquad (7)$$

for a discrete set of vector processes  $\{\vartheta_k(t)\}_{t \leq t_k}$ and  $\widetilde{W}$  being a vector Brownian motion under the martingale measure with  $B(t) = \left(\prod_{j=0}^{n-1} P(t_j, t_{j+1})\right)$  $\times P(t, t_{n+1}), t_n \le t < t_{n+1}$  as numeraire.

Andersen and Brotherton-Ratcliffe [3] consider an uncorrelated stochastic volatility extended constant elasticity of variance (CEV) Libor market model

$$\begin{aligned} \|\vartheta_k(t)\| &= \sqrt{z(t)}\lambda_k(t)L_k(t)^{\beta} \\ \mathrm{d}z(t) &= \theta(1-z(t))\,\mathrm{d}t + \varepsilon\sqrt{z(t)}\,\mathrm{d}Z(t) \\ \mathrm{d}L_k(t) \cdot \mathrm{d}z(t) &= 0 \end{aligned} \tag{8}$$

where Z is a Brownian motion,  $\lambda_k$  is a timedependent function, and  $\theta$ ,  $\varepsilon$  are constants. Andersen and Brotherton-Ratcliffe suggest asymptotic expansions for solving for European swaption prices based on approximation of the swap rate dynamics.

Piterbarg [16] replaces the CEV assumption for the forward rate volatility with a linear one:

$$\begin{aligned} \|\vartheta_k(t)\| &= \sqrt{z(t)}\lambda_k(t)[\beta_k(t)L_k(t) \\ &+ (1 - \beta_k(t))L_k(0)] \\ \mathrm{d}z(t) &= \theta(1 - z(t))\,\mathrm{d}t + \varepsilon\sqrt{z(t)}\,\mathrm{d}Z(t) \\ \mathrm{d}L_k(t) \cdot \mathrm{d}z(t) &= 0 \end{aligned} \tag{9}$$

Piterbarg shows that using time- and tenordependent skew coefficients  $(\beta_k(t))$  improves the simultaneous fit to implied cap and swaption skews and smiles. Piterbarg solves for European swaption prices using Markovian projection techniques applied to the process for the swap rate.

Andersen and Andreasen [2] present a one-factor Markov HJM model with uncorrelated stochastic volatility:

$$P(t,T) = \frac{P(0,T)}{P(0,t)} e^{-G(t,T)x(t) - \frac{1}{2}G(t,T)^2 y(t)}$$
$$G(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}$$
$$dx(t) = (-\kappa x(t) + y(t)) dt + \eta(t) dW(t)$$
$$dy(t) = (\eta(t)^2 - 2\kappa y(t)) dt$$
$$\eta(t) = \lambda(t) \sqrt{z(t)} [\beta R(t,s,T) + (1-\beta)R(0,s,T)]$$
$$dz(t) = \theta(1-z(t)) dt + \varepsilon \sqrt{z(t)} dZ(t)$$
$$dW(t) \cdot dZ(t) = 0 \tag{10}$$

where  $W, Z$  are Brownian motions under the riskneutral measure and

$$R(t,s,T) = -\frac{1}{T-s} \ln \frac{P(t,T)}{P(t,s)}$$
(11)

is a continuously compounded zero-coupon forward rate that is linked to the choice of calibration instruments. Piterbarg's Markovian projection techniques are used for calibration of the model. Owing to the limited number of state variables (equation 3), the model allows for finite difference solution and efficient simulations.

Andreasen [1] presents a multifactor Markov HJM model that extends equation  $(10)$  and allows for time- and tenor-dependent skew as in equation (9). For a selected set of (continuously compounded) forward rates with tenors, the dynamics are similar to the forward rate dynamics in equation  $(9)$  (see also Markovian Term Structure Models).

The models discussed so far are all based on zero correlation between the interest rates and the stochastic volatility process. The reason for this choice is mainly technical: if it were not the case, then the stochastic volatility process would be different for different annuity measures (see Forward and Swap Measures) and it would often include complicated terms in its drift. This would, in turn, make approximation of the swaption prices and thereby calibration more complicated.

The reason for the choice of square-root process for the stochastic volatility is also tractability. The square-root process admits computation of exponential moments in closed form and this can either be used for approximation of at-the-money option prices as in Piterbarg [16] or for direct computation of option prices via numerical inversion of Fourier transforms. An example of the latter is the model in equation (10) with level independent but correlated volatility:

$$\eta(t) = \lambda(t)\sqrt{z(t)}$$
  
dW(t) \cdot dZ(t) = \rho(t) dt (12)

where  $\rho$  is a time-dependent function. For this model, the processes for the maturity  $U$  forward bond price  $P(t, U)/P(t, T)$  and the stochastic volatility factor, z, are

$$\frac{\mathrm{d}(P(t,U)/P(t,T))}{(P(t,U)/P(t,T))} = \lambda(t)\sqrt{z(t)}(G(t,T))$$
$$-G(t,U)\,\mathrm{d}W^{T}(t)$$
$$\mathrm{d}z(t) = \theta(1-z(t))\,\mathrm{d}t + \varepsilon\sqrt{z(t)}\,\mathrm{d}Z^{T}(t)$$
$$-\rho\varepsilon z(t)\lambda(t)G(t,T)\,\mathrm{d}t \quad (13)$$

where  $W^T$ ,  $Z^T$  are correlated Brownian motions under the maturity  $T$  forward measure. So, essentially, the processes in equation  $(13)$  are similar to the single-asset stochastic volatility model of Heston [11] but with time-dependent parameters. So, as shown by Dufresne and Goldstein [6], this means that the prices of caplets and options on zero-coupon bonds can be

found by numerical inversion of Fourier transforms in the same way as for the Heston model. Swaption prices can, in turn, be found by approximating swaptions as options on zero-coupon bonds by duration matching as suggested by Munk [14].

As an alternative to the square-root process for the stochastic volatility, Rebonato [15] and Henry-Labordere [10] consider the SABR-based stochastic volatility Libor market models with correlated stochastic volatility of the form (see [8] for the SABR model).

$$\begin{aligned} \mathrm{d}L_k(t) &= z\lambda_k(t)L_k(t)^{\beta_k}\,\mathrm{d}W_k(t) + O(\,\mathrm{d}t),\\ k &= 1,\dots,n\\ \mathrm{d}z(t) &= vz(t)\,\mathrm{d}W_{n+1}(t) \end{aligned} \tag{14}$$

$$\mathrm{d}W_i(t)\cdot\mathrm{d}W_j(t)=\rho_{ij}(t)\,\mathrm{d}t,$$

 $i, j = 1, \ldots, n + 1$ 

where v is a constant and  $\{\rho_{ii}(t)\}\$ is time dependent. Henry-Labordere provides asymptotic expansion results for the prices of caplets and swaptions based on hyperbolic geometry methods.

### References

- [1] Andreasen, J. (2005). Back to the future, Risk 18(9),  $72 - 78$
- Andersen, L. & Andreasen, J. (2002). Volatile volatili-[2] ties, Risk 15(12), 65-71.
- Andersen, L. & Brotherton-Ratcliffe, R. (2005). [3] Extended libor market models with stochastic volatility, *Journal of Computational Finance* **9**, 1–40.
- [4] Andreasen, J., Dufresne, P. & Shi, W. (1994). An arbitrage term Structure model of interest rates with stochastic volatility.
- Casassus, J., Dufresne, P. & Goldstein, R. (2005). [5] Unspanned stochastic volatility and fixed income derivatives pricing, Journal of Banking and Finance 29, 2723-2749.
- [6] Dufresne, P. & Goldstein, R. (2002). Do bonds span the fixed income markets? Theory and evidence for unspanned stochastic volatility, Journal of Finance 57,  $1685 - 1730.$
- Fong, H. & Vasicek, O. (1991). Fixed income volatility [7] management, The Journal of Portfolio Management,  $41 - 46$
- Hagan, P., Kumar, D., Lesniewski, A. & Woodward, D. [8] (2002). Managing smile risk, Wilmott Magazine 2(7),  $84 - 108.$
- Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing [9] and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**, 77-106.

## **4 Stochastic Volatility Interest Rate Models**

- [10] Henry-Labordere, P. (2007). Combining the SABR and LMM models, *Risk* **20**(10), 102–107.
- [11] Heston, S. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–344.
- [12] Hunt, P., Kennedy, J. & Pelsser, A. (1998). Fit and run, *Risk* **10**(11), 65–67.
- [13] Longstaff, F. & Schwartz, E. (1992). Interest rate volatility and the term structure: a two-factor general equilibrium model, *Journal of Finance* **47**, 1259–1282.
- [14] Munk, C. (1999). Stochastic duration and fast coupon bond option pricing in multi-factor models, *Review of Derivatives Research* **3**, 157–181.
- [15] Rebonato, R. (2001). The stochastic volatility LIBOR market model, *Risk* **13**(10), 105–110.

[16] Piterbarg, V. (2003). *A Stochastic Volatility Forward Libor Model with a Term Structure of Volatility Smiles*. Bank of America working paper. Available from http:// papers.ssrn.com/sol3/papers.cfm?abstract−id=472061.

## **Related Articles**

**Heath–Jarrow–Morton Approach**; **Heston Model**; **LIBOR Market Model**; **Markovian Term Structure Models**.

JESPER ANDREASEN
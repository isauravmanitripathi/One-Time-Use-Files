# **Markovian Term Structure Models**

An interest rate model is said to be Markovian (see **Markov Processes**) in  $N$  state variables if all discount factors at any future date can be written as a function of an N-dimensional Markov process. HJM [7] and Libor market models are generally not Markov in a limited number of state variables—the full yield curve has to be included as a Markov state variable. The separable forward rate volatility structure in the HJM introduced by Babbs [4], Cheyette [5], Jamshidian [8], and Ritchken and Sankarasubramaniam [11] avoids this problem. Specifically, if the dimension of the driving Brownian motion is  $n$ , then a model with separable volatility will have a Markov representation in  $N = n + n(n+1)/2$  state variables. We discuss the connection to short rate models in general and Gaussian models in particular, calibration techniques, simulation and finitedifference implementation, and the specification of multifactor separable models.

## Non-Markovian Nature of HJM Models

Let  $P(t, T)$  be the time t price of a zero-coupon bond with maturity  $T$ . The continuously compounded forward rates are given by

$$f(t,T) = -\frac{\partial \ln P(t,T)}{\partial T} \tag{1}$$

and the short rate is given by

$$r(t) = f(t, t) \tag{2}$$

Under the assumption of continuous dynamics and one driving Brownian motion, in  $[3, 7]$  it is shown that the absence of arbitrage implies that forward rates evolve according to

$$df(t,T) = \sigma(t,T) \left( \int_{t}^{T} \sigma(t,s) \, ds \right) dt$$
  
+  $\sigma(t,T) \, dW(t)$  (3)

where  $\{\sigma(t,T)\}_{t\leq T}$  is a family of volatility processes and  $W$  is a Brownian motion under the riskneutral measure, that is, the martingale measure under which the bank account  $B(t) = \exp\left(\int_0^t r(u) \, \mathrm{d}u\right)$  is the numeraire.

This shows that all that is required to construct an arbitrage-free interest rate model that automatically fits the initial yield curve is a specification of the forward rate volatility structure  $\{\sigma(t, T)\}_{t \leq T}$ .

The problem, however, with arbitrary specification of the volatility structure is that the resulting model will generally not be Markov in a limited number of state variables. In general, the whole continuum  $\{f(t, T)\}_{t \leq T}$  has to be used as state variables for the model. This is true regardless of the dimension of the driving Brownian motion and it is also the case for deterministic forward rate volatility structures. It should be stressed that the Libor market model exhibits the same problem. Generally, it will require all the modeled discrete forward rates as Markov state variables.

#### **Separable Volatility Structure**

**Heath–Jarrow–Morton Approach** gives the necessary and sufficient conditions on the forward rate volatility structure for the resulting HJM model to be Markov. An important subset of the general class of Markov HJM models is the separable volatility structure models, independently introduced by Babbs [4], Cheyette [5], Jamshidian [8], and Ritchken and Sankarasubramaniam [11]. For the one-factor case, the separable form is to assume that the forward rate volatility structure is given by

$$\sigma(t,T) = g(T)h(t) \tag{4}$$

where  $g$  is a deterministic function and  $h$  is a process.

Under the assumption  $(4)$ , equation  $(3)$  can be rewritten as

$$f(t,T) = f(0,T) + \frac{g(T)}{g(t)}x(t) + y(t)\int_{t}^{T} \frac{g(s)}{g(t)}ds$$
(5)

where

$$dx(t) = \left(\frac{g'(t)}{g(t)}x(t) + y(t)\right) dt$$
$$+ g(t)h(t) dW(t), \quad x(0) = 0$$

$$dy(t) = (g(t)^{2}h(t)^{2} + 2\frac{g'(t)}{g(t)}y(t)) dt,$$
  
 
$$y(0) = 0$$
 (6)

72.

By defining  $\kappa(t) = -g'(t)/g(t)$ ,  $\eta(t) = g(t)h(t)$ and integrating equation  $(5)$  we obtain the more convenient model representation

$$P(t,T) = \frac{P(0,T)}{P(0,t)} e^{-G(t,T)x(t) - \frac{1}{2}G(t,T)^2 y(t)}$$
  

$$dx(t) = (-\kappa(t)x(t) + y(t)) dt + \eta(t) dW(t),$$
  

$$x(0) = 0$$
  

$$dy(t) = (\eta(t)^2 - 2\kappa(t)y(t)) dt, \quad y(0) = 0$$
  

$$G(t,T) = \int_t^T e^{-\int_t^s \kappa(u) du} ds \qquad (7)$$

So if we assume  $\eta = \eta(t, x(t), y(t))$ , then we have a Markov representation of the full yield curve in the state variables  $x, y$ . Here, we can interpret x as a stochastic yield curve factor that perturbs the yield curve and  $\nu$  as a locally deterministic convexity term that has to be included to keep the model arbitragefree.

It should be noted here that the bond prices are exponentially affine in the state variables. The separable model thus belongs to the general class of affine models (see Affine Models). In this class it is a special member, as the model's second locally deterministic state variable  $(y)$  eliminates the need for  $\eta(t, x, y)^2$  to be linear in  $(x, y)$ , as in the models studied in [6].

From equation (5) we note that  $r(t) = f(0, t) +$  $x(t)$  and consequently that the process for the short rate is

$$dr(t) = \left[\frac{\partial f(0, t)}{\partial t} + \kappa(t)(r(t) - f(0, t)) + y(t)\right]$$
  
$$nd \times dt + \eta(t) dW(t)$$
 (8)

If we set  $\eta = \lambda(t)r(t)^{\beta}$ , we get a model that, except for the state variable  $y$  included in the drift term of the short rate, is very similar to the short rate models by Vasicek [12], and others.<sup>a</sup>

For  $\beta = 0$ , or equivalently  $\eta$  deterministic, y becomes deterministic, and the model is equivalent to the Gaussian model, that is, a general time-dependent parameter version of the Vasicek [12] model. For this case, equation  $(7)$  can be seen as a convenient implementation of a time-dependent Vasicek model. The fact that the separable volatility models have a structure that is very close to the Gaussian models led Babbs [4] and Jamshidian [8] to term these models *auasi-Gaussian* and *pseudo-Gaussian*, respectively.

Another feature shared with the Gaussian model is that for fixed  $\kappa$  the distribution of the rates at time  $t$  only depends on the volatility up to time  $t, \{\eta(u)\}_{0\leq u\leq t}.$  This means that the model can be bootstrap calibrated to swaption prices, by calibrating the model to one swaption expiry at the time. This is not the case for general short rate models because the bond price  $P(t, T)$  generally depends on the short rate volatility over the interval  $[t, T]$ . So short rate models generally have to be calibrated to swaption prices using global routines.

#### **Model Implementation**

The forward par swap rate for swapping over the dates  $t_0, t_1, \ldots, t_n$  is given by

$$S(t) = \frac{P(t, t_0) - P(t, t_n)}{A(t)},$$
  
$$A(t) = \sum_{i=1}^{n} \delta_i P(t, t_i), \quad \delta_i = t_i - t_{i-1} \qquad (9)$$

Following Forward and Swap Measures, we have that the swap rate is a martingale under the annuity measure, so we can write

$$dS(t) = \frac{\partial S(t)}{\partial x} \eta(t) dW^{A}(t) \tag{10}$$

where  $W^A$  is a Brownian motion under the martingale measure with the annuity  $A$  as numeraire. This can be used for deriving approximations for the value of swaptions using the same techniques as in the Libor market model literature. Specifically, we may, for example, approximate the stochastic differential equation (SDE)  $(10)$  by

$$dS(t) = \lambda(\beta S(t) + (1 - \beta)S(0)) dW^{A}(t) \qquad (11)$$

Matching the diffusions in equations  $(10)$  and  $(11)$ in level and derivative with respect to  $x$  along the path  $x = y = 0$  yields

$$\lambda^{2} = t^{-1} S(0)^{-2} \int_{0}^{t} [(S_{x}(u)^{2} \eta(u)^{2}]_{x=y=0} du$$

$$\beta = \frac{\int_{0}^{t} [S_{x}(u)S_{xx}(u)\eta(u)^{2} + S_{x}(u)^{2}\eta(u)\eta_{x}(u)]_{x=y=0} du}{\lambda^{2} S(0) \int_{0}^{t} [S_{x}(u)]_{x=y=0} du}$$
(12)

where we have used subscripts for derivatives, so  $S_x = \partial S/\partial x, \eta_x = \partial \eta/\partial x.$ 

From this we have that the swaption prices of the model can be approximated by

$$E^{A}[(S(t) - K)^{+}] \approx \frac{1}{\beta}[S(0)\Phi(z_{+}) - \overline{K}\Phi(z_{-})]$$
$$\overline{K} = \beta K + (1 - \beta)S(0)$$
$$z_{\pm} = \frac{\ln(S(0)/\overline{K})}{\beta\lambda\sqrt{t}} \pm \frac{1}{2}\beta\lambda\sqrt{t}$$
(13)

More refined approximations based on the Markovian projection techniques of Piterbarg [10] can be found in  $[2]$ .

Let  $0 = t_0 < t_1 < \dots$  be a simulation time line. Then using equation  $(5)$  it can be shown that

$$x(t_{i+1}) = \frac{g(t_{i+1})}{g(t_i)} x(t_i) + \frac{g(t_{i+1})}{g(t_i)} \left( \int_{t_i}^{t_{i+1}} \frac{g(u)}{g(t_i)} du \right)$$
$$\times y(t_i) + \int_{t_i}^{t_{i+1}} \frac{g(t_{i+1})}{g(u)} \eta(u) \, dW^{t_{i+1}}(u)$$
$$y(t_{i+1}) = \left( \frac{g(t_{i+1})}{g(t_i)} \right)^2 y(t_i) + \int_{t_i}^{t_{i+1}} \left( \frac{g(t_{i+1})}{g(u)} \right)^2$$
$$\times \eta(u)^2 du \tag{14}$$

where  $W^T$  is a Brownian motion under the martingale measure with  $P(\cdot, T)$  as numeraire, that is, the maturity  $T$  forward measure.

If we make the approximation  $\eta(t) = \eta(t_i)$  for  $t \in [t_i, t_{i+1}]$  then equation (14) provides a simulation scheme that produces bias-free pricing of all bonds, in the sense that if we generate discrete paths of  $\{x(t_i), y(t_i)\}_{i=0,1,\dots}$  using equation (14) and use these

for producing bond prices, then for all  $n$ 

$$P(0, t_n) = \hat{E}[B(t_n)],$$
  

$$B(t_n) = \prod_{i=0}^{n-1} P(t_i, t_{i+1}; x(t_i), y(t_i)) \qquad (15)$$

where  $\hat{E}[\cdot]$  denotes the simulation mean. This is so because over each time step the scheme (14) is the exact simulation of a Gaussian model.

The pricing partial differential equation (PDE) associated with the model is

$$0 = \frac{\partial V}{\partial t} + D_x V + D_y V$$
  
$$D_x = -\frac{r}{2} + (-\kappa x + y)\frac{\partial}{\partial x} + \frac{1}{2}\eta^2 \frac{\partial^2}{\partial x^2}$$
  
$$D_y = -\frac{r}{2} + (\eta^2 - 2\kappa y)\frac{\partial}{\partial y}$$
 (16)

The absence of diffusion term in the second dimension can make the finite-difference solution of the PDE quite challenging, and this suggests the use of upwind and fully implicit schemes to prevent "ringing" in the numerical solution which would reduce the accuracy of the solution. Andreasen [1], however, reports good practical results with the  $O(\Delta t^2 + \Delta x^2 + \Delta y^4)$  accurate Mitchell scheme [9]

$$\begin{split} & \left[ \frac{1}{\Delta t} - \frac{1}{2} D_x \right] U(t) \\ & = \left[ \frac{1}{\Delta t} + \frac{1}{2} D_x + D_y \right] V(t + \Delta t) \\ & \left[ \frac{1}{\Delta t} - \frac{1}{2} D_y \right] V(t) \\ & = \frac{1}{\Delta t} U(t) - \frac{1}{2} D_y V(t + \Delta t) \end{split} \tag{17}$$

used with a standard 3-point discretization of  $D_x$ and a 5-point discretization of  $D_{\rm v}$ . The 5-point discretization in the second dimension eliminates the need for the use of upwind schemes at a slightly higher computational cost than would be the case for a standard 3-point scheme.

# **Multiple Factors**

The multifactor counterpart to equation  $(3)$  is

$$df(t,T) = \sigma(t,T) \cdot \left(\int_t^T \sigma(t,s) \, ds\right) dt$$
  
+  $\sigma(t,T) \cdot dW(t)$  (18)

where  $\{\sigma(t, T)\}_{t \leq T}$  is a family of *n*-dimensional vector processes,  $W$  is an  $n$ -dimensional vector Brownian motion, and  $\cdot$  denotes vector product. In the  $n$  factor separable volatility structure model, the forward rate volatility is given by

$$\sigma(t,T) = h(t)g(T) \tag{19}$$

where *g* is a deterministic vector function on  $\mathbb{R}^n_+$  and *h* is a matrix process on  $\mathbb{R}^{n \times n}$ . Defining

$$\kappa_i(t) = -\frac{g_i'(t)}{g_i(t)}\tag{20}$$

and

$$\eta_{ij}(t) = g_i(t)h_{ij}(t) \tag{21}$$

the separable volatility model can be written as follows [5]:

So we have a Markov representation involving  $n + n(n + 1)/2$  state variables with  $x = (x_i)$  being a vector of stochastic yield curve factors and the symmetric matrix  $y = (y_{ij})$  being a locally deterministic convexity term that has to be pulled along in simulation of the model to keep the model arbitragefree.

The number of state variables grows at a quadratic rate and this prevents the use of finite-difference methods for  $n > 1$ . There are, however, very significant computational savings associated with using this type of model rather than a general HJM (see Heath-Jarrow-Morton Approach) or LIBOR market model (see **LIBOR Market Model**) approach even though Monte Carlo simulations have to be used for the numerical solution. For the case of  $n = 4$  driving Brownian motions the number of state variables is 14, which should be compared against the 120 state variables of a 30-year quarterly Libor market model.

If we let the mean-reversion parameters,  $\kappa_1, \ldots, \kappa_n$ be constant, then

$$\sigma_j(t, t+\tau) = \sum_{i=1}^n e^{-\kappa_i \tau} \eta_{ij}(t) \to \int e^{-\kappa \tau} \eta_{\kappa j}(t) \, d\kappa \tag{23}$$

for  $n \to \infty$  and an appropriately chosen sequence  $\kappa_1, \kappa_2, \ldots$  So model (22) can be seen as a representation of the forward rate volatility structure on a (discrete) basis of exponential functions. The function  $\kappa \mapsto \eta_{j\kappa}(t)$  can thus be viewed as the inverse Laplace transform of the  $j$ th component of the forward rate volatility structure in the tenor dimension:  $\tau \mapsto \sigma_i(t, t+\tau).$ 

$$P(t,T) = \frac{P(0,T)}{P(0,t)} e^{-\sum_{i=1}^{n} G_i(t,T)x_i(t) - \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} G_i(t,T)y_{ij}(t)G_j(t,T)}$$
$$dx_i(t) = (-\kappa_i(t)x_i(t) + \sum_{j=1}^{n} y_{ij}(t)) dt + \sum_{j=1}^{n} \eta_{ij}(t) dW_j(t)$$
$$dy_{ij}(t) = \left(\sum_{k=1}^{n} \eta_{ik}(t)\eta_{jk}(t) - (\kappa_i(t) + \kappa_j(t))y_{ij}(t)\right) dt$$
$$G_i(t,T) = \int_t^T e^{-\int_t^s \kappa_i(u) du} ds$$
(22)

$$dF(t) = \Sigma(t) dW(t) + O(dt)$$

$$\Sigma(t) = \begin{bmatrix} \sigma_1(t, t + \tau_1) & \dots & \sigma_n(t, t + \tau_1) \\ \vdots & \ddots & \vdots \\ \sigma_1(t, t + \tau_n) & \dots & \sigma_n(t, t + \tau_n) \end{bmatrix}$$
(24)

In model  $(22)$  we have

$$dF(t) = \Gamma(t)\eta(t) dW(t) + O(dt)$$
  

$$\Gamma(t) = \begin{bmatrix} g_1(t, t + \tau_1) & \dots & g_n(t, t + \tau_1) \\ \vdots & \ddots & \vdots \\ g_1(t, t + \tau_n) & \dots & g_n(t, t + \tau_n) \end{bmatrix}$$
  

$$g_i(t, T) = e^{-\int_t^T \kappa_i(u) du}$$
 (25)

If we equate the diffusion terms in equations  $(24)$ and  $(25)$  we get

$$\eta(t) = \Gamma(t)^{-1} \Sigma(t) \tag{26}$$

So for this choice, models  $(22)$  and  $(24)$  exactly match on the dynamics of the selected forward rates. Andreasen [2] uses this technique to construct a separable volatility structure model that mimics the dynamics of a Libor market model with ratedependent and stochastic volatility, and it is shown that a four-factor version of such a model is capable of fitting the full cap and swaption market for all expiries and tenors and strikes within quite narrow tolerances

# **End Notes**

<sup>a.</sup>This volatility specification is suggested in [11]. In [1] it is suggested to model volatility to have dependencies of longer tenor rates.

#### References

- [1] Andreasen, J. (2000). Turbo-Charging the Cheyette Model. Working paper, General Re Financial Products.
- [2] Andreasen, J. (2005). Back to the future, *Risk* September,  $43-48$ .

- Babbs, S. (1990). The Term Structure of Interest Rates: [3] Stochastic Processes and Continent Claims. PhD thesis, Imperial College, London.
- [4] Babbs, S. (1993). Generalised Vasicek Models of the term structure, Applied Stochastic Models and Data Analysis 1, 49-62.
- [5] Cheyette, O. (1992). Markov Representation of the Heath-Jarrow-Morton Model. Working paper, BARRA.
- [6] Duffie, D. & Kan, R. (1996). A yield-factor model of interest rates, *Mathematical Finance* **6**, 379–406.
- Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing [7] and the term structure of interest rates: a new methodology for contingent claims valuation. *Econometrica* **60**. 77-106.
- [8] Jamshidian, F. (1991). Bond and option evaluation in the Gaussian interest rate model, *Research in Finance* **9**.  $131 - 710$
- [9] Mitchell, A. & Griffiths, D. (eds) (1980). The Finite Difference Method in Partial Differential Equations, John Wiley & Sons, New York.
- [10] Piterbarg, V. Time to smile, (2005). *Risk* May, 52–56.
- [11] Ritchken, P. & Sankarasubramaniam, L. (1993). On Finite State Markovian Representations of the Term Structure. Working paper, Department of Finance, University of Southern California.
- [12] Vasicek, O. (1977). An equilibrium characterization of the term structure, Journal of Financial Economics 5,  $177 - 188$ .

## **Further Reading**

- Andersen, L. & Andreasen, J. (2002). Volatile volatilities, Risk December, 163-168.
- Bjork, T. & Landen, C. (2001). A geometric view of interest rate theory, in Option Pricing, Interest Rates and Risk Management, E. Jouini, J. Cvitanic & M. Musiela, eds, Cambridge University Press, pp. 241–277.
- Cox, J., Ingersoll, J. & Ross, S. (1985). A theory of the term structure of interest rates, *Econometrica* 53, 385-408.
- Filipovic, D. (2001). Consistency Problems for Heath-Jarrow-Morton Interest Rate Models (Lecture Notes in Mathematics 1760), Springer-Verlag.

# **Related Articles**

Affine Models; Finite Difference Methods for Barrier Options; Gaussian Interest-Rate Models; Heath-Jarrow-Morton Approach; Markov Processes; Partial Differential Equations; Quadratic Gaussian Models.

JESPER ANDREASEN
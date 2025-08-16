# **Moment Explosions**

Let  $(S_t, V_t)_{t>0}$  be a Markov process, representing a (not necessarily purely continuous) stochastic volatility model.  $(S_t)_{t>0}$  is the (discounted) price of a traded asset, such as a stock, and  $(V_t)_{t>0}$  represents a latent factor, such as stochastic volatility, stochastic variance, or the stochastic arrival rate of jumps. A moment explosion takes place, if the moment  $\mathbb{E}[S^u]$  of some given order  $u \in \mathbb{R}$  becomes infinite ("explodes") after some finite time  $T_*(u)$ . This time is called the *time of moment explosion* and formally defined by

$$T_*(u) = \sup \left\{ t \ge 0 : \mathbb{E}[S_t^u] < \infty \right\} \tag{1}$$

We say that no moment explosion takes place for some given order  $u$ , if  $T_*(u) = \infty$ .

Moment explosions can be considered both under the physical and the pricing measure, with most applications belonging to the latter. If  $(S_t)_{t>0}$  is a martingale, then Jensen's inequality implies that moment explosions can only occur for moments of order  $u \in \mathbb{R} \setminus [0, 1]$ .

Conceptually, the notion of a moment explosion has to be distinguished from an explosion of the process itself, which refers to the situation that the process  $(S_t)_{t\geq 0}$ , not one of its moments, becomes infinite with some positive probability.

### Applications

In *equity* and *foreign exchange* models, where  $(S_t)_{t>0}$ represents a stock price or an exchange rate, moment explosions are closely related to the shape of the implied volatility surface, and can be used to obtain approximations for the implied volatility of deep in-the-money and out-of-the-money options (see Implied Volatility: Large Strike Asymptotics, and the references therein). According to [5, 14], the asymptotic shape of the implied volatility surface for some fixed maturity  $T$  is determined by the smallest and largest moment of  $S_T$  that is still finite. These critical moments  $u_{-}(T)$  and  $u_{+}(T)$  are the piecewise inverse functions<sup>a</sup> of the moment explosion time. Often the explosion time is easier to calculate, so a feasible approach is to first calculate explosion times, and then to invert to obtain the critical moments. Let us note that finite critical moments of the underlying  $S_T$  correspond, in essence, to exponential tails of  $\log(S_T)$ . There is evidence that refined knowledge of how moment explosion occurs (or the asymptotic behavior of  $u \mapsto \mathbb{E}\left[S_T^u\right]$  in the case of nonexplosion) can lead to refined results about implied volatility, see [6, 11] for some examples of stochastic alpha beta rho (SABR) type.

In *fixed-income* markets  $(S_t)_{t>0}$  might represent a forward LIBOR rate or swap rate. Andersen and Piterbarg [2] give examples of derivatives with superlinear payoff, whose pricing involves calculation of the second moment of  $S_T$ . It is clear that an explosion of the second moment will lead to infinite prices of such derivatives.

For numerical procedures, such as discretization schemes for stochastic differential equations (SDEs), error estimates that depend on higher order moments of the approximated process may break down if moment explosions occur [1]. Moment explosions may also lead to *infinite expected utility* in utility maximization problems [12].

# **Moment Explosions in the Black–Scholes** and Exponential Lévy Models

In the Black-Scholes model, moment explosions never occur, since moments of all orders exist for all times. In an exponential Lévy model (see **Exponential Lévy Models**),  $S_t$  is given by  $S_t =$  $S_0 \exp(X_t)$ , where  $X_t$  is a Lévy process. It holds that  $\mathbb{E}\left[S_t^u\right] = e^{t\kappa(u)}$ , where  $\kappa(u)$  is the cumulantgenerating function (cgf) of  $X_1$ . Thus in an exponential Lévy model, the time of moment explosion is given by

$$T_*(u) = \begin{cases} +\infty & \kappa(u) < \infty \\ 0 & \kappa(u) = \infty \end{cases} \tag{2}$$

Let us remark that, from Theorem 25.3 in [16],  $\kappa(u) < \infty \text{ iff } \int e^{ux} 1_{|x|>1} \nu(dx) < \infty \text{ where } \nu(dx)$ denotes the Lévy measure of  $X$ .

### **Moment Explosions in the Heston Model**

The situation becomes more interesting in a stochastic volatility model, like the Heston model (see Heston Model):

$$\begin{aligned} \mathrm{d}S_t &= S_t \sqrt{V_t} \, \mathrm{d}W_t^1, \quad S_0 = s \\ \mathrm{d}V_t &= -\lambda (V_t - \theta) \, \mathrm{d}t + \eta \sqrt{V_t} \, \mathrm{d}W_t^2, \\ V_0 &= v, \quad \langle \mathrm{d}W_t^1, \, \mathrm{d}W_t^2 \rangle = \rho \, \mathrm{d}t \end{aligned} \tag{3}$$

We now discuss how to compute the moments of  $S_t$  (equivalently, the moment-generating function of  $X_t = \log S_t / S_0$ ). The joint process  $(X_t, V_t)_{t>0}$  is a (time-homogenous) diffusion, started at  $(0, v)$ , with generator

$$\mathcal{L} = \frac{v}{2} \left( \frac{\partial^2}{\partial x^2} - \frac{\partial}{\partial x} \right) + \frac{v}{2} \eta^2 \frac{\partial^2}{\partial v^2}$$
$$+ \lambda (\theta - v) \frac{\partial}{\partial v} + \rho \eta v \frac{\partial^2}{\partial x \partial v} \tag{4}$$

Note that  $(X_t, V_t)_{t>0}$  has affine structure in the sense that the coefficients of  $\mathcal{L}$  are affine linear in the state variables.<sup>b</sup>

Now

$$\mathbb{E}\left[e^{uX_T}|X_t = x, V_t = v\right]$$
  
=  $e^{ux}\mathbb{E}\left[e^{uX_T}|X_t = 0, V_t = v\right]$  (5)

we see that  $f$  satisfies a parabolic partial differential equation (PDE).

$$\partial_t f = \mathcal{A}f := \left(\frac{v}{2}\eta^2 \frac{\partial^2}{\partial v^2} + \left[\lambda(\theta - v) + \rho \eta u v\right] \frac{\partial}{\partial v} + \frac{v}{2} \left(u^2 - u\right)\right) f \tag{7}$$

with initial condition  $f(0, \cdot; u) = 1$ , in which (again) all coefficients depend in an affine-linear way on  $v$ . The exponentially affine ansatz  $f(t, v; u) =$  $\exp(\phi(t, u) + v\psi(t, u))$  then immediately reduces this PDE to a system of ordinary differential equations (ODEs) for  $\phi(t, u)$  and  $\psi(t, u)$ :

$$\frac{\partial}{\partial t}\phi(t,u) = F(u,\psi(t,u)), \qquad \phi(0,u) = 0 \quad (8)$$
  
$$\frac{\partial}{\partial t}\psi(t,u) = R(u,\psi(t,u)), \qquad \psi(0,u) = 0 \quad (9)$$

where  $F(u, w) = \lambda \theta w$  and  $R(u, w) = \frac{w^2}{2} \eta^2 +$  $(\rho \eta u - \lambda)w + \frac{1}{2}(u^2 - u)$ . Equation (9) is a Riccati differential equation, whose solution blows up at finite time, corresponding to the moment explosion of  $S_t$ . Explicit calculations ([2], for instance) yield<sup>c</sup>

$$T_{*}^{\text{Heston}}(u) = \begin{cases} +\infty & \text{if } \Delta(u) \ge 0, \chi(u) < 0\\ \frac{1}{\sqrt{\Delta(u)}} \log\left(\frac{\chi(u) + \sqrt{\Delta(u)}}{\chi(u) - \sqrt{\Delta(u)}}\right) & \text{if } \Delta(u) \ge 0, \chi(u) > 0\\ \frac{2}{\sqrt{-\Delta(u)}} \left(\arctan\frac{\sqrt{-\Delta(u)}}{\chi(u)} + \pi \mathbf{1}_{\{\chi(u) < 0\}}\right) & \text{if } \Delta(u) < 0 \end{cases} \tag{10}$$

satisfies, as a function of  $(t, x, v)$ , the backward equation  $\partial_t + \mathcal{L} = 0$  with terminal data  $e^{ux}$  and after replacing  $T - t$  with t we can rewrite this as an initial value problem. Indeed, setting  $f = f(t, v; u) :=$  $\mathbb{E}\left[e^{uX_t}|X_0=0,V_0=v\right]$ , and noting that

$$\left(\frac{\partial^2}{\partial x^2} - \frac{\partial}{\partial x}\right) \left(e^{ux} f\right) = e^{ux} \left(u^2 - u\right) f \text{ and}$$
$$\frac{\partial^2}{\partial x \partial v} \left(e^{ux} f\right) = e^{ux} u \frac{\partial}{\partial v} f \tag{6}$$

where  $\chi(u) = \rho \eta u - \lambda$  and  $\Delta(u) = \chi(u)^2 - \eta^2(u^2 - \lambda)$  $u$ ). A simple analysis of this condition (cf. [2]) then allows to express the no-explosion condition in terms of the correlation parameter  $\rho$ . With focus on positive moments of the underlying,  $u \ge 1$ , we have

$$T_*^{\text{Heston}}(u) = +\infty \Longleftrightarrow \rho \le -\sqrt{\frac{u-1}{u}} + \frac{\lambda}{\eta u} \tag{11}$$

Similar results for a class of nonaffine stochastic volatility models is discussed below.

# Moment Explosions in Time-changed **Exponential Lévy Models**

Stochastic volatility can also be introduced in the sense of running time at a stochastic "business" clock. For instance, when  $\rho = 0$  the (log-price) in the Heston model is a Brownian motion with drift.  $W_t - t/2$ , run at a Cox-Ingersoll-Ross<sup>d</sup> (CIR) clock  $\tau(t,\omega) = \tau_t$  where

$$dV_t = -\lambda(V_t - \theta) dt + \eta \sqrt{V_t} dW_t, \quad V_0 = v$$
(12)

$$\mathrm{d}\tau_t = V \,\mathrm{d}t, \quad \tau_0 = 0 \tag{13}$$

Since  $(V, \tau)$  has an affine structure, there is a tractable moment-generating/characteristic function in the form

$$\mathbb{E} \left( \exp \left( u \tau_T \right) \right) = \mathbb{E} \left( \exp \left( u \int_0^T V \left( t, \omega \right) \, \mathrm{d}t \right) \right)$$
$$= \exp \left( A \left( u, T \right) + v B \left( u, T \right) \right) \tag{14}$$

where<sup>e</sup>

$$A(u,t) = \lambda^2 \theta t / \eta^2 - \frac{2\lambda\theta}{\eta^2} \log \left[ \sinh(\gamma t/2) \cdot \left( \coth(\gamma t/2) + \frac{\lambda}{\gamma} \right) \right]$$
(15)

$$B(u, t)$$
  
= 2u/(\lambda + \gamma \coth(\gamma t/2)), \qquad \gamma = \sqrt{\lambda^2 - 2\eta^2 u} (16)

We can replace  $W_t - t/2$  above by a general Lévy process  $L = L_t$  and run it again at some independent clock  $\tau = \tau (t, \omega)$ , assuming only knowledge of the cgf  $\kappa_T(u) = \log \mathbb{E} (\exp(u\tau_T))$ . If we also set  $\kappa_L(u) = \log \mathbb{E} \left[ \exp(uL_1) \right]$ , a simple conditioning argument shows that the moment-generating function of  $L_{\tau}$  is given by

$$M(u) = \mathbb{E}\left[\mathbb{E}\left(\mathrm{e}^{uL_{\tau}}|\tau\right)\right] = \mathbb{E}\left[\mathrm{e}^{\kappa_{L}(u)\tau}\right]$$
  
=  $\exp\left[\kappa_{\tau}(\kappa_{L}(u))\right]$  (17)

From here on, moment explosions of  $L_{\tau}$  can be investigated analytically, provided  $\kappa_{\tau}$ ,  $\kappa_{L}$  are known in sufficiently explicit form. For some computations in this context, also with regard to the asymptotic behavior of the implied volatility smile, see [5].

# **Moment Explosions in Non-affine Diffusion Models**

Both [2] and [15] study existence of  $u$ th moments,  $u \ge 1$ , for (not necessarily affine) diffusion models of the type

$$\begin{aligned} \mathrm{d}S_t &= V_t^\delta S_t^\beta \, \mathrm{d}W_t^1, & S_0 &= s \\ \mathrm{d}V_t &= \eta V_t^\gamma \, \mathrm{d}W_t^2 + b(V_t) \, \mathrm{d}t, \end{aligned} \tag{18}$$

$$V_0 = v, \quad \langle \mathbf{d}W_t^1, \mathbf{d}W_t^2 \rangle = \rho \,\mathbf{d}t \tag{19}$$

where  $\delta, \gamma > 0, \beta \in [0, 1]$  and the function  $b(v)$  are subject to suitable conditions that ensure a unique solution. For instance, the SABR model falls into this class. Lions and Musiela [15] first show that if  $\beta < 1$ , no moment explosions occur. For  $\beta = 1$ , the same reasoning as in the Heston model shows that  $f(t, v; u) = \mathbb{E}[(S_t/s)^u]$  satisfies the PDE<sup>f</sup>

$$\frac{\partial}{\partial t}f = \mathcal{A}f := \frac{v^{2\gamma}}{2}\eta^2\frac{\partial^2 f}{\partial v^2} + \left[b(v) + \eta\rho uv^{\delta+\gamma}\right]\frac{\partial f}{\partial v} + \frac{v^{2\delta}}{2}\left(u^2 - u\right)f\tag{20}$$

with initial condition  $f(0, \cdot; u) \equiv 1$ . Note that the Heston model is recovered as the special case  $\beta = 1, \delta = \gamma = 1/2, b(v) = -\lambda(v - \theta)$ . Using the (exponentially-affine in  $v^q$ ) ansatz  $f(t, v; u)$  $= \exp(\phi(t, u) + v^q \psi(t, u)),$  with suitably chosen q,  $\phi$ , and  $\psi$ , Lions and Musiela [15] construct supersolutions of equation  $(20)$ , leading to lower bounds for  $T_*(u)$ , and then subsolutions, leading to matching upper bounds.<sup>g</sup> We report the following results from [15]:

- 1.  $\beta < 1$ : no moment explosion occurs, that is,  $\mathbb{E}\left(S_t^u\right) < \infty \text{ for all } u \ge 1, t \ge 0;$
- 2.  $\beta = 1, \gamma + \delta < 1$ : as in 1. no moment explosion
- 3.  $\beta = 1, \gamma + \delta = 1$ : If  $\gamma = \delta = \frac{1}{2}$ , then this choice of parameters yields a Heston-type model, where

#### 4 **Moment Explosions**

the mean-reversion term  $-\lambda(V_t - \theta)dt$  has been replaced by the more general  $b(V_t) dt$ . With  $\lambda$ replaced by  $\lim_{v\to\infty} -b(v)/v$  the formula (10) remains valid. If  $\gamma \neq \delta$ , then the model can be transformed into a Heston-like model by the change of variables  $\widetilde{V}_t := V_t^{2\delta}$ . The time of moment explosion  $T_*(u)$  can be related to the expression in equation  $(10)$ , by

$$T_*(u) = \frac{1}{2\delta} T_*^{\text{Heston}}(u) \tag{21}$$

4.  $\beta = 1, \gamma + \delta > 1$ : Let  $b_{\infty} = \lim_{v \to \infty} b(v) / v^{\delta + \gamma}$ , and  $\rho^*(u) = -\sqrt{(u-1)/u} - b_{\infty}/(\eta u)$ , then

$$T_*(u) = \begin{cases} +\infty & \rho < \rho^*(u) \\ 0 & \rho > \rho^*(u) \end{cases} \tag{22}$$

The borderline case  $\rho = \rho^*(u)$  is delicate and we refer to  $[15, page 13]$ . Observe that, the condition on  $\rho < \rho^*(u)$  is consistent with the Heston model (11), upon setting  $\gamma = \delta = 1/2, b_{\infty} =$  $-\lambda$ , whereas the behavior of  $\rho > \rho^*(u)$  is different in the sense that there is no immediate moment explosion in the Heston model.

### **Moment Explosions in Affine Models** with Jumps

Recall that in the Heston model

$$\mathbb{E}\left[e^{uX_t}|X_0=x, V_0=v\right]$$
  
=  $e^{ux}\exp\left(\phi(t,u)+v\psi(t,u)\right)$  (23)

and it was this form of exponentially affine dependence on  $x, v$  that allowed an analytical treatment via Riccati equations. Assuming validity only of equation (23), for all  $u \in \mathbb{C}$  for which the expectation exists, and that  $(X_t, V_t)_{t\geq 0}$  is a (stochastically continuous, time-homogenous) Markov process on  $\mathbb{R} \times \mathbb{R}_{>0}$  puts us in the framework of affine processes [8], which, in fact, includes the bulk of analytically tractable stochastic volatility models with and without jumps.

The infinitesimal generator  $\mathcal{L}$  of the process  $(X_t, V_t)_{t>0}$  now includes integral terms corresponding to the jump effects and thus is a partial integrodifferential operator. Nevertheless, the exponentially

affine ansatz  $f(t, v; u) = \exp(\phi(t, u) + v\psi(t, u))$ still reduces the Kolmogorov equation to ordinary differential equations of the type equation  $(8)$ . The functions  $F(u, w)$  and  $R(u, w)$  are no longer quadratic polynomials, but of Lévy-Khintchine form (see Infi**nite Divisibility**). The time of moment explosion can be determined by calculating the blow-up time for the solutions of these *generalized* Riccati equations. This approach can be applied to a Heston model with an additional jump term:

$$dX_t = \left(c\left(V_t\right) - \frac{V_t}{2}\right) dt + \sqrt{V_t} dW_t^1 + dJ_t(V_t),$$
  
$$X_0 = 0 \tag{24}$$

$$\begin{aligned} \mathrm{d}V_t &= -\lambda(V_t - \theta)\,\mathrm{d}t + \eta\sqrt{V_t}\,\mathrm{d}W_t^2, \\ V_0 &= v, \quad \langle\,\mathrm{d}W_t^1,\,\mathrm{d}W_t^2\rangle = \rho\,\mathrm{d}t \end{aligned} \tag{25}$$

The process  $J_t(V_t)$  is a pure-jump process based on a fixed Lévy measure  $\nu(dx)$ . More precisely, writing  $\mu$  for the uncompensated and  $\hat{\mu}$  for the compensated Poisson random measure, independent of  $(W^1, W^2)$ , with intensity  $\nu(dx) \otimes dt$ , we assume that

$$\begin{split} \mathrm{d}J_{t}\left(V_{t}\right) &= \begin{cases} \int_{\left|x\right|<1} x\tilde{\mu}\left(\mathrm{d}x,\mathrm{d}t\right) & \dots \text{case (a)} \\ + \int_{\left|x\right|\geq 1} x\mu\left(\mathrm{d}x,\mathrm{d}t\right) & \dots \text{case (b)} \\\ \int_{\left|x\right|<1} V_{t} x\tilde{\mu}\left(\mathrm{d}x,\mathrm{d}t\right) & \dots \text{case (b)} \end{cases} \end{split} \tag{26}$$

In case (a), the process  $J_t$  is a genuine (purejump) Lévy process; in case (b) jumps are amplified linearly with the variance level, as proposed by Bates [4]. We focus first on case (a). Assuming  $\mathbb{E}\left[e^{J_t}\right] < \infty$ , or equivalently  $\int e^x 1_{|x|>1} \nu(dx) < \infty$ , so that  $e^{\tilde{J}_t} := e^{J_t + ct}$  is a martingale for suitable drift,  $c = -\log \mathbb{E}\left[e^{J_1}\right]$ , we have<sup>h</sup>

$$\mathbb{E}\left[e^{uX_{t}}\right] = \mathbb{E}\left[e^{uX_{t}^{\text{Heston}}}\right] \mathbb{E}\left[e^{u\tilde{J}_{t}}\right]$$
$$= \mathbb{E}\left[e^{uX_{t}^{\text{Heston}}}\right]e^{t\tilde{\kappa}(u)} \tag{27}$$

Here,  $\tilde{\kappa}(u) = \int (e^{ux} - 1 - u(e^x - 1)) v(dx)$  is well defined with values in  $(-\infty, \infty]$  and finiteness of  $\tilde{\kappa}(u) < \infty$  is tantamount to  $\int e^{ux} 1_{|x|>1} \nu(dx) < \infty$ . Hence in case (a), we can link the time of moment explosion  $T_*(u)$  to  $T_*^{\text{Heston}}(u)$ , given by equation (10), and have

$$T_*(u) = \begin{cases} T_*^{\text{Heston}}(u) & \tilde{\kappa}(u) < \infty \\ 0 & \tilde{\kappa}(u) = \infty \end{cases} \tag{28}$$

In the case (b), the jump process  $J_t(V_t)$  depends on  $V_t$  and the above argument cannot be used. A direct analysis of the (generalized) Riccati equations [13] shows that in the case  $\tilde{\kappa}(u) < \infty$  the time of moment explosion is given by formula (10), only now  $\Delta(u) = \chi(u)^2 - \eta^2 (2\tilde{\kappa}(u) + u^2 - u)$ , and immediate moment explosion happens in the case  $\tilde{\kappa}(u) = \infty.$ 

Also the model introduced by Barndorff-Nielsen and Shephard [3] (see Barndorff-Nielsen and Shephard (BNS) Models), which features simultaneous jumps in price and variance, falls into the class of affine models. It is given by

$$dX_t = \left(c - \frac{V_t}{2}\right) dt + \sqrt{V_t} dW_t + \rho dJ_{\lambda t}, \quad X_0 = 0$$

 $(29)$ 

$$dV_t = -\lambda V_t dt + dJ_{\lambda t}, \quad V_0 = v,$$
 (30)

where  $\lambda > 0$ ,  $\rho < 0$  and  $(J_t)_{t>0}$  is a pure-jump Lévy process with positive jumps only, and with Lévy measure  $\nu(\mathrm{d}x)$ . The drift parameter c is determined by the martingale condition for  $(S_t)_{t\geq 0}$ . The time of moment explosion can be calculated  $[13]$  and is given by

$$T_*(u) = -\frac{1}{\lambda} \log \max \left(0, 1 - \frac{2\lambda \max(0, \kappa_+ - \rho u)}{u(u - 1)}\right)$$
(31)

where  $\kappa_+ := \sup \{ u > 0 : \kappa(u) < \infty \}$  and  $\kappa(u) =$  $\int_0^\infty (e^{ux} - 1) \nu(dx) \in [0, \infty].$ 

# Moment Explosions in Affine Diffusion **Models of Dai–Singleton Type**

For affine diffusion models with an arbitrary number of stochastic factors, the analysis of moment explosions through the Riccati equations has been studied by Glasserman and Kim [10]. Without structural restrictions, this approach will lead to multiple coupled Riccati differential equations, whose blowup behavior is tedious to analyze in full generality. However, for concrete specifications, this approach can still lead to explicit results. Glasserman and Kim [10] consider affine models (see Affine Models), of Dai-Singleton type [7], which are given by a diffusion process

$$dY_t = -A^{\top}(\Theta - Y_t) dt + \sqrt{\text{diag}(b + B^{\top}Y_t)} dW_t$$
(32)

evolving on the state space  $\mathbb{R}_{>0}^m \times \mathbb{R}^{n-m}$ . The state vector  $Y$  is partitioned correspondingly, into components  $(Y^v, Y^d)$ , called *volatility factors* and *dependent factors.* The vector  $b \in \mathbb{R}^n$  and matrices  $A, B \in$  $\mathbb{R}^{n\times n}$  are subject to the following structural constraints:

- (C1)  $A = \begin{pmatrix} A^v & A^c \\ 0 & A^d \end{pmatrix}$ , with real and strictly negative eigenvalues.
- (C2) The off-diagonal entries of  $A^v$  are nonnegative.
- (C3) The vector  $\Theta = (\Theta^v, \Theta^d)$  has  $\Theta^d = 0, \Theta^v \ge$ 0, and  $(-A^{\top}\Theta)^{v} \gg 0$ .

(C4) 
$$B = \begin{pmatrix} I & B^c \\ 0 & 0 \end{pmatrix}$$
, and  $b = (b^v, b^d)$  with  $b^v = 0$   
and  $b^d = (1, \dots, 1)$ .

Note that condition C1 assumes strict mean reversion in all components, which is a typical assumption for interest rate models. Most equity pricing models, however, will not satisfy this condition in the strict sense: The Heston model, for example, is of the form  $(32)$ , but has an eigenvalue of 0 in the matrix A, and thus does not satisfy C1. Nevertheless, relaxing this condition is in general not a problem, see for example [9]. Glasserman and Kim [10] show that the moments of  $Y_t$  are represented by the *transform formula* 

$$\mathbb{E}[\exp(2u \cdot Y_t)] = \exp\left(-2\int_0^t \Theta^\top A x(s) \, \mathrm{d}s$$
$$+ 2\int_0^t |x^d(s)|^2 \, \mathrm{d}s + 2x(t) \cdot Y_0\right) \tag{33}$$

where  $x(t)$  is a solution to the coupled system of Riccati equations, given by

$$\begin{pmatrix} \dot{x}_1(t) \\ \vdots \\ \dot{x}_n(t) \end{pmatrix} = \begin{pmatrix} A^v & A^c \\ 0 & A^d \end{pmatrix} \cdot \begin{pmatrix} x_1(t) \\ \vdots \\ x_n(t) \end{pmatrix} \\
+ \begin{pmatrix} I & B^c \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} x_1^2(t) \\ \vdots \\ x_n^2(t) \end{pmatrix} \quad (34)$$

with initial condition  $x(0) = u$ . Equation (33) holds in the sense that if either side is well defined and finite, the other one is also finite, and equality holds. Thus, moment explosions can again be linked to the blow-up time of the ODE (34). [10] considers two concrete specifications of the above model, with one volatility factor and one dependent factor in each case. Owing to conditions  $C1-C4$ , the model parameters are of the form  $A = \begin{pmatrix} p & q \\ 0 & r \end{pmatrix}$ ,  $B =$  $\begin{pmatrix} 1 & s \\ 0 & 0 \end{pmatrix}$ , and  $\Theta = (\theta_1, 0)$ , with  $p < 0, q \ge 0, r < 0$ ,  $s \ge 0$ , and  $\theta_1 \ge 0$ .

 $q = s = 0$ : This specification decouples the system  $(34)$  fully, which can then easily be solved explicitly. In this case, the moment explosion time is given by

$$T_*(u_1, u_2) = \begin{cases} +\infty, & u_1 \le -p\\ \frac{1}{p} \log\left(1 + \frac{p}{u_1}\right), & u_1 > -p \end{cases}$$
(35)

Note that the moment explosion time does not depend on  $u_2$ .

 $s > 0$ ,  $q = 0$ ,  $r = p < 0$ : In this case, the system (34) decouples only partially; The equation for the second component becomes  $\dot{x}_2 =$ 

 $px_2$ , with the solution  $x_2(t) = u_2e^{pt}$ . Substituting into the equation for the first component yields  $\dot{x}_2(t) = px_1 + x_1^2 + su_2^2 e^{2pt}$ , a nonautonomous Riccati equation. After the transformation  $\xi(t) = e^{-pt}x(t)$  it can be solved explicitly, and the moment explosion time is determined as

$$T_*(u_1, u_2) = \frac{1}{p} \log \max \left\{ 0, \frac{p}{|u_2|\sqrt{s}} \operatorname{arccot} \left( \frac{u_1}{|u_2|\sqrt{s}} + 1 \right) \right\} \tag{36}$$

### **End Notes**

<sup>a.</sup>On the intervals  $(-\infty, 0)$  and  $(1, \infty)$ , respectively.

<sup>b.</sup>In fact, it does not even depend on  $x$ , which implies the homogeneity properties in equation  $(5)$ .

<sup>c</sup>. Only  $u \notin [0, 1]$  needs to be discussed; in this case,  $\chi(u) =$  $0 \Longrightarrow \Delta(u) < 0.$ 

<sup>d.</sup>When  $u=1$ , equation (14) is precisely the Cox-Ingersoll-Ross bond pricing formula.

<sup>e.</sup>For  $u < u^*$  since equation (14) explodes as  $u$  ↑  $u^*$ , where  $u^* > 0$  is determined by  $I(u^*) \equiv \lambda +$  $\gamma(u)\coth(\gamma(u)t/2) = 0.$ 

<sup>f</sup>Care is necessary since  $f$  can be  $+\infty$ ; see [15] for a proper discussion via localization.

<sup>g.</sup>A supersolution  $\overline{f}$  of equation (20) satisfies  $\mathcal{A}\overline{f} - \frac{\partial \overline{f}}{\partial t} \leq$ 

0, a subsolution  $\underline{f}$  satisfies  $A\underline{f} - \frac{\partial f}{\partial t} \ge 0$ .<br><sup>h.</sup>  $X_t^{\text{Reston}}$  denotes the usual log-price process in the classical Heston model, that is, with  $J \equiv 0$ .

<sup>i</sup>Following the notation of [7], " $\gg$ " denotes strict inequality, simultaneously in all components of the vectors.

### References

- Alfonsi, A. (2008). High Order Discretization Schemes [1] for the CIR Process: Application to Affine Term Structure and Heston Models. Preprint.
- Andersen, L.B.G. & Piterbarg, V.V. (2007). Moment [2] explosions in stochastic volatility models, Finance and Stochastics 11, 29-50.
- Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-[3] Gaussian Ornstein-Uhlenbeck-based models and some of their uses in financial economics, Journal of the Royal Statistical Society B 63, 167-241.
- [4] Bates, D.S. (2000). Post-'87 crash fears in the S&P 500 futures option market, Journal of Econometrics 94,  $181 - 238.$
- [5] Benaim, S. & Friz, P. (2008). Smile asymptotics ii: models with known moment generating functions, Journal of Applied Probability  $45(1)$ ,  $16-32$ .

- [6] Benaim, S., Friz, P. & Lee, R. (2008). The Black Scholes implied volatility at extreme strikes, in *Frontiers in Quantitative Finance: Volatility and Credit Risk Modeling*, R. Cont, ed, Wiley, Chapter 2.
- [7] Dai, Q. & Singleton, K.J. (2000). Specification analysis of affine term structure models, *The Journal of Finance* **55**, 1943–1977.
- [8] Duffie, D., Filipovic, D. & Schachermayer, W. (2003). Affine processes and applications in finance, *The Annals of Applied Probability* **13**(3), 984–1053.
- [9] Filipovic, D. & Mayerhofer, E. (2009). ´ *Affine Diffusion Processes: Theory and Applications*, Preprint, arXiv:0901.4003.
- [10] Glasserman, P. & Kim, K.-K. (2009). Moment explosions and stationary distributions in affine diffusion models, *Mathematical Finance*, Forthcoming, available at SSRN: http://ssrn.com/abstract=1280428.

- [11] Gulisashvili, A. & Stein, E. (2009). Implied volatility in the Hull-White model, *Mathematical Finance*, to appear.
- [12] Kallsen, J. & Muhle-Karbe, J. (2008). *Utility Maximization in Affine Stochastic Volatility Models*, Preprint.
- [13] Keller-Ressel, M. (2008). Moment explosions and long-term behavior of affine stochastic volatility models, arXiv:0802.1823, forthcoming. in *Mathematical Finance*.
- [14] Lee, R. (2004). The moment formula for implied volatility at extreme strikes, *Mathematical Finance* **14**(3), 469–480.
- [15] Lions, P.-L. & Musiela, M. (2007). Correlations and bounds for stochastic volatility models, *Annales de l'Institut Henri Poincar´e* **24**, 1–16.
- [16] Sato, K.-I. (1999). *L´evy Processes and Infinitely Divisible Distributions*, Cambridge University Press.

PETER K. FRIZ & MARTIN KELLER-RESSEL
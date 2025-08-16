# Implied Volatility: Volvol Expansion

In order to calibrate stochastic volatility models, it is convenient to have an accurate analytical formula or approximation for call options. However, deriving such a formula is not always an easy task. In the Heston model, the most popular technique involves numerical integration, which is necessarily time consuming. The main idea is to apply a perturbation method to the volvol parameter, calculating the first and second order of the difference between a stochastic volatility model and a Black-Scholes model. In general case, we can reduce the integration of the exact formula to some simpler integration.

Consider the following two-factor stochastic volatility model:

$$dS = (r - d)Sdt + \sigma SdB_t \tag{1}$$

$$dV = b(V)dt + \epsilon \nu(V)dW \qquad (2)$$

$$\mathrm{d}B\mathrm{d}W = \rho(V)\mathrm{d}t\tag{3}$$

where r is the short rate, d is the dividend yield,  $\epsilon$ is a constant, and  $b(V)$  and  $v(V)$  are independent of  $\epsilon$ . We assume parameters r and d to be constant for the sake of simplicity. The series expansion consists in writing the option price formula as a series in  $\epsilon$ .

Fourier methods (see Fourier Methods in Options Pricing) tell us that the call option price is given by

$$C(S, V, T) = Se^{-dT} - \frac{Ke^{-rT}}{2\pi} \int_{i/2-\infty}^{i/2+\infty} \exp(-\mathrm{i}uX) \frac{\Phi(u, V, T)}{u(u-i)} \mathrm{d}u \qquad (4)$$

where  $X = \ln(S/K) + (r - d)T$ .

$$\frac{\partial f}{\partial \tau} = \frac{1}{2} \epsilon^2 \nu^2(V) \frac{\partial^2 f}{\partial V^2} + \left[ b(V) - \mathrm{i} u \epsilon \rho(V) \nu(V) \sqrt{V} \right]$$

$$\times \frac{\partial f}{\partial V} - \frac{u(u-i)}{2} Vf \tag{5}$$

We look for solutions which can be written as a power series of  $\epsilon$ .

$$f(u, V, T) = f^{(0)}(u, V, T) + \epsilon f^{(1)}(u, V, T)$$
$$+ \epsilon^2 f^{(2)}(u, V, T) \tag{6}$$

Thus, we can obtain the power series of the call price using either equation  $(4)$  directly

$$C(u, V, T) = C^{(0)}(u, V, T) + \epsilon C^{(1)}(u, V, T)$$
$$+ \epsilon^{2} C^{(2)}(u, V, T) \tag{7}$$

or expanding first the implied volatility

$$V_{\text{imp}}(u, V, T) = V_{\text{imp}}^{(0)}(u, V, T) + \epsilon V_{\text{imp}}^{(1)}(u, V, T)$$
$$+ \epsilon^2 V_{\text{imp}}^{(2)}(u, V, T) \tag{8}$$

and then plugging it into the option price with Black-Scholes formula.

As a matter of fact, these two methods differ significantly. The former—denoted by series A in the remainder of this article-gives the call price first and implied volatility while the latter—denoted by series  $B$ —gives the implied volatility and call price is obtained afterward. Nevertheless, in most cases, there is a slight numerical difference between the two series. However, regarding far out-of-the money options, the two series give different results as shown in Figure 1. Empirical evidence shows that series  $B$  is very often better than series A. Even though this is not a general rule, series B should be usually preferred over series A.

We now explicitly compute the two series for the following model. In particular, this model encompasses the Heston model for the special case  $\phi = 0.5.$ 

$$dS = (r - d)Sdt + \sigma SdB_t \tag{9}$$

![](_page_1_Figure_1.jpeg)

**Figure 1** Series A (expansion on price), series B (expansion on implied volatility), and exact volatility

$$dV = (\omega - \theta V)dt + \epsilon V^{\phi}dW \qquad (10)$$

$$\mathrm{d}B\mathrm{d}W = \rho(V)\mathrm{d}t\tag{11}$$

First, the expansion is on the fundamental transform of the closed formula, which is presented by *(u, V , T )* in equation (4). The idea is that we can expand this function into a simpler form, so that the integration in the equation (4) can be reduced to analytic form. Here, we do not discuss the detailed derivation but only give the result. Interested readers can refer to [2]. For series A, the expansion on price is

$$\begin{split} C(S,V,\tau) &= c(S,v,\tau) + \epsilon \tau^{-1} J^{(1)} \tilde{R}^{(1,1)} c_V(S,v,\tau) \\ &+ \epsilon^2 \left\{ \tau^{-1} J^2 + \tau^{-2} J^{(3)} \tilde{R}^{(2,0)} \right. \\ &\left. + \tau^{-1} J^{(4)} \tilde{R}^{(1,2)} + \frac{\tau^{-2}}{2} (J^1)^2 \tilde{R}^{(2,2)} \right\} \\ &\times c_V(S,v,\tau) + O(\epsilon^3) \end{split} \tag{12}$$

For series B, the expansion on price is

$$V^{\text{imp}} = v(S, v, \tau) + \epsilon \tau^{-1} J^{(1)} \tilde{R}^{(1,1)}$$
$$+ \epsilon^{2} \left\{ \tau^{-1} J^{2} + \tau^{-2} J^{(3)} \tilde{R}^{(2,0)}$$
$$+ \tau^{-1} J^{(4)} \tilde{R}^{(1,2)} + \frac{\tau^{-2}}{2} (J^{(1)})^{2}$$
$$\times \left[ \tilde{R}^{(2,2)} - \left( \tilde{R}^{(1,1)} \right)^{2} \tilde{R}^{(2,0)} \right] \right\}$$
$$+ O(\epsilon^{3}) \tag{13}$$

In the above formulae, term *c(S, v, τ )* presents the corresponding Black–Scholes price. When volvol *-* = 0, the stochastic model reduces to a Black–Scholes model. *v* here is the equivalent variance for Black–Scholes, which is basically the integration of the variance from 0 to *τ* .

The functions  $\tilde{R}^{(p,q)}$  and  $J^{(s)}$  are the derivative ratios and integration, respectively. Here, for academic and practitioners' interest their expressions are listed.

$$\mathrm{d}v_t = \kappa (\theta_t - v_t) \mathrm{d}t + \xi_t \sqrt{v_t} \mathrm{d}B_t, \ v_0 \ (20)$$

$$\mathbf{d}\langle W,\,B\rangle_t = \rho_t \mathbf{d}t\tag{21}$$

$$\tilde{R}^{(2,0)} = \tau \left[ \frac{1}{2} \frac{X^2}{Y^2} - \frac{1}{2Z} - \frac{1}{8} \right], \quad \tilde{R}^{(1,1)} = \left[ -\frac{X}{Z} + \frac{1}{2} \right]\n$$

$$\n\tilde{R}^{(1,2)} = \left[ \frac{X^2}{Z^2} - \frac{X}{Z} - \frac{1}{4Z} (4 - Z) \right], \quad \tilde{R}^{(2,2)} = \tau \left[ \frac{1}{2\frac{X^4}{Z^4}} - \frac{1}{2} \frac{X^3}{Z^3} - 3\frac{X^2}{Z^3} + \frac{1}{8} \frac{X}{Z^2} (12 + Z) + \frac{1}{32} \frac{1}{Z^2} (48 - Z^2) \right]\n$$
(14)

with  $Z = V\tau$  and

Here, we have adjusted to risk neutral probability; as a consequence, it introduces the drift term in spot process by the change of probability.

$$J^{(1)}(V,\tau) = \frac{\rho}{\theta} \int_0^{\tau} \left(1 - e^{-\theta(\tau-s)}\right) \left[\frac{\omega}{\theta} + e^{-\theta s} \left(V - \frac{\omega}{\theta}\right)\right]^{\phi + \frac{1}{2}} \mathrm{d}s, \quad J^{(2)}(V,\tau) = 0 \tag{15}$$

$$J^{(3)}(V,\tau) = \frac{1}{2\theta^2} \int_0^\tau \left(1 - e^{-\theta(\tau - s)}\right)^2 \left[\frac{\omega}{\theta} + e^{-\theta s} \left(V - \frac{\omega}{\theta}\right)\right]^{2\phi} \mathrm{d}s \tag{16}$$

$$J^{(4)}(V,\tau) = \left(\phi + \frac{1}{2}\right) \int_0^\tau \left[\frac{\omega}{\theta} + e^{-\theta(\tau-s)} \left(V - \frac{\omega}{\theta}\right)\right]^{\phi + \frac{1}{2}} J^{(6)}(V,\tau) \mathrm{d}s \tag{17}$$

with 
$$J^{(6)}(V,\tau)ds = \int_0^\tau \left(e^{-\theta(\tau-s)} - e^{-\theta s}\right) \left[\frac{\omega}{\theta} + e^{-\theta(\tau-u)}\left(V - \frac{\omega}{\theta}\right)\right]^{\phi-\frac{1}{2}} du$$
 (18)

# **Example of Volvol Expansion: Heston** Model

We will now show the expansion of volvol for the Heston model (see Heston Model). By the asymptotic expansion, we can finally obtain an approximate analytic formula for the European call option. This work comes from the result of Benhamou et al. [1]. Consider a Heston model

$$\mathrm{d}X_t = \sqrt{v_t} \mathrm{d}W_t - \frac{v_t}{2} \mathrm{d}t, \ \ X_0 = x_0 \tag{19}$$

To expand the model, we add  $\epsilon$  in the model.

$$\mathrm{d}X_{t}^{\epsilon} = \sqrt{v_{t}^{\epsilon}} \mathrm{d}W_{t} - \frac{v_{t}^{\epsilon}}{2} \mathrm{d}t, \quad X_{0}^{\epsilon} = x_{0} \tag{22}$$

$$\mathrm{d}v_t^{\epsilon} = \kappa (\theta_t - v_t^{\epsilon}) \mathrm{d}t + \epsilon \xi_t \sqrt{v_t^{\epsilon} \mathrm{d}B_t}, \quad v_0^{\epsilon} = v_0 \tag{23}$$

Now, we will expand the European call option price formula with respect to  $\epsilon$ . Note that, when  $\epsilon = 0$ , we have a Black–Scholes model; while  $\epsilon = 1$ , we have a Heston model. We already have the closed formula of Black-Scholes for  $\epsilon = 0$ . We expand at  $\epsilon = 0$ , and let  $\epsilon = 1$  to obtain the approximate formula. In mathematical language, this can be written as follows:

$$P_{\text{Heston}} = P_{\text{BS}} + \mathbb{E}\left[\frac{\partial P_{\text{BS}}}{\partial \epsilon}\right] + \frac{1}{2}\mathbb{E}\left[\frac{\partial^2 P_{\text{BS}}}{\partial \epsilon^2}\right] + \mathcal{E}$$
(24)

Here, we will take another approximation to simulate the partial derivatives in the above equation by the linear combination of the Greek letters of Black-Scholes. Here, the idea is that use of the chain rule in the derivative can result in  $\frac{\partial P_{\text{BS}}}{\partial \epsilon}$  =  $\frac{\partial P_{\text{BS}}}{\partial S}\frac{\partial S}{\partial \epsilon} + \frac{\partial P_{\text{BS}}}{\partial \sigma}\frac{\partial \sigma}{\partial \epsilon}$ . The same idea holds for the second derivative.

$$P_{\text{Heston}} = P_{\text{BS}}(x_0, \text{var}_T) + \sum_{i=1}^{2} a_{i,T} \frac{\partial^{i+1} P_{\text{BS}}}{\partial x^i y}(x_0, \text{var}_T)$$
$$+ \sum_{i=0}^{1} b_{2i,T} \frac{\partial^{2i+2} P_{\text{BS}}}{\partial x^{2i} y^2}(x_0, \text{var}_T) + \mathcal{E} \qquad (25)$$

We refer to [1] for proofs and intermediate derivation. The parameters in the formula are as follows:

$$\begin{aligned} \text{var}_T &= m_0 v_0 + m_1 \theta, \quad a_{1,T} = \rho \xi (p_0 v_0 + p_1 \theta) \\ a_{2,T} &= (\rho \xi)^2 (q_0 v_0 + q_1 \theta), \quad b_{0,T} = \xi^2 (r_0 v_0 + r_1 \theta) \end{aligned}$$

 $(26)$ 

$$\text{var}_T = \int_0^T v_{0,t} \text{d}t \tag{27}$$

$$m_0 = \frac{e^{-\kappa T} \left(-1 + e^{\kappa T}\right)}{\kappa},$$
  

$$m_1 = T - \frac{e^{-\kappa T} \left(-1 + e^{\kappa T}\right)}{\kappa},$$
  

$$p_0 = \frac{e^{-\kappa T} \left(-\kappa T + e^{\kappa T} - 1\right)}{\kappa^2},$$
  

$$p_1 = \frac{e^{-\kappa T} \left(\kappa T + e^{\kappa T} (\kappa T - 2) + 2\right)}{\kappa^2},$$

$$q_{0} = \frac{e^{-\kappa T} \left(-\kappa T (\kappa T + 2) + 2e^{\kappa T} - 2\right)}{2\kappa^{3}},$$

$$q_{1} = \frac{e^{-\kappa T} \left(2e^{\kappa T} (\kappa T - 3) + \kappa T (\kappa T + 4) + 6\right)}{2\kappa^{3}},$$

$$r_{0} = \frac{e^{-2\kappa T} \left(-4e^{\kappa T} \kappa T + 2e^{2\kappa T} - 2\right)}{4\kappa^{3}},$$

$$r_{1} = \frac{e^{-2\kappa T} \left(4e^{\kappa T} (\kappa T + 1) + e^{2\kappa T} (2\kappa T - 5) + 1\right)}{4\kappa^{3}}$$

$$(28)$$

The advantage is that there is no integration in the approximate formula. So the calculations are done much faster than in the exact formula. We will discuss this point in the section Numerical Results.

The error in the approximation is estimated as  $\mathcal{E} = O\left([\xi_{\text{Sup}}\sqrt{T}]^3\sqrt{T}\right).$ 

### **Numerical Results**

We test the approximate formula with the following strikes. We take strikes from 70% to 130% for short maturity and 10% to 730% for long maturity. Implied Black-Scholes volatilities of the closed formula, of the approximation formula, and related errors (in bp), are expressed as a function of maturities in fractions of years and relative strikes. The values of the parameters are as follows:  $\theta = 6\%$ ,  $\kappa = 3, \xi = 30\%$ , and  $\rho = 0\%$ . Except for short maturity plus very small strikes, where we observe the largest difference  $(18.01 \text{ bp})$ ; the difference is less than 5 bp (1 bp =  $0.01\%$ ) in almost all other cases. With regard to the speed of calculation, the approximate formula is about 100 times quicker than the exact formula (with the optimization in integral).

#### References

- [1] Benhamou, E., Gobet, E. & Miri, M. (2009). Time dependent Heston model, SIAM Journal on Financial Mathematics.
- [2] Lewis, A.L. (2000). Option Valuation Under Stochastic Volatility: With Mathematica Code. February 2000.

## **Related Articles**

**Heavy Tails**; **Heston Model**; **Hull–White Stochastic Volatility Model**; **Implied Volatility in Stochastic Volatility Models**; **Implied Volatility Surface**; **Model Calibration**; **Partial Differential Equations**; **SABR Model**; **Stochastic Volatility Models**; **Stylized Properties of Asset Returns**.

ZAIZHI WANG & MOHAMMED MIRI
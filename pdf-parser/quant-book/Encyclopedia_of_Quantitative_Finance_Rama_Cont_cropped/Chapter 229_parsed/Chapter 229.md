# Cox-Ingersoll-Ross (CIR) Model

The Cox-Ingersoll-Ross (CIR) model, one of the most well-known short-rate models (see Term **Structure Models**), was proposed in 1985 by Cox, Ingersoll, and Ross (see Ross, Stephen). In their pioneering work [3], they use an equilibrium approach to derive an explicit formula for the interest rate as a function of the wealth and the state of technology. On the basis of economic arguments, they specify their general framework in [4] and obtain the following dynamics for the short rate  $(r_t, t > 0)$ under the objective probability measure  $\mathbb{P}^o$  with a risk premium factor  $\Lambda$ :

$$t \ge 0, \, \mathrm{d}r_t = \left[\kappa\theta - (\kappa + \Lambda)r_t\right] \mathrm{d}t + \sigma\sqrt{r_t} \,\mathrm{d}W_t^o \quad (1)$$

Here, the process  $(W_t^o, t \ge 0)$  is a standard Brownian motion, and the real parameters  $\kappa, \theta, \sigma$  satisfy  $\kappa \theta \ge 0$ and  $\sigma > 0$ . To deal with pricing, we, however, consider in the sequel the dynamics under the risk-neutral measure  $\mathbb{P}$  (see **Hedging**). The usual assumption is to take a risk premia function equal to  $\Lambda \sqrt{r}/\sigma$  (see Risk Premia). This choice allows to keep a similar dynamics under  $\mathbb{P}$ :

$$t \ge 0, \, \mathrm{d}r_t = \kappa (\theta - r_t) \, \mathrm{d}t + \sigma \sqrt{r_t} \, \mathrm{d}W_t \qquad (2)$$

 $W_t = W_t^o - \int_0^t (\Lambda \sqrt{r_s}/\sigma) \, ds$  being a Brownian motion under  $\mathbb{P}$ . Indeed, using  $\int_0^t \sqrt{r_s} \, \mathrm{d}W_s^o =$  $[r_t - r_0 - \kappa \theta t + \int_0^t (\kappa + \Lambda) r_s \, ds] / \sigma$ , we can check from equation (3) that  $\mathbb{E}^o[\exp[\int_0^t (\Lambda \sqrt{r_s}/\sigma) \, \mathrm{d}W_s^o \frac{1}{2}\int_0^t (\Lambda/\sigma)^2 r_s \, ds = 1$ , so  $\mathbb{P}$  is indeed equivalent to  $\mathbb{P}^o$ . The parameters have a clear interpretation. First,  $\sigma$  determines the volatility of the interest rate. Moreover, for the common practical choice  $\kappa, \theta > 0$  that we assume in the following, the short rate has a mean reversion toward  $\theta$  with a speed driven by  $\kappa$ . It is known that equation  $(2)$  has a (pathwise) unique nonnegative solution for any starting value  $r_0 \geq 0$ . Furthermore, the short rate remains positive at any time as long as  $r_0 > 0$  and  $2\kappa \theta \geq \sigma^2$ . Nonnegativity is, of course, a nice feature when modeling interest rates. This is the main qualitative difference between CIR and Vasicek models (see Term Structure Models) that have otherwise similar properties for pricing derivatives.

#### **Analytical Results**

Beyond the natural meaning of its parameters, the CIR model strength is to provide analytical formulas for the main financial quantities. It belongs to the class of affine models (see Affine Models), which means that the Laplace transform of the joint distribution  $(r_t, \int_0^t r_s \, ds)$  is known to be for  $\lambda, \mu > 0$ ,

$$\mathbb{E}\left[e^{-\lambda r_t - \mu \int_0^t r_s \mathrm{d}s}\right] = A_{\lambda,\mu}(t) \exp(-r_0 B_{\lambda,\mu}(t)) \quad (3)$$

We have the following formulas (see  $[10]$ ):

$$A_{\lambda,\mu}(t) = \left[ \frac{2\gamma_{\mu}e^{t\frac{\gamma_{\mu}+\kappa}{2}}}{\{\sigma^{2}\lambda(e^{\gamma_{\mu}t}-1)+\gamma_{\mu}}\} \right]^{\frac{2\kappa\theta}{\sigma^{2}}},$$
$$B_{\lambda,\mu}(t) = \frac{\lambda[\gamma_{\mu}+\kappa+e^{\gamma_{\mu}t}(\gamma_{\mu}+\kappa)]}{\sigma^{2}\lambda(e^{\gamma_{\mu}t}-1)+\gamma_{\mu}-\kappa+e^{\gamma_{\mu}t}(\gamma_{\mu}+\kappa)}$$
(4)

with  $\gamma_{\mu} = \sqrt{\kappa^2 + 2\sigma^2\mu}$ . An analogous formula to equation (3) holds for the Fourier transform, handling complex logarithms with care, and even for a wider range of complex values of  $\lambda$  and  $\mu$  as long as the left-hand side is well defined. Thanks to equation (3), the law of  $r_t$  is known. Defining  $c_t = \frac{4\kappa}{\sigma^2(1-\mathbf{e}^{-\kappa t})}$ ,  $c_t r_t$ is distributed as a chi-square distribution with  $v =$  $\frac{4\kappa\theta}{\sigma^2}$  degrees of freedom and noncentrality parameter  $d_t = c_t r_0 e^{-\kappa t}$  More explicitly, this means that  $r_t$ has the following density function for  $r > 0$ ,

$$\sum_{i=0}^{\infty} \frac{\mathrm{e}^{-\frac{d_{t}}{2}} \left(\frac{d_{t}}{2}\right)^{i}}{i!} \frac{c_{t}/2}{\Gamma\left(i+\frac{\nu}{2}\right)} \left(\frac{c_{t}r}{2}\right)^{i-1+\frac{\nu}{2}} \mathrm{e}^{-\frac{c_{t}r}{2}} \quad (5)$$

In particular, one can see that  $r_t$  converges to a steady-state distribution with density  $\frac{(c_{\infty}/2)^{\frac{\nu}{2}}}{\Gamma(\frac{\nu}{2})}r^{\frac{\nu}{2}-1}$  $e^{-\frac{c_{\infty}}{2}r}$  where  $c_{\infty} = 4\kappa/\sigma^2$  when  $t \to +\infty$ . This is a Gamma distribution with mean  $\theta$  and variance

 $\theta \sigma^2/(2\kappa)$ . It is the stationary law of the stochastic differential equation (2).

#### **Derivative Pricing**

Under a short-rate model, the initial price of a zerocoupon bond with maturity  $T > 0$  (see definition in **Bond**) is given by  $\mathbb{E}[\mathrm{e}^{-\int_0^T r_s ds}]$ . It is here analytically known and is equal to  $A_{0,1}(T) \exp(-r_0 B_{0,1}(T)).$ More generally, the price at time  $t > 0$  of a zerocoupon bond with maturity  $T$  is given by

$$P(r_t, t, T) = A_{0,1}(T - t) \exp(-r_t B_{0,1}(T - t)) \quad (6)$$

The CIR model also provides closed form formulas for some option prices. For instance, let us consider a call option with strike  $K$  and maturity  $T$ , written on a zero-coupon bond with maturity  $S \geq T$ . Its initial price is given by

$$\mathbf{C} = \mathbb{E}[\mathrm{e}^{-\int_{0}^{T} r_{s} ds} (P(r_{T}, T, S) - K)^{+}] \qquad (7)$$

To calculate  $C$ , we use another nice feature of the CIR model: the short-rate distribution is known under the forward measure. Let us recall that for a fixed maturity  $T > 0$ , the *T*-forward measure is defined by

$$\mathbb{P}^{T}(A) = \frac{\mathbb{E}\left[e^{-\int_{0}^{T} r_{s} \mathrm{d}s} \mathbf{1}_{A}\right]}{P(r_{0}, 0, T)} \tag{8}$$

for any event  $A$  anterior to time  $T$  (see Forward and Swap Measures), which amounts to taking the zerocoupon bond as a numeraire. Under  $\mathbb{P}^T$ ,  $(r_t, 0 \le t \le t)$  $T$ ) solves the following SDE

$$dr_t = [\kappa \theta - (\kappa + \sigma^2 B_{0,1}(T-t))r_t] dt + \sigma \sqrt{r_t} dW_t^T$$
(9)

where  $(W_t^T, 0 \le t \le T)$  is a Brownian motion under  $\mathbb{P}^T$ . This diffusion is again of the affine type and is tractable. In particular, for  $t \in [0, T]$ , the law of  $r_t$  under  $\mathbb{P}^T$  is known: it is distributed as  $1/(2\alpha_T(t))$  times a chi-square random variable with  $\nu$  degrees of freedom and noncentrality parameter  $\frac{8r_0\gamma_1^2e^{\gamma_1t}}{\sigma^4(e^{\gamma_1t}-1)^2\alpha_T(t)}$ , where  $\alpha_T(t) = \frac{2\gamma_1}{\sigma^2(e^{\gamma_1t}-1)} +$ 

 $\frac{\kappa + \gamma_1}{\sigma^2} + B_{0,1}(T - t)$  (see [2, 4, 8]). Then, from equations  $(6 \text{ and } 7)$ , we easily get the call price

$$\mathbf{C} = P(r_0, 0, S) \mathbb{P}^S(r_T \le r^\star)$$
$$- K P(r_0, 0, T) \mathbb{P}^T(r_T \le r^\star) \tag{10}$$

where  $r^* = \ln(A_{0,1}(S-T)/K)/B_{0,1}(S-T)$ . Obviously, we have a similar formula for put options. Nonetheless, options on zero-coupon bonds are not standard in practice, and products like caps, floors, and swaptions are mostly preferred to get hedge against interest-rate fluctuations (see Caps and **Floors**). A well-known relation is that the price of a floorlet (resp. caplet) between maturities  $T$  and  $S$ can be written as a simple function of a call (resp. put) option on the zero-coupon bond between  $T$  and  $S$  (see, e.g., [2]). This way, from equation (10), we derive closed form formulas for cap and floor prices also. Receiver (resp. payer) European swaptions can readily be seen as call (resp. put) option with a unit strike on a bond whose coupon rate corresponds to the swaption strike (see **Bond Options**). Thus, denoting the maturity by T, and with  $T <$  $S_1 < \ldots < S_n$ , the payment grid, its price has the following form  $\mathbb{E}[\mathrm{e}^{-\int_0^T r_s \mathrm{d}s} (\sum_{i=1}^n \alpha_i P(r_T, T, S_i) - 1)^+]$ <br>with  $\alpha_i \geq 0$ ,  $\sum_{i=1}^n \alpha_i > 1$ . Thanks to the strike decomposition introduced by Jamshidian [7], it turns out to be a combination of call prices on zerocoupon bonds. Indeed,  $P(r, T, S)$  being decreasing with respect to r, there is a unique  $\rho > 0$ such that  $\sum_{i=1}^{n} \alpha_i P(\rho, T, S_i) = 1$ , and we have  $(\sum_{i=1}^{n} \alpha_i [P(r_T, T, S_i) - P(\rho, T, S_i)])^+ = \sum_{i=1}^{n}$  $\overline{\alpha_i(P(r_T,T,S_i)-P(\rho,T,S_i))^{+}}$ .

#### Calibration

Let us turn to the calibration of the CIR model to the market prices. We have analytical formulas for zero-coupon bond, cap, and floor prices. Swaption prices can also be computed very quickly,  $\rho$  being obtained, for example, by dichotomy. Therefore, the distance between the market prices and the theoretical ones obtained from the CIR model can be computed quickly and minimized with the use of any optimization algorithm. In this way, we can identify optimal parameters  $r_0$ ,  $\kappa$ ,  $\theta$ , and  $\sigma$ . In practice, it is likely to better fit swaption prices than cap and floor prices. Indeed, they do not only

describe the evolution of each single rate for different maturities but also the dependence between them. Unfortunately, these four parameters are anyway not enough in practice, if we want to accurately capture all the market data. For this reason, many works have been done to extend the CIR model. While doing this, the challenge is to preserve the nice analytical tractability of the CIR model. Without being exhaustive, we mention here the extended CIR model [9] where parameters *κ*, *θ* and *σ* are supposed to be time dependent, and the particular case where *κ(t )θ (t )/σ*<sup>2</sup>*(t)* is constant that allow to preserve some closed formulas [8]. Other generalizations have been proposed, like adding a deterministic shift or another independent CIR process (see [2] for some numerical experiments). Most of these extensions are embedded in the general affine framework described in [5] (*see* **Term Structure Models**).

## **Monte Carlo Simulation**

Finally, it is important to mention the simulation issues concerning square-root diffusions. This topic goes beyond the world of interest derivatives because these diffusions are widespread in finance, such as in the Heston model (*see* **Heston Model**). First, exact simulation is possible for the CIR model since we know how to simulate a noncentral chi-square distribution [6]. However, in some applications, it may be more convenient to use discretization schemes that often lead to smaller computation times. We face the difficulty that usual schemes such as Euler and Milstein generally fail. This is due to the square root in the CIR dynamics, which is non-Lipschitzian near the origin and is not defined for negative values. Tailored schemes should then be considered as in [1]. More information on the simulation of the CIR process can be found in **Simulation of Square-root Processes**.

### **Conclusion**

The fundamental features of the CIR model—intuitive parameterization, nonnegativity, pricing formulas for main options—explain why it has been widely used for hedging risk on interest-rate derivatives. Nowadays, owing to the complexity of the fixed income market, more sophisticated models are required, such as Libor or Swap Market models (*see* **LIBOR Market Model** and **Swap Market Models**). Nonetheless, the CIR model is often used as a building block for more complex models. Many extensions that rely on the same mathematical properties are widespread for interest-rate modeling (multifactor quadratic Gaussian models (*see* **Quadratic Gaussian Models**, affine models (*see* **Affine Models**), the Heston model for equity (*see* **Heston Model**), or the Duffie–Singleton model on credit derivatives (*see* **Duffie–Singleton Model**).

### **References**

- [1] Alfonsi A. (2008). *High Order Discretization Schemes for the CIR Process: Application to Affine Term Structure and Heston Models*, available on http://hal.archivesouvertes.fr/
- [2] Brigo D. & Mercurio, F. (2006). *Interest Rate Models: Theory and Practice*, 2nd Edition, Springer-Verlag.
- [3] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). An intertemporal general equilibrium model of asset prices, *Econometrica* **53**, 363–384.
- [4] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–407.
- [5] Duffie, D., Pan, J. & Singleton, S.A. (2000). Transform analysis and asset pricing for affine jump diffusions, *Econometrica* **68**, 1343–1376.
- [6] Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*, Series: Applications of Mathematics, Vol. 53, Springer.
- [7] Jamshidian, F. (1989). An exact bond option formula, *Journal of Finance* **44**, 205–209.
- [8] Jamshidian, F. (1995). A simple class of square-root interest-rate models, *Applied Mathematical Finance* **2**, 61–72.
- [9] Hull, J. & White, A. (1990). Pricing interest rate derivative securities, *The Review of Financial Studies* **3**, 573–592.
- [10] Lamberton, D. & Lapeyre, B. (1996). *An Introduction to Stochastic Calculus Applied to Finance*, Chapman & Hall.

## **Related Articles**

**Affine Models**; **Bond**; **Bond Options**; **Caps and Floors**; **Duffie–Singleton Model**; **Forward and Swap Measures**; **Hedging**; **Heston Model**; **LIBOR Market Model**; **Quadratic Gaussian Models**; **Risk Premia**; **Ross, Stephen**; **Simulation of Square-root Processes**; **Swap Market Models**; **Term Structure Models**.

AURELIEN ´ ALFONSI
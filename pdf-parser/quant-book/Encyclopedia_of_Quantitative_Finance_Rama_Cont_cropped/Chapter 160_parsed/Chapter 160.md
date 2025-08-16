# Time-changed Lévy Process

If  $L$  is a Lévy process (see **Lévy Processes**) and  $(T_t)_{t\geq 0}$  is a positive increasing process,  $X_t = L(T_t)$  is called a time-changed Lévy process with time change  $(T_t)_{t>0}$ . When the time change is independent from  $L$ , many properties of  $X$  can be derived from those of  $L$ .

Many Lévy processes have appeared as timechanged Brownian motions (see Time Change), so one might ask why one should time change them yet again. In this regard, we note that Lévy processes are by construction processes of independent identically distributed increments and hence all distributional parameters such as variances, skewness, kurtosis, and possibly correlations are constant. Yet all these and possibly more entities are stochastic in actual economies, and this randomness may be important for particular questions of interest. These considerations led in the first instance to the construction of processes displaying stochastic volatility with the local innovations of a Lévy process. Analytical tractability of characteristic functions motivated models with exponential affine characteristic functions (see Affine **Models**) and through the work of Duffie *et al.* [4] it became well known that this would be the case if the infinitesimal generator of the resulting Markov process was linear in state variables. The recipe for constructing these models was, therefore, clear.

A number of models in this direction were presented by Carr et al. [2]. Three Lévy processes were selected for being time changed and they were the normal inverse Gaussian (NIG) (see Normal Inverse Gaussian Model), the variance gamma (VG) (see Variance-gamma Model), and the CGMY model (see **Tempered Stable Process**). The first two were already known to be time changes of Brownian motion with drift. Cont and Tankov [3, Prop. 4.1] show that the CGMY also has such a representation. Characteristic exponents  $\psi(u;.)$  are critical to the development of the exponential affine representations (see Affine Models) involved, which are given here by the logarithm of the characteristic functions taken at unit time. For these three models, the characteristic exponents are given as (subscript indicates the model name)

 $\psi_{\text{NIG}}(u; \sigma, \nu, \theta)$ 

$$=\sigma\left(\frac{\nu}{\theta}-\sqrt{\frac{\nu^{2}}{\theta^{2}}-2\frac{\theta\mathrm{i}u}{\sigma^{2}}+u^{2}}\right),\,\sigma,\,\nu>0,\,\,\theta\in\mathbb{R}$$
(1)

 $\psi_{\text{VG}}(u;\sigma,\nu,\theta)$ 

$$= \frac{1}{\nu} \log \left( 1 - \mathrm{i} u \theta \nu - \frac{\sigma^2 \nu}{2} u^2 \right), \sigma, \ \theta, \nu \in \mathbb{R} \ (2)$$

 $\psi_{\text{CGMY}}(u;C,G,M,Y)$ 

$$= C\Gamma(-Y)((M - iu)^{Y} - M^{Y} + (G + iu)^{Y}$$
$$- G^{Y}), C, G, M > 0, 0 < Y < 2.$$
 (3)

The details of the associated Lévy processes are given, which would assist in various applications. The NIG and VG processes can be written as Brownian motion with drift  $\theta$  and volatility  $\sigma$  time changed by an inverse Gaussian process and a gamma process, respectively. The inverse Gaussian process  $T_t^{\nu}$  is the time taken by an independent Brownian motion with drift  $\nu$  to reach the level  $t$ , while the gamma process  $G_t^v$  is an increasing process with independent identically distributed increments where the increments over unit time have a gamma distribution with unit mean and volatility  $\nu$ . Both the NIG and VG are pure jump processes with Lévy measures  $k_{\text{NIG}}(x) dx$ ,  $k_{\text{VG}}(x) dx$  defined as

$$k_{\text{NIG}}(x) = \sqrt{\frac{2}{\pi}} \sigma \alpha^2 \frac{e^{\beta x} K_1(|x|)}{|x|} \tag{4}$$

$$\beta = \frac{\theta}{\sigma^2}, \quad \alpha^2 = \frac{v^2}{\sigma^2} + \frac{\theta^2}{\sigma^4} \tag{5}$$

$$k_{\text{VG}}(x) = \frac{C}{|x|} \exp\left(\frac{G-M}{2}x\right) \exp\left(-\frac{G+M}{2}|x|\right) \tag{6}$$

$$C = \frac{1}{\nu}; G = \left(\sqrt{\frac{\theta^2 \nu^2}{4} + \frac{\sigma^2 \nu}{2}} - \frac{\theta \nu}{2}\right)^{-1},$$
$$M = \left(\sqrt{\frac{\theta^2 \nu^2}{4} + \frac{\sigma^2 \nu}{2}} + \frac{\theta \nu}{2}\right)^{-1}$$
(7)

where  $K_{\alpha}(x)$  is the Bessel K function.

The CGMY process was defined in terms of its Lévy measure  $k_{\text{CGMY}}(x) dx$  with

$$k_{\text{CGMY}}(x) = \frac{C}{|x|^{1+Y}} \exp\left(\frac{G-M}{2}x\right)$$
$$\times \exp\left(-\frac{G+M}{2}|x|\right) \qquad (8)$$

It was shown in  $[3,$  Proposition 4.1] (see also [6]) that the  $CGMY$  process can be represented as Brownian motion with drift  $(G - M)/2$  time changed by a shaved stable  $\frac{Y}{2}$  subordinator with shaving function

$$f(y) = e^{-\frac{(B^2 - A^2)y}{2}} E\left[e^{-\frac{B^2 y}{2} \frac{\gamma \gamma/2}{\gamma_{1/2}}}\right],$$
$$A = \frac{G - M}{2}, \quad B = \frac{G + M}{2} \tag{9}$$

where  $\gamma_{Y/2}$ ,  $\gamma_{1/2}$  are independent gamma variates.

One may explicitly evaluate in terms of Hermite functions:

$$E\left[e^{-\frac{B^2y}{2}\frac{\gamma_{Y/2}}{\gamma_{1/2}}}\right] = \frac{\Gamma(Y)}{\Gamma\left(\frac{Y}{2}\right)2^{\frac{Y}{2}-1}}h_{-Y}(B\sqrt{y})$$

where

$$h_{\nu}(z) = \frac{1}{\Gamma(-\nu)} \int_0^{\infty} e^{-y^2/2 - yz} y^{-\nu - 1} dy \quad (\nu < 0)$$
(11)

### **A Continuous Time Change**

We can introduce stochastic volatility along with a clustering of volatility by time changing these Lévy processes by the integral of the square root process  $y(t)$ , where

$$dy = \kappa (\eta - y) dt + \lambda \sqrt{y} dW \qquad (12)$$

for an independent Brownian motion  $(W(t), t > 0)$ . For a candidate Lévy process  $X(t)$ , we consider as a model for the uncertainty driving the stock the composite process

$$Z(t) = X(Y(t)) \tag{13}$$

where

$$Y(t) = \int_0^t y(u) \, \mathrm{d}u \tag{14}$$

The characteristic function for the composite process is easily derived from the characteristic function of  $Y(t)$  as

$$E\left[e^{iuY(t)}\right] = \phi(u, t, y(0), \kappa, \eta, \lambda)$$
  
$$= A(t, u) \exp\left(B(t, u)y(0)\right) \qquad (15)$$
  
$$A(t, u) = \frac{\exp\left(\frac{\kappa^2 \eta t}{\lambda^2}\right)}{\left(\cosh\left(\frac{\gamma t}{2}\right) + \frac{\kappa}{\gamma} \sinh\left(\frac{\gamma t}{2}\right)\right)^{\frac{2\kappa\eta}{\lambda^2}}} \qquad (16)$$

$$B(t, u) = \frac{2\mathrm{i}u}{\kappa + \gamma \coth\left(\frac{\gamma t}{2}\right)}$$
(17)

$$\gamma = \sqrt{\kappa^2 - 2\lambda^2 \mathrm{i}u} \tag{18}$$

It follows that

 $(10)$ 

$$E\left[\exp\left(iuZ(t)\right)\right] = \phi\left(-i\psi_X(u), t, y(0), \kappa, \eta, \lambda\right) \tag{19}$$

## The Stock Price Model

There are two approaches to model the stock price  $S(t)$ . The first approach takes the exponential of the composite process corrected to get the correct forward price, whereby we define

$$S_1(t) = S(0) \frac{\exp\left(Z\left(t\right)\right)}{E\left[\exp\left(Z\left(t\right)\right)\right]} \tag{20}$$

In this case, the stock price has the right forward and the resulting option prices are free of static arbitrage. However, there may be the possibility of dynamic arbitrage in the model and this is an issue if the model is being used continuously to quote on options with constant parameters through time. To exclude dynamic arbitrage in the model, one could form a martingale model for the forward stock price by modeling it as the stochastic exponential of the martingale:

$$n(t) = Z(t) - \int_0^t \int_{-\infty}^\infty xy(t) k_X(x) \, \mathrm{d}x \mathrm{d}s \qquad (21)$$

In the second approach, one writes the stock price process  $S_2(t)$  as

$$S_2(t) = S(0) \exp\left((r-q)t\right) \exp(Z(t)$$
$$-Y(t)\psi_X(-\mathbf{i})) \tag{22}$$

For the first approach, the log characteristic function for the logarithm of the stock price is given as

$$E \left[ \exp \left( \mathrm{i}u \log S_1(t) \right) \right]$$
  
=  $\exp \left( \mathrm{i}u (\log(S(0) + (r - q)t)) \right)$   
 $\times \frac{\phi \left( -\mathrm{i}\psi_X(u), t, y(0); \kappa, \eta, \lambda \right)}{\phi \left( -\mathrm{i}\psi_X(-i), t, y(0); \kappa, \eta, \lambda \right)^{\mathrm{i}u}}$ (23)

The second approach leads to the following characteristic function:

$$E \left[ \exp \left( \mathrm{i}u \log S_2(t) \right) \right]$$
  
=  $\exp \left( \mathrm{i}u (\log(S(0) + (r - q)t)) \times \phi(-\mathrm{i}\psi_X(u) - u\psi_X(-\mathrm{i}), t, y(0); \kappa, \eta, \lambda) \right)$   
(24)

The models of the first approach are termed NIGSA, VGSA, and CGMYSA for NIG, VG, and CGMY with a stochastic arrival rate of jumps adapted to the level of the process  $y(t)$ . The models of the second approach are martingale models and are termed NIGSAM, VGSAM, and CGMYSAM, respectively. It is observed in calibrations that the first approach generally fits the option price data better.

#### Some Discontinuous Time Changes

One can replace the continuous stochastic process for the arrival rate of jump activity  $v(t)$  by a discontinuous process that now only has upward jumps. We call this process  $y^{J}(t)$  for discontinuous jump arrival rates. Given a background driving Lévy process (BDLP)  $U(t)$  with only positive jumps, we define

$$dy^{J}(t) = -\kappa y^{J}(t) dt + dU(t)$$
 (25)

The composite process now permits some direct dependence between arrival rate jumps and the underlying uncertainty:

$$Z^{J}(t) = X(Y^{J}(t)) + \rho U(t) \tag{26}$$

$$Y^{J}(t) = \int_{0}^{t} y^{J}(s) \, \mathrm{d}s \tag{27}$$

We suppose that the background driving Lévy process has the following characteristic function:

$$E[\exp(iuU(t)) = \exp(t\psi_U(u)) \qquad (28)$$

The characteristic function of the composite process  $Z^{J}(t)$  may be developed in terms of the joint characteristic function of  $Y^{J}(t)$ ,  $U(t)$  as

$$\Phi_t(a,b) = E\left[\exp\left(\mathrm{i}aY^J(t) + \mathrm{i}bU(t)\right)\right] \tag{29}$$

We may show that

$$E\left[\exp\left(iuZ^{J}(t)\right)\right] = \Phi_{t}(-i\psi_{X}(u), u\rho) \qquad (30)$$

We have that

$$\Phi_t(a,b) = \exp\left(iay(0)\frac{1 - e^{-\kappa t}}{\kappa}\right)$$
$$\times \exp\left(\int_L^U \frac{\psi_U(v)}{a + \kappa b - \kappa v} dv\right) \tag{31}$$

$$L = b \tag{32}$$

$$U = b + a \frac{1 - e^{-\kappa t}}{\kappa} \tag{33}$$

The characteristic functions for the logarithm of the stock price for the exponential model are now

$$E \left[ \exp \left( \mathrm{i}u \log(S_1^J(t)) \right) \right]$$
  
=  $\exp \left( \mathrm{i}u (\log(S(0) + (r - q)t)) \times \Phi_t(-\mathrm{i}\psi_X(u), \rho u) \times \exp \left( -\mathrm{i}u \log \left( \Phi_t(-\mathrm{i}\psi_X(-i), -\mathrm{i}\rho) \right) \right) \right)$  (34)

For the stochastic exponential, the result is given as

$$E\left[\exp\left(iu\log(S_2^J(t))\right)\right]$$
  
=  $\exp(iu(\log(S(0)) + (r-q)t - \psi_U(-i\rho)t))$   
 $\times \Phi_t\left(-i\psi_X(u) - u\psi_X(-i), \rho u\right)$  (35)

Some explicit examples for  $\psi_U(u)$ , for which we may obtain exact expressions for  $\Phi_t(a, b)$ , remain to be determined.

#### Examples for $\psi_U(u)$ and $\Phi_t(a,b)$

Three explicit models for  $\psi_U$  were developed. These are SG for stationary gamma, IG for inverse Gaussian, and SIG for stationary inverse Gaussian.

### The SG Case

In this case, the Lévy density for jumps in the process  $U(t)$  is

$$k_U(x) = \frac{\lambda}{\zeta} e^{-x/\zeta} \tag{36}$$

The log characteristic function of the BDLP is

$$\psi_U(u) = \frac{\mathrm{i}u\lambda}{1/\zeta - \mathrm{i}u} \tag{37}$$

#### The IG Case

The Laplace transform for inverse Gaussian (see Normal Inverse Gaussian Model) time with drift  $\nu$  for the Brownian motion is

$$E\left[\exp\left(-\lambda T_1^{\nu}\right)\right] = \exp\left(\nu - \sqrt{\nu^2 + 2\lambda}\right) \qquad (38)$$

and the log characteristic function is

$$\psi_U(u) = \nu - \sqrt{\nu^2 - 2\mathrm{i}u} \tag{39}$$

### The SIG Case

For this case, Barndorff-Nielsen and Shephard [1] show that the Lévy density is

$$k_U(x) = \frac{1}{2\sqrt{2\pi}} x^{-3/2} (1 + \nu^2 x) \exp\left(-\frac{\nu^2 x}{2}\right) \tag{40}$$

The log characteristic function is

$$\psi_U(u) = \frac{\mathrm{i}u}{\sqrt{v^2 - 2\mathrm{i}u}}\tag{41}$$

For these three cases, the construction of  $\Phi_t(a, b)$ is completed on determining the integral

$$\int_{L}^{U} \frac{\psi_{Z}(v)}{a + \kappa b - \kappa v} dv = \Psi(U, a, b) - \Psi(L, a, b)$$
(42)

and we have analytic expressions for  $\Psi(x, a, b)$  in the SG, IG, and SIG cases that are as follows:

$$\Psi_{\text{SG}}(x, a, b; \kappa, \lambda, \zeta)\n$$

$$\n= \log \left[ \left( x + \frac{\mathrm{i}}{\zeta} \right)^{\frac{\lambda}{\kappa - \mathrm{i}\zeta(a + \kappa b)}} \times (a + \kappa b - \kappa x)^{\frac{\lambda(a + \kappa b)\zeta}{\kappa((a + \kappa b)\zeta + \mathrm{i}\kappa)}} \right] \n$$
(43)

$$\Psi_{\text{IG}}(x, a, b; \kappa, \nu)\n$$

$$\n= \frac{2\sqrt{\nu^2 - 2ix}}{\kappa} + \frac{2\sqrt{\nu^2\kappa - 2i(a + \kappa b)}}{\kappa^{3/2}}\n$$

$$\n\times \operatorname{arctanh}\left[\frac{\sqrt{\kappa}\sqrt{\nu^2 - 2ix}}{\sqrt{\nu^2\kappa - 2i(a + \kappa b)}}\right]\n$$

$$\n- \frac{\nu \log(a + \kappa b - \kappa x)}{\kappa}\n$$

$$\n\Psi_{\text{SIG}}(x, a, b; \kappa, \nu)\n$$
(44)

$$= \frac{\sqrt{\nu^2 - 2ix}}{\kappa} - \frac{2i(a + \kappa b)}{\kappa^{3/2}\sqrt{\nu^2\kappa - 2i(a + \kappa b)}}$$
$$\times \operatorname{arctanh}\left[\frac{\sqrt{\kappa}\sqrt{\nu^2 - 2ix}}{\sqrt{\nu^2\kappa - 2i(a + \kappa b)}}\right] \qquad (45)$$

# Correlation in VGSA or VGCSA

We consider the introduction of correlation in VGSA along the following lines. We define the correlated uncertainty as

$$Z^{C}(t) = X(Y(t)) + \rho y(t) \tag{46}$$

The characteristic function now follows from the joint characteristic function of  $Y(t)$ ,  $y(t)$ :

$$E\left[e^{iuZ^{C}(t)}\right] = E\left[e^{Y(t)\psi_{X}(u) + iu\rho_{Y}(t)}\right] \qquad (47)$$

Let

$$\Phi_t^C(a, b, x) = E\left[\exp\left(\mathrm{i}aY(t) + \mathrm{i}by(t)\right)|y(0) = x\right]$$
(48)

We have

$$\phi_{Z^C}(u) = \Phi_t^C(-\mathrm{i}\psi_X(u), \rho u) \tag{49}$$

We recall the solution for  $\Phi_t(a, b, x)$  from  $[5, 7]$  as

$$\Phi_t^C(a,b,x) = A^C(t,a,b) \exp(B^C(t,a,b)x) \quad (50)$$
$$A^C(t,a,b) \quad (50)$$

$$=\frac{\exp\left(\frac{\kappa^{2}\eta t}{\lambda^{2}}\right)}{\left[\cosh\left(\frac{\gamma t}{2}\right)+\frac{\left(\kappa-\mathrm{i}b\lambda^{2}\right)}{\gamma}\sinh\left(\frac{\gamma t}{2}\right)\right]^{\frac{2\kappa\eta}{\lambda^{2}}}}$$
(51)

$$B^{C}(t,a,b) = \frac{\mathrm{i}b\left[\gamma\cosh\left(\frac{\gamma t}{2}\right) - \kappa\sinh\left(\frac{\gamma t}{2}\right)\right] + 2\mathrm{i}a\sinh\left(\frac{\gamma t}{2}\right)}{\gamma\cosh\left(\frac{\gamma t}{2}\right) + \left(\kappa - \mathrm{i}b\lambda^{2}\right)\sinh\left(\frac{\gamma t}{2}\right)}$$
(52)  
$$\gamma = \sqrt{\kappa^{2} - 2\lambda^{2}\mathrm{i}a}$$
(53)

We get the characteristic function for the model VGCSA, where the letter  $C$  denotes correlated stochastic arrival by exponentiation as

$$E \left[ \exp \left( iu \log(S_1^C(t)) \right) \right]$$
  
=  $\exp \left( iu (\log(S(0)) + (r - q)t) \right)$   
 $\times \Phi_t^C(-i\psi_X(u), \rho u)$   
 $\times \exp\left( -iu \log(\Phi_t^C(-i\psi_X(-i), -i\rho)) \right)$  (54)

# Exciting the Jumps by the Level of Activity that Is Also a Heston Type of **Correlated Volatility**

In this class of models, we introduce stochastic volatility and allow jump arrival rates to respond to the volatility on each side with separate sensitivities. This will give rise to stochastic skewness as well as to volatility. The model for the logarithm of the stock price  $H(t) = \log(S(t))$  is now as follows:

$$H(t) = H(0) + (r - q)t - \int_0^t \frac{y(u)}{2} du$$
$$- (c_p t + s_p Y(t)) \int_0^\infty (e^x - 1 - x) k_p(x) dx$$
$$- (c_n t + s_n Y(t)) \int_{-\infty}^0 (e^x - 1 - x) k_n(x) dx$$
$$+ x * (\mu - \nu) + \int_0^t \sqrt{y(u)} dW_S(u) \qquad (55)$$

$$\Psi(t, H(t), y(t)) = A(\tau) \exp(\mathrm{i}aH(t) + \gamma(\tau)y(t))$$

$$Y(t) = \int_0^t y(u) \, \mathrm{d}u \tag{56}$$

$$dy = \kappa(\eta - y) dt + \lambda \sqrt{y} dW_y(t) \quad (57)$$

$$dW_y \, dW_S = \rho \, dt \tag{58}$$

$$\nu(\,dx,\,dt) = \left(c_p + s_p y(t)\right) k_p(x) \mathbf{1}_{x>0} \, dx \n+ (c_n + s_n y(t)) k_n(x) \mathbf{1}_{x<0} \, dx \tag{59}$$

The growth rate of the stock price is at the risk neutral level of  $(r - q)$ . The coefficients  $c_p, c_n$  are the Lévy jump response components. The sensitivities of jumps to volatility are captured by the two slope coefficients  $s_p$ ,  $s_n$  for the positive and the negative sides. The logarithm of the stock price is a continuous martingale with stochastic volatility plus a compensated jump martingale that has jumps responding to volatility with log price drift set to fix the stock drift at  $r - q$ .

The joint characteristic function of the log of the stock price, the level of the terminal variance, and the remaining integrated variance is

$$\Psi(t, H(t), y(t))\n$$

$$\n= E_t \left[ \exp(\mathrm{i}aH(T) + \mathrm{i}by(T) + \mathrm{i}c \int_t^T y(u) \, \mathrm{d}u \right]\n$$
(60)

We have a closed form for  $\Psi$  in this model given

(61)

$$A(\tau) = \exp\left(\left(\mathrm{i}a(r-q) + c_p u_p + c_n u_n + (\kappa - \lambda \rho \mathrm{i}a)\frac{\kappa \eta}{\lambda^2}\right)\tau\right)\left(\frac{\cosh(D)}{\cosh\left(D - \frac{\tau}{2}\xi\right)}\right)^{\frac{2\kappa \eta}{\lambda^2}}\tag{62}$$

as

$$\gamma(\tau) = \frac{\kappa - \lambda \rho i a}{\lambda^2} + \frac{\xi}{\lambda^2} \tanh\left(D - \frac{\xi}{2}\tau\right) \tag{63}$$

$$\xi = \sqrt{(\kappa - \lambda \rho \mathrm{i}a)^2 + \lambda^2 \left[a^2 + \mathrm{i}(a - 2c) - 2(s_p u_p + s_n u_n)\right]}$$
(64)

$$u_p = \int_0^\infty (e^x - 1 - iax)k_p(x) dx - ia \int_0^\infty (e^x - 1 - x)k_p(x) dx \tag{65}$$

$$u_n = \int_{-\infty}^0 (e^x - 1 - iax)k_n(x) dx - \int_{-\infty}^0 (e^x - 1 - x)k_n(x) dx \tag{66}$$

$$D = \tanh^{-1} \left( \frac{\mathrm{i}b\lambda^2}{\xi} - \frac{\kappa - \lambda\rho\mathrm{i}a}{\xi} \right) \tag{67}$$

On setting  $b = c = 0$ , we obtain the characteristic function of the log of the final stock price and this yields the models: SVADNE, SVAVG, and SVAC-CGMYY.

We note that for DNE

$$u_{p} = (1 - ia) \frac{1}{\beta_{p} - 1}$$
 (68)

$$u_n = -(1 - ia)\frac{1}{\beta_n + 1}$$
 (69)

The corresponding calculations for VG in the CGM parameterization are

$$u_p = \log\left(\frac{M}{M-1}\right) \tag{70}$$

$$u_n = \log\left(\frac{G}{G+1}\right) \tag{71}$$

For CCGMYY, we have the following result:

$$u_p = \Gamma(-y_p) \left( (M-1)^{y_p} - M^{y_p} \right) \tag{72}$$

$$u_n = \Gamma(-y_n) \left( (G+1)^{y_n} - G^{y_n} \right) \tag{73}$$

#### References

- [1] Barndorff-Nielsen, O.E. (1998). Processes of normal inverse Gaussian type, Finance and Stochastics 2, 41-68.
- [2] Carr, P., Geman, H., Madan, D. & Yor, M. (2003). Stochastic volatility for Levy processes, Mathematical Finance 13, 345-382.

- [3] Cont, R. & Tankov, P. (2004). Financial Modelling with Jump Processes, Series in Financial Mathematics, CRC Press.
- [4] Duffie, D., Filipovic, D. & Schachermayer, W. (2003). Affine processes and applications in finance, Annals of Applied Probability 13, 984–1053.
- [5] Lamberton, D. & Lapeyre, B. (1996). Introduction to Stochastic Calculus Applied to Finance, Chapman and Hall, New York.
- [6] Madan, D. & Yor, M. (2008). Representing the CGMY and Meixner Levy processes as time changed Brownian motions, Journal of Computational Finance Fall, 27-47.
- [7] Pitman, J. & Yor M. (1982). A decomposition of Bessel Bridges, Zeitschrift für Wahrsch- einlichkeitstheorie und Verwandte Gebiete 59, 425–457.

#### **Further Reading**

- Carr, P., Geman, H., Madan, D. & Yor, M. (2002). The fine structure of asset returns: an empirical investigation, Journal of Business, 75(2), 305-332.
- Madan, D., Carr, P. & Chang, E. (1998). The variance gamma process and option pricing, European Finance Review 2,  $79 - 105$ .
- Madan, D.B. & Seneta, E. (1990). The Variance Gamma (VG) model for share market returns, Journal of Business 63, 511-524.

#### **Related Articles**

Affine Models; Barndorff-Nielsen and Shephard (BNS) Models; Exponential Lévy Models; Heston Model; Lévy Processes; Normal Inverse Gaussian Model; Squared Bessel Processes; Stochastic Exponential; Tempered Stable Process; Time Change; Variance-gamma Model.

DILIP B. MADAN
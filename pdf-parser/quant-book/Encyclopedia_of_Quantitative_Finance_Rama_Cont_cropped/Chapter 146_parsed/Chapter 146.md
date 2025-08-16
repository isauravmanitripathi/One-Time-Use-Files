# **SABR Model**

The SABR model [4] is a stochastic volatility (see Stochastic Volatility Models) model in which the forward asset price follows the dynamics in a forward measure  $\mathbb{P}^T$ :

$$\mathrm{d}f_t = a_t C(f_t) \,\mathrm{d}W_t \tag{1}$$

$$da_t = va_t dZ_t , \alpha \equiv a_0 \tag{2}$$

$$dW_t dZ_t = \rho dt, \ C(f) \equiv f^{\beta}, \ \beta \in [0, 1) \tag{3}$$

The stochastic volatility  $a_t$ , is described by a geometric Brownian motion. The model depends on four parameters:  $\alpha$ ,  $\nu$ ,  $\rho$ , and  $\beta$ . By using singular perturbation techniques, Hagan et al. [4] obtained a closed-form formula for the implied volatility  $\sigma_{\text{BS}}(\tau, K)$ , at the first-order in the maturity  $\tau$ . Here, we display a corrected version of the formula  $[8]$ :

$$\sigma_{\text{BS}}(\tau, K) = \frac{\nu \ln \frac{f_0}{K}}{\hat{x}(\zeta)} \left(1 + \sigma_1(f_{\text{av}})\tau\right) \tag{4}$$

with

$$\hat{x}(\zeta) = \ln\left(\frac{\sqrt{1 - 2\rho\zeta + \zeta^2} - \rho + \zeta}{1 - \rho}\right)\n$$

$$\n\zeta = \frac{\nu}{\alpha} \int_{K}^{f_0} \frac{\mathrm{d}x}{C(x)}, f_{\mathrm{av}} = \sqrt{f_0 K}\n$$

$$\n\sigma_1(f) = \frac{\alpha \nu \partial_f C(f)\rho}{4} + \frac{2 - 3\rho^2}{24} \nu^2 + \frac{(\alpha C(f))^2}{24}\n$$

$$\n\times \left(\frac{1}{f^2} + \frac{2\partial_{ff} C(f)}{C(f)} - \left(\frac{\partial_f C(f)}{C(f)}\right)^2\right)\n$$
(5)

Though this formula is popular, volatility does not mean-revert in the underlying SABR model, so for given  $\alpha$ ,  $\nu$ ,  $\beta$ , and  $\rho$ , the SABR formula cannot simultaneously calibrate to the implied volatility smile at more than one expiry.

By mapping Hagan et al.'s computations into a geometrical framework based on the heat kernel expansion, approximate implied volatility formulae may be derived for more general stochastic volatility models (SVMs), in particular for the models where volatility mean-reverts. The use of geometrical methods in quantitative finance originates from  $[1, 2]$  and was investigated in detail in  $[5, 6, 7]$ .

# A More General Stochastic Process

In the following, we will assume arbitrary local volatility functions  $C(\cdot)$  and a general time-homo geneous one-dimensional stochastic differential equation (SDE) for the stochastic volatility process

$$da_t = b(a_t) dt + \sigma(a_t) dZ_t \tag{6}$$

In principle,  $b(\cdot)$  and  $\sigma(\cdot)$  could depend on the forward  $f$  as well, but the models we are interested in here do not exhibit this additional dependence.

This strategy for computing the short-time implied volatility asymptotics induced by the SVM involves two main steps:

- Derive the short-time limit of the effective local . volatility function. The computation involves the use of the heat kernel expansion.
- Derive an approximate expression for the implied volatility corresponding to this effective local volatility function.

## **Effective Local Volatility Model**

The square of the Dupire effective local volatility function (*see* **Model Calibration**) [3] is equal to the mean of the square of the stochastic volatility when the forward is fixed to the strike

$$\sigma_{\text{loc}}(t, K)^{2} = C(K)^{2} \mathbb{E}^{\mathbb{P}}[a_{t}^{2}|f_{t} = K]$$
$$= C(K)^{2} \frac{\int_{-\infty}^{\infty} a^{2} \mathbf{p}(t, K, a|f_{0}, \alpha) da}{\int_{-\infty}^{\infty} \mathbf{p}(t, K, a|f_{0}, \alpha) da}$$
(7)

where  $p(t, K, a | f, \alpha)$  is the conditional probability density for the forward and the volatility at time t. As we now proceed to explain,  $p(t, K, a|f, \alpha)$  is the fundamental solution of a heat kernel equation depending on two important geometrical quantities: first a metric tensor in equation (9), which is the inverse of the local covariance matrix and second an Abelian connection in equation  $(10)$  which depends on the drift  $b(a)$ .

# **Heat Kernel Expansion**

A short-time expansion of the density for a multidimensional Itô diffusion process can be obtained using the heat kernel expansion: the Kolmogorov equation is rewritten as a heat kernel equation on an  $n$ -dimensional Riemannian manifold endowed with an Abelian connection as explained in [7].

Suppose the stochastic equations are written as

$$dx^{\mu} = b^{\mu}(x) dt + \sigma^{\mu}(x) dW^{\mu} \tag{8}$$

with  $dW^{\mu} dW^{\nu} = \rho_{\mu\nu} dt$ . The associated metric  $g_{\mu\nu}$ depends only on the diffusion terms  $\sigma_{\mu}$ , while the connection  $\mathcal{A}_{\mu}(x)$  involves drift terms  $b^{\mu}$  as well:

$$g_{\mu\nu}(x) = 2 \frac{\rho^{\mu\nu}}{\sigma_{\mu}(x)\sigma_{\nu}(x)}$$
$$\rho^{\mu\nu} \equiv [\rho^{-1}]_{\mu\nu}, \ \mu, \nu = 1 \cdots n$$
$$\mathcal{A}^{\mu}(x) = \frac{1}{2} \left( b^{\mu}(x) - g^{-\frac{1}{2}} \partial_{\nu} \left( g^{1/2} g^{\mu\nu}(x) \right) \right) \tag{9}$$

with

$$g(x) \equiv \det[g_{\mu\nu}(x)] \tag{10}$$

Here, we have used the Einstein convention meaning that two repeated indices are implicitly summed. We set

$$\mathcal{A}_{\mu}(x) = g_{\mu\nu}(x)\mathcal{A}^{\nu}(x) \tag{11}$$

The asymptotic solution to the Kolmogorov equation in the short-time limit is given by

$$\mathbf{p}(t, x|x_0) = \frac{\sqrt{g(x)}}{(4\pi t)^{\frac{n}{2}}} \sqrt{\Delta(x)} \mathcal{P}(x^0, x) e^{-\frac{\mathbf{d}(x)^2}{4t}}$$
$$\times \sum_{n=1}^{\infty} a_n(x) t^n \tag{12}$$

 $d(x)$  is the geodesic distance between x and  $x^0$ c measured in the metric  $g_{\mu\nu}$ .  $d(x)$  is defined as the minimizer of

$$d(x)^{2} = \min_{\mathcal{C}} \int_{0}^{1} g_{\mu\nu} \frac{dx^{\mu}}{d\lambda} \frac{dx^{\nu}}{d\lambda} d\lambda \qquad (13)$$

where  $\lambda$  parameterizes the curve  $\mathcal{C}(x^0, x)$  joining  $x(\lambda = 0) \equiv x^0$  and  $x(\lambda = 1) \equiv x$ .

 $\Delta(x)$  is the so-called Van Vleck-Morette determinant:

$$\Delta(x) = g(x)^{-\frac{1}{2}} \det\left(-\frac{\partial^2 \mathrm{d}(x)^2}{2\partial x \partial x^0}\right) g(x^0)^{-\frac{1}{2}}$$
(14)

 $\mathcal{P}(x^0, x)$  is the parallel transport of the Abelian connection along the geodesic  $C(x^0, x)$  from the point  $x^0$  to x:

$$\mathcal{P}(x^{0}, x) = e^{-\int_{\mathcal{C}(x^{0}, x)} \mathcal{A}_{\mu}(x) dx^{\mu}} \tag{15}$$

The  $a_i(x)$  coefficients  $(a_0(x) = 1)$  are smooth functions and depend on geometric invariants such as the scalar curvature. More details can be found in  $[7]$ .

## The Short-time Limit

Plugging the general short-time limit for  $p$  at the firstorder in time as given by equation  $(12)$  in equation (7) and using a saddle-point approximation for the integration over  $a$ , we obtain the short-time limit of the effective local volatility function.

Getting implied volatility from the effective local volatility function boils down to calculating the geodesic distance between any two given points in the metric defined by the SVM. While this is generally a nontrivial task, the geodesic distance is known analytically in the special case of the geometry associated with the SVM defined by equations (1) and (6). Details are given in [7].

## Asymptotic Implied Volatility

Applying these techniques, we find that the general asymptotic implied volatility at the first order for any

time-homogeneous SVM, depending implicitly on the metric  $g_{ij}$  (9) and the connection  $\mathcal{A}_i$  (10) is given by

$$\sigma_{\text{BS}}(\tau, K) = \frac{\ln \frac{K}{f_0}}{\int_{f_0}^K \frac{\mathrm{d}f'}{\sqrt{2g^{ff}}}} \left( 1 + \frac{g^{ff}\tau}{12} \right)$$
$$\left( -\frac{3}{4} \left( \frac{\partial_f g^{ff}}{g^{ff}} \right)^2 + \frac{\partial_f^2 g^{ff}}{g^{ff}} + \frac{1}{f_{\text{av}^2}} \right)$$
$$+ \frac{g^{ff'}\tau}{2g^{ff}\phi''(a_{\text{min}})}$$
$$\left( \ln(\Delta g \mathcal{P}^2)'(a_{\text{min}}) - \frac{\phi'''(a_{\text{min}})}{\phi''(a_{\text{min}})} + \frac{g^{ff''}}{g^{ff'}} \right) \right) \tag{16}$$

with  $a_{\min}$  the volatility  $a$ , which minimizes the geodesic distance  $d(a, f_{av}|\alpha, f_0)$ . The  $g^{ff}$  are the  $ff$ -components of the inverse metric evaluated at  $a_{\min}$ .  $\Delta$  is the Van Vleck-Morette determinant as in equation (14),  $g$  is the determinant of the metric, and  $\mathcal{P}$  is the parallel gauge transport as in equation (15). The prime symbol ' indicates a derivative according to  $a$ . This formula in equation (16) is particularly useful as we can use it to rapidly calibrate any given SVM. In the following, we apply it to the SABR model with an arbitrary local volatility  $C(\cdot)$ .

# **Improved SABR Formula**

The asymptotic implied volatility in the SABR model with arbitrary local volatility  $C(\cdot)$  is then given by

$$\sigma_{\text{BS}}(\tau, K) = \frac{\ln \frac{K}{f_0}}{\sigma(K)} \left(1 + \sigma_1 \left(f_{\text{av}}\right) \tau\right) \qquad (17)$$

with

$$\sigma_{1}(f) = \frac{\alpha v \rho}{4} \partial_{f} C(f) \frac{\sinh(\mathbf{d}(f))}{\mathbf{d}(f)} + \frac{\left(C(f)a_{\min}\right)^{2}}{24}$$
$$\left(\frac{1}{f^{2}} + \frac{2\partial_{ff} \left(C(f)a_{\min}\right)}{C(f)a_{\min}} - \left(\frac{\partial_{f}(C(f)a_{\min})}{C(f)a_{\min}}\right)^{2}\right) \tag{18}$$

with

$$\sigma(f) = \frac{1}{\nu}$$

$$\times \ln\left(\frac{q\nu + \alpha\rho + \sqrt{\alpha^2 + q^2\nu^2 + 2q\alpha\nu\rho}}{\alpha(1+\rho)}\right)$$

$$q = \int_{f_0}^f \frac{dx}{C(x)}$$

$$a_{\min}(f) = \sqrt{\alpha^2 + 2\alpha\nu\rho q + \nu^2 q^2}$$

$$d(f) = \cosh^{-1}\left(\frac{-q\nu\rho - \alpha\rho^2 + a_{\min}(f)}{\alpha(1-\rho^2)}\right) \quad (19)$$

The original SABR formula (6) can be reproduced by approximating  $a_{\min}$  for strikes near the money by

$$a_{\min} \simeq \alpha + q\rho v$$

and

$$\frac{\sinh(\mathsf{d}(a_{\min}))}{\mathsf{d}(a_{\min})} \simeq 1 \tag{20}$$

An asymptotic formula for a SABR model with a mean-reversion term, called  $\lambda$ -SABR, has been obtained similarly in [7].

#### **Calibration of the Short-term Smile**

Moreover, by inverting equation  $(17)$  to lowest order in  $\tau$ , we see that for any values  $\alpha$ ,  $\rho$ , and  $\nu$ , a given short-term smile  $\sigma_{\text{BS}}(f)$  is calibrated by construction if the local volatility function is chosen as

$$C(f) = \frac{f\sigma_{\rm BS}(f)\left(1 - f\ln\left(\frac{f}{f_0}\right)\frac{\sigma_{\rm BS}'(f)}{\sigma_{\rm BS}(f)}\right)^{-1}}{\alpha\sqrt{1 - \rho^2}\cosh\left(\frac{\rho}{|\rho|}v\frac{\ln\left(\frac{f}{f_0}\right)}{\sigma_{\rm BS}(f)} + \cosh^{-1}\left(\frac{1}{\sqrt{1 - \rho^2}}\right)\right)}$$
(21)

# References

[1] Avellaneda, M., Boyer-Olson, D., Busca, J. & Friz, P. (2002). Reconstructing the smile, Risk Magazine October 91-95.

- [2] Berestycki, H., Busca, J. & Florent, I. (2004). Computing the implied volatility in stochastic volatility models, *Communications on Pure and Applied Mathematics* **57**(10), 1352–1373.
- [3] Dupire, B. (2004). A unified theory of volatility, in *Derivatives Pricing: The Classic Collection*, P. Carr, ed., Risk Publications.
- [4] Hagan, P., Kumar, D., Lesniewski, A.S. & Woodward, D.E. (2002). Managing smile risk, *Wilmott Magazine* September, 84–108.
- [5] Henry-Labordere, P. (2007). Combining the SABR and ` BGM models, *Risk Magazine* October 102–107.
- [6] Henry-Labordere, P (2008). A geometric approach to ` the asymptotics of implied volatility, in R. Cont, ed., *Frontiers in Quantitative Finance: Volatility and Credit Risk Modeling*, Wiley, Chapter 4.
- [7] Henry-Labordere, P. (2008). ` *Analysis, Geometry and Modeling in Finance: Advanced Methods in Option*

*Pricing*, Financial Mathematics Series, Chapman & Hall/CRC 102–104.

[8] Obłoj, J. (2008). Fine-tune your smile, ´ *Wilmott Magazine* May.

# **Further Reading**

- Benaim, S., Friz, P., Lee, R. (2008). On the Black-Scholes implied volatility at extreme strikes, in *Frontiers in Quantitative Finance: Volatility and Credit Risk Modeling*, R. Cont, ed., Wiley, Chapter 3.
- Lee, R. (2004). The moment formula for implied volatility at extreme strikes, *Mathematical Finance* **14**(3), July 469–480.

PIERRE HENRY-LABORDERE `
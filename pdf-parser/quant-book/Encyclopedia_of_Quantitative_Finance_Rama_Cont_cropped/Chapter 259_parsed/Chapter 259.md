# **Fourier Methods in Options Pricing**

## **Pricing European Options**

There are various ways to price European options *via* Fourier inversion. Before we consider such methods, it is worth mentioning why Fourier option pricing methods can be useful. First recall that the riskneutral valuation theorem states that the forward price of a European call option on a single asset *S* can be written as

$$C(S(t), K, T) = \mathbb{E}[(S(T) - K)^{+}] \tag{1}$$

where *C* denotes the value, *T* the maturity, and *K* the strike price of the call. The expectation is taken under the *T* -forward probability measure. As equation (1) is an expectation, it can be calculated *via* numerical integration, provided we know the density in closed form. For many models the density is either not known in closed form, or is quite cumbersome, whereas its characteristic function is often much easier to obtain. A good example in finance is the variance gamma model, introduced by Madan and Seneta [15]. Its density involves a Bessel function of the third kind, whereas its characteristic function only consists of elementary functions.

Heston [8] was among the first to utilize Fourier methods to price European options within his stochastic volatility model. Since Heston's seminal paper, the pricing of European options by means of Fourier inversion has become more and more commonplace. Heston's approach starts from the observation that equation (1) can be recast as

$$C(S(t), K, T) = F(t, T) \cdot \mathbb{S}(S(T) > K)$$
$$-K \cdot \mathbb{P}(S(T) > K) \tag{2}$$

with *F (t, T )* the forward price of the asset and and  respectively the *T* -forward probability measure and the measure induced by taking the asset price as the numeraire. The cumulative probabilities in equation (2) can subsequently be found by Fourier inversion, an approach dating back to [6, 7, 11]. As this approach necessitates the evaluation of two Fourier inversions, and is inaccurate for out-of-themoney options, due to cancellation, we do not discuss it here in further detail. Instead we focus on more recent approaches due to [3, 16], and [12].

Carr and Madan's approach was to consider the Fourier transform of the damped European call price with respect to the logarithm of the strike price:

$$\psi(v,\alpha) \equiv \int_{-\infty}^{\infty} e^{ivk} e^{\alpha k} C(k) dk$$
$$= \frac{\phi(v - i(\alpha + 1))}{-(v - i\alpha)(v - i(\alpha + 1))} \tag{3}$$

and subsequently invert this to arrive at the desired call price:

$$C(S(t), K, T) = \frac{e^{-\alpha k}}{2\pi} \int_{-\infty}^{\infty} e^{-\mathrm{i}vk} \psi(v, \alpha) \, \mathrm{d}v$$
$$= \frac{e^{-\alpha k}}{\pi} \int_{0}^{\infty} \mathrm{Re}(e^{-\mathrm{i}vk} \psi(v, \alpha)) \, \mathrm{d}v \tag{4}$$

In equations (3) and (4), *φ(u)* is the characteristic function; *φ(u)* = *Ɛ*[exp*(*i*u* ln *S(T ))*]. Sufficient conditions for equation (4) to exist are that the damping factor *α >* 1, and that the (*α* + 1)st moment of the asset, *φ(*−*(α* + 1*)*i*)*, is finite. The first condition is required to make the damped call price an L1 integrable function, which is a sufficient condition for the existence of its Fourier transform.

Whereas Carr and Madan took the Fourier transform with respect to the strike price of the call option, Raible [16] and Lewis [12] used an approach that is slightly more general in that it does not require the existence of a strike in a payoff. Raible took the transform with respect to the log-forward price, Lewis used the log-spot price. Note that for all three methods, the Fourier transform of the option price can be decoupled into two parts, a payoff-dependent part, the payoff transform, and a model-dependent part, the characteristic function.

One of the restrictions on the damping factor *α* for a call price is that it must be larger than 1. However, as Lewis [12] and Lee [9] point out, this is not a real restriction if we recast equation (4) as a contour integral in the complex plane. Shifting the contour, equivalent to varying *α* in equation (4), and carefully applying Cauchy's residue theorem leads to the following option pricing equation:

$$C(S(t), K, T, \alpha)$$
  
=  $R(F(t, T), K, \alpha)$ 

$$+\frac{\mathrm{e}^{-\alpha k}}{\pi}\int_{0}^{\infty}\mathrm{Re}(\mathrm{e}^{-\mathrm{i}vk}\psi(v,\alpha))\,\mathrm{d}v\tag{5}$$

where the residue term  $R(F, K, \alpha)$  equals 0 for  $\alpha >$ 0,  $1/2F$  for  $\alpha = 0$ , F for  $\alpha \in (-1, 0)$ ,  $F - 1/2K$ for  $\alpha = -1$ , and  $F - K$  for  $\alpha < -1$ . For values of  $\alpha < -1$ , for example, this means that the integral in equation  $(5)$  yields the value of a put, from which we obtain the price of a call *via* put-call parity.

As far as the numerical implementation of equation (5) goes, the appropriate numerical algorithm depends, as always, on the user's demands. If one is interested in the option price at a great many strike prices, equation (5) can be discretized in such a way that it is amenable to use of the fast Fourier transform (FFT), as detailed in [3] and in the article Fourier Transform. If one is calibrating a model to a volatility surface, one often only needs to evaluate option prices at a handful of strikes, at which point a direct integration of equation  $(5)$  becomes computationally advantageous. Important points to consider in approximating the semi-infinite integral in equation (5) are the discretization error, the truncation error, and the choice of contour or damping factor  $\alpha$ . Lee [9] extensively analyzes these choices when equation (5) is discretized using the discrete Fourier transform (DFT), and proposes a minimization algorithm to determine the parameters of the discretization.

Lord and Kahl [14] propose a different approach. If an appropriate transformation function is available that maps the semi-infinite interval into a finite one, the truncation error can be avoided altogether. This leaves the discretization error, which can be controlled by using adaptive integration methods. Finally, the speed and accuracy of the integration algorithm can be controlled by choosing an appropriate value of  $\alpha$ . A good proxy for the optimal value of  $\alpha$ , the value that minimizes the approximation error given a fixed computational budget, is

$$\alpha^* = \begin{array}{l} \arg \min \\ \alpha \in (\alpha_{\min}, \alpha_{\max}) \end{array} |e^{-\alpha k} \psi(0, \alpha)|$$
$$= \begin{array}{l} \arg \min \\ \alpha \in (\alpha_{\min}, \alpha_{\max}) \end{array} - \alpha k + \frac{1}{2} \ln(\psi(0, \alpha)^2) \quad (6)$$

where  $(\alpha_{\min}, \alpha_{\max})$  is the allowed range of  $\alpha$ , corresponding to  $\phi(-(\alpha+1)i) < \infty$ . This choice of contour is closely linked to how the optimal contour is chosen in saddlepoint approximations. That  $\alpha$ really can have a significant impact on the accuracy should become clear from the following example.

## Example 1—Impact of $\alpha$ on the Numerical Approximation in Heston's Model

As an example, we look at the impact of  $\alpha$  in Heston's stochastic volatility model (see **Heston Model**). The parameters we pick are  $\kappa = \omega = 1$ ,  $\rho = -0.7$ ,  $\theta =$  $v(0) = 0.1$ ,  $F = 1$ ,  $K = 1.5$  and the time to expiry is 0.1 years. Figure 1 shows the impact of  $\alpha$  on the approximation error when two different ways are used to discretize equation  $(5)$ .

If one plots the function that is minimized in equation (6), one obtains a very similar pattern, suggesting that  $\alpha^*$  is indeed close to optimal.

Finally, Andersen and Andreasen [2] and Cont and Tankov [4] have suggested that the Black-Scholes

![](_page_1_Figure_12.jpeg)

**Figure 1** Impact of  $\alpha$  using (a) Lee [9] DFT discretization, or (b) Gauss-Legendre quadratures. The various lines represent the number of abscissae used  $(8, 16, \text{ or } 32)$ 

option price could be used as a control variate in the evaluation of equation (5), that is, we could subtract the Black–Scholes integrand from the integrand, and subsequently add the Black–Scholes price back to the equation. While this could work for some models, the approach does require a good correspondence between both characteristic functions, and also requires an educated guess as to which Black–Scholes volatility should be used.

## **Pricing Bermudan and American Options**

Now that we can price European options using Fourier methods, the next question is whether options with early exercise features can be priced in a similar framework. The answer is in the affirmative. The first paper to attempt this in the framework of Carr and Madan was by O'Sullivan [18], who extended the QUAD method of [1] (see **Quadrature Methods**) to allow for models where the density is not known in closed form, but has to be approximated *via* Fourier inversion. This method has complexity O(*MN*2), where *M* is the number of time steps and *N* is the number of discretization points used in a onedimensional model.

Building upon a presentation by Reiner [17], Lord *et al.* [13] noticed that the key to extending Carr and Madan's approach to early exercise options was to abandon the idea of working with an analytical Fourier transform of the option payoff and to numerically approximate it. If at time *tm* we have an expression for the value of the option contract, then its continuation value at *tm*<sup>−</sup><sup>1</sup> can be obtained by calculating its convolution with the transition density. As we know the Fourier transform of a convolution is the product of the individual Fourier transforms, all we need to do is numerically calculate the Fourier transform of the continuation value. Having calculated the continuation value, we obtain the value at time *tm*<sup>−</sup><sup>1</sup> simply by comparison with the exercise value. The CONV method of Lord *et al.* [13] utilizes the FFT to approximate the convolutions. As such, the algorithm is O(*MN* log *N*). For Bermudan options, the algorithm is certainly competitive with the fastest partial integro-differential differential equation (PIDE) methods (*see* **Partial Integrodifferential Equations (PIDEs)**); see the numerical comparison in [13]. The prices of American options can be obtained *via* Richardson extrapolation. It is here that PIDE methods have an advantage. Another area where PIDE methods are advantageous is at the choice of gridpoints—as the CONV method employs the FFT, the grid for the logarithm of the asset price needs to be uniform. This makes it harder to place discontinuities on the grid, something which is much easier to achieve in, for example, the QUAD or PIDE methods. Extensions of the CONV method to multiple dimensions can be found in [10].

Finally, we mention a recent paper by Fang and Oosterlee [5], in which Bermudan options are efficiently priced *via* Fourier cosine series expansions. While this method is also O(*MN* log *N*) and has some similarities with the CONV method, a great advantage is that the exercise boundary is directly solved, as in the QUAD method. Hence, the cosine series coefficients can be calculated exactly, instead of being approximated, which is the case in the CONV method. Whereas the convergence of the CONV method is dictated by the chosen Newton–Cotes rule, the convergence of the COS method is dictated by the rate of decay of the characteristic function.

## **References**

- [1] Andricopoulos, A.D., Widdicks, M., Duck, P.W. & Newton, D.P. (2003). Universal option valuation using quadrature, *Journal of Financial Economics* **67**(3), 447–471.
- [2] Andersen, L.B.G. & Andreasen, J. (2002). Volatile volatilities, *Risk* **15**(12), 163–168.
- [3] Carr, P. & Madan, D.B. (1999). Option valuation using the Fast Fourier Transform, *Journal of Computational Finance* **2**(4), 61–73.
- [4] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman and Hall.
- [5] Fang, F. & Oosterlee, C.W. (2008). *Pricing Earlyexercise and Discrete Barrier Options by Fourier-cosine Series Expansions*, working paper, Delft University of Technology and CWI.
- [6] Gil-Pelaez, J. (1951). Note on the inversion theorem, *Biometrika* **37**, 481–482.
- [7] Gurland, J. (1948). Inversion formulae for the distribution of ratios, *Annals of Mathematical Statistics* **19**, 228–237.
- [8] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**(2), 327–343.
- [9] Lee, R.W. (2004). Option pricing by transform methods: extensions, unification and error control, *Journal of Computational Finance* **7**(3), 51–86.

## **4 Fourier Methods in Options Pricing**

- [10] Leentvaar, C.C.W. & Oosterlee, C.W. (2008). Multiasset option pricing using a parallel Fourier-based technique, *Journal of Computational Finance* **12**(1), 1–26.
- [11] Levy, P. (1925). ´ *Calcul des Probabilites*, Gauthier-Villars, Paris.
- [12] Lewis, A. (2001). *A Simple Option Formula for General Jump-diffusion and other Exponential L´evy Processes*, working paper, OptionCity.net, http://ssrn.com/abstract =282110.
- [13] Lord, R., Fang, F., Bervoets, F. & Oosterlee, C.W. (2008). A fast and accurate FFT-based method for pricing early-exercise options under Levy processes, ´ *SIAM Journal on Scientific Computing* **30**(4), 1678–1705.
- [14] Lord, R. & Kahl, C. (2007). Optimal Fourier inversion in semi-analytical option pricing, *Journal of Computational Finance* **10**(4), 1–30.
- [15] Madan, D.B. & Seneta, E. (1990). The variance gamma (V.G.) model for share market returns, *Journal of Business* **63**(4), 511–524.
- [16] Raible, S. (2000). *L´evy Processes in Finance: Theory, Numerics and Empirical Facts*. PhD thesis, Institut fur¨

Mathematische Stochastik, Albert-Ludwigs-Universitat, ¨ Freiburg.

- [17] Reiner, E. (2001). Convolution methods for pathdependent options, *Financial Mathematics Workshop*, Institute for Pure and Applied Mathematics, UCLA, January 2001, available at: http://www.ipam.ucla.edu/ publications/fm2001/fm2001 4272.pdf.
- [18] O'Sullivan, C. (2005). *Path Dependent Option Pricing under L´evy Processes*, EFA 2005 Moscow meetings paper, available at: http://ssrn.com/abstract=673424.

## **Related Articles**

**Fourier Transform**; **Partial Integro-differential Equations (PIDEs)**; **Quadrature Methods**; **Wavelet Galerkin Method**.

ROGER LORD
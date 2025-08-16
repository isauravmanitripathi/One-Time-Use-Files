# **Bates Model**

The Bates [3] and Scott [13] option pricing models were designed to capture two features of the asset returns: the fact that conditional volatility evolves over time in a stochastic but mean-reverting fashion, and the presence of occasional substantial outliers in the asset returns. The two models combined the Heston [9] model of stochastic volatility (see **Heston Model**) with the Merton [11] model of independent normally distributed jumps in the log asset price (see Jump-diffusion Models). The Bates model ignores interest rate risk, while the Scott model allows interest rates to be stochastic. Both models evaluate European option prices numerically, using the Fourier inversion approach of Heston (see also Fourier Transform and Fourier Methods in Options Pricing for a general discussion of Fourier transform methods in finance). The Bates model also includes an approximation for pricing American options (see American Options). The two models were historically important in showing that the tractable class of affine option pricing models includes jump processes as well as diffusion processes.

All option pricing models rely upon a risk-neutral representation of the data generating process that includes appropriate compensation for the various risks. In the Bates and Scott models, the riskneutral processes for the underlying asset price  $S_t$ and instantaneous variance  $V_t$  are assumed to be of the form

$$\begin{aligned} \mathrm{d}S_t/S_t &= (b - \lambda^* \overline{k}^*) \, \mathrm{d}t + \sqrt{V_t} \, \mathrm{d}Z_t + k^* \, \mathrm{d}q_t \\ \mathrm{d}V_t &= \left(\alpha - \beta^* V_t\right) \, \mathrm{d}t + \sigma_v \sqrt{V_t} \, \mathrm{d}Z_{vt} \end{aligned} \tag{1}$$

where  $b$  is the cost of carry;  $Z_t$  and  $Z_{vt}$  are Wiener processes with correlation  $\rho$ ;  $q_t$  is an integervalued Poisson counter with risk-neutral intensity  $\lambda^*$ that counts the occurrence of jumps; and  $k^*$  is the random percentage jump\_size, with a Gaussian distribution  $\ln(1+k^*) \sim N \left[ \ln(1+\overline{k}^*) - \frac{1}{2}\delta^2, \delta^2 \right]$  conditional upon the occurrence of a jump. The Bates model assumes  $b$  is constant, while the Scott model assumes it is a linear combination of  $V_t$  and an additional state variable that follows an independent square-root process. Bates [3] examines foreign currency options, for which  $b$  is the domestic/foreign interest differential, while Scott's application [13] to nondividend paying stock options implies the cost of carry is equal to the risk-free interest rate

The postulated process has an associated conditional characteristic function that is exponentially affine in the state variables. For the Bates model, the characteristic function is

$$\varphi(\mathrm{i}\Phi) = E_0^*[e^{\mathrm{i}\Phi S_T}|S_0, V_0, T]$$
  
=  $\exp\left[\mathrm{i}\Phi S_0 + C(T; \mathrm{i}\Phi) + D(T; \mathrm{i}\Phi) V_0$   
 $+ \lambda^* TE\left(\mathrm{i}\Phi\right)\right]$  (2)

where  $E_0^*[\cdot]$  is the risk-neutral expectational operator associated with equation  $(1)$ , and

$$\gamma(z) = \sqrt{(\rho \sigma_v z - \beta^*)^2 - \sigma_v^2 (z^2 - z)}$$
 (3)

$$C(T; z) = bTz - \frac{\alpha T}{\sigma_v^2} [\rho \sigma_v z - \beta^* - \gamma(z)] - \frac{2\alpha}{\sigma_v^2}$$
$$\times \ln \left\{ 1 + [\rho \sigma_v z - \beta^* - \gamma(z)] \frac{1 - e^{\gamma(z)T}}{2\gamma(z)} \right\} \tag{4}$$

$$D(T;z) = \frac{z^2 - z}{\gamma(z)T + 1} + \beta^* - \rho \sigma_v z$$
(5)  
$$E(z) = \left(1 + \overline{k}^*\right)^z e^{\frac{1}{2}\delta^2(z^2 - z)} - 1 - \overline{k}^* z$$
(6)

The terms  $C(\cdot)$  and  $D(\cdot)$  are identical to those in the Heston [9] stochastic volatility model, while  $E(\cdot)$  captures the additional distributional impact of jumps. Scott's generalization to stochastic interest rates uses an extended Fourier transform of the form

$$\varphi^*(z)$$
  
=  $E_0^* \left[ \exp\left(-\int_0^T r_t \mathrm{d}t + z \ln S_T\right) | S_0, r_0, V_0, T\right]$   
(7)

which has an analytical solution for complex-valued  $z$  that is also exponentially affine in the state variables  $S_0$ ,  $r_0$ , and  $V_0$ .

European call option prices take the form  $c =$  $B(FP_1 - XP_2)$ , where B is the price of a discount bond of maturity  $T, F$  is the forward price on the underlying asset,  $X$  is the option's exercise price, and

 $P_1$  and  $P_2$  are upper tail probability measures derivable from the characteristic function. The papers of Bates [3] and Scott [13] present Fourier inversion methods for evaluating  $P_1$  and  $P_2$  numerically. However, faster methods were subsequently developed for directly evaluating European call options, using a single numerical integration of the form

$$c = BF - BX$$

$$\times \left\{ \frac{1}{2} + \frac{1}{\pi} \int_0^\infty \text{Re} \left[ \frac{f(\text{i}\Phi)\text{e}^{-\text{i}\Phi\ln X}}{\text{i}\Phi(1-\text{i}\Phi)} \right] \text{d}\Phi \right\} \tag{8}$$

where  $\text{Re}[z]$  is the real component of a complex variable  $z$  (see Fourier Methods in Options Pricing). For the Bates model,  $f(i\Phi) = \varphi(i\Phi)$ ; for the Scott model,  $f(i\Phi) = \varphi^*(i\Phi)/B$ . European put options can be evaluated from European call option prices using the put-call parity relationship  $p = c + B(X - F)$ (*see* **Put–Call Parity** for details on put-call parity).

Evaluating equation (8) typically involves integration of a dampened oscillatory function. While there exist canned programs for integration over a semiinfinite domain, most papers use various forms of integration over a truncated domain. Bates [3] uses Gauss-Kronrod quadrature (see Quadrature Methods). Fast Fourier transform approaches have also been proposed, but these involve substantially more functional evaluations. The integration is typically well behaved, but there do exist extreme parameter values (e.g.,  $|\rho|$  near 1) for which the path of integration crosses the branch cut of the log function. As all contemporaneous option prices of a given maturity use the same values of  $f(i\Phi)$  regardless of the strike price  $X$ , evaluating options jointly greatly increases numerical efficiency.

### **Related Models**

Related affine models can be categorized along four lines:

- 1. alternate specifications of jump processes;
- 2. the Bates [5] extension to stochastic-intensity jump processes;
- 3. models in which the underlying volatility can also jump; and
- 4. multifactor specifications.

Alternate jump specifications (including Lévy processes) with independent and identically distributed jumps involve modification of the functional form of  $E(\cdot)$ , and are discussed in other articles: **Temp**ered Stable Process; Normal Inverse Gaussian Model; Variance-gamma Model; Kou Model; Exp**onential Lévy Models**). The Bates [5] model with (risk-neutral) stochastic jump intensities of the form  $\lambda^* + \lambda_1^* V_t$  involves modifying  $\gamma(\cdot)$  and  $D(\cdot)$ :

$$\gamma(z) = \sqrt{(\rho \sigma_v z - \beta^*)^2 - \sigma_v^2 [z^2 - z + 2\lambda_1^* E(z)]}$$
(9)

$$D(T;z) = \frac{z^2 - z + 2\lambda_1^* E(z)}{\gamma(z) \frac{e^{\gamma(z)T} + 1}{e^{\gamma(z)T} - 1} + \beta^* - \rho \sigma_v z}$$
(10)

See also **Time-changed Lévy Process** for other stochastic-intensity jump models.

Bates [5] also contains multifactor specifications for the instantaneous variance and jump intensity. The general class of affine jump-diffusion models is presented in [8], including the volatility-jump option pricing model. Scott's extended Fourier transform approach for stochastic interest rates was subsequently also used by Bakshi and Madan [2] and Duffie et al. [8]

#### **Further Reference Material**

Bates [7, pp. 943-4] presents a simple derivation of equation (8), and cites earlier papers that develop the single-integration approach. Numerical integration issues are discussed by Lee [10]. Bates [3] and Bakshi *et al.* [1] estimate and test the Bates and Scott models, respectively, while Pan [12] provides additional estimates and tests of the Bates [5] stochasticintensity model. Bates [4, 6] surveys empirical option pricing research.

# References

- Bakshi, G., Cao, C. & Chen, Z. (1997). Empirical per- $[1]$ formance of alternative option pricing models, Journal of Finance 52, 2003–2049.
- Bakshi, G. & Madan, D.B. (2000). Spanning and [2] derivative-security valuation, Journal of Financial Economics 55, 205-238.

- [3] Bates, D.S. (1996). Jumps and stochastic volatility: exchange rate processes implicit in PHLX deutschemark options, *Review of Financial Studies* **9**, 69–107.
- [4] Bates, D.S. (1996). Testing option pricing models, in *Handbook of Statistics*, G.S. Maddala & C.R. Rao, eds, (Statistical Methods in Finance), Elsevier, Amsterdam, Vol. 14, pp. 567–611.
- [5] Bates, D.S. (2000). Post-'87 crash fears in the S&P 500 futures option market, *Journal of Econometrics* **94**, 181–238.
- [6] Bates, D.S. (2003). Empirical option pricing: a retrospection, *Journal of Econometrics* **116**, 387–404.
- [7] Bates, D.S. (2006). Maximum likelihood estimation of latent affine processes, *Review of Financial Studies* **19**, 909–965.
- [8] Duffie, D., Pan, J. & Singleton, K.J. (2000). Transform analysis and asset pricing for affine jump-diffusions, *Econometrica* **68**, 1343–1376.
- [9] Heston, S.L. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–344.

- [10] Lee, R.W. (2004). Option pricing by transform methods: extensions, unification and error control, *Journal of Computational Finance* **7**, 51–86.
- [11] Merton, R.C. (1976). Option pricing when underlying stock returns are discontinuous, *Journal of Financial Economics* **3**, 125–144.
- [12] Pan, J. (2002). The jump-risk premia implicit in options: evidence from an integrated time-series study, *Journal of Financial Economics* **63**, 3–50.
- [13] Scott, L.O. (1997). Pricing stock options in a jumpdiffusion model with stochastic volatility and interest rates: applications of Fourier inversion methods, *Mathematical Finance* **7**, 413–426.

## **Related Articles**

**Barndorff-Nielsen and Shephard (BNS) Models**; **Heston Model**; **Jump-diffusion Models**; **Stochastic Volatility Models: Foreign Exchange**; **Timechanged Levy Process ´** .

DAVID S. BATES
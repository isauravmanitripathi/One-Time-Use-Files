# **Tempered Stable Process**

A tempered stable process is a pure-jump Levy process (see Lévy Processes) with infinite activity (see **Exponential Lévy Models**) whose small jumps behave like a stable process, while the large jumps are "tempered" so that the tail of the density decays exponentially. Tempered stable processes can be constructed from stable processes by exponential tilting (*see Esscher Transform*) of the Levy measure.

Tempered stable processes were introduced in [8] and introduced in financial modeling by Cont et al. [4] under the name truncated stable process, where it was noted that tempered stable processes have a short-time behavior similar to stable Levy processes while retaining finite variance and finite exponential moments. Option pricing with tempered stable processes was studied in [1], [2], and [5].

The best known example of tempered stable processes is the CGMY process introduced in [2], which is a pure-jump Levy process with Levy density given by

$$k_{\text{CGMY}} = C \frac{\exp(-G|x|)}{|x|^{1+Y}} 1_{\{x<0\}} + C \frac{\exp(-M|x|)}{|x|^{1+Y}} 1_{\{x>0\}}$$
(1)

The model parameters of equation (1) fulfill  $C >$  $0, G, M \ge 0$ , and  $Y \in (-\infty, 2)$ . The restriction on the parameter  $Y$  ensures that the measure is a Lévy measure.

For a given stochastic process  $X(t)$ , its characteristic function is given by  $\Phi(u,t) = \mathbb{E}[\exp$  $(iuX(t))]$  (see Fourier Transform; Fourier Methods in Options Pricing). For the CGMY model, it is derived in  $[2]$  and it is given by

$$\Phi(u,t) = \exp(tC \Gamma(-Y)((M - iu)^Y - M^Y)$$
$$+ (G + iu)^Y - G^Y)$$
(2)

On this basis, Fourier-transform methods (see Fourier Transform; Fourier Methods in Options **Pricing**) can be applied to option pricing. Carr et al. show that the CGMY process has completely monotone Lévy density for  $Y > -1$  and is of infinite activity for  $Y > 0$ . The drift parameter is chosen to make  $S(t)$  into a martingale and can be determined by using equation (2), which leads to  $\omega = -\ln(\Phi(-i)).$ Further methods to compute an equivalent martingale measure are discussed in  $[7]$ .

#### **Tempered Stable**

The CGMY process is a special case of the tempered stable process considered in Boyarenko and Levendorskii [1], Cont and Tankov [5] or Rosinski [12]. The latter process has Lévy measure with density given by

$$k_{\rm TS} = C_{-} \frac{\exp(-G|x|)}{|x|^{1+Y_{-}}} 1_{\{x<0\}} + C_{+} \frac{\exp(-M|x|)}{|x|^{1+Y_{+}}} 1_{\{x>0\}}$$
(3)

The parameters of equation (3) fulfill  $G, M >$ 0,  $C_{\pm} > 0$ , and  $Y_{\pm} \in (-\infty, 2)$ . The characteristic function is available in closed form and hence option pricing and calibration can be performed using Fourier-transform methods. Choosing  $C_{-} = C_{+}$  and  $Y_{-} = Y_{+}$  leads to the CGMY process and  $Y_{-} = Y_{+} =$ 0 leads to a variance gamma process (see Variancegamma Model).

#### **Interpretation of the Parameters**

In order to show the impact of the model parameters to asset returns, we consider the properties of the process  $X(t)$ . Increasing C makes the density more peaked while decreasing  $C$  flattens it.  $C$  controls the frequency of jumps. While determining the probability of jumps larger than a certain level, this parameter is incorporated. The parameter  $Y$  governs the fine structure of the process and the choice affects the overall properties of the process as explained in the previous section. It determines if the process is of finite or infinite activity.

The parameters  $G$  and  $M$  control the rate of exponential decay, that is, the tail behavior, on the right and the left of  $k_{\text{CGMY}}$ . We consider three cases:  $G = M$  leads to a symmetric Lévy measure,  $G < M$ makes the left tail heavier than the right one, and *vice versa* for the case  $G > M$ . The last two cases lead to a skewed distribution.

This behavior is illustrated in Figure 1.

![](_page_1_Figure_1.jpeg)

Figure 1 Illustration of the effect of changing the CGMY model parameters  $C, G, M$ , and  $Y$  on the probability density function

If variance, skewness, and kurtosis exist, they can be computed by

Variance = 
$$C\Gamma(2 - Y) \left(\frac{1}{M^{2-Y}} + \frac{1}{G^{2-Y}}\right)$$
 (4)

Skewness = 
$$\frac{C\Gamma(3-Y)\left(\frac{1}{M^{3-Y}} + \frac{1}{G^{3-Y}}\right)}{V^{3/2}}$$
 (5)

$$\text{Kurtosis} = \frac{C\Gamma(4-Y)\left(\frac{1}{M^{4-Y}} + \frac{1}{G^{4-Y}}\right)}{V^2} \tag{6}$$

The equations for the higher moments suggest that the parameter  $C$  controls the overall size of the moments. This has already been verified by the expression for the density. In the case  $\int_{\mathbb{R}} k(x) dx <$  $+\infty$ , it can be interpreted as a measure for the overall level of activity. In the case of finite activity, the process has a finite number of jumps on every compact interval.

## **Pricing and Calibration**

We can use the characteristic function of the log-price  $X(t)$  from equation (2) to apply Fourier methods described in Carr and Madan [3] or Eberlein et al. [6] to price European and path-dependent options (see Fourier Methods in Options Pricing).

Options may also be priced by Monte Carlo simulation  $[10, 11]$  using the representation of the tempered stable process as a subordinated Brownian motion  $[5,$  Proposition  $4.1]$ .

In contrast to the diffusion processes, for the pure-jump processes, the change in measure can be computed from the statistical measure, that is, using parameters computed from time-series data and riskneutral measure, that is, using parameters obtained using quoted option prices. It holds that  $k_{\tilde{p}}(x) =$  $Y(x)k_{\mathbb{P}}$ ; see [2] for details. Let us call the corresponding parameter sets  $\mathcal{P} = \{C, G, M, Y, \mu\}$  and  $\mathcal{P} =$  $\{\tilde{C}, \tilde{G}, \tilde{M}, \tilde{Y}, r\}$ , where r denotes the riskless rate and the corresponding measures by  $\mathbb{P}$  and  $\mathbb{P}$  respectively. If the characteristic functions are denoted by  $\Phi$  and

 $\tilde{\Phi}$  then using the results in [2] state that  $\tilde{\mathbb{P}}$  is an equivalent martingale measure to  $\mathbb{P}$  if and only if  $C = \tilde{C}, Y = \tilde{Y}$ , and  $r - \Phi(-i) = \mu - \tilde{\Phi}(-i)$ . The constraints on the parameters  $G, M, \tilde{G}$ , and  $\tilde{M}$  are implicit in the last equality.

# **Path Properties**

Path properties of the model affect the prices of exotic path-dependent options. We considered path variation when we gave the interpretation for the model parameters. Other concepts like hitting points, creeping, or regularity of the halfline are considered in [9]. We shortly introduce hitting points. The process  $X_t$  can hit a point  $x \in \mathbb{R}$  if  $\mathbb{P}(X_t = x \text{ for at least one } t > 0) > 0$ . We denote the set of all points the process can hit by  $H = \{x \in \mathbb{R} | \mathbb{P}(X_t = x \text{ for at least one } t > 0) > 0 \}.$ See  $[9]$  for details.

## References

- $\lceil 1 \rceil$ Boyarchenko, S.I. & Levendorskii, S.Z. (2002). Non-Gaussian Merton-Black-Scholes theory, Advanced Series on Statistical Science and Applied Probability, World Scientific, River Edge, NJ, Vol. 9.
- Carr, P., Geman, H., Madan, D. & Yor, M. (2002). The [2] fine structure of asset returns: an empirical investigation, Journal of Business 75(2), 305-332.
- [3] Carr, P. & Madan, D. (1999). Option valuation using the fast Fourier transform, Journal of Computational Finance  $2(4)$ ,  $61-73$ .
- Cont, R., Potters, M. & Bouchaud, J.P. (1997). Scal-[4] ing in stock market data: stable laws and beyond, in Scale Invariance and Beyond. B. Dubrulle, F. Graner & D. Sornette, eds, Springer.

- [5] Cont, R. & Tankov, P. (2003). Financial Modelling with Jump Processes, Chapman and Hall / CRC Press.
- [6] Eberlein, E., Glau, K. & Papapantoleon, A. (2008) Analysis of Valuation Formulae and Applications to *Exotic Options.. Preprint Uni Freiburg*, www.stochastic. uni-freiburg.de/~eberlein/papers/Eberlein-glau.Papapan. pdf
- Kim, Y.S. & Lee, J.H. (2007). The relative entropy in [7] CGMY processes and its applications to finance, *Mathe*matical Methods of Operations Research 66(2),  $327 - 338.$
- [8] Koponen, I. (1995). Analytic approach to the problem of convergence of truncated Lévy flights towards the Gaussian stochastic process, Physical Review E 52, 1197-1199.
- Kyprianou, A.E. & Loeffen, T.L. (2005). Lévy processes [9] in finance distinguished by their coarse and fine path properties, in Exotic Option Pricing and Advanced Lévy models, A.E. Kyprianou, W. Schoutens & P. Wilmott, eds. Wiley. Chichester.
- [10] Madan, D. & Yor, M. (2005). CGMY and Meixner Subordinators are Absolutely Continuous with Respect to One Sided Stable Subordinators. Prépublication du Laboratoire de Probabilités et Modèles Aléatoires.
- [11] Poirot, J. & Tankov, P. (2006). Monte Carlo option pricing for tempered stable (CGMY) processes. Asia Pacific Financial Markets 13(4), 327-344.
- [12] Rosinski, J (2007). Tempering stable processes, Stochastic Processes and their Applications, 117(6), 677–707.

# **Related Articles**

Exponential Lévy Models; Fourier Methods in Options Pricing; Fourier Transform; Lévy Processes; Time-changed Lévy Process.

JÖRG KIENITZ
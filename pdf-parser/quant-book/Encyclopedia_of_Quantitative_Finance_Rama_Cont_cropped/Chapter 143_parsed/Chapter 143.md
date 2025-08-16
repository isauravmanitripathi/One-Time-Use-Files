# **Dividend Modeling**

A dividend is a portion of a company's earnings paid to its shareholders. In the process of dividend payment, the following stages are distinguished: (i) declaration date, when the dividend size and the ex-dividend date are announced; (ii) ex-dividend date, when the share starts trading net of dividend; (iii) record date, when holders eligible to dividend payment are identified; and (iv) payment date, when delivery is made. At the ex-dividend date, the stock price drops by an amount proportional to the size of the dividend; the proportionality factor depends on the tax regulations. There are a lot of issues, research streams, and approaches in dividend modeling; here the issue is considered mainly in the context of option pricing theory.

The usual way to price derivatives on dividendpaying stocks is to take a model for non-dividendpaying stocks and extend it to take the dividends into account. The dividends then are commonly modeled as (i) continuously paid dividend yield, (ii) proportional dividends (known fractions of the stock price) paid at known discrete times, or (iii) fixed dividends (known amounts), paid at known discrete times. It is also possible to model the dividend amounts and the dividend dates stochastically (though there is evidence that this has a negligible impact on vanilla options [10]). In fact, there is an alternative approach where the stochastic dividends are the primary quantities and the stock followed by option price are derived from these, which was pioneered in [9]. As usual, one has to choose the complexity of the model depending on dividend exposure of the derivative to be priced.

In practice, one comes across the notion of implied dividends: the value of the dividends (independent of how they are modeled) can be inverted from the synthetic forward or future contract; the fact that one can get quite different (from analyst predictions) numbers reflects various uncertainties. Among them are the sundry tax regulations in different countries for various market players, timing, and value of the dividends, just to name a few.

The impact of dividends can be illustrated, starting simply by adding a continuous dividend yield to the drift. For the sake of the simplicity of notations, it is written in lognormal terms:

$$dS_t = (r - q)S_t dt + \sigma S_t dW_t \tag{1}$$

This approach is especially popular when modeling options on indexes, where dividend payments are numerous and spread through time. Another choice, of proportional amounts *di* = *fiSti* paid at exdividend dates *t*<sup>1</sup> *< t*<sup>2</sup> *<* ··· for single shares, can be justified by the fact that dividends tend to increase when a company is doing well, which is correlated with a high share price:

$$dS_t = (r - Q_t)S_t dt + \sigma S_t dW_t \text{ with}$$
  
$$Q_t = \sum_i \delta(t - t_i) f_i$$
 (2)

In both these cases, the stock price at each time still has a lognormal distribution, so the prices of European options are given by straightforward modifications of the Black–Scholes (BS) pricing formula. This is no longer true, however, for discrete cash dividends:

$$dS_t = (rS_t - D_t) dt + \sigma S_t dW_t \text{ with}$$
  
$$D_t = \sum_i \delta(t - t_i) d_i \qquad (3)$$

The stock price *St* jumps down with the amount of dividend *di* paid at time *ti* and between the dividends it follows a geometric Brownian motion. In this setting, the stock price can become negative, but this is usually so unlikely that, in practice, it is not a problem. Still, one might want to use a more robust dividend policy in the model, such as capping the dividend at the stock price. Obviously, different dividend policies result in different option prices [7].

# **Impact on Option Pricing**

To compute an option price under equation (3) the standard collection of numerical methods can be employed: finite difference (FD) method with jump conditions across ex-dividend date [11], Monte Carlo simulations, or nonrecombining trees [8]. There is no real closed-form solution with multiple dividends for European option under equation (3); however, several approximations are available. All of them are based on bootstrapping, that is, repeatedly computing the convolution of the option value at one dividend date with the density kernel from that date to the previous dividend date and applying the jump condition at the dividend dates, starting from the payoff at maturity. One can use a piecewise linear or a more sophisticated approximation of the option value at each convolution step and enjoy having a finite sum of closed-form solutions. On the basis of the fact that diffusion preserves monotonicity and convexity, it can be shown that the result converges to the true value (unpublished work of Amaro de Matos *et al.*). Another choice of parameterization was made in [7]: at each step of the integration the option value is approximated by BS-like function where strike and volatility are adjusted to obtain the best fit. Such methods can be used for any underlying process where one can compute the density kernel (Green function, propagator) for the convolution, though it will probably be not much faster or more accurate than employing the standard finite difference method, especially in the case of multiple dividends. For the handling of American options, one can find an extensive list of references in  $[4]$  and the relation between early exercise and dividends is explained in American Options; Finite Difference Methods for Early **Exercise Options** or [8].

### A Common Approach

As already pointed out in the discrete cash dividend model (3), the price of a European option has no closed-form solution and trees do not recombine. In order to remedy this, traders often split the stock price into a risky net-dividend part and a deterministic dividend part:

$$\begin{aligned} \mathrm{d}\tilde{S}_{t} &= r\,\tilde{S}_{t}\,\mathrm{d}t + \tilde{\sigma}\,\tilde{S}_{t}\,\mathrm{d}t \\ S_{t} &= \tilde{S}_{t} + \tilde{D}_{t} \\ \tilde{D}_{t} &= \tilde{D}_{t}^{\mathrm{fut}} - \tilde{D}_{t}^{\mathrm{past}} \\ \tilde{D}_{t}^{\mathrm{fut}} &= \sum_{t < t_{i} \leq T} \alpha_{i}d_{i}\mathrm{e}^{-r(t_{i}-t)} \\ \tilde{D}_{t}^{\mathrm{past}} &= \sum_{0 < t_{i} \leq t} (1 - \alpha_{i})d_{i}\mathrm{e}^{-r(t_{i}-t)} \end{aligned} \tag{4}$$

Note that the dependence on the option maturity  $T$ in the notation  $\tilde{D}_{t}^{\text{fut}}$  is suppressed. The most common choices used by practitioners  $[3, 5]$  are

$$\alpha_i = 1$$
 so  $\tilde{D}_t = \sum_{t < t_i \leq T} d_i e^{-r(t_i - t)}$  (6)

$$\alpha_i = 0 \quad \text{so} \quad \tilde{D}_t = \sum_{0 < t_i \le t} d_i e^{-r(t_i - t)} \tag{7}$$

$$\alpha_i = 1 - \frac{t_i}{T} \tag{8}$$

In this approach, the tree for  $\tilde{S}_t$  is recombining (see **Binomial Tree** or [8]), and the price of a European option is again given by a BS type formula, where the spot and the strike are adjusted as  $S_0 \rightarrow S_0 - \tilde{D}_0^{\text{fut}}$ and  $K \to K + \tilde{D}_T^{\text{past}}$ . Needless to say, however, the volatility for each of these processes will be different. Namely, choice (6) underestimates and choice (7) overestimates the volatility compared to the "true" model  $(3)$ ; the weighted choice  $(8)$  aims to minimize this effect.

## Arbitrage Opportunities

In reference [1], it was shown that arbitrage opportunities exist in the most standard approach  $(6)$  if the volatility surface is continuously interpolated around ex-dividend dates. They apply a rough volatility adjustment to prevent the arbitrage opportunities. The following example demonstrates that the continuous interpolation of volatility around ex-dividend dates can lead to significant mispricing. Figure 1 shows

![](_page_1_Figure_13.jpeg)

Figure 1 Price of an American call as a function of the time to maturity  $T$  for the following models: (3) (solid line),  $(6)$  (dotted line), and  $(6)$  with the volatility adjustment (10) (dashed line). The parameters are  $S_0 = 100$ ,  $K = 100$ ,  $r = 0.05, \, \sigma = 0.3, \, d_i = 8, \, \text{and} \, t_i = i - \frac{1}{2}$ 

the price of an American call as a function of the time to maturity  $T$  for different models. Given a flat volatility, the prices under equation (6) jump down after an ex-dividend date, which is not realistic, because a risk-free profit can be locked in by selling an option maturing just before the ex-dividend date and by buying a similar option maturing just after the ex-dividend date. Although the mispricing under equation (6) is most evident for American options, it is equally present in the valuation of European options. Note that equation (4) produces continuous prices around dividend payments and the price differences between the two models increase dramatically with maturity (see  $[1, 5]$  for similar results). Another primitive pitfall with equation  $(6)$  is to use constant extrapolation of the implied volatility to longer maturities. For example, if the present value of dividends of a long-term contract is half of the current stock price, then with simple flat term structure extrapolation one will underestimate the volatility by a factor of at least one and a half [2].

### **Volatility Adjustments**

To understand the difference in terms of volatility for the specified models, consider the local volatility model. Substitution of equation  $(4)$  into equation  $(3)$ yields the result that  $\tilde{S}$  follows the process with local volatility

$$\tilde{\sigma}(\tilde{S},t) = \left(1 + \frac{\tilde{D}_t}{\tilde{S}}\right)\sigma\tag{9}$$

It is handy to translate this result into implied terms [6]. Following the line of reasoning presented in [2], a slightly generalized result for the implied volatility can be derived:

$$\tilde{\sigma}^2 \approx \sigma^2 + \sigma \sqrt{\frac{\pi}{2T}} A \tag{10}$$

where

$$A = 4e^{\frac{b_1^2}{2} - s} \sum_i \tilde{d}_i \bigg( \omega_i \left[ \mathcal{N}(b_1) - \mathcal{N}(b_1 - \xi_i) \right]$$
  
+  $\tilde{\omega}_i \left[ \mathcal{N}(b_2) - \mathcal{N}(b_1 - \xi_i) \right] \bigg)$   
+  $e^{\frac{c_1^2}{2} - 2s} \sum_{i,j} \tilde{d}_i \tilde{d}_j \bigg( \omega_i \omega_j \left[ \mathcal{N}(c_1) - \mathcal{N}(c_1 - \psi_{ij}) \right]$   
-  $\tilde{\omega}_i \tilde{\omega}_j \left[ \mathcal{N}(c_2) - \mathcal{N}(c_1 - \psi_{ij}) \right]$   
+  $\Omega_{ij} \left[ \mathcal{N}(c_1 - \Psi_{ij}) - \mathcal{N}(c_1 - \psi_{ij}) \right] \bigg)$  (11)

with  $s = \ln(S_0 - \tilde{D}_0^{\text{fut}}), k = \ln(K + \tilde{D}_T^{\text{past}}) - rT, x_t = (s + (k - s)\frac{t}{T}) + rt, y_t = \frac{t(T - t)}{T}, \tilde{\omega}_i = 1 - \omega_i, \tilde{d}_i = d_i e^{-rt_i}, a = \frac{s - k}{\sigma\sqrt{T}}, b_{1/2} = a \pm \frac{\sigma\sqrt{T}}{2}, c_{1/2} = a \pm \sigma\sqrt{T}, \xi_i = \sigma\frac{t_i}{\sqrt{T}}, \psi_{ij} = 2\min(\xi_i, \xi_j), \Psi_{ij} = 2\max(\xi_i, \xi_j),$  $\Omega_{ij} = \omega_i \tilde{\omega_j} 1_{t_i > t_j} + \omega_j \tilde{\omega_i} 1_{t_j > t_i}.$ 

This gives a very simple and quick way of switching between models for trading practice as well as for understanding the essence of the feature. Moreover, it can be used independently of the option type. To give an idea of the quantitative value of presented methods, some numerical results with and without volatility adjustment are summarized in Table 1. All results are compared to the numerical solution calculated with the FD method. Bootstrapping with the piecewise linear interpolation converges to FD with sufficiently many points; HHL approximation of [7] differs a bit, probably due to the fact that the BS-like formula cannot exactly fit the shape of the integrand. Clearly, even in approximate form, equation  $(10)$ gives a fair correction in all cases, performing especially well for the weighted model (8).

When pricing equity derivatives, one should be aware that these instruments can be sensitive to

**Table 1** European call prices with parameter set of Figure 1 for different strikes. HHL refers to the approximation of [7]; FD to finite difference and BS to closed-form solution

| Strike |              |               | BS for $(6)$ |             |              | BS for $(8)$ |  |
|--------|--------------|---------------|--------------|-------------|--------------|--------------|--|
|        | $FD$ for (3) | $HHL$ for (3) | BS for $(6)$ | with $(10)$ | BS for $(8)$ | with $(10)$  |  |
| 50     | 33.509       | 33.641        | 29.908       | 33.312      | 33.547       | 33.497       |  |
| 80     | 22.482       | 22.559        | 17.846       | 22.414      | 22.304       | 22.473       |  |
| 100    | 17.393       | 17.428        | 12.772       | 17.404      | 17.102       | 17.388       |  |
| 120    | 13.573       | 13.575        | 9.250        | 13.644      | 13.209       | 13.573       |  |
| 150    | 9.511        | 9.479         | 5.836        | 9.635       | 9.099        | 9.515        |  |

dividends. Examples are exotic options on stocks and derivatives involving realized volatility, such as variance swaps (*see* **Variance Swap**), volatility swaps (*see* **Volatility Swaps**), correlation swaps (*see* **Correlation Swap**), and gamma swaps (*see* **Gamma Swap**). This sensitivity determines the required sophistication in dividend modeling. Adding dividends to a stock price process may seem trivial at first glance, but one has to be careful in setting the model parameters. The resulting model can then be solved by the usual methods. For the plain vanilla option with dividends, a number of numerical approximations have been developed.

## **References**

- [1] Beneder, R. & Vorst, T. (2001). Options on dividends paying stocks, in *Recent Developments in Mathematical Finance*, World Scientific Printers, Shanghai, pp. 204–217.
- [2] Bos, R., Gairat, A. & Shepeleva, A. (2003). Dealing with discrete dividends, *Risk* **16**, 109–112.
- [3] Bos, M. & Vandermark, S. (2002). Finessing fixed dividends, *Risk* **15**, 157–158.
- [4] Cassimon, D., Engelen, P.J., Thomassen, L. & Van Wouwe, M. (2007). Closed-form valuation of American

call options on stocks paying multiple dividends, *Finance Research Letters* **4**, 34–48.

- [5] Frishling, V. (2002). A discrete question, *Risk* **15**, 115–116.
- [6] Gatheral, J. (2006). *The Volatility Surface*, John Wiley & Sons, Hoboken, pp. 13–14.
- [7] Haug, E., Haug, J. & Lewis, A. (2003). Back to basics: a new approach to the discrete dividend problem, *Wilmott Magazine* (September), 37–47.
- [8] Hull, J.C. (2006). *Options, Futures and Other Derivatives*, 6th Edition, Prentice-Hall, Upper Saddle River.
- [9] Korn, R. & Rogers, L.C.G. (2005). Stocks paying discrete dividends: modeling and option pricing, *Journal of Derivatives* **13**(2), 44–48.
- [10] Kruchen, S. (2005). *Dividend Risk* , thesis, Uni/ETH, Zurich. ¨
- [11] Tavella, D. & Randall, C. (2000). *Pricing Financial Instruments. The Finite Difference Method*, John Wiley & Sons, New York.

## **Related Articles**

**American Options**; **Finite Difference Methods for Early Exercise Options**; **Local Volatility Model**; **Monte Carlo Simulation**.

ANNA SHEPELEVA & ALAIN VERBERKMOES
## **Discretely Monitored** Options

Traditional pricing models for path-dependent options rely on continuously monitoring the underlying, often resulting in closed-form or analytic formulas. References include [14, 19, 20, 21] for barrier options, [6, 12, 13] for look-back options, and [11, 18] for Asian or average options. However, in practice, monitoring is performed over discrete dates (e.g., monthly, weekly, or daily), while the underlying is still assumed to follow a continuous model. In contrast to continuous monitoring, discrete monitoring rarely, if ever, leads to similarly tractable solutions and using continuous monitoring as approximation for discrete monitoring often leads to significant mispricing (cf. [5, 15, 16].) As a consequence, various approaches have been followed to arrive at practically useful computational schemes.

For illustration, we focus on a down-and-out call option, where a standard call option with strike  $K$ is canceled if the underlying falls below a barrier prior to expiry  $T$ . We first assume the traditional Black-Scholes-Merton setup with the price  $\{S_t\}$ of the underlying following a geometric Brownian motion

$$S_t = S_0 e^{B_t} \tag{1}$$

where  $\{B_t\}$  is a Brownian motion with drift  $r$  –  $\sigma^2/2$  and standard deviation  $\sigma$ . Here the parameters r and  $\sigma$  represent the prevailing risk-free rate and the return volatility of the underlying asset, respectively. Let  $H > 0$  be a given constant (barrier) and assume  $H < S_0$ . With monitoring effected over a set of *m* dates  $n\Delta t$  (*n* =  $1,\ldots,m)$  such that  $\Delta t = T/m$ , let  $U_n = X_1 + X_2 +$  $\cdots + X_n$ , where the  $X_i$ s are independent normal random variables with mean  $\mu = (r - \sigma^2/2) \Delta t$  and standard deviation  $\tilde{\sigma} = \sigma \sqrt{\Delta t}$ . Then the call is knocked-out the first (random) time  $\tau \in \{1, 2, \ldots, m\}$ such that  $H \geq S_{\tau}$  and the time-0 price of such a call is

$$V_m(H) = e^{-rT} E \left( S_0 e^{U_m} - K \right)^+ 1_{\{\tau > m\}} \tag{2}$$

where  $\tau = \inf\{n : U_n \leq \log(H/S_0)\}\.$  The main source of the evaluation of the above expectation

is the computational complexity associated with an  $m$ -variate normal distribution for even moderate values of  $m$ . For example, Monte Carlo or tree-based algorithms may take several hours or even days for common values of  $m$  [4]. In their paper, Broadie et al. [3] (see also [17]), opt to circumvent this hurdle by linking  $V_m(H)$  to the price of a continuously monitored option with a barrier shifted away from the original. More precisely, they show that

$$V_m(H) = V\left(He^{\pm\beta\sigma\sqrt{\Delta t}}\right) + o\left(1/\sqrt{m}\right) \tag{3}$$

where  $V(\tilde{H})$  is the price of a continuously monitored barrier option with threshold  $\tilde{H}$  and  $\beta \approx$  $0.5826$ , with + for an up option and - for a down option.

Although this approach works very well, it appears to be inaccurate when the barrier is near the initial price of the underlying. Under such circumstances, one can opt to use the recursive method of Ait-Sahlia and Lai [1], which consists in reducing an  $m$ -dimensional integration problem to successively evaluating  $m$  one-dimensional integrals. Specifically, they show that

$$V_m(H) = \int_{\log(H/S_0)}^{\infty} \left( S_0 e^x - K \right)^+ f_m(x) \, dx \qquad (4)$$

where, for  $1 \le n \le m$ ,  $f_n(x) dx = P\{\tau > n, U_n \in$ dx} for  $x > \log(H/S_0)$ , with  $f_n$  defined recursively for each  $n$  according to the following:

$$f_1(x) = \psi(x)$$
  

$$f_n(x) = \int_{\log(H/S_0)}^{\infty} f_{n-1}(y)\psi(x-y) \, dy$$
  
for  $2 \le n \le m$  (5)

Here  $\psi(x) = \tilde{\sigma}^{-1}\phi = ((x - \mu)/\tilde{\sigma})$ , with  $\phi$  being the density of a standard normal distribution, and  $f_n(x) = 0$ , for  $x \leq \log(H/S_0)$  and  $1 \leq n \leq m$ . This approach is very accurate and efficient for generally moderate values of  $m$ , using as little as 20 integration points.

Both the continuity correction and recursive integration methods can also be similarly applied to discretely monitored look-back options (cf. [2] and [4].) Alternatives to the above abound as well. Fusai *et al.* [10] use a Wiener-Hopf machinery to also compute hedge parameters. In the context of a GARCH model, Duan *et al.* [7] propose a Markov chain technique that can also handle American-style exercise. Partial differential equations are used in [9, 22, 23, 24] to price average and barrier options, including when volatility is stochastic and exercise is of American style. Finally, [8] contains an approach that ultimately relies on Hilbert and Fourier transform techniques to address the situation when the underlying follows a Levy ´ process.

## **References**

- [1] AitSahlia, F. & Lai, T. (1997). Valuation of discrete barrier and hindsight options, *Journal of Financial Engineering* **6**, 169–177.
- [2] AitSahlia, F. & Lai, T. (1998). Random walk duality and the valuation of discrete lookback options, *Applied Mathematical Finance* **5**, 227–240.
- [3] Broadie, M., Glasserman, P. & Kou, S. (1997). A continuity correction for discrete barrier options, *Mathematical Finance* **7**, 325–349.
- [4] Broadie, M., Glasserman, P. & Kou, S. (1999). Connecting discrete and continuous path-dependent options, *Finance and Stochastics* **3**, 55–82.
- [5] Chance, D. (1994). The pricing and hedging of limited exercise caps and spreads, *Journal of Financial Research* **17**, 561–583.
- [6] Conze, A. & Viswanathan, R. (1991). Path dependent options: the case of lookback options, *Journal of Finance* **46**, 1893–1907.
- [7] Duan, J.C., Dudley, E., Gauthier, G. & Simonato, J.G. (2003). Pricing discretely monitored barrier options by a Markov Chain, *Journal of Derivatives* **10**, 9–31.
- [8] Feng, L. & Linetsky, V. (2008). Pricing discretely monitored barrier options and defaultable bonds in Levy process models: a fast Hilb ´ ert transform approach, *Mathematical Finance* **18**, 337–384.
- [9] Forsyth, P.A., Vetzal, K. & Zvan, R. (1999). A finite element approach to the pricing of discrete lookbacks with stochastic volatility, *Applied Mathematical Finance* **6**, 87–106.

- [10] Fusai, G., Abrahams, D. & Sgarra, C. (2006). An exact analytical solution for discrete barrier options, *Finance and Stochastics* **10**, 1–26.
- [11] Geman, H. & Yor, M. (1993). Bessel processes, Asian options and perpetuities, *Mathematical Finance* **3**, 349–375.
- [12] Goldman, M., Sosin, H. & Gatto, M. (1979). Path dependent options: 'Buy at the low, sell at the high', *Journal of Finance* **34**, 1111–1127.
- [13] Goldman, M., Sosin, H. & Shepp, L. (1979). On contingent claims that insure ex-post optimal stock market timing, *Journal of Finance* **34**, 401–414.
- [14] Heynen, R.C. & Kat, H.M. (1994). Partial barrier options, *Journal of Financial Engineering* **3**, 253–274.
- [15] Heynen, R.C. & Kat, H.M. (1994). Lookback options with discrete and partial monitoring of the underlying price, *Applied Mathematical Finance* **2**, 273–284.
- [16] Kat, H. & Verdonk, L. (1995). Tree surgery, *Risk* **8**, 53–56.
- [17] Kou, S. (2003). On pricing of discrete barrier options, *Statistica Sinica* **13**, 955–964.
- [18] Linetsky, V. (2004). Spectral expansions for Asian (average price) options, *Operations Research* **52**, 856–867.
- [19] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**, 141–183.
- [20] Rich, D. (1994). The mathematical foundations of barrier option pricing theory, *Advances in Futures and Options Research* **7**, 267–312.
- [21] Rubinstein, M. & Reiner, E. (1991). Breaking down the barriers, *Risk* **4**, 28–35.
- [22] Vetzal, K. & Forsyth, P.A. (1999). Discrete Parisian and delayed barrier options: a general numerical approach, *Advanced Futures Options Research* **10**, 1–16.
- [23] Zvan, R., Forsyth, P.A & Vetzal, K. (1999). Discrete Asian barrier options, *Journal of Computational Finance* **3**, 41–68.
- [24] Zvan, R., Vetzal, K. & Forsyth, P.A. (2000). PDE methods for pricing barrier options, *Journal of Economic Dynamics and Control* **24**, 1563–1590.

FARID AITSAHLIA
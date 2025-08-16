# Implied Volatility: Market Models

The market model approach for implied volatility consists in taking implied volatilities as the quantities one wishes to model. In many options exchanges and over-the-counter markets, implied volatility is the way an option is quoted and hence plays the role of a price.

The market model approach for implied volatilities is inspired by the corresponding market model approach for interest rates, the so-called Heath-Jarrow-Morton (HJM) approach to interest rate modeling (see Heath-Jarrow-Morton Approach). In interest rate modeling, it is simple to characterize the dynamics of the entire family of instantaneous forward rates in such a way that the corresponding family of bond prices is arbitrage free. It is also simple to give examples of such dynamics and to price interest rate sensitive contingent claims in such models.

Correspondingly, the market model approach to implied volatility seeks to characterize the dynamics of the entire implied volatility surface in such a way that the corresponding family of option prices is arbitrage free. It also seeks simple examples of such dynamics and ideally practical means of computing prices of exotic options on the underlying in such models.

Despite numerous attempts and recent progress in this area, it is fair to say that this approach has unfortunately not delivered the same elegant and useful results as the HJM approach has in interest rate modeling. The market approach to implied volatility can be traced back to the works [11, 12, 20].

As in the HJM approach, the no-arbitrage condition for implied volatilities takes the form of a drift restriction. In other words, the drift must be constrained for option prices to be local martingales under the pricing measure.

## **Drift Restriction**

To continue the discussion, we need the following definitions. Let  $(\mathbf{W}_t)_{t>0}$  be an *n*-dimensional Wiener process that models the uncertainty in the economy. We shall use boldface letters for vectors, . for the usual scalar product, and  $|\cdot|$  for the Euclidean norm. We assume that the probability measure is risk neutral, that is, discounted price processes are local martingales. We assume for simplicity that interest rates and dividends are zero.

The traded asset on which options are written is denoted by  $S_t$  and its volatility vector by  $\boldsymbol{\sigma}_t$ , that is,

$$\frac{\mathrm{d}S_t}{S_t} = \boldsymbol{\sigma}_t \cdot \mathrm{d}\mathbf{W}_t \tag{1}$$

The no-arbitrage constraint for the implied volatility  $\Sigma_t(T, K)$  for the option with strike K and maturity  $T$  implies the following drift restriction in their dynamics

$$\begin{split} &\Sigma_t(T,K) \\ &= \Sigma_0(T,K) - \int_0^t \left[ \frac{\left| \boldsymbol{\sigma}_s - \ln\left(S_s/K\right) \boldsymbol{\xi}_s\right|^2 - \Sigma_s^2}{2\Sigma_s(T-s)} \right. \\ &\quad + \left. \frac{1}{2} \Sigma_s \boldsymbol{\sigma}_s \cdot \boldsymbol{\xi}_s - \frac{1}{8} \Sigma_s^3(T-s) \left| \boldsymbol{\xi}_s \right|^2 \right] \left(T,K\right) \mathrm{d}s \\ &\quad + \int_0^t \Sigma_s(T,K) \boldsymbol{\xi}_s(T,K) \cdot \mathrm{d}\mathbf{W}_s \end{split} \tag{2}$$

where  $\xi_t(T, K)$  is the implied volatility's volatility vector. The corresponding call option price dynamics is

$$C_t(T, K) = C_0(T, K) + \int_0^t S_s(\Phi(d_1)\boldsymbol{\sigma}_s$$
  
+  $\Sigma_s \sqrt{T - s}\varphi(d_1)\boldsymbol{\xi}_s(T, K) \cdot d\mathbf{W}_s$  (3)

where, as usual,  $d_1 = (\ln(S_t/K)/\Sigma_t(T, K)\sqrt{T-t})$  $+\frac{1}{2}\Sigma_t(T, K)\sqrt{T-t}$  and  $\Phi$  and  $\varphi$  denote, respectively, the cumulative distribution and density probability function of a standard Gaussian random variable.

The above equation (2) is the equivalent of the HJM equation for implied volatilities. However, unlike the HJM equation, the drift does not solely involve the volatility vector  $\boldsymbol{\xi}_t$  but also depends on  $S_t$  and  $\boldsymbol{\sigma}_t$ .

#### The Spot Volatility Specification

Equation  $(2)$  has interesting properties. In particular, when we consider the infinite system of equation  $(2)$  for a fixed K and all  $T > t$ , it alone specifies the spot volatility  $\sigma_t$ . This phenomenon is directly related to the convergence of option prices to the option payoff at expiry. Equivalently, the solution to equation  $(2)$ should not blow up too fast near expiry. It is called *no-bubble restriction* in [17], whereas [5] calls it the *feedback condition* and traces it back to [8]. It is also called the *volatility specification* in [19] and [6]. It reads

$$\Sigma_t(t,K) = \left| \boldsymbol{\sigma}_t - \ln\left(\frac{S_t}{K}\right) \boldsymbol{\xi}_t(t,K) \right| \qquad (4)$$

For a proof under proper assumptions, see  $[13]$ .

The case where we let  $K = S_t$  in equation (4) says  $\Sigma_t(t, S_t) = |\boldsymbol{\sigma}_t|$ . In other words, the current value of the spot volatility can be exactly recovered from the implied volatility smile. This very much parallels the fact that the instantaneous forward rate with infinitely small tenor is the short rate in the HJM approach to interest rates.

It is shown in [14] that the relation  $\Sigma_t(t, S_t) = |\boldsymbol{\sigma}_t|$ holds in great generality even when jumps in the spot and/or its volatility are present. It turns out to be a consequence of the central limit theorem for martingales.

Equation (4) has an interesting connection to the work of Berestycki *et al.* [3]. In a time homogeneous stochastic volatility model, [3] shows that the implied volatility in the short maturity limit can be expressed using the geodesic distance associated with the generator of the bivariate diffusion  $(x_t, y_t)$ , where  $x_t$  is the log-moneyness and  $y_t$  is the spot volatility ( $|\sigma_t|$ in our notation). Keeping their notation, we denote by  $d(x, y)$  the signed geodesic distance from  $(x, y)$ to  $(0, y)$ , and obtain

$$\Sigma_t(t, K) = \frac{\ln(S_t/K)}{d(\ln(S_t/K), |\boldsymbol{\sigma}_t|)}$$
(5)

By comparing equations  $(4)$  and  $(5)$ , it becomes clear that the geodesic distance associated with the generator of the stochastic volatility model and the implied volatility's volatility vector are strongly related.

## The Case of a Single Strike

We first deal with the problem studied by  $[1, 4, 16,$ 17, 19] where only a single option is considered. The goal is to set up conditions under which the infinite system of equation (2) for a fixed  $K$  and all  $T > t$  together with equation (1) admits a unique solution. The best results were obtained by [4] and [19]. Without loss of generality, one can assume that equation  $(1)$  is driven by the first Wiener process only and that  $\boldsymbol{\sigma}_t = (\sigma_t, 0, \ldots, 0)$ . Assume that  $\boldsymbol{\xi}_t$  has the functional form.

$$\xi_t(T,K) = \frac{1}{2} \int_t^T \frac{X_t(u,K)}{X_t(T,K)} \mathbf{V}_t(u,K) \, \mathrm{d}u \quad (6)$$

where  $X_t(T, K) = \frac{\partial}{\partial T} (\Sigma_t(T, K)^2(T - t))$  is the square of the *forward* implied volatility and where  $\mathbf{V}$  has the form

$$\mathbf{V}_t(T,K) = \mathbf{V}(t,T,K,\Sigma_t(T,K),\Sigma_t(t,K),S_t) \quad (7)$$

for a deterministic function  $V$  satisfying technical positivity, growth, and Lipschitz conditions [19]. Assume also that the spot volatility has the functional form  $\sigma_t = \sigma(t, K, \Sigma_t(t, K), S_t)$ , where the deterministic function  $\sigma$  is determined by equation (4). Then, the infinite system of equation (2) for a fixed  $K$  and all  $T > t$  together with equation (1) admits a unique solution.

#### The Case of Several Strikes

The infinite system of equation (2) for all  $K$  and all  $T > t$  together with equation (1) is more complicated and conditions on  $\xi_t$  under which it admits a unique solution are still poorly understood. One advantage of dealing with all strikes  $K$  at once is that one can remove the dependence on  $S$  in equation (2) by changing the parameterization of the surface from  $K$ to moneyness  $K/S_t$ . The dynamics of the implied volatility surface in these coordinates are obtained by applying the Itô-Wentzell formula as in [5]. One of the difficulties of the multistrike case is that the solution to the infinite system in equation (2) must satisfy some shape restrictions at each time  $t$ . These are consequences of the well-known static arbitrage restrictions that we now recall.

#### **Static Arbitrage Restrictions**

Static arbitrage relations lead to constraints on the shape of the implied volatility surface. The fact that calendar spreads have positive values leads to

$$\frac{\partial \Sigma_t}{\partial T} + \frac{\Sigma_t}{2(T-t)} \ge 0 \tag{8}$$

The fact that call values are a decreasing function of the strike leads to

$$\frac{-\Phi(-\mathrm{d}_1)}{\varphi(\mathrm{d}_1)\sqrt{T-t}} \le K \frac{\partial \Sigma_t}{\partial K} \le \frac{\Phi(\mathrm{d}_2)}{\varphi(\mathrm{d}_2)\sqrt{T-t}} \qquad (9)$$

Finally, the fact that butterfly spreads have positive values, or that calls are convex functions of the strike leads to

$$\left(1 - \frac{\ln\left(K/S_t\right)}{\Sigma_t} K \frac{\partial \Sigma_t}{\partial K}\right)^2 - \frac{\left(T - t\right)^2}{4} \Sigma_t^2 \left(K \frac{\partial \Sigma_t}{\partial K}\right)^2 + (T - t)\Sigma_t \left(K \frac{\partial \Sigma_t}{\partial K} + K^2 \frac{\partial^2 \Sigma_t}{\partial K^2}\right) \ge 0 \tag{10}$$

where  $d_2 = d_1 - \Sigma_t(T, K)\sqrt{T - t}$ . These restrictions must hold at each time  $t$  and at each point  $(T, K)$  of the implied volatility surface.

#### **Deterministic Models**

Practitioners [10] have proposed two simple models for implied volatility surfaces movements: the sticky strike model and the sticky delta model. The sticky strike model supposes that between date s and  $t \geq s$ , the implied volatility surface evolves as

$$\Sigma_t(T, K) = \Sigma_s(T, K) \tag{11}$$

whereas the sticky delta model supposes that

$$\Sigma_t(T,K) = \Sigma_s\left(T, \frac{S_s}{S_t}K\right) \tag{12}$$

In a sticky strike model, an option with a given strike has constant implied volatility. This contrasts with a sticky delta model where options with same moneyness have same implied volatilities. In other words, the implied volatility surface moves in perfect sync with the spot. In reality, implied volatilities move in a more complicated fashion but these two extreme cases are useful stylized benchmarks.

The sticky strike and sticky delta models, in fact, imply strong restrictions on the possible spot dynamics. Balland [2] showed that a sticky delta occurs if and only if the underlying asset price is the exponential of a process with independent increments (i.e., a Lévy process, *see* **Exponential Lévy Models**) under the pricing measure, and that a sticky strike situation occurs in the Black-Scholes model only!

## **Empirical Models**

To overcome the obvious shortcomings of the sticky strike and sticky delta models, Cont and da Fonseca [9] have proposed to write down a model for the future evolution of the surface as an infinite system where each point of the surface is driven by a few common factors. These dynamics allow for easy calibration using principal component analysis [9] and can be useful for risk management and scenarios simulation. It is difficult, however, to check whether such specifications satisfy arbitrage restrictions, which prevents them from being used to price exotic options.

## The Spot Volatility Dynamics from the Implied Volatility Surface

In the HJM approach (see Heath-Jarrow-Mor**ton Approach**) to interest rate modeling, the HJM equation can be used to write down the short rate dynamics starting from the forward rate dynamics. The parallel result in the case of implied volatility was obtained in  $[13]$ . The statement is the following: there exists a scalar Wiener process  $W^{\perp}$  adapted to the filtration generated by  $(\mathbf{W}_t)_{t>0}$  such that

$$\begin{split} \boldsymbol{\sigma}_{t}|^{2} &= |\boldsymbol{\sigma}_{0}|^{2} + \int_{0}^{t} \left[4\left|\boldsymbol{\sigma}_{s}\right|\frac{\partial\Sigma_{s}}{\partial T}(s,\,S_{s}) + 6\left|\boldsymbol{\sigma}_{s}\right|^{2}\right. \\ & \times \left(S_{s}\frac{\partial\Sigma_{s}}{\partial K}(s,\,S_{s})\right)^{2} + 2\left|\boldsymbol{\sigma}_{s}\right|^{3}S_{s}^{2}\frac{\partial^{2}\Sigma_{s}}{\partial K^{2}}(s,\,S_{s})\right] \mathrm{d}s \\ & + \int_{0}^{t} 4\left|\boldsymbol{\sigma}_{s}\right|\frac{\partial\Sigma_{s}}{\partial K}(s,\,S_{s})\,\mathrm{d}S_{s} + \int_{0}^{t} 2\left|\boldsymbol{\sigma}_{s}\right|^{2}\xi_{s}^{\perp}\,\mathrm{d}W_{s}^{\perp} \end{split} \tag{13}$$

where

$$\begin{split} \left(\xi_t^{\perp}\right)^2 &= \ -\ \frac{2}{|\boldsymbol{\sigma}_t|} \frac{\mathrm{d}}{\mathrm{d}t} \left\langle S_t, \frac{\partial \Sigma_t}{\partial K}(t, S_t) \right\rangle \\ &+ 2\left(S_t \frac{\partial \Sigma_t}{\partial K}(t, S_t)\right)^2 - |\boldsymbol{\sigma}_t| \ S_t \frac{\partial \Sigma_t}{\partial K}(t, S_t) \\ &- 3|\boldsymbol{\sigma}_t| \ S_t^2 \frac{\partial^2 \Sigma_t}{\partial K^2}(t, S_t) \end{split}$$

Moreover, the two local martingales appearing in the decomposition are orthogonal in the sense that

$$\left\langle \int_0^t 4 \left| \boldsymbol{\sigma}_s \right| \frac{\partial \Sigma_s}{\partial K} (s, S_s) \, \mathrm{d}S_s; \int_0^t 2 \left| \boldsymbol{\sigma}_s \right|^2 \xi_s^{\perp} \mathrm{d}W_s^{\perp} \right\rangle = 0 \tag{14}$$

This result actually has a converse, which allows one to get a very precise idea of the implied volatility of a given spot model. It indeed allows to compute the first terms of the Taylor expansion of the implied volatility surface for short maturity and around the money [13].

#### **Other Approaches**

Modeling implied volatilities is equivalent to modeling option prices; as seen in equation (3), it is merely a parameterization of the options' volatilities. The difficulties in modeling implied volatilities have led researchers to look for other and possibly more tractable parameterizations. We mention them here, although these approaches depart from the strict study of implied volatilities.

First, following a program started in  $[7, 10]$  model option prices by modeling Dupire local volatility as a random field. They are able to find explicit drift conditions as well as some examples of such dynamics. The Dupire local volatility surface also specifies the spot volatility in the short maturity limit but does not have complicated static arbitrage restrictions like equations  $8-10$ .

Another way of parameterizing option prices consists in modeling its intrinsic value, that is, the difference between the option price and the payoff if the option was exercised today. This is the approach taken by  $[15]$  in a very general semimartingale framework. Exactly as with implied volatilities, this approach yields a spot specification when options are close to maturity.

Finally, let us mention the recent work [18], where the authors introduce new quantities: the "local implied volatilities" and "price level" to parameterize option prices. These have nicer dynamics and naturally satisfy the static arbitrage conditions. They derive existence results for the infinite system of equations driving these quantities.

## References

- $[1]$ Babbar, K. (2001). Aspects of Stochastic Implied Volatility in Financial Markets. PhD thesis, Imperial College, London.
- [2] Balland, P. (2002). Deterministic implied volatility models, *Quantitative Finance* 2(2), 31-44.
- Berestycki, H., Busca, J. & Florent, I. (2004). Comput-[3] ing the implied volatility in stochastic volatility models, Communications on Pure and Applied Mathematics 57(10), 1352-1373.
- Brace, A., Fabbri, G. & Goldys, B. (2007). An Hilbert [4] Space Approach for A Class of Arbitrage Free Implied Volatilities Models, Technical report, Department of Statistics, University of New South Wales, at http://arxiv. org/abs/0712.1343.
- [5] Brace, A., Goldys, B., Klebaner, F. & Womersley, R. (2001). Market Model for Stochastic Implied Volatility with Application to the BGM Model, Technical report, Department of Statistics, University of New South Wales.
- Carmona, R. (2007). HJM: a unified approach to [6] dynamic models for fixed income, credit and equity markets, in Paris-Princeton Lectures on Mathematical Finance 2004, Lecture Notes in Mathematics, Springer, Vol. 1919.
- [7] Carmona, R. & Nadtochiy, S. (2009). Local volatility dynamic models, *Finance and Stochastics*  $13(1)$ , 1–48.
- Carr, P. (2000). A Survey of Preference Free Option [8] Valuation with Stochastic Volatility, Risk's 5th annual European derivatives and risk management congress, Paris.
- [9] Cont, R. & Da Fonseca, J. (2002). Dynamics of implied volatility surfaces, *Quantitative Finance* 2(2), 45-60.
- [10] Derman, E. (1999). Regimes of volatility, Risk (4),  $55 - 59$
- [11] Derman, E. & Kani, I. (1998). Stochastic implied trees: arbitrage pricing with stochastic term and strike structure of volatility, International Journal of Theoretical Applied Finance  $1(1)$ , 61–110.
- [12] Dupire, B. (1993). Model art, Risk 6(9), 118-124.
- Durrleman, V. (2004). From Implied to Spot Volatilities, [13] PhD thesis, Department of Operations Research & Financial Engineering, Princeton University, at http:// papers.ssrn.com/sol3/papers.cfm?abstract id=1162425 to appear in Finance and Stochastics.
- Durrleman, V. (2008). Convergence of at-the-money [14] implied volatilities to the spot volatility, Journal of Applied Probability 45, 542-550.
- [15] Jacod, J. and Protter, P. (2006). Risk Neutral Compatibility with Option Prices, Technical report, Université Paris VI and Cornell University, at http://people.orie.cornell. edu/ protter/WebPapers/JP-OptionPrice.pdf.
- [16] Lyons, T. 1995. Uncertain volatility and the risk-free synthesis of derivatives, Applied Mathematical Finance  $(2), 117-133.$

- [17] Schonbucher, P. (1999). A market model for stochastic ¨ implied volatility, *Philosophical Transactions of the Royal Society of London. Series A: Mathematical and Physical Sciences* **357**(1758), 2071–2092.
- [18] Schweizer, M. & Wissel, J. (2008). Arbitrage-free market models for option prices: the multi-strike case, *Finance and Stochastics* **12**(4), 469–505.
- [19] Schweizer, M. & Wissel, J. (2008). Term structures of implied volatilities: absence of arbitrage and existence results, *Mathematical Finance* **18**, 77–114.
- [20] Zhu, Y. & Avellaneda, M. (1998). A risk-neutral stochastic volatility model, *International Journal of Theoretical and Applied Finance* **1**(2), 289–310.

# **Further Reading**

Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*, Wiley Finance.

Heath, D., Jarrow, R. & Morton, A. Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**(1), 77–105.

# **Related Articles**

**Black–Scholes Formula**; **Dividend Modeling**; **Exponential Levy Models ´** ; **Heath–Jarrow–Morton Approach**; **Implied Volatility: Long Maturity Behavior**; **Implied Volatility: Large Strike Asymptotics**; **Implied Volatility: Volvol Expansion**; **Implied Volatility Surface**; **Implied Volatility in Stochastic Volatility Models**; **Local Volatility Model**; **Moment Explosions**; **SABR Model**.

VALDO DURRLEMAN
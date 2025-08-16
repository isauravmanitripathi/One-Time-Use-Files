# **Fractional Brownian** Motion

A fractional Brownian motion (fBm) is a self-similar Gaussian process, defined as follows:

**Definition 1** Let  $0 < H < 1$ . The Gaussian stochastic process  $\{B_H(t)\}_{t>0}$  satisfying the following three properties

- (*i*)  $B_H(0) = 0$
- (ii)  $E[B_H(t)] = 0$  for all  $t \ge 0$ ,
- (iii) for all  $s, t > 0$ ,

$$E[B_H(t)B_H(s)]$$
  
=  $\frac{1}{2} \left( |t|^{2H} - |t - s|^{2H} + |s|^{2H} \right)$  (1)

#### is called the (standard) fBm with parameter $H$ .

The fBm has been the subject of numerous investigations, in particular, in the context of long-range dependence (often referred to as long memory). fBm was first introduced in 1940 by Kolmogorov (see Kolmogorov, Andrei Nikolaevich) [11], but its main properties and its relevance in many fields of application such as economics, finance, turbulence, and telecommunications were first discussed in the seminal paper of Mandelbrot (see **Mandelbrot, Benoit**) and Van Ness [12].

For historical reasons, the parameter  $H$  is also referred to as the *Hurst coefficient*. In fact, in 1951, while he was investigating the flow of the river Nile, the British hydrologist H. E. Hurst [10] noticed that his measurements showed dependence properties and, in particular, long memory behavior in the sense that they seemed to require models, whose autocorrelation functions exhibit a power law decay at large timescales. This index of dependence  $H$  always takes values between  $0$  and  $1$  and indicates relatively long-range dependence if  $H > 0.5$ , for example, Hurst observed  $H = 0.91$  in the case of Nile level data.

If  $H = 0.5$ , it is obvious from equation (1) that the increments of fBm are independent and  $\{B_{0.5}(t)\}_{t\in\mathbb{R}} = \{B(t)\}_{t\in\mathbb{R}}$  is ordinary Brownian motion. Moreover, fBm has stationary increments which, for  $H \neq 0.5$ , are not independent.

One can define a parametric family of fBms in terms of the *stochastic Weyl integral* (see e.g. [16], chapter 7.2). In fact, for any  $a, b \in \mathbb{R}$ ,

$$\{B_{H}(t)\}_{t\in\mathbb{R}} \stackrel{d}{=} \left\{ \int_{\mathbb{R}} \left\{ a \left[ (t-s)_{+}^{H-\frac{1}{2}} - (-s)_{+}^{H-\frac{1}{2}} \right] \right. \\ + \left. b \left[ (t-s)_{-}^{H-\frac{1}{2}} - (-s)_{-}^{H-\frac{1}{2}} \right] \right\} \mathrm{d}B(s) \right\}_{t\in\mathbb{R}} \tag{2}$$

where  $u_{+} = \max(u, 0), \quad u_{-} = \max(-u, 0), \text{ and}$  $\{B(t)\}_{t\in\mathbb{R}}$  is a two-sided standard Brownian motion constructed by taking a Brownian motion  $B_1$  and an independent copy  $B_2$  and setting  $B(t) = B_1(t)1_{\{t \ge 0\}}$  $-B_2(-t-1)_{\{t<0\}}.$ 

If we choose  $a = \sqrt{\Gamma(2H+1)\sin(\pi H)}/\Gamma(H+$ 1/2) and  $b = 0$  in equation (2) then  $\{B_H(t)\}_{t \in \mathbb{R}}$  is an  $fBm$  satisfying equation (1).

fBm admits a *Volterra type representation*  $B_H(t)$  $=\int_0^t K_H(t,s) B(ds)$ , where  $K_H$  is some square integrable kernel (see [13] or [1] for details).

#### Properties

Many properties of fBm, like self-similarity, are given by its fractional index  $H$ .

**Definition 2** A real-valued stochastic process  $\{X(t)\}_{t\in\mathbb{R}}$  is self-similar with index H if for all  $c>0$ ,  $\{X(ct)\}_{t\in\mathbb{R}} \stackrel{d}{=} c^H \{X(t)\}_{t\in\mathbb{R}}, \text{ where } \stackrel{d}{=} \text{ denotes equality}$ in distribution

**Proposition 1** *Fractional Brownian motion (fBm)* is self-similar with index H. Moreover, fBm is the only self-similar Gaussian process with stationary increments.

Now, we consider the increments of fBm.

**Definition 3** *The stationary process*  $\{Y(t)\}_{t\in\mathbb{R}}$  *given*  $by$ 

$$Y(t) = B_H(t) - B_H(t-1) \quad t \in \mathbb{R} \tag{3}$$

is called fractional Gaussian noise.

![](_page_1_Figure_1.jpeg)

**Figure 1** Various sample paths, each showing 500 points of fBm

For  $n \in \mathbb{N}$ , it follows by the stationarity of the increments of  $B_H$ ,

$$\rho_H(n) := \text{cov}(Y(k+n), Y(k))$$
  
=  $\frac{1}{2}(|n+1|^{2H} - 2|n|^{2H} - |n-1|^{2H}) \tag{4}$ 

#### **Proposition 2**

- (i) If  $0 < H < 0.5$ ,  $\rho_H$  is negative and  $\sum_{i=1}^{\infty} |\rho_H(n)|$  $< \infty$ .
- (ii) If  $H = 0.5$ ,  $\rho_H$  equals 0, that is, the increments are independent.

(iii) If 
$$0.5 < H < 1$$
,  $\rho_H$  is positive,  $\sum_{n=1}^{\infty} |\rho_H(n)| = \infty$ 

 $and$ 

$$o_H(n) \sim C n^{2H-2}, \quad n \to \infty$$
 (5)

Hence, for  $0.5 < H < 1$  the increments of fBm are persistent or long-range dependent, whereas for  $0 < H < 0.5$  they are said to be *antipersistent*.

**Proposition 3** The sample paths of fBm are continuous. In particular, for every  $\tilde{H} < H$  there exists a modification of  $B_H$  whose sample paths are almost surely (a.s.) locally  $\tilde{H}$ -Hölder continuous on  $\mathbb{R}$ , that is, for each trajectory, there exists a constant  $c > 0$  such that

$$|B_H(t) - B_H(s)| \le c|t - s|^{H - \epsilon} \tag{6}$$

for any  $\epsilon > 0$ .

Figure 1 shows the sample paths of fBm for various values of the Hurst parameter  $H$ .

**Proposition 4** The sample paths of fBm are of finite *p*-variation for every  $p > 1/H$  and of infinite *p*variation if  $p < 1/H$ .

Consequently, for  $H < 0.5$  the quadratic variation is infinite. On the other hand, if  $H > 0.5$  it is known that the quadratic variation of fBm is zero, whereas the total variation is infinite.

**Corollary 1** This shows that for  $H \neq 1/2$ , fBm cannot be a semimartingale.

A proof of this well-known fact can be found in for example, [15] or [4].

However, since fBm is not a semimartingale one cannot use the Itô stochastic integral (see Stochastic **Integrals**) when considering integrals with respect to fBm. Recently, integration with respect to fBms has been studied extensively and various approaches have been made to define a stochastic integration theory for fBm (see e.g., [14] for a survey).

## **Applications in Finance**

Many studies of financial time series point to longrange dependence (*see* **Long Range Dependence**), which indicates the potential usefulness of fBm in financial modeling (see [7] for a summary and references). One obstacle is that fBm is not a semimartingale (*see* **Semimartingale**), so the Ito integral cannot be used to define the gain of a self-financing portfolio as, for instance, in the Black–Scholes model (*see* **Black–Scholes Formula**). Various approaches have been developed for integrating fBm, some of which are as follows:

1. The *pathwise Riemann–Stieltjes fractional integral* defined by

$$\int_{0}^{T} f(t) \, \mathrm{d}B_{H}(t)$$
$$= \lim_{|\pi| \to 0} \sum_{k=0}^{n-1} f(t_{k}) (B_{H}(t_{k+1}) - B_{H}(t_{k})) \tag{7}$$

where *π* = {*tk* : 0 = *t*<sup>0</sup> *< t*<sup>1</sup> *<...<tn* = *T* } is a partition of the interval [0*, T* ] and *f* has bounded *p*-variation for some *p <* 1*/(*1 − *H )* a.s.

2. Under some regularity conditions on *f* , the *fractional Wick–It ˆo integral* has the form

$$\int_{0}^{T} f(t) \, \delta B_{H}(t)$$

$$= \lim_{|\pi| \to 0} \sum_{k=0}^{n-1} f(t_{k}) \, \diamondsuit \, (B_{H}(t_{k+1}) - B_{H}(t_{k}))$$
(8)

where ♦ represents the Wick product [18] and the convergence is the *L*<sup>2</sup>*()*-convergence of random variables [2].

Whereas, the pathwise fractional integral mirrors a Stratonovich integral, the Wick– Ito-Skorohod calcu- ˆ lus is similar to the Ito calculus, for example, integrals ˆ always have zero expectation.

The Wick– Ito integral was constructed by Duncan ˆ *et al.* [8] and later applied to finance by, for example, Hu and Oksendal [9] in a fractional Black–Scholes pricing model in which the "gain" of a self-financing portfolio *φ* is replaced by *T* 0 *φ(t) δS(t)*. However, results produced by this approach are controversial: indeed, for a piecewise constant strategy (represented by a simple predictable process) *φ*, this definition does not coincide with the capital gain of the portfolio, so the approach lacks economical interpretation [3]. An interesting study is [17], where the implications of different notions of integrals to the problem of arbitrage and self-financing condition in the fractional pricing model are considered.

An alternative is to use mixed Brownian motion, defined as the sum of a (regular) Brownian motion and an fBm with index *H* which, under some conditions on *H*, is a semimartingale [5]. Alternatively, Rogers [15] proposes to modify the behavior near zero of the kernel in equation (2) to obtain a semimartingale. In both the cases, one loses selfsimilarity, but conserves long-range dependence.

On the other hand, there is empirical evidence of long-range dependence in absolute returns [7], showing that it might be more interesting to use fractional processes as models of volatility rather than prices [6]. Fractional volatility processes are compatible with the semimartingale assumption for prices, so the technical obstacles discussed above do not necessarily arise when defining portfolio gain processes (*see* **Long Range Dependence**; **Multifractals**).

## **References**

- [1] Baudoin, F. & Nualart, D. (2003). Equivalence of Volterra processes, *Stochastic Processes and their Applications* **107**, 327–350.
- [2] Bender, C. (2003). An Ito formula for generalized func- ˆ tionals of a fractional Brownian motion with arbitrary Hurst parameter, *Stochastic Processes and their Applications* **104**, 81–106.
- [3] Bjork, T. & Hult, H. (2005). A note on Wick products ¨ and the fractional Black-Scholes model, *Finance and Stochastics* **9**, 197–209.
- [4] Cheridito, P. (2001). *Regularizing Fractional Brownian Motion with a View towards Stock Price Modelling*, PhD Dissertation, ETH Zurich.
- [5] Cheriditio, P. (2003). Arbitrage in fractional Brownian motion models, *Finance and Stochastics* **7**, 533–553.
- [6] Comte, F. & Renault, E. (1998). Long memory in continuous time stochastic volatility models, *Mathematical Finance* **8**, 291–323.

- [7] Cont, R. (2005). Long range dependence in financial time series, in *Fractals in Engineering*, E. Lutton & J. Levy-Vehel, eds, Springer.
- [8] Duncan, T.E., Hu, Y. & Pasik-Duncan, B. (2000). Stochastic calculus for fractional Brownian motion I. Theory, *SIAM Journal of Control and Optimization* **28**, 582–612.
- [9] Hu, Y. & Oksendal, B. (2003). Fractional white noise calculus and applications to finance, *Infinite Dimensional Analysis, Quantum Probability and Related Topics* **6**, 1–32.
- [10] Hurst, H. (1951). Long term storage capacity of reservoirs, *Transactions of the American Society of Civil Engineers* **116**, 770–1299.
- [11] Kolmogorov, A.N. (1940). Wienersche Spiralen und einige andere interessante Kurven im Hilbertschen Raum, *Computes Rendus (Doklady) Academic Sciences USSR (N.S.)* **26**, 115–118.
- [12] Mandelbrot, B.B. & Van Ness, J.W. (1968). Fractional Brownian motions, fractional noises and applications, *SIAM Review* **10**, 422–437.
- [13] Norros, I., Valkeila, E. & Virtamo, J. (1999). An elementary approach to a Girsanov formula and other analytical results on fractional Brownian motion, *Bernoulli* **5**, 571–589.
- [14] Nualart, D. (2003). Stochastic calculus with respect to the fractional Brownian motion and applications, *Contemporary Mathematics* **336**, 3–39.

- [15] Rogers, L.C.G. (1997). Arbitrage with fractional Brownian motion, *Mathematical Finance* **7**, 95–105.
- [16] Samorodnitsky, G. & Taqqu, M. (1994). *Stable Non-Gaussian Random Processes: Stochastic Models with Infinite Variance*, Chapman & Hall, New York.
- [17] Sottinen, T. & Valkeila, E. (2003). On arbitrage and replication in the fractional Black-Scholes pricing model, *Statistics and Decisions* **21**, 93–107.
- [18] Wick, G.-C. (1950). Evaluation of the collision matrix, *Physical Review* **80**, 268–272.

## **Further Reading**

- Doukhan, P., Oppenheim, G. & Taqqu, M.S. (2003). *Theory and Applications of Long-Range Dependence*, Birkhauser, ¨ Boston.
- Lin, S.J. (1995). Stochastic analysis of fractional Brownian motion, *Stochastics and Stochastics Reports* **55**, 121–140.

## **Related Articles**

**Long Range Dependence**; **Mandelbrot, Benoit**; **Multifractals**; **Semimartingale**; **Stylized Properties of Asset Returns**.

TINA M. MARQUARDT
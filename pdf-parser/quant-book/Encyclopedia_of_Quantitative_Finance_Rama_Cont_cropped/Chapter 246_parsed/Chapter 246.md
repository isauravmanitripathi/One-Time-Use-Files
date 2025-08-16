# **Fourier Transform**

### **Discrete Fourier Transform (DFT)**

The *n*th root of unity is denoted by  $z_n := \cos \frac{2\pi}{n} +$ i sin  $\frac{2\pi}{n} = e^{i\frac{2\pi}{n}}$ . Geometrically, the numbers  $z_n^j$ , with  $j = 0, \ldots, n-1$ , represent *n* equidistantly spaced points on the unit circle in the complex plane. The point  $z_n^{j+1}$  is reached from  $z_n^j$  by turning  $1/n$ th of the full circle anticlockwise.

**Definition 1** Given an n-dimensional vector  $a =$  $[a_0, a_1, \ldots, a_{n-1}],$  we say that

$$rev(a) := [a_0, a_{n-1}, \dots, a_1] \tag{1}$$

is a in reverse order. Intuitively, if a is written around the circle in the anticlockwise direction, then  $rev(a)$ is obtained by reading from  $a_0$  in the clockwise direction.

**Definition 2** The discrete Fourier transform (DFT) of  $a = [a_0, a_1, \ldots, a_{n-1}] \in \mathbb{C}^n$  is the vector  $b =$  $[b_0, b_1, \ldots, b_{n-1}] \in \mathbb{C}^n$  such that

$$b_k = \frac{1}{\sqrt{n}} \sum_{j=0}^{n-1} a_j z_n^{jk} = \frac{1}{\sqrt{n}} \sum_{j=0}^{n-1} a_j e^{i\frac{2\pi}{n}jk} \qquad (2)$$

We write

$$b = \mathcal{F}(a) \tag{3}$$

Equation (2) represents the forward transform. The inverse transform is given by

$$a_{l} = \frac{1}{\sqrt{n}} \sum_{k=0}^{n-1} b_{k} z_{n}^{-kl} = \frac{1}{\sqrt{n}} \sum_{k=0}^{n-1} b_{k} e^{-i\frac{2\pi}{n} kl} \qquad (4)$$

and we write

$$a = \mathcal{F}^{-1}(b) \tag{5}$$

**Proposition 1** The following statements hold:

1. The inverse  $DFT$  of sequence  $b$  is the same as the forward transform of the same sequence in the reverse order:

$$\mathcal{F}^{-1}(b) = \mathcal{F}(\text{rev}(b)) \tag{6}$$

and vice versa

$$\mathcal{F}^{-1}(\text{rev}(b)) = \mathcal{F}(b) \tag{7}$$

2.  $\mathcal{F}^{-1}$  is indeed an inverse transformation to  $\mathcal{F}$ . that is.

$$\mathcal{F}^{-1}\left(\mathcal{F}(a)\right) = \mathcal{F}\left(\mathcal{F}^{-1}\left(a\right)\right) = a \qquad (8)$$

Next, we explain the relationship between binomial option pricing and the DFT.

## **Binomial Option Pricing**

Consider a two-period binomial model (see **Binomial Tree**) with a high rate of return of  $25\%$  and a low rate of return of  $-20\%$ . Assuming that the initial stock price is 100, the evolution of the stock price in the two periods ahead is given in Table 1.

Suppose that we wish to price a call option struck at  $K = 100$ , maturing two periods from now. The risk-free rate is  $0\%$ . The intrinsic value of the option at maturity is

$$C(2, :) = \begin{bmatrix} 56.25 & 0 & 0 \end{bmatrix}^\top \tag{9}$$

As per the asset pricing theory, the no-arbitrage price of the option is given recursively as

$$C(t,j) = \frac{q_u C(t+1,j) + q_d C(t+1,j+1)}{R_f} \tag{10}$$

where the risk-neutral probabilities  $q_u$  and  $q_d$  satisfy

$$q_u = \frac{R_f - R_d}{R_u - R_d} = \frac{1 - 0.8}{1.25 - 0.8} = \frac{4}{9} \qquad (11)$$

$$q_d = 1 - q_u = \frac{5}{9} \tag{12}$$

Here,  $R_u = S(t + 1, j)/S(t, j)$ ,  $R_d = S(t + 1, j)$  $(j+1)/S(t, j)$ , and  $R_f - 1$  is equal to the risk-free rate. Recursive application of equation (10) with terminal value (9) leads to option prices as given in Table 2.

#### Option Pricing by Circular Convolution

For any two *n*-dimensional vectors  $a = [a_0, a_1, \ldots,$  $a_{n-1}$  and  $b = [b_0, b_1, \ldots, b_{n-1}]$ , we define *circular*  $(cyclic)$  convolution of  $a$  and  $b$  to be a new vector  $c = [c_0, c_1, \ldots, c_{n-1}],$ 

$$c = a \circledast b \tag{13}$$

| Number of<br>low returns $i$ | S(0, j) | S(1, i) | S(2, i) |
|------------------------------|---------|---------|---------|
|                              | 100     | 125     | 156.25  |
|                              |         | 80      | 100     |
|                              |         |         | 64      |

**Table 1** Binomial stock price lattice

**Table 2** Option prices in a binomial lattice

| Number of<br>low returns $i$ | C(0, i)         | C(1, i) | C(2, j) |
|------------------------------|-----------------|---------|---------|
|                              | $11\frac{1}{9}$ | 25      | 56.25   |
|                              |                 |         |         |
| 2                            |                 |         |         |

such that

$$c_j = \sum_{k+l=j \text{ or } k+l=j+n} a_k b_l \tag{14}$$

We use the binomial example to illustrate the use of circular convolution in option pricing. At maturity, the option has three values:

$$C(2, :) = \begin{bmatrix} 56.25 & 0 & 0 \end{bmatrix}^\top \tag{15}$$

Let vector  $q$  contain the conditional one-period riskneutral probabilities  $q_u = 0.43523$  and  $q_d = 0.56477$ . Since there are just two states over one period the remaining entries will be padded by zeros:

$$q = \begin{bmatrix} q_u & q_d & 0 \end{bmatrix}^\top \tag{16}$$

To compute option prices at time  $t = 1$ , we evaluate

$$C(1,:) = C(2,:) \circledast \text{rev}(q)/R_{\text{f}} = [25 \quad 0 \quad 31.25]^\top$$
(17)

Note that we need only the first two prices in equation  $(17)$ . The last entry is meaningless—it corresponds to the no-arbitrage price of the payoff [0 56.25]. Moving backward in time, we have

$$C(0, :) = C(1, :) \circledast \operatorname{rev}(q)/R_{\text{f}}$$
  
=  $\left[ 11\frac{1}{9} \quad 17\frac{13}{36} \quad 27\frac{7}{9} \right]^{\top}$  (18)

Again, only the first entry is meaningful.

This procedure can be generalized to multinomial lattices as follows.

Proposition 2 Consider an N-period model in which the random variables  $S_{t+1}/S_t$  are independent, identically distributed under the risk-neutral measure and such that  $\ln S_{t+1}/S_t$  takes k distinct, equidistantly spaced values with probabilities  $q_1, \ldots, q_k$ . Then stock price can be represented by a multinomial lattice with  $1 + t(k - 1)$  values at time t. Let  $C(N, :) \in \mathbb{R}^n$ ,  $n = 1 + N(k - 1)$ , be the payoff of a derivative asset as a function of  $S_N$ , and define riskneutral price of the option recursively by setting

$$C(t, j) = \sum_{l=1}^{k} q_l C(t+1, j+l-1),$$
  
$$1 \le l \le 1 + t(k-1)$$
 (19)

Let q be a vector with first k entries  $q_1, \ldots, q_k$  and padded by zeros to dimension n. Then  $C(t, :)$  can also be obtained from the following formula:

$$C(t, :) = C(N, :) \circledast \overbrace{\operatorname{rev}(q) \circledast \operatorname{rev}(q)}^{(N-t)} \circledast \dots \circledast \operatorname{rev}(q)$$
(20)

The vector  $C(t, :)$  computed in this manner has more entries than required (n in total); the useful  $1 + t(k -$ 1) entries are at the top end of the vector.

## Pricing via Discrete Fourier Transform

In this section, we reformulate the circular pricing formula (20) using the DFT.

**Proposition 3** Consider  $a, b \in \mathbb{C}^n$ . The following equalities hold:

$$\mathcal{F}(a \circledast b) = \sqrt{n}\mathcal{F}(a)\,\mathcal{F}(b) \tag{21}$$

$$\mathcal{F}^{-1}\left(a\circledast b\right) = \sqrt{n}\mathcal{F}^{-1}\left(a\right)\mathcal{F}^{-1}\left(b\right) \qquad (22)$$

Now applying the inverse transform  $\mathcal{F}^{-1}$  to both sides of equation  $(20)$  and using property  $(22)$  on the right-hand side

$$\mathcal{F}^{-1} (C_0) = \mathcal{F}^{-1} (C_N)$$
$$\times \left( \sqrt{\text{dimension of } C_N} \mathcal{F}^{-1} (\text{rev}(q)) / R_{\text{f}} \right)^N (23)$$

Recall from equation (7) that  $\mathcal{F}^{-1}(\text{rev}(q)) = \mathcal{F}(q)$ , and substitute this into equation (23). Finally, applying the forward transform to both sides again, and using equation  $(8)$  on the left-hand side, we obtain

$$C_{0} = \mathcal{F}\left(\mathcal{F}^{-1}\left(C_{N}\right)\right)$$
$$\times \left(\sqrt{\text{dimension of }C_{N}}\mathcal{F}\left(q\right)/R_{\text{f}}\right)^{N}\right) (24)$$

# **Fast Fourier Transform (FFT)**

A naive implementation of the DFT algorithm with an *n*-dimensional input requires  $n^2$  complex multiplications. An efficient implementation of DFT, known as the *fast Fourier transform (FFT)*, will only require  $Kn \ln n$  operations, but one still has to choose *n* carefully because the constant  $K$  can be very large for some choices of  $n$ . There are many instances when FFT of length  $n_1$  is faster than FFT of length  $n_2$ even though  $n_1 > n_2$ . This slightly counterintuitive phenomenon is illustrated in Table 3. In general, it is advisable to use the transform size of the form  $n = 2^{p}3^{q}5^{r}$ , where q and r should be small compared to  $p$ . In the context of option pricing, this is always possible by padding the payoff vector  $C_N$  with a sufficient number of zeros.

An efficient implementation of FFT for all transform lengths is suggested in [17]. Efficient implementation of mixed  $2, 3, 5$ -radix algorithm is

Table 3 Execution time of FFT algorithm for different input lengths  $n$ 

| n        | Factorization                                         | Execution time<br>(seconds) |
|----------|-------------------------------------------------------|-----------------------------|
| 999983   | 999983                                                | 26.3                        |
| 2097 150 | $2 \times 3 \times 5^2 \times 11 \times 31 \times 41$ | 1.4                         |
| 2097 152 | $\gamma^{21}$                                         | 0.42                        |
| 2160 000 | $2^73^35^4$                                           | 0.40                        |
|          |                                                       |                             |

Intel Core 2, 2 GHz, 2Gb RAM, Matlab 6.5.

due to Temperton [25]. Duhamel and Vetterli [15] survey a wide range of FFT algorithms. Fast implementation of equation (24) for Gauss and Matlab is discussed in [7].

# FFT in Continuous-time Models

In the continuous-time limit, the DFT is replaced by the (continuous) Fourier transform: that is, for a contingent claim with payoff  $C_T = f(\ln S_T)$ , we wish to find coefficients  $\psi(v)$  such that

$$f(x) = \int_{\beta - i\infty}^{\beta + i\infty} \psi(v) e^{vx} dv \qquad (25)$$

for some real constant  $\beta$  [19]. The recipe for obtaining the coefficients  $\psi(v)$  is known—it is given by the inverse Fourier transform:

$$\psi(v) = \frac{1}{2\pi i} \int_{-\infty}^{+\infty} f(x) \mathrm{e}^{-vx} \, \mathrm{d}x \tag{26}$$

For example, the payoff of a European call option with strike price  $e^k$  corresponds to  $f(x) = (e^x$  $e^{k}$ <sup>+</sup>, whereby, simple integration yields

$$\psi(v) = \frac{e^{(1-v)k}}{2\pi i v(v-1)} \text{ for } \text{Re}v > 1 \qquad (27)$$

Substituting for  $C_T$  from equation (25) the riskneutral pricing formula reads

$$C_{0}(\ln S_{0}) = e^{-rT} \mathbb{E} \left[C_{T}(\ln S_{T})\right]$$
  
$$= e^{-rT} \mathbb{E} \left[\int_{\beta - i\infty}^{\beta + i\infty} \psi(v) e^{v \ln S_{T}} dv\right]$$
  
$$= e^{-rT} \int_{\beta - i\infty}^{\beta + i\infty} \psi(v) e^{v \ln S_{0}} \mathbb{E} \left[e^{v \ln S_{T}/S_{0}}\right] dv$$
  
(28)

In practice, one is mainly interested in models where the risk-neutral characteristic function of log stock return  $\phi(-\mathrm{i}v) := \mathrm{E}[e^{v \ln S_T/S_0}]$  is available in the closed form. This is the case in the class of exponential Lévy models with affine stochastic volatility process, discussed in [6] (see also Time-changed Lévy Process). This class contains a large number of popular models allowing for excess kurtosis, stochastic volatility, and leverage effects. It includes, among others, the stochastic volatility models of Heston [18] (see **Heston Model**), Duffie *et al.* [14], and all exponential Lévy models (cf. [16, 23], see Exponential Lévy Models). For a detailed description of affine processes, see [13, 20].

Option pricing, therefore, boils down to the evaluation of integrals of the type

 $C_0(\ln S_0)$  $= S_0 e^{-rT} \int_{\beta - i\infty}^{\beta + i\infty} \frac{e^{(v-1)(\ln S_0 - k)}}{2\pi v (v-1)} \phi(-\mathrm{i} v) \, \mathrm{d} v$  $=2S_0e^{-rT}\int_{\beta+i0}^{\beta+i\infty} \mathrm{Re}\left(\frac{e^{(v-1)(\ln S_0-k)}}{2\pi v(v-1)}\phi(-\mathrm{i}v)\right)\,\mathrm{d}v$  $(29)$ 

where both  $\psi(v)$  and  $\phi(v)$  are known. To evaluate equation  $(29)$ , one truncates the integral at a high value of  $\text{Im}v$  and then uses a numerical quadrature to approximate it by a sum; see [22] for a detailed exposition. This yields an expression of the following type:

$$C_{0}(\ln S_{0}) \approx 2\text{Re}\left(S_{0}e^{-rT}\sum_{j=0}^{n-1}w_{j}\frac{e^{(v_{j}-1)(\ln S_{0}-k)}}{2\pi v_{j}(v_{j}-1)}\phi(-\mathrm{i}v_{j})\right)$$
(30)

where the integration weights  $w_i$  and abscissas  $v_i$ depend on the quadrature rule. It is particularly convenient to use Newton-Cotes rules, which employ equidistantly spaced abscissas. For example, a trapezoidal rule yields

$$v_i = \beta + \mathrm{i}j\triangle v \tag{31}$$

$$\text{Im}v_{\text{max}} = (n-1)\triangle v \tag{32}$$

$$w_0 = w_n = \frac{1}{2}\triangle v \tag{33}$$

$$w_1 = w_2 = \dots = w_{n-1} = \triangle v \qquad (34)$$

In conclusion, if the characteristic function of log returns is known, one needs to evaluate a single sum  $(30)$  to find the option price. Consequently, there is no need to use FFT if one wishes to evaluate the option price for *one fixed*  $\log$  strike  $k$ .

### FFT Option Pricing with Multiple Strikes

The situation is different if we wish to evaluate the option price (30) for many different strikes simultaneously. Let us consider  $m$  values of moneyness  $\kappa_l = \ln S_0 - k_l$ , ranging from  $\kappa_{\text{max}} - m \triangle \kappa$  to  $\kappa_{\text{max}}$ with increment  $\triangle \kappa$ 

$$\kappa_l = \kappa_{\text{max}} - l \triangle \kappa \tag{35}$$

$$l = 0, \dots, m - 1 \tag{36}$$

The idea of using FFT in this context is due to Carr and Madan [5], who noted that with equidistantly spaced abscissas (31) one can write the option pricing equation (30) for different strike values (35 and 36) as a z-transform with  $z_l = e^{-i\Delta v \Delta \kappa l}$ :

$$C_{0l} = 2S_0 e^{(\beta - 1)\kappa_l - rT} \operatorname{Re} \sum_{k=0}^{n-1} e^{i\Delta v \Delta \kappa kl} a_j \qquad (37)$$

$$a_j = w_j \frac{e^{ij\Delta v \kappa_{\text{max}}} \phi(-\mathrm{i} v_j)}{2\pi v_j (v_j - 1)}$$
(38)

Setting  $\triangle v \triangle \kappa = \frac{2\pi}{n}$ , Carr and Madan obtained a DFT in equation (37). Chourdakis [11] points out that one can evaluate equation  $(37)$  by means of a fractional FFT with  $\triangle v \triangle \kappa \neq \frac{2\pi}{n}$ . For the discussion of relative merits of the two strategies, see [7].

## Further Reading

Further applications of FFT appear in  $[1-4, 10, 12,$ 24]. For the latest developments in option pricing using (continuous) Fourier transform, see [6, 8, 9, 19, 21]. Proofs of Propositions 1 and 3 can be found in [7].

## Acknowledgments

I am grateful to Peter Forsyth and Damien Lamberton for their helpful comments.

# References

- Albanese, C., Jackson, K. & Wiberg, P. (2004). A  $[1]$ new Fourier transform algorithm for value at risk, Quantitative Finance 4, 328-338.
- Andersen, L. & Andreasen, J. (2000). Jump diffusion [2] processes: volatility smile fitting and numerical methods

for option pricing, *Review of Derivatives Research* **4**(3), 231–261.

- [3] Andreas, A., Engelmann, B., Schwendner, P. & Wystup, U. (2002). Fast Fourier method for the valuation of options on several correlated currencies, in *Foreign Exchange Risk*, J. Hakala & U. Wystup, eds, Risk Publications.
- [4] Benhamou, E. (2002). Fast Fourier transform for discrete Asian options, *Journal of Computational Finance* **6**(1), 49–68.
- [5] Carr, P. & Madan, D.B. (1999). Option valuation using the fast Fourier transform, *Journal of Computational Finance* **2**, 61–73.
- [6] Carr, P. & Wu, L. (2004). Time-changed Levy processes ´ and option pricing, *Journal of Financial Economics* **71**(1), 113–141.
- [7] Cern ˇ y, A. (2004). Introduction to FFT in finance, ´ *Journal of Derivatives* **12**(1), 73–88.
- [8] Cern ˇ y, A. (2007). Optimal continuous-time hedging ´ with leptokurtic returns, *Mathematical Finance* **17**(2), 175–203.
- [9] Cern ˇ y, A. & Kallsen, J. (2008). Mean–variance hedging ´ and optimal investment in Heston's model with correlation, *Mathematical Finance* **18**(3), 473–492.
- [10] Chiarella, C. & El-Hassan, N. (1997). Evaluation of derivative security prices in the Heath-Jarrow-Morton framework as path integrals using fast Fourier transform techniques, *Journal of Financial Engineering* **6**(2), 121–147.
- [11] Chourdakis, K. (2004). Option pricing using the fractional FFT, *Journal of Computational Finance* **8**(2), 1–18.
- [12] Dempster, M.A.H. & Hong, S.S.G. (2002). Spread option valuation and the fast Fourier transform, in *Mathematical Finance – Bachelier Congress 2000*, H. Geman, D. Madan, S.R. Pliska & T. Vorst, eds, Springer, pp. 203–220.
- [13] Duffie, D., Filipovic, D. & Schachermayer, W. (2003). ´ Affine processes and applications in finance, *The Annals of Applied Probability* **13**(3), 984–1053.
- [14] Duffie, D., Pan, J. & Singleton, K. (2000). Transform analysis and asset pricing for affine jump diffusions, *Econometrica* **68**, 1343–1376.
- [15] Duhamel, P. & Vetterli, M. (1990). Fast Fourier transforms: a tutorial review and a state of the art, *Signal Processing* **19**, 259–299.

- [16] Eberlein, E., Keller, U. & Prause, K. (1998). New insights into smile, mispricing and value at risk: the hyperbolic model, *Journal of Business* **71**(3), 371–405.
- [17] Frigo, M. & Johnson, S.G. (1998). FFTW: an adaptive software architecture for the FFT, *Proceedings of IEEE International Conference on Acoustics, Speech, and Signal Processing*, Seattle, WA, Vol. 3, pp. 1381–1384.
- [18] Heston, S. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–344.
- [19] Hubalek, F., Kallsen, J. & Krawczyk, L. (2006). Variance-optimal hedging for processes with stationary independent increments, *The Annals of Applied Probability* **16**, 853–885.
- [20] Kallsen, J. (2006). A didactic note on affine stochastic volatility models, in *From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift*, Y. Kabanov, R. Liptser & J. Stoyanov, eds, Springer, Berlin, pp. 343–368.
- [21] Kallsen, J. & Vierthauer, R. (2009). Variance-optimal hedging in affine stochastic volatility models, *Review of Derivatives Research* **12**(1), 3–27.
- [22] Lee, R.W. (2004). Option pricing by transform methods: extensions, unification and error control, *Journal of Computational Finance* **7**(3), 1–15.
- [23] Madan, D. & Seneta, E. (1990). The variance gamma model for stock market returns, *Journal of Business* **63**(4), 511–524.
- [24] Rebonato, R. & Cooper, I. (1998). Coupling backward induction with monte carlo simulations: a fast Fourier transform (FFT) approach, *Applied Mathematical Finance* **5**(2), 131–141.
- [25] Temperton, C. (1992). A generalized prime factor FFT algorithm for any *n* = 2*<sup>p</sup>*3*<sup>q</sup>* 5*<sup>s</sup>*, *SIAM Journal on Scientific and Statistical Computing* **13**, 676–686.

# **Related Articles**

**Exponential Levy Models ´** ; **Fourier Methods in Options Pricing**; **Wavelet Galerkin Method**.

ALESˇ Cˇ ERNY´
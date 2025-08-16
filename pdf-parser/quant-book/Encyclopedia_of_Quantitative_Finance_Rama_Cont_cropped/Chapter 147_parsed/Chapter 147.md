# Implied Volatility: Large **Strike Asymptotics**

Let  $S_t$  be the price of a risky asset at time  $t \in [0, T]$  and  $B_t = B(t, T)$  the time-t value of one monetary unit received at time  $T$ . Assuming suitable no-arbitrage conditions, there exists a probability measure  $\mathbb{P} = \mathbb{P}_T$ , called the (*T*-forward) *pricing measure*, under which the  $B_t$ -discounted asset price

$$F_t = F(t, T) = S(t) / B(t, T)$$
(1)

is a martingale and so are  $B_t$ -discounted time-t option prices, such as  $C_t/B(t,T)$ , where  $C_t$  denotes the time- $t$  value of a European call option with maturity T and payoff  $(S_T - K)^+$ . With focus on  $t = 0$  and writing  $C$  instead of  $C_0$ , we have

$$C = B(0, T) \mathbb{E}\left[C_T/B(T, T)\right] \tag{2}$$

$$= B (0, T) \mathbb{E} \left[ (F_T - K)^+ \right]$$
$$= S_0 \mathbb{E} \left[ \left( \frac{F_T}{F_0} - \frac{K}{F_0} \right)^+ \right] \tag{3}$$

Let us remark that in the case of deterministic interest rates  $r(\cdot)$ , one can rewrite this as<sup>a</sup>

$$C = \mathbb{E}\left[\exp\left(-\int_{0}^{T} r\left(u\right) \, \mathrm{d}u\right) \left(S_{T} - K\right)^{+}\right] \quad (4)$$

If we now make the assumption that there exists  $\sigma > 0$ , the Black-Scholes volatility, such that  $F_t$ satisfies

$$dF_t = \sigma F_t \, dW \tag{5}$$

where W is a Brownian motion under  $\mathbb{P}$ , then we have *normal returns*  $X_{\text{BS}} := \log (F_T/F_0)$ . More precisely,

$$X_{\text{BS}} \sim \text{Normal}\left(-V^2/2, V^2\right) \text{ with } V \equiv \sigma\sqrt{T} \quad (6)$$

and an elementary integration of equation (3) yields the classical Black-Scholes formula,<sup>b</sup>

$$C_{\text{BS}} = S_0 \left\{ \Phi \left( d_1 \right) - \frac{K}{F_0} \Phi \left( d_2 \right) \right\} \tag{7}$$

with  $d_{1,2} = -\log(K/F_0)/V \pm V/2$ . It follows that we can express the normalized Black-Scholes call price

$$c_{\text{BS}} := C_{\text{BS}} / S_0 \tag{8}$$

as a function of two variables: *log-strike*  $k :=$  $\log(K/F_0)$  and (scaled) *Black–Scholes volatility*  $V = \sigma \sqrt{T}$ .

$$c_{\text{BS}}(k, V) = \Phi(d_1) - e^k \Phi(d_2)$$
  
with  $d_{1,2} = -k/V \pm V/2$  (9)

Let us now return to the general setting and just assume that, for fixed  $T$ , the *returns* 

$$X := \log \frac{F_T}{F_0} \tag{10}$$

have a known distribution, fully specified by the probability distribution function

$$F(x) := \mathbb{P}[X \le x] \tag{11}$$

From equation (2), the value of a normalized call price  $c = C/S_0$  is then given by

$$\mathbb{E}\left[\left(\frac{F_T}{F_0} - e^k\right)^+\right] = \int_{-\infty}^{\infty} \left(e^x - e^k\right)^+ dF(x)$$
$$=: c(k) \tag{12}$$

**Definition 1** (Implied volatility). Let  $T > 0$  be a fixed maturity and assume  $F$  is the distribution function of the returns  $\log (F_T/F_0)$  under the pricing measure. Then, the scaled (Black-Scholes) implied volatility is the unique value  $V(k)$  such that

$$c(k) = c_{\text{BS}}(k, V(k)) \quad \text{for all } k \in \mathbb{R} \tag{13}$$

We also write  $\sigma$   $(k, T) := V(k) / \sqrt{T}$  for the (annualized, Black-Scholes) implied volatility.

By the very definition, the volatility smile  $V(\cdot, T)$ is flat, namely constant equal to  $V = \sigma \sqrt{T}$ , in the Black-Scholes model. To see existence/uniqueness of implied volatility, in general, it suffices to note that  $c_{\text{BS}}(k, \cdot)$  is strictly increasing in the volatility parameter and that

 $c_{\text{BS}}(k, V=0)$  $= \left(1 - \mathrm{e}^{k}\right)^{+} \leq \mathbb{E}\left[\left(F_{T}/F_{0} - \mathrm{e}^{k}\right)^{+}\right] = c\left(k\right) \quad (14)$ 

$$c(k) \le \mathbb{E}[F_T/F_0] = 1 = c_{\text{BS}}(k, V = +\infty)$$
 (15)

It is clear from the afore mentioned monotonicity of  $c_{\text{BS}}(k, \cdot)$  that the fatness of the tail of the returns, for example, the behavior of

$$\overline{F}(k) = 1 - F(k) = \mathbb{P}[X > k] \text{ as } k \to \infty \quad (16)$$

is related to the shape of the "wing" of the implied volatility (smile) for far-out-of-the-money calls,  $V(k)$ as  $k \to \infty$ , and similarly, for  $F(k)$ ,  $V(k)$  as  $k \to \infty$  $-\infty$ . Surprisingly, perhaps, this link can be made very explicit. Let us agree that if  $F$  admits a density, it is denoted by  $f = F'$ . Let us also adopt the common convention that

$$g(k) \sim h(k)$$
 means  $g(k)/h(k) \to 1$  as  $k \to \infty$  (17)

The (meta) result is the following *tail-wing formula*: as  $k \to \infty$  we have

$$V(k)^{2}/k \sim \psi \left[ -1 - \log \bar{F}(k) / k \right]$$
  
 
$$\sim \psi \left[ -1 - \log f(k) / k \right] \qquad (18)$$

$$V(-k)^{2}/k \sim \psi \left[ -\log F \left( -k \right) / k \right]$$
  
 
$$\sim \psi \left[ -\log f \left( -k \right) / k \right] \tag{19}$$

where

$$\psi(x) \equiv 2 - 4\left(\sqrt{x^2 + x} - x\right)\n$$
(20)

An interesting special case arises when either

$$p^* = \sup \left\{ p \in \mathbb{R} : M \left( 1 + p \right) < \infty \right\} \tag{21}$$

$$q^* = \sup \left\{ q \in \mathbb{R} : M(-q) < \infty \right\} \tag{22}$$

is finite, where  $M$  is the *moment generating function* of  $F$ , and this is equivalent to *moment explosion* of the underlying since

$$M(u) := \int e^{ux} dF(x) = \frac{1}{F_0^u} \mathbb{E}\left[F_T^u\right] = \frac{1}{F_0^u} \mathbb{E}\left[S_T^u\right]$$
(23)

In this case, one expects an exponential tail so that

$$-\log \bar{F}(k) \sim (p^* + 1)k \tag{24}$$

$$-\log F(-k) \sim q^*k \tag{25}$$

and one is led to Lee's moment formula

$$V(k)^{2}/k \sim \psi(p^{*})$$
  
$$V(-k)^{2}/k \sim \psi(q^{*})$$
 (26)

Recall that  $g(k) \sim h(k)$  stands for the precise mathematical statement that  $\lim_{k \to \infty} g(k) / h(k) \to 1$  as  $k \to \infty$  $\infty$ . In the same spirit, let us agree that

$$g(k) \lesssim h(k)$$
 means  $\limsup g(k) / h(k) \to 1$   
as  $k \to \infty$  (27)

**Proposition 1** (Lee's Moment Formula; [3, 8]). Assume  $\mathbb{E}[e^X] = \mathbb{E}[S_T]/F_0 < \infty$ . The moment formula then holds in complete generality in "limsup" form. More precisely, as  $k \to \infty$ ,

$$V(k)^{2}/k \lesssim \psi\left(p^{*}\right) \tag{28}$$

$$V(-k)^2/k \lesssim \psi\left(q^*\right) \tag{29}$$

The power of the moment formula comes from the fact that the critical exponents  $p^*, q^*$  can often be obtained by sheer inspection of a moment generating function known in closed form. One can also make use of the recent literature on moment explosions to obtain such critical exponents in various stochastic volatility models; see **Moment Explosions** and the references therein. Let us note that it is possible [4] to construct (pathological) examples to see that one cannot hope for a genuine limit form of the above moment formula, as was suggested in (26). Another remark is that the moment formula provides little information in the absence of moment explosion. For instance,  $p^* = +\infty$  only implies  $V(k)^2 = o(k)$  but gives no further information about the behavior of  $V(k)$  for large k. Both the issues are dealt with by the tail-wing formula. The key assumptions is a certain well behavedness of  $F$ ; but only on a crude logarithmic scale and, therefore, rather easy to check in many examples.

**Definition 2** (Regular Variation; [5]). A positive, real-valued function  $f$ , defined at least on  $[M, \infty)$ for some large  $M$ , is said to be regularly varying of *index*  $\alpha$  *if for all*  $\lambda > 0$ 

$$f(\lambda k) \sim \lambda^{\alpha} f(k) \text{ as } k \to \infty \ \forall \lambda > 0 \tag{30}$$

and in this case we write  $f \in R_{\alpha}$ .

**Theorem 1** (Right-hand Tail-wing Formula; [2]). Assume  $\exists \epsilon > 0$ :  $\mathbb{E}[\mathrm{e}^{(1+\epsilon)X}] = \mathbb{E}\left[S_{T}^{1+\epsilon}\right]/F_{0}^{1+\epsilon} < \infty.$ Let also  $\alpha > 0$  and set

$$\psi(x) \equiv 2 - 4\left(\sqrt{x^2 + x} - x\right) \tag{31}$$

Then  $(i) \Longrightarrow (ii) \Longrightarrow (iii) \Longrightarrow (iv)$  where

(i) 
$$-\log f(k) \in R_{\alpha};$$

(ii) 
$$-\log \bar{F}(k) \in R_{\alpha};$$

(iii) 
$$-\log c(k) \in R_{\alpha};$$

and

(iv) 
$$V(k)^{2}/k \sim \psi \left[ -\log c \left( k \right) / k \right].$$

If (ii) holds, then  $-\log c(k) \sim -k - \log \bar{F}$  and

(iv') 
$$V(k)^{2}/k \sim \psi \left[ -1 - \log \bar{F}(k) / k \right],$$

if (i) holds, then  $-\log f \sim -\log \bar{F}$  and

(iv'') 
$$V(k)^{2}/k \sim \psi \left[ -1 - \log f(k) / k \right]$$

Of course, there is a similar left-hand result, which we state such as to involve far-out-of-the-money (normalized) European puts,

$$p(k) := \int_{-\infty}^{\infty} \left( e^k - e^x \right)^+ dF(x) \qquad (32)$$

**Theorem 2** (Left-hand Tail-wing Formula). *Assume*  $\exists \epsilon > 0 : \mathbb{E}[\mathrm{e}^{-\epsilon X}] < \infty.$  Then (i) (ii) (iii)  $\Longrightarrow$ (iv) where

(i) 
$$-\log f(-k) \in R_{\alpha};$$

 $-\log F(-k) \in R_{\alpha};$ (ii)

(iii) 
$$-\log p(-k) \in R_{\alpha};$$

and

(iv) 
$$V(-k)^2/k \sim \psi[-1 - \log p(-k)/k].$$

If (ii) holds, then 
$$-\log p(-k) \sim k - \log F(-k)$$
  
and

(iv') 
$$V(-k)^2/k \sim \psi\bigl[-\log F(-k)/k\bigr],$$

if (i) holds, then 
$$-\log f(-k) \sim -\log F(-k)$$

 $and$ 

(iv") 
$$V(-k)^2/k \sim \psi\bigl[-\log f(-k)/k\bigr].$$

With focus on the right-hand tail-wing, let us single out two cases of particular importance in applications.

1. (Asymptotically Linear Regime) If  $-1 \log f(k) / k$  or  $-1 - \log \overline{F}(k) / k$  converges to  $p^* \in (0, \infty)$  then

$$V(k)^{2} \sim \psi(p^{*}) \times k \tag{33}$$

and the *implied variance*, defined as the square of implied volatility, is asymptotically linear with slope  $\psi$  ( $p^*$ ). One can, in fact, check this from the moment generating function of  $X$ . Indeed, it is shown in [3] that if

$$s \mapsto M(1 + p^* - 1/s) \tag{34}$$

is regularly varying then  $-\log f(k)/k \rightarrow$  $p^*+1$ . In other words, to ensure equation (26), that is, a genuine limit in Lee's moment formula, one needs some well behavedness of the  $M$  as its argument approaches the critical exponent  $1 + p^*$ . Similar conditions can be given with  $M$  replaced by  $M'$  or  $\log M$ and these conditions are, indeed, easy to check in a number of familiar exponential Lévy models (including Barndorff-Nielsen's Normal Inverse Gaussian model, Carr-Madan's Variance Gamma model, or Kou's Double *Exponential model*) and various time changes of these models (see [3] for details).

2. (Asymptotically Sublinear Regime) If - $\log f(k) / k \rightarrow \infty$ , we can use  $\psi(x) \sim 1/(2x)$ as  $x \to \infty$  to see that

$$V(k)^{2} \sim \frac{1}{-2\log f(k) / k} \times k = \frac{k^{2}}{-2\log f(k)}$$
(35)

so that the implied variance is asymptotically sublinear. As sanity check, consider the Black-Scholes model where  $f$  is the density of the (normally distributed) returns with variance  $V^2 \equiv \sigma^2 T$ , as given in (6); then  $-\log f(k) \sim k^2/(2V^2)$  and it follows that  $V(k) \sim V$ , in trivial agreement with the flat smile in the Black-Scholes model. Following [2], other examples are given by Merton's jump diffusion as a borderline example in which the sublinear behavior comes from a subtle logarithmic correction term, and Carr-Wu's Finite Moment Logstable model. The tail behavior of the latter, as noted in [2], can be derived from the growth of the (nonexplosive) moment generating function by means of Kasahara's Tauberian theorem [5]. Another example where this methodology works is the SABR model

$$dF = \sigma F^{\beta} dW, \ d\sigma = \eta \sigma dZ \qquad (36)$$

with  $\sigma, \eta > 0, \beta < 1$  and two Brownian motions  $W, Z$  assumed (here) to be independent. Using standard stochastic calculus [4], one can give good enough estimates on  $\mathbb{E}\left[|F_T/F_0|^u\right]$ , from above and below, to see that

$$\log \mathbb{E}\left[|F_T/F_0|^u\right] = \log \mathbb{E}\left[\exp\left(uX\right)\right]$$
$$\sim \frac{\eta^2 T}{\left(1-\beta\right)^2} \frac{u^2}{2} \text{ as } u \to \infty \tag{37}$$

From this, Kasahara's theorem allows to deduce the tail behavior of  $X$ , namely

$$-\log \mathbb{P}\left[X>x\right] \sim \frac{(1-\beta)^2}{\eta^2 T} \frac{x^2}{2} \tag{38}$$

and the (right hand) tail-wing formula reveals that the implied volatility in the SABR model is asymptotically flat,  $\sigma(k, T) \sim \eta/(1 - \beta)$  as  $k \to \infty$ .

Early contributions in the study of smile asymptotics are  $[1, 6]$ . The moment formula appears in  $[8]$ , the tail-wing formula in [2] with some additional criteria in  $[3]$ . A survey on the topic, together with some new examples (including CEV and SABR) is found in  $[4]$ . Further developments in the field include the refined asymptotic results of Gulisashvili and Stein [7]; in a simple log-normal stochastic volatility model of the form  $dF = \sigma F dW$ ,  $d\sigma = \eta \sigma dZ$ , with two independent Brownian motions  $W$ ,  $Z$  they find

$$\sigma(k,T)\sqrt{T} = \sqrt{2k} - \frac{\log k + \log\log k}{2\eta\sqrt{T}} + O(1)$$
(39)

The leading order term  $\sqrt{2k}$  says that implied variance grows linearly with slope 2, as one expects in a model with immediate moment explosion.

### Acknowledgments

Financial support form the Cambridge Endowment of Research in Finance is gratefully acknowledged.

#### End Notes

<sup>a</sup>. Equation  $(4)$  is valid in a nondeterministic interest rate setting, provided the expectation is taken with respect to the risk-neutral measure (which is equivalent but, in general, not identical to  $\mathbb{P}_T$ ).

<sup>b.</sup> $\Phi$  denotes the distribution function of normal (0, 1).

#### References

- [1] Avellaneda, M. & Zhu, Y. (1998). A risk-neutral stochastic volatility model, International Journal of Theoretical and Applied Finance  $1(2)$ , 289–310.
- [2] Benaim, S. & Friz, P.K. (2009). Regular variation and smile asymptotics, *Mathematical Finance*  $19(1)$ , 1–12, eprint arXiv:math/0603146.
- [3] Benaim, S. Friz, P.K. (2008). Smile asymptotics II: models with known MGF, Journal of Applied Probability 45(1), 16-32.
- Benaim, S. Friz, P.K. & Lee, R. (2008). The [4] Black-Scholes implied volatility at extreme strikes, in frontiers, in *Quantitative Finance: Volatility and Credit* Risk Modeling, Chapter 2, Wiley.
- [5] Bingham, N.H. Goldie, C.M. & Teugels, J.L. (1987). Regular Variation, CUP.
- [6] Gatheral, J. (2000). Rational shapes of the Volatility Surface, Presentation, RISK Conference.
- [7] Gulisashvili, A. & Stein, E. Implied volatility in the Hull–White model, *Mathematical Finance*, to appear.
- [8] Lee, R. (2004). The moment formula for implied volatility at extreme strikes, *Mathematical Finance*  $14(3)$ , 469-480.

## **Further Reading**

Gatheral, J. (2006). The Volatility Surface, A Practitioner's Guide, Wiley.

PETER K. FRIZ
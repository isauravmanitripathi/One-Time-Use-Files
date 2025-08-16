## **Call Options**

Call options appeared as rights to buy an underlying traded asset for a prespecified price, named the *option strike* or the *exercise price*, at a prespecified future date named the *option expiry* or the *maturity*. Put options are analogous rights to sell an underlying asset. For strike *K* and maturity *T* with the underlying asset trading at maturity for *S*, the call expires unexercised if *S* is below *K* while the put expires unexercised if *S* is above *K.* On exercise, the value of the call option is *S* − *K* while that of the put option is *K* − *S.* Hence, one may write the payoffs at maturity to the call and put options as *(S* − *K)*<sup>+</sup> and *(K* − *S)*<sup>+</sup>, respectively. More generally, one may define a call or put payoff for any underlying random variable, which need not be a traded asset, for which the realized value at maturity is known to be *A,* as *(A* − *K)*<sup>+</sup> and *(K* − *A)*<sup>+</sup>, respectively.

When call and put options trade before the maturity, on an underlying uncertainty resolved at maturity for various strikes *K,* with prices determined in markets at time *t<T* as *c(t, K, T ), p(t, K, T )*, respectively, we have an options market for the underlying risk. Such markets provide a rich source of opportunities for holding the underlying asset or risk while simultaneously providing information on the prices of these risks. With regard to the opportunities, they make it possible to hold any function *f (A)* of the underlying risk *via* a portfolio of put and call options. This fact is easily demonstrated as follows [2].

Let *f (A)* be the function we wish to hold. We note that

$$f(A) = f(a) + \mathbf{1}_{A>a} \int_{a}^{A} f'(u) \, du - \mathbf{1}_{a>A} \int_{A}^{a} f'(u) \, du$$
  
$$= f(a) + \mathbf{1}_{A>a} \int_{a}^{A} \left[ f'(a) + \int_{a}^{u} f''(v) \, dv \right] du$$
  
$$- \mathbf{1}_{a>A} \int_{A}^{a} \left[ f'(a) - \int_{u}^{a} f''(v) \, dv \right] du$$
  
$$= f(a) + f'(a)(A - a) + \mathbf{1}_{A>a}$$
  
$$\times \int_{a}^{A} dv f''(v)(A - v)$$
  
$$+ \mathbf{1}_{a>A} \int_{A}^{a} dv f''(v)(v - A)$$

$$= f(a) + f'(a)(A - a) + \mathbf{1}_{A>a}$$
$$\times \int_{a}^{\infty} dv f''(v)(A - v)^{+}$$
$$+ \mathbf{1}_{a>A} \int_{0}^{a} dv f''(v)(v - A)^{+} \tag{1}$$

On the right hand side, we have a position in a bond with face value given by the constant term, a position in the underlying risk of *f (a)* and a position in puts struck below *a* and calls struck above a at strike *ν* of *f (ν)*.

With regard to the information content of the market prices, we consider Breeden and Litzenberger [1], who showed how one may extract the pricing density at time *t < T , p(t, A)* for the underlying risk from market option prices. By definition, we have

$$c(t, K, T) = e^{-r(T-t)} \int_{K}^{\infty} (A - K)p(t, A) \, dA \quad (2)$$

where *r* is the interest rate prevailing at time *t* for the maturity *(T* − *t).* We may differentiate twice with respect to the strike to get

$$p(t, K) = e^{r(T-t)} \frac{\partial^2 c(t, K, T)}{\partial K^2}$$
(3)

In the case when the underlying risk is an asset price with a specific dynamics with exposure to a Brownian motion with a space–time deterministic volatility (*see* **Local Volatility Model**) as postulated by Dupire [6] plus a compensated jump martingale with a space–time deterministic arrival rate of jumps and a fixed dependence of the arrival rate on the jump size, one may extract information on the dynamics from market prices. Here, we follow Carr *et al.* [4]. Let *(S(t), t >* 0*)* denote the path of the stock price, where *r* is the interest rate, *η* the dividend yield, *σ (S, t)* the deterministic space–time volatility function, *(W (t), t >* 0*)* a Brownian motion, *m(dx, ds)* the integer-valued counting measure associated with the jumps in the logarithm of the stock price, *a(S, t)* the deterministic space–time jump arrival rate, and *k(x)* the Levy density across jump sizes ´ *x.* The dynamics for the stock price may be written as

$$S(t) = S(0) + \int_0^t S(u_{-})(r - \eta) du$$
  
+ 
$$\int_0^t S(u_{-})\sigma(S(u_{-}), u) dW(u)$$

$$+\int_0^t \int_{-\infty}^\infty S(u_-) \left(e^x - 1\right) (m(\mathrm{d}x, \mathrm{d}u)$$
$$-a(S(u_-), u)k(x) \, \mathrm{d}x \, \mathrm{d}u) \tag{4}$$

We now apply a generalization of Itô's lemma to convex functions known as the Meyer-Tanaka for*mula* (see, e.g., [5, 7, 8] for the specific formulation below) to the call option payoff at maturity to obtain

$$(S(T) - K)^{+} = (S(0) - K)^{+} + \int_{0}^{T} \mathbf{1}_{S(u_{-}) > K} \mathrm{d}S(u)$$
  
+  $\frac{1}{2} \int_{0}^{T} \delta_{K}(S(u_{-})) \sigma^{2}$   
 $\times (S(u), u) S^{2}(u) \, \mathrm{d}u$   
+  $\sum_{u \leq T} \mathbf{1}_{S(u_{-}) > K} (K - S(u))^{+}$   
+  $\mathbf{1}_{S(u_{-}) < K} (S(u) - K)^{+}$  (5)

The second integral denotes the value at  $K$ of the continuous local time  $L_T^a; a \in \mathbb{R}$ , which is globally defined for every bounded Borel function  $f$ , as  $\int_{-\infty}^{\infty} f(a) L_T^a da = \int_0^T f(S(u_-)) d \langle S^c \rangle_u$ , where  $d\langle S^c \rangle_u = \sigma^2(S(u), u)S^2(u)du$ , and is applied here formally to the Dirac measure  $f(a) = \delta_K(a)$ . The last term, which is the discontinuous component of local time at level  $K$ , is made up of just the crossovers, whereby one receives  $S(u) - K$  on crossing the strike into the money, whereas one receives  $(K - S(u))$  on crossing the strike out of the money.

Computing expectations on both sides of equation (5) and introducing  $q(\Sigma, u)$ , the transition density that the stock price is  $\Sigma$  at time *u* given that at time 0 it is at  $S(0)$ , we may write the call price function at time zero as

$$\begin{split} \mathrm{e}^{rT} C(K,T) &= (S(0) - K)^{+} \\ &+ \int_{0}^{T} \int_{K}^{\infty} \mathrm{d}Y \; q(Y,u) Y(r-\eta) \, \mathrm{d}u \\ &+ \frac{1}{2} \int_{0}^{T} q(K,u) \sigma^{2}(K,u) K^{2} \, \mathrm{d}u \\ &+ \int_{0}^{T} \int_{K}^{\infty} \mathrm{d}Y \; q(Y,u) a(Y,u) \\ &\times \int_{-\infty}^{\ln\left(\frac{K}{Y}\right)} (K - Y \mathrm{e}^{x}) k(x) \, \mathrm{d}x \mathrm{d}u \end{split}$$

$$+ \int_{0}^{T} \int_{0}^{K} dY \ q(Y, u) a(Y, u)$$
$$\times \int_{\ln\left(\frac{K}{Y}\right)}^{\infty} (Ye^{x} - K) k(x) \, dx \, du \ (6)$$

Now differentiating equation  $(6)$  with respect to  $T$ , we get

$$re^{rT}C + e^{rT}C_{T}$$

$$= (r - \eta) \int_{K}^{\infty} q(Y, T^-)YdY$$

$$+ \frac{\sigma^{2}(K, T^-)K^{2}}{2} q(K, T^-)$$

$$+ \int_{K}^{\infty} dYYq(Y, T)a(Y, T) \int_{-\infty}^{\ln\left(\frac{K}{Y}\right)} \left(e^{\ln\left(\frac{K}{Y}\right)} - e^{x}\right)$$

$$\times k(x) dx + \int_{0}^{K} dYYq(Y, T)a(Y, T)$$

$$\times \int_{\ln\left(\frac{K}{Y}\right)}^{\infty} \left(e^{x} - e^{\ln\left(\frac{K}{Y}\right)}\right) k(x) dx \tag{7}$$

We now isolate  $C_T$  on the left, using some elementary properties of the relationship between call prices and the pricing density. In particular, we note

$$e^{-rT} \int_0^\infty Yq(Y,T) dY = C - KC_K \qquad (8)$$
$$e^{-rT} q(K,T) = C_{KK} \qquad (9)$$

and obtain

$$C_{T} = -\eta C - (r - \eta)KC_{K}$$
  
+ 
$$\frac{\sigma^{2}(K, T)K^{2}}{2}C_{KK}$$
  
+ 
$$\int_{K}^{\infty} dY \ Y \ C_{YY} \ a(Y, T)$$
  
$$\times \int_{-\infty}^{\ln\left(\frac{K}{Y}\right)} \left(e^{\ln\left(\frac{K}{Y}\right)} - e^{x}\right)k(x) dx$$
  
+ 
$$\int_{0}^{K} dY \ Y \ C_{YY} \ a(Y, T)$$
  
$$\times \int_{\ln\left(\frac{K}{Y}\right)}^{\infty} \left(e^{x} - e^{\ln\left(\frac{K}{Y}\right)}\right)k(x) dx \quad (10)$$

We may define the function

$$\psi(x) = \mathbf{1}_{x<0} \int_{-\infty}^{x} (e^{x} - e^{s}) k(s) \, ds$$
$$+ \int_{x}^{\infty} (e^{s} - e^{x}) k(s) \, ds \tag{11}$$

and then write

$$C_{T} = -\eta C - (r - \eta)KC_{K}$$
$$+ \frac{\sigma^{2}(K, T)K^{2}}{2}C_{KK}$$
$$+ \int_{0}^{\infty} C_{YY}Ya(Y, T)\psi\left(\ln\left(\frac{K}{Y}\right)\right)dY \tag{12}$$

When there are no jumps in the process for  $X$  and  $\psi \equiv 0$ , equation (12) is identical to the formula in [6] for local volatility (see **Dupire Equation**). In the opposite case, when there is no continuous martingale component, we have the following result:

$$C_{T} + \eta C + (r - \eta)KC_{K}$$
  
= 
$$\int_{0}^{\infty} C_{YY} Ya(Y, T) \psi \left( \ln \left( \frac{K}{Y} \right) \right) dY \quad (13)$$

It is now useful to rewrite equation  $(13)$  in terms of  $k = \ln(K)$ ,  $y = \ln(Y)$ , and  $c(k, T) = C(e^k, T)$ . With this substitution, we may rewrite equation  $(12)$  as

$$c_T + \eta c + \left(r - \eta + \frac{\sigma^2(\mathbf{e}^k, T)}{2}\right) c_k$$
$$- \frac{\sigma^2(\mathbf{e}^k, T)}{2} c_{kk} = \int_{-\infty}^{\infty} b(y, T) \psi_e(k - y) \, \mathrm{d}y \tag{14}$$

where  $b(y, T) = e^{2y}C_{YY}a(e^y, T)$ . The forward speed function,  $a(Y, T)$ , may be identified as

$$a(Y,T) = \frac{b(\ln(Y),T)}{Y^2 C_{YY}} \tag{15}$$

For specific Lévy measures, the convolution equation (14) may be solved in closed form to yield explicit solutions for the Markov process from data on option prices (see Fourier Methods in

## Options Pricing; Partial Integro-differential Equations (PIDEs)).

Apart from spanning all functions of the underlying risk and providing us with information on the possible dynamic movements of the stock price consistent with market option prices, we have the question of understanding the absence of arbitrage between option prices. This question was addressed in [3], where it was shown that if call spread, butterfly spread, and calendar spread arbitrages are excluded then the option quotes are free of static arbitrage. It is, therefore, important to document the three arbitrages that need to be checked. For a call spread, we have the inequality for two strikes  $K_1 < K_2$  for a fixed maturity  $T$ :

$$\frac{c(K_1,T) - c(K_2,T)}{K_2 - K_1} < 1$$

For a butterfly spread, we have three strikes  $K_1 <$  $K_2 < K_3$  and a fixed maturity T for which we must have

$$c(K_1, T) - \left(\frac{K_3 - K_1}{K_3 - K_2}\right) c(K_2, T) + \frac{K_2 - K_1}{K_3 - K_2} c(K_3, T) \ge 0 \tag{16}$$

Finally, the calendar spread inequality requires that for two maturities  $T_1 < T_2$  and strike K

$$c(K, T_2) \ge c(Ke^{-r(T_2-T_1)}, T_1)$$
 (17)

Similar results hold for put options *via* put-call parity that asserts in the case of a stock

$$p(K,T) = c(K,T) + K - S(0)e^{-\eta T}$$
(18)

The call spread inequality approximates the probability that the stock exceeds  $K_1$  when we take  $K_2$ close to and above  $K_1$ . The butterfly spread inequality guarantees the existence of a positive pricing density and the calendar spread inequality arranges these densities to be increasing in the convex order with respect to the maturity. When the underlying risk is not a traded asset as occurs, for example, for options on the VIX index where the underlying is the price of the one month variance swap, we lose the calendar spread inequality and the requisite densities are not increasing in the convex order. One can check that on most days VIX call option prices when deflated by the forward VIX are increasing in maturity for given strikes and we have an empirical increase in the convex order, but there are days when this monotonicity is lost. The conditions for VIX option surfaces to be free of arbitrage are, therefore, not as clear as they are for an underlying stock or a stock index.

## **References**

- [1] Breeden, D. & Litzenberger, R.L. (1978). Pricing of statecontingent claims implicit in option prices, *Journal of Business* **51**, 621–651.
- [2] Carr, P. & Madan, D.B. (2001). Optimal positioning in derivatives, *Quantitative Finance* **1**, 19–37.
- [3] Carr, P. & Madan, D.B. (2005). A note on sufficient conditions for no arbitrage, *Finance Research Letters* **2**, 125–130.

- [4] Carr, P., Geman, H., Madan, D. & Yor, M. (2005). From local volatility to local Levy models, ´ *Quantitative Finance* **4**, 581–588.
- [5] Dellacherie, C. & Meyer, P. (1980). *Probabilit´es et Potentiel, Theorie des Martingales*, Hermann, Paris.
- [6] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- [7] Meyer, P. (1976). Un Cours sur les Integrales stochas- ´ tiques, in *S´eminaire de Probabilit´es X*, Lecture Notes in Mathematics, Springer-Verlag, Berlin, Vol. 511.
- [8] Yor, M. (1978). Rappels et Preliminaires G ´ en´ eraux, ´ in *Temps Locaux*, *Soci´et´e Math´ematique de France*, Asterisque, pp. 17–22, 52–53. ´

## **Related Articles**

**Dupire Equation**; **Local Volatility Model**; **Put–Call Parity**; **Static Hedging**; **Variance Swap**.

DILIP B. MADAN
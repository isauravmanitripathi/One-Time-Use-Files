# **Convexity Adjustments**

The notion of convexity adjustment (or convexity correction) in fixed income markets arises when one uses prices of standard (plain vanilla) products corrected by an *adjustment* to price nonstandard products.

Many fixed income products are nonstandard with respect to aspects such as the timing, the currency, or the rate of payment. Examples of such adjustments can be found in approximations for pricing formulae of products such as in-arrears or inadvance products, quanto products, constant maturity swaps (CMS) products, or equity swaps. Despite their nonstandard features, these products are quite similar to plain vanilla ones whose price can either be directly obtained from the market or at least computed in closed form. Thus, adjustments of plain vanilla prices can be understood as corrections needed to capture the bias introduced in prices by the complexities of the nonstandard products. Taking this effect into account correctly could provide financial institutions with a competitive advantage. Examples of particular interest for practitioners include

- yield convexity adjustments;
- forward *versus* futures price adjustments;
- modified schedule or timing adjustments; and
- mismatch between currencies or quanto adjustments.

The yield convexity adjustment is somewhat unrelated to the remaining adjustments, but it is probably the "original one" in the sense that it is related to the nonlinear (and convex) relationship between bond prices and their yield to maturity. The three remaining adjustments have traditionally been separated, both by practitioners and academics, as they concern different classes of products. Various *ad hoc* rules have been proposed in the literature to calculate a variety of convexity adjustments for different products. Many of them are, however, mutually inconsistent. Nonetheless, as we explain later, the last three adjustments can be understood as corrections resulting from the fact that by using quotes of plain vanilla products to price nonstandard ones, we are taking expectations under the "wrong" martingale measure. Pelsser [14] was the first to put convexity adjustments on a firm mathematical basis by showing that they can be interpreted as the side effect of changes in probability measures. To understand this connection, recall that in a stochastic interest rate setting, the no arbitrage price  $\pi$ , at time t, of any derivative paying  $\Phi(T)$  at maturity  $T$  is given by

$$\pi(t,\,\Phi) = \mathbb{E}_{t}^{\mathcal{Q}} \left[ e^{-\int_{t}^{T} r_{u} du} \Phi(T) \right]$$
$$= p(t,T) \mathbb{E}_{t}^{T} \left[ \Phi(T) \right] \tag{1}$$

where  $p(t, T)$ , denotes the price at time t of a pure discount bond with maturity T and  $\mathbb{E}^Q_t[\cdot], \mathbb{E}^T_t[\cdot],$ denote expectation under the risk-neutral and the  $T$ -forward measure, respectively, conditional on the information available at time  $t$ . When dealing with fixed income derivatives, given the nature of the underlying asset, we are in a stochastic interest rate setting by definition, and, consequently, we are ultimately interested in computing,  $\mathbb{E}^T_t [\Phi(T)]$ , that is, the expected value, under the  $T$ -forward measure where the *numeraire* is  $p(t, T)$ , of our payoff. In the trivial cases, when our payoff turns out to be a  $T$ -forward martingale, we immediately get  $\mathbb{E}^{T}_{t}[\Phi(T)] = \Phi(t)$ . Unfortunately, this is *not* the case in most situations. Even if our payoff is not a martingale under the appropriate  $T$ -forward measure, it could be a martingale under some martingale measure,  $\mathbb{Q}^{\Phi}$ . This is obviously a restrictive assumption, but as it turns out, it includes many popular interest rate products. Suppose, therefore, our payoff is a martingale under the  $\mathbb{O}^{\Phi}$  martingale measure. Then we know  $\Phi(t) = \mathbb{E}^{\Phi}_{t} [\Phi(T)]$ , and we can define the convexity adjustment as the term  $CC^{\Phi}$  for which the following holds:

$$\mathbb{E}_{t}^{T} \left[ \Phi(T) \right] = \Phi(t) + CC^{\Phi}(t) \tag{2}$$

From the martingale properties of our payoff we get  $\Phi(t) = \mathbb{E}^{\Phi}_{t} [\Phi(T)] = \mathbb{E}^{T}_{t} [\Phi(T) \Lambda(T)],$  where  $\Lambda$ denotes the Radon–Nikodym derivative (with  $\Lambda(t)$  = 1). Clearly, the cases where we can say something about  $\mathbb{E}^T_t [\Phi(T) \Lambda(T)]$  are the cases where we can say something about convexity adjustment terms  $CC^{\Phi}$ , which is nothing but a side effect of measure changes. For details concerning Radon–Nikodym derivatives and their relation to measure changes, we refer to [6]. In the following, we address each type of adjustment separately.

#### Yield Convexity Adjustments

Consider a pure discount bond with maturity  $T$ . This section is based on a particular " $T$ -bond", and to ease up notation we always suppress " $T$ ". That is, we simply use  $p(t)$ ,  $y(t)$ , to denote the spot price and yield to maturity of the  $T$ -bond. One of the most commonly used convexity adjustments results from the nonlinear relationship between the bond's price and its yield to maturity  $p(t) = G(v(t))$ . See **Bond**. The exact functional form of  $G$  depends on capitalization assumptions, but it is always a continuous and convex function. Given a concrete  $G$ , one can define the forward bond yield,  $y_f(t, S)$ , as the yield satisfying  $f(t, S) = G(y_f(t, S))$ , where  $f(t, S)$  is the forward price of a contract written on the  $T$ -bond and maturing at time  $S$ . Without loss of generality, we consider  $t \leq S \leq T$ . One way to approximate the price at some future time  $S$  of the  $T$ -bond is to use a second-order Taylor expansion around the  $y_f(t, S)$ yield, that is,

$$p(S) = f(t, S) + G'(y_f(t, S)) [y(S) - y_f(t, S)]$$
  
+ 
$$\frac{1}{2}G''(y_f(t, S)) [y(S) - y_f(t, S)]^2 \qquad (3)$$

We can then take expectations under the  $S$ -forward measure to obtain

$$\mathbb{E}_{t}^{S} \left[ p(S) \right] \approx f(t, S)$$
  
+  $G'(y_{f}(t, S)) \mathbb{E}_{t}^{S} \left[ y(S) - y_{f}(t, S) \right]$   
+  $\frac{1}{2} G''(y_{f}(t, S)) \mathbb{E}_{t}^{S} \left[ y(S) - y_{f}(t, S) \right]^{2}$   
(4)

As  $f(t, S) = \mathbb{E}^{S}[p(S)]$ , we immediately obtain

$$\mathbb{E}_{t}^{S}\left[y(S)\right] \approx y_{f}(t, S)$$
$$-\frac{1}{2} \frac{G''(y_{f}(t, S))}{G'(y_{f}(t, S))} \mathbb{E}^{S}\left[y(S) - y_{f}(t, S)\right]^{2}$$
(5)

and the second term on the right-hand side (RHS) is what is understood as convexity adjustment in this context. It results from the fact that future yields of  $T$ bonds are not today's yields from forward contracts on T-bonds.

A common step to get the convexity adjustment in closed form is to further assume that  $\mathbb{E}^{S}\left[\left(y(S) - y_{f}(t, S)\right)^{2}\right] = \sigma^{2}y(t)^{2}(S - t).$  This adjustment was first proposed in [4, 9] and later sharpened in [8], but it is hard to justify on theoretical grounds. Note that  $\mathbb{E}_{t}^{S}[y(S)] \neq y_{f}(t, S)$ , so  $\mathbb{E}_{t}^{S}\left[\left(y(S)-y_{f}(t, S)\right)^{2}\right]$  cannot be understood as some sort of variance of future yields.

Moreover, the above derived convexity adjustment is an obvious consequence of the Jensen inequality on convex functions, which tells us that for convex G,  $\mathbb{E}[G(y)] > G(\mathbb{E}[y])$ . The Jensen inequality is true under any measure, so, in particular, one could also use futures contracts on  $T$ bonds. As mentioned earlier, we could define the futures bond yield,  $y_F(t, S)$ , as the yield satisfying  $F(t, S) = G(y_F(t, S))$  and using the fact that  $F(t, S) = \mathbb{E}^{Q} [p(S)]$  we would get  $\mathbb{E}_{t}^{Q} [y(S)] \approx$  $y_F(t, S) - \frac{1}{2} \left[ G''(y_F(t, S)) / G'(y_F(t, S)) \right] \mathbb{E}_t^Q \left[ y(S)$  $y_F(t, S)^2$ . Once again, this is hard to interpret, but at least it would have the advantage that futures quotes may be observed directly from the market.

Finally, it is difficult to justify why the expansion should be around the forward bond yield  $y_f(t, S)$  and not directly around today's yield  $y(t)$ .

In our opinion, a more sensible way to study the relationship between a  $T$ -bond price and its yield to maturity is to derive it directly from the dynamics of bond prices. For any risk-neutral " $T$ -bond" dynamics  $dp(t) = r_t p(t) dt + v_t p(t) dW_t^Q$ , no arbitrage arguments allow us to obtain the exact relationship. For instance, in the continuously compounded yield case, we get

$$\mathbb{E}_{t}^{\mathcal{Q}}\left[y(\mathcal{S})\right] = y(t) - \frac{p(t,\mathcal{S}) - \mathbb{E}_{t}^{\mathcal{Q}}\left[\frac{1}{2}\int_{t}^{\mathcal{S}} v_{u}^{2} du\right]}{T - \mathcal{S}}\tag{6}$$

where  $p(t, S)$ , as above, denotes the price at time t of an S-bond. The second term on the left-hand side (LHS) can be understood as a convexity correction, and for any deterministic volatility of bond prices it can be computed in closed form. In particular, this is true for any affine model.

## Forward/Futures Adjustments

A second type of convexity adjustment occurs when we are interested in quoting forward prices on any given underlying while having available futures prices on the same underlying. Recall (see Forwards and Futures) that the difference between futures and forward prices results from the correlation between the underlying to the financial contract and the spot interest rate. As mentioned in [12], this correlation, capitalized by the margin calls of the futures contract, leads to a more expensive (respectively cheaper) futures contract in the case of positive (respectively negative) correlation. Let us denote by  $f(t, T)$  and  $F(t, T)$  the forward and futures prices for contracts with maturity  $T$  on any underlying, respectively. It is a well-known fact that forward prices with maturity  $T$  are martingales under the  $T$ -forward martingale measure, while futures prices are martingales under the  $Q$  risk-neutral measure. For further reading on forward martingale measures, we refer to [1]. The difference in both prices occurs only in a stochastic interest rate setting and is therefore of particular importance when dealing with fixed income products and derivatives. For concrete examples on the difference between futures and forward term structures in a quite general setting (including any affine model), we refer to  $[5]$ .

#### Timing Adjustments

This third cause of adjustment occurs when an interest rate derivative is structured so that it does not incorporate the natural time lag. Examples of products with modified schedule not only are obviously in-arrears products but also include the case of the CMS rate where the floating rate is in itself a swap rate with a certain maturity, usually higher than the time interval until the next payment. The market practice concerning schedule bias is to distinguish between LIBOR rates related convexity adjustments and swap rate convexity adjustments. We follow market practice and present them separately.

LIBOR Convexity Adjustments. The forward LIBOR rate  $L(t, T_{i-1}, T_i)$  can be expressed in terms of discount bond prices as

$$L(t, T_{i-1}, T_i) = \frac{1}{\alpha_i} \frac{p(t, T_{i-1}) - p(t, T_i)}{p(t, T_i)} \tag{7}$$

where  $\alpha_i = T_i - T_{i-1}$ . Spot LIBOR rates can be defined in terms of the forward ones as  $L(t, T) =$  $L(t, t, T)$ . From the above expression, one can easily see the forward LIBOR rate  $L(t, T_{i-1}, T_i)$  is a martingale under the forward martingale measure  $\mathbb{Q}^{T_i}$ . Thus, we can price future LIBOR-dependent payments due at  $T_i$ , using equation (1) and forward LIBOR rates quoted today as we have  $\mathbb{E}^{T_i}_t[L(T_{i-1},$  $[T_i] = \mathbb{E}_t^{T_i} [L(T_{i-1}, T_{i-1}, T_i)] = L(t, T_{i-1}, T_i).$  This is the case in standard swap contracts, for instance.

However, in LIBOR-in-arrears (LIA) contracts, the LIBOR payment is due in advance, at time  $T_{i-1}$ . This leads to defining the LIA convexity correction as

$$\mathbb{E}_{t}^{T_{i-1}}\left[L(T_{i-1},T_{i})\right] = L(t,T_{i-1},T_{i}) + CC^{\text{LIA}}(t)$$
(8)

In this particular case, the measure change that we are interested in occurs between two forward measures and we have

$$\mathbb{E}_{t}^{T_{i-1}}\left[L(T_{i-1},T_{i})\right]$$
  
= 
$$\mathbb{E}_{t}^{T_{i}}\left[L(T_{i-1},T_{i})\frac{1+\alpha_{i}L(T_{i-1},T_{i})}{1+\alpha_{i}L(t,T_{i-1},T_{i})}\right] \tag{9}$$

which implies

$$CC^{\text{LIA}}(t)$$

$$= \alpha_{i} \frac{\mathbb{E}^{T_{i}} \left[ (L(T_{i-1}, T_{i}))^{2} \right] - \left[ L(t, T_{i-1}, T_{i}) \right]^{2}}{1 + \alpha_{i} L(t, T_{i-1}, T_{i})}$$

$$= \frac{\alpha_{i} \text{Var}_{t} \left[ L(T_{i-1}, T_{i}) \right]}{1 + \alpha_{i} L(t, T_{i-1}, T_{i})} \tag{10}$$

This is valid irrespective of the distribution that we assume for the forward LIBOR rates. Moreover, it only depends on its variance, which is the same under any equivalent martingale measure. Reference [15] provides exact LIA convexity adjustments based upon the assumption of lognormal LIBOR rates as in LIBOR market models (see LIBOR Market **Model**). In that particular case, we get  $CC^{LIA}(t) =$  $\alpha_i \left( L(t, T_{i-1}, T_i) \right)^2 e^{\sigma^2 (T_{i-1} - t)} / \left( 1 + \alpha_i L(t, T_{i-1}, T_i) \right),$ where  $\sigma$  represents the LIBOR volatility taken as constant. More generally, it is also possible to find exact LIA convexity adjustments in the context of affine term structure models.

Swap Convexity Adjustments. Since interest rate swaps make up a big proportion of the over-thecounter (OTC) derivatives market, convexity corrections needed for CMS are of particular interest and deserve separate attention. CMS payoffs and related products are discussed in detail in CMS spread products.

We start by recalling that the forward swap rate  $S(t, T_n, T_N)$  quoted at time t, with start date  $T_n$  and maturity  $T_N$  is model-free and equal to

$$S(t, T_n, T_N) = \frac{p(t, T_n) - p(t, T_N)}{P(t, T_n, T_N)}$$
(11)

where  $P(t, T_n, T_N) = \sum_{i=n}^{N} \alpha_i p(t, T_i)$  for  $\alpha_i$  as before, is a portfolio of bonds, sometimes known as *swap level*. It is well known that swap rates are martingales under the so-called swap martingale measure, here denoted by  $Q^S$ , and whose *numeraire* is the swap level.

A CMS exchanges a swap rate with a certain maturity  $c$  against a fixed payment  $K$ . The difficulty lies in computing the value of each payment of the floating leg. By no arbitrage, the value at time  $t$  of the payment due at  $T_i$  is given by  $\alpha_i p(t, T_i) \mathbb{E}_t^{T_i} \left[ S(T_{i-1}, T_i, T_{i+c}) \right]$  where, as before,  $\mathbb{E}_{t}^{T_{i}}[\cdot]$  denotes conditional expectation under the  $T_{i}$ forward measure. As  $S(T_{i-1}, T_i, T_{i+c})$  is not a martingale under forward measures, we need a convexity adjustment to take care of this. The convexity adjustment for each payment of a CMS can be defined as

$$\mathbb{E}_{t}^{T_{i}}\left[S(T_{i-1}, T_{i}, T_{i+c})\right] = S(t, T_{i}, T_{i+c}) + CC^{\text{CMS}}(t)$$
(12)

and it relies on measure changes from the  $T_i$ -forward measure to  $Q^{\mathcal{S}}$ . Concretely we get,

$$CC_{t}^{\text{CMS}} = \frac{P(t, T_{i}, T_{i+c})}{p(t, T_{i})} \times \mathbb{E}_{t}^{\mathcal{S}} \left[ S(T_{i-1}, T_{i}, T_{i+c}) \frac{p(T_{i-1}, T_{i})}{P(T_{i-1}, T_{i}, T_{i+c})} \right] - S(t, T_{i}, T_{i+c}) \tag{13}$$

This is not easy to obtain in closed form. Most CMS convexity adjustment formulas can only be obtained in an approximative way. A common practice at this stage is to see  $p(t, T_i)/P(t, T_i, T_{i+c})$  as a function G of the swap rate  $S(t, T_i, T_{i+c})$ .

In the case of the linear swap model (LSM) introduced in [10],  $G$  is linear and we have  $p(t, T_i)/P(t, T_i, T_{i+c}) = G(S(t, T_i, T_{i+c})) = A +$  $B(T_i)S(t, T_i, T_{i+c})$  for  $A = (\sum_i \alpha_i)^{-1}$  a constant and  $B(T_i) = \left[ p(t, T_i) / P(t, T_i, T_{i+c}) - A \right] / S(t, T_i, T_{i+c})$ only dependent on  $T_i$ . This linearity assumption is a crude one, but it yields better results in practice than one would expect. The reason for this is that convexity adjustments only become sizable for long maturities, and, for those maturities the term structure movements tend to be parallel. Thus, they are well captured by a linear model.

Alternatively, we can consider a generic (truly convex) function  $G$ , expand it around today's swap rate  $S(t, T_i, T_{i+c})$  using a Taylor expansion to then take expectations. Reference  $[7]$  is a popular paper on convexity adjustments of CMS swaps, caps, and floors that follows this line. The author analyzes three basic term structure models, starting from a standard yield curve model and continuing to more sophisticated models, which account for nonparallel shifts and continuous time compounding of interest rates. This is equivalent to assuming particular functional forms for the  $G$  function. Given a functional for  $G$ , the author then uses a first-order Taylor approximation and a lognormal distribution for the swap rates to approximations for the convexity adjustments of  $CMS$ 

$$CC_{t}^{\text{CMS}} \approx S(t, T_{i}, T_{i+c}) \frac{G'(S(t, T_{i}, T_{i+c}))}{G(S(t, T_{i}, T_{i+c}))} \times \left[ S(t, T_{i}, T_{i+c}) e^{\sigma^{2}(T_{i-1}-t)} - 1 \right] \quad (14)$$

where  $\sigma$  can be taken to be [2] implied volatility from at-the-money vanilla swaptions market quotes. For convexity adjustments of CMS caps and floors, we refer to the paper itself. For more information on popular formulation of swap rate dynamics, see **Swap Market Models.** 

The method proposed in  $[7]$  includes the LSM as a special case, in which the first-order Taylor approximation is, in fact, exact. Depending on the underlying dynamics for the swap rate, the formulas may be quite evolved, but the paper [16] provides hope for nice formulas in the affine term structure setup.

#### Quanto Adjustments

So far, we have discussed timing adjustments. Quanto products refer to products with an underlying expressed in one currency and payment in a different currency. Quanto adjustments are adjustments that try to correct for payment in the "wrong currency" versus the "wrong timing". We can have quanto (diff) swaps, swaptions, caps, floors, CMS rates, barrier options, equity swaps, and so on. For an overview of existing quanto products, see Quanto Options.

As explained in [14], a convexity adjustment of this type occurs when our product is a martingale under the foreign risk-neutral measure, but needs to be priced under the domestic risk-neutral measure. As an example, we shall use a diffed LIBOR contract, that is, a contract where the foreign LIBOR rate  $L^f(T_{i-1},T_i)$  is observed at  $T_{i-1}$  and is paid in domestic currency at time  $T_i$ . This contract can serve as the floating payment for a differential swap (also known as *diff swap* or *quanto swap*), and it is made against a fixed payment in domestic currency. We know that the forward LIBOR rate  $L^{f}(t, T_{i-1}, T_{i})$  is a martingale under the foreign  $T_i$  forward measure  $Q^{f,T_i}$ , so  $L^f(t,T_{i-1},T_i) = \mathbb{E}_t^{f,T_i}[L^f(T_{i-1},T_i)],$  but we need to compute the expectation of the foreign LIBOR rate under the domestic forward measure. Under that measure we know

$$\mathbb{E}_{t}^{d,T_{i}}[L^{f}(T_{i-1},T_{i})] = L^{f}(t,T_{i-1},T_{i}) + CC^{\text{diff}}(t)$$
(15)

and this type of convexity adjustment is given by

$$CC^{\text{diff}}(t) = \frac{\mathbb{E}_{t}^{f, T_{i}}[L^{f}(T, T_{i})F(T_{i-1}, T_{i})]}{F(t, T_{i})} - L^{f}(t, T_{i-1}, T_{i}) \tag{16}$$

where  $F(t, T_i)$  is the forward exchange rate  $(f/d)$ , quoted at t and with delivery at  $T_i$ . The convexity correction for quanto products will typically depend on the correlation between the foreign interest rate and the exchange rate. If, in the above example, both the forward LIBOR and the forward exchange rates have lognormal distributions under  $Q^{f,T_i}$  as proposed in [11], one can easily derive the convexity adjustment formula as  $CC^{\text{diff}}(t) =$  $L^f(t,T_{i-1},T_i)$   $\left[e^{\rho_{F,L}\sigma_L\sigma_F(T_{i-1}-t)}-1\right]$ , where  $\rho_{F,L}$  is the instant correlation between the LIBOR and the forward exchange rate,  $\sigma_L$  is the volatility of the LIBOR, and  $\sigma_F$  is the volatility of the forward exchange rate, assumed to be constant.

### References

- Björk, T. (2004). Arbitrage Theory in Continuous Time, [1] 2nd Edition, Oxford University Press.
- Black, F. (1976). The pricing of commodity contracts, [2] Journal of Financial Economics 3(2), 167-179.
- [3] Brigo, D. & Mercurio, F. (2006). Interest Rate Models: Theory and Practice, 2nd Edition, Springer Finance, Heidelberg.
- [4] Brotherton-Ractcliffe, R. & Iben, B. (1993). Yield curve applications of swap products, in Advanced Strategies in Financial Risk Management, R. Schwartz & C. Smith, eds, New York Institute of Finance, New York, рр. 400-450.
- Gaspar, R.M. (2006). Credit Risk and Forward Price [5] Models, EFI - The Economic Research Institute, Stockholm
- Geman, H., El-Karoui, N. & Rochet, J.-C. (1995). [6] Changes of numeraire, changes of probability measure and option pricing, Journal of Applied Probability 32,  $443 - 458$
- Hagan, P.S. (2003). Convexity conundrums: pricing [7] CMS swaps, caps, and floors, *Wilmott magazine* March,  $38 - 44$
- [8] Hart, Y. (1997). Unifying theory, *Risk* February, 54-55.
- Hull, J.C. (2006). Options, Futures, and other Derivative [9] Securities, Prentice Hall International, Inc. 6.
- [10] Hunt, P. & Kennedy, J. (2000). Financial Derivatives in Theory and Practice, 6th Edition, John Wiley & Sons, Chichester.
- $[11]$ Hunt, P. & Pelsser, A. (1998). Arbitrage free pricing of quanto-swaptions, Journal of Financial Engineering  $7(1), 25-33.$
- Park, H.Y. & Chen, A.H. (1985). Differences between [12] futures and forward prices: a further investigation of marking to market effects, Journal of Future Markets 5. 77-88.
- [13] Pelsser, A. (2000). *Efficient Methods for Valuing Interest* Rate Derivatives, Springer Finance, Heidelberg.
- [14] Pelsser, A. (2003). Mathematical foundation of convexity correction, *Quantitative Finance* 3, 59-65.
- Pugachevsky, D. (2001). Forward CMS rate adjustment, [15] Risk March, 125-128.
- Schrager, D. & Pelsser, A. (2006). Pricing swaptions [16] and coupon bond options in affine term structure models, Mathematical Finance  $16(4)$ , 673–694.

### **Further Reading**

References [13] and [3] are two important textbook references for fixed income products. Both books present good reviews of the nonstandard products that lead to convexity adjustments, including all products discussed here as well as more exotic ones.

## **Related Articles**

**Affine Models**; **Bond**; **Caps and Floors**; **CMS Spread Products**; **Constant Maturity Swap**; **Eurodollar Futures and Options**; **Forward and Swap Measures**; **LIBOR Market Model**; **LIBOR Rate**; **Swap Market Models**; **Yield Curve Construction**.

RAQUEL M. GASPAR & AGATHA MURGOCI
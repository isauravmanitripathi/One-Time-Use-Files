# **Constant Maturity Swap**

In-arrears swaps, averaging swaps, and constant maturity swaps (CMS) are simple extensions of vanilla interest rate swaps. Unlike vanilla swaps, these securities are sensitive to volatility via socalled convexity adjustments (see Convexity Adjust**ments**). We demonstrate two methods for calculating convexity adjustments: the standard Black-Scholes framework and the replication method.

Market uncertainty is described via a filtered probability space  $(\Omega, \mathcal{F}, \mathcal{F}_t, Q)$  where  $\mathcal{F}_t$  is a filtration associated with a Q-Brownian motion  $W_t$ . Q is the so-called risk-neutral probability measure, under which money-market-discounted asset prices are martingales.  $\mathbb{E}_t[X] = \mathbb{E}[X|\mathcal{F}_t]$  is the conditional expectation under  $Q$  of the integrable random variable  $X$ .

#### Notations

We use the following notations within the article:

- $r_t$  is the short rate at time  $t$ .
- $\beta_{t,T} = \exp(\int_t^T r_s \mathrm{d}s)$  is the continuously rolled money-market account between  $t$  and  $T$ . Note that  $\beta_{t,T} = \frac{\beta_{0,T}}{\beta_{0,t}}$  and that  $\beta_{t,T}$  is  $\mathcal{F}_T$ -measurable.<br> $P(t, T)$  is the value at *t* of 1\$ paid at *T*. We have

$$P(t,T) = \mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T}} \right] = \mathbb{E}_{t} \left[ e^{-\int_{t}^{T} r_{s} ds} \right] \quad (1)$$

- $G(w, f, N) = \sum_{i=1}^{f \cdot N} \frac{\delta(f)}{(1 + \delta(f)w)^i}$  is the cash level of the swap, or an approximation to the present value of a basis-point, or PV01, of a swap with different payment frequencies  $f \in \{1, 2, 4\}$  and different maturities  $N \in \mathbb{N}$ . Note that  $\delta(f) \approx \frac{1}{f}$  is the day-count fraction associated with a given day-count basis such as "Act360", "30-360", and so on. Going forward, we assume the frequency to be annual (i.e.,  $f = 1$ ), and T to be fixed and equal to N; then we simply write  $G(w, 1, N) = G(w)$ .
- $L(t, T_1, T_2)$  is the value at t of the forward LIBOR . rate, paid at  $T_2$ , and determined at the settlement date  $T_1$ , as described in **LIBOR Rate**.
- $\bullet$  $L^{f}(t, T_1, T_2)$  is the futures rate with settlement date  $T_1$ . Because of margin calls, the value

 $L^{f}(t, T_{1}, T_{2})$  differs from  $L(t, T_{1}, T_{2})$ , as detailed in **Eurodollar Futures and Options**.

.  $Q^T$  denotes the T-forward probability measure (see Forward and Swap Measures). It is the risk-neutral probability measure associated with the numeraire  $P(t, T)$  (see **LIBOR Rate**). For any  $\mathcal{F}_T$ -measurable random variable X, the change of measures is given by

$$\mathbb{E}_{t}\left[\frac{\beta_{0,t}}{\beta_{0,T}}X\right] = P(t,T)\mathbb{E}_{t}^{T}[X] \tag{2}$$

where  $\mathbb{E}_{t}^{T}$  (.) is the conditional expectation under  $Q^T$ .

- The O-Brownian motion,  $W_t$ , changes into  $W_t^T$ . under  $Q^T$  via the Girsanov theorem.
- $P^{f}(t, \widetilde{T}, T') = \frac{P(t, T')}{P(t, T)}$  is the forward zerocoupon, that is, the *t*-value of 1 $\$  paid at  $T'$  but borrowed at time  $T < T'$ . Note that  $P^f(t, T, T')$ is a  $Q^T$ -martingale as  $P(t,T)$  is a traded asset. More details on forward measures can be found in Forward and Swap Measures or in [5].
- $w_{t,T}$  is the forward swap rate of an N-year LIBOR swap paying annual coupons at dates  $T_1, \ldots, T_N$  (see LIBOR Rate for the definition of a LIBOR swap). We define  $T_0$  to be the fixing date  $T$ . We have

$$w_{t,T} = \frac{P(t,T) - P(t,T_N)}{\sum_{i=1}^{N} \theta_i P(t,T_i)} = \frac{1 - P^f(t,T,T_N)}{\sum_{i=1}^{N} \theta_i P^f(t,T,T_i)}$$
(3)

The quantity  $\theta_i$  is the day-count fraction for period  $[T_{i-1}, T_i], i = 1, \ldots, N.$ 

- $A(t) = \sum_{i=1}^{N} \theta_i P(t, T_i)$  is the spot annuity paying
- $\theta_i$  at times  $T_1, \ldots, T_N$ .<br>
    $A^f(t,T) = \sum_{i=1}^N \theta_i \frac{P(t,T_i)}{P(t,T)}$  is the forward annuity paying  $\theta_i$  at time  $T_1, \ldots, T_N$  forward in time, as of T. Note that  $A^f(T,T) = A(T)$ .
- The probability measure  $Q^{A_T}$  (see Forward and  $\bullet$ Swap Measures) associated with the numeraire  $A(.)$  is defined *via* the following measure change. For any  $\mathcal{F}_T$ -measurable random variable X,

$$\mathbb{E}_{t}\left[\frac{\beta_{0,t}}{\beta_{0,T}}A(T)X\right] = A(t)\mathbb{E}_{t}^{A_{T}}[X] \qquad (4)$$

 $Q^{A_T}$  is usually called the *annuity*, or *swap*, measure. Note that for  $N = 1$ ,  $O^{A_{T_1}}$  coincides with  $O^{T_1}$ .

- The Q-Brownian motion,  $W_t$ , changes into  $W_t^{A_T}$ under  $Q^{A_T}$  via the Girsanov theorem.
- A swaption is an option to enter into a swap at a future date  $T$ . We define  $K$  as the fixed rate in the swap. The price at  $t < T$  of a cashsettled swaption is given by  $CSS_{t,T}(K, \zeta) =$  $\mathbb{E}_{t} \left[ \beta_{t,T}^{-1} G \left( w_{T,T} \right) \left( \zeta \cdot w_{T,T} - \zeta \cdot K \right)_{+} \right] \text{ with } \zeta = 1$ <br>for a payer swaption and  $\zeta = -1$  for a receiver swaption.
- In this section, we define the payout of a CMS caplet referencing the swap rate  $w_{T}$  with strike K as  $(w_{T,T}-K)_+$ , and paying at the fixing date T. So its price is  $CMScaplet_{t,T}(K) =$  $\mathbb{E}_{t}[\beta_{t,T}^{-1}(w_{T,T}-K)_{+}]$ . We define the CMS floorlet as  $CMSfloor_{t,T}(K) = \mathbb{E}_{t}[\beta_{t,T}^{-1}(K - w_{T,T})_{+}].$ For a definition of standard caps and floors, see Caps and Floors: a standard (LIBOR) caplet with maturity  $T_{i+1}$  is given by  $Caplet_{t,T_{i+1}}(K) =$  $\mathbb{E}_{t}[\beta_{t,T_{i+1}}^{-1}(L(T_{i},T_{i},T_{i+1})-K)_{+}].$ <br>In CMS and LIBOR swaps, we distinguish two
- different types of payments: the nonstandard case (in-arrears), where the floating cash flow fixes on the same date as it pays, that is,  $T$ , and the standard case, (in advance), where the fixing takes place, say, 3 or 6 months before the payment.

#### **Constant Maturity Swaps**

Constant maturity swaps, constant maturity treasuries (CMT), and modified schedule LIBOR swaps are extensions of the standard fixed-for-floating swaps. Unlike the standard vanilla interest rate swaps (see LIBOR Rate) that specify an exchange of a fixed coupon for a LIBOR rate, CMS instruments pay the swap rate that is reset at each period versus either a fixed coupon or a LIBOR rate plus a spread. For CMT swaps, the structure is identical, but instead of the swap rate, the yield of a government bond is referenced. These swaps are often suggested as a way to benefit from a steepening or a flattening of the yield curve, while still being hedged against its parallel moves. To illustrate, let us consider the following CMS instrument: one pays 3-month LIBOR rate and receives the 10-year swap rate, denoted by  $CMS_{10Y}(t)$ , that is reset (observed) every 6 months. If, during the life of the swap (for instance 10 years)

the curve steepens, so that  $CMS_{10Y}(t)$  increases as time  $t$  goes by relative to the LIBOR rate, the holder realizes a positive carry, that is, the amount of received cash flows exceeds the amount of paid cash flows. Given that LIBOR and CMS rates are reset at each period, a sudden parallel shift of the curve has no effect on the present value of the swap because of the mutual offset of both legs. As instruments that express views on the nonparallel moves of the yield curve, both CMS and CMT instruments are very popular and generally very liquid, and also often serve as building blocks for more complicated derivatives such as options on CMS rates or CMS spreads (differences between CMS rates of different tenors). Given their widespread use, accurate pricing of the underlying CMS cash flows is important. We describe the nonstandard CMS first, as the standard CMS is the nonstandard CMS adjusted for a payment lag.

There are two main methods for valuing CMS instruments: a standard Black-Scholes approach and a replication method. The first, a more traditional approach, assumes the swap rate to be log-normal, allowing the standard Black-Scholes framework to be used (see Black-Scholes Formula for this model). The key benefit of this approach is that it leads a to closed-form formula for the value of a CMS cash flow, also allowing options on CMS rates and other derivatives to be priced with the Black-Scholes formula.

We will show that the value of the CMS rate cash flow differs from the forward swap rate as it depends on volatility. This difference, called *convexity adjustment*, is often explained by the fact that in a CMS cash flow, the rate is paid once, rather than on its "natural" schedule. More details about convexity can be found in [4], [6], and [9].

Before describing these pricing methods in some detail, we introduce some notations. We know that in a CMS cash flow, the swap rate is paid once, at  $T$ , so the CMS value at  $t < T$  is simply given by

$$P(t,T) \cdot CMS_t = \mathbb{E}_t[\beta_{t,T}^{-1}w_{T,T}]$$
  
=  $P(t,T)\mathbb{E}_t^T[w_{T,T}]$  (5)

so that

$$CMS_t = \mathbb{E}_t^T[w_{T,T}] \tag{6}$$

Note that  $w_{.,T}$  is not a  $Q^T$ -martingale, so  $\mathbb{E}_{t}^{T}[w_{T,T}] \neq w_{t,T}$ . The difference between  $CMS_{t}$  and the forward swap rate  $w_{t,T}$  is the convexity adjustment. Let us write the formula under the annuity measure  $Q^{A_T}$ , the probability measure under which  $w_{..T}$  is a martingale. Using equation (4), we get

$$CMS_{t} = \frac{A(t)}{P(t,T)} \mathbb{E}_{t}^{A_{T}} \left[ \frac{w_{T,T}}{A(T)} \right] \tag{7}$$

We see that  $CMS_t$  is a function of both the curve level via  $\frac{A(t)}{P(t,T)}$  and the covariance between  $A(T)$ and  $w_{T,T}$ . This strongly hints that the convexity adjustment is a function of the volatility of the forward swap rate  $w_{T,T}$ .

### CMS Convexity Adjustment: the Simple Approach

The aim of this approach is to find a simple, closedform approximation, assuming that the forward swap rate is log-normal: it is consequently often referred as the *Black* convexity adjustment. As  $w_{T}$  is a  $Q^{A_T}$ martingale, we have  $\frac{\mathrm{d}w_{u,T}}{w_{u,T}} = \sigma \mathrm{d}W_u^{A_T}$  at any time *u* between  $t$  and  $T$ . We assume that the variance of the swap rate under its swap measure is equal to its variance under the  $T$ -forward measure, that is,  $\mathbb{E}_{t}^{T}[w_{T,T}-w_{t,T}]^{2}=\sigma^{2}(T-t)w_{t,T}^{2}$  (more precisely, we assume the convexity adjustment to be an adjustment of second order). We further assume that at any time *u* between *t* and *T*,  $A^f(u,T) \approx G(w_{u,T})$ , so that we approximate  $w_{u,T}$  with the par yield of the forward starting bond—a common assumption used by market participants to, for example, compute the swap PV01. Since  $A^f(., T)$  is a  $Q^T$ -martingale, so it is approximately  $G(w_{T})$ . Performing a Taylor expansion to second order of  $G(w_{T,T})$  around  $w_{t,T}$ , we obtain

$$G(w_{T,T}) = G(w_{t,T}) + (w_{T,T} - w_{t,T})G'(w_{t,T})$$
  
+ 
$$\frac{1}{2}(w_{T,T} - w_{t,T})^2 G^{''}(w_{t,T})$$
  
+ 
$$o(w_{T,T} - w_{t,T,(T_i)})^2$$
 (8)

Given also that  $\mathbb{E}_{t}^{T}[G(w_{T,T})] = G(w_{t,T}),$  we apply the expected value operator  $\mathbb{E}^T_t$  to both sides of  $(8)$  to give us

$$CMS_t = w_{t,T} \left( 1 - \frac{1}{2} w_{t,T} \cdot \sigma^2 \cdot (T - t) \cdot \frac{G''(w_{t,T})}{G'(w_{t,T})} \right)$$

$$\simeq w_{t,T} \exp\left(-\frac{1}{2}w_{t,T} \cdot \sigma^2 \cdot (T-t) \cdot \frac{G''(w_{t,T})}{G'(w_{t,T})}\right)$$
(9)

From the above formula, we see that the convexity adjustment  $\exp\left(-\frac{1}{2}w_{t,T}\cdot\sigma^2\cdot(T-t)\cdot\frac{G''(w_{t,T})}{G'(w_{t,T})}\right)$ <br>-1 is positive given that G is decreasing, convex  $(G' < 0 \text{ and } G'' > 0)$ , and increases with the implied volatility  $\sigma$ .

#### CMS Convexity Adjustment: the Replication Approach

The simple approach does not capture the fact that the implied volatilities exhibit volatility smile. The replication method we develop in this section captures the smile effect, as noted by Amblard et al. [1].

The simple adjustment has a further drawback that it does not provide a way to construct a hedge for a CMS cash flow. Indeed, to hedge the CMS using the Black-Scholes adjustment, one can compute the delta and vega, but this is not a static hedge. The replication approach rectifies this issue as well.

The replication approach has the disadvantage of being nonparametric, but on the other hand, it takes into account the volatility smile and exhibits an explicit static hedge for the CMS rate cash flows and options in terms of payer and receiver swaptions. The computation is done in two steps. First we compute a CMS caplet and a CMS floorlet at a given strike  $k$  (see Notations for a definition of CMS caplets and floorlets; see also Caps and Floors for a definition of caps and floors). The CMS rate is then obtained *via* the call $-$ put parity.

We use a numerical integration, commonly used to replicate European options with complex payoffs using vanilla European options (see [3]). Indeed, for any real  $C_2$ -function V of the swap rate w and any real number  $x$ , we have

$$V(w) = V(x) + (w - x) \cdot V'(x)$$
  
+  $1_{\{w > x\}} \int_{x}^{w} V''(K)(w - K)_{+} dK$   
+  $1_{\{w < x\}} \int_{w}^{x} V''(K)(K - w)_{+} dK$   
(10)

Observing that the boundaries for the integrals can be extended to  $+\infty$  and  $-\infty$ , respectively, we have

$$V(w) = V(x) + (w - x) \cdot V'(x)$$
  
+  $1_{\{w > x\}} \int_{x}^{+\infty} V''(K)(w - K)_{+} dK$   
+  $1_{\{w < x\}} \int_{-\infty}^{x} V''(K)(K - w)_{+} dK$  (11)

so by setting  $x = 0$ 

$$V(w) = V(0) + wV'(0)$$
  
+  $1_{\{w>0\}} \int_{0}^{+\infty} V''(K)(w-K)_{+} dK$   
+  $1_{\{w<0\}} \int_{-\infty}^{0} V''(K)(K-w)_{+} dK$  (12)

Let  $k > 0$  be the strike of CMS caplet or CMS floorlet.

To compute the CMS caplet, let us define  $V(w) =$  $\frac{(w-k)_{+}}{G(w)}$ . Then as  $V(0) = V'(0) = 0$ :

$$(w-k)_{+} = 1_{\{w>0\}} \int_{0}^{+\infty} V''(K)G(w)(w-K)_{+} \, \mathrm{d}K$$
$$+ 1_{\{w<0\}} \int_{-\infty}^{0} V''(K)G(w)(K-w)_{+} \, \mathrm{d}K \tag{13}$$

Equation (13) expresses the general decomposition of a call payoff  $(w-k)_+$  on a continuous set of payoffs  $(G(w)(w-K)_{+})_{K\geq 0}$  and  $(G(w)$  $(K-w)_{+}$ ) $_{K<0}$ .

By replacing  $w$  with  $w_{T,T}$ , multiplying both sides by  $\beta_{t,T}^{-1}$  , taking the  $\mathcal{F}_t$ -conditional expectation under the risk-neutral measure, and using the definition of a CMS caplet in the section Notations, we obtain

$$CMScaplet_{t,T}(k)$$
  
=  $\int_{0}^{+\infty} V''(K) \mathbb{E}_{t} [\beta_{t,T}^{-1} G(w_{T,T})(w_{T,T} - K)_{+}] dK$   
+  $\int_{-\infty}^{0} V''(K) \mathbb{E}_{t} [\beta_{t,T}^{-1} G(w_{T,T})(K - w_{T,T})_{+}] dK$  (14)

On the right-hand side, we recognize the prices of cash-settled swaptions as described in the section Notations. Note that  $G(w_{T,T})$  is an approximation for  $A(T)$  in the cash-settled swaption formula. So we have

$$CMScaplet_{t,T}(k)$$
  
=  $\int_{0}^{+\infty} V''(K)CSS_{t,T}(K, \zeta = 1) dK$   
+  $\int_{-\infty}^{0} V''(K)CSS_{t,T}(K, \zeta = -1) dK$  (15)

If we assume  $k > 0$ , the second integral vanishes as  $V''(K) = 0$  if  $K < k$ . To be tractable, this decomposition must be discretized and the integrals ultimately truncated:

$$CMScaplet_{t,T}(K) \approx \sum_{i=0}^{N_{\text{cap}}} \alpha_i^{\text{cap}} CSS_{t,T}(K_i, x=1)$$
(16)

We start from  $K_0 = k + \varepsilon$ , with  $\varepsilon$  very small to avoid the discontinuity at  $K = k$ , and set  $K_i =$  $K_0 + i \Delta K$ . The strike step  $\Delta K$  is also arbitrary. We have  $\alpha_i^{\text{cap}} = 2h'(K_i) + (K_i - k)h''(K_i)$  with  $h(x) =$  $\frac{1}{G(x)}$ . In practice, the choice of  $N_{\text{cap}}$  or, equivalently, the last payer swaption strike used for replication can be computed dynamically: we add in that case an extra strike until we reach  $\alpha_i^{\text{cap}}CSS_{t,T}(K_i, x=1) <$ Chosen Precision. Depending on the assumption chosen for the smile extrapolation far out of the money, this can lead to some divergence of the replication algorithm. In that case, we can use an arbitrary cap, for example  $K_{\text{max}}^{\text{cap}} = 50\%$ .

The CMS floorlet is computed in a similar way, replacing  $V(w)$  by  $\frac{(k-w)_+}{G(w)}$ . Note that we have  $V(0) \neq 0$  and  $V'(0) \neq 0$ , so we have two extra terms:

$$\begin{split} &\quad \mathcal{C}MSfloorlet_{t,T}(k) \\ &= V(0)\mathbb{E}_{t}[\beta_{t,T}^{-1}G(w_{T,T})] \\ &+ V'(0)\mathbb{E}_{t}[\beta_{t,T}^{-1}w_{T,T}G(w_{T,T})] \\ &+ \int_{0}^{+\infty} V''(K)\mathbb{E}_{t}[\beta_{t,T}^{-1}G(w_{T,T})(w_{T,T}-K)_{+}] \, \mathrm{d}K \\ &+ \int_{-\infty}^{0} V''(K)\mathbb{E}_{t}[\beta_{t,T}^{-1}G(w_{T,T}) \\ &\times (K - w_{T,T})_{+}] \, \mathrm{d}K \end{split} \tag{17}$$

If we assume that rates cannot be negative, the second integral vanishes. In the current environment, it is not clear that rates cannot go slightly negative, so we should also compute the second part, which has value if we use, for example, a Gaussian model. Assuming  $G(w_{T,T})$  as an approximation for  $A(T)$ we have  $\mathbb{E}_{t}[\beta_{t,T}^{-1}G(w_{T,T})] \approx A(t)$  and using equation (4), we get  $\mathbb{E}_t[\beta_{t,T}^{-1}w_{T,T}G(w_{T,T})] \approx A(t)w_{t,T}$ . We start the first integration from  $K_0^{\alpha} = k - \varepsilon$ <br>and set  $K_i^{\alpha} = K_0^{\alpha} - i\Delta K$ , with  $\alpha_i^{\text{floor}} = -2h'(K_i^{\alpha}) +$  $(k - K_i^{\alpha})h^{''}(K_i^{\alpha})$  until we reach  $K_{N_i}^{\alpha} = 0$ . Concerning the receiver swaption, we start from  $K_0^{\beta} = 0$ <br>and set  $K_j^{\beta} = K_0^{\beta} - j\Delta K$  with  $\beta_j^{\text{floor}} = -2h'(K_j^{\beta}) +$  $(k - K_i^{\beta})h^{''}(K_i^{\beta})$  until we reach an arbitrary lower bound for the receivers  $K_{N_2}^{\beta} = K_{\min}(<0)$ . Then we have

$$\begin{split} CMSfloorlet_{t,T}(K) \\ \approx & \left(V(0) + V'(0)w_{t,T}\right)A(t) \\ &+ \Sigma_{i=0}^{N_1} \alpha_i^{\text{floor}} CSS_{t,T}(K_i^{\alpha}, \zeta = 1) \\ &+ \Sigma_{j=0}^{N_2} \beta_j^{\text{floor}} CSS_{t,T}(K_j^{\beta}, \zeta = -1) \end{split} \tag{18}$$

To compute the CMS rate, we see from expression (6) that if we assume interest rates to be positive as in the Black-Scholes case, we can value the CMS rate directly from a CMS caplet struck at  $k = 0$  as  $\mathbb{E}_t[(w_{T,T})_+] = \mathbb{E}_t[w_{T,T}]:$ 

$$CMS_{t} = \frac{1}{P(t,T)} CMScaplet_{t,T}(k=0) \qquad (19)$$

Alternatively, we use the call-put parity. Note that the choice of the strike  $k$  in the caplet and floorlet is arbitrary (a common practice is to set the strike to the forward swap rate  $k = w_{t,T}$ :

$$CMS_{t} = k + \frac{CMScaplet_{t,T}(k) - CMSfloorlet_{t,T}(k)}{P(t,T)}$$
(20)

Alternative pricing methods have been proposed in the literature such as higher order Taylor expansions or chaos expansions (see [2]) or linear swap rate model approximation (see  $[6-8]$ ).

#### Computation of the CMS rate in the standard case

In the standard case, fixing is at  $T$ , and payment takes place at  $T + \theta$ , so we have  $P(t, T + \theta) \cdot CMS_t^{\text{std}} =$  $\mathbb{E}_t\left[\frac{\beta_{0,t}}{\beta_{0,T+\theta}}w_{T,T}\right]$ . We see that we can no longer apply the change of probability as in equation  $(4)$ because of the presence of  $\beta_{0,T+\theta}$  instead of f  $\beta_{0,T}$ : we artificially introduce  $\beta_{0,T}$  in order to use equation  $(4)$ . We have

$$\mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T+\theta}} w_{T,T} \right] = \mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T}} \frac{\beta_{0,T}}{\beta_{0,T+\theta}} w_{T,T} \right]$$
$$= \mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T}} w_{T,T} B(T,T+\theta) \right]$$
$$= P(t,T) \mathbb{E}_{t}^{T} [w_{T,T} B(T,T+\theta)] \tag{21}$$

There are at least two methods for computing the above quantity.

The first method consists in replacing  $B(T, T +$  $\theta$ ) with a function involving  $w_{T,T}$  plus a spread s. For example, we could write  $B(T, T + \theta) =$  $\frac{1}{1+\theta(w_{T,T}+s)} \quad \text{so} \quad \text{that} \quad \mathbb{E}_t^T[w_{T,T}B(T,T+\theta)] =$  $\mathbb{E}_{t}^{T}[f(w_{T,T})] \text{ with } f(w) = \frac{w}{1 + \theta(w+s)}. \text{ We then}$ use the replication formula (12) by replacing  $V(w)$ with  $V(w) = \frac{f(w)}{G(w)}$ .<br>Alternatively, we can replace  $B(T, T + \theta)$  with

 $B(T, T + \theta) = \frac{1}{1 + \theta L(T, T, T + \theta)}$ . The approximation:

$$\frac{1}{1 + \theta L(T, T, T + \theta)} \approx 1 - \theta L(T, T, T + \theta) \tag{22}$$

together with a correlation assumption  $\rho = corr^{Q_T}$  $(L(T, T, T + \theta), w_{T,T})$  between the forward LIBOR and the forward swap rate under measure  $Q^T$  give us

$$\begin{split} \mathbb{E}_{t}^{T}[w_{T,T}B(T,T+\theta)] \\ \approx & \mathcal{C}MS_{t} - \theta \mathcal{C}MS_{t}\mathbb{E}_{t}^{T}[L(T,T,T+\theta)] \\ - & \theta \rho \sqrt{Var^{\mathcal{Q}^{T}}(w_{T,T})} \sqrt{Var^{\mathcal{Q}^{T}}(L(T,T,T+\theta))} \end{split} \tag{23}$$

where  $CMS_t$  is the nonstandard CMS rate computed previously and  $\mathbb{E}^T_t[L(T,T,T+\theta)]$  is a convexityadjusted forward LIBOR (see the next section for

more details). The variances under  $O^T$  of the forward swap and LIBOR rates can be both valued via replication or approximated with the variances under their "natural" measures, respectively,  $Q^A$ and  $Q^{T+\theta}$ . Under Black–Scholes assumptions, they are simply  $w_{t,T}^2(e^{(T-t)\sigma_w^2(T)}-1)$  and  $L(t,T,T+1)$  $(\theta)^2 (e^{(T-t)\sigma_L^2(T)} - 1)$ , respectively.

On the one hand, the second method involves more computations, themselves involving approximations, and uses an input  $\rho$  not explicitly given by the market. However, it better illustrates the "negative" convexity in the standard CMS case, that is, the presence of a negative second term in the formula.

### **In-arrears Swaps**

In this section, we deal with LIBOR swaps, the CMS case having been described previously. As defined in the section Notations, in-arrears swaps are interest rate swaps that differ from vanilla swaps by the absence of a payment lag in the floating leg. More precisely, in a vanilla swap, the floating rate  $L(T_{i-1}, T_{i-1}, T_i)$  fixes at  $T_{i-1}$  and is paid at  $T_i$ , that is, payment at  $T_i$  is  $\theta_i L(T_{i-1}, T_{i-1}, T_i)$  while in an in-arrears swap, the floating rate is fixed and paid the same date at the end of the period, that is, the payment at  $T_i$  is  $\theta_{i+1}L(T_i, T_i, T_{i+1})$ . As we will see, this change also creates a positive convexity adjustment in the valuation of the floating leg. The valuation of in-arrears swaps can be done by at least two different methods: the traditional Black-Scholes adjustment and the replication technique. For the replication method, the underlying replication instruments are caplets/floorlets as opposed to swaptions for the CMS cash flows described in the previous section.

The time *t*-value of the in-arrears payment at  $T_i$  is

$$\mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T_{i}}} \theta_{i+1} L(T_{i}, T_{i}, T_{i+1}) \right]$$
  
=  $\theta_{i+1} P(t, T_{i}) \mathbb{E}_{t}^{T_{i}} [L(T_{i}, T_{i}, T_{i+1})]$  (24)

As the forward LIBOR rate  $L(., T_i, T_{i+1})$  is a  $Q^{T_{i+1}}$ -martingale, we have

$$\mathbb{E}_{t}^{T_{i+1}}[L(T_{i}, T_{i}, T_{i+1})] = L(t, T_{i}, T_{i+1}) \tag{25}$$

but

$$\mathbb{E}_{t}^{T_{i}}[L(T_{i}, T_{i}, T_{i+1})] \neq L(t, T_{i}, T_{i+1}) \tag{26}$$

To use the martingale property of  $L(., T_i, T_{i+1})$ under  $Q^{T_{i+1}}$ , we discount  $\theta_{i+1}L(T_i,T_i,T_{i+1})$  from date  $T_{i+1}$ . Obviously, the cash flow must be capitalized between  $T_i$  to  $T_{i+1}$  to compensate for this "late" discounting:

$$\mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T_{i}}} \theta_{i+1} L(T_{i}, T_{i}, T_{i+1}) \right]$$

$$= \mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T_{i+1}}} \theta_{i+1} L(T_{i}, T_{i}, T_{i+1}) \frac{\beta_{0,T_{i+1}}}{\beta_{0,T_{i}}} \right]$$

$$= \mathbb{E}_{t} \left[ \frac{\beta_{0,t}}{\beta_{0,T_{i+1}}} \theta_{i+1} L(T_{i}, T_{i}, T_{i+1}) \times (1 + \theta_{i+1} L(T_{i}, T_{i}, T_{i+1})) \right]$$

$$= P(t, T_{i+1}) \theta_{i+1} L(t, T_{i}, T_{i+1}) + P(t, T_{i+1}) \theta_{i+1}^{2} \mathbb{E}_{t}^{T_{i+1}} [L^{2}(T_{i}, T_{i}, T_{i+1})]$$

$$(27)$$

Now we can compute  $\mathbb{E}_{t}^{T_{i+1}}[L^{2}(T_{i}, T_{i}, T_{i+1})]$  either using a standard Black-Scholes adjustment or via replication on caplets. In the first case, assuming that the at-the-money implied volatility of the forward rate  $L(., T_i, T_{i+1})$  is  $\sigma_i$ , we find  $\mathbb{E}_t^{T_{i+1}}[L^2(T_i, T_i, T_{i+1})]$  $= L(t, T_i, T_{i+1})^2 e^{\sigma_i^2(T_i - t)}$ . In the second case, we can use formula  $(12)$  to find that

$$x^{2} = 2 \int_{0}^{+\infty} (x - K)_{+} \, \mathrm{d}K \tag{28}$$

so that using the caplet definition given in the section Notations

$$\mathbb{E}_{t}^{T_{i+1}}[L^{2}(T_{i}, T_{i}, T_{i+1})]$$

$$= 2 \int_{0}^{+\infty} \mathbb{E}_{t}^{T_{i+1}}[(L(T_{i}, T_{i}, T_{i+1}) - K)_{+}] dK$$

$$= \frac{2}{P(t, T_{i+1})} \int_{0}^{+\infty} Caplet_{t, T_{i+1}}(K) dK \quad (29)$$

To be tractable, this integral must be discretized and capped as previously described in the CMS case.

# **Averaging Swaps**

As nonstandard fixed-for-floating interest rate swaps, averaging swaps are somewhat less common than CMS and in-arrears swaps. The floating leg of such a swap pays at each coupon date  $T_i$  the average of the LIBOR rates observed over a predetermined period. Let us consider a set of dates  $T_{i(k)}$  with  $i(k) < i$ . The cash flow at date  $T_i$  is given by

$$\frac{1}{N} \sum_{k=1}^{N} \theta_{i(k)+1} L(T_{i(k)}, T_{i(k)}, T_{i(k)+1}) \qquad (30)$$

So assuming that under the "terminal measure"  $Q_{T_i}$ , we know the drift  $\mu_{i(k)}$ ,

$$\frac{\mathrm{d}L(t,T_{i(k)},T_{i(k)+1})}{L(t,T_{i(k)},T_{i(k)+1})} = \mu_{i(k)}(t)\,\mathrm{d}t + \sigma_{i(k)}\mathrm{d}W_t^{T_i} \quad (31)$$

the averaging formula has a value at time  $t$  given by

$$\mathbb{E}_{t} \left[ \beta_{t,T_{i}}^{-1} \frac{1}{N} \sum_{k=1}^{N} \theta_{i(k)+1} L(T_{i(k)}, T_{i(k)}, T_{i(k)+1}) \right]$$
$$= P(t, T_{i}) \sum_{k=1}^{N} \theta_{i(k)+1} L(t, T_{i(k)}, T_{i(k)+1})$$
$$\times \exp \left( \int_{t}^{T_{i(k)}} \mu_{i(k)}(u) \, \mathrm{d}u \right) \tag{32}$$

The convexity adjustments  $\exp\left(\int_{t}^{T_{i}(k)} \mu_{i}(k)}(u) du\right)$ can either be computed by Black-Scholes formula, or by replication. Alternatively, a term structure model such as a LIBOR market model (see LIBOR Market Model) or a Chevette model (see Markovian Term Structure Models) could be used to obtain the required drifts. (See also Change of Numeraire; Forward and Swap Measures; Convexity Adjustments.)

### References

- [1] Amblard, G. & Lebuchoux, J. (2000). *The Relationship* Between CMS Options and the Smile, Risk Magazine.
- [2] Benhamou, E. (2000). Pricing Convexity Adjustment with Wiener Chaos. Working paper available from www.ssrn.com.

- [3] Carr. P., Lewis, K. & Mandan, D. (2000). On the *Nature of Options*. working paper 2000, available from http://www.math.nyu.edu/research/carrp/papers.
- [4] Coleman, T. (1995). Convexity Adjustments for CMS and Libor in Arrears Basis Swaps. Working paper.
- [5] El Karoui, N., Geman, H. & Rochet, J.C. (1995). Changes of numeraire, changes of probability measures and option pricing, Journal of Applied Probability 32, 443-458.
- [6] Hunt, J.P. & Kennedy, J.F. (2000). On Convexity Corrections. Working Paper, ABN-AMRO Bank and Warwick University.
- [7] Hunt, J.P. & Kennedy J.F. (2000). Financial Derivatives in Theory and Practice, Wiley, Chichester.
- [8] Pelsser, A. (2000). Efficient Methods for Valuing Interest Rate Derivatives, Springer Finance, Heidelberg.
- [9] Pugachewsky, D. (2001). Forward CMS rate adjustment, RISK March, 125-128.

## **Further Reading**

- Amin, K. & Jarrow, R. (1992). Pricing options on risky assets in a stochastic interest rate economy, *Mathematical Finance* 2, 217-237.
- Black, F & Scholes M. (1973). The pricing of options and corporate liabilities, Journal of Political Economy 8(1), 637-654.
- Flesaker, B. (1993). Arbitrage free pricing of interest rate futures and forward contracts, Journal of Futures Markets 13, 77-91.
- Hull, J. (2007). Options, Futures and other Derivatives, Prentice Hall India.
- Jamshidian, F. (1993). Option and Future evaluation with deterministic volatilities, Mathematical Finance 3, 149-159.
- Musiela, M & Rutkowski, M. (1998). Martingale Methods in Financial Modelling, Springer Verlag.

#### Related Articles

Black-Scholes Formula; Convexity Adjustments; Forward and Swap Measures; LIBOR Rate; Markovian Term Structure Models.

LAURENT VEILEX
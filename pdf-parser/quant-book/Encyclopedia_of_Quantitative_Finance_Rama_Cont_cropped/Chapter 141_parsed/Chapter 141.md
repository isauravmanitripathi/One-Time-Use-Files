# Implied Volatility in **Stochastic Volatility** Models

Given the geometric Brownian motion (hence constant volatility) dynamics of an underlying share price, the Black-Scholes formula finds the no-arbitrage prices of call or put options. Given, on the other hand, the price of a call or put, the Black-Scholes implied volatility is by definition the unique volatility parameter such that the Black-Scholes formula recovers the given option price.

If the share price truly follows geometric Brownian motion, then the Black-Scholes implied volatility matches the constant realized volatility of the shares. Empirically, however, stock prices do not exhibit constant volatility, which explains the description in [23] of implied volatility as "the wrong number to put in the wrong formula to obtain the right price". Nonetheless, the Black-Scholes implied volatility remains, at the very least, a language/scale/metric by which option prices may be quoted and compared across strikes, expiries, underliers, and observation times, as noted in  $[17]$ .

Moreover, even under stochastic volatility dynamics, Black-Scholes implied volatility is not only a language but indeed carries meaningful information about realized volatility. This article surveys those relationships between implied and realized stochastic volatility, in particular, the following:

- Expected realized variance equals the weighted average of implied variance across strikes, with "implied normal" weights.
- Implied volatility of an option is the breakeven realized volatility for "business-time delta hedging" of that option.
- Implied volatility at-the-money approximates expected realized volatility, under an independence condition.

Aside from Black–Scholes implied volatility, alternative notions of options-implied volatility have robust relationships to realized volatility. We define and discuss two notions of model-free implied volatility (MFIV):

- "VIX-style" MFIV equals the square root of expected variance.
- "Synthetic volatility swap (SVS) style" MFIV equals expected volatility under an independence condition, and approximates expected volatility under perturbations of that condition.

Unless otherwise noted, the only assumptions on the underlying price process are positivity and continuity.

Specifically, on a filtered probability space  $(\Omega, \mathcal{F},$  $\{\mathcal{F}_t\}, \mathbb{P}$ ), let S be a positive continuous martingale. Regard  $S$  as the share price of an underlying tradable asset, and  $\mathbb{P}$  as risk-neutral measure, with respect to a bond having price 1 at all times. Extensions to arbitrary deterministic interest rates are straightforward. Let  $\mathbb{E}_t$  denote  $\mathcal{F}_t$ -conditional expectation, with respect to  $\mathbb{P}$ . Let

$$X_t := \log(S_t/S_0) \tag{1}$$

denote the log returns process, and let  $\langle X \rangle_t$  denote its *quadratic variation* process, which may be regarded as the unannualized running total of the squared realized returns of S continuously monitored on  $[0, t]$ .

Fixing a time horizon  $T > 0$ , define *realized* variance to be

 $\langle X \rangle_T$ 

and define realized volatility to be the square root  $\sqrt{\langle X \rangle_T}$  of realized variance. For example, if S has dynamics

$$\mathrm{d}S_t = \sigma_t S_t \, \mathrm{d}W_t \tag{2}$$

with respect to Brownian motion W, then  $\langle X \rangle_T =$  $\int_0^T \sigma_t^2 dt$ .

#### **Black–Scholes Implied Volatility**

Fix a time horizon  $T > 0$ . Define the Black-Scholes [3] function, for S, K, and  $\sigma$  positive, by

$$C^{\text{bs}}(\sigma, S, K) := SN\left(\frac{\log(S/K)}{\sigma} + \frac{\sigma}{2}\right) - KN\left(\frac{\log(S/K)}{\sigma} - \frac{\sigma}{2}\right) \tag{3}$$

where N is the standard normal cdf. Define  $C^{bs}(0, S,$  $K) := (S - K)^{+}.$ 

For each  $K > 0$ , define the time-0 dimensionless Black-Scholes *implied volatility*  $IV_0(K)$  to be the unique solution of

$$C^{\text{bs}}(\text{IV}_0(K), S_0, K) = \mathbb{E}_0(S_T - K)^+ =: C(K)$$
 (4)

Dividing IV<sub>0</sub>(K) by  $\sqrt{T}$  produces the usual annualized implied volatility.

Often, it is more convenient to regard the Black-Scholes formula as a function of dimensionless variance instead of dimensionless volatility, so define

$$C^{\text{BS}}(V, S, K) := C^{\text{bs}}(\sqrt{V}, S, K) \tag{5}$$

Moreover, it may be convenient to regard the Black-Scholes implied volatility as a function of log strike instead of strike, so define

$$IV_0(k) := IV_0(S_0 e^k) \tag{6}$$

We survey how the realized volatility  $\sqrt{\langle X \rangle_T}$  (or realized variance  $\langle X \rangle_T$ ) relates to the time-0 implied volatility (or its square, the *implied variance*).

# Expected Realized Variance Equals Weighted Average Implied Variance Across Strikes

Black-Scholes implied variance at one strike does not determine the risk-neutral expectation of realized variance, but the weighted average of implied variance at all strikes does so. This result facilitates, for instance, analysis [14] of how the implied volatility skew's slope and convexity relate to expected variance.

The "implied normal" weights are given by the standard normal distribution, applied to the log strike standardized by "implied standard deviations". Specifically, assuming  $IV_0(k) > 0$ , define the standardized log strike by

$$z(k) := -d_2(k) := \frac{k}{IV_0(k)} + \frac{IV_0(k)}{2} \qquad (7)$$

The result

$$\mathbb{E}_0 \langle X \rangle_T = \int_{-\infty}^{\infty} I V_0^2(k) \, \mathrm{d}N(z(k)) \tag{8}$$

follows from relating each side to the value of a log contract.

Expected Realized Variance Equals Log Contract Value. Realized variance admits replication by holding a log contract and dynamically trading shares, via the strategy developed in [7, 10, 21], and [9]. Specifically,

$$dX_t = d \log S_t = \frac{1}{S_t} dS_t - \frac{1}{2S_t^2} d\langle S \rangle_t$$
$$= \frac{1}{S_t} dS_t - \frac{1}{2} d\langle X \rangle_t \qquad (9)$$

hence,

$$\langle X \rangle_T = -2\log(S_T/S_0) + \int_0^T \frac{2}{S_t} \, \mathrm{d}S_t \tag{10}$$

Therefore, the log contract payoff  $-2\log(S_T/S_0)$ , plus the profit/loss from a dynamic position long  $2/S_t$ shares, replicates  $\langle X \rangle_T$ . A corollary is that

$$\mathbb{E}_0 \langle X \rangle_T = \mathbb{E}_0(-2X_T) \tag{11}$$

if they are finite.

Log Contract Value Equals Weighted Average Implied Variance. In turn, the expectation of  $-2X_T$  equals weighted average implied variance. Proofs appear in [19] and [22]. The following is due to [22]. Let  $P(K) := \mathbb{E}_0(K - S_T)^+$ . Assuming differentiability of  $IV_0$ ,

$$\mathbb{E}_0(-2X_T) = \int_0^{S_0} \frac{2}{K^2} P(K) \, \mathrm{d}K + \int_{S_0}^\infty \frac{2}{K^2} C(K) \, \mathrm{d}K \tag{12}$$

$$= \int_0^{S_0} \frac{2}{K} P'(K) \, \mathrm{d}K + \int_{S_0}^\infty \frac{2}{K} C'(K) \, \mathrm{d}K \tag{13}$$

$$= 2 \int_{-\infty}^{0} \left( N'(d_2) + N(-d_2)IV'_0 \right) dk$$
$$+ 2 \int_{0}^{\infty} \left( N'(d_2)IV'_0 - N(d_2) \right) dk \tag{14}$$

$$= 2 \int_{-\infty}^{\infty} kN'(d_2)d_2' dk + 2 \int_{-\infty}^{\infty} N'(d_2)IV'_0 dk \quad (15)$$

$$=2\int_{-\infty}^{\infty}kN'(d_2)d_2' + N'(d_2)d_2d_2'IV_0 \, \mathrm{d}k \tag{16}$$

$$=\int_{-\infty}^{\infty} IV_0^2(k) N'(z(k)) z'(k) \,\mathrm{d}k \tag{17}$$

where  $'$  denotes derivative (unambiguously, as  $C, P$ ,  $d_2$ ,  $IV_0$ ,  $N$  are defined as single-variable functions). For brevity, we suppress the argument  $(k)$  of  $d_2$  and  $IV_0$  and their derivatives.

To justify the integration by parts in equations  $(15,$ 16), it suffices to assume the existence of  $\varepsilon > 0$  such that  $\mathbb{E}S_T^{1+\varepsilon} < \infty$  and  $\mathbb{E}S_T^{-\varepsilon} < \infty$ . Then the *moment formula* [18] implies that for some  $\beta < 2$  and all  $|k|$ sufficiently large, we have  $IV_0^2(k) < \beta |k|$ ; hence

$$kN(d_2)|_{-\infty}^0 - kN(-d_2)|_0^{\infty} = 0$$
  
and  $N'(d_2)IV_0|_{-\infty}^{\infty} = 0$  (18)

Combining equations  $(11)$  and  $(17)$  gives the conclusion in equation  $(8)$ .

#### Implied Volatility Equals Break-even Realized Volatility

Suppose that we buy at time 0 a  $T$ -expiry  $K$ -strike call or put; to be definite, let us say a call. We pay a premium of  $C_0 := C^{BS}(IV_0^2(K), S_0, K)$ .

Dynamically, delta hedging this option using shares, we have, in principle, a position that is delta neutral and "long vega". Indeed, the implied volatility is the option's *break-even realized volatility* in the following sense: There exists a model-independent share trading strategy  $N_t$ , such that

$$P\&L := -C_0 + \int_0^T N_t \, \mathrm{d}S_t + (S_T - K)^+$$
  
< 0 in the event  $\sqrt{\langle X \rangle_T} < \mathrm{IV}_0(K)$  (19)

and  $P\&L \ge 0$  in the event  $\sqrt{\langle X \rangle_T} \ge \text{IV}_0(K)$ .

In other words, total profit/loss (from the time-0 option purchase, the trading in shares, and the time- $T$  option payout) is negative if and only if volatility realizes to less than the initial implied volatility.

Implied Volatility is Break-even Realized Volatility for Business-time Delta Hedging. Define the business-time delta hedging strategy by letting

$$\tau := \inf\{t : \langle X \rangle_t = \mathrm{IV}_0^2(K)\}\tag{20}$$

and holding  $N_t$  shares at each time  $t \in [0, T]$ , where

$$N_{t} := -\frac{\partial C^{\text{BS}}}{\partial S} (\text{IV}_{0}^{2}(K) - \langle X \rangle_{t}, S_{t}, K)$$
  
$$t \in [0, \tau \wedge T]$$
(21)

$$N_t := -\mathbb{I}(S_\tau > K), \quad t \in (\tau \wedge T, T] \tag{22}$$

The break-even property follows from applying Ito's rule to the process

$$C_t := C^{\text{BS}}(\text{IV}_0^2(K) - \langle X \rangle_t, S_t, K), \quad t \in [0, \tau \wedge T]$$
(23)

to obtain

$$\begin{split} \mathrm{d}C_{t} &= \ -\ \frac{\partial C^{\mathrm{BS}}}{\partial V} \, \mathrm{d}\langle X \rangle_{t} + \frac{\partial C^{\mathrm{BS}}}{\partial S} \, \mathrm{d}S_{t} \\ &+ \frac{1}{2} \frac{\partial^{2} C^{\mathrm{BS}}}{\partial S^{2}} \, \mathrm{d}\langle S \rangle_{t} \\ &= \left(\frac{1}{2} S_{t}^{2} \frac{\partial^{2} C^{\mathrm{BS}}}{\partial S^{2}} - \frac{\partial C^{\mathrm{BS}}}{\partial V}\right) \mathrm{d}\langle X \rangle_{t} \\ &+ \frac{\partial C^{\mathrm{bs}}}{\partial S} \, \mathrm{d}S_{t} = \frac{\partial C^{\mathrm{BS}}}{\partial S} \, \mathrm{d}S_{t} \end{split} \tag{24}$$

where the partials of  $C^{\text{BS}}$  are evaluated at  $(IV_0^2(K) \langle X \rangle_t$ ,  $S_t$ ,  $K$ ). Therefore,

$$-C_{\tau \wedge T} = -C_0 - \int_0^{\tau \wedge T} \frac{\partial C^{\text{BS}}}{\partial S} \, \text{d}S_t \qquad (25)$$

as shown in [2, 11, 20].

In the event  $\langle X \rangle_T < \text{IV}_0^2(K)$ , hence  $T < \tau$ , we have

$$P&L = (S_T - K)^+ - C_T$$
  
=  $(S_T - K)^+ - C^{BS}(\text{IV}_0^2(K) - \langle X \rangle_T, S_T, K)$   
< 0 (26)

and in the event  $\langle X \rangle_T \geq \mathrm{IV}_0^2(K)$ , hence  $\tau \leq T$ , we have

$$P&L = (S_T - K)^+ - C_\tau - \int_\tau^T \mathbb{I}(S_\tau > K) \, dS_t$$
  
=  $(S_T - K)^+ - (S_\tau - K)^+$   
 $- \mathbb{I}(S_\tau > K)(S_T - S_\tau) \ge 0$  (27)

as claimed. This break-even result is a special case of a proposition in  $[6]$ .

Implied Volatility is Not Break-even Realized Volatility for Standard Delta Hedging. The breakeven property of the previous section does not extend to standard "calendar time" delta hedging, defined by share holdings

$$-\frac{\partial C^{\text{BS}}}{\partial S}((T-t)\bar{\text{IV}}_0^2, S_t, K), \quad t \in [0, T] \tag{28}$$

where  $\text{I}\overline{\text{V}}_0^2 := \text{IV}_0^2(K)/\textit{T}$  denotes the time-0 annualized implied variance.

This strategy guarantees neither a profit in the event that  $\langle X \rangle_T > \mathrm{IV}_0^2(K)$  nor a loss in the opposite event. To see this, under the dynamics (2), let

$$Y_t = C^{\text{BS}}((T-t)\bar{\text{IV}}_0^2, S_t, K) \tag{29}$$

and apply Ito's rule to obtain

$$\begin{split} \mathrm{d}Y_{t} &= -\frac{\partial C^{\mathrm{BS}}}{\partial V} \bar{\mathrm{I}} \bar{\mathrm{V}}_{0}^{2} \, \mathrm{d}t + \frac{\partial C^{\mathrm{BS}}}{\partial S} \, \mathrm{d}S_{t} \\ &+ \frac{1}{2} \frac{\partial^{2} C^{\mathrm{BS}}}{\partial S^{2}} \, \mathrm{d}\langle S \rangle_{t} \\ &= -\frac{1}{2} \bar{\mathrm{I}} \bar{\mathrm{V}}_{0}^{2} S_{t}^{2} \frac{\partial^{2} C^{\mathrm{BS}}}{\partial S^{2}} \, \mathrm{d}t + \frac{\partial C^{\mathrm{BS}}}{\partial S} \, \mathrm{d}S_{t} \\ &+ \frac{1}{2} \sigma_{t}^{2} S_{t}^{2} \frac{\partial^{2} C^{\mathrm{BS}}}{\partial S^{2}} \, \mathrm{d}t \end{split} \tag{30}$$

where the partial derivatives of  $C^{BS}$  are evaluated at  $((T-t)\overline{\mathrm{IV}}_0^2, S_t, K)$ . Hence,

$$P\&L = Y_T - Y_0 - \int_0^T \frac{\partial C^{\text{BS}}}{\partial S} \, \text{d}S_t$$
$$= \int_0^T \frac{1}{2} (\sigma_t^2 - \bar{\text{IV}}_0^2) S_t^2 \frac{\partial^2 C^{\text{BS}}}{\partial S^2} \, \text{d}t \qquad (31)$$

which is half the time-integrated cash-gamma*weighted* difference of instantaneous variance  $\sigma_t^2$  and implied variance  $\bar{IV}_0^2$ , as shown in [7] and [12]. So if, along some trajectory,  $\sigma_t > \overline{\text{IV}}_0$  at points where gamma is low, but  $\sigma_t < \bar{IV}_0$  at points where gamma is high, then it can occur that realized variance  $\int_0^T \sigma_t^2 dt$ exceeds implied variance  $IV_0^2$ , yet this long-vega strategy incurs a loss.

In conclusion, implied volatility is the option's break-even realized volatility for business-time delta hedging, but not for calendar-time delta hedging.

# Implied Volatility ATM Approximates Expected Realized Volatility, Under an Independence Condition

In this section, we specialize to dynamics (2) such that  $\sigma$  and W are *independent*.

Let  $K_{\text{atm}} := S_0$  be the at-the-money (ATM) strike. Then

$$\mathbb{E}(S_T - K_{\text{atm}})^+ = \mathbb{E}C^{\text{bs}}(\sqrt{\langle X \rangle_T}, S_0, K_{\text{atm}}) \qquad (32)$$
$$\leq C^{\text{bs}}(\mathbb{E}\sqrt{\langle X \rangle_T}, S_0, K_{\text{atm}}) \qquad (33)$$

by the conditioning argument of  $[15]$ , independence, and the concavity of

$$v \mapsto C^{\text{bs}}(v, S_0, K_{\text{atm}}) \tag{34}$$

It follows that

$$IV_0(K_{\text{atm}}) \le \mathbb{E}\sqrt{\langle X \rangle_T} \tag{35}$$

The function (34), while concave, is nearly linear for small  $v$ ; indeed, its second derivative vanishes at  $v = 0$ , as observed in [4]. Therefore, the inequalities  $(33)$  and  $(35)$  are nearly equalities, as shown in [13]. In that sense,

$$IV_0(K_{\text{atm}}) \approx \mathbb{E}\sqrt{\langle X \rangle_T} \tag{36}$$

assuming the independence of  $\sigma$  and W.

## Model-free Implied Volatility (MFIV)

Inverting Black-Scholes is not the only way to extract an implied volatility from option prices. While the ATM Black-Scholes implied volatility approximates expected volatility under the independence assumption, alternative definitions of MFIV use call/put data at all strikes, in order to reflect the expected variance or volatility under more general conditions.

#### VIX-style MFIV Equals the Square Root of Expected Realized Variance

Motivated by equation (11), define the VIX-style model-free implied volatility by

$$\begin{aligned} \textit{VIXIV}_{0} &:= \sqrt{\mathbb{E}_{0}[-2X_{T}]} \\ &:= \sqrt{\mathbb{E}_{0}[-2\log(S_{T}/S_{0}) + 2(S_{T}/S_{0}) - 2]} \end{aligned} \tag{37}$$

 $VIXIV_0$  is an observable function of option prices, specifically the square root of the time-0 value of the portfolio

$$2/K^2 dK$$
 calls at strikes  $K > S_0$   
 $2/K^2 dK$  puts at strikes  $K < S_0$  (38)

Indeed in 2003, the Chicago board options exchange (CBOE) [8] adopted an implementation of equation  $(38)$  to define the VIX volatility index (but due to the availability of only finitely many strikes in practice, the CBOE VIX is not precisely identical to  $VIXIV_0$ ; see [16]).

By equation (11), the square of VIX-style MFIV equals expected realized variance:

$$VIXIV_{0} = \sqrt{\mathbb{E}_{0} \langle X \rangle_{T}} \tag{39}$$

However, by Jensen's inequality, for random  $\langle X \rangle_T$ ,

$$VIXIV_0 > \mathbb{E}_0 \sqrt{\langle X \rangle_T} \tag{40}$$

thus, VIX-style MFIV differs from expected realized volatility, due to convexity.

#### SVS-style MFIV Equals Expected Realized Volatility

For nonconstant  $\langle X \rangle_T$ , the VIX-style MFIV never equals  $\mathbb{E}_0\sqrt{\langle X\rangle_T}$ ; in contrast, the SVS-style MFIV will equal  $\mathbb{E}_0\sqrt{\langle X\rangle_T}$  exactly under an independence condition, and approximately under perturbations of that condition. Define SVS-style model-free implied volatility (where SVS stands for "synthetic volatility swap") by

$$SVSIV_0 := \mathbb{E}_0 \sqrt{\frac{\pi}{2}} e^{X_T/2}$$
$$\times \left| X_T I_0(X_T/2) - X_T I_1(X_T/2) \right| \quad (41)$$

where  $X_T := \log(S_T/S_0)$  and  $I_\nu$  is the modified Bessel function of order  $\nu$ .

 $SVSIV_0$  is observable from option prices, as the time-0 value of the portfolio

$$\sqrt{\pi/2}/S_0$$

straddles at strike  $K = S_0$ ,

$$\sqrt{\frac{\pi}{8K^{3}S_{0}}} \Big[ I_{1} \big( \log \sqrt{K/S_{0}} \big) - I_{0} \big( \log \sqrt{K/S_{0}} \big) \Big] \mathrm{d}K$$
  
calls at strikes  $K > S_{0}$ ,  
$$\sqrt{\frac{\pi}{8K^{3}S_{0}}} \Big[ I_{0} \big( \log \sqrt{K/S_{0}} \big) - I_{1} \big( \log \sqrt{K/S_{0}} \big) \Big] \mathrm{d}K$$
  
puts at strikes  $K < S_{0}$  (42)

Under the dynamics (2) with  $\sigma$  and W independent, the exact equality

$$SVSIV_0 = \mathbb{E}_0 \sqrt{\langle X \rangle_T} \tag{43}$$

is proved in [5]. Moreover, it still holds approximately, under perturbations of the independence assumption. To be precise, consider a family of processes  $S^{[\rho]}$ , indexed by parameters  $\rho \in [-1, 1]$ , and defined by

$$dS_t^{[\rho]} = \sqrt{1 - \rho^2} \sigma_t S_t^{[\rho]} dW_{1t} + \rho \sigma_t S_t^{[\rho]} dW_{2t}$$
  
$$S_0^{[\rho]} = S_0 \tag{44}$$

where  $W_1$  and  $W_2$  are  $\mathcal{F}_t$ -Brownian motions, and  $\sigma$  and  $W_2$  are adapted to some filtration  $\mathcal{H}_t \subseteq \mathcal{F}_t$ ,<br>where  $\mathcal{H}_T$  and  $\mathcal{F}_T^{W_1}$  are independent. This includes all the standard stochastic volatility models of the form  $d\sigma_t = \alpha(\sigma_t) dt + \beta(\sigma_t) dW_{2t}$ .

Changing the  $\rho$  parameter does not affect the  $\sigma$  dynamics, and hence cannot affect  $\mathbb{E}_0\sqrt{\langle X\rangle_T}$ . However, changing  $\rho$  does change the S dynamics, and hence may change option prices,  $IV_0(K_{\text{atm}})$ , and  $SVSIV_0$ . Thus, the relationships (36, 43) below

$$\text{IV}_0(K_{\text{atm}}) \approx \mathbb{E}_0 \sqrt{\langle X \rangle_T}, \quad \text{SVSIV}_0 = \mathbb{E}_0 \sqrt{\langle X \rangle_T}$$
(45)

that are valid for the uncorrelated case  $S = S^{[0]}$ , may not hold for  $S = S^{[\rho]}$  where  $\rho \neq 0$ . Unlike IV<sub>0</sub>( $K_{\text{atm}}$ ), the  $SVSIV_0$  has the robustness property of being *immunized* against perturbations of  $\rho$  around  $\rho = 0$ , meaning that

$$\left. \frac{\partial}{\partial \rho} \right|_{\rho=0} SV\!SIV_0 = 0 \tag{46}$$

can be verified. This suggests that SVS-style implied volatility *SVSIV* <sup>0</sup> should outperform Black–Scholes implied volatility IV0, as an approximation to the expected realized volatility, at least for *ρ* not too large.

This is confirmed in [5] for Heston dynamics with parameters from [1], and *T* = 0*.*5. Across essentially all correlation assumptions, the SVS notion of implied volatility exhibited the smallest bias, relative to the true expected annualized volatility. For example, in the case *ρ* = −0*.*64, the VIX-style implied volatility had bias +98 bp, the Black–Scholes implied volatility had bias −30 bp, and the SVS-style implied volatility had the smallest bias, −6 bp.

## **Acknowledgments**

This article benefited from the comments of Peter Carr.

## **References**

- [1] Bakshi, G., Cao, C. & Chen, Z. (1997). Empirical performance of alternative option pricing models, *Journal of Finance* **52**, 2003–2049.
- [2] Bick, A. (1995). Quadratic-variation-based dynamic strategies, *Management Science* **41**, 722–732.
- [3] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–659.
- [4] Brenner, M. & Subrahmanyam, M. (1988). A simple formula to compute the implied standard deviation, *Financial Analysts Journal* **44**, 80–83.
- [5] Carr, P. & Lee, R. (2008). *Robust Replication of Volatility Derivatives*, Bloomberg LP, University of Chicago.
- [6] Carr, P. & Lee, R. (2008). *Hedging Variance Options on Continuous Semimartingales*, Forthcoming in Finance and Stochastics.
- [7] Carr, P. & Madan, D. (1998). Towards a theory of volatility trading, in *Volatility*, R. Jarrow, ed, Risk Publications, pp. 417–427.

- [8] CBOE. (2003). The VIX White Paper, Chicago Board Options Exchange.
- [9] Derman, E., Demeterfi, K., Kamal, M. & Zou, J. (1999). A guide to volatility and variance swaps, *Journal of Derivatives* **6**, 9–32.
- [10] Dupire, B. (1992). *Arbitrage pricing with stochastic volatility*, *Soc´et´e G´en´erale*.
- [11] Dupire, B. (2005). *Volatility Derivatives Modeling*, Bloomberg LP.
- [12] El Karoui, N., Jeanblanc-Picque, M. & Shreve, S. ´ (1998). Robustness of the Black and Scholes formula, *Mathematical Finance* **8**, 93–126.
- [13] Feinstein, S.P. (1989). *The Black–Scholes Formula is Nearly Linear in Sigma for At-the-Money Options: Therefore Implied Volatilities from At-the-Money Options are Virtually Unbiased*, Federal Reserve Bank of Atlanta.
- [14] Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*, John Wiley & Sons.
- [15] Hull, J. & White, A. (1987). The pricing of options on assets with stochastic volatilities, *Journal of Finance* **42**, 281–300.
- [16] Jiang, G.J. & Tian, Y.S. (2005). The model-free implied volatility and its information content, *Review of Financial Studies* **18**, 1305–1342.
- [17] Lee, R. (2004). Implied volatility: statics, dynamics, and probabilistic interpretation, *Recent Advances in Applied Probability*, Springer, pp. 241–268.
- [18] Lee, R. (2004). The moment formula for implied volatility at extreme strikes, *Mathematical Finance* **14**, 469–480.
- [19] Matytsin, A. (2000). *Perturbative Analysis of Volatility Smiles*, Merrill Lynch.
- [20] Mykland, P. (2000). Conservative delta hedging, *Annals of Applied Probability* **10**, 664–683.
- [21] Neuberger, A. (1994). The log contract, *Journal of Portfolio Management* **20**, 74–80.
- [22] Polishchuk, A. (2007). *Variance swap voluation*, Bloomberg LP.
- [23] Rebonato, R. (1999). *Volatility and Correlation in the Pricing of Equity, FX and Interest Rate Options*, John Wiley & Sons.

PETER CARR & ROGER LEE
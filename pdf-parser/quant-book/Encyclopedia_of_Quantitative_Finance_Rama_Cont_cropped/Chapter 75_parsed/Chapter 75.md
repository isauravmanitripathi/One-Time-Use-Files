# **Change of Numeraire**

Consider a financial market model with nondividend paying asset price processes  $(S^0, S^1, \ldots, S^N)$  living on a filtered probability space  $(\Omega, \mathcal{F}, \mathbf{F}, P)$ , where  $\mathbf{F} = \{\mathcal{F}_t\}_{t>0}$  and P is the objective probability measure. For general results concerning completeness, self-financing portfolios, martingale measures, and arbitrage, (see Arbitrage Strategy; Fundamental Theorem of Asset Pricing; Risk-neutral Pricing).

We choose the asset  $S^0$  as the numeraire asset, and we assume that  $S_t^0 > 0$  with probability 1. From general theory, we know that (modulo integrability and technical conditions) the market is free of arbitrage if and only if there exists a measure  $Q^0 \sim P$ such that the normalized price processes

$$\frac{S_t^0}{S_t^0}, \frac{S_t^1}{S_t^0}, \ldots, \frac{S_t^N}{S_t^0}$$

are  $O^0$  martingales. Using the notation  $Z^i = S^i / S^0$ , thus we also have, apart from the nominal price system  $S^0, S^1, \ldots, S^n$ , the normalized price system  $Z^0, Z^1, \ldots, Z^n$ . The economic importance of the normalized system is clarified by the following standard result.

**Proposition 1** With notation as defined above the following hold.

- A portfolio is self-financing in the S system if and only if it is self-financing in the  $Z$  system.
- $\bullet$  A portfolio is an arbitrage opportunity in the S system if and only if it is an arbitrage in the  $Z$ system.
- The S market is complete if and only if the  $Z$ market is complete.
- In the Z market, the asset  $Z^0$  has the property that  $Z_t^0 \equiv 1$ , so it represents a bank account with zero interest rate.

If  $X \in \mathcal{F}_T$  is a fixed contingent claim with exercise date  $T$ , and if we denote the (not necessarily unique) arbitrage-free price process of X by  $\Pi_t[X]$ , then by applying the above-mentioned result to the extended market  $S^0$ ,  $S^1$ ,...,  $S^N$ ,  $\Pi_t[X]$  we see that  $\Pi_t[X]/S_t^0$ is a  $Q^0$  martingale, and using this fact together with the obvious fact that  $\n\Pi_T[X] = X\n$  we obtain the basic

pricing formula:

$$\Pi_t[X] = S_t^0 E^0 \left[ \frac{X}{S_T^0} \middle| \mathcal{F}_t \right] \tag{1}$$

where  $E^0$  denotes integration with respect to (w.r.t.)  $O^0$ .

Very often one uses the bank account  $B$  with dynamics

$$dB_t = r_t B_t dt, \quad B_0 = 1 \tag{2}$$

where  $r$  is the short rate, as numeraire. The corresponding martingale measure  $Q^B$  is then often denoted by  $O$  and referred to as "the risk neutral martingale measure". In this case, the pricing formula becomes

$$\Pi_t[X] = E^{\mathcal{Q}} \left[ e^{-\int_t^T r_s \, ds} X \Big| \mathcal{F}_t \right] \tag{3}$$

In many concrete situations, the computational work needed for the determination of arbitrage-free prices can be drastically reduced by a clever choice of numeraire, and the purpose of this article is to analyze such changes.

To set the scene, we consider a fixed risk neutral martingale measure  $Q$  for the numeraire  $B$ , and an alternative numeraire asset  $S^0$  with the corresponding martingale measure  $Q^0$ . Our first task is to find the measure transformation between  $O$  and  $O^0$ .

To see what  $Q^0$  must look like, we consider a fixed time  $T$  and an arbitrarily chosen  $T$ -claim  $X$ . Assuming enough integrability we then know that, by using  $B$  as the numeraire, the arbitrage-free price of *X* at time  $t = 0$  is given as

$$\Pi_0[X] = E^{\mathcal{Q}} \left[ \frac{X}{B_T} \right] \n$$
(4)

On the other hand, using  $S^0$  as numeraire, the price is also given by the following formula:

$$\Pi_0[X] = S_0^0 E^0 \left[ \frac{X}{S_T^0} \right] \n$$
(5)

Defining the likelihood process L by  $L_t = dQ^0/$  $dQ$  on  $\mathcal{F}_t$ , we thus have

$$E^{\mathcal{Q}}\left[\frac{X}{B_T}\right] = S_0^0 E^{\mathcal{Q}}\left[L_T \frac{X}{S_T^0}\right] \tag{6}$$

Since this holds for all  $X \in \mathcal{F}_T$ , we have the following basic result.

**Proposition 2** Under the above-mentioned assumptions, the likelihood process  $L$ , defined as

$$L_t = \frac{\mathrm{d}Q^0}{\mathrm{d}Q}, \quad \text{on} \quad \mathcal{F}_t, \quad 0 \le t \le T \tag{7}$$

is given by the formula

$$L_t = \frac{S_t^0}{S_0^0 \cdot B_t} \tag{8}$$

We note that since  $S^0/B$  is a O martingale, the likelihood process  $L$  is also, as expected, a  $Q$ martingale.

As an immediate corollary we have the following.

**Proposition 3** Assume that the  $S^0$  dynamics under the  $Q$  measure are of the form

$$dS_t^0 = r_t S_t^0 dt + S_t^0 \sigma_t dW_t^Q \tag{9}$$

where  $W^Q$  is a d-dimensional O Wiener process, r is the short rate, and  $\sigma$  is a d-dimensional optional row vector process. Then the dynamics for the likelihood process  $L$  are of the form

$$\mathrm{d}L_t = L_t \sigma_t \,\mathrm{d}W_t^{\mathcal{Q}} \tag{10}$$

We can thus easily construct the relevant Girsanov transformation directly from the volatility of the  $S^0$ process.

We can, in a straightforward manner, extend Proposition 3 to change from one numeraire  $Q^0$  to another numeraire  $Q^1$ . The proof is obvious.

**Proposition 4** Let  $S^0$  and  $S^1$  be two strictly positive numeraire assets with the corresponding martingale measures  $Q^0$  and  $Q^1$ . Denote the likelihood process  $L^{0,1}$  as

$$L_t^{0,1} = \frac{\mathrm{d}Q^1}{\mathrm{d}Q^0}, \quad \text{on} \quad \mathcal{F}_t \tag{11}$$

Then  $L^{0,1}$  is given by

$$L_t^{0,1} = \frac{S_t^1}{S_t^0} \cdot \frac{S_0^0}{S_0^1} \tag{12}$$

**Remark 1** It may perhaps seem surprising that even in the case of an incomplete market, we obtain a unique martingale measure  $O^0$ . In more detail, the situation is as follows.

- If the market is incomplete, then there will exist . several risk neutral measures  $Q$ .
- Each of these measures generates a different price system, defined by the pricing formula (3).
- Choosing one particular  $Q$  is thus equivalent to choosing one particular price system.
- For a given numeraire  $S^0$ , there will also exist several different martingale measures  $O^0$ .
- Each of these measures generates a different price system, defined by the pricing formula (1).
- If a risk neutral measure  $Q$  and thus a price system are fixed, there exists a unique measure  $Q^0$  such that  $Q^0$  generates the same price system as  $O$ .
- The measure transformations considered here are . precisely those corresponding to a change of measure within a given price system.

### **Pricing Homogeneous Contracts**

Using a numeraire  $S^0$  is particularly useful when the claim X is of the form  $X = S_T^0 \cdot Y$ , since then we obtain the following simple expression:

$$\Pi_t[X] = S_t^0 E^0[Y|\mathcal{F}_t] \tag{13}$$

A typical example when this situation occurs is when dealing with derivatives defined in terms of several underlying assets. Assume, for example, that we are given two asset prices  $S^0$  and  $S^1$ , and that the contract X to be priced is of the form  $X = \Phi(S_T^0, S_T^1)$ , where  $\Phi$  is a given linearly homogeneous function. Using the standard machinery, we would have to compute the price as

$$\Pi_t[X] = E^0 \left[ e^{-\int_t^T r(s) \, \mathrm{d}s} \Phi(S_T^0, S_T^1) \middle| \mathcal{F}_t \right] \tag{14}$$

which essentially amounts to the calculation of a triple integral. If we instead use  $S^0$  as numeraire we have

$$\Pi_t[X] = S_t^0 E^0 \left[ \frac{1}{S_T^0} \Phi(S_T^0, S_T^1) \Big| \mathcal{F}_t \right]\n$$

$$\n= S_t^0 E^0 \left[ \Phi\left(1, \frac{S_T^1}{S_T^0}\right) \mathcal{F}_t \right]$$

$$=S_t^0 E^0[\varphi(Z_T)\mathcal{F}_t] \tag{15}$$

where  $\varphi(z) = \Phi(1, z)$  and  $Z_T = S_T^1 / S_T^0$ . Note that the factor  $S_t^0$  is the price of the traded asset  $S^0$  at time  $t$ , so this quantity does not have to be computed—it can be directly observed on the market. Thus, the computational work is reduced to computing a single integral.

As an example, assume that we have two stocks.  $S^0$  and  $S^1$ , with price processes of the following form under the objective probability  $P$ :

$$\mathrm{d}S_t^0 = \alpha S_t^0 \,\mathrm{d}t + \sigma S_t^0 \,\mathrm{d}\tilde{W}_t^0 \tag{16}$$

$$\mathrm{d}S_t^1 = \beta S_t^1 \,\mathrm{d}t + \delta S_t^1 \,\mathrm{d}\tilde{W}_t^1. \tag{17}$$

Here  $\tilde{W}^0$  and  $\tilde{W}^1$  are assumed to be independent  $P$ -Wiener processes, but it would also be easy to treat the case when there is a coupling between the two assets.

Under  $Q$  the price dynamics will be given as

$$dS_t^0 = rS_t^0 dt + \sigma S_t^0 dW_t^0 \tag{18}$$

$$dS_t^1 = rS_t^1 dt + \delta S_t^1 dW_t^1 \tag{19}$$

where  $W^0$  and  $W^1$  are Q-Wiener processes, and from Proposition 3 it follows that the Girsanov transformation from Q to  $Q^0$  has a likelihood process with dynamics given as

$$dL_t = L_t \sigma \, dW_t^0 \tag{20}$$

The  $T$ -claim to be priced is an exchange option, which gives the holder the right, but not the obligation, to exchange one  $S^0$  share for one  $S^1$  share at time  $T$ . Formally, this means that the claim is given by  $X = \max[S_T^1 - S_T^0, 0]$ , and we note that we have a linearly homogeneous contract function. From equation  $(15)$ , the price process is given as

$$\Pi_t[X] = S_t^0 E^0[\max[Z_T - 1, 0] | \mathcal{F}_t] \tag{21}$$

with  $Z(t) = S_t^1 / S_t^0$ . We are thus, in fact, valuing a European call option on  $Z_T$ , with strike price  $K = 1$ .

By construction, Z will be a  $Q^0$ -martingale, and since a Girsanov transformation will not affect the volatility, it follows easily from equations (16) and (17) that the  $Q^0$ -dynamics of Z are given by

$$dZ_t = Z_t \sqrt{\sigma^2 + \delta^2} \mathrm{d}W_t \tag{22}$$

where W is a standard  $Q^0$ -Wiener process. The price is thus given by the following formula:

$$\Pi_t[X] = S_t^0 \cdot c(t, Z_t) \tag{23}$$

Here  $c(t, z)$  is given directly by the Black–Scholes formula as the price of a European call option, valued at t, with time of maturity T, strike price  $K = 1$ , short rate  $r = 0$ , on a stock with volatility  $\sqrt{\sigma^2 + \delta^2}$ and price  $z$ .

# **Forward Measures**

We now specialize the theory to the case when the chosen numeraire is a zero coupon bond. As can be expected, this choice of numeraire is particularly useful when dealing with interest rate derivatives.

Suppose, therefore, that we are given a specified bond market model with a fixed risk neutral martingale measure  $Q$  (always with  $B$  as numeraire). For a fixed time of maturity  $T$ , we now choose the price process  $p(t, T)$ , of a zero coupon bond maturing at  $T$ , as our new numeraire.

**Definition 1** The T-forward measure  $Q^T$  is defined as

$$L_t^T = \frac{\mathrm{d}Q^T}{\mathrm{d}Q} \tag{24}$$

on  $\mathcal{F}_t$  for  $0 < t < T$  where  $L^T$  is defined as

$$L_t^T = \frac{p(t,T)}{B_t p(0,T)}$$
 (25)

Observing that  $p(T, T) = 1$  we have the following useful pricing formula as an immediate corollary of Proposition 3.

**Proposition 5** For any sufficiently integrable  $T$ -claim  $X$ , we have the pricing formula

$$\Pi_t[X] = p(t, T)E^T[X|\mathcal{F}t] \tag{26}$$

where  $E^{T}$  denotes integration w.r.t.  $Q^{T}$ .

Note again that the price  $p(t, T)$  does not have to be computed. It can be observed directly on the market at time  $t$ .

A natural question to ask is when  $Q$  and  $Q^T$ coincide. This occurs if and only if we  $Q$ -a.s. have  $L^{T}(T) = 1$ , that is when

$$1 = \frac{p(T,T)}{B_T p(0,T)} = \frac{e^{-\int_0^T r(s) ds}}{E^{\mathcal{Q}} \left[ e^{-\int_0^T r(s) ds} \right]}$$
(27)

that is if and only if  $r$  is deterministic.

### The General Option Pricing Formula

We now present a fairly general formula for the pricing of European call options. Therefore, assume that we are given a financial market with a (possibly stochastic) short rate  $r$  and a strictly positive asset price process  $S$ . We also assume the existence of a risk neutral martingale measure  $Q$ .

Consider now a fixed time  $T$ , and a European call on  $S$  with exercise date  $T$  and strike price  $K$ . We are, thus, considering the  $T$ -claim:

$$X = \max[S_T - K, 0] \tag{28}$$

The main trick when dealing with options is to write  $X$  as

$$X = (S_T - K) \cdot I\{S_T \ge K\}$$
  
=  $S_T \cdot I\{S_T \ge K\} - K \cdot I\{S_T \ge K\}$  (29)

where  $I$  denotes an indicator function. Using the linear property of pricing we thus obtain

$$\Pi_t[X] = \Pi_t[S_T \cdot I\{S_T \ge K\}] - K \cdot \Pi_t[I\{S_T \ge K\}]\n$$
(30)

For the first term, we change to the measure  $Q^S$ having  $S$  as numeraire, and for the second term, we use the  $T$ -forward measure. Using the pricing formula  $(1)$  twice, once for each numeraire, we obtain the following basic option pricing formula, where we recognize the structure of the standard Black–Scholes formula.

**Proposition 6** Given the above-mentioned assumptions, the option price is given as

$$\Pi_t[X] = S_t Q^S(S_T \ge K | \mathcal{F}t) \n- Kp(t, T) Q^T(S_T \ge K | \mathcal{F}_t) \quad (31)$$

# Notes

The first use of a numeraire different from the riskfree asset  $B$  was probably in [8] where, however,

the technique is not explicitly discussed. The first explicit use of a change of numeraire change was in [7], where an underlying stock was used as numeraire in order to value an exchange option. The numeraire change is also used in  $[4, 5]$  and basically in all later works on the existence of martingale measures in order to reduce the general case to the basic case of zero short rate. In these papers, the numeraire change as such is, however, not put to systematic use as an instrument for facilitating the computation of option prices in complicated models. In the context of interest rate theory, changes of numeraire were used and discussed independently in [2] and (within a Gaussian framework) in [6], where in both cases a bond maturing at a fixed time  $T$  is used as numeraire. A systematic study of general changes of numeraire can be found in [3]. For further examples of the change of numeraire technique see [1].

# References

- [1] Benninga, S., Biörk, T. & Wiener, Z. (2002). On the use of numeraires in option pricing, Journal of Derivatives  $43 - 58.$
- [2] Geman, H. (1989). The Importance of the Forward Neutral Probability in a Stochastic Approach of Interest Rates. Working paper, ESSEC, 10.
- [3] Geman, H., El Karoui, N. & Rochet, J.-C. (1995). Changes of numéraire, changes of probability measure and option pricing, Journal of Applied Probability 32, 443-458.
- [4] Harrison, J. & Kreps, J. (1979). Martingales and arbitrage in multiperiod markets, Journal of Economic Theory 11,  $418 - 443.$
- [5] Harrison, J. & Pliska, S. (1981). Martingales and stochastic integrals in the theory of continuous trading, *Stochastic* Processes and Applications 11, 215–260.
- [6] Jamshidian, F. (1989). An exact bond option formula. Journal of Finance 44, 205-209.
- [7] Margrabe, W. (1978). The value of an option to exchange one asset for another. Journal of Finance 33, 177-186.
- [8] Merton, R. (1973). The theory of rational option pricing. Bell Journal of Economics and Management Science 4,  $141 - 183$ .

# **Related Articles**

### Forward and Swap Measures.

### TOMAS BJÖRK
# **Credit Default Swaption**

Credit default swap (CDS) options, also known as single name credit default swaptions, allow an investor to buy protection on a reference name by entering a CDS (see Credit Default Swaps) at a previously set CDS spread. CDS options may knock out if the reference entity defaults before the exercise date. Usually, the buyer of protection will also receive the default payment in that case. Such a cash flow simply corresponds to the default leg of a CDS with maturity equal to the exercise date. We will thereafter assume cancellation of the contract if the underlying name defaults before the exercise date. We refer to Credit Default Swap Index Options for the extensions to the portfolio case.

Denote the default time associated with the underlying name by  $\tau$ . This is usually the date of a credit event; we refer to ISDA master agreement for further details, given that this notion may vary through time and differ across geographical regions. For  $t < s$ , we denote by  $B(t, s)$  the time t price of a defaultable discount bond, paying one at time  $s$  if  $\tau > s$  and zero otherwise. Clearly,  $B(t, s)$  collapses to zero at the default of the underlying name if it occurs before  $s$ , since no payment will eventually be received by the discount bond holder.  $T_1, \ldots, T_N$ denote the payment dates on the premium leg of the underlying CDS. For simplicity, we will further neglect effects of accrued premiums.  $T$  is the exercise date of the European credit spread call option and  $p$  the strike. We can write the payoff at time  $T$  as  $(p_T - p)^+ \sum_{T_k > T} \tilde{B}(T, T_k)$ .  $p_T$  is the CDS par spread at time  $T$ . There is also usually a multiplica-

tive adjustment to take into account the premium payment frequency, which is quarterly in most cases and which is not dealt with here for notational simplicity. For the same reason, we do not account for a possible up-front payment associated with the CDS, which is likely to be applied after the implementation of the "big bang" CDS protocol. That will result in some small adjustments to the payoff function and thus to the pricing formulas, which will be neglected thereafter. Clearly,  $p_T$  is not defined if the option has already cancelled out, that is, if  $\tau < T$ , but the option payoff is equal to zero in that case.

## **Pricing Approaches**

With some adaptations due to the cancellation feature of the CDS option, the pricing methodology parallels the well-known approaches in interest rate swaptions. One may consider a suitable distribution of the forward CDS spread under an appropriate riskneutral measure. This readily leads to a Black-type pricing formula and is dealt with first. In another approach, one can rather model the "instantaneous" CDS spread, which is related to the "intensity" of the default time.

### Black Formula for Credit Default Swap Options

As usual  $r$  denotes the default-free short rate and  $Q$  is the usual risk-neutral probability associated with the savings account. We consider  $G = (G_t)$ , a filtration such that  $\tau$  is a stopping time and r is an adapted process.

The idea of using "survival measures" was introduced in  $[9]$  and further developed in  $[4, 6, 7, 10]$ , among others (see also Credit Default Swap Index **Options**). We will denote by  $\sum \tilde{B}(t, T_k)$  the "risky level" which corresponds to the time  $t$  price of a unitary premium leg associated with the forward CDS starting at T. We consider the probability measure  $\hat{O}$ associated with the previous risky level numéraire (see also Change of Numeraire about change of numéraire techniques) defined by

$$\frac{\mathrm{d}\hat{Q}}{\mathrm{d}Q} = \frac{\sum_{T_k>T} \tilde{B}(T, T_k)}{\sum_{T_k>T} \tilde{B}(0, T_k)} \exp{-\int_0^T r(u) \,\mathrm{d}u} \qquad (1)$$

Let us remark that  $\frac{\mathrm{d}\hat{Q}}{\mathrm{d}O} = 0$  on the set  $\{\tau \leq T\}$ .

Thus  $\hat{Q}$  is absolutely continuous but not equivalent to  $Q. \hat{Q}(\tau > T) = 1$  which leads to the terminology "survival measure". We can then readily express the value of the credit spread option at  $t = 0$  as

$$\left(\sum_{T_k>T}\tilde{B}(0,T_k)\right)E^{\hat{Q}}\left[(p_T-p)^+\right] \qquad (2)$$

We can get around the issue of the CDS premium  $p_T$  not being defined *after default* by considering  $p_T 1_{\{\tau>T\}}$ , which we assume to be a random variable

with respect to  $G_T$ . This does not change the computation in the previous equation since  $\hat{Q}(\tau > T) = 1$ .

Let us first remark that for the forward CDS to be priced normally, we must have  $E^{Q}[p_{T}1_{\{\tau>T\}}] = p_{0,T}$ where  $p_{0,T}$  denotes the forward CDS premium. In the case where  $p_T 1_{\{\tau>T\}}$  is lognormal under  $\hat{Q}$ , with volatility parameter  $\sigma$ , we readily get a Black formula for the price of the CDS option:

$$\left(\sum_{T_k>T}\tilde{B}(0,T_k)\right)\times(p_{0,T}N(d_1)-pN(d_2))\quad(3)$$

where 
$$d_1 = \frac{\ln\left(\frac{p_{0,T}}{p}\right) + \frac{\sigma^2}{2}T}{\sigma\sqrt{T}}$$
 and  $d_2 = d_1 - \sigma\sqrt{T}$ .

#### Intensity Approaches

Another approach consists in specifying the intensity of the default time. This is the path followed in  $[2-4]$ . To circumvent the difficulty with default intensity dropping down to zero after default and the various mathematical issues related to enlargement of filtrations, the easiest way is to model the default time through a Cox process. We thus define the default time  $\tau$  associated with the underlying name as

$$\tau = \inf \left\{ t, \int_{0}^{t} \lambda(s) \, \mathrm{d}s \ge -\ln U \right\} \tag{4}$$

where  $\lambda$  is a positive process adapted to some filtration  $\Im = (\Im_t)$  and U follows a standard uniform variable independent of  $\Im$ . For simplicity, we will further assume that  $(\Im, Q)$  is a Brownian filtration. Following [1] or [8], we define as  $H = (H_t)$  the filtration generated by the counting process  $N_t = 1_{\{\tau < t\}}$  and we denote by  $G_t = \mathfrak{F}_t \vee H_t$ , the relevant information at time  $t$ , incorporating knowledge about occurrence of default prior to  $t$  and current and past values of financial variables such as interest rates or credit spreads of the reference entity (see Filtrations for mathematical details about filtrations in finance). Up to default time,  $\lambda(t)$  is the default intensity of  $\tau$  (we refer to **Point Processes** regarding point processes and to **Compensators** about compensators and intensities). While the default intensity drops to zero after  $\tau$ , we can remark that  $\lambda(t)$  is still well defined, thanks to the above Cox modeling framework. For instance, one can consider shifted Cox-Ingersoll-Ross (CIR) processes for the short rate r and the pseudodefault intensity  $\lambda$  (see Cox-Ingersoll-Ross (CIR) Model).

 $p_{t,T}$  will further denote the time t forward CDS premium. Though  $p_{t,T}$  has a financial meaning only on the set  $\{\tau > t\}$ , its computation can be extended to the complete set of events in the previous Cox modeling framework (see [4] for further discussion).  $p_{t,T}$  solves for the following equation where, once again, we do not take into account accrued premium or up-front payments effects

$$p_{t,T} \times \sum_{T_k > T} E\left[\left(\exp - \int_t^{T_k} (r+\lambda)(u) \, \mathrm{d}u\right) | \Im_t\right]$$
  
$$= \int_T^{T_N} E\left[\left(\exp - \int_t^s (r+\lambda)(u) \, \mathrm{d}u\right) \times (1-\delta)\lambda(s) | \Im_t\right] \mathrm{d}s \tag{5}$$

Prior to default, the left-hand term corresponds to the value at time  $t$  of the premium leg of the underlying forward default swap, while the righthand term is associated with the default leg. Clearly  $p_{t,T}$  is  $\Im_t$ -measurable and we can prove that it is both a  $(\Im, \hat{Q})$  and a  $(G, \hat{Q})$  martingale. Thus, the forward default swap premium shares the properties of a "true" price. It can be checked that  $p_{T,T}$  $p_T$ .

Using an extended version of Girsanov theorem (see Equivalence of Probability Measures) for point processes (see Point Processes), it can be shown that

$$\frac{\mathrm{d}p_{t,T}}{p_{t,T}} = \sigma \mathrm{d}\hat{W}_t \tag{6}$$

where  $\hat{W}$  is a  $(\Im, \hat{Q})$  Brownian motion.

Let us also assume that there exists some specification of r and  $\lambda$  such that the volatility  $\sigma$  is constant. Then, the forward CDS spread has a lognormal dynamics under  $\hat{O}$ . This readily leads to the already stated Black formula for the price of the CDS option. The most obvious advantage is the simplicity of the outcome. The drawbacks are also rather obvious. The lognormal assumption for the forward spreads is questionable since jumps are often included in the dynamics of  $\lambda$  as in the affine specification within  $[5]$ .

The intensity approach is easy to understand and is consistent across strikes, maturity of the option, and maturity of the CDS. However, it entails dealing with extra parameters and is numerically more involved. In the more general setting involving correlation between *r* and *λ*, Monte Carlo simulation is usually required. In special cases, such as deterministic default-free rates, analytical formulas can be derived. Fortunately enough, in most examples, the correlation parameter has little impact on option prices and analytical approximations of the implied volatility in the Black formula can be derived. Let us remark that in these approximations *σ* depends on the exercise date and the maturity of the underlying CDS.

# **Acknowledgments**

The author thanks A. Cousin, L. Cousot, A. Godet and C. Pedersen and the editors for helpful remarks. The usual disclaimer applies.

# **References**

- [1] Bielecki, T.R. & Rutkowski, M. (2002). *Credit Risk: Modeling, Valuation and Hedging*, Springer.
- [2] Brigo, D. & Alfonsi, A. (2005). Credit default swap calibration and derivatives pricing with the SSRD stochastic intensity model, *Finance and Stochastics* **9**(1), 29–42.
- [3] Brigo, D. & Cousot, L. (2006). The stochastic intensity SSRD implied volatility patterns for credit default

swap options and the impact of correlation, *International Journal of Theoretical and Applied Finance* **9**(3), 315–339.

- [4] Brigo, D. & Matteotti, C. (2005). *Candidate Market Models and the Calibrated CIR*++ *Stochastic Intensity Model for Credit Default Swap Options and Callable Floaters*. Working paper, Credit Models, Banca IMI.
- [5] Duffie, D. & Garleanu, N. (2001). Risk and valuation ˆ of collateralized debt obligations, *Financial Analysts Journal* **57**(1), 41–59.
- [6] Hull, J. & White, A. (2003). The valuation of credit default swap options, *Journal of Derivatives* **10**(3), 40–50.
- [7] Jamshidian, F. (2004). Valuation of credit default swaps and swaptions, *Finance and Stochastics* **8**(3), 343–371.
- [8] Jeanblanc, M. & Rutkowski, M. (2000). Modelling of default risk: an overview, in *Mathematical Finance: Theory and Practice*, J. Yong & R. Cont, eds, Higher Education Press, Beijing. pp. 171–269.
- [9] Schonbucher, P.J. (2000). ¨ *A Libor Market Model with Default Risk*. Working paper, University of Bonn.
- [10] Schonbucher, P.J. (2003). ¨ *A Note on Survival Measures and the Pricing of Options on Credit Default Swaps*. Working paper, ETH Zurich.

# **Related Articles**

**Change of Numeraire**; **Compensators**; **Cox–Ingersoll–Ross (CIR) Model**; **Credit Default Swap Index Options**; **Credit Default Swaps**; **Filtrations**; **Point Processes**.

JEAN–PAUL LAURENT
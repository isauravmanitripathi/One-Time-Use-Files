## **Duffie-Singleton Model**

The credit risk modeling approach of Duffie and Singleton [8, 9] falls into the class of reducedform (see Reduced Form Credit Risk Models: Intensity-based Credit Risk Models) or intensitybased models in the sense that default is directly modeled as being triggered by a point process, as opposed to structural models (see Structural Default Risk Models) attempting to explain default through the dynamics of the firm's capital structure, and the intensity of this process under a risk-neutral probability measure is related to an appropriately defined instantaneous credit spread. In its original construction, it is set out as an econometric model, that is, a model the parameters of which are estimated from the time series of market data, such as the weekly data of swap yields used in [8]. To this end, the model is driven by a set of state variables following a Markov process under the risk-neutral measure, and defaultable zero-coupon bond prices are exponentially affine functions of the state variables along the lines of the results derived by Duffie and Kan [6] for default-free models of the term structure of interest rates (see Affine Models). Duffie and Singleton [9] show that the model framework can be made specific in a way that also allows default intensities and default-free interest rates to be negatively correlated in a manner that is more consistent theoretically than in prior attempts in the literature.

A key assumption of Duffie-Singleton is the modeling of recovery in the event of default as an exogenously given fraction of the market value of the defaultable claim immediately prior to default. Under this assumption, the possibility of default on a claim can be priced by default-adjusting the interest rate with which the future cash flow (or payoff) from the claim is discounted. That is to say that today's  $(t = 0)$ value  $V_0$  of a claim with the (possibly random) payoff X at time  $t = T$  can be calculated as the expectation under the spot risk-neutral measure  $O$ ,

$$V_0 = E_0^{\mathcal{Q}} \left[ \exp \left\{ -\int_0^T R_t \mathrm{d}t \right\} X \right] \tag{1}$$

where the discounting is given in terms of the defaultadjusted short-rate process  $R_t = r_t + h_t L_t$ , with  $r_t$ the default-free continuously compounded short rate,  $h_t$  the default hazard rate, and  $L_t$  the fraction of market value lost in the event of default.  $\lambda_t = h_t L_t$ can be interpreted as a "risk-neutral mean-loss rate of the instrument due to default." As a consequence, credit spread data alone (be it corporate bond yields, swap to treasury spreads, or credit default swap spreads) are insufficient to separate the "risk-neutral mean-loss rate"  $\lambda_t$  into its hazard rate  $h_t$  and loss fraction  $L_t$ .

The representation (1) lends the model considerable tractability, particularly for applications that do not require the separation of  $R_t$  into its components  $r_t$ ,  $h_t$ , and  $L_t$ , since  $R_t$  could then be modeled directly as a function  $\rho(Y_t)$  of a state variable process Y that is Markovian under  $Q$ . If the payoff of the claim is also Markovian in Y, say  $X = g(Y_T)$ , then the value of the claim at any time  $t$  (assuming that default has not occurred by time  $t$ ) can be written as the conditional expectation

$$V_t = E^{\mathcal{Q}} \left[ \exp \left\{ - \int_t^T \rho(Y_s) \, \mathrm{d}s \right\} g(Y_T) \middle| \, Y_t \right] \quad (2)$$

 $\rho(Y_s)$  can be modeled analogously to any one of a number of tractable default-free interest rate term structure models. One possible choice of making the Markovian model specific is along the lines of a multifactor affine term structure model as studied by Dai and Singleton [3], in which  $r_t$  and  $\lambda_t$  are affine functions of the vector  $Y_t$ ,

$$r_{t} = \delta_{0} + \sum_{i=1}^{N} \delta_{i} Y_{t}^{(i)} = \delta_{0} + \delta_{Y}^{\top} Y_{t}$$
(3)

$$\lambda_{t} = \gamma_{0} + \sum_{i=1}^{N} \gamma_{i} Y_{t}^{(i)} = \gamma_{0} + \gamma_{Y}^{\top} Y_{t} \tag{4}$$

and  $Y_t$  follows an "affine diffusion"

$$dY_t = \mathcal{K}(\Theta - Y_t) dt + \Sigma \sqrt{S(t)} dW(t) \qquad (5)$$

where  $W$  is an  $N$ -dimensional standard Brownian motion under  $Q$ ,  $\mathcal{K}$  and  $\Sigma$  are  $N \times N$  matrices (which may, in general, be nondiagonal and asymmetric), and  $S(t)$  is a diagonal matrix with the *i*th diagonal element given by

$$[S(t)]_{ii} = \alpha_i + \beta_i^\top Y_t \tag{6}$$

If certain admissibility conditions on the model parameters are satisfied [3], it follows from [6] that default-free and defaultable zero-coupon bond prices are exponential affine functions of the state variables.

Duffie and Singleton [9] highlight that modeling  $Y$  as a vector of independent components following [2] "square-root diffusions" constrains the joint conditional distribution of  $r_t$  and  $\lambda_t$  in a manner inconsistent with empirical findings. In particular, the [3] conditions on admissible model parameters imply that such a model cannot produce negative correlation between the default-free interest rate and the default hazard rate. Duffie-Singleton instead propose to use a more flexible specification, which does not suffer from this disadvantage. In its three-factor form, it is given by

$$\begin{aligned}\n\alpha &= \begin{pmatrix} 0 \\ 0 \\ \beta_3 \end{pmatrix} \quad \beta_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad \beta_2 = \begin{pmatrix} 0 \\ \beta_{22} \\ 0 \end{pmatrix} \\
\beta_3 &= \begin{pmatrix} \beta_{31} \\ \beta_{32} \\ 0 \end{pmatrix} \quad \delta_Y = \begin{pmatrix} \delta_1 \\ 1 \\ 1 \end{pmatrix} \quad \gamma_Y = \begin{pmatrix} \gamma \\ \gamma \\ 0 \end{pmatrix} \quad (7)\n\end{aligned}$$

with all coefficients (including  $\delta_0$  and  $\gamma_0$  in equations (3) and (4)) strictly positive. Furthermore,

$$\mathcal{K} = \begin{bmatrix} \kappa_{11} & \kappa_{12} & 0 \\ \kappa_{21} & \kappa_{22} & 0 \\ 0 & 0 & \kappa_{33} \end{bmatrix} \quad \Sigma = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \sigma_{31} & \sigma_{32} & 1 \end{bmatrix} \tag{8}$$

with the off-diagonal elements of  $\mathcal{K}$  being nonpositive. This specification ensures strictly positive credit spreads  $\lambda_t$  and can represent negative correlation between the increments of  $r$  and  $\lambda$ .

The "recovery-of-market-value" assumption at the core of the Duffie-Singleton framework is in line with market practice for defaultable derivative financial instruments such as swaps. For defaultable bonds, it is arguably more realistic to model the loss in the event of default as a fraction of the par value. However, Duffie and Singleton [9] provide evidence that par yield spreads implied by reduced-form models are relatively robust with respect to different recovery assumptions, and suggest that for bonds trading substantially away from par, pricing differences due to different recovery assumptions can be largely compensated by changes in the recovery parameters. The computational tractability gained through the "recovery-of-market-value" assumption may thus justify accepting its slight inconsistency with legal and market practice.

The parallels of equation  $(1)$  to the valuation of contingent claims in default-free interest rate term structure models also extend to the methodology of Heath et al. [10] (HJM). Defining a term structure of "defaultable instantaneous forward rates"  $\bar{f}(t, T)$  in terms of defaultable zero-coupon bond prices  $\bar{B}(t,T)$ (i.e., the time  $t$  price of a bond maturing in  $T$ ) by

$$\bar{B}(t,T) = \exp\left\{-\int_{t}^{T} \bar{f}(t,u) \, \mathrm{d}u\right\} \tag{9}$$

the model can be written in terms of the dynamics of the  $\bar{f}(t, T)$ , the drift of which under the riskneutral measure must obey the no-arbitrage restrictions, derived by Heath, Jarrow, and Morton (HJM) in the default-free case. Note that the  $\bar{f}$  are "forward rates" only in the sense that equation  $(9)$  is analogous to the definition of instantaneous forward rates in the default-free case and their relationship to forward bond prices is less straightforward than for defaultfree forward rates. That is to say that typically for the forward price  $\bar{F}(t, T_1, T_2) = \bar{B}(t, T_2)/B(t, T_1)$ (where  $B(t, T)$  is a default-free zero-coupon bond), one has

$$\bar{F}(t, T_1, T_2) \neq \frac{\bar{B}(t, T_2)}{\bar{B}(t, T_1)} = \exp\left\{-\int_{T_1}^{T_2} \bar{f}(t, u) \, \mathrm{d}u\right\} \tag{10}$$

For the continuously compounded defaultable short rate  $\bar{r}(t) = \bar{f}(t, t)$ , the no-arbitrage restrictions imply

$$\bar{f}(t,t) = r_t + h_t L_t = R_t \tag{11}$$

which is equal to the default-adjusted short rate given in equation (1). In this sense, the risk-neutral meanloss rate  $h_t L_t$  is equal to the instantaneous credit spread  $\bar{r}(t) - r_t$ .

Cast in terms of HJM, the model is automatically calibrated to an initial term structure of defaultable discount factors  $\bar{B}(t, T)$ . This type of straightforward "cross-sectional" calibration makes the model useful not only for the econometric estimation followed by Duffie and Singleton [8] and others such as Duffee [4] and Collin-Dufresne and Solnik [1] but also for the relative pricing of credit derivatives.

The model can be extended in a number of directions, several of which are discussed in [9]. "Liquidity" effects can be modeled by defining a fractional carrying cost of defaultable instruments, in which case the relevant discount rate *Rt* = *rt* + *htLt* + *t* is adjusted for default and liquidity. The assumption of exogenous default intensity and recovery rate can be lifted, as in [5], by allowing intensities/recovery rates to differ for the counterparties in an overthe-counter (OTC) derivative transaction, with the intensity/recovery rate relevant for discounting determined by which counterparty is in the money. Jumps in the default-adjusted rate can be introduced along the lines of [6] while preserving the tractability of an affine term structure model. The model of singleobligor default considered by Duffie and Singleton [8, 9] can also be extended to the portfolio level using the copula function approach of Schonbucher ¨ and Schubert [11], since introducing default correlation through correlated diffusive dynamics of the default intensities *ht* for different obligors is typically insufficient, resulting only in very mild correlation of defaults.

Historically, reduced-form models like Duffie– Singleton have been considered to be following a different paradigm than the more fundamental structural models where default is triggered when the value of the firm falls below a barrier taken to represent the firm's liabilities. However, the two approaches have been reconciled by Duffie and Lando [7], who show that models based on a default intensity can be underpinned by a structural model in which bondholders are imperfectly informed about the firm's value.

## **References**

[1] Collin-Dufresne, P. & Solnik, B. (2001). On the term structure of default premia in the swap and LIBOR markets, *Journal of Finance* **56**(3), 1095–1115.

- [2] Cox, J.C., Ingersoll, J.E. & Ross, S.A. (1985). A theory of the term structure of interest rates, *Econometrica* **53**(2), 385–407.
- [3] Dai, Q. & Singleton, K.J. (2000). Specification analysis of affine term structure models, *The Journal of Finance* **55**(5), 1943–1978.
- [4] Duffee, G. (1999). Estimating the price of default risk, *Review of Financial Studies* **12**(1), 197–226.
- [5] Duffie, D. & Huang, M. (1996). Swap rates and credit quality, *Journal of Finance* **51**(3), 921–949.
- [6] Duffie, J.D. & Kan, R. (1996). A yield factor model of interest rates, *Mathematical Finance* **6**(4), 379–406.
- [7] Duffie, D. & Lando, D. (2001). Term structures of credit spreads with incomplete accounting information, *Econometrica* **69**(3), 633–664.
- [8] Duffie, D. & Singleton, K.J. (1997). An econometric model of the term structure of interest-rate swap yields, *The Journal of Finance* **52**(4), 1287–1322.
- [9] Duffie, D. & Singleton, K. (1999). Modeling term structures of defaultable bonds, *Review of Financial Studies* **12**, 687–720.
- [10] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**(1), 77–105.
- [11] Schonbucher, P. & Schubert, D. (2001). ¨ *Copula Dependent Default Risk in Intensity Models*, University of Bonn. Working paper.

## **Related Articles**

**Affine Models**; **Constant Maturity Credit Default Swap**; **Intensity-based Credit Risk Models**; **Jarrow–Lando–Turnbull Model**; **Markov Processes**; **Multiname Reduced Form Models**; **Point Processes**; **Reduced Form Credit Risk Models**.

ERIK SCHLOGL ¨ & LUTZ SCHLOGL ¨
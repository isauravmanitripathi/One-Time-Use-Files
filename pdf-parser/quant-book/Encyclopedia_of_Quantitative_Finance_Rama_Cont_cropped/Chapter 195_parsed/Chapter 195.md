# **Hazard Rate**

Consider a credit default swap (CDS) (see Credit **Default Swaps**), where the premium payments are periodic and the terminal payment is a digital cash settlement of recovery rate  $1 - \bar{\ell}$ . For simplicity, we assume that the current time is normalized to  $t = 0$ , the risk-free rate  $r$  is constant throughout the maturity of the contract, and spreads are already given at standard interperiod rates (allowing us to ignore daycount fractions and division by period length). The cash flows of a CDS can be decomposed into the default leg and the premium leg. The default leg is a single lump sum compensation for the loss  $\bar{\ell}$  on the face value of the reference asset made at the default time by the protection seller to the protection buyer, given that the default is before the expiration date  $T$  of the contract. The premium leg consists of the fees, called the CDS spread, paid by the protection buyer at dates  $t_m$  (assumed to be equidistant e.g., quarterly) until the default event or  $T$ , whichever is first. The spread  $S$  is given as a fraction of the unit notional.

A concise mathematical expression for both legs can be obtained via a point process representation. Suppose we have a filtered probability space  $(\Omega, \mathscr{F}, \mathbb{F}, \mathbb{Q})$  satisfying the usual conditions. We model the default time as a random time  $\tau$  in  $[0, \infty]$ with an associated single jump point process

$$N_t = \mathbf{1}_{\{\tau \le t\}} = \begin{cases} 1 & \text{if } \tau \le t \\ 0 & \text{if } \tau > t \end{cases} \tag{1}$$

The default leg  $D_0$  and premium leg  $P_0(S)$  can now be expressed in terms of  $N$  as

$$D_0 = \mathbb{E}_0 \bigg[ \bar{\ell} \mathrm{e}^{-r\tau} N_\tau \bigg] = \mathbb{E}_0 \bigg[ \int_0^T \bar{\ell} \mathrm{e}^{-rs} \, \mathrm{d}N_s \bigg] \tag{2}$$
$$P_0(S) = \mathbb{E}_0 \bigg[ S \sum_{t_m} \mathrm{e}^{-rt_m} (1 - N_{t_m}) \bigg] \tag{3}$$

where  $\mathbb{E}_{t}[\cdot] = \mathbb{E}[\cdot|\mathscr{F}_{t}]$  is the conditional expectation with respect to time t, information  $\mathscr{F}_t$ , and the integral of equation (2) is defined in the Stieltjes sense. Finally, by an application of Fubini's theorem and integration by parts, equations  $(2)$  and  $(3)$  can be expressed as

$$D_0 = \bar{\ell} e^{-rT} \mathbb{Q}_0[\tau \le T] + \bar{\ell}r \int_0^T e^{-rs} \mathbb{Q}_0[\tau \le s] \, \mathrm{d}s \tag{4}$$

$$P_0(S) = S \sum_{t_m} e^{-rt_m} \mathbb{Q}_0[\tau > t_m]$$

$$\tag{5}$$

The fair spread is the spread  $S^*$  for which  $P_0(S^*) = D_0$ , making the value of the contract at initiation 0. This simple expositional formulation shows that the modeling of survival probabilities under the pricing measure of the form  $\mathbb{Q}_0[\tau > s]$  is the essence of CDS pricing. These quantities can be modeled in a unified way using the concept of *hazard rate*.

#### **Hazard Rate and Default Intensity**

Suppose that we have a filtered probability space  $(\Omega, \mathscr{F}, \mathbb{F}, \mathbb{Q})$  satisfying the usual conditions and that the default time of a firm is modeled by a random time  $\tau$ , where  $\mathbb{Q}[\tau = 0] = 0$  and  $\mathbb{Q}[\tau >$  $t] > 0$  for all  $t \in \mathbb{R}_+$ . We start under the assumption, which will be relaxed later, that the evolution of information only involves observations of whether or not default has occurred up to time  $t$ . In other words, we are dealing with the natural filtration  $\mathscr{F}_t = \mathscr{N}_t = \sigma(N_s, s \leq t)$  of the right continuous, increasing process  $N$ , introduced earlier, completed to include the  $\mathbb{Q}$ -negligible sets. Let  $F(t) = \mathbb{Q}[\tau <$ t] be the cumulative distribution function of  $\tau$ . Then, the *hazard function* of  $\tau$  is defined by the increasing function  $H: \mathbb{R}_+ \to \mathbb{R}_+$  given as

$$H(t) = -\ln(1 - F(t)) \quad \forall t \in \mathbb{R}_+ \tag{6}$$

Suppose, furthermore, that  $F$  is absolutely continuous, admitting a density representation of  $F(t)$  =  $\int_0^t f(s) ds$ . The *hazard rate* of  $\tau$  is defined by the nonnegative function  $h: \mathbb{R}_+ \to \mathbb{R}_+$  given as

$$h(t) = \frac{f(t)}{1 - F(t)}\tag{7}$$

under which we have

$$F(t) = 1 - e^{-H(t)} = 1 - e^{-\int_0^t h(s) ds} \quad \forall t \in \mathbb{R}_+ \tag{8}$$

Naturally, the component probabilities of equations  $(4)$  and  $(5)$  can be expressed in terms of the hazard rate as

$$\mathbb{Q}[\tau > s|\mathscr{N}_t]$$
  
=  $\mathbf{1}_{\{\tau > t\}} \mathbf{e}^{H(t) - H(s)} = \mathbf{1}_{\{\tau > t\}} \mathbf{e}^{-\int_t^s h(u) \, \mathrm{d}u}$  (9)  
$$\mathbb{Q}[t < \tau \le s|\mathscr{N}_t] = \mathbf{1}_{\{\tau > t\}} \left(1 - \mathbf{e}^{H(t) - H(s)}\right)$$

$$= \mathbf{1}_{\{\tau > t\}} \left( 1 - e^{-\int_t^s h(u) \, du} \right) \tag{10}$$

where  $s \geq t$ . Note that for a continuous  $h$ ,  $h(t)\Delta$ represents the first-order approximation of the probability of default between t and  $t + \Delta$ , given survival up to  $t$ . The term *hazard rate* stems from the fact that  $h(t)$  can be thought of as the instantaneous  $(\Delta \rightarrow 0)$  rate of failure (in our case default arrival) at time  $t$  conditional on survival up to time  $t$ . Because of this conceptualization, the hazard rate is often referred to as the *forward default rate* in financial literature. While the term *default intensity* is also frequently used interchangeably with *hazard rate* [3], some authors [5] elect to distinguish between the two terms, where *intensity* is used to refer to the arrival rate conditioned on all observable information, and not only on survival. If survival is the only observable information, as in our current setting, the two terms are equivalent even under this distinction.

A useful alternate characterization of the hazard rate is possible using the martingale theory of point processes highlighted in [2]. As an increasing process,  $N$  has an obvious upward trend. The conditional probability of default by time  $s \ge t$  is always greater than or equal to  $N_t$  itself, and hence  $N$  is a submartingale. It follows that  $N$  admits the Doob–Meyer decomposition [4]  $N = M + A$ , where M is an  $\mathbb{F}$ -martingale and A is a right-continuous,  $\mathbb{F}$ predictable, increasing process starting from 0, both unique up to indistinguishability.  $A$  compensates for the upward trend such that  $N - A$  is an  $\mathbb{F}$ -martingale, and hence the popular terminology ( $\mathbb{F}$ -)compensator (see Compensators). Compensators are interesting constructs in and of themselves, as their analytical properties correspond to probabilistic properties of the underlying random time. For instance, the almost sure continuity of sample paths of  $A$  is equivalent to the total inaccessibility of  $\tau$ . Giesecke [6] outlines these properties and provides a direct compensator-based pricing application. As shown in [7], the connection between the compensator  $A$  and the hazard function H is that  $A(t) = H(t \wedge \tau)$ , if and

only if the cumulative distribution function  $F(t)$  is continuous. Furthermore, if  $F(t)$  is absolutely continuous we have  $A(t) = \int_0^{t \wedge \tau} h(s) \, \text{d}s$ , where h is the hazard rate. Therefore, under the continuity (absolute continuity) of  $F(t)$ , we can say that the hazard function  $H$  (hazard rate  $h$ ) is the unique function such that  $N(t) - H(t \wedge \tau) \left(= N(t) - \int_0^{t \wedge \tau} h(s) \, \mathrm{d}s \right)$  is an F-martingale. However, the martingale/compensator characterization and the standard hazard function definition no longer coincide when  $F(t)$  is not continuous.

In financial literature, we are also interested in cases where the current information filtration models not only survival but the observation of other processes as well. Let the total flow of information be modeled by  $\mathbb{F} = \mathbb{N} \vee \mathbb{G}$ , where  $\mathbb{N}$  is once again the natural filtration of  $N$  (and all filtrations considered are right-continuous completions). Under certain conditions the previous concepts can be extended in a straightforward fashion. Let  $F(t) =$  $\mathbb{Q}[\tau \leq t|\mathscr{G}_t]$ . First, we assume that  $\tau$  is not a  $\mathbb{G}$ -stopping time (while it is trivially an  $\mathbb{F}$ -stopping time) such that the G- hazard process  $H(t) =$  $-\ln(1-F(t))$  is well-defined. If H is absolutely continuous, admitting the G-progressive density representation  $H(t) = \int_0^t h(s) \, ds$ , then the process

$$M(t) := N(t) - H(t \wedge \tau) = N(t) - \int_0^{t \wedge \tau} h(s) \,\mathrm{d}s \tag{11}$$

is an  $\mathbb{F}$ -martingale, and the analogs of equations (9) and  $(10)$  are given by

$$\begin{split} \mathbb{Q}[\tau > s|\mathscr{F}_{t}] &= \mathbf{1}_{\{\tau > t\}} \mathbb{E}\left[\mathrm{e}^{H(t) - H(s)}|\mathscr{G}_{t}\right] \\ &= \mathbf{1}_{\{\tau > t\}} \mathbb{E}\left[\mathrm{e}^{-\int_{t}^{s} h(u) \, \mathrm{d}u} |\mathscr{G}_{t}\right] \quad (12) \\ \mathbb{Q}[t < \tau \leq s|\mathscr{F}_{t}] &= \mathbf{1}_{\{\tau > t\}} \mathbb{E}\left[1 - \mathrm{e}^{H(t) - H(s)} |\mathscr{G}_{t}\right] \\ &= \mathbf{1}_{\{\tau > t\}} \mathbb{E}\left[1 - \mathrm{e}^{-\int_{t}^{s} h(u) \, \mathrm{d}u} |\mathscr{G}_{t}\right] \quad (13) \end{split}$$

In this setting,  $h$  is deemed the  $G$ -intensity or  $G$ *hazard rate*. Even, in the case where  $\tau$  is a  $\mathbb{G}$ -stopping time ( $\mathbb{D} \subset \mathbb{G}$ ) and thus the  $\mathbb{G}$ -hazard function is not well defined, similar results can be obtained under certain conditions. Under certain restrictions on the

distributional properties of  $\tau$ , we can still use point process martingale theory (see Point Processes) to find an increasing  $\mathbb{F}$ -predictable process  $\Lambda$  for which the conditional survival probabilities are given by

$$\mathbb{Q}[\tau > s|\mathscr{F}_t] = \mathbf{1}_{\{\tau > t\}} \mathbb{E}\left[e^{\Lambda(t) - \Lambda(s)}|\mathscr{G}_t\right] \qquad (14)$$

Routinely, if  $\Lambda$  is absolutely continuous then,  $\Lambda(t) - \Lambda(s)$  in equation (14) can be replaced by its density representation  $-\int_{t}^{s} \lambda(u) \, \mathrm{d}u$ . The details of such conditions and results, as well as a general theory of hazard processes, are summarized in  $[1, 7]$ .

## **Reduced-form Modeling and Other Issues**

The importance of the concept of hazard rates (or intensities) lies in the fact that their direct modeling and parametrization is the prevalent industry practice in evaluating credit derivatives. Now that the CDS market has grown to one of great volume and liquidity, the realm of CDS spread modeling has become less of a pricing issue and more of a calibration one. Reduced-form modeling (see Intensity-based Credit Risk Models) refers to valuation methods in which one exogenously specifies the dynamics of an intensity model, much like we would for spot rates, and then calibrates the model parameters to fit the market spread data via a pricing formulation such as equations  $(4)$ – $(5)$ . A full-fledged model could incorporate features such as premium accrual, dependence of intensity with stochastic spot rates and the loss rate, and interaction/contagion effects with other names, which were ignored in our expositional formulation.

The assumptions, the underlying informational assumptions in particular, implied by the mere existence of a hazard rate are a nontrivial issue. Not all models admit an intensity process in their given information filtrations. For instance, in the classical first passage structural model under perfect information (see Default Barrier Models) the forward default rate (hazard rate with survival information only) exists, but the intensity process (hazard rate with all available information i.e. the firm value process) does not. Conceptually, the existence of a positive instantaneous default arrival rate implies a certain imperfection in the observable information, modeled either explicitly through a noisy filtration or implicitly through a totally inaccessible stopping time in the complete filtration. This underlines one of

the many issues surrounding the divergence of opinions and efforts for convergence in the reduced-form versus structural literature. Duffie and Singleton [5, 8] both provide a comprehensive overview of different credit models, while Giesecke [6] specifically outlines the different informational assumptions and their implications in intensity formulations.

# References

- [1] Bielecki, T.R. & Rutkowski, M. (2001). Credit Risk: Modeling, Valuation and Hedging, Springer.
- [2] Bremaud, P. (1981). Point Processes and Oueues. Martingale Dynamics, Springer-Verlag.
- [3] Brigo, D. & Mercurio, F. (2007). Interest Rate Models -Thoery and Practice, With Smile, Inflation and Credit, 2nd Edition, Springer.
- [4] Dellacherie, C. & Meyer, P.A. (1982). Probabilities and Potential, North Holland, Amsterdam.
- Duffie, D. & Singleton, K. (2003). Credit Risk: Pric-[5] ing, Measurement and Management, Princeton University Press.
- [6] Giesecke, K. (2006). Default and information, *Journal of* Economic Dynamics and Control 30, 2281-2303.
- [7] Jeanblanc, M. & Rutkowski, M. (2000). Modelling of default risk: an overview, in *Mathematical Finance:* Theory and Practice, Higher Education Press, Beijing, pp.  $171 - 269.$
- [8] Lando, D. (2004). Credit Risk Modeling: Theory and Applications, Princeton University Press.

## **Further Reading**

- International Swaps and Derivatives Association (1997). Confirmation of OTC Credit Swap Transaction Single Reference Entity Non-Sovereign.
- International Swaps and Derivatives Association (2002). 2002 Master Agreement.
- Tavakoli, J. (2001). Credit Derivatives and Synthetic Structures, A Guide to Instruments and Structures, 2nd Edition, John Wiley & Sons.

### **Related Articles**

Compensators; Credit Default Swaps; Default Barrier Models; Duffie-Singleton Model; Intensity-based Credit Risk Models; Jarrow-Lando-Turnbull Model; Point Processes; Reduced Form Credit Risk Models.

JUNE HO KIM
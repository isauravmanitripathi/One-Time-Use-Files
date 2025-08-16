# **Basket Default Swaps**

Basket default derivatives or swaps are more sophisticated credit derivatives that are linked to several underlying credits. The standard product is an insurance contract that offers protection against the event of the kth default on a basket of  $n, n > k$ , underlying names. It is similar to a plain credit default swap (CDS) but the credit event to insure against is the event of the  $k$ th default, and it is not specified to a particular name in the basket. A premium, or spread,  $s$ is paid as an insurance fee until maturity or the event of kth default. We denote by  $s^{k\text{th}}$  the fair spread in a  $k$ th-to-default swap, that is, the spread making the value of this swap equal to zero at inception. For the basic product description, we refer, for example, to [2, 3, 12].

If the  $n$  underlying credits in the basket default swap are independent, the fair spread  $s^{1st}$  of a first-todefault swap (FtD) is expected to be close to the sum of the fair individual default swap spreads  $s_i$  over all underlying credits  $i = 1, \ldots, n$ . For exponential waiting times, this follows since the minimum of exponentially distributed waiting times has itself an exponential distribution with an intensity that equals the sum of the intensities of the individual waiting times. If, on the other hand, the underlying credits are in some sense "totally" dependent the first default will be the one with the worst spread; therefore  $s^{1\text{st}} = \max_i(s_i).$ 

For the exact determination of the fair spread of basket default swaps, multivariate modeling of the default times of the credits in the basket is necessary. This dependency modeling can be classified into three different approaches, which are also used in collateralized debt obligations (CDO)-modeling (see Collateralized Debt Obligations (CDO)):

- Copula approach (see Default Time Copulas;  $\bullet$ Gaussian Copula Model; Copulas: Estimation)
- Asset-value approach (see Structural Default Risk Models; also Merton, Robert C.)
- Reduced-form, spread-based approach (see Multiname Reduced Form Models; Hazard Rate: Intensity-based Credit Risk Models; Duffie-Singleton Model; Jarrow-Lando-Turnbull Model)

### **Modeling Approaches**

#### *Copula Approach*

As contingent payments are only triggered in case of default, copula modeling focuses on the multivariate distribution of default times.

The copula approach was first applied in this context in [13, 14]. The challenge is to specify a function  $C$  such that with given marginal distribution  $F_i$ , we have that

$$\text{Prob}\{\tau_1 \le t_1, \dots, \tau_n \le t_n\} = F(t_1, \dots, t_n)$$
$$= C(F_1(t_1), \dots, F_n(t_n))$$
(1)

Basically, the set of Copula functions coincides with the set of all multivariate distribution functions whose marginal distributions are uniform distributions on  $[0, 1]$ , since under certain regularity assumptions

$$C(u_1,\ldots,u_n) = F(F_1^{-1}(u_1),\ldots,F_n^{-1}(u_n)) \quad (2)$$

One of the most elementary copula functions is the normal copula (or Gauss copula), which is derived by this approach from the multivariate normal distribution (see Gaussian Copula Model). Clearly, there are various different copulas generating all kinds of dependencies, for example, in [3, 12]. The advantage of the normal copula, however, is that it relates to the one period version of certain asset-value models used in credit portfolio risk modeling. But note that since the asset-value approach can only model defaults up to a single time horizon  $T$ , the calibration between the two models can only be done for one fixed horizon. Dynamic extensions of this in the asset-value context are exit time models.

#### Asset-value Models

In asset-value models we are looking for stochastic processes  $(Y_t^i)$  called *ability-to-pay processes* and (nonstochastic) barriers  $K_i(t)$  such that the default time  $\tau_i$  for credit *i* can be modeled as the first hitting time of the barrier  $K_i(t)$  by the process  $(Y_i^i)$ :

$$\tau_i = \inf\{t \ge 0 : Y_t^i \le K_i(t)\}\tag{3}$$

First, successful models of this class are reached when  $Y^i$  are either Brownian motions with drift or time changed Brownian motions; see [9, 15], where also some numerical calibration results are shown. Exit times of more general stochastic processes, including stochastic volatility models, are applied to default modeling in [8].

#### Reduced-form Modeling

Here we start from the classical single-name CDS approach, where the default time is a double stochastic Poisson process (or Cox-process); see **Hazard** Rate; Multiname Reduced Form Models and [5, 6, 11]. In this approach, it is assumed that conditional on a realization of a path of the default intensity, the default time is distributed like the time of the first jump of a time-inhomogeneous Poisson process with this intensity. Typically, the dynamics of resulting credit spreads are closely tied to the dynamics of the default intensity in this approach.

The main challenge here is the incorporation of default dependence. One either has to model common jumps in the spread processes or applies the copula approach exogenously to the default times given from the spread and hazard rates [4, 17]. Recently, an even more reduced approach was developed [1, 7, 18, 19] in which the accumulated losses  $(L_t)_{t>0}$ are modeled directly as a stochastic process. The

most general construction (as e.g., in [7]) is to view  $L$  as an increasing cadlag pure Jump process with absolute continuous compensator  $v(\mathrm{d}t, \mathrm{d}x) =$  $g(t, dx)dt$ ; see, for example, [10] for the underlying stochastic analysis. This is particularly useful, if one considers options on the spread  $s^{k\text{th}}$  of a basket swap. Here, the modeling attempt is on  $L$  and the singlename modeling is not considered.

#### Pricing

In order to price basket default swaps, we need the distribution  $F_{(k:n)}(t)$  of the time  $\tau^{k\text{th}}$  of the kth default. The  $k$ th default time is, in fact, the order statistic  $\tau_{(k:n)}$ ,  $k \leq n$ , and, in general, we can derive the distribution of the  $k$ th order statistics from the multivariate distribution functions [3]. For pricing we also need the survival function:

$$S_{(k:n)}(t) = 1 - F_{(k:n)}(t) \tag{4}$$

The fair spread  $s^{k\text{th}}$  for maturity  $T_m$  is then given hv

$$s^{k\text{th}} \sum_{i=1}^{m} \Delta_i B(T_0, T_i) S_{(k:n)}(T_i)$$
  
= 
$$\sum_{i=1}^{n} (1 - REC_i) \int_{T_0}^{T_m} B(T_0, u) F_{(k:n)}^{k\text{th}=i}(\text{d}u) \tag{5}$$

![](_page_1_Figure_11.jpeg)

**Figure 1**  $k$ th-to-default spread versus correlation for a basket with three underlyings: (solid)  $s^{1st}$ , (dashed)  $s^{2nd}$ , (dashed-dotted)  $s^{3rd}$ 

The first part is the present value of the spread payments, which stops at  $\tau^{k\text{th}}$ . The second part is the present value of the payment at the time of the  $k$ th default. Since the recovery rates might be different for the  $n$  underlying names, we have to sum up over all names and weigh with the probability that the  $k$ th default happens around  $u$  and that the  $k$ th defaulted name is just  $i$  (we assume that there are no joint defaults at exactly the same time). So  $F_{(k:n)}^{k\text{th}=i}$  is the probability distribution of the  $k$ th order statistic of the default times and that  $k\text{th} = i$ . Figure 1 [3] shows the  $k$ th-to-default spreads for a basket of three underlyings with fair spreads  $s_1 = 0.009$ ,  $s_2 = 0.010$ , and  $s_3 = 0.011$ , and pairwise equal normal copula correlation on the x-axis. In [16], it was already observed that the sum of the  $k$ th-to-default swap spreads is greater than the sum of the individual spreads, that is,  $\sum_{k=1}^{n} s^{kth} > \sum_{i=1}^{n} s_i$ . Both sides insure exactly the same risk, so this discrepancy is due to a windfall effect of the first-to default swap. At the time of the first default, one stops paying the huge spread  $s^{1st}$  on the one side but on the plainvanilla side one stops just paying the spread  $s_i$  of the first defaulted obligor  $i$ .

## References

- [1] Bennani, N. (2005). The Forward Loss Model: A Dynamic Term Structure Approach for the Pricing of Portfolio Credit Derivatives. Working paper.
- [2] Bluhm, C., Overbeck, L. & Wagner, C. (2002). An Introduction to Credit Risk Modeling, CRC Press/Chapman & Hall.
- [3] Bluhm, C. & Overbeck, L. (2006). Structured Credit Portfolio Analysis, Baskets and CDOs, CRCpress/Chapman & Hall.
- [4] Duffie, D. & Gârleanu, N. (2001). Risk and valuation of collateralized debt obligations, Financial Analysts Journal 57, 41-59.
- [5] Duffie, D. & Singleton, K. (1998). Simulating Correlated Defaults. Working paper, Graduate School of Business, Stanford University.
- Duffie, D. & Singleton, K. (1999). Modeling term [6] structures of defaultable bonds, Review of Financial Studies 12, 687-720.
- Filipovic, D., Overbeck, L. & Schmidt, T. (2008). [7] Dynamic Term Structure of CDO-losses. Working Paper.

- Fougue, J.P., Wignall, B.C. & Zhou, X. (2008). Mod-[8] eling correlated defaults: first passage model under stochastic volatility, Journal of Computational Finance 11(3), 43-78.
- Hull, J. & White, A. (2001). Valuing credit default [9] swaps II: modeling default correlations, The Journal of Derivatives Spring, 12-21.
- [10] Jacod, J. & Shiryaev, A.N. (1987). Limit Theorems for Stochastic Processes, Springer.
- [11] Jarrow, R.A., Lando, D. & Turnbull, S.M. (1997). A Markov model for the term structure of credit risk spreads, Review of Financial Studies 10, 481-523.
- [12] Laurent, J. & Gregory, J. (2005). Basket default swaps, cdos and factor copulas, Journal of Risk 7,  $103 - 122$
- [13] Li, D.X. (1999). The valuation of basket credit derivatives,  $CreditMetrics^{TM}$  Monitor April, 34–50.
- [14] Li, D.X. (2000). On default correlation: a copula function approach, Journal of Fixed Income 6, 43-54.
- [15] Overbeck, L. & Schmidt, W. (2005). Modeling default dependence with threshold models, Journal of Derivatives  $12(4)$ , 10–19.
- [16] Schmidt, W. & Ward, I. (2002). Pricing default baskets, Risk 15(1), 111-114.
- [17] Schoenbucher, P. (2003). Credit Derivatives Pricing Models: Models, Pricing, Implementation, Wiley Finance.
- [18] Schönbucher, P. (2005). Portfolio Losses and the Term Structure of Loss Transition Rates: A New Methodology for the Pricing of Portfolio Credit Derivatives. Working naner.
- [19] Sidenius, J., Piterbarg, V. & Andersen, L. (2005). A New Framework for Dynamic Credit Portfolio Loss *Modelling*. Working paper.

#### Related Articles

Collateralized Debt Obligations (CDO); Copulas: **Estimation; Copulas in Insurance; Credit Default** Swaps; Credit Default Swap (CDS) Indices; **Default Time Copulas; Duffie-Singleton Model;** Gaussian Copula Model; Hazard Rate; Jarrow-Lando-Turnbull Model; Multiname Reduced Form Models; Intensity-based Credit Risk Models; Reduced Form Credit Risk Models; Structural **Default Risk Models.** 

LUDGER OVERBECK
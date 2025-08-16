# **Forward-starting CDO Tranche**

At the core of any CDO pricing model is a mechanism for generating dependent defaults. If a simple factor structure is used to join their marginal distributions, the default times of the underlying credits are independent conditionally on the realization of the common factor(s). This conditional independence of defaults is very useful because it allows one to use quasi-analytical algorithms to compute the term structure of expected tranche losses, which is the fundamental ingredient for the valuation of a synthetic CDO.

Because of their analytical tractability, conditionally independent models have become a standard in the synthetic CDO market. In the next section, we review the one-factor Gaussian-copula model, which has played a dominant role since the early days of single-tranche trading.

## **The Gaussian-copula Model**

In the one-factor Gaussian-copula framework, the dependence of the default times is Gaussian, and is therefore completely specified by their correlations. In this model, given a particular realization of a normally distributed common factor *Y* , the probability that the *j* th credit defaults by time *t* is equal to

$$\pi_{j,t}(Y) = N\left(\frac{D_{j,t} - \beta_j \cdot Y}{\sqrt{1 - \beta_j^2}}\right),\newline j = 1, 2, \dots M\tag{1}$$

where *N (.)* denotes the standard Gaussian distribution function, the vector {*βj* } determines the correlations of the default times, {*Dj,t*} are free parameters chosen to satisfy

$$p_{j,t} = \int_{Y} \pi_{j,t}(Y) \, \mathrm{d}N(Y) \tag{2}$$

and *pj,t* are the (unconditional) probabilities that name *j* defaults by time *t*. Importantly, for the CDO model to price the underlying credit default swap (CDS) correctly, *pj,t* must be backed out from the term structure of observable CDS spreads.

Given a realization of the Gaussian factor *Y* , the *M* individual credits are independent, and a simple recursive procedure [2] can then be employed to recover the conditional loss distribution of the underlying portfolio, as well as the loss distribution of any particular tranche of interest. Once we know how to compute the loss distribution of a tranche for a given realization of the common factor, it is straightforward to take a probability-weighted average across all possible realizations of *Y* and thus recover the unconditional loss distribution of the tranche.

Repeating this procedure for a grid of horizon dates and interpreting the expected percentage loss up to time *t* as a "cumulative default probability", we can price the tranche using exactly the same analytics that we would use for pricing a CDS. More precisely, we can define the "tranche curve" as the term structure of expected surviving percentage notionals of the tranche, that is,

$$Q(t) = 1 - E\left[\frac{[L_t - U]^+ - [L_t - (U + V)]^+}{V}\right]$$
(3)

where *Lt* is the number of loss units experienced by the reference portfolio by time *t,U* is the number of loss units that the tranche can withstand (attachment), and *V* is the number of loss units protected by the tranche investor. Then the two legs of the swap can be priced using

Premium = 
$$cN \sum_{i=1}^{T} \Delta_i Q(t_i) B(t_i)$$
 (4)

Protection = 
$$N \sum_{i=1}^{T} B(t_i) (Q(t_{i-1}) - Q(t_i))$$
 (5)

where *c* is the annual coupon paid on the tranche, *N* is the notional of the tranche, *ti*, *i* = 1*,* 2*,...,T* are the coupon dates, *i*, *i* = 1*,* 2*,...,T* are accrual factors, and *B(t)* is the risk-free discount factor for time *t*. Notice that, for ease of notation, we have used the coupon dates *ti*, *i* = 1*,* 2*,...,T* to discretize the timeline for the valuation of the protection leg.

## **Pricing of Reset Tranches**

Let us define a reset tranche as a path-dependent tranche whose attachment and/or width are reset *at* *a predetermined time (the reset date) as deterministic functions of the random amount of losses incurred by the reference portfolio up to that time*. Notice that forward-starting tranches and tranches whose attachment point resets at a future date both belong to this class.

#### *Pricing a Reset Tranche*

Let *ts* denote the reset date, *λj* , *j* = 1*,* 2*,...,M*, the number of loss units produced by the default of the *j* th name, *λ* = *λj* the maximum number of loss units that the portfolio can suffer, *p(ω)* the probability today that the reference portfolio incurs exactly *ω* loss units by the reset date *ts*.

A reset tranche can be defined by the vector {*tT , ts, U, V , U (ω), V (ω)*} where *U (ω)* ≥ *ω* is the attachment point of the tranche (in loss units) after the reset date, and *V (ω)* is the number of loss units protected by the tranche investor after the reset date. We can price the two legs of this swap as follows:

Premium

$$= cN \sum_{\omega=0}^{\lambda} p(\omega) \sum_{i=1}^{T} \Delta_i Q(t_i; \omega) B(t_i) \quad (6)$$

Protection

$$= N \sum_{\omega=0}^{\lambda} p(\omega) \sum_{i=1}^{T} B(t_i) (Q(t_{i-1}; \omega) - Q(t_i; \omega))$$
(7)

where we have defined the *conditional* tranche curve *Q(t*; *ω)*, *t*<sup>0</sup> ≤ *t* ≤ *tT* , as

In words, the conditional tranche curve *Q(t*; *ω)* represents the (risk-neutral) expected percentage surviving notional of the tranche at time *t*, conditional on the event that the reference portfolio experiences a cumulative loss of *ω* units up to the reset date.

Equally, we can write down the valuation in terms of the *unconditional* tranche curve

$$Q(t) = \sum_{\omega=0}^{\lambda} p(\omega) \cdot Q(t; \omega) \tag{9}$$

and thus obtain the familiar equations

$$\text{Premium} = cN \sum_{i=1}^{T} \Delta_i Q(t_i) B(t_i) \tag{10}$$

Protection = 
$$N \sum_{i=1}^{T} B(t_i)(Q(t_{i-1}) - Q(t_i))$$
 (11)

However, while the unconditional tranche curve for *t*<sup>0</sup> ≤ *t* ≤ *ts* reduces to the standard tranche curve defined in the section The Gaussian-copula Model,

$$Q(t) = \sum_{\omega=0}^{\lambda} p(\omega) \cdot Q(t; \omega) = 1 - \sum_{\omega=0}^{\lambda} p(\omega)$$
$$\times E\left[\frac{[L_t - U]^+ - [L_t - (U + V)]^+}{V} | L_{t_s} = \omega\right]$$
$$= 1 - E\left[\frac{[L_t - U]^+ - [L_t - (U + V)]^+}{V}\right]$$
(12)

$$Q(t;\omega) = T(t,\omega) \cdot \left(1 - E\left[\frac{\left[L_t - U(t;\omega)\right]^+ - \left[L_t - (U(t;\omega) + V(t;\omega))\right]^+}{V(t;\omega)} | L_{t_s} = \omega\right]\right),\,$$

$$T(t,\omega) = 1 - 1_{\{t > t_s\}} \frac{\left[\omega - U\right]^+ - \left[\omega - (U+V)\right]^+}{V},\,$$

$$U(t;\omega) = \begin{cases} U, t \le t_s\\ U(\omega), t > t_s \end{cases},\,$$

$$V(t;\omega) = \begin{cases} V, t \le t_s\\ V(\omega), t > t_s \end{cases},\,$$

$$(8)$$

the unconditional tranche curve for *ts < t* ≤ *tT*

$$Z_{v_1, v_2}^0 = 0 \text{ otherwise} \tag{15}$$

$$Q(t) = \sum_{\omega=0}^{\lambda} p(\omega) \cdot Q(t; \omega)$$
  
= 
$$\sum_{\omega=0}^{\lambda} p(\omega) \cdot T(t, \omega) \cdot \left(1 - E\left[\frac{[L_t - U(\omega)]^+ - [L_t - (U(\omega) + V(\omega))]^+}{V(\omega)} | L_{t_s} = \omega\right]\right) \tag{13}$$

incorporates the added complexity of the pathdependent valuation.

#### *Deriving the Conditional Tranche Curve*

Our discussion so far leaves open the problem of constructing the conditional tranche curve. From the previous discussion, it should be clear that to achieve this goal we need to be able to compute conditional expectations of the form *E f Ltu , ω* |*Lts* = *ω* for some function *f* . In this section, we present a twodimensional recursive algorithm for computing the joint distribution of cumulative losses at two different horizons, which in turn allows us to compute the conditional expectations that we need. The methodology is conceptually similar to the one introduced by Baheti *et al.* [3] for pricing "squared" products.

As anticipated, we assume that the underlying default model exhibits the property of conditional independence. We exploit this by conditioning our procedure on a particular realization of a common factor *Y* . We first discretize losses in the event of default by associating each credit with the number of loss units that its default would produce: we indicate by *λj* the integer number of loss units that would result from the default of name *j* . Next, we construct a square matrix *Zv*1*,v*<sup>2</sup> whose sides consist of all possible loss levels for the reference portfolio, that is, *(*0*,* 1*,...,λ)*. In this matrix, we store the joint probabilities that the reference portfolio incurs *v*<sup>1</sup> loss units up to time *ts* and *v*<sup>2</sup> loss units up to time *tu*, with *tu* ≥ *ts*. By definition of cumulative loss, the matrix must be upper triangular, that is,

$$Z_{v_1, v_2} = 0 \text{ if } v_2 < v_1 \tag{14}$$

For the nontrivial elements where *v*<sup>2</sup> ≥ *v*1, we set up the following recursion. We first initiate each state (recursion step *j* = 0) by setting

$$Z_{v_1,v_2}^0 = 1$$
, if  $v_1 = 0$  and  $v_2 = 0$ 

We preserve the notation adopted during our description of the Gaussian-copula model and denote by 
$$\pi_{j,t}(Y)$$
 the probability that name *j* defaults by time *t*, conditional on the market factor taking value *Y*. Now we feed one credit at a time into the recursion and update each element according to the following:

If *v*<sup>1</sup> ≥ *λj* , then

$$Z_{v_1, v_2}^j = (1 - \pi_{j,u}(Y)) \cdot Z_{v_1, v_2}^{j-1}$$
  
+  $\pi_{j,s}(Y) \cdot Z_{(v_1 - \lambda_j), (v_2 - \lambda_j)}^{j-1}$   
+  $(\pi_{j,u}(Y) - \pi_{j,s}(Y)) \cdot Z_{(v_1), (v_2 - \lambda_j)}^{j-1}$  (16)

If *v*<sup>2</sup> *< λj* , then

$$Z_{v_1, v_2}^j = (1 - \pi_{j,u}(Y)) \cdot Z_{v_1, v_2}^{j-1} \tag{17}$$

If *v*<sup>1</sup> *< λj* ≤ *v*2, then

$$Z_{v_1, v_2}^j = (1 - \pi_{j,u}(Y)) \cdot Z_{v_1, v_2}^{j-1}$$
  
+ 
$$(\pi_{j,u}(Y) - \pi_{j,s}(Y)) \cdot Z_{(v_1), (v_2 - \lambda_j)}^{j-1}$$
(18)

After including all the issuers, we set

$$\left(Z_{v_1,v_2}\right) = \left(Z_{v_1,v_2}^M\right) \tag{19}$$

The matrix *Zv*1*,v*<sup>2</sup> now holds the joint loss distribution of the reference portfolio at the two horizon dates *ts* and *tu*, conditional on the realization of the market factor *Y* , and we can numerically integrate over the common factor to recover the unconditional joint loss distribution. Using the joint distribution of losses at different horizons, it is then straightforward, for any function *f (.)*, to compute conditional expectations of the form *E f Ltu , ω* |*Lts* = *ω* , which is how we construct the conditional tranche curve.

## **Comments**

We have presented a simple methodology for quasianalytically pricing a class of default-path-dependent tranches. The proposed methodology is general in the sense that it can be easily applied to any model with conditionally independent defaults, including "implied copula" models fitted to liquidly traded tranches as in the Hull–White [4] model. The algorithm is useful because fast pricing of reset tranches allows one to obtain a variety of Greeks that are essential for effective risk management.

As observed by Andersen [1], however, some caution is necessary when pricing instruments whose valuation is sensitive to the joint distribution of cumulative losses at different horizons. Liquidly traded tranches only contain information about marginal loss distributions and tell us nothing about their dependence. Implying a default time copula from these prices, therefore, implicitly contains an arbitrary assumption about intertemporal dependencies, and it is easy to verify that different implied copulae that fit observable prices equally well may produce significantly different valuations for path-dependent instruments.

## **References**

- [1] Andersen, L. (2006). Portfolio losses in factor models: term structures and intertemporal loss dependence, *Journal of Credit Risk* **4**, 71–78.
- [2] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *Risk* November, 67–72.
- [3] Baheti, P., Mashal, R., Naldi, M. & Schloegl, L. (2005). Squaring factor copula models, *Risk* June, 73–76.
- [4] Hull, J. & White, A. (2006). *The Perfect Copula*. Working Paper, University of Toronto.

### PRASUN BAHETI, ROY MASHAL & MARCO NALDI
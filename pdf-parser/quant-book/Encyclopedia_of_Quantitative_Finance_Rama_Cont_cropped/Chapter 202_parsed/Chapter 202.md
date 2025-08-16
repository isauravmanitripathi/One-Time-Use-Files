# **Gaussian Copula Model**

Li [5] has introduced a copula function approach to credit portfolio modeling. In this approach, the author first introduces a random variable to denote the survival time for each credit and characterizes its properties using a density function or a hazard rate (*see* **Hazard Rate**). This allows us to move away from a one-period framework so that we could incorporate the term structure of default probabilities for each name in the portfolio. Then, the author introduces copula functions (*see* **Copulas: Estimation**) to combine information from all individual credits and further assumes a correlation structure among all credits. Mathematically, copula functions allow us to construct a joint distribution of survival times with given marginal distributions as specified by individual credit curves. This two-stage approach to forming a joint distribution of survival times has advantages. First, it incorporates all information on each individual credit. Second, we have more choices of different copula functions to form a good joint distribution to serve our purpose than if we assume a joint distribution of survival times from the start. While the normal copula function was used in [5] for illustration due to the simplicity of its economic interpretation of the correlation parameters and the relative ease of computation of its distribution function, the framework does allow use of other copula functions. We also discuss an efficient "one-step" simulation algorithm of survival times in the copula framework by exploring the mathematical property of copula functions in contrast to the period by period simulation as suggested earlier by others.

## **Default Information of a Single Name**

To price any basket credit derivative structure, we first need to build a credit curve for each single credit in the portfolio, and then we need to have a default correlation model so that we can link all individual credits in the portfolio.

A credit curve for a company is a series of default probabilities to future dates. Traditionally, we use rating agency's historical default experience to derive this information. From a relative value trading perspective, however, we rely more on market information from traded assets such as risky bond prices, asset swap spreads, or, nowadays, directly the singlename term structure of default swap spreads to derive market implied default probabilities. These probabilities are usually called *risk neutral default probabilities*, which, in general, are much higher than the historical default probabilities for the rating class to which this company belongs. Mathematically, we use the distribution function of survival time to describe these probabilities. If we denote *τ* as an individual credit's survival time which measures the length of time from today to the time of default, we use *F (t)* as the distribution function defined as follows:

$$F(t) = \Pr[\tau \le t] = 1 - S(t) \tag{1}$$

where *S(t)* is called the *survival probability* up to time *t*. The marginal probabilities of defaults such as the ones over one-year periods, or hazard rates in continuous term, are usually called a *credit curve*. In general, for single-name default swap pricing, only a credit curve is needed in the same way as an interest rate curve is needed to price an interest rate swap.

## **Correlating Defaults through Copula Functions**

Central to the valuation of the credit derivatives based on a credit portfolio is the default correlation. To put it in simple terms, default correlation measures the impact of one credit default on other credits. Intuitively, one would think of default correlation as being driven by some common macroeconomic factors. These factors tend to tie all industries into the common economic cycle, a sector-specific effect or a company-specific effect. From this angle, it is generally believed that default correlation is positive even between companies in different sectors. Within the same sector, we would expect companies to have an even higher default correlation since they have more commonalities. For example, overcapacity in the telecommunication industry after the internet/telecom bubble resulted in the default of numerous telecommunication and telephone companies. However, the sheer lack of default data means those assumptions are difficult to verify with any degree of certainty. Then we have to resort to an economic model to solve this problem.

From a mathematical point of view, we know the marginal distribution of survival time of each credit in the portfolio and we need to find a joint survival time distribution function such that the marginal distributions are the same as the credit curves of individual credits. This problem cannot be solved uniquely. There exist a number of ways to construct a joint distribution with known marginals. Copula functions, used in multivariate statistics, provide a convenient way to specify any joint distribution with given marginal distributions.

A copula function (*see* **Copulas: Estimation**) is simply a specification of how to use the univariate marginal distributions to form a multivariate distribution. For example, if we have *N*-correlated uniform random variables *U*1*, U*2*,...,UN* , then

$$C(u_1, u_2, \dots, u_N)$$
  
=  $\Pr\{U_1 < u_1, U_2 < u_2, \dots, U_N < u_N\}$  (2)

is the joint distribution function, which gives the probability that all of the uniforms are in the specified *N*-dimensional space cube. Using this joint distribution function *C* and *N* marginal distribution functions *Fi(ti)*, which describe *N* credit curves, we form another function as follows: *C*[*F*1*(t*1*), F*2*(t*2*), . . . , FN (tN )*]. It can be shown that this function is a distribution function for the *N*-dimensional random vector of survival times where, as desired, the marginal distributions are *F*1*(t*1*), F*2*(t*2*), . . . , FN (tN )*; see [5]. So a copula function is nothing more than a joint distribution of uniform random variables from which we can build a joint distribution with a set of given marginals.

Then we need to solve two problems. First, which copula function should we use? Second, how do we calibrate the parameters in a copula function? Suppose we study a credit portfolio of two credits over a given period. The marginal default probabilities are given by the two credit curves constructed using market information or historical information. From an economic perspective, a company defaults when its asset falls below its liability. However, in the relative value trading environment, we know the default probability from the credit curve constructed using market information such as default swap spreads, asset swap spreads, or risky bond prices. Assume that there exists a standardized "asset return" *X* and a critical value *x*, and when *X* ≤ *x* the company would default, that is,

$$\Pr[X_1 \le x_1] = \Phi(x_1) = q_1$$
  
$$\Pr[X_2 \le x_2] = \Phi(x_2) = q_2 \tag{3}$$

where  is the cumulative univariate standard normal distribution. We use *<sup>n</sup>* to denote the *n*-dimension cumulative normal distribution function. If we assume that the asset returns follow a bivariate normal distribution *-*<sup>2</sup>*(x, y, ρ)* with correlation coefficient *ρ*, the joint default probability is given by

$$\begin{aligned} \Pr[X_1 \le x_1, X_2 \le r_2] \\ &= \Pr[X_1 \le \Phi^{-1}(q_1), X_2 \le \Phi^{-1}(q_2)] \\ &= \Phi_2[\Phi^{-1}(q_1), \Phi^{-1}(q_2), \rho] \end{aligned} \tag{4}$$

This expression suggests that we can use a Gaussian copula function with asset return correlations as parameters.

The above argument need not be associated with a normal copula. Any other copula function would be still able to give us a joint survival time distribution while preserving the individual credit curves. We have to use extra conditions in order to choose an appropriate copula function. When we compare two copula functions, we need to control the marginal distribution-free correlation parameter such as the rank correlation.

This approach gives a very flexible framework based on which we can value many basket structures. It can be expressed in the following graph:

![](_page_1_Figure_12.jpeg)

We also present an efficient simulation algorithm here to implement our framework. To simulate correlated survival times, we introduce another sequence of random variables *X*1*, X*2*, . . . ., Xn* such that

$$X_i = \Phi^{-1}(F(\tau_i)) \tag{5}$$

where *-*<sup>−</sup><sup>1</sup>*(*·*)* is a one-dimensional standard normal inverse function. *X*1*, X*2*, . . . ., Xn* follow a joint normal distribution with a given correlation matrix . From this equation, we see that there is a one-to-one mapping between *Xi* and *τi*. Any problem associated with *τi* could be transformed into a problem associated with *Xi*, which follows a joint normal distribution. Then we could make use of an efficient calculation method of multivariate normal distribution function.

The correlation parameters, in the framework of our credit portfolio model, can be roughly interpreted as the asset return correlation. However, in most practical uses of the current model, we either set the correlation matrix using one constant number or two numbers as the inter- and intraindustrial correlation for trading models. We could either use an economic model to asset correlation or we can calibrate the parameters using traded instruments involving correlation such as first-to-default or collateralized debt obligation (CDO) tranches.

The commonly used one or two correlation parameters are strongly associated with factor models for asset returns. For example, the one correlation parameter *ρ* ≥ 0 corresponds to a one-factor asset return model where each asset return can be expressed as follows:

$$X_i = \sqrt{\rho} \cdot X_m + \sqrt{1 - \rho} \cdot X_i \tag{6}$$

where *Xm* represents the common factor return and *εi* is the idiosyncratic risk associated with credit asset *i*. Vasicek [7] and Finger [3] use this one-factor copula for portfolio loss calculation. For a detailed discussion on this one-factor copula model, the reader is referred to these two references.

If we use two parameters, the interindustrial correlation *ρo* and the intraindustry correlation *ρI* , then for each credit of industry group *k* = 1*,* 2*,...,K*, we can express the asset return as follows [6]:

$$X_i = \sqrt{\rho_I - \rho_o} \cdot X_k + \sqrt{\rho_o} \cdot X_m + X_i \tag{7}$$

Using these factor models, we can substantially reduce the dimensionality of the model. The number of independent factors then does not depend on the size of the portfolio. For example, for a portfolio whose credits belong to 10 industries, we just need to use 11 independent factors, one factor for each industry and one common factor for all credits. We could substantially improve the efficiency of our simulation or analytical approach once we exploit the property of the factor models embedded in the correlation structure. Some other orthogonal transformations such as the ones obtained by applying principal component analysis could also be used to reduce the dimension.

## **Loss Distribution**

For a given credit portfolio, the first information investors would like to know is its loss distribution over a given time horizon in the future such as 1 year or 5 years. This would give the investor some idea about the possible default loss of his investment in the next few years. The information we need to use in our framework is as follows: the credit curve of each credit that characterizes the default property over the time horizon, the recovery assumption, and the asset correlation structures. Many useful risk measurements, such as the expected loss, the unexpected loss, or the standard deviation of loss, the maximum loss, Value-at-Risk (VaR) or the conditional shortfall, could be obtained easily once the total loss distribution is calculated.

Here we study the property of the loss distribution using a numerical example. The base case used is as given in Table 1.

Figure 1 shows the excess loss distribution where the *x*-axis is the loss amount and *y*-axis is the probability of loss more than a given amount in the *x*-axis. All excess loss functions would start from 1 and gradually go to zero. If we include the zero loss in the probability calculation, then the probability of having nonnegative losses is always 1. We purposely exclude the zero loss in the calculation so that we can see the probability of having zero loss in the graph explicitly. Let us define the excess loss more precisely. Suppose that *L* represents the total loss of the portfolio, which is a random variable, since we do not know for sure what value it takes. For a given set of loss amounts *l*0*, l*1*,...,ln*, we can calculate the probability of excess loss *p*0*, p*1*,...,pn* as follows:

$$p_i = S(l_i) = \Pr[L > l_i] \tag{8}$$

The excess loss distribution essentially depicts *(li, pi)*. The reason we use excess loss distribution instead of loss distribution, which is defined as *F (li)* = 1 − *S(li)*, is mainly due to the fact that many interesting properties of the loss distribution can be viewed more explicitly from the excess loss distribution graph than from the ordinary loss distribution

**Table 1** Assumptions on a Credit Portfolio

| Number of Assets | 100     |
|------------------|---------|
| Credit spread    | 200 bps |
| Correlation      | 50%     |
| Maturity         | 5 years |
| Recovery         | 30%     |

![](_page_3_Figure_1.jpeg)

**Figure 1** Excess Loss Distribution

graph. For example, the expected loss using the density function *f (l)* of the loss distribution can be calculated as follows:

$$\mu_L = E(L) = \int_0^\infty l \cdot f(l) \mathrm{d}l = \int_0^\infty S(l) \mathrm{d}l \qquad (9)$$

which is just the area below the excess loss distribution line. Some other quantity such as the expected loss of tranched securities (loss with a deductible and a ceiling) could also be more simply expressed if we use excess loss function. We discuss this point in the next section when we discuss about CDO pricing.

Figure 1 shows the impact of correlation on the total excess loss distribution. From the graph we see that the probability of having zero loss increases from almost 0 to about 20% when correlation changes from 0 to 50%. The default probability over 5 years for each name is 1 − e<sup>−</sup>5·0*.*2*/(*1−30%*)* = 13*.*31%, and the probability of having no default of a portfolio with 100 independent names is *(*1 − 13*.*31%*)*100, practically 0. However, when the correlation is high, default occurs more in bulk, which makes the probability of having zero loss go up to 20%. When correlation is high, more loss would be pushed to the right, which makes the excess loss distribution tail much fatter since the expected total loss, the area below the excess loss function line, does not change along with the change in correlation. This can be shown using a credit VaR, which is defined as the excess loss, that probability of loss larger than this value is less than a given percentage such as 1%. The 1% credit VaR for various correlation values are given in Table 2.

In practice, it is very important to quickly obtain an accurate total excess loss distribution. There are a variety of methods that have been used for the total loss distribution. Here, we present the details on the recursive method in a one-factor Gaussian copula model and briefly summarize the conditional normal approximation approach.

**Table 2** Correlation vs C-VaR

| Correlation (%) | C-VaR |
|-----------------|-------|
| 0               | 14.7  |
| 10              | 25.2  |
| 20              | 32.9  |
| 50              | 53.9  |
| 75              | 67.2% |

We consider a credit portfolio consisting of  $n$ underlying credits whose notional amounts are  $N_i$ and fixed recovery rates are  $R_i$ ,  $i = 1, 2, \ldots, n$ . We consider the aggregate loss from today to time  $t$  as a fixed sum of random variables  $X_i$ :

$$L_n(t) = \sum_{i=1}^n l_i(t) = \sum_{i=1}^n (1 - R_i) \cdot N_i \cdot I_{(\tau_i < t)}$$
(10)

where  $\tau_i$  is the survival time for the *i*th credit in the credit portfolio and  $I$  is the indicator function, which is 1 in the case  $\tau_i < t$  and 0 otherwise. The distribution function of survival time  $c$  is denoted as  $F_i(t) = \Pr[\tau_i \leq t]$ . The specification of the survival time distribution  $F_i(t)$  is usually called a *credit curve*, which can be derived from market credit default swap spreads.

From the above equation, we can calculate the total loss distribution as

$$F_{L(t)}(x) = \Pr[L_n(t) \le x] = \Pr\left[\sum_{i=1}^n X_i \le x\right]$$
$$= \int \Pr\left[\sum_{i=1}^n X_i \le x | F\right] \cdot \mathrm{d}F \qquad (11)$$

Conditional on the common factor  $F$ , all  $X_i$  are independent, and then we just need to calculate the convolution of  $n$  independent random variables,  $c$ . As discussed in the last section, we know that  $X_i$ are independent conditional on the common factor  $X_M$  in the one-factor model. Each  $X_i$  can take only two discrete values with constant recovery rate assumption as follows: the loss would be 0 if default does not occur or  $B_i = (1 - R_i)N_i$  if default occurs.

$$f(x|F) = \begin{cases} 0, & 1 - q_i(t|F) \\ B_i, & q_i(t|F) \end{cases}$$
(12)

where  $q_i(t|F)$  is the conditional default probability for credit  $i$  before time  $t$ .

The density of the conditional total loss distribution can be calculated recursively over the partial sum  $L_i = L_{i-1} + X_i$ . We then have the following recursive formula:

This has been described in [4] and also in [1]. The unconditional total loss distribution is obtained by simply integrating the conditional loss distribution over the common factor  $F$ . In the simple case of one-factor Gaussian copula model, we use a Gaussian quadrature for the integration over the one common factor. In the one-parameter case, the conditional default probability can be calculated directly as follows:

$$q_{i}(t|X_{M}) = \Pr[\tau_{i} < t|X_{M}]$$
  
$$= \Pr[F_{i}^{-1}(N(X_{i})) < t|X_{M}]$$
  
$$= \Pr[X_{i} < N^{-1}(F(t))|X_{M}]$$
  
$$= N\left(\frac{N^{-1}(q_{i}(t)) - \rho \cdot X_{M}}{\sqrt{1 - \rho}}\right) \quad (14)$$

where  $q_i(t)$  is the unconditional default probability of credit  $i$  before time  $t$ .

Another approach uses the conditional normal approximation. Conditional on the common factors, all credits are independent. On the basis of the law of large numbers, the total conditional loss distribution can be approximated by a normal distribution. The mean and variance of this normal distribution can be simply calculated similarly as we do in the above one-factor case. More details are given as follows.

Conditioning on the common factor  $X_M$ , we can compute the mean and variance of the total loss variable,  $L|X_M$ ,

$$M_{v} = \sum_{i=1}^{n} N_{i} \cdot (1 - R_{i}) \cdot q_{i} \left( t | X_{M} \right)$$
$$\sigma_{v}^{2} = \sum_{i=1}^{n} N_{i}^{2} \cdot (1 - R_{i})^{2} \cdot q_{i} \left( t | X_{M} \right) (1 - q_{i} \left( t | X_{M} \right)) \tag{15}$$

The conditional normal approach uses normal distributions to approximate the conditional loss distribution. The normal distribution has the same mean and variance as computed above. In general, other distributions, such as inverse normal or Student- $t$ , can be used. The normal distribution is chosen because of the central limit theorem, which states that the

$$f_{L_j}(x|F) = \begin{cases} p_j \cdot f_{L_{j-1}}(x|F), & x < B_j \\ p_j \cdot f_{L_{j-1}}(x|F) + q_j \cdot f_{L_{j-1}}(x - B_j|F), & x \ge B_j \end{cases} \tag{13}$$

sum of independent distributions (but not identical distribution) approaches a normal distribution as the number of the independent distributions increases. In this case, the independent distributions are the distributions of the indicator functions of  $N_i \cdot (1 - R_i)$ .  $l_{\tau_i < t}$ , which are independent when conditioned on the common factor  $X_M$ .

Given the conditional normal approach, the conditional expected loss for a tranche with attachment and detachment  $K_L^T$  and  $K_U^T$  can be easily computed in closed form as follows:

$$E(L^{T}(t)|X_{M}) = (M_{v} - K_{L}^{T})\Phi\left(\frac{M_{v} - K_{L}^{T}}{\sigma_{v}}\right)$$
$$+ \sigma_{v} \cdot \phi\left(\frac{M_{v} - K_{L}^{T}}{\sigma_{v}}\right)$$
$$- (M_{v} - K_{U}^{T})\Phi\left(\frac{M_{v} - K_{U}^{T}}{\sigma_{v}}\right)$$
$$- \sigma_{v} \cdot \phi\left(\frac{M_{v} - K_{U}^{T}}{\sigma_{v}}\right) \qquad (16)$$

where  $\phi$  is the one-dimensional normal density function.

With the calculated conditional expected loss, the unconditional expected loss is obtained simply by integrating over the common factor  $X_M$ .

$$E(L^{T}(t)) = \int_{-\infty}^{+\infty} E(L^{T}(t)|y) \cdot \phi(y) \mathrm{d}y \qquad (17)$$

However, by choosing normal distribution in its approximation, the approach has its limitations. First, a normal variable can have a negative value with nozero probability. As we know, the loss in a portfolio should never be negative. However, this limitation only affects the equity tranche (the most junior tranche) and can be mitigated through the method described below. Second, as a loss is a summation of discrete loss variables, when a portfolio consists of only a few underlying names, then approximating the loss by a continuous variable (such as a normal variable) might not be a good approximation. This limitation also applies to some extreme case when the loss is dominated by only a few underlying names. In general, the conditional normal approach is a very good approximation when the number of names in a portfolio is larger than 30. Most of the CDO portfolios have the number of names larger than 30.

To mitigate the negative loss problem for an equity tranche one can use the following method, which preserves the expected loss of a CDO portfolio. An equity tranche  $[0, K_U^T]$  with detachment point  $K_U^T$  has payoff as follows:

$$L^{T}(t) = L(t) - \max[L(t) - K_{U}^{T}, 0]$$
 (18)

The conditional expected loss for the equity tranche is

$$E(L^{T}(t)|X_{M}) = M_{v} - (M_{v} - K_{U}^{T}) \cdot \Phi\left(\frac{M_{v} - K_{U}^{T}}{\sigma_{v}}\right)$$
$$- \sigma_{v} \cdot \phi\left(\frac{M_{v} - K_{U}^{T}}{\sigma_{v}}\right) \tag{19}$$

This has been proven to work well for index equity tranche of size more than 2%. Alternatively, we can also use inverse Gaussian distribution to approximate for the equity tranche since inverse Gaussian distribution takes only a positive value.

#### **Risk Measurement and Hedging**

Once a model and a mapping algorithm are chosen we can price all credit portfolio trades, and produce a series of risk measures based on the model. These risk measures are then used to form a hedging strategy for the trading book. The commonly used risk measures are as follows:

Credit spread delta: This is defined as the sensitivity of the mark-to-market value of a position to the instantaneous movement of the spread of a single entity, with all other parameters remaining constant. It is calculated through perturbation of the individual credit curves. Individual spread delta is reported as the change in value of the trade for a 1 basis point  $(1 \text{ bp})$  move in the indicated spread. Individual spread delta can be calculated as parallel moves in the individual curve (in which each spread on a particular curve is moved by 1 bp in a parallel fashion) or as bucketed moves in the curve. Individual spread delta is calculated trade-by-trade, and aggregated on the basis of issuer name, industry, or portfolio level. When we change the spread, we recalibrate the credit curve or instantaneous marginal default probability. Global spread delta is defined as the

change in the portfolio value change when all the underlying reference credit curves move by 1 bp. Global spread is calculated by bumping all spread curves of the underlying reference credits simultaneously in a parallel way or in buckets. Sometimes, we also study the sensitivities of our trade or book with respect to a large spread movement. Another common practice is to adjust the individual spread movement with respect to the index spreadsheet. The reason is that not all individual spread moves by the same amount when index moves. A statistical beta based on regression analysis is usually used.

- Single-name spread gamma: This is defined as the sensitivity of individual spread delta to a 1-bp move in a particular reference credit. As such, it represents the second-order price sensitivity with respect to a change in the spreads of the reference credit. Individual spread gamma is calculated by bumping one credit curve a time while all other credit curves remain the same for portfolio transactions. Global gamma is defined as the change in the global spread delta (which is defined as the portfolio value change when all the underlying reference credit curves move by 1 bp) of a portfolio for a 1-bp move in all reference credit spreads simultaneously. Global spread gamma is calculated by bumping all spread curves of the underlying reference credits simultaneously in a parallel way. Sometimes, we simply use a large spread movement as a measure of gamma risk by bumping the current spread by 50%. Similar to spread delta risk, we can also use bucket gamma risks which are more computationally challenging.
- Jump-to-default risk: We measure it by simply assuming one-name defaults right away or at a specific time in the future. We can also study the group jump-to-default risk.
- Time-decay risk: This measures the risk that as time passes, or maturity shortens, the value of portfolio transactions changes. For portfolio credit default swap, its survival time curve is most likely not flat, which makes the time decay an important risk factor.
- Correlation risk: Since we use a base correlation curve, we could measure the risk in terms of parallel change or bucket correlation change. In practice, we very often see a correlation curve twist, which reflects market changing perception

about different tranche risks. We can measure this risk by creating a sensitivity report for the whole book with respect to each base correlation point.

In practice, we tend to minimize spread and gamma risks, control jump-to-default risk, and also make correlation risk flat. We would also like to have positive carry: we receive more cash inflow than outflow. The hedging instruments we use are single name and index credit default swaps and index tranches. Very often, broker dealers tend to incur residual risks by using hedge ratios higher than the model-based amount to maintain a positive carry, but this strategy does not work well all the time, especially during turmoil, when there are unexpected defaults or jumps in spreads. We can use index tranche to hedge the base correlation risk. Sometimes, we can also use the index plus complementary tranches to hedge the correlation risk. In conclusion, for any hedging strategy, there will be a residual risk. Traders very often use their own view toward the market to selectively keep some residual risk.

In conclusion, the Gaussian copula function approach along with a base correlation method provides a simple and flexible framework to price basket credit derivatives. We further studied the framework and gained some more insights of it, especially from the conditional perspective of its correlation structure. This shows that the Gaussian copula function implies a too strong correlation structure. The reason for this is that we describe each credit using only two states: default or survival. This simple way of binary description creates too strong a conditional default property. It is also associated with the simple way of specifying the correlation structure using only one parameter or pairwise constant correlation, in practice, even though the original framework allows a completely flexible correlation matrix specification. Another possible reason is that this framework still misses certain fundamental driving factors such as volatilities of individual names in the framework.

We briefly discuss the risk measurement and risk management issues using the Gaussian copula function method. From the pricing formula, we can obtain all necessary risk measures, such as spread DV01, jump-to-default risk, and gamma risk of individual spreads or the general index. We can also obtain the sensitivities of the portfolio of portfolio transactions with respect to each point of base correlation curve. The hedging instruments we could use include single name and index CDS, and index tranche, or even options on single name and index. However, we need to bear in mind that hedging strategies lead to residual risks.

There is an urgent need to come up with alternative models. Many alternative methods and enhancements of the current ones have been suggested (*see* **Random Factor Loading Model (for Portfolio Credit)**; **Reduced Form Credit Risk Models**; **Structural Default Risk Models**; **Jarrow–Lando–Turnbull Model**; **Duffie–Singleton Model**; **Multiname Reduced Form Models**; **Intensity Gamma Model**). However, there is no market consensus on the pricing models for basic CDOs and *i*th-to-default transactions. The ultimate judge of a model should be its hedging performance. Extensive empirical studies on the performance of models from the hedging perspective need to be done comparing new models with the Gaussian copula plus the base correlation approach [2].

The current copula framework gained its popularity due to its simplicity. However, there is little economic justification for its framework. Its popularity in credit portfolio trading might match that of Black–Scholes formula for option valuation, but it lacks the theoretical background of the Black–Scholes formula. We essentially have a credit portfolio model without a solid credit portfolio theory. More theoretical studies are needed to make further advancement in this area besides various extensions and improvements, which attempt to fit the current market data.

## **References**

[1] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *Risk* November, 67–72.

- [2] Cont, R. & Kan, R. (2008). *Dynamic Hedging of Portfolio Credit Derivatives*. Columbia University Financial Engineering Report, 2008, http://ssrn.com/abstract=1349847
- [3] Finger, C. (1999). Conditional approaches for Creditmetrics portfolio distributions, *CreditMetrics Monitor* April, 14–33.
- [4] Klugman, S.A., Panjer, H.H. & Willmot, G.E. (1998). *Loss Distribution: From Data to Decisions*, John Wiley & Sons, Inc.
- [5] Li, D.X. (2000). On default correlation: a copula function approach, *Journal of Fixed Income* March, 41–50.
- [6] Li, D.X. & Skarabot, J. (2004). Pricing and hedging synthetic CDOs, a chapter in the book, in *Credit Derivatives: A Definitive Guide*, J. Gregory, ed., Risk Publications.
- [7] Vasicek, O. (2004). Probability of loss on loan portfolio (KMV Working Paper, 1987), in *Derivatives Pricing: The Classic Collection*, P. Carr, ed., Risk Books.

## **Further Reading**

Li, D. & Liang, M. (2005). *A Mixture Copula Function Approach to CDO and CDO Squared Pricing*.

## **Related Articles**

**Base Correlation**; **CDO Tranches: Impact on Economic Capital**; **Collateralized Debt Obligations (CDO)**; **Default Time Copulas**; **Duffie–Singleton Model**; **Intensity Gamma Model**; **Jarrow–Lando– Turnbull Model**; **Multiname Reduced Form Models**; **Random Factor Loading Model (for Portfolio Credit)**; **Reduced Form Credit Risk Models**; **Structural Default Risk Models**.

DAVID XIANGLIN LI
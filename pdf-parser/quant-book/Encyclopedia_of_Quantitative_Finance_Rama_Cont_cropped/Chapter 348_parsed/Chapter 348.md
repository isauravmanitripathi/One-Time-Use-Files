# **Econometrics of Option** Pricing

In 1997, Robert Merton and Myron Scholes were awarded the Nobel Memorial Prize in Economics "for a new method to determine the value of derivatives". Of course, Fisher Black, who died two years earlier, had been associated with this huge contribution to financial engineering, now known as the Black-Scholes (BS) model. The purpose of econometrics of option pricing, as sketched later, is not really to check the empirical validity of this model. It has been widely documented that, by contrast with maintained assumptions of Black and Scholes geometric Brownian motion model, stock returns exhibit both stochastic volatility and jumps. Thus, the interesting issue is not the validity of the model itself. In this article, we focus on the assessment of the possible errors of the BS option pricing formula and on empirically successful strategies to alleviate them. We can get the right pricing and hedging formula with a wrong model. The widespread acceptance of the BS option pricing formula as a benchmark, among academics and investment professionals, is undoubtedly due to its usefulness for pricing and hedging options, irrespective of the unrealistic assumptions of the initial model. This is the reason the largest part of this article is focused on econometric modeling and inference about empirically valid extensions of the BS option pricing formula.

However, it is worth stressing the general econometric content of arbitrage pricing. As first emphasized by Cox et al. [20], the message of the BS approach goes beyond any particular specification of the underlying stochastic processes. Arbitrage-free pricing models generally allow to interpret derivative prices as expectations of discounted payoffs, when expectations are computed with respect to an equivalent martingale measure. In this respect, a nice correspondence between the theory of arbitrage pricing and econometrics is worth noting. While option contracts are useful to complete the markets and so to get a unique equivalent martingale measure. While only the historical probability distribution can be estimated from return data on the underlying asset, option prices data allow the econometrician to perform some statistical inference about the relevant martingale measure. Econometric approaches based on implied volatility and also those used for option pricing that are unrelated to the lognormal benchmark of Black and Scholes, either because they are based on unrelated parametric models or because they introduce some nonparametric components, are discussed.

For sake of brevity, in this article, the only option contracts considered are European calls written on stocks. In the same manner, BS option pricing methodology has since been generalized to price many other derivative securities, and the econometric approaches sketched later can be extended accordingly.

### The Information Content of Option Prices

Assume that all stochastic processes of interest are adapted in a filtered probability space  $(\Omega, (\mathcal{F}_t), P)$ . Under some regularity conditions, the absence of arbitrage is equivalent to the existence of an equivalent martingale measure  $O$  (see **Equivalent** Martingale Measures). Without loss of generality, throughout we consider that the payoffs of options of interest are attainable [25]. Then, the arbitrage-free price of these options is defined, without ambiguity, as expectation under the probability measure  $Q$ of the discounted value of their payoff. Moreover, for a European call with maturity  $T$ , we characterize its arbitrage price at time  $t < T$  as the discounted value at time  $t$  of its expectation under the time  $t$ forward measure  $Q_{t,T}$  for time T. By Bayes rule,  $Q_{t,T}$  is straightforwardly defined as equivalent to the restriction of  $Q$  on  $\mathcal{F}_t$ . The density function  $dQ_{t,T}/dQ$  is  $[B(t,T)]^{-1}(B_t/B_T)$ , where  $B_t$  denotes the value at time t of a bank account, while  $B(t, T)$ is the time  $t$  price of a pure discount bond (with unit face value) maturing at time T. If  $K$  and  $S_t$ denote, respectively, the strike price and the price at time t of the underlying stock, the option price  $C_t$  at time  $t$  is

$$C_t = B(t, T)E^{Q_{t,T}} \text{Max}[0, S_T - K] \tag{1}$$

Such a formula (1) provides a decomposition of the option price into two components:

 $C_t = S_t \Delta_{1t} - K \Delta_{2t}$ 

where

(2)

$$\Delta_{2t} = B(t, T)Q_{t,T}[S_T \ge K] \tag{3}$$

and

$$\Delta_{1t} = \Delta_{2t} E^{Q_{t,T}} \left[ \frac{S_T}{S_t} \mid S_T \ge K \right] \tag{4}$$

It immediately follows (see [34], pp. 140, 169) that

$$\Delta_{2t} = -\frac{\partial \mathsf{C}_t}{\partial K} \tag{5}$$

In other words, a cross section at time  $t$  of European call option prices, all maturing at time  $T$  but with different strike prices  $K$ , provides information about the pricing probability measure  $Q_{t,T}$ . In the limit, a continuous observation of the function  $K \longrightarrow C_t$  (or of its partial derivative  $\partial C_t/\partial K$ ) would completely characterize the cumulative distribution function of the underlying asset return  $(S_T/S_t)$ under  $Q_{t,T}$ . Let us rather consider it through the probability distribution of the continuously compounded net return on the period  $[t, T]$ :

$$r_S(t,T) = \log\left[\frac{S_T B(t,T)}{S_t}\right] \tag{6}$$

With (log-forward) moneyness of the option measured by

$$x_t = \log\left[\frac{KB(t,T)}{S_t}\right] \tag{7}$$

the probability distribution under  $Q_{t,T}$  of the net return on the stock  $r_S(t, T)$  is characterized by its survival function deduced from equations  $(3)$  and  $(5)$  as

$$G_{t,T}(x_t) = -\exp(-x_t)\frac{\partial C_t}{\partial x_t}$$
(8)

where

$$C_t(x_t) = \frac{C_t}{S_t}$$
  
=  $E^{Q_{t,T}} \{ \text{Max}[0, \exp(r_S(t, T)) - \exp(x_t) \}$   
(9)

For the purpose of easy assessment of suitably normalized orders of magnitude, practitioners often prefer to plot the BS-implied volatility  $\sigma_{t}^{\text{imp}}(x_t)$  rather than the option price  $C_t(x_t)$  itself, as a function of moneyness  $x_t$ . The key reason that makes this sensible is that, in the BS model, the pricing distribution is indexed by a single volatility parameter  $\sigma$ . Under BS' assumptions, the probability distribution of the net return  $r_S(t, T)$  under  $Q_{t,T}$  is the normal one with mean  $(-1/2)(T-t)\sigma^2$  and variance  $(T-t)\sigma^2$ . This distribution is denoted by  $\aleph_{t,T}(\sigma)$ .

Then, the BS-implied volatility  $\sigma_{T-t}^{\text{imp}}(x_t)$  is defined as the value of the volatility parameter  $\sigma^2$  that would generate the observed option price  $C(x_t)$  as if the

distribution of net return under  $Q_{t,T}$  was the normal  $\aleph_{t,T}(\sigma)$ . In other words,  $\sigma_{T-t}^{\text{imp}}(x_t)$  is characterized as the solution of the following equation:

$$C_t(x_t) = BS_h[x_t, \sigma_h^{\text{imp}}(x_t)] \tag{10}$$

where  $h = T - t$  and

$$BS_h[x,\sigma] = N[d_1(x,\sigma,h)] - \exp(x)N[d_2(x,\sigma,h)] \tag{11}$$

where  $N$  is the cumulative distribution function of the standardized normal distribution and

$$d_1(x,\sigma,h) = \frac{-x}{\sigma\sqrt{h}} + \frac{1}{2}h\sigma^2 \tag{12}$$

$$d_2(x,\sigma,h) = \frac{-x}{\sigma\sqrt{h}} - \frac{1}{2}h\sigma^2 \tag{13}$$

It is worth recalling that the common use of the BS-implied volatility  $\sigma_h^{\text{imp}}(x_t)$  by no means implies that the BS model is thought as a well-specified one. By equation (10),  $\sigma_h^{\text{imp}}(x_t)$  is nothing but a known strictly increasing function of the observed option price  $C_t(x_t)$ . When plotting the volatility smile as a function  $x_t \longrightarrow \sigma_h^{\text{imp}}(x_t)$  rather than  $x_t \longrightarrow$  $C_t(x_t)$ , a convenient rescaling of the characterization (8) of the pricing distribution is simply considered. However, this rescaling depends on  $x_t$  and, by definition, produces a flat volatility smile whenever the BS pricing formula is valid in the cross section (for all moneyness levels at a given maturity) for some specific value of the volatility parameter. Note that for this the validity of the BS model itself is only a sufficient but not a necessary condition.

#### How to Graph the Smile

When the volatility smile is not flat, its pattern obviously depends on whether implied volatility  $\sigma_h^{\text{imp}}(x_t)$ is plotted against strike K, moneyness  $(K/S_t)$ , forward moneyness  $(KB(t, T)/S_t) = \exp(x_t)$ , logforward moneyness  $x_t$ , and so on. The optimal choice of variable depends on what kind of information is expected to be revealed immediately on plotting implied volatilities. The common terminology volatility smile suggests that initially it was thought of as a kind of U-shaped pattern, whereas more recent words such as *smirk* or *frown* suggest that the focus is set on frequently observed asymmetries with respect to a symmetric benchmark. Even more explicitly, since the volatility smile is supposed to reveal the underlying pricing probability measure  $Q_{t,T}$ , a common belief is that asymmetries observed in the volatility smile reveal a corresponding skewness in the distribution of (log) return under  $Q_{t,T}$ . Note, in particular, that, as mentioned above, a flat volatility smile at level  $\sigma$  characterizes a normal distribution with mean  $(-\sigma^2/2)$  and variance  $\sigma^2$ .

Beyond the flat case, the common belief of a close connection between smile asymmetries and risk-neutral skewness requires further qualification. First, the choice of variable must of course matter for discussion of smile asymmetries. We argue later that log-forward moneyness  $x_t$  is the right choice, that is, the fact that the smile asymmetry issue must be understood as a violation of the identity:

$$\sigma_h^{\text{imp}}(x_t) = \sigma_h^{\text{imp}}(-x_t) \tag{14}$$

This identity is actually necessary and sufficient to deduce from equation  $(10)$  that the general option pricing formula (9) fulfills the same kind of symmetry property as the BS one:

$$C_t(x) = 1 - \exp(x) + \exp(x)C_t(-x) \tag{15}$$

Although equation  $(15)$  is automatically satisfied when  $C_t(x) = B S_h[x, \sigma]$  (by the symmetry property of the normal distribution:  $N(-d) = 1 - N(d)$ , it characterizes the symmetry property of the forward measure that corresponds to volatility smile symmetry. It actually mimics the symmetry property of the normal distribution with mean  $(-\sigma^2/2)$  and variance  $\sigma^2$ , which would prevail in the case of validity of the BS model. By differentiation of equation (15) and comparison with equation  $(8)$ , the following can be easily checked:

The volatility smile is symmetric in the sense of equation (14) if and only if, when  $f_{t,T}$  stands for the probability density function of the log-return  $r_S(t, T)$ under the forward measure  $Q_{t,T}$ ,  $\exp(x/2) f_{t,T}(x)$  is an even function of  $x$ .

In conclusion, the relevant concept of symmetry amounts to considering pairs of moneynesses that are symmetric to each other in the following sense:

$$x_{1t} = \log\left[\frac{K_1B(t,T)}{S_t}\right] = -x_{2t} = \log\left[\frac{S_t}{K_2B(t,T)}\right]$$
(16)

In other words, the geometric mean of the two strike prices coincides with the current stock price:

$$\sqrt{K_1 B(t,T)} \sqrt{K_2 B(t,T)} = S_t \tag{17}$$

To conclude, it is worth noting that graphing the smile as a function of the log-moneyness  $x_t$  is even more relevant when one maintains the natural assumption that option prices are homogeneous functions of degree one with respect to the pair  $(S_t, K)$ . Merton [39] advocated this homogeneity property to preclude any "perverse local concavity" of the option price with respect to the stock price. It is obvious from equation  $(9)$  that a sufficient condition for homogeneity is that, as in the BS case, the pricing probability distribution  $Q_{t,T}$  does not depend on the level  $S_t$  of the stock price. This is the reason, as discussed by Garcia and Renault [30], homogeneity holds with standard stochastic volatility option pricing models and does not hold for GARCH option pricing.

For our purpose, the big advantage of the homogeneity assumption is that it allows to compare volatility smiles (for a given time to maturity) at different dates since then the implied volatility  $\sigma_{h}^{\text{imp}}(x_t)$ depends only on moneyness  $x_t$  and not directly on the level  $S_t$  of the underlying stock price. Moreover, from the Euler characterization of homogeneity,

$$C_t = S_t \frac{\partial C_t}{\partial S_t} + K \frac{\partial C_t}{\partial K} \tag{18}$$

we deduce (by comparing equations 2 and 5) that

$$\Delta_{1t} = \frac{\partial C_t}{\partial S_t} \tag{19}$$

is the standard delta-hedging ratio. Note that a common practice is to compute a proxy of  $\Delta_{1t}$  by plugging  $\sigma_h^{\text{imp}}(x_t)$  in the BS delta ratio. Unfortunately, according to some probability distribution of the volatility parameter, this approximation suffers from a convexity bias when the correct option price is a mixture of BS prices (see below). Renault [42] showed that the BS delta ratio (computed with  $\sigma_h^{\text{imp}}(x_t)$  underestimates (respectively, overestimates) the correct ratio  $\Delta_{1t}$  when the option is in the money (respectively, out of the money), that is, when  $x_t < 0$  (respectively,  $x_t > 0$ ).

### Implied Risk Aversion

Under suitable assumptions for preferences and endowment shocks, it is well known that market completeness allows us to introduce a representative investor with a utility function  $U$ . Assuming that he/she can consume at date  $t$  and at the fixed future date  $T$  and that he/she receives one share of the stock as endowment at date  $t$ , the representative investor adjusts the dollar amount invested in the stock at each intermediary date in order to maximize the expected utility of his/her terminal consumption at time  $T$  (see **Expected Utility Maximization**). In equilibrium, the investor optimally invests all his/her wealth in the risky stock and then consumes the terminal value  $S_T$ of the stock. Thus, the Euler first-order condition for optimality imposes that the price  $\pi_t$  at time t of any contingent claim that delivers the dollar amount  $g_T$ at time  $t$  is such that

$$\pi_t = E^P \left[ \beta^{T-t} \frac{U'(S_T)}{U'(S_t)} g_T \mid \mathcal{F}_t \right] \tag{20}$$

where  $E^{P}$  [.  $|\mathcal{F}_{t}]$  denotes the conditional expectation given  $\mathcal{F}_t$  with respect to the historical probability measure P.  $\beta$  is the subjective discount factor. By identifying equation  $(20)$  with equation  $(1)$ , we deduce that the density function given  $\mathcal{F}_t$  of  $Q_{t,T}$ with respect to P is proportional to  $U'(S_T)$ . Thus, if  $f_t^*$  (respectively,  $f_t$ ) stands for the density function given  $\mathcal{F}_t$  of the distribution function of  $S_T$  under the martingale measure  $Q$  (respectively under the historical measure P), we have  $(f_t^*/f_t)$  proportional to the marginal utility function and thus, by logarithmic derivatives,

$$\rho_t(S_T) = -S_T \frac{U''(S_T)}{U'(S_T)} = S_T \left(\frac{f'_t(S_T)}{f_t(S_T)} - \frac{f^{*'}_t(S_T)}{f^{*}_t(S_T)}\right) \tag{21}$$

where  $\rho_t(S_T)$  is, by definition, the Arrow-Pratt measure of relative risk aversion. Note that the result would not have changed if we had used the forward probability measure  $Q_{t,T}$  (see Forward and Swap **Measures**) instead of the risk-neutral one  $Q$ . Since as explained in the first section, the observation at time  $t$  of a cross section of option prices written on  $S_T$  allows us to infer these probability measures, it suggests that risk-aversion functions or preference parameters may be extracted from observed option

prices. Aït-Sahalia and Lo [4] and Jackwerth [35] proposed nonparametric approaches to recover riskaversion functions across wealth states from observed stock and option prices. Bliss and Panigirtzoglou [10], Garcia et al. [29], and Rosenberg and Engle [45] have estimated preference parameters based on parametric asset pricing models with several specifications of the utility function.

These efforts to exploit prices of options to recover fundamental economic parameters have produced puzzling results. Aït-Sahalia and Lo [4] found that the nonparametrically implied function of relative risk aversion varies significantly across the range of S&P 500 index values, from 1 to 60, and is U-shaped. Jackwerth [35] also found that the implied absolute risk-aversion function is U-shaped around the current forward price and also that it can become negative. Parametric empirical estimates of the coefficient of relative risk aversion also show considerable variation. Rosenberg and Engle [45] reported values ranging from  $2.36$  to  $12.55$  for a power utility pricing kernel across time, while Bliss and Panigirtzoglou [10] estimated average values between 2.33 and 11.14 for the same S&P 500 index for several option maturities. Garcia et al. [29] estimated a consumption-based asset pricing model with regimeswitching fundamentals and Epstein and Zin [23], the preferences. The estimated parameters for risk aversion and intertemporal substitution are reasonable, with average values of  $0.6838$  and  $0.8532$ , respectively, over the period  $1991-1995$ .

The general conclusion is that empirical riskneutral distributions that are computed without a precise account of the state variables that enter into the investors' information sets cannot provide valuable insights on intertemporal preferences. For example, Chabi-Yo et al. [17] showed that in an economy with regime changes either in fundamentals or in preferences, an application of the nonparametric methodology used by Jackwerth [35] to recover risk aversion will lead to similar negative estimates of the risk-aversion function in some states of wealth even though the risk-aversion functions are consistent with economic theory within each regime.

## Implied Volatility as a Calibrated Parameter

Formula (20) puts forward the so-called pricing kernel  $m_{t,T} = \beta^{T-t} \frac{U'(S_T)}{U'(S_t)}$  that emphasizes the role of risk aversion. In particular, in the case of constant relative risk aversion  $(\rho_t(S_T) = -S_T \frac{U''(S_T)}{U'(S_T)} =$  $a > 0$ ), the log-pricing kernel is perfectly correlated to the log-return on the stock:

$$\text{Log}(m_{t,T}) = -a\text{Log}\left[\frac{S_T}{S_t}\right] + (T-t)\text{Log}(\beta) \quad (22)$$

More generally, it is convenient to rewrite the callpricing equation  $(1)$  in terms of the pricing kernel:

$$C_t = E^P \left[ m_{t,T} Max[0, S_T - K] \mid \mathcal{F}_t \right] \tag{23}$$

where the general definition of the pricing kernel (see also **Pricing Kernels**) gives

$$\frac{\mathrm{d}Q_{t,T}}{\mathrm{d}P} = \frac{m_{t,T}}{B(t,T)}\tag{24}$$

It is easy to check that the general call-pricing formula (23) collapses into the BS one when the two following conditions are fulfilled:

- 1. The conditional distribution given  $\mathcal{F}_t$  of the logreturn Log  $\left[\frac{S_T}{S_t}\right]$  is normal with constant variance
- 2. The log-pricing kernel  $\text{Log}(m_{t,T})$  is perfectly correlated to the log-return on the stock as in equation  $(22)$ .

We get the first interesting generalization of the BS formula by now considering that the log-return  $\text{Log}\left[\frac{S_T}{S_t}\right]$  and the log-pricing kernel  $\text{Log}(m_{t,T})$  may be jointly normally distributed given  $\mathcal{F}_t$ , with conditional moments possibly depending on the conditional information at time  $t$ . Interestingly enough, it can be shown that the call price computed from formula  $(23)$ with this joint conditional lognormal distribution will explicitly depend on the conditional moments only through the conditional stock volatility:

$$(T-t)\sigma_{t,T}^{2} = \text{Var}\left[\text{Log}\left[\frac{S_{T}}{S_{t}}\right] \mid \mathcal{F}_{t}\right]$$
(25)

More precisely, we get the following option pricing formula:

$$C_t = S_t B S_{T-t}[x_t, \sigma_{t,T-t}] \tag{26}$$

Formula (26) is actually the generalization of the "risk-neutral valuation relationship" (RNVR) put forward by Brennan [12]. With joint log-normality

of return and pricing kernel, we find again the BS functional form due to the Cameron-Martin formula (a static version of Girsanov's theorem), which tells us that when  $X$  and  $Y$  are jointly normal,

$$E\left\{\exp(X)g(Y)\right\} = E[\exp(X)]E\left\{g[Y + \text{cov}(X, Y)]\right\}$$
(27)

While the term  $E[\exp(X)]$  will give  $B(t, T)$ (with  $X = \text{Log}(m_{t,T})$ ), the term  $cov(X, Y)$  (with  $Y =$  $\text{Log}\left[\frac{S_T}{S_t}\right]$ ) will make the risk-neutralization since  $E\left\{\exp(X)\exp(Y)\right\} = E[\exp(X)]E\left\{\exp[Y + \text{cov}(X,$  $Y$ ]} must be 1.

From an econometric viewpoint, the interest of equation  $(26)$ , when compared to equation  $(10)$ , is to deliver a flat volatility smile but with an implied volatility level that may be time varying and correspond to the conditional variance of the conditionally lognormal stock return. In other words, the timevarying volatility of the stock becomes observable as calibrated from option prices:

$$\sigma_{t,T} = \sigma_{T-t}^{\text{imp}}(x_t) \quad \forall x_t \tag{28}$$

The weakness of this approach is its lack of robustness with respect to temporal aggregation. In the GARCH-type literature, stock returns may be conditionally lognormal when they are considered on the elementary period of the discrete-time setting  $(T = t + 1)$  while implied time-aggregated dynamics are more complicated. This is the reason the GARCH option pricing literature [21, 33]) maintains formula (26) only for  $T = t + 1$ . Nonflat volatility smiles may be observed with longer times to maturity. Kallsen and Taqqu [37] provided a continuous-time interpretation of such GARCH option pricing.

## Implied Volatility as an Expected Average Volatility

To account for excess kurtosis and skewness in stock log-returns, a fast empirical approach amounts to considering that the option price at time  $t$  is given by a weighted average:

$$\alpha_t S_t B S_h[x_t, \sigma_{1t}] + (1 - \alpha_t) S_t B S_h[x_t, \sigma_{2t}] \qquad (29)$$

The rationale for equation  $(29)$  is to consider that a mixture of two normal distributions with standard errors  $\sigma_{1t}$  and  $\sigma_{2t}$  and weights  $\alpha_t$  and  $(1 - \alpha_t)$ , respectively, may account for both skewness and excess kurtosis in stock log-return. The problem with this naive approach is that it does not take into account any risk premium associated with the mixture component. More precisely, if we want to accommodate a mixture of normal distributions with a mixing variable  $U_{t,T}$ , we can rewrite equation (23) as

$$C_{t} = E^{P} \left\{ E^{P} \left[ m_{t,T} Max[0, S_{T} - K] \mid \mathcal{F}_{t}, U_{t,T} \right] \mid \mathcal{F}_{t} \right\}$$
(30)

where, for each possible value  $u_{t,T}$  of  $U_{t,T}$ , a BS formula such as equation  $(26)$  is valid for computing

$$E^{P}\left[m_{t,T}Max[0, S_{T}-K] \mid \mathcal{F}_{t}, U_{t,T}=u_{t,T}\right] \quad (31)$$

In other words, it is true that, as in equation  $(29)$ , the conditional expectation operator (given  $\mathcal{F}_t$ ) in equation  $(30)$  displays the option price as a weighted average of different BS prices with the weights corresponding to the probabilities of the possible values  $u_{t,T}$  of the mixing variable  $U_{t,T}$ . However, the naive approach  $(29)$  is applied incorrectly if we do not take into account the fact that the additional conditioning information  $U_{t,T}$  should lead to modify some key inputs in the BS option pricing formula. Suppose that investors are told that the mixing variable  $U_{t,T}$  will take the value  $u_{t,T}$ , then the current stock price would no longer be

$$S_t = E^P[m_{t,T}S_T \mid \mathcal{F}_t] \tag{32}$$

but

$$S_t^*(u_{t,T}) = E^P \left[ m_{t,T} S_T \mid \mathcal{F}_t, U_{t,T} = u_{t,T} \right] \quad (33)$$

For the same reason, the pure discount bond that delivers  $1$  at time  $T$  will no longer be priced at time  $t$  as

$$B(t, T) = E^{P}\left[m_{t, T} \mid \mathcal{F}_{t}\right] \tag{34}$$

but as

$$B^*(t,T)(u_{t,T}) = E^P \left[ m_{t,T} \mid \mathcal{F}_t, U_{t,T} = u_{t,T} \right] \tag{35}$$

In other words, various BS option prices that are averaged in a mixture approach such as equation  $(29)$ must be computed, not with actual values  $B(t, T)$ and  $S_t$  of the current bond and stock prices, but with values  $B^*(t,T)(u_{t,T})$  and  $S^*_t(u_{t,T})$  not directly

observed but computed from equations (35) and (33). In particular, the key inputs, underlying stock price and interest rate, should be different in various applications of the BS formulas like  $BS_{h}[x, \sigma_{1}]$  and  $BS_{h}[x, \sigma_{2}]$  in equation (29). This remark is crucial for the conditional Monte Carlo approach, as developed, for instance, by Willard [47] in the context of option pricing with stochastic volatility. Revisiting a formula initially derived by Romano and Touzi [44], Willard [47] noted that the variance reduction technique, known as conditional Monte Carlo, can be applied even when the conditioning factor (the stochastic volatility process) is instantaneously correlated with the stock return as it is the case when leverage effect is present. He stressed that "by conditioning on the entire path of the noise element in the volatility (instead of just the average volatility), we can still write the option's price as an expectation over Black-Scholes prices by appropriately adjusting the arguments to the Black-Scholes formula". Willard's [47] "appropriate adjustment" of the stock price is actually akin to equation (33). Moreover, he does not explicitly adjust the interest rate according to equation (35) and works with a fixed risk-neutral distribution. More generally, the continuous-time dynamics of a pricing kernel  $m_{t,T}$  is considered, which is seen as the relative increment of a pricing kernel process  $M_t$ :

$$m_{t,T} = \frac{M_T}{M_t} \tag{36}$$

The key idea of the mixture model is then to define a conditioning variable  $U_{t,T}$  such that the pricing kernel process and the stock price process jointly follow a bivariate geometric Brownian motion under the conditional probability distribution given  $U_{t,T}$ . The mixing variable  $U_{t,T}$  will typically show up as a function of a state variable path  $(X_{\tau})_{t \leq \tau \leq T}$ . More precisely, we specify the jump-diffusion model:

٠.

$$d(\log S_t) = \mu(X_t) dt + \alpha(X_t) dW_{1t}$$
$$+ \beta(X_t) dW_{2t} + \gamma_t dN_t \qquad (37)$$

$$d(\log M_t) = h(X_t) dt + a(X_t) dW_{1t}$$
$$+ b(X_t) dW_{2t} + c_t dN_t \qquad (38)$$

where  $(W_{1t}, W_{2t})$  is a two-dimensional standard Brownian motion,  $N_t$  is a Poisson process with intensity  $\lambda(X_t)$  depending on the state variable  $X_t$ . Given

the jump dates, the jump amplitudes at these dates are independent draws  $(\gamma_t, c_t)$  in a fixed bivariate normal distribution. These draws are also independent of the state variable process  $X$ . The Brownian motion  $W_1$  is assumed to be part of the state variable vector  $X$  to capture the possible instantaneous correlation between ex-jump volatility of the stock (as measured by  $V_t = \alpha^2(X_t) + \beta^2(X_t)$  and its Brownian innovation. More precisely, the correlation coefficient  $\rho(X_t) = \frac{\alpha(X_t)}{\sqrt{V_t}}$  measures the so-called leverage effect.

The jump-diffusion model (37 and 38) is devised such that, given the state variables path  $(X_{\tau})_{t < \tau < T}$ as well as the number  $(N_T - N_t)$  of jumps between times t and T, the joint normality of  $(\log S_T, \log m_{t,T})$ is maintained. This allows us to derive a generalized Black and Scholes (GBS) option pricing formula by application of equations  $(30)$  and  $(26)$ :

$$C_t = S_t E^P[\xi_{t,T} B S_{T-t}(x_t^*, \sigma_{t,T}) \mid \mathcal{F}_t]$$
(39)

where

$$\sigma_{t,T}^{2} = \int_{t}^{T} [1 - \rho^{2}(X_{\tau})] V_{\tau} d\tau + (N_{T} - N_{t}) Var(\gamma_{t})$$
(40)

and

$$x_t^* = \log\left[\frac{KB^*(t,T)}{S_t \xi_{t,T}}\right] \tag{41}$$

where  $S_t \xi_{t,T}$  and  $B^*(t,T)$  correspond to  $S_t^*(u_{t,T})$ and  $B^*(t,T)(u_{t,T})$ , respectively, which are defined in equations (33) and (35). General computations of these quantities in the context of a jumpdiffusion model can be found in [27] and [48]. Let us exemplify these formulas when there is no jump. Then, we can define a short-term interest rate as

$$r(X_t) = -h(X_t) - \frac{1}{2}[a^2(X_t) + b^2(X_t)] \qquad (42)$$

and then

$$B^*(t,T) = \exp\left[-\int_t^T r(X_\tau) \,\mathrm{d}\tau\right]$$
$$\times \exp\left[\int_t^T a(X_\tau) \,\mathrm{d}W_{1\tau} - \frac{1}{2} \int_t^T a^2(X_\tau) \,\mathrm{d}\tau\right]$$
(43)

and

$$\xi_{t,T} = \exp\left[\int_t^T [a(X_\tau) + \alpha(X_\tau)] \, \mathrm{d}W_{1\tau} - \frac{1}{2} \int_t^T [a(X_\tau) + \alpha(X_\tau)]^2 \mathrm{d}\tau\right] \tag{44}$$

In particular, it can be easily checked that

$$B(t,T) = E^{P}[B^{*}(t,T) | \mathcal{F}_{t}] \tag{45}$$

and

$$S_t = E^P[S_t \xi_{t,T} \mid \mathcal{F}_t] \tag{46}$$

For now, the difference between  $S_t \xi_{t,T}$  and  $B^*(t,T)$  and their respective expectations  $S_t$  and  $B(t, T)$  are neglected. It is then clear that the GBS formula warrants the interpretation of the BS-implied volatility  $\sigma_{T-t}^{\text{imp}}(x_t)$  as approximatively an expected average volatility. Neglecting convexity effects (nonlinearity of the BS formula with respect to volatility), the GBS formula would actually give

$$\left[\sigma_{T-t}^{\text{imp}}(x_t)\right]^2 = E^P[\sigma_{t,T}^2 \mid \mathcal{F}_t] \tag{47}$$

The likely impact of the difference between  $S_t \xi_{t,T}$ and  $B^*(t, T)$  and their respective expectations  $S_t$  and  $B(t, T)$  is twofold. First, a nonzero function  $a(X_{\tau})$ must be understood as a risk premium on the volatility risk. In other words, the above interpretation of  $\sigma_{T-t}^{\text{imp}}(x_t)$  as approximatively an expected average volatility can be maintained by using risk-neutral expectations. Considering the BS-implied volatility as a predictor of volatility over the lifetime of the option is tantamount to neglecting the volatility risk premium. Beyond this risk premium effect, the leverage effect  $\rho(X_t)$  will distort this interpretation through its joint impact on  $\sigma_{t,T}^2$  and also on  $\xi_{t,T}$  (through  $\alpha(X_t) = \rho(X_t) \sqrt{V_t}$ ). Although Renault and Touzi [43] have shown that we will get a symmetric volatility smile in the case of zero-leverage, Renault [42] explained that, with nonzero leverage, the implied distortion of the stock price by the factor  $\xi_{t,T}$  will produce asymmetric volatility smirks. More precisely, Yoon [48] characterized the cumulative impact of the two effects of leverage and showed that they compensate each other almost exactly for at the money options. Finally, Comte and Renaul's [18] long-memory volatility model explains that, in spite of the time averaging in equations  $(40)$  and  $(47)$ , the

volatility smile does not become flat even for longterm options.

The close connection (equations  $40$  and  $47$ ) between BS-implied volatility and the underlying volatility process  $(\sqrt{V_t})$  has inspired a strand of literature on estimating volatility dynamics from option prices data. Pastorello et al. [41] consider directly  $[\sigma_{T-t}^{\text{imp}}(x_t)]^2$  as a proxy for squared spot volatility  $V_t$ and correct the resulting approximation bias in estimating volatility dynamics by indirect inference. The "implied-states approach" (see [40] and references therein) more efficiently uses the exact relationship between  $\sigma_{T-t}^{\text{imp}}(x_t)$  and  $V_t$ , as given by equations (40) and (47) for a given spot volatility model, to estimate the volatility parameters by maximum likelihood or generalized method of moments. Finally, Garcia et al. [28] simplified the procedure by taking advantage of high-frequency intraday return data for a direct measurement of the integrated volatility  $\int_t^T V_{\tau} d\tau$ .

### **Data-driven Approaches**

In this section, we discuss methods that are, to various degrees, data-driven approaches, ranging from purely data-driven, sometimes called *nonparametric* approaches to semiparametric ones—where parametric and nonparametric estimators are combined. The estimation of option-implied densities can take various forms as there are many different ways to smooth a curve. Nadaraya-Watson kernel regression was used by Aït-Sahalia and Lo [3, 13, 14, 19], constrained splines by Bates [9], flexible parametric functional forms by Abadir and Rockinger [1], and neural networks by Aït-Sahalia and Duarte [2]; Bondarenko [11] and Garcia and Gençay [26], considered constrained least-square approaches. A more practitioneroriented approach was pioneered by Jackwerth and Rubinstein [36] and Rubinstein [46] who constructed implied trees from listed option prices.

All these methods are data intensive and typically feature slow convergence rates. Only a few indices have enough liquid actively traded derivatives with a wide span of maturities and moneyness to warrant applications of these methods.

The extended method of moments (XMMs) estimator, introduced by Gagliardini *et al.* [31], extends the standard GMM to accommodate a more general set of moment restrictions. The standard GMM is based on uniform conditional moment restrictions,

such as equation (20), which are valid for any value of the conditioning variables. The XMM can handle not only the uniform moment restrictions but also the local moment restrictions that are valid only for a given value of the conditioning variables. This leads to a new field of application to derivative pricing, as the XMM can be used for reconstructing the pricing operator on a given day, by using the information in a cross section of observed traded derivative prices and a time series of underlying asset returns. To illustrate the principle of XMM, the S&P 500 index and its derivatives are considered. Suppose that an investor at date  $t_0$  is interested in estimating the price  $c_{t_0}(h, k)$ of a call option with time-to-maturity  $h$  and moneyness strike  $k$  that is currently not (actively) traded on the market. He/she has data on a time series of T daily returns of the S&P 500 index, as well as on a small cross section of current option prices  $c_{t_0}(h_i,k_i), i=1,\ldots,n$ , of *n* highly traded derivatives. The XMM approach provides the estimated prices  $\hat{c}_{t_0}(h,k)$  for different values of moneyness strike  $k$  and time-to-maturity  $h$ , which interpolate the observed prices of highly traded derivatives and satisfy the hypothesis of the absence of arbitrage opportunities. These estimated prices are consistent for a large number of dates  $T$ , but with a fixed, even small, number of observed derivative prices  $n$ .

A slightly less ambitious approach has been recently advocated by Erikkson et al. [24]. They suggest the use of the normal inverse Gaussian (NIG) family (see Normal Inverse Gaussian Model) to approximate an unknown distribution risk-neutral density. The appeal of the NIG family of distributions is that they are characterized by the first four moments: mean, variance, skewness, and kurtosis. These are the moments we care about in many applications, including derivative pricing. The unknown density function is approximated by matching the cumulants. The latter are obtained from the cross section of option prices using methods proposed by Bakshi *et al.* [5]. The strength of their approach is that they link the pricing of individual derivatives to the moments of the risk-neutral distribution, which has an intuitive appeal in terms of how volatility, skewness, and kurtosis of the riskneutral distribution can explain the behavior of the derivative prices. Erikkson et al. [24] showed that the approximation errors are minor when compared to several option pricing models that have known densities.

# **Non-Gaussian Option Pricing**

The affine jump-diffusion framework (*see* **Affine Models**) represents an important theoretical advance. Yet, it has been argued that it has its limitations, notably due to the exclusive use of compound Poisson processes to model jumps. These processes generate a finite number of jumps within a finite time interval and have accordingly been referred to as *finite activity jump processes*. The observation that asset prices actually display many small jumps on a fine timescale has led to the development of more general jump structures, which permit an infinite number of jumps to occur within any bounded time interval. Examples of infinite-activity jump models include the inverse Gaussian model of Barndorff-Nielsen [6, 7], the generalized hyperbolic class of Eberlein *et al.* [22], the variance gamma (VG) model (*see* **Variance-gamma Model**) of Madan and Milne [38], the generalization of VG by Carr *et al.* [15], and the finite moment log-stable model of Carr and Wu [16]. Empirical work by these authors is generally supportive of the use of infinite-activity processes as a way to model returns in a parsimonious way. The recognition that volatility is stochastic has led to further extensions of infinite-activity Levy models ( ´ *see* **Barndorff-Nielsen and Shephard (BNS) Models**; **Time-changed Levy Process ´** ) by Barndorff-Nielsen and Shephard [8] and Carr and Wu [16]. However, these models often assume that changes in volatility are independent of asset returns, and consider the leverage effect only under special cases. Carr and Wu [16] used time-changed Levy processes that general- ´ ize the affine Poisson jump diffusions by relaxing the affine structure and by allowing more general specifications of the jump structure. Since the pioneering work of Heston [32], the literature has used the characteristic function for deriving option prices. Accordingly, Carr and Wu focus on developing analytic expressions for the characteristic function of a time-changed Levy process ( ´ *see* **Time-changed Levy ´ Process**).

# **References**

[1] Abadir, K.M. & Rockinger, M. (1998). *Densityembedding Functions*, University of York and Groupe HEC. Working Paper.

- [2] A¨ıt-Sahalia, Y. & Duarte, J. (2003). Nonparametric option pricing under shape restrictions, *Journal of Econometrics* **116**, 9–47.
- [3] A¨ıt-Sahalia, Y. & Lo, A.W. (1998). Nonparametric estimation of state-price densities implicit in financial asset prices, *Journal of Finance* **53**, 499–547.
- [4] Ait-Sahalia Y. & Lo A. (2000). Nonparametric risk management and implied risk aversion, *Journal of Econometrics* **94**, 9–51.
- [5] Bakshi G., Kapadia N. & Madan D. (2003). Stock return characteristics, Skew laws, and differential pricing of individual equity options, *Review of Financial Studies* **16**, 101–143.
- [6] Barndorff-Nielsen, O.E. (1998). Processes of normal inverse Gaussian type, *Finance and Stochastics* **2**, 41–68.
- [7] Barndorff-Nielsen, O.E. (2001). Superposition of Ornstein-Uhlenbeck type processes, *Theory of Probability and Its Applications* **45**(2), 175–194.
- [8] Barndorff-Nielsen, O.E. & Shephard, N. (2001). Non-Gaussian Ornstein-Uhlenbeck-based models and some of their uses in financial economics (with discussion), *Journal of the Royal Statistical Society, Series B* **63**, 167–241.
- [9] Bates, D. (2000). Post-'87 crash fears in the S&P 500 futures option, *Journal of Econometrics* **94**, 181–238.
- [10] Bliss, R.R. & Panigirtzoglou, N. (2004). Option-implied risk aversion estimates, *Journal of Finance* **59**, 407–446.
- [11] Bondarenko, O. (2003). Estimation of risk-neutral densities using positive convolution approximation, *Journal of Econometrics* **116**, 85–112.
- [12] Brennan, M.J. (1979). The pricing of contingent claims in discrete-time models, *Journal of Finance* **34**, 53–68.
- [13] Broadie, M., Detemple, J., Ghysels, E. & Torres, O. ` (2000). American options with stochastic dividends and volatility: a nonparametric investigation, *Journal of Econometrics* **94**, 53–92.
- [14] Broadie, M., Detemple, J., Ghysels, E. & Torres, O. ` (2000). Nonparametric estimation of American options exercise boundaries and call prices, *Journal of Economic Dynamics and Control* **24**, 1829–1857.
- [15] Carr, P., Geman, H., Madan, D.B. & Yor, M. (2003). Stochastic volatility for Levy processes, ´ *Mathematical Finance* **13**, 345–382.
- [16] Carr, P. & Wu, L. (2004). Time-changed Levy processes ´ and option pricing, *Journal of Financial Economics* **71**, 113–141.
- [17] Chabi-Yo, F., Garcia, R. & Renault, E. (2008). State dependence can explain the risk aversion puzzle, *Review of Financial Studies* **21**, 973–1011.
- [18] Comte, F. & Renault E. (1998). Long-memory in continuous time stochastic volatility models, *Mathematical Finance* **8**, 291–323; Reprinted in Shephard, N. (ed.) (2005). *Stochastic Volatility: Selected Readings*, Oxford University Press.

- [19] Cont, R. & Da Fonseca, J. (2002). Dynamics of implied volatility surfaces, *Quantitative Finance* **2**(1), 45–60.
- [20] Cox, J.C., Ross, S.A. & Rubinstein, M. (1979). Option pricing: a simplified approach, *Journal of Financial Economics* **7**, 229–263.
- [21] Duan, J.C. (1995). The GARCH option pricing model, *Mathematical Finance* **5**, 13–32.
- [22] Eberlein, E., Keller, U. & Prause, K. (1998). New insights into smile, mispricing, and Value at Risk: the hyperbolic model, *Journal of Business* **71**, 371–405.
- [23] Epstein, L. & Zin, S. (1989). Substitution, risk aversion, and the temporal behavior of consumption and asset returns: a theoretical framework, *Econometrica* **57**, 937–969.
- [24] Erikkson, A., Ghysels, E. & Wang, F. (2009). The normal inverse Gaussian distribution and the pricing of derivatives, *Journal of Derivatives* **16**, 23–38.
- [25] Follmer, H. & Schied, A.A. (2004). ¨ *Stochastic Finance: An Introduction in Discrete Time*, Walter de Gruyter.
- [26] Garcia, R. & Gen¸cay, R. (2000). Pricing and hedging derivative securities with neural networks and a homogeneity hint, *Journal of Econometrics* **94**, 93–115.
- [27] Garcia, R., Ghysels, E. & Renault, E. (2009). Econometrics of option pricing models, in *Handbook of Financial Econometrics*, Y. Ait-Sahalia & L.P. Hansen, eds, North Holland, forthcoming.
- [28] Garcia, R., Lewis, M., Pastorello, S. & Renault, E. (2009). Estimation of objective and risk-neutral distributions based on moments of integrated volatility, *Journal of Econometrics*, forthcoming.
- [29] Garcia, R., Luger, R. & Renault, E. (2003). Empirical assessment of an intertemporal option pricing model with latent variables, *Journal of Econometrics* **116**, 49–83.
- [30] Garcia, R. & Renault, E. (1998). A note on GARCH option pricing and hedging, *Mathematical Finance* **8**(2), 153–161.
- [31] Gagliardini, P., Gourieroux, C. & Renault, E. (2009). ´ *Efficient Derivative Pricing by Extended Method of Moments*, Discussion Paper.
- [32] Heston, S. (1993). A closed form solution for options with stochastic volatility with applications to bond and currency options, *The Review of Financial Studies* **6**, 327–343.
- [33] Heston, S. & Nandi, S. (2000). A closed-form GARCH option valuation model, *Review of Financial Studies* **13**, 585–625.
- [34] Huang, C. & Litzenberger, R.H. (1998). *Foundations for Financial Economics*, North Holland.
- [35] Jackwerth, J. (2000). Recovering risk aversion from option prices and realized returns, *Review of Financial Studies* **13**, 433–451.
- [36] Jackwerth, J. & Rubinstein, M. (1996). Recovering probabilities distributions from option prices, *Journal of Finance* **51**, 1611–1631.
- [37] Kallsen, J. & Taqqu, M.S. (1998). Option pricing in ARCH-type models, *Mathematical Finance* **8**, 13–26.

- [38] Madan, D. & Milne, F. (1991). Option pricing with VG martingale components, *Mathematical Finance* **1**, 39–56.
- [39] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**, 141–183.
- [40] Pastorello, S., Patilea, V. & Renault, E. (2003). Iterative and recursive estimation in structural non-adaptive models - invited lecture with discussion, *Journal of Business, Economics and Statistics* **21**, 449–509.
- [41] Pastorello, S., Renault, E. & Touzi, N. (2000). Statistical inference for random-variance option pricing, *Journal of Business and Economic Statistics* **18**, 358–367.
- [42] Renault, E. (1997). Econometric models of option pricing errors, in *Advances in Economics and Econometrics: Theory and Applications*, D. Kreps & K. Wallis, eds, Cambridge University Press, Vol. 3.
- [43] Renault, E. & Touzi, N. (1996). Option hedging and implied volatilities in a stochastic volatility model, *Mathematical Finance* **6**, 279–302.
- [44] Romano M. & Touzi N. (1997). Contingent claims an market completeness in a stochastic volatility model, *Mathematical Finance* **7**, 399–410.
- [45] Rosenberg, J.V. & Engle, R.F. (2002). Empirical pricing Kernels, *Journal of Financial Economics* **64**, 341–372.
- [46] Rubinstein, M. (1994). Implied binomial trees, *Journal of Finance* **44**, 771–818.
- [47] Willard, G.A. (1997). Calculating prices and sensitivities for path-independent derivative securities in multifactor models, *Journal of Derivatives* **5**, 45–61.
- [48] Yoon, J. (2008). *Option Pricing with Stochastic Volatility Models*. PhD Thesis, UNC at Chapel Hill.

# **Further Reading**

- Bakshi, G. & Madan, D. (2000). Spanning and derivativesecurity valuation, *Journal of Financial Economics* **55**, 205–238.
- Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–659.
- Garcia, R., Luger, R. & Renault, E. (2005). Viewpoint: option prices, preferences and state variables, *Canadian Journal of Economics* **38**, 1–27.
- Ghysels, E. & Wang, F. (2009). *Some Useful Densities for Risk Management and their Properties*, Discussion Paper, UNC.

# **Related Articles**

**Affine Models**; **Arrow–Debreu Prices**; **Black– Scholes Formula**; **Equivalent Martingale Measures**; **Implied Volatility in Stochastic Volatility** **Models**; **Implied Volatility Surface**; **Jump-diffusion Models**; **Jump Processes**; **Model Calibration**; **Option Pricing: General Principles**; **Pricing Kernels**; **Risk-neutral Pricing**; **Saddlepoint Approximation**; **Stochastic Volatility Models**.

ERIC RENAULT
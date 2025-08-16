## **Measurements Errors**

In physical sciences, errors in measurement are present everywhere owing to the unavoidable inaccuracy of the measuring devices, and most often they are thought of as being independent and centered variables, usually with a density, and which add up to the "true" values of the quantity of interest. In finance, the quantities of interest are usually prices, which can be exactly observed by virtually any person. Some factual errors, like wrong records, may occur, but those are relatively infrequent and easy to detect (giving rise to the "cleaning" of data), and may be modeled with independent centered variables with no density and a rather large mass at  $0$  (= no error).

However, mathematical models in finance are often continuous-time models describing the dynamics of a process  $(X_t : t > 0)$ . This process is the basic underlying "price", or log-price, of an asset, or several assets if it is multivariate, and it satisfies the rules of mathematical finance, and, in particular, it is a semimartingale by the first fundamental theorem of asset pricing. This process cannot be exactly observed because (i) any observed price is an integer (a number of elementary units, like a cent or a hundredth of a cent); and (ii) one may think that extraneous reasons, like some erratic behavior of price makers or erratic orders, "locally" change the price in a way that does not affect the underlying and should not influence the model for it.

In practice, one then observes prices  $Z_t$  that are possibly different from the underlying, or "efficient", prices  $X_t$ , and at finitely many times  $t_0, t_1, \dots, t_n$ . This may look like an academic difference and it may appear that, in practice, we ought to consider  $Z_t$ and not  $X_t$  at all. However, currently we have highfrequency or very high-frequency data, like tick data, and it is empirically clear that we need to differentiate between  $X_t$  and  $Z_t$ . For example, when  $Z_t = X_t$ (no error), the so-called realized volatility, which is the sum

$$V_n = (Z_{t1} - Z_{t_0})^2 + (Z_{t_2} - Z_{t_1})^2$$
  
+ \dots + (Z\_{t\_n} - Z\_{t\_{n-1}})^2 (1)

is a quantity that converges, when the observations become more and more frequent over a fixed time interval  $[0, T]$ , to a given quantity V (the integrated volatility over  $[0, T]$  when  $X_t$  is continuous, and, more generally, to the quadratic variation of the process  $X_t$ ). Moreover, at least when observation times are equidistant or almost equidistant, the "rate of convergence" is  $\sqrt{n}$ , which means that  $\sqrt{n}$  ( $V_n$  –  $V$ ) does neither explode nor go to 0 (and in fact it usually converges to some limit). Now, all empirical studies show that  $V_n$  increases indefinitely when the frequency of observations increases: this goes back to [15] and [8], or more recently to, for example, [2] or [12]. Hence, the observations  $Z_t$ differ from the underlying  $X_t$  in a nonnegligible way, and the difference  $\epsilon_t = Z_t - X_t$  is referred to as the microstructure noise, or market frictions, and should be taken into account.

We then have to give a model for this microstructure noise, on top of these mimartingale model for  $X_t$ , like Black-Scholes, possibly with stochastic volatility, or jump diffusion, or others. The microstructure noise models that have been proposed so far in the literature are mostly the following:

1. The errors  $\epsilon_t$  are independent, centered, identically distributed variables, and also independent of the underlying  $X_t$ . This is the simplest and most well-understood situation, in which the uncorrected realized volatility  $V_n$  increases to  $\infty$ at the rate *n*. When the efficient price  $X_t$  is continuous and one is interested in estimating the integrated volatility  $V$  over  $[0, T]$ , that is, the quadratic variation of  $X_t$  at time T, a variety of variants of  $V_n$  have been proposed, using various smoothing kernels: the best methods give a rate of convergence which is  $n^{1/4}$ , known as the *optimal rate* when  $X_t$  is a Brownian motion, and asymptotic variances which are nearly optimal. Note that no distributional assumption is made on the errors, and, in particular, the variance of the errors is not supposed to be known.

Such results can be extended to (i) errors that are not independent, but present some sort of "weak" dependence, and are still globally independent of  $X_t$ ; (ii) errors that are not identically distributed, provided their second moments stay constant; (iii) errors that are multiplicative instead of additive, meaning that the variables  $Z_t/X_t$  are independent instead of the  $Z_t - X_t$ , and "centered" is replaced by "with mean 1". The literature about this question is huge, and among many articles we can quote  $[1, 3-6, 13, 14, 16, 17]$ .

## **2 Measurements Errors**

- 2. The previous models more or less take care of reason (ii) for microstructure noise. As for reason (i), and if it were the only reason for the noise, one should simply take the observation *Zt* to be *Zt* = *α*[*Xt /α*], where [*x*] denotes the integer part of any number *x*, and *α* is the precision with which prices are written (1 cent or 1*/*100 cent for example). Then again some results for the estimation of the integrated volatility *V* are available, asymptotically when *n* increases whereas the rounding level *α* decreases to 0. Very few papers have been devoted so far to this subject; see, for example, [7].
- 3. Now, with the frequency attained by observations of prices, one cannot satisfactorily consider that the rounding level *α* is "small", and we have a serious problem here: if *α* is fixed and the frequency increases, then the realized volatility increases to <sup>∞</sup> with the rate <sup>√</sup>*n*, and the integrated volatility is no longer identifiable. The best one can know about the process *Xt* is the times at which it crosses the level *iα* for any integer *i*, or equivalently the family of so-called "local times" *L(iα)* at levels *iα* for all integers *i* (and time *T* , the time horizon). This is very far from *V* , although *V* is indeed the limit of *α <sup>i</sup>*≥<sup>0</sup> *L(iα)* as *α* → 0 (see [9]).
- 4. In practice, models like (1) above are not fully satisfactory because they do not account for the—obvious and ubiquitous—fact that rounding-off occurs. Models like (2) with a fixed level *α* are not satisfactory either, on a mathematical level (they do not permit to retrieve the quantities of interest like *V* ) and on an empirical level they give rise to sequences of prices that stay constant for relatively many successive times and then oscillate wildly between two adjacent multiples of *α*, then stay constant again: this is not quite observed in practice; usually prices stay constant for a few successive times, with occasionally a jump back and forth of one unit. Probably a more reasonable model consists in a mixture of (1) and (2): we have additive errors *t* , and then rounding, that is, we observe *Zt* = *α(*[*(Xt* + *t)/α*]. It turns out—perhaps surprisingly—that if the errors *t* have a density that is positive on an arbitrarily located interval of length at least *α*, then it is possible to retrieve the integrated volatility *V* in pretty much the same way as when rounding

is absent, and at the same rate. Some recent attempts in this direction may be found in [11] and [10].

5. One might also look for more microeconomically oriented models. That is, in addition to the rounding effect, which is probably unavoidable, one tries to model the behavior of the various agents so that the observed prices *Zt* behave according to empirical data, whereas the underlying *Xt* , which is a sort of "local limit" of the *Zt*'s, satisfies a model that fits the usual requirements of mathematical finance (no-arbitrage, completeness, and so on). This looks like the two-scale diffusions, but so far this has not really been put in use, because of the mathematical difficulties, and even more because the underlying microeconomics is still at a rather rudimentary level.

## **References**

- [1] Ait-Sahalia, Y., Mykland, P.A. & Zhang, L. (2005). How often to sample a continuous-time process in the presence of market microstructure noise, *Review of Financial Studies* **18**, 351–416.
- [2] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Labys, P. (2000). Great realizations, *Risk* **13**, 105–108.
- [3] Andersen, T.G., Bollerslev, T., Diebold, F.X. & Labys, P. (2001). The distribution of realized exchange rate volatility, *Journal of the American Statistical Association* **96**, 42–55.
- [4] Bandi, F.M. & Russell, J.R. (2006b). Separating microstructure noise from volatility, *Journal of Financial Economics* **79**, 655–692.
- [5] Barndorff-Nielsen, O.E., Hansen, P.R., Lunde, A. & Shephard, N. (2008). Designing realised kernels to measure ex-post variation of equity prices in the presence of noise, *Econometrica* **76**(6), 1481–1536.
- [6] Barndorff-Nielsen, O.E. & Shephard, N. (2002). Econometric analysis of realised volatility and its use in estimating stochastic volatility models, *Journal of the Royal Statistical Society, B* **64**, 253–280.
- [7] Delattre, S. & Jacod, J. (1997). A central limit theorem for normalized functions of the increments of a diffusion process, in the presence of round-off errors, *Bernoulli* **3**, 1–28.
- [8] Hasbrouck, J. (1993). Assessing the quality of a security market: a new approach to transaction-cost measurement, *Review of Financial Studies* **6**, 191–212.
- [9] Jacod, J. (1996). La variation quadratique du Brownien en presence d'erreurs d'arrondi, ´ *Ast´erisque* **236**, 155–162.
- [10] Jacod, J., Li, Y., Mykland, P.A., Podolskij, M. & Vetter, M. (2009). Microstructure noise in the continuous

case: the pre-averaging approach, *Stochastic Processes and their Applications* **119**(7), 2249–2276.

- [11] Li, Y. & Mykland, P.A. (2007). Are volatility estimators robust with respect to modeling assumptions? *Bernoulli* **13**, 601–622.
- [12] Mykland, P.A. & Zhang, L. (2005). Discussion of paper "a selective overview of nonparametric methods in financial econometrics" by J. Fan, *Statistical Science* **20**, 347–350.
- [13] Oomen, R.A.A. (2005). Properties of bias corrected realized variance in calendar time and business time, *Journal of Financial Econometrics* **3**, 258–272.
- [14] Podolskij, M. & Vetter, M. (2006). Estimation of volatility functionals in the simultaneous presence of

microstructure noise and jumps, Technical Report, Ruhr-Universitat, Bochum. To appear in ¨ *Bernoulli*.

- [15] Roll, R. (1984). A simple model of the implicit bid-ask spread in an efficient market, *Journal of Finance* **39**, 1127–1139.
- [16] Zhang, L. (2006). Efficient estimation of stochastic volatility using noisy observations: a multi-scale approach, *Bernoulli* **12**, 1019–1043.
- [17] Zhang, L., Mykland, P.A. & A¨ıt-Sahalia, Y. (2005). A tale of two time scales: determining integrated volatility with noisy high-frequency data, *Journal of the American Statistical Association* **100**, 1394–1411.

JEAN JACOD
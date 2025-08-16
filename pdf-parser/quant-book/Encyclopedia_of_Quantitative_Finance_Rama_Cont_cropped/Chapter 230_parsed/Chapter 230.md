# **Gaussian Interest-Rate** Models

A major milestone in interest-rate modeling was the one-factor Gaussian mean-reverting model proposed by Vasicek [6] in 1977 for the short-term interest rate, using a time-homogeneous setup of the Ornstein-Uhlenbeck process (see Term Structure **Models**). Its analytical tractability and feasibility of effective numerical methods made the model popular among practitioners for many years. Multifactor Gaussian interest-rate models were subsequently developed as a natural extension of the Vasicek model and share these properties.

In 1990, Hull and White [3] generalized the Vasicek model to time-dependent parameters to permit fitting term structures of yields and volatilities. The instantaneous short rate  $r(t)$  for the Hull–White one-factor (HW1F) model satisfies the evolution

$$dr(t) = (\vartheta(t) - a(t)r(t)) dt + \sigma(t) dW(t) \quad (1)$$

A volatility function  $\sigma(t)$  and a mean reversion  $a(t)$ are the main parameters of the model. The drift compensator  $\vartheta(t)$  serves to fit the initial yield curve. Zero-bond and option pricing, as well as transition probabilities, are available analytically for the HW1F model, which makes it attractive not only for a calibration procedure but also for effective numerical implementations.

One of the main drawbacks of the HW1F model is the fact that yields of all maturities are functions of only one state-variable,  $r(t)$ , implying that all points on the yield curve are perfectly correlated. For financial contracts sensitive to the joint movements of multiple points on the yield curve, the HW1F model is therefore clearly inadequate. To decorrelate yields of different maturities, Hull and White [4] in 1995 proposed a two-dimensional generalization of the HW1F model, introducing a stochastic mean reversion  $u(t)$  in the short rate,

$$dr(t) = (\vartheta(t) + u(t) - ar(t)) dt + \sigma dW(t) (2)$$

$$du(t) = -a_u u(t) dt + \sigma_u dW_u(t)$$
(3)

Apart from previously defined short-rate parameters, the stochastic mean reversion  $u(t)$  has its own time-independent volatility  $\sigma_u$  and mean reversion

 $a_u$ . Nontrivial correlation between the two Brownian motions,  $\rho_u = E[dW(t) dW_u(t)]/dt$ , and the two mean reversions,  $a \neq a_u$ , guarantee nontrivial correlations between yields of different maturities.

Duffie and Kan [2] generalized the model  $(2-3)$  to an arbitrary dimension as a special case of their affine model. Here, the short-rate process is presented as a sum of correlated Gaussian mean-reverting processes,  $x_i(t)$ , and an additional deterministic function,  $\theta(t)$ , used to match the original yield curve,

$$r(t) = \sum_{i=1}^{N} x_i(t) + \theta(t)$$
 (4)

Each underlying process  $x_i(t)$  obeys the Ornstein-Uhlenbeck equation,

$$dx_i(t) = -a_i(t)x_i(t) dt + \sigma_i(t) dW_i(t) \qquad (5)$$

with correlated Brownian motions  $E[dW_i(t) dW_i(t)]$  $= C_{ii}(t) dt$ . The model's stochastic differential equations (SDEs) are understood to be in the riskneutral measure associated with the savings account numeraire  $N(t) = e^{\int_0^t ds \, r(s)}$  and the expectation operator  $E[\cdots]$ .

The Hull–White two-factor model  $(2-3)$  and the  $N = 2$  case of the symmetric form (4-5) are equivalent for  $a \neq a_u$  provided that  $a = a_1, a_u = a_2, \sigma^2 =$  $\sigma_1^2 + \sigma_2^2 + 2\rho \,\sigma_1 \,\sigma_2, \,\,\sigma_u = (a_1 - a_2)\sigma_2, \,\,\rho_u = (\sigma_1 \rho + \sigma_2)$  $\sigma_2/\sigma$ , and  $\vartheta(t) = a_1 \theta(t) + \theta'(t)$ .

### **Analytical Properties**

It is convenient to orthogonalize the Brownian motions in the model (5). For this, introduce vector-valued volatilities  $\gamma_i(t)$  with elements  $\gamma_{if}(t)$ for  $f = 1, \ldots, N$ . Also consider vector-valued Brownian motion  $dZ(t) = \{ dZ_1, dZ_2, \ldots, dZ_N \}$ with independent elements  $E[dZ_f(t) dZ_{f'}(t)] =$  $\delta_{ff'}$  dt, where  $\delta_{ij}$  is the Kronecker symbol. Now the underlying mean-reverting process (5) can be rewritten as

$$dx_i(t) = -a_i(t)x_i(t) dt + \gamma_i(t) \cdot dZ(t) \qquad (6)$$

where the dot symbol denotes the dot product  $\sum_{f=1}^{N} \gamma_{if}(t) dZ_{f}(t) = \gamma_{i}(t) \cdot dZ(t)$ . To restore the initial dynamics (5), one should identify the scalar volatility  $\sigma_i$  with the module  $|\gamma_i|$  and the correlation structure  $C_{ij}(t) = E[dW_i(t) dW_j(t)]/ dt$  with  $\gamma_i(t)$ .

 $\gamma_i(t)/|\gamma_i(t)| |\gamma_i(t)|$ . In these notations, the initial Brownian motion can be expressed as  $dW_i(t) =$  $\gamma_i(t) \cdot dZ(t)/|\gamma_i(t)|$ .

## Key Formulas

This mean-reverting Ornstein–Uhlenbeck process (6) has the solution

$$x_{i}(\tau) = e^{-\int_{t}^{\tau} a_{i}(u) du} \left(x_{i}(t) + \int_{t}^{\tau} e^{\int_{t}^{s} a_{i}(u) du} \gamma_{i}(s) \cdot dZ(s)\right)$$
(7)

provided that its value at time  $t$  is fixed. Conditional moments of the  $x_i$  are easily shown to be

$$E[x_i(\tau) | x_i(t) = y_i] = e^{-\int_t^{\tau} a_i(u) du} y_i \qquad (8)$$
$$\text{Cov}\Big(x_i(\tau), x_j(\tau) | x_i(t) = y_i, x_j(t) = y_j\Big)$$

$$= \int_{t}^{\tau} e^{-\int_{s}^{\tau} (a_{i}(u)+a_{j}(u)) du} \times \gamma_{i}(s) \cdot \gamma_{j}(s) ds \quad (9)$$

Let  $P(t, T)$  be the time t price of a discount bond maturing at time  $T$ , and define instantaneous forward rates by  $f(t,T) = -\partial \ln P(t,T)/\partial T$ . In the model  $(4-6),$ 

$$P(t,T) = E\left[e^{-\int_t^T r(\tau) d\tau} | F_t\right] = e^{-\int_t^T \theta(\tau) d\tau}$$
$$\times E\left[e^{-\sum_i \int_t^T x_i(\tau) d\tau} | F_t\right] \tag{10}$$

which can be evaluated as the processes  $x_i$  are Gaussian. Indeed, it is easily established that

$$dP(t,T)/P(t,T) = r(t) dt - \sum_{i} \alpha_{i}(t,T)\gamma_{i}(t) \cdot dZ(t),$$
  
$$\alpha_{i}(t,T) \equiv \int_{t}^{T} ds \, e^{-\int_{t}^{s} a_{i}(u) du} \tag{11}$$

where we have used the fact that the drift of  $dP(t,T)/P(t,T)$  must be  $r(t)$  in the risk-neutral measure. Differentiating the SDE for  $\ln P(t, T)$  over  $T$ , the forward rate dynamics emerge as

$$df(t,T) = \sum_{i} e^{-\int_{t}^{T} a_{i}(u) du} \gamma_{i}(t)$$
$$\cdot dZ(t) + \mu(t,T) dt \qquad (12)$$

where we have defined

$$\mu(t,T) = \sum_{i,j} e^{-\int_t^T a_i(u) du} \alpha_j(t,T) \gamma_i(t) \cdot \gamma_j(t)$$
(13)

Integrating the forward rate SDE leads to

$$f(t,T) = f(0,T) + \sum_{i} e^{-\int_{t}^{T} a_{i}(u) du} x_{i}(t)$$
$$+ \int_{0}^{t} \mu(\tau,T) d\tau \qquad (14)$$

so forward rates are clearly Gaussian. For a general approach to the forward rates evolution, see Heath–Jarrow–Morton Approach. Integrating equation  $(14)$  yields the discount bond reconstitution formula

$$P(t,T) = \frac{P(0,T)}{P(0,t)} e^{-\sum_{i} \alpha_{i}(t,T) x_{i}(t) - \frac{1}{2} \int_{0}^{t} (v(\tau,T) - v(\tau,t)) d\tau}$$
(15)

where  $v(t,T)$  is the instantaneous variance of  $dP(t,T)/P(t,T)$ , that is,  $v(t,T) = \left| \sum_{i} \alpha_{i}(t,T) \right|$  $\gamma_i(t)$ <sup>2</sup>. Note that equation (15) demonstrates that the entire discount curve at time  $t$  can be computed from the N Markov state-variables  $x_i(t)$ ,  $i = 1, \ldots, N$ . Also note that, from equation  $(14)$ ,

$$r(t) \equiv f(t,t) = f(0,t) + \sum_{i} x_i(t) + \int_0^t \mu(\tau,t) \, d\tau$$
(16)

which immediately establishes the drift  $\theta(t)$  in formula (4) to be  $\theta(t) = f(0, t) + \int_0^t \mu(\tau, t) d\tau$ .

Finally, we present the covariance structure for the forward rates.

$$\operatorname{Cov}(\operatorname{d}f(t,T),\operatorname{d}f(t,T')) = \frac{E[\operatorname{d}f(t,T)\operatorname{d}f(t,T')]}{\operatorname{d}t}$$

$$= \sum_{i,j} e^{-\int_t^T a_i(u) du - \int_t^{T'} a_j(u) du} \gamma_i(t) \cdot \gamma_j(t) \qquad (17)$$

from which one can obtain two important financial quantities: forward rate variance  $V_{\rm F}(t,T)$  and correlation between two forward rates  $C_{\rm F}(t, T, T')$ , or

$$V_{\rm F}(t,T) = \frac{E[\,\mathrm{d}f(t,T)\,\mathrm{d}f(t,T)]}{\mathrm{d}t}$$
$$= \sum_{i,j} \mathrm{e}^{-\int_t^T (a_i(u) + a_j(u))\,\mathrm{d}u}$$
$$\times \gamma_i(t) \cdot \gamma_j(t) \tag{18}$$

$$C_{\rm F}(t,T,T') = \frac{\text{Cov}(\text{d}f(t,T),\text{d}f(t,T'))}{\sqrt{V_{\rm F}(t,T)V_{\rm F}(t,T')}} \tag{19}$$

#### European Option Prices

Consider a general European payer swaption with exercise date  $T_0$  and payment dates  $T_1, \ldots, T_N$ . For a fixed rate  $K$ , the swaption payoff is

$$\Pi(T_0) = \left(1 - P(T_0, T_N) - K \sum_{n=1}^N \delta_n P(T_0, T_n)\right)^+ \n$$
(20)

where  $\delta_n$  is a day count faction for a period starting at  $T_{n-1}$  and ending at  $T_n$ .

Defining discounted bonds as  $R(t, T) = P(t, T) /$  $P(t, T_0)$ , the time zero value of the swaption can be written as

$$C = P(0, T_0) E_0 \left[ \left( \frac{\Pi(T_0)}{P(t, T_0)} \right)^+ \right] = P(0, T_0) E_0$$
$$\times \left[ \left( 1 - R(T_0, T_N) - K \sum_{n=1}^N \delta_n R(T_0, T_n) \right)^+ \right] \tag{21}$$

where  $E_0[\cdots]$  denotes expectation operator in the  $T_0$ -forward measure, that is, the measure associated with a numeraire of  $N_0(t) = P(t, T_0)/P(0, T_0)$  (see **Forward and Swap Measures**). As  $R(t, T)$  must be a martingale in the  $T_0$ -forward measure, equation (11) shows that

$$dR(t,T) = -R(t,T)\Sigma(t,T) \cdot dZ_0(t) \qquad (22)$$

where  $Z_0(t)$  is a Brownian motion in the  $T_0$ -forward measure and  $\Sigma(t, T)$  is a vector log-volatility

$$\Sigma(t,T) \equiv \sum_{i} e^{\int_{0}^{t} a_{i}(u) du} \gamma_{i}(t) \int_{T_{0}}^{T} ds \ e^{-\int_{0}^{s} a_{i}(u) du}$$
(23)

A solution for the discounted bonds can be easily written as

$$R(t, T_n) = \frac{P(0, T_n)}{P(0, T_0)} e^{-Y_n(t) - 1/2V_n(t)}$$
(24)

where we have denoted Gaussian processes  $Y_n(t) =$  $\int_0^t \Sigma(\tau, T_n) \cdot dZ_0(\tau)$  and its variance,  $V_n(t) = \int_0^t |\Sigma(\tau, T_n)|^2 d\tau$ . Note that the processes  $Y_n$  can be presented as a linear combination of the driving processes  $x_i$ ,

$$Y_n(t) = \sum_i \beta_i(T_n) x_i(t) \text{ for}$$
  
$$\beta_i(T_n) = \int_{T_0}^{T_n} ds \ e^{-\int_0^s a_i(u) \ du}$$
(25)

Substituting solution  $(24)$  into the price formula  $(21)$ , we obtain

$$C = P(0, T_0) E_0 \left[ \left( 1 - \sum_{n=1}^{N} e^{A_n - Y_n(T_0)} \right)^{+} \right] \quad (26)$$

where we have denoted  $A_N = \ln((1 + K \delta_N))$  $P(0, T_N)/P(0, T_0) - 1/2V_N(T_0)$  and  $A_n = \ln(K \delta_n)$  $P(0, T_n)/P(0, T_0) - 1/2V_n(T_0)$  for  $n = 1, ...,$  $N - 1$ .

For the case where  $N = 1$ , that is when our swaption is really a caplet, equation (26) can be solved in closed form

$$C_{1} = P(0, T_{0}) \Phi\left(-\frac{A_{1}}{\sqrt{V_{1}(T_{0})}} + \frac{\sqrt{V_{1}(T_{0})}}{2}\right)$$
$$- (1 + K \delta_{1}) P(0, T_{1})$$
$$\times \Phi\left(-\frac{A_{1}}{\sqrt{V_{1}(T_{0})}} - \frac{\sqrt{V_{1}(T_{0})}}{2}\right) \qquad (27)$$

where  $\Phi(x)$  is the cumulative Gaussian distribution function and  $A_1 = \ln((1 + K \delta_1) P(0, T_1)/P(0, T_0))$  $-1/2V_1(T_0)$ .

For the case of a regular multiperiod swaption, we can rely on the trick in Jamshidian [5]. It is based on the observation that, for a continuous stochastic variable  $X$  taking values on the whole real axis, the following equation

$$E\left[\left(1 - \sum_{n=1}^{N} e^{A_{n} - B_{n}X}\right)^{+}\right]$$
  
=  $E\left[\left(1 - \sum_{n=1}^{N} e^{A_{n} - B_{n}X}\right) 1_{X > x_{0}}\right]$  (28)

holds for barrier level  $x_0$  satisfying  $1 = \sum_{n=1}^{N} e^{A_n - B_n x_0}$ , provided that coefficients  $B_n \ge 0$  and at least one coefficient  $B$  is strictly positive. For Gaussian variable  $V$  with zero mean and variance  $v$ , we have

$$E\left[\left(1 - \sum_{n=1}^{N} e^{A_n - B_n X}\right)^{+}\right] = \Phi\left(-\frac{x_0}{\sqrt{v}}\right)$$
$$-\sum_{n=1}^{N} e^{A_n + 1/2B_n^2 v} \Phi\left(-\frac{x_0}{\sqrt{v}} - B_n \sqrt{v}\right) \quad (29)$$

For the one-factor case, the Jamshidian trick applies directly to equation (26) and leads to a closed-form swaption pricing formula involving a simple root-search for the trigger level  $x_0$ . For two-factor models, where  $Y_n(T_0) = \beta_1(T_n) x_1(T_0) +$  $\beta_2(T_n)$   $x_2(T_0)$ , defines Gaussian stochastic variables  $X_1 = x_1(T_0)$  and  $X_2 = x_2(T_0)$  with known covariance matrix by formula (9). To integrate the option price (26) over Gaussian  $X_1$  and  $X_2$ , one can compute analytically the conditional-to- $X_1$  average

$$E_0\left[\left(1-\sum_{n=1}^N e^{A_n-Y_n(T_0)}\right)^+\,\Big|\,X_1\right] \qquad (30)$$

using the Jamshidian lemma, and then do the numerical integration over the Gaussian variable  $X_1$ . The first step is indeed possible since the variable  $X_2$  conditional to  $X_1$  is normally distributed, and the exponents in the option formula  $(35)$  depend linearly on the variable  $X_2$  as in expression (29). More details can be found in, for instance, [1].

If the exact option pricing algorithm is slow for concrete applications, or if the number of model factors is more than two, one can come up with a purely

analytical approximation<sup>a</sup> in the so-called *swap mea*sure (see Forward and Swap Measures). Namely, introduce a swap level  $L(t) = \sum_{n=1}^{N} \delta_n P(t, T_n)$  of and associate the swap measure with the numeraire  $N_S(t) = L(t)/L(0)$  equipped with Brownian motion  $dZ_S$  and corresponding expectation operator  $E_S[\cdots]$ . Then, a swap rate,

$$S(t) = \frac{P(t, T_0) - P(t, T_N)}{\sum_{n=1}^{N} \delta_n P(t, T_n)} = \frac{P(t, T_0) - P(t, T_N)}{L(t)}$$
(31)

is a martingale in the swap measure. The option price written in the swap measure reduces to a simple expression,  $C(T_0) = L(0) E_S[(S(T_0) - K)^{+}].$ The swap rate SDE can be easily written,

$$dS(t) = \sum_{i} \frac{\partial S(t)}{\partial x_i(t)} \gamma_i(t) \cdot dZ_S(t) \qquad (32)$$

The partial swap derivatives  $d_i(t, x(t)) \equiv \partial S(t) /$  $\partial x_i(t)$  can be calculated using the zero-bond solution (15),  $\partial P(t,T)/\partial x_i(t) = -\alpha_i(t,T)P(t,T)$ .

Given that the forward rates are here Gaussian, it is natural to assume that the swap rates are as well, approximating derivatives with their value for the underlying rates at the origin, that is  $d_i(t, x(t)) \simeq$  $d_i(t, 0)$ . This approximation resembles the freezing technique of low-variance processes used for swaption pricing in Libor market models by many authors (see LIBOR Market Model).

Define  $v = \int_0^{T_0} \left| \sum_i d_i(t, 0) \gamma_i(t) \right|^2 dt$ . Then the swaption price for the Gaussian approximation of the swap rate,

$$dS(t) \simeq \sum_{i} d_{i}(t, 0) \gamma_{i}(t) \cdot dZ_{S}(t) \qquad (33)$$

can be easily written

$$C = L(0) E_S[(S(T_0) - K)^+] \simeq L(0)$$
$$\times \left( (S(0) - K) \Phi\left(\frac{S(0) - K}{\sqrt{v}}\right) + \sqrt{v} \Phi'\left(\frac{S(0) - K}{\sqrt{v}}\right) \right) \tag{34}$$

## **Numerical Methods**

Given available transition probabilities for the model, one can apply lattice methods on the basis of the conditional expectation calculus via convolution with the Gaussian kernel for the pricing of general payouts. Of course, other lattice techniques-such as finite differences-can be successfully used as well.

When the payout is path-dependent or the dimension of the model is beyond, say, 3 or 4, lattice methods must be replaced by Monte Carlo simulation; path simulation in the Monte Carlo method is straightforward and involves making Gaussian draws with moments computed from the conditional expectations  $(8-9)$ .

## Properties

We cover in detail the two-factor case,  $r(t) =$  $x_1(t) + x_2(t) + \theta(t)$  frequently used in the financial industry. In practical applications, the model correlation between the two Brownian motions  $\rho(t)$  =  $E[dW_1(t) dW_2(t)]/dt$  in the notation (5), or the cosine of the angle between the two volatility vectors  $\rho(t) = \gamma_1(t) \cdot \gamma_2(t)/|\gamma_1(t)| |\gamma_2(t)|$  in the notations (6), typically takes highly negative values,  $\rho(t) \sim -0.9$ . The two mean reversions are often radically different  $a_1(t) \sim 0.5$  and  $a_2(t) \sim 0.05$  with the volatilities  $\sigma_1(t) = |\gamma_1(t)| \sim 0.005$  and  $\sigma_2(t) =$  $|\gamma_2(t)| \sim 0.01$ 

#### Volatility Hump and Correlations

For illustration, we consider in more detail the twofactor model with time-independent parameters. The forward rates variance (18) simplifies to

$$V_{\rm F}(t,T) = e^{-2a_1(T-t)}\sigma_1^2 + 2e^{-(a_1+a_2)(T-t)}$$
$$\times \sigma_1 \sigma_2 \rho + e^{-2a_2(T-t)}\sigma_2^2 \tag{35}$$

For positive correlation  $\rho$ , the variance is a monotonous function of  $T - t$ , although, for negative  $\rho$ , it can give the volatility hump observed on the market, see [1] for details.

In our two-dimensional model, the forward rate  $f(t, T)$  has instantaneous volatility,

$$\sigma(t,T) = e^{-(T-t)a_1} \gamma_1 + e^{-(T-t)a_2} \gamma_2 \tag{36}$$

obtained from the general formula (12). The correlation between two forward rates  $f(t, T)$  and  $f(t, T')$ can be computed from equation  $(19)$  as

$$C_{\rm F}(t,T,T') = \frac{\sigma(t,T) \cdot \sigma(t,T')}{|\sigma(t,T)| |\sigma(t,T')|} \tag{37}$$

We notice that the correlation is one when  $a_1 = a_2$ , a result of the fact that the volatilities for  $f(t, T)$  and  $f(t, T')$  are colinear in this case.

#### Volatility Smile

Swap rates in the Gaussian model are, as we have seen, nearly Gaussian, irrespective of parameter choice. As such, there is essentially no way to control the volatility skew implied by the model, which is often more steeply downward-sloping than marketobserved smiles. Consequently, some care must be taken when applying the model to smile-sensitive instruments (see Markovian Term Structure Models).

#### Calibration

Practitioners typically use two- and three-factor Gaussian models. For four factors and more, pricing of an exotic instrument may become too time consuming.

A standard approach to the two-factor model calibration includes the following steps. First, we fix the time-independent correlation to a highly negative value or calibrate it to average historical correlations between forward rates by inversion of the correlation formula (19). Second, we calibrate the time-dependent volatilities and time-independent mean reversions<sup>b</sup> to European options. The calibration options are often taken at-the-money, which reflects the absence of control of the skew and smile. The time-dependent parameters are typically considered as step-wise constant between option exercise dates. One can also use specially parameterized volatility curves, for example, having a hump form. Another popular calibration technique maintains a fixed ratio between the time-dependent volatilities,  $\sigma_1(t)/\sigma_2(t) = \text{const.}$ 

The calibration is typically done using a numerical global optimizer to fit the model option prices to the market prices. The model option prices are calculated analytically, see the section European Option Prices. For fixed mean reversions, one can also use a bootstrap in option exercise dates for the step wise constant volatilities calibration.

## **Acknowledgments**

The author is indebted to Leif Andersen, Vladimir Piterbarg, and Jesper Andreasen for numerous discussions he had with them and their help with references. He is also grateful to Leo Mizrahi, Maria Belyanina, and his NumeriX colleagues, especially, to Greg Whitten, Serguei Issakov, Nicolas Audet, Meng Lu, Serguei Mechkov, and Patti Harris, for their valuable comments on the article.

## **End Notes**

a*.* Thanks to Leif Andersen and Vladimir Piterbarg for suggesting this approach.

b*.* Time-dependence in mean reversion is often avoided as it implies nonstationary behavior of the shape of the volatility term structure.

## **References**

[1] Brigo, D. & Mercurio, F. (2001). *Interest Rate Models, Theory and Practice*. Springer Finance.

- [2] Duffie, D. & Kan, R. (1996). A yield-factor model of interest rates, *Mathematical Finance* **6**(4), 379–406.
- [3] Hull, J. & White, A. (1990). Pricing interest-rate derivative securities, *The Review of Financial Studies* **3**(4), 573–592.
- [4] Hull, J. & White, A. (1994). Numerical procedures for implementing term structure models II: two-factor models, *Journal of Derivatives* **2**, 37–47.
- [5] Jamshidian, F. (1989). An exact bond option formula, *Journal of Finance* **44**, 205–209.
- [6] Vasicek, O. (1977). An equilibrium characterization of the term structure, *Journal of Financial Economics* **5**(2), 177–188.

## **Related Articles**

**Bermudan Swaptions and Callable Libor Exotics**; **Forward and Swap Measures**; **Heath–Jarrow– Morton Approach**; **LIBOR Rate**; **LIBOR Market Model**; **Markovian Term Structure Models**; **Term Structure Models**.

ALEXANDRE V. ANTONOV
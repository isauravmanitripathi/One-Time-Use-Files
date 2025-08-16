# **Heston Model**

In the class of stochastic volatility models (*see* **Stochastic Volatility Models**), Heston's is probably the most well-known model. The model was published in 1993 by S. Heston in his seminal article the title of which readily reveals much of its popularity, *A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options*. It is probably the only stochastic volatility model for equities which both allows very efficient computing of European option prices and fits reasonably well to market data in very different conditions.

In fact, the model was used successfully (in the sense explained below) during the boom of the end of the 1990s, in the brief recession 2001, in the very low volatility regime until 2007, and it still performed well during the very volatile period of late-2008.

However, the model also has several questionable properties: critics point out that its inherent structure as a square-root diffusion does not reflect statistical properties seen in real market data. For example, typical calibrated parameters allow the instantaneous volatility of the stock to become zero with a positive probability. From a practical point of view, the most challenging property of Heston's model is the interdependence of its parameters and the resulting inability to give these parameters a real idiosyncratic meaning. One example is the fact that moving the term structure of volatility has an impact on the shape of the implied volatility skew. This means that traders who use this model will have to have a very a good understanding of the dynamics of the model and the interplay between its parameters.

Other stochastic volatility models with efficient pricing methods for European options are: SABR, Schobel–Zhou or Hull–White model (*see* **Hull–White Stochastic Volatility Model**) and Lewis' "3/2-model" presented in Lewis' book [13]. The *n*-dimensional extension of Heston's model is the class of affine models [9]. Related are Levy' based models that can also be computed efficiently (*see* **Time-changed Levy Process ´** ). The most natural model that is used frequently but which actually does not allow efficient pricing of Europeans is a lognormal model for instantaneous volatility.

# **Model Description**

If we assume a prevailing instantaneous interest rate of *r* = *(rt)t*<sup>≥</sup><sup>0</sup> and a yield from holding a stock of *µ* = *(µt)t*≥0, then Heston's model is given as the unique strong solution *Z* = *(St, vt)t*<sup>≥</sup><sup>0</sup> of the following stochastic differential equation (SDE):

$$\begin{aligned} \mathrm{d}v_t &= \kappa (\theta - v_t) \, \mathrm{d}t + \sigma \sqrt{v_t} \, \mathrm{d}W_t \\ \mathrm{d}S_t &= S_t \left( r_t - \mu_t \right) \, \mathrm{d}t + S_t \sqrt{v_t} \, \mathrm{d}B_t \end{aligned} \tag{1}$$

with starting values spot *S*<sup>0</sup> *>* 0 and "Short Vol" <sup>√</sup>*v*<sup>0</sup> *<sup>&</sup>gt;* 0. In this equation, *<sup>W</sup>* and *<sup>B</sup>* are two standard Brownian motions with a Correlation of *ρ* ∈ *(*−1*,* +1*)*. The model is usually specified directly under a risk-neutral measure.

This Correlation together with the "Vol Of Vol" *σ* ≥ 0 can be thought of being responsible for the skew. This is illustrated in Figure 1: Vol Of Vol controls the volume of the smile and Correlation and its "tilt". A negative Correlation produces the desired downward skew of implied volatility. It is usually calibrated to a value around −70%.

The other parameters control the term structure of the model: in Figure 2, the impact of changing "Short Vol" <sup>√</sup>*v*<sup>0</sup> <sup>≥</sup> 0, "Long Vol" <sup>√</sup>*<sup>θ</sup>* <sup>≥</sup> 0, and "Reversion Speed" *κ >* 0 on the term structure of at-the-money (ATM) implied volatility is illustrated. It can be seen that Short Vol lives up to its name and controls the level of the short-date implied volatilities, whereas Long Vol controls the long end. Reversion Speed controls the skewness or "decay" of the curve from the Short Vol level to the Long Vol level.

This inherent mean-reversion property of Heston's stochastic volatility around a long-term mean <sup>√</sup>*<sup>θ</sup>* is one of the important properties of the model. Real market data are often mean-reverting, and it also makes economic sense to assume that volatility is not unbounded in its growth as, for example, a stock price process is. In historic data, the "natural" level of mean-reversion is often seen to be itself a mean-reverting process as Fouque *et al.* [10] have shown. Some extensions of Heston in this direction are discussed below.

## *Parameter Interdependence*

Before we proceed, a note of caution: the above distinction of the parameters by their effect on

![](_page_1_Figure_1.jpeg)

**Figure 1** Stylized effects of changing Vol Of Vol and Correlation in Heston's model on the one-year implied volatility. The Heston parameters are *v*<sup>0</sup> = 15%2, *θ* = 20%2, *κ* = 1, *ρ* = −70%, and *σ* = 35%

![](_page_1_Figure_3.jpeg)

**Figure 2** The effects of changing Short Vol (a), Long Vol (b), and Reversion Speed (c) on the ATM term structure of implied volatilities. Each graph shows the volatility term structure for 12 years. The reference Heston parameters are *v*<sup>0</sup> = 15%2, *θ* = 20%2, *κ* = 1, *ρ* = 70%, and *σ* = 35%

term structure and strike structure, was made for illustration purposes only: in particular, *κ* and *σ* are strongly interdependent if the model is used in the form (1).

This is one of the most serious drawbacks of Heston's model since it means that a trader who uses it to risk-manage a position cannot independently control the risk with the five available parameters, but has to understand very well their interdependency. For example, to hedge, say, convexity risk in strike direction of the implied volatility surface, the trader will also have to deal with the skew risk at the same time since in Heston, there is no one parameter to control either: convexity is mainly controlled by Vol Of Vol, but the effect of Correlation on skew depends on the level of Vol Of Vol, too. Moreover, changes to the short end volatility skew will always affect the long-term skew. A similar strong codependency exists between Vol of Vol and Reversion Speed; as pointed out in [14], some of the strong interdependence between Vol Of Vol and Reversion Speed can be alleviated by using the alternative formulation

$$\mathrm{d}v_t = (\theta - v_t)\kappa \,\mathrm{d}t + \tilde{\sigma}\sqrt{v_t}\sqrt{\kappa} \,\mathrm{d}W_t \qquad (2)$$

In this parametrization, the new Vol Of Vol and reversion speed are much less interdependent, which stabilizes results of daily calibration to market data substantially. Mathematically, this parametrization much more naturally defines  $\kappa$  as the "speed" of the equation.

Such complications are a general issue with stochastic volatility models: since such models attempt to describe an unobservable, rather theoretical quantity (instantaneous variance), they do not produce very intuitive behavior when looked at through the lens of the observable measure of "implied volatility". That said, implied volatility itself or, rather, its interpolations are also moving on a daily basis. This indicates that natural parameters such as convexity and skew of implied volatility might be a valuable tool for feeding a stochastic volatility model, but it is unreasonable to keep them as constant parameters inside the model.

# **Pricing European Options**

Heston's popularity is probably mainly derived from the fact that it is possible to price European options on the stock price  $S$  using semi-closed-form Fourier transformation, which in turn allows rapid calibration of the model parameters to market data. "Calibration" here means to infer values for the five unobservable parameters  $\sqrt{v_0}, \sqrt{\theta}, \kappa, \sigma, \rho$  from market data by minimizing the distance between the models' European option prices and observed market prices.

We focus on the call prices. Following Carr and Madan [7], we price them *via* Fourier inversion.<sup>a</sup> The call price for a relative strike  $K$  at maturity  $T$  is given as

$$\mathbb{C}(T,K) := \mathrm{DF}(T)\mathbb{E}\left[ (S_T - K F_T)^+ \right] \qquad (3)$$

where DF(T) represents the discount factor and  $F_T$ is the forward of the stock. Since the call price itself is not an  $L^2$ -function in K, we define a "dampened call"

$$c(T,k) := \frac{\mathrm{e}^{\alpha k}}{\mathrm{DF}(T)F_T} \mathbb{C}(T,\mathrm{e}^k) \tag{4}$$

for an  $\alpha > 0$ ,<sup>b</sup> for which its characteristic function  $\psi_t(z;k) := \int_{\mathbb{R}} e^{ikz} c(t,k) dk$  is well defined and given as

$$\psi_t(z;k) = \frac{\varphi_t (k - \mathrm{i}(\alpha + 1))}{(\mathrm{i}k + \alpha)(\mathrm{i}k + \alpha + 1)} \tag{5}$$

The function  $\varphi_t(z) := \mathbb{E}[\exp\{iz \log S_t/F_t\}]$  is the characteristic function of  $X_t := \log S_t / F_t$ . Since Heston belongs to the affine model class, its characteristic function has the form

$$\varphi_t(z) = \mathrm{e}^{-v_0 A_t - m B_t} \tag{6}$$

with (cf. [14])

$$A_{t} := \frac{\alpha + ae^{\gamma t}}{\beta + be^{\gamma t}} \quad \text{and}$$

$$B_{t} := \tilde{\kappa} \frac{\alpha b\gamma t + (a\beta - \alpha b)\log\frac{\beta + be^{\gamma t}}{\beta + b}}{\beta b\gamma} \qquad (7)$$

where  $\mu := (iz + z^2)/2$ ,  $\tilde{\kappa} := \kappa - \rho iz\sigma$ ,  $\gamma :=$  $-\sqrt{2\mu\sigma^2+\tilde{\kappa}^2}$ ,  $a:=-2\mu$ ,  $\alpha:=2\mu$ ,  $b:=-\tilde{\kappa}+\gamma$ and  $\beta := \tilde{\kappa} + \gamma$ .

We can then price a call on  $X$  using

$$\mathbb{C}(T, K) = \text{DF}(T)F_T \frac{e^{-\alpha \ln(K)}}{\pi}$$
$$\times \int_0^\infty e^{-iz \ln(K)} \psi_t(z; \ln(K)) dz \quad (8)$$

The method also lends itself to Fast Fourier Transform if a range of option prices for a single maturity is required.

Similarly, various other payoffs can be computed very efficiently with the Fourier approach, for example, forward started vanilla options, options on integrated short variance, and digital options.

# Time-Dependent Parameters

Moreover, for most of these products—and most importantly, plain European options—it is very straightforward to extend the model to time-dependent, piece-wise constant parameters. This is briefly

![](_page_3_Figure_1.jpeg)

**Figure 3** Heston (a) without and (b) with time-dependent parameters fitted to STOXX50E for maturities from 1m to 5y. The introduction of time dependency clearly improves the fit

discussed in [14]. It improves the fit of the model to the market prices markedly, cf. Figure 3.

However, it should be noted that by introducing piecewise constant time-dependent parameters, we lose much of a model's structure. It is turned from a time-homogeneous model which "takes a view" on the actual evolution of the volatility *via* its SDE into a kind of an arbitrage-free interpolation of market data: if calibrated without additional constraints to ensure smoothness of the parameters over time, this

is reflected in large discrepancies of the parameter values for distinct periods. For example, the excellent fit of the time-dependent Heston model in Figure 3 is achieved with the following parameter values (short volatility  $\sqrt{\zeta_0}$  was 15.0%):

|                          | 6m        | 1v        | 3v        | $\infty$  |
|--------------------------|-----------|-----------|-----------|-----------|
| Long Vol $\sqrt{\theta}$ | 20.7%     | 23.6%     | 36.1%     | 46.5%     |
| Reversion                | 5.0       | 3.2       | 0.4       | 0.3       |
| Speed $\kappa$           |           |           |           |           |
| Correlation $\rho$       | $-55.2\%$ | $-70.9\%$ | $-80.1\%$ | $-69.4\%$ |
| Vol Of Vol $\sigma$      | 78.7%     | 81.5%     | 35.3%     | 60.0      |
|                          |           |           |           |           |

The increased number of parameters also makes it more difficult to hedge in such a model in practice; even though both Heston and the time-dependent Heston models create complete markets, we will always need to additionally protect our position against moves in the parameter values of our model. Just as for Vega in Black and Scholes, this is typically done by computing "parameter greeks" and neutralizing the respective sensitivities. Clearly, the more the parameters that are involved, and the less stable these are, this "parameter hedge" becomes less and less reliable.

## Mathematical Drawbacks

The underlying mathematical reason for the relative tractability of Heston's model is that  $v$  is a squared Bessel process, which is well understood and reasonably tractable. In fact, a statistical estimation on S&P 500 by Aït-Sahalia and Kimmel [1] of  $\alpha \in [1/2, 2]$ in the extended model

$$\mathrm{d}v_t = \kappa(\theta - v_t)\,\mathrm{d}t + \sigma v_t^{\alpha}\,\mathrm{d}W_t^1\tag{9}$$

has shown that, depending on the observation frequency, a value around 0.7 would probably be more adequate (see Econometrics of Diffusion Models). What is more, the square-root volatility terms mean that unless

$$2\kappa\theta \ge \sigma^2 \tag{10}$$

the process  $v$  can reach zero with nonzero probability. The crux is that this condition is regularly violated if the model is calibrated freely to observed market data. Although a vanishing short variance is not a problem in itself (after all, a variance of zero simply means absence of trading activity), it makes

![](_page_4_Figure_1.jpeg)

Probability density of Heston's short vol for a 20%

**Figure 4** This graphs shows the density of *vt* for one, three and six months for the case where condition (10) is satisfied (above) or not (below). Apart from Vol Of Vol, the parameters were *v*<sup>0</sup> = 15%2, *θ* = 20%2 and *κ* = 1

numerical approximations more complicated. In a Monte Carlo simulation, for example, we have to take the event of *v* being negative into account. The same problem appears in a partial differential equation (PDE) solver: Heston's PDE becomes degenerate if Short Vol hits zero. A violation of Equation (10) also implies that the distribution of short variance *Vt* at some later time *t* is very wide, cf. Figure 4.

Additionally, if Equation (10) does not hold, then the stock price *S* may fail to have a second moment if the Correlation is not negative enough in the sense detailed in proposition 3.1 in [2] (*see* **Moment Explosions** for more details). Again, this is not a problem from a purely mathematical point of view, but it makes numerical schemes less efficient. In particular, Monte Carlo simulations perform much worse: although an Euler scheme will still converge to the desired value, the speed of convergence deteriorates. Moreover, we cannot safely use control variates anymore if the payoff is not bounded.

## **Pricing Methods**

Once we have calibrated the model using the aforementioned semiclosed form of solution for the European options, the question is how to evaluate complex products. At our disposal are PDEs and Monte Carlo schemes.

Since the conditional transition density of the entire process is not known, we have to revert to solving a discretization of the SDE (1) if we want to use a Monte Carlo scheme (see Monte Carlo Simulation for Stochastic Differential Equations for an overview of Monte Carlo concepts). To this end, assume that we are given fixing dates  $0 = t_0 < \cdots <$  $t_N = T$  and let  $\Delta t_i := t_{i+1} - t_i$  for  $i = 0, ..., N - 1$ . Moreover, we denote by  $\Delta W_i$  for  $i = 0, \ldots, N-1$  a sequence of independent normal variables with variance  $\Delta_i$ , and by  $\Delta B_i$  a corresponding sequence where  $\Delta B_i$  and  $\Delta W_i$  have Correlation  $\rho$ .

When using a straightforward Euler scheme, we will face the problem that  $v$  can become negative. It works well simply to reduce the volatility term of the variance to the positive part of the variance, that is, to simulate

$$v_{t_{i+1}} = v_{ti} + \kappa (\theta - v_{ti}) \Delta_i + \sigma \sqrt{v_{ti}^+} \Delta W_i \qquad (11)$$

A flaw of this scheme is that it is biased. This is overcome by using the moment-matching scheme

$$v_{t_{i+1}} = \theta \Delta t_i + \left(\theta - v_{t_i}\right) e^{-\kappa \Delta t_i} + \left(\sigma v_{t_i}^+ \sqrt{\frac{1 - e^{-2\kappa \Delta t_i}}{2\kappa}}\right) \Delta W_i \qquad (12)$$

which works well in practice. To compute the stock price, we approximate the integrated variance over  $[t_i, t_{i+1}]$  as

$$\Delta_i V := \theta \Delta t_i + \left(v_{t_i} - \theta\right) \frac{1 - e^{-\kappa \Delta t_i}}{\kappa} \tag{13}$$

and set

$$S_{t_k} := F_{t_k} \exp\left\{\sum_{i=1}^{k-1} \left\{\sqrt{\Delta_i V} \Delta B_i - \frac{1}{2} \Delta_i V\right\}\right\} \quad (14)$$

Note that this scheme is unbiased in the sense that  $\mathbb{E}[S_T] = F_T$ .

#### Heston's PDE

It is straightforward to derive the PDE for the previous model. Let

$$P_t(v, S) := DF_t(T) \mathbb{E} [F(S_T) | S_t = S, v_t = v] \quad (15)$$

be the price of a derivative with maturity  $T$  at time  $t$ . It satisfies

$$0 = r_t P_t + \partial_S P_t (r_t - \mu_t) S_t + \partial_v P_t \kappa (m - v_t)$$
  
+  $\frac{1}{2} \partial_{SS}^2 P_t S_t v_t + \frac{1}{2} \partial_{vv}^2 P_t \sigma^2 v_t + \partial_{vS}^2 P_t \rho v_t S_t$  (16)

with boundary condition  $P_T(S, v) = F(S_T)$ . To solve this two-factor PDE with a potentially degenerate diffusion term in  $\partial_{uv}^2 P_t$ , it is recommended to use a stabilized alternating direction implicit (ADI) scheme such as the one described by Craig and Sneyd [8] (see Alternating Direction Implicit (ADI) Method for a discussion on ADI).

#### **Risk Management**

Provided that we consider not only the stock price itself but also a second liquid instrument  $V$  such as a listed option as hedging instrument, stochastic volatility models are complete, that is, in theory every contingent claim  $P$  can be replicated in the sense that there are hedging strategies  $(\Delta_t, \mathcal{V}_t)_t$  such that

$$dP_t - r_t P_t dt = \Delta_t (dS_t - S_t(r_t - \mu_t) dt)$$
  
+  $\mathcal{V}_t (dV_t - r_t V_t dt)$  (17)

(see **Complete Markets** for a discussion on complete markets). In Heston's model, we can write the price process of both the derivative we want to hedge and the hedging instrument as a function of current spot level and short variance, that is,  $P_t \equiv P_t(S_t, v_t)$  and  $V_t \equiv V_t(S_t, v_t)$ . Then, the correct hedging ratios are

$$\mathcal{V}_t = \frac{\partial_v P}{\partial_v V} \quad \text{and} \quad \Delta_t = \partial_S P_t - \frac{\partial_v P}{\partial_v V} \partial_S V_t \quad (18)$$

This is the equivalent of delta hedging in Black and Scholes (see **Delta Hedging**). However, as for the latter, plain theoretical hedging will not work since the other parameters in our model, Reversion Speed, Vol of Vol, Long Vol, and potentially Correlation, will not remain constant if we calibrate our model on a daily basis. This is the effect of a change in volatility for Black and Scholes—a change of this parameter is not anticipated by the model itself and must be taken care of "outside the model".

As a result, one way to control this risk is to engage in additional parameter hedging, that is, the desk also displays sensitivities with respect to the other model parameters including, potentially, second-order exposures. Those can then be monitored on a book level and managed explicitly. The drawback of this method is that to reduce risk with respect to those parameters, a portfolio of vanilla options has to be bought whose composition can change quickly if implemented blindly.<sup>c</sup>

A second variant is to try to map standard risks of the desk such as implied volatility convexity, skewness, and so on into stochastic volatility risk by "recalibration". The idea here is that, say, the convexity parameter of the implied volatility is modified, then Heston's model is calibrated to this new implied volatility surface and the option priced off this model. The resulting change in model price is then considered the sensitivity of the option to convexity in implied volatility. This approach suffers from the fact that typical "implied vol risks" are very different from typical movements in the Heston model. For example, the standard Heston model is homogeneous so it cannot easily accommodate changes in short-term skew only.

## **Related Models**

Owing to its numerical efficiency, Heston's model is the base for many extensions. The first notable extension is Bates' addition of jumps to the diffusion process in his article [3] (see **Bates Model**). Jumps are commonly seen as a necessary feature of any risk management model, even though the actual handling of the jump risk part is far from clear.

Bates' approach can be written as follows: let  $X$ be given by

$$\begin{aligned} \mathrm{d}v_t &= \kappa (\theta - v_t) \, \mathrm{d}t + \sigma \sqrt{v_t} \, \mathrm{d}W_t \\ \mathrm{d}X_t &= X_t \sqrt{v_t} \, \mathrm{d}B_t \end{aligned} \tag{19}$$

and let

$$S_t = F_t X_t e^{\sum_{j=1}^{N_t} \xi_j - \lambda m t}$$
 (20)

where  $N_t$  is a Poisson process with intensity  $\lambda$  (see **Poisson Process**) and where  $(\xi_i)_i$  are the normal jumps of the returns of S with mean  $\mu$  and volatility v. To make sure that  $S_t/F_t$  is a martingale we stipulate that  $\mu = e^{m + \frac{1}{2}v^2} - 1$ .

Since the process  $X$  is independent of the jumps, the characteristic function of the log-stock process is the product of the separate characteristic functions. In other words, Bates' model can be evaluated using the same approach as above and is equally efficient while allowing for a very pronounced short-term skew due to the jump part.<sup>d</sup> Figure 5 shows the improvement of time-dependent Bates over time-dependent Heston.

The model has been further enhanced by Knudsen and Nguyen-Ngoc [12] who also added exponentially distributed jumps to the variance process.

#### **Multifactor Models**

Structurally, Heston's model is a member of the class of "affine models" as introduced by Duffie et al. [9]. As such, it can easily be extended by mixing in further independent square-root processes. One obvious approach presented in [14] is simply to multiply several independent Heston processes. For the two-factor case, this means to set  $S_t := F_t X_t^1 X_t^2$  where both  $X^1$ and  $X^2$  have the form (19). Jumps can be added, but to make the Fourier integration work efficiently, the processes  $X^1$  and  $X^2$  must remain independent.

The stochastic variance of the joint stock price is then simply the sum of the two separate variances,  $v^1$ and  $v^2$ , and it is intuitively assumed that one is a "short-term", fast mean-reverting process whereas the other is mean reverting slowly. Such a structure is supported by statistical evidence, cf. [10]. However, the independence of the two processes makes it very difficult to impose enough skew into this model since the effective Correlation between instantaneous variance and stock price weakens. In practice, this model is used only rarely.

A related model "Double Heston" has been mentioned by Buehler [6], which is obtained by modeling the mean variance level  $\theta$  in Heston itself as a squareroot diffusion, that is,

$$\begin{aligned} \mathrm{d}v_t &= \kappa (\theta_t - v_t) \, \mathrm{d}t + \sigma \sqrt{v_t} \, \mathrm{d}W_t \\ \mathrm{d}\theta_t &= c(m - \theta_t) \, \mathrm{d}t + v \sqrt{\theta_t} \, \mathrm{d}W_t^{\theta} \\ \mathrm{d}S_t &= S_t (r_t - \mu_t) \, \mathrm{d}t + S_t \sqrt{v_t} \, \mathrm{d}B_t \end{aligned} \tag{21}$$

![](_page_7_Figure_1.jpeg)

**Figure 5** Heston (a) and Bates (b) with time-dependent parameters fitted to STOXX50E for maturities from 1m to 5y

where *W<sup>θ</sup>* is independent of *W* and *B*. While this model has a reasonably tractable characteristic function, it also suffers from the problem that long-term skew becomes too symmetric, contrary to what is observed in the market. Such a model, however, may have applications when pricing options on variance where the skew counts less and it is more important to be able to account for some dynamics of the term *structure of variance*. Refer to [6] for an extensive discussion on this.

## *Fitted Heston*

A particular class of derivatives that has gained reasonable popularity in recent years are "Options on Variance", that is, structures whose terminal payoff depends on the realized variance of the returns of the stock over a set of business days 0 = *t*<sup>0</sup> *<* ··· *< tn* = *T* ,

$$\mathbb{RV}(T) := \sum_{i=1}^{n} \left( \log \frac{S_{t_i}}{S_{t_{i-1}}} \right)^2 \tag{22}$$

The most standard of such products is a "variance swap" (*see* **Variance Swap**), which essentially pays the actual realized annualized variance over the period in exchange for a previously agreed fair strike. This strike is usually quoted in volatility terms, that is a variance swap with maturity *T* , and strike *(T )* pays

$$\frac{252}{n}\mathbb{RV}(T) - \Sigma^2(T) \tag{23}$$

From this product, a market with options on realized variance has evolved naturally; these include capped variance swaps (mainly traded on single stocks), outright straddles on realized variance swaps, and also VIX futures and options (*see* **Realized Volatility Options**). Although there are several discussions around how best to approach the risk management of such products, a particularly useful Heston's model is the "Fitted Heston" approach introduced by Buehler [4].

The main idea here is that to price an option on realized variance in a given model, it is crucial to price correctly a variance swap itself, that is, to make sure that

$$\mathbb{E}\left[\mathbb{RV}(T)\right] = \frac{n}{252} \Sigma^2(T) \tag{24}$$

The idea of "fitting to the market", say, Heston's model (2) is now simply to force the model to satisfy this equation. First, assume that we have the term structure of the market's expected realized variance, *M(T )* = *n*<sup>2</sup>*(T )/*252 = <sup>2</sup>*(T )T* , and define *m(t)* := *∂T* |*<sup>T</sup>* <sup>=</sup>*tM(T )*. Take the original short variance of the model,

$$\mathrm{d}v_t = (\theta - v_t)\kappa \,\mathrm{d}t + \sigma \sqrt{v_t} \sqrt{\kappa} \,\mathrm{d}W_t \qquad (25)$$

and define the new "fitted" process as

$$w_t := m(t) \frac{v_t}{\mathbb{E}\left[v_t\right]} \tag{26}$$

with the stock price as

$$dS_t = S_t(r_t - \mu_t) dt + S_t \sqrt{w_t} dB_t \qquad (27)$$

This now reprices all variance swaps automatically in the sense (24). Note that this method does not at all depend on using Heston's model and can be applied to any stochastic volatility model as long as the expectation of instantaneous variance is known.

As pointed out in [6], this model is naturally very attractive from a risk-management point of view if the input *M* is computed on the fly within the risk management system. In this case, the risk embedded in the variance swap level (called *VarSwapDelta*) is automatically reflected back in the standard implied volatility risk, and the underlying stochastic volatility model is used purely to control skew and convexity around the variance swap backbone.e Further practical considerations and the impact of jumps are discussed by Buehler in [5].

# **End Notes**

a*.* In his original paper [11], Heston suggested a numerically more expensive approach via numerical integration that is twice as slow but still much faster than the same computation for most other models. The approach to price with Fourier inversion is due to Carr and Madan [7]; the interested reader finds more details on the subject in Lewis's book [13].

b*.* See [7] for a discussion on the choice of *α*.

c*.* Bermudez *et al.* discuss one approach to find such portfolios [14].

d*.* In practice, calibrating all parameters (stochastic volatility plus jumps) together is relatively unstable since the two parts play similar roles for the short-term options. It is therefore customary to fix the jump parameters themselves or to calibrate them separately to very short-term options. e*.*

Usually, the parameters *v*<sup>0</sup> and *θ* are fixed to some "usual level" such as 20%. Then, they do not need to be calibrated anymore and, in addition, *σ* retains some comparability to the standard Heston model.

# **References**

- [1] A¨ıt-Sahalia, Y. & Kimmel, R. (2004). *Maximum Likelihood Estimation of Stochastic Volatility Models*, NBER Working Paper No. 10579, June 2004.
- [2] Andersen, L. & Piterbarg, V. (2007). Moment explosions in stochastic volatility models, *Finance and Stochastics* **11**(1), 20–50.

- [3] Bates, D. (1996). Jumps and stochastic volatility: exchange rate process implicit in the Deutschemark options, *Review of Financial Studies* **9**(1), 69–107.
- [4] Buehler, H. (2006). Consistent variance curve models, *Finance and Stochastics* **10**(2), 178–203.
- [5] Buehler, H. (2006). Options on variance: pricing and hedging, *Presentation, IQPC Volatility Trading Conference*, London November 28th, 2006, http://www. quantitative-research.de/dl/IQPC2006-2.pdf
- [6] Buehler, H. (2006). *Volatility Markets: Consistent Modeling, Hedging and Practical Implementation*, PhD thesis TU Berlin, http://www.quantitative-research.de/dl/ HansBuehlerDiss.pdf
- [7] Carr, P. & Madan, D. (1999). Option pricing and the Fast Fourier Transform, *Journal of Computational Finance* **2**(4), 61–73. Summer.
- [8] Craig, I.J.D. & Sneyd, A.D. (1988). An alternatingdirection implicit scheme for parabolic equations with mixed derivatives, *Computers and Mathematics with Applications* **16**(4), 341–350.
- [9] Duffie, D., Pan, J. & Singleton, K. (2000). Transform analysis and asset pricing for affine jump-diffusions, *Econometrica* **68**, 1343–1376.
- [10] Fouque, J.-P., Papanicolaou, G. & Sircar, K. (2000). *Derivatives in Financial Markets with Stochastic Volatility*, Cambridge Press.
- [11] Heston, S. (1993). A closed-from solution for option with stochastic volatilty with applications to bond and currency options, *Review of Financial Studies* **6**(2), 327–343.
- [12] Knudsen, T. & Nguyen-Ngoc, L. (2000). The Heston model steps further Deutsche Bank Quantessence **1**(7) https://www.dbconvertibles.com/dbquant/quantessence/ Vol1Issue7External.pdf
- [13] Lewis, A. (2000). *Option Valuation under Stochastic Volatility*, Finance Press.
- [14] Overhaus, M., Bermudez, A., Buehler, H., Ferraris, A., Jordinson, C., Lamnouar, A. (2006). *Equity Hybrid Derivatives*, Wiley.

# **Related Articles**

**Alternating Direction Implicit (ADI) Method**; **Bates Model**; **Complete Markets**; **Cliquet Options**; **Econometrics of Diffusion Models**; **Hedging**; **Hull–White Stochastic Volatility Model**; **Model Calibration**; **Monte Carlo Simulation for Stochastic Differential Equations**; **Moment Explosions**; **Realized Volatility Options**; **Variance Swap**.

HANS BUEHLER
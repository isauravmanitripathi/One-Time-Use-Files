# **Parisian Option**

Parisian options are barrier options that are activated or canceled—depending on the type of option—if the underlying asset has been continuously traded above or below the barrier level long enough. A down-and-out Parisian option denotes a contract that expires worthless if the underlying asset reaches a prespecified level  $L$  and remains constantly below this level for a time interval longer than a fixed number  $D$ , called the *window*. Its price (for a call option) at time  $0$  is given by

$$\phi(T,K) := e^{-rT} \mathbb{E}\left[ (S_T - K)^+ \mathbb{1}_{T_L^{D,-}(S) > T} \right] \quad (1)$$

where  $T_L^{D,-}(S)$  is the first time the asset S makes an excursion longer than  $D$  below  $L$ . Parisianstyle options are mostly encountered in convertible bonds with "soft-call" provision for conversion. For example, the bond's specifications may be such that conversion will be allowed if and only if the share price remains above a theoretical price for a given amount of time, for example, 20 business days prior to the conversion date (this is Parisian option). Other covenants stipulate that the average share price trades for  $n$  days above the trigger level. While the latter does not correspond *sensu stricto* to a Parisian option, the motivation is similar: to render the conversion rule more stable—and less prone to manipulation—basing it on the behavior of the stock price over a window of time as opposed to basing it on the (more volatile) spot price. The pioneer paper on that topic is owed to Chesney et al., [5]. Pricing Parisian options is a challenging issue and several methods have been proposed in the literature: Monte Carlo simulations, Laplace transforms, lattices, and partial differential equations.

#### **Monte Carlo Method**

As for standard barrier options, using simulations leads to a biased problem, owing to the choice of the discretization time step in the Monte Carlo algorithm. Baldi et al., [3] have developed a method based on sharp large deviation estimates, which improves the usual Monte Carlo procedure. It consists in providing an approximation of  $p^{\epsilon}$ —the probability that a Brownian bridge reaches a time-dependent barrier

over a time of length  $\epsilon$ —by studying its asymptotic behavior when  $\epsilon$  tends to 0. They derive precise estimates of  $g_{L,t}^S := \sup\{u \le t | S_u = L\}$ , which is, for a down-and-out Parisian option, related to  $T_L^{D,-}(S)$ by the following formula:  $T_L^{D,-}(S) := \inf\{t > 0 : (t - g_{L,t}^S) \mathbb{1}_{S_t < L} > D\}$ . This procedure still works when the asset follows a diffusion process with general coefficients.

### **Laplace Transforms**

The idea of using Laplace transforms for pricing Parisian options is owed to Chesney et al., [5]. By using the Brownian excursion theory, they get closed formulas for

$$\int_0^\infty dt \, \mathrm{e}^{-\lambda t} \phi(t, K) \tag{2}$$

the Laplace transform of the price with respect to the maturity time.

For models with constant parameters, when considering a down and in call option, one rewrites  $\phi(T, K)$  as

$$e^{-\left(r+\frac{m^{2}}{2}\right)T}\mathbb{E}_{\mathbb{P}}\left(\mathbb{1}_{T_{b}^{D,-}< T}\left(xe^{\sigma Z_{T}}-K\right)^{+}e^{mZ_{T}}\right) \tag{3}$$

where Z is a  $\mathbb{P}$ -Brownian motion, *m* depends on r and  $\sigma$ , and  $T_b^{D,-} := T_b^{D,-}(Z)$  is the first time Z makes an excursion below  $b := \frac{1}{\sigma} \log(L/S_0)$  longer than  $D$ . By using the Brownian motion excursion theory, notably the Azéma martingale and the Brownian meander, the density of  $Z_{T^{D,-}}$  can be obtained and it can be shown that  $T_b^{D,-}$  and  $Z_{T_b^{D,-}}$  are independent. There is no explicit formula for the density of  $T_b^{D,-}$ , but we only know its Laplace transform. The strong Markov property enables to introduce  $Z_{T^{D,-}}$  in equation  $(3)$ . We rewrite equation  $(3)$  as

$$\int_{-\infty}^{\infty} \mathbb{E}_{\mathbb{P}}(\mathbb{1}_{T^{D,-}_{b} < T} \mathcal{P}_{T-T^{D,-}_{b}}(f_{x})(z)) \nu^{-}(\mathrm{d}z) \qquad (4)$$

where  $\nu^-$  denotes the law of  $Z_{T^{D,-}}$ ,  $f_x(z) =$  $e^{-(r+m^2/2)T}e^{mz}(xe^{\sigma z}-K)^{+}$ , and  $\mathcal{P}_{t}^{'}(f_{x})(z)=1/$  $\sqrt{2\pi t} \int_{-\infty}^{\infty} f_x(u) \exp\left(-(u-z)^2/2t\right) du$ . It remains to compute the Laplace transform of equation (4) with respect to the maturity. A change of variables introduces the Laplace transform of  $T_b^{D,-}$ , which is explicitly known. This leads to a closed formula.

We refer the reader to  $[1]$  for the description of a fast and accurate numerical inversion of the Laplace transforms. By studying the regularity of the Parisian option prices with respect to the maturity time, Labart and Lelong [9] justify the accuracy of the numerical inversion. Except for particular values of the barrier, the prices are of class  $C^{\infty}$ . Their study relies on the existence and the regularity of a density for the Parisian time  $T_b^{D,-}$ .

This algorithm is implemented in  $[4]$  and is compared to a procedure for approximating a general Laplace transform with one that can be easily inverted. The Laplace transform approach is very specific to the problem, but practically we see that the lack in the flexibility of the method is compensated by its accuracy and computational speed.

## Lattices

Costabile [6] presents a discrete time algorithm to evaluate Parisian options. The evaluation method is based on a combinatorial approach used to count the number of trajectories of a particle which, moving in a binomial lattice, remains constantly above an upper barrier for time intervals strictly smaller than a prespecified window period. Once this number has been computed, it can be used to derive a binomial algorithm, based on the Cox-Ross-Rubinstein (CRR) model (see **Binomial Tree** or **Tree Methods**). It enables to evaluate Parisian options with a constant or an exponential barrier. Avellaneda and Wu [2] model and price Parisian-style options by a trinomial lattice method, which changes with the value of the asset with respect to the barrier.

# **Partial Differential Equations**

Pricing of Parisian options can be done using partial differential equations. Let  $\tau$  define the time the underlying asset has continuously spent in the excursion. For a down Parisian option,  $\tau := t - \sup\{t' <$  $t|S_{t'} > L$ . The dynamics of  $\tau$  is

$$\mathrm{d}\tau_t = \begin{cases} \mathrm{d}t & \text{if} \quad S_t < L, \\ -\tau_{t^-} & \text{if} \quad S_t = L, \\ 0 & \text{if} \quad S_t < L \end{cases} \tag{5}$$

The new state variable  $\tau$  can be viewed as a clock that starts ticking as soon as the share price crosses the barrier level and is immediately reset when the share price returns above  $L$ . We assume that the asset follows a log normal Brownian motion given by  $dS_t = \mu S_t dt + \sigma S_t dW_t$ . The option price is a function of S, t,  $\tau$ . If  $S > L$ , the governing equation is the standard Black Scholes equation:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0 \qquad (6)$$

If  $S \leq L$ ,  $\tau$  is ticking. The new governing equation is

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} + \frac{\partial V}{\partial \tau} - rV = 0 \quad (7)$$

The boundary conditions are the following: the pathwise continuity of V in  $S = L$  leads to  $V(L, t, \tau) =$  $V(L, t, 0)$  for all t, and

$$V(S, T, \tau) = (S_T - K)^{+} \quad \text{if } \tau < D,$$
  
$$V(S, T, \tau) = 0 \quad \text{otherwise}$$
(8)

In the study of Haber et al. [8], the numerical solution to equations  $(6)$  and  $(7)$  is implemented using an explicit finite difference scheme. In the case of a discrete monitoring of the contract, Vetzal and Forsyth [7] develop an algorithm based on the numerical solution of a system of one-dimensional PDEs. It is assumed that  $\tau$  only changes at observation dates with the value of  $S$  with respect to the barrier. Away from observation dates, the PDE satisfied by  $V$  does not depend on  $\tau$ . Then, the pricing problems consist of a small number of one-dimensional PDEs, which exchange information only at observation dates (we impose the continuity of  $V$ ).

These methods have one major benefit: they are flexible enough to be easily modified to price more general options, like Parisian (i.e., when the recorded duration is cumulative rather than continuous).

## **Double Parisian**

There exists a double barrier version of the standard Parisian options. Double Parisian options are barrier options that are activated or canceled if the underlying asset continuously remains outside a range  $[L_1, L_2]$  long enough. The price of a double Parisian out call at time  $0$  is given by

$$e^{-rT} \mathbb{E}\left[ (S_T - K)^+ \mathbb{1}_{T^{D,-}_{L_1}(S) > T} \mathbb{1}_{T^{D,+}_{L_2}(S) > T} \right] \tag{9}$$

These double Parisian options can be priced using the Monte Carlo procedure improved with the sharp large deviation method proposed by Baldi, Caramellino, and Iovino [3]. Labart and Lelong [9] give analytical formulas for the Laplace transforms of the prices with respect to the maturity time.

#### References

- [1] Abate, J., Choudhury, L.G. & Whitt, G. (1999). An introduction to numerical transform inversion and its application to probability models, in *Computational Probability*, W. Grassman, ed., Kluwer, Boston, pp. 257-323.
- [2] Avellaneda, M. & Wu, L. (1999). Pricing Parisian-style options with a lattice method, International Journal of Theoretical and Applied Finance  $2(1)$ , 1–16.
- Baldi, P., Caramellino, L. & Iovino, M.G. (2000). Pricing [3] complex barrier options with general features using sharp large deviation estimates, in Monte Carlo and Quasi-Monte Carlo Methods 1998 (Claremont, CA), Springer, Berlin, pp. 149-162.
- [4] Bernard, C., LeCourtois, O. & Quittard-Pinon, F. (2005). A new procedure for pricing Parisian options, The Journal of Derivatives  $12(4)$ , 45-53.

- [5] Chesney, M., Jeanblanc-Picqué, M. & Yor, M. (1997). Brownian excursions and Parisian barrier options, Advances in Applied Probability  $29(1)$ ,  $165-184$ .
- [6] Costabile, M. (2002). A combinatorial approach for pricing Parisian options, Decisions in Economics and Finance 25(2), 111-125.
- [7] Forsyth, P.A. & Vetzal, K.R. (1999). Discrete Parisian and delayed barrier options: A general numerical approach, Advances in Futures Options Research 10, 1-16.
- [8] Haber, R.J., Schonbucher, P.J. & Wilmott, P. (1999). Pricing Parisian options, Journal of Derivatives 6(3), 71-79.
- [9] Labart, C. & Lelong, J. Pricing Double Parisian options using Laplace transforms, International Journal of Theoretical and Applied Finance (to appear), http://hal.archives-ouvertes.fr/hal-00220470/fr/.

# **Related Articles**

Barrier Options; Discretely Monitored Options; Finite Difference Methods for Barrier Options; Lattice Methods for Path-dependent Options; **Partial Differential Equations.** 

Céline Labart
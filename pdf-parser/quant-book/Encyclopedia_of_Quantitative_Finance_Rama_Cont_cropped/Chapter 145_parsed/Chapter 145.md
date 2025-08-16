# Implied Volatility: Long **Maturity Behavior**

We discuss some properties of implied volatility surfaces (see Implied Volatility Surface) for large times to maturity. The key result is that the implied volatility smile flattens at long maturities, independently of the model of the underlying asset price, so long as there exists an equivalent martingale measure. An asymptotic formula for the long implied volatility is given and illustrated by examples from stochastic volatility models. The dynamics of the long implied volatility are shown to be almost surely nondecreasing as a function of calendar time, in complete analogy with the Dybvig et al. [2] theorem for long interest rates. For a more in-depth treatment of these issues, consult [3, 4], and [7].

#### Flattening of the Smile

To set up notation and present the main result, we consider in this section a market in which the riskless interest rate is zero, and the underlying stock pays no dividends. The results described here are valid for price processes with either continuous or discontinuous sample paths, or even discrete-time models.

We let  $S = (S_t)_{t \ge 0}$  be a nonnegative martingale with  $S_0 > 0$  modeling the price of a given stock under a fixed risk-neutral measure. All calculations will be performed with respect to this measure, so we do not include it in the notation.

Introduce a function  $C_{\text{BS}} : \mathbb{R} \times [0, \infty) \to [0, \infty)$ 1) by

$$C_{\text{BS}}(k, v) = \begin{cases} \Phi\left(-\frac{k}{\sqrt{v}} + \frac{\sqrt{v}}{2}\right) - e^{k}\Phi\left(-\frac{k}{\sqrt{v}} - \frac{\sqrt{v}}{2}\right) & \text{if } v > 0\\ (1 - e^{k})^{+} & \text{if } v = 0 \end{cases}$$
(1)

where  $a^+ = \max\{a, 0\}$  denotes the positive part of the real number a as usual. Since  $v \mapsto C_{\text{BS}}(k, v)$  is strictly increasing for each  $k \in \mathbb{R}$ , we now define the Black-Scholes implied volatility  $\Sigma(k, T)$  for  $\log$  moneyness  $k$  and maturity  $T$  as the unique

nonnegative solution to the equation

$$\mathbb{E}\left[\left(\frac{S_T}{S_0} - e^k\right)^+\right] = C_{\text{BS}}(k, T\Sigma(k, T)^2) \quad (2)$$

Note that we are using the convention that the log moneyness k corresponds to the strike  $K = S_0 e^k$ .

The main result is that the implied volatility smile flattens at long maturities:

**Theorem 1** For any  $M > 0$ , we have

$$\lim_{T \to \infty} \sup_{k_1, k_2 \in [-M, M]} |\Sigma(k_2, T) - \Sigma(k_1, T)| = 0 \quad (3)$$

That the implied volatility smile flattens at long maturities seems to be a folk theorem, and has been verified for various models for which the long implied volatility can be calculated explicitly. The result is sometimes attributed erroneously to the central limit theorem, but it is true in complete generality without any notion of mean reversion of the spot volatility process. Indeed, Theorem 1 contains no assumption on the dynamics of the stock price other than that it is a nonnegative martingale. Also note that we have not even assumed that  $\lim_{T\to\infty} \Sigma(k,T)$  exists for any  $k$ .

A proof of the flattening of the implied volatility smile under some mild regularity assumptions appears in [1]. A proof of Theorem 1 in the form that it appears here can be found in  $[9]$ .

It turns out that the rate of flattening can be precisely bounded:

#### Theorem 2

1. For any  $0 \le k_1 < k_2$ , we have

$$\frac{\Sigma(k_2, T)^2 - \Sigma(k_1, T)^2}{k_2 - k_1} \le \frac{4}{T} \tag{4}$$

2. For any  $k_1 < k_2 \le 0$ , we have

$$\frac{\Sigma(k_2, T)^2 - \Sigma(k_1, T)^2}{k_2 - k_1} \ge -\frac{4}{T} \tag{5}$$

3. If  $S_t \rightarrow 0$  in probability as  $t \rightarrow \infty$ , for any  $M > 0$ , we have

$$\limsup_{T \to \infty} \sup_{\substack{k_1, k_2 \in [-M, M] \\ k_1 \neq k_2}} T \left| \frac{\Sigma(k_2, T)^2 - \Sigma(k_1, T)^2}{k_2 - k_1} \right| \le 4$$
(6)

The inequality in part 3 of Theorem 2 is sharp, as there exists a martingale  $(S_t)_{t>0}$  such that  $S_t \to 0$  in probability and such that

$$T\frac{\partial}{\partial k}\Sigma(k,T)^2 \to -4\tag{7}$$

as  $T \to \infty$  uniformly for  $k \in [-M, M]$ . A proof of Theorem 2 is in [9].

**Remark** The condition  $S_t \rightarrow 0$  in probability appearing in part 3 of Theorem 2 has a natural financial interpretation. Indeed, we have  $S_t \rightarrow 0$  in probability (equivalently, almost surely) if and only if  $C(K,T) \to S_0$  as  $T \to \infty$  for some  $K > 0$  (equivalently, for all  $K > 0$ ) where

$$C(K,T) = \mathbb{E}[(S_T - K)^{+}] \tag{8}$$

is the price of a European call option. Since the long maturity call prices converge to stock price in many models of interest (including, of course, the Black-Scholes model), we see that the assumption  $S_t \rightarrow 0$  is not particularly onerous.

In fact, since  $(S_t)_{t\geq 0}$  is a nonnegative martingale, it must converge almost surely to some random variable  $S_{\infty}$  by the martingale convergence theorem. If  $S_{\infty} > 0$  with positive probability, then  $\lim_{T\to\infty}\sqrt{T}\Sigma(k,T)$  exists and is finite for each k, and hence  $\lim_{T\to\infty} \Sigma(k,T) = 0$ .

## A Representation Formula

Now that we know that the volatility smile flattens in the limit as the maturity goes to infinity, we can study the behavior of the long implied volatility.

**Theorem 3** For any  $M > 0$ , we have

$$\lim_{T \to \infty} \sup_{k \in [-M,M]} \left| \Sigma(k,T) - \left( -\frac{8}{T} \log \mathbb{E}[S_T \wedge 1] \right)^{1/2} \right| = 0 \tag{9}$$

where  $a \wedge b = \min\{a, b\}$  as usual. In particular, we have the following representation formula

$$\Sigma(\infty) = \lim_{T \to \infty} \left( -\frac{8}{T} \log \mathbb{E}[S_T \wedge 1] \right)^{1/2} \quad (10)$$

whenever the limit exists.

Formula (10) of Theorem 3 can be found, for instance, in [8]. It can be used to calculate the long implied volatility for some examples.

**Example** (Exponential Lévy Models (see Exp**onential Lévy Models**)). The simple inequality

$$\mathbb{1}_{[1,\infty)}(x) \le x \wedge 1 \le x^p \tag{11}$$

which holds for all  $0 < p < 1$  and  $x > 0$ , gives the bound

$$\begin{split} &\limsup_{T \to \infty} \sup_{p \in [0,1]} \left( -\frac{8}{T} \log \mathbb{E}[S_T^p] \right)^{1/2} \\ &\leq \Sigma(\infty) \leq \liminf_{T \to \infty} \left( -\frac{8}{T} \log \mathbb{P}[S_T \geq 1] \right)^{1/2} \tag{12} \end{split}$$

If  $(\log(S_t))_{t>0}$  has independent identically distributed increments, then the above bounds hold with equality by the large deviation principle. Indeed, let  $(L_t)_{t>0}$ be a Lévy process with cumulant-generating function

$$\Lambda(p) = \log \mathbb{E}(e^{pL_1}) \tag{13}$$

such that  $\Lambda(1) < \infty$ , and model the stock price by the martingale  $S_t = e^{L_t - t\Lambda(1)}$ . Then the long implied volatility satisfies

$$\Sigma(\infty)^{2} = 8 \sup_{p \in [0,1]} \{ p \Lambda(1) - \Lambda(p) \} \tag{14}$$

which is eight times the Legendre transform of the cumulant generating function evaluated at  $\Lambda(1)$ .

**Example** (*Stochastic volatility model.*) Lewis [8] has proposed a saddle-point approximation method for calculating long implied volatility in stochastic volatility models. For instance, suppose that the asset price satisfies the following system of stochastic differential equations:

$$dS_t = S_t \sqrt{V} \, dW_t \tag{15}$$

$$dV_t = \kappa (\theta - V_t) dt + \eta \sqrt{V_t} dZ_t \qquad (16)$$

where  $\kappa$ ,  $\theta$ , and  $\eta$  are real constants, and  $(W_t)_{t>0}$ and  $(Z_t)_{t>0}$  are correlated standard Wiener processes with  $\langle W, Z \rangle_t = \rho t$ . Lewis [8] has shown that the long implied volatility is given by the following formula:

$$\Sigma(\infty)^{2} = \frac{4\kappa\theta}{(1-\rho^{2})\eta^{2}}$$
$$\times \left[\sqrt{(2\kappa-\rho\eta)^{2}+(1-\rho^{2})\eta^{2}}-(2\kappa-\rho\eta)\right] \quad (17)$$

See [5] for further asymptotics of stochastic volatility models based on this method, and see [4] for asymptotics based on perturbation methods.

## **Long Implied Volatility Cannot Fall**

In many models of interest, the long implied volatility, if it exists, is constant as a function of the calendar time. However, the long implied volatility need not be a constant in general. In this section, we consider the dynamics of the long implied volatility, and in fact, we will see that the long implied volatility can never fall. In this section, we also assume that the stock price is strictly positive, rather than merely nonnegative. We define the implied volatility  $\Sigma_t(k,\tau)$ for log moneyness k and time to maturity  $\tau$  as the unique nonnegative  $\mathcal{F}_t$ -measurable random variable that satisfies

$$\mathbb{E}\left[\left(\frac{S_{t+\tau}}{S_t} - \mathrm{e}^k\right)^+\right] = C_{\mathrm{BS}}(k, \,\tau\,\Sigma_t(k,\,\tau)^2) \tag{18}$$

The following theorem was proved in [9].

**Theorem 4** For all  $k_1, k_2$  and  $0 \le s \le t$  we have

$$\limsup_{\tau \to \infty} \Sigma_t(k_1, \tau) - \Sigma_s(k_2, \tau) \ge 0 \tag{19}$$

almost surely.

This result is an exact analog of the Dybvig-Ingersoll-Ross theorem that long zero-coupon rates never fall. See [6] for a nice proof of this fact.

## Extensions

The previous discussion has considered the case where the stock pays no dividend and the risk-free interest rate is zero. In the general case, a stock pays a dividend and there is a cost to borrow money. The situation is usually modeled as follows. Let  $S_t$  be the stock price, let  $D_t$  be the cumulative dividends, and let  $B_t$  be the price of a numéraire asset such as a bank account at time  $t$ . There is no arbitrage if there exists a probability measure such that the process

$$\frac{S_t}{B_t} + \int_0^t \frac{\mathrm{d}D_s}{B_s} \tag{20}$$

is a martingale. In the case of proportional continuous dividends  $dD_t = \delta S_t dt$  and constant interest rate  $dB_t = r B_t dt$ , there is no arbitrage if  $\tilde{S}_t = S_t e^{(\delta - r)t}$ defines a martingale. In this case, everything from above applies if we define the implied volatilitv bv

$$\mathbb{E}\left[\left(\frac{\tilde{S}_T}{\tilde{S}_0} - \mathrm{e}^k\right)^+\right] = C_{\mathrm{BS}}(k, T\Sigma(k, T)^2) \quad (21)$$

where the log-moneyness parameter  $k$  now corresponds to the strike  $K = S_0 e^{k + (r - \delta)T}$ .

However, it is unclear which of the above results can be suitably extended to the general case with arbitrary increasing adapted processes  $(D_t)_{t>0}$  and  $(B_t)_{t>0}$ .

#### References

- [1] Carr, P. & Wu, L. (2003). The finite moment log stable process and option pricing, *Journal of Finance* **58**(2), 753-778.
- [2] Dybvig, P., Ingersoll, J. & Ross, S. (1996). Long forward and zero-coupon rates can never fall, Journal of Business 60.  $1-25$ .
- [3] Gatheral, J. (2006). The Volatility Surface: A Practitioner's Guide, John Wiley & Sons, Hoboken, NJ.
- [4] Fouque, J.-P., Papanicolaou, G. & Sircar, K.R. (2000). Derivatives in Financial Markets with Stochastic Volatility, Cambridge University Press.
- [5] Jacquier, A. (2007). Asymptotic Skew Under Stochastic Volatility, Pre-print, Birkbeck College, University of London.
- [6] Hubalek, F., Klein, I. & Teichmann, J. (2002). A general proof of the Dybvig-Ingersoll-Ross theorem: long forward rates can never fall, Mathematical Finance 12(4),  $447 - 451.$
- [7] Lee, R. (2004). Implied volatility: statics, dynamics, and probabilistic interpretation, in Recent Advances in Applied Probability, R. Baeza-Yates, et al., eds, Springer-Verlag, Springer, New York, 241-268.
- [8] Lewis, A. (2000). *Option Valuation Under Stochastic* Volatility, Finance Press, Newport Beach.
- [9] Rogers, L.C.G. & Tehranchi, M.R. (2008). Can the Implied Volatility Surface Move by Parallel Shifts? Preprint, University of Cambridge.

# **Related Articles**

## Exponential Lévy Models; Heston Model; Implied Volatility Surface; Moment Explosions.

MICHAEL R. TEHRANCHI
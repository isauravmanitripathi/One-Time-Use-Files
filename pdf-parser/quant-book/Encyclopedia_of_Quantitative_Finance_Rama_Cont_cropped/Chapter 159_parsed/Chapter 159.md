# Jump-diffusion Models

Jump-diffusion (JD) option pricing models are particular cases of exponential Lévy models (see Exponential Lévy Models) in which the frequency of jumps is finite. They can be considered as prototypes for a large class of more complex models such as the stochastic volatility plus jumps model of Bates (see Bates Model).

Consider a market with a riskless asset (the bond) and one risky asset (the stock) whose price at time t is denoted by  $S_t$ . In a JD model, the SDE for the stock price is given as

$$dS_t = \mu S_{t-} dt + \sigma S_{t-} dZ_t + S_{t-} dJ_t \qquad (1)$$

where  $Z_t$  is a Brownian motion and

$$J_t = \sum_{i=1}^{N_t} Y_i \tag{2}$$

is a compound Poisson process where the jump sizes  $Y_i$  are independent and identically distributed with distribution F and the number of jumps  $N_t$  is a Poisson process with intensity  $\lambda$ . The asset price  $S_t$  thus follows geometric Brownian motion between jumps. Monte Carlo simulation of the process can be carried out by first simulating the number of jumps  $N_t$ , the jump times, and then simulating geometric Brownian motion on intervals between jump times.

The SDE  $(1)$  has the exact solution:

$$S_t = S_0 \exp{\{\mu t + \sigma Z_t - \sigma^2 t/2 + J_t\}} \qquad (3)$$

Merton  $[5]$  considers the case where the jump sizes  $Y_i$  are normally distributed.

## **Risk-neutral Drift**

If the above model is used as a pricing model, the drift  $\mu$  in equation (1) is given by the risk-neutral drift  $\hat{\mu}$ , which contains a jump compensator  $\mu_I$ :

$$\mu = \hat{\mu} + \mu_J \tag{4}$$

To identify  $\mu_J$ , taking expectations of equation (1) and from the definition of  $\hat{\mu}$ ,

$$\mathbb{E}[\mathrm{d}S_t] = \hat{\mu} S_t \, \mathrm{d}t = \mu S_t \, \mathrm{d}t$$
$$+ \lambda \left\{ \int \xi \, F(\mathrm{d}\xi) \right\} S_t \, \mathrm{d}t \tag{5}$$

where  $F$  is the risk-neutral jump distribution. The jump compensator is then given as

$$\mu_J = -\lambda \int \xi F(\mathrm{d}\xi) \tag{6}$$

To simplify the presentation, we henceforth assume zero dividends so that  $\hat{\mu} = r$ , the risk-free rate.

## Characteristic Function

Define the forward price  $F := S_0 e^{rt}$ . If  $x_t :=$  $\log S_t/F$  is a Lévy process (see Lévy Processes), its characteristic function  $\phi_T(u) := \mathbb{E}\left[e^{iux_T}\right]$  has the Lévy-Khintchine representation

$$\phi_T(u) = \exp\left\{i\,u\,(\mu_J - \sigma^2/2)\,T - u^2\,\sigma^2/2\,T\right.+ T\,\int \left[e^{iu\xi} - 1\right]\,\nu(\xi)\,\mathrm{d}\xi\right\} \tag{7}$$

Typical assumptions for the distribution of jump sizes are as follows: normal as in the original paper by Merton  $[5]$  and double exponential as in  $[3]$  (see Kou Model). In the Merton model, the Lévy density  $\nu(\cdot)$  is given as

$$\nu(\xi) = \frac{\lambda}{\sqrt{2\pi}\,\delta} \exp\left\{-\frac{(\xi - \alpha)^2}{2\,\delta^2}\right\} \tag{8}$$

where  $\alpha$  is the mean of the log-jump size log J and  $\delta$  the standard deviation of jumps. This leads to the explicit characteristic function

$$\phi_T(u) = \exp\left\{i\,u\,\omega\,T - \frac{1}{2}\,u^2\,\sigma^2\,T\right.\left. + \lambda\,T\,\left(e^{iu\,\alpha - u^2\,\delta^2/2} - 1\right)\right\} \tag{9}$$

with

$$\omega = -\frac{1}{2}\sigma^2 - \lambda \left( e^{\alpha + \delta^2/2} - 1 \right) \tag{10}$$

In the double-exponential case (see **Kou Model**)

$$\nu(\xi) = \lambda \left\{ p \, \alpha_{+} \, \mathrm{e}^{-\alpha_{+} \, \xi} \, \mathbf{1}_{\xi \ge 0} \right. \\
\quad + (1 - p) \, \alpha_{-} \, \mathrm{e}^{-\alpha_{-} \, |\xi|} \, \mathbf{1}_{\xi < 0} \right\} \tag{11}$$

where  $\alpha_{+}$  and  $\alpha_{-}$  are the expected positive and negative jump sizes, respectively, and  $p$  is the relative probability of a positive jump. This gives the explicit characteristic function:

$$\phi_T(u) = \exp\left\{ \mathrm{i}\, u \,\omega \,T - \frac{1}{2} \,u^2 \,\sigma^2 \,T + \lambda \,T \right.$$
$$\times \left( \frac{p}{\alpha_+ - \mathrm{i}\, u} - \frac{1 - p}{\alpha_- + \mathrm{i}\, u} \right) \right\} \tag{12}$$

with

$$\omega = -\frac{1}{2}\sigma^2 - \lambda \left(\frac{p}{\alpha_+ + 1} - \frac{1 - p}{\alpha_- - 1}\right) \tag{13}$$

## **Pricing of European Options**

Given a characteristic function, European call options can be priced using Fourier methods (see Fourier **Methods in Options Pricing**), as in [4]:

$$C(S, K, T) = e^{-rT} \left\{ F - \sqrt{FK} \frac{1}{\pi} \int_0^\infty \frac{du}{u^2 + \frac{1}{4}} \times \text{Re} \left[ e^{-iuk} \phi_T (u - i/2) \right] \right\} \tag{14}$$

where the log-strike  $k := \log{(K/F)}$ .

#### Valuation Equation

Assuming the process (1) and a constant risk-free rate  $r$  and further supposing that the market is complete, the value  $V(S, t)$  of a European-style option satisfies

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V + \lambda \int F(\mathrm{d}\xi)$$
$$\left\{ V(S \mathrm{e}^{\xi}, t) - V(S, t) - \left( \mathrm{e}^{\xi} - 1 \right) S \frac{\partial V}{\partial S} \right\} = 0 \tag{15}$$

where for ease of notation, V denotes  $V(S, t)$ . Equation  $(15)$  is a partial integro-differential equation (PIDE) (see Partial Integro-differential Equations (PIDEs)), which can be solved using finite-difference methods  $[1]$ .

#### A Valuation Formula for European Options

Merton [5] derived an exact solution of the valuation equation  $(15)$  for a European-style call option with strike  $K$  and time to expiration  $T$ , which has the form of an infinite sum of Black-Scholes-like terms:

$$C(S, K, T) = \sum_{n=0}^{\infty} \frac{e^{-\lambda T} (\lambda T)^n}{n!} \int F_n(d\xi) \times C_{\text{BS}}(S e^{\xi} e^{\mu_J T}, K, r, \sigma, T)$$
(16)

where  $F_n$  is the distribution of the sum of  $n$ independent jumps and  $C_{\text{BS}}(\cdot)$  denotes the Black-Scholes solution, which is given as

$$C_{\text{BS}}(S, K, r, \sigma, T) = S N(d_1) - K e^{-rT} N(d_2)$$
(17)

with

$$d_1 = \frac{\log(S/K) + rT}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2}$$
$$d_2 = \frac{\log(S/K) + rT}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2} \tag{18}$$

#### Jump to Ruin

In the case where  $e^{Y_i} = 0$  with probability 1,  $\mu_J = \lambda$ and equation  $(16)$  simplifies to

$$C(S, K, T) = e^{-\lambda T} C_{\text{BS}}(S e^{\lambda T}, K, r, \sigma, T) \quad (19)$$

which is the Black-Scholes formula with a shifted interest rate  $r \rightarrow r + \lambda$ . This special case of the JD model where the stock price jumps to zero (or ruin) whenever there is a jump is the simplest possible model of default. Equation  $(19)$  for the option price in the jump-to-ruin model may also be derived from a Black-Scholes style replication argument using stock and bonds of the issuer of the stock; upon default of the issuer, both stock and bonds jump to zero. The cost of funding stock with bonds of the issuer is  $r + \lambda$ in this picture, which explains the simple form  $(19)$ of the solution.

## **Local Volatility**

There is a particularly simple expression for Dupire local volatility in the jump-to-ruin model. It is given by Gatheral [2]:

$$\sigma_{\text{loc}}^2(K, T; S) = \sigma^2 + 2\lambda \sigma \sqrt{T} \frac{N(d_2)}{N'(d_2)} \tag{20}$$

with

$$d_2 = \frac{\log(S/K) + \lambda T}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2} \tag{21}$$

As  $K \to \infty$ ,  $d_2 \to -\infty$  and the correction term vanishes, and as  $K \rightarrow 0$ , the correction term explodes. In addition, as the *hazard rate*  $\lambda$  increases, so does  $d_2$ , increasing the local volatility for low strikes  $K$  relative to high strikes.

## Normally Distributed Jumps

Merton [5] also shows that if jumps are normally distributed with  $Y_i \sim N(\alpha, \delta)$ , equation (16) again simplifies considerably to give

$$C(S, K, T) = \sum_{n=0}^{\infty} \frac{e^{-\lambda' T} \left(\lambda' T\right)^n}{n!} C_{\text{BS}}(S, K, r_n, \sigma_n, T)$$
(22)

with

$$\lambda' = \lambda \, \mathrm{e}^{\alpha + \delta^2/2} \tag{23}$$

$$\sigma_n^2 T = \sigma^2 T + n \,\delta^2 \tag{24}$$

$$r_n T = (r + \mu_J) T + n \left(\alpha + \delta^2/2\right)$$
 (25)

Each term  $C_{\text{BS}}(S, K, r_n, \sigma_n, T)$  in equation (22) is the value of the option conditional on there being exactly  $n$  jumps during its life.

#### Implied Volatility Smile

If there were no jumps in this model, the implied volatility smile would be flat. Jumps in the JD stock price process induce an implied volatility smile whose short time limit (see, e.g., [2]) is given as

$$K \frac{\partial}{\partial K} \sigma_{\text{BS}}^2(K, T) \to -2\,\mu_J \text{ as } T \to 0$$
 (26)

The greater the  $\mu_J$ , because jumps are either more frequent or more negatively skewed, the more negative is the implied volatility skew.

## References

- [1] Cont, R. & Voltchkova, E. (2005). A finite difference scheme for option pricing in jump-diffusion and exponential Lévy models, SIAM Journal on Numerical Analysis 43(4), 1596-1626.
- Gatheral, J. (2006). The Volatility Surface, John Wiley & [2] Sons, Hoboken, Chapter 5.
- [3] Kou, S. (2002). A jump-diffusion model for option pricing, Management Science 48, 1086-1101.
- [4] Lewis, A.L. (2000). Option Valuation under Stochastic Volatility with Mathematica Code, Finance Press, Newport Beach, CA.
- [5] Merton, R.C. (1976). Option pricing when underlying stock returns are discontinuous, Journal of Financial Economics 3, 125-144.

# **Related Articles**

Bates Model; Exponential Lévy Models; Fourier Methods in Options Pricing; Implied Volatility Surface: Kou Model: Partial Integro-differential Equations (PIDEs).

JIM GATHERAL
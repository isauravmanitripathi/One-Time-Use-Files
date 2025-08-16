# **Term Structure Models**

*Term structure models* describe the behavior of interest rates as a function of time and term (time to maturity). As a function of time, rates behave as stochastic processes (see Figure 1). As a function of term, interest rates on a given date form a *yield curve* (see Figure 2).

Interest rates of different maturities behave as a joint stochastic process. Not all joint processes, however, can describe interest-rate behavior in an efficient market. For instance, suppose that a term structure model postulates that rates of all maturities change in time by equal amounts, that is, that yield curves move by parallel shifts (which, empirically, appears to be a reasonable first-order approximation). It can be shown that in this case a portfolio consisting of a long bond and a short bond would always outperform a medium-term bond with the same Macaulay duration (*see* **Bond**). In an efficient market, supply and demand would drive the price of the medium maturity bond down and the prices of the long and short bonds up. As this would cause the yield on the medium bond to increase and the yields on the long and short bonds to decrease, the yield curves would not stay parallel. This model therefore cannot describe interest-rate behavior.

In order that riskless arbitrage opportunities are absent, the joint process of interest-rate behavior must satisfy some conditions. Determining these conditions and finding processes that satisfy them is the purpose of term structure models.

The joint stochastic process will be driven by a number of sources of uncertainty. For continuous processes, the sources of uncertainty are often specified as Wiener processes. If the evolution of the yield curve can be represented by Markovian state variables, these variables are called *factors*.

Let *B(t, T )* be the price at time *t* of a defaultfree zero-coupon bond maturing at time *T* with unit maturity value. *Yield to maturity R(t, s)* at time *t* with term *s* is defined as the continuously compounded rate of return on the bond,

$$R(t,s) = -\frac{1}{s} \log B(t,t+s) \tag{1}$$

The instantaneous interest rate will be called the *short rate*,

$$r(t) = \lim_{s \to 0} R(t, s) \tag{2}$$

An asset accumulating interest at the short rate will be called the *money market account*,

$$\beta(t) = \exp\left(\int_0^t r(\tau) \,\mathrm{d}\tau\right) \tag{3}$$

*Forward rates f (t, T )* are defined by the equation

$$B(t,T) = \exp\left(-\int_{t}^{T} f(t,\tau) \,\mathrm{d}\tau\right) \tag{4}$$

# **One-factor Models**

A general theory of one-factor term structure models was given by Vasicek [9]. He assumed the following:

- 1. The short rate follows a continuous Markov process.
- 2. The price *B(t, T )* of a bond is determined by the assessment at time *t* of the segment {*r(τ ), t* ≤ *τ* ≤ *T* } of the short-rate process over the term of the bond.
- 3. The market is efficient; that is, there are no transaction costs, information is available to all investors simultaneously, and every investor acts rationally (prefers more wealth to less, and uses all available information).

Assumption 3 implies that investors have homogeneous expectations and that no profitable riskless arbitrage is possible.

By assumption 1, the development of the short rate over an interval (*t,T* ), *t* ≤ *T* , given its values prior to time *t*, depends only on the current value *r(t)*. Assumption 2 then implies that the price *B(t, T )* is a function of *r(t)*. Thus, the value of the short rate is the only state variable for the whole term structure.

Let the dynamics of the short rate be given by

$$dr(t) = \zeta(r, t) dt + \varphi(r, t) dW(t)$$
(5)

where *W (t)* is a Wiener process. Denote the mean and variance of the instantaneous rate of return on the bond with price *B(t, T )* by *µ(t, T )* and *σ*<sup>2</sup>*(t, T )*, respectively,

$$\frac{\mathrm{d}B(t,T)}{B(t,T)} = \mu(t,T)\,\mathrm{d}t - \sigma(t,T)\,\mathrm{d}W(t) \tag{6}$$

Consider an investor who at time *t* issues an amount *w*<sup>1</sup> of a bond with maturity date *T*1, and

![](_page_1_Figure_1.jpeg)

Figure 1 US Treasury Yields

![](_page_1_Figure_3.jpeg)

Figure 2 US Treasury Yield Curves

simultaneously buys an amount  $w_2$  of a bond with maturity date  $T_2$ . Suppose the amounts  $w_1$  and  $w_2$ are chosen to be proportional to  $\sigma(t, T_2)$  and  $\sigma(t, T_1)$ , respectively. Then the position is instantaneously riskless, and should realize the short rate of return  $r(t)$ . It follows that the ratio  $(\mu(t, T) - r(t))/\sigma(t, T)$ is independent of T. Its common value  $\lambda(t)$  is called the market price of risk, as it specifies the increase in the expected rate of return on a bond per an additional unit of risk. We thus have

$$\mu(t,T) = r(t) + \lambda(t)\sigma(t,T) \tag{7}$$

Applying Ito's lemma to the price  $B(t, T) =$  $B(t, T, r)$  and comparing with equation (6) yields

$$\frac{\partial B}{\partial t} + (\zeta + \varphi \lambda) \frac{\partial B}{\partial r} + \frac{1}{2} \varphi^2 \frac{\partial^2 B}{\partial r^2} - rB = 0 \qquad (8)$$

The bond price is subject to the boundary condition  $B(T, T) = 1$ .

The solution to equation  $(8)$  is given by

$$B(t,T) = E_t \exp\left(-\int_t^T r(\tau) \, \mathrm{d}\tau - \frac{1}{2} \int_t^T \lambda^2(\tau) \, \mathrm{d}\tau + \int_t^T \lambda(\tau) \, \mathrm{d}W(\tau)\right) \tag{9}$$

This equation, called the *fundamental bond pricing* equation (the Vasicek equation), fully describes the term structure and its behavior.

#### **Model Examples**

Various specific cases have been proposed in the literature. Vasicek [9] gives an example of a term structure model in which the short rate follows a mean reverting random walk (the Ornstein-Uhlenbeck process, see Ornstein-Uhlenbeck Processes)

$$dr = \alpha(\theta - r) dt + \varphi dW \qquad (10)$$

and the market price of risk  $\lambda(t, r) = \lambda$  is constant. In that case, the expectation in equation  $(9)$  can be evaluated explicitly to give

$$B(t,T) = \exp\left(\frac{1}{\alpha}\left(1 - e^{-\alpha(T-t)}\right)(R(\infty) - r) - (T-t)R(\infty) - \frac{\varphi^2}{4\alpha^3}\left(1 - e^{-\alpha(T-t)}\right)^2\right)$$
(11)

where

$$R(\infty) = \theta + \lambda \varphi / \alpha - \frac{1}{2} \varphi^2 / \alpha^2 \tag{12}$$

Interest rates are Gaussian. The advantage of this specification is its tractability. A drawback is that interest rates can become negative.

Cox *et al.* [3] derive a model in which

$$dr = \alpha(\theta - r) dt + \varphi \sqrt{r} dW \qquad (13)$$

and the market price of risk  $\lambda(t,r) = \eta \sqrt{r}$ . In this case, the bond prices can also be explicitly given (see Cox-Ingersoll-Ross (CIR) Model). They have the form

$$B(t,T) = A(t,T) \exp(-D(t,T)r(t)) \tag{14}$$

Interest rates are always nonnegative.

Hull and White [8] extended these two models by allowing the parameters in equations  $(10)$  and  $(13)$ , as well as the market price of risk, to be time dependent. This has the advantage that the model can be made consistent with initial data. For instance, by making  $\theta$  a function of time, the model can be made to exactly fit the initial term structure of interest rates (which is not possible with time-homogeneous models). Similarly, making the volatility  $\varphi$  a function of time allows calibration of the model to the term structure of swaption volatilities. Hull and White give closed-form solutions for bond prices for what they call the extended Vasicek and the extended Cox-Ingersoll-Ross models. These cases belong to the class of models that Duffie and Kan [4] call the affine term structure models (see Affine Models), in which bond prices have the form  $(14)$ .

Black et al. [1] and Black and Karasinski [2] give a model with

$$d \log r = \alpha(t) (\log \theta(t) - \log r) dt + \varphi(t) dW \quad (15)$$

In this model, bond prices cannot be given in closed-form formulas, but can be calculated numerically. Interest rates are lognormal. Lognormal models have regularity issues, for example, they produce infinite Eurodollar future prices (see **Eurodollar** Futures and Options).

The term structure theory generalizes easily to multiple factors and multiple sources of uncertainty. In fact, the bond pricing equation (9) is universally valid for any arbitrage-free term structure model. If  $W, \varphi, \lambda$  are vectors, their products are interpreted as inner products.

# **Contingent Claim Pricing**

One of the main tasks of term structure models in applications is pricing of *interest-rate-contingent* claims (interest-rate derivatives). This could be approached in several ways. For one-factor models it can be shown, by means of an arbitrage argument similar to that above for bonds, that the price  $P(t)$  of any interest-rate derivative satisfies the partial differential equation  $(8)$ . The valuation of the derivative is then accomplished by solving that equation subject to boundary conditions that describe the derivative asset payouts. If a closed-form solution cannot be given, the equation can be solved numerically in a tree or a finite difference lattice. A more general method is to realize that such a solution has the form

$$P(t) = E_t P(s) \exp\left(-\int_t^s r(\tau) \, \mathrm{d}\tau - \frac{1}{2} \int_t^s \lambda^2(\tau) \, \mathrm{d}\tau + \int_t^s \lambda(\tau) \, \mathrm{d}W(\tau)\right) \tag{16}$$

This equation holds even in the cases where there are no Markovian state variables. To calculate the expectation in equation  $(16)$ , however, is typically more difficult than solving a partial differential equation.

The modern theory of derivative asset pricing (see Harrison and Kreps [5]) introduces a change of probability measure as the basic pricing tool. There exists an equivalent probability measure  $P^*$ , called the risk-neutral measure, such that the value of any asset expressed in units of the money market account  $\beta(t)$  follows a martingale under that measure.

$$\frac{P(t)}{\beta(t)} = E_t^* \frac{P(s)}{\beta(s)}$$
(17)

The process

$$W^*(t) = W(t) - \int_0^t \lambda(\tau) d\tau \qquad (18)$$

is a Wiener process under the risk-neutral probability measure  $P^*$ 

If current bond prices are considered given, interest-rate derivatives can be priced without knowing the market price of risk  $\lambda(t)$  by writing the dynamics of interest rates directly in terms of the process  $W^*(t)$ . From equations (6) and (7), bond prices are subject to

$$\frac{\mathrm{d}B(t,T)}{B(t,T)} = r(t)\,\mathrm{d}t - \sigma(t,T)\,\mathrm{d}W^*(t) \tag{19}$$

Integrating equation (19) with respect to *t* and differentiating with respect to *T* yields

$$f(t,T) - f(0,T)$$
  
= 
$$\int_0^t \varphi(\tau,T)\sigma(\tau,T) d\tau + \int_0^t \varphi(\tau,T) dW^*(\tau)$$
  
(20)

where *ϕ(t, T )* is the volatility of the forward rate *f (t, T )* and

$$\sigma(\tau, T) = \int_{\tau}^{T} \varphi(\tau, s) \, \mathrm{d}s \tag{21}$$

Thus, knowledge of the initial term structure *f (*0*,T)*, *T* ≥ 0 and of the forward-rate volatilities is sufficient for pricing interest-rate-contingent claims. This was proposed in essence by Ho and Lee [7] and later formalized by Heath *et al.* [6] (*see* **Heath–Jarrow–Morton Approach**).

# **References**

[1] Black, F., Derman, E. & Toy, W. (1990). A one-factor model of interest rates and its application to Treasury bond options, *Financial Analysts Journal* January-February, 33–39.

- [2] Black, F. & Karasinski, P. (1991). Bond and option pricing when interest rates are lognormal, *Financial Analysts Journal* July-August, 52–59.
- [3] Cox, J., Ingersoll, J. Jr. & Ross, S. (1985). A theory of the term structure of interest rates, *Econometrica* **53**, 385–407.
- [4] Duffie, D. & Kan, R. (1996). A yield-factor model of interest rates, *Mathematical Finance* **6**, 379–406.
- [5] Harrison, J.M. & Kreps, D.M. (1979). Martingales and arbitrage in multiperiod security markets, *Journal of Economic Theory* **20**, 381–408.
- [6] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**, 77–105.
- [7] Ho, T.S.Y. & Lee, S.-B. (1986). Term structure movements and pricing interest rate contingent claims, *Journal of Finance* **41**, 1011–1028.
- [8] Hull, J. & White, A. (1990). Pricing interest-rate derivative securities, *Review of Financial Studies* **3**, 573–592.
- [9] Vasicek, O.A. (1977). An equilibrium characterization of the term structure, *Journal of Financial Economics* **5**, 177–188.

# **Related Articles**

**Affine Models**; **Bond**; **Caps and Floors**; **Cox–Ingersoll–Ross (CIR) Model**; **Heath–Jarrow–Morton Approach**.

OLDRICH ALFONS VASICEK
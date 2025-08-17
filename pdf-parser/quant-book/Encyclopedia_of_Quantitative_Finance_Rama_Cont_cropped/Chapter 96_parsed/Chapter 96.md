# **Pricing Formulae for Foreign Exchange Options**

The foreign exchange options market is highly competitive, even for products beyond vanilla call and put options. This means that pricing and risk management systems always need to have the fastest possible method to compute values and sensitivities for all the products in the book. Only then can a trader or risk manager know the current position and risk of his book. The ideal solution is to use pricing formulae in closed form. However, this is often only possible in the Black-Scholes model.

# **General Model Assumptions and** Abbreviations

Throughout this article, we denote the current value of the spot  $S_t$  by x and use the abbreviations listed in Table 1.

The pricing follows the usual procedures of Arbitrage pricing theory and the Fundamental theorem of asset pricing. In a foreign exchange market, this means that we model the underlying exchange rate by a geometric Brownian motion

$$dS_t = (r_d - r_f)S_t dt + \sigma S_t dW_t \tag{1}$$

where  $r_d$  denotes the domestic interest rate,  $\sigma$  the volatility, and  $W_t$  the standard Brownian motion; see Foreign Exchange Symmetries for details. Most importantly, we note that there is a foreign interest rate  $r_f$ . As in **Option Pricing: General Princi**ples, one can compute closed-form solutions for many options types with payoff  $F(S_T)$  at maturity  $T$  directly *via* 

$$v(t,x) = e^{-r_d T} \mathbb{E}[F(S_T)|S_t = x]$$
  
=  $e^{-r_d T} \mathbb{E}\left[F\left(x e^{(r_d - r_f - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z}\right)\right]$  (2)

where  $v(t, x)$  denotes the value of the derivative with payoff  $F$  at time  $t$  if the spot is at  $x$ . The random variable  $Z$  represents the continuous returns, which are modeled as standard normal in the Black-Scholes **model**. In this model, we can proceed as

<table>

 **Table 1** Abbreviations used for the pricing formulae of
  $FX$  options

| $\tau \stackrel{\Delta}{=} T - t$                                            | $\theta_{\pm} \triangleq \frac{r_d - r_f}{\sigma} \pm \frac{\sigma}{2}$                                          |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| $D_d \stackrel{\Delta}{=} e^{-r_d \tau}$                                     | $d_{\pm} \triangleq \frac{\ln\left(\frac{x}{K}\right) + \sigma\theta_{\pm}\tau}{\sigma_{2}\sqrt{\tau}}$          |
| $D_f \stackrel{\Delta}{=} \mathrm{e}^{-r_f \tau}$                            | $x_{\pm} \triangleq \frac{\ln\left(\frac{x}{B}\right) + \sigma\theta_{\pm}\tau}{\sqrt{-}}$                       |
| $n(t) \stackrel{\Delta}{=} \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}}$         | $z_{\pm} \stackrel{\Delta}{=} \frac{\ln\left(\frac{B^2}{xK}\right) + \sigma\theta_{\pm}\tau}{\sigma_{\pm}/\tau}$ |
| $\mathcal{N}(x) \stackrel{\Delta}{=} \int_{-\infty}^{x} n(t) \, \mathrm{d}t$ | $y_{\pm} \triangleq \frac{\ln\left(\frac{B}{x}\right) + \sigma\theta_{\pm}\tau}{\ln\sqrt{1 - \frac{B}{\tau}}}$   |
| $\phi = +1$ for call options                                                 | $\phi = -1$ for put options                                                                                      |
| $t$ : current time                                                           | $T$ : maturity time                                                                                              |
| $K$ : strike                                                                 | $B, L, H$ : barriers                                                                                             |

 $v(t,x)$ 

$$= e^{-r_d \tau} \int_{-\infty}^{+\infty} F\left(x e^{(r_d - r_f - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z}\right) n(z) dz$$
$$= D_d \int_{-\infty}^{+\infty} F\left(x e^{\sigma\theta_{-}\tau + \sigma\sqrt{\tau}z}\right) n(z) dz \tag{3}$$

The rest is working out the integration. In other models, one would replace the normal density by another density function such as a  $t$ -density. However, in many other models densities are not explicitly known, or even if they are, the integration becomes cumbersome.

For the resulting pricing formulae, there are many sources, for example, [7, 11, 17]. Many general books on **Option Pricing** also contain formulae in a context outside the foreign exchange, for example, [8, 18]. Obviously, we cannot cover all possible formulae in this section. We give an overview of several relevant examples and refer to Foreign Exchange Basket Options; Margrabe Formula; Quanto Options for more. FX vanilla options are covered in Foreign **Exchange Symmetries.** 

## **Barrier Options**

We consider the payoff for single-barrier knock-out options

$$\begin{aligned} [\phi(S_T - K)]^+ \mathbf{I}_{\{\eta S_t > \eta B, 0 \le t \le T\}} \\ &= [\phi(S_T - K)]^+ \mathbf{I}_{\{\min_{t \in [0, T]} (\eta S_t) > \eta B\}} \end{aligned} \tag{4}$$

where the binary variable  $\eta$  takes the value +1 if the barrier  $B$  is approached from above (down-andout) and  $-1$  if the barrier is approached from below (up-and-out).

To price knock-in options paying

$$[\phi(S_T - K)]^+ \mathbb{I}_{\{\min_{t \in [0,T]} (\eta S_t) \le \eta B\}} \tag{5}$$

we use the fact that

$$\text{knock-in} + \text{knock-out} = \text{vanilla}$$
 (6)

Computing the value of a barrier option in the Black-Scholes model boils down to knowing the joint density  $f(x, y)$  for a Brownian motion with drift and its running extremum  $(\eta = +1$  for a minimum and  $\eta = -1$  for a maximum),

$$\left(W(T) + \theta_{-}T, \eta \min_{0 \le t \le T} \left[\eta(W(t) + \theta_{-}t)\right]\right) \quad (7)$$

which is derived, for example, in [15], and can be written as

$$f(x, y) = -\eta e^{\theta_{-}x - \frac{1}{2}\theta_{-}^{2}T} \frac{2(2y - x)}{T\sqrt{2\pi T}} \exp\left\{-\frac{(2y - x)^{2}}{2T}\right\}, \quad (8)$$
$$\eta y \leq \min(0, \eta x)$$

Using the density (8), the value of a barrier option can be written as the following integral

barrier 
$$(S_0, \sigma, r_d, r_f, K, B, T)$$

$$= e^{-r_d T} \mathbb{E} \left[ \left[ \phi(S_T - K) \right]^+ \mathbb{I}_{\{\eta S_t > \eta B, 0 \le t \le T\}} \right] \quad (9)$$
$$= e^{-r_d T} \int_{x = -\infty}^{x = +\infty} \int_{\eta y \le \min(0, \eta x)} \left[ \phi(S_0 e^{\sigma x} - K) \right]^+ \times \mathbb{I}_{\left\{\eta y > \eta \frac{1}{\sigma} \ln \frac{B}{S_0} \right\}} f(x, y) \, \mathrm{d}y \, \mathrm{d}x \quad (10)$$

Further details on how to evaluate this integral can be found in [15]. It results in four terms. We provide the four terms and summarize, in Table 2, how they are used to find the value function (see also [13] or [14]).

$$A_1 = \phi x D_f \mathcal{N}(\phi d_+) - \phi K D_d \mathcal{N}(\phi d_-) \tag{11}$$

$$A_2 = \phi x D_f \mathcal{N}(\phi x_+) - \phi K D_d \mathcal{N}(\phi x_-) \tag{12}$$

$$A_{3} = \phi \left(\frac{B}{x}\right)^{\frac{2\theta_{-}}{\sigma}}$$
$$\times \left[xD_{f}\left(\frac{B}{x}\right)^{2}\mathcal{N}(\eta z_{+}) - KD_{d}\mathcal{N}(\eta z_{-})\right] \tag{13}$$
$$A_{4} = \phi \left(\frac{B}{x}\right)^{\frac{2\theta_{-}}{\sigma}}$$
$$\times \left[xD_{f}\left(\frac{B}{x}\right)^{2}\mathcal{N}(\eta y_{+}) - KD_{d}\mathcal{N}(\eta y_{-})\right] \tag{14}$$

**Table 2** The summands for the value of single barrier options

| Option type                | $\phi$ | $\eta$ | In/Out | Reverse    | Combination             |
|----------------------------|--------|--------|--------|------------|-------------------------|
| Standard up-and-in call    | $+1$   | $-1$   | in     | K > B      | $A_1$                   |
| Reverse up-and-in call     | $+1$   | $-1$   | in     | K < B      | $A_2 - A_3 + A_4$       |
| Reverse up-and-in put      | $-1$   | $-1$   | in     | K > B      | $A_1 - A_2 + A_4$       |
| Standard up-and-in put     | $-1$   | $-1$   | in     | $K \leq B$ | $A_3$                   |
| Standard down-and-in call  | $+1$   | $+1$   | in     | K > R      | $A_3$                   |
| Reverse down-and-in call   | $+1$   | $+1$   | in     | $K \leq B$ | $A_1 - A_2 + A_4$       |
| Reverse down-and-in put    | $-1$   | $+1$   | in     | K > B      | $A_2 - A_3 + A_4$       |
| Standard down-and-in put   | $-1$   | $+1$   | in     | K < B      | $A_1$                   |
| Standard up-and-out call   | $+1$   | $-1$   | out    | K > R      | 0                       |
| Reverse up-and-out call    | $+1$   | $-1$   | out    | K < B      | $A_1 - A_2 + A_3 - A_4$ |
| Reverse up-and-out put     | $-1$   | $-1$   | out    | K > B      | $A_2 - A_4$             |
| Standard up-and-out put    | $-1$   | $-1$   | out    | $K \leq B$ | $A_1 - A_3$             |
| Standard down-and-out call | $+1$   | $+1$   | out    | K > B      | $A_1 - A_3$             |
| Reverse down-and-out call  | $+1$   | $+1$   | out    | K < B      | $A_2 - A_4$             |
| Reverse down-and-out put   | $-1$   | $+1$   | out    | K > B      | $A_1 - A_2 + A_3 - A_4$ |
| Standard down-and-out put  | $-1$   | $+1$   | out    | $K \leq B$ | 0                       |

# **Digital and Touch Options**

Digital Options

Digital options have a payoff

$$v(T, S_T) = I_{\{\phi S_T \ge \phi K\}}$$
 domestic paying (15)

$$w(T, S_T) = S_T \mathbb{I}_{\{\phi S_T > \phi K\}}$$
 foreign paying (16)

In the domestic paying case, the payment of the fixed amount is in domestic currency, whereas in the foreign paying case the payment is in foreign currency. We obtain for the value functions

$$v(t,x) = D_d \mathcal{N}(\phi d_-) \tag{17}$$

$$w(t, x) = x D_f \mathcal{N}(\phi d_+) \tag{18}$$

of the digital options paying one unit of domestic and paying one unit of foreign currency, respectively.

#### One-touch Options

The payoff of a one-touch is given by

$$R\,I\!I_{\{\tau_B\leq T\}}\tag{19}$$

$$\tau_B \stackrel{\Delta}{=} \inf\{t \ge 0 : \eta S_t \le \eta B\} \tag{20}$$

This type of option pays a domestic cash amount  $R$  if a barrier  $B$  is hit any time before the expiration time. We use the binary variable  $\eta$  to describe whether B is a lower barrier  $(\eta = 1)$  or an upper barrier  $(\eta = -1)$ . The stopping time  $\tau_B$  is called the first hitting time. In FX markets, an option with this payoff is usually called a one-touch (option), onetouch-digital, or hit option. The modified payoff of a *no-touch* (*option*),  $RI_{\{\tau_R>T\}}$  describes a rebate, which is paid if a knock-in-option is not knocked-in by the time it expires and can be valued similarly by exploiting the identity

$$R\mathbf{I}_{\{\tau_B \le T\}} + R\mathbf{I}_{\{\tau_B > T\}} = R \tag{21}$$

Furthermore, we distinguish the time at which the rebate is paid and let

$$\omega = 0$$
, if the rebate is paid at first hitting time  $\tau_B$ 

$$\omega = 1$$
, if the rebate is paid at maturity time T

where the former is also called instant one-touch and the latter is the default in FX options markets. It is important to mention that the payoff is one unit of the domestic currency. For a payment in the foreign currency EUR, one needs to exchange  $r_d$  and  $r_f$ , replace x and B by their reciprocal values, and change the sign of  $\eta$ ; see Foreign Exchange Symmetries.

For the one-touch, we use the abbreviations

$$\vartheta_{-} \stackrel{\Delta}{=} \sqrt{\theta_{-}^{2} + 2(1 - \omega)r_{d}} \quad \text{and}$$
$$e_{\pm} \stackrel{\Delta}{=} \frac{\pm \ln \frac{x}{B} - \sigma \vartheta_{-} \tau}{\sigma \sqrt{\tau}} \tag{24}$$

The theoretical value of the one-touch turns out to be

$$v(t,x) = Re^{-\omega r_d \tau}$$
$$\times \left[ \left(\frac{B}{x}\right)^{\frac{\theta_- + \theta_-}{\sigma}} \mathcal{N}(-\eta e_+) + \left(\frac{B}{x}\right)^{\frac{\theta_- - \theta_-}{\sigma}} \mathcal{N}(\eta e_-) \right]$$
(25)

Note that  $\vartheta_- = |\theta_-|$  for rebates paid-at-end ( $\omega = 1$ ).

The risk-neutral probability of knocking out is given by

$$\mathbb{I}\!\!P[\tau_B \le T] = \mathbb{I}\!\!E\left[\mathbb{I}\!\!I_{\{\tau_B \le T\}}\right] = \frac{1}{R} e^{r_d T} v(0, S_0) \quad (26)$$

Properties of the First Hitting Time  $\tau_B$ . As derived, for example, in [15], the first hitting time

$$\tilde{\tau} \stackrel{\Delta}{=} \inf\{t \ge 0 : \theta t + W(t) = x\} \tag{27}$$

of a Brownian motion with drift  $\theta$  and hit level  $x > 0$ has the density

$$\begin{aligned} &IP[\tilde{\tau} \in \mathrm{d}t] \\ &= \frac{x}{t\sqrt{2\pi t}} \exp\left\{-\frac{(x-\theta t)^2}{2t}\right\} \mathrm{d}t, \quad t > 0 \quad (28) \end{aligned}$$

the cumulative distribution function

$$\begin{split} \mathit{IP}[\tilde{\tau} \leq t] &= \mathcal{N}\bigg(\frac{\theta t - x}{\sqrt{t}}\bigg) \\ &+ \mathrm{e}^{2\theta x} \mathcal{N}\bigg(\frac{-\theta t - x}{\sqrt{t}}\bigg), \quad t > 0 \quad (29) \end{split}$$

the Laplace transform

$$\mathbb{E}e^{-\alpha\tilde{\tau}} = \exp\left\{x\theta - x\sqrt{2\alpha + \theta^2}\right\}, \quad \alpha > 0, \quad x > 0$$
(30)

and the property

$$\mathit{IP}[\tilde{\tau} < \infty] = \begin{cases} 1 & \text{if } \theta \ge 0 \\ e^{2\theta x} & \text{if } \theta < 0 \end{cases} \tag{31}$$

For upper barriers  $B > S_0$ , we can now rewrite the first passage time  $\tau_B$  as

$$\tau_B = \inf\{t \ge 0 : S_t = B\}$$
$$= \inf\left\{t \ge 0 : W_t + \theta_- t = \frac{1}{\sigma} \ln\left(\frac{B}{S_0}\right)\right\} \quad (32)$$

The density of  $\tau_B$  is hence

$$IP[\tilde{\tau_B} \in dt] = \frac{\frac{1}{\sigma} \ln\left(\frac{B}{S_0}\right)}{t\sqrt{2\pi t}}$$
$$\times \exp\left\{-\frac{\left(\frac{1}{\sigma} \ln\left(\frac{B}{S_0}\right) - \theta_{-t}\right)^2}{2t}\right\}, \quad t > 0$$
(33)

Derivation of the value function. Using the density (33), the value of the paid-at-end ( $\omega = 1$ ) upper rebate ( $\eta = -1$ ) option can be written as the following integral:

$$v(T, S_0) = Re^{-r_d T} \mathbb{E} \left[ \mathbb{I}_{\{\tau_B \le T\}} \right]$$
  
$$= Re^{-r_d T} \int_0^T \frac{\frac{1}{\sigma} \ln \left(\frac{B}{S_0}\right)}{t \sqrt{2\pi t}}$$
  
$$\times \exp \left\{ -\frac{\left(\frac{1}{\sigma} \ln \left(\frac{B}{S_0}\right) - \theta_{-t}\right)^2}{2t} \right\} dt \quad (34)$$

To evaluate this integral, we introduce the notation

$$\mathbf{e}_{\pm}(t) \triangleq \frac{\pm \ln \frac{S_0}{B} - \sigma \theta_{-} t}{\sigma \sqrt{t}} \tag{35}$$

and list the properties

$$e_{-}(t) - e_{+}(t) = \frac{2}{\sqrt{t}} \frac{1}{\sigma} \ln\left(\frac{B}{S_0}\right)$$
 (36)

$$n(\mathbf{e}_{+}(t)) = \left(\frac{B}{S_{0}}\right)^{-\frac{2\theta_{-}}{\sigma}} n(\mathbf{e}_{-}(t)) \quad (37)$$

$$\frac{\partial \mathbf{e}_{\pm}(t)}{\partial t} = \frac{\mathbf{e}_{\mp}(t)}{2t} \tag{38}$$

We evaluate the integral in equation  $(34)$  by rewriting the integrand in such a way that the coefficients of the exponentials are the inner derivatives of the exponentials using properties  $(36)$ – $(38)$ .

$$\begin{split} &\int_{0}^{T} \frac{\frac{1}{\sigma} \ln\left(\frac{B}{S_{0}}\right)}{t\sqrt{2\pi t}} \exp\left\{-\frac{\left(\frac{1}{\sigma} \ln\left(\frac{B}{S_{0}}\right) - \theta_{-}t\right)^{2}}{2t}\right\} dt \\ &= \frac{1}{\sigma} \ln\left(\frac{B}{S_{0}}\right) \int_{0}^{T} \frac{1}{t^{(3/2)}} n(\mathbf{e}_{-}(t)) dt \\ &= \int_{0}^{T} \frac{1}{2t} n(\mathbf{e}_{-}(t)) [\mathbf{e}_{-}(t) - \mathbf{e}_{+}(t)] dt \\ &= -\int_{0}^{T} n(\mathbf{e}_{-}(t)) \frac{\mathbf{e}_{+}(t)}{2t} + \left(\frac{B}{S_{0}}\right)^{\frac{2\theta_{-}}{\sigma}} n(\mathbf{e}_{+}(t)) \frac{\mathbf{e}_{-}(t)}{2t} dt \\ &= \left(\frac{B}{S_{0}}\right)^{\frac{2\theta_{-}}{\sigma}} \mathcal{N}(\mathbf{e}_{+}(T)) + \mathcal{N}(-\mathbf{e}_{-}(T)) \end{split} \tag{39}$$

The computation for lower barriers ( $\eta = 1$ ) is similar.

### Double-no-touch Options

A double-no-touch with payoff function

$$I_{\{L < \min_{t \in [0,T]} S_t \le \max_{t \in [0,T]} S_t < H\}}$$
(40)

pays one unit of domestic currency at maturity  $T$ , if the spot never touches any of the two barriers, where the lower barrier is denoted by  $L$ , the higher barrier by  $H$ . A *double-one-touch* pays one unit of domestic currency at maturity, if the spot either touches or crosses any of the lower or higher barrier at least once between inception of the trade and maturity. This means that a portfolio of a doubleone-touch and a double-no-touch is equivalent to a certain payment of one unit of domestic currency at maturity.

To compute the value, let us introduce the stopping time

$$\tau_{L,H} \stackrel{\Delta}{=} \min \{ \inf \{ t \in [0,T] | S_t = L \text{ or } S_t = H \}, T \}$$
(41)

and the notation

$$\tilde{h} \stackrel{\Delta}{=} \frac{1}{\sigma} \ln \frac{H}{S_t} \tag{42}$$

$$\tilde{l} \triangleq \frac{1}{\sigma} \ln \frac{L}{S_t} \tag{43}$$

$$\tilde{\theta}_{\pm} \stackrel{\Delta}{=} \theta_{\pm} \sqrt{\tau} \tag{44}$$

$$h \stackrel{\Delta}{=} \tilde{h}/\sqrt{\tau} \tag{45}$$

$$l \stackrel{\Delta}{=} \tilde{l}/\sqrt{\tau} \tag{46}$$

$$\epsilon_{\pm} \stackrel{\Delta}{=} \epsilon_{\pm}(j) = 2j(h-l) - \tilde{\theta}_{\pm} \n$$
(47)

$$n_T(x) \triangleq \frac{1}{\sqrt{2\pi T}} \exp\left(-\frac{x^2}{2T}\right) \tag{48}$$

At any time  $t < \tau_{L,H}$ , the value of the double-notouch is

$$v(t) = I\!E^{t} \left[ D_{d} I\!I_{\{L < \min_{t \in [0,T]} S_{t} \le \max_{t \in [0,T]} S_{t} < H\}} \right]$$
(49)

and for  $t \in [\tau_{L,H}, T]$ ,

$$v(t) = D_d \, \mathbf{I}_{\{L < \min_{t \in [0,T]} S_t \le \max_{t \in [0,T]} S_t < H\}} \tag{50}$$

The joint distribution of the maximum and the minimum of a Brownian motion can be taken from  $[12]$  and is given by

$$\mathit{IP}\left[\tilde{l} < \min_{[0,T]} W_t \le \max_{[0,T]} W_t < \tilde{h}\right] = \int_{\tilde{l}}^{\tilde{h}} k_T(x) \, \mathrm{d}x \tag{51}$$

with

$$k_T(x) = \sum_{j=-\infty}^{\infty} \left[ n_T(x+2j(\tilde{h}-\tilde{l})) - n_T(x-2\tilde{h}+2j(\tilde{h}-\tilde{l})) \right]$$
(52)

One can use Girsanov's theorem (see **Equivalent** Martingale Measures) to deduce that the joint density of the maximum and the minimum of a Brownian motion with drift  $\theta$ ,  $W_t^{\theta} \stackrel{\Delta}{=} W_t + \theta t$ , is then given by

$$k_T^{\theta}(x) \stackrel{\Delta}{=} k_T(x) \exp\left\{\theta x - \frac{1}{2}\theta^2 T\right\} \tag{53}$$

We obtain for the value of the double-no-touch at any time  $t < \tau_{L,H}$ 

$$v(t, S_{t}) = D_{d} \mathbb{E} \mathbb{I} \left\{_{L < \min_{u \in [t, T]} S_{u} \le \max_{u \in [t, T]} S_{u} < H} \right\}$$
  

$$= D_{d} \mathbb{E} \mathbb{I} \left\{_{\tilde{l} < \min_{u \in [t, T]} W_{u}^{\theta_{-}} \le \max_{u \in [t, T]} W_{u}^{\theta_{-}} < \tilde{h}} \right\}$$
  

$$= D_{d} \int_{\tilde{l}}^{\tilde{h}} k_{(T - t)}^{\theta_{-}}(x) dx$$
  

$$= D_{d} \cdot \sum_{j = -\infty}^{\infty} \left[ e^{-2j\tilde{\theta}_{-}(h - l)} \times \left\{ \mathcal{N}(h + \epsilon_{-}) - \mathcal{N}(l + \epsilon_{-}) \right\} - e^{-2j\tilde{\theta}_{-}(h - l) + 2\tilde{\theta}_{-} h} \times \left\{ \mathcal{N}(h - 2h + \epsilon_{-}) - \mathcal{N}(l - 2h + \epsilon_{-}) \right\} \right]$$
  
(54)

and for  $t \in [\tau_{L,H}, T]$ 

$$v(t, S_t) = D_d \, \mathbb{I}_{\{L < \min_{u \in [t,T]} S_u \le \max_{u \in [t,T]} S_t < H\}} \tag{55}$$

Of course, the value of the double-one-touch is given by

$$D_d - v(t, S_t) \tag{56}$$

To obtain a formula for a double-no-touch paying foreign currency, see Foreign Exchange Symmetries.

## **Lookback Options**

**Lookback** options are path dependent. At expiration, the holder of the option can "look back" over the lifetime of the option and exercise based upon the optimal underlying value (extremum) achieved during that period. Thus, lookback options (like Asian **options**) avoid the problem of European options that the underlying performed favorably throughout most of the option's lifetime but moves into a nonfavorable direction toward maturity. Moreover, (unlike American Options) lookback options optimize the market timing, because the investor gets, by definition, the most favorable underlying price. As summarized in Table 3, **lookback** options can be structured in two different types with the extremum representing either the strike price or the underlying value. Figure 1 shows the development of the payoff of lookback options depending on a sample price path. In detail, we define

$$M_T \stackrel{\Delta}{=} \max_{0 \le u \le T} S(u) \quad \text{and} \quad m_T \stackrel{\Delta}{=} \min_{0 \le u \le T} S(u) \quad (57)$$

Variations of lookback options include *partial* lookback options, where the monitoring period for the underlying is shorter than the lifetime of the option. Conze and Viswanathan [2] present further variations like *limited risk* and *American lookback* options.

In theory, Garman pointed out in [4], that lookback options can also add value for risk managers, because floating (fixed) strike lookback options are good means to solve the timing problem of market entries (exits) (see [9]). For instance, a minimum strike call is suitable for avoiding missing the best

**Table 3** Types of lookback options. The contract parameters  $T$  and  $X$  are the time to maturity and the strike price, respectively, and  $S_T$  denotes the spot price at expiration time. Fixed strike lookback options are also called *hindsight* options

| Payoff        | Lookback type        | Parameter used below<br>in valuation |
|---------------|----------------------|--------------------------------------|
| $M_T - S_T$   | Floating strike put  | $\phi = -1, \bar{\eta} = +1$         |
| $S_T - m_T$   | Floating strike call | $\phi = +1, \bar{\eta} = +1$         |
| $(M_T - X)^+$ | Fixed strike call    | $\phi = +1, \bar{\eta} = -1$         |
| $(X-m_T)^+$   | Fixed strike put     | $\phi = -1, \bar{\eta} = -1$         |

exchange rate in currency-linked security issues. However, this right is very expensive. Since one buys a guarantee for the best possible exchange rate ever, lookback options are generally too expensive and hardly ever trade. Exceptions are performance notes, where lookback and average features are mixed, for example, performance notes paying say  $50\%$  of the best of 36 monthly average gold price returns.

#### Valuation

We consider the example of the floating strike lookback call. Again, the value of the option is given by

$$v(0, S_0) = \mathbb{E} \left[ e^{-r_d T} (S_T - m_T) \right]$$
  
=  $S_0 e^{-r_f T} - e^{-r_d T} \mathbb{E} \left[ m_T \right]$  (58)

![](_page_5_Figure_11.jpeg)

**Figure 1** Payoff profile of lookback calls (sample underlying price path,  $m = 20$  trading days)

In the standard Black-Scholes model (1), the value can be derived using the reflection principle and results in

$$v(t,x) = \phi \left\{ x D_f \mathcal{N}(\phi d_+) - K D_d \mathcal{N}(\phi d_-) \right.$$
$$\left. + \frac{1-\eta}{2} \phi D_d [\phi (R-X)]^+ \right.$$
$$\left. + \eta x D_d \frac{1}{h} \left[ \left(\frac{x}{K}\right)^{-h} \mathcal{N}(-\eta \phi (d_+ - h\sigma \sqrt{\tau})) \right] \right\}$$
(59)

This value function has a removable discontinuity at  $h = 0$  where it turns out to be

$$v(t,x) = \phi \left\{ x D_f \mathcal{N}(\phi d_+) - K D_d \mathcal{N}(\phi d_-) \right.$$
$$\left. + \frac{1-\eta}{2} \phi D_d [\phi (R-X)]^+ \right.$$
$$\left. + \eta x D_d \sigma \sqrt{\tau} \left[ -d_+ \mathcal{N}(-\eta \phi d_+) \right] \right\}$$
(60)

The abbreviations we use are

$$h \triangleq \frac{2(r_d - r_f)}{\sigma^2} \tag{61}$$

 $R \stackrel{\Delta}{=}$  running extremum: extremum observed

until valuation time  $(62)$ 

$$K \stackrel{\Delta}{=} \begin{cases} R & \text{floating strike lookback} \\ -\phi \min(-\phi X, -\phi R) & \text{fixed strike lookback} \end{cases} \tag{63}$$

$$\eta \triangleq \begin{cases}\n+1 & \text{floating strike lookback} \\
-1 & \text{fixed strike lookback}\n\end{cases} \tag{64}$$

Note that this formula basically consists of that for a **call option** (the first two terms) plus another term. Conze and Viswanathan also show closed-form solutions for fixed strike lookback options and the variations mentioned above in [2]. Heynen and Kat develop equations for *partial fixed and floating strike* 

Table 4 Sample values for lookback options. For the input data, we used spot  $S_0 = 0.9800, r_d = 3\%, r_f = 6\%,$  $\sigma = 10\%, \tau = 1/12$ , running min  $R = 0.9500$ , running max  $R = 0.9900$ , and number of equidistant fixings  $m = 22$ 

| Payoff sampled   | Discretely sampled<br>Equations $(67)$<br>and $(68)$ | Continuously<br>Equations $(59)$<br>or $(60)$ |
|------------------|------------------------------------------------------|-----------------------------------------------|
| $M_T - S_T$      | 0.0231                                               | 0.0255                                        |
| $S_T - m_T$      | 0.0310                                               | 0.0320                                        |
| $(M_T - 0.99)^+$ | 0.0107                                               | 0.0131                                        |
| $(0.97 - m_T)^+$ | 0.0235                                               | 0.0246                                        |

*lookback options* in [10]. We list some sample results in Table 4.

### Discrete Sampling

In practice, one cannot take the average over a continuum of exchange rates. The standard is to specify a fixing calendar and take only a finite number of fixings into account. Suppose there are  $m$  equidistant sample points left until expiration at which we evaluate the extremum. In this case, the value function  $v_m$  can be determined by an approximation described by Broadie et al. [1]. We set

$$\begin{array}{l} \beta \stackrel{\Delta}{=} -\zeta(1/2)/\sqrt{2\pi} \\ \\ = 0.5826 \quad (\zeta \text{ being Riemann's } \zeta\text{-function}) \quad (65) \\ \\ \alpha \stackrel{\Delta}{=} e^{\phi\beta\sigma}\sqrt{\tau/m} \quad (66) \end{array}$$

and obtain for fixed strike lookback options

$$v_m(t, x, r_d, r_f, \sigma, R, X, \phi, \eta)$$
  
=  $v(t, x, r_d, r_f, \sigma, \alpha R, \alpha X, \phi, \eta)/\alpha$  (67)

and for floating strike lookback options

$$v_m(t, x, r_d, r_f, \sigma, R, X, \phi, \eta)$$
  
=  $av(t, x, r_d, r_f, \sigma, R/\alpha, X, \phi, \eta) - \phi(\alpha - 1)xD_f$   
(68)

### **Forward Start Options**

#### Product Definition

A forward start vanilla option is just like a vanilla option, except that the strike is fixed on some future date  $t_f \in (0, T)$ , specified in the contract. The strike is fixed as  $\alpha S_{t_{\ell}}$ , where  $\alpha > 0$  is some contractually defined factor (very common one) and  $S_{t_f}$  is the spot at time  $t_f$ . It pays off

$$[\phi(S_T - \alpha S_{t_f})]^+ \tag{69}$$

The Value of Forward Start Options

Using the abbreviations

$$d_{\pm}(x) \triangleq \frac{\ln \frac{x}{K} + \sigma \theta_{\pm}(T - t_f)}{\sigma \sqrt{T - t_f}} \tag{70}$$

$$d_{\pm}^{\alpha} \stackrel{\Delta}{=} \frac{-\ln\alpha + \sigma\theta_{\pm}(T - t_f)}{\sigma\sqrt{T - t_f}} \tag{71}$$

we recall the value of a vanilla option with strike  $K$ at time  $t_f$  as

$$\text{vanilla}(t_f, x; K, T, \phi)$$
  
=  $\phi \left[ x e^{-r_f(T - t_f)} \mathcal{N}(\phi d_+(x)) - K e^{-r_d(T - t_f)} \mathcal{N}(\phi d_-(x)) \right]$   
(72)

For the value of a forward start vanilla option, we obtain

$$v(0, S_0)$$
  
=  $e^{-r_d t_f} \mathbb{I} \mathbb{E} \left[ \text{vanilla}(t_f, S_{t_f}; K = \alpha S_{t_f}, T, \phi) \right]$   
=  $\phi S_0 \left[ e^{-r_f T} \mathcal{N}(\phi d_+^{\alpha}) - \alpha e^{(r_d - r_f) t_f} e^{-r_d T} \mathcal{N}(\phi d_-^{\alpha}) \right]$   
(73)

Noticeably, the value computation is easy here, because the strike  $K$  is set as a *multiple* of the future spot. If we were to choose to set the strike as a constant *difference* of the future spot, the integration would not work in closed form, and we would have to use numerical integration.

Table 5 Value of a forward start vanilla in USD on EUR/USD—spot of 0.9000,  $\alpha = 99\%$ ,  $\sigma = 12\%$ ,  $r_d = 2\%$ ,  $r_f = 3\%$ , maturity  $T = 186$  days, and strike set at  $t_f = 90$ days

|       | Call   | Put    |
|-------|--------|--------|
| Value | 0.0251 | 0.0185 |

#### Example

We consider an example in Table 5.

### **Compound and Instalment Options**

An instalment call option allows the holder to pay the premium of the **call option** in instalments spread over time. A first payment is made at the inception of the trade. On the following payment days, the holder of the instalment call can decide to prolong the contract, in which case, he has to pay the second instalment of the premium, or to terminate the contract by simply not paying any more. After the last instalment payment, the contract turns into a plain vanilla call.

#### Valuation in the Black–Scholes Model

The intention of this section is to obtain a closedform formula for the  $n$ -variate instalment option in the **Black–Scholes model**. For the cases  $n = 1$ and  $n = 2$ , the Black-Scholes formula and Geske's compound option formula (see [5]) are well-known special cases.

Let  $t_0 = 0$  be the instalment option inception date and  $t_1, t_2, \ldots, t_n = T$  a schedule of decision dates in the contract on which the option holder has to pay the premiums  $k_1, k_2, \ldots, k_{n-1}$  to keep the option alive. To compute the price of the instalment option, which is the upfront payment  $V_0$  at  $t_0$  to enter into the contract, we begin with the option payoff at maturity  $T$ 

$$V_n(s) \stackrel{\Delta}{=} [\phi_n(s-k_n)]^+ \stackrel{\Delta}{=} \max[\phi_n(s-k_n), 0] \tag{74}$$

where  $s = S_T$  is the price of the underlying asset at T and as usual  $\phi_n = +1$  for a call option,  $\phi_n = -1$ for a put option.

At time  $t_i$ , the option holder can either terminate the contract or pay  $k_i$  to continue. This means that the instalment option can be viewed as an option with strike  $k_1$  on an option with strike  $k_2 \cdots$  on an option with strike  $k_n$ . Therefore, by the **risk-neutral pricing** theory, the holding value is

$$e^{-r_d(t_{i+1}-t_i)} \mathbb{I}E[V_{i+1}(S_{t_{i+1}}) | S_{t_i} = s],$$
  
for  $i = 0, \dots, n-1$  (75)

where

$$V_i(s) = \begin{cases} \left[ e^{-r_d(t_{i+1}-t_i)} \middle| E[V_{i+1}(S_{t_{i+1}}) \middle| S_{t_i} = s] - k_i \right]^+ \\ \text{for } i = 1, \dots, n-1 \\ V_n(s) \quad \text{for } i = n \end{cases}$$
(76)

Then the unique arbitrage-free time-zero value is

$$P \stackrel{\Delta}{=} V_0(s) = e^{-r_d(t_1 - t_0)} \mathbb{I} E[V_1(S_{t_1}) \mid S_{t_0} = s] \quad (77)$$

Figure 2 illustrates this context.

One way of pricing this instalment option is to evaluate the nested expectations through multiple numerical integration of the payoff functions via backward iteration. Alternatively, one can derive a solution in closed form in terms of the  $n$ -variate cumulative normal, which is described in the following.

# The Curnow and Dunnett Integral Reduction Technique

Denote the  $n$ -dimensional multivariate normal integral with upper limits  $h_1, \ldots, h_n$  and correlation matrix  $R_n \stackrel{\Delta}{=} (\rho_{ij})_{i,j=1,\ldots,n}$  by  $\mathcal{N}_n(h_1,\ldots,h_n;R_n)$ .<br>Let the correlation matrix be nonsingular and  $\rho_{11} = 1.$ 

Under these conditions, Curnow and Dunnett [3] derived the following reduction formula for multivariate normal integrals:

$$\mathcal{N}_{n}(h_{1},\cdots,h_{n};R_{n})$$

$$= \int_{-\infty}^{h_{1}} \mathcal{N}_{n-1} \left(\frac{h_{2}-\rho_{21}y}{(1-\rho_{21}^{2})^{1/2}},\cdots,\frac{h_{n}-\rho_{n1}y}{(1-\rho_{n1}^{2})^{1/2}};R_{n-1}^{*}\right) n(y) \, \mathrm{d}y,$$

$$R_{n-1}^{*} \triangleq (\rho_{ij}^{*})_{i,j=2,\ldots,n},$$

$$\rho_{ij}^{*} \triangleq \frac{\rho_{ij}-\rho_{i1}\rho_{j1}}{(1-\rho_{i1}^{2})^{1/2}(1-\rho_{j1}^{2})^{1/2}} \tag{78}$$

For example, to go from dimension 1 to dimension 2, this takes the form

$$\int_{-\infty}^{x} \mathcal{N}(az+B)n(z) dz$$
  
=  $\mathcal{N}_{2}\left(x, \frac{B}{\sqrt{1+a^{2}}}; \frac{-a}{\sqrt{1+a^{2}}}\right)$  (79)

or more generally,

$$\int_{-\infty}^{x} e^{Az} \mathcal{N}(az+B)n(z) dz$$
  
=  $e^{\frac{A^2}{2}} \mathcal{N}_2 \left(x-A, \frac{aA+B}{\sqrt{1+a^2}}; \frac{-a}{\sqrt{1+a^2}}\right)$  (80)

![](_page_8_Figure_18.jpeg)

**Figure 2** Lifetime of the options  $V_i$ 

# A Closed-form Solution for the Value of an Instalment Option

Heuristically, the formula which is given in the Theorem 1 has the structure of the **Black–Scholes formula** in higher dimensions, namely,  $S_0\mathcal{N}_n(\cdot)$  –  $k_n \mathcal{N}_n(\cdot)$  minus the later premium payments  $k_i \mathcal{N}_i(\cdot)$ 

**Theorem 1** Let  $\mathbf{k} = (k_1, \ldots, k_n)$  be the strike price *vector*,  $\mathbf{t} = (t_1, \ldots, t_n)$  *the vector of the exercise* dates of an n-variate instalment option and  $\boldsymbol{\phi} =$  $(\phi_1,\ldots,\phi_n)$  the vector of the put/call-indicators of  $\text{these } n \text{ options.}$ 

The value function of an n-variate instalment option is given by

$$V_n(S_0, \mathbf{k}, \mathbf{t}, \boldsymbol{\phi})$$

$$= e^{-r_{f}t_{n}} S_{0}\phi_{1} \cdots \phi_{n} \times \mathcal{N}_{n} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{+}t_{1}}{\sigma\sqrt{t_{1}}}, \phi_{2} \frac{\ln \frac{S_{0}}{S_{2}^{*}} + \sigma\theta_{+}t_{2}}{\sigma\sqrt{t_{2}}}, \ldots, \phi_{n} \frac{\ln \frac{S_{0}}{S_{n}^{*}} + \sigma\theta_{+}t_{n}}{\sigma\sqrt{t_{n}}}; R_{n} \right]$$

$$-e^{-r_{d}t_{n}} k_{n} \phi_{1} \cdots \phi_{n} \times \mathcal{N}_{n} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{-}t_{1}}{\sigma\sqrt{t_{1}}}, \phi_{2} \frac{\ln \frac{S_{0}}{S_{2}^{*}} + \sigma\theta_{-}t_{2}}{\sigma\sqrt{t_{2}}}, \ldots, \phi_{n} \frac{\ln \frac{S_{0}}{S_{n}^{*}} + \sigma\theta_{-}t_{n}}{\sigma\sqrt{t_{n}}}; R_{n} \right]$$

$$-e^{-r_{d}t_{n}} k_{n} \phi_{1} \cdots \phi_{n} \times \mathcal{N}_{n} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{-}t_{1}}{\sigma\sqrt{t_{1}}}, \phi_{2} \frac{\ln \frac{S_{0}}{S_{2}^{*}} + \sigma\theta_{-}t_{2}}{\sigma\sqrt{t_{2}}}, \ldots, \phi_{n} \frac{\ln \frac{S_{0}}{S_{n}^{*}} + \sigma\theta_{-}t_{n}}{\sigma\sqrt{t_{n}}}; R_{n} \right]$$

$$\vdots$$

$$-e^{-r_{d}t_{n-1}} k_{n-1} \phi_{1} \cdots \phi_{n-1} \times \mathcal{N}_{n-1} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{-}t_{1}}{\sigma\sqrt{t_{1}}}, \phi_{2} \frac{\ln \frac{S_{0}}{S_{2}^{*}} + \sigma\theta_{-}t_{2}}{\sigma\sqrt{t_{2}}}, \ldots, \phi_{n-1} \frac{\ln \frac{S_{0}}{S_{n-}^{*}} + \sigma\theta_{-}t_{n-1}}{\sigma\sqrt{t_{n-1}}}; R_{n-1} \right]$$

$$\vdots$$

$$-e^{-r_{d}t_{2}} k_{2} \phi_{1} \phi_{2} \mathcal{N}_{2} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{-}t_{1}}{\sigma\sqrt{t_{1}}}, \phi_{2} \frac{\ln \frac{S_{0}}{S_{2}^{*}} + \sigma\theta_{-}t_{2}}{\sigma\sqrt{t_{2}}}; \rho_{12} \right]$$

$$-e^{-r_{d}t_{1}} k_{1} \phi_{1} \mathcal{N} \left[ \phi_{1} \frac{\ln \frac{S_{0}}{S_{1}^{*}} + \sigma\theta_{-}t_{1}}{\sigma\sqrt{t_{1}}} \right]$$
(81)

 $(i = 1, \ldots, n-1)$ . This structure is a result of the integration of the vanilla option payoff, which is again integrated minus the next instalment, which in turn is integrated with the following instalment and so forth. By this iteration, the vanilla payoff is integrated with respect to the normal density function  $n$  times and the *i*th payment is integrated *i* times for  $i = 1, \ldots, n-1.$ 

The correlation coefficients  $\rho_{ij}$  of these normal distribution functions contained in the formula arise from the overlapping increments of the Brownian motion, which models the price process of the underlying  $S_t$  at the particular exercise dates  $t_i$ and  $t_i$ .

where  $S_i^*$   $(i = 1, ..., n)$  is to be determined as the spot price  $S_t$  for which the payoff of the corresponding *i-variate instalment option*  $(i = 1, ..., n)$  *is equal to* 0, that is,  $V_i(S_i^*, \mathbf{k}, \mathbf{t}, \boldsymbol{\phi}) = 0$ . This has to be done numerically by a zero search.

The correlation coefficients in  $R_i$  of the *i*-variate normal distribution function can be expressed through the exercise dates  $t_i$ ,

$$\rho_{ij} = \sqrt{t_i/t_j} \text{ for } i, j = 1, ..., n \text{ and } i < j$$
 (82)

The proof is established with equation (78). Formula  $(81)$  has been independently derived by Thomassen and Wouve in [16] and Griebsch et al. in [6].

# **References**

- [1] Broadie, M. Glasserman, P. & Kou, S.G. (1999). Connecting discrete and continuous path-dependent options, *Finance and Stochastics* **3**(1), 55–82.
- [2] Conze, A. & Viswanathan, R. (1991). Path dependent options: the case of lookback options, *The Journal of Finance*, **XLVI**(5), 1893–1907.
- [3] Curnow, R.N. & Dunnett, C.W. (1962). The numerical evaluation of certain multivariate normal integrals, *Annals of Mathematical Statistics* **33**, 571–579.
- [4] Garman, M. (1989). Recollection in tranquillity,, reedited version, in *From Black Scholes to Black Holes*, Originally in Risk Publications, London, pp. 171–175.
- [5] Geske, R. (1979). The valuation of compound options, *Journal of Financial Economics* **7**, 63–81.
- [6] Griebsch, S.A. Kuhn, C. & Wystup, U. (2008). Instal- ¨ ment options: a closed-form solution and the limiting case, in Contribution to *Mathematical Control Theory and Finance*, A. Sarychev, A. Shiryaev, M. Guerra, & M.R. Grossinho, eds, Springer, pp. 211–229.
- [7] Hakala, J. & Wystup, U. (2002). *Foreign Exchange Risk*, Risk Publications, London.
- [8] Haug, E.G. (1997). *Option Pricing Formulas*, McGraw Hill.
- [9] Heynen, R. & Kat, H. (1994). Selective memory: reducing the expense of lookback options by limiting their memory, re-edited version, in *Over the Rainbow: Developments in Exotic Options and Complex Swaps*, Risk Publications, London.

- [10] Heynen, R. & Kat, H. (1994). Crossing barriers, *Risk* **7**(6), 46–51.
- [11] Lipton, A. (2001). *Mathematical Methods for Foreign Exchange*, World Scientific, Singapore.
- [12] Revuz, D. & Yor, M. (1995). *Continuous Martingales and Brownian Motion*, 2nd Edition, Springer.
- [13] Rich, D. (1994). The mathematical foundations of barrier option pricing theory, *Advances in Futures and Options Research* **7**, 267–371.
- [14] Reiner, E. & Rubinstein, M. (1991). Breaking down the barriers, *Risk* **4**(8), 28–35.
- [15] Shreve, S.E. (2004). *Stochastic Calculus for Finance I+II*, Springer.
- [16] Thomassen, L. & van Wouve, M. (2002). *A Sensitivity Analysis for the N-fold Compound Option*, Research Paper, Faculty of Applied Economics, University of Antwerpen.
- [17] Wystup, U. (2006). *FX Options and Structured Products*, Wiley Finance Series.
- [18] Zhang, P.G. (1998). *Exotic Options*, 2nd Edition, World Scientific, London.

## **Related Articles**

**Barrier Options**; **Black–Scholes Formula**; **Discretely Monitored Options**; **Foreign Exchange Markets**; **Foreign Exchange Options**; **Foreign Exchange Symmetries**; **Lookback Options**.

ANDREAS WEBER & UWE WYSTUP
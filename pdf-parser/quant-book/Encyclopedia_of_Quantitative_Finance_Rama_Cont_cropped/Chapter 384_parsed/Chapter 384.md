# **Ruin Theory**

The earliest ruin problem was formulated by de Moivre around 1730. A gambler has an initial fortune of  $u$  monetary units (an integer). Each time he plays (heads or tails in coin tossing, black or red at the roulette, etc.), his fortune goes one up or down according to whether he wins or loses. If the fortune becomes 0, the gambler is ruined. He decides a pri*ori* to stop gambling if his fortune reaches  $v > u$ . If the probability of a win is p, what is then  $\psi_{v}(u)$ , the probability of getting ruined as opposed to reach the target  $v$ ?

The classical ruin problem of insurance mathematics is rather similar:  $u$  is the initial reserve of the insurance company, and incoming premiums make the reserve go up, payments to insurance holders make it go down. One then considers  $\psi(u)$ , the ruin probability defined as the probability that the reserve ever becomes nonpositive (note that this is a onebarrier problem, whereas the gambler's ruin problem involves two barriers).

A general mathematical formulation of this and related types of problems is a stochastic process  $\{R(t)\}\$  (corresponding to the fortune of the gambler or the insurance company at time  $t$ ) and the stopping times

$$\tau_v(u) = \inf\{t : R(t) \notin (0, v) | R(0) = u\}$$
  
=  $\inf\{t : R(t) \le 0 \text{ or } R(t) \ge v | R(0) = u\}$   
$$\tau(u) = \inf\{t : R(t) \le 0 | R(0) = u\}$$
 (1)

In broad terms, ruin theory is concerned with deriving properties of these stopping times. In particular, in the two-barrier setting one typically has  $\psi_{v}(u) < \infty$  and could ask for  $\mathbb{P}(R(\tau_v(u)) \ge v)$  or  $\mathbb{P}(R(\tau_v(u)) \le 0)$ . In the one-barrier setting, the main object of interest is the probability  $\psi(u) = \mathbb{P}(\tau(u) < \infty)$  of eventual ruin. Other quantities of interest are the distribution of  $\tau(u)$ , needed to say something about the finite horizon ruin probability  $\psi(u,T) = \mathbb{P}(\tau(u) \leq T)$ , and the deficit  $-R(\tau(u))$  after ruin (see Gerber-Shiu Function).

Ruin problems occur also in finance. A simple example is an equity default swap (see Equity Swaps) that pays a certain amount if a security price drops by a certain amount (say  $50\%$ ) in a time period  $[0, T]$ . The price of the equity default

swap then involves the risk-neutral probability (see **Risk-neutral Pricing**) that this happens, which can easily be represented in the form  $\psi(u, T)$ . A few more examples occur in barrier options (see Barrier **Options**). For example, a digital down-and-in option will pay the amount 1 if the security price  $Z(t)$  goes below L before T, but is above  $K > L$  at time T  $(Z(T) > K)$ . A standard down-and-in option will pay instead  $(Z(T) - K)^{+}$  under the same conditions.

### **Explicit Solutions**

In the rest of the article, we assume that  $\{R(t)\}_{t>0}$ has stationary independent increments (though there is a considerable literature on extensions such as Markovian regime, see **Regime-switching Models**, jumps at the epochs of a renewal process, etc.). Beyond the simple random walk in the gambler's ruin problem, key examples are Brownian motion (with drift  $\mu$  and variance constant  $\sigma^2$ , say) and the Cramér-Lundberg risk model

$$R(t) = u + ct - \sum_{i=1}^{N(t)} V_i$$
 (2)

where  $c$  is the premium rate,  $N$  is the Poisson process of times of arrivals of claims, and  $V_1, V_2, \ldots$  are the claim sizes.

The gambler's ruin problem is easily solvable: conditioning upon the outcome of the first play gives

$$\psi_v(u) = p\psi_v(u+1) + (1-p)\psi_v(u-1) \qquad (3)$$

when  $0 < u < v$ . Subject to the obvious boundary conditions  $\psi_v(0) = 1$ ,  $\psi_v(v) = 0$ , this set of equations has a unique solution that can be seen to be

$$\psi_{v}(u) = \frac{\left[ (1-p)/p \right]^{v} - \left[ (1-p)/p \right]^{u}}{\left[ (1-p)/p \right]^{v} - 1} \qquad (4)$$

(for  $p = 1/2$ , this needs to be modified to  $\psi_{v}(u) =$  $1 - u/v$ ).

What withother models? The simplest example is Brownian motion with drift  $\mu$  and variance  $\sigma^2$ , where conditioning upon  $R(h)$  and letting  $h \downarrow 0$ gives  $\psi_{v}(u) = \mu \psi'_{v}(u) + \sigma^{2} \psi''_{v}(u) / 2$ . Together with  $\psi_v(0) = 1$ ,  $\psi_v(v) = 0$ , this differential equation is easily solved to get

$$\psi_{v}(u) = \frac{e^{-\gamma u} - e^{-\gamma v}}{1 - e^{-\gamma v}} \text{ where } \gamma = 2\mu/\sigma^{2} \quad (5)$$

for *µ >* 0 and *ψv(u)* = 1 − *u/v* for *µ* = 0. A more elegant and general approach uses martingales (*see* **Martingales**). The Wald exponential martingale is

$$W(t) = W_{\alpha}(t) = \exp\{-\alpha R(t) - t\kappa(\alpha)\}\qquad(6)$$

where *κ(α)* = log *Ɛ* {−*αR(*1*)*} (the so-called Levy ´ exponent, *see* **Levy Processes ´** ). A particularly important choice of *α* is *γ* , the nonzero solution of *κ(γ )* = 0 and going under names such as the adjustment coefficient, the Cramer–Lundberg root and so ´ on. Indeed, for this case *W (t)* = exp {−*αR(t)*}, and since *R(τv (u))* = *v* when *R(τv (u))* ≥ *v* (and similarly *R(τv (u))* = 0 when *R(τv (u))* ≤ 0) for Brownian motion, optional stopping gives

$$e^{-\gamma u} = W(0) = \mathbb{E} W(\tau_v(u))$$
  
=  $\psi_v(u)e^0 + (1 - \psi_v(u))e^{-\gamma v}$  (7)

In the Brownian case, *κ(α)* = −*αµ* + *α*<sup>2</sup>*σ*<sup>2</sup>*/*2, and so *γ* = 2*µ/σ*2. Inserting in equation (7) and solving for *ψu(v)*, equation (5) follows easily. For the following, note that

$$\kappa(\alpha) = \lambda \big( \mathbb{E} e^{-\alpha V_i} - 1 \big) + \alpha c \tag{8}$$

for the Cramer–Lundberg model (here ´ *γ* is only explicit for a few examples, in particular exponential *Vi*, cf. equation (11) below).

For further generalizations, basically one needs to be able to say something about the overshoot *R(τv (u))* − *v*, given *R(τv (u))* ≥ *v* and the undershoot −*R(τv (u)* given *R(τv (u))* ≤ 0. A basic example is the Cramer–Lundberg model with the ´ *Vi* exponential, say, at rate *µ*. Then by the memoryless property of the exponential distribution, −*R(τv (u))*, given *R(τv (u))* ≤ 0 is again exponential*(µ)* so that

$$\mathbb{E}\bigl[\exp\left\{\gamma\,R(\tau_v(u))\right\}\bigg|R(\tau_v(u))\leq 0\bigr] = \frac{\mu}{\mu+\gamma} \quad (9)$$

Since *R(τv (u))* = *v* when *R(τv (u))* ≥ *v* (the process has no upward jumps), it follows that

$$e^{-\gamma u} = W(0) = \mathbb{E}W(\tau_v(u))$$
  
=  $\psi_v(u)\frac{\mu}{\mu + \gamma} + (1 - \psi_v(u))e^{-\gamma v}$  (10)

However, if *λ* is the Poisson intensity, then

$$\kappa(\alpha) = \lambda \Big(\frac{\mu}{\mu + \alpha} - 1\Big) + \alpha c \Longrightarrow \gamma = \lambda/c - \mu \tag{11}$$

Solving equation (10) for *ψv(u)* yields an explicit expression for *ψv(u)*, and letting *v* → ∞ we then get one of the classical formulas in ruin theory,

$$\psi(u) = \frac{\lambda}{c\mu} \exp\left\{ -(\lambda/c - \mu)u \right\} \tag{12}$$

in the exponential case.

A generalization of equation (10) is to let the *Vi* be phase-type, say with initial vector *ν*, phase generator *T* and exit rates *t*. Then ([1 p. 227])

$$\psi(u) = \mathbf{v}_{+} \exp\left\{ (\boldsymbol{T} + t\mathbf{v}_{+})u \right\} \text{ where } \mathbf{v}_{+} = -\lambda \boldsymbol{v} \boldsymbol{T}^{-1}/c$$
(13)

The derivation involves some additional steps, but again, the crucial feature is that one can control the undershoot: the distribution of −*R(τv (u))*, given *R(τv (u)))* ≤ 0 is determined by the phase in which 0 is downcrossed. Thus we have a finite set of unknowns, which motivates the matrix form of equation (13).

#### *Bounds and Symptotics*

Formula (13) is more or less the end of the road with regard to explicit solutions, even for the simple Cramer–Lundberg model. Therefore, inequalities and ´ approximations play a major role in the area.

The celebrated *Lundberg's inequality* states that

$$\psi(u) \le \mathrm{e}^{-\gamma u} \tag{14}$$

A simple proof of equation (14) (and many other inequalities and approximations) is to use change of measure: for each *θ* with *κ(θ ) <* ∞, consider the risk process with *λ* changed to *λθ* = *λƐ*e<sup>−</sup>*θVi* and the distribution of *Vi* given by *Ɛ<sup>θ</sup>* e*αVi* = *Ɛ*e*(α*−*θ )Vi /Ɛ*e<sup>−</sup>*θVi* . Then

$$\begin{aligned} \psi(u) &= \mathbb{P}(\tau(u) < \infty) \\ &= \mathbb{E}_{\theta} \exp\left\{\theta \big[ R\big(\tau(u)\big) - u \big] - \theta \kappa(\theta) \tau(u) \right\} \end{aligned} \tag{15}$$

Taking *θ* = *γ* and bounding *R τ (u)*below by 0 immediately yields equation (14). A more elaborate argument involving the *<sup>θ</sup>* -limit distribution of *R τ (u)*gives the other main result in the area, going under the name of the Cramér-Lundberg approximation,

$$\psi(u) \sim Ce^{-\gamma u}, u \to \infty, \text{ where } C = \frac{1 - \kappa'(0)/c}{\kappa'(\gamma)/c - 1}$$
(16)

The results  $(14)$  and  $(17)$ , both require a lighttailed assumption, namely, the existence of  $\gamma$  (and for equation (17) in addition that  $\kappa'(\gamma) < \infty$ ). With heavy tails, the situation is completely different. Assume that  $V$  is subexponential (see Heavy Tails in Insurance; Heavy Tails; for example, the tail is regularly varying,  $\mathbb{P}(V > v) = L(v)/v^{\alpha}$  with  $\alpha > 1$ and  $L(\cdot)$  slowly varying). Then

$$\psi(u) \sim \frac{\lambda/\mathbb{E}V}{(c-\lambda/\mathbb{E}V)\mathbb{E}V} \int_{u}^{\infty} \mathbb{P}(V>y) \, \mathrm{d}y, u \to \infty \tag{17}$$

a result that is often associated with the names (in alphabetical order) of Borovkov, Cohen, Embrechts, Pakes, Veraverbeke, and von Bahr.

#### **Finite Horizon Ruin Probabilities**

The density or the distribution function of  $\tau(u)$  is essentially only explicit for Brownian motion: if  $\sigma^2 = 1$ , then

$$\mathbb{P}_{\mu}\big(\tau(u) \in dt\big)$$

$$= \frac{u}{\sqrt{2\pi}t^{3/2}} \exp\Bigl\{-\mu u - \frac{1}{2}\Bigl(\frac{u^2}{t} + \mu^2 t\Bigr)\Bigr\} \tag{18}$$

However, if one is satisfied with transforms, the situation is somewhat better, at least for the Cramér-Lundberg model: with exponential claims, one has

$$\mathbb{E}\big[e^{-a\tau(u)};\tau(u)<\infty\big] = e^{-\theta u}(1-\theta/\mu) \qquad (19)$$

where  $\theta$  is the largest root of  $\kappa(\theta) = ac$  or, equivalently, of the quadratic  $\theta^2 + (\lambda/c - \mu + ac)\theta - ac\mu$ . For general claim size distributions, one has to go todouble transforms to get a reasonably simple formula:

$$\int_0^\infty e^{bu} \mathbb{E}\left[e^{-a\tau(u)}; \tau(u) < \infty\right] du$$
$$= \frac{-ac/r(a) - \kappa(b)/b}{\kappa(b) + ac} \tag{20}$$

where  $r(a)$  is the smallest solution of  $-ac = \kappa(r(a))$ .

The asymptotics of the ruin time  $\tau(u)$  is, however, well understood. In the light-tailed setting,  $\tau(u)/u$ has limit (conditional upon  $\tau(u) < \infty$ )  $1/\kappa'(\gamma)$  as  $u \rightarrow \infty$ , and there is further a central limit theorem for  $(\tau(u) - u/\kappa'(\gamma))/u^{1/2}$ . In the subexponential case, there is again a limit for  $\tau(u)/c(u)$  for some suitable constants  $c(u) \rightarrow \infty$ ), but the limit is random (e.g., Pareto in the regularly varying case where  $c(u) = u$ ), not constant as for light tails. These statements translate easily into approximations for

$$\begin{aligned} \psi(u,t) &= \mathbb{P}\big(\tau(u) \le t\big) \\ &= \psi(u)\mathbb{P}\big(\tau(u) \le t \big|\tau(u) < \infty\big) \end{aligned} \tag{21}$$

Further approximations worth mentioning are the corrected diffusion approximation and the saddlepoint approximation. For these, as well as the remaining topics discussed in this article, see Asmussen [1]. Some additional standard monographs in the area are Bühlmann [2], Gerber [3], and Grandell [4].

#### References

- [1] Asmussen, S. (2000). *Ruin Probabilities*, World Scientific, Singapore.
- Bühlmann, H. (1976). Mathematical Methods in Risk [2] Theory, Springer-Verlag.
- Gerber, H.U. (1979). An Introduction to Mathematical [3] Risk Theory, SS. Huebner Foundation Monographs, University of Pennsylvania.
- [4] Grandell, J. (1990). Aspects of Risk Theory, Chapman & Hall.

## **Related Articles**

Gerber-Shiu Function; Heavy Tails in Insurance; Lévy Processes; Solvency.

Søren Asmussen
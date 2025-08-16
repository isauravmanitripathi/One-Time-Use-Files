# **Convex Risk Measures**

Quantifying the risk of the uncertainty in the future value of a portfolio is one of the key tasks of risk management. This quantification is usually achieved by modeling the uncertain payoff as a random variable, to which then a certain functional is applied. Such functionals are usually called *risk measures*. The corresponding industry standard, Value at Risk, is often criticized for encouraging the accumulation of shortfall risk in particular scenarios. This deficiency has lead to a search for more appropriate alternatives. The first step of this search consists in specifying certain desirable axioms for risk measures. In the second step, one then tries to characterize those risk measures that satisfy these axioms and to identify suitable examples. In the section Monetary, Convex, and Coherent Risk Measures, we first provide the various axiom sets for *monetary, convex,* and *coherent* risk measures. In the section Acceptance Sets, the representation of monetary risk measures in terms of their *acceptance sets* is briefly discussed. The general *dual representation* for convex and coherent risk measures is given in the section Dual Representation. Various examples are provided in the section Examples and Applications. In many situations, it is reasonable to assume that a risk measure depends on the randomness of the portfolio value only through its probability law. Such risk measures are usually called *law invariant*. They are discussed in the section Law-invariant Risk Measures. Finally, section Conditional Convex Risk Measures and Time Consistency analyzes various notions of *dynamic consistency* that naturally arise in a multiperiod setting.

# **Monetary, Convex, and Coherent Risk Measures**

The uncertainty in the future value of a portfolio is usually described by a function *X* : → , where is a fixed set of scenarios. For instance, *X* can be the (discounted) value of the portfolio or the sum of its P&L and some economic capital. The goal is to determine a number *ρ(X)* that quantifies the risk and can serve as a capital requirement, that is, as the minimal amount of capital that, if added to the position and invested in a risk-free manner, makes the position acceptable. The following axiomatic approach to such risk measures was initiated in the coherent case by [1] and later extended to the class of convex risk measures in [26, 30, 33]. In the sequel, X denotes a given linear space of functions *X* : → containing the constants.

**Definition 1** *A mapping ρ* : X → ∪ {+∞} *is called a monetary risk measure if ρ(*0*) is finite and if ρ satisfies the following conditions for all X, Y* ∈ X*.*

- *Monotonicity*: *if X* ≤ *Y , then ρ(X)* ≥ *ρ(Y ).*
- *Cash invariance*: *if m* ∈ *, then ρ(X* + *m)* = *ρ(X)* − *m.*

The financial meaning of monotonicity is clear: the downside risk of a position is reduced if the payoff profile is increased. Cash invariance is also called *translation property*; in the normalized case *ρ(*0*)* = 0 and *ρ(*1*)* = −1, it is equivalent to *cash additivity*, that is, *ρ(X* + *m)* = *ρ(X)* + *ρ(m)*. This is motivated by the interpretation of *ρ(X)* as a capital requirement, that is, *ρ(X)* is the amount that should be raised in order to make *X* acceptable from the point of view of a supervising agency. Thus, if the risk-free amount *m* is appropriately added to the position or to the economic capital, then the capital requirement is reduced by the same amount. Note that we work with discounted quantities (cf. [22] for a discussion of forward risk measures and interest rate ambiguity).

**Definition 2** *A monetary risk measure ρ is called a convex risk measure if it satisfies the following*:

• *Convexity*: *ρ(λX* + *(*1 − *λ)Y )* ≤ *λρ(X)* + *(*1 − *λ)ρ(Y ), for* 0 ≤ *λ* ≤ 1*.*

Consider the collection of possible future outcomes that can be generated with the resources available to an investor: one investment strategy leads to *X*, while a second strategy leads to *Y* . If one *diversifies*, spending only the fraction *λ* of the resources on the first possibility and using the remaining part for the second alternative, one obtains *λX* + *(*1 − *λ)Y* . Thus, the axiom of convexity gives a precise meaning to the idea that diversification should not increase the risk. This idea becomes even clearer when we note that, for a monetary risk measure, convexity is in fact equivalent to the weaker requirement of

#### 2 **Convex Risk Measures**

 $\rho(\lambda X + (1 - \lambda)Y) \leq$ . Quasi *convexity*:  $\max (\rho(X), \rho(Y)), \text{ for } 0 \le \lambda \le 1.$ 

**Definition 3** A convex measure of risk  $\rho$  is called a *coherent risk measure if it satisfies the following:* 

Positive homogeneity: if  $\lambda > 0$ , then  $\rho(\lambda X) =$  $\lambda \rho(X)$ .

Under the assumption of positive homogeneity, the convexity of a monetary risk measure is equivalent to the following:

Subadditivity:  $\rho(X + Y) \leq \rho(X) + \rho(Y)$ . .

This property allows to decentralize the task of managing the risk arising from a collection of different positions: if separate risk limits are given to different "desks", then the risk of the aggregate position is bounded by the sum of the individual risk limits.

*Value at Risk* at level  $\alpha \in ]0, 1[$ , defined for random variables X on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  by

$$V@R_{\alpha}(X) = \inf\{m \in \mathbb{R} \mid \mathbb{P}[X + m < 0] \le \alpha\} \tag{1}$$

is a monetary risk measure that is positively homogeneous but not subadditive and hence not convex (see Value-at-Risk). Average Value at Risk at level λ ∈]0, 1],

$$AV@R_{\lambda} = \frac{1}{\lambda} \int_{0}^{\lambda} V@R_{\alpha}(X) d\alpha \qquad (2)$$

also called *Conditional Value at Risk*, expected shortfall, or Tail Value at Risk (see Expected Shortfall), is a coherent risk measure. Other examples are discussed in Section "Examples and Applications".

It is sometimes convenient to reverse signs and to emphasize on the *utility* of a position rather than on its risk. Thus, if  $\rho$  is a convex risk measure, then  $\phi(X) := -\rho(X)$  is called a *concave monetary utility functional.* If  $\rho$  is coherent, then  $\phi$  is called a *coherent monetary utility functional.* 

#### **Acceptance Sets**

A monetary measure of risk  $\rho$  induces the set

$$\mathcal{A}_{\rho} := \{ X \in \mathcal{X} \mid \rho(X) \le 0 \} \tag{3}$$

of positions that are acceptable in the sense that they do not require additional capital. The set  $\mathcal{A}_{\rho}$  is called

the *acceptance set* of  $\rho$ . One can show that  $\rho$  is a convex risk measure if and only if  $\mathcal{A}_{\rho}$  is a convex set and that  $\rho$  is positively homogeneous if and only if  $\mathcal{A}_{\rho}$  is a cone. In particular,  $\rho$  is coherent if and only if  $\mathcal{A}_{\rho}$  is a convex cone. The acceptance set completely determines  $\rho$ , because

$$\rho(X) = \inf\{m \in \mathbb{R} \mid m + X \in \mathcal{A}_{\rho}\}\tag{4}$$

Moreover,  $\mathcal{A} := \mathcal{A}_{\rho}$  satisfies the following properties.

$$\mathcal{A} \cap \mathbb{R} \neq \emptyset \tag{5}$$

 $\inf\{m \in \mathbb{R} \mid X + m \in \mathcal{A}\} > -\infty \text{ for all } X \in \mathcal{X} \tag{6}$ 

$$X \in \mathcal{A}, \ Y \in \mathcal{X}, \ Y \ge X \quad \Longrightarrow \quad Y \in \mathcal{A} \tag{7}$$

Conversely, one can take a given class  $\mathcal{A} \subset \mathcal{X}$  of acceptable positions as the primary object. For a position  $X \in \mathcal{X}$ , we can then define

$$\rho_{\mathcal{A}}(X) := \inf\{m \in \mathbb{R} \mid m + X \in \mathcal{A}\}\tag{8}$$

If A satisfies the properties (5)–(7), then  $\rho_A$  is a monetary risk measure. If A is convex, then so is  $\rho_A$ . If  $\mathcal{A}$  is a cone, then  $\rho_{\mathcal{A}}$  is positively homogeneous. Note that, with this notation, equation (4) takes the form  $\rho_{A_{\rho}} = \rho$ . The validity of the analogous identity  $\mathcal{A}_{\rho_A} = \mathcal{A}$  requires that  $\mathcal{A}$  satisfies a certain closure property.

#### **Dual Representation**

Suppose now that  $\mathcal{X}$  consists of measurable functions on  $(\Omega, \mathcal{F})$ . A dual representation of a convex risk measure  $\rho$  has the form

$$\rho(X) = \sup_{Q \in \mathcal{M}} \left( E_Q[-X] - \alpha(Q) \right) \tag{9}$$

Here,  $\mathcal{M}$  is a set of probability measures on  $(\Omega, \mathcal{F})$ such that  $E_Q[X]$  is well defined for all  $Q \in \mathcal{M}$  and  $X \in \mathcal{X}$ . The functional  $\alpha : \mathcal{M} \to \mathbb{R} \cup \{+\infty\}$  is called penalty function.

The elements of  $\mathcal{M}$  can be interpreted as possible probabilistic models, which are taken more or less seriously according to the size of the penalty  $\alpha(Q)$ . Thus, the value  $\rho(X)$  is computed as the worstcase expectation taken over all models  $Q \in \mathcal{M}$  and penalized by  $\alpha(Q)$  (see [8, 28, 42]).

In the dual representation theory of convex risk measures, one aims at deriving a representation  $(9)$  in a systematic manner. The general idea is to apply convex duality. For every  $O \in \mathcal{M}$ , we define the minimal penalty function of  $\rho$  by

$$\alpha_{\rho}(Q) := \sup_{X \in \mathcal{X}} \left( E_{\mathcal{Q}}[-X] - \rho(X) \right) = \sup_{X \in \mathcal{A}_{\rho}} E_{\mathcal{Q}}[-X]$$
(10)

With additional assumptions on the structure of  $\mathcal{X}$  and on continuity properties of  $\rho$ , it is often possible to derive the representation

$$\rho(X) = \sup_{Q \in \mathcal{M}} \left( E_Q[-X] - \alpha_\rho(Q) \right) \tag{11}$$

*via* Fenchel-Legendre duality. In this case,  $\rho$  is coherent if and only if  $\alpha_{\rho}$  takes only the values 0 and  $+\infty$ , and so

$$\rho(X) = \sup_{Q \in \mathcal{Q}_{\rho}} E_Q[-X] \tag{12}$$

where  $\mathcal{Q}_{\rho}$  consists of all  $Q \in \mathcal{M}$  with  $\alpha_{\rho}(Q) = 0$ . We now discuss some situations in which representation (11) can be obtained. In general, however, it may be necessary to consider extended sets  $\mathcal{M}$  that also contain, for example, finitely additive set functions. Dual representation theory goes back to [1, 18, 26, 30, 32-34].

First, let  $\mathcal{X}$  be the space of all bounded measurable functions on  $(\Omega, \mathcal{F})$ . Then, every convex risk measure  $\rho$  takes only finite values and is Lipschitz continuous with respect to the supremum norm. For  $\mathcal{M}$ , we can take the set of all probability measures on  $(\Omega, \mathcal{F})$ . The validity of the dual representation (9) implies that  $\rho$  is *continuous from above* in the sense that

$$X_n \searrow X \quad \Longrightarrow \quad \rho(X_n) \nearrow \rho(X) \tag{13}$$

On the other hand, the condition of continuity from below,

$$X_n \nearrow X \quad \Longrightarrow \quad \rho(X_n) \searrow \rho(X) \tag{14}$$

is equivalent to the validity of the *strong representa*tion

$$\rho(X) = \max_{Q \in \mathcal{M}} \left( E_Q[-X] - \alpha_\rho(Q) \right) \tag{15}$$

in which for every  $X \in \mathcal{X}$  the maximum is attained by some  $Q \in \mathcal{M}$ . In particular, continuity from below is stronger than the continuity from above. Continuity

from above is equivalent to the so-called Fatou property,

$$\liminf_{n \uparrow \infty} \rho(X_n) \ge \rho(X) \text{ for any bounded sequence}$$
  
(*X<sub>n</sub>*) converging pointwise to *X* (16)

Continuity from below is equivalent to the stronger Lebesgue property,

$$\lim_{n \uparrow \infty} \rho(X_n) = \rho(X) \text{ for any bounded sequence}$$
  
(X<sub>n</sub>) converging pointwise to X (17)

Next, we fix a reference probability measure  $\mathbb{P}$  on  $(\Omega, \mathcal{F})$  and consider the case in which  $\mathcal{X} = L^p := L^p(\Omega, \mathcal{F}, \mathbb{P})$  for some  $p \in [1, \infty]$ . This choice implicitly requires that  $\rho(X) = \rho(\widetilde{X})$  whenever  $X = \widetilde{X}$   $\mathbb{P}$ -almost surely. For  $\mathcal{M}$ , we take the set of all probability measures that are absolutely continuous with respect to  $\mathbb{P}$  and whose density belongs to  $L^q$ , where  $q = p/(p-1)$  is the dual exponent.

The space  $\mathcal{X} = L^{\infty}$  can be regarded as a subset of the space of all bounded measurable functions, and so all corresponding results carry over. In addition, continuity from above (or, equivalently, the Fatou property) of  $\rho$  is now even equivalent to a dual representation (11) in terms of probability measures.

For a convex risk measure  $\rho$  on  $\mathcal{X} = L^p$  with  $1 \le p < \infty$ , the existence of a dual representation (11) is equivalent to the lower semicontinuity of  $\rho$ with respect to the standard  $L^p$ -norm. If  $\rho$  takes only finite values, then it is even Lipschitz continuous and admits a strong representation  $(15)$ . Here, we assume for simplicity that  $(\Omega, \mathcal{F}, \mathbb{P})$  is atomless and  $L^2$  is separable.

For the discussion of the dual representation of convex risk measures on spaces of bounded measurable functions, we refer to [28, 37, 38]. For  $L^p$  spaces, see [23, 36] and the references therein. Representation theory on Orlicz spaces is considered in [9].

## **Examples and Applications**

In this section, we take  $\mathcal{X} = L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$ . The class of convex risk measures comprises many of the common valuation methods in finance and economics. The risk-neutral expectation in a nice arbitrage-free market model, for instance, clearly corresponds to a coherent risk measure. If the market model is incomplete, then the cost of superhedging a position  $X \in \mathcal{X}$ is given by the coherent risk measure

$$\sup_{Q \in \mathcal{P}} E_Q[-X] \tag{18}$$

where  $\mathcal{P}$  is the set of equivalent local martingale measures (see **Superhedging**). If one imposes additional convex trading constraints, the cost of superhedging is a convex risk measure whose representation  $(9)$  is explicitly known (see [24, 26, 28]).

Let us now consider the case in which valuation of positions  $X \in \mathcal{X}$  is based on the expected utility  $\mathbb{E}[u(X)]$  for a concave and strictly increasing function  $u : \mathbb{R} \to \mathbb{R}$ . Then, a position can be called *acceptable* if  $E_{O}[u(X)]$  is bounded from below by  $u(c)$  for a given threshold c. The set

$$\mathcal{A} := \{ X \in \mathcal{X} \mid E_{\mathcal{Q}}[u(X)] \ge u(c) \} \tag{19}$$

is a valid and convex acceptance set. Hence,  $\rho_A$ , defined by equation (8), is a convex risk measure called utility-based shortfall risk measure. It is continuous from below and admits the strong representation  $(15)$  with minimal penalty function

$$\alpha_{\rho}(Q) = \inf_{\lambda > 0} \frac{1}{\lambda} \left( \mathbb{E} \left[ \widetilde{u} \left( \lambda \frac{\mathrm{d}Q}{\mathrm{d}\mathbb{P}} \right) \right] - u(c) \right) \quad (20)$$

where  $\widetilde{u}(y) = \sup_{x} (u(x) - xy)$  denotes the convex conjugate function of  $u$  (see [26] or [28]). In the exponential utility case with  $u(x) = -e^{-\theta x}$  for some  $\theta > 0$ , we obtain for  $c = 0$  the *entropic risk measure*,

$$\rho^{\text{ent}}(X) = \frac{1}{\theta} \log \mathbb{E}\left[e^{-\theta X}\right] \tag{21}$$

Its minimal penalty function is given by  $\alpha_{\rho}(Q) =$  $\theta^{-1}H(Q|\mathbb{P})$ , where

$$H(Q|\mathbb{P}) = \mathbb{E}\left[\begin{array}{c} \mathrm{d}Q\\ \mathrm{d}\mathbb{P} \end{array}\log \begin{array}{c} \mathrm{d}Q\\ \mathrm{d}\mathbb{P} \end{array}\right] \tag{22}$$

is the relative entropy of  $Q \ll \mathbb{P}$  (see [28]). For the role of entropic risk measures in problems of risk transfer, (see [3]).

To introduce another closely related class of concave monetary utility functionals, let  $g: [0, \infty[ \rightarrow$  $\mathbb{R} \cup \{+\infty\}$  be a lower semicontinuous convex function satisfying  $g(1) < \infty$  and the superlinear growth condition  $g(x)/x \to +\infty$  as  $x \uparrow \infty$ . Associated to it is the *g*-divergence

$$I_g(Q|\mathbb{P}) := \mathbb{E}\left[g\left(\frac{\mathrm{d}Q}{\mathrm{d}\mathbb{P}}\right)\right], \qquad Q \ll \mathbb{P}$$
(23)

as introduced in [14, 15]. The *g*-divergence  $I_g(Q|\mathbb{P})$ can be interpreted as a statistical distance between the hypothetical model  $Q$  and the reference measure  $\mathbb{P}$ , so that  $\gamma_{\mathfrak{g}}(Q) := I_{\mathfrak{g}}(Q|\mathbb{P})$  is a natural choice for a penalty function. The risk measure

$$\rho_g(X) := \sup_{Q \ll \mathbb{P}} \left( E_Q[-X] - I_g(Q|\mathbb{P}) \right) \tag{24}$$

corresponding to such a divergence penalty, is continuous from below, and  $I_{\sigma}(\cdot|\mathbb{P})$  is its minimal penalty function. The corresponding concave utility functional,  $\phi_g = -\rho_g$ , was called *optimized certainty* equivalent in [5]. This name stems from the variational identity

$$\phi_g(X) = \sup_{z \in \mathbb{R}} \left( \mathbb{E}[u(X-z)] + z \right), \qquad X \in L^{\infty}$$
(25)

where  $u(x) = \inf_{z>0} (xz + g(z))$  is the concave conjugate function of  $g$  (see [4, 47]). In [13], the name divergence utility is used. Note that the particular choice  $g(x) = x \log x$  corresponds to the relative entropy,  $I_g(Q|\mathbb{P}) = H(Q|\mathbb{P})$ , and so  $\rho_g$  coincides with the entropic risk measure. Another important example is provided by taking  $g(x) = 0$  for  $x \le \lambda^{-1}$ and  $g(x) = \infty$  otherwise, so that the corresponding coherent risk measure is given by Average Value at Risk at level  $\lambda$ :

$$AV@R_{\lambda}(X) = \inf_{Q \in \mathcal{Q}_{\lambda}} E_{Q}[X] \quad \text{for}$$
$$\mathcal{Q}_{\lambda} := \left\{ Q \ll \mathbb{P} \, \big| \, \frac{\mathrm{d}Q}{\mathrm{d}\mathbb{P}} \leq \frac{1}{\lambda} \right\} \quad (26)$$

see Definition (1) and **Expected Shortfall**. In this case, we have  $u(x) = 0 \land x/\lambda$  and hence get the classical duality formula

1

$$AV@R_{\lambda}(X) = \frac{1}{\lambda} \inf_{z \in \mathbb{R}} \left( \mathbb{E}[\left(z - X\right)^{+}] - \lambda z \right) \quad (27)$$

as a special case of equation (25). The mixtures of Average Value at Risk at various levels  $\lambda$  are called spectral risk measures. They are again coherent risk measures and discussed in more detail in Spectral Measures of Risk

Many of these risk measures can be extended in a straightforward manner to spaces of unbounded random variables (see [23] for a systematic study of such extensions). For Gaussian random variables  $X$ , Value at Risk, Average Value at Risk, and the spectral risk measures all take the form

$$\rho(X) = \mathbb{E} \big[ -X \big] + c \cdot \sigma(X) \tag{28}$$

with different constants  $c$ ; for the entropic risk measure, the standard deviation  $\sigma(X)$  is replaced by the variance  $\sigma^2(X)$ .

Model uncertainty is another situation in which it is natural to consider risk measures, due to the interpretation of the measures  $Q$  in the dual representation (9) as suitably penalized probabilistic models. This idea already appears in robust statistics [34]. More recently, coherent and convex risk measures were applied in obtaining numerical representations of investors who are averse against both risk and model uncertainty [27, 29, 32, 43] or to define measures of model uncertainty [16].

In a financial market model, it makes sense to combine risk measurement with dynamic or static hedges. For instance, measuring the residual risk of a position after hedging by a convex risk measure  $\rho$  is equivalent to using the convex risk measure that arises as the *inf-convolution* of  $\rho$  and the superhedging risk measure, defined at the beginning of this section (cf. [3, 26, 28, 46] and the references therein).

#### Law-invariant Risk Measures

Here, we discuss those convex risk measures  $\rho$  on  $\mathcal{X} = L^{\infty}(\Omega, \mathcal{F}, \mathbb{P})$  that satisfy  $\rho(X) = \rho(\widetilde{X})$  for random variables  $X, \widetilde{X} \in \mathcal{X}$  that have the same law under  $\mathbb{P}$ . These risk measures are usually called law invariant. Examples from the preceding section are Average Value at Risk, the spectral risk measures, the utility-based shortfall risk measures, and the optimized certainty equivalents. Under mild conditions on the underlying probability space, every

law-invariant convex risk measure  $\rho$  can be represented in the form

$$\rho(X) = \sup_{\mu} \left( \int_{(0,1]} AV \circledast R_{\lambda}(X) \,\mu(\,\mathrm{d}\lambda) - \beta(\mu) \right) \tag{29}$$

where the supremum is taken over all Borel probability measures  $\mu$  on [0,1] and  $\beta(\mu)$  is a penalty for  $\mu$ . Under the additional assumption of continuity from above, this representation was obtained in the coherent case by [41] and later extended by [17, 28, 31, 39]. More recently, it was shown in [35] that the condition of continuity from above can actually be dropped.

# **Conditional Convex Risk Measures and Time Consistency**

A risk measure should take into account the available information, and it should do so in a consistent manner as new information comes in. Here, we limit the discussion to discrete time and fix a filtration  $(\mathcal{F}_t)_{t=0,1,\dots}$  on  $(\Omega, \mathcal{F}, \mathbb{P})$ ; for continuous time and the connection to backward stochastic differential equations (BSDEs), (see  $[10, 20]$ ) and the references therein. A *conditional convex risk measure* at time  $t$ is now defined as a map

$$\rho_t: L^{\infty} \to L^{\infty}_t := L^{\infty}(\Omega, \mathcal{F}_t, \mathbb{P}) \qquad (30)$$

which satisfies the obvious conditional versions of monotonicity, cash invariance, and convexity where the constants  $m$  and  $\lambda$  are replaced by functions in  $L^{\infty}_{t}$ . The associated *acceptance set* 

$$\mathcal{A}_t := \{ X \in L^\infty \mid \rho_t(X) \le 0 \} \tag{31}$$

is conditionally convex (i.e.,  $\alpha X + (1 - \alpha)Y \in \mathcal{A}_t$ for  $X, Y \in \mathcal{A}_t$  and  $\mathcal{F}_{t-1}$ -measurable  $\alpha$  with  $0 \leq \alpha \leq$ 1) and it determines  $\rho_t$  via

$$\rho_t(X) = \text{ess inf}\left\{Y \in L_t^{\infty} \mid X + Y \in \mathcal{A}_t\right\} \tag{32}$$

The Fatou property is now equivalent to a dual *representation* of the form

$$\rho_t(X) = \operatorname*{ess\,sup}_{Q \in \mathcal{M}} \left( E_Q[-X \,|\, \mathcal{F}_t \,] - \alpha_t(Q) \right) \tag{33}$$

where the conditional penalty function  $\alpha_t$  is given by

$$\alpha_t(Q) = \underset{X \in \mathcal{A}_t}{\text{ess sup}} E_Q[-X \mid \mathcal{F}_t] \tag{34}$$

The inequality  $\geq$  immediately follows from the definition of  $\alpha_t$ , and the converse inequality is obtained by using the dual representation of the unconditional convex risk measure  $\rho(X) := \mathbb{E}[\rho_t(X)]$  (cf. [6, 11, 21, 25, 45]).

For the conditional entropic risk measure,

$$\rho_t^{\text{ent}}(X) = \frac{1}{\theta} \log \mathbb{E}\left[e^{-\theta X} \mid \mathcal{F}_t\right] \tag{35}$$

the dual representation holds with

$$\alpha_t(Q) = \frac{1}{\theta} \widehat{H}_t(Q|P) \tag{36}$$

where

$$\widehat{H}_{t}(Q|P) := \mathbb{E}\left[\left.\frac{Z}{Z_{t}}\log\left.\frac{Z}{Z_{t}}\right|\mathcal{F}_{t}\right]I_{\{Z_{t}>0\}}\right]$$
(37)

denotes the *conditional entropy* of  $Q \in \mathcal{M}$  with respect to P, defined in terms of the densities  $Z =$  $dQ/dP$  and  $Z_t = dQ/dP|_{\mathcal{F}_t}$ .

In our dynamic setting, the key question is how the conditional risk assessments of a financial position at different times are connected to each other.

**Definition** A dynamic risk measure given by a seq*uence of conditional convex risk measures*  $(\rho_t)_{t=0,1,...}$ is called time-consistent if

$$\rho_{t+1}(X) \le \rho_{t+1}(Y) \quad \Longrightarrow \quad \rho_t(X) \le \rho_t(Y) \tag{38}$$

and this is equivalent to recursiveness:

$$\rho_t = \rho_t(-\rho_{t+1}) \quad \text{for } t = 0, 1, \dots\n$$
(39)

To characterize time consistency in terms of acceptance sets and penalty functions, we define the "myopic" acceptance sets

$$\mathcal{A}_{t,t+1} := \left\{ X \in L_{t+1}^{\infty} \; \middle| \; \rho_t(X) \le 0 \right\} \tag{40}$$

and the corresponding "myopic" penalty functions

$$\alpha_{t,t+1}(Q) := \underset{X \in \mathcal{A}_{t,t+1}}{\text{ess sup}} E_Q[-X \mid \mathcal{F}_t] \qquad (41)$$

We also assume that the class  $Q^*$  of all equivalent probability measures Q with  $\alpha_0(Q) < \infty$  is not empty. Then time consistency is equivalent to each of the following conditions:

- $A_t = A_{t,t+1} + A_{t+1}$  for  $t = 0, 1, ...$
- For any  $O \in \mathcal{M}$ ,

$$\alpha_t(Q) = \alpha_{t,t+1}(Q) + E_Q[\alpha_{t+1} | \mathcal{F}_t] \quad \text{for}$$
  
$$t = 0, 1, \dots \tag{42}$$

For any  $Q \in \mathcal{Q}^*$  and any  $X \in L^{\infty}$ , the process 0.1

$$\rho_t(X) + \alpha_t(Q), \quad t = 0, 1, \dots$$
 (43)

is a  $Q$ -supermartingale

(cf. [2, 7, 11, 12, 19, 25]). Moreover, each condition implies that the dynamic risk measure admits a robust representation in terms of the set  $Q^*$ , that is,

$$\rho_t(X) = \operatorname*{ess\,sup}_{Q \in \mathcal{Q}^*} \left( E_Q[-X \mid \mathcal{F}_t] - \alpha_t(Q) \right) \tag{44}$$

for all  $X \in L^{\infty}$  and all  $t > 0$  (cf. [25]).

The entropic dynamic risk measure is time consistent as long as the parameter  $\theta$  remains constant. On the other hand, time consistency fails for the dynamic risk measure defined by conditional Average Value at Risk. Under the assumption of law invariance, the entropic case is in fact the only time-consistent example, if we include the limiting cases  $\theta = 0$  and  $\theta = \infty$ corresponding to the conditional expected loss under  $\mathbb{P}$  and the *conditional worst-case risk measure*,

$$\rho_t(X) = \operatorname{ess\,inf} \left\{ Y \in L_t^{\infty} \mid Y \ge -X \right\} \tag{45}$$

respectively (cf. [40]). This suggests to consider weaker versions of time consistency. For example, the supermartingale property above implies that for each  $Q \in \mathcal{Q}^*$  the process  $\alpha_t(Q), t = 0, 1, \ldots$ , is a Qsupermartingale, and this is equivalent to the weaker requirement

$$\rho_{t+1}(X) \le 0 \quad \Longrightarrow \quad \rho_t(X) \le 0 \qquad (46)$$

that is,  $\mathcal{A}_t \subseteq \mathcal{A}_{t+1}$  for all  $t = 0, 1, \ldots$  In the law invariant case, such weaker notions of consistency may be used for a characterization of utility-based shortfall risk (cf. [48]). The notion of *prudence* introduced in  $[44]$  requires

$$X \in \mathcal{A}_t \quad \Longrightarrow \quad -\rho_{t+s}(X) \in \mathcal{A}_t \text{ for all } s \ge 0 \tag{47}$$

and this is characterized by the fact that

$$\rho_t(X) - \sum_{k=0}^{t-1} \alpha_k(Q), \quad t = 0, 1, \dots \qquad (48)$$

is a *<sup>Q</sup>*-supermartingale for any *<sup>Q</sup>* <sup>∈</sup> <sup>Q</sup><sup>∗</sup> and any *X* ∈ *L*<sup>∞</sup>.

For an infinite time horizon, the supermartingale criteria for time consistency and for prudence both yield almost sure convergence of the capital requirements *ρt(X)* to an asymptotic capital requirement *ρ*∞*(X)*. We may now ask whether the sequence is *asymptotically safe* in the sense that *ρ*∞*(X)* ≥ −*X,* or even *asymptotically precise* in the sense of *ρ*∞*(X)* = −*X*; note that asymptotic precision can be viewed as a nonlinear analog of martingale convergence. Criteria in terms of acceptance sets and penalty functions are derived in [25] for the time-consistent case and in [44] for the case of prudence.

## **References**

- [1] Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D. (1999). Coherent measures of risk, *Mathematical Finance* **9**(3), 203–228.
- [2] Artzner, P., Delbaen, F., Eber, J.-M., Heath, D. & Ku, H. (2007). Coherent multiperiod risk adjusted values and Bellman's principle, *Annals of Operational Research* **152**, 5–22.
- [3] Barrieu, P. & El Karoui, N. (2005). Inf-convolution of risk measures and optimal risk transfer, *Finance and Stochastics* **9**(2), 269–298.
- [4] Ben-Tal, A. & Teboulle, M. (1987). Penalty functions and duality in stochastic programming via *φ*-divergence functionals, *Mathematical Operational Research* **12**, 224–240.
- [5] Ben-Tal, A. & Teboulle, M. (2007). An old-new concept of convex risk measures: the optimized certainty equivalent, *Mathematical Finance* **17**(3), 449–476.
- [6] Bion-Nadal, J. (2004). *Conditional Risk Measure and Robust Representation of Convex Conditional Risk Measures*, CMAP preprint 557, Ecole Polytechnique Palaiseau.
- [7] Bion-Nadal, J. (2006). *Dynamic Risk Measuring: Discrete Time in a Context of Uncertainty, and Continuous Time on a Probability Space*, CMAP preprint 596, Ecole Polytechnique Palaiseau.
- [8] Carr, P., Geman, H. & Madan, D. (2001). Pricing and hedging in incomplete markets, *Journal of Financial Economics* **62**, 131–167.
- [9] Cheridito, P. & Li, T. Risk measures on Orlicz hearts, *Mathematical Finance*, to appear.
- [10] Cheridito, P., Delbaen, F. & Kupper, M. (2005). Coherent and convex monetary risk measures for

unbounded cadl ` ag processes, ` *Finance and Stochastics* **9**, 1713–1732.

- [11] Cheridito, P. Delbaen, F. & Kupper, M. (2006). Dynamic monetary risk measures for bounded discrete-time processes, *Electronic Journal of Probability* **11**, 57–106.
- [12] Cheridito, P. & Kupper, M. (2006). *Composition of Time-Consistent Dynamic Monetary Risk Measures in Discrete Time*, Preprint.
- [13] Cherny, A. & Kupper, M. (2007). *Divergence Utilities*, Preprint, Moscow State University.
- [14] Csiszar, I. (1963). Eine informationstheoretische Ungleichung und ihre Anwendung auf den Beweis der Ergodizitat von Markoffschen Ketten, ¨ *Magyar Tudomanyos Akademia Mathematica Kutat´o International K¨ozl* **8**, 85–108.
- [15] Csiszar, I. (1967). On topological properties of *f* divergences, *Studia Scientiarum Mathematicarum Hungarica* **2**, 329–339.
- [16] Cont, R. (2006). Model uncertainty and its impact on the pricing of derivative instruments, *Mathematical Finance* **16**, 519–542.
- [17] Dana, R.-A. (2005). A representation result for concave Schur concave functions, *Mathematical Finance* **15**, 613–634.
- [18] Delbaen, F. (2002). Coherent measures of risk on general probability spaces, *Advances in Finance and Stochastics. Essays in Honour of Dieter Sondermann*, Springer-Verlag, pp. 1–37.
- [19] Delbaen, F. (2006). The structure of m-stable sets and in particular of the set of risk neutral measures, in *Memoriam Paul-Andr´e Meyer – S´eminaire de Probabilit´es XXXIX*, M. Yor & M. Emery, eds, Springer, Berlin, pp. ´ 215–258.
- [20] Delbaen, F., Peng, S. & Rosazza Gianin, E. (2008). *Representation of the Penalty Term of Dynamic Concave Utilities*, arXiv:0802.1121.
- [21] Detlefsen, K. & Scandolo, G. (2005). Conditional and dynamic convex risk measures, *Finance and Stochastics* **9**(4), 539–561.
- [22] El Karoui, N. & Ravanelli, C. (2008). Cash sub-additive risk measures and interest rate ambiguity, *Mathematical Finance*, to appear.
- [23] Filipovic, D. & Svindland, G. (2008). ´ *Convex Risk Measures Beyond Bounded Risks, or The Canonical Model Space for Law-Invariant Convex Risk Measures is \$L 1\$*, Preprint, University of Vienna.
- [24] Follmer, H. & Kramkov, D. (1997). Optional decompo- ¨ sitions under constraints, *Probability Theory and Related Fields* **109**, 1–25.
- [25] Follmer, H. & Penner, I. (2006). Convex risk measures ¨ and the dynamics of their penalty functions, *Statistics and Decisions* **24**(1), 61–96.
- [26] Follmer, H. & Schied, A. (2002). Convex measures of ¨ risk and trading constraints, *Finance and Stochastics* **6**, 429–447.
- [27] Follmer, H. & Schied, A. (2002). Robust preferences ¨ and convex measures of risk, in *Advances in Finance and Stochastics*, Springer, Berlin, pp. 39–56.

- [28] Follmer, H. & Schied, A. (2004). ¨ *Stochastic Finance: An Introduction in Discrete Time*, 2nd revised and extended edition, *de Gruyter Studies in Mathematics 27* Walter de Gruyter, Berlin.
- [29] Follmer, H., Schied, A., Weber, S. (2007). Robust ¨ preferences and robust portfolio choice, in *Handbook on Mathematical Finance*, A. Bensoussan, ed, Elsevier, Amsterdam, forthcoming.
- [30] Frittelli, M. & Rosazza Gianin, E. (2002). Putting order in risk measures, *Journal of Banking and Finance* **26**, 1473–1486.
- [31] Frittelli, M. & Rosazza Gianin, E. (2005). Law-invariant convex risk measures, *Advances in Mathematical Economics* **7**, 33–46.
- [32] Gilboa, I. & Schmeidler, D. (1989). Maxmin expected utility with non-unique prior, *Journal of Mathematical Economics* **18**, 141–153.
- [33] Heath, D. (2000). *Back to the Future*, Plenary Lecture, First World Congress of the Bachelier Finance Society, Paris.
- [34] Huber, P. (1981). Robust statistics, *Wiley Series in Probability and Mathematical Statistics*, Wiley, New York.
- [35] Jouini, E., Schachermayer, W. & Touzi, N. (2006). Law invariant risk measures have the Fatou property, *Advances in Mathematical Economics* **9**, 49–71.
- [36] Kaina, M. & Ruschendorf, L. On convex risk measures ¨ on Lp-spaces, *Mathematical Methods in Operations Research*, to appear.
- [37] Kratschmer, V. (2005). Robust representation of convex ¨ risk measures by probability measures, *Finance and Stochastics* **9**, 597–608.
- [38] Kratschmer, V. (2007). ¨ *On Sigma-Additive Robust Representation of Convex Risk Measures for Unbounded Financial Positions in the Presence of Uncertainty About the Market Model*, Preprint, TU, Berlin.
- [39] Kunze, M. (2003). *Verteilungsinvariante konvexe Risikomaße*, Diplomarbeit, Humboldt-Universitat zu Berlin. ¨

- [40] Kupper, M. & Schachermayer, W. (2008). *Representation Results for Law Invariant Time Consistent Functions*, Preprint TU, Vienna.
- [41] Kusuoka, S. (2001). On law invariant coherent risk measures, *Advances in Mathematical Economics* **3**, 83–95.
- [42] Larsen, K., Pirvu, T., Shreve, S. & Tut¨ unc ¨ u, R. (2005). ¨ Satisfying Convex Risk Limits by Trading, *Finance and Stochastics* **9**(2), 177–195.
- [43] Maccheroni, F., Marinaci, M. & Rustichini, A. (2006). Ambiguity aversion, robustness, and the variational representation of preferences, *Econometrica* **74**, 1447–1498.
- [44] Penner, I. (2007). *Dynamic Convex Risk Measures: Time Consistency, Prudence, and Sustainability*, Ph.D. Thesis, Humboldt-Universitat zu Berlin, Berlin. ¨
- [45] Riedel, F. (2004). Dynamic coherent risk measures, *Stochastic Processes and their Applications* **112**(2), 185–200.
- [46] Schied, A. (2006). Risk measures and robust optimization problems, *Stochastic Models* **22**, 753–831.
- [47] Schied, A. (2007). Optimal investments for risk- and ambiguity-averse preferences: a duality approach, *Finance and Stochastics* **11**(1), 107–129.
- [48] Weber, S. (2006). Distribution-invariant risk measures, information, and dynamic consistency, *Mathematical Finance* **16**, 419–442.

## **Related Articles**

**Convex Duality**; **Expected Shortfall**; **Expected Utility Maximization: Duality Methods**; **Risk Measures: Statistical Estimation**; **Spectral Measures of Risk**; **Superhedging**; **Utility Function**; **Utility Indifference Valuation**; **Value-at-Risk**.

HANS FOLLMER ¨ & ALEXANDER SCHIED
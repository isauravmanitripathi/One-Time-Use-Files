# **Large Deviations**

Modern large deviations theory, pioneered by Donsker and Varadhan [11], concerns the study of rare events, and it has become a common tool for the analysis of stochastic systems in a variety of scientific disciplines and in engineering. The theory developed by Donsker and Varadhan is a generalization of Laplace's principle and Cramér's theorem. Here we concentrate on applications to finance and risk management.

A wealth of monographs discuss the large deviations theory in detail; see, for instance,  $[8-10]$ . Here, we shall discuss applications to mathematical finance, including option pricing (see Option Pricing: General Principles), risk management (see Risk Exposures; Risk Management: Historical Perspectives), and portfolio optimization (see Risk-Return Analysis; Merton Problem). The reader may also consult [21], which includes details behind many of the topics touched upon here. Before discussing these applications, however, we provide a brief introduction to some basic concepts underlying the theory of large deviations.

**Definition 1** A sequence of random objects  $(Z_n : n \ge 0)$  taking values on some topological space S satisfies a, large deviations principle with rate function  $(J(z): z \in \mathcal{S})$ , if for each Borel measurable set  $A \in \mathcal{S}$ 

$$\begin{split} & \inf_{z \in A^{o}} J\left(z\right) \leq \underline{\lim}_{n \to \infty} - \frac{1}{n} \log P\left(Z_{n} \in A\right) \\ & \leq \overline{\lim}_{n \to \infty} - \frac{1}{n} \log P\left(Z_{n} \in A\right) \leq \inf_{z \in \overline{A}} J\left(z\right) \end{split} \tag{1}$$

and  $J(\cdot)$  is nonnegative and upper semicontinuous. Here  $A^o$  and  $\overline{A}$  stand for the interior and closure of A, respectively.

Throughout this article, we assume that  $S$  is a Polish space (i.e., a separable, completely metrizable topological space). One can show that if a large deviations principle holds, then there exists a deterministic element  $\widetilde{z} \in \mathcal{S}$  such that  $Z_n \Rightarrow \widetilde{z}$  (where  $\Rightarrow$  denotes weak convergence). In many applications,  $S$  is a function space, so  $Z_n$  is a stochastic process and  $\widetilde{z}$  is the asymptotically most likely path.

A large deviations principle is intuitively interpreted as having the formal approximation

$$P\left(Z_n \approx z\right) \approx \exp\left(-nJ\left(z\right)\right) \tag{2}$$

for z outside a neighborhood of  $\tilde{z}$ . The previous approximation does not carry any rigorous meaning. Nevertheless, the formal use of equation (2) often allows to infer large deviations properties of stochastic systems that can be later justified rigorously using large deviations theory. The rigorous meaning behind equation (2) is given by Varadhan's lemma (see [8], p. 137), which states that, in the presence of a large deviations principle, for every continuous function  $(F(z): z \in \mathcal{S})$  bounded from below we have that

$$\log \frac{1}{n} E \exp\left(-nF\left(Z_n\right)\right) \longrightarrow -\inf_{z \in \mathcal{S}} \left(J\left(z\right) + F\left(z\right)\right) \tag{3}$$

as  $n \nearrow \infty$ . Varadhan's lemma is a generalized version of Laplace's principle. Indeed, note that in view of representation (2), Varadhan's lemma makes perfect intuitive sense after applying Laplace's principle since

$$E \exp(-nF(Z_n)) \approx \int \exp(-n(J(z) + F(z))) dz$$
  
$$\approx \exp\left(-n \inf_{z \in S} (J(z) + F(z))\right)$$
  
(4)

The solution to the optimization problem  $\inf_{z \in S} (I(z) + F(z))$  is the so-called minimum energy path or optimal path. Formally, if we put  $F(z) = \infty \times I_{A^c}(z)$ , then  $E \exp(-nF(Y)) =$  $P(Y \in A)$  and if  $\widetilde{z} \notin A$  and regularity assumptions on the set  $A$  hold, Varadhan's lemma yields

$$P\left(Z_n \in A\right) \approx \exp\left(-n \inf_{z \in A} J\left(z\right)\right) \tag{5}$$

A related class of asymptotic approximations arises in the setting of dynamical systems with a small random perturbation, for instance,

$$\begin{aligned} \mathrm{d}Z_{\varepsilon}\left(t\right) &= \mu\left(Z_{\varepsilon}\left(t\right)\right) \,\mathrm{d}t + \varepsilon\sigma\left(Z_{\varepsilon}\left(t\right)\right) \,\mathrm{d}B\left(t\right); \\ Z_{\varepsilon}\left(0\right) &= z_{\varepsilon}\left(0\right) \end{aligned} \tag{6}$$

assuming the necessary regularity conditions for the existence of a solution to the previous stochastic differential equations (SDEs) driven by a standard Brownian motion  $B(\cdot)$ . Note that, formally, if we send  $\varepsilon \to 0$  and assume that  $z_{\varepsilon}(0) \to \widetilde{z}(0)$ , we obtain convergence of  $Z_{\varepsilon}$  to a deterministic dynamical system satisfying  $\widetilde{z}'(t) = \mu(\widetilde{z}(t))$  given  $\widetilde{z}(0)$ . Therefore, under appropriate conditions, one would expect the existence of a theory backing up approximations such as equation  $(2)$  given by an appropriate rate function  $I(\cdot)$ . Such a theory has indeed been developed, and it is known as the Freidlin-Wentzel theory (see, [8], p. 212 or [22], p. 129). The rest of this article concentrates on the application of the ideas of large deviations in finance.

# **Option Pricing**

## Direct Use of Large Deviations Approximations

Large deviations principles are applied in finance to develop approximations for option prices (see **Option Pricing: General Principles**). It is easier to explain the techniques with a simple example. Consider the problem of pricing a digital knock-in call option (see **Barrier Options**) with maturity time  $T$  under a Black-Scholes economy (see Black-Scholes For**mula**), in particular,

$$\alpha_T = P\left(\min_{0 \le s \le T} B(s) \le -a, B(T) > b\right) \qquad (7)$$

for some barrier values  $a, b > 0$ , where  $B(\cdot)$  is a standard Brownian motion. This probability can be, of course, evaluated in closed form  $(17, 18]$ , or see equation 12 below), but we illustrate the use of large deviations theory here. We develop approximations that can be asymptotically validated when the time to maturity and the barriers are large. First, we embed the problem in a large deviations setting by introducing an appropriate scaling

$$\alpha_T = P\left(\min_{0 \le u \le 1} Z_T\left(u\right) \le -c, Z_T\left(1\right) \ge d\right) \quad (8)$$

where  $a = -Tc$  and  $b = Td$ , and  $Z_T(u) = B(uT)/T$ ,  $u \in [0, 1]$ . The rate function of  $Z_T(\cdot)$  is defined on the space  $C_1 := C_1[0, 1]$  of absolutely continuous functions and takes the form

$$J(z) = \frac{1}{2} \int_0^1 \dot{z} (u)^2 du \tag{9}$$

Note that  $Z_T \rightarrow \widetilde{z} = 0$  uniformly in probability. A formal application of equation (2) combined with Laplace's principle then yields

$$\alpha_T \approx \exp\left(-T \inf_{z \in A} J(z) + o(T)\right) \n$$
(10)

where

$$A = \{ z \in C_1 : z(0) = 0, \min_{0 \le u \le 1} z(u) \le -c, z(1) \ge d \}$$
(11)

One can then show directly using standard techniques from calculus of variations (applying Euler-Lagrange's principle) that the optimal path is a piecewise linear function. Note that equation  $(2)$  also suggests that the optimal path is the most likely way in which the particular large deviations event, given by A, can occur. In our simple example one can directly evaluate such an optimal path by using the reflection principle. In particular, note that

$$\alpha_T = P(B(T) > (2a + b)T)$$
  
=  $P(Z_T(1) > 2c + d)$  (12)

which allows to conclude (again by reflection) that

$$z^*(t) = I(t \le t^*) \theta_{-}t + (\theta_{+}t - c) I(1 \le t \le t^*)$$
(13)

where  $\theta_{-} = -(2c + d)$ ,  $\theta_{+} = -\theta_{-}$  and  $t^{*} = c/(2c + d)$ d). Moreover, we have that  $J(z^*) = (2c+d)^2/2$ . It is important to note using equation  $(12)$  and elementary properties of the Gaussian density that

$$\alpha_T = \frac{\exp\left(-T\,J\left(z^*\right)\right)}{\left(2\pi\right)^{1/2}\,T^{1/2}}\tag{14}$$

as  $T \nearrow \infty$ . In particular, it is worth noting that the large deviations results such as equation  $(11)$  provide only rough approximations because no information is given about premultiplying terms like the factor  $T^{-1/2}$ , which appears in equation (14).

### **Enhancing Monte Carlo Simulations**

As indicated above, large deviations approximations typically provide only logarithmic asymptotics (i.e., only the exponential rate of decay is identified without any additional information). Sharp asymptotics (i.e., asymptotics with information about premultiplying factors such as equation 14) can only be developed under an additional problem structure. We continue with our discussion on pricing issues in the context of **barrier options**; the option pricing described in the previous paragraph is just an example of one of many types that are possible. In evaluating barrier options, an important aspect relates to the calculation of exit probabilities. For instance, in [5] such calculations are treated combining both Monte Carlo methods and large deviation principles. The model in use is a geometric Brownian motion under the risk-neutral measure (see Fundamental Theorem of Asset Pricing; Risk-neutral Pricing)

$$dS_t = rS_t dt + \sigma S_t dB_t, \ S_0 = x \tag{15}$$

Using this model, we consider computing the probability that the process  $S$  solving equation (15) does not hit any of two barriers, a lower or an upper barrier, which are suitable, positive, twice continuously differentiable functions  $(l(t), t > 0)$  and  $(u(t), t > 0)$ , respectively.

The approach suggested by Baldi *et al.* [5] consists in using sharp large deviations to reduce bias in **Monte Carlo simulation.** The simulation of  $S$  is done by making an equidistant partition of the time interval  $[0, T]$ , where T indicates the expiration of the contract. Then, the sample path is the collection

$$S_{t_{i+1}} = S_{t_i} \exp\left(\left(r - \frac{\sigma}{2}\right)\epsilon + \sigma(B_{t_{i+1}} - B_{t_i})\right)$$
  
$$i = 0, 1, \dots, m \tag{16}$$

where  $t_0 = 0 < t_1 < \ldots < t_m = T$  and  $t_{i+1} - t_i =$  $\epsilon > 0$ .

Using sharp asymptotics, it is possible to find approximations of the exit probabilities over small intervals, that is, when  $\epsilon$  becomes small. Let  $\zeta \in (l(t_i), u(t_i))$  and  $y \in (l(t_{i+1}), u(t_{i+1}))$ . Then the approximation appears as follows:

$$\begin{aligned} p_i^{\circ} &:= \\ P(\exists t \in [t_i, t_{i+1}] : S_t \notin (l(t), u(t)) \mid S_{t_i} = \varsigma, S_{t_{i+1}} = y) \\ &= f(t_i, \varsigma, y, \epsilon)(1 + O(\epsilon)) \end{aligned} \tag{17}$$

where the function  $f$  is indeed known explicitly:

$$f(t,\varsigma,y,\epsilon) = \exp\left\{-\frac{Q(t,\varsigma,y)}{\epsilon} - R(t,\varsigma,y)\right\}$$
(18)

with

$$Q(t,\varsigma,y) = \begin{cases} \frac{2(u(t) - \varsigma)(u(t) - y)}{\sigma^2} \\ \text{if } \varsigma + y > u(t) + l(t) \\ \frac{2(\varsigma - l(t))(y - l(t))}{\sigma^2} \\ \text{if } \varsigma + y < u(t) + l(t) \end{cases}$$
(19)

The service of

2000

and

$$R(t,\zeta,y) = \begin{cases} \frac{2(u(t) - \zeta)u'(t)}{\sigma^2} \\ \text{if } \zeta + y > u(t) + l(t) \\ \frac{2(\zeta - l(t))l'(t)}{\sigma^2} \\ \text{if } \zeta + y < u(t) + l(t) \end{cases}$$
(20)

The final estimator, with reduced bias, for the probability that  $S$  does not hit the barriers in the interval  $[0, T]$  is constructed by simulating N independent identically distributed (i.i.d.) replications  $(S^{(j)}: j \leq N)$  of the process S and obtaining

$$\frac{1}{N} \sum_{j=1}^{N} \prod_{i=0}^{m-1} I\left(S_{t_{i}}^{(j)} \in (l\left(t_{i}\right), u\left(t_{i}\right))\right) p\left(t_{i}, S_{t_{i}}^{(j)}, S_{t_{i+1}}^{(j)}\right)$$
(21)

where

$$p\left(t_{i}, S_{t_{i}}^{(j)}, S_{t_{i+1}}^{(j)}\right) = 1 - f\left(t_{i}, S_{t_{i}}^{(j)}, S_{t_{i+1}}^{(j)}, \varepsilon\right) \quad (22)$$

Large deviations analysis can also aid the application of variance reduction techniques for Monte Carlo simulation via importance sampling, as is discussed next.

### *Importance Sampling*

Once again, we concentrate on a concrete problem to illustrate the use of large deviations in the design of importance sampling (see Variance Reduction). Consider the problem of calculating equation (7). The optimal path equation  $(13)$  suggests a particular way in which one could bias the occurrence of the large deviations event; here we also consider time to maturity and barrier values to be large and thus we would be dealing with small probabilities (see Rare-event Simulation). In particular, consider a probability measure, say  $\mathbb{Q}$ , under which a process  $(Y(u): 0 < u < T)$  follows a Brownian motion with *drift*  $\theta_-$  up to time  $\tau_{-a} = \inf\{s \ge 0 : Y(u) \le -Ta\},\$ and from time  $\tau_{-a}$  up to time T (assuming  $\tau_{-a} < T$ ) the drift of  $Y(\cdot)$  is switched to the value  $\theta_{+}$ . Using the process  $Y$ , we obtain the representation

$$\alpha_T = E_{\mathbb{Q}} \left\{ I(\min_{0 \le s \le T} Y(s) \le -aT, Y(T) > bT) \times h \right\}$$
(23)

where

$$h = e^{-\theta_{-}a + \theta_{-}^{2}\tau_{-a}/2 - \theta_{+}(T - \tau_{a})(Y(T) + a) + \theta_{+}^{2}(T - \tau_{a})/2} \quad (24)$$

The expression above, involving the exponentials, is nothing but the likelihood ratio between the Wiener measure  $\mathbb{P}$  (corresponding to the process  $(B(s): 0 < s < T)$  and the measure  $\mathbb{Q}$  on the set  $I(\tau_{-a} < T)$ . More precisely,

$$\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}}I\left(\tau_{-a} < T\right) = I\left(\tau_{-a} < T\right)$$
$$\times \mathrm{e}^{-\theta_{-}a + \theta_{-}^{2}\tau_{-a}/2 - \theta_{+}(T - \tau_{-a})(Y(T) + a) + \theta_{+}^{2}(T - \tau_{-a})/2} \tag{25}$$

The use of importance sampling proceeds by simulating, say, N i.i.d. replications  $(Y_i : i < N)$ of the process  $(Y(s): 0 \le s \le T)$  and estimating  $P\left(\min_{0\leq s\leq T}B\left(s\right)\leq-a,\,B\left(T\right)>b\right)$  via

$$\alpha_T^{(N)} = \frac{1}{N} \sum_{i=1}^{N} I\left(\tau_{-a}^{(i)} < T, Y_i\left(T\right) > bT\right) \times h^{(i)}$$
(26)

where

$$h^{(i)} = e^{-\theta_{-}a + \theta_{-}^{2}\tau_{-a}^{(i)}/2 - \theta_{+} \left(T - \tau_{-a}^{(i)}\right)(Y_{i}(T) + a) + \theta_{+}^{2} \left(T - \tau_{-a}^{(i)}\right)/2}$$
(27)

Here,  $\tau_{-a}^{(i)}$ ,  $i = 1, \ldots, N$  are the i.i.d. replications of  $\tau_{-a}$  obtained from the corresponding i.i.d. processes  $Y_i$ . Moreover, large deviations theory allows to conclude that the previous importance sampling estimator satisfies certain optimality properties as  $T \nearrow \infty$  (see, for instance, [3], Ch. 7). Additional extensions of this methodology are applicable to

other types of processes. However, to design optimal importance sampling estimators, it is required to compute the associated optimal path under the corresponding rate function of the underlying process. Research in this direction has been developed recently [3, 16].

We now give a broader description of the importance sampling technique in option pricing. When pricing an option, the question is to find the expectation

$$I_g = E(g(S_t : 0 \le t \le T)) \tag{28}$$

where  $g$  is a payoff function (possibly path dependent) (see Options: Basic Definitions), and S is governed by a suitable SDE. Let us concentrate here on the geometric Brownian motion given by equation (15). The naive Monte Carlo estimator based on  $N$ replications is

$$\widehat{I}_{g}^{N} = \frac{1}{N} \sum_{i=1}^{N} g(S_{t}^{(i)} : 0 \le t \le T) \tag{29}$$

where the  $S^{(i)}$ 's are i.i.d. replications ([3], a general reference on stochastic simulation) of the process  $S$ following equation  $(15)$ .

The importance sampling procedure turns  $(28)$  into

$$I_g = E_{\mathbb{Q}}(g(S_t^{\phi}, 0 \le t \le T) \times L_T^{-1}) \qquad (30)$$

where

$$\begin{split} \mathrm{d}S_t^{\phi} &= (r + \sigma \phi_t) \, S_t^{\phi} \, \mathrm{d}t + \sigma \, S_t^{\phi} \, \mathrm{d}B_t^{\mathbb{Q}} \\ &= r \, S_t^{\phi} \, \mathrm{d}t + \sigma \, S_t^{\phi} \, \mathrm{d}B_t \end{split} \tag{31}$$

and the process  $\left(B_t^{\mathbb{Q}}: 0 \leq t \leq T\right)$  is a standard Brownian motion under  $\mathbb{Q}$ . The relation between  $B_t^{\mathbb{Q}}$ and  $B_t$  is given by

$$\mathrm{d}B_t = \phi_t \,\mathrm{d}t + \mathrm{d}B_t^{\mathbb{Q}} \tag{32}$$

The likelihood ratio  $L_T^{-1} = d\mathbb{P}/d\mathbb{Q}$  satisfies

$$L_T^{-1} = \exp\left(-\int_0^T \phi_s \, \mathrm{d}B_s + \frac{1}{2} \int_0^T \phi_s^2 \, \mathrm{d}s\right)$$
  
=  $\exp\left(-\int_0^T \phi_s \, \mathrm{d}B_s^{\mathbb{Q}} - \frac{1}{2} \int_0^T \phi_s^2 \, \mathrm{d}s\right)$  (33)

Under this specification, the importance sampling estimator takes the form

$$I_{g,IS}^{N} = \frac{1}{N} \sum_{i=1}^{N} g(S_{t,i}^{\phi}, 0 \le t \le T)) L_T^{-1}(i) \qquad (34)$$

where  $S^{\phi}_{\cdot,i}$  and  $L_T^{-1}(i)$  are obtained from the corresponding i.i.d. copies of the process  $S^{\phi}$ , which follows the evolution equations (31). Therefore, the ultimate problem is to find a process  $\phi$  (which might or might not be deterministic) that guaranties an efficient estimation of  $I_g$  in terms of variance reduction. As we indicated in the simple barrier example, large deviation techniques provide tools to find such a process  $\phi$ . In the next subsection we discuss another example.

#### Freidlin-Wentzel Theory

Let us suppose that we are dealing with a European option (see Options: Basic Definitions). Thus equa- $(28)$  becomes

$$I_{g}(x) = E(g(S_{T})|S_{0} = x)$$
(35)

and we write  $I_{g}(x)$  to emphasize the dependence on the initial position.

Using **Itô's formula**, under measure  $\mathbb{Q}$ , the variance of  $I_{g,IS}^N$  is given by

$$Var_{\mathbb{Q}}(I_{g,IS}^{N})$$

$$= \frac{1}{N} E_{\mathbb{Q}} \left( \int_{0}^{T} L_{t} (\sigma I_{g}^{\prime}(S_{t}^{\phi}) + \phi_{t} I_{g}(S_{t}^{\phi}))^{2} \mathrm{d}t \right)$$

$$(36)$$

where  $I'_{g}$  is the derivative with respect to x. One can readily see that if  $\phi_s = -\sigma I'_o(S_t^{\phi})/I_g(S_t^{\phi})$  the variance of the estimator would vanish. Unfortunately, the function  $I_g(\cdot)$  is precisely what we want to find, but the idea is to find an approximation to  $I_{\rho}(\cdot)$ , say  $\widetilde{I}_{g}(\cdot)$ , and consider  $\widetilde{\phi}_{s} = -\sigma \widetilde{I}'_{g}\left(S_{t}^{\widetilde{\phi}}\right) / I_{g}\left(S_{t}^{\widetilde{\phi}}\right)$  which can be used to generate a change of measure that reduces the variance of the associated importance sampling estimator. For instance, Fourniè et al. [13] suggest developing a parametric expansion for  $I_g(x)$ as a function of  $\sigma$  as  $\sigma \searrow 0$ . In turn, such an expansion is based, for options out of the money, on the Freidlin-Wentzel theory.

#### Varadhan–Laplace Principle

Recall that under the geometric Brownian motion, model  $(15)$ , the path simulation at discrete-time points satisfies

$$S_{t_{i+1}} = S_{t_i} \exp\left(\left(r - \frac{\sigma^2}{2}\right)\epsilon + \sigma\sqrt{\epsilon}Z_i\right) \tag{37}$$

where  $Z_i \sim N(0, 1)$  for  $i = 1, \ldots, n$ . Let  $\mathbf{Z} =$  $(Z_1,\ldots,Z_n)^\top$  ( $\top$  stands for the transpose), then we denote by  $G(Z)$  the payoff of the option under a sample  $Z$ , for instance, for the Asian option we have  $G(Z) = \max\left(0, \frac{1}{n}\sum_{i=1}^{n} S_{t_i} - K\right)$ . In this case, the partition indicates the times when the process is monitored to take the average.

The procedure developed in  $[14]$  is to change the mean of **Z** from 0 to a vector  $\boldsymbol{\mu}$  to obtain an estimator of  $I_{\rho}$ . Multiplying each sample by the corresponding importance sampling weight or likelihood ratio the estimator is then

$$I_g^N = \frac{1}{N} \sum_{i=1}^N G(Z^{(i)}) \exp\left(-\boldsymbol{\mu}^\top Z^{(i)} + \frac{1}{2}\boldsymbol{\mu}^\top \boldsymbol{\mu}\right)$$
(38)

where  $\mathbf{Z}^{(i)}$  is the vector  $(Z_1^{(i)}, \ldots, Z_n^{(i)})^{\top}$  of independent random variables such that  $Z_j^{(i)} \sim N(\mu_j, 1)$ ,  $j = 1, ..., n$ . The  $Z^{(i)}$ 's,  $i = 1, ..., N$  are i.i.d. replications. To choose  $\mu$  it suffices to minimize the variance of  $I_g^N$ , which turns out to be equivalent to minimizing

$$E\left(G(Z)^{2} \exp\left(-\boldsymbol{\mu}^{\top} \boldsymbol{Z} + \frac{1}{2} \boldsymbol{\mu}^{\top} \boldsymbol{\mu}\right)\right) \tag{39}$$

where  $\mathbf{Z}$  here is an *n*-dimensional vector of i.i.d. standard Gaussian random variables. It is not an easy task to solve this optimization problem, but it can be tackled using Varadhan-Laplace asymptotics. The idea is to scale **Z** by  $\sqrt{\epsilon}$  and asymptotically estimate the expectation in equation (39) as  $\epsilon \to 0$ . This approach makes it simpler to find the optimal  $\mu$ , at least as an approximation, which is asymptotically correct in an environment of small volatility, that is,  $\sigma$  close to 0 in equation (15).

Another interesting application of large deviations principles is in the context of index option pricing. Consider an index  $H$  composed of  $m$  stocks  $(S_1, \ldots, S_m)$ . The index at time t is computed as  $H(t) = \sum_{i=1}^{m} w_i S_i$ , where  $w_1, \ldots, w_m$  are constants.

Pricing, for instance, a European call on the index involves knowing the so-called local volatility function (see Local Volatility Model) of the index. What is proposed in  $[4]$  is to approximate such a function using Varadhan's principle to handle it in a simpler way, and therefore, pricing the option.

### **Risk Management**

The use of large deviations theory for computational purposes also arises in the context of risk management. For instance, Dembo *et al.* [7] developed approximations based on large deviations theory for the tail of a loss distribution; a relevant assumption is that the individual losses are conditionally i.i.d., given the state of the economy and their identifying class (these parameters can be given by the specific industry or business line).

#### Credit Risk

Typically, an important task in credit risk theory (*see* **Credit Risk**) involves computing the distribution of losses in a portfolio composed of several debt contracts. More precisely, in a portfolio composed of  $n$  obligors, the question is to calculate the tail probability of  $L_n = c_1 Y_1 + \cdots + c_n Y_n$ ,

$$P(L_n > l) \tag{40}$$

where the  $Y_i$ 's are Bernoulli random variables such that  $P(Y_i = 1) = p_i = 1 - P(Y_i = 0)$ , and indicating that the *i* obligor (for  $i = 1, \ldots, n$ ) may or may not default. The  $c_i$ 's represent the loss resulting from the default, and  $l$  is a threshold. Generally, the number of obligors is large, and surpassing threshold  $l$ may be a rare event, which represents significant losses, in which case one may use large deviations theory to approximate the probability in equation  $(40)$ . In [15] such a probability is approximated under a multifactor Gaussian copula model (see Gaussian **Copula Model**) and using large deviation theory; here we present some results that can be found in [21].

Suppose that the variables  $Y_i$ ,  $i = 1, \ldots, n$  are triggered by other variables  $X_i, i = 1, \ldots, n$  that might or not be related; this is done in the following way:  $Y_i = 1_{\{X_i > x_i\}}, i = 1, \ldots, n$  and the vector  $(X_1, \ldots, X_n)$  is normally distributed. The parameters  $x_i$  are such that  $P(X_i > x_i) = p_i$  for  $i = 1, \ldots, n$ .

The correlations among variables  $\{X_1, \ldots, X_n\}$  are determined by the following single-factor model:

$$X_i = \rho Z + \sqrt{1 - \rho^2} Z_i, i = 1, \dots, n \qquad (41)$$

where  $\rho \in [0, 1)$  and  $Z, Z_1, \ldots, Z_n$  are independent standard normal random variables (r.v's).

When  $\rho = 0$ , there is no correlation, and using Cramér's theorem one can find an asymptotic formula. Suppose that  $p_i = p, i = 1, \ldots, n$ . Then

$$\lim_{n \to \infty} \frac{1}{n} \log P(L_n > nq) = -q \ln(q/p) \ln\left(\frac{1-q}{1-p}\right)$$
(42)

where  $l = nq$  and  $q \in (p, 1)$ .

When  $\rho > 0$ , that is, there is dependence among obligors, it is also possible to derive an asymptotic result. Indeed, if  $q_n = 1 - n^{-a}$  with  $a \in (0, 1)$ , it is shown in  $[21]$  that

$$\lim_{n \to \infty} \frac{1}{\log n} \log P(L_n > nq_n) = -a \frac{1 - \rho^2}{\rho^2} \qquad (43)$$

A more elaborate model of this type is treated in [15].

We have discussed the use of large deviations theory in several computational settings, both in pricing and in risk assessment. Another application of large deviations, also in the context of risk management, arises in the theoretical analysis of risk measures.

## Risk Measures

Financial institutions are constantly worried about the quantification of the risk in their portfolios of assets: stocks, bonds, credits, and options (see Risk **Exposures**). A financial asset is generally represented by a random variable, say  $X$ , and characterized by the probability measure  $\mu$  that governs the outcome of X, that is, we write  $\mathcal{L}(X) = \mu$  whenever  $P(X \in A) =$  $\mu(A)$ . The risk associated with X is measured by means of a so-called *risk measure*  $\rho$ , which is a realvalued function on the space of random variables that satisfies certain properties (such as monotonicity, subadditivity, positive homogeneity, and translation invariance); see  $[2]$ .

Assume that it is not possible to deal with the probability measure  $\mu$  directly, but instead we have independent samples  $X_1, \ldots, X_n$  of X. Then, one may want to approximate  $\rho(X)$  by calculating  $\rho(X^{(n)})$ ; in this case,  $X^{(n)}$  is a random variable and its law  $\mathcal{L}(X^{(n)})$  is the empirical measure

$$\mu_n = \frac{1}{n} \sum_{i=1}^n \delta_{X_i} \tag{44}$$

Here  $\delta_X$  stands for the Dirac measure at X.

This approach generates an error, and the question suggested in [25] is to quantify the error by considering the asymptotics, as  $n \to \infty$ , of

$$P\left(\left|\rho(X) - \rho(X^{(n)})\right| > \epsilon\right), \text{ for } \epsilon > 0 \tag{45}$$

Then, for positive  $\epsilon$  and when  $n \to \infty$ , the previous quantity becomes small, and large deviation principles can be used to deal with this probability. An important result used for this is Sanov's theorem  $[8]$ .

## **Optimal Investment**

We now move to investment. Maximizing revenue in investments under a certain risk profile (which could be induced by a specific set of assets types) has been a common question for financial investors. To tackle the problem, the usual approaches are the mean-variance analysis of Markowitz (see **Risk–Return Analysis**) or the use of utility functions (see Utility Function; Expected Utility Maximization). Alternatively, a criterion can be set by considering asymptotic performance of the portfolio over long time horizons [1]. One has to decide how to measure such a performance, and one way to do this is by estimating, given a fixed investment policy, the probability of performing well [6, 12]. The optimization problem can be set as selecting the investment policy that minimizes the probability of ending up below a threshold or the one that maximizes the probability of surpassing it. Since the problem involves calculating an asymptotic probability, it is appealing to use large deviations techniques (one can find this approach in [19, 20, 23, 24]).

As an illustration, we describe below the method described by Pham in [19, 20]. Given an investment policy  $\alpha \in \mathcal{A}$  (where  $\mathcal{A}$  is the set of admissible investment policies), we consider the rate of return of the associated wealth process (i.e., the logarithm of the value of the portfolio obtained by applying the policy  $\alpha$ ). We denote such a rate of return process by  $X(\alpha) = (X_t(\alpha), t \ge 0)$ . The aim is to maximize over A the probability  $P(X_t(\alpha)/t \ge x)$  in the long term, which is the probability of a rare event as  $t \rightarrow$  $\infty$ . Here, level  $x \in \mathbb{R}$  represents a benchmark that an investor wants to achieve; in [6] it is considered as a stochastic benchmark, such as an index.

It is natural to attempt using large deviations theory to find a (static) policy  $\alpha^*$  from

$$v(x, \alpha^*) := \sup_{\alpha \in \mathcal{A}} v(x, \alpha) \tag{46}$$

where

$$v(x,\alpha) = -\lim_{t \to \infty} \frac{1}{t} \log P\left(X_t\left(\alpha\right)/t > x\right) \quad (47)$$

Under regularity conditions on the drift and the volatility of the process  $X_t(\alpha)$  (for instance, if the drift and diffusion coefficients are bounded and continuously differentiable), one can evaluate  $v(x)$ via

$$v(x,a) = \sup_{\theta} (\theta x - \Gamma(\theta,\alpha)) \tag{48}$$

where

$$\Gamma(\theta,\alpha) := \limsup_{t \to \infty} \frac{1}{t} \ln E\left(e^{\theta X_t(\alpha)}\right) \tag{49}$$

This approach is considered in [19]. For instance, if  $X_t(\alpha) = \alpha Y(t)$  where  $\alpha \in \mathbb{R}$  and  $Y(t) = rt +$  $\sigma B(t)$  with  $r > 0$  and  $B(\cdot)$  is a standard Brownian motion, we have that

$$\Gamma(\theta,\alpha) = \theta\alpha r + \frac{(\theta\alpha\sigma)^2}{2} \tag{50}$$

and then the problem is solved when  $\alpha = x/r$  [21]. More sophisticated and also explicit calculations can be found in [19].

#### References

- [1] Algoet, P.H. & Cover, T.M. (1988). Asymptotic optimality and asymptotic equipartition properties of logoptimum investment, The Annals of Probability 16(2), 876-898.
- [2] Artzner, P., Delbaen, F., Eber, J.M. & Heath, D. (1999). Coherent measures of risk, Mathematical Finance 9(3),  $203 - 228$
- [3] Asmussen, S. & Glynn, P.W. (2007). Stochastic Simulation: Algorithms and Analysis, Springer.
- [4] Avellaneda, M., Boyer-Olson, D., Busca, J. & Friz, P. (2003). Méthodes de grandes déviations et pricing

d'options sur indices, *Comptes rendus de l'Academie des sciences. Paris* **336**, 263–266.

- [5] Baldi, P., Caramellino, L. & Iovino, M.G. (1999). Pricing general barrier options: a numerical approach using sharp large deviations, *Mathematical Finance* **9**(4), 293–322.
- [6] Browne, S. (1999). Beating a moving target: Optimal portfolio strategies for outperforming stochastic benchmark, *Stochastic and Finance* **3**, 275–294.
- [7] Dembo, A., Deuschel, J.D. & Duffie, D. (2004). Large portfolio losses, *Stochastic and Finance* **8**, 3–16.
- [8] Dembo, A. & Zeitouni, O. (1999). *Large Deviation Techniques and Applications*, Springer.
- [9] Deuschel, J.-D. & Strook, D.W. (1989). *Large Deviation*, AMS Chelsea Publishing.
- [10] Dupuis, P. & Ellis, R.S. (1997). *A Weak Convergence Approach to the Theory of Large Deviations*, John Wiley & Sons, Inc.
- [11] Donsker, M.D. & Varadhan, S.R.S. (1983). Asymptotic evaluation of certain Markov process expectations for large time, *Communications on Pure and Applied Mathematics*; (I (1975) **28**, 1–47); (II (1975) **28**, 279–301); (III (1976) **29**, 389–461); (IV (1983) **36**, 183–212).
- [12] Follmer, H. & Leukert, P. (1999). Quantile Hedging, ¨ *Stochastics and Finance* **3**, 251–273.
- [13] Fournie, E., Lasry, J.M. & Touzi, N. (1997). Monte ` Carlo methods for stochastic volatility models, in *Numerical Methods in Finance*, L.C.G. Rogers & D. Talay, eds, Cambridge University Press.
- [14] Glasserman, P., Heidelberg, P. & Shahabuddin, P. (1999). Asymptotically optimal importance sampling and stratification for pricing path-dependent option, *Mathematical Finance* **9**(2), 117–152.
- [15] Glasserman, P., Kang, W. & Shahabuddin, P. (2007). Large deviations in multifactor portfolio credit risk, *Mathematical Finance* **17**(3), 345–379.
- [16] Guasoni, P. & Robertson, S. (2008). Optimal importance sampling with explicit formulas in continuous time, *Finance and Stochastics* **12**, 1–19.
- [17] Karatzas, I. & Shreve, S.E. (1998). *Brownian Motion and Stochastic Calculus*, Springer.
- [18] Klebaner, F. (2005). *Introduction to Stochastic Calculus with Applications*, 2nd Edition, Imperial College Press.
- [19] Pham, H. (2003). A large deviations approach to optimal long term investment, *Finance and Stochastics* **7**, 169–195.

- [20] Pham, H. (2003). A risk-sensitive control dual approach to a large deviations control problem, *Systems and Control Letters* **49**, 295–309.
- [21] Pham, H. (2008). *Some Applications and Methods of Large Deviations in Finance and Insurance*, Lectures from a Bachelier course at Institute Henri Poincare, Paris.
- [22] Shwartz, A. & Weiss, A. (1995). *Large Deviation for Performance Analysis*, Chapman & Hall.
- [23] Sornette, D. (1998). Large deviations and portfolio optimization, *Physica A* **256**, 251–283.
- [24] Stutzer, M. (2003). Portfolio choice with endogenous utility: a large deviations approach, *Journal of Econometrics* **116**, 365–386.
- [25] Weber, S. (2007). Distribution-invariant risk measures entropy, and larger deviations, *Journal of Applied Probability* **44**, 16–40.

# **Further Reading**

- Bares, P., Cont, R., Gardiol, L., Gibson, R. & Gyger, S. (2000). A large deviation approach to portfolio management, *International Journal of Theoretical and Applied Finance* **3**, 617–639.
- Huh, J. & Kolkiewicz, A. (2006). *Efficient Computation of Multivariate Barrier Crossing Probability and its Applications in Credit Risk Models*, manuscript.

# **Related Articles**

**Cramer's Theorem ´** ; **Esscher Transform**; **Implied Volatility: Large Strike Asymptotics**; **Implied Volatility: Long Maturity Behavior**; **Monte Carlo Simulation**; **Rare-event Simulation**; **SABR Model**; **Saddlepoint Approximation**; **Variance Reduction**.

> JOSE H. BLANCHET & CARLOS G. PACHECO-GONZALEZ ´
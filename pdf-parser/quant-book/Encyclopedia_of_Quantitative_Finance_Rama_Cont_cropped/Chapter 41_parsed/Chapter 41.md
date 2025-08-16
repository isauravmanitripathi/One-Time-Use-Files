# **Markov Processes**

A Markov process is a process that evolves in a memoryless way: its future law depends on the past only through the present position of the process. This property can be formalized in terms of conditional expectations: a process  $(X_t, t \ge 0)$  adapted to the **filtration**  $(\mathcal{F}_t)_{t>0}$  (representing the information available at time  $t$ ) is a Markov process if

$$\mathbb{E}(f(X_{t+s}) \mid \mathcal{F}_t) = \mathbb{E}(f(X_{t+s}) \mid X_t) \tag{1}$$

for all  $s, t \ge 0$  and  $f$  bounded and measurable.

The interest of such a process in financial models becomes clear when one observes that the price of an option, or more generally, the value at time  $t$  of any future claim with maturity  $T$ , is given by the general formula (see Risk-neutral Pricing)

$$V_t = \text{value at time } t$$
  
=  $\mathbb{E}(\text{discounted payoff at time } T \mid \mathcal{F}_t)$  (2)

where the expectation is computed with respect to a pricing measure (see Equivalent Martingale Measures). The Markov property is a frequent assumption in financial models because it provides powerful tools (semigroup, theory of partial differential equations (PDEs), etc.) for the quantitative analysis of such problems.

Assuming the Markov property (1) for  $(S_t, t > 0)$ , the value  $V_t$  of the option can be expressed as

$$V_t = \mathbb{E}(\mathrm{e}^{-r(T-t)}f(S_T) \mid \mathcal{F}_t)$$
  
=  $\mathbb{E}(\mathrm{e}^{-r(T-t)}f(S_T) \mid S_t)$  (3)

so  $V_t$  can be expressed as a (deterministic) function of  $t, S_t: u(t, S_t) = \mathbb{E}(e^{-r(T-t)}f(S_T) | S_t)$ . Furthermore, this function  $u$  is shown to be the solution of a parabolic PDE, the Kolmogorov backward equation.

The goal of this article is to present the Markov processes and their relation with PDEs, and to illustrate the role of Markovian models in various financial problems. We give a general overview of the links between Markov processes and PDEs without giving more details and we focus on the case of Markov processes solution to stochastic differential equations (SDEs).

We will restrict ourselves to  $\mathbb{R}^d$ -valued Markov processes. The set of Borel subsets of  $\mathbb{R}^d$  is denoted

by  $\mathcal{B}$ . In the following, we will denote a Markov process by  $(X_t, t \ge 0)$ , or simply X when no confusion is possible.

# **Markov Property and Transition** Semigroup

A Markov process retains no memory of where it has been in the past. Only the current state of the process influences its future dynamics. The following definition formalizes this notion:

**Definition 1** Let  $(X_t, t > 0)$  be a stochastic process defined on a probability filtered space  $(\Omega, \mathcal{F}_t, \mathbb{P})$  with values in  $\mathbb{R}^d$ . X is a Markov process if

$$\mathbb{P}(X_{t+s} \in \Gamma \mid \mathcal{F}_t) = \mathbb{P}(X_{t+s} \in \Gamma \mid X_t) \quad \mathbb{P}\text{-a.s.}$$
(4)

for all  $s, t \ge 0$  and  $\Gamma \in \mathcal{B}$ . Equation (4) is called the Markov property of the process  $X$ . The Markov process is called time homogeneous if the law of  $X_{t+s}$ conditionally on  $X_t = x$  is independent of t.

Observe that equation  $(4)$  is equivalent to equation (1) and that  $X$  is a time-homogeneous Markov process if there exists a positive function  $P$  defined on  $\mathbb{R}_+ \times \mathbb{R}^d \times \mathcal{B}$  such that

$$P(s, X_t, \Gamma) = \mathbb{P}(X_{t+s} \in \Gamma \mid \mathcal{F}_t) \tag{5}$$

holds  $\mathbb{P}$ -a.s. for all  $t, s \geq 0$  and  $\Gamma \in \mathcal{B}$ . *P* is called the transition function of the time homogeneous Markov process  $X$ .

For the moment, we restrict ourselves to the timehomogeneous case.

**Proposition 1** The transition function  $P$  of a timehomogeneous Markov process X satisfies

- 1.  $P(t, x, \cdot)$  is a probability measure on  $\mathbb{R}^d$  for any  $t > 0$  and  $x \in \mathbb{R}^d$ ,
- 2.  $P(0, x, \cdot) = \delta_x$  (unit mass at x) for any  $x \in \mathbb{R}^d$ ,
- 3.  $P(\cdot, \cdot, \Gamma)$  is measurable for any  $\Gamma \in \mathcal{B}$ ,

and for any  $s, t \ge 0, x \in \mathbb{R}^d, \Gamma \in \mathcal{B}, P$  satisfies the *Chapman–Kolmogorov property* 

$$P(t+s,x,\Gamma) = \int_{\mathbb{R}^d} P(s,y,\Gamma) P(t,x,\mathrm{d}y) \qquad (6)$$

From an analytical viewpoint, we can think of the transition function as a Markov semigroup<sup>a</sup>  $(P_t, t >$ 0), defined by

$$P_t f(x) := \int_{\mathbb{R}^d} P(t, x, dy) f(dy)$$
  
=  $\mathbb{E}(f(X_t) | X_0 = x)$  (7)

in which case the Chapman-Kolmogorov equation becomes the *semigroup property* 

$$P_s P_t = P_{t+s}, \quad s, t \ge 0 \tag{8}$$

Conversely, given a Markov semigroup  $(P_t, t >$ 0) and a probability measure  $\nu$  on  $\mathbb{R}^d$ , it is always possible to construct a Markov process  $X$  with initial law  $\nu$  that satisfies equation (7) (see [9, Th.4.1.1]). The links between PDEs and Markov processes are based on this equivalence between semigroups and Markov processes. This can be expressed through a single object: the infinitesimal generator.

#### Strong Markov Property, Feller Processes

Recall that a random time  $\tau$  is called a  $\mathcal{F}_t$ -stopping *time* if  $\{\tau \le t\} \in \mathcal{F}_t$  for any  $t \ge 0$ .

**Definition 2** A Markov process  $(X_t, t > 0)$  with transition function  $P(t, x, \Gamma)$  is strong Markov if, for any  $\mathcal{F}_t$ -stopping time  $\tau$ ,

$$\mathbb{P}(X_{\tau+t} \in \Gamma \mid \mathcal{F}_{\tau}) = P(t, X_{\tau}, \Gamma) \tag{9}$$

for all  $t \geq 0$  and  $\Gamma \in \mathcal{B}$ .

Let  $C_0(\mathbb{R}^d)$  denote the space of bounded continuous functions on  $\mathbb{R}^d$ , which vanish at infinity, equipped with the  $L^{\infty}$  norm denoted by  $\|\cdot\|$ .

**Definition 3** A Feller semigroup<sup>b</sup> is a strongly continuous,<sup>c</sup> positive, Markov semigroup  $(P_t, t > 0)$ such that  $P_t: C_0(\mathbb{R}^d) \to C_0(\mathbb{R}^d)$  and

$$\begin{aligned} \forall f \in C_0(\mathbb{R}^d), \ \ 0 \le f \Rightarrow 0 \le P_t f \\ \forall f \in C_0(\mathbb{R}^d) \ \ \forall x \in \mathbb{R}^d, \ \ P_t f(x) \to f(x) \ \ as \ t \to 0 \end{aligned} \tag{10}$$

For a Feller semigroup, the corresponding Markov process can be constructed as a strong Markov process.

**Theorem 1** ([9] Th.4.2.7). Given a Feller semigroup  $(P_t, t \ge 0)$  and any probability measure v on  $\mathbb{R}^d$ , there exists a filtered probability space  $(\Omega, \mathcal{F}_t, \mathbb{P})$ and a strong Markov process  $(X_t, t > 0)$  on this space with values in  $\mathbb{R}^d$  with initial law v and with transition function  $P_t$ . A strong Markov process whose semigroup is Feller is called a Feller process.

## **Infinitesimal Generator**

We are now in a position to introduce the key notion of *infinitesimal generator* of a Feller process.

**Definition 4** For a Feller process  $(X_t, t > 0)$ , the infinitesimal generator of  $X$  is the (generally unbounded) linear operator  $L: \mathcal{D}(L) \to C_0(\mathbb{R}^d)$  defined as follows. We write  $f \in \mathcal{D}(L)$  if, for some  $g \in$  $C_0(\mathbb{R}^d)$ , we have

$$\frac{\mathbb{E}(f(X_t) \mid X_0 = x) - f(x)}{t} \to g(x) \tag{11}$$

when  $t \rightarrow 0$  for the norm  $\|\cdot\|$ , and we then define  $Lf = g.$ 

By Theorem 1, an equivalent definition can be obtained by replacing  $X$  by its Feller semigroup  $(P_t, t \ge 0)$ . In particular, for all  $f \in \mathcal{D}(L)$ ,

$$Lf(x) = \lim_{t \to 0} \frac{P_t f(x) - f(x)}{t}$$
(12)

An important property of the infinitesimal generator is that it allows one to construct fundamental martingales associated with a Feller process.

**Theorem 2** ([21], III.10). Let  $X$  be a Feller process on  $(\Omega, \mathcal{F}_t, \mathbb{P})$  with infinitesimal generator L such that  $X_0 = x \in \mathbb{R}^d$ . For all  $f \in \mathcal{D}(L)$ ,

$$f(X_t) - f(x) - \int_0^t Lf(X_s) \, \mathrm{d}s \tag{13}$$

defines a  $\mathcal{F}_t$ -martingale. In particular,

$$\mathbb{E}(f(X_t)) = f(x) + \mathbb{E}\Big(\int_0^t Lf(X_s) \,\mathrm{d}s\Big) \qquad (14)$$

As explained earlier, the law of a Markov process is characterized by its semigroup. In most cases, a Feller semigroup can be itself characterized by its infinitesimal generator (the precise conditions for this to hold are given by the Hille-Yosida theorem, see [21, Th.III.5.1]). For almost all Markov financial models, these conditions are well established and always satisfied (see Examples 1, 2, 3, and 4). As illustrated by equation (14), when  $\mathcal{D}(L)$  is large enough, the infinitesimal generator captures the law of the whole dynamics of a Markov process and provides an analytical tool to study the Markov process. The other major mathematical tool used in finance is the stochastic calculus (see Stochastic integral, Itô formula), which applies to Semimartingales (see  $[18]$ ). It is therefore crucial for applications to characterize under which conditions a Markov process is a semimartingale. This question is answered for very general processes in  $[5]$ . We mention that this is always the case for Feller diffusions, defined later.

## **Feller Diffusions**

Let us consider the particular case of continuous Markov processes, which include the solutions of stochastic differential equations (SDEs).

**Definition 5** A Feller diffusion on  $\mathbb{R}^d$  is a Feller process X on  $\mathbb{R}^d$  that has continuous paths, and such *that the domain*  $\mathcal{D}(L)$  *of the generator*  $L$  *of*  $X$  *contains* the space  $C_K^{\infty}(\mathbb{R}^d)$  of infinitely differentiable functions of compact support.

Feller diffusions are Markov processes admitting a second-order differential operator as infinitesimal generator.

**Theorem 3** For any  $f \in C_K^{\infty}(\mathbb{R}^d)$ , the infinitesimal generator  $L$  of a Feller diffusion has the form

$$Lf(x) = \frac{1}{2} \sum_{i,j=1}^{d} a_{ij}(x) \frac{\partial^2 f}{\partial x_i \partial x_j}(x) + \sum_{i=1}^{d} b_i(x) \frac{\partial f}{\partial x_i}(x)$$
(15)

where the functions  $a_{ij}(\cdot)$  and  $b_i(\cdot)$ ,  $1 \le i, j \le d$ are continuous and the matrix  $a = (a_{ij}(x))_{1 \le i, j \le d}$  is nonnegative definite symmetric for all  $x \in \mathbb{R}^d$ .

#### Kolmogorov Equations

Observe by equation (12) that the semigroup  $P_t$  of a Feller process  $X$  satisfies the following differential

equation; for all  $f \in \mathcal{D}(L)$ ,

$$\frac{\mathrm{d}}{\mathrm{d}t}P_t f = L P_t f \tag{16}$$

This equation is called *Kolmogorov's backward equation*. In particular, if  $L$  is a differential operator (e.g., if X is a Feller diffusion), the function  $u(t,x) =$  $P_t f(x)$  is the solution of the PDE

$$\begin{cases} \frac{\partial u}{\partial t} = Lu \\ u(0, x) = f(x) \end{cases} \tag{17}$$

Conversely, if this PDE admits a unique solution, then its solution is given by

$$u(t,x) = \mathbb{E}(f(X_t) \mid X_0 = x) \tag{18}$$

This is the simplest example of a probabilistic interpretation of the solution of a PDE in terms of a Markov process.

Moreover, because Feller semigroups are strongly continuous, it is easy to check that the operators  $P_t$ and L commute. Therefore, equation (16) may be rewritten as

$$\frac{\mathrm{d}}{\mathrm{d}t}P_t f = P_t L f \tag{19}$$

This equation is known as Kolmogorov's forward equation. It is the weak formulation of the equation

$$\frac{\mathrm{d}}{\mathrm{d}t}\mu_t^x = L^*\mu_t^x \tag{20}$$

where the probability measure  $\mu_t^x$  on  $\mathbb{R}^d$  denotes the law of  $X_t$  conditioned on  $X_0 = x$  and where  $L^*$  is the adjoint operator of  $L$ . In particular, with the notation of Theorem 3, if *X* is a Feller diffusion and if  $\mu_t^x$ (dy) admits a density  $q(x;t,y)$  with respect to Lebesgue's measure on  $\mathbb{R}^d$  (which holds, e.g., if the functions  $b_i(x)$  and  $a_{ii}(x)$  are bounded and locally Lipschitz, if the functions  $a_{ij}(x)$  are globally Hölder and if the matrix  $a(x)$  is uniformly positive definite [10,  $Th.6.5.2$ ], the forward Kolmogorov equation is the weak form (in the sense of the distribution theory) of the PDE

$$\frac{\partial}{\partial t}q(x;t,y) = -\sum_{i=1}^{d} \frac{\partial}{\partial y_i} (b_i(y)q(x;t,y))$$
$$+ \sum_{i,j=1}^{d} \frac{\partial^2}{\partial y_i \partial y_j} (a_{ij}(y)q(x;t,y)) \quad (21)$$

This equation is known as Fokker-Planck equation and gives another family of PDEs that have probabilistic interpretations. Fokker-Planck equation has applications in finance for quantiles, Value at Risk, or risk measure computations [22], whereas Kolmogorov's backward equation (17) is more suited to financial problems related to the hedging of derivatives products or portfolio allocation (see the section "Parabolic PDEs Associated to Markov Processes". and sequel).

#### **Time-inhomogeneous Markov Processes**

The law of a time-inhomogeneous Markov process is described by the doubly indexed family of operators  $(P_{s,t}, 0 \le s \le t)$  where, for any bounded measurable  $f$  and any  $x \in \mathbb{R}^d$ ,

$$P_{s,t}f(x) = \mathbb{E}(f(X_t) \mid X_s = x) \tag{22}$$

Then, the semigroup property becomes, for  $s \le t \le r$ ,

$$P_{s,t}P_{t,r} = P_{s,r} \tag{23}$$

Definition 3 of Feller semigroups can be generalized to time-inhomogeneous processes as follows. The time-inhomogeneous Markov process  $X$ is called a Feller time-inhomogeneous process if  $(P_{s,t}, 0 < s < t)$  is a family of positive, Markov linear operators on  $C_0(\mathbb{R}^d)$  which is strongly continuous in the sense

$$\forall s \ge 0, \quad x \in \mathbb{R}^d, \ f \in C_0(\mathbb{R}^d), \quad \|P_{s,t}f - f\| \to 0$$
  
as  $t \to s$  (24)

In this case, it is possible to generalize the notion of infinitesimal generator. For any  $t$ , let

$$L_{t}f(x) = \lim_{s \to 0} \frac{P_{t,t+s}f(x) - f(x)}{s}$$
$$= \lim_{s \to 0} \frac{\mathbb{E}\left[f(X_{t+s}) \mid X_{t} = x\right] - f(x)}{s}$$
(25)

for any  $f \in C_0(\mathbb{R}^d)$  such that  $L_t f \in C_0(\mathbb{R}^d)$  and the limit above holds in the sense of the norm  $\|\cdot\|$ . The set of such  $f \in C_0(\mathbb{R}^d)$  is called the *domain*  $\mathcal{D}(L_t)$ of the operator  $L_t$ .  $(L_t, t \ge 0)$  is called the *family of*  time-inhomogeneous infinitesimal generators of the process  $X$ .

All the results on Feller processes stated earlier can be easily transposed to the time-inhomogeneous case, observing that if  $(X_t, t \ge 0)$  is a timeinhomogeneous Markov process on  $\mathbb{R}^d$ , then  $(\tilde{X}_t, t \geq$ 0), where  $\tilde{X}_t = (t, X_t)$  is a time-homogeneous Markov process on  $\mathbb{R}_+ \times \mathbb{R}^d$ . Moreover, if *X* is timeinhomogeneous Feller, it is elementary to check that the process  $\tilde{X}$  is time-homogeneous Feller as defined in Definition 3. Its semigroup  $(\tilde{P}_t, t \ge 0)$  is linked to the time-inhomogeneous semigroup by the relation

$$\tilde{P}_t f(s, x) = \mathbb{E}[f(s+t, X_{s+t}) \mid X_s = x] \\
= (P_{s, s+t} f(s+t, \cdot))(x) \tag{26}$$

for all bounded and measurable  $f: \mathbb{R}_+ \times \mathbb{R}^d \to$  $\mathbb{R}$ . If  $\tilde{L}$  denotes the infinitesimal generator of the process  $\tilde{X}$ , it is elementary to check that, for any  $f(t,x) \in \mathcal{D}(\tilde{L})$  that is differentiable with respect to t, with derivative uniformly continuous in  $(t, x)$ ,  $x \mapsto f(t, x)$  belongs to  $\mathcal{D}(L_t)$  for any  $t \geq 0$  and

$$\tilde{L}f(t,x) = \frac{\partial f}{\partial t}(t,x) + \left(L_t f(t,\cdot)\right)(x) \tag{27}$$

On this observation, it is possible to apply Theorem 3 to time-inhomogeneous Feller diffusions, defined as continuous time-inhomogeneous Feller processes with infinitesimal generators  $(L_t, t \ge 0)$  such that  $C_K^{\infty}(\mathbb{R}^d) \subset \mathcal{D}(L_t)$  for any  $t \geq 0$ . For such processes, there exist continuous functions  $b_i$  and  $a_{ij}$ ,  $1 \le i, j \le j$ d from  $\mathbb{R}_+ \times \mathbb{R}^d$  to  $\mathbb{R}$  such that the matrix  $a(t, x) =$  $(a_{i,j}(t,x))_{1\leq i,j\leq d}$  is symmetric nonnegative definite and

$$L_t f(x) = \frac{1}{2} \sum_{i,j=1}^d a_{ij}(t,x) \frac{\partial^2 f}{\partial x_i \partial x_j}(x)$$
$$+ \sum_{i=1}^d b_i(t,x) \frac{\partial f}{\partial x_i}(x) \tag{28}$$

for all  $t \ge 0$ ,  $x \in \mathbb{R}^d$  and  $f \in C_K^{\infty}(\mathbb{R}^d)$ .

For more details on time-inhomogeneous Markov processes, we refer to  $[10]$ .

Example 1 Brownian Motion The standard onedimensional Brownian motion  $(B_t, t \ge 0)$  is a Feller diffusion in  $\mathbb{R}$   $(d = 1)$  such that  $B_0 = 0$  and for

which the parameters of Theorem 3 are  $b = 0$  and  $a = 1$ . The Brownian motion is the fundamental prototype of Feller diffusions. Other diffusions are inherited from this process because they can be expressed as solutions to SDEs driven by independent Brownian motions (see later). Similarly, the standard  $d$ -dimensional Brownian motion is a vector of  $d$  independent standard one-dimensional Brownian motions and corresponds to the case  $b_i = 0$  and  $a_{ij} = \delta_{ij}$  for  $1 \leq i, j \leq d$ , where  $\delta_{ij}$  is the Kronecker delta function ( $\delta_{ij} = 1$  if  $i = j$  and 0 otherwise).

Example 2 Black-Scholes Model In the Black-Scholes model, the underlying asset price  $S_t$  follows a geometric Brownian motion with constant drift  $\mu$ and volatility  $\sigma$ .

$$S_t = S_0 \exp\left((\mu - \sigma^2/2)t + \sigma B_t\right) \tag{29}$$

where  $B$  is a standard Brownian motion. With Itô's formula, it is easily checked that  $S$  is a Feller diffusion with infinitesimal generator

$$Lf(x) = \mu x f'(x) + \frac{1}{2}\sigma^2 x^2 f''(x) \tag{30}$$

Itô's formula also yields

$$S_t = S_0 + \mu \int_0^t S_s \, \mathrm{d}s + \sigma \int_0^t S_s \, \mathrm{d}B_s \tag{31}$$

which can be written as the SDE

$$dS_t = \mu S_t dt + \sigma S_t dB_t \tag{32}$$

The correspondence between the SDE and the second-order differential operator  $L$  appears below as a general fact.

Example 3 Stochastic Differential Equations SDEs are probably the most used Markov models in finance. Solutions of SDEs are examples of Feller diffusions. When the parameters  $b_i$  and  $a_{ij}$  of Theorem 3 are sufficiently regular, a Feller process  $X$ with generator equation  $(15)$  can be constructed as the solution of the SDE

$$dX_t = b(X_t)dt + \sigma(X_t) dB_t \tag{33}$$

where  $b(x) \in \mathbb{R}^d$  is  $(b_1(x), \ldots, b_d(x))$ , where the  $d \times r$  matrix  $\sigma(x)$  satisfies  $a_{ij}(x) = \sum_{k=1}^r \sigma_{ik}(x) \sigma_{jk}(x)$ 

(i.e.,  $a = \sigma \sigma'$ ) and where  $B_t$  is a r-dimensional standard Brownian motion. For example, when  $d = r$ , one can take for  $\sigma(x)$  the symmetric square root matrix of the matrix  $a(x)$ .

The construction of Markov solutions to the SDE (33) with generator (15) is possible if b and  $\sigma$  are globally Lipschitz with linear growth [13, Th.5.2.9], or if  $b$  and  $a$  are bounded and continuous functions [13, Th.5.4.22]. In the second case, the SDE has a solution in a weaker sense. Uniqueness (at least in law) and the strong Markov property hold if  $b$  and  $\sigma$  are locally Lipschitz [13, Th.5.2.5], or if b and a are Hölder continuous and the matrix  $a$  is uniformly positive definite [13, Rmk.5.4.30, Th.5.4.20]. In the one-dimensional case, existence and uniqueness for the SDE (32) can be proved under weaker assumptions [13, Sec.5.5].

In all these cases, the Markov property allows one to identify the SDE  $(33)$  with its generator  $(15)$ . This will allow us to make the link between parabolic PDEs and the corresponding SDE in the section "Parabolic PDEs Associated to Markov Processes" and sequel.

Similarly, one can associate to the time-inhomogeneous SDE

$$dX_t = b(t, X_t) dt + \sigma(t, X_t) dB_t \qquad (34)$$

the time-inhomogeneous generators (28). Existence for this SDE holds if  $b_i$  and  $\sigma_{ij}$  are globally Lipschitz in x and locally bounded (uniqueness holds if  $b_i$  and  $\sigma_{ij}$  are only locally Lipschitz in x). As earlier, in this case, a solution to equation (34) is strong Markov. We refer the reader to  $[16]$  for more details.

Example 4 Backward Stochastic Differential **Equations Backward** stochastic differential **equations** are SDEs where a random variable is given as a terminal condition. Let us motivate the definition of a backward SDE (BSDE) by continuing the study of the elementary example of the introduction of this article.

Consider an asset  $S_t$  modeled by the Black-Scholes SDE (32) and assume that it is possible to borrow and lend cash at a constant risk-free interest rate  $r$ . A self-financed trading strategy is determined by an initial portfolio value and the amount  $\pi_t$  of the portfolio value placed in the risky asset at time  $t$ . Given the stochastic process  $(\pi_t, t \ge 0)$ , the portfolio value  $V_t$  at time t solves the SDE

$$dV_t = rV_t dt + \pi_t(\mu - r) dt + \sigma \pi_t dB_t \qquad (35)$$

where  $B$  is the Brownian motion driving the dynamics (32) of the risky asset  $S$ .

Assume that this portfolio serves to hedge a call option with strike  $K$  and maturity  $T$ . This problem can be expressed as finding a couple of processes  $(V_t, \pi_t)$  adapted to the Brownian filtration  $\mathcal{F}_t =$  $\sigma(B_s, s \leq t)$  such that

$$V_t = (S_T - K)^+ - \int_t^T (rV_s + \pi_s(\mu - r)) \, \mathrm{d}s$$
$$- \int_t^T \sigma \pi_s \, \mathrm{d}B_s \tag{36}$$

Such SDEs with terminal condition and with unknown process driving the Brownian integral are called *BSDEs*. This particular BSDE admits a unique solution (see the section "Quasi- and Semilinear PDEs and BSDEs") and can be explicitly solved. Because  $V_0$  is  $\mathcal{F}_0$  adapted, it is nonrandom and therefore  $V_0$  is the usual free arbitrage price of the option. In particular, choosing  $\mu = r$ , we recover the usual formula for the free arbitrage price  $V_0 =$  $\mathbb{E}[\mathrm{e}^{-rT}(S_T-K)^+]$ , and the quantity of risky asset  $\pi_t/S_t$  in the portfolio is given by the Black–Scholes  $\Delta$ -hedge  $\partial u/\partial x(t, S_t)$ , where  $u(t, x)$  is the solution of the Black–Scholes PDE (*see* **Exchange Options**)

$$\begin{cases}\n\frac{\partial u}{\partial t} + rx\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}x^2\frac{\partial^2 u}{\partial t^2} - ru = 0\\
\forall (t, x) \in [0, T) \times (0, +\infty)\\
u(T, x) = f(x) \qquad \qquad \forall x \in (0, +\infty)\n\end{cases}\n$$
(37)

Applying Itô formula to  $u(t, S_t)$ , an elementary computation shows that  $u(t, S_t)$  solves the same SDE (35) with  $\mu = r$  as  $V_t$ , with the same terminal condition. Therefore, by uniqueness,  $V_t = u(t, S_t)$ .

Usually, for more general BSDEs,  $(\pi_t, t \ge 0)$  is an implicit process given by the martingale representation theorem. In the section "Quasi- and Semilinear PDEs and BSDEs", we give results on the existence and uniqueness of solutions of BSDEs, and on their links with nonlinear PDEs.

#### **Discontinuous Markov Processes**

In financial models, it is sometimes natural to consider discontinuous Markov processes, for example, when one wants to take into account jumps in prices. This can sometimes be done by modeling the dynamics using **Poisson processes**, **Lévy processes** or other jump processes (see Jump Processes). In particular, it is possible to define SDEs where the Brownian motion is replaced by a Lévy process (see CGMY model, NIG model, or Generalized **hyperbolic model** for examples). In this situation, the generator is an integro-differential operator and the parabolic PDE is replaced by Partial integrodifferential Equations.

## **Dimension of the State Space**

In many pricing/hedging problems, the dimension of the pricing PDE is greater than the state space of the underlyings. In such cases, the financial problem is apparently related to non-Markov stochastic processes. However, it can usually be expressed in terms of Markov processes if one increases the dimension of the process considered. For example, in the context of Markov short rates  $(r_t, t \ge 0)$ , the pricing of a **zero-coupon bond** is expressed in terms of the process  $R_t = \int_0^t r_s \, ds$  which is not Markovian, whereas the couple  $(r_t, R_t)$  is Markovian. For Asian options on a Markov asset, the couple formed by the asset and its integral is Markovian. If the asset involves a stochastic volatility solution to a SDE (see Heston **model** and **SABR** model), then the couple formed by the asset value and its volatility is Markov. As mentioned earlier, another important example is given by time-inhomogeneous Markov processes that become time homogeneous when one considers the couple formed by the current time and the original process.

In some cases, the dimension of the system can be reduced while preserving the Markovian nature of the problem. In the case of the portfolio management of multidimensional Black-Scholes prices with deterministic volatility matrix, mean return vector and interest rate, the dimension of the problem is actually reduced to one (see **Merton problem**). When the volatility matrix, the mean return vector, and the interest rate are Markov processes of dimension  $d'$ , the dimension of the problem is reduced to  $d' + 1$ .

# **Parabolic PDEs Associated to Markov** Processes

Computing the value of any future claim with fixed maturity (for example, the price of an European option on an asset solution to a SDE), or solving an optimal portfolio management problem, amounts to solve a parabolic second-order PDE, that is a PDE of the form

$$\frac{\partial u}{\partial t}(t,x) + L_t u(t,x)$$
  
=  $f(t,x,u(t,x), \nabla u(t,x)), \quad (t,x) \in \mathbb{R}_+ \times \mathbb{R}^d$   
(38)

where  $\nabla u(t, x)$  is the gradient of  $u(t, x)$  with respect to x and the linear differential operators  $L_t$  has the form equation  $(28)$ .

The goal of this section is to explain the links between these PDEs and the original diffusion process, or some intermediate Markov process. We will distinguish between *linear* parabolic PDEs, where the function  $f(t, x, y, z)$  does not depend on z and is linear in y, semilinear parabolic PDEs, where the function  $f(t, x, y, z)$  does not depend on z but is nonlinear in  $y$ , and *quasi-linear* parabolic PDEs, where the function  $f(t, x, y, z)$  is nonlinear in  $(y, z)$ . We will also discuss the links between diffusion processes and some fully nonlinear PDEs (Hamilton-Jacobi-Bellman (HJB) equations or variational inequalities) of the form

$$F\left(t, \frac{\partial u}{\partial t}(t, x), u(t, x), \nabla u(t, x), Hu(t, x)\right) = 0,$$
  
$$(t, x) \in \mathbb{R}_+ \times \mathbb{R}^d \tag{39}$$

for some nonlinear function  $F$ , where  $Hu$  denotes the Hessian matrix of  $u$  with respect to the space variable  $x$ .

Such problems involve several notions of solutions discussed in the literature (see viscosity solution). In the sections "Brownian Motion, Ornstein-Uhlenbeck Process, and the Heat Equation" and "Linear Case", we consider *classical solutions*, that is, solutions that are continuously differentiable with respect to the time variable, and twice continuously differentiable with respect to the space variables. In the sections "Ouasi- and Semilinear PDEs and BSDEs" and "Optimal Control, Hamilton-Jacobi-Bellman Equations, and Variational Inequalities", because of the nonlinearity of the problem, classical solutions may not exist, and one must consider the weaker notion of viscosity solutions.

In the section "Brownian Motion, Ornstein-Uhlenbeck Process, and the Heat Equation", we consider heat-like equations where the solution can be explicitly computed. The section "Linear Case" deals with linear PDEs, the section "Ouasi- and Semilinear PDEs and BSDEs" deals with quasi- and semilinear PDEs and their links with BSDEs, and the section "Optimal Control, Hamilton-Jacobi-Bellman Equations, and Variational Inequalities" deals with optimal control problems.

# **Brownian Motion. Ornstein-Uhlenbeck Process, and the Heat Equation**

The *heat equation* is the first example of a parabolic PDE with basic probabilistic interpretation (for which there is no need of stochastic calculus).

$$\begin{cases} \frac{\partial u}{\partial t}(t,x) = \frac{1}{2}\Delta u(t,x), & (t,x) \in (0,+\infty) \times \mathbb{R}^d\\ u(0,x) = f(x), & x \in \mathbb{R}^d \end{cases}$$
(40)

where  $\Delta$  denotes the Laplacian operator of  $\mathbb{R}^d$ . When  $f$  is a bounded measurable function, it is well known that the solution of this problem is given by the formula

$$u(t,x) = \int_{\mathbb{R}^d} f(y)g(x;t,y) \, \mathrm{d}y \tag{41}$$

where

$$g(x;t,y) = \frac{1}{(2\pi t)^{d/2}} \exp\left(\frac{|x-y|^2}{2t}\right) \tag{42}$$

 $|\cdot|$  denotes the Euclidean norm on  $\mathbb{R}^d$ . g is often called the *fundamental solution* of the heat equation. We recognize that  $g(x; t, y)$  dy is the law of  $x + B_t$ where  $B$  is a standard  $d$ -dimensional Brownian motion. Therefore, equation (41) may be rewritten as

$$u(t,x) = \mathbb{E}[f(x+B_t)] \tag{43}$$

which provides a simple probabilistic interpretation of the solution of the heat equation in  $\mathbb{R}^d$  as a particular case of equation  $(18)$ . Note that equation  $(40)$  involves the infinitesimal generator of the Brownian motion  $(1/2)\Delta$ .

Let us mention two other cases where the link between PDEs and stochastic processes can be done without stochastic calculus. The first one is the Black-Sholes model, solution to the SDE

$$dS_t = S_t(\mu \, dt + \sigma \, dB_t) \tag{44}$$

When  $d = 1$ , its infinitesimal generator is  $Lf(x) =$  $\mu x f'(x) + (\sigma^2/2) x^2 f''(x)$  and its law at time t when  $S_0 = x$  is  $l(x; t, y)$  dy where

$$l(x;t,y) = \frac{1}{\sigma y \sqrt{2\pi t}}$$
$$\times \exp\left[-\frac{1}{2\sigma^2 t} \left(\log\frac{y}{x} - \left(\mu - \frac{\sigma^2}{2}\right)t\right)^2\right]$$
(45)

Then, for any bounded and measurable  $f$ , elementary computations show that

$$u(t,x) = \int_0^\infty f(y)l(x;t,y) \, \mathrm{d}y \tag{46}$$

satisfies

$$\begin{cases}\n\frac{\partial u}{\partial t}(t,x) = Lu(t,x), & (t,x) \in (0,+\infty)^2 \\
u(0,x) = f(x), & x \in (0,+\infty)\n\end{cases}\n$$
(47)

Here again, this formula gives immediately the probabilistic interpretation

$$u(t,x) = \mathbb{E}[f(S_t) \mid S_0 = x] \tag{48}$$

The last example is the **Ornstein-Uhlenbeck** process in  $\mathbb{R}$ 

$$dX_t = \beta X_t dt + \sigma dB_t \tag{49}$$

with  $\beta \in \mathbb{R}$ ,  $\sigma > 0$  and  $X_0 = x$ . The infinitesimal generator of this process is  $Af(x) = \beta x f'(x) +$  $(\sigma^2/2) f''(x)$ . It can be easily checked that  $X_t$  is a Gaussian random variable with mean  $x \exp(\beta t)$  and variance  $\sigma^2(\exp(2\beta t) - 1)/2\beta$  with the convention that  $(\exp(2\beta t) - 1)/2\beta = t$  if  $\beta = 0$ . Therefore, its probability density function is given by

$$h(x;t,y) = \sqrt{\frac{\beta}{\sigma^2 \pi (\exp(2\beta t) - 1)}}$$

$$\times \exp\left[-\frac{2\beta(y-x\exp(\beta t))^2}{\sigma^2(\exp(2\beta t)-1)}\right] \quad (50)$$

Then, for any bounded and measurable  $f$ ,

$$u(t,x) = \int_{\mathbb{R}} f(y)h(x;t,y) \, \mathrm{d}y = \mathbb{E}[f(X_t) \mid X_0 = x]$$
(51)

is solution of

$$\begin{cases} \frac{\partial u}{\partial t}(t,x) = Au(t,x), & (t,x) \in (0,+\infty) \times \mathbb{R} \\ u(0,x) = f(x), & x \in \mathbb{R} \end{cases}$$
(52)

## **Linear Case**

The probabilistic interpretations of the previous PDEs can be generalized to a large class of linear parabolic PDEs with arbitrary second-order differential operator, interpreted as the infinitesimal generator of a Markov process. Assume that the vector  $b(t, x) \in \mathbb{R}^d$ and the  $d \times r$  matrix  $\sigma(t, x)$  are uniformly bounded and locally Lipschitz functions on  $[0,T] \times \mathbb{R}^d$  and consider the SDE in  $\mathbb{R}^d$ 

$$dX_t = b(t, X_t) dt + \sigma(t, X_t) dB_t \qquad (53)$$

where  $B$  is a standard r-dimensional Brownian motion. Set  $a = \sigma \sigma'$  and assume also that the  $d \times d$ matrix  $a(t, x)$  is uniformly Hölder and satisfies the uniform ellipticity condition: there exists  $\gamma > 0$  such that for all  $(t, x) \in [0, T] \times \mathbb{R}^d$  and  $\xi \in \mathbb{R}^d$ ,

$$\sum_{i,j=1}^{d} a_{ij}(t,x)\xi_{i}\xi_{j} \ge \gamma |\xi|^{2} \tag{54}$$

Let  $(L_t)_{t\geq 0}$  be the family of time-inhomogeneous infinitesimal generators of the Feller diffusion  $X_t$ solution to the SDE (53), given by equation (28). Consider the Cauchy problem

$$\begin{cases}\n\frac{\partial u}{\partial t}(t,x) + L_t u(t,x) \\
+c(t,x)u(t,x) = f(t,x), \quad (t,x) \in [0,T) \times \mathbb{R}^d \\
u(T,x) = g(x), \quad x \in \mathbb{R}^d\n\end{cases} \tag{55}$$

where  $c(t, x)$  is uniformly bounded and locally Hölder on  $[0, T] \times \mathbb{R}^d$ ,  $f(t, x)$  is locally Hölder on  $[0,T] \times \mathbb{R}^d$ ,  $g(x)$  is continuous on  $\mathbb{R}^d$  and

$$|f(t,x)| + |g(x)| \le A \exp(a|x|),$$
  

$$\forall (t,x) \in [0,T] \times \mathbb{R}^d$$
(56)

for some constants  $A, a > 0$ . Under these conditions, it follows easily from Theorems  $6.4.5$  and  $6.4.6$ of [10] that equation (55) admits a unique classical solution  $u$  such that

$$|u(t,x)| \le A' \exp(a|x|) \quad \forall (t,x) \in [0,T] \times \mathbb{R}^d$$
(57)

for some constant  $A' > 0$ .

The following result is known as Feynman-Kac *formula* and can be deduced from equation  $(57)$ using exactly the same method as for  $[10, Th.6.5.3]$ and using the fact that, under our assumptions, has finite exponential moments  $X_{\cdot}$  $[10, Th.6.4.5].$ 

**Theorem 4** Under the previous assumptions, the solution of the Cauchy problem  $(55)$  is given by

$$u(t,x) = \mathbb{E}\left[g(X_T)\exp\left(\int_t^T c(s,X_s)\,\mathrm{d}s\right) \mid X_t = x\right]$$
$$-\mathbb{E}\left[\int_t^T f(s,X_s)\right]$$
$$\times \exp\left(\int_t^s c(\alpha,X_\alpha)\,\mathrm{d}\alpha\right)\,\mathrm{d}s \mid X_t = x\right]$$
(58)

Let us mention that this result can be extended to parabolic linear PDEs on bounded domains [10, Th.6.5.2] and to elliptic linear PDEs on bounded domains [10, Th.6.5.1].

Example 5 European Options The Feynman-Kac formula has many applications in finance. Let us consider the case of an European option on a one-dimensional Markov asset  $(S_t, t \ge 0)$  with payoff  $g(S_u, 0 \le u \le T)$ . The free arbitrage value at time t of this option is

$$V_t = \mathbb{E}[\mathrm{e}^{-r(T-t)}g(S_u, t \le u \le T) \mid \mathcal{F}_t] \tag{59}$$

By the Markov property (1), this quantity only depends on  $S_t$  and  $t$  [10, Th.2.1.2]. The Feynman-Kac formula (58) allows one to characterize  $V$  in the case where  $g$  depends only on  $S_T$  and  $S$  is a Feller diffusion.

Most often, the asset SDE

$$dS_t = S_t(\mu(t, S_t) dt + \sigma(t, S_t) dB_t)$$
(60)

cannot satisfy the uniform ellipticity assumption (54) in the neighborhood of 0. Therefore, Theorem 4 does not apply directly. This is a general difficulty for financial models. However, in most cases (and in all the examples below), it can be overcome by taking the logarithm of the asset price. In our case, we assume that the process  $(\log S_t, 0 \le t \le T)$  is a Feller diffusion on  $\mathbb{R}$  with time-inhomogeneous generator

$$L_t \phi(y) = \frac{1}{2} a(t, y) \phi''(y) + b(t, y) \phi'(y) \tag{61}$$

that satisfy the assumptions of Theorem 4. This holds for example for the Black-Scholes model (32). This assumption implies that  $S$  is a Feller diffusion on  $(0, +\infty)$  whose generator takes the form

$$\tilde{L}_t \phi(x) = \frac{1}{2} \tilde{a}(t, x) x^2 \phi''(x) + \tilde{b}(t, y) x \phi'(x) \quad (62)$$

where  $\tilde{a}(t, x) = a(t, \log x)$  and  $\tilde{b}(t, x) = b(t, \log x) +$  $a(t, \log x)/2$ .

Assume also that  $g(x)$  is continuous on  $\mathbb{R}_+$ with polynomial growth when  $x \to +\infty$ . Then, by Theorem 4, the function

$$v(t, y) = \mathbb{E}\left[e^{-r(T-t)}g(S_T) \mid \log S_t = y\right] \qquad (63)$$

is solution to the Cauchy problem

$$\begin{cases} \frac{\partial v}{\partial t}(t, y) + L_t v(t, y) \\ -rv(t, y) = 0, \end{cases} \quad (t, y) \in [0, T) \times \mathbb{R}_{(64)}$$

Making the change of variable  $x = \exp(y), u(t, x) =$  $v(t, \log x)$  is solution to

It is straightforward to check that  $(S, A)$  is a Feller diffusion on  $(0, +\infty)^2$  with infinitesimal generator

$$\begin{cases}\n\frac{\partial u}{\partial t}(t,x) + \tilde{b}(t,x)x\frac{\partial u}{\partial x}(t,x) + \frac{1}{2}\tilde{a}(t,x)x^2\frac{\partial^2 u}{\partial x^2}(t,x) - rv(t,x) = 0, & (t,x) \in [0,T) \times (0,+\infty) \\
u(T,x) = g(x), & x \in (0,+\infty)\n\end{cases} \tag{65}$$

and  $V_t = u(t, S_t)$ . The Black-Scholes PDE (37) is a particular case of this result.

**Example 6** An Asian Option We give an example of a path-dependent option for which the uniform ellipticity condition of the matrix  $a$  does not hold. An Asian option is an option where the payoff is determined by the average of the underlying price over the period considered. Consider the Asian call option

$$\left(\frac{1}{T}\int_0^T S_u \, \mathrm{d}u - K\right)^+ \tag{66}$$

on a Black–Scholes asset  $(S_t, t \ge 0)$  following

$$dS_t = r S_t dt + \sigma S_t dB_t \tag{67}$$

$$\begin{cases} \frac{\partial u}{\partial t} + \frac{\sigma^2}{2} x^2 \frac{\partial^2 u}{\partial x^2} + rx \frac{\partial u}{\partial x} + \frac{1}{T} x \frac{\partial u}{\partial y} - ru = 0, \\ u(T, x, y) = (y/T - K)^+, \end{cases}$$

where  $B$  is a standard one-dimensional Brownian motion. The free arbitrage price at time  $t$  is

$$\mathbb{E}\left[e^{-r(T-t)}\left(\frac{1}{T}\int_{0}^{T}S_{u}\,\mathrm{d}u-K\right)^{+}\middle|\,S_{t}\right] \qquad (68)$$

To apply the Feynman-Kac formula, one must express this quantity as the (conditional) expectation

$$Lf(x, y) = rx \frac{\partial f}{\partial x}(x, y) + \frac{\sigma^2}{2} x^2 \frac{\partial^2 f}{\partial x^2}(x, y) + \frac{1}{T} x \frac{\partial f}{\partial y}(x, y)$$
(70)

Although considering the change of variable ( $\log S$ ,  $A$ ), Theorem 4 does not apply to this process because the infinitesimal generator is degenerated (without second-order derivative in  $\nu$ ). Formally, the Feynman-Kac formula would give that

$$u(t, x, y)$$
  
:=  $\mathbb{E}[e^{-r(T-t)}(A_T/T - K)^{+} | S_t = x, A_t = y]$   
(71)

is solution to the PDE

$$(t, x, y) \in [0, T) \times (0, +\infty) \times \mathbb{R}$$
  
$$(x, y) \in (0, +\infty) \times \mathbb{R}$$
  
$$(72)$$

Actually, it is possible to justify the previous statement in the specific case of a one-dimensional Black-Scholes asset:  $\mu$  can be written as

$$u(t, x, y) = e^{-r(T-t)}x \varphi\left(t, \frac{KT-y}{x}\right) \qquad (73)$$

(see [20]) where  $\varphi(t, z)$  is the solution of the onedimensional parabolic PDE

$$\begin{cases} \frac{\partial\varphi}{\partial t}(t,z) + \frac{\sigma^2}{2}z^2\frac{\partial^2\varphi}{\partial z^2}(t,z) - \left(\frac{1}{T} + rz\right)\frac{\partial\varphi}{\partial z}(t,z) + r\varphi(t,z) = 0, & (t,z)\in[0,T)\times\mathbb{R} \\ \varphi(T,z) = -(z)^+/T, & z\in\mathbb{R} \end{cases} \tag{74}$$

of the value at time  $T$  of some Markov quantity. This can be done by introducing the process

$$A_t = \int_0^t S_u \, \mathrm{d}u, \quad 0 \le t \le T \tag{69}$$

From this, it is easy to check that  $u$  solves equation (72).

Note that this relies heavily on the fact that the underlying asset follows the Black-Scholes model. As far as we know, no rigorous justification of Feynman-Kac formula is available for Asian options on more general assets.

### **Ouasi- and Semilinear PDEs and BSDEs**

The link between quasi- and semilinear PDEs and BSDEs is motivated by the following formal argument. Consider the semilinear PDE

$$\begin{cases} \frac{\partial u}{\partial t}(t,x) + L_t u(t,x) = f(u(t,x)) \\ & (t,x) \in (0,T) \times \mathbb{R} \\ u(T,x) = g(x) & x \in \mathbb{R} \end{cases}$$
(75)

where  $(L_t)$  is the family of infinitesimal generators of a time-inhomogeneous Feller diffusion  $(X_t, t \ge 0)$ . Assume that this PDE admits a classical solution  $u(t, x)$ . Assume also that we can find a unique adapted process  $(Y_t, 0 \le t \le T)$  such that

$$Y_{t} = \mathbb{E}[g(X_{T}) - \int_{t}^{T} f(Y_{s}) \, \mathrm{d}s \mid \mathcal{F}_{t}] \quad \forall t \in [0, T]$$

$$(76)$$

Now, by Itô's formula applied to  $u(t, X_t)$ ,

$$u(t, X_t) = \mathbb{E}[g(X_T) - \int_t^T f(u(s, X_s)) \, \mathrm{d}s \mid \mathcal{F}_t]$$
(77)

Therefore,  $Y_t = u(t, X_t)$  and the stochastic process  $Y$  provides a probabilistic interpretation of the solutionof the PDE (75). Now, by the martingale decomposition theorem, if  $Y$  satisfies (76), there exists an adapted process  $(Z_t, 0 \le t \le T)$  such that

$$Y_t = g(X_T) - \int_t^T f(Y_s) \, \mathrm{d}s$$
$$- \int_t^T Z_s \, \mathrm{d}B_s \quad \forall t \in [0, T] \tag{78}$$

solution of the SDE  $dY_t = f(Y_t) dt + Z_t dB_t$  with *terminal* condition  $Y_T = g(X_T)$ .

The following definition of a BSDE generalizes the previous situation. Given functions  $b_i(t, x)$  and  $\sigma_{ii}(t, x)$  that are globally Lipschitz in x and locally bounded  $(1 \le i, j \le d)$  and a standard *d*-dimensional Brownian motion  $B$ , consider the unique solution  $X$ of the time-inhomogeneous SDE

$$dX_t = b(t, X_t) dt + \sigma(t, X_t) dB_t \qquad (79)$$

with initial condition  $X_0 = x$ . Consider also two functions  $f: [0, T] \times \mathbb{R}^d \times \mathbb{R}^k \times \mathbb{R}^{k \times d} \to \mathbb{R}^k$  and  $g: \mathbb{R}^d \to \mathbb{R}^k$ . We say that  $((Y_t, Z_t), t > 0)$  solve the BSDE

$$dY_t = f(t, X_t, Y_t, Z_t) dt + Z_t dB_t \qquad (80)$$

with terminal condition  $g(X_T)$  if Y and Z are progressively measurable processes with respect to the Brownian filtration  $\mathcal{F}_t = \sigma(B_s, s \leq t)$  such that, for any  $0 \le t \le T$ ,

$$Y_t = g(X_T) - \int_t^T f(s, X_s, Y_s, Z_s) \, \mathrm{d}s - \int_t^T Z_s \, \mathrm{d}B_s \tag{81}$$

Example 4 corresponds to  $g(x) = (x - K)^{+}$ ,  $f(t, x, y, z) = -ry + z(\mu - r)/\sigma$  and  $Z_t = \sigma \pi_t$ . Note that the role of the implicit unknown process Z is to make Y adapted.

The existence and uniqueness of  $(Y, Z)$  solving equation (81) hold under the assumptions that  $g(x)$  is continuous with polynomial growth in x,  $f(t, x, y, z)$ is continuous with polynomial growth in  $x$  and linear growth in y and z, and f is uniformly Lipschitz in y and  $z$ . Let us denote by (A) all these assumptions. We refer to [17] for the proof of this result and the general theory of BSDEs (see also forwardbackward SDEs).

Consider the quasi-linear parabolic PDE

$$\begin{cases}\n\frac{\partial u}{\partial t}(t,x) + L_t u(t,x) = f(t,x,u(t,x), \nabla_x u(t,x)\sigma(t,x)), & (t,x) \in (0,T) \times \mathbb{R}^d \\
u(T,x) = g(x), & x \in \mathbb{R}^d\n\end{cases} \tag{82}$$

where  $B$  is the same Brownian motion as the one driving the Feller diffusion  $X$ . In other words,  $Y$  is

The following results give the links between the BSDE (80) and the PDE (82).

**Theorem 5** ([15], Th.4.1). Assume that  $b(t, x)$ ,  $\sigma(t, x)$ ,  $f(t, x, y, z)$ , and  $g(x)$  are continuous and dif*ferentiable with respect to the space variables*  $x, y, z$ with uniformly bounded derivatives. Assume also that b,  $\sigma$ , and f are uniformly bounded and that  $a = \sigma \sigma'$ is uniformly elliptic. Then equation (82) admits a unique classical solution u and

$$Y_t = u(t, X_t) \quad and \quad Z_t = \nabla_x u(t, X_t) \sigma(t, X_t) \quad (83)$$

**Theorem 6** ([17], Th.2.4). Assume  $(A)$  and that  $b(t, x)$  and  $\sigma(t, x)$  are globally Lipschitz in x and locally bounded. Define the function  $u(t,x) = Y_t^{t,x}$ , *where*  $Y^{t,x}$  *is the solution to the BSDE* (82) *on the time* interval  $[t, T]$ , where X is solution to the SDE (79) with initial condition  $X_t = x$ . Then u is a viscosity solution of equation (82).

Theorem 5 gives an interpretation of the solution of a BSDE in terms of the solution of a quasilinear PDE. In particular, in Example 4, it gives the usual interpretation of the hedging strategy  $\pi_t =$  $Z_t/\sigma$  as the  $\Delta$ -hedge of the option price. Note also that Theorem 5 implies that the process  $(X, Y, Z)$ is Markov—a fact which is not obvious from the definition. Conversely, Theorem 6 shows how to construct a viscosity solution of a quasi-linear PDE from BSDEs.

BSDEs provide an indirect tool to compute quantities related to a solution  $X$  of the SDE (such as the hedging price and strategy of an option based on the process  $X$ ). BSDEs also have links with general stochastic control problems, that we will not mention (see BSDEs). Here, we give an example of application to the pricing of an American put option.

Example 7 Pricing of an American Put Option Consider a Black-Scholes underlying asset  $S$  and assume for simplicity that the risk-free interest rate  $r$  is zero. The price of an **American put option** on  $S$  with strike  $K$  and maximal exercise policy  $T$  is given by

$$\sup_{0 \le \tau \le T} \mathbb{E}^*[(K - S_\tau)^+] \tag{84}$$

where  $\tau$  is a stopping time and where  $\mathbb{P}^*$  is the riskneutral probability measure, under which the process S is simply a Black-Scholes asset with zero drift.

In the case of an European put option, the price is given by the solution of the BSDE

$$Y_{t} = (K - S_{T})^{+} - \int_{t}^{T} Z_{s} \, \mathrm{d}B_{s} \tag{85}$$

by a similar argument as in Example 4. In the case of an American put option, the price at time t is necessarily bigger than  $(K - S_t)^+$ . It is therefore natural to include this condition by considering the BSDE (85) reflected on the obstacle  $(K-S_t)^+$ . Mathematically, this corresponds to the problem of finding adapted processes  $Y$ ,  $Z$ , and  $R$ such that

$$Y_{t} = (K - S_{T})^{+} - \int_{t}^{T} Z_{s} dB_{s} + R_{T} - R_{t}$$
  

$$Y_{t} \geq (K - S_{t})^{+}$$
  
*R* is continuous, increasing,  $R_{0} = 0$  and  

$$\int_{0}^{T} [Y_{t} - (K - S_{t})^{+}] dR_{t} = 0$$
(86)

The process R increases only when  $Y_t = (K - S_t)^+$ in such a way that  $Y$  cannot cross this obstacle. The existence of a solution of this problem is a particular case of general results, (see [7]). As a consequence of the following theorem, this reflected BSDE gives a way to compute the price of the American put option.

**Theorem 7** ([7], Th.7.2). *The American put option* has the price  $Y_0$ , where  $(Y, Z, R)$  solves the reflected BSDE (86).

The essential argument of the proof is the following. Fix  $t \in [0, T)$  and a stopping time  $\tau \in [t, T]$ . Since

$$Y_{\tau} - Y_{t} = R_{t} - R_{\tau} + \int_{t}^{\tau} Z_{s} \, \mathrm{d}B_{s} \qquad (87)$$

and because R is increasing,  $Y_t = \mathbb{E}^*[Y_\tau + R_\tau R_t \mid \mathcal{F}_t \ge \mathbb{E}^*[(K - S_\tau)^+ \mid \mathcal{F}_t]$ . Conversely, if  $\tau_t^* =$  $\inf\{u \in [t, T] : Y_u = (K - S_u)^+\}\text{, because } Y > (K - S_u)^{-1}$  $(S)^+$  on  $[t, \tau_t^*)$ ,  $R$  is constant on this interval and

$$Y_{t} = \mathbb{E}^{*}[Y_{\tau_{t}^{*}} + R_{\tau_{t}^{*}} - R_{t} \mid \mathcal{F}_{t}] = \mathbb{E}^{*}[(K - S_{\tau_{t}^{*}})^{+}]$$
(88)

Therefore,

$$Y_t = \underset{t \le \tau \le T}{\text{ess sup}} \quad \mathbb{E}^*[(K - S_\tau)^+ \mid \mathcal{F}_t] \tag{89}$$

which gives another interpretation for the solution  $Y$ of the reflected BSDE. Applying this for  $t = 0$  yields  $Y_0 = \sup_{\tau < T} \mathbb{E}^*[(K - S_\tau)^+]$  as stated.

Moreover, as shown by the previous computation, the process  $Y$  provides an interpretation of the optimal exercise policy as the first time where  $Y$  hits the obstacle  $(K - S)^+$ . This fact is actually natural from equation  $(89)$ ; the optimal exercise policy is the first time where the current payoff equals the maximal future expected payoff.

As it will appear in the next section, as the solution of an optimal stopping problem, if  $S_0 = x$ , the price of this American put option is  $u(0, x)$ , where u is the solution of the nonlinear PDE

## Optimal Control,

# Hamilton-Jacobi-Bellman Equations, and Variational Inequalities

We discuss only two main families of stochastic **control problems:** finite horizon and the optimal stopping problems. Other classes of optimal problems appearing in finance are mentioned in the end of this section.

#### Finite Horizon Problems

The study of optimal control problems with finite horizon is motivated, for example, by the ques-

$$\begin{cases}\n\min\left\{u(t,x) - (K-x)^+; -\frac{\partial u}{\partial t}(t,x) - \frac{\sigma^2}{2}x^2\frac{\partial^2 u}{\partial x^2}u(t,x)\right\} = 0, & (t,x) \in (0,T) \times (0,+\infty) \\
u(T,x) = (K-x)^+, & x \in (0,+\infty)\n\end{cases} \tag{90}$$

Therefore, similarly as in Theorem 6, the reflected BSDE (84) provides a probabilistic interpretation of the solution of this PDE.

The (formal) essential argument of the proof of this result can be summarized as follows (for details, see [14, Section V.3.1]). Consider the solution  $u$  of equation (90) and apply Itô's formula to  $u(t, S_t)$ . Then, for any stopping time  $\tau \in [0, T]$ ,

$$u(0,x) = \mathbb{E}[u(\tau, S_{\tau})] - \mathbb{E}\bigg[\int_{0}^{\tau} \bigg(\frac{\partial u}{\partial t}(t, S_{t}) + \frac{\sigma^{2}}{2}S_{t}^{2}\frac{\partial^{2} u}{\partial x^{2}}u(t, S_{t})\bigg) \mathrm{d}s\bigg]$$
(91)

Because u is solution of equation (90),  $u(0, x) \ge$  $\mathbb{E}[u(\tau, S_{\tau})] \ge \mathbb{E}[(K - S_{\tau})^{+}]. \quad \text{Hence,} \quad u(0, x) \ge$  $\sup_{0 \le \tau \le T} \mathbb{E}[(K - S_{\tau})^{+}].$ <br>Conversely, if  $\tau^{*} = \inf\{0 \le t \le T : u(s, S_{s}) =$ 

 $(K-S_s)^{+}$ , then

$$\frac{\partial u}{\partial t}(t, S_t) + \frac{\sigma^2}{2} S_t^2 \frac{\partial^2 u}{\partial x^2} u(t, S_t) = 0 \quad \forall t \in [0, \tau^*]$$
(92)

Therefore, for  $\tau = \tau^*$ , all the inequalities in the previous computation are equalities and  $u(0, x) =$  $\sup_{0 < \tau < T} \mathbb{E}[(K - S_{\tau})^+].$ 

tions of portfolio management, quadratic hedging of options, or super-hedging cost for uncertain volatility models.

Let us consider a controlled diffusion  $X^{\alpha}$  in  $\mathbb{R}^d$ solution to the SDE

$$dX_t^{\alpha} = b(X_t^{\alpha}, \alpha_t) dt + \sigma(X_t^{\alpha}) dB_t \qquad (93)$$

where  $B$  is a standard r-dimensional Brownian motion and the control  $\alpha$  is a given progressively measurable process taking values in some compact metric space A. Such a control is called *admissible*. For simplicity, we consider the time-homogeneous case and we assume that the control does not act on the diffusion coefficient  $\sigma$  of the SDE. Assume that  $b(x, a)$  is bounded, continuous, and Lipschitz in the variable x, uniformly in  $a \in A$ . Assume also that  $\sigma$  is Lipschitz and bounded. For any  $a \in A$ , we introduce the linear differential operator

$$L^{a}\varphi = \frac{1}{2} \sum_{i,j=1}^{d} \left( \sum_{k=1}^{d} \sigma_{ik}(x)\sigma_{jk}(x) \right) \frac{\partial^{2}\varphi}{\partial x_{i}\partial x_{j}} + \sum_{i=1}^{d} b_{i}(x,a) \frac{\partial\varphi}{\partial x_{i}}$$
(94)

which is the infinitesimal generator of  $X^{\alpha}$  when  $\alpha$  is a constant equal to  $a \in A$ .

A typical form of finite horizon optimal control problems in finance consists in computing

$$u(t, x) = \inf_{\alpha \text{ admissible}} \mathbb{E}\bigg[e^{-rT}g(X_T^{\alpha}) + \int_t^T e^{-rt}f(X_t^{\alpha}, \alpha_t) dt \mid X_t^{\alpha} = x\bigg]$$
(95)

where  $f$  and  $g$  are continuous and bounded functions and to find an optimal control  $\alpha^*$  that realizes the minimum. Moreover, it is desirable to find a Markov optimal control, that is, an optimal control having the form  $\alpha_t^* = \psi(t, X_t)$ . Indeed, in this case, the controlled diffusion  $X^{\alpha^*}$  is a Markov process.

In the case of nondegenerate diffusion coefficient, we have the following link between the optimal control problems and a semilinear PDEs.

**Theorem 8** Under the additional assumption that  $\sigma$  is uniformly elliptic, u is the unique bounded classical solution of the Hamilton-Jacobi-Bellman  $(HJB)$  equation

$$\times \mathbb{E}\bigg[\frac{\partial v}{\partial t}(t, X_t^{\alpha}) + L^{\alpha_t} v(t, X_t^{\alpha}) + r v(t, X_t^{\alpha})\bigg] \mathrm{d}s \tag{98}$$

Therefore, by equation  $(96)$ ,

$$v(0, x)$$

$$\leq \mathbb{E}\left[e^{-rT}g(X_T^{\alpha}) + \int_t^T e^{-rt}f(X_t^{\alpha}, \alpha_t) dt \mid X_t^{\alpha} = x\right]$$
(99)

for any admissible control  $\alpha$ . Now, for the Markov control  $\alpha^*$  defined in Theorem 8, all the inequalities in the previous computation are equalities. Hence  $v = u$ .

The cases where  $\sigma$  is not uniformly elliptic or where  $\sigma$  is also dependent on the current control  $\alpha_t$  are much more difficult. In both cases, it is necessary to enlarge the set of admissible control by considering *relaxed controls*, that is, controls that belong to the set  $\mathcal{P}(A)$  of probability measures on A. For such a control  $\alpha$ , the terms  $b(x, \alpha_t)$  and

$$\begin{cases} \frac{\partial u}{\partial t}(t,x) + \inf_{a \in A} \{L^a u(t,x) + f(x,a)\} - r u(t,x) = 0, & (t,x) \in (0,T) \times \mathbb{R}^d \\ u(T,x) = g(x), & x \in \mathbb{R}^d \end{cases} \tag{96}$$

*Furthermore, a Markov control*  $\alpha_t^* = \psi(t, X_t)$  *is opti*mal for a fixed initial condition  $x$  and initial time  $t = 0$  if and only if

$$L^{\psi(t,x)}u(t,x) + f(x,\psi(t,x))$$
  
= 
$$\inf_{a \in A} \{L^a u(t,x) + f(x,a)\}$$
 (97)

for almost every  $(t, x) \in [0, T] \times \mathbb{R}^d$ .

This is Theorem III.2.3 of [3] restricted to the case of precise controls (see later).

Here again, the essential argument of the proof can be easily (at least formally) written: consider any admissible control  $\alpha$  and the corresponding controlled diffusion  $X^{\alpha}$  with initial condition  $X_0 = x$ . By Itô's formula applied to  $e^{-rt}v(t,X_t^{\alpha})$ , where v is the solution of equation  $(96)$ ,

$$\mathbb{E}[\mathrm{e}^{-rT}v(T,X_T^{\alpha})] = v(0,x) + \int_0^T \mathrm{e}^{-rt}$$

 $f(x, \alpha_t)$  in equations (93) and (95) are replaced by  $\int b(x,a)\alpha_t(da)$  and  $\int f(x,a)\alpha_t(da)$ , respectively. The admissible controls of the original problem correspond to relaxed controls that are Dirac masses at each time. These are called *precise controls*.

The value  $\tilde{u}$  of this new problem is defined as in equation (95), but the infimum is taken over all progressively measurable processes  $\alpha$  taking values in  $\mathcal{P}(A)$ . It is possible to prove under general assumptions that both problems give the same value:  $\tilde{u} = u$  (cf. [3, Cor.I.2.1] or [8, Th.2.3]).

In these cases, one usually cannot prove the existence of a classical solution of equation (96). The weaker notion of **viscosity solution** is generally the correct one. In all the cases treated in the literature,  $u = \tilde{u}$  solves the same HJB equation as in Theorem 8, except that the infimum is taken over  $\mathcal{P}(A)$  instead of  $A$  (cf. [3, Th.IV.2.2] for the case without control on  $\sigma$ ). However, it is not trivial at all in general to obtain a result on precise controls from the result on relaxed controls. This is due to the fact that

usually no result is available on the existence and the characterization of a Markov-relaxed optimal control. The only examples where it has been done require restrictive assumptions (cf. [8, Cor.6.8]). However, in most of the financial applications, the value function  $u$  is the most useful information. In practice, one usually only needs to compute a control that give an expected value arbitrarily close to the optimal one.

## Optimal Stopping Problems

Optimal stopping problems arise in finance, for example, for the American options pricing (when assume that  $g(t, x)$  is differentiable with respect to  $t$  and twice differentiable with respect to  $x$ and that

$$|f(t,x)| + \left|\frac{\partial g}{\partial t}(t,x)\right| + \sum_{i=1}^{d} \left|\frac{\partial g}{\partial x_i}(t,x)\right| \le Ce^{\mu|x|}$$
(102)

for positive constants C and  $\mu$ .

**Theorem 9** ([2], Sec.III.4.9). Under the previous assumptions,  $u(t, x)$  admits first-order derivatives with respect to t and second-order derivatives with respect to x that are  $L^p$  for all  $1 \le p \le \infty$ . Moreover,  $u$  is the solution of the variational inequality

$$\begin{cases} \max\left\{u(t,x) - g(t,x); -\frac{\partial u}{\partial t}(t,x) - L_t u(t,x) + r u(t,x) - f(t,x)\right\} = 0, & (t,x) \in (0,T) \times \mathbb{R}^d\\ u(T,x) = g(T,x) & x \in \mathbb{R}^d \end{cases} \tag{103}$$

to sell a claim, an asset?) or in production models (when to extract or product a good? when to stop production?).

Let us consider a Feller diffusion  $X$  in  $\mathbb{R}^d$  solution to the SDE

$$dX_t = b(t, X_t) dt + \sigma(t, X_t) dB_t \qquad (100)$$

where  $B$  is a standard  $d$ -dimensional Brownian motion. As in equation (28), let  $(L_t)_{t>0}$  denote its family of time-inhomogeneous infinitesimal generators. Denote by  $\Pi(t, T)$  the set of stopping times valued in  $[t, T]$ .

A typical form of optimal stopping problems consists in computing

$$u(t,x) = \inf_{\tau \in \Pi(t,T)} \mathbb{E} \bigg[ e^{-r(\tau - t)} g(\tau, X_{\tau}) + \int_{t}^{\tau} e^{-r(s-t)} f(s, X_{s}) \, \mathrm{d}s \mid X_{t} = x \bigg]$$
(101)

and to characterize an optimal stopping time.

Assume that  $b(t, x)$  is bounded and continuously differentiable with bounded derivatives and that  $\sigma(t, x)$  is bounded, continuously differentiable with respect to  $t$  and twice continuously differentiable with respect to  $x$  with bounded derivatives. Assume also that  $\sigma$  is uniformly elliptic. Finally,

The proof of this result is based on a similar (formal) justification as the one we gave for equation (90). We refer to [12] for a similar result under weaker assumptions more suited to financial models when  $f = 0$  (this is in particular the case for American options).

In some cases (typically with  $f = 0$ , see [11]), it can be shown that the infimum in equation  $(101)$  is attained for the stopping time

$$\tau^* = \inf \left\{ t \le s \le T : u(s, X_s^{t,x}) = g(s, X_s^{t,x}) \right\}$$
(104)

where  $X^{t,x}$  is the solution of the SDE (100) with initial condition  $X_t^{t,x} = x$ .

### Generalizations and Extensions

An optimal control problem can also be solved through the optimization of a family of BSDEs related to the laws of the controlled diffusions. On this question, we refer to  $[19]$  and **BSDEs**.

In this section, we considered only very specific optimal control problems. Other important families of optimal control problems are given by impulse control problems, where the control may induce a jump of the underlying stochastic process, or ergodic control problems, where the goal is to optimize a quantity related to the stationary behavior of the controlled diffusion. Impulse control has applications, for example, in stock or resource management problems. In the finite horizon case, when the underlying asset follows a model with stochastic or elastic volatility or when the market is incomplete, other optimal control problems can be considered, such as characterizing the superhedging cost, or minimizing some risk measure. Various constraints can be included in the optimal control problem, such as maximizing the expectation of an utility with the constraint that this utility has a fixed volatility, or minimizing the volatility for a fixed expected utility. One can also impose Gamma constraints on the control. Another important extension of optimal control problems arises when one wants tosolve numerically an HJB equation. Usual discretization methods require to restrict to a bounded domain and to fix artificial boundary conditions. The numerical solution can be interpreted as the solution of an optimal control problem in a bounded domain. In this situation, a crucial question is to quantify the impact on the discretized solution of an error on the artificial boundary condition (which usually cannot be computed exactly).

# **On Numerical Methods**

The Feynman–Kac formula for linear PDEs allows one to use **Monte Carlo methods** to compute the solution of the PDE. They are especially useful when the solution of the PDE has to be computed at a small number of points, or when dimension is large (typically larger or equal to 4), since they provide a rate of convergence independent of the dimension.

Concerning quasi- or semilinear PDEs and some optimal control problems (e.g., American put options in the section "Quasi- and Semilinear PDEs and BSDEs"), interpretations in terms of BSDEs provide indirect Monte Carlo methods of numerical computation (see [1] for **Bermudan options** or [4, 6] for general BSDEs schemes). These methods have the advantage that they do not require to consider artificial boundary conditions. However, their speed of convergence to the exact solution is still largely unknown, and could depend on the dimension of the problem.

For high dimensional HJB equations, the analytical discretization methods lead to important numerical problems. First, these methods need to solve an optimization problem at each node of the discretization grid, which can be very costly in high dimension

or difficult depending on the particular constraints imposed on the control. Moreover, these methods require to localize the problem, that is, to solve the problem in a bounded domain with artificial boundary conditions, which are usually difficult to compute precisely. This localization problem can be solved by computing the artificial boundary condition with a Monte Carlo method based on BSDEs. However, the error analysis of this method is based on the probabilistic interpretation of HJB equations in bounded domains, which is a difficult problem in general.

# **End Notes**

a*.* A Markov semigroup family *(Pt, t* ≥ 0*)* on *<sup>d</sup>* is a family of bounded linear operators of norm 1 on the set of bounded measurable functions on *<sup>d</sup>* equipped with the *L*<sup>∞</sup> norm, which satisfies equation (8).

b*.* This is not the most general definition of Feller semigroups (see [21, Def.III.6.5]). In our context, because we only introduce analytical objects from stochastic processes, the semigroup *(Pt)* is naturally defined on the set of bounded measurable functions.

c*.* The strong continuity of a semigroup is usually defined as *Ptf* − *f* → 0 as *t* → 0 for all *f* ∈ *C*0*(<sup>d</sup> )*. However, in the case of Feller semigroups, this is equivalent to the weaker formulation (10) (see [21, Lemma III.6.7]).

# **References**

- [1] Bally, V. & Pages, G. (2003). Error analysis of the ` optimal quantization algorithm for obstacle problems, *Stochastic Processes and their Applications* **106**(1), 1–40.
- [2] Bensoussan, A. & Lions, J.-L. (1982). *Applications of Variational Inequalities in Stochastic Control*, *Studies in Mathematics and its Applications*, North-Holland Publishing, Amsterdam, Vol. 12 (Translated from the French).
- [3] Borkar, V.S. (1989). *Optimal Control of Diffusion Processes*, *Pitman Research Notes in Mathematics Series*, Longman Scientific & Technical, Harlow, Vol. 203.
- [4] Bouchard, B. & Touzi, N. (2004). Discrete-time approximation and Monte-Carlo simulation of backward stochastic differential equations, *Stochastic Processes and their Applications* **111**(2), 175–206.
- [5] ¸Cinlar, E. & Jacod, J. (1981). Representation of semimartingale Markov processes in terms of Wiener processes and Poisson random measures, in *Seminar on Stochastic Processes, 1981 (Evanston, Ill., 1981)*, *Progress in Probability and Statistics*, Birkhauser, ¨ Boston, Vol. 1, pp. 159–242.
- [6] Delarue, F. & Menozzi, S. (2006). A forward-backward stochastic algorithm for quasi-linear PDEs, *Annals of Applied Probability* **16**(1), 140–184.